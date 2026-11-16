"""TYT Biyoloji · Canlıların Temel Bileşenleri · ek paket (bilesenleriki): 30 soru, kardeş yok, ipucu 1.
Sayısal cevaplar, çeldirici değerleri, öncül doğrulukları ve şekil verileri Python'da hesaplanır/assert edilir;
öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır, anahtar/adım/çeldirici açıklamaları oradan üretilir."""
import sys,os,math,itertools
BD=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,BD)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Canlıların Temel Bileşenleri'; UK='bio|Canlıların Temel Bileşenleri'
H.KONU=KONU_
P=Parti('bilesenleriki',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji dağılımı (yalnız mantık) · MEB 9. sınıf Canlıların Temel Bileşenleri'
TIP={'ino':('inorganik','İnorganik bileşikler ve suyun özellikleri'),'kar':('karbonhidrat','Karbonhidratlar ve su hesapları'),
     'lip':('lipit','Lipitlerin yapısı ve çeşitleri'),'pro':('protein','Proteinlerin yapısı ve peptit bağı'),
     'enz':('enzim','Enzimler, grafik ve deney yorumu'),'vit':('vitamin','Vitaminler'),
     'nuk':('nukleik','Nükleik asitler ve nükleotit hesapları'),'atp':('atp','ATP')}
TIPNO={}
for n in ('01','02','03'): TIPNO[n]='ino'
for n in ('04','05','06','07'): TIPNO[n]='kar'
for n in ('08','09','10','11'): TIPNO[n]='lip'
for n in ('12','13','14'): TIPNO[n]='pro'
for n in ('15','16','17','18','19','20','21'): TIPNO[n]='enz'
for n in ('22','23'): TIPNO[n]='vit'
for n in ('24','25','26','27','28'): TIPNO[n]='nuk'
for n in ('29','30'): TIPNO[n]='atp'
assert len(TIPNO)==30
def q(no,ad,fikir,tuzak,ne,**k):
    n=no[-2:]; sl,tp=TIP[TIPNO[n]]
    assert len(k['ip'])==1
    kart(f'K-BYTB2-{n}',k['alt'],fikir,tuzak,k['z'],k['kalip'],len(ad),f'by-tb2-{sl}',tp,KY)
    k['tipId']=f'by-tb2-{sl}'; k['tip']=tp; k['kart']=f'K-BYTB2-{n} ({tp.lower()}) · {ne}'
    mk(P,no,ad=ad,adim=len(ad),**k)
def say():
    from collections import Counter
    return Counter(x['cevap']['sik'] for x in P.ANA)
def sec_harf(izinli='ABCDE'):
    c=say(); m=min(c[h] for h in izinli); aday=[h for h in izinli if c[h]==m]
    return aday[len(P.ANA)%len(aday)]
def cap(s): return ('İ' if s[0]=='i' else s[0].upper())+s[1:]
def tekli(dogru,yanlislar,hedef=True):
    """dogru=(metin,neden); yanlislar=[(metin,neden)]*4. hedef True: tek doğru ifade; False: tek yanlış ifade (yanlışlar aslında doğru ifadeler)."""
    assert len(yanlislar)==4
    h=sec_harf(); i='ABCDE'.index(h); sira=[m for m,_ in yanlislar]; sira.insert(i,dogru[0])
    if hedef: yan=[(m,f'Bu ifadeyi doğru sanmış; oysa {n}','bilgi') for m,n in yanlislar]
    else: yan=[(m,f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}','bilgi') for m,n in yanlislar]
    return dict(dogru=dogru[0],yan=yan,sira=sira)
ROM=['I','II','III']
def _ad(s): return ('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
def _an(s): return (len(s),tuple(ROM.index(x) for x in s))
def onc2(d,ask=True,hedef=None):
    """d={'I':(doğru_mu,'olgu cümlesi (küçük harfle, noktasız)')}; ask True: doğru olanlar, False: yanlış olanlar sorulur."""
    T=frozenset(k for k,v in d.items() if v[0]==ask)
    adaylar=sorted([tuple(c) for n in (1,2,3) for c in itertools.combinations(ROM[:len(d)],n)],key=_an)
    kt=_an(tuple(sorted(T,key=ROM.index))); assert T
    alt=[c for c in adaylar if _an(c)<kt]; ust=[c for c in adaylar if _an(c)>kt]
    uz=lambda c:len(frozenset(c)^T)
    fe=[h for h in range(5) if h<=len(alt) and 4-h<=len(ust)]; assert fe,(T,len(alt),len(ust))
    if hedef is None:
        c=say(); m=min(c['ABCDE'[h]] for h in fe); aday=[h for h in fe if c['ABCDE'[h]]==m]; hedef=aday[len(P.ANA)%len(aday)]
    assert hedef in fe,(hedef,fe)
    sa=sorted(alt,key=lambda c:(uz(c),-adaylar.index(c)))[:hedef]; su=sorted(ust,key=lambda c:(uz(c),adaylar.index(c)))[:4-hedef]
    ops=sorted(sa+[tuple(sorted(T,key=ROM.index))]+su,key=_an); assert len(ops)==5
    yan=[]
    for o in ops:
        W=frozenset(o)
        if W==T: continue
        p=[]
        for x in sorted(W-T,key=ROM.index): p.append(f'{x} öncülünü '+('doğru' if ask else 'yanlış')+f' sanmış; oysa {d[x][1]}')
        for x in sorted(T-W,key=ROM.index): p.append(f'{x} öncülünü '+('yanlış' if ask else 'doğru')+f' sanmış; oysa {d[x][1]}')
        yan.append((_ad(o),'. '.join(p)+'.','bilgi'))
    return dict(dogru=_ad(tuple(sorted(T,key=ROM.index))),yan=yan,sira=[_ad(o) for o in ops])
def adim_onc(d,k):
    return A(f'{k}. öncül',cap(d[k][1])+'.','doğru' if d[k][0] else 'yanlış')
def HEADT(): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
def tk(g,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,g))
def rozet(x,y,t): return f'\\node[draw,circle,inner sep=1.2pt,fill=white,font=\\small\\bfseries] at ({x},{y}) {{{t}}};'

# ======================= 01 · su özellikleri · kolay · olumsuz =======================
SUB=B('Suyun özellikleri','Su çözücüdür · Isı kapasitesi ve buharlaşma ısısı yüksektir · Su molekülleri birbirine tutunur (kohezyon) ve başka yüzeylere de tutunabilir (adezyon)')
r=tekli(('Hidrolize girmesi – Küçük moleküllerin birleşmesini sağlar',''),
 [('Çözücü olması – Besin ve atıkların kanla taşınmasını sağlar','su çözücü olduğundan çözdüğü besin ve atıkları taşımaya uygun ortam oluşturur.'),
  ('Isı kapasitesinin yüksek olması – Vücut sıcaklığının ani değişmesini önler','suyun ısı kapasitesi yüksek olduğundan sıcaklığı yavaş değişir.'),
  ('Kohezyon göstermesi – Bitkilerde suyun kökten yapraklara iletilmesine katkı sağlar','su molekülleri birbirine tutunduğundan sütun hâlinde iletilebilir.'),
  ('Buharlaşma ısısının yüksek olması – Terleyen canlının serinlemesine yardım eder','su buharlaşırken çok ısı alır ve yüzeyi soğutur.')],hedef=False)
q('0001',ad=[A('Özellikleri hatırla','Su çözücüdür; ısı kapasitesi ve buharlaşma ısısı yüksektir; molekülleri birbirine tutunur.','çözücülük · ısı kapasitesi · buharlaşma ısısı · kohezyon'),
 A('Eşleştirmeleri sına','Çözücülük taşımayı, yüksek ısı kapasitesi sıcaklık dengesini, yüksek buharlaşma ısısı serinlemeyi, kohezyon bitkide su iletimini açıklar.','dört eşleştirme biyolojik olarak uygun'),
 A('Kalan eşleştirmeyi incele','Hidroliz, suyun kullanılarak büyük molekülün parçalanmasıdır. Küçük moleküllerin birleşmesi ise su çıkışıyla giden dehidrasyon sentezidir.','Hidroliz: parçalanma · Dehidrasyon: birleşme'),
 A('Sonuç','Yanlış olan, hidrolizi birleştirme olayıyla eşleştiren ifadedir.','Hidroliz ↔ birleştirme: yanlış')],
 fikir='Suyun özelliği ile canlıdaki sonucu eşleştirilir; hidroliz ile dehidrasyon sentezi karıştırılır.',tuzak='Hidrolizi küçük moleküllerin birleşmesi sanmak.',ne='özellik–sonuç eşleştirmesi',
 alt='İnorganik Bileşikler',z='kolay',kaz='Suyun özelliklerini canlıdaki sonuçlarıyla ilişkilendirir.',kalip='düz',
 metin='Su, canlı vücudunda en fazla bulunan inorganik bileşiktir. Suyun çözücü olması, ısı kapasitesinin ve buharlaşma ısısının yüksek olması, molekülleri arasında kohezyonun bulunması gibi özellikleri canlılığın sürmesine katkı sağlar. Bir öğrenci, suyun bu özelliklerini canlılardaki sonuçlarıyla eşleştiriyor.\nBuna göre öğrencinin yaptığı eşleştirmelerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan eşleştirme.',ip=['Her şıkta özelliğin gerçekten o sonucu doğurup doğurmadığını sorgula.'],bilgi=[SUB],
 puf='Hidroliz parçalar (su harcanır), dehidrasyon sentezi birleştirir (su çıkar).')

# ======================= 02 · ısıtma grafiği · orta · öncüllü =======================
KS,LS=3,6
assert KS*2==LS and 20+KS*8==44 and 20+LS*8==68<100
d={'I':(True,'aynı ısıyla sıcaklığı daha yavaş artan sıvı, ısı kapasitesi daha yüksek olan sudur ve bu sıvı K’dır'),
   'II':(False,'aynı ısı miktarıyla sıcaklığı daha çok artan sıvı L’dir; K’nın sıcaklığı daha az artmıştır'),
   'III':(True,'suyun yüksek ısı kapasitesi, suyu bol bulunduran canlıların vücut sıcaklığının ani değişmesini engellemeye katkı sağlar')}
r=onc2(d,True)
def kap(x,ad,son):
    return (f'\\draw[line width=1.3pt] ({x-.9},2.6)--({x-.9},.7)--({x+.9},.7)--({x+.9},2.6);'
            f'\\fill[black,fill opacity=.10] ({x-.9},.7) rectangle ({x+.9},2.0);\\draw[line width=.8pt] ({x-.9},2.0)--({x+.9},2.0);'
            f'\\draw[line width=1.3pt] ({x-.55},.7)--({x-.7},.2)--({x+.7},.2)--({x+.55},.7);\\node at ({x},.42) {{ısıtıcı}};'
            f'\\node[font=\\bfseries] at ({x},3.0) {{{ad}}};\\node[anchor=north,text width=3.4cm,align=center] at ({x},-.1) {{Başlangıç: 20 °C\\\\[2pt]8. dakikada: \\textbf{{{son} °C}}}};')
SK2=tk(kap(0,'K',20+KS*8)+kap(4.2,'L',20+LS*8))
q('0002',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Isıtma düzeneğinden sıcaklık artışı karşılaştırılır; suyun yüksek ısı kapasitesi canlıdaki sonuca bağlanır.',tuzak='Sıcaklığı hızlı artan sıvının ısı kapasitesini daha büyük sanmak.',ne='su–zeytinyağı ısıtma düzeneği',
 alt='İnorganik Bileşikler',z='orta',kaz='Isı kapasitesi düzeneğinden suyun sıcaklığı dengeleyici etkisini yorumlar.',kalip='şekilli',
 metin='Özdeş iki kapta bulunan eşit kütleli saf su ve zeytinyağı, özdeş ısıtıcılarla aynı koşullarda ısıtılıyor ve sıvıların sıcaklığı zamana göre ölçülüyor. Düzenekler (K ve L) ile ölçülen sıcaklıklar şekilde gösterilmiştir. Sıvılardan biri su, diğeri zeytinyağıdır ve hiçbiri kaynamamıştır.\nI. K sıvısı sudur.\nII. Aynı ısı miktarıyla L sıvısının sıcaklığı, K sıvısınınkinden daha az artar.\nIII. Suyun bu özelliği, suyu bol bulunduran canlıların vücut sıcaklığının ani değişmesini engellemeye katkı sağlar.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Düzenekteki iki sıvının sıcaklık artışlarını karşılaştır.'],
 bilgi=[B('Isı kapasitesi','Bir maddenin sıcaklığını 1 °C değiştirmek için gereken ısıdır. Isı kapasitesi büyük olan madde, aynı ısı alındığında sıcaklığını daha az değiştirir. Örnek: deniz suyu, kumdan daha yavaş ısınır')],
 puf='Aynı ısıyla sıcaklığı yavaş artan madde, ısı kapasitesi yüksek olandır; su bu yüzden sıcaklık dengeleyicidir.',sekil=SK2)

# ======================= 03 · mineraller · orta · hikâyeli =======================
r=tekli(('Kalsiyum – Kan pıhtılaşmasında görev alır',''),
 [('Demir – Tiroksin hormonunun yapısına katılır','tiroksinin yapısında iyot bulunur; demir hemoglobinin yapısına katılır.'),
  ('İyot – Kemik ve dişlerin yapısına katılır','kemik ve dişlerin yapısında kalsiyum bulunur; iyot tiroksin hormonunun yapısına katılır.'),
  ('Magnezyum – Hemoglobinin yapısına katılır','hemoglobinde demir bulunur; magnezyum klorofilin yapısında yer alır.'),
  ('Kalsiyum – Klorofilin yapısına katılır','klorofilde magnezyum bulunur; kalsiyum kemik, diş ve kan pıhtılaşmasıyla ilgilidir.')])
q('0003',ad=[A('Minerali tanı','Mineraller inorganik bileşiklerdir; enerji vermez, yapıya katılır ya da düzenleyici görev yapar.','yapı + düzenleme'),
 A('Eşleştirmeleri sına','Demir hemoglobinde, iyot tiroksinde, magnezyum klorofilde bulunur; kalsiyum kemik–diş yapısında bulunur.','Fe: hemoglobin · I: tiroksin · Mg: klorofil'),
 A('Kalsiyumun görevini ekle','Kalsiyum ayrıca kan pıhtılaşması ve kas kasılmasında rol alır.','Ca: pıhtılaşma'),
 A('Sonuç','Yalnız kalsiyumun pıhtılaşmadaki görevi doğru verilmiştir.','Kalsiyum – kan pıhtılaşması')],
 fikir='Mineral–görev eşleştirmesi; her mineralin yapıya katıldığı molekül bilinir.',tuzak='Demir, iyot, magnezyum ve kalsiyumun görevlerini birbirine karıştırmak.',ne='mineral–görev eşleştirmesi',
 alt='İnorganik Bileşikler',z='kolay',kaz='Minerallerin canlıdaki görevlerini eşleştirir.',kalip='hikâyeli',
 metin='Bir diyetisyen, kan tahlilinde hemoglobin düzeyi düşük çıkan danışanına demir bakımından zengin besinleri önermiş; ayrıca iyot, kalsiyum ve magnezyum minerallerinin de yeterli alınması gerektiğini belirtmiştir. Mineraller inorganik bileşiklerdir ve enerji vermezler; ancak canlı vücudunda çeşitli yapılarda ve olaylarda görev alırlar.\nBuna göre minerallerle ilgili aşağıdaki eşleştirmelerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru eşleştirme.',ip=['Her mineralin görevini ayrı ayrı hatırla.'],
 bilgi=[B('Minerallerin görevleri','Mineraller inorganik bileşiklerdir; enerji vermez, yapıya katılır ya da düzenleyici görev yapar. Örnek: fosfor kemik ve dişlerde bulunur, sodyum ve potasyum sinir iletiminde rol alır')],
 puf='Mineral adını yapısına girdiği molekülle birlikte öğren: demir–hemoglobin, magnezyum–klorofil, iyot–tiroksin.')

# ======================= 04 · sükroz hidrolizi · kolay =======================
r=tekli(('Glikoz ve fruktoz oluşur; 1 molekül su harcanır.',''),
 [('Glikoz ve fruktoz oluşur; 1 molekül su açığa çıkar.','hidrolizde su harcanır; su çıkışı birleşme (dehidrasyon sentezi) olayında görülür.'),
  ('İki glikoz oluşur; 1 molekül su harcanır.','sükrozun yapısında glikozun yanında fruktoz bulunur; iki glikoz maltozun ürünüdür.'),
  ('Glikoz ve galaktoz oluşur; 1 molekül su harcanır.','glikoz ve galaktoz süt şekeri laktozun ürünleridir; sükroz glikoz ve fruktozdan oluşur.'),
  ('İki fruktoz oluşur; 2 molekül su harcanır.','disakkarit hidrolizinde tek bağ kopar ve 1 su harcanır; sükroz iki fruktozdan oluşmaz.')])
q('0004',ad=[A('Sükrozu tanı','Sükroz glikoz ve fruktozun dehidrasyon sentezi ile birleştiği bir disakkarittir.','sükroz = glikoz + fruktoz'),
 A('Hidrolizi yönlendir','Hidrolizde su harcanarak bağ kırılır ve yapıtaşları ayrılır; tek bağ olduğundan 1 su gerekir.','1 bağ → 1 su harcanır'),
 A('Sonuç','Sükrozun hidrolizinde glikoz ve fruktoz oluşur ve 1 molekül su harcanır.','glikoz + fruktoz · 1 su harcanır')],
 fikir='Disakkaritin hidrolizinde oluşan monosakkaritler ve suyun yönü sınanır.',tuzak='Hidrolizde su çıktığını sanmak; disakkaritleri (sükroz, maltoz, laktoz) karıştırmak.',ne='sükroz hidrolizi',
 alt='Karbonhidratlar',z='kolay',kaz='Disakkaritin hidrolizinde oluşan ürünleri ve suyun yönünü belirler.',kalip='hikâyeli',
 metin='Bir çocuk, çayına koyduğu sofra şekerini (sükroz) yedikten sonra sindirim sırasında sükrozun hidrolizle daha küçük şekerlere ayrıldığını öğreniyor. Sükroz iki monosakkaritin birleşmesiyle oluşmuş bir disakkarittir.\nBuna göre sükrozun hidrolizi ile ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Hidrolizin ürünleri ve suyun durumu.',ip=['Hidrolizde bağın nasıl kırıldığını ve sükrozu oluşturan monosakkaritlerin hangileri olduğunu hatırla.'],
 bilgi=[B('Karbonhidrat çeşitleri','Monosakkarit: tek şeker (glikoz, fruktoz, galaktoz) · Disakkarit: iki şeker (sükroz, maltoz, laktoz) · Polisakkarit: çok sayıda şeker (nişasta, glikojen)')],
 puf='Hidrolizde su girer, bağ kırılır, yapıtaşları serbest kalır.')

# ======================= 05 · tablo · orta · öncüllü =======================
d={'I':(True,'iki monosakkaritin birleşmesinde bir bağ kurulur ve bir su molekülü açığa çıkar'),
   'II':(False,'tek zincirli 150 monosakkaritte 149 bağ vardır; tam hidroliz için 149 su gerekir'),
   'III':(True,'tek şekerli bir monosakkarit hidrolizle daha basit şekerlere ayrılamaz')}
r=onc2(d,True); assert 150-1==149
q('0005',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Monosakkarit sayısından karbonhidrat türü belirlenir; sentez ve hidrolizde su sayısı hesaplanır.',tuzak='Hidrolizde gereken su sayısını monosakkarit sayısı kadar sanmak.',ne='X, Y, Z karbonhidratları',
 alt='Karbonhidratlar',z='orta',kaz='Monosakkarit sayısından karbonhidrat çeşidini ve su hesaplarını yorumlar.',kalip='öncüllü',
 metin='X, Y ve Z karbonhidratlarının birer molekülü sırasıyla 1, 2 ve 150 monosakkaritten oluşmaktadır. Y ve Z, dallanma göstermeyen tek zincirli yapıdadır.\nI. Y’nin bir molekülü oluşurken 1 molekül su açığa çıkar.\nII. Z’nin bir molekülü tam hidroliz edildiğinde 150 molekül su kullanılır.\nIII. X, hidrolizle daha küçük karbonhidratlara ayrılamaz.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Verilen sayılardan her karbonhidratın monosakkarit, disakkarit ya da polisakkarit olduğunu belirle.'],
 bilgi=[B('Karbonhidrat çeşitleri','Monosakkarit: tek şeker (glikoz) · Disakkarit: iki şeker (sükroz) · Polisakkarit: çok sayıda şeker (nişasta)')],
 puf='Sentezde de hidrolizde de su sayısı bağ sayısına eşittir.')

