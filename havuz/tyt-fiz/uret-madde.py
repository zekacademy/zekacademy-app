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
KONU='Madde ve Özellikleri'
P=Parti('madde','Madde ve Özellikleri','fiz|Madde ve Özellikleri',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 (madde ve özkütle, yapışma) · MEB 9. sınıf'
def grafik_mV(cizgiler,xmax,ymax,xt,yt):
    """cizgiler: [(etiket,(V,m))] orijinden geçen doğrular; noktalar kesikli çizgiyle işaretlenir."""
    x0,y0,x1,y1=46,16,300,150
    X=lambda v:x0+(x1-x0)*v/xmax; Y=lambda m:y1-(y1-y0)*m/ymax
    o=[f'<path d="M{x0} {y0-4} L{x0} {y1} L{x1+6} {y1}" stroke-width="1.6"/>']
    o.append(T(x0-6,y0,'m (g)',anchor='end',size=11)); o.append(T(x1+4,y1+16,'V (cm³)',anchor='end',size=11))
    for t in xt: o.append(f'<path d="M{X(t)} {y1} l0 4" stroke-width="1.2"/>'+T(X(t),y1+14,str(t),size=11))
    for t in yt: o.append(f'<path d="M{x0} {Y(t)} l-4 0" stroke-width="1.2"/>'+T(x0-8,Y(t)+4,str(t),anchor='end',size=11))
    for et,(v,m) in cizgiler:
        ex=min(xmax,ymax*v/m); ey=ex*m/v
        o.append(f'<path d="M{X(0)} {Y(0)} L{X(ex)} {Y(ey)}" stroke-width="2" style="stroke:var(--acc,#16A34A)"/>')
        o.append(f'<path d="M{x0} {Y(m)} L{X(v)} {Y(m)} L{X(v)} {y1}" stroke-width="1" stroke-dasharray="3 3"/><circle cx="{X(v)}" cy="{Y(m)}" r="2.8" style="fill:currentColor"/>')
        o.append(T(X(ex)-4,Y(ey)-6,et,anchor='end',bold=True))
    return G._svg(330,176,''.join(o))
kart('K-FZMD-01','Özkütle bağıntısı','d = m/V; üç büyüklükten ikisi verilince üçüncüsü bulunur.','Bağıntıyı ters kurmak.','kolay','düz',2,'fz-md-ozkutle','Özkütle bağıntısı',KY)
kart('K-FZMD-02','Karışımın özkütlesi','Homojen karışımda d = toplam kütle / toplam hacim.','Özkütlelerin aritmetik ortalamasını almak.','orta','hikâyeli',3,'fz-md-karisim','Karışımın özkütlesi',KY)
kart('K-FZMD-03','Kap ve sıvı kütlesi','İki farklı doluluk durumundan kabın kütlesi ayrıştırılır.','Yarı dolu kabın kütlesini yalnız sıvı sanmak.','orta','hikâyeli',3,'fz-md-kap','Kap ve sıvı kütlesi',KY)
kart('K-FZMD-04','Adezyon ve kohezyon','Aynı cins moleküller arası çekim kohezyon, farklı cins moleküller arası çekim adezyondur.','İki kavramı karıştırmak.','orta','öncüllü',2,'fz-md-yapisma','Yapışma ve birbirini tutma',KY)
kart('K-FZMD-05','m–V grafiğinden karışım','Doğruların eğimi özkütledir; eşit kütlede hacimler farklı olur.','Eşit kütlede ortalama özkütle almak.','zor','grafik',4,'fz-md-grafik','Özkütle grafiği ve karışım',KY)
kart('K-FZMD-06','İçi boş cisim','Boşluk hacmi = toplam hacim − (kütle / madde özkütlesi).','Maddenin hacmini boşluk sanmak.','zor','hikâyeli',4,'fz-md-bosluk','İçi boş cisimde boşluk hacmi',KY)
D=B('Özkütle','d = m ÷ V (kütle ÷ hacim). Birimi g/cm³ ya da kg/m³. Örnek: 40 g kütleli, 10 cm³ hacimli cismin özkütlesi 4 g/cm³')
# 0001
d,V=5,20; assert d*V==100 and Fr(V,d)==4 and V-d==15 and V+d==25 and Fr(d,V)==Fr(1,4)
mk(P,'0001',tipId='fz-md-ozkutle',tip='Özkütle bağıntısı',z='kolay',alt='Madde ve Özkütle',kaz='Özkütle, kütle ve hacim arasındaki bağıntıyı kullanır.',kalip='düz',adim=2,
 kart='K-FZMD-01 (d = m/V) · kütle istenen',
 metin='Özkütlesi 5 g/cm³ olan maddeden yapılmış cismin hacmi 20 cm³’tür.\nBuna göre cismin kütlesi kaç g’dır?',
 dogru=100,yan=[(Fr(1,4),'Özkütleyi hacme bölmüş (5 ÷ 20); bağıntıyı ters kurmuş.','bilgi'),(4,'Hacmi özkütleye bölmüş (20 ÷ 5); kütle yerine hacim ile özkütle oranını bulmuş.','bilgi'),(15,'Hacimden özkütleyi çıkarmış; büyüklükler çarpılmalıdır.','bilgi'),(25,'Hacimle özkütleyi toplamış; farklı büyüklükler toplanmaz.','bilgi')],
 istenen='Cismin kütlesi (g).',ip=['d = m ÷ V bağıntısından m’yi yalnız bırak.'],bilgi=[D],
 ad=[A('Bağıntıyı yaz','Özkütle kütlenin hacme oranıdır.','d = m ÷ V'),A('Kütleyi çek','Her iki tarafı V ile çarp.','m = d × V'),A('Hesapla','Değerleri yerine yaz.','m = 5 × 20 = 100 g')],
 puf='Üç büyüklükten ikisini bilince d = m ÷ V ile üçüncüsünü bul; çarpma ya da bölmeyi birim düşünerek seç (g/cm³ × cm³ = g).')
# 0002
d1,V1,d2,V2=Fr(4,5),200,Fr(6,5),300; m=d1*V1+d2*V2; dk=m/(V1+V2); assert m==520 and dk==Fr(26,25)
assert (d1*V2+d2*V1)/(V1+V2)==Fr(24,25) and (d1+d2)/2==1 and d1+d2==2
mk(P,'0002',tipId='fz-md-karisim',tip='Karışımın özkütlesi',z='orta',alt='Madde ve Özkütle',kaz='Birbiri içinde tamamen çözünen sıvıların karışımının özkütlesini hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-FZMD-02 (karışımın özkütlesi) · yeni sıvılar ve hacimler',
 metin='Özkütlesi 0,8 g/cm³ olan 200 cm³ sıvı ile özkütlesi 1,2 g/cm³ olan 300 cm³ sıvı birbirine karıştırılıyor.\nSıvılar birbiri içinde tamamen çözündüğüne ve karışımda hacim değişmediğine göre karışımın özkütlesi kaç g/cm³ olur?',
 dogru=Fr(26,25),yan=[(Fr(24,25),'Hacimleri ters yerleştirmiş: 0,8 × 300 ile 1,2 × 200’ü toplamış.','dikkat'),(1,'Özkütlelerin aritmetik ortalamasını almış; hacimlerin farklı olduğunu hesaba katmamış.','bilgi'),(Fr(6,5),'Büyük hacimli sıvının özkütlesini karışımın özkütlesi sanmış.','dikkat'),(2,'İki özkütleyi toplamış (0,8 + 1,2).','bilgi')],
 istenen='Karışımın özkütlesi (g/cm³).',ip=['Her sıvının kütlesini m = d × V ile bul.'],
 bilgi=[D,B('Karışımın özkütlesi','d(karışım) = toplam kütle ÷ toplam hacim. Örnek: 10 g + 30 g kütleli sıvılar 40 cm³ oluşturuyorsa d = 40 ÷ 40 = 1 g/cm³')],
 ad=[A('Kütleleri bul','Her sıvının kütlesi özkütle ile hacmin çarpımıdır.','m₁ = 0,8 × 200 = 160 g · m₂ = 1,2 × 300 = 360 g'),A('Toplamları al','Kütleler ve hacimler ayrı ayrı toplanır.','m = 160 + 360 = 520 g · hacim = 200 + 300 = 500 cm³'),A('Özkütleyi bul','Toplam kütle toplam hacme bölünür.','d = 520 ÷ 500 = 1,04 g/cm³')],
 puf='Karışımlarda özkütleleri ortalama alma; toplam kütleyi toplam hacme böl.')
# 0003
tam,yari=700,450; sivi_yari=tam-yari; sivi_tam=2*sivi_yari; kap=tam-sivi_tam
assert sivi_yari==250 and sivi_tam==500 and kap==200 and tam//2==350
mk(P,'0003',tipId='fz-md-kap',tip='Kap ve sıvı kütlesi',z='orta',alt='Madde ve Özkütle',kaz='Kap ve sıvı kütlelerini iki farklı doluluk durumundan ayırır.',kalip='hikâyeli',adim=3,
 kart='K-FZMD-03 (kap ve sıvı) · yeni kütleler, boş kabın kütlesi istenen',
 metin='Homojen sıvı dolu bir kabın kütlesi 700 g’dır. Sıvının yarısı boşaltılınca kabın kütlesi 450 g oluyor.\nBuna göre boş kabın kütlesi kaç g’dır?',
 dogru=200,yan=[(250,'Boşaltılan yarım sıvının kütlesini (250 g) kabın kütlesi sanmış.','dikkat'),(350,'700’ün yarısını almış; kabın kütlesini de ikiye bölmüş.','bilgi'),(450,'Yarı dolu kabın kütlesini boş kap sanmış.','dikkat'),(500,'Tüm sıvının kütlesini (500 g) kabın kütlesi sanmış.','dikkat')],
 istenen='Boş kabın kütlesi (g).',ip=['İki durum arasındaki kütle farkı, boşaltılan sıvının kütlesidir.'],bilgi=[B('Kütle farkı','kütle azalması boşaltılan maddenin kütlesine eşittir. Örnek: 300 g olan kaptan 50 g su dökülürse 250 g kalır')],
 ad=[A('Yarım sıvının kütlesi','Kütledeki azalma boşaltılan sıvıdır.','700 − 450 = 250 g'),A('Tüm sıvının kütlesi','Boşaltılan, sıvının yarısıdır.','250 × 2 = 500 g'),A('Kabın kütlesi','Dolu kabın kütlesinden sıvının kütlesi çıkarılır.','700 − 500 = 200 g')],
 puf='Doluluk değişen kaplarda kütle farkından sıvının kütlesini bul, kalanı kaba ait say.')
# 0004
S=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
mk(P,'0004',tipId='fz-md-yapisma',tip='Yapışma ve birbirini tutma',z='orta',alt='Yapışma ve Birbirini Tutma',kaz='Adezyon ve kohezyon kuvvetlerini günlük olaylarla ayırt eder.',kalip='öncüllü',adim=2,
 kart='K-FZMD-04 (adezyon ve kohezyon) · yeni günlük olaylar',
 metin='I. Tebeşirin tahtaya sürtüldüğünde iz bırakması\nII. Cıva damlasının cam yüzeyinde küre biçimini alması\nIII. Boya fırçasındaki boyanın duvara yapışması\nYukarıdaki olaylardan hangileri adezyon (yapışma) kuvvetinin etkisiyle açıklanır?',
 dogru='I ve III',sira=S,yan=[('Yalnız I','III’teki boya ile duvarın farklı cins olduğunu görememiş.','dikkat'),('Yalnız III','I’deki tebeşir ile tahtanın farklı cins olduğunu görememiş.','dikkat'),('I ve II','Cıvanın kendi molekülleri arasındaki çekimi (kohezyon) adezyon sanmış.','bilgi'),('II ve III','Cıva damlasının küre biçimini adezyona bağlamış; bu kohezyondur.','bilgi')],
 istenen='Adezyonla açıklanan olayların hangileri olduğu.',ip=['Her olayda birbirine tutunan maddelerin aynı cins mi farklı cins mi olduğuna bak.'],
 bilgi=[B('Adezyon ve kohezyon','adezyon farklı cins moleküller arasındaki çekimdir (tebeşir–tahta); kohezyon aynı cins moleküller arasındaki çekimdir (su damlasındaki su molekülleri)')],
 ad=[A('Kavramı ayır','Farklı maddeler arasındaki çekim adezyon, aynı madde içindeki çekim kohezyondur.','adezyon: farklı cins · kohezyon: aynı cins'),A('I ve III','Tebeşir–tahta ve boya–duvar farklı maddelerdir.','I: adezyon · III: adezyon'),A('II','Cıva damlasını bir arada tutan cıva moleküllerinin birbirini çekmesidir.','II: kohezyon'),A('Sonuç','Adezyon yalnız I ve III’tür.','I ve III')],
 puf='Önce iki tarafın aynı mı farklı mı madde olduğuna bak: farklıysa adezyon, aynıysa kohezyon.')
# 0005
dX,dY=6,2; mm=60; Vx,Vy=Fr(mm,dX),Fr(mm,dY); dk=2*mm/(Vx+Vy); assert dk==3 and (dX+dY)/2==4 and dX+dY==8 and dX==6 and dX*dY==12 and Vx==10 and Vy==30
mk(P,'0005',tipId='fz-md-grafik',tip='Özkütle grafiği ve karışım',z='zor',alt='Madde ve Özkütle',kaz='Kütle–hacim grafiğinden özkütle bulup eşit kütleli karışımın özkütlesini hesaplar.',kalip='grafik',adim=4,
 kart='K-FZMD-05 (m–V grafiği, eşit kütleli karışım) · yeni doğrular',
 metin='Şekilde X ve Y maddelerinin kütle–hacim grafikleri verilmiştir.\nX ve Y’den eşit kütlede alınarak tamamen çözünen bir karışım hazırlanıyor ve hacim değişmiyor.\nBuna göre karışımın özkütlesi kaç g/cm³ olur?',
 sekil=grafik_mV([('X',(10,60)),('Y',(30,60))],40,80,[10,30],[60]),
 dogru=3,yan=[(4,'Özkütlelerin aritmetik ortalamasını almış; kütleler eşit olduğunda hacimler eşit değildir.','bilgi'),(6,'X’in özkütlesini karışımın özkütlesi sanmış.','dikkat'),(8,'İki özkütleyi toplamış (6 + 2).','bilgi'),(12,'Özkütleleri çarpmış (6 × 2).','bilgi')],
 istenen='Karışımın özkütlesi (g/cm³).',ip=['Grafikte her madde için aynı kütleye karşılık gelen hacmi oku ve özkütleleri bul.'],bilgi=[D,B('Karışımın özkütlesi','d = toplam kütle ÷ toplam hacim. Örnek: 20 g + 20 g kütle, 10 + 20 cm³ hacim → 40 ÷ 30 g/cm³')],
 ad=[A('Özkütleleri oku','Grafikte 60 g’a karşılık X için 10 cm³, Y için 30 cm³ okunur.','dX = 60 ÷ 10 = 6 g/cm³ · dY = 60 ÷ 30 = 2 g/cm³'),A('Eşit kütle seç','Her maddeden 60 g alındığında toplam kütle 120 g olur.','m = 60 + 60 = 120 g'),A('Toplam hacim','Hacimler kütleyi özkütleye bölerek bulunur; grafikten de 10 ve 30 cm³ okunur.','V = 10 + 30 = 40 cm³'),A('Karışımın özkütlesi','Toplam kütleyi toplam hacme böl.','d = 120 ÷ 40 = 3 g/cm³')],
 puf='Eşit kütlede özkütleler ortalaması alınmaz; toplam kütleyi toplam hacme bölmek gerekir.')
# 0006
Vt,m,dm=150,300,5; Vm=Fr(m,dm); bos=Vt-Vm; assert Vm==60 and bos==90 and Vt+Vm==210 and m+Vt==450
mk(P,'0006',tipId='fz-md-bosluk',tip='İçi boş cisimde boşluk hacmi',z='zor',alt='Madde ve Özkütle',kaz='İçi boş cismin madde hacmini ve boşluk hacmini özkütle bağıntısıyla bulur.',kalip='hikâyeli',adim=4,
 kart='K-FZMD-06 (içi boş cisim) · yeni sayılar',
 metin='Özkütlesi 5 g/cm³ olan maddeden yapılmış, içinde hava boşluğu bulunan cismin kütlesi 300 g, dış hacmi 150 cm³’tür. Boşluğun kütlesi ihmal edilmektedir.\nBuna göre cismin içindeki boşluğun hacmi kaç cm³’tür?',
 dogru=90,yan=[(60,'Maddenin hacmini boşluk hacmi sanmış.','dikkat'),(150,'Cismin dış hacmini boşluk hacmi sanmış.','dikkat'),(210,'Dış hacimle madde hacmini toplamış (150 + 60).','islem'),(450,'Kütle ile dış hacmi toplamış; farklı büyüklükler toplanmaz.','bilgi')],
 istenen='Boşluğun hacmi (cm³).',ip=['Önce cismi oluşturan maddenin gerçek hacmini bul.'],bilgi=[D],
 ad=[A('Madde hacmi','Maddenin kütlesi ve özkütlesi biliniyor; V = m ÷ d.','V(madde) = 300 ÷ 5 = 60 cm³'),A('Dış hacim','Cismin kapladığı toplam hacim 150 cm³’tür; bu madde ile boşluğun toplamıdır.','V(dış) = V(madde) + V(boşluk)'),A('Boşluk','Dış hacimden madde hacmi çıkarılır.','V(boşluk) = 150 − 60 = 90 cm³')],
 puf='İçi boş cisimlerde maddenin hacmini V = m ÷ d ile bul, dış hacimden çıkar.')
bitir(P,'madde','fiz|Madde ve Özellikleri')
