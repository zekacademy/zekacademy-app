import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_b import *
Q=Konu('yerlesme','Yerleşme','cog|Yerleşme',4)
Q.kart('K-CGYR-01','Kent yerleşmesi','Kentte nüfusun çoğu sanayi, ticaret ve hizmette çalışır; kırda tarım ve hayvancılık ağır basar.','Kırsal özellikleri kente yazmak.','kolay','düz',2,'cg-yerlesme-tur','Kent yerleşmesinin özellikleri')
Q.kart('K-CGYR-02','Yer seçimi etkenleri','Su, tarıma elverişli arazi, ulaşım ve güvenlik yerleşmeyi çeker; afet riski caydırır.','Afet riskini avantaj saymak.','orta','öncüllü',3,'cg-yerlesme-yer','Yerleşme yeri seçimini etkileyen etkenler')
Q.kart('K-CGYR-03','Kır yerleşmesinin biçimi','Yağışlı, bol sulu, engebeli ve ormanlık yerlerde dağınık; suyun kıt ve tek kaynaktan sağlandığı düzlüklerde toplu yerleşme görülür.','Dağınık ve toplu koşullarını ters eşleştirmek.','orta','hikâyeli',3,'cg-yerlesme-bicim','Dağınık ve toplu kır yerleşmesi')
Q.kart('K-CGYR-04','Kentleşme oranı','Kentleşme oranı = kent nüfusu ÷ toplam nüfus × 100; iki tarihte hem toplam hem oran değişir.','Oran farkını nüfus artışı sanmak.','zor','tablo',4,'cg-yerlesme-kentlesme','Kentleşme oranı ve nüfus değişimi')
# ---- 0001
Q.S('0001','K-CGYR-01','kolay','Kent yerleşmesinin ayırt edici özelliğini belirler.',
 'Aşağıdakilerden hangisi kent yerleşmelerinin özelliklerinden biridir?',
 [('Nüfusun büyük bölümünün tarım ve hayvancılıkla geçinmesi',False,'Bu, kır yerleşmelerinin özelliğidir.','bilgi'),('Nüfusun büyük bölümünün sanayi, ticaret ve hizmet kollarında çalışması',True,'',''),('Evlerin arasında geniş tarla ve bahçelerin yer alması',False,'Bahçeli ve tarlalı düzen kırsal yerleşmeye aittir.','bilgi'),('Yerleşmenin yaylacılık amacıyla yılın yalnız birkaç ayında kullanılması',False,'Mevsimlik kullanım, geçici kır yerleşmesi (yayla) özelliğidir.','bilgi'),('Nüfus yoğunluğunun çok düşük olması',False,'Kentlerde yoğunluk yüksektir.','dikkat')],'B',
 'Kent yerleşmesinin özelliği.','Kentte insanların ne iş yaptığını ve nüfusun yoğunluğunu düşün.',
 [B('Kır ve kent','Kır yerleşmesi: nüfus az, geçim tarım ve hayvancılık, bahçeli ev düzeni · Kent yerleşmesi: nüfus çok, geçim sanayi, ticaret ve hizmet')],
 [A('Ayrımı hatırla','Kentte geçim tarım dışı kollardan sağlanır.','kent: sanayi, ticaret, hizmet'),
  A('Şıkları sına','A, C ve D kır ve yayla özellikleridir; E’de yoğunluk kentte yüksektir.','A, C, D, E: kır'),
  A('Sonuç','Yalnız B kent özelliğidir.','B')],
 'Geçim kolu tarımsa kır, sanayi ve hizmetse kenttir.','kır–kent ayrımı')
# ---- 0002
st=[('Akarsu ve kaynak gibi su kaynaklarına yakın olma',True,'su, yaşamın temel ihtiyacıdır'),
    ('Tarıma elverişli verimli arazinin bulunması',True,'geçim için arazi gerekir'),
    ('Sel ve heyelan riskinin yüksek olması',False,'afet riski yerleşmeyi caydırır, avantaj sağlamaz'),
    ('Yolların kesiştiği noktada bulunma',True,'ulaşım kolaylığı yerleşmeyi büyütür')]
op,dg=oncul(st,['Yalnız I','I ve II','II ve III','III ve IV','I, II ve IV'],'E'); assert dg=={'I','II','IV'}
Q.S('0002','K-CGYR-02','orta','Yerleşme yerinin seçiminde avantaj sağlayan etkenleri belirler.',
 metin_oncul('Bir yerleşmenin kurulacağı yer belirlenirken',st,'özelliklerinden hangileri o yer için avantaj sayılır?'),op,'E',
 'Avantaj sağlayan özelliklerin belirlenmesi.','Her özelliğin yerleşmeyi kolaylaştırıp kolaylaştırmadığını sor.',
 [B('Yerleşme yeri seçimi','Çeken etkenler: su, verimli arazi, ılıman iklim, ulaşım kolaylığı, güvenlik · Caydıran etkenler: sel, heyelan, deprem riski, aşırı engebe')],
 [A('Ölçütü belirle','Yaşamı ve geçimi kolaylaştıran özellikler avantajdır.','avantaj = su, arazi, ulaşım'),
  A('Öncülleri sına','I, II ve IV avantaj sağlar; III afet riskidir, caydırır.','I: evet · II: evet · III: hayır · IV: evet'),
  A('Sonuç','Avantajlar I, II ve IV’tür.','I, II ve IV')],
 'Yerleşmeyi kolaylaştıran etkenler çeker, afet riski ve engebe caydırır.','yerleşme avantajları')
