import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_c import *
P=Parti('kuvvetler','İç Kuvvetler / Dış Kuvvetler','cog|İç Kuvvetler / Dış Kuvvetler',ders='TYT Coğrafya',idon='tytcog')
KY='ÖSYM 2018–2026 TYT Coğrafya (dünyanın yapısı, yer şekillendiren süreçler) · MEB 10. sınıf'
kart('K-CGKV-01','İç ve dış kuvvetlerin ürünü','İç kuvvetler yer kabuğunu kıvırır, kırar, volkan oluşturur; dış kuvvetler aşındırır, taşır, biriktirir.','Delta gibi birikim şekillerini iç kuvvet sanmak.','kolay','düz',2,'cg-kuvvetler-urun','İç–dış kuvvet ürünü ayırma',KY)
kart('K-CGKV-02','Fiziksel ayrışma','Fiziksel ayrışmada kayaç kimyasal yapısı değişmeden parçalanır (don, sıcaklık farkı); çözünme kimyasaldır.','Çözünmeyi fiziksel ayrışma saymak.','orta','öncüllü',3,'cg-kuvvetler-ayrisma','Fiziksel ve kimyasal ayrışma',KY)
kart('K-CGKV-03','Karstik şekiller','Kalkerli arazide suyun çözmesiyle dolin, lapya, düden gibi şekiller oluşur.','Karstik şekli rüzgâr ya da buzul şekliyle karıştırmak.','orta','yeni nesil',3,'cg-kuvvetler-karst','Yer şekli–oluşturan etken eşleştirme',KY)
kart('K-CGKV-04','Olay sıralaması','İç ve dış kuvvetlerin etkileri belirli bir sırayla birbirini izler: birikim, yükselme, aşınma.','Olayları verildiği sırayla dizmek.','zor','öncüllü',4,'cg-kuvvetler-sira','Yer şekillenme olaylarını sıralama',KY)
IC=B('İç ve dış kuvvetler','İç kuvvetler (yer içi enerji): kıvrılma, kırılma, volkanizma, deprem — kabuğu kıvırır, kırar, yükseltir. Dış kuvvetler (Güneş enerjisi ve yer çekimi): akarsu, rüzgâr, buzul, dalga — aşındırır, taşır, biriktirir. Örnek: delta dış, graben iç kuvvet ürünüdür')
AYR=B('Ayrışma','Fiziksel (mekanik) ayrışma: kayaç kimyasal yapısı değişmeden parçalanır; don olayı, gece–gündüz sıcaklık farkı. Kimyasal ayrışma: kayaç suyla ve gazlarla tepkimeye girip çözünür; kireçtaşının çözünmesi')
KRS=B('Karstik şekiller','Kalkerli (kireçtaşlı) arazide suyun çözmesiyle lapya, dolin (çanak), düden ve polye oluşur. Rüzgâr: barhan, yardang · Buzul: fiyort · Akarsu: delta, meander')
# 0001
Q(P,'0001','K-CGKV-01','kolay','İç ve dış kuvvetlerin oluşturduğu yer şekillerini ayırt eder.','düz',2,
 'Aşağıdakilerden hangisi, dış kuvvetlerin etkisiyle oluşan bir yer şeklidir?',
 [('Delta ovası','dış',None,None),('Graben','iç','Graben, yer kabuğunun kırılıp çökmesiyle oluşur; iç kuvvet ürünüdür.','bilgi'),('Horst','iç','Horst, kırıklarla yükselen blok olup iç kuvvet ürünüdür.','bilgi'),('Volkanik koni','iç','Volkanik koni, magmanın yüzeye çıkmasıyla oluşur; iç kuvvet ürünüdür.','bilgi'),('Kıvrım dağı','iç','Kıvrım dağları kabuğun kıvrılmasıyla oluşur; iç kuvvet ürünüdür.','bilgi')],
 lambda e:e=='dış','Dış kuvvetlerin oluşturduğu yer şekli.',
 'Yer şeklinin aşındırma ve biriktirmeyle mi, yer içi hareketlerle mi oluştuğunu düşün.',[IC],
 [A('Ayrımı hatırla','Yer içi hareketler kabuğu kıvırır, kırar ya da magmayı çıkarır. Akarsu gibi dış etkenler aşındırır, taşır, biriktirir.','iç: kıvrılma, kırılma, volkan · dış: aşındırma, biriktirme'),
  A('Şıkları sına','Graben, horst, volkanik koni ve kıvrım dağı yer içi hareketlerle oluşur.','4 şık: iç kuvvet'),
  A('Sonuç','Delta, akarsuyun taşıdığı malzemeyi denizde biriktirmesiyle oluşur.','Delta: dış kuvvet')],
 'Biriktirme ve aşındırma şekilleri dış kuvvet, kırık ve kıvrım şekilleri iç kuvvet ürünüdür.','yeni şık kümesi',harf='A')