# ======================= 06 · glikojen · orta · olumsuz =======================
r=tekli(('Glikojenin sentezi, suyun harcandığı bir hidroliz tepkimesidir.',''),
 [('Makarnadaki nişasta, sindirimle glikoza kadar parçalanır.','nişasta bir polisakkarittir ve hidrolizle glikoza ayrılır.'),
  ('Kas ve karaciğer hücrelerinde depo edilen polisakkarit glikojendir.','hayvan hücrelerinde depo polisakkarit glikojendir.'),
  ('Kan şekeri düştüğünde glikojenin hidrolizi ile glikoz elde edilir.','glikojen hidrolizle glikoz birimlerine ayrılır.'),
  ('Glikojenin yapıtaşı glikozdur ve sentezi sırasında su açığa çıkar.','glikojen sentezi dehidrasyon sentezidir ve su açığa çıkarır.')],hedef=False)
q('0006',ad=[A('Depo karbonhidratı bul','Hayvan hücreleri fazla glikozu glikojen olarak karaciğerde ve kasta depolar.','depo polisakkarit: glikojen'),
 A('Yıkım ve yapımı ayır','Glikojenin glikoza ayrılması hidrolizdir (su harcanır). Glikozun glikojene çevrilmesi dehidrasyon sentezidir (su çıkar).','yıkım: hidroliz · yapım: dehidrasyon'),
 A('Şıkları sına','Nişastanın glikoza parçalanması, kas–karaciğer deposu, glikojenin hidrolizi ve yapıtaşı–su çıkışı ifadeleri doğrudur.','4 ifade doğru'),
 A('Sonuç','Sentezi hidroliz saymak yanlıştır; glikojen sentezinde su açığa çıkar.','Sentez ≠ hidroliz')],
 fikir='Depo polisakkaritin yapım ve yıkımında su akışı yön olarak ayırt edilir.',tuzak='Sentezi hidroliz, yıkımı dehidrasyon sanmak.',ne='maraton koşucusu ve depo glikojen',
 alt='Karbonhidratlar',z='orta',kaz='Depo polisakkaritlerin yapım ve yıkımını hidroliz–dehidrasyon açısından ayırt eder.',kalip='hikâyeli',
 metin='Bir maraton koşucusu yarıştan önceki günlerde makarna ağırlıklı beslenerek kas ve karaciğer hücrelerindeki depo karbonhidrat miktarını artırmaya çalışıyor. Yarış sırasında kan şekeri düştüğünde bu depolardan yararlanılıyor.\nBuna göre bu olaylarla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Depo polisakkaritin glikoza ayrılmasında ve yeniden depolanmasında suyun yönünü ayrı ayrı düşün.'],
 bilgi=[B('Depo polisakkaritler','Bitkilerde nişasta, hayvanlarda glikojen depo edilir. Hidrolizde su harcanır ve zincir parçalanır; dehidrasyon sentezinde su açığa çıkar ve zincir büyür')],
 puf='Yıkım = hidroliz (su girer), yapım = dehidrasyon sentezi (su çıkar).')

# ======================= 07 · polisakkarit zincirleri · zor · sayı =======================
toplam=100; su=96; zin=toplam-su; assert zin==4
x40=40; kalan=toplam-x40; zk=zin-1; assert zk==3 and kalan%zk==0; es=kalan//zk; assert es==20; hid=es-1
assert hid==19 and (toplam//zin)-1==24 and (kalan//zin)-1==14 and kalan-1==59 and es==20
q('0007',ad=[A('Zincir sayısını bul','Dallanmamış zincirlerde su sayısı = glikoz sayısı − zincir sayısıdır.','100 − 96 = 4 zincir'),
 A('Eşit zincirleri ayır','Dört zincirden biri 40 glikozludur; kalan 3 zincir eşit uzunluktadır.','100 − 40 = 60 glikoz · 3 zincir'),
 A('Bir zincirin uzunluğu','Eşit zincirlerin her biri aynı sayıda glikoz taşır.','60 ÷ 3 = 20 glikoz'),
 A('Hidroliz suyunu hesapla','Tek zincirin tam hidrolizinde, bağ sayısı kadar su gerekir.','20 − 1 = 19 su'),
 A('Sonuç','Eşit uzunluktaki bir zincirin tam hidrolizi için 19 su gerekir.','19')],
 fikir='Toplam glikoz ve su sayısından zincir sayısı bulunur; zincir uzunluğundan hidroliz suyu hesaplanır.',tuzak='Zincir sayısını bulmadan toplam glikozu bölmek; bağ sayısı yerine glikoz sayısını almak.',ne='zincir sayısı ve hidroliz suyu',
 alt='Karbonhidratlar',z='zor',kaz='Su çıkışından zincir sayısını bulup zincir uzunluğu ve hidroliz suyunu hesaplar.',kalip='yeni nesil',
 metin='Bir hücrede toplam 100 glikoz molekülü kullanılarak dallanmamış polisakkarit zincirleri sentezleniyor ve bu sentez sırasında 96 molekül su açığa çıkıyor. Oluşan zincirlerden biri 40 glikozludur; diğer zincirlerin hepsi eşit sayıda glikozdan oluşmuştur.\nBuna göre eşit uzunluktaki zincirlerden birinin tam hidrolizi için kaç molekül su gerekir?',
 dogru=19,yan=[(14,'Kalan 60 glikozu 4 zincire bölmüş (15 glikoz) ve 15 − 1 almış; 40’lık zinciri eşit zincirlerden saymış.','dikkat'),(20,'Hidroliz suyunu zincirdeki glikoz sayısına eşitlemiş; bağ sayısı 1 eksiktir.','bilgi'),(24,'40’lık zinciri hesaba katmadan 100 glikozu 4 eşit zincire bölmüş (25 glikoz) ve 25 − 1 almış.','dikkat'),(59,'Kalan üç zinciri tek zincir saymış (60 − 1).','islem')],
 istenen='Bir eşit zincirin tam hidrolizi için gereken su sayısı.',ip=['Önce su ve glikoz sayısından zincir sayısını bul.'],
 bilgi=[B('Zincir ve su','Dallanmamış zincirlerde bağ sayısı, zincir sayısına bağlıdır. Sentezde su açığa çıkar, hidrolizde su harcanır')],
 puf='Su sayısı = birim sayısı − zincir sayısı; bu bağıntıyı ters yönde de kullan.')

# ======================= 08 · yağ asitleri şekli · kolay =======================
def zigzag(y0,cift=None,n=11):
    pts=[(0.95+0.5*i,y0+0.28*(i%2)) for i in range(n)]; o=''
    for i in range(n-1):
        (x1,y1),(x2,y2)=pts[i],pts[i+1]
        if cift==i:
            dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy); nx,ny=-dy/L*0.045,dx/L*0.045
            for s in (1,-1): o+=f'\\draw[line width=1.2pt] ({x1+s*nx:.3f},{y1+s*ny:.3f})--({x2+s*nx:.3f},{y2+s*ny:.3f});'
        else: o+=f'\\draw[line width=1.2pt] ({x1:.3f},{y1:.3f})--({x2:.3f},{y2:.3f});'
    return o,pts
