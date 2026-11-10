import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_c import *
P=Parti('cevre','Çevre ve Toplum','cog|Çevre ve Toplum',ders='TYT Coğrafya',idon='tytcog')
KY='ÖSYM 2018–2026 TYT Coğrafya (çevre sorunları, kaynaklar) · MEB 10. sınıf'
kart('K-CGCV-01','Yenilenebilir ve yenilenemez kaynaklar','Kullanıldıkça tükenen kaynaklar yenilenemez, kendini yenileyenler yenilenebilirdir.','Jeotermal ve akarsuyu yenilenemez saymak.','kolay','düz',2,'cg-cevre-kaynak','Enerji kaynaklarını ayırma',KY)
kart('K-CGCV-02','Küresel ısınmanın sonuçları','Sera gazları artınca sıcaklık yükselir; buzullar erir, deniz seviyesi artar. Ozon incelmesi ayrı bir sorundur.','Ozon incelmesini küresel ısınmanın sonucu saymak.','orta','öncüllü',3,'cg-cevre-isinma','Küresel ısınma ve sonuçları',KY)
kart('K-CGCV-03','Çevre sorunu ve nedeni','Her çevre sorununun başlıca nedeni bellidir: asit yağmuru–SO₂, ozon–CFC, erozyon–bitki tahribi.','Sera etkisini orman artışına bağlamak.','kolay','düz',3,'cg-cevre-neden','Çevre sorunu–neden eşleştirme',KY)
kart('K-CGCV-04','Enerji payı hesabı','Toplam üretim sabitken hedef payın GW karşılığı bulunup mevcut üretimden çıkarılır.','Yüzdeyi doğrudan GW sanmak; yenilenebilir kaynakları yanlış gruplamak.','zor','tablo',4,'cg-cevre-pay','Yenilenebilir enerji payı hesabı',KY)
KAY=B('Kaynak türleri','Yenilenebilir: güneş, rüzgâr, akarsu, jeotermal, biyokütle (kendini yeniler). Yenilenemez: kömür, petrol, doğal gaz (milyonlarca yılda oluşur, tükenir)')
SER=B('Sera gazı ve küresel ısınma','Sera gazları (CO₂, metan) arttıkça atmosfer fazla ısı tutar, ortalama sıcaklık yükselir. Sonuçları: buzulların erimesi, deniz seviyesinin yükselmesi, alçak kıyıların su altında kalma riski. Ozon incelmesi küresel ısınmanın sonucu değil, başlıca CFC gazlarının yol açtığı ayrı bir sorundur.')
SOR=B('Çevre sorunları ve nedenleri','Asit yağmuru: fosil yakıtlardan çıkan SO₂ ve azot oksit · Ozon incelmesi: CFC · Erozyon: bitki örtüsünün tahribi · Su kirliliği: sanayi ve evsel atıklar · Sera etkisinin artması: fosil yakıt kullanımı ve ormansızlaşma')
PAY=B('Yüzde pay','Pay (%) = parça ÷ toplam × 100. Toplam 100 GW iken %50 pay 50 GW eder')
# 0001
Q(P,'0001','K-CGCV-01','kolay','Yenilenebilir ve yenilenemez enerji kaynaklarını ayırt eder.','düz',2,
 'Aşağıdakilerden hangisi yenilenemez enerji kaynağıdır?',
 [('Kömür','y',None,None),('Rüzgâr','n','Rüzgâr tükenmez; yenilenebilir kaynaktır.','bilgi'),('Güneş','n','Güneş enerjisi tükenmez; yenilenebilir kaynaktır.','bilgi'),('Jeotermal','n','Yer ısısı sürekli yenilenir; yenilenebilir kaynak sayılır.','bilgi'),('Akarsu','n','Akarsuyun enerjisi yağışla sürekli yenilenir; yenilenebilirdir.','bilgi')],
 lambda e:e=='y','Yenilenemez kaynak.',
 'Kullanıldıkça tükenip yeniden oluşması çok uzun süren kaynağı seç.',[KAY],
 [A('Ayrımı hatırla','Kendini kısa sürede yenileyen kaynaklar yenilenebilirdir. Milyonlarca yılda oluşan fosil kaynaklar yenilenemezdir.','fosil yakıt: yenilenemez'),
  A('Şıkları sına','Rüzgâr, güneş, jeotermal ve akarsu sürekli yenilenir.','4 şık: yenilenebilir'),
  A('Sonuç','Kömür fosil yakıttır ve tükenir.','Kömür: yenilenemez')],
 'Fosil yakıtlar (kömür, petrol, doğal gaz) yenilenemez kaynaklardır.','yenilenebilir şık kümesi',harf='A')
