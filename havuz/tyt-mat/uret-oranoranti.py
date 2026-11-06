"""Oran Orantı · iskelet havuz (8 ana + 8 kardeş). Her cevap ve ara sonuç kodla doğrulanır."""
import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
TT=lambda **k:k
KONU='Oran Orantı'; UK='mat|Oran Orantı'
P=Parti('oranoranti',KONU,UK)

KARTLAR=[
 dict(id='K-ORN-01',konu=KONU,alt='Doğru orantı',fikir='Birlikte artan iki çokluk (miktar–tutar, yol–yakıt) verilir; birim değer bulunup istenen miktara geçilir, gerekirse iki orantı art arda uygulanır.',
      tuzak='Doğru orantıyı ters kurmak; artışı mevcut miktara eklemek; birim dönüşümünde virgül hatası.',zorluk='kolay-orta',kalip='hikâyeli',adim=2,tipId='oo-dogru',tip='Doğru orantı ve birim değer',
      kaynak='ÖSYM YKS çıkmış (kitap s78 #96, büyütme oranı) · Bilgi Sarmal s188 #10, s189 #4'),
 dict(id='K-ORN-02',konu=KONU,alt='Ters orantı',fikir='Biri artarken diğeri azalan iki çokluk (tüketici sayısı–gün, birim fiyat–adet) verilir; çarpım sabit tutulur.',
      tuzak='Ters orantıyı doğru orantı gibi kurmak; artış oranı kadar doğrudan azaltmak; azalma miktarını sonuç sanmak.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='oo-ters',tip='Ters orantı',
      kaynak='Bilgi Sarmal s188 #14–15, s189 #6 · 345 SB oran-orantı testleri'),
 dict(id='K-ORN-03',konu=KONU,alt='Oranları birleştirme',fikir='Ortak bir terim içeren iki oran verilir (a/b ve b/c); ortak terim eşitlenip üçlü oran kurulur, toplam ya da bir parça verilir.',
      tuzak='Ortak terimi eşitlemeden oranları yan yana yazmak; istenen parçayı karıştırmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='oo-bilesik',tip='Ortak terimle oranları birleştirme',
      kaynak='Bilgi Sarmal ve 345 SB üçlü oran soruları · ÖSYM YKS çıkmış (kitap s120 #140, 3–4–6 ile orantılı)'),
 dict(id='K-ORN-04',konu=KONU,alt='Orantılı paylaştırma',fikir='Bir çokluk sayılarla doğru ya da ters orantılı paylaştırılır; bir pay, iki payın farkı ya da paylaştırma koşulundaki değişim verilir.',
      tuzak='Ters orantılıyı doğru orantılı gibi paylaştırmak; bir parçanın değeri ile pay sayısını karıştırmak; değişimden sonra parça sayısını güncellememek.',zorluk='orta-zor',kalip='hikâyeli',adim=4,tipId='oo-paylastirma',tip='Doğru ve ters orantılı paylaştırma',
      kaynak='ÖSYM YKS çıkmış (kitap s120 #140, kalemliklere orantılı paylaştırma) · Bilgi Sarmal s188 #10, s189 #8'),
 dict(id='K-ORN-05',konu=KONU,alt='Oran değişimi',fikir='İki grubun oranı verilir; gruplardan birine ya da ikisine ekleme/çıkarma yapılınca yeni oran verilir. Gruplar k ile yazılıp yeni oran denklemi kurulur.',
      tuzak='Değişimi yalnızca bir gruba uygulamak; ilk ve son durumu karıştırmak; oran 2’yi “yarı yarıya” sanmak.',zorluk='orta-zor',kalip='hikâyeli',adim=4,tipId='oo-oran-degisim',tip='Ekleme ve çıkarmayla oran değişimi',
      kaynak='ÖSYM YKS çıkmış (kitap s138 #161, gidilen ve gidilmeyen müzeler) · Bilgi Sarmal s231 #7 · 345 Deneme'),
]
TIPLER=[dict(tipId=k['tipId'],ad=k['tip'],kartlar=[k['id']],uygulamaKonu=UK) for k in KARTLAR]
json.dump(dict(konu=KONU,surum=1,kartlar=KARTLAR,tipler=TIPLER),open(os.path.join(H,'..','kartlar','oranoranti.json'),'w'),ensure_ascii=False,indent=1)
T={k['tipId']:k['tip'] for k in KARTLAR}

