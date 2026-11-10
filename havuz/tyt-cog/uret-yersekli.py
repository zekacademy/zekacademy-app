import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_c import *
P=Parti('yersekli','Türkiye’nin Yer Şekilleri','cog|Türkiye’nin Yer Şekilleri',ders='TYT Coğrafya',idon='tytcog')
KY='ÖSYM 2018–2026 TYT Coğrafya (yer şekilleri, harita) · MEB 10. sınıf'
kart('K-CGYS-01','Dağların oluşumu','Türkiye’deki dağlar oluşumlarına göre kıvrım, kırık (horst) ve volkanik olarak ayrılır.','Erciyes gibi volkanik dağları kıvrım dağı sanmak.','kolay','düz',2,'cg-yersekli-dag','Dağların oluşum türü',KY)
kart('K-CGYS-02','Dağların uzanışı ve etkisi','Dağların kıyıya paralel ya da dik uzanması kıyı yapısını, ulaşımı ve iklimi etkiler.','Ege’de dağların kıyıya paralel uzandığını sanmak.','orta','öncüllü',3,'cg-yersekli-uzanis','Dağların uzanışının sonuçları',KY)
kart('K-CGYS-03','Ova ve göl oluşumu','Ovalar akarsu biriktirmesiyle, çöküntüyle ya da göl tabanından oluşur; göller de çöküntüyle oluşabilir.','Dağ oluşumunu volkanik sanmak.','orta','düz',3,'cg-yersekli-olusum','Yer şekli–oluşum eşleştirme',KY)
kart('K-CGYS-04','Kıyı özelliklerinden bölge bulma','Birden çok ipucunun birlikte sağlandığı bölge seçilir.','Yalnız bir ipucuna bakıp Akdeniz’i seçmek.','orta','yeni nesil',4,'cg-yersekli-bolge','Birden çok ipucundan kıyı bölgesi bulma',KY)
DAG=B('Dağların oluşumu','Kıvrım: Alp kıvrımlarıyla oluşan Toroslar, Kuzey Anadolu ve Doğu Anadolu dağları (Kaçkar, Aladağlar, Munzur) · Kırık (horst): Ege’deki Bozdağlar, Menteşe Dağları · Volkanik: Erciyes, Hasan, Ağrı, Süphan')
UZA=B('Dağların uzanışı','Kıyıya paralel dağlar (Karadeniz, Akdeniz): kıyı düzdür, iç kesimlerle ulaşım zordur, iklim etkisi içeri girmez. Kıyıya dik dağlar (Ege): kıyı girintili çıkıntılıdır, denizin etkisi içeri sokulur')
OVA=B('Ova ve göl oluşumu','Delta ovası: akarsuyun denize taşıdığı alüvyonlar (Bafra, Çarşamba, Çukurova) · Eski göl tabanı: Konya Ovası · Tektonik göl: çöküntü çukurunda (Eğirdir, Tuz Gölü)')
# 0001
Q(P,'0001','K-CGYS-01','kolay','Türkiye’deki dağları oluşum türlerine göre ayırır.','düz',2,
 'Aşağıdaki dağlardan hangisi volkanik faaliyetlerle oluşmuştur?',
 [('Kaçkar Dağları','kıv','Kaçkarlar Alp kıvrımlarıyla oluşan kıvrım dağıdır.','bilgi'),('Aladağlar','kıv','Aladağlar Toros kıvrım sisteminin parçasıdır.','bilgi'),('Munzur Dağları','kıv','Munzur Dağları kıvrılmayla oluşmuştur.','bilgi'),('Bozdağlar','kır','Bozdağlar Ege’de kırılmalarla yükselen bir kütle (horst) dağıdır.','bilgi'),('Erciyes Dağı','vol',None,None)],
 lambda e:e=='vol','Volkanik dağ.',
 'Önce hangi dağların kıvrılmayla, hangisinin kırılmayla oluştuğunu ele.',[DAG],
 [A('Türleri hatırla','Dağlar kıvrılma, kırılma ya da volkanizmayla oluşur.','kıvrım · kırık · volkanik'),
  A('Şıkları ayır','Kaçkar, Aladağlar ve Munzur kıvrım; Bozdağlar kırıklı dağdır.','4 şık: volkanik değil'),
  A('Sonuç','Erciyes, püskürmelerle oluşmuş sönmüş bir yanardağdır.','Erciyes: volkanik')],
 'Erciyes, Hasan, Ağrı ve Süphan Türkiye’nin başlıca volkanik dağlarıdır.','yeni dağ şıkları',harf='E')
# 0002
tr={'I':False,'II':True,'III':False}; dg={k for k,v in tr.items() if v}
Q(P,'0002','K-CGYS-02','orta','Dağların uzanışının kıyı yapısı ve ulaşım üzerindeki etkilerini yorumlar.','öncüllü',3,
 'Türkiye’de dağların uzanışı ile ilgili olarak\nI. Ege kıyılarında dağlar kıyıya paralel uzandığı için kıyı düzdür.\nII. Karadeniz kıyısında dağların kıyıya paralel uzanması, kıyıdan iç kesimlere ulaşımı zorlaştırır.\nIII. Toroslar, Akdeniz’in nemli havasının İç Anadolu’ya girmesini kolaylaştırır.\nifadelerinden hangileri doğrudur?',
 onc_opts(dg,[{'II'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}],{'I ve II':('Ege’de dağların kıyıya dik uzandığını, bu yüzden kıyının girintili çıkıntılı olduğunu unutmak.','bilgi'),'I ve III':('Ege kıyısını düz sanıp Torosların nemli havayı engellediğini atlamak.','bilgi'),'II ve III':('Torosların nemli havayı İç Anadolu’ya geçirmediğini, aksine engellediğini unutmak.','bilgi'),'I, II ve III':('Ege’deki dağların uzanışını ve Torosların engelleyici etkisini bilmemek.','bilgi')}),
 lambda e:e==frozenset(dg),'Doğru ifadeler.',
 'Her ifadede dağların kıyıya paralel mi, dik mi uzandığını ve bunun sonucunu kontrol et.',[UZA],
 [A('I. ifade','Ege’de dağlar kıyıya diktir; bu yüzden kıyı girintili çıkıntılıdır.','I yanlış'),
  A('II. ifade','Karadeniz’de dağlar kıyıya paraleldir ve kıyıyla iç kesim arasında engel oluşturur.','II doğru'),
  A('III. ifade','Toroslar kıyıya paralel yükselerek nemli havanın iç kesimlere geçmesini engeller.','III yanlış · yalnız II')],
 'Kıyıya paralel uzanan dağlar ulaşımı ve nemli hava akışını kıyıda tutar.','dağ uzanışı öncülleri',harf='A')
