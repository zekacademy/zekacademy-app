"""Veri ve İstatistik (hafif mod): 30 ana soru, kardeş yok, ipucu 1. Şekil/tablo de metin de aynı veri listelerinden üretilir;
her cevap ve her çeldirici değeri statistics/Fraction ile hesaplanıp assert edilir. Standart sapma: n−1'e bölünen örneklem tanımı, soruda açıkça verilir.
Çizim yardımcıları uret-grafikiki.py'den kopyalandı."""
import sys,os,math,itertools,statistics as stt
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from _hafif_mat import tablo_svg
H.KONU='Veri ve İstatistik'
UK='matd|Veri ve İstatistik'
P=Parti('veri','Veri ve İstatistik',UK)
ACC=G.ACC
# ---------- çizim yardımcıları (G._svg / G._t / G.ACC stili; currentColor, viewBox)
def _eksen(x0,yb,x1,yt):
    return (f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke-width="1.6"/>'
            f'<line x1="{x0}" y1="{yb}" x2="{x0}" y2="{yt-8}" stroke-width="1.6"/>'
            f'<path d="M{x0-4} {yt-4} L{x0} {yt-12} L{x0+4} {yt-4}" stroke-width="1.4"/>')
def _izgara(x0,x1,Y,adim,ust,olcek):
    b=[]
    for v in range(adim,ust+1,adim):
        y=Y(v); b.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke-width="1" stroke-dasharray="3 3" opacity=".4"/>')
        if olcek: b.append(G._t(x0-6,y+4,str(v),anchor='end',size=10))
    if olcek: b.append(G._t(x0-6,Y(0)+4,'0',anchor='end',size=10))
    return ''.join(b)
def sutun(et,dg,adim,ust,ybas,xbas=None,olcek=True,W=330,H=226):
    """Sütun grafiği gövdesi. Her değer ızgara çizgisinde bitmeli (okunabilirlik)."""
    assert all(v%adim==0 and 0<v<=ust for v in dg) and len(et)==len(dg)
    x0,x1,yt,yb=46,W-8,34,H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,olcek)]
    n=len(et); sl=(x1-x0)/n; bw=min(34,sl*.55)
    for i,(e,v) in enumerate(zip(et,dg)):
        cx=x0+sl*(i+.5); y=Y(v)
        b.append(f'<rect x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{yb-y:.1f}" stroke-width="1.2" style="fill:{ACC}" fill-opacity=".55"/>')
        b.append(G._t(cx,yb+15,e,size=10))
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def cizgi(et,dg,adim,ust,ybas,xbas=None,W=330,H=226):
    assert all(v%adim==0 and 0<v<=ust for v in dg) and len(et)==len(dg)
    x0,x1,yt,yb=46,W-12,34,H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,True)]
    n=len(et); sl=(x1-x0)/n; pts=[(x0+sl*(i+.5),Y(v)) for i,v in enumerate(dg)]
    for (x,y),e in zip(pts,et):
        b.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{yb}" stroke-width="1" stroke-dasharray="2 3" opacity=".55"/>')
        b.append(G._t(x,yb+15,e,size=10))
    b.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" stroke-width="2.4" style="stroke:{ACC}"/>')
    for x,y in pts: b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" style="fill:{ACC};stroke:{ACC}"/>')
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def tek(g): body,W,Hh=g; return G._svg(W,Hh,body)
def alt_alta(*parcalar):
    """[(başlık, (gövde,W,H))] parçalarını alt alta tek SVG'de birleştirir."""
    W=max(p[1][1] for p in parcalar); y=0; b=[]
    for ad,(body,w,h) in parcalar:
        b.append(G._t(W/2,y+14,ad,size=11,bold=True)); b.append(f'<g transform="translate({(W-w)/2:.1f},{y+20})">{body}</g>'); y+=h+26
    return G._svg(W,y,''.join(b))


# ---------- ek çizim yardımcıları (aynı görsel dil)
def sutun_h(et,dg,adim,ust,ybas,xbas=None,W=340,H=226):
    """Sütun; dg içinde None = çizilmemiş sütun ('?' yazılır)."""
    assert all(v is None or (v%adim==0 and 0<v<=ust) for v in dg) and len(et)==len(dg)
    x0,x1,yt,yb=46,W-8,34,H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,True)]
    n=len(et); sl=(x1-x0)/n; bw=min(34,sl*.55)
    for i,(e,v) in enumerate(zip(et,dg)):
        cx=x0+sl*(i+.5)
        if v is None:
            b.append(f'<rect x="{cx-bw/2:.1f}" y="{yt:.1f}" width="{bw:.1f}" height="{yb-yt:.1f}" fill="none" stroke-width="1.4" stroke-dasharray="5 4" opacity=".7"/>'); b.append(G._t(cx,Y(ust*0.54)+6,'?',size=18,bold=True,renk=ACC))
        else:
            y=Y(v); b.append(f'<rect x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{yb-y:.1f}" stroke-width="1.2" style="fill:{ACC}" fill-opacity=".55"/>')
        b.append(G._t(cx,yb+15,e,size=10))
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H

