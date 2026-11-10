import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..'))
from ortak import *
import gorsel as G
from fractions import Fraction as Fr
def fm(x):
    x=Fr(x).limit_denominator(10**6); n=x<0; x=abs(x)
    if x.denominator==1: s=str(x.numerator)
    else:
        d=x.denominator
        while d%2==0: d//=2
        while d%5==0: d//=5
        assert d==1,'ondalik degil'
        s=f'{float(x):.6f}'.rstrip('0').rstrip('.').replace('.',',')
    return ('−' if n else '')+s
ORT={}; KARTLAR=[]
def kart(id,alt,fikir,tuzak,zorluk,kalip,adim,tipId,tip,kaynak):
    KARTLAR.append(dict(id=id,konu=KONU,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zorluk,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=kaynak))
def mk(P,no,kard=False,metin=None,dogru=None,yan=None,istenen=None,ad=None,sekil=None,sira=None,ip=None,bilgi=None,puf=None,kisa=None,
       tipId=None,tip=None,z=None,alt=None,kaz=None,kalip=None,adim=None,kart=None):
    vals=[dogru]+[y[0] for y in yan]; assert len(vals)==5
    if all(not isinstance(v,str) for v in vals):
        fv=[Fr(v).limit_denominator(10**6) for v in vals]; assert len(set(fv))==5
        order=sorted(range(5),key=lambda i:fv[i]); siklar=[fm(vals[i]) for i in order]
        pos={i:'ABCDE'[j] for j,i in enumerate(order)}
    else:
        assert sira and sorted(sira)==sorted(vals), (sira,vals)
        siklar=list(sira); pos={i:'ABCDE'[sira.index(vals[i])] for i in range(5)}
    sik=pos[0]
    cel={pos[i+1]:y[1] for i,y in enumerate(yan)}; tur={pos[i+1]:y[2] for i,y in enumerate(yan)}
    if not kard:
        ORT[no]=(ip,bilgi,puf,kisa)
        P.R(no,tipId,tip,z,alt,kaz,kalip,adim,kart,metin,siklar,sik,istenen,ip,bilgi,ad,puf,cel,tur,kisa=kisa,sekil=sekil)
    else:
        o=ORT[no]
        P.K(no,metin,siklar,sik,istenen,ip or o[0],bilgi or o[1],ad,puf or o[2],cel,tur,kisa=kisa if kisa is not None else o[3],sekil=sekil)
