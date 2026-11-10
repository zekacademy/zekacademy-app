import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim as H
from _hafif_kim import *
H.KONU='Periyodik Sistem'
P=Parti('periyodik','Periyodik Sistem','kim|Periyodik Sistem',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (periyodik sistem, periyodik özellikler) · MEB 9. sınıf'
kart('K-PRDK-01','Periyot ve grup bulma','Elektron dizilimindeki katman sayısı periyodu, son katmandaki elektron sayısı A grubunu verir.','Periyot ile grup numarasını karıştırmak.','kolay','düz',2,'kim-pr-yer','Atom numarasından periyot ve grup',KY)
kart('K-PRDK-02','Atom yarıçapı sıralaması','Aynı grupta aşağı inildikçe, aynı periyotta sağa gidildikçe azalır; katman sayısı belirleyicidir.','Katman sayısını hesaba katmadan yalnız atom numarasına bakmak.','orta','düz',3,'kim-pr-yaricap','Atom yarıçapı sıralaması',KY)
kart('K-PRDK-03','Element sınıflandırması','Atom numarasından dizilim, buradan metal–ametal ve değerlik elektronu bulunur.','Son katman elektron sayısını atom numarasıyla karıştırmak.','orta','öncüllü',3,'kim-pr-sinif','Atom numarasından element özellikleri',KY)
kart('K-PRDK-04','İyonlaşma enerjisi sıralaması','Aynı periyotta soldan sağa genelde artar, aynı grupta yukarıdan aşağı azalır.','Periyodik eğilimleri ters yorumlamak.','orta','düz',3,'kim-pr-iyonlasma','İyonlaşma enerjisi sıralaması',KY)
kart('K-PRDK-05','İyon yüklerinden element bulma','İyon yükü ve elektron sayısından nötr atomun elektron sayısı ve yeri bulunur.','Elektron sayısını atom numarası sanmak.','zor','düz',4,'kim-pr-iyon','İyonlardan element belirleme',KY)
kart('K-PRDK-06','Konumdan özellik yorumu','Bir elementin periyot ve grup konumuna göre yarıçap, değerlik elektronu ve elektronegatiflik karşılaştırılır.','Gruptaki elementlerin değerlik elektron sayısını farklı sanmak.','zor','öncüllü',4,'kim-pr-konum','Konuma göre periyodik özellik',KY)
# ---- 0001
per,gr=yer(17); assert (per,gr)==(3,7) and kab(17)==[2,8,7]
S=[('2. periyot 7A',False,'elektron dizilimi 2, 8, 7 olduğu için üç katman vardır, periyot 3’tür'),
   ('3. periyot 5A',False,'son katmanda 7 elektron bulunduğundan grup 7A’dır'),
   ('3. periyot 7A',True,''),
   ('4. periyot 7A',False,'elektronlar üç katmanda bulunur; dördüncü katman yoktur'),
   ('3. periyot 1A',False,'son katmanda 1 değil 7 elektron vardır')]
r=tek(S,True)
mk(P,'0001',tipId='kim-pr-yer',tip='Atom numarasından periyot ve grup',z='kolay',alt='Periyodik Sistem',kaz='Atom numarasından elektron dizilimini yazıp elementin periyot ve grubunu bulur.',kalip='düz',adim=2,
 kart='K-PRDK-01 (periyot ve grup) · atom numarası 17',
 metin='Atom numarası 17 olan X elementi periyodik sistemde hangi periyot ve grupta yer alır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='X elementinin periyodu ve grubu.',
 ip=['Önce elektronları katmanlara 2, 8, 8 sırasıyla yerleştir; katman sayısı periyodu, son katmandaki elektron sayısı grubu verir.'],
 bilgi=[B('Periyot ve grup','Katman sayısı periyot numarasını, son katmandaki elektron sayısı A grubu numarasını verir. Örnek: atom numarası 11 → 2, 8, 1 → 3. periyot 1A')],
 ad=[A('Elektron dizilimi','17 elektron 2, 8, 8 kuralıyla katmanlara yerleştirilir.','K: 2 · L: 8 · M: 7'),A('Periyot','Üç katman dolu olduğu için periyot 3’tür.','periyot = 3'),A('Grup','Son katmanda 7 elektron vardır.','grup = 7A')],
 puf='Katman sayısı periyodu, son katmandaki elektron sayısı A grubunu verir.')
# ---- 0002
ZX,ZY,ZZ=11,12,19
assert yer(ZX)==(3,1) and yer(ZY)==(3,2) and yer(ZZ)==(4,1)
kl={11:3,12:3,19:4}
S=[('X > Y > Z',False,'Z’nin katman sayısı fazla olduğundan yarıçapı en büyüktür'),
   ('Y > X > Z',False,'aynı periyotta soldan sağa gidildikçe yarıçap azalır, X Y’den büyüktür; ayrıca Z en büyüktür'),
   ('X > Z > Y',False,'Z dört katmanlıdır, üç katmanlı X’ten büyüktür'),
   ('Y > Z > X',False,'aynı periyotta X, Y’den büyüktür ve Z en büyük yarıçaplıdır'),
   ('Z > X > Y',True,'')]
r=tek(S,True)
mk(P,'0002',tipId='kim-pr-yaricap',tip='Atom yarıçapı sıralaması',z='orta',alt='Periyodik Sistem',kaz='Atom numarasından konum bulup atom yarıçaplarını karşılaştırır.',kalip='düz',adim=3,
 kart='K-PRDK-02 (atom yarıçapı) · atom numaraları 11, 12, 19',
 metin='X, Y ve Z elementlerinin atom numaraları sırasıyla 11, 12 ve 19’dur.\nBuna göre bu atomların yarıçapları arasındaki ilişki aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Atom yarıçaplarının büyükten küçüğe sıralaması.',
 ip=['Önce her elementin kaç katmanı olduğuna bak; katman sayıları eşitse çekirdek yükünün etkisine bak.'],
 bilgi=[B('Atom yarıçapı','Aynı grupta yukarıdan aşağı gidildikçe katman sayısı artar, yarıçap artar. Aynı periyotta soldan sağa gidildikçe çekirdek yükü artar, yarıçap azalır. Örnek: Na atomu Li atomundan büyüktür')],
 ad=[A('Elektron dizilimleri','Dizilimlerden periyot ve grup bulunur.','X: 2, 8, 1 (3. periyot) · Y: 2, 8, 2 (3. periyot) · Z: 2, 8, 8, 1 (4. periyot)'),A('Katman sayısı','Z dört, X ve Y üç katmanlıdır; Z en büyüktür.','Z > X, Y'),A('Aynı periyot','X ile Y aynı periyottadır; Y daha sağdadır, daha küçüktür.','X > Y'),A('Sıralama','İki sonuç birleştirilir.','Z > X > Y')],
 puf='Yarıçap karşılaştırmasında önce katman sayısına, eşitse atom numarasına bak (büyük atom numarası = daha küçük yarıçap).')
# ---- 0003
Zs={'X':8,'Y':11,'Z':18}
assert yer(8)==(2,6) and yer(11)==(3,1) and yer(18)==(3,8)
d={'I':(True,'X’in dizilimi 2, 6’dır; 2. periyot 6A grubundadır'),
   'II':(True,'Y’nin dizilimi 2, 8, 1’dir; 3. periyot 1A’da, elektron vermeye yatkın bir metaldir'),
   'III':(False,'Z’nin dizilimi 2, 8, 8’dir; son katmanında 2 değil 8 elektron bulunur')}
r=onc(d,[('I','II'),('I',),('II',),('III',),('I','III')])
mk(P,'0003',tipId='kim-pr-sinif',tip='Atom numarasından element özellikleri',z='orta',alt='Periyodik Sistem',kaz='Atom numarasından konum bulup metal–ametal ve değerlik elektronu özelliklerini yorumlar.',kalip='öncüllü',adim=3,
 kart='K-PRDK-03 (element sınıflandırması) · atom numaraları 8, 11, 18',
 metin='X, Y ve Z elementlerinin atom numaraları sırasıyla 8, 11 ve 18’dir.\nBu elementlerle ilgili şunlar söyleniyor.\nI. X, 2. periyot 6A grubundadır.\nII. Y, 3. periyot 1A grubunda yer alan bir metaldir.\nIII. Z’nin son katmanında 2 elektron bulunur.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her elementin elektron dizilimini yaz; katman sayısı ve son katmandaki elektron sayısı konumu belirler.'],
 bilgi=[B('Elektron dizilimi ve konum','Elektronlar 2, 8, 8 … sırasıyla katmanlara yerleşir. Katman sayısı periyodu, son katman elektron sayısı A grubunu verir. Örnek: atom numarası 6 → 2, 4 → 2. periyot 4A')],
 ad=[A('X elementi','8 elektron: 2, 6.','2. periyot 6A → I: doğru'),A('Y elementi','11 elektron: 2, 8, 1.','3. periyot 1A, metal → II: doğru'),A('Z elementi','18 elektron: 2, 8, 8.','son katmanda 8 elektron → III: yanlış'),A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve II')],
 puf='Elektron dizilimini yazmak, konum ve değerlik elektronu sorularının her zaman ilk adımıdır.')
# ---- 0004
assert yer(3)==(2,1) and yer(9)==(2,7) and yer(11)==(3,1)
S=[('X > Y > Z',False,'aynı periyotta sağa gidildikçe iyonlaşma enerjisi artar, Y (7A) X’ten (1A) büyüktür'),
   ('Y > X > Z',True,''),
   ('Z > X > Y',False,'aynı grupta aşağı inildikçe iyonlaşma enerjisi azalır; Z en küçüktür'),
   ('X > Z > Y',False,'Y aynı periyotta en sağdadır, iyonlaşma enerjisi en büyük olan odur'),
   ('Y > Z > X',False,'aynı grupta aşağı inildikçe iyonlaşma enerjisi azalır, X Z’den büyüktür')]
r=tek(S,True)
mk(P,'0004',tipId='kim-pr-iyonlasma',tip='İyonlaşma enerjisi sıralaması',z='orta',alt='Periyodik Sistem',kaz='Periyodik sistemdeki konuma göre birinci iyonlaşma enerjilerini karşılaştırır.',kalip='düz',adim=3,
 kart='K-PRDK-04 (iyonlaşma enerjisi) · atom numaraları 3, 9, 11',
 metin='X, Y ve Z elementlerinin atom numaraları sırasıyla 3, 9 ve 11’dir.\nBuna göre bu elementlerin birinci iyonlaşma enerjileri arasındaki ilişki aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Birinci iyonlaşma enerjilerinin büyükten küçüğe sıralaması.',
 ip=['Önce her elementin periyodunu ve grubunu bul; periyotta sağa ve grupta aşağı gitmenin iyonlaşma enerjisini nasıl değiştirdiğini düşün.'],
 bilgi=[B('İyonlaşma enerjisi','Gaz hâlindeki bir atomdan bir elektron koparmak için gereken enerjidir. Aynı periyotta soldan sağa genelde artar, aynı grupta yukarıdan aşağı azalır. Örnek: Na’nın iyonlaşma enerjisi Li’den küçüktür')],
 ad=[A('Konumlar','Elektron dizilimleri yazılır.','X: 2, 1 (2. periyot 1A) · Y: 2, 7 (2. periyot 7A) · Z: 2, 8, 1 (3. periyot 1A)'),A('Aynı periyot','X ve Y 2. periyottadır; Y daha sağdadır.','Y > X'),A('Aynı grup','X ve Z 1A grubundadır; Z daha aşağıdadır.','X > Z'),A('Sıralama','İki sonuç birleştirilir.','Y > X > Z')],
 puf='İyonlaşma enerjisi periyotta sağa doğru artar, grupta aşağı doğru azalır.')
# ---- 0005
eX,qX=18,2; eY,qY=10,3
ZXa=eX-qX; ZYa=eY+qY; assert (ZXa,ZYa)==(16,13) and yer(16)==(3,6) and yer(13)==(3,3)
S=[('X ve Y aynı grupta yer alır',False,'X 6A, Y 3A grubundadır; gruplar farklıdır'),
   ('Y’nin değerlik elektron sayısı 5’tir',False,'Y’nin dizilimi 2, 8, 3’tür; değerlik elektron sayısı 3’tür'),
   ('X, 2. periyot 6A grubundadır',False,'X’in dizilimi 2, 8, 6’dır; üç katmanı olduğundan 3. periyottadır'),
   ('X ve Y aynı periyottadır, X’in değerlik elektron sayısı 6’dır',True,''),
   ('Y ametaldir',False,'Y 3A grubunda yer alan bir metaldir ve elektron vermeye yatkındır')]
r=tek(S,True)
mk(P,'0005',tipId='kim-pr-iyon',tip='İyonlardan element belirleme',z='zor',alt='Periyodik Sistem',kaz='İyon yükü ve elektron sayısından nötr atomun atom numarasını ve periyodik sistemdeki yerini bulur.',kalip='düz',adim=4,
 kart='K-PRDK-05 (iyon yükleri) · X²⁻ 18 elektron, Y³⁺ 10 elektron',
 metin='X²⁻ iyonunda 18, Y³⁺ iyonunda 10 elektron bulunmaktadır.\nBuna göre X ve Y elementleriyle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='X ve Y için doğru olan ifade.',
 ip=['Anyon elektron almıştır, katyon elektron vermiştir; nötr atomun elektron sayısını bulmak için yükü kullan.'],
 bilgi=[B('İyon ve elektron sayısı','Nötr atomda proton sayısı elektron sayısına eşittir. Anyon, yükü kadar elektron almıştır; katyon, yükü kadar elektron vermiştir. Örnek: Cl⁻ iyonunda 18 elektron varsa Cl atomunda 17 elektron vardır')],
 ad=[A('X atomu','X²⁻ iyonu 2 elektron almıştır.','nötr X: 18 − 2 = 16 elektron → 2, 8, 6'),A('Y atomu','Y³⁺ iyonu 3 elektron vermiştir.','nötr Y: 10 + 3 = 13 elektron → 2, 8, 3'),A('Konumlar','Her ikisi de üç katmanlıdır.','X: 3. periyot 6A · Y: 3. periyot 3A'),A('Şıkları ele','Şıklar tek tek denetlenir.','D: doğru · diğerleri: yanlış')],
 puf='İyonlarda önce nötr atomun elektron sayısını bul: anyondan yükü çıkar, katyona yükü ekle.')
# ---- 0006
d={'I':(True,'Z’nin katman sayısı X’ten fazladır; X ile Y aynı periyottadır ve Y daha sağda olduğundan daha küçüktür: Z > X > Y'),
   'II':(True,'aynı gruptaki elementlerin değerlik elektron sayıları eşittir'),
   'III':(False,'Y aynı periyotta X’in sağında, Z ise X’in altındadır; Y’nin elektronegatifliği Z’ninkinden büyüktür')}
r=onc(d,[('I',),('I','II'),('II','III'),('I','III'),('III',)])
mk(P,'0006',tipId='kim-pr-konum',tip='Konuma göre periyodik özellik',z='zor',alt='Periyodik Sistem',kaz='Elementlerin periyodik sistemdeki göreli konumuna göre periyodik özelliklerini karşılaştırır.',kalip='öncüllü',adim=4,
 kart='K-PRDK-06 (konumdan özellik) · X, Y, Z göreli konumları',
 metin='A grubu elementlerinden X, Y ve Z için şu bilgiler veriliyor.\n• X ile Y aynı periyottadır ve Y, X’in sağında yer alır.\n• Z, X ile aynı gruptadır ve X’in altında yer alır.\n• Y soy gaz değildir.\nBu elementlerle ilgili şunlar söyleniyor.\nI. Atom yarıçapları arasındaki ilişki Z > X > Y’dir.\nII. Z ile X’in değerlik elektron sayıları eşittir.\nIII. Y’nin elektronegatifliği Z’ninkinden küçüktür.\nBuna göre hangileri kesinlikle doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Kesinlikle doğru olan öncüller.',
 ip=['Elementlerin kabaca bir tablo üzerindeki yerini çiz: X’in sağına Y’yi, altına Z’yi koy ve eğilimleri uygula.'],
 bilgi=[B('Periyodik eğilimler','Aynı grupta aşağı inildikçe katman sayısı ve atom yarıçapı artar, elektronegatiflik azalır. Aynı periyotta sağa gidildikçe yarıçap azalır, elektronegatiflik artar. Aynı gruptaki elementlerin değerlik elektron sayısı aynıdır')],
 ad=[A('Konum çizimi','Y, X’in sağında; Z, X’in altında.','Y → X ↓ Z'),A('I. öncül','Z’nin katman sayısı fazladır; X ile Y arasında soldaki X daha büyüktür.','Z > X > Y → doğru'),A('II. öncül','Aynı gruptadırlar.','değerlik elektronları eşit → doğru'),A('III. öncül','Y sağa, Z aşağı kaydığı için Y’nin elektronegatifliği Z’den büyüktür.','III: yanlış · Sonuç: I ve II')],
 puf='Konumdan karşılaştırma yaparken elementleri bir ızgarada yerleştir; sağ = küçük yarıçap, aşağı = büyük yarıçap.')
bitir(P,'periyodik','kim|Periyodik Sistem')
