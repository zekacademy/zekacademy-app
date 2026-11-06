import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
from collections import Counter
def _num(t):
    try: return Fr(t.replace('−','-').replace(',','.').strip())
    except Exception: return None
def _opts(o):
    if all(_num(x[0]) is not None for x in o): o=sorted(o,key=lambda x:_num(x[0]))
    L='ABCDE'; assert len(o)==5
    sik=[L[i] for i,x in enumerate(o) if x[1] is None]; assert len(sik)==1,sik
    return [x[0] for x in o],sik[0],{L[i]:x[1] for i,x in enumerate(o) if x[1] is not None},{L[i]:x[2] for i,x in enumerate(o) if x[1] is not None}
KARTLAR=[]
def Q(P,pre,no,tipId,tip,zor,alt,kaz,kalip,adim,fikir,tuzak,bilgi,puf,a,k,ozet,degisti,kisa=None):
    kid=f'K-{pre}-{int(no):02d}'
    KARTLAR.append(dict(id=kid,konu=P.konu_adi,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak='ÖSYM 2018–2026 TYT Biyoloji dağılımı · MEB 9–10. sınıf biyoloji'))
    s,c,cel,tur=_opts(a['o'])
    P.R(no,tipId,tip,zor,alt,kaz,kalip,adim,f'{kid} ({ozet}) · {degisti}',a['m'],s,c,a['i'],a['ip'],bilgi,a['ad'],puf,cel,tur,kisa=kisa)
    s,c,cel,tur=_opts(k['o'])
    P.K(no,k['m'],s,c,k.get('i',a['i']),k.get('ip',a['ip']),k.get('bilgi',bilgi),k['ad'],k.get('puf',puf),cel,tur,kisa=kisa)
def bitir(P,onek,konu,uyg,n_ana):
    assert len(P.ANA)==n_ana==len(P.KAR),(len(P.ANA),len(P.KAR))
    tipler={}
    for k in KARTLAR: tipler.setdefault(k['tipId'],dict(tipId=k['tipId'],ad=k['tip'],kartlar=[],uygulamaKonu=uyg))['kartlar'].append(k['id'])
    json.dump(dict(konu=konu,surum=1,kartlar=KARTLAR,tipler=list(tipler.values())),open(os.path.join(H,'..','kartlar',onek+'.json'),'w'),ensure_ascii=False,indent=1)
    P.yaz(os.path.join(H,onek+'-1.json'),os.path.join(H,onek+'-1-kardes.json'))
    print('zorluk',Counter(q['zorluk'] for q in P.ANA),'tipler',len(tipler))
