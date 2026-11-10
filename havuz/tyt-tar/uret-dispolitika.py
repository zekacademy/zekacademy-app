"""TYT Tarih · Atatürk Dönemi Türk Dış Politikası: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_tar_c import *
KY='ÖSYM 2018–2026 TYT Tarih (Atatürk dönemi dış politika) · MEB T.C. İnkılap Tarihi ve Atatürkçülük'
KARTLAR={
 'K-DPL-01':dict(alt='Montrö Boğazlar Sözleşmesi',fikir='Boğazlar üzerinde Türk egemenliğini getiren sözleşmeyi öteki antlaşma ve paktlardan ayırmak.',tuzak='Balkan Antantı ve Sadabat Paktı’nı Boğazlarla ilişkilendirmek.',zorluk='kolay',kalip='düz',adim=2,tipId='tar-dpl-montro',kaynak=KY),
 'K-DPL-02':dict(alt='Musul sorunu',fikir='Metinden Musul sorununun nasıl çözüldüğünü doğru okumak.',tuzak='Musul’un Türkiye’ye bağlandığını sanmak.',zorluk='kolay',kalip='düz',adim=3,tipId='tar-dpl-musul',kaynak=KY),
 'K-DPL-03':dict(alt='Bölgesel paktlar',fikir='Atatürk döneminde imzalanan paktları sonraki dönem paktlarından ayırmak.',tuzak='NATO ve Bağdat Paktı’nı Atatürk dönemine yerleştirmek.',zorluk='orta',kalip='öncüllü',adim=3,tipId='tar-dpl-pakt',kaynak=KY),
 'K-DPL-04':dict(alt='Hatay sorunu',fikir='Metinde olmayan, hatta yanlış bir yargıyı bulmak.',tuzak='Hatay’ın savaşla alındığını sanmak.',zorluk='kolay',kalip='düz',adim=4,tipId='tar-dpl-hatay',kaynak=KY),
}
TIPLER={'tar-dpl-montro':'Montrö Boğazlar Sözleşmesi','tar-dpl-musul':'Musul sorunu metin yorumu','tar-dpl-pakt':'Atatürk dönemi paktları','tar-dpl-hatay':'Hatay sorunu metin yorumu'}
Q=Konu('dispolitika','Atatürk Dönemi Türk Dış Politikası',KARTLAR,TIPLER)
Q.zd={'kolay': 3, 'orta': 1}

Q.S('0001','K-DPL-01','kolay','Boğazlar üzerinde Türk egemenliğini sağlayan sözleşmeyi bilir.',2,'düz',
 'Boğazlar Komisyonu’nu kaldıran ve Türkiye’ye Boğazlar’ı silahlandırma hakkı tanıyan düzenleme aşağıdakilerden hangisidir?',
 'Montrö Sözleşmesi (1936)',
 [('Balkan Antantı (1934)','Balkan Antantı 1934’te Balkan devletleriyle yapılan bir güvenlik paktıdır; Boğazları düzenlemez.','bilgi'),
  ('Ankara Antlaşması (1926)','1926 tarihli Ankara Antlaşması Musul sorununu çözmüştür; Boğazlarla ilgili değildir.','bilgi'),
  ('Sadabat Paktı (1937)','Sadabat Paktı 1937’de Türkiye, İran, Irak ve Afganistan arasında yapılmıştır; Boğazları düzenlemez.','bilgi'),
  ('Mudanya Mütarekesi (1922)','Mudanya Mütarekesi 1922’de Büyük Taarruz’un ardından imzalanan ateşkestir.','bilgi')],
 'B','Boğazlar rejimini Türkiye lehine değiştiren düzenleme.','Boğazlar ve silahlandırma sözcükleri Lozan’dan sonraki bir sözleşmeyi gösterir.',
 [B('Montrö Boğazlar Sözleşmesi','20 Temmuz 1936 · Boğazlar Komisyonu kaldırıldı · Türkiye Boğazlar’ı silahlandırabilir')],
 [A('Anahtar bilgiyi bul','Soruda Boğazlar Komisyonu ve silahlandırma hakkı geçiyor.','anahtar: Boğazlar + silahlandırma'),
  A('Şıkları konularına göre ele','Balkan Antantı ve Sadabat Paktı güvenlik paktıdır. Ankara Antlaşması (1926) Musul’u, Mudanya Mütarekesi savaşın sonunu ilgilendirir.','A, D: pakt · C: Musul · E: ateşkes'),
  A('Doğru şıkkı seç','Boğazlar rejimini Montrö Sözleşmesi düzenlemiştir.','B: doğru')],
 'Boğazlar sorusunda Lozan ve Montrö’yü karıştırma: silahlandırma hakkı Montrö’dedir.')

Q.S('0002','K-DPL-02','kolay','Musul sorununun çözümünü metinden yorumlar.',3,'düz',
 'Lozan Konferansı’nda Musul sorunu çözülememiştir. Türkiye ile İngiltere anlaşamayınca sorun Milletler Cemiyeti’ne götürülmüştür. 1926’da Türkiye, İngiltere ve Irak arasında imzalanan antlaşmayla Musul Irak’a bırakılmış, Türkiye’ye 25 yıl boyunca bölge petrol gelirinden pay verilmiştir.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılabilir?',
 'Musul sorunu Lozan’da kesin olarak çözülememiştir.',
 [('Musul, antlaşmayla Türkiye’ye bağlanmıştır.','Metne göre Musul Irak’a bırakılmıştır; yargı sonucu tersine çeviriyor.','bilgi'),
  ('Petrol gelirinden pay Türkiye’ye süresiz verilmiştir.','Metinde payın 25 yıl boyunca verildiği yazıyor; süresiz değildir.','dikkat'),
  ('Antlaşma Türkiye ile Fransa arasında yapılmıştır.','Metne göre antlaşma Türkiye, İngiltere ve Irak arasındadır; Fransa geçmiyor.','dikkat'),
  ('Sorun, Milletler Cemiyeti’ne götürülmeden çözülmüştür.','Metinde sorunun önce Milletler Cemiyeti’ne götürüldüğü yazıyor; yargı bununla çelişir.','dikkat')],
 'C','Metinden çıkan yargı.','Lozan’dan 1926’ya kadar olan süreci sırala.',
 [B('Musul sorunu','Lozan’da çözülemedi · Milletler Cemiyeti’ne götürüldü · 1926 Ankara Antlaşması ile Musul Irak’a bırakıldı · Türkiye 25 yıl petrol gelirinden pay aldı')],
 [A('Süreci sırala','Önce Lozan’da çözülememiş, sonra Milletler Cemiyeti’ne gidilmiş, 1926’da antlaşma yapılmıştır.','Lozan → Milletler Cemiyeti → 1926'),
  A('Şıkları sına','Türkiye’ye bağlanma, süresiz pay, Fransa ve Milletler Cemiyeti’ne gidilmeden çözüm metinle uyuşmaz.','A, B, D, E: elenir'),
  A('Doğru şıkkı seç','Sorunun Lozan’da çözülememesi metinde açıkça yazar.','C: doğru')],
 'Antlaşma sorularında tarafları, süreyi ve sonucu ayrı ayrı kontrol et.')

Q.oncul('0003','K-DPL-03','orta','Atatürk döneminde imzalanan paktları ayırt eder.',3,'',
 [('Sadabat Paktı',True,'1937’de Atatürk döneminde imzalanmıştır'),('Kuzey Atlantik Antlaşması’na (NATO) katılma',False,'Türkiye 1952’de NATO’ya katılmıştır; Atatürk’ten sonradır'),('Balkan Antantı',True,'1934’te Atatürk döneminde imzalanmıştır'),('Bağdat Paktı',False,'1955’te imzalanmıştır; Atatürk’ten sonradır')],
 'Yukarıdakilerden hangileri Atatürk döneminde (1938’e kadar) Türkiye’nin taraf olduğu paktlardandır?',
 ['Yalnız IV','II ve IV','Yalnız III','I, II ve III','I ve III'],'E',True,'Atatürk dönemi paktları.','Atatürk’ün vefatı 1938’dir; NATO ve Bağdat Paktı hangi on yıllardadır?',
 [B('Atatürk dönemi paktları','Balkan Antantı (1934: Türkiye, Yunanistan, Romanya, Yugoslavya) · Sadabat Paktı (1937: Türkiye, İran, Irak, Afganistan)'),B('Sonraki paktlar','NATO’ya katılma 1952 · Bağdat Paktı 1955')],
 [A('Sınırı koy','Atatürk 10 Kasım 1938’de vefat etmiştir. Pakt bu tarihten önce imzalanmış olmalıdır.','sınır: 1938'),
  A('Paktları tarihlendir','Sadabat Paktı 1937’de, Balkan Antantı 1934’te imzalanmıştır. NATO 1952’de, Bağdat Paktı 1955’tedir.','I: 1937 · II: 1952 · III: 1934 · IV: 1955'),
  A('Sonucu bul','Atatürk dönemindeki paktlar I ve III’tür.','I ve III')],
 'Pakt sorularında paktın yılını Atatürk’ün vefat yılıyla (1938) karşılaştır.')

Q.S('0004','K-DPL-04','kolay','Hatay sorunu bilgisinden ulaşılamayan yargıyı bulur.',4,'düz',
 'Hatay’ın statüsü 1921 tarihli Ankara Antlaşması’yla Suriye içinde özel bir idare olarak belirlenmişti. Fransa’nın Suriye’ye bağımsızlık vermeyi kabul etmesi üzerine Türkiye, Hatay’ın durumunu uluslararası alana taşımıştır. Milletler Cemiyeti kararıyla Hatay’a özerklik tanınmış, 1938’de kurulan Hatay Devleti 1939’da Türkiye’ye katılma kararı almıştır.\nBu bilgilere göre aşağıdakilerden hangisine ulaşılamaz?',
 'Hatay’ın Fransa’yla yapılan savaşla Türkiye’ye katıldığına',
 [('Hatay’ın katılmadan önce bir özerklik dönemi yaşadığına','Metne göre Milletler Cemiyeti kararıyla Hatay’a özerklik tanınmıştır; yargı metinden çıkar.','dikkat'),
  ('Sorunun uluslararası bir kuruluşun devreye girmesiyle ilerlediğine','Metinde Milletler Cemiyeti kararından söz ediliyor; yargı metinden çıkar.','dikkat'),
  ('Hatay’ın durumunun Fransa’nın Suriye politikasındaki değişiklikle gündeme geldiğine','Metne göre Fransa’nın Suriye’ye bağımsızlık vermeyi kabul etmesi üzerine Türkiye konuyu taşımıştır; yargı metinden çıkar.','dikkat'),
  ('Hatay’ın 1921’de Suriye içinde özel idareye sahip olduğuna','Metnin ilk cümlesi 1921 Ankara Antlaşması’yla özel idareyi belirtir; yargı metinden çıkar.','dikkat')],
 'D','Metinden ulaşılamayan yargı.','Kök “ulaşılamaz” diyor; metinde savaştan söz edilip edilmediğine bak.',
 [B('Hatay sorunu','1921 Ankara Antlaşması: Hatay’a özel idare · 1937 Milletler Cemiyeti kararıyla özerklik · 1938 Hatay Devleti · 23 Temmuz 1939’da Türkiye’ye katılma')],
 [A('Metindeki bilgileri yaz','1921’de özel idare, Fransa’nın Suriye kararı, Milletler Cemiyeti kararı, özerklik, 1938 Hatay Devleti, 1939 katılma.','özel idare → özerklik → Hatay Devleti → katılma'),
  A('Şıkları metinle sına','Özerklik, uluslararası kuruluşun rolü, Fransa’nın Suriye kararı ve 1921 özel idaresi metinde var.','A, B, C, E: metinde var'),
  A('Metinde olmayanı bul','Metinde Fransa ile bir savaştan söz edilmiyor; Hatay’ın katılması karar yoluyla anlatılıyor.','D: metinden çıkmaz'),
  A('Doğru şıkkı seç','Ulaşılamayan yargı D’dir.','D')],
 'Hatay’ın katılmasını savaşla değil, hukuki süreç ve karar zinciriyle hatırla.')
Q.bitir()
