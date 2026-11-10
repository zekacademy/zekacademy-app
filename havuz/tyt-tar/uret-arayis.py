import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_b import *
Q=KonuT('arayis','Osmanlı Devletinde Arayış Yılları','tar|Osmanlı Devletinde Arayış Yılları',4)
Q.zd={'kolay': 2, 'orta': 2}
Q.kart('K-ARY-01','Karlofça Antlaşması','1699’da Macaristan ve Transilvanya Avusturya’ya, Mora ve Dalmaçya Venedik’e, Podolya Lehistan’a bırakılmıştır.','Toprak bırakılan devletleri karıştırmak.','kolay','yeni nesil',2,'ary-karlofca','Karlofça Antlaşması')
Q.kart('K-ARY-02','Celali isyanları','Vergi yükü ve işsiz silahlı grupların artmasıyla Anadolu’da isyanlar çıkmış; köylü göç etmiş, üretim ve vergi geliri azalmıştır.','Sonuçları ters (artış) sanmak.','orta','yeni nesil',3,'ary-celali','Celali isyanları ve sonuçları')
Q.kart('K-ARY-03','Köprülüler dönemi','Köprülü Mehmed Paşa 1656’da sadrazam olmuş; Fazıl Ahmed Paşa döneminde Uyvar (1663) alınmış, Girit (1669) fethedilmiştir.','Olayları yanlış sadrazam ya da seferle eşlemek.','orta','öncüllü',3,'ary-koprululer','Köprülüler dönemi gelişmeleri')
Q.kart('K-ARY-04','Yönetimi düzeltme girişimleri','II. Osman yeniçeri ocağını yenilemek isteyip 1622’de öldürülmüş; IV. Murad sert önlemlerle otoriteyi kurmuş, 1638’de Bağdat’ı almıştır.','Girişimlerin hepsini başarılı sanmak.','kolay','yeni nesil',4,'ary-islahat','XVII. yüzyıl ıslahat girişimleri')
# 0001 D
Q.Y('0001','K-ARY-01','kolay','Karlofça Antlaşması’nın sonuçlarını belirler.',
 'Osmanlı Devleti, 1699’da imzalanan antlaşmayla Macaristan ve Transilvanya’yı Avusturya’ya, Mora ve Dalmaçya’yı Venedik’e, Podolya’yı Lehistan’a bırakmıştır.\nBu parçaya göre bu antlaşma ile ilgili aşağıdakilerden hangisi söylenebilir?',
 'Birden fazla devlete toprak bırakılmıştır.',
 [('Osmanlı Devleti bu antlaşmayla toprak kazanmıştır.','Parçada Osmanlı’nın toprak bıraktığı yazar; kazanç söz konusu değildir.','dikkat'),
  ('Mora ve Dalmaçya Avusturya’ya bırakılmıştır.','Parçada Mora ve Dalmaçya’nın Venedik’e bırakıldığı belirtilir.','dikkat'),
  ('Podolya, Venedik ve Avusturya’ya verilmiştir.','Parçada Podolya’nın Lehistan’a bırakıldığı yazar.','dikkat'),
  ('Antlaşma yalnızca Avusturya ile yapılmıştır.','Parçada Venedik ve Lehistan’a da toprak bırakıldığı belirtilir.','dikkat')],'D',
 'Parçadan çıkarılabilecek yargının belirlenmesi.','Hangi bölgenin hangi devlete bırakıldığına tek tek bak.',
 [('Karlofça Antlaşması (1699)','Osmanlı Devleti Macaristan ve Transilvanya’yı Avusturya’ya, Mora ve Dalmaçya’yı Venedik’e, Podolya’yı Lehistan’a bıraktı.')],
 'Parçada bırakılan bölgeler ve devletler eşleştirilmiş.','Avusturya · Venedik · Lehistan','Osmanlı, birden fazla devlete toprak bırakmıştır.','Karlofça, Osmanlı’nın büyük toprak kaybına uğradığı antlaşmadır.','Bölge–devlet eşleşmelerini parçadan oku, ezberine güvenme.','Özgün metin; MEB Karlofça')
