"""TYT Kimya · Kimya Bilimi · ek paket (kimyabilimiiki): 16 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır, TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (OG) tanımlanır;
anahtar, adımlar ve çeldirici kümeleri oradan türetilir. Sayısal her şey assert edilir."""
import sys,os,re
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
H.KONU='Kimya Bilimi'
P=Parti('kimyabilimiiki','Kimya Bilimi','kim|Kimya Bilimi',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (kimya bilimi, sembolik dil, iş güvenliği; yalnız mantık) · MEB 9. sınıf Kimya Bilimi'
TM={'malzeme':('malzeme','Laboratuvar malzemeleri'),'silindir':('malzeme','Laboratuvar malzemeleri'),'simya':('simya','Simya ve bilim insanları'),'bilimadamlari':('simya','Simya ve bilim insanları'),
    'altdal':('altdal','Alt dallar ve meslekler'),'meslek':('altdal','Alt dallar ve meslekler'),'sembol':('sembol','Element ve bileşik adları, sembolleri'),'gunlukad':('sembol','Element ve bileşik adları, sembolleri'),
    'denkles':('formul','Formülde ve denklemde atom sayısı'),'formulsay':('formul','Formülde ve denklemde atom sayısı'),'karma':('formul','Formülde ve denklemde atom sayısı'),'esitleme':('formul','Formülde ve denklemde atom sayısı'),
    'uyari':('uyari','Uyarı işaretleri'),'saglik':('saglik','Elementlerin sağlığa etkisi'),'durum':('saglik','Elementlerin sağlığa etkisi'),'agirmetal':('saglik','Elementlerin sağlığa etkisi')}
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    tipad,tip=TM[tipad]
    kart(f'K-KMKB2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-kb2-{tipad}',tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    t_,n_=TM[k['tipId'][7:]]; k['tipId']=f'km-kb2-{t_}'; k['tip']=n_
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
RM={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI'}
def kume(s):
    s=sorted(s)
    if len(s)==1: return f'Yalnız {RM[s[0]]}'
    if len(s)==2: return f'{RM[s[0]]} ve {RM[s[1]]}'
    return ', '.join(RM[i] for i in s[:-1])+f' ve {RM[s[-1]]}'
def oncul(og):
    """og: [(metin, doğru_mu, açıklama)] → (metin satırları, doğru küme, adım listesi)"""
    metin='\n'.join(f'{RM[i+1]}. {t}' for i,(t,_,_) in enumerate(og))
    dog=[i+1 for i,(_,d,_) in enumerate(og) if d]
    ad=[A(f'{RM[i+1]}. öncül',ac,f'{RM[i+1]}: '+('doğru' if d else 'yanlış')) for i,(_,d,ac) in enumerate(og)]
    return metin,dog,ad

# ===================================================== 01 · laboratuvar malzemeleri (şekil) · kolay
kartla('01','Laboratuvar malzemeleri','Dereceli silindir sıvı hacmini ölçer; erlenmayer çalkalama, ısıtma ve titrasyon için, beherglas çözelti hazırlama ve ısıtma için, büret ise akıtılan hacmi damla damla ölçmek için kullanılır.','Beherglasın üzerindeki bölmeleri hassas ölçüm sanmak; büreti genel hacim ölçme aracı saymak.','kolay','şekilli',2,'malzeme','Laboratuvar malzemesi tanıma')
def beher(x):
    t=f'\\draw[thick] ({x-.1:.2f},1.78) -- ({x:.2f},1.7) -- ({x:.2f},0) -- ({x+1.3:.2f},0) -- ({x+1.3:.2f},1.7);\n'
    for y in (.5,.9,1.3): t+=f'\\draw ({x+1.3:.2f},{y}) -- ({x+1.0:.2f},{y});\n'
    return t
def erlen(x):
    return (f'\\draw[thick] ({x+.5:.2f},2.1) -- ({x+.55:.2f},1.4) -- ({x:.2f},0) -- ({x+1.5:.2f},0) -- ({x+.95:.2f},1.4) -- ({x+1.0:.2f},2.1);\n'
            f'\\draw[thick] ({x+.45:.2f},2.1) -- ({x+1.05:.2f},2.1);\n')
def silindir(x,h=2.6):
    t=f'\\draw[thick] ({x:.2f},{h}) -- ({x:.2f},.15) -- ({x+.45:.2f},.15) -- ({x+.45:.2f},{h});\n\\draw[thick] ({x-.2:.2f},0) rectangle ({x+.65:.2f},.15);\n'
    y=.45
    while y<h-.1: t+=f'\\draw ({x+.45:.2f},{y:.2f}) -- ({x+.2:.2f},{y:.2f});\n'; y+=.22
    return t
def buret(x):
    t=f'\\draw[thick] ({x:.2f},3.3) -- ({x:.2f},.8) -- ({x+.3:.2f},.8) -- ({x+.3:.2f},3.3);\n'
    t+=f'\\draw[thick] ({x-.15:.2f},.8) -- ({x+.45:.2f},.8);\\draw[thick] ({x-.2:.2f},.62) rectangle ({x+.5:.2f},.74);\n'
    t+=f'\\draw[thick] ({x+.08:.2f},.62) -- ({x+.15:.2f},.05) -- ({x+.22:.2f},.62);\n'
    y=1.15
    while y<3.2: t+=f'\\draw ({x+.3:.2f},{y:.2f}) -- ({x+.12:.2f},{y:.2f});\n'; y+=.18
    return t
g=beher(0)+erlen(2.1)+silindir(4.5)+buret(6.5)
for xc,r in ((.65,'I'),(2.85,'II'),(4.72,'III'),(6.65,'IV')): g+=f'\\node at ({xc},-.45) {{\\textbf{{{r}}}}};\n'
SK1=tk(g)
s1=['I – II','II – III','III – I','III – II','IV – II']
q('0001',[A('Malzemeleri tanı','Çizimlerde I beherglas, II erlenmayer, III dereceli silindir, IV bürettir.','I: beherglas · II: erlenmayer · III: dereceli silindir · IV: büret'),
          A('Hacim ölçümünü bul','Sıvı hacmini hassas ölçmek için dereceli silindir kullanılır.','dereceli silindir → III'),
          A('Çalkalamayı bul','Konik gövdeli, dar ağızlı erlenmayer çalkalamaya uygundur.','erlenmayer → II'),
          A('Sırayı yaz','İstenen sıra: önce dereceli silindir, sonra erlenmayer.','III – II')],
  tipId='km-kb2-malzeme',tip='Laboratuvar malzemesi tanıma',z='kolay',alt='Laboratuvar Malzemeleri',kaz='Temel laboratuvar malzemelerini çizimlerinden tanır ve kullanım amacına göre seçer.',kalip='şekilli',
  kart='K-KMKB2-01 (malzeme tanıma) · silindir ve erlenmayer eşleştirme',
  metin='Kimya dersinde öğrenciler, tuzlu su çözeltisi hazırlama deneyini yapmaktadır. Öğrencilerden biri önce 40 mL suyun hacmini hassas biçimde ölçmek için dereceli silindiri kullanmış, ardından ölçtüğü suyu içine tuz ekleyip çalkalayarak karıştırabilmek için erlenmayere aktarmıştır.\nÖğrencinin kullandığı bu iki laboratuvar malzemesi, yukarıdaki çizimlerde sırasıyla hangi numaralarla gösterilmiştir?',
  dogru=s1[3],sira=s1,sekil=SK1,
  yan=[(s1[0],'Beherglas üzerindeki bölmeleri hassas hacim ölçümü sanmış; beherin bölmeleri yalnız yaklaşık değer verir.','bilgi'),
       (s1[1],'İki malzemenin adlarını çizimlerle ters eşleştirmiş.','dikkat'),
       (s1[2],'Çalkalama için beherglası seçmiş; beherin geniş ağzı çalkalarken sıvı taşırır.','bilgi'),
       (s1[4],'Büreti hacim ölçme aracı sanmış; büret, akıtılan sıvı hacmini damla damla ölçmek için kullanılır.','bilgi')],
  istenen='Dereceli silindir ve erlenmayerin çizim numaraları (sırasıyla).',
  ip=['Dar ve uzun, üzerinde eşit aralıklı bölmeler bulunan kap, hacim ölçmek için tasarlanmıştır.'],
  bilgi=[B('Laboratuvar malzemeleri','dereceli silindir sıvı hacmini ölçer, erlenmayer çalkalama ve titrasyonda, beherglas çözelti hazırlamada ve ısıtmada, büret ise sıvıyı damla damla akıtıp hacmini ölçmede kullanılır')],
  puf='Hassas hacim ölçümü dereceli silindir, çalkalama erlenmayer, geniş ağızlı hazırlama kabı beherglastır.')

# ===================================================== 02 · simya (öncüllü) · orta
kartla('02','Simyadan kimyaya','Simyacıların amaçları (altın, ölümsüzlük) ve deneysel birikimi; damıtma, süzme gibi yöntemlerin kimyaya aktarılması.','Simyacıların deney yapmadığını sanmak; eski yöntemlerin bugün kullanılmadığını düşünmek.','kolay','öncüllü',3,'simya','Simyacılar ve kimyaya katkıları')
m2,d2,a2=oncul([
 ('Simyacılar, adi metalleri altına dönüştürmeyi amaçlamıştır.',True,'Adi metalleri altına çevirmek, simyacıların temel amaçlarından biridir.'),
 ('Simyacıların kullandığı damıtma ve süzme gibi yöntemler, günümüz kimya laboratuvarlarında da kullanılır.',True,'Damıtma ve süzme günümüzde de madde ayırmada kullanılan yöntemlerdir.'),
 ('Simyacılar deney yapmadıkları için simya, kimyanın gelişmesine katkı sağlamamıştır.',False,'Simyacılar çok sayıda deney yapmış; bu birikim kimyanın doğuşuna zemin hazırlamıştır.')])
assert d2==[1,2]
s2=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']; assert s2[2]==kume(d2)
q('0002',a2+[A('Sonucu bul','Doğru öncüller I ve II’dir.',kume(d2))],
  tipId='km-kb2-simya',tip='Simyacılar ve kimyaya katkıları',z='kolay',alt='Simyadan Kimyaya',kaz='Simyacıların amaçlarını ve çalışmalarının kimyaya katkısını açıklar.',kalip='öncüllü',
  kart='K-KMKB2-02 (simya) · üç öncül, I ve II doğru',
  metin='Kimya bilimi, uzun bir geçmişe dayanan deneysel birikimin sonucunda ortaya çıkmıştır. Bu birikimin önemli bir kısmı, kimyadan önce maddelerle uğraşan simyacılara aittir. Bir tarih dersinde simyacılar ve kimyaya etkileri üzerine aşağıdaki üç ifade yazılıyor.\n'+m2+'\nBuna göre bu ifadelerden hangileri doğrudur?',
  dogru=s2[2],sira=s2,
  yan=[(s2[0],'II’yi yanlış sanmış; damıtma ve süzmenin günümüzde de kullanıldığını bilmemiş.','bilgi'),
       (s2[1],'I’i yanlış sanmış; adi metalleri altına çevirme çabasını bilmemiş.','bilgi'),
       (s2[3],'II’yi yanlış, III’ü doğru sanmış; simyacıların deney yaptığını gözden kaçırmış.','bilgi'),
       (s2[4],'III’ü doğru sanmış; simyacıların deneysel çalışmalarının kimyaya katkı yaptığını bilmemiş.','bilgi')],
  istenen='Doğru ifadelerin belirlenmesi.',
  ip=['Simyacıların laboratuvarda neler yaptığını düşün; yöntemlerin bugün de kullanılıp kullanılmadığına bak.'],
  bilgi=[B('Simya','kimyadan önceki dönemde adi metalleri altına çevirmeyi ve ölümsüzlük iksirini arayan, deneye dayalı bir çalışma alanıdır; damıtma, süzme gibi yöntemler bu dönemden günümüze ulaşmıştır')],
  puf='Simya bilimsel kimya sayılmaz ama deney birikimiyle kimyanın temelini hazırlamıştır.')

# ===================================================== 03 · bilim insanları (tablo, öncüllü mantık) · orta
kartla('03','Kimyaya katkı yapan bilim insanları','Cabir bin Hayyan deneysel yöntem ve damıtma gibi işlemler; Lavoisier kütlenin korunumu; Boyle deneye dayalı yaklaşım; elementlerin periyodik sınıflandırması sonraki dönemde yapılmıştır.','Bilim insanlarının katkılarını birbirinin yerine yazmak; periyodik sınıflandırmayı simyacılara bağlamak.','orta','tablo',4,'bilimadamlari','Bilim insanı–katkı eşleştirme')
og3=[('Cabir bin Hayyan','Damıtma gibi yöntemleri deneylerde kullandı',True,'Cabir bin Hayyan damıtma gibi laboratuvar yöntemlerini deneylerinde kullanmıştır.'),
     ('Lavoisier','Tepkimelerde kütlenin korunduğunu gösterdi',True,'Lavoisier kütlenin korunumunu ortaya koyan bilim insanıdır.'),
     ('Simyacılar','Elementleri periyodik tabloda sınıflandırdı',False,'Elementlerin periyodik tabloda sınıflandırılması simyacılardan çok sonra yapılmıştır.'),
     ('Boyle','Kimyanın bilim olmasına deneyleriyle katkı verdi',True,'Boyle’un deneye dayalı çalışmaları kimyanın bilim olmasına katkı sağlamıştır.')]
d3=[i+1 for i,x in enumerate(og3) if x[2]]; assert d3==[1,2,4]
SK3=tablo_svg(['No','Bilim insanı','Kimyaya katkısı'],[[RM[i+1],x[0],x[1]] for i,x in enumerate(og3)])
s3=['I ve II','I ve IV','II ve III','II ve IV','I, II ve IV']; assert s3[4]==kume(d3)
q('0003',[A(f'{RM[i+1]}. satır',x[3],f'{RM[i+1]}: '+('doğru' if x[2] else 'yanlış')) for i,x in enumerate(og3)]+[A('Sonucu bul','Doğru satırlar I, II ve IV’tür.',kume(d3))],
  tipId='km-kb2-bilimadamlari',tip='Bilim insanı–katkı eşleştirme',z='orta',alt='Simyadan Kimyaya',kaz='Kimyanın gelişimine katkı yapan bilim insanlarını katkılarıyla eşleştirir.',kalip='tablo',
  kart='K-KMKB2-03 (bilim insanları) · tablo, I-II-IV doğru',
  metin='Kimya tarihi dersinde öğretmen, kimyanın simyadan bilime uzanan gelişimini anlatmış ve öğrencilerden simyacılar ile kimyanın gelişimine katkı sağlayan bazı bilim insanlarının çalışmalarını bir tabloda eşleştirmelerini istemiştir. Öğrencilerden biri eşleştirmeyi aşağıdaki gibi yapmıştır.\nBuna göre öğrencinin eşleştirmelerinden hangileri doğrudur?',
  dogru=s3[4],sira=s3,sekil=SK3,
  yan=[(s3[0],'IV’ü yanlış sanmış; Boyle’un deneye dayalı çalışmalarının kimyaya katkısını bilmemiş.','bilgi'),
       (s3[1],'II’yi yanlış sanmış; kütlenin korunumunun Lavoisier’e ait olduğunu bilmemiş.','bilgi'),
       (s3[2],'I ve IV’ü yanlış, III’ü doğru sanmış; periyodik sınıflandırmayı simyacılara bağlamış.','bilgi'),
       (s3[3],'I’i yanlış sanmış; Cabir bin Hayyan’ın damıtma gibi yöntemleri kullandığını bilmemiş.','bilgi')],
  istenen='Doğru eşleştirmelerin belirlenmesi.',
  ip=['Tablodaki her satırı, o bilim insanının ya da simyacıların bilinen çalışmasıyla tek tek karşılaştır.'],
  bilgi=[B('Kimya tarihi','Cabir bin Hayyan, Boyle ve Lavoisier kimya tarihinin önemli isimleridir; her birinin kimyaya katkısı farklı bir yöntem ya da kavrama dayanır')],
  puf='Bilim insanını ismine değil, bıraktığı kavram ya da kanuna bağlayarak hatırla.')

# ===================================================== 04 · alt dallar (öncüllü, hikâyeli) · orta
kartla('04','Kimyanın alt dalları','Madde türü/miktarı analitik; karbon bileşikleri organik; canlıdaki olaylar biyokimya; enerji ve fiziksel ilkeler fizikokimya.','Çalışma konusuna değil maddenin adına bakıp dalı seçmek.','orta','öncüllü',4,'altdal','Olay–alt dal eşleştirme')
og4=[('Ayşe, bir nehir suyundaki kurşun miktarını ölçüyor. (Analitik kimya)',True,'Madde miktarının belirlenmesi analitik kimyanın konusudur.'),
     ('Burak, karbon atomlarından oluşan yeni bir ilaç etken maddesini sentezliyor. (Anorganik kimya)',False,'Karbon bileşiklerinin sentezi organik kimyanın konusudur; anorganik kimya değildir.'),
     ('Cem, hücre içindeki enzimlerin katalizlediği tepkimeleri inceliyor. (Biyokimya)',True,'Canlıdaki kimyasal olaylar biyokimyanın konusudur.'),
     ('Deniz, tepkimelerde enerji değişimini inceliyor. (Organik kimya)',False,'Tepkimelerde enerji değişimini incelemek fizikokimyanın konusudur; organik kimya değildir.')]
m4,d4,a4=oncul([(a,b,c) for a,b,c in og4]); assert d4==[1,3]
s4=['Yalnız I','I ve III','II ve IV','I, II ve III','I, III ve IV']; assert s4[1]==kume(d4)
q('0004',a4+[A('Sonucu bul','Doğru eşleştirmeler I ve III’tür.',kume(d4))],
  tipId='km-kb2-altdal',tip='Olay–alt dal eşleştirme',z='orta',alt='Kimyanın Alt Dalları ve İlgi Alanları',kaz='Bir çalışmanın ilgili olduğu kimya alt dalını belirler.',kalip='öncüllü',
  kart='K-KMKB2-04 (alt dallar) · dört çalışma, I ve III doğru',
  metin='Bir kimya araştırma merkezinde çalışan dört bilim insanının çalışma konuları ve bu çalışmaların girdiği düşünülen kimya alt dalları aşağıda verilmiştir.\n'+m4+'\nBuna göre bu eşleştirmelerden hangileri doğrudur?',
  dogru=s4[1],sira=s4,
  yan=[(s4[0],'III’ü yanlış sanmış; enzim tepkimelerinin canlıdaki olay olduğunu ve biyokimyaya girdiğini bilmemiş.','bilgi'),
       (s4[2],'II ve IV’ü doğru, I ve III’ü yanlış sanmış; karbon bileşikleri ile enerji değişimini ilgili dallara bağlayamamış.','bilgi'),
       (s4[3],'II’yi doğru sanmış; karbon bileşiklerinin sentezini anorganik kimyaya yazmış.','bilgi'),
       (s4[4],'IV’ü doğru sanmış; enerji değişimini organik kimyaya bağlamış.','bilgi')],
  istenen='Doğru eşleştirmelerin belirlenmesi.',
  ip=['Her çalışmada incelenen şeyin ne olduğuna bak: madde miktarı mı, karbon bileşiği mi, canlıdaki olay mı, enerji mi?'],
  bilgi=[B('Kimyanın alt dalları','analitik kimya madde türü ve miktarını, organik kimya karbon bileşiklerini, biyokimya canlıdaki olayları, fizikokimya enerji ve fiziksel ilkeleri inceler')],
  puf='Alt dalı seçerken çalışmanın konusu olan "ne" sorusuna bak: miktar, karbon, canlı, enerji.')

# ===================================================== 05 · meslek (olumsuz kök) · kolay
kartla('05','Kimyacıların çalışma alanları','Kimyagerler ilaç, boya, gıda, kozmetik, çevre gibi sektörlerde sentez, analiz ve kalite kontrolü yapar; yapı statiği mühendislik hesabıdır.','Her teknik görevi kimyacıya yazmak.','kolay','düz',2,'meslek','Kimyacıların görev alanları')
s5=['İlaç etken maddesinin laboratuvarda sentezlenmesi','Gıdadaki katkı maddesi miktarının analiz edilmesi','Boya üretiminde ürün bileşiminin kontrol edilmesi','Köprü taşıyıcı kirişlerinin statik hesabının yapılması','İçme suyundaki kirleticilerin ölçülmesi']
q('0005',[A('Görev alanını hatırla','Kimyagerler madde sentezler, madde miktarını ve türünü analiz eder, ürün kalitesini kontrol eder.','sentez · analiz · kalite kontrol'),
          A('Şıkları ele','İlaç sentezi, katkı maddesi analizi, boya bileşimi kontrolü ve su kirleticisi ölçümü maddelerle ilgilidir.','A, B, C, E: kimyagerin işi'),
          A('Farklı olanı bul','Köprü kirişi hesabı yapı mühendisliğine aittir; madde incelemesi değildir.','D: kimya dışı')],
  tipId='km-kb2-meslek',tip='Kimyacıların görev alanları',z='kolay',alt='Kimyacıların Çalışma Alanları ve Meslekler',kaz='Kimyagerlerin çalışma alanlarını ve görevlerini ayırt eder.',kalip='düz',
  kart='K-KMKB2-05 (meslek) · kimya dışı görev',
  metin='Kimyagerler; ilaç, boya, gıda, kozmetik ve çevre gibi birçok sektörde görev alır. Kimya bölümünden yeni mezun olan bir öğrenci, kimyager olarak başvurabileceği iş ilanlarını incelemekte ve ilanlardaki görev tanımlarını bir listeye yazmaktadır. İlanların hepsinde, farklı sektörlerdeki bazı görev tanımları sıralanmıştır.\nBuna göre aşağıdakilerden hangisi bir kimyagerin görev alanında gösterilemez?',
  dogru=s5[3],sira=s5,
  yan=[(s5[0],'İlaç sentezini kimyanın dışında sanmış; organik kimyacılar etken madde sentezler.','bilgi'),
       (s5[1],'Gıdadaki madde miktarını bulmayı kimyacıya ait görmemiş; bu analitik kimya çalışmasıdır.','bilgi'),
       (s5[2],'Boyanın bileşimini kontrol etmeyi kimya dışı sanmış; bileşim incelemesi kimyacının işidir.','bilgi'),
       (s5[4],'Su kirleticilerini ölçmeyi kimyacıya ait görmemiş; bu bir analiz çalışmasıdır.','bilgi')],
  istenen='Kimyagerin görev alanında gösterilemeyen çalışma.',
  ip=['Kimyagerin işi madde üzerindedir: sentez, analiz, kalite kontrol. Şıklardan hangisi maddeyi değil başka bir alanı ilgilendiriyor?'],
  bilgi=[B('Kimyagerlerin çalışması','ilaç, boya, gıda, kozmetik ve çevre sektörlerinde madde sentezler, analiz eder, kalite kontrolü yapar. Örnek: boyadaki çözücü miktarının ölçülmesi')],
  puf='Kimyacının işi madde odaklıdır; kuvvet, yapı ve makine hesapları başka mühendislik alanlarına aittir.')

# ===================================================== 06 · element sembolleri (öncüllü) · kolay
kartla('06','Element sembolleri','Sodyum Na, potasyum K, demir Fe, cıva Hg, gümüş Ag, altın Au; sembolün bir ya da iki harften oluştuğu ve ilk harfin büyük, ikincinin küçük yazıldığı.','Sembolü ilk harflerden tahmin etmek (potasyumu P, gümüşü Gu yazmak).','kolay','öncüllü',3,'sembol','Element adı–sembol eşleştirme')
og6=[('Sodyum: Na',True,'Sodyumun sembolü Na’dır.'),('Potasyum: P',False,'Potasyumun sembolü K’dır; P fosforun sembolüdür.'),
     ('Demir: Fe',True,'Demirin sembolü Fe’dir.'),('Cıva: Hg',True,'Cıvanın sembolü Hg’dir.'),('Gümüş: Gu',False,'Gümüşün sembolü Ag’dir; Gu diye bir element sembolü yoktur.')]
m6,d6,a6=oncul([(a,b,c) for a,b,c in og6]); assert d6==[1,3,4]
s6=['Yalnız I','I ve III','II ve V','III ve IV','I, III ve IV']; assert s6[4]==kume(d6)
q('0006',a6+[A('Sonucu bul','Doğru yazımlar I, III ve IV’tür.',kume(d6))],
  tipId='km-kb2-sembol',tip='Element adı–sembol eşleştirme',z='kolay',alt='Element ve Bileşik Sembolleri',kaz='Yaygın elementlerin Türkçe adlarını sembolleriyle eşleştirir.',kalip='öncüllü',
  kart='K-KMKB2-06 (element sembolleri) · beş eşleştirme',
  metin='Bir öğrenci, kimya defterine bazı elementlerin Türkçe adlarını ve sembollerini aşağıdaki gibi yazmıştır.\n'+m6+'\nÖğretmeni defteri incelerken yazımları tek tek kontrol ediyor.\nBuna göre öğrencinin yazdıklarından hangileri doğrudur?',
  dogru=s6[4],sira=s6,
  yan=[(s6[0],'III ve IV’ü yanlış sanmış; demir ve cıvanın sembollerini bilmemiş.','bilgi'),
       (s6[1],'IV’ü yanlış sanmış; cıvanın sembolünün Hg olduğunu bilmemiş.','bilgi'),
       (s6[2],'II ve V’i doğru, diğerlerini yanlış sanmış; sembolü ilk harflerden tahmin etmiş.','bilgi'),
       (s6[3],'I’i yanlış sanmış; sodyumun sembolünün Na olduğunu bilmemiş.','bilgi')],
  istenen='Doğru yazılmış ad–sembol çiftlerinin belirlenmesi.',
  ip=['Bazı sembollerin Latince addan geldiğini hatırla; her yazımı tek tek sına.'],
  bilgi=[B('Element sembolleri','sembol bir ya da iki harften oluşur; ilk harf büyük, ikinci küçük yazılır. Örnek: kalsiyum Ca, altın Au, kurşun Pb')],
  puf='Sembol çoğu zaman adın baş harfi değildir: potasyum K, sodyum Na, cıva Hg, demir Fe.')

# ===================================================== 07 · günlük ad–formül (tablo, olumsuz kök) · orta
kartla('07','Bileşik formülleri ve günlük adlar','Sofra tuzu NaCl, kireç taşı CaCO₃, kostik NaOH, sönmemiş kireç CaO, kuru buz katı CO₂.','CO (karbon monoksit) ile CO₂ (karbon dioksit) karıştırmak.','orta','tablo',3,'gunlukad','Günlük ad–formül eşleştirme')
r7=[['Sofra tuzu','Sodyum klorür','NaCl'],['Kuru buz','Karbon dioksit','CO'],['Kireç taşı','Kalsiyum karbonat','CaCO₃'],['Kostik','Sodyum hidroksit','NaOH'],['Sönmemiş kireç','Kalsiyum oksit','CaO']]
SK7=tablo_svg(['Günlük ad','Kimyasal ad','Formül'],r7)
s7=[r[0] for r in r7]
q('0007',[A('Her satırı çöz','Adlardaki ön eklere ve köklere göre formülü kur: klorür Cl, karbonat CO₃, hidroksit OH, oksit O.','NaCl · CaCO₃ · NaOH · CaO doğru'),
          A('Karbon dioksiti incele','Karbon dioksitte karbona iki oksijen bağlıdır; formülü CO₂ olmalıdır.','karbon dioksit = CO₂'),
          A('Hatalı satırı bul','Tablodaki CO, karbon monoksiti gösterir; kuru buz satırındaki formül hatalıdır.','Kuru buz satırı yanlış')],
  tipId='km-kb2-gunlukad',tip='Günlük ad–formül eşleştirme',z='orta',alt='Element ve Bileşik Sembolleri',kaz='Günlük hayatta kullanılan maddelerin kimyasal adlarını ve formüllerini eşleştirir.',kalip='tablo',
  kart='K-KMKB2-07 (günlük adlar) · kuru buz CO yazılmış',
  metin='Bir kimya öğretmeni, günlük hayatta ve sanayide sık kullanılan bazı maddelerin günlük adlarını, kimyasal adlarını ve formüllerini öğrencilere aşağıdaki tabloyla vermiştir. Öğrenciler tabloyu defterlerine geçirirken öğretmen, satırlardan birinde bir formülün hatalı yazıldığını fark etmiştir.\nBuna göre hangi maddenin satırındaki bilgi yanlıştır?',
  dogru=s7[1],sira=s7,sekil=SK7,
  yan=[(s7[0],'Sofra tuzunun sodyum klorür olduğunu ve formülünün NaCl olduğunu bilmeyerek bu satırı hatalı bulmuş.','bilgi'),
       (s7[2],'Karbonat iyonunu bilmemiş; kireç taşının formülü CaCO₃’tür ve satır doğrudur.','bilgi'),
       (s7[3],'Hidroksit grubunun OH olduğunu bilmemiş; kostiğin formülü NaOH’tır ve satır doğrudur.','bilgi'),
       (s7[4],'Oksit adının yalnız oksijen içeren bileşiği gösterdiğini bilmemiş; kalsiyum oksit CaO’dur ve satır doğrudur.','bilgi')],
  istenen='Formülü ya da adı hatalı verilen madde.',
  ip=['Adlardaki ön ekler atom sayısını gösterir; her satırda adı formülle karşılaştır.'],
  bilgi=[B('Bileşik adları','klorür Cl, oksit O, hidroksit OH, karbonat CO₃ içerir; di-, tri- gibi ön ekler atom sayısını gösterir. Örnek: magnezyum klorür MgCl₂')],
  puf='Formülü ezberlemek yerine adın parçalarını formüle çevir.')

# ===================================================== 08 · denkleştirme ve atom sayısı · zor
kartla('08','Denkleştirme ve atom sayısı','Önce Al, S, H, O sırasıyla katsayıları bul; girenlerde atom sayısı katsayı × birim başına atom toplamıdır.','Katsayıları atom sayısı sanmak; parantez dışı indisi tüm grup yerine tek atoma uygulamak.','zor','düz',5,'denkles','Denkleştirme ve atom sayısı')
import itertools
# Al(OH)3 + H2SO4 -> Al2(SO4)3 + H2O : Al: a=2c ; S: b=3c ; O: 3a+4b=12c+d ; H: 3a+2b=2d
sol=[(a,b,c,d) for a,b,c,d in itertools.product(range(1,13),repeat=4) if a==2*c and b==3*c and 3*a+4*b==12*c+d and 3*a+2*b==2*d]
sol=[x for x in sol if x[2]==1]; assert sol==[(2,3,1,6)]
a_,b_,c_,d_=sol[0]; per1=1+3+3; per2=2+1+4; per3=2+3+12; assert per1==7 and per2==7 and per3==17
tot=a_*per1+b_*per2; assert tot==35 and c_*per3+d_*3==35
w14=per1+per2; w21=b_*per2; w31=a_*5+b_*per2; w12=a_+b_+c_+d_
assert (w14,w21,w31,w12)==(14,21,31,12) and len({w12,w14,w21,w31,tot})==5
q('0008',[A('Alüminyum ve kükürdü eşitle','Ürünlerde Al₂(SO₄)₃ biriminde 2 Al ve 3 S vardır; bu yüzden Al(OH)₃ ve H₂SO₄ katsayıları 2 ve 3 olur.','Al: 2 · S: 3'),
          A('H₂O’yu bul','Girenlerde 2 × 3 + 3 × 2 = 12 H bulunur; her H₂O iki H taşıdığı için 6 H₂O gerekir.','H: 12 → 6H₂O'),
          A('Oksijeni kontrol et','Girenlerde 6 + 12 = 18 O, ürünlerde 12 + 6 = 18 O vardır; denklem denkleşir.','2Al(OH)₃ + 3H₂SO₄ → Al₂(SO₄)₃ + 6H₂O'),
          A('Birim atomlarını say','Al(OH)₃ biriminde 1 + 3 + 3 = 7, H₂SO₄ biriminde 2 + 1 + 4 = 7 atom vardır.','7 ve 7'),
          A('Girenleri topla','Katsayılarla çarpılıp toplanır.','2 × 7 + 3 × 7 = 35')],
  tipId='km-kb2-denkles',tip='Denkleştirme ve atom sayısı',z='zor',alt='Element ve Bileşik Sembolleri',kaz='Kimyasal denklemi denkleştirir ve formüllerdeki atom sayılarını bulur.',kalip='düz',
  kart='K-KMKB2-08 (denkleştirme) · Al(OH)₃ + H₂SO₄ tepkimesi, girenlerde toplam atom',
  metin='Bir ilaç laboratuvarında, mide ekşimesine karşı kullanılan antasit tabletlerin etken maddesi olan alüminyum hidroksitin tepkimeleri inceleniyor. Alüminyum hidroksit, laboratuvarda sülfürik asitle tepkimeye girerek alüminyum sülfat ve su oluşturmaktadır.\nAl(OH)₃ + H₂SO₄ → Al₂(SO₄)₃ + H₂O\nTepkime denklemi en küçük tam sayılarla denkleştirildiğinde girenler tarafında toplam kaç atom bulunur?',
  dogru=tot,yan=[(w12,'Katsayıların toplamını (2 + 3 + 1 + 6) atom sayısı sanmış.','dikkat'),
                 (w14,'Katsayıları kullanmayıp girenlerdeki iki formülün atomlarını (7 + 7) toplamış.','dikkat'),
                 (w21,'Yalnız H₂SO₄’nin katsayısıyla işlem yapmış (3 × 7), Al(OH)₃’ü hesaba katmamış.','islem'),
                 (w31,'Al(OH)₃’teki indisi (3) yalnız H atomuna uygulayıp birimi 5 atom saymış (2 × 5 + 3 × 7).','bilgi')],
  istenen='Denkleştirilmiş denklemde girenlerdeki toplam atom sayısı.',
  ip=['Önce Al ve S atomlarını ürün tarafındaki Al₂(SO₄)₃ birimine göre eşitle; hidrojeni ve oksijeni en son say.'],
  bilgi=[B('Atom sayma','katsayı tüm formül birimini, parantez dışındaki indis parantezin içindeki her atomu çoğaltır. Örnek: 2Ca(OH)₂ içinde 2 Ca, 4 O ve 4 H vardır')],
  puf='Denkleştirmede en çok geçen atom (burada Al ve S) kilit rol oynar; H ve O’yu sona bırak.')

# ===================================================== 09 · uyarı işaretleri (şekil) · orta
kartla('09','Laboratuvar güvenliği · uyarı işaretleri','Alev işareti yanıcı; kuru kafa zehirli; aşındırıcı işareti dokuya ve metale zarar veren; ünlem tahriş edici/dikkat anlamına gelir.','Aşındırıcı ile zehirli işaretini karıştırmak.','orta','şekilli',3,'uyari','Uyarı işaretleri')
def elmas(cx,cy=0,r=1.05): return f'\\draw[thick] ({cx},{cy+r}) -- ({cx+r},{cy}) -- ({cx},{cy-r}) -- ({cx-r},{cy}) -- cycle;\n'
def alev(cx,cy=0):
    dis=[(0,-.52),(.3,-.4),(.42,-.08),(.3,.18),(.2,.3),(.3,.6),(.02,.42),(-.18,.22),(-.4,-.08),(-.3,-.4)]
    ic=[(0,-.38),(.16,-.26),(.06,-.02),(-.1,-.1),(-.14,-.28)]
    p1=' '.join(f'({cx+x:.2f},{cy+y:.2f})' for x,y in dis); p2=' '.join(f'({cx+x:.2f},{cy+y:.2f})' for x,y in ic)
    return f'\\fill[even odd rule] plot[smooth cycle,tension=.7] coordinates {{{p1}}} plot[smooth cycle,tension=.7] coordinates {{{p2}}};\n'
def kuru(cx,cy=0):
    t=f'\\draw[thick] ({cx},{cy+.18}) circle (.3);\\fill ({cx-.11},{cy+.2}) circle (.07);\\fill ({cx+.11},{cy+.2}) circle (.07);\n'
    t+=f'\\draw[thick] ({cx-.15},{cy-.1}) -- ({cx-.15},{cy-.22}) -- ({cx+.15},{cy-.22}) -- ({cx+.15},{cy-.1});\n'
    t+=f'\\draw[line width=2pt] ({cx-.38},{cy-.45}) -- ({cx+.38},{cy-.12});\\draw[line width=2pt] ({cx-.38},{cy-.12}) -- ({cx+.38},{cy-.45});\n'
    return t
def asinma(cx,cy=0):
    t=f'\\draw[line width=2.4pt] ({cx-.62},{cy+.6}) -- ({cx-.32},{cy+.4});\\draw[line width=2.4pt] ({cx+.62},{cy+.6}) -- ({cx+.32},{cy+.4});\n'
    for dx in (-.3,.3):
        for dy in (.2,-.02): t+=f'\\fill ({cx+dx},{cy+dy}) circle (.06);\n'
    t+=f'\\draw[thick] ({cx-.62},{cy-.55}) -- ({cx-.62},{cy-.3}) -- ({cx-.4},{cy-.3}) -- ({cx-.34},{cy-.42}) -- ({cx-.27},{cy-.3}) -- ({cx-.05},{cy-.3}) -- ({cx-.05},{cy-.55}) -- cycle;\n'
    t+=f'\\draw[thick] ({cx+.05},{cy-.55}) -- ({cx+.05},{cy-.3}) -- ({cx+.62},{cy-.3}) -- ({cx+.62},{cy-.55}) -- cycle;\n'
    for fx in (.1,.24,.38,.52): t+=f'\\draw[thick] ({cx+fx},{cy-.3}) -- ({cx+fx},{cy-.14});\n'
    return t
def unlem(cx,cy=0):
    return f'\\fill ({cx-.1},{cy+.5}) -- ({cx+.1},{cy+.5}) -- ({cx+.05},{cy-.12}) -- ({cx-.05},{cy-.12}) -- cycle;\\fill ({cx},{cy-.35}) circle (.1);\n'
g=''
for i,(fn,r) in enumerate(((alev,'I'),(kuru,'II'),(asinma,'III'),(unlem,'IV'))):
    cx=i*2.4; g+=elmas(cx)+fn(cx)+f'\\node at ({cx},-1.45) {{\\textbf{{{r}}}}};\n'
SK9=tk(g)
s9=['I – III','I – IV','II – III','III – I','IV – III']
q('0009',[A('Birinci kimyasalı çöz','Açık alevle tutuşabilen madde "yanıcı" sınıfındadır; yanıcı işareti alevdir.','yanıcı → alev → I'),
          A('İkinci kimyasalı çöz','Doku ve metale zarar veren madde "aşındırıcı" sınıfındadır; işareti aşınan yüzey ve damlalardır.','aşındırıcı → III'),
          A('Sırayı yaz','İşaretler soruda verilen şişe sırasıyla yazılır.','I – III')],
  tipId='km-kb2-uyari',tip='Uyarı işaretleri',z='orta',alt='Laboratuvar Güvenliği ve Malzemeleri',kaz='Kimyasal madde etiketlerindeki uyarı işaretlerini tanır ve maddenin özelliğiyle eşleştirir.',kalip='şekilli',
  kart='K-KMKB2-09 (uyarı işaretleri) · yanıcı ve aşındırıcı şişe',
  metin='Bir okul laboratuvarının depo görevlisi, yeni gelen iki şişeyi etiketlemektedir. Birinci şişedeki çözücü, açık alev ve kıvılcım yakınında tutuşabilmektedir. İkinci şişedeki derişik çözelti ise cilde ve metale temas ettiğinde onlara zarar vermektedir. Görevli, her şişeye o şişenin ana tehlikesini gösteren işareti yapıştırmak istemektedir.\nGörevlinin, bu şişelerin etiketlerine sırasıyla yukarıdaki hangi işaretleri yapıştırması gerekir?',
  dogru=s9[0],sira=s9,sekil=SK9,
  yan=[(s9[1],'İkinci şişede aşındırıcı yerine ünlem işaretini seçmiş; ünlem hafif tahriş ve dikkat içindir.','bilgi'),
       (s9[2],'Birinci şişe için kuru kafayı seçmiş; açık alevle tutuşma tehlikesi zehirlilik değildir.','bilgi'),
       (s9[3],'İşaretleri şişelerle ters eşleştirmiş.','dikkat'),
       (s9[4],'Birinci şişede ünlem işaretini seçmiş; tutuşma tehlikesini yanıcı işaretiyle karıştırmış.','bilgi')],
  istenen='Şişelere sırasıyla yapıştırılacak uyarı işaretleri.',
  ip=['Birinci şişenin tehlikesi alevle ilgili, ikincisinin tehlikesi temas ettiği yüzeyi aşındırmakla ilgilidir; işaretlerin çizimlerini bu özelliklerle karşılaştır.'],
  bilgi=[B('Uyarı işaretleri','alev yanıcı, kuru kafa zehirli, aşınan yüzey ve damlalar aşındırıcı, ünlem tahriş edici ya da dikkat edilmesi gereken madde anlamına gelir')],
  puf='Uyarı işaretini görüntüsünden değil, anlattığı tehlikeden (yanma, zehirleme, aşındırma) hatırla.')

# ===================================================== 10 · dereceli silindir okuma (şekil) · kolay
kartla('10','Hacim ölçme ve dereceli silindir','Dereceli silindirde seviye farkı katı cisimlerin toplam hacmidir; parça sayısına bölünür.','Son okumayı ya da toplamı doğrudan kullanmak; parça sayısına bölmeyi unutmak.','kolay','şekilli',3,'silindir','Dereceli silindirle hacim okuma')
V1,V2,npar=35,65,2; vh=Fr(V2-V1,npar); assert vh==15
def cyl(x,level,parca=0,ad=''):
    sc=.06; Ht=80*sc; t=f'\\fill[vurgu!15] ({x},.15) rectangle ({x+.8},{.15+level*sc:.3f});\n'
    t+=f'\\draw[thick] ({x},{Ht+.15:.2f}) -- ({x},.15) -- ({x+.8},.15) -- ({x+.8},{Ht+.15:.2f});\\draw[thick] ({x-.2},0) rectangle ({x+1.0},.15);\n'
    for v in range(5,81,5):
        y=.15+v*sc; ln=.3 if v%10==0 else .15
        t+=f'\\draw ({x+.8},{y:.3f}) -- ({x+.8-ln:.2f},{y:.3f});\n'
        if v%10==0: t+=f'\\node[font=\\scriptsize,anchor=east] at ({x-.05},{y:.3f}) {{{v}}};\n'
    t+=f'\\draw[thick,vurgu] ({x},{.15+level*sc:.3f}) -- ({x+.8},{.15+level*sc:.3f});\n'
    for k in range(parca): t+=f'\\filldraw[fill=gray!50] ({x+.28+k*.28:.2f},.3) circle (.11);\n'
    t+=f'\\node at ({x+.4},-.4) {{{ad}}};\n'
    return t
SK10=tk(cyl(0,V1,0,'Önce')+cyl(2.6,V2,npar,'Sonra'))
v10=[Fr(30),Fr(65,2),Fr(50),Fr(100)]
assert V2-V1==30 and Fr(V2,npar)==Fr(65,2) and Fr(V1+V2,npar)==50 and V1+V2==100 and len({vh}|set(v10))==5
q('0010',[A('İlk seviyeyi oku','Silindirdeki su seviyesi çizimde 35 mL’ye gelmiştir.','V₁ = 35 mL'),
          A('İkinci seviyeyi oku','Parçalar atıldıktan sonra seviye 65 mL’ye çıkmıştır.','V₂ = 65 mL'),
          A('Seviye farkını bul','Yükselme, parçaların toplam hacmine eşittir.','65 − 35 = 30 mL'),
          A('Parça sayısına böl','Parçalar özdeş olduğu için her birinin hacmi eşittir.','30 : 2 = 15 mL')],
  tipId='km-kb2-silindir',tip='Dereceli silindirle hacim okuma',z='kolay',alt='Laboratuvar Güvenliği ve Malzemeleri',kaz='Dereceli silindirdeki sıvı seviyelerini okuyarak katı cismin hacmini bulur.',kalip='şekilli',sekil=SK10,
  kart='K-KMKB2-10 (dereceli silindir) · iki özdeş parçanın hacmi',
  metin='Bir kimya laboratuvarında öğrenci, suda çözünmeyen ve suya tamamen batan iki özdeş katı parçanın hacmini bulmak istemektedir. Bu amaçla dereceli silindirdeki suyun seviyesini, parçaları silindire atmadan önce ve attıktan sonra okumuştur. Parçalar atılırken silindirden hiç su taşmamıştır.\nBuna göre bu parçalardan her birinin hacmi kaç mL’dir?',
  dogru=vh,yan=[(v10[0],'Seviye farkını (30 mL) parça sayısına bölmeyi unutmuş.','dikkat'),
                (v10[1],'Son okumayı (65 mL) parça sayısına bölmüş; başlangıçtaki suyun hacmini çıkarmamış.','islem'),
                (v10[2],'İki okumayı toplayıp (100 mL) parça sayısına bölmüş.','islem'),
                (v10[3],'İki okumayı toplamış; seviye farkını almamış.','islem')],
  istenen='Parçalardan her birinin hacmi (mL).',
  ip=['Parçalar suya batınca seviyedeki yükselme neye eşittir? Sonra parça sayısını düşün.'],
  bilgi=[B('Dereceli silindirde hacim','katı bir cisim suya tamamen batınca su seviyesi cismin hacmi kadar yükselir; hacim, iki seviye farkı alınarak bulunur')],
  puf='Batan cismin hacmi = son seviye − ilk seviye; birden çok özdeş cisim varsa sonra bölünür.')

# ===================================================== 11 · sağlık etkileri (öncüllü) · orta
kartla('11','Kimyasalların sağlığa etkisi','Fe hemoglobinde, Ca kemik ve dişte bulunur; Cu iz element; Pb, Hg, Cd vücuda gerekmez, birikince zehirlidir.','Kurşunu gerekli mineral saymak.','kolay','öncüllü',4,'saglik','Elementlerin insan sağlığına etkisi')
og11=[('Demir, kanda oksijen taşıyan hemoglobinin yapısında bulunur.',True,'Hemoglobinde demir bulunur; eksikliği kansızlığa yol açabilir.'),
      ('Kalsiyum, kemik ve dişlerin yapısında bulunur.',True,'Kemik ve dişlerin yapısında kalsiyum vardır.'),
      ('Bakır, vücut için çok az miktarda gerekli olan bir iz elementtir.',True,'Bakır çok az miktarda gerekli iz elementtir.'),
      ('Kurşun, vücutta bulunması gereken bir mineraldir ve eksikliğinde kansızlık görülür.',False,'Kurşun vücuda gerekli değildir; birikince sağlığa zarar verir.')]
m11,d11,a11=oncul([(a,b,c) for a,b,c in og11]); assert d11==[1,2,3]
s11=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']; assert s11[4]==kume(d11)
q('0011',a11+[A('Sonucu bul','Doğru ifadeler I, II ve III’tür.',kume(d11))],
  tipId='km-kb2-saglik',tip='Elementlerin insan sağlığına etkisi',z='kolay',alt='Kimyasal Maddelerin İnsan Sağlığına Etkileri',kaz='Bazı elementlerin insan sağlığındaki rolünü ve zararlı etkilerini açıklar.',kalip='öncüllü',
  kart='K-KMKB2-11 (sağlığa etkiler) · Fe, Ca, Cu doğru; Pb yanlış',
  metin='Bir sağlık bilgisi dersinde, insan sağlığı açısından önemli bazı elementlerle ilgili aşağıdaki ifadeler yazılıyor.\n'+m11+'\nBuna göre bu ifadelerden hangileri doğrudur?',
  dogru=s11[4],sira=s11,
  yan=[(s11[0],'II ve III’ü yanlış sanmış; kalsiyumun kemikte ve bakırın iz element olduğunu bilmemiş.','bilgi'),
       (s11[1],'III’ü yanlış sanmış; bakırın az miktarda gerekli iz element olduğunu bilmemiş.','bilgi'),
       (s11[2],'II’yi yanlış sanmış; kalsiyumun kemik ve diş yapısındaki yerini bilmemiş.','bilgi'),
       (s11[3],'I’i yanlış sanmış; demirin hemoglobinde bulunduğunu bilmemiş.','bilgi')],
  istenen='Doğru ifadelerin belirlenmesi.',
  ip=['Elementleri vücut için gerekli olanlar ve gerekli olmayıp zehirli etki yapanlar diye ikiye ayırarak düşün.'],
  bilgi=[B('Elementler ve sağlık','demir hemoglobinde, kalsiyum kemik ve dişte bulunur; bakır ve çinko iz elementtir; kurşun, cıva ve kadmiyum vücuda gerekmez ve birikince zehirlidir')],
  puf='Gerekli mineraller (Na, K, Ca, Mg, Fe, Cu, Zn) ile zehirli ağır metaller (Pb, Hg, Cd) ayrı grupta düşünülür.')

# ===================================================== 12 · sağlık (tablo) · orta
kartla('12','Kimyasalların sağlığa etkisi · durum–element','Hemoglobin düşüklüğü demir eksikliğiyle, kemik zayıflığı kalsiyum eksikliğiyle, cıva buharı soluma zehirlenmeyle ilişkilidir.','Elementlerin etkilerini birbirine karıştırmak.','kolay','tablo',3,'durum','Durum–element ilişkilendirme')
r12=[['Ali','Hemoglobin değeri düşük, sürekli halsiz'],['Elif','Cıvalı termometreyi kırdı, buharını soludu'],['Mert','Kemikleri zayıfladı, dişleri çabuk çürüyor']]
SK12=tablo_svg(['Kişi','Durum'],r12)
doğru12=('Fe','Hg','Ca'); perm=[' – '.join(p) for p in sorted(itertools.permutations(['Fe','Hg','Ca']))]
s12=['Ca – Fe – Hg','Ca – Hg – Fe','Fe – Ca – Hg','Fe – Hg – Ca','Hg – Fe – Ca']; assert ' – '.join(doğru12)==s12[3] and set(s12)<=set(perm) and len(set(s12))==5
q('0012',[A('Ali’nin durumu','Hemoglobin düşüklüğü, hemoglobinde bulunan demirin eksikliğiyle ilişkilidir.','Ali → Fe'),
          A('Elif’in durumu','Cıva buharını solumak, ağır metal olan cıvayla zehirlenmeye yol açar.','Elif → Hg'),
          A('Mert’in durumu','Kemik ve diş zayıflığı kalsiyum eksikliğiyle ilişkilidir.','Mert → Ca'),
          A('Sırayı yaz','Kişilerin sırasıyla Ali, Elif, Mert olarak yazılır.','Fe – Hg – Ca')],
  tipId='km-kb2-durum',tip='Durum–element ilişkilendirme',z='kolay',alt='Kimyasal Maddelerin İnsan Sağlığına Etkileri',kaz='Sağlıkla ilgili bir durumu ilişkili olduğu elementin sembolüyle eşleştirir.',kalip='tablo',
  kart='K-KMKB2-12 (durum–element) · Fe, Hg, Ca',
  metin='Bir aile sağlığı merkezinde çalışan hekim, üç hastanın muayene sırasında aldığı notları bir tabloya geçirmiştir. Tablodaki durumların her biri, vücutta bir elementin eksik ya da fazla bulunmasıyla ilişkilendirilebilmektedir.\nBu durumlarla en doğrudan ilişkili olan elementlerin sembolleri, Ali, Elif ve Mert için sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
  dogru=s12[3],sira=s12,sekil=SK12,
  yan=[(s12[0],'Ali’yi kalsiyumla, Elif’i demirle, Mert’i cıvayla ilişkilendirmiş; üç eşleştirmeyi de kuramamış.','bilgi'),
       (s12[1],'Ali’yi kalsiyumla ilişkilendirmiş; hemoglobin düşüklüğünün demirle ilgili olduğunu bilmemiş.','bilgi'),
       (s12[2],'Elif ile Mert’i ters eşleştirmiş; cıva buharını kemik zayıflığıyla karıştırmış.','dikkat'),
       (s12[4],'Ali’yi cıvayla, Elif’i demirle ilişkilendirmiş; cıvanın buhar soluma durumuyla ilgisini kuramamış.','bilgi')],
  istenen='Ali, Elif ve Mert için ilişkili element sembolleri (sırasıyla).',
  ip=['Hemoglobin, kemik–diş yapısı ve cıva buharı için her birinin hangi elementle bağlantılı olduğunu ayrı ayrı düşün.'],
  bilgi=[B('Elementlerin sağlığa etkisi','demir hemoglobinde, kalsiyum kemik ve dişte bulunur; cıva ağır metaldir, buharı sinir sistemine zarar verir. Örnek: demir eksikliğinde kansızlık görülebilir')],
  puf='Sembolü ve görevi birlikte öğren: Fe–kan, Ca–kemik, Hg–zehirlenme.')

# ===================================================== 13 · şişeler, ağır metal (şekil) · zor
kartla('13','Ağır metaller','Hg, Pb, Cd vücuda gerekmeyen ve birikerek zehirli etki yapan ağır metallerdir; Na, Ca, Fe gerekli elementlerdir.','Demiri (Fe) ağır metal grubuna yazmak.','orta','şekilli',4,'agirmetal','Zehirli ağır metaller')
sy13=['Na','Hg','Ca','Pb','Fe','Cd']; zeh13={2,4,6}
assert {i+1 for i,s in enumerate(sy13) if s in ('Hg','Pb','Cd')}==zeh13
def sise(cx,sy,no):
    t=f'\\draw[thick,rounded corners=3pt] ({cx-.5},0) rectangle ({cx+.5},1.2);\\draw[thick] ({cx-.2},1.2) rectangle ({cx+.2},1.55);\\draw[thick] ({cx-.27},1.55) rectangle ({cx+.27},1.7);\n'
    t+=f'\\draw ({cx-.4},.2) rectangle ({cx+.4},.85);\\node at ({cx},.52) {{\\textbf{{{sy}}}}};\\node at ({cx},-.4) {{\\textbf{{{RM[no]}}}}};\n'
    return t
SK13=tk(''.join(sise(i*1.45,s,i+1) for i,s in enumerate(sy13)))
s13=[{1,2,4},{2,4,5},{2,4,6},{2,5,6},{3,4,6}]
assert s13[2]==zeh13 and s13==sorted(s13,key=lambda a:sorted(a))
lab13=[kume(sorted(x)) for x in s13]
q('0013',[A('Elementleri tanı','Şişelerde I Na, II Hg, III Ca, IV Pb, V Fe, VI Cd sembolleri yazılıdır.','Na · Hg · Ca · Pb · Fe · Cd'),
          A('Gerekli olanları ayır','Sodyum, kalsiyum ve demir vücuda gerekli elementlerdir.','Na, Ca, Fe: gerekli'),
          A('Zehirli olanları seç','Cıva, kurşun ve kadmiyum vücuda gerekmeyen, birikerek zehirli etki yapan ağır metallerdir.','Hg, Pb, Cd'),
          A('Numaralara çevir','Hg II, Pb IV ve Cd VI numaralı şişelerdedir.','II, IV ve VI')],
  tipId='km-kb2-agirmetal',tip='Zehirli ağır metaller',z='orta',alt='Kimyasal Maddelerin İnsan Sağlığına Etkileri',kaz='Vücuda gerekli elementler ile zehirli ağır metalleri ayırt eder.',kalip='şekilli',
  kart='K-KMKB2-13 (ağır metaller) · altı şişe, üç zehirli',
  metin='Bir üniversite laboratuvarında, etiketlerinde yalnızca element sembolleri bulunan altı şişe atık depolama bölümüne getirilmiştir. Laboratuvar sorumlusu, atık yönetmeliğine göre vücuda gerekli olmayan ve canlıda birikerek zehirli etki yapan ağır metallerin bulunduğu şişelerin özel atık kutusuna konacağını, diğerlerinin ise normal depoya kaldırılacağını belirtmiştir.\nBuna göre özel atık kutusuna hangi numaralı şişeler konmalıdır?',
  dogru=lab13[2],sira=lab13,sekil=SK13,
  yan=[(lab13[0],'Sodyumu (I) ağır metal saymış; kadmiyumu (VI) atlamış.','bilgi'),
       (lab13[1],'Demiri (V) ağır metal saymış; demir vücuda gerekli bir elementtir. Kadmiyumu da atlamış.','bilgi'),
       (lab13[3],'Demiri (V) ağır metal saymış; kurşunun (IV) zehirli olduğunu gözden kaçırmış.','bilgi'),
       (lab13[4],'Kalsiyumu (III) ağır metal saymış; cıvayı (II) atlamış.','bilgi')],
  istenen='Özel atık kutusuna konacak şişelerin numaraları.',
  ip=['Sembollerden elementleri bul, sonra vücuda gerekli olanları ayır; geriye kalanların ortak özelliğini düşün.'],
  bilgi=[B('Ağır metaller','cıva, kurşun ve kadmiyum vücuda gerekmez, birikince zehirli etki yapar; demir, kalsiyum ve sodyum ise gerekli elementlerdir')],
  puf='Pb, Hg ve Cd’yi zehirli ağır metal üçlüsü olarak aklında tut.')

# ===================================================== 14 · formül, öncüllü atom sayıları · orta
kartla('14','Formülde atom sayıları','Katsayı bütün birimi, parantez dışı indis parantez içini çoğaltır.','Parantez dışı indisi yalnız bir atoma uygulamak.','orta','öncüllü',4,'formulsay','Formülde atom sayıları (öncüllü)')
nCa,nN,nO=1,2,6; unit=nCa+nN+nO; k14=3
assert unit==9 and k14*unit==27 and k14*nN==6 and k14*nO==18 and k14*nCa==3
og14=[('3Ca(NO₃)₂ ifadesinde toplam 27 atom vardır.',True,'Bir birimde 1 + 2 + 6 = 9 atom vardır; 3 × 9 = 27.'),
      ('3Ca(NO₃)₂ ifadesinde 3 tane azot atomu vardır.',False,'Bir birimde 2 azot vardır; 3 birimde 6 azot atomu bulunur.'),
      ('3Ca(NO₃)₂ ifadesinde 18 tane oksijen atomu vardır.',True,'Bir birimde 6 oksijen vardır; 3 × 6 = 18.'),
      ('3Ca(NO₃)₂ ifadesinde kalsiyum atomu sayısı azot atomu sayısına eşittir.',False,'Kalsiyum 3, azot 6 tanedir; eşit değildir.')]
m14,d14,a14=oncul([(a,b,c) for a,b,c in og14]); assert d14==[1,3]
s14=['I ve III','II ve III','I, II ve III','I, III ve IV','II, III ve IV']; assert s14[0]==kume(d14)
q('0014',a14+[A('Sonucu bul','Doğru ifadeler I ve III’tür.',kume(d14))],
  tipId='km-kb2-formulsay',tip='Formülde atom sayıları (öncüllü)',z='orta',alt='Element ve Bileşik Sembolleri',kaz='Katsayı ve indisleri kullanarak formüldeki atom sayılarını yorumlar.',kalip='öncüllü',
  kart='K-KMKB2-14 (formül atom sayıları) · 3Ca(NO₃)₂',
  metin='Tarımda azot ve kalsiyum kaynağı olarak kullanılan bir gübrenin ana bileşeni olan kalsiyum nitratın formülü Ca(NO₃)₂’dir. Bir öğrenci, 3Ca(NO₃)₂ gösterimiyle ilgili aşağıdaki ifadeleri yazmıştır.\n'+m14+'\nBuna göre öğrencinin yazdıklarından hangileri doğrudur?',
  dogru=s14[0],sira=s14,
  yan=[(s14[1],'Parantez dışındaki 2’yi N’ye uygulamayı unutup azotu 3 saymış; toplamı 24 bulup I’i yanlış saymış, IV’ü gözden kaçırmış.','bilgi'),
       (s14[2],'II’yi doğru sanmış; azot atomu sayısını yalnız katsayıya (3) eşitlemiş.','bilgi'),
       (s14[3],'IV’ü doğru sanmış; kalsiyum ile azot atom sayılarını eşit bulmuş.','bilgi'),
       (s14[4],'Azotu 3 sayıp kalsiyumla eşitlemiş; toplamı 24 bulup I’i yanlış saymış.','bilgi')],
  istenen='Doğru ifadelerin belirlenmesi.',
  ip=['Önce bir Ca(NO₃)₂ biriminde her atomdan kaç tane olduğunu say, sonra katsayıyla çarp.'],
  bilgi=[B('Atom sayıları','katsayı tüm formül birimini çoğaltır; parantezin dışındaki indis parantezin içindeki bütün atomları çoğaltır. Örnek: 2Fe(OH)₃ içinde 6 O vardır')],
  puf='Atomları önce tek birimde, sonra katsayıyla çarparak say.')

# ===================================================== 15 · beş ifade, kaç doğru · zor
kartla('15','Sembolik dil ve laboratuvar bilgisi karması','Günlük ad, atom sayısı, laboratuvar malzemesi, bileşik formülü ve element sembolü bilgilerinin her biri ayrı doğrulanır.','Bir ifadeyi ezbere doğru sanıp işlemini yapmamak.','orta','öncüllü',5,'karma','Karma ifade değerlendirme')
og15=[('NaCl bileşiğinin günlük hayattaki adı sofra tuzudur.',True,'NaCl sodyum klorürdür; günlük adı sofra tuzudur.'),
      ('2H₂O ifadesinde toplam 6 atom vardır.',True,'Bir H₂O’da 3 atom vardır; 2 × 3 = 6.'),
      ('Beherglas, sıvı hacmini hassas ölçmek için kullanılan malzemedir.',False,'Hassas hacim ölçümü dereceli silindirle yapılır; beherin bölmeleri yaklaşık değer verir.'),
      ('Kireç taşının formülü CaCO₃’tür.',True,'Kireç taşı kalsiyum karbonattır; formülü CaCO₃’tür.'),
      ('Fe sembolü flor elementini gösterir.',False,'Fe demirin sembolüdür; florun sembolü F’dir.')]
m15,d15,a15=oncul([(a,b,c) for a,b,c in og15]); assert d15==[1,2,4] and len(d15)==3
q('0015',a15+[A('Sayıyı bul','Doğru ifadelerin sayısı yazılır.','I, II ve IV doğru → 3')],
  tipId='km-kb2-karma',tip='Karma ifade değerlendirme',z='orta',alt='Kimyanın Sembolik Dili ve Laboratuvar',kaz='Kimyanın sembolik dili ve laboratuvar bilgileriyle ilgili ifadeleri değerlendirir.',kalip='öncüllü',
  kart='K-KMKB2-15 (karma değerlendirme) · beş ifade, üçü doğru',
  metin='Kimya laboratuvarı kullanım kılavuzunun sonunda öğrencilerin bilgisini sınamak için aşağıdaki beş ifade verilmiştir.\n'+m15+'\nBuna göre bu ifadelerden kaç tanesi doğrudur?',
  dogru=3,yan=[(1,'Yalnız bir ifadeyi doğru bulmuş; sembol ve formül bilgilerini işleme koymamış.','bilgi'),
               (2,'II’yi yanlış sayarak iki ifade bulmuş; 2H₂O’yu 4 atom sanmış.','islem'),
               (4,'III’ü doğru sanmış; beherglasın hassas hacim ölçümü için kullanıldığını düşünmüş.','bilgi'),
               (5,'Hiçbir ifadeyi yanlış bulmamış; Fe sembolünü ve beherglasın işlevini kontrol etmemiş.','dikkat')],
  istenen='Doğru ifadelerin sayısı.',
  ip=['Her ifadeyi ayrı ayrı sına: ad ve formül bilgilerini tek tek kontrol et, atom sayısını katsayıyla çarparak hesapla.'],
  bilgi=[B('Sembolik dil','ad, sembol ve formül bilgileri tek tek doğrulanır; katsayı bütün formül birimini çoğaltır')],
  puf='Beş ifadeli sorularda her ifadeyi bağımsız değerlendir; birinin sonucu ötekini etkilemez.')

# ===================================================== 16 · glikoz ve Mg(OH)2 atom denklemi · zor
kartla('16','Atom sayısı eşitlemesi','Birim başına atom sayıları çıkarılır; iki maddedeki istenen atom türü eşitlenerek bilinmeyen birim sayısı bulunur.','Toplam atom sayısını oksijen sayısı sanmak; indisi yalnız bir atoma uygulamak.','zor','düz',4,'esitleme','Atom sayısı eşitleme')
glO=6; glH=12; mgO=2; mgH=2
n_gl=4; Otop=n_gl*glO; per=mgO+mgH; assert Otop==24 and per==4 and Fr(Otop,per)==6
w12b=Fr(Otop,mgO); w8=Fr(Otop,3); w24=Fr(n_gl*(glH+glO+6),per) ; w3=Fr(glH,per)
assert (w12b,w8,w3)==(12,8,3) and w24==24 and n_gl*(6+12+6)==96
s16v=[Fr(6),Fr(12),Fr(8),Fr(24),Fr(3)]; assert len(set(s16v))==5
q('0016',[A('Glikozdaki oksijeni bul','C₆H₁₂O₆ molekülünde 6 oksijen atomu vardır.','1 molekül: 6 O'),
          A('4 molekülü hesapla','Katsayı bütün molekülü çoğaltır.','4 × 6 = 24 O atomu'),
          A('Mg(OH)₂ birimini say','Parantezin dışındaki 2, O ve H’yi çoğaltır; bir birimde 2 O ve 2 H vardır.','2 + 2 = 4 atom (O + H)'),
          A('Birim sayısını bul','İki yandaki atom sayıları eşitlenir.','24 : 4 = 6')],
  tipId='km-kb2-esitleme',tip='Atom sayısı eşitleme',z='zor',alt='Kimyanın Sembolik Dili',kaz='Formül ve katsayılardan atom sayısı eşitliği kurarak bilinmeyen birim sayısını bulur.',kalip='düz',
  kart='K-KMKB2-16 (atom eşitleme) · glikoz oksijeni = Mg(OH)₂ içindeki O + H',
  metin='Bir kimya öğretmeni, sembolik dil çalışmasında öğrencilerden iki maddedeki atom sayılarını karşılaştırmalarını istiyor. Mide ilaçlarında kullanılan magnezyum hidroksit Mg(OH)₂ ile besinlerdeki glikoz C₆H₁₂O₆ karşılaştırılmaktadır.\n4C₆H₁₂O₆ ifadesinde bulunan oksijen atomlarının sayısı, n tane Mg(OH)₂ biriminde bulunan oksijen atomları ile hidrojen atomlarının sayıları toplamına eşittir (magnezyum atomları bu toplama katılmaz).\nBuna göre n kaçtır?',
  dogru=6,yan=[(12,'Mg(OH)₂ içinde yalnız oksijen atomlarını (2 tane) hesaba katmış.','dikkat'),
               (24,'Glikozdaki toplam atom sayısını (96) oksijen sayısı sanıp 4’e bölmüş.','dikkat'),
               (8,'Magnezyum atomunu da sayarak Mg(OH)₂ birimini 3 atom saymış; 24 : 3 = 8.','dikkat'),
               (3,'4 glikoz molekülü yerine tek glikozdaki hidrojen atomu sayısını (12) kullanmış; 12 : 4 = 3.','bilgi')],
  istenen='n değeri.',
  ip=['Her iki yandaki atom türünü ayrı ayrı say.'],
  bilgi=[B('Katsayı ve indis','katsayı tüm molekülü çoğaltır; parantez dışındaki indis parantez içindeki her atomu çoğaltır. Örnek: 2Ba(NO₃)₂ içinde 4 N ve 12 O vardır')],
  puf='Eşitlenen atom türünü (burada O ve H) yazıp iki yandan da yalnız onu say.')
assert 4*(glO)==24 and n_gl*(glO+glH+6)==96 and Fr(96,per)==24
bitir(P,'kimyabilimiiki','kim|Kimya Bilimi')
