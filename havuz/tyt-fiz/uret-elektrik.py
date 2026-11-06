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
# ---- devre çizimi (SVG): bileşen = (tür, etiket); tür: R direnç, L lamba, A ampermetre, V voltmetre, S kapalı anahtar, O açık anahtar
def _ln(a,b): return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke-width="1.6"/>'
def _glif(k,lab,cx,cy,dik):
    half={'R':18,'L':10,'A':10,'V':10,'S':14,'O':14}[k]
    if k=='R': sh='<rect x="-18" y="-6" width="36" height="12" stroke-width="1.6"/>'
    elif k=='L': sh='<circle r="10" stroke-width="1.6"/><path d="M-7 -7 L7 7 M-7 7 L7 -7" stroke-width="1.4"/>'
    elif k in 'AV': sh='<circle r="10" stroke-width="1.6"/>'
    else:
        sh='<circle cx="-14" r="2" stroke-width="1.4"/><circle cx="14" r="2" stroke-width="1.4"/>'+('<path d="M-14 0 L14 0" stroke-width="1.8"/>' if k=='S' else '<path d="M-14 0 L10 -14" stroke-width="1.8"/>')
    o=f'<g transform="translate({cx:.1f},{cy:.1f}) rotate({90 if dik else 0})">{sh}</g>'
    if k in 'AV': o+=T(cx,cy+4.5,k,size=12,bold=True)
    if lab: o+=(T(cx+16,cy+4,lab,anchor='start',size=11) if dik else T(cx,cy-14 if k!='O' else cy-20,lab,size=11))
    return o,half
def _zincir(p,q,comps):
    dik=abs(p[0]-q[0])<1e-6; n=len(comps); o=[]; cur=p
    for i,(k,lab) in enumerate(comps):
        t=(i+1)/(n+1); c=(p[0]+(q[0]-p[0])*t,p[1]+(q[1]-p[1])*t)
        g,h=_glif(k,lab,c[0],c[1],dik)
        a=(c[0],c[1]-h) if dik else (c[0]-h,c[1]); b=(c[0],c[1]+h) if dik else (c[0]+h,c[1])
        o.append(_ln(cur,a)); o.append(g); cur=b
    o.append(_ln(cur,q)); return ''.join(o)
def devre(V=None,ust=(),kol=(),alt=(),uc=None,kapat=True):
    """V: üreteç etiketi (ör. '12 V'). ust: üst telde seri bileşenler; kol: sütunlar (her biri üstten alta bileşen listesi); alt: alt telde seri bileşenler;
    uc=('A','B'): üreteç yerine uçlar. Üreteç solda, + kutup üstte."""
    lx=58; ty=36; mx=max([len(c) for c in kol]+[1]); by=ty+max(100,54*mx)
    if kol:
        xc0=lx+(78*len(ust) if ust else 50)+ (0 if ust else 0); xs=[xc0+82*i for i in range(len(kol))]; rx=xs[-1]
    else:
        rx=lx+82*max(len(ust),len(alt),1)+20; xs=[]
    W=max(330,rx+60); H=by+18; o=[]
    # sol taraf
    cy=(ty+by)/2
    if uc:
        o.append(f'<circle cx="{lx}" cy="{ty}" r="3.5" stroke-width="1.6"/><circle cx="{lx}" cy="{by}" r="3.5" stroke-width="1.6"/>')
        o.append(T(lx-10,ty+4,uc[0],anchor='end',bold=True)); o.append(T(lx-10,by+4,uc[1],anchor='end',bold=True))
        sol=(lx+3.5,ty)
        o.append(_zincir((lx+3.5,ty),(xs[0] if xs else rx,ty),list(ust)) if kol else _zincir((lx+3.5,ty),(rx,ty),list(ust)))
        # alt tel
        o.append(_zincir(((xs[0] if kol else rx),by),(lx+3.5,by),list(alt)))
    else:
        o.append(_ln((lx,ty),(lx,cy-5))); o.append(_ln((lx,cy+5),(lx,by)))
        o.append(f'<line x1="{lx-13}" y1="{cy-5}" x2="{lx+13}" y2="{cy-5}" stroke-width="2.4"/><line x1="{lx-7}" y1="{cy+5}" x2="{lx+7}" y2="{cy+5}" stroke-width="3.4"/>')
        o.append(T(lx+17,cy-8,'+',anchor='start',size=13,bold=True)); o.append(T(lx-17,cy+4,V,anchor='end',size=12,bold=True))
        o.append(_zincir((lx,ty),(xs[0] if kol else rx,ty),list(ust)))
        o.append(_zincir(((xs[0] if kol else rx),by),(lx,by),list(alt)))
    # sütunlar
    for i,c in enumerate(kol):
        x=xs[i]
        o.append(_zincir((x,ty),(x,by),list(c)))
        if i<len(kol)-1:
            o.append(_ln((x,ty),(xs[i+1],ty))); o.append(_ln((x,by),(xs[i+1],by)))
            o.append(f'<circle cx="{x}" cy="{ty}" r="2.8" style="fill:currentColor"/><circle cx="{x}" cy="{by}" r="2.8" style="fill:currentColor"/>')
    if not kol: o.append(_ln((rx,ty),(rx,by)))
    return G._svg(W,H,''.join(o))
def _tara(R,prt):  # sıfır kontrol
    return R
