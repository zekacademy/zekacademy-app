"""TYT Kimya · Kimyanın Temel Kanunları · ek paket (kanunlariki): 18 soru, kardeş yok, ipucu 1.
Şekil verileri (terazi, kütle–kütle grafiği, tablo, gaz hacimleri, tanecik modeli) Python'da hesaplanır; her cevap ve çeldirici değer assert edilir."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
KONU_='Kimyanın Temel Kanunları'; UK='kim|Kimyanın Temel Kanunları'
H.KONU=KONU_
P=Parti('kanunlariki',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 TYT Kimya (yalnız mantık) · MEB 10. sınıf Kimyanın Temel Kanunları'
TIPAD={'korunum':'Kütlenin korunumu (açık ve kapalı kap)','sabit':'Sabit oranlar ve artan madde','katli':'Katlı oranlar ve formül',
       'hacim':'Birleşen hacim oranları ve Avogadro hipotezi','tur':'Tepkime türleri','denk':'Tepkime denklemi ve denkleştirme'}
def kartla(n,alt,fikir,tuzak,z,kalip,adim,t):
    kart(f'K-KMKN2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-kn2-{t}',TIPAD[t],KY)
def q(no,ad,t,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    mk(P,no,ad=ad,adim=len(ad),tipId=f'km-kn2-{t}',tip=TIPAD[t],**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def ad_(s): return ('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
def onc(durum,ops,dogru_ara=True):
    """durum {öncül:(doğru_mu,gerekçe)}; dogru_ara=True: 'doğrudur' kökü, False: 'yanlıştır' kökü. ops: 5 şık (ORD içinden, alışılmış sırada)."""
    T=frozenset(k for k,v in durum.items() if v[0]==dogru_ara)
    names=[ad_(sorted(T,key=lambda x:'I II III'.split().index(x)))]
    assert ops==[o for o in ORD if o in ops] and len(ops)==5 and names[0] in ops,(ops,names)
    yan=[]
    for o in ops:
        if o==names[0]: continue
        W=SETLER[o]
        p=[]
        for x in sorted(W-T,key=lambda x:'I II III'.split().index(x)):
            p.append(f'{x} öncülünü '+('doğru sanmış; oysa yanlıştır: ' if dogru_ara else 'yanlış sanmış; oysa doğrudur: ')+durum[x][1])
        for x in sorted(T-W,key=lambda x:'I II III'.split().index(x)):
            p.append(f'{x} öncülünü '+('yanlış sanmış; oysa doğrudur: ' if dogru_ara else 'doğru sanmış; oysa yanlıştır: ')+durum[x][1])
        yan.append((o,' '.join(p),'bilgi'))
    return dict(dogru=names[0],yan=yan,sira=ops)
SETLER={'Yalnız I':frozenset('I'),'Yalnız II':frozenset(['II']),'Yalnız III':frozenset(['III']),'I ve II':frozenset(['I','II']),'I ve III':frozenset(['I','III']),'II ve III':frozenset(['II','III']),'I, II ve III':frozenset(['I','II','III'])}
SETLER['Yalnız I']=frozenset(['I'])
def etk(d): return ' · '.join(f'{k}: '+('doğru' if v[0] else 'yanlış') for k,v in d.items())

# ================= 01 · açık/kapalı kap, terazi · kolay · öncüllü · şekil =================
kartla('01','Açık ve kapalı kapta kütle','Kapalı kapta toplam kütle değişmez; açık kapta çıkan gaz terazide görünmez, çıkan gazın kütlesi hesaba katılınca kütle korunur.','Açık kapta kütle azalmasını kanuna aykırı saymak.','kolay','öncüllü',4,'korunum')
m0,mK,mA=250,250,246; gaz=m0-mA; assert gaz==4 and mK==m0
def erlen(x,kapali,onc_,son):
    s=f'\\draw[thick,fill=gray!15] ({x-1.1},-.3) rectangle ({x+1.1},0);'
    s+=f'\\fill[vurgu!15] ({x-.8},0) -- ({x+.8},0) -- ({x+.54},.45) -- ({x-.54},.45) -- cycle;'
    s+=f'\\draw[thick] ({x-.25},1.3) -- ({x-.25},.95) -- ({x-.8},0) -- ({x+.8},0) -- ({x+.25},.95) -- ({x+.25},1.3);'
    if kapali: s+=f'\\draw[thick,fill=gray!45] ({x-.3},1.3) rectangle ({x+.3},1.55);'
    s+=f'\\node at ({x},2.05) {{\\textbf{{{"Kapalı kap" if kapali else "Açık kap"}}}}};'
    s+=f'\\node[align=center] at ({x},-1.2) {{Önce: {onc_} g\\\\Sonra: {son} g}};'
    return s
SK1=tk(erlen(0,True,m0,mK)+erlen(3.2,False,m0,mA))
q('0001',[A('Kapalı kabı yorumla','Kapalı kapta madde giriş ve çıkışı yoktur.',f'{m0} g → {mK} g · kütle değişmemiş'),
  A('Açık kabı yorumla','Açık kapta oluşan gaz ortama geçebilir.',f'{m0} g → {mA} g · {gaz} g azalmış'),
  A('Azalmanın nedenini bul','Terazi yalnız kabın içinde kalanı gösterir; azalan kütle yok olmamış, kaptan ayrılmıştır.','Kaybolan kütle = çıkan CO₂ kütlesi'),
  A('Öncülleri değerlendir','Kanun, giren ve çıkan bütün maddeler hesaba katılırsa geçerlidir.','I: doğru · II: yanlış · III: doğru')],'korunum',
 z='kolay',alt='Açık ve Kapalı Kapta Kütle',kaz='Açık ve kapalı kapta tepkime sırasındaki kütle değişimini kütlenin korunumu kanunuyla yorumlar.',kalip='öncüllü',
 kart='K-KMKN2-01 (açık/kapalı kap) · CaCO₃ + HCl, terazi',sekil=SK1,
 metin='Bir laboratuvarda, aynı miktarda HCl çözeltisi içeren iki özdeş erlen ayrı terazilere konuyor. Her erlene aynı miktarda CaCO₃ katısı atılıyor ve CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂ tepkimesi gerçekleşiyor. Biri tıpayla kapatılmış, diğeri açık bırakılan erlenlerde tepkime tamamlanınca terazi okumaları şekildeki gibi oluyor.\nBuna göre,\nI. Kapalı kaptaki kütlenin değişmemesi, kütlenin korunumu kanunuyla uyumludur.\nII. Açık kaptaki kütle azalması, kütlenin korunumu kanununa aykırıdır.\nIII. Açık kaptaki azalma, kaptan çıkan CO₂ gazının kütlesine eşittir.\nyargılarından hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Kapalı ve açık kapta terazinin neyi ölçtüğünü karşılaştır.'],
 bilgi=[B('Kütlenin korunumu','kapalı bir sistemde tepkimeden önceki toplam kütle, tepkimeden sonraki toplam kütleye eşittir. Örnek: kapalı kapta 3 g A ile 5 g B tepkimeye girerse ürünlerin toplam kütlesi 8 g olur')],
 puf='Açık kapta kütle azalıyorsa ya da artıyorsa ortama çıkan ya da giren gazı düşün; kanun yine geçerlidir.',
 **onc({'I':(True,'Kapalı kapta madde alışverişi olmadığından kütle sabit kalır.'),'II':(False,'Azalan 4 g, kaptan çıkan CO₂ gazıdır; çıkan gaz da hesaba katılınca kütle korunur.'),'III':(True,'250 − 246 = 4 g, ortama karışan CO₂ kütlesidir.')},
   ['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']))

# ================= 02 · CaCO3 ayrışması tablosu · orta · tablo =================
kartla('02','Kütlenin korunumu (tablo)','Her deneyde girenlerin kütlesi ürünlerin kütle toplamına eşittir; eksik hücreler bu eşitlikle bulunur.','Çıkarma yerine toplama; yanlış sütunu okuma.','orta','tablo',4,'korunum')
d2=[(25,14,11),(50,28,22),(100,56,44)]
for a,b,c in d2: assert a==b+c
X2=d2[0][0]-d2[0][1]; Y2=d2[1][0]-d2[1][2]; assert (X2,Y2)==(11,28)
SK2=tablo_svg(['Deney','CaCO₃ (g)','CaO (g)','CO₂ (g)'],[['1','25','14','X'],['2','50','Y','22'],['3','100','56','44']])
assert (25+14)+(50+22)==111 and X2+(50+22)==83 and (25+14)+Y2==67 and X2+22==33 and X2+Y2==39
q('0002',[A('Eşitliği yaz','Kapalı kapta ayrışmadan önceki kütle, ayrışma ürünlerinin toplam kütlesine eşittir.','m(CaCO₃) = m(CaO) + m(CO₂)'),
  A('X’i bul','1. deneyde bilinen değerler yerine konur.','25 = 14 + X → X = 11'),
  A('Y’yi bul','2. deneyde aynı eşitlik yazılır.','50 = Y + 22 → Y = 28'),
  A('Toplamı hesapla','Bulunan iki değer toplanır.','X + Y = 11 + 28 = 39')],'korunum',
 z='orta',alt='Kütlenin Korunumu',kaz='Kütlenin korunumu kanununu tablo verisine uygulayarak bilinmeyen kütleleri bulur.',kalip='tablo',
 kart='K-KMKN2-02 (kütlenin korunumu, tablo) · CaCO₃ ayrışması, eksik hücreler',sekil=SK2,
 metin='CaCO₃ katısı kapalı bir kapta ısıtıldığında CaO katısı ve CO₂ gazına ayrışmaktadır. Bir öğrenci, üç ayrı deneyde tepkimeye giren ve oluşan maddelerin kütlelerini aşağıdaki tabloda toplamıştır. Her deneyde CaCO₃ tamamen ayrışmış ve kap kapalı olduğu için ortama madde çıkmamıştır.\nTabloda X ve Y ile gösterilen kütleler ölçülememiştir. Buna göre X + Y toplamı kaç gramdır?',
 dogru=39,yan=[(111,'Kütleleri çıkarmak yerine toplamış: X için 25 + 14, Y için 50 + 22.','islem'),(83,'Y’yi 50 + 22 = 72 olarak toplayıp bulmuş; X’i doğru bulmuş.','islem'),(67,'X’i 25 + 14 = 39 olarak toplayıp bulmuş; Y’yi doğru bulmuş.','islem'),(33,'Y yerine tabloda zaten verilen CO₂ değerini (22) kullanmış.','dikkat')],
 istenen='X + Y toplamı (g).',ip=['Her satırda ayrışmadan önceki kütle ile sonraki kütlelerin toplamı arasındaki ilişkiyi kullan.'],
 bilgi=[B('Kütlenin korunumu','kapalı kapta tepkimeye girenlerin toplam kütlesi, ürünlerin toplam kütlesine eşittir. Örnek: 10 g A → 6 g B + 4 g C')],
 puf='Kapalı kapta tek maddeden oluşan ürünlerin kütle toplamı, ayrışan maddenin kütlesine eşittir.')

# ================= 03 · C–O2 kütle–kütle grafiği · kolay · grafik =================
kartla('03','Kütle–kütle grafiği','Doğrusal grafikteki noktadan sabit birleşme oranı okunur; bileşik kütlesi paylara bölünür.','Oranı doğrudan bileşik kütlesine uygulamak.','kolay','grafik',3,'sabit')
pts=[(8,3),(16,6),(24,9),(32,12)]
for o_,c_ in pts: assert Fr(c_,o_)==Fr(3,8)
oran=Fr(3,8); toplam=88; Cm=Fr(toplam*3,11); Om=Fr(toplam*8,11); assert Cm==24 and Om==64 and Cm+Om==toplam
assert Fr(toplam)*oran==33 and Fr(toplam,2)==44
sx,sy=.2,.38
g=''
for x in range(0,33,8):
    g+=f'\\draw[gray!45,very thin] ({x*sx},0) -- ({x*sx},{12*sy});\\draw ({x*sx},0) -- ({x*sx},-.08) node[below]{{{x}}};'
for y in range(0,13,3):
    g+=f'\\draw[gray!45,very thin] (0,{y*sy}) -- ({32*sx},{y*sy});\\draw (0,{y*sy}) -- (-.08,{y*sy}) node[left]{{{y}}};'
g+=f'\\draw[->,thick] (0,0) -- ({34*sx},0);\\draw[->,thick] (0,0) -- (0,{13.3*sy});'
g+=f'\\node at ({16*sx},-.95) {{$m(\\ce{{O2}})$ (g)}};\\node[rotate=90] at (-.95,{6*sy}) {{$m(\\mathrm{{C}})$ (g)}};'
g+=f'\\draw[very thick,vurgu] (0,0) -- ({32*sx},{12*sy});'
for o_,c_ in pts: g+=f'\\fill ({o_*sx},{c_*sy}) circle (.07);'
SK3=tk(g)
q('0003',[A('Oranı oku','Doğrunun üzerindeki bir noktadan C ve O kütleleri okunur.','16 g O₂ ile 6 g C → mC / mO = 6/16 = 3/8'),
  A('Bileşikteki payları bul','CO₂ kütlesi C ve O kütlelerinin toplamıdır.','3 + 8 = 11 birim → mC = 3k, mCO₂ = 11k'),
  A('Hesapla','88 g CO₂ için birim kütle bulunur.','k = 88 ÷ 11 = 8 → mC = 3 × 8 = 24 g')],'sabit',
 z='kolay',alt='Kütle–Kütle Grafiği',kaz='Kütle–kütle grafiğinden sabit oranı okuyarak bileşikteki element kütlesini hesaplar.',kalip='grafik',
 kart='K-KMKN2-03 (sabit oranlar, grafik) · C ve O₂ doğrusu, bileşik kütlesinden element kütlesi',sekil=SK3,
 metin='Bir öğrenci kapalı bir kapta farklı miktarlarda C katısını yeterli O₂ ile yakıyor ve her seferinde tam tepkimeye giren C ile O₂ kütlelerini kaydediyor. Tepkimede yalnız CO₂ gazı oluştuğuna göre öğrencinin elde ettiği veriler şekildeki grafiktedir.\nBuna göre aynı koşullarda 88 g CO₂ elde etmek için kaç g C yakılmalıdır?',
 dogru=24,yan=[(33,'C/O oranını (3/8) doğrudan bileşik kütlesine uygulamış.','islem'),(44,'Bileşiğin yarısının C olduğunu sanmış.','bilgi'),(64,'C yerine bileşikteki O kütlesini hesaplamış.','dikkat'),(88,'Bileşik kütlesini C kütlesi sanmış.','dikkat')],
 istenen='Yakılması gereken C kütlesi (g).',ip=['Grafikteki noktalardan C ve O kütleleri arasındaki sabit ilişkiyi bul; bileşik kütlesinin hangi kısmının C olduğunu düşün.'],
 bilgi=[B('Sabit oranlar kanunu','bir bileşikte elementlerin kütlece birleşme oranı her zaman aynıdır. Örnek: kütlece 1/3 oranında birleşen X ve Y’den oluşan bileşiğin 4 birimden 1’i X’tir')],
 puf='Bileşik kütlesi, birleşme oranındaki payların toplamına bölünerek her elementin kütlesi bulunur.')

# ================= 04 · H2 + O2 üç deney · orta · öncüllü =================
kartla('04','Sabit oran ve artan madde (üç deney)','Her deneyde gereken miktar orandan bulunur; yetmeyen madde tamamen harcanır, öteki artar.','Artan maddeyi ters söylemek; oluşan su kütlesini girenlerin toplamı sanmak.','orta','öncüllü',4,'sabit')
r=Fr(1,8); dn=[(4,16),(2,16),(3,40)]
res=[]
for h,o in dn:
    gO=h*8;
    if gO>o: kul_o=o; kul_h=Fr(o,8)
    else: kul_o=gO; kul_h=h
    res.append((kul_h,kul_o,h-kul_h,o-kul_o,kul_h+kul_o))
assert res[0]==(2,16,2,0,18) and res[1]==(2,16,0,0,18) and res[2]==(3,24,0,16,27)
q('0004',[A('Gereken miktarı bul','Her deneyde 1/8 oranına göre H₂ ile O₂ gereksinimi karşılaştırılır.','4 g H₂ için 32 g O₂ · 2 g H₂ için 16 g O₂ · 3 g H₂ için 24 g O₂'),
  A('Yetmeyeni belirle','Yetmeyen madde tamamen harcanır, öteki artar.','İlkinde 16 g O₂ biter, 2 g H₂ artar · ikincide ikisi de biter · üçüncüde H₂ biter, 16 g O₂ artar'),
  A('Su kütlelerini hesapla','Birleşen kütleler toplanır.','18 g · 18 g · 27 g'),
  A('Öncülleri değerlendir','Sonuçlar öncüllerle karşılaştırılır.','I: yanlış · II: doğru · III: yanlış')],'sabit',
 z='orta',alt='Sabit Oranlar ve Artan Madde',kaz='Sabit oranlar kanununa göre farklı deneylerde artan maddeyi ve oluşan bileşik kütlesini yorumlar.',kalip='öncüllü',
 kart='K-KMKN2-04 (sabit oranlar, üç deney) · H₂ ve O₂, artan madde yorumu',
 metin='Hidrojen ile oksijen, su oluştururken kütlece 1/8 oranında birleşir. Bir öğrenci, her biri kapalı kapta yapılan ve tepkime tamamlanana kadar sürdürülen üç deneyde aşağıdaki kütleleri kullanıyor.\n1. deney: 4 g H₂ ile 16 g O₂\n2. deney: 2 g H₂ ile 16 g O₂\n3. deney: 3 g H₂ ile 40 g O₂\nBuna göre,\nI. 1. deneyde artan madde O₂’dir.\nII. 1. ve 2. deneyde oluşan su kütleleri eşittir.\nIII. 3. deneyde 40 g O₂’nin tamamı harcanır.\nyargılarından hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Her deneyde, verilen H₂ ile tam birleşecek O₂ kütlesini hesaplayıp eldekiyle karşılaştır.'],
 bilgi=[B('Artan madde','sabit oranda birleşen iki maddeden biri yetmezse tamamen harcanır; fazla gelen madde tepkimeye girmeden kalır. Örnek: 1/4 oranında birleşen A ile B’den 2 g A, 12 g B ile karıştırılırsa 4 g B artar')],
 puf='Önce oran, sonra yetmeyen madde; bileşik kütlesi yalnız gerçekten birleşenlerin toplamıdır.',
 **onc({'I':(False,'1. deneyde 16 g O₂ yalnız 2 g H₂ ile birleşir; artan madde H₂’dir.'),'II':(True,'İkisinde de 2 g H₂ ile 16 g O₂ birleşir ve 18 g su oluşur.'),'III':(False,'3 g H₂ yalnız 24 g O₂ ile birleşir; 16 g O₂ artar.')},
   ['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']))

# ================= 05 · Fe + S, başlangıç kütlesi · orta =================
kartla('05','Sabit oranlar (ters yön)','Oluşan bileşik kütlesinden birleşen element kütlesi bulunur; artan maddeyi gerektirmeyen elementin başlangıç kütlesi birleşen kütleye eşittir.','Ürün kütlesini ya da artan maddeyi başlangıç kütlesi sanmak.','orta','hikâyeli',3,'sabit')
rFe,rS=7,4; FeS=33; Fe_b=Fr(FeS*7,11); S_b=Fr(FeS*4,11); S0=24; assert Fe_b==21 and S_b==12 and S0-S_b==12
assert Fr(FeS,11)==3 and Fr(S0*7,4)==42
q('0005',[A('Bileşikteki payları bul','Birleşen kütleler 7 ve 4 olduğuna göre bileşik 11 birimdir.','mFe : mS : mFeS = 7 : 4 : 11'),
  A('Birleşen demiri hesapla','33 g FeS kaç birimdir, bir birim kaç gramdır?','33 ÷ 11 = 3 → mFe = 3 × 7 = 21 g'),
  A('Artan maddeyi kontrol et','Birleşen kükürt kütlesi bulunur; fazlası artandır.','S: 3 × 4 = 12 g birleşir · 24 − 12 = 12 g S artar'),
  A('Başlangıç demirini yaz','Kapta yalnız kükürt arttığına göre demirin tamamı harcanmıştır.','Başlangıçtaki Fe = birleşen Fe = 21 g')],'sabit',
 z='orta',alt='Sabit Oranlar (Ters Yön)',kaz='Oluşan bileşik kütlesinden ve artan maddeden başlangıç kütlesini sabit oranlarla bulur.',kalip='hikâyeli',
 kart='K-KMKN2-05 (sabit oranlar, ters yön) · Fe ve S, FeS kütlesinden başlangıç Fe',
 metin='Demir ile kükürt, FeS bileşiğini oluştururken kütlece 7 g demir ile 4 g kükürt birleşir. Bir öğrenci, kapalı bir kapta bir miktar demir tozu ile 24 g kükürt tozunu karıştırıp ısıtıyor. Tepkime bittiğinde kapta 33 g FeS oluştuğu ve başka madde olarak yalnız kükürt kaldığı belirleniyor.\nBuna göre başlangıçta kullanılan demir tozu kaç gramdır?',
 dogru=21,yan=[(3,'33 g FeS’i 11 parçaya bölüp tek parçayı (3 g) demir kütlesi sanmış.','islem'),(12,'Birleşen (ve artan) kükürt kütlesini demir kütlesi sanmış.','dikkat'),(33,'Oluşan FeS kütlesini demir kütlesi sanmış.','dikkat'),(42,'Kükürtün tamamının harcandığını sanıp 24 g S için gereken demiri (42 g) hesaplamış.','bilgi')],
 istenen='Başlangıçtaki demir tozu kütlesi (g).',ip=['Oluşan bileşiğin kaç gramının demir olduğunu orandan bul; kapta demir kalmadığına dikkat et.'],
 bilgi=[B('Sabit oranlar kanunu','bir bileşikteki elementlerin kütlece oranı sabittir; bileşik kütlesi, birleşen elementlerin kütleleri toplamıdır. Örnek: X ile Y 2 g : 3 g birleşiyorsa 10 g bileşikte 4 g X vardır')],
 puf='Bileşik kütlesini oran paylarına bölerek birleşen miktarlar bulunur; başlangıç kütlesi için artanı da düşün.')

# ================= 06 · katlı oranlar tablosu · orta · öncüllü · tablo =================
kartla('06','Katlı oranlar (tablo, formül)','X kütlesi eşitlenir; Y kütlelerinin oranı indislerin oranını verir.','X kütlelerini eşitlemeden Y kütlelerini oranlamak.','orta','öncüllü',4,'katli')
tb=[('K',7,4),('L',14,16),('M',21,48)]
yb=[Fr(y*7,x) for _,x,y in tb]; assert yb==[4,8,16] and [v/yb[0] for v in yb]==[1,2,4]
SK6=tablo_svg(['Bileşik','X kütlesi (g)','Y kütlesi (g)'],[[a,str(x),str(y)] for a,x,y in tb])
q('0006',[A('X’i eşitle','Üç bileşikte de 7 g X olacak biçimde kütleler oranlanır.','K: 7 g X ve 4 g Y; L: 7 g X ve 8 g Y; M: 7 g X ve 16 g Y'),
  A('Y oranını yaz','Aynı X kütlesiyle birleşen Y kütleleri kıyaslanır.','4 : 8 : 16 = 1 : 2 : 4'),
  A('Formülleri bul','K, XY olduğuna göre Y atom sayısı aynı oranda artar.','K: XY · L: XY₂ · M: XY₄'),
  A('Öncülleri değerlendir','Bulunan formüller ve oranla karşılaştırılır.','I: yanlış · II: doğru · III: doğru')],'katli',
 z='orta',alt='Katlı Oranlar (Tablo)',kaz='Katlı oranlar kanununu tablo verisine uygulayarak bileşik formüllerini yorumlar.',kalip='öncüllü',
 kart='K-KMKN2-06 (katlı oranlar, tablo) · X ve Y, üç bileşik',sekil=SK6,
 metin='X ve Y elementlerinden oluşan K, L ve M bileşiklerinin her birinde, elementlerin tamamen birleştiği kütleler aşağıdaki tabloda verilmiştir. K bileşiğinin formülü XY’dir.\nBuna göre,\nI. L bileşiğinin formülü XY₃’tür.\nII. M bileşiğinin formülü XY₄’tür.\nIII. Sabit kütleli X ile birleşen Y kütleleri K : L : M = 1 : 2 : 4’tür.\nyargılarından hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Üç bileşikte X kütlesini aynı değere getirip Y kütlelerini karşılaştır.'],
 bilgi=[B('Katlı oranlar kanunu','aynı iki elementten oluşan bileşiklerde, birinin sabit kütlesiyle birleşen diğerinin kütleleri arasında basit tam sayılı oran vardır. Örnek: C ve O’dan oluşan iki bileşikte 12 g C ile 16 g ve 32 g O birleşir (1 : 2)')],
 puf='Katlı oranda önce sabit tutulan elementin kütlesini eşitle; sonra öteki elementin kütle oranı indis oranını verir.',
 **onc({'I':(False,'L’de 7 g X ile 8 g Y birleşir; Y kütlesi K’nin 2 katıdır, formül XY₂ olur.'),'II':(True,'M’de 7 g X ile 16 g Y birleşir; Y kütlesi K’nin 4 katıdır, formül XY₄ olur.'),'III':(True,'7 g X ile birleşen Y kütleleri 4 g, 8 g ve 16 g’dır; oran 1 : 2 : 4’tür.')},
   ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']))

# ================= 07 · katlı oranlar, azot oksitleri · zor =================
kartla('07','Katlı oranlar (formül bulma)','X kütleleri eşitlenir, Y kütlelerinin oranı I. bileşikteki indise uygulanır.','Y kütlelerini X’i eşitlemeden oranlamak; indisleri yalnızca X’in kat sayısıyla çarpmak.','zor','hikâyeli',4,'katli')
I_=(7,12); II_=(14,40)
yII=Fr(II_[1]*I_[0],II_[0]); assert yII==20 and yII/I_[1]==Fr(5,3) and 3*Fr(5,3)==5
assert Fr(II_[1],I_[1])*3==10 and 3*2==6 and 3+5==8 and (II_[1]-I_[1])/4==7
q('0007',[A('N kütlesini eşitle','L bileşiğinin kütleleri 2’ye bölünerek 7 g N’ye indirilir.','L: 14 g N + 40 g O → 7 g N + 20 g O'),
  A('O kütlelerini oranla','Aynı 7 g N ile birleşen oksijen kütleleri kıyaslanır.','K’de 12 g, L’de 20 g → 20/12 = 5/3'),
  A('O indisini bul','Oksijen atom sayısı da aynı oranda artar.','3 × 5/3 = 5'),
  A('Formülü yaz','Her iki molekülde de 2 azot atomu vardır.','N₂O₅')],'katli',
 z='zor',alt='Katlı Oranlar (Formül Bulma)',kaz='Katlı oranlar kanununu kullanarak ikinci bileşiğin formülünü bulur.',kalip='hikâyeli',
 kart='K-KMKN2-07 (katlı oranlar, formül) · N ve O iki bileşik, X kütlesini eşitleme',
 metin='Bir laboratuvarda azot ve oksijen elementlerinden oluşan K ve L bileşikleri, elementlerine ayrıştırılarak analiz ediliyor. K bileşiği 7 g azot ve 12 g oksijen, L bileşiği ise 14 g azot ve 40 g oksijen içeriyor. K bileşiğinin formülü N₂O₃’tür ve her iki bileşiğin molekülünde de 2 azot atomu bulunmaktadır.\nBuna göre L bileşiğinin formülü aşağıdakilerden hangisidir?',
 dogru='N₂O₅',sira=['N₂O₅','N₂O₆','N₂O₇','N₂O₈','N₂O₁₀'],
 yan=[('N₂O₆','L’de azot kütlesi 2 kat olduğu için oksijen indisini (3) 2 ile çarpmış.','islem'),('N₂O₇','Azotları eşitlemeden oksijen kütle farkını (40 − 12 = 28) alıp bir oksijene düşen 4 g’a bölmüş.','islem'),('N₂O₈','Oksijen kütlelerinin farkını (20 − 12 = 8) doğrudan indis sanmış.','islem'),('N₂O₁₀','Azotları eşitlemeden oksijen kütlelerini oranlamış (40/12 × 3 = 10).','bilgi')],
 istenen='L bileşiğinin formülü.',ip=['İki bileşikte de aynı azot kütlesi olacak biçimde oksijen kütlelerini karşılaştır.'],
 bilgi=[B('Katlı oranlar kanunu','aynı elementlerden oluşan farklı bileşiklerde, birinin sabit kütlesiyle birleşen diğerinin kütleleri basit tam sayılı oran verir. Örnek: bir bileşikte 2 g X ile 3 g Y, ötekinde 2 g X ile 9 g Y birleşiyorsa Y kütleleri oranı 1 : 3’tür')],
 puf='Önce sabit elementin kütlesini eşitle; öteki elementin kütle oranı o elementin indis oranıdır.')

# ================= 08 · Gay-Lussac, sınırlayıcı gaz · orta · şekil =================
kartla('08','Birleşen hacim oranları (sınırlayıcı gaz)','Aynı koşullarda gaz hacimleri katsayılarla orantılıdır; sınırlayıcı gaz bulunup ürün ve artan gaz hacmi hesaplanır.','Hacmin korunduğunu sanmak; artan gazı saymamak.','orta','şekilli',4,'hacim')
VN,VH=8,18; usedN=Fr(VH,3); NH3=2*usedN; art=VN-usedN; tot=NH3+art
assert usedN==6 and NH3==12 and art==2 and tot==14 and VN+VH==26 and VH+art==20 and VN+(VH-VN)==18 and NH3==12
cs=.15
g=f'\\draw[thick,fill=vurgu!15] (0,0) rectangle (1,{VN*cs});\\node[above] at (.5,{VN*cs}) {{\\ce{{N2}}(g)}};\\node[below] at (.5,0) {{{VN} L}};'
g+=f'\\draw[thick,fill=vurgu!15] (2,0) rectangle (3,{VH*cs});\\node[above] at (2.5,{VH*cs}) {{\\ce{{H2}}(g)}};\\node[below] at (2.5,0) {{{VH} L}};'
g+=f'\\draw[thick,dashed] (5.2,0) rectangle (6.8,{VH*cs});\\node[align=center] at (6,{VH*cs/2}) {{Tepkime\\\\kabı}};'
g+=f'\\draw[-{{Stealth[length=2.2mm]}},thick] (3.4,{VH*cs/2}) -- (4.8,{VH*cs/2});\\node at (1.5,{VN*cs/2}) {{\\large +}};'
g+=f'\\node at (3.4,-1.0) {{Hacimler aynı sıcaklık ve basınçta ölçülmüştür.}};'
SK8=tk(g)
q('0008',[A('Hacim oranını yaz','Aynı koşullarda gaz hacimleri katsayılarla orantılıdır.','N₂ : H₂ : NH₃ = 1 : 3 : 2'),
  A('Yetmeyen gazı bul','8 L N₂ için 24 L H₂ gerekir; yalnız 18 L H₂ var.','H₂ biter → 18 ÷ 3 = 6 L N₂ harcanır'),
  A('Ürün ve artanı hesapla','Oluşan NH₃ ve artan N₂ hacmi bulunur.','NH₃ = 2 × 6 = 12 L · artan N₂ = 8 − 6 = 2 L'),
  A('Toplam hacmi bul','Kapta artan N₂ ve oluşan NH₃ vardır.','12 + 2 = 14 L')],'hacim',
 z='orta',alt='Gay-Lussac (Sınırlayıcı Gaz)',kaz='Birleşen hacim oranlarını kullanarak tepkime sonunda kaptaki toplam gaz hacmini bulur.',kalip='şekilli',
 kart='K-KMKN2-08 (birleşen hacim oranları) · N₂ + 3H₂ → 2NH₃, sınırlayıcı gaz',sekil=SK8,
 metin='Aynı sıcaklık ve basınçta, şekilde hacimleri verilen N₂ ve H₂ gazları boş bir tepkime kabına aktarılıyor ve N₂(g) + 3H₂(g) → 2NH₃(g) tepkimesi, girenlerden biri tükenene kadar sürüyor. Daha sonra kap, başlangıçtaki sıcaklık ve basınca getiriliyor.\nBuna göre kapta aynı koşullarda ölçülen gazların toplam hacmi kaç L’dir?',
 dogru=14,yan=[(12,'Yalnız oluşan NH₃ hacmini yazmış; artan N₂’yi hesaba katmamış.','dikkat'),(18,'Katsayıları 1 : 1 : 1 sanıp 8 L NH₃ ile artan 10 L H₂’yi toplamış.','bilgi'),(20,'H₂ hacmi kadar NH₃ oluştuğunu sanıp (18 L) artan N₂’yi (2 L) eklemiş.','bilgi'),(26,'Gaz hacminin korunduğunu sanıp başlangıç hacimlerini toplamış (8 + 18).','bilgi')],
 istenen='Tepkime sonunda gazların toplam hacmi (L).',ip=['Katsayı oranına göre H₂ ile N₂’den hangisinin önce biteceğini belirle.'],
 bilgi=[B('Birleşen hacim oranları','sabit sıcaklık ve basınçta gazlar, hacimleri arasında basit tam sayılı oranla tepkimeye girer; bu oran denklemdeki katsayı oranıdır. Örnek: A₂ + 2B₂ → 2AB₂ tepkimesinde 3 L A₂ ile 6 L B₂ birleşir')],
 puf='Gazlarda katsayı oranı hacim oranıdır; toplam hacim korunmaz, ürün ve artan gaz ayrı ayrı hesaplanır.')

# ================= 09 · Avogadro hipotezi · kolay · öncüllü · şekil =================
kartla('09','Avogadro hipotezi','Aynı sıcaklık ve basınçta eşit hacimli gazlar eşit sayıda tanecik içerir; atom sayısı ve kütle molekül yapısına ve cinsine bağlıdır.','Eşit sayıda taneciği eşit atom ya da eşit kütle sanmak.','kolay','öncüllü',3,'hacim')
atom={'He':1,'H₂':2,'CO₂':3}; assert len(set(atom.values()))==3
def kutu(x,ad,mol,etiket):
    s=f'\\draw[thick] ({x},0) rectangle ({x+2},1.7);\\node at ({x+1},2.05) {{\\textbf{{{ad}}}}};\\node at ({x+1},-.4) {{{etiket}}};'
    if mol=='He': s+=f'\\draw[thick,fill=vurgu!25] ({x+1},.85) circle (.2);'
    if mol=='H2': s+=f'\\draw[thick,fill=white] ({x+.84},.85) circle (.16);\\draw[thick,fill=white] ({x+1.16},.85) circle (.16);'
    if mol=='CO2': s+=f'\\draw[thick,fill=white] ({x+.64},.85) circle (.17);\\draw[thick,fill=gray!40] ({x+1},.85) circle (.2);\\draw[thick,fill=white] ({x+1.36},.85) circle (.17);'
    return s
SK9=tk(kutu(0,'K','He','\\ce{He}(g)')+kutu(2.7,'L','H2','\\ce{H2}(g)')+kutu(5.4,'M','CO2','\\ce{CO2}(g)')+'\\node at (3.7,-1.05) {Her kapta bir gaz molekülünün modeli gösterilmiştir.};')
q('0009',[A('Hipotezi hatırla','Eşit hacim, aynı sıcaklık ve basınç: tanecik sayısı eşittir.','n(K) = n(L) = n(M) (tanecik sayısı)'),
  A('Atom sayılarını karşılaştır','Modelde He tek atomlu, H₂ iki atomlu, CO₂ üç atomludur.','Atom sayıları 1 : 2 : 3 oranındadır'),
  A('Kütleleri karşılaştır','Farklı gazların taneciklerinin kütleleri farklıdır.','He, H₂ ve CO₂’nin tanecik kütleleri farklı → kaplardaki kütleler farklı'),
  A('Öncülleri değerlendir','Bulgular öncüllerle eşleştirilir.','I: doğru · II: yanlış · III: yanlış')],'hacim',
 z='kolay',alt='Avogadro Hipotezi',kaz='Avogadro hipotezini kullanarak eşit hacimli gaz kaplarındaki tanecik, atom ve kütle bilgilerini yorumlar.',kalip='öncüllü',
 kart='K-KMKN2-09 (Avogadro hipotezi, nitel) · He, H₂, CO₂ eşit hacimli kaplar',sekil=SK9,
 metin='Aynı sıcaklık ve basınçta, hacimleri birbirine eşit olan K, L ve M kaplarında sırasıyla He, H₂ ve CO₂ gazları bulunmaktadır. Her gazın molekül modeli şekilde gösterilmiştir.\nBuna göre,\nI. Üç kapta da eşit sayıda gaz taneciği bulunur.\nII. Kaplardaki toplam atom sayıları birbirine eşittir.\nIII. Kaplardaki gazların kütleleri birbirine eşittir.\nyargılarından hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Aynı koşullarda hacim ile tanecik sayısı arasındaki ilişkiyi, sonra molekül modellerini düşün.'],
 bilgi=[B('Avogadro hipotezi','aynı sıcaklık ve basınçtaki eşit hacimli gazlar eşit sayıda tanecik (atom ya da molekül) içerir. Örnek: bir kapta 5 molekül varsa aynı koşullarda eşit hacimli başka bir gaz kabında da 5 molekül vardır')],
 puf='Eşit hacim, eşit tanecik sayısıdır; atom sayısını molekül formülü, kütleyi taneciğin cinsi belirler.',
 **onc({'I':(True,'Aynı sıcaklık ve basınçta eşit hacimli gazlarda tanecik sayısı eşittir.'),'II':(False,'Her molekülde atom sayısı farklıdır (He 1, H₂ 2, CO₂ 3), toplam atom sayıları 1 : 2 : 3 oranındadır.'),'III':(False,'Tanecik sayısı eşit olsa da farklı gazların taneciklerinin kütleleri farklıdır.')},
   ['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']))

# ================= 10 · tepkime türleri tablosu · orta · olumsuz kök · tablo =================
kartla('10','Tepkime türlerini ayırt etme','Girenler ve ürünlerin sayısı ve niteliği tepkime türünü belirler: sentez, analiz, yanma, asit–baz, çözünme–çökelme.','Tek maddeden çok madde oluşan tepkimeyi sentez sanmak.','orta','tablo',3,'tur')
satir=[('K','CH₄ + 2O₂ → CO₂ + 2H₂O','Yanma',True),('L','2Na + Cl₂ → 2NaCl','Sentez',True),('M','CaCO₃ → CaO + CO₂','Analiz',True),('N','AgNO₃ + NaCl → AgCl + NaNO₃','Çözünme–çökelme',True),('P','HNO₃ + KOH → KNO₃ + H₂O','Çözünme–çökelme',False)]
assert [s[3] for s in satir].count(False)==1
SK10=tablo_svg(['Satır','Tepkime','Öğrencinin yazdığı tür'],[[a,b,c] for a,b,c,_ in satir])
nedenT={'K':'metan O₂ ile tepkimeye girip CO₂ ve H₂O verir; bu bir yanma tepkimesidir.','L':'iki elementten tek bileşik oluşur; bu bir sentez tepkimesidir.','M':'tek maddeden iki madde oluşur; bu bir analiz tepkimesidir.','N':'iki çözeltiden suda az çözünen AgCl katısı çöker; bu bir çökelme tepkimesidir.'}
q('0010',[A('Türleri hatırla','Sentez: iki ya da daha çok maddeden tek madde. Analiz: tek maddeden birden çok madde.','Yanma · sentez · analiz · asit–baz · çökelme'),
  A('Satırları sınıflandır','Her tepkimeyi girenlerine ve ürünlerine bakarak adlandır.','K: yanma · L: sentez · M: analiz · N: çökelme · P: asit–baz'),
  A('Yanlış eşleşmeyi bul','Öğrencinin yazdığı tür ile bulunanı karşılaştır.','P’de yazılan tür “çözünme–çökelme”, doğrusu “asit–baz”')],'tur',
 z='orta',alt='Tepkime Türleri',kaz='Kimyasal tepkimeleri yanma, sentez, analiz, asit–baz ve çözünme–çökelme türlerine göre sınıflandırır.',kalip='tablo',
 kart='K-KMKN2-10 (tepkime türleri, tablo) · beş denklem, yanlış tür',sekil=SK10,
 metin='Bir öğrenci, kimyasal tepkimeleri yanma, sentez, analiz, asit–baz ve çözünme–çökelme türlerinden birine yerleştirerek aşağıdaki tabloyu hazırlamıştır. Öğretmeni, satırlardan yalnızca birinde tepkime türünün hatalı yazıldığını söylemiştir.\nBuna göre hangi satırda yazılan tür yanlıştır?',
 dogru='P',sira=['K','L','M','N','P'],
 yan=[(a,f'{a} satırında doğru yazılmış türü hatalı sanmış; oysa {nedenT[a]}','bilgi') for a in 'KLMN'],
 istenen='Türü yanlış yazılmış satır.',ip=['Her tepkimede giren madde sayısını ve ürün sayısını karşılaştır.'],
 bilgi=[B('Tepkime türleri','sentez A + B → AB, analiz AB → A + B, yanma bir maddenin O₂ ile tepkimesi, asit–baz asit + baz → tuz + su, çökelme çözeltilerden katı oluşmasıdır. Örnek: H₂ + Cl₂ → 2HCl sentez tepkimesidir')],
 puf='Tek maddeden çok madde oluşuyorsa analiz, çok maddeden tek madde oluşuyorsa sentezdir.')

# ================= 11 · tanecik modelinden denklem · kolay · şekil =================
kartla('11','Tanecik modelinden denklem yazma','Şekildeki tanecikler sayılır, atom sayıları eşitlenir ve katsayılar en küçük tam sayılara indirilir.','Şekildeki tanecik sayısını doğrudan katsayı yapmak; ürüne katsayı yazmayı unutmak.','kolay','şekilli',4,'denk')
nN2,nH2,nNH3=2,6,4; assert 2*nN2==nNH3 and 2*nH2==3*nNH3
def N2(x,y): return f'\\draw[thick,fill=vurgu!35] ({x-.2},{y}) circle (.2);\\draw[thick,fill=vurgu!35] ({x+.2},{y}) circle (.2);'
def H2(x,y): return f'\\draw[thick,fill=white] ({x-.12},{y}) circle (.12);\\draw[thick,fill=white] ({x+.12},{y}) circle (.12);'
import math
def NH3_(x,y):
    s=f'\\draw[thick,fill=vurgu!35] ({x},{y}) circle (.2);'
    for a in (90,210,330): s+=f'\\draw[thick,fill=white] ({x+.33*math.cos(math.radians(a)):.3f},{y+.33*math.sin(math.radians(a)):.3f}) circle (.12);'
    return s
g='\\draw[thick] (0,-.1) rectangle (3.4,2.9);\\draw[thick] (5,-.1) rectangle (8.4,2.9);'
slots=[(.9,2.35),(2.5,2.35)]+[(cx,cy) for cy in (1.65,1.0,.35) for cx in (.9,2.5)]
for i,(cx,cy) in enumerate(slots): g+=N2(cx,cy) if i<nN2 else H2(cx,cy)
assert len(slots)==nN2+nH2
for cx,cy in [(5.9,1.9),(7.5,1.9),(5.9,.6),(7.5,.6)]: g+=NH3_(cx,cy)
g+='\\draw[-{Stealth[length=2.2mm]},thick] (3.6,1.4) -- (4.8,1.4);\\node at (1.7,-.5) {Tepkimeden önce};\\node at (6.7,-.5) {Tepkimeden sonra};'
g+='\\draw[thick,fill=vurgu!35] (.35,-1.15) circle (.15);\\node[right] at (.55,-1.15) {N atomu};\\draw[thick,fill=white] (2.6,-1.15) circle (.11);\\node[right] at (2.8,-1.15) {H atomu};'
SK11=tk(g)
q('0011',[A('Tanecikleri say','Şekildeki giren ve ürün taneciklerinin sayısı okunur.','Giren: 2 N₂ ve 6 H₂ · ürün: 4 NH₃'),
  A('Atom sayılarını kontrol et','Her iki tarafta aynı atom türü ve sayısı olmalıdır.','N: 4 = 4 · H: 12 = 12'),
  A('Katsayıları sadeleştir','Katsayılar en küçük tam sayılara indirilir.','2 : 6 : 4 → 1 : 3 : 2'),
  A('Denklemi yaz','Katsayı 1 yazılmaz.','N₂ + 3H₂ → 2NH₃')],'denk',
 z='kolay',alt='Tanecik Modelinden Denklem',kaz='Tanecik modelinden tepkime denklemini yazıp en küçük tam sayılarla denkleştirir.',kalip='şekilli',
 kart='K-KMKN2-11 (tanecik modeli, denklem) · N₂ + H₂ → NH₃ modeli',sekil=SK11,
 metin='Bir öğretmen, azot ve hidrojen gazlarının tepkimesini kapalı bir kapta modelleyerek öğrencilerine şekildeki tanecik çizimini veriyor. Tepkimeden önce ve sonra kapta başka tanecik bulunmuyor, tepkime girenlerden biri artmadan tamamlanıyor.\nBuna göre bu tepkimenin en küçük tam sayılarla denkleştirilmiş denklemi aşağıdakilerden hangisidir?',
 dogru='N₂ + 3H₂ → 2NH₃',sira=['N₂ + H₂ → NH₃','N₂ + 3H₂ → NH₃','3N₂ + H₂ → 2NH₃','2N₂ + 6H₂ → 4NH₃','N₂ + 3H₂ → 2NH₃'],
 yan=[('N₂ + H₂ → NH₃','Katsayıları yazmadan yalnız giren ve ürünlerin türünü yazmış; atom sayıları eşit değil.','bilgi'),('N₂ + 3H₂ → NH₃','Ürüne katsayı yazmamış; N atomu solda 2, sağda 1 kalmış.','dikkat'),('3N₂ + H₂ → 2NH₃','Katsayıları iki gaz arasında karıştırmış; H atomu 2, N atomu 6 olmuş.','dikkat'),('2N₂ + 6H₂ → 4NH₃','Şekildeki tanecik sayılarını doğrudan katsayı yapmış; en küçük tam sayılara indirmemiş.','dikkat')],
 istenen='Denkleştirilmiş tepkime denklemi.',ip=['Şekildeki taneciklerden atom sayılarını say ve katsayıları en küçük oranlara indir.'],
 bilgi=[B('Denklem denkleştirme','tepkimenin iki yanında her atomun sayısı eşit olacak biçimde formüllerin önüne katsayı yazılır; katsayılar en küçük tam sayılar olur. Örnek: 2H₂ + O₂ → 2H₂O tepkimesinde 4 H ve 2 O atomu iki yanda da vardır')],
 puf='Tanecik modelinden denklem yazarken önce atomları say, sonra katsayıları ortak bölenle sadeleştir.')

# ================= 12 · katsayı–alt simge · orta · öncüllü · olumsuz kök =================
kartla('12','Katsayı ve alt simge farkı','Katsayı molekül (formül birimi) sayısını, alt simge bir molekülde atom sayısını gösterir; denkleştirmede alt simge değiştirilmez.','Katsayıyı atom sayısı sanmak; alt simgeyi değiştirerek denkleştirmek.','orta','öncüllü',4,'denk')
q('0012',[A('Katsayı ile alt simgeyi ayır','Katsayı molekül sayısı, alt simge atom sayısıdır.','2H₂O: 2 molekül su · H₂O: bir molekülde 2 H ve 1 O'),
  A('I’i incele','Katsayı atom sayısını değil molekül sayısını gösterir.','2H₂O’nun başındaki 2 → 2 su molekülü'),
  A('II’yi incele','Alt simge değişirse madde değişir.','H₂O₂ (hidrojen peroksit) ≠ H₂O (su)'),
  A('III’ü incele','Atomlar korunur, moleküller korunmak zorunda değildir.','Girenler: 3 molekül, ürün: 2 molekül · 4 H ve 2 O iki yanda da var')],'denk',
 z='orta',alt='Katsayı ve Alt Simge Farkı',kaz='Tepkime denklemlerinde katsayı ile alt simgenin anlamını ayırt eder.',kalip='öncüllü',
 kart='K-KMKN2-12 (katsayı–alt simge) · 2H₂ + O₂ → 2H₂O notları',
 metin='Bir öğrenci, hidrojenin yanması tepkimesi olan 2H₂ + O₂ → 2H₂O için ders defterine aşağıdaki notları yazmıştır.\nI. 2H₂O ifadesinin başındaki 2, bir su molekülündeki hidrojen atomu sayısını gösterir.\nII. Denklemi denkleştirmek için H₂O yerine H₂O₂ yazılarak oksijen atomu sayısı artırılabilir.\nIII. Tepkimede atom türü ve sayısı korunur, molekül sayısının korunması gerekmez.\nÖğretmeni, bu notlardan bazılarının yanlış olduğunu söylemiştir. Buna göre hangileri yanlıştır?',
 istenen='Yanlış olan notlar.',ip=['Katsayının ve alt simgenin ayrı ayrı neyi gösterdiğini yaz; sonra her notu bununla karşılaştır.'],
 bilgi=[B('Katsayı ve alt simge','katsayı bir maddeden kaç molekül ya da formül birimi olduğunu, alt simge bir molekülde ya da formül biriminde kaç atom olduğunu gösterir. Örnek: 4NH₃ ifadesinde 4 molekül NH₃ vardır, her molekülde 1 azot ve 3 hidrojen atomu bulunur')],
 puf='Denkleştirirken yalnız katsayı değiştirilir; alt simge değişirse başka bir madde yazılmış olur.',
 **onc({'I':(False,'2H₂O’nun başındaki 2 katsayıdır, 2 su molekülü demektir; bir molekülde hidrojen atomu sayısını alt simge (2) gösterir.'),'II':(False,'Alt simge değişince madde değişir; H₂O₂ su değil hidrojen peroksittir.'),'III':(True,'Denklemde girenler 3, ürün 2 moleküldür; yine de her iki yanda 4 H ve 2 O atomu bulunur.')},
   ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],dogru_ara=False))

# ================= 13 · bütan yanması denkleştirme · orta =================
kartla('13','Yanma denkleminin denkleştirilmesi','C, H, O sırasıyla atomlar eşitlenir; kesirli katsayı tüm denklemi 2 ile çarparak tam sayıya çevrilir.','O₂ katsayısını yalnız CO₂’deki oksijene göre bulmak; en küçük tam sayıya inmemek.','orta','hikâyeli',4,'denk')
def top(k): return sum(k)
assert top([2,13,8,10])==33
# atom kontrolü: 2C4H10 + 13O2 -> 8CO2 + 10H2O
assert 2*4==8 and 2*10==2*10 and 13*2==8*2+10
assert 13+10==23 and 4+5==9 and 13+5==18 and 13+8==21 and 26+20==46
q('0013',[A('C atomlarını eşitle','Bütandaki 4 C atomu 4 CO₂ verir.','C₄H₁₀ + O₂ → 4CO₂ + H₂O'),
  A('H atomlarını eşitle','10 H atomu için 5 H₂O gerekir.','C₄H₁₀ + O₂ → 4CO₂ + 5H₂O'),
  A('O atomlarını eşitle','Sağda 8 + 5 = 13 O atomu var; O₂ için 6,5 gerekir, tam sayı için tüm katsayılar 2 ile çarpılır.','2C₄H₁₀ + 13O₂ → 8CO₂ + 10H₂O'),
  A('İstenen katsayıları topla','O₂ ve H₂O katsayıları toplanır.','13 + 10 = 23')],'denk',
 z='orta',alt='Yanma Denkleminin Denkleştirilmesi',kaz='Bir yanma tepkimesinin denklemini en küçük tam sayılarla denkleştirir.',kalip='hikâyeli',
 kart='K-KMKN2-13 (yanma, denkleştirme) · C₄H₁₀ + O₂, O₂ ve H₂O katsayıları',
 metin='Kamp tüplerinde yakıt olarak kullanılan bütan gazı, yeterli miktarda oksijenle tam olarak yandığında karbondioksit ve su buharı oluşturur. Bu tepkimenin denkleştirilmemiş hâli C₄H₁₀ + O₂ → CO₂ + H₂O biçiminde gösterilmektedir.\nBuna göre denklem en küçük tam sayılarla denkleştirildiğinde O₂ ile H₂O’nun katsayıları toplamı kaç olur?',
 dogru=23,yan=[(9,'O₂ katsayısını yalnız CO₂’deki oksijen atomlarına göre (4) belirleyip H₂O için 5 almış: 4 + 5.','islem'),(18,'H₂O katsayısını bütanın 1 molekülüne göre (5) bırakıp O₂’yi 13 almış: 13 + 5.','islem'),(21,'H₂O yerine CO₂’nin katsayısını (8) almış: 13 + 8.','dikkat'),(46,'Katsayıları 2 ile çarpmış; en küçük tam sayılara inmemiş: 26 + 20.','dikkat')],
 istenen='O₂ ile H₂O katsayılarının toplamı.',ip=['Atomları sırayla eşitle; oksijeni en sona bırak.'],
 bilgi=[B('Yanma denklemini denkleştirme','hidrokarbon yanmasında önce C, sonra H, en son O atomları eşitlenir; O₂ katsayısı kesir çıkarsa bütün katsayılar aynı sayıyla çarpılır. Örnek: C₂H₂ yanmasında 2C₂H₂ + 5O₂ → 4CO₂ + 2H₂O')],
 puf='Yanma denkleminde oksijeni en sona bırak; O₂ katsayısı kesirliyse bütün katsayıları 2 ile çarp.')

# ================= 14 · propan yanması, hacim · zor =================
kartla('14','Gay-Lussac ve denklem (propan yanması)','Gaz hacimleri katsayılarla orantılıdır; sınırlayıcı gaz bulunur, ürünler ve artan gaz toplanır.','Artan gazı ya da su buharını saymamak; O₂’nin tamamen bittiğini sanmak.','orta','hikâyeli',5,'hacim')
Vp,Vo=6,40; ok_=Fr(Vp*5); assert ok_==30<Vo
co2=3*Vp; h2o=4*Vp; artO=Vo-30; assert (co2,h2o,artO)==(18,24,10) and co2+h2o+artO==52
assert artO+co2==28 and co2+h2o==42 and Vp+Vo==46 and 3*Fr(Vo,5)+4*Fr(Vo,5)==56
q('0014',[A('Hacim oranını yaz','Aynı koşullarda gaz hacimleri katsayılarla orantılıdır.','C₃H₈ : O₂ : CO₂ : H₂O = 1 : 5 : 3 : 4'),
  A('Yetmeyen gazı bul','6 L propan için 30 L O₂ gerekir; 40 L O₂ var.','Propan biter, 40 − 30 = 10 L O₂ artar'),
  A('Ürün hacimlerini hesapla','Propanın 6 L’sine göre ürünler bulunur.','CO₂ = 3 × 6 = 18 L · H₂O(g) = 4 × 6 = 24 L'),
  A('Toplam hacmi bul','Artan O₂ ile iki ürün toplanır.','10 + 18 + 24 = 52 L')],'hacim',
 z='orta',alt='Gay-Lussac ve Denklem',kaz='Yanma denklemi ve gaz hacim oranlarını birlikte kullanarak tepkime sonundaki gaz hacmini bulur.',kalip='hikâyeli',
 kart='K-KMKN2-14 (Gay-Lussac + denklem) · propan yanması, artan O₂ ve su buharı',
 metin='Aynı sıcaklık ve basınçta ölçülen 6 L propan (C₃H₈) gazı ile 40 L O₂ gazı kapalı bir kapta yakılıyor. Yanma, C₃H₈(g) + 5O₂(g) → 3CO₂(g) + 4H₂O(g) denklemine göre girenlerden biri tükenene kadar sürüyor. Hacimler, bütün maddelerin gaz hâlinde olduğu aynı sıcaklık ve basınçta ölçülmüştür.\nBuna göre tepkime sonunda kapta bulunan gazların toplam hacmi kaç L’dir?',
 dogru=52,yan=[(28,'Oluşan H₂O buharının hacmini hesaba katmamış (10 + 18).','dikkat'),(42,'Artan O₂’yi unutmuş (18 + 24).','dikkat'),(46,'Başlangıç hacimlerini toplayıp (6 + 40) gaz hacminin korunduğunu sanmış.','bilgi'),(56,'O₂’nin tamamının harcandığını sanıp ürün hacimlerini 40 L’ye göre hesaplamış (24 + 32).','bilgi')],
 istenen='Tepkime sonunda gazların toplam hacmi (L).',ip=['Katsayı oranına göre propan ve O₂’den hangisinin önce biteceğini belirle.'],
 bilgi=[B('Sınırlayıcı gaz','denklemdeki katsayı oranına göre önce biten gaz ürün miktarını belirler; öteki gaz artar. Örnek: 2A + B → 2C tepkimesinde 4 L A ile 3 L B girerse B 1 L artar')],
 puf='Gaz tepkimelerinde önce oran, sonra sınırlayıcı gaz; sonunda artan gaz ve bütün gaz ürünleri topla.')

# ================= 15 · tepkime türleri, öncüllü · orta =================
kartla('15','Tepkime türleri (öncüllü)','Bir tepkime birden çok türe girebilir; ayrışma analiz, çözeltilerden katı oluşması çökelme, element + O₂ yanma ve sentezdir.','Mg + O₂ tepkimesini yalnız yanma ya da yalnız sentez saymak.','orta','öncüllü',4,'tur')
q('0015',[A('1. tepkimeyi sınıflandır','Tek maddeden iki madde oluşuyor.','KClO₃ → KCl + O₂ : analiz'),
  A('2. tepkimeyi sınıflandır','İki çözeltiden suda az çözünen katı çöküyor.','BaCl₂ + Na₂SO₄ : çözünme–çökelme'),
  A('3. tepkimeyi sınıflandır','İki elementten tek bileşik oluşuyor ve O₂ ile birleşme var.','Mg + O₂ → MgO : sentez ve yanma'),
  A('Sonuç','Üç öncül de tür tanımlarına uyar.','I, II ve III doğru')],'tur',
 z='orta',alt='Tepkime Türleri',kaz='Verilen tepkime denklemlerinin türlerini yanma, sentez, analiz ve çökelme olarak belirler.',kalip='öncüllü',
 kart='K-KMKN2-15 (tepkime türleri, öncüllü) · KClO₃ ayrışması, BaSO₄ çökelmesi, Mg yanması',
 metin='Bir kimya öğretmeni tahtaya aşağıdaki tepkimeleri yazarak öğrencilerinden türlerini belirlemelerini istiyor.\n1. tepkime: 2KClO₃ → 2KCl + 3O₂\n2. tepkime: BaCl₂ + Na₂SO₄ → 2NaCl + BaSO₄ (BaSO₄ suda çok az çözünerek katı hâlde çöker.)\n3. tepkime: 2Mg + O₂ → 2MgO\nBuna göre,\nI. 1. tepkime bir analiz tepkimesidir.\nII. 2. tepkime bir çözünme–çökelme tepkimesidir.\nIII. 3. tepkime hem sentez hem yanma tepkimesidir.\nyargılarından hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Her tepkimede giren ve ürün madde sayısına ve tepkimenin özelliğine bak.'],
 bilgi=[B('Tepkime türleri','analiz tek maddenin parçalanması, sentez maddelerin birleşmesi, yanma O₂ ile tepkime, çökelme çözeltilerden katı oluşmasıdır; bir tepkime birden çok türe girebilir. Örnek: C + O₂ → CO₂ tepkimesi yanma tepkimesidir')],
 puf='Her tepkimeyi tür tanımlarıyla tek tek karşılaştır; girenlere ve ürünlere bak.',
 **onc({'I':(True,'Tek madde (KClO₃) iki maddeye ayrışıyor; analiz tepkimesidir.'),'II':(True,'İki çözeltiden suda az çözünen BaSO₄ katısı çöküyor; çökelme tepkimesidir.'),'III':(True,'İki elementten tek bileşik oluşuyor (sentez) ve Mg O₂ ile yanıyor (yanma).')},
   ['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']))

# ================= 16 · kütle–zaman grafiği, iki deney · zor · grafik =================
kartla('16','Kütle–zaman grafiğinden oran ve ürün','Grafikte azalan kütlelerden birleşen miktarlar ve oran bulunur; yeni deneyde sınırlayıcı belirlenir.','Girenlerin toplamını ürün sanmak; sınırlayıcıyı bulmadan hesaplamak.','zor','grafik',4,'sabit')
A0,B0,Af,Bf=15,35,0,15; ukA=A0-Af; ukB=B0-Bf; assert (ukA,ukB)==(15,20) and Fr(ukA,ukB)==Fr(3,4)
A2,B2=30,50; needB=Fr(A2*4,3); assert needB==40<B2 and A2+needB==70 and A2+B2==80 and B2+Fr(B2*3,4)==Fr(175,2) and ukA+ukB==35
sx,sy=.9,.12
g=''
for t in range(0,6): g+=f'\\draw[gray!45,very thin] ({t*sx},0) -- ({t*sx},{35*sy});\\draw ({t*sx},0) -- ({t*sx},-.08) node[below]{{{t}}};'
for y in range(0,36,5): g+=f'\\draw[gray!45,very thin] (0,{y*sy}) -- ({5*sx},{y*sy});\\draw (0,{y*sy}) -- (-.08,{y*sy}) node[left]{{{y}}};'
g+=f'\\draw[->,thick] (0,0) -- ({5.4*sx},0);\\draw[->,thick] (0,0) -- (0,{37.5*sy});'
g+=f'\\node at ({2.5*sx},-.95) {{Zaman (dk)}};\\node[rotate=90] at (-1.0,{17.5*sy}) {{Kütle (g)}};'
g+=f'\\draw[very thick,vurgu] (0,{A0*sy}) -- ({3*sx},0) -- ({5*sx},0);\\draw[very thick] (0,{B0*sy}) -- ({3*sx},{Bf*sy}) -- ({5*sx},{Bf*sy});'
g+=f'\\node[above] at ({4.5*sx},{Bf*sy}) {{\\textbf{{B}}}};\\node[above] at ({4.5*sx},0) {{\\textbf{{A}}}};'
for (t,y) in [(0,A0),(0,B0),(3,0),(3,Bf)]: g+=f'\\fill ({t*sx},{y*sy}) circle (.06);'
SK16=tk(g)
q('0016',[A('Birleşen miktarları oku','A tamamen bitmiş, B ise 35’ten 15’e inmiştir.','A: 15 g; B: 35 − 15 = 20 g'),
  A('Oranı yaz','Birleşen kütlelerin oranı sabittir.','mA / mB = 15/20 = 3/4'),
  A('2. deneyde sınırlayıcıyı bul','30 g A ile birleşecek B kütlesi hesaplanır.','30 × 4 ÷ 3 = 40 g B gerekir · 50 g B var'),
  A('C kütlesini hesapla','A tamamen biter, 10 g B artar; birleşenler toplanır.','30 + 40 = 70 g')],'sabit',
 z='zor',alt='Kütle–Zaman Grafiği ve Sabit Oran',kaz='Kütle–zaman grafiğinden birleşme oranını bulup yeni deneyde oluşan bileşik kütlesini hesaplar.',kalip='grafik',
 kart='K-KMKN2-16 (sabit oranlar, kütle–zaman grafiği) · A ve B, ikinci deneyde sınırlayıcı',sekil=SK16,
 metin='A ve B elementlerinden yalnız C bileşiği oluşmaktadır. Kapalı bir kapta yapılan birinci deneyde A ve B’nin kütlelerinin zamanla değişimi şekildeki grafikte gösterilmiştir; tepkime 3. dakikada sona ermiş ve ortama madde çıkmamıştır.\nAynı koşullarda yapılan ikinci deneyde 30 g A ile 50 g B tepkimeye sokuluyor.\nBuna göre ikinci deneyde en fazla kaç g C oluşur?',
 dogru=70,yan=[(35,'Birinci deneyde oluşan C kütlesini (15 + 20) ikinci deneyin sonucu sanmış.','dikkat'),(40,'Birleşen B kütlesini bileşik kütlesi sanmış.','dikkat'),(80,'Girenlerin toplamını (30 + 50) almış; artan B’yi görmemiş.','bilgi'),(Fr(175,2),'B’nin tamamının harcandığını sanıp A’yı 37,5 g bulmuş (50 + 37,5).','bilgi')],
 istenen='İkinci deneyde oluşan C kütlesi (g).',ip=['Birinci deneyde her elementten ne kadarının birleştiğini grafikten bul; ikinci deneyde hangisinin yeteceğine bak.'],
 bilgi=[B('Sınırlayıcı madde','sabit oranda birleşen iki maddeden oranla yetmeyen tamamen harcanır, ürün kütlesini o belirler. Örnek: 1/2 oranında birleşen X ve Y’den 3 g X, 9 g Y karıştırılırsa 3 g Y artar')],
 puf='Grafikte azalan miktar birleşen miktardır; artan değil, azalan kısım orana girer.')

# ================= 17 · Gay-Lussac + Avogadro ile formül · orta · öncüllü =================
kartla('17','Hacim oranlarından formül bulma (öncüllü)','Aynı koşullarda gaz hacim oranı katsayı oranıdır; atom korunumundan ürünün formülü bulunur, hacim ve molekül sayısı yorumlanır.','Gaz hacminin tepkimede korunduğunu sanmak; formülü hacim oranından atom sayısına çevirememek.','orta','öncüllü',4,'hacim')
VX,VY,VZ=4,6,4; assert 2*VX==2*VZ and 2*VY==3*VZ  # 4X2 + 6Y2 -> 4 X2Y3
assert VZ<VX+VY and VZ==VX
q('0017',[A('Hacim oranını yaz','Aynı koşullarda hacim oranı molekül sayısı oranıdır.','X₂ : Y₂ : Z = 4 : 6 : 4 = 2 : 3 : 2'),
  A('Z’nin formülünü bul','2X₂ + 3Y₂ → 2Z denkleminde atomlar korunur.','X: 4 atom, Y: 6 atom → 2Z → Z = X₂Y₃'),
  A('Toplam hacmi karşılaştır','Girenler 10 L, ürün 4 L’dir.','Gaz hacmi korunmamıştır'),
  A('Öncülleri değerlendir','Bulgular öncüllerle karşılaştırılır.','I: doğru · II: yanlış · III: doğru')],'hacim',
 z='orta',alt='Hacim Oranlarından Formül Bulma',kaz='Birleşen hacim oranlarını ve Avogadro hipotezini kullanarak gaz bileşiğinin formülünü ve hacim değişimini yorumlar.',kalip='öncüllü',
 kart='K-KMKN2-17 (hacim oranı, formül, öncüllü) · X₂ ve Y₂ gazlarından Z bileşiği',
 metin='Aynı sıcaklık ve basınçta ölçülen 4 L X₂ gazı ile 6 L Y₂ gazı, artan madde kalmayacak biçimde tepkimeye girerek yalnız 4 L Z gazı oluşturuyor.\nBuna göre,\nI. Z gazının formülü X₂Y₃’tür.\nII. Tepkime sonunda gaz hacmi, başlangıçtaki toplam gaz hacmine eşittir.\nIII. Aynı koşullarda 1 L Z gazı ile 1 L X₂ gazı eşit sayıda molekül içerir.\nyargılarından hangileri doğrudur?',
 istenen='Doğru olan yargılar.',ip=['Hacim oranını molekül sayısı oranı say ve her iki yanda atom sayılarını eşitle.'],
 bilgi=[B('Hacim oranı ve formül','aynı koşullarda gazların hacim oranı molekül sayısı oranıdır; ürünün formülü atomların korunumundan bulunur. Örnek: 1 hacim A₂ ile 1 hacim B₂ den 2 hacim gaz oluşuyorsa ürün AB’dir')],
 puf='Hacim oranını katsayı oranı olarak yaz, atom korunumuyla ürünün formülünü bul; gaz hacmi korunmak zorunda değildir.',
 **onc({'I':(True,'2X₂ + 3Y₂ → 2Z denkleminde atomların korunması için Z = X₂Y₃ olur.'),'II':(False,'Girenlerin hacmi 4 + 6 = 10 L, ürün hacmi 4 L’dir; gaz hacmi korunmamıştır.'),'III':(True,'Aynı sıcaklık ve basınçta eşit hacimli gazlar eşit sayıda molekül içerir.')},
   ['Yalnız II','Yalnız III','I ve III','II ve III','I, II ve III']))

# ================= 18 · iki denklem, katsayı toplamı farkı · zor =================
kartla('18','İki denklemin denkleştirilmesi','Her denklem ayrı ayrı en küçük tam sayılarla denkleştirilir; katsayı toplamları karşılaştırılır.','Atomları eksik eşitlemek; katsayıları genişletip en küçük sayıya inmemek.','zor','hikâyeli',5,'denk')
assert 4*1==2*2 and 3*2==2*3 and sum([4,3,2])==9
assert 2*2==4*1 and 2*6==6*2 and 7*2==4*2+6 and sum([2,7,4,6])==19 and 19-9==10
assert sum([2,4,4,6])-9==7 and 19-sum([2,3,2])==12 and sum([4,14,8,12])-9==29
q('0018',[A('1. denklemi denkleştir','Fe sayısını 2 Fe₂O₃ ile 4’e getir, sonra oksijeni eşitle.','4Fe + 3O₂ → 2Fe₂O₃ · toplam = 4 + 3 + 2 = 9'),
  A('2. denklemde C ve H’yi eşitle','2 C₂H₆’dan 4 C ve 12 H olur.','2C₂H₆ + O₂ → 4CO₂ + 6H₂O'),
  A('2. denklemde O’yu eşitle','Sağda 8 + 6 = 14 O atomu var, O₂ katsayısı 7 olur.','2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O · toplam = 2 + 7 + 4 + 6 = 19'),
  A('Farkı bul','2. denklemin toplamından 1. denklemin toplamı çıkarılır.','19 − 9 = 10')],'denk',
 z='zor',alt='İki Denklemin Denkleştirilmesi',kaz='İki farklı tepkime denklemini en küçük tam sayılarla denkleştirip katsayı toplamlarını karşılaştırır.',kalip='hikâyeli',
 kart='K-KMKN2-18 (denkleştirme, iki denklem) · Fe + O₂ ve C₂H₆ + O₂, katsayı toplamı farkı',
 metin='Bir kimya öğretmeni, demirin paslanmasını ve etanın tam yanmasını gösteren iki tepkimeyi denkleştirilmemiş olarak tahtaya yazıyor.\n1. tepkime: Fe + O₂ → Fe₂O₃\n2. tepkime: C₂H₆ + O₂ → CO₂ + H₂O\nÖğrencilerden iki denklemi de en küçük tam sayılı katsayılarla denkleştirmeleri ve 2. denklemin katsayıları toplamı ile 1. denklemin katsayıları toplamı arasındaki farkı bulmaları isteniyor.\nBuna göre bu fark kaçtır?',
 dogru=10,yan=[(7,'2. denklemde O₂ katsayısını yalnız CO₂’deki oksijene göre (4) belirleyip toplamı 16 bulmuş: 16 − 9.','islem'),(12,'1. denklemde Fe atomlarını eşitlememiş (2Fe + 3O₂ → 2Fe₂O₃, toplam 7): 19 − 7.','dikkat'),(19,'Yalnız 2. denklemin katsayıları toplamını bulmuş, farkı almamış.','dikkat'),(29,'2. denklemin katsayılarını 2 ile genişletmiş (toplam 38): 38 − 9.','islem')],
 istenen='Katsayı toplamları farkı.',ip=['Her denklemi ayrı ayrı, önce metal ya da C ve H, en son O atomlarını eşitleyerek denkleştir.'],
 bilgi=[B('En küçük tam sayılı katsayılar','denklem denkleştirilince katsayıların hepsinin birlikte bölünebileceği ortak bir sayı kalmamalıdır. Örnek: 2H₂ + O₂ → 2H₂O doğrudur, 4H₂ + 2O₂ → 4H₂O en küçük değildir')],
 puf='Katsayı toplamı sorularında önce her denklemi bağımsız ve en küçük tam sayılarla denkleştir.')

bitir(P,'kanunlariki','kim|Kimyanın Temel Kanunları')