ORAN=B('Oranı k ile yazmak','a/b = 2/3 ise a = 2k ve b = 3k yazılır. Örnek: oranı 2/3 olan iki grup toplam 30 kişi ise 5k = 30, k = 6 ⇒ 12 ve 18')
DOGRU=B('Doğru orantı','biri kaç katına çıkarsa diğeri de o kadar katına çıkar; bölümleri sabittir. Örnek: 2 kg 60 TL ise 6 kg 180 TL')
TERS=B('Ters orantı','biri kaç katına çıkarsa diğeri o kadar kata bölünür; çarpımları sabittir. Örnek: 4 kişiye 6 gün yeten yemek 8 kişiye 3 gün yeter')
ORTAK=B('Ortak terimi eşitleme','a/b = 2/3 ve b/c = 4/5 ise b iki oranda eşitlenir: 2/3 = 8/12, 4/5 = 12/15 ⇒ a : b : c = 8 : 12 : 15')
PAYL=B('Orantılı paylaştırma','2, 3 ve 5 ile doğru orantılı paylar 2k, 3k, 5k’dir. 2, 3 ve 6 ile ters orantılı paylar k/2, k/3, k/6’dır; paydalar eşitlenince 3 : 2 : 1 olur')

# ===== 0001 doğru KOLAY
u=Fr(450,6)*10; assert u==750 and Fr(450,6)==75 and Fr(450*6,10)==270 and 450+750==1200 and 450*10==4500
P.R('0001','oo-dogru',T['oo-dogru'],'kolay','Tarif ölçekleme','Kişi sayısıyla doğru orantılı malzeme miktarını birim değer üzerinden bulur.','hikâyeli',2,
 'K-ORN-01 (doğru orantı) · yeni kurgu (mantı tarifi), kişi sayısı artıyor',
 'Bir mantı tarifinde 6 kişilik hamur için 450 gram un kullanılmaktadır.\nAynı tarifle, kişi başına aynı miktarda un kullanılarak 10 kişilik mantı hamuru hazırlanacaktır.\nBuna göre bu hamur için kaç gram un gerekir?',
 ['75','270','750','1200','4500'],'C','10 kişilik hamur için gereken un.',
 ['Kişi sayısı artınca un artar mı, azalır mı?','Bir kişilik hamura kaç gram un düşer?','Bir kişilik miktarı 10 ile çarp.'],[DOGRU],
 [A('Orantı türü','Kişi sayısı artınca un da aynı oranda artar.','doğru orantı'),
  A('Bir kişilik','6 kişiye 450 gram.','450 ÷ 6 = 75 gram'),
  A('10 kişilik','Birim miktar × kişi sayısı.','10 × 75 = 750 gram')],
 'Doğru orantıda önce birim değeri (1 kişi, 1 kg) bul; sonra istenen miktarla çarp.',
 dict(A='75 gram, yalnızca bir kişilik un.',B='270 gram, ters orantı kurmak (450 × 6 ÷ 10); kişi artınca un artmalı.',D='1200 gram, 10 kişilik unu ilk 450 grama eklemek.',E='4500 gram, 450’yi 10 ile çarpıp 6’ya bölmeyi unutmak.'),
 TT(A='dikkat',B='bilgi',D='dikkat',E='islem'))
assert Fr(140,4)*10==350 and Fr(140,4)==35 and Fr(140*4,10)==56 and 6*35==210 and 140*10==1400
P.K('0001','Bir pazarda 4 kilogram domates 140 TL’ye satılmaktadır.\nAynı fiyattan 10 kilogram domates almak isteyen Zeynep kaç TL öder?',
 ['35','56','210','350','1400'],'D','10 kg domatesin tutarı.',
 ['Miktar artarsa tutar nasıl değişir?','1 kilogram domates kaç TL?','1 kilogramın fiyatını 10 ile çarp.'],[DOGRU],
 [A('Orantı türü','Miktar artınca tutar da aynı oranda artar.','doğru orantı'),
  A('Birim fiyat','4 kg 140 TL.','140 ÷ 4 = 35 TL'),
  A('10 kilogram','Birim fiyat × miktar.','10 × 35 = 350 TL')],
 'Birim fiyatı bulmak, doğru orantıdaki her soruyu tek çarpmaya indirir.',
 dict(A='35 TL, yalnızca 1 kilogramın fiyatı.',B='56 TL, ters orantı kurmak (140 × 4 ÷ 10).',C='210 TL, fazladan alınan 6 kilogramın tutarı; 10 kilogramın tamamı istenmiş.',E='1400 TL, 140’ı 10 ile çarpıp 4’e bölmeyi unutmak.'),
 TT(A='dikkat',B='bilgi',C='dikkat',E='islem'))

