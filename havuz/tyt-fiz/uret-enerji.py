import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif as H
from _hafif import *
H.KONU='İş, Güç ve Enerji'
P=Parti('enerji','İş, Güç ve Enerji','fiz|İş, Güç ve Enerji',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (iş, güç, enerji) · MEB 9. sınıf'
kart('K-FZEN-01','Kuvvet–yol grafiği','Kuvvet–yol grafiğinde eğrinin altında kalan alan yapılan işe eşittir.','Yalnız dikdörtgen alanı almak; üçgeni 1/2 ile çarpmamak.','kolay','grafik',2,'fz-en-grafik','Kuvvet–yol grafiğinden iş',KY)
kart('K-FZEN-02','Güç ve verim','P = W ÷ t; verimli sistemde girdi gücü = yararlı güç ÷ verim.','Verimi çarpmak; süreyi hesaba katmamak.','orta','hikâyeli',4,'fz-en-guc-verim','Motorun gücü ve verimi',KY)
kart('K-FZEN-03','Mekanik enerji korunumu','Sürtünmesiz yolda E_k + E_p sabittir; E_k = m × g × (yükseklik farkı).','Başlangıç ya da bitiş potansiyel enerjisini kinetik enerji sanmak.','orta','şekilli',3,'fz-en-korunum','Mekanik enerjinin korunumu',KY)
kart('K-FZEN-04','Sürtünmeli yol','Enerji kaybı ısıya dönüşür; kalan kinetik enerji, yatay yoldaki sürtünme işiyle tükenir.','Kayıp enerjiyi kalan enerji sanmak; eğik yoldaki kaybı atlamak.','zor','şekilli',4,'fz-en-surtunme','Sürtünmeli yolda enerji dönüşümü',KY)
IS=B('İş','W = F × x (kuvvet yol doğrultusundayken). Kuvvet–yol grafiğinde grafiğin altında kalan alan işi verir. Örnek: 10 N’luk kuvvet 3 m’de 30 J iş yapar')
EP=B('Potansiyel ve kinetik enerji','E_p = m × g × h; E_k = ½ × m × v². Sürtünmesiz yolda E_k + E_p sabit kalır. Örnek: 2 kg, 5 m için E_p = 2 × 10 × 5 = 100 J')
# ---- 0001 grafik
x0,y0,sx,sy=45,125,28,3.6
def X(v): return x0+v*sx
def Y(v): return y0-v*sy
poli=f'<path d="M{X(0)} {Y(0)} L{X(2)} {Y(20)} L{X(5)} {Y(20)} L{X(5)} {Y(0)} Z" stroke-width="2" style="fill:{G.ACC};fill-opacity:.2;stroke:{G.ACC}"/>'
ax=L(x0,y0,x0+5.6*sx,y0,1.6)+L(x0,y0,x0,Y(26),1.6)+T(x0-6,Y(26)+4,'F (N)',anchor='end',size=11,bold=True)+T(X(5.6)+4,y0+4,'x (m)',anchor='start',size=11,bold=True)
for v in (2,5): ax+=L(X(v),y0-3,X(v),y0+3)+T(X(v),y0+16,str(v),size=11)
ax+=L(x0-3,Y(20),x0+3,Y(20))+T(x0-8,Y(20)+4,'20',anchor='end',size=11)+L(x0,Y(20),X(2),Y(20),1,'stroke-dasharray="3 3" opacity=".6"')+L(X(2),Y(20),X(2),y0,1,'stroke-dasharray="3 3" opacity=".6"')
alan=Fr(1,2)*2*20+3*20; assert alan==80 and 3*20==60 and 5*20==100 and Fr(1,2)*2*20==20 and 2*20==40
mk(P,'0001',tipId='fz-en-grafik',tip='Kuvvet–yol grafiğinden iş',z='kolay',alt='İş',kaz='Kuvvet–yol grafiğinin altında kalan alandan yapılan işi hesaplar.',kalip='grafik',adim=2,
 kart='K-FZEN-01 (kuvvet–yol grafiği) · yamuk alan',
 metin='Yatay düzlemde duran bir cisme, yol doğrultusunda uygulanan kuvvetin konuma bağlı grafiği şekildeki gibidir.\nBuna göre cisim 0–5 m konumları arasında hareket ederken kuvvetin yaptığı iş kaç J’dür?',
 sekil=svg(300,150,poli+ax),
 dogru=80,yan=[(20,'Yalnız ilk 2 m’deki üçgenin alanını almış.','dikkat'),(40,'İlk 2 m’de kuvveti sabit 20 N sanıp 2 × 20 hesaplamış.','bilgi'),(60,'Yalnız 2–5 m’deki dikdörtgenin alanını almış.','dikkat'),(100,'Tüm yolu 20 N’luk sabit kuvvet sanıp 5 × 20 hesaplamış; üçgeni dikdörtgen saymış.','bilgi')],
 istenen='Kuvvetin 0–5 m arasında yaptığı iş (J).',
 ip=['İş, grafiğin altında kalan alandır; alanı üçgen ve dikdörtgen olarak iki parçaya ayır.'],
 bilgi=[IS],
 ad=[A('Üçgen kısım','0–2 m arasında kuvvet 0’dan 20 N’a çıkar.','W₁ = ½ × 2 × 20 = 20 J'),A('Dikdörtgen kısım','2–5 m arasında kuvvet 20 N sabittir.','W₂ = 3 × 20 = 60 J'),A('Toplam','Alanlar toplanır.','W = 20 + 60 = 80 J')],
 puf='Kuvvet değişse de iş her zaman kuvvet–yol grafiğinin altında kalan alandır.')
# ---- 0002 güç/verim
m,h,t,v=40,5,10,Fr(80,100); W=m*10*h; Pg=Fr(W,t); Pe=Pg/v
assert W==2000 and Pg==200 and Pe==250 and Pg*v==160 and W/v==2500
mk(P,'0002',tipId='fz-en-guc-verim',tip='Motorun gücü ve verimi',z='orta',alt='Güç ve Verim',kaz='Yük kaldıran motorun yararlı gücünden elektrik girdi gücünü bulur.',kalip='hikâyeli',adim=4,
 kart='K-FZEN-02 (güç ve verim) · yük kaldıran motor',
 metin='Verimi %80 olan bir elektrik motoru, kütlesi 40 kg olan bir yükü sabit hızla 5 m yükseğe 10 s’de çıkarmaktadır.\ng = 10 m/s² olduğuna göre motorun şebekeden çektiği elektrik gücü kaç W’tır?',
 dogru=250,yan=[(160,'Yararlı gücü (200 W) verimle çarpmış.','islem'),(200,'Verimi hesaba katmamış; yararlı gücü elektrik gücü sanmış.','dikkat'),(2000,'Süreye bölmeyi atlayıp yük ağırlığının işini güç sanmış.','islem'),(2500,'Süreye bölmeden iş değerini verime bölmüş.','islem')],
 istenen='Motorun çektiği elektrik gücü (W).',
 ip=['Önce yükün kazandığı enerjiyi, sonra bu enerjiyi sağlayan yararlı gücü bul; yararlı güç, şebekeden çekilen elektrik gücünün %80’idir.'],
 bilgi=[B('Güç','P = W ÷ t; birimi watt (W). Örnek: 10 s’de 500 J iş yapan makinenin gücü 50 W’tır'),B('Verim','verim = yararlı güç ÷ harcanan güç. Örnek: verim %50 ise 100 W harcayan makine 50 W yararlı güç verir')],
 ad=[A('Yükün kazandığı enerji','Sabit hızla kaldırmada motor yükün potansiyel enerji artışı kadar iş yapar.','W = m × g × h = 40 × 10 × 5 = 2000 J'),A('Yararlı güç','İş süreye bölünür.','P_yararlı = 2000 ÷ 10 = 200 W'),A('Verim bağıntısı','Yararlı güç, çekilen gücün %80’idir.','200 = 0,8 × P_çekilen'),A('Sonuç','P_çekilen çekilir.','P_çekilen = 200 ÷ 0,8 = 250 W')],
 puf='Verimli makinede çekilen güç, yararlı gücün verime bölünmesiyle bulunur; verim 1’den küçük olduğundan çekilen güç hep büyüktür.')
# ---- 0003 korunum
mm,hK,hL=2,20,5; Ek=mm*10*(hK-hL)
assert Ek==300 and mm*10*hL==100 and mm*10*hK==400 and Fr(1,2)*Ek==150 and mm*10*(hK-10)==200
xk,yk=40,30; foot=(200,130)
def yl(h): return 130-h*5
xl=xk+(yl(5)-yk)/(130-yk)*(200-xk)
sk=svg(280,160,L(20,130,260,130,2)+f'<path d="M{xk} {yk} L{foot[0]} {foot[1]}" stroke-width="2.5"/>'+f'<circle cx="{xk}" cy="{yk}" r="5" style="fill:currentColor;stroke:none"/><circle cx="{xl:.1f}" cy="{yl(5)}" r="5" style="fill:currentColor;stroke:none"/>'
  +T(xk+14,yk-4,'K',bold=True)+T(xl+14,yl(5)-6,'L',bold=True)
  +L(20,yl(20),xk-8,yl(20),1,'stroke-dasharray="3 3"')+ok(18,yl(20)+0,18,130,G.ACC)+ok(18,130,18,yl(20),G.ACC)+T(24,82,'20 m',anchor='start',size=11,bold=True,renk=G.ACC)
  +L(xl,yl(5),256,yl(5),1,'stroke-dasharray="3 3"')+ok(250,yl(5),250,130,G.ACC)+ok(250,130,250,yl(5),G.ACC)+T(246,118,'5 m',anchor='end',size=11,bold=True,renk=G.ACC)
  +T(150,150,'yatay zemin',size=10))
mk(P,'0003',tipId='fz-en-korunum',tip='Mekanik enerjinin korunumu',z='orta',alt='Mekanik Enerji',kaz='Sürtünmesiz yolda iki nokta arasındaki kinetik enerjiyi enerji korunumundan hesaplar.',kalip='şekilli',adim=3,
 kart='K-FZEN-03 (mekanik enerji korunumu) · yerden yükseklikler verilmiş',
 metin='Kütlesi 2 kg olan bir cisim, sürtünmesiz eğik yolun yerden 20 m yüksekteki K noktasından serbest bırakılıyor. Cisim yerden 5 m yüksekteki L noktasından geçmektedir (şekil).\ng = 10 m/s² olduğuna göre cismin L noktasındaki kinetik enerjisi kaç J’dür?',
 sekil=sk,
 dogru=300,yan=[(100,'L noktasındaki potansiyel enerjiyi (2 × 10 × 5) kinetik enerji sanmış.','dikkat'),(150,'Potansiyel enerji farkını ½ ile çarpmış.','islem'),(200,'K ile L arasındaki yükseklik farkını 10 m almış.','dikkat'),(400,'K noktasındaki toplam enerjiyi L’deki kinetik enerji sanmış.','dikkat')],
 istenen='Cismin L noktasındaki kinetik enerjisi (J).',
 ip=['Sürtünme yok: K’deki potansiyel enerji, L’de potansiyel ve kinetik enerjinin toplamına eşittir.'],
 bilgi=[EP],
 ad=[A('K noktasındaki enerji','Cisim serbest bırakıldığı için yalnız potansiyel enerjisi vardır.','E_K = 2 × 10 × 20 = 400 J'),A('L noktasındaki potansiyel enerji','Yükseklik 5 m’dir.','E_p = 2 × 10 × 5 = 100 J'),A('Enerji korunumu','Toplam enerji değişmez; kalan kısım kinetik enerjidir.','400 = 100 + E_k · E_k = 300 J')],
 puf='Sürtünmesiz yolda kinetik enerji, yükseklik farkından kaybedilen potansiyel enerjiye eşittir: E_k = m × g × Δh.')
# ---- 0004 sürtünmeli
m,h,F=4,10,20; Ep=m*10*h; kayip=Fr(25,100)*Ep; KE=Ep-kayip; xx=KE/F
assert Ep==400 and kayip==100 and KE==300 and xx==15 and Ep/F==20 and (Ep+kayip)/F==25 and kayip/F==5 and (Ep+KE)/F==35
xk,yk=40,35
sk=svg(310,160,f'<path d="M{xk} {yk} L130 130 L275 130" stroke-width="2.5"/>'+L(20,130,300,130,1,'opacity=".4"')
  +f'<circle cx="{xk}" cy="{yk}" r="5" style="fill:currentColor;stroke:none"/>'+T(xk+14,yk-6,'K',bold=True)+T(124,148,'L',bold=True)+T(275,148,'M',bold=True)
  +ok(22,yk,22,130,G.ACC)+ok(22,130,22,yk,G.ACC)+T(28,88,'10 m',anchor='start',size=11,bold=True,renk=G.ACC)
  +T(85,64,'sürtünmeli',size=10,anchor='start')+T(85,76,'(enerjinin %25’i ısıya)',size=10,anchor='start')
  +T(202,120,'sürtünme kuvveti 20 N',size=10)+T(202,108,'L → M',size=10))
mk(P,'0004',tipId='fz-en-surtunme',tip='Sürtünmeli yolda enerji dönüşümü',z='zor',alt='Enerji Dönüşümleri',kaz='Eğik yoldaki enerji kaybını ve yatay yoldaki sürtünme işini birlikte değerlendirir.',kalip='şekilli',adim=4,
 kart='K-FZEN-04 (sürtünmeli yol) · önce yüzde kayıp, sonra sabit sürtünme kuvveti',
 metin='Kütlesi 4 kg olan bir cisim, K noktasından serbest bırakılıyor. K–L eğik yolunda cismin ilk enerjisinin %25’i ısıya dönüşmektedir. Cisim L noktasından sonra yatay L–M yolunda 20 N’luk sabit sürtünme kuvvetinin etkisiyle M noktasında duruyor (şekil).\ng = 10 m/s² olduğuna göre L–M uzaklığı kaç m’dir?',
 sekil=sk,
 dogru=15,yan=[(5,'Eğik yolda ısıya dönen enerjiyi (100 J) L’deki kinetik enerji sanmış.','dikkat'),(20,'Eğik yoldaki kaybı hesaba katmamış; ilk enerjiyi (400 J) kullanmış.','dikkat'),(25,'Isıya dönen enerjiyi ilk enerjiye eklemiş (500 J).','islem'),(35,'İlk enerji ile L’deki kinetik enerjiyi toplamış (700 J).','islem')],
 istenen='L–M yatay yolunun uzunluğu (m).',
 ip=['L’deki kinetik enerji, yatay yolda sürtünme kuvvetinin yaptığı işle tükenir; önce L’deki kinetik enerjiyi bul.'],
 bilgi=[EP,B('Sürtünme işi','sürtünme kuvveti cismin enerjisini ısıya çevirir: W_sürt = F_s × x. Örnek: 5 N’luk sürtünme 4 m’de 20 J enerjiyi ısıya dönüştürür')],
 ad=[A('İlk enerji','Cisim K’de durgun; yalnız potansiyel enerjisi vardır.','E_K = 4 × 10 × 10 = 400 J'),A('Isıya dönen enerji','K–L yolunda ilk enerjinin %25’i ısı olur.','0,25 × 400 = 100 J'),A('L’deki kinetik enerji','Kalan enerji kinetik enerjidir.','E_L = 400 − 100 = 300 J'),A('Yatay yol','Kinetik enerjinin tamamı sürtünme işiyle tükenir.','F_s × x = 300 · 20 × x = 300 · x = 15 m')],
 puf='Önce eğik yoldaki kaybı çıkar, kalan kinetik enerjiyi sürtünme kuvvetine bölerek yolu bul: x = E_k ÷ F_s.')
bitir(P,'enerji','fiz|İş, Güç ve Enerji')
