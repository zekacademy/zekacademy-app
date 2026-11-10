"""TYT Tarih · II. TBMM Dönemi ve Çok Partili Hayata Geçiş: 4 ana soru (hafif mod). Önek rakam içeremediği için 'tbmmiki' (tbmm2)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (çok partili hayata geçiş denemeleri) · MEB T.C. İnkılap Tarihi ve Atatürkçülük'
KARTLAR={
 'K-TBB-01':dict(alt='Terakkiperver Cumhuriyet Fırkası',fikir='Cumhuriyet döneminin ilk muhalefet partisini bilmek.',tuzak='Serbest Cumhuriyet Fırkası’nı ya da sonraki muhalefet partilerini ilk muhalefet partisi sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-tbb-ilkparti',kaynak=KY),
 'K-TBB-02':dict(alt='Serbest Cumhuriyet Fırkası',fikir='Partinin kuruluşu ve kapanışına ilişkin metinden doğru yargıyı seçmek.',tuzak='Partinin kapanışını hükûmete bağlamak.',zorluk='orta',kalip='düz',adim=3,tipId='tar-tbb-scf',kaynak=KY),
 'K-TBB-03':dict(alt='II. TBMM Dönemi gelişmeleri',fikir='Gelişmeleri II. TBMM dönemine (1923–1927) ayırmak.',tuzak='Saltanatın kaldırılması ve Teşkilât-ı Esasiye’yi II. TBMM işi sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='tar-tbb-donem',kaynak=KY),
 'K-TBB-04':dict(alt='Çok partili hayata geçiş',fikir='1946 ve 1950 seçimlerine ilişkin bilgileri metinden okuyup metinde olmayanı ayırmak.',tuzak='Demokrat Parti’nin 1946’da iktidara geldiğini sanmak.',zorluk='orta',kalip='düz',adim=4,tipId='tar-tbb-secim',kaynak=KY),
}
TIPLER={'tar-tbb-ilkparti':'İlk muhalefet partisi','tar-tbb-scf':'Serbest Cumhuriyet Fırkası metin yorumu','tar-tbb-donem':'II. TBMM Dönemi gelişmeleri','tar-tbb-secim':'1946 ve 1950 seçimleri metin yorumu'}
Q=Konu('tbmmiki','II. TBMM Dönemi ve Çok Partili Hayata Geçiş',KARTLAR,TIPLER)
Q.zd={'kolay': 1, 'orta': 3}

Q.S('0001','K-TBB-01','kolay','Cumhuriyet döneminin ilk muhalefet partisini bilir.',2,'düz',
 'Kâzım Karabekir, Ali Fuat Cebesoy ve Rauf Orbay gibi isimlerce 1924’te kurulan, Cumhuriyet döneminin ilk muhalefet partisi aşağıdakilerden hangisidir?',
 'Terakkiperver Cumhuriyet Fırkası',
 [('Serbest Cumhuriyet Fırkası','Serbest Cumhuriyet Fırkası 1930’da kurulmuştur; 1924’te değil.','bilgi'),
  ('Cumhuriyet Halk Fırkası','Cumhuriyet Halk Fırkası, Mustafa Kemal’in kurduğu iktidar partisidir; muhalefet partisi değildir.','bilgi'),
  ('Cumhuriyetçi Köylü Millet Partisi','Cumhuriyetçi Köylü Millet Partisi 1950’lerin sonunda bu adı almıştır; 1924’te kurulmamıştır.','bilgi'),
  ('Millî Kalkınma Partisi','Millî Kalkınma Partisi 1945’te kurulmuştur; 1924’ten sonradır.','bilgi')],
 'C','1924’te kurulan ilk muhalefet partisi.','Kuruluş yılı 1924; iktidar partisini ve sonraki muhalefet partilerini ele.',
 [B('Terakkiperver Cumhuriyet Fırkası','17 Kasım 1924 · kurucuları Kâzım Karabekir, Rauf Orbay, Ali Fuat Cebesoy, Refet Bele, Adnan Adıvar · 1925’te kapatıldı')],
 [A('Tarihi belirle','Parti 1924’te kurulmuştur.','kuruluş: 1924'),
  A('Şıkları kuruluş yıllarına göre ele','Serbest Cumhuriyet Fırkası 1930, Millî Kalkınma Partisi 1945, Cumhuriyetçi Köylü Millet Partisi 1950’lerin sonunda bu adı aldı. Cumhuriyet Halk Fırkası iktidar partisidir.','A: 1930 · D: 1950’ler · E: 1945 · B: iktidar'),
  A('Doğru şıkkı seç','1924’te kurulan muhalefet partisi Terakkiperver Cumhuriyet Fırkası’dır.','C: doğru')],
 'Parti sorularında kuruluş yılı ve iktidar/muhalefet ayrımı belirleyicidir.')

Q.S('0002','K-TBB-02','orta','Serbest Cumhuriyet Fırkası’nın kapanışına ilişkin metinden çıkarım yapar.',3,'düz',
 '12 Ağustos 1930’da Ali Fethi Okyar önderliğinde kurulan parti, Atatürk’ün desteğiyle ortaya çıkmıştır. Kısa sürede hızlı bir örgütlenme gösteren parti, Cumhuriyet rejimine karşı bazı kesimlerin kendisine yönelmesi üzerine kurucusu tarafından 17 Kasım 1930’da kapatılmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Parti, kurucusunun kararıyla kapatılmıştır.',
 [('Parti, Atatürk’ün isteği dışında kurulmuştur.','Metne göre parti Atatürk’ün desteğiyle ortaya çıkmıştır; yargı metne ters.','bilgi'),
  ('Parti iki yıldan uzun süre faaliyet göstermiştir.','Metne göre parti Ağustos 1930’da kurulup Kasım 1930’da kapanmıştır; üç ay kadar sürmüştür.','islem'),
  ('Partinin kapanışı Menemen Olayı’nın sonucudur.','Metinde Menemen Olayı’ndan söz edilmiyor; yargı metinden çıkarılamaz.','dikkat'),
  ('Parti, Cumhuriyet’in ilk muhalefet partisidir.','Metinde böyle bir bilgi yok; ayrıca ilk muhalefet partisi Terakkiperver Cumhuriyet Fırkası’dır.','bilgi')],
 'D','Metinden çıkan yargı.','Kapanışı kimin yaptığını metinde bul.',
 [B('Serbest Cumhuriyet Fırkası','12 Ağustos 1930 · başkanı Ali Fethi Okyar · 17 Kasım 1930’da Fethi Okyar tarafından kapatıldı')],
 [A('Tarih ve kurucuyu yaz','Parti 12 Ağustos 1930’da kurulmuş, 17 Kasım 1930’da kapatılmıştır. Kapatan kurucusudur.','Ağustos 1930 → Kasım 1930 · kapatan: kurucu'),
  A('Şıkları metinle sına','Atatürk’ün isteği dışında kuruluş, iki yıldan uzun faaliyet, Menemen bağlantısı ve ilk muhalefet partisi olma yargıları metinle uyuşmaz.','A, B, C, E: elenir'),
  A('Doğru şıkkı seç','Kapanışın parti yönetimince yapıldığı yargısı metinden çıkar.','D: doğru')],
 'Metin sorusunda kapanışı kimin yaptığı gibi ayrıntıyı metinden bul.')

Q.oncul('0003','K-TBB-03','orta','Gelişmeleri II. TBMM Dönemi’ne ayırır.',3,'',
 [('Cumhuriyet’in ilan edilmesi',True,'29 Ekim 1923’te II. TBMM döneminde ilan edilmiştir'),('Saltanatın kaldırılması',False,'1 Kasım 1922’de I. TBMM döneminde kaldırılmıştır'),('Takrir-i Sükûn Kanunu’nun kabul edilmesi',True,'1925’te II. TBMM döneminde kabul edilmiştir'),('Teşkilât-ı Esasiye Kanunu’nun kabul edilmesi',False,'20 Ocak 1921’de I. TBMM döneminde kabul edilmiştir')],
 'Yukarıdakilerden hangileri II. TBMM Dönemi’nde (1923–1927) gerçekleşmiştir?',
 ['I ve III','II ve IV','Yalnız III','III ve IV','I, II ve III'],'A',True,'II. TBMM dönemi gelişmeleri.','II. TBMM’nin 1923 Ağustos’unda başladığını düşün.',
 [B('II. TBMM Dönemi','Ağustos 1923’te başlar · Cumhuriyet’in ilanı (1923) · Takrir-i Sükûn (1925)'),B('I. TBMM işleri','Teşkilât-ı Esasiye (1921) · saltanatın kaldırılması (1922)')],
 [A('Dönem başlangıcını koy','II. TBMM Ağustos 1923’te çalışmaya başlamıştır.','sınır: Ağustos 1923'),
  A('Olayları tarihlendir','Cumhuriyet Ekim 1923’te, Takrir-i Sükûn Kanunu 1925’te kabul edildi. Saltanat 1922’de kaldırıldı, Teşkilât-ı Esasiye 1921’de kabul edildi.','I: 1923 · II: 1922 · III: 1925 · IV: 1921'),
  A('Sonucu bul','Ağustos 1923’ten sonraki olaylar I ve III’tür.','I ve III')],
 'Bir olayın hangi meclise ait olduğunu Ağustos 1923 sınırıyla belirle.')

Q.S('0004','K-TBB-04','orta','Çok partili hayata geçişe ilişkin metinde olmayan yargıyı bulur.',4,'düz',
 '1946 yılında Türkiye’de ilk kez birden fazla partinin katıldığı bir genel seçim yapılmıştır. Bu seçimde Cumhuriyet Halk Partisi çoğunluğu elde etmiş, Demokrat Parti ise muhalefette kalmıştır. 1950 seçimlerinde Demokrat Parti çoğunluğu kazanmıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 'Demokrat Parti’nin 1946 seçimlerini kazanarak iktidara geldiğine',
 [('Türkiye’de çok partili seçimlerin 1946’da başladığına','Metnin ilk cümlesi 1946’da birden fazla partinin katıldığı seçim yapıldığını belirtir; yargı metinden çıkar.','dikkat'),
  ('Cumhuriyet Halk Partisi’nin 1946’da çoğunluğu elde ettiğine','Metne göre 1946 seçiminde çoğunluğu Cumhuriyet Halk Partisi elde etmiştir; yargı metinden çıkar.','dikkat'),
  ('Demokrat Parti’nin 1946’da muhalefette kaldığına','Metin, Demokrat Parti’nin 1946 seçiminde muhalefette kaldığını söyler; yargı metinden çıkar.','dikkat'),
  ('Demokrat Parti’nin 1950’de çoğunluğu kazandığına','Metnin son cümlesi bunu belirtir; yargı metinden çıkar.','dikkat')],
 'B','Metinden ulaşılamayan yargı.','Kök “ulaşılamaz” diyor; metinde Demokrat Parti’nin 1946’daki durumu nasıl anlatılıyor?',
 [B('Çok partili hayata geçiş','1946: çok partili hayata geçişten sonra ilk genel seçim · Cumhuriyet Halk Partisi çoğunluğu kazandı, Demokrat Parti muhalefette kaldı · 1950: Demokrat Parti çoğunluğu kazandı ve iktidara geldi')],
 [A('Metindeki bilgileri yaz','1946: birden fazla parti, CHP çoğunluğu, DP muhalefette. 1950: DP çoğunluğu.','1946: CHP çoğunluk · 1950: DP çoğunluk'),
  A('Şıkları sına','Çok partili seçim, CHP’nin çoğunluğu, DP’nin muhalefette kalışı ve DP’nin 1950’de çoğunluğu metinde var.','A, C, D, E: metinde var'),
  A('Metinle çelişeni bul','Metne göre 1946’da çoğunluğu CHP almıştır; DP’nin 1946’da iktidara geldiği yargısı metinle çelişir.','B: metinle çelişir'),
  A('Doğru şıkkı seç','Ulaşılamayan yargı B’dir.','B')],
 'Yıl ve olay eşleşmelerini metindeki cümlelerle tek tek doğrula.')
Q.bitir()