# 0002
tr={'I':True,'II':True,'III':False}; dg={k for k,v in tr.items() if v}
Q(P,'0002','K-CGKV-02','orta','Fiziksel ayrışma ile kimyasal ayrışmayı ayırt eder.','öncüllü',3,
 'I. Don olayıyla kayaçların çatlayıp parçalanması\nII. Gece ve gündüz arasındaki sıcaklık farkıyla kayaçların çatlaması\nIII. Kireçtaşının yağmur suyuyla çözünmesi\nYukarıdaki olaylardan hangileri fiziksel ayrışmaya örnektir?',
 onc_opts(dg,[{'III'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}],{'Yalnız III':('Çözünmeyi fiziksel ayrışma saymak; çözünme kimyasaldır.','bilgi'),'I ve III':('Don olayını doğru bulup sıcaklık farkını atlamak; çözünmeyi de fiziksel saymak.','bilgi'),'II ve III':('Don olayını atlayıp çözünmeyi fiziksel saymak.','bilgi'),'I, II ve III':('Kireçtaşının çözünmesinin kimyasal ayrışma olduğunu unutmak.','bilgi')}),
 lambda e:e==frozenset(dg),'Fiziksel ayrışma örnekleri.',
 'Kayacın yalnız parçalandığı mı, yoksa suyla kimyasal olarak çözündüğü mü diye bak.',[AYR],
 [A('Ayrımı hatırla','Fiziksel ayrışmada kayaç yalnız parçalanır. Kimyasal ayrışmada kayaç suyla ve gazlarla tepkimeye girer.','fiziksel: parçalanma · kimyasal: çözünme'),
  A('Öncülleri sına','Don ve sıcaklık farkı kayacı çatlatır, yapısını değiştirmez. Kireçtaşının çözünmesi kimyasal bir tepkimedir.','I: fiziksel · II: fiziksel · III: kimyasal'),
  A('Sonuç','Fiziksel ayrışma örnekleri I ve II’dir.','I ve II')],
 'Parçalanma fiziksel, çözünme kimyasal ayrışmadır.','don, sıcaklık farkı ve çözünme',harf='B')
# 0003
Q(P,'0003','K-CGKV-03','orta','Kalkerli arazide suyun çözmesiyle oluşan şekli tanır.','yeni nesil',3,
 'Kalkerli (kireçtaşlı) bir arazide yağmur ve yeraltı suları kayacı çözmüş; yüzeyde çanak ya da huni biçiminde çukurluklar oluşmuştur.\nBu çukurluklara ne ad verilir?',
 [('Barhan','x','Barhan, rüzgârın biriktirdiği kum tepesidir.','bilgi'),('Delta','x','Delta, akarsuyun denize taşıdığı malzemeyi biriktirmesiyle oluşur.','bilgi'),('Dolin','d',None,None),('Fiyort','x','Fiyort, buzulun açtığı vadiye denizin dolmasıyla oluşur.','bilgi'),('Meander','x','Meander, akarsuyun düzlükte yaptığı menderes biçimli kıvrımdır.','bilgi')],
 lambda e:e=='d','Çukurlukların adı.',
 'Çözünmeyle oluşan karstik şekillerden çanak biçimli olanı hatırla.',[KRS],
 [A('Süreci belirle','Kalkerli arazide suyun çözmesi karstlaşmadır.','kalker + su → karstik şekil'),
  A('Şekilleri ele','Barhan rüzgâra, delta ve meander akarsuya, fiyort buzula bağlıdır.','4 şık: karstik değil'),
  A('Sonuç','Çanak biçimli çukurluğa dolin denir.','Dolin')],
 'Kalkerli arazide çözünmeyle oluşan çanak biçimli çukurluk dolindir.','karstik tanım',harf='C')
# 0004
dogru=['II','III','I','IV']
sec=['I – II – III – IV','III – II – I – IV','II – I – III – IV','II – III – IV – I','II – III – I – IV']
def kisit(s):
    o=[x.strip() for x in s.split('–')]; return o.index('II')<o.index('III')<o.index('I')<o.index('IV')
assert [s for s in sec if kisit(s)]==['II – III – I – IV']
Q(P,'0004','K-CGKV-04','zor','İç ve dış kuvvetlerin yer şeklini değiştirme sırasını kurar.','öncüllü',4,
 'Bir bölgede aşağıdaki olaylar gerçekleşmiştir:\nI. Akarsuların yükselmiş kütlede derin vadiler açması\nII. Deniz tabanında tortul malzemenin birikmesi\nIII. Tortul tabakaların kıvrılarak karaya yükselmesi\nIV. Vadi yamaçlarındaki ayrışma ve aşınmayla vadilerin genişlemesi\nBu olaylar oluş sırasına göre aşağıdakilerden hangisinde doğru sıralanmıştır?',
 [(sec[0],'a','Olayları verilen numara sırasıyla dizmek; sıra olaylar arasındaki bağımlılığa göre kurulur.','dikkat'),(sec[1],'a','Tortulların biriken ve kıvrılan malzeme olduğunu unutup kıvrılmayı önce koymak.','bilgi'),(sec[2],'a','Akarsu vadisinin, kütle yükselmeden önce açılabileceğini sanmak.','bilgi'),(sec[3],'a','Vadi yamaçlarının vadi açılmadan önce aşındığını sanmak.','bilgi'),(sec[4],'d',None,None)],
 lambda e:e=='d','Olayların oluş sırası.',
 'Her olayın hangi olaydan sonra gerçekleşebileceğini sor: önce malzeme birikir, sonra yükselir.',[IC],
 [A('Önce malzeme','Tortullar denizde birikmeden kıvrılacak bir tabaka olmaz.','II birinci'),
  A('Sonra yükselme','Kıvrılma ve yükselme (iç kuvvet) karayı oluşturur; akarsu ancak karada vadi açar.','III, ardından I'),
  A('Vadiyi genişleme','Yamaçlardaki aşınma, vadi açıldıktan sonra olur.','II – III – I – IV')],
 'Sıralama sorularında her olay için ön koşulu bul: ne olmadan olamaz?','dört olaylı sıralama',harf='E')
bitir(P,'kuvvetler','cog|İç Kuvvetler / Dış Kuvvetler','İç Kuvvetler / Dış Kuvvetler')