# 0002
tr={'I':False,'II':True,'III':True}; dg={k for k,v in tr.items() if v}
Q(P,'0002','K-CGCV-02','orta','Küresel ısınmanın sonuçlarını diğer çevre sorunlarından ayırır.','öncüllü',3,
 'Sera gazlarındaki artış nedeniyle hızlanan küresel ısınmanın sonuçları arasında\nI. ozon tabakasının incelmesi,\nII. buzulların erimesi ve deniz seviyesinin yükselmesi,\nIII. alçak kıyı yerleşimlerinin su altında kalma riskinin artması\nolaylarından hangileri yer alır?',
 onc_opts(dg,[{'I'},{'III'},{'I','II'},{'II','III'},{'I','II','III'}],{'Yalnız I':('Ozon incelmesini küresel ısınmanın sonucu sanmak; ozon incelmesi CFC gazlarından olur.','bilgi'),'Yalnız III':('Buzulların erimesinin de küresel ısınmanın sonucu olduğunu atlamak.','dikkat'),'I ve II':('Ozon incelmesini sonuç sayıp kıyıların su altında kalma riskini atlamak.','bilgi'),'I, II ve III':('Ozon incelmesini de küresel ısınmaya bağlamak.','bilgi')}),
 lambda e:e==frozenset(dg),'Küresel ısınmanın sonuçları.',
 'Ozon incelmesinin nedenini küresel ısınmanın nedeniyle karşılaştır.',[SER],
 [A('Nedeni hatırla','Küresel ısınma sera gazlarının artmasıyla olur. Ozon incelmesi ise başlıca CFC gazlarından kaynaklanan ayrı bir sorundur; küresel ısınmanın sonucu değildir.','ısınma: sera gazı · ozon: CFC'),
  A('Öncülleri sına','Sıcaklık artınca buzullar erir, deniz seviyesi yükselir ve alçak kıyılar tehlikeye girer.','I: hayır · II: evet · III: evet'),
  A('Sonuç','Küresel ısınmanın sonuçları II ve III’tür.','II ve III')],
 'Ozon incelmesi küresel ısınmanın sonucu değildir; ayrı bir sorundur (başlıca nedeni CFC). Küresel ısınmanın sonuçları buzul erimesi, deniz seviyesi yükselmesi ve kıyıların su altında kalma riskidir.','ozon–ısınma ayrımı',harf='D')
# 0003
Q(P,'0003','K-CGCV-03','kolay','Çevre sorunlarını başlıca nedenleriyle eşleştirir.','düz',3,
 'Aşağıdakilerden hangisinde çevre sorunu ile bu soruna yol açan başlıca neden yanlış eşleştirilmiştir?',
 [('Asit yağmurları – Fosil yakıtlardan çıkan kükürt dioksit ve azot oksitler','d','Doğru eşleştirme.','bilgi'),
  ('Ozon tabakasının incelmesi – CFC içeren gazların kullanımı','d','Doğru eşleştirme.','bilgi'),
  ('Sera etkisinin artması – Orman alanlarının genişlemesi','x',None,None),
  ('Toprak erozyonu – Bitki örtüsünün tahrip edilmesi','d','Doğru eşleştirme.','bilgi'),
  ('Su kirliliği – Sanayi atıklarının akarsulara verilmesi','d','Doğru eşleştirme.','bilgi')],
 lambda e:e=='x','Yanlış eşleştirme.',
 'Orman alanlarının karbondioksiti tutup tutmadığını düşün.',[SOR],
 [A('Eşleştirmeleri hatırla','Her sorunun bilinen bir başlıca nedeni vardır.','asit yağmuru–SO₂ · ozon–CFC · erozyon–bitki tahribi · su kirliliği–atık'),
  A('Şıkları sına','A, B, D ve E bu bilgilerle uyumludur.','4 şık: doğru'),
  A('Sonuç','Ormanlar karbondioksit tutar; genişlemeleri sera etkisini azaltır. Orman azalması etkiyi artırır.','C: yanlış')],
 'Orman alanlarının azalması sera etkisini artırır, genişlemesi azaltır.','çevre sorunu–neden',harf='C')
# 0004
U=dict(Kömür=40,**{'Doğal gaz':30},Hidroelektrik=20,Rüzgâr=6,Güneş=4)
top=sum(U.values()); yen=U['Hidroelektrik']+U['Rüzgâr']+U['Güneş']; hedef=top*50//100
assert top==100 and yen==30 and hedef==50 and hedef-yen==20 and top-yen==70 and 40-30==10
tablo='\n'.join(f'{k} | {v}' for k,v in U.items())
Q(P,'0004','K-CGCV-04','zor','Enerji üretim tablosundan yenilenebilir kaynakların payını yorumlar.','tablo',4,
 'Bir ülkenin elektrik üretiminde kullanılan kaynaklar ve üretim miktarları (GW) aşağıdaki tabloda verilmiştir.\nKaynak | Üretim (GW)\n'+tablo+'\nToplam üretim aynı kalmak koşuluyla yenilenebilir kaynakların payının %50’ye çıkarılması için yenilenebilir kaynaklardan yapılan üretim kaç GW artırılmalıdır?',
 [('20','d',None,None),('10','y','Hedef payı %40 okuyup 40 − 30 = 10 bulmak.','dikkat'),('30','y','Mevcut yenilenebilir üretimi (30 GW) artış miktarı sanmak.','dikkat'),('50','y','Hedef payı (%50) doğrudan GW olarak yazmak; farkı almamak.','islem'),('70','y','Yenilenemez kaynakların toplamını (70 GW) artış sanmak.','dikkat')],
 lambda e:e=='d','Yenilenebilir üretimdeki artış (GW).',
 'Önce hangi kaynakların yenilenebilir olduğunu belirle, sonra hedef payın GW karşılığını bul.',[KAY,PAY],
 [A('Mevcut yenilenebilir','Hidroelektrik, rüzgâr ve güneş yenilenebilirdir. Kömür ve doğal gaz yenilenemezdir.','20 + 6 + 4 = 30 GW'),
  A('Hedef üretim','Toplam 100 GW; hedef pay %50.','100 × 50 ÷ 100 = 50 GW'),
  A('Artış miktarı','Hedeften mevcut üretim çıkarılır.','50 − 30 = 20 GW')],
 'Pay hedeflerinde önce hedefin miktarını bul, sonra mevcut miktarı çıkar.','toplam üretim sabit, hedef pay %50',sirala=int,harf='B')
bitir(P,'cevre','cog|Çevre ve Toplum','Çevre ve Toplum',zd={'kolay':2,'orta':1,'zor':1})
