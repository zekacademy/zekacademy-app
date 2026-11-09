"""TYT Kimya · Karışımlar (6 ana + 6 kardeş). Tüm sayısal cevaplar kodla doğrulanır."""
from kimortak import *
K=Kim('karisimlar','Karışımlar','kim|Karışımlar','KKR')
HOM=B('Homojen ve heterojen karışım','Homojen: her yerinde aynı özellik, tek faz (tuzlu su, alaşımlar). Heterojen: bölgeleri birbirinden ayırt edilir, birden çok faz (çamurlu su, yağ–su)')

# ---- 0001 kolay: homojen/heterojen sınıflandırma
K.Q('0001','kim-karisim-sinif','Homojen ve heterojen karışımları ayırt etme','kolay','Homojen ve Heterojen Karışımlar','Verilen karışımları homojen ve heterojen olarak sınıflandırır.','öncüllü',2,
 'Günlük karışımlar homojen mi heterojen mi?','Alaşımı saf madde ya da heterojen sanmak.',[HOM],
 'Gözle ya da mikroskopla ayrı bölgeler ayırt ediliyorsa karışım heterojendir; çözeltiler ve alaşımlar homojendir.',
 dict(m='I. Sirke (asetik asit–su)\nII. Çamurlu su\nIII. Bronz (bakır–kalay alaşımı)\nYukarıdaki karışımlardan hangileri homojendir?',
  i='Homojen olan karışımlar.',ip=['Homojen karışımın her yerinde özellik aynıdır.','Alaşımlar katı çözelti sayılır.','Çamurlu suda toprak parçacıkları ayırt edilir mi?'],
  ad=[A('Tanımı hatırla','Homojen karışımda her yer aynı görünür; heterojende ayrı bölgeler vardır.','homojen: tek faz · heterojen: çok faz'),
      A('Öncülleri incele','Sirke bir çözeltidir. Bronz katı çözeltidir. Çamurlu suda toprak parçacıkları ayırt edilir.','I: homojen · II: heterojen · III: homojen'),
      A('Sonuç','Homojen olanlar I ve III’tür.','I ve III')],
  d='I ve III',y=[('Yalnız I','Bronzu homojen saymamışsın; alaşımlar da homojen karışımdır.','b'),('Yalnız II','Çamurlu su heterojendir; soruyu “heterojen hangisi” diye okumuşsun.','d'),('I ve II','Çamurlu suyu homojen sanmışsın; toprak parçacıkları gözle ayırt edilir.','b'),('II ve III','Sirkeyi homojen saymayıp çamurlu suyu homojen kabul etmişsin.','b')],
  sira=['Yalnız I','Yalnız II','I ve II','II ve III','I ve III']),
 dict(m='I. Tuzlu su\nII. Demir tozu–kükürt tozu karışımı\nIII. Temiz ve kuru hava\nYukarıdaki karışımlardan hangisi ya da hangileri heterojendir?',
  d='Yalnız II',y=[('Yalnız I','Tuzlu su çözeltidir; tuz suda her yere eşit dağılır, homojendir.','b'),('Yalnız III','Gaz karışımları da homojendir; havada ayrı bölgeler ayırt edilmez.','b'),('I ve II','Tuzlu suyu da heterojen saymışsın; çözeltiler homojendir.','b'),('I ve III','İki homojen karışımı seçmişsin; soru heterojen olanı soruyor.','d')],
  ad=[A('Tanımı hatırla','Heterojen karışımda bölgeler birbirinden ayırt edilir.','heterojen: çok faz'),
      A('Öncülleri incele','Tuzlu su ve hava çözeltidir. Demir ve kükürt tozları ayrı parçacıklar hâlinde durur.','I: homojen · II: heterojen · III: homojen'),
      A('Sonuç','Yalnız II heterojendir.','Yalnız II')],
  sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']),
 'Karışım türü: homojen–heterojen','Öncüllü sınıflandırma','homojen: sirke, alaşım · heterojen: çamurlu su')

# ---- 0002 orta: karıştırma %
for (m1,p1,m2,p2) in [(100,20,300,40),(150,12,250,20)]:
    c=Fr(m1*p1+m2*p2,m1+m2); assert c==(35 if m1==100 else 17)
    assert Fr(m2*p1+m1*p2,m1+m2)==(25 if m1==100 else 15)  # ağırlıklar ters
K.Q('0002','kim-karisim-yuzde','Kütlece yüzde derişimli çözeltileri karıştırma','orta','Kütlece Yüzde Derişim','Farklı derişimli çözeltilerin karışımının kütlece yüzde derişimini hesaplar.','hikâyeli',3,
 'İki çözeltinin karıştırılmasında yeni yüzde','Derişimlerin aritmetik ortalamasını almak.',
 [B('Kütlece yüzde derişim','100 g çözeltide çözünen kütlesidir. Örnek: %20’lik 150 g çözeltide 150 × 20/100 = 30 g çözünen vardır'),B('Karıştırma','Çözünen kütleleri ve çözelti kütleleri ayrı ayrı toplanır, sonra oran alınır')],
 'Karışımın derişimi, kütleleriyle ağırlıklandırılmış ortalamadır; çözünen ve çözelti kütlelerini ayrı topla.',
 dict(m='Kütlece %20’lik 100 g şekerli su çözeltisi ile kütlece %40’lık 300 g şekerli su çözeltisi karıştırılıyor.\nBuna göre oluşan çözeltinin kütlece yüzde derişimi kaçtır?',
  i='Son çözeltinin kütlece yüzde derişimi.',ip=['Her çözeltideki şeker kütlesini ayrı ayrı bul.','Şeker kütlelerini de çözelti kütlelerini de topla.','Toplam şeker kütlesini toplam çözelti kütlesine böl.'],
  ad=[A('Şeker kütlelerini bul','Kütlece % derişim, 100 g çözeltideki çözünen kütlesidir.','1. çözelti: 100 × 20/100 = 20 g · 2. çözelti: 300 × 40/100 = 120 g'),
      A('Toplamları bul','Karıştırmada şeker ve çözelti kütleleri ayrı ayrı toplanır.','şeker: 20 + 120 = 140 g · çözelti: 100 + 300 = 400 g'),
      A('Yüzdeyi hesapla','Şeker kütlesi toplam çözelti kütlesine bölünür.','140/400 × 100 = %35')],
  d='35',y=[('25','Çözelti kütlelerini ters ağırlıklandırmışsın; çok olan 300 g’ın derişimi daha etkilidir.','i'),('30','İki derişimin aritmetik ortalamasını almışsın; kütleler farklı olduğundan ortalama ağırlıklı olmalı.','b'),('40','Yüksek derişimli çözeltinin yüzdesini aynen almışsın.','d'),('60','Yüzdeleri toplamışsın; karışımda derişim toplanmaz.','b')]),
 dict(m='Kütlece %12’lik 150 g tuzlu su çözeltisi ile kütlece %20’lik 250 g tuzlu su çözeltisi karıştırılıyor.\nBuna göre oluşan çözeltinin kütlece yüzde derişimi kaçtır?',
  ip=['Her çözeltideki tuz kütlesini ayrı ayrı bul.','Tuz kütlelerini de çözelti kütlelerini de topla.','Toplam tuzu toplam çözeltiye böl.'],
  ad=[A('Tuz kütlelerini bul','Kütlece % derişim, 100 g çözeltideki çözünen kütlesidir.','1. çözelti: 150 × 12/100 = 18 g · 2. çözelti: 250 × 20/100 = 50 g'),
      A('Toplamları bul','Tuz ve çözelti kütleleri ayrı ayrı toplanır.','tuz: 18 + 50 = 68 g · çözelti: 150 + 250 = 400 g'),
      A('Yüzdeyi hesapla','Tuz kütlesi toplam çözelti kütlesine bölünür.','68/400 × 100 = %17')],
  d='17',y=[('15','Çözelti kütlelerini ters ağırlıklandırmışsın; 250 g olan çözeltinin payı daha büyüktür.','i'),('16','İki derişimin aritmetik ortalamasını almışsın; kütleler eşit olmadığından ağırlıklı ortalama gerekir.','b'),('20','Daha derişik çözeltinin yüzdesini aynen almışsın.','d'),('32','Yüzdeleri toplamışsın; karışımda derişim toplanmaz.','b')]),
 'iki çözeltiyi karıştırma','farklı kütle ve derişim, yeni çözünen','kütle oranı 1:3 ⇒ ağırlıklı ortalama',
 kisa='Çözelti kütleleri 1 : 3 oranındadır; derişim 20 ile 40’ın ağırlıklı ortalamasıdır: (1 × 20 + 3 × 40)/4 = 35.')

# ---- 0003 orta: çözünürlük
for (c,su,konan,kal) in [(30,250,90,15),(25,160,50,10)]:
    cozen=Fr(su*c,100); assert max(0,konan-cozen)==kal
K.Q('0003','kim-karisim-cozunurluk','Çözünürlük ve doymuş çözelti','orta','Çözünürlük','Verilen sıcaklıktaki çözünürlüğe göre çözünen ve çözünmeden kalan madde miktarını hesaplar.','hikâyeli',3,
 'Çözünürlüğe göre çözünmeyen miktar','Çözünürlüğü 100 g suya göre değil, verilen su miktarına uyarlamamak.',
 [B('Çözünürlük','Belirli sıcaklıkta 100 g suda çözünebilen en çok madde kütlesidir. Örnek: 100 g suda 30 g çözünüyorsa 200 g suda 60 g çözünür'),B('Doymuş çözelti','O sıcaklıkta daha fazla madde çözemeyen çözeltidir; fazlası dipte çözünmeden kalır')],
 'Önce verilen su kütlesinin çözebileceği en çok miktarı bul, sonra konan miktarla karşılaştır.',
 dict(m='Bir katının 20 °C’deki çözünürlüğü 100 g suda 30 g’dır.\n20 °C’de 250 g saf suya bu katıdan 90 g konup karıştırılıyor.\nBuna göre çözünmeden kalan katı kütlesi kaç g’dır?',
  i='Çözünmeden kalan katının kütlesi.',ip=['Çözünürlük 100 g su için verilmiş; 250 g su kaç g çözer?','Konan miktar bu değerden büyük mü?','Fazlası çözünmeden kalır.'],
  ad=[A('Çözülebilecek miktarı bul','Çözünürlük su kütlesiyle doğru orantılıdır.','100 g su → 30 g · 250 g su → 250 × 30/100 = 75 g'),
      A('Konan miktarla karşılaştır','90 g, çözülebilecek en çok miktar olan 75 g’dan büyüktür.','90 > 75'),
      A('Artanı hesapla','Çözünmeyen kısım, konan ile çözünen miktarın farkıdır.','90 − 75 = 15 g')],
  d='15',y=[('30','Çözünürlük değerini (30 g) çözünmeyen miktar sanmışsın.','b'),('60','100 g su varmış gibi hesaplamışsın: 90 − 30 = 60.','i'),('75','Çözünen kütleyi bulup soruyu orada bırakmışsın.','d'),('90','Konan katının tamamının çözünmediğini düşünmüşsün; 75 g’ı çözünür.','b')]),
 dict(m='Bir tuzun 25 °C’deki çözünürlüğü 100 g suda 25 g’dır.\n25 °C’de 160 g saf suya bu tuzdan 50 g konup karıştırılıyor.\nBuna göre çözünmeden kalan tuz kütlesi kaç g’dır?',
  ip=['Çözünürlük 100 g su için verilmiş; 160 g su kaç g tuz çözer?','Konan miktar bu değerden büyük mü?','Fazlası çözünmeden kalır.'],
  ad=[A('Çözülebilecek miktarı bul','Çözünürlük su kütlesiyle doğru orantılıdır.','100 g su → 25 g · 160 g su → 160 × 25/100 = 40 g'),
      A('Konan miktarla karşılaştır','50 g, çözülebilecek en çok miktar olan 40 g’dan büyüktür.','50 > 40'),
      A('Artanı hesapla','Çözünmeyen kısım, konan ile çözünen miktarın farkıdır.','50 − 40 = 10 g')],
  d='10',y=[('0','Konan tuzun tamamının çözüneceğini sanmışsın; 160 g su en çok 40 g çözer.','b'),('25','Çözünürlük değerini çözünmeyen miktar sanmışsın.','b'),('40','Çözünen kütleyi bulup soruyu orada bırakmışsın.','d'),('50','Konan tuzun hiç çözünmediğini varsaymışsın.','b')]),
 'çözünürlüğe göre kalan katı','farklı su kütlesi ve çözünürlük','250 g su · 75 g çözer · 15 g artar')

# ---- 0004 orta: donma noktası (koligatif)
K.Q('0004','kim-karisim-koligatif','Çözünen tanecik sayısına göre donma noktası','orta','Çözeltilerin Donma Noktası','Çözünen tanecik sayısına göre çözeltilerin donma noktalarını karşılaştırır.','öncüllü',3,
 'Tanecik sayısı arttıkça donma noktası düşer','Tuzun iyonlarına ayrıştığını unutup mol sayısını karşılaştırmak.',
 [B('Donma noktası alçalması','Suda çözünen tanecik sayısı arttıkça çözeltinin donma noktası saf suyunkinden daha çok düşer'),B('İyonlarına ayrışma','Tuzlar suda iyonlarına ayrışır: KCl → K⁺ + Cl⁻ (1 mol KCl, 2 mol iyon) · Na₂SO₄ → 2Na⁺ + SO₄²⁻ (1 mol, 3 mol iyon)')],
 'Aynı miktar suda, çözünen toplam tanecik (molekül ya da iyon) sayısı en çok olanın donma noktası en düşüktür.',
 dict(m='Üç ayrı kapta 500’er g saf suya aşağıdaki maddeler ilave edilip tamamen çözünmeleri sağlanıyor.\nI. kap: 0,1 mol glikoz (C₆H₁₂O₆)\nII. kap: 0,1 mol KCl\nIII. kap: 0,1 mol Na₂SO₄\n(Glikoz suda moleküller hâlinde; KCl ve Na₂SO₄ tamamen iyonlarına ayrışarak çözünmektedir.)\nBu çözeltilerin 1 atm dış basınçta donmaya başlama sıcaklıkları sırasıyla T₁, T₂ ve T₃ olduğuna göre bunlar arasındaki ilişki aşağıdakilerden hangisidir?',
  i='T₁, T₂ ve T₃ arasındaki sıralama.',ip=['Donma noktasını çözünen toplam tanecik sayısı belirler.','Tuzların her molü kaç mol iyon verir?','Tanecik sayısı arttıkça donma noktası yükselir mi, düşer mi?'],
  ad=[A('Tanecik sayısını bul','Donma noktasını molekül ve iyonların toplam sayısı etkiler.','glikoz: 0,1 mol · KCl: 0,1 + 0,1 = 0,2 mol · Na₂SO₄: 0,2 + 0,1 = 0,3 mol'),
      A('Etkiyi yorumla','Tanecik sayısı arttıkça donma noktası daha çok düşer.','tanecik: I < II < III'),
      A('Sıralamayı yaz','En az tanecikli çözeltinin donma noktası en yüksektir.','T₁ > T₂ > T₃')],
  d='T₁ > T₂ > T₃',y=[('T₁ = T₂ = T₃','Üçünde de 0,1 mol madde olduğu için eşit sanmışsın; iyonlaşma tanecik sayısını artırır.','b'),('T₃ > T₂ > T₁','Etkiyi ters yorumlamışsın; tanecik arttıkça donma noktası düşer.','i'),('T₂ > T₁ = T₃','KCl’nin donma noktasının en yüksek olduğunu düşünmek için dayanak yok.','d'),('T₁ > T₂ = T₃','İki tuzu eşit saymışsın; Na₂SO₄ daha çok iyon verir.','b')],pos='B'),
 dict(m='Üç ayrı kapta 1000’er g saf suya aşağıdaki maddeler ilave edilip tamamen çözünmeleri sağlanıyor.\nI. kap: 0,2 mol sakkaroz (C₁₂H₂₂O₁₁)\nII. kap: 0,1 mol CaCl₂\nIII. kap: 0,1 mol NaNO₃\n(Sakkaroz suda moleküller hâlinde; CaCl₂ ve NaNO₃ tamamen iyonlarına ayrışarak çözünmektedir.)\nBu çözeltilerin 1 atm dış basınçta donmaya başlama sıcaklıkları sırasıyla T₁, T₂ ve T₃ olduğuna göre bunlar arasındaki ilişki aşağıdakilerden hangisidir?',
  ip=['Donma noktasını çözünen toplam tanecik sayısı belirler.','CaCl₂ ve NaNO₃’ın her molü kaç mol iyon verir?','Tanecik sayıları eşitse donma noktaları da eşittir.'],
  bilgi=[B('Donma noktası alçalması','Suda çözünen tanecik sayısı arttıkça çözeltinin donma noktası saf suyunkinden daha çok düşer'),B('İyonlarına ayrışma','CaCl₂ → Ca²⁺ + 2Cl⁻ (1 mol CaCl₂, 3 mol iyon) · NaNO₃ → Na⁺ + NO₃⁻ (1 mol, 2 mol iyon)')],
  ad=[A('Tanecik sayısını bul','Donma noktasını molekül ve iyonların toplam sayısı etkiler.','sakkaroz: 0,2 mol · CaCl₂: 0,1 × 3 = 0,3 mol · NaNO₃: 0,1 × 2 = 0,2 mol'),
      A('Etkiyi yorumla','Tanecik sayısı en çok olan çözeltinin donma noktası en çok düşer.','tanecik: I = III < II'),
      A('Sıralamayı yaz','I ve III’ün donma noktası eşit ve CaCl₂’lü çözeltinin üstündedir.','T₁ = T₃ > T₂')],
  d='T₁ = T₃ > T₂',y=[('T₁ = T₂ = T₃','Üçünde de benzer mol miktarı gördüğün için eşit sanmışsın; CaCl₂ 3 mol iyon verir.','b'),('T₂ > T₁ = T₃','Etkiyi ters yorumlamışsın; tanecik çoksa donma noktası daha düşüktür.','i'),('T₁ > T₃ > T₂','Sakkaroz ile NaNO₃’ı farklı saymışsın; ikisi de 0,2 mol tanecik verir.','i'),('T₃ > T₁ > T₂','NaNO₃’ın iyonlarını sayıp sakkarozun 0,2 molünü eksik saymışsın.','b')],pos='E'),
 'koligatif: donma noktası','farklı madde ve mol sayıları, eşitlik durumu','çözünen tanecik sayısı')

# ---- 0005 zor: çok adımlı yüzde
for (M0,p,w,x,c) in [(140,20,40,20,40),(140,20,60,20,48)]:
    s0=Fr(M0*p,100); assert (s0+x)*100/(M0-w+x)==c
assert Fr(48*100,160)==30 and Fr(48*100,100)==48 and Fr(28*100,100)==28
K.Q('0005','kim-karisim-derisim','Buharlaştırma ve ekleme ile derişim değişimi','zor','Kütlece Yüzde Derişim','Buharlaştırma ve çözünen ekleme sonucu oluşan çözeltinin derişimini adım adım hesaplar.','hikâyeli',5,
 'Su buharlaştırıp çözünen eklemek','Eklenen çözünenin kütlesini toplam çözeltiye katmamak ya da buharlaşmayı unutmak.',
 [B('Kütlece yüzde derişim','100 g çözeltide çözünen kütlesidir. Örnek: %20’lik 150 g çözeltide 150 × 20/100 = 30 g çözünen vardır'),B('Buharlaşma ve ekleme','Buharlaşırken yalnız su gider (çözünen kalır). Çözünen eklenirse hem çözünen hem çözelti kütlesi artar')],
 'Her işlemden sonra çözünen ve çözelti kütlesini ayrı ayrı yaz; buharlaşırken yalnız çözelti kütlesi azalır.',
 dict(m='Kütlece %20’lik 140 g şekerli su çözeltisinden 40 g su buharlaştırılıyor. Ardından çözeltiye 20 g şeker ekleniyor ve şekerin tamamı çözünüyor.\nBuna göre son çözeltinin kütlece yüzde derişimi kaçtır?',
  i='Son çözeltinin kütlece yüzde derişimi.',ip=['İlk çözeltideki şeker kütlesini bul.','Buharlaşan su şekeri etkiler mi, çözelti kütlesini mi azaltır?','Eklenen şeker hem şeker hem çözelti kütlesine eklenir.'],
  ad=[A('İlk şeker kütlesi','Kütlece %20’lik 140 g çözeltide şeker vardır.','140 × 20/100 = 28 g şeker'),
      A('Buharlaşma','Yalnız su gider; şeker kütlesi değişmez.','çözelti: 140 − 40 = 100 g · şeker: 28 g'),
      A('Şeker ekleme','Eklenen şeker hem şekere hem çözeltiye katılır.','şeker: 28 + 20 = 48 g · çözelti: 100 + 20 = 120 g'),
      A('Yüzdeyi hesapla','Şeker kütlesi çözelti kütlesine bölünür.','48/120 × 100 = %40')],
  d='40',y=[('20','Hiçbir şey değişmemiş gibi ilk derişimi yazmışsın.','d'),('28','Eklenen şekeri unutup 28 g’ı 100 g’a bölmüşsün.','i'),('30','Buharlaşmayı hesaba katmamışsın: 48/160 = %30.','i'),('48','Eklenen 20 g şekeri çözelti kütlesine katmamışsın: 48/100.','i')],pos='D'),
 dict(m='Kütlece %20’lik 140 g tuzlu su çözeltisinden 60 g su buharlaştırılıyor. Ardından çözeltiye 20 g tuz ekleniyor ve tuzun tamamı çözünüyor.\nBuna göre son çözeltinin kütlece yüzde derişimi kaçtır?',
  ip=['İlk çözeltideki tuz kütlesini bul.','Buharlaşan su tuzu etkiler mi, çözelti kütlesini mi azaltır?','Eklenen tuz hem tuz hem çözelti kütlesine eklenir.'],
  ad=[A('İlk tuz kütlesi','Kütlece %20’lik 140 g çözeltide tuz vardır.','140 × 20/100 = 28 g tuz'),
      A('Buharlaşma','Yalnız su gider; tuz kütlesi değişmez.','çözelti: 140 − 60 = 80 g · tuz: 28 g'),
      A('Tuz ekleme','Eklenen tuz hem tuza hem çözeltiye katılır.','tuz: 28 + 20 = 48 g · çözelti: 80 + 20 = 100 g'),
      A('Yüzdeyi hesapla','Tuz kütlesi çözelti kütlesine bölünür.','48/100 × 100 = %48')],
  d='48',y=[('20','Hiçbir şey değişmemiş gibi ilk derişimi yazmışsın.','d'),('30','Buharlaşmayı hesaba katmamışsın: 48/160 = %30.','i'),('35','Eklenen tuzu unutup 28 g’ı 80 g’a bölmüşsün.','i'),('60','Eklenen 20 g tuzu çözelti kütlesine katmamışsın: 48/80.','i')],pos='D'),
 'buharlaştırma + ekleme','farklı kütleler, tuz','çözünen ve çözelti kütlesi ayrı izlenir')

# ---- 0006 zor: molarite karışımı
def cl(M1,V1,k1,M2,V2,k2): return (Fr(M1)*Fr(V1)*k1+Fr(M2)*Fr(V2)*k2)/(Fr(V1)+Fr(V2))
a_=cl(Fr(1,10),Fr(3,10),2,Fr(3,10),Fr(2,10),1); assert a_==Fr(24,100)
assert (Fr(1,10)*Fr(3,10)+Fr(3,10)*Fr(2,10))/Fr(1,2)==Fr(18,100) and (Fr(2,10)+Fr(3,10))/2==Fr(25,100) and (Fr(1,10)+Fr(3,10))/2==Fr(20,100)
b_=cl(Fr(2,10),Fr(2,10),2,Fr(1,10),Fr(3,10),3); assert b_==Fr(34,100)
assert (Fr(2,10)*Fr(2,10)+Fr(1,10)*Fr(3,10))/Fr(1,2)==Fr(14,100) and (Fr(4,10)+Fr(3,10))/2==Fr(35,100) and (Fr(2,10)+Fr(1,10))/2==Fr(15,100)
K.Q('0006','kim-karisim-molarite','Çözeltileri karıştırınca iyon derişimi','zor','Molar Derişim','İyonlaşan tuz çözeltilerini karıştırınca ortak iyonun derişimini hesaplar.','hikâyeli',5,
 'İki tuz çözeltisinde ortak iyon derişimi','Formüldeki iyon sayısını çarpmayı unutmak ve derişimlerin ortalamasını almak.',
 [B('Molar derişim (molarite)','1 L çözeltideki çözünen mol sayısıdır: M = n / V(L). Örnek: 0,2 M 500 mL çözeltide n = 0,2 × 0,5 = 0,1 mol çözünen vardır'),B('İyonlarına ayrışma','CaCl₂ → Ca²⁺ + 2Cl⁻: 1 mol CaCl₂ 2 mol Cl⁻ verir · NaCl → Na⁺ + Cl⁻: 1 mol NaCl 1 mol Cl⁻ verir')],
 'Ortak iyonun toplam mol sayısını toplam hacme böl; iyon sayısını formülden oku.',
 dict(m='0,1 M 300 mL CaCl₂ çözeltisi ile 0,3 M 200 mL NaCl çözeltisi karıştırılıyor.\n(Hacimlerin toplandığı ve tuzların tamamen iyonlarına ayrıştığı varsayılacaktır.)\nBuna göre karışımdaki Cl⁻ iyonlarının molar derişimi kaç M’dir?',
  i='Karışımdaki Cl⁻ derişimi.',ip=['Her çözeltideki çözünen mol sayısını n = M × V ile bul (V litre).','CaCl₂’ün 1 molü kaç mol Cl⁻ verir?','Toplam Cl⁻ molünü toplam hacme böl.'],
  ad=[A('Tuz mollerini bul','Mol sayısı molarite ile hacmin (L) çarpımıdır.','CaCl₂: 0,1 × 0,3 = 0,03 mol · NaCl: 0,3 × 0,2 = 0,06 mol'),
      A('Cl⁻ mollerini bul','CaCl₂ formül birimi başına 2 Cl⁻, NaCl 1 Cl⁻ verir.','CaCl₂’den: 0,03 × 2 = 0,06 mol · NaCl’den: 0,06 mol'),
      A('Toplamları bul','Cl⁻ molleri ve hacimler toplanır.','0,06 + 0,06 = 0,12 mol · 300 + 200 = 500 mL = 0,5 L'),
      A('Derişimi hesapla','Toplam mol toplam hacme bölünür.','0,12 / 0,5 = 0,24 M')],
  d='0,24 M',y=[('0,18 M','CaCl₂’ün 2 Cl⁻ verdiğini unutmuşsun: (0,03 + 0,06) / 0,5.','b'),('0,20 M','Çözeltilerin derişimlerinin ortalamasını almışsın: (0,1 + 0,3) / 2.','b'),('0,25 M','Cl⁻ derişimlerinin (0,2 ve 0,3) ortalamasını almışsın; hacimler eşit değil.','i'),('0,30 M','Yalnız NaCl çözeltisinin derişimini yazmışsın.','d')]),
 dict(m='0,2 M 200 mL MgCl₂ çözeltisi ile 0,1 M 300 mL AlCl₃ çözeltisi karıştırılıyor.\n(Hacimlerin toplandığı ve tuzların tamamen iyonlarına ayrıştığı varsayılacaktır.)\nBuna göre karışımdaki Cl⁻ iyonlarının molar derişimi kaç M’dir?',
  ip=['Her çözeltideki çözünen mol sayısını n = M × V ile bul (V litre).','MgCl₂ ve AlCl₃’ün 1 molü kaç mol Cl⁻ verir?','Toplam Cl⁻ molünü toplam hacme böl.'],
  bilgi=[B('Molar derişim (molarite)','1 L çözeltideki çözünen mol sayısıdır: M = n / V(L). Örnek: 0,2 M 500 mL çözeltide n = 0,2 × 0,5 = 0,1 mol çözünen vardır'),B('İyonlarına ayrışma','MgCl₂ → Mg²⁺ + 2Cl⁻ (1 mol MgCl₂, 2 mol Cl⁻) · AlCl₃ → Al³⁺ + 3Cl⁻ (1 mol AlCl₃, 3 mol Cl⁻)')],
  ad=[A('Tuz mollerini bul','Mol sayısı molarite ile hacmin (L) çarpımıdır.','MgCl₂: 0,2 × 0,2 = 0,04 mol · AlCl₃: 0,1 × 0,3 = 0,03 mol'),
      A('Cl⁻ mollerini bul','MgCl₂ başına 2 Cl⁻, AlCl₃ başına 3 Cl⁻ vardır.','MgCl₂’den: 0,04 × 2 = 0,08 mol · AlCl₃’ten: 0,03 × 3 = 0,09 mol'),
      A('Toplamları bul','Cl⁻ molleri ve hacimler toplanır.','0,08 + 0,09 = 0,17 mol · 200 + 300 = 500 mL = 0,5 L'),
      A('Derişimi hesapla','Toplam mol toplam hacme bölünür.','0,17 / 0,5 = 0,34 M')],
  d='0,34 M',y=[('0,14 M','Formüldeki Cl sayısını çarpmamışsın: (0,04 + 0,03) / 0,5.','b'),('0,15 M','Çözeltilerin derişimlerinin ortalamasını almışsın: (0,2 + 0,1) / 2.','b'),('0,17 M','Toplam mol sayısını hacme bölmeyi unutmuşsun.','d'),('0,35 M','Cl⁻ derişimlerinin (0,4 ve 0,3) ortalamasını almışsın; hacimler eşit değil.','i')]),
 'iyon derişimi karışımı','farklı tuzlar ve iyon sayıları','n = M × V; Cl⁻ toplamı / toplam hacim')
K.bitir(6)
