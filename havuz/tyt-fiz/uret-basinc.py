import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif as H
from _hafif import *
H.KONU='Basınç'
KONU='Basınç'
P=Parti('basinc','Basınç','fiz|Basınç',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (basınç) · MEB 10. sınıf'
kart('K-FZBS-01','Katı basıncı','P = F ÷ A; aynı cisim farklı yüzleri üzerinde durunca kuvvet sabit, alan değişir.','Yanlış yüzün alanını almak; cm²’yi m²’ye çevirmemek; g’yi atlamak.','kolay','şekilli',2,'fz-bs-kati','Katı basıncı',KY)
kart('K-FZBS-02','Sıvı basıncı','Üst üste karışmayan sıvılarda taban basıncı, her katmanın d × g × h değerlerinin toplamıdır.','Tüm sıvıyı tek özkütleli saymak; yalnız bir katmanı hesaba katmak.','orta','şekilli',3,'fz-bs-sivi','Katmanlı sıvıda taban basıncı',KY)
kart('K-FZBS-03','Hidrolik sistem','Pascal prensibi: P₁ = P₂ olduğundan F₁ ÷ A₁ = F₂ ÷ A₂; alan yarıçapın karesiyle orantılıdır.','Yarıçap oranını alan oranı sanmak.','orta','şekilli',3,'fz-bs-hidrolik','Hidrolik pres',KY)
kart('K-FZBS-04','Üst üste küpler','Her yüzeydeki basınç, o yüzeye bastıran toplam ağırlığın o yüzeyin alanına bölümüdür.','Zemin basıncında üstteki cismin ağırlığını katmamak; alanları karıştırmak.','zor','şekilli',4,'fz-bs-yigin','Üst üste konulan cisimlerde basınç',KY)
KATI=B('Katı basıncı','P = F ÷ A; yatay zeminde F cismin ağırlığıdır (G = m × g). 1 cm² = 10⁻⁴ m². Örnek: 20 N ağırlık, 0,005 m² alana basarsa P = 20 ÷ 0,005 = 4000 Pa')
SIVI=B('Sıvı basıncı','P = d × g × h; h sıvının yüzeyden olan derinliğidir. Örnek: d = 1000 kg/m³, h = 0,2 m, g = 10 için P = 1000 × 10 × 0,2 = 2000 Pa')
# ---- 0001
def kutu(x0,yb,w,h,dx,dy,lw,lh,ld,zemin=True):
    o=[Rc(x0,yb-h,w,h,0.18),
       f'<path d="M{x0} {yb-h} L{x0+dx} {yb-h-dy} L{x0+w+dx} {yb-h-dy} L{x0+w} {yb-h} Z" stroke-width="2" style="fill:currentColor;fill-opacity:.08"/>',
       f'<path d="M{x0+w} {yb-h} L{x0+w+dx} {yb-h-dy} L{x0+w+dx} {yb-dy} L{x0+w} {yb} Z" stroke-width="2" style="fill:currentColor;fill-opacity:.28"/>']
    if lw: o.append(T(x0+w/2,yb+15,lw,size=11,bold=True))
    if lh: o.append(T(x0+w+dx+6,yb-h/2-dy/2+4,lh,anchor='start',size=11,bold=True))
    if ld: o.append(T(x0+w+dx/2-4,yb-h-dy-4,ld,anchor='start',size=11,bold=True))
    return ''.join(o)
m=6; g=10; Al=Fr(10*20,10**4); Pz=Fr(m*g)/Al
assert Al==Fr(2,100) and Pz==3000 and Fr(60)/Fr(20*30,10**4)==1000 and Fr(60)/Fr(10*30,10**4)==2000 and Fr(60)/Al/10==300 and Fr(60)/2==30
sk=svg(260,160,L(10,135,250,135,2)+kutu(70,135,70,105,28,18,'20 cm','30 cm','10 cm'))
mk(P,'0001',tipId='fz-bs-kati',tip='Katı basıncı',z='kolay',alt='Katı Basıncı',kaz='Cismin zemine uyguladığı basıncı ağırlık ve temas alanından hesaplar.',kalip='şekilli',adim=2,
 kart='K-FZBS-01 (katı basıncı) · dikdörtgenler prizması, ayrıtlar 10–20–30 cm',
 metin='Kütlesi 6 kg olan homojen bir blok, ayrıtları şekilde verilen konumda yatay zemin üzerinde durmaktadır.\ng = 10 m/s² olduğuna göre bloğun zemine uyguladığı basınç kaç Pa’dır?',
 sekil=sk,
 dogru=3000,yan=[(1000,'Zemine değen yüzü 20 cm × 30 cm sanıp alanı 600 cm² almış.','dikkat'),(2000,'Zemine değen yüzü 10 cm × 30 cm sanıp alanı 300 cm² almış.','dikkat'),(300,'Ağırlık yerine kütleyi (6) kullanmış; g ile çarpmayı atlamış.','islem'),(30,'200 cm²’yi 2 m² almış; cm²’yi m²’ye yanlış çevirmiş.','islem')],
 istenen='Bloğun zemine uyguladığı basınç (Pa).',
 ip=['Zemine değen yüzün hangi ayrıtlardan oluştuğuna şekilden bak; yükseklik temas alanına girmez.'],
 bilgi=[KATI],
 ad=[A('Temas alanı','Blok 20 cm × 10 cm’lik yüzü üzerinde durmaktadır; 1 cm² = 10⁻⁴ m².','A = 20 × 10 = 200 cm² = 0,02 m²'),A('Ağırlık','Yatay zeminde zemine uygulanan kuvvet ağırlıktır.','F = 6 × 10 = 60 N'),A('Basınç','Kuvvet alana bölünür.','P = 60 ÷ 0,02 = 3000 Pa')],
 puf='Katı basıncında önce zemine değen yüzü, sonra alanı metrekareye çevirerek bul.')
# ---- 0002
hx,hy,dx,dy,g=Fr(25,100),Fr(10,100),800,1200,10
Pt=dx*g*hx+dy*g*hy; assert dx*g*hx==2000 and dy*g*hy==1200 and Pt==3200 and dx*g*(hx+hy)==2800 and dy*g*(hx+hy)==4200
sk=svg(250,170,Rc(70,30,100,125,0.0)+Rc(70,30,100,78,0.10)+Rc(70,108,100,47,0.30)+T(120,70,'X',bold=True)+T(120,136,'Y',bold=True)
  +ok(55,108,55,30,G.ACC)+ok(55,30,55,108,G.ACC)+T(50,72,'25 cm',anchor='end',size=11,bold=True,renk=G.ACC)
  +ok(55,155,55,108,G.ACC)+ok(55,108,55,155,G.ACC)+T(50,135,'10 cm',anchor='end',size=11,bold=True,renk=G.ACC)
  +T(178,72,'d_X = 800',anchor='start',size=11)+T(178,136,'d_Y = 1200',anchor='start',size=11)+T(178,150,'kg/m³',anchor='start',size=10))
mk(P,'0002',tipId='fz-bs-sivi',tip='Katmanlı sıvıda taban basıncı',z='orta',alt='Sıvı Basıncı',kaz='Birbirine karışmayan iki sıvının kap tabanında oluşturduğu basıncı hesaplar.',kalip='şekilli',adim=3,
 kart='K-FZBS-02 (sıvı basıncı) · iki katmanlı karışmayan sıvı',
 metin='Birbirine karışmayan X ve Y sıvıları şekildeki kapta dengededir. X sıvısının özkütlesi 800 kg/m³ ve yüksekliği 25 cm, Y sıvısının özkütlesi 1200 kg/m³ ve yüksekliği 10 cm’dir.\nAçık hava basıncı ihmal edildiğine ve g = 10 m/s² olduğuna göre kabın tabanındaki sıvı basıncı kaç Pa’dır?',
 sekil=sk,
 dogru=3200,yan=[(1200,'Yalnız alttaki Y sıvısının basıncını hesaplamış.','dikkat'),(2000,'Yalnız üstteki X sıvısının basıncını hesaplamış.','dikkat'),(2800,'Tüm 35 cm’lik sıvıyı X’in özkütlesiyle hesaplamış.','bilgi'),(4200,'Tüm 35 cm’lik sıvıyı Y’nin özkütlesiyle hesaplamış.','bilgi')],
 istenen='Kabın tabanındaki sıvı basıncı (Pa).',
 ip=['Tabandaki basınç, iki sıvı katmanının basınçlarının toplamıdır; her katman kendi özkütlesi ve yüksekliğiyle hesaplanır.'],
 bilgi=[SIVI],
 ad=[A('X katmanı','Yükseklik 25 cm = 0,25 m.','P_X = 800 × 10 × 0,25 = 2000 Pa'),A('Y katmanı','Yükseklik 10 cm = 0,1 m.','P_Y = 1200 × 10 × 0,1 = 1200 Pa'),A('Toplam','Katmanların basınçları toplanır.','P = 2000 + 1200 = 3200 Pa')],
 puf='Karışmayan sıvılarda taban basıncı, her katman için d × g × h hesaplanıp toplanarak bulunur.')
# ---- 0003
r1,r2,F2=2,10,2500; ar=Fr(r2**2,r1**2); F1=Fr(F2)/ar
assert ar==25 and F1==100 and Fr(F2)/Fr(r2,r1)==500 and F2*Fr(r2,r1)==12500 and F2*ar==62500
sk=svg(300,175,
  '<path d="M40 80 L64 80 L64 120 L140 120 L140 80 L260 80 L260 140 L40 140 Z" stroke="none" style="fill:currentColor;fill-opacity:.13"/>'
  +L(40,50,40,140,2)+L(64,50,64,120,2)+L(140,50,140,120,2)+L(260,50,260,140,2)+L(40,140,260,140,2)+L(64,120,140,120,2)
  +Rc(42,72,20,8,0.3)+Rc(142,72,116,8,0.3)
  +Rc(165,44,70,28,0.18)+T(200,62,'yük 2500 N',size=10,bold=True)
  +ok(52,22,52,70,G.ACC)+T(52,16,'F₁',bold=True,renk=G.ACC)
  +T(52,162,'r₁ = 2 cm',size=11,bold=True)+T(200,162,'r₂ = 10 cm',size=11,bold=True))
mk(P,'0003',tipId='fz-bs-hidrolik',tip='Hidrolik pres',z='orta',alt='Pascal Prensibi',kaz='Hidrolik sistemde piston yarıçaplarından alan oranını bulup kuvvet dengesini kurar.',kalip='şekilli',adim=3,
 kart='K-FZBS-03 (hidrolik sistem) · yarıçap verilmiş, yük dengelenir',
 metin='Şekildeki hidrolik sistemde sıvı dolu bağlantılı iki silindirik kabın, aynı yatay seviyedeki pistonlarının yarıçapları 2 cm ve 10 cm’dir. Büyük pistonun üzerine ağırlığı 2500 N olan bir yük konulmuştur. Pistonların ağırlıkları ve sürtünmeler ihmal edilmektedir.\nSistem dengede kalması için küçük pistona uygulanması gereken F₁ kuvveti kaç N olmalıdır?',
 sekil=sk,
 dogru=100,yan=[(500,'Alan oranı yerine yarıçap oranını (5) kullanmış.','bilgi'),(2500,'Kuvvetlerin eşit olması gerektiğini sanmış.','bilgi'),(12500,'Yarıçap oranıyla (5) çarpmış.','islem'),(62500,'Küçük pistondaki kuvveti büyük olması gerekir sanıp alan oranıyla (25) çarpmış.','islem')],
 istenen='Küçük pistona uygulanması gereken kuvvet (N).',
 ip=['Her iki pistonun sıvıya yaptığı basınç eşittir; piston alanı yarıçapın karesiyle orantılıdır.'],
 bilgi=[B('Pascal prensibi','kapalı kaptaki sıvıya uygulanan basınç her yöne aynen iletilir; F₁ ÷ A₁ = F₂ ÷ A₂. Dairesel pistonda A = π × r². Örnek: yarıçap 3 katına çıkarsa alan 9 katına çıkar')],
 ad=[A('Alan oranı','Alan yarıçapın karesiyle orantılıdır.','A₂ ÷ A₁ = (10 ÷ 2)² = 25'),A('Basınç eşitliği','İki pistonun altındaki basınç eşit olmalıdır.','F₁ ÷ A₁ = 2500 ÷ A₂'),A('Sonuç','F₁ çekilir.','F₁ = 2500 ÷ 25 = 100 N')],
 puf='Hidrolik sistemde kuvvet oranı alan oranına, alan oranı da yarıçap oranının karesine eşittir.')
# ---- 0004
ma,mb=2,12; g=10; Pz=Fr((ma+mb)*g)/Fr(20*20,10**4); Pa=Fr(ma*g)/Fr(10*10,10**4)
assert Pz==3500 and Pa==2000 and Pz/Pa==Fr(7,4) and Pa/Pz==Fr(4,7) and Fr(mb*g)/Fr(20*20,10**4)/Pa==Fr(3,2) and Fr((ma+mb)*g)/Fr(500,10**4)/Pa==Fr(7,5) and Fr((ma+mb)*g,ma*g)==7
sk=svg(260,190,L(30,170,230,170,2)+Rc(70,70,100,100,0.18)+Rc(95,20,50,50,0.35,2,True)+T(120,50,'K',bold=True)+T(120,125,'L',bold=True)
  +T(120,185,'20 cm',size=11,bold=True)+T(150,48,'10 cm',anchor='start',size=11,bold=True)+T(178,98,'m_K = 2 kg',anchor='start',size=10)+T(178,115,'m_L = 12 kg',anchor='start',size=10))
mk(P,'0004',tipId='fz-bs-yigin',tip='Üst üste konulan cisimlerde basınç',z='zor',alt='Katı Basıncı',kaz='Üst üste duran cisimlerde farklı yüzeylerdeki basınçları karşılaştırır.',kalip='şekilli',adim=4,
 kart='K-FZBS-04 (üst üste küpler) · iki farklı yüzeydeki basınç oranı',
 metin='Ayrıtı 10 cm olan homojen K küpü, ayrıtı 20 cm olan homojen L küpünün üst yüzeyinin tam ortasına gelecek biçimde şekildeki gibi yatay zemin üzerinde durmaktadır. K’nin kütlesi 2 kg, L’nin kütlesi 12 kg’dır.\ng = 10 m/s² olduğuna göre L’nin zemine yaptığı basıncın, K’nin L’nin üst yüzeyine yaptığı basınca oranı kaçtır?',
 sekil=sk,
 dogru='7/4',sira=['4/7','7/5','3/2','7/4','7'],yan=[('4/7','Oranı ters kurmuş: K’nin basıncını zemindeki basınca bölmüş.','dikkat'),('7/5','Zemindeki basıncı hesaplarken iki küpün alanlarını toplayıp (500 cm²) kullanmış.','bilgi'),('3/2','Zemindeki basınçta K’nin ağırlığını katmamış.','dikkat'),('7','Alanları hesaba katmadan yalnız ağırlıklar oranını (140 N ÷ 20 N) almış.','bilgi')],
 istenen='P_zemin ÷ P_K oranı.',
 ip=['Zemine bastıran toplam ağırlık ile K’nin bastığı yüzeyin alanı farklıdır; iki basıncı ayrı ayrı hesapla.'],
 bilgi=[KATI,B('Alan','kenarı a olan karenin alanı a × a’dır. Örnek: 20 cm ayrıtlı küpün tabanı 20 × 20 = 400 cm² = 0,04 m²')],
 ad=[A('Zemindeki basınç','Zemine L ve K’nin toplam ağırlığı bastırır; temas alanı L’nin tabanıdır (0,04 m²).','F = (2 + 12) × 10 = 140 N · P_zemin = 140 ÷ 0,04 = 3500 Pa'),A('K’nin yaptığı basınç','L’nin üst yüzeyine yalnız K’nin ağırlığı bastırır; temas alanı K’nin tabanıdır (0,01 m²).','F = 2 × 10 = 20 N · P_K = 20 ÷ 0,01 = 2000 Pa'),A('Oran','İki basınç bölünür.','3500 ÷ 2000 = 7/4')],
 puf='Üst üste cisimlerde her yüzey için “o yüzeye bastıran toplam ağırlık ÷ o yüzeyin temas alanı” hesabı ayrı yapılır.')
bitir(P,'basinc','fiz|Basınç')
