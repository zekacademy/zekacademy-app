"""Denklem Çözme · ŞEKİLLİ paket (10 soru): şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Denklem Çözme'
P=Parti('denklemsek','Denklem Çözme','mat|Denklem Çözme')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli denklem soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

TER=B('Terazi ve denklem','denge halinde iki kefedeki kütleler eşittir; özdeş cisimlerin kütleleri aynıdır. Her iki kefeden aynı kütle çıkarılırsa denge bozulmaz. Örnek: 2m + 1 = m + 4 ise m = 3')
DEN=B('Birinci dereceden denklem','bilinmeyen terimler bir tarafta, sayılar öteki tarafta toplanır; taraf değiştiren terimin işareti değişir. Örnek: 5x − 3 = 2x + 9 ise 3x = 12, x = 4')
PAR=B('Parantez açma','önündeki sayı, parantez içindeki her terimle çarpılır. Örnek: 3(y − 4) = 3y − 12')
DOG=B('Doğru denklemi','(x₁, y₁) ve (x₂, y₂) noktalarından geçen doğrunun eğimi (y₂ − y₁)/(x₂ − x₁)’dir; eksenin kesim noktası b ise denklem y = mx + b’dir. Örnek: (0, 1) ve (2, 7) noktalarından geçen doğru y = 3x + 1’dir')
ORT=B('Eşit aralıklı noktalar','ardışık noktalar arası uzaklık sabit ise k. nokta ile ilk nokta arası uzaklık, (k − 1) tane aralığa eşittir. Örnek: 0, 5, 10, 15 noktalarında 0 ile 15 arası 3 aralıktır')
CEV=B('Çevre ve dik kenarlı çokgen','dik kenarlı bir çokgenin çevresi, kapladığı en küçük dikdörtgenin çevresine eşittir; yatay kenarların toplamı genişliğe, düşey kenarların toplamı yüksekliğe denk gelir. Örnek: 3 + 2 genişlik, 4 + 1 yükseklik ise çevre 2 × (5 + 5) = 20')

# ---------- kartlar ----------
kartla('K-DNS-01','Terazi ve denklem','Dengedeki terazi iki kefenin eşitliğini verir; kutuların kütlesi bilinmeyen alınıp denklem kurulur.','Terimleri taraf değiştirirken işareti değiştirmemek; kefedeki kütleleri toplayıp kutu sayısına bölmek.','kolay','şekilli',3,'dns-terazi','Terazi ile denklem kurma')
kartla('K-DNS-02','İşlem akış şeması','İki koldan gelen ifadeler yazılıp birleşme işlemi uygulanır; denklem çözülür.','Çıkarmada işareti dağıtmamak; kolların sırasını karıştırmak.','orta','şekilli',4,'dns-akis','İşlem akış şeması')
kartla('K-DNS-03','Sayı piramidi','Her kutu altındaki iki kutunun toplamıdır; üstteki sayıdan denklem kurulur.','Bir kutuyu eksik toplamak; sorulanı karıştırmak.','orta','şekilli',4,'dns-piramit','Sayı piramidi')
kartla('K-DNS-04','Sihirli kare','Sihirli karede her satır, sütun ve köşegen toplamı eşittir; iki sütun/satır toplamı eşitlenerek denklem çözülür.','Toplamı yanlış yazmak; denklemi çözerken işlem hatası.','orta','şekilli',4,'dns-sihirli','Sihirli kare ile denklem')
kartla('K-DNS-05','Fiyat etiketi ve kasa fişi','Etiketlerdeki ifadelerle toplam tutar denklemi kurulur; kupon ve poşet ücreti işaretleriyle eklenir.','Kuponu ya da poşet ücretini unutmak; farkı yanlış tarafa uygulamak.','orta','şekilli',5,'dns-etiket','Fiyat etiketi ve toplam tutar')
kartla('K-DNS-06','Çubuk (bar) modeli ile yaş','Şekildeki çubuklardan ifadeler yazılır; 5 yıl sonra kurulan oran denklemi çözülür.','Annenin 5 yılını denklemde unutmak; 5 yılı çıkarmak.','orta','şekilli',4,'dns-bar','Çubuk modeli ve yaş denklemi')
kartla('K-DNS-07','Çevresi verilen çokgen','Dik kenarlı çokgenin çevresi iki boyutun toplamının iki katıdır; etiketsiz kenarlar etiketli kenarların toplamıyla bulunur.','Yalnız etiketli kenarları toplamak; etiketsiz kenarı unutmak.','orta','şekilli',5,'dns-cevre','Çevresi verilen şekilde denklem')
kartla('K-DNS-08','Kesişen iki doğru','İşaretli noktalardan her doğrunun denklemi bulunur; denklemler eşitlenip kesişim noktası hesaplanır.','Kesim noktasını eğim sanmak; eğim işaretini yanlış almak.','zor','grafik',5,'dns-grafik','İki doğrunun kesişimi')
kartla('K-DNS-09','Eşit aralıklı noktalar','Eşit aralıklı noktalarda uzaklıklar oranı parça sayılarının oranına eşittir; denklemden x bulunup istenen nokta hesaplanır.','Nokta sayısını parça sayısı sanmak; yanlış noktaları karşılaştırmak.','zor','şekilli',5,'dns-dogru','Sayı doğrusunda x’li noktalar')
kartla('K-DNS-10','Kasa fişi','Fişte silik kalan tutar toplamdan bulunur; sonra adede bölünerek birim fiyata gidilir.','İndirimi yok saymak; adede bölmeyi unutmak.','orta','tablo',3,'dns-fis','Kasa fişi')

# ================= 01 kolay · terazi =================
k_,s1_,s2_=4,5,13; assert 3*k_+s1_==k_+s2_
assert (s2_+s1_)//(3)==6 and (s2_-s1_)==8 and (s2_+s1_)//2==9 and 3*9-s1_==9+s2_ and (s2_-s1_)//2==4
e=[2,6,8,9]; assert (s2_-s1_)//4==2 and len({k_,*e})==5
SKK=fig('''\\draw[thick] (-2.5,3.2) -- (2.5,3.2); \\draw[thick] (0,3.2) -- (0,0.1); \\draw[thick] (-0.8,0.1) -- (0.8,0.1); \\fill (0,3.2) circle (0.08);
'''+'\n'.join(f'''\\draw[thin] ({x},3.2) -- ({x-2.1},1.2); \\draw[thin] ({x},3.2) -- ({x+2.1},1.2); \\draw[thick] ({x-2.1},1.2) -- ({x+2.1},1.2);''' for x in (-2.5,2.5))
 +'\n'+''.join(f'\\draw[thick,fill=gray!35] ({-2.5-1.85+i*0.9:.2f},1.2) rectangle ({-2.5-1.85+i*0.9+0.7:.2f},1.9);' for i in range(3))
 +f'\\node[draw,thick,rounded corners=1pt,fill=gray!15,minimum width=1.0cm,minimum height=0.7cm,anchor=south] at ({-2.5-1.85+3*0.9+0.5:.2f},1.2) {{{s1_} kg}};'
 +f'\\draw[thick,fill=gray!35] ({2.5-0.95:.2f},1.2) rectangle ({2.5-0.95+0.7:.2f},1.9);'
 +f'\\node[draw,thick,rounded corners=1pt,fill=gray!15,minimum width=1.0cm,minimum height=0.7cm,anchor=south] at ({2.5-0.95+0.9+0.5:.2f},1.2) {{{s2_} kg}};'
 +'\\draw[thick,fill=gray!35] (-1.0,-0.65) rectangle (-0.4,-0.1); \\node[anchor=west] at (-0.3,-0.4) {özdeş kutu};')
q('0001',tipId='dns-terazi',tip='Terazi ile denklem kurma',z='kolay',alt='Terazi',kaz='Dengedeki terazi şemasından denklem kurup bilinmeyen kütleyi bulur.',kalip='şekilli',
 kart='K-DNS-01 (terazi) · 3k + 5 = k + 13',
 metin='Şekildeki eşit kollu terazi dengededir. Terazinin kefeleri ve kolları kütlesizdir; taralı kutuların hepsi birbirinin özdeşidir ve ağırlıklar üzerlerinde yazılı kütlelere sahiptir.\nBuna göre, bir kutunun kütlesi kaç kilogramdır?',
 dogru=k_,yan=[(e[0],'k terimini yanlış tarafa geçirmiş: 3k + k = 13 − 5, 4k = 8.','dikkat'),(e[1],'İki kefedeki ağırlıkları toplayıp kutu sayısına bölmüş: (13 + 5) ÷ 3.','dikkat'),(e[2],'Ağırlıkların farkını (13 − 5) bir kutunun kütlesi sanmış.','dikkat'),(e[3],'5 kg’ı sol taraftan çıkarmak yerine eksilterek geçirmiş: 3k − 5 = k + 13.','dikkat')],
 istenen='Bir kutunun kütlesi (kg).',ip=['Her iki kefeden aynı şeyleri çıkararak kefeleri sadeleştir; geriye kalan durumun dengede olması neyi gösterir?'],bilgi=[TER],sekil=SKK,
 ad=[A('Denklemi kur','Sol kefe 3 kutu ve 5 kg, sağ kefe 1 kutu ve 13 kg.','3k + 5 = k + 13'),A('Düzenle','Bilinmeyenler bir tarafa, sayılar öteki tarafa.','3k − k = 13 − 5 → 2k = 8'),A('Çöz','Her iki taraf 2’ye bölünür.','k = 4 kg')],
 puf='İki kefeden de aynı şeyi alırsan denge bozulmaz: önce birer kutu, sonra 5’er kg al.')

# ================= 02 orta · akış şeması (iki kol) =================
x0=10; up=3*x0-2; lo=x0+6; out=up-lo; assert out==12
# her çeldirici denklemini doğrula
assert 3*4-2-4+6==12 and (-2+6)-(3*(-2)-2)==12 and 4*2+4==12 and 3*9-(9+6)==12 and len({x0,-2,2,4,9})==5
SK=fig('''\\node[draw,thick,rounded corners=2pt,minimum width=1cm,minimum height=0.8cm] (g) at (0,0) {$x$}; \\node[above=2pt] at (g.north) {Giriş};
\\node[draw,thick,minimum width=1.1cm,minimum height=0.8cm] (a1) at (2.4,1.1) {$\\times 3$}; \\node[draw,thick,minimum width=1.1cm,minimum height=0.8cm] (a2) at (4.5,1.1) {$-2$};
\\node[draw,thick,minimum width=1.1cm,minimum height=0.8cm] (b1) at (3.4,-1.1) {$+6$};
\\node[draw,thick,circle,minimum size=0.9cm] (m) at (6.7,0) {$-$};
\\node[draw,thick,rounded corners=2pt,minimum width=1cm,minimum height=0.8cm] (c) at (8.7,0) {$12$}; \\node[above=2pt] at (c.north) {Çıkış};
\\draw[-{Stealth},thick] (g.east) -- (1.1,0) |- (a1.west); \\draw[-{Stealth},thick] (g.east) -- (1.1,0) |- (b1.west);
\\draw[-{Stealth},thick] (a1.east) -- (a2.west); \\draw[-{Stealth},thick] (a2.east) -| (m.north); \\draw[-{Stealth},thick] (b1.east) -| (m.south); \\draw[-{Stealth},thick] (m.east) -- (c.west);''')
q('0002',tipId='dns-akis',tip='İşlem akış şeması',z='orta',alt='Akış Şeması',kaz='İki kollu işlem akış şemasından denklem kurup girişi bulur.',kalip='şekilli',
 kart='K-DNS-02 (iki kollu akış) · (3x − 2) − (x + 6) = 12',
 metin='Aşağıdaki işlem şemasında giriş olarak verilen x sayısı, hem üst koldaki hem alt koldaki işlemlerden oklar yönünde sırayla geçer. Birleşme kutusunda üst koldan gelen sayıdan alt koldan gelen sayı çıkarılır ve sonuç çıkışa yazılır. Çıkışta 12 elde edilmiştir.\nBuna göre, giriş olarak verilen x sayısı kaçtır?',
 dogru=x0,yan=[(-2,'Çıkarmayı ters sırayla yapmış: alt koldan üst kolu çıkarmış, (x + 6) − (3x − 2) = 12.','dikkat'),(2,'Birleşme kutusunda çıkarmak yerine toplamış: (3x − 2) + (x + 6) = 12.','dikkat'),(4,'Çıkarmada parantezi dağıtmamış: 3x − 2 − x + 6 = 12.','dikkat'),(9,'Üst koldaki − 2 işlemini unutmuş: 3x − (x + 6) = 12.','dikkat')],
 istenen='Giriş sayısı x.',ip=['Her koldan çıkan ifadeyi x cinsinden yaz; birleşme kutusunun işlemini uygula.'],bilgi=[DEN,PAR],sekil=SK,
 ad=[A('Üst kol','Önce 3 ile çarpılır, sonra 2 çıkarılır.','3x − 2'),A('Alt kol','x’e 6 eklenir.','x + 6'),A('Denklem','Üstten alt çıkarılır ve sonuç 12’dir.','(3x − 2) − (x + 6) = 12 → 2x − 8 = 12'),A('Çöz','8 karşıya geçer.','2x = 20 → x = 10')],
 puf='Çıkarılan ifade parantez içinde yazılır; işaretler dağıtılır.')

# ================= 03 orta · sayı piramidi =================
xv=7; b=[xv,2*xv,xv+3]; m=[b[0]+b[1],b[1]+b[2]]; top=sum(m); assert top==45==6*xv+3 and max(b)==14
e=[xv,xv+3,m[0],sum(b)]; assert e==[7,10,21,31] and len({max(b),*e})==5
def kt(x,y,t): return f'\\node[draw,thick,minimum width=1.5cm,minimum height=0.8cm] at ({x},{y}) {{{t}}};'
SK=fig(kt(-1.6,0,'$x$')+kt(0,0,'$2x$')+kt(1.6,0,'$x+3$')+kt(-0.8,0.9,'')+kt(0.8,0.9,'')+kt(0,1.8,'45'))
q('0003',tipId='dns-piramit',tip='Sayı piramidi',z='orta',alt='Sayı Piramidi',kaz='Sayı piramidindeki toplam ilişkisinden x’i bulup kutudaki sayıyı hesaplar.',kalip='şekilli',
 kart='K-DNS-03 (piramit) · alt sıra x, 2x, x + 3; tepe 45',
 metin='Aşağıdaki sayı piramidinde her kutudaki sayı, hemen altındaki iki kutudaki sayının toplamına eşittir. Alt sıradaki kutulara x’e bağlı ifadeler yazılmış, en üst kutuya 45 yazılmıştır; ortadaki kutular boş bırakılmıştır.\nBuna göre, alt sıradaki en büyük sayı kaçtır?',
 dogru=14,yan=[(e[0],'x’in değerini (7) sorulan sayı sanmış.','dikkat'),(e[1],'Alt sıradaki en büyük sayıyı x + 3 kutusu sanmış: 7 + 3.','dikkat'),(e[2],'Orta sıradaki sol kutunun değerini yazmış: 3x = 21.','dikkat'),(e[3],'Alt sıradaki üç sayının toplamını yazmış: 7 + 14 + 10.','islem')],
 istenen='Alt sıradaki en büyük sayı.',ip=['Ortadaki iki kutunun değerini x cinsinden yaz; tepe kutusu bunların toplamıdır.'],bilgi=[DEN],sekil=SK,
 ad=[A('Orta sıra','Her kutu altındaki ikisinin toplamıdır.','x + 2x = 3x · 2x + (x + 3) = 3x + 3'),A('Tepe','Ortadaki ikisinin toplamı 45’tir.','3x + (3x + 3) = 45 → 6x + 3 = 45'),A('x’i bul','3 karşıya geçip 6’ya bölünür.','6x = 42 → x = 7'),A('Alt sıra','Üç kutu: 7 · 14 · 10.','en büyüğü 2x = 14')],
 puf='Alt sıradaki ifadeleri tepeye kadar toplayarak tek denklem kur.')

# ================= 04 orta · sihirli kare =================
xs=4; cells=[[3*xs-2,3,8],[5,xs+3,9],[6,11,2*xs-4]]
S=sum(cells[0]); assert all(sum(r)==S for r in cells) and all(sum(cells[i][j] for i in range(3))==S for j in range(3)) and cells[0][0]+cells[1][1]+cells[2][2]==S and cells[0][2]+cells[1][1]+cells[2][0]==S==21
assert 3*(-1)+9==-1+7 and 3*3+11==3+17 and len({xs,-1,3,8,13})==5
def cell(i,j,t): return f'\\node[draw,thick,minimum width=1.7cm,minimum height=1.0cm] at ({j*1.7},{-i*1.0}) {{{t}}};'
txt=[['$3x-2$','3','8'],['5','$x+3$','9'],['6','11','$2x-4$']]
SK=fig(''.join(cell(i,j,txt[i][j]) for i in range(3) for j in range(3)))
q('0004',tipId='dns-sihirli',tip='Sihirli kare ile denklem',z='orta',alt='Sihirli Kare',kaz='Sihirli karedeki eşit toplamlardan denklem kurup x’i bulur.',kalip='şekilli',
 kart='K-DNS-04 (sihirli kare) · 3x + 9 = x + 17',
 metin='Aşağıdaki 3 × 3’lük karenin her satırındaki, her sütunundaki ve iki köşegenindeki sayıların toplamı birbirine eşittir. Karedeki kutulara bazı sayılar ve x’e bağlı ifadeler yazılmıştır.\nBuna göre, x kaçtır?',
 dogru=xs,yan=[(-1,'2. satırın toplamında sabitleri yanlış toplamış: x + 7 (doğrusu x + 17); 3x + 9 = x + 7.','islem'),(3,'1. sütunun toplamında −2’yi unutmuş: 3x + 11 = x + 17.','dikkat'),(8,'2x = 8 denkleminde 2’ye bölmeyi unutmuş.','islem'),(13,'Terimleri karşıya geçirirken işareti değiştirmemiş: 3x − x = 17 + 9.','dikkat')],
 istenen='x değeri.',ip=['İçinde x bulunan kutuları kapsayan iki farklı satır ya da sütunun toplamını yazıp eşitle.'],bilgi=[DEN],sekil=SK,
 ad=[A('2. satır','Üç kutu toplanır.','5 + (x + 3) + 9 = x + 17'),A('1. sütun','Üç kutu toplanır.','(3x − 2) + 5 + 6 = 3x + 9'),A('Eşitle','Satır ve sütun toplamları eşittir.','3x + 9 = x + 17'),A('Çöz','Bilinmeyenler bir tarafa.','2x = 8 → x = 4')],
 puf='x’li kutuları ortak içeren iki doğrultunun toplamını eşitle; sabit kutular tabloda yeterince var.')

# ================= 05 zor · fiyat etiketi =================
xt=60; sapka=xt-15; tutar=3*xt+2*sapka-20+5; assert tutar==255
assert 5*61-50==255 and 5*56-25==255 and 5*57-30==255 and 5*48+15==255
e=[48,56,57,61]; assert len({xt,*e})==5
def etiket(x,adi,fiyat): return (f'\\draw[thick,rounded corners=3pt,fill=gray!8] ({x},0) -- ({x+2.6},0) -- ({x+2.6},1.5) -- ({x},1.5) -- cycle; \\draw[thick] ({x+0.25},1.2) circle (0.09); '
  f'\\node at ({x+1.4},1.05) {{{adi}}}; \\node at ({x+1.4},0.5) {{{fiyat}}};')
kasa=''.join(f'\\draw[thick,rounded corners=3pt,fill=gray!8] ({xx},-1.9) rectangle ({xx+2.6},-0.7); \\node at ({xx+1.3},-1.3) {{{tt}}};' for xx,tt in ((0,'Kupon: $-20$ TL'),(3.4,'Poşet: $+5$ TL')))
SK=fig(etiket(0,'Tişört','$x$ TL')+etiket(3.4,'Şapka','$(x-15)$ TL')+kasa)
q('0005',tipId='dns-etiket',tip='Fiyat etiketi ve toplam tutar',z='orta',alt='Fiyat Etiketi',kaz='Etiket ifadeleri ve kasadaki indirim-ücret işlemlerinden tutar denklemi kurar.',kalip='şekilli',
 kart='K-DNS-05 (fiyat etiketi) · 3x + 2(x − 15) − 20 + 5 = 255',
 metin='Bir mağazada tişört ve şapkanın fiyat etiketleri ile kasadaki kupon ve poşet bilgisi şekilde gösterilmiştir. Mert bu mağazadan 3 tişört ve 2 şapka almış; kasada toplam tutardan şekildeki indirim kuponu düşülmüş, ardından şekildeki poşet ücreti eklenmiştir. Mert’in ödediği toplam tutar 255 TL’dir ve başka bir ücret alınmamıştır.\nBuna göre, tişörtün etiket fiyatı olan x kaç TL’dir?',
 dogru=xt,yan=[(61,'Poşet ücretini eklememiş: 5x − 30 − 20 = 255.','dikkat'),(56,'Kuponu düşmemiş: 5x − 30 + 5 = 255.','dikkat'),(57,'Hem kuponu hem poşet ücretini hesaba katmamış: 5x − 30 = 255.','dikkat'),(48,'Şapka fiyatını x + 15 almış: 5x + 30 − 20 + 5 = 255.','dikkat')],
 istenen='Tişörtün etiket fiyatı x (TL).',ip=['Önce etiketlere göre 3 tişört ve 2 şapkanın tutarını x cinsinden yaz; sonra kupon ve poşet ücretini ekle.'],bilgi=[DEN,PAR],sekil=SK,
 ad=[A('Etiket tutarı','3 tişört ve 2 şapka.','3x + 2(x − 15) = 5x − 30'),A('Kupon ve poşet','Kupon düşülür, poşet eklenir.','5x − 30 − 20 + 5 = 5x − 45'),A('Denklem','Ödenen 255 TL’dir.','5x − 45 = 255'),A('Çöz','45 karşıya geçer, 5’e bölünür.','5x = 300 → x = 60')],
 puf='Kuponun işareti eksi, poşet ücretinin artı; ikisini ayrı ayrı yaz.')

# ================= 06 orta · çubuk modeli =================
xe=10; anne=4*xe; assert 4*xe+5==3*(xe+5)==45
assert 4*15==3*(15+5) and 4*20-5==3*(20+5) and len({xe,15,20,40,45})==5
bw=0.9
def bar(y,n,ek,ad):
    o=[f'\\node[anchor=east] at (-0.15,{y+0.35}) {{{ad}}};']
    for i in range(n): o.append(f'\\draw[thick] ({i*bw},{y}) rectangle ({(i+1)*bw},{y+0.7}); \\node at ({(i+0.5)*bw},{y+0.35}) {{$x$}};')
    if ek: o.append(f'\\draw[thick,fill=gray!20] ({n*bw},{y}) rectangle ({n*bw+0.7},{y+0.7}); \\node at ({n*bw+0.35},{y+0.35}) {{5}};')
    return '\n'.join(o)
SK=fig('\n'.join([bar(3.6,1,False,'Ece (bugün)'),bar(2.6,4,False,'Anne (bugün)'),bar(1.0,1,True,'Ece (5 yıl sonra)'),bar(0,4,True,'Anne (5 yıl sonra)')]))
q('0006',tipId='dns-bar',tip='Çubuk modeli ve yaş denklemi',z='orta',alt='Çubuk Modeli',kaz='Çubuk modelinden yaş ifadelerini yazıp oran denklemini çözer.',kalip='şekilli',
 kart='K-DNS-06 (çubuk modeli) · 4x + 5 = 3(x + 5)',
 metin='Şekilde Ece ile annesinin bugünkü ve 5 yıl sonraki yaşları çubuklarla gösterilmiştir; her “x” kutusu aynı uzunluktadır ve Ece’nin bugünkü yaşını (yıl cinsinden) temsil etmektedir. 5 yıl sonra annenin yaşı Ece’nin yaşının 3 katı olacaktır (şekil ölçekli çizilmemiştir).\nBuna göre, Ece’nin bugünkü yaşı kaçtır?',
 dogru=xe,yan=[(15,'Annenin 5 yılını denkleme koymamış: 4x = 3(x + 5).','dikkat'),(20,'Annenin yaşına 5 eklemek yerine 5 çıkarmış: 4x − 5 = 3(x + 5).','dikkat'),(40,'Annenin bugünkü yaşını (4x) yazmış.','dikkat'),(45,'Annenin 5 yıl sonraki yaşını yazmış.','dikkat')],
 istenen='Ece’nin bugünkü yaşı.',ip=['Çubuklardan annenin ve Ece’nin 5 yıl sonraki yaşlarını x cinsinden yaz; 3 katı ilişkisini kur.'],bilgi=[DEN,PAR],sekil=SK,
 ad=[A('Bugünkü yaşlar','Ece 1, anne 4 kutu.','Ece = x · Anne = 4x'),A('5 yıl sonra','İkisine de 5 eklenir.','Ece: x + 5 · Anne: 4x + 5'),A('Denklem','Anne, Ece’nin 3 katı.','4x + 5 = 3(x + 5)'),A('Çöz','Parantezi aç, düzenle.','4x + 5 = 3x + 15 → x = 10')],
 puf='5 yıl sonra iki yaşa da 5 eklenir; annenin yaşına eklemeyi unutma.')

# ================= 07 orta · çevresi verilen çokgen =================
xc=6; top_,adx,sag,ady=2*xc+3,xc-2,xc+2,2*xc+1; W=top_+adx; Hh=sag+ady; per=2*(W+Hh); assert per==80 and W==19 and Hh==21 and top_==15 and adx==4 and sag==8 and ady==13
lens=[W,sag,adx,ady,top_,Hh]; assert max(lens)==21 and sum(lens)==per
e=[xc,ady,top_,W]; assert len({21,*e})==5 and 12*xc+8==80
s=0.24; w2=top_*s; Wd=W*s; h1=sag*s; Ht=Hh*s
SK=fig(f'\\draw[thick] (0,0) -- ({Wd:.3f},0) -- ({Wd:.3f},{h1:.3f}) -- ({w2:.3f},{h1:.3f}) -- ({w2:.3f},{Ht:.3f}) -- (0,{Ht:.3f}) -- cycle;'
 f'\\node[above=2pt] at ({w2/2:.3f},{Ht:.3f}) {{$2x+3$}}; \\node[above=2pt] at ({(w2+Wd)/2:.3f},{h1:.3f}) {{$x-2$}}; \\node[right=3pt] at ({Wd:.3f},{h1/2:.3f}) {{$x+2$}}; \\node[right=3pt] at ({w2:.3f},{(h1+Ht)/2:.3f}) {{$2x+1$}};')
q('0007',tipId='dns-cevre',tip='Çevresi verilen şekilde denklem',z='orta',alt='Çevre ve Denklem',kaz='Dik kenarlı çokgenin çevresinden denklem kurup en uzun kenarı bulur.',kalip='şekilli',
 kart='K-DNS-07 (çevre) · 12x + 8 = 80',
 metin='Şekildeki çokgenin bütün kenarları birbirine dik ya da paraleldir; bazı kenarların uzunlukları cm cinsinden x’e bağlı olarak verilmiştir. Çokgenin çevresi 80 cm’dir.\nBuna göre, bu çokgenin en uzun kenarı kaç cm’dir?',
 dogru=21,yan=[(xc,'x değerini bulup sorulan uzunluk sanmış.','dikkat'),(ady,'Şekilde en uzun görünen etiketli düşey kenarı (2x + 1 = 13) en uzun sanmış.','dikkat'),(top_,'En uzun kenarı etiketli kenarlar arasından seçmiş: 2x + 3.','dikkat'),(W,'Etiketsiz kenarlardan alttakini (3x + 1) en uzun sanmış.','dikkat')],
 istenen='En uzun kenarın uzunluğu (cm).',ip=['Etiketsiz alt kenar ve sol kenarı, etiketli kenarların toplamı olarak x cinsinden yaz.'],bilgi=[CEV,DEN],sekil=SK,
 ad=[A('Genişlik','Alt kenar = üst kenar + basamağın yatay kenarı.','(2x + 3) + (x − 2) = 3x + 1'),A('Yükseklik','Sol kenar = sağ kenar + basamağın düşey kenarı.','(x + 2) + (2x + 1) = 3x + 3'),A('Denklem','Çevre = 2 × (genişlik + yükseklik).','2(6x + 4) = 80 → x = 6'),A('Kenarlar','x = 6 için kenarlar: 19, 8, 4, 13, 15, 21.','en uzun kenar = 3x + 3 = 21 cm')],
 puf='Etiketsiz kenarlar için karşılarındaki etiketli kenarları topla.')

# ================= 08 zor · iki doğrunun kesişimi =================
xa,ya=3,7; assert 3*xa-2==ya==-2*xa+13
e=[xa,ya,1+1,15+43]; assert 3*1-2==-2*1+3==1 and 3*15-2==2*15+13==43 and len({xa+ya,*e})==5
sx,sy=0.9,0.28
def pt(x,y,lab,anchor): return f'\\fill ({x*sx:.2f},{y*sy:.2f}) circle (0.07); \\node[{anchor}] at ({x*sx:.2f},{y*sy:.2f}) {{{lab}}};'
SK=fig(f'\\draw[-{{Stealth}}] (-0.4,0) -- (6.6,0) node[right] {{$x$}}; \\draw[-{{Stealth}}] (0,-0.9) -- (0,4.2) node[above] {{$y$}}; \\node[above left] at (0,0) {{O}};'
 f'\\draw[thick] ({-0.2*sx:.2f},{(-2.6)*sy:.2f}) -- ({4.2*sx:.2f},{10.6*sy:.2f}) node[right] {{$d_1$}}; \\draw[thick] (0,{13*sy:.2f}) -- ({6.2*sx:.2f},{0.6*sy:.2f}) node[right] {{$d_2$}};'
 +pt(0,-2,'$(0,-2)$','left=5pt')+pt(2,4,'$(2,4)$','right')+pt(0,13,'$(0,13)$','left=5pt')+pt(3,7,'A','right=7pt')+pt(5,3,'$(5,3)$','above right'))
q('0008',tipId='dns-grafik',tip='İki doğrunun kesişimi',z='zor',alt='Kesişen Doğrular',kaz='İki doğrunun denklemini grafikteki noktalardan yazıp kesişim noktasını bulur.',kalip='grafik',
 kart='K-DNS-08 (kesişen doğrular) · y = 3x − 2 ve y = −2x + 13',
 metin='Şekilde d₁ ve d₂ doğrularının grafikleri verilmiştir; doğrular üzerindeki işaretli noktaların koordinatları şekilde yazılıdır (şekil ölçekli çizilmemiştir). Bu iki doğru şekilde gösterilen A noktasında kesişmektedir.\nBuna göre, A noktasının apsisi ile ordinatının toplamı kaçtır?',
 dogru=xa+ya,yan=[(e[0],'Yalnız apsisi (3) yazmış.','dikkat'),(e[1],'Yalnız ordinatı (7) yazmış.','dikkat'),(e[2],'d₂ doğrusunun y eksenini kestiği yer olarak (5, 3) noktasının ordinatını almış: y = −2x + 3; kesişimi (1, 1) bulmuş.','dikkat'),(e[3],'d₂ doğrusunun eğimini +2 almış: y = 2x + 13; kesişimi (15, 43) bulmuş.','dikkat')],
 istenen='A noktasının koordinatları toplamı.',ip=['Her doğrunun eğimini iki işaretli noktadan hesapla; y eksenini kestiği noktayı kullanarak denklemini yaz.'],bilgi=[DOG,DEN],sekil=SK,
 ad=[A('d₁ denklemi','Eğim = (4 − (−2))/(2 − 0); y eksenini −2’de keser.','y = 3x − 2'),A('d₂ denklemi','Eğim = (3 − 13)/(5 − 0); y eksenini 13’te keser.','y = −2x + 13'),A('Eşitle','Kesişimde iki y değeri eşittir.','3x − 2 = −2x + 13 → 5x = 15 → x = 3'),A('Ordinat','x = 3 denklemde yerine yazılır.','y = 3 · 3 − 2 = 7'),A('Toplam','Apsis ve ordinat toplanır.','3 + 7 = 10')],
 puf='Kesişim noktasında iki denklemin y değerleri eşittir.')

# ================= 09 zor · sayı doğrusunda x'li noktalar =================
xn=4; K,L,M,N=2*xn-5,None,xn+7,4*xn-1; d=(M-K)//2; L=K+d; assert (M-K)%2==0 and N-K==3*d and (K,L,M,N)==(3,7,11,15)
e=[K+(N-K)//4*1,(K+N)//2,M,N]; assert e==[6,9,11,15] and (N-K)%4==0 and len({L,*e})==5
SK=fig('\\draw[-{Stealth}] (-0.4,0) -- (8.2,0);'+''.join(f'\\fill ({1.0+i*2.0},0) circle (0.08); \\node[above=4pt] at ({1.0+i*2.0},0) {{{n_}}};' for i,n_ in enumerate('KLMN'))
 +'\\node[below=4pt] at (1.0,0) {$2x-5$}; \\node[below=4pt] at (5.0,0) {$x+7$}; \\node[below=4pt] at (7.0,0) {$4x-1$};')
q('0009',tipId='dns-dogru',tip='Sayı doğrusunda x’li noktalar',z='zor',alt='Sayı Doğrusu',kaz='Eşit aralıklı noktaların x’li ifadelerinden denklem kurup bir noktanın değerini bulur.',kalip='şekilli',
 kart='K-DNS-09 (sayı doğrusu) · K = 2x − 5, M = x + 7, N = 4x − 1',
 metin='Şekildeki sayı doğrusunda ardışık iki noktası arasındaki uzaklıklar birbirine eşit olacak biçimde yerleştirilmiş K, L, M ve N noktalarından K, M ve N noktalarının gösterdiği sayılar x’e bağlı olarak verilmiştir.\nBuna göre, L noktasının gösterdiği sayı kaçtır?',
 dogru=L,yan=[(e[0],'K ile N arasını 4 eş parça sanmış (nokta sayısı): L = 3 + 12 ÷ 4.','dikkat'),(e[1],'L’yi K ile N’nin orta noktası sanmış: (3 + 15) ÷ 2.','dikkat'),(e[2],'L yerine M noktasının değerini yazmış.','dikkat'),(e[3],'L yerine N noktasının değerini yazmış.','dikkat')],
 istenen='L noktasının gösterdiği sayı.',ip=['K’dan M’ye ve K’dan N’ye kaç eş aralık olduğunu say; iki uzaklığı x cinsinden yaz.'],bilgi=[ORT,DEN],sekil=SK,
 ad=[A('Uzaklıklar','K’dan M’ye 2, K’dan N’ye 3 aralık vardır.','KM = (x + 7) − (2x − 5) = 12 − x · KN = (4x − 1) − (2x − 5) = 2x + 4'),A('Denklem','KN = 3 aralık, KM = 2 aralık: 3·KM = 2·KN.','3(12 − x) = 2(2x + 4) → 36 − 3x = 4x + 8'),A('x’i bul','Bilinmeyenler bir tarafa.','7x = 28 → x = 4'),A('L’yi bul','K = 3, M = 11; L bunların ortasındadır.','L = (3 + 11) ÷ 2 = 7')],
 puf='Aralık sayısını noktaları değil, noktalar arasındaki boşlukları sayarak bul.')

# ================= 10 orta · fiş (kampanya indirimi) =================
pey,zey=300,270; r=60; adet=4; ind=Fr(1,4); rec=Fr(adet*r)*(1-ind); tot=pey+zey+rec; assert rec==180 and tot==750
v=r; e=[Fr(tot-pey-zey,adet),rec/(adet*(1+ind)),rec/2,rec]
assert e==[45,36,90,180] and len({v,*e})==5 and pey+zey+3*r==tot
SK=tablo_svg(['Ürün','Miktar','Tutar (TL)'],[['Peynir','2 kg',str(pey)],['Zeytin','3 kg',str(zey)],['Reçel (%25 indirimli)','4 kavanoz','silinmiş'],['TOPLAM','',str(int(tot))]])
q('0010',tipId='dns-fis',tip='Kasa fişi',z='orta',alt='Kasa Fişi',kaz='Fişteki toplam tutar ve indirimden denklem kurup birim fiyatı bulur.',kalip='tablo',
 kart='K-DNS-10 (fiş) · 300 + 270 + 4r × 3/4 = 750',
 metin='Aşağıdaki tabloda bir marketin kasa fişi görülmektedir; reçel kavanozlarına %25 kampanya indirimi uygulanmış, indirimli tutar fişte silinmiştir, toplam tutar ise okunmaktadır. Reçelin bütün kavanozlarının indirimsiz birim fiyatı aynıdır.\nBuna göre, bir kavanoz reçelin indirimsiz fiyatı kaç TL’dir?',
 dogru=v,yan=[(e[0],'İndirimi hesaba katmamış: (750 − 570) ÷ 4.','dikkat'),(e[1],'İndirimi fiyata ekleyerek uygulamış: 180 ÷ (4 × 1,25).','dikkat'),(e[2],'İndirimli tutarı (180 TL) 2’ye bölmüş (peynirin miktarı).','dikkat'),(e[3],'İndirimli tutarı bulup kavanoz sayısına bölmeyi unutmuş.','dikkat')],
 istenen='Bir kavanoz reçelin indirimsiz fiyatı (TL).',ip=['Toplam tutardan diğer iki ürünün tutarını çıkararak reçelin ödenen tutarını bul; ödenen tutarın indirimsiz fiyatın kaçta kaçı olduğuna bak.'],bilgi=[DEN],sekil=SK,
 ad=[A('Reçelin ödenen tutarı','Toplamdan peynir ve zeytin çıkarılır.','750 − 300 − 270 = 180 TL'),A('Denklemi kur','4 kavanoz, fiyatın %75’i ödenir; r indirimsiz fiyat.','4 × r × 3/4 = 180 → 3r = 180'),A('Çöz','Her iki taraf 3’e bölünür.','r = 60 TL')],
 puf='%25 indirim, fiyatın %75’inin (3/4) ödenmesidir.')

bitir(P,'denklemsek','mat|Denklem Çözme')
