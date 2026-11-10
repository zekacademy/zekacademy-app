import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('yenicag','Yeni Çağ Avrupa Tarihi','tar|Yeni Çağ Avrupa Tarihi',4)
Q.zd={'kolay': 2, 'orta': 2}
Q.kart('K-YCA-01','Coğrafi keşifler','Kolomb 1492’de Hindistan’a batıdan ulaşmayı hedeflemiş, Amerika’ya ulaşmıştır.','Hedefi ile sonucu karıştırmak.','kolay','yeni nesil',2,'yca-kesif','Kolomb seferi')
Q.kart('K-YCA-02','Reform hareketi','Luther 1517’de af belgesi satışını eleştiren 95 tezi yayımlamış, Kilise’nin otoritesi sorgulanmaya başlamıştır.','Reformu Kilise’nin güçlenmesi sanmak.','orta','yeni nesil',3,'yca-reform','Reform hareketinin başlangıcı')
Q.kart('K-YCA-03','Aydınlanma düşünürleri','Montesquieu–Kanunların Ruhu (kuvvetler ayrılığı), Rousseau–Toplum Sözleşmesi.','Eser–düşünür eşleşmesini karıştırmak.','orta','öncüllü',3,'yca-aydinlanma','Aydınlanma düşünürleri ve eserleri')
Q.kart('K-YCA-04','Sanayi İnkılabı','İngiltere’de kömür–demir zenginliği, sömürge hammaddesi ve sermaye birikimi ile buhar gücü fabrikaları ve işçi sınıfını doğurmuştur.','Hammaddenin yalnız yerli olduğunu sanmak.','kolay','yeni nesil',4,'yca-sanayi','Sanayi İnkılabı’nın nedenleri ve sonuçları')
# 0001 C
Q.Y('0001','K-YCA-01','kolay','Kolomb seferinin amacı ile sonucunu ayırt eder.',
 'Kristof Kolomb, Hindistan’a batı yönünden giderek ulaşmayı amaçlamış ve 1492’de yola çıkmıştır. Bu yolculuğun sonunda Amerika kıtasına ulaşmıştır.\nBu parçaya göre Kolomb’un seferi ile ilgili aşağıdakilerden hangisi söylenebilir?',
 'Hedeflediğinden farklı bir kıtaya ulaşmıştır.',
 [('Yolculuğu doğu yönünde yapmıştır.','Parçada Hindistan’a batı yönünden gitmek istediği yazar.','dikkat'),
  ('Amaçladığı gibi Hindistan’a ulaşmıştır.','Parçada yolculuğun sonunda Amerika kıtasına ulaştığı belirtilir.','dikkat'),
  ('Amerika’yı keşfetmek amacıyla yola çıkmıştır.','Parçada amacın Hindistan’a ulaşmak olduğu yazar.','dikkat'),
  ('Yolculuğuna 1498’de başlamıştır.','Parçada yolculuğun 1492’de başladığı belirtilir.','bilgi')],'C',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Seferin amacını ve ulaşılan yeri ayrı ayrı bul.',
 [('Kolomb’un seferi (1492)','Kolomb Hindistan’a batı yönünden ulaşmak istedi · Amerika kıtasına ulaştı.')],
 'Parçada amaç, yön, tarih ve sonuç verilmiş.','Amaç: Hindistan · Sonuç: Amerika · Yıl: 1492','Hedefle sonucun farklı olduğu yargısı parçayla uyuşur.','Kolomb 1492’de Hindistan’a ulaşmaya çalışırken Amerika’ya ulaşmıştır.','Amaç ile sonucu ayır; “amaçladığı” ve “ulaştığı” ayrı şeylerdir.','Özgün metin; MEB coğrafi keşifler')
# 0002 B
Q.Y('0002','K-YCA-02','orta','Reform hareketinin başlangıcını yorumlar.',
 'Martin Luther, 1517’de Katolik Kilisesi’nin af belgesi satışını eleştiren 95 maddelik tezlerini yayımlamıştır. Bu eleştiriler kısa sürede Almanya’da yayılmış ve Kilise’nin otoritesi sorgulanmaya başlanmıştır.\nBu parçaya göre Luther’in eleştirileri ile ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Kilise’nin Hristiyan toplumundaki otoritesi tartışılır hâle gelmiştir.',
 [('Kilise af belgesi satışını artırmıştır.','Parçada Luther’in af belgesi satışını eleştirdiği yazar; satışın artırıldığı belirtilmez.','dikkat'),
  ('Eleştiriler yalnızca Almanya sınırları içinde kalmış, tartışma yaratmamıştır.','Parçada eleştirilerin yayıldığı ve otoritenin sorgulandığı belirtilir.','dikkat'),
  ('Luther’in tezleri Kilise tarafından olduğu gibi kabul edilmiştir.','Parçada Kilise’nin otoritesinin sorgulandığı yazar; tezlerin kabul edildiği belirtilmez.','bilgi'),
  ('Tezler 1492’de yayımlanmıştır.','Parçada tezlerin 1517’de yayımlandığı belirtilir.','bilgi')],'B',
 'Parçadan çıkarılabilecek sonucun belirlenmesi.','Eleştirinin konusuna ve Kilise’nin otoritesine olan etkisine bak.',
 [('Reform hareketi','Luther 1517’de Kilise’nin af belgesi satışını eleştiren 95 tezi yayımladı · Kilise’nin otoritesi sorgulanmaya başladı · Protestanlık doğdu.')],
 'Parçada eleştirinin konusu, yayılması ve etkisi verilmiş.','Luther: 1517 · 95 tez · Kilise otoritesi tartışılır','Kilise otoritesinin tartışılır hâle gelmesi parçayla uyuşur.','Reform, Kilise’nin otoritesinin sorgulanmasıyla başlar.','Neden (eleştirinin konusu) ile sonucu (otoritenin sorgulanması) ayır.','Özgün metin; MEB Reform')
