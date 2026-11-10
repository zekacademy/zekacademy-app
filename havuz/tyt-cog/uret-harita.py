import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_c import *
P=Parti('harita','Harita Bilgisi','cog|Harita Bilgisi',ders='TYT Coğrafya',idon='tytcog')
KY='ÖSYM 2018–2026 TYT Coğrafya (harita okuryazarlığı) · MEB 9. sınıf'
kart('K-CGHR-01','Ölçek ve uzunluk','Haritadaki uzaklık × ölçek paydası = gerçek uzaklık; santimetre kilometreye çevrilir.','Sıfırları yanlış atmak; ölçek paydasını yanlış okumak.','kolay','düz',2,'cg-harita-olcek','Ölçekten gerçek uzaklık hesabı',KY)
kart('K-CGHR-02','Harita projeksiyonları','Silindir, konik ve düzlem projeksiyonların uygun kullanım alanları ve bozulma yönü.','Konik ile düzlem projeksiyonun uygun kullanım alanlarını karıştırmak.','orta','düz',3,'cg-harita-proj','Projeksiyon türleri ve bozulma',KY)
kart('K-CGHR-03','Eş yükselti ve eğim','Eğim (%) = yükselti farkı × 100 ÷ yatay uzaklık; yatay uzaklık ölçekle bulunur.','Yükselti farkını yanlış okumak; metre ve santimetreyi karıştırmak.','orta','şekilli',3,'cg-harita-egim','Eş yükselti eğrisinden eğim hesabı',KY)
kart('K-CGHR-04','Ölçek ve alan','Alan, uzunluğun karesiyle değiştiğinden alan oranı ölçek oranının karesidir.','Alan oranını uzunluk oranıyla aynı sanmak.','zor','düz',4,'cg-harita-alan','Ölçek değişince alanın değişimi',KY)
OLC=B('Ölçek','Kesir ölçek 1/50.000: haritada 1 cm, gerçekte 50.000 cm = 500 m’dir. Gerçek uzaklık = harita uzaklığı × payda. 100.000 cm = 1 km')
PRO=B('Projeksiyon','Küre yüzeyi düzleme aktarılırken bozulma kaçınılmazdır. Silindir: Ekvator çevresi iyi, kutuplara doğru bozulma artar · Konik: orta enlemlerdeki ülkeler · Düzlem: kutup bölgeleri')
EGM=B('Eğim','Eş yükselti eğrileri aynı yükseltideki noktaları birleştirir. Eğim (%) = yükselti farkı × 100 ÷ yatay uzaklık. Örnek: 1000 m’de 100 m yükselen yamaç %10 eğimlidir')
ALN=B('Ölçek ve alan','Uzunluklar k kat küçülürse alanlar k² kat küçülür. Örnek: ölçek paydası 2 kat artarsa harita üzerindeki alan 4 kat azalır')
# 0001
gercek=Fr(45,10)*2_000_000/100_000; assert gercek==90
key=lambda s:float(s.replace(',','.'))
Q(P,'0001','K-CGHR-01','kolay','Kesir ölçekten gerçek uzaklığı hesaplar.','düz',2,
 'Ölçeği 1/2.000.000 olan bir haritada iki kent arasındaki uzaklık 4,5 cm ölçülmüştür.\nBuna göre bu iki kent arasındaki gerçek uzaklık kaç km’dir?',
 [('90','d',None,None),('9','y','Santimetreyi kilometreye çevirirken bir sıfır fazla atmak.','islem'),('45','y','Ölçeği 1/1.000.000 sanmak.','dikkat'),('180','y','Haritadaki uzaklığı iki katı (9 cm) almak.','dikkat'),('900','y','Santimetreyi kilometreye çevirirken bir sıfırı atlamak.','islem')],
 lambda e:e=='d','İki kent arasındaki gerçek uzaklık (km).',
 'Haritadaki uzunluğu ölçek paydasıyla çarp, sonra cm’yi km’ye çevir.',[OLC],
 [A('Ölçeği oku','1/2.000.000: haritada 1 cm gerçekte 2.000.000 cm’dir.','1 cm → 2.000.000 cm'),
  A('Gerçek uzaklık','Haritadaki uzaklık ölçek paydasıyla çarpılır.','4,5 × 2.000.000 = 9.000.000 cm'),
  A('Km’ye çevir','100.000 cm = 1 km.','9.000.000 ÷ 100.000 = 90 km')],
 'Gerçek uzaklık cm cinsinden bulunur; kilometre için 5 sıfır atılır.','kesir ölçekten uzaklık',sirala=key,harf='C')