# ---------- istatistik yardımcıları (tanımlar soruda verilir)
def ort(l): return Fr(sum(l),len(l))
def ortanca(l):
    s=sorted(l); n=len(s)
    return Fr(s[n//2]) if n%2 else Fr(s[n//2-1]+s[n//2],2)
def tepe(l):
    c={}
    for x in l: c[x]=c.get(x,0)+1
    m=max(c.values()); return sorted(k for k,v in c.items() if v==m)
def aciklik(l): return max(l)-min(l)
def ceyrekA(l):
    s=sorted(l); n=len(s); h=n//2
    return ortanca(s[h+(n%2):])-ortanca(s[:h])
def varyans(l):
    m=ort(l); return sum((x-m)**2 for x in l)/(len(l)-1)
def kok(v):
    v=Fr(v); a=math.isqrt(v.numerator); b=math.isqrt(v.denominator); assert a*a==v.numerator and b*b==v.denominator,'tam kare degil'; return Fr(a,b)
def sd(l): return kok(varyans(l))
def liste(l): return ', '.join(map(str,l))
def tabdizi(pairs): return [x for v,f in pairs for x in [v]*f]
def Q(no,tipId,z,alt,kaz,kalip,kart_,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,sira=None,kisa=None):
    c=[k for k in KARTLAR if k['tipId']==tipId][0]
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,sira=sira,ip=[ip],bilgi=bilgi,puf=puf,kisa=kisa,
       tipId=tipId,tip=c['tip'],z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=kart_)

ORT=B('Aritmetik ortalama','ortalama = verilerin toplamı ÷ veri sayısı, yani toplam = ortalama × veri sayısı. Örnek: 4, 6, 8 için ortalama 18 ÷ 3 = 6, toplam 6 × 3 = 18')
AGR=B('Ağırlıklı ortalama','her değer kendi ağırlığıyla çarpılıp toplanır, ağırlıklar toplamına bölünür. Örnek: 2 tanesi 10, 3 tanesi 20 olan değerlerin ortalaması (2 × 10 + 3 × 20) ÷ 5 = 16')
MED=B('Ortanca (medyan)','veri küçükten büyüğe sıralanır; terim sayısı tekse ortadaki, çiftse ortadaki iki sayının ortalaması ortancadır. Örnek: 3, 5, 9, 12 → (5 + 9) ÷ 2 = 7')
MOD=B('Tepe değer (mod)','veri grubunda en çok tekrar eden değerdir. Örnek: 2, 3, 3, 5, 3, 5 → tepe değer 3 (3 kez geçer)')
ACK=B('Açıklık','en büyük değer ile en küçük değerin farkıdır. Örnek: 4, 9, 15 → açıklık 15 − 4 = 11')
CEY=B('Çeyrekler açıklığı','sıralı veride ortanca grubu iki yarıya ayırır (terim sayısı tekse ortanca iki yarıya da katılmaz). Alt yarının ortancası Q1, üst yarının ortancası Q3 olur; çeyrekler açıklığı Q3 − Q1’dir. Örnek: 1, 3, 5, 7, 9, 11, 13 → Q1 = 3, Q3 = 11, fark 8')
STD=B('Standart sapma','veriler ortalamadan ne kadar uzaksa sapma o kadar büyüktür. Bu soruda s = √[ (her verinin ortalamadan farkının karelerinin toplamı) ÷ (veri sayısı − 1) ] alınır. Örnek: 2, 4, 6 → ortalama 4, farklar −2, 0, 2, s = √(8 ÷ 2) = 2')
DON=B('Veriyi dönüştürme','her veri a ile çarpılıp b eklenirse ortalama ve ortanca da aynı işlemden geçer (a × ort + b); açıklık ve standart sapma |a| ile çarpılır, b etkisizdir. Örnek: 2, 4, 6 → 2x + 1 → 5, 9, 13 ve ortalama 4 → 9, açıklık 4 → 8')
SIK=B('Sıklık tablosu','tablodaki her değer, yanındaki sıklık kadar tekrar eden veri demektir. Örnek: “3 → 2 kez, 5 → 1 kez” veri grubu 3, 3, 5 demektir; toplam veri sayısı sıklıkların toplamıdır')
BIR=B('Merkezi eğilim ölçüleri','ortalama, ortanca ve tepe değer verinin “ortası” hakkında bilgi verir; üçünün eşit olması bu ölçülerden elde edilen koşulları birlikte yazmayı gerektirir. Örnek: 2, 3, 3, 4 → ortalama 3, ortanca 3, tepe değer 3')
GRF=B('Grafikten veri okuma','sütunun ya da noktanın yüksekliği eksendeki değeri verir; bu değerler listelenip ölçüler hesaplanır. Örnek: yükseklikleri 20, 40, 40 olan üç sütun → veri 20, 40, 40')

# ---------- kartlar
KY='ÖSYM 2018–2026 (veri/istatistik soruları) · MEB 9. sınıf Veri · yayın soru bankaları (yalnız mantık)'
kart('K-VRI-01','Aritmetik ortalama: eleman ekleme, çıkarma, eksik veri','Ortalama × terim sayısı = toplam eşitliğiyle eklenen, çıkarılan ya da eksik elemanın değeri bulunur.','Yeni terim sayısını kullanmamak; ortalamaların farkını elemanın kendisi sanmak; toplamı yanlış terim sayısına bölmek.','orta','hikâyeli',3,'vri-ort','Aritmetik ortalama: eleman ekleme, çıkarma ve eksik veri',KY)
kart('K-VRI-02','Ağırlıklı ve gruplu ortalama','Grupların toplam değerleri (ortalama × kişi sayısı) birleştirilip toplam sayıya bölünür; ağırlıklı ortalamada eksik değer denklemle bulunur.','Basit ortalama almak; ağırlıkları ters eşleştirmek; toplam kişi sayısına bölmeyi unutmak.','orta','hikâyeli',4,'vri-agirlik','Ağırlıklı ve gruplu ortalama',KY)
kart('K-VRI-03','Ortanca ve tepe değer','Veriyi sıralayıp ortadaki terimi (ya da ortadaki ikiliyi) bulma; sıklık tablosunda birikimli sıklıkla ortanca konumu belirleme; en çok tekrarlanan değer.','Sıralamadan ortadakini almak; çift terimde tek terim seçmek; sıklığı değer sanmak.','orta','tablo',3,'vri-medmod','Ortanca ve tepe değer (sıralı ve sıklık tablolu)',KY)
kart('K-VRI-04','Ortalama–ortanca–tepe değer koşulları','Ölçülerin eşitliği ya da birbirine göre konumu eşitlik/eşitsizlik olarak yazılır; sıralama ve tekrar koşulları denetlenir.','Tek tepe değer koşulunu atlamak; sıralamayı gözetmemek; tüm çözümleri taramamak.','zor','düz',4,'vri-birlikte','Merkezi eğilim ölçülerinin birlikte yorumu',KY)
kart('K-VRI-05','Açıklık ve çeyrekler açıklığı','Bilinmeyen terimin en küçük/en büyük olma durumları ayrı ayrı incelenir; çeyrekler Q1 ve Q3 sıralı veriden bulunur.','Bilinmeyenin yalnız bir durumunu almak; ortancayı iki yarıya da katmak; Q3 − Q1 yerine açıklık vermek.','orta','düz',3,'vri-aciklik','Açıklık ve çeyrekler açıklığı',KY)
kart('K-VRI-06','Standart sapma','Ortalamadan farkların karelerinin toplamı (n − 1’e bölünerek) kök altına alınır; karşılaştırmada ölçüt dağılımın ortalamadan uzaklığıdır, açıklık değildir.','n yerine n − 1 kullanmak; kök almayı unutmak; açıklığı standart sapma ile karıştırmak.','orta','yeni nesil',4,'vri-sapma','Standart sapma ve tanımlı sapma ölçüleri',KY)
kart('K-VRI-07','Veri grubunu dönüştürme','Her veriye aynı işlem uygulanınca ortalama aynı işlemle, açıklık ve standart sapma |çarpan| ile değişir; toplama etkisizdir.','Standart sapmaya da toplamayı uygulamak; çarpma sırasını karıştırmak.','kolay','öncüllü',2,'vri-donusum','Sabit toplama ve çarpmanın ölçülere etkisi',KY)
kart('K-VRI-08','Tablo ve grafikten ölçü hesabı','Tablodan ya da grafikten okunan değerler tek listede toplanır; ortalama, ortanca, tepe değer ve eksik sıklık/sütun aynı veri listesinden bulunur.','Sıklığı veri sanmak; ortalamayı değerlerin ortalaması sanmak; grafikten yanlış okumak.','orta','tablo',4,'vri-sekil','Tablo ve grafikten ölçü hesabı',KY)

# ================= 0001 · kolay · eleman ekleme (yazılı)
assert 5*72-4*70==80 and 72-70==2 and 4*(72-70)==8 and Fr(70+72,2)==71
mk_=lambda *a,**k:None
Q('0001','vri-ort','kolay','Aritmetik Ortalama','Ortalama ve terim sayısından toplamı bulup eklenen terimin değerini hesaplar.','hikâyeli','K-VRI-01 (eleman ekleme) · ilk dört yazılı ve beşinci yazılı',
 'Bir öğrencinin matematik dersinin ilk 4 yazılısından aldığı puanların aritmetik ortalaması 70’tir. Öğrenci 5. yazılıdan da puan alınca beş yazılının aritmetik ortalaması 72 olmuştur.\nBuna göre öğrenci 5. yazılıdan kaç puan almıştır?',
 80,[(2,'İki ortalama arasındaki farkı (72 − 70) 5. yazılının puanı sanmış.','dikkat'),(8,'Ortalamadaki artışı yalnız ilk dört sınavın sayısıyla çarpıp (4 × 2) ek puan saymış.','bilgi'),(72,'Yeni ortalamayı 5. sınavın puanı sanmış.','dikkat'),(71,'İki ortalamanın ortalamasını (70 ile 72’nin ortası) 5. sınavın puanı sanmış.','bilgi')],
 '5. yazılıdan alınan puan.',
 'İki ortalamayı da toplam puana çevirip karşılaştır: bunun için her ortalamayı hangi sayıyla çarpmalısın?',
 [ORT],
 [A('İlk dört sınavın toplamı','Toplam = ortalama × sınav sayısı.','4 × 70 = 280'),A('Beş sınavın toplamı','Yeni ortalama 72 ve sınav sayısı 5.','5 × 72 = 360'),A('5. sınavın puanı','İki toplamın farkı 5. sınavdır.','360 − 280 = 80')],
 'Ortalama ve terim sayısı bilindiğinde önce toplamı bul; yeni terimin değeri iki toplamın farkıdır.')

# ================= 0002 · kolay · eksik veri (kurye)
v=[18,24,30,21]; kt=125; x=kt-sum(v); assert x==32 and ort(v+[x])==25
assert 4*25-sum(v)==7 and kt-sum(v[:3])-0==53 and 5*25==125
mk_=None
Q('0002','vri-ort','kolay','Aritmetik Ortalama','Bir veri grubunun ortalaması verildiğinde eksik terimi bulur.','hikâyeli','K-VRI-01 (eksik veri) · kuryenin günlük paketleri',
 'Bir kuryenin 5 gün boyunca günlük teslim ettiği paket sayıları sırasıyla 18, 24, x, 30 ve 21’dir. Bu veri grubunun aritmetik ortalaması 25’tir.\nBuna göre x kaçtır?',
 32,[(7,'Toplamı 5 yerine 4 veriyle (4 × 25) kurup bilinen dört sayının toplamını çıkarmış.','islem'),(25,'Ortalamanın bütün verilere eşit olduğunu düşünüp x’i ortalamaya eşitlemiş.','bilgi'),(53,'5 × 25’ten yalnız üç bilinen sayıyı (18 + 24 + 30) çıkarıp 21’i unutmuş.','dikkat'),(125,'Beş verinin toplamını (5 × 25) bulup bilinen sayıları çıkarmayı unutmuş.','dikkat')],
 'Eksik paket sayısı x.',
 'Beş verinin toplamı ortalamayla nasıl ilişkilidir? Bilinen dört sayının toplamını da bul.',
 [ORT],
 [A('Toplamı bul','Beş verinin toplamı ortalama × 5’tir.','5 × 25 = 125'),A('Bilinen sayıların toplamı','x dışındaki dört sayıyı topla.','18 + 24 + 30 + 21 = 93'),A('x’i bul','Toplamdan bilinenleri çıkar.','x = 125 − 93 = 32')],
 'Eksik terim = (ortalama × terim sayısı) − bilinen terimlerin toplamı.')

# ================= 0003 · kolay · çift sayıda veri ortanca (kafe)
d=[12,7,19,5,14,9]; assert sorted(d)==[5,7,9,12,14,19] and ortanca(d)==Fr(21,2)
assert 9==sorted(d)[2] and ort(d)==11 and (d[2]+d[3])/2==12 and aciklik(d)==14
Q('0003','vri-medmod','kolay','Ortanca','Çift sayıda terimi olan veride ortancayı ortadaki iki terimin ortalaması olarak bulur.','hikâyeli','K-VRI-03 (çift sayıda ortanca) · kafede satılan tatlılar',
 'Bir kafede ardışık 6 gün boyunca satılan tatlı sayıları günlere göre sırasıyla 12, 7, 19, 5, 14 ve 9’dur.\nBuna göre bu veri grubunun ortancası (medyanı) kaçtır?',
 Fr(21,2),[(9,'Çift sayıda terimde ortadaki iki sayıdan yalnız küçüğünü (9) almış.','bilgi'),(11,'Ortanca yerine aritmetik ortalamayı (66 ÷ 6) bulmuş.','bilgi'),(12,'Veriyi sıralamadan, yazıldığı sıradaki ortadaki iki sayının (19 ve 5) ortalamasını almış.','dikkat'),(14,'Ortanca yerine açıklığı (19 − 5) bulmuş.','bilgi')],
 'Veri grubunun ortancası.',
 'Önce sayıları küçükten büyüğe diz; kaç terim olduğuna bak.',
 [MED],
 [A('Sırala','Sayıları küçükten büyüğe diz.','5, 7, 9, 12, 14, 19'),A('Ortadakileri bul','6 terim vardır; 3. ve 4. terim ortadadır.','9 ve 12'),A('Ortalamalarını al','Çift sayıda terimde ortanca ortadaki ikilinin ortalamasıdır.','(9 + 12) ÷ 2 = 10,5')],
 'Ortanca bulurken önce sırala; terim sayısı çiftse ortadaki iki sayının ortalamasını al.')

# ================= 0004 · kolay · tablo tepe değer + açıklık
pr=[(36,5),(37,9),(38,12),(39,8),(40,6)]; dd=tabdizi(pr); assert len(dd)==40 and tepe(dd)==[38] and aciklik(dd)==4
assert 38+4==42 and 12+4==16 and max(f for _,f in pr)-min(f for _,f in pr)==7 and 38+7==45
SK=tablo_svg(['Ayakkabı numarası','Üye sayısı'],[[str(a),str(b)] for a,b in pr])
Q('0004','vri-medmod','kolay','Tepe Değer ve Açıklık','Sıklık tablosundan tepe değeri ve açıklığı bulur.','tablo','K-VRI-03 (tepe değer, açıklık, tablo) · spor salonu üyelerinin ayakkabı numaraları',
 'Bir spor salonundaki 40 üyenin giydiği ayakkabı numaraları ve her numarayı giyen üye sayısı aşağıdaki tabloda verilmiştir.\nBuna göre bu veri grubunun tepe değeri ile açıklığının toplamı kaçtır?',
 42,[(4,'Yalnız açıklığı (40 − 36) bulmuş; tepe değeri toplamaya katmamış.','dikkat'),(16,'Tepe değer yerine en büyük sıklığı (12) alıp açıklığa (4) eklemiş.','bilgi'),(38,'Yalnız tepe değeri bulup açıklığı toplamaya katmamış.','dikkat'),(45,'Açıklığı sıklıkların farkı (12 − 5 = 7) olarak alıp tepe değere (38) eklemiş.','bilgi')],
 'Tepe değer ile açıklığın toplamı.',
 'Tepe değer, en çok tekrar eden numaradır. Açıklık ise numaralar üzerinden bulunur.',
 [MOD,ACK],
 [A('Tepe değer','En büyük sıklık 12 olan numara en çok giyilendir.','Tepe değer = 38'),A('Açıklık','Açıklık numaralar arasındaki farktır; sıklıklara bakılmaz.','40 − 36 = 4'),A('Topla','Tepe değer ile açıklığı topla.','38 + 4 = 42')],
 'Tepe değer sıklığı en büyük olan değerdir (sıklık değil); açıklık ise değerlerden bulunur.',sekil=SK)

# ================= 0005 · kolay · standart sapma karşılaştırma
G5=['20, 20, 20, 20','18, 19, 21, 22','14, 18, 22, 26','8, 20, 20, 32','10, 10, 30, 30']
V5=[list(map(int,s.split(', '))) for s in G5]
assert all(ort(l)==20 for l in V5)
vs=[varyans(l) for l in V5]; ac=[aciklik(l) for l in V5]
assert vs.index(max(vs))==4 and ac.index(max(ac))==3 and vs[0]==0 and vs[1]<vs[2]<vs[3]<vs[4]
Q('0005','vri-sapma','kolay','Standart Sapma','Ortalamaları eşit veri gruplarının standart sapmalarını ortalamaya uzaklıklarına bakarak karşılaştırır.','düz','K-VRI-06 (standart sapma, karşılaştırma) · ortalamaları eşit dört elemanlı gruplar',
 'Aşağıdaki veri gruplarının her birinin aritmetik ortalaması 20’dir.\nBuna göre bu veri gruplarından hangisinin standart sapması en büyüktür?',
 G5[4],
 [(G5[0],'Bütün sayıları aynı olan grubu “sapması en büyük” sanmış; bu grupta sapma sıfırdır, en küçüktür.','bilgi'),(G5[1],'Sayıları birbirine en yakın ve ardışık gibi duran grubu seçmiş; bu grup ortalamaya çok yakındır.','bilgi'),(G5[2],'Sayıların eşit aralıklı dizilmesini büyük dağılım sanmış; bu gruptaki sayılar daha çok ortalamaya yakındır.','dikkat'),(G5[3],'Yalnız en küçük ile en büyük sayıya (açıklık 24) bakmış; ortadaki iki sayı ortalamaya eşit olduğu için sapma 10, 10, 30, 30’dan küçüktür.','dikkat')],
 'Standart sapması en büyük olan veri grubu.',
 'Her sayının ortalamaya (20) uzaklığını yaz; uzaklıkların hangi grupta genel olarak en büyük olduğuna bak.',
 [STD],
 [A('Ortalamadan farkları yaz','Her grup için sayıların 20’den farkına bak.','20, 20, 20, 20 → 0, 0, 0, 0 · 18, 19, 21, 22 → −2, −1, 1, 2 · 14, 18, 22, 26 → −6, −2, 2, 6 · 8, 20, 20, 32 → −12, 0, 0, 12 · 10, 10, 30, 30 → −10, −10, 10, 10'),A('Farkların karelerini topla','Standart sapma farkların karelerine dayanır.','0 · 10 · 80 · 288 · 400'),A('En büyüğü seç','Kareler toplamı en büyük olan grubun standart sapması en büyüktür.','10, 10, 30, 30')],
 'Ortalamaları eşit gruplarda standart sapma, sayıların ortalamaya uzaklıklarının karelerinin toplamıyla büyür; yalnız uç değerlere (açıklığa) bakma.',sira=G5)

# ================= 0006 · kolay · her veriyi 3 ile çarp 4 ekle
o6=8; assert 3*o6+4==28 and 3*o6==24 and o6+4==12 and o6+3*4==20 and o6+3+4==15
Q('0006','vri-donusum','kolay','Veriyi Dönüştürme','Bir veri grubunun her terimine aynı işlem uygulanınca ortalamanın aynı işlemle değiştiğini kullanır.','düz','K-VRI-07 (çarp ve ekle, ortalama) · ortalaması 8 olan veri',
 'Aritmetik ortalaması 8 olan bir veri grubundaki her terim önce 3 ile çarpılmış, sonra elde edilen sayılara 4 eklenmiştir.\nBuna göre yeni veri grubunun aritmetik ortalaması kaçtır?',
 28,[(12,'Yalnız 4 ekleme işlemini uygulamış (8 + 4).','dikkat'),(15,'Çarpmayı yapmamış; 3 ve 4’ü ortalamaya toplamış (8 + 3 + 4).','bilgi'),(24,'Yalnız 3 ile çarpmayı yapıp 4’ü eklemeyi unutmuş.','dikkat'),(20,'Çarpanı 3 ile eklenen 4’ü çarpıp (3 × 4) ortalamaya eklemiş: 8 + 12.','islem')],
 'Yeni veri grubunun aritmetik ortalaması.',
 'Toplam ve terim sayısı değişirken ortalama ne olur? Önce çarpmanın, sonra eklemenin etkisini ayrı düşün.',
 [DON],
 [A('Çarpmanın etkisi','Her terim 3 katı olunca toplam da ortalama da 3 katı olur.','3 × 8 = 24'),A('Eklemenin etkisi','Her terime 4 eklenince ortalama 4 artar.','24 + 4 = 28'),A('Kontrol et','Örnek: 7, 9 → ortalama 8; 3x + 4 → 25, 31 → ortalama 28.','(25 + 31) ÷ 2 = 28')],
 'Her terime aynı işlem uygulanınca ortalama da aynı işlemden geçer: yeni ortalama = çarpan × eski ortalama + eklenen.')

# ================= 0007 · orta · iki şubenin birleşik ortalaması
n7a,o7a,n7b,o7b=24,65,16,80; t7=n7a*o7a+n7b*o7b; r7=Fr(t7,n7a+n7b)
assert t7==2840 and r7==71 and Fr(o7a+o7b,2)==Fr(145,2) and Fr(n7a*o7b+n7b*o7a,n7a+n7b)==74 and o7a+Fr(o7b-o7a)*Fr(n7b,n7a)==75
Q('0007','vri-agirlik','orta','Ağırlıklı Ortalama','İki grubun ortalamalarından ve kişi sayılarından birleşik ortalamayı hesaplar.','hikâyeli','K-VRI-02 (gruplu ortalama) · iki şubenin matematik sınavı',
 'Bir okulda 9-A sınıfındaki 24 öğrencinin matematik sınavı puanlarının aritmetik ortalaması 65, 9-B sınıfındaki 16 öğrencinin ortalaması 80’dir.\nBuna göre iki sınıftaki 40 öğrencinin sınav puanlarının aritmetik ortalaması kaçtır?',
 71,[(Fr(145,2),'İki sınıfın ortalamasını öğrenci sayılarını hesaba katmadan (65 + 80) ÷ 2 olarak almış.','bilgi'),(74,'Ağırlıkları ters eşleştirmiş: 65’i 16 ile, 80’i 24 ile çarpmış.','islem'),(75,'65 ile 80 arasındaki farkın 16 ÷ 24 kadarını 65’e eklemiş; oranı toplam kişiye (16 ÷ 40) göre almamış.','islem'),(2840,'Toplam puanı bulmuş ama 40 öğrenciye bölmeyi unutmuş.','dikkat')],
 'İki sınıfın birleşik puan ortalaması.',
 'Her sınıfın toplam puanını bulup birleştir; toplam öğrenci sayısına bölmek için sınıfların toplam puanına ihtiyacın var.',
 [ORT,AGR],
 [A('9-A’nın toplam puanı','Toplam = ortalama × kişi sayısı.','24 × 65 = 1 560'),A('9-B’nin toplam puanı','Aynı işlem.','16 × 80 = 1 280'),A('Birleşik ortalama','Toplam puanı toplam kişiye böl.','(1 560 + 1 280) ÷ 40 = 2 840 ÷ 40 = 71')],
 'İki grubun ortalaması, kişi sayılarıyla ağırlıklandırılarak birleştirilir; ortalamaların ortalaması alınmaz.')

# ================= 0008 · orta · eleman çıkarma (maaş)
n8,o8,o8y=6,30,27; c8=n8*o8-(n8-1)*o8y; assert c8==45 and o8-o8y==3 and o8+3==33 and (o8-o8y)*(n8-1)==15 and o8y+3*5==42
Q('0008','vri-ort','orta','Aritmetik Ortalama','Bir elemanın çıkarılması sonucu değişen ortalamadan çıkarılan elemanı bulur.','hikâyeli','K-VRI-01 (eleman çıkarma) · küçük bir ofisin maaşları',
 'Bir ofiste çalışan 6 kişinin aylık maaşlarının aritmetik ortalaması 30 bin TL’dir. Bu çalışanlardan biri işten ayrılınca kalan 5 kişinin maaşlarının aritmetik ortalaması 27 bin TL olmuştur.\nBuna göre işten ayrılan kişinin aylık maaşı kaç bin TL’dir?',
 45,[(3,'Ortalamalar arasındaki farkı (30 − 27) ayrılan kişinin maaşı sanmış.','dikkat'),(27,'Yeni ortalamayı ayrılan kişinin maaşı sanmış.','dikkat'),(33,'Ortalamanın 3 düştüğünü görüp ayrılanın maaşını ortalamanın 3 fazlası (30 + 3) almış.','bilgi'),(15,'Ortalamadaki düşüşü (3) kalan kişi sayısıyla (5) çarpıp ayrılanın maaşı sanmış.','islem')],
 'Ayrılan kişinin aylık maaşı (bin TL).',
 'İlk durumdaki toplam maaşı ve ayrıldıktan sonra kalan kişilerin toplam maaşını ayrı ayrı yaz.',
 [ORT],
 [A('İlk toplam','6 kişinin toplam maaşı.','6 × 30 = 180'),A('Kalanların toplamı','5 kişinin toplam maaşı.','5 × 27 = 135'),A('Ayrılanın maaşı','İki toplamın farkıdır.','180 − 135 = 45 bin TL')],
 'Bir terim çıkınca değişen toplam, çıkan terimin değeridir: ilk toplam − kalan toplam.')

# ================= 0009 · orta · ortalama = ortanca = tepe değer
d9=lambda x:[4,6,x,20,x]
sol9=[x for x in range(1,100) if ort(d9(x))==x and ortanca(d9(x))==x and tepe(d9(x))==[x]]; assert sol9==[10]
assert Fr(30,4)==Fr(15,2) and 30//2==15 and ortanca([6,20])==13
Q('0009','vri-birlikte','orta','Ortalama, Ortanca, Tepe Değer','Aritmetik ortalama, ortanca ve tepe değerin eşitliğinden bilinmeyen terimi bulur.','düz','K-VRI-04 (üç ölçünün eşitliği) · x’in iki kez geçtiği beş elemanlı veri',
 'x pozitif bir tam sayı olmak üzere 4, 6, x, 20, x veri grubunun aritmetik ortalaması, ortancası ve tepe değeri birbirine eşittir.\nBuna göre x kaçtır?',
 10,[(Fr(15,2),'Toplamda x’i yalnız bir kez sayıp (30 + x = 5x) x = 7,5 bulmuş.','islem'),(13,'Ortanca olarak 6 ile 20’nin ortalamasını alıp x’i ona eşitlemiş.','bilgi'),(15,'Toplamı 30 + 2x olarak yazıp 5 yerine yalnız x’li terim sayısına (2) bölerek 30 ÷ 2 = 15 bulmuş.','islem'),(20,'En büyük sayıyı (20) tepe değer sanıp x’i ona eşitlemiş.','bilgi')],
 'x’in değeri.',
 'Tepe değerin x olması için x kaç kez geçmeli? Ortalamayı x’e eşitlerken kaç terim olduğuna dikkat et.',
 [ORT,MED,MOD],
 [A('Tepe değer ve ortanca','x iki kez geçtiğinden tepe değerdir. Ortanca da x ise x, 4 ile 20 arasında ve sıralamada ortadadır.','4, 6, x, x, 20 → ortanca x (6 ≤ x ≤ 20)'),A('Ortalamayı yaz','Beş terimin ortalaması x olmalı.','(4 + 6 + 20 + 2x) ÷ 5 = x'),A('Çöz','Eşitliği düzenle.','30 + 2x = 5x ⇒ 3x = 30 ⇒ x = 10'),A('Kontrol et','10 koşulları sağlar.','4, 6, 10, 10, 20 → ortalama 10, ortanca 10, tepe değer 10')],
 'Ölçüler eşitse her biri için ayrı koşul yaz; ortalama eşitliği genellikle bilinmeyeni verir, ortanca ve tepe değer yerleşimi doğrular.')

# ================= 0010 · orta · ortanca verilip x
b11=[15,4,9,6,12]; assert sorted(b11)==[4,6,9,12,15]
s11=[x for x in range(1,60) if ortanca(b11+[x])==10]; assert s11==[11]
assert Fr(2*10-12)==8 and 2*10==20 and 6*10-(15+4+9+6+12)==14
Q('0010','vri-medmod','orta','Ortanca','Çift terimli bir veride ortancanın bilinen değerinden bilinmeyen terimi bulur.','hikâyeli','K-VRI-03 (ortanca verilip x) · antrenmandaki tur sayıları',
 'Bir atletizm antrenörü, 6 sporcunun bir antrenmanda attığı tur sayılarını 15, 4, 9, x, 6 ve 12 olarak kaydetmiştir. Bu veri grubunun ortancası 10’dur.\nBuna göre x pozitif tam sayısı kaçtır?',
 11,[(8,'Ortadaki ikiliyi 9 yerine 12 alıp 2 × 10 − 12 hesaplamış.','islem'),(10,'Ortancayı x’in kendisi sanmış.','dikkat'),(14,'Ortancayı aritmetik ortalama sanmış: 6 × 10 − (15 + 4 + 9 + 6 + 12) = 60 − 46 = 14.','bilgi'),(20,'Ortadaki iki sayının toplamının 2 × 10 = 20 olduğunu bulup 9’u çıkarmayı unutmuş.','dikkat')],
 'x’in değeri.',
 'Bilinen beş sayıyı sırala. 6 terimde ortadaki iki sayıdan biri x olmak zorunda mı, bu iki sayı hangileri olabilir?',
 [MED],
 [A('Bilinen sayıları sırala','4, 6, 9, 12, 15; ortancanın 10 olması için x yalnız 9 ile 12 arasında olabilir.','4, 6, 9, 12, 15'),A('Ortadaki ikiliyi belirle','x, 9 ile 12 arasındaysa 3. ve 4. terimler 9 ve x olur.','4, 6, 9, x, 12, 15'),A('Ortanca denklemi','İkilinin ortalaması 10 olmalı.','(9 + x) ÷ 2 = 10 ⇒ x = 11'),A('Kontrol','11, 9 ile 12 arasındadır; ortanca 10 olur.','4, 6, 9, 11, 12, 15 → (9 + 11) ÷ 2 = 10')],
 'Ortancası verilen çift terimli veride, bilinmeyenin sıradaki yerini ortancanın bulunduğu bölgeden bul, sonra ortanca denklemini yaz.')

# ================= 0011 · orta · açıklık verilip x
d12=[6,11,9,14]; s12=[x for x in range(0,200) if aciklik(d12+[x])==12]; assert s12==[2,18] and sum(s12)==20 and aciklik(d12)==8
Q('0011','vri-aciklik','orta','Açıklık','Açıklığı verilen veride bilinmeyen terimin en küçük ya da en büyük olma durumlarını ayrı inceler.','düz','K-VRI-05 (açıklık verilip x) · doğal sayı dizisi',
 'x bir doğal sayı olmak üzere 6, 11, 9, x, 14 veri grubunun açıklığı 12’dir.\nBuna göre x’in alabileceği değerlerin toplamı kaçtır?',
 20,[(2,'Yalnız x’in en küçük terim olduğu durumu (14 − x = 12) incelemiş.','dikkat'),(8,'x’i dikkate almadan mevcut açıklığı (14 − 6) yazmış.','dikkat'),(18,'Yalnız x’in en büyük terim olduğu durumu (x − 6 = 12) incelemiş.','dikkat'),(12,'Açıklık olan 12’yi x’in değeri sanmış.','dikkat')],
 'x’in alabileceği değerlerin toplamı.',
 'Veride x hariç en küçük ve en büyük terim hangileri? x bu terimlerin dışına çıkarsa açıklığı nasıl değişir?',
 [ACK],
 [A('Mevcut açıklık','x dışındaki en küçük 6, en büyük 14’tür.','14 − 6 = 8 (≠ 12)'),A('x en küçükse','Açıklık 14 − x olur.','14 − x = 12 ⇒ x = 2'),A('x en büyükse','Açıklık x − 6 olur.','x − 6 = 12 ⇒ x = 18'),A('Değerleri topla','İki değer de doğal sayıdır.','2 + 18 = 20')],
 'Açıklığı verilen veride bilinmeyen, ya yeni en küçük ya da yeni en büyük terim olur; iki durumu da ayrı ayrı çöz.')

# ================= 0012 · orta · çeyrekler açıklığı
d13=[14,3,22,9,17,5,11,16,8]; sd13=sorted(d13); assert sd13==[3,5,8,9,11,14,16,17,22] and ceyrekA(d13)==10
q1=ortanca(sd13[:4]); q3=ortanca(sd13[5:]); assert (q1,q3)==(Fr(13,2),Fr(33,2))
assert ortanca(sd13[:5])==8 and ortanca(sd13[4:])==16 and 16-8==8 and aciklik(d13)==19
Q('0012','vri-aciklik','orta','Çeyrekler Açıklığı','Tek sayıda terimli bir veride ortancayı iki yarıya katmadan çeyrekler açıklığını hesaplar.','hikâyeli','K-VRI-05 (çeyrekler açıklığı) · atış yarışması puanları',
 'Bir atış yarışmasında 9 sporcunun aldığı puanlar 14, 3, 22, 9, 17, 5, 11, 16 ve 8’dir.\nSıralı bir veri grubunda ortanca, grubu alt ve üst olmak üzere iki yarıya ayırır (terim sayısı tek ise ortanca iki yarıya da katılmaz). Alt yarının ortancasına Q1, üst yarının ortancasına Q3 denir ve çeyrekler açıklığı Q3 − Q1 olarak tanımlanır.\nBuna göre bu veri grubunun çeyrekler açıklığı kaçtır?',
 10,[(Fr(13,2),'Yalnız Q1’i (6,5) bulup cevap olarak yazmış.','dikkat'),(8,'Ortancayı (11) iki yarıya da katmış: Q1 = 8, Q3 = 16.','bilgi'),(Fr(33,2),'Yalnız Q3’ü (16,5) bulup cevap olarak yazmış.','dikkat'),(19,'Çeyrekler açıklığı yerine açıklığı (22 − 3) bulmuş.','bilgi')],
 'Veri grubunun çeyrekler açıklığı.',
 'Önce veriyi sırala, ortancayı işaretle ve alt ile üst yarıları ayrı ayrı yaz.',
 [CEY],
 [A('Sırala','Dokuz sayıyı küçükten büyüğe diz.','3, 5, 8, 9, 11, 14, 16, 17, 22'),A('Yarılara ayır','Ortanca 5. terim (11); iki yarıya katılmaz.','Alt yarı: 3, 5, 8, 9 · Üst yarı: 14, 16, 17, 22'),A('Q1 ve Q3','Her yarının ortancası.','Q1 = (5 + 8) ÷ 2 = 6,5 · Q3 = (16 + 17) ÷ 2 = 16,5'),A('Farkı al','Çeyrekler açıklığı Q3 − Q1.','16,5 − 6,5 = 10')],
 'Terim sayısı tekse ortancayı iki yarıya katma; Q1 ve Q3’ü yarıların ortancalarından bul.')

# ================= 0013 · orta · standart sapma hesabı
d15=[2,3,3,5,7]; assert ort(d15)==4 and sum((x-4)**2 for x in d15)==16 and varyans(d15)==4 and sd(d15)==2
assert Fr(16,5)==Fr(16,5) and Fr(sum(abs(x-4) for x in d15),5)==Fr(8,5)
Q('0013','vri-sapma','orta','Standart Sapma','Küçük bir veri grubunun standart sapmasını tanıma göre hesaplar.','hikâyeli','K-VRI-06 (standart sapma hesabı) · beş denemedeki yanlış sayıları',
 'Bir öğrenci, bir ders için girdiği beş denemede sırasıyla 2, 3, 3, 5 ve 7 yanlış yapmıştır.\nBir veri grubunda her verinin aritmetik ortalamadan farkının karesi alınıp bu kareler toplanır; toplam (veri sayısı − 1)’e bölünür ve sonucun kareköküne standart sapma denir.\nBuna göre bu öğrencinin yanlış sayılarının standart sapması kaçtır?',
 2,[(Fr(8,5),'Farkların mutlak değerlerinin ortalamasını (8 ÷ 5) bulmuş.','bilgi'),(Fr(16,5),'Kareler toplamını (veri sayısı − 1) yerine 5’e bölüp kök almayı bırakmış.','islem'),(4,'Kareler toplamını 4’e bölüp kök almayı unutmuş (varyans).','dikkat'),(16,'Yalnız farkların karelerinin toplamını bulup durmuş.','dikkat')],
 'Yanlış sayılarının standart sapması.',
 'Önce aritmetik ortalamayı bul; sonra her verinin ortalamadan farkını yaz.',
 [STD],
 [A('Ortalama','Beş verinin toplamı 20.','20 ÷ 5 = 4'),A('Ortalamadan farklar','Her veriden 4 çıkar.','−2, −1, −1, 1, 3'),A('Karelerin toplamı','Farkların karelerini topla.','4 + 1 + 1 + 1 + 9 = 16'),A('Standart sapma','(n − 1) = 4’e böl, kök al.','√(16 ÷ 4) = √4 = 2')],
 'Standart sapma = √(farkların kareleri toplamı ÷ (n − 1)); kök almayı ve doğru bölenle bölmeyi unutma.')

# ================= 0014 · orta · öncüllü dönüşüm (y = 2x + 3)
d14=[3,5,6,10,11]; y14=[2*x+3 for x in d14]
T1=ort(y14)==2*ort(d14)+3; T2=aciklik(y14)==2*aciklik(d14); T3=(varyans(y14)==4*varyans(d14) and abs(stt.stdev(y14)-2*stt.stdev(d14))<1e-9)
T3b=abs(stt.stdev(y14)-(2*stt.stdev(d14)+3))<1e-9
assert T1 and T2 and T3 and not T3b and ort(d14)==7 and ort(y14)==17 and aciklik(d14)==8 and aciklik(y14)==16
Q('0014','vri-donusum','orta','Veriyi Dönüştürme','Her veriye aynı doğrusal işlem uygulandığında ortalama, açıklık ve standart sapmanın nasıl değiştiğini ayırt eder.','öncüllü','K-VRI-07 (y = 2x + 3 dönüşümü, öncüllü) · ortalama, açıklık, standart sapma',
 'Bir veri grubundaki her x değeri için y = 2x + 3 işlemi uygulanarak yeni bir veri grubu oluşturulmuştur.\nI. Yeni grubun aritmetik ortalaması, eski grubun ortalamasının 2 katından 3 fazladır.\nII. Yeni grubun açıklığı, eski grubun açıklığının 2 katıdır.\nIII. Yeni grubun standart sapması, eski grubun standart sapmasının 2 katından 3 fazladır.\nBuna göre bu ifadelerden hangileri her zaman doğrudur?',
 'I ve II',sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],
 yan=[('Yalnız I','Açıklıkta da toplanan 3’ün etkili olduğunu sanıp II’yi yanlış saymış; yalnız I’i doğru bulmuş.','bilgi'),('Yalnız II','Ortalamanın da aynı işlemden geçtiğini bilmeyip I’i yanlış saymış.','bilgi'),('II ve III','Standart sapmaya da +3’ün uygulanacağını sanıp III’ü doğru, ortalamayı bozulmaz sanıp I’i yanlış saymış.','bilgi'),('I, II ve III','Standart sapmanın da ortalama gibi 2x + 3 işleminden geçeceğini sanmış; toplama standart sapmayı etkilemez.','bilgi')],
 istenen='Her zaman doğru olan ifadeler.',
 ip='Örnek bir veri grubunda (ör. 3, 5, 7) üç ölçüyü önce, sonra dönüşümden sonra karşılaştır. Toplanan sabit hangi ölçüleri etkiler?',
 bilgi=[DON],
 ad=[A('I. ifade','Ortalama, verilerle aynı işlemden geçer.','ort(y) = 2 × ort(x) + 3 → doğru'),A('II. ifade','Açıklık fark olduğu için toplanan 3 sadeleşir, çarpan kalır.','(2 × maks + 3) − (2 × min + 3) = 2 × açıklık → doğru'),A('III. ifade','Sapmalar ortalamadan farklardır; 3 eklemesi farkları değiştirmez, çarpan 2 farkları 2 katına çıkarır.','s(y) = 2 × s(x), +3 yok → yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')],
 puf='Verilere sabit eklemek yayılım ölçülerini (açıklık, standart sapma) değiştirmez; çarpmak onları |çarpan| katına çıkarır.')

