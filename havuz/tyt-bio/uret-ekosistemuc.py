"""TYT Biyoloji · Ekosistem · 3. paket (ekosistemuc): 10 soru, kardeş yok, ipucu 1.
Grafik zaman noktaları, besin zinciri sayımı, karbon bütçesi, enerji hesabı ve öncül doğrulukları Python'da hesaplanır/assert edilir; şekiller aynı değerlerden çizilir."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_bio as H
from _hafif_bio3 import *
KONU_='Ekosistem'; UK='bio|Ekosistem'; H.KONU=KONU_
P=Parti('ekosistemuc',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 10. sınıf Ekosistem Ekolojisi'
TIP={'bilesen':('by-ek3-bilesen','Ekosistemin canlı bileşenleri'),'cevre':('by-ek3-cevre','Çevre sorunları ve ekosistem dengesi'),'kaynak':('by-ek3-kaynak','Doğal kaynaklar'),
     'enerji':('by-ek3-enerji','Enerji akışı ve madde döngüsü'),'dongu':('by-ek3-dongu','Karbon döngüsü bütçesi'),'agi':('by-ek3-agi','Besin ağında zincir sayımı'),'tolerans':('by-ek3-tolerans','Tolerans aralığı grafiği')}
def kartla(n,tip,alt,fikir,tuzak,z,kalip,adim):
    kart(f'K-BYEK3-{n}',alt,fikir,tuzak,z,kalip,adim,TIP[tip][0],TIP[tip][1],KY)
def q(no,tip,ad,ne,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[tip][0],tip=TIP[tip][1],kart=f"K-BYEK3-{no[-2:]} ({TIP[tip][1].lower()}) · {ne}",**k)
def F(a,b=1): return Fr(a,b)
AX='tick label style={font=\\footnotesize},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.5pt}'

# ============ 0001 · canlı rolleri tablosu · kolay ============
kartla('01','bilesen','Üretici, tüketici, ayrıştırıcı ayrımı','Üretici fotosentezle kendi besinini yapar; tüketici hazır organik madde alır; ayrıştırıcı da hazır organik madde alır ve ölü organik maddeyi inorganik maddelere dönüştürür.','Hazır besin alan her canlıyı tüketici saymak; ayrıştırıcıyı tüketici sanmak.','kolay','tablo',3)
ROL={'X':('Yapar','Almaz','Yapmaz'),'Y':('Yapmaz','Alır','Yapmaz'),'Z':('Yapmaz','Alır','Yapar')}
def rol(v): return 'üretici' if v[0]=='Yapar' else ('ayrıştırıcı' if v[2]=='Yapar' else 'tüketici')
assert [rol(ROL[k]) for k in 'XYZ']==['üretici','tüketici','ayrıştırıcı']
S1=['X: üretici, Y: tüketici, Z: ayrıştırıcı','X: tüketici, Y: üretici, Z: ayrıştırıcı','X: üretici, Y: ayrıştırıcı, Z: tüketici','X: ayrıştırıcı, Y: tüketici, Z: üretici','X: tüketici, Y: ayrıştırıcı, Z: üretici']
q('0001','bilesen',[A('Tablodaki özellikleri oku','X fotosentez yapar ve hazır besin almaz; Y ve Z hazır besin alır; yalnız Z ayrıştırma yapar.','X: kendi besinini yapar · Y, Z: hazır besin alır'),
   A('Rolleri eşleştir','Kendi besinini yapan üretici, ölü organik maddeyi ayrıştıran ayrıştırıcı, yalnız hazır besin alan tüketicidir.','X: üretici · Y: tüketici · Z: ayrıştırıcı'),
   A('Şıkları ele','Z de hazır besin alır ancak ayrıştırma yaptığı için ayrıştırıcıdır.','Doğru: X–Y–Z sırası üretici, tüketici, ayrıştırıcı')],
 'üç canlının beslenme özellikleri tablosu',z='kolay',alt='Ekosistem Bileşenleri',kaz='Beslenme özelliklerinden canlıların ekosistemdeki rolünü belirler.',kalip='tablo',
 metin='Bir ekosistemde yaşayan X, Y ve Z canlılarının beslenme özellikleri aşağıdaki tabloda verilmiştir. “Hazır besin”, başka canlıların ürettiği organik maddeyi besin olarak almayı; “Ayrıştırma”, ölü canlıların organik maddesini inorganik maddelere dönüştürmeyi ifade etmektedir.\nBuna göre, X, Y ve Z canlıları sırasıyla ekosistemdeki hangi role sahiptir?',
 sekil=tablo_dar(['Canlı','Fotosentez','Hazır besin','Ayrıştırma'],[['X']+list(ROL['X']),['Y']+list(ROL['Y']),['Z']+list(ROL['Z'])]),
 dogru=S1[0],sira=yer('A',S1[0],S1[1:]),
 yan=[(S1[1],'X ve Y yer değiştirmiş: fotosentez yapan X kendi besinini yaptığı için üreticidir, hazır besin alan Y üretici olamaz.','bilgi'),
      (S1[2],'Y ve Z yer değiştirmiş: ayrıştırma yapan Z ayrıştırıcıdır; Y yalnız hazır besin aldığı için tüketicidir.','dikkat'),
      (S1[3],'X ayrıştırıcı sanılmış; oysa X fotosentez yapar, ölü organik maddeyi ayrıştırmaz.','bilgi'),
      (S1[4],'X’i tüketici sanmış; fotosentez yapan canlı üreticidir.','bilgi')],
 istenen='X, Y ve Z’nin ekosistemdeki rolleri.',
 ip=['Her canlının besinini nereden sağladığına ve ölü organik maddeyle ilişkisine bak.'],
 bilgi=[B('Ekosistemin canlı bileşenleri','Üreticiler fotosentez ya da kemosentezle organik madde üretir · Tüketiciler besinini hazır alır · Ayrıştırıcılar ölü canlıları inorganik maddelere dönüştürür')],
 puf='Önce kendi besinini yapanı (üretici) ayır; hazır besin alanlar arasında ayrıştırma yapan ayrıştırıcıdır.')

# ============ 0002 · ötrofikasyon grafiği · orta · öncüllü ============
kartla('02','cevre','Ötrofikasyon zaman grafiği','Sulara karışan besin tuzları algleri çoğaltır; alg ölümleri ayrıştırıcıların çoğalmasına ve çözünmüş oksijenin azalmasına yol açar. Grafikte olayların sırası zaman ekseninden okunur.','Oksijen azalmasını alg çoğalmasıyla aynı anda sanmak; alg ölümünü besin tuzu azalmasına bağlamak.','orta','öncüllü',4)
def s(t,t0,w): return 1/(1+math.exp(-(t-t0)/w))
FOS=lambda t:8+52*s(t,2.5,.4); ALG=lambda t:5+38*s(t,4,.5)*(1-s(t,7,.5)); OKS=lambda t:90-75*s(t,7.6,.3)
ts=[i/20 for i in range(0,201)]
tp=max(ts,key=ALG); assert 5<=tp<=6
def ilk(f,esik,yon): return next(t for t in ts if (f(t)>=esik if yon>0 else f(t)<=esik))
t_fos=ilk(FOS,34,1); t_alg=ilk(ALG,24,1); t_oks=ilk(OKS,80,-1)
assert t_fos<t_alg and t_oks>tp and FOS(9)>=FOS(5)
d2={'I':(True,'Fosfat derişimi yaklaşık 1,5–2. yılda yükselmeye başlar, alg miktarı ise yaklaşık 3. yıldan sonra artar; alg artışı fosfat artışından sonradır.'),
    'II':(False,'Alg miktarı yaklaşık 5,5. yılda en yüksek değerine ulaşır; çözünmüş oksijen ise yaklaşık 6,5. yıldan sonra düşmeye başlar. Azalma alg tepe noktasından önce başlamamıştır.'),
    'III':(False,'Grafikte alglerin azaldığı dönemde fosfat derişimi yüksek kalmıştır; alg ölümlerinin nedeni fosfatın azalması olamaz.')}
r=onc(d2,True,'A')
def cr(f): return ' '.join(f'({t:.2f},{f(t):.1f})' for t in ts[::2])
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=10,ymin=0,ymax=105,xtick={0,2,4,6,8,10},ytick=\\empty,xlabel={Zaman (yıl)},ylabel={Göreli değer},'+AX+']',
   f'\\addplot[black] coordinates {{{cr(FOS)}}};',f'\\addplot[black,densely dashed] coordinates {{{cr(ALG)}}};',f'\\addplot[vurgu] coordinates {{{cr(OKS)}}};',
   '\\node[font=\\normalsize\\bfseries] at (axis cs:8.8,68) {K};\\node[font=\\normalsize\\bfseries] at (axis cs:5.5,50) {L};\\node[font=\\normalsize\\bfseries,vurgu] at (axis cs:1.5,98) {M};','\\end{axis}']
SK2=tk('\n'.join(b),1.0)
q('0002','cevre',[A('Eğrileri tanı','K fosfat derişimi, L alg miktarı, M çözünmüş oksijen miktarıdır.','K: fosfat · L: alg · M: çözünmüş oksijen'),
   adim_onc(d2,'I'),adim_onc(d2,'II'),adim_onc(d2,'III'),sonuc(r,True)],
 'göle gübre karışması, fosfat–alg–oksijen',z='orta',alt='Çevre Sorunları',kaz='Zaman grafiğinden besin tuzu artışının sudaki alg ve oksijen düzeyine etkisini yorumlar.',kalip='öncüllü',
 metin='Tarım alanlarından gübre karışan bir gölde, yıllar içinde fosfat derişimi (K), alg miktarı (L) ve çözünmüş oksijen miktarı (M) ölçülmüş ve sonuçlar grafikte gösterilmiştir. Değerler her eğri için kendi ölçeğinde verilmiştir.\nBuna göre,\nI. Alg miktarındaki artış, fosfat derişimindeki artıştan sonra başlamıştır.\nII. Çözünmüş oksijen miktarındaki azalma, alg miktarının en yüksek değere ulaştığı andan önce başlamıştır.\nIII. Alg miktarının azalmasının nedeni fosfat derişiminin düşmesidir.\nyargılarından hangileri doğrudur?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her eğrinin yükselmeye ya da düşmeye başladığı zamanı karşılaştır ve eğriler arasındaki sıralamayı belirle.'],
 bilgi=[B('Besin tuzları ve oksijen','Azot ve fosfor gibi besin tuzları alglerin çoğalmasını destekler · Canlıların çoğu solunum için sudaki çözünmüş oksijeni kullanır')],
 puf='Sıra sorularında eğrilerin değişime başladığı zamanları yan yana yaz; olaylar o sırayla gerçekleşmiştir.')

# ============ 0003 · yenilenebilir/yenilenemez · kolay · olumsuz ============
kartla('03','kaynak','Yenilenebilir ve yenilenemez kaynak ayrımı','Doğal kaynaklar tükenme hızına göre sınıflanır: güneş, rüzgâr, jeotermal ve biyokütle yenilenebilir; kömür, petrol, doğal gaz ve uranyum yenilenemez (fosil ve madenî) kaynaklardır.','Doğal gazı ve petrolü yenilenebilir sanmak; biyokütleyi yenilenemez saymak.','kolay','tablo',3)
SAT=[('Rüzgâr','Yenilenebilir'),('Doğal gaz','Yenilenebilir'),('Güneş','Yenilenebilir'),('Kömür','Yenilenemez'),('Uranyum','Yenilenemez')]
yanl=[i for i,(k,c) in enumerate(SAT) if (k in('Rüzgâr','Güneş'))!=(c=='Yenilenebilir') or (k in('Kömür','Doğal gaz','Uranyum'))!=(c=='Yenilenemez')]
assert yanl==[1]
S3=[f'{i}. satır' for i in range(1,6)]
q('0003','kaynak',[A('Sınıflandırma ölçütünü hatırla','Kısa sürede doğa tarafından yeniden oluşabilenler yenilenebilir, oluşması milyonlarca yıl sürenler yenilenemezdir.','Ölçüt: yenilenme hızı'),
   A('Satırları tek tek sına','Rüzgâr ve güneş yenilenebilir; kömür ve uranyum yenilenemez; doğal gaz fosil kaynaktır ve yenilenemez.','2. satır hatalı'),A('Sonucu yaz','Yenilenemez olması gereken doğal gaz, tabloda yenilenebilir yazılmıştır.','Cevap: 2. satır')],
 'beş enerji kaynağının sınıflandırma tablosu',z='kolay',alt='Doğal Kaynaklar',kaz='Doğal kaynakları yenilenebilir ve yenilenemez olarak sınıflandırır.',kalip='tablo',
 metin='Bir öğrenci, enerji üretiminde kullanılan beş doğal kaynağı, tükenme hızına göre “yenilenebilir” ve “yenilenemez” olarak sınıflandırıp sonuçları aşağıdaki tabloya yazıyor.\nBuna göre, numaralı satırlardan hangisindeki sınıflandırma yanlıştır?',
 sekil=tablo_dar(['No','Kaynak','Sınıf'],[[str(i+1),k,c] for i,(k,c) in enumerate(SAT)]),
 dogru=S3[1],sira=['1. satır','2. satır','3. satır','4. satır','5. satır'],
 yan=[(S3[0],'Rüzgâr kısa sürede yenilenen, tükenmeyen bir kaynaktır; sınıflandırma doğrudur.','bilgi'),(S3[3],'Kömürün oluşması milyonlarca yıl sürer; yenilenemez olarak sınıflandırılması doğrudur.','bilgi'),
      (S3[2],'Güneş enerjisi tükenmeyen, yenilenebilir bir kaynaktır; satır doğrudur.','bilgi'),(S3[4],'Uranyum madenî bir kaynaktır ve tükenir; yenilenemez sınıflandırması doğrudur.','dikkat')],
 istenen='Sınıflandırması yanlış olan satır.',
 ip=['Her kaynağın yeniden oluşma süresini kullanılma hızıyla karşılaştır.'],
 bilgi=[B('Doğal kaynaklar','Yenilenebilir kaynaklar kullanılma hızından hızlı ya da sürekli yenilenir · Yenilenemez kaynakların oluşumu çok uzun zaman alır, kullanıldıkça azalır')],
 puf='Kaynağın oluşma süresini kullanılma hızıyla karşılaştır.')

# ============ 0004 · enerji akışı / madde döngüsü şeması · orta · öncüllü ============
kartla('04','enerji','Enerji akışı ve madde döngüsü şeması','Enerji ekosisteme güneşten girer, basamaklarda ısı olarak kaybolur ve geri dönmez (tek yönlü akış); madde ise ayrıştırıcılar aracılığıyla inorganik hâle gelip üreticilerce yeniden kullanılır (döngü).','Enerjinin de madde gibi döngüsel kullanıldığını sanmak; güneş enerjisinin tüm canlılarca doğrudan kullanıldığını sanmak.','orta','öncüllü',4)
OKS4=r'-{Stealth[length=2.3mm,width=1.9mm]}'
bl=['\\node[draw,rounded corners=2pt,inner sep=4pt,font=\\small] (gunes) at (0,4.2) {Güneş};',
    '\\node[draw,rounded corners=2pt,inner sep=4pt,font=\\small] (uret) at (3,4.2) {Üretici};',
    '\\node[draw,rounded corners=2pt,inner sep=4pt,font=\\small] (otcul) at (6,4.2) {Otçul};',
    '\\node[draw,rounded corners=2pt,inner sep=4pt,font=\\small] (etcil) at (9,4.2) {Etçil};',
    '\\node[draw,rounded corners=2pt,inner sep=4pt,font=\\small] (ayr) at (6,0.4) {Ayrıştırıcı};',
    '\\node[draw,rounded corners=2pt,inner sep=4pt,font=\\small,align=center] (min) at (1.4,0.4) {İnorganik\\\\madde};',
    '\\node[draw,rounded corners=2pt,inner sep=4pt,font=\\small] (isi) at (9,0.4) {Isı};']
ar=[('gunes','uret','1',1),('uret','otcul','',0),('otcul','etcil','',0),('etcil','isi','2',1),('ayr','min','',0),('min','uret','3',1)]
for a,b_,e,n in ar:
    bl.append(f'\\draw[{OKS4},line width=1pt] ({a})--({b_}) '+(f'node[midway,fill=white,font=\\normalsize\\bfseries,inner sep=1.5pt]{{{e}}}' if e else '')+';')
bl.append(f'\\draw[{OKS4},line width=1pt] (uret) to[out=-60,in=140] (ayr);\\draw[{OKS4},line width=1pt] (otcul)--(ayr);\\draw[{OKS4},line width=1pt] (etcil) to[out=-120,in=40] (ayr);')
SK4=tk('\n'.join(bl),.72)
d4={'I':(True,'1 numaralı ok güneşten üreticilere ışık enerjisinin girişini gösterir; ekosisteme enerji bu yolla girer.'),
    'II':(False,'2 numaralı ok enerjinin ısı olarak ortama kaybını gösterir; bu enerji ekosisteme geri dönmez. Enerji madde gibi döngüsel değildir.'),
    'III':(True,'3 numaralı okla üreticilere ulaşan inorganik maddeler, ayrıştırıcılar sayesinde yeniden kullanılır; madde ekosistemde döngüsel dolaşır.')}
r=onc(d4,True,'E')
q('0004','enerji',[A('Okları tanı','1: güneşten üreticiye giriş · 2: ısı kaybı · 3: inorganik maddeden üreticiye dönüş.','Enerji: tek yönlü · Madde: döngü'),
   adim_onc(d4,'I'),adim_onc(d4,'II'),adim_onc(d4,'III'),sonuc(r,True)],
 'enerji akışı ve madde döngüsü şeması',z='orta',alt='Enerji Akışı ve Madde Döngüsü',kaz='Enerji akışının tek yönlü, madde döngüsünün döngüsel olduğunu şemadan yorumlar.',kalip='öncüllü',
 metin='Şekilde, bir ekosistemde enerjinin ve maddenin canlı bileşenler arasındaki hareketi şematik olarak gösterilmiştir. Bazı oklar 1, 2 ve 3 ile numaralandırılmıştır; ısı kaybı yalnız etçil için örnek olarak gösterilmiş, diğer canlılar da ısı kaybeder.\nBuna göre,\nI. 1 numaralı ok, ekosisteme enerji girişini gösterir.\nII. 2 numaralı okla taşınan enerji, ekosistemde yeniden kullanılmak üzere üreticilere döner.\nIII. 3 numaralı okla taşınan maddeler, üreticiler tarafından yeniden kullanılır.\nyargılarından hangileri doğrudur?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her okun neyi taşıdığını (enerji ya da madde) ve bunun ekosistemde nereye gittiğini düşün.'],
 bilgi=[B('Enerji ve madde','Besin zincirinde enerji akışı tek yönlüdür · Madde, canlılar ile cansız çevre arasında döngüsel dolaşır')],
 puf='Enerji akar ve ısı olarak kaybolur; madde ise ayrıştırıcılar aracılığıyla döner.')

# ============ 0005 · karbon bütçesi tablosu · zor ============
kartla('05','dongu','Karbon bütçesi tablosu','Atmosferdeki karbondioksit değişimi, atmosfere verilen (solunum, ayrışma, yanma) ve atmosferden alınan (fotosentez, okyanusta çözünme) miktarların toplamından bulunur; koşullar değişince ilgili satırlar yeniden hesaplanır.','Ayrıştırıcıların solunumunu unutmak; koşul değişince yalnız bir satırı değiştirmek.','orta','tablo',4)
VER={'Canlıların solunumu':55,'Ayrıştırıcıların solunumu':60,'Fosil yakıt yanması':10,'Orman yangınları':5,'Fotosentez':-120,'Okyanusta çözünme':-8}
assert sum(VER.values())==2
yeni=dict(VER); yeni['Fosil yakıt yanması']=5; yeni['Orman yangınları']=0
dog5=sum(yeni.values()); assert dog5==-8
y1=sum(v for k,v in VER.items() if k!='Fosil yakıt yanması' and k!='Orman yangınları'); assert y1==-13
y2=sum(v for k,v in yeni.items() if k!='Orman yangınları')+5; assert y2==-3
y3=sum(v for k,v in VER.items() if k!='Orman yangınları')-10+20; assert y3==7
q('0005','dongu',[A('Tablodaki toplamı kur','Pozitif değerler atmosfere CO₂ verir, negatifler atmosferden alır.','Mevcut net: +2'),
   A('Yeni koşulları uygula','Fosil yakıt yarıya iner (10 → 5), orman yangınları sıfırlanır (5 → 0).','55 + 60 + 5 + 0 − 120 − 8'),
   A('Hesabı bitir','Pozitifler toplamı 120, negatifler toplamı 128’dir.','120 − 128 = −8')],
 'karbondioksit bütçesi, fosil yakıt yarıya iner',z='orta',alt='Madde Döngüleri',kaz='Karbon döngüsü verilerinden atmosferdeki CO₂ değişimini yeni koşullar için hesaplar.',kalip='tablo',
 metin='Bir ekosistemde atmosferdeki karbondioksit ile canlı ve cansız ortam arasındaki yıllık karbondioksit alışverişi aşağıdaki tabloda verilmiştir (birim/yıl). Pozitif değerler atmosfere verilen, negatif değerler atmosferden alınan karbondioksit miktarını göstermektedir. Diğer tüm olayların aynı kaldığı varsayılacaktır.\nBuna göre, fosil yakıt yanması yarıya inip orman yangınları hiç görülmezse atmosferdeki karbondioksit miktarının yıllık değişimi kaç birim olur?',
 sekil=tablo_dar(['Olay','CO₂ (birim/yıl)'],[[k,('+' if v>0 else '−')+str(abs(v))] for k,v in VER.items()]),
 dogru=-8,yan=[(-13,'Fosil yakıt yanmasını tamamen kaldırmış; oysa yalnız yarıya inmiştir (5 birim hâlâ atmosfere verilir).','dikkat'),
               (-3,'Orman yangınlarını (5 birim) de hesaba katmış; yangınlar hiç görülmeyeceğinden sıfırlanmalıdır.','dikkat'),
               (2,'Tablodaki mevcut toplamı vermiş; koşulların değiştiği gözden kaçmış.','dikkat'),
               (7,'Fosil yakıt yanmasını yarıya indirmek yerine iki katına çıkarmış (20 birim).','islem')],
 istenen='Yeni koşullarda atmosferdeki CO₂’nin yıllık değişimi.',
 ip=['Değişen satırları yeni değerleriyle yaz ve verilen ile alınan miktarların işaretlerine dikkat ederek topla.'],
 bilgi=[B('Karbon döngüsü','Solunum, ayrışma ve yanma atmosfere karbondioksit verir · Fotosentez atmosferden karbondioksit alır')],
 puf='Değişen satırları yeniden yaz, tüm satırları işaretleriyle topla.')

# ============ 0006 · besin ağı zincir sayımı · orta ============
kartla('06','agi','Besin ağında farklı besin zinciri sayısı','Besin ağında zincirler üreticiden başlayıp son tüketicide biter; bir canlı ağdan çıkınca onu içeren tüm zincirler kopar.','Ok sayısını zincir sayısı sanmak; çıkan canlıyı içermeyen zincirleri de saymamak.','orta','şekilli',4)
YE={'Böcek':['Bitki'],'Fare':['Bitki'],'Kurbağa':['Böcek'],'Yılan':['Kurbağa','Fare'],'Şahin':['Yılan','Fare','Kurbağa']}
def zincir(c,yok=()):
    if c in yok: return []
    if c=='Bitki': return [['Bitki']]
    out=[]
    for y in YE[c]:
        for z in zincir(y,yok): out.append(z+[c])
    return out
Z=zincir('Şahin'); assert len(Z)==4
Zf=zincir('Şahin',yok=('Fare',)); assert len(Zf)==2
assert len(zincir('Şahin',yok=('Kurbağa',)))==2 and sum(len(v) for v in YE.values())==8
POS={'Bitki':(2.7,0),'Böcek':(.6,1.6),'Fare':(4.8,1.6),'Kurbağa':(.6,3.2),'Yılan':(2.7,3.2),'Şahin':(4.8,4.8)}
nid=lambda c:c.replace('ı','i').replace('ş','s').replace('ğ','g').replace('İ','I')
bl=[f'\\node[draw,rounded corners=2pt,inner sep=4pt,line width=.9pt,font=\\small] ({nid(c)}) at ({x},{y}) {{{c}}};' for c,(x,y) in POS.items()]
for c,v in YE.items():
    for y in v: bl.append(f'\\draw[{OKU},line width=.9pt] ({nid(y)})--({nid(c)});')
SK6=tk('\n'.join(bl),.95)
dg,yn=(2,[(4,'Fareyi ağdan çıkarmayı hesaba katmamış; ağdaki bütün zincirleri saymıştır.','dikkat'),(1,'Yalnız bir zinciri saymış; fare olmadan da böcek–kurbağa kolu ve fare dışındaki yılan yolu sürer.','islem'),
   (3,'Fareyi içeren iki zincirden yalnızca birini çıkarmış (4 − 1 = 3).','islem'),(0,'Fare yok olunca besin zincirlerinin tamamen koptuğunu sanmış; oysa fareye bağlı olmayan zincirler sürer.','bilgi')])
q('0006','agi',[A('Ağı oku','Oklar yenen canlıdan yiyene doğrudur; her zincir bitkiden başlar, şahinde biter.','Bitki → … → Şahin'),
   A('Tüm zincirleri yaz','Şahin; yılan, fare ve kurbağayla beslenir; bunlara ulaşan yollar sayılır.','Toplam 4 zincir'),
   A('Fareyi içerenleri çıkar','Fare yok olunca fareyi içeren iki zincir kopar.','Kalan: böcek–kurbağa–şahin · böcek–kurbağa–yılan–şahin'),
   A('Sonucu yaz','Fare içermeyen zincirler kalır.','2 zincir')],
 'besin ağı, fare yok olunca zincir sayısı',z='orta',alt='Besin Ağı',kaz='Besin ağında farklı besin zinciri sayısını ve bir canlı yok olduğunda kalan zincirleri belirler.',kalip='şekilli',
 metin='Şekilde, bir ekosistemdeki canlılar arasındaki beslenme ilişkileri gösterilmiştir. Oklar yenen canlıdan yiyen canlıya doğrudur. Bir besin zinciri, üreticiden başlayıp hiçbir canlı tarafından yenmeyen son tüketicide biter. Bir hastalık nedeniyle fare popülasyonu tamamen yok olmuş, ağdaki diğer canlıların varlığını sürdürdüğü ve beslenme ilişkilerinin değişmediği bilinmektedir.\nBuna göre, ağda üreticiden son tüketiciye giden kaç farklı besin zinciri kalmıştır?',
 sekil=SK6,dogru=dg,yan=yn,istenen='Fare yok olduktan sonra kalan farklı besin zinciri sayısı.',
 ip=['Önce üreticiden son tüketiciye giden tüm yolları yaz; sonra yok olan canlıyı içerenleri ele.'],
 bilgi=[B('Besin zinciri ve ağı','Besin zinciri üreticiyle başlar ve son tüketiciyle biter · Besin ağı, birbirine bağlı birçok besin zincirinden oluşur')],
 puf='Zincirleri tek tek yaz, çıkan canlıyı içerenleri çiz ve kalanları say.')

# ============ 0007 · tolerans grafiği · orta · öncüllü ============
kartla('07','tolerans','Sıcaklık tolerans aralığı grafiği','Her canlının yaşayabildiği sıcaklık aralığı (tolerans aralığı) farklıdır; aralık geniş ise tür çevre değişimine dayanıklıdır. Belirli bir sıcaklıkta yalnız o değeri aralığında bulunduran türler yaşar.','Tepe yüksekliğini tolerans genişliği sanmak; sıcaklık değişiminde tür sayısını yanlış okumak.','orta','öncüllü',4)
TL={'X':(20,5,100),'Y':(25,20,60),'Z':(10,10,80)}
def yasar(k,T): o,h,_=TL[k]; return abs(T-o)<=h
assert max(TL,key=lambda k:TL[k][1])=='Y' and [k for k in TL if yasar(k,12)]==['Y','Z'] and [k for k in TL if yasar(k,30)]==['Y']
def tfun(k): o,h,A_=TL[k]; return lambda T:max(0,A_*(1-((T-o)/h)**2))
def cr7(k): return ' '.join(f'({T/2:.1f},{tfun(k)(T/2):.1f})' for T in range(0,101))
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=50,ymin=0,ymax=115,xtick={0,10,20,30,40,50},ytick=\\empty,xlabel={Sıcaklık ($^\\circ$C)},ylabel={Popülasyon büyüklüğü},'+AX+']',
   f'\\addplot[black] coordinates {{{cr7("X")}}};',f'\\addplot[vurgu] coordinates {{{cr7("Y")}}};',f'\\addplot[black,densely dashed] coordinates {{{cr7("Z")}}};',
   '\\node[font=\\normalsize\\bfseries] at (axis cs:20,108) {X};\\node[font=\\normalsize\\bfseries,vurgu] at (axis cs:32,60) {Y};\\node[font=\\normalsize\\bfseries] at (axis cs:7,88) {Z};','\\end{axis}']
SK7=tk('\n'.join(b),1.0)
d7={'I':(True,'Y’nin eğrisi yaklaşık 5 °C ile 45 °C arasındadır; X ve Z’ye göre en geniş sıcaklık aralığına sahiptir.'),
    'II':(False,'12 °C’ta yalnız Y (5–45 °C) ve Z (0–20 °C) yaşayabilir; X’in aralığı 15 °C’ta başlar. Yaşayabilen tür sayısı ikidir.'),
    'III':(True,'30 °C’ta X’in (15–25 °C) ve Z’nin (0–20 °C) aralığı dışında kalır; yalnız Y’nin aralığı 30 °C’ı içerir.')}
r=onc(d7,True,'D')
q('0007','tolerans',[A('Aralıkları oku','X yaklaşık 15–25 °C, Y yaklaşık 5–45 °C, Z yaklaşık 0–20 °C aralığında yaşar.','X: 10 · Y: 40 · Z: 20 °C genişlik'),
   adim_onc(d7,'I'),adim_onc(d7,'II'),adim_onc(d7,'III'),sonuc(r,True)],
 'üç türün sıcaklık tolerans eğrileri',z='orta',alt='Toleranslık',kaz='Tolerans eğrilerinden türlerin sıcaklık aralığını ve değişen sıcaklıkta yaşayabilen türleri belirler.',kalip='öncüllü',
 metin='Aynı ekosistemde yaşayan X, Y ve Z türlerinin popülasyon büyüklüklerinin ortam sıcaklığına göre değişimi grafikte gösterilmiştir. Eğrinin sıfıra indiği sıcaklık değerlerinde tür yaşamını sürdürememektedir; diğer çevre koşulları türler için uygundur.\nBuna göre,\nI. Y türü, sıcaklık bakımından en geniş tolerans aralığına sahiptir.\nII. 12 °C’ta üç türün üçü de yaşamını sürdürebilir.\nIII. Ortam sıcaklığı 30 °C’a çıkarsa yalnız Y türü yaşamını sürdürebilir.\nyargılarından hangileri doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her eğrinin başladığı ve sıfıra indiği sıcaklık değerlerini okuyarak aralıkları belirle.'],
 bilgi=[B('Tolerans aralığı','Canlının yaşamını sürdürebildiği çevre koşulu (sıcaklık, tuzluluk vb.) aralığına tolerans aralığı denir · Aralığı geniş türler çevre değişimine daha dayanıklıdır')],
 puf='Önce her türün aralığını yaz; sonra verilen değerin hangi aralıklarda kaldığını işaretle.')

# ============ 0008 · kompost · kolay · olumsuz ============
kartla('08','cevre','Kompostlaşma ve ayrıştırıcılar','Organik atıklar havalı ortamda bakteri ve mantarlar tarafından ayrıştırılır; sonuçta bitkilerin yeniden kullanabileceği inorganik besin tuzları açığa çıkar.','Ayrışmanın yalnız ısı ya da fiziksel etkenlerle olduğunu sanmak.','kolay','hikâyeli',3)
S8=['Atıkların dönüşümü yalnızca ısı enerjisi etkisiyle gerçekleşir, bu olayda canlıların rolü yoktur.','Atıkların dönüşümünde ayrıştırıcı bakteri ve mantarlar rol oynar.','Ayrıştırıcıların etkinliğiyle atıktaki organik maddeler inorganik maddelere dönüşür.','Oluşan topraksı madde, bitkilerin yeniden kullanabileceği mineraller içerir.','Kabın havadar olması, ayrıştırıcıların solunum yapmasını kolaylaştırır.']
q('0008','cevre',[A('Olayı tanımla','Kompost, organik atıkların ayrıştırıcılar tarafından dönüştürülmesidir.','Kompost = ayrıştırıcı etkinliği'),
   A('İfadeleri sına','Ayrıştırıcılar organik maddeyi inorganik hâle getirir, mineraller bitkilere yarar.','4 ifade doğru'),
   A('Yanlışı seç','Dönüşümde canlıların rolü olmadığını söyleyen ifade yanlıştır.','Yanlış: canlıların rolü yoktur')],
 'mutfak atıklarından kompost',z='kolay',alt='Madde Döngüsü',kaz='Kompost örneğiyle ayrıştırıcıların madde döngüsündeki rolünü açıklar.',kalip='hikâyeli',
 metin='Bir öğrenci, sebze ve meyve artıklarını toprakla karıştırıp havadar bir kapta nemli biçimde bekletiyor. Birkaç hafta sonra atıkların koyu renkli, topraksı bir maddeye dönüştüğünü görüyor ve bu maddeyi saksı çiçeklerine karıştırıyor.\nBu olayla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=S8[0],sira=yer('C',S8[0],S8[1:]),
 yan=[(S8[1],'Ayrıştırıcı bakteri ve mantarlar atıkları parçalar; ifade doğrudur.','bilgi'),(S8[2],'Ayrıştırıcılar organik maddeleri inorganik maddelere (mineraller, CO₂, su) çevirir; ifade doğrudur.','bilgi'),
      (S8[3],'Ayrışma ürünü olan mineraller, bitkilerin köklerinden alabileceği besin tuzlarıdır; ifade doğrudur.','dikkat'),(S8[4],'Havalı ortam, solunum yapan ayrıştırıcıların oksijen almasını sağlar; ifade doğrudur.','bilgi')],
 istenen='Kompostlaşmayla ilgili yanlış olan ifade.',
 ip=['Atıkları dönüştüren canlı grubunun ne olduğunu ve ürünlerinin bitkiler için ne işe yaradığını düşün.'],
 bilgi=[B('Ayrıştırıcılar','Bakteri ve mantarlar gibi ayrıştırıcılar ölü canlıları ve atıkları parçalayarak madde döngüsünü sürdürür')],
 puf='Ölü organik madde ayrıştırıcılar eliyle inorganik hâle gelir ve üreticilerce yeniden kullanılır.')

# ============ 0009 · dallanan besin zincirinde enerji · orta ============
kartla('09','enerji','Dallanan besin zincirinde enerji hesabı','Her basamakta enerjinin yaklaşık %10’u bir üst basamağa aktarılır; bir etçilin enerjisini iki farklı otçuldan aldığı durumda her kol ayrı hesaplanıp üretici enerjisi toplanır.','Basamak sayısını yanlış almak; yalnız bir kolu hesaba katmak; enerji aktarımını %1 almak.','orta','hikâyeli',4)
sahin=400; tav=F(3,4)*sahin*10; fare=F(1,4)*sahin*10; ot=(tav+fare)*10
assert (tav,fare,ot)==(3000,1000,40000)
q('0009','enerji',[A('Aktarım kuralını yaz','Her basamakta enerjinin %10’u üst basamağa geçer; bir basamak geriye gitmek için 10 ile çarpılır.','Alt basamak = üst × 10'),
   A('Şahinin kaynaklarını ayır','Şahinin 400 kJ’sinin 3/4’ü tavşandan, 1/4’ü fareden gelmiştir.','Tavşan payı: 300 · Fare payı: 100'),
   A('Tavşan ve farenin enerjisini bul','Her paya karşılık gelen enerji 10 katıdır.','Tavşan: 3000 kJ · Fare: 1000 kJ'),
   A('Otun enerjisini bul','Tavşan ve fare yalnızca otla beslenir; toplam enerji 10 ile çarpılır.','(3000 + 1000) × 10 = 40000 kJ')],
 'şahin, tavşan ve fare, ot enerjisi',z='orta',alt='Enerji Akışı',kaz='Dallanan besin zincirinde basamaklar arası enerji aktarımını hesaplar.',kalip='hikâyeli',
 metin='Bir çayır ekosisteminde ot, tavşan, fare ve şahin yaşamaktadır. Tavşan ve fare yalnızca otla beslenir; şahin ise enerji gereksiniminin dörtte üçünü tavşandan, dörtte birini fareden karşılar. Her basamakta, bir önceki basamaktaki enerjinin %10’u bir üst basamağa aktarılmaktadır. Şahin popülasyonunda bulunan enerji 400 kJ’dir.\nBuna göre, bu şahinlerin enerjisini sağlayabilmek için otlarda kaç kJ enerji bulunmalıdır?',
 dogru=40000,yan=[(4000,'Yalnız bir basamak geriye gitmiş: şahinin 400 kJ’si için 4000 kJ’yi otun enerjisi sanmıştır; tavşan ve fareden sonra otun da hesaplanması gerekir.','islem'),
                  (3000,'Tavşanın enerjisini otun enerjisi sanmış; ot bir basamak daha geridedir.','dikkat'),
                  (30000,'Yalnız tavşan koluna bakıp fareyi hesaba katmamıştır.','dikkat'),
                  (400000,'Üç basamak geriye giderek 400 kJ’yi 1000 ile çarpmış; oysa ot şahinden iki basamak gerisindedir.','islem')],
 istenen='Otlarda bulunması gereken enerji.',
 ip=['Şahinin enerjisinin hangi canlılardan geldiğini düşün.'],
 bilgi=[B('Enerji aktarımı','Besin zincirinde bir basamaktan sonrakine enerjinin yaklaşık %10’u aktarılır, geri kalanı solunumla ve ısı olarak harcanır')],
 puf='Her kolu ayrı düşün ve aktarım oranını basamak sayısına göre uygula.')

# ============ 0010 · ada besin zinciri · zor · öncüllü · olumsuz ============
kartla('10','cevre','Dışarıdan getirilen türün zincir etkisi','Besin zincirinde bir halkanın değişimi ardışık etkiler yaratır: avcı artınca av azalır, avın avı artar, onun besini azalır; ancak sınırlı besinle popülasyon sürekli büyüyemez.','Etkileri tek halkada bırakmak; bitki–böcek ilişkisinin yönünü karıştırmak.','orta','öncüllü',5)
d10={'I':(True,'Kuş kertenkelelerle beslendiğinden kertenkele popülasyonunun azalması beklenir.'),
     'II':(False,'Kertenkeleler azalınca böcekler artar; artan böcekler otları daha çok tüketir. Ot miktarının artması beklenmez, azalması beklenir.'),
     'III':(False,'Kuşun tek besini kertenkelelerdir; besin kaynağı azaldıkça kuş popülasyonu da sınırsız artamaz, besin yetersizliği büyümeyi durdurur.')}
r=onc(d10,False,'E')
q('0010','cevre',[A('Zinciri kur','Ot → böcek → kertenkele → kuş. Kuş yalnız kertenkelelerle beslenir.','Zincir yönü: otçul → etçiller'),
   adim_onc(d10,'I'),adim_onc(d10,'II'),adim_onc(d10,'III'),A('Sorunun kökünü uygula','Kökte beklenmeyen olaylar sorulmuştur; doğru olmayan etkiler seçilir.','Beklenmeyenler: '+', '.join(sorted(r['T'],key=['I','II','III'].index))),sonuc(r,False)],
 'ada, kertenkele ve kuş, zincir etkisi',z='orta',alt='Çevre Sorunları',kaz='Besin zincirinde bir halkanın değişiminin diğer halkalara etkisini yorumlar.',kalip='öncüllü',
 metin='Bir adada yalnızca ot, otla beslenen böcekler ve böceklerle beslenen kertenkeleler yaşamaktadır. Adaya, kertenkelelerden başka besin kullanmayan bir kuş türü getirilip bırakılıyor ve kuşların adada doğal düşmanı bulunmuyor. Uzun bir süre sonra adadaki canlıların popülasyon büyüklükleri inceleniyor.\nBuna göre,\nI. Kertenkele popülasyonu azalır.\nII. Böcek sayısındaki artışa bağlı olarak otların miktarı artar.\nIII. Kuş popülasyonu, kertenkelelerin azalmasına rağmen sınırsız artar.\nyargılarından hangilerinin gerçekleşmesi beklenemez?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Gerçekleşmesi beklenemeyen yargılar.',
 ip=['Zincirdeki her halkanın değişiminin ardışık olarak bir önceki ve bir sonraki halkaya nasıl yansıdığını düşün.'],
 bilgi=[B('Besin zincirinde denge','Bir halkanın sayısındaki değişim zincirdeki diğer halkaları etkiler · Besin kaynağı sınırlıysa popülasyonlar süresiz büyüyemez')],
 puf='Her halkanın değişimini komşu halkaya yansıt.')

bitir(P,'ekosistemuc',UK)
