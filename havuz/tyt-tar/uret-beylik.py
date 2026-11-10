import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('beylik','Beylikten Devlete Osmanlı Siyaseti(1300-1453)','tar|Beylikten Devlete Osmanlı Siyaseti(1300-1453)',4)
Q.zd={'kolay': 1, 'orta': 3}
Q.kart('K-BYL-01','Osmanlı Beyliği’nin kuruluş koşulları','Osmanlı Beyliği, Bizans sınırındaki uç bölgesinde kurulmuş; gazilerin katıldığı akınlarla büyümüştür.','Beyliğin kuruluş yerini Selçuklu merkezi ya da Bizans içi sanmak.','kolay','yeni nesil',2,'byl-kurulus','Kuruluş koşulları ve uç bölgesi')
Q.kart('K-BYL-02','Rumeli’de iskân ve istimalet','Fethedilen Balkan topraklarına Türkmen iskânı yapılmış, yerli halka istimalet (gönül alma) uygulanmıştır.','İstimaleti zorla göçürme sanmak.','orta','yeni nesil',3,'byl-iskan','Rumeli’de iskân ve istimalet')
Q.kart('K-BYL-03','Ankara Savaşı ve Fetret Devri','1402 Ankara Savaşı sonrası şehzade mücadeleleri (Fetret) 1413’te Çelebi Mehmed ile sona ermiştir.','Fetret Devri’ni bitiren padişahı karıştırmak.','orta','öncüllü',3,'byl-fetret','Ankara Savaşı ve Fetret Devri')
Q.kart('K-BYL-04','Savaşların kronolojisi','Niğbolu (1396), Ankara (1402), Varna (1444), II. Kosova (1448) sıralaması.','Varna ile II. Kosova sırasını ters kurmak.','orta','yeni nesil',4,'byl-kronoloji','Savaşların kronolojik sıralaması')
# 0001 -> C
Q.Y('0001','K-BYL-01','kolay','Osmanlı Beyliği’nin kuruluşunda uç bölgesinin rolünü yorumlar.',
 'Osmanlı Beyliği, Anadolu Selçuklu Devleti’nin batı ucunda, Bizans ile komşu bir bölgede kurulmuştur. Beylik, ilk yıllarında Bizans topraklarına düzenlediği akınlarla genişlemiş; bu akınlara Anadolu’nun çeşitli yerlerinden gelen gaziler de katılmıştır.\nBu parçaya göre Osmanlı Beyliği ile ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Bizans’la komşu bölgede kurulması genişlemesinde etkili olmuştur.',
 [('Genişlemesini Bizans ile yaptığı ittifaklara dayandırmıştır.','Metinde Bizans’la ittifaktan değil, Bizans topraklarına yapılan akınlardan söz edilir.','dikkat'),
  ('Kuruluşu, Selçuklu başkentine yakın bir bölgede gerçekleşmiştir.','Beylik, Selçuklu’nun batı ucunda ve Bizans sınırında kurulmuştur; merkeze yakın değildir.','bilgi'),
  ('Akınlara yalnızca kendi boyundan olan savaşçılar katılmıştır.','Parçada Anadolu’nun çeşitli yerlerinden gelen gazilerin de katıldığı belirtilir.','dikkat'),
  ('Yayılma sürecinde diğer Türk beyliklerine karşı savaşmıştır.','Metinde başka Türk beyliklerine karşı bir savaştan söz edilmez; akınlar Bizans’a yöneliktir.','bilgi')],'C',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Beyliğin nerede kurulduğuna ve akınların kime yöneldiğine bak.',
 [('Uç beyliği','Uç, devletin sınır bölgesidir; uç beylikleri komşu devletin topraklarına akın düzenleyerek büyürdü · Osmanlı Beyliği, Bizans sınırındaki bir uç beyliğiydi.')],
 'Parçada kuruluş yeri (Selçuklu’nun batı ucu, Bizans sınırı) ve akınların yönü (Bizans) verilmiş.','Uç beyliği: sınır komşusuna akın yaparak büyüyen beylik.','Bizans’a komşu = Bizans topraklarına akın = genişleme','Parçayla örtüşen tek yargı, sınır komşusuna yönelmenin genişlemede etkili olduğudur.','Metne dayalı sorularda şıkkı bilginle değil, parçadaki cümleyle sına.','Özgün metin; MEB uç beyliği bilgisi')
