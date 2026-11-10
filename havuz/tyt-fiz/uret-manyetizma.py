import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif as H
from _hafif import *
H.KONU='Manyetizma'
P=Parti('manyetizma','Manyetizma','fiz|Manyetizma',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (manyetizma) · MEB 10. ve 11. sınıf'
kart('K-FZMN-01','Mıknatıs özellikleri','Aynı kutuplar iter; alan çizgilerinin sık olduğu yerde alan güçlüdür; mıknatıs bölünse de her parça iki kutupludur.','Mıknatısın bölününce tek kutuplu parçalar verdiğini sanmak.','kolay','öncüllü',2,'fz-mn-ozellik','Mıknatısın özellikleri',KY)
kart('K-FZMN-02','Pusula ve çubuk mıknatıs','Manyetik alan çizgileri mıknatısın dışında N’den S’ye doğrudur; pusula iğnesinin N ucu alanın yönünü gösterir.','Alan yönünü S’den N’ye sanmak; her noktada aynı yönü göstermesini beklemek.','orta','şekilli',3,'fz-mn-pusula','Pusula iğnesinin yönü',KY)
kart('K-FZMN-03','Akım taşıyan düz tel','Sağ el kuralı: başparmak akım yönünü, kıvrılan parmaklar alanın yönünü gösterir; alan çizgileri tel etrafında halkadır.','Alanı tele dik (radyal) sanmak; sağ el kuralında yönü ters uygulamak.','orta','şekilli',3,'fz-mn-duztel','Düz telin manyetik alanı',KY)
kart('K-FZMN-04','Elektromıknatıs','Elektromıknatısın gücü akım şiddeti, sarım sayısı ve demir çekirdekle artar; kutup yönü akımla değişir ama çekme özelliği kalır.','Pil ters çevrilince mıknatıs özelliğinin kaybolduğunu sanmak.','zor','öncüllü',4,'fz-mn-elektromiknatis','Elektromıknatısın gücü',KY)
S6=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
# ---- 0001
mk(P,'0001',tipId='fz-mn-ozellik',tip='Mıknatısın özellikleri',z='kolay',alt='Mıknatıs ve Manyetik Alan',kaz='Mıknatısın kutupları ve manyetik alan çizgileri hakkındaki bilgileri değerlendirir.',kalip='öncüllü',adim=2,
 kart='K-FZMN-01 (mıknatıs özellikleri) · öncüllü genel bilgi',
 metin='Çubuk mıknatıslarla ilgili;\nI. Aynı cins kutuplar birbirini iter.\nII. Manyetik alan çizgilerinin sık olduğu bölgede alan şiddeti daha büyüktür.\nIII. Çubuk mıknatıs ortasından kırılırsa parçalardan biri yalnız N, diğeri yalnız S kutbuna sahip olur.\nifadelerinden hangileri doğrudur?',
 dogru='I ve II',sira=S6,yan=[('Yalnız I','Alan çizgilerinin sıklığı ile alan şiddeti arasındaki ilişkiyi (II) bilmiyor.','bilgi'),('Yalnız II','Aynı cins kutupların birbirini ittiğini (I) bilmiyor.','bilgi'),('I ve III','Mıknatıs bölününce her parçada yeni N ve S kutupları oluştuğunu bilmiyor; III yanlıştır.','bilgi'),('II ve III','Mıknatısın tek kutuplu parçalara ayrılabileceğini sanmış; I’i de atlamış.','bilgi')],
 istenen='Doğru ifadelerin hangileri olduğu.',
 ip=['Bir mıknatıs kırıldığında oluşan her parçanın kutuplarını düşün; N ve S kutuplar hep birlikte bulunur.'],
 bilgi=[B('Mıknatıs ve alan çizgileri','aynı cins kutuplar iter, farklı cins kutuplar çeker; alan çizgileri sık olan yerde alan güçlüdür. Mıknatıs kırılınca her parça yine N ve S kutbu olan bir mıknatıs olur. Örnek: 10 cm’lik mıknatıs ikiye bölününce iki tane 5 cm’lik mıknatıs olur')],
 ad=[A('I’i değerlendir','Aynı cins kutuplar birbirini iter; farklı cinsler çeker.','I doğru'),A('II’yi değerlendir','Alan çizgilerinin sık olduğu yerde alan şiddeti büyüktür (kutuplara yakın).','II doğru'),A('III’ü değerlendir','Mıknatıs kırılınca her parça kendi N ve S kutbunu oluşturur; tek kutuplu parça yoktur.','III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')],
 puf='Mıknatısın tek kutbu olmaz: ne kadar küçük parçalara bölünse de her parçada N ve S birlikte bulunur.')
# ---- 0002 pusula
mx0,mx1,my0,my1=90,210,72,98
mg=svg(300,130,Rc(mx0,my0,(mx1-mx0)/2,my1-my0,0.0,2)+Rc((mx0+mx1)/2,my0,(mx1-mx0)/2,my1-my0,0.35,2)+T((mx0*3+mx1)/4,my1-9,'S',bold=True)+T((mx0+mx1*3)/4,my1-9,'N',bold=True)
  +f'<circle cx="255" cy="85" r="9" stroke-width="1.6"/>'+T(255,108,'X',bold=True)+T(255,70,'',size=2)
  +f'<circle cx="150" cy="30" r="9" stroke-width="1.6"/>'+T(172,34,'Y',anchor='start',bold=True))
mk(P,'0002',tipId='fz-mn-pusula',tip='Pusula iğnesinin yönü',z='orta',alt='Mıknatıs ve Manyetik Alan',kaz='Çubuk mıknatısın çevresindeki noktalarda pusula iğnesinin yönünü manyetik alan çizgilerine göre belirler.',kalip='şekilli',adim=3,
 kart='K-FZMN-02 (pusula ve çubuk mıknatıs) · eksen üzerindeki ve orta üstündeki noktalar',
 metin='Kutupları şekilde gösterilen çubuk mıknatısın N kutbunun sağındaki X noktasına ve mıknatısın tam ortasının üstündeki Y noktasına küçük birer pusula iğnesi konuyor.\nYer’in manyetik alanı ihmal edildiğine göre iğnelerin N uçları X ve Y noktalarında hangi yönü gösterir?',
 sekil=mg,
 dogru='X: →, Y: ←',sira=['X: →, Y: ←','X: →, Y: →','X: ←, Y: ←','X: ←, Y: →','X: ↑, Y: ←'],yan=[('X: →, Y: →','Y’de alan çizgilerinin N kutbunun yönünde (sağa) olduğunu sanmış; mıknatısın dışında alan N’den S’ye doğrudur.','bilgi'),('X: ←, Y: ←','X’te pusula N ucunun mıknatısın N kutbuna doğru döneceğini sanmış; aynı cins kutuplar iter.','bilgi'),('X: ←, Y: →','Alan yönünü her iki noktada da ters (S’den N’ye) almış.','bilgi'),('X: ↑, Y: ←','X noktasında alan çizgisinin eksene dik olduğunu sanmış; eksen üzerinde alan eksen doğrultusundadır.','dikkat')],
 istenen='X ve Y’deki pusula iğnelerinin N uçlarının gösterdiği yönler.',
 ip=['Manyetik alan çizgileri mıknatısın dışında N kutbundan çıkıp S kutbuna girer; pusula iğnesinin N ucu çizginin yönünü gösterir.'],
 bilgi=[B('Alan yönü ve pusula','manyetik alan çizgileri mıknatısın dışında N’den S’ye, içinde S’den N’ye doğrudur. Pusula iğnesinin N ucu bulunduğu noktadaki alan yönünü gösterir. Örnek: N kutbundan uzakta, eksen üzerinde iğnenin N ucu N kutbundan uzağı gösterir')],
 ad=[A('X noktası','X, N kutbunun sağında eksen üzerindedir; alan çizgisi N’den dışarı doğrudur.','iğnenin N ucu →'),A('Y noktası','Mıknatısın dışında alan N’den S’ye doğrudur; ortanın üstünde bu yön sağdan sola doğrudur.','iğnenin N ucu ←'),A('Sonuç','İki yön birleştirilir.','X: →, Y: ←')],
 puf='Pusula iğnesinin N ucu hep o noktadaki alan çizgisini izler; mıknatısın dışında bu yön N kutbundan S kutbuna doğrudur.')
# ---- 0003 düz tel
tel=svg(300,150,f'<circle cx="150" cy="80" r="13" stroke-width="2"/><circle cx="150" cy="80" r="3.5" style="fill:currentColor;stroke:none"/>'
  +f'<circle cx="150" cy="80" r="40" stroke-width="1" stroke-dasharray="3 4" opacity=".35"/>'
  +f'<circle cx="230" cy="80" r="9" stroke-width="1.6"/>'+T(230,104,'K',bold=True)+f'<circle cx="150" cy="22" r="9" stroke-width="1.6"/>'+T(172,26,'L',anchor='start',bold=True)
  +T(150,140,'Akım sayfa düzleminden dışarıya doğru (⊙)',size=11))
mk(P,'0003',tipId='fz-mn-duztel',tip='Düz telin manyetik alanı',z='orta',alt='Akım ve Manyetik Alan',kaz='Akım taşıyan düz telin çevresindeki manyetik alanın yönünü sağ el kuralıyla bulur.',kalip='şekilli',adim=3,
 kart='K-FZMN-03 (akım taşıyan düz tel) · sayfaya dik tel, iki nokta',
 metin='Sayfa düzlemine dik, uzun bir telden sayfa düzleminden dışarıya doğru akım geçmektedir. Telin sağındaki K noktasına ve üstündeki L noktasına küçük birer pusula iğnesi konuyor (şekil).\nYer’in manyetik alanı ihmal edildiğine göre iğnelerin N uçları K ve L noktalarında sayfa düzleminde hangi yönü gösterir?',
 sekil=tel,
 dogru='K: ↑, L: ←',sira=['K: ↓, L: →','K: ↑, L: →','K: ↓, L: ←','K: →, L: ↑','K: ↑, L: ←'],yan=[('K: ↓, L: →','Akımı sayfaya girer gibi düşünüp sağ el kuralını ters uygulamış.','bilgi'),('K: ↑, L: →','K’de doğru bulmuş; L’de alanın yönünü ters almış.','islem'),('K: ↓, L: ←','L’de doğru bulmuş; K’de alanın yönünü ters almış.','islem'),('K: →, L: ↑','Alan çizgilerini telden dışarı doğru (radyal) sanmış; oysa tel etrafında halkalar oluşturur.','bilgi')],
 istenen='K ve L’deki pusula iğnelerinin N uçlarının gösterdiği yönler.',
 ip=['Başparmağın akım yönünü (okuyucuya doğru) gösterdiği sağ elin kıvrılan parmakları alan yönünü verir.'],
 bilgi=[B('Sağ el kuralı','sağ elin başparmağı akım yönünü gösterirse kıvrılan dört parmak telin çevresindeki alan yönünü gösterir; alan çizgileri tele dik düzlemde halkadır. Örnek: akım sayfadan dışarıya ise alan, sayfaya bakınca saat yönünün tersindedir')],
 ad=[A('Alanın dönüş yönü','Akım dışarıya doğru: başparmak okuyucuya bakar, parmaklar saat yönünün tersine kıvrılır.','alan çizgileri saat yönünün tersine'),A('K noktası','Telin sağında saat yönünün tersindeki teğet yukarıdır.','K: ↑'),A('L noktası','Telin üstünde saat yönünün tersindeki teğet soldur.','L: ←')],
 puf='Alan çizgileri akım taşıyan telin çevresinde halkadır; pusula iğnesi halkanın o noktadaki teğetini gösterir.')
# ---- 0004 elektromıknatıs
S4=['I ve III','I ve IV','II ve IV','I, III ve IV','II, III ve IV']
mk(P,'0004',tipId='fz-mn-elektromiknatis',tip='Elektromıknatısın gücü',z='orta',alt='Akım ve Manyetik Alan',kaz='Elektromıknatısın gücünü etkileyen etkenleri akım, sarım sayısı ve çekirdek yönünden değerlendirir.',kalip='öncüllü',adim=4,
 kart='K-FZMN-04 (elektromıknatıs) · reosta, pil yönü, sarım ve çekirdek',
 metin='İç direnci önemsiz bir pil, bir reosta ve demir çekirdekli bir bobin seri bağlanarak masadaki çivileri çeken bir elektromıknatıs yapılıyor.\nI. Reostanın direnci artırılırsa çekilen çivi sayısı azalır.\nII. Pilin kutupları ters çevrilirse elektromıknatıs çivileri çekemez.\nIII. Akım şiddeti sabit tutulup sarım sayısı artırılırsa çekilen çivi sayısı artar.\nIV. Demir çekirdek aynı boyutta bir plastik çubukla değiştirilirse çekilen çivi sayısı azalır.\nifadelerinden hangileri doğrudur?',
 dogru='I, III ve IV',sira=S4,yan=[('I ve III','IV’ü yanlış sanmış; demir çekirdeğin alanı güçlendirdiğini bilmiyor.','bilgi'),('I ve IV','III’ü yanlış sanmış; sarım sayısının alanı artırdığını atlamış.','bilgi'),('II ve IV','Direnç artınca akımın azalacağını (I) ve sarım etkisini (III) kaçırmış; II’yi doğru sanmış.','bilgi'),('II, III ve IV','Pil ters çevrilince mıknatıslığın kaybolduğunu sanmış; yalnız kutuplar yer değiştirir, çiviler yine çekilir.','bilgi')],
 istenen='Doğru ifadelerin hangileri olduğu.',
 ip=['Elektromıknatısın gücünü artıran üç etkeni düşün: akım şiddeti, sarım sayısı, demir çekirdek; pil ters çevrilince yalnız kutuplar yer değiştirir.'],
 bilgi=[B('Elektromıknatıs','bobinden akım geçince manyetik alan oluşur; akım şiddeti ve sarım sayısı arttıkça, bobine demir çekirdek konunca alan güçlenir. Akım yönü değişince N ve S kutupları yer değiştirir. Örnek: akım iki katına çıkarsa çivileri çekme gücü artar')],
 ad=[A('I','Gerilim sabit; direnç artarsa akım azalır, alan zayıflar.','I doğru'),A('II','Akım yönü değişince yalnız kutuplar yer değiştirir; demir çiviler her iki kutupta da çekilir.','II yanlış'),A('III','Akım sabitken sarım sayısı arttıkça manyetik alan güçlenir.','III doğru'),A('IV','Demir çekirdek alanı güçlendirir; plastik çubuk alanı güçlendirmez, çekilen çivi azalır.','IV doğru · Sonuç: I, III ve IV')],
 puf='Elektromıknatısın gücü akımla, sarım sayısıyla ve demir çekirdekle artar; pil ters çevrilince yalnız kutup yönü değişir.')
bitir(P,'manyetizma','fiz|Manyetizma')
