import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('enuzun','En Uzun Yüzyıl','tar|En Uzun Yüzyıl',4)
Q.kart('K-EUY-01','Tanzimat Fermanı','1839’da ilan edilen fermanla can, mal ve namus güvenliği, adil vergi ve düzenli askerlik esasları getirilmiştir.','Fermanı yalnız Müslümanlara ait sanmak ya da meclis kuran belge sanmak.','kolay','yeni nesil',2,'euy-tanzimat','Tanzimat Fermanı’nın esasları')
Q.kart('K-EUY-02','Kanun-ı Esasi','1876’da ilan edilen ilk anayasada Ayan Meclisi atamayla, Mebusan Meclisi seçimle oluşmuş; padişah meclisi dağıtma yetkisini korumuştur.','Meclisin tamamını seçimli sanmak.','orta','yeni nesil',3,'euy-kanunesasi','Kanun-ı Esasi’nin özellikleri')
Q.kart('K-EUY-03','Islahat Fermanı','1856’da ilan edilen fermanla gayrimüslimlere Müslümanlarla eşit haklar tanınmıştır.','Islahat ile Tanzimat ya da Kanun-ı Esasi’yi karıştırmak.','orta','öncüllü',3,'euy-islahat','Islahat Fermanı’nın özellikleri')
Q.kart('K-EUY-04','XIX. yüzyıl olayları kronolojisi','Sened-i İttifak (1808), Yunan isyanı (1821), Vaka-i Hayriye (1826), Tanzimat (1839), Kırım Savaşı (1853).','Vaka-i Hayriye ile Yunan isyanı sırasını karıştırmak.','zor','yeni nesil',4,'euy-kronoloji','XIX. yüzyıl olaylarının sıralanması')
# 0001 A
Q.Y('0001','K-EUY-01','kolay','Tanzimat Fermanı’nın getirdiği esasları yorumlar.',
 '1839’da ilan edilen fermanda, bütün tebaanın can, mal ve namus güvenliğinin güvence altına alınacağı, vergilerin herkesin gücüne göre toplanacağı ve askerliğin belirli bir süreyle sınırlandırılacağı belirtilmiştir.\nBu parçaya göre ferman ile ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Bireylerin hak ve güvenliği güvence altına alınmıştır.',
 [('Padişahın bütün yetkileri bir meclise devredilmiştir.','Parçada böyle bir düzenlemeden söz edilmez; ferman bir meclis kurmaz.','bilgi'),
  ('Yalnızca Müslüman tebaanın hakları güvence altına alınmıştır.','Parçada “bütün tebaa” ifadesi geçer; yargı bununla çelişir.','dikkat'),
  ('Vergiler herkesten eşit miktarda alınacaktır.','Parçada vergilerin gücüne göre alınacağı yazar; eşit miktar değil.','dikkat'),
  ('Askerlik süresi belirsiz bırakılmıştır.','Parçada askerliğin belirli bir süreyle sınırlandırıldığı belirtilir.','dikkat')],'A',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Ferman maddelerinde kimlerin kapsandığına ve neyin sınırlandığına bak.',
 [('Tanzimat Fermanı (1839)','Gülhane Hatt-ı Hümayunu da denir · Can, mal ve namus güvenliği, adil vergi, düzenli askerlik esasları getirildi.')],
 'Parçada üç temel esas (güvenlik, vergi, askerlik) yazılı.','Güvenlik · adil vergi · süreli askerlik','Hak ve güvenliğin güvence altına alınması yargısı parçayla uyuşur.','Tanzimat, hukuki güvenceyi ve eşitliği öne çıkaran bir fermandır.','Fermanın kapsamını (“bütün tebaa”) ve her maddeyi parçadan oku.','Özgün metin; MEB Tanzimat')
# 0002 E
Q.Y('0002','K-EUY-02','orta','Kanun-ı Esasi’nin yönetime getirdiği değişiklikleri yorumlar.',
 '1876’da ilan edilen Kanun-ı Esasi ile Osmanlı Devleti’nde ilk kez yazılı bir anayasa yürürlüğe girmiştir. Meclis iki kamaralı kurulmuş; Mebusan Meclisi üyeleri seçimle gelirken Ayan Meclisi üyelerini padişah atamıştır. Padişah, meclisi dağıtma yetkisini de elinde tutmuştur.\nBu parçaya göre Kanun-ı Esasi ile ilgili aşağıdakilerden hangisi söylenebilir?',
 'Padişah yasama organı üzerindeki etkisini sürdürmüştür.',
 [('Meclisin bütün üyeleri halk tarafından seçilmiştir.','Ayan Meclisi üyelerini padişah atamıştır; hepsi seçimle gelmemiştir.','dikkat'),
  ('Padişahın meclisi dağıtma yetkisi kaldırılmıştır.','Parçada padişahın bu yetkiyi elinde tuttuğu yazar.','dikkat'),
  ('Yönetim biçimi cumhuriyete dönüştürülmüştür.','Parçada böyle bir değişiklikten söz edilmez; padişahlık sürmektedir.','bilgi'),
  ('Osmanlı Devleti’nde anayasa ilk kez bu dönemde kaldırılmıştır.','Parçada anayasanın ilk kez yürürlüğe girdiği belirtilir; kaldırılmasından söz edilmez.','dikkat')],'E',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Padişahın elinde kalan yetkilere ve meclisin oluşumuna bak.',
 [('Kanun-ı Esasi (1876)','İlk Osmanlı anayasasıdır · Mebusan Meclisi seçimle, Ayan Meclisi padişah atamasıyla oluşur · Padişah meclisi dağıtabilir.')],
 'Parçada meclisin oluşumu ve padişahın yetkisi verilmiş.','Mebusan: seçim · Ayan: atama · Padişah: dağıtma yetkisi','Meclisi dağıtma yetkisi padişahın etkisini sürdürdüğünü gösterir.','Kanun-ı Esasi padişahın yetkilerini kısıtlar ancak tümüyle kaldırmaz.','Parçada “yetki kaldı mı, kalktı mı?” sorusunu cümleden çöz.','Özgün metin; MEB Kanun-ı Esasi')
