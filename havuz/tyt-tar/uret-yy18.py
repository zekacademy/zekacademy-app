import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('yy18','18. Yüzyılda Değişim ve Diplomasi','tar|18. Yüzyılda Değişim ve Diplomasi',4)
Q.kart('K-YYS-01','Lale Devri ve matbaa','III. Ahmed döneminde İbrahim Müteferrika 1727’de matbaayı kurmuş; Avrupa’daki yenilikler izlenmiştir.','Matbaanın kuruluş dönemini ya da ilk basılan eserleri karıştırmak.','kolay','yeni nesil',2,'yy18-matbaa','Lale Devri’nde matbaa')
Q.kart('K-YYS-02','Küçük Kaynarca Antlaşması','1774’te Kırım bağımsız sayılmış, Rus ticaret gemilerine Karadeniz ve Boğazlarda serbestlik tanınmış, tazminat ödenmiştir.','Osmanlı’nın kazançlı çıktığını sanmak.','orta','yeni nesil',3,'yy18-kucukkaynarca','Küçük Kaynarca Antlaşması')
Q.kart('K-YYS-03','III. Selim dönemi yenilikleri','Nizam-ı Cedid ordusu kuruldu; Avrupa başkentlerinde daimî elçilikler açıldı; Sened-i İttifak (1808) II. Mahmud dönemindedir.','Padişah–yenilik eşleşmesini karıştırmak.','orta','öncüllü',3,'yy18-selim','III. Selim dönemi yenilikleri')
Q.kart('K-YYS-04','Avrupa’ya elçi gönderme','XVIII. yüzyılda Avrupa’yı tanımak için elçiler gönderilmiş; Yirmisekiz Mehmed Çelebi 1720’de Fransa’ya gitmiş ve sefaretname yazmıştır.','Metinde olmayan sonucu söylenebilir sanmak.','zor','yeni nesil',4,'yy18-sefaret','Sefaretnameler ve Avrupa ile ilişkiler')
# 0001 E
Q.Y('0001','K-YYS-01','kolay','Lale Devri’nde matbaanın kurulmasını yorumlar.',
 'III. Ahmed döneminde sadrazam Nevşehirli Damat İbrahim Paşa’nın desteğiyle İbrahim Müteferrika, Avrupa’daki matbaacılıktan yararlanarak 1727’de İstanbul’da bir matbaa kurmuştur. Bu matbaada ilk olarak sözlük ve tarih gibi dinî olmayan eserler basılmıştır.\nBu parçaya göre matbaa ile ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Avrupa’daki bir yenilik Osmanlı’ya aktarılmıştır.',
 [('Matbaada ilk olarak dinî eserler basılmıştır.','Parçada ilk basılanların dinî olmayan eserler olduğu belirtilir.','dikkat'),
  ('Matbaa, Avrupa’dan hiç etkilenmeden geliştirilmiştir.','Parçada Avrupa’daki matbaacılıktan yararlanıldığı yazar.','dikkat'),
  ('Matbaayı kuran kişi sadrazam Nevşehirli Damat İbrahim Paşa’dır.','Matbaayı kuran İbrahim Müteferrika’dır; sadrazam yalnızca destek vermiştir.','dikkat'),
  ('Matbaa, III. Selim döneminde kurulmuştur.','Parçada matbaanın III. Ahmed döneminde kurulduğu belirtilir.','bilgi')],'E',
 'Parçadan çıkarılabilecek sonucun belirlenmesi.','Matbaayı kimin kurduğuna, kimin desteklediğine ve nelerden yararlanıldığına bak.',
 [('Türk matbaası','İbrahim Müteferrika, III. Ahmed döneminde (1727) matbaayı kurdu · Sadrazam Nevşehirli Damat İbrahim Paşa destek verdi · İlk basılan eserlerden biri Vankulu Lügati’dir.')],
 'Parçada kurucu, destekçi, tarih ve basılan eserler verilmiş.','Kurucu: Müteferrika · Destek: Damat İbrahim Paşa · Padişah: III. Ahmed','Avrupa’dan yararlanıldığı bilgisi, yeniliğin aktarıldığı yargısını doğrular.','Matbaa, Lale Devri’nde Avrupa’dan alınan bir yeniliktir.','Kurucu ile destekleyeni ayır: soru “kuran”ı mı, “destekleyen”i mi soruyor?','Özgün metin; MEB matbaa')
# 0002 D
Q.Y('0002','K-YYS-02','orta','Küçük Kaynarca Antlaşması’nın Osmanlı açısından sonuçlarını değerlendirir.',
 'Osmanlı Devleti, 1774’te Rusya ile yaptığı antlaşmayla Kırım Hanlığı’nı bağımsız saymış, Rus ticaret gemilerine Karadeniz’de ve Boğazlarda serbest geçiş hakkı tanımış ve Rusya’ya savaş tazminatı ödemeyi kabul etmiştir.\nBu parçaya göre bu antlaşma ile ilgili aşağıdakilerden hangisi söylenebilir?',
 'Osmanlı, Karadeniz’de Rusya’ya taviz vermiştir.',
 [('Osmanlı Devleti, Rusya’dan savaş tazminatı almıştır.','Parçada Osmanlı’nın Rusya’ya tazminat ödediği yazar.','dikkat'),
  ('Kırım Hanlığı Rusya’ya bağlanmıştır.','Parçada Kırım Hanlığı’nın bağımsız sayıldığı belirtilir.','dikkat'),
  ('Rus gemilerine yalnızca savaş zamanı geçiş izni verilmiştir.','Parçada ticaret gemilerine serbest geçiş hakkı tanındığı yazar.','dikkat'),
  ('Antlaşma Osmanlı’nın askerî üstünlüğünü pekiştirmiştir.','Parçadaki tavizler Osmanlı’nın üstünlüğünü değil gerilemesini gösterir.','bilgi')],'D',
 'Parçadan çıkarılabilecek sonucun belirlenmesi.','Antlaşmadaki her maddede kimin kazandığına ve kimin ödediğine bak.',
 [('Küçük Kaynarca Antlaşması (1774)','Osmanlı–Rus savaşı sonrası imzalandı · Kırım Hanlığı bağımsız sayıldı · Rus ticaret gemilerine serbest geçiş tanındı · Osmanlı Rusya’ya tazminat ödedi.')],
 'Parçadaki üç madde de Rusya lehinedir.','Kırım bağımsız · Rus gemileri serbest · tazminat ödeme','Osmanlı’nın Karadeniz’de Rusya’ya taviz verdiği sonucuna varılır.','Maddelerde kimin lehine olduğunu belirle; taraf karışırsa tüm şıklar kayar.','Antlaşma maddelerini “kim verdi, kim aldı” diye ikiye ayır.','Özgün metin; MEB Küçük Kaynarca')
