"""Denklem Çözme · parti 2 (hafif mod): 24 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Denklem Çözme'
UK='mat|Denklem Çözme'
P=Parti('denklemiki','Denklem Çözme',UK)
def lin(f):
    f0=Fr(f(Fr(0))); f1=Fr(f(Fr(1))); assert f1!=f0; x=-f0/(f1-f0); assert f(x)==0; return x
DAG=B('Dağılma ve işaret','parantezin önündeki sayı içerideki her terimle çarpılır; önünde eksi varsa tüm terimlerin işareti değişir. Örnek: −2(3 − x) = −6 + 2x')
PAYDA=B('Paydaları eşitleme','denklemin her iki tarafı paydaların EKOK’u ile çarpılır; sabit terimler de çarpılmayı unutmamalıdır. Örnek: x/2 + 1/3 = 2 için 6 ile çarp: 3x + 2 = 12')
KUME=B('p·x = q denkleminin çözüm kümesi','p ≠ 0 ise tek çözüm x = q/p; p = 0 ve q ≠ 0 ise çözüm yok (boş küme); p = 0 ve q = 0 ise her gerçel sayı çözümdür. Örnek: 0·x = 5 → boş küme · 0·x = 0 → ℝ')
OZDES=B('Her x için sağlanan denklem','p·x + q = r·x + s eşitliği her x için doğruysa x’in katsayıları ve sabitler ayrı ayrı eşittir: p = r ve q = s. Örnek: (a + 1)x + 3 = 5x + 3 her x için doğruysa a + 1 = 5')
SIS=B('Denklem sistemi','iki denklem taraf tarafa toplanır ya da çıkarılarak bir bilinmeyen yok edilir. Örnek: x + y = 5 ve x − y = 1 toplanırsa 2x = 6, x = 3, y = 2')
SSON=B('Sistemin çözümü','p·x + q·y = r ve s·x + t·y = u sisteminde p/s = q/t = r/u ise sonsuz çözüm; p/s = q/t ≠ r/u ise çözüm yoktur. Örnek: x + y = 2 ve 2x + 2y = 4 sonsuz çözümlüdür')
UCLU=B('Denklemleri toplayarak sadeleştirme','üç bilinmeyenli sistemde istenen toplam çoğu zaman denklemler taraf tarafa toplanıp ortak katsayıya bölünerek bulunur; her bilinmeyeni ayrı ayrı bulmak gerekmez. Örnek: a + b = 3, b + c = 4, a + c = 5 toplanırsa 2(a + b + c) = 12')
ORAN=B('İçler dışlar çarpımı','a/b = c/d ise a·d = b·c. Örnek: 3/x = 6/4 ise 6x = 12, x = 2. Paydalar sıfır olamaz')
ORK=B('Oranı k ile yazmak','x/y = 3/4 ise x = 3k, y = 4k yazılır. Örnek: x/y = 3/4 ve x + y = 14 ise 7k = 14, k = 2 → x = 6, y = 8')
KUR=B('Denklem kurma','soruda bilinmeyen bir harfle gösterilir, verilen koşullar eşitlik olarak yazılır ve çözülür. Örnek: bir sayının 3 katının 4 fazlası 19 ise 3x + 4 = 19, x = 5')
TANIM=B('Tanımlı işlem','işlem sembolü soruda verilen kurala göre uygulanır; parantez içi önce yapılır. Örnek: a ⊗ b = a + 2b ise 3 ⊗ 4 = 3 + 8 = 11, (1 ⊗ 2) ⊗ 3 = 5 ⊗ 3 = 11')
MAKINE=B('Makine kuralı','makine girdiye kuralını uygular; iki makine ardışıksa birinin çıktısı diğerinin girdisidir. Örnek: kural n → 2n + 1 ise girdi 3 için çıktı 7, bu çıktı yine girilirse 15 olur')
OLC=B('Ters işlem','sonuçtan girdiye giderken işlemler ters sırada ve ters işaretle geri alınır. Örnek: n → 2n + 1 ve çıktı 9 ise önce 1 çıkarılır (8), sonra 2’ye bölünür (4)')
DENK=B('Denklemin her iki yanına aynı işlem','bir denklemin iki yanı da aynı sayıyla çarpılır ya da bölünürse eşitlik bozulmaz; hata, bir terimi atlamaktan doğar. Örnek: x/2 + 1 = 3 için 2 ile çarp: x + 2 = 6')
KY='ÖSYM 2018–2026 TYT Matematik (denklem çözme, denklem sistemleri) · yayın soru bankaları (yalnız mantık) · MEB 8–9. sınıf'
kart('K-DNKB-01','Birinci dereceden denklem (paydalı, parantezli)','Parantezleri aç, paydaları EKOK ile eşitle, bilinmeyenleri tek yana topla.','Eksi işaretli parantezde işareti değiştirmemek; sabit terimi EKOK ile çarpmamak.','orta','düz',3,'dkb-birinci','Birinci dereceden denklem: paydalı ve parantezli',KY)
kart('K-DNKB-02','Çözüm kümesi boş / sonsuz, parametre','a·x = b biçimine getirip katsayı ve sabite göre çözüm sayısı ve parametre bulunur.','a = 0 iken b’ye bakmamak; iki ayrı özel durumu (∅ ve ℝ) karıştırmak.','zor','düz',4,'dkb-kume','Çözüm kümesi boş / sonsuz ve parametre',KY)
kart('K-DNKB-03','İki bilinmeyenli denklem sistemi','Yok etme ya da yerine koymayla x ve y bulunur; x + y ve x − y için denklemler toplanır / çıkarılır.','İşareti hatalı toplamak; sorulan ifadeyi (x yerine x − y) değiştirmek.','orta','düz',3,'dkb-sistem','İki bilinmeyenli denklem sistemi',KY)
kart('K-DNKB-04','Üç bilinmeyenli sistemde istenen toplam','Denklemler taraf tarafa toplanıp katsayıya bölünerek istenen toplam bulunur.','Toplamı katsayıya bölmemek; yalnız bir bilinmeyeni hesaplamak.','orta','hikâyeli',3,'dkb-uclu','Üç bilinmeyenli sistemde toplam',KY)
kart('K-DNKB-05','Oranlı denklem','İçler dışlar çarpımı ya da oranı k ile yazma; x² terimleri sadeleşen denklemler birinci dereceye iner.','Çapraz çarpımı hatalı kurmak; paydayı sıfır yapan değeri kontrol etmemek.','orta','düz',3,'dkb-oran','Oranlı denklem',KY)
kart('K-DNKB-06','Denklem kurma (kısa hikâye)','Hikâyedeki koşullar bir ya da iki bilinmeyenle denkleme çevrilir.','Farkı iki yerde saymak; sorulan nicelikle bulunan niceliği karıştırmak.','orta','hikâyeli',3,'dkb-kurma','Denklem kurma: fiyat, bilet, yol',KY)
kart('K-DNKB-07','Tanımlı işlem, makine ve işlem hatası','Kural uygulanarak denklem kurulur; makinede ters işlemler ya da öğrencinin hatası yeniden kurularak doğru sonuç bulunur.','İşlem sırasını karıştırmak; hatalı ve doğru çözümü karıştırmak.','zor','yeni nesil',4,'dkb-islem','Tanımlı işlem, makine, işlem hatası',KY)

# ---------- 01 kolay · parantezli ----------
f=lambda x:7-3*(2-x)-(4*x-3*(x+1)); assert lin(f)==-2
w=[lin(lambda x:7-3*2-x-(4*x-3*(x+1))),lin(lambda x:7-3*(2-x)-(4*x-3*x+3)),lin(lambda x:4*(2-x)-(4*x-3*(x+1)))]
assert w==[2,1,Fr(11,5)] and Fr(-4,1)==-4
mk(P,'0001',tipId='dkb-birinci',tip='Birinci dereceden denklem: paydalı ve parantezli',z='kolay',alt='Parantezli Denklem',kaz='Eksi işaretli parantezleri açıp iki yanda x içeren denklemi çözer.',kalip='düz',adim=4,
 kart='K-DNKB-01 (birinci dereceden denklem) · iki yanda x ve eksi işaretli parantez',
 metin='7 − 3(2 − x) = 4x − 3(x + 1)\nolduğuna göre x kaçtır?',
 dogru=-2,yan=[(2,'−3(2 − x) = −6 − x yazmış; −3, x ile de çarpılmalı.','bilgi'),(1,'−3(x + 1)’i −3x + 3 yazmış; −3, 1 ile çarpılınca −3 olur.','bilgi'),(Fr(11,5),'7 − 3 = 4 yapıp 4(2 − x) yazmış; −3 yalnız parantezle çarpılır.','bilgi'),(-4,'2x = −4’te 2’ye bölmeyi unutmuş.','islem')],
 istenen='Denklemi sağlayan x değeri.',
 ip=['Önce iki parantezi aç; önündeki eksi işaretlerine dikkat et.'],
 bilgi=[DAG],
 ad=[A('Parantezleri aç','−3, 2 ve −x ile; −3, x ve 1 ile çarpılır.','7 − 6 + 3x = 4x − 3x − 3'),A('Sadeleştir','Her yanda benzer terimleri topla.','3x + 1 = x − 3'),A('x’i yalnız bırak','x’leri sola, sayıları sağa topla.','3x − x = −3 − 1'),A('Böl','Katsayıya böl.','2x = −4 → x = −2')],
 puf='Eksi işaretli parantezi açarken tüm terimlerin işaretini değiştir.')

# ---------- 02 kolay · paydalı ----------
f=lambda x:Fr(2*x,3)-5-(Fr(x,6)+1); assert lin(f)==12
assert lin(lambda x:4*x-5-(x+1))==2 and lin(lambda x:4*x-30-(x-6))==8 and Fr(-24,3)==-8 and Fr(36,1)==36
mk(P,'0002',tipId='dkb-birinci',tip='Birinci dereceden denklem: paydalı ve parantezli',z='kolay',alt='Paydalı Denklem',kaz='Paydaları EKOK ile eşitleyerek birinci dereceden denklemi çözer.',kalip='düz',adim=3,
 kart='K-DNKB-01 (birinci dereceden denklem) · iki yanda paydalı terim ve sabit',
 metin='2x/3 − 5 = x/6 + 1\neşitliğini doğrulayan x gerçel sayısı kaçtır?',
 dogru=12,yan=[(2,'6 ile çarparken −5 ve 1’i çarpmamış: 4x − 5 = x + 1.','dikkat'),(8,'6 ile çarparken 1’i 6 yerine −6 yazmış: 4x − 30 = x − 6.','islem'),(-8,'3x = 6 − 30 = −24 yazmış; −30, karşı tarafa +30 geçer.','islem'),(36,'3x = 36’da 3’e bölmeyi unutmuş.','islem')],
 istenen='Denklemi sağlayan x değeri.',
 ip=['Paydaların EKOK’u olan sayıyla iki yanın her terimini çarp.'],
 bilgi=[PAYDA],
 ad=[A('EKOK ile çarp','3 ve 6’nın EKOK’u 6; her terim 6 ile çarpılır.','4x − 30 = x + 6'),A('x’leri topla','x’ler sola, sayılar sağa.','4x − x = 6 + 30 → 3x = 36'),A('Böl','Katsayıya böl.','x = 12')],
 puf='Paydalı denklemde sabit terimler de EKOK ile çarpılır; yalnız kesirli terimleri çarpmak hatadır.')

# ---------- 03 kolay · sistem ----------
x_=Fr(4);y_=Fr(5); assert x_+y_==9 and 2*x_-y_==3
assert lin(lambda x:2*x-(9-x)-3)==4 and lin(lambda x:2*x-9-x-3)==12 and 9-12==-3 and 4*5==20
mk(P,'0003',tipId='dkb-sistem',tip='İki bilinmeyenli denklem sistemi',z='kolay',alt='Denklem Sistemi',kaz='Denklemleri taraf tarafa toplayarak yok etme yöntemiyle y değerini bulur.',kalip='düz',adim=3,
 kart='K-DNKB-03 (iki bilinmeyenli sistem) · toplayarak yok etme, y istenir',
 metin='x ve y gerçel sayılardır.\nx + y = 9\n2x − y = 3\nolduğuna göre y kaçtır?',
 dogru=5,yan=[(4,'x’i bulup y yerine x’i yazmış.','dikkat'),(-3,'y yerine 9 − x yazıp −(9 − x)’i −9 − x açmış; x = 12, y = −3 bulmuş.','bilgi'),(9,'İlk denklemin sağ tarafını y’nin değeri sanmış.','dikkat'),(20,'x · y çarpımını bulmuş.','dikkat')],
 istenen='y’nin değeri.',
 ip=['İki denklemde y’nin katsayılarına bak; ne fark ediyorsun?'],
 bilgi=[SIS],
 ad=[A('Topla','y’ler birbirini götürür.','(x + y) + (2x − y) = 9 + 3 → 3x = 12'),A('x’i bul','3’e böl.','x = 4'),A('y’yi yaz','x’i ilk denklemde yerine koy.','4 + y = 9 → y = 5')],
 puf='Katsayıları zıt işaretli bilinmeyeni yok etmek için denklemleri topla.')

# ---------- 04 kolay · taksi ----------
assert lin(lambda x:50+25*x-350)==12 and Fr(350,25)==14 and Fr(350+50,25)==16 and 350-50==300 and 350-25==325
mk(P,'0004',tipId='dkb-kurma',tip='Denklem kurma: fiyat, bilet, yol',z='kolay',alt='Denklem Kurma',kaz='Açılış ücreti ve kilometre ücretinden denklem kurarak gidilen yolu bulur.',kalip='hikâyeli',adim=3,
 kart='K-DNKB-06 (denklem kurma) · sabit ücret + birim ücret',
 metin='Bir taksinin sayacı açılışta 50 TL gösteriyor ve sayaç, gidilen her kilometre için 25 TL artıyor (artış gidilen yolla orantılıdır). Başka bir ücret alınmıyor.\nBir yolcu yolculuk sonunda sayaçta 350 TL gördüğüne göre kaç kilometre yol gitmiştir?',
 dogru=12,yan=[(14,'Açılış ücretini düşmeden 350’yi 25’e bölmüş.','dikkat'),(16,'Açılış ücretini düşmek yerine 350’ye eklemiş: (350 + 50) ÷ 25.','islem'),(300,'Açılış ücretini düşüp 25’e bölmeyi unutmuş.','dikkat'),(325,'Kilometre ücretini (25) açılış ücreti yerine 350’den çıkarmış.','dikkat')],
 istenen='Gidilen yol (km).',
 ip=['Yol x km ise sayacın göstereceği tutarı x cinsinden yaz ve 350’ye eşitle.'],
 bilgi=[KUR],
 ad=[A('Denklemi kur','x km için tutar: açılış + 25x.','50 + 25x = 350'),A('Sabiti karşıya geç','50’yi 350’den çıkar.','25x = 300'),A('Böl','25’e böl.','x = 12')],
 puf='Sabit ücret + birim ücret × miktar = toplam; önce sabit ücreti çıkar, sonra birim ücrete böl.')

# ---------- 05 kolay · oranlı ----------
assert lin(lambda x:x+3-2*(x-1))==5 and Fr(5+3,5-1)==2
assert lin(lambda x:x+3-2*x-2)==1 and lin(lambda x:x+3-(2*x-1))==4 and 3-(-2)==5 and -1+0==-1
mk(P,'0005',tipId='dkb-oran',tip='Oranlı denklem',z='kolay',alt='Oranlı Denklem',kaz='Eşitliğe dönüşen kesirli oranı içler dışlar çarpımıyla çözer.',kalip='düz',adim=3,
 kart='K-DNKB-05 (oranlı denklem) · kesir = tam sayı, paydada x',
 metin='(x + 3)/(x − 1) = 2\nolduğuna göre x kaçtır?',
 dogru=5,yan=[(-5,'x + 3 = 2x − 2’den −x = −5 yazıp x = −5 bulmuş.','islem'),(-1,'Yalnız payı 2’ye eşitlemiş: x + 3 = 2.','bilgi'),(1,'x + 3 = 2x + 2 yazmış; 2(x − 1) = 2x − 2’dir.','bilgi'),(4,'2(x − 1)’i 2x − 1 açmış; 2, −1 ile de çarpılmalı.','bilgi')],
 istenen='x değeri.',
 ip=['Paydayı karşı yana çarpan olarak geçir: 2 ile (x − 1)’in tamamını çarp.'],
 bilgi=[ORAN,DAG],
 ad=[A('Paydayı kaldır','Her iki yanı (x − 1) ile çarp.','x + 3 = 2(x − 1)'),A('Parantezi aç','2 her terimle çarpılır.','x + 3 = 2x − 2'),A('Çöz','x’leri tek yana topla.','3 + 2 = 2x − x → x = 5')],
 puf='Kesirli denklemde payda karşı yana çarpan olarak geçer; paydayı sıfır yapan değeri sonda denetle (x = 5 için payda 4).')

# ---------- 06 orta · x − y ----------
x_,y_=5,2; assert 4*x_+3*y_==26 and 3*x_+4*y_==23 and x_-y_==3 and x_+y_==7 and 26+23==49 and x_*y_==10
mk(P,'0006',tipId='dkb-sistem',tip='İki bilinmeyenli denklem sistemi',z='orta',alt='Denklem Sistemi',kaz='Simetrik katsayılı sistemde denklemleri çıkararak x − y farkını bulur.',kalip='düz',adim=3,
 kart='K-DNKB-03 (iki bilinmeyenli sistem) · simetrik katsayı, fark istenir',
 metin='x ve y gerçel sayılardır.\n4x + 3y = 26\n3x + 4y = 23\nolduğuna göre x − y kaçtır?',
 dogru=3,yan=[(5,'x’i bulup soruyu x sanmış.','dikkat'),(7,'Denklemleri toplayıp 7(x + y) = 49’dan x + y = 7 bulmuş; fark sorulmuş.','dikkat'),(10,'x ve y’yi bulup x · y çarpımını vermiş.','dikkat'),(49,'Denklemleri toplayıp sonucu 7’ye bölmemiş.','islem')],
 istenen='x − y farkı.',
 ip=['İki denklemin katsayıları arasında nasıl bir ilişki var? İstenen ifade bu ilişkiyle nasıl elde edilir?'],
 bilgi=[SIS],
 ad=[A('Çıkar','Birinci denklemden ikinciyi çıkar.','(4x − 3x) + (3y − 4y) = 26 − 23'),A('Sadeleştir','Sol yan x − y olur.','x − y = 3'),A('Kontrol','Toplayarak x + y = 7 bulunur; x = 5, y = 2.','4 × 5 + 3 × 2 = 26 ✓')],
 puf='Katsayıları yer değiştirmiş sistemlerde toplayınca x + y, çıkarınca x − y doğrudan çıkar.')

# ---------- 07 orta · koli (üçlü, ikişerli toplam) ----------
K,Lv,M=8,6,11; assert Fr(14+19-17,2)==8 and Fr(50,4)==Fr(25,2) and K+Lv==14 and Lv+M==17 and K+M==19 and K+Lv+M==25 and 14+17+19==50 and 17+19==36 and 14+17==31
mk(P,'0007',tipId='dkb-uclu',tip='Üç bilinmeyenli sistemde toplam',z='orta',alt='Üç Bilinmeyenli Sistem',kaz='İkişerli toplamlardan üç niceliğin toplamını denklemleri toplayarak bulur.',kalip='hikâyeli',adim=3,
 kart='K-DNKB-04 (üçlü sistem) · ikişerli tartım toplamları',
 metin='Bir depocu, K, L ve M kolilerini ikişerli tartıyor.\nK ile L’nin kütleleri toplamı 14 kg,\nL ile M’nin kütleleri toplamı 17 kg,\nK ile M’nin kütleleri toplamı 19 kg\nbulunuyor.\nBuna göre üç kolinin kütleleri toplamı kaç kilogramdır?',
 dogru=25,yan=[(8,'K = (14 + 19 − 17) ÷ 2 = 8 bulup durmuş; üç kolinin toplamını hesaplamamış.','dikkat'),(Fr(25,2),'Üç denklemi toplayıp sonucu 4’e bölmüş (50 ÷ 4).','islem'),(36,'İki toplamı (17 + 19) toplayıp üçüncüsünü katmamış.','dikkat'),(50,'Üç denklemi toplayıp sonucu 2’ye bölmemiş.','islem')],
 istenen='K, L ve M kolilerinin toplam kütlesi (kg).',
 ip=['Her koli kaç toplamda yer alıyor? İstenen toplam için bunu nasıl kullanırsın?'],
 bilgi=[UCLU],
 ad=[A('Denklemleri topla','Her koli iki toplamda yer alır.','(K + L) + (L + M) + (K + M) = 14 + 17 + 19'),A('Sadeleştir','Sol yan her koliden iki tane içerir.','2(K + L + M) = 50'),A('Böl','Toplamı 2’ye böl.','K + L + M = 25 kg')],
 puf='İkişerli toplamlardan üçlü toplama giderken denklemleri toplayıp 2’ye böl.')

# ---------- 08 orta · üçlü katsayılı ----------
x_,y_,z_=6,4,2; assert x_+2*y_+3*z_==20 and 3*x_+2*y_+z_==28 and x_+y_+z_==12 and 48//4==12 and x_-z_==4 and 48//2==24 and 48//3==16
assert all(a+b+c==12 for a in range(0,21) for b in range(0,21) for c in range(0,21) if a+2*b+3*c==20 and 3*a+2*b+c==28)
mk(P,'0008',tipId='dkb-uclu',tip='Üç bilinmeyenli sistemde toplam',z='orta',alt='Üç Bilinmeyenli Sistem',kaz='Katsayıları farklı iki denklemi toplayarak x + y + z toplamını bulur.',kalip='düz',adim=3,
 kart='K-DNKB-04 (üçlü sistem) · iki denklemden üçlü toplam',
 metin='x, y ve z gerçel sayılardır.\nx + 2y + 3z = 20\n3x + 2y + z = 28\nolduğuna göre x + y + z toplamı kaçtır?',
 dogru=12,yan=[(4,'Denklemleri çıkarıp x − z = 4 bulmuş; toplam sorulmuş.','dikkat'),(16,'Toplayıp 48’i 3’e bölmüş; ortak katsayı 4’tür.','islem'),(24,'Toplayıp 48’i 2’ye bölmüş; ortak katsayı 4’tür.','islem'),(48,'Denklemleri toplayıp 4’e bölmemiş.','islem')],
 istenen='x + y + z toplamı.',
 ip=['İki denklemde aynı bilinmeyenin katsayılarını topla; ne görüyorsun?'],
 bilgi=[UCLU],
 ad=[A('Topla','Aynı bilinmeyenlerin katsayılarını topla.','(1 + 3)x + (2 + 2)y + (3 + 1)z = 20 + 28'),A('Ortak çarpanı gör','Her katsayı 4 çıkar.','4x + 4y + 4z = 48'),A('Böl','4’e böl.','x + y + z = 12')],
 puf='Denklemleri toplayınca katsayılar eşitleniyorsa, bilinmeyenleri tek tek bulmadan toplam doğrudan çıkar.')

# ---------- 09 orta · oran ve fark ----------
k=Fr(5); x_,y_=3*k,4*k; assert 2*x_-y_==10 and x_+y_==35 and Fr(10,5)==2 and 7*2==14
mk(P,'0009',tipId='dkb-oran',tip='Oranlı denklem',z='orta',alt='Oran ve Denklem',kaz='Oranı k ile yazıp verilen denklemden x + y toplamını bulur.',kalip='düz',adim=3,
 kart='K-DNKB-05 (oranlı denklem) · oranı k ile yazıp denkleme taşıma',
 metin='x ve y, y ≠ 0 olan gerçel sayılardır.\nx/y = 3/4\n2x − y = 10\nolduğuna göre x + y toplamı kaçtır?',
 dogru=35,yan=[(5,'Ortak değeri k = 5’i bulup x + y’yi hesaplamamış.','dikkat'),(14,'Oranı ters yazıp x = 4k, y = 3k almış: 8k − 3k = 10, k = 2, x + y = 7k = 14.','bilgi'),(15,'x’i bulup toplamı sormuş olduğunu unutmuş.','dikkat'),(20,'y’yi bulup toplamı sormuş olduğunu unutmuş.','dikkat')],
 istenen='x + y toplamı.',
 ip=['x ve y’yi ortak bir k ile yaz, sonra verilen ikinci denkleme taşı.'],
 bilgi=[ORK],
 ad=[A('k ile yaz','x/y = 3/4 olduğundan.','x = 3k · y = 4k'),A('Denkleme taşı','2x − y = 10’da yerine yaz.','6k − 4k = 10 → k = 5'),A('Toplamı bul','x + y = 7k.','7 × 5 = 35')],
 puf='Oran verilince ortak k’yi seç; ikinci koşul k’yi bulmak için kullanılır.')

# ---------- 10 orta · pay payda çapraz, x² sadeleşir ----------
f=lambda x:(x-1)*(x+8)-(x+3)*(x+2); assert lin(f)==7
assert Fr(7-1,7+2)==Fr(7+3,7+8)
assert lin(lambda x:(x**2+7*x+8)-(x**2+5*x+6))==-1 and lin(lambda x:(x**2+7*x-8)-(x**2+5*x+5))==Fr(13,2) and lin(lambda x:(x-1)*(x+2)-(x+3)*(x+8))==Fr(-13,5)
mk(P,'0010',tipId='dkb-oran',tip='Oranlı denklem',z='orta',alt='İçler Dışlar Çarpımı',kaz='x² terimleri sadeleşen oranlı denklemi içler dışlar çarpımıyla çözer.',kalip='düz',adim=3,
 kart='K-DNKB-05 (oranlı denklem) · iki kesrin eşitliği, x² sadeleşir',
 metin='(x − 1)/(x + 2) = (x + 3)/(x + 8)\nolduğuna göre x kaçtır?',
 dogru=7,yan=[(Fr(-13,5),'Payları kendi aralarında, paydaları kendi aralarında çarpmış: (x − 1)(x + 2) = (x + 3)(x + 8).','bilgi'),(-1,'(x − 1)(x + 8)’i x² + 7x + 8 açmış; −1 × 8 = −8’dir.','islem'),(Fr(13,2),'(x + 3)(x + 2)’yi x² + 5x + 5 açmış; 3 × 2 = 6’dır.','islem'),(14,'2x = 14’te 2’ye bölmeyi unutmuş.','islem')],
 istenen='x değeri.',
 ip=['İçler dışlar çarpımı yap: birinci payı ikinci paydayla, ikinci payı birinci paydayla çarp.'],
 bilgi=[ORAN],
 ad=[A('Çapraz çarp','Pay × karşı payda.','(x − 1)(x + 8) = (x + 3)(x + 2)'),A('Çarpımları aç','x² terimleri iki yanda da var.','x² + 7x − 8 = x² + 5x + 6'),A('x²’leri sadeleştir','Kalan birinci derece denklemdir.','2x = 14 → x = 7')],
 puf='İki yanda aynı x² görünüyorsa çarpımları açınca birbirini götürür; denklem birinci dereceye iner.')

# ---------- 11 orta · her x için ----------
a_,b_=4,-3; assert 3*a_-2==10 and 2*b_+1==-5 and a_*b_==-12
assert 10*(-5)==-50 and Fr(-5-1,2)==-3 and Fr(-5+1,2)==-2 and 4*-2==-8 and a_+b_==1 and 4*3==12
mk(P,'0011',tipId='dkb-kume',tip='Çözüm kümesi boş / sonsuz ve parametre',z='orta',alt='Özdeşlik',kaz='Denklemin her x için sağlanması koşulundan parametreleri bulur.',kalip='düz',adim=3,
 kart='K-DNKB-02 (çözüm kümesi, parametre) · her x için sağlanır, çarpım istenir',
 metin='a ve b gerçel sayılardır.\n(3a − 2)x + 2b + 1 = 10x − 5\neşitliği her x gerçel sayısı için sağlandığına göre a · b çarpımı kaçtır?',
 dogru=-12,yan=[(-50,'Katsayıları doğrudan a = 10, b = −5 almış; 3a − 2 = 10 ve 2b + 1 = −5 çözülmeli.','bilgi'),(-8,'2b = −5 + 1 = −4 yazıp b = −2 bulmuş; 1 karşıya −1 geçer.','islem'),(1,'a + b toplamını vermiş.','dikkat'),(12,'2b = −5 − 1 = −6’yı b = 3 yazmış; işareti kaçırmış.','islem')],
 istenen='a · b çarpımı.',
 ip=['Eşitlik x’in hangi değerleri için sağlanmalı? İki yanı karşılaştır.'],
 bilgi=[OZDES],
 ad=[A('Katsayıları eşitle','x’li terimler.','3a − 2 = 10 → a = 4'),A('Sabitleri eşitle','Sabit terimler.','2b + 1 = −5 → b = −3'),A('Çarp','İstenen çarpım.','a × b = 4 × (−3) = −12')],
 puf='“Her x için sağlanır” ifadesi katsayıların ve sabitlerin ayrı ayrı eşit olması demektir.')

# ---------- 12 orta · öncüllü ----------
def cs(a,b):
    # (a-2)x=b+1 çözüm kümesi türü
    if a!=2: return 'tek'
    return 'R' if b==-1 else 'bos'
R_=range(-5,6)
I_=all(cs(2,b)=='bos' for b in R_)       # a=2 -> boş (yanlış, b=-1 iken R)
II_=all(cs(a,-1)=='R' for a in R_)       # b=-1 -> R (yanlış)
III_=all(cs(a,b)=='tek' for a in R_ for b in R_ if a!=2)
assert (I_,II_,III_)==(False,False,True)
mk(P,'0012',tipId='dkb-kume',tip='Çözüm kümesi boş / sonsuz ve parametre',z='orta',alt='Çözüm Kümesi Yorumu',kaz='a·x = b biçimindeki denklemin çözüm kümesini katsayı ve sabite göre yorumlar.',kalip='öncüllü',adim=4,
 kart='K-DNKB-02 (çözüm kümesi, parametre) · öncüllü: a = 2 ve a ≠ 2 durumları',
 metin='a ve b gerçel sayılar olmak üzere, x’e bağlı\n(a − 2)x = b + 1\ndenklemi veriliyor.\nBuna göre,\nI. a = 2 ise çözüm kümesi boş kümedir.\nII. b = −1 ise çözüm kümesi gerçel sayılardır.\nIII. a ≠ 2 ise çözüm kümesi tek elemanlıdır.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='Yalnız III',sira=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III'],
 yan=[('Yalnız I','a = 2 iken b’ye bakmadan boş küme sanmış; III’ü de işaretlememiş.','bilgi'),('I ve II','a = 2 iken b’ye, b = −1 iken a’ya bakmadan ikisinin de geçerli olduğunu sanmış; (a = 2, b = −1) özel durumunu görmemiş.','bilgi'),('II ve III','II’yi doğru sanmış; b = −1 iken a ≠ 2 ise tek çözüm vardır.','bilgi'),('I, II ve III','I ve II’deki özel durumları (b’nin değeri, a’nın değeri) sınamadan hepsini doğru sanmış.','dikkat')],
 istenen='Kesinlikle doğru olan öncüllerin hangileri olduğu.',
 ip=['Her öncül için a ve b’ye uygun örnek değerler verip denklemi çöz.'],
 bilgi=[KUME],
 ad=[A('a ≠ 2 durumu','Katsayı sıfırdan farklı; x = (b + 1)/(a − 2) tek değerdir.','III doğru'),A('a = 2 durumu','Denklem 0·x = b + 1 olur; b + 1 ≠ 0 ise boş küme, b + 1 = 0 ise ℝ.','I kesin değil (b = −1 iken ℝ)'),A('b = −1 durumu','Denklem (a − 2)x = 0; a ≠ 2 iken x = 0 tek çözüm.','II kesin değil'),A('Sonuç','Yalnız III her durumda doğrudur.','Yalnız III')],
 puf='a·x = b denkleminde önce a’nın sıfır olup olmadığına, sonra b’ye bak.')

# ---------- 13 orta · konser bileti ----------
o=Fr(80); assert 5*(o+20)+3*o==740 and o+20==100 and Fr(740,8)==Fr(185,2) and 5*Fr(90)+20+3*90==740 and 90+20==110 and Fr(740,5)==148
mk(P,'0013',tipId='dkb-kurma',tip='Denklem kurma: fiyat, bilet, yol',z='orta',alt='Denklem Kurma',kaz='Biletler arasındaki fiyat farkını kullanarak toplam ödemeden bilet fiyatını bulur.',kalip='hikâyeli',adim=4,
 kart='K-DNKB-06 (denklem kurma) · fark bilgisiyle fiyat denklemi',
 metin='Bir konser salonunda tam bilet, öğrenci biletinden 20 TL daha pahalıdır.\nBir grup, 5 tam bilet ve 3 öğrenci bileti için toplam 740 TL ödemiştir.\nBuna göre bir tam biletin fiyatı kaç TL’dir?',
 dogru=100,yan=[(80,'Öğrenci biletinin fiyatını bulup durmuş.','dikkat'),(Fr(185,2),'20 TL farkı hiç kullanmayıp 740’ı 8’e bölmüş.','dikkat'),(110,'20 TL farkı 5 bilet için yalnız bir kez eklemiş; öğrenci 90 çıkmış, tam bileti 110 bulmuş.','islem'),(148,'740’ı yalnız tam bilet sayısına (5) bölmüş.','dikkat')],
 istenen='Bir tam biletin fiyatı (TL).',
 ip=['Öğrenci biletinin fiyatına x de; tam biletin fiyatını x cinsinden yaz ve toplam ödemeyi kur.'],
 bilgi=[KUR],
 ad=[A('Bilinmeyeni seç','Öğrenci bileti x TL ise tam bilet x + 20 TL.','tam = x + 20'),A('Denklemi kur','5 tam + 3 öğrenci = 740.','5(x + 20) + 3x = 740 → 8x + 100 = 740'),A('x’i bul','Çöz.','8x = 640 → x = 80'),A('Tam bileti yaz','Sorulan tam biletin fiyatı.','80 + 20 = 100 TL')],
 puf='Farkı bilinen iki fiyattan küçüğünü bilinmeyen seç; sorulan fiyatı çözümün sonunda ayrıca hesapla.')

# ---------- 14 orta · tanımlı işlem ----------
op=lambda a,b:3*a-b+2
x_=lin(lambda x:op(x,2)-op(6,x)); assert x_==5 and op(x_,x_)==12
assert lin(lambda x:3*x-(3*6-x-2))==4 and 3*4-4+2==10 and 3*5-5-2==8 and 3*5+2==17
mk(P,'0014',tipId='dkb-islem',tip='Tanımlı işlem, makine, işlem hatası',z='orta',alt='Tanımlı İşlem',kaz='Tanımlı işlemle kurulan denklemden bilinmeyeni bulup işlemi tekrar uygular.',kalip='düz',adim=3,
 kart='K-DNKB-07 (tanımlı işlem) · iki yanda işlem, sonra x △ x',
 metin='Gerçel sayılar kümesinde bir △ işlemi\na △ b = 3a − b + 2\nbiçiminde tanımlanıyor.\n(x △ 2) = (6 △ x)\neşitliğini sağlayan x için x △ x işleminin sonucu kaçtır?',
 dogru=12,yan=[(5,'Denklemi çözüp x’i bulmuş; x △ x işlemini yapmamış.','dikkat'),(8,'x △ x’i 3x − x − 2 yazmış; +2 sabit terimdir.','islem'),(10,'6 △ x = 18 − x − 2 yazıp x = 4 bulmuş; x △ x = 3 × 4 − 4 + 2 = 10.','islem'),(17,'x △ x’te −x terimini unutup 3x + 2 hesaplamış.','dikkat')],
 istenen='x △ x işleminin sonucu.',
 ip=['Her iki △ işlemini tanıma göre yaz: ilk sayı 3 ile çarpılır, ikinci sayı çıkarılır.'],
 bilgi=[TANIM],
 ad=[A('İşlemleri yaz','Sol: a = x, b = 2. Sağ: a = 6, b = x.','x △ 2 = 3x − 2 + 2 = 3x · 6 △ x = 18 − x + 2 = 20 − x'),A('x’i bul','İki yanı eşitle.','3x = 20 − x → x = 5'),A('x △ x’i hesapla','a = b = 5.','3 × 5 − 5 + 2 = 12')],
 puf='Tanımlı işlemde sayıları kuraldaki yerlerine koy; sıra değişirse sonuç da değişir.')

# ---------- 15 orta · makine ----------
m1=lambda n:2*n+3; m2=lambda n:3*n-5; x_=lin(lambda x:m2(m1(x))-40); assert x_==6 and m1(6)==15
assert Fr(40-3,2)==Fr(37,2) and lin(lambda x:3*(2*x+3-5)-40+0)!=6 and lin(lambda x:3*(2*x)+3-5-40)==7 and 2*6==12
mk(P,'0015',tipId='dkb-islem',tip='Tanımlı işlem, makine, işlem hatası',z='orta',alt='Makine Sorusu',kaz='Ardışık iki makinenin kuralını birleştirip çıktıdan girdiyi bulur.',kalip='yeni nesil',adim=3,
 kart='K-DNKB-07 (makine) · iki makine, çıktıdan girdi',
 metin='Birinci makine girdiği sayıyı 2 ile çarpıp 3 ekler.\nİkinci makine girdiği sayıyı 3 ile çarpıp 5 çıkarır.\nBir x sayısı önce birinci, çıkan sonuç ikinci makineye girildiğinde son çıktı 40 oluyor.\nBuna göre x kaçtır?',
 dogru=6,yan=[(7,'3(2x + 3) − 5’te 3’ü yalnız 2x ile çarpıp 6x + 3 − 5 yazmış.','bilgi'),(12,'2x = 12’de 2’ye bölmeyi unutmuş.','islem'),(15,'Birinci makinenin çıktısını (15) x sanmış.','dikkat'),(Fr(37,2),'Yalnız birinci makineyi geri alıp 40’tan (40 − 3) ÷ 2 hesaplamış.','dikkat')],
 istenen='Girilen x sayısı.',
 ip=['Birinci makinenin çıktısını 2x + 3 olarak yaz; bu ifade ikinci makineye girer.'],
 bilgi=[MAKINE],
 ad=[A('Çıktıyı yaz','Birinci makine: 2x + 3. İkinci makine bunu 3 ile çarpıp 5 çıkarır.','3(2x + 3) − 5 = 40'),A('Sadeleştir','Önce 5’i karşıya geçir.','3(2x + 3) = 45 → 2x + 3 = 15'),A('x’i bul','Ters işlemlerle.','2x = 12 → x = 6')],
 puf='İç içe makinelerde çıktıyı ifade olarak ikinci makineye ver; sonra sondan başa ters işlem yap.')

# ---------- 16 orta · işlem hatası (dağılma) ----------
yan_=lin(lambda x:5*x-2-(3*x+8)); dog_=lin(lambda x:5*(x-2)-(3*x+8)); assert (yan_,dog_)==(5,9) and dog_-yan_==4 and yan_-dog_==-4 and dog_+yan_==14 and 2*dog_==18
mk(P,'0016',tipId='dkb-islem',tip='Tanımlı işlem, makine, işlem hatası',z='orta',alt='İşlem Hatası',kaz='Öğrencinin dağılma hatasını bulup doğru çözümle hatalı çözümü karşılaştırır.',kalip='hikâyeli',adim=3,
 kart='K-DNKB-07 (işlem hatası) · parantez açarken eksik çarpma',
 metin='Ayşe,\n5(x − 2) = 3x + 8\ndenklemini çözerken 5’i yalnız x ile çarpıp −2 ile çarpmayı unutuyor ve bu yüzden hatalı bir çözüm buluyor.\nBuna göre doğru çözümün, Ayşe’nin bulduğu hatalı çözümden farkı kaçtır?',
 dogru=4,yan=[(18,'Doğru denklemde 2x = 18’i 2’ye bölmeden yazmış.','islem'),(5,'Yalnız Ayşe’nin hatalı çözümünü bulup durmuş.','dikkat'),(9,'Yalnız doğru çözümü bulup farkı almamış.','dikkat'),(14,'İki çözümü toplamış (5 + 9).','dikkat')],
 istenen='Doğru çözüm − hatalı çözüm.',
 ip=['Önce Ayşe’nin hatalı denklemini yaz ve çöz; sonra doğru denklemi çöz.'],
 bilgi=[DAG],
 ad=[A('Hatalı çözüm','5x − 2 = 3x + 8.','2x = 10 → x = 5'),A('Doğru çözüm','5x − 10 = 3x + 8.','2x = 18 → x = 9'),A('Farkı al','Doğru çözümden hatalı çözümü çıkar.','9 − 5 = 4')],
 puf='Hatalı çözümü de kuralıyla yeniden kur; iki çözümü ayrı ayrı bulduktan sonra istenen işlemi yap.')

# ---------- 17 orta · sistem sonsuz çözüm ----------
sol=[(x,y) for x in range(-6,7) for y in range(-6,7) if 2*x+3*y==7 and 4*x+6*y==14]
assert all(4*x+6*y==14 for x,y in sol) and len(sol)>1
assert 6+14==20 and 6+7==13 and 3+14==17 and 12+28==40
mk(P,'0017',tipId='dkb-kume',tip='Çözüm kümesi boş / sonsuz ve parametre',z='orta',alt='Sistemde Sonsuz Çözüm',kaz='İki bilinmeyenli sistemin sonsuz çözümlü olması koşulundan parametreleri bulur.',kalip='düz',adim=3,
 kart='K-DNKB-02 (çözüm kümesi, parametre) · sistemde sonsuz çözüm',
 metin='a ve b gerçel sayılardır.\n2x + 3y = 7\n4x + ay = b\ndenklem sisteminin çözüm kümesi sonsuz elemanlı olduğuna göre a + b toplamı kaçtır?',
 dogru=20,yan=[(40,'İkinci denklemi birincinin 4 katı sanmış: a = 12, b = 28.','bilgi'),(13,'b’yi bulurken 7’yi çarpmamış: b = 7 yazmış.','islem'),(14,'Yalnız b’yi bulmuş.','dikkat'),(17,'a’yı bulurken 3’ü 2 ile çarpmayıp a = 3 yazmış.','bilgi')],
 istenen='a + b toplamı.',
 ip=['İkinci denklemin x’li terimi birincininkinden nasıl elde edilir? Diğer terimler de aynı değişimi yaşamalı mı?'],
 bilgi=[SSON],
 ad=[A('Katı bul','x’in katsayısı 2’den 4’e çıkıyor.','İkinci denklem = 2 × birinci'),A('a ve b’yi bul','Diğer terimleri 2 ile çarp.','a = 2 × 3 = 6 · b = 2 × 7 = 14'),A('Topla','İstenen toplam.','6 + 14 = 20')],
 puf='Sistem sonsuz çözümlüyse iki denklem aynı doğrudur: biri diğerinin katıdır.')

# ---------- 18 zor · paydalı karmaşık ----------
f=lambda x:Fr(2*x-1,3)-Fr(x+4,6)-Fr(3*x-10,4); assert lin(f)==6
assert lin(lambda x:4*(2*x-1)-2*(x+4)-3*(3*x-10)+0)==6
assert lin(lambda x:8*x-1-2*(x+4)-3*(3*x-10))==7 and Fr(-18,3)==-6 and Fr(18,1)==18 and Fr(18,2)==9
mk(P,'0018',tipId='dkb-birinci',tip='Birinci dereceden denklem: paydalı ve parantezli',z='zor',alt='Paydalı Denklem',kaz='Üç farklı paydalı terimi EKOK ile eşitleyip parantezleri açarak denklemi çözer.',kalip='düz',adim=5,
 kart='K-DNKB-01 (birinci dereceden denklem) · üç farklı payda, eksi işaretli kesir',
 metin='(2x − 1)/3 − (x + 4)/6 = (3x − 10)/4\ndenklemini sağlayan x değeri kaçtır?',
 dogru=6,yan=[(-6,'6x − 12 = 9x − 30’da 3x = −18 yazıp x = −6 bulmuş.','islem'),(7,'4(2x − 1)’i 8x − 1 açmış; 4, −1 ile de çarpılmalı.','bilgi'),(9,'3x = 18’i 2’ye bölmüş; x’in katsayısı 3’tür.','islem'),(18,'3x = 18’de 3’e bölmeyi unutmuş.','islem')],
 istenen='Denklemi sağlayan x değeri.',
 ip=['Paydaların en küçük ortak katıyla her kesri çarp; ikinci kesrin önündeki eksi işaretini koru.'],
 bilgi=[PAYDA,DAG],
 ad=[A('EKOK’u bul','3, 6 ve 4’ün EKOK’u 12.','12 ile çarp'),A('Kesirleri kaldır','Her payı ilgili çarpanla çarp.','4(2x − 1) − 2(x + 4) = 3(3x − 10)'),A('Parantezleri aç','Eksi işaretini dağıt.','8x − 4 − 2x − 8 = 9x − 30'),A('Sadeleştir','Benzer terimleri topla.','6x − 12 = 9x − 30'),A('x’i bul','x’leri tek yana topla.','−3x = −18 → x = 6')],
 puf='Eksi işaretli kesirde payın tamamı parantez içinde düşünülmeli; EKOK ile çarpınca eksi işaret parantezin önünde kalır.')

# ---------- 19 zor · (a²−1)x = a²+3a+2 ----------
def tur19(a):
    c=a*a-1; d=a*a+3*a+2
    return 'tek' if c!=0 else ('R' if d==0 else 'bos')
RS=[a for a in range(-10,11) if tur19(a)=='R']; BS=[a for a in range(-10,11) if tur19(a)=='bos']
assert RS==[-1] and BS==[1]; k_,m_=RS[0],BS[0]; assert k_-2*m_==-3 and m_-2*k_==3 and k_-m_==-2 and k_*m_==-1 and k_+2*m_==1
mk(P,'0019',tipId='dkb-kume',tip='Çözüm kümesi boş / sonsuz ve parametre',z='zor',alt='Boş ve Sonsuz Çözüm',kaz='a² − 1 katsayılı denklemde çözüm kümesinin ℝ ve boş küme olduğu a değerlerini ayrı ayrı bulur.',kalip='düz',adim=4,
 kart='K-DNKB-02 (çözüm kümesi, parametre) · katsayı sıfırken sabite bakma, iki ayrı durum',
 metin='a bir gerçel sayı olmak üzere, x’e bağlı\n(a² − 1)x = a² + 3a + 2\ndenkleminin çözüm kümesi, a = k için gerçel sayıların tamamı, a = m için boş kümedir.\nBuna göre k − 2m kaçtır?',
 dogru=-3,yan=[(-2,'2m yerine m’yi çıkarıp k − m hesaplamış.','dikkat'),(-1,'k − 2m yerine k · m çarpımını hesaplamış: (−1) × 1 = −1.','dikkat'),(1,'k − 2m yerine k + 2m yazmış: −1 + 2 = 1.','islem'),(3,'k ile m’yi karıştırıp m − 2k hesaplamış.','dikkat')],
 istenen='k − 2m değeri.',
 ip=['a² − 1 hangi a değerlerinde sıfır olur? Bu değerleri denkleme geri koyup ne olduğuna bak.'],
 bilgi=[KUME],
 ad=[A('Katsayıyı sıfırla','a² − 1 = 0 için iki aday vardır.','a = 1 ya da a = −1'),A('a = 1 için bak','Sağ taraf 1 + 3 + 2 = 6.','0·x = 6 → boş küme, m = 1'),A('a = −1 için bak','Sağ taraf 1 − 3 + 2 = 0.','0·x = 0 → ℝ, k = −1'),A('İfadeyi hesapla','k − 2m.','−1 − 2 × 1 = −3')],
 puf='Katsayı sıfır olduğunda çözüm sayısını sağ taraf belirler: sağ taraf 0 ise sonsuz, 0’dan farklıysa yok.')

# ---------- 20 zor · tanımlı işlem iç içe ----------
o2=lambda a,b:2*a+b-3
x_=lin(lambda x:o2(o2(x,2),x)-15); assert x_==4
assert lin(lambda x:o2(2*x+2,x)-15)==Fr(14,5) and lin(lambda x:(4*x-1)+x-3-15)==Fr(19,5) and 5*3==15 and 5*2==10
mk(P,'0020',tipId='dkb-islem',tip='Tanımlı işlem, makine, işlem hatası',z='zor',alt='Tanımlı İşlem',kaz='İç içe tanımlı işlemden kurulan birinci dereceden denklemi çözer.',kalip='düz',adim=4,
 kart='K-DNKB-07 (tanımlı işlem) · iç içe işlem, parantezli denklem',
 metin='Gerçel sayılar kümesinde bir ⊕ işlemi\na ⊕ b = 2a + b − 3\nbiçiminde tanımlanıyor.\n(x ⊕ 2) ⊕ x = 15\neşitliğini sağlayan x değeri kaçtır?',
 dogru=4,yan=[(2,'5x − 5 = 15’i 5x = 10 yazıp x = 2 bulmuş.','islem'),(Fr(14,5),'x ⊕ 2’yi 2x + 2 yazmış; −3’ü unutmuş.','dikkat'),(3,'5x = 15 yazıp −5’i hesaba katmamış.','islem'),(Fr(19,5),'2(2x − 1)’i 4x − 1 açmış; 2, −1 ile de çarpılmalı.','bilgi')],
 istenen='x değeri.',
 ip=['Önce parantez içindeki x ⊕ 2’yi x cinsinden yaz; sonra bu ifadeyi ilk sayı yerine koy.'],
 bilgi=[TANIM],
 ad=[A('İç işlemi yap','a = x, b = 2.','x ⊕ 2 = 2x + 2 − 3 = 2x − 1'),A('Dış işlemi yaz','a = 2x − 1, b = x.','(2x − 1) ⊕ x = 2(2x − 1) + x − 3'),A('Aç ve topla','Parantezi aç.','4x − 2 + x − 3 = 5x − 5'),A('Çöz','Denklemi kur.','5x − 5 = 15 → x = 4')],
 puf='İç içe tanımlı işlemde önce parantezi bir ifadeye çevir, sonra onu dış işlemde ilgili yere koy.')

# ---------- 21 zor · makine iki geçiş ----------
mf=lambda n:3*n-2; x_=lin(lambda x:mf(mf(x))-(5*x+4)); assert x_==3
assert lin(lambda x:mf(x)-(5*x+4))==-3 and lin(lambda x:9*x-8-(5*x+4)+0)==3 and lin(lambda x:9*x-8-5*x-4)==3
assert Fr(4-8,4)==-1 and lin(lambda x:3*(3*x-2)-2-0-(5*x+4)+0)==3 and lin(lambda x:9*x-4-(5*x+4))==2 and 12==Fr(12,1)
mk(P,'0021',tipId='dkb-islem',tip='Tanımlı işlem, makine, işlem hatası',z='zor',alt='Makine Sorusu',kaz='Aynı makineden iki kez geçen sayıyı ifade olarak yazıp denklemi çözer.',kalip='yeni nesil',adim=4,
 kart='K-DNKB-07 (makine) · aynı makineden iki geçiş, iki yanda x',
 metin='Bir makine girdiği sayıyı 3 ile çarpıp 2 çıkarmaktadır.\nMakineye bir x sayısı girilmiş, çıkan sonuç aynı makineye yeniden girilmiştir. Bu ikinci çıktı, x’in 5 katının 4 fazlasına eşit olmuştur.\nBuna göre x kaçtır?',
 dogru=3,yan=[(-3,'Makineden yalnız bir kez geçirip 3x − 2 = 5x + 4 yazmış.','dikkat'),(-1,'9x − 8 = 5x + 4’te 4x = 4 − 8 = −4 yazıp x = −1 bulmuş.','islem'),(2,'3(3x − 2) − 2’yi 9x − 2 − 2 yazmış; 3, −2 ile de çarpılmalı.','bilgi'),(12,'4x = 12’de 4’e bölmeyi unutmuş.','islem')],
 istenen='x değeri.',
 ip=['İlk çıktıyı x cinsinden yaz; bu ifadeye makinenin kuralını bir kez daha uygula.'],
 bilgi=[MAKINE,DAG],
 ad=[A('İlk çıktı','x girince 3x − 2 çıkar.','3x − 2'),A('İkinci çıktı','3x − 2 ifadesini yeniden makineye ver.','3(3x − 2) − 2 = 9x − 8'),A('Denklemi kur','İkinci çıktıyı 5x + 4’e eşitle.','9x − 8 = 5x + 4'),A('Çöz','x’leri sola topla.','4x = 12 → x = 3')],
 puf='Makineyi iki kez uygulamak, kuralı ifadenin tamamına ikinci kez uygulamaktır; parantezi unutma.')

# ---------- 22 zor · pizza sistem ----------
p_,i_=90,50; assert 2*p_+3*i_==330 and 3*p_+i_==320 and 4*p_+5*i_==610
assert 5*p_+4*i_==650 and 4*p_+4*i_==560 and Fr(330-90,3)==80 and 4*90+5*80==760 and 4*90+5*150==1110
sol=[(p,i) for p in range(0,300) for i in range(0,300) if 2*p+3*i==330 and 3*p+i==320]; assert sol==[(90,50)]
mk(P,'0022',tipId='dkb-sistem',tip='İki bilinmeyenli denklem sistemi',z='orta',alt='Sistem Kurma',kaz='İki tür ürünün fiyatından sistem kurup yok etme yöntemiyle istenen toplam tutarı bulur.',kalip='hikâyeli',adim=5,
 kart='K-DNKB-03 (iki bilinmeyenli sistem) · fiyat sistemi, farklı adette sipariş',
 metin='Bir lokantada pizzaların tümü aynı fiyatlı, içeceklerin tümü aynı fiyatlıdır.\n2 pizza ile 3 içecek 330 TL, 3 pizza ile 1 içecek 320 TL’dir.\nBuna göre 4 pizza ile 5 içeceğin toplam fiyatı kaç TL’dir?',
 dogru=610,yan=[(560,'5 içecek yerine 4 içecek (4 × 90 + 4 × 50) hesaplamış.','dikkat'),(650,'İki denklemi toplayıp 5 pizza + 4 içecek = 650’yi istenen sipariş sanmış.','dikkat'),(760,'3i = 330 − 90 = 240 yazıp i = 80 bulmuş (2p yerine p çıkarmış); 4 × 90 + 5 × 80 = 760.','islem'),(1110,'3i = 150’yi 3’e bölmeden i = 150 almış; 4 × 90 + 5 × 150 = 1110.','islem')],
 istenen='4 pizza ile 5 içeceğin toplam fiyatı (TL).',
 ip=['İçecek sayılarını eşitlemek için hangi denklemi kaç ile çarpabilirsin?'],
 bilgi=[SIS],
 ad=[A('Sistemi kur','Pizza p, içecek i olsun.','2p + 3i = 330 · 3p + i = 320'),A('i’yi yok et','İkinci denklemi 3 ile çarp.','9p + 3i = 960'),A('Çıkar','Birinci denklemi çıkar.','7p = 630 → p = 90'),A('i’yi bul','Birinci denklemde yerine yaz.','180 + 3i = 330 → i = 50'),A('İstenen toplam','4 pizza + 5 içecek.','4 × 90 + 5 × 50 = 360 + 250 = 610 TL')],
 puf='Fiyat sistemlerinde önce her ürünün fiyatını bul, sonra sorulan siparişi hesapla.')

# ---------- 23 zor · işlem hatası (EKOK) ----------
hat=lin(lambda x:2*(2*x+1)-3*(x-2)-3); dog=lin(lambda x:2*(2*x+1)-3*(x-2)-18)
assert Fr(2*dog+1,3)-Fr(dog-2,2)==3 and (hat,dog)==(-5,10) and Fr(dog,hat)==-2 and Fr(hat,dog)==Fr(-1,2) and dog-hat==15 and dog+hat==5 and abs(Fr(dog,hat))==2
mk(P,'0023',tipId='dkb-islem',tip='Tanımlı işlem, makine, işlem hatası',z='zor',alt='İşlem Hatası',kaz='Denklemin sağ tarafını EKOK ile çarpmayı unutan öğrencinin hatalı ve doğru çözümünü karşılaştırır.',kalip='hikâyeli',adim=4,
 kart='K-DNKB-07 (işlem hatası) · EKOK ile çarparken sağ tarafı atlama',
 metin='Mert,\n(2x + 1)/3 − (x − 2)/2 = 3\ndenklemini çözerken paydaları eşitlemek için iki tarafı 6 ile çarpıyor; ancak sağ taraftaki 3’ü 6 ile çarpmayı unutuyor ve hatalı bir çözüm buluyor.\nBuna göre doğru çözüm, Mert’in bulduğu hatalı çözümün kaç katıdır?',
 dogru=-2,yan=[(Fr(-1,2),'Oranı ters kurup hatalı çözümü doğru çözüme bölmüş.','dikkat'),(2,'Katı −2 yerine işaretsiz (2) yazmış; çözümler zıt işaretlidir.','dikkat'),(5,'Doğru ve hatalı çözümü toplamış (10 + (−5)).','dikkat'),(15,'Kat yerine farkı (10 − (−5)) hesaplamış.','dikkat')],
 istenen='Doğru çözüm ÷ hatalı çözüm.',
 ip=['Önce Mert’in hatalı denklemini kurup çöz; sonra sağ taraf da 6 ile çarpılmış doğru denklemi çöz.'],
 bilgi=[PAYDA,DENK],
 ad=[A('Hatalı denklem','Sağ taraf 3 kalmış.','2(2x + 1) − 3(x − 2) = 3 → x + 8 = 3'),A('Hatalı çözüm','x’i bul.','x = −5'),A('Doğru denklem','Sağ taraf 3 × 6 = 18 olmalı.','x + 8 = 18 → x = 10'),A('Oranla','Doğru çözümü hatalı çözüme böl.','10 ÷ (−5) = −2')],
 puf='Hatalı çözümü ve doğru çözümü ayrı ayrı bul; soru kat, fark ya da toplam istiyorsa ancak ondan sonra işlem yap.')

# ---------- 24 orta · öncüllü, oranlı ----------
from fractions import Fraction as Fr2
# (x+y)/(x-y)=5/3 -> x=4y (y≠0)
assert all(Fr(x+y,x-y)==Fr(5,3)==Fr(5,3) for y in range(1,9) for x in [4*y])
sols=[(x,y) for x in range(-40,41) for y in range(-40,41) if x!=y and 3*(x+y)==5*(x-y)]
assert all(x==4*y for x,y in sols)
I_=all(x==4*y for x,y in sols)
II_=all((x+y)%5==0 for x,y in sols if x>0 and y>0)
s36=[(x,y) for x,y in sols if x*y==36]; assert sorted(s36)==[(-12,-3),(12,3)] and {x+y for x,y in s36}=={15,-15}
III_=all(x+y==15 for x,y in s36)
assert (I_,II_,III_)==(True,True,False)
mk(P,'0024',tipId='dkb-oran',tip='Oranlı denklem',z='orta',alt='Oranlı Denklem Yorumu',kaz='Oranlı denklemi sadeleştirip x ile y arasındaki ilişkiyi öncüllerde sınar.',kalip='öncüllü',adim=4,
 kart='K-DNKB-05 (oranlı denklem) · öncüllü: x = 4y ilişkisi ve işaret tuzağı',
 metin='x ve y, x ≠ y olan gerçel sayılardır.\n(x + y)/(x − y) = 5/3\nolduğuna göre,\nI. x = 4y’dir.\nII. x ve y pozitif tam sayı ise x + y toplamı 5’in katıdır.\nIII. x · y = 36 ise x + y = 15’tir.\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve II',sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 yan=[('Yalnız I','II’de x = 4y yazınca x + y = 5y olduğunu görmemiş.','bilgi'),('Yalnız II','I’i sınamamış; içler dışlar çarpımından x = 4y çıktığını görmemiş.','dikkat'),('I ve III','III’te y = 3, x = 12 bulup y = −3, x = −12 durumunu unutmuş; o durumda x + y = −15’tir.','dikkat'),('II ve III','I’i yanlış sanmış; III’te de y’nin negatif değerini unutmuş.','bilgi')],
 istenen='Kesinlikle doğru olan öncüllerin hangileri olduğu.',
 ip=['İçler dışlar çarpımıyla x ile y arasındaki ilişkiyi bul; her öncülü bu ilişkiyle sına.'],
 bilgi=[ORAN],
 ad=[A('İçler dışlar','Paydalar sıfırdan farklı (x ≠ y).','3(x + y) = 5(x − y)'),A('İlişkiyi bul','Parantezleri aç, x ve y’yi ayır.','3x + 3y = 5x − 5y → 8y = 2x → x = 4y'),A('I ve II’yi sına','I doğru. II’de x + y = 5y, y tam sayı olduğundan 5’in katı.','I doğru · II doğru'),A('III’ü sına','x · y = 4y² = 36 → y = 3 ya da y = −3. İkincisinde x + y = −15.','III kesin değil')],
 puf='Oranlı denklemden çıkan ilişkiyi öncüllere yerleştir; kare alınan durumlarda negatif kökü de düşün.')

bitir(P,'denklemiki',UK)