# ===== 0002 ters KOLAY
g=Fr(30*24,40); assert g==18 and 24-18==6 and 24-10==14 and 24-Fr(24,3)==16 and Fr(24*40,30)==32
P.R('0002','oo-ters',T['oo-ters'],'kolay','Tüketici sayısı ve gün','Tüketici sayısı ile yetme süresi arasındaki ters orantıdan yeni süreyi bulur.','hikâyeli',2,
 'K-ORN-02 (ters orantı) · yeni kurgu (barınak maması), tüketici artıyor',
 'Bir barınaktaki mama stoğu, barınaktaki 30 köpeğe 24 gün yetmektedir.\nBarınağa 10 köpek daha getirilmiştir.\nHer köpek her gün eşit miktarda mama yediğine göre aynı stok bu köpeklerin tamamına kaç gün yeter?',
 ['6','14','16','18','32'],'D','40 köpeğe stoğun yettiği gün sayısı.',
 ['Köpek sayısı artınca stok daha az mı, daha çok mu gün yeter?','Stok kaç “köpek-gün” mamadır?','Bu toplamı yeni köpek sayısına böl.'],[TERS],
 [A('Orantı türü','Köpek arttıkça gün azalır; köpek × gün sabittir.','ters orantı'),
  A('Toplam stok','30 köpek 24 gün yer.','30 × 24 = 720 köpek-gün'),
  A('Yeni süre','Artık 40 köpek var.','720 ÷ 40 = 18 gün')],
 'Ters orantıda iki çokluğun çarpımı sabittir; önce bu çarpımı bul.',
 dict(A='6, günlerdeki azalma (24 − 18); soru stoğun kaç gün yettiğini soruyor.',B='14, eklenen köpek sayısı kadar günü azaltmak.',C='16, köpek sayısı 1/3 arttı diye günü 1/3 azaltmak; ters orantıda bölme yapılır (24 × 30/40).',E='32, doğru orantı kurmak (24 × 40 ÷ 30).'),
 TT(A='dikkat',B='bilgi',C='islem',E='bilgi'))
n=Fr(120*30,180); assert n==20 and 30-20==10 and Fr(30*180,120)==45 and Fr(3600,60)==60
P.K('0002','Bir okul, belirli bir bütçeyle tanesi 120 TL olan defterden 30 tane alabilmektedir.\nDefterin tanesi 180 TL’ye çıkınca okul aynı bütçenin tamamını yine bu defterlere harcayacaktır.\nBuna göre okul kaç defter alabilir?',
 ['10','20','30','45','60'],'B','Yeni fiyatla alınabilecek defter sayısı.',
 ['Fiyat artınca aynı parayla daha az mı, daha çok mu defter alınır?','Bütçe kaç TL?','Bütçeyi yeni fiyata böl.'],[TERS],
 [A('Orantı türü','Bütçe sabit: fiyat × adet değişmez.','ters orantı'),
  A('Bütçe','30 defter, tanesi 120 TL.','30 × 120 = 3600 TL'),
  A('Yeni adet','Tanesi 180 TL.','3600 ÷ 180 = 20 defter')],
 'Sabit bütçede birim fiyat ile adet ters orantılıdır: çarpımları bütçeyi verir.',
 dict(A='10, defter sayısındaki azalma; soru yeni adedi soruyor.',C='30, fiyat değişimini hesaba katmamak.',D='45, doğru orantı kurmak (30 × 180 ÷ 120).',E='60, bütçeyi fiyat artışına (60 TL) bölmek.'),
 TT(A='dikkat',C='dikkat',D='bilgi',E='islem'))

# ===== 0003 birleşik ORTA
a,g_,b_=8,12,15; assert Fr(a,g_)==Fr(2,3) and Fr(g_,b_)==Fr(4,5); k=Fr(140,a+g_+b_); assert k==4 and (a*k,g_*k,b_*k)==(32,48,60)
assert 140*Fr(5,10)==70 and 140-60==80
P.R('0003','oo-bilesik',T['oo-bilesik'],'orta','Üçlü oran','Ortak terimi eşitleyerek iki orandan üçlü oran kurar ve toplamdan istenen parçayı bulur.','hikâyeli',3,
 'K-ORN-03 (ortak terimle birleştirme) · yeni kurgu (okul olimpiyatı madalyaları), toplam verildi',
 'Bir okul olimpiyatında dağıtılan altın madalyaların sayısının gümüş madalyaların sayısına oranı 2/3, gümüş madalyaların sayısının bronz madalyaların sayısına oranı ise 4/5’tir.\nOlimpiyatta toplam 140 madalya dağıtıldığına göre kaç bronz madalya dağıtılmıştır?',
 ['32','48','60','70','80'],'C','Bronz madalya sayısı.',
 ['İki oranda ortak olan madalya türü hangisi?','Gümüşü iki oranda da aynı sayıyla göster.','Üçlü oranın parçalarını topla; bir parça kaç madalya?'],[ORAN,ORTAK],
 [A('Ortak terim','Gümüş iki oranda da var: 3 ve 4’ün ortak katı 12.','2/3 = 8/12 · 4/5 = 12/15'),
  A('Üçlü oran','Altın : gümüş : bronz.','8 : 12 : 15 ⇒ 35 parça'),
  A('Bir parça','Toplam 140 madalya.','140 ÷ 35 = 4'),
  A('Bronz','15 parça.','15 × 4 = 60 · kontrol: 32 + 48 + 60 = 140 ✓')],
 'İki oranı birleştirirken önce ortak terimi aynı sayıya getir; sonra parçaları topla.',
 dict(A='32, altın madalya sayısı.',B='48, gümüş madalya sayısı.',D='70, gümüşü eşitlemeden 2 : 3 : 5 yazmak (10 parça, bir parça 14).',E='80, bronz olmayan madalyaların sayısı.'),
 TT(A='dikkat',B='dikkat',D='islem',E='dikkat'))