CIFT=4
o1,_=zigzag(1.2); o2,_=zigzag(0.0,CIFT)
g=o1+o2+''.join(f'\\node[anchor=east] at (0.93,{y}) {{COOH}};' for y in (1.2,0.0))+rozet(-0.45,1.2,'I')+rozet(-0.45,0.0,'II')
SK8=tk(g)
r=tekli(('II numaralı yağ asidi doymamıştır; yağı oda sıcaklığında genellikle sıvıdır.',''),
 [('I numaralı yağ asidi, yapısındaki bağlar nedeniyle doymamıştır.','I’de karbonlar arasında yalnız tekli bağ vardır; bu nedenle doymuştur.'),
  ('I ve II numaralı yağ asitleri aynı sayıda hidrojen atomu taşır.','II’deki çift bağ nedeniyle bu yağ asidinde karbonlar daha az hidrojen bağlar.'),
  ('Doymamış yağ asitleri hayvansal yağlarda baskındır ve yağlar oda sıcaklığında katıdır.','doymamış yağ asitleri çoğunlukla bitkisel yağlarda bulunur ve bu yağlar oda sıcaklığında sıvıdır.'),
  ('Karbon sayıları eşit olduğundan iki yağ asidinin oda sıcaklığındaki hâli de aynıdır.','çift bağlı doymamış yağ asitleri sıkı paketlenemez; bu yağlar doymuş olanlara göre daha sıvıdır.')])
q('0008',ad=[A('Bağları oku','Şekilde karbon zincirinde I’de yalnız tekli bağ, II’de bir çift bağ vardır.','I: tekli bağlar · II: bir çift bağ'),
 A('Doymuşluğu belirle','Yalnız tekli bağ içeren yağ asidi doymuş, çift bağ içeren doymamıştır.','I: doymuş · II: doymamış'),
 A('Sonuçları yorumla','Çift bağlı yağ asidinde hidrojen sayısı daha azdır ve bu yağ asitleri daha gevşek dizildiğinden yağ oda sıcaklığında sıvıdır.','II: daha az H · sıvı yağ'),
 A('Sonuç','Doğru ifade, II’nin doymamış olduğunu ve yağın sıvı olduğunu söyler.','II: doymamış, sıvı yağ')],
 fikir='Yağ asidi çiziminden çift bağ okunur; doymamışlık hidrojen sayısı ve yağın hâliyle ilişkilendirilir.',tuzak='Doymamış yağ asidini hayvansal ve katı yağla ilişkilendirmek.',ne='doymuş ve doymamış yağ asidi çizimi',
 alt='Lipitler',z='kolay',kaz='Yağ asidi yapısından doymuşluğu belirleyip yağın hâliyle ilişkilendirir.',kalip='şekilli',
 metin='Şekilde, karbon sayıları eşit olan I ve II numaralı yağ asitlerinin yapıları gösterilmiştir. Zincirin her köşesi ve ucu bir karbon atomunu temsil eder; karbonlara bağlı hidrojen atomları gösterilmemiştir. Bu yağ asitleri, gliserolle birleşerek yağların yapısına katılabilir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Zincirdeki bağların türünü karşılaştır; çift bağın hidrojen sayısını nasıl etkilediğini düşün.'],
 bilgi=[B('Doymuş ve doymamış yağ asitleri','Karbonları arasında yalnız tekli bağ bulunan yağ asidi doymuş, en az bir çift bağ bulunan doymamıştır. Hayvansal yağlar çoğunlukla doymuş yağ asitleri taşır; zeytinyağı gibi bitkisel yağlarda doymamış yağ asitleri bol bulunur')],
 puf='Çift bağ gör: doymamış yağ asidi; daha az hidrojen, daha sıvı yağ.',sekil=SK8)

# ======================= 09 · fosfolipit çift katmanı · orta · öncüllü =======================
xs=[0.6*i for i in range(7)]; b=[]
for x in xs:
    b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.15] ({x:.2f},3.0) circle (.2);\\draw[line width=1pt] ({x:.2f},3.0) circle (.2);')
    b.append(f'\\draw[line width=1.1pt] ({x-.1:.2f},2.8)--({x-.1:.2f},1.5);\\draw[line width=1.1pt] ({x+.1:.2f},2.8)--({x+.1:.2f},1.5);')
    xb=x+0.3
    b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.15] ({xb:.2f},0.0) circle (.2);\\draw[line width=1pt] ({xb:.2f},0.0) circle (.2);')
    b.append(f'\\draw[line width=1.1pt] ({xb-.1:.2f},.2)--({xb-.1:.2f},1.5);\\draw[line width=1.1pt] ({xb+.1:.2f},.2)--({xb+.1:.2f},1.5);')
xr=xs[-1]
b.append(f'\\node[anchor=south] at (2.1,3.45) {{Sulu ortam}};\\node[anchor=north] at (2.1,-0.45) {{Sulu ortam}};')
b.append(f'\\node[font=\\small\\bfseries] at ({xr+1.2:.2f},3.0) {{K}};\\draw[-{{Stealth[length=2mm]}},line width=.8pt] ({xr+.95:.2f},3.0)--({xr+.28:.2f},3.0);')
b.append(f'\\node[font=\\small\\bfseries] at ({xr+1.2:.2f},2.2) {{L}};\\draw[-{{Stealth[length=2mm]}},line width=.8pt] ({xr+.95:.2f},2.2)--({xr+.14:.2f},2.2);')
SK9=tk('\n'.join(b))
d={'I':(True,'fosfolipitlerin fosfat taşıyan baş kısmı suyu sever'),
   'II':(True,'fosfolipitlerin kuyruk kısımları, suyu sevmeyen yağ asidi zincirleridir'),
   'III':(False,'çift katmanda suyu seven baş kısımlar sulu ortama dönüktür; yağ asidi uçları katmanın iç kısmında bulunur')}
r=onc2(d,True)
q('0009',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Fosfolipit çift katmanında baş ve kuyruk kısımlarının suyla ilişkisi yorumlanır.',tuzak='Yağ asidi uçlarının sulu ortama dönük olduğunu sanmak.',ne='fosfolipit çift katmanı şeması',
 alt='Lipitler',z='orta',kaz='Fosfolipit çift katmanında baş ve kuyruk kısımlarının özelliklerini yorumlar.',kalip='şekilli',
 metin='Şekilde, hücre zarının temel yapısını oluşturan fosfolipit çift katmanının bir bölümü gösterilmiştir. Çift katmanın iki yüzü de sulu ortamla çevrilidir. Fosfolipitlerin bir ucu fosfat taşırken diğer ucunda iki yağ asidi zinciri bulunur.\nI. K ile gösterilen kısım suyu sever.\nII. L ile gösterilen kısımlar yağ asidi zincirleridir.\nIII. L ile gösterilen kısımlar sulu ortama dönüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Şekilde hangi uçların sulu ortama baktığına ve hangi uçların katmanın içinde kaldığına bak.'],
 bilgi=[B('Fosfolipit','Gliserole bağlı iki yağ asidi ve bir fosfat grubundan oluşur. Fosfatlı baş suyu sever, yağ asidi kuyrukları suyu sevmez. Bu yapı hücre zarının çift katmanlı olmasını sağlar')],
 puf='Baş sulu ortama, kuyruk katmanın içine döner: suyu sevenler dışta, sevmeyenler içte.',sekil=SK9)

# ======================= 10 · trigliserit · zor · sayı =======================
gl,ya=4,10; tg=min(gl,ya//3); su10=3*tg
assert tg==3 and su10==9 and (tg,gl,ya,3*gl)==(3,4,10,12)
q('0010',ad=[A('Yağın yapısı','Bir yağ molekülü (trigliserit), 1 gliserol ile 3 yağ asidinin birleşmesiyle oluşur; her yağ asidi bir su çıkışıyla bağlanır.','1 gliserol + 3 yağ asidi → 1 yağ + 3 su'),
 A('Yağ asidinden hesapla','10 yağ asidi, 3’erli gruplarla en fazla 3 yağ molekülü oluşturur; 1 yağ asidi artar.','10 ÷ 3 → 3 yağ (9 yağ asidi)'),
 A('Gliserolü kontrol et','3 yağ molekülü için 3 gliserol yeterlidir; 4 gliserolün biri artar.','3 ≤ 4 gliserol'),
 A('Suyu hesapla','Her yağ molekülünde 3 yağ asidi bağlandığından 3 su açığa çıkar.','3 × 3 = 9 su'),
 A('Sonuç','En fazla 9 molekül su açığa çıkar.','9')],
 fikir='Sınırlayıcı madde (yağ asidi) bulunur; oluşan yağ sayısından açığa çıkan su hesaplanır.',tuzak='Artan maddeyi hesaba katmak; gliserol sayısına göre ya da yağ asidi sayısına göre su saymak.',ne='gliserol ve yağ asidinden yağ sentezi',
 alt='Lipitler',z='zor',kaz='Sınırlayıcı maddeyi bularak yağ sentezinde açığa çıkan su sayısını hesaplar.',kalip='yeni nesil',
 metin='Bir yağ hücresinde, yağ sentezi için kullanılabilecek 4 gliserol ve 10 yağ asidi molekülü bulunmaktadır. Her yağ molekülü, 1 gliserol ile 3 yağ asidinin dehidrasyon sentezi ile oluşmakta ve bütün koşullar sentez için uygundur.\nBuna göre bu hücrede en fazla kaç molekül su açığa çıkabilir?',
 dogru=9,yan=[(3,'Su sayısı yerine oluşan yağ molekülü sayısını yazmış.','dikkat'),(4,'Su sayısını gliserol sayısına eşitlemiş; oysa her yağ molekülünde 3 su çıkar.','bilgi'),(10,'Su sayısını yağ asidi sayısına eşitlemiş; kalan yağ asidi bağlanmadığından 10 su çıkmaz.','dikkat'),(12,'4 gliserolün hepsinin 3’er yağ asidiyle bağlandığını sanmış; oysa yağ asidi yetmez.','islem')],
 istenen='Açığa çıkabilecek en fazla su sayısı.',ip=['Bir yağ molekülü için kaç yağ asidi gerektiğini düşün.'],
 bilgi=[B('Yağın yapısı','Yağlar gliserol ve yağ asitlerinden oluşur. Gliserole bağlanan her yağ asidi için dehidrasyon sentezi gerçekleşir. Örnek: 1 gliserol ile 2 yağ asidi birleşirse 2 su açığa çıkar')],
 puf='Madde sayılarını tepkimedeki oranlarla karşılaştırıp suyu oluşan ürün sayısından hesapla.')

# ======================= 11 · lipit nitel · orta · öncüllü =======================
d={'I':(False,'steroitler halkalı yapılıdır; gliserol ve yağ asitlerinden oluşmaz (kolesterol bir steroittir)'),
   'II':(True,'yağlar, aynı kütledeki karbonhidratlardan daha fazla enerji verir'),
   'III':(True,'yağ tabakası ısı yalıtımı sağlayarak vücut sıcaklığının korunmasına yardım eder')}
r=onc2(d,True)
q('0011',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Steroit, yağ ve enerji ilişkisi üç yargı üzerinden sınanır.',tuzak='Steroitleri gliserol ve yağ asidinden oluşan yağlarla karıştırmak.',ne='kış uykusu, yağ ve steroit yargıları',
 alt='Lipitler',z='orta',kaz='Yağların ve steroitlerin yapı ve görevlerini ayırt eder.',kalip='öncüllü',
 metin='Kış uykusuna yatacak olan bir ayı, uykudan önceki aylarda yoğun beslenerek vücudunda yağ biriktirir. Ayının kolesterol gibi steroitleri de vardır. Bu canlının lipitlerinin yapı ve görevleriyle ilgili,\nI. Steroitler, gliserol ve yağ asitlerinin birleşmesiyle oluşur.\nII. Yağlar, aynı kütledeki karbonhidratlardan daha fazla enerji verir.\nIII. Deri altındaki yağ tabakası, ısı yalıtımı sağlayarak vücut sıcaklığının korunmasına yardım eder.\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Steroitlerin yağlardan farklı bir yapıya sahip olup olmadığını hatırla.'],
 bilgi=[B('Lipit çeşitleri','Yağlar gliserol ve yağ asitlerinden oluşur; enerji deposudur ve ısı yalıtımı sağlar. Steroitler halkalı yapılı lipitlerdir; kolesterol hücre zarında bulunur, bazı hormonlar da steroit yapılıdır')],
 puf='Steroit = halkalı lipit; yağ = gliserol + yağ asitleri. İkisini ayrı tut.')