# 0002
Q(P,'0002','K-CGHR-02','orta','Harita projeksiyonlarının özelliklerini ve kullanım alanlarını bilir.','düz',3,
 'Harita projeksiyonları ile ilgili aşağıdakilerden hangisi doğrudur?',
 [('Konik projeksiyon, kutup bölgelerinin haritasını çizmek için en uygun yöntemdir.','y','Kutup bölgeleri için düzlem projeksiyon uygundur; konik projeksiyon orta enlemlerde kullanılır.','bilgi'),
  ('Silindir projeksiyonda bozulma, Ekvator’dan kutuplara doğru artar.','d',None,None),
  ('Düzlem projeksiyon, orta enlemlerdeki ülkelerin haritasını çizmek için en uygun yöntemdir.','y','Orta enlemler için konik projeksiyon uygundur; düzlem projeksiyon kutuplar içindir.','bilgi'),
  ('Silindir projeksiyonda Ekvator’dan uzaklaştıkça bozulma azalır.','y','Tersi doğrudur: silindir projeksiyonda bozulma Ekvator’dan kutuplara doğru artar.','dikkat'),
  ('Küre yüzeyini düzleme aktarırken hiçbir projeksiyonda bozulma olmaz.','y','Küre düzleme tam olarak açılamaz; her projeksiyonda bir miktar bozulma olur.','bilgi')],
 lambda e:e=='d','Doğru ifade.',
 'Her projeksiyonun hangi bölge için uygun olduğunu ve bozulmanın nerede arttığını hatırla.',[PRO],
 [A('Bilgiyi hatırla','Silindir: Ekvator çevresi, konik: orta enlemler, düzlem: kutuplar için uygundur.','silindir–Ekvator · konik–orta enlem · düzlem–kutup'),
  A('Şıkları sına','Konik ve düzlem için verilen kullanım alanları yer değiştirmiştir. Bozulmanın hiç olmadığı bir projeksiyon yoktur.','A, C, E: yanlış'),
  A('Bozulma yönü','Silindirde Ekvator’dan uzaklaştıkça bozulma artar.','B: doğru · D: yanlış')],
 'Silindir Ekvator’a, konik orta enlemlere, düzlem kutuplara uygundur.','projeksiyon ifadeleri',harf='B')
