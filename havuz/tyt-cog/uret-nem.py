"""TYT Coğrafya · Nem, Yağış ve Buharlaşma: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_a import *
KY='ÖSYM 2018–2026 (nem, yağış türleri, buharlaşma) · MEB 9. sınıf coğrafya'
KARTLAR={
 'K-NEM-01':dict(alt='Yağış türleri',fikir='Yağışlar oluşumuna göre konveksiyonel, yamaç ve cephe yağışı olarak ayrılır; yükselme nedeni ayırt edicidir.',tuzak='Yağış şeklini (dolu, kar) oluşum türü sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='cg-nem-tur',kaynak=KY),
 'K-NEM-02':dict(alt='Nem ve yoğunlaşma hesabı',fikir='Soğuyan havanın taşıyabileceği buhar miktarı azalır; mutlak nem kapasiteyi aşan kısım yoğunlaşır.',tuzak='Kapasite farkını yoğunlaşan miktar sanmak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='cg-nem-hesap',kaynak=KY),
 'K-NEM-03':dict(alt='Buharlaşmayı etkileyen etkenler',fikir='Sıcaklık ve yüzey genişliği buharlaşmayı artırır; havanın bağıl neminin yüksek olması azaltır.',tuzak='Nemli havada buharlaşmanın arttığını sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='cg-nem-buharlasma',kaynak=KY),
 'K-NEM-04':dict(alt='Yamaç yağışı ve yağmur gölgesi',fikir='Rüzgârüstünde yükselen hava yağış bırakır; rüzgâraltında alçalırken ısınır, bağıl nemi azalır ve yağış azdır.',tuzak='Alçalan havanın soğuduğunu sanmak.',zorluk='orta',kalip='şekilli',adim=4,tipId='cg-nem-yamac',kaynak=KY),
}
TIPLER={'cg-nem-tur':'Yağış türleri','cg-nem-hesap':'Yoğunlaşma miktarı hesabı','cg-nem-buharlasma':'Buharlaşmayı etkileyen etkenler','cg-nem-yamac':'Yamaç yağışı ve rüzgâraltı (şekil)'}
Q=Konu('nem','Nem, Yağış ve Buharlaşma','cog|Nem, Yağış ve Buharlaşma',4,KARTLAR,TIPLER,{'kolay':1,'orta':3})

# 0001 kolay · C
Q.soru('0001','K-NEM-01','kolay','Yağışları oluşum biçimine göre ayırt eder.',2,'düz',
 'Güneş ışınlarıyla ısınan nemli havanın yükselip soğuması ve yoğunlaşması sonucu oluşan yağış türü aşağıdakilerden hangisidir?',
 [('Yamaç (orografik) yağışı','yamac','Yamaç yağışında havayı yükselten etken dağ yamacıdır; burada yükselmenin nedeni ısınmadır.','bilgi'),
  ('Cephe (frontal) yağışı','cephe','Cephe yağışında sıcak hava, soğuk havanın üzerine çıkarak yükselir; ısınma nedeni değildir.','bilgi'),
  ('Konveksiyonel yağış','konv','',''),
  ('Dolu','dolu','Dolu bir yağış şeklidir (buz taneleri); yağışın oluşum türü değildir.','dikkat'),
  ('Çiy','ciy','Çiy yağış sayılmaz; soğuyan yüzeyde havadaki buharın yoğunlaşmasıdır.','bilgi')],
 'C',lambda t:t=='konv','Isınmayla yükselen havanın oluşturduğu yağış türü.',
 'Havayı yükselten şey dağ mı, soğuk hava mı, yoksa yüzeyin ısınması mı?',
 [B('Yağış türleri (oluşuma göre)','konveksiyonel: ısınan hava yükselir · yamaç: hava dağ yamacında yükselir · cephe: sıcak hava soğuk havanın üzerine çıkar')],
 [A('Yükselme nedenini bul','Soruda havanın Güneş’le ısınıp yükseldiği söyleniyor.','neden: ısınma'),
  A('Yağış türlerini eşle','Dağ yamacı yamaç yağışını, hava kütlelerinin karşılaşması cephe yağışını doğurur. Dolu ve çiy oluşum türü değildir.','yamaç: dağ · cephe: hava kütleleri'),
  A('Sonucu seç','Isınmayla yükselen havanın yağışı konveksiyonel yağıştır.','konveksiyonel')],
 'Yağış türünü, havayı yükselten etkene bakarak adlandır.')

# 0002 orta · B
kap1,kap2,mut=24,12,20
yog=mut-kap2; assert yog==8 and kap1-kap2==12 and kap1-mut==4
Q.soru('0002','K-NEM-02','orta','Soğuyan havada kapasiteyi aşan su buharı miktarını hesaplar.',3,'hikâyeli',
 '1 m³ hava 25 °C’de en fazla 24 g, 15 °C’de en fazla 12 g su buharı taşıyabilmektedir.\n25 °C’de 1 m³’ünde 20 g su buharı bulunan bir hava kütlesi 15 °C’ye soğuduğunda, 1 m³ havadan kaç g su buharı yoğunlaşır?',
 [('4','4','25 °C’deki boşluğu (24 − 20) yoğunlaşan miktar sanmış.','islem'),
  ('8','8','',''),
  ('12','12','İki sıcaklıktaki kapasite farkını (24 − 12) bulmuş; oysa havada başlangıçta 24 g değil 20 g buhar vardı.','dikkat'),
  ('20','20','Havadaki bütün buharın yoğunlaştığını sanmış; 15 °C’de hava 12 g taşıyabilir.','bilgi'),
  ('24','24','25 °C’deki kapasiteyi yoğunlaşan miktar saymış.','bilgi')],
 'B',lambda t:t=='8','Yoğunlaşan su buharı miktarı (g).',
 'Soğuyan havanın taşıyabileceği en fazla buhar miktarını yeni sıcaklıkta bul.',
 [B('Kapasite ve yoğunlaşma','sıcaklık düştükçe havanın taşıyabileceği en fazla buhar miktarı azalır · havada taşınamayan fazla buhar yoğunlaşır (ör. 15 g içeren hava, kapasite 10 g olunca 5 g yoğunlaştırır)')],
 [A('Yeni kapasiteyi oku','15 °C’de hava en fazla 12 g buhar taşıyabilir.','15 °C kapasitesi: 12 g'),
  A('Fazlayı bul','Havadaki buhar 20 g idi; 12 g’ı taşınabilir, geri kalan taşınamaz.','20 − 12 = 8 g'),
  A('Sonucu yaz','Taşınamayan 8 g su buharı yoğunlaşarak sıvı suya dönüşür.','8 g yoğunlaşır')],
 'Yoğunlaşan miktar = havadaki buhar − yeni sıcaklıktaki kapasite.')

# 0003 orta · C
Q.oncul('0003','K-NEM-03','orta','Buharlaşma miktarını artıran etkenleri ayırt eder.',3,
 'Bir gölün buharlaşma miktarını belirleyen etkenler incelenmektedir.',
 [('Havanın sıcaklığının yüksek olması',True,'Sıcaklık arttıkça su molekülleri hızlanır ve buharlaşma artar.'),
  ('Su yüzeyinin geniş olması',True,'Havayla temas eden yüzey genişledikçe buharlaşan su artar.'),
  ('Havanın bağıl neminin yüksek olması',False,'Hava buharla dolu ise daha az buhar alabilir; buharlaşma azalır.')],
 'Yukarıdakilerden hangileri buharlaşma miktarını artırır?',
 ['Yalnız II','I ve III','I ve II','Yalnız III','I, II ve III'],'C',True,'Buharlaşmayı artıran etkenler.',
 'Hava ne kadar nemliyse daha fazla buhar alabilir mi?',
 [B('Buharlaşma','suyun buhara dönüşmesidir · artıran etkenler: sıcaklık, rüzgâr, geniş su yüzeyi, havanın kuru olması (düşük bağıl nem)')],
 [A('Etkenleri hatırla','Sıcaklık, rüzgâr ve yüzey genişliği buharlaşmayı artırır. Havadaki nem arttıkça buharlaşma azalır.','artıran: sıcaklık, yüzey · azaltan: yüksek nem'),
  A('İfadeleri sına','I ve II artırır. III’te nem yüksek olduğundan buharlaşma artmaz.','I: evet · II: evet · III: hayır'),
  A('Sonuç','Artıran etkenler I ve II.','I ve II')],
 'Buharlaşma için hava “kuru ve sıcak”, yüzey “geniş” ise artar.')

# 0004 orta · A
sk=[]
sk.append('<path d="M10 172 Q40 164 70 172 L10 172 Z" stroke-width="0" style="fill:currentColor;fill-opacity:.12"/>')
sk.append('<path d="M10 172 Q25 166 40 172 T70 172" stroke-width="1.6" fill="none"/>')
sk.append(G._t(38,196,'Deniz',size=11))
sk.append(f'<path d="M70 172 L205 50 L335 172 Z" stroke-width="2" style="fill:currentColor;fill-opacity:.12"/>')
sk.append(f'<path d="M12 120 L58 120" stroke-width="2.4" style="stroke:{G.ACC}"/><path d="M50 114 L60 120 L50 126" stroke-width="2.4" fill="none" style="stroke:{G.ACC}"/>')
sk.append(G._t(36,108,'Nemli hava',size=11,renk=G.ACC))
for ad,x,y in (('K',84,172),('L',140,111),('M',205,50),('N',295,139)):
    sk.append(f'<circle cx="{x}" cy="{y}" r="4.5" style="fill:{G.ACC};stroke:none"/>'+G._t(x+(8 if ad!='N' else 8),y-(6 if ad!='K' else -16),ad,anchor='start',size=14,bold=True))
SK4=G._svg(350,205,''.join(sk))
Q.oncul('0004','K-NEM-04','orta','Dağın rüzgârüstü ve rüzgâraltı yamacında nem ve yağış durumunu yorumlar.',4,
 'Şekilde, denizden esen nemli havanın geçtiği bir dağ ve K, L, M, N noktaları gösterilmiştir.',
 [('Nemli hava K’den L’ye doğru yükselirken soğur ve yoğunlaşarak yağış bırakır.',True,'Yükselen hava soğur, buharın bir kısmı yoğunlaşıp yamaç yağışı olarak düşer.'),
  ('N noktasına inen hava soğuyarak bağıl nemini artırır.',False,'Alçalan hava sıkışarak ısınır; bağıl nemi azalır.'),
  ('N noktasında yıllık yağış miktarının L noktasından az olması beklenir.',True,'Rüzgâraltı yamaçta hava kurumuştur; yağış azdır (yağmur gölgesi).')],
 'Bu ifadelerden hangileri yanlıştır?',
 ['Yalnız II','Yalnız I','Yalnız III','I ve III','II ve III'],'A',False,'Yanlış olan ifadeler.',
 'Hava alçalırken sıkışır mı, genleşir mi? Sıcaklığı ve bağıl nemi bu yönde düşün.',
 [B('Rüzgârüstü ve rüzgâraltı','rüzgârüstü yamaç: hava yükselir, soğur, yoğunlaşır → bol yağış · rüzgâraltı yamaç: hava alçalır, ısınır, bağıl nemi azalır → yağış az (yağmur gölgesi)')],
 [A('Rüzgârüstünü yorumla','K’den L’ye hava yükselir, soğur ve yoğunlaşır. I doğrudur.','K → L: yükselir, soğur → yağış'),
  A('Rüzgâraltını yorumla','Zirveden sonra hava alçalır, sıkışıp ısınır. Isınan havanın bağıl nemi azalır.','N: alçalır → ısınır → bağıl nem azalır'),
  A('İfadeleri değerlendir','II’de “soğuyarak” denmiş; bu yanlıştır. III’te yağmur gölgesi doğru anlatılmıştır.','I: doğru · II: yanlış · III: doğru'),
  A('Sonucu yaz','Soru yanlış olanı soruyor; yalnız II yanlıştır.','Yalnız II')],
 'Alçalan hava ısınır ve kurur; yükselen hava soğur ve yağış bırakır.',sekil=SK4)
Q.bitir()
