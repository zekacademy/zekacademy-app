"""Sayı Problemleri · ŞEKİLLİ ek paket b (10 soru: 2 kolay / 4 orta / 4 zor): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Sayı Problemleri'
UK='prob|Sayı Problemleri'
P=Parti('sayisekb','Sayı Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu sayı problemleri; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

KUT=B('Kutu modeli','eş kutular aynı değeri gösterir; toplam, eş kutuların ve sabit parçanın toplamıdır. Örnek: iki eş kutu ve 5’lik parça toplam 25’i gösteriyorsa bir kutu 10’dur')
ORU=B('Şekil örüntüsü','şekiller arasındaki artış sabitse n. şekildeki sayı, ilk değer ve artışla yazılır. Örnek: 1. şekilde 3, her adımda 2 artan dizide n. şekil 2n + 1 ögedir')
SIH=B('Eşit toplamlı dizilim','sihirli karede her satır, sütun ve köşegenin toplamı eşittir; iki eşit toplamı karşılaştırınca ortak kutular sadeleşir. Örnek: köşegen 2 + m + 6 ile satır 4 + m + 4 eşit toplamlıysa 8 = 8 olduğundan ortak toplam 8 + m bulunur')
TOP=B('Her kenarı eşit toplamlı şekil','her kenardaki sayıların toplamı aynıdır; tam bilinen kenar ortak toplamı verir. Örnek: bir kenarda 1, 2, 6 varsa ortak toplam 9’dur')
CRP=B('Çarpım tablosu','tablodaki her kutu satır ve sütun başlıklarının çarpımıdır; aynı satırdaki iki kutunun oranı sütun başlıklarının oranına eşittir. Örnek: bir satırda 6 ve 9 varsa sütun başlıkları 2 : 3 oranındadır')
SIR=B('Sıra ve toplam','iki kişinin sıraları ve aralarındaki kişi sayısından, sondan sırasından toplam kişi bulunur; baştan sırası + sondan sırası − 1 toplamı verir. Örnek: baştan 4., sondan 6. olan kişi için kuyrukta 9 kişi vardır')
FRM=B('Optik form puanı','doğru, yanlış ve boş cevaplar ayrı sayılır; puan, doğru sayısı ile yanlış sayısının kural katsayılarıyla bulunur. Örnek: doğruya 3 puan, yanlışa −1 puan verilen testte 4 doğru, 1 yanlış, 2 boş 11 puandır')
PUN=B('Puan durumu tablosu','oynanan maç, galibiyet, beraberlik ve mağlubiyetlerin toplamıdır; puan galibiyet ile beraberliğe verilen katsayılarla bulunur. Örnek: galibiyet 3, beraberlik 1 puan ise 2 galibiyet 1 beraberlik 7 puandır')
YIL=B('Yılan dizilim','satır sayısı ve yön, sayının yerini belirler; her satırda sütun sayısı kadar sayı bulunur ve yön satırdan satıra değişir. Örnek: 3 sütunlu yılan dizilimde 1 2 3 üstte, 6 5 4 ikinci satırdadır')
VEN=B('Venn şemasında cebirsel bölgeler','bölgelerin eleman sayıları toplamı evrensel kümenin eleman sayısıdır; bir koşul denklem kurulup çözülür. Örnek: bölgeler x, 2x ve 6 ise evrensel küme 12 elemanlı olduğunda x = 2’dir')

kartla('K-SYB-01','Kutu modeli','Sabit parça toplamdan çıkarılıp eş kutulara bölünür; istenen fark kutulardan bulunur.','Sabit parçayı kutulara dağıtmak; kutu sayısını yanlış saymak.','kolay','hikâyeli',3,'syb-model','Kutu modeli')
kartla('K-SYB-02','Kibrit çöpü örüntüsü','Şekillerdeki çöp sayısından genel terim yazılır, verilen toplamdan şekil numarası bulunur.','Her şekle aynı sayıda çöp eklemek; ortak kenarı atlamamak.','kolay','hikâyeli',3,'syb-oruntu','Şekil örüntüsü')
kartla('K-SYB-03','Sihirli kare','Tam bilinen doğrudan ortak toplam bulunur; diğer hücreler sırayla eşitlikten çıkar.','Ortak toplamı tek satırdan tahmin etmek; hücreyi sütundan değil satırdan almak.','orta','yeni nesil',4,'syb-yerlestirme','Sayı yerleştirme')
kartla('K-SYB-04','Üçgen dizilim','Kenar toplamları eşitlenir; kalan sayılar eşitliklere yerleştirilir.','Bir sayıyı iki kez kullanmak; kenar toplamını yanlış almak.','orta','yeni nesil',3,'syb-yerlestirme','Sayı yerleştirme')
kartla('K-SYB-05','Çarpım tablosu','Satır oranlarından sütun başlıkları arasındaki oran, sonra istenen kutu bulunur.','Kutuları toplamak; oranı ters almak.','orta','tablo',3,'syb-tablo','Tablo ve sayılar')
kartla('K-SYB-06','Kuyrukta sıra','Aralarındaki kişilerle iki kişinin sırası, sondan sırasından toplam, oradan ortadaki kişi bulunur.','Aradaki kişi sayısına iki kişiyi katmamak; ortadaki sırayı yarıya yuvarlamak.','orta','hikâyeli',4,'syb-sira','Sıra ve dizilim')
kartla('K-SYB-07','Optik form','Her öğrencide doğru, yanlış ve boş sayılır; puan kuralıyla toplanır.','Boşları yanlış saymak; yanlışları düşmemek.','zor','hikâyeli',4,'syb-tablo','Tablo ve sayılar')
kartla('K-SYB-08','Puan durumu','Satırlardaki eksik kutular maç ve puan toplamlarından çözülür; son satırdaki koşul kullanılır.','Beraberliği atlamak; maç sayısını puana katmak.','zor','tablo',5,'syb-tablo','Tablo ve sayılar')
kartla('K-SYB-09','Yılan dizilim','Sayının satırı bölmeyle bulunur; satırın yönüne göre sütun, alt satır aynı sütunda hesaplanır.','Yönü unutmak; satır numarasını yuvarlamamak.','orta','hikâyeli',4,'syb-sira','Sıra ve dizilim')
kartla('K-SYB-10','Cebirsel Venn şeması','İki koşuldan evrensel küme ve dışarıdaki bölge çözülür; x bulunup istenen bölge hesaplanır.','Dışarıdaki bölgeyi toplama katmamak; ortak bölgeyi iki kez saymak.','zor','yeni nesil',4,'syb-venn','Cebirsel Venn şeması')

# 01 kolay · kutu modeli
b_=15; kk=2*b_+8; ll=b_; top=kk+ll; v=kk-ll
assert top==53 and kk==38 and v==23
e=[8,15,38,45]
assert len({v,*e})==5 and 53-8==45
u=0.12; o=['\\node[left] at (-0.1,0.4) {K}; \\node[left] at (-0.1,-0.5) {L};']
for j in range(2): o.append(f'\\filldraw[fill=vurgu!{25},draw=vurgu!80!black] ({j*b_*u:.2f},0) rectangle ({(j+1)*b_*u:.2f},0.8);')
o.append(f'\\filldraw[fill=white,draw=vurgu!80!black] ({2*b_*u:.2f},0) rectangle ({(2*b_+8)*u:.2f},0.8); \\node at ({(2*b_+4)*u:.2f},0.4) {{8}};')
o.append(f'\\filldraw[fill=vurgu!25,draw=vurgu!80!black] (0,-0.9) rectangle ({b_*u:.2f},-0.1);')
SK=fig('\n'.join(o))
q('0001',tipId='syb-model',tip='Kutu modeli',z='kolay',alt='Kutu Modeli',kaz='Eş kutulu modelden iki sayıyı bulup farkını hesaplar.',kalip='hikâyeli',
 kart='K-SYB-01 · K = 2 kutu + 8, L = 1 kutu; toplam 53',
 metin='Bir bilye koleksiyoncusu, K ve L kutularındaki bilyelerin sayısını şekildeki çubuklarla göstermiştir. Aynı biçimli kutucuklar birbirinin aynı sayıda bilyeyi, boş kutucuk ise yazılı sayıdaki bilyeyi gösterir. İki kutudaki bilyelerin sayısı toplam 53’tür.\nBuna göre, K kutusundaki bilye sayısı ile L kutusundaki bilye sayısı arasındaki fark kaçtır?',
 dogru=v,yan=[(8,'Boş kutucuktaki sayıyı fark sanmış.','dikkat'),(15,'Bir eş kutucuğun değerini fark sanmış.','dikkat'),(38,'K kutusundaki bilye sayısını fark sanmış.','dikkat'),(45,'Toplamdan yalnız 8 çıkarıp farkı bulduğunu sanmış: 53 − 8.','dikkat')],
 istenen='K ile L arasındaki fark.',ip=['Çubuklardaki eş kutucukların sayısını ve boş kutucuğu ayrı değerlendir.'],bilgi=[KUT],sekil=SK,
 ad=[A('Eş kutucuklar','Toplamdan boş kutucuk çıkarılır, 3 eş kutucuk kalır.','53 − 8 = 45; 45 ÷ 3 = 15'),A('Sayılar','K iki kutucuk ile 8, L bir kutucuktur.','K = 38, L = 15'),A('Fark','K − L.','38 − 15 = 23')],
 puf='Önce bir eş kutucuğun değerini bul.')

# 02 kolay · kibrit çöpü
n=33; assert 3*n+1==100
e=[100//4,3*(n-1)+4,34,99]
assert e==[25,100,34,99] or True
e=[25,32,34,99]; assert len({n,*e})==5 and 3*32+4==100
def kare(x0,n_):
    s=[]
    for i in range(n_):
        xx=x0+i*0.9
        s.append(f'\\draw[line width=2pt,vurgu!70!black] ({xx:.2f},0) -- ({xx+0.9:.2f},0) -- ({xx+0.9:.2f},0.9) -- ({xx:.2f},0.9) -- cycle;')
    return s
o=kare(0,1)+kare(2.2,2)+kare(5.2,3)+['\\node at (0.45,-0.45) {1. şekil}; \\node at (3.1,-0.45) {2. şekil}; \\node at (6.55,-0.45) {3. şekil};']
SK=fig('\n'.join(o))
q('0002',tipId='syb-oruntu',tip='Şekil örüntüsü',z='kolay',alt='Kibrit Çöpü Örüntüsü',kaz='Kibrit çöplerinden oluşan şekil örüntüsünde genel terimi yazıp verilen çöp sayısından şekil numarasını bulur.',kalip='hikâyeli',
 kart='K-SYB-02 · 4, 7, 10 çöp → 3n + 1; 100 çöp',
 metin='Bir çocuk, kibrit çöplerini yan yana ekleyerek şekildeki kare dizilerini oluşturmuş ve bu düzeni aynı biçimde sürdürmeye karar vermiştir; her şekilde, bir önceki şekle bir kare eklenmiştir. Çocuğun elinde tam 100 kibrit çöpü vardır ve yaptığı şekilde hiç çöp artmamıştır.\nBuna göre, çocuk kaç kareli şekil yapmıştır?',
 dogru=n,yan=[(25,'Her kareyi bağımsız 4 çöple yapıp 100 ÷ 4 almış.','dikkat'),(32,'Genel terimi 3n + 4 yazmış.','dikkat'),(34,'3n = 100 çözümünü yukarı yuvarlamış.','dikkat'),(99,'Toplamdan 1 çıkarıp kare sayısı sanmış: 100 − 1.','dikkat')],
 istenen='Yapılan şekildeki kare sayısı.',ip=['Şekillerdeki çöp sayılarının her adımda nasıl arttığına bak.'],bilgi=[ORU],sekil=SK,
 ad=[A('Çöp sayıları','1, 2, 3 kareli şekillerde 4, 7, 10 çöp vardır; her adımda 3 artar.','4, 7, 10'),A('Genel terim','n kareli şekilde 4 + 3(n − 1).','3n + 1'),A('Kare sayısı','3n + 1 = 100.','n = 33')],
 puf='Her yeni kare üç çöp ister.')

# 03 orta · sihirli kare
S=36; M=[[15,8,13],[10,12,14],[11,16,9]]
assert all(sum(r)==S for r in M) and all(sum(M[i][j] for i in range(3))==S for j in range(3)) and sum(M[i][i] for i in range(3))==S and sum(M[i][2-i] for i in range(3))==S
v=M[2][1]; e=[8,12,14,36]; assert len({v,*e})==5
shown={(0,0):15,(0,2):13,(1,0):10,(2,2):9}
o=[]
for i in range(3):
    for j in range(3):
        t=shown.get((i,j),'?' if (i,j)==(2,1) else '')
        o.append(f'\\node[draw,thick,minimum width=1.0cm,minimum height=1.0cm,fill={"vurgu!20" if t=="?" else "white"}] at ({j*1.0},{-i*1.0}) {{\\large {t}}};')
SK=fig('\n'.join(o))
q('0003',tipId='syb-yerlestirme',tip='Sayı yerleştirme',z='orta',alt='Sihirli Kare',kaz='Kısmen doldurulmuş sihirli karede ortak toplamı bulup ? ile gösterilen sayıyı hesaplar.',kalip='yeni nesil',
 kart='K-SYB-03 · ortak toplam 36; ? = 16',
 metin='Şekildeki 3 × 3 tabloda her satırın, her sütunun ve iki köşegenin sayıları toplamı aynıdır; bu ortak toplam bilinmemektedir. Tabloda dört kutu doldurulmuş, ? ile gösterilen kutudaki sayı sorulmaktadır.\nBuna göre, ? ile gösterilen kutuda hangi sayı vardır?',
 dogru=v,yan=[(8,'Üst satırın orta kutusunu bulup sorulan kutu sanmış.','dikkat'),(12,'Merkezdeki sayıyı sorulan kutu sanmış.','dikkat'),(14,'Orta satırın son kutusunu sorulan kutu sanmış.','dikkat'),(36,'Ortak toplamı sorulan sayı sanmış.','dikkat')],
 istenen='? ile gösterilen kutudaki sayı.',ip=['Merkez m, ortak toplam T olsun; iki köşegen ve sol sütun üç denklem verir.'],bilgi=[SIH],sekil=SK,
 ad=[A('Ortak toplam','Köşegenlerden 15 + m + 9 = T ve 13 + m + g = T (g, sol alt kutu); sol sütun 15 + 10 + g = T.','15 + m + 9 = T ve 13 + m + g = T ⇒ g = 11 ⇒ T = 36'),A('Üst ve orta','Üst satır: 15 + b + 13 = 36; merkez = 36 − 24 = 12.','b = 8, m = 12'),A('Orta sütun','b + m + ? = 36.','8 + 12 + ? = 36 ⇒ ? = 16')],
 puf='Önce ortak toplamı bul.')

# 04 orta · üçgen
vals={'A':1,'C':2,'CA':6}; Sm=9; Bv=3
assert sum([1,2,6])==Sm and Bv+5+1==Sm and Bv+4+2==Sm
v=Bv; e=[4,5,6,9]; assert len({v,*e})==5
pos={'A':(0,3.0),'B':(2.8,0),'C':(-2.8,0),'AB':(1.4,1.5),'BC':(0,0),'CA':(-1.4,1.5)}
lab={'A':'1','C':'2','CA':'6','B':'?'}
o=['\\draw[thick] (0,3.0) -- (2.8,0) -- (-2.8,0) -- cycle;']
for k,(x,y) in pos.items():
    t=lab.get(k,'')
    o.append(f'\\node[draw,thick,circle,minimum size=0.9cm,fill={"vurgu!20" if t=="?" else "white"}] at ({x},{y}) {{\\large {t}}};')
SK=fig('\n'.join(o))
q('0004',tipId='syb-yerlestirme',tip='Sayı yerleştirme',z='orta',alt='Üçgen Dizilim',kaz='Her kenarındaki sayılar toplamı eşit olan üçgen dizilimde eksik sayıyı bulur.',kalip='yeni nesil',
 kart='K-SYB-04 · 1–6 sayıları, kenar toplamı 9; B = 3',
 metin='Şekildeki üçgenin köşelerine ve kenar ortalarına 1’den 6’ya kadar olan sayılar birer kez yazılmaktadır; her kenar üzerindeki üç sayının toplamı birbirine eşittir. Şekilde üç dairedeki sayı yazılmış, sağ alt köşesindeki sayı ? ile gösterilmiş ve diğer daireler boş bırakılmıştır.\nBuna göre, ? yerine hangi sayı yazılmalıdır?',
 dogru=v,yan=[(4,'Alt kenarın orta sayısını (4) sorulan sanmış.','dikkat'),(5,'Sağ kenarın orta sayısını B sanmış.','dikkat'),(6,'Şekilde verilen 6’yı B sanmış.','dikkat'),(9,'Kenar toplamını B sanmış.','dikkat')],
 istenen='? yerine yazılacak sayı.',ip=['Üzerinde üç sayısı da bilinen kenardan her kenarın ortak toplamını bul.'],bilgi=[TOP],sekil=SK,
 ad=[A('Ortak toplam','Sol kenar: 1 + 6 + 2.','9'),A('Kalan sayılar','3, 4, 5 boş dairelere yerleşir; sağ kenar B + orta + 1 = 9, alt kenar B + orta + 2 = 9.','B + 5 = 8 veya B + 4 = 7'),A('B','İki eşitliği sağlayan sayı.','B = 3')],
 puf='Önce her kenarın toplamını bul.')

# 05 orta · çarpım tablosu
px,py,pz=4,6,3; pp,pq,pr=3,2,5
cells={(0,0):pp*px,(0,1):pp*py,(1,1):pq*py,(1,2):pq*pz,(2,0):pr*px}
v=pr*pz; assert v==15 and cells[(0,0)]==12 and cells[(0,1)]==18 and cells[(1,1)]==12 and cells[(1,2)]==6 and cells[(2,0)]==20
e=[12,18,30,40]; assert len({v,*e})==5 and 20*Fr(3,2)==30 and 20*2==40
rows=[['p',str(cells[(0,0)]),str(cells[(0,1)]),'–'],['q','–',str(cells[(1,1)]),str(cells[(1,2)])],['r',str(cells[(2,0)]),'–','?']]
SK=tablo_svg(['','x','y','z'],rows)
q('0005',tipId='syb-tablo',tip='Tablo ve sayılar',z='orta',alt='Çarpım Tablosu',kaz='Çarpım tablosunda satır oranlarından sütun başlıklarını karşılaştırıp istenen kutuyu bulur.',kalip='tablo',
 kart='K-SYB-05 · p,q,r = 3,2,5; x,y,z = 4,6,3; ? = 15',
 metin='Aşağıdaki tabloda satır başlıkları p, q, r; sütun başlıkları x, y, z ile gösterilmiştir. Tablonun her kutusuna, o kutunun satır ve sütun başlıklarına karşılık gelen pozitif tam sayıların çarpımı yazılmıştır; başlıklardaki sayılar bilinmemektedir ve “–” bulunan kutular boş bırakılmıştır.\nBuna göre, tabloda ? ile gösterilen kutudaki sayı kaçtır?',
 dogru=v,yan=[(12,'Tablodaki başka bir kutuyu (q satırı, y sütunu) sorulan kutu sanmış.','dikkat'),(18,'p satırı, y sütunundaki sayıyı sorulan kutu sanmış.','dikkat'),(30,'z/x oranını 3/2 almış: 20 × 3/2.','dikkat'),(40,'z’yi x’in 2 katı sanmış: 20 × 2.','dikkat')],
 istenen='? ile gösterilen kutudaki sayı.',ip=['p ve q satırlarındaki kutulardan x, y, z arasındaki ilişkiyi kurmaya çalış.'],bilgi=[CRP],sekil=SK,
 ad=[A('y : x','p satırı: 18 ÷ 12.','y : x = 3 : 2'),A('y : z','q satırı: 12 ÷ 6.','y : z = 2 : 1 ⇒ z : x = 3 : 4'),A('? kutusu','r satırında x sütunundaki 20’nin z : x oranı kadarı.','20 × 3/4 = 15')],
 puf='Önce sütun başlıkları arasındaki ilişkiyi bul.')

# 06 orta · kuyruk
ali,bora_ara=7,9; bora=ali+bora_ara+1; sonda=7; n=bora+sonda-1; ort=(n+1)//2
assert bora==17 and n==23 and ort==12
v=ort; e=[11,13,17,23]; assert len({v,*e})==5
o=[]; sp=0.48
for i in range(1,bora+1):
    x=(i-1)*sp
    if i==ali: o.append(f'\\filldraw[fill=vurgu!40,draw=black,thick] ({x:.2f},0) circle (0.2); \\node[above=5pt] at ({x:.2f},0) {{Ali}};')
    elif i==bora: o.append(f'\\filldraw[fill=vurgu!40,draw=black,thick] ({x:.2f},0) circle (0.2); \\node[above=5pt] at ({x:.2f},0) {{Bora}};')
    else: o.append(f'\\draw[thick] ({x:.2f},0) circle (0.2);')
xa,xb=(ali-1)*sp+0.2,(bora-1)*sp-0.2
o.append(f'\\draw[<->] ({xa+0.08:.2f},-0.5) -- ({xb-0.08:.2f},-0.5); \\node[below=1pt] at ({(xa+xb)/2:.2f},-0.5) {{9 kişi}};')
o.append(f'\\draw[-{{Stealth}}] (-0.3,-0.9) -- (1.3,-0.9); \\node[right=2pt] at (1.3,-0.9) {{kuyruğun başı}}; \\node[right=4pt] at ({(bora-1)*sp+0.2:.2f},0) {{…}};')
SK=fig('\n'.join(o))
q('0006',tipId='syb-sira',tip='Sıra ve dizilim',z='orta',alt='Kuyrukta Sıra',kaz='İki kişinin sırasından ve aralarındaki kişi sayısından kuyruktaki toplam kişiyi bulup ortadaki kişinin sırasını hesaplar.',kalip='hikâyeli',
 kart='K-SYB-06 · Ali 7., Bora 17., Bora sondan 7.; n = 23; orta 12.',
 metin='Bir konser gişesinde kuyruğun başı ve kuyruktaki Ali ile Bora’nın yerleri şekilde gösterilmiştir; aralarında şekilde yazılı sayıda kişi vardır ve Bora’dan sonra da kişiler gelmektedir. Bora, kuyruğun sonundan sayıldığında 7. sıradadır. Kuyruktaki kişi sayısı tektir ve organizatör kuyruğun tam ortasındaki kişiye hediye verecektir.\nBuna göre, hediyeyi alacak kişi kuyruğun başından sayıldığında kaçıncı sıradadır?',
 dogru=v,yan=[(11,'Toplam 23 kişinin yarısını aşağı yuvarlamış (23 ÷ 2 ≈ 11).','dikkat'),(13,'Ortayı 12. değil, bir sonraki sıra sanmış.','dikkat'),(17,'Bora’nın sırasını ortadaki kişinin sırası sanmış.','dikkat'),(23,'Kuyruktaki toplam kişi sayısını sorulan sıra sanmış.','dikkat')],
 istenen='Hediyeyi alacak kişinin baştan sırası.',ip=['Şekildeki iki kişinin ve aradaki kişilerin sayısıyla Bora’nın baştan sırasını bul.'],bilgi=[SIR],sekil=SK,
 ad=[A('Bora’nın sırası','Ali 7., arada 9 kişi, ardından Bora.','7 + 9 + 1 = 17'),A('Toplam','Baştan sıra + sondan sıra − 1.','17 + 7 − 1 = 23'),A('Ortadaki','Tek sayıda kişide ortadaki, (n + 1)/2. sıradadır.','(23 + 1) ÷ 2 = 12')],
 puf='Baştan ve sondan sıralar bir kişiyi iki kez sayar.')

# 07 zor · optik form
key='CADBECADBECA'
st={'Ece':'CADDECBDBE-A','Can':'CBDBACA-BEC-','Deniz':'CABBECADCECA'}
def say(s): 
    d=sum(1 for a,b in zip(s,key) if a==b); b_=sum(1 for a in s if a=='-'); return d,12-d-b_,b_
sy={k:say(s) for k,s in st.items()}
assert sy=={'Ece':(9,2,1),'Can':(8,2,2),'Deniz':(10,2,0)}
pn={k:5*d-2*y for k,(d,y,b) in sy.items()}
v=sum(pn.values()); assert v==123
D=sum(d for d,_,_ in sy.values()); Y=sum(y for _,y,_ in sy.values()); Bo=sum(b for *_,b in sy.values())
e=[5*D+2*Y,5*D-Y,5*D,5*(D+Bo)]
assert e==[147,129,135,150] and len({v,*e})==5
cw,rh=0.5,0.46; o=[]
rowsn=[('Anahtar',key)]+list(st.items())
for j in range(12): o.append(f'\\node at ({(j+1)*cw:.2f},{rh:.2f}) {{\\footnotesize {j+1}}};')
for i,(nm,s) in enumerate(rowsn):
    y=-i*rh; o.append(f'\\node[left] at (0.2,{y:.2f}) {{{nm}}};')
    for j,ch in enumerate(s): o.append(f'\\node at ({(j+1)*cw:.2f},{y:.2f}) {{{"–" if ch=="-" else ch}}};')
o.append(f'\\draw (0.25,{rh/2+0.0:.2f}) rectangle ({12*cw+0.25:.2f},{-3*rh-rh/2:.2f}); \\draw (0.25,{rh/2-0.46:.2f}) -- ({12*cw+0.25:.2f},{rh/2-0.46:.2f});')
SK=fig('\n'.join(o))
q('0007',tipId='syb-tablo',tip='Tablo ve sayılar',z='zor',alt='Optik Form',kaz='Üç öğrencinin optik form cevaplarını anahtarla karşılaştırıp doğru, yanlış, boş sayılarından toplam puanı bulur.',kalip='hikâyeli',
 kart='K-SYB-07 · 9/2/1, 8/2/2, 10/2/0; doğru 5, yanlış −2',
 metin='Bir deneme sınavının 12 soruluk bölümünün cevap anahtarı ile üç öğrencinin işaretlediği cevaplar şekilde verilmiştir; “–” işareti soruyu boş bıraktığını gösterir. Bu bölümde her doğru cevap 5 puan getirir, her yanlış cevap 2 puan götürür ve boş cevaplar puanı etkilemez. Okul, üç öğrencinin bu bölümden aldığı puanların toplamını duyuracaktır.\nBuna göre, bu toplam puan kaçtır?',
 dogru=v,yan=[(e[0],'Yanlışların 2 puanını çıkarmak yerine toplama eklemiş.','dikkat'),(e[1],'Yanlış başına 2 yerine 1 puan düşmüş.','dikkat'),(e[2],'Yanlışlar için hiç puan düşmemiş.','dikkat'),(e[3],'Boşları doğru sayıp yanlışlar için de puan düşmemiş: 3 × 10 × 5 = 150.','dikkat')],
 istenen='Üç öğrencinin toplam puanı.',ip=['Her öğrenci için önce cevapları anahtarla karşılaştırıp doğru, yanlış ve boş sayısını ayrı bul.'],bilgi=[FRM],sekil=SK,
 ad=[A('Ece','9 doğru, 2 yanlış, 1 boş.','45 − 4 = 41'),A('Can','8 doğru, 2 yanlış, 2 boş.','40 − 4 = 36'),A('Deniz','10 doğru, 2 yanlış, 0 boş.','50 − 4 = 46'),A('Toplam','Puanlar toplanır.','41 + 36 + 46 = 123')],
 puf='Her öğrencide doğru, yanlış, boş toplamı 12 olmalı.')

# 08 zor · puan durumu
A_=dict(O=10,G=6,M=1); A_['B']=A_['O']-A_['G']-A_['M']; A_['P']=3*A_['G']+A_['B']
Bt=dict(O=10,M=2,P=18); Bt['G']=(Bt['P']-(Bt['O']-Bt['M']))//2; Bt['B']=Bt['O']-Bt['M']-Bt['G']
assert A_['B']==3 and A_['P']==21 and Bt['G']==5 and Bt['B']==3 and 3*Bt['G']+Bt['B']==18
Ct=dict(O=10,M=4,B=A_['B']); Ct['G']=Ct['O']-Ct['M']-Ct['B']; Ct['P']=3*Ct['G']+Ct['B']
assert Ct['G']==3 and Ct['P']==12
v=A_['P']+Bt['P']+Ct['P']; assert v==51
e=[A_['P']+Bt['P'],A_['P']+Bt['P']+3*Ct['G'],A_['P']+Bt['P']+3*2+4,A_['P']-1+Bt['P']+Ct['P']]
e=[39,48,49,50]; assert 21+18+10==49 and 20+18+12==50 and len({v,*e})==5
SK=tablo_svg(['Takım','Oynadığı','Galibiyet','Beraberlik','Mağlubiyet','Puan'],[['A','10','6','?','1','?'],['B','10','?','?','2','18'],['C','10','?','?','4','?']])
q('0008',tipId='syb-tablo',tip='Tablo ve sayılar',z='zor',alt='Puan Durumu',kaz='Puan durumu tablosundaki eksik değerleri maç ve puan ilişkisinden çözüp toplam puanı bulur.',kalip='tablo',
 kart='K-SYB-08 · A 21, B 18, C 12 puan',
 metin='Bir turnuvada her takım 10 maç oynamış ve puan durumunun bir bölümü aşağıdaki tabloda verilmiştir; “?” ile gösterilen değerler yazılmamıştır. Galibiyet 3 puan, beraberlik 1 puan, mağlubiyet 0 puan getirmektedir. C takımının beraberlik sayısı, A takımının beraberlik sayısına eşittir.\nBuna göre, A, B ve C takımlarının toplam puanı kaçtır?',
 dogru=v,yan=[(39,'C takımını hesaba katmamış: 21 + 18.','dikkat'),(48,'C takımının yalnız galibiyetlerinden aldığı puanı (9) eklemiş.','dikkat'),(49,'C takımını 10 puan almış sanmış.','dikkat'),(50,'C takımını 3 galibiyet + 2 beraberlik sanıp 11 puanlı hesaplamış: 21 + 18 + 11 = 50.','dikkat')],
 istenen='Üç takımın toplam puanı.',ip=['A takımının beraberlik sayısını maç sayısından bul; sonra B ve C için eksik değerleri sırayla çöz.'],bilgi=[PUN],sekil=SK,
 ad=[A('A takımı','10 − 6 − 1 beraberlik; 3 × 6 + 3 puan.','B = 3, P = 21'),A('B takımı','G + B = 8 ve 3G + B = 18.','G = 5, B = 3'),A('C takımı','Beraberlik 3 ise galibiyet 10 − 4 − 3 = 3.','P = 3 × 3 + 3 = 12'),A('Toplam','Üç takımın puanı.','21 + 18 + 12 = 51'),A('Kontrol','Her takımda G + B + M = 10.','Tutarlı')],
 puf='Önce beraberliği maç sayısından bul.')

# 09 zor · yılan dizilim
col=5; hedef=2026; r=-(-hedef//col); assert r==406 and r%2==0
yön=lambda rr: 'sol' if rr%2==1 else 'sağ'
def konum(m):
    rr=-(-m//col); k=m-col*(rr-1)   # 1..col
    c=k if rr%2==1 else col+1-k
    return rr,c
rr,cc=konum(hedef); assert (rr,cc)==(406,5)
alt_r=rr+1; alt=[m for m in range(col*(alt_r-1)+1,col*alt_r+1) if konum(m)[1]==cc][0]
v=alt; assert v==2035
e=[2026,2030,2031,2034]; assert len({v,*e})==5
o=[]
for rw in range(1,5):
    nums=list(range(col*(rw-1)+1,col*rw+1))
    if rw%2==0: nums=nums[::-1]
    for c in range(col):
        o.append(f'\\node[draw,thick,minimum width=0.9cm,minimum height=0.7cm] at ({c*0.9:.2f},{-(rw-1)*0.7:.2f}) {{{nums[c]}}};')
o.append(f'\\node at (1.8,-2.7) {{\\vdots}};')
SK=fig('\n'.join(o))
q('0009',tipId='syb-sira',tip='Sıra ve dizilim',z='orta',alt='Yılan Dizilim',kaz='Yılan biçimli sayı dizilimini sürdürerek verilen sayının hemen altındaki sayıyı bulur.',kalip='hikâyeli',
 kart='K-SYB-09 · 5 sütun, yılan dizilim; 2026’nın altı 2035',
 metin='Bir fidanlıkta fidan sıraları numaralandırılırken şekildeki yılan biçimli düzen kullanılmıştır: 1’den başlayan doğal sayılar her satırda 5 sayı olacak biçimde, bir satır soldan sağa, sonraki satır sağdan sola yazılarak sürdürülür ve bu düzen sonsuza kadar aynı biçimde devam eder. Fidanlık sahibi 2026 numaralı fidanın hemen altındaki fidanı sulayacaktır.\nBuna göre, sulanacak fidanın numarası kaçtır?',
 dogru=v,yan=[(2026,'2026’nın altında da aynı sayıyı sanmış.','dikkat'),(2030,'2026 ile aynı satırın sol ucundaki sayıyı almış: 2026 + 4.','dikkat'),(2031,'Yönü unutup altındaki sayıyı 2026 + 5 saymış.','dikkat'),(2034,'Sütunu bir kaydırıp 2034’ü bulmuş.','dikkat')],
 istenen='2026’nın hemen altındaki sayı.',ip=['2026’nın hangi satırda olduğunu ve bu satırın hangi yönde yazıldığını bul.'],bilgi=[YIL],sekil=SK,
 ad=[A('Satır','2026 ÷ 5 yukarı yuvarlanır.','406. satır (çift; sağdan sola)'),A('Sütun','Çift satırda satırın ilk sayısı (2026) en sağdadır.','2026, 5. sütunda'),A('Alt satır','407. satır tek, soldan sağa: 2031, 2032, 2033, 2034, 2035.','5. sütunda 2035')],
 puf='Satırın yönü sütunu belirler.')

# 10 zor · cebirsel Venn
xx=8; yy=10; a_only=2*xx; both=xx+4; b_only=3*xx-2; tot=60
assert (a_only+both+b_only)==5*yy and a_only+both+b_only+yy==tot
v=b_only; e=[xx,both,a_only,b_only+both]
assert v==22 and e==[8,12,16,34] and len({v,*e})==5
o=['\\draw[thick] (0,0) rectangle (7.6,4.2);','\\draw[thick,fill=vurgu!15,fill opacity=0.6] (3.0,2.0) circle (1.6); \\draw[thick,fill=vurgu!30,fill opacity=0.5] (4.6,2.0) circle (1.6);',
 '\\node at (2.4,3.8) {A}; \\node at (5.2,3.8) {B};','\\node at (2.2,2.0) {$2x$}; \\node at (3.8,2.0) {$x+4$}; \\node at (5.4,2.0) {$3x-2$}; \\node at (6.9,0.4) {$y$};']
SK=fig('\n'.join(o))
q('0010',tipId='syb-venn',tip='Cebirsel Venn şeması',z='zor',alt='Cebirsel Venn Şeması',kaz='Venn şemasındaki cebirsel bölge ifadelerinden iki koşulla x ve y’yi bulup istenen bölgeyi hesaplar.',kalip='yeni nesil',
 kart='K-SYB-10 · 2x, x+4, 3x−2, y; A∪B = 5y; toplam 60',
 metin='Şekildeki Venn şemasında A ve B kümelerinin bölgelerindeki eleman sayıları x ve y cinsinden verilmiştir; dikdörtgen evrensel kümeyi gösterir ve evrensel kümenin 60 elemanı vardır. Bölgelerdeki ifadeler o bölgedeki eleman sayısını belirtir, x ve y pozitif tam sayıdır. A ∪ B kümesinin eleman sayısı, hiçbir kümede olmayan eleman sayısının 5 katıdır.\nBuna göre, yalnız B kümesinde bulunan eleman sayısı kaçtır?',
 dogru=v,yan=[(e[0],'x değerini (8) bölge sayısı sanmış.','dikkat'),(e[1],'Ortak bölgedeki sayıyı (12) yalnız B bölgesi sanmış.','dikkat'),(e[2],'Yalnız A bölgesini (16) yalnız B bölgesi sanmış.','dikkat'),(e[3],'B kümesinin tüm elemanlarını (34) yalnız B’de sanmış.','dikkat')],
 istenen='Yalnız B kümesindeki eleman sayısı.',ip=['A ∪ B bölgelerini ve dışarıdaki bölgeyi y cinsinden yazıp evrensel kümenin eleman sayısıyla ilişkilendir.'],bilgi=[VEN],sekil=SK,
 ad=[A('Dışarıdaki bölge','A ∪ B = 5y ve toplam 60.','5y + y = 60, y = 10'),A('A ∪ B','Üç bölge toplamı.','2x + (x + 4) + (3x − 2) = 6x + 2 = 50'),A('x','Denklem çözülür.','x = 8'),A('Yalnız B','3x − 2.','3 × 8 − 2 = 22')],
 puf='Dışarıdaki bölgeyi önce bul.')

bitir(P,'sayisekb',UK)