# 0002 B
Q.Y('0002','K-ARY-02','orta','Celali isyanlarının toplumsal ve ekonomik sonuçlarını yorumlar.',
 'XVI. yüzyılın sonlarından itibaren Anadolu’da vergilerin artması ve silahlı işsiz grupların çoğalması üzerine isyanlar çıkmıştır. Çiftçiler topraklarını bırakarak şehirlere göç etmiş, tarım üretimi gerilemiş ve devletin vergi gelirleri azalmıştır.\nBu parçaya göre bu isyanlarla ilgili aşağıdakilerden hangisine ulaşılabilir?',
 'Kırsaldaki üretim düşüşü devlet gelirlerini azaltmıştır.',
 [('Çiftçilerin köylerine dönmesiyle tarım üretimi artmıştır.','Parçada çiftçilerin köylerini bırakıp şehirlere göç ettiği ve üretimin gerilediği yazar.','dikkat'),
  ('İsyanlar, vergilerin azaltılması nedeniyle çıkmıştır.','Parçada isyanın nedeni olarak vergilerin artması gösterilir.','dikkat'),
  ('Devletin vergi gelirleri bu dönemde yükselmiştir.','Parçada vergi gelirlerinin azaldığı belirtilir.','dikkat'),
  ('Şehirlerden köylere doğru bir göç yaşanmıştır.','Parçada göçün köylerden şehirlere doğru olduğu yazar.','dikkat')],'B',
 'Parçadan çıkarılabilecek sonucun belirlenmesi.','Üretimin ve gelirin artıp artmadığına, göçün yönüne dikkat et.',
 [('Celali isyanları','XVI. yüzyıl sonunda Anadolu’da çıkan isyanlardır · Köylü şehirlere göç etti, tarım üretimi ve devlet geliri azaldı.')],
 'Parçada nedenler (vergi artışı) ve sonuçlar (göç, üretim ve gelirde azalma) verilmiş.','Vergi ↑ → isyan → göç → üretim ↓ → gelir ↓','Üretim düşüşünün devlet gelirini azalttığı yargısı parçayla uyuşur.','Nedeni ve sonucu ayır: vergi artışı neden, üretim ve gelir düşüşü sonuçtur.','Neden–sonuç sorularında yönü (artış/azalış) şıkla karşılaştır.','Özgün metin; MEB Celali')
# 0003 oncul
st=[('Köprülü Mehmed Paşa, 1656’da sadrazamlığa getirilmiştir.',True,'Köprülü Mehmed Paşa 1656’da sadrazam olmuştur'),
    ('Girit’in fethi, Fazıl Ahmed Paşa döneminde tamamlanmıştır.',True,'Girit 1669’da Fazıl Ahmed Paşa döneminde alınmıştır'),
    ('II. Viyana Kuşatması, Fazıl Ahmed Paşa komutasında yapılmıştır.',False,'1683’teki kuşatmayı Merzifonlu Kara Mustafa Paşa yönetmiştir; Fazıl Ahmed Paşa 1676’da ölmüştür'),
    ('Uyvar Kalesi, Fazıl Ahmed Paşa döneminde Osmanlı topraklarına katılmıştır.',True,'Uyvar 1663’te alınmıştır')]