# ================= 0015 · kolay · iki terimin toplamı (sipariş)
n15,o15,y15=10,12,13; top15=n15*o15-(n15-2)*y15; assert top15==16
assert y15-o15==1 and (n15-2)*y15==104 and n15*y15-n15*o15==10 and Fr(top15,2)==8
Q('0015','vri-ort','kolay','Aritmetik Ortalama','Terim çıkarılınca değişen ortalamadan çıkarılan terimlerin toplamını bulur.','hikâyeli','K-VRI-01 (iki terimin toplamı) · çiçekçinin haftalık siparişleri',
 'Bir çiçekçi 10 hafta boyunca haftalık sipariş sayısını kaydetmiş ve ortalamasını 12 bulmuştur. Bayram haftası olan iki hafta kayıttan çıkarılınca kalan 8 haftanın sipariş sayılarının aritmetik ortalaması 13 olmuştur.\nBuna göre kayıttan çıkarılan iki haftanın sipariş sayıları toplamı kaçtır?',
 16,[(1,'Ortalamalar arasındaki farkı (13 − 12) çıkarılan toplam sanmış.','dikkat'),(8,'Çıkarılan iki haftanın toplamı yerine ortalamasını (16 ÷ 2) vermiş.','dikkat'),(10,'Kalan toplamı 8 yerine 10 haftayla (10 × 13) kurmuş: 130 − 120.','islem'),(104,'Kalan 8 haftanın toplamını (8 × 13) çıkarılanların toplamı sanmış.','dikkat')],
 'Kayıttan çıkarılan iki haftanın sipariş sayıları toplamı.',
 'İlk durumdaki toplamı ve kalan haftaların toplamını ayrı ayrı yaz.',
 [ORT],
 [A('İlk toplam','10 haftanın toplamı.','10 × 12 = 120'),A('Kalan toplam','8 haftanın toplamı.','8 × 13 = 104'),A('Çıkarılanların toplamı','İki toplamın farkıdır.','120 − 104 = 16')],
 'Çıkarılan terimlerin toplamı, ilk toplam ile kalan toplamın farkıdır.')