# 0003
yy=[100,200,300,400]; ab_cm=4; payda=25_000
yat=Fr(ab_cm*payda,100); eg=Fr(400-100)*100/yat
assert yat==1000 and eg==30 and Fr(100,1000)*100==10 and Fr(300*100,2000)==15 and Fr(300,1000)==Fr(3,10) and Fr(400*100,1000)==40
cx,cy=160,108
RR=(110,82,54,26); RY=tuple(round(r*0.64) for r in RR)
assert RY[0]==70
def elips(rx,ry): return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" stroke-width="1.8" style="fill:currentColor;fill-opacity:.05"/>'
body=''.join(elips(r,y) for r,y in zip(RR,RY))
body+=f'<line x1="{cx-RR[0]}" y1="{cy}" x2="{cx-RR[3]}" y2="{cy}" stroke-width="1.4" stroke-dasharray="4 3" style="stroke:{G.ACC}"/>'
for r,v,dx in zip(RR[:3],yy[:3],(14,14,15)): body+=T(cx-r+dx,cy+13,str(v),size=10)
body+=T(cx,cy+4,str(yy[3]),size=10)
body+=f'<circle cx="{cx-RR[0]}" cy="{cy}" r="4" style="fill:{G.ACC};stroke:{G.ACC}"/><circle cx="{cx-RR[3]}" cy="{cy}" r="4" style="fill:{G.ACC};stroke:{G.ACC}"/>'
body+=T(cx-RR[0]-9,cy+4,'A',anchor='end',bold=True,renk=G.ACC)+T(cx-RR[3]-4,cy-9,'B',bold=True,renk=G.ACC)+T(cx,14,'Eş yükselti eğrileri (m)',size=10)
sk=svg(320,208,body+T(cx,200,'Şekil ölçekli değildir',size=10))
Q(P,'0003','K-CGHR-03','orta','Eş yükselti haritasında iki nokta arasındaki eğimi hesaplar.','şekilli',3,
 'Ölçeği 1/25.000 olan bir haritada, eş yükselti eğrileri şekilde verilen tepe üzerindeki A ve B noktaları arasındaki doğrusal uzaklık 4 cm ölçülmüştür.\nBuna göre A ile B arasındaki ortalama eğim yüzde kaçtır?',
 [('30','d',None,None),('0,3','y','Eğim formülündeki 100 ile çarpmayı unutmak (300 ÷ 1000 = 0,3).','islem'),('10','y','Yükselti farkı yerine tek bir eğri aralığını (100 m) kullanmak.','dikkat'),('15','y','Ölçeği 1/50.000 alıp yatay uzaklığı 2 km bulmak.','dikkat'),('40','y','Yükselti farkı yerine B’nin yüksekliğini (400 m) almak.','dikkat')],
 lambda e:e=='d','A ile B arasındaki ortalama eğim (%).',
 'Şekilden A ve B’nin yüksekliğini oku, haritadaki uzaklığı ölçekle metreye çevir.',[OLC,EGM],
 [A('Yükselti farkı','A, 100 m’lik; B, 400 m’lik eğri üzerindedir.','400 − 100 = 300 m'),
  A('Yatay uzaklık','4 cm × 25.000 = 100.000 cm.','100.000 cm = 1000 m'),
  A('Eğimi bul','Eğim = yükselti farkı × 100 ÷ yatay uzaklık.','300 × 100 ÷ 1000 = %30')],
 'Eğimde önce yükselti farkını, sonra yatay uzaklığı metreye çevir.','eş yükselti şekli ve ölçek',sekil=sk,sirala=key,harf='D')
# 0004
a1=12; k=Fr(200_000,50_000); a2=Fr(a1)/k**2; assert a2==Fr(3,4)
assert Fr(a1)/k==3 and a1*k*k==192 and a1*k==48
Q(P,'0004','K-CGHR-04','zor','Ölçek değiştiğinde harita üzerindeki alanın nasıl değiştiğini hesaplar.','düz',4,
 '1/50.000 ölçekli bir haritada 12 cm² yer kaplayan bir göl, aynı gölü gösteren 1/200.000 ölçekli haritada kaç cm² yer kaplar?',
 [('0,75','d',None,None),('3','y','Alanı yalnız uzunluk oranıyla (4) bölmek; alan oranı 4² = 16’dır.','bilgi'),('12','y','Alanın ölçekten bağımsız olduğunu sanmak.','bilgi'),('48','y','Küçük ölçekte alanın büyüyeceğini sanıp 4 ile çarpmak.','dikkat'),('192','y','Alanı 16 ile çarpmak; ölçek küçüldüğünde alan azalır.','dikkat')],
 lambda e:e=='d','Gölün 1/200.000 ölçekli haritadaki alanı (cm²).',
 'Ölçek paydası 4 kat artınca uzunluklar 4 kat küçülür; alan için bunun karesini al.',[ALN,OLC],
 [A('Uzunluk oranı','Payda 50.000’den 200.000’e çıkar.','200.000 ÷ 50.000 = 4 kat küçülme'),
  A('Alan oranı','Alan, uzunluğun karesi gibi değişir.','4² = 16 kat küçülme'),
  A('Yeni alan','Eski alanı 16’ya böl.','12 ÷ 16 = 0,75 cm²')],
 'Ölçek k kat küçülürse harita üzerindeki alan k² kat küçülür.','alan–ölçek ilişkisi',sirala=key,harf='A')
bitir(P,'harita','cog|Harita Bilgisi','Harita Bilgisi')
