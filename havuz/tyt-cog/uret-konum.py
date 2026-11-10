import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_c import *
P=Parti('konum','Coğrafi Konum','cog|Coğrafi Konum',ders='TYT Coğrafya',idon='tytcog')
KY='ÖSYM 2018–2026 TYT Coğrafya (konum, koordinat) · MEB 9. sınıf'
kart('K-CGKN-01','Matematik ve özel konum','Matematik konum enlem–boylam ile, özel konum çevredeki denizler, kıtalar ve yollarla ilgilidir; sonuçları ayrı ayrı düşünülür.','Güneş ışınları ve mevsim sonuçlarını özel konuma yazmak.','kolay','düz',2,'cg-konum-ozel','Matematik ve özel konum ayrımı',KY)
kart('K-CGKN-02','Türkiye’nin matematik konumu','Uç paralel ve meridyenlerden uzaklık (1° enlem = 111 km) ve yerel saat farkı (1° boylam = 4 dakika) çıkarılır.','Enlem farkını boylam farkıyla karıştırmak; güneş ışınlarının dik geleceğini sanmak.','orta','öncüllü',3,'cg-konum-turkiye','Türkiye’nin matematik konumu yorumu',KY)
kart('K-CGKN-03','Yerel saat','Boylam farkı × 4 dakika = saat farkı; doğuya gidildikçe saat ileridir.','Ayrı yarımkürelerdeki boylamları çıkarmak; yönü ters almak.','orta','düz',3,'cg-konum-saat','Yerel saat hesabı',KY)
kart('K-CGKN-04','Saatten boylam bulma','Saat farkı dakikaya çevrilir, 4’e bölünüp boylam farkı bulunur; yön saatten çıkarılır.','Saat farkını ondalık yazmak (3 saat 20 dk ≠ 3,2 saat); batı–doğu yönünü karıştırmak.','zor','düz',4,'cg-konum-boylam','Yerel saatten boylam bulma',KY)
ENL=B('Yerel saat','Dünya 24 saatte 360° döner: 1 saat = 15°, 1° = 4 dakika. Doğuda saat ileridir. Örnek: 15° doğuya gidince saat 1 saat ileri gider')
MAT=B('Matematik ve özel konum','Matematik konum: enlem ve boylamla belirlenen yer (mevsimler, sıcaklık, yerel saat). Özel konum: çevredeki deniz, kara, yarımada, boğaz ve geçit gibi özellikler (jeopolitik, ulaşım, ticaret). İki paralel arası 1° = 111 km')
# 0001
q1=Q(P,'0001','K-CGKN-01','kolay','Matematik konum ile özel konumun sonuçlarını ayırt eder.','düz',2,
 'Aşağıdakilerden hangisi Türkiye’nin özel konumunun bir sonucudur?',
 [('Dört mevsimin belirgin yaşanması','mat','Mevsimler enleme bağlıdır; bu, matematik konumun sonucudur.','bilgi'),
  ('Güneş ışınlarının yıl boyunca Türkiye’ye dik açıyla gelmemesi','mat','Işınların geliş açısı enleme bağlıdır; matematik konum sonucudur.','bilgi'),
  ('Doğu ile batı uçları arasında yerel saat farkı bulunması','mat','Yerel saat farkı boylamdan doğar; matematik konum sonucudur.','bilgi'),
  ('Asya ile Avrupa arasındaki kara ve deniz yollarının kavşağında yer alması','ozel',None,None),
  ('Ekvator’a yakın ülkelere göre yıllık sıcaklık ortalamasının daha düşük olması','mat','Sıcaklık enlemle değişir; matematik konum sonucudur.','bilgi')],
 lambda e:e=='ozel','Özel konumun sonucu olan durum.',
 'Önce her şıkkın enleme ve boylama mı, yoksa çevredeki kara, deniz ve yollara mı dayandığına bak.',[MAT],
 [A('Ayrımı hatırla','Enlem ve boylamdan doğan durumlar matematik konumun sonucudur. Çevredeki kıtalar, denizler ve yollar özel konumu belirler.','matematik: enlem–boylam · özel: çevre ve yollar'),
  A('Şıkları sına','Mevsimler, ışınların geliş açısı, sıcaklık ve yerel saat farkı enlem ve boylamla ilgilidir.','mevsim, ışın açısı, sıcaklık, saat: matematik konum'),
  A('Sonuç','Asya ile Avrupa arasındaki yolların kavşağında olmak çevreye bağlı bir özelliktir.','Yolların kavşağı: özel konum')],
 'Enlem ve boylamdan doğan sonuçlar matematik, çevreden doğan sonuçlar özel konuma aittir.','yeni şık kümesi',harf='D')