# ======================= 12 · amino asit şekli · kolay =======================
g=('\\node at (0,0) {C};\\node at (-1.75,0) {H$_2$N};\\node at (1.85,0) {COOH};\\node at (0,1.55) {R};\\node at (0,-1.3) {H};'
   '\\draw[line width=1.2pt] (-1.22,0)--(-.25,0);\\draw[line width=1.2pt] (.25,0)--(1.22,0);\\draw[line width=1.2pt] (0,.25)--(0,1.2);\\draw[line width=1.2pt] (0,-.25)--(0,-1.0);'
   +rozet(-1.75,-1.1,'I')+'\\draw[line width=.8pt] (-1.75,-.83)--(-1.75,-.3);'
   +rozet(1.85,-1.1,'II')+'\\draw[line width=.8pt] (1.85,-.83)--(1.85,-.3);'
   +rozet(1.25,1.55,'III')+'\\draw[line width=.8pt] (1.0,1.55)--(.25,1.55);')
SK12=tk(g,1.3)
r=tekli(('I numaralı grup ile başka amino asidin II numaralı grubu arasında peptit bağı kurulur.',''),
 [('Amino asitleri birbirinden ayıran kısım II numaralı gruptur.','amino asitleri R grubu (III) ayırır; II karboksil grubudur ve bütün amino asitlerde ortaktır.'),
  ('Peptit bağı, III numaralı gruplar arasında kurulur.','peptit bağı bir amino grubu ile bir karboksil grubu arasında kurulur; III değişken yan zincirdir.'),
  ('Peptit bağı kurulurken amino asitlerin I numaralı grupları birbirine bağlanır.','peptit bağı bir amino grubu ile bir karboksil grubu arasındadır; iki amino grubu birleşmez.'),
  ('III numaralı kısım, bütün amino asitlerde aynıdır.','III (R grubu) amino asitten amino asite değişir; bu yüzden amino asit çeşidi oluşur.')])
q('0012',ad=[A('Grupları tanı','Şekilde I amino grubu, II karboksil grubu, III ise değişken R grubudur.','I: amino · II: karboksil · III: R'),
 A('Peptit bağını yerleştir','Peptit bağı, bir amino asidin karboksil grubu ile diğerinin amino grubu arasında kurulur ve bir su açığa çıkar.','karboksil + amino → peptit bağı + H₂O'),
 A('Çeşitliliği açıkla','Amino asitlerin birbirinden farkı yalnız R grubundandır; amino ve karboksil grupları ortaktır.','farklılık: R grubu'),
 A('Sonuç','Doğru ifade, amino ve karboksil grupları arasında peptit bağı kurulduğunu söyleyendir.','I ile II arasında bağ, su çıkar')],
 fikir='Amino asit çiziminde amino, karboksil ve R grubu tanınır; peptit bağının kurulduğu gruplar belirlenir.',tuzak='R grubunu peptit bağına katılan grup ya da bütün amino asitlerde ortak sanmak.',ne='numaralı amino asit gruplarının görevi',
 alt='Proteinler',z='kolay',kaz='Amino asidin gruplarını tanıyıp peptit bağının kurulduğu yerleri belirler.',kalip='şekilli',
 metin='Şekilde, bir amino asidin genel yapısı gösterilmiştir. Proteinlerin yapısına yaklaşık 20 çeşit amino asit katılır ve bu amino asitler birbirlerine peptit bağlarıyla bağlanır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Peptit bağı kurulurken hangi iki grubun tepkimeye girdiğini düşün.'],
 bilgi=[B('Amino asit yapısı','Her amino asitte bir amino grubu, bir karboksil grubu ve bir R (yan) grubu bulunur. R grubu amino asidin çeşidini belirler')],
 puf='Bağı kuran gruplar ortaktır (amino ve karboksil); amino asidi farklı yapan grup R’dir.',sekil=SK12)

# ======================= 13 · tripeptit çeşitliliği · orta · sayı =======================
CES=4; sayim=len(list(itertools.permutations(range(CES),3)))
assert sayim==24==CES*(CES-1)*(CES-2) and 6==math.factorial(3) and 12==CES*(CES-1) and 64==CES**3 and CES==4
q('0013',ad=[A('Konumları say','Tripeptitte üç konum vardır; her çeşit en fazla bir kez kullanılabilir. İlk konuma 4 çeşit amino asit yerleştirilebilir.','1. konum: 4 seçenek'),
 A('Kalan konumlar','İkinci konuma kalan 3 çeşitten biri, üçüncü konuma kalan 2 çeşitten biri gelir.','2. konum: 3 · 3. konum: 2'),
 A('Çarp','Dizilişi farklı peptitler farklı molekül sayıldığından seçenekler çarpılır.','4 × 3 × 2 = 24'),
 A('Sonuç','Farklı tripeptit çeşidi sayısı 24’tür.','24')],
 fikir='Amino asit çeşitleri ve dizilişinden oluşabilecek peptit çeşidi sayılır.',tuzak='Dizilişin peptiti değiştirdiğini unutmak ya da çeşitlerin tekrar kullanılabileceğini sanmak.',ne='dört çeşit amino asitten tripeptit çeşitliliği',
 alt='Proteinler',z='orta',kaz='Amino asit çeşidi ve diziliminden oluşabilecek peptit çeşidi sayısını hesaplar.',kalip='yeni nesil',
 metin='Bir deneyde X, Y, Z ve T olmak üzere dört çeşit amino asit kullanılarak üç amino asitten oluşan peptitler sentezleniyor. Her peptitte aynı çeşit amino asit en fazla bir kez bulunuyor. Amino asitlerin diziliş sırası farklı olan peptitler farklı moleküller sayılıyor.\nBuna göre bu deneyde en fazla kaç çeşit tripeptit sentezlenebilir?',
 dogru=24,yan=[(4,'Peptit çeşidini amino asit çeşidi sayısına eşitlemiş.','bilgi'),(6,'Üç amino asidin sıralanışını (3!) hesaplayıp hangi üçünün seçileceğini hesaba katmamış.','dikkat'),(12,'Yalnız iki konumu hesaba katmış (4 × 3).','islem'),(64,'Aynı çeşidin tekrar kullanılabileceğini sanmış (4 × 4 × 4).','dikkat')],
 istenen='Sentezlenebilecek tripeptit çeşidi sayısı.',ip=['Peptitteki her konuma kaç farklı amino asit çeşidinin gelebileceğini sırayla düşün.'],
 bilgi=[B('Protein çeşitliliği','Proteinler amino asitlerin sayısı, çeşidi ve diziliş sırasıyla farklılaşır. Dizilişi farklı olan peptitler farklı moleküllerdir')],
 puf='Konumları sırayla doldur: her konumda kalan seçenek sayısını çarp.')

# ======================= 14 · denatürasyon tüpleri · zor · öncüllü =======================
def tup(x,lv,op,alt,pul=False):
    s=(f'\\draw[line width=1.2pt] ({x-.35},2.1)--({x-.35},.35) arc(180:360:.35)--({x+.35},2.1);'
       f'\\fill[black,fill opacity={op}] ({x-.35},{lv})--({x-.35},.35) arc(180:360:.35)--({x+.35},{lv})--cycle;'
       f'\\draw[line width=.8pt] ({x-.35},{lv})--({x+.35},{lv});')
    if pul:
        for dx,dy in ((-.18,.55),(.12,.75),(-.05,1.0),(.2,.5),(-.2,.95)): s+=f'\\draw[line width=.8pt] ({x+dx-.06:.2f},{dy-.06:.2f})--({x+dx+.06:.2f},{dy+.06:.2f});'
    return s+f'\\node[anchor=north,text width=2.1cm,align=center] at ({x},-.1) {{{alt}}};'
TB=[('25 °C','Şeffaf',.06),('80 °C','Beyaz, katı',.22),('25 °C, HCl eklendi','Beyaz, katı',.22),('4 °C','Şeffaf',.06)]
g=''
for i,(kosul,gor,op) in enumerate(TB):
    x=2.3*i; g+=tup(x,1.35,op,kosul+'\\\\[2pt]\\textbf{'+gor+'}',pul=(gor!='Şeffaf'))+rozet(x,2.6,str(i+1))
SK14=tk(g)
d={'I':(True,'yüksek sıcaklık proteinin üç boyutlu yapısını bozar (denatürasyon) ve çözelti beyaz, katı hâle gelir'),
   'II':(True,'düşük sıcaklık proteini denatüre etmez; çözelti şeffaf kalmıştır'),
   'III':(False,'denatürasyonda peptit bağları kopmaz; yalnız üç boyutlu yapı bozulur ve amino asit dizilimi korunur')}
r=onc2(d,True)
q('0014',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Deney sonucundan denatürasyon belirlenir; denatürasyonun yalnız yapıyı bozduğu, peptit bağlarını kırmadığı sınanır.',tuzak='Denatürasyonda peptit bağlarının koptuğunu ve soğuğun da proteini bozduğunu sanmak.',ne='yumurta akı proteini ve tüp deneyi',
 alt='Proteinler',z='orta',kaz='Deney sonucundan denatürasyonu belirleyip yapıya etkisini yorumlar.',kalip='şekilli',
 metin='Bir öğrenci, aynı miktarda yumurta akı çözeltisini (albümin proteini) dört ayrı tüpe koyuyor. Tüplerin ortam koşullarını şekildeki gibi düzenleyip 10 dakika bekledikten sonra çözeltinin görünümünü kaydediyor.\nI. 2 numaralı tüpte albüminin üç boyutlu yapısı bozulmuştur.\nII. 4 numaralı tüpte albüminin yapısı bozulmamıştır.\nIII. 3 numaralı tüpte peptit bağlarının kopması sonucu amino asitler serbest kalmıştır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Görünümü değişen tüplerde proteinin hangi düzeyde değiştiğini düşün: yalnız şekil mi, yoksa bağlar mı?'],
 bilgi=[B('Denatürasyon','Yüksek sıcaklık, aşırı asit ya da baz gibi etkenlerle proteinin üç boyutlu yapısının bozulmasıdır; protein görevini yapamaz. Örnek: ısıtılan süte limon eklenince sütün kesilmesi')],
 puf='Denatürasyon yalnız üç boyutlu yapıyı bozar; peptit bağları ve amino asit dizilimi korunur.',sekil=SK14)

# ======================= 15 · aktivasyon enerjisi grafiği · kolay =======================
Rg,Pg=2.2,1.0
Sg=lambda x:1/(1+math.exp(-(x-3.8)*1.8))
Ek=lambda x,h:Rg+(Pg-Rg)*Sg(x)+h*math.exp(-((x-3.5)/0.95)**2)
xsr=[i*0.1 for i in range(0,76)]
pk=max(Ek(x,2.6) for x in xsr); pl=max(Ek(x,1.5) for x in xsr)
assert pk>pl>Rg>Pg and pk-Rg>pl-Rg
cK=' '.join(f'({x:.2f},{Ek(x,2.6):.2f})' for x in xsr[::3]); cL=' '.join(f'({x:.2f},{Ek(x,1.5):.2f})' for x in xsr[::3])
ar='<->,line width=.9pt'
g=(f'\\draw[-{{Stealth}},line width=1.1pt] (0,0)--(0,5.5);\\draw[-{{Stealth}},line width=1.1pt] (0,0)--(8.2,0);'
   '\\node[rotate=90] at (-.4,2.8) {Enerji};\\node at (4.1,-.5) {Tepkimenin ilerleyişi};'
   f'\\draw[line width=1.5pt] plot[smooth] coordinates {{{cK}}};\\draw[line width=1.5pt,vurgu] plot[smooth] coordinates {{{cL}}};'
   f'\\draw[dashed,line width=.6pt] (0,{Rg})--(9.9,{Rg});\\draw[dashed,line width=.6pt] (6.2,{Pg})--(9.9,{Pg});'
   f'\\draw[dashed,line width=.6pt] (3.5,{pk:.2f})--(8.2,{pk:.2f});\\draw[dashed,line width=.6pt] (3.5,{pl:.2f})--(9.0,{pl:.2f});'
   f'\\draw[{ar}] (8.2,{Rg})--(8.2,{pk:.2f});\\draw[{ar}] (9.0,{Rg})--(9.0,{pl:.2f});\\draw[{ar}] (9.9,{Rg})--(9.9,{Pg});'
   f'\\node[font=\\bfseries] at (8.2,{pk+.35:.2f}) {{a}};\\node[font=\\bfseries] at (9.0,{pl+.35:.2f}) {{b}};\\node[font=\\bfseries,anchor=west] at (10.05,{(Rg+Pg)/2}) {{c}};'
   f'\\node[font=\\bfseries] at (1.95,4.3) {{K}};\\draw[-{{Stealth[length=2mm]}},line width=.8pt] (2.15,4.05)--(2.6,{Ek(2.65,2.6)+.08:.2f});'
   f'\\node[font=\\bfseries,vurgu] at (2.6,1.6) {{L}};\\draw[-{{Stealth[length=2mm]}},line width=.8pt,vurgu] (2.6,1.85)--(2.6,{Ek(2.6,1.5)-.08:.2f});')