e,p,n=3,4,6; assert Fr(e,p)==Fr(3,4) and Fr(p,n)==Fr(2,3); k=Fr(450,n); assert k==75 and (e*k,p*k,(e+p+n)*k)==(225,300,975) and 225+300==525 and 300+450==750
P.K('0003','Bir meyve suyu karışımında elma suyu miktarının portakal suyu miktarına oranı 3/4, portakal suyu miktarının nar suyu miktarına oranı ise 2/3’tür.\nKarışımda yalnızca bu üç meyve suyu vardır ve karışımdaki nar suyu 450 mL’dir.\nBuna göre karışımın tamamı kaç mL’dir?',
 ['225','300','525','750','975'],'E','Karışımın toplam miktarı.',
 ['Ortak terim hangisi? İki oranda onu aynı sayıyla yaz.','Nar suyu üçlü oranda kaç parça?','Bir parçayı bulup tüm parçalarla çarp.'],[ORAN,ORTAK],
 [A('Ortak terim','Portakal iki oranda da var: 4 ve 2’nin ortak katı 4.','3/4 · 2/3 = 4/6'),
  A('Üçlü oran','Elma : portakal : nar.','3 : 4 : 6 ⇒ 13 parça'),
  A('Bir parça','Nar 6 parça = 450 mL.','450 ÷ 6 = 75 mL'),
  A('Karışım','13 parça.','13 × 75 = 975 mL')],
 'Bir parçanın değeri bulunduğunda istenen miktar, ona düşen parça sayısıyla çarpılarak bulunur.',
 dict(A='225 mL, elma suyu miktarı.',B='300 mL, portakal suyu miktarı.',C='525 mL, elma ve portakal sularının toplamı; nar suyu eklenmedi.',D='750 mL, portakal ve nar sularının toplamı; elma suyu eklenmedi.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='dikkat'))

# ===== 0004 ters paylaştırma ORTA
w=[Fr(1,2),Fr(1,3),Fr(1,4)]; L=12; parca=[x*L for x in w]; assert parca==[6,4,3]
k=Fr(2400,parca[0]-parca[1]); assert k==1200 and [x*k for x in parca]==[7200,4800,3600] and 13*k==15600
assert Fr(2400,1)*4==9600
P.R('0004','oo-paylastirma',T['oo-paylastirma'],'orta','Ters orantılı ödül','Sürelerle ters orantılı paylaştırmada iki payın farkından bir parçanın değerini ve istenen payı bulur.','hikâyeli',3,
 'K-ORN-04 (orantılı paylaştırma) · ters orantı, iki payın farkı verildi, yeni kurgu (dağ maratonu)',
 'Bir dağ maratonunda parkuru 2 saatte, 3 saatte ve 4 saatte tamamlayan üç koşucuya verilen para ödülü, koşucuların bitirme süreleriyle ters orantılı olarak paylaştırılmıştır.\nParkuru 2 saatte bitiren koşucu, 3 saatte bitiren koşucudan 2400 TL fazla almıştır.\nBuna göre parkuru 4 saatte bitiren koşucu kaç TL almıştır?',
 ['3600','4800','7200','9600','15 600'],'A','4 saatte bitiren koşucunun aldığı ödül.',
 ['Ters orantıda paylar 1/2, 1/3 ve 1/4 ile orantılıdır.','Paydaları eşitle: 12 ile genişlet.','İlk iki payın farkı kaç parça?'],[TERS,PAYL],
 [A('Payları yaz','Süreyle ters orantılı: 1/2, 1/3, 1/4.','12 ile genişlet: 6 : 4 : 3'),
  A('Bir parça','İlk iki pay arasında 6 − 4 = 2 parça fark var.','2 parça = 2400 ⇒ 1 parça = 1200 TL'),
  A('4 saatte bitiren','3 parça.','3 × 1200 = 3600 TL · paylar 7200, 4800, 3600')],
 'Ters orantılı paylaştırmada sayıların çarpmaya göre terslerini al, paydaları eşitleyip tam sayılı orana çevir.',
 dict(B='4800 TL, 3 saatte bitiren koşucunun payı.',C='7200 TL, 2 saatte bitiren koşucunun payı.',D='9600 TL, doğru orantılı paylaştırmak (2 : 3 : 4) ve farkı 1 parça almak.',E='15 600 TL, ödülün tamamı.'),
 TT(B='dikkat',C='dikkat',D='bilgi',E='dikkat'))
pr=[2,3,5]; k=Fr(18000,2); assert k==9000 and [x*k for x in pr]==[18000,27000,45000] and 10*k==90000 and 90000-18000==72000 and 18000*10==180000
P.K('0004','Üç ortak, bir kooperatife sırasıyla 40 000 TL, 60 000 TL ve 100 000 TL yatırmıştır.\nYıl sonundaki kâr, ortakların yatırdıkları parayla doğru orantılı olarak paylaştırılmış ve en az pay alan ortak 18 000 TL almıştır.\nBuna göre yıl sonundaki kârın tamamı kaç TL’dir?',
 ['27 000','45 000','72 000','90 000','180 000'],'D','Kârın tamamı.',
 ['Yatırımları en sade tam sayı oranına indir.','En az alan ortak kaç parça aldı?','Bir parçanın değerini bul, tüm parçalarla çarp.'],[PAYL],
 [A('Sade oran','40 000 : 60 000 : 100 000.','2 : 3 : 5 ⇒ 10 parça'),
  A('Bir parça','En az pay 2 parça = 18 000 TL.','1 parça = 9000 TL'),
  A('Kârın tamamı','10 parça.','10 × 9000 = 90 000 TL')],
 'Doğru orantılı paylaştırmada önce oranı sadeleştir; verilen pay kaç parçaysa ona böl.',
 dict(A='27 000 TL, ikinci ortağın payı.',B='45 000 TL, üçüncü ortağın payı.',C='72 000 TL, en az pay alan ortağın dışındaki ortakların toplam payı.',E='180 000 TL, 18 000 TL’yi 1 parça sanmak; bu ortak 2 parça aldı.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='islem'))

# ===== 0005 oran değişimi ORTA
c=[(o,42-o) for o in range(42) if Fr(o,42-o)==Fr(2,5)]; assert c==[(12,30)]
x=[x for x in range(30) if Fr(12+x,30-x)==2]; assert x==[16] and 30-16==14 and 12+16==28 and 42//2==21
P.R('0005','oo-oran-degisim',T['oo-oran-degisim'],'orta','Okunan ve okunmayan','Toplamı bilinen iki grubun ilk oranından grupları bulup, aradaki geçişle oluşan yeni orandan geçen miktarı hesaplar.','hikâyeli',3,
 'K-ORN-05 (oran değişimi) · yeni kurgu (okuma listesi), toplam sabit, istenen aktarılan miktar',
 'Defne’nin yaz okuma listesinde 42 kitap vardır. Tatil başlamadan önce Defne’nin bu listeden okuduğu kitapların sayısının okumadığı kitapların sayısına oranı 2/5’tir.\nDefne tatilde listedeki kitaplardan bir kısmını daha okumuş ve bu oran 2 olmuştur.\nBuna göre Defne tatilde listeden kaç kitap okumuştur?',
 ['12','14','16','28','30'],'C','Tatilde okunan kitap sayısı.',
 ['Tatilden önce okunan ve okunmayan kitaplar kaçar tane?','Tatilden sonra oran 2 ise okunan kitaplar okunmayanların kaç katı?','Okunan kitapların artışı tatilde okunanlardır.'],[ORAN],
 [A('İlk durum','2k + 5k = 42 ⇒ k = 6.','okunan 12 · okunmayan 30'),
  A('Son durum','Oran 2: okunan = 2 × okunmayan; toplam yine 42.','3 parça = 42 ⇒ okunmayan 14 · okunan 28'),
  A('Tatilde okunan','Okunan kitaplardaki artış.','28 − 12 = 16 · kontrol: 30 − 16 = 14 ✓')],
 'Toplam sabitken oran değişiyorsa iki durumu da toplamdan çöz; fark aktarılan miktardır.',
 dict(A='12, tatilden önce okunan kitap sayısı.',B='14, tatilden sonra okunmayan kitap sayısı.',D='28, tatilden sonra okunan kitapların toplamı; tatilden öncekiler de içinde.',E='30, tatilden önce okunmayan kitap sayısı.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='dikkat'))
t=[t for t in range(1,100) if Fr(5*t,3*t+20)==Fr(5,4)]; assert t==[20] and (100,60,80) == (5*20,3*20,3*20+20) and 160==100+60 and 100+80==180
P.K('0005','Bir kafede gün içinde verilen çay siparişlerinin sayısının kahve siparişlerinin sayısına oranı öğlene kadar 5/3’tür.\nÖğleden sonra yalnızca 20 kahve siparişi daha verilmiş ve çay siparişlerinin sayısının kahve siparişlerinin sayısına oranı 5/4 olmuştur.\nBuna göre bu kafede gün içinde toplam kaç sipariş verilmiştir?',
 ['60','80','100','160','180'],'E','Gün içindeki toplam sipariş sayısı.',
 ['Öğlene kadarki çay ve kahve siparişlerini k ile yaz.','Öğleden sonra yalnızca kahve değişti; yeni oranı denkleme yaz.','k’yi bulduktan sonra son durumdaki toplamı hesapla.'],[ORAN],
 [A('İlk durum','Oran 5/3.','çay 5k · kahve 3k'),
  A('Yeni oran','Kahveye 20 eklendi, çay aynı.','5k ÷ (3k + 20) = 5/4 ⇒ 20k = 15k + 100 ⇒ k = 20'),
  A('Sayılar','Çay 100, kahve önce 60, sonra 80.','100 ÷ 80 = 5/4 ✓'),
  A('Toplam','Gün sonundaki siparişler.','100 + 80 = 180')],
 'Oran değişimi sorularında değişmeyen grubu k ile yazıp yeni oranı içler-dışlar çarpımıyla çöz.',
 dict(A='60, öğlene kadarki kahve siparişi.',B='80, gün içindeki toplam kahve siparişi.',C='100, çay siparişlerinin sayısı.',D='160, öğlene kadarki toplam sipariş; öğleden sonraki 20 kahve eklenmedi.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='dikkat'))

# ===== 0006 doğru (iki adım) ORTA
lt=Fr(6*450,100); assert lt==27 and lt*55==1485 and 6*55==330 and 5*330==1650 and Fr(450,6)*55==4125 and 450*Fr(6,10)*55==14850
P.R('0006','oo-dogru',T['oo-dogru'],'orta','Yakıt ve tutar','İki doğru orantıyı (yol–yakıt, yakıt–tutar) art arda uygular.','hikâyeli',3,
 'K-ORN-01 (doğru orantı) · iki orantı art arda, yeni kurgu (yakıt tüketimi)',
 'Bir otomobil her 100 kilometrede 6 litre benzin harcamaktadır. Benzinin litresi 55 TL’dir.\nBu otomobil, yakıt tüketimi değişmeden 450 kilometrelik bir yol gidecektir.\nBuna göre bu yolculuk için harcanacak benzinin tutarı kaç TL’dir?',
 ['330','1485','1650','4125','14 850'],'B','450 km için benzin tutarı.',
 ['450 km, 100 km’nin kaç katı?','Harcanacak benzin kaç litre?','Litreyi birim fiyatla çarp.'],[DOGRU],
 [A('Yakıt miktarı','Yol 4,5 katına çıkınca yakıt da 4,5 katına çıkar.','6 × 4,5 = 27 litre'),
  A('Tutar','Litresi 55 TL.','27 × 55 = 1485 TL'),
  A('Kontrol','100 km 6 × 55 = 330 TL tutar.','4,5 × 330 = 1485 ✓')],
 'Art arda doğru orantılarda her adımda birim değeri bul ya da katsayıyı taşı.',
 dict(A='330 TL, yalnızca 100 km’nin yakıt tutarı.',C='1650 TL, 450 km’yi 5 tane 100 km saymak.',D='4125 TL, 450’yi 6’ya bölüp 75 litre bulmak; 6 litre 100 km içindir.',E='14 850 TL, litre hesabında virgülü kaydırmak (450 × 0,6).'),
 TT(A='dikkat',C='islem',D='bilgi',E='islem'))
kwh=Fr(16*250,100); assert kwh==40 and kwh*9==360 and 16*9==144 and 2*144==288 and 250*16*9//10==3600
P.K('0006','Elektrikli bir otomobil her 100 kilometrede 16 kWh enerji harcamaktadır. Bir şarj istasyonunda 1 kWh enerjinin ücreti 9 TL’dir.\nBu otomobil, enerji tüketimi değişmeden 250 kilometre yol gidecektir.\nBuna göre bu yol için gereken enerjinin şarj ücreti kaç TL’dir?',
 ['40','144','288','360','3600'],'D','250 km için şarj ücreti.',
 ['250 km, 100 km’nin kaç katı?','Gereken enerji kaç kWh?','kWh’yi birim ücretle çarp.'],[DOGRU],
 [A('Enerji','Yol 2,5 katına çıkınca enerji de 2,5 katına çıkar.','16 × 2,5 = 40 kWh'),
  A('Ücret','1 kWh 9 TL.','40 × 9 = 360 TL'),
  A('Kontrol','100 km 16 × 9 = 144 TL tutar.','2,5 × 144 = 360 ✓')],
 'Önce ara çokluğu (litre, kWh) bul, sonra fiyata geç; birimleri her adımda yaz.',
 dict(A='40, gereken enerji (kWh); soru ücreti soruyor.',B='144 TL, yalnızca 100 km’nin şarj ücreti.',C='288 TL, 250 km’yi 2 tane 100 km saymak.',E='3600 TL, enerji hesabında virgülü kaydırmak (400 kWh).'),
 TT(A='dikkat',B='dikkat',C='islem',E='islem'))

# ===== 0007 paylaştırma değişim ZOR
e1=[Fr(112*x,12+16+28) for x in (12,16,28)]; e2=[Fr(112*x,12+24+28) for x in (12,24,28)]
assert e1==[24,32,56] and e2==[21,42,49] and e1[2]-e2[2]==7 and e1[0]-e2[0]==3 and e2[1]-e1[1]==10 and Fr(112,14)==8 and Fr(112,16)==7
P.R('0007','oo-paylastirma',T['oo-paylastirma'],'zor','Değişen paylaştırma','Orantılı paylaştırmada bir terim değişince yeni payları hesaplayıp planlananla karşılaştırır.','hikâyeli',4,
 'K-ORN-04 (orantılı paylaştırma) · paylaştırma ölçütü değişiyor, istenen bir paydaki azalma; yeni kurgu (şubelere bilgisayar)',
 'Bir firma, 112 bilgisayarı üç şubesine, şubelerdeki çalışan sayılarıyla doğru orantılı olacak biçimde dağıtmayı planlamıştır. Bu şubelerdeki çalışan sayıları sırasıyla 12, 16 ve 28’dir.\nDağıtımdan önce 2. şubeye 8 yeni çalışan katılmış ve bilgisayarlar yeni çalışan sayılarıyla doğru orantılı olarak dağıtılmıştır.\nBuna göre 3. şube planlanandan kaç bilgisayar eksik almıştır?',
 ['3','7','8','10','49'],'B','3. şubenin planlanana göre eksik aldığı bilgisayar sayısı.',
 ['Planlanan oranı sadeleştir; bir parça kaç bilgisayar?','8 çalışan katılınca yeni oran ve parça sayısı ne olur?','3. şubenin iki dağıtımdaki payını karşılaştır.'],[PAYL],
 [A('Plan','12 : 16 : 28 = 3 : 4 : 7 ⇒ 14 parça.','112 ÷ 14 = 8 ⇒ 24, 32, 56'),
  A('Yeni oran','2. şube 24 çalışan oldu.','12 : 24 : 28 = 3 : 6 : 7 ⇒ 16 parça'),
  A('Yeni paylar','Bir parça 112 ÷ 16 = 7.','21, 42, 49'),
  A('3. şube','Planlanan 56, alınan 49.','56 − 49 = 7')],
 'Paylaştırmada bir terim değişirse toplam parça sayısı da değişir; bütün payları yeniden hesapla.',
 dict(A='3, 1. şubedeki azalma (24 − 21).',C='8, plandaki bir parçanın değeri (112 ÷ 14); soru 3. şubenin eksiğini soruyor.',D='10, 2. şubedeki artış (42 − 32).',E='49, 3. şubenin yeni dağıtımdaki payı; soru eksik kalan miktarı soruyor.'),
 TT(A='dikkat',C='dikkat',D='dikkat',E='dikkat'))
e1=[Fr(220*x,20) for x in (4,6,10)]; e2=[Fr(220*x,22) for x in (6,6,10)]
assert e1==[44,66,110] and e2==[60,60,100] and e1[1]-e2[1]==6 and e1[2]-e2[2]==10 and e2[0]-e1[0]==16 and Fr(220,10)==22 and Fr(220,11)==20
P.K('0007','Bir belediye, 220 fidanı üç mahalleye, mahallelerin nüfuslarıyla doğru orantılı olacak biçimde dağıtmayı planlamıştır. Mahallelerin nüfusları sırasıyla 4000, 6000 ve 10 000’dir.\nDağıtımdan önce yapılan sayımda 1. mahallenin nüfusunun 6000 olduğu görülmüş ve fidanlar güncel nüfuslarla doğru orantılı dağıtılmıştır.\nBuna göre 2. mahalle planlanandan kaç fidan eksik almıştır?',
 ['6','10','16','20','60'],'A','2. mahallenin eksik aldığı fidan sayısı.',
 ['Planlanan oranı sadeleştir; bir parça kaç fidan?','Güncel nüfuslarla yeni oranı ve parça sayısını bul.','2. mahallenin iki paylaştırmadaki payını karşılaştır.'],[PAYL],
 [A('Plan','4000 : 6000 : 10 000 = 2 : 3 : 5 ⇒ 10 parça.','220 ÷ 10 = 22 ⇒ 44, 66, 110'),
  A('Yeni oran','1. mahalle 6000.','6000 : 6000 : 10 000 = 3 : 3 : 5 ⇒ 11 parça'),
  A('Yeni paylar','Bir parça 220 ÷ 11 = 20.','60, 60, 100'),
  A('2. mahalle','Planlanan 66, alınan 60.','66 − 60 = 6')],
 'Bir terim değişmese bile ona düşen pay değişebilir; çünkü toplam parça sayısı değişir.',
 dict(B='10, 3. mahalledeki azalma (110 − 100).',C='16, 1. mahalledeki artış (60 − 44).',D='20, yeni dağıtımda bir parçanın değeri.',E='60, 2. mahallenin yeni payı; soru eksik kalan miktarı soruyor.'),
 TT(B='dikkat',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0008 iki yönlü değişim ZOR
t=[t for t in range(1,100) if Fr(4*t-6,5*t+3)==Fr(1,2)]; assert t==[5]
kz,er=20,25; assert (kz-6,er+3)==(14,28) and 14+28==42 and 45-6==39 and kz+er==45
P.R('0008','oo-oran-degisim',T['oo-oran-degisim'],'zor','İki grupta değişim','İki gruptan birinden çıkış, diğerine giriş olduktan sonraki orandan grupları bulup son durumu hesaplar.','hikâyeli',4,
 'K-ORN-05 (oran değişimi) · iki grupta zıt yönlü değişim, istenen son toplam; yeni kurgu (yüzme kursu)',
 'Bir yüzme kursundaki kız öğrencilerin sayısının erkek öğrencilerin sayısına oranı 4/5’tir.\nKurstan 6 kız öğrenci ayrılmış, kursa 3 erkek öğrenci katılmıştır. Bu değişikliklerden sonra kız öğrencilerin sayısının erkek öğrencilerin sayısına oranı 1/2 olmuştur.\nBuna göre son durumda kursta kaç öğrenci vardır?',
 ['14','28','39','42','45'],'D','Son durumdaki öğrenci sayısı.',
 ['Başlangıçtaki kız ve erkek sayılarını k ile yaz.','Kızlardan 6 çıkar, erkeklere 3 ekle; yeni oranı yaz.','k’yi bulup son durumdaki sayıları topla.'],[ORAN],
 [A('İlk durum','Oran 4/5.','kız 4k · erkek 5k'),
  A('Değişim','Kızlar 6 azaldı, erkekler 3 arttı.','(4k − 6) ÷ (5k + 3) = 1/2'),
  A('Çöz','İçler-dışlar çarpımı.','8k − 12 = 5k + 3 ⇒ 3k = 15 ⇒ k = 5'),
  A('Son durum','Kız 20 − 6 = 14, erkek 25 + 3 = 28.','14 ÷ 28 = 1/2 ✓ · 14 + 28 = 42')],
 'Değişimden sonra oran verildiğinde her grubun değişimini ayrı yaz, sonra tek denklem kur.',
 dict(A='14, son durumdaki kız öğrenci sayısı.',B='28, son durumdaki erkek öğrenci sayısı.',C='39, başlangıç toplamından yalnızca ayrılan kızları çıkarmak; katılan erkekler eklenmedi.',E='45, başlangıçtaki öğrenci sayısı.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='dikkat'))
t=[t for t in range(1,100) if Fr(7*t-10,3*t+5)==Fr(3,2)]; assert t==[7]
o,m=49,21; assert (o-10,m+5)==(39,26) and 39+26==65 and o+m==70
P.K('0008','Bir alışveriş merkezinin otoparkındaki otomobillerin sayısının motosikletlerin sayısına oranı 7/3’tür.\nBir süre sonra otoparktan 10 otomobil çıkmış, otoparka 5 motosiklet girmiştir. Bu durumda otomobillerin sayısının motosikletlerin sayısına oranı 3/2 olmuştur.\nBuna göre otoparkta başlangıçta kaç araç vardır?',
 ['26','39','49','65','70'],'E','Başlangıçtaki araç sayısı.',
 ['Başlangıçtaki otomobil ve motosiklet sayılarını k ile yaz.','Çıkan ve giren araçları ayrı gruplara uygula.','k’yi bulup başlangıçtaki toplamı hesapla.'],[ORAN],
 [A('İlk durum','Oran 7/3.','otomobil 7k · motosiklet 3k'),
  A('Değişim','10 otomobil çıktı, 5 motosiklet girdi.','(7k − 10) ÷ (3k + 5) = 3/2'),
  A('Çöz','İçler-dışlar çarpımı.','14k − 20 = 9k + 15 ⇒ 5k = 35 ⇒ k = 7'),
  A('Başlangıç','Otomobil 49, motosiklet 21.','49 + 21 = 70 · kontrol: 39 ÷ 26 = 3/2 ✓')],
 'Hangi durumun sorulduğuna dikkat et: k’yi bulunca hem ilk hem son durumu yazmak hatayı önler.',
 dict(A='26, son durumdaki motosiklet sayısı.',B='39, son durumdaki otomobil sayısı.',C='49, başlangıçtaki otomobil sayısı; motosikletler eklenmedi.',D='65, son durumdaki araç sayısı; soru başlangıcı soruyor.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='dikkat'))

P.yaz(os.path.join(H,'oranoranti-1.json'),os.path.join(H,'oranoranti-1-kardes.json'))
