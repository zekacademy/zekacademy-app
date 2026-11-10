import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim as H
from _hafif_kim import *
H.KONU='Maddenin Halleri'
P=Parti('haller','Maddenin Halleri','kim|Maddenin Halleri',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (sıvılar, hâl değişimleri, gazlar) · MEB 9–10. sınıf'
kart('K-HALL-01','Hâllerin özellikleri','Katıda şekil ve hacim belirli, sıvıda yalnız hacim belirli, gazda ikisi de kabın tamamına bağlıdır.','Gazın belirli hacmi olduğunu sanmak.','kolay','öncüllü',2,'kim-hl-ozellik','Maddenin hâllerinin özellikleri',KY)
kart('K-HALL-02','Hâl değişimi ve ısı','Buharlaşma, erime, süblimleşme ısı alır; yoğuşma, donma, kırağılaşma ısı verir.','Buharlaşmayı ısı veren olay sanmak.','orta','öncüllü',3,'kim-hl-isi','Hâl değişimlerinde ısı alışverişi',KY)
kart('K-HALL-03','Isıtma eğrisi','Sıcaklık sabit kaldığı aralıklarda hâl değişimi vardır ve iki hâl birlikte bulunur.','Sabit sıcaklık aralığında ısı alınmadığını sanmak.','orta','grafik',3,'kim-hl-egri','Isıtma grafiğini yorumlama',KY)
kart('K-HALL-04','Buhar basıncı ve kaynama','Aynı sıcaklıkta buhar basıncı büyük olan sıvının kaynama noktası düşüktür.','Buhar basıncı ile kaynama noktasını doğru orantılı sanmak.','orta','tablo',3,'kim-hl-buhar','Buhar basıncından kaynama noktası sırası',KY)
kart('K-HALL-05','Sıvıların özellikleri','Yüzey gerilimi, viskozite, buhar basıncı ve kaynama noktasının sıcaklık, miktar ve dış basınçla ilişkisi.','Viskozitenin sıcaklıkla arttığını sanmak.','zor','öncüllü',4,'kim-hl-sivi','Sıvıların özellikleri',KY)
kart('K-HALL-06','Buhar basıncı ve dış basınç','Sıvı, buhar basıncı dış basınca eşit olunca kaynar; dış basınç azalırsa kaynama noktası düşer. Buhar basıncı–sıcaklık grafiğinde kaynama noktası, dış basınç doğrusunun eğriyi kestiği sıcaklıktır.','Kaynama noktasını yalnız 1 atm değerinden okumak; dış basınç değişince değişeceğini unutmak.','zor','grafik',4,'kim-hl-bp-grafik','Buhar basıncı–sıcaklık grafiğinden kaynama noktası',KY)
# ---- 0001
d={'I':(True,'katı hâlde madde belirli şekil ve hacme sahiptir'),
   'II':(True,'sıvılar bulundukları kabın şeklini alır ve hacimleri belirlidir'),
   'III':(False,'gazların hacmi belirli değildir, bulundukları kabın tamamını doldururlar')}
r=onc(d,[('I','II'),('I',),('II',),('III',),('I','III')])
mk(P,'0001',tipId='kim-hl-ozellik',tip='Maddenin hâllerinin özellikleri',z='kolay',alt='Sıvılar',kaz='Katı, sıvı ve gaz hâllerinin genel özelliklerini ayırt eder.',kalip='öncüllü',adim=2,
 kart='K-HALL-01 (hâllerin özellikleri) · şekil ve hacim',
 metin='Maddenin hâlleriyle ilgili şunlar söyleniyor.\nI. Katılar belirli şekle ve belirli hacme sahiptir.\nII. Sıvılar bulundukları kabın şeklini alır, hacimleri belirlidir.\nIII. Gazların belirli bir hacmi vardır.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifadeler.',
 ip=['Hangi hâlde şekil, hangi hâlde hacim kabın özelliğine bağlıdır?'],
 bilgi=[B('Hâllerin özellikleri','Katı: şekli ve hacmi belirlidir. Sıvı: hacmi belirli, şekli kabına bağlıdır. Gaz: ne şekli ne hacmi belirlidir, bulunduğu kabın tamamını doldurur. Örnek: bir balondaki hava balonun şeklini alır')],
 ad=[A('Katılar','Tanecikler sıkı dizilmiştir.','I: doğru'),A('Sıvılar','Tanecikler birbiri üzerinde kayar, hacim sabit kalır.','II: doğru'),A('Gazlar','Tanecikler arası çok uzaktır, gaz kabın tamamına yayılır.','III: yanlış'),A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve II')],
 puf='Gazın belirli şekli de hacmi de yoktur; sıvının yalnız hacmi belirlidir.')
# ---- 0002
d={'I':(True,'su buharı yoğuşurken ısı verir'),
   'II':(False,'ıslak çamaşır kururken su buharlaşır ve buharlaşma ısı alan bir olaydır'),
   'III':(True,'su donarken ortama ısı verir')}
r=onc(d,[('I',),('II',),('I','III'),('II','III'),('I','II')])
mk(P,'0002',tipId='kim-hl-isi',tip='Hâl değişimlerinde ısı alışverişi',z='orta',alt='Sıvılar',kaz='Günlük olaylardaki hâl değişimlerini ısı alan ya da ısı veren olarak sınıflandırır.',kalip='öncüllü',adim=3,
 kart='K-HALL-02 (hâl değişimi ve ısı) · yoğuşma, buharlaşma, donma',
 metin='Aşağıdaki olaylar veriliyor.\nI. Soğuk bardağın dış yüzeyinde su damlacıklarının oluşması\nII. Islak çamaşırın kuruması\nIII. Gölün yüzeyindeki suyun donması\nBunlardan hangileri ortama ısı vererek gerçekleşir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Isı veren hâl değişimleri.',
 ip=['Her olayın hangi hâl değişimi olduğunu adlandır; sonra ısı alan mı, veren mi olduğuna karar ver.'],
 bilgi=[B('Hâl değişimi ve ısı','Erime, buharlaşma ve süblimleşme ısı alır. Donma, yoğuşma ve kırağılaşma ısı verir. Örnek: buzun erimesi ısı alır')],
 ad=[A('Olayları adlandır','Her olaydaki hâl değişimi belirlenir.','I: yoğuşma · II: buharlaşma · III: donma'),A('Isı alışverişi','Gaz→sıvı ve sıvı→katı ısı verir; sıvı→gaz ısı alır.','I: verir · II: alır · III: verir'),A('Sonuç','Isı verenler seçilir.','I ve III')],
 puf='Tanecikler birbirine yaklaşıyorsa (gaz→sıvı→katı) olay ısı verir, uzaklaşıyorsa ısı alır.')
# ---- 0003
pts=[(0,10),(2,30),(5,30),(8,90),(13,90),(15,110)]
X=lambda t:40+t*14; Y=lambda T:170-T*1.35
yol=' '.join(('M' if i==0 else 'L')+f'{X(t):.1f} {Y(T):.1f}' for i,(t,T) in enumerate(pts))
sk=svg(290,205,L(40,170,40,18,1.6)+L(40,170,265,170,1.6)
   +f'<path d="{yol}" stroke-width="2.6" style="stroke:{G.ACC}"/>'
   +''.join(L(X(t),170,X(t),175,1.4)+T(X(t),188,str(t),size=10) for t in (0,2,5,8,13,15))
   +''.join(L(35,Y(v),40,Y(v),1.4)+T(33,Y(v)+4,str(v),anchor='end',size=10) for v in (10,30,90,110))
   +T(60,14,'Sıcaklık (°C)',size=10,anchor='start')+T(265,200,'Zaman (dk)',size=10,anchor='end'))
d={'I':(True,'3. dakika sıcaklığın sabit kaldığı erime aralığındadır; madde katı ve sıvı karışımıdır'),
   'II':(False,'10. dakika kaynama aralığındadır; madde sıvı ve gaz birlikte bulunur, yalnız gaz değildir'),
   'III':(True,'5–8. dakikalarda sıcaklık arttığı için verilen ısı sıvının sıcaklığını yükseltir')}
r=onc(d,[('II',),('I',),('III',),('I','II'),('I','III')])
mk(P,'0003',tipId='kim-hl-egri',tip='Isıtma grafiğini yorumlama',z='orta',alt='Sıvılar',kaz='Saf maddenin ısıtma grafiğinden hâl ve hâl değişimi aralıklarını yorumlar.',kalip='grafik',adim=3,
 kart='K-HALL-03 (ısıtma eğrisi) · katıdan gaza ısıtma grafiği',
 metin='Katı hâldeki saf bir X maddesi sabit güçlü bir ısıtıcıyla ısıtılıyor ve sıcaklığın zamanla değişimi şekildeki grafikte verilmiştir.\nI. 3. dakikada X hem katı hem sıvı hâldedir.\nII. 10. dakikada X yalnız gaz hâldedir.\nIII. 5–8. dakikalar arasında verilen ısı X sıvısının sıcaklığını yükseltmek için kullanılır.\nBuna göre hangileri doğrudur?',
 sekil=sk,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Grafiğe göre doğru olan öncüller.',
 ip=['Grafikte sıcaklığın sabit kaldığı aralıklarda hâl değişimi olur; arttığı aralıklarda tek hâl vardır.'],
 bilgi=[B('Isıtma grafiği','Saf maddede hâl değişimi sırasında sıcaklık sabit kalır ve ısı hâl değiştirmeye harcanır. Sıcaklık yükseliyorsa madde tek hâldedir. Örnek: buz erirken 0 °C’de sabit kalır')],
 ad=[A('Sabit aralıkları bul','Sıcaklık 2–5 dk 30 °C’de ve 8–13 dk 90 °C’de sabit.','2–5 dk: erime · 8–13 dk: kaynama'),A('I. öncül','3. dk erime aralığındadır.','katı + sıvı → I: doğru'),A('II. öncül','10. dk kaynama aralığındadır.','sıvı + gaz → II: yanlış'),A('III. öncül','5–8. dk sıcaklık 30 °C’den 90 °C’ye çıkıyor.','sıvı ısınıyor → III: doğru · Sonuç: I ve III')],
 puf='Düz (yatay) aralık hâl değişimini, eğimli aralık tek hâlde ısınmayı gösterir.')
# ---- 0004
bp={'X':150,'Y':40,'Z':90}
sir=sorted(bp,key=lambda k:-bp[k])   # buhar basıncı büyükten küçüğe: X,Z,Y -> kaynama küçükten büyüğe
kay=' > '.join(sir[::-1]); assert kay=='Y > Z > X'
S=[('X > Z > Y',False,'buhar basıncı en yüksek olan X’in kaynama noktası en düşüktür; sıralama ters kurulmuştur'),
   ('Y > Z > X',True,''),
   ('Z > Y > X',False,'Y’nin buhar basıncı en düşük olduğundan kaynama noktası en yüksektir'),
   ('X > Y > Z',False,'buhar basıncı ile kaynama noktası ters orantılıdır; X en düşük kaynama noktasına sahiptir'),
   ('Y > X > Z',False,'X’in buhar basıncı Z’den yüksek olduğu için kaynama noktası Z’den düşüktür')]
r=tek(S,True)
mk(P,'0004',tipId='kim-hl-buhar',tip='Buhar basıncından kaynama noktası sırası',z='orta',alt='Sıvılar',kaz='Aynı sıcaklıktaki buhar basınçlarından sıvıların kaynama noktalarını karşılaştırır.',kalip='tablo',adim=3,
 kart='K-HALL-04 (buhar basıncı) · X, Y, Z sıvıları',
 metin='Saf X, Y ve Z sıvılarının aynı sıcaklıktaki buhar basınçları tabloda verilmiştir.\nSıvı | Buhar basıncı (mmHg)\nX | 150\nY | 40\nZ | 90\nBu sıvıların aynı dış basınçtaki kaynama noktaları arasındaki ilişki aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Kaynama noktalarının büyükten küçüğe sıralaması.',
 ip=['Aynı sıcaklıkta kolay buharlaşan sıvının tanecikleri arasındaki çekim zayıftır.'],
 bilgi=[B('Buhar basıncı ve kaynama','Aynı sıcaklıkta buhar basıncı büyük olan sıvı kolay buharlaşır; çekim kuvvetleri zayıftır ve kaynama noktası düşüktür. Örnek: ağız açık kolonya, sudan daha çabuk buharlaşır')],
 ad=[A('Buhar basınçlarını sırala','En büyük olan en kolay buharlaşır.','X (150) > Z (90) > Y (40)'),A('Kaynama noktasına çevir','Buhar basıncı ile kaynama noktası ters sıralanır.','kaynama noktası: Y > Z > X'),A('Şıkları karşılaştır','Sıralamayı veren şık seçilir.','B')],
 puf='Buhar basıncı yüksek olan sıvının kaynama noktası düşüktür; sıralama ters çevrilir.')
# ---- 0005
d={'I':(True,'yüzeydeki moleküller içeriden aşağı doğru çekildiği için yüzey gerilimi oluşur'),
   'II':(False,'sıcaklık arttıkça sıvıların viskozitesi azalır'),
   'III':(False,'dış basınç azaldıkça kaynama noktası düşer (yüksek yerlerde su daha düşük sıcaklıkta kaynar)'),
   'IV':(True,'sıcaklık sabitken sıvının buhar basıncı sıvı miktarına ve kabın hacmine bağlı değildir')}
r=onc(d,[('I','II'),('II','III'),('III','IV'),('I','IV'),('II','IV')])
mk(P,'0005',tipId='kim-hl-sivi',tip='Sıvıların özellikleri',z='zor',alt='Sıvılar',kaz='Sıvıların yüzey gerilimi, viskozite, kaynama noktası ve buhar basıncı ile ilgili ifadeleri değerlendirir.',kalip='öncüllü',adim=4,
 kart='K-HALL-05 (sıvıların özellikleri) · yüzey gerilimi, viskozite, kaynama noktası, buhar basıncı',
 metin='Sıvıların özellikleriyle ilgili aşağıdaki ifadeler veriliyor.\nI. Yüzey gerilimi, sıvı yüzeyindeki moleküllerin iç kısma doğru çekilmesinden kaynaklanır.\nII. Sıcaklık arttıkça sıvıların viskozitesi artar.\nIII. Dış basınç azaldıkça bir sıvının kaynama noktası yükselir.\nIV. Sıcaklık sabitken bir sıvının buhar basıncı, sıvının miktarına bağlı değildir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifadeler.',
 ip=['Viskozitenin sıcaklığa, buhar basıncının miktara, kaynama noktasının dış basınca nasıl bağlı olduğunu tek tek düşün.'],
 bilgi=[B('Sıvı özellikleri','Yüzey gerilimi: yüzeyin gerilmiş zar gibi davranması. Viskozite: akmaya karşı direnç, sıcaklık artınca azalır. Kaynama noktası: sıvının buhar basıncının dış basınca eşit olduğu sıcaklıktır; dış basınç azalırsa kaynama noktası düşer. Buhar basıncı yalnız sıcaklık ve sıvı türüne bağlıdır')],
 ad=[A('I. öncül','Yüzeydeki moleküller yalnız aşağıdan ve yanlardan çekilir.','I: doğru'),A('II. öncül','Sıcaklık artınca moleküller kolay kayar, viskozite azalır.','II: yanlış'),A('III. öncül','Dış basınç azalınca buhar basıncı daha düşük sıcaklıkta dış basınca ulaşır.','III: yanlış'),A('IV. öncül','Buhar basıncı sıvı miktarına ve kap hacmine bağlı değildir.','IV: doğru · Sonuç: I ve IV')],
 puf='Viskozite sıcaklıkla azalır; buhar basıncı yalnız sıvı türü ve sıcaklığa bağlıdır, miktara değil; dış basınç azalınca kaynama noktası düşer.')
# ---- 0006
# buhar basıncı P(T)=760*2^((T-Tk)/h): Tk 760 mmHg'deki kaynama noktası, h basıncın 2 katına çıkması için gereken sıcaklık artışı
PA={'X':(60,20),'Y':(80,25)}
Pf=lambda k,T:760*2**((T-PA[k][0])/PA[k][1])
Tb=lambda k,P:PA[k][0]+PA[k][1]*__import__('math').log2(P/760)
import math
assert abs(Tb('X',760)-60)<1e-9 and abs(Tb('Y',760)-80)<1e-9
assert abs(Tb('X',380)-40)<1e-9 and abs(Tb('Y',380)-55)<1e-9      # 380 mmHg: X 40, Y 55
fark760=Tb('Y',760)-Tb('X',760); fark380=Tb('Y',380)-Tb('X',380); assert (fark760,fark380)==(20,15)
assert all(Pf('X',t)>Pf('Y',t) for t in range(20,91))            # aynı sıcaklıkta X daha uçucu
assert abs(Pf('X',40)-380)<1e-9 and abs(Pf('Y',55)-380)<1e-9
X6=lambda t:46+(t-20)*3.3; Y6=lambda p:170-p*0.145
def egri(k):
    pt=[(t,Pf(k,t)) for t in range(20,91) if Pf(k,t)<=1000]
    tt=PA[k][0]+PA[k][1]*math.log2(1000/760); pt.append((tt,1000.0))
    return 'M'+' L'.join(f'{X6(t):.1f} {Y6(p):.1f}' for t,p in pt)
gr='stroke-dasharray="3 3" style="stroke-opacity:.35"'
sk6=svg(300,215,L(46,170,46,18,1.6)+L(46,170,285,170,1.6)
   +''.join(L(X6(t),20,X6(t),170,0.8,gr) for t in range(25,91,5))
   +''.join(L(46,Y6(p),285,Y6(p),1.0,gr) for p in (380,760))
   +f'<path d="{egri("X")}" stroke-width="2.6" style="stroke:{G.ACC}"/>'
   +f'<path d="{egri("Y")}" stroke-width="2.6"/>'
   +''.join(L(X6(t),170,X6(t),175,1.4)+T(X6(t),188,str(t),size=10) for t in range(20,91,10))
   +''.join(L(41,Y6(p),46,Y6(p),1.4)+T(38,Y6(p)+4,str(p),anchor='end',size=10) for p in (380,760))
   +T(X6(60)-8,Y6(1000)+16,'X',size=12,anchor='end',bold=True,renk=G.ACC)+T(X6(82),Y6(Pf('Y',82))-10,'Y',size=12,anchor='end',bold=True)
   +T(50,12,'Buhar basıncı (mmHg)',size=10,anchor='start')+T(285,205,'Sıcaklık (°C)',size=10,anchor='end'))
d={'I':(True,'aynı sıcaklıkta X’in buhar basıncı Y’ninkinden büyüktür; grafikte X eğrisi Y eğrisinin üstündedir'),
   'II':(False,'X’in kaynama noktası daha düşük olduğundan X’in tanecikleri arası çekim kuvveti Y’ninkinden zayıftır'),
   'III':(True,'380 mmHg doğrusu X eğrisini 40 °C’de, Y eğrisini 55 °C’de keser'),
   'IV':(False,'dış basınç 380 mmHg’ye düşünce kaynama noktaları farkı 20 °C’den 15 °C’ye azalır')}
r=onc(d,[('I','III'),('I',),('II','IV'),('I','II'),('III','IV')])
mk(P,'0006',tipId='kim-hl-bp-grafik',tip='Buhar basıncı–sıcaklık grafiğinden kaynama noktası',z='zor',alt='Sıvılar',kaz='Buhar basıncı–sıcaklık grafiğinden farklı dış basınçlardaki kaynama noktalarını okuyup yorumlar.',kalip='grafik',adim=4,
 kart='K-HALL-06 (buhar basıncı ve dış basınç) · X ve Y sıvıları, 760 ve 380 mmHg doğruları',
 metin='Saf X ve Y sıvılarının buhar basıncının sıcaklıkla değişimi şekildeki grafikte verilmiştir.\nI. Aynı sıcaklıkta X’in buhar basıncı Y’ninkinden büyüktür.\nII. X’in tanecikleri arasındaki çekim kuvveti Y’ninkinden daha büyüktür.\nIII. Dış basıncın 380 mmHg olduğu bir ortamda X 40 °C’de, Y 55 °C’de kaynar.\nIV. Dış basınç 760 mmHg’den 380 mmHg’ye düşürülürse X ile Y’nin kaynama noktaları arasındaki fark artar.\nBuna göre hangileri doğrudur?',
 sekil=sk6,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Grafiğe göre doğru olan öncüller.',
 ip=['Kaynama noktası, buhar basıncının dış basınca eşit olduğu sıcaklıktır; dış basıncı gösteren yatay doğruyu eğrilerle kesiştir.'],
 bilgi=[B('Kaynama noktası ve dış basınç','Sıvı, buhar basıncı dış basınca eşit olunca kaynar. Grafikte dış basınç değerinden çizilen yatay doğrunun eğriyi kestiği nokta kaynama noktasıdır; dış basınç azalırsa kaynama noktası düşer. Örnek: yüksek yerlerde su 100 °C’den düşük sıcaklıkta kaynar'),B('Buhar basıncı ve çekim kuvveti','Aynı sıcaklıkta buhar basıncı büyük olan sıvı daha uçucudur; tanecikleri arası çekim kuvveti zayıftır ve kaynama noktası düşüktür')],
 ad=[A('Kaynama noktalarını oku','760 mmHg ve 380 mmHg doğrularını X ve Y eğrileriyle kesiştir.','760 mmHg: X 60 °C, Y 80 °C · 380 mmHg: X 40 °C, Y 55 °C'),A('I ve II','X eğrisi Y’nin üstündedir; X daha uçucudur, çekim kuvveti daha zayıftır.','I: doğru · II: yanlış'),A('III ve IV','380 mmHg okumaları 40 ve 55 °C; fark 80 − 60 = 20 °C iken 55 − 40 = 15 °C olur.','III: doğru · IV: yanlış'),A('Sonuç','Doğru olanlar toplanır.','Sonuç: I ve III')],
 puf='Kaynama noktasını sorarken önce dış basıncı bul; o basınçtan çizdiğin yatay doğrunun eğriyi kestiği sıcaklığı oku.')
bitir(P,'haller','kim|Maddenin Halleri')
