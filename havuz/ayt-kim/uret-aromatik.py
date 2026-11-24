"""AYT Kimya · Aromatik Bileşikler · 20 soru, kardeş yok, ipucu 1.
Şekil koordinatları, mol/kütle hesapları, izomer sayıları (kaba kuvvet) ve öncül doğrulukları Python'da hesaplanır."""
import sys,os,math,itertools,json
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__))
TD=os.path.join(GD,'..','tyt-kim')
sys.path.insert(0,TD)
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc_eski, tek
KONU_='Aromatik Bileşikler'; UK='akim|Aromatik Bileşikler'
H.KONU=KONU_
P=Parti('aromatik',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT Kimya organik soruları (yalnız mantık) · MEB 12. sınıf Aromatik Bileşikler'
MAP={}
for _n,_t in [(('01','04','05'),('yapi','Benzenin yapısı ve aromatiklik')),
              (('02','07','08'),('adlandirma','Adlandırma ve o-/m-/p- konumları')),
              (('06','09'),('izomer','Aromatik bileşiklerde izomerlik')),
              (('10','11','20'),('fenol','Fenol ve fenol türevleri')),
              (('03','13','16'),('toluen','Toluen ve benzen türevleri hesapları')),
              (('12','17','18'),('tepkime','Aromatik bileşiklerin tepkimeleri')),
              (('14','19'),('ozellik','Fiziksel özellikler ve kullanım')),
              (('15',),('enerji','Rezonans kararlılığı'))]:
    for _x in _n: MAP[_x]=_t
assert len(MAP)==20
def kartla(n,alt,fikir,tuzak,z,kalip,adim):
    a,b=MAP[n]; kart(f'K-AKAROM-{n}',alt,fikir,tuzak,z,kalip,adim,f'ak-arom-{a}',b,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    k['tipId']='ak-arom-'+MAP[no[-2:]][0]; k['tip']=MAP[no[-2:]][1]
    ne=k.pop('ne'); k['kart']=f"K-AKAROM-{no[-2:]} ({MAP[no[-2:]][1].lower()}) · {ne}"
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)

# ---------- öncüllü ve tekli yardımcılar ----------
def _anah(s): return (len(s),tuple(s))
def onc_t(d,hedef):
    etiket=sorted(d,key=lambda x:['I','II','III','IV'].index(x))
    T=frozenset(k for k,v in d.items() if v[0])
    ad=lambda s:tuple(sorted(s,key=lambda x:['I','II','III','IV'].index(x)))
    adaylar=[]
    for n in range(1,min(3,len(etiket))+1):
        for c in itertools.combinations(etiket,n): adaylar.append(c)
    adaylar=sorted(adaylar,key=_anah); kt=_anah(ad(T))
    alt=[c for c in adaylar if _anah(c)<kt]; ust=[c for c in adaylar if _anah(c)>kt]
    assert hedef<=len(alt) and 4-hedef<=len(ust),('hedef uygun degil',T,hedef,len(alt),len(ust))
    uz=lambda c:len(frozenset(c)^T)
    sa=sorted(alt,key=lambda c:(uz(c),-adaylar.index(c)))[:hedef]
    su=sorted(ust,key=lambda c:(uz(c),adaylar.index(c)))[:4-hedef]
    ops=sorted(sa+[ad(T)]+su,key=_anah)
    assert ops.index(ad(T))==hedef
    return _onc_eski(d,ops)
def tek_t(dogru,yanlislar,hedef,hedef_bool=True):
    S=[(m,not hedef_bool,n) for m,n in yanlislar]
    S.insert(hedef,(dogru[0],hedef_bool,dogru[1]))
    return tek(S,hedef_bool)
def cap(s): return ('İ' if s[0]=='i' else s[0].upper())+s[1:]
def oy(d,anahtarlar=None):
    return ' · '.join(f'{k}: '+('doğru' if d[k][0] else 'yanlış') for k in (anahtarlar or d))
def adim_onc(d,keys,baslik=None):
    ac=' '.join(cap(d[k][1])+'.' for k in keys)
    return A(baslik or ('. '.join(keys)+'. öncül' if len(keys)==1 else ' ve '.join(keys)+'. öncüller'),ac,oy(d,keys))
def sonuc(d,r): return A('Sonucu yaz','Doğru olan öncüller bir arada yazılır.',oy(d)+' · Sonuç: '+r['dogru'])

# ---------- halka çizim yardımcıları ----------
def vt(c,r,k):
    a=math.radians(90-60*k); return (c[0]+r*math.cos(a),c[1]+r*math.sin(a))
def inner(c,p,q_,t=.2,s=.14):
    p2=(p[0]+(c[0]-p[0])*t,p[1]+(c[1]-p[1])*t); q2=(q_[0]+(c[0]-q_[0])*t,q_[1]+(c[1]-q_[1])*t)
    d=(q2[0]-p2[0],q2[1]-p2[1]); a=(p2[0]+d[0]*s,p2[1]+d[1]*s); b=(q2[0]-d[0]*s,q2[1]-d[1]*s)
    return f'\\draw[thick] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
ANC={0:'south',1:'west',2:'west',3:'north',4:'east',5:'east'}
def subst(c,r,k,lab,L_=.45):
    p=vt(c,r,k); e=vt(c,r+L_,k)
    return f'\\draw[thick] ({p[0]:.3f},{p[1]:.3f}) -- ({e[0]:.3f},{e[1]:.3f}); \\node[anchor={ANC[k]},inner sep=1.5pt] at ({e[0]:.3f},{e[1]:.3f}) {{{lab}}};'
def ring(c=(0,0),r=.8,dbl=(0,2,4),sub=None,outline=True):
    pts=[vt(c,r,k) for k in range(6)]; g=''
    if outline: g+='\\draw[thick] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+' -- cycle;'
    for k in dbl: g+=inner(c,pts[k],pts[(k+1)%6])
    for k,lab in (sub or {}).items(): g+=subst(c,r,k,lab)
    return g
def naftalin(c=(0,0),r=.7):
    c2=(c[0]+math.sqrt(3)*r,c[1])
    return ring(c,r,dbl=(1,3,5))+ring(c2,r,dbl=(0,2))
def etiket(x,y,s): return f'\\node[font=\\bfseries] at ({x:.2f},{y:.2f}) {{{s}}};'
def ce(s): return '\\ce{'+s+'}'

# ---------- izomer kaba kuvvet ----------
GRUP=[]
for dn in range(6):
    GRUP.append([(i+dn)%6 for i in range(6)])
    GRUP.append([(dn-i)%6 for i in range(6)])
def kanon(atama):  # atama: {konum:etiket}
    best=None
    for g in GRUP:
        t=tuple(sorted((g[k],v) for k,v in atama.items()))
        t=tuple(sorted(t)); 
        if best is None or t<best: best=t
    return best
def sinif(etikets):
    """etikets: sıralı etiket listesi (örn. ['CH3','OH']); halkada tüm yerleşimlerin dihedral sınıf sayısı."""
    S=set()
    for kon in itertools.permutations(range(6),len(etikets)):
        S.add(kanon(dict(zip(kon,etikets))))
    return len(S)
def pozisyon(a,b):
    dd=(b-a)%6; dd=min(dd,6-dd); return {1:'o',2:'m',3:'p'}[dd]

# ============================================================ KARTLAR
kartla('01','Benzenin yapısı','Benzen düzlemsel altıgendir; C atomları sp² hibritleşmesi yapmıştır, π elektronları halka boyunca dağıldığından altı C–C bağı özdeştir.','Kekulé formülündeki tek ve çift bağların gerçekten ayrı uzunlukta olduğunu sanmak.','kolay','öncüllü',3)
kartla('02','Konum ekleri ve adlandırma','İki sübstitüentin halkadaki konumu o- (1,2), m- (1,3), p- (1,4) ile belirtilir; aynı bilgi sayı ile de verilir.','Konumu sayarken halka üzerinde yanlış yönde ya da yanlış atlayarak saymak; grubu yan zincir sanmak.','kolay','şekilli',3)
kartla('03','Benzen türevinde mol ve atom sayısı','Önce kütleden mol bulunur, sonra molekül formülündeki atom sayısıyla çarpılır.','Molekül molünü atom molü ile karıştırmak; benzenin formülünü toluene uygulamak.','kolay','düz',3)
kartla('04','Aromatik ve aromatik olmayan halkalar','Aromatik halka düzlemsel, tüm atomları sp² ve halkada π elektronları delokalizedir; tek çift bağlı halkalı hidrokarbon aromatik değildir.','Halka ve çift bağ içeren her bileşiği aromatik sanmak.','orta','şekilli',3)
kartla('05','Sigma ve pi bağı sayımı','Tüm bağlar σ, her çift bağın ikinci bağı π sayılır; π bağı sayısı Kekulé yapısındaki çift bağ sayısıdır.','Çift bağı iki π, halkayı σ dışında saymak; yalnız C–C bağlarını saymak.','orta','şekilli',4)
kartla('06','Fonksiyonel grup ve konum izomerliği','Aynı molekül formülüne sahip aromatik bileşikler fonksiyonel grup ve konum bakımından sayılır; halkadaki konumlar dihedral simetriye göre özdeşleşir.','Yalnız bir izomer türünü saymak; aynı bileşiği iki kez saymak.','zor','düz',5)
kartla('07','Üç yapıda ad–yapı eşleştirme','Her yapıda iki grubun halkadaki konumuna bakılarak o-, m- ya da p- adı belirlenir.','Konumu atlayarak saymak; fenol türevinde -OH grubunu başa almamak.','orta','öncüllü',3)
kartla('08','IUPAC adlandırma, alfabetik sıra','Sübstitüentler alfabetik sırayla yazılır; en küçük konum numaraları verilir, eşitlikte alfabetik olarak ilk grup 1 numarayı alır.','Numaralamayı metilden başlatmak; en küçük numara kuralını uygulamamak.','orta','şekilli',3)
kartla('09','Halkada ikinci sübstitüsyon izomerleri','Halkada birden çok farklı konumda sübstitüsyon izomer sayısı simetriye göre tarama yapılarak sayılır.','Simetrik çiftleri ayrı saymak; benzenin üç izomerli düzenini toluene aynen uygulamak.','zor','şekilli',5)
kartla('10','Fenolün özellikleri','Fenol halkaya doğrudan bağlı –OH içerir, zayıf asittir, NaOH ve Na ile tepkime verir; alkoller NaOH ile tepkime vermez.','Fenolü alkol gibi nötr sanmak.','orta','öncüllü',3)
kartla('11','Fenol–NaOH stokiyometrisi','Fenol NaOH ile sodyum fenolat ve su verir; mol oranı 1:1:1:1.','Ürün kütlesini girenlerin toplamıyla bulmak (suyu unutmak).','orta','düz',4)
kartla('12','Benzen ve halkalı hidrokarbonlar karşılaştırması','Brom çözeltisinde renk kaybı katılma tepkimesini, FeBr₃ ile HBr çıkışı sübstitüsyonu gösterir.','Benzenin siklohekzen gibi katılma verdiğini sanmak.','orta','tablo',3)
kartla('13','Toluenin yapısı ve özellikleri','Toluen C₇H₈; halka karbonları sp², CH₃ karbonu sp³; apolar olduğundan suda çözünmez.','Tüm karbonların sp² olduğunu sanmak; apolar bileşiğin suda çözüneceğini düşünmek.','orta','öncüllü',3)
kartla('14','Kaynama noktası karşılaştırması','Hidrojen bağı yapabilen madde en yüksek kaynama noktasına sahiptir; benzer apolar maddelerde mol kütlesi büyük olanın kaynama noktası yüksektir.','Kütleyi tek ölçüt almak ve hidrojen bağını gözden kaçırmak.','orta','grafik',3)
kartla('15','Hidrojenleme entalpisinden rezonans enerjisi','Üç izole çift bağlı varsayımsal molekülün hidrojenleme ısısı tek çift bağınkinin üç katıdır; gerçek benzenin ısısı bundan küçüktür, fark rezonans enerjisidir.','Farkı gerçek ve varsayımsal ısının toplamı ile bulmak.','zor','grafik',4)
kartla('16','Karışım yanması','İki bileşenli karışımda önce mol sayıları denklem sisteminden bulunur, sonra denkleştirilmiş yanma denklemlerinden ürün miktarı hesaplanır.','Eşit mol varsaymak; yalnız tek bileşenin yanma ürününü hesaplamak.','zor','hikâyeli',5)
kartla('17','Benzenin sübstitüsyon tepkimeleri','Benzende nitrolama, halojenleme ve alkilleme tepkimelerinde H atomu başka atom ya da grupla yer değiştirir.','Benzenin alkenler gibi katılma tepkimesine yatkın olduğunu sanmak.','orta','şekilli',3)
kartla('18','Sınırlayıcı bileşen ve verim','Önce sınırlayıcı bileşen bulunur, teorik ürün hesaplanır, sonra verimle çarpılır.','Verimi unutmak; fazla olan bileşene göre hesap yapmak.','zor','tablo',5)
kartla('19','Kullanım alanları ve sağlık etkileri','Benzen kanserojendir; toluen çözücüdür; fenol dezenfektan ve plastik hammaddesidir; naftalin güve önleyicidir.','Naftalinin suda çözünen iyonik bir madde olduğunu sanmak.','orta','düz',3)
kartla('20','Fenol, alkol ve eter ayrımı','C₇H₈O: halkada –OH (kresol) Na ve NaOH ile; yan zincirde –OH (benzil alkol) yalnız Na ile; eter (anisol) hiçbiriyle tepkime vermez.','Benzil alkolü fenol gibi NaOH ile tepkimeye girer sanmak.','zor','tablo',4)

# ============================================================ 01 · benzen yapısı (kolay, öncüllü, şekil)
SK1=tk(ring((0,0),1.0)+etiket(0,-1.45,'Benzen'))
d={'I':(True,'benzende altı karbon atomu da sp² hibritleşmesi yaptığından halka düzlemseldir'),
   'II':(True,'π elektronları halka boyunca dağıldığından altı C–C bağı özdeştir ve uzunlukları eşittir'),
   'III':(False,'benzende tek bağ ile çift bağ ayrımı yoktur; bütün C–C bağları aynı uzunluktadır')}
r=onc_t(d,1)
q('0001',ad=[A('Yapıyı hatırla','Benzen düzlemsel altıgen bir halkadır; Kekulé formülü gerçek bağ durumunu yalnız yaklaşık gösterir.','C₆H₆: 6 C, 6 H'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 alt='Benzenin Yapısı',z='kolay',kaz='Benzenin yapısal özelliklerini (düzlemsellik, bağ uzunlukları) açıklar.',kalip='öncüllü',ne='Kekulé yapısı, düzlemsellik ve bağ uzunluğu',
 metin='Benzen molekülünün Kekulé yapı formülü şekilde verilmiştir (C ve H atomları köşelerde gösterilmemiştir).\nI. Altı karbon atomu da aynı düzlemdedir.\nII. Karbon–karbon bağlarının uzunlukları birbirine eşittir.\nIII. Üç karbon–karbon bağı tek bağ, üç karbon–karbon bağı çift bağ uzunluğundadır.\nBuna göre hangileri doğrudur?',
 sekil=SK1,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Çift bağın π elektronlarının halkada nasıl dağıldığını düşün; bağ uzunlukları buna göre belirlenir.'],
 bilgi=[B('Rezonans','Birden fazla Kekulé yapısı çizilebilen moleküllerde gerçek yapı bu yapıların karışımıdır; elektronlar tek bir bağa ait değildir, halka boyunca dağılmıştır. Örnek: ozon (O₃) molekülünde iki O–O bağı özdeştir')],
 puf='Benzende tek–çift bağ ayrımı yoktur; altı C–C bağı özdeştir ve halka düzlemseldir.')

# ============================================================ 02 · p-klorotoluen (kolay, şekil, adlandırma)
SK2=tk(ring((0,0),.95,sub={0:ce('CH3'),3:'Cl'}))
assert pozisyon(0,3)=='p'
sec2=[('p-klorotoluen','CH3 ve Cl halkanın karşılıklı köşelerindedir (1,4-konumu); bu konum p- ile gösterilir'),
      ('o-klorotoluen','iki grup yan yana (1,2) olduğunda o- eki kullanılır; şekildeki gruplar komşu değildir'),
      ('m-klorotoluen','m- eki 1,3-konumunu gösterir; şekilde gruplar arasında iki karbon değil üç bağ vardır'),
      ('benzil klorür','Cl’un halkaya değil CH3 grubuna bağlı olduğu C₆H₅CH₂Cl bileşiğidir; şekilde Cl doğrudan halkadadır'),
      ('klorobenzen','tek sübstitüentli yapıdır; şekilde halkada metil grubu da bulunmaktadır')]
r=tek_t(sec2[0],sec2[1:],0)
q('0002',ad=[A('Gruplara bak','Halkaya doğrudan iki grup bağlıdır: CH₃ ve Cl.','Sübstitüentler: –CH₃, –Cl'),A('Konumu say','Birinci gruptan ikinci gruba halka üzerinden kaç bağ olduğuna bakılır.','CH₃ → Cl: 3 bağ (karşılıklı köşe)'),A('Konum önekini seç','Karşılıklı köşe p-, bir köşe arayla m-, komşu o- ile gösterilir.','1,4-konumu = p-'),A('Adı yaz','Ana ad toluen, ek olarak Cl ve konum eki yazılır.','p-klorotoluen')],
 alt='Adlandırma',z='kolay',kaz='Benzen türevlerini o-, m-, p- önekleriyle adlandırır.',kalip='şekilli',ne='p-klorotoluen yapısı',
 metin='Bir benzen türevinin yapı formülü şekilde verilmiştir.\nBuna göre bu bileşiğin adı aşağıdakilerden hangisidir?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Bileşiğin adı.',
 ip=['İki grubun halka üzerinde birbirinden kaç köşe uzakta olduğunu say.'],
 bilgi=[B('Konum önekleri','İki sübstitüent yan yana ise orto (o-), bir köşe arayla ise meta (m-), karşılıklı köşelerde ise para (p-) öneki kullanılır. Örnek: 1,3-dimetilbenzen m-ksilendir')],
 puf='Komşu = o-, bir köşe arayla = m-, karşılıklı = p-.')

# ============================================================ 03 · toluen mol H (kolay, düz)
M_T=7*12+8; assert M_T==92
mol=Fr(46,M_T); assert mol==Fr(1,2)
dogru3=mol*8; assert dogru3==4
yan3=[(mol,'Verilen kütleyi molar kütleye bölüp bulduğu 0,5 mol toluen molekülünü, H atomu mol sayısı olarak vermiştir.','islem'),
      (Fr(46,8),'Toluenin kütlesini H atomunun sayısına (8) bölmüş, mol hesabında molar kütle yerine 8 kullanmıştır.','islem'),
      (mol*15,'Toluendeki toplam atom sayısını (7 C + 8 H = 15) H atomu sayısı yerine almıştır.','dikkat'),
      (8,'1 mol toluende 8 mol H atomu bulunduğunu düşünüp verilen kütleyi hesaba katmamıştır.','dikkat')]
assert [y[0] for y in yan3]==[Fr(1,2),Fr(23,4),Fr(15,2),8]
q('0003',ad=[A('Molar kütleyi bul','Toluenin formülü C₇H₈ olduğundan molar kütle atom kütlelerinden hesaplanır.','7 × 12 + 8 × 1 = 92 g/mol'),A('Mol sayısını hesapla','Mol = kütle / molar kütle.','46 / 92 = 0,5 mol toluen'),A('H atomu sayısını yaz','Bir toluen molekülü 8 H atomu içerir.','1 mol toluen → 8 mol H atomu'),A('Sonucu çarp','Toluen molü ile molekül başına H atomu sayısı çarpılır.','0,5 × 8 = 4 mol H')],
 alt='Toluen Hesapları',z='kolay',kaz='Toluen örneğinde kütleden mol ve atom sayısını hesaplar.',kalip='düz',ne='46 gram toluende H atomu molü',
 metin='Toluen (C₆H₅CH₃), benzen halkasına bir metil grubunun bağlanmasıyla oluşan aromatik bir bileşiktir. Bir laboratuvarda 46 gram toluen örneği alınmıştır.\n(H: 1 g/mol, C: 12 g/mol)\nBuna göre bu örnekte toplam kaç mol H atomu bulunur?',
 dogru=dogru3,yan=yan3,istenen='Örnekteki H atomu mol sayısı.',
 ip=['Toluenin molekül formülünü yazıp önce verilen kütleye karşılık gelen mol sayısını bul.'],
 bilgi=[B('Mol ve atom sayısı','Bir bileşiğin mol sayısı, formüldeki atom sayısıyla çarpılınca o atomun mol sayısı bulunur. Örnek: 2 mol H₂O’da 2 × 2 = 4 mol H atomu vardır')],
 puf='Önce bileşiğin molü, sonra formüldeki atom sayısıyla çarpım.')

# ============================================================ 04 · aromatik mi? (orta, öncüllü, şekil)
g=ring((0,0),.75,sub={0:'OH'})+etiket(0,-1.35,'I')
g+=ring((3.2,0),.75,dbl=(0,))+etiket(3.2,-1.35,'II')
g+=naftalin((5.9,0),.75)+etiket(5.9+.65,-1.35,'III')
SK4=tk(g)
d={'I':(True,'bu yapı fenoldür; altı karbonlu düzlemsel halkada delokalize π elektronları bulunur, aromatiktir'),
   'II':(False,'sikloheksen halkalıdır ama tek çift bağ içerir, delokalize π sistemi yoktur ve aromatik değildir'),
   'III':(True,'naftalin kenar paylaşan iki benzen halkasından oluşur; halkalardaki π elektronları delokalizedir, aromatiktir')}
r=onc_t(d,2)
q('0004',ad=[A('Aromatik ölçütü hatırla','Aromatik halka düzlemsel olup π elektronları halka boyunca dağılmıştır.','Benzen halkası = aromatik'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 alt='Aromatiklik',z='orta',kaz='Verilen yapıların aromatik olup olmadığını belirler.',kalip='öncüllü',ne='fenol, sikloheksen, naftalin yapıları',
 metin='Aşağıda yapı formülleri verilen I, II ve III bileşiklerinden bazıları aromatik, bazıları aromatik olmayan bileşiktir (C ve H atomları köşelerde gösterilmemiştir).\nBuna göre hangileri aromatik bileşiktir?',
 sekil=SK4,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Aromatik olan bileşikler.',
 ip=['Her yapıda halkadaki π elektronlarının delokalize olup olmadığını, yani benzen halkası bulunup bulunmadığını incele.'],
 bilgi=[B('Aromatik bileşik','Benzen halkası içeren ya da benzen gibi kararlı delokalize π sistemine sahip bileşiklere aromatik bileşik denir. Örnek: toluen aromatiktir, sikloheksan değildir')],
 puf='Halka ve çift bağ yetmez; delokalize π sistemi (benzen halkası) olmalı.')

# ============================================================ 05 · etilbenzen σ−π (orta, şekil)
SK5=tk(ring((0,0),.9,sub={0:ce('C2H5')})+etiket(0,-1.45,'Etilbenzen'))
atom=8+10; halka=1; sig=atom-1+halka; assert sig==18
pi=3
# bağ sayımı el ile: C–C halka 6, halka–etil 1, etil C–C 1, C–H (5 halka + 5 etil) 10
assert 6+1+1+10==sig
n=Fr(1,2); dg=(sig-pi)*n; assert dg==Fr(15,2)
yan5=[(sig*n,'Yalnız σ bağlarını saymış ve π bağlarını farktan çıkarmayı unutmuştur: 0,5 × 18.','dikkat'),
      ((sig+pi)*n,'σ ile π bağı sayısını çıkarmak yerine toplamıştır: 0,5 × 21.','islem'),
      (sig-pi,'Farkı doğru bulmuş (15) ancak 0,5 mol ile çarpmayı unutmuştur.','islem'),
      (sig,'1 mol molekülün σ bağı sayısını (18) vermiş, mol sayısını ve π bağlarını hesaba katmamıştır.','dikkat')]
assert [y[0] for y in yan5]==[9,Fr(21,2),15,18]
q('0005',ad=[A('Atom ve halka sayısı','Tek halkalı bir molekülde σ bağı sayısı = atom sayısı − 1 + halka sayısı.','C₈H₁₀: 18 atom, 1 halka'),A('σ bağlarını say','Halkada 6 C–C, etil grubunda 1 C–C, halkaya bağlanmada 1 C–C ve 10 C–H bağı vardır.','σ = 6 + 1 + 1 + 10 = 18'),A('π bağlarını say','Kekulé yapısındaki her çift bağ bir π bağı içerir.','π = 3'),A('Farkı ve molü çarp','Bir moleküldeki fark, 0,5 mol ile çarpılır.','(18 − 3) × 0,5 = 7,5 mol')],
 alt='σ ve π Bağları',z='orta',kaz='Aromatik bir bileşikteki σ ve π bağı sayısını belirler.',kalip='şekilli',ne='0,5 mol etilbenzen σ−π farkı',
 metin='Etilbenzen (C₆H₅C₂H₅), stirenin üretiminde kullanılan aromatik bir bileşiktir; yapı formülü şekilde verilmiştir.\nBuna göre 0,5 mol etilbenzen molekülündeki sigma (σ) bağı mol sayısı ile pi (π) bağı mol sayısı arasındaki fark kaçtır?',
 sekil=SK5,dogru=dg,yan=yan5,istenen='σ bağı mol sayısı − π bağı mol sayısı.',
 ip=['Moleküldeki tüm bağları, C–H bağları dahil, tek tek say; π bağı yalnız çift bağların ikinci bağıdır.'],
 bilgi=[B('σ ve π bağı','Her tek bağ bir σ bağıdır; çift bağ bir σ ve bir π bağından oluşur. Örnek: eten (C₂H₄) molekülünde 5 σ ve 1 π bağı vardır')],
 puf='Tüm bağları σ say, çift bağların sayısı kadar π ekle; farkı mol ile çarp.')

# ============================================================ 06 · C7H8O izomerleri (zor, düz)
n_kresol=sinif(['CH3','OH']); assert n_kresol==3
topla=n_kresol+sinif(['OCH3'])+sinif(['CH2OH']); assert topla==5 and sinif(['OCH3'])==1
yan6=[(2,'Yalnız fonksiyonel grup izomerlerini (benzil alkol ve anisol) saymış, halkada CH₃ ve OH taşıyan kresol izomerlerini atlamıştır.','bilgi'),
      (n_kresol,'Yalnız halkada CH₃ ve OH bulunan o-, m-, p-kresolleri saymış, benzil alkol ile anisolü atlamıştır.','bilgi'),
      (4,'Üç kresol ile benzil alkolü saymış, anisol (metil fenil eter) izomerini atlamıştır.','dikkat'),
      (6,'Anisolü hem “metil fenil eter” hem “fenil metil eter” adıyla iki ayrı bileşik saymıştır.','dikkat')]
q('0006',ad=[A('Doymamışlığı belirle','C₇H₈O için halka ve üç çift bağ gerekir; geriye 1 C ve 1 O kalır.','Benzen halkası + 1 C + 1 O'),A('Halkada –CH₃ ve –OH','İki grup halkada o-, m-, p- konumlarında bulunabilir.','3 kresol izomeri'),A('Tek sübstitüentliler','C ve O tek grup olarak halkaya bağlanabilir: –CH₂OH ya da –OCH₃.','Benzil alkol ve anisol'),A('Toplamı yaz','Tüm özdeş olmayan yapılar toplanır.','3 + 1 + 1 = 5')],
 alt='İzomerlik',z='zor',kaz='Aromatik bileşiklerde fonksiyonel grup ve konum izomerlerini sayar.',kalip='düz',ne='C₇H₈O formüllü aromatik bileşikler',
 metin='Bileşiklerde halka dışında çift bağ bulunmadığı bilinmektedir.\nBuna göre molekül formülü C₇H₈O olan ve yapısında benzen halkası bulunan, birbirinden farklı kaç bileşik yazılabilir?',
 dogru=5,yan=yan6,istenen='Farklı izomer sayısı.',
 ip=['Halka dışında kalan C ve O atomlarının halkaya hangi gruplarla bağlanabileceğini ayrı ayrı düşün; sonra konumları ele al.'],
 bilgi=[B('Fonksiyonel grup izomerliği','Aynı molekül formülüne sahip, farklı fonksiyonel grup içeren bileşiklere fonksiyonel grup izomerleri denir. Örnek: C₂H₆O formülünde etanol (alkol) ve dimetil eter (eter) bulunur')],
 puf='Önce kalan atomlardan oluşabilecek grupları yaz, sonra iki gruplu yapıda konumları say.')

# ============================================================ 07 · üç yapıda adlandırma (orta, öncüllü, şekil)
assert pozisyon(0,1)=='o' and pozisyon(0,2)=='m' and pozisyon(0,3)=='p'
g=ring((0,0),.7,sub={0:ce('CH3'),1:'Br'})+etiket(0,-2.0,'K')
g+=ring((4.4,0),.7,sub={0:'OH',2:ce('NO2')})+etiket(4.4,-2.0,'L')
g+=ring((8.6,0),.7,sub={0:ce('CH3'),3:ce('CH3')})+etiket(8.6,-2.0,'M')
SK7=tk(g)
d={'I':(False,'K’de CH₃ ve Br komşu karbonlardadır; bu konum o- ile gösterilir, o-bromotoluendir'),
   'II':(False,'L’de OH ve NO₂ bir köşe arayla bağlıdır; bu konum m- ile gösterilir, m-nitrofenoldür'),
   'III':(True,'M’de iki CH₃ grubu karşılıklı köşelerdedir; 1,4-dimetilbenzen p-ksilendir')}
r=onc_t(d,1)
q('0007',ad=[A('Konumları belirle','Her yapıda iki grup arasındaki köşe sayısına bakılır.','K: komşu · L: bir köşe arayla · M: karşılıklı'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 alt='Adlandırma',z='orta',kaz='Yapı formülü verilen benzen türevlerinin adlarını konum eklerine göre değerlendirir.',kalip='öncüllü',ne='K, L, M yapıları ve adları',
 metin='K, L ve M bileşiklerinin yapı formülleri şekilde verilmiştir (C ve H atomları köşelerde gösterilmemiştir).\nI. K bileşiğinin adı m-bromotoluendir.\nII. L bileşiğinin adı p-nitrofenoldür.\nIII. M bileşiğinin adı p-ksilendir.\nBuna göre hangileri doğrudur?',
 sekil=SK7,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Her yapıda iki grubun halkadaki yerini ayrı ayrı sayarak adlardaki konum ekiyle karşılaştır.'],
 bilgi=[B('Ksilen','Ksilen, benzen halkasına iki metil grubunun bağlandığı dimetilbenzendir; o-, m- ve p- olmak üzere üç izomeri vardır. Örnek: 1,2-dimetilbenzen o-ksilendir')],
 puf='Önce her yapıda konumu say (komşu o-, bir köşe arayla m-, karşılıklı p-), sonra adla eşleştir.')

# ============================================================ 08 · IUPAC adı (orta, şekil)
SK8=tk(ring((0,0),.95,sub={0:ce('C2H5'),2:ce('CH3')}))
assert pozisyon(0,2)=='m'
sec8=[('1-etil-3-metilbenzen','alfabetik sırada etil önce gelir; konum numaraları eşit olduğunda etil 1 numarayı alır'),
      ('3-etil-1-metilbenzen','numaralamayı metilden başlatmış; oysa en küçük numara eşitliğinde alfabetik olarak ilk gelen etil grubu 1 numarayı alır'),
      ('1-etil-2-metilbenzen','iki grup arasında bir köşe bulunduğu halde konumu 1,2 (komşu) sanmış'),
      ('1-etil-4-metilbenzen','iki grup karşılıklı olmadığı halde konumu 1,4 saymış'),
      ('1-etil-5-metilbenzen','en küçük numara kuralını uygulamamış; 1,5 yerine 1,3 numaralaması kullanılır')]
r=tek_t(sec8[0],sec8[1:],4)
q('0008',ad=[A('Grupları tanı','Halkaya bir etil (C₂H₅) ve bir metil (CH₃) grubu bağlıdır.','–C₂H₅ ve –CH₃'),A('Konumu bul','Gruplar arasında bir köşe vardır.','1,3-konumu (meta)'),A('Numaralamayı seç','Numaralarda eşitlik varsa alfabetik olarak önce gelen grup 1 olur.','e < m → etil: 1, metil: 3'),A('Adı yaz','Sübstitüentler alfabetik sırayla yazılır, sonra benzen eklenir.','1-etil-3-metilbenzen')],
 alt='IUPAC Adlandırma',z='orta',kaz='Birden fazla sübstitüent taşıyan benzen türevlerini IUPAC kurallarına göre adlandırır.',kalip='şekilli',ne='etil ve metil gruplu benzen türevi',
 metin='Bir aromatik bileşiğin yapı formülü şekilde verilmiştir.\nBuna göre bu bileşiğin IUPAC adı aşağıdakilerden hangisinde doğru olarak verilmiştir?',
 sekil=SK8,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Bileşiğin IUPAC adı.',
 ip=['Önce iki grubun konumunu bul; sonra hangi grubun 1 numarayı alacağını alfabetik sıraya göre belirle.'],
 bilgi=[B('Alfabetik sıra','Sübstitüent adları alfabetik sırayla yazılır; yazarken sayısal önekler (di-, tri-) sıralamayı etkilemez. Örnek: 1-bromo-3-klorobenzen')],
 puf='En küçük numara eşitse alfabetik ilk grup 1 olur; adlar da alfabetik yazılır.')

# ============================================================ 09 · diklorotoluen izomer sayısı (zor, şekil)
SK9=tk(ring((0,0),.95,sub={0:ce('CH3')})+etiket(0,-1.5,'Toluen'))
n9=0
S=set()
for a,b in itertools.combinations(range(1,6),2):
    S.add(kanon({0:'CH3',a:'Cl',b:'Cl'}))
n9=len(S); assert n9==6
assert len({kanon({0:'CH3',a:'Cl'}) for a in range(1,6)})==3   # monokloro 3 ürün
assert sinif(['Cl','Cl'])==3
yan9=[(3,'Metil grubunu hesaba katmayıp halkayı benzen gibi düşünmüş; diklorobenzenin o-, m-, p- olmak üzere 3 izomeri olduğundan bu sayıyı vermiştir.','bilgi'),
      (4,'Halkadaki konum çiftlerinden yalnız simetrik eşi olanları saymış, kendi kendine simetrik iki çifti (2,6 ve 3,5) atlamıştır.','dikkat'),
      (5,'Tek Cl’lu ürünlerde hesaplanan 5 farklı konumu iki Cl için de aynen sanmıştır.','dikkat'),
      (10,'Halkadaki 5 H atomundan ikisini seçerken C(5,2) = 10 bulmuş, simetri nedeniyle özdeş olanları ayrı saymıştır.','islem')]
q('0009',ad=[A('Konumları numarala','CH₃ taşıyan karbon 1 kabul edilir; Cl yerine geçebilecek H atomları 2–6 konumlarındadır.','5 olası konum'),A('Çiftleri yaz','İki konumdan seçilen tüm Cl çiftleri yazılır.','C(5,2) = 10 çift'),A('Simetriyi uygula','Metil karbonundan geçen eksene göre 2↔6 ve 3↔5 konumları özdeştir.','23=56 · 24=46 · 25=36 · 34=45'),A('Özdeş olanları ele','Kendi kendine simetrik 26 ve 35 çiftleri ayrı sayılır.','4 + 2 = 6 farklı bileşik'),A('Sonucu yaz','Farklı diklorotoluenlerin sayısı bulunur.','6')],
 alt='İzomerlik',z='zor',kaz='Aromatik halkada ikinci sübstitüsyonla oluşan izomer sayısını belirler.',kalip='şekilli',ne='toluenin halkasında iki Cl sübstitüsyonu',
 metin='Toluenin yapı formülü şekilde verilmiştir. Toluenin benzen halkasındaki iki hidrojen atomu klor (Cl) atomlarıyla yer değiştirirse molekül formülü C₇H₆Cl₂ olan diklorotoluenler oluşur. (Metil grubundaki hidrojenler yer değiştirmemektedir.)\nBuna göre oluşabilecek diklorotoluen izomerlerinin sayısı kaçtır?',
 sekil=SK9,dogru=6,yan=yan9,istenen='Farklı diklorotoluen sayısı.',
 ip=['Metil grubunun bulunduğu karbondan geçen simetri eksenini düşün; hangi konum çiftleri aynı bileşiği verir?'],
 bilgi=[B('Simetri ve izomer sayımı','Halkada özdeş görünen konumlar, molekülün simetri düzlemiyle birbirine dönüşüyorsa aynı bileşiği verir. Örnek: toluende metil grubuna göre iki orto konumu özdeştir')],
 puf='Konum çiftlerini yaz, simetriyle birbirine dönüşenleri tek say.')

# ============================================================ 10 · fenol (orta, olumsuz kök)
sec10_d=('Sodyum metali ile tepkime vermez.','fenol Na metali ile tepkimeye girer ve H₂ gazı açığa çıkar; bu yüzden yanlış olan ifade budur')
sec10_y=[('Sodyum hidroksit çözeltisi ile tepkime vererek tuz oluşturur.','fenol zayıf asidik olduğundan NaOH ile sodyum fenolat ve su verir'),
         ('Hidroksil grubu doğrudan benzen halkasına bağlıdır.','fenolde –OH grubu halkadaki karbona doğrudan bağlıdır, yan zincirde değildir'),
         ('Su ile hidrojen bağı yapabilir.','–OH grubu sayesinde fenol su moleküllerine hidrojen bağıyla bağlanabilir'),
         ('Aynı koşullarda sikloheksanolden daha kuvvetli asidik özellik gösterir.','halkadaki π elektronları fenoksit iyonunu kararlı kıldığından fenol alkollerden daha asidiktir')]
r=tek_t(sec10_d,sec10_y,3,False)
q('0010',ad=[A('Fenolü tanı','Fenol halkaya doğrudan bağlı –OH içerir ve zayıf asittir.','C₆H₅OH'),A('Asitlik tepkimeleri','Zayıf asit olduğundan NaOH ve aktif metallerle tepkime verir.','NaOH ve Na ile tepkime verir'),A('İfadeleri sına','Her ifade fenolün bilinen özellikleriyle karşılaştırılır.','Yalnız bir ifade yanlıştır'),A('Yanlışı seç','Yanlış olan ifade Na ile tepkime vermediğini söyleyendir.','Na ile tepkime verir')],
 alt='Fenol',z='orta',kaz='Fenolün asidik özelliğini ve tepkimelerini açıklar.',kalip='düz',ne='fenolün özellikleri (olumsuz kök)',
 metin='Fenol (C₆H₅OH), dezenfektan ve plastik üretiminde kullanılan, benzen halkasına doğrudan –OH grubu bağlı aromatik bir bileşiktir. Bir öğrenci, fenolün özelliklerini aynı koşullardaki alkollerle karşılaştırmaktadır.\nBuna göre fenolle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',
 ip=['Fenolün asit özelliği gösterip göstermediğini düşün; asitlerin metallerle ve bazlarla verdiği tepkimeleri hatırla.'],
 bilgi=[B('Alkol ve fenol','–OH grubu halkaya doğrudan bağlıysa bileşik fenoldür, doymuş karbona bağlıysa alkoldür. Örnek: C₆H₁₁OH bir alkoldür, C₆H₅OH fenoldür')],
 puf='Fenol zayıf asittir: Na ve NaOH ile tepkime verir; halkaya bağlı –OH hidrojen bağı da yapar.')

# ============================================================ 11 · fenol + NaOH (orta, düz)
MF=6*12+6+16; assert MF==94
MN=6*12+5+16+23; assert MN==116
nf=Fr(188,10)/MF; assert nf==Fr(1,5)
dg11=nf*MN; assert dg11==Fr(232,10)
assert nf*40==8
yan11=[(Fr(8),'Yalnız harcanan NaOH kütlesini (0,2 × 40) bulup sonuç olarak vermiştir; ürünün kütlesini hesaplamamıştır.','dikkat'),
       (nf/2*MN,'Sodyum fenolatın molünü 0,1 mol bulup 0,1 × 116 hesaplamıştır; tepkime oranını 2 fenol : 1 ürün sanmıştır.','bilgi'),
       (nf*(MN-23),'Sodyum fenolatın formülünü C₆H₅O⁻ (93 g/mol) alıp Na kütlesini katmamıştır.','islem'),
       (Fr(188,10),'Fenolün kütlesini ürünün kütlesi sanmıştır.','dikkat')]
assert [y[0] for y in yan11]==[8,Fr(116,10),Fr(186,10),Fr(188,10)]
q('0011',ad=[A('Denklemi yaz','Fenol NaOH ile sodyum fenolat ve su oluşturur; katsayılar 1:1:1:1’dir.','C₆H₅OH + NaOH → C₆H₅ONa + H₂O'),A('Fenolün molünü bul','Mol = kütle / molar kütle.','18,8 / 94 = 0,2 mol'),A('Ürünün molünü bul','Mol oranı 1:1 olduğundan ürün de 0,2 moldür.','0,2 mol C₆H₅ONa'),A('Kütleyi hesapla','Ürünün molar kütlesiyle çarpılır.','0,2 × 116 = 23,2 g')],
 alt='Fenol Hesabı',z='orta',kaz='Fenolün NaOH ile tepkimesinde oluşan tuzun kütlesini hesaplar.',kalip='düz',ne='18,8 g fenol ile NaOH',
 metin='Fenol, sulu NaOH çözeltisi ile aşağıdaki denkleme göre tepkime verir:\nC₆H₅OH + NaOH → C₆H₅ONa + H₂O\n18,8 gram fenol, yeterli miktarda NaOH çözeltisi ile tam olarak tepkimeye giriyor.\n(H: 1 g/mol, C: 12 g/mol, O: 16 g/mol, Na: 23 g/mol)\nBuna göre oluşan sodyum fenolat (C₆H₅ONa) kaç gramdır?',
 dogru=dg11,yan=yan11,istenen='Oluşan C₆H₅ONa kütlesi (g).',
 ip=['Denklemdeki katsayılara bakarak harcanan fenol molü ile oluşan sodyum fenolat molünü ilişkilendir.'],
 bilgi=[B('Mol ve kütle','Bir maddenin kütlesi, mol sayısı ile molar kütlesinin çarpımıdır. Örnek: 0,5 mol CO₂ (44 g/mol) 22 g gelir')],
 puf='Önce mol bul, katsayı oranıyla ürün molüne geç, sonra molar kütleyle çarp.')

# ============================================================ 12 · brom testi tablosu (orta, öncüllü, tablo)
TAB12=[('K','Rengi değişmez','HBr gazı çıkar'),('L','Renk kaybolur','Gaz çıkmaz'),('M','Rengi değişmez','Gaz çıkmaz')]
SK12=tablo_svg(['Sıvı','Br₂ / CCl₄ (karanlık, katalizörsüz)','Br₂ / CCl₄ + FeBr₃'],[list(t) for t in TAB12])
d={'I':(True,'K’de katalizörle HBr çıkışı gözlenir; bu yer değiştirme (sübstitüsyon) benzen için tipiktir ve K benzendir'),
   'II':(True,'L brom çözeltisinin rengini giderir; çift bağa katılma olur, L siklohekzendir'),
   'III':(True,'M ne katılma ne sübstitüsyon verdiğinden doymuş halkalı hidrokarbon siklohekzandır; formülü C₆H₁₂’dir')}
r=onc_t(d,4)
q('0012',ad=[A('Gözlemleri yorumla','Renk kaybı katılmayı, HBr gazı sübstitüsyonu gösterir.','K: sübstitüsyon · L: katılma · M: tepkime yok'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 alt='Benzenin Tepkimeleri',z='orta',kaz='Gözlemlerden benzen, alken ve alkan davranışını ayırt eder.',kalip='tablo',ne='K, L, M için brom deneyleri',
 metin='Bir öğrenci, etiketleri karışmış K, L ve M sıvılarının benzen (C₆H₆), siklohekzen (C₆H₁₀) ve siklohekzan (C₆H₁₂) olduğunu biliyor. Sıvıları sırasıyla önce karanlıkta katalizörsüz brom çözeltisiyle, sonra FeBr₃ katalizörlüğünde brom çözeltisiyle karıştırıyor ve gözlemleri tabloda kaydediyor.\nI. K benzendir.\nII. L siklohekzendir.\nIII. M’nin molekül formülü C₆H₁₂’dir.\nBuna göre hangileri doğrudur?',
 sekil=SK12,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Brom renginin kaybolması ile gaz çıkışının hangi tepkime türünü gösterdiğini ayrı ayrı düşün.'],
 bilgi=[B('Brom testi','Doymamış hidrokarbonlar (alken, alkin) brom çözeltisinin rengini katılma tepkimesiyle giderir. Benzen ise katalizör olmadan brom ile tepkime vermez. Örnek: eten, brom suyunu renksizleştirir')],
 puf='Renk kaybı = katılma (doymamış); katalizörle HBr çıkışı = benzen halkasında sübstitüsyon.')

# ============================================================ 13 · toluen (orta, öncüllü)
d={'I':(True,'toluen C₆H₅CH₃ yapısındadır ve halkaya bir metil grubu bağlıdır; molekül formülü C₇H₈’dir'),
   'II':(False,'halkadaki karbonlar sp², metil grubundaki karbon sp³ hibritleşmesi yapmıştır; tüm karbonlar sp² değildir'),
   'III':(False,'toluen apolar bir bileşik olduğundan polar çözücü olan suda çok az çözünür')}
r=onc_t(d,0)
q('0013',ad=[A('Toluenin yapısını yaz','Toluen halkaya CH₃ bağlı aromatik bileşiktir.','C₆H₅–CH₃'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 alt='Toluen',z='orta',kaz='Toluenin yapısını ve fiziksel özelliklerini açıklar.',kalip='öncüllü',ne='toluenin formülü, hibritleşme ve çözünürlük',
 metin='Toluen, boya ve yapıştırıcı sanayisinde çözücü olarak kullanılan bir sıvıdır. Bir öğrenci, toluenle ilgili aşağıdaki ifadeleri yazmıştır.\nI. Molekül formülü C₇H₈’dir.\nII. Yapısındaki tüm karbon atomları sp² hibritleşmesi yapmıştır.\nIII. Suda her oranda çözünür.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Metil grubundaki karbonun kaç σ bağı yaptığını sayarak hibritleşmesini belirle.'],
 bilgi=[B('Hibritleşme','Dört σ bağı yapan karbon sp³, bir π bağı ve üç σ bağı yapan karbon sp² hibritleşmesi yapar. Örnek: etanda sp³, etende sp² karbonlar vardır')],
 puf='Halka karbonları sp², metil karbonu sp³; apolar bileşik suda çözünmez.')

# ============================================================ 14 · kaynama noktası grafiği (orta, grafik)
KN={'K':('toluen',111),'L':('fenol',182),'M':('benzen',80)}
sy=.02
g=f'\\draw[thick,{ARR}] (0,0) -- (0,4.4); \\draw[thick] (0,0) -- (5.6,0);'
for t in range(0,201,40):
    g+=f'\\draw[gray!40] (0,{t*sy:.2f}) -- (5.4,{t*sy:.2f}); \\draw (0,{t*sy:.2f}) -- (-.08,{t*sy:.2f}) node[left] {{{t}}};'
for i,(k,(ad_,v)) in enumerate(KN.items()):
    x=1.0+i*1.7
    g+=f'\\draw[thick,fill=vurgu!30] ({x-.5},0) rectangle ({x+.5},{v*sy:.2f}); \\node[below,font=\\bfseries] at ({x},-.05) {{{k}}};'
g+='\\node[anchor=south west,font=\\small] at (-.3,4.45) {Kaynama noktası (°C)};'
SK14=tk(g)
assert KN['L'][1]>KN['K'][1]>KN['M'][1]
sec14=[('K: toluen, L: fenol, M: benzen','fenol hidrojen bağı yapabildiğinden kaynama noktası en yüksektir (L); apolar toluen, benzenden büyük mol kütlesi nedeniyle daha yüksekte kaynar (K > M)'),
       ('K: benzen, L: fenol, M: toluen','benzenin mol kütlesi toluenden küçüktür; aynı tür etkileşimde benzenin kaynama noktası toluenden düşük olur, grafikte M K’dan düşüktür'),
       ('K: fenol, L: toluen, M: benzen','fenol hidrojen bağı yaptığından en yüksek kaynama noktasına sahip olandır; grafikte bu L’dir'),
       ('K: toluen, L: benzen, M: fenol','fenolün kaynama noktası en yüksek olmalıdır; grafikteki en yüksek çubuk M değildir'),
       ('K: benzen, L: toluen, M: fenol','grafikteki en yüksek çubuk L’dir; fenol hidrojen bağı nedeniyle en yüksekte kaynar ve L’ye karşılık gelir')]
r=tek_t(sec14[0],sec14[1:],2)
q('0014',ad=[A('Etkileşimleri belirle','Fenol hidrojen bağı yapar; benzen ve toluen apolardır, yalnız London kuvvetleri vardır.','Fenol: H bağı + London'),A('Fenolü bul','Hidrojen bağı yapan madde en yüksek kaynama noktasına sahiptir.','En yüksek çubuk: L = fenol'),A('Benzen ve toluenı ayır','Apolar maddelerde mol kütlesi büyük olanın kaynama noktası yüksektir.','Toluen (92) > benzen (78) → K = toluen, M = benzen'),A('Eşleştirmeyi yaz','Üç madde çubuklarla eşleştirilir.','K: toluen, L: fenol, M: benzen')],
 alt='Kaynama Noktası',z='orta',kaz='Aromatik bileşiklerin kaynama noktalarını molekül etkileşimleriyle yorumlar.',kalip='grafik',ne='K, L, M kaynama noktası grafiği',
 metin='K, L ve M ile gösterilen maddeler; benzen (C₆H₆, 78 g/mol), toluen (C₆H₅CH₃, 92 g/mol) ve fenol (C₆H₅OH, 94 g/mol) bileşikleridir. Aynı dış basınçta bu maddelerin kaynama noktaları grafikte çubuklarla gösterilmiştir.\nBuna göre K, L ve M aşağıdakilerden hangisinde doğru olarak verilmiştir?',
 sekil=SK14,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='K, L, M maddelerinin doğru eşleşmesi.',
 ip=['Üç maddenin molekülleri arasındaki en baskın etkileşimi belirle; kaynama noktası bu etkileşimin gücüyle artar.'],
 bilgi=[B('Kaynama noktası','Moleküller arası çekim kuvveti büyüdükçe kaynama noktası artar. Hidrojen bağı, London kuvvetlerinden güçlüdür. Örnek: etanol (H bağı) aynı kütleli propanın kaynama noktasından yüksektir')],
 puf='Önce hidrojen bağı yapanı (en yüksek) bul, kalanları mol kütlesiyle sırala.')

# ============================================================ 15 · rezonans enerjisi (zor, grafik)
sc=.015
yh=360*sc; yb=208*sc
g=f'\\draw[thick,{ARR}] (-.5,-.2) -- (-.5,6.2); \\node[anchor=south,font=\\small] at (-.5,6.25) {{Enerji}};'
g+=f'\\draw[very thick] (0,{yh:.2f}) -- (2.2,{yh:.2f}); \\draw[very thick] (3.4,{yb:.2f}) -- (5.6,{yb:.2f}); \\draw[very thick] (6.8,0) -- (9.0,0);'
g+=f'\\node[above,align=center,font=\\footnotesize] at (1.1,{yh+.05:.2f}) {{Varsayımsal\\\\siklohekzatrien\\\\(üç yalıtılmış C=C)\\\\+ 3 \\ce{{H2}}}};'
g+=f'\\node[above,font=\\footnotesize] at (4.5,{yb+.05:.2f}) {{\\ce{{C6H6 + 3H2}}}}; \\node[above,font=\\footnotesize] at (7.9,.05) {{\\ce{{C6H12}}}};'
g+=f'\\draw[dashed,gray] (2.2,{yh:.2f}) -- (2.9,{yh:.2f}); \\draw[dashed,gray] (2.9,{yb:.2f}) -- (3.4,{yb:.2f});'
g+=f'\\draw[Stealth-Stealth] (2.9,{yb:.2f}) -- (2.9,{yh:.2f}); \\node[anchor=west] at (2.98,{(yb+yh)/2:.2f}) {{$x$}};'
g+=f'\\draw[dashed,gray] (5.6,{yb:.2f}) -- (6.2,{yb:.2f}); \\draw[dashed,gray] (6.2,0) -- (6.8,0); \\draw[{ARR}] (6.2,{yb:.2f}) -- (6.2,0); \\node[anchor=east,align=right] at (6.1,{yb/2:.2f}) {{$\\Delta H=-208$ kJ}};'
SK15=tk(g)
rez=3*120-208; assert rez==152
yan15=[(3*120,'Üç çift bağın hidrojenlenme ısısının toplamını (3 × 120) rezonans enerjisi olarak vermiştir.','dikkat'),
       (208,'Benzenin gerçek hidrojenlenme ısısını rezonans enerjisi sanmıştır.','dikkat'),
       (120,'Siklohekzenin hidrojenlenme ısısını (120) rezonans enerjisi sanmıştır.','bilgi'),
       (208-120,'Benzenin hidrojenlenme ısısından yalnız bir çift bağın ısısını çıkarmıştır: 208 − 120.','bilgi')]
assert [y[0] for y in yan15]==[360,208,120,88]
q('0015',ad=[A('Varsayımsal ısıyı bul','Üç yalıtılmış çift bağın hidrojenlenme ısısı bir çift bağınkinin üç katıdır.','3 × (−120) = −360 kJ'),A('Gerçek ısıyı oku','Şekilde benzenin hidrojenlenme ısısı verilmiştir.','ΔH = −208 kJ'),A('Enerji farkını yaz','Varsayımsal sistem, benzenden x kadar daha yüksek enerjilidir.','x = 360 − 208'),A('Rezonans enerjisini bul','Bu fark benzenin ek kararlılığıdır.','x = 152 kJ/mol')],
 alt='Rezonans Kararlılığı',z='zor',kaz='Hidrojenleme entalpilerinden benzenin rezonans kararlılığını hesaplar.',kalip='grafik',ne='benzen ve siklohekzen hidrojenleme entalpileri',
 metin='Siklohekzenin (C₆H₁₀) 1 mol’ünün hidrojenlenerek siklohekzana (C₆H₁₂) dönüşmesinde 120 kJ ısı açığa çıkar. Benzenin hidrojenlenerek siklohekzana dönüşme tepkimesinin enerji diyagramı ise şekilde verilmiştir. Diyagramda üç yalıtılmış çift bağlı varsayımsal siklohekzatrienin enerjisi ile benzenin enerjisi arasındaki fark x ile gösterilmiştir.\nBuna göre x değeri kaç kJ’dür?',
 sekil=SK15,dogru=rez,yan=yan15,istenen='x değeri (kJ).',
 ip=['Üç çift bağın birbirinden bağımsız hidrojenlendiğini varsayarak o sistemin toplam ısısını hesapla, sonra diyagramdaki gerçek değerle karşılaştır.'],
 bilgi=[B('Entalpi ve kararlılık','Aynı ürüne giden iki yoldan daha az ısı veren başlangıç maddesi daha düşük enerjilidir, yani daha kararlıdır. Örnek: bir maddeyi yakınca açığa çıkan ısı küçükse madde yanmadan önce daha kararlıdır')],
 puf='Varsayımsal toplam ısı − gerçek ısı = rezonans enerjisi.')

# ============================================================ 16 · benzen–toluen karışımı yanması (zor, hikâyeli)
Mb=78; Mt=92
toplam_mol=Fr(1,2); kutle=Fr(418,10)
xb=(Mt*toplam_mol-kutle)/(Mt-Mb); xt=toplam_mol-xb; assert (xb,xt)==(Fr(3,10),Fr(1,5)) and xb*Mb+xt*Mt==kutle
su_mol=3*xb+4*xt; assert su_mol==Fr(17,10)
dg16=su_mol*18; assert dg16==Fr(306,10)
yan16=[(toplam_mol*3*18,'Karışımın tamamını benzen sanıp 0,5 × 3 mol su hesaplamıştır.','dikkat'),
       (toplam_mol*4*18,'Karışımın tamamını toluen sanıp 0,5 × 4 mol su hesaplamıştır.','dikkat'),
       ((Fr(1,4)*3+Fr(1,4)*4)*18,'Benzen ve toluenin mol sayılarını eşit (0,25’er mol) almıştır.','bilgi'),
       ((xt*3+xb*4)*18,'Benzen ve toluenin mol sayılarını birbiriyle değiştirmiştir (0,2 mol benzen, 0,3 mol toluen).','islem')]
assert [y[0] for y in yan16]==[27,36,Fr(63,2),Fr(162,5)]
q('0016',ad=[A('Bilinmeyenleri tanımla','Benzen ve toluenin mol sayıları x ve y olsun.','x + y = 0,5'),A('Kütle denklemini yaz','Toplam kütle, mol sayıları ile molar kütlelerin çarpımlarının toplamıdır.','78x + 92y = 41,8'),A('Mol sayılarını çöz','İki denklem birlikte çözülür.','x = 0,3 mol · y = 0,2 mol'),A('Su molünü bul','C₆H₆ başına 3 H₂O, C₇H₈ başına 4 H₂O oluşur.','0,3 × 3 + 0,2 × 4 = 1,7 mol'),A('Kütleyi hesapla','Su molü molar kütle ile çarpılır.','1,7 × 18 = 30,6 g')],
 alt='Karışım Yanması',z='zor',kaz='Benzen–toluen karışımından yanma ürünlerini stokiyometrik olarak hesaplar.',kalip='hikâyeli',ne='41,8 g benzen–toluen karışımı',
 metin='Bir çözücü karışımının benzen (C₆H₆) ve toluen (C₆H₅CH₃) içerdiği, başka madde içermediği biliniyor. Karışımdan alınan numune 0,5 mol olup 41,8 gramdır. Bu numune oksijenle tam olarak yakılıyor ve yalnız CO₂ ile H₂O oluşuyor.\n(H: 1 g/mol, C: 12 g/mol, O: 16 g/mol)\nBuna göre oluşan su kaç gramdır?',
 dogru=dg16,yan=yan16,istenen='Oluşan H₂O kütlesi (g).',
 ip=['Numunedeki iki bileşenin mol sayılarını, toplam mol ve toplam kütle verisinden iki bilinmeyenli denklemle bul.'],
 bilgi=[B('Hidrokarbon yanması','Hidrokarbonlar tam yanınca CO₂ ve H₂O verir; oluşan H₂O molü, bileşikteki H atomu sayısının yarısına eşittir. Örnek: C₂H₆ yanarsa 1 mol C₂H₆’dan 3 mol H₂O oluşur')],
 puf='Mol ve kütle denklemlerini birlikte çöz; su molü H atomu sayısının yarısıdır.')

# ============================================================ 17 · benzenin tepkimeleri (orta, öncüllü, şema)
g=ring((0,0),.6,dbl=(0,2,4))+'\\node[font=\\bfseries] at (0,-1.0) {Benzen};'
g+='\\draw[thick] (.75,0) -- (1.3,0); \\draw[thick] (1.3,-2.3) -- (1.3,2.3);'
RE=[(2.3,'HNO$_3$ / H$_2$SO$_4$',ce('NO2'),'K'),(0,'Cl$_2$ / FeCl$_3$','Cl','L'),(-2.3,'CH$_3$Cl / AlCl$_3$',ce('CH3'),'M')]
for y,reag,sb,lab in RE:
    g+=f'\\draw[thick,{ARR}] (1.3,{y}) -- (4.4,{y}); \\node[above,font=\\footnotesize] at (2.85,{y+.02}) {{{reag}}};'
    g+=ring((5.4,y),.6,dbl=(0,2,4),sub={1:sb})+etiket(5.4,y-1.0,lab)
SK17=tk(g)
d={'I':(False,'üç tepkimede de benzen halkasındaki bir H atomu başka bir atom ya da grupla yer değiştirir; bunlar sübstitüsyon tepkimeleridir, katılma değildir'),
   'II':(True,'L, benzenin bir H atomunun Cl ile yer değiştirmesiyle oluşan klorobenzendir; formülü C₆H₅Cl’dir'),
   'III':(False,'M’de halkaya bir CH₃ grubu bağlanmıştır; bu bileşik toluendür, etilbenzen değildir')}
r=onc_t(d,0)
q('0017',ad=[A('Tepkime türünü belirle','Halkaya bir grup bağlanırken bir H ayrılıyorsa tepkime sübstitüsyondur.','K, L, M: H yerine grup'),adim_onc(d,['I']),adim_onc(d,['II']),adim_onc(d,['III']),sonuc(d,r)],
 alt='Sübstitüsyon Tepkimeleri',z='orta',kaz='Benzenin nitrolama, halojenleme ve alkilleme ürünlerini belirler.',kalip='şekilli',ne='benzenden K, L, M elde edilmesi',
 metin='Benzenden başlayarak K, L ve M bileşiklerinin elde edildiği tepkimeler şekilde verilmiştir (C ve H atomları köşelerde gösterilmemiştir).\nI. Üç tepkime de katılma tepkimesidir.\nII. L’nin molekül formülü C₆H₅Cl’dür.\nIII. M’nin adı etilbenzendir.\nBuna göre hangileri doğrudur?',
 sekil=SK17,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Ürünlerde halkadaki H atomu sayısının benzene göre ne olduğuna bak; her grup halkaya hangi atomla bağlanıyor?'],
 bilgi=[B('Sübstitüsyon','Sübstitüsyon (yer değiştirme) tepkimesinde bir atom ya da atom grubu, molekülden ayrılan bir başka atom ya da grubun yerini alır. Örnek: CH₄ + Cl₂ → CH₃Cl + HCl')],
 puf='Benzende H atomu yer değiştirir, çift bağlara katılma olmaz.')

# ============================================================ 18 · nitrobenzen verimi (zor, tablo)
Mb=78; Mn=6*12+5+14+32; assert Mn==123
nb=Fr(468,10)/Mb; nn=Fr(252,10)/63
assert (nb,nn)==(Fr(3,5),Fr(2,5)) and nn<nb
dg18=nn*Fr(1,2)*Mn; assert dg18==Fr(246,10)
yan18=[(nn*Fr(1,2)*18,'Oluşan suyun kütlesini (0,2 × 18) nitrobenzenin kütlesi olarak vermiştir.','dikkat'),
       (nn*Fr(1,2)*Mb,'Ürünün molar kütlesi yerine benzenin molar kütlesini (78 g/mol) kullanmıştır.','bilgi'),
       (nb*Fr(1,2)*Mn,'Fazla olan benzene göre hesap yapmış, sınırlayıcı bileşen olan HNO₃’ü gözden kaçırmıştır.','bilgi'),
       (nn*Mn,'Sınırlayıcı bileşeni doğru bulmuş ancak yüzde 50 verimi hesaba katmamıştır.','dikkat')]
assert [y[0] for y in yan18]==[Fr(18,5),Fr(78,5),Fr(369,10),Fr(246,5)]
SK18=tablo_svg(['Giren madde','Kütle (g)'],[['Benzen (C₆H₆)','46,8'],['Nitrik asit (HNO₃, saf)','25,2']])
q('0018',ad=[A('Mol sayılarını bul','Her girenin molü kütle / molar kütle ile bulunur.','C₆H₆: 46,8/78 = 0,6 mol · HNO₃: 25,2/63 = 0,4 mol'),A('Sınırlayıcıyı belirle','Tepkime 1:1 mol oranlıdır; mol sayısı az olan bitince tepkime durur.','HNO₃ sınırlayıcı: 0,4 mol'),A('Teorik ürünü hesapla','Teorik nitrobenzen molü sınırlayıcı kadardır.','0,4 mol C₆H₅NO₂'),A('Verimi uygula','Gerçek ürün, teorik ürünün yarısı kadardır.','0,4 × 0,5 = 0,2 mol'),A('Kütleye çevir','Nitrobenzenin molar kütlesi 123 g/mol’dür.','0,2 × 123 = 24,6 g')],
 alt='Nitrolama ve Verim',z='zor',kaz='Benzenin nitrolanmasında sınırlayıcı bileşeni ve verimi hesaba katarak ürün kütlesini bulur.',kalip='tablo',ne='benzen + HNO₃ → nitrobenzen, %50 verim',
 metin='Derişik H₂SO₄ katalizörlüğünde benzenin nitrolanması aşağıdaki denkleme göre gerçekleşir:\nC₆H₆ + HNO₃ → C₆H₅NO₂ + H₂O\nBir laboratuvarda tabloda verilen miktarlarda benzen ve saf nitrik asit karıştırılıyor. Tepkime yüzde 50 verimle gerçekleşiyor.\n(H: 1 g/mol, C: 12 g/mol, N: 14 g/mol, O: 16 g/mol)\nBuna göre oluşan nitrobenzen (C₆H₅NO₂) kaç gramdır?',
 sekil=SK18,dogru=dg18,yan=yan18,istenen='Oluşan C₆H₅NO₂ kütlesi (g).',
 ip=['Tepkimenin hangi girenin bitmesiyle durduğunu mol sayılarını karşılaştırarak belirle.'],
 bilgi=[B('Sınırlayıcı bileşen','Girenlerden mol sayısı (katsayıya göre) önce tükenen sınırlayıcı bileşendir; ürün miktarını o belirler. Örnek: 2 mol H₂ ile 2 mol O₂ tepkimesinde H₂ sınırlayıcıdır')],
 puf='Önce sınırlayıcıyı bul, teorik ürünü hesapla, en son verimle çarp.')

# ============================================================ 19 · kullanım alanları (orta, düz, olumsuz kök)
sec19_d=('Naftalin, suda çok iyi çözünen iyonik yapılı bir katıdır.','naftalin apolar kovalent bir bileşiktir, suda çok az çözünür; bu nedenle yanlış olan ifade budur')
sec19_y=[('Naftalin, güve önleyici olarak kullanılır.','naftalin süblimleşen bir katıdır ve güve topu olarak kullanılır'),
         ('Fenol, dezenfektan ve bazı plastiklerin üretiminde kullanılır.','fenol antiseptik özelliği nedeniyle dezenfektanlarda, ayrıca reçine ve plastik üretiminde kullanılır'),
         ('Toluen, boya ve yapıştırıcılarda çözücü olarak kullanılır.','toluen apolar bir sıvıdır ve boya, yapıştırıcı gibi ürünlerde çözücü görevi görür'),
         ('Benzen, kanserojen etkili olduğundan kullanımı sınırlandırılmıştır.','benzenin buharı solunduğunda kansere yol açabildiğinden kullanımı kısıtlanmıştır')]
r=tek_t(sec19_d,sec19_y,3,False)
q('0019',ad=[A('Her bileşiği tanı','Benzen, toluen, fenol ve naftalin aromatik bileşiklerdir.','Dört bileşik: kullanım ve özellikleri'),A('Kullanımları eşle','Naftalin güve önleyici, fenol dezenfektan, toluen çözücüdür.','Naftalin: güve topu'),A('Çözünürlüğü yorumla','Aromatik hidrokarbonlar apolardır; suda çok az çözünürler.','Naftalin: apolar, suda az çözünür'),A('Yanlışı seç','Naftalinin suda çok iyi çözündüğünü ve iyonik olduğunu söyleyen ifade yanlıştır.','İyonik ve suda çok çözünür: yanlış')],
 alt='Kullanım ve Etkileri',z='orta',kaz='Aromatik bileşiklerin kullanım alanlarını ve çevre/sağlık etkilerini açıklar.',kalip='düz',ne='aromatik bileşiklerin kullanımı (olumsuz kök)',
 metin='Aromatik bileşikler endüstride ve günlük hayatta pek çok alanda kullanılır; bazılarının sağlığa zararlı etkileri nedeniyle kullanımı sınırlandırılmıştır. Bir kimya öğretmeni, bu bileşiklerle ilgili beş ifade yazıp öğrencilerinden yanlış olanı bulmalarını istemiştir.\nBuna göre aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',
 ip=['Hidrokarbon yapısındaki aromatik bileşiklerin polarlığını ve bağ türünü düşünerek çözünürlüğe bak.'],
 bilgi=[B('Polarlık ve çözünürlük','Benzer benzeri çözer: apolar maddeler apolar çözücülerde, polar maddeler polar çözücülerde çözünür. Örnek: yağ suda değil, benzende çözünür')],
 puf='Aromatik hidrokarbonlar apolar kovalent yapıdadır; suda çok az çözünürler.')

# ============================================================ 20 · C7H8O tablosu (zor, tablo)
TAB20=[('K','Tepkime verir, H₂ çıkar','Tepkime verir'),('L','Tepkime verir, H₂ çıkar','Tepkime vermez'),('M','Tepkime vermez','Tepkime vermez')]
SK20=tablo_svg(['Bileşik','Na metali ile','NaOH çözeltisi ile'],[list(t) for t in TAB20])
TRUTH={'K':'kresol (metilfenol)','L':'benzil alkol','M':'anisol'}
sebep={'kresol (metilfenol)':'halkaya bağlı –OH içerir; hem Na hem NaOH ile tepkime verir',
       'benzil alkol':'–OH grubu halkaya değil CH₂ karbonuna bağlıdır; Na ile tepkime verir, NaOH ile vermez',
       'anisol':'eter olduğundan –OH grubu yoktur; ne Na ne NaOH ile tepkime verir'}
def sirala(a): return f'K: {a[0]}, L: {a[1]}, M: {a[2]}'
PM=[tuple(TRUTH[k] for k in 'KLM')]
for pm in itertools.permutations(TRUTH.values()):
    if pm!=PM[0]: PM.append(pm)
sec20=[PM[0],PM[1],PM[3],PM[2],PM[4]]  # doğru + 4 çeldirici
yl20=[]
for pm in sec20[1:]:
    yanl=[f'{k} için {pm[i]} denmiş; oysa {k} için gözlemler {TRUTH[k]} ile uyumludur ({sebep[TRUTH[k]]})' for i,k in enumerate('KLM') if pm[i]!=TRUTH[k]]
    yl20.append((sirala(pm),yanl[0]))
r=tek_t((sirala(PM[0]),'K, L ve M sırasıyla halkada –OH, yan zincirde –OH ve eter grubu taşıyan bileşiklerdir'),yl20,4)
q('0020',ad=[A('Gözlemleri sınıfla','Na ile tepkime –OH grubunu, NaOH ile tepkime asidik (fenol) hidrojeni gösterir.','K: Na ve NaOH · L: yalnız Na · M: hiçbiri'),A('K’yi belirle','Hem Na hem NaOH ile tepkime veren –OH halkaya bağlıdır.','K: kresol (fenol türevi)'),A('L ve M’yi belirle','Yalnız Na ile tepkime veren alkoldür; hiçbiriyle vermeyen eterdir.','L: benzil alkol · M: anisol'),A('Eşleştirmeyi yaz','Üç bileşik gözlemlerle eşleştirilir.','K: kresol, L: benzil alkol, M: anisol')],
 alt='Fenol, Alkol ve Eter',z='zor',kaz='C₇H₈O izomerlerini Na ve NaOH ile tepkimelerine göre ayırt eder.',kalip='tablo',ne='C₇H₈O izomerleri K, L, M',
 metin='Molekül formülü C₇H₈O olan ve benzen halkası içeren K, L ve M bileşikleri; kresol (metilfenol), benzil alkol (C₆H₅CH₂OH) ve anisol (C₆H₅OCH₃) bileşiklerinden biridir. Bu bileşiklerin sodyum metali ve sulu NaOH çözeltisi ile tepkime verip vermediği tabloda verilmiştir.\nBuna göre K, L ve M aşağıdakilerden hangisinde doğru olarak verilmiştir?',
 sekil=SK20,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='K, L, M bileşiklerinin doğru eşleşmesi.',
 ip=['–OH grubunun halkaya bağlı olup olmamasının NaOH ile tepkimeyi nasıl etkilediğini; eterde –OH olup olmadığını düşün.'],
 bilgi=[B('Alkol, fenol ve eter','Alkol ve fenol –OH, eter ise C–O–C grubu içerir. Fenol zayıf asit olduğundan NaOH ile de tepkime verir; alkoller yalnız aktif metallerle H₂ çıkarır. Örnek: etanol Na ile tepkime verir, NaOH ile vermez')],
 puf='Na ve NaOH ikisi de: fenol; yalnız Na: alkol; hiçbiri: eter.')

# ---------- yaz ----------
def bitir2(P,onek,k):
    P.ANA and [q_.__setitem__('kardes',None) for q_ in P.ANA]
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Kimya çıkmış soruları, MEB 12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(GD,'..','kartlar',f'ak{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir2(P,'aromatik',UK)
