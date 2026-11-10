import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_c import *
P=Parti('dogainsan','Doğa ve İnsan','cog|Doğa ve İnsan',ders='TYT Coğrafya',idon='tytcog')
KY='ÖSYM 2018–2026 TYT Coğrafya (doğal sistemler, doğa–insan etkileşimi) · MEB 9. sınıf'
kart('K-CGDI-01','Doğal ve beşeri unsurlar','Doğal ortam doğada kendiliğinden bulunan unsurlardan, beşeri ortam insanın yaptıklarından oluşur.','İnsan yapımı bir unsuru (baraj gölü, köprü) doğal sanmak.','kolay','öncüllü',2,'cg-dogainsan-unsur','Doğal ve beşeri unsurları ayırma',KY)
kart('K-CGDI-02','İnsanın doğayı değiştirmesi','Etkileşimin yönü: doğa insanı etkiler (uyum), insan doğayı değiştirir (dönüştürme).','Doğal koşula uyumu, doğayı değiştirme sanmak.','orta','düz',3,'cg-dogainsan-yon','Etkileşimin yönünü belirleme',KY)
kart('K-CGDI-03','Doğal koşullara uyum','Konut, tarım ve geçim biçimi doğal koşullara göre biçimlenir.','Doğal koşulu dikkate almayan uygulamayı uyum örneği saymak.','orta','düz',3,'cg-dogainsan-uyum','Doğal koşul–insan faaliyeti ilişkisi',KY)
kart('K-CGDI-04','Etkileşim örneklerini sayma','Cümleleri tek tek yönüne göre ayırıp sayma.','Bir cümleyi yanlış gruba koymak; sayımı eksik yapmak.','orta','yeni nesil',4,'cg-dogainsan-say','Etkileşim yönüne göre sayım',KY)
KAV=B('Doğal ve beşeri unsurlar','Doğal ortam: iklim, rüzgâr, akarsu, bitki örtüsü, yer şekilleri. Beşeri ortam: insanın yaptıkları (baraj, köprü, yol, yerleşme). Örnek: akarsu doğal, üzerindeki köprü beşeridir')
YON=B('Etkileşimin yönü','Doğa → insan: doğal koşullar insanın konut, giyim, geçim ve yerleşmesini biçimlendirir. İnsan → doğa: insan ormanı keser, baraj yapar, bataklığı kurutur')
# 0001
tr={'I':True,'II':False,'III':True}; dg={k for k,v in tr.items() if v}
Q(P,'0001','K-CGDI-01','kolay','Doğal çevre unsurlarını beşeri unsurlardan ayırt eder.','öncüllü',2,
 'I. Akarsu vadisi\nII. Baraj gölü\nIII. Rüzgâr\nYukarıdakilerden hangileri doğal çevre unsurudur?',
 onc_opts(dg,[{'II'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}],{'Yalnız II':('Baraj gölünü doğal sanıp akarsu vadisi ve rüzgârı atlamak.','bilgi'),'I ve II':('Baraj gölünü doğal sayıp rüzgârı atlamak.','bilgi'),'II ve III':('Akarsu vadisinin doğal bir yer şekli olduğunu unutup baraj gölünü doğal saymak.','bilgi'),'I, II ve III':('İnsan yapımı baraj gölünü de doğal ortama katmak.','bilgi')}),
 lambda e:e==frozenset(dg),'Doğal çevre unsurları.',
 'Her unsurun insan tarafından yapılıp yapılmadığını sor.',[KAV],
 [A('Ayrımı hatırla','Doğada kendiliğinden oluşanlar doğal, insanın yaptıkları beşeridir.','doğal: kendiliğinden · beşeri: insan yapımı'),
  A('Öncülleri sına','Akarsu vadisi ve rüzgâr doğaldır. Baraj gölü, akarsuyun önüne insanın yaptığı bir setle oluşur.','I: doğal · II: beşeri · III: doğal'),
  A('Sonuç','Doğal çevre unsurları I ve III’tür.','I ve III')],
 'Kendiliğinden var olan unsur doğal, insanın yaptığı unsur beşeridir.','yeni unsur örnekleri',harf='C')
# 0002
yon={'Kutup çevresinde yaşayan toplulukların kalın kürk giysiler giymesi':'dI','Çöl vahalarında yerleşmelerin su kaynağı çevresinde toplanması':'dI','Ilıman iklimli kıyı ovalarında turizmin gelişmesi':'dI','Soğuk iklimlerde tarım ürünlerinin yılda bir kez yetiştirilmesi':'dI','Orman alanlarının açılarak tarım arazisine dönüştürülmesi':'iD'}
Q(P,'0002','K-CGDI-02','orta','İnsan–doğa etkileşiminde etkinin yönünü belirler.','düz',3,
 'Aşağıdakilerden hangisi, insanın doğal çevreyi değiştirmesine örnek olarak gösterilebilir?',
 [('Kutup çevresinde yaşayan toplulukların kalın kürk giysiler giymesi','dI','Giysi seçimi doğal koşula (soğuğa) uyumdur; doğayı değiştirmez.','bilgi'),
  ('Çöl vahalarında yerleşmelerin su kaynağı çevresinde toplanması','dI','Yerleşmenin su kaynağına bağlı olması doğanın insanı etkilemesidir.','bilgi'),
  ('Ilıman iklimli kıyı ovalarında turizmin gelişmesi','dI','İklimin insan faaliyetini biçimlendirmesidir; doğa değişmez.','bilgi'),
  ('Soğuk iklimlerde tarım ürünlerinin yılda bir kez yetiştirilmesi','dI','Ürün sayısını iklim sınırlar; insan doğayı değiştirmemiştir.','bilgi'),
  ('Orman alanlarının açılarak tarım arazisine dönüştürülmesi','iD',None,None)],
 lambda e:e=='iD','İnsanın doğayı değiştirdiği örnek.',
 'Önce her şıkta etkinin doğadan insana mı, insandan doğaya mı olduğuna bak.',[YON],
 [A('Yönü ayır','Doğal koşula uyum doğanın insanı etkilediğini gösterir. Doğayı değiştirme ise insanın doğaya müdahalesidir.','uyum: doğa → insan · değiştirme: insan → doğa'),
  A('Şıkları sına','Giysi, yerleşme yeri, turizm ve ürün sayısı doğal koşullara bağlıdır.','4 şıkta: doğa → insan'),
  A('Sonuç','Ormanı açıp tarla yapmak doğal ortamı değiştirir.','Orman → tarla: insan → doğa')],
 'İnsan doğayı değiştiriyorsa etki insandan doğaya doğrudur.','yönü ayırma',harf='E')