# 0002 -> A
Q.Y('0002','K-BYL-02','orta','Osmanlı’nın Balkanlardaki iskân ve istimalet politikasını yorumlar.',
 'Osmanlı Devleti, Balkanlarda fethettiği yerlerde yerel halkın can, mal ve inanç güvenliğini korumuş, halktan alınan vergileri ağır tutmamıştır. Öte yandan Anadolu’dan getirilen Türkmen aileler, bu bölgelere yerleştirilmiştir.\nBu parçaya göre Osmanlı Devleti’nin Balkanlardaki politikası için aşağıdakilerden hangisi söylenebilir?',
 'Yerli halkın güvenliğini korurken Türkmen nüfusu da yerleştirmiştir.',
 [('Yerli halkı bölgeden çıkararak yerine yalnızca askerleri yerleştirmiştir.','Parça yerli halkın korunduğunu söyler; halkın çıkarıldığına dair bilgi yoktur.','dikkat'),
  ('Fethedilen yerlerdeki vergileri Anadolu’dakilerden daha ağır tutmuştur.','Parçada vergilerin ağır tutulmadığı belirtilir.','dikkat'),
  ('Türkmen ailelerin Balkanlara yerleştirilmesinden bilerek kaçınmıştır.','Parçada Türkmen ailelerin Balkanlara yerleştirildiği açıkça yazar.','dikkat'),
  ('Balkanlardaki halkın inanç özgürlüğünü kısıtlayarak yönetimi sağlamıştır.','Parçada inanç güvenliğinin korunduğu belirtilir; kısıtlama bilgisi yoktur.','dikkat')],'A',
 'Parçadan çıkarılabilecek politikanın belirlenmesi.','İki uygulamayı ayır: yerli halka ne yapılmış, Türkmenlere ne yapılmış?',
 [('İskân ve istimalet','İskân: Türkmen ailelerin yeni fethedilen yerlere yerleştirilmesi · İstimalet: yerli halkın gönlünü kazanma (can, mal ve inanç güvenliği, hafif vergi)')],
 'Parçada iki uygulama var: Türkmen iskânı ve yerli halka hoşgörü.','İskân + istimalet = kalıcı hâkimiyet','İki uygulamayı birlikte karşılayan yargı doğru olur.','İskân nüfusu yerleştirir, istimalet gönül kazanır; ikisi birlikte fethi kalıcı kılar.','İskân ile istimalet birbirini tamamlar: biri nüfusu yerleştirir, öteki yerli halkın desteğini kazanır.','Özgün metin; iskân/istimalet kavramı MEB')
# 0003 oncul
st=[('Yıldırım Bayezid, Ankara Savaşı’nda Timur’a yenilmiştir.',True,'Ankara Savaşı 1402’de Timur ile Yıldırım Bayezid arasında yapılmış, Bayezid yenilmiştir'),
    ('Ankara Savaşı’ndan sonra şehzadeler arasında taht mücadeleleri yaşanmıştır.',True,'bu dönem Fetret Devri adıyla anılır'),
    ('Fetret Devri, I. Murad döneminde sona ermiştir.',False,'Fetret Devri’ni Çelebi Mehmed 1413’te sona erdirmiştir; I. Murad 1389’da vefat etmiştir')]
op,dg=oncul(st,['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],'C'); assert dg=={'I','II'}
Q.Y2('0003','K-BYL-03','orta','Ankara Savaşı’nın sonuçlarını ve Fetret Devri’ni değerlendirir.',
 metin_oncul('Osmanlı tarihiyle ilgili şu bilgiler verilmiştir:',st,'Bu bilgilerden hangileri doğrudur?'),op,'C',
 'Doğru öncüllerin belirlenmesi.','Her öncülün tarihini ve olayın sahibini ayrı ayrı kontrol et.',
 [('Fetret Devri','Ankara Savaşı’ndan (1402) sonra Bayezid’in oğulları arasında taht mücadeleleri yaşandı; Çelebi Mehmed 1413’te birliği yeniden sağladı.')],
 'Her öncülü Osmanlı tarihinin bilinen olaylarıyla karşılaştır.','Ankara 1402 · Fetret 1402–1413 · Çelebi Mehmed 1413','Doğru olanlar I ve II’dir.','Fetret Devri’ni bitiren padişah Çelebi I. Mehmed’dir.','Bir olayın başlangıcı ve sonu için iki ayrı tarihi birlikte öğren.','Ankara–Fetret bağlantısı')
# 0004 kronoloji
ev={'I':('Niğbolu Savaşı',1396),'II':('Ankara Savaşı',1402),'III':('II. Kosova Savaşı',1448),'IV':('Varna Savaşı',1444)}
op,dg=kron(ev,[['II','I','IV','III'],['I','II','III','IV'],['I','IV','II','III'],['I','II','IV','III'],['IV','I','II','III']]); assert dg=='I – II – IV – III'
Q.Y2('0004','K-BYL-04','orta','Osmanlı Devleti’nin önemli savaşlarını kronolojik sıraya koyar.',
 'Aşağıda Osmanlı Devleti’nin yaptığı bazı savaşlar verilmiştir.\nI. Niğbolu Savaşı\nII. Ankara Savaşı\nIII. II. Kosova Savaşı\nIV. Varna Savaşı\nBu savaşlar eskiden yeniye doğru sıralandığında aşağıdakilerden hangisi elde edilir?',op,'D',
 'Savaşların eskiden yeniye doğru sıralanması.','Yıldırım Bayezid dönemi savaşlarını II. Murad dönemi savaşlarından önce düşün.',
 [('Savaşların tarihleri','Niğbolu 1396 (Yıldırım Bayezid) · Ankara 1402 (Timur) · Varna 1444 (II. Murad) · II. Kosova 1448 (II. Murad)')],
 'Dört savaşın tarihini hatırla ve sırala.','1396 < 1402 < 1444 < 1448','Sıralama I – II – IV – III olur.','Aynı padişah dönemindeki savaşların sırasını (Varna, sonra II. Kosova) ayrıca ezberle.','Önce padişahı, sonra yılı bağla: Bayezid 1396–1402, Murad 1444–1448.','Dört savaşın sıralaması',kalip='yeni nesil')
Q.bitir()
