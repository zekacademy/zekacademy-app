"""Kâr Zarar Problemleri · ŞEKİLLİ paket (9 soru): şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Kâr Zarar Problemleri'
P=Parti('karzararsek','Kâr Zarar Problemleri','prob|Kar Zarar Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli kâr-zarar soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

KAR=B('Kâr ve zarar','kâr = satış fiyatı − alış fiyatı; kâr yüzdesi alış fiyatına göre hesaplanır: kâr yüzdesi = kâr ÷ alış × 100. Örnek: alış 80 TL, satış 100 TL ise kâr 20 TL, kâr yüzdesi %25')
IND=B('İndirimli fiyat','indirimli fiyat = etiket fiyatı × (100 − indirim yüzdesi) ÷ 100. Örnek: etiket 200 TL, %10 indirim → 180 TL')

# ---------- kartlar ----------
kartla('K-KZS-01','Etiket kartı ve kâr tutarı','Etiket fiyatından indirimli satış fiyatı bulunur; satış fiyatından alış fiyatı çıkarılarak kâr tutarı elde edilir.','İndirim tutarını kâr sanmak; kâr yüzdesini TL yazmak.','kolay','hikâyeli',2,'kzs-etiket','Etiket kartı ve indirim')
kartla('K-KZS-02','Alış–satış tablosu','Her modelin birim kârı (negatif olabilir) adetle çarpılır; kâr ve zarar işaretli toplanır.','Zararı yok saymak ya da kâr gibi toplamak; adedi unutmak.','kolay','tablo',3,'kzs-tablo','Alış–satış tablosu ve net kâr')
kartla('K-KZS-03','Aylık satış sütun grafiği','Sütunlardan adetler okunur; indirimli ayın birim kârı ayrı hesaplanır; adetle çarpılıp toplanır.','İndirimli ayı da aynı birim kârla hesaplamak; kâr yerine ciro bulmak.','orta','grafik',4,'kzs-sutun','Aylık satış grafiği')
kartla('K-KZS-04','Kâr–adet doğrusal grafiği','Grafikteki iki noktadan adet başına kâr (eğim) ve sabit gider bulunur; istenen kâr için adet hesaplanır.','Sabit gideri hesaba katmamak ya da ters işaretle kullanmak; eğimi yanlış okumak.','orta','grafik',3,'kzs-dogru','Kâr–adet doğrusu')
kartla('K-KZS-05','Fatura ve KDV','Faturadan ara toplam hesaplanır; KDV satıcıya kalmadığı için kâr ara toplam ile alış bedeli arasındaki farktır.','KDV dahil tutarı satış saymak; kârı satışa oranlamak.','orta','hikâyeli',3,'kzs-fatura','Fatura ve KDV')
kartla('K-KZS-06','Kademeli fiyat tablosu','Müşterinin aldığı adet hangi aralıktaysa o birim fiyat bütün adetlere uygulanır; her müşterinin kârı ayrı bulunup toplanır.','Aralıkları artımlı uygulamak; müşterileri birleştirip tek fiyat kullanmak.','orta','tablo',4,'kzs-kademe','Kademeli fiyat tablosu')
kartla('K-KZS-07','Fiyat akış şeması','Akış şemasındaki işlemler sırayla uygulanır: önce yüzde artış, sonra yüzde indirim, sonra sabit tutarlı düşüm; son fiyattan alış çıkarılır.','Yüzdeleri toplayıp tek işlem yapmak; kuponu yanlış yönde kullanmak.','zor','hikâyeli',4,'kzs-akis','Fiyat belirleme akışı')
kartla('K-KZS-08','Kâr–zarar yüzdesi sütun grafiği','Eşit alış fiyatlı ürünlerin kâr–zarar yüzdeleri işaretli toplanıp toplam satıştan alış fiyatı bulunur.','Zararı çıkarmamak; grafiği yanlış okumak.','orta','grafik',4,'kzs-yuzde','Kâr–zarar yüzdesi grafiği')
kartla('K-KZS-09','İki etiket kartı','Bir mağazanın kâr yüzdesinden alış fiyatı bulunur; ikinci mağazanın indirimli fiyatından aynı alış fiyatı çıkarılır.','İndirim oranını kâr sanmak; iki mağazanın kârını karıştırmak.','zor','hikâyeli',4,'kzs-iki-etiket','Etiket kartları karşılaştırma')

def etiket(cx,baslik,fiyat,ind,w=3.8,h=2.6):
    o=[f'\\draw[thick,rounded corners=6pt] ({cx},0) rectangle ({cx+w},{h});',f'\\draw[thick] ({cx+0.45},{h-0.4}) circle (0.12);']
    if baslik: o.append(f'\\node[above] at ({cx+w/2},{h+0.05}) {{\\textbf{{{baslik}}}}};')
    o.append(f'\\node at ({cx+w/2+0.2},{h-0.5}) {{Etiket fiyatı}};')
    o.append(f'\\node at ({cx+w/2},{h-1.2}) {{\\Large\\textbf{{{fiyat} TL}}}};')
    o.append(f'\\draw[fill=vurgu!20,thick,rounded corners=4pt] ({cx+0.5},0.2) rectangle ({cx+w-0.5},0.85); \\node at ({cx+w/2},0.52) {{İndirim: \\%{ind}}};')
    return '\n'.join(o)

# ================= 01 kolay · etiket kartı =================
et,ind,alis=2000,10,1440; sat=Fr(et*(100-ind),100); v=sat-alis
e=[Fr(v*100,alis),alis*ind//100,sat*ind//100,et*ind//100]
assert sat==1800 and v==360 and e==[25,144,180,200] and len({v,*e})==5
SK=fig(etiket(0,None,et,ind))
q('0001',tipId='kzs-etiket',tip='Etiket kartı ve indirim',z='kolay',alt='Etiket Kartı',kaz='Etiket fiyatı ve indirim oranından satış fiyatını bulup alış fiyatıyla karşılaştırarak kâr tutarını hesaplar.',kalip='hikâyeli',
 kart='K-KZS-01 (etiket kartı) · 2000 TL, %10 indirim, alış 1440 TL',
 metin='Bir elektronik mağazası, alış fiyatı 1440 TL olan bir ütüyü şekildeki etiketle satışa çıkarmıştır. Kasada müşteriye etiket üzerindeki indirim eksiksiz uygulanmış ve ütü başka hiçbir indirim yapılmadan satılmıştır.\nBuna göre, mağaza bu satıştan kaç TL kâr elde etmiştir?',
 dogru=v,yan=[(e[0],'Kâr yüzdesini (360 ÷ 1440 × 100 = %25) kâr tutarı sanmış.','dikkat'),(e[1],'Kârı alış fiyatının %10’u (1440 × %10) olarak almış; indirim oranını kâr oranı sanmış.','dikkat'),(e[2],'Satış fiyatının %10’unu (1800 × %10) kâr saymış.','dikkat'),(e[3],'İndirim tutarını (2000 × %10) kâr sanmış.','dikkat')],
 istenen='Mağazanın kâr tutarı (TL).',ip=['Etiket üzerindeki indirimi uygulayarak ütünün satış fiyatını bul.'],bilgi=[IND,KAR],sekil=SK,
 ad=[A('İndirim tutarı','Etiket fiyatının %10’u.','2000 × 10/100 = 200 TL'),A('Satış fiyatı','Etiketten indirim çıkarılır.','2000 − 200 = 1800 TL'),A('Kâr','Satış fiyatından alış fiyatı çıkarılır.','1800 − 1440 = 360 TL')],
 puf='Kâr = satış fiyatı − alış fiyatı; satış fiyatı indirimli fiyattır.')

# ================= 02 kolay · alış–satış tablosu =================
M=[('K',400,500,6),('L',350,300,8),('M',250,310,5)]; kr=[(s-a)*n for _,a,s,n in M]; v=sum(kr)
e=[kr[0]+kr[2],kr[0]+abs(kr[1])+kr[2],sum(a*n for _,a,s,n in M),sum(s*n for _,a,s,n in M)]
assert kr==[600,-400,300] and v==500 and e==[900,1300,6450,6950] and len({v,*e})==5
SK=tablo_svg(['Model','Alış fiyatı (TL)','Satış fiyatı (TL)','Satılan adet'],[[m,str(a),str(s),str(n)] for m,a,s,n in M])
q('0002',tipId='kzs-tablo',tip='Alış–satış tablosu ve net kâr',z='kolay',alt='Alış–Satış Tablosu',kaz='Tablodaki alış ve satış fiyatlarından her modelin kâr ya da zararını bulup net kârı hesaplar.',kalip='tablo',
 kart='K-KZS-02 (alış–satış tablosu) · K +600, L −400, M +300',
 metin='Bir ayakkabı mağazası, bir haftada sattığı üç ayakkabı modelinin alış fiyatını, satış fiyatını ve satış adedini aşağıdaki tabloda göstermiştir. Her model, tablodaki satış fiyatıyla satılmıştır; bu haftada başka satış yapılmamıştır.\nBuna göre, mağazanın bu üç modelden elde ettiği net kâr kaç TL’dir?',
 dogru=v,yan=[(e[0],'L modelinde zarar ettiğini hesaba katmamış: 600 + 300.','dikkat'),(e[1],'L’nin zararını da kâr gibi toplamış: 600 + 400 + 300.','dikkat'),(e[2],'Kâr yerine toplam alış tutarını (maliyeti) yazmış.','dikkat'),(e[3],'Kâr yerine toplam satış tutarını (ciroyu) yazmış.','dikkat')],
 istenen='Net kâr (TL).',ip=['Her model için birim kâr ya da zararı bulup satılan adetle çarp; zarar eksi işaretlidir.'],bilgi=[KAR],sekil=SK,
 ad=[A('K modeli','Birim kâr 100 TL, 6 adet.','(500 − 400) × 6 = 600 TL kâr'),A('L modeli','Satış fiyatı alıştan düşük: zarar.','(300 − 350) × 8 = −400 TL'),A('M modeli','Birim kâr 60 TL, 5 adet.','(310 − 250) × 5 = 300 TL kâr'),A('Net kâr','Kâr ve zarar işaretli toplanır.','600 − 400 + 300 = 500 TL')],
 puf='Zarar eden modelin etkisini eksi işaretle toplama kat.')

# ================= 03 orta · aylık satış sütun grafiği =================
ay=[('Oca',40),('Şub',50),('Mar',60),('Nis',70)]; al,etk,indp=100,150,20; nis=Fr(etk*(100-indp),100)
ilk=sum(n for _,n in ay[:3]); v=ilk*(etk-al)+ay[3][1]*(nis-al)
e=[ay[3][1]*(nis-al),ilk*(etk-al)+ay[3][1]*(etk-al)*(100-indp)//100,ilk*(etk-al)+ay[3][1]*(etk-al),ilk*(etk-al)+ay[3][1]*nis]
assert nis==120 and ilk==150 and v==8900 and e==[1400,10300,11000,15900] and len({v,*e})==5
sx,sy=1.2,0.04; o=[]
for t in range(0,81,20): o.append(f'\\draw[gray!50,thin] (0,{t*sy:.2f}) -- ({4*sx+0.2:.2f},{t*sy:.2f}); \\node[left=2pt] at (0,{t*sy:.2f}) {{{t}}};')
o.append(f'\\draw[thick] (0,0) -- ({4*sx+0.2:.2f},0); \\draw[thick] (0,0) -- (0,{80*sy+0.2:.2f});')
o.append(f'\\node[above] at (0,{80*sy+0.2:.2f}) {{Satılan tişört sayısı}};')
for i,(nm,n) in enumerate(ay):
    x=0.15+i*sx; o.append(f'\\draw[fill=vurgu!20,thick] ({x:.2f},0) rectangle ({x+0.7:.2f},{n*sy:.2f}); \\node[below] at ({x+0.35:.2f},0) {{{nm}}};')
SK=fig('\n'.join(o))
q('0003',tipId='kzs-sutun',tip='Aylık satış grafiği',z='orta',alt='Aylık Satış Grafiği',kaz='Sütun grafiğinden aylık satış adedini okuyup indirimli ayın birim kârını ayrı hesaplayarak toplam kârı bulur.',kalip='grafik',
 kart='K-KZS-03 (sütun grafiği) · 40/50/60/70 adet; alış 100, etiket 150, Nisan %20 indirim',
 metin='Bir giyim mağazası, tanesini 100 TL’ye aldığı tişörtleri etiket fiyatı olan 150 TL’den satmaktadır; yalnızca Nisan ayında etiket fiyatı üzerinden %20 indirim yapmıştır. Şekildeki sütun grafiği, mağazanın dört aylık tişört satışlarını göstermektedir.\nBuna göre, mağazanın bu dört ayda tişört satışından elde ettiği toplam kâr kaç TL’dir?',
 dogru=v,yan=[(e[0],'Yalnız Nisan ayının kârını (70 × 20) yazmış.','dikkat'),(e[1],'İndirimi fiyata değil birim kâra uygulamış: Nisan’da birim kârı 50 × %80 = 40 TL almış; 7500 + 70 × 40.','islem'),(e[2],'Nisan ayındaki indirimi hesaba katmamış: 220 × 50.','dikkat'),(e[3],'Nisan ayı için kâr yerine indirimli satış tutarını (70 × 120) eklemiş.','dikkat')],
 istenen='Dört aylık toplam kâr (TL).',ip=['İlk üç ay ile Nisan ayının birim kârlarını ayrı ayrı bul.'],bilgi=[IND,KAR],sekil=SK,
 ad=[A('İlk üç ay','Grafikten 40 + 50 + 60 = 150 tişört; birim kâr 150 − 100 = 50 TL.','150 × 50 = 7500 TL'),A('Nisan fiyatı','Etiket fiyatından %20 indirim.','150 × 80/100 = 120 TL'),A('Nisan kârı','Birim kâr 20 TL, 70 tişört.','70 × 20 = 1400 TL'),A('Toplam','İki kâr toplanır.','7500 + 1400 = 8900 TL')],
 puf='İndirimli ayda birim kâr değişir; ayları ayrı hesapla.')

# ================= 04 orta · kâr–adet doğrusal grafiği =================
g0,a1,k1=-600,60,600; bir=Fr(k1-g0,a1); hedef=1800; v=(hedef-g0)/bir
e=[hedef/bir,(hedef+g0)/bir,hedef/Fr(k1,a1),-g0/bir]
assert bir==20 and v==120 and e==[90,60,180,30] and len({v,*e})==5
e[2]=Fr(hedef+600,1)/Fr(k1,a1); assert e[2]==240
ux,uy=0.07,0.0018; o=[]
for t in (-600,0,600,1200): o.append(f'\\draw[gray!50,thin] (0,{(t-g0)*uy:.3f}) -- ({100*ux:.2f},{(t-g0)*uy:.3f}); \\node[left=2pt] at (0,{(t-g0)*uy:.3f}) {{${t}$}};')
for x in range(0,101,20): o.append(f'\\draw (  {x*ux:.2f},0) -- ({x*ux:.2f},-0.08); \\node[below=2pt] at ({x*ux:.2f},0) {{{x}}};')
o.append(f'\\draw[thick] (0,0) -- ({100*ux:.2f},0); \\draw[thick] (0,0) -- (0,{1800*uy+0.2:.3f});')
o.append(f'\\node[below=0.5cm] at ({50*ux:.2f},0) {{Satılan vaza sayısı}}; \\node[above] at (0,{1800*uy+0.2:.3f}) {{Net kâr (TL)}};')
o.append(f'\\draw[thick,vurgu,-{{Stealth}}] (0,0) -- ({90*ux:.2f},{1800*uy:.3f});')
o.append(f'\\draw[dashed] ({a1*ux:.2f},0) -- ({a1*ux:.2f},{(k1-g0)*uy:.3f}) -- (0,{(k1-g0)*uy:.3f}); \\fill ({a1*ux:.2f},{(k1-g0)*uy:.3f}) circle (0.08); \\fill (0,0) circle (0.08);')
SK=fig('\n'.join(o))
q('0004',tipId='kzs-dogru',tip='Kâr–adet doğrusu',z='orta',alt='Kâr–Adet Grafiği',kaz='Doğrusal kâr grafiğinden adet başına kârı ve sabit gideri bulup istenen kâr için gereken adedi hesaplar.',kalip='grafik',
 kart='K-KZS-04 (kâr–adet doğrusu) · (0, −600), (60, 600); hedef 1800 TL',
 metin='Bir seramik atölyesi ürettiği vazoları hep aynı fiyattan satmakta ve her ay aynı sabit giderleri ödemektedir. Şekildeki doğru, atölyenin bir ayda sattığı vaza sayısı ile o ay sabit giderler çıkarıldıktan sonra elde ettiği net kârı göstermektedir.\nBuna göre, atölye bir ayda 1800 TL net kâr elde etmek için kaç vaza satmalıdır?',
 dogru=v,yan=[(e[0],'Sabit gideri hesaba katmamış: 1800 ÷ 20.','dikkat'),(e[1],'Sabit gideri çıkarması gerekirken kârdan çıkarmış: (1800 − 600) ÷ 20.','dikkat'),(e[2],'Eğimi yanlış okumuş: 600 ÷ 60 = 10 TL; (1800 + 600) ÷ 10.','dikkat'),(e[3],'Net kârın sıfır olduğu (zarar etmeme) vaza sayısını yazmış.','dikkat')],
 istenen='Gereken vaza sayısı.',ip=['Grafikteki iki işaretli noktadan vaza başına kâr artışını bul; doğrunun dikey eksenle kesiştiği noktayı oku.'],bilgi=[KAR],sekil=SK,
 ad=[A('Noktaları oku','Doğru (0; −600) ve (60; 600) noktalarından geçer.','Sabit gider 600 TL'),A('Vaza başına kâr','Net kâr artışı satılan vaza artışına bölünür.','(600 − (−600)) ÷ 60 = 20 TL'),A('Adedi bul','1800 TL net kâr için gerekli artış 1800 − (−600) = 2400 TL.','2400 ÷ 20 = 120 vaza')],
 puf='Doğrunun eğimi, bir vazanın katkısını verir.')

# ================= 05 orta · fatura ve KDV =================
ur=[('Termos',3,250),('Matara',5,90)]; kdv=20; ara=sum(n*f for _,n,f in ur); top=ara*(100+kdv)//100; alis=960; v=Fr((ara-alis)*100,alis)
e=[Fr((ara-alis*(100+kdv)//100)*100,alis),Fr((ara-alis)*100,ara),Fr((top-alis)*100,alis),ara-alis]
assert ara==1200 and top==1440 and v==25 and e==[5,20,50,240] and len({v,*e})==5
o=['\\draw[thick] (0,0) rectangle (6.6,4.6);','\\node at (3.3,4.15) {FATURA}; \\draw (0.15,3.8) -- (6.45,3.8);',
   '\\node[anchor=west] at (0.25,3.4) {Ürün}; \\node at (3.4,3.4) {Adet}; \\node[anchor=east] at (6.4,3.4) {Birim fiyat (TL)}; \\draw (0.15,3.05) -- (6.45,3.05);']
for i,(nm,n,f) in enumerate(ur):
    y=2.6-i*0.65; o.append(f'\\node[anchor=west] at (0.25,{y}) {{{nm}}}; \\node at (3.4,{y}) {{{n}}}; \\node[anchor=east] at (6.4,{y}) {{{f}}};')
o.append('\\draw[dashed] (0.15,1.45) -- (6.45,1.45); \\node[anchor=west,text width=6cm] at (0.25,0.7) {KDV oranı: \\%20 \\\\ (KDV, birim fiyatların toplamına eklenir)};')
SK=fig('\n'.join(o))
q('0005',tipId='kzs-fatura',tip='Fatura ve KDV',z='orta',alt='Fatura ve KDV',kaz='Faturadaki ürün tutarlarından ara toplamı bulup KDV’nin satıcıya kalmadığını bilerek kâr yüzdesini hesaplar.',kalip='hikâyeli',
 kart='K-KZS-05 (fatura) · 3×250 + 5×90 = 1200; KDV %20; alış 960',
 metin='Bir züccaciye mağazası, şekildeki faturada gösterilen ürünleri bir müşteriye satmıştır. Faturadaki birim fiyatlara KDV dahil değildir; KDV, ürün tutarlarının toplamına eklenerek müşteriden alınır ve mağazaya kalmayıp devlete ödenir. Mağazanın bu ürünler için tedarikçisine ödediği toplam alış bedeli 960 TL’dir.\nBuna göre, mağazanın bu satıştaki kâr yüzdesi kaçtır?',
 dogru=v,yan=[(e[0],'KDV’yi mağazanın gideri sayıp alış bedeline eklemiş (960 × 1,2 = 1152 TL); kârı 1200 − 1152 = 48 TL bulup 960’a oranlamış: 48 ÷ 960.','dikkat'),(e[1],'Kârı alış bedeline değil ürün tutarlarının toplamına oranlamış: 240 ÷ 1200.','dikkat'),(e[2],'Müşterinin ödediği KDV dahil tutarı (1440 TL) satış gelirine saymış: 480 ÷ 960.','dikkat'),(e[3],'Kâr tutarını (240 TL) yüzde sanmış.','dikkat')],
 istenen='Kâr yüzdesi.',ip=['Faturadaki ürün tutarlarının toplamını hesapla; mağazaya kalan gelir hangisidir?'],bilgi=[KAR],sekil=SK,
 ad=[A('Ürün tutarları','Adet × birim fiyat toplanır.','3 × 250 + 5 × 90 = 1200 TL'),A('Mağazanın geliri','KDV mağazaya kalmaz; gelir KDV hariç tutardır.','1200 TL'),A('Kâr','Gelirden alış bedeli çıkarılır.','1200 − 960 = 240 TL'),A('Kâr yüzdesi','Kâr alış bedeline oranlanır.','240 ÷ 960 × 100 = %25')],
 puf='KDV satıcının geliri değildir; kâr, KDV hariç tutardan hesaplanır.')

# ================= 06 orta · kademeli fiyat tablosu =================
fy=[('1 – 4',60),('5 – 9',55),('10 ve üzeri',50)]; alis=42; mus=[4,7,12]
def kdm(n): return fy[0][1] if n<=4 else fy[1][1] if n<=9 else fy[2][1]
v=sum(n*(kdm(n)-alis) for n in mus)
def art(n): return min(n,4)*60+max(0,min(n,9)-4)*55+max(0,n-9)*50
e=[sum(mus)*(55-alis),sum(art(n)-n*alis for n in mus),sum(mus)*(60-alis),sum(n*kdm(n) for n in mus)]
assert [n*(kdm(n)-alis) for n in mus]==[72,91,96] and v==259 and e==[299,344,414,1225] and len({v,*e})==5
SK=tablo_svg(['Bir seferde alınan adet','Birim satış fiyatı (TL)'],[[a,str(f)] for a,f in fy])
q('0006',tipId='kzs-kademe',tip='Kademeli fiyat tablosu',z='orta',alt='Kademeli Fiyat Tablosu',kaz='Adet aralığına göre değişen birim fiyattan her müşterinin kârını bulup toplar.',kalip='tablo',
 kart='K-KZS-06 (kademeli fiyat) · alış 42; 4, 7, 12 adet → 72 + 91 + 96',
 metin='Bir toptancı, tanesini 42 TL’ye aldığı pil paketlerini bir seferde alınan adede göre aşağıdaki tabloda verilen birim fiyattan satmaktadır. Müşterinin aldığı adet hangi aralıktaysa o birim fiyat, müşterinin aldığı bütün paketlere uygulanır. Üç müşteri bu toptancıdan tek seferde sırasıyla 4, 7 ve 12 paket almıştır.\nBuna göre, toptancı bu üç satıştan toplam kaç TL kâr etmiştir?',
 dogru=v,yan=[(e[0],'Üç müşterinin 23 paketini toplayıp tek fiyatla (55 TL) hesaplamış: 23 × 13.','dikkat'),(e[1],'Aralıkları artımlı uygulamış: örneğin 7 paketin ilk 4’üne 60, kalan 3’üne 55 TL almış.','dikkat'),(e[2],'Bütün paketleri ilk aralığın fiyatıyla (60 TL) hesaplamış: 23 × 18.','dikkat'),(e[3],'Kâr yerine toplam satış tutarını (ciroyu) yazmış.','dikkat')],
 istenen='Toplam kâr (TL).',ip=['Her müşterinin aldığı adedin hangi aralıkta olduğuna bakıp o müşteri için birim kârı ayrı bul.'],bilgi=[KAR],sekil=SK,
 ad=[A('4 paket','60 TL’lik aralık; birim kâr 18 TL.','4 × 18 = 72 TL'),A('7 paket','55 TL’lik aralık; birim kâr 13 TL.','7 × 13 = 91 TL'),A('12 paket','50 TL’lik aralık; birim kâr 8 TL.','12 × 8 = 96 TL'),A('Toplam','Üç müşterinin kârı toplanır.','72 + 91 + 96 = 259 TL')],
 puf='Her müşteri kendi aralığının fiyatıyla hesaplanır; adetleri birleştirme.')

# ================= 07 zor · fiyat akış şeması =================
al,art_,ind_,kup=2000,50,20,150; etk=al*(100+art_)//100; indf=etk*(100-ind_)//100; sat=indf-kup; v=sat-al
e=[kup,indf-al,al*(100+art_-ind_)//100-kup-al,indf+kup-al]
assert etk==3000 and indf==2400 and sat==2250 and v==250 and e==[150,400,450,550] and len({v,*e})==5
def kut(y,t): return f'\\draw[thick,rounded corners=3pt,fill=vurgu!12] (-2.2,{y-0.4}) rectangle (2.2,{y+0.4}); \\node at (0,{y}) {{{t}}};'
o=[kut(0,'Alış fiyatı: 2000 TL'),kut(-1.9,'Etiket fiyatı'),kut(-3.8,'İndirimli fiyat'),kut(-5.7,'Satış fiyatı')]
for i,t in enumerate(['alış fiyatının \\%50 fazlası','etiket fiyatı üzerinden \\%20 indirim','indirimli fiyattan 150 TL düşülür']):
    y1=-i*1.9-0.4; y2=-(i+1)*1.9+0.4; o.append(f'\\draw[-{{Stealth}},thick] (0,{y1}) -- (0,{y2}); \\node[anchor=west] at (0.3,{(y1+y2)/2}) {{{t}}};')
SK=fig('\n'.join(o))
q('0007',tipId='kzs-akis',tip='Fiyat belirleme akışı',z='zor',alt='Fiyat Akış Şeması',kaz='Akış şemasındaki yüzde artış, yüzde indirim ve sabit tutarlı düşümü sırayla uygulayıp kâr tutarını bulur.',kalip='hikâyeli',
 kart='K-KZS-07 (akış şeması) · 2000 → ×1,5 → ×0,8 → −150',
 metin='Bir mağaza, bir ürünün satış fiyatını şekildeki akış şemasında gösterilen adımları sırayla uygulayarak belirlemektedir; her adım bir önceki adımın sonucuna uygulanır ve ürün bu hesaplanan fiyattan satılmaktadır.\nBuna göre, mağazanın bu üründen elde ettiği kâr kaç TL’dir?',
 dogru=v,yan=[(e[0],'Yalnız son adımdaki 150 TL’yi kâr sanmış.','dikkat'),(e[1],'150 TL’lik son düşümü uygulamamış: 2400 − 2000.','dikkat'),(e[2],'Yüzdeleri toplayıp tek işlemde uygulamış: 2000 × (%150 − %20) = 2600; 2600 − 150 − 2000.','islem'),(e[3],'150 TL’yi düşmek yerine fiyata eklemiş: 2400 + 150 − 2000.','dikkat')],
 istenen='Mağazanın kârı (TL).',ip=['Şemadaki adımları yukarıdan aşağıya sırayla uygula; her adım önceki sonucun üzerine yapılır.'],bilgi=[IND,KAR],sekil=SK,
 ad=[A('Etiket fiyatı','Alış fiyatının %50 fazlası.','2000 × 150/100 = 3000 TL'),A('İndirimli fiyat','Etiket üzerinden %20 indirim.','3000 × 80/100 = 2400 TL'),A('Satış fiyatı','150 TL düşülür.','2400 − 150 = 2250 TL'),A('Kâr','Satıştan alış çıkarılır.','2250 − 2000 = 250 TL')],
 puf='Yüzdeler birbirine toplanmaz; her adım bir öncekinin sonucuna uygulanır.')

# ================= 08 orta · kâr–zarar yüzdesi sütun grafiği =================
yz=[('K',25),('L',20),('M',-5)]; toplam=3400; x=Fr(toplam*100,100*3+sum(p for _,p in yz)); v=Fr(toplam)-3*x
e=[sum(p for _,p in yz),Fr(toplam*sum(p for _,p in yz),100),x*45/100,x*(25+20+5)/100]
assert x==1000 and v==400 and [e[0],e[1],e[2],e[3]]==[40,1360,450,500] and len({v,*e})==5
ux,uy=1.2,0.1; o=[]
for t in range(-5,26,5): o.append(f'\\draw[gray!50,thin] (0,{t*uy:.2f}) -- ({3*ux+0.2:.2f},{t*uy:.2f}); \\node[left=2pt] at (0,{t*uy:.2f}) {{${t}$}};')
o.append(f'\\draw[thick] (0,0) -- ({3*ux+0.2:.2f},0); \\draw[thick] (0,{-5*uy-0.1:.2f}) -- (0,{25*uy+0.2:.2f});')
o.append(f'\\node[above] at (0,{25*uy+0.2:.2f}) {{Kâr (+) / zarar ($-$) yüzdesi}};')
for i,(nm,p) in enumerate(yz):
    xx=0.15+i*ux; y0,y1=sorted([0,p*uy]); o.append(f'\\draw[fill=vurgu!20,thick] ({xx:.2f},{y0:.2f}) rectangle ({xx+0.7:.2f},{y1:.2f}); \\node[below] at ({xx+0.35:.2f},{-5*uy-0.1:.2f}) {{{nm}}};')
SK=fig('\n'.join(o))
q('0008',tipId='kzs-yuzde',tip='Kâr–zarar yüzdesi grafiği',z='orta',alt='Kâr–Zarar Yüzdesi Grafiği',kaz='Grafikteki kâr ve zarar yüzdelerinden eşit alış fiyatını bulup net kârı hesaplar.',kalip='grafik',
 kart='K-KZS-08 (yüzde grafiği) · +%25, +%20, −%5; toplam satış 3400',
 metin='Bir mağaza, alış fiyatları birbirine eşit olan K, L ve M ürünlerini satmıştır. Şekildeki sütun grafiği, her ürünün satışından elde edilen kâr (sıfırın üstü) ya da zarar (sıfırın altı) yüzdesini göstermektedir. Üç ürünün satışından elde edilen toplam satış geliri 3400 TL’dir.\nBuna göre, mağazanın bu üç üründen elde ettiği net kâr kaç TL’dir?',
 dogru=v,yan=[(e[0],'Yüzdelerin işaretli toplamını (25 + 20 − 5 = 40) TL sanmış.','dikkat'),(e[1],'Yüzdelerin net toplamını (%40) toplam satışa uygulamış: 3400 × 40 ÷ 100.','dikkat'),(e[2],'M’nin zararını hesaba katmamış: 1000 × (25 + 20) ÷ 100.','dikkat'),(e[3],'M’nin zararını da kâr gibi toplamış: 1000 × (25 + 20 + 5) ÷ 100.','islem')],
 istenen='Net kâr (TL).',ip=['Her ürünün satış fiyatını alış fiyatının yüzdesi olarak yaz ve üçünü toplayıp 3400 TL’ye eşitle.'],bilgi=[KAR],sekil=SK,
 ad=[A('Satış–alış ilişkisi','Alış fiyatı x olsun; satışlar 1,25x, 1,20x ve 0,95x.','1,25x + 1,20x + 0,95x = 3,4x'),A('Alış fiyatı','Toplam satış 3400 TL.','3,4x = 3400 → x = 1000 TL'),A('Toplam alış','Üç ürün.','3 × 1000 = 3000 TL'),A('Net kâr','Satıştan alış çıkarılır.','3400 − 3000 = 400 TL')],
 puf='Zarar eden ürünün satışı alıştan düşüktür; satış fiyatını 100 eksi zarar yüzdesiyle yaz.')

# ================= 09 zor · iki etiket kartı =================
kE,kI,lE,lI=1800,20,1500,12; kS=kE*(100-kI)//100; alisK=Fr(kS*100,120); lS=lE*(100-lI)//100; v=lS-alisK
e=[Fr(v*100,alisK),lI,kI,lE-alisK]
assert kS==1440 and alisK==1200 and lS==1320 and v==120 and e==[10,12,20,300] and len({v,*e})==5
SK=fig(etiket(0,'K mağazası',kE,kI)+'\n'+etiket(4.4,'L mağazası',lE,lI))
q('0009',tipId='kzs-iki-etiket',tip='Etiket kartları karşılaştırma',z='zor',alt='İki Etiket Kartı',kaz='Bir mağazanın kâr yüzdesinden ortak alış fiyatını bulup ikinci mağazanın kâr tutarını hesaplar.',kalip='hikâyeli',
 kart='K-KZS-09 (iki etiket) · K: 1800, %20; K kârı %20 → alış 1200; L: 1500, %12',
 metin='Aynı ürünü aynı alış fiyatından satın alan K ve L mağazaları, ürünü şekildeki etiketlerle satışa çıkarmıştır. İki mağaza da kasada etiketteki indirimi uygulamış ve ürünü yalnızca bu fiyattan satmıştır. K mağazası bu üründen %20 kâr etmiştir.\nBuna göre, L mağazasının bu üründen elde ettiği kâr kaç TL’dir?',
 dogru=v,yan=[(e[0],'L’nin kâr yüzdesini (120 ÷ 1200 × 100 = %10) TL sanmış.','dikkat'),(e[1],'L’nin indirim yüzdesini kâr sanmış.','dikkat'),(e[2],'K mağazasının kâr yüzdesini L’nin kârı sanmış.','dikkat'),(e[3],'L’nin etiket fiyatından alış fiyatını çıkarmış: 1500 − 1200 (indirimi uygulamamış).','dikkat')],
 istenen='L mağazasının kârı (TL).',ip=['K mağazasının indirimli satış fiyatını bul; bu fiyatın alışın yüzde kaçı olduğunu kullanarak alış fiyatına ulaş.'],bilgi=[IND,KAR],sekil=SK,
 ad=[A('K’nın satış fiyatı','Etiket üzerinden %20 indirim.','1800 × 80/100 = 1440 TL'),A('Alış fiyatı','K %20 kârla sattı: satış = alış × 120/100.','1440 ÷ 1,2 = 1200 TL'),A('L’nin satış fiyatı','Etiket üzerinden %12 indirim.','1500 × 88/100 = 1320 TL'),A('L’nin kârı','Satıştan alış çıkarılır.','1320 − 1200 = 120 TL')],
 puf='Ortak bilgi alış fiyatıdır; önce onu K’nın verisinden bul.')

bitir(P,'karzararsek','prob|Kar Zarar Problemleri')
