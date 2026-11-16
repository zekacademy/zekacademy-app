"""Sayı Problemleri · ŞEKİLLİ paket (10 soru): şekil/tablo çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Sayı Problemleri'
P=Parti('sayisek','Sayı Problemleri','prob|Sayı Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu problem soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

ET=B('Birim fiyat ve toplam tutar','toplam tutar = adet × birim fiyat; para üstü = verilen para − toplam tutar. Örnek: 3 adet 14 TL’lik üründen 50 TL ile alışveriş yapılırsa para üstü 50 − 42 = 8 TL')
ISL=B('Ters işlem','bir işlem zincirinde girişi bulmak için çıkıştan başlayıp her işlemin tersi (+ ↔ −, × ↔ ÷) ters sırayla uygulanır. Örnek: ×2 sonra +1 ile 9 çıkıyorsa giriş (9 − 1) ÷ 2 = 4')
TB=B('Tablo okuma ve eşitlik','toplam, bilinen ve bilinmeyen parçaların toplamına eşittir; bilinmeyen parça toplamdan bilinenler çıkarılarak bulunur. Örnek: 20 = 6 + 9 + a ise a = 5')
TE=B('Terazi ve denklem','denge halinde iki kefedeki kütleler eşittir; iki dengeden iki bilinmeyenli denklem kurulur. Örnek: 2a = 10 ve a + b = 9 ise a = 5, b = 4')
SAY=B('Sayma ve çarpma ilkesi','düzenli dizilmiş eş gruplarda toplam, grup sayısı × bir gruptaki sayıdır; katman sayısı da çarpıma girer. Örnek: 2 sıra × 5 sütun × 3 kat = 30 birim')
ARD=B('Piramit ve cebirsel toplam','üstteki kutu altındaki iki kutunun toplamıdır; ortadaki kutular iki kez sayılır. Örnek: tabanı a, b, c olan 3 katlı piramitte tepe a + 2b + c olur')
MEN=B('Koşullu sayı problemi','koşullar bilinmeyenleri tek bir bilinmeyene indirger; bulunan değer tüm koşullarla ve tam sayı olma şartıyla denetlenir. Örnek: a + b = 7 ve b = 2a ise 3a = 7 olur, tam sayı olmadığından bu durum olamaz')

# ---------- kartlar ----------
kartla('K-SYS-01','Fiyat etiketli raf ve para üstü','Etiketlerden birim fiyatlar okunur; adetle çarpılıp toplanır, verilen paradan çıkarılarak para üstü bulunur.','Bir adedin fiyatını tüm adetlere uygulamak; toplamı para üstü sanmak; bir ürünü atlamak.','kolay','hikâyeli',4,'sys-raf','Fiyat etiketli raf')
kartla('K-SYS-02','Kasa fişi tablosu','Fişteki bilinen satırların tutarları toplamdan çıkarılır; kalan tutar adede bölünerek birim fiyat bulunur.','Kalan tutarı birim fiyat sanmak; bir satırı çıkarmayı unutmak; birim fiyatı tutar sanmak.','kolay','tablo',3,'sys-fis','Kasa fişi tablosu')
kartla('K-SYS-03','Kutu–paket düzeni','Üstten görünüşteki paket sayısı kat sayısıyla, sonra koli sayısı ve paketteki adetle çarpılır; toplam eşit paylaştırılır.','Kat sayısını unutmak; paket içindeki adedi katmamak; toplamı paylaştırmamak.','orta','hikâyeli',4,'sys-koli','Kutu–paket düzeni')
kartla('K-SYS-04','Sayı makinesi şeması','Çıkıştan girişe doğru her işlemin tersi sırayla uygulanır.','İşlemin tersini almamak; bir işlemi atlamak; çıkışı girişten ileri doğru işlemek.','orta','şekilli',5,'sys-makine','Sayı makinesi şeması')
kartla('K-SYS-05','Bozuk para dizilimi','Her bozuk para türünün adedi şekilden sayılıp değeriyle çarpılarak toplam bulunur; kurulan denklemden diğer kişinin parası, sonra adet bulunur.','Adet ile TL’yi karıştırmak; 3 katını unutmak; son adımda bozuk para değerine bölmemek.','kolay','hikâyeli',5,'sys-para','Bozuk para dizilimi')
kartla('K-SYS-06','Sinema koltuk düzeni','Satır başına koltuk sayıları ve dolu koltuklar şekilden sayılır; hasılattan bilet fiyatı, fiyattan tam doluluk hasılatı bulunur.','Boş koltukları saymak; satır sayısını koltuk sayısı sanmak; bir satırı atlamak.','orta','hikâyeli',4,'sys-koltuk','Sinema koltuk düzeni')
kartla('K-SYS-07','Skor tablosu ve fark','Bilinen çeyrekler toplanır; fark bilgisiyle diğer takımın toplamından aranan çeyrek bulunur.','Farkın yönünü ters almak; “4 eksik” koşulunu artı almak; toplam yerine çeyrek değerini kullanmak.','orta','tablo',5,'sys-puan','Puan tablosu')
kartla('K-SYS-08','İki terazi ve kütle','İlk dengeden bir bağıntı, ikinci dengeden ikinci bağıntı kurulur; yok edilerek her cismin kütlesi, sonra istenen toplam bulunur.','Ağırlığı yanlış kefeye yazmak; tek terazi kullanmak; sorulan cisim yerine başka cismi bulmak.','orta','hikâyeli',5,'sys-terazi','İki terazi ve kütle')
kartla('K-SYS-09','Fiyat menüsü ve koşullu sipariş','Toplam adet, fiyat toplamı ve oran koşulundan tek bilinmeyenli denklem kurulur; bulunan adetler koşullarla denetlenir.','Oran koşulunu ters yorumlamak; orta boyu unutmak; sorulan toplam yerine tek bir boyu vermek.','zor','hikâyeli',5,'sys-menu','Fiyat menüsü ve koşullu sipariş')
kartla('K-SYS-10','Sayı piramidi','Her kutuyu altındaki iki kutunun toplamı olarak yaz; tepe, tabanın katsayılı toplamıdır; bilinmeyenleri toplamlı çöz.','Tepeyi yalnız tabanın toplamı sanmak; ortadaki kutuların kat sayısını yanlış almak.','zor','yeni nesil',5,'sys-piramit','Sayı piramidi')

# ================= 1 kolay · fiyat etiketli raf =================
zt,pn,bl=85,140,210; odenen=600
tutar=2*zt+pn+bl; dg=odenen-tutar; assert tutar==520 and dg==80
e=[odenen-(zt+pn+bl),odenen-(2*zt+pn),odenen-(2*zt+bl),tutar]; assert e==[165,290,220,520] and len({dg,*e})==5
def kavanoz(x,w,h,ad,fiy):
    return (f'\\draw[thick,rounded corners=2pt,fill=vurgu!10] ({x},0.1) rectangle ({x+w},{h});'
            f'\\draw[thick,fill=vurgu!25] ({x+0.15},{h}) rectangle ({x+w-0.15},{h+0.18});'
            f'\\node at ({x+w/2},{h/2+0.1}) {{\\textbf{{{ad}}}}};'
            f'\\draw[thick,fill=white] ({x+0.2},-0.15) rectangle ({x+w-0.2},-0.75);\\node at ({x+w/2},-0.45) {{\\textbf{{{fiy} TL}}}};')
SK=fig('\\draw[line width=2pt] (-0.2,0) -- (8.6,0);\n'+kavanoz(0.1,2.4,1.5,'Zeytin',zt)+'\n'+kavanoz(3.0,2.4,1.2,'Peynir',pn)+'\n'+kavanoz(5.9,2.4,1.5,'Bal',bl)+'\n\\node at (4.2,-1.2) {\\footnotesize Şarküteri rafı ve fiyat etiketleri};')
q('0001',tipId='sys-raf',tip='Fiyat etiketli raf',z='kolay',alt='Fiyat Etiketli Raf',kaz='Raftaki etiketlerden toplam tutarı bulup para üstünü hesaplar.',kalip='hikâyeli',
 kart='K-SYS-01 (etiketli raf) · 2 zeytin + peynir + bal, 600 TL → para üstü',
 metin='Selin, bir marketin şarküteri rafındaki ürünlerin etiketlerini inceledikten sonra 2 kavanoz zeytin, 1 kutu peynir ve 1 kavanoz bal almıştır. Kasada 600 TL veren Selin’e, ürünlerin hiçbirinde indirim uygulanmadığı için etiketteki fiyatlar üzerinden hesap yapılmıştır.\nBuna göre, Selin’in alacağı para üstü kaç TL’dir?',
 dogru=dg,yan=[(e[0],'Zeytinden yalnız 1 kavanoz hesaplamış: 600 − (85 + 140 + 210).','dikkat'),(e[1],'Balı hesaba katmamış: 600 − (2 × 85 + 140).','dikkat'),(e[2],'Peyniri hesaba katmamış: 600 − (2 × 85 + 210).','dikkat'),(e[3],'Toplam tutarı (520 TL) para üstü sanmış.','dikkat')],
 istenen='Para üstü (TL).',ip=['Her ürün için etikette yazan fiyatı adetle çarp; toplamı verilen paradan çıkar.'],bilgi=[ET],sekil=SK,
 ad=[A('Zeytinin tutarı','2 kavanoz, tanesi 85 TL.','2 × 85 = 170 TL'),A('Peynir ve bal','Birer adet alınmıştır.','140 + 210 = 350 TL'),A('Toplam tutar','Üç ürünün tutarı toplanır.','170 + 350 = 520 TL'),A('Para üstü','Verilen paradan toplam tutar çıkarılır.','600 − 520 = 80 TL')],
 puf='Önce toplam harcamayı bul, sonra verilen paradan çıkar.')

# ================= 2 kolay · kasa fişi =================
d_,s_,k_=3,2,4; dfy,sfy,kfy=36,12,17; top=d_*dfy+s_*sfy+k_*kfy; assert top==200
e=[top-d_*dfy-s_*sfy,(top-d_*dfy)//k_,(top-s_*sfy)//k_,dfy+sfy+0];
assert (top-d_*dfy)%k_==0 and (top-s_*sfy)%k_==0 and e[0]==68 and e[1]==23 and e[2]==44 and e[3]==48
e=[e[0],e[1],e[2],top//k_]; assert e==[68,23,44,50] and len({kfy,*e})==5
SK=tablo_svg(['Ürün','Adet','Birim fiyat (TL)','Tutar (TL)'],[['Defter',d_,dfy,d_*dfy],['Silgi',s_,sfy,s_*sfy],['Yazı kalemi',k_,'?','?'],['Toplam','','',top]])
q('0002',tipId='sys-fis',tip='Kasa fişi tablosu',z='kolay',alt='Kasa Fişi Tablosu',kaz='Fişteki tutarlardan bilinmeyen birim fiyatı bulur.',kalip='tablo',
 kart='K-SYS-02 (kasa fişi) · 3×36 + 2×12 + 4×k = 200',
 metin='Ceren, okul alışverişi yaptığı kırtasiyenin kasa fişini aşağıda göstermiştir. Fişin bir bölümü ıslandığı için yazı kalemlerinin birim fiyatı ve tutarı okunamamaktadır. Fişteki 4 yazı kalemi aynı fiyattan satılmıştır ve toplam tutar doğru yazılmıştır.\nBuna göre, bir yazı kaleminin fiyatı kaç TL’dir?',
 dogru=kfy,yan=[(e[0],'Yazı kalemlerinin toplam tutarını (68 TL) bir kalemin fiyatı sanmış.','dikkat'),(e[1],'Silgilerin tutarını çıkarmayı unutmuş: (200 − 108) ÷ 4.','dikkat'),(e[2],'Defterlerin tutarını çıkarmayı unutmuş: (200 − 24) ÷ 4.','dikkat'),(e[3],'Toplam tutarı doğrudan kalem adedine bölmüş: 200 ÷ 4.','dikkat')],
 istenen='Bir yazı kaleminin fiyatı (TL).',ip=['Defter ve silgi satırlarının tutarlarını bul; toplamdan çıkarınca kalan ne ifade eder?'],bilgi=[ET],sekil=SK,
 ad=[A('Defter tutarı','3 defter, tanesi 36 TL.','3 × 36 = 108 TL'),A('Silgi tutarı','2 silgi, tanesi 12 TL.','2 × 12 = 24 TL'),A('Yazı kalemlerinin tutarı','Toplamdan bilinen tutarlar çıkarılır.','200 − 108 − 24 = 68 TL'),A('Birim fiyat','4 kalem eşit fiyatlıdır.','68 ÷ 4 = 17 TL')],
 puf='Toplamdan bilinen satırları çıkar, kalanı adede böl.')

# ================= 3 orta · kutu–paket düzeni =================
sat,sut,kat,ic=3,4,3,12; koli,sinif=5,18
kalem=koli*sat*sut*kat*ic; assert kalem==2160 and kalem%sinif==0; dg=kalem//sinif; assert dg==120
e=[koli*sat*sut*ic//sinif,koli*sat*sut*kat//sinif,koli*(sat*sut+kat)*ic//sinif,kalem]; assert e==[40,10,50,2160] and len({dg,*e})==5
o=[]
for r in range(sat):
    for c in range(sut):
        o.append(f'\\draw[thick,rounded corners=1.5pt,fill=vurgu!12] ({c*0.85:.2f},{-r*0.85:.2f}) rectangle ({c*0.85+0.75:.2f},{-r*0.85-0.75:.2f});\\node at ({c*0.85+0.375:.2f},{-r*0.85-0.375:.2f}) {{12}};')
o.append(f'\\draw[thick] (-0.1,0.1) rectangle ({sut*0.85-0.0:.2f},{-sat*0.85+0.0});')
o.append(f'\\node at ({sut*0.85/2-0.05:.2f},-{sat*0.85+0.45:.2f}) {{\\footnotesize Üstten görünüş}};')
bx=5.4
for k in range(kat):
    o.append(f'\\draw[thick,fill=vurgu!12] ({bx},{-k*0.8:.2f}) rectangle ({bx+1.9},{-k*0.8-0.8:.2f});')
o.append(f'\\draw[thick] ({bx+2.1},0) -- ({bx+2.25},0) -- ({bx+2.25},{-kat*0.8}) -- ({bx+2.1},{-kat*0.8});\\node[right] at ({bx+2.25},{-kat*0.4}) {{{kat} kat}};')
o.append(f'\\node at ({bx+0.95},-{sat*0.85+0.45:.2f}) {{\\footnotesize Yandan görünüş}};')
SK=fig('\n'.join(o)+'\n\\node at (3.5,0.55) {\\footnotesize Her kutudaki sayı: paketteki kalem adedi};')
q('0003',tipId='sys-koli',tip='Kutu–paket düzeni',z='orta',alt='Kutu–Paket Düzeni',kaz='Koli düzeninden toplam adedi bulup eşit paylaştırır.',kalip='hikâyeli',
 kart='K-SYS-03 (koli düzeni) · 5 koli × (3×4 paket × 3 kat) × 12 kalem ÷ 18 sınıf',
 metin='Bir kalem üreticisinin okula gönderdiği 5 kolinin hepsi, aynı düzende paketlenmiştir. Şekilde bir kolinin üstten ve yandan görünüşleri verilmiştir; paketlerin hepsi birbirinin aynısıdır. Okul müdürlüğü gelen kalemlerin tamamını 18 sınıfa eşit sayıda dağıtacaktır.\nBuna göre, her sınıfa kaç kalem düşer?',
 dogru=dg,yan=[(e[0],'Kat sayısını (3) hesaba katmamış: 5 × 12 × 12 ÷ 18.','dikkat'),(e[1],'Paketteki kalem sayısını (12) katmamış: 5 × 36 ÷ 18.','dikkat'),(e[2],'Kat sayısını çarpmak yerine paket sayısına eklemiş: 5 × (12 + 3) × 12 ÷ 18.','dikkat'),(e[3],'Toplam kalemi sınıflara bölmemiş.','dikkat')],
 istenen='Her sınıfa düşen kalem sayısı.',ip=['Bir kolideki paket sayısını bulmak için üstten görünüşteki sıra ve sütunu, yandan görünüşteki katı birlikte düşün.'],bilgi=[SAY],sekil=SK,
 ad=[A('Bir kat','Üstten görünüşte 3 sıra, 4 sütun.','3 × 4 = 12 paket'),A('Bir koli','Yandan görünüşte 3 kat vardır.','12 × 3 = 36 paket'),A('Toplam kalem','5 koli, her pakette 12 kalem.','5 × 36 × 12 = 2160 kalem'),A('Sınıf başına','18 sınıfa eşit dağıtılır.','2160 ÷ 18 = 120')],
 puf='Toplam kalem = koli × kat × sıra × sütun × paketteki adet.')

# ================= 4 orta · sayı makinesi =================
xg=8; ops=[('\\times 3',lambda v:v*3),('+6',lambda v:v+6),('\\div 2',lambda v:v/2),('-5',lambda v:v-5)]
v=xg
for _,f in ops: v=f(v)
assert v==10 and xg==(((10+5)*2-6)//3) and ((10+5)*2-6)%3==0
def ileri(x):
    for _,f in ops: x=f(x)
    return x
e1=((10+5)*2)//3; e2=((10+5)-6)//3; e3=((10+5)*2+6)//3; e4=ileri(10)
assert ((10+5)*2)%3==0 and ((10+5)-6)%3==0 and ((10+5)*2+6)%3==0 and e4==13 and (e1,e2,e3)==(10,3,12)
e1=(10+5)*2-6; assert e1==24
e=[e1,e2,e3,e4]; assert e==[24,3,12,13] and len({xg,*e})==5
o=['\\node[draw,circle,thick,minimum size=0.95cm] (g) at (0,0) {\\large $x$};']
xs=[1.65,3.3,4.95,6.6]
for i,(t,_) in enumerate(ops): o.append(f'\\node[draw,thick,rounded corners=3pt,fill=vurgu!12,minimum width=1.05cm,minimum height=0.85cm] (m{i}) at ({xs[i]},0) {{${t}$}};')
o.append('\\node[draw,circle,thick,minimum size=0.95cm] (c) at (8.25,0) {10};')
prev='g'
for i in range(4): o.append(f'\\draw[-{{Stealth[length=2mm]}},thick] ({prev}) -- (m{i}); '); prev=f'm{i}'
o.append('\\draw[-{Stealth[length=2mm]},thick] (m3) -- (c);')
o.append('\\node at (0,-0.95) {\\footnotesize Giriş}; \\node at (8.25,-0.95) {\\footnotesize Çıkış};')
SK=fig('\n'.join(o))
q('0004',tipId='sys-makine',tip='Sayı makinesi şeması',z='orta',alt='Sayı Makinesi Şeması',kaz='İşlem zincirinde çıkıştan girişe ters işlemlerle ilerler.',kalip='şekilli',
 kart='K-SYS-04 (makine) · ×3, +6, ÷2, −5 → 10 ; giriş 8',
 metin='Aşağıdaki sayı makinesinde giriş kutusuna yazılan sayı, okların gösterdiği sırayla dört işlem kutusundan geçer ve çıkış kutusunda sonuç görünür.\nÇıkışta şekilde gösterilen sayı elde edildiğine göre, giriş kutusundaki x sayısı kaçtır?',
 dogru=xg,yan=[(e[0],'İlk kutudaki × 3 işleminin tersini (÷ 3) uygulamayı unutmuş: (10 + 5) × 2 − 6.','dikkat'),(e[1],'÷ 2 işleminin tersini (× 2) uygulamamış: (10 + 5 − 6) ÷ 3.','dikkat'),(e[2],'+ 6 işlemini geri alırken tekrar toplamış: ((10 + 5) × 2 + 6) ÷ 3.','dikkat'),(e[3],'Çıkıştan geri gitmek yerine 10’u makineye girmiş gibi işlemiş.','islem')],
 istenen='x sayısı.',ip=['Çıkıştan başla; her işlem kutusunu sondan başa doğru tersiyle değiştir.'],bilgi=[ISL],sekil=SK,
 ad=[A('Son kutu','− 5’in tersi + 5.','10 + 5 = 15'),A('Üçüncü kutu','÷ 2’nin tersi × 2.','15 × 2 = 30'),A('İkinci kutu','+ 6’nın tersi − 6.','30 − 6 = 24'),A('Birinci kutu','× 3’ün tersi ÷ 3.','24 ÷ 3 = 8'),A('Kontrol','8 girince 24, 30, 15, 10 elde edilir.','8 → 24 → 30 → 15 → 10')],
 puf='Sondan başa, her adımda işlemin tersini al; sonucu ileri doğru işleyerek denetle.')

# ================= 5 kolay · bozuk para dizilimi =================
ad_={1:7,5:4,10:3}; ali=sum(k*v for k,v in ad_.items()); assert ali==57
berk=(ali-12)//3; assert (ali-12)%3==0 and berk==15 and berk%5==0; dg=berk//5; assert dg==3
e=[berk,ali//3,(ali+12)//3,(ali-12)//5]; assert ali%3==0 and (ali+12)%3==0 and (ali-12)%5==0 and e==[15,19,23,9] and len({dg,*e})==5
o=[]
for i,(dn,adt) in enumerate(ad_.items()):
    r={1:0.3,5:0.36,10:0.42}[dn]; y=-i*1.0
    for j in range(adt): o.append(f'\\draw[thick,fill=vurgu!15] ({j*0.92+0.45:.2f},{y:.2f}) circle ({r});\\node at ({j*0.92+0.45:.2f},{y:.2f}) {{\\footnotesize\\textbf{{{dn}}}}};')
o.append('\\node at (3.0,-2.85) {\\footnotesize Ali’nin bozuk paraları (üzerindeki sayı: TL değeri)};')
SK=fig('\n'.join(o))
q('0005',tipId='sys-para',tip='Bozuk para dizilimi',z='kolay',alt='Bozuk Para Dizilimi',kaz='Bozuk para sayılarından toplam parayı bulup kurulan ilişkiden adedi hesaplar.',kalip='hikâyeli',
 kart='K-SYS-05 (bozuk para) · 57 TL = 3 × Berk + 12 → Berk 15 TL = 3 adet 5 TL',
 metin='Ali, cüzdanındaki bütün bozuk paraları masaya şekildeki gibi dizmiştir. Arkadaşı Berk’in bütün parası ise yalnızca 5 TL’lik bozuk paralardan oluşmaktadır. Ali’nin toplam parası (TL), Berk’in toplam parasının (TL) 3 katından 12 TL fazladır.\nBuna göre, Berk’in cüzdanında kaç adet 5 TL’lik bozuk para vardır?',
 dogru=dg,yan=[(e[0],'Berk’in parasını (15 TL) bozuk para sayısı sanmış; 5’e bölmemiş.','dikkat'),(e[1],'12 TL farkı hesaba katmamış: 57 ÷ 3 = 19.','dikkat'),(e[2],'12 TL farkı çıkarmak yerine eklemiş: (57 + 12) ÷ 3 = 23.','dikkat'),(e[3],'Berk’in parasını 3’e bölmeyi unutmuş: (57 − 12) ÷ 5.','dikkat')],
 istenen='Berk’in 5 TL’lik bozuk para adedi.',ip=['Önce Ali’nin toplam parasını bozuk paraların sayısını ve değerini kullanarak bul.'],bilgi=[B('Bozuk para toplamı','toplam para = (her türün adedi × değeri) toplamıdır. Örnek: 2 tane 10 TL ile 3 tane 1 TL, 20 + 3 = 23 TL eder')],sekil=SK,
 ad=[A('Ali’nin parası','7 tane 1 TL, 4 tane 5 TL, 3 tane 10 TL.','7 + 20 + 30 = 57 TL'),A('Denklem','Ali = 3 × Berk + 12.','57 = 3b + 12'),A('Berk’in parası','12 çıkarılıp 3’e bölünür.','(57 − 12) ÷ 3 = 15 TL'),A('Bozuk para sayısı','Her bozuk para 5 TL’dir.','15 ÷ 5 = 3'),A('Kontrol','3 × 15 + 12 = 57 TL.','45 + 12 = 57')],
 puf='Önce Ali’nin parasını sayarak bul, sonra denklemi geriye doğru çöz.')

# ================= 6 orta · sinema koltuk düzeni =================
satirlar=[7,9,11,13,15]
dolu=[{0,1,2,4,5,6},set(range(9)),{0,1,2,3,4,6,7,8,9,10}-{0}|{0},{2,3,4,5,7,8,9,10},{6,7,8}]
dolu[2]={0,1,2,3,4,6,7,8,9,10}; assert [len(x) for x in dolu]==[6,9,10,8,3] and all(max(x)<n for x,n in zip(dolu,satirlar))
toplam=sum(satirlar); sd=sum(len(x) for x in dolu); assert toplam==55 and sd==36
has=3060; assert has%sd==0; fiyat=has//sd; assert fiyat==85; dg=toplam*fiyat; assert dg==4675
e=[(toplam-satirlar[-1])*fiyat,(toplam-1)*fiyat,(toplam+1)*fiyat,len(satirlar)*max(satirlar)*fiyat]; assert e==[3400,4590,4760,6375] and len({dg,*e})==5
o=['\\draw[thick] (-4.2,0.55) -- (4.2,0.55);\\node at (0,0.9) {\\footnotesize PERDE};']
for i,n in enumerate(satirlar):
    y=-i*0.62; x0=-(n*0.56)/2+0.28
    o.append(f'\\node at (-4.55,{y:.2f}) {{\\footnotesize {i+1}}};')
    for j in range(n):
        f='vurgu!55' if j in dolu[i] else 'white'
        o.append(f'\\draw[thick,rounded corners=2pt,fill={f}] ({x0+j*0.56-0.22:.2f},{y-0.22:.2f}) rectangle ({x0+j*0.56+0.22:.2f},{y+0.22:.2f});')
o.append('\\draw[thick,fill=vurgu!55,rounded corners=2pt] (-2.4,-3.65) rectangle (-1.96,-3.25);\\node[right] at (-1.9,-3.45) {\\footnotesize Satılmış};')
o.append('\\draw[thick,fill=white,rounded corners=2pt] (0.4,-3.65) rectangle (0.84,-3.25);\\node[right] at (0.9,-3.45) {\\footnotesize Boş};')
SK=fig('\n'.join(o))
q('0006',tipId='sys-koltuk',tip='Sinema koltuk düzeni',z='orta',alt='Sinema Koltuk Düzeni',kaz='Koltuk düzeninden satılan ve toplam koltuk sayısını bulup hasılatı hesaplar.',kalip='hikâyeli',
 kart='K-SYS-06 (koltuk) · 36 koltuk 3060 TL → 55 koltuk 4675 TL',
 metin='Bir sinema salonunun koltuk düzeni şekilde verilmiştir; satırların numaraları soldadır. Bu seans için satılan bütün biletlerin fiyatı aynıdır ve satılan biletlerden toplam 3 060 TL hasılat elde edilmiştir.\nSalonun bütün koltukları aynı bilet fiyatıyla satılmış olsaydı toplam hasılat kaç TL olurdu?',
 dogru=dg,yan=[(e[0],'Son satırı (15 koltuk) saymayı unutmuş: 40 × 85.','dikkat'),(e[1],'Toplam koltuğu 54 saymış (bir koltuğu eksik): 54 × 85.','dikkat'),(e[2],'Toplam koltuğu 56 saymış (bir koltuğu fazla): 56 × 85.','dikkat'),(e[3],'Her satırı en uzun satır kadar (15) sanmış: 5 × 15 × 85.','dikkat')],
 istenen='Tam doluluk hasılatı (TL).',ip=['Önce satılmış (yeşil) koltukları sayıp bilet fiyatını bul; sonra tüm koltukların sayısına geç.'],bilgi=[B('Toplam hasılat','hasılat = satılan bilet sayısı × bilet fiyatı; fiyat, hasılatın bilet sayısına bölünmesiyle bulunur. Örnek: 4 bilet × 25 TL = 100 TL')],sekil=SK,
 ad=[A('Satılan koltuk','Satırlarda 6, 9, 10, 8 ve 3 yeşil (satılmış) koltuk.','6 + 9 + 10 + 8 + 3 = 36'),A('Bilet fiyatı','Hasılat satılan koltuk sayısına bölünür.','3060 ÷ 36 = 85 TL'),A('Tüm koltuklar','Satırlarda 7, 9, 11, 13 ve 15 koltuk.','7 + 9 + 11 + 13 + 15 = 55'),A('Tam doluluk hasılatı','Koltuk sayısı × bilet fiyatı.','55 × 85 = 4675 TL')],
 puf='Önce yeşil (satılmış) koltukları say, bilet fiyatını bul; sonra bütün koltukları say.')

# ================= 7 orta · puan (skor) tablosu =================
A_=[21,24,None,19]; Bq=[22,18,25,None]; b4=Bq[2]-4; Bt=sum(Bq[:3])+b4; At=Bt+5; a3=At-(21+24+19)
assert b4==21 and Bt==86 and At==91 and a3==27
e=[(sum(Bq[:3])+5)-(21+24+19),(Bt-5)-(21+24+19),(sum(Bq[:3])+25+5)-(21+24+19),(sum(Bq[:3])+29+5)-(21+24+19)]; assert e==[6,17,31,35] and len({a3,*e})==5
SK=tablo_svg(['Takım','1. çeyrek','2. çeyrek','3. çeyrek','4. çeyrek'],[['A',21,24,'?',19],['B',22,18,25,'?']])
q('0007',tipId='sys-puan',tip='Puan tablosu',z='orta',alt='Puan Tablosu',kaz='Skor tablosu ve fark bilgisiyle bilinmeyen çeyrek sayısını bulur.',kalip='tablo',
 kart='K-SYS-07 (skor tablosu) · B toplamı 86, A 5 fazla → 3. çeyrek 27',
 metin='İki basketbol takımının bir maçtaki çeyrek skorları aşağıdaki tabloda verilmiştir; bazı değerler okunamamaktadır. B takımının 4. çeyrekte attığı sayı, 3. çeyrekte attığı sayıdan 4 eksiktir. Maçı 5 sayı farkla A takımı kazanmıştır.\nBuna göre, A takımının 3. çeyrekte attığı sayı kaçtır?',
 dogru=a3,yan=[(e[0],'B’nin 4. çeyrek sayısını hiç hesaba katmamış: (22 + 18 + 25 + 5) − 64.','dikkat'),(e[1],'Farkın yönünü ters almış (B kazanmış gibi): (86 − 5) − 64.','dikkat'),(e[2],'“4 eksik” koşulunu kullanmayıp B’nin 4. çeyreğini 25 almış: (65 + 25 + 5) − 64.','dikkat'),(e[3],'“4 eksik” koşulunu 4 fazla olarak okumuş (29): (65 + 29 + 5) − 64.','dikkat')],
 istenen='A takımının 3. çeyrekte attığı sayı.',ip=['Önce B takımının bütün çeyreklerdeki toplam sayısını bulmaya çalış.'],bilgi=[TB],sekil=SK,
 ad=[A('B’nin 4. çeyreği','3. çeyrekten 4 eksik.','25 − 4 = 21'),A('B’nin toplamı','Dört çeyreğin toplamı.','22 + 18 + 25 + 21 = 86'),A('A’nın toplamı','A, 5 sayı farkla kazanmıştır.','86 + 5 = 91'),A('A’nın bilinen çeyrekleri','Tablodaki üç çeyrek.','21 + 24 + 19 = 64'),A('3. çeyrek','Toplamdan bilinenler çıkarılır.','91 − 64 = 27')],
 puf='Önce kazanan ve kaybeden takımın toplamlarını yaz, sonra eksik çeyreği toplamdan çıkarma ile bul.')

# ================= 8 orta · iki terazi =================
e_,p_,w1,w2=120,150,60,270
assert 3*e_==2*p_+w1 and e_+p_==w2
def coz(a,b,c,d):  # a*E = b*P + c ; E + P = d  → E=(b*d+c)/(a+b)
    E=Fr(b*d+c,a+b); return E,d-E
E0,P0=coz(3,2,w1,w2); assert (E0,P0)==(120,150); dg=2*E0+P0; assert dg==390
E1,P1=coz(3,2,0,w2); E2,P2=coz(3,2,-w1,w2)
assert (E1,P1)==(Fr(540,5),Fr(810,5)); e=[2*E1+P1,2*E2+P2,E0+2*P0,w2+w1]
assert e==[378,366,420,330] and len({dg,*e})==5
def terazi(oy,sol,sag):
    """sol/sag: [(tür,değer)] tür: 'e' elma(daire), 'p' portakal(kare), 'w' ağırlık(kutu etiketli)."""
    yb,yp=oy+1.9,oy+0.75
    o=[f'\\draw[thick] (-0.9,{oy}) -- (0.9,{oy});\\draw[thick] (0,{oy}) -- (0,{yb});\\draw[thick] (-3.5,{yb}) -- (3.5,{yb});\\fill (0,{yb}) circle (0.07);']
    for sgn,lst in ((-1,sol),(1,sag)):
        cx=sgn*2.1
        o.append(f'\\draw[thick] ({cx-1.3},{yb}) -- ({cx-1.3},{yp});\\draw[thick] ({cx+1.3},{yb}) -- ({cx+1.3},{yp});\\draw[line width=1.4pt] ({cx-1.4},{yp}) -- ({cx+1.4},{yp});')
        ws=[0.6 if t!='w' else 1.0 for t,_ in lst]; tot=sum(ws)+0.1*(len(lst)-1); x=cx-tot/2
        for (t,v),w in zip(lst,ws):
            mx=x+w/2
            if t=='e': o.append(f'\\draw[thick,fill=vurgu!15] ({mx:.2f},{yp+0.3:.2f}) circle (0.3);')
            elif t=='p': o.append(f'\\draw[thick,fill=vurgu!15,rounded corners=1pt] ({mx-0.28:.2f},{yp:.2f}) rectangle ({mx+0.28:.2f},{yp+0.56:.2f});')
            else: o.append(f'\\draw[thick,fill=white,rounded corners=1pt] ({mx-0.5:.2f},{yp:.2f}) rectangle ({mx+0.5:.2f},{yp+0.55:.2f});\\node at ({mx:.2f},{yp+0.28:.2f}) {{\\footnotesize\\textbf{{{v} g}}}};')
            x+=w+0.1
    return '\n'.join(o)
SK=fig(terazi(3.1,[('e',0)]*3,[('p',0)]*2+[('w',w1)])+'\n'+terazi(0,[('e',0),('p',0)],[('w',w2)])+
 '\n\\draw[thick,fill=vurgu!15] (-1.9,-0.8) circle (0.22);\\node[right] at (-1.6,-0.8) {\\footnotesize : elma};\\draw[thick,fill=vurgu!15,rounded corners=1pt] (0.3,-1.02) rectangle (0.74,-0.58);\\node[right] at (0.85,-0.8) {\\footnotesize : portakal};')
q('0008',tipId='sys-terazi',tip='İki terazi ve kütle',z='orta',alt='İki Terazi ve Kütle',kaz='İki denge durumundan iki bilinmeyenli ilişki kurup istenen kütleyi bulur.',kalip='hikâyeli',
 kart='K-SYS-08 (iki terazi) · 3e = 2p + 60, e + p = 270 → 2e + p',
 metin='Bir manav, elma ve portakal kütlelerini kontrol etmek için iki teraziyi şekildeki gibi dengelemiştir. Bütün elmalar birbirinin aynı, bütün portakallar da birbirinin aynıdır; kefelerdeki kutular ise belirtilen kütlede ağırlıklardır.\nBuna göre, 2 elma ile 1 portakalın toplam kütlesi kaç gramdır?',
 dogru=dg,yan=[(e[0],'Birinci terazideki 60 g’ı hesaba katmamış (3e = 2p): e = 108, p = 162.','dikkat'),(e[1],'60 g’ı yanlış kefeye yazmış (3e = 2p − 60): e = 96, p = 174.','dikkat'),(e[2],'Elma ve portakalın kütlelerini bulmuş, fakat 1 elma + 2 portakalı hesaplamış.','dikkat'),(e[3],'İkinci dengedeki 270 g’ın üstüne yalnız 60 g ekleyerek bulmuş: 270 + 60.','islem')],
 istenen='2 elma ile 1 portakalın kütlesi (g).',ip=['İkinci terazi bir elma ile bir portakalın toplamını verir; bunu birinci terazide kullanmayı dene.'],bilgi=[TE],sekil=SK,
 ad=[A('Birinci denge','3 elma = 2 portakal + 60 g.','3e = 2p + 60'),A('İkinci denge','1 elma + 1 portakal = 270 g.','e + p = 270 → p = 270 − e'),A('Yerine yaz','p’yi birinci denklemde kullan.','3e = 540 − 2e + 60 → 5e = 600'),A('Elma ve portakal','e ve p bulunur.','e = 120 g, p = 150 g'),A('İstenen','2 elma + 1 portakal.','240 + 150 = 390 g')],
 puf='İkinci terazi toplamı verir; “e + p” ile birinci dengeden e ya da p’yi çıkar.')

# ================= 9 zor · fiyat menüsü =================
fy={'s':120,'m':160,'l':200}; N=9; HES=1520
sol=[(s,m,l) for s in range(0,N+1) for m in range(0,N+1) for l in range(0,N+1) if s+m+l==N and l==2*s and fy['s']*s+fy['m']*m+fy['l']*l==HES and s>0]
assert sol==[(2,3,4)]; s_,m_,l_=sol[0]; dg=s_+l_; assert dg==6
e=[s_,m_,l_,N-l_]; assert e==[2,3,4,5] and len({dg,*e})==5
o=['\\draw[thick,rounded corners=4pt] (0,0) rectangle (6.4,3.3);\\node at (3.2,2.85) {\\textbf{PİZZA MENÜSÜ}};\\draw[thin] (0.3,2.5) -- (6.1,2.5);']
for i,(ad,kod) in enumerate([('Küçük boy','s'),('Orta boy','m'),('Büyük boy','l')]):
    y=1.95-i*0.75
    o.append(f'\\node[anchor=west] at (0.4,{y}) {{{ad}}};\\node[anchor=east] at (6.0,{y}) {{\\textbf{{{fy[kod]} TL}}}};\\draw[dotted] (2.3,{y-0.1}) -- (4.4,{y-0.1});')
SK=fig('\n'.join(o))
q('0009',tipId='sys-menu',tip='Fiyat menüsü ve koşullu sipariş',z='zor',alt='Fiyat Menüsü',kaz='Toplam adet, hesap tutarı ve oran koşulundan sipariş sayılarını bulur.',kalip='hikâyeli',
 kart='K-SYS-09 (menü) · 9 pizza, 1520 TL, büyük = 2 × küçük',
 metin='Bir grup öğrenci, bir pizzacıda menüde fiyatları verilen küçük, orta ve büyük boy pizzalardan toplam 9 tane sipariş etmiş ve hesap 1 520 TL gelmiştir. Siparişte her boydan en az bir pizza vardır ve büyük boy pizza sayısı, küçük boy pizza sayısının 2 katıdır.\nBuna göre, bu siparişteki küçük ve büyük boy pizzaların toplam sayısı kaçtır?',
 dogru=dg,yan=[(e[0],'Yalnız küçük boy pizza sayısını (2) vermiş.','dikkat'),(e[1],'Orta boy pizza sayısını (3) vermiş.','dikkat'),(e[2],'Yalnız büyük boy pizza sayısını (4) vermiş.','dikkat'),(e[3],'Orta boy yerine büyük boyu çıkarmış: 9 − 4 = 5.','dikkat')],
 istenen='Küçük ve büyük boy pizzaların toplam sayısı.',ip=['Küçük boy sayısına a de; büyük ve orta boy sayılarını a cinsinden yazıp hesap tutarıyla eşitle.'],bilgi=[MEN],sekil=SK,
 ad=[A('Bilinmeyenler','Küçük a, büyük 2a, orta 9 − 3a tanedir.','a + 2a + (9 − 3a) = 9'),A('Hesap denklemi','Fiyatlar menüden okunur.','120a + 160(9 − 3a) + 200 · 2a = 1520'),A('Sadeleştir','Terimler toplanır.','40a + 1440 = 1520'),A('Küçük boy','a bulunur.','a = 2'),A('Sayılar','Küçük 2, büyük 4, orta 3; toplam kontrolü doğru.','2 + 4 = 6')],
 puf='Bütün boyları tek bir bilinmeyenle yaz; toplam adet koşulu orta boyu verir.')

# ================= 10 zor · sayı piramidi =================
b1,b4=9,11; tepe=80
def tepe_f(x,y): return b1+3*x+3*y+b4
ss=[(x,y) for x in range(1,40) for y in range(1,40) if tepe_f(x,y)==tepe]; assert all(x+y==20 for x,y in ss)
dg=20; e=[(tepe-b1-b4)//c for c in (1,2,4,6)]; assert e==[60,30,15,10] and all((tepe-b1-b4)%c==0 for c in (1,2,4,6)) and len({dg,*e})==5
bw,bh=1.3,0.8
def kutu(i,j,t=''):  # i: satır (0 tepe), j: sütun
    n=i+1; x=(j-(n-1)/2)*bw; y=-i*bh
    return f'\\draw[thick,fill=vurgu!10] ({x-bw/2:.2f},{y-bh/2:.2f}) rectangle ({x+bw/2:.2f},{y+bh/2:.2f});'+(f'\\node at ({x:.2f},{y:.2f}) {{\\textbf{{{t}}}}};' if t!='' else '')
tx={(0,0):tepe,(3,0):b1,(3,1):'$x$',(3,2):'$y$',(3,3):b4}
o=[kutu(i,j,tx.get((i,j),'')) for i in range(4) for j in range(i+1)]
SK=fig('\n'.join(o))
q('0010',tipId='sys-piramit',tip='Sayı piramidi',z='zor',alt='Sayı Piramidi',kaz='Piramit kurallarıyla tepeyi tabandan ifade edip bilinmeyen toplamı bulur.',kalip='yeni nesil',
 kart='K-SYS-10 (piramit) · tepe = a + 3x + 3y + d',
 metin='Aşağıdaki sayı piramidinde alt sıra dışındaki her kutuya, hemen altındaki iki kutuda yazan sayıların toplamı yazılmaktadır. Piramidin alt sırasındaki iki kutuda sayılar yerine x ve y harfleri bulunmaktadır.\nBuna göre, x + y toplamı kaçtır?',
 dogru=dg,yan=[(e[0],'Tepeyi yalnız alt sıradaki dört sayının toplamı sanmış: 80 − 20 = 60.','dikkat'),(e[1],'x ve y’nin tepeye 2’şer kez katıldığını sanmış: 60 ÷ 2 = 30.','dikkat'),(e[2],'Katsayıyı 4 almış: 60 ÷ 4 = 15.','dikkat'),(e[3],'Katsayıyı 6 almış: 60 ÷ 6 = 10.','dikkat')],
 istenen='x + y toplamı.',ip=['Her kutuyu alt sıradaki sayılar cinsinden yaz; tepede 9 ve 11’in kaçar kez, x ve y’nin kaçar kez bulunduğunu say.'],bilgi=[ARD],sekil=SK,
 ad=[A('İkinci sıra','Üç kutu: altlarındaki ikililerin toplamı.','9 + x,  x + y,  y + 11'),A('Üçüncü sıra','İki kutu.','(9 + x) + (x + y) = 9 + 2x + y;  (x + y) + (y + 11) = x + 2y + 11'),A('Tepe','İki kutunun toplamı.','20 + 3x + 3y'),A('Denklem','Tepe 80’dir.','20 + 3(x + y) = 80'),A('Çöz','3’e bölünür.','x + y = 20')],
 puf='Ortadaki iki sayı tepeye 3’er kez katılır; tepe = köşeler + 3 × (ortadakilerin toplamı).')

bitir(P,'sayisek','prob|Sayı Problemleri')
