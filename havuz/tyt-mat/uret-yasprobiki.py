"""Yaş Problemleri · parti 2 (hafif mod): 19 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici kodla doğrulanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Yaş Problemleri'
UK='prob|Yaş Problemleri'
P=Parti('yasprobiki','Yaş Problemleri',UK)
FARK=B('Yaş farkı sabittir','İki kişi her yıl birer yaş büyür; aralarındaki fark hiç değişmez. Örnek: 10 ve 40 yaşındakilerin farkı 30’dur; 5 yıl sonra 15 ve 45 olurlar, fark yine 30’dur')
TOPL=B('Yaşlar toplamı','n kişinin yaşları toplamı, t yılda n × t kadar değişir. Örnek: 3 kişinin yaşları toplamı 90 ise 4 yıl sonra 90 + 3 × 4 = 102 olur')
ORAN=B('Oranı k ile yazmak','Yaşlar 2 : 7 oranındaysa yaşlar 2k ve 7k’dir; aralarındaki fark 5k olur. Örnek: fark 20 ise 5k = 20, k = 4 → yaşlar 8 ve 28')
ORT=B('Aritmetik ortalama','yaşlar toplamı ÷ kişi sayısı ortalamadır; toplam = ortalama × kişi sayısı. Örnek: 3 kişinin ortalaması 20 ise toplamları 60’tır')
YIL=B('Yıl ile yaş','Yaş = bulunulan yıl − doğum yılı. Örnek: 2000 doğumlu biri 2026’da 26 yaşındadır; doğum yılı küçük olan daha büyüktür')
ZAMAN=B('Geçmişe ve geleceğe gitmek','t yıl önce herkesin yaşından t çıkar, t yıl sonra herkesin yaşına t eklenir. Doğmamış biri yoksa hiçbir yaş negatif olamaz. Örnek: 12 yaşındaki biri 5 yıl önce 7 yaşındaydı')
KAYAN=B('“Ben senin yaşındayken” cümleleri','Yaş farkı d ise “ben senin yaşındayken” d yıl öncesidir, “sen benim yaşıma geldiğinde” d yıl sonrasıdır. Örnek: 30 ve 20 yaşındakiler için d = 10; 10 yıl önce 20 ve 10 yaşındaydılar')
AYRI=B('Herkes ayrı yaşlanır','1 baba ve 3 çocuğun yaşları toplamı karşılaştırılırken baba yılda 1, çocukların toplamı yılda 3 artar; fark yılda 2 değişir. Örnek: baba 50, çocuklar toplam 40 ise 5 yıl sonra 55 ve 55 olur')

KY='ÖSYM 2018–2026 TYT Matematik (yaş problemleri) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf'
kart('K-YASB-01','İki kişi: toplam, fark, oran','İki kişinin yaşları toplamı, farkı ya da oranı verilir; büyük ve küçük yaş toplam–fark ya da k oranıyla ayrı ayrı bulunur.','Farkı almadan toplamı ikiye bölmek; sorulan kişiyi karıştırmak; oranda k yerine parça sayısını yaş sanmak.','kolay','hikâyeli',2,'ysb-toplamfark','İki kişinin yaşları: toplam, fark, oran',KY)
kart('K-YASB-02','Yıl kaydırma ve oran değişimi','t yıl önce ya da sonra herkesin yaşı t değişir, yaş farkı sabit kalır; oran ve toplam bilgisiyle bugünkü yaşlar bulunur.','Yıl kaydırırken yalnız bir kişiyi kaydırmak; iki kişinin toplamında t yılı bir kez saymak.','orta','hikâyeli',3,'ysb-yilkaydir','Yıl kaydırma ve yaşlar oranının değişimi',KY)
kart('K-YASB-03','“Ben senin yaşındayken”','Yaş farkı kadar geriye ya da ileriye gitmek; farkı bilinmeyen alıp toplam bilgisiyle yaşlar çözülür.','Yaş farkının zamanla değiştiğini sanmak; geçmişte ve gelecekte yalnız bir kişiyi kaydırmak.','orta','hikâyeli',4,'ysb-benseninyas','“Ben senin yaşındayken” tipi sabit yaş farkı',KY)
kart('K-YASB-04','Aile ve yaş ortalaması','Üç ya da dört kişilik ailelerde toplam = ortalama × kişi sayısı ve geçmişte doğmamış kişilerin sayılmaması birlikte kullanılır.','Doğmamış çocuğu da sayıp ortalamaya yıl eklemek; ortalamayı toplam yerine doğrudan kaydırmak.','orta','hikâyeli',4,'ysb-aile','Üç ve dört kişilik aile, yaş ortalaması',KY)
kart('K-YASB-05','Doğum yılı ve takvim yılı','Doğum yılı, yaş ve yıl arasındaki yaş = yıl − doğum yılı ilişkisi; yıl dönümü ve mum sayısı gibi tanımlı kurallarla birlikte işlenir.','Yaşı doğum yılıyla karıştırmak; yıl yerine yaş farkını yıl sanmak.','orta','yeni nesil',3,'ysb-yilhesap','Doğum yılı, takvim yılı ve yıl dönümü',KY)
kart('K-YASB-06','Kaç yıl sonra eşitlenir','Her kişi ayrı yaşlanır: bir tarafta 1 kişi, diğer tarafta n kişi varsa fark yılda n − 1 değişir; tablo, ikiz ve öncüllü kurgularla.','Babanın yaşını sabit tutmak; farkı kişi sayısına bölmemek; “önce/sonra” yönünü karıştırmak.','zor','tablo',4,'ysb-esitlenme','Kaç yıl sonra eşitlenir: herkes ayrı yaşlanır',KY)

# ---------- 01 kolay · toplam-fark ----------
S,D=63,27; amca=(S+D)//2; emre=(S-D)//2
assert (amca,emre)==(45,18) and (S+D)%2==0 and amca-emre==D and amca+emre==S
assert [(a,b) for a in range(1,100) for b in range(1,a) if a+b==S and a-b==D]==[(45,18)]
mk(P,'0001',tipId='ysb-toplamfark',tip='İki kişinin yaşları: toplam, fark, oran',z='kolay',alt='Toplam ve Fark',kaz='İki kişinin yaşları toplamı ve farkından büyük olanın yaşını bulur.',kalip='hikâyeli',adim=2,
 kart='K-YASB-01 (iki kişi: toplam–fark) · Emre ve amcası',
 metin='Emre ile amcasının bugünkü yaşları toplamı 63, yaşları arasındaki fark 27’dir.\nBuna göre Emre’nin amcası bugün kaç yaşındadır?',
 dogru=amca,yan=[(emre,'Küçük yaşı (Emre’nin yaşını) bulup amcayı sormayı unutmuş.','dikkat'),(D,'Sorulan yaş yerine yaş farkını yazmış.','dikkat'),(Fr(S,2),'Toplamı ikiye bölüp ortalamayı yaş sanmış; farkı kullanmamış.','bilgi'),(S-D,'63 − 27 = 36’yı ikiye bölmeyi unutmuş (bu değer küçük yaşın iki katıdır).','islem')],
 istenen='Amcanın bugünkü yaşı.',
 ip=['Büyük yaşa b, küçük yaşa k de; b + k ve b − k ifadelerini alt alta yaz.'],
 bilgi=[FARK],
 ad=[A('Denklemleri yaz','Amca b, Emre k yaşında olsun.','b + k = 63 · b − k = 27'),A('Taraf tarafa topla','k’ler birbirini götürür.','2b = 90 → b = 45'),A('Kontrol','Emre’nin yaşı da toplamdan bulunur.','k = 63 − 45 = 18 · 45 − 18 = 27 ✓')],
 puf='Toplam ve fark verilince büyük yaş = (toplam + fark) ÷ 2, küçük yaş = (toplam − fark) ÷ 2’dir.')

# ---------- 02 kolay · oran ----------
fk=30; z=Fr(2*fk,5); an=Fr(7*fk,5); assert (z,an)==(12,42) and an-z==fk and Fr(z,an)==Fr(2,7)
assert [y for y in range(1,100) if Fr(y,y+fk)==Fr(2,7)]==[12]
assert 7*7==49 and 2*fk==60 and Fr(fk,2)*7==105 and fk*7==210
mk(P,'0002',tipId='ysb-toplamfark',tip='İki kişinin yaşları: toplam, fark, oran',z='kolay',alt='Yaşlar Oranı',kaz='Yaşlar oranı ve yaş farkından büyük yaşı bulur.',kalip='hikâyeli',adim=2,
 kart='K-YASB-01 (iki kişi: oran) · Zeynep ve annesi',
 metin='Zeynep’in yaşının annesinin yaşına oranı 2/7’dir.\nAnnesi Zeynep’ten 30 yaş büyük olduğuna göre annesi bugün kaç yaşındadır?',
 dogru=an,yan=[(49,'Payı 7 olan terimi 7 ile çarpmış; k değerini bulmamış.','bilgi'),(2*fk,'30 yaş farkını iki katlayıp annenin yaşı sanmış.','dikkat'),(105,'Farkı 2 parça sanıp parçayı 15 bulmuş, 7 × 15 yazmış; fark 7 − 2 = 5 parçadır.','bilgi'),(210,'Farkı 7 ile çarpmış; parça değerini bulmamış.','islem')],
 istenen='Annenin bugünkü yaşı.',
 ip=['Yaşlara 2k ve 7k de; aralarındaki fark kaç k eder?'],
 bilgi=[ORAN],
 ad=[A('Yaşları k ile yaz','Zeynep 2k, annesi 7k yaşında.','Zeynep: 2k · anne: 7k'),A('Farkı kur','Fark 7k − 2k = 5k ve 30’a eşit.','5k = 30 → k = 6'),A('Annenin yaşı','Annesi 7k yaşında.','7 × 6 = 42 (Zeynep 12) ✓')],
 puf='Oranı verilen iki yaşta fark (büyük pay − küçük pay) parçadır; farktan parça değerini bul, sonra istenen yaşla çarp.')

# ---------- 03 kolay · yıl ----------
kaan,cem=1998,2009; y40=kaan+40; assert y40==2038 and y40-cem==29 and 2026-cem==17 and 29+17==46 and 40+(cem-kaan)==51 and cem-kaan==11 and 40+29==69 and cem-kaan>0
mk(P,'0003',tipId='ysb-yilhesap',tip='Doğum yılı, takvim yılı ve yıl dönümü',z='kolay',alt='Doğum Yılı',kaz='Doğum yıllarından yaşları hesaplar ve iki kişinin yaşlarını aynı yılda karşılaştırır.',kalip='hikâyeli',adim=2,
 kart='K-YASB-05 (doğum yılı–yıl hesabı) · iki kardeşin doğum yılları',
 metin='Kaan 1998, kardeşi Cem 2009 yılında doğmuştur. Bir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki fark olarak alınmaktadır.\nBuna göre Kaan 40 yaşına geldiği yıl Cem kaç yaşında olur?',
 dogru=29,yan=[(11,'Sorulan yaş yerine iki doğum yılı arasındaki farkı (2009 − 1998) yazmış.','dikkat'),(40,'Cem’i de Kaan’la aynı yaşta sanmış.','dikkat'),(69,'Kaan’ın 40’ı ile Cem’in 29’unu toplamış.','islem'),(51,'Cem’in Kaan’dan büyük olduğunu sanıp 40 + 11 hesaplamış.','bilgi')],
 istenen='Cem’in o yıldaki yaşı.',
 ip=['Önce Kaan’ın 40 yaşına geldiği takvim yılını bul.'],
 bilgi=[YIL],
 ad=[A('Yılı bul','Kaan 40 yaşına, doğum yılından 40 yıl sonra gelir.','1998 + 40 = 2038'),A('Cem’in yaşı','Yaş = yıl − doğum yılı.','2038 − 2009 = 29'),A('Kontrol','Yaş farkı 11 olmalı.','40 − 29 = 11 = 2009 − 1998 ✓')],
 puf='Takvim yılı verilmişse her kişinin yaşı için “yıl − doğum yılı” yaz; yaş farkı doğum yılları farkına eşittir.')

# ---------- 04 kolay · üç kardeş ----------
sol=[x for x in range(1,40) if x+(x+3)+(x+6)==45]; assert sol==[12]
mk(P,'0004',tipId='ysb-toplamfark',tip='İki kişinin yaşları: toplam, fark, oran',z='kolay',alt='Üç Kardeş',kaz='Aralarında sabit yaş farkı olan üç kardeşin yaşlarını toplamdan bulur.',kalip='düz',adim=2,
 kart='K-YASB-01 (kardeşler: toplam) · 3’er yıl arayla üç kardeş',
 metin='Üç kardeşin bugünkü yaşları toplamı 45’tir.\nOrtanca kardeş en küçüğünden, en büyük kardeş de ortancadan 3 yaş büyüktür.\nBuna göre en büyük kardeş kaç yaşındadır?',
 dogru=18,yan=[(12,'En küçük kardeşin yaşını bulup durmuş.','dikkat'),(15,'Üç yaşın ortalamasını (ortanca yaş) en büyük sanmış.','dikkat'),(21,'Ortancanın 15 olduğunu bulup 6 eklemiş; aralık 3’tür.','islem'),(30,'Toplamdan ortanca yaşı çıkarıp en büyük sanmış (45 − 15).','dikkat')],
 istenen='En büyük kardeşin yaşı.',
 ip=['En küçüğe x de; diğer ikisini x cinsinden yaz ve toplamı kur.'],
 bilgi=[FARK],
 ad=[A('Yaşları yaz','En küçük x olsun.','x ve x + 3 ve x + 6'),A('Toplamı kur','Üçünün toplamı 45.','3x + 9 = 45 → x = 12'),A('En büyüğü bul','En büyük x + 6.','12 + 6 = 18 (yaşlar 12, 15, 18) ✓')],
 puf='Aralarında sabit fark olan yaşları en küçüğe göre yaz; toplamda sabit kısımları (3 + 6) ayrı topla.')

# ---------- 05 orta · oran değişimi ----------
bs=[(y,o) for o in range(1,100) for y in range(1,o) if Fr(y,o)==Fr(2,9) and Fr(y+6,o+6)==Fr(1,3)]
assert bs==[(8,36)] and 36-8>=18 and 36+6==42 and 36-8==28 and Fr(8,2)==4
mk(P,'0005',tipId='ysb-yilkaydir',tip='Yıl kaydırma ve yaşlar oranının değişimi',z='orta',alt='Oranın Değişimi',kaz='Bugünkü ve gelecekteki yaşlar oranından yaşları bulur.',kalip='hikâyeli',adim=3,
 kart='K-YASB-02 (yıl kaydırma, oran değişimi) · Burak ve babası',
 metin='Burak’ın yaşının babasının yaşına oranı bugün 2/9’dur.\n6 yıl sonra bu oran 1/3 olacaktır.\nBuna göre Burak’ın babası bugün kaç yaşındadır?',
 dogru=36,yan=[(4,'Yalnız k değerini (4) bulup durmuş.','dikkat'),(8,'Burak’ın yaşını bulup babasını sormayı unutmuş.','dikkat'),(28,'İki yaş arasındaki farkı (7k) babanın yaşı sanmış.','dikkat'),(42,'6 yıl sonraki baba yaşını bugünkü yaş sanmış.','dikkat')],
 istenen='Babanın bugünkü yaşı.',
 ip=['Bugünkü yaşlara 2k ve 9k de; 6 yıl sonra ikisine de 6 ekle ve oranı eşitle.'],
 bilgi=[ORAN,ZAMAN],
 ad=[A('Bugünkü yaşlar','Burak 2k, babası 9k yaşında.','2k · 9k'),A('6 yıl sonra','İkisi de 6 yaş büyür, oran 1/3 olur.','(2k + 6)/(9k + 6) = 1/3 → 6k + 18 = 9k + 6'),A('k’yi bul','Denklemi çöz.','3k = 12 → k = 4'),A('Babanın yaşı','Baba 9k yaşında.','9 × 4 = 36 (Burak 8; 14/42 = 1/3 ✓)')],
 puf='Yaşlar oranı verilince bugünkü yaşları k ile yaz; yıl kaydırırken iki yaşa da aynı sayıyı ekle, oranı yeni yaşlar için kur.')

# ---------- 06 orta · ben senin yaşındayken ----------
r6=[(a,b) for a in range(1,100) for b in range(1,a) if 2*b-(a-b)==40 and 2*a+(a-b)==72]
assert r6==[(32,24)] and (32-24,24-8)==(8,16) and 40//2==20 and 72//2==36
mk(P,'0006',tipId='ysb-benseninyas',tip='“Ben senin yaşındayken” tipi sabit yaş farkı',z='orta',alt='Sabit Yaş Farkı',kaz='“Ben senin yaşındayken” ve “sen benim yaşıma geldiğinde” bilgilerinden yaşları bulur.',kalip='hikâyeli',adim=4,
 kart='K-YASB-03 (ben senin yaşındayken) · iki kız kardeşin yaşları toplamları',
 metin='Selma, kız kardeşi Nur’a şunları söylemiştir:\n• “Ben senin bugünkü yaşındayken ikimizin yaşları toplamı 40’tı.”\n• “Sen benim bugünkü yaşıma geldiğinde ikimizin yaşları toplamı 72 olacak.”\nSelma, Nur’dan büyük olduğuna göre Selma bugün kaç yaşındadır?',
 dogru=32,yan=[(8,'Yaş farkını (8) Selma’nın yaşı sanmış.','dikkat'),(16,'Nur’un geçmişteki yaşını (16) bulup durmuş.','dikkat'),(20,'İlk toplamı ikiye bölüp (40 ÷ 2) iki kardeşi aynı yaşta saymış.','bilgi'),(24,'Nur’un bugünkü yaşını (24) Selma’nın yaşı sanmış.','dikkat')],
 istenen='Selma’nın bugünkü yaşı.',
 ip=['Yaş farkına d de; geçmişte ve gelecekte iki yaşı d cinsinden yaz.'],
 bilgi=[KAYAN],
 ad=[A('Yaşlar ve fark','Selma s, Nur n yaşında; fark d = s − n.','d = s − n'),A('Geçmişteki toplam','d yıl önce Selma n, Nur n − d yaşındaydı.','n + (n − d) = 40 → 2n − d = 40'),A('Gelecekteki toplam','d yıl sonra Nur s, Selma s + d olur.','s + (s + d) = 72 → 2s + d = 72'),A('İkisini çöz','Taraf tarafa çıkar: 2(s − n) + 2d = 32 → 4d = 32.','d = 8 · 2n = 48 → n = 24 · s = 32')],
 puf='“Ben senin yaşındayken” yaş farkı kadar geri, “sen benim yaşıma geldiğinde” yaş farkı kadar ileri gitmektir; farkı bilinmeyen alıp iki toplamı yaz.')

# ---------- 07 orta · aile ortalama ----------
ba=[(b,an_) for b in range(1,100) for an_ in range(1,100) if b-an_==4 and b+an_+4==72]
assert ba==[(36,32)] and (36+32)//2==34 and 24*3==72 and 36-4>=18 and 32-4>=18
mk(P,'0007',tipId='ysb-aile',tip='Üç ve dört kişilik aile, yaş ortalaması',z='orta',alt='Aile ve Ortalama',kaz='Üç kişilik bir ailenin yaş ortalamasından toplamı bulup babanın yaşını hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-YASB-04 (üç kişilik aile, yaş ortalaması) · anne, baba, 4 yaşında çocuk',
 metin='Anne, baba ve 4 yaşında bir çocuktan oluşan üç kişilik bir ailenin yaş ortalaması 24’tür.\nBaba, anneden 4 yaş büyük olduğuna göre baba bugün kaç yaşındadır?',
 dogru=36,yan=[(4,'Çocuğun yaşını babanın yaşı sanmış.','dikkat'),(32,'Anne ile baba yaşlarından annenin yaşını bulup durmuş.','dikkat'),(34,'Anne ile babanın yaşları ortalamasını (68 ÷ 2) babanın yaşı sanmış.','dikkat'),(72,'Üç kişinin yaşları toplamını babanın yaşı sanmış.','dikkat')],
 istenen='Babanın bugünkü yaşı.',
 ip=['Ortalamadan toplamı bul; çocuğun yaşını çıkarınca anne ile babanın toplamı kalır.'],
 bilgi=[ORT,FARK],
 ad=[A('Toplam yaşı bul','Toplam = ortalama × kişi sayısı.','24 × 3 = 72'),A('Anne ile baba','Çocuğun 4 yaşını çıkar.','72 − 4 = 68 = anne + baba'),A('Toplam ve fark','Baba anneden 4 yaş büyük: b + a = 68, b − a = 4.','2b = 72 → b = 36 (anne 32)')],
 puf='Ortalama verilince hemen toplama geç (ortalama × kişi sayısı); bilinen kişilerin yaşını çıkarıp kalanı toplam–fark yöntemiyle çöz.')

# ---------- 08 orta · doğum yılı, 3 katı ----------
by,cy=1990,2014; sy=[y for y in range(cy+1,2200) if y-by==3*(y-cy)]; assert sy==[2026] and 2026-by==36 and 2026-cy==12 and by+12==2002
assert cy-by==24 and 24//3==8 and cy+8==2022 and cy+24==2038 and cy+36==2050 and cy-by>=18
mk(P,'0008',tipId='ysb-yilhesap',tip='Doğum yılı, takvim yılı ve yıl dönümü',z='orta',alt='Doğum Yılı',kaz='Doğum yıllarından kurduğu denklemle yaşların belirli bir kat ilişkisine ulaştığı yılı bulur.',kalip='hikâyeli',adim=3,
 kart='K-YASB-05 (doğum yılı–yıl hesabı) · baba–çocuk ve 3 katı olduğu yıl',
 metin='Bir baba 1990, çocuğu 2014 yılında doğmuştur. Bir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki fark olarak alınmaktadır.\nBabanın yaşının çocuğun yaşının 3 katı olduğu yıl, aşağıdakilerden hangisidir?',
 dogru=2026,yan=[(2002,'Babanın doğum yılına çocuğun yaşını (12) ekleyerek yıl bulmuş.','dikkat'),(2022,'Yaş farkını (24) 3 parçaya bölüp çocuğun yaşını 8 almış; 24 farkı 2 parçadır.','bilgi'),(2038,'Çocuğun doğum yılına yaş farkını (24) eklemiş.','dikkat'),(2050,'Çocuğun doğum yılına babanın o yılki yaşını (36) eklemiş.','dikkat')],
 istenen='Babanın yaşının çocuğun yaşının 3 katı olduğu yıl.',
 ip=['Yıla y de; babanın yaşı y − 1990, çocuğun yaşı y − 2014 olur.'],
 bilgi=[YIL],
 ad=[A('Yaşları yaz','Yıl y olsun.','baba: y − 1990 · çocuk: y − 2014'),A('Denklemi kur','Baba, çocuğun 3 katı.','y − 1990 = 3 × (y − 2014)'),A('y’yi bul','Açıp düzenle.','y − 1990 = 3y − 6042 → 2y = 4052 → y = 2026'),A('Kontrol','Yaşları hesapla.','baba 36, çocuk 12 ✓')],
 puf='Yıl sorularında bilinmeyen yılı y al ve her yaşı “y − doğum yılı” olarak yaz; kat ilişkisi doğrudan denklem olur.')

# ---------- 09 orta · öncüllü ----------
mi,an9=Fr(48,4),0; mina=12; ann=36; assert mina+ann==48 and ann==3*mina
I=(mina+6)+(ann+6)==60; II=ann-3==4*(mina-3); III=(mina+(ann-mina))+(ann+(ann-mina))==96
assert (I,II,III)==(True,False,True) and Fr(33,9)!=4 and 48+6==54 and 36+36==72
mk(P,'0009',tipId='ysb-yilkaydir',tip='Yıl kaydırma ve yaşlar oranının değişimi',z='orta',alt='Öncüllü Yaş',kaz='Verilen yaş bilgilerinden bugünkü yaşları bulup yıl kaydırmalı öncüllerin doğruluğunu sınar.',kalip='öncüllü',adim=3,
 kart='K-YASB-02 (yıl kaydırma) · öncüllü: anne ve kızın yaşları',
 metin='Mina ile annesinin bugünkü yaşları toplamı 48’dir.\nAnnesinin yaşı Mina’nın yaşının 3 katıdır.\nBuna göre,\nI. 6 yıl sonra ikisinin yaşları toplamı 60 olur.\nII. 3 yıl önce annesinin yaşı Mina’nın yaşının 4 katıydı.\nIII. Mina, annesinin bugünkü yaşına geldiğinde ikisinin yaşları toplamı 96 olur.\nifadelerinden hangileri doğrudur?',
 dogru='I ve III',sira=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III'],
 yan=[('Yalnız I','III’te Mina 36 yaşına geldiğinde annesinin yaşını hâlâ 36 saymış (toplam 72).','bilgi'),('Yalnız II','II’de 33 ÷ 9 ≈ 4 sanmış; I ve III’ü yanlış saymış.','islem'),('II ve III','I’de yalnız bir kişiye 6 ekleyip toplamı 54 bulmuş (I yanlış); II’de 33 ile 9’un oranını 4 sanmış (II doğru).','bilgi'),('I, II ve III','II’de 3 yıl önceki yaşların (33 ve 9) oranını 4 sanmış.','islem')],
 istenen='Doğru olan ifadeler.',
 ip=['Önce Mina ile annesinin bugünkü yaşlarını bul; sonra her öncülü bu yaşlarla ayrı ayrı sına.'],
 bilgi=[ZAMAN,FARK],
 ad=[A('Bugünkü yaşlar','Mina m, annesi 3m yaşında; toplam 48.','4m = 48 → m = 12, anne 36'),A('I’i sına','6 yıl sonra iki kişi de 6 yaş büyür.','12 + 6 = 18 · 36 + 6 = 42 · 18 + 42 = 60 → doğru'),A('II’yi sına','3 yıl önce 9 ve 33 yaşındalar.','4 × 9 = 36 ≠ 33 → yanlış'),A('III’ü sına','Yaş farkı 24 yıl; Mina 36 olunca anne 60.','36 + 60 = 96 → doğru')],
 puf='Öncüllü yaş sorularında önce bugünkü yaşları bul, sonra her öncülü yaşlarla tek tek hesaplayıp sına.')

# ---------- 10 orta · mum (yeni nesil) ----------
m10=[(a,b) for a in range(1,60) for b in range(1,60) if a+b==20 and a-4==3*(b-4) and b>4]
assert m10==[(13,7)]; a10,b10=13,7; t10=(40-20)//2; assert t10==10 and a10+t10==23 and 13+20==33 and 40-10==30 and 7+10==17
mk(P,'0010',tipId='ysb-yilhesap',tip='Doğum yılı, takvim yılı ve yıl dönümü',z='orta',alt='Mum Sayısı',kaz='Her yıl artan toplam mum sayısı kuralından iki kardeşin yaşlarını ve gelecekteki yaşı bulur.',kalip='yeni nesil',adim=3,
 kart='K-YASB-05 (yıl dönümü, mum) · iki kardeşin ortak pastası',
 metin='Defne ile kardeşi Kuzey, her yılbaşında ortak bir pasta kesmektedir. Pastaya, o yılbaşında ikisinin yaşları toplamı kadar mum konmaktadır.\nBu yıl pastaya 20 mum konmuştur. 4 yıl önce Defne’nin yaşı, Kuzey’in yaşının 3 katıydı.\nBuna göre pastaya 40 mum konacağı yıl Defne kaç yaşında olacaktır?',
 dogru=23,yan=[(17,'Kuzey’in 10 yıl sonraki yaşını (7 + 10) yazmış.','dikkat'),(30,'Mum sayısından yıl sayısını çıkarmış (40 − 10).','dikkat'),(33,'Mum artışını (40 − 20 = 20) 2’ye bölmeyip yıl sayısı sanmış (13 + 20).','bilgi'),(40,'Mum sayısını Defne’nin yaşı sanmış.','dikkat')],
 istenen='40 mum konacağı yıl Defne’nin yaşı.',
 ip=['Bu yılki yaşları d ve k al, bugünkü toplam ile 4 yıl önceki kat ilişkisinden yaşları bul.'],
 bilgi=[TOPL,ZAMAN],
 ad=[A('Bugünkü yaşlar','D + K = 20 ve D − 4 = 3(K − 4).','D = 3K − 8'),A('Çöz','İlk denklemde yerine yaz.','4K − 8 = 20 → K = 7, D = 13'),A('Kaç yıl geçer','Mum sayısı her yıl 2 artar (iki kişi birer yaş büyür).','(40 − 20) ÷ 2 = 10 yıl'),A('Defne’nin yaşı','Bugünkü yaşa 10 ekle.','13 + 10 = 23 (Kuzey 17; 23 + 17 = 40 ✓)')],
 puf='İki kişinin yaşları toplamı yılda 2 artar; hedef toplama kaç yılda varıldığını bulmak için farkı 2’ye böl.')

# ---------- 11 orta · anne-kız ----------
r11=[(a,k) for a in range(1,100) for k in range(4,60) if a+k+10==70 and a-3==5*(k-3)]
assert r11==[(48,12)] and 48-12>=18 and 12-3>0 and 48+5==53 and 48-3==45 and 48-12==36
mk(P,'0011',tipId='ysb-yilkaydir',tip='Yıl kaydırma ve yaşlar oranının değişimi',z='orta',alt='Yıl Kaydırma',kaz='Gelecekteki toplam ve geçmişteki kat ilişkisinden bugünkü yaşı bulur.',kalip='hikâyeli',adim=3,
 kart='K-YASB-02 (yıl kaydırma) · anne ve kızı, hem önce hem sonra',
 metin='Bir anne ile kızının 5 yıl sonraki yaşları toplamı 70 olacaktır.\n3 yıl önce annenin yaşı, kızının yaşının 5 katıydı.\nBuna göre anne bugün kaç yaşındadır?',
 dogru=48,yan=[(12,'Kızın bugünkü yaşını bulup anneyi sormayı unutmuş.','dikkat'),(36,'Anne ile kızı arasındaki yaş farkını annenin yaşı sanmış.','dikkat'),(45,'Annenin 3 yıl önceki yaşını bugünkü yaş sanmış.','dikkat'),(53,'Annenin 5 yıl sonraki yaşını bugünkü yaş sanmış.','dikkat')],
 istenen='Annenin bugünkü yaşı.',
 ip=['5 yıl sonra iki kişinin toplamı kaç artar? Önce bugünkü toplamı bul.'],
 bilgi=[ZAMAN,TOPL],
 ad=[A('Bugünkü toplam','İki kişi 5 yıl sonra toplam 10 yaş büyümüş olur.','a + k + 10 = 70 → a + k = 60'),A('Geçmiş koşulu','3 yıl önce anne a − 3, kız k − 3.','a − 3 = 5(k − 3) → a = 5k − 12'),A('Çöz','İlk denkleme yaz.','6k − 12 = 60 → k = 12'),A('Annenin yaşı','a = 60 − 12.','a = 48 (3 yıl önce 45 = 5 × 9 ✓)')],
 puf='İki kişinin toplamını t yıl kaydırırken 2t ekle ya da çıkar; iki ayrı yıl koşulu verilince ikisini de bugünkü yaşlarla yaz.')

# ---------- 12 orta · doğmamış çocuk ortalama ----------
tot3=22*3; tot_now=tot3+3*7+5; assert tot_now==92 and Fr(tot_now,4)==23 and 5-7<0
assert 22+7==29 and Fr(tot3+4*7,4)==Fr(47,2) and 22!=23
mk(P,'0012',tipId='ysb-aile',tip='Üç ve dört kişilik aile, yaş ortalaması',z='orta',alt='Doğmamış Çocuk',kaz='Geçmişte henüz doğmamış bir aile üyesini sayıya katmadan yaş ortalamasının bugünkü değerini bulur.',kalip='hikâyeli',adim=4,
 kart='K-YASB-04 (dört kişilik aile, doğmamış çocuk) · 7 yıl önceki ortalama',
 metin='Anne, baba ve iki çocuktan oluşan bir ailenin küçük çocuğu bugün 5 yaşındadır.\n7 yıl önce küçük çocuk henüz doğmamıştı; o tarihte anne, baba ve büyük çocuktan oluşan üç kişinin yaşları ortalaması 22’ydi.\nBuna göre bu ailenin bugünkü dört kişilik yaş ortalaması kaçtır?',
 dogru=23,yan=[(22,'Ortalamanın yıllar içinde değişmeyeceğini sanmış.','bilgi'),(Fr(47,2),'Küçük çocuğu 7 yıl önce 0 yaşında sayıp dört kişiyi de 7 yıl yaşlandırmış: (66 + 28) ÷ 4.','bilgi'),(29,'Ortalamaya 7 yıl ekleyip (22 + 7) küçük çocuğu hesaba katmamış.','bilgi'),(92,'Bugünkü yaşlar toplamını ortalama sanmış.','dikkat')],
 istenen='Bugünkü yaş ortalaması.',
 ip=['7 yıl önce ailede kaç kişi vardı ve bugün bu kişilerin yaşlar toplamı ne olur?'],
 bilgi=[ORT,TOPL],
 ad=[A('7 yıl önceki toplam','Üç kişinin toplamı.','22 × 3 = 66'),A('Üç kişi bugün','Her biri 7 yaş büyümüştür.','66 + 3 × 7 = 87'),A('Küçük çocuğu ekle','O tarihte doğmamıştı; bugün 5 yaşında.','87 + 5 = 92'),A('Ortalamayı bul','Toplam ÷ 4.','92 ÷ 4 = 23')],
 puf='Geçmişte olmayan bir kişi toplam hesabına yıl kaydırmasıyla değil, bugünkü yaşıyla ayrıca eklenir; ortalamayı hep toplama çevirerek kaydır.')

# ---------- 13 orta · baba = iki çocuğun toplamı ----------
bb,c1,c2=38,11,5; t=[t for t in range(0,200) if bb+t==c1+c2+2*t]; assert t==[22] and bb+22==60 and (c1+22)+(c2+22)==60
assert (bb-(c1+c2))==22 and Fr(bb-(c1+c2),2)==11 and bb-c1==27 and bb-c2==33 and bb-c1>=18 and bb-c2>=18
mk(P,'0013',tipId='ysb-esitlenme',tip='Kaç yıl sonra eşitlenir: herkes ayrı yaşlanır',z='orta',alt='Her Biri Yaşlanır',kaz='Bir babanın yaşının iki çocuğunun yaşları toplamına eşit olacağı yıl sayısını, herkesin ayrı yaşlandığını dikkate alarak bulur.',kalip='hikâyeli',adim=3,
 kart='K-YASB-06 (kaç yıl sonra eşitlenir) · baba ve iki çocuk',
 metin='Bir babanın yaşı 38, iki çocuğunun yaşları 11 ve 5’tir.\nBuna göre kaç yıl sonra babanın yaşı, iki çocuğunun yaşları toplamına eşit olur?',
 dogru=22,yan=[(11,'Babanın yaşını sabit tutup yalnız çocukların yaşlandığını sanmış (38 = 16 + 2t).','bilgi'),(27,'Babanın yaşından büyük çocuğun yaşını çıkarmış (38 − 11).','dikkat'),(33,'Babanın yaşından küçük çocuğun yaşını çıkarmış (38 − 5).','dikkat'),(38,'Babanın yaşını yıl sayısı sanmış.','dikkat')],
 istenen='Eşitliğin sağlandığı yıl sayısı.',
 ip=['t yıl sonra babanın yaşını ve iki çocuğun yaşları toplamını t cinsinden yaz.'],
 bilgi=[AYRI],
 ad=[A('t yıl sonra','Baba bir kişi, çocuklar iki kişidir.','baba: 38 + t · çocuklar: (11 + t) + (5 + t) = 16 + 2t'),A('Eşitle','İki ifadeyi eşitle.','38 + t = 16 + 2t'),A('t’yi bul','Bilinmeyenleri tek tarafa topla.','t = 22'),A('Kontrol','22 yıl sonra yaşlar.','baba 60 · çocuklar 33 + 27 = 60 ✓')],
 puf='Bir tarafta 1, diğer tarafta n kişi varsa herkes aynı hızda yaşlanır; iki taraf da t’ye bağlı yazılır, yalnızca çocukları kaydırmak hatadır.')

# ---------- 14 zor · tablo ----------
by_,ky=1972,[2011,2014,2017]
tt=[t for t in range(0,100) if (2026+t-by_)==sum(2026+t-k for k in ky)]; assert tt==[9]
assert 2026-by_==54 and sum(2026-k for k in ky)==36 and 54-36==18 and Fr(18,3)==6 and  all(2026-k>=0 for k in ky) and min(k-by_ for k in ky)>=18
mk(P,'0014',tipId='ysb-esitlenme',tip='Kaç yıl sonra eşitlenir: herkes ayrı yaşlanır',z='orta',alt='Tablo ve Eşitlenme',kaz='Doğum yılları tablosundan yaşları bulup babanın yaşının üç çocuğun yaşları toplamına eşit olacağı yılı hesaplar.',kalip='tablo',adim=4,
 kart='K-YASB-06 (kaç yıl sonra eşitlenir) · tablo: baba ve üç çocuk',
 metin='Aşağıdaki tabloda bir babanın ve üç çocuğunun doğum yılları verilmiştir.\nKişi : Baba | 1. çocuk | 2. çocuk | 3. çocuk\nDoğum yılı : 1972 | 2011 | 2014 | 2017\nBir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki fark olarak alınmaktadır.\nBuna göre 2026 yılından kaç yıl sonra babanın yaşı, üç çocuğunun yaşları toplamına eşit olur?',
 dogru=9,yan=[(6,'Yaş farkını (18) çocuk sayısına bölmüş; baba da yaşlandığı için fark yılda 2 değişir.','bilgi'),(18,'Yalnız çocukların yaşlandığını sanıp fark olan 18 yılı yazmış.','bilgi'),(36,'Çocukların 2026’daki yaşları toplamını (36) yıl sayısı sanmış.','dikkat'),(54,'Babanın 2026’daki yaşını (54) yıl sayısı sanmış.','dikkat')],
 istenen='Eşitliğe kaç yıl sonra ulaşılacağı.',
 ip=['2026’da babanın yaşını ve üç çocuğun yaşları toplamını bul; her yıl bu iki değer nasıl değişir?'],
 bilgi=[YIL,AYRI],
 ad=[A('2026’daki yaşlar','Yaş = yıl − doğum yılı.','baba: 54 · çocuklar: 15 + 12 + 9 = 36'),A('Aradaki fark','Baba çocukların toplamından büyük.','54 − 36 = 18'),A('Yılda değişim','Baba 1, çocukların toplamı 3 artar; fark yılda 2 azalır.','3 − 1 = 2'),A('Yıl sayısı','Farkı hızla böl.','18 ÷ 2 = 9 yıl (63 = 24 + 21 + 18 ✓)')],
 puf='Bir kişinin yaşı birden çok kişinin toplamına eşitlenirken fark yılda (kişi sayısı − 1) kadar değişir; farkı bu hıza böl.')

# ---------- 15 zor · oran, iki yönlü ----------
o15=[(y,o) for o in range(1,200) for y in range(7,o) if Fr(y-6,o-6)==Fr(2,5) and Fr(y+6,o+6)==Fr(1,2)]
assert o15==[(30,66)] and 30+66==96 and 66-30==36 and 96-12==84 and 96+12==108 and 66-30>=18
mk(P,'0015',tipId='ysb-yilkaydir',tip='Yıl kaydırma ve yaşlar oranının değişimi',z='zor',alt='İki Yönlü Oran',kaz='Geçmişteki ve gelecekteki iki oran bilgisinden yaş farkını bulup bugünkü yaşları hesaplar.',kalip='hikâyeli',adim=5,
 kart='K-YASB-02 (yıl kaydırma, iki oran) · Orhan ve babası',
 metin='Orhan ile babasının yaşları için şunlar bilinmektedir:\n• 6 yıl önce Orhan’ın yaşı, babasının yaşının 2/5’i kadardı.\n• 6 yıl sonra Orhan’ın yaşı, babasının yaşının yarısı kadar olacaktır.\nBuna göre ikisinin bugünkü yaşları toplamı kaçtır?',
 dogru=96,yan=[(36,'Yaş farkını (36) bulup yaşlar toplamını sormayı unutmuş.','dikkat'),(66,'Babanın bugünkü yaşını toplam sanmış.','dikkat'),(84,'6 yıl önceki yaşlar toplamını bugünkü toplam sanmış.','dikkat'),(108,'6 yıl sonraki yaşlar toplamını bugünkü toplam sanmış.','dikkat')],
 istenen='Bugünkü yaşlar toplamı.',
 ip=['Yaş farkına d de; her iki zamanda da küçük yaşı d cinsinden yaz.'],
 bilgi=[FARK,ORAN],
 ad=[A('Geçmişte oran 2/5','6 yıl önce fark d; küçük yaş 2 parça, büyük 5 parça, fark 3 parça.','Orhan o zaman: 2d/3'),A('Gelecekte oran 1/2','6 yıl sonra küçük yaş 1 parça, büyük 2 parça, fark 1 parça.','Orhan o zaman: d'),A('İkisini birleştir','İki zaman arası 12 yıl.','d − 2d/3 = 12 → d = 36'),A('Bugünkü yaşlar','Orhan 6 yıl sonra 36, yani bugün 30; babası 66.','30 + 66 = 96 (6 yıl önce 24/60 = 2/5 ✓)')],
 puf='Yaş farkı sabit olduğundan her oran bilgisinden küçük yaş farkın bir kesri olarak yazılır; iki zaman arasındaki yıl farkı küçük yaşların farkına eşittir.')

# ---------- 16 zor · ikizler ----------
r16=[(c,y) for c in range(7,60) for y in range(6,60) if y==c-6 and 2*(y-5)==c-5]; assert r16==[(17,11)]
tn=[t for t in range(0,100) if 17+22+3*t==60]; assert tn==[7] and 17+22==39 and 60-39==21 and Fr(21,2)==Fr(21,2) and Fr(24-0,1)==24 and (60-24)//3==12
c7,y7=7,1; assert 2*(y7+5)==c7+5 and (60-(c7+2*y7))//3==17 and y7==c7-6
mk(P,'0016',tipId='ysb-esitlenme',tip='Kaç yıl sonra eşitlenir: herkes ayrı yaşlanır',z='zor',alt='İkizler',kaz='İkiz kardeşler ve ağabeyleri arasındaki yaş bilgilerinden yaşları bulup toplamın belirli bir değere ulaşacağı yılı hesaplar.',kalip='hikâyeli',adim=5,
 kart='K-YASB-06 (ikizler, toplamın eşitlenmesi) · Arda, Berk ve Can',
 metin='İkiz kardeşler Arda ve Berk, ağabeyleri Can’dan 6 yaş küçüktür.\n5 yıl önce ikizlerin yaşları toplamı, Can’ın o zamanki yaşına eşitti.\nBuna göre üç kardeşin yaşları toplamı kaç yıl sonra 60 olur?',
 dogru=7,yan=[(Fr(21,2),'Üç kardeşin yaşları toplamı yerine iki kişinin yaşlandığını sanıp 21 ÷ 2 hesaplamış.','bilgi'),(12,'Bugün yerine 5 yıl önceki toplamdan (24) başlayıp (60 − 24) ÷ 3 hesaplamış.','dikkat'),(17,'“5 yıl önce” yerine “5 yıl sonra” okumuş (Can 7, ikizler 1 yaşında).','dikkat'),(21,'Toplamdaki artışı (60 − 39) yıl sayısı sanmış; her yıl toplam 3 artar.','bilgi')],
 istenen='Toplamın 60 olacağı yıl sayısı.',
 ip=['Can’a c, ikizlerin her birine c − 6 de; 5 yıl önceki toplam ilişkisini yaz.'],
 bilgi=[TOPL,ZAMAN],
 ad=[A('Yaşları yaz','Can c; ikizler c − 6 yaşındadır.','Can: c · ikizler: c − 6, c − 6'),A('5 yıl önce','İkizlerin toplamı Can’ın yaşına eşitti.','2(c − 6 − 5) = c − 5 → 2c − 22 = c − 5 → c = 17'),A('Bugünkü toplam','Can 17, ikizler 11’er yaşında.','17 + 11 + 11 = 39'),A('Kaç yıl sonra','Üç kişi olduğundan toplam yılda 3 artar.','39 + 3t = 60 → t = 7')],
 puf='Toplam sorularında kişi sayısını unutma: n kişinin toplamı yılda n artar, hedefe kalan farkı n’ye bölerek yıl bulunur.')

# ---------- 17 zor · öncüllü ----------
sol17=[(b,al,ce) for b in range(5,60) for al in [2*b] for ce in [b-4] if al+b+ce==44]; assert sol17==[(12,24,8)]
ali,bes,cem_=24,12,8
I17=(ali+10)>2*(cem_+10); II17=(bes+ali+cem_)+3*(ali-bes)==80; III17=(ali-6)+(bes-6)==12*(cem_-6)
assert (I17,II17,III17)==(False,True,True) and cem_-6>0 and (ali+10,2*(cem_+10))==(34,36)
mk(P,'0017',tipId='ysb-yilkaydir',tip='Yıl kaydırma ve yaşlar oranının değişimi',z='zor',alt='Öncüllü Kardeşler',kaz='Kardeşlerin yaşlarını verilen koşullardan bulup yıl kaydırmalı üç öncülün doğruluğunu sınar.',kalip='öncüllü',adim=5,
 kart='K-YASB-02 (yıl kaydırma) · öncüllü: üç kardeş',
 metin='Ali, Beste ve Cem kardeştir.\nAli’nin yaşı Beste’nin yaşının 2 katıdır; Cem, Beste’den 4 yaş küçüktür.\nÜçünün bugünkü yaşları toplamı 44’tür.\nBuna göre,\nI. 10 yıl sonra Ali’nin yaşı, Cem’in yaşının 2 katından fazla olur.\nII. Beste, Ali’nin bugünkü yaşına geldiğinde üçünün yaşları toplamı 80 olur.\nIII. 6 yıl önce Ali ile Beste’nin yaşları toplamı, Cem’in o zamanki yaşının 12 katıydı.\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',sira=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III'],
 yan=[('Yalnız II','III’te yalnız bir kez 6 çıkarıp (36 − 6 = 30) 30 ≠ 24 bulmuş.','islem'),('Yalnız III','II’de yalnız Beste’nin yaşlandığını sanıp toplamı 56 bulmuş.','bilgi'),('I ve II','I’i doğru saymış (34’ü 36’dan büyük sanmış); III’te Ali ile Beste’yi 6 yıl öncesine kaydırmayı unutup 36 ≠ 24 bulmuş.','dikkat'),('I, II ve III','I’de 34’ü 36’dan büyük sanmış; II ve III’ü doğru bulmuş.','islem')],
 istenen='Doğru olan ifadeler.',
 ip=['Beste’ye b de; Ali ve Cem’i b cinsinden yaz ve toplamdan b’yi bul.'],
 bilgi=[ZAMAN,AYRI],
 ad=[A('Bugünkü yaşlar','Beste b, Ali 2b, Cem b − 4.','b + 2b + (b − 4) = 44 → b = 12 (Ali 24, Cem 8)'),A('I’i sına','10 yıl sonra Ali 34, Cem 18.','2 × 18 = 36 > 34 → yanlış'),A('II’yi sına','Beste 24 yaşına 12 yıl sonra gelir; üç kişi 12’şer yaş büyür.','44 + 3 × 12 = 80 → doğru'),A('III’ü sına','6 yıl önce Ali 18, Beste 6, Cem 2.','18 + 6 = 24 = 12 × 2 → doğru')],
 puf='Önce bugünkü yaşları bul; yıl kaydıran her öncülde kaç kişinin yaşlandığını say, herkes aynı yıl kadar kayar.')

# ---------- 18 zor · ben senin yaşındayken (üç kişi) ----------
r18=[(b,a,k) for b in range(20,90) for a in range(20,90) for k in range(1,60) if a+k==54 and b-(a-k)==37 and b+(a-k)==73]
assert r18==[(55,36,18)] and 55+36+18==109
assert 36-18>=18 and 55-36>0 and 54+73==127 and 55+36==91 and 73==55+18
mk(P,'0018',tipId='ysb-benseninyas',tip='“Ben senin yaşındayken” tipi sabit yaş farkı',z='zor',alt='Üç Kişi',kaz='Anne ile kızı arasındaki sabit yaş farkını kullanarak babanın yaşını bulur ve üç kişinin yaşları toplamını hesaplar.',kalip='hikâyeli',adim=5,
 kart='K-YASB-03 (ben senin yaşındayken) · anne, kız ve baba',
 metin='Anne, baba ve kızdan oluşan bir ailede anne ile kızının bugünkü yaşları toplamı 54’tür.\nAnne, kızının bugünkü yaşındayken baba 37 yaşındaymış.\nKız, annesinin bugünkü yaşına geldiğinde baba 73 yaşında olacaktır.\nBuna göre bu üç kişinin bugünkü yaşları toplamı kaçtır?',
 dogru=109,yan=[(54,'Yalnız anne ile kızın toplamını (verilen 54’ü) yazmış.','dikkat'),(55,'Babanın bugünkü yaşını bulup üç kişiyi toplamayı unutmuş.','dikkat'),(73,'Babanın gelecekteki yaşını (73) bugünkü toplam sanmış.','dikkat'),(91,'Baba ile annenin yaşlarını toplayıp kızı eklememiş (55 + 36).','dikkat')],
 istenen='Üç kişinin bugünkü yaşları toplamı.',
 ip=['Anne ile kız arasındaki yaş farkına d de; baba 37 ile 73 yaşındayken kaç yıl geçtiğine bak.'],
 bilgi=[KAYAN],
 ad=[A('Babanın yaşı','Baba d yıl önce 37, d yıl sonra 73 yaşında; bugünkü yaşı bu ikisinin ortasıdır.','b = (37 + 73) ÷ 2 = 55'),A('Yaş farkı','Ortadan 37’ye iki taraf da d kadar uzaktır.','d = 55 − 37 = 18'),A('Anne ve kız','Toplam 54, fark 18.','anne = (54 + 18) ÷ 2 = 36 · kız = 18'),A('Üçü topla','Baba + anne + kız.','55 + 36 + 18 = 109')],
 puf='Aynı fark kadar geri ve ileri bilgi verilmişse bugünkü yaş bu iki yaşın ortasıdır; farkı da yarısı olarak bul.')

# ---------- 19 zor · aile 9 yıl önce ----------
bo,ko=41,26
assert bo-9==4*(ko-18) and ko-18==8 and bo-4==37 and 37+ko+3*5==78 and 63+5==68 and bo+ko+15==82
kk=77; assert kk-9==4*(ko-9) and kk-4==73 and 73+ko+15==114 and 37+ko==63
assert min(37-(ko-9),37-17)>=18
mk(P,'0019',tipId='ysb-aile',tip='Üç ve dört kişilik aile, yaş ortalaması',z='zor',alt='Dört Kişilik Aile',kaz='Geçmişteki kat ilişkisinden babanın yaşını bulup ailenin gelecekteki yaşlar toplamını hesaplar.',kalip='hikâyeli',adim=5,
 kart='K-YASB-04 (dört kişilik aile) · 9 yıl önceki kat ilişkisi, 5 yıl sonraki toplam',
 metin='Anne, baba ve iki çocuktan oluşan bir ailede baba, anneden 4 yaş büyüktür.\nİki çocuğun bugünkü yaşları toplamı 26’dır ve her ikisi de 9 yıl önce zaten doğmuş durumdaydı.\n9 yıl önce babanın yaşı, o tarihte iki çocuğun yaşları toplamının 4 katıydı.\nBuna göre 5 yıl sonra anne ile iki çocuğun yaşları toplamı kaç olur?',
 dogru=78,yan=[(63,'Bugünkü toplamı (37 + 26) yazmış; 5 yıl sonrasını hesaplamamış.','dikkat'),(68,'Üç kişi 5’er yıl büyüyeceği halde toplama yalnız 5 eklemiş (63 + 5).','bilgi'),(82,'Anne yerine babanın yaşını almış (41 + 26 + 15).','dikkat'),(114,'9 yıl önce çocuk toplamını 26 − 9 = 17 alıp (iki kişiyi tek kişi saymış) babayı 77, anneyi 73 bulmuş.','bilgi')],
 istenen='5 yıl sonra anne ile iki çocuğun yaşları toplamı.',
 ip=['9 yıl önce iki çocuğun toplamı kaç yaş azalmıştır? Babanın o zamanki yaşından bugünkünü bul.'],
 bilgi=[TOPL,ZAMAN],
 ad=[A('9 yıl önceki çocuk toplamı','İki çocuk 9’ar yıl küçüktü.','26 − 2 × 9 = 8'),A('Babanın yaşı','O tarihte baba bu toplamın 4 katıydı; bugün 9 yıl büyüktür.','4 × 8 = 32 → baba 32 + 9 = 41'),A('Annenin yaşı','Baba anneden 4 yaş büyük.','41 − 4 = 37'),A('5 yıl sonra','Üç kişi 5’er yıl büyür.','37 + 26 + 3 × 5 = 78')],
 puf='Çocukların toplamı t yılda 2t, anne–baba dahil üç kişinin toplamı 3t değişir; her kaydırmada kaç kişinin yaşlandığını say.')

bitir(P,'yasprobiki',UK)