# 0003
Q(P,'0003','K-CGYS-03','orta','Yer şekillerinin oluşum biçimlerini eşleştirir.','düz',3,
 'Aşağıdakilerden hangisinde yer şekli ile oluşum biçimi yanlış eşleştirilmiştir?',
 [('Bafra Ovası – Kızılırmak’ın taşıdığı alüvyonların birikmesi','d','Bafra, Kızılırmak’ın alüvyonlarıyla oluşan delta ovasıdır; doğru eşleştirme.','bilgi'),
  ('Çukurova – Seyhan ve Ceyhan’ın taşıdığı alüvyonların birikmesi','d','Çukurova delta ovasıdır; doğru eşleştirme.','bilgi'),
  ('Kuzey Anadolu Dağları – Volkanik püskürmeler','x',None,None),
  ('Konya Ovası – Eski bir gölün tabanının kuruması','d','Konya Ovası eski göl tabanıdır; doğru eşleştirme.','bilgi'),
  ('Eğirdir Gölü – Tektonik çöküntü','d','Eğirdir Gölü çöküntü çukurunda oluşmuştur; doğru eşleştirme.','bilgi')],
 lambda e:e=='x','Yanlış eşleştirme.',
 'Her yer şeklinin oluşum biçimini bilinenlerle karşılaştır; kıvrım dağlarının nasıl oluştuğunu hatırla.',[OVA,DAG],
 [A('Oluşumları hatırla','Delta ovaları akarsu birikimiyle, Konya Ovası göl tabanıyla, Eğirdir çöküntüyle oluşmuştur.','delta · göl tabanı · tektonik'),
  A('Şıkları sına','A, B, D ve E bu bilgilerle uyumludur.','4 şık: doğru'),
  A('Sonuç','Kuzey Anadolu Dağları kıvrılmayla oluşmuştur; volkanik değildir.','C: yanlış')],
 'Ovalar çoğunlukla birikimle, dağlar kıvrılma, kırılma ya da volkanizmayla oluşur.','yer şekli–oluşum',harf='C')
# 0004
Q(P,'0004','K-CGYS-04','orta','Birden çok ipucundan kıyı bölgesini belirler.','yeni nesil',4,
 'Bir kıyı bölgesi için şu bilgiler verilmiştir:\nI. Dağlar kıyıya paralel uzanır ve kıyıdan iç kesimlere ulaşımı zorlaştırır.\nII. Kıyı çizgisi düzdür, girinti ve çıkıntı azdır.\nIII. Kıyıda Kızılırmak ve Yeşilırmak’ın alüvyonlarıyla oluşan delta ovaları bulunur.\nBu bilgilerin tümü aşağıdaki bölgelerden hangisi için doğrudur?',
 [('Akdeniz Bölgesi','a','Toroslar kıyıya paraleldir ancak delta ovaları Seyhan ve Ceyhan’ındır; Kızılırmak ve Yeşilırmak Karadeniz’e dökülür.','bilgi'),
  ('Doğu Anadolu Bölgesi','a','Bölgenin denize kıyısı yoktur; kıyı özellikleri verilemez.','dikkat'),
  ('Ege Bölgesi','a','Ege’de dağlar kıyıya diktir; kıyı girintili çıkıntılıdır.','bilgi'),
  ('Karadeniz Bölgesi','k',None,None),
  ('Marmara Bölgesi','a','Kızılırmak ve Yeşilırmak Marmara’ya dökülmez; kıyı da düz değildir.','bilgi')],
 lambda e:e=='k','Bilgilerin tümünün doğru olduğu bölge.',
 'Kızılırmak ve Yeşilırmak hangi denize dökülüyor? Sonra diğer iki ipucunu bu bölgede sına.',[UZA,OVA],
 [A('Delta ipucu','Kızılırmak ve Yeşilırmak Karadeniz’e dökülür; delta ovaları (Bafra, Çarşamba) oradadır.','III: Karadeniz'),
  A('Diğer ipuçları','Karadeniz’de dağlar kıyıya paraleldir, kıyı düzdür ve ulaşım zordur.','I ve II: Karadeniz'),
  A('Şıkları ele','Ege’de dağlar kıyıya diktir, Akdeniz’de delta ovaları başka akarsulardandır, Doğu Anadolu’nun kıyısı yoktur.','Karadeniz Bölgesi')],
 'Birden çok ipucu varsa en ayırt edici olanla başla, ötekileri onun üzerinde sına.','üç ipucu birlikte',sirala=lambda s:s,harf='D')
bitir(P,'yersekli','cog|Türkiye’nin Yer Şekilleri','Türkiye’nin Yer Şekilleri',zd={'kolay':1,'orta':3})