SK15=tk(g,.72)
r=tekli(('Enzim, a ile gösterilen enerjiyi b düzeyine indirir.',''),
 [('L eğrisi, enzimsiz tepkimeye aittir.','enzim aktivasyon enerjisini düşürür; enerji tepesi daha alçak olan L enzimli tepkimedir.'),
  ('Enzim, c ile gösterilen enerji farkını artırır.','enzim girenlerin ve ürünlerin enerjisini değiştirmez; c iki durumda da aynıdır.'),
  ('b, enzimli tepkimede ürünlerin enerjisini gösterir.','b enzimli tepkimenin aktivasyon enerjisini gösterir; ürünlerin enerjisi eğrilerin bitiş düzeyinden okunur.'),
  ('Enzim, tepkimeye giren maddelerin toplam enerjisini düşürür.','enzim girenlerin enerjisini değil, tepkimenin başlaması için gereken enerjiyi azaltır.')])
q('0015',ad=[A('Eğrileri oku','Aynı başlangıç ve bitiş düzeyine sahip iki eğriden K’nın enerji tepesi daha yüksek, L’nin daha alçaktır.','K tepesi > L tepesi'),
 A('Enzimli tepkimeyi belirle','Enzim aktivasyon enerjisini düşürdüğünden enerji tepesi alçak olan L enzimli tepkimedir.','L: enzimli · K: enzimsiz'),
 A('Oklara bak','a enzimsiz, b enzimli tepkimenin aktivasyon enerjisidir; c giren ile ürün arasındaki enerji farkıdır ve değişmez.','a > b; c sabit'),
 A('Sonuç','Enzim, aktivasyon enerjisini a düzeyinden b düzeyine indirir.','a → b')],
 fikir='Enerji–tepkime grafiğinde enzimli ve enzimsiz eğri ayırt edilir; aktivasyon enerjisi ve giren–ürün farkı yorumlanır.',tuzak='Enzimin giren ürün enerji farkını ya da girenlerin enerjisini değiştirdiğini sanmak.',ne='enzimli–enzimsiz enerji grafiği',
 alt='Enzimler',z='kolay',kaz='Aktivasyon enerjisi grafiğini okuyup enzimin etkisini yorumlar.',kalip='grafik',
 metin='Şekilde, aynı tepkimenin enzimli ve enzimsiz olarak gerçekleştiği iki durumdaki enerji değişimi K ve L eğrileriyle gösterilmiştir. a, b ve c ile gösterilen oklar enerji farklarını belirtmektedir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['a, b ve c oklarının neyi gösterdiğini oku.'],
 bilgi=[B('Aktivasyon enerjisi','Bir tepkimenin başlaması için gereken en az enerjidir. Enzim bu enerjiyi düşürerek tepkimeyi hızlandırır; giren ve ürünlerin enerjisini değiştirmez')],
 puf='Enzim yalnız tepkimenin tepesini alçaltır; başlangıç ve bitiş düzeyleri aynı kalır.',sekil=SK15)

# ======================= 16 · enzim–substrat uyumu · orta · öncüllü =======================
g=('\\draw[line width=1.4pt,fill=black,fill opacity=.12] (0,0)--(3.2,0)--(3.2,1.7)--(2.2,1.7)--(2.0,.95)--(1.2,.95)--(1.0,1.7)--(0,1.7)--cycle;'
   '\\draw[line width=1.4pt] (0,0)--(3.2,0)--(3.2,1.7)--(2.2,1.7)--(2.0,.95)--(1.2,.95)--(1.0,1.7)--(0,1.7)--cycle;'
   '\\node[font=\\normalsize\\bfseries] at (1.6,.45) {Enzim};'
   '\\draw[line width=1.4pt] (4.5,2.6)--(5.7,2.6)--(5.5,1.85)--(4.7,1.85)--cycle;\\node[font=\\bfseries] at (6.3,2.22) {K};'
   '\\draw[line width=1.4pt] (5.1,.95) circle (.45);\\node[font=\\bfseries] at (6.3,.95) {L};'
   '\\draw[line width=1.4pt] (4.5,-.55)--(5.7,-.55)--(5.1,.2)--cycle;\\node[font=\\bfseries] at (6.3,-.2) {M};')
SK16=tk(g,1.15)
d={'I':(True,'K maddesinin biçimi enzimin aktif bölgesiyle uyumludur; enzim yalnız bu maddeye etki eder'),
   'II':(False,'enzimler özgüldür; L ve M bu enzimin substratı değildir ve aktif bölgeye uymadığından ürüne dönüştürülemez'),
   'III':(True,'enzim, tepkime sonunda değişmeden kalır ve yeniden kullanılabilir')}
r=onc2(d,True)
q('0016',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Aktif bölge ile madde biçimleri karşılaştırılarak enzimin özgüllüğü ve yeniden kullanılabilirliği yorumlanır.',tuzak='Enzimin birden çok farklı maddeyi ürüne dönüştürebildiğini ya da tepkimede harcandığını sanmak.',ne='enzim ve üç maddenin biçimleri',
 alt='Enzimler',z='orta',kaz='Enzim–substrat uyumundan enzimin özgüllüğünü yorumlar.',kalip='şekilli',
 metin='Şekilde, aktif bölgesi girinti olarak gösterilen bir enzim ile K, L ve M maddeleri verilmiştir. Ortamda yalnız bu enzim ve K, L, M maddeleri bulunmaktadır.\nI. K maddesi, bu enzimin substratıdır.\nII. L ve M maddeleri de bu enzimle ürüne dönüştürülebilir.\nIII. K ürüne dönüştükten sonra enzim, yeniden kullanılabilir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Aktif bölgenin biçimini madde biçimleriyle tek tek karşılaştır.'],
 bilgi=[B('Enzim–substrat uyumu','Enzimin aktif bölgesi yalnız biçimce uyan maddeye (substrata) bağlanır. Enzim tepkime sonunda değişmeden kalır ve yeni substratlarla yeniden çalışır')],
 puf='Aktif bölgeye biçimce uyan tek madde substrattır; enzim tepkimede harcanmaz.',sekil=SK16)

# ======================= 17 · substrat derişimi · orta · öncüllü =======================
Km=3; VK,VL=40,80
vK=lambda s:VK*s/(Km+s); vL=lambda s:VL*s/(Km+s)
a_,b_=3,30
assert vK(a_)==20 and abs(vK(b_)-VK)/VK<.1 and (vK(36)-vK(30))/vK(30)<.02 and vL(a_)==40 and vL(b_)>vK(VK)
cK=' '.join(f'({s/2:.1f},{vK(s/2):.2f})' for s in range(0,73)); cL=' '.join(f'({s/2:.1f},{vL(s/2):.2f})' for s in range(0,73))
b=['\\begin{axis}[width=7.4cm,height=5.2cm,xmin=0,xmax=40,ymin=0,ymax=90,xtick={3,30},xticklabels={a,b},ytick={0},axis lines=left,xlabel={Substrat derişimi},ylabel={Tepkime hızı},tick label style={font=\\small\\bfseries},label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
   f'\\addplot[black,smooth] coordinates {{{cK}}};\\addplot[vurgu,smooth] coordinates {{{cL}}};',
   '\\draw[dotted,line width=.7pt] (axis cs:3,0)--(axis cs:3,85);\\draw[dotted,line width=.7pt] (axis cs:30,0)--(axis cs:30,85);',
   '\\node[font=\\small\\bfseries,anchor=west] at (axis cs:36.3,43) {K};\\node[font=\\small\\bfseries,vurgu,anchor=west] at (axis cs:36.3,81) {L};','\\end{axis}']
SK17=tk('\n'.join(b))
d={'I':(True,'maksimum hızı daha yüksek olan L ortamında enzim miktarı K ortamındakinden fazladır'),
   'II':(True,'a derişiminde hız substrat arttıkça yükselmektedir; bu nedenle hızı sınırlayan etken substrat derişimidir'),
   'III':(False,'b derişiminde K’nın hızı en yüksek değere yaklaşmıştır; substrat eklemek hızı belirgin artırmaz, hızı sınırlayan etken enzim miktarıdır')}
r=onc2(d,True)
q('0017',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Substrat derişimi–hız grafiğinde sınırlayıcı etken ve enzim miktarı etkisi yorumlanır.',tuzak='Doyum bölgesinde substrat artışının hızı artırdığını sanmak.',ne='iki enzim miktarı için hız–substrat grafiği',
 alt='Enzimler',z='orta',kaz='Substrat derişimi grafiğinde hızı sınırlayan etkeni belirler.',kalip='grafik',
 metin='Bir enzimin tepkime hızı, aynı sıcaklık ve pH’ta iki ayrı ortamda (K ve L) farklı substrat derişimleri için ölçülmüş ve sonuçlar şekildeki grafikte gösterilmiştir. Ortamlardan birinde enzim miktarı diğerinin iki katıdır; başka bütün koşullar aynıdır.\nI. L ortamındaki enzim miktarı, K ortamındakinden fazladır.\nII. a derişiminde her iki ortamda da hızı sınırlayan etken substrat derişimidir.\nIII. K ortamında b derişiminde substrat eklenmesi, hızı belirgin biçimde artırır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Eğrilerin yükseldiği ve yatay seyrettiği bölgelerde hızı neyin belirlediğini ayrı ayrı düşün.'],
 bilgi=[B('Substrat derişimi ve hız','Enzim miktarı sabitken substrat arttıkça hız önce artar; tüm enzimler substrata bağlanınca hız en yüksek değerde sabitlenir(doyma)')],
 puf='Eğri yükseliyorsa sınırlayıcı substrattır; eğri yataylaştıysa enzim miktarıdır.',sekil=SK17)

# ======================= 18 · pH ve enzim · orta · olumsuz =======================
r=tekli(('pH 5 ortamında iki enzim de optimum etkinliğine yakın çalışır.',''),
 [('X enziminin etkinliği, pH 2 ortamında Y enziminin etkinliğinden yüksektir.','X enzimi pH 2’de en yüksek etkinliğe ulaşır; Y pH 2’de optimumundan uzaktır.'),
  ('Y enzimi, mide özsuyunun pH değerine yakın ortamda etkinliğini büyük ölçüde yitirir.','Y’nin optimum pH’ı 8’dir; pH 2’de etkinliği çok düşüktür.'),
  ('X enzimi, ince bağırsağın pH değerine yakın bir ortamda etkinlik gösteremez.','X’in optimum pH’ı 2’dir; pH 8’de etkinliği çok düşüktür.'),
  ('Enzimlerin etkinliği ortamın pH değerinden etkilenir.','her enzimin etkinliği optimum pH değerinde en yüksektir ve pH değiştikçe azalır.')],hedef=False)
q('0018',ad=[A('Verileri oku','X pH 2’de, Y pH 8’de en yüksek etkinliğe sahiptir; ikisi de optimum pH’tan uzaklaştıkça etkinliğini kaybeder.','X: optimum pH 2 · Y: optimum pH 8'),
 A('Şıkları sına','pH 2’de X daha etkindir; Y mide ortamında, X ince bağırsak ortamında etkinliğini yitirir; pH etkinliği değiştirir.','4 ifade verilerle uyumlu'),
 A('Kalan ifadeyi incele','pH 5, iki enzimin de optimum pH değerlerinden uzaktır; etkinlikleri ihmal edilebilir düzeydedir.','pH 5: iki enzim de etkisiz'),
 A('Sonuç','İki enzimin de pH 5’te optimuma yakın çalıştığını söyleyen ifade yanlıştır.','pH 5 ≠ optimum')],
 fikir='Optimum pH verilerinden enzim etkinliğinin pH ile değişimi yorumlanır.',tuzak='Etkinliğin pH ile değişmediğini ya da iki enzimin aynı pH’ta çalıştığını sanmak.',ne='mide ve ince bağırsak enzimleri',
 alt='Enzimler',z='orta',kaz='Enzim etkinliğinin pH ile ilişkisini yorumlar.',kalip='hikâyeli',
 metin='Bir araştırmacı, biri mide özsuyunda (pH yaklaşık 2), diğeri ince bağırsakta (pH yaklaşık 8) çalışan X ve Y enzimlerinin etkinliğini farklı pH değerlerinde ölçüyor. X enzimi en yüksek etkinliğini pH 2’de, Y enzimi ise pH 8’de gösteriyor. Her iki enzim de kendi optimum pH değerinden uzaklaştıkça etkinliğini kaybediyor ve pH 5’te ikisinin de etkinliği çok düşük kalıyor.\nBuna göre bu enzimlerle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Her enzimin etkinliğinin en yüksek olduğu pH değerini ve diğer pH değerlerindeki durumunu karşılaştır.'],
 bilgi=[B('Enzim ve pH','Her enzimin etkinliğinin en yüksek olduğu bir optimum pH değeri vardır. pH bu değerden uzaklaştıkça etkinlik azalır')],
 puf='Etkinlik optimum pH’ta tepe yapar, iki yönde de azalır.')