# 0002
dB,dK=36,42; bB,bD=26,45
assert (bD-bB)*4==76 and (dK-dB)*111==666 and 23.45<dB
tr=dict(I=False,II=True,III=False)
dg={k for k,v in tr.items() if v}
q2=Q(P,'0002','K-CGKN-02','orta','Uç noktaların enlem ve boylamından uzaklık ve yerel saat farkını yorumlar.','öncüllü',3,
 'Türkiye, 36° ile 42° kuzey paralelleri ve 26° ile 45° doğu meridyenleri arasında yer alır. (1° enlem = 111 km; Yengeç Dönencesi 23° 27′ kuzeydedir.)\nBuna göre\nI. Doğu ve batı uçları arasındaki yerel saat farkı 19 dakikadır.\nII. Güney ve kuzey uç paralelleri arasındaki uzaklık 666 km’dir.\nIII. Yılın bazı günlerinde Güneş ışınları öğle vakti Türkiye’nin güneyine dik açıyla gelir.\nifadelerinden hangileri doğrudur?',
 onc_opts(dg,[{'I'},{'II'},{'I','II'},{'I','III'},{'II','III'}],{'Yalnız I':('Boylam farkını (19°) doğrudan dakika sanmak; 1° = 4 dakikadır.','islem'),'I ve II':('I’deki 19° farkını dakikaya çevirmeyi atlamak.','islem'),'I ve III':('Türkiye’nin Yengeç Dönencesi’nin çok kuzeyinde olduğunu unutmak.','bilgi'),'II ve III':('Işınların dönencelerin dışına dik gelmeyeceğini bilmemek.','bilgi')}),
 lambda e:e==frozenset(dg),'Doğru ifadeler.',
 'Her ifadede uç meridyenler ya da paraleller arasındaki farkı bul, uygun çarpanla çarp.',[ENL,MAT],
 [A('Saat farkı','Boylam farkı 45 − 26 = 19°; 1° = 4 dakikadır.','19 × 4 = 76 dakika · I yanlış'),
  A('Uzaklık','Enlem farkı 42 − 36 = 6°; 1° = 111 km.','6 × 111 = 666 km · II doğru'),
  A('Güneş ışınları','Işınlar en fazla Yengeç Dönencesi’ne (23° 27′ K) dik gelir; Türkiye 36° K’nin kuzeyindedir.','III yanlış · yalnız II')],
 'Boylam farkı × 4 dakika saat farkını, enlem farkı × 111 km uzaklığı verir.','Türkiye’nin uç koordinatları verildi',harf='B')
# 0003
fark=(40+20); assert fark*4==240
sat=14*60+fark*4; assert sat==18*60
def tm(x): return f'{x//60}.{x%60:02d}'
vals={'dogru':tm(sat),'yon':tm(14*60-fark*4),'cik':tm(14*60+(40-20)*4),'otuz':tm(14*60+(fark//30)*60),'yon30':tm(14*60-(fark//30)*60)}
assert vals=={'dogru':'18.00','yon':'10.00','cik':'15.20','otuz':'16.00','yon30':'12.00'},vals
key=lambda s:float(s)
q3=Q(P,'0003','K-CGKN-03','orta','İki boylam arasındaki yerel saat farkını hesaplar.','düz',3,
 'K kenti 20° batı, L kenti 40° doğu boylamındadır.\nK kentinde yerel saat 14.00 iken L kentinde yerel saat kaçtır?',
 [('18.00','d',None,None),('10.00','y','Doğuya gidildiğinde saatin geri gideceğini sanmak; doğuda saat ileridir.','bilgi'),
  ('15.20','y','Farklı yarımkürelerdeki boylamları çıkarmak (40 − 20 = 20°); toplamak gerekir.','islem'),
  ('16.00','y','60° farkı 30° = 1 saat sanıp 2 saat bulmak; 15° = 1 saattir.','bilgi'),
  ('12.00','y','Hem yönü ters almak hem 30° = 1 saat saymak.','bilgi')],
 lambda e:e=='d','L kentindeki yerel saat.',
 'K batıda, L doğuda olduğundan boylamlar toplanır; 1° = 4 dakika.',[ENL],
 [A('Boylam farkı','Boylamlar farklı yarımkürelerde olduğu için toplanır.','20 + 40 = 60°'),
  A('Saat farkı','1° = 4 dakika.','60 × 4 = 240 dakika = 4 saat'),
  A('Yönü uygula','L, K’nin doğusundadır; saat ileridir.','14.00 + 4 = 18.00')],
 'Zıt yarımkürelerde boylamlar toplanır, aynı yarımkürede çıkarılır.','K ve L kentleri, farklı yarımküreler',sirala=key,harf='E')
# 0004
fark_dk=3*60+20; assert fark_dk//4==50 and 30-50==-20
ana=30
assert ana-fark_dk//4==-20 and ana+fark_dk//4==80 and round(3.2*15)==48 and ana-48==-18
def bk(s): return -int(s[:-3]) if s.endswith('B') else int(s[:-3])
q4=Q(P,'0004','K-CGKN-04','zor','Yerel saat farkından bir yerin boylamını bulur.','düz',4,
 'A kenti 30° doğu boylamındadır. A kentinde yerel saat 09.00 iken B kentinde yerel saat 05.40’tır.\nBuna göre B kenti hangi boylamdadır?',
 [('20° B','d',None,None),('20° D','y','Boylam değerini 20 bulup batı–doğu yönünü saatten çıkarmamak.','dikkat'),
  ('50° B','y','Yalnız boylam farkını (50°) yazıp A’nın boylamını hesaba katmamak.','dikkat'),
  ('80° D','y','Saati geride olan kenti A’nın doğusuna koymak.','bilgi'),
  ('18° B','y','3 saat 20 dakikayı 3,2 saat sanıp 48° bulmak.','islem')],
 lambda e:e=='d','B kentinin boylamı.',
 'Saati geride olan yer batıdadır; saat farkını dakikaya çevirip 4’e böl.',[ENL],
 [A('Saat farkı','09.00 − 05.40 = 3 saat 20 dakika.','3 × 60 + 20 = 200 dakika'),
  A('Boylam farkı','1° = 4 dakika.','200 ÷ 4 = 50°'),
  A('Yönü bul','B’nin saati geride olduğundan B, A’nın batısındadır.','30° − 50° = −20° → 20° B')],
 'Önce yönü saatten çıkar, sonra dakikayı 4’e bölerek boylam farkını bul.','saatten boylama dönüş',sirala=bk,harf='B')
bitir(P,'konum','cog|Coğrafi Konum','Coğrafi Konum')