op,dg=oncul(st,['Yalnız I','I ve II','I ve III','II ve III','I, II ve IV'],'E'); assert dg=={'I','II','IV'}
Q.Y2('0003','K-ARY-03','orta','Köprülüler dönemindeki gelişmeleri doğru kişi ve olayla eşler.',
 metin_oncul('Köprülüler dönemiyle ilgili şu bilgiler verilmiştir:',st,'Bu bilgilerden hangileri doğrudur?'),op,'E',
 'Doğru öncüllerin belirlenmesi.','II. Viyana Kuşatması’nın hangi sadrazam zamanında yapıldığını hatırla.',
 [('Köprülüler dönemi','Köprülü Mehmed Paşa 1656’da sadrazam oldu · Fazıl Ahmed Paşa döneminde Uyvar (1663) ve Girit (1669) alındı · II. Viyana Kuşatması (1683) Merzifonlu Kara Mustafa Paşa komutasındadır.')],
 'Her öncülü olayın tarihi ve yöneticisiyle karşılaştır.','Köprülü 1656 · Uyvar 1663 · Girit 1669 · Viyana 1683 (Kara Mustafa)','I, II ve IV doğrudur; III yanlıştır.','Olayı tarih ve komutanla birlikte öğren: Viyana 1683 = Kara Mustafa Paşa.','Öncüllerde yanlış kişi eşleşmesi olabilir; olay–kişi çiftini tek tek sına.','Dört öncülden biri yanlış')
# 0004 A (ulaşılamaz)
Q.Y('0004','K-ARY-04','kolay','XVII. yüzyıldaki ıslahat girişimlerini sonuçlarıyla birlikte değerlendirir.',
 'XVII. yüzyılda yönetimdeki bozulmaları gidermek isteyen padişahlar çeşitli önlemler almıştır. Genç Osman, yeniçeri ocağını yenilemek için Anadolu’da yeni bir ordu kurmayı planlamış; ancak 1622’de yeniçerilerin isyanı sonucunda tahttan indirilip öldürülmüştür. IV. Murad ise otoriteyi sert önlemlerle yeniden kurmaya çalışmış ve 1638’de Bağdat’ı Safevilerden geri almıştır.\nBu parçadaki bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 'Genç Osman’ın yeniçeri ocağını yenileme girişimi amacına ulaşmıştır.',
 [('Yeniçeriler, bir padişahın tahttan indirilmesinde etkili olmuştur.','Parçada Genç Osman’ın yeniçeri isyanıyla tahttan indirildiği belirtildiği için bu yargıya ulaşılabilir.','dikkat'),
  ('IV. Murad döneminde Bağdat yeniden Osmanlı denetimine girmiştir.','Parçada Bağdat’ın 1638’de geri alındığı yazar; yargıya ulaşılabilir.','dikkat'),
  ('Genç Osman’ın ordu yenileme planı yeniçerilerin tepkisine yol açmıştır.','Parçada plan sonrası yeniçeri isyanı yazar; yargıya ulaşılabilir.','dikkat'),
  ('XVII. yüzyılda padişahlar yönetimdeki bozulmaları gidermeyi amaçlamıştır.','Parçanın ilk cümlesi bunu söyler; yargıya ulaşılabilir.','dikkat')],'A',
 'Parçadan çıkarılamayan yargının belirlenmesi.','Kök “ulaşılamaz” diyor: parçada doğrulanamayan ya da parçayla çelişen yargıyı ara.',
 [('XVII. yüzyıl ıslahatları','II. Osman (Genç Osman) yeniçeri ocağını yenilemek istedi, 1622’de öldürüldü · IV. Murad sert önlemlerle otoriteyi sağladı, 1638’de Bağdat’ı geri aldı.')],
 'Kökte “ulaşılamaz” var; dört şık parçada doğrulanır, biri doğrulanmaz.','Genç Osman’ın girişimi başarısız olduğu için amacına ulaştığı yargısına ulaşılamaz.','Genç Osman: girişim başarısız · IV. Murad: Bağdat 1638','Olumsuz köklerde dört şıkkı parçada işaretle, işaretsiz kalanı seç.','Olumsuz köklerde her şıkkı parçadaki cümleyle eşleştir; eşleşmeyen şık cevaptır.','Özgün metin; MEB XVII. yüzyıl')
Q.bitir()
