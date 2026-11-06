"""Hareket Hız Problemleri · parti 1 (8 ana + 8 kardeş). Her cevap ve çeldirici kodla yeniden hesaplanır."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('hareketprob','Hareket Hız Problemleri','prob|Hareket Hız Problemleri')
TT=lambda **k:k

def saat(h):
    h=Fr(h); m=(h-int(h))*60; assert m.denominator==1
    return f'{int(h):02d}.{int(m):02d}'
def virg(x):
    x=Fr(x); return str(x.numerator) if x.denominator==1 else f'{float(x):g}'.replace('.',',')
def sirali(s):
    v=[Fr(x.replace(',','.')) for x in s]; assert v==sorted(v) and len(set(v))==5, s
    return s

def yol(uclar,oklar=(),noktalar=(),olcu=(),L=1,alt=None):
    """Basit yol şeması. Konumlar 0..L. oklar: (konum, yön ±1, yazı); noktalar: (konum, yazı) vurgulu nokta;
    olcu: (a, b, yazı, satır) ölçü çizgisi."""
    W,x0,x1,y=330,26,304,52; b=[]; L=Fr(L)
    X=lambda v:x0+float(Fr(v)/L)*(x1-x0)
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke-width="3" stroke-linecap="round" opacity=".55"/>')
    for x,ad in ((x0,uclar[0]),(x1,uclar[1])):
        b.append(f'<circle cx="{x}" cy="{y}" r="5" style="fill:currentColor"/>'); b.append(G._t(x,y+20,ad,size=13,bold=True))
    for k,yon,s in oklar:
        x=X(k); xe=x+yon*30
        b.append(f'<path d="M{x:.1f} {y-12} H{xe:.1f} M{xe-yon*6:.1f} {y-17} L{xe:.1f} {y-12} L{xe-yon*6:.1f} {y-7}" stroke-width="2"/>')
        b.append(G._t(x-4 if yon>0 else x+4,y-22,s,anchor='start' if yon>0 else 'end',size=11))
    for n in noktalar:
        k,s=n[0],n[1]; ust=len(n)>2 and n[2]
        x=X(k); b.append(f'<circle cx="{x:.1f}" cy="{y}" r="6" style="fill:{G.ACC};stroke:{G.ACC}"/>')
        b.append(G._t(x,y-14 if ust else y+20,s,size=12,bold=True,renk=G.ACC))
    sat=0
    for a,c,s,r in olcu:
        yy=y+40+r*24; sat=max(sat,r+1); xa,xc=X(a),X(c)
        b.append(f'<path d="M{xa:.1f} {yy-5} V{yy+5} M{xc:.1f} {yy-5} V{yy+5} M{xa:.1f} {yy} H{xc:.1f}" stroke-width="1.4" style="stroke:{G.ACC}"/>')
        if xc>W-60 and xc-xa<60: b.append(G._t(xc,yy-7,s,anchor='end',size=11,bold=True))
        else: b.append(G._t((xa+xc)/2,yy-5,s,size=11,bold=True))
    h=y+30+sat*24+(22 if alt else 6)
    if alt: b.append(G._t(W/2,h-8,alt,size=11))
    return G._svg(W,h,''.join(b))

YOL=B('Yol, hız ve zaman','yol = hız × zaman. Örnek: saatte 60 km hızla 3 saatte 60 × 3 = 180 km gidilir')
KARS=B('Karşılaşma','birbirine doğru giden iki hareketli arasındaki yol her saat hızlarının toplamı kadar kısalır: süre = aradaki yol ÷ (v₁ + v₂)')
YET=B('Yetişme','aynı yönde giden iki hareketliden arkadaki, öndekine her saat hız farkı kadar yaklaşır: süre = aradaki yol ÷ (v₁ − v₂)')
ORT=B('Ortalama hız','ortalama hız = toplam yol ÷ toplam süre. Hızların ortalaması değildir: 2 saat 60 km/sa, 1 saat 90 km/sa ⇒ (120 + 90) ÷ 3 = 70')
DAK=B('Dakika ve saat','1 saat = 60 dakika. Örnek: 30 dakika = 1/2 saat · 15 dakika = 1/4 saat · 40 dakika = 2/3 saat')
PIST=B('Dairesel pist','aynı yönde koşanlar, hızlı olan bir tur fazla attığında yan yana gelir (hız farkı); zıt yönde koşanlar, ikisinin toplam yolu bir tur olunca karşılaşır (hız toplamı)')

# ===================== 0001 karşılaşma KOLAY
d,v1,v2=420,60,80; t=Fr(d,v1+v2); assert t==3 and v1*t+v2*t==d
s=sirali([saat(9+t),saat(9+Fr(d,2)/v1),saat(9+Fr(d,v2)),saat(9+Fr(d,(v1+v2)/Fr(2))),saat(9+Fr(d,v1))])
assert s==['12.00','12.30','14.15','15.00','16.00']
P.R('0001','hr-karsilasma','Karşılaşma (zıt yönlü hareket)','kolay','Karşılaşma','Birbirine doğru hareket eden iki aracın karşılaşma süresini hızlar toplamıyla bulur ve saate çevirir.','hikâyeli',2,
 'K-HR-01 (zıt yönlü hareket, hızlar toplamı) · yeni kurgu (iki otomobil), istenen: karşılaşma saati',
 'Aralarındaki yol 420 km olan A ve B kentlerinden saat 09.00’da iki otomobil birbirine doğru yola çıkıyor. A’dan çıkan otomobil saatte 60 km, B’den çıkan otomobil saatte 80 km sabit hızla gidiyor.\nBuna göre otomobiller saat kaçta karşılaşır?',
 s,'A','Otomobillerin karşılaştığı saat.',
 ['Otomobiller birbirine doğru gidiyor: aralarındaki yol her saat ne kadar kısalır?','420 km’yi bu “yaklaşma hızına” böl.','Bulduğun süreyi çıkış saatine ekle.'],[YOL,KARS],
 [A('Yaklaşma hızı','Birbirlerine doğru gittikleri için aradaki yol her saat iki hızın toplamı kadar kısalır.','60 + 80 = 140 km/sa'),
  A('Karşılaşma süresi','420 km’lik ara, saatte 140 km kapanır.','420 ÷ 140 = 3 saat · kontrol: 60 × 3 + 80 × 3 = 180 + 240 = 420',
    yol(('A','B'),[(0,1,'60 km/sa'),(420,-1,'80 km/sa')],[(180,'karşılaşma')],[(0,180,'180 km',0),(180,420,'240 km',0)],L=420)),
  A('Saati bul','Çıkış saatine 3 saat ekle.','09.00 + 3 saat = 12.00')],
 'Birbirine doğru giden iki araçta hızları topla; aradaki yolu bu toplama böl.',
 dict(B='12.30, yarı yolda (210 km) karşılaşacaklarını sanıp yavaş otomobilin süresini almak; hızlar farklı olduğu için orta noktada karşılaşmazlar.',
      C='14.15, yalnız hızlı otomobilin 420 km’yi gitmesini hesaplamak (5 saat 15 dakika); diğer otomobil de yaklaşıyor.',
      D='15.00, iki hızın ortalamasını (70) tek bir aracın hızı gibi kullanmak; yaklaşma hızı toplamdır.',
      E='16.00, yalnız yavaş otomobilin yolun tamamını gitmesini hesaplamak (7 saat).'),
 TT(B='bilgi',C='dikkat',D='bilgi',E='dikkat'))
d=(12+15)*2; assert d==54
s=sirali(['6','24','27','30','54'])
assert 3*2==6 and 12*2==24 and Fr(27,2)*2==27 and 15*2==30
P.K('0001','Bir bisiklet yolunun iki ucunda bulunan Selin ile Mert, saat 07.30’da birbirine doğru bisikletleriyle yola çıkıyor. Selin saatte 12 km, Mert saatte 15 km sabit hızla ilerliyor ve ikisi saat 09.30’da karşılaşıyor.\nBuna göre bisiklet yolunun uzunluğu kaç km’dir?',
 s,'E','Bisiklet yolunun uzunluğu.',
 ['Karşılaşana kadar kaç saat geçmiştir?','Bu sürede Selin ve Mert ayrı ayrı kaç km yol alır?','Karşılaştıklarında ikisinin aldığı yollar toplamı neye eşittir?'],[YOL,KARS],
 [A('Geçen süre','07.30’dan 09.30’a kadar geçen zaman.','09.30 − 07.30 = 2 saat'),
  A('Herkesin yolu','Her biri kendi hızıyla 2 saat ilerler.','Selin: 12 × 2 = 24 km · Mert: 15 × 2 = 30 km'),
  A('Yolun tamamı','Karşılaştıklarında iki yol birleşip bisiklet yolunu tamamlar.','24 + 30 = 54 km · ya da (12 + 15) × 2 = 54',
    yol(('Selin','Mert'),[(0,1,'12 km/sa'),(54,-1,'15 km/sa')],[(24,'09.30')],[(0,24,'24 km',0),(24,54,'30 km',0)],L=54))],
 'Karşılaşmada iki hareketlinin aldığı yolların toplamı aradaki yolun tamamıdır.',
 dict(A='6, hızların farkını (3) süreyle çarpmak; birbirine doğru gidenlerde hızlar toplanır.',B='24, yalnız Selin’in aldığı yol; Mert’in yolu eklenmemiş.',
      C='27, hızların ortalamasını (13,5) süreyle çarpmak; iki kişi birlikte yaklaşıyor.',D='30, yalnız Mert’in aldığı yol; Selin’in yolu eklenmemiş.'),
 TT(A='bilgi',B='dikkat',C='bilgi',D='dikkat'))

# ===================== 0002 ortalama KOLAY
yol_=2*70+3*90; assert yol_==410 and Fr(yol_,5)==82
assert Fr(2*70+90,5)==46 and Fr(3*70+2*90,5)==78 and Fr(70+90,2)==80
s=sirali(['46','78','80','82','410'])
P.R('0002','hr-ortalama','Ortalama hız','kolay','Ortalama hız','Parçalı bir yolculukta her parçanın yolunu bulup ortalama hızı toplam yol ÷ toplam süre ile hesaplar.','hikâyeli',2,
 'K-HR-03 (parçalı yolculukta ortalama hız) · yeni kurgu (otobüs), farklı süreli iki parça',
 'Bir otobüs, bir yolculuğun ilk 2 saatinde saatte 70 km, sonraki 3 saatinde saatte 90 km sabit hızla gitmiştir.\nBuna göre otobüsün bu yolculuktaki ortalama hızı saatte kaç km’dir?',
 s,'D','Yolculuğun tamamındaki ortalama hız.',
 ['Her bölümde kaç km yol alındığını ayrı ayrı bul.','Toplam yol ve toplam süre kaçtır?','Ortalama hız, hızların ortalaması mıdır?'],[YOL,ORT],
 [A('Birinci bölüm','2 saat boyunca saatte 70 km.','2 × 70 = 140 km'),
  A('İkinci bölüm','3 saat boyunca saatte 90 km.','3 × 90 = 270 km'),
  A('Ortalama hız','Toplam yolu toplam süreye böl.','140 + 270 = 410 km · 2 + 3 = 5 saat · 410 ÷ 5 = 82 km/sa')],
 'Ortalama hız her zaman toplam yol ÷ toplam süredir; daha uzun süre gidilen hız sonuca daha çok etki eder.',
 dict(A='46, ikinci bölümde 90 km yol alındığını sanmak (140 + 90 = 230, 230 ÷ 5); 90 hızdır, yol 3 × 90 = 270 km.',
      B='78, süreleri hızlara ters eşlemek (3 × 70 + 2 × 90); 70 km/sa ile 2 saat gidilmiş.',
      C='80, iki hızın aritmetik ortalaması; süreler farklı olduğu için ortalama hız toplam yol ÷ toplam süredir.',
      E='410, toplam yol (km); soru saatteki ortalama hızı soruyor.'),
 TT(A='islem',B='dikkat',C='bilgi',E='dikkat'))
assert Fr(48,24//12+24//6)==8 and Fr(12+6,2)==9 and Fr(48,4)==12
s=sirali(['8','9','12','18','24'])
P.K('0002','Elif, evinden 24 km uzaklıktaki göle bisikletiyle saatte 12 km sabit hızla gitmiş, aynı yoldan evine saatte 6 km sabit hızla dönmüştür.\nBuna göre Elif’in bu gidiş-dönüş yolculuğundaki ortalama hızı saatte kaç km’dir?',
 s,'A','Gidiş-dönüşün tamamındaki ortalama hız.',
 ['Gidiş ve dönüş ayrı ayrı kaç saat sürdü?','Gidiş-dönüşte toplam kaç km yol alındı?','Toplam yolu toplam süreye böl; hızların ortalamasını alma.'],[YOL,ORT],
 [A('Gidiş süresi','24 km saatte 12 km hızla.','24 ÷ 12 = 2 saat'),
  A('Dönüş süresi','Aynı 24 km saatte 6 km hızla.','24 ÷ 6 = 4 saat'),
  A('Ortalama hız','Toplam yol gidiş + dönüş.','24 + 24 = 48 km · 2 + 4 = 6 saat · 48 ÷ 6 = 8 km/sa')],
 'Gidiş-dönüşte yavaş bölüm daha uzun sürer; bu yüzden ortalama hız iki hızın ortalamasından küçük çıkar.',
 dict(B='9, iki hızın aritmetik ortalaması; dönüş daha uzun sürdüğü için ortalama hız toplam yol ÷ toplam süredir.',
      C='12, toplam yolu (48 km) yalnız dönüş süresine (4 saat) bölmek; gidiş süresi de eklenmeli.',
      D='18, iki hızı toplamak; ortalama hız toplam yol ÷ toplam süre ile bulunur.',
      E='24, göle olan uzaklık (km); soru saatteki ortalama hızı soruyor.'),
 TT(B='bilgi',C='dikkat',D='bilgi',E='dikkat'))

# ===================== 0003 yetişme ORTA
ond=Fr(3,2)*60; t=ond/(90-60); assert ond==90 and t==3 and 90*t==60*(Fr(3,2)+t)==270
s=sirali([saat(Fr(19,2)+Fr(90,150)),saat(8+t),saat(Fr(19,2)+Fr(60,30)),saat(Fr(19,2)+t),saat(Fr(19,2)+Fr(135,30))])
assert s==['10.06','11.00','11.30','12.30','14.00']
P.R('0003','hr-yetisme','Yetişme (aynı yönlü hareket)','orta','Yetişme','Önce çıkan aracın aldığı yolu bulur, hız farkıyla yetişme süresini hesaplar ve doğru saate ekler.','hikâyeli',3,
 'K-HR-02 (aynı yoldan farklı saatte çıkış) · yeni kurgu (kamyon ve otomobil), istenen: yetişme saati',
 'Bir kamyon saat 08.00’de A kentinden B kentine doğru saatte 60 km sabit hızla yola çıkıyor. Bir otomobil saat 09.30’da aynı yerden, aynı yolu izleyerek saatte 90 km sabit hızla kamyonun arkasından yola çıkıyor.\nOtomobil kamyona B kentine varmadan yetiştiğine göre otomobil kamyona saat kaçta yetişir?',
 s,'D','Otomobilin kamyona yetiştiği saat.',
 ['Otomobil yola çıktığında kamyon kaç km öndedir?','Aynı yönde giderken otomobil kamyona her saat kaç km yaklaşır?','Bulduğun süreyi hangi saate eklemelisin?'],[YOL,YET,DAK],
 [A('Kamyonun önü','08.00 ile 09.30 arasında kamyon 1,5 saat yol almıştır.','1,5 × 60 = 90 km',
    yol(('A','B'),[(0,1,'90 km/sa'),(90,1,'60 km/sa')],[(90,'kamyon, 09.30')],[(0,90,'90 km',0)],L=300,alt='09.30: otomobil A’da, kamyon 90 km önde')),
  A('Yaklaşma hızı','Aynı yönde gittikleri için otomobil her saat hız farkı kadar yaklaşır.','90 − 60 = 30 km/sa'),
  A('Yetişme süresi','90 km’lik fark saatte 30 km kapanır.','90 ÷ 30 = 3 saat'),
  A('Saati bul','Süre otomobilin çıkışından başlar.','09.30 + 3 saat = 12.30 · kontrol: 90 × 3 = 270 · 60 × 4,5 = 270')],
 'Yetişmede önce öndekinin aldığı yolu bul; süreyi geride kalanın çıkış saatine ekle.',
 dict(A='10.06, hızları toplamak (90 ÷ 150 saat); aynı yönde gidenlerde hız farkı kullanılır.',B='11.00, 3 saati kamyonun çıkış saatine (08.00) eklemek; süre otomobilin çıkışından başlar.',
      C='11.30, aradaki farkı 1 saat sanıp kamyonun önünü 60 km almak; 08.00’den 09.30’a 1,5 saat geçer.',E='14.00, kamyonun önündeki yolu otomobilin hızıyla (1,5 × 90 = 135) hesaplamak.'),
 TT(A='bilgi',B='dikkat',C='islem',E='islem'))
ond=6*Fr(40,60); t=ond/(18-6); assert ond==4 and t*60==20 and 18*t==6*(Fr(2,3)+t)
assert Fr(4,24)*60==10 and Fr(6,12)*60==30 and 20+40==60
s=sirali(['10','20','30','40','60'])
P.K('0003','Bir yaya, köy meydanından saatte 6 km sabit hızla yürümeye başlıyor. Yayadan 40 dakika sonra bir bisikletli, aynı yerden aynı yolu izleyerek saatte 18 km sabit hızla yola çıkıyor.\nBuna göre bisikletli, yola çıktıktan kaç dakika sonra yayaya yetişir?',
 s,'B','Bisikletlinin yola çıkışından yetişmeye kadar geçen dakika.',
 ['40 dakikayı saate çevir; bu sürede yaya kaç km yürür?','Bisikletli yayaya her saat kaç km yaklaşır?','Süreyi saat olarak bulup dakikaya çevir.'],[YOL,YET,DAK],
 [A('Yayanın önü','40 dakika = 2/3 saat.','6 × 2/3 = 4 km'),
  A('Yaklaşma hızı','Aynı yönde gidiyorlar; hız farkı kadar yaklaşma olur.','18 − 6 = 12 km/sa'),
  A('Yetişme süresi','4 km’lik fark saatte 12 km kapanır.','4 ÷ 12 = 1/3 saat'),
  A('Dakikaya çevir','1/3 saat = 60 ÷ 3 dakika.','20 dakika · kontrol: 18 × 1/3 = 6 km · 6 × 1 = 6 km')],
 'Önce süre farkını yola çevir, sonra hız farkına böl; birimleri (dakika–saat) en başta eşitle.',
 dict(A='10, hızları toplamak (4 ÷ 24 saat); aynı yönde gidenlerde hız farkı kullanılır.',C='30, 40 dakikayı 1 saat sanıp yayanın önünü 6 km almak.',
      D='40, iki kişinin çıkışları arasındaki süre; yetişme süresi değil.',E='60, süreyi yayanın çıkışından ölçmek (40 + 20); soru bisikletlinin çıkışından soruyor.'),
 TT(A='bilgi',C='islem',D='dikkat',E='dikkat'))

# ===================== 0004 hız-süre ORTA
sol=[(dd,Fr(dd,60)) for dd in range(1,2000) if Fr(dd,60)-Fr(dd,90)==2]; assert sol==[(360,6)]
cik=13-6; assert cik==7 and 11-Fr(360,90)==7
s=sirali(['05.00','06.00',saat(cik),'09.00','12.00'])
assert 11-6==5 and 13-Fr(360,90)==9 and 13-Fr(2*(90-60),60)==12
P.R('0004','hr-sure-hiz','Hız değişince süre ve yol','orta','Hız ve süre değişimi','Aynı yolu iki farklı hızla gitme sürelerinin farkından yolu, oradan da çıkış saatini bulur.','hikâyeli',3,
 'K-HR-04 (iki hızla iki varış saati) · yeni kurgu (kargo aracı), yeni istenen (çıkış saati)',
 'Bir kargo aracı depodan belirli bir saatte yola çıkıp bir müşteriye gidecektir. Araç saatte 60 km sabit hızla giderse saat 13.00’te, saatte 90 km sabit hızla giderse aynı gün saat 11.00’de müşteriye ulaşacaktır.\nBuna göre kargo aracı depodan saat kaçta yola çıkacaktır?',
 s,'C','Kargo aracının depodan çıkış saati.',
 ['İki durumda da yol ve çıkış saati aynıdır; varış saatleri arasındaki fark neyi gösterir?','Yolu x ile göster: 60 km/sa ve 90 km/sa ile süreler kaçtır?','Süre farkı denklemini kur, x’i bul; sonra varış saatinden süreyi çıkar.'],[YOL,B('Aynı yol, farklı hız','yol sabitse hız arttıkça süre azalır: süre = yol ÷ hız. Örnek: 180 km, 60 km/sa ile 3 saat, 90 km/sa ile 2 saat')],
 [A('Süre farkı','Çıkış saati aynı; varışlar arasında 13.00 − 11.00 kadar fark var.','x/60 − x/90 = 2'),
  A('Yolu bul','Paydaları 180’de eşitle.','3x/180 − 2x/180 = 2 ⇒ x/180 = 2 ⇒ x = 360 km'),
  A('Süre','60 km/sa ile 360 km.','360 ÷ 60 = 6 saat (90 km/sa ile 4 saat)'),
  A('Çıkış saati','Varış saatinden süreyi çıkar.','13.00 − 6 saat = 07.00 · kontrol: 11.00 − 4 saat = 07.00')],
 'Aynı yol iki hızla gidiliyorsa süre farkından yolu bul; çıkış saatini iki varıştan da kontrol et.',
 dict(A='05.00, 60 km/sa ile süren 6 saati 90 km/sa’nin varış saatinden (11.00) çıkarmak; süreleri yanlış varışlarla eşleştirmişsin.',
      B='06.00, süreyi (6 saat) çıkış saati sanmak.',
      D='09.00, 90 km/sa ile süren 4 saati 13.00’ten çıkarmak; süre ile varış saati aynı hıza ait olmalı.',
      E='12.00, hız farkını süre farkıyla çarpıp yolu 60 km sanmak; yol x/60 − x/90 = 2 denkleminden çıkar.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='bilgi'),
 kisa='Hız 60’tan 90’a çıkınca (3/2 katı) süre 2/3’üne iner: süreler 3k ve 2k, fark k = 2 saat ⇒ 60 km/sa ile 6 saat, çıkış 07.00.')
sol=[x for x in [Fr(n,10) for n in range(1,200)] if x/4-x/6==Fr(15,60)]; assert sol==[3]
assert [x for x in [Fr(n,10) for n in range(1,200)] if x/4-x/6==Fr(5,60)]==[1]
assert Fr('0.15')*12==Fr('1.8') and Fr(15,60)*10==Fr('2.5') and Fr(1,2)*12==6
s=sirali(['1','1,8','2,5','3','6'])
P.K('0004','Bir öğrenci evinden okula saatte 4 km sabit hızla yürürse derse 10 dakika geç kalıyor, saatte 6 km sabit hızla yürürse derse 5 dakika erken varıyor. Öğrenci iki durumda da evden aynı saatte çıkıyor.\nBuna göre ev ile okul arası kaç km’dir?',
 s,'D','Ev ile okul arasındaki uzaklık.',
 ['10 dakika geç ile 5 dakika erken arasında toplam kaç dakika fark var?','Bu farkı saate çevir.','Yolu x ile göster: x/4 − x/6 bu farka eşittir.'],[YOL,DAK],
 [A('Süre farkı','Geç kalma ile erken varma arasındaki fark iki gecikmenin toplamıdır.','10 + 5 = 15 dakika = 1/4 saat'),
  A('Denklemi kur','Yavaş yürüyüş, hızlı yürüyüşten 1/4 saat uzun sürer.','x/4 − x/6 = 1/4'),
  A('Paydaları eşitle','Paydalar 12’de eşitlenir.','3x/12 − 2x/12 = x/12 = 1/4 ⇒ x = 3 km'),
  A('Kontrol','Süreler ve fark.','3 ÷ 4 = 45 dk · 3 ÷ 6 = 30 dk · 45 − 30 = 15 dk')],
 '“Geç” ve “erken” birlikte verilmişse süre farkı ikisinin toplamıdır.',
 dict(A='1, süre farkını 10 − 5 = 5 dakika almak; biri geç, biri erken olduğu için fark 10 + 5 = 15 dakikadır.',
      B='1,8, 15 dakikayı 0,15 saat almak; 15 dakika = 15/60 = 0,25 saattir.',
      C='2,5, hızları toplayıp 15 dakika ile çarpmak; aynı yolun iki süresinin farkı kullanılmalı.',
      E='6, 15 dakikayı yarım saat almak; 15 dakika saatin dörtte biridir.'),
 TT(A='dikkat',B='islem',C='bilgi',E='islem'))

# ===================== 0005 dairesel ORTA
c,vd,ve=600,180,120; t=Fr(c,vd-ve); assert t==10 and (vd*t-ve*t)==c and ve*t==1200
assert ve*Fr(c,vd+ve)==240 and vd*t==1800 and (vd+ve)*t==3000
s=sirali(['240','600','1200','1800','3000'])
P.R('0005','hr-dairesel','Dairesel pistte hareket','orta','Dairesel pist','Dairesel pistte aynı yönde hareket edenlerin ilk kez yan yana gelme süresini hız farkıyla bulur.','hikâyeli',3,
 'K-HR-05 (dairesel pist, aynı yön) · yeni kurgu (iki koşucu), istenen: yavaş koşucunun yolu',
 'Çevresi 600 metre olan dairesel bir koşu pistinde Deniz ile Efe, aynı noktadan aynı anda ve aynı yönde koşmaya başlıyor. Deniz dakikada 180 metre, Efe dakikada 120 metre sabit hızla koşuyor.\nDeniz’in Efe’ye arkadan ilk kez yetiştiği anda Efe kaç metre koşmuş olur?',
 s,'C','Deniz’in Efe’ye ilk kez yetiştiği ana kadar Efe’nin koştuğu yol.',
 ['Deniz’in Efe’ye arkadan yetişmesi için Efe’den kaç metre fazla koşması gerekir?','Deniz her dakika Efe’den kaç metre fazla koşar?','Süreyi bulup Efe’nin hızıyla çarp.'],[YOL,PIST],
 [A('Gereken fark','Deniz arkadan yetiştiğinde Efe’den tam bir tur fazla koşmuştur.','fark = 600 m'),
  A('Fark hızı','Her dakika Deniz, Efe’den hız farkı kadar fazla koşar.','180 − 120 = 60 m/dk · 600 ÷ 60 = 10 dakika'),
  A('Efe’nin yolu','Efe 10 dakika koşmuştur.','120 × 10 = 1200 m · kontrol: 180 × 10 = 1800 · 1800 − 1200 = 600')],
 'Dairesel pistte aynı yönde ilk yan yana geliş, hızlının bir tur fazla attığı andır.',
 dict(A='240, zıt yön formülünü (600 ÷ 300 = 2 dakika) kullanmak; koşucular aynı yönde.',B='600, Efe’nin tam bir tur attığını sanmak; bir tur fazla koşan Deniz’dir.',
      D='1800, Deniz’in koştuğu yol; soru Efe’yi soruyor.',E='3000, süreyi bulduktan sonra hızları toplamıyla çarpmak; istenen yalnız Efe’nin yolu.'),
 TT(A='bilgi',B='bilgi',D='dikkat',E='islem'))
kars=[sn for sn in range(1,33*60+1) if (Fr(150,60)*sn)%900==0]; assert len(kars)==5 and [k//60 for k in kars]==[6,12,18,24,30]
assert Fr(33*70,900)<3 and Fr(33*80,900)<3 and round(Fr(33*80,900))==3
s=sirali(['0','2','3','5','6'])
P.K('0005','Çevresi 900 metre olan dairesel bir yürüyüş parkurunda iki arkadaş, aynı noktadan aynı anda zıt yönlerde yürümeye başlıyor. Arkadaşlardan biri dakikada 70 metre, diğeri dakikada 80 metre sabit hızla yürüyor.\nBaşlangıç anı sayılmadığına göre yürüyüşün ilk 33 dakikasında bu iki arkadaş kaç kez karşılaşır?',
 s,'D','İlk 33 dakikadaki karşılaşma sayısı.',
 ['Zıt yönde yürüyenler ilk kez karşılaştığında ikisinin toplam yolu kaç metredir?','İki arkadaş birlikte bir dakikada kaç metre yol alır?','Her karşılaşma arası süreyi bul; 33 dakikaya kaç tane sığar?'],[YOL,PIST],
 [A('Karşılaşma koşulu','Zıt yönde yürüyenlerin yolları toplamı her 900 metrede bir karşılaşma demektir.','toplam yol = 900, 1800, 2700, …'),
  A('Karşılaşma aralığı','Birlikte her dakika hızları toplamı kadar yol alırlar.','70 + 80 = 150 m/dk · 900 ÷ 150 = 6 dakika'),
  A('Say','Karşılaşmalar 6’nın katı olan dakikalarda olur; 33’ü aşmayanları say.','6, 12, 18, 24, 30 ⇒ 5 kez (36 > 33)')],
 'Zıt yönde dairesel harekette karşılaşmalar eşit aralıklarla olur: aralık = çevre ÷ hızlar toplamı.',
 dict(A='0, aynı yön formülünü (900 ÷ 10 = 90 dakika) kullanmak; arkadaşlar zıt yönde yürüyor.',B='2, yavaş yürüyenin tam tur sayısını (2310 ÷ 900) karşılaşma sayısı sanmak.',
      C='3, hızlı yürüyenin tur sayısını (2640 ÷ 900 ≈ 2,9) yuvarlayıp karşılaşma sayısı sanmak.',E='6, 33 ÷ 6 = 5,5’i yukarı yuvarlamak; 36. dakika 33’ü aşar.'),
 TT(A='bilgi',B='dikkat',C='dikkat',E='islem'))

# ===================== 0006 karşılaşma (mola) ORTA
def kars_mola(D,va,vb,mola_bas,mola_sure,adim=Fr(1,120)):
    """Zaman taraması: A aracı mola_bas anında mola_sure kadar durur. Karşılaşma anı ve konumları."""
    t=Fr(0)
    while True:
        xa=va*(min(t,mola_bas)+max(0,t-mola_bas-mola_sure)); xb=vb*t
        if xa+xb>=D: return t,xa,xb
        t+=adim
tm,xa,xb=kars_mola(350,80,50,2,Fr(1,2)); assert tm==3 and xa==200 and xb==150 and 80*2+50*Fr(5,2)<350
assert 50*2==100 and 50*Fr(5,2)==125 and 350//2==175
s=sirali(['100','125','150','175','200'])
P.R('0006','hr-karsilasma','Karşılaşma (zıt yönlü hareket)','orta','Karşılaşma','Mola veren aracın hareket süresini ayrı hesaplayarak karşılaşma süresini ve karşılaşma noktasını bulur.','hikâyeli',3,
 'K-HR-01 (karşılaşma, bir araç mola veriyor) · yeni kurgu (otomobil ve kamyon), istenen: karşılaşma noktasının uzaklığı',
 'Aralarında 350 km bulunan K ve L kentlerinden bir otomobil ile bir kamyon aynı anda birbirine doğru yola çıkıyor. K’den çıkan otomobil saatte 80 km, L’den çıkan kamyon saatte 50 km sabit hızla gidiyor. Otomobil, yola çıktıktan 2 saat sonra yarım saat mola veriyor ve sonra aynı hızla yoluna devam ediyor; kamyon hiç durmuyor.\nBuna göre araçların karşılaştığı noktanın L kentine uzaklığı kaç km’dir?',
 s,'C','Karşılaşma noktasının L kentine uzaklığı (kamyonun aldığı yol).',
 ['Karşılaşma t saat sonra olsun: kamyon kaç saat, otomobil kaç saat hareket etmiştir?','İki aracın aldığı yolların toplamı 350 km’dir.','Karşılaşma noktasının L’ye uzaklığı, kamyonun aldığı yoldur.'],[YOL,KARS,DAK],
 [A('Hareket süreleri','Karşılaşma t saat sonra olsun. Kamyon t saat, otomobil molası çıkınca t − 1/2 saat gider.','kamyon: t · otomobil: t − 1/2'),
  A('Denklem','İki yolun toplamı K ile L arasındaki yoldur.','80 × (t − 1/2) + 50 × t = 350 ⇒ 130t − 40 = 350 ⇒ t = 3'),
  A('Molayı kontrol et','Mola karşılaşmadan önce bitmeli: 2,5. saatte araçlar arasında hâlâ yol vardır.','80 × 2 + 50 × 2,5 = 285 < 350 ✓'),
  A('L’ye uzaklık','Kamyon 3 saat gitmiştir.','50 × 3 = 150 km · otomobil: 80 × 2,5 = 200 km · 150 + 200 = 350 ✓',
    yol(('K','L'),[(0,1,'80 km/sa'),(350,-1,'50 km/sa')],[(200,'karşılaşma')],[(0,200,'otomobil 200 km',0),(200,350,'kamyon 150 km',0)],L=350))],
 'Mola veren araç için hareket süresi = toplam süre − mola süresidir; molada yalnız o araç durur.',
 dict(A='100, kamyonun ilk 2 saatte aldığı yol; karşılaşma mola anında değil, sonra oluyor.',B='125, molayı kamyona da uygulayıp kamyonun 2,5 saat gittiğini sanmak.',
      D='175, karşılaşmanın yolun ortasında olduğunu sanmak; hızlar ve süreler farklı.',E='200, otomobilin aldığı yol yani K’ye uzaklık; soru L’ye uzaklığı soruyor.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'))
tm,xa,xb=kars_mola(41,14,10,1,Fr(1,2)); assert tm==2 and xa==21 and xb==20 and 14+10*Fr(3,2)<41
assert 10*Fr(3,2)==15 and 10*1==10 and Fr(41,2)==Fr('20.5')
s=sirali(['10','15','20','20,5','21'])
P.K('0006','Aralarında 41 km bulunan iki köyden Ali ve Can, bisikletleriyle aynı anda birbirine doğru yola çıkıyor. Ali saatte 14 km, Can saatte 10 km sabit hızla gidiyor. Ali, yola çıktıktan 1 saat sonra 30 dakika dinlenip aynı hızla devam ediyor; Can ise hiç durmuyor.\nBuna göre karşılaştıkları anda Can kaç km yol almıştır?',
 s,'C','Karşılaşma anına kadar Can’ın aldığı yol.',
 ['Karşılaşma t saat sonra olsun: Ali kaç saat pedal çevirmiştir?','İkisinin yollarının toplamı 41 km’dir; denklemi kur.','Can hiç durmadığı için yolu 10 × t’dir.'],[YOL,KARS,DAK],
 [A('Hareket süreleri','Karşılaşma t saat sonra olsun. Can t saat, Ali dinlenme çıkınca t − 1/2 saat ilerler.','Can: t · Ali: t − 1/2'),
  A('Denklem','İki yolun toplamı 41 km.','14 × (t − 1/2) + 10 × t = 41 ⇒ 24t − 7 = 41 ⇒ t = 2'),
  A('Dinlenmeyi kontrol et','Dinlenme 1,5. saatte biter; o anda aralarında hâlâ yol vardır.','14 × 1 + 10 × 1,5 = 29 < 41 ✓'),
  A('Can’ın yolu','Can 2 saat ilerlemiştir.','10 × 2 = 20 km · Ali: 14 × 1,5 = 21 km · 20 + 21 = 41 ✓')],
 'Dinlenen kişinin süresinden dinlenmeyi çıkar, diğerininkine dokunma; sonra yolların toplamını kur.',
 dict(A='10, Can’ın dinlenme başladığında aldığı yol; karşılaşma daha sonra.',B='15, dinlenmeyi Can’a da uygulayıp Can’ın 1,5 saat gittiğini sanmak.',
      D='20,5, karşılaşmanın yolun ortasında olduğunu sanmak; hızlar farklı.',E='21, Ali’nin aldığı yol; soru Can’ı soruyor.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'))

# ===================== 0007 karşılaşma (kalan süreler) ZOR
def kalan_sure(t1,t2,vb):
    """t1: K aracının karşılaşmadan sonra M'ye varış süresi; t2: M aracının K'ye varış süresi; vb: M aracının hızı. Tarama ile t ve va."""
    r=[]
    for t in [Fr(n,4) for n in range(1,81)]:
        va=vb*t2/t  # KC = va·t = vb·t2
        if vb*t==va*t1: r.append((t,va,(va+vb)*t))
    return r
r=kalan_sure(2,Fr(9,2),60); assert r==[(3,90,450)]
assert 60*Fr(9,2)==270 and 150*Fr(13,4)==Fr('487.5') and 60*Fr(9,2)/2*2+60*Fr(9,2)==540 and 90*Fr(13,2)==585
s=sirali(['270','450','487,5','540','585'])
P.R('0007','hr-karsilasma','Karşılaşma (zıt yönlü hareket)','zor','Karşılaşma','Karşılaşmadan sonra kalan yolları her iki araç için ayrı ayrı yazarak karşılaşma süresini ve yolu bulur.','hikâyeli',5,
 'K-HR-01 (karşılaşma sonrası kalan süreler) · yeni veri (bir aracın hızı), yeni istenen (yolun tamamı)',
 'K ve M kasabalarından iki araç aynı anda, birbirine doğru sabit hızlarla yola çıkıyor. Araçlar yolda karşılaştıktan sonra K’den gelen araç M’ye 2 saatte, M’den gelen araç K’ye 4 saat 30 dakikada ulaşıyor.\nM’den çıkan aracın hızı saatte 60 km olduğuna göre K ile M arası kaç km’dir?',
 s,'B','K ile M arasındaki yol.',
 ['Karşılaşma noktasına C de; K ile C arasını hangi araç kaç saatte gider?','C ile M arası için de aynı şeyi yaz; karşılaşma süresine t de.','İki eşitliği taraf tarafa böl: t ile ilgili bir kare çıkar.'],[YOL,KARS,DAK],
 [A('K–C parçası','K’den gelen araç K–C’yi t saatte, M’den gelen araç aynı yolu karşılaşmadan sonra 4,5 saatte gider.','K–C = 60 × 4,5 = 270 km · K aracının hızı = 270 ÷ t'),
  A('C–M parçası','M’den gelen araç C–M’yi t saatte, K’den gelen araç bu yolu 2 saatte gider.','C–M = 60 × t = (270 ÷ t) × 2'),
  A('Karşılaşma süresi','İkinci eşitliği t ile çarp.','60 × t² = 540 ⇒ t² = 9 ⇒ t = 3 saat',
    yol(('K','M'),[(0,1,'K aracı'),(450,-1,'60 km/sa')],[(270,'C')],[(0,270,'270 km',0),(270,450,'180 km',0)],L=450)),
  A('K aracının hızı','K–C’yi 3 saatte gitmiştir.','270 ÷ 3 = 90 km/sa'),
  A('Yolun tamamı','İki parça toplanır.','270 + 60 × 3 = 450 km · kontrol: 90 × 2 = 180 ✓')],
 'Karşılaşma sonrası süreler verilince her parçayı iki araç cinsinden ayrı ayrı yaz; bilinmeyen süre t² = (kalan süre) × (kalan süre) olarak çıkar.',
 dict(A='270, yalnız K ile karşılaşma noktası arasındaki yol; diğer parça (180 km) eklenmemiş.',
      C='487,5, karşılaşma süresini kalan sürelerin ortalaması (3,25 saat) sanmak; t² = 2 × 4,5 bağıntısı kullanılmalı.',
      D='540, hız oranını süre oranı (4,5 ÷ 2) sanıp K aracının hızını 135 almak; oran karşılaşma süresiyle kurulur.',
      E='585, K aracının hızını (90) iki kalan sürenin toplamıyla çarpmak; 6,5 saat bu aracın yolculuk süresi değil.'),
 TT(A='dikkat',C='bilgi',D='bilgi',E='islem'),
 kisa='Karşılaşma süresi t ise t² = 2 × 4,5 = 9 ⇒ t = 3; yol = M aracı × (t + 4,5) = 60 × 7,5 = 450 km.')
r=kalan_sure(1,4,15); assert r==[(2,30,90)]
assert 15*4==60 and 45*Fr(5,2)==Fr('112.5') and 60*1+15*4==120 and 30*5==150
s=sirali(['60','90','112,5','120','150'])
P.K('0007','Bir bisikletli ile bir motosikletli, bir yolun iki ucundan aynı anda birbirine doğru sabit hızlarla hareket ediyor. Karşılaşmalarından 1 saat sonra motosikletli yolun öbür ucuna, karşılaşmalarından 4 saat sonra da bisikletli motosikletlinin çıktığı uca varıyor.\nBisikletlinin hızı saatte 15 km olduğuna göre yolun uzunluğu kaç km’dir?',
 s,'B','Yolun uzunluğu.',
 ['Karşılaşma noktasından motosikletlinin çıktığı uca kadar olan yolu bisikletli kaç saatte gider?','Karşılaşma süresine t de; iki parçayı ayrı ayrı iki araç cinsinden yaz.','Eşitliklerden t² çıkar; t’yi bulup hızları hesapla.'],[YOL,KARS],
 [A('Motosikletli tarafı','Motosikletli bu parçayı t saatte, bisikletli karşılaşmadan sonra 4 saatte gider.','parça 1 = 15 × 4 = 60 km · motosiklet hızı = 60 ÷ t'),
  A('Bisikletli tarafı','Bisikletli bu parçayı t saatte, motosikletli 1 saatte gider.','parça 2 = 15 × t = (60 ÷ t) × 1'),
  A('Karşılaşma süresi','İkinci eşitliği t ile çarp.','15 × t² = 60 ⇒ t² = 4 ⇒ t = 2 saat'),
  A('Motosikletin hızı','60 km’yi 2 saatte gitmiştir.','60 ÷ 2 = 30 km/sa'),
  A('Yolun tamamı','İki parçayı topla.','60 + 15 × 2 = 90 km · kontrol: 30 × 1 = 30 ✓')],
 'Karşılaşma sonrası iki kalan süre verilmişse karşılaşma süresi bu iki sürenin çarpımının kareköküdür.',
 dict(A='60, yalnız bir parça (bisikletlinin karşılaşmadan sonra aldığı yol); diğer parça eklenmemiş.',C='112,5, karşılaşma süresini kalan sürelerin ortalaması (2,5 saat) sanmak.',
      D='120, hız oranını kalan sürelerin oranı (4 ÷ 1) sanıp motosiklet hızını 60 almak.',E='150, motosikletin hızını (30) iki kalan sürenin toplamıyla (5 saat) çarpmak.'),
 TT(A='dikkat',C='bilgi',D='bilgi',E='islem'),
 kisa='t² = 1 × 4 ⇒ t = 2 saat; yol = bisikletlinin hızı × (t + 4) = 15 × 6 = 90 km.')

# ===================== 0008 yetişme ZOR
def son_fark(v1,v2,once,fark):
    r=[]
    for D in range(1,2000):
        T=Fr(D,v2)  # hızlı aracın yolculuk süresi
        if D-v1*(T+once)==fark: r.append((D,T))
    return r
r=son_fark(60,80,1,30); assert r==[(360,Fr(9,2))]
yet=Fr(60,80-60); assert yet==3 and 80*yet==240 and 60*(Fr(9,2)+1)==330
assert [D for D in range(1,2000) if D-60*Fr(D,80)==30]==[120]
s=sirali(['120','240','330','360','440'])
P.R('0008','hr-yetisme','Yetişme (aynı yönlü hareket)','zor','Yetişme','Geç çıkan hızlı aracın varışında yavaş araçla arasındaki farktan yolu bulur; yetişmeden sonra farkın açılmasını yorumlar.','hikâyeli',4,
 'K-HR-02 (yetişip geçme, varışta kalan fark) · yeni kurgu (iki tren), yeni istenen (iki istasyon arası)',
 'Bir yük treni saat 06.00’da K istasyonundan L istasyonuna doğru saatte 60 km sabit hızla hareket ediyor. Bir yolcu treni ise saat 07.00’de K istasyonundan, paralel raylarda aynı yöne doğru saatte 80 km sabit hızla hareket ediyor. Trenler yol boyunca hiç durmuyor ve yolcu treni L’ye vardığı anda yük treni L’ye 30 km uzaklıkta bulunuyor.\nBuna göre K ile L istasyonları arası kaç km’dir?',
 s,'D','K ile L istasyonları arasındaki yol.',
 ['Yolcu treni çıktığında yük treni kaç km öndedir?','Yolcu treninin yolculuğu T saat sürsün: o anda iki trenin K’ye uzaklıklarını yaz.','Yolcu treni yük trenine yetişip geçer; varışta aralarında 30 km olur. Denklemi kur.'],[YOL,YET],
 [A('Başlangıç farkı','07.00’de yük treni 1 saattir yoldadır.','60 × 1 = 60 km önde'),
  A('Varış anı','Yolcu treninin yolculuğu T saat sürsün. Bu anda yük treni T + 1 saattir yoldadır.','K–L = 80 × T · yük treni: 60 × (T + 1)'),
  A('Denklem','Yolcu treni L’de, yük treni 30 km geride.','80T − 60(T + 1) = 30 ⇒ 20T = 90 ⇒ T = 4,5 saat'),
  A('İki istasyon arası','Yolcu treni 4,5 saat gitmiştir.','80 × 4,5 = 360 km',
    yol(('K','L'),[],[(240,'yetişme 10.00'),(330,'yük treni',True)],[(0,240,'240 km',0),(330,360,'30 km',0)],L=360,alt='11.30: yolcu treni L’de, yük treni 330. km’de')),
  A('Kontrol','Yetişme 60 ÷ 20 = 3 saat sonra (10.00, 240. km); sonra fark saatte 20 km açılır.','30 ÷ 20 = 1,5 saat · 3 + 1,5 = 4,5 ✓ · yük treni: 60 × 5,5 = 330')],
 'Yetişip geçme sorularında arkadan çıkanın varış anını yaz: aradaki fark = hızlının yolu − yavaşın yolu.',
 dict(A='120, yük treninin 1 saat önce çıktığını unutup 80T − 60T = 30 kurmak.',B='240, 30 km’lik farkı kullanmadan yetişme noktasını bulmak; soru istasyonlar arasını soruyor.',
      C='330, yük treninin K’ye uzaklığı; yolcu treni L’dedir ve 30 km öndedir.',E='440, başlangıç farkını yolcu treninin hızıyla (80 × 1) hesaplamak.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='islem'))
r=son_fark(60,90,2,30); assert r==[(450,5)]
assert 90*Fr(30,30)==90 and 60*2==120 and 90*Fr(120,30)==360 and 60*7==420
s=sirali(['90','120','360','420','450'])
P.K('0008','Bir minibüs saat 10.00’da bir duraktan saatte 60 km sabit hızla yola çıkıyor. Bir otobüs saat 12.00’de aynı duraktan, aynı yolu izleyerek saatte 90 km sabit hızla yola çıkıyor. İki araç da yol boyunca durmuyor. Otobüs son durağa vardığı anda minibüs son durağa 30 km uzaklıktadır.\nBuna göre iki durak arası kaç km’dir?',
 s,'E','İki durak arasındaki yol.',
 ['Otobüs yola çıktığında minibüs kaç km öndedir?','Otobüsün yolculuğu T saat sürsün; minibüs kaç saattir yoldadır?','Otobüsün yolu − minibüsün yolu = 30 denklemini kur.'],[YOL,YET],
 [A('Başlangıç farkı','12.00’de minibüs 2 saattir yoldadır.','60 × 2 = 120 km önde'),
  A('Varış anı','Otobüsün yolculuğu T saat sürsün; minibüs T + 2 saattir yoldadır.','yol = 90 × T · minibüs: 60 × (T + 2)'),
  A('Denklem','Otobüs son durakta, minibüs 30 km geride.','90T − 60(T + 2) = 30 ⇒ 30T = 150 ⇒ T = 5 saat'),
  A('İki durak arası','Otobüs 5 saat gitmiştir.','90 × 5 = 450 km · minibüs: 60 × 7 = 420 ✓')],
 'Önce yavaş aracın başlangıç farkını bul; varışta kalan fark, yetişmeden sonra açılan farktır.',
 dict(A='90, minibüsün 2 saat önce çıktığını unutup 90T − 60T = 30 kurmak.',B='120, otobüs çıktığında minibüsün öndeki yolu; yolun tamamı değil.',
      C='360, 30 km’lik farkı kullanmadan yetişme noktasını (120 ÷ 30 = 4 saat) bulmak.',D='420, minibüsün aldığı yol; minibüs son durağa 30 km uzakta.'),
 TT(A='dikkat',B='bilgi',C='dikkat',D='dikkat'))

P.yaz(os.path.join(H,'hareketprob-1.json'),os.path.join(H,'hareketprob-1-kardes.json'))