# 0003 oncul
st=[('Nizam-ı Cedid adıyla yeni bir ordu kurulmuştur.',True,'Nizam-ı Cedid ordusu III. Selim döneminde kurulmuştur'),
    ('Avrupa başkentlerinde daimî elçilikler açılmıştır.',True,'Londra’da 1793’te ilk daimî elçilik açılmıştır'),
    ('Sened-i İttifak imzalanmıştır.',False,'Sened-i İttifak 1808’de II. Mahmud döneminde imzalanmıştır'),
    ('İbrahim Müteferrika matbaayı kurmuştur.',False,'Matbaa 1727’de III. Ahmed döneminde kurulmuştur')]
op,dg=oncul(st,['Yalnız I','Yalnız IV','I ve II','II ve III','III ve IV'],'C'); assert dg=={'I','II'}
Q.Y2('0003','K-YYS-03','orta','III. Selim dönemindeki yenilikleri ayırt eder.',
 metin_oncul('Aşağıdakilerden bazıları III. Selim dönemine ait gelişmeler olarak sıralanmıştır.',st,'Bu gelişmelerden hangileri III. Selim döneminde gerçekleşmiştir?'),op,'C',
 'III. Selim dönemine ait gelişmelerin belirlenmesi.','Sened-i İttifak ve matbaanın hangi padişah dönemlerine ait olduğunu hatırla.',
 [('III. Selim dönemi','Nizam-ı Cedid ordusu · Avrupa’da daimî elçilikler (Londra, 1793) · Sened-i İttifak II. Mahmud (1808), matbaa III. Ahmed (1727) dönemidir.')],
 'Her gelişmeyi padişahıyla eşle.','III. Selim: Nizam-ı Cedid, daimî elçilik','I ve II III. Selim dönemindedir.','Yenilikleri padişahlarıyla birlikte öğren: Ahmed–matbaa, Selim–Nizam-ı Cedid, Mahmud–Sened-i İttifak.','Padişah adını görünce o dönemin ayırt edici olayını hatırla.','III. Selim dönemine dair 4 öncül')
# 0004 B (söylenemez)
Q.Y('0004','K-YYS-04','zor','Elçilik raporlarına dayanarak Osmanlı’nın Avrupa’yla ilişkisini çıkarım yoluyla değerlendirir.',
 'Osmanlı Devleti, XVIII. yüzyılda Avrupa’daki gelişmeleri yakından tanımak amacıyla Avrupa ülkelerine elçiler göndermiştir. Bunlardan Yirmisekiz Mehmed Çelebi 1720’de Fransa’ya gitmiş ve gözlemlerini sefaretname adlı eserinde toplamıştır.\nBu parçadaki bilgilere göre aşağıdakilerden hangisi söylenemez?',
 'Fransa’ya giden elçinin önerileri tümüyle uygulanmıştır.',
 [('Osmanlı Devleti, Avrupa’daki gelişmelerle ilgilenmiştir.','Parçanın ilk cümlesi bunu söyler; yargı söylenebilir.','dikkat'),
  ('Elçilerin gözlemleri yazıya geçirilmiştir.','Parçada gözlemlerin sefaretnamede toplandığı belirtilir; yargı söylenebilir.','dikkat'),
  ('XVIII. yüzyılda Fransa’ya bir elçi gönderilmiştir.','Parçada Yirmisekiz Mehmed Çelebi’nin 1720’de Fransa’ya gittiği yazar; yargı söylenebilir.','dikkat'),
  ('Elçilik, Avrupa’yı tanıma amacına hizmet etmiştir.','Parçada elçilerin tanıma amacıyla gönderildiği belirtilir; yargı söylenebilir.','dikkat')],'B',
 'Parçada yer almayan (söylenemez) yargının belirlenmesi.','Kök “söylenemez” diyor: dört yargı parçada var, biri yok.',
 [('Sefaretname','Elçilerin gittikleri ülkeyi gözlemleyip yazdıkları rapor · Yirmisekiz Mehmed Çelebi’nin Fransa sefaretnamesi (1720) en bilinenidir.')],
 'Kökte “söylenemez” var; dört şık parçadan çıkarılır.','Dört şık parçada var · B’deki “önerilerin tamamı” yok','Önerilerin uygulanıp uygulanmadığı parçada belirtilmediği için o yargı söylenemez.','Metinde olmayan bir sonucu “doğru” saymamak için her şıkkı parçada ara.','Olumsuz köklerde parçada geçmeyen şıkkı seç.','Özgün metin; MEB sefaretname')
Q.bitir()