# ======================= 19 · katalaz deneyi · zor · tek doğru =======================
def tup2(x,kosul,kopuk):
    s=tup(x,1.2,.08,kosul)
    for rr in range(kopuk):
        y=1.28+0.15*rr; n=3 if rr%2==0 else 2
        for j in range(n): s+=f'\\draw[line width=.7pt] ({x+(j-(n-1)/2)*0.2:.2f},{y:.2f}) circle (.085);'
    return s
KT=[('Çiğ karaciğer\\\\25 °C',4),('Kaynatılmış karaciğer\\\\25 °C',0),('Saf su\\\\25 °C',0),('Çiğ karaciğer\\\\0 °C (buz)',1)]
g=''.join(tup2(2.3*i,k,n)+rozet(2.3*i,2.6,str(i+1)) for i,(k,n) in enumerate(KT))
SK19=tk(g)
r=tekli(('1 ve 4 numaralı tüpler, sıcaklığın enzim etkinliğine etkisini gösterir.',''),
 [('2 numaralı tüpte köpürme olmaması, enzimin düşük sıcaklıkta çalışmamasından kaynaklanır.','2 numaralı tüp oda sıcaklığındadır; karaciğer kaynatıldığı için enzim yüksek sıcaklıkta denatüre olmuştur.'),
  ('3 numaralı tüpteki sonuç, enzimin tepkime sonunda harcandığını gösterir.','3 numaralı tüpte enzim yoktur; enzimler tepkimede harcanmaz, bu tüp enzimsiz kontrol grubudur.'),
  ('4 numaralı tüpteki az köpürme, enzimin buz banyosunda denatüre olduğunu gösterir.','düşük sıcaklık enzimi denatüre etmez; yalnızca etkinliğini ve tepkime hızını azaltır.'),
  ('1 numaralı tüpteki köpürme, H₂O₂’nin enzimsiz ayrıştığını gösterir.','köpürme, karaciğerdeki katalaz enziminin H₂O₂’yi ayrıştırmasıyla açığa çıkan oksijenden kaynaklanır.')])
q('0019',ad=[A('Deney düzeneğini oku','Çiğ karaciğer 25 °C’ta çok, 0 °C’ta az köpürtmüştür; kaynatılmış karaciğer ve saf su köpürtmemiştir.','1: çok · 4: az · 2 ve 3: yok'),
 A('Değişkenleri ayır','1 ve 4 yalnız sıcaklıkla, 1 ve 2 yalnız karaciğerin kaynatılmasıyla, 1 ve 3 yalnız karaciğerin varlığıyla ayrılır.','1–4: sıcaklık · 1–2: ısıl işlem · 1–3: enzim'),
 A('Şıkları sına','Kaynatma enzimi denatüre eder; düşük sıcaklık yalnız yavaşlatır; saf su kontrol grubudur; köpürme enzim etkisidir.','diğer ifadeler hatalı'),
 A('Sonuç','Yalnız 1 ve 4 numaralı tüpler sıcaklığın etkisini ayrı olarak gösterir.','1 ↔ 4: sıcaklık')],
 fikir='Deney düzeneğinde yalnız bir değişkenin farklı olduğu tüpler eşleştirilir; kontrol ve denatürasyon yorumlanır.',tuzak='Düşük sıcaklığı denatürasyonla, kaynatmayı düşük sıcaklık etkisiyle karıştırmak.',ne='katalaz ve H₂O₂ tüp deneyi',
 alt='Enzimler',z='zor',kaz='Enzim deneyinde değişkenleri ve kontrol grubunu belirleyip sonuçları yorumlar.',kalip='şekilli',
 metin='Karaciğer hücrelerinde bulunan katalaz enzimi, hidrojen peroksiti (H₂O₂) su ve oksijene ayrıştırır; açığa çıkan oksijen köpük oluşturur. Bir öğrenci, aynı miktarda H₂O₂ çözeltisi bulunan dört tüpe şekilde belirtilen maddeleri ekliyor ve koşulları sağlıyor. Karaciğer parçalarının kütleleri eşittir; köpük miktarı şekilde gösterilmiştir.\nBuna göre bu deneyle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Hangi iki tüpün birbirinden yalnız tek bir koşulla ayrıldığını bul.'],
 bilgi=[B('Deneyde değişkenler','Bir etkiyi sınamak için yalnız bir koşul değiştirilir (bağımsız değişken), diğerleri sabit tutulur. Tepkimenin gözlenen sonucu bağımlı değişkendir. Kontrol grubunda sınanan etken bulunmaz')],
 puf='Bir etkiyi görmek için yalnız o koşulu farklı olan tüpleri karşılaştır.',sekil=SK19)

# ======================= 20 · sıcaklık–ürün grafiği · zor · öncüllü =======================
c1=[(0,0),(10,40)]; c2=[(0,0),(4,100),(10,100)]; c3=[(0,0),(1.5,30),(10,30)]; c4=[(0,0),(0.5,4),(10,4)]
assert c1[1][1]<100 and c2[-1][1]==100 and c3[-1][1]==30
f=lambda c:' '.join(f'({x},{y})' for x,y in c)
b=['\\begin{axis}[width=7.4cm,height=5.2cm,xmin=0,xmax=11.3,ymin=0,ymax=115,xtick={0,2,4,6,8,10},ytick={0,50,100},axis lines=left,xlabel={Zaman (dk)},ylabel={Ürün miktarı (birim)},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt},clip=false]',
   f'\\addplot[black] coordinates {{{f(c1)}}};\\addplot[vurgu] coordinates {{{f(c2)}}};\\addplot[black,dashed] coordinates {{{f(c3)}}};\\addplot[vurgu,dashed,line width=2.2pt] coordinates {{{f(c4)}}};',
   '\\node[font=\\small\\bfseries,anchor=west] at (axis cs:10.3,40) {1};\\node[font=\\small\\bfseries,vurgu,anchor=west] at (axis cs:10.3,100) {2};\\node[font=\\small\\bfseries,anchor=west] at (axis cs:10.3,27) {3};\\node[font=\\small\\bfseries,vurgu,anchor=west] at (axis cs:10.3,11) {4};','\\end{axis}']
SK20=tk('\n'.join(b))
d={'I':(True,'1 numaralı tüpte enzim 10 °C’ta denatüre olmamıştır ve substrat kalmıştır; 37 °C’ta ürün oluşumu hızlanarak sürer'),
   'II':(False,'3 numaralı tüpte enzim 50 °C’ta denatüre olmuştur; sıcaklık düşürülse de enzim etkinliğini geri kazanmaz ve ürün miktarı artmaz'),
   'III':(True,'2 numaralı tüpte substrat tükendiği için ürün miktarı 100 birimde sabit kalır')}
r=onc2(d,True)
q('0020',ad=[A('Grafikten durumları çıkar','1’de ürün yavaş ve sürekli artıyor; 2’de ürün 100’de sabitleniyor; 3’te ürün erken durup 30’da kalıyor; 4’te ürün çok az.','1: yavaş · 2: substrat bitti · 3: erken durdu · 4: yok'),
 adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Ürün–zaman grafiğinde substrat tükenmesi ile enzim denatürasyonu ayırt edilir; sıcaklık değişince sonuçlar öngörülür.',tuzak='Ürünün durmasını her durumda substratın bitmesine bağlamak ya da denatürasyonun soğutmayla geri döneceğini sanmak.',ne='dört sıcaklıkta ürün–zaman grafiği',
 alt='Enzimler',z='zor',kaz='Sıcaklığın enzim etkinliğine etkisini ürün–zaman grafiğinde yorumlayıp sonraki durumu öngörür.',kalip='grafik',
 metin='Aynı miktarda enzim ve 100 birim substrat içeren dört tüp, 1 numaralı tüp 10 °C, 2 numaralı tüp 37 °C, 3 numaralı tüp 50 °C ve 4 numaralı tüp 80 °C’ta tutuluyor. Oluşan ürün miktarının zamanla değişimi şekildeki grafikte gösterilmiştir. Ürün miktarı 100 birime ulaşınca substrat tükenmektedir. 10. dakikada tüplerin tamamı 37 °C’a getirilip 20 dakika daha bekletiliyor.\nI. 1 numaralı tüpte ürün miktarı artmaya devam eder.\nII. 3 numaralı tüpte ürün miktarı artmaya devam eder.\nIII. 2 numaralı tüpte ürün miktarı 100 birimde kalır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Ürünün durduğu tüplerde nedenin substratın bitmesi mi, enzimin bozulması mı olduğunu ayrı ayrı değerlendir.'],
 bilgi=[B('Enzim ve sıcaklık','Enzimler sıcaklığa duyarlıdır: düşük sıcaklık etkinliği azaltır, çok yüksek sıcaklık yapıyı bozar')],
 puf='Ürün neden durdu? Substrat bittiyse enzim sağlamdır; enzim bozulduysa substrat kalmıştır.',sekil=SK20)

# ======================= 21 · kofaktör, koenzim · orta · öncüllü · olumsuz =======================
d={'I':(True,'koenzimler organik yapılı kofaktörlerdir; birçoğunun yapısında vitamin türevleri bulunur'),
   'II':(False,'Fe²⁺ ve Zn²⁺ gibi metal iyonları inorganik kofaktörlerdir; organik molekül değildir'),
   'III':(False,'kofaktörler enzime yardımcı olur; substrat gibi sürekli tüketilmez ve yeni substratlarla yeniden kullanılır')}
r=onc2(d,False)
q('0021',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Yanlış olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Kofaktör ve koenzim kavramları, yapılarıyla ve enzimle ilişkileriyle sınanır.',tuzak='Metal iyonlarını organik, kofaktörleri harcanan madde sanmak.',ne='kofaktör ve koenzim yargıları',
 alt='Enzimler',z='orta',kaz='Kofaktör ve koenzimin yapısını ve enzim etkinliğindeki rolünü ayırt eder.',kalip='öncüllü',
 metin='Bazı enzimler yalnız protein kısmıyla etkinlik gösterirken bazıları, etkinlik gösterebilmek için kofaktör adı verilen yardımcı molekül ya da iyonlara gereksinim duyar. Vitamin türevi olan NAD⁺ ve FAD ile Fe²⁺ ve Zn²⁺ iyonları bu yardımcılara örnektir.\nI. Koenzimler, organik yapılı kofaktörlerdir.\nII. Fe²⁺ ve Zn²⁺ gibi iyonlar, organik yapılı kofaktörlerdir.\nIII. Kofaktörler, substrat gibi tepkimelerde sürekli tüketilir.\nBuna göre bu ifadelerden hangileri yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifadeler.',ip=['Metal iyonlarının organik molekül olup olmadığını ve yardımcıların substrattan farkını düşün.'],
 bilgi=[B('Kofaktör ve koenzim','Kofaktör, enzimin etkinliği için gereken yardımcı yapıdır: metal iyonları (inorganik) ya da koenzimler (organik) olabilir. Birçok koenzimin yapısında vitaminler bulunur')],
 puf='Kofaktör iki gruba ayrılır: inorganik iyonlar ve organik koenzimler; substrat gibi sürekli tüketilmezler.')

# ======================= 22 · vitamin tablosu · kolay =======================
def yerles(dogru,yanlislar):
    h=sec_harf(); s=list(yanlislar); s.insert('ABCDE'.index(h),dogru); return s
VT=[('A','Gece körlüğü',True),('B12','Kansızlık',False),('C','İskorbüt (diş eti kanaması)',False),('D','Raşitizm (kemik gelişim bozukluğu)',True),('K','Kanın geç pıhtılaşması',True)]
yag=[v for v,_,y in VT if y]; assert yag==['A','D','K']
SK22=tablo_svg(['Vitamin','Eksikliğinde görülen durum'],[[v,e] for v,e,_ in VT])
dg='A, D ve K'; yn=[('B12 ve C','Suda çözünenleri seçmiş; soruyu “yağda çözünen” yerine “suda çözünen” olarak okumuş.','dikkat'),('A ve D','K vitamininin de yağda çözündüğünü bilmemiş.','bilgi'),('A, C ve D','C vitamininin yağda çözündüğünü sanmış.','bilgi'),('A, B12, D ve K','B12 vitaminini de yağda çözünenler arasında saymış.','bilgi')]
sr=yerles(dg,[y[0] for y in yn])
q('0022',ad=[A('Tabloyu oku','Tabloda A, B12, C, D ve K vitaminleri ile eksikliklerinde görülen durumlar verilmiştir.','5 vitamin'),
 A('Çözünürlüğü hatırla','Yağda çözünen vitaminler A, D, E ve K’dır; B grubu vitaminleri ve C vitamini suda çözünür.','yağda: A, D, E, K · suda: B, C'),
 A('Tabloya uygula','Tablodaki vitaminlerden A, D ve K yağda çözünür; B12 ve C suda çözünür.','A, D, K yağda'),
 A('Sonuç','Yağda çözünen vitaminler A, D ve K’dır.','A, D ve K')],
 fikir='Tablodaki vitaminler yağda ve suda çözünenler olarak ayrılır.',tuzak='C vitaminini ya da B12’yi yağda çözünen sanmak.',ne='vitaminler tablosu ve çözünürlük',
 alt='Vitaminler',z='kolay',kaz='Vitaminleri yağda ve suda çözünenler olarak sınıflandırır.',kalip='tablo',
 metin='Aşağıdaki tabloda bazı vitaminler ve bu vitaminlerin eksikliğinde görülen durumlar verilmiştir. Vitaminler, vücutta az miktarda gereken ve enerji vermeyen organik bileşiklerdir.\nBuna göre tablodaki vitaminlerden hangileri yağda çözünür?',
 dogru=dg,yan=yn,sira=sr,istenen='Yağda çözünen vitaminler.',ip=['Vitaminler çözünürlüklerine göre iki gruba ayrılır.'],
 bilgi=[B('Vitaminler','Vitaminler az miktarda gereken, enerji vermeyen organik bileşiklerdir; bazıları yağda, bazıları suda çözünür')],
 puf='Yağda çözünenler: A, D, E, K; geri kalan B grubu ve C suda çözünür.',sekil=SK22)