P=Parti('bilesenler','Canlıların Temel Bileşenleri','bio|Canlıların Temel Bileşenleri',ders='TYT Biyoloji',idon='tytbio')
PRE='BBI'
YAP=B('Yapıtaşı ve polimer','Amino asit → protein · Nükleotit → nükleik asit (DNA, RNA) · Glikoz gibi monosakkarit → polisakkarit (nişasta, glikojen, selüloz) · Gliserol + yağ asitleri → yağ')
ENZ=B('Enzim','Tepkimeleri hızlandıran biyolojik katalizördür; yapısı genellikle proteindir · Aktivasyon enerjisini düşürür, tepkime sonunda değişmez, her enzim belirli bir substrata etki eder · Aşırı sıcaklık enzimi bozar')
KH=B('Karbonhidratlar','Glikoz, fruktoz: monosakkarit · Sükroz, maltoz: disakkarit · Nişasta: bitkide, glikojen: hayvanda depo polisakkarit · Selüloz: bitki hücre duvarının yapısı')
SU=B('Suyun görevleri','Çözücüdür, madde taşınmasını sağlar · Hidroliz tepkimelerine girer · Isı kapasitesi yüksektir, vücut sıcaklığını dengeler · Enerji vermez')
PEP=B('Peptit bağı ve su','Amino asitler arasında bağ kurulurken her bağda 1 su molekülü açığa çıkar (dehidrasyon sentezi) · Peptit bağı sayısı = amino asit sayısı − zincir sayısı. Örnek: tek zincirli 5 amino asit → 4 bağ')
DNA=B('DNA’da baz eşleşmesi','Adenin (A) timin (T) ile 2, guanin (G) sitozin (C) ile 3 hidrojen bağı yapar · Çift zincirli DNA’da A = T ve G = C olur')
# 0001
Q(P,PRE,'0001','bl-yapitasi','Yapıtaşı–bileşik eşleştirmesi','kolay','Organik bileşikler','Organik bileşiklerin yapıtaşlarını eşleştirir.','düz',2,
 'Yapıtaşı ve oluşturduğu bileşik eşleştirilir.','Amino asit ile glikozu karıştırmak.',[YAP],
 'Protein ← amino asit, nükleik asit ← nükleotit, polisakkarit ← monosakkarit.',
 dict(m='Aşağıdaki yapıtaşı–bileşik eşleştirmelerinden hangisi doğrudur?',i='Doğru eşleştirme.',ip=['Proteinin yapıtaşı nedir?','Nükleik asitler hangi birimlerden oluşur?','Her şıktaki yapıtaşını bileşikle karşılaştır.'],
  o=[('Glikoz – Protein','Karbonhidrat yapıtaşını proteinle karıştırmak.','bilgi'),('Amino asit – Karbonhidrat','Amino asidin proteinin yapıtaşı olduğunu bilmemek.','bilgi'),('Nükleotit – Protein','Nükleotitin nükleik asit yapıtaşı olduğunu bilmemek.','bilgi'),('Yağ asidi ve gliserol – Nükleik asit','Yağın yapıtaşlarını nükleik asitle eşleştirmek.','bilgi'),('Amino asit – Protein',None,None)],
  ad=[A('Yapıtaşlarını hatırla','Protein amino asitlerden, nükleik asit nükleotitlerden, karbonhidrat monosakkaritlerden oluşur.','amino asit → protein'),A('Şıkları sına','Glikoz karbonhidrat, nükleotit nükleik asit yapıtaşıdır; yağ asidi ve gliserol yağı oluşturur.','A, B, C, D hatalı'),A('Sonuç','Doğru eşleştirme amino asit – proteindir.','Amino asit – Protein')]),
 dict(m='Aşağıdakilerden hangisinde yapıtaşı ve oluşturduğu bileşik doğru eşleştirilmiştir?',
  o=[('Gliserol ve yağ asidi – Yağ',None,None),('Glikoz – Nükleik asit','Karbonhidrat yapıtaşını nükleik asitle eşleştirmek.','bilgi'),('Nükleotit – Karbonhidrat','Nükleotitin nükleik asit yapıtaşı olduğunu bilmemek.','bilgi'),('Amino asit – Yağ','Amino asidin proteinin yapıtaşı olduğunu bilmemek.','bilgi'),('Yağ asidi – Protein','Yağ asidini amino asitle karıştırmak.','bilgi')],
  ad=[A('Yapıtaşlarını hatırla','Yağ gliserol ve yağ asitlerinden, protein amino asitlerden oluşur.','gliserol + yağ asidi → yağ'),A('Şıkları sına','Glikoz karbonhidrat, nükleotit nükleik asit yapıtaşıdır; amino asit proteinin yapıtaşıdır.','diğer şıklar hatalı'),A('Sonuç','Doğru eşleştirme gliserol ve yağ asidi – yağdır.','Gliserol ve yağ asidi – Yağ')]),
 'yapıtaşı–bileşik','eşleştirmeler ve şıklar değişti')