# 0003
Q(P,'0003','K-CGDI-03','orta','Doğal koşullar ile insan faaliyetleri arasındaki ilişkiyi yorumlar.','düz',3,
 'Aşağıdakilerden hangisi, doğal koşullara uyum örneği olarak gösterilemez?',
 [('Taşkın riski yüksek dere yataklarına konut yapılması','u0',None,None),
  ('Soğuk bölgelerde evlerin kalın duvarlı ve küçük pencereli yapılması','u1','Kalın duvar ve küçük pencere soğuktan korunmayı sağlar; doğal koşula uyum örneğidir.','bilgi'),
  ('Sıcak ve kurak çöllerde evlerin kalın duvarlı yapılması','u1','Kalın duvar sıcaktan korunmayı sağlar; uyum örneğidir.','bilgi'),
  ('Çok yağış alan yerlerde çatıların eğimli yapılması','u1','Eğimli çatı suyun akmasını sağlar; uyum örneğidir.','bilgi'),
  ('Kıyı kasabalarında balıkçılığın gelişmesi','u1','Denize kıyı olmak balıkçılığı doğurur; doğal koşula uyumdur.','bilgi')],
 lambda e:e=='u0','Uyum örneği olmayan durum.',
 'Her şıkta uygulamanın doğal koşuldan doğan bir sorunu çözüp çözmediğini düşün.',[YON],
 [A('Uyumu tanımla','Uyum, doğal koşulun getirdiği sınırlamaya göre davranmaktır.','uyum = koşula göre önlem'),
  A('Şıkları sına','Soğukta kalın duvar, sıcakta kalın duvar, eğimli çatı ve balıkçılık doğal koşula göre yapılır.','4 şık: uyum'),
  A('Sonuç','Dere yatağına konut yapmak taşkın riskini göz ardı eder.','Yatağa konut: uyum değil')],
 'Uyum doğal koşulun sorununa uygun önlem almaktır; riski yok saymak uyum değildir.','çeşitli uyum örnekleri',harf='A')
# 0004
C=[('Kuzey Avrupa’da uzun ve soğuk kışlar nedeniyle konutlarda ısı yalıtımına önem verilmesi','dI'),
 ('Akarsu üzerine baraj yapılarak elektrik enerjisi üretilmesi','iD'),
 ('Muson yağışlarının bol olduğu alanlarda çeltik tarımının yapılması','dI'),
 ('Bataklık alanların kurutularak tarım arazisine dönüştürülmesi','iD'),
 ('Yüksek dağlık alanlarda nüfusun seyrek olması','dI'),
 ('Kıyı kasabalarında balıkçılığın başlıca geçim kaynağı olması','dI')]
n=sum(1 for _,e in C if e=='dI'); assert n==4
metin='I. '+C[0][0]+'.\nII. '+C[1][0]+'.\nIII. '+C[2][0]+'.\nIV. '+C[3][0]+'.\nV. '+C[4][0]+'.\nVI. '+C[5][0]+'.\nYukarıdaki cümlelerden kaç tanesi, doğal çevrenin insan faaliyetlerini etkilediğine örnektir?'
Q(P,'0004','K-CGDI-04','orta','Doğa–insan etkileşimi örneklerini yönüne göre ayırıp sayar.','yeni nesil',4,metin,
 [('4',4,None,None),('1',1,'Üç doğa → insan cümlesini atlamak; yalnız bir cümleyi saymak.','dikkat'),('2',2,'Doğa → insan örneklerinin yarısını atlamak.','dikkat'),('3',3,'Bir doğa → insan cümlesini insan → doğa sanmak.','dikkat'),('5',5,'İnsanın doğaya müdahalesi olan bir cümleyi de saymak.','dikkat')],
 lambda e:e==n,'Doğa → insan yönündeki cümle sayısı.',
 'Her cümlede etkinin kaynağını bul: doğal koşul mu, insan eylemi mi?',[YON],
 [A('Yönü belirle','Doğal koşulun insan faaliyetini biçimlendirdiği cümleler sayılacak.','doğa → insan: sayılır'),
  A('Cümleleri ayır','I, III, V ve VI doğal koşula bağlıdır. II ve IV insanın doğaya müdahalesidir.','I, III, V, VI: doğa → insan · II, IV: insan → doğa'),
  A('Say','Doğa → insan yönündeki cümleler sayılır.','4 cümle')],
 'Sayma sorularında her cümleyi önce yönüne göre etiketle, sonra say.','altı cümleli sayım',sirala=int,harf='D')
bitir(P,'dogainsan','cog|Doğa ve İnsan','Doğa ve İnsan',zd={'kolay':1,'orta':3})
