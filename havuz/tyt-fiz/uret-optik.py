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
    P.yaz(os.path.join(HD,f'{onek}-1.json'),os.path.join(HD,f'{onek}-1-kardes.json'))
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Fizik çıkmış soruları, MEB 9–10. sınıf müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def T(x,y,s,**k): return G._t(x,y,s,**k)
import math
def _ok(x1,y1,x2,y2,w=1.6):
    a=math.atan2(y2-y1,x2-x1); L=7
    p1=(x2-L*math.cos(a-0.4),y2-L*math.sin(a-0.4)); p2=(x2-L*math.cos(a+0.4),y2-L*math.sin(a+0.4))
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-width="{w}"/><path d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}" stroke-width="{w}"/>'
def eksen(tur,ustler,altlar,cisim,birim=36):
    """tur: 'ayna' (çukur ayna sağda) | 'mercek' (ortada). ustler: {konum: etiket} (eksen üstünde F, M gibi); altlar: {konum: harf};
    konumlar aynadan/mercekten sola doğru birim cinsinden; mercekte sağ taraf simetrik ustler'le işaretlenir. cisim=(konum,etiket)."""
    W,H,y=330,130,78; x0=290 if tur=='ayna' else 165; o=[]
    o.append(_ok(14,y,W-10,y,1.2))
    if tur=='ayna':
        o.append(f'<path d="M{x0} 28 Q{x0+18} {y} {x0} 128" stroke-width="2.4"/>')
        for t in range(0,5): yy=40+t*20; o.append(f'<line x1="{x0+ (4 if 0<t<4 else 1)}" y1="{yy}" x2="{x0+9}" y2="{yy+6}" stroke-width="1"/>')
    else:
        o.append(_ok(x0,y,x0,22,1.8)); o.append(_ok(x0,y,x0,134,1.8))
    for p,l in ustler.items():
        xs=[x0-p*birim]+([x0+p*birim] if tur=='mercek' else [])
        for x in xs: o.append(f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" stroke-width="1.4"/>'); o.append(T(x,y-9,l,size=11,bold=True))
    for p,l in altlar.items():
        x=x0-p*birim; o.append(f'<line x1="{x}" y1="{y-3}" x2="{x}" y2="{y+3}" stroke-width="1.4"/>'); o.append(T(x,y+17,l,size=12,bold=True))
    cp,cl=cisim; cx=x0-cp*birim
    o.append(_ok(cx,y,cx,y-34,2.2)); o.append(T(cx,y-40,cl,size=11,renk=G.ACC,bold=True))
    return G._svg(W,H,''.join(o))
def kirilma(a1,a2,ust,alt):
    W,H=330,170; cx,cy=165,85; L=68; o=[]
    o.append(f'<line x1="20" y1="{cy}" x2="310" y2="{cy}" stroke-width="1.6"/>'); o.append(f'<line x1="{cx}" y1="14" x2="{cx}" y2="158" stroke-dasharray="4 3" stroke-width="1" opacity=".6"/>')
    r=math.radians
    sx,sy=cx-L*math.sin(r(a1)),cy-L*math.cos(r(a1)); ex,ey=cx+L*math.sin(r(a2)),cy+L*math.cos(r(a2))
    o.append(_ok(sx,sy,cx,cy,2)); o.append(_ok(cx,cy,ex,ey,2))
    o.append(T(300,cy-8,ust,anchor='end',size=12,bold=True)); o.append(T(300,cy+18,alt,anchor='end',size=12,bold=True))
    o.append(T(cx+6,cy-18-0,'normal',anchor='start',size=10)); 
    o.append(T(cx-46*math.sin(r(a1/2)),cy-46*math.cos(r(a1/2))+4,f'{a1}°',size=12,bold=True,renk=G.ACC)); o.append(T(cx+50*math.sin(r(a2/2)),cy+50*math.cos(r(a2/2))+4,f'{a2}°',size=12,bold=True,renk=G.ACC))
    return G._svg(W,H,''.join(o))
def boy_ayna(boy,goz,uzak):
    """boy, goz m; birim 52 px/m. Kişi solda, duvar/ayna sağda kesik çizgi."""
    boy=float(boy); goz=float(goz); uzak=float(uzak)
    s=52; W,H=330,int(boy*s+50); yg=H-18; x=70; xa=x+uzak*60; o=[]
    o.append(f'<line x1="14" y1="{yg}" x2="320" y2="{yg}" stroke-width="1.6"/>')
    yt=yg-boy*s; yge=yg-goz*s
    o.append(f'<line x1="{x}" y1="{yg}" x2="{x}" y2="{yt+9}" stroke-width="3"/><circle cx="{x}" cy="{yt+5}" r="6" stroke-width="2"/>')
    o.append(f'<circle cx="{x}" cy="{yge:.1f}" r="2.6" style="fill:{G.ACC};stroke:none"/>')
    o.append(f'<line x1="{xa}" y1="{yg}" x2="{xa}" y2="{yt-8}" stroke-dasharray="5 4" stroke-width="2.2"/>'); o.append(T(xa+8,yt+4,'ayna',anchor='start',size=12,bold=True))
    o.append(f'<line x1="{x-20}" y1="{yt}" x2="{x-8}" y2="{yt}" stroke-width="1"/><line x1="{x-14}" y1="{yt}" x2="{x-14}" y2="{yg}" stroke-width="1"/>'); o.append(T(x-18,(yt+yg)/2+4,fm(boy)+' m',anchor='end',size=11))
    o.append(T(x+10,yge+4,'göz: '+fm(goz)+' m',anchor='start',size=11,renk=G.ACC,bold=True))
    o.append(f'<line x1="{x}" y1="{yg+10}" x2="{xa}" y2="{yg+10}" stroke-width="1"/>'); o.append(T((x+xa)/2,yg+9-2,fm(uzak)+' m',size=11))
    return G._svg(W,H+10,''.join(o))
KONU='Optik'
P=Parti('optik','Optik','fiz|Optik',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (optik) · MEB 9–10. sınıf'
kart('K-FZOP-01','Mesafe ve aydınlanma','Noktasal kaynakta E = I/d²: uzaklık oranının karesiyle ters orantı.','Orantıyı uzaklıkla doğrusal almak; oranı ters kurmak.','kolay','hikâyeli',2,'fz-op-aydinlanma','Aydınlanma şiddeti',KY)
kart('K-FZOP-02','Düzlem ayna uzaklığı','Görüntü aynadan cisim kadar uzaktadır; cisim–görüntü arası aynaya uzaklığın 2 katıdır.','Aynaya uzaklıkla cisim–görüntü arasını karıştırmak.','kolay','hikâyeli',2,'fz-op-duzlem-ayna','Düzlem aynada görüntü',KY)
kart('K-FZOP-03','Renkli ışıkta cisim','Cisim yalnız kendi renginin bileşenlerini yansıtır; ışıkta o bileşen yoksa siyah görünür.','Cismin rengini ışığın rengiyle aynı sanmak.','orta','öncüllü',3,'fz-op-renk','Işık ve cisim rengi',KY)
kart('K-FZOP-04','Snell yasası','Normalden ölçülen açılarla n = sin θ₁ / sin θ₂, hız v = c / n.','Açıları yüzeyden ölçmek; sinüs oranını ters yazmak.','orta','şekilli',3,'fz-op-kirilma','Işığın kırılması',KY)
kart('K-FZOP-05','Çukur ayna görüntüsü','Cismin F, M’ye göre konumundan görüntünün yeri ve özelliği (gerçek/sanal, ters/düz, büyük/küçük).','Görüntü yerini cisim yeriyle karıştırmak; F–M aralığını ters kurmak.','orta','öncüllü',4,'fz-op-kure-ayna','Küresel aynada görüntü',KY)
kart('K-FZOP-06','Mercekte görüntü','İnce kenarlı mercekte cismin konumu değişince görüntünün yeri ve boyu nasıl değişir.','Gerçek–sanal geçişini F noktasında aramamak.','orta','öncüllü',4,'fz-op-mercek','Mercekte görüntü',KY)
kart('K-FZOP-07','Eşit aydınlanma noktası','İki kaynağın aydınlanması eşitlenir: I₁/d₁² = I₂/d₂²; kareköklü oran kurulur.','Şiddet oranını doğrusal almak; uzaklığı yanlış kaynaktan ölçmek.','zor','hikâyeli',5,'fz-op-aydinlanma','Aydınlanma şiddeti',KY)
kart('K-FZOP-08','Boy görme','Aynada boyun tamamını görme: yansıma noktaları göz ile uçlar arasındaki yüksekliklerin ortasındadır.','Ayna boyunu göz yüksekliğine göre değil boya göre almak.','zor','şekilli',5,'fz-op-duzlem-ayna','Düzlem aynada görüntü',KY)
AYD=B('Aydınlanma şiddeti','noktasal kaynağın ışık şiddeti I, ekranın uzaklığı d ise aydınlanma E = I ÷ d². Uzaklık 2 katına çıkarsa aydınlanma 4’te 1’ine düşer (birim: lüks, lx)')
DZ=B('Düzlem ayna','görüntü aynanın arkasındadır ve aynadan cisim kadar uzaktır. Cisim ile görüntü arası = 2 × (cismin aynaya uzaklığı). Örnek: cisim aynadan 2 m uzaktaysa görüntüsü ile arası 4 m')
RK=B('Işık ve cisim rengi','kırmızı, yeşil ve mavi ana renklerdir; sarı = kırmızı + yeşil, mor = kırmızı + mavi, camgöbeği = yeşil + mavi. Cisim yalnız kendi rengindeki bileşenleri yansıtır, kalanını soğurur; yansıtacak bileşen yoksa siyah görünür')
# ---- 0001
assert Fr(90)*Fr(2,6)**2==10 and Fr(90,4)==Fr(45,2) and 90*Fr(2,6)==30
mk(P,'0001',tipId='fz-op-aydinlanma',tip='Aydınlanma şiddeti',z='kolay',alt='Aydınlanma',kaz='Noktasal kaynağın aydınlanma şiddetinin uzaklıkla değişimini oranla hesaplar.',kalip='hikâyeli',adim=2,
 kart='K-FZOP-01 (uzaklık ve aydınlanma) · yeni uzaklıklar ve ekran kaydırma',
 metin='Işık şiddeti değişmeyen noktasal bir ışık kaynağından 2 m uzaktaki bir ekranın aydınlanma şiddeti 90 lüks (lx)’tür.\nEkran kaynaktan 6 m uzaklığa götürülürse ekranın aydınlanma şiddeti kaç lüks olur?',
 dogru=10,yan=[(Fr(45,2),'Uzaklık farkını (6 − 2 = 4) kullanıp 90 ÷ 4 almış.','bilgi'),(30,'Aydınlanmanın uzaklıkla doğrusal (ters) orantılı olduğunu sanıp 90 ÷ 3 almış.','bilgi'),(270,'Uzaklık arttığında aydınlanmanın da 3 kat arttığını sanmış.','dikkat'),(810,'Uzaklık oranının karesiyle (9) çarpmış; ters orantıyı atlamış.','dikkat')],
 istenen='Ekran 6 m uzaktayken aydınlanma şiddeti (lx).',
 ip=['Aydınlanma, uzaklığın karesiyle ters orantılıdır.','Uzaklık kaç kat artıyor? Aydınlanma bunun karesi kadar azalır.','Önce uzaklık oranını bul, sonra karesini al.'],
 bilgi=[AYD],
 ad=[A('Uzaklık oranı','Ekran 2 m’den 6 m’ye gidiyor; uzaklık 3 katına çıkıyor.','6 ÷ 2 = 3 kat'),A('Aydınlanmanın değişimi','Aydınlanma uzaklığın karesiyle ters orantılı olduğundan 3² = 9 kat azalır.','E′ = 90 ÷ 9'),A('Sonuç','Yeni aydınlanma şiddeti.','E′ = 10 lx')],
 puf='Aydınlanmada uzaklık kaç kat artarsa aydınlanma o sayının karesi kadar azalır.')
assert 16*Fr(5,2)**2==100 and 16*Fr(5,2)==40 and 16*Fr(2,5)**2==Fr(64,25)
mk(P,'0001',True,metin='Işık şiddeti sabit noktasal bir lambanın 5 m uzağındaki duvarın aydınlanma şiddeti 16 lx’tir.\nDuvar ile lamba arası 2 m’ye düşürülürse duvarın aydınlanma şiddeti kaç lx olur?',
 dogru=100,yan=[(Fr(64,25),'Oranı ters kurup uzaklığın karesiyle çarpmış: 16 × (2/5)².','islem'),(40,'Aydınlanmanın uzaklıkla ters orantılı olduğunu sanıp 16 × 5 ÷ 2 almış.','bilgi'),(80,'16 ile uzaklığı (5) çarpmış.','islem'),(16,'Aydınlanmanın uzaklıkla değişmediğini sanıp ilk değeri yazmış.','dikkat')],
 istenen='Lamba 2 m uzaktayken aydınlanma şiddeti (lx).',
 ad=[A('Uzaklık oranı','Uzaklık 5 m’den 2 m’ye iniyor; uzaklık 2,5 kat azalıyor.','5 ÷ 2 = 2,5 kat'),A('Aydınlanmanın değişimi','Uzaklık azalınca aydınlanma uzaklık oranının karesi kadar artar.','2,5² = 6,25 kat'),A('Sonuç','Yeni aydınlanma şiddeti.','E′ = 16 × 6,25 = 100 lx')])
# ---- 0002
assert 2*(3-1)==4 and 2*3==6
mk(P,'0002',tipId='fz-op-duzlem-ayna',tip='Düzlem aynada görüntü',z='kolay',alt='Düzlem Ayna',kaz='Düzlem aynada cisim–görüntü uzaklığını konum değişimiyle bulur.',kalip='hikâyeli',adim=2,
 kart='K-FZOP-02 (cisim–görüntü uzaklığı) · yeni kurgu, cisim aynaya yaklaşıyor',
 metin='Düzlem aynanın 3 m önünde duran bir öğrenci, aynaya doğru 1 m yürüyor.\nBuna göre yürüdükten sonra öğrenci ile görüntüsü arasındaki uzaklık kaç m’dir?',
 dogru=4,yan=[(2,'Öğrencinin aynaya olan uzaklığını (2 m) cevap sanmış.','dikkat'),(5,'İlk cisim–görüntü uzaklığından (6 m) 1 m çıkarmış; görüntünün de 1 m yaklaştığını atlamış.','bilgi'),(6,'Başlangıçtaki cisim–görüntü uzaklığını (2 × 3) yazmış; yürüyüşü hesaba katmamış.','dikkat'),(8,'Öğrencinin aynadan 4 m uzaklaştığını sanmış (3 + 1 = 4; 2 × 4).','dikkat')],
 istenen='Yürüdükten sonra öğrenci ile görüntüsü arası (m).',
 ip=['Görüntü, aynanın arkasında ve öğrenci kadar uzaktadır.','Yürüdükten sonra öğrencinin aynaya uzaklığı kaç m?','Öğrenci ile görüntü arasındaki uzaklık, aynaya uzaklığın 2 katıdır.'],
 bilgi=[DZ],
 ad=[A('Yeni uzaklık','Öğrenci aynaya yaklaştığı için uzaklık azalır.','3 − 1 = 2 m'),A('Görüntü','Görüntü de aynanın arkasında 2 m uzaktadır.','görüntü: 2 m'),A('Sonuç','Öğrenci ile görüntü arası iki uzaklığın toplamıdır.','2 + 2 = 4 m')],
 puf='Düzlem aynada cisim ile görüntü arasındaki uzaklık hep aynaya uzaklığın iki katıdır.')
assert 2*(4+1)==10
mk(P,'0002',True,metin='Bir cisim, bir düzlem aynanın 4 m önündedir. Cisim sabit tutulup ayna cisimden 1 m uzaklaştırılıyor.\nBuna göre ayna uzaklaştırıldıktan sonra cisim ile görüntüsü arasındaki uzaklık kaç m olur?',
 dogru=10,yan=[(5,'Cismin yeni aynaya olan uzaklığını (5 m) cevap sanmış.','dikkat'),(6,'Görüntünün aynadan uzaklığına (5 m) kaydırmayı (1 m) eklemiş.','islem'),(8,'Başlangıçtaki cisim–görüntü uzaklığını (2 × 4) yazmış; aynanın kaymasını hesaba katmamış.','dikkat'),(9,'Başlangıçtaki uzaklığa (8 m) yalnızca 1 m eklemiş; görüntünün de aynayla birlikte kaydığını atlamış.','bilgi')],
 istenen='Ayna kaydırıldıktan sonra cisim ile görüntü arası (m).',
 ip=['Cismin aynaya olan yeni uzaklığını bul.','Görüntü, aynanın arkasında cisim kadar uzaktadır.','Cisim ile görüntü arası, aynaya uzaklığın 2 katıdır.'],
 ad=[A('Yeni uzaklık','Ayna uzaklaştığı için cismin aynaya uzaklığı artar.','4 + 1 = 5 m'),A('Görüntü','Görüntü aynanın arkasında 5 m uzaktadır.','görüntü: 5 m'),A('Sonuç','Cisim ile görüntü arası iki uzaklığın toplamıdır.','5 + 5 = 10 m')])
# ---- 0003  renk (öncüllü)
# sarı cisim: K+Y yansıtır. Işık: kırmızı→kırmızı, mavi→siyah, yeşil→yeşil
S3=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III']
mk(P,'0003',tipId='fz-op-renk',tip='Işık ve cisim rengi',z='orta',alt='Renk',kaz='Renkli ışık altında cismin görünen rengini ışığın ve cismin bileşenlerinden belirler.',kalip='öncüllü',adim=3,
 kart='K-FZOP-03 (renkli ışıkta cisim) · yeni cisim rengi, öncüllü',
 metin='Beyaz ışıkta sarı görünen bir cisim, karanlık odada ayrı ayrı aşağıdaki saf renkli ışıklarla aydınlatılıyor.\nI. Kırmızı\nII. Mavi\nIII. Yeşil\nBuna göre bu ışıklardan hangileriyle aydınlatıldığında cisim, ışığın rengiyle aynı renkte görünür?',
 dogru='I ve III',sira=S3,yan=[('Yalnız I','Sarı cismin yeşil ışığı da yansıttığını atlamış (sarı = kırmızı + yeşil).','dikkat'),('Yalnız II','Cismin mavi ışığı yansıttığını sanmış; sarı cisim maviyi soğurur, siyah görünür.','bilgi'),('II ve III','Mavi ışıkta cismin mavi görüneceğini sanmış; cisimde mavi bileşen yoktur.','bilgi'),('I, II ve III','Cismin her ışığı yansıttığını sanmış; sarı cisim maviyi soğurur.','bilgi')],
 istenen='Cismin ışığın rengiyle aynı renkte göründüğü ışıklar.',
 ip=['Sarı, hangi iki ana rengin birleşimidir?','Cisim yalnızca kendi bileşenlerini yansıtır, diğerlerini soğurur.','Işıkta cismin yansıtabileceği bir bileşen var mı, her ışık için ayrı bak.'],
 bilgi=[RK],
 ad=[A('Cismin yansıttığı renkler','Sarı = kırmızı + yeşil. Sarı cisim kırmızıyı ve yeşili yansıtır, maviyi soğurur.','yansıtır: kırmızı, yeşil · soğurur: mavi'),A('Işıkları sına','Kırmızı ışık yansır, cisim kırmızı görünür. Mavi ışık soğurulur, cisim siyah görünür. Yeşil ışık yansır, cisim yeşil görünür.','I: kırmızı · II: siyah · III: yeşil'),A('Sonuç','Işığın rengiyle aynı renkte görünme yalnız I ve III’te olur.','I ve III')],
 puf='Renkli ışıkta cisim, ışığın rengi cismin yansıttığı renklerden biriyse o renkte, değilse siyah görünür.')
S3k=['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III']
mk(P,'0003',True,metin='Beyaz ışıkta mor görünen bir cisim, karanlık odada ışık kaynaklarıyla aydınlatılıyor.\nBuna göre;\nI. sarı ışıkta kırmızı,\nII. camgöbeği ışıkta mavi,\nIII. yeşil ışıkta mor\ngörünür ifadelerinden hangileri doğrudur?',
 dogru='I ve II',sira=S3k,yan=[('Yalnız I','Camgöbeği (yeşil + mavi) ışıktaki mavi bileşenin yansıdığını atlamış.','dikkat'),('Yalnız II','Sarı (kırmızı + yeşil) ışıktaki kırmızı bileşenin yansıdığını atlamış.','dikkat'),('Yalnız III','Mor cismin yeşil ışıkta mor görüneceğini sanmış; cismin yeşil bileşeni yoktur, siyah görünür.','bilgi'),('II ve III','Yeşil ışıkta cismin mor göründüğünü sanmış; cisim yeşili soğurur.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['Mor, hangi iki ana rengin birleşimidir?','Her ışığın hangi bileşenlerinden cismin yansıtabildiği var mı, ayrı ayrı bak.','Yansıtılacak bileşen kalmıyorsa cisim siyah görünür.'],
 ad=[A('Cismin yansıttığı renkler','Mor = kırmızı + mavi. Mor cisim kırmızıyı ve maviyi yansıtır, yeşili soğurur.','yansıtır: kırmızı, mavi · soğurur: yeşil'),A('İfadeleri sına','Sarı ışık = kırmızı + yeşil: kırmızı yansır, yeşil soğurulur, cisim kırmızı görünür. Camgöbeği ışık = yeşil + mavi: mavi yansır, cisim mavi görünür. Yeşil ışık soğurulur, cisim siyah görünür.','I: doğru · II: doğru · III: yanlış'),A('Sonuç','Doğru ifadeler I ve II.','I ve II')])
# ---- 0004 Snell
assert Fr(8,10)/Fr(6,10)==Fr(4,3) and Fr(3,4)*1==Fr(3,4)
K4=['3/4','4/5','5/4','4/3','5/3']
mk(P,'0004',tipId='fz-op-kirilma',tip='Işığın kırılması',z='orta',alt='Kırılma',kaz='Işığın iki ortam sınırındaki kırılmasında kırılma indisini açılardan bulur.',kalip='şekilli',adim=3,
 kart='K-FZOP-04 (Snell yasası, kırılma indisi) · yeni açılar, havadan sıvıya',
 metin='Şekildeki gibi havadan bir sıvıya gelen tek renkli ışık, normalle 53° açı yaparak gelip 37° açıyla kırılıyor.\nHavanın kırılma indisi 1, sin 37° = 0,6 ve sin 53° = 0,8 olduğuna göre sıvının kırılma indisi kaçtır?',
 sekil=kirilma(53,37,'Hava','Sıvı'),
 dogru='4/3',sira=K4,yan=[('3/4','Sinüs oranını ters yazmış: sin 37° ÷ sin 53°.','islem'),('4/5','Yalnızca sin 53° değerini (0,8) kırılma indisi sanmış.','dikkat'),('5/4','1 ÷ sin 53° işlemini yapmış; sin 37°’yi hiç kullanmamış.','bilgi'),('5/3','1 ÷ sin 37° işlemini yapmış; sin 53°’yi hiç kullanmamış.','bilgi')],
 istenen='Sıvının kırılma indisi.',
 ip=['Snell yasası: n₁ × sin θ₁ = n₂ × sin θ₂.','Açılar normalden ölçülür; şekildeki açıları kontrol et.','Havanın n değeri 1; sıvının n değerini çekmek için sinüsleri oranla.'],
 bilgi=[B('Snell yasası','n₁ × sin θ₁ = n₂ × sin θ₂ (açılar normalden ölçülür). Havanın kırılma indisi 1’dir. Işık kırılma indisi büyük ortama geçerken normale yaklaşır')],
 ad=[A('Yasayı yaz','Hava: n = 1, gelme açısı 53°; sıvı: kırılma açısı 37°.','1 × sin 53° = n × sin 37°'),A('Değerleri koy','Sinüs değerleri verilmiş.','1 × 0,8 = n × 0,6'),A('Sonuç','Eşitlikten n çekilir.','n = 0,8 ÷ 0,6 = 4/3')],
 puf='Işık havadan ortama geçiyorsa n = sin(hava açısı) ÷ sin(ortam açısı); açılar normalden ölçülür.')
assert Fr(6,10)/Fr(5,10)==Fr(6,5) and 1/Fr(6,5)==Fr(5,6)
K4k=['c/2','3c/5','5c/6','6c/5','2c']
mk(P,'0004',True,metin='Şekildeki gibi havadan bir camdan yapılmış levhaya normalle 37° açıyla gelen tek renkli ışık, levhada 30° açıyla kırılıyor.\nIşığın havadaki hızı c, sin 37° = 0,6 ve sin 30° = 0,5 olduğuna göre ışığın levhadaki hızı kaç c’dir?',
 sekil=kirilma(37,30,'Hava','Cam'),
 dogru='5c/6',sira=K4k,yan=[('c/2','sin 30° değerini (0,5) hız oranı sanmış.','dikkat'),('3c/5','sin 37° değerini (0,6) hız oranı sanmış.','dikkat'),('6c/5','Hızı c × n olarak bulmuş; v = c ÷ n olduğunu atlamış.','bilgi'),('2c','n = sin 30° ÷ sin 37° hesabı yerine 1 ÷ sin 30° almış; hızı da c × n bulmuş.','bilgi')],
 istenen='Işığın camdaki hızı (c cinsinden).',
 ip=['Önce Snell yasasıyla camın kırılma indisini bul.','Havadaki n = 1; sinüs oranından n çıkar.','Işığın ortamdaki hızı v = c ÷ n.'],
 bilgi=[B('Snell yasası','n₁ × sin θ₁ = n₂ × sin θ₂ (açılar normalden ölçülür). Havanın kırılma indisi 1’dir'),B('Hız ve kırılma indisi','ışığın n kırılma indisli ortamdaki hızı v = c ÷ n. Örnek: n = 2 ise v = c ÷ 2')],
 ad=[A('Kırılma indisi','Snell yasası hava ve cam için yazılır.','1 × sin 37° = n × sin 30° · n = 0,6 ÷ 0,5 = 6/5'),A('Hız bağıntısı','Işığın ortamdaki hızı kırılma indisiyle ters orantılıdır.','v = c ÷ n'),A('Sonuç','n değeri yerine konur.','v = c ÷ (6/5) = 5c/6')])
# ---- 0005 çukur ayna (öncüllü)
f,p=Fr(2),Fr(3); q=1/(1/f-1/p); assert q==6 and q>2*f and -q/p==-2
S5=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III']
mk(P,'0005',tipId='fz-op-kure-ayna',tip='Küresel aynada görüntü',z='orta',alt='Küresel Aynalar',kaz='Çukur aynada cismin konumundan görüntünün yerini ve özelliklerini belirler.',kalip='öncüllü',adim=4,
 kart='K-FZOP-05 (çukur ayna görüntüsü) · yeni konum (F–M arası), öncüllü',
 metin='Şekilde odak noktası F, merkezi M olan çukur aynanın önüne bir cisim konulmuştur.\nBuna göre cismin görüntüsü için;\nI. Gerçek ve ters oluşur.\nII. Cisimden küçüktür.\nIII. M noktasının ötesinde oluşur.\nifadelerinden hangileri doğrudur?',
 sekil=eksen('ayna',{2:'F',4:'M'},{},(3,'cisim')),
 dogru='I ve III',sira=S5,yan=[('Yalnız I','Görüntünün M’nin ötesinde oluştuğunu (III) atlamış.','dikkat'),('Yalnız II','F–M arasındaki cismin görüntüsünün büyük olduğunu bilmiyor.','bilgi'),('II ve III','Görüntüyü cisimden küçük sanmış; F–M arasındaki cismin görüntüsü büyüktür, gerçek ve terstir.','bilgi'),('I, II ve III','Görüntünün küçük olduğunu (II) doğru sanmış; cisim M’ye yakın değil F’ye yakınsa görüntü büyür.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['Şekilde cismin F ve M noktalarına göre yerini belirle.','Cisim F ile M arasındaysa görüntü M’nin ötesinde mi, içinde mi oluşur?','Görüntü M’nin ötesindeyse boyu cisimden büyük müdür, küçük mü?'],
 bilgi=[B('Çukur ayna','M = 2F. Cisim M’nin ötesinde: görüntü F–M arasında, gerçek, ters, küçük · F ile M arasında: görüntü M’nin ötesinde, gerçek, ters, büyük · F’nin içinde: sanal, düz, büyük')],
 ad=[A('Cismin konumu','Şekildeki cisim F ile M arasındadır.','F (2 birim) < cisim (3 birim) < M (4 birim)'),A('Görüntü yeri','F–M arasındaki cismin görüntüsü M’nin ötesinde oluşur.','III doğru'),A('Görüntü özelliği','Bu bölgede görüntü gerçek, ters ve cisimden büyüktür.','I doğru · II yanlış'),A('Sonuç','Doğru olanlar I ve III.','I ve III')],
 puf='Çukur aynada cismi F ve M’ye göre yerleştir; F–M arasında ise görüntü M’nin ötesinde, gerçek, ters ve büyüktür.')
f,p=Fr(2),Fr(5); q=1/(1/f-1/p); assert f<q<2*f and q/p<1
S5k=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
mk(P,'0005',True,metin='Şekilde odak noktası F, merkezi M olan çukur aynanın önüne bir cisim konulmuştur.\nBuna göre cismin görüntüsü için;\nI. Gerçektir.\nII. F ile M arasında oluşur.\nIII. Cisimden büyüktür.\nifadelerinden hangileri doğrudur?',
 sekil=eksen('ayna',{2:'F',4:'M'},{},(5,'cisim')),
 dogru='I ve II',sira=S5k,yan=[('Yalnız I','Görüntünün F ile M arasında oluştuğunu (II) atlamış.','dikkat'),('Yalnız II','Görüntünün gerçek olduğunu (I) atlamış.','dikkat'),('I ve III','M’nin ötesindeki cismin görüntüsünü büyük sanmış; görüntü küçüktür.','bilgi'),('II ve III','M’nin ötesindeki cismin görüntüsünü büyük sanmış; görüntü küçük ve gerçektir.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ad=[A('Cismin konumu','Şekildeki cisim M’nin ötesindedir.','cisim (5 birim) > M (4 birim)'),A('Görüntü yeri','M’nin ötesindeki cismin görüntüsü F ile M arasında oluşur.','II doğru'),A('Görüntü özelliği','Bu bölgede görüntü gerçek, ters ve cisimden küçüktür.','I doğru · III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')])
# ---- 0006 mercek (öncüllü)
def mq(f,p): return 1/(1/f-1/p)
assert mq(Fr(2),Fr(3))==6 and mq(Fr(2),Fr(6))==Fr(3) and 6/3==2 and Fr(3,3)==1 and Fr(3)/6<Fr(6)/3
S6=['Yalnız II','I ve II','I ve III','II ve III','I, II ve III']
mk(P,'0006',tipId='fz-op-mercek',tip='Mercekte görüntü',z='orta',alt='Mercekler',kaz='İnce kenarlı merceğin önünde cisim yer değiştirince görüntünün yerini ve boyunu karşılaştırır.',kalip='öncüllü',adim=4,
 kart='K-FZOP-06 (mercekte konum değişimi) · yeni konumlar, öncüllü',
 metin='Şekildeki ince kenarlı mercekte F odak noktası, 2F merceğin iki katı odak uzaklığındaki noktadır. Merceğin önünde L noktasında duran cisim N noktasına götürülüyor.\nBuna göre görüntü için;\nI. Boyu küçülür.\nII. Merceğe yaklaşır.\nIII. Sanal olur.\nifadelerinden hangileri doğrudur?',
 sekil=eksen('mercek',{2:'F',4:'2F'},{1:'K',3:'L',6:'N'},(3,'cisim'),birim=24),
 dogru='I ve II',sira=S6,yan=[('Yalnız II','Görüntü boyunun küçüldüğünü (I) atlamış.','dikkat'),('I ve III','Görüntünün sanal olacağını sanmış; sanal görüntü yalnız cisim F’nin içindeyken oluşur.','bilgi'),('II ve III','Görüntü boyunun küçüldüğünü (I) atlamış; ayrıca görüntünün sanal olduğunu sanmış.','bilgi'),('I, II ve III','Cisim 2F’nin ötesindeyken görüntünün sanal olduğunu sanmış; görüntü gerçektir.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['L ve N noktalarının F ve 2F’ye göre yerini belirle.','Cisim L’deyken görüntü nerede ve nasıl; N’deyken nerede ve nasıl?','Sanal görüntü cisim hangi bölgedeyken oluşur?'],
 bilgi=[B('İnce kenarlı mercek','cisim 2F’nin ötesinde: görüntü F–2F arasında, gerçek, ters, küçük · F–2F arasında: görüntü 2F’nin ötesinde, gerçek, ters, büyük · F’nin içinde: sanal, düz, büyük')],
 ad=[A('İlk konum','L, F ile 2F arasındadır.','görüntü: 2F’nin ötesinde, büyük, gerçek'),A('Son konum','N, 2F’nin ötesindedir.','görüntü: F–2F arasında, küçük, gerçek'),A('Karşılaştır','Görüntü 2F’nin ötesinden F–2F arasına geçer: merceğe yaklaşır. Boyu büyükten küçüğe iner.','I doğru · II doğru'),A('Sonuç','Görüntü her iki durumda gerçek; III yanlış.','I ve II')],
 puf='Mercekte cisim merceğe doğru yaklaşırsa görüntü büyür ve mercekten uzaklaşır; cisim uzaklaşırsa görüntü küçülür ve merceğe yaklaşır.')
S6k=['Yalnız I','Yalnız III','I ve III','II ve III','I, II ve III']
assert mq(Fr(2),Fr(3))==6
mk(P,'0006',True,metin='Şekildeki ince kenarlı mercekte F odak noktası, 2F merceğin iki katı odak uzaklığındaki noktadır. Merceğin önünde L noktasında duran cisim K noktasına getiriliyor.\nBuna göre görüntü için;\nI. Sanal olur.\nII. Cisimden küçük olur.\nIII. Cisimle aynı yönlü (düz) olur.\nifadelerinden hangileri doğrudur?',
 sekil=eksen('mercek',{2:'F',4:'2F'},{1:'K',3:'L',6:'N'},(3,'cisim'),birim=24),
 dogru='I ve III',sira=S6k,yan=[('Yalnız I','Sanal görüntünün düz olduğunu (III) atlamış.','dikkat'),('Yalnız III','Görüntünün sanal olduğunu (I) atlamış.','dikkat'),('II ve III','Görüntünün küçük olacağını sanmış; F’nin içindeki cismin görüntüsü büyüktür.','bilgi'),('I, II ve III','Görüntünün cisimden küçük olacağını (II) doğru sanmış; F’nin içindeki cismin görüntüsü büyüktür.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['K’nın F’ye göre yerini belirle: F’nin içinde mi, dışında mı?','F’nin içindeki cismin görüntüsü sanal mıdır, gerçek mi?','Sanal görüntü düz mü ters mi, boyu cisimden büyük mü küçük mü?'],
 ad=[A('İlk konum','L, F ile 2F arasındadır.','görüntü: gerçek, ters, büyük'),A('Son konum','K, F’nin içindedir (merceğe F’den yakın).','görüntü: sanal, düz, büyük'),A('İfadeleri sına','F’nin içindeki cismin görüntüsü sanal ve düzdür; boyu cisimden büyüktür.','I doğru · II yanlış · III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')])
# ---- 0007 zor eşit aydınlanma
x=symbols=None
for xx in range(1,60):
    if Fr(9,xx**2)==Fr(1,(60-xx)**2): assert xx==45
assert 60*Fr(9,10)==54 and 60*Fr(1,10)==6 and 60-45==15
mk(P,'0007',tipId='fz-op-aydinlanma',tip='Aydınlanma şiddeti',z='zor',alt='Aydınlanma',kaz='İki kaynağın aydınlanmasının eşit olduğu noktayı uzaklık oranlarının kareköküyle bulur.',kalip='hikâyeli',adim=5,
 kart='K-FZOP-07 (eşit aydınlanma noktası) · yeni şiddet oranı (9 : 1) ve 60 cm',
 metin='Işık şiddetleri sırasıyla 9I ve I olan noktasal K ve L ışık kaynakları birbirinden 60 cm uzaktadır. K ve L’yi birleştiren doğru üzerinde, ikisinin arasındaki bir ekran, iki kaynağın ekranda oluşturduğu aydınlanma şiddetleri eşit olacak biçimde yerleştiriliyor.\nBuna göre ekran K’dan kaç cm uzaktadır?',
 dogru=45,yan=[(6,'Şiddet oranını (1 : 10) doğrusal alıp 60 ÷ 10 hesaplamış.','bilgi'),(15,'Ekranın L’ye olan uzaklığını (60 − 45) K’ya olan uzaklık sanmış.','dikkat'),(30,'İki kaynağın ortasına koymuş; şiddetlerin farklı olduğunu atlamış.','bilgi'),(54,'Şiddet oranını doğrusal alıp 60 × 9 ÷ 10 hesaplamış; aydınlanmanın uzaklığın karesiyle değiştiğini atlamış.','bilgi')],
 istenen='Ekranın K kaynağına uzaklığı (cm).',
 ip=['Eşit aydınlanma için 9I ÷ x² = I ÷ (60 − x)² olmalı (x: K’ya uzaklık).','Eşitliğin iki yanının karekökünü al: 3 ÷ x = 1 ÷ (60 − x).','Çapraz çarp ve x’i çek.'],
 bilgi=[AYD],
 ad=[A('Eşitliği yaz','Ekranın K’ya uzaklığı x ise L’ye uzaklığı 60 − x olur. Aydınlanmalar eşittir.','9I ÷ x² = I ÷ (60 − x)²'),A('Karekök al','Her iki tarafın karekökü alınır.','3 ÷ x = 1 ÷ (60 − x)'),A('Çapraz çarp','Paydalar eşitlenir.','3 × (60 − x) = x'),A('Çöz','Parantez açılır, x yalnız bırakılır.','180 − 3x = x · 180 = 4x'),A('Sonuç','K’ya uzaklık.','x = 45 cm')],
 puf='Eşit aydınlanma için I₁ ÷ d₁² = I₂ ÷ d₂² yaz; karekök alıp uzaklık oranını şiddetlerin kareköküne eşitle.')
for xx in range(1,90):
    if Fr(4,xx**2)==Fr(1,(90-xx)**2): assert xx==60
assert 90*Fr(4,5)==72 and 90*Fr(1,5)==18 and 90-60==30
mk(P,'0007',True,metin='Işık şiddetleri sırasıyla 4I ve I olan noktasal M ve N lambaları arasındaki uzaklık 90 cm’dir. Lambaları birleştiren doğru üzerinde ve aralarında bulunan bir perde, iki lambanın perdede oluşturduğu aydınlanmalar eşit olacak biçimde konuluyor.\nBuna göre perde M’den kaç cm uzaktadır?',
 dogru=60,yan=[(18,'Şiddet oranını (1 : 5) doğrusal alıp 90 ÷ 5 hesaplamış.','bilgi'),(30,'Perdenin N’ye olan uzaklığını (90 − 60) M’ye olan uzaklık sanmış.','dikkat'),(45,'İki lambanın ortasına koymuş; şiddetlerin farklı olduğunu atlamış.','bilgi'),(72,'Şiddet oranını doğrusal alıp 90 × 4 ÷ 5 hesaplamış; aydınlanmanın uzaklığın karesiyle değiştiğini atlamış.','bilgi')],
 istenen='Perdenin M lambasına uzaklığı (cm).',
 ip=['Perdenin M’ye uzaklığı x ise N’ye uzaklığı toplam uzaklıktan x çıkarılarak bulunur.','Aydınlanmalar eşit: şiddet ÷ uzaklık² iki lamba için aynıdır.','Karekök alıp çapraz çarp, sonra x’i çek.'],
 ad=[A('Eşitliği yaz','Perdenin M’ye uzaklığı x ise N’ye uzaklığı 90 − x olur.','4I ÷ x² = I ÷ (90 − x)²'),A('Karekök al','Her iki tarafın karekökü alınır.','2 ÷ x = 1 ÷ (90 − x)'),A('Çapraz çarp','Paydalar eşitlenir.','2 × (90 − x) = x'),A('Çöz','Parantez açılır, x yalnız bırakılır.','180 − 2x = x · 180 = 3x'),A('Sonuç','M’ye uzaklık.','x = 60 cm')])
# ---- 0008 zor boy görme
boy,goz=Fr(18,10),Fr(17,10); ust=(boy+goz)/2; alt=goz/2; assert ust==Fr(175,100) and alt==Fr(85,100) and ust-alt==Fr(9,10)
mk(P,'0008',tipId='fz-op-duzlem-ayna',tip='Düzlem aynada görüntü',z='zor',alt='Düzlem Ayna',kaz='Düzlem aynada boyun tamamını görmek için aynanın kenar yüksekliklerini belirler.',kalip='şekilli',adim=5,
 kart='K-FZOP-08 (boy görme) · yeni boy ve göz yüksekliği, istenen üst kenar',
 metin='Boyu 1,8 m olan, göz hizası yerden 1,7 m yükseklikte bulunan bir kişi, 2 m uzağındaki dik duran düzlem aynada kendisini baştan ayağa görüyor (şekil).\nKişi başının tepesini aynada görebildiğine göre aynanın üst kenarı yerden en az kaç m yüksekte olmalıdır?',
 sekil=boy_ayna(Fr(18,10),Fr(17,10),2),
 dogru=Fr(175,100),yan=[(Fr(85,100),'Ayak ucunu görmek için gereken yüksekliği (1,7 ÷ 2) üst kenar sanmış.','dikkat'),(Fr(9,10),'Aynanın en az boyunu (1,8 ÷ 2) yüksekliğe dönüştürmüş.','dikkat'),(Fr(17,10),'Göz yüksekliğini üst kenar sanmış; baş ucundan gelen ışının yansıma noktasını bulmamış.','bilgi'),(Fr(45,100),'Aynanın en az boyunun yarısını (0,9 ÷ 2) yüksekliğe dönüştürmüş.','bilgi')],
 istenen='Aynanın üst kenarının yerden en az yüksekliği (m).',
 ip=['Baş ucundan gelen ışık aynada yansıyıp göze ulaşır.','Yansıma noktası, göz ile baş ucu arasındaki yüksekliğin tam ortasındadır.','Kişinin aynaya uzaklığı sonucu değiştirmez.'],
 bilgi=[B('Düzlem aynada boy görme','baş ucundan ve ayak ucundan gelen ışınların aynadaki yansıma noktaları, göz ile bu uçlar arasındaki yüksekliğin tam ortasındadır. Kişinin aynaya uzaklığı bu yükseklikleri değiştirmez')],
 ad=[A('Işının yolu','Baş ucunun görüntüsü aynanın arkasında 1,8 m yüksekliktedir; göz ona bakar.','baş ucu: 1,8 m · göz: 1,7 m'),A('Yansıma noktası','Düzlem aynada yansıma noktası, baş ucu ile göz yüksekliklerinin ortasındadır.','(1,8 + 1,7) ÷ 2'),A('Üst kenar','Baş ucunun görülebilmesi için ayna bu noktaya kadar çıkmalıdır.','1,75 m'),A('Kontrol','Ayak ucu için yansıma noktası 1,7 ÷ 2 = 0,85 m; ayna boyu 1,75 − 0,85 = 0,9 m olur (boyun yarısı).','0,9 m = 1,8 ÷ 2')],
 puf='Boyun tamamını görmek için ayna en az boyun yarısı kadar olmalıdır; üst kenar (boy + göz) ÷ 2, alt kenar göz ÷ 2 yüksekliktedir.')
boy,goz=Fr(16,10),Fr(15,10); ust=(boy+goz)/2; alt=goz/2; assert alt==Fr(75,100) and ust==Fr(155,100)
mk(P,'0008',True,metin='Boyu 1,6 m olan, göz hizası yerden 1,5 m yükseklikte bulunan bir çocuk, 3 m uzağındaki dik duran düzlem aynada kendisini baştan ayağa görüyor (şekil).\nÇocuk ayak ucunu aynada görebildiğine göre aynanın alt kenarı yerden en çok kaç m yüksekte olabilir?',
 sekil=boy_ayna(Fr(16,10),Fr(15,10),3),
 dogru=Fr(75,100),yan=[(Fr(8,10),'Aynanın en az boyunu (1,6 ÷ 2) alt kenar yüksekliği sanmış.','dikkat'),(Fr(155,100),'Baş ucunu görmek için gereken yüksekliği alt kenar sanmış.','dikkat'),(Fr(15,10),'Göz yüksekliğini alt kenar sanmış; ayak ucundan gelen ışının yansıma noktasını bulmamış.','bilgi'),(Fr(16,10),'Çocuğun boyunu alt kenar yüksekliği sanmış.','bilgi')],
 istenen='Aynanın alt kenarının yerden en çok yüksekliği (m).',
 ip=['Ayak ucundan gelen ışık aynada yansıyıp göze ulaşır.','Yansıma noktası, ayak ucu ile göz arasındaki yüksekliğin ortasındadır.','Çocuğun aynaya uzaklığı sonucu değiştirmez.'],
 ad=[A('Işının yolu','Ayak ucunun görüntüsü aynanın arkasında yer seviyesindedir (0 m); göz 1,5 m yüksekliktedir.','ayak ucu: 0 m · göz: 1,5 m'),A('Yansıma noktası','Yansıma noktası, ayak ucu ile göz yüksekliklerinin ortasındadır.','(0 + 1,5) ÷ 2'),A('Alt kenar','Ayak ucunun görülebilmesi için aynanın alt kenarı bu noktadan yukarıda olamaz.','0,75 m'),A('Kontrol','Baş ucu için yansıma noktası (1,6 + 1,5) ÷ 2 = 1,55 m; ayna boyu 1,55 − 0,75 = 0,8 m olur (boyun yarısı).','0,8 m = 1,6 ÷ 2')])
bitir(P,'optik','fiz|Optik')