# ================= 0016 · orta · ağırlıklı ortalama, hedef (ders)
w=(2,3,5); p16=(70,80); h16=78; e16=Fr(h16*sum(w)-w[0]*p16[0]-w[1]*p16[1],w[2]); assert e16==80
assert Fr(w[0]*p16[0]+w[1]*p16[1]+w[2]*e16,sum(w))==h16
assert 3*h16-sum(p16)==84 and h16*10-w[0]*p16[0]-w[1]*p16[1]==400 and Fr(400,10)==40 and Fr(h16*10-3*70-2*80,5)==82 and Fr(h16*10-5*70-3*80,2)==95
Q('0016','vri-agirlik','orta','Ağırlıklı Ortalama','Ağırlıklı ortalama koşulundan eksik notu hesaplar.','hikâyeli','K-VRI-02 (ağırlıklı ortalama, hedef not) · ders geçme notu',
 'Bir derste dönem puanı, 1. yazılı, 2. yazılı ve proje notlarının sırasıyla 2, 3 ve 5 ağırlıkla alınan ağırlıklı aritmetik ortalamasıdır. Bir öğrenci 1. yazılıdan 70, 2. yazılıdan 80 almıştır.\nÖğrencinin dönem puanının 78 olması için proje notu kaç olmalıdır?',
 80,[(40,'Proje katkısını (780 − 380 = 400) projenin ağırlığı 5 yerine ağırlıklar toplamı olan 10’a bölmüş.','islem'),(82,'Ağırlıkları yanlış eşleştirmiş: 1. yazılıya 3, 2. yazılıya 2 vermiş.','islem'),(84,'Ağırlıkları hiç kullanmamış: 3 × 78 − (70 + 80) hesaplamış.','bilgi'),(95,'Ağırlıkları tersine eşleştirmiş (5, 3, 2) ve proje ağırlığını 2 almış.','islem')],
 'Dönem puanının 78 olması için gereken proje notu.',
 'Ağırlıklar toplamı kaç? Dönem puanının ağırlıklarla çarpımını yazıp bilinenleri ayır.',
 [AGR],
 [A('Ağırlıklı toplam','Dönem puanı 78 ve ağırlıklar toplamı 2 + 3 + 5 = 10.','78 × 10 = 780'),A('Bilinen notların katkısı','1. ve 2. yazılı ağırlıklarıyla çarpılır.','2 × 70 + 3 × 80 = 140 + 240 = 380'),A('Projenin katkısı','Toplamdan çıkar.','780 − 380 = 400'),A('Proje notu','Projenin ağırlığı 5.','400 ÷ 5 = 80')],
 'Ağırlıklı ortalamada her notu ağırlığıyla çarp; hedef toplamı (ortalama × ağırlıklar toplamı) kur, bilinenleri çıkar.')

