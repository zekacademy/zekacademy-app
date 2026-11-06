"""Grafik Problemleri · parti 1: 8 ana + 8 kardeş. Grafikler (sütun, çizgi, daire, tablo) aynı veri listelerinden çizilir;
her cevap ve her ara değer bu listelerden kodla yeniden hesaplanır (assert)."""
import sys,os,json,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('grafikprob','Grafik Problemleri','prob|Grafik Problemleri')
UK='prob|Grafik Problemleri'
TT=lambda **k:k
ACC=G.ACC
def sirali(s): assert s==sorted(s) and len(set(s))==5, s
def tek_dogru(s,d): assert s.count(d)==1; return 'ABCDE'[s.index(d)]

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
def daire(dl,W=330,H=196,r=74):
    """dl: [(ad, derece)]; dilimler tepeden başlayıp saat yönünde. Açılar dilimin içinde, adlar dışında."""
    assert sum(d for _,d in dl)==360
    cx,cy=W/2,H/2; b=[]; a=-90.0; op=['.14','.42','.26','.56','.34']
    P_=lambda ang,rr:(cx+rr*math.cos(math.radians(ang)),cy+rr*math.sin(math.radians(ang)))
    for i,(ad,d) in enumerate(dl):
        a1=a+d; (xa,ya),(xb,yb)=P_(a,r),P_(a1,r)
        b.append(f'<path d="M{cx:.1f} {cy:.1f} L{xa:.1f} {ya:.1f} A{r} {r} 0 {1 if d>180 else 0} 1 {xb:.1f} {yb:.1f} Z" stroke-width="1.4" style="fill:{ACC}" fill-opacity="{op[i%len(op)]}"/>')
        m=a+d/2; xt,yt=P_(m,r*.6); b.append(G._t(xt,yt+4,f'{d}°',size=11,bold=True))
        xo,yo=P_(m,r+10); c=math.cos(math.radians(m))
        b.append(G._t(xo,yo+4,ad,anchor='start' if c>.25 else ('end' if c<-.25 else 'middle'),size=11))
        a=a1
    return ''.join(b),W,H
def tablo(bas,sat,gen):
    """bas: başlıklar; sat: satırlar (metin); gen: sütun genişlikleri."""
    W=sum(gen)+4; h=26; Hh=h*(len(sat)+1)+4; b=[]; xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b.append(f'<rect x="2" y="2" width="{W-4}" height="{h}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>')
    for j,s in enumerate(bas): b.append(G._t((xs[j]+xs[j+1])/2,2+h/2+4,s,size=10,bold=True))
    for i,row in enumerate(sat):
        y=2+h*(i+1)
        for j,s in enumerate(row): b.append(G._t((xs[j]+xs[j+1])/2,y+h/2+4,s,size=11,bold=(j==0 or s=='?'),renk=(ACC if s=='?' else None)))
    for i in range(len(sat)+2): b.append(f'<line x1="2" y1="{2+h*i}" x2="{W-2}" y2="{2+h*i}" stroke-width="{1.4 if i in (0,1,len(sat)+1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{2+h*(len(sat)+1)}" stroke-width="1"/>')
    return ''.join(b),W,Hh
def tek(g): body,W,Hh=g; return G._svg(W,Hh,body)
def alt_alta(*parcalar):
    """[(başlık, (gövde,W,H))] parçalarını alt alta tek SVG'de birleştirir."""
    W=max(p[1][1] for p in parcalar); y=0; b=[]
    for ad,(body,w,h) in parcalar:
        b.append(G._t(W/2,y+14,ad,size=11,bold=True)); b.append(f'<g transform="translate({(W-w)/2:.1f},{y+20})">{body}</g>'); y+=h+26
    return G._svg(W,y,''.join(b))