def bitir(P,onek,k):
    HV=os.path.join(HD,'..')
    for q in P.ANA: q['kardes']=None
    P.yaz(os.path.join(HD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Fizik çıkmış soruları, MEB 9–10. sınıf müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def T(x,y,s,**k): return G._t(x,y,s,**k)
KONU='Hareket ve Kuvvet'
P=Parti('hareketkuvvet','Hareket ve Kuvvet','fiz|Hareket ve Kuvvet',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 (hareket, kuvvet) · MEB 9. sınıf'
def vt_grafik(pts,xt,yt):
    x0,y0,x1,y1=46,16,304,150; xm=max(p[0] for p in pts)+2; ym=max(p[1] for p in pts)+2
    X=lambda t:x0+(x1-x0)*t/xm; Y=lambda v:y1-(y1-y0)*v/ym
    o=[f'<path d="M{x0} {y0-4} L{x0} {y1} L{x1+6} {y1}" stroke-width="1.6"/>',T(x0-6,y0,'v (m/s)',anchor='end',size=11),T(x1+4,y1+16,'t (s)',anchor='end',size=11)]
    o.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{X(t):.1f} {Y(v):.1f}' for i,(t,v) in enumerate(pts))+'" stroke-width="2.2" style="stroke:var(--acc,#16A34A)"/>')
    for t in xt: o.append(f'<path d="M{X(t)} {y1} l0 4" stroke-width="1.2"/>'+T(X(t),y1+14,str(t),size=11)+(f'<path d="M{X(t)} {y1} L{X(t)} {Y(dict(pts)[t])}" stroke-width="1" stroke-dasharray="3 3"/>' if t in dict(pts) and dict(pts)[t]>0 else ''))
    for v in yt: o.append(f'<path d="M{x0} {Y(v)} l-4 0" stroke-width="1.2"/>'+T(x0-8,Y(v)+4,str(v),anchor='end',size=11)+f'<path d="M{x0} {Y(v)} L{X(max(t for t,vv in pts if vv==v))} {Y(v)}" stroke-width="1" stroke-dasharray="3 3"/>')
    return G._svg(330,176,''.join(o))
def ok(x0,y0,x1,y1,et,tx,ty,anc='middle'):
    import math
    a=math.atan2(y1-y0,x1-x0); hx=[(x1,y1),(x1-9*math.cos(a-0.4),y1-9*math.sin(a-0.4)),(x1-9*math.cos(a+0.4),y1-9*math.sin(a+0.4))]
    return (f'<path d="M{x0} {y0} L{x1} {y1}" stroke-width="2" style="stroke:var(--acc,#16A34A)"/><polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in hx)+'" style="fill:var(--acc,#16A34A);stroke:none"/>'+T(tx,ty,et,anchor=anc,bold=True))
def vektor3(sag,yuk,sol,s=14):
    cx,cy=165,95; o=['<circle cx="165" cy="95" r="3.5" style="fill:currentColor"/>',T(cx+8,cy+16,'O',anchor='start',bold=True)]
    o.append(ok(cx,cy,cx+sag*s,cy,f'{sag} N',cx+sag*s/2,cy-9))
    o.append(ok(cx,cy,cx,cy-yuk*s,f'{yuk} N',cx+8,cy-yuk*s/2,anc='start'))
    o.append(ok(cx,cy,cx-sol*s,cy,f'{sol} N',cx-sol*s/2,cy+17))
    return G._svg(330,170,''.join(o))
kart('K-FZHK-01','Ortalama hız ve sürat','Ortalama hız yer değiştirmenin süreye oranı; yön değişince yoldan küçüktür.','Yolu yer değiştirme saymak.','kolay','hikâyeli',2,'fz-hk-ortalama','Ortalama hız ve sürat',KY)
kart('K-FZHK-02','v–t grafiğinde yer değiştirme','Grafiğin altında kalan alan yer değiştirmedir; parçalara ayrılır.','Tepe hızı × toplam süre almak.','orta','grafik',3,'fz-hk-vt','Hız–zaman grafiği',KY)
kart('K-FZHK-03','Sabit ivmeli hareket','x = v₀t + ½at²; ½ katsayısı ve v₀t terimi birlikte.','½ katsayısını unutmak.','orta','hikâyeli',3,'fz-hk-ivmeli','Sabit ivmeli hareket',KY)
kart('K-FZHK-04','Bileşke kuvvet','Doğrusal kuvvetler işaretle toplanır; dik bileşenlerden Pisagor.','Büyüklükleri aritmetik toplamak.','orta','şekilli',3,'fz-hk-bileske','Bileşke kuvvet',KY)
kart('K-FZHK-05','Yetişme problemi','Sabit hızlı ile ivmeli hareketlinin aynı yolu aldığı an bulunur; sonra hız hesaplanır.','½ katsayısını unutarak süreyi yanlış bulmak.','zor','hikâyeli',4,'fz-hk-yetisme','Yetişme problemi',KY)
kart('K-FZHK-06','Düşey hareketle karşılaşma','Bağıl hızla süre bulunur; v = v₀ − gt ile hız hesaplanır.','Hızları büyüklükçe toplamak.','zor','hikâyeli',5,'fz-hk-dusey','Düşey atış ve serbest düşme',KY)
# 0001
x1,t1,x2,t2=60,20,40,20; xyer=x1-x2; assert Fr(xyer,t1+t2)==Fr(1,2) and Fr(x1+x2,t1+t2)==Fr(5,2) and Fr(xyer,t1)==1 and Fr(x1+x2,t1)==5 and Fr(x1,t1)==3
mk(P,'0001',tipId='fz-hk-ortalama',tip='Ortalama hız ve sürat',z='kolay',alt='Hareket',kaz='Yön değiştiren hareketlide ortalama hızı yer değiştirmeden hesaplar.',kalip='hikâyeli',adim=2,
 kart='K-FZHK-01 (ortalama hız ve sürat) · gidiş–dönüş yeni sayılar',
 metin='Doğrusal bir yolda hareket eden bir koşucu K noktasından doğuya doğru 60 m’yi 20 s’de koşuyor, hemen ardından batıya doğru 40 m’yi 20 s’de koşuyor.\nBuna göre koşucunun tüm hareket boyunca ortalama hızının büyüklüğü kaç m/s’dir?',
 dogru=Fr(1,2),yan=[(1,'Yer değiştirmeyi (20 m) yalnız ilk sürenin (20 s) tamamına bölmüş.','dikkat'),(Fr(5,2),'Yolu (100 m) toplam süreye bölmüş; bu ortalama süratir, ortalama hız değildir.','bilgi'),(3,'Yalnız ilk 20 s’lik hareketin hızını yazmış.','dikkat'),(5,'Yolu (100 m) yalnız ilk sürenin (20 s) tamamına bölmüş.','islem')],
 istenen='Ortalama hızın büyüklüğü (m/s).',ip=['Ortalama hızda toplam yol değil, yer değiştirme kullanılır.'],
 bilgi=[B('Ortalama hız','ortalama hız = yer değiştirme ÷ geçen süre; yer değiştirme ilk ve son konum arasındaki uzaklıktır, yön değiştirince yoldan küçük olur. Örnek: 10 m doğuya, 4 m batıya giden 6 m yer değiştirmiştir')],
 ad=[A('Yer değiştirme','Doğuya 60 m, batıya 40 m gidildiği için son konum K’nin 20 m doğusundadır.','Δx = 60 − 40 = 20 m'),A('Toplam süre','İki hareketin süreleri toplanır.','t = 20 + 20 = 40 s'),A('Ortalama hız','Yer değiştirme toplam süreye bölünür.','v = 20 ÷ 40 = 0,5 m/s')],
 puf='Yön değişiyorsa ortalama hız için önce yer değiştirmeyi bul; yolu kullanma.')
# 0002
pts=[(0,0),(4,8),(10,8),(12,0)]; alan=Fr(4*8,2)+6*8+Fr(2*8,2); assert alan==72 and 8*12==96 and 6*8==48 and Fr(4*8,2)+Fr(2*8,2)==24
mk(P,'0002',tipId='fz-hk-vt',tip='Hız–zaman grafiği',z='orta',alt='Hareket',kaz='Hız–zaman grafiğinin altında kalan alandan yer değiştirmeyi bulur.',kalip='grafik',adim=3,
 kart='K-FZHK-02 (v–t grafiğinin altındaki alan) · yamuk biçimli grafik, yeni değerler',
 metin='Doğrusal yolda hareket eden bir aracın hız–zaman grafiği şekilde verilmiştir.\nBuna göre aracın 0–12 s aralığındaki yer değiştirmesi kaç m’dir?',
 sekil=vt_grafik(pts,[4,10,12],[8]),
 dogru=72,yan=[(8,'Grafikteki en büyük hızı yer değiştirme sanmış.','dikkat'),(24,'Yalnız hızın değiştiği iki bölgenin alanını toplamış.','dikkat'),(48,'Yalnızca sabit hızlı bölgenin alanını bulmuş.','dikkat'),(96,'En büyük hızı toplam süreyle çarpmış (8 × 12); grafiği dikdörtgen saymış.','bilgi')],
 istenen='0–12 s aralığındaki yer değiştirme (m).',ip=['Hız–zaman grafiğinde yer değiştirme, grafikle zaman ekseni arasında kalan alandır.'],
 bilgi=[B('v–t grafiği','grafikle zaman ekseni arasındaki alan yer değiştirmeyi verir. Üçgen alanı = taban × yükseklik ÷ 2, dikdörtgen alanı = taban × yükseklik. Örnek: 5 m/s hızla 3 s giden 15 m gider')],
 ad=[A('Grafiği parçala','Grafik üç bölgeden oluşur: 0–4 s, 4–10 s, 10–12 s.','üçgen · dikdörtgen · üçgen'),A('Alanları bul','Her bölgenin alanı ayrı hesaplanır.','A₁ = 4 × 8 ÷ 2 = 16 · A₂ = 6 × 8 = 48 · A₃ = 2 × 8 ÷ 2 = 8'),A('Topla','Alanlar toplanarak yer değiştirme bulunur.','Δx = 16 + 48 + 8 = 72 m')],
 puf='v–t grafiklerinde şekli üçgen ve dikdörtgenlere ayır, alanları topla.')
# 0003
v0,a,t=5,3,4; x=v0*t+Fr(a*t*t,2); assert x==44 and v0*t==20 and v0*t+a*t==32 and (v0+a*t)*t==68 and a*t==12 and v0+a*t==17
mk(P,'0003',tipId='fz-hk-ivmeli',tip='Sabit ivmeli hareket',z='orta',alt='Hareket',kaz='Sabit ivmeli doğrusal harekette alınan yolu hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-FZHK-03 (x = v₀t + ½at²) · yeni değerler, ilk hız var',
 metin='Doğrusal yolda 5 m/s hızla giden bir bisikletli, hareket yönünde sabit 3 m/s² ivmeyle hızlanmaya başlıyor.\nBuna göre bisikletlinin hızlanmaya başladığı andan sonraki 4 s içinde aldığı yol kaç m’dir?',
 dogru=44,yan=[(12,'Yolu ½at² yerine a × t (3 × 4) olarak hesaplamış.','bilgi'),(17,'4 s sonundaki hızı (17 m/s) alınan yol sanmış.','dikkat'),(20,'İvmenin etkisini atlayıp yalnız v₀ × t almış.','dikkat'),(32,'½ katsayısını unutarak v₀t + at hesaplamış.','bilgi')],
 istenen='4 s içinde alınan yol (m).',ip=['Yol için v₀ × t terimine ivmeden gelen ½ × a × t² terimini ekle.'],
 bilgi=[B('Sabit ivmeli hareket','x = v₀ × t + ½ × a × t². Örnek: v₀ = 2 m/s, a = 2 m/s², t = 3 s için x = 6 + 9 = 15 m')],
 ad=[A('Bağıntıyı yaz','Başlangıç hızı ve sabit ivme birlikte verildiğinden iki terim vardır.','x = v₀ × t + ½ × a × t²'),A('Terimleri hesapla','Değerleri yerine koy.','v₀ × t = 5 × 4 = 20 m · ½ × a × t² = ½ × 3 × 16 = 24 m'),A('Topla','İki terim toplanır.','x = 20 + 24 = 44 m')],
 puf='İvmeli harekette yol, başlangıç hızıyla alınan yol ile ivmeden gelen ½at² teriminin toplamıdır.')
# 0004
sag,yuk,sol=7,4,4; fx=sag-sol; fy=yuk; import math; F=math.hypot(fx,fy); assert F==5 and sag+yuk+sol==15
mk(P,'0004',tipId='fz-hk-bileske',tip='Bileşke kuvvet',z='orta',alt='Kuvvet',kaz='Aynı noktaya etkiyen kuvvetlerin bileşkesini dik bileşenlerle bulur.',kalip='şekilli',adim=3,
 kart='K-FZHK-04 (bileşke kuvvet) · üç kuvvet, dik bileşenler',
 metin='Şekilde O noktasına yatay ve düşey doğrultuda üç kuvvet etki etmektedir (sağ yön doğu, yukarı yön kuzeydir).\nBuna göre bu kuvvetlerin bileşkesinin büyüklüğü kaç N’dur?',
 sekil=vektor3(7,4,4),
 dogru=5,yan=[(3,'Yalnız yatay doğrultudaki bileşkeyi (7 − 4) yazmış.','dikkat'),(4,'Yalnız düşey kuvveti bileşke sanmış.','dikkat'),(7,'Yalnız doğuya olan kuvveti bileşke sanmış.','dikkat'),(15,'Büyüklükleri yönlerine bakmadan toplamış (7 + 4 + 4).','bilgi')],
 istenen='Bileşke kuvvetin büyüklüğü (N).',ip=['Önce yatay doğrultudaki kuvvetleri kendi aralarında işaretle topla.'],
 bilgi=[B('Bileşke kuvvet','aynı doğrultudaki zıt yönlü kuvvetler çıkarılır; birbirine dik iki bileşke varsa büyüklük R = √(Rx² + Ry²). Örnek: 3 N ve 4 N dik kuvvetlerin bileşkesi 5 N’dur')],
 ad=[A('Yatay bileşke','Doğuya 7 N, batıya 4 N vardır; zıt yönler çıkarılır.','Rx = 7 − 4 = 3 N (doğu)'),A('Düşey bileşke','Düşey doğrultuda yalnız kuzeye 4 N vardır.','Ry = 4 N (kuzey)'),A('Dik bileşkeleri birleştir','Dik bileşenler Pisagor ile birleşir.','R² = 3² + 4² = 25 · R = 5 N')],
 puf='Önce her doğrultunun bileşkesini işaretle bul, sonra dik iki bileşkeyi Pisagor ile birleştir.')
# 0005
vK,aL=10,2; tt=Fr(2*vK,aL); vL=aL*tt; assert tt==10 and vL==20 and vK*tt==Fr(aL*tt*tt,2) and Fr(vK,aL)==5 and (vK+vL)/2==15
mk(P,'0005',tipId='fz-hk-yetisme',tip='Yetişme problemi',z='zor',alt='Hareket',kaz='Sabit hızlı ve ivmeli hareketlinin buluşma anını bulup hızı hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-FZHK-05 (yetişme) · L’nin yetişme anındaki hızı istenen',
 metin='Aynı doğru boyunca ve aynı yönde hareket eden K ve L araçları t = 0 anında aynı noktadan geçiyor. K sabit 10 m/s hızla gidiyor; L ise o anda durgun halden başlayarak 2 m/s² sabit ivmeyle hızlanıyor.\nBuna göre L aracı K’ya yetiştiği anda hızı kaç m/s’dir?',
 dogru=20,yan=[(2,'İvmeyi (2 m/s²) hız sanmış.','dikkat'),(5,'½ katsayısını unutarak 10t = 2t² yazmış, t = 5 s bulup L’nin hızı yerine zamanı yazmış.','dikkat'),(10,'Yetiştiği anda hızların eşit (10 m/s) olduğunu sanmış.','bilgi'),(15,'K’nin hızı ile L’nin son hızının ortalamasını almış.','bilgi')],
 istenen='L’nin yetişme anındaki hızı (m/s).',ip=['Yetiştiği anda iki aracın aldığı yol eşittir: K için v × t, L için ½ × a × t².'],
 bilgi=[B('Sabit ivmeli hareket','x = ½ × a × t² (durgun başlayan için), v = a × t. Sabit hızda x = v × t. Örnek: durgun başlayıp 2 m/s² ivmeyle 3 s giden 9 m yol alır, hızı 6 m/s olur')],
 ad=[A('Yolları eşitle','Yetiştiklerinde iki araç da aynı yolu almıştır.','10 × t = ½ × 2 × t²'),A('Zamanı bul','t’yi sadeleştirip çöz.','10 = t ; t = 10 s'),A('L’nin hızı','Durgun başlayan L’nin hızı a × t’dir.','v = 2 × 10 = 20 m/s'),A('Kontrol','Alınan yollar eşit olmalıdır.','K: 10 × 10 = 100 m ; L: ½ × 2 × 100 = 100 m')],
 puf='Yetişme sorularında yolları eşitle, süreyi bul; sonra istenen hız ya da yolu hesapla.')
# 0006
H,v0,g=60,20,10; tt=Fr(H,v0); vB=v0-g*tt; vA=g*tt; assert tt==3 and vB==-10 and vA==30 and abs(vB)+vA==40 and Fr(H,2)==30
mk(P,'0006',tipId='fz-hk-dusey',tip='Düşey atış ve serbest düşme',z='zor',alt='Hareket',kaz='Aynı anda başlayan serbest düşme ve düşey atışın karşılaşma anını bulur.',kalip='hikâyeli',adim=5,
 kart='K-FZHK-06 (düşey karşılaşma) · karşılaşma anında hız istenen',
 metin='Yerden 60 m yükseklikteki bir noktadan A cismi serbest bırakılırken aynı anda aynı düşey doğrultudaki yerden B cismi 20 m/s hızla düşey yukarı fırlatılıyor.\nHava direnci ihmal edildiğine ve g = 10 m/s² olduğuna göre cisimler karşılaştığı anda B’nin hızının büyüklüğü kaç m/s’dir?',
 dogru=10,yan=[(0,'B’nin hızını karşılaşma anında sıfır (en üst nokta) sanmış.','dikkat'),(20,'B’nin ilk hızını karşılaşma anındaki hız sanmış.','dikkat'),(30,'A’nın karşılaşma anındaki hızını (30 m/s) B’nin hızı sanmış.','dikkat'),(40,'A’nın ve B’nin hızlarını toplamış; soru yalnız B’nin hızını soruyor.','dikkat')],
 istenen='Karşılaşma anında B’nin hızının büyüklüğü (m/s).',ip=['Cisimler birbirine yaklaşırken ikisine de aynı g ivmesi etki ettiğinden aradaki mesafe, ilk hızların toplamı (0 + 20 = 20 m/s) olan sabit bir bağıl hızla kapanır.'],
 bilgi=[B('Düşey atış ve serbest düşme','serbest bırakılan cismin hızı v = g × t. Yukarı atılan cismin hızı v = v₀ − g × t; eksi çıkarsa cisim aşağı iniyordur. Örnek: 20 m/s ile atılan cisim 3 s sonra 20 − 30 = −10 m/s hıza sahip olur (10 m/s aşağı)')],
 ad=[A('Bağıl hız','A ilk hızsız bırakılır, B 20 m/s ile yukarı atılır; ikisine de aynı g ivmesi etki ettiği için bağıl hız değişmez ve ilk hızların toplamına eşittir.','v(bağıl) = 0 + 20 = 20 m/s'),A('Karşılaşma süresi','Aradaki 60 m bu hızla kapanır.','t = 60 ÷ 20 = 3 s'),A('B’nin hızı','Yukarı atılan cisim için v = v₀ − g × t.','v = 20 − 10 × 3 = −10 m/s'),A('Yön ve büyüklük','Eksi işaret B’nin aşağı doğru indiğini gösterir; büyüklük 10 m/s’dir.','|v| = 10 m/s'),A('Kontrol','Karşılaşma yüksekliği iki cisim için de aynı çıkmalıdır.','A: 60 − ½ × 10 × 9 = 15 m ; B: 20 × 3 − 45 = 15 m')],
 puf='Aynı anda başlayan düşey hareketlerde yerçekimi etkisi sadeleşir; süre, mesafenin ilk hızlar toplamına bölümüyle bulunur.')
bitir(P,'hareketkuvvet','fiz|Hareket ve Kuvvet')
