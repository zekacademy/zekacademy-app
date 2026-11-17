"""Karışım Problemleri · ŞEKİLLİ ek paket (karisimsekb): 10 soru; şekil/tablo/grafik çözüm verisini taşır; her doğru ve çeldirici değer Python'da hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Karışım Problemleri'
P=Parti('karisimsekb','Karışım Problemleri','prob|Karışım Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli karışım soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def tx(x,y,t,st=''): return f'\\node[{st}] at ({x:.3f},{y:.3f}) {{{t}}};'
def ln(x1,y1,x2,y2,st=''): return f'\\draw[{st}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'

PAYB=B('Dilim ve oran','daire grafiğinde bir dilimin açısı, o maddenin bütündeki payını 360° üzerinden gösterir. Örnek: 90°’lik dilim bütünün 90/360 = 1/4’ünü oluşturur')
ORAN=B('Karışım oranı','oran = maddenin miktarı ÷ karışımın toplam miktarı; iki çözelti karışınca madde miktarları ve toplam miktarlar ayrı ayrı toplanır. Örnek: 100 g %10’luk ile 100 g %30’luk tuzlu su karışınca tuz 10 + 30 = 40 g, oran 40/200 = %20 olur')
BUH=B('Buharlaşma','buharlaşınca yalnız su kaybolur; tuzun kütlesi değişmez ve yeni oran = tuz ÷ kalan toplam kütle. Örnek: 100 g %10’luk tuzlu sudan 50 g su buharlaşırsa tuz 10 g, oran 10/50 = %20 olur')
FIY=B('Ortalama fiyat','karışımın birim fiyatı = toplam maliyet ÷ toplam miktar. Örnek: 100 TL/kg’dan 1 kg ile 200 TL/kg’dan 1 kg karıştırılırsa 300 ÷ 2 = 150 TL/kg olur')
DER=B('Derişim doğrusu','karışımın derişimi, iki çözeltinin derişimi arasındadır; bir çözeltiden alınan hacim, karışımın öteki çözeltiye olan uzaklığıyla orantılıdır. Örnek: 10 ve 30 arasında 20 olan karışım için iki çözeltinin hacimleri eşittir')
EKL=B('Tuz ekleme','eklenen tuz hem tuz miktarını hem toplam kütleyi artırır. Örnek: 100 g %10’luk tuzlu suya 20 g tuz eklenirse tuz 10 + 20 = 30 g, toplam 120 g olur')
SUL=B('Seyreltme','su eklenince madde miktarı değişmez, toplam hacim artar; oran yeniden hesaplanır. Örnek: 200 mL’de 50 mL madde (%25) varsa 200 mL su ekleyince oran 50/400 = %12,5 olur')
KAD=B('Gösterge okuma','alkolmetre gibi göstergeler çözeltideki alkolün hacimce yüzdesini verir; alkol hacmi = yüzde × çözelti hacmi. Örnek: %40 gösteren 200 mL çözeltide 80 mL alkol vardır')

kartla('K-KRC-01','Daire grafiği ve seyreltme','Dilim açısından maddenin payı bulunur; su ekleyince yalnız su ve toplam hacim artar.','Açıyı mililitre sanmak; eklenen suyu toplam hacme katmamak.','orta','grafik',4,'krc-daire','Daire grafiğinde dilim payı ve seyreltme')
kartla('K-KRC-02','Sütun grafiğinden derişim','Grafikten her tankın tuz oranı okunur; seçilen tanklardan tuz miktarı ve toplam kütle ile yeni oran bulunur.','Oranların basit ortalamasını almak; tankları karıştırmak.','orta','grafik',4,'krc-sutun','Sütun grafiğindeki derişimlerle karışım')
kartla('K-KRC-03','Buharlaşma grafiği','Kütle–zaman doğrusundan buharlaşma hızı bulunur; tuz sabit kalacağından istenen oran için gereken kütle ve süre hesaplanır.','Buharlaşan kütleyi süre sanmak; tuzu da azalan sanmak.','zor','grafik',5,'krc-buhar','Kütle–zaman grafiğinde buharlaşma')
kartla('K-KRC-04','Fiyat tablosu','Her türün maliyeti ağırlıkla çarpılıp toplanır; toplam maliyet toplam miktara bölünür.','Fiyatların basit ortalaması; bir türü unutmak.','kolay','tablo',3,'krc-fiyat','Fiyat tablosundan karışım maliyeti')
kartla('K-KRC-05','Derişim doğrusu','Karışımın iki derişime uzaklığından hacim oranı bulunur; toplam hacme paylaştırılır.','Oranı ters kurmak; eşit hacim sanmak.','orta','şekilli',4,'krc-dogru','Derişim doğrusunda hacim oranı')
kartla('K-KRC-06','Önce–sonra kapları','İlk tuz miktarı oran ve kütleden bulunur; kütle artışı eklenen tuzdur; yeni oran hesaplanır.','Eklenen tuzu toplam tuza katmamak; paydayı yanlış seçmek.','kolay','şekilli',3,'krc-sonra','Önce–sonra kaplarında tuz ekleme')
kartla('K-KRC-07','Şerit modelde seyreltme','Şeritteki parça oranından tuz ve su bulunur; eklenen suyla yeni oran denklemle çözülür.','Eklenen suyu parça sayısına katmak; tuzu azalan sanmak.','orta','şekilli',4,'krc-serit','Şerit modelde seyreltme denklemi')
kartla('K-KRC-08','Yığılmış sütun grafiği','Her tankın alkol ve su hacmi sütunun iki parçasından okunur; seçilen tankların alkolü ve toplam hacmi toplanır.','Yüzdelerin ortalamasını almak; alkol hacmini yüzde sanmak.','orta','grafik',4,'krc-yigma','Yığılmış sütun grafiğinde karışım')
kartla('K-KRC-09','Seyreltme eğrisi','Eğriden ilk hacim ve tuz miktarı bulunur; hedef orana göre gereken toplam hacim ve eklenecek su hesaplanır.','Toplam hacmi eklenen su sanmak; ilk hacmi eklenen su sanmak.','zor','grafik',5,'krc-egri','Tuz oranı–eklenen su eğrisi')
kartla('K-KRC-10','Alkolmetre göstergeleri','Göstergelerden iki çözeltinin alkol yüzdesi okunur; hedef yüzdeye göre gereken hacim bulunur.','Hacimleri eşit sanmak; oranı ters kurmak.','orta','şekilli',4,'krc-gosterge','Alkolmetre göstergeleriyle hacim bulma')

# ---------- 01 daire grafiği ----------
ang={'Pigment':90,'Beyaz':150,'Su':120}; assert sum(ang.values())==360
V=480; su=Fr(V*ang['Su'],360); d1=V-2*su; assert su==160 and d1==160
e1=[Fr(V,2)-su,Fr(ang['Su']),V-su,Fr(V,2)]; assert e1==[80,120,320,240] and len({d1,*e1})==5
a0=90; o=[]; cols={'Pigment':'vurgu!40','Beyaz':'white','Su':'black!14'}
for k,v in ang.items():
    a1=a0-v; o.append(f'\\filldraw[fill={cols[k]},line width=1pt] (0,0) -- ({a0}:1.5) arc ({a0}:{a1}:1.5) -- cycle;')
    m=math.radians((a0+a1)/2); o.append(tx(2.15*math.cos(m),1.85*math.sin(m),f'{k}\\\\ {v}$^\\circ$','align=center')); a0=a1
SK=fig('\n'.join(o))
q('0001',tipId='krc-daire',tip='Daire grafiğinde dilim payı ve seyreltme',z='orta',alt='Su Ekleme',kaz='Daire grafiğindeki dilim açısından suyun hacmini bulup hedef su oranı için eklenecek saf su miktarını hesaplar.',kalip='grafik',sekil=SK,
 kart='K-KRC-01 (daire grafiği) · 90°, 150°, 120° dilimleri; 480 mL',
 metin='Bir boya atölyesinde hazırlanan 480 mL’lik karışımın bileşenleri hacimce yukarıdaki daire grafiğinde gösterilmiştir. Bu karışımın üzerine bir miktar saf su eklenerek suyun hacimce oranı tam %50 yapılacaktır; eklenen su ile diğer bileşenler arasında bir tepkime olmamaktadır.\nBuna göre karışıma kaç mL saf su eklenmelidir?',
 dogru=int(d1),yan=[(80,'Eklenecek suyu, toplamın yarısı ile ilk su arasındaki farkla (240 − 160) bulmuş; eklenen suyun toplamı da büyüttüğünü unutmuş.','dikkat'),(120,'Dilimin açısını (120°) hacim sanmış.','dikkat'),(240,'Toplamın yarısını (480 ÷ 2) eklenecek su sanmış.','dikkat'),(320,'Suyun dışındaki bileşenlerin hacmini (320 mL) eklenecek su sanmış.','dikkat')],
 istenen='Eklenecek saf su miktarı (mL).',
 ip=['Suyun diliminin açısından ilk hacmini bul; eklenen suyun toplam hacmi de büyüttüğünü yaz.'],
 bilgi=[PAYB],
 ad=[A('Suyun payı','Suyun açısı 120°’dir.','120/360 = 1/3'),A('İlk su','480 mL’nin 1/3’ü sudur.','480 ÷ 3 = 160 mL'),A('Denklemi kur','x mL su eklenince suyun oranı 1/2 olur.','(160 + x) / (480 + x) = 1/2'),A('Çöz','Düzenlenince x bulunur.','320 + 2x = 480 + x → x = 160')],
 puf='Su ekleyince hem suyun hem toplam hacmin x kadar arttığını denkleme yaz.')

# ---------- 02 sütun grafiği ----------
T2={'A':10,'B':25,'C':30}
c_=400; a_=600; tuz=Fr(c_*T2['C']+a_*T2['A'],100); d2=tuz*100/(c_+a_); assert (tuz,d2)==(180,18)
e2=[Fr(T2['A']+T2['C'],2),Fr(c_*T2['A']+a_*T2['C'],c_+a_),T2['A']+T2['C'],Fr(c_*T2['C']+a_*T2['B'],c_+a_)]
assert e2==[20,22,40,27] and len({d2,*e2})==5
sx=1.0;sy=.06;o=[]
for t in range(0,51,10): o.append(ln(0,t*sy,3*sx+.3,t*sy,'black!15,line width=.4pt')); o.append(tx(-.3,t*sy,f'\\footnotesize {t}'))
o+=[ln(0,0,0,52*sy,'line width=1pt'),ln(0,0,3*sx+.3,0,'line width=1.2pt'),tx(.3,52*sy+.3,'\\footnotesize Tuz oranı (\\%)')]
for i,(k,v) in enumerate(T2.items()):
    x=.3+i*sx; o.append(f'\\fill[vurgu!45] ({x:.3f},0) rectangle ({x+.55:.3f},{v*sy:.3f});'); o.append(tx(x+.27,-.3,f'\\footnotesize {k}'))
SK=fig('\n'.join(o))
q('0002',tipId='krc-sutun',tip='Sütun grafiğindeki derişimlerle karışım',z='orta',alt='İki Karışımı Karıştırma',kaz='Sütun grafiğinden iki tankın kütlece tuz oranını okuyup verilen kütlelerle karıştırınca oluşan oranı hesaplar.',kalip='grafik',sekil=SK,
 kart='K-KRC-02 (sütun grafiği) · C 400 g (%30) + A 600 g (%10)',
 metin='Bir tuz fabrikasında A, B ve C tanklarındaki tuzlu suların kütlece tuz oranları yukarıdaki grafikte gösterilmiştir. Bir mühendis, C tankından 400 gram ve A tankından 600 gram tuzlu su alıp boş bir kapta iyice karıştırmıştır; karışırken kütle kaybı olmamıştır.\nBuna göre oluşan karışımın kütlece tuz oranı yüzde kaçtır?',
 dogru=int(d2),yan=[(20,'İki oranın aritmetik ortalamasını almış: (10 + 30) ÷ 2 = 20.','dikkat'),(22,'Kütleleri ters eşleştirmiş: 400 g’ı %10’luk, 600 g’ı %30’luk sanmış: (40 + 180) ÷ 1000 = %22.','dikkat'),(27,'A tankı yerine B tankını almış: (120 + 150) ÷ 1000 = %27.','dikkat'),(40,'İki oranı toplamış: 10 + 30 = 40.','islem')],
 istenen='Karışımın kütlece tuz yüzdesi.',
 ip=['Grafikten her tankın tuz oranını oku; her tanktan alınan tuz kütlesini bul.'],
 bilgi=[ORAN],
 ad=[A('Oranları oku','C’nin %30, A’nın %10 olduğu okunur.','C: %30; A: %10'),A('Tuz kütleleri','Alınan kütleler oranlarla çarpılır.','400 × 0,30 = 120 g; 600 × 0,10 = 60 g'),A('Toplamlar','Tuz kütleleri ve toplam kütle toplanır.','tuz: 180 g; karışım: 1000 g'),A('Oran','Tuz kütlesi toplam kütleye bölünür.','180 ÷ 1000 = %18')],
 puf='Karışımda yüzdelerin değil, madde miktarlarının (kütle × oran) toplamını al; toplam kütleye böl.')

# ---------- 03 buharlaşma grafiği ----------
M0,M1,t1=800,600,5; hz=Fr(M0-M1,t1); assert hz==40
tuz3=M0*Fr(12,100); kal=tuz3*100/20; d3=(M0-kal)/hz; assert (tuz3,kal,d3)==(96,480,8)
e3=[M0-kal,kal/hz,Fr(t1),M0/hz]; assert e3==[320,12,5,20] and len({d3,*e3})==5
sx=.4; sy=.0042; o=[]
for t in range(0,13,2): o.append(ln(t*sx,0,t*sx,800*sy,'black!12,line width=.4pt')); o.append(tx(t*sx,-.3,f'\\footnotesize {t}'))
for v in range(0,801,100): o.append(ln(0,v*sy,12*sx,v*sy,'black!12,line width=.4pt')); o.append(tx(-.4,v*sy,f'\\footnotesize {v}'))
o+=[ln(0,0,12*sx,0,'line width=1.2pt'),ln(0,0,0,800*sy,'line width=1.2pt'),tx(12*sx+.5,0,'\\footnotesize saat'),tx(.5,800*sy+.3,'\\footnotesize Kütle (g)'),
 f'\\draw[line width=1.8pt] (0,{800*sy}) -- ({5*sx},{600*sy});',f'\\fill (0,{800*sy}) circle (.07); \\fill ({5*sx},{600*sy}) circle (.07);']
SK=fig('\n'.join(o))
q('0003',tipId='krc-buhar',tip='Kütle–zaman grafiğinde buharlaşma',z='zor',alt='Buharlaşma',kaz='Kütle–zaman grafiğinden buharlaşma hızını bulup istenen tuz oranına ulaşma süresini hesaplar.',kalip='grafik',sekil=SK,
 kart='K-KRC-03 (buharlaşma grafiği) · 800 g, %12 tuz; oran %20 olunca',
 metin='Kütlece %12’si tuz olan tuzlu su bir kapta ısıtılmakta ve yalnız su buharlaşmaktadır. Kaptaki karışımın kütlesinin zamanla değişimi grafikte ilk 5 saat için gösterilmiştir; buharlaşma hızı sabittir ve işlem aynı hızla sürdürülmüştür.\nBuna göre karışımın kütlece tuz oranı %20 olduğunda ısıtma işleminin başlamasından kaç saat geçmiştir?',
 dogru=int(d3),yan=[(5,'Grafikte son görünen zamanı (5 saat) cevap sanmış.','dikkat'),(12,'Kalan kütleyi (480 g) buharlaşma hızına bölmüş: 480 ÷ 40 = 12.','dikkat'),(20,'Tüm kütleyi hıza bölmüş: 800 ÷ 40 = 20.','dikkat'),(320,'Buharlaşan su kütlesini (320 g) süre sanmış.','dikkat')],
 istenen='Tuz oranı %20 olana kadar geçen süre (saat).',
 ip=['Tuzun kütlesi değişmez; tuz oranı %20 olduğunda karışımın toplam kütlesinin ne olduğunu bul.'],
 bilgi=[BUH],
 ad=[A('Hızı bul','Grafikte 5 saatte kütle 800’den 600’e iner.','200 ÷ 5 = 40 g/saat'),A('Tuz kütlesi','Tuz buharlaşmaz.','800 × 0,12 = 96 g'),A('Hedef kütle','Tuz bu kütlenin %20’si olacaktır.','96 ÷ 0,20 = 480 g'),A('Buharlaşan su','Başlangıç kütlesinden hedef kütle çıkarılır.','800 − 480 = 320 g'),A('Süre','Buharlaşan su hıza bölünür.','320 ÷ 40 = 8 saat')],
 puf='Buharlaşmada tuz sabit kalır; hedef oranın toplam kütlesini bul, kütle kaybını hıza böl.')

# ---------- 04 fiyat tablosu ----------
Ty=[('Siyah çay',180,6),('Yeşil çay',120,9),('Beyaz çay',240,5)]
mal=sum(f*k for _,f,k in Ty); kg=sum(k for *_,k in Ty); d4=Fr(mal,kg); assert (mal,kg,d4)==(3360,20,168)
e4=[Fr(180+120+240,3),Fr(180*5+120*9+240*6,20),Fr(240),mal]
assert e4==[180,171,240,3360] and len({d4,*e4})==5
SK=tablo_svg(['Çay türü','Fiyat (TL/kg)','Karışımdaki miktar (kg)'],[[n,str(f),str(k)] for n,f,k in Ty])
q('0004',tipId='krc-fiyat',tip='Fiyat tablosundan karışım maliyeti',z='kolay',alt='Fiyat Karışımı',kaz='Tablodaki fiyat ve miktarlardan karışımın kilogram maliyetini hesaplar.',kalip='tablo',sekil=SK,
 kart='K-KRC-04 (fiyat tablosu) · 168 TL/kg',
 metin='Bir çay satıcısı, üç farklı çayı kilogram fiyatları ve karışıma kattığı miktarlarla yukarıdaki tabloda gösterildiği gibi karıştırarak yeni bir harman hazırlamıştır. Harmanın hazırlanmasında yalnız bu üç çay kullanılmıştır.\nBuna göre bu harmanın kilogram maliyeti kaç TL’dir?',
 dogru=int(d4),yan=[(180,'Fiyatların basit ortalamasını almış: (180 + 120 + 240) ÷ 3 = 180.','dikkat'),(171,'Miktarları fiyatlarla yanlış eşleştirmiş: (900 + 1080 + 1440) ÷ 20 = 171.','dikkat'),(240,'Tablodaki en yüksek kilogram fiyatını yazmış.','dikkat'),(3360,'Toplam maliyeti, toplam kütleye bölmeden yazmış.','dikkat')],
 istenen='Harmanın kilogram maliyeti (TL).',
 ip=['Her çay için fiyatı miktarıyla çarp; toplam maliyeti toplam miktarla karşılaştır.'],
 bilgi=[FIY],
 ad=[A('Maliyetler','Her türün fiyatı kendi miktarıyla çarpılır.','180 × 6 = 1080 · 120 × 9 = 1080 · 240 × 5 = 1200'),A('Toplamlar','Maliyetler ve miktarlar ayrı ayrı toplanır.','3360 TL · 20 kg'),A('Birim maliyet','Toplam maliyet toplam miktara bölünür.','3360 ÷ 20 = 168')],
 puf='Fiyatların basit ortalaması değil, miktarlarla ağırlıklandırılmış ortalaması alınır.')

# ---------- 05 derişim doğrusu ----------
a5,b5,m5,V5=10,40,34,600
x40=Fr(V5*(m5-a5),b5-a5); d5=x40; assert d5==480
e5=[Fr(V5*(b5-m5),b5-a5),Fr(V5*m5,100),Fr(V5,2),Fr(V5*2,3)]; assert e5==[120,204,300,400] and len({d5,*e5})==5
sc=.13; o=[ln(0,0,50*sc,0,'line width=1.2pt,-{Stealth[length=2mm]}')]
for t in range(0,50,10): o.append(ln(t*sc,-.1,t*sc,.1)); o.append(tx(t*sc,-.4,f'\\footnotesize {t}'))
for v,n in [(a5,'X'),(m5,'M'),(b5,'Y')]:
    o.append(f'\\fill ({v*sc:.3f},0) circle (.08);'); o.append(tx(v*sc,.45,f'\\textbf{{{n}}}'))
o.append(tx(m5*sc,-.85,'\\footnotesize\\bfseries 34'))
o.append(tx(50*sc+.5,0,'\\footnotesize \\%'))
SK=fig('\n'.join(o))
q('0005',tipId='krc-dogru',tip='Derişim doğrusunda hacim oranı',z='orta',alt='İki Karışımı Karıştırma',kaz='Derişim doğrusunda karışımın iki çözeltiye uzaklığından hacim oranını bulup toplam hacme paylaştırır.',kalip='şekilli',sekil=SK,
 kart='K-KRC-05 (derişim doğrusu) · X %10, Y %40, karışım %34; 600 mL',
 metin='Bir laboratuvarda hacimce alkol oranı X çözeltisinde, Y çözeltisinde ve bu iki çözeltinin karıştırılmasıyla elde edilen M çözeltisinde sırasıyla yukarıdaki doğru üzerinde gösterilen yüzdelerdedir (doğru ölçeklidir). M çözeltisinden 600 mL hazırlanırken yalnız X ve Y çözeltileri kullanılmış, kütle ve hacim kaybı olmamıştır.\nBuna göre bu hazırlıkta kaç mL Y çözeltisi kullanılmıştır?',
 dogru=int(d5),yan=[(120,'Oranı ters kurmuş: Y’nin payını X’inkiyle karıştırmış, 600 × 6/30 = 120.','dikkat'),(204,'M’nin yüzdesini (%34) 600 ile çarpmış: 600 × 0,34 = 204; bu alkol miktarını Y hacmi sanmış.','dikkat'),(300,'Hacimlerin eşit olduğunu sanmış: 600 ÷ 2.','dikkat'),(400,'Hacim oranını 2 : 1 sanıp 600’ün 2/3’ünü almış.','dikkat')],
 istenen='Kullanılan Y çözeltisi hacmi (mL).',
 ip=['X ve Y’deki alkol miktarlarının toplamının, M’deki alkol miktarına eşit olduğunu kullanarak iki hacim arasındaki ilişkiyi bul.'],
 bilgi=[DER],
 ad=[A('Derişimleri oku','Doğruda X = 10, M = 34 ve Y = 40’tır.','10, 34, 40'),A('Alkolü yaz','x mL X ve y mL Y için alkol, M’deki alkole eşittir.','0,10x + 0,40y = 0,34 · (x + y)'),A('Oranı bul','Düzenlenince hacimler arasındaki ilişki çıkar.','0,06y = 0,24x → y = 4x'),A('Paylaştır','Toplam 600 mL’de Y’nin payı 4/5’tir.','600 × 4/5 = 480 mL')],
 puf='Alkolün toplamı, karışımdaki alkole eşit olmalıdır; iki derişim arasındaki farklar hacim oranını verir.')

# ---------- 06 önce–sonra kapları ----------
m_on,o_on,m_sn=400,5,500
t0=Fr(m_on*o_on,100); eklenen=m_sn-m_on; d6=(t0+eklenen)*100/m_sn; assert (t0,eklenen,d6)==(20,100,24)
e6=[t0*100/m_sn,Fr(eklenen*100,m_sn),Fr(o_on),(t0+eklenen)*100/m_on]; assert e6==[4,20,5,30] and len({d6,*e6})==5
def beher(x,ad,kg,ora):
    ls=[f'\\draw[line width=1.2pt] ({x},2.2) -- ({x},0) -- ({x+1.6},0) -- ({x+1.6},2.2);',f'\\fill[vurgu!18] ({x+.03},.03) rectangle ({x+1.57},{kg/400*1.4:.3f});',
        ln(x,kg/400*1.4,x+1.6,kg/400*1.4,'line width=.8pt'),tx(x+.8,-.4,f'\\textbf{{{ad}}}'),tx(x+.8,-.85,f'\\footnotesize {kg} g')]
    if ora: ls.append(tx(x+.8,-1.25,f'\\footnotesize tuz oranı {ora}'))
    return ls
SK=fig('\n'.join(beher(0,'Önce',400,'\\%5')+beher(3.4,'Sonra',500,'')+[ln(1.9,1.0,3.2,1.0,'-{Stealth[length=2mm]}'),tx(2.55,1.35,'\\footnotesize tuz eklendi')]))
q('0006',tipId='krc-sonra',tip='Önce–sonra kaplarında tuz ekleme',z='kolay',alt='Madde Ekleme',kaz='Önce ve sonra kaplarında yazan kütlelerden eklenen tuzu bulup yeni tuz oranını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KRC-06 (önce–sonra kapları) · 400 g %5 → 500 g',
 metin='Bir tuzlu su kabına tuz eklenmiş ve eklenen tuzun tamamı çözünmüştür. Kabın tuz eklenmeden önceki ve eklendikten sonraki durumları, kütleleri ve ilk tuz oranıyla yukarıda gösterilmiştir. Kaba tuz dışında başka bir şey eklenmemiştir ve hiçbir madde kaptan çıkarılmamıştır.\nBuna göre eklendikten sonraki karışımın kütlece tuz oranı yüzde kaçtır?',
 dogru=int(d6),yan=[(4,'Eklenen tuzu hesaba katmamış: 20 ÷ 500 = %4.','dikkat'),(20,'Yalnız eklenen tuzu (100 g) toplam kütleye oranlamış: 100 ÷ 500 = %20.','dikkat'),(5,'İlk tuz oranını (%5) yeni oran sanmış.','dikkat'),(30,'Yeni tuz miktarını ilk kütleye bölmüş: 120 ÷ 400 = %30.','dikkat')],
 istenen='Yeni karışımın kütlece tuz yüzdesi.',
 ip=['Kütle artışının neden kaynaklandığını düşün; ilk tuz miktarını bul ve yeni tuz miktarını toplam kütleyle karşılaştır.'],
 bilgi=[EKL],
 ad=[A('İlk tuz','400 g’ın %10’u tuzdur.','400 × 0,05 = 20 g'),A('Eklenen tuz','Kütle artışı eklenen tuzdur.','500 − 400 = 100 g'),A('Oran','Yeni tuz miktarı toplam kütleye bölünür.','(20 + 100) ÷ 500 = %24')],
 puf='Tuz eklenince hem tuz miktarı hem toplam kütle artar; kütle farkı eklenen tuzdur.')

# ---------- 07 şerit model ----------
ts,sw,su_ek,oran=2,3,90,Fr(1,4)
k7=Fr(su_ek*oran,ts-5*oran)*0+Fr(su_ek*oran,ts-oran*5)  # 2k=(5k+90)/4
k7=Fr(su_ek,8-5); d7=5*k7; assert k7==30 and d7==150 and 2*k7*4==5*k7+su_ek
e7=[k7,2*k7,5*k7+su_ek,5*su_ek]; assert e7==[30,60,240,450] and len({d7,*e7})==5
o=[tx(-.9,.45,'Tuz'),tx(-.9,-.15,'Su')]
for i in range(2): o.append(f'\\draw[fill=vurgu!35] ({i*.8},.15) rectangle ({i*.8+.8},.75);')
for i in range(3): o.append(f'\\draw[fill=white] ({i*.8},-.45) rectangle ({i*.8+.8},.15);')
SK=fig('\n'.join(o))
q('0007',tipId='krc-serit',tip='Şerit modelde seyreltme denklemi',z='orta',alt='Su Ekleme',kaz='Şerit modeldeki parça oranından tuz ve su miktarını yazıp eklenen suyla oluşan oranı denklemle çözer.',kalip='şekilli',sekil=SK,
 kart='K-KRC-07 (şerit model) · tuz:su = 2:3, 90 g su, %25',
 metin='Bir aşçı, tuz ve sudan oluşan bir salamurayı kütlece şekildeki parça oranlarıyla hazırlamıştır; her bir kutu aynı kütleyi göstermektedir. Aşçı salamuranın tadını yumuşatmak için içine 90 gram saf su eklemiştir ve karışımın kütlece tuz oranı tam %25 olmuştur.\nBuna göre aşçının ilk hazırladığı salamuranın kütlesi kaç gramdır?',
 dogru=int(d7),yan=[(30,'Bir kutunun kütlesini (k = 30) cevap sanmış.','dikkat'),(60,'Yalnız tuzun kütlesini (2k = 60) yazmış.','dikkat'),(240,'Eklenen sudan sonraki toplam kütleyi (150 + 90) yazmış.','dikkat'),(450,'Eklenen suyu parça sayısıyla (5) çarpmış: 90 × 5.','dikkat')],
 istenen='İlk salamuranın kütlesi (g).',
 ip=['Bir kutunun kütlesine k deyip tuzun ve toplam kütlenin k cinsinden yeni değerlerini yaz.'],
 bilgi=[SUL],
 ad=[A('Parçaları yaz','Şeritte tuz 2 kutu, su 3 kutudur.','tuz = 2k · su = 3k · toplam = 5k'),A('Denklemi kur','Su eklenince toplam 5k + 90 olur, tuz 2k kalır; oran 1/4’tür.','2k / (5k + 90) = 1/4'),A('Çöz','İçler dışlar çarpımı yapılır.','8k = 5k + 90 → k = 30'),A('İlk kütle','Toplam 5 kutudur.','5 × 30 = 150 g')],
 puf='Parça oranlarını bir ortak k ile yaz; eklenen maddeyi yalnız toplam kütleye ekle.')

# ---------- 08 yığılmış sütun ----------
TK={'A':(15,25),'B':(30,50),'C':(45,15)}
alk=TK['A'][0]+TK['C'][0]; tot=sum(TK['A'])+sum(TK['C']); d8=Fr(alk*100,tot); assert d8==60
e8=[Fr(TK['A'][0]*100,sum(TK['A'])),Fr(sum(TK[k][0] for k in 'ABC')*100,sum(sum(TK[k]) for k in 'ABC')),Fr(TK['C'][0]),Fr(Fr(TK['A'][0]*100,sum(TK['A']))+Fr(TK['C'][0]*100,sum(TK['C'])),2)]
assert e8==[Fr('37.5'),50,45,Fr('56.25')] and len({d8,*e8})==5
sx=1.1;sy=.036;o=[]
for t in range(0,101,5): o.append(ln(0,t*sy,3*sx+.3,t*sy,'black!15,line width=.4pt'))
for t in range(0,101,10): o.append(tx(-.35,t*sy,f'\\footnotesize {t}'))
o+=[ln(0,0,0,104*sy,'line width=1pt'),ln(0,0,3*sx+.3,0,'line width=1.2pt'),tx(.5,104*sy+.3,'\\footnotesize Hacim (L)')]
for i,(k,(al,sv)) in enumerate(TK.items()):
    x=.3+i*sx; o.append(f'\\fill[vurgu!45] ({x:.3f},0) rectangle ({x+.6:.3f},{al*sy:.3f});'); o.append(f'\\draw[fill=white] ({x:.3f},{al*sy:.3f}) rectangle ({x+.6:.3f},{(al+sv)*sy:.3f});'); o.append(tx(x+.3,-.3,f'\\footnotesize {k} tankı'))
o.append(f'\\fill[vurgu!45] ({3*sx+.5:.3f},{90*sy:.3f}) rectangle ({3*sx+.75:.3f},{96*sy:.3f}); '+tx(3*sx+1.45,93*sy,'\\footnotesize alkol')+f'\\draw ({3*sx+.5:.3f},{80*sy:.3f}) rectangle ({3*sx+.75:.3f},{86*sy:.3f}); '+tx(3*sx+1.3,83*sy,'\\footnotesize su'))
SK=fig('\n'.join(o))
q('0008',tipId='krc-yigma',tip='Yığılmış sütun grafiğinde karışım',z='orta',alt='İki Karışımı Karıştırma',kaz='Yığılmış sütun grafiğinden iki tankın alkol ve su hacmini okuyup karışımın hacimce alkol oranını hesaplar.',kalip='grafik',sekil=SK,
 kart='K-KRC-08 (yığılmış sütun) · A (15 + 25) ile C (45 + 15)',
 metin='Bir eczanede A, B ve C tanklarındaki alkol–su çözeltilerinin hacimleri, alkol ve su kısımları ayrı gösterilerek yukarıdaki grafikte verilmiştir. Eczacı, A ve C tanklarındaki çözeltinin tamamını büyük bir kaba boşaltıp karıştırmıştır; karışırken hacim kaybı olmamıştır.\nBuna göre karışımın hacimce alkol oranı yüzde kaçtır?',
 dogru=int(d8),yan=[(Fr('37.5'),'Yalnız A tankının alkol yüzdesini yazmış: 15 ÷ 40 = %37,5.','dikkat'),(50,'Üç tankın tümünü karıştırmış: 90 ÷ 180 = %50.','dikkat'),(45,'C tankının alkol hacmini (45 L) yüzde sanmış.','dikkat'),(Fr('56.25'),'İki tankın yüzdelerinin aritmetik ortalamasını almış: (37,5 + 75) ÷ 2 = 56,25.','dikkat')],
 istenen='Karışımın hacimce alkol yüzdesi.',
 ip=['Her sütunda alkol ve su kısımlarını ayrı oku; alkolleri ve toplam hacimleri ayrı topla.'],
 bilgi=[ORAN],
 ad=[A('A ve C’yi oku','A: 15 L alkol, 25 L su; C: 45 L alkol, 15 L su.','A toplam 40 L; C toplam 60 L'),A('Alkolü topla','İki tankın alkolü toplanır.','15 + 45 = 60 L'),A('Toplam hacim','İki tankın hacimleri toplanır.','40 + 60 = 100 L'),A('Oran','Alkol toplam hacme bölünür.','60 ÷ 100 = %60')],
 puf='Yığılmış sütunda alt ve üst parçaları ayrı oku; alkolleri topla, toplam hacme böl.')

# ---------- 09 seyreltme eğrisi ----------
V9,c0=300,24; tz9=Fr(V9*c0,100); assert tz9==72
def oran9(x): return tz9*100/(V9+x)
assert [oran9(x) for x in (0,100,200,300,450)]==[24,18,Fr('14.4'),12,Fr('9.6')]
hedef=8; d9=tz9*100/hedef-V9; assert d9==600
e9=[Fr(450),Fr(V9),Fr(tz9*100/hedef),Fr(200)]; e9=[Fr(450),Fr(V9),tz9*100/hedef,Fr(200)]
e9=[Fr(100),Fr(V9),Fr(450),tz9*100/hedef]; assert e9==[100,300,450,900] and len({d9,*e9})==5
sx=.0095; sy=.12; o=[]
for t in range(0,501,100): o.append(ln(t*sx,0,t*sx,28*sy,'black!12,line width=.4pt')); o.append(tx(t*sx,-.3,f'\\footnotesize {t}'))
for v in range(0,29,4): o.append(ln(0,v*sy,500*sx,v*sy,'black!12,line width=.4pt')); o.append(tx(-.35,v*sy,f'\\footnotesize {v}'))
pts=' '.join(f'({x*sx:.3f},{float(oran9(x))*sy:.3f})' for x in range(0,451,50))
o+=[ln(0,0,500*sx,0,'line width=1.2pt'),ln(0,0,0,28*sy,'line width=1.2pt'),tx(500*sx+.6,0,'\\footnotesize mL'),tx(.7,28*sy+.3,'\\footnotesize Tuz oranı (\\%)'),f'\\draw[line width=1.8pt] plot[smooth] coordinates {{{pts}}};',f'\\draw[dashed] ({100*sx:.3f},0) -- ({100*sx:.3f},{18*sy:.3f}) -- (0,{18*sy:.3f}); \\fill ({100*sx:.3f},{18*sy:.3f}) circle (.07);',tx(-.4,18*sy+.0,'\\footnotesize\\bfseries 18','left=0pt')]
SK=fig('\n'.join(o))
q('0009',tipId='krc-egri',tip='Tuz oranı–eklenen su eğrisi',z='zor',alt='Su Ekleme',kaz='Seyreltme eğrisinden ilk hacmi ve tuz miktarını bulup hedef oran için eklenecek su miktarını hesaplar.',kalip='grafik',sekil=SK,
 kart='K-KRC-09 (seyreltme eğrisi) · 300 mL %24; hedef %8',
 metin='Kütlesi bilinmeyen bir miktar tuzlu suya kademeli olarak saf su eklenmiş ve kaptaki karışımın tuz oranı, eklenen su miktarına göre yukarıdaki grafikte gösterilmiştir. Suyun tuz dışında bir şeyle tepkimeye girmediği ve her 1 mL suyun 1 gram olduğu kabul edilmektedir.\nBuna göre tuz oranını %8’e düşürmek için başlangıçtaki tuzlu suya toplam kaç mL saf su eklenmelidir?',
 dogru=int(d9),yan=[(100,'Grafikte işaretli noktanın eklenen su değerini (100 mL) cevap sanmış.','dikkat'),(300,'Başlangıçtaki tuzlu suyun kütlesini (300 g) eklenecek su sanmış.','dikkat'),(450,'Grafikte görünen son eklenme miktarını (450 mL) cevap sanmış.','dikkat'),(900,'Toplam kütleyi (900 g) eklenecek su sanmış, ilk kütleyi çıkarmamış.','dikkat')],
 istenen='Eklenecek toplam saf su miktarı (mL).',
 ip=['Grafiğin başlangıç noktası ve bir sonraki okunabilir noktasından tuzun kütlesinin değişmediğini kullanarak ilk kütleyi bul.'],
 bilgi=[SUL],
 ad=[A('İlk kütleyi bul','x = 0’da oran %24, x = 100’de %18’dir; tuz miktarı sabittir.','0,24 · K = 0,18 · (K + 100) → K = 300 g'),A('Tuz kütlesi','İlk kütlenin %24’ü tuzdur.','300 × 0,24 = 72 g'),A('Hedef kütle','72 g, toplamın %8’i olmalıdır.','72 ÷ 0,08 = 900 g'),A('Eklenen su','Toplamdan ilk kütle çıkarılır.','900 − 300 = 600 mL')],
 puf='Su eklenince tuzun kütlesi sabittir; hedef oran için gereken toplam kütleyi bulup ilk kütleyi çıkar.')

# ---------- 10 alkolmetre ----------
aa,bb,tt,VA=70,20,60,200
d10=Fr(VA*(aa-tt),tt-bb); assert d10==50
e10=[Fr(VA*(tt-bb),aa-bb),Fr(VA),Fr(VA*(tt-bb),aa-tt),Fr(VA*(aa-tt),aa-bb)]
assert e10==[160,200,800,40] and len({d10,*e10})==5
def kadran(cx,p,ad_):
    ls=[f'\\draw[line width=1.2pt] ({cx+1.5},0) arc (0:180:1.5) -- cycle;']
    for k in range(0,101,10):
        a=math.radians(180-1.8*k); c,s=math.cos(a),math.sin(a)
        ls.append(ln(cx+1.5*c,1.5*s,cx+1.3*c,1.3*s,'line width=.8pt')); ls.append(tx(cx+1.12*c,1.12*s,f'\\tiny {k}'))
    a=math.radians(180-1.8*p); ls.append(ln(cx,0,cx+.95*math.cos(a),.95*math.sin(a),'line width=2pt,vurgu')); ls.append('\\fill (%.2f,0) circle (.06);'%cx)
    ls.append(tx(cx,-.4,f'\\textbf{{{ad_}}}')); return ls
SK=fig('\n'.join(kadran(0,aa,'A kabı')+kadran(4.0,bb,'B kabı')))
q('0010',tipId='krc-gosterge',tip='Alkolmetre göstergeleriyle hacim bulma',z='orta',alt='İki Karışımı Karıştırma',kaz='İki göstergeden alkol yüzdelerini okuyup hedef yüzdeye ulaşmak için gereken hacmi hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KRC-10 (alkolmetre) · A %70 (200 mL), B %20, hedef %60',
 metin='Bir parfüm atölyesinde A ve B kaplarındaki alkol–su çözeltilerinin hacimce alkol yüzdesi, alkolmetre göstergeleriyle yukarıdaki gibi okunmuştur. A kabında 200 mL çözelti bulunmaktadır. Usta, A kabındaki çözeltinin tamamına B kabından bir miktar çözelti ekleyerek hacimce %60 alkollü bir karışım elde etmiştir; karışırken hacim kaybı olmamıştır.\nBuna göre B kabından kaç mL çözelti eklenmiştir?',
 dogru=int(d10),yan=[(40,'Hedefe olan farkı (10) iki çözeltinin farkına (50) bölmüş: 200 × 10 ÷ 50 = 40.','dikkat'),(160,'Hedefin B’ye farkını (40) iki çözeltinin farkına (50) bölmüş: 200 × 40 ÷ 50 = 160.','dikkat'),(200,'İki kaptan eşit hacimde karıştığını sanmış.','dikkat'),(800,'Oranı ters kurmuş: 200 × 40 ÷ 10 = 800.','dikkat')],
 istenen='B kabından eklenen çözelti hacmi (mL).',
 ip=['Göstergelerden iki alkol yüzdesini oku; eklenen B hacmine x deyip karışımdaki alkol hacmini yaz.'],
 bilgi=[KAD],
 ad=[A('Göstergeleri oku','A %70, B %20 göstermektedir.','A: 200 mL · %70'),A('Denklemi kur','Alkol miktarları toplanıp %60’a eşitlenir.','0,70 · 200 + 0,20 · x = 0,60 · (200 + x)'),A('Çöz','Düzenlenince x bulunur.','140 + 0,2x = 120 + 0,6x → x = 50')],
 puf='Karışımdaki alkol = A’nın alkolü + B’nin alkolü; hedef yüzdeyi toplam hacimle çarp ve denklem kur.')

bitir(P,'karisimsekb','prob|Karışım Problemleri')