# ---------- kartlar ve tipler
KARTLAR=[
 dict(id='K-GR-01',konu='Grafik Problemleri',alt='Sütun grafiği',fikir='Sütun grafiğinden değerler okunur; toplam, fark ya da bir değerin toplam içindeki yüzdesi hesaplanır.',tuzak='Komşu sütunu okumak; bir değeri toplamın dışında bırakmak; sayıyı yüzde sanmak.',zorluk='kolay',kalip='grafik',adim=2,tipId='grf-sutun',tip='Sütun grafiği okuma ve yorumlama',kaynak='Bilgi Sarmal, Mert Hoca (sütun grafiğinde dağılım) · ÖSYM 2019'),
 dict(id='K-GR-02',konu='Grafik Problemleri',alt='Ölçeği verilmemiş sütun',fikir='Dikey eksende sayı yoktur; bir sütunun değeri (ya da iki sütunun farkı) verilir, bir bölmenin değeri bulunup diğer sütunlar okunur.',tuzak='Bölme sayısını değer sanmak; bölmeleri yanlış saymak.',zorluk='orta',kalip='grafik',adim=3,tipId='grf-sutun',tip='Sütun grafiği okuma ve yorumlama',kaynak='Mert Hoca (araçlardaki benzin), 345 SB (ölçeksiz grafik)'),
 dict(id='K-GR-03',konu='Grafik Problemleri',alt='Daire grafiği',fikir='Daire 360°’dir; toplam verilince bir derecenin karşılığı bulunur ve dilimler sayıya çevrilir.',tuzak='Açıyı sayı sanmak; bir derecenin değerini yanlış bulmak; istenmeyen dilimi almak.',zorluk='kolay',kalip='grafik',adim=2,tipId='grf-daire',tip='Daire grafiği',kaynak='ÖSYM 2020 (spor egzersizi süreleri), ÖSYM 2022 (dolaptaki kıyafetler)'),
 dict(id='K-GR-04',konu='Grafik Problemleri',alt='Çizgi grafiği',fikir='Zamana göre değişim çizgi grafiğinden okunur; iki an arasındaki fark ya da bir önceki döneme göre yüzde değişim bulunur.',tuzak='Yüzde puan farkını miktar sanmak; değişimi yeni değere bölmek; yanlış aralığı seçmek.',zorluk='orta',kalip='grafik',adim=3,tipId='grf-cizgi',tip='Çizgi grafiği ve değişim',kaynak='3D (aracın aldığı yol), 345 SB (mumun boyu) · ÖSYM 2024'),
 dict(id='K-GR-05',konu='Grafik Problemleri',alt='Tablo',fikir='Tablodaki bazı hücreler boştur; satır/sütun ilişkileri (gelir = fiyat × adet) ve verilen toplamla eksikler tamamlanır.',tuzak='Bir satırı toplamdan düşmeyi unutmak; istenmeyen hücreyi cevap sanmak.',zorluk='orta',kalip='tablo',adim=3,tipId='grf-tablo',tip='Tablo yorumlama',kaynak='Bilgi Sarmal (kurs kayıt tablosu, maaş tablosu) · Mert Hoca (deneme tablosu)'),
 dict(id='K-GR-06',konu='Grafik Problemleri',alt='Veri değişince grafik',fikir='Daire grafiğindeki bir gruba ekleme yapılınca o grubun yeni yüzdesi verilir; başlangıç toplamı denklemle bulunur.',tuzak='Yeni oranı kurarken eklenenleri toplama katmamak; istenmeyen dilimi vermek.',zorluk='orta',kalip='grafik',adim=4,tipId='grf-degisim',tip='Veri değişince grafiği yorumlama',kaynak='ÖSYM 2022 (dolaptan ceket eksilince), ÖSYM 2021 (anket oyları eklenince)'),
 dict(id='K-GR-07',konu='Grafik Problemleri',alt='İki grafik: dağılım ve oran',fikir='Daire grafiği grupların dağılımını, sütun grafiği her grupta bir özelliğin yüzdesini verir; açı × yüzde toplamı bilinen sayıya eşlenir.',tuzak='Yüzdeleri doğrudan toplamak ya da ortalamak; bir dereceyi bir kişi sanmak; istenmeyen alt grubu vermek.',zorluk='zor',kalip='grafik',adim=5,tipId='grf-iki',tip='İki grafiği birlikte yorumlama',kaynak='ÖSYM 2019 (yatak satış ve iade yüzdeleri), ÖSYM 2023 (fabrika ve ihracat yüzdeleri)'),
 dict(id='K-GR-08',konu='Grafik Problemleri',alt='İki grafik: adet ve gelir',fikir='Sütun grafiği satış adedini, daire grafiği gelirin dağılımını verir; bilinen bir fiyattan bir derecenin değeri, oradan diğer fiyatlar bulunur.',tuzak='Fiyat oranını açı oranı sanmak; geliri yanlış ürünün adedine bölmek.',zorluk='zor',kalip='grafik',adim=4,tipId='grf-iki',tip='İki grafiği birlikte yorumlama',kaynak='Bilgi Sarmal (alış fiyatı tablosu + dairesel grafik), Orijinal Deneme (ciro ve maliyet grafiği)'),
]
TIPLER={}
for k in KARTLAR: TIPLER.setdefault(k['tipId'],dict(tipId=k['tipId'],ad=k['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(k['id'])
json.dump(dict(konu='Grafik Problemleri',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 (Veri ve Problemler), Bilgi Sarmal, 3D, Mert Hoca, 345 SB, Orijinal Deneme.',kartlar=KARTLAR,tipler=list(TIPLER.values())),
          open(os.path.join(H,'..','kartlar','grafikprob.json'),'w'),ensure_ascii=False,indent=1)
T={t:TIPLER[t]['ad'] for t in TIPLER}

SOK=B('Sütun grafiği okuma','sütunun üst ucundan yatay çizgiyi izleyip dikey eksendeki değeri oku')
YZB=B('Yüzdeyi bulmak','parça ÷ bütün × 100. Örnek: 30 ÷ 120 = 0,25 ⇒ %25')
DAI=B('Daire grafiği','tüm daire 360°’dir; dilimin sayısı = toplam × açı ÷ 360. Örnek: 60 kişide 90°’lik dilim ⇒ 60 × 90 ÷ 360 = 15 kişi')
BOL=B('Bir bölmenin değeri','bilinen değer ÷ ona karşılık gelen bölme sayısı. Örnek: 4 bölme 20 ise 1 bölme 5')
GEL=B('Gelir','gelir = birim fiyat × satılan adet. Örnek: tanesi 25 TL olan üründen 8 tane ⇒ 200 TL')
DEG=B('Yüzde değişim','değişim ÷ eski değer × 100. Örnek: 40’tan 50’ye çıkış ⇒ 10 ÷ 40 = %25 artış')
DER=B('Bir derecenin değeri','bilinen sayı ÷ ona karşılık gelen açı. Örnek: 90° = 1800 TL ise 1° = 20 TL')

# ===== 0001 sütun KOLAY
et=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma']; dg=[40,60,30,70,50]
top=sum(dg); per=dg[3]; assert top==250 and Fr(per,top)*100==28
s=[20,24,28,35,70]; sirali(s); assert Fr(dg[1],top)*100==24 and Fr(per,top-dg[4])*100==35
SK=tek(sutun(et,dg,10,80,'Kitap sayısı','Günler'))
P.R('0001','grf-sutun',T['grf-sutun'],'kolay','Sütun grafiği','Sütun grafiğinden değerleri okuyup toplamı bulur; bir değerin toplam içindeki yüzdesini hesaplar.','grafik',2,
 'K-GR-01 (sütundan değer okuma, toplam içindeki yüzde) · yeni kurgu (kitapçının günlük satışı)',
 'Bir kitapçının bir haftanın beş iş gününde sattığı kitap sayıları aşağıdaki sütun grafiğinde gösterilmiştir.\nBuna göre bu beş günde satılan kitapların yüzde kaçı perşembe günü satılmıştır?',
 [str(v) for v in s],tek_dogru(s,28),'Perşembe satışının beş günlük toplam içindeki yüzdesi.',
 ['Her sütunun değerini dikey eksenden oku.','Beş günün toplamını bul.','Perşembe değerini toplama bölüp 100 ile çarp.'],[SOK,YZB],
 [A('Değerleri oku','Pazartesiden cumaya sütunların değerleri.','40 · 60 · 30 · 70 · 50'),
  A('Toplam satış','Beş günü topla.','40 + 60 + 30 + 70 + 50 = 250'),
  A('Perşembenin payı','Perşembe 70 kitap.','70 ÷ 250 = 0,28 ⇒ %28')],
 'Grafikte yüzde sorulunca önce bütünü (tüm sütunların toplamını) bul; her sütunu toplama kattığından emin ol.',
 dict(A='20, beş günde eşit satış varsaymak (100 ÷ 5); sütunlar eşit değil.',B='24, perşembe yerine salı sütununu (60) okumak.',D='35 = 70 ÷ 200; toplamı bulurken cumayı (50) unutmak.',E='70, perşembe satılan kitap sayısı; soru yüzdeyi soruyor.'),
 TT(A='bilgi',B='dikkat',D='islem',E='dikkat'),sekil=SK)
et=['08–10','10–12','12–14','14–16','16–18']; dg=[50,30,20,40,60]
top=sum(dg); ara=dg[2]+dg[3]; assert top==200 and Fr(ara,top)*100==30
s=[10,20,30,40,60]; sirali(s); assert Fr(dg[2],top)*100==10 and Fr(dg[3],top)*100==20 and ara==60
SK=tek(sutun(et,dg,10,70,'Araç sayısı','Saat aralığı'))
P.K('0001','Bir alışveriş merkezinin otoparkına bir gün boyunca iki saatlik zaman dilimlerinde giren araç sayıları aşağıdaki grafikte verilmiştir.\nBuna göre saat 12.00 ile 16.00 arasında otoparka giren araçlar, 08.00 ile 18.00 arasında giren tüm araçların yüzde kaçıdır?',
 [str(v) for v in s],tek_dogru(s,30),'12.00–16.00 arasında giren araçların tüm araçlara göre yüzdesi.',
 ['12.00 ile 16.00 arası hangi iki dilimi kapsar?','Beş dilimin toplamını bul.','İki dilimin toplamını tüm araçlara böl.'],[SOK,YZB],
 [A('Değerleri oku','Beş dilimdeki araç sayıları.','50 · 30 · 20 · 40 · 60'),
  A('Toplam ve aralık','12.00–16.00 arası iki dilimdir: 12–14 ve 14–16.','toplam: 200 · aralık: 20 + 40 = 60'),
  A('Yüzde','Aralıktaki araçları toplama böl.','60 ÷ 200 = 0,3 ⇒ %30')],
 'Bir zaman aralığı birden çok dilimi kapsıyorsa hepsini topla; sonra bütüne böl.',
 dict(A='10, yalnız 12.00–14.00 dilimini almak (20 ÷ 200); 14.00–16.00 de aralıkta.',B='20, yalnız 14.00–16.00 dilimini almak (40 ÷ 200).',D='40, beş dilimden ikisini seçip 2/5 almak; dilimlerdeki araç sayıları eşit değil.',E='60, bu aralıkta giren araç sayısı; soru yüzdeyi soruyor.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'),sekil=SK)

# ===== 0002 daire KOLAY
dl=[('Otobüs',135),('Servis',75),('Yürüyerek',90),('Bisiklet',60)]; N=48
say={a:Fr(N*d,360) for a,d in dl}; assert all(v.denominator==1 for v in say.values()) and sum(say.values())==N
cev=say['Otobüs']+say['Servis']-say['Yürüyerek']; assert (say['Otobüs']+say['Servis'],say['Yürüyerek'],cev)==(28,12,16)
s=[8,12,16,28,120]; sirali(s); assert (135+75-90)//15==8 and 135+75-90==120
SK=tek(daire(dl))
P.R('0002','grf-daire',T['grf-daire'],'kolay','Daire grafiği','Daire grafiğindeki açıları toplam sayıya göre kişi sayısına çevirir ve iki grubu karşılaştırır.','grafik',2,
 'K-GR-03 (açıdan sayıya) · yeni kurgu (okula ulaşım), yeni istenen (iki grubun farkı)',
 'Bir sınıftaki 48 öğrencinin okula geliş biçimlerine göre dağılımı aşağıdaki daire grafiğinde gösterilmiştir.\nBuna göre okula otobüsle ya da servisle gelen öğrencilerin sayısı, yürüyerek gelenlerin sayısından kaç fazladır?',
 [str(v) for v in s],tek_dogru(s,16),'Otobüs ve servisle gelenlerin yürüyerek gelenlerden farkı.',
 ['360° kaç öğrenciye karşılık geliyor? Bir öğrenci kaç derece eder?','Otobüs ve servis dilimlerinin açılarını topla.','Açıları öğrenci sayısına çevirip farkı al.'],[DAI],
 [A('Bir öğrencinin açısı','Tüm daire 48 öğrenci.','360 ÷ 48 = 7,5° · yani 15° = 2 öğrenci'),
  A('Grupları say','Otobüs + servis 210°, yürüyerek 90°.','210 ÷ 7,5 = 28 · 90 ÷ 7,5 = 12'),
  A('Fark','İki grubun farkı.','28 − 12 = 16')],
 'Daire grafiğinde önce bir derecenin (ya da bir kişinin) karşılığını bul; açıları sonra sayıya çevir.',
 dict(A='8 = 120 ÷ 15; 15°’yi 1 öğrenci sanmak. 15° 2 öğrenciye karşılık gelir.',B='12, yürüyerek gelenlerin sayısı; fark değil.',D='28, otobüs ve servisle gelenlerin sayısı; fark değil.',E='120, iki grubun açı farkı (°); öğrenci sayısına çevrilmemiş.'),
 TT(A='islem',B='dikkat',D='dikkat',E='dikkat'),
 kisa='Yalnız açı farkını çevir: 210° − 90° = 120° · 120 ÷ 7,5 = 16 öğrenci.',sekil=SK)
dl=[('Elma',108),('Armut',72),('Ceviz',120),('Kiraz',60)]; N=60
say={a:Fr(N*d,360) for a,d in dl}; assert all(v.denominator==1 for v in say.values())
cev=say['Elma']+say['Kiraz']; assert (say['Elma'],say['Kiraz'],cev)==(18,10,28)
s=[10,14,18,28,168]; sirali(s); assert (108+60)//12==14 and 108+60==168
SK=tek(daire(dl))
P.K('0002','Bir bahçedeki 60 meyve ağacının türlerine göre dağılımı aşağıdaki daire grafiğinde verilmiştir.\nBuna göre bahçedeki elma ve kiraz ağaçlarının toplam sayısı kaçtır?',
 [str(v) for v in s],tek_dogru(s,28),'Elma ve kiraz ağaçlarının toplamı.',
 ['Tüm daire 60 ağaç ise 1 ağaç kaç derecedir?','Elma ve kiraz dilimlerinin açılarını topla.','Toplam açıyı ağaç sayısına çevir.'],[DAI],
 [A('Bir ağacın açısı','Tüm daire 60 ağaç.','360 ÷ 60 = 6°'),
  A('İki dilim','Elma 108°, kiraz 60°.','108 + 60 = 168°'),
  A('Ağaç sayısı','Açıyı 6’ya böl.','168 ÷ 6 = 28 ağaç')],
 'Daire grafiğinde birden çok dilim soruluyorsa açıları topla, sonra tek seferde sayıya çevir.',
 dict(A='10, yalnız kiraz ağaçlarının sayısı.',B='14 = 168 ÷ 12; bir ağacı 12° sanmak. 360 ÷ 60 = 6°.',C='18, yalnız elma ağaçlarının sayısı.',E='168, iki dilimin açılarının toplamı (°); ağaç sayısına çevrilmemiş.'),
 TT(A='dikkat',B='islem',C='dikkat',E='dikkat'),sekil=SK)

# ===== 0003 çizgi ORTA
et=['Oca','Şub','Mar','Nis','May','Haz']; dg=[40,50,70,80,60,50]; K=240
mx=max(dg); assert dg.count(mx)==1 and et[dg.index(mx)]=='Nis'; cev=Fr(mx-dg[5],100)*K; assert cev==72
s=[24,30,48,72,120]; sirali(s); assert Fr(dg[4]-dg[5],100)*K==24 and Fr(dg[2]-dg[5],100)*K==48 and Fr(dg[5],100)*K==120
SK=tek(cizgi(et,dg,10,90,'Doluluk oranı (%)','Aylar'))
P.R('0003','grf-cizgi',T['grf-cizgi'],'orta','Çizgi grafiği','Çizgi grafiğinden en büyük değeri ve istenen değeri okuyup yüzde farkını miktara çevirir.','grafik',3,
 'K-GR-04 (zamana göre değişim, yüzde puan → miktar) · yeni kurgu (baraj doluluğu), yeni istenen (miktar farkı)',
 'Su kapasitesi 240 milyon m³ olan bir barajın ocak–haziran aylarındaki doluluk oranları aşağıdaki çizgi grafiğinde gösterilmiştir. Ölçümler her ayın aynı gününde yapılmıştır.\nBuna göre barajdaki su miktarının en fazla olduğu ay ile haziran ayı arasındaki su miktarı farkı kaç milyon m³’tür?',
 [str(v) for v in s],tek_dogru(s,72),'En dolu ay ile haziran arasındaki su miktarı farkı.',
 ['Grafikte en yüksek nokta hangi aya ait ve değeri kaç?','Haziran ayının doluluk oranı kaç?','Oran farkını 240 milyon m³’ün yüzdesi olarak hesapla.'],[YZB,B('Doluluk oranı','kaptaki miktar ÷ kapasite. Örnek: 200 L’lik deponun %30’u dolu ⇒ 60 L su')],
 [A('En dolu ay','En yüksek nokta nisan ayında.','nisan: %80 · haziran: %50'),
  A('Oran farkı','İki oranın farkı kapasitenin yüzdesidir.','80 − 50 = 30 ⇒ kapasitenin %30’u'),
  A('Miktara çevir','240 milyon m³’ün %30’u.','240 × 0,3 = 72 milyon m³')],
 'Oranlarla verilen grafikte farkı önce yüzde olarak bul, sonra bütünün (kapasitenin) yüzdesi olarak miktara çevir.',
 dict(A='24, mayıs ile haziranı karşılaştırmak (%10); en yüksek doluluk nisanda.',B='30, doluluk oranlarının farkı; milyon m³’e çevrilmemiş.',C='48, en yüksek ayı mart sanmak (%70 − %50 = %20).',E='120, haziran ayındaki su miktarı (240’ın %50’si); fark değil.'),
 TT(A='dikkat',B='bilgi',C='dikkat',E='dikkat'),sekil=SK)
et=['Pzt','Salı','Çar','Per','Cuma','Cmt']; dg=[120,150,90,180,210,240]
fk=[dg[i]-dg[i-1] for i in range(1,6)]; i_=fk.index(max(fk))+1; assert fk.count(max(fk))==1 and et[i_]=='Per'
yz=[Fr(dg[i]-dg[i-1],dg[i-1])*100 for i in range(1,6)]; assert yz.index(max(yz))+1==i_ and yz[i_-1]==100
s=[25,50,60,90,100]; sirali(s); assert yz[0]==25 and Fr(90,180)*100==50 and dg[1]-dg[2]==60 and max(fk)==90
SK=tek(cizgi(et,dg,30,270,'Satılan çay (bardak)','Günler'))
P.K('0003','Bir kafede bir haftanın altı gününde satılan çay sayıları aşağıdaki çizgi grafiğinde gösterilmiştir.\nBuna göre satılan çay sayısının bir önceki güne göre sayıca en çok arttığı günde, satış bir önceki güne göre yüzde kaç artmıştır?',
 [str(v) for v in s],tek_dogru(s,100),'En büyük artışın olduğu günün yüzde artışı.',
 ['Her günün değerini oku ve bir önceki günle farkını yaz.','En büyük artış hangi günde?','Artışı bir önceki günün değerine böl.'],[DEG],
 [A('Değerleri oku','Pazartesiden cumartesiye.','120 · 150 · 90 · 180 · 210 · 240'),
  A('Günlük değişimler','Her günü bir öncekiyle karşılaştır.','+30 · −60 · +90 · +30 · +30 ⇒ en büyük artış perşembe'),
  A('Yüzde artış','Perşembe 90’dan 180’e çıkmış; artışı eski değere böl.','90 ÷ 90 = 1 ⇒ %100')],
 'Yüzde artışta bölen her zaman eski (önceki) değerdir.',
 dict(A='25, salıdaki artışın yüzdesi (120 → 150); en büyük artış perşembe.',B='50 = 90 ÷ 180; artışı yeni değere bölmek. Bölen önceki gündür.',C='60, çarşambadaki düşüş miktarı; artış değil.',D='90, perşembedeki artış miktarı (bardak); yüzde değil.'),
 TT(A='dikkat',B='islem',C='dikkat',D='dikkat'),sekil=SK)

# ===== 0004 tablo ORTA
fd,ad_,gs=90,40,900; fk_=30; TOP=6000; kal=Fr(TOP-fd*ad_-gs,fk_); assert kal==50
s=[50,80,170,200,1500]; sirali(s); assert Fr(TOP-fd*ad_,fk_)==80 and Fr(TOP-gs,fk_)==170 and Fr(TOP,fk_)==200 and kal*fk_==1500
SK=tek(tablo(['Ürün','Birim fiyat (TL)','Satış adedi','Gelir (TL)'],[['Defter',str(fd),str(ad_),'?'],['Kalem',str(fk_),'?','?'],['Silgi','?','45',str(gs)]],[62,96,80,84]))
assert gs%45==0
P.R('0004','grf-tablo',T['grf-tablo'],'orta','Tablo','Tablodaki eksik hücreleri gelir = fiyat × adet ilişkisi ve verilen toplamla tamamlar.','tablo',3,
 'K-GR-05 (eksik hücreli tablo, toplam koşulu) · yeni kurgu (kırtasiye geliri), yeni istenen (satış adedi)',
 'Bir kırtasiyenin bir günde sattığı üç ürüne ait bilgilerin bir kısmı aşağıdaki tabloda verilmiştir.\nBu üç ürünün satışından elde edilen toplam gelir 6000 TL’dir.\nBuna göre bu kırtasiye o gün kaç kalem satmıştır?',
 [str(v) for v in s],tek_dogru(s,50),'Satılan kalem sayısı.',
 ['Defterden elde edilen geliri tablodan hesapla.','Toplam gelirden defter ve silgi gelirlerini çıkar.','Kalan geliri kalemin birim fiyatına böl.'],[GEL],
 [A('Defter geliri','Birim fiyat × adet.','90 × 40 = 3600 TL'),
  A('Kalem geliri','Toplamdan diğer iki ürünün gelirini çıkar.','6000 − 3600 − 900 = 1500 TL'),
  A('Kalem sayısı','Geliri birim fiyata böl.','1500 ÷ 30 = 50 kalem')],
 'Eksik hücreli tablolarda önce doğrudan hesaplanabilen hücreleri doldur; kalan bilinmeyeni toplam koşuluyla bul.',
 dict(B='80: silgi gelirini (900 TL) toplamdan düşmeyi unutmak.',C='170: defter gelirini (3600 TL) toplamdan düşmeyi unutmak.',D='200 = 6000 ÷ 30; toplam gelirin hepsini kaleme ait sanmak.',E='1500, kalem satışından elde edilen gelir (TL); soru kalem sayısını soruyor.'),
 TT(B='dikkat',C='dikkat',D='bilgi',E='dikkat'),sekil=SK)
ft,at_,gc,ac=240,100,3000,30; fo=150; TOP=39000; og=Fr(TOP-ft*at_-gc,fo); assert og==80; cev=at_+og+ac; assert cev==210
s=[80,130,180,210,230]; sirali(s); assert at_+ac==130 and at_+og==180 and at_+Fr(TOP-ft*at_,fo)+ac==230
SK=tek(tablo(['Bilet türü','Bilet fiyatı (TL)','Satılan bilet','Gelir (TL)'],[['Tam',str(ft),str(at_),'?'],['Öğrenci',str(fo),'?','?'],['Çocuk','?',str(ac),str(gc)]],[66,98,80,80]))
P.K('0004','Bir sinemanın hafta sonu bilet satışlarına ait bilgilerin bir kısmı aşağıdaki tabloda verilmiştir.\nSinema hafta sonu bu biletlerden toplam 39000 TL gelir elde etmiştir.\nBuna göre hafta sonu toplam kaç bilet satılmıştır?',
 [str(v) for v in s],tek_dogru(s,210),'Hafta sonu satılan tüm biletlerin sayısı.',
 ['Tam bilet gelirini tablodan hesapla.','Toplam gelirden tam ve çocuk bileti gelirlerini çıkarıp öğrenci bileti sayısını bul.','Üç bilet türünün adetlerini topla.'],[GEL],
 [A('Tam bilet geliri','Fiyat × adet.','240 × 100 = 24000 TL'),
  A('Öğrenci biletleri','Kalan geliri öğrenci bileti fiyatına böl.','39000 − 24000 − 3000 = 12000 · 12000 ÷ 150 = 80'),
  A('Toplam bilet','Üç türün adetleri.','100 + 80 + 30 = 210 bilet')],
 'Tablodaki toplam koşulunu kullanmadan önce bilinen satırların hepsini toplamdan düş.',
 dict(A='80, yalnız öğrenci biletlerinin sayısı; soru tüm biletleri soruyor.',B='130: öğrenci biletlerini toplama katmamak (100 + 30).',C='180: çocuk biletlerini toplama katmamak (100 + 80).',E='230: çocuk gelirini düşmeden öğrenci bileti sayısını 100 bulmak; (39000 − 24000) ÷ 150 = 100.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='islem'),sekil=SK)

# ===== 0005 değişim ORTA
dl=[('Kırmızı',150),('Sarı',90),('Mavi',120)]
ns=[n for n in range(1,1000) if n*90%360==0 and Fr(n*90//360+6,n+6)==Fr(3,10)]; assert ns==[84]; N=84
mavi=N*120//360; assert mavi==28 and N*90//360==21 and N*150//360==35
hat=[n for n in range(1,1000) if n*90%360==0 and Fr(n*90//360+6,n)==Fr(3,10)]; assert hat==[120] and 120*120//360==40
s=[21,28,35,40,84]; sirali(s)
SK=tek(daire(dl))
P.R('0005','grf-degisim',T['grf-degisim'],'orta','Veri değişince grafik','Daire grafiğindeki bir gruba ekleme yapıldığında verilen yeni yüzdeden başlangıç toplamını denklemle bulur.','grafik',4,
 'K-GR-06 (ekleme sonrası yeni yüzde) · yeni kurgu (akvaryumdaki balıklar), yeni istenen (başka bir dilimin sayısı)',
 'Bir akvaryumdaki balıkların renklerine göre dağılımı aşağıdaki daire grafiğinde gösterilmiştir.\nAkvaryuma 6 sarı balık daha konulduğunda sarı balıklar akvaryumdaki tüm balıkların %30’u olmaktadır.\nBuna göre başlangıçta akvaryumda kaç mavi balık vardır?',
 [str(v) for v in s],tek_dogru(s,28),'Başlangıçtaki mavi balık sayısı.',
 ['Sarı dilim tüm dairenin kaçta kaçı?','Başlangıçta N balık varsa, eklemeden sonra kaç sarı ve toplam kaç balık olur?','Yeni oranı %30’a eşitle; N’yi bulunca mavi dilimi hesapla.'],[DAI,YZB],
 [A('Sarının payı','90°, dairenin dörtte biri.','90 ÷ 360 = 1/4 ⇒ sarı: N ÷ 4'),
  A('Yeni durum','6 sarı balık eklenir; toplam da 6 artar.','sarı: N ÷ 4 + 6 · toplam: N + 6'),
  A('Denklem','Yeni sarı oranı %30.','N ÷ 4 + 6 = 0,3 × (N + 6) · 0,25N + 6 = 0,3N + 1,8 ⇒ 0,05N = 4,2 ⇒ N = 84'),
  A('Mavi balıklar','Mavi dilim 120°.','84 × 120 ÷ 360 = 28')],
 'Bir gruba ekleme yapıldığında hem o grubu hem de toplamı artırmayı unutma.',
 dict(A='21, başlangıçtaki sarı balık sayısı.',C='35, başlangıçtaki kırmızı balık sayısı.',D='40: yeni oranı kurarken eklenen 6 balığı toplama katmamak (N ÷ 4 + 6 = 0,3N ⇒ N = 120).',E='84, başlangıçtaki toplam balık sayısı.'),
 TT(A='dikkat',C='dikkat',D='islem',E='dikkat'),sekil=SK)
dl=[('Roman',168),('Bilim',72),('Tarih',120)]
ns=[n for n in range(1,2000) if n*72%360==0 and n*168%360==0 and Fr(n*72//360+12,n+12)==Fr(1,4)]; assert ns==[180]; N=180
tar=N*120//360; assert tar==60 and N*72//360==36 and N*168//360==84
hat=[n for n in range(1,2000) if n*72%360==0 and Fr(n*72//360+12,n)==Fr(1,4)]; assert hat==[240] and 240*120//360==80
s=[36,60,80,84,180]; sirali(s)
SK=tek(daire(dl))
P.K('0005','Bir okul kütüphanesindeki kitapların türlerine göre dağılımı aşağıdaki daire grafiğinde verilmiştir.\nKütüphaneye 12 yeni bilim kitabı bağışlandığında bilim kitapları kütüphanedeki tüm kitapların %25’i olmuştur.\nBuna göre başlangıçta kütüphanede kaç tarih kitabı vardır?',
 [str(v) for v in s],tek_dogru(s,60),'Başlangıçtaki tarih kitabı sayısı.',
 ['Bilim dilimi dairenin kaçta kaçı?','Bağıştan sonra bilim kitapları ve toplam kitap sayısı kaç olur?','Yeni oranı %25’e eşitle; toplamı bulunca tarih dilimini hesapla.'],[DAI,YZB],
 [A('Bilimin payı','72°, dairenin beşte biri.','72 ÷ 360 = 1/5 ⇒ bilim: N ÷ 5'),
  A('Yeni durum','12 bilim kitabı eklenir; toplam da 12 artar.','bilim: N ÷ 5 + 12 · toplam: N + 12'),
  A('Denklem','Yeni bilim oranı %25 = 1/4.','4 × (N ÷ 5 + 12) = N + 12 · 0,8N + 48 = N + 12 ⇒ 0,2N = 36 ⇒ N = 180'),
  A('Tarih kitapları','Tarih dilimi 120°.','180 × 120 ÷ 360 = 60')],
 'Ekleme sonrası oran sorularında payı da paydayı da güncelle; sonra istenen dilimi başlangıç toplamından hesapla.',
 dict(A='36, başlangıçtaki bilim kitabı sayısı.',C='80: yeni oranı kurarken bağışlanan 12 kitabı toplama eklememek (N ÷ 5 + 12 = N ÷ 4 ⇒ N = 240).',D='84, başlangıçtaki roman sayısı.',E='180, başlangıçtaki toplam kitap sayısı.'),
 TT(A='dikkat',C='islem',D='dikkat',E='dikkat'),sekil=SK)

# ===== 0006 ölçeksiz sütun ORTA
et=['Çınar','Lale','Gül','Defne']; bl=[3,5,2,4]; birim=Fr(12,bl[0]); assert birim==4
cev=(bl[1]+bl[3])*birim; assert cev==36
s=[9,27,36,44,56]; sirali(s); assert bl[1]+bl[3]==9 and (bl[1]+bl[3])*Fr(12,4)==27 and (bl[1]+bl[2]+bl[3])*birim==44 and sum(bl)*birim==56
SK=tek(sutun(et,bl,1,6,'Bank sayısı','Parklar',olcek=False))
P.R('0006','grf-sutun',T['grf-sutun'],'orta','Ölçeği verilmemiş sütun','Değerleri yazılmamış eşit bölmeli bir sütun grafiğinde bilinen bir sütundan bir bölmenin değerini bulur ve diğer sütunları okur.','grafik',3,
 'K-GR-02 (ölçeksiz sütun, bir değer verilir) · yeni kurgu (parklardaki banklar), yeni istenen (iki sütunun toplamı)',
 'Bir belediye dört parktaki bank sayılarını aşağıdaki sütun grafiğiyle göstermiştir. Grafiğin dikey eksenindeki sayılar silinmiştir; yatay çizgiler eşit aralıklıdır ve her sütun bir çizgide bitmektedir.\nÇınar Parkı’nda 12 bank olduğuna göre Lale ve Defne parklarındaki bankların toplam sayısı kaçtır?',
 [str(v) for v in s],tek_dogru(s,36),'Lale ve Defne parklarındaki bankların toplamı.',
 ['Çınar sütunu kaç bölme yüksekliğinde?','Bir bölme kaç banka karşılık gelir?','Lale ve Defne sütunlarının bölmelerini toplayıp bir bölmenin değeriyle çarp.'],[BOL],
 [A('Bölmeleri say','Sütunların yükseklikleri (bölme).','Çınar 3 · Lale 5 · Gül 2 · Defne 4'),
  A('Bir bölmenin değeri','Çınar’daki 12 bank 3 bölmeye karşılık gelir.','12 ÷ 3 = 4 bank'),
  A('Lale ve Defne','Toplam bölme sayısını 4 ile çarp.','(5 + 4) × 4 = 36 bank')],
 'Ölçeksiz grafikte önce bir bölmenin değerini bul; sonra her sütunu “bölme sayısı × bölmenin değeri” ile oku.',
 dict(A='9, iki sütunun bölme sayılarının toplamı; bir bölmenin değeriyle çarpılmalı.',B='27: Çınar sütununu 4 bölme okumak (bir bölme 3 bank).',D='44: Lale, Gül ve Defne parklarını toplamak; Gül soruda yok.',E='56, dört parktaki bankların toplamı.'),
 TT(A='dikkat',B='islem',D='dikkat',E='dikkat'),sekil=SK)
et=['İnek','Koyun','Keçi','Tavuk']; bl=[4,7,3,6]; birim=Fr(20,bl[1]-bl[2]); assert birim==5
cev=(bl[0]+bl[3])*birim; assert cev==50
s=[10,20,30,40,50]; sirali(s); assert bl[0]+bl[3]==10 and bl[0]*birim==20 and bl[3]*birim==30 and (bl[0]+bl[3])*Fr(20,5)==40
SK=tek(sutun(et,bl,1,8,'Hayvan sayısı','Hayvan türü',olcek=False))
P.K('0006','Bir çiftlikteki hayvanların türlerine göre sayıları aşağıdaki sütun grafiğinde gösterilmiştir. Dikey eksendeki sayılar okunamamaktadır; yatay çizgiler eşit aralıklıdır ve her sütun bir çizgide bitmektedir.\nÇiftlikteki koyun sayısı keçi sayısından 20 fazla olduğuna göre çiftlikteki inek ve tavukların toplam sayısı kaçtır?',
 [str(v) for v in s],tek_dogru(s,50),'İnek ve tavukların toplam sayısı.',
 ['Koyun ve keçi sütunları arasında kaç bölme fark var?','Bu fark 20 hayvan ise bir bölme kaç hayvan?','İnek ve tavuk sütunlarının bölmelerini toplayıp çarp.'],[BOL],
 [A('Bölmeleri say','Sütunların yükseklikleri (bölme).','İnek 4 · Koyun 7 · Keçi 3 · Tavuk 6'),
  A('Bir bölmenin değeri','Koyun ile keçi arasında 7 − 3 = 4 bölme fark var; bu 20 hayvan.','20 ÷ 4 = 5 hayvan'),
  A('İnek ve tavuk','Toplam bölmeyi 5 ile çarp.','(4 + 6) × 5 = 50 hayvan')],
 'Fark verildiğinde bölme farkını say; farkın değerini bu sayıya bölerek bir bölmeyi bul.',
 dict(A='10, inek ve tavuk sütunlarının bölme sayılarının toplamı.',B='20, yalnız ineklerin sayısı.',C='30, yalnız tavukların sayısı.',D='40: koyun ile keçi arasını 5 bölme saymak (bir bölme 4 hayvan).'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='islem'),sekil=SK)

# ===== 0007 iki grafik ZOR
dl=[('9. sınıf',120),('10. sınıf',100),('11. sınıf',80),('12. sınıf',60)]; yz=[60,45,30,75]; KART=372
pay=[Fr(d*y,100) for (_,d),y in zip(dl,yz)]; assert pay==[72,45,24,45] and sum(pay)==186
bd=Fr(KART,sum(pay)); assert bd==2; N=360*bd; on2=dl[3][1]*bd; cev=on2*Fr(100-yz[3],100); assert (N,on2,cev)==(720,120,30)
assert sum(d*bd*Fr(y,100) for (_,d),y in zip(dl,yz))==KART
s=[15,30,90,120,348]; sirali(s); assert dl[3][1]*Fr(25,100)==15 and on2*Fr(yz[3],100)==90 and N-KART==348
SK=alt_alta(('Şekil 1',daire(dl,H=190,r=70)),('Şekil 2',sutun([a for a,_ in dl],yz,15,90,'Kartı olanlar (%)','Sınıf düzeyi')))
P.R('0007','grf-iki',T['grf-iki'],'zor','İki grafik: dağılım ve oran','Daire grafiğindeki açıları sütun grafiğindeki yüzdelerle birleştirip bir derecenin kaç kişiye karşılık geldiğini bulur; istenen alt grubu hesaplar.','grafik',5,
 'K-GR-07 (daire: dağılım · sütun: her gruptaki yüzde) · yeni kurgu (lise ve kütüphane kartı), yeni istenen (bir alt grubun tümleyeni)',
 'Bir lisedeki öğrencilerin sınıf düzeylerine göre dağılımı Şekil 1’deki daire grafiğinde gösterilmiştir. Her sınıf düzeyinde kütüphane kartı olan öğrencilerin o düzeydeki öğrencilere oranı ise Şekil 2’deki sütun grafiğinde yüzde olarak verilmiştir.\nBu lisede kütüphane kartı olan 372 öğrenci olduğuna göre 12. sınıflardan kütüphane kartı olmayan kaç öğrenci vardır?',
 [str(v) for v in s],tek_dogru(s,30),'12. sınıflardan kütüphane kartı olmayanların sayısı.',
 ['Her dilimin açısını o düzeydeki kart yüzdesiyle çarp; kartlıların toplamı kaç dereceye karşılık gelir?','Bu açı 372 öğrenciye eşitse 1° kaç öğrenci eder?','12. sınıfların sayısını bul; kartı olmayanlar yüzde kaçtır?'],[DAI,DER],
 [A('Kartlıların açı payı','Açı × kart oranı.','120 × 0,6 = 72 · 100 × 0,45 = 45 · 80 × 0,3 = 24 · 60 × 0,75 = 45'),
  A('Topla','Kartlı öğrencilerin toplam açı karşılığı.','72 + 45 + 24 + 45 = 186°'),
  A('Bir derece','186° = 372 öğrenci.','372 ÷ 186 = 2 öğrenci'),
  A('12. sınıflar','Dilim 60°.','60 × 2 = 120 öğrenci'),
  A('Kartı olmayanlar','12. sınıfların %75’inin kartı var, %25’inin yok.','120 × 0,25 = 30 öğrenci')],
 'Dağılım ve oran grafikleri birlikte verildiğinde açı × oran toplamını bilinen sayıya eşle; yüzdeleri tek başına toplama.',
 dict(A='15: bir dereceyi 1 öğrenci sanmak (60 × 0,25); 186 derecelik pay 372 öğrenciye karşılık geliyor.',C='90, 12. sınıflardan kartı olanların sayısı; soru kartı olmayanları soruyor.',D='120, 12. sınıf öğrencilerinin tamamı.',E='348, lisedeki kartı olmayan öğrencilerin tamamı (720 − 372).'),
 TT(A='islem',C='dikkat',D='dikkat',E='dikkat'),sekil=SK)
dl=[('Ankara',150),('İzmir',90),('Bursa',60),('Antalya',60)]; yz=[40,20,30,50]; UZ=252
pay=[Fr(d*y,100) for (_,d),y in zip(dl,yz)]; assert pay==[60,18,18,30] and sum(pay)==126
bd=Fr(UZ,sum(pay)); assert bd==2; izm=dl[1][1]*bd; cev=izm*Fr(yz[1],100); assert (izm,cev)==(180,36)
assert sum(d*bd*Fr(y,100) for (_,d),y in zip(dl,yz))==UZ
s=[18,36,90,144,180]; sirali(s); assert dl[1][1]*Fr(yz[1],100)==18 and izm-cev==144
SK=alt_alta(('Şekil 1',daire(dl,H=190,r=70)),('Şekil 2',sutun([a for a,_ in dl],yz,10,60,'Uzaktan çalışanlar (%)','Şubeler')))
P.K('0007','Bir şirketin dört şubesindeki çalışanların şubelere göre dağılımı Şekil 1’deki daire grafiğinde verilmiştir. Her şubede uzaktan çalışanların o şubedeki tüm çalışanlara oranı ise Şekil 2’deki sütun grafiğinde yüzde olarak gösterilmiştir.\nŞirkette uzaktan çalışan 252 kişi olduğuna göre İzmir şubesinde uzaktan çalışan kaç kişi vardır?',
 [str(v) for v in s],tek_dogru(s,36),'İzmir şubesinde uzaktan çalışanların sayısı.',
 ['Her şubenin açısını uzaktan çalışma yüzdesiyle çarp ve topla.','Bu toplam açı 252 kişiye karşılık geliyorsa 1° kaç kişi?','İzmir şubesinin çalışan sayısını bulup yüzdesini uygula.'],[DAI,DER],
 [A('Uzaktan çalışanların açı payı','Açı × oran.','150 × 0,4 = 60 · 90 × 0,2 = 18 · 60 × 0,3 = 18 · 60 × 0,5 = 30'),
  A('Topla','Uzaktan çalışanların açı karşılığı.','60 + 18 + 18 + 30 = 126°'),
  A('Bir derece','126° = 252 kişi.','252 ÷ 126 = 2 kişi'),
  A('İzmir şubesi','Dilim 90°.','90 × 2 = 180 kişi'),
  A('Uzaktan çalışanlar','İzmir’de oran %20.','180 × 0,2 = 36 kişi')],
 'Açı × yüzde çarpımlarının toplamı, özelliği taşıyanların daire üzerindeki payıdır; bunu bilinen sayıya eşle.',
 dict(A='18: bir dereceyi 1 kişi sanmak (90 × 0,2); 126 derecelik pay 252 kişiye karşılık geliyor.',C='90, İzmir diliminin açısı (°); kişi sayısı değil.',D='144, İzmir’de ofisten çalışanların sayısı.',E='180, İzmir şubesindeki tüm çalışanlar.'),
 TT(A='islem',C='dikkat',D='dikkat',E='dikkat'),sekil=SK)

# ===== 0008 iki grafik (adet + gelir) ZOR
ur=['Defter','Kalem','Çanta','Boya']; ad=[40,120,20,60]; dl=list(zip(ur,[90,60,150,60])); fd=90
der=Fr(fd*ad[0],dl[0][1]); assert der==40; gelir=[d*der for _,d in dl]; fiy=[g/a for g,a in zip(gelir,ad)]
assert fiy==[90,20,300,40] and all(f.denominator==1 for f in fiy) and sum(gelir)==14400
s=[20,40,60,120,2400]; sirali(s); assert Fr(60,90)*fd==60 and Fr(sum(gelir),ad[1])==120 and gelir[1]==2400
SK=alt_alta(('Şekil 1',sutun(ur,ad,20,140,'Satış adedi','Ürünler')),('Şekil 2',daire(dl,H=190,r=70)))
P.R('0008','grf-iki',T['grf-iki'],'zor','İki grafik: adet ve gelir','Bilinen bir fiyattan gelir dağılımında bir derecenin değerini bulur; başka bir ürünün gelirini adedine bölerek fiyatını hesaplar.','grafik',4,
 'K-GR-08 (sütun: adet · daire: gelir dağılımı) · yeni kurgu (kırtasiyenin aylık satışı), yeni istenen (bir ürünün fiyatı)',
 'Bir kırtasiyede ocak ayında satılan dört ürünün satış adetleri Şekil 1’deki sütun grafiğinde, bu ürünlerin satışından elde edilen gelirin ürünlere göre dağılımı ise Şekil 2’deki daire grafiğinde gösterilmiştir.\nHer ürün ay boyunca hep aynı fiyattan satılmıştır ve bir defterin satış fiyatı 90 TL’dir.\nBuna göre bir kalemin satış fiyatı kaç TL’dir?',
 [str(v) for v in s],tek_dogru(s,20),'Bir kalemin satış fiyatı.',
 ['Defterlerden elde edilen gelir kaç TL ve daire grafiğinde kaç dereceye karşılık geliyor?','Bir derece kaç TL gelir eder?','Kalem gelirini bulup satılan kalem sayısına böl.'],[GEL,DER],
 [A('Defter geliri','Fiyat × adet.','90 × 40 = 3600 TL'),
  A('Bir derecenin değeri','Defter dilimi 90°.','3600 ÷ 90 = 40 TL'),
  A('Kalem geliri','Kalem dilimi 60°.','60 × 40 = 2400 TL'),
  A('Kalem fiyatı','Geliri satılan kalem sayısına böl.','2400 ÷ 120 = 20 TL')],
 'Gelir dağılımı verilen grafikte açılar geliri gösterir, fiyatı değil; fiyat için geliri adede böl.',
 dict(B='40, bir derecenin karşılığı (TL); kalemin fiyatı değil.',C='60 = 90 × 60 ÷ 90; fiyat oranını açı oranı sanmak. Açılar geliri gösterir, satış adetleri farklı.',D='120 = 14400 ÷ 120; toplam geliri kalem sayısına bölmek.',E='2400, kalem satışından elde edilen gelir; tek bir kalemin fiyatı değil.'),
 TT(B='dikkat',C='bilgi',D='dikkat',E='dikkat'),sekil=SK)
ur=['Elma','Muz','Kiraz','Portakal']; ad=[50,20,10,40]; dl=list(zip(ur,[90,80,100,90])); fe=36
der=Fr(fe*ad[0],dl[0][1]); assert der==20; gelir=[d*der for _,d in dl]; fiy=[g/a for g,a in zip(gelir,ad)]
assert fiy==[36,80,200,45] and sum(gelir)==7200
s=[36,45,90,180,1800]; sirali(s); assert Fr(gelir[3],ad[1])==90 and Fr(sum(gelir),ad[3])==180 and gelir[3]==1800
SK=alt_alta(('Şekil 1',sutun(ur,ad,10,60,'Satış (kg)','Meyveler')),('Şekil 2',daire(dl,H=190,r=70)))
P.K('0008','Bir manavın bir günde sattığı dört çeşit meyvenin miktarları Şekil 1’deki sütun grafiğinde, bu meyvelerin satışından elde edilen gelirin meyvelere göre dağılımı ise Şekil 2’deki daire grafiğinde verilmiştir.\nHer meyve gün boyunca aynı fiyattan satılmıştır ve elmanın kilogram fiyatı 36 TL’dir.\nBuna göre portakalın kilogram fiyatı kaç TL’dir?',
 [str(v) for v in s],tek_dogru(s,45),'Portakalın kilogram fiyatı.',
 ['Elmadan elde edilen gelir kaç TL ve kaç dereceye karşılık geliyor?','Bir derece kaç TL gelir eder?','Portakal gelirini satılan portakal miktarına böl.'],[GEL,DER],
 [A('Elma geliri','Fiyat × miktar.','36 × 50 = 1800 TL'),
  A('Bir derecenin değeri','Elma dilimi 90°.','1800 ÷ 90 = 20 TL'),
  A('Portakal geliri','Portakal dilimi de 90°.','90 × 20 = 1800 TL'),
  A('Portakal fiyatı','Geliri satılan miktara böl.','1800 ÷ 40 = 45 TL')],
 'Eşit açılı dilimler eşit geliri gösterir; satılan miktarlar farklıysa fiyatlar da farklıdır.',
 dict(A='36: aynı açılı dilimlerin fiyatlarını eşit sanmak; gelirler eşit ama satılan miktarlar farklı.',C='90 = 1800 ÷ 20; portakal gelirini muzun miktarına bölmek.',D='180 = 7200 ÷ 40; toplam geliri portakal miktarına bölmek.',E='1800, portakal satışından elde edilen gelir (TL); kilogram fiyatı değil.'),
 TT(A='bilgi',C='dikkat',D='dikkat',E='dikkat'),sekil=SK)

P.yaz(os.path.join(H,'grafikprob-1.json'),os.path.join(H,'grafikprob-1-kardes.json'))
# önizleme için SVG'leri ayrı dosyalara da yaz (yalnız yerel kontrol; havuza girmez)
if '--svg' in sys.argv:
    d='/tmp/grafikprob-svg'; os.makedirs(d,exist_ok=True)
    for q in P.ANA+P.KAR:
        if q['sekil']: open(f"{d}/{q['id']}.svg",'w').write(q['sekil'].replace('currentColor','#222').replace('var(--acc,#16A34A)','#16A34A'))
