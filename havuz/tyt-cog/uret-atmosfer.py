"""TYT Coğrafya · Atmosfer ve Sıcaklık: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_a import *
KY='ÖSYM 2018–2026 (atmosferin katmanları, sıcaklık dağılışı, izotermler) · MEB 9. sınıf coğrafya'
KARTLAR={
 'K-ATM-01':dict(alt='Atmosferin katmanları',fikir='Katmanların özellikleri (hava olayları, ozon, iyonosfer) sıralanıp doğru katman bulunur.',tuzak='Hava olayı ile ozonun katmanlarını karıştırmak.',zorluk='kolay',kalip='düz',adim=2,tipId='cg-atm-katman',kaynak=KY),
 'K-ATM-02':dict(alt='Yükselti ve sıcaklık',fikir='Verilen azalma oranı yükselti farkıyla çarpılıp sıcaklık farkı bulunur.',tuzak='İki yükseltiyi toplamak ya da deniz seviyesinden başlamak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='cg-atm-yukselti',kaynak=KY),
 'K-ATM-03':dict(alt='Sıcaklığı etkileyen etkenler',fikir='Aynı enlemde sıcaklık farkını yükselti, kara-deniz dağılışı ve akıntılar açıklar; geliş açısı sabittir.',tuzak='Aynı enlemde ışın açısını farklı sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='cg-atm-etken',kaynak=KY),
 'K-ATM-04':dict(alt='İzoterm haritası',fikir='Eş sıcaklık eğrileri arasında kalan yerlerin değer aralığından en az/en çok fark çıkarılır.',tuzak='Komşu eğriler arasındaki noktaları hep yakın sıcaklıkta saymak.',zorluk='zor',kalip='şekilli',adim=4,tipId='cg-atm-izoterm',kaynak=KY),
}
TIPLER={'cg-atm-katman':'Atmosfer katmanlarının özellikleri','cg-atm-yukselti':'Yükselti ve sıcaklık hesabı','cg-atm-etken':'Sıcaklığı etkileyen etkenler','cg-atm-izoterm':'İzoterm haritası yorumu'}
Q=Konu('atmosfer','Atmosfer ve Sıcaklık','cog|Atmosfer ve Sıcaklık',4,KARTLAR,TIPLER,{'kolay':1,'orta':2,'zor':1})

# 0001 kolay · C
Q.soru('0001','K-ATM-01','kolay','Atmosfer katmanlarını özelliklerine göre ayırt eder.',2,'düz',
 'Ozon tabakasının bulunduğu, hava olaylarının görülmediği ve Güneş’ten gelen zararlı morötesi ışınların büyük bölümünü soğuran atmosfer katmanı aşağıdakilerden hangisidir?',
 [('Troposfer','tropo','Hava olayları troposferde görülür; soruda hava olaylarının görülmediği belirtiliyor.','dikkat'),
  ('Mezosfer','mezo','Mezosfer atmosferin en soğuk katmanıdır ve gök taşları burada yanar; ozon tabakası bu katmanda değildir.','bilgi'),
  ('Stratosfer','strato','',''),
  ('Termosfer','termo','Termosferde sıcaklık çok yüksektir ve iyonosfer burada yer alır; ozon tabakası bu katmanda değildir.','bilgi'),
  ('Ekzosfer','ekzo','Ekzosfer atmosferin en dış katmanıdır; gazlar burada uzaya karışır, ozon tabakası bulunmaz.','bilgi')],
 'C',lambda t:t=='strato','Verilen özelliklere sahip atmosfer katmanı.',
 'Yerden yukarıya katmanların sırasını düşün; ozon hangi katmandadır?',
 [B('Atmosferin katmanları (yerden yukarıya)','troposfer: hava olayları, sıcaklık yükseldikçe azalır · stratosfer: ozon tabakası · mezosfer: gök taşları yanar · termosfer: iyonosfer · ekzosfer: gazların uzaya karıştığı en dış katman')],
 [A('Verilenleri ayır','Üç ipucu var: ozon, hava olayı olmaması ve morötesi ışınların soğurulması.','ozon + hava olayı yok'),
  A('Katmanları sına','Hava olayları troposferdedir. Mezosfer, termosfer ve ekzosferde ozon yoktur.','troposfer, mezosfer, termosfer, ekzosfer: uymuyor'),
  A('Sonucu bul','Ozon tabakası stratosferdedir ve burada hava olayı görülmez.','stratosfer')],
 'Ozon denince stratosferi, hava olayı denince troposferi hatırla.')

# 0002 orta · D
h1,t1,h2=400,18,1600
sonuc=t1-(h2-h1)//200; assert sonuc==12
yanlis={'6':t1-(h2-h1)//100,'8':t1-(h1+h2)//200,'10':t1-h2//200,'24':t1+(h2-h1)//200}
assert yanlis=={'6':6,'8':8,'10':10,'24':24}
Q.soru('0002','K-ATM-02','orta','Yükselti farkından sıcaklık değişimini hesaplar.',3,'hikâyeli',
 'Troposferde yükseldikçe sıcaklığın her 200 metrede 1 °C azaldığı kabul edilmektedir.\nYükseltisi 400 metre olan K kasabasında sıcaklık 18 °C ölçüldüğü anda, yükseltisi 1600 metre olan L kasabasında sıcaklığın kaç °C olması beklenir?',
 [('6','6','Yükselti farkını her 100 metrede 1 °C düşüyormuş gibi hesaplamış (1200 ÷ 100 = 12 °C azalma).','islem'),
  ('8','8','K’nin yükseltisini de L’ye eklemiş: (400 + 1600) ÷ 200 = 10 °C düşmüş olur.','islem'),
  ('10','10','K’nin 400 metresini çıkarmadan 1600 ÷ 200 = 8 °C azalma bulmuş (18 − 8 = 10).','dikkat'),
  ('12','12','',''),
  ('24','24','L, K’den yüksek olduğu için sıcaklık azalır; azalmayı eklemiş (18 + 6).','dikkat')],
 'D',lambda t:t=='12','L kasabasında beklenen sıcaklık (°C).',
 'Önce iki kasaba arasındaki yükselti farkını bul.',
 [B('Yükselti ve sıcaklık','troposferde yükseldikçe sıcaklık azalır · her 200 m’de 1 °C azalıyorsa 1000 m’de 5 °C azalır (1000 ÷ 200 = 5)')],
 [A('Yükselti farkını bul','İki kasaba arasındaki fark, yüksek yükseltiden alçak yükselti çıkarılarak bulunur.','1600 − 400 = 1200 m'),
  A('Düşüşü hesapla','Her 200 metrede 1 °C azalıyor. Kaç tane 200 metre olduğu sayılır.','1200 ÷ 200 = 6 → 6 °C azalır'),
  A('Sıcaklığı bul','L daha yüksek olduğundan K’den soğuktur.','18 − 6 = 12 °C')],
 'Sıcaklık değişimi için her zaman iki yükselti arasındaki farkı kullan, tek yükseltiyi değil.')

# 0003 orta · A
Q.oncul('0003','K-ATM-03','orta','Aynı enlemde sıcaklık farkına yol açan etkenleri ayırt eder.',3,
 'Aynı enlem üzerinde bulunan iki yerin yıllık ortalama sıcaklıkları farklı ölçülmüştür.',
 [('İki yer arasındaki yükselti farkı',True,'Yükseldikçe sıcaklık azalır; yükseltisi farklı yerlerin sıcaklığı farklı olur.'),
  ('Güneş ışınlarının yere düşme açısındaki fark',False,'Aynı enlemde Güneş ışınlarının geliş açısı aynıdır; bu fark yaratmaz.'),
  ('Kıyıdan geçen sıcak ya da soğuk deniz akıntıları',True,'Sıcak akıntı geçen kıyı ısınır, soğuk akıntı geçen kıyı soğur.')],
 'Bu durumun nedeni olarak yukarıdakilerden hangileri gösterilebilir?',
 ['I ve III','Yalnız I','Yalnız II','I ve II','II ve III'],'A',True,'Sıcaklık farkının nedeni olabilecek etkenler.',
 'Aynı enlemde hangi etken zaten aynıdır?',
 [B('Sıcaklığı etkileyen etkenler','enlem (ışınların geliş açısı) · yükselti · kara-deniz dağılışı · okyanus akıntıları · bakı · bitki örtüsü'),B('Aynı enlem','Güneş ışınları aynı açıyla geldiği için enlemin etkisi eşit olur; fark başka etkenden doğar')],
 [A('Sabit olanı bul','İki yer aynı enlemde olduğundan ışınların geliş açısı eşittir.','geliş açısı: aynı → II hariç'),
  A('Farklılaşanları ayır','Yükselti ve deniz akıntıları yerden yere değişebilir ve sıcaklığı etkiler.','I: evet · III: evet'),
  A('Sonuç','Gösterilebilecek nedenler I ve III.','I ve III')],
 'Aynı enlemde sıcaklık farkı soruluyorsa geliş açısını elemeden başla.')

# 0004 zor · E (izoterm)
class Iv:
    def __init__(s,lo,hi,lo_o=False,hi_o=False): s.lo,s.hi,s.lo_o,s.hi_o=lo,hi,lo_o,hi_o
PT={'K':Iv(20,20),'L':Iv(15,20,True,True),'M':Iv(10,10),'N':Iv(20,25,True,True),'P':Iv(10,15,True,True)}
def kesin_az(a,b,esik):
    c=[(a.hi-b.lo,not(a.hi_o or b.lo_o)),(b.hi-a.lo,not(b.hi_o or a.lo_o))]
    sup=max(v for v,_ in c); att=any(x for v,x in c if v==sup)
    return sup<esik or (sup==esik and not att)
def yaz_cift(p): return ''.join(p)
cifler=[('L','P'),('K','M'),('M','N'),('N','P'),('K','L')]
assert [kesin_az(PT[a],PT[b],5) for a,b in cifler]==[False,False,False,False,True]
import math
def egri(deger,x): return {25:52,20:90,15:128,10:166}[deger]+7*math.sin(x/42)
def yol(deger): return 'M20 %.1f '%egri(deger,20)+' '.join('L%d %.1f'%(x,egri(deger,x)) for x in range(30,301,10))
b=[]
for d in (25,20,15,10):
    b.append(f'<path d="{yol(d)}" stroke-width="1.8" fill="none"/>'+G._t(318,egri(d,300)+4,f'{d} °C',anchor='start',size=11,bold=True))
def nokta(ad,x,y,dx=7,dy=-7): return f'<circle cx="{x}" cy="{y:.1f}" r="4" style="fill:{G.ACC};stroke:none"/>'+G._t(x+dx,y+dy,ad,anchor='start',size=13,bold=True)
b.append(nokta('K',70,egri(20,70)))
b.append(nokta('L',190,(egri(15,190)+egri(20,190))/2))
b.append(nokta('M',255,egri(10,255)))
b.append(nokta('N',105,(egri(20,105)+egri(25,105))/2))
b.append(nokta('P',150,(egri(10,150)+egri(15,150))/2))
b.append(G._t(170,16,'Deniz seviyesine indirgenmiş izoterm haritası',size=11))
SK=G._svg(360,200,''.join(b))
opts=[]
cels={('L','P'):('L noktası 15–20 °C, P noktası 10–15 °C arasında kalır; ikisi de bu aralıklarda herhangi bir değer alabilir. Fark 0’a da 10’a da yaklaşabilir.','bilgi'),
      ('K','M'):('K 20 °C, M 10 °C’lik eğri üzerindedir; fark tam 10 °C’dir, 5 °C’den azdır denemez.','islem'),
      ('M','N'):('N 20 °C’den sıcaktır (20–25 arası), M 10 °C’dir; fark 10 °C’den büyüktür.','islem'),
      ('N','P'):('N 20 °C’den sıcak, P 15 °C’den soğuktur; fark en az 5 °C’den büyüktür, azdır denemez.','dikkat')}
for a,b_ in cifler:
    opts.append((f'{a} – {b_}',(a,b_),cels.get((a,b_),('',''))[0],cels.get((a,b_),('',''))[1]))
Q.soru('0004','K-ATM-04','zor','İzoterm haritasında iki yer arasındaki sıcaklık farkını aralıklarla değerlendirir.',4,'şekilli',
 'Şekilde, bir bölgenin deniz seviyesine indirgenmiş izoterm haritası verilmiştir. K ve M noktaları, 20 °C ve 10 °C’lik izoterm eğrileri üzerindedir; L, N ve P noktaları ise iki izoterm arasındadır.\nBuna göre, hangi iki noktanın sıcaklıkları arasındaki fark kesinlikle 5 °C’den azdır?',
 opts,'E',lambda t:kesin_az(PT[t[0]],PT[t[1]],5),'Sıcaklık farkı kesinlikle 5 °C’den az olan iki nokta.',
 'Her noktanın sıcaklığının hangi iki değer arasında olduğunu yaz.',
 [B('İzoterm','sıcaklığı eşit olan yerleri birleştiren eğridir (ör. 20 °C’lik izoterm üzerindeki her yer 20 °C’dir) · iki izoterm arasındaki yer, bu iki değerin arasında bir sıcaklığa sahiptir')],
 [A('Aralıkları yaz','Eğri üzerindeki yerin değeri kesindir; iki eğri arasındaki yerin değeri aralıkta kalır.','K = 20 · M = 10 · L: 15–20 · N: 20–25 · P: 10–15'),
  A('En büyük farkı bul','İki noktanın farkı en çok, birinin en yüksek ve diğerinin en düşük değerinde olur.','K–L: fark < 20 − 15 = 5'),
  A('Diğer çiftleri sına','L–P arası 0 ile 10 arasında değişebilir. K–M tam 10, M–N 10’dan büyük, N–P 5’ten büyüktür.','L–P: belirsiz · K–M: 10 · M–N: >10 · N–P: >5'),
  A('Sonucu bul','Yalnız K–L çiftinde fark her durumda 5 °C’den küçüktür.','K – L')],
 'Kesinlik soruluyorsa her noktanın değer aralığını yazıp en uç farkı hesapla.',sekil=SK)
Q.bitir()