# 0002
Q(P,PRE,'0002','bl-enzim','Enzimlerin özellikleri','orta','Enzimler','Enzimlerin yapı ve işleyiş özelliklerini değerlendirir.','öncüllü',3,
 'Üç enzim yargısından doğru olanlar seçilir.','Enzimin tepkimede harcandığını sanmak.',[ENZ],
 'Enzim katalizördür: tepkimeyi hızlandırır, harcanmaz, özgüdür.',
 dict(m='Enzimlerle ilgili,\nI. Yapıları genellikle proteindir.\nII. Tepkimeye girip harcanırlar.\nIII. Her enzim belirli bir substrata etki eder.\nifadelerinden hangileri doğrudur?',i='Doğru olan ifadeler.',ip=['Enzim hangi tür bileşiktir?','Katalizör tepkime sonunda ne olur?','Bir enzim her maddeyi mi parçalar, belirli bir maddeyi mi?'],
  o=[('Yalnız I','Enzimlerin özgül olduğunu bilmemek.','bilgi'),('Yalnız III','Enzimlerin protein yapılı olduğunu bilmemek.','bilgi'),('I ve II','Enzimin tepkimede harcandığını sanmak.','bilgi'),('II ve III','Enzimin harcandığını sanıp proteinliğini atlamak.','bilgi'),('I ve III',None,None)],
  ad=[A('I. ifade','Enzimlerin yapısı genellikle proteindir.','I doğru'),A('II. ifade','Enzim katalizördür; tepkime sonunda değişmeden kalır ve tekrar kullanılır.','II yanlış'),A('III. ifade','Enzimler özgüldür: her biri belirli bir substrata etki eder.','III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 dict(m='Enzimlerle ilgili,\nI. Tepkimenin aktivasyon enerjisini düşürürler.\nII. Tepkime sonunda yapıları değişmeden kalır.\nIII. Sıcaklık ne kadar artarsa o kadar hızlı çalışırlar.\nifadelerinden hangileri doğrudur?',
  o=[('I ve II',None,None),('Yalnız I','Enzimin tepkime sonunda değişmediğini bilmemek.','bilgi'),('Yalnız III','Sıcaklık ile enzim hızı arasındaki sınırı bilmemek.','bilgi'),('I ve III','Çok yüksek sıcaklıkta enzimin bozulduğunu unutmak.','bilgi'),('II ve III','Aktivasyon enerjisini atlayıp sıcaklık yargısını doğru saymak.','bilgi')],
  ad=[A('I. ifade','Enzimler tepkimeyi başlatmak için gereken aktivasyon enerjisini düşürür.','I doğru'),A('II. ifade','Enzim tepkime sonunda aynı kalır, tekrar kullanılır.','II doğru'),A('III. ifade','Aşırı sıcaklıkta enzim yapısı bozulur ve çalışmaz.','III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 'enzimlerin özellikleri','farklı üç yargı')
# 0003
Q(P,PRE,'0003','bl-karbonhidrat','Karbonhidratların görevleri','orta','Karbonhidratlar','Karbonhidrat çeşitlerini ve görevlerini değerlendirir.','öncüllü',3,
 'Depo ve yapı karbonhidratlarının görevleri doğru/yanlış olarak sınanır.','Nişasta ile glikojenin canlı gruplarını karıştırmak.',[KH],
 'Nişasta bitkide, glikojen hayvanda depo polisakkarittir.',
 dict(m='Karbonhidratlarla ilgili,\nI. Nişasta, bitkilerde depo edilen bir polisakkarittir.\nII. Glikojen, bitkilerde depo edilen bir polisakkarittir.\nIII. Selüloz, bitki hücre duvarının yapısına katılır.\nifadelerinden hangileri doğrudur?',i='Doğru olan ifadeler.',ip=['Hayvanlarda depo polisakkarit hangisidir?','Bitki hücre duvarı hangi polisakkaritten yapılıdır?','Nişasta ile glikojeni hangi canlı grubuna bağlarsın?'],
  o=[('Yalnız I','Selülozun bitki hücre duvarında olduğunu bilmemek.','bilgi'),('Yalnız III','Nişastanın bitkilerde depo edildiğini bilmemek.','bilgi'),('I ve II','Glikojeni bitki deposu sanmak.','bilgi'),('I ve III',None,None),('II ve III','Nişasta ile glikojenin canlı gruplarını karıştırmak.','bilgi')],
  ad=[A('I. ifade','Bitkiler fazla glikozu nişasta olarak depo eder.','I doğru'),A('II. ifade','Glikojen hayvan hücrelerinde (karaciğer, kas) depolanır; bitkide nişasta bulunur.','II yanlış'),A('III. ifade','Selüloz bitki hücre duvarının yapıtaşıdır.','III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 dict(m='Karbonhidratlarla ilgili,\nI. Sükroz, bir disakkarittir.\nII. Glikojen, hayvanlarda depo edilen bir polisakkarittir.\nIII. Glikoz, bir polisakkarittir.\nifadelerinden hangileri doğrudur?',
  o=[('Yalnız I','Glikojenin hayvanlarda depo edildiğini bilmemek.','bilgi'),('I ve II',None,None),('Yalnız II','Sükrozun disakkarit olduğunu bilmemek.','bilgi'),('I ve III','Glikozu polisakkarit sanmak.','bilgi'),('II ve III','Glikozu polisakkarit sanıp sükrozu atlamak.','bilgi')],
  ad=[A('I. ifade','Sükroz glikoz ile fruktozdan oluşur, iki monosakkaritli bir disakkarittir.','I doğru'),A('II. ifade','Glikojen hayvan hücrelerinde depo polisakkarittir.','II doğru'),A('III. ifade','Glikoz tek şekerli bir monosakkarittir.','III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 'depo ve yapı karbonhidratları','farklı üç yargı')
# 0004
Q(P,PRE,'0004','bl-su','Suyun canlılar için önemi','orta','Su','Suyun canlıdaki görevlerini ayırt eder.','düz',2,
 'Suyun görevlerinden olmayan seçenek bulunur.','Suyun enerji sağladığını sanmak.',[SU],
 'Su çözücü ve ortamdır; enerji kaynağı değildir.',
 dict(m='Aşağıdakilerden hangisi suyun canlılardaki görevlerinden biri değildir?',i='Suyun görevi olmayan seçenek.',ip=['Besin maddeleri enerji verir; su verir mi?','Suyun çözücü özelliği ne işe yarar?','Isı kapasitesi yüksek olması neye yarar?'],
  o=[('Maddeleri çözerek taşınmalarını sağlamak','Suyun çözücü ve taşıyıcı olduğunu bilmemek.','bilgi'),('Hidroliz tepkimelerine girmek','Suyun hidrolizde kullanıldığını bilmemek.','bilgi'),('Vücut sıcaklığının ani değişmesini önlemek','Suyun yüksek ısı kapasitesini bilmemek.','bilgi'),('Oksidasyonla enerji açığa çıkarmak',None,None),('Tepkimelerin gerçekleştiği ortamı oluşturmak','Hücre içi tepkimelerin sulu ortamda olduğunu bilmemek.','bilgi')],
  ad=[A('Görevleri hatırla','Su çözücüdür, taşır, hidrolize girer, sıcaklığı dengeler.','dört görev'),A('Şıkları sına','Taşıma, hidroliz, sıcaklığı dengeleme ve ortam olma suyun görevidir.','4 şık görev'),A('Kalan şık','Su yakıt olarak yakılıp enerji vermez.','enerji vermez'),A('Sonuç','Görev olmayan oksidasyonla enerji vermedir.','Oksidasyonla enerji açığa çıkarmak')]),
 dict(m='Aşağıdakilerden hangisi suyun canlılar için önemini doğru ifade etmez?',
  o=[('Vücut sıcaklığının dengede kalmasına yardım eder.','Isı kapasitesi yüksek olmasının sıcaklığı dengelediğini bilmemek.','bilgi'),('Hücrelerde tepkimelerin gerçekleştiği ortamı oluşturur.','Tepkimelerin sulu ortamda gerçekleştiğini bilmemek.','bilgi'),('Karbonhidrat gibi enerji kaynağı olarak kullanılır.',None,None),('Kanda maddelerin taşınmasında çözücü olarak görev yapar.','Suyun çözücü olduğunu bilmemek.','bilgi'),('Büyük moleküllerin parçalanmasında hidroliz tepkimesine katılır.','Hidroliz tepkimesinde suyun kullanıldığını bilmemek.','bilgi')],
  ad=[A('Görevleri hatırla','Su çözücüdür, taşır, hidrolize girer, sıcaklığı dengeler.','dört görev'),A('Şıkları sına','Sıcaklık dengesi, ortam olma, taşıma ve hidroliz doğrudur.','4 şık doğru'),A('Kalan şık','Su besin değildir, enerji kaynağı olarak kullanılmaz.','enerji vermez'),A('Sonuç','Yanlış olan enerji kaynağı olma ifadesidir.','Enerji kaynağı')]),
 'suyun görevleri','"değildir" yönü, şıklar baştan yazıldı')
# 0005
assert 120-2==118 and 90-3==87
Q(P,PRE,'0005','bl-peptit','Peptit bağı ve su hesabı','zor','Proteinler','Zincir sayısını da hesaba katarak peptit bağı ve su sayısını bulur.','yeni nesil',4,
 'Amino asit sayısı ve zincir sayısından açığa çıkan su hesaplanır.','Zincir sayısını hesaba katmamak.',[PEP,YAP],
 'Su sayısı = peptit bağı sayısı = amino asit sayısı − zincir sayısı.',
 dict(m='120 amino asitten oluşan bir protein, birbirine bağlı olmayan iki polipeptit zincirinden meydana gelmektedir.\nBu proteinin sentezi sırasında bütün amino asitler peptit bağlarıyla bağlandığına göre kaç molekül su açığa çıkmıştır?',i='Açığa çıkan su molekülü sayısı.',ip=['Tek zincirde n amino asit kaç bağ yapar?','İki zincir olması bağ sayısını nasıl etkiler?','Her peptit bağında kaç su molekülü açığa çıkar?'],
  o=[('59','Amino asit sayısını zincir sayısına bölmek.','islem'),('60','120’nin yarısını almak.','islem'),('118',None,None),('119','Zincir sayısını 1 sanmak.','dikkat'),('120','Her amino asit için bir su açığa çıktığını sanmak.','bilgi')],
  ad=[A('Her zinciri düşün','n amino asitli bir zincirde n − 1 peptit bağı oluşur.','zincir başına n − 1'),A('İki zincir','İki zincir birbirine bağlı olmadığından toplam bağ sayısı 120 − 2 olur.','120 − 2 = 118'),A('Suya çevir','Her peptit bağında bir su molekülü açığa çıkar.','118 bağ = 118 su'),A('Sonuç','Açığa çıkan su sayısı 118’dir.','118')]),
 dict(m='90 amino asitten oluşan bir enzim, birbirine bağlı olmayan üç polipeptit zincirinden meydana gelmektedir.\nBu enzimin sentezi sırasında bütün amino asitler peptit bağlarıyla bağlandığına göre kaç molekül su açığa çıkmıştır?',
  o=[('30','Amino asit sayısını zincir sayısına bölmek.','islem'),('86','Zincir sayısını 4 almak.','islem'),('87',None,None),('89','Zincir sayısını 1 sanmak.','dikkat'),('90','Her amino asit için bir su açığa çıktığını sanmak.','bilgi')],
  ad=[A('Her zinciri düşün','n amino asitli bir zincirde n − 1 peptit bağı oluşur.','zincir başına n − 1'),A('Üç zincir','Üç zincir birbirine bağlı olmadığından toplam bağ sayısı 90 − 3 olur.','90 − 3 = 87'),A('Suya çevir','Her peptit bağında bir su molekülü açığa çıkar.','87 bağ = 87 su'),A('Sonuç','Açığa çıkan su sayısı 87’dir.','87')]),
 'amino asit ve zincir sayısı','sayılar ve zincir sayısı değişti')
# 0006
a=40;g=60; assert 2*a+2*g==200 and 2*a+3*g==260 and a+a+g+g==200 and a*2+g*3==260
a2=90;g2=60; assert 2*a2+3*g2==360 and 2*a2+2*g2==300 and 2*a2+2*g2==300
Q(P,PRE,'0006','bl-dna-hesap','DNA’da baz sayısı ve hidrojen bağı','zor','Nükleik asitler','Baz yüzdesinden DNA’daki hidrojen bağı sayısını hesaplar.','yeni nesil',5,
 'Bir bazın yüzdesinden diğer bazlar bulunur; eşleşmelere göre hidrojen bağı sayılır.','A–T ve G–C bağ sayılarını karıştırmak.',[DNA],
 'Önce A = T ve G = C sayılarını bul; sonra çift sayısı × bağ sayısı.',
 dict(m='Çift zincirli bir DNA molekülü 200 nükleotitten oluşmaktadır. Bu nükleotitlerin %20’si timindir.\nBuna göre bu DNA molekülündeki toplam hidrojen bağı sayısı kaçtır?',i='Toplam hidrojen bağı sayısı.',ip=['Timin sayısını, sonra adenin sayısını bul.','Kalan nükleotitler guanin ve sitozin arasında nasıl paylaşılır?','A–T çifti 2, G–C çifti 3 hidrojen bağı yapar.'],
  o=[('200','Bütün çiftlerin 2 bağlı olduğunu sanmak.','bilgi'),('260',None,None),('300','Bütün çiftlerin 3 bağlı olduğunu sanmak.','bilgi'),('340','A ve T için ayrı ayrı çift sayıp 2 ile çarpmak.','islem'),('520','Bağları iki kez saymak.','islem')],
  ad=[A('Timin ve adenin','200’ün %20’si timin: 40 T. Çift zincirde A = T, yani 40 A.','T = 40 · A = 40'),A('Guanin ve sitozin','Kalan 200 − 80 = 120 nükleotit G ve C’dir; G = C olduğundan her biri 60.','G = 60 · C = 60'),A('Baz çiftleri','40 A–T çifti ve 60 G–C çifti vardır.','40 + 60 = 100 çift'),A('Hidrojen bağları','A–T 2 bağ, G–C 3 bağ yapar.','40 × 2 + 60 × 3 = 80 + 180'),A('Sonuç','Toplam hidrojen bağı 260’tır.','260')]),
 dict(m='Çift zincirli bir DNA molekülü 300 nükleotitten oluşmaktadır. Bu nükleotitlerin %30’u adenindir.\nBuna göre bu DNA molekülündeki toplam hidrojen bağı sayısı kaçtır?',
  o=[('300','Bütün çiftlerin 2 bağlı olduğunu sanmak.','bilgi'),('360',None,None),('450','Bütün çiftlerin 3 bağlı olduğunu sanmak.','bilgi'),('540','A ve T sayısının toplamını 3 ile çarpmak.','islem'),('720','Bağları iki kez saymak.','islem')],
  ad=[A('Adenin ve timin','300’ün %30’u adenin: 90 A. Çift zincirde A = T, yani 90 T.','A = 90 · T = 90'),A('Guanin ve sitozin','Kalan 300 − 180 = 120 nükleotit G ve C’dir; her biri 60.','G = 60 · C = 60'),A('Baz çiftleri','90 A–T çifti ve 60 G–C çifti vardır.','90 + 60 = 150 çift'),A('Hidrojen bağları','A–T 2 bağ, G–C 3 bağ yapar.','90 × 2 + 60 × 3 = 180 + 180'),A('Sonuç','Toplam hidrojen bağı 360’tır.','360')]),
 'baz yüzdesi, hidrojen bağı','baz, sayılar ve toplam değişti')
bitir(P,'bilesenler','Canlıların Temel Bileşenleri','bio|Canlıların Temel Bileşenleri',6)
