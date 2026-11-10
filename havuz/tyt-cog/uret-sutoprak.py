"""TYT Coğrafya · Su – Toprak ve Bitkiler: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_a import *
KY='ÖSYM 2018–2026 (bitki toplulukları, topraklar, su kaynakları) · MEB 9–10. sınıf coğrafya'
KARTLAR={
 'K-SUT-01':dict(alt='Toprak horizonları',fikir='Toprak profilinde A, B, C horizonları ve ana kayaç sıralanır; humus A horizonundadır.',tuzak='Humusu B horizonuna yerleştirmek.',zorluk='kolay',kalip='düz',adim=2,tipId='cg-sut-horizon',kaynak=KY),
 'K-SUT-02':dict(alt='Bitki toplulukları ve iklim',fikir='Her bitki topluluğu, geliştiği iklim tipiyle eşleştirilir.',tuzak='Savanı ekvatoral iklime bağlamak.',zorluk='orta',kalip='düz',adim=3,tipId='cg-sut-bitki',kaynak=KY),
 'K-SUT-03':dict(alt='Akarsu rejimi',fikir='Debinin yıl içindeki değişiminden akarsuyun beslenme kaynağı (kar, yağmur, buzul) bulunur.',tuzak='Yüksek debiyi hep yağmura bağlamak.',zorluk='orta',kalip='grafik',adim=3,tipId='cg-sut-rejim',kaynak=KY),
 'K-SUT-04':dict(alt='Zonal topraklar',fikir='İklim ve bitki örtüsü bilgisinden zonal toprak tipi (podzol, çernezyom, laterit) çıkarılır.',tuzak='Kırmızı toprağı her sıcak bölgeye bağlamak; podzol ile çernezyomu karıştırmak.',zorluk='orta',kalip='yeni nesil',adim=4,tipId='cg-sut-zonal',kaynak=KY),
}
TIPLER={'cg-sut-horizon':'Toprak horizonları','cg-sut-bitki':'Bitki topluluğu–iklim eşleştirme','cg-sut-rejim':'Akarsu rejimi (grafik)','cg-sut-zonal':'Zonal topraklar'}
Q=Konu('sutoprak','Su – Toprak ve Bitkiler','cog|Su – Toprak ve Bitkiler',4,KARTLAR,TIPLER,{'kolay':1,'orta':3})

# 0001 kolay · E
Q.soru('0001','K-SUT-01','kolay','Toprak horizonlarını özelliklerine göre ayırt eder.',2,'düz',
 'Toprak profilinde organik madde (humus) bakımından en zengin olan, bitki köklerinin en çok bulunduğu ve verimliliğin belirlendiği üst katman aşağıdakilerden hangisidir?',
 [('B horizonu','B','B horizonu, üstten yıkanan maddelerin biriktiği, humusu az katmandır.','bilgi'),
  ('C horizonu','C','C horizonu ana kayacın ayrışmış parçalarından oluşur; humus içermez.','bilgi'),
  ('Ana kayaç','ana','Ana kayaç toprağın oluştuğu sert tabakadır; organik madde içermez.','bilgi'),
  ('Taban suyu tabakası','su','Taban suyu bir toprak katmanı değildir; toprağın altındaki sudur.','dikkat'),
  ('A horizonu','A','','')],
 'E',lambda t:t=='A','Humusça en zengin üst katman.',
 'Toprak profilinde yüzeye en yakın katman hangisidir?',
 [B('Toprak profili (yukarıdan aşağıya)','A horizonu: humuslu, verimli üst toprak · B horizonu: yıkanan maddelerin biriktiği alt toprak · C horizonu: ayrışmış kayaç parçaları · ana kayaç')],
 [A('Profili sırala','Yüzeyden derine doğru A, B, C horizonları ve ana kayaç gelir.','A → B → C → ana kayaç'),
  A('Özellikle eşle','Bitki kalıntıları yüzeyde ayrışarak humusu oluşturur; humus üstte toplanır.','humus: yüzeyde'),
  A('Sonucu seç','Humusça zengin, köklerin yoğun olduğu katman A horizonudur.','A horizonu')],
 'Humus ve canlılık yüzeyde, kayaç parçaları derinde yer alır.')

# 0002 orta · D
YO='Gür ve çok katlı yağmur ormanı'
ES={'Maki':'Akdeniz iklimi',YO:'Ekvatoral iklim','Tundra':'Tundra iklimi','Savan':'Savan iklimi','Step':'Karasal iklim'}
iddia=[('Maki','Akdeniz iklimi'),(YO,'Ekvatoral iklim'),('Tundra','Tundra iklimi'),('Savan','Ekvatoral iklim'),('Step','Karasal iklim')]
CEL={'Savan':'Savan, ekvatoral iklimde değil savan ikliminde (kurak ve yağışlı mevsimli sıcak bölgelerde) görülür; ekvatoral iklimde yağmur ormanı yer alır.'}
CEL0={'Maki':'Maki, Akdeniz iklimi bölgelerinde görülür; eşleştirme doğrudur.',YO:'Yağmur ormanı, ekvatoral iklim bölgelerinde görülür; eşleştirme doğrudur.','Tundra':'Tundra bitki örtüsü (yosun, liken) tundra ikliminde görülür; eşleştirme doğrudur.'}
Q.soru('0002','K-SUT-02','orta','Bitki topluluklarını görüldükleri iklimlerle eşleştirir.',3,'düz',
 'Aşağıda bitki toplulukları ile bunların görüldüğü iklim tipleri eşleştirilmiştir.\nBu eşleştirmelerden hangisi yanlıştır?',
 [(f'{b} – {i}',(b,i),CEL0[b],'bilgi') for b,i in iddia[:3]]+
 [(f'{iddia[3][0]} – {iddia[3][1]}',iddia[3],'',''),(f'{iddia[4][0]} – {iddia[4][1]}',iddia[4],f'{iddia[4][0]}, {iddia[4][1]} bölgelerinde görülür; eşleştirme doğrudur.','bilgi')],
 'D',lambda t:ES[t[0]]!=t[1],'Yanlış eşleştirilen bitki topluluğu ve iklim.',
 'Yanlış eşleşmeyi bulmak için her birinin doğru iklimini hatırla.',
 [B('Bitki toplulukları ve iklim','maki: Akdeniz · yağmur ormanı: ekvatoral · tundra (yosun, likenler): tundra iklimi · savan (uzun otlar, seyrek ağaç): savan iklimi · step (bozkır): karasal'),B('Ekvatoral iklimde','yıl boyu yağış ve sıcaklık nedeniyle yağmur ormanları gelişir')],
 [A('Doğru eşleşmeleri yaz','Her bitki topluluğunun doğru iklimini bilgi kutusundan hatırla.','maki: Akdeniz · yağmur ormanı: ekvatoral'),
  A('Şıkları kontrol et','Maki, yağmur ormanı, tundra ve step eşleştirmeleri doğrudur.','A, B, C, E: doğru'),
  A('Yanlışı bul','Savan ekvatoral iklimde değil, savan ikliminde görülür.','D: yanlış')],
 'Savanı savan iklimiyle, yağmur ormanını ekvatoral iklimle eşle.')

# 0003 orta · A (akarsu rejimi)
V=[40,45,90,210,330,300,120,70,55,50,45,40]
def rejim(v):
    m=v.index(max(v))
    assert max(v)>3*min(v)
    return 'kar' if m in (2,3,4,5) else 'kis' if m in (11,0,1) else 'yaz' if m in (6,7,8) else 'diger'
assert rejim(V)=='kar' and V.index(max(V))==4
Q.soru('0003','K-SUT-03','orta','Akarsuyun aylık debi grafiğinden beslenme kaynağını belirler.',3,'grafik',
 'Aşağıda, Türkiye’de yüksek dağlardan doğan bir akarsuyun aylık ortalama debi (akış miktarı) grafiği verilmiştir.\nGrafiğe göre bu akarsuyun başlıca beslenme kaynağı aşağıdakilerden hangisidir?',
 [('İlkbaharda kar erimesi','kar','',''),
  ('Kış yağmurları','kis','Kış yağmuruyla beslenen akarsuyun debisi aralık–şubatta en yüksek olurdu; grafikte bu aylar en düşük debili aylardır.','bilgi'),
  ('Yaz yağmurları','yaz','Yaz yağmuruyla beslenen akarsuyun debisi temmuz–ağustosta tepe yapardı; grafikteki doruk mayıstadır.','bilgi'),
  ('Yer altı suyu (düzenli kaynak)','kaynak','Yer altı suyuyla beslenen akarsuyun debisi yıl boyu hemen hemen sabittir; grafikte 40 ile 330 arasında büyük değişim vardır.','dikkat'),
  ('Yaz sonunda buzul erimesi','buzul','Buzul erimesi en çok temmuz–ağustosta olur; grafikte debi mayıstan sonra düşmektedir.','bilgi')],
 'A',lambda t:t==rejim(V),'Akarsuyun başlıca beslenme kaynağı.',
 'Debinin en yüksek olduğu ayı bul ve o ayda hangi su kaynağının bol olduğunu düşün.',
 [B('Akarsu rejimi','akarsuyun debisinin yıl içindeki değişimidir · kar erimesiyle beslenenlerde debi ilkbahar–yaz başında yükselir · yağmurla beslenenlerde yağışın bol olduğu mevsimde yükselir')],
 [A('Grafiği oku','Debi mart–mayıs arasında hızla artıyor ve mayıs ayında en yüksek (330 m³/sn) oluyor.','en yüksek: mayıs · en düşük: ocak (40)'),
  A('Mevsimi yorumla','Kışın debi düşük olduğu için kış yağmuru kaynak değildir. Yaz ortası yağış ya da buzul da değildir; doruk ilkbahardadır.','kış: düşük · temmuzdan sonra: azalıyor'),
  A('Kaynağı belirle','Yüksek dağlarda kışın biriken kar, ilkbaharda erir ve debiyi artırır.','kar erimesi')],
 'Debi dorukta ilkbahar ise kar erimesini, kış ise yağmuru düşün.',sekil=cubuk(V,400,100,'m³/sn'))

# 0004 zor · C
Z={'K':'Podzol','L':'Çernezyom (kara toprak)','M':'Laterit'}
OZ={'K':'K bölgesinde iğne yapraklı ormanların altında soğuk ve nemli iklimde yıkanma fazladır; toprak asidik ve verimsiz podzoldur.','L':'L bölgesinde otsu bozkır bitkilerinin bıraktığı humus toprağı koyu renkli ve verimli çernezyom yapar.','M':'M bölgesinde yıl boyu sıcak ve çok yağışlı ortamda aşırı yıkanma olur; demir ve alüminyum oksitli kırmızı laterit oluşur.'}
dog=(Z['K'],Z['L'],Z['M'])
perms=[(Z['L'],Z['K'],Z['M']),(Z['K'],Z['M'],Z['L']),dog,(Z['M'],Z['L'],Z['K']),(Z['L'],Z['M'],Z['K'])]
opt=[]
for p in perms:
    cel='' if p==dog else ' '.join(f'{k} için {p[i].split(" (")[0]} seçilmiş; oysa '+OZ[k] for i,k in enumerate('KLM') if p[i]!=dog[i])
    opt.append((' – '.join(f'{k}: {v}' for k,v in zip('KLM',p)),p,cel,'bilgi'))
Q.soru('0004','K-SUT-04','orta','Bitki örtüsü ve iklim özelliklerinden zonal toprak tiplerini belirler.',4,'yeni nesil',
 'Bir ziraat mühendisi, üç bölgeden toprak örneği toplamıştır:\nK bölgesi: İğne yapraklı sık ormanlar, uzun ve soğuk kış, yıkanması fazla ve asidik toprak\nL bölgesi: Yarı nemli iklim, otsu bozkır bitkileri, humusu bol ve koyu renkli toprak\nM bölgesi: Yıl boyu sıcak ve çok yağışlı iklim, yağmur ormanı, aşırı yıkanmış kırmızı toprak\nBu bölgelerde oluşan zonal toprak tipleri aşağıdakilerden hangisinde doğru verilmiştir?',
 opt,'C',lambda t:t==dog,'K, L ve M bölgelerinin zonal toprak tipleri.',
 'Her bölgenin bitki örtüsünü ve yıkanma durumunu toprak tipiyle eşleştir.',
 [B('Zonal topraklar','iklim ve bitki örtüsüne bağlı, geniş alanlarda oluşur · podzol: iğne yapraklı orman, asidik, yıkanmış · çernezyom: step, humusu bol, kara toprak · laterit: ekvatoral ve savan bölgeleri, aşırı yıkanma, kırmızı')],
 [A('İpuçlarını ayır','Her bölgede bitki örtüsü, yıkanma ve renk bilgisi verilmiş.','K: orman + asidik · L: bozkır + humus · M: yağmur ormanı + kırmızı'),
  A('K ve M’yi eşle','İğne yapraklı orman ve asidik, yıkanmış toprak podzoldur. Sıcak-nemli ortamda kırmızı, yıkanmış toprak lateritidir.','K: podzol · M: laterit'),
  A('L’yi eşle','Bozkırın bol humuslu, koyu toprağı çernezyomdur (kara toprak).','L: çernezyom'),
  A('Sıralamayı seç','K, L, M sırasıyla podzol, çernezyom ve laterittir.','Podzol, Çernezyom, Laterit')],
 'Orman altında asidik podzol, bozkırda humuslu çernezyom, sıcak-nemli ortamda kırmızı laterit.')
Q.bitir()
