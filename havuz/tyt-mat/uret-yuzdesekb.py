"""Yüzde Problemleri · ŞEKİLLİ ek paket b (10 soru): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Yüzde Problemleri'
P=Parti('yuzdesekb','Yüzde Problemleri','prob|Yüzde Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu yüzde soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

YP=B('Yüzde','bir niceliğin yüzde p’si, niceliğin p/100 katıdır. Örnek: 80 sayısının %25’i 20’dir')
DOL=B('Doluluk oranı','doluluk yüzdesi, dolu kısmın kapasiteye oranıdır. Örnek: 40 litrelik bir kabın 10 litresi doluysa doluluk %25’tir')
KZ=B('Kâr yüzdesi','kâr yüzdesi, toplam kârın alış maliyetine oranıdır; zarar eksi kâr sayılır. Örnek: 200 TL’ye alınıp 250 TL’ye satılan ürünün kârı %25’tir')
ARD=B('Ardışık değişim','her yüzde değişim, bir önceki adımın sonucu üzerinden uygulanır; bu yüzden yüzdeler toplanmaz, katsayılar çarpılır. Örnek: %50 artış ve ardından %50 azalış, 1,5 × 0,5 = 0,75 katına, yani %25 azalışa yol açar')
ALN=B('Alan ve kenar değişimi','dikdörtgenin alanı kenarların çarpımıdır; kenarlar yüzdeyle değişince katsayılar çarpılır. Örnek: bir kenar 2 katına çıkıp diğeri yarıya inerse alan değişmez')
KOS=B('Koşullu yüzde','“… arasında yüzde kaç” sorusunda payda, koşulu sağlayan topluluğun tamamıdır. Örnek: 50 kişiden 20’si gözlüklüyse, gözlüklülerin 5’i kadınsa, gözlüklü kadınlar gözlüklülerin %25’idir')
AGC=B('Olasılık ağacı gibi yüzde ağacı','dal yüzdeleri çarpılarak bir koşulun bütündeki payı bulunur; sonra bu pay toplam içindeki oranla karşılaştırılır. Örnek: kişilerin %50’si kadın ve kadınların %20’si gözlüklüyse bütünün %10’u gözlüklü kadındır')
GRP=B('Grafik okuma ve toplam değişim','toplam değişim, ayrı ayrı yüzdelerin ortalaması değil, toplam değerlerin başlangıçtaki toplama göre değişimidir. Örnek: 10’dan 20’ye ve 90’dan 90’a çıkış toplamda 100’den 110’a, yani %10 artıştır')
KUR=B('Birimli simge grafiği','her simge belirli bir miktarı temsil eder; oran sorularında simge sayıları doğrudan oranlanabilir. Örnek: 6 simgenin 3’ü %50’dir')

kartla('K-YSB-01','Kap göstergesi','Dolu bölme sayısından doluluk yüzdesi ve litre bulunur; boşaltılan litre çıkarılıp yeni oran hesaplanır.','Litreyi yüzde gibi çıkarmak; boşaltılanı yüzde sanmak.','kolay','hikâyeli',4,'yzb-kap','Kap göstergesi ve doluluk')
kartla('K-YSB-02','Venn şeması','Koşulu sağlayan grup bulunur; istenen bölge sayısı bu grubun sayısına oranlanır.','Tüm öğrenciye oranlamak; kesişimi iki kez saymak.','orta','hikâyeli',3,'yzb-venn','Venn şeması ve yüzde')
kartla('K-YSB-03','Kâr–zarar tablosu','Her ürünün kâr ya da zararı adetle çarpılır, toplam alış maliyetine oranlanır.','Zararı yok saymak; yüzdelerin ortalamasını almak.','orta','tablo',4,'yzb-kar','Kâr–zarar tablosu')
kartla('K-YSB-04','Kare model (ızgara)','Boyalı ve boş kareler sayılır; kare başına düşen alan bulunup yüzdeyle çarpılır.','Boş alanı yüzdeyle çarpmamak; yüzdeyi tüm tarlaya uygulamak.','kolay','hikâyeli',4,'yzb-izgara','Kare model ve alan')
kartla('K-YSB-05','İşlem makinesi','Çıkıştan başlayıp ters işlemlerle giriş bulunur; yüzde işlemleri katsayıyla geri alınır.','Ters işlemi yüzde çıkararak yapmak; sırayı karıştırmak.','orta','yeni nesil',4,'yzb-makine','İşlem makinesi ve geri izleme')
kartla('K-YSB-06','Simge grafiği','Simge sayılarından toplam bulunur; istenen simgelerin toplama oranı yüzde olarak yazılır.','Simge sayısını adet sanmak; yanlış günleri toplamak.','kolay','grafik',3,'yzb-piktogram','Simge grafiği')
kartla('K-YSB-07','İki serili sütun grafiği','İki yılın toplamları ayrı ayrı bulunur, toplam artış başlangıç toplamına bölünür.','Yüzdelerin ortalamasını almak; farkı yüzde yazmak.','orta','grafik',4,'yzb-gruplu','İki serili sütun grafiği ve toplam artış')
kartla('K-YSB-08','Dikdörtgen kenar değişimi','Kenarlar yüzde katsayılarıyla çarpılır; yeni alan eski alanla karşılaştırılır.','Yüzdeleri toplamak; yalnız bir kenarı değiştirmek.','orta','hikâyeli',3,'yzb-alan','Kenar değişimi ve alan')
kartla('K-YSB-09','Oranlı tablo','Her satırdaki oran sayıyla çarpılıp parça sayısı bulunur; toplam parça toplam sayıya oranlanır.','Oranların aritmetik ortalamasını almak; erkek yüzdesini yazmak.','orta','tablo',4,'yzb-oranli','Oranlı tablo ve ağırlıklı yüzde')
kartla('K-YSB-10','Yüzde ağacı','Dal yüzdeleri çarpılarak bir makinedeki hatalı ürünün tüm üretimdeki payı bulunur.','Hata oranını cevap sanmak; yanlış dalın oranını çarpmak.','orta','hikâyeli',3,'yzb-agac','Yüzde ağacı ve dal çarpımı')

# ===== 01 kolay · akvaryum göstergesi =====
kap,say,dol,al=150,10,7,45
kalan=Fr(kap*dol,say)-al; v=kalan*100/kap
e=[Fr(dol*10-al),Fr(al*100,kap),kalan,dol*10]
assert kalan==60 and v==40 and e==[25,30,60,70] and len({v,*e})==5
o=['\\draw[thick] (0,3.6) -- (0,0) -- (3.2,0) -- (3.2,3.6);',f'\\filldraw[fill=vurgu!15,draw=none] (0.02,0.02) rectangle (3.18,{dol*0.36:.2f});',
   f'\\draw[thick,vurgu!80!black] (0,{dol*0.36:.2f}) -- (3.2,{dol*0.36:.2f});']
for i in range(1,say+1): o.append(f'\\draw (3.2,{i*0.36:.2f}) -- (3.55,{i*0.36:.2f});')
o.append('\\draw[<->] (3.85,0) -- (3.85,3.6); \\node[right,align=left] at (3.9,1.8) {tam dolu\\\\150 L};')
o.append('\\node at (1.6,-0.35) {Akvaryum (bölmeler eşit)};')
SK=fig('\n'.join(o))
q('0001',tipId='yzb-kap',tip='Kap göstergesi ve doluluk',z='kolay',alt='Kap Göstergesi',kaz='Kap üzerindeki eş bölmelerden doluluğu okuyup boşaltılan miktardan sonra yeni doluluk yüzdesini bulur.',kalip='hikâyeli',
 kart='K-YSB-01 · 10 bölme, 7 dolu, 150 L, 45 L boşaltma',
 metin='Bir evde bakım yapılacak akvaryumdaki suyun seviyesi şekilde gösterilmiştir; kabın eş bölmeli olduğu ve kapasitesinin yanında belirtildiği görülmektedir. Bakım için akvaryumdan 45 litre su boşaltılıyor ve başka hiçbir yere su aktarılmıyor ya da eklenmiyor.\nBuna göre, boşaltmadan sonra akvaryumun doluluk oranı yüzde kaçtır?',
 dogru=v,yan=[(e[0],'Boşaltılan 45 litreyi %45 gibi düşünüp %70’ten çıkarmış: 70 − 45.','dikkat'),(e[1],'Kalan doluluk yerine boşaltılan suyun kapasiteye oranını bulmuş: 45 ÷ 150.','dikkat'),(e[2],'Kalan suyu (60 litre) yüzde sanmış.','dikkat'),(e[3],'Boşaltmayı hiç hesaba katmamış; ilk doluluğu yazmış.','dikkat')],
 istenen='Boşaltma sonrası doluluk oranı (%).',ip=['Önce şekildeki dolu bölme sayısından akvaryumdaki su miktarını litre olarak bul.'],bilgi=[DOL],sekil=SK,
 ad=[A('İlk su miktarı','Dolu bölmeler kapasitenin 7/10’udur.','150 × 7/10 = 105 L'),A('Boşaltma sonrası','Boşaltılan su çıkarılır.','105 − 45 = 60 L'),A('Oran','Kalan su kapasiteye bölünür.','60 ÷ 150 = 0,4'),A('Yüzde','Oran yüzdeye çevrilir.','%40')],
 puf='Litreleri yüzdeye ancak kapasiteye bölerek çevirebilirsin.')

# ===== 02 orta · Venn =====
t,b,m,h=30,20,45,105; top=t+b+m+h; ntiy=m+h; v=Fr(m*100,ntiy)
e=[Fr((m+b)*100,top),Fr(m*100,top),Fr(b*100,t+b),Fr(h*100,ntiy)]
assert top==200 and ntiy==150 and v==30 and e==[Fr(65,2)*1,Fr(45,2),40,70] and len({v,*e})==5
o=['\\draw[thick] (0,0) rectangle (7.2,4.1);','\\draw[thick,fill=vurgu!15,fill opacity=0.6] (2.6,1.9) circle (1.35); \\draw[thick,fill=vurgu!30,fill opacity=0.5] (4.6,1.9) circle (1.35);',
   '\\node at (2.0,3.75) {Tiyatro}; \\node at (5.2,3.75) {Müzik};',f'\\node at (1.95,1.9) {{{t}}}; \\node at (3.6,1.9) {{{b}}}; \\node at (5.25,1.9) {{{m}}}; \\node at (6.4,0.4) {{{h}}};']
SK=fig('\n'.join(o))
q('0002',tipId='yzb-venn',tip='Venn şeması ve yüzde',z='orta',alt='Venn Şeması',kaz='Venn şemasındaki bölgelerden koşullu bir grubun yüzdesini hesaplar.',kalip='hikâyeli',
 kart='K-YSB-02 · 30, 20, 45, 105; tiyatro dışı içinde yalnız müzik',
 metin='Bir lisede tiyatro ve müzik kulüpleri bulunmaktadır. Okuldaki her öğrencinin bu kulüplere üyeliği şekildeki Venn şemasında öğrenci sayısı olarak gösterilmiştir; dikdörtgen okulun bütün öğrencilerini, bölgelerdeki sayılar o bölgedeki öğrenci sayısını belirtir. Rehber öğretmen, tiyatro kulübüne üye olmayan öğrencilerle bir anket yapacaktır.\nBuna göre, tiyatro kulübüne üye olmayan öğrencilerin yüzde kaçı müzik kulübüne üyedir?',
 dogru=v,yan=[(e[0],'Müzik kulübünün tüm üyelerini (65) bütün öğrencilere oranlamış: 65 ÷ 200.','dikkat'),(e[1],'Yalnız müzik üyelerini bütün öğrencilere oranlamış: 45 ÷ 200.','dikkat'),(e[2],'Tiyatro üyelerinin içindeki ortak üyeleri oranlamış: 20 ÷ 50.','dikkat'),(e[3],'Hiçbir kulübe üye olmayanları tiyatro dışındakilere oranlamış: 105 ÷ 150.','dikkat')],
 istenen='Tiyatro dışındaki öğrencilerde müzik üyelerinin yüzdesi.',ip=['Önce “tiyatro kulübüne üye olmayan” öğrencilerin hangi bölgelerde olduğunu belirle; yüzde bu grubun sayısına göre alınacak.'],bilgi=[KOS],sekil=SK,
 ad=[A('Tiyatro dışı','Tiyatro çemberinin dışındaki bölgeler toplanır.','45 + 105 = 150'),A('İstenen kesim','Bunların içinde müzik kulübünde olanlar yalnız müzik bölgesindedir.','45'),A('Yüzde','Pay, tiyatro dışındakilerin sayısına bölünür.','45 ÷ 150 = %30')],
 puf='Payda her zaman koşulu sağlayan grubun sayısıdır.')

# ===== 03 orta · kâr–zarar tablosu =====
ur=[('Tava',200,260,10),('Tencere',300,330,20),('Çaydanlık',125,110,8)]
mal=sum(a*n for _,a,s,n in ur); kar=sum((s-a)*n for _,a,s,n in ur); v=Fr(kar*100,mal)
kar_pos=sum((s-a)*n for _,a,s,n in ur if s>a); ort=Fr(sum(Fr((s-a)*100,a) for _,a,s,n in ur if s>a),2)
yp=sum(Fr((s-a)*100,a) for _,a,s,n in ur)
e=[Fr(kar_pos*100,sum(a*n for _,a,s,n in ur if s>a)),ort,yp,kar]
assert mal==9000 and kar==1080 and v==12 and e==[15,20,28,1080] and len({v,*e})==5
SK=tablo_svg(['Ürün','Alış fiyatı (TL)','Satış fiyatı (TL)','Satılan adet'],[[n,str(a),str(s),str(k)] for n,a,s,k in ur])
q('0003',tipId='yzb-kar',tip='Kâr–zarar tablosu',z='orta',alt='Kâr–Zarar Tablosu',kaz='Tablodaki alış–satış fiyatı ve adetlerden toplam kâr yüzdesini hesaplar.',kalip='tablo',
 kart='K-YSB-03 · maliyet 9 000, kâr 1 080',
 metin='Bir mutfak eşyası mağazası, bir haftada sattığı üç üründen her birini aşağıdaki tabloda verilen birim fiyatlarla almış ve satmıştır; satılan adetler de tabloda gösterilmiştir. Haftanın sonunda hiç stok kalmamış, ürünlerin dışında başka gelir ya da gider olmamıştır.\nBuna göre, mağazanın bu üç üründen elde ettiği toplam kâr, toplam alış maliyetinin yüzde kaçıdır?',
 dogru=v,yan=[(e[0],'Zarar eden çaydanlığı hesaba katmamış: 1 200 ÷ 8 000.','dikkat'),(e[1],'Yalnız kâr eden iki ürünün kâr yüzdelerinin ortalamasını almış: (30 + 10) ÷ 2.','dikkat'),(e[2],'Her ürünün kâr (zarar) yüzdesini ayrı bulup toplamış: 30 + 10 − 12.','dikkat'),(e[3],'Net kâr tutarını (1 080 TL) yüzde olarak yazmış.','dikkat')],
 istenen='Toplam kârın toplam alış maliyetine oranı (%).',ip=['Her ürün için (satış − alış) farkını adetle çarpıp kâr ya da zararı bul; zararı eksi işaretle kâra kat.'],bilgi=[KZ],sekil=SK,
 ad=[A('Toplam maliyet','Alış fiyatı × adet toplanır.','2000 + 6000 + 1000 = 9000 TL'),A('Ürün kârları','Tava +600, tencere +600, çaydanlık −120.','600 + 600 − 120 = 1080 TL'),A('Oran','Net kâr, maliyete bölünür.','1080 ÷ 9000 = 0,12'),A('Yüzde','Oran yüzdeye çevrilir.','%12')],
 puf='Yüzdeleri ürün ürün toplamak yerine toplam kârı toplam maliyete böl.')

# ===== 04 kolay · tarla ızgarası =====
alan=2400; kare=alan//100; dom=25; bib=15; bos=100-dom-bib; ay=bos*75//100
v=ay*kare
e=[bib*kare,dom*kare,(dom+bib)*75//100*kare,bos*kare]
assert kare==24 and bos==60 and ay==45 and v==1080 and e==[360,600,720,1440] and len({v,*e})==5
o=[]
for r in range(10):
    for c in range(10):
        f='vurgu!45' if (c<5 and r<5) else 'vurgu!15' if (5<=c<8 and r<5) else 'white'
        o.append(f'\\filldraw[fill={f},draw=gray] ({c*0.42:.2f},{-r*0.42:.2f}) rectangle ({(c+1)*0.42:.2f},{-(r+1)*0.42:.2f});')
o.append('\\draw[thick] (0,0) rectangle (4.2,-4.2);')
o.append('\\filldraw[fill=vurgu!45,draw=gray] (4.7,-0.5) rectangle (5.1,-0.9); \\node[right] at (5.15,-0.7) {domates};')
o.append('\\filldraw[fill=vurgu!15,draw=gray] (4.7,-1.3) rectangle (5.1,-1.7); \\node[right] at (5.15,-1.5) {biber};')
o.append('\\filldraw[fill=white,draw=gray] (4.7,-2.1) rectangle (5.1,-2.5); \\node[right] at (5.15,-2.3) {boş};')
SK=fig('\n'.join(o))
q('0004',tipId='yzb-izgara',tip='Kare model ve alan',z='kolay',alt='Kare Model',kaz='Eş karelere bölünmüş tarla planında kare sayılarından alan ve yüzde hesaplar.',kalip='hikâyeli',
 kart='K-YSB-04 · 100 kare, 2 400 m², boşun %75’i',
 metin='Alanı 2 400 m² olan bir tarlanın planı şekilde, birbirinin aynı olan karelere bölünerek gösterilmiştir; domates ve biber ekilen kısımlar boyalıdır. Çiftçi, tarlada ekili olmayan (boş) kısmın %75’ine ayçiçeği ekecektir.\nBuna göre, ayçiçeği ekilecek alan kaç m² olur?',
 dogru=v,yan=[(e[0],'Yalnız biber alanını bulmuş: 15 kare × 24 m².','dikkat'),(e[1],'Yalnız domates alanını bulmuş: 25 kare × 24 m².','dikkat'),(e[2],'Boş alan yerine ekili alanın %75’ini hesaplamış: 40 karenin %75’i.','dikkat'),(e[3],'Boş alanın tamamını bulup %75 işlemini yapmamış: 60 × 24.','dikkat')],
 istenen='Ayçiçeği ekilecek alan (m²).',ip=['Karelerin sayısını kullanarak bir karenin kaç m² olduğunu bul; boş kare sayısını da say.'],bilgi=[YP],sekil=SK,
 ad=[A('Bir kare','Tarla 100 eş kareye bölünmüştür.','2400 ÷ 100 = 24 m²'),A('Boş kare','Boyalı kareler çıkarılır.','100 − 25 − 15 = 60'),A('Ayçiçeği karesi','Boş karelerin %75’i.','60 × 75/100 = 45'),A('Alan','Kare sayısı birim alanla çarpılır.','45 × 24 = 1080 m²')],
 puf='Önce bir karenin alanını bul.')

# ===== 05 zor · işlem makinesi (yeni nesil) =====
cik=1100; ekle=20; s1=cik-ekle; s2=Fr(s1*100,75); x=s2*100/120
assert s1==1080 and s2==1440 and x==1200
e=[s1,s2,Fr(1080)*Fr(5,4)/Fr(6,5),cik*Fr(6,5)*Fr(3,4)]
assert e==[1080,1440,1125,990] and len({x,*e})==5
bx=lambda x,y,txt,w=1.9: f'\\node[draw,thick,rounded corners=3pt,fill=vurgu!12,minimum width={w}cm,minimum height=1.3cm,align=center,inner sep=3pt] at ({x},{y}) {{{txt}}};'
o=[bx(0,0,'Giriş\\\\x',1.5),bx(3.2,0,'Sayının\\\\\\%20 fazlasını\\\\al',2.3),bx(6.6,0,'Sonucun\\\\\\%25 eksiğini\\\\al',2.3),bx(6.6,-2.1,'Sonuca\\\\20 ekle',2.3),bx(3.2,-2.1,'Çıkış',2.3)]
o+=['\\draw[-{Stealth},thick] (0.75,0) -- (2.05,0);','\\draw[-{Stealth},thick] (4.35,0) -- (5.45,0);','\\draw[-{Stealth},thick] (6.6,-0.65) -- (6.6,-1.45);','\\draw[-{Stealth},thick] (5.45,-2.1) -- (4.35,-2.1);']
SK=fig('\n'.join(o))
q('0005',tipId='yzb-makine',tip='İşlem makinesi ve geri izleme',z='orta',alt='İşlem Makinesi',kaz='Yüzde işlemleri içeren bir işlem makinesinde çıkıştan geriye giderek girişi bulur.',kalip='yeni nesil',
 kart='K-YSB-05 · +%20, −%25, +20; çıkış 1 100',
 metin='Şekildeki işlem makinesi, girişe verilen pozitif x sayısına kutulardaki işlemleri okların yönünde sırayla uygular ve sonucu çıkışta gösterir. Her kutudaki işlem, yalnız o kutuya gelen sayı üzerinden yapılır; makine yuvarlama yapmaz. Makinenin çıkışında 1 100 sayısı görülmüştür.\nBuna göre, girişe verilen x sayısı kaçtır?',
 dogru=x,yan=[(e[0],'Yalnız “20 ekle” işlemini geri almış; yüzde kutularını atlamış.','dikkat'),(e[1],'Son iki işlemi geri almış; ilk yüzde kutusunu geri almamış.','dikkat'),(e[2],'%25 eksiğini geri alırken 1 080’e %25 eklemiş, sonra %20 fazlasını geri almış: 1 080 × 1,25 ÷ 1,2.','islem'),(e[3],'İşlemleri geri almak yerine çıkışa ileri yönde uygulamış: 1 100 × 1,2 × 0,75.','dikkat')],
 istenen='Girişe verilen x sayısı.',ip=['Çıkıştan başlayıp işlemleri sondan başa doğru, her birinin tersini alarak geri izle.'],bilgi=[ARD],sekil=SK,
 ad=[A('Eklemeyi geri al','Son kutu 20 eklemişti.','1100 − 20 = 1080'),A('İkinci kutuyu geri al','Önceki sayının %75’i 1 080 ise önceki sayı:','1080 ÷ 0,75 = 1440'),A('Birinci kutuyu geri al','Giriş sayısının 1,2 katı 1 440 ise giriş:','1440 ÷ 1,2 = 1200')],
 puf='Yüzde işlemlerinin tersi, çarpan katsayısına bölmektir.')

# ===== 06 kolay · simge grafiği =====
gun=[('Cuma',5),('Cumartesi',8),('Pazar',4),('Pazartesi',3)]; sm=25; T=sum(s for _,s in gun); ist=5+3
v=Fr(ist*100,T); e=[ist,3*100//T,T,5*100//T]
assert T==20 and v==40 and e==[8,15,20,25] and len({v,*e})==5
o=[]
for i,(nm,s) in enumerate(gun):
    y=-i*0.8
    o.append(f'\\node[left] at (-0.1,{y}) {{{nm}}};')
    for j in range(s): o.append(f'\\filldraw[fill=vurgu!45,draw=vurgu!80!black] ({0.25+j*0.5:.2f},{y}) circle (0.19);')
o.append(f'\\filldraw[fill=vurgu!45,draw=vurgu!80!black] (0.25,-3.4) circle (0.19); \\node[right] at (0.5,-3.4) {{: {sm} ekmek}};')
SK=fig('\n'.join(o))
q('0006',tipId='yzb-piktogram',tip='Simge grafiği',z='kolay',alt='Simge Grafiği',kaz='Simge grafiğinden toplamı bulup seçilen günlerin toplam içindeki yüzdesini hesaplar.',kalip='grafik',
 kart='K-YSB-06 · 5, 8, 4, 3 simge',
 metin='Bir mahalle fırını, bir hafta sonu etkinliği için dört günde sattığı ekmek sayısını şekildeki simge grafiğiyle göstermiştir; her simge aynı sayıda ekmeği temsil etmektedir ve tüm simgeler tamdır. Fırın sahibi, cuma ve pazartesi günlerini “hafta içi satış” olarak adlandırmaktadır.\nBuna göre, hafta içi satış, bu dört günde satılan ekmeklerin yüzde kaçıdır?',
 dogru=v,yan=[(e[0],'Cuma ve pazartesi simge sayısının toplamını (8) yüzde sanmış.','dikkat'),(e[1],'Yalnız pazartesi gününün payını bulmuş: 3 ÷ 20.','dikkat'),(e[2],'Toplam simge sayısını (20) yüzde sanmış.','dikkat'),(e[3],'Yalnız cuma gününün payını bulmuş: 5 ÷ 20.','dikkat')],
 istenen='Hafta içi satışın toplam satışa oranı (%).',ip=['Her simgenin değeri toplam ve parça için aynıdır; simge sayılarını doğrudan oranlayabilirsin.'],bilgi=[KUR],sekil=SK,
 ad=[A('Toplam simge','Dört günün simge sayıları toplanır.','5 + 8 + 4 + 3 = 20'),A('Hafta içi simge','Cuma ve pazartesi.','5 + 3 = 8'),A('Yüzde','Parça, toplama bölünür.','8 ÷ 20 = %40')],
 puf='Simgelerin her biri aynı değerdeyse oran simge sayısından bulunur.')

# ===== 07 orta · iki serili sütun =====
mg=[('A',40,50),('B',60,66),('C',100,110)]; t23=sum(a for _,a,b2 in mg); t24=sum(b2 for _,a,b2 in mg); v=Fr((t24-t23)*100,t23)
ort=Fr(sum(Fr((b2-a)*100,a) for _,a,b2 in mg),3)
e=[Fr(25),ort,t24-t23,Fr(t24*100,t23)]
assert t23==200 and t24==226 and v==13 and e==[25,15,26,113] and len({v,*e})==5
sy=0.026; o=['\\draw[-{Stealth}] (0,0) -- (5.6,0); \\draw[-{Stealth}] (0,0) -- (0,3.3) node[above] {Satış (bin TL)};']
for tv in (20,40,60,80,100,120): o.append(f'\\draw[gray!50,dashed] (0,{tv*sy:.2f}) -- (5.3,{tv*sy:.2f}); \\draw (-0.06,{tv*sy:.2f}) -- (0.06,{tv*sy:.2f}); \\node[left=2pt] at (0,{tv*sy:.2f}) {{{tv}}};')
for i,(nm,a,b2) in enumerate(mg):
    x=0.5+i*1.7
    o.append(f'\\filldraw[fill=vurgu!10,draw=vurgu!80!black] ({x:.2f},0) rectangle ({x+0.55:.2f},{a*sy:.2f}); \\filldraw[fill=vurgu!55,draw=vurgu!80!black] ({x+0.55:.2f},0) rectangle ({x+1.1:.2f},{b2*sy:.2f});')
    o.append(f'\\node[below=2pt] at ({x+0.55:.2f},0) {{{nm}}};')
o.append('\\filldraw[fill=vurgu!10,draw=vurgu!80!black] (5.9,2.6) rectangle (6.2,2.9); \\node[right] at (6.25,2.75) {2023}; \\filldraw[fill=vurgu!55,draw=vurgu!80!black] (5.9,2.0) rectangle (6.2,2.3); \\node[right] at (6.25,2.15) {2024};')
SK=fig('\n'.join(o))
q('0007',tipId='yzb-gruplu',tip='İki serili sütun grafiği ve toplam artış',z='orta',alt='İki Serili Sütun Grafiği',kaz='İki serili sütun grafiğinden iki yılın toplam satışını bulup toplam artış yüzdesini hesaplar.',kalip='grafik',
 kart='K-YSB-07 · 200 → 226 bin TL',
 metin='Bir zincirin A, B ve C mağazalarının 2023 ve 2024 yıllarındaki yıllık satış tutarları (bin TL) şekildeki sütun grafikte verilmiştir. Zincirin genel müdürü, üç mağazanın birlikte satışının bir yılda ne kadar değiştiğini öğrenmek istemektedir; grafikteki mağazalar dışında satış yapılmamıştır.\nBuna göre, üç mağazanın toplam satışı 2023’e göre yüzde kaç artmıştır?',
 dogru=v,yan=[(e[0],'Yalnız A mağazasının artış yüzdesini yazmış: 10 ÷ 40.','dikkat'),(e[1],'Üç mağazanın artış yüzdelerinin ortalamasını almış: (25 + 10 + 10) ÷ 3.','dikkat'),(e[2],'Artış miktarını (26 bin TL) yüzde olarak yazmış.','dikkat'),(e[3],'Artış yüzdesi yerine 2024 toplamının 2023 toplamına oranını (%113) yazmış.','dikkat')],
 istenen='Toplam satışın artış yüzdesi.',ip=['İki yılın toplam satışını ayrı ayrı bul; artışı 2023 toplamına oranla.'],bilgi=[GRP],sekil=SK,
 ad=[A('2023 toplamı','Açık sütunlar toplanır.','40 + 60 + 100 = 200'),A('2024 toplamı','Koyu sütunlar toplanır.','50 + 66 + 110 = 226'),A('Artış','Farkın alınması.','226 − 200 = 26'),A('Yüzde','Artış, 2023 toplamına bölünür.','26 ÷ 200 = %13')],
 puf='Toplam değişimi, toplamlar üzerinden hesapla.')

# ===== 08 orta · dikdörtgen bahçe =====
uz,kı=30,20; A0=uz*kı; yeni=Fr(uz*120,100)*Fr(kı*75,100)
e=[A0-yeni,A0*Fr(95,100),Fr(uz*120,100)*kı,uz*Fr(kı*75,100)]
assert A0==600 and yeni==540 and e==[60,570,720,450] and len({yeni,*e})==5
o=['\\draw[thick] (0,0) rectangle (5.4,3.6);','\\draw[<->] (0,-0.35) -- (5.4,-0.35); \\node[below=1pt] at (2.7,-0.35) {30 m};','\\draw[<->] (5.8,0) -- (5.8,3.6); \\node[right] at (5.85,1.8) {20 m};','\\node at (2.7,1.8) {Bahçe};']
SK=fig('\n'.join(o))
q('0008',tipId='yzb-alan',tip='Kenar değişimi ve alan',z='orta',alt='Kenar Değişimi',kaz='Dikdörtgenin iki kenarı yüzdeyle değişince yeni alanı hesaplar.',kalip='hikâyeli',
 kart='K-YSB-08 · 30×20; +%20, −%25',
 metin='Dikdörtgen biçimli bir okul bahçesinin boyutları şekilde verilmiştir. Bahçenin yeniden düzenlenmesinde uzun kenarı %20 uzatılacak, kısa kenarı ise %25 kısaltılacak ve bahçe yine dikdörtgen biçiminde kalacaktır; şekil ölçekli çizilmemiştir.\nBuna göre, düzenlemeden sonra bahçenin alanı kaç m² olur?',
 dogru=yeni,yan=[(e[0],'Yeni alan yerine alandaki azalma miktarını bulmuş: 600 − 540.','dikkat'),(e[1],'Yüzdeleri toplamış: %20 − %25 = −%5, yani alan 600 × 0,95.','dikkat'),(e[2],'Yalnız uzun kenarı %20 artırmış, kısa kenarı değiştirmemiş: 36 × 20.','dikkat'),(e[3],'Yalnız kısa kenarı %25 azaltmış, uzun kenarı değiştirmemiş: 30 × 15.','dikkat')],
 istenen='Yeni bahçenin alanı (m²).',ip=['Önce yeni kenar uzunluklarını bul; alanı onlardan hesapla.'],bilgi=[ALN],sekil=SK,
 ad=[A('Yeni uzun kenar','%20 artış, 1,2 katı.','30 × 1,2 = 36 m'),A('Yeni kısa kenar','%25 azalış, 0,75 katı.','20 × 0,75 = 15 m'),A('Yeni alan','Kenarlar çarpılır.','36 × 15 = 540 m²')],
 puf='Yüzdeler alan üzerinde toplanmaz; kenarlar ayrı ayrı değişir.')

# ===== 09 orta · oranlı tablo =====
br=[('Basketbol',80,25),('Voleybol',100,70),('Yüzme',120,40)]; N=sum(n for _,n,_ in br); kz=sum(n*p//100 for _,n,p in br)
assert all(n*p%100==0 for _,n,p in br); v=Fr(kz*100,N); ortp=Fr(sum(p for _,_,p in br),3)
e=[ortp,100-v,kz,N-kz]
assert N==300 and kz==138 and v==46 and e==[45,54,138,162] and len({v,*e})==5
SK=tablo_svg(['Branş','Katılan öğrenci sayısı','Kızların oranı (%)'],[[n,str(k),f'%{p}'] for n,k,p in br])
q('0009',tipId='yzb-oranli',tip='Oranlı tablo ve ağırlıklı yüzde',z='orta',alt='Oranlı Tablo',kaz='Tabloda her satırdaki oranı sayıyla çarpıp toplamın yüzdesini hesaplar.',kalip='tablo',
 kart='K-YSB-09 · 80/%25, 100/%70, 120/%40',
 metin='Bir okulun yaz spor kursuna katılan öğrencilerin sayıları ve her branştaki kızların oranı aşağıdaki tabloda verilmiştir. Her öğrenci yalnız bir branşa kayıtlıdır ve tabloda gösterilen branşlar dışında kurs açılmamıştır. Okul müdürlüğü, kurs raporunda kız öğrencilerin genel payını belirtecektir.\nBuna göre, kursa katılan tüm öğrencilerin yüzde kaçı kızdır?',
 dogru=v,yan=[(e[0],'Üç branşın kız oranlarının aritmetik ortalamasını almış: (25 + 70 + 40) ÷ 3.','dikkat'),(e[1],'Kız yüzdesi yerine erkeklerin yüzdesini yazmış: 100 − 46.','dikkat'),(e[2],'Kız öğrenci sayısını (138) yüzde sanmış.','dikkat'),(e[3],'Erkek öğrenci sayısını (162) yüzde sanmış.','dikkat')],
 istenen='Kız öğrencilerin tüm katılımcılara oranı (%).',ip=['Her branştaki kız sayısını, oranı o branşın öğrenci sayısıyla çarparak bul.'],bilgi=[YP],sekil=SK,
 ad=[A('Kız sayıları','Her satırda sayı × oran.','20 + 70 + 48'),A('Toplam kız','Üç sayı toplanır.','20 + 70 + 48 = 138'),A('Toplam öğrenci','Üç branşın öğrencileri.','80 + 100 + 120 = 300'),A('Yüzde','Kızlar toplama bölünür.','138 ÷ 300 = %46')],
 puf='Oranların ortalaması, grup büyüklükleri farklıyken genel oranı vermez.')

# ===== 10 zor · yüzde ağacı =====
pa,pb=60,40; ha,hb=Fr(5),Fr(5,2)
a_h=Fr(pa)*ha/100; b_h=Fr(pb)*hb/100; v=a_h
e=[b_h,Fr(pa)*hb/100,Fr(pb)*ha/100,hb]
assert a_h==3 and b_h==1 and v==3 and e==[1,Fr(3,2),2,Fr(5,2)] and len({v,*e})==5
o=['\\node[draw,circle,fill=vurgu!10,inner sep=3pt] (r) at (0,0) {Ürün};',
 '\\node[draw,circle,fill=vurgu!25,inner sep=4pt] (a) at (3.2,1.7) {A}; \\node[draw,circle,fill=vurgu!25,inner sep=4pt] (b) at (3.2,-1.7) {B};',
 '\\draw[thick] (r) -- node[above left=-1pt] {\\%60} (a); \\draw[thick] (r) -- node[below left=-1pt] {\\%40} (b);',
 '\\node[right] (h1) at (6.3,2.3) {Hatalı}; \\node[right] (s1) at (6.3,1.1) {Sağlam}; \\node[right] (h2) at (6.3,-1.1) {Hatalı}; \\node[right] (s2) at (6.3,-2.3) {Sağlam};',
 '\\draw[thick] (a) -- node[above,sloped] {\\%5} (h1.west); \\draw[thick] (a) -- node[below=2pt,sloped] {\\%95} (s1.west); \\draw[thick] (b) -- node[above,sloped] {\\%2,5} (h2.west); \\draw[thick] (b) -- node[below=2pt,sloped] {\\%97,5} (s2.west);']
SK=fig('\n'.join(o))
q('0010',tipId='yzb-agac',tip='Yüzde ağacı ve dal çarpımı',z='orta',alt='Yüzde Ağacı',kaz='Yüzde ağacındaki dal oranlarını çarparak bir makinenin hatalı ürünlerinin tüm üretimdeki yüzdesini bulur.',kalip='hikâyeli',
 kart='K-YSB-10 · A %60 (%5 hatalı), B %40 (%2,5 hatalı)',
 metin='Bir tekstil fabrikasında üretilen gömlekler A ve B makinelerinde dikilmektedir; her gömlek yalnız bir makinede dikilir. Üretimin makinelere dağılımı ve her makinenin hatalı gömlek oranı şekildeki ağaç şemasında verilmiştir. Üretim sonunda gömleklerin tamamı kalite kontrolden geçirilmiştir.\nBuna göre, A makinesinde dikilen hatalı gömlekler, tüm üretimin yüzde kaçıdır?',
 dogru=v,yan=[(e[0],'B makinesinin hatalı gömleklerini bulmuş: 40 × 2,5/100.','dikkat'),(e[1],'A’nın üretim payını B’nin hata oranıyla çarpmış: 60 × 2,5/100.','dikkat'),(e[2],'B’nin üretim payını A’nın hata oranıyla çarpmış: 40 × 5/100.','dikkat'),(e[3],'B makinesinin hata oranını (%2,5) cevap sanmış.','dikkat')],
 istenen='A’nın hatalı gömleklerinin tüm üretimdeki yüzdesi.',ip=['Ağaçta A koluna ve oradan hatalı dalına giden oranların birlikte ne anlama geldiğini düşün.'],bilgi=[AGC],sekil=SK,
 ad=[A('A’nın payı','Üretimin %60’ı A’dadır.','60/100'),A('A’da hatalı oran','A’nın gömleklerinin %5’i hatalıdır.','5/100'),A('Çarpım','Oranlar çarpılır.','60 × 5/100 = %3')],
 puf='Ardışık dalların yüzdeleri çarpılır.')

bitir(P,'yuzdesekb','prob|Yüzde Problemleri')