# ================= 0017 · orta · tablo, ortalama (basketbol)
pr17=[(60,2),(70,5),(80,8),(90,3),(100,2)]; d17=tabdizi(pr17); assert len(d17)==20 and ort(d17)==79 and sum(a*b for a,b in pr17)==1580
assert ort([a for a,_ in pr17])==80 and Fr(1580,5)==316 and ort([b for _,b in pr17])==4
SK=tablo_svg(['Attığı sayı','Maç sayısı'],[[str(a),str(b)] for a,b in pr17])
Q('0017','vri-sekil','kolay','Tablodan Ortalama','Sıklık tablosundaki değerleri sıklıklarıyla çarparak aritmetik ortalamayı hesaplar.','tablo','K-VRI-08 (tablodan ortalama) · basketbolcunun maçlardaki sayıları',
 'Bir basketbolcunun bir sezonda oynadığı 20 maçta attığı sayılar ve bu sayıları kaç maçta attığı aşağıdaki tabloda verilmiştir.\nBuna göre basketbolcunun maç başına attığı sayıların aritmetik ortalaması kaçtır?',
 79,[(4,'Sıklıkların (maç sayılarının) ortalamasını (20 ÷ 5) bulmuş.','dikkat'),(80,'Tablodaki sayıların (60, 70, 80, 90, 100) basit ortalamasını almış; sıklıkları hesaba katmamış.','bilgi'),(316,'Toplam sayıyı 20 maça değil, tablodaki 5 satıra bölmüş.','islem'),(1580,'Toplam sayıyı bulmuş ama maç sayısına bölmeyi unutmuş.','dikkat')],
 'Maç başına atılan sayıların aritmetik ortalaması.',
 'Her satırdaki sayıyı o sayıyı kaç maçta attığıyla çarp; toplam maç sayısını da ayrıca bul.',
 [SIK,ORT],
 [A('Toplam maç','Sıklıkların toplamı.','2 + 5 + 8 + 3 + 2 = 20'),A('Toplam sayı','Her sayıyı sıklığıyla çarpıp topla.','60 × 2 + 70 × 5 + 80 × 8 + 90 × 3 + 100 × 2 = 120 + 350 + 640 + 270 + 200 = 1 580'),A('Ortalama','Toplam sayıyı maç sayısına böl.','1 580 ÷ 20 = 79')],
 'Sıklık tablosunda ortalama = (her değer × kendi sıklığı)’nın toplamı ÷ sıklıkların toplamı.',sekil=SK)

# ================= 0018 · orta · tablo, ortanca ve tepe değer farkı (kütüphane)
pr18=[(1,5),(2,10),(3,3),(4,11),(5,1)]; d18=tabdizi(pr18); assert len(d18)==30 and ortanca(d18)==Fr(5,2) and tepe(d18)==[4]
assert sorted(d18)[14]==2 and sorted(d18)[15]==3 and 4-Fr(5,2)==Fr(3,2) and 4-3==1 and 4-2==2
SK=tablo_svg(['Ödünç alınan kitap sayısı','Üye sayısı'],[[str(a),str(b)] for a,b in pr18])
Q('0018','vri-medmod','orta','Tablodan Ortanca ve Tepe Değer','Birikimli sıklıkla ortanca konumunu bulup tepe değerle karşılaştırır.','tablo','K-VRI-03 (tablodan ortanca ve tepe değer) · kütüphane üyelerinin ödünç aldığı kitaplar',
 'Bir kütüphanenin 30 üyesinin bir ayda ödünç aldığı kitap sayıları ve bu kadar kitap alan üye sayıları aşağıdaki tabloda verilmiştir.\nBuna göre tepe değer ile ortancanın farkı kaçtır?',
 Fr(3,2),[(1,'Ortancayı 16. terim olan 3 alıp ortadaki iki terimin ortalamasını almamış.','bilgi'),(2,'Ortancayı 15. terim olan 2 alıp ortadaki iki terimin ortalamasını almamış.','bilgi'),(Fr(5,2),'Tepe değer yerine ortancayı sonuç yazmış.','dikkat'),(4,'Farkı hesaplamak yerine tepe değeri (4) yazmış.','dikkat')],
 'Tepe değer ile ortancanın farkı.',
 'Üye sayıları toplamı 30; ortanca hangi sıradaki terimlerin ortalamasıdır? Birikimli sıklığı yaz.',
 [MED,MOD,SIK],
 [A('Tepe değer','En büyük sıklık 11 olan kitap sayısı.','Tepe değer = 4'),A('Birikimli sıklık','Değerleri sıraladıkça kaç veri geçildiğine bak.','1 → 5 · 2 → 15 · 3 → 18 · 4 → 29 · 5 → 30'),A('Ortanca','30 veri var; 15. ve 16. terim ortadadır. 15. terim 2, 16. terim 3’tür.','(2 + 3) ÷ 2 = 2,5'),A('Fark','Tepe değerden ortancayı çıkar.','4 − 2,5 = 1,5')],
 'Sıklık tablosunda ortancayı bulmak için birikimli sıklığı yaz ve ortadaki sıra numarasını bul.',sekil=SK)

# ================= 0019 · orta · tablo, eksik sıklık (kardeş sayısı)
def d19(x): return tabdizi([(0,x),(1,8),(2,6),(3,2)])
s19=[x for x in range(1,100) if ort(d19(x))==Fr(13,10)]; assert s19==[4]
assert sum(a*b for a,b in [(1,8),(2,6),(3,2)])==26 and 26+0==26 and 8+6+2==16 and 20-(8+6)==6
SK=tablo_svg(['Kardeş sayısı','Öğrenci sayısı'],[['0','x'],['1','8'],['2','6'],['3','2']])
Q('0019','vri-sekil','orta','Tablodan Eksik Sıklık','Aritmetik ortalaması verilen bir sıklık tablosunda bilinmeyen sıklığı bulur.','tablo','K-VRI-08 (tablodan eksik sıklık) · öğrencilerin kardeş sayıları',
 'Bir sınıftaki öğrencilerin kardeş sayıları ve bu kadar kardeşi olan öğrenci sayıları aşağıdaki tabloda verilmiştir. Hiç kardeşi olmayan öğrenci sayısı x’tir ve sınıftaki öğrencilerin kardeş sayılarının aritmetik ortalaması 1,3’tür.\nBuna göre x kaçtır?',
 4,[(6,'Toplam öğrenciyi 26 ÷ 1,3 = 20 bulup bilinen öğrencilerden yalnız 8 + 6’yı çıkarmış; 3 kardeşli 2 öğrenciyi unutmuş: 20 − 14 = 6.','dikkat'),(16,'Tabloda bilinen öğrenci sayılarının toplamını (8 + 6 + 2) x sanmış.','dikkat'),(20,'Toplam öğrenci sayısını (26 ÷ 1,3 = 20) x olarak yazmış.','dikkat'),(26,'Toplam kardeş sayısını (8 + 12 + 6) x sanmış.','dikkat')],
 'Hiç kardeşi olmayan öğrenci sayısı x.',
 'Toplam kardeş sayısını ve toplam öğrenci sayısını (x cinsinden) yaz; ortalama bu ikisinin oranıdır.',
 [SIK,ORT],
 [A('Toplam kardeş sayısı','Her kardeş sayısını öğrenci sayısıyla çarp; 0 kardeşliler katkı vermez.','0 × x + 1 × 8 + 2 × 6 + 3 × 2 = 26'),A('Toplam öğrenci','Sıklıkların toplamı.','x + 8 + 6 + 2 = x + 16'),A('Ortalama denklemi','Toplam kardeş ÷ toplam öğrenci = 1,3.','26 ÷ (x + 16) = 1,3 ⇒ x + 16 = 20'),A('x’i bul','Denklemi çöz.','x = 4')],
 'Sıklık tablosunda bilinmeyen sıklık varsa toplam değeri ve toplam sıklığı x cinsinden yaz, ortalama eşitliğiyle çöz.',sekil=SK)

