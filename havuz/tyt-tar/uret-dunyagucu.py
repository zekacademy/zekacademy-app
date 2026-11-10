import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('dunyagucu','Dünya Gücü Osmanlı Devleti (1453-1600)','tar|Dünya Gücü Osmanlı Devleti (1453-1600)',4)
Q.zd={'kolay': 2, 'orta': 2}
Q.kart('K-DGO-01','İstanbul’un fethi','1453’te Fatih Sultan Mehmed İstanbul’u fethetmiş, Bizans sona ermiş, Orta Çağ kapanıp Yeni Çağ başlamıştır.','Fetih sonucunu Orta Çağ’ın başlangıcı sanmak.','kolay','yeni nesil',2,'dgo-fetih','İstanbul’un fethi ve sonuçları')
Q.kart('K-DGO-02','Preveze Deniz Savaşı','1538’de Barbaros Hayrettin Paşa komutasındaki donanma Haçlı donanmasını yenmiş, Akdeniz’de üstünlük sağlanmıştır.','Zaferin sonucunu yenilgi ya da tersi sanmak.','orta','yeni nesil',3,'dgo-preveze','Preveze Deniz Savaşı')
Q.kart('K-DGO-03','Yavuz Sultan Selim’in doğu seferleri','Çaldıran (Safevi), Mercidabık ve Ridaniye (Memlük) savaşları; Mısır’ın katılması.','Savaşın karşı tarafını karıştırmak.','orta','öncüllü',3,'dgo-yavuz','Yavuz Sultan Selim dönemi savaşları')
Q.kart('K-DGO-04','Coğrafi keşifler ve Osmanlı','Ümit Burnu yolu ticareti Akdeniz’den uzaklaştırdı; Osmanlı Kızıldeniz ve Hint Okyanusu’nda Portekiz’e karşı donanma gönderdi.','Metinde olmayan sonucu doğru sanmak.','kolay','yeni nesil',4,'dgo-kesif','Coğrafi keşiflerin Osmanlı üzerindeki etkisi')
# 0001 B
Q.Y('0001','K-DGO-01','kolay','İstanbul’un fethinin sonuçlarını yorumlar.',
 'Fatih Sultan Mehmed, 1453’te İstanbul’u büyük bir ordu ve güçlü toplarla kuşatarak fethetmiştir. Bu fetih, Bizans İmparatorluğu’nun varlığına son vermiş; tarihçiler tarafından Orta Çağ’ın sona erişi olarak kabul edilmiştir.\nBu parçaya göre İstanbul’un fethi ile ilgili aşağıdakilerden hangisi söylenebilir?',
 'Bizans İmparatorluğu’nun siyasi varlığı sona ermiştir.',
 [('Orta Çağ’ın başlangıcı sayılmıştır.','Parçada fetih, Orta Çağ’ın başlangıcı değil sona erişi olarak anılır.','dikkat'),
  ('Bizans İmparatorluğu’nun yeni başkenti olmuştur.','Fetih, Bizans’ın varlığına son vermiştir; başkent olması söz konusu değildir.','bilgi'),
  ('Kuşatmada top gibi ateşli silahlar kullanılmamıştır.','Parçada güçlü topların kullanıldığı belirtilir.','dikkat'),
  ('Fethi Fatih’in babası II. Murad gerçekleştirmiştir.','Parçada fethi yapan padişahın Fatih Sultan Mehmed olduğu yazar.','dikkat')],'B',
 'Parçadan çıkarılabilecek sonucun belirlenmesi.','Parçanın “varlığına son vermiş” ifadesine ve Orta Çağ ile ilgili cümleye dikkat et.',
 [('İstanbul’un fethi','1453’te Fatih Sultan Mehmed İstanbul’u fethetti · Bizans İmparatorluğu yıkıldı · Orta Çağ sona erdi, Yeni Çağ başladı.')],
 'Parçada fethi yapan, kullanılan silah ve fethin sonuçları yazılı.','Fetih 1453 = Bizans’ın sonu = Orta Çağ’ın sonu','Parçayla uyuşan tek şık Bizans’ın siyasi varlığının bitmesidir.','1453, Orta Çağ’ın bitişi ve Yeni Çağ’ın başlangıcıdır; bunu “başlangıç/bitiş” karışıklığına düşmeden öğren.','Tarih sınırlarında “sona erdi” ve “başladı” sözcüklerini ayrı ayrı işaretle.','Özgün metin; 1453 MEB')