KONU='Elektrik'
P=Parti('elektrik','Elektrik','fiz|Elektrik',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2019–2024 (elektrik devreleri) · MEB 9–10. sınıf'
kart('K-FZEL-01','Yük paylaşımı','Özdeş iletken kürelerin teması: toplam yük işaretiyle bulunur ve eşit paylaşılır.','Yükleri işaretsiz toplamak; paylaştırmayı unutmak.','kolay','düz',2,'fz-el-yuk','Yüklü cisimlerin temasında yük paylaşımı',KY)
kart('K-FZEL-02','Direnç bağıntısı','R = ρℓ/A: uzunlukla doğru, kesit alanıyla ters orantı; oranlar birlikte uygulanır.','Kesit alanını doğru orantılı almak; yalnız bir oranı kullanmak.','kolay','düz',2,'fz-el-direnc','Telin direncini etkileyen etmenler',KY)
kart('K-FZEL-03','Karma bağlama','Seri ve paralel dirençlerden oluşan ağın A–B arası eşdeğeri adım adım indirgenir.','Paralel kolu seri toplamak; bir kolu unutmak.','orta','şekilli',3,'fz-el-es-direnc','Eşdeğer direnç',KY)
kart('K-FZEL-04','Paralel kolda akım','Ana kol akımı bulunur, paralel uçlardaki gerilimden kol akımları elde edilir.','Ana koldaki akımı kola yazmak; tüm gerilimi bir dirence uygulamak.','orta','şekilli',4,'fz-el-akim-gerilim','Devrede akım ve gerilim',KY)
kart('K-FZEL-05','Enerji bedeli','E = P × t (kWh); gider = kWh × birim bedel; W–kW dönüşümü.','Watt’ı kW’a çevirmemek; süre ya da gün sayısını atlamak.','orta','hikâyeli',4,'fz-el-guc-enerji','Elektriksel güç ve enerji',KY)
kart('K-FZEL-06','Seri devrede voltmetre','Seri devrede akım ortak; voltmetre okuması I × R.','Üreteç gerilimini okuma sanmak; kalan gerilimi okumak.','orta','şekilli',3,'fz-el-akim-gerilim','Devrede akım ve gerilim',KY)
kart('K-FZEL-07','Anahtarın etkisi','Anahtar kapanınca eşdeğer direnç değişir; ampermetre değeri iki halde hesaplanıp karşılaştırılır.','Kapalı değeri artış sanmak; kollardaki akımı karıştırmak.','zor','şekilli',5,'fz-el-anahtar-lamba','Anahtar ve lamba parlaklığı',KY)
kart('K-FZEL-08','Lamba parlaklığı','Parlaklık P = I²R; anahtar sonrası her lambanın akımı yeniden bulunup öncüller sınanır.','Paralel kolda gerilimin düştüğünü görmemek; özdeş lambaları karıştırmak.','zor','öncüllü',5,'fz-el-anahtar-lamba','Anahtar ve lamba parlaklığı',KY)
ILE=B('Seri ve paralel bağlama','seri: eşdeğer direnç R = R₁ + R₂, akım ortak · paralel: iki direnç için R = (R₁ × R₂) ÷ (R₁ + R₂), gerilim ortak. Örnek: 6 Ω ve 3 Ω paralel → 18 ÷ 9 = 2 Ω')
OHM=B('Ohm yasası','V = I × R. Seri koldaki her elemandan aynı akım geçer; paralel kollarda uçlar arası gerilim aynıdır, akımlar toplanır. Örnek: 12 V’ta 4 Ω’dan 3 A geçer')
PAR_A=lambda a,b: Fr(a*b,a+b)
# ---------- 0001
q=Fr(10)+Fr(-4); assert q/2==3
mk(P,'0001',tipId='fz-el-yuk',tip='Yüklü cisimlerin temasında yük paylaşımı',z='kolay',alt='Elektrik Yükleri',kaz='Özdeş iletken cisimlerin temasından sonraki yük dağılımını belirler.',kalip='düz',adim=2,
 kart='K-FZEL-01 (özdeş iletken kürelerin teması) · yeni yük değerleri, istenen X’in son yükü',
 metin='Yalıtkan saplarla tutulan özdeş iletken X ve Y kürelerinden X’in yükü +10q, Y’nin yükü −4q’dur. Küreler birbirine dokundurulup yeniden ayrılıyor.\nBuna göre X küresinin son yükü kaç q’dur?',
 dogru=3,yan=[(-4,'Y’nin ilk yükünü yazmış; temasta yük paylaşıldığını atlamış.','dikkat'),(6,'Toplam yükü (+6q) ikiye bölmeyi unutmuş.','islem'),(7,'Yükleri işaretsiz toplayıp (10 + 4) ÷ 2 almış; negatif yükü pozitif saymış.','bilgi'),(14,'Yükleri işaretsiz toplamış ve paylaştırmamış.','bilgi')],
 istenen='Temastan sonra X küresinin yükü.',
 ip=['Temas sırasında toplam yük değişmez.','Önce iki yükü işaretleriyle topla.','Özdeş iletken küreler toplam yükü eşit paylaşır.'],
 bilgi=[B('Yük paylaşımı','özdeş iletken kürelerde toplam yük korunur ve temastan sonra eşit paylaşılır: son yük = toplam yük ÷ 2. Örnek: +6q ve +2q → her biri +4q'),B('Yüklerin toplanması','yükler işaretleriyle toplanır: (+5q) + (−3q) = +2q')],
 ad=[A('Toplam yük','Yükler işaretleriyle toplanır; temas sırasında yük yok olmaz.','(+10q) + (−4q) = +6q'),A('Eşit paylaştır','Küreler özdeş ve iletken olduğundan toplam yük ikiye bölünür.','+6q ÷ 2 = +3q'),A('Sonuç','Ayrıldıktan sonra her kürede +3q vardır.','X küresi: +3q')],
 puf='Özdeş iletken kürelerde önce yükleri işaretiyle topla, sonra küre sayısına böl.')
assert (Fr(-12)+2)/2==-5
mk(P,'0001',True,metin='Özdeş iletken M ve N kürelerinden M’nin yükü −12q, N’nin yükü +2q’dur. M ile N birbirine dokundurulduktan sonra ayrılıyor.\nBuna göre N küresinin son yükü kaç q’dur?',
 dogru=-5,yan=[(-10,'Toplam yükü (−10q) ikiye bölmeyi unutmuş.','islem'),(-7,'(−12 − 2) ÷ 2 işlemiyle N’nin yükünü negatif almış.','bilgi'),(2,'N’nin ilk yükünü yazmış; temasta yük paylaşıldığını atlamış.','dikkat'),(5,'Toplam yükün işaretini ters yazmış.','islem')],
 istenen='Temastan sonra N küresinin yükü.',
 ad=[A('Toplam yük','Yükler işaretleriyle toplanır.','(−12q) + (+2q) = −10q'),A('Eşit paylaştır','Özdeş iletken küreler toplam yükü yarı yarıya paylaşır.','−10q ÷ 2 = −5q'),A('Sonuç','Ayrılan her kürede −5q kalır.','N küresi: −5q')])
# ---------- 0002
R0=6; assert R0*Fr(3,1)/2==9
mk(P,'0002',tipId='fz-el-direnc',tip='Telin direncini etkileyen etmenler',z='kolay',alt='Elektrik Akımı, Potansiyel Farkı ve Direnç',kaz='Telin direncinin uzunluk ve kesit alanıyla değişimini orantıyla hesaplar.',kalip='düz',adim=2,
 kart='K-FZEL-02 (uzunluk ve kesit alanı oranları) · yeni oranlar',
 metin='Aynı maddeden yapılmış homojen bir telin uzunluğu ℓ, kesit alanı A iken direnci 6 Ω’dur.\nSıcaklık sabit tutulduğuna göre aynı maddeden yapılmış, uzunluğu 3ℓ ve kesit alanı 2A olan telin direnci kaç Ω olur?',
 dogru=9,yan=[(3,'Yalnızca kesit alanının etkisini (6 ÷ 2) hesaplamış; uzunluğu atlamış.','dikkat'),(4,'Oranları ters yazmış: 6 × 2 ÷ 3.','bilgi'),(18,'Yalnızca uzunluğun etkisini (6 × 3) hesaplamış; kesit alanını atlamış.','dikkat'),(36,'Kesit alanı arttığında direncin de arttığını sanıp 6 × 3 × 2 almış.','bilgi')],
 istenen='Yeni telin direnci (Ω).',
 ip=['Direnç uzunlukla doğru, kesit alanıyla ters orantılıdır.','Uzunluk kaç kat oluyor, direnç buna göre değişir; alan için tersini düşün.','Önce uzunluğun, sonra alanın etkisini 6 Ω’a uygula.'],
 bilgi=[B('Telin direnci','R = ρ × ℓ ÷ A (ρ: maddeye ve sıcaklığa bağlı özdirenç). Uzunluk 2 katına çıkarsa R iki katına çıkar; kesit alanı 2 katına çıkarsa R yarıya iner')],
 ad=[A('Uzunluğun etkisi','Uzunluk 3 katına çıkınca direnç doğru orantılı olarak 3 katına çıkar.','6 Ω × 3 = 18 Ω'),A('Alanın etkisi','Kesit alanı 2 katına çıkınca direnç ters orantılı olarak yarıya iner.','18 Ω ÷ 2 = 9 Ω'),A('Kısaca','İki etki birlikte oran olarak uygulanır.','R = 6 × 3 ÷ 2 = 9 Ω')],
 puf='Direnç için uzunluk oranını payda, kesit alanı oranını paydaya yaz: R′ = R × (ℓ′/ℓ) ÷ (A′/A).')
assert 12*Fr(2,1)/4==6
mk(P,'0002',True,metin='Bir iletken telin direnci 12 Ω’dur. Aynı maddeden yapılan ve sıcaklığı aynı tutulan ikinci telin boyu birinciden 2 kat uzun, kesit alanı ise 4 kat büyüktür.\nBuna göre ikinci telin direnci kaç Ω’dur?',
 dogru=6,yan=[(3,'Yalnızca kesit alanının etkisini (12 ÷ 4) hesaplamış; uzunluğu atlamış.','dikkat'),(24,'Yalnızca uzunluğun etkisini (12 × 2) hesaplamış; kesit alanını atlamış.','dikkat'),(48,'Kesit alanı büyüdükçe direncin de büyüdüğünü sanıp 12 × 4 almış.','bilgi'),(96,'Hem uzunluğu hem alanı doğru orantılı alıp 12 × 2 × 4 hesaplamış.','bilgi')],
 istenen='İkinci telin direnci (Ω).',
 ip=['Direnç uzunlukla doğru, kesit alanıyla ters orantılıdır.','Boy kaç kat oluyorsa direnç o kadar kat değişir; alan için tersini düşün.','Önce boyun, sonra alanın etkisini ilk dirence uygula.'],
 ad=[A('Uzunluğun etkisi','Boy 2 katına çıkınca direnç 2 katına çıkar.','12 Ω × 2 = 24 Ω'),A('Alanın etkisi','Kesit alanı 4 katına çıkınca direnç dörtte birine iner.','24 Ω ÷ 4 = 6 Ω'),A('Kısaca','Oranlar birlikte uygulanır.','R = 12 × 2 ÷ 4 = 6 Ω')])
# ---------- 0003  eşdeğer direnç
R1,R2,R3=4,12,6; req=R1+PAR_A(R2,R3); assert PAR_A(R2,R3)==4 and req==8
assert 1/(Fr(1,4)+Fr(1,12)+Fr(1,6))==2 and R1+R2+R3==22 and R1+R3==10
mk(P,'0003',tipId='fz-el-es-direnc',tip='Eşdeğer direnç',z='orta',alt='Elektrik Devreleri',kaz='Seri ve paralel bağlı dirençlerden oluşan devrenin eşdeğer direncini bulur.',kalip='şekilli',adim=3,
 kart='K-FZEL-03 (karma bağlama) · yeni ağ ve değerler',
 metin='Şekildeki devrede R₁ = 4 Ω, R₂ = 12 Ω ve R₃ = 6 Ω’dur.\nBuna göre A ve B uçları arasındaki eşdeğer direnç kaç Ω’dur?',
 sekil=devre(uc=('A','B'),ust=[('R','R₁')],kol=[[('R','R₂')],[('R','R₃')]]),
 dogru=8,yan=[(2,'Üç direnci de paralel sanıp 1/4 + 1/12 + 1/6 işlemini yapmış.','bilgi'),(4,'Yalnızca paralel kolun eşdeğerini (4 Ω) yazmış; seri R₁’i eklememiş.','dikkat'),(10,'R₁ ile paralel kolun yalnız bir direncini (4 + 6) toplamış.','dikkat'),(22,'Bütün dirençleri seri sanıp toplamış.','bilgi')],
 istenen='A–B uçları arasındaki eşdeğer direnç.',
 ip=['Hangi dirençler aynı iki nokta arasına bağlı? Onlar paralel.','Önce paralel kolun eşdeğerini bul.','Bulduğun değeri seri bağlı dirençle topla.'],
 bilgi=[ILE],
 ad=[A('Paralel kolu bul','R₂ ve R₃ aynı iki nokta arasına bağlıdır, paraleldir.','R₂₃ = (12 × 6) ÷ (12 + 6) = 4 Ω'),A('Seri ekle','R₁ bu paralel grupla seridir.','R = 4 + 4'),A('Sonuç','Eşdeğer direnç iki değerin toplamıdır.','R = 8 Ω')],
 puf='Önce paralel grupları tek dirence indir, sonra seri olanları topla.')
mk(P,'0003',True,metin='Şekildeki devrede R₁ = 1 Ω, R₂ = 10 Ω, R₃ = 15 Ω ve R₄ = 3 Ω’dur.\nBuna göre K ve L uçları arasındaki eşdeğer direnç kaç Ω’dur?',
 sekil=devre(uc=('K','L'),ust=[('R','R₁')],kol=[[('R','R₂')],[('R','R₃')]],alt=[('R','R₄')]),
 dogru=10,yan=[(4,'Paralel kolu atlayıp yalnız R₁ + R₄ toplamış.','dikkat'),(7,'Paralel kolun eşdeğeri (6 Ω) ile R₁’i toplayıp R₄’ü unutmuş.','dikkat'),(9,'R₁’i unutup paralel kolun eşdeğeri ile R₄’ü (6 + 3) toplamış.','dikkat'),(29,'Bütün dirençleri seri sanıp toplamış.','bilgi')],
 istenen='K–L uçları arasındaki eşdeğer direnç.',
 ad=[A('Paralel kolu bul','R₂ ve R₃ aynı iki nokta arasındadır.','R₂₃ = (10 × 15) ÷ (10 + 15) = 6 Ω'),A('Seri olanları topla','R₁, R₂₃ ve R₄ aynı yol üzerindedir.','R = 1 + 6 + 3'),A('Sonuç','Toplam eşdeğer direnç.','R = 10 Ω')])
assert PAR_A(10,15)==6 and 1+6+3==10 and 6+3==9
# ---------- 0004  paralel kolda ampermetre
V=24;R1,R2,R3=4,6,12; Rp=PAR_A(R2,R3); I=Fr(V)/(R1+Rp); Vp=I*Rp; assert Rp==4 and I==3 and Vp==12 and Vp/R3==1 and Vp/R2==2 and Fr(V,R2)==4 and Fr(V,R1)==6
mk(P,'0004',tipId='fz-el-akim-gerilim',tip='Devrede akım ve gerilim',z='orta',alt='Elektrik Devreleri',kaz='Karma devrede kol akımını ve uçlar arası gerilimi hesaplar.',kalip='şekilli',adim=4,
 kart='K-FZEL-04 (paralel kolda akım) · yeni değerler, ampermetre paralel kolda',
 metin='Şekildeki devrede üreteç ve ampermetre idealdir (ampermetrenin direnci ihmal edilir). R₁ = 4 Ω, R₂ = 6 Ω ve R₃ = 12 Ω’dur.\nBuna göre ampermetre kaç A’i gösterir?',
 sekil=devre(V='24 V',ust=[('R','R₁')],kol=[[('R','R₂')],[('R','R₃'),('A','')]]),
 dogru=1,yan=[(2,'R₂ üzerinden geçen akımı (12 ÷ 6) ampermetrenin okuması sanmış.','dikkat'),(3,'Ana koldaki akımı ampermetrenin okuması sanmış; ampermetre yalnız R₃ koludadır.','dikkat'),(4,'24 V’u doğrudan R₂’ye uygulamış (24 ÷ 6).','bilgi'),(6,'24 V’u yalnızca R₁’e uygulamış (24 ÷ 4); devrenin geri kalanını atlamış.','bilgi')],
 istenen='R₃ koluna bağlı ampermetrenin okuması.',
 ip=['Önce üretecin verdiği toplam akımı bul.','Paralel kolun uçları arasındaki gerilimi hesapla.','Ampermetre hangi koldan geçen akımı ölçüyor?'],
 bilgi=[OHM,ILE],
 ad=[A('Eşdeğer direnç','R₂ ve R₃ paraleldir; R₁ ile seri bağlanır.','R₂₃ = (6 × 12) ÷ 18 = 4 Ω · R = 4 + 4 = 8 Ω'),A('Ana kol akımı','Üretecin verdiği akım toplam dirence bölünerek bulunur.','I = 24 ÷ 8 = 3 A'),A('Paralel uç gerilimi','R₁’den 3 A geçer; paralel kolun uçlarında kalan gerilim vardır.','V₁ = 3 × 4 = 12 V · V₂₃ = 24 − 12 = 12 V'),A('Ampermetre okuması','Ampermetre R₃ koldaki akımı ölçer.','I₃ = 12 ÷ 12 = 1 A')],
 puf='Önce ana kol akımını, sonra paralel uç gerilimini bul; kol akımı bu gerilimin kol direncine bölümüdür.')
V=30;R1,R2,R3=6,12,6; Rp=PAR_A(R2,R3); I=Fr(V)/(R1+Rp); Vp=I*Rp; assert Rp==4 and I==3 and Vp==12 and I*R1==18
mk(P,'0004',True,metin='Şekildeki devrede üreteç, ampermetre ve voltmetre idealdir. R₁ = 6 Ω, R₂ = 12 Ω ve R₃ = 6 Ω’dur.\nBuna göre voltmetre kaç V’u gösterir?',
 sekil=devre(V='30 V',ust=[('R','R₁'),('A','')],kol=[[('R','R₂')],[('R','R₃')],[('V','')]]),
 dogru=12,yan=[(6,'R₁’in direnç değerini (6 Ω) gerilim değeri sanmış.','dikkat'),(18,'R₁ üzerindeki gerilimi (3 × 6) voltmetrenin okuması sanmış.','dikkat'),(24,'30 V’tan 6 çıkarmış; R₁’in direncini gerilim düşümü sanmış.','bilgi'),(30,'Üretecin gerilimini voltmetrenin okuması sanmış.','bilgi')],
 istenen='Paralel kolun uçlarına bağlı voltmetrenin okuması.',
 ad=[A('Eşdeğer direnç','R₂ ve R₃ paraleldir; R₁ ile seri bağlıdır.','R₂₃ = (12 × 6) ÷ 18 = 4 Ω · R = 6 + 4 = 10 Ω'),A('Ana kol akımı','Ampermetrenin gösterdiği akım toplam dirence bölünerek bulunur.','I = 30 ÷ 10 = 3 A'),A('Voltmetre okuması','Voltmetre paralel kolun uçlarındadır.','V = 3 × 4 = 12 V')])
# ---------- 0005  güç ve enerji
E=Fr(1,10)*4*5*30; assert E==60 and E*2==120 and Fr(1,10)*4*5*2==4 and 1*4*5*30*2==1200 and Fr(1,100)*4*5*30*2==12
mk(P,'0005',tipId='fz-el-guc-enerji',tip='Elektriksel güç ve enerji',z='orta',alt='Elektrik Devreleri',kaz='Güç ve süreden elektrik enerjisini (kWh) ve bedelini hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-FZEL-05 (kWh ve gider) · yeni cihazlar, süre ve birim bedel',
 metin='Bir evde her biri 100 W gücündeki 4 lamba günde 5 saat yanıyor. 1 kWh elektrik enerjisinin bedeli 2 TL’dir.\nBuna göre bu lambaların 30 günlük elektrik gideri kaç TL’dir?',
 dogru=120,yan=[(4,'Yalnızca bir günün giderini hesaplamış; 30 günü atlamış.','dikkat'),(60,'Harcanan enerjiyi (60 kWh) bulup birim bedelle çarpmayı unutmuş.','dikkat'),(1200,'100 W’ı 1 kW almış; watt–kilowatt dönüşümünü yanlış yapmış.','bilgi'),(12,'100 W’ı 0,01 kW almış; watt–kilowatt dönüşümünü yanlış yapmış.','bilgi')],
 istenen='30 günlük toplam elektrik gideri (TL).',
 ip=['Enerji = güç × süre; kWh için gücü kW cinsinden yaz.','Önce bir günde harcanan toplam enerjiyi bul.','Enerjiyi gün sayısıyla, sonra birim bedelle çarp.'],
 bilgi=[B('Elektrik enerjisi','E = P × t. Güç kW, süre saat alınırsa enerji kWh olur; 1 kW = 1000 W. Örnek: 500 W’lık cihaz 2 saatte 0,5 × 2 = 1 kWh harcar'),B('Gider','gider = harcanan kWh × 1 kWh’in bedeli')],
 ad=[A('Gücü kW yap','Hesabı kWh cinsinden yapmak için watt, 1000’e bölünür.','100 W = 0,1 kW'),A('Günlük enerji','4 lambanın toplam gücü süreyle çarpılır.','E = 4 × 0,1 × 5 = 2 kWh'),A('30 günlük enerji','Günlük enerji gün sayısıyla çarpılır.','E = 2 × 30 = 60 kWh'),A('Gider','Enerji birim bedelle çarpılır.','60 × 2 = 120 TL')],
 puf='Elektrik giderinde sıra: W → kW, kW × saat = kWh, kWh × birim bedel = TL.')
E=Fr(800,1000)*3*4; assert E==Fr(48,5) and E*5==48 and Fr(8,10)*3*5==12 and 8*3*4*5==480 and Fr(8,100)*3*4*5==Fr(24,5)
mk(P,'0005',True,metin='Bir ailede 800 W gücündeki elektrik süpürgesi haftada 3 saat çalıştırılıyor. 1 kWh elektrik enerjisinin bedeli 5 TL’dir.\nBuna göre süpürgenin 4 haftalık elektrik gideri kaç TL’dir?',
 dogru=48,yan=[(Fr(48,5),'Harcanan enerjiyi (9,6 kWh) bulup birim bedelle çarpmayı unutmuş.','dikkat'),(12,'Yalnızca bir haftanın giderini hesaplamış; 4 haftayı atlamış.','dikkat'),(480,'800 W’ı 8 kW almış; watt–kilowatt dönüşümünü yanlış yapmış.','bilgi'),(Fr(24,5),'800 W’ı 0,08 kW almış; watt–kilowatt dönüşümünü yanlış yapmış.','bilgi')],
 istenen='4 haftalık toplam elektrik gideri (TL).',
 ad=[A('Gücü kW yap','800 W, 1000’e bölünerek kW olur.','800 W = 0,8 kW'),A('Haftalık enerji','Güç süreyle çarpılır.','E = 0,8 × 3 = 2,4 kWh'),A('4 haftalık enerji','Haftalık enerji hafta sayısıyla çarpılır.','E = 2,4 × 4 = 9,6 kWh'),A('Gider','Enerji birim bedelle çarpılır.','9,6 × 5 = 48 TL')])
# ---------- 0006  seri devre, voltmetre
V=36;R1,R2,R3=2,4,12; I=Fr(V,R1+R2+R3); assert I==2 and I*R3==24 and I*(R1+R2)==12
mk(P,'0006',tipId='fz-el-akim-gerilim',tip='Devrede akım ve gerilim',z='orta',alt='Elektrik Devreleri',kaz='Seri devrede akımı bulup bir elemanın uçları arasındaki gerilimi hesaplar.',kalip='şekilli',adim=3,
 kart='K-FZEL-06 (seri devrede voltmetre okuması) · yeni değerler, voltmetre R₃ uçlarında',
 metin='Şekildeki devrede üreteç ve voltmetre idealdir. R₁ = 2 Ω, R₂ = 4 Ω ve R₃ = 12 Ω’dur.\nBuna göre voltmetre kaç V’u gösterir?',
 sekil=devre(V='36 V',ust=[('R','R₁'),('R','R₂')],kol=[[('R','R₃')],[('V','')]]),
 dogru=24,yan=[(2,'Devredeki akımı (2 A) voltmetrenin okuması sanmış.','dikkat'),(12,'R₃’ün direnç değerini ya da R₁–R₂ uçlarındaki gerilimi (12 V) okuma sanmış.','dikkat'),(18,'Toplam direnci (18 Ω) gerilim değeri sanmış.','bilgi'),(8,'R₂ uçlarındaki gerilimi (2 × 4) okuma sanmış; voltmetre R₃’tedir.','dikkat')],
 istenen='R₃ direncinin uçlarına bağlı voltmetrenin okuması.',
 ip=['Seri devrede her dirençten aynı akım geçer.','Toplam direnç ile üreteç geriliminden akımı bul.','Voltmetre, R₃’ün uçlarındaki gerilimi okur: V = I × R₃.'],
 bilgi=[OHM,ILE],
 ad=[A('Toplam direnç','Seri bağlı dirençler toplanır.','R = 2 + 4 + 12 = 18 Ω'),A('Devre akımı','Seri devrede akım her yerde aynıdır.','I = 36 ÷ 18 = 2 A'),A('Voltmetre okuması','Voltmetre R₃’ün uçlarındadır.','V = 2 × 12 = 24 V')],
 puf='Seri devrede önce ortak akımı bul; bir elemanın gerilimi o akımın elemanın direnciyle çarpımıdır.')
V=30;R1,R2,R3=3,5,7; I=Fr(V,R1+R2+R3); assert I==2 and I*R2==10 and I*(R1+R3)==20
mk(P,'0006',True,metin='Şekildeki devrede üreteç ve voltmetre idealdir. R₁ = 3 Ω, R₂ = 5 Ω ve R₃ = 7 Ω’dur.\nBuna göre voltmetre kaç V’u gösterir?',
 sekil=devre(V='30 V',ust=[('R','R₁')],kol=[[('R','R₂')],[('V','')]],alt=[('R','R₃')]),
 dogru=10,yan=[(2,'Devredeki akımı (2 A) voltmetrenin okuması sanmış.','dikkat'),(15,'Toplam direnci (15 Ω) gerilim değeri sanmış.','bilgi'),(20,'R₁ ve R₃ uçlarındaki gerilimi (2 × 10) okuma sanmış; voltmetre R₂’dedir.','dikkat'),(30,'Üretecin gerilimini voltmetrenin okuması sanmış.','bilgi')],
 istenen='R₂ direncinin uçlarına bağlı voltmetrenin okuması.',
 ad=[A('Toplam direnç','Üç direnç seri bağlıdır.','R = 3 + 5 + 7 = 15 Ω'),A('Devre akımı','Seri devrede akım her yerde aynıdır.','I = 30 ÷ 15 = 2 A'),A('Voltmetre okuması','Voltmetre R₂’nin uçlarındadır.','V = 2 × 5 = 10 V')])
# ---------- 0007  anahtar kapanınca ampermetre (zor)
V=24;R1,R3,R2=2,6,3; Ia=Fr(V,R1+R3); Ik=Fr(V)/(R1+PAR_A(R3,R2)); Vp=Ik*PAR_A(R3,R2)
assert Ia==3 and Ik==6 and Ik-Ia==3 and Vp==12 and Vp/R2==4 and Vp/R3==2
mk(P,'0007',tipId='fz-el-anahtar-lamba',tip='Anahtar ve lamba parlaklığı',z='zor',alt='Elektrik Devreleri',kaz='Anahtarın açılıp kapanmasıyla devrenin eşdeğer direncindeki ve akımdaki değişimi hesaplar.',kalip='şekilli',adim=5,
 kart='K-FZEL-07 (anahtarın etkisi) · yeni değerler, istenen kapalı durum okuması',
 metin='Şekildeki devrede üreteç ve ampermetre idealdir. R₁ = 2 Ω, R₂ = 3 Ω ve R₃ = 6 Ω’dur. S anahtarı açıkken devre dengeye ulaşmıştır.\nS anahtarı kapatılırsa ampermetre kaç A’i gösterir?',
 sekil=devre(V='24 V',ust=[('R','R₁'),('A','')],kol=[[('R','R₃')],[('R','R₂'),('O','S')]]),
 dogru=6,yan=[(1,'R₃’ten geçen akımdaki azalmayı (3 A → 2 A) okuma sanmış.','dikkat'),(2,'Kapalı durumda yalnız R₃’ten geçen akımı (2 A) okuma sanmış; ampermetre toplam akımı ölçer.','dikkat'),(3,'Anahtar açıkken okunan değeri yazmış; S’nin kapanmasını hesaba katmamış.','dikkat'),(4,'Kapalı durumda yalnız R₂ koluna giden akımı (4 A) okuma sanmış.','dikkat')],
 istenen='S kapalıyken ampermetrenin okuması.',
 ip=['Anahtar açıkken akımın hangi dirençlerden geçtiğini belirle.','Anahtar kapanınca R₂ ve R₃ paralel olur; yeni toplam direnci bul.','İki durumdaki akımı ayrı ayrı hesapla ve farkı al.'],
 bilgi=[OHM,ILE],
 ad=[A('S açıkken','R₂ koluna akım gitmez; devrede yalnız R₁ ve R₃ vardır.','R = 2 + 6 = 8 Ω'),A('S açıkken akım','Ampermetre toplam akımı okur; bu, anahtar açıkken değerdir.','I₁ = 24 ÷ 8 = 3 A'),A('S kapalıyken direnç','R₂ ve R₃ paralel olur, R₁ ile seri kalır.','R₂₃ = (3 × 6) ÷ 9 = 2 Ω · R = 2 + 2 = 4 Ω'),A('S kapalıyken akım','Ampermetre toplam akımı okur.','I₂ = 24 ÷ 4 = 6 A'),A('Kontrol','Paralel uç gerilimi 12 V; kol akımları toplam akımı vermelidir.','V₂₃ = 6 × 2 = 12 V · I₃ + I₂ = 2 + 4 = 6 A')],
 puf='Anahtarlı sorularda ilgili durumun toplam direncini yeniden bul; kol akımlarının toplamı ana akıma eşit olmalıdır.')
V=24;R1,R3,R2=4,8,8; Ia=Fr(V,R1+R3); Ik=Fr(V)/(R1+PAR_A(R3,R2)); Vp=Ik*PAR_A(R3,R2)
assert Ia==2 and Ik==3 and Ik-Ia==1 and Vp==12 and Vp/R2==Fr(3,2)
mk(P,'0007',True,metin='Şekildeki devrede üreteç ve ampermetre idealdir. R₁ = 4 Ω, R₂ = 8 Ω ve R₃ = 8 Ω’dur. S anahtarı açıkken devre dengeye ulaşmıştır.\nS anahtarı kapatılırsa ampermetrenin gösterdiği değer kaç A artar?',
 sekil=devre(V='24 V',ust=[('R','R₁')],kol=[[('R','R₃')],[('R','R₂'),('O','S')]],alt=[('A','')]),
 dogru=1,yan=[(Fr(3,2),'Kapalı durumda her paralel koldan geçen akımı (1,5 A) artış sanmış.','dikkat'),(2,'Anahtar açıkken okunan değeri (2 A) artış sanmış.','dikkat'),(3,'Anahtar kapalıyken okunan değeri (3 A) artış sanmış; ilk değeri çıkarmamış.','dikkat'),(6,'24 V’u yalnızca R₁’e uygulamış (24 ÷ 4); devrenin geri kalanını atlamış.','bilgi')],
 istenen='Ampermetre okumasındaki artış (A).',
 ad=[A('S açıkken','Yalnız R₁ ve R₃ devrededir.','R = 4 + 8 = 12 Ω'),A('S açıkken akım','Ampermetre toplam akımı okur.','I₁ = 24 ÷ 12 = 2 A'),A('S kapalıyken direnç','R₂ ve R₃ paralel olur, R₁ ile seri kalır.','R₂₃ = (8 × 8) ÷ 16 = 4 Ω · R = 4 + 4 = 8 Ω'),A('S kapalıyken akım','Toplam akım yeni dirence göre bulunur.','I₂ = 24 ÷ 8 = 3 A'),A('Artış','Son değerden ilk değer çıkarılır.','3 − 2 = 1 A')])
# ---------- 0008  lamba parlaklığı (öncüllü)
# ana: K ust seri; L ve M paralel kol, M kolunda S. R özdeş, V ideal. Birimler V²/R.
Rr=Fr(1); Vv=Fr(1)
Ia=Vv/(2*Rr); PK0=Ia**2*Rr; PL0=PK0
Rt=Rr+Rr/2; Ik=Vv/Rt; PK1=Ik**2*Rr; Vp=Ik*Rr/2; PL1=Vp**2/Rr; PM1=PL1
assert PK1>PK0 and PL1<PL0 and PM1<PK1 and PM1==PL1 and (PK0,PK1,PL1)==(Fr(1,4),Fr(4,9),Fr(1,9))
S_=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
mk(P,'0008',tipId='fz-el-anahtar-lamba',tip='Anahtar ve lamba parlaklığı',z='zor',alt='Elektrik Devreleri',kaz='Anahtar kapanınca lambaların akımındaki ve parlaklığındaki değişimi karşılaştırır.',kalip='öncüllü',adim=5,
 kart='K-FZEL-08 (anahtar sonrası lamba parlaklığı) · yeni bağlantı, öncüllü',
 metin='Şekildeki devrede K, L ve M lambaları özdeştir; lambaların dirençleri sabit, üreteç idealdir. S anahtarı açıkken devre dengeye ulaşmıştır.\nS anahtarı kapatılırsa;\nI. K lambasının parlaklığı artar.\nII. L lambasının parlaklığı azalır.\nIII. M lambasının parlaklığı K lambasınınkinden fazla olur.\nifadelerinden hangileri doğrudur?',
 sekil=devre(V='V',ust=[('L','K')],kol=[[('L','L')],[('L','M'),('O','S')]]),
 dogru='I ve II',sira=S_,yan=[('Yalnız I','L’nin de paralel kolda akımının azaldığını görememiş.','dikkat'),('I ve III','III’ü doğru sanmış; M ve L özdeş paralel kollardır, her birinin akımı K’nınkinin yarısıdır.','bilgi'),('II ve III','Toplam direnç azaldığından K’nın akımının arttığını (I) atlamış.','dikkat'),('I, II ve III','M’nin K’dan parlak olduğunu sanmış; K’dan geçen akım M ve L’ninkinin iki katıdır.','bilgi')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',
 ip=['Anahtar açıkken ve kapalıyken devrenin toplam direncini karşılaştır.','Parlaklık, lambadan geçen akımla artar. K’dan geçen akım değişti mi?','Kapalıyken K’nın akımı L ve M arasında nasıl paylaşılıyor?'],
 bilgi=[B('Lamba parlaklığı','lambanın gücü P = I² × R; dirençleri sabit özdeş lambalarda akım ne kadar büyükse lamba o kadar parlaktır'),ILE],
 ad=[A('S açıkken','Devrede yalnız K ve L seri bağlıdır; direnç R seçilirse toplam direnç 2R olur.','I = V ÷ 2R · K ve L’nin gücü eşit'),A('S kapalıyken','L ve M paralel olur: eşdeğeri R ÷ 2. K ile seri toplam direnç 1,5R olur.','R = R + R ÷ 2 = 3R ÷ 2 · I = 2V ÷ 3R'),A('K lambası','Toplam akım arttığından K’dan geçen akım artar; I doğru.','K: V ÷ 2R → 2V ÷ 3R (artar)'),A('L lambası','K’dan gelen akım L ve M’ye eşit bölünür; L’nin akımı V ÷ 3R olur ve ilk değerden küçüktür; II doğru.','L: V ÷ 2R → V ÷ 3R (azalır)'),A('M ve K','M’nin akımı L’ninkine eşittir ve K’nınkinin yarısıdır. M, K’dan sönük kalır; III yanlış.','M: V ÷ 3R, K: 2V ÷ 3R')],
 puf='Anahtar kapanınca önce toplam akımı bul, sonra her lambadan geçen akımı yeniden hesaplayıp ilk haliyle karşılaştır.')
# kardeş: K ve L seri, M'ye paralel anahtar (M kısa devre)
Rr=Fr(1);Vv=Fr(1)
I0=Vv/(3*Rr); I1=Vv/(2*Rr); assert I1>I0
S2=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
mk(P,'0008',True,metin='Şekildeki devrede K, L ve M lambaları özdeştir; lambaların dirençleri sabit, üreteç idealdir. S anahtarı açıkken devre dengeye ulaşmıştır.\nS anahtarı kapatılırsa;\nI. K lambasının parlaklığı artar.\nII. M lambasının parlaklığı artar.\nIII. Üretecin devreye verdiği akım artar.\nifadelerinden hangileri doğrudur?',
 sekil=devre(V='V',ust=[('L','K'),('L','L')],kol=[[('L','M')],[('O','S')]]),
 dogru='I ve III',sira=S2,yan=[('Yalnız I','Toplam akımın arttığını (III) atlamış.','dikkat'),('Yalnız II','S kapanınca M’nin akım yolunun dışında kaldığını (söndüğünü) görememiş.','bilgi'),('Yalnız III','K’nın da akımının arttığını (I) atlamış.','dikkat'),('I ve II','S kapanınca akımın M yerine anahtardan geçtiğini görmemiş; M’nin söndüğünü kaçırmış.','bilgi')],
 istenen='Doğru olan öncüllerin hangileri olduğu.',
 ad=[A('S açıkken','K, L ve M seri; direnç R seçilirse toplam direnç 3R olur.','I = V ÷ 3R'),A('S kapalıyken','Anahtar M’nin uçlarını telle birleştirir; akım M yerine anahtardan geçer, M söner. Toplam direnç 2R olur.','R = R + R = 2R · I = V ÷ 2R'),A('K lambası','Akım V ÷ 3R’den V ÷ 2R’ye çıkar; I doğru.','K: V ÷ 3R → V ÷ 2R (artar)'),A('M lambası','M’den akım geçmez; II yanlış.','M: V ÷ 3R → 0 (söner)'),A('Üreteç akımı','Toplam direnç azaldığından üretecin verdiği akım artar; III doğru.','I: V ÷ 3R → V ÷ 2R')])
bitir(P,'elektrik','fiz|Elektrik')