# ================= 0020 · orta · sütun grafiği, ortalama – ortanca
g20=[20,60,100,40,40]; e20=['Pzt','Sal','Çar','Per','Cum']; assert ort(g20)==52 and ortanca(g20)==40 and ort(g20)-ortanca(g20)==12
assert abs(ort(g20)-g20[2])==48 and ort(g20)+ortanca(g20)==92 and tepe(g20)==[40]
SK=tek(sutun(e20,g20,20,100,'Bardak','Gün'))
Q('0020','vri-sekil','orta','Sütun Grafiği Ortalama ve Ortanca','Sütun grafiğinden okunan değerlerin ortalamasını ve ortancasını karşılaştırır.','grafik','K-VRI-08 (sütun grafiği, ortalama–ortanca) · limonata standının satışları',
 'Bir limonata standında bir haftanın ilk beş günü satılan bardak sayıları aşağıdaki sütun grafiğinde gösterilmiştir.\nBuna göre bu veri grubunun aritmetik ortalaması ile ortancasının farkı kaçtır?',
 12,[(40,'Farkı bulmak yerine yalnız ortancayı yazmış.','dikkat'),(48,'Verileri sıralamadan ortadaki sütunu (Çarşamba, 100) ortanca sanıp ortalamayla farkını (100 − 52) almış.','dikkat'),(52,'Farkı bulmak yerine yalnız ortalamayı yazmış.','dikkat'),(92,'Ortalama ile ortancayı çıkarmak yerine toplamış.','dikkat')],
 'Aritmetik ortalama ile ortancanın farkı.',
 'Beş sütunun değerlerini okuyup liste yap. Ortanca için sıralama gerekir.',
 [GRF,ORT,MED],
 [A('Değerleri oku','Sütunların yükseklikleri.','20, 60, 100, 40, 40'),A('Ortalama','Toplam 260, 5 gün.','260 ÷ 5 = 52'),A('Ortanca','Sıralanmış: 20, 40, 40, 60, 100; ortadaki 3. terim.','Ortanca = 40'),A('Fark','Ortalamadan ortancayı çıkar.','52 − 40 = 12')],
 'Grafikteki sütun sırası ortancayı vermez; değerleri okuyup önce sırala.',sekil=SK)

# ================= 0021 · orta · çizgi grafiği, öncüllü (sıcaklık)
g21=[12,16,10,18,16,14,12]; e21=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz']
assert ort(g21)==14 and ortanca(g21)==14 and tepe(g21)==[12,16] and aciklik(g21)==8
SK=tek(cizgi(e21,g21,2,20,'Sıcaklık (°C)','Gün'))
Q('0021','vri-sekil','orta','Çizgi Grafiği Ölçüleri','Çizgi grafiğinden okunan veride ortalama, ortanca, tepe değer ve açıklıkla ilgili ifadeleri değerlendirir.','öncüllü','K-VRI-08 (çizgi grafiği, ölçülerin yorumu) · bir haftanın en yüksek sıcaklıkları',
 'Bir kentte bir haftanın günlük en yüksek sıcaklıkları (°C) aşağıdaki çizgi grafiğinde gösterilmiştir.\nI. Sıcaklıkların aritmetik ortalaması ortancasına eşittir.\nII. Veri grubunun tek bir tepe değeri vardır ve bu 16’dır.\nIII. Veri grubunun açıklığı 8 °C’dir.\nBuna göre bu ifadelerden hangileri doğrudur?',
 'I ve III',sira=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],
 yan=[('Yalnız I','Açıklığı 18 − 12 = 6 hesaplayıp (en küçük sıcaklığı 12 sanarak) III’ü yanlış saymış.','dikkat'),('Yalnız III','Ortalama ile ortancanın eşit olduğunu görmeyip I’i yanlış saymış (ortancayı sıralamadan okumuş).','islem'),('I ve II','12 ve 16 iki kez geçtiği hâlde 16’yı tek tepe değer sanmış; açıklığı da kontrol etmemiş.','bilgi'),('II ve III','Ortalamayı yanlış (örn. 15) bulup I’i yanlış saymış; 16’nın tek tepe değer olduğunu sanmış.','islem')],
 istenen='Doğru olan ifadeler.',
 ip='Yedi sıcaklığı okuyup listele; her ifadeyi ayrı ayrı bu listeden kontrol et. Hangi değerler kaç kez geçiyor?',
 bilgi=[GRF,MOD],
 ad=[A('Değerleri oku','Noktaların yükseklikleri.','12, 16, 10, 18, 16, 14, 12'),A('I. ifade','Toplam 98; ortalama 98 ÷ 7. Sıralı: 10, 12, 12, 14, 16, 16, 18; ortanca 4. terim.','Ortalama = 14, ortanca = 14 → doğru'),A('II. ifade','12 ve 16 ikişer kez geçer; ikisi de tepe değerdir.','Tepe değerler 12 ve 16 → yanlış'),A('III. ifade','En büyük 18, en küçük 10.','18 − 10 = 8 → doğru')],
 puf='Tepe değer birden fazla olabilir; “tek tepe değer” iddiasında en yüksek sıklığa sahip tüm değerleri say.',sekil=SK)

# ================= 0022 · orta · iki grubun birleşik ortalaması, kişi sayısı bulma (kurs)
n22a,o22a,o22b,o22=8,42,36,38; nb=Fr(n22a*(o22a-o22),o22-o22b); assert nb==16
assert Fr(n22a*o22a+nb*o22b,n22a+nb)==38 and Fr(n22a*(o22-o22b),o22a-o22)==4 and o22a-o22b==6 and n22a*(o22a-o22)==32
Q('0022','vri-agirlik','orta','Gruplu Ortalama','İki grubun ve birleşik grubun ortalamalarından bilinmeyen grup büyüklüğünü bulur.','hikâyeli','K-VRI-02 (gruplu ortalama, kişi sayısı bulma) · kursun sabah ve akşam grupları',
 'Bir kursta sabah grubunda 8 kişi vardır ve bu grubun yaş ortalaması 42’dir. Akşam grubunun yaş ortalaması 36’dır. Kursun bütün katılımcılarının yaş ortalaması 38’dir.\nBuna göre akşam grubunda kaç kişi vardır?',
 16,[(4,'Ortalamaya yakınlık oranını ters kurup (42 − 38) : (38 − 36) = 2 : 1 oranının tersiyle 8 ÷ 2 hesaplamış.','islem'),(6,'İki grubun ortalama farkını (42 − 36) kişi sayısı sanmış.','dikkat'),(8,'Birleşik ortalamanın iki ortalamanın tam ortasında olmadığını görmeyip grupları eşit büyüklükte sanmış.','bilgi'),(32,'Sabah grubunun sayısını ortalama farkıyla (8 × 4) çarpmış; (38 − 36) = 2’ye bölmeyi unutmuş.','islem')],
 'Akşam grubundaki kişi sayısı.',
 'Akşam grubunun kişi sayısına b de; üç ortalamayı toplam yaşlarla ilişkilendirip denklem kur.',
 [ORT,AGR],
 [A('Sabah grubunun toplam yaşı','Toplam = ortalama × kişi.','8 × 42 = 336'),A('Akşam grubu ve toplam','Akşam grubunda b kişi olsun; tüm katılımcıların toplam yaşı 38 × (8 + b).','336 + 36b = 38 × (8 + b)'),A('Denklemi çöz','Parantezi aç.','336 + 36b = 304 + 38b ⇒ 32 = 2b'),A('Kişi sayısı','b’yi bul.','b = 16')],
 'Gruplu ortalamada toplam değerleri (ortalama × kişi sayısı) yazıp birleşik ortalamayla eşitle.')

# ================= 0023 · zor · ortalama, ortanca, tepe değer koşulları, en büyük elemanın en çok değeri
mxs=[]
for dd in range(1,36):
    for e in range(1,60):
        l=[3,3,5,dd,e]
        if sorted(l)==l and tepe(l)==[3] and ort(l)==7: mxs.append((dd,e))
assert max(e for _,e in mxs)==18 and min(e for _,e in mxs)==13 and (6,18) in mxs and (5,19) not in mxs and (12,12) not in mxs and tepe([3,3,5,12,12])==[3,12]
assert 35-3-3-5-5==19 and 35-3-3-5==24 and 35-3-3-5-1==23 and 24//2==12 and 12+12==24
Q('0023','vri-birlikte','zor','Ortalama, Ortanca, Tepe Değer','Tepe değerin tek olması, ortancanın ve ortalamanın verilmesi koşullarını birlikte kullanarak en büyük terimin alabileceği en büyük değeri bulur.','düz','K-VRI-04 (tepe değer–ortanca–ortalama birlikte, en büyük terim) · beş elemanlı pozitif tam sayı grubu',
 'Küçükten büyüğe doğru sıralanmış beş elemanlı bir veri grubunun elemanları pozitif tam sayılardır. Bu veri grubunun tek bir tepe değeri vardır ve bu değer 3’tür. Ortancası 5, aritmetik ortalaması 7’dir.\nBuna göre bu veri grubunun en büyük elemanı en çok kaç olabilir?',
 18,[(12,'Dördüncü ve beşinci elemanı eşit paylaştırmış (12 ve 12); bu durumda 12 de iki kez geçer, tepe değer tek olmaz ve en büyük değer de aranmamış olur.','dikkat'),(19,'4. elemanı 5 almış; 5 iki kez geçeceği için tepe değer yalnız 3 olmaz.','dikkat'),(23,'Eleman toplamından yalnız 3, 3 ve 5’i çıkarıp 4. elemanı 1 almış; ama sıralamada 4. eleman ortancadan küçük olamaz.','bilgi'),(24,'Eleman toplamından 3, 3 ve 5’i çıkarıp 4. elemanı hiç saymamış.','dikkat')],
 'En büyük elemanın alabileceği en büyük değer.',
 'Ortancanın ve sıralamanın 3. ve 4. elemanı hakkında ne söylediğine bak; 3’ün tek tepe değer olması başka hangi sayıların kaç kez geçebileceğini kısıtlar?',
 [MED,MOD,ORT],
 [A('Sıralamayı yaz','Tepe değer 3 en az 2 kez geçer; ortanca 3. terim olan 5’tir.','3, 3, 5, d, e (3 ≤ 3 ≤ 5 ≤ d ≤ e)'),A('Toplamı kullan','Ortalama 7 olduğundan toplam 35 olmalıdır.','3 + 3 + 5 + d + e = 35 ⇒ d + e = 24'),A('d’yi kısıtla','d ≥ 5 olmalı; d = 5 olursa 5 de iki kez geçer ve tepe değer yalnız 3 olmaz. Bu yüzden d ≥ 6.','d ≥ 6'),A('e’yi büyük yap','e’nin en büyük olması için d en küçük alınır.','d = 6 ⇒ e = 18'),A('Kontrol et','3, 3, 5, 6, 18 → ortalama 7, ortanca 5, tek tepe değer 3.','e en çok 18')],
 puf='Tepe değerin “tek” olması, öteki değerlerin tekrar sayısını sınırlar; bu sınırı atlarsan uç değer yanlış çıkar.')