# 0002 A
Q.Y('0002','K-DGO-02','orta','Preveze Deniz Savaşı’nın sonuçlarını değerlendirir.',
 'Barbaros Hayrettin Paşa komutasındaki Osmanlı donanması, 1538’de Preveze açıklarında Akdeniz’deki Haçlı donanmasıyla karşılaşmış ve onu yenmiştir. Bu zaferden sonra Osmanlı Devleti Akdeniz’de uzun süre üstünlük sağlamıştır.\nBu bilgilere göre Preveze Deniz Savaşı ile ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Osmanlı’nın Akdeniz’deki deniz gücü artmıştır.',
 [('Osmanlı donanması yenilgiye uğramıştır.','Parçada Osmanlı donanmasının Haçlı donanmasını yendiği belirtilir.','dikkat'),
  ('Osmanlı’nın Akdeniz’deki etkinliği kısa sürede sona ermiştir.','Parçada zaferden sonra uzun süre üstünlük sağlandığı yazar.','dikkat'),
  ('Savaşı Haçlı donanmasının komutanı kazanmıştır.','Savaşı Barbaros Hayrettin Paşa komutasındaki Osmanlı donanması kazanmıştır.','bilgi'),
  ('Barbaros Hayrettin Paşa bu savaşta şehit düşmüştür.','Parçada böyle bir bilgi yoktur; ayrıca Barbaros savaştan sonra da görev yapmıştır.','bilgi')],'A',
 'Parçadan çıkarılabilecek sonucun belirlenmesi.','Savaşın kazananına ve zaferin Akdeniz’deki sonucuna bak.',
 [('Preveze Deniz Savaşı','1538 · Barbaros Hayrettin Paşa komutasındaki Osmanlı donanması, Haçlı donanmasını yendi · Akdeniz’de Osmanlı üstünlüğü başladı.')],
 'Parçada savaşın tarihi, komutanı, sonucu ve etkisi yazılı.','1538 Preveze = Osmanlı zaferi = Akdeniz’de üstünlük','Parçaya göre Osmanlı’nın deniz gücü artmıştır.','Preveze (1538) Osmanlı’nın Akdeniz’de güç kazandığı savaştır.','Savaşın kazananını ilk cümleden belirle; şıklardaki tersine çıkarımları ele.','Özgün metin; MEB Preveze')
# 0003 oncul
st=[('Çaldıran Savaşı’nda Osmanlı ordusu Safevi ordusunu yenmiştir.',True,'Çaldıran 1514’te Safevilere karşı kazanılmıştır'),
    ('Mercidabık Savaşı, Safeviler ile yapılmıştır.',False,'Mercidabık (1516) Memlüklerle yapılmıştır'),
    ('Ridaniye Savaşı, Memlük Devleti’nin yıkılmasına yol açmıştır.',True,'Ridaniye (1517) sonrası Memlük Devleti sona ermiştir'),
    ('Ridaniye Savaşı’ndan sonra Mısır, Osmanlı topraklarına katılmıştır.',True,'Memlüklerin yıkılmasıyla Mısır Osmanlı’ya geçmiştir')]