# ======================= 23 · vitamin nitel · orta · olumsuz =======================
r=tekli(('Yağda çözünen vitaminlerin fazlası idrarla atılır, bu yüzden zarar vermez.',''),
 [('Vitaminler, enerji vermeyen düzenleyici organik moleküllerdir.','vitaminler yakıt değil, düzenleyicidir ve enerji vermez.'),
  ('Suda çözünen vitaminlerin fazlası genellikle idrarla atılır.','suda çözünen vitaminler vücutta depolanmaz ve fazlası idrarla atılır.'),
  ('Birçok vitamin vücutta yeterince sentezlenemediği için besinlerle alınır.','çoğu vitamin vücutta yeterli miktarda üretilemez ve dışarıdan alınmalıdır.'),
  ('Yağda çözünen vitaminler vücutta depolanabilir.','yağda çözünen vitaminler yağ dokusu ve karaciğerde depolanır; fazla alınması zararlıdır.')],hedef=False)
q('0023',ad=[A('Vitaminlerin özelliklerini hatırla','Vitaminler enerji vermez, düzenleyicidir; çoğu besinlerle alınır. Suda çözünenler depolanmaz, yağda çözünenler depolanır.','enerji yok · besinle alınır · depolama farkı'),
 A('Şıkları sına','Enerji vermemesi, suda çözünenlerin idrarla atılması, besinle alınma ve yağda çözünenlerin depolanması bilgilerle uyumludur.','4 ifade doğru'),
 A('Kalan ifadeyi incele','Yağda çözünen vitaminlerin fazlası idrarla atılmaz, vücutta birikir; bu nedenle yüksek dozları zarar verebilir.','biriken fazla → zarar'),
 A('Sonuç','Yanlış olan, yağda çözünenlerin fazlasının idrarla atıldığını söyleyen ifadedir.','Yağda çözünen: depolanır')],
 fikir='Vitaminlerin çözünürlüğüne bağlı depolanma ve atılma farkı sınanır.',tuzak='Yağda çözünen vitaminlerin de idrarla atıldığını sanmak.',ne='sporcu ve vitamin takviyesi',
 alt='Vitaminler',z='orta',kaz='Yağda ve suda çözünen vitaminlerin vücuttaki durumunu ayırt eder.',kalip='hikâyeli',
 metin='Yoğun antrenman yapan bir sporcu, performansını artırmak amacıyla yüksek dozda vitamin takviyesi kullanmak istiyor. Doktoru, vitaminlerin yağda ya da suda çözünen çeşitleri bulunduğunu ve kontrolsüz kullanımın zararlı olabileceğini söylüyor.\nBuna göre vitaminlerle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Çözünürlüğün, vitaminin vücutta kalıp kalmayacağını nasıl belirlediğini düşün.'],
 bilgi=[B('Vitaminlerin özellikleri','Vitaminler az miktarda gereken, enerji vermeyen düzenleyici organik bileşiklerdir. Suda çözünenler (B, C) depolanmaz; yağda çözünenler (A, D, E, K) yağ dokusunda ve karaciğerde depolanır')],
 puf='Suda çözünen vitamin atılır, yağda çözünen birikir; bu yüzden fazlası yalnız ikincisinde risklidir.')

# ======================= 24 · nükleotit şekli · kolay =======================
g=('\\draw[line width=1.3pt] (0,0) circle (.42);\\draw[line width=1.3pt] (.42,0)--(1.2,0);'
   '\\node[regular polygon,regular polygon sides=5,draw,line width=1.3pt,minimum size=1.15cm] at (1.75,0) {};\\draw[line width=1.3pt] (2.3,0)--(3.0,0);'
   '\\draw[line width=1.3pt] (3.0,-.45) rectangle (3.9,.45);'
   +rozet(0,-1.15,'I')+'\\draw[line width=.8pt] (0,-.88)--(0,-.45);'
   +rozet(1.75,-1.15,'II')+'\\draw[line width=.8pt] (1.75,-.88)--(1.75,-.55);'
   +rozet(3.45,-1.15,'III')+'\\draw[line width=.8pt] (3.45,-.88)--(3.45,-.45);')
SK24=tk(g,1.6)
r=tekli(('II numaralı kısım, deoksiriboz şekeridir.',''),
 [('I numaralı kısım, organik bazdır.','I numaralı kısım fosfat grubudur; organik baz, şekere bağlı III numaralı kısımdır.'),
  ('III numaralı kısım, fosfat grubudur.','III numaralı kısım organik bazdır (A, T, G ya da C); fosfat grubu I’dir.'),
  ('III numaralı kısım, urasil bazını içerebilir.','urasil RNA’ya özgüdür; DNA nükleotitindeki baz A, T, G ya da C’dir.'),
  ('II numaralı kısım, riboz şekeridir.','DNA nükleotitinde şeker deoksiribozdur; riboz RNA’da bulunur.')])
q('0024',ad=[A('Parçaları tanı','Nükleotit; fosfat, pentoz şeker ve organik bazdan oluşur. Şekerin bir yanında fosfat, öbür yanında baz bulunur.','I: fosfat · II: şeker · III: organik baz'),
 A('DNA’ya uygula','DNA nükleotitinde şeker deoksiribozdur ve baz A, T, G ya da C’dir; urasil ve riboz RNA’ya özgüdür.','DNA: deoksiriboz, A–T–G–C'),
 A('Şıkları sına','Fosfat ile baz karıştırılan ve urasil ya da riboz içeren ifadeler DNA nükleotitine uymaz.','4 ifade hatalı'),
 A('Sonuç','Doğru ifade, II numaralı kısmın deoksiriboz olduğunu söyler.','II: deoksiriboz')],
 fikir='Nükleotitin üç parçası şekilden ayırt edilir ve DNA nükleotidine özgü şeker ve bazlar bilinir.',tuzak='Fosfat ile organik bazı karıştırmak; riboz ve urasili DNA’ya ait sanmak.',ne='DNA nükleotidinin şematik çizimi',
 alt='Nükleik Asitler',z='kolay',kaz='Nükleotitin yapısını tanıyıp DNA’ya özgü parçaları belirler.',kalip='şekilli',
 metin='Şekilde, DNA molekülünün yapıtaşı olan bir nükleotit şematik olarak gösterilmiştir. Nükleotit; birbirine bağlı fosfat grubu, pentoz şeker ve organik bazdan oluşmaktadır ve parçalar I, II ve III ile numaralandırılmıştır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Şekerin hangi yanında fosfat, hangi yanında baz bulunduğuna bak.'],
 bilgi=[B('Nükleotit','Nükleik asitlerin yapıtaşıdır: bir fosfat grubu, bir pentoz şeker ve bir organik bazdan oluşur. DNA’da şeker deoksiriboz, bazlar A, T, G, C; RNA’da şeker riboz, bazlar A, U, G, C’dir')],
 puf='Nükleotit: şekeri ortaya al, bir yanına fosfat, öbür yanına baz koy; DNA’da şeker deoksiribozdur.',sekil=SK24)

# ======================= 25 · DNA–RNA tablosu · orta · olumsuz =======================
SK25=tablo_svg(['Özellik','X','Y'],[['Pentoz şeker','Deoksiriboz','Riboz'],['Zincir sayısı','2','1'],['Baz çeşidi sayısı','4','4']])
r=tekli(('Y’nin tek zincirinde guanin sayısı, sitozin sayısına her zaman eşittir.',''),
 [('X’in nükleotitlerinde timin bazı bulunabilir.','X, deoksiriboz taşıyan çift zincirli DNA’dır ve DNA’da timin bulunur.'),
  ('Y’nin nükleotitlerinde urasil bazı bulunabilir.','Y, riboz taşıyan RNA’dır ve RNA’da timin yerine urasil bulunur.'),
  ('X’te adenin sayısı, timin sayısına eşittir.','çift zincirli DNA’da adenin timinle eşleştiğinden iki sayı eşittir.'),
  ('X ve Y’nin nükleotitlerinin ikisi de fosfat grubu taşır.','bütün nükleotitlerde fosfat grubu bulunur.')],hedef=False)
q('0025',ad=[A('Tabloyu yorumla','X deoksiriboz taşıyan ve çift zincirli olduğundan DNA, Y riboz taşıyan ve tek zincirli olduğundan RNA’dır.','X: DNA · Y: RNA'),
 A('Bazları hatırla','DNA’da A, T, G, C; RNA’da A, U, G, C bazları bulunur. Çift zincirli DNA’da A = T ve G = C’dir.','DNA: A = T ve G = C'),
 A('Şıkları sına','X’te timin, Y’de urasil bulunur; X’te A = T olur; her iki nükleotit de fosfat taşır.','4 ifade doğru'),
 A('Sonuç','Tek zincirli Y’de eşleşme kuralı bulunmadığından G ile C’nin her zaman eşit olduğu söylenemez.','Tek zincirde G = C zorunlu değil')],
 fikir='Tablodan DNA ve RNA ayırt edilir; eşitlik kurallarının yalnız çift zincirde geçerli olduğu sınanır.',tuzak='A = T, G = C eşitliğini tek zincirli RNA için de geçerli sanmak.',ne='X ve Y nükleik asitleri tablosu',
 alt='Nükleik Asitler',z='orta',kaz='DNA ile RNA’yı karşılaştırır ve baz eşitliği kurallarını yorumlar.',kalip='tablo',
 metin='Aşağıdaki tabloda, canlı hücrelerinde bulunan iki nükleik asit olan X ve Y’nin bazı özellikleri karşılaştırılmıştır. X ve Y’den biri DNA, diğeri RNA’dır.\nBuna göre aşağıdakilerden hangisi söylenemez?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Söylenemeyen ifade.',ip=['Önce tablodan X ve Y’yi tanı.'],
 bilgi=[B('DNA ve RNA','DNA: deoksiriboz, çift zincir, A–T ve G–C eşleşmesi. RNA: riboz, genellikle tek zincir, timin yerine urasil bulunur. Eşleşme kuralı yalnız iki zincir arasında geçerlidir')],
 puf='Nükleik asitleri tablodan tanıdıktan sonra her ifadeyi kurallara göre tek tek sına.',sekil=SK25)

# ======================= 26 · DNA zinciri şekli · orta · sayı =======================
SQ='GCATGCCATGAC'; GC=sum(1 for c in SQ if c in 'GC'); AT=len(SQ)-GC
assert (GC,AT)==(7,5); top=GC*3+AT*2; assert top==31 and len(SQ)*2==24 and len(SQ)*3==36 and GC*2+AT*3==29 and 2*top==62
b=[]
for i,c in enumerate(SQ):
    x=0.55*i
    b.append(f'\\draw[line width=1.1pt] ({x},1.2) rectangle ({x+.45},1.65);\\node at ({x+.225},1.425) {{{c}}};')
    b.append(f'\\draw[line width=.9pt,opacity=.45] ({x},0) rectangle ({x+.45},.45);\\node[opacity=.6] at ({x+.225},.225) {{?}};')
b.append(f'\\node[anchor=east] at (-.15,1.425) {{1. zincir}};\\node[anchor=east] at (-.15,.225) {{2. zincir}};')
SK26=tk('\n'.join(b))
q('0026',ad=[A('Bazları say','Verilen zincirde 12 baz vardır: A ve T toplam 5, G ve C toplam 7 tanedir.','5 (A, T) + 7 (G, C) = 12'),
 A('Eşleşmeyi uygula','Diğer zincirde her baz eşleşir: A–T çifti 2, G–C çifti 3 hidrojen bağı yapar.','A–T: 2 · G–C: 3'),
 A('Çift sayılarını yaz','Her baz bir çift oluşturur: 5 tane A–T çifti ve 7 tane G–C çifti.','5 A–T + 7 G–C'),
 A('Bağları topla','Bağ sayıları çift sayısıyla çarpılıp toplanır.','5 × 2 + 7 × 3 = 10 + 21 = 31'),
 A('Sonuç','Toplam hidrojen bağı sayısı 31’dir.','31')],
 fikir='Tek zincirden eşleşen çiftler ve hidrojen bağı sayısı hesaplanır.',tuzak='Bağ sayılarını ters kullanmak ya da iki zincirin bazlarını ayrı ayrı saymak.',ne='tek zincirli baz dizisinden hidrojen bağı sayısı',
 alt='Nükleik Asitler',z='orta',kaz='Tek zincirin baz dizisinden çift zincirdeki hidrojen bağı sayısını hesaplar.',kalip='şekilli',
 metin='Şekilde, çift zincirli bir DNA parçasının 1. zincirindeki bazlar verilmiştir. 2. zincir, 1. zincirle baz eşleşmesi kurallarına uygun olarak tamamlanacaktır.\nBuna göre 2. zincir tamamlandığında iki zincir arasında toplam kaç hidrojen bağı bulunur?',
 dogru=31,yan=[(24,'Bütün baz çiftlerini 2 hidrojen bağlı saymış (12 × 2).','bilgi'),(29,'A–T için 3, G–C için 2 hidrojen bağı almış; bağ sayılarını ters kullanmış.','bilgi'),(36,'Bütün baz çiftlerini 3 hidrojen bağlı saymış (12 × 3).','bilgi'),(62,'İki zincirdeki bazları ayrı ayrı sayıp bağları iki kez hesaplamış.','islem')],
 istenen='İki zincir arasındaki toplam hidrojen bağı sayısı.',ip=['Hangi bazların birbiriyle eşleştiğini ve her eşleşmedeki bağ sayısını hatırla.'],
 bilgi=[B('Baz eşleşmesi','Adenin (A) timinle iki, guanin (G) sitozinle üç hidrojen bağı yapar. Bir zincirdeki her baz, karşı zincirde kendi eşiyle bir çift oluşturur')],
 puf='Zincirdeki A ve T sayısı × 2 ile G ve C sayısı × 3’ü topla; karşı zinciri ayrıca sayma.',sekil=SK26)