# ================= 0024 · zor · sütun grafiği, çizilmeyen sütun (ortalama = ortanca)
k24=[30,90,None,20,50]; e24=['Pzt','Sal','Çar','Per','Cum']
c24=[x for x in range(1,101) if ort([v if v else x for v in k24])==ortanca([v if v else x for v in k24])]
assert c24==[60]
assert Fr(190,4)==Fr(95,2) and 4*50-190==10 and 30+90+20+50==190 and 5*50-210==40
SK=tek(sutun_h(e24,k24,10,100,'Satış (adet)','Gün'))
Q('0024','vri-sekil','zor','Sütun Grafiği Eksik Sütun','Ortalama ile ortancanın eşitliğinden grafikte gösterilmeyen sütunun değerini sıralamayı da gözeterek bulur.','grafik','K-VRI-08 (eksik sütun, ortalama = ortanca) · bir mağazanın günlük satışları',
 'Bir mağazanın bir haftanın ilk beş günü sattığı ürün adetleri aşağıdaki sütun grafiğinde gösterilmiştir. Çarşamba gününe ait sütun çizilmemiş, “?” ile belirtilmiştir. Çarşamba günü satılan ürün adedi pozitif bir tam sayıdır ve beş günün satış adetlerinin aritmetik ortalaması, ortancasına eşittir.\nBuna göre Çarşamba günü kaç adet ürün satılmıştır?',
 60,[(10,'Toplamı 5 yerine 4 terime göre kurmuş: 4 × 50 − 190.','islem'),(47,'x’i ortanca sanıp 190 = 4x denkleminden 47,5 bulmuş; tam sayı olması gerektiğini görmeden yuvarlamış.','dikkat'),(50,'Ortancayı (50) bulup Çarşamba değerinin de ortanca kadar olduğunu sanmış.','bilgi'),(40,'Bilinen sütunların toplamını yanlış (210) toplayıp 250 − 210 hesaplamış.','islem')],
 'Çarşamba günü satılan ürün adedi.',
 'x’in sıralamadaki yerine göre ortancanın hangi değer olabileceğini düşün; ortalamayı x cinsinden yaz.',
 [GRF,ORT,MED],
 [A('Bilinen değerler','Grafikten okunan dört sütun.','30, 90, 20, 50 (toplam 190)'),A('Ortalamayı yaz','Beş günün ortalaması x’e bağlıdır.','Ortalama = (190 + x) ÷ 5'),A('Durumları incele','x ≤ 30 iken ortanca 30: (190 + x) ÷ 5 = 30 ⇒ x = −40 olamaz. 30 ≤ x ≤ 50 iken ortanca x: 190 = 4x ⇒ x = 47,5 tam sayı değil. x ≥ 50 iken ortanca 50.','x ≥ 50 durumu kalır'),A('x ≥ 50 durumunda çöz','Ortalama 50 olmalı.','(190 + x) ÷ 5 = 50 ⇒ x = 60'),A('Kontrol et','60, 50 ile 90 arasında olduğundan ortanca gerçekten 50’dir.','20, 30, 50, 60, 90 → ortalama 50, ortanca 50')],
 puf='Ortalama ve ortanca birlikte verildiğinde bilinmeyenin sıradaki yerine göre durumları ayrı ayrı dene ve sonucu sıralamayla doğrula.',sekil=SK)

# ================= 0025 · orta · standart sapma ve dönüşüm (satış)
d25=[2,2,10,14]; assert ort(d25)==7 and sum((x-7)**2 for x in d25)==108 and sd(d25)==6
y25=[2*x-3 for x in d25]; assert sd(y25)==12 and 2*6-3==9 and varyans(d25)==36 and 2*36==72
Q('0025','vri-sapma','orta','Standart Sapma','Küçük bir veri grubunun standart sapmasını hesaplayıp doğrusal dönüşümdeki değişimini bulur.','hikâyeli','K-VRI-06 (standart sapma hesabı ve dönüşüm) · dört günlük satışlar',
 'Bir mağazada ardışık 4 günde satılan ürün sayıları 2, 2, 10 ve 14’tür. Bu satış sayılarının her biri 2 ile çarpılıp 3 çıkarılarak yeni bir veri grubu oluşturulmuştur.\nBir veri grubunda her verinin aritmetik ortalamadan farkının karesi alınıp bu kareler toplanır; toplam (veri sayısı − 1)’e bölünür ve sonucun kareköküne standart sapma denir.\nBuna göre yeni veri grubunun standart sapması kaçtır?',
 12,[(6,'Yeni grubun değil, ilk grubun standart sapmasını vermiş (çarpmanın etkisini unutmuş).','dikkat'),(9,'Standart sapmaya da dönüşümü uygulamış: 2 × 6 − 3.','bilgi'),(36,'Yeni grubun değil, ilk grubun varyansını (kareler toplamı ÷ 3) vermiş.','dikkat'),(72,'Varyansı (36) 2 ile çarpıp standart sapma sanmış.','bilgi')],
 'Yeni veri grubunun standart sapması.',
 'Önce ilk gruptaki sapmayı hesapla; sonra verilere yapılan işlemlerin hangisinin sapmayı etkilediğini düşün.',
 [STD,DON],
 [A('Ortalama','Dört verinin toplamı 28.','28 ÷ 4 = 7'),A('Farklar ve kareleri','Her veriden 7 çıkar, karesini al.','−5, −5, 3, 7 → 25 + 25 + 9 + 49 = 108'),A('İlk grubun standart sapması','(n − 1) = 3’e böl, kök al.','√(108 ÷ 3) = √36 = 6'),A('Dönüşümün etkisi','Çıkarma sapmayı değiştirmez, 2 ile çarpma 2 katına çıkarır.','2 × 6 = 12')],
 puf='Verilere sabit çıkarmak standart sapmayı değiştirmez; |çarpan| ile çarpmak standart sapmayı aynı oranda büyütür.')

# ================= 0026 · zor · gruplu ortalama, katılan öğrenciler (sınav)
ka,er,tn=10,15,10; assert Fr(70*ka+60*er,ka+er)==64 and Fr(64*(ka+er)+50*tn,ka+er+tn)==60
cz=[k for k in range(1,60) for e in range(1,60) if Fr(70*k+60*e,k+e)==64 and Fr(64*(k+e)+50*10,k+e+10)==60]; assert cz==[10]
assert Fr(2*35,5)==14 and 15==er and 25==ka+er and 35==ka+er+tn
Q('0026','vri-agirlik','zor','Gruplu Ortalama','İki ortalamadan oranı, üçüncü ortalamadan toplam sayıyı bularak grup büyüklüğünü hesaplar.','hikâyeli','K-VRI-02 (gruplu ortalama, iki aşamalı) · ortak sınava giren öğrenciler',
 'Bir lisede yapılan ortak sınavın ilk gününde sınava giren kız öğrencilerin puan ortalaması 70, erkek öğrencilerin puan ortalaması 60’tır. İlk gün sınava giren tüm öğrencilerin puan ortalaması 64’tür.\nİkinci gün sınava 10 öğrenci daha girmiş ve bu 10 öğrencinin puan ortalaması 50 olmuştur. Böylece sınava giren tüm öğrencilerin puan ortalaması 60 olmuştur.\nBuna göre ilk gün sınava giren kız öğrenci sayısı kaçtır?',
 10,[(14,'Kız:erkek oranını 2:3 bulmuş ama toplamı 25 yerine 35 (ikinci gün girenlerle birlikte) alıp 35 × 2 ÷ 5 hesaplamış.','dikkat'),(15,'Oranı ters yorumlayıp (3:2) kız öğrenci sayısını erkeklerin sayısı olan 15 bulmuş.','islem'),(25,'İlk gün sınava giren öğrencilerin toplamını (25) kız öğrenci sayısı sanmış.','dikkat'),(35,'Sınava giren tüm öğrencilerin sayısını (35) kız öğrenci sayısı sanmış.','dikkat')],
 'İlk gün sınava giren kız öğrenci sayısı.',
 'Önce 64 ortalamasını kullanıp kız ve erkek sayıları arasındaki oranı bul; ardından ikinci gün ve 60 ortalamasıyla toplam sayıyı belirle.',
 [ORT,AGR],
 [A('Kız–erkek oranı','Kız sayısı k, erkek sayısı e olsun. Toplam puanı iki biçimde yaz.','70k + 60e = 64(k + e) ⇒ 6k = 4e ⇒ k : e = 2 : 3'),A('Sayıları t cinsinden yaz','k = 2t, e = 3t ise ilk gün giren 5t kişidir.','k = 2t, e = 3t, toplam 5t'),A('İkinci gün denklemi','İlk gün toplam puan 64 × 5t, ikinci gün toplam puan 50 × 10.','64 × 5t + 500 = 60 × (5t + 10)'),A('t’yi bul','Denklemi çöz.','320t + 500 = 300t + 600 ⇒ 20t = 100 ⇒ t = 5'),A('Kız sayısı','k = 2t.','2 × 5 = 10')],
 puf='İki ortalamanın birleşiminde oran, ortalamaların birleşik ortalamaya uzaklıklarının tersiyle kurulur; sonra toplam sayıyı ikinci koşuldan bul.')

# ================= 0027 · zor · çeyrekler açıklığı verilip x
b27=[11,26,5,17,14,21,8]; d27=lambda x:b27+[x]
s27=[x for x in range(1,200) if ceyrekA(d27(x))==13]; assert s27==[24]
q27=lambda x:(ortanca(sorted(d27(x))[:4]),ortanca(sorted(d27(x))[4:]))
assert q27(24)==(Fr(19,2),Fr(45,2)) and ceyrekA(d27(19))!=13 and ceyrekA(d27(28))!=13 and ceyrekA(d27(13))!=13 and 8+13==21
assert Fr(45,2)-Fr(19,2)==13 and (21+24)/2==22.5 and (24+26)/2==25 and (17+28)/2==22.5 and (19+26)/2==22.5
Q('0027','vri-aciklik','zor','Çeyrekler Açıklığı','Çeyrekler açıklığı verilen sekiz elemanlı veride bilinmeyen terimin sıralamadaki yerini bularak değerini hesaplar.','hikâyeli','K-VRI-05 (çeyrekler açıklığı verilip x) · öğrencilerin günlük kitap okuma süreleri',
 'Bir okulda 8 öğrencinin bir günde kitap okuma süreleri (dakika) 11, 26, 5, 17, x, 14, 21 ve 8’dir. Burada x pozitif bir tam sayıdır.\nSıralı bir veri grubunda ortanca, grubu alt ve üst olmak üzere eşit sayıda terimli iki yarıya ayırır. Alt yarının ortancasına Q1, üst yarının ortancasına Q3 denir ve çeyrekler açıklığı Q3 − Q1 olarak tanımlanır.\nBu veri grubunun çeyrekler açıklığı 13 olduğuna göre x kaçtır?',
 24,[(13,'x’i çeyrekler açıklığının kendisine (13) eşitlemiş.','dikkat'),(19,'Q3’ü (x + 26) ÷ 2 yazarak x’in en büyük iki terimden biri olduğunu varsaymış (x = 19).','islem'),(21,'Q1 yerine alt yarının 2. terimini (8) alıp Q3 = 8 + 13 = 21 bulmuş ve x’i 21 sanmış.','islem'),(28,'Q3’ü (17 + x) ÷ 2 yazarak x’i 17’den büyük, 21’den küçük bir yere yerleştirmemiş (x = 28).','islem')],
 'x’in değeri.',
 'Bilinen yedi sayıyı sırala. Q1 ve Q3’ün x’e bağlı olup olmadığını x’in sıralamadaki olası yerlerine göre incele.',
 [CEY],
 [A('Bilinen sayıları sırala','Yedi sayı sıralanır.','5, 8, 11, 14, 17, 21, 26'),A('Q1’i bul','x büyük çıkarsa alt yarı 5, 8, 11, 14 olur.','Q1 = (8 + 11) ÷ 2 = 9,5'),A('Q3’ü yaz','Q3 = Q1 + 13 olmalı.','Q3 = 9,5 + 13 = 22,5'),A('x’i yerleştir','Üst yarı 17, 21, 26 ve x’ten oluşur; Q3 ortadaki iki terimin ortalamasıdır. Q3 = 22,5 için x, 21 ile 26 arasında olmalı.','(21 + x) ÷ 2 = 22,5 ⇒ x = 24'),A('Kontrol et','24 sıralamaya uyar.','5, 8, 11, 14, 17, 21, 24, 26 → Q1 = 9,5, Q3 = 22,5, fark 13')],
 puf='Çeyrekler açıklığında bilinmeyenin yerine göre Q1 ya da Q3 değişir; yerini varsayıp sonucu sıralamayla doğrula.')

