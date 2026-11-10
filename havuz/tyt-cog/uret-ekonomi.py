import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_b import *
Q=Konu('ekonomi','Ekonomik Faaliyetler','cog|Ekonomik Faaliyetler',4)
Q.kart('K-CGEK-01','Faaliyet grupları','Birincil: doğadan doğrudan ürün alma; ikincil: işleme; üçüncül: hizmet.','Konserve üretimi gibi işlemeyi birincil saymak.','kolay','öncüllü',2,'cg-ekonomi-grup','Ekonomik faaliyet grupları')
Q.kart('K-CGEK-02','Doğal koşullar ve faaliyet','Geniş otlaklar hayvancılığı, kıyı balıkçılığı, karlı dağ kış turizmini destekler.','Koşulla çelişen faaliyeti seçmek.','kolay','düz',3,'cg-ekonomi-dogal','Doğal koşulların ekonomiye etkisi')
Q.kart('K-CGEK-03','Hayvancılık biçimleri','Entansif hayvancılık ahırda, yemle, denetimli ve verimlidir; ekstansif geniş meralarda, az masrafla yapılır.','İki biçimi karıştırmak.','orta','düz',3,'cg-ekonomi-hayvan','Entansif hayvancılık')
Q.kart('K-CGEK-04','Sektörel çalışan sayısı','Çalışan sayısı = toplam çalışan × sektör payı; ülkeler sayı ve oran açısından karşılaştırılır.','Yüzdeyi sayı sanmak.','zor','tablo',4,'cg-ekonomi-sektor','Sektörlere göre çalışan dağılımı')
# ---- 0001
st=[('Bir köyde arıcılık yapılması',True,'arıcılık doğadan doğrudan ürün almaktır'),
    ('Bir fabrikada konserve üretilmesi',False,'üretimi işlemek ikincil faaliyettir'),
    ('Bir kıyı kasabasında balık avcılığı yapılması',True,'avcılık doğadan ürün almadır'),
    ('Bir otelde konukların karşılanması',False,'hizmet üçüncül faaliyettir')]
op,dg=oncul(st,['Yalnız I','Yalnız III','I ve III','II ve IV','I, II ve III'],'C'); assert dg=={'I','III'}
Q.S('0001','K-CGEK-01','kolay','Verilen faaliyetleri birincil, ikincil ve üçüncül gruplara ayırır.',
 metin_oncul('Aşağıda bazı ekonomik faaliyetler verilmiştir.',st,'Bu faaliyetlerden hangileri birincil ekonomik faaliyet grubundadır?'),op,'C',
 'Birincil faaliyetlerin belirlenmesi.','Faaliyetin doğadan ürün alma mı, ürünü işleme mi, hizmet mi olduğuna bak.',
 [B('Ekonomik faaliyet grupları','Birincil: doğadan doğrudan ürün alma (tarım, hayvancılık, balıkçılık, madencilik, ormancılık) · İkincil: ürünü işleme (sanayi) · Üçüncül: hizmet (ticaret, ulaşım, turizm, eğitim)')],
 [A('Grupları hatırla','Birincil faaliyet, ürünün doğadan doğrudan alınmasıdır.','birincil = doğadan alma'),
  A('Örnekleri sına','Arıcılık ve avcılık doğadan ürün alır; konserve üretimi işlemedir; otel hizmettir.','I: birincil · II: ikincil · III: birincil · IV: üçüncül'),
  A('Sonuç','Birincil faaliyetler I ve III’tür.','I ve III')],
 'Ham maddeyi doğadan alma birincil, işleme ikincil, hizmet üçüncüldür.','yeni faaliyet örnekleri')