# ======================= 27 · hidrojen bağından baz sayısı · zor =======================
nt=100; hb=130; cift=nt//2; y_=hb-2*cift; x_=cift-y_
assert (cift,y_,x_)==(50,30,20) and 2*x_+3*y_==hb and (x_,y_,2*x_,cift,2*y_)==(20,30,40,50,60)
q('0027',ad=[A('Çift sayısını bul','Çift zincirli DNA’da her baz çifti 2 nükleotit demektir.','100 ÷ 2 = 50 çift'),
 A('Denklem kur','A–T çiftleri 2, G–C çiftleri 3 hidrojen bağı yapar. A–T çifti x, G–C çifti y olsun: x + y = 50 ve 2x + 3y = 130.','x + y = 50 · 2x + 3y = 130'),
 A('Çöz','Birinci denklemin 2 katını ikinciden çıkarınca G–C çifti sayısı bulunur.','y = 130 − 100 = 30 · x = 20'),
 A('Adenini bul','Her A–T çiftinde bir adenin vardır.','A = 20'),
 A('Sonuç','Adenin nükleotiti sayısı 20’dir.','20')],
 fikir='Toplam nükleotit ve hidrojen bağı verilerinden baz çiftleri iki bilinmeyenli denklemle bulunur.',tuzak='Bulunan çift sayısını nükleotit sayısıyla karıştırmak; G–C çiftini sorulan sanmak.',ne='hidrojen bağı sayısından adenin sayısı',
 alt='Nükleik Asitler',z='zor',kaz='Hidrojen bağı ve nükleotit sayısından baz sayılarını hesaplar.',kalip='yeni nesil',
 metin='Bir bakteriden elde edilen çift zincirli DNA parçası 100 nükleotitten oluşmaktadır. Bu DNA parçasında iki zincir arasında toplam 130 hidrojen bağı bulunduğu belirlenmiştir.\nBuna göre bu DNA parçasındaki adenin nükleotiti sayısı kaçtır?',
 dogru=20,yan=[(30,'G–C çiftlerinin sayısını bulmuş ve guanin sayısını adenin sanmış.','dikkat'),(40,'A ve T nükleotitlerinin toplamını adenin sayısı olarak vermiş.','dikkat'),(50,'Baz çifti sayısını adenin sayısı sanmış.','dikkat'),(60,'G ve C nükleotitlerinin toplamını adenin sayısı olarak vermiş.','dikkat')],
 istenen='Adenin nükleotiti sayısı.',ip=['A–T ve G–C çiftlerinin sayısına ayrı ayrı bir değişken verip iki bilgiden iki denklem kur.'],
 bilgi=[B('Baz çifti ve hidrojen bağı','Adenin timinle 2, guanin sitozinle 3 hidrojen bağı yapar. Çift zincirde A = T ve G = C olur.')],
 puf='Hidrojen bağı verilmişse A–T ve G–C çiftleri için iki bilinmeyenli denklem kur.')

# ======================= 28 · baz oranları · orta · öncüllü =======================
d={'I':(True,'A, T ile; G, C ile eşleştiğinden A + G toplamı, T + C toplamına eşittir'),
   'II':(False,'adenin ve guanin sayıları arasında eşitlik kuralı yoktur; eşitlik A ile T, G ile C arasındadır'),
   'III':(True,'G–C çifti 3, A–T çifti 2 hidrojen bağı yaptığından G–C çifti daha fazla hidrojen bağı içerir')}
r=onc2(d,True)
q('0028',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncüller: {r["dogru"]}.',r['dogru'])],
 fikir='Baz eşleşme kuralından toplam baz oranları ve hidrojen bağı farkı çıkarılır.',tuzak='Adenin ile guaninin sayısını eşit sanmak.',ne='çift zincirli DNA baz oranı yargıları',
 alt='Nükleik Asitler',z='orta',kaz='Çift zincirli DNA’da baz oranlarını ve hidrojen bağlarını yorumlar.',kalip='öncüllü',
 metin='Bir araştırmacı, çift zincirli bir DNA molekülünde bazların birbirleriyle eşleşme kurallarını ve sayısal ilişkilerini inceliyor. Bu DNA’da adenin timinle, guanin sitozinle eşleşmektedir.\nI. Adenin ve guanin sayılarının toplamı, timin ve sitozin sayılarının toplamına eşittir.\nII. Adenin sayısı, guanin sayısına her zaman eşittir.\nIII. Bir G–C çiftinde, bir A–T çiftine göre daha fazla hidrojen bağı bulunur.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her bazın hangi bazla eşleştiğini düşün.'],
 bilgi=[B('Baz eşleşmesi','Çift zincirli DNA’da A–T çifti 2, G–C çifti 3 hidrojen bağı ile bağlanır; bu nedenle A = T ve G = C olur. Diğer baz ikilileri arasında sayısal eşitlik zorunlu değildir')],
 puf='Eşitlik yalnız eşleşen bazlar arasındadır: A = T, G = C.')

# ======================= 29 · ATP yapısı · kolay · olumsuz =======================
def dal(x1,x2): return f'\\draw[line width=1.3pt,decorate,decoration={{snake,amplitude=.7mm,segment length=2.2mm}}] ({x1},0)--({x2},0);'
g=('\\draw[line width=1.3pt] (-.45,-.45) rectangle (.45,.45);\\draw[line width=1.3pt] (.45,0)--(1.0,0);'
   '\\node[regular polygon,regular polygon sides=5,draw,line width=1.3pt,minimum size=1.1cm] at (1.55,0) {};\\draw[line width=1.3pt] (2.1,0)--(2.65,0);'
   '\\draw[line width=1.3pt] (3.0,0) circle (.35);\\node at (3.0,0) {P};'+dal(3.35,4.15)+'\\draw[line width=1.3pt] (4.5,0) circle (.35);\\node at (4.5,0) {P};'
   +dal(4.85,5.65)+'\\draw[line width=1.3pt] (6.0,0) circle (.35);\\node at (6.0,0) {P};'
   +rozet(0,-1.1,'I')+'\\draw[line width=.8pt] (0,-.83)--(0,-.45);'+rozet(1.55,-1.1,'II')+'\\draw[line width=.8pt] (1.55,-.83)--(1.55,-.55);'
   +rozet(6.0,-1.1,'III')+'\\draw[line width=.8pt] (6.0,-.83)--(6.0,-.35);')
SK29=tk(g)
r=tekli(('II numaralı kısım, deoksiriboz şekeridir.',''),
 [('I numaralı kısım, organik bazdır.','I numaralı kısım organik baz olan adenindir.'),
  ('Molekülde iki yüksek enerjili fosfat bağı bulunur.','dalgalı çizgiyle gösterilen iki fosfat bağı yüksek enerjilidir.'),
  ('ATP’nin hidrolizinde ADP ve inorganik fosfat oluşur ve enerji açığa çıkar.','ATP bir fosfatını kaybedip ADP’ye dönüşürken enerji verir.'),
  ('III numaralı kısım, bir fosfat grubudur.','III numaralı kısım fosfat gruplarından biridir.')],hedef=False)
q('0029',ad=[A('Parçaları tanı','ATP; adenin bazı (I), pentoz şeker (II) ve üç fosfat grubundan oluşur. Fosfatlar arasındaki dalgalı çizgiler yüksek enerjili bağlardır.','I: adenin · II: şeker · III: fosfat'),
 A('Şeker türünü belirle','ATP’deki şeker ribozdur; deoksiriboz DNA nükleotitlerinde bulunur.','ATP: riboz'),
 A('Şıkları sına','Adenin organik bazdır, iki yüksek enerjili bağ vardır, hidrolizde ADP ve Pi oluşur, III fosfat grubudur.','4 ifade doğru'),
 A('Sonuç','Yanlış olan, ATP’deki şekere deoksiriboz demektir.','II: riboz')],
 fikir='ATP’nin parçaları şekilden tanınır; şekerinin riboz olduğu ve yüksek enerjili bağlar sınanır.',tuzak='ATP’deki şekeri deoksiriboz sanmak.',ne='ATP’nin şematik yapısı',
 alt='ATP',z='kolay',kaz='ATP’nin yapısını tanır ve görevini ilişkilendirir.',kalip='şekilli',
 metin='Şekilde, hücrelerde enerji aktarımında görev alan ATP molekülünün yapısı şematik olarak gösterilmiştir. Fosfat grupları arasındaki dalgalı çizgiler yüksek enerjili bağları temsil etmektedir.\nBuna göre ATP ile ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Şekildeki molekülün hangi uçta fosfat gruplarıyla bittiğine ve parçaların her birinin ne olduğuna bak.'],
 bilgi=[B('ATP','Adenozin trifosfat: adenin bazı, riboz şekeri ve üç fosfat grubundan oluşur. Fosfat bağlarının kopmasıyla enerji açığa çıkar; hücrede enerji gerektiren olaylarda kullanılır')],
 puf='ATP: adenin + riboz + 3 fosfat; yüksek enerjili bağlar fosfatlar arasındadır.',sekil=SK29)

# ======================= 30 · ATP–ADP döngüsü · orta · öncüllü =======================
g=('\\draw[line width=1.3pt,rounded corners=4pt] (-.9,-.5) rectangle (.9,.5);\\node at (0,0) {ATP};'
   '\\draw[line width=1.3pt,rounded corners=4pt] (4.1,-.5) rectangle (6.4,.5);\\node at (5.25,0) {ADP + Pi};'
   '\\draw[-{Stealth[length=2.4mm]},line width=1.2pt] (1.1,.25)--(3.9,.25);\\draw[-{Stealth[length=2.4mm]},line width=1.2pt] (3.9,-.25)--(1.1,-.25);'
   +rozet(2.5,.8,'1')+rozet(2.5,-.8,'2'))
SK30=tk(g,1.25)
d={'I':(False,'1 numaralı olay ATP’nin hidrolizidir ve enerji açığa çıkarır; enerji gerektirmez'),
   'II':(True,'2 numaralı olay için gereken enerji, hücresel solunumda besinlerin yıkımıyla sağlanır'),
   'III':(False,'2 numaralı olayda ATP yıkılmaz, ADP ve inorganik fosfattan ATP oluşur')}
r=onc2(d,True)
q('0030',ad=[adim_onc(d,'I'),adim_onc(d,'II'),adim_onc(d,'III'),A('Sonuç',f'Doğru olan öncül: {r["dogru"]}.',r['dogru'])],
 fikir='ATP–ADP dönüşümünün yönleri enerji alışverişiyle birlikte yorumlanır.',tuzak='ATP oluşumunu enerji açığa çıkaran, yıkımını enerji gerektiren olay sanmak.',ne='ATP ⇄ ADP + Pi döngüsü',
 alt='ATP',z='orta',kaz='ATP–ADP dönüşümlerinde enerji alışverişini yorumlar.',kalip='şekilli',
 metin='Şekilde, hücrelerde sürekli gerçekleşen ATP ve ADP + Pi (inorganik fosfat) dönüşümleri 1 ve 2 numaralı oklarla gösterilmiştir. Kas hücreleri gibi enerji harcayan hücrelerde bu dönüşümler çok hızlı gerçekleşir.\nI. 1 numaralı olay, enerji gerektirir.\nII. 2 numaralı olay için gereken enerji, hücresel solunumda besinlerin yıkımıyla sağlanır.\nIII. 2 numaralı olayda ATP yıkılır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargı.',ip=['Okların yönüne bakarak hangi olayda ATP’nin oluştuğunu, hangisinde yıkıldığını belirle.'],
 bilgi=[B('ATP ve ADP','ATP, bir fosfat grubunu kaybederek ADP’ye dönüşürken enerji verir. ADP ve fosfattan ATP oluşumu ise enerji gerektirir ve bu enerji besinlerin yıkımından sağlanır')],
 puf='ATP → ADP: enerji açığa çıkar; ADP → ATP: enerji gerekir ve depolanır.',sekil=SK30)

bitir(P,'bilesenleriki',UK)
