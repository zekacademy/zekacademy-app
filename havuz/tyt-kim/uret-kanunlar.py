import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
H.KONU='Kimyanın Temel Kanunları'
P=Parti('kanunlar','Kimyanın Temel Kanunları','kim|Kimyanın Temel Kanunları',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (temel kanunlar) · MEB 9–10. sınıf'
kart('K-KKN-01','Kütlenin korunumu','Kapalı kapta tepkimeye girenlerin toplam kütlesi ürünlerin toplam kütlesine eşittir.','Harcanan maddeyi yanlış çıkarmak; kütleleri mol sanmak.','kolay','düz',2,'kim-kn-korunum','Kütlenin korunumu',KY)
kart('K-KKN-02','Sabit oranlar','Bir bileşikteki elementlerin kütlece oranı sabittir; fazla madde artar.','Toplam kütleyi ürün kütlesi sanmak; sınırlayıcıyı bulmamak.','orta','düz',3,'kim-kn-sabit','Sabit oranlar ve artan madde',KY)
kart('K-KKN-03','Katlı oranlar','Aynı iki elementten oluşan bileşiklerde, sabit kütleli birinin yanındaki öteki elementin kütleleri küçük tam sayılı oran verir.','Kütleleri sabit bir element kütlesine eşitlemeden kıyaslamak.','orta','düz',3,'kim-kn-katli','Katlı oranlar ve formül',KY)
kart('K-KKN-04','Sabit oranlar','İlk deneyden birleşme oranı çıkarılır; ikinci deneyde sınırlayıcı belirlenip ürün kütlesi bulunur.','Artan maddeyi karıştırmak; ikinci deneye 1. deneyin sonucunu yazmak.','zor','düz',4,'kim-kn-deney','İki deneyden oran bulma',KY)
# 0001
mMg,mMgO=12,20; mO=mMgO-mMg; assert mO==8
mk(P,'0001',tipId='kim-kn-korunum',tip='Kütlenin korunumu',z='kolay',alt='Kütlenin Korunumu',kaz='Kütlenin korunumu kanununu kullanarak harcanan madde miktarını bulur.',kalip='düz',adim=2,
 kart='K-KKN-01 (kütlenin korunumu) · Mg yanması, harcanan O₂',
 metin='Mg + O₂ → MgO tepkimesinde 12 g Mg, yeterli miktarda O₂ ile tamamen tepkimeye girerek 20 g MgO oluşturuyor.\nBuna göre tepkimede kaç g O₂ harcanmıştır?',
 dogru=8,yan=[(12,'Harcanan O₂ yerine Mg’nin kütlesini yazmış.','dikkat'),(16,'Oksijenin mol kütlesini (16) harcanan kütle sanmış.','bilgi'),(20,'Oluşan MgO kütlesini harcanan O₂ sanmış.','dikkat'),(32,'Girenlerle ürünün kütlesini toplamış (12 + 20).','islem')],
 istenen='Tepkimede harcanan O₂ kütlesi (g).',
 ip=['Tepkimeye girenlerin toplam kütlesi ile ürünün kütlesi arasındaki ilişkiyi düşün.'],
 bilgi=[B('Kütlenin korunumu','kapalı kapta tepkimeden önceki toplam kütle, tepkimeden sonraki toplam kütleye eşittir. Örnek: 4 g A + 6 g B → 10 g ürün')],
 ad=[A('Eşitliği yaz','Girenlerin toplam kütlesi ürünün kütlesine eşit olmalıdır.','m(Mg) + m(O₂) = m(MgO)'),A('Değerleri yerleştir','Bilinen kütleler eşitlikte yerine yazılır.','12 + m(O₂) = 20'),A('Hesapla','Bilinmeyen kütle yalnız bırakılır.','m(O₂) = 20 − 12 = 8 g')],
 puf='Tepkimede bir maddenin kütlesi bilinmiyorsa girenlerin toplamını ürünlerin toplamına eşitle.')
# 0002
rMg,rO=3,2; Mg0,O0=24,24; needO=Fr(Mg0*rO,rMg); needMg=Fr(O0*rMg,rO)
assert needO==16 and needMg==36 and needO<=O0 and needMg>Mg0
prod=Mg0+needO; assert prod==40 and Mg0+O0==48 and needMg+O0==60
mk(P,'0002',tipId='kim-kn-sabit',tip='Sabit oranlar ve artan madde',z='orta',alt='Sabit Oranlar Kanunu',kaz='Sabit oranlar kanununa göre sınırlayıcı maddeyi bulup oluşan bileşik kütlesini hesaplar.',kalip='düz',adim=3,
 kart='K-KKN-02 (sabit oranlar) · Mg ve O oranı 3/2, artan oksijen',
 metin='MgO bileşiğinde Mg ile O’nun kütlece birleşme oranı mMg / mO = 3/2’dir.\n24 g Mg ile 24 g oksijen tepkimeye sokuluyor ve MgO oluşuyor.\nBuna göre tepkime sonunda kaç g MgO oluşur?',
 dogru=40,yan=[(24,'Yalnız Mg’nin kütlesini ürün kütlesi sanmış.','dikkat'),(36,'24 g oksijen için gereken Mg kütlesini (36 g) ürün sanmış.','dikkat'),(48,'Girenlerin toplam kütlesini ürün sanmış; artan oksijeni görmemiş.','bilgi'),(60,'Mg’nin yeteceğini varsaymış; oksijenin tamamı harcanmış sanmış.','bilgi')],
 istenen='Oluşan MgO kütlesi (g).',
 ip=['24 g Mg ile birleşmesi gereken oksijen kütlesini 3/2 oranından bul; hangisinin yettiğine bak.'],
 bilgi=[B('Sabit oranlar kanunu','bir bileşikte elementlerin kütlece oranı sabittir; fazla gelen madde tepkimeye girmeden artar. Örnek: oran 3/2 ise 6 g Mg yalnız 4 g oksijenle birleşir')],
 ad=[A('Gereken oksijen','24 g Mg için oran korunur.','mO = 24 × 2 ÷ 3 = 16 g'),A('Artan madde','Oksijenden 24 g var, 16 g yeterli; Mg tamamen biter.','24 − 16 = 8 g oksijen artar'),A('Oluşan bileşik','Birleşen Mg ve oksijen kütleleri toplanır.','24 + 16 = 40 g MgO')],
 puf='Sabit oranda önce oranı koruyan miktarı bul; fazla gelen madde artar, ürün kütlesi birleşenlerin toplamıdır.')
# 0003
a1=(6,8); a2=(9,24)
r1=Fr(a1[1],a1[0]); r2=Fr(a2[1],a2[0]); katli=r2/r1; assert katli==2
ind=2*katli; assert ind==4
s3=['XY₃','XY₄','XY₅','XY₆','XY₈']
mk(P,'0003',tipId='kim-kn-katli',tip='Katlı oranlar ve formül',z='orta',alt='Katlı Oranlar Kanunu',kaz='Katlı oranlar kanununu kullanarak ikinci bileşiğin formülünü bulur.',kalip='düz',adim=3,
 kart='K-KKN-03 (katlı oranlar) · X ve Y’den iki bileşik, formül bulma',
 metin='X ve Y elementlerinden oluşan iki farklı bileşiğin kütlece bileşimi aşağıda verilmiştir.\nI. bileşik: 6 g X ve 8 g Y\nII. bileşik: 9 g X ve 24 g Y\nI. bileşiğin formülü XY₂ olduğuna göre II. bileşiğin formülü aşağıdakilerden hangisidir?',
 dogru='XY₄',sira=s3,
 yan=[('XY₃','Y kütleleri oranını (24 ÷ 8 = 3) doğrudan atom sayısı sanmış.','islem'),('XY₅','I. bileşikteki indise (2) Y kütleleri oranını (3) eklemiş.','islem'),('XY₆','Y kütleleri oranını (3) I. bileşikteki indisle (2) çarpmış.','islem'),('XY₈','Katlı oranı iki kez uygulamış (2 × 2 × 2).','islem')],
 istenen='II. bileşiğin formülü.',
 ip=['İki bileşikte X kütlesini eşitle; sonra bu kütleyle birleşen Y kütlelerini kıyasla.'],
 bilgi=[B('Katlı oranlar kanunu','aynı iki elementten oluşan bileşiklerde, birinin sabit kütlesiyle birleşen öteki elementin kütleleri arasında küçük tam sayılı oran vardır. Örnek: CO ve CO₂’de 12 g C ile 16 g ve 32 g O birleşir (oran 1/2)')],
 ad=[A('X’i eşitle','İki bileşikte 18 g X olacak şekilde birinci bileşiği 3, ikinciyi 2 ile genişlet.','I: 18 g X + 24 g Y · II: 18 g X + 48 g Y'),A('Y oranı','Aynı X kütlesiyle birleşen Y kütleleri oranlanır.','48 ÷ 24 = 2'),A('Formül','Y atom sayısı da 2 katına çıkar.','XY₂ → XY₄')],
 puf='Katlı oranda önce sabit element kütlesini eşitle, sonra öteki elementin kütle oranını indislere uygula.')
# 0004
e1=(12,20,4)  # 12 g A, 20 g B girdi, 4 g B artti
rA,rB=12,e1[1]-e1[2]; assert rB==16 and Fr(rA,rB)==Fr(3,4) and rA+rB==28
A2,B2=15,30; needB=Fr(A2*rB,rA); assert needB==20 and needB<=B2
prod=A2+needB; assert prod==35 and A2+B2==45 and rA+rB==28 and Fr(B2*rA,rB)+B2==Fr(105,2)
mk(P,'0004',tipId='kim-kn-deney',tip='İki deneyden oran bulma',z='zor',alt='Sabit Oranlar Kanunu',kaz='İlk deneyden birleşme oranını çıkarıp ikinci deneyde oluşan bileşik kütlesini bulur.',kalip='düz',adim=4,
 kart='K-KKN-04 (sabit oranlar) · iki deney, birinci deneyden oran çıkarma',
 metin='A ve B elementleri yalnız bir bileşik oluşturmaktadır.\n1. deney: 12 g A ile 20 g B tepkimeye giriyor ve tepkime sonunda 4 g B artıyor.\n2. deney: 15 g A ile 30 g B tepkimeye giriyor.\nBuna göre 2. deneyde kaç g bileşik oluşur?',
 dogru=35,yan=[(20,'Oluşan bileşik yerine 2. deneyde birleşen B kütlesini yazmış.','dikkat'),(28,'1. deneyde oluşan bileşik kütlesini 2. deneyin sonucu sanmış.','dikkat'),(45,'Girenlerin toplamını yazmış; 2. deneyde B’nin 10 g arttığını görmemiş.','bilgi'),(Fr(105,2),'B’nin tamamen bittiğini varsaymış; gereken A kütlesinin 15 g’ı aştığını kontrol etmemiş.','bilgi')],
 istenen='2. deneyde oluşan bileşik kütlesi (g).',
 ip=['1. deneyde artan B’yi çıkararak A ile gerçekten birleşen B kütlesini bul; oranı 2. deneye uygula.'],
 bilgi=[B('Sabit oranlar kanunu','bir bileşikte elementlerin kütlece oranı sabittir; artan madde tepkimeye girmemiştir. Örnek: oran 1/2 ise 3 g X, 6 g Y ile birleşir')],
 ad=[A('Birleşen miktarlar','1. deneyde B’den 4 g arttığı için 4 g B tepkimeye girmemiştir.','B: 20 − 4 = 16 g · mA/mB = 12/16 = 3/4'),A('2. deneyde gereken B','15 g A, aynı oranla birleşecek B kütlesini belirler.','mB = 15 × 4 ÷ 3 = 20 g'),A('Sınırlayıcıyı bul','30 g B var, 20 g yeterli; A tamamen biter, 10 g B artar.','30 − 20 = 10 g B artar'),A('Bileşik kütlesi','Birleşen A ve B toplanır.','15 + 20 = 35 g')],
 puf='Birinci deneyden artanı çıkararak gerçek birleşme oranını bul; ikinci deneyde sınırlayıcıyı bu orana göre belirle.')
bitir(P,'kanunlar','kim|Kimyanın Temel Kanunları')