# ---- 0002
Q.S('0002','K-CGEK-02','kolay','Doğal koşullarla ekonomik faaliyet arasındaki ilişkiyi yorumlar.',
 'Aşağıdakilerden hangisi, bir bölgedeki ekonomik faaliyetin o bölgenin doğal koşullarıyla açıklanabileceğine örnektir?',
 [('Geniş otlakların bulunduğu yaylalarda hayvancılığın yapılması',True,'',''),('Yağışın çok az olduğu çöl alanlarında pirinç tarımının geniş yer tutması',False,'Pirinç çok su ister; çölde bu doğal koşula uygun değildir.','bilgi'),('Kıyıdan uzak yüksek dağlarda deniz ticaretinin gelişmesi',False,'Deniz ticareti kıyı ve liman ister; yüksek dağda doğal koşullar buna uymaz.','bilgi'),('Hiç kar yağmayan ılıman alanlarda kış turizminin gelişmesi',False,'Kış turizmi kar gerektirir; kar yoksa gelişemez.','bilgi'),('Maden yatağı bulunmayan bir alanda madenciliğin yaygın olması',False,'Madencilik, yeraltı kaynağı bulunan yerlerde yapılır.','dikkat')],'A',
 'Doğal koşulla uyumlu faaliyet.','Faaliyetin hangi doğal koşulu gerektirdiğini ve o koşulun örnekte var olup olmadığını sor.',
 [B('Doğal koşullar ve faaliyet','Otlak ve mera: hayvancılık · Kıyı ve deniz: balıkçılık, deniz taşımacılığı · Karlı dağ: kış turizmi · Yeraltı kaynağı: madencilik · Bol su: pirinç gibi sulu tarım')],
 [A('Koşulu bul','Her faaliyetin dayandığı doğal koşulu belirle.','hayvancılık: otlak · pirinç: su · kış turizmi: kar'),
  A('Şıkları sına','B, C, D ve E’de gerekli doğal koşul yoktur.','B, C, D, E: koşul yok'),
  A('Sonuç','Yalnız A’da faaliyet doğal koşula uyar.','A')],
 'Faaliyetin ihtiyaç duyduğu doğal koşulun alanda bulunup bulunmadığını kontrol et.','doğal koşul–faaliyet eşleşmesi')
# ---- 0003
Q.S('0003','K-CGEK-03','orta','Entansif hayvancılığın özelliğini ekstansif hayvancılıktan ayırır.',
 'Entansif hayvancılık yönteminin kullanıldığı bir işletmeyle ilgili aşağıdakilerden hangisi söylenebilir?',
 [('Hayvanlar geniş meralarda serbestçe otlatılır.',False,'Geniş meralarda otlatma ekstansif hayvancılığın özelliğidir.','bilgi'),('Üretim, az işgücü ve düşük masrafla yapılır; verim düşüktür.',False,'Bu özellikler ekstansif hayvancılığa aittir.','bilgi'),('Üretim doğal otlakların genişliğine bağlıdır.',False,'Entansif hayvancılıkta yem hazırlanır, doğal otlağa bağımlılık azdır.','bilgi'),('Hayvanlar ahırda, yemle ve veteriner denetiminde beslenir; birim başına verim yüksektir.',True,'',''),('Hayvancılık yalnızca mevsimlik olarak yaylalarda yapılır.',False,'Yaylada mevsimlik otlatma, entansif değil ekstansif yönteme yakındır.','dikkat')],'D',
 'Entansif hayvancılığın özelliği.','Entansif, “yoğun” anlamına gelir; az alanda çok emek ve yemle üretim yapılır.',
 [B('Hayvancılık yöntemleri','Entansif: ahırda, bilinçli beslenme, veteriner bakımı, verim yüksek, az alan · Ekstansif: geniş meralarda otlatma, az masraf, verim düşük')],
 [A('Yöntemi tanı','Entansif hayvancılık yoğun bakımla az alanda yapılır.','entansif = ahır + yem + bakım'),
  A('Şıkları sına','A, B ve C geniş mera, düşük masraf ve doğal otlağa bağımlılığı anlatır; E mevsimlik yayla kullanımıdır.','A, B, C, E: ekstansif'),
  A('Sonuç','Yalnız D entansif hayvancılığı anlatır.','D')],
 'Ahır, yem ve bakım varsa entansif; geniş mera ve az masraf varsa ekstansiftir.','entansif–ekstansif ayrımı')
