"""TYT Biyoloji · Canlıların Sınıflandırılması · 3. paket (siniflandirmauc): 10 soru, kardeş yok, ipucu 1.
Venn yerleşimleri, bakteri sayıları, antibiyotik duyarlılık eşiği, deney/grafik değerleri ve öncül doğrulukları Python'da hesaplanır/assert edilir; şekiller aynı değerlerden çizilir."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_bio as H
from _hafif_bio3 import *
KONU_='Canlıların Sınıflandırılması'; UK='bio|Canlıların Sınıflandırılması'; H.KONU=KONU_
P=Parti('siniflandirmauc',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 9. sınıf Canlılar Dünyası'
TIP={'virus':('by-sn3-virus','Virüslerin yapısı ve konak özgüllüğü'),'dogal':('by-sn3-dogal','Doğal sınıflandırma ölçütleri'),'venn':('by-sn3-venn','Âlem özelliklerinin küme diyagramı'),
     'bakteri':('by-sn3-bakteri','Bakteri sayısının zamanla artışı'),'mantar':('by-sn3-mantar','Mantarlar ve simbiyotik yaşam deneyleri'),'omurgasiz':('by-sn3-omurgasiz','Omurgasız grupları özellik tablosu'),
     'antibiyotik':('by-sn3-antibiyotik','Antibiyotik duyarlılık deneyi'),'protista':('by-sn3-protista','Protista beslenme deneyi')}
def kartla(n,tip,alt,fikir,tuzak,z,kalip,adim):
    kart(f'K-BYSN3-{n}',alt,fikir,tuzak,z,kalip,adim,TIP[tip][0],TIP[tip][1],KY)
def q(no,tip,ad,ne,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[tip][0],tip=TIP[tip][1],kart=f"K-BYSN3-{no[-2:]} ({TIP[tip][1].lower()}) · {ne}",**k)
AX='tick label style={font=\\footnotesize},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.5pt}'

# ============ 0001 · virüs yapısı şeması · kolay · olumsuz ============
kartla('01','virus','Bakteri virüsünün yapısı ve özellikleri','Virüsler hücresel yapıda değildir; protein kılıf (kapsit) ve içinde nükleik asitten oluşur, ribozomu ve kendi metabolizması yoktur, çoğalmak için konak hücreye gereksinim duyar.','Virüsün kendi ribozomuyla protein sentezlediğini sanmak.','kolay','şekilli',3)
b=['\\draw[line width=1.2pt] (0,3.7)--(.75,3.3)--(.75,2.4)--(0,2.0)--(-.75,2.4)--(-.75,3.3)--cycle;',
   '\\draw[vurgu,line width=1.4pt] plot[smooth,tension=.8] coordinates {(-.4,3.2) (.15,3.05) (-.3,2.85) (.25,2.7) (-.2,2.5)};',
   '\\draw[line width=1.2pt] (-.14,2.0) rectangle (.14,.7);','\\draw[line width=.8pt] (-.14,1.7)--(.14,1.7) (-.14,1.4)--(.14,1.4) (-.14,1.1)--(.14,1.1);',
   '\\draw[line width=1.2pt] (-.5,.7)--(.5,.7)--(.5,.5)--(-.5,.5)--cycle;',
   '\\draw[line width=1.2pt] (-.45,.5)--(-1.05,-.35) (-.2,.5)--(-.45,-.45) (.2,.5)--(.45,-.45) (.45,.5)--(1.05,-.35);',
   '\\draw[line width=.8pt] (.75,2.85)--(1.7,2.85);\\node[font=\\normalsize\\bfseries] at (1.95,2.85) {1};',
   '\\draw[line width=.8pt] (.14,1.3)--(1.7,1.3);\\node[font=\\normalsize\\bfseries] at (1.95,1.3) {2};',
   '\\draw[line width=.8pt] (.9,-.1)--(1.7,-.1);\\node[font=\\normalsize\\bfseries] at (1.95,-.1) {3};']
SK1=tk('\n'.join(b),1.05)
S1=['1 numaralı yapının içinde kalıtım materyali bulunur.','1 ve 2 numaralı yapıların yapısında protein bulunur.','3 numaralı yapılar, virüsün konak hücreye tutunmasında rol oynar.','Bu virüs, kendi ribozomları aracılığıyla protein sentezler.','Bu virüs, çoğalmak için konak hücreye gereksinim duyar.']
q('0001','virus',[A('Şekli oku','1 numaralı baş bölümünde nükleik asit, 2 numaralı kuyruk ve 3 numaralı lifler protein yapıdadır.','1: baş (nükleik asit) · 2: kuyruk · 3: lifler'),
   A('İfadeleri sına','Nükleik asit baştadır, kılıf proteindir, lifler tutunmayı sağlar, virüs konak hücre olmadan çoğalamaz.','4 ifade doğru'),
   A('Yanlışı seç','Virüslerde ribozom bulunmaz; protein sentezi konak hücrenin ribozomlarıyla yapılır.','Yanlış: virüsün ribozomu')],
 'bakteri virüsünün şeması',z='kolay',alt='Virüsler',kaz='Virüs yapısını şemadan okur ve virüslerin hücresel olmayan yapısını açıklar.',kalip='şekilli',
 metin='Şekilde, bakterileri enfekte eden bir virüsün yapısı gösterilmiştir. Virüs, 1 numaralı yapısında kalıtım materyalini taşımakta, 2 ve 3 numaralı yapılarıyla bakteri yüzeyine tutunmaktadır.\nBu virüsle ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK1,dogru=S1[3],sira=yer('A',S1[3],[S1[0],S1[1],S1[2],S1[4]]),
 yan=[(S1[0],'Baş bölümü nükleik asit taşır; ifade doğrudur.','bilgi'),(S1[1],'Kapsit ve kuyruk protein yapıdadır; ifade doğrudur.','bilgi'),(S1[2],'Lifler konak yüzeyine tutunmayı sağlar; ifade doğrudur.','dikkat'),(S1[4],'Virüsler yalnız konak hücre içinde çoğalabilir; ifade doğrudur.','bilgi')],
 istenen='Virüsle ilgili yanlış olan ifade.',
 ip=['Virüslerin hücresel yapıda olup olmadığını ve protein sentezini nerede yaptıklarını düşün.'],
 bilgi=[B('Virüsler','Virüsler hücresel yapıda değildir · Genellikle protein kılıf ve içindeki nükleik asitten oluşur')],
 puf='Hücreye özgü bir yapının virüste bulunup bulunmadığını kontrol et.')

# ============ 0002 · doğal sınıflandırma ölçütü · kolay · olumsuz ============
kartla('02','dogal','Doğal sınıflandırmada kullanılan ölçütler','Doğal sınıflandırma, canlılar arasındaki akrabalık ilişkilerine dayanır; DNA ve protein benzerliği, homolog organlar, embriyo gelişimi ve fosil kayıtları ölçüt olur; yaşam alanı ya da kullanım amacı yapay ölçüttür.','Yaşam alanı benzerliğini akrabalık ölçütü sanmak.','kolay','hikâyeli',3)
S2=['DNA ve protein dizilimlerinin benzerliği','Embriyonik gelişim evrelerinin benzerliği','Homolog organların yapısal benzerliği','Fosil kayıtlarından çıkarılan benzerlikler','Yaşadıkları ortamın benzerliği']
q('0002','dogal',[A('Ölçütün amacını belirle','Doğal sınıflandırma akrabalık ilişkilerini yansıtır.','Ölçüt: akrabalık'),
   A('Seçenekleri sına','DNA, embriyo, homolog organ ve fosil verileri ortak atadan gelişi gösterir.','4 seçenek akrabalık ölçütü'),
   A('Yapay ölçütü seç','Aynı ortamda yaşamak akrabalık göstermez; yunus ile balık aynı ortamda yaşar ama akraba değildir.','Yapay: yaşam ortamı')],
 'yaşam ortamına göre gruplama ve doğal sınıflandırma',z='kolay',alt='Sınıflandırma Sistemleri',kaz='Doğal sınıflandırmada kullanılan ölçütleri yapay ölçütlerden ayırır.',kalip='hikâyeli',
 metin='Bir öğrenci, canlıları yaşadıkları ortama göre karada ve suda yaşayanlar diye gruplayınca yunus ile balığı aynı grupta, kurbağa ile kertenkeleyi ise farklı gruplarda topluyor. Öğretmeni, bilimsel sınıflandırmanın canlılar arasındaki akrabalık ilişkilerini yansıtması gerektiğini söylüyor.\nBuna göre, aşağıdakilerden hangisi akrabalık ilişkisine dayalı sınıflandırmada ölçüt olarak kullanılan bir özellik değildir?',
 dogru=S2[4],sira=yer('C',S2[4],S2[:4]),
 yan=[(S2[0],'Moleküler benzerlik akrabalığın en doğrudan göstergelerinden biridir.','bilgi'),(S2[1],'Embriyo gelişimindeki benzerlik ortak atayı gösterir.','bilgi'),(S2[2],'Homolog organlar ortak kökenli yapılardır.','dikkat'),(S2[3],'Fosil kayıtları akrabalık ve evrim hakkında bilgi verir.','bilgi')],
 istenen='Akrabalık ilişkisine dayalı sınıflandırmada ölçüt olmayan özellik.',
 ip=['Hangi ölçütlerin canlıların ortak atadan gelişini yansıttığını düşün.'],
 bilgi=[B('Sınıflandırma sistemleri','Doğal sınıflandırma akrabalık ilişkilerine dayanır · Yapay sınıflandırma kolay gözlenen özelliklere dayanır')],
 puf='Ölçütün ortak atayla ilgili bir kanıt verip vermediğine bak.')

# ============ 0003 · Venn: âlem özellikleri · orta ============
kartla('03','venn','Üç özellik kümesinde canlıların yeri','Hücre duvarı, çekirdek ve fotosentez her âlemde farklı birleşir: bakteri hücre duvarlıdır ama çekirdeği yoktur, mantar hücre duvarlı ve çekirdeklidir ama fotosentez yapmaz, bitki üçünü birden taşır, hayvanda hücre duvarı yoktur.','Siyanobakteriye çekirdek, bitkiye eksik özellik yazmak; mantarı fotosentetik saymak.','orta','şekilli',4)
OZE={'E. coli':(1,0,0),'Siyanobakteri':(1,0,1),'Maya':(1,1,0),'Ayçiçeği':(1,1,1),'İnsan':(0,1,0)}
YER={'E. coli':(1,0,0),'Siyanobakteri':(1,0,1),'Maya':(1,1,1),'Ayçiçeği':(1,1,1),'İnsan':(0,1,0)}
hata=[k for k in OZE if OZE[k]!=YER[k]]; assert hata==['Maya']
RC={(1,0,0):(-.85,-.4),(0,1,0):(3.15,-.4),(0,0,1):(1.15,3.7),(1,1,0):(1.15,-1.0),(1,0,1):(-.1,1.6),(0,1,1):(2.2,1.55),(1,1,1):(1.15,.8)}
b=['\\draw[line width=1.3pt] (0,0) circle (2.2);\\draw[line width=1.3pt] (2.3,0) circle (2.2);\\draw[line width=1.3pt] (1.15,2.0) circle (2.2);',
   '\\node[font=\\normalsize\\bfseries] at (-2.0,-1.9) {K};\\node[font=\\normalsize\\bfseries] at (4.3,-1.9) {L};\\node[font=\\normalsize\\bfseries] at (1.15,4.45) {M};']
from collections import defaultdict
say=defaultdict(list)
for k,v in YER.items(): say[v].append(k)
AD={'Siyanobakteri':'Siyano-\\\\bakteri','Maya':'Maya'}
for reg,adlar in say.items():
    x,y=RC[reg]
    for i,a in enumerate(adlar):
        yy=y+(.35 if len(adlar)==2 and i==0 else (-.35 if len(adlar)==2 else 0))
        b.append(f'\\node[font=\\small,align=center,text width=1.5cm] at ({x},{yy}) {{{AD.get(a,a)}}};')
SK3=tk('\n'.join(b),.95)
S3=['İnsan','Ayçiçeği','Maya','Siyanobakteri','E. coli']
q('0003','venn',[A('Kümeleri tanı','K hücre duvarı, L zarla çevrili çekirdek, M kendi organik besinini üretebilme özelliğidir.','K: duvar · L: çekirdek · M: fotosentez'),
   A('Canlıların özelliklerini yaz','E. coli yalnız K; siyanobakteri K ve M; maya K ve L; insan yalnız L; ayçiçeği K, L ve M özelliğine sahiptir.','Maya: K, L · Ayçiçeği: K, L, M'),
   A('Yerleşimi sına','Maya üç kümenin kesiştiği bölgeye konmuştur; mantar fotosentez yapamaz, M kümesinde olmamalıdır.','Hatalı: maya')],
 'üç özellik kümesinde beş canlının yerleşimi',z='orta',alt='Âlemler',kaz='Canlıların hücre duvarı, çekirdek ve fotosentez özelliklerine göre küme diyagramındaki yerini belirler.',kalip='şekilli',
 metin='Şekilde, K hücre duvarı bulunan, L hücresinde zarla çevrili çekirdek bulunan ve M kendi organik besinini üretebilen canlıların kümelerini göstermektedir. Beş canlıdan yalnız biri, küme diyagramında yanlış bölgeye yerleştirilmiştir.\nBuna göre, yeri hatalı olan canlı hangisidir?',
 sekil=SK3,dogru=S3[2],sira=yer('B',S3[2],[S3[0],S3[1],S3[3],S3[4]]),
 yan=[(S3[0],'İnsan hücre duvarsız, çekirdekli ve heterotroftur; yalnız L bölgesindedir, yeri doğrudur.','bilgi'),(S3[1],'Ayçiçeği duvarlı, çekirdekli ve fotosentetiktir; üç kümenin kesişimindeki yeri doğrudur.','dikkat'),
      (S3[3],'Siyanobakteri duvarlı, çekirdeksiz ve fotosentetiktir; K ve M kesişimi doğrudur.','bilgi'),(S3[4],'E. coli duvarlı, çekirdeksiz ve heterotroftur; yalnız K bölgesinde doğru yerdedir.','bilgi')],
 istenen='Yeri hatalı olan canlı.',
 ip=['Her canlının üç özellikten hangilerini taşıdığını yaz ve bulunduğu bölgenin hangi kümelerin kesişimi olduğuna bak.'],
 bilgi=[B('Âlemlerin ortak özellikleri','Hücre duvarı, çekirdek ve fotosentez âlemlere göre farklı birleşir · Prokaryotlarda zarla çevrili çekirdek bulunmaz')],
 puf='Her canlı için üç özelliği yaz, sonra kesiştiği kümelerle bölgeyi eşleştir.')

# ============ 0004 · bakteri sayısı grafiği · orta ============
kartla('04','bakteri','Bakteri sayısının zamanla artışı','İkiye bölünerek çoğalan bakteri popülasyonu her bölünme süresinde iki katına çıkar; grafikten bölünme süresi okunur ve sayı 2 üzeri bölünme sayısı olarak bulunur.','Bölünme sayısı yerine süre oranını kullanmak; doğrusal artış sanmak.','orta','şekilli',4)
n0=100; sK,sL=20,30
Kf=lambda t:n0*2**(t/sK); Lf=lambda t:n0*2**(t/sL)
assert (Kf(60),Lf(60))==(800,400) and Kf(180)/Lf(180)==8
ts=[i for i in range(0,91)]
def cb(f): return ' '.join(f'({t},{f(t):.1f})' for t in ts)
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=90,ymin=0,ymax=2500,xtick={0,15,30,45,60,75,90},ytick={0,400,800,1200,1600,2000,2400},xlabel={Zaman (dakika)},ylabel={Bakteri sayısı},'+AX+']',
   f'\\addplot[black] coordinates {{{cb(Kf)}}};',f'\\addplot[vurgu] coordinates {{{cb(Lf)}}};',
   '\\addplot[only marks,mark=*,mark size=2pt,black] coordinates {(60,800)};\\addplot[only marks,mark=*,mark size=2pt,vurgu] coordinates {(60,400)};',
   '\\node[font=\\normalsize\\bfseries] at (axis cs:70,1500) {K};\\node[font=\\normalsize\\bfseries,vurgu] at (axis cs:80,500) {L};','\\end{axis}']
SK4=tk('\n'.join(b),1.0)
q('0004','bakteri',[A('Başlangıç ve 60. dakikayı oku','İki türün başlangıç sayısı 100’dür; 60. dakikada K 800, L 400’e ulaşmıştır.','K: 100 → 800 · L: 100 → 400'),
   A('Bölünme sürelerini bul','K 60 dakikada 3 kez, L 2 kez iki katına çıkmıştır.','K: 20 dk · L: 30 dk'),
   A('180. dakikadaki sayıları bul','180 dakikada K 9 kez, L 6 kez bölünür.','K: 100·2⁹ · L: 100·2⁶'),
   A('Oranla','Oran 2⁹ / 2⁶ = 2³ olur.','8 kat')],
 'iki bakteri türünün büyüme grafiği, 3. saat oranı',z='orta',alt='Bakteriler',kaz='Büyüme grafiğinden bakterilerin bölünme süresini bulur ve ileri bir zamandaki sayı oranını hesaplar.',kalip='şekilli',
 metin='Besin ve alanın sınırlı olmadığı bir ortamda, ikiye bölünerek çoğalan K ve L bakteri türlerinin hücre sayılarının zamanla değişimi grafikte gösterilmiştir. Her iki türde de bölünmeler sonraki zamanlarda da aynı düzenle sürmekte ve başlangıçta 100 hücre bulunmaktadır.\nBuna göre, 3. saatin sonunda K’nin hücre sayısı L’nin hücre sayısının kaç katı olur?',
 sekil=SK4,dogru=8,yan=[(Fr(3,2),'Bölünme sayılarını oranlamış: 9 / 6 = 1,5; sayı oranı 2’nin kuvvetiyle bulunur.','islem'),(2,'60. dakikadaki değerleri oranlamış: 800 / 400 = 2; süreyi 3 saate taşımamıştır.','dikkat'),
                        (3,'Bölünme sayıları farkını (9 − 6) sayı oranı sanmış; fark kuvvet olmalıdır.','islem'),(4,'120. dakikadaki değerleri oranlamış: 6400 / 1600 = 4; 3. saate (180. dakika) ulaşmamıştır.','dikkat')],
 istenen='3. saat sonundaki K / L hücre sayısı oranı.',
 ip=['Grafikteki noktaların bölünme hakkında ne söylediğine bak.'],
 bilgi=[B('Bakterilerin çoğalması','Bakteriler çoğunlukla ikiye bölünerek çoğalır · Uygun koşullarda sayı düzenli aralıklarla katlanır')],
 puf='Önce her türün bölünme süresini bul, sonra bölünme sayısını kuvvet olarak yaz.')

# ============ 0005 · liken deneyi · orta · öncüllü ============
kartla('05','mantar','Mantar ve algin birlikte yaşamı','Kültür sonuçları, yalnız bir etkeni farklı olan tüplerin karşılaştırılmasıyla yorumlanır.','Birden çok etkeni değişen tüpleri karşılaştırmak.','orta','öncüllü',4)
d5={'I':(True,'3 numaralı tüpte mantar, alg ile birlikte kuru kayada yaşamıştır.'),
    'II':(True,'Alg tek başına kuru kayada ölürken mantarla birlikte yaşar; mantarla birlikte olmak algın yaşamasını sağlamıştır.'),
    'III':(False,'1 numaralı tüpte mantar tek başına kuru kayada ölmüştür; alg olmadan yaşayamamıştır.')}
r=onc(d5,True,'C')
OZT=[('1','Mantar','Kuru kaya','Öldü'),('2','Alg','Kuru kaya','Öldü'),('3','Mantar + alg','Kuru kaya','Yaşadı'),('4','Mantar','Besi yeri','Yaşadı')]
q('0005','mantar',[A('Tüpleri karşılaştır','1 ve 3 ile 2 ve 3 karşılaştırılarak birlikteliğin etkisi görülür.','Tek farklı etken karşılaştırılır'),
   adim_onc(d5,'I'),adim_onc(d5,'II'),adim_onc(d5,'III'),sonuc(r,True)],
 'mantar ve algin kuru kayada deneyi',z='orta',alt='Mantarlar',kaz='Mantar ve alg kültür sonuçlarından birlikte yaşamın her iki canlıya etkisini yorumlar.',kalip='öncüllü',
 metin='Bir araştırmacı, ışık alan kuru kaya yüzeyinde ve organik besin içeren besi yerinde mantar, alg ve mantar + alg kültürlerini bir ay bekletiyor; sonuçlar tabloda verilmiştir.\nBuna göre,\nI. Mantar, kuru kayada alg varlığında yaşamını sürdürmüştür.\nII. Alg, mantarla birlikte yaşayınca kuru ortamda hayatta kalmıştır.\nIII. Mantar, alg bulunmadan da kuru kayada yaşayabilir.\nyargılarından hangileri doğrudur?',
 sekil=tablo_dar(['Tüp','Canlı','Ortam','Sonuç'],[list(t) for t in OZT]),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Aynı ortamdaki tüpleri canlılar bakımından, aynı canlıdaki tüpleri ortam bakımından karşılaştır.'],
 bilgi=[B('Birlikte yaşam','Bazı canlılar birlikte yaşayarak birbirine yarar sağlar · Fotosentez yapan canlılar organik besin üretir')],
 puf='Önce karşılaştırılacak iki tüpü seç; aralarındaki tek farkı belirleyip sonuca bağla.')

# ============ 0006 · omurgasız grupları · orta · öncüllü ============
kartla('06','omurgasiz','Omurgasız gruplarının özellik tablosu','Omurgasız hayvan grupları doku, segmentli vücut, eklemli bacak ve kitin iskelet gibi özelliklerle ayrılır; tablodaki ortak sonuç sayısı karşılaştırılarak grupların benzerliği yorumlanır.','Segmentli vücutla eklemli bacağı aynı saymak; tabloda olmayan genellemeyi doğru kabul etmek.','orta','öncüllü',4)
OG={'K':'YYYY','L':'VVYY','M':'VYYY','N':'VVVV'}
col=lambda i:{g:OG[g][i] for g in OG}
ok_=lambda a,b:sum(OG[a][i]==OG[b][i] for i in range(4))
assert ok_('N','L')==2 and ok_('N','M')==1
assert [g for g in OG if OG[g][0]=='Y']==['K'] and (OG['L'][1]=='V' and OG['L'][2]=='Y')
d6={'I':(True,'Gerçek doku yalnız K’da yoktur; diğer üç grupta vardır.'),
    'II':(False,'L’de vücut segmentlidir ancak eklemli bacak yoktur; segmentli her canlıda eklemli bacak bulunmaz.'),
    'III':(True,'N ile L dört özelliğin ikisinde (doku, segment), N ile M yalnız birinde (doku) aynı sonucu verir.')}
r=onc(d6,True,'E')
vy=lambda s:['Var' if c=='V' else 'Yok' for c in s]
q('0006','omurgasiz',[A('Tabloyu oku','Doku yalnız K’da yoktur; segment L ve N’de, eklemli bacak ve kitin iskelet yalnız N’de bulunur.','Doku: K yok · Segment: L, N · Bacak, kitin: N'),
   adim_onc(d6,'I'),adim_onc(d6,'II'),adim_onc(d6,'III'),sonuc(r,True)],
 'dört omurgasız grubunun özellik tablosu',z='orta',alt='Hayvanlar',kaz='Özellik tablosundan omurgasız gruplarının ortak ve farklı özelliklerini yorumlar.',kalip='öncüllü',
 metin='K, L, M ve N dört omurgasız hayvan grubudur. Tabloda Doku gerçek doku, Segment halkalı vücut, Bacak eklemli bacak, Kitin kitinli dış iskelet bulunmasını göstermektedir.\nBuna göre,\nI. Gerçek doku bulunmayan tek grup K’dır.\nII. Vücudu segmentli olan grupların hepsinde eklemli bacak vardır.\nIII. N’nin L ile aynı sonucu verdiği özellik sayısı, M ile verdiğinden fazladır.\nyargılarından hangileri doğrudur?',
 sekil=tablo_dar(['Grup','Doku','Segment','Bacak','Kitin'],[[g]+vy(OG[g]) for g in 'KLMN']),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her özelliğin hangi gruplarda bulunduğunu işaretle ve gruplar arasında aynı sonuç sayısını say.'],
 bilgi=[B('Omurgasız hayvanlar','Omurgasız gruplar vücut yapısındaki özelliklerle ayrılır · Her özelliğin tüm gruplarda bulunması gerekmez')],
 puf='İfadeyi tablodaki ilgili sütunla karşılaştır; “hepsi”, “tek” gibi kapsamlı sözleri tüm satırlarda sına.')

# ============ 0007 · virüs–konak tablosu · zor · öncüllü ============
kartla('07','virus','Virüsün konak hücreye özgüllüğü','Virüsler yüzeylerine uygun konak hücreleri enfekte eder; her virüs belirli hücre tiplerinde çoğalır ve diğerlerinde çoğalmaz.','Virüsün her hücreyi enfekte edeceğini sanmak; enfeksiyon oranını karşılaştırmayı atlamak.','orta','öncüllü',5)
KON=[('İnsan akciğeri',(80,1,0)),('İnsan karaciğeri',(2,75,0)),('Fare akciğeri',(0,0,0)),('Bakteri',(0,0,90))]
V=lambda ad,j:dict(KON)[ad][j]
assert V('İnsan akciğeri',0)>V('İnsan karaciğeri',1) and V('İnsan akciğeri',2)==0 and V('İnsan karaciğeri',2)==0 and V('Bakteri',2)==90 and max(V('Bakteri',0),V('Bakteri',1))==0
d7={'I':(False,'V3’ün insan akciğeri ve karaciğer hücrelerindeki enfeksiyon oranı sıfırdır; insan hücrelerinde çoğalamaz.'),
    'II':(True,'V1’in insan akciğerindeki oranı % 80, V2’nin insan karaciğerindeki oranı % 75’tir; ilki daha büyüktür.'),
    'III':(True,'V3 yalnız bakteri kültüründe etkilidir (% 90); diğer kültürlerde sıfırdır.')}
r=onc(d7,True,'D')
q('0007','virus',[A('Tabloyu oku','V1 akciğer, V2 karaciğer, V3 bakteri hücrelerinde yüksek oranda enfeksiyon oluşturmuştur.','V1: akciğer · V2: karaciğer · V3: bakteri'),
   adim_onc(d7,'I'),adim_onc(d7,'II'),adim_onc(d7,'III'),sonuc(r,True)],
 'üç virüsün dört hücre kültüründe enfeksiyon oranı',z='orta',alt='Virüsler',kaz='Deney tablosundan virüslerin konak hücreye özgüllüğünü yorumlar.',kalip='öncüllü',
 metin='Bir araştırmacı, V1, V2 ve V3 virüslerini ayrı ayrı insan akciğeri, insan karaciğeri, fare akciğeri ve bakteri hücre kültürlerine bulaştırıyor. Virüsle enfekte olan hücrelerin yüzdesi tabloda verilmiştir.\nBuna göre,\nI. V3 insan hücrelerinde çoğalabilir.\nII. V1’in insan akciğeri hücrelerini enfekte etme oranı, V2’nin insan karaciğeri hücrelerini enfekte etme oranından yüksektir.\nIII. Bu deneyde V3 yalnız bakteri hücrelerinde etkili olmuştur.\nyargılarından hangileri doğrudur?',
 sekil=tablo_dar(['Kültür','V1','V2','V3'],[[k,*(str(x) for x in v)] for k,v in KON]),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her virüsün hangi kültürlerde yüksek, hangilerinde sıfıra yakın değer verdiğine bak.'],
 bilgi=[B('Virüslerin konak özgüllüğü','Virüsler yalnız yüzeyine uygun hücrelerde çoğalabilir · Hücresel yapıda olmadıkları için kendi başlarına çoğalamazlar')],
 puf='Her yargı için ilgili sütun ve satırı bul; sıfır değerleri etkisizlik olarak yorumla.')

# ============ 0008 · antibiyotik diski · zor ============
kartla('08','antibiyotik','Antibiyotik diski ve engelleme bölgesi','Antibiyotik diskinin çevresinde bakteri üremesinin engellendiği şeffaf bölge oluşur; bölge çapı büyüdükçe bakteri o antibiyotiğe daha duyarlıdır; çap eşiğin altındaysa bakteri dirençlidir.','Çapı eşiğin altında kalan antibiyotiği de etkili saymak.','zor','şekilli',5)
ZON={'A':24,'B':12,'C':6,'D':30}; ESIK=15; DISK=6
duy=[k for k,v in ZON.items() if v>=ESIK]; assert duy==['A','D'] and max(ZON,key=ZON.get)=='D' and ZON['C']==DISK
S8=['A ve D kullanılabilir; en etkili antibiyotik D’dir.','A, B ve D kullanılabilir; en etkili antibiyotik D’dir.','A ve D kullanılabilir; en etkili antibiyotik A’dır.','Yalnız D kullanılabilir; en etkili antibiyotik D’dir.','C kullanılabilir; çünkü çevresinde üreme engellenmemiştir.']
CRD={'A':(-1.7,1.3),'B':(1.9,1.5),'C':(-1.6,-1.7),'D':(1.5,-1.2)}
b=['\\filldraw[fill=gray!35,draw=black,line width=1.4pt] (0,0) circle (3.65);']
for k,(x,y) in CRD.items():
    rz=ZON[k]/20
    b.append(f'\\filldraw[fill=white,draw=black,densely dashed,line width=.9pt] ({x},{y}) circle ({rz});')
    b.append(f'\\filldraw[fill=gray!70,draw=black,line width=.8pt] ({x},{y}) circle (.3);')
    b.append(f'\\node[font=\\normalsize\\bfseries] at ({x},{y+.0}) {{\\textcolor{{white}}{{{k}}}}};')
b.append('\\node[font=\\small] at (0,-4.35) {Engelleme bölgesi çapı (mm): A 24 · B 12 · C 6 · D 30};')
SK8=tk('\n'.join(b),.78)
q('0008','antibiyotik',[A('Eşiği uygula','Çapı 15 mm ve üstü olan antibiyotik etkilidir; C’nin çapı disk çapına (6 mm) eşittir, yani bölge yoktur.','A: 24 · B: 12 · C: 6 · D: 30'),
   A('Etkili olanları ayır','A (24) ve D (30) eşiğin üzerindedir; B (12) ve C (6) altındadır.','Kullanılabilir: A, D'),
   A('En etkiliyi bul','Bölge çapı en büyük olan en etkilidir.','En etkili: D (30 mm)')],
 'dört antibiyotik diskinde engelleme bölgeleri',z='zor',alt='Bakteriler',kaz='Antibiyotik duyarlılık deneyinde bölge çaplarını eşikle karşılaştırarak etkili antibiyotikleri belirler.',kalip='şekilli',
 metin='Bir bakteri türü besi yerine ekiliyor ve üzerine A, B, C ve D antibiyotiklerini içeren, çapı 6 mm olan birer disk konuyor. Bir gün sonra disklerin çevresinde üremenin engellendiği şeffaf bölgeler oluşuyor. Bölge çapı en az 15 mm ise bakteri o antibiyotiğe duyarlı, daha küçükse dirençli sayılıyor.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK8,dogru=S8[0],sira=yer('D',S8[0],[S8[1],S8[2],S8[3],S8[4]]),
 yan=[(S8[1],'B’nin bölge çapı 12 mm’dir ve eşiğin altındadır; bakteri B’ye dirençlidir.','dikkat'),(S8[2],'En geniş bölge D’dedir (30 mm); A (24 mm) en etkili değildir.','islem'),
      (S8[3],'A’nın bölge çapı 24 mm olduğundan A da kullanılabilir.','dikkat'),(S8[4],'C’nin çevresinde disk çapı kadar bölge vardır; üreme engellenmemiştir, bakteri C’ye dirençlidir.','bilgi')],
 istenen='Deney sonuçlarına göre doğru olan ifade.',
 ip=['Bölge çaplarının eşik değere göre durumuna bak.'],
 bilgi=[B('Antibiyotikler','Antibiyotikler bakterilerin üremesini engeller veya bakterileri öldürür · Bakteriler bir antibiyotiğe karşı dirençli olabilir')],
 puf='Önce duyarlı sayılanları eşikle ayır; sonra aralarından bölge çapı en büyük olanı seç.')

# ============ 0009 · öglena deneyi · zor · öncüllü ============
kartla('09','protista','Öglenanın ışık ve besin koşullarına tepkisi','Işık ve organik besin koşulları öglenanın çoğalmasını farklı biçimlerde etkileyebilir.','Her koşulun etkisini ayrı ayrı yorumlamayı atlamak.','zor','öncüllü',5)
B0=20; SON9={'1':100,'2':12,'3':150,'4':90}
art={k:v-B0 for k,v in SON9.items()}
assert art['1']+art['4']!=art['3'] and SON9['1']>B0 and SON9['2']<B0 and SON9['4']>B0
d9={'I':(False,'Karanlıkta organik besin varken (4. koşul) de çoğalma olmuştur; öglena yalnız ışıkta çoğalmaz.'),
    'II':(True,'Işık ve besin birlikte olduğunda artış 130 birimdir; yalnız ışıkta 80, yalnız besinle 70 birim; bu iki artışın toplamı 150 ettiğinden 130’a eşit değildir; ancak karanlıkta organik besin varlığı çoğalmayı sağlar; bu, öglenanın heterotrof de beslenebildiğini gösterir.'),
    'III':(False,'Işık ve besin birlikte iken artış 130 birimdir; tek tek artışların toplamı 80 + 70 = 150’dir, eşit değildir.')}
d9['II']=(True,'Karanlıkta organik besin yokken popülasyon azalmış (20 → 12), organik besin varken artmıştır (20 → 90); öglena karanlıkta ortamdaki organik besinle çoğalabilir.')
r=onc(d9,True,'A')
b=['\\begin{axis}[ybar,width=7.8cm,height=5.4cm,bar width=.7cm,xmin=.4,xmax=4.6,ymin=0,ymax=170,xtick={1,2,3,4},xticklabels={{Işık\\\\Besin yok},{Karanlık\\\\Besin yok},{Işık\\\\Besin var},{Karanlık\\\\Besin var}},xticklabel style={font=\\footnotesize,align=center},ytick={0,50,100,150},ylabel={Popülasyon (birim)},tick label style={font=\\footnotesize},label style={font=\\small},axis lines=left,nodes near coords,every node near coord/.append style={font=\\footnotesize,fill=white,inner sep=1pt}]',
   f'\\draw[densely dashed,line width=.9pt] (axis cs:.4,{B0})--(axis cs:4.6,{B0});',
   f'\\addplot[fill=black!55,draw=black] coordinates {{(1,{SON9["1"]}) (2,{SON9["2"]}) (3,{SON9["3"]}) (4,{SON9["4"]})}};',
   '\\end{axis}']
SK9=tk('\n'.join(b),1.0)
q('0009','protista',[A('Başlangıç değerini kullan','Başlangıçta popülasyon 20 birimdir; kesikli çizgi bu değeri göstermektedir.','Başlangıç: 20'),
   adim_onc(d9,'I'),adim_onc(d9,'II'),adim_onc(d9,'III'),sonuc(r,True)],
 'öglena kültürleri, ışık ve besin',z='zor',alt='Protista',kaz='Işık ve organik besin koşullarına göre değişen popülasyon verilerinden öglenanın beslenme biçimini yorumlar.',kalip='öncüllü',
 metin='Başlangıçta 20 birim olan öglena popülasyonu, ışık ve organik besin koşulları değiştirilen dört kültürde 10 gün bekletiliyor. Ulaşılan büyüklükler grafikte, başlangıç değeri kesikli çizgiyle gösterilmiştir.\nBuna göre,\nI. Öglena yalnız ışıkta çoğalabilir.\nII. Öglena, karanlıkta ortamda organik besin varsa çoğalabilir.\nIII. Işık ve besinin birlikte sağladığı artış, ayrı ayrı sağladıkları artışların toplamına eşittir.\nyargılarından hangileri doğrudur?',
 sekil=SK9,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her koşuldaki değeri başlangıç değeriyle karşılaştırıp artış ya da azalışı hesapla.'],
 bilgi=[B('Protista âlemi','Protistalar tek hücreli ya da basit yapılı ökaryotlardır · Bazı üyeleri hem fotosentez yapar hem de hazır besin alabilir')],
 puf='Önce her çubuğun başlangıca göre artışını yaz; sonra yargılardaki koşulları bu artışlarla eşleştir.')

# ============ 0010 · maya deneyi · zor · olumsuz ============
kartla('10','mantar','Maya, şeker ve gaz çıkışı deneyi','Maya tek hücreli bir mantardır; deneyde yalnız bir etkeni farklı olan tüpler karşılaştırılır.','Veride olmayan bir sonucu çıkarmak.','zor','şekilli',5)
TB=[('1','Maya + şekerli su','35 °C',.78),('2','Maya + su','35 °C',.12),('3','Kaynatılıp soğutulmuş maya + şekerli su','35 °C',.12),('4','Maya + şekerli su','4 °C',.3)]
b=[]
for i,(no,ic,ort,rb) in enumerate(TB):
    x=2.6*i
    b.append(f'\\draw[line width=1.2pt] ({x-.4},3.1)--({x-.4},.4) arc (180:360:.4)--({x+.4},3.1);')
    b.append(f'\\fill[vurgu,opacity=.35] ({x-.4+.03},.4) arc (180:360:.37)--({x+.37},1.9)--({x-.37},1.9)--cycle;')
    if rb>.2: b.append(f'\\filldraw[fill=gray!25,draw=black,line width=1pt] ({x},{3.1+rb*1.2}) ellipse ({rb} and {rb*1.2});')
    else: b.append(f'\\draw[line width=1.2pt] ({x-.4},3.1)--({x-.15},3.3)--({x+.15},3.22)--({x+.4},3.1);')
    b.append(f'\\node[font=\\normalsize\\bfseries] at ({x},-.55) {{{no}}};')
SK10=tk('\n'.join(b),.8)
S10=['1 ve 2 numaralı tüplerin karşılaştırılması, mayanın gaz çıkarması için şekerin gerekli olduğunu gösterir.','1 ve 3 numaralı tüplerin karşılaştırılması, canlı mayanın gaz çıkışında gerekli olduğunu gösterir.','1 ve 4 numaralı tüplerin karşılaştırılması, düşük sıcaklığın gaz çıkışını azalttığını gösterir.','Maya, gaz çıkışını etkileyen koşullar bakımından sıcaklıktan etkilenir.','2 numaralı tüpte balonun şişmemesi, mayanın suda canlılığını yitirdiğini gösterir.']
q('0010','mantar',[A('Tüpleri ikişer ikişer karşılaştır','1–2 şeker, 1–3 maya canlılığı, 1–4 sıcaklık karşılaştırmasıdır.','Her karşılaştırmada tek etken farklı'),
   A('İfadeleri sına','Şeker, canlı maya ve uygun sıcaklık gaz çıkışı için gereklidir; ilk dört ifade verilerle uyumludur.','4 ifade verilerle uyumlu'),
   A('Desteklenmeyeni seç','2. tüpte şeker yoktur; balonun şişmemesinden mayanın öldüğü sonucu çıkarılamaz.','Desteklenmeyen: 2. tüp')],
 'maya, şeker, sıcaklık ve balon deneyi',z='zor',alt='Mantarlar',kaz='Kontrollü maya deneyinde karşılaştırma yaparak geçerli ve geçersiz çıkarımları ayırır.',kalip='şekilli',
 metin='Maya tek hücreli bir mantardır. Dört özdeş tüpe karışımlar konup ağızlarına balon takılıyor: 1 maya + şekerli su, 2 maya + su, 3 kaynatılıp soğutulmuş maya + şekerli su, 4 maya + şekerli su. Tüp 1, 2 ve 3 35 °C’ta, tüp 4 4 °C’ta bekletildiğinde balonlar şekildeki gibi oluyor.\nBu deneye göre aşağıdakilerden hangisi söylenemez?',
 sekil=SK10,dogru=S10[4],sira=yer('B',S10[4],[S10[0],S10[1],S10[2],S10[3]]),
 yan=[(S10[0],'Yalnız 2. tüpte şeker yoktur ve balon şişmemiştir; ifade doğrudur.','bilgi'),(S10[1],'Yalnız 3. tüpteki maya kaynatılmıştır ve balon şişmemiştir; ifade doğrudur.','dikkat'),
      (S10[2],'Yalnız 4. tüpün sıcaklığı düşüktür ve balon daha az şişmiştir; ifade doğrudur.','bilgi'),(S10[3],'1 ve 4 numaralı tüpler gaz çıkışının sıcaklıkla değiştiğini gösterir; ifade doğrudur.','bilgi')],
 istenen='Deney verileriyle desteklenmeyen ifade.',
 ip=['Her karşılaştırmada hangi etkenin tek başına değiştiğine ve verinin neyi kanıtlayıp neyi kanıtlamadığına dikkat et.'],
 bilgi=[B('Mantarlar','Mantarlar ökaryot, hücre duvarlı ve heterotroftur · Maya tek hücreli bir mantardır')],
 puf='Tek farkı belirle ve sonucu yalnız o farkla ilişkilendir; fazla yorumu ele.')

bitir(P,'siniflandirmauc',UK)