# ---- 0003
Q.S('0003','K-CGYR-03','orta','Dağınık yerleşmenin görüldüğü doğal koşulları belirler.',
 'Dağınık yerleşme, evlerin birbirinden uzakta, arazi içine serpiştirilmiş olduğu kır yerleşme biçimidir.\nBuna göre aşağıdaki köylerden hangisinde dağınık yerleşme görülmesi beklenir?',
 [('Yağışın bol, suyun her yerde bulunduğu, engebeli ve ormanlık bir yamaçtaki köy',True,'',''),('Suyun kıt olduğu, düz bir plato üzerindeki köy',False,'Su kıtlığı evleri su kaynağı çevresinde toplar; toplu yerleşme görülür.','bilgi'),('Suyun tek kaynaktan sağlandığı geniş bir bozkır köyü',False,'Tek su kaynağı çevresinde evler toplanır.','bilgi'),('Yazın akarsuyun kuruduğu, suyun yalnız tek bir çeşmeden alındığı düz bir ova köyü',False,'Su tek çeşmeden sağlandığı için evler çeşme çevresinde toplanır; toplu yerleşme görülür.','dikkat'),('Suyun yalnız bir kuyudan alındığı bir vaha köyü',False,'Tek kuyu çevresinde evler sık dizilir; toplu yerleşmedir.','bilgi')],'A',
 'Dağınık yerleşme beklenen köy.','Evlerin birbirinden uzak durabilmesi için suyun ve arazinin nasıl olması gerektiğini düşün.',
 [B('Dağınık ve toplu yerleşme','Dağınık: su her yerde bulunur, yağış fazladır, arazi engebeli ve ormanlıktır (ör. Karadeniz) · Toplu: su kıt ya da tek kaynaktan sağlanır, arazi düzdür (ör. İç Anadolu bozkırı)')],
 [A('Koşulları hatırla','Dağınıklık için su her yerde bulunmalı; toplu yerleşmede ise su kaynağı çevresinde toplanılır.','su bol → dağınık · su kıt → toplu'),
  A('Şıkları sına','B, C, D ve E’de su kıt ya da tek kaynaktandır; evler o kaynağa yakın toplanır.','B, C, D, E: toplu'),
  A('Sonuç','Bol sulu, yağışlı, engebeli yamaç köyünde evler dağınık kurulur.','A')],
 'Su her yerdeyse dağınık, su tek yerdeyse toplu yerleşme olur.','dağınık–toplu eşleştirmesi')
# ---- 0004
t0=(8000000,Fr(40,100)); t1=(12000000,Fr(65,100))
kent0=t0[0]*t0[1]; kent1=t1[0]*t1[1]; kir0=t0[0]-kent0; kir1=t1[0]-kent1
assert kent0==3200000 and kent1==7800000 and kir0==4800000 and kir1==4200000 and kent1-kent0==4600000
assert kir0-kir1==600000 and (t1[1]-t0[1])*t1[0]==3000000
Q.S('0004','K-CGYR-04','zor','Kentleşme oranından kent nüfusunu bulup iki tarihi karşılaştırır.',
 'Kentleşme oranı, kent nüfusunun toplam nüfusa bölünüp 100 ile çarpılmasıyla bulunur. Kurgusal bir ülkenin iki yıla ait verileri aşağıdaki tabloda verilmiştir.\nYıl – Toplam nüfus – Kentleşme oranı\n2000 – 8 000 000 – %40\n2020 – 12 000 000 – %65\nBuna göre bu ülkede 2000–2020 arasında kent nüfusu kaç kişi artmıştır?',
 [('600 000',False,'Kırsal nüfusun azalışını (4 800 000 − 4 200 000) bulmuş; kent artışı sorulmuştur.','dikkat'),('3 000 000',False,'Oran farkını (25 puan) 2020 toplam nüfusuyla çarpmış; iki yılın kent nüfusunu ayrı hesaplamamış.','islem'),('4 600 000',True,'',''),('4 800 000',False,'2000 yılındaki kırsal nüfusu (4 800 000) kent artışı sanmış.','dikkat'),('7 800 000',False,'2020 kent nüfusunu bulup 2000 kent nüfusunu çıkarmamış.','dikkat')],'C',
 'Kent nüfusunun artış miktarı.','Her yıl için önce oranı kullanarak kent nüfusunu bul; sonra iki yılı karşılaştır.',
 [B('Kentleşme oranı','Kentleşme oranı = kent nüfusu ÷ toplam nüfus × 100. Kent nüfusu = toplam nüfus × oran ÷ 100. Örnek: 1000 kişilik yerde oran %30 ise kent nüfusu 300 kişidir.')],
 [A('2000 yılı kent nüfusu','Toplam nüfusun %40’ı kentte yaşar.','8 000 000 × 40 ÷ 100 = 3 200 000'),
  A('2020 yılı kent nüfusu','Toplam nüfusun %65’i kentte yaşar.','12 000 000 × 65 ÷ 100 = 7 800 000'),
  A('Artışı bul','Sonraki kent nüfusundan önceki kent nüfusunu çıkar.','7 800 000 − 3 200 000 = 4 600 000'),
  A('Şıkları ele','600 000 kırsal azalışı, 4 800 000 ise 2000’deki kırsal nüfustur.','C: 4 600 000')],
 'Oran verilmişse önce her tarih için sayıya çevir; oran farkı sayı farkı değildir.','kurgusal tablo; oran→sayı',kalip='tablo')
Q.bitir()