# 0003 A oncul
st=[('Kuvvetler ayrılığı fikri, “Kanunların Ruhu” adlı eserde Montesquieu tarafından savunulmuştur.',True,'Kanunların Ruhu Montesquieu’nun eseridir'),
    ('“Toplum Sözleşmesi” adlı eser Voltaire’indir.',False,'Toplum Sözleşmesi Rousseau’nun eseridir'),
    ('“Kanunların Ruhu” adlı eser Rousseau’ya aittir.',False,'Kanunların Ruhu Montesquieu’nundur')]
op,dg=oncul(st,['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],'A'); assert dg=={'I'}
Q.Y2('0003','K-YCA-03','orta','Aydınlanma düşünürlerini eserleriyle eşleştirir.',
 metin_oncul('Aydınlanma Çağı düşünürleri ve eserleriyle ilgili şu bilgiler verilmiştir:',st,'Bu bilgilerden hangileri doğrudur?'),op,'A',
 'Doğru öncüllerin belirlenmesi.','Hangi eserin hangi düşünüre ait olduğunu tek tek hatırla.',
 [('Aydınlanma düşünürleri','Montesquieu: Kanunların Ruhu (kuvvetler ayrılığı) · Rousseau: Toplum Sözleşmesi (halk egemenliği).')],
 'Eserleri düşünürleriyle eşleştir.','Montesquieu–Kanunların Ruhu · Rousseau–Toplum Sözleşmesi','Yalnız I doğrudur.','Eser adını düşünürle birlikte öğren: Kanunların Ruhu–Montesquieu, Toplum Sözleşmesi–Rousseau.','Her öncülde kişi–eser çiftini ayrı kontrol et.','Üç eşleştirme, bir doğru')
# 0004 E
Q.Y('0004','K-YCA-04','kolay','Sanayi İnkılabı’nın İngiltere’de başlamasının nedenlerini çıkarım yoluyla değerlendirir.',
 'Sanayi İnkılabı’nın İngiltere’de başlamasında, bu ülkenin kömür ve demir kaynaklarına sahip olması, sömürgelerinden hammadde sağlaması ve sermaye birikimi etkili olmuştur. Buhar makinesinin üretimde kullanılmasıyla fabrikalar kurulmuş, işçi sınıfı oluşmuştur.\nBu parçadaki bilgilere göre aşağıdakilerden hangisi söylenemez?',
 'Fabrikalaşma sonucunda işçi sınıfı ortadan kalkmıştır.',
 [('Kömür ve demir kaynakları sanayileşmeyi kolaylaştırmıştır.','Parçada bu kaynakların etkili olduğu yazar; yargı söylenebilir.','dikkat'),
  ('Sömürgeler, sanayinin hammadde ihtiyacının karşılanmasında rol oynamıştır.','Parçada sömürgelerden hammadde sağlandığı yazar; yargı söylenebilir.','dikkat'),
  ('Buhar gücünün üretimde kullanılması fabrikaların kurulmasına yol açmıştır.','Parçada bu bilgi yer alır; yargı söylenebilir.','dikkat'),
  ('Üretim biçimindeki değişim yeni bir işçi sınıfının oluşmasıyla sonuçlanmıştır.','Parçada işçi sınıfının oluştuğu belirtilir; yargı söylenebilir.','dikkat')],'E',
 'Parçada yer almayan (söylenemez) yargının belirlenmesi.','Kök “söylenemez” diyor: dört yargı parçada var, biri çelişiyor.',
 [('Sanayi İnkılabı','İngiltere’de başladı · Kömür–demir kaynakları, sömürge hammaddesi ve sermaye birikimi etkili oldu · Buhar makinesiyle fabrikalar ve işçi sınıfı doğdu.')],
 'Kökte “söylenemez” var; dört şık parçada yazılı.','Parça işçi sınıfının oluştuğunu söylediği için sınıfın ortadan kalktığı yargısı söylenemez.','Dört şık parçada var · E’deki işçi sınıfının ortadan kalktığı yargısı parçayla çelişir','Olumsuz kökte parçayla çelişen şıkkı bul.','Olumsuz kökte parçayla çelişen şıkkı bul.','Özgün metin; MEB Sanayi İnkılabı')
Q.bitir()
