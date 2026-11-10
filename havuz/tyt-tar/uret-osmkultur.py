import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('osmkultur','Osmanlı Kültür ve Medeniyeti','tar|Osmanlı Kültür ve Medeniyeti',4)
Q.zd={'kolay': 1, 'orta': 3}
Q.kart('K-OKM-01','Mimar Sinan','Mimar Sinan eserlerini çıraklık (Şehzade), kalfalık (Süleymaniye) ve ustalık (Selimiye) olarak sınıflandırmıştır.','Eser–dönem eşleşmesini karıştırmak.','kolay','yeni nesil',2,'okm-sinan','Mimar Sinan ve eserleri')
Q.kart('K-OKM-02','Millet sistemi','Gayrimüslim topluluklar dinî önderleri aracılığıyla iç işlerinde (inanç, eğitim, aile hukuku) özerk olmuş, vergi ödemiştir.','Gayrimüslimleri vergiden muaf ya da hukuksuz sanmak.','orta','yeni nesil',3,'okm-millet','Millet sistemi')
Q.kart('K-OKM-03','Merkez teşkilatı','Divan-ı Hümayun devlet işlerinin görüşüldüğü kuruldur; sadrazam başkanlık eder; defterdar maliye, kaptan-ı derya donanma başındadır.','Görevleri birbirine karıştırmak.','orta','öncüllü',3,'okm-teskilat','Merkez teşkilatı görevleri')
Q.kart('K-OKM-04','Bilim ve edebiyat','Piri Reis (Kitab-ı Bahriye), Evliya Çelebi (Seyahatname), Katip Çelebi (Cihannüma), Takiyüddin (İstanbul Rasathanesi), Fuzuli (Leyla ile Mecnun).','Yazar–eser eşleştirmesini karıştırmak.','orta','yeni nesil',4,'okm-eser','Bilim insanı ve eser eşleştirmesi')
# 0001 C
Q.Y('0001','K-OKM-01','kolay','Mimar Sinan’ın eserlerini kendi sınıflamasına göre yorumlar.',
 'Mimar Sinan, Kanuni Sultan Süleyman döneminde başmimarlık yapmıştır. Kendi anlatımına göre Şehzade Camii çıraklık eseri, Süleymaniye Camii kalfalık eseri, Selimiye Camii ise ustalık eseridir.\nBu parçaya göre Mimar Sinan ile ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Selimiye Camii’ni ustalık eseri olarak görmüştür.',
 [('Süleymaniye Camii’ni ustalık eseri saymıştır.','Parçada Süleymaniye’nin kalfalık eseri olduğu belirtilir.','dikkat'),
  ('Şehzade Camii’ni ustalık eseri olarak göstermiştir.','Parçada Şehzade Camii çıraklık eseridir.','dikkat'),
  ('Selimiye Camii’ni çıraklık eseri olarak nitelendirmiştir.','Parçada Selimiye ustalık eseri olarak geçer.','dikkat'),
  ('Kanuni döneminde başmimarlık görevinde bulunmamıştır.','Parçanın ilk cümlesinde Kanuni döneminde başmimarlık yaptığı yazar.','dikkat')],'C',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Her camiyi parçada hangi dönemle (çıraklık, kalfalık, ustalık) eşleştirildiğine bak.',
 [('Mimar Sinan’ın eserleri','Çıraklık eseri: Şehzade Camii · Kalfalık eseri: Süleymaniye Camii · Ustalık eseri: Selimiye Camii (Edirne).')],
 'Parçada eser–dönem eşleşmeleri ve görev dönemi verilmiş.','Şehzade: çıraklık · Süleymaniye: kalfalık · Selimiye: ustalık','Selimiye’nin ustalık eseri olması yargısı parçayla uyuşur.','Sinan’ın üç dönem eserini sırasıyla öğren: Şehzade, Süleymaniye, Selimiye.','Eserleri “çıraklık → kalfalık → ustalık” sırasıyla ezberle.','Özgün metin; MEB Mimar Sinan')
# 0002 A
Q.Y('0002','K-OKM-02','orta','Osmanlı’daki millet sisteminin özelliklerini yorumlar.',
 'Osmanlı Devleti’nde farklı dinlere mensup topluluklar, dinî önderlerinin yönetiminde kendi inanç ve eğitim işlerini yürütmüş; evlilik ve miras gibi konularda kendi dinî kurallarına uymuştur. Bu topluluklar devlete vergi ödemiş ve devletin güvencesi altında yaşamıştır.\nBu parçaya göre millet sistemi ile ilgili aşağıdakilerden hangisi söylenebilir?',
 'Dinî toplulukların iç işlerinde ölçülü bir özerklik tanınmıştır.',
 [('Gayrimüslim topluluklar vergiden tamamen muaf tutulmuştur.','Parçada toplulukların devlete vergi ödediği belirtilir.','dikkat'),
  ('Dinî topluluklar devletin güvencesi dışında bırakılmıştır.','Parçada toplulukların devletin güvencesi altında yaşadığı yazar.','dikkat'),
  ('Toplulukların eğitim işlerini doğrudan devlet yürütmüştür.','Parçada eğitim işlerini toplulukların dinî önderlerinin yürüttüğü belirtilir.','dikkat'),
  ('Topluluklar evlilik ve miras konularında devletin hukukuna tabi olmuştur.','Parçada bu konularda toplulukların kendi dinî kurallarına uyduğu yazar.','dikkat')],'A',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Toplulukların neleri kendilerinin yürüttüğüne, devlete ne verdiklerine bak.',
 [('Millet sistemi','Osmanlı’da dinî topluluklar (millet) kendi önderleriyle inanç, eğitim ve aile hukuku işlerini yürütür · Devlete vergi öder, devlet güvencesinde yaşar.')],
 'Parçada özerk alanlar (inanç, eğitim, evlilik, miras) ve yükümlülük (vergi) verilmiş.','Özerklik: iç işler · Yükümlülük: vergi','İç işlerde özerklik, ölçülü özerklik yargısını doğrular.','Millet sistemi: topluluklara iç işlerinde özerklik, devlete vergi ve bağlılık.','Parçada “hangi işleri kim yürütüyor?” sorusunu cevapla.','Özgün metin; MEB millet sistemi')
