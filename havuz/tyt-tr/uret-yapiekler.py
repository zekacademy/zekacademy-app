"""TYT Türkçe · Sözcükte Yapı/Ekler: 4 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (biçim bilgisi: yapı ve ekler) ve MEB Türk Dili ve Edebiyatı müfredatı'
KARTLAR={
 'K-YE-01':dict(alt='Yapı Bakımından Sözcükler',fikir='Sözcüğün basit, türemiş ya da birleşik yapılı olduğunu kök ve ek çözümlemesiyle belirlemek.',tuzak='Yapım eki almış sözcüğü basit sanmak; birleşik sözcüğü türemiş saymak.',zorluk='kolay',kalip='düz',adim=2,tipId='yap-yapi',kaynak=KY),
 'K-YE-02':dict(alt='Yapım Eki ve Çekim Eki',fikir='Sözcükteki eklerin yapım eki mi çekim eki mi olduğunu ayırt etmek.',tuzak='Çoğul, hâl ve iyelik eklerini yapım eki sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='yap-yapimcekim',kaynak=KY),
 'K-YE-03':dict(alt='Ekin Türü (Kök Türü)',fikir='Yapım ekinin hangi tür sözcükten hangi tür sözcük türettiğini belirlemek.',tuzak='Kökün türünü bakmadan eki görünce karar vermek.',zorluk='orta',kalip='düz',adim=3,tipId='yap-ekturu',kaynak=KY),
 'K-YE-04':dict(alt='Ek Sayısı ve Sırası',fikir='Birden fazla ek alan sözcüklerde yapım ve çekim eklerini sayıp sıralamak.',tuzak='Sözcüğü eksik çözümlemek; çekim ekini yapım eki saymak.',zorluk='zor',kalip='düz',adim=4,tipId='yap-eksayi',kaynak=KY),
}
TIPLER={'yap-yapi':'Yapı bakımından sözcükler','yap-yapimcekim':'Yapım eki ve çekim eki','yap-ekturu':'Ekin türü','yap-eksayi':'Ek sayısı ve sırası'}
Q=kur('yapiekler','Sözcükte Yapı/Ekler','tr|Sözcükte Yapı/Ekler',KARTLAR,TIPLER); Q.n=4
B_YAPI=B('Yapı bakımından sözcükler','basit: kök halinde, ek almamış (göz, sandalye) · türemiş: kök + yapım eki (göz+lük) · birleşik: iki sözcüğün birleşmesi (baş+bakan)')
B_EK=B('Yapım eki / çekim eki','yapım eki sözcüğün anlamını ya da türünü değiştirir (göz → gözlük) · çekim eki sözcüğü cümleye bağlar, anlamını değiştirmez (çoğul -ler, hâl -i/-e/-den, iyelik -im, kişi, zaman ekleri)')
B_TUR=B('Ekin türü','isimden isim: göz+lük · fiilden isim: oku+yucu · isimden fiil: baş+la- · fiilden fiil: yaz+dır-. Ek, kökün türüne göre adlandırılır')

# 0001 yapı · kolay · A
soru(Q,'0001','K-YE-01','kolay','Sözcüklerin yapı bakımından basit, türemiş ve birleşik olduğunu ayırt eder.',2,
 'Aşağıdaki sözcüklerden hangisi yapı bakımından basit bir sözcüktür?',
 [('sandalye','basit','','' ),
  ('gözlük','türemiş','Göz + -lük: yapım eki aldığı için türemiş yapılıdır; basit değildir.','bilgi'),
  ('başbakan','birleşik','Baş + bakan: iki sözcüğün birleşmesidir; birleşik yapılıdır.','bilgi'),
  ('güzellik','türemiş','Güzel + -lik: yapım eki almıştır; türemiştir.','dikkat'),
  ('hanımeli','birleşik','Hanım + eli: iki sözcük kaynaşarak yeni bir kavramı (bitki adı) karşılar; birleşiktir.','bilgi')],
 'A',lambda t:t=='basit','Yapı bakımından basit olan sözcük.',
 'Sözcüğü köküne ve eklerine ayırmayı dene; ek almamış, tek parçalı olanı ara.',[B_YAPI],
 [AD('Yapı türlerini hatırla','Basit sözcük ek almaz, iki sözcükten de oluşmaz.','basit = tek kök'),AD('Şıkları çözümle','gözlük: göz+lük, güzellik: güzel+lik (türemiş). başbakan: baş+bakan, hanımeli: hanım+eli (birleşik).','B, D: türemiş · C, E: birleşik'),AD('Basit olanı seç','Sandalye bölünemeyen, ek almamış bir sözcüktür.','sandalye: basit')],
 'Sözcüğü parçalara ayırabiliyorsan basit değildir; parça yoksa basittir.')

# 0002 yapım eki · orta · D
soru(Q,'0002','K-YE-02','orta','Sözcükteki ekin yapım eki mi çekim eki mi olduğunu belirler.',3,
 'Aşağıdaki sözcüklerden hangisi bir yapım eki almıştır?',
 [('evlerden',(0,2),'Ev + -ler (çoğul) + -den (ayrılma hâli): iki ek de çekim ekidir.','bilgi'),
  ('kitabın',(0,1),'Kitap + -ın (tamlayan eki): çekim ekidir, yapım eki yoktur.','bilgi'),
  ('yazdık',(0,2),'Yaz- + -dı (geçmiş zaman) + -k (kişi): ikisi de çekim ekidir.','dikkat'),
  ('balıkçı',(1,0),'',''),
  ('gözlerim',(0,2),'Göz + -ler (çoğul) + -im (iyelik): ikisi de çekim ekidir.','bilgi')],
 'D',lambda t:t[0]>=1,'Yapım eki almış sözcük.',
 'Eki çıkarınca sözcüğün anlamı ya da türü değişiyor mu diye kontrol et.',[B_EK],
 [AD('İki ek türünü ayır','Yapım eki yeni sözcük türetir; çekim eki türetmez, yalnız cümledeki göreve işaret eder.','yapım: yeni sözcük · çekim: görev'),AD('Şıkları çözümle','evlerden: ev+ler+den. kitabın: kitap+ın. yazdık: yaz+dı+k. gözlerim: göz+ler+im. Hepsinde yalnız çekim eki var.','A, B, C, E: yalnız çekim'),AD('Yapım ekini bul','Balıkçı: balık + -çı. Ek, “balık avlayan ya da satan kişi” anlamlı yeni bir sözcük türetmiştir.','D: balık+çı')],
 'Eki çıkardığında yeni bir kavram kayboluyorsa ek yapım ekidir.')

# 0003 ekin türü · orta · E
soru(Q,'0003','K-YE-03','orta','Yapım ekinin türettiği sözcüğün kökünün türünü belirler.',3,
 'Aşağıdaki sözcüklerden hangisi fiilden türemiş bir isimdir?',
 [('gözlük','isim','Göz + -lük: kök bir isimdir; ek isimden isim türetmiştir.','bilgi'),
  ('çiçekçi','isim','Çiçek + -çi: kök isimdir; fiil kökü yoktur.','bilgi'),
  ('güzellik','sıfat','Güzel + -lik: kök sıfat (isim soylu) bir sözcüktür; fiilden türememiştir.','dikkat'),
  ('evcil','isim','Ev + -cil: kök isimdir; üstelik türeyen sözcük isim değil sıfattır.','bilgi'),
  ('okuyucu','fiil','','')],
 'E',lambda t:t=='fiil','Fiilden türemiş isim.',
 'Her sözcüğün kökünü bul; kökü “-mek” alabilen (fiil olan) sözcüğü ara.',[B_TUR],
 [AD('Kökleri ayır','Her sözcüğü ek ve köke ayır: göz+lük, çiçek+çi, güzel+lik, ev+cil, oku+yucu.','5 kök'),AD('Kök türüne bak','Göz, çiçek, ev isim; güzel sıfattır. Bunların hiçbiri fiil değildir.','A, B, C, D: fiil kökü yok'),AD('Fiil kökünü bul','Oku- bir fiildir; -yucu eki fiilden isim yapar. Okumak denilebilir.','E: oku- fiil')],
 'Kök “-mek” alıp fiil oluyorsa ve türeyen sözcük isimse ek fiilden isim yapma ekidir.')

# 0004 ek sayısı · zor · B
soru(Q,'0004','K-YE-04','zor','Sözcükteki yapım ve çekim eklerini sayarak ayırt eder.',4,
 'Aşağıdaki sözcüklerden hangisinde birden fazla yapım eki vardır ve çekim eki yoktur?',
 [('kitaplık',(1,0),'Kitap + -lık: yalnız bir yapım eki vardır; birden fazla değildir.','islem'),
  ('gözlükçü',(2,0),'',''),
  ('balıkçıya',(1,1),'Balık + -çı (yapım) + -ya (yönelme hâli, çekim): bir yapım, bir çekim eki vardır.','dikkat'),
  ('evlerde',(0,2),'Ev + -ler + -de: iki ek de çekim ekidir; yapım eki yoktur.','bilgi'),
  ('okuyucu',(1,0),'Oku- + -yucu: tek yapım eki vardır.','islem')],
 'B',lambda t:t[0]>=2 and t[1]==0,'Birden fazla yapım eki olup çekim eki olmayan sözcük.',
 'Her sözcüğü köküne kadar çöz; ekleri yapım ve çekim diye iki sütunda say.',[B_EK],
 [AD('Ölçütü yaz','İki koşul var: en az iki yapım eki, hiç çekim eki yok.','yapım ≥ 2 · çekim = 0'),AD('Şıkları say','kitaplık 1 yapım. balıkçıya 1 yapım ve 1 çekim. evlerde 2 çekim. okuyucu 1 yapım.','A, C, D, E: koşulu sağlamıyor'),AD('Çözümü doğrula','Gözlükçü: göz + -lük + -çü. İki ek de yeni sözcük türetir ve çekim eki yoktur.','B: göz+lük+çü')],
 'Ek saymada her şıkkı köke kadar çöz ve yapım-çekim ayrımını tabloya dök.')
bitir(Q)