# ---- 0004
V={'X':(8000000,50,20,30),'Y':(20000000,10,30,60),'Z':(5000000,4,26,70)}
for k,(t,a,b,c) in V.items(): assert a+b+c==100
n=lambda k,i:V[k][0]*V[k][i]//100
assert [n('X',1),n('Y',1),n('Z',1)]==[4000000,2000000,200000]
assert [n('X',3),n('Y',3),n('Z',3)]==[2400000,12000000,3500000]
assert n('Z',2)==1300000 and n('X',2)==1600000 and n('Y',2)==6000000 and n('Y',2)==3*n('Y',1)
st=[('Birincil faaliyette çalışan sayısı en fazla olan ülke X’tir.',True,'X: 4 000 000, Y: 2 000 000, Z: 200 000'),
    ('Üçüncül faaliyette çalışan sayısı en fazla olan ülke Y’dir.',True,'X: 2 400 000, Y: 12 000 000, Z: 3 500 000'),
    ('İkincil faaliyette çalışan sayısı Z’de X’ten fazladır.',False,'Z: 1 300 000, X: 1 600 000; Z daha azdır'),
    ('Y’de ikincil faaliyette çalışan sayısı, birincil faaliyette çalışan sayısının 2 katıdır.',False,'6 000 000 ÷ 2 000 000 = 3 kattır')]
op,dg=oncul(st,['Yalnız I','I ve II','I ve III','II ve IV','III ve IV'],'B'); assert dg=={'I','II'}
Q.S('0004','K-CGEK-04','zor','Sektörlere göre çalışan yüzdelerinden çalışan sayılarını hesaplayıp ülkeleri karşılaştırır.',
 'Aşağıdaki tabloda üç ülkenin toplam çalışan sayısı ve çalışanların ekonomik faaliyet gruplarına dağılımı verilmiştir. Veriler kurgusaldır.\nÜlke – Toplam çalışan – Birincil – İkincil – Üçüncül\nX – 8 000 000 – %50 – %20 – %30\nY – 20 000 000 – %10 – %30 – %60\nZ – 5 000 000 – %4 – %26 – %70\nBu verilere göre\nI. '+st[0][0]+'\nII. '+st[1][0]+'\nIII. '+st[2][0]+'\nIV. '+st[3][0]+'\nifadelerinden hangileri doğrudur?',op,'B',
 'Doğru ifadelerin belirlenmesi.','Yüzdelerin kendisi değil, toplam çalışanla çarpılmış sayılar karşılaştırılmalıdır.',
 [B('Yüzdeden sayıya','Grup sayısı = toplam çalışan × yüzde ÷ 100. Örnek: 1000 çalışanın %20’si ikincil grupta ise 1000 × 20 ÷ 100 = 200 kişi ikincil faaliyette çalışır.')],
 [A('Birincil sayılar','Toplam çalışanı birincil yüzdesiyle çarp.','X: 4 000 000 · Y: 2 000 000 · Z: 200 000'),
  A('İkincil ve üçüncül','Aynı işlemi iki grup için yap.','ikincil: X 1 600 000, Y 6 000 000, Z 1 300 000 · üçüncül: X 2 400 000, Y 12 000 000, Z 3 500 000'),
  A('İfadeleri sına','I ve II doğrudur; III’te Z, X’ten azdır; IV’te oran 3’tür.','I: doğru · II: doğru · III: yanlış · IV: yanlış'),
  A('Sonuç','Doğru ifadeler I ve II’dir.','I ve II')],
 'Ülkeleri karşılaştırırken yüzde değil, yüzdenin toplam çalışanla çarpımı olan sayıya bak.','kurgusal tablo; sayılar kodla',kalip='tablo')
Q.zd={'kolay':2,'orta':1,'zor':1}
Q.bitir()
