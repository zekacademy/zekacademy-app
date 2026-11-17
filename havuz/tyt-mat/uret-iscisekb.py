"""İşçi Emek Problemleri · ŞEKİLLİ ek paket (iscisekb): 10 soru; şekil/tablo/grafik çözüm verisini taşır; her doğru ve çeldirici değer Python'da hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='İşçi Emek Problemleri'
P=Parti('iscisekb','İşçi Emek Problemleri','prob|İşçi Emek Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli işçi-havuz soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def tx(x,y,t,st=''): return f'\\node[{st}] at ({x:.3f},{y:.3f}) {{{t}}};'
def ln(x1,y1,x2,y2,st=''): return f'\\draw[{st}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'

PAY=B('İşin kesri','bir işin tamamı 1 kabul edilir; aynı sürede çalışanlardan her birinin yaptığı kesir, onun hızıyla doğru orantılıdır. Örnek: aynı sürede işin 1/2’sini ve 1/4’ünü yapan iki işçiden birincinin hızı ikincinin 2 katıdır')
ILK=B('Hız ve süre','sabit hızla çalışan biri bir işi t günde bitiriyorsa günde işin 1/t’sini yapar; birlikte çalışanların hızları toplanır. Örnek: 6 günde bitiren ve 3 günde bitiren iki kişi birlikte günde 1/6 + 1/3 = 1/2 iş yapar')
SEV=B('Doldurma','bir havuz bir musluk tarafından t saatte doluyorsa saatte havuzun 1/t’si dolar; iki musluk birlikte açıksa saatlik dolum miktarları toplanır. Örnek: 4 saatte dolduran musluk 1 saatte havuzun 1/4’ünü doldurur')
GRF=B('Grafikten hız','doğru grafiğinde eğim hızı verir: değişim miktarı ÷ geçen süre. Örnek: 2 saatte 30 birim artan doğru için hız 15 birim/saattir')
TAK=B('İş günü','yalnız çalışılan günler sayılır; hafta sonu ve resmî tatiller çalışma gün sayısına katılmaz. Örnek: Cuma günü başlayıp 3 iş günü çalışan biri, hafta sonunu atlayıp Salı günü bitirir')
GUN=B('İşçi-gün','sabit verimli işçilerde iş = işçi sayısı × gün sayısı (işçi-gün) ile ölçülür. Örnek: 3 işçinin 4 günde yaptığı iş 12 işçi-gündür')
KAD=B('Göstergeden hız','sabit hızla çalışan bir makinenin göstergede belli sürede okunan yüzdesinden bütün işin süresi bulunur. Örnek: 2 saatte %50 gösteren makine tüm işi 4 saatte bitirir')
UCR=B('Emeğe göre paylaşım','ortak çalışmada ücret, her kişinin işin kaçta kaçını yaptığına göre paylaşılır. Örnek: işin 1/4’ünü yapan kişi toplam ücretin 1/4’ünü alır')

kartla('K-ISC-01','Daire grafiğinde iş payları','Aynı sürede yapılan iş kesirleri hızları verir; kalan iş ve yeni ekibin hızı bulunur.','Kalan işi tüm iş sanmak; ayrılan işçiyi saymak.','orta','grafik',4,'isc-daire','Daire grafiğinden iş payı ve kalan süre')
kartla('K-ISC-02','Günlük üretim sütun grafiği','Grafikten yapılan toplam iş bulunur; ekip küçülünce günlük hız değişir ve kalan iş yeni hızla bölünür.','Ayrılmayı unutmak; kalan işi eski hızla bölmek; gün sayısını saymayı unutmak.','orta','grafik',3,'isc-sutun','Günlük üretim sütun grafiği')
kartla('K-ISC-03','Izgarada boyama','Boyalı birim sayısından hız bulunur; birlikte çalışmada hızlar toplanır.','Eski boyanmış kısmı hesaba katmamak.','orta','şekilli',4,'isc-izgara','Izgara üzerinde boyanan kısım')
kartla('K-ISC-04','Havuz seviye göstergesi','Seviye göstergesinden dolum kesri okunur; ikinci musluk açılınca hızlar toplanır.','Havuzun tamamını yeniden doldurmak; bölme sayısını yanlış okumak.','orta','şekilli',4,'isc-seviye','Havuz seviyesi ve ikinci musluk')
kartla('K-ISC-05','Kalan iş grafiği','Doğru parçalarının eğimlerinden hızlar bulunur; ayrılan işçiden sonraki hız kullanılır.','Eğimi birlikte hız yerine tek hız sanmak; süreyi eklemeyi unutmak.','zor','grafik',5,'isc-kalan','Kalan iş–zaman grafiği')
kartla('K-ISC-06','İş günü takvimi','İki işçinin birleşik hızından gerekli iş günü bulunur; takvimde hafta sonu ve tatiller atlanır.','Hafta sonunu saymak; tatili iş günü saymak.','orta','şekilli',5,'isc-takvim','Tatilli takvimde bitiş günü')
kartla('K-ISC-07','İşçi sayısı basamak grafiği','Grafikten işçi-gün toplamı bulunur; planlanan toplam işten çıkarılıp kalan gün hesaplanır.','Planlanan işçi sayısını sabit varsaymak.','orta','grafik',4,'isc-basamak','Gün gün işçi sayısı grafiği')
kartla('K-ISC-08','Gösterge okuma','İki göstergenin aynı sürede gösterdiği yüzdeler toplanıp birlikte hız bulunur.','Yüzdeleri birlikte tamamlanma yüzdesi sanmak.','kolay','şekilli',3,'isc-kadran','İş göstergeleri ve birlikte çalışma')
kartla('K-ISC-09','Emek tablosu ve ücret','Her kişinin işin kaçta kaçını yaptığı çalışılan gün ÷ tek başına gün ile bulunur; ücret bu kesirlerle paylaşılır.','Ücreti çalışılan günle orantılamak.','orta','tablo',4,'isc-ucret','Çalışma tablosundan ücret paylaşımı')
kartla('K-ISC-10','Depo hacim grafiği','Eğimlerden dolum ve gider hızı bulunur; gider kapanınca kalan hacim dolum hızıyla doldurulur.','Ayrı eğimleri birbirine karıştırmak; süreyi yalnız kalan bölüm sanmak.','zor','grafik',5,'isc-depo','Dolum–gider hacim grafiği')

# ---------- 01 daire grafiği ----------
ang={'Ali':120,'Burak':60,'Cem':90,'Yapılmayan':90}; assert sum(ang.values())==360
fr={k:Fr(v,360) for k,v in ang.items()}; h={k:fr[k]/4 for k in ('Ali','Burak','Cem')}
kal=fr['Yapılmayan']; d1=kal/(h['Ali']+h['Burak']); assert d1==2 and h['Ali']==Fr(1,12) and h['Burak']==Fr(1,24)
e1=[kal/h['Ali'],kal/h['Cem'],Fr(1,2)/(h['Ali']+h['Burak']),1/(h['Ali']+h['Burak'])]
assert e1==[3,4,4,8] or True
e1=[kal/h['Ali'],kal/h['Burak'],Fr(1,2)/(h['Ali']+h['Burak']),1/(h['Ali']+h['Burak'])]
assert e1==[3,6,4,8] and len({d1,*e1})==5
a0=90; o=[]
cols={'Ali':'vurgu!40','Burak':'vurgu!18','Cem':'black!14','Yapılmayan':'white'}
for k,v in ang.items():
    a1=a0-v; o.append(f'\\filldraw[fill={cols[k]},line width=1pt] (0,0) -- ({a0}:1.5) arc ({a0}:{a1}:1.5) -- cycle;')
    m=math.radians((a0+a1)/2); o.append(tx(2.15*math.cos(m),1.85*math.sin(m),f'{k}\\\\ {v}$^\\circ$','align=center')); a0=a1
SK=fig('\n'.join(o))
q('0001',tipId='isc-daire',tip='Daire grafiğinden iş payı ve kalan süre',z='orta',alt='Birlikte Çalışma',kaz='Daire grafiğindeki iş paylarından sabit hızları bulup ayrılan işçiden sonra kalan işin süresini hesaplar.',kalip='grafik',sekil=SK,
 kart='K-ISC-01 (daire grafiği) · 120°, 60°, 90°, kalan 90°; Cem ayrılır',
 metin='Ali, Burak ve Cem, bir bahçe duvarını örmek için aynı anda işe başlamış ve sabit hızlarla 4 gün çalışmıştır. İşin tamamına göre her işçinin 4 günde yaptığı kısım ile henüz yapılmayan kısım yukarıdaki daire grafiğinde gösterilmiştir. Cem bu günün sonunda işten ayrılmış, Ali ve Burak aynı hızlarla çalışarak kalan işi bitirmiştir.\nBuna göre kalan iş kaç günde bitirilmiştir?',
 dogru=2,yan=[(3,'Kalan işi yalnız Ali yapıyor sanmış: (1/4) ÷ (1/12) = 3.','dikkat'),(4,'Kalan işi 1/2 sanmış (yapılmayan dilimi yerine yapılan yarıyı almış): (1/2) ÷ (1/8) = 4.','dikkat'),(6,'Kalan işi yalnız Burak yapıyor sanmış: (1/4) ÷ (1/24) = 6.','dikkat'),(8,'Kalan iş yerine işin tamamını almış: 1 ÷ (1/8) = 8.','dikkat')],
 istenen='Kalan işin bitirilme süresi (gün).',
 ip=['Dilimlerin açıları, işçilerin aynı sürede yaptığı işin kesrini verir; bunlardan işçilerin günlük hızlarını bul.'],
 bilgi=[PAY],
 ad=[A('Kesirleri bul','Her dilimin açısı 360°’ye oranlanır.','Ali 1/3, Burak 1/6, Cem 1/4, kalan 1/4'),A('Günlük hızı bul','Kesirler 4 güne bölünür.','Ali 1/12, Burak 1/24'),A('Birlikte hız','Cem ayrıldığı için yalnız iki işçinin hızı toplanır.','1/12 + 1/24 = 1/8'),A('Kalan süre','Kalan iş birlikte hıza bölünür.','(1/4) ÷ (1/8) = 2 gün')],
 puf='Aynı sürede çalışan işçilerin yaptığı işler hızlarıyla orantılıdır; kalan işi yeni ekibin hızına böl.')

# ---------- 02 sütun grafiği ----------
gunl=[40,40,40,100,100]; top=720; kalan2=top-sum(gunl); hz2=Fr(100,2); d2=len(gunl)+kalan2/hz2; assert d2==13
e2=[len(gunl)+Fr(kalan2,100),len(gunl)+Fr(kalan2,40),kalan2/hz2,3+kalan2/hz2]; assert e2==[9,15,8,11] and len({d2,*e2})==5
sx=.8;sy=.022;o=[]
for t in range(0,121,20): o.append(ln(0,t*sy,5*sx+.2,t*sy,'black!15,line width=.4pt')); o.append(tx(-.3,t*sy,f'\\footnotesize {t}'))
o+=[ln(0,0,0,125*sy,'line width=1pt'),ln(0,0,5*sx+.2,0,'line width=1.2pt'),tx(-.1,125*sy+.3,'\\footnotesize Fidan sayısı'),tx(5*sx+.65,0,'\\footnotesize gün')]
for i,v in enumerate(gunl):
    x=.2+i*sx; o.append(f'\\fill[vurgu!45] ({x:.3f},0) rectangle ({x+.5:.3f},{v*sy:.3f});'); o.append(tx(x+.25,-.3,f'\\footnotesize {i+1}'))
SK=fig('\n'.join(o))
q('0002',tipId='isc-sutun',tip='Günlük üretim sütun grafiği',z='orta',alt='Günlük Üretim Grafiği',kaz='Sütun grafiğinden ilk günlerde yapılan işi okuyup ekip küçülünce yarıya inen günlük hızla işin biteceği günü hesaplar.',kalip='grafik',sekil=SK,
 kart='K-ISC-02 (sütun grafiği) · 5 günde 320 fidan, 6. günden hız yarıya iniyor, toplam 720',
 metin='Bir belediye ekibi, park alanına toplam 720 fidan dikecektir. Ekibin ilk beş gün boyunca her gün diktiği fidan sayısı yukarıdaki grafikte verilmiştir. Çalışan işçilerin hepsi aynı verimle çalışmaktadır; 6. günden itibaren işçilerin yarısı başka bir işe geçmiş, kalan işçiler işi her gün çalışarak sürdürmüştür.\nBuna göre dikim işi kaçıncı günün sonunda bitmiştir?',
 dogru=int(d2),yan=[(9,'İşçilerin yarısının ayrıldığını hesaba katmamış: 5 + 400 ÷ 100 = 9.','dikkat'),(15,'Kalan işi ilk günlerin hızıyla (40) bölmüş: 5 + 400 ÷ 40 = 15.','dikkat'),(8,'Yalnız kalan günü yazmış, ilk 5 günü eklememiş: 400 ÷ 50 = 8.','dikkat'),(11,'Kalan günü yalnız ilk 3 güne eklemiş: 3 + 8 = 11.','dikkat')],
 istenen='İşin biteceği gün.',
 ip=['Grafikten ilk beş günde dikilen toplam fidanı bul; 6. günden sonraki günlük dikim sayısının ne olacağını düşün.'],
 bilgi=[GUN],
 ad=[A('Dikilenleri topla','İlk beş günde dikilen fidan sayısı bulunur.','40 + 40 + 40 + 100 + 100 = 320'),A('Kalanı bul','Toplamdan dikilenler çıkarılır.','720 − 320 = 400'),A('Yeni hız','İşçilerin yarısı kaldığı için günlük dikim yarıya iner.','100 ÷ 2 = 50 fidan/gün'),A('Süre ve gün','Kalan iş yeni hıza bölünür, geçen günlere eklenir.','400 ÷ 50 = 8 gün; 5 + 8 = 13')],
 puf='Önce yapılan işi grafikten topla; işçi sayısı değişince günlük hızı da aynı oranda değiştirip kalan işi bununla böl.')

# ---------- 03 ızgara ----------
R,C=5,12; boy=15; ali=Fr(boy,3); alitam=Fr(R*C)/ali; assert ali==5 and alitam==12
bur=Fr(R*C,6); kalan3=R*C-boy; d3=kalan3/(ali+bur); assert d3==3 and bur==10
e3=[kalan3/ali,kalan3/bur,Fr(R*C)/(ali+bur),3+d3]; assert e3==[9,Fr('4.5'),4,6] and len({d3,*e3})==5
o=[]
for i in range(R):
    for j in range(C): o.append(f'\\draw[fill={"vurgu!35" if j<3 else "white"}] ({j*.5},{-i*.5}) rectangle ({j*.5+.5},{-i*.5-.5});')
SK=fig('\n'.join(o))
q('0003',tipId='isc-izgara',tip='Izgara üzerinde boyanan kısım',z='orta',alt='Birlikte Çalışma',kaz='Boyanmış kare sayısından işçinin hızını bulup ikinci işçi katılınca kalan işin süresini hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-ISC-03 (ızgarada boyama) · 3 günde 15 kare, kalan 45 kare',
 metin='Kare kare panolardan oluşan yukarıdaki duvarı Ali sabit hızla boyamaya başlamıştır. Ali’nin 3 günlük çalışması sonunda boyanmış kısım şekilde gösterilmiştir. Bu günün sonunda Burak da işe katılmıştır; Burak bu duvarın tamamını tek başına 6 günde boyayabilmektedir. İkisi de sabit hızla çalışmaktadır.\nBuna göre Burak katıldıktan sonra kalan kısım kaç günde boyanır?',
 dogru=int(d3),yan=[(9,'Kalan kısmı yalnız Ali’nin hızıyla (5 kare/gün) böldü: 45 ÷ 5 = 9.','dikkat'),(Fr('4.5'),'Kalan kısmı yalnız Burak’ın hızıyla (10 kare/gün) böldü: 45 ÷ 10 = 4,5.','dikkat'),(4,'Boyanmış kısmı hesaba katmadan tüm duvarı iki işçinin hızıyla böldü: 60 ÷ 15 = 4.','dikkat'),(6,'Ali’nin çalıştığı 3 günü ekleyip toplam süreyi vermiş: 3 + 3 = 6.','dikkat')],
 istenen='Burak katıldıktan sonra kalan işin süresi (gün).',
 ip=['Şekildeki boyalı kare sayısından Ali’nin günlük boyadığı kare sayısını bul; Burak’ın hızını toplam kare sayısından hesapla.'],
 bilgi=[ILK],
 ad=[A('Kare sayıları','Duvarda 5 × 12 = 60 kare vardır; 3 sütun (15 kare) boyanmıştır.','kalan: 60 − 15 = 45'),A('Hızlar','Ali 3 günde 15 kare boyamıştır; Burak 60 kareyi 6 günde boyar.','Ali 5, Burak 10 kare/gün'),A('Birlikte hız','İkisinin hızı toplanır.','5 + 10 = 15 kare/gün'),A('Süre','Kalan kare birlikte hıza bölünür.','45 ÷ 15 = 3 gün')],
 puf='Şekilden hızı bul (yapılan kısım ÷ süre); birlikte çalışmada hızlar toplanır.')

# ---------- 04 havuz seviye ----------
bol=12; dol=3; saat=2; hA=Fr(dol,bol)/saat; assert hA==Fr(1,8)
hB=Fr(1,24); d4=(1-Fr(dol,bol))/(hA+hB); assert d4==Fr('4.5')
e4=[(1-Fr(dol,bol))/hA,1/(hA+hB),2+d4,(1-Fr(dol,bol))/hB]; assert e4==[6,6,Fr('6.5'),18]
e4=[Fr(dol),1-Fr(dol,bol),2+d4,(1-Fr(dol,bol))/hB]; assert e4==[3,Fr('0.75'),Fr('6.5'),18] and len({d4,*e4})==5
o=['\\draw[line width=1.2pt] (0,3) -- (0,0) -- (2,0) -- (2,3);','\\fill[vurgu!22] (.03,.03) rectangle (1.97,.75);']
for i in range(1,12): o.append(ln(2,i*.25,2.15 if i%3 else 2.3,i*.25,'line width=.7pt'))
o+=[ln(0,.75,2,.75,'line width=1pt'),tx(3.2,.75,'\\footnotesize 3. bölme'),tx(1,-.4,'\\footnotesize 2 saat sonra')]
SK=fig('\n'.join(o))
q('0004',tipId='isc-seviye',tip='Havuz seviyesi ve ikinci musluk',z='orta',alt='Havuz ve Musluk',kaz='Seviye göstergesinden musluğun doldurduğu kesri bulup ikinci musluk açılınca havuzun dolma süresini hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-ISC-04 (havuz seviyesi) · 12 bölmeden 3’ü 2 saatte, ikinci musluk 24 saatte',
 metin='Boş bir yüzme havuzunun kenarındaki gösterge 12 eş bölmeye ayrılmıştır. A musluğu tek başına açıldıktan 2 saat sonra su düzeyi şekildeki gibi olmuştur. Bu andan sonra, havuzu tek başına 24 saatte dolduran B musluğu da açılmıştır. İki musluğun debisi sabittir ve havuzdan su çıkmamaktadır.\nBuna göre B musluğu açıldıktan kaç saat sonra havuz dolar?',
 dogru=Fr('4.5'),yan=[(3,'Dolu bölme sayısını (3) süre sanmış.','dikkat'),(Fr('0.75'),'Kalan kesri (3/4) süre sanmış.','dikkat'),(Fr('6.5'),'İlk 2 saati de eklemiş (toplam süre): 2 + 4,5 = 6,5.','dikkat'),(18,'Kalan kısmı yalnız B musluğuyla doldurmuş: (3/4) ÷ (1/24) = 18.','dikkat')],
 istenen='B musluğu açıldıktan sonra geçen süre (saat).',
 ip=['Göstergeden A musluğunun 1 saatte havuzun kaçta kaçını doldurduğunu bul; kalan kısmı iki musluğun birlikte hızına böl.'],
 bilgi=[SEV],
 ad=[A('Dolu kısım','Su düzeyi 12 bölmeden 3’ünü kaplamaktadır.','3/12 = 1/4; kalan 3/4'),A('A’nın hızı','A 2 saatte havuzun 1/4’ünü doldurmuştur.','(1/4) ÷ 2 = 1/8 havuz/saat'),A('Birlikte hız','B tek başına 24 saatte doldurur.','1/8 + 1/24 = 1/6'),A('Süre','Kalan kısım birlikte hıza bölünür.','(3/4) ÷ (1/6) = 4,5')],
 puf='Göstergedeki dolu bölmeden hızı bul; yeni musluk açılınca hızları topla ve yalnız kalan kısmı böl.')

# ---------- 05 kalan iş grafiği ----------
rA=Fr(100-70,6); assert rA==5
rAB=Fr(70-30,8-6); assert rAB==20; rB=rAB-rA; assert rB==15
d5=8+Fr(30)/rB; assert d5==10
e5=[8+Fr(30)/rA,8+Fr(30)/rAB,Fr(30)/rB,Fr(100)/((rA+rAB)/2)]
assert e5==[14,Fr('9.5'),2,8] and len({d5,*e5})==5
sx=.42; sy=.034; o=[]
for t in range(0,13,2): o.append(ln(t*sx,0,t*sx,100*sy,'black!12,line width=.4pt')); o.append(tx(t*sx,-.3,f'\\footnotesize {t}'))
for v in range(0,101,10): o.append(ln(0,v*sy,12*sx,v*sy,'black!12,line width=.4pt')); o.append(tx(-.4,v*sy,f'\\footnotesize {v}'))
o+=[ln(0,0,12*sx,0,'line width=1.2pt'),ln(0,0,0,100*sy,'line width=1.2pt'),tx(12*sx+.5,0,'\\footnotesize gün'),tx(.3,100*sy+.3,'\\footnotesize Kalan iş (\\%)'),
 f'\\draw[line width=1.8pt] (0,{100*sy}) -- ({6*sx},{70*sy}) -- ({8*sx},{30*sy});',f'\\fill ({6*sx},{70*sy}) circle (.07); \\fill ({8*sx},{30*sy}) circle (.07);']
SK=fig('\n'.join(o))
q('0005',tipId='isc-kalan',tip='Kalan iş–zaman grafiği',z='zor',alt='İşçi Sayısı ve Verim',kaz='Kalan iş grafiğindeki doğru parçalarının eğimlerinden hızları bulup ayrılan işçiden sonra işin biteceği günü hesaplar.',kalip='grafik',sekil=SK,
 kart='K-ISC-05 (kalan iş grafiği) · hızlar 5 ve 15, birlikte 20 (%/gün)',
 metin='Bir inşaat firmasında Usta tek başına çalışmaya başlamış, bir süre sonra çırağı da ona katılmıştır. Yukarıdaki grafik, işin yüzde kaçının henüz yapılmadığını zamana göre göstermektedir. Grafikte ikinci parça, çırağın katıldığı andan Usta’nın işten ayrıldığı ana kadar uzanmaktadır; Usta ayrılınca çırak aynı hızla çalışmaya devam etmiştir. Herkes sabit hızla çalışmaktadır.\nBuna göre iş toplam kaç günde bitmiştir?',
 dogru=int(d5),yan=[(2,'Yalnız çırağın çalışacağı süreyi yazmış, ilk 8 günü eklememiş: 30 ÷ 15 = 2.','dikkat'),(8,'Her iki doğrunun hızlarının ortalamasıyla (12,5) tüm işi bölmüş: 100 ÷ 12,5 = 8.','dikkat'),(Fr('9.5'),'İkinci parçanın eğimini (20) çırağın hızı sanmış: 8 + 30 ÷ 20 = 9,5.','dikkat'),(14,'Kalan işi Usta’nın hızıyla bölmüş: 8 + 30 ÷ 5 = 14.','dikkat')],
 istenen='İşin toplam süresi (gün).',
 ip=['Her doğru parçasının eğimi o aralıktaki toplam hızı verir; çırağın tek başına hızını iki eğimin farkından bul.'],
 bilgi=[GRF],
 ad=[A('Usta’nın hızı','İlk parçada kalan iş 100’den 70’e 6 günde inmiştir.','30 ÷ 6 = %5 / gün'),A('Birlikte hız','İkinci parça 6. günden 8. güne iner.','(70 − 30) ÷ 2 = %20 / gün'),A('Çırağın hızı','Birlikte hızdan Usta’nın hızı çıkarılır.','20 − 5 = %15 / gün'),A('Kalan iş','8. günde kalan iş %30’dur ve yalnız çırak çalışır.','30 ÷ 15 = 2 gün'),A('Toplam süre','Geçen 8 gün ile 2 gün toplanır.','8 + 2 = 10')],
 puf='Kalan iş grafiğinde eğimin büyüklüğü o aralıktaki hızdır; ayrılan işçiden sonra eğim, kalan işçinin hızıdır.')

# ---------- 06 takvim ----------
TAT=(9,16); BAS=4; GUNLER=31
def hf(d): return d%7   # ay Salı ile başlar: 1 → 1
def bitis(n,sayt=True,sayh=True):
    d=BAS; c=0
    while True:
        ok=not((sayh and hf(d)>=5) or (sayt and d in TAT))
        if ok:
            c+=1
            if c==n: return d
        d+=1
assert hf(4)==4
t6=Fr(1,18)+Fr(1,36); gun6=1/t6; assert gun6==12
d6=bitis(12); e6=[bitis(12,False,True),bitis(12,True,False),bitis(12,False,False),BAS+12]
assert d6==23 and e6==[21,17,15,16] and len({d6,*e6})==5
cw=.8; ch=.5; o=[]
for j,g in enumerate(['Pzt','Sal','Çar','Per','Cum','Cmt','Paz']): o.append(f'\\node[draw,minimum width={cw}cm,minimum height={ch}cm,inner sep=1pt,fill=black!8] at ({j*cw},0) {{\\footnotesize {g}}};')
for d in range(1,GUNLER+1):
    idx=d-1+1; r,c=divmod(idx,7)
    f='vurgu!35' if d in TAT else ('black!12' if c>=5 else None)
    o.append(f'\\node[draw,minimum width={cw}cm,minimum height={ch}cm,inner sep=1pt{",fill="+f if f else ""}] at ({c*cw},{-(r+1)*ch}) {{\\footnotesize {d}}};')
o.append(f'\\draw[fill=vurgu!35] (.0,-3.55) rectangle (.2,-3.35); '+tx(1.0,-3.45,'\\footnotesize resmî tatil'))
o=[x.replace('\\footnotesize resmî tatil','\\footnotesize resmî tatil') for x in o]
SK=fig('\n'.join(o))
q('0006',tipId='isc-takvim',tip='Tatilli takvimde bitiş günü',z='orta',alt='Birlikte Çalışma',kaz='İki işçinin birleşik hızından gereken iş gününü bulup hafta sonu ve resmî tatilleri atlayarak bitiş tarihini belirler.',kalip='şekilli',sekil=SK,
 kart='K-ISC-06 (tatilli takvim) · 18 ve 36 günlük işçiler, 4’ünde başlıyor',
 metin='Bir tadilat firmasında Usta bir daireyi tek başına 18 iş gününde, Kalfa ise tek başına 36 iş gününde boyayabilmektedir. İkisi de sabit hızla çalışmaktadır. Yukarıdaki takvimde gösterilen ayın 4’ünde birlikte işe başlıyorlar; yalnızca Pazartesi–Cuma günleri çalışıyorlar ve takvimde işaretli resmî tatil günlerinde de çalışmıyorlar. Başlama günü de çalışılan günlerdendir.\nBuna göre iş ayın kaçıncı günü biter?',
 dogru=d6,yan=[(15,'Ayın 4’ünden itibaren 12 günü hiç atlamadan saymış (hafta sonu ve tatili hesaba katmamış): 4 + 11 = 15.','dikkat'),(16,'Başlama gününü saymayıp 12 gün eklemiş: 4 + 12 = 16.','dikkat'),(17,'Hafta sonlarını da çalışılan gün saymış, yalnızca resmî tatilleri atlamış.','dikkat'),(21,'Hafta sonlarını atlamış ancak işaretli resmî tatilleri iş günü saymış.','dikkat')],
 istenen='İşin biteceği gün.',
 ip=['İki işçinin birlikte kaç iş gününde bitireceğini bul; sonra takvimde yalnız çalışılan günleri say.'],
 bilgi=[TAK],
 ad=[A('Birlikte hız','İki işçinin günlük işleri toplanır.','1/18 + 1/36 = 1/12'),A('İş günü sayısı','Birlikte işi 12 iş gününde bitirirler.','12 iş günü'),A('Takvimi say','4 Cuma günüdür; Cumartesi, Pazar ve işaretli 9 ile 16 atlanarak çalışılan günler yazılır.','4, 7, 8, 10, 11, 14, 15, 17, 18, 21, 22, 23'),A('Bitiş','Listedeki 12. gün işin bittiği gündür.','12. iş günü: 23')],
 puf='Önce birleşik hızla gereken iş günü sayısını bul; takvimde yalnız çalışılan günleri say.')

# ---------- 07 işçi sayısı basamak grafiği ----------
isc=[2,2,4,4]; plan=5*8; yap=sum(isc); kal7=plan-yap; d7=len(isc)+Fr(kal7,4); assert (plan,yap,kal7,d7)==(40,12,28,11)
e7=[Fr(kal7,4),Fr(plan,4),4+Fr(plan-5*4,4),8]; assert e7==[7,10,9,8] and len({d7,*e7})==5
sx=.9;sy=.45;o=[]
for t in range(0,7): o.append(ln(0,t*sy,4*sx+.2,t*sy,'black!15,line width=.4pt')); o.append(tx(-.3,t*sy,f'\\footnotesize {t}'))
o+=[ln(0,0,0,6.3*sy,'line width=1pt'),ln(0,0,4*sx+.2,0,'line width=1.2pt'),tx(.3,6.3*sy+.3,'\\footnotesize Çalışan işçi sayısı'),tx(4*sx+.6,0,'\\footnotesize gün')]
for i,v in enumerate(isc):
    x=.15+i*sx; o.append(f'\\fill[vurgu!45] ({x:.3f},0) rectangle ({x+.6:.3f},{v*sy:.3f});'); o.append(tx(x+.3,-.3,f'\\footnotesize {i+1}'))
SK=fig('\n'.join(o))
q('0007',tipId='isc-basamak',tip='Gün gün işçi sayısı grafiği',z='orta',alt='İşçi Sayısı ve Verim',kaz='Gün gün değişen işçi sayısından yapılan işçi-günü bulup planlanan toplam işten kalanı ve bitiş gününü hesaplar.',kalip='grafik',sekil=SK,
 kart='K-ISC-07 (işçi sayısı grafiği) · 5 işçi 8 gün = 40 işçi-gün, ilk 4 günde 12',
 metin='Eşit verimle çalışan 5 işçi bir sıva işini 8 günde bitirebilecekken, malzeme gecikmesi nedeniyle ilk dört gün çalışan işçi sayısı yukarıdaki grafikteki gibi olmuştur. Beşinci günden itibaren işçi sayısı 4 olarak sabit kalmış ve iş bu şekilde bitirilmiştir; işe her gün çalışılmıştır.\nBuna göre iş kaçıncı günün sonunda bitmiştir?',
 dogru=int(d7),yan=[(7,'İlk dört günü hesaba katmadan kalan süreyi yazmış: 28 ÷ 4 = 7.','dikkat'),(8,'Planlanan süreyi (8 gün) cevap sanmış.','dikkat'),(9,'İlk dört günde de 5 işçi çalışmış sanmış: 4 + (40 − 20) ÷ 4 = 9.','dikkat'),(10,'Tüm işi 4 işçiyle yapılmış gibi bölmüş: 40 ÷ 4 = 10.','dikkat')],
 istenen='İşin bittiği gün.',
 ip=['İşin tamamını işçi-gün cinsinden bul; grafikteki ilk dört günde yapılan işçi-günü çıkar.'],
 bilgi=[GUN],
 ad=[A('Toplam iş','5 işçi 8 günde bitirir.','5 × 8 = 40 işçi-gün'),A('Yapılan iş','Grafikteki işçi sayıları toplanır.','2 + 2 + 4 + 4 = 12'),A('Kalan süre','Kalan iş, 4 işçiye bölünür.','(40 − 12) ÷ 4 = 7 gün'),A('Bitiş','İlk dört gün eklenir.','4 + 7 = 11')],
 puf='Eşit verimli işçilerde işi işçi-gün ile ölç; değişen işçi sayılarını gün gün topla.')

# ---------- 08 kadran ----------
pa,pb,sa=30,20,3
tum8=Fr(100)/Fr(pa+pb,sa); assert tum8==6
e8=[sa,Fr(100*sa,pa),Fr(100*sa,pb),sa+tum8]; assert e8==[3,10,15,9] and len({tum8,*e8})==5
def kadran(cx,p,ad_):
    ls=[f'\\draw[line width=1.2pt] ({cx+1.5},0) arc (0:180:1.5) -- cycle;']
    for k in range(0,101,10):
        a=math.radians(180-1.8*k); c,s=math.cos(a),math.sin(a)
        ls.append(ln(cx+1.5*c,1.5*s,cx+1.3*c,1.3*s,'line width=.8pt')); ls.append(tx(cx+1.7*c,1.7*s,f'\\tiny {k}'))
    a=math.radians(180-1.8*p); ls.append(ln(cx,0,cx+1.3*math.cos(a),1.3*math.sin(a),'line width=1.6pt,vurgu')); ls.append('\\fill (%.2f,0) circle (.06);'%cx)
    ls.append(tx(cx,-.4,f'\\textbf{{{ad_}}}')); return ls
SK=fig('\n'.join(kadran(0,pa,'Makine A')+kadran(4.0,pb,'Makine B')))
q('0008',tipId='isc-kadran',tip='İş göstergeleri ve birlikte çalışma',z='kolay',alt='Birlikte Çalışma',kaz='İki göstergenin aynı sürede gösterdiği yüzdelerden birlikte hızı bulup işin toplam süresini hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-ISC-08 (kadran) · 3 saatte %30 ve %20',
 metin='Bir matbaadaki aynı işi yapan A ve B baskı makinelerinin üzerindeki göstergeler, makineler aynı anda çalışmaya başladıktan 3 saat sonra yukarıdaki gibi görünmektedir. Göstergeler, makinelerin kendi başlarına tamamladığı işin yüzdesini göstermektedir. İki makine de sabit hızla çalışmaktadır ve bir sipariş iki makineye birlikte yaptırılmaktadır.\nBuna göre bu sipariş birlikte çalışan iki makineyle toplam kaç saatte biter?',
 dogru=int(tum8),yan=[(3,'Göstergelerin 3 saatte işin yarısı kadar iş yaptığını görüp süreyi 3 sanmış (toplam yüzde 50’yi 100’e tamamlamamış).','dikkat'),(9,'Başlangıçtaki 3 saati kalan 6 saate değil, toplam 6 saate eklemiş: 3 + 6 = 9.','dikkat'),(10,'Yalnız A makinesinin tüm işi bitirme süresini yazmış: 3 ÷ 0,30 = 10.','dikkat'),(15,'Yalnız B makinesinin tüm işi bitirme süresini yazmış: 3 ÷ 0,20 = 15.','dikkat')],
 istenen='İşin birlikte bitirilme süresi (saat).',
 ip=['İki göstergenin aynı sürede birlikte yaptığı işi bul; bütün işi bu orana göre değerlendir.'],
 bilgi=[KAD],
 ad=[A('Göstergeleri oku','A %30, B %20 göstermektedir.','30 + 20 = %50'),A('Birlikte hız','3 saatte işin %50’si yapılmıştır.','%50 / 3 saat'),A('Tüm iş','İşin tamamı için 2 katı süre gerekir.','3 × 2 = 6 saat')],
 puf='Aynı sürede iki makinenin yaptığı işi topla; işin tamamı için süre bu toplama oranla bulunur.')

# ---------- 09 tablo ve ücret ----------
Tb=[('Usta',4,10),('Kalfa',3,12),('Çırak',7,20)]
fr9=[Fr(g,t) for _,g,t in Tb]; assert sum(fr9)==1
UC=8000; pay=[f*UC for f in fr9]; assert pay==[3200,2000,2800]
e9=[Fr(7,14)*UC*Fr(1,1),pay[1],pay[0],UC-pay[2]]; assert e9==[4000,2000,3200,5200] and len({pay[2],*e9})==5
SK=tablo_svg(['İşçi','Çalıştığı gün','Tek başına bitirme (gün)'],[[n,str(g),str(t)] for n,g,t in Tb])
q('0009',tipId='isc-ucret',tip='Çalışma tablosundan ücret paylaşımı',z='orta',alt='Ücret Paylaşımı',kaz='Tablodaki çalışma günlerinden her işçinin işin kaçta kaçını yaptığını bulup toplam ücreti paylaştırır.',kalip='tablo',sekil=SK,
 kart='K-ISC-09 (tablo ve ücret) · 4/10, 3/12, 7/20; 8 000 TL',
 metin='Üç işçi, bir parke döşeme işini sırayla çalışarak bitirmiş; her biri sabit hızla çalışmıştır. Tabloda her işçinin işte çalıştığı gün sayısı ile aynı işi tek başına bitirme süresi verilmiştir. İş bittikten sonra firma, toplam 8 000 TL ücreti işçilere yaptıkları iş oranında paylaştırmıştır; işte başka çalışan yoktur.\nBuna göre Çırak’ın aldığı ücret kaç TL’dir?',
 dogru=2800,yan=[(2000,'Kalfa’nın payını yazmış.','dikkat'),(3200,'Usta’nın payını yazmış.','dikkat'),(4000,'Ücreti çalışılan günlerle orantılamış: 7/14 × 8 000 = 4 000.','dikkat'),(5200,'Çırak yerine diğer iki işçinin toplam payını yazmış: 8 000 − 2 800.','dikkat')],
 istenen='Çırak’ın aldığı ücret (TL).',
 ip=['Her işçinin çalıştığı günü, onun tek başına bitirme süresine oranlayıp işin kaçta kaçını yaptığını bul.'],
 bilgi=[UCR],
 ad=[A('İş kesirleri','Çalışılan gün ÷ tek başına bitirme süresi','Usta 4/10, Kalfa 3/12, Çırak 7/20'),A('Denetle','Kesirler işin tamamını vermelidir.','2/5 + 1/4 + 7/20 = 1'),A('Çırak’ın payı','Kesir toplam ücretle çarpılır.','7/20 × 8 000 = 2 800 TL')],
 puf='Ücreti, her işçinin yaptığı iş kesriyle paylaştır; iş kesri = çalıştığı gün ÷ tek başına süre.')

# ---------- 10 depo grafiği ----------
r1=Fr(240,2); g_=r1-Fr(480-240,6-2); assert (r1,g_)==(120,60)
tank=600; d10=6+Fr(tank-480,r1); assert d10==7
e10=[6+Fr(tank-480,r1-g_),Fr(tank,r1)+0,Fr(tank,r1-g_),Fr(tank-480,r1)]
assert e10==[8,5,10,1] and len({d10,*e10})==5
sx=.42; sy=.0055; o=[]
for t in range(0,13,2): o.append(ln(t*sx,0,t*sx,600*sy,'black!12,line width=.4pt')); o.append(tx(t*sx,-.3,f'\\footnotesize {t}'))
for v in range(0,601,100): o.append(ln(0,v*sy,12*sx,v*sy,'black!12,line width=.4pt')); o.append(tx(-.4,v*sy,f'\\footnotesize {v}'))
o+=[ln(0,0,12*sx,0,'line width=1.2pt'),ln(0,0,0,600*sy,'line width=1.2pt'),tx(12*sx+.5,0,'\\footnotesize saat'),tx(.4,600*sy+.3,'\\footnotesize Hacim (L)'),
 f'\\draw[line width=1.8pt] (0,0) -- ({2*sx},{240*sy}) -- ({6*sx},{480*sy});',f'\\fill ({2*sx},{240*sy}) circle (.07); \\fill ({6*sx},{480*sy}) circle (.07);']
SK=fig('\n'.join(o))
q('0010',tipId='isc-depo',tip='Dolum–gider hacim grafiği',z='zor',alt='Havuz ve Musluk',kaz='Grafikteki eğimlerden dolum ve gider debilerini bulup gider kapatıldıktan sonra deponun dolma süresini hesaplar.',kalip='grafik',sekil=SK,
 kart='K-ISC-10 (depo hacim grafiği) · 120 L/sa dolum, 60 L/sa gider, 600 L',
 metin='Boş bir su deposuna sabit debili bir musluktan su akıtılırken, 2. saatte deponun altındaki sabit debili bir gider açılmıştır. Deponun içindeki su hacminin zamanla değişimi yukarıdaki grafikte, ilk 6 saat için gösterilmiştir. Gider 6. saatin sonunda kapatılmış, musluk aynı debiyle akmaya devam etmiştir. Deponun hacmi 600 litredir.\nBuna göre depo, musluğun açılmasından kaç saat sonra dolar?',
 dogru=int(d10),yan=[(1,'Yalnız kalan 120 L’nin dolum süresini yazmış, ilk 6 saati eklememiş.','dikkat'),(5,'Deponun tamamını musluğun debisiyle (120 L/sa) bölmüş: 600 ÷ 120 = 5, gideri hiç hesaba katmamış.','dikkat'),(8,'Gider kapanınca da ikinci doğrunun eğimiyle (60 L/sa) devam etmiş: 6 + 120 ÷ 60 = 8.','dikkat'),(10,'Depoyu baştan 60 L/sa ile doldurmuş: 600 ÷ 60 = 10.','dikkat')],
 istenen='Deponun dolma süresi (saat).',
 ip=['İlk doğrunun eğimi tek başına musluğun debisidir; ikinci doğrunun eğimi musluk ve giderin birlikte etkisidir.'],
 bilgi=[GRF],
 ad=[A('Musluğun debisi','0–2 saatte hacim 240 L artmıştır.','240 ÷ 2 = 120 L/sa'),A('Gider debisi','2–6 saatte hacim 240 L’den 480 L’ye çıkmıştır; eğim musluk eksi gider.','(480 − 240) ÷ 4 = 60 L/sa → gider 120 − 60 = 60'),A('Kalan hacim','6. saatte 480 L vardır.','600 − 480 = 120 L'),A('Gider kapalı süre','Gider kapanınca eğim yeniden 120 L/sa olur.','120 ÷ 120 = 1 saat'),A('Toplam süre','Geçen 6 saatle toplanır.','6 + 1 = 7')],
 puf='Doğrunun eğimi o aralıktaki net debidir; gider kapanınca eğim yalnız musluğun debisine döner.')

bitir(P,'iscisekb','prob|İşçi Emek Problemleri')
