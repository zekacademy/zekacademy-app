"""TYT Coğrafya · Dünya’nın Şekli ve Hareketleri: 4 ana soru (hafif mod)."""
import sys,os,math
from datetime import datetime,timedelta
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_a import *
KY='ÖSYM 2018–2026 (Dünya’nın hareketleri, yerel saat, Güneş ışınları) · MEB 9. sınıf coğrafya'
KARTLAR={
 'K-DNH-01':dict(alt='Günlük ve yıllık hareketin sonuçları',fikir='Gece-gündüz, yerel saat farkı ve sapma günlük hareketin; mevsimler ve gündüz süresinin değişimi yıllık hareketin sonucudur.',tuzak='Gece-gündüz süresinin değişmesini günlük harekete bağlamak.',zorluk='kolay',kalip='düz',adim=2,tipId='cg-dnh-sonuc',kaynak=KY),
 'K-DNH-02':dict(alt='Güneş ışınlarının geliş açısı',fikir='Öğle vakti geliş açısı = 90° − (enlem ile Güneş’in dik düştüğü paralel arasındaki fark).',tuzak='Dönenceyi unutmak ya da enlemle toplamak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='cg-dnh-aci',kaynak=KY),
 'K-DNH-03':dict(alt='Gündüz süresi',fikir='21 Haziran’da Kuzey Yarım Küre’de gündüzler uzundur, Güney’de kısadır; kutup dairelerinde uç durumlar görülür.',tuzak='Güney Yarım Küre’yi Kuzey ile aynı saymak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='cg-dnh-gunduz',kaynak=KY),
 'K-DNH-04':dict(alt='Yerel saat ve tarih değiştirme çizgisi',fikir='Boylam farkı × 4 dk saat farkını verir; 180° meridyeni geçilirken tarih değişir.',tuzak='Boylam farkını 340° yerine 20° almak, tarihi unutmak.',zorluk='zor',kalip='yeni nesil',adim=5,tipId='cg-dnh-saat',kaynak=KY),
}
TIPLER={'cg-dnh-sonuc':'Günlük hareketin sonuçları','cg-dnh-aci':'Güneş ışınlarının geliş açısı','cg-dnh-gunduz':'Gündüz süresi (21 Haziran)','cg-dnh-saat':'Yerel saat ve tarih çizgisi'}
Q=Konu('dunyahareket','Dünya’nın Şekli ve Hareketleri','cog|Dünya’nın Şekli ve Hareketleri',4,KARTLAR,TIPLER,{'kolay':1,'orta':2,'zor':1})

# 0001 kolay · B
Q.soru('0001','K-DNH-01','kolay','Dünya’nın günlük hareketinin sonuçlarını yıllık hareketin sonuçlarından ayırır.',2,'düz',
 'Aşağıdakilerden hangisi Dünya’nın kendi ekseni etrafındaki dönüşünün (günlük hareketin) sonuçlarından biridir?',
 [('Mevsimlerin oluşması','yillik','Mevsimler Dünya’nın Güneş etrafındaki dolanımı ve eksen eğikliğinin sonucudur; yıllık harekete bağlıdır.','bilgi'),
  ('Gece ile gündüzün oluşması','gunluk','',''),
  ('Gece ve gündüz sürelerinin yıl boyunca değişmesi','yillik','Süre farkları eksen eğikliği ve yıllık hareketle ilgilidir; günlük hareket yalnızca gece-gündüzü doğurur.','bilgi'),
  ('Kutup bölgelerinde altı ay süren gece ve gündüz','yillik','Bu durum eksen eğikliğiyle yıllık hareketin birleşmesinden doğar.','dikkat'),
  ('Güneş ışınlarının geliş açısının yıl boyunca değişmesi','yillik','Geliş açısının yıl içinde değişmesi yıllık hareketin sonucudur.','bilgi')],
 'B',lambda t:t=='gunluk','Günlük hareketin sonucu.',
 'Dünya’nın kendi çevresinde dönmesi 24 saatte bir tur sürer; hangi olay her gün tekrar eder?',
 [B('Günlük hareket (dönme)','Dünya’nın kendi ekseni etrafında dönmesi, 24 saat sürer · sonuçları: gece-gündüz oluşumu, yerel saat farkları, rüzgâr ve akıntıların sapması'),B('Yıllık hareket (dolanma)','Güneş etrafındaki dolanım, 365 gün 6 saat sürer · sonuçları: mevsimler, gece-gündüz sürelerinin değişmesi, ışınların geliş açısının değişmesi')],
 [A('Hareketleri ayır','Dönme günlük, dolanma yıllık harekettir. Her harekete ait sonuçlar farklıdır.','dönme: günlük · dolanma: yıllık'),
  A('Şıkları sınıflandır','Mevsimler, süre değişimi, altı aylık gece-gündüz ve geliş açısı değişimi yıllık harekete bağlıdır.','A, C, D, E: yıllık'),
  A('Sonuç','Yalnız gece ile gündüzün oluşması günlük harekete bağlıdır.','B: günlük')],
 'Her gün tekrar eden olay günlük harekete, yıl boyunca değişen olay yıllık harekete aittir.')

# 0002 orta · E (dakika cinsinden hesap)
def dm(d,m=0): return d*60+m
DEK=dm(23,27); LAT=dm(40)
acı=lambda a: dm(90)-abs(LAT-a)
def yaz(a): return f"{a//60}°{a%60:02d}’" if a%60 else f"{a//60}°"
assert yaz(acı(DEK))=='73°27’'
yan=[acı(DEK)]  # doğru
dog=acı(DEK); hat={'hatali1':acı(0),'hatali2':dm(90)-(LAT+DEK),'hatali3':dm(90)-DEK,'hatali4':LAT-DEK}
assert hat=={'hatali1':dm(50),'hatali2':dm(26,33),'hatali3':dm(66,33),'hatali4':dm(16,33)}
opts=[(yaz(hat['hatali4']),hat['hatali4'],'Enlem ile dönence arasındaki farkı (40° − 23°27’) geliş açısı sanmış; bu fark 90°’den çıkarılmalıdır.','islem'),
 (yaz(hat['hatali2']),hat['hatali2'],'Enlem ile dönenceyi toplayıp (40° + 23°27’ = 63°27’) 90°’den çıkarmış (90° − 63°27’ = 26°33’); oysa dönence ile K aynı yarım kürededir, fark alınmalıdır.','islem'),
 (yaz(hat['hatali1']),hat['hatali1'],'Güneş ışınlarının dönenceye dik geldiğini unutup ekvatora dik geliyormuş gibi hesaplamış (90° − 40°).','dikkat'),
 (yaz(hat['hatali3']),hat['hatali3'],'Yalnız dönenceyi kullanmış (90° − 23°27’); K’nin enlemini hesaba katmamış.','bilgi'),
 (yaz(dog),dog,'','')]
Q.soru('0002','K-DNH-02','orta','Güneş ışınlarının öğle vakti geliş açısını hesaplar.',3,'hikâyeli',
 '21 Haziran’da öğle vakti Güneş ışınları 23°27’ Kuzey paralelinde yere dik (90°) olarak düşer.\nBu tarihte, 40° Kuzey enleminde bulunan bir K şehrine öğle vakti Güneş ışınlarının geliş açısı kaç derecedir?',
 opts,'E',lambda t:t==dog,'K şehrinde öğle vakti ışınların geliş açısı.',
 'Güneş ışınlarının dik geldiği paralel ile K’nin enlemi arasındaki farkı bul.',
 [B('Geliş açısı','öğle vakti Güneş ışınlarının yere düşme açısı = 90° − (enlem ile ışınların dik düştüğü paralel arasındaki fark) · 1° = 60’ (dakika)'),B('Örnek','Işınlar 20° K’ye dik düşerken 35° K’de açı: 90° − (35° − 20°) = 75°')],
 [A('Enlem farkını bul','K, dik düşen paralelin kuzeyindedir; fark çıkarılarak bulunur.','40° − 23°27’ = 16°33’'),
  A('Açıyı hesapla','Dik açıdan (90°) enlem farkı çıkarılır.','90° − 16°33’ = 73°27’'),
  A('Doğrula','Işınların dik düştüğü yere yaklaştıkça açı 90°’ye yaklaşır; 73°27’ makul bir değerdir.','73°27’ < 90°')],
 'Geliş açısı = 90° − (enlem farkı); fark, ışınların dik düştüğü paralele göre hesaplanır.')

# 0003 orta · D
def gunduz(lat,dec=23.44):
    c=-math.tan(math.radians(lat))*math.tan(math.radians(dec))
    if c>=1: return 0.0
    if c<=-1: return 24.0
    return 2*math.degrees(math.acos(c))/15
assert gunduz(40)>12 and gunduz(-40)<12 and gunduz(-70)==0
Q.oncul('0003','K-DNH-03','orta','21 Haziran’da farklı enlemlerde gündüz süresini yorumlar.',3,
 '21 Haziran tarihinde Güneş ışınları öğle vakti Yengeç Dönencesi’ne (23°27’ K) dik düşer.',
 [('40° Kuzey enleminde gündüz süresi 12 saatten uzundur.',gunduz(40)>12,'Güneş ışınları kuzey yarım küreye daha dik gelir; gündüzler uzundur.'),
  ('40° Güney enleminde gündüz süresi 12 saatten uzundur.',gunduz(-40)>12,'Güney Yarım Küre’de bu tarih kıştır; gündüzler 12 saatten kısadır.'),
  ('70° Güney enleminde Güneş gün boyunca doğmaz.',gunduz(-70)==0,'Güney Kutup Dairesi’nin (66°33’G) güneyinde bu tarihte gece kesintisiz sürer.')],
 'Yukarıdaki ifadelerden hangileri doğrudur?',
 ['Yalnız I','Yalnız II','Yalnız III','I ve III','II ve III'],'D',True,'Doğru ifadeler.',
 'Haziran’da Güney Yarım Küre’de mevsim nedir? Gündüz süresi uzar mı kısalır mı?',
 [B('21 Haziran','Güneş ışınları Yengeç Dönencesi’ne (23°27’K) dik gelir · Kuzey Yarım Küre’de yaz: gündüzler uzun · Güney Yarım Küre’de kış: gündüzler kısa · Güney Kutup Dairesi’nin güneyinde gün boyu gece')],
 [A('Işınların konumunu bul','Işınlar kuzeye (23°27’K) dik düştüğü için kuzey yarım küre daha çok ısınır.','kuzey: yaz · güney: kış'),
  A('Gündüz sürelerini yorumla','Yazın gündüz uzun, kışın kısadır. Kutup dairesi ötesinde gün boyu gece vardır.','40°K: uzun · 40°G: kısa · 70°G: gece'),
  A('İfadeleri sına','I ve III doğrudur. II’de güneyde gündüz uzun denmiş; yanlıştır.','I: doğru · II: yanlış · III: doğru')],
 'Haziran’da Kuzey’i yaz, Güney’i kış say; gündüz süreleri buna göre uzar ya da kısalır.')

# 0004 zor · A
t0=datetime(2025,3,21,2,0)
dlon=(180-170)+(180-170); dak=dlon*4; assert dak==80
L_dog=t0+timedelta(minutes=dak)-timedelta(days=1)       # doğuya giderken tarih çizgisi geçilir: bir gün geri
assert L_dog==datetime(2025,3,20,3,20)
fark=(170-(-170))*4  # UTC farkı K–L (dakika)
assert t0-timedelta(minutes=fark)==L_dog
def f(t): return f"{t.day} Mart {t:%H:%M}"
H={'dog':L_dog,'h1':t0-timedelta(minutes=80),'h2':datetime(2025,3,21,3,20),'h3':t0+timedelta(minutes=fark),'h4':t0-timedelta(hours=22)}
assert [f(H[k]) for k in ('dog','h1','h2','h3','h4')]==['20 Mart 03:20','21 Mart 00:40','21 Mart 03:20','22 Mart 00:40','20 Mart 04:00']
Q.soru('0004','K-DNH-04','zor','Tarih değiştirme çizgisini geçen iki yer arasında yerel saat ve tarih farkını bulur.',5,'yeni nesil',
 'K noktası 170° Doğu, L noktası 170° Batı boylamındadır. Yerel saatler esas alınmaktadır ve 180° meridyeni tarih değiştirme çizgisidir.\nK noktasında 21 Mart günü saat 02:00 iken L noktasında tarih ve saat aşağıdakilerden hangisidir?',
 [(f(H['dog']),'dog','',''),
  (f(H['h1']),'h1','Boylam farkını 340° yerine 20° alıp L’yi geride saymış (02:00 − 1 saat 20 dakika); tarih çizgisini de hesaba katmamış.','dikkat'),
  (f(H['h2']),'h2','Saati doğru bulmuş (03:20) ama doğuya giderken tarih çizgisi geçildiği halde tarihi bir gün geri almamış.','dikkat'),
  (f(H['h3']),'h3','Doğu-batı yönünü ters yorumlayıp 22 saat 40 dakika eklemiş.','bilgi'),
  (f(H['h4']),'h4','340° ÷ 15 = 22,67 saati 22 saate yuvarlamış; 40 dakikayı atlamış.','islem')],
 'A',lambda t:t=='dog','L noktasındaki tarih ve saat.',
 'K’den L’ye doğuya giderken 180° meridyeninden geçildiğini unutma.',
 [B('Saat farkı','1° boylam = 4 dakika (ör. 15° = 60 dakika = 1 saat) · doğuya gidildikçe saat ileri, batıya gidildikçe geri alınır'),B('Tarih değiştirme çizgisi','180° meridyenidir · doğuya doğru geçilirse tarih bir gün geri alınır, batıya doğru geçilirse bir gün ileri alınır')],
 [A('Boylam farkını bul','170° D ile 170° B arasında 180° meridyeni var. K’den doğuya gidince L’ye 10° + 10° = 20° ile ulaşılır.','(180 − 170) + (180 − 170) = 20°'),
  A('Saat farkını hesapla','Her derece 4 dakikadır. L, K’nin doğusunda olduğundan saati ileridir.','20 × 4 = 80 dk = 1 saat 20 dk'),
  A('Saati uygula','K’deki 02:00’ye 1 saat 20 dakika eklenir.','02:00 + 1:20 = 03:20'),
  A('Tarihi düzelt','K’den L’ye doğuya giderken tarih değiştirme çizgisi geçilir; tarih bir gün geri alınır.','21 Mart → 20 Mart'),
  A('Sonucu yaz','L noktasında tarih 20 Mart, saat 03:20’dir.','20 Mart 03:20')],
 'Çizgiyi geçiyorsan önce yakın yoldan boylam farkını al, sonra tarihi düzelt.')
Q.bitir()
