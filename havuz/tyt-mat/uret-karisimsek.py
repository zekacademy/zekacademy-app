"""Karışım Problemleri · ŞEKİLLİ paket (8 soru): şekil/tablo veri taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Karışım Problemleri'
P=Parti('karisimsek','Karışım Problemleri','prob|Karışım Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu karışım soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

ORN=B('Karışım oranı','oran = maddenin miktarı ÷ karışımın toplam miktarı. Örnek: 200 mL çözeltide 50 mL madde varsa oran 50/200 = %25')
BIR=B('Karışımları birleştirme','maddeler kendi arasında, toplam miktarlar kendi arasında toplanır; yeni oran = toplam madde ÷ toplam karışım. Örnek: 100 mL %10’luk ile 100 mL %30’luk çözeltiyi karıştırırsak madde 10 + 30 = 40 mL, toplam 200 mL, oran %20')

kartla('K-KRS-01','Hacim çizgili kaplarda karışım','Kaplardaki hacimler çizgilerden okunur; her kaptaki alkol miktarı hacim × oran ile bulunur; toplam alkol toplam hacme bölünür.','Oranların aritmetik ortalamasını almak; ağırlıkları ters kullanmak; alkol hacmini oran sanmak.','kolay','hikâyeli',3,'krs-kaplar','Kaplarda karışım')
kartla('K-KRS-02','Alaşım çubuğu','Bölmeli çubukta bakırın bölme sayısı ve kütlesi bir bölmenin kütlesini verir; diğer metaller bölme sayısıyla bulunur.','Yalnız bir metali hesaplamak; bölme kütlesi yerine toplamı yazmak.','kolay','hikâyeli',3,'krs-alasim','Alaşım çubuğu')
kartla('K-KRS-03','Derişim–kütle tablosu','Her çözeltideki tuz miktarı kütle × oran ile bulunur; toplam tuz toplam kütleye oranlanıp bilinmeyen oran çözülür.','Oranları ağırlıksız ortalamak; tuz miktarını oran sanmak.','orta','tablo',4,'krs-tablo','Derişim tablosu')
kartla('K-KRS-04','Kaplar arası aktarım','İki çözeltinin karışımında oranlar arası farklar, hacimlerin ters oranını verir; aktarılan hacim denklemle bulunur.','Farkları ters kurmak; B’nin kendi hacmini hesaba katmamak.','orta','hikâyeli',4,'krs-aktarim','Kaplar arası aktarım')
kartla('K-KRS-05','İki depodan karışım düzeneği','Debi × süre ile akıtılan hacimler bulunur; alkol miktarı toplanır; eklenen saf su yalnız toplam hacmi büyütür.','Eklenen suyu hesaba katmamak; yüzde puanı çıkarmak; oranların ortalamasını almak.','orta','hikâyeli',4,'krs-akis','Depolardan karışım')
kartla('K-KRS-06','Ağzına kadar doldurma','Kapta kalan boşluk, ölçek çizgilerinden bulunur; eklenen çözeltinin alkol miktarı toplanıp tüm kapasiteye bölünür.','Eklenen hacmi yanlış almak; ağırlıkları ters kullanmak.','orta','hikâyeli',4,'krs-doldur','Kabı doldurma')
kartla('K-KRS-07','Ayar çubuğu','Ayar, 24 bölmede altın bölme sayısıdır; bakır miktarı değişmeyeceğinden yeni ayardan toplam kütle bulunur.','Altını değil bakırı sabit sanmamak; ayarları kütle oranı gibi kullanmak.','zor','hikâyeli',4,'krs-ayar','Ayar ve alaşım')
kartla('K-KRS-08','Üç çözelti tablosu','Tablodaki üç çözeltinin madde miktarları a cinsinden yazılır; toplam miktar denklemle bilinmeyen hacmi verir.','Saf suyu hesaba katmamak; denklemi hatalı kurmak.','orta','tablo',4,'krs-tablo2','Üç çözelti ve bilinmeyen hacim')

def kap(cx,seviye,cap,nb,nm,etik,dh=0.7,w=1.5,etiket_aralik=1):
    h=nb*dh; bs=cap//nb; o=[f'\\fill[vurgu!15] ({cx-w/2},0) rectangle ({cx+w/2},{seviye/bs*dh:.3f});',f'\\draw[line width=1.3pt] ({cx-w/2},{h:.3f}) -- ({cx-w/2},0) -- ({cx+w/2},0) -- ({cx+w/2},{h:.3f});',
       f'\\draw[thick] ({cx-w/2},{seviye/bs*dh:.3f}) -- ({cx+w/2},{seviye/bs*dh:.3f});']
    for i in range(1,nb+1):
        o.append(f'\\draw ({cx-w/2},{i*dh:.3f}) -- ({cx-w/2+0.25},{i*dh:.3f});')
        if i%etiket_aralik==0: o.append(f'\\node[left=2pt] at ({cx-w/2},{i*dh:.3f}) {{{i*bs}}};')
    o.append(f'\\node[below] at ({cx},-0.05) {{{nm}}}; \\node[above] at ({cx},{h+0.4:.3f}) {{{etik}}};')
    return '\n'.join(o)

# ================= 01 kolay · kaplarda karışım =================
vK,pK,vL,pL=300,40,200,70; alk=Fr(vK*pK+vL*pL,100); v=alk*100/(vK+vL)
e=[Fr(pK+pL,2),Fr(vL*pK+vK*pL,vK+vL),alk,alk/2]
assert alk==260 and v==52 and e==[55,58,260,130] and len({v,*e})==5
SK=fig(kap(0,vK,400,4,'K',f'hacimce \\%{pK} alkol',dh=0.75,etiket_aralik=1)+'\n'+kap(4.2,vL,400,4,'L',f'hacimce \\%{pL} alkol',dh=0.75))
q('0001',tipId='krs-kaplar',tip='Kaplarda karışım',z='kolay',alt='Hacim Çizgili Kaplar',kaz='Kaplardaki hacimleri okuyup iki alkol çözeltisinin karışımındaki alkol oranını bulur.',kalip='hikâyeli',
 kart='K-KRS-01 (kaplar) · K: 300 mL %40, L: 200 mL %70',
 metin='Bir laboratuvarda, hacimce alkol oranları üzerlerinde yazılı olan iki alkol–su çözeltisi, hacim çizgileri mL cinsinden verilmiş K ve L kaplarında şekildeki seviyelere kadar doldurulmuştur. İki kaptaki çözeltinin tamamı temiz bir kaba boşaltılıp iyice karıştırılmıştır; hacimlerin toplamı korunmaktadır.\nBuna göre, oluşan karışımın hacimce alkol oranı yüzde kaçtır?',
 dogru=v,yan=[(e[0],'İki oranın aritmetik ortalamasını almış: (40 + 70) ÷ 2.','dikkat'),(e[1],'Hacimleri ters kullanmış: (200 × 40 + 300 × 70) ÷ 500.','dikkat'),(e[2],'Alkol hacmini (260 mL) oran sanmış.','dikkat'),(e[3],'Alkol hacmini kap sayısına bölmüş: 260 ÷ 2.','dikkat')],
 istenen='Karışımın alkol oranı (%).',ip=['Her kapta kaç mL çözelti olduğunu çizgilerden oku; her kaptaki alkol hacmini bul.'],bilgi=[ORN,BIR],sekil=SK,
 ad=[A('Hacimler','Çizgilerden okunur: K 300 mL, L 200 mL.','Toplam 500 mL'),A('Alkol hacimleri','Hacim × oran.','300 × 0,40 + 200 × 0,70 = 120 + 140 = 260 mL'),A('Oran','Toplam alkol toplam hacme bölünür.','260 ÷ 500 = 0,52 = %52')],
 puf='Önce her kaptaki alkol hacmini bul; oranları doğrudan ortalama alma.')

# ================= 02 kolay · alaşım çubuğu =================
bl=[('bakır',5),('çinko',4),('kalay',3)]; bak=250; bolme=Fr(bak,5); v=(4+3)*bolme
e=[4*bolme,3*bolme,bak,bolme]
assert bolme==50 and v==350 and e==[200,150,250,50] and len({v,*e})==5
fl=['gray!40','vurgu!25','white']; o=[]; x=0; bw=0.55
for (nm,k),f in zip(bl,fl):
    o.append(f'\\draw[thick,fill={f}] ({x*bw:.2f},0) rectangle ({(x+k)*bw:.2f},0.9);')
    for j in range(1,k): o.append(f'\\draw[thin] ({(x+j)*bw:.2f},0) -- ({(x+j)*bw:.2f},0.9);')
    o.append(f'\\node[above=2pt] at ({(x+k/2)*bw:.2f},0.9) {{{nm}}};'); x+=k
SK=fig('\n'.join(o))
q('0002',tipId='krs-alasim',tip='Alaşım çubuğu',z='kolay',alt='Alaşım Çubuğu',kaz='Bölmeli alaşım çubuğunda bir metalin kütlesinden bölme kütlesini bulup diğer metallerin toplamını hesaplar.',kalip='hikâyeli',
 kart='K-KRS-02 (alaşım çubuğu) · 5 + 4 + 3 bölme; bakır 250 g',
 metin='Bir dökümhanede üretilen alaşım parçasındaki bakır, çinko ve kalay kütlelerinin oranı, şekildeki çubukla gösterilmiştir; çubuktaki bütün bölmeler eşit kütleyi temsil etmektedir. Bu alaşım parçasındaki bakırın kütlesi 250 gramdır.\nBuna göre, parçadaki bakır dışındaki metallerin toplam kütlesi kaç gramdır?',
 dogru=v,yan=[(e[0],'Yalnız çinkonun kütlesini (4 bölme) yazmış.','dikkat'),(e[1],'Yalnız kalayın kütlesini (3 bölme) yazmış.','dikkat'),(e[2],'Bakırın kütlesini (verilen 250 g) cevap yazmış.','dikkat'),(e[3],'Bir bölmenin kütlesini (250 ÷ 5) bulup bırakmış.','dikkat')],
 istenen='Bakır dışındaki metallerin toplam kütlesi (g).',ip=['Bakır kaç bölmeyse 250 gram o bölmelerin kütlesidir; bir bölmenin kütlesini bul.'],bilgi=[ORN],sekil=SK,
 ad=[A('Bir bölme','Bakır 5 bölmedir.','250 ÷ 5 = 50 g'),A('Diğer bölmeler','Çinko 4, kalay 3 bölme.','4 + 3 = 7 bölme'),A('Kütle','Bölme sayısıyla bölme kütlesi çarpılır.','7 × 50 = 350 g')],
 puf='Bilinen bir parçadan bir bölmenin kütlesine geç.')

# ================= 03 orta · derişim–kütle tablosu =================
C=[('I',200,10),('II',300,20)]; m3=500; hedef=22; tuz3=Fr(hedef*(200+300+m3),100)-sum(Fr(m*p,100) for _,m,p in C); v=tuz3*100/m3
e=[Fr(tuz3*100,200+300+m3),hedef,3*hedef-10-20,tuz3]
assert tuz3==140 and v==28 and e==[14,22,36,140] and len({v,*e})==5
SK=tablo_svg(['Çözelti','Kütle (g)','Tuz oranı (kütlece, %)'],[['I','200','10'],['II','300','20'],['III','500','a']])
q('0003',tipId='krs-tablo',tip='Derişim tablosu',z='orta',alt='Derişim–Kütle Tablosu',kaz='Tablodaki kütle ve tuz oranlarından karışımın toplam tuz miktarını yazıp bilinmeyen oranı bulur.',kalip='tablo',
 kart='K-KRS-03 (derişim tablosu) · 200 g %10; 300 g %20; 500 g %a; karışım %22',
 metin='Bir tuz çözeltisi üretim tesisinde, kütlece tuz oranları farklı üç tuzlu su çözeltisinin kütleleri ve tuz oranları aşağıdaki tabloda verilmiştir; III. çözeltinin tuz oranı a ile gösterilmiştir. Üç çözelti tamamen karıştırıldığında oluşan karışımın kütlece tuz oranı %22 olmuştur; karışırken kütle kaybı olmamıştır.\nBuna göre, a kaçtır?',
 dogru=v,yan=[(e[0],'Üçüncü çözeltinin tuz kütlesini (140 g) tüm kütle yerine 1000 g’a bölmüş.','dikkat'),(e[1],'Karışımın oranını (%22) III. çözeltinin oranı sanmış.','dikkat'),(e[2],'Kütleleri hesaba katmadan oranların ortalamasını %22 almış: (10 + 20 + a) ÷ 3 = 22.','dikkat'),(e[3],'III. çözeltinin tuz kütlesini (140 g) oran sanmış.','dikkat')],
 istenen='a değeri.',ip=['Karışımdaki toplam tuz kütlesini bul; I. ve II. çözeltideki tuz miktarlarını çıkararak III. çözeltideki tuzu elde et.'],bilgi=[ORN,BIR],sekil=SK,
 ad=[A('Toplam kütle','Üç çözeltinin kütleleri toplanır.','200 + 300 + 500 = 1000 g'),A('Toplam tuz','Karışımın %22’si tuzdur.','1000 × 22/100 = 220 g'),A('III’teki tuz','I ve II’deki tuz çıkarılır.','220 − 20 − 60 = 140 g'),A('a','III’ün tuz oranı.','140 ÷ 500 × 100 = 28')],
 puf='Oranlar kütleyle ağırlıklandırılır; önce tuz kütlelerini yaz.')

# ================= 04 orta · kaplar arası aktarım =================
vA,pA,vB,pB,son=600,50,200,20,40; x=Fr(vB*(son-pB),pA-son)
e=[Fr(vB*(pA-son),son-pB),vB,Fr(vB*(pA-pB),son-pB),vA]
assert x==400 and e==[100,200,300,600] and len({x,*e})==5 and (vB*pB+x*pA)*100==son*(vB+x)*100
def tut(cx,nm,v,p):
    return (f'\\draw[thick,rounded corners=4pt,fill=vurgu!12] ({cx-1.5},0) rectangle ({cx+1.5},1.8); '
        f'\\node[align=center] at ({cx},0.9) {{\\textbf{{{nm} kabı}}\\\\{v} mL\\\\hacimce \\%{p} alkol}};')
o=[tut(0,'A',vA,pA),tut(4.6,'B',vB,pB),'\\draw[-{Stealth},very thick] (1.6,0.9) -- (3.0,0.9); \\node[above] at (2.3,0.95) {$x$ mL};']
SK=fig('\n'.join(o))
q('0004',tipId='krs-aktarim',tip='Kaplar arası aktarım',z='orta',alt='Kaplar Arası Aktarım',kaz='Bir kaptan diğerine aktarılan hacmi, oluşan yeni derişimden yararlanarak bulur.',kalip='hikâyeli',
 kart='K-KRS-04 (aktarım) · A: 600 mL %50; B: 200 mL %20; B son %40',
 metin='Bir dezenfektan üreticisinin A ve B kaplarındaki alkol–su çözeltilerinin hacimleri ve hacimce alkol oranları şekilde verilmiştir. A kabından x mL çözelti alınıp B kabına boşaltılmış ve B kabındaki çözelti iyice karıştırılmıştır. Bu işlemden sonra B kabındaki çözeltinin hacimce alkol oranı %40 olmuştur.\nBuna göre, A kabından alınan x kaç mL’dir?',
 dogru=x,yan=[(e[0],'Oran farklarını ters yazmış: 200 × (50 − 40) ÷ (40 − 20).','dikkat'),(e[1],'B kabının hacmini (200 mL) aktarılan sanmış.','dikkat'),(e[2],'Farkları yanlış almış: 200 × (50 − 20) ÷ (40 − 20).','dikkat'),(e[3],'A kabının tamamını aktarılan hacim sanmış.','dikkat')],
 istenen='Aktarılan x hacmi (mL).',ip=['B’deki alkol miktarını ve aktarılan x mL’deki alkol miktarını yaz; toplamı, yeni toplam hacmin %40’ına eşitle.'],bilgi=[ORN,BIR],sekil=SK,
 ad=[A('B’deki alkol','Hacim × oran.','200 × 0,20 = 40 mL'),A('Aktarılandaki alkol','x mL’nin %50’si.','0,5x mL'),A('Denklem','Toplam alkol, yeni hacmin %40’ıdır.','40 + 0,5x = 0,4 · (200 + x)'),A('x','Denklem çözülür.','40 + 0,5x = 80 + 0,4x → 0,1x = 40 → x = 400 mL')],
 puf='Oranlar arası farklar, hacimlerin ters oranını verir.')

# ================= 05 orta · iki depodan karışım =================
qx,px,qy,py,sure,su=3,80,2,20,10,20; hx,hy=qx*sure,qy*sure; alk=Fr(hx*px+hy*py,100); tp=hx+hy+su; v=alk*100/tp
e=[alk,Fr(alk*100,hx+hy)-su,Fr(px+py,2),Fr(alk*100,hx+hy)]
assert alk==28 and tp==70 and v==40 and e==[28,36,50,56] and len({v,*e})==5
o=[]
def depo(cx,nm,p): return (f'\\draw[thick,fill=vurgu!15] ({cx-1.3},3.2) rectangle ({cx+1.3},4.6); \\node[align=center] at ({cx},3.9) {{{nm}\\\\hacimce \\%{p} alkol}};')
o+=[depo(-1.7,'X deposu',px),depo(1.7,'Y deposu',py)]
o.append('\\draw[thick] (-2.7,0) rectangle (2.7,1.6); \\node at (0,0.8) {Karışım kabı (boş)};')
for cx,qq in ((-1.7,qx),(1.7,qy)): o.append(f'\\draw[-{{Stealth}},very thick] ({cx},3.2) -- ({cx},1.65); \\node[fill=white,inner sep=1pt] at ({cx},2.4) {{{qq} L/dk}};')
SK=fig('\n'.join(o))
q('0005',tipId='krs-akis',tip='Depolardan karışım',z='orta',alt='İki Depodan Karışım',kaz='Debi ve süreden akıtılan hacimleri bulup alkol miktarını toplayarak su eklenmiş karışımın oranını hesaplar.',kalip='hikâyeli',
 kart='K-KRS-05 (iki depo) · 3 L/dk %80, 2 L/dk %20, 10 dk, +20 L su',
 metin='Şekildeki düzenekte X ve Y depolarından, hacimce alkol oranları depolarda yazılı olan çözeltiler boş bir karışım kabına aynı anda ve sabit debiyle akıtılmaktadır; debiler borular üzerinde litre/dakika cinsinden verilmiştir. Musluklar 10 dakika açık tutulup kapatıldıktan sonra kaptaki çözeltiye 20 litre saf su eklenmiştir.\nBuna göre, kaptaki son karışımın hacimce alkol oranı yüzde kaçtır?',
 dogru=v,yan=[(e[0],'Alkol hacmini (28 L) oran sanmış.','dikkat'),(e[1],'Suyu hesaba katmadan bulduğu %56’dan 20 yüzde puanı çıkarmış.','dikkat'),(e[2],'İki oranın aritmetik ortalamasını almış: (80 + 20) ÷ 2.','dikkat'),(e[3],'Eklenen suyu toplam hacme katmamış: 28 ÷ 50.','dikkat')],
 istenen='Son karışımın alkol oranı (%).',ip=['Her depodan 10 dakikada kaç litre aktığını ve içindeki alkol miktarını bul; suyun yalnız toplam hacmi büyüttüğünü unutma.'],bilgi=[ORN,BIR],sekil=SK,
 ad=[A('Akan hacimler','Debi × süre.','X: 3 × 10 = 30 L, Y: 2 × 10 = 20 L'),A('Alkol miktarı','Hacim × oran.','30 × 0,80 + 20 × 0,20 = 24 + 4 = 28 L'),A('Toplam hacim','Eklenen su da katılır.','30 + 20 + 20 = 70 L'),A('Oran','Alkol toplam hacme bölünür.','28 ÷ 70 = 0,40 = %40')],
 puf='Saf su alkol miktarını değiştirmez, yalnız toplam hacmi artırır.')

# ================= 06 orta · ağzına kadar doldurma =================
cap,sev,pk,psise=1000,600,50,80; ek=cap-sev; alk=Fr(sev*pk+ek*psise,100); v=alk*100/cap
e=[pk,Fr(pk+psise,2),Fr(sev*psise+ek*pk,100)*100/cap,psise]
assert ek==400 and alk==620 and v==62 and e==[50,65,68,80] and len({v,*e})==5
o=[kap(0,sev,cap,10,'Kap','hacimce \\%50 alkol',dh=0.4,w=1.6,etiket_aralik=2)]
o.append('\\draw[thick,fill=vurgu!15] (3.6,0) rectangle (5.0,1.5); \\draw[thick,fill=vurgu!15] (4.05,1.5) rectangle (4.55,2.1); \\draw[thick] (4.0,2.1) rectangle (4.6,2.25);')
o.append('\\node[below,align=center] at (4.3,-0.05) {Şişe \\\\ hacimce \\%80 alkol};')
SK=fig('\n'.join(o))
q('0006',tipId='krs-doldur',tip='Kabı doldurma',z='orta',alt='Kabı Doldurma',kaz='Ölçekli kapta boş kalan hacmi bulup eklenen çözeltiyle oluşan karışımın oranını hesaplar.',kalip='hikâyeli',
 kart='K-KRS-06 (doldurma) · kap 1000 mL, seviye 600 mL %50; şişe %80',
 metin='Şekildeki ölçekli kapta, hacimce alkol oranı yazılı olan bir alkol–su çözeltisi bulunmaktadır; kabın hacim çizgileri mL cinsindendir. Şişedeki çözelti, kabın ağzına kadar dolana dek kaba boşaltılıyor ve karışım iyice karıştırılıyor. Şişedeki çözelti bu iş için yeterlidir.\nBuna göre, kaptaki son karışımın hacimce alkol oranı yüzde kaçtır?',
 dogru=v,yan=[(e[0],'Kaptaki ilk çözeltinin oranını (%50) değişmez sanmış.','dikkat'),(e[1],'İki oranın aritmetik ortalamasını almış: (50 + 80) ÷ 2.','dikkat'),(e[2],'Hacimleri ters kullanmış: (600 × 80 + 400 × 50) ÷ 1000.','dikkat'),(e[3],'Şişedeki çözeltinin oranını (%80) karışımın oranı sanmış.','dikkat')],
 istenen='Son karışımın alkol oranı (%).',ip=['Kabın dolu kısmını çizgilerden oku; ağzına kadar dolması için kaç mL eklendiğini bul.'],bilgi=[ORN,BIR],sekil=SK,
 ad=[A('Eklenen hacim','Kapasite 1000 mL, dolu kısım 600 mL.','1000 − 600 = 400 mL'),A('Alkol miktarı','Hacim × oran toplamı.','600 × 0,50 + 400 × 0,80 = 300 + 320 = 620 mL'),A('Oran','Toplam alkol, kapasiteye bölünür.','620 ÷ 1000 = %62')],
 puf='Kabın ağzına kadar dolması, toplam hacmin kapasiteye eşit olduğunu söyler.')

# ================= 07 zor · ayar çubuğu =================
n_alt,ayar2=18,22; m=60; altin=Fr(m*n_alt,24); bakir=m-altin; yeni_toplam=bakir*24/(24-ayar2); v=yeni_toplam-m
e=[m*(ayar2-n_alt)/24,bakir,m,yeni_toplam]
assert altin==45 and bakir==15 and yeni_toplam==180 and v==120 and e==[10,15,60,180] and len({v,*e})==5 and (altin+v)*24==ayar2*(m+v)
o=[]; bw=0.3
for i in range(24):
    f='vurgu!25' if i<n_alt else 'white'; o.append(f'\\draw[thick,fill={f}] ({i*bw:.2f},0) rectangle ({(i+1)*bw:.2f},0.8);')
o.append(f'\\draw[<->] (0,1.1) -- ({24*bw:.2f},1.1); \\node[above] at ({12*bw:.2f},1.1) {{24 eş bölme}};')
o.append(f'\\draw[thick,fill=vurgu!25] (0.3,-0.9) rectangle (0.6,-0.6); \\node[anchor=west] at (0.7,-0.75) {{altın}}; \\draw[thick] (2.6,-0.9) rectangle (2.9,-0.6); \\node[anchor=west] at (3.0,-0.75) {{bakır}};')
SK=fig('\n'.join(o))
q('0007',tipId='krs-ayar',tip='Ayar ve alaşım',z='zor',alt='Ayar Çubuğu',kaz='Ayarı bölme sayısı olarak yorumlayıp bakır miktarı sabit kalacak biçimde eklenecek saf altın miktarını bulur.',kalip='hikâyeli',
 kart='K-KRS-07 (ayar çubuğu) · 24 bölmede 18 altın; 60 g; 22 ayar için saf altın',
 metin='Bir alaşımın ayarı, kütlesi 24 eş bölmeye ayrıldığında saf altına ait bölme sayısıdır (24 ayar saf altındır); alaşımın geri kalanı bakırdır. Şekildeki çubuk, bir kuyumcunun elindeki 60 gramlık bileziğin alaşımını göstermektedir. Kuyumcu bileziği eritip üzerine saf (24 ayar) altın ekleyerek 22 ayarlık bir alaşım elde edecektir.\nBuna göre, kuyumcu kaç gram saf altın eklemelidir?',
 dogru=v,yan=[(e[0],'Ayar farkını (22 − 18 = 4) 24’e oranlayıp bileziğin kütlesiyle çarpmış: 60 × 4 ÷ 24.','dikkat'),(e[1],'Bakırın kütlesini (15 g) eklenecek altın sanmış.','dikkat'),(e[2],'Bileziğin kütlesi kadar (60 g) saf altın eklemeyi yeterli saymış.','dikkat'),(e[3],'Yeni alaşımın toplam kütlesini (180 g) eklenecek altın sanmış.','dikkat')],
 istenen='Eklenecek saf altın (g).',ip=['Eklenen saf altın alaşımdaki hangi maddenin kütlesini değiştirmez?'],bilgi=[ORN],sekil=SK,
 ad=[A('Bilezikteki altın','18/24 oranında altın.','60 × 18/24 = 45 g altın'),A('Bakır','Kalan kütle bakırdır.','60 − 45 = 15 g'),A('22 ayarda bakır','Bakır, 24 bölmenin 2’sidir.','Toplam kütle = 15 × 24/2 = 180 g'),A('Eklenecek altın','Yeni toplam kütleden eski kütle çıkarılır.','180 − 60 = 120 g')],
 puf='Ayarı 24’te kaç bölme olduğu olarak oku; her iki durumda bölmeleri karşılaştır.')

# ================= 08 zor · üç çözelti tablosu =================
a_hedef=25; b,pb=200,50; c=100; pa=20
a=Fr(pb*b-a_hedef*(b+c),a_hedef-pa)   # 0,2a + 100 = 0,25(a + 300)
assert a==500 and (Fr(pa*a,100)+Fr(pb*b,100))*100==a_hedef*(a+b+c)
a2=Fr(pb*b-a_hedef*b,a_hedef-pa)   # su hacmi toplama katılmazsa: 0,2a + 100 = 0,25(a + 200)
a3=Fr(pb*b-a_hedef*c,a_hedef-pa)   # II. kabın hacmi toplama katılmazsa: 0,2a + 100 = 0,25(a + 100)
a4=Fr(25,1)/Fr(25,100)   # 100 − 75 = 25 değerini 0,25 ile bölmek
assert a2==1000 and a3==1500 and a4==100 and Fr(25,Fr(25,100))==100
assert (Fr(pa*a2,100)+Fr(pb*b,100))*100==a_hedef*(a2+b) and (Fr(pa*a3,100)+Fr(pb*b,100))*100==a_hedef*(a3+c)
e=[a+b+c,a4,a3,a2]
assert e==[800,100,1500,1000] and len({a,*e})==5
SK=tablo_svg(['Kap','Hacim (mL)','Asit oranı (hacimce, %)'],[['I','a','20'],['II','200','50'],['III (saf su)','100','0']])
q('0008',tipId='krs-tablo2',tip='Üç çözelti ve bilinmeyen hacim',z='orta',alt='Üç Çözelti Tablosu',kaz='Tabloda hacmi bilinmeyen çözeltinin hacmini, toplam asit miktarından kurduğu denklemle bulur.',kalip='tablo',
 kart='K-KRS-08 (üç çözelti) · a mL %20, 200 mL %50, 100 mL su; karışım %25',
 metin='Bir kimya laboratuvarında hazırlanan üç sıvının hacimleri ve hacimce asit oranları aşağıdaki tabloda verilmiştir; I. kaptaki asit çözeltisinin hacmi a mL’dir, III. kapta yalnızca saf su vardır. Üç kaptaki sıvının tamamı bir araya boşaltıldığında oluşan karışımın hacimce asit oranı %25 olmuştur; karışırken hacim kaybı olmamıştır.\nBuna göre, a kaçtır?',
 dogru=a,yan=[(e[0],'Karışımın toplam hacmini (800 mL) a sanmış.','dikkat'),(e[1],'0,2a + 100 = 0,25 · (a + 300) denkleminde 100 − 75 = 25’i 0,05’e değil 0,25’e bölmüş.','islem'),(e[3],'Saf suyu toplam hacme katmamış: 0,2a + 100 = 0,25 · (a + 200).','dikkat'),(e[2],'II. kabın hacmini toplam hacme katmamış: 0,2a + 100 = 0,25 · (a + 100).','dikkat')],
 istenen='a değeri (mL).',ip=['Toplam asit miktarını a cinsinden yaz ve karışımın toplam hacminin %25’ine eşitle; saf suyun asidi olmadığına dikkat et.'],bilgi=[ORN,BIR],sekil=SK,
 ad=[A('Asit miktarları','I: 0,20a mL; II: 200 × 0,50 = 100 mL; III: 0.','Toplam asit = 0,2a + 100'),A('Toplam hacim','Üç hacim toplanır.','a + 200 + 100 = a + 300'),A('Denklem','Asit toplam hacmin %25’i.','0,2a + 100 = 0,25 · (a + 300)'),A('Çözüm','Düzenlenir.','100 − 75 = 0,05a → a = 500')],
 puf='Saf suyun asit miktarı sıfırdır ama hacmi toplama girer.')

bitir(P,'karisimsek','prob|Karışım Problemleri')