op,dg=oncul(st,['Yalnız II','I ve III','I ve IV','II ve III','I, III ve IV'],'E'); assert dg=={'I','III','IV'}
Q.Y2('0003','K-DGO-03','orta','Yavuz Sultan Selim döneminde yapılan savaşları karşı taraflarıyla eşleştirir.',
 metin_oncul('Yavuz Sultan Selim döneminde yapılan savaşlarla ilgili şu bilgiler verilmiştir:',st,'Bu bilgilerden hangileri doğrudur?'),op,'E',
 'Doğru öncüllerin belirlenmesi.','Çaldıran’ın Safevilere, Mercidabık ve Ridaniye’nin Memlüklere karşı yapıldığını hatırla.',
 [('Yavuz Sultan Selim dönemi savaşları','Çaldıran (1514): Safeviler · Mercidabık (1516) ve Ridaniye (1517): Memlükler · Ridaniye sonrası Memlük Devleti yıkıldı, Mısır katıldı.')],
 'Her savaşın karşı tarafını ve sonucunu ayrı ayrı sına.','Çaldıran–Safevi · Mercidabık, Ridaniye–Memlük','Doğru öncüller I, III ve IV’tür.','Savaş adını karşı devletle eşle: Çaldıran Safevi, Mercidabık ve Ridaniye Memlük.','Savaşın adı ile karşı devletini birlikte öğren.','Üç savaş, iki rakip')
# 0004 C (söylenemez)
Q.Y('0004','K-DGO-04','kolay','Coğrafi keşiflerin Osmanlı dış politikasına etkisini çıkarım yoluyla değerlendirir.',
 'Ümit Burnu’nun keşfiyle Portekizliler, Hindistan’a okyanus yoluyla ulaşmış ve baharatı Akdeniz’e uğramadan Avrupa’ya taşımaya başlamıştır. Bu gelişme üzerine Osmanlı Devleti, Kızıldeniz ve Hint Okyanusu’nda Portekizlilere karşı donanma göndermiştir.\nBu parçadaki bilgilere göre aşağıdakilerden hangisi söylenemez?',
 'Osmanlı donanması, Portekizlileri Hint Okyanusu’ndan çıkarmıştır.',
 [('Portekizliler baharatı Akdeniz’e uğramadan Avrupa’ya taşıyabilmiştir.','Bu yargı parçanın ilk cümlesinde açıkça yer aldığı için söylenebilir; soruda “söylenemez” olan aranıyor.','dikkat'),
  ('Osmanlı Devleti, ticaret yollarındaki değişime donanmayla karşılık vermiştir.','Parçada donanma gönderildiği yazar; bu yargı söylenebilir.','dikkat'),
  ('Ümit Burnu’nun keşfi, Hindistan’a okyanus yoluyla ulaşılmasını sağlamıştır.','Parçada bu bilgi açıkça yer alır; yargı söylenebilir.','dikkat'),
  ('Osmanlı Devleti’nin donanması Kızıldeniz’de faaliyet göstermiştir.','Parçada Kızıldeniz’e donanma gönderildiği belirtilir; yargı söylenebilir.','dikkat')],'C',
 'Parçada yer almayan (söylenemez) yargının belirlenmesi.','Kök “söylenemez” diyor: parçadan çıkarılabilen dört yargıyı ele, kalanını seç.',
 [('Coğrafi keşifler','Ümit Burnu yolu (Vasco da Gama, 1498) ile Hindistan’a deniz yoluyla ulaşıldı · Baharat ticareti Akdeniz yolundan uzaklaştı · Osmanlı Kızıldeniz ve Hint Okyanusu’nda Portekiz’e karşı donanma gönderdi.')],
 'Kökte “söylenemez” var; dört şık parçadan çıkarılabilir, biri çıkarılamaz.','Parçada seferlerin sonucundan söz edilmediği için Portekizlilerin Hint Okyanusu’ndan çıkarıldığı yargısı söylenemez.','Dört şık parçada var · C’deki Portekizlilerin Hint Okyanusu’ndan çıkarıldığı yok','“Söylenemez” kökünde dört doğru yargıyı bul, geriye kalanı işaretle.','Kökte olumsuz ifade (söylenemez, ulaşılamaz) varsa her şıkkı “parçada var mı?” diye sına.','Özgün metin; MEB coğrafi keşifler')
Q.bitir()
