"""TYT Türkçe · Anlatım Bozukluğu: 4 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (anlatım bozuklukları) ve MEB Türk Dili ve Edebiyatı müfredatı'
KARTLAR={
 'K-AB-01':dict(alt='Gereksiz Sözcük Kullanımı',fikir='Anlamca aynı olan sözcüklerin gereksiz yinelendiği cümleyi bulmak.',tuzak='Vurgu amaçlı doğal tekrarı bozukluk sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='anl-gereksiz',kaynak=KY),
 'K-AB-02':dict(alt='Özne–Yüklem Uyumu',fikir='Öznenin kişi ve sayısı ile yüklemin kişi ve sayısının uyuşmadığı cümleyi bulmak.',tuzak='Yüklemi bulmadan öznenin tek görünen biçimine bakmak.',zorluk='orta',kalip='düz',adim=3,tipId='anl-ozne',kaynak=KY),
 'K-AB-03':dict(alt='Neden–Sonuç ve Mantık',fikir='Neden-sonuç ilişkisi mantıkla bağdaşmayan cümleyi bulmak.',tuzak='Bağlaç ve ekleri doğru diye cümleyi doğru sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='anl-mantik',kaynak=KY),
 'K-AB-04':dict(alt='Bozukluğu Olmayan Cümle',fikir='Beş cümlenin dördündeki farklı türde bozukluğu görüp bozukluğu olmayanı bulmak.',tuzak='Bozuklukların türünü tanıyamayıp kalanı doğru sanmak.',zorluk='zor',kalip='düz',adim=4,tipId='anl-karma',kaynak=KY),
}
TIPLER={'anl-gereksiz':'Gereksiz sözcük kullanımı','anl-ozne':'Özne–yüklem uyumsuzluğu','anl-mantik':'Neden–sonuç ve mantık','anl-karma':'Bozukluğu olmayan cümle'}
Q=kur('anlatimboz','Anlatım Bozukluğu','tr|Anlatım Bozukluğu',KARTLAR,TIPLER); Q.n=4
B_GS=B('Gereksiz sözcük','anlamca aynı olan sözcüklerin birlikte kullanılması anlatım bozukluğudur (bir daha tekrar, yaklaşık olarak tahminen). Kullanılan sözcüklerden biri yetmektedir')
B_OY=B('Özne–yüklem uyumu','özne ile yüklem kişi ve sayı bakımından uyumlu olmalıdır. Öğrenciler geldi (3. çoğul + 3. çoğul) doğru; Öğrenciler geldim (3. çoğul + 1. tekil) bozuktur')
B_MN=B('Neden–sonuç / mantık','cümledeki neden ile sonuç anlamca birbirini karşılamalıdır. “Hava soğuk olduğu için kalın giyindik” doğru; “Hava sıcak olduğu için kalın giyindik” mantık bakımından bozuktur')
B_KR=B('Bozukluk türleri','gereksiz sözcük (bir daha tekrar) · özne–yüklem uyumsuzluğu (öğrenciler geldim) · mantık hatası (sıcak olduğu için kalın giyindik) · ek eksikliği (hem öğretmeni hem öğrencilerle: ortak ek her sözcüğe uymalı)')

# 0001 gereksiz sözcük · kolay · D
soru(Q,'0001','K-AB-01','kolay','Anlamca aynı sözcüklerin gereksiz yinelendiği cümleyi bulur.',2,
 'Aşağıdaki cümlelerin hangisinde anlamca aynı olan sözcüklerin gereksiz kullanımından kaynaklanan bir anlatım bozukluğu vardır?',
 [('Komşumuz, bahçedeki ağaçları sonbaharda budadı.','dogru','Anlamca tekrar eden sözcük yoktur; cümle doğrudur.','bilgi'),
  ('Öğretmenimiz, ödevlerin cuma gününe kadar getirilmesini istedi.','dogru','Gereksiz sözcük yoktur; anlatım doğrudur.','bilgi'),
  ('Çocuklar, yağmur dinince sokakta top oynamaya başladı.','dogru','Anlamca tekrar yoktur; anlatım doğrudur.','dikkat'),
  ('Kitabı bitirdikten sonra onu bir daha tekrar okumak istedi.','bozuk','',''),
  ('Kütüphaneden aldığım roman, beklediğimden çok daha akıcıydı.','dogru','“Çok daha” karşılaştırmayı pekiştirir; aynı anlamlı gereksiz sözcük yoktur.','dikkat')],
 'D',lambda t:t=='bozuk','Gereksiz sözcük nedeniyle bozuk olan cümle.',
 '“Bir daha” ve “tekrar” gibi aynı anlamı veren sözcük çiftlerini ara.',[B_GS],
 [AD('Bozukluk türünü hatırla','Aynı anlamı veren iki sözcük birlikte kullanılırsa gereksiz yineleme olur.','bir daha = tekrar'),AD('Şıkları tara','A, B, C ve E’de aynı anlamı taşıyan sözcük çifti yok; her sözcük cümleye yeni bir bilgi katıyor.','A, B, C, E: doğru'),AD('Bozuk cümleyi seç','D’de “bir daha” ve “tekrar” aynı anlamdadır; birini çıkarınca cümle düzelir.','D: bozuk')],
 'Anlam bakımından yinelenen sözcükleri ararken birini çıkar; cümle hâlâ aynı anlamı veriyorsa yineleme vardır.')

# 0002 özne yüklem · orta · B
soru(Q,'0002','K-AB-02','orta','Özne ile yüklemin kişi ve sayı bakımından uyuşmadığı cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisinde özne–yüklem uyumsuzluğundan kaynaklanan bir anlatım bozukluğu vardır?',
 [('Arkadaşlarım hafta sonu şehrin eski müzesini gezdi.','dogru','Özne “arkadaşlarım” (3. kişi), yüklem “gezdi” (3. kişi); uyumludur.','bilgi'),
  ('Misafirler yemekten sonra çaylarını içip bizimle vedalaştım.','bozuk','',''),
  ('Hepimiz sınav sonuçlarını sabırsızlıkla merak ediyorduk.','dogru','Özne “hepimiz” (1. çoğul), yüklem “ediyorduk” (1. çoğul); uyumludur.','dikkat'),
  ('Sizler bu projede gece gündüz çok emek harcadınız.','dogru','Özne “sizler” (2. çoğul), yüklem “harcadınız” (2. çoğul); uyumludur.','dikkat'),
  ('Çocuklar bahçede akşama kadar neşeyle saklambaç oynadı.','dogru','Özne “çocuklar”, yüklem “oynadı”: çoğul özneye tekil yüklem Türkçede uyumsuzluk sayılmaz.','bilgi')],
 'B',lambda t:t=='bozuk','Özne–yüklem uyumsuzluğu olan cümle.',
 'Her cümlede öznenin kişisini ve yüklemin kişi ekini yan yana yaz.',[B_OY],
 [AD('Ölçütü hatırla','Özne ile yüklemin kişisi uyuşmalı: biz → -ık, siz → -ınız, onlar → -dı.','özne ↔ yüklem uyumu'),AD('Şıkları çözümle','A: arkadaşlarım–gezdi, C: hepimiz–ediyorduk, D: sizler–harcadınız, E: çocuklar–oynadı. Hepsi uyumlu.','A, C, D, E: uyumlu'),AD('Uyumsuzluğu bul','B’de özne “misafirler” (3. çoğul); yüklem “vedalaştım” 1. tekil kişi eki alıyor.','B: bozuk')],
 'Önce özneyi, sonra yüklemin kişi ekini bul; ikisinin kişisini karşılaştır.')

# 0003 mantık · orta · E
soru(Q,'0003','K-AB-03','orta','Neden–sonuç ilişkisi mantıkla bağdaşmayan cümleyi bulur.',3,
 'Aşağıdaki cümlelerin hangisinde neden–sonuç ilişkisinden kaynaklanan bir anlatım bozukluğu vardır?',
 [('Yeni açılan metro hattı sayesinde şehir içi ulaşım kolaylaştı.','dogru','Metro hattı ulaşımı kolaylaştırır; neden ile sonuç tutarlıdır.','bilgi'),
  ('Sabah erken kalktığı için derse geç kalmadı.','dogru','Erken kalkmak, derse zamanında yetişmenin nedenidir; mantık tutarlıdır.','bilgi'),
  ('Yeterince çalışmadığı hâlde sınavdan yüksek not aldı.','dogru','“Hâlde” karşıtlık bildirir; çalışmama ile yüksek not arasındaki karşıtlık doğru kurulmuştur.','dikkat'),
  ('Yolların kapanması nedeniyle seferler iptal edildi.','dogru','Yolların kapanması seferlerin iptaline yol açar; mantık tutarlıdır.','dikkat'),
  ('Sürekli yağış yüzünden barajlardaki su seviyesi düştü.','bozuk','','')],
 'E',lambda t:t=='bozuk','Neden–sonuç ilişkisi mantıksız olan cümle.',
 'Her cümlede nedenin sonucu gerçekten doğurup doğurmadığını sor.',[B_MN],
 [AD('Ölçütü hatırla','Neden ile sonuç birbirini karşılamalıdır; neden sonucu doğurmalıdır.','neden → sonuç'),AD('Şıkları sına','Metro hattı ulaşımı kolaylaştırır. Erken kalkan geç kalmaz. Yolların kapanması seferleri durdurur. C’deki karşıtlık da doğrudur.','A, B, C, D: tutarlı'),AD('Mantıksız olanı bul','Sürekli yağış barajlardaki suyu azaltmaz, artırır; “yüzünden düştü” mantıkla bağdaşmaz.','E: bozuk')],
 'Neden-sonuç cümlelerinde nedeni ve sonucu ayrı ayrı yaz, sonra nedenin sonucu doğurup doğurmadığına bak.')

# 0004 bozukluğu olmayan · zor · A
soru(Q,'0004','K-AB-04','zor','Farklı türde bozukluk içeren cümleler arasından bozukluğu olmayanı bulur.',4,
 'Aşağıdaki cümlelerin hangisinde anlatım bozukluğu yoktur?',
 [('Akşam yağan sağanak yüzünden şehrin bazı yolları ulaşıma kapandı.','dogru','',''),
  ('Müdür, hem öğretmenleri hem öğrencilerle uzun uzun konuştu.','bozuk','“Konuşmak” fiili “-le” alır; ortak ek “öğretmenleri” sözcüğüne uymaz (ek eksikliği). “Öğretmenlerle ve öğrencilerle” olmalıdır.','bilgi'),
  ('Sınıf başkanı seçilen Zeynep, bütün arkadaşlarına teşekkür ettik.','bozuk','Özne “Zeynep” 3. tekil, yüklem “ettik” 1. çoğul: özne–yüklem uyumsuzluğu vardır.','bilgi'),
  ('Toplantıya yaklaşık olarak tahminen elli kişi katıldı.','bozuk','“Yaklaşık olarak” ve “tahminen” aynı anlamdadır; gereksiz sözcük kullanımı vardır.','dikkat'),
  ('Hava çok sıcak olduğu için kalın montlarımızı giyip yola çıktık.','bozuk','Sıcak havanın sonucu kalın giyinmek değildir; neden-sonuç mantığı bozuktur.','dikkat')],
 'A',lambda t:t=='dogru','Anlatım bozukluğu bulunmayan cümle.',
 'Dört cümlede farklı türde bozukluk var: ek, özne–yüklem, yineleme ve mantık.',[B_KR],
 [AD('Tür listesini yap','Aranacak bozukluklar: ek eksikliği, özne–yüklem uyumsuzluğu, gereksiz sözcük, mantık hatası.','4 tür'),AD('Bozuk cümleleri ele','B’de ortak ek eksik, C’de Zeynep–ettik uyumsuz, D’de yaklaşık olarak–tahminen yinelemesi, E’de sıcak–kalın mont çelişkisi var.','B, C, D, E: bozuk'),AD('Temiz olanı doğrula','A’da yağış nedeni ile yolların kapanması sonucu tutarlı; özne “yollar”, yüklem “kapandı” uyumlu; gereksiz sözcük yok.','A: doğru')],
 '“Bozukluk yoktur” sorularında önce bozuk olanları türleriyle birlikte etiketle; geriye kalan temizdir.')
bitir(Q)