# ================= 0028 · zor · tablo, ortancası verilip en büyük x
def d28(x): return tabdizi([(40,4),(50,x),(60,7),(70,5),(80,3)])
s28=[x for x in range(1,100) if ortanca(d28(x))==60]; assert s28==list(range(1,11)) and max(s28)==10
assert ortanca(d28(11))==55 and ortanca(d28(12))==50
SK=tablo_svg(['Puan','Yarışmacı sayısı'],[['40','4'],['50','x'],['60','7'],['70','5'],['80','3']])
Q('0028','vri-medmod','zor','Tabloda Ortanca Koşulu','Ortancası verilen sıklık tablosunda bilinmeyen sıklığın alabileceği en büyük değeri birikimli sıklıkla bulur.','tablo','K-VRI-03 (tabloda ortanca koşulu, en büyük x) · bilgi yarışması puanları',
 'Bir bilgi yarışmasına katılanların aldığı puanlar ve her puanı alan yarışmacı sayısı aşağıdaki tabloda verilmiştir. 50 puan alan yarışmacı sayısı x’tir ve x pozitif bir tam sayıdır. Yarışmacıların puanlarının ortancası 60’tır.\nBuna göre x en çok kaç olabilir?',
 10,[(4,'Ortancanın 60 olması için 50 puanlıların sayısını 40 puanlıların sayısıyla (4) sınırlamış.','bilgi'),(7,'50 puanlıların sayısını 60 puanlıların sayısıyla (7) sınırlamış.','bilgi'),(11,'x = 11 için ortadaki terimlerin 15. ve 16. olduğunu, 15. terimin 50 olması nedeniyle ortancanın 55 çıkacağını denetlememiş.','dikkat'),(12,'Tek terimli durumdaki eşitsizliği (x < 12) kullanıp sınırı dahil etmiş ve çift terim durumunu incelememiş.','islem')],
 'x’in alabileceği en büyük değer.',
 'Birikimli sıklığı x cinsinden yaz. Ortanca 60 olacaksa ortadaki terim(ler) hangi sıra numaralarında olmalı?',
 [MED,SIK],
 [A('Toplam ve birikimli sıklık','Veri sayısı x + 19. 40 puana kadar 4 kişi, 50 puana kadar 4 + x kişi, 60 puana kadar 11 + x kişi vardır.','n = x + 19 · 40: 4 · 50: 4 + x · 60: 11 + x'),A('Ortanca 60 olmalı','Ortadaki terim(ler) 60 puanlıların arasında olmalı; yani sıra numarası 4 + x’ten büyük olmalıdır.','Ortadaki sıra > 4 + x'),A('Çift ve tek durum','n tekse ortadaki sıra (x + 20) ÷ 2 > 4 + x ⇒ x < 12. n çiftse n ÷ 2 = (x + 19) ÷ 2 > 4 + x ⇒ x < 11.','x tek ⇒ x ≤ 9 · x çift ⇒ x ≤ 10'),A('En büyük x','x = 11 için n = 30; 15. terim 50, 16. terim 60 ⇒ ortanca 55; x = 10 için n = 29 ve 15. terim 60’tır.','x en çok 10')],
 puf='Tabloda ortanca koşulu verildiğinde birikimli sıklıkla ortanca sırasının hangi değer aralığına düştüğünü bul; tek ve çift terim sayısını ayrı denetle.',sekil=SK)

# ================= 0029 · zor · yeni nesil: ortalama mutlak sapma
d29=[5,9,13]; x29=40-sum(d29); assert x29==13
dd29=d29+[x29]; oms=Fr(sum(abs(v-10) for v in dd29),4); assert ort(dd29)==10 and oms==3
assert sum(abs(v-10) for v in dd29)==12 and Fr(sum(v-10 for v in dd29),4)==0 and Fr(sum(abs(v-10) for v in d29+[10]),4)==Fr(9,4) and Fr(12,3)==4
Q('0029','vri-sapma','orta','Tanımlı Sapma Ölçüsü','Soruda tanımlanan ortalama mutlak sapma ölçüsünü, önce eksik terimi bularak hesaplar.','yeni nesil','K-VRI-06 (tanımlı sapma ölçüsü: ortalama mutlak sapma) · dört elemanlı veri',
 'Bir veri grubundaki her verinin aritmetik ortalamadan farkının mutlak değeri alınıp bu mutlak değerlerin aritmetik ortalamasına “ortalama mutlak sapma” denir. Örneğin 2, 4, 9 veri grubunun aritmetik ortalaması 5, ortalama mutlak sapması (3 + 1 + 4) ÷ 3 = 8 ÷ 3’tür.\n5, 9, 13, x veri grubunun aritmetik ortalaması 10’dur.\nBuna göre bu veri grubunun ortalama mutlak sapması kaçtır?',
 3,[(0,'Farkların işaretlerini koruyup toplamış; −5, −1, 3, 3’ün toplamı 0 çıkmış.','bilgi'),(Fr(9,4),'x’i ortalamaya (10) eşitlemiş; gerçek değeri 13’tür.','dikkat'),(4,'Mutlak sapmaların toplamını (12) veri sayısı 4 yerine 3’e bölmüş.','islem'),(12,'Mutlak sapmaların toplamını bulup veri sayısına bölmeyi unutmuş.','dikkat')],
 'Veri grubunun ortalama mutlak sapması.',
 'Tanımdaki ortalamayı almak için hangi bilgiler gerekir? Örnekteki işlem sırasını izle.',
 [ORT,B('Mutlak değer','bir sayının sıfıra uzaklığıdır; farkın işareti önemsizdir. Örnek: |−5| = 5, |3| = 3')],
 [A('x’i bul','Ortalama 10 olduğundan dört verinin toplamı 40’tır.','5 + 9 + 13 + x = 40 ⇒ x = 13'),A('Ortalamadan farklar','Her veriden 10 çıkar.','−5, −1, 3, 3'),A('Mutlak değerler','İşaretleri at ve topla.','5 + 1 + 3 + 3 = 12'),A('Ortalamasını al','Veri sayısı 4’e böl.','12 ÷ 4 = 3')],
 puf='Tanımlı bir ölçüde önce tanımı örnekle eşleştir; ortalama gibi eksik bir veri varsa önce onu bul, sonra tanımdaki işlemleri sırayla uygula.')

# ================= 0030 · zor · iki sütun grafiği, öncüllü
pu=['50','60','70','80','90']; fa=[2,4,8,4,2]; fb=[6,2,4,2,6]; pv=[50,60,70,80,90]
dA=tabdizi(list(zip(pv,fa))); dB=tabdizi(list(zip(pv,fb)))
assert len(dA)==len(dB)==20 and ort(dA)==ort(dB)==70 and ortanca(dA)==ortanca(dB)==70 and tepe(dA)==[70] and tepe(dB)==[50,90]
assert stt.stdev(dA)<stt.stdev(dB) and varyans(dA)<varyans(dB) and aciklik(dA)==aciklik(dB)==40
SK=alt_alta(('Şekil 1 · A sınıfı',sutun(pu,fa,2,8,'Öğrenci sayısı','Puan')),('Şekil 2 · B sınıfı',sutun(pu,fb,2,8,'Öğrenci sayısı','Puan')))
Q('0030','vri-sekil','zor','İki Sütun Grafiği Karşılaştırma','İki sınıfın puan dağılımını gösteren sütun grafiklerinden ortalama, standart sapma ve tepe değerleri karşılaştırır.','öncüllü','K-VRI-08 (iki sıklık grafiği, ölçülerin karşılaştırılması) · iki sınıfın deneme puanları',
 'Bir okulda 20’şer öğrencinin bulunduğu A ve B sınıflarının bir denemeden aldıkları puanların dağılımı, her puanı alan öğrenci sayısı olarak Şekil 1 ve Şekil 2’deki sütun grafiklerinde gösterilmiştir.\nI. A sınıfının puanlarının standart sapması, B sınıfınınkinden büyüktür.\nII. İki sınıfın puanlarının aritmetik ortalaması birbirine eşittir.\nIII. B sınıfının puanlarının iki tepe değeri vardır.\nBuna göre bu ifadelerden hangileri doğrudur?',
 'II ve III',sira=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III'],
 yan=[('Yalnız II','B sınıfındaki 50 ve 90 sütunlarının ikisinin de en yüksek olduğunu görmeyip III’ü yanlış saymış.','dikkat'),('Yalnız III','İki grafiğin simetrik olması nedeniyle ortalamaların eşit olduğunu (ikisi de 70) fark etmeyip II’yi yanlış saymış.','islem'),('I ve II','A sınıfının tepe değerinin tek (70) olmasına bakıp B’deki iki tepe değeri sayamamış; standart sapmayı da ters yorumlamış.','dikkat'),('I, II ve III','Verilerin uçlarda toplanmasının standart sapmayı artıracağını görmeyip, A sınıfındaki yığılmayı büyük yayılım sanmış.','bilgi')],
 istenen='Doğru olan ifadeler.',
 ip='Her grafikten puanları ve sıklıkları oku; ortalama ve tepe değeri hesapla, sonra verilerin ortalamadan ne kadar uzak olduğunu karşılaştır.',
 bilgi=[GRF,STD,MOD],
 ad=[A('Değerleri oku','Sütunlar öğrenci sayısını verir.','A: 50 → 2, 60 → 4, 70 → 8, 80 → 4, 90 → 2 · B: 50 → 6, 60 → 2, 70 → 4, 80 → 2, 90 → 6'),A('Ortalamalar','Her sınıf için puan toplamı ÷ 20.','A: (100 + 240 + 560 + 320 + 180) ÷ 20 = 70 · B: (300 + 120 + 280 + 160 + 540) ÷ 20 = 70 → II doğru'),A('Tepe değerler','A’da en yüksek sütun 70; B’de 50 ve 90 sütunları 6’şar öğrencili.','A: 70 · B: 50 ve 90 → III doğru'),A('Standart sapma','Ortalama (70) aynı; B’nin verileri ortalamadan daha uzakta toplandığı için standart sapması daha büyüktür.','A’nın standart sapması < B’nin standart sapması → I yanlış')],
 puf='Ortalamaları eşit iki gruptan, verileri ortalamadan daha uzağa yığılmış olanın standart sapması daha büyüktür.',sekil=SK)

bitir(P,'veri',UK)