# 0003 oncul E
st=[('Divan-ı Hümayun, devlet işlerinin görüşüldüğü merkezî kuruldur.',True,'Divan-ı Hümayun Osmanlı’nın merkezî yönetim kuruludur'),
    ('Nişancı, donanmanın komutanıdır.',False,'donanmanın komutanı Kaptan-ı Derya’dır; nişancı ferman ve beratlara padişahın tuğrasını çeken görevlidir'),
    ('Defterdar, maliye işlerinden sorumludur.',True,'defterdar devletin mali işlerini yürütür'),
    ('Sadrazam, Divan-ı Hümayun’a padişahın vekili olarak başkanlık eder.',True,'Divan toplantılarına sadrazam başkanlık eder')]
op,dg=oncul(st,['Yalnız I','I ve III','II ve IV','II, III ve IV','I, III ve IV'],'E'); assert dg=={'I','III','IV'}
Q.Y2('0003','K-OKM-03','orta','Osmanlı merkez teşkilatındaki görevleri ayırt eder.',
 metin_oncul('Osmanlı Devleti’nin merkez teşkilatıyla ilgili şu bilgiler verilmiştir:',st,'Bu bilgilerden hangileri doğrudur?'),op,'E',
 'Doğru öncüllerin belirlenmesi.','Donanmanın başında hangi görevlinin bulunduğunu ve tuğrayı kimin çektiğini hatırla.',
 [('Merkez teşkilatı','Divan-ı Hümayun: merkezî yönetim kurulu · Sadrazam: Divan’a başkanlık eder · Defterdar: maliye · Kaptan-ı Derya: donanma · Nişancı: tuğra çekmek.')],
 'Her görevi görev alanıyla eşle.','I, III, IV doğru · II yanlış','Doğru öncüller I, III ve IV’tür.','Görev–alan çiftlerini öğren: defterdar–maliye, kaptan-ı derya–donanma, nişancı–tuğra.','Öncülde bir görev varsa “ne iş yapar?” diye önce kendin hatırla, sonra karşılaştır.','Dört görev, bir yanlış')
# 0004 D (yanlış eşleştirme)
Q.Y('0004','K-OKM-04','orta','Osmanlı bilim, sanat ve edebiyat insanlarını eserleriyle eşleştirir.',
 'Aşağıdaki kişi–eser ya da kişi–alan eşleştirmelerinden hangisi yanlıştır?',
 'Piri Reis – Cihannüma',
 [('Mimar Sinan – Selimiye Camii','Bu eşleştirme doğrudur; Selimiye Mimar Sinan’ın ustalık eseridir. Soru yanlış olanı arıyor.','dikkat'),
  ('Takiyüddin – İstanbul Rasathanesi','Bu eşleştirme doğrudur; Takiyüddin İstanbul Rasathanesi’ni kurmuştur. Soru yanlış olanı arıyor.','dikkat'),
  ('Evliya Çelebi – Seyahatname','Bu eşleştirme doğrudur; Seyahatname Evliya Çelebi’nin eseridir. Soru yanlış olanı arıyor.','dikkat'),
  ('Fuzuli – Leyla ile Mecnun','Bu eşleştirme doğrudur; Leyla ile Mecnun Fuzuli’nin mesnevisidir. Soru yanlış olanı arıyor.','dikkat')],'D',
 'Yanlış eşleştirmenin belirlenmesi.','Kökte “yanlış” isteniyor: doğru eşleşmeleri ele, kalanı seç.',
 [('Kişi–eser eşleşmeleri','Piri Reis: Kitab-ı Bahriye · Katip Çelebi: Cihannüma, Keşfü’z-Zünun · Evliya Çelebi: Seyahatname · Takiyüddin: İstanbul Rasathanesi · Fuzuli: Leyla ile Mecnun.')],
 'Kökte “yanlış” isteniyor; dört eşleştirme doğru, biri yanlış.','Cihannüma → Katip Çelebi, Piri Reis → Kitab-ı Bahriye','Cihannüma Piri Reis’e değil Katip Çelebi’ye aittir; Piri Reis’in eseri Kitab-ı Bahriye’dir.','Eser adlarını kişilerle birlikte öğren; “Cihannüma” Katip Çelebi, “Kitab-ı Bahriye” Piri Reis demektir.','“Yanlış” köklerinde bildiğin eşleşmeleri ele ve kalanı işaretle.','Eşleştirme sorusu',kalip='düz')
Q.bitir()
