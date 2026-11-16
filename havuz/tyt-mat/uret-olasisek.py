"""Olasılık · ŞEKİLLİ paket (7 soru): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer Fraction/tarama ile hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,itertools,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians,sqrt
H.KONU='Olasılık'
P=Parti('olasisek','Olasılık','matd|Olasılık')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu olasılık soruları; yalnız mantık) · MEB 10. sınıf'
def fs(x):
    x=Fr(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def mkp(no,dogru,yan,**k):
    sira=[fs(v) for v in sorted({Fr(dogru),*[Fr(y[0]) for y in yan]})]; assert len(sira)==5
    mk(P,no,dogru=fs(dogru),yan=[(fs(y[0]),y[1],y[2]) for y in yan],sira=sira,**k)
def q(no,ad,**k): mkp(no,ad=ad,adim=len(ad),**k)
def tf(x):
    x=Fr(x); return str(x.numerator) if x.denominator==1 else r'\dfrac{%d}{%d}'%(x.numerator,x.denominator)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

ASL=B('Asal sayı','1’den büyük olup yalnız 1’e ve kendisine bölünebilen doğal sayıdır. Örnek: 17 asaldır, 21 asal değildir (3 ile bölünür)')
TEM=B('Olasılık','eşit olasılıklı sonuçlarda olay olasılığı = istenen sonuç sayısı ÷ tüm sonuç sayısıdır. Örnek: 8 eş dilimli çarkta 3 dilim kırmızı ise kırmızıda durma olasılığı 3/8')
BAG=B('Bağımsız olaylar','biri diğerinin sonucunu etkilemeyen olayların birlikte olma olasılığı, olasılıkların çarpımıdır. Örnek: 1/2 ve 1/3 olasılıklı iki bağımsız olay birlikte 1/6 olasılıkla gerçekleşir')
GEO=B('Alana dayalı olasılık','alanı eşit bölgelerden birine isabet olasılığı bölge sayısının tersidir; atışlar birbirini etkilemez. Örnek: 5 eş alanlı bölgenin her birine isabet olasılığı 1/5')
SAY=B('Örnek uzay tablosu','iki aşamalı denemede sonuçlar satır ve sütunların kesişimlerindeki hücrelerdir; olasılık, uygun hücre sayısının toplam hücre sayısına oranıdır. Örnek: 6 × 6 tabloda 9 uygun hücre varsa olasılık 9/36 = 1/4')
AGA=B('Ağaç diyagramı','bir dal boyunca olasılıklar çarpılır, aynı olayı veren dalların olasılıkları toplanır. Örnek: 1/2 · 1/5 ve 1/2 · 3/5 dalları aynı olayı veriyorsa olasılık 1/10 + 3/10 = 2/5')
KOM=B('Geri konmadan çekiliş','iki nesne birlikte çekildiğinde tüm durum sayısı C(n, 2) = n(n − 1)/2’dir; istenen durumlar da kombinasyonla sayılır. Örnek: 5 nesneden 2 seçmek 10 yoldur')
TAB=B('Tablodan olasılık','tablodaki sayılar toplanarak durum sayısı bulunur; “ya da” içeren olayda ortak elemanlar bir kez sayılır. Örnek: 20 kişilik grupta 12 kişi A, 9 kişi B ise ve 4 kişi ikisi de ise A ya da B’de 17 kişi vardır')

# ---------- kartlar ----------
kartla('K-OLS-01','Eşit dilimli çark','Dilimler üzerindeki sayılardan koşula uyanlar tek tek sayılır; dilim sayısına bölünür.','Farklı sayıları sayıp aynı sayılı dilimleri tek saymak; “ya da”da çarpmak.','kolay','şekilli',3,'ols-cark','Eşit dilimli çark')
kartla('K-OLS-02','Tablodan olasılık (kız-erkek, branş)','Tablodaki sayılar toplanır; koşulu sağlayanlar ortak kısım bir kez sayılarak bulunur, toplama oranlanır.','Ortak kısmı iki kez saymak; yanlış satırı seçmek.','kolay','tablo',3,'ols-tablo','Tablodan olasılık')
kartla('K-OLS-03','Hedef tahtası ve iki atış','Eşit alanlı bölgelerin her birine isabet olasılığı eşittir; iki atışın puan toplamı koşuluna uyan sıralı çiftler sayılır.','Aynı puanlı bölgeleri tek saymak; sırayı hesaba katmamak.','orta','hikâyeli',4,'ols-hedef','Hedef tahtası ve iki atış')
kartla('K-OLS-04','İki torbadan birer top','Her torbanın top sayılarından renk olasılıkları bulunur; aynı renk olasılığı renk renk çarpılıp toplanır.','Torbaları birleştirip tek torba gibi çekmek; bir rengi atlamak.','orta','hikâyeli',4,'ols-torba','İki torbadan birer top çekme')
kartla('K-OLS-05','İki özel zarın toplam tablosu','Tablodaki 36 hücrenin kaçının koşulu sağladığı sayılır; tekrarlanan toplamlar ayrı hücrelerdir.','Farklı toplamları sayıp hücreleri saymamak; 2’yi asal saymamak.','orta','tablo',3,'ols-zar','Zar tablosu')
kartla('K-OLS-06','Ağaç diyagramı ve toplam olasılık','Her dal boyunca olasılıklar çarpılır; istenen sonucu veren dalların çarpımları toplanır.','Dalları ağırlıksız ortalamak; bir dalı unutmak.','orta','hikâyeli',5,'ols-agac','Ağaç diyagramı')
kartla('K-OLS-07','Kart destesi ve geri konmadan çekiliş','Kartların simge ve sayı özelliklerine göre gruplar ayrılır; her gruptan uygun ikililer kombinasyonla sayılıp tüm ikililere oranlanır.','Geri koyarak çekmiş gibi hesaplamak; koşullardan birini unutmak.','zor','şekilli',5,'ols-deste','Kart destesi şeması')

# ================= 01 kolay · eşit dilimli çark =================
D=[4,7,2,9,5,2,8,3,6,5]; asal={2,3,5,7}
sec=[i for i,x in enumerate(D) if x in asal or x%4==0]
v=Fr(len(sec),len(D)); assert v==Fr(4,5)
e=[Fr(sum(1 for x in D if x in asal),len(D)),Fr(len({x for x in D if x in asal or x%4==0}),len(set(D))),Fr(sum(1 for x in D if x in asal),len(D))*Fr(sum(1 for x in D if x%4==0),len(D)),Fr(sum(1 for x in D if x%4==0),len(D))]
assert e==[Fr(3,5),Fr(3,4),Fr(3,25),Fr(1,5)] and len({v,*e})==5
R=2.2; o=[]
for i,x in enumerate(D):
    a1=90-i*36; a2=a1-36; am=radians(a1-18)
    o.append(f'\\path[draw,thick,{"fill=vurgu!20" if i%2==0 else "fill=none"}] (0,0) -- ({R*cos(radians(a1)):.3f},{R*sin(radians(a1)):.3f}) arc[start angle={a1},end angle={a2},radius={R}] -- cycle;')
    o.append(f'\\node[font=\\large\\bfseries] at ({0.74*R*cos(am):.3f},{0.74*R*sin(am):.3f}) {{{x}}};')
o.append(f'\\fill (0,0) circle (0.08); \\fill ({-0.16},{R+0.55}) -- (0.16,{R+0.55}) -- (0,{R+0.08}) -- cycle; \\node at (0,{R+0.8}) {{ibre}};')
SK=fig('\n'.join(o))
q('0001',tipId='ols-cark',tip='Eşit dilimli çark',z='kolay',alt='Çark',kaz='Eşit dilimli çarkın dilimlerindeki sayılardan koşula uyanları sayıp olasılığı bulur.',kalip='şekilli',
 kart='K-OLS-01 (çark) · 10 eşit dilim; asal ya da 4’ün katı → 8/10',
 metin='Bir lunaparkta, şekildeki eş dilimlere ayrılmış çark çevrilmekte ve ibre bir dilimde durmaktadır. Her dilimin üzerindeki sayı, o dilimde durulduğunda kazanılan puandır ve ibrenin her dilimde durma olasılığı eşittir.\nBuna göre, çark bir kez çevrildiğinde ibrenin üzerindeki sayı asal sayı ya da 4’ün katı olan bir dilimde durma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız asal sayılı dilimleri saymış: 6 dilim.','dikkat'),(e[1],'Aynı sayıyı taşıyan dilimleri tek saymış: farklı 8 sayıdan 6’sı koşula uyuyor.','dikkat'),(e[2],'“Ya da” için olasılıkları çarpmış: 3/5 · 1/5.','islem'),(e[3],'Yalnız 4’ün katı olanları (4 ve 8) saymış.','dikkat')],
 istenen='İbrenin asal ya da 4’ün katı sayılı dilimde durma olasılığı.',ip=['Çarktaki her dilimi ayrı ayrı say; aynı sayıdan birden fazla dilim olabileceğini unutma.'],bilgi=[TEM,ASL],sekil=SK,
 ad=[A('Dilimleri say','Çarkta 10 eş dilim vardır.','Tüm dilim: 10'),A('Asalları bul','2, 2, 3, 5, 5, 7 sayılı dilimler.','6 dilim'),A('4’ün katlarını ekle','4 ve 8 asal değildir ama 4’ün katıdır; iki küme ayrık olduğundan dilim sayıları toplanır.','6 + 2 = 8 dilim'),A('Oranla','İstenen dilim sayısı ÷ tüm dilim sayısı.','8/10 = 4/5')],
 puf='Eş dilimli çarkta olasılık, uygun dilim sayısının dilim sayısına oranıdır; aynı sayılı dilimler ayrı dilimdir.')

# ================= 02 kolay · tablo (kız/erkek × branş) =================
tb={'K':{'Futbol':6,'Basketbol':9,'Voleybol':8},'E':{'Futbol':12,'Basketbol':7,'Voleybol':4}}
tot=sum(sum(r.values()) for r in tb.values()); kiz=sum(tb['K'].values()); bas=tb['K']['Basketbol']+tb['E']['Basketbol']
v=Fr(kiz+tb['E']['Basketbol'],tot); assert tot==46 and kiz==23 and bas==16 and v==Fr(15,23)
e=[Fr(kiz+bas,tot),Fr(tb['K']['Basketbol'],tot),Fr(kiz,tot),Fr(kiz+bas-tb['K']['Basketbol']+0,tot)-Fr(0)]
e[3]=Fr(kiz*bas,tot*tot)  # çarpmış
assert e==[Fr(39,46),Fr(9,46),Fr(1,2),Fr(92,529)] and len({v,*e})==5
SK=tablo_svg(['Cinsiyet','Futbol','Basketbol','Voleybol'],[['Kız','6','9','8'],['Erkek','12','7','4']])
q('0002',tipId='ols-tablo',tip='Tablodan olasılık',z='kolay',alt='Tablodan Olasılık',kaz='Tablodaki sayılardan “ya da” içeren bir olayın olasılığını ortak kısmı bir kez sayarak bulur.',kalip='tablo',
 kart='K-OLS-02 (tablo) · 46 öğrenci; kız ya da basketbol → 30/46',
 metin='Bir okulun spor şenliğine katılan öğrencilerin her biri tabloda gösterilen üç branştan yalnızca birinde yarışmaktadır; tabloda her branştaki kız ve erkek öğrenci sayıları verilmiştir. Katılan öğrenciler arasından rastgele bir öğrenci seçilip ödül töreni için çağrılacaktır.\nBuna göre, seçilen öğrencinin kız ya da basketbol branşında yarışan biri olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Kız sayısı ile basketbol sayısını toplayıp ortak 9 öğrenciyi iki kez saymış: (23 + 16) ÷ 46.','dikkat'),(e[1],'“Ya da” yerine “ve” okumuş: yalnız basketbolda yarışan kızları (9) almış.','dikkat'),(e[2],'Yalnız kızları saymış: 23 ÷ 46.','dikkat'),(e[3],'Olasılıkları çarpmış: (23/46) · (16/46).','islem')],
 istenen='Seçilen öğrencinin kız ya da basketbolcu olma olasılığı.',ip=['Tablodaki bütün sayıları toplayıp toplam öğrenci sayısını bul; “ya da” olayında ortak öğrencileri bir kez say.'],bilgi=[TAB],sekil=SK,
 ad=[A('Toplamı bul','Tablodaki tüm sayılar toplanır.','6 + 9 + 8 + 12 + 7 + 4 = 46'),A('Kızları say','Kız satırı toplanır.','6 + 9 + 8 = 23'),A('Erkek basketbolcuları ekle','Kızlar zaten sayıldı; basketbol sütunundan yalnız erkekler eklenir.','23 + 7 = 30'),A('Oranla','Uygun öğrenci ÷ toplam öğrenci.','30/46 = 15/23')],
 puf='“A ya da B” sayılırken ortak elemanlar iki kez değil bir kez sayılır.')

# ================= 03 orta · hedef tahtası (4 eşit alanlı bölge) =================
Z=[10,6,6,2]; pairs=list(itertools.product(range(4),repeat=2))
v=Fr(sum(1 for a,b in pairs if Z[a]+Z[b]>=12),16); assert v==Fr(11,16)
e=[Fr(sum(1 for a,b in pairs if Z[a]+Z[b]>12),16),Fr(sum(1 for a,b in itertools.product(set(Z),repeat=2) if a+b>=12),9),Fr(sum(1 for a,b in pairs if Z[a]+Z[b]>=12 and not (Z[a]==6 and Z[b]==6)),16),Fr(sum(1 for a in Z if a>=6),4)]
assert e==[Fr(5,16),Fr(2,3),Fr(7,16),Fr(3,4)] and len({v,*e})==5
Rt=4.6; rr=[Rt*sqrt(k/4) for k in (1,2,3,4)]; o=[]
o.append(f'\\fill[fill=vurgu!25] (0,0) circle ({rr[0]:.4f}); \\fill[fill=vurgu!25,even odd rule] (0,0) circle ({rr[2]:.4f}) (0,0) circle ({rr[1]:.4f});')
for k in (3,2,1,0): o.append(f'\\draw[thick] (0,0) circle ({rr[k]:.4f});')
o.append(f'\\node[font=\\Large\\bfseries] at (0,0) {{{Z[0]}}};')
for k in (1,2,3): o.append(f'\\node[font=\\large\\bfseries] at (0,{-(rr[k-1]+rr[k])/2:.4f}) {{{Z[k]}}};')
SK=fig('\n'.join(o))
q('0003',tipId='ols-hedef',tip='Hedef tahtası ve iki atış',z='orta',alt='Hedef Tahtası',kaz='Alanları eşit bölgelerden oluşan hedef tahtasında iki atışın puan toplamı koşulunu sağlayan durumların olasılığını bulur.',kalip='hikâyeli',
 kart='K-OLS-03 (hedef tahtası) · 4 eşit alanlı bölge, puanlar 10-6-6-2; toplam ≥ 12 → 11/16',
 metin='Bir okul şenliğinde, şekildeki dairesel hedef tahtası alanları eşit olan 4 bölgeye ayrılmıştır; her bölgenin üzerindeki sayı, oraya isabet eden okun puanıdır. Bir öğrenci tahtaya iki ok atmakta; her ok tahtanın herhangi bir noktasına eşit olasılıkla saplanmakta ve atışlar birbirinden bağımsızdır.\nBuna göre, öğrencinin iki atışta aldığı puanların toplamının en az 12 olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Koşulu “12’den büyük” almış: (10,10) ve 10 ile 6’nın dört ikilisi (10 + 6 = 16) sayılmış.','dikkat'),(e[1],'Aynı puanlı iki bölgeyi tek puan saymış: 3 farklı puanla 9 durum üzerinden 6 uygun durum.','dikkat'),(e[2],'6 puanlık iki bölgenin birlikte atılmasını (6 + 6 = 12) saymamış.','dikkat'),(e[3],'Tek atışa bakmış: bir atışın en az 6 olma olasılığı.','dikkat')],
 istenen='İki atışın puanları toplamının en az 12 olma olasılığı.',ip=['Dört bölge eşit alanlı olduğundan her bölgeye isabet olasılığı eşittir; iki atışın 16 sıralı sonucunu düşün.'],bilgi=[GEO,BAG],sekil=SK,
 ad=[A('Bölge olasılığı','4 eşit alanlı bölgenin her birine isabet olasılığı 1/4’tür.','Atış başına 4 durum; iki atışta 4 · 4 = 16 sıralı durum'),A('10 puanın olduğu durumlar','İlk ya da ikinci atış 10 olursa toplam en az 12 olur: (10,10), (10,6) ×2 bölge, (10,2) ve ters sıralar.','(10,10): 1 · (10,6)+(6,10): 2·2 = 4 · (10,2)+(2,10): 2'),A('6 + 6 durumu','İki atış da 6 puanlık bölgelerden biri.','2 · 2 = 4 durum'),A('Oranla','Uygun durum ÷ tüm durum.','(1 + 4 + 2 + 4)/16 = 11/16')],
 puf='Aynı puanlı bölgeler ayrı bölgedir; iki atışın sonuçları sıralı çiftler olarak sayılır.')

# ================= 04 orta · iki torbadan birer top =================
T1={'K':4,'M':3,'Y':1}; T2={'K':2,'M':5,'Y':3}; n1,n2=sum(T1.values()),sum(T2.values())
v=sum(Fr(T1[c],n1)*Fr(T2[c],n2) for c in 'KMY'); assert v==Fr(13,40) and n1==8 and n2==10
e=[sum(Fr(T1[c],n1)*Fr(T2[c],n2) for c in 'KM'),Fr(math.comb(6,2)+math.comb(8,2)+math.comb(4,2),math.comb(18,2)),1-v,sum(Fr(T1[c],n1)**2 for c in 'KMY')]
assert e==[Fr(23,80),Fr(49,153),Fr(27,40),Fr(13,32)] and len({v,*e})==5
def torba(cx,T,ncol,ad):
    items=[c for c in 'KMY' for _ in range(T[c])]; rows=math.ceil(len(items)/ncol); sp=0.74; w=ncol*sp+0.3; h=rows*sp+0.3; r=[]
    r.append(f'\\draw[thick,rounded corners=6pt] ({cx},0) rectangle ({cx+w:.2f},{h:.2f}); \\node[font=\\normalsize\\bfseries] at ({cx+w/2:.2f},{h+0.35:.2f}) {{{ad}}};')
    for i,c in enumerate(items):
        rw,cl=divmod(i,ncol); x=cx+0.15+sp/2+cl*sp; y=h-0.15-sp/2-rw*sp
        fl={'K':'fill=vurgu!45','M':'fill=vurgu!15','Y':'fill=none'}[c]
        r.append(f'\\path[draw,thick,{fl}] ({x:.2f},{y:.2f}) circle (0.29); \\node[font=\\small\\bfseries] at ({x:.2f},{y:.2f}) {{{c}}};')
    return '\n'.join(r),w
b1,w1=torba(0,T1,4,'I. torba'); b2,w2=torba(w1+0.8,T2,5,'II. torba')
SK=fig(b1+'\n'+b2+f'\n\\node at ({(w1+0.8+w2)/2:.2f},-0.45) {{K: kırmızı \\quad M: mavi \\quad Y: yeşil}};')
q('0004',tipId='ols-torba',tip='İki torbadan birer top çekme',z='orta',alt='İki Torba',kaz='İki torbanın renk dağılımından, birer top çekildiğinde topların aynı renk olma olasılığını bulur.',kalip='hikâyeli',
 kart='K-OLS-04 (iki torba) · I: 4K 3M 1Y, II: 2K 5M 3Y → 13/40',
 metin='Bir oyun standında, şekilde dağılımı gösterilen iki torba bulunmaktadır; torbaların içindeki toplar renkleri dışında birbirinin aynıdır. Oyuncu her torbadan gözü kapalı olarak rastgele birer top çekmekte ve çektiği iki top aynı renkteyse ödül kazanmaktadır.\nBuna göre, bir oyuncunun ödül kazanma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Yeşil topları unutmuş; yalnız kırmızı ve mavi eşleşmelerini toplamış.','dikkat'),(e[1],'Bütün 18 topu tek torbaya koymuş gibi 2 top çekmiş: aynı renkli ikililer ÷ C(18, 2).','dikkat'),(e[2],'Aynı renk yerine farklı renk olasılığını (1 − 13/40) vermiş.','dikkat'),(e[3],'İkinci torbayı da birinci torba gibi sanmış: (4/8)² + (3/8)² + (1/8)².','dikkat')],
 istenen='İki topun aynı renk olma olasılığı.',ip=['Her torbada her rengin olasılığını ayrı yaz; hangi renk çiftlerinin ödül verdiğini düşün.'],bilgi=[BAG],sekil=SK,
 ad=[A('Torbalardaki toplar','Her torbada renk sayıları okunur.','I: 4 K, 3 M, 1 Y (8 top) · II: 2 K, 5 M, 3 Y (10 top)'),A('Kırmızı çifti','İki torbada da kırmızı gelmesi.','4/8 · 2/10 = 1/10'),A('Mavi ve yeşil çiftleri','Aynı işlem diğer renkler için yapılır.','3/8 · 5/10 = 3/16 · 1/8 · 3/10 = 3/80'),A('Topla','Ödül veren üç durum birbirini dışlar.','8/80 + 15/80 + 3/80 = 26/80 = 13/40')],
 puf='Torbalardan çekilen toplar bağımsızdır; her renk için olasılıklar çarpılır, renkler toplanır.')

# ================= 05 orta · iki özel zar tablosu =================
ZA=[1,2,2,3,4,6]; ZB=[1,2,2,4,5,6]; pr={2,3,5,7,11,13}
S=[a+b for b in ZB for a in ZA]; v=Fr(sum(1 for s in S if s in pr),36); assert v==Fr(5,12)
ds=set(S); e=[Fr(len([s for s in ds if s in pr]),len(ds)),1-v,Fr(sum(1 for s in S if s%2),36),Fr(sum(1 for s in S if s in pr and s>2),36)]
assert e==[Fr(5,11),Fr(7,12),Fr(4,9),Fr(7,18)] and len({v,*e})==5
say={t:sum(1 for s_ in S if s_==t) for t in (2,3,5,7,11,13)}; assert say=={2:1,3:4,5:4,7:5,11:1,13:0} and sum(say.values())==15
cw=0.95; o=[]
o.append(f'\\fill[fill=vurgu!20] (0,0) rectangle ({7*cw:.2f},{cw}); \\fill[fill=vurgu!20] (0,0) rectangle ({cw},{-6*cw:.2f});')
for i,a in enumerate(ZA): o.append(f'\\node[font=\\large\\bfseries] at ({(i+1.5)*cw:.2f},{0.5*cw:.2f}) {{{a}}};')
for j,b in enumerate(ZB): o.append(f'\\node[font=\\large\\bfseries] at ({0.5*cw:.2f},{-(j+0.5)*cw:.2f}) {{{b}}};')
o.append(f'\\node at ({0.5*cw:.2f},{0.5*cw:.2f}) {{$+$}};')
for j in range(6):
    for i in range(6): o.append(f'\\node at ({(i+1.5)*cw:.2f},{-(j+0.5)*cw:.2f}) {{{ZA[i]+ZB[j]}}};')
for k in range(8): o.append(f'\\draw[thin] ({k*cw:.2f},{cw}) -- ({k*cw:.2f},{-6*cw:.2f});')
for k in range(8): o.append(f'\\draw[thin] (0,{cw-k*cw:.2f}) -- ({7*cw:.2f},{cw-k*cw:.2f});')
o.append(f'\\draw[thick] (0,{cw}) rectangle ({7*cw:.2f},{-6*cw:.2f}); \\node[above] at ({4.5*cw:.2f},{cw+0.05}) {{I. zarın yüzleri}}; \\node[rotate=90,above] at (-0.1,{-2.5*cw:.2f}) {{II. zarın yüzleri}};')
SK=fig('\n'.join(o))
q('0005',tipId='ols-zar',tip='Zar tablosu',z='orta',alt='Özel Zarlar Tablosu',kaz='İki özel zarın toplam tablosunda koşula uyan hücreleri sayıp olasılığı bulur.',kalip='tablo',
 kart='K-OLS-05 (özel zar tablosu) · 36 hücre; toplam asal → 15/36',
 metin='Yüzlerindeki sayılar standart zardan farklı olan, hilesiz iki özel zar birlikte atılıyor. Tabloda, I. zarın yüzleri ilk satıra, II. zarın yüzleri ilk sütuna yazılmış; diğer hücrelere de iki zarın üst yüzlerindeki sayıların toplamı yazılmıştır. Her zarın altı yüzünün gelme olasılığı eşittir.\nBuna göre, atışta görülen sayıların toplamının asal sayı olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Hücreleri değil farklı toplam değerlerini saymış: 11 farklı toplamdan 5’i asal.','dikkat'),(e[1],'Asal olmayanların olasılığını vermiş (1 − 5/12).','dikkat'),(e[2],'Asal yerine tek toplamları saymış: 16 hücre.','dikkat'),(e[3],'2’yi asal saymamış: 3, 5, 7, 11 toplamlarının 14 hücresini saymış.','dikkat')],
 istenen='Toplamın asal sayı olma olasılığı.',ip=['36 hücrenin her biri eşit olasılıklıdır; aynı toplamın birden fazla hücrede bulunabileceğini unutma.'],bilgi=[SAY,ASL],sekil=SK,
 ad=[A('Hücre sayısı','Her iki zarın altı yüzü vardır.','6 · 6 = 36 hücre'),A('Asal toplamları işaretle','Tabloda en büyük toplam 12’dir; 2, 3, 5, 7, 11 toplamlarının geçtiği hücreler sayılır.','2: 1 hücre · 3: 4 · 5: 4 · 7: 5 · 11: 1 hücre'),A('Say','Asal toplamlı hücreler.','1 + 4 + 4 + 5 + 1 = 15'),A('Oranla','Uygun hücre ÷ tüm hücre.','15/36 = 5/12')],
 puf='Tablodaki her hücre bir sonuçtur; aynı değer birden fazla hücrede varsa her hücre ayrı sayılır.')

# ================= 06 zor · ağaç diyagramı =================
pm=[Fr(1,2),Fr(3,10),Fr(1,5)]; ps=[Fr(19,20),Fr(9,10),Fr(4,5)]; assert sum(pm)==1
v=sum(a*b for a,b in zip(pm,ps)); assert v==Fr(181,200)
e=[1-v,sum(a*b for a,b in zip(pm[:2],ps[:2])),1-sum(1-b for b in ps),sum(ps)/3]
assert e==[Fr(19,200),Fr(149,200),Fr(13,20),Fr(53,60)] and len({v,*e})==5
o=[]; ys=[2.6,0,-2.6]
for i,y in enumerate(ys):
    o.append(f'\\draw[thick] (0,0) -- node[above,sloped,pos=0.55] {{${fs(pm[i])}$}} (3.0,{y}); \\node[draw,thick,circle,inner sep=1.5pt,fill=vurgu!20] at (3.0,{y}) {{$M_{i+1}$}};')
    for dy,lab,p in ((0.7,'S',ps[i]),(-0.7,'D',1-ps[i])):
        o.append(f'\\draw[thick] (3.3,{y}) -- node[{"above" if dy>0 else "below"},sloped,pos=0.5] {{${fs(p)}$}} (6.6,{y+dy}); \\node[draw,thick,rounded corners=2pt,fill={"vurgu!20" if lab=="S" else "none"},inner sep=3pt,anchor=west] at (6.7,{y+dy}) {{{"kusursuz" if lab=="S" else "kusurlu"}}};')
SK=fig('\n'.join(o))
q('0006',tipId='ols-agac',tip='Ağaç diyagramı',z='orta',alt='Ağaç Diyagramı',kaz='İki aşamalı ağaç diyagramında dalların olasılıklarını çarpıp toplayarak istenen olayın olasılığını bulur.',kalip='hikâyeli',
 kart='K-OLS-06 (ağaç diyagramı) · üç makine, kusursuz → 181/200',
 metin='Bir fabrikada üretilen parçalar M₁, M₂ ve M₃ makinelerinden birinde üretilmektedir. Şekildeki ağaç diyagramında, üretilen bir parçanın hangi makineden geldiği ve o makinenin parçasının kusursuz ya da kusurlu çıkma olasılıkları gösterilmiştir. Üretim bandından rastgele bir parça alınmaktadır.\nBuna göre, alınan parçanın kusursuz olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Sorulan yerine kusurlu olma olasılığını (1 − 181/200) vermiş.','dikkat'),(e[1],'M₃ dalını unutmuş; yalnız M₁ ve M₂ dallarını toplamış.','dikkat'),(e[2],'Kusurlu olasılıklarını makine payına bakmadan toplayıp 1’den çıkarmış: 1 − (1/20 + 1/10 + 1/5).','dikkat'),(e[3],'Kusursuz olasılıklarını makine payına bakmadan ortalamış: (19/20 + 9/10 + 4/5) ÷ 3.','dikkat')],
 istenen='Alınan parçanın kusursuz olma olasılığı.',ip=['Her makine için “makineden gelme” ve “kusursuz olma” dallarını birlikte düşün; sonra makineleri birleştir.'],bilgi=[AGA],sekil=SK,
 ad=[A('M₁ dalı','Dal boyunca olasılıklar çarpılır.','1/2 · 19/20 = 19/40'),A('M₂ dalı','Aynı işlem.','3/10 · 9/10 = 27/100'),A('M₃ dalı','Aynı işlem.','1/5 · 4/5 = 4/25'),A('Paydayı eşitle','Üç dalın payları 200’lük kesre çevrilir.','95/200 + 54/200 + 32/200'),A('Topla','Kusursuz çıkan dallar toplanır.','181/200')],
 puf='Ağaçta bir olayı veren dallar ayrı ayrı çarpılır, sonra toplanır; her makinenin payı dikkate alınır.')

# ================= 07 zor · kart destesi =================
kupa=[8,5,1,10,4]; maca=[2,12,6,9]
cards=[('h',x) for x in kupa]+[('s',x) for x in maca]; pairs=list(itertools.combinations(cards,2)); T=len(pairs)
v=Fr(sum(1 for a,b in pairs if a[0]==b[0] and (a[1]+b[1])%2==0),T); assert v==Fr(7,36) and T==36
e=[Fr(sum(1 for a,b in pairs if a[0]==b[0]),T),Fr(sum(1 for a,b in pairs if (a[1]+b[1])%2==0),T),Fr(sum(1 for a in cards for b in cards if a[0]==b[0] and (a[1]+b[1])%2==0),81),Fr(sum(1 for a,b in pairs if a[0]==b[0] and (a[1]+b[1])%2==1),T)]
assert e==[Fr(4,9),Fr(1,2),Fr(23,81),Fr(1,4)] and len({v,*e})==5
dizi=[('h',8),('s',2),('h',5),('s',12),('h',1),('s',6),('h',10),('s',9),('h',4)]; assert sorted(dizi)==sorted(cards)
o=[]
for i,(s_,x) in enumerate(dizi):
    cx=i*1.12; sym='\\heartsuit' if s_=='h' else '\\spadesuit'
    o.append(f'\\draw[thick,rounded corners=3pt] ({cx:.2f},0) rectangle ({cx+0.95:.2f},1.6); \\node[font=\\large\\bfseries] at ({cx+0.475:.2f},1.08) {{{x}}}; \\node[font=\\large] at ({cx+0.475:.2f},0.45) {{${sym}$}};')
o.append(f'\\node at (4.5,-0.45) {{$\\heartsuit$: kupa \\quad $\\spadesuit$: maça}};')
SK=fig('\n'.join(o))
q('0007',tipId='ols-deste',tip='Kart destesi şeması',z='zor',alt='Kart Destesi',kaz='Kartların simge ve sayı özelliklerine göre geri konmadan çekilen iki kartın olasılığını kombinasyonla bulur.',kalip='şekilli',
 kart='K-OLS-07 (kart destesi) · 5 kupa, 4 maça; aynı simge ve çift toplam → 7/36',
 metin='Şekildeki dokuz kart, yüzleri aşağı bakacak biçimde karıştırılıp bir masaya konuyor. Kartların her birinde bir doğal sayı ve kupa ya da maça simgesi bulunmaktadır. Masadan rastgele ve aynı anda iki kart seçiliyor.\nBuna göre, seçilen iki kartın simgelerinin aynı ve üzerlerindeki sayıların toplamının çift olma olasılığı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız simgesi aynı olan ikilileri saymış (10 + 6 = 16).','dikkat'),(e[1],'Simge koşulunu unutmuş; yalnız toplamı çift olan ikilileri saymış (15 + 3 = 18 ikili).','dikkat'),(e[2],'Kartı geri koyarak çekmiş gibi 81 durum üzerinden saymış.','dikkat'),(e[3],'Toplamı çift yerine tek olan, simgesi aynı ikilileri saymış (9 ikili).','dikkat')],
 istenen='İki kartın simgesi aynı ve sayı toplamı çift olma olasılığı.',ip=['Önce kartları simgesine göre, sonra sayılarının tek ya da çift olmasına göre grupla.'],bilgi=[KOM,B('Çift toplam','iki sayının toplamı, ikisi de tek ya da ikisi de çift ise çifttir. Örnek: 3 + 5 = 8 ve 4 + 6 = 10 çifttir, 3 + 4 = 7 tektir')],sekil=SK,
 ad=[A('Tüm ikililer','9 karttan 2’si seçilir.','C(9, 2) = 36'),A('Kupa kartları','Kupa: 8, 5, 1, 10, 4 → 3 çift, 2 tek sayı. Toplamı çift olan ikililer.','C(3, 2) + C(2, 2) = 3 + 1 = 4'),A('Maça kartları','Maça: 2, 12, 6, 9 → 3 çift, 1 tek sayı.','C(3, 2) + C(1, 2) = 3 + 0 = 3'),A('Oranla','Uygun ikili ÷ tüm ikili.','(4 + 3)/36 = 7/36')],
 puf='Aynı simgeli kartlar kendi içinde sayılır; toplam çift olması için iki sayı da tek ya da iki sayı da çift olmalıdır.')

bitir(P,'olasisek','matd|Olasılık')