# 0003 oncul
st=[('1856’da ilan edilmiştir.',True,'Islahat Fermanı 1856’da ilan edilmiştir'),
    ('Gayrimüslimlere Müslümanlarla eşit haklar tanıyan maddeler içerir.',True,'fermanın en önemli maddeleri gayrimüslimlerle ilgilidir'),
    ('Osmanlı Devleti’nin ilk yazılı anayasasıdır.',False,'ilk yazılı anayasa Kanun-ı Esasi’dir, 1876'),
    ('Yeniçeri Ocağı bu fermanla kaldırılmıştır.',False,'Yeniçeri Ocağı 1826’da Vaka-i Hayriye ile kaldırılmıştır')]
op,dg=oncul(st,['Yalnız II','I ve II','I ve III','II ve IV','III ve IV'],'B'); assert dg=={'I','II'}
Q.Y2('0003','K-EUY-03','orta','Islahat Fermanı’nın özelliklerini ayırt eder.',
 metin_oncul('Islahat Fermanı ile ilgili şu bilgiler verilmiştir:',st,'Bu bilgilerden hangileri doğrudur?'),op,'B',
 'Doğru öncüllerin belirlenmesi.','Fermanın tarihini ve kimleri ilgilendirdiğini düşün; III ve IV başka belgelerin özelliğidir.',
 [('Islahat Fermanı (1856)','Kırım Savaşı’nın sonunda ilan edildi · Gayrimüslimlere Müslümanlarla eşit haklar getirdi · İlk anayasa Kanun-ı Esasi (1876), Yeniçeri Ocağı’nın kaldırılması Vaka-i Hayriye (1826)’dir.')],
 'Her öncülü Islahat Fermanı’nın özellikleriyle karşılaştır.','Islahat 1856 · gayrimüslim hakları','I ve II doğrudur.','Belgelerin karşılığını öğren: Tanzimat 1839, Islahat 1856, Kanun-ı Esasi 1876.','Aynı yüzyıldaki üç belgeyi tarih ve içerikle ayır.','Dört öncül, iki doğru')
# 0004 D kronoloji
ev={'I':('Tanzimat Fermanı’nın ilanı',1839),'II':('Sened-i İttifak’ın imzalanması',1808),'III':('Kırım Savaşı’nın başlaması',1853),'IV':('Vaka-i Hayriye',1826),'V':('Yunan isyanının başlaması',1821)}
op,dg=kron(ev,[['II','IV','V','I','III'],['V','II','IV','I','III'],['II','V','I','IV','III'],['II','V','IV','I','III'],['II','V','IV','III','I']]); assert dg=='II – V – IV – I – III'
Q.Y2('0004','K-EUY-04','zor','XIX. yüzyıl olaylarını kronolojik sıraya koyar.',
 'XIX. yüzyılda Osmanlı Devleti’nde yaşanan bazı gelişmeler aşağıda verilmiştir.\nI. Tanzimat Fermanı’nın ilanı\nII. Sened-i İttifak’ın imzalanması\nIII. Kırım Savaşı’nın başlaması\nIV. Vaka-i Hayriye (Yeniçeri Ocağı’nın kaldırılması)\nV. Yunan isyanının başlaması\nBu gelişmeler eskiden yeniye doğru sıralandığında aşağıdakilerden hangisi elde edilir?',op,'D',
 'Gelişmelerin eskiden yeniye doğru sıralanması.','Padişahları sırala: II. Mahmud dönemi olayları Tanzimat’tan önce, Kırım Savaşı ise sonra gelir.',
 [('Olay tarihleri','Sened-i İttifak 1808 · Yunan isyanı 1821 · Vaka-i Hayriye 1826 · Tanzimat 1839 · Kırım Savaşı 1853')],
 'Beş olayın tarihini hatırla ve sırala.','1808 < 1821 < 1826 < 1839 < 1853','Sıralama II – V – IV – I – III olur.','II. Mahmud dönemi (1808–1839) olaylarını Tanzimat’tan önce, Kırım Savaşı’nı sonra yerleştir.','Padişah dönemine göre grupla: II. Mahmud olayları, sonra Abdülmecid olayları.','Beş olayın sıralaması',kalip='yeni nesil')
Q.bitir()
