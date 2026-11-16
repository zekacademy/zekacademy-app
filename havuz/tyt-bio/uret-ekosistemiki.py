"""TYT Biyoloji · Ekosistem · ek paket (ekosistemiki): 30 soru, kardeş yok, ipucu 1.
Şekil verileri, enerji hesapları ve öncül doğrulukları Python'da tanımlanır/hesaplanır; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math
BD=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,BD)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Ekosistem'; UK='bio|Ekosistem'; H.KONU=KONU_
P=Parti('ekosistemiki',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 9–10. sınıf Ekosistem'
TIP={'bilesen':'Ekosistemin bileşenleri ve düzeyleri','agi':'Besin zinciri ve besin ağı','piramit':'Besin piramitleri ve enerji aktarımı','dongu':'Madde döngüleri',
     'iliski':'Ekolojik ilişkiler','populasyon':'Popülasyon grafikleri','cevre':'Çevre sorunları','surdur':'Sürdürülebilirlik ve biyoçeşitliliğin korunması'}
USED=[]
def q(no,tp,z,kalip,alt,kaz,ne,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1 and no not in USED; USED.append(no)
    kart(f'K-BYEK2-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),'by-ek2-'+tp,TIP[tp],KY)
    mk(P,no,ad=ad,adim=len(ad),tipId='by-ek2-'+tp,tip=TIP[tp],z=z,kalip=kalip,alt=alt,kaz=kaz,kart=f'K-BYEK2-{no[-2:]} ({TIP[tp].lower()}) · {ne}',**k)
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS=[('I',),('II',),('III',),('I','II'),('I','III'),('II','III'),('I','II','III')]
def onc(d,harf,neg=False):
    """d: {'I':(metin,doğru_mu,gerçek)}; neg: kök 'yanlış olanlar' mı. harf: doğru şıkkın harfi."""
    T=tuple(k for k in d if d[k][1]!=neg); i=SETS.index(T); p='ABCDE'.index(harf)
    assert i-2<=p<=i,('harf uygun degil',T,harf)
    ops=SETS[:i][:p]+[T]+SETS[i+1:][:4-p]; assert len(ops)==5
    sira=[ORD[SETS.index(o)] for o in ops]; yan=[]
    for o in ops:
        if o==T: continue
        pr=[]
        for x in sorted(set(o)-set(T),key=lambda z:'I II III'.split().index(z)):
            pr.append(f'{x} öncülünü '+('doğru' if not neg else 'yanlış')+' sanmış; oysa '+('yanlıştır' if not neg else 'doğrudur')+f': {d[x][2]}')
        for x in sorted(set(T)-set(o),key=lambda z:'I II III'.split().index(z)):
            pr.append(f'{x} öncülünü '+('yanlış' if not neg else 'doğru')+' sanmış; oysa '+('doğrudur' if not neg else 'yanlıştır')+f': {d[x][2]}')
        yan.append((ORD[SETS.index(o)],'. '.join(pr)+'.','bilgi'))
    return dict(dogru=ORD[i],yan=yan,sira=sira)
def omet(giris,d,kok):
    return giris+'\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\n'+kok
def oad(d,neg=False,bas=None):
    a=list(bas or [])
    for x in d: a.append(A(f'{x}. öncülü incele',d[x][2][0].upper()+d[x][2][1:]+'.',('doğru' if d[x][1] else 'yanlış')))
    T=[x for x in d if d[x][1]!=neg]
    a.append(A('Sonucu yaz','Köke uygun öncüller bir arada yazılır.',' ve '.join(T) if len(T)<3 else 'I, II ve III' if len(T)==3 else T[0]))
    return a
def tek(items,hedef,harf):
    """items: [(metin,doğru_mu,gerçek)]; hedef True: tek doğru ifade; False: tek yanlış ifade."""
    h=[s for s in items if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    dg=h[0]; dig=[s for s in items if s[1]!=hedef]; assert len(dig)==4
    sira=dig[:]; sira.insert('ABCDE'.index(harf),dg)
    yan=[(m,(f'Bu ifadeyi doğru sanmış; oysa yanlıştır: {n}' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}'),'bilgi') for m,b,n in dig]
    return dict(dogru=dg[0],yan=yan,sira=[s[0] for s in sira]),dg[2]
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.3mm,width=1.9mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def nid(s): return 'n'+''.join(c for c in s if c.isascii() and c.isalnum()) if s else 'n'

# ===== 01 · kolay · tablo + öncüllü · bileşen =====
d={'I':('Kayın ağacı üreticidir.',True,'kayın ağacı organik maddeyi ışık enerjisiyle kendisi sentezlediği için üreticidir'),
   'II':('Tavşan ikincil tüketicidir.',False,'tavşan üreticiyi yediği için birincil tüketicidir; ikincil tüketici, tavşanı yiyen kurttur'),
   'III':('Mantar ayrıştırıcıdır.',True,'mantar ölü organik maddeyi ayrıştırıp besin olarak kullandığı için ayrıştırıcıdır')}
r=onc(d,'C')
q('0001','bilesen','orta','öncüllü','Üretici, tüketici, ayrıştırıcı','Canlıları ekosistemdeki besinsel rollerine göre ayırt eder.','rol belirleme',
 'Organik maddeyi nasıl elde ettiğine bakarak canlının rolü belirlenir.','Tavşanı ikincil tüketici saymak.',
 oad(d),metin='Bir orman ekosisteminde kayın ağacı ışık enerjisi, CO2 ve sudan organik madde sentezler; tavşan kayın yapraklarını yer; kurt tavşanı yer; mantar ise ölü kütükteki organik maddeyi sindirip emer. Bu canlılar ekosistemde üretici, tüketici ya da ayrıştırıcı olarak görev yapmaktadır.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Üretici organik maddeyi kendisi sentezler; tüketici hazır alır; ayrıştırıcı ölüleri ayrıştırır.'],
 bilgi=[B('Besinsel roller','Üretici: kendi organik maddesini sentezler (bitki, alg) · Tüketici: hazır organik madde yer · Ayrıştırıcı: ölü kalıntıları ayrıştırır (mantar, bakteri)'),B('Tüketici basamakları','Üreticiyi yiyen birincil, onu yiyen ikincil tüketicidir')],
 puf='Önce canlının organik maddeyi nereden aldığını bul, sonra rolünü adlandır.')

# ===== 02 · kolay · öncüllü · bileşen =====
d={'I':('Bir adada yaşayan tüm yaban keçileri: Popülasyon',True,'aynı türün aynı bölgedeki bireyleri popülasyondur'),
   'II':('Bir akarsuda yaşayan tüm canlıların oluşturduğu topluluk: Ekosistem',False,'yalnız canlıların oluşturduğu topluluğa komünite denir; ekosistem cansız bileşenleri de kapsar'),
   'III':('Bir gölün tüm canlıları ile cansız çevresi: Biyosfer',False,'bir gölün canlı ve cansız bileşenleri ekosistemdir; biyosfer yeryüzündeki tüm ekosistemlerin toplamıdır')}
r=onc(d,'A')
q('0002','bilesen','orta','öncüllü','Ekolojik düzeyler','Popülasyon, komünite, ekosistem ve biyosfer düzeylerini ayırt eder.','düzey eşleştirme',
 'Düzeyler tür sayısı ve cansız bileşenin varlığıyla ayrılır.','Komüniteyi ekosistem saymak; ekosistemi biyosferle karıştırmak.',
 oad(d),metin='Ekolojide canlıların bir arada bulunuşu popülasyon, komünite, ekosistem ve biyosfer düzeylerinde incelenir. Aşağıda bazı örnekler ve ait oldukları düzeyler eşleştirilmiştir.\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nBu eşleştirmelerden hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru eşleştirmeler.',ip=['Her örnekte kaç türün ve hangi bileşenlerin sözü edildiğine bak.'],
 bilgi=[B('Popülasyon ve komünite','Popülasyon: aynı türün bir bölgedeki bireyleri · Komünite: bir bölgede yaşayan farklı türlerin tüm popülasyonları')],
 puf='Tek tür = popülasyon; tüm canlılar = komünite; canlılar + cansız çevre = ekosistem.')

# ===== 03 · kolay · şekil · olumsuz · agi =====
it=[('Enerji, algden martıya doğru akar.',True,'oklar yenen canlıdan yiyen canlıya doğrudur; enerji algden martıya akar'),
    ('Karides, birincil tüketici basamağındadır.',True,'karides üretici olan algı yediği için birincil tüketicidir'),
    ('Martının bulunduğu basamakta algın bulunduğu basamaktan daha az enerji bulunur.',True,'enerji basamaklar çıkıldıkça azalır'),
    ('Hamsideki enerjinin tamamı martıya aktarılır.',False,'her basamakta enerjinin büyük bölümü solunumla ısı olarak kaybolur; yaklaşık %10’u aktarılır'),
    ('Alg ortadan kalkarsa zincirdeki diğer canlılar da olumsuz etkilenir.',True,'zincirin enerji kaynağı olan üretici kalkarsa tüketiciler besinsiz kalır')]
r,g=tek(it,False,'D')
q('0003','agi','kolay','düz','Besin zinciri','Besin zincirinde ok yönü, basamaklar ve enerji aktarımını yorumlar.','zincir, olumsuz kök',
 'Zincirde enerji yenenden yiyene akar ve her basamakta azalır.','Aktarılan enerjinin tamamının sonraki basamağa geçtiğini sanmak.',
 [A('Oku yönünü oku','Oklar yenen canlıdan yiyen canlıya doğrudur.','Alg → Karides → Hamsi → Martı'),A('Basamakları belirle','Alg üretici, karides birincil, hamsi ikincil, martı üçüncül tüketicidir.','1 üretici, 3 tüketici'),A('Şıkları ele','Dört ifade enerji akışına ve basamaklara uygundur.','4 ifade doğru'),A('Sonucu yaz','Yanlış olan ifade enerjinin tamamının aktarıldığını söyleyendir.','Yanlış: tam aktarım')],
 metin='Bir kıyı ekosisteminde yaşayan bazı canlıların beslenme ilişkisi alg → karides → hamsi → martı biçimindedir. Oklar yenen canlıdan yiyen canlıya doğrudur ve enerjinin akış yönünü belirtmektedir. Zincirdeki canlıların hepsi aynı kıyı bölgesinde yaşamaktadır.\nBuna göre bu besin zinciri ile ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Zincirde enerji nerelere gider?'],
 bilgi=[B('Enerji akışı','Enerji yenenden yiyene doğru akar')],
 puf='Besin zincirinde enerji tek yönlüdür ve basamaklar çıkıldıkça azalır.')

# ===== piramit çizimi =====
def piramit(katman,W0=6.0,adim=1.0,h=.95):
    """katman: alttan üste (ad, değer metni)"""
    b=[]
    for i,(ad_,dg) in enumerate(katman):
        w=W0-adim*i*1.0; y=i*h
        b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.06] ({-w/2:.2f},{y:.2f}) rectangle ({w/2:.2f},{y+h:.2f});\\draw[line width=1pt] ({-w/2:.2f},{y:.2f}) rectangle ({w/2:.2f},{y+h:.2f});')
        b.append(f'\\node[anchor=west] at ({W0/2+.3:.2f},{y+h/2:.2f}) {{{ad_}: {dg}}};')
    return tk(''.join(b))
# ===== 04 · kolay · piramit =====
U4=20000; X4=U4//10; T4=X4//10; assert (X4,T4)==(2000,200)
S4=piramit([('Üreticiler',f'{U4} kJ'),('Birincil tüketiciler','X'),('İkincil tüketiciler',f'{T4} kJ')],W0=4.6,adim=1.0)
q('0004','piramit','kolay','şekilli','Enerji piramidi','Enerji piramidinde %10 aktarımla bir basamağın enerjisini bulur.','piramit, tek aktarım',
 'Her basamakta enerjinin %10’u bir üst basamağa geçer.','Aktarımın %90 olduğunu ya da hiç kayıp olmadığını sanmak.',
 [A('Aktarım oranını hatırla','Bir basamaktaki enerjinin yalnızca %10’u üst basamağa geçer.','× 0,1'),A('Üreticiden hesapla','Üreticilerdeki enerji birincil tüketicilere %10 oranında aktarılır.',f'{U4} × 0,1 = {X4}'),A('Kontrol et','Aynı oran X’ten ikincil tüketicilere de uygulanınca verilen değer bulunur.',f'{X4} × 0,1 = {T4}'),A('Sonucu yaz','X basamağının enerjisi 2000 kJ’dür.','X = 2000 kJ')],
 metin='Bir ekosistemin enerji piramidi şekilde verilmiştir. Her basamakta, bir önceki basamaktaki enerjinin yaklaşık %10’u bir üst basamağa aktarılmakta, geri kalanı canlıların yaşamsal faaliyetlerinde kullanılıp ısı olarak ortama verilmektedir. Piramitte yalnız X basamağının değeri verilmemiştir.\nBuna göre X ile gösterilen basamağın enerjisi kaç kJ’dür?',
 dogru=X4,yan=[(X4+T4,'X ile şekilde verilen üst basamağın değerini toplamış (2000 + 200).','dikkat'),(4000,'Aktarımın %20 olduğunu sanmış.','bilgi'),(18000,'Kaybolan %10’u çıkarıp %90’ın aktarıldığını sanmış.','bilgi'),(20000,'Enerjinin basamaklarda azalmadığını sanmış.','bilgi')],
 istenen='X basamağının enerjisi (kJ).',ip=['Üreticilerden bir üst basamağa geçerken enerjinin ne kadarı aktarılır?'],
 bilgi=[B('%10 kuralı','Bir basamaktaki enerjinin yaklaşık %10’u üst basamağa aktarılır · Örnek: 500 kJ → 50 kJ')],puf='Her basamak çıkışında enerji 10’a bölünür.',sekil=S4)

# ===== 05 · kolay · olumsuz · dongu =====
it=[('Baklagil köklerinde yaşayan bakteriler havanın serbest azotunu bağlayarak bitkinin kullanabileceği biçime getirir.',True,'azot bağlayıcı bakteriler N2’yi amonyağa dönüştürür'),
    ('Nitrifikasyon bakterileri amonyağı nitrata dönüştürür.',True,'nitrifikasyon, amonyağın nitrata dönüşmesidir'),
    ('Denitrifikasyon bakterileri nitratı serbest azot gazına çevirerek atmosfere verir.',True,'denitrifikasyon nitratı N2’ye çevirir'),
    ('Ayrıştırıcılar, ölü canlıların azotlu bileşiklerini amonyağa dönüştürür.',True,'ayrıştırıcılar ölü organik maddedeki azotu amonyak olarak serbest bırakır'),
    ('Bitkiler havadaki serbest azot gazını yapraklarıyla doğrudan alıp proteine dönüştürür.',False,'bitkiler azotu çoğunlukla nitrat biçiminde topraktan alır; serbest N2’yi doğrudan kullanamaz')]
r,g=tek(it,False,'E')
q('0005','dongu','orta','düz','Azot döngüsü','Azot döngüsündeki canlı ve süreçleri ayırt eder.','azot döngüsü, olumsuz kök',
 'Bitkiler serbest azotu kullanamaz; bakteriler azotun biçimini değiştirir.','Bitkilerin havadaki azotu doğrudan kullandığını sanmak.',
 [A('Döngüyü hatırla','N2 → amonyak → nitrat → N2 sırası bakteriler aracılığıyla gerçekleşir.','bağlama · nitrifikasyon · denitrifikasyon'),A('İfadeleri ele','İlk dört ifade bakterilerin ve ayrıştırıcıların görevlerini doğru verir.','4 ifade doğru'),A('Bitkiyi sına','Bitki yaprakla serbest N2 alamaz; nitratı kökle alır.','5. ifade yanlış'),A('Sonucu yaz','Yanlış olan ifade bitkilerle ilgili olandır.','Yanlış: bitki N2’yi doğrudan alır')],
 metin='Azotun doğadaki dolaşımına azot döngüsü denir. Havadaki serbest azot gazı (N2) çoğu canlı tarafından doğrudan kullanılamaz; bu gazın canlıların kullanabileceği bileşiklere dönüşmesinde ve bu bileşiklerin yeniden havaya dönmesinde bazı bakteriler görev alır.\nBuna göre azot döngüsü ile ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Bitkiler azotu hangi biçimde alır?'],
 bilgi=[B('Azot döngüsü','N2 → (azot bağlayıcı bakteriler) amonyak → (nitrifikasyon bakterileri) nitrat → (denitrifikasyon bakterileri) N2')],puf='Havadaki N2’yi bitki değil, bakteri bağlar.')

# ===== 06 · kolay · düz · cevre =====
r=dict(dogru='Kükürt dioksit ve azot oksitler',sira=['Oksijen ve azot','Kükürt dioksit ve azot oksitler','Kloroflorokarbonlar (CFC)','Karbon dioksit ve metan','Argon ve neon'],
 yan=[('Oksijen ve azot','Havanın temel bileşenlerini asit yağmuru gazı sanmış; bu gazlar normal havada bulunur ve asit oluşturmaz.','bilgi'),('Kloroflorokarbonlar (CFC)','Ozon incelmesine yol açan gazları asit yağmuruyla karıştırmış.','bilgi'),('Karbon dioksit ve metan','Sera gazlarını asit yağmuru nedeni sanmış; bunlar küresel ısınmaya yol açar.','bilgi'),('Argon ve neon','Soy gazların kimyasal tepkime vermediğini bilmemiş.','bilgi')])
q('0006','cevre','kolay','hikâyeli','Asit yağmurları','Asit yağmurlarının oluşumuna neden olan gazları bilir.','asit yağmuru gazları',
 'Asit yağmuru, kükürt ve azot oksitlerinin su ile tepkimesiyle oluşur.','Asit yağmurunu ozon incelmesi ya da sera etkisiyle karıştırmak.',
 [A('Sorunu belirle','Yağışla yeryüzüne dönen asit, asit yağmurudur.','asit yağmuru'),A('Kaynağı bul','Fosil yakıtlar yanınca kükürt ve azot oksitleri açığa çıkar.','SO2, NOx'),A('Su ile birleşmesini düşün','Bu oksitler su buharıyla tepkimeye girip asit oluşturur.','SO2, NOx + su → asit'),A('Diğer şıkları ele','CFC ozonu, CO2 ve metan sera etkisini etkiler; O2, N2, Ar ve Ne asit oluşturmaz.','Doğru: SO2 ve NOx')],
 metin='Fosil yakıtların yakılması ve sanayi faaliyetleri sonucunda atmosfere karışan bazı gazlar, havadaki su buharı ile birleşerek yağışlarla yeryüzüne asit olarak döner. Bu yağışlar ormanlara, göllere ve tarihî yapılara zarar vermektedir.\nBuna göre asit yağmurlarının oluşumunda doğrudan rol oynayan gazlar aşağıdakilerin hangisinde doğru olarak verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Asit yağmuru oluşturan gazlar.',ip=['Yanma ürünlerinden hangisi su ile birleşince asit oluşturur?'],
 bilgi=[B('Asit yağmuru','Fosil yakıtlar yanınca açığa çıkan bazı oksitler havadaki su buharıyla birleşerek asit oluşturur')],puf='Asit yağmuru = kükürt ve azot oksitleri + su.')

# ===== 07 · kolay · grafik · olumsuz =====
CO2={1960:320,1980:340,2000:370,2020:410}
Y_=sorted(CO2); dif=[CO2[Y_[i+1]]-CO2[Y_[i]] for i in range(3)]; assert dif==[20,30,40] and all(x>0 for x in dif)
gx=lambda y:(y-1960)/10*1.5; gy=lambda v:(v-300)*0.036
b=[f'\\draw[thick,{ARR}] (0,0)--(9.6,0);\\draw[thick,{ARR}] (0,0)--(0,4.6);']
for y in Y_: b.append(f'\\draw ({gx(y):.2f},0)--({gx(y):.2f},-.1) node[below] {{{y}}};')
for v in range(300,421,20): b.append(f'\\draw ({gy(v)*0:.2f},{gy(v):.2f})--(-.1,{gy(v):.2f}) node[left] {{{v}}};\\draw[gray!40] (0,{gy(v):.2f})--(9.2,{gy(v):.2f});')
b.append('\\draw[line width=1.4pt,vurgu] '+'--'.join(f'({gx(y):.2f},{gy(CO2[y]):.2f})' for y in Y_)+';')
for y in Y_: b.append(f'\\fill[vurgu] ({gx(y):.2f},{gy(CO2[y]):.2f}) circle (.08);')
b.append('\\node[anchor=north west] at (3.6,-.55) {Yıl};\\node[anchor=south] at (0,4.7) {CO$_2$ derişimi (ppm)};')
S7=tk(''.join(b))
it=[('Atmosferdeki CO2 derişimi 1960’tan 2020’ye kadar sürekli artmıştır.',True,'verilen dört ölçümde derişim her seferinde yükselmiştir'),
    ('2000–2020 arasındaki CO2 artışı, 1960–1980 arasındakinden daha azdır.',False,'2000–2020 arasında artış 40 ppm, 1960–1980 arasında 20 ppm’dir; artış hızlanmıştır'),
    ('Fosil yakıt tüketimindeki artış, bu değişimin nedenlerinden biri olabilir.',True,'fosil yakıtlar yanınca atmosfere CO2 verilir'),
    ('Bu artış sera etkisini güçlendirerek küresel ısınmaya katkıda bulunabilir.',True,'CO2 bir sera gazıdır; derişimi artınca tutulan ısı artar'),
    ('Orman alanlarının azalması, CO2’nin atmosferden uzaklaştırılmasını zayıflatır.',True,'ağaçlar fotosentezle CO2 kullanır; azalmaları CO2 kullanımını azaltır')]
r,g=tek(it,False,'B')
q('0007','cevre','orta','grafik','Küresel ısınma','Grafikten okunan CO2 değişimini sera etkisi ile ilişkilendirir.','CO2 grafiği, olumsuz kök',
 'Grafik değerleri karşılaştırılır; CO2 bir sera gazıdır.','Artış hızını yanlış karşılaştırmak.',
 [A('Değerleri oku','Grafikte 1960’tan 2020’ye 320, 340, 370 ve 410 ppm değerleri okunur.','320 · 340 · 370 · 410'),A('Artışları hesapla','Her yirmi yıllık dönemdeki artışı bul.','20 · 30 · 40 ppm'),A('İfadeleri sına','Artış sürekli ve giderek hızlıdır; CO2 sera gazı olup fosil yakıt ve orman kaybı etkilidir.','4 ifade doğru'),A('Sonucu yaz','Artışın azaldığını söyleyen ifade yanlıştır.','Yanlış: son artış daha az')],
 metin='Bir araştırma istasyonunda ölçülen atmosferdeki karbondioksit derişiminin yıllara göre değişimi grafikte gösterilmiştir. Aynı dönemde dünya genelinde fosil yakıt tüketimi artmış, orman alanları ise azalmıştır.\nBu grafiğe göre aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Dönemler arasındaki artış miktarlarını karşılaştır.'],
 bilgi=[B('Küresel ısınma','Sera gazları (CO2, metan) yeryüzünden yayılan ısıyı tutar; derişimleri artınca sıcaklık yükselir')],puf='Grafikte önce her dönemin değişimini hesapla, sonra ifadeleri sına.',sekil=S7)

# ===== 08 · kolay · öncüllü · iliski =====
d={'I':('Arı ve çiçekli bitki: Mutualizm',True,'arı nektar bulur, bitki tozlaşır; iki taraf da yararlanır'),
   'II':('Köpekbalığına tutunarak taşınan remora balığı: Kommensalizm',True,'remora köpekbalığıyla taşınıp artıklarla beslenir; köpekbalığı etkilenmez'),
   'III':('Aslan ve zebra: Parazitizm',False,'aslanın zebrayı yemesi avcılıktır; parazit konağı öldürmeden onunla beslenir')}
r=onc(d,'D')
q('0008','iliski','orta','öncüllü','Canlılar arası ilişkiler','Mutualizm, kommensalizm, parazitlik ve avcılığı ayırt eder.','ilişki eşleştirme',
 'Yarar/zarar durumuna göre ilişki türü belirlenir.','Avcılığı parazitlik sanmak.',
 oad(d),metin='Canlılar arasındaki ilişkiler, ilişkiye katılan canlıların yarar ya da zarar görmesine göre adlandırılır. Aşağıda bazı canlı çiftleri ile aralarındaki ilişkinin türü eşleştirilmiştir.\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nBu eşleştirmelerden hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru eşleştirmeler.',ip=['Her çiftte kimin yararlandığını, kimin zarar gördüğünü yaz.'],
 bilgi=[B('İlişki türleri','Mutualizm: iki taraf yararlanır · Kommensalizm: biri yararlanır, diğeri etkilenmez · Parazitlik: biri yararlanır, konak zarar görür · Avcılık: avcı yararlanır, av ölür')],puf='Yarar–zarar tablosunu çıkar: (+,+) mutualizm, (+,0) kommensalizm, (+,−) parazitlik veya avcılık.')

# ===== besin ağı çizimi =====
def ag(POS,KEN,lab=None,bend=None):
    lab=lab or {}; bend=bend or {}; b=[]
    for c,(x,y) in POS.items():
        b.append(f'\\node[draw,rounded corners=2pt,inner sep=3.5pt,line width=.9pt,align=center] ({nid(c)}) at ({x},{y}) {{{lab.get(c,c)}}};')
    for a_,c in KEN:
        s=f'[{ARR},line width=.9pt{","+bend[(a_,c)] if (a_,c) in bend else ""}]'
        b.append(f'\\draw{s} ({nid(a_)}) to ({nid(c)});' if (a_,c) in bend else f'\\draw{s} ({nid(a_)})--({nid(c)});')
    return tk(''.join(b))
# ===== 09 · orta · besin ağı =====
POS9={'Meşe':(1,0),'Ot':(6,0),'Sincap':(1,2),'Geyik':(6,2),'Ayı':(-1.2,4),'Kurt':(4.5,4)}
E9=[('Meşe','Sincap'),('Ot','Geyik'),('Sincap','Ayı'),('Geyik','Ayı'),('Meşe','Ayı'),('Sincap','Kurt'),('Geyik','Kurt')]
yer9=lambda a_,c:(a_,c) in E9
assert yer9('Meşe','Ayı') and yer9('Sincap','Ayı') and not yer9('Sincap','Geyik') and not yer9('Ayı','Kurt') and not yer9('Meşe','Kurt') and not yer9('Kurt','Ayı')
S9=ag(POS9,E9,bend={('Meşe','Ayı'):'bend left=28'})
it=[('Ayı hem bitkisel hem hayvansal kaynaklı besinlerle beslenir.',True,'ayı meşeyi (üretici) ve sincap ile geyiği (tüketici) yer'),
    ('Kurt, meşe ağacından doğrudan enerji alır.',False,'kurda enerji sincap ve geyik aracılığıyla ulaşır; meşeden kurda ok yoktur'),
    ('Sincap ve geyik ikincil tüketicidir.',False,'ikisi de doğrudan üreticiyle beslendiği için birincil tüketicidir'),
    ('Ot ortadan kalkarsa meşe ağacı da ortadan kalkar.',False,'ot ile meşe arasında besin ilişkisi yoktur; ot kalkınca doğrudan geyik etkilenir'),
    ('Ayı, kurt tarafından yenmektedir.',False,'ayıdan kurda ok yoktur; ikisi de sincap ve geyikle beslenir')]
r,g=tek(it,True,'C')
q('0009','agi','orta','şekilli','Besin ağı','Besin ağında oklardan beslenme biçimini ve tüketici basamağını yorumlar.','orman besin ağı, hepçil',
 'Oklar ve basamaklar okunarak ifadeler tek tek sınanır.','Ok yönünü ters okumak; dolaylı enerji aktarımını doğrudan saymak.',
 [A('Okları oku','Her ok yenen canlıdan yiyen canlıya gider.','Meşe → Sincap, Ayı · Ot → Geyik'),A('Ayıyı incele','Ayıya meşeden, sincaptan ve geyikten ok gelir.','bitki + hayvan'),A('Diğer canlıları incele','Kurt yalnız sincap ve geyiği yer; sincap ve geyik üreticiyi yer.','kurt: 2 av · sincap, geyik: birincil'),A('Sonucu yaz','Yalnız ayıyla ilgili ifade şekle uyar.','Doğru: ayı hepçil')],
 metin='Şekilde bir orman ekosisteminde yaşayan bazı canlılar arasındaki beslenme ilişkileri gösterilmiştir. Oklar yenen canlıdan yiyen canlıya doğrudur; meşe ve ot ekosistemin üreticileridir. Şekildeki canlıların dışında başka besin kaynağı yoktur.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Her ifadede söz edilen canlılar arasında ok var mı diye bak.'],
 bilgi=[B('Besin ağı','Birbirine bağlı besin zincirlerinin tümüdür · Hem bitki hem hayvanla beslenen canlıya hepçil denir (ayı gibi)')],puf='Okun başladığı canlı yenen, bittiği canlı yiyendir.',sekil=S9)

# ===== 10 · orta · besin ağı · olumsuz =====
POS10={'Buğday':(3,0),'Çekirge':(.4,1.8),'Fare':(5.6,1.8),'Kurbağa':(.4,3.6),'Yılan':(3,4.4),'Şahin':(3,6.2)}
E10=[('Buğday','Çekirge'),('Buğday','Fare'),('Çekirge','Kurbağa'),('Kurbağa','Yılan'),('Fare','Yılan'),('Fare','Şahin'),('Yılan','Şahin')]
besinler=lambda c:[a_ for a_,b_ in E10 if b_==c]
assert besinler('Kurbağa')==['Çekirge'] and besinler('Fare')==['Buğday'] and 'Çekirge' not in besinler('Fare') and 'Çekirge' not in besinler('Şahin')
S10=ag(POS10,E10)
it=[('Kurbağa, besin kaynağının azalması nedeniyle olumsuz etkilenir.',True,'kurbağanın tek besini çekirgedir'),
    ('Yılan, fareyle beslenmeyi artırarak besin sıkıntısını kısmen giderebilir.',True,'yılanın besinleri kurbağa ve farelerdir; kurbağa azalınca fare payı artar'),
    ('Çekirgelerin buğday üzerindeki baskısı azalır.',True,'çekirge sayısı azalınca tüketilen buğday miktarı da azalır'),
    ('Şahin, çekirgeyle doğrudan beslenmese de dolaylı olarak etkilenebilir.',True,'şahin yılanı yer; yılan kurbağa üzerinden çekirgeye bağlıdır'),
    ('Fare çekirgeyle beslendiği için fare popülasyonu da hemen azalır.',False,'fare çekirge yemez, buğdayla beslenir; çekirgenin azalması farenin besin kaynağını azaltmaz')]
r,g=tek(it,False,'E')
q('0010','agi','orta','şekilli','Besin ağı','Besin ağında bir canlının azalmasının diğer canlılara etkisini yorumlar.','tarla besin ağı, olumsuz kök',
 'Okların izlediği yoldan doğrudan ve dolaylı etkiler bulunur.','Fareyi çekirgeyle beslenen sanmak.',
 [A('Besin ilişkilerini yaz','Buğdayı çekirge ve fare yer; çekirgeyi kurbağa yer.','Buğday → Çekirge, Fare'),A('Çekirge azalınca doğrudan etkilenenleri bul','Besini yalnız çekirge olan kurbağa etkilenir; çekirgenin buğday baskısı azalır.','Kurbağa ↓'),A('Dolaylı etkiyi izle','Kurbağa azalınca yılan fareye, şahin de yılan ve fareye bağlı kalır.','Kurbağa → Yılan → Şahin'),A('Sonucu yaz','Fare çekirge yemediği için hemen azalmaz.','Yanlış: fare ifadesi')],
 metin='Şekilde bir tarla ekosistemindeki canlılar arasındaki beslenme ilişkileri gösterilmiştir. Oklar yenen canlıdan yiyen canlıya doğrudur. Tarlada bir hastalık nedeniyle çekirge popülasyonu kısa sürede büyük ölçüde azalmıştır.\nBuna göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Çekirgeyi kimlerin yediğine ve çekirgenin kimi yediğine ayrı ayrı bak.'],
 bilgi=[B('Besin ağında denge','Bir canlının azalması, onu yiyenleri doğrudan, o canlıya bağlı diğerlerini dolaylı etkiler')],puf='Önce doğrudan, sonra dolaylı etkileri okların üzerinden izle.',sekil=S10)

# ===== 11 · zor · öncüllü + zincir şekli · biyolojik birikim =====
DD=[('Plankton',Fr(4,100)),('Küçük balık',Fr(1,2)),('Büyük balık',Fr(2)),('Balıkçıl kuşu',Fr(25))]
assert DD[3][1]/DD[0][1]==625 and DD[2][1]/DD[1][1]==4 and all(DD[i][1]<DD[i+1][1] for i in range(3))
d={'I':('DDT derişimi, besin zincirinde ilerledikçe canlılarda artmaktadır.',True,'DDT yıkılmadan vücutta birikir; üst basamakta derişimi yüksektir (biyolojik birikim)'),
   'II':('Balıkçıl kuşundaki DDT derişimi, planktondakinin 600 katından fazladır.',True,'25 ÷ 0,04 = 625; derişim 625 kat artmıştır'),
   'III':('Büyük balıktaki DDT derişimi, küçük balıktakinin 8 katıdır.',False,'2 ÷ 0,5 = 4; derişim 4 kat fazladır')}
r=onc(d,'B')
q('0011','agi','orta','öncüllü','Biyolojik birikim','Besin zincirinde zehirli madde derişiminin basamaklarla artışını yorumlar.','zincirde DDT, oran hesabı',
 'Yıkılmayan madde üst basamaklarda birikir; oranlar verilerden hesaplanır.','Derişim farkını yanlış bölmek; birikimi tersine yorumlamak.',
 oad(d),metin='Bir göle yıllarca karışan DDT adlı böcek ilacının, gölün besin zincirindeki canlıların vücudunda biriktiği belirlenmiştir. Zincir plankton → küçük balık → büyük balık → balıkçıl kuşu biçimindedir ve canlıların vücudundaki DDT derişimleri sırasıyla 0,04 ppm, 0,5 ppm, 2 ppm ve 25 ppm olarak ölçülmüştür.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Derişimleri art arda oranlayarak karşılaştır.'],
 bilgi=[B('Biyolojik birikim','Canlı vücudunda yıkılmayan zehirli maddeler, besin zincirinde üst basamaklara çıkıldıkça daha yüksek derişimde birikir')],
 puf='Oranları bölerek bul: büyük değer ÷ küçük değer = kaç kat.',)

# ===== 12 · orta · piramit · iki bilinmeyen =====
U12=90000; X12=U12//10; Y12=X12//10; T12=Y12//10; assert (X12,Y12,T12)==(9000,900,90)
S12=piramit([('Üreticiler',f'{U12} kJ'),('Otçullar','X'),('Birincil etçiller','Y'),('İkincil etçiller',f'{T12} kJ')],W0=5.0,adim=1.0)
q('0012','piramit','orta','şekilli','Enerji piramidi','Çok basamaklı enerji piramidinde bilinmeyenleri %10 kuralıyla bulur.','piramit, iki bilinmeyen',
 'Basamaklar arası %10 aktarım zinciri ardışık uygulanır.','Yalnız bir bilinmeyeni bulup toplamı atlamak; üreticiyi toplama katmak.',
 [A('Aktarım kuralını yaz','Her basamakta enerjinin %10’u üst basamağa geçer.','× 0,1'),A('X’i bul','Üreticilerdeki enerjinin %10’u otçullara geçer.',f'{U12} × 0,1 = {X12}'),A('Y’yi bul','Otçullardaki enerjinin %10’u birincil etçillere geçer.',f'{X12} × 0,1 = {Y12}'),A('Verilenle sına','Y’nin %10’u ikincil etçillerdeki değeri verir.',f'{Y12} × 0,1 = {T12}'),A('Toplamı yaz','Sorulan yalnız X ve Y’nin toplamıdır.',f'{X12} + {Y12} = {X12+Y12}')],
 metin='Bir göl ekosisteminin enerji piramidi şekilde gösterilmiştir. Basamaklar arasında enerjinin yaklaşık %10’u bir üst basamağa aktarılmakta, geri kalanı canlıların yaşamsal faaliyetlerinde kullanılıp ısı olarak ortama verilmektedir. Piramitte yalnız üreticilerin ve en üst basamağın enerjisi verilmiştir.\nBuna göre X ve Y ile gösterilen basamaklardaki enerjilerin toplamı kaç kJ’dür?',
 dogru=X12+Y12,yan=[(Y12,'Yalnız Y’yi bulup X’i toplamaya katmamış.','dikkat'),(Y12+T12,'Y ile verilen en üst basamağı toplamış (900 + 90).','dikkat'),(X12,'Yalnız X’i bulmuş.','dikkat'),(U12+X12+Y12,'Üreticileri de toplamaya katmış.','dikkat')],
 istenen='X ve Y basamaklarının enerji toplamı (kJ).',ip=['Önce her iki bilinmeyeni ayrı ayrı bul, sonra istenen işlemi yap.'],
 bilgi=[B('%10 kuralı','Bir basamaktaki enerjinin yaklaşık %10’u üst basamağa aktarılır · Örnek: 700 kJ → 70 kJ')],puf='Üstten verilen değer varsa aşağı doğru 10 ile çarparak da doğrulayabilirsin.',sekil=S12)

# ===== 13 · orta · düz · olumsuz · sayı piramidi =====
it=[('Bu ekosistemin enerji piramidi de sayı piramidi gibi üst basamağı geniş olacak biçimde ters çizilir.',False,'enerji piramidi her zaman geniş üretici tabanından daralarak çıkar; enerji basamaklarda azalır'),
    ('Meşe ağacının birey sayısı az olsa da üreticiler ekosistemdeki enerjinin kaynağıdır.',True,'tüm enerji üreticilerin fotosentezle sağladığı organik maddeden gelir'),
    ('Sayı piramidindeki basamak genişliği, basamaktaki enerji miktarını doğrudan göstermez.',True,'sayı piramidi birey sayısını gösterir; bir ağaç çok sayıda böceği besleyebilir'),
    ('Tırtıl sayısı tek ağaca göre çok fazla olduğundan sayı piramidinin tabanı dar kalır.',True,'tek ağaç binlerce tırtılı besleyebildiği için taban dar görünür'),
    ('Kuşlar, ağacın sentezlediği organik maddeden tırtıllar aracılığıyla dolaylı yararlanır.',True,'enerji ağaçtan tırtıla, tırtıldan kuşa akar')]
r,g=tek(it,False,'A')
q('0013','piramit','kolay','düz','Sayı piramidi','Sayı piramidinin ters olabileceğini, enerji piramidinin ise olamayacağını bilir.','sayı piramidi, olumsuz kök',
 'Sayı piramidi bazı ekosistemlerde ters olabilir; enerji piramidi olamaz.','Sayı piramidindeki biçimi enerji piramidine de uygulamak.',
 [A('Verileri sırala','Bir meşe ağacı, binlerce tırtıl ve onlarca kuş var.','1 · 5000 · 40'),A('Sayı piramidini yorumla','Taban en dar, orta basamak en geniştir; bu piramit ters biçimlidir.','sayı piramidi bozuk'),A('Enerjiyi yorumla','Enerji akışında her basamakta enerji azalır; taban her zaman en geniştir.','enerji piramidi düz'),A('Sonucu yaz','Enerji piramidinin de ters çizildiğini söyleyen ifade yanlıştır.','Yanlış: enerji piramidi ters')],
 metin='Bir orman ekosisteminde 1 meşe ağacı, bu ağacın yapraklarıyla beslenen 5000 tırtıl ve bu tırtılları yiyen 40 kuş yaşamaktadır. Bu veriler sayı piramidi olarak çizildiğinde piramidin tabanı en dar basamak olarak kalmaktadır.\nBuna göre bu ekosistemle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Sayı piramidinin neyi, enerji piramidinin neyi gösterdiğine bak.'],
 bilgi=[B('Besin piramitleri','Enerji, sayı ve biyokütle piramitleri basamaklardaki enerjiyi, birey sayısını ve toplam kütleyi gösterir')],puf='Piramit türünü adlandır: enerji piramidi ters olamaz, sayı piramidi olabilir.')

# ===== 14 · orta · öncüllü · piramit =====
d={'I':('Enerji piramidinin en geniş basamağını üreticiler oluşturur.',True,'enerji kaynağı üreticilerdir ve en çok enerji bu basamaktadır'),
   'II':('Basamaklar yükseldikçe bir üst basamağa aktarılan enerjinin yüzdesi artar.',False,'her basamakta aktarılan oran yaklaşık %10’dur; azalan, enerjinin miktarıdır'),
   'III':('Üst basamaklardaki canlıların toplam biyokütlesi, alt basamaklardakinden genellikle daha azdır.',True,'enerji azaldığı için üst basamakları besleyecek madde de azalır')}
r=onc(d,'C')
q('0014','piramit','kolay','öncüllü','Besin piramitleri','Enerji ve biyokütle piramidi ilkelerini yorumlar.','piramit ilkeleri öncüllü',
 'Aktarım oranı sabit, miktar azalır; biyokütle de azalır.','Aktarılan yüzdeyi artıyor sanmak.',
 oad(d),metin='Besin piramitleri, bir ekosistemde basamaklar boyunca enerji, biyokütle ya da birey sayısındaki değişimi gösterir. Besin piramitlerinde basamaklar üretici ile başlar ve tüketicilerle yükselir.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Üst basamakta enerjiye ve yüzdeye ayrı ayrı bak.'],
 bilgi=[B('Besin piramitleri','Piramidin her basamağı bir beslenme düzeyini gösterir; basamak genişliği enerjiyi, biyokütleyi ya da birey sayısını temsil eder')],puf='Yüzde sabit, miktar azalır.')

# ===== döngü çizimi =====
def dongu(POS,OK_,lab=None):
    """OK_: (a,b,no|None,bend|None)"""
    lab=lab or {}; b=[]
    for c,(x,y) in POS.items(): b.append(f'\\node[draw,rounded corners=2pt,inner sep=3.5pt,line width=.9pt,align=center] ({nid(c)}) at ({x},{y}) {{{lab.get(c,c)}}};')
    for a_,c,no,bd in OK_:
        st=f'[{ARR},line width={"1" if no else ".6"}pt{",gray" if not no else ""}]'
        nn=f' node[midway,circle,draw,fill=white,inner sep=1.3pt,font=\\small\\bfseries] {{{no}}}' if no else ''
        b.append(f'\\draw{st} ({nid(a_)}) to{"["+bd+"]" if bd else ""}{nn} ({nid(c)});')
    return tk(''.join(b))
# ===== 15 · orta · su döngüsü =====
P15={'Deniz':(0,0),'Bulut':(3.4,3.4),'Bitki':(6.8,2.0),'Toprak':(6.8,0)}
S15=dongu(P15,[('Deniz','Bulut',1,None),('Bitki','Bulut',2,None),('Bulut','Toprak',3,None),('Toprak','Deniz',4,None)])
it=[('2 numaralı ok, bitkilerden atmosfere su buharı geçişini (terleme) gösterir.',True,'bitkiler yapraklarından su buharı verir; buna terleme denir'),
    ('1 numaralı ok, bitkilerin terlemesini gösterir.',False,'1 numaralı ok denizden atmosfere su geçişini (buharlaşmayı) gösterir'),
    ('3 numaralı ok, suyun buharlaşmasını gösterir.',False,'3 numaralı ok bulutlardan yeryüzüne su dönüşünü (yağışı) gösterir'),
    ('4 numaralı ok, suyun yağışla bulutlardan yeryüzüne inişini gösterir.',False,'4 numaralı ok yeryüzünden denize su akışını gösterir'),
    ('Su döngüsünün sürmesi için Güneş enerjisine gerek yoktur.',False,'buharlaşma Güneş enerjisiyle gerçekleşir; döngü bu enerjiyle sürer')]
r,g=tek(it,True,'E')
q('0015','dongu','kolay','şekilli','Su döngüsü','Şematik su döngüsünde olayları numaralı oklardan okur.','su döngüsü şeması',
 'Okun başlangıç ve bitişindeki ortamdan olay belirlenir.','Terlemeyi buharlaşmayla karıştırmak; Güneş’in rolünü unutmak.',
 [A('Okları oku','Her okun nereden nereye gittiğine bak.','1: deniz → bulut · 2: bitki → bulut'),A('Olayları adlandır','Denizden buhar çıkışı buharlaşma, bitkiden çıkış terleme, buluttan iniş yağıştır.','1 buharlaşma · 2 terleme · 3 yağış'),A('Dönüşü incele','4 numaralı ok yüzey akışıyla suyun denize dönüşünü gösterir.','4 akış'),A('Sonucu yaz','Yalnız terlemeyi doğru adlandıran ifade doğrudur.','2: terleme')],
 metin='Şekilde suyun doğadaki dolaşımı şematik olarak gösterilmiştir. Oklar suyun bir ortamdan diğerine geçişini, numaralar da bu geçişleri sağlayan olayları belirtmektedir. Dolaşım boyunca yeryüzündeki toplam su miktarı değişmemektedir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Her okun başladığı ve bittiği ortamı oku.'],
 bilgi=[B('Su döngüsü','Su, yeryüzü ile atmosfer arasında sürekli dolaşır; bu dolaşım Güneş enerjisiyle sürer')],puf='Önce okun yönünü, sonra ortamın değişimini oku.',sekil=S15)

# ===== 16 · orta · karbon döngüsü · öncüllü =====
P16={'Atmosfer (CO$_2$)':(3.5,3.9),'Bitkiler':(0.2,1.6),'Hayvanlar':(3.5,1.6),'Ölü canlılar ve atıklar':(6.6,1.6)}
A_,Bk,Hy,Ol='Atmosfer (CO$_2$)','Bitkiler','Hayvanlar','Ölü canlılar ve atıklar'
S16=dongu(P16,[(A_,Bk,1,'bend right=14'),(Bk,A_,2,'bend right=14'),(Bk,Hy,3,None),(Hy,A_,4,None),(Ol,A_,5,None),(Bk,Ol,None,'bend right=38'),(Hy,Ol,None,None)])
d={'I':('1 numaralı ok, fotosentezi gösterir.',True,'atmosferdeki CO2’nin bitkilerde organik maddeye geçişi fotosentezdir'),
   'II':('5 numaralı ok, ayrıştırıcıların etkinliğiyle karbonun CO2 olarak atmosfere dönüşünü gösterir.',True,'ayrıştırıcılar ölü kalıntıları ayrıştırırken solunumla CO2 verir'),
   'III':('4 numaralı ok, hayvanlarda gerçekleşen fotosentezi gösterir.',False,'4 numaralı ok hayvanların solunumla CO2 vermesini gösterir; hayvanlar fotosentez yapmaz')}
r=onc(d,'B')
q('0016','dongu','orta','şekilli','Karbon döngüsü','Karbon döngüsünde numaralı oklarla gösterilen süreçleri belirler.','karbon döngüsü şeması, öncüllü',
 'Karbon atmosferden fotosentezle girer; solunum ve ayrışmayla geri döner.','Hayvanlarda fotosentez olduğunu sanmak; bitkilerin solunum yaptığını unutmak.',
 oad(d),metin='Şekilde karbonun doğadaki dolaşımı şematik olarak gösterilmiştir. Numaralı oklar karbonun bir ortamdan diğerine geçişini belirtmektedir; numarasız oklar canlıların ölmesiyle ilgilidir.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Atmosfere giden ve atmosferden gelen okların hangi süreçleri anlattığını ayır.'],
 bilgi=[B('Karbon döngüsü','Karbon, atmosferde CO2, canlılarda organik madde biçiminde dolaşır')],puf='Atmosferden canlıya fotosentez, canlıdan atmosfere solunum ve ayrışma.',sekil=S16)

# ===== 17 · orta · azot döngüsü · olumsuz =====
N2,Am,Ni,Bt,Hv,Ob='Atmosferdeki N$_2$','Amonyak','Nitrat','Bitkiler','Hayvanlar','Ölü canlılar'
P17={N2:(3.5,4.0),Am:(0.4,2.0),Ni:(6.6,2.0),Bt:(6.6,0),Hv:(3.5,0),Ob:(0.4,0)}
S17=dongu(P17,[(N2,Am,1,None),(Am,Ni,2,None),(Ni,N2,3,None),(Ni,Bt,4,None),(Bt,Hv,5,None),(Ob,Am,6,None),(Hv,Ob,None,None),(Bt,Ob,None,'bend right=30')])
it=[('1 numaralı ok, azot bağlayıcı bakterilerin etkinliğini gösterir.',True,'N2’yi amonyağa çeviren azot bağlayıcı bakterilerdir'),
    ('3 numaralı ok, denitrifikasyon bakterilerinin etkinliğini gösterir.',True,'nitratı N2’ye çeviren bakterilere denitrifikasyon bakterileri denir'),
    ('4 numaralı ok, bitkilerin nitratı topraktan almasını gösterir.',True,'bitkiler azotu nitrat biçiminde kökleriyle alır'),
    ('2 numaralı ok, denitrifikasyon bakterilerinin etkinliğini gösterir.',False,'2 numaralı ok amonyağın nitrata dönüşmesini gösterir; bunu nitrifikasyon bakterileri yapar'),
    ('6 numaralı ok, ayrıştırıcıların ölü canlılardaki azotlu bileşikleri amonyağa dönüştürmesini gösterir.',True,'ayrıştırıcılar ölü organik maddedeki azotu amonyak olarak serbest bırakır')]
r,g=tek(it,False,'D')
q('0017','dongu','orta','şekilli','Azot döngüsü','Şematik azot döngüsünde numaralı oklarla süreç ve canlıları eşleştirir.','azot döngüsü şeması, olumsuz kök',
 'Maddenin biçim değişiminden süreç ve görevli bakteri belirlenir.','Nitrifikasyon ile denitrifikasyonu karıştırmak.',
 [A('Okları oku','Her okun başladığı ve bittiği maddeyi yaz.','1: N2 → amonyak · 2: amonyak → nitrat · 3: nitrat → N2'),A('Süreçleri adlandır','N2 → amonyak bağlama, amonyak → nitrat nitrifikasyon, nitrat → N2 denitrifikasyondur.','bağlama · nitrifikasyon · denitrifikasyon'),A('Bitki ve ayrıştırıcıyı incele','4 numaralı ok bitkinin nitratı alışını, 6 numaralı ok ayrışmayı gösterir.','4 alım · 6 ayrışma'),A('Sonucu yaz','2 numaralı oku denitrifikasyon saymak yanlıştır.','Yanlış: 2 nitrifikasyon')],
 metin='Şekilde azotun doğadaki dolaşımı şematik olarak gösterilmiştir. Numaralı oklar azotun bir maddeden ya da canlıdan diğerine geçişini belirtmektedir; numarasız ok hayvanların ölümüyle ilgilidir.\nBuna göre şekildeki numaralı oklarla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Her okta azotun hangi maddeden hangisine döndüğünü yaz.'],
 bilgi=[B('Azot döngüsü','Bazı bakteriler azotu bir bileşikten diğerine dönüştürerek döngünün sürmesini sağlar')],puf='Önce maddenin dönüşümünü yaz, sonra süreci adlandır.',sekil=S17)

# ===== 18 · orta · tablo deney · öncüllü =====
D18=[('1','Azotlu','Yok',Fr(40,10)),('2','Azotsuz','Yok',Fr(10,10)),('3','Azotsuz','Var',Fr(41,10)),('4','Azotlu','Var',Fr(40,10))]
assert D18[2][3]-D18[1][3]>3 and D18[3][3]==D18[0][3]
S18=tablo_svg(['Grup','Toprak','Rhizobium','Ort. kuru kütle (g)'],[[a,b,c,fm(v)] for a,b,c,v in D18])
d={'I':('Azotsuz toprakta Rhizobium, bitkinin kuru kütlesini artırmıştır.',True,'azotsuz topraktaki 2. ve 3. gruplar yalnız bakteri bakımından farklıdır ve bakterili grubun ortalama kütlesi çok daha fazladır'),
   'II':('Rhizobium, azotlu toprakta da bitkinin kuru kütlesini belirgin biçimde artırmıştır.',False,'azotlu topraktaki 1. ve 4. grupların ortalama kütleleri eşittir; bakteri bu toprakta kütleyi artırmamıştır'),
   'III':('Bu deney, bitki ile Rhizobium arasındaki ilişkinin mutualizm olduğunu kanıtlar.',False,'tablo yalnız bitkinin kütlesini gösterir; bakterinin bitkiden yarar sağladığına ilişkin veri yoktur, bu yüzden mutualizm tablodan kanıtlanamaz')}
r=onc(d,'A')
q('0018','iliski','orta','tablo','Simbiyotik ilişki deneyi','Deney sonuçlarından değişken etkisini ve ilişki türünü yorumlar.','tablo, deney, öncüllü',
 'Yalnız bir etmenin farklı olduğu gruplar karşılaştırılır.','Veriyle desteklenmeyen sonucu kanıtlanmış saymak; karşılaştırmada birden çok etmeni birlikte değiştirmek.',
 oad(d),metin='Bir araştırmacı, baklagil bitkisinin gelişimi üzerinde Rhizobium bakterisinin etkisini incelemek için her birinde 20 fide bulunan dört grup hazırlamıştır. Her gruba aynı miktarda ışık ve su verilmiş, 30 gün sonra bitkilerin ortalama kuru kütlesi ölçülmüştür. Sonuçlar tabloda verilmiştir.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Karşılaştırdığın iki grupta yalnız tek etmenin farklı olması gerekir.'],
 bilgi=[B('Deney değişkenleri','Bağımsız değişken: araştırmacının değiştirdiği etmen · Bağımlı değişken: ölçülen sonuç · Karşılaştırmada yalnız bir etmen farklı olmalıdır')],puf='Etkiyi görmek için yalnız tek etmeni farklı olan grupları karşılaştır.',sekil=S18)

# ===== 19 · orta · grafik · popülasyon S eğrisi =====
G19=[(0,100),(2,200),(4,400),(6,800),(8,900),(10,1000),(12,1000),(14,1000)]
art=[G19[i+1][1]-G19[i][1] for i in range(7)]; assert art==[100,200,400,100,100,0,0] and art.index(max(art))==2
gx=lambda t:t*.6; gy=lambda v:v*.0045
b=[f'\\draw[thick,{ARR}] (0,0)--(9.0,0);\\draw[thick,{ARR}] (0,0)--(0,5.0);']
for t in range(0,15,2): b.append(f'\\draw ({gx(t):.2f},0)--({gx(t):.2f},-.1) node[below] {{{t}}};')
for v in range(0,1001,100): b.append(f'\\draw (0,{gy(v):.2f})--(-.1,{gy(v):.2f}) node[left,font=\\footnotesize] {{{v}}};\\draw[gray!35] (0,{gy(v):.2f})--(8.6,{gy(v):.2f});')
b.append('\\draw[line width=1.5pt,vurgu,smooth] plot[smooth] coordinates {'+' '.join(f'({gx(t):.2f},{gy(v):.2f})' for t,v in G19)+'};')
for t,v in G19: b.append(f'\\fill[vurgu] ({gx(t):.2f},{gy(v):.2f}) circle (.07);')
b.append('\\node[anchor=north west] at (3.4,-.6) {Zaman (yıl)};\\node[anchor=south] at (.6,5.1) {Birey sayısı};')
S19=tk(''.join(b))
d={'I':('Popülasyonun en hızlı büyüdüğü aralık 6. ve 8. yıllar arasıdır.',False,'en büyük artış 4. ve 6. yıllar arasındadır (400 birey); 6–8. yıllar arasında artış 100 bireydir'),
   'II':('Popülasyon büyüklüğü 14. yıla kadar sürekli artmıştır.',False,'10. yıldan sonra popülasyon büyüklüğü 1000’de sabit kalmıştır'),
   'III':('10. yıldan sonra popülasyonda doğum ve ölüm sayıları yaklaşık olarak dengededir.',True,'büyüklük değişmediğine göre doğum ve ölüm sayıları birbirine eşittir; ortam taşıma kapasitesine ulaşmıştır')}
r=onc(d,'C')
q('0019','populasyon','zor','grafik','Popülasyon büyüme grafiği','Popülasyon büyüme grafiğinden artış hızını ve taşıma kapasitesini yorumlar.','S tipi büyüme, öncüllü',
 'Artış miktarları aralıklarla karşılaştırılır; sabit bölge doğum–ölüm dengesidir.','Sabitlenmeyi doğumların durması sanmak.',
 oad(d),metin='Bir adaya bırakılan geyik topluluğunun büyüklüğü yıllar boyunca izlenmiş ve sonuçlar grafikte gösterilmiştir. Adadaki besin ve yaşam alanı sınırlıdır; adaya dışarıdan geyik girişi ya da adadan çıkışı olmamıştır.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Aralıklar arasındaki artış miktarlarını tek tek bul.'],
 bilgi=[B('Taşıma kapasitesi','Bir ortamın sürdürebileceği en fazla birey sayısıdır; bu düzeyde doğum ve ölüm sayıları yaklaşık dengelenir')],puf='Eğri düzleşince doğum ≈ ölüm; en dik bölge en hızlı artıştır.',sekil=S19)

# ===== 20 · orta · grafik · avcı–av =====
av=lambda t:600+300*math.sin(2*math.pi*t/10); avc=lambda t:250+100*math.sin(2*math.pi*(t-2)/10)
ta=max(range(0,101),key=lambda i:av(i/10)); tc=max(range(0,101),key=lambda i:avc(i/10)); assert 0<tc-ta<=30 and abs((tc-ta)/10-2)<1e-9 and min(range(0,101),key=lambda i:av(i/10))==75 and avc(7.5)<max(avc(i/10) for i in range(101))-100
gx=lambda t:t*.45; gy=lambda v:v*.0045
b=[f'\\draw[thick,{ARR}] (0,0)--(9.6,0);\\draw[thick,{ARR}] (0,0)--(0,5.0);']
for t in range(0,21,5): b.append(f'\\draw ({gx(t):.2f},0)--({gx(t):.2f},-.1) node[below] {{{t}}};')
for v in range(0,1001,250): b.append(f'\\draw (0,{gy(v):.2f})--(-.1,{gy(v):.2f}) node[left] {{{v}}};')
b.append('\\draw[line width=1.5pt,smooth] plot[smooth] coordinates {'+' '.join(f'({gx(t):.2f},{gy(av(t)):.2f})' for t in range(0,21))+'};')
b.append('\\draw[line width=1.5pt,vurgu,dashed,smooth] plot[smooth] coordinates {'+' '.join(f'({gx(t):.2f},{gy(avc(t)):.2f})' for t in range(0,21))+'};')
b.append(f'\\node[anchor=south west] at ({gx(2.2):.2f},{gy(900):.2f}) {{Av}};\\node[vurgu,anchor=south] at ({gx(4.5):.2f},{gy(350)+.12:.2f}) {{Avcı}};')
b.append('\\node[anchor=north west] at (3.6,-.6) {Zaman (yıl)};\\node[anchor=south] at (.8,5.1) {Birey sayısı};')
S20=tk(''.join(b))
it=[('Av popülasyonunun en düşük olduğu yılda avcı popülasyonu en yüksek değerindedir.',False,'av en düşük 7,5 ve 17,5. yıllarda, avcı en yüksek 4,5 ve 14,5. yıllardadır'),
    ('Av ve avcı popülasyonlarının büyüklüğü zamanla sürekli artar.',False,'iki popülasyon da artıp azalarak dalgalanır'),
    ('Avcı popülasyonu, av popülasyonunu kısa sürede tamamen yok eder.',False,'av sayısı azalsa da sıfırlanmaz; avcı sayısı azalınca av yeniden artar'),
    ('Avcı popülasyonu, av sayısından bağımsız olarak dalgalanır.',False,'avcıdaki değişim av sayısındaki değişimi izler'),
    ('Avcı popülasyonu en yüksek değerine, av popülasyonunun zirvesinden yaklaşık 2 yıl sonra ulaşır.',True,'avcının besini olan av artınca avcı beslenir ve çoğalır; bu yüzden avcı eğrisi av eğrisinin gerisindedir')]
r,g=tek(it,True,'E')
q('0020','populasyon','orta','grafik','Avcı–av ilişkisi grafiği','Avcı ve av popülasyon büyüklüklerinin birbirini izleyen dalgalanmasını yorumlar.','avcı–av grafiği',
 'Av artınca avcı gecikmeyle artar; avcı artınca av azalır.','Avcı ve avın aynı anda değiştiğini sanmak.',
 [A('Eğrileri ayır','Sürekli çizgi av, kesikli çizgi avcıdır.','av: sürekli · avcı: kesikli'),A('Zirveleri karşılaştır','Av eğrisi avcı eğrisinden daha önce yükselir ve düşer.','av zirvesi önce'),A('Nedeni düşün','Avcı sayısı, besini olan avın artmasından sonra artar.','av ↑ → avcı ↑'),A('Sonucu yaz','Avcının artışı avın artışından sonra görülür.','Gecikmeli artış')],
 metin='Bir ormanda uzun yıllar boyunca yapılan gözlemlerde, bir av popülasyonu ile bu avı besin olarak kullanan avcı popülasyonunun büyüklükleri ölçülmüş ve sonuçlar grafikte gösterilmiştir. Ormanda başka bir av ya da avcı bulunmamaktadır.\nBu grafiğe göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Eğrilerin tepe noktalarının x değerlerine bak.'],
 bilgi=[B('Avcı–av ilişkisi','Av çoğalınca avcıya besin artar, avcı çoğalınca av azalır; iki popülasyon dalgalı biçimde birbirini izler')],puf='Besini olan canlı artar, onu yiyen gecikmeyle artar.',sekil=S20)

# ===== 21 · orta · düz · olumsuz · küresel ısınma =====
it=[('Buzulların erimesi, deniz seviyesinin yükselmesine yol açar.',True,'eriyen kara buzulları denizlere su katar'),
    ('Küresel ısınma, ozon tabakasındaki incelmenin doğrudan sonucudur.',False,'küresel ısınma sera gazlarının artmasıyla oluşur; ozon incelmesi ise CFC gibi maddelerden kaynaklanan ayrı bir sorundur'),
    ('Yağış rejiminin değişmesi bazı bölgelerde kuraklığa yol açabilir.',True,'sıcaklık artışı yağış dağılımını değiştirir'),
    ('Isınmaya uyum sağlayamayan bazı canlı türlerinin yaşam alanları daralabilir.',True,'iklim değişince uygun yaşam alanı azalan türler tehlikeye girer'),
    ('Atmosferdeki sera gazı derişiminin artması, küresel ısınmanın temel nedenidir.',True,'sera gazları ısıyı tutar')]
r,g=tek(it,False,'B')
q('0021','cevre','kolay','düz','Küresel ısınma','Küresel ısınmanın neden ve sonuçlarını diğer çevre sorunlarından ayırır.','küresel ısınma, olumsuz kök',
 'Küresel ısınma sera gazlarıyla, ozon incelmesi CFC ile ilişkilidir.','Küresel ısınma ile ozon incelmesini aynı sorun sanmak.',
 [A('Nedeni belirle','Küresel ısınmanın nedeni sera gazlarının artmasıdır.','CO2, metan ↑'),A('Sonuçları sırala','Buzul erimesi, yağış değişimi ve yaşam alanı kaybı ısınmanın sonuçlarındandır.','4 ifade doğru'),A('Ozonu ayır','Ozon incelmesi CFC gibi maddelerle oluşan ayrı bir sorundur.','ısınma ≠ ozon'),A('Sonucu yaz','Ozonu ısınmanın nedeni gösteren ifade yanlıştır.','Yanlış: ozon ifadesi')],
 metin='Dünya genelinde ortalama sıcaklığın yıllar içinde artması küresel ısınma olarak adlandırılır. Bu değişim, doğal yaşamı ve insan etkinliklerini çeşitli yönlerden etkilemektedir. Bilim insanları ısınmanın nedenleri ve sonuçlarını birçok farklı ölçümle izlemektedir.\nBuna göre küresel ısınma ile ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Isınmanın nedeni olarak hangi gaz grubu sayılır?'],
 bilgi=[B('Sera gazları','Sera gazları, yeryüzünden yayılan ısıyı tutan atmosfer gazlarıdır')],puf='Her çevre sorununu kendi nedeniyle eşleştir.')

# ===== 22 · zor · tablo · öncüllü · su kirliliği =====
T22=[('A','Yok',Fr(2,100),'Az',9,14),('B','Orta',Fr(30,100),'Çok',5,9),('C','Yoğun',Fr(110,100),'Çok yoğun',2,3)]
assert T22[0][2]<T22[1][2]<T22[2][2] and T22[0][4]>T22[1][4]>T22[2][4] and T22[0][5]>T22[1][5]>T22[2][5]
S22=tablo_svg(['Göl','Gübre','Fosfat (mg/L)','Alg','O2 (mg/L)','Balık türü'],[[a,b,fm(c),dd,str(e),str(f)] for a,b,c,dd,e,f in T22])
d={'I':('Çevredeki gübre kullanımı arttıkça gölün fosfat derişimi artmıştır.',True,'gübre kullanımı Yok, Orta, Yoğun arttıkça fosfat 0,02, 0,3 ve 1,1 mg/L olmuştur'),
   'II':('Alg yoğunluğu arttıkça sudaki çözünmüş oksijen miktarı artmıştır.',False,'alg yoğunluğu artarken oksijen 9, 5 ve 2 mg/L’ye düşmüştür; ölen algleri ayrıştıranlar oksijeni tüketir'),
   'III':('Çözünmüş oksijen azaldıkça göldeki balık türü sayısı azalmıştır.',True,'oksijen 9’dan 2’ye düşerken balık türü sayısı 14’ten 3’e inmiştir')}
r=onc(d,'D')
q('0022','cevre','orta','tablo','Su kirliliği','Gübre kaynaklı su kirliliğinin zincirleme etkilerini tablodan yorumlar.','tablo, su kirliliği, öncüllü',
 'Tablodaki değişkenler sırayla karşılaştırılarak neden–sonuç zinciri kurulur.','Alg çoğalınca oksijenin arttığını sanmak.',
 oad(d),metin='Aynı bölgedeki üç gölün çevresindeki tarım alanlarında kullanılan gübre miktarı farklıdır. Araştırmacılar bu gölleri incelemiş, sonuçları tabloda göstermiştir. Göllerin büyüklüğü, derinliği ve sıcaklığı birbirine yakındır.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Tabloda her sütunun gölden göle nasıl değiştiğine bak.'],
 bilgi=[B('Su kirliliği','Gübre ve deterjan gibi maddeler suyu besin elementleriyle zenginleştirir; algler çoğalır, ölünce ayrıştırıcılar oksijeni tüketir')],puf='Sütunları sırayla izle: artan ile artan, artan ile azalan.',sekil=S22)

# ===== 23 · orta · grafik · erozyon deneyi =====
E23=[('A','Çıplak',120),('B','Çimli',30),('C','Fidanlı',10)]
assert E23[1][2]*4==E23[0][2] and E23[2][2]<E23[1][2]
b=[f'\\draw[thick,{ARR}] (0,0)--(7.2,0);\\draw[thick,{ARR}] (0,0)--(0,4.9);']
for v in (0,40,80,120): b.append(f'\\draw (0,{v*.036:.2f})--(-.1,{v*.036:.2f}) node[left] {{{v}}};\\draw[gray!35] (0,{v*.036:.2f})--(6.9,{v*.036:.2f});')
for i,(k,ad_,v) in enumerate(E23):
    x=1.1+i*2.1; b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.12] ({x-.6:.2f},0) rectangle ({x+.6:.2f},{v*.036:.2f});\\draw[line width=1pt] ({x-.6:.2f},0) rectangle ({x+.6:.2f},{v*.036:.2f});\\node[below,align=center] at ({x:.2f},-.05) {{{ad_}}};\\node[above] at ({x:.2f},{v*.036:.2f}) {{{v}}};')
b.append('\\node[anchor=south] at (.9,5.0) {Taşınan toprak (g)};')
S23=tk(''.join(b))
it=[('Bağımsız değişken yağmur şiddetidir.',False,'yağmur şiddeti tüm tepsilerde aynı tutulmuştur; değiştirilen değişken bitki örtüsüdür'),
    ('Ağaç fidanlı tepsiden taşınan toprak, çimli tepsiden taşınandan fazladır.',False,'ağaç fidanlı tepsiden 10 g, çimli tepsiden 30 g toprak taşınmıştır'),
    ('Bağımsız değişken toprak yüzeyindeki bitki örtüsü, bağımlı değişken ise taşınan toprak miktarıdır.',True,'araştırmacı bitki örtüsünü değiştirmiş, taşınan toprağı ölçmüştür'),
    ('Sonuçlar, eğimin erozyonu etkilemediğini gösterir.',False,'eğim tüm tepsilerde aynıdır; bu deneyle eğimin etkisi sınanamaz'),
    ('Çimli tepsiden taşınan toprak, çıplak tepsiden taşınanın yarısı kadardır.',False,'30 g, 120 g’ın dörtte biridir')]
r,g=tek(it,True,'C')
q('0023','cevre','orta','grafik','Erozyon deneyi','Erozyon deneyinde değişkenleri ve sonuçları yorumlar.','erozyon deneyi, grafik',
 'Değişen etmen bağımsız, ölçülen sonuç bağımlı değişkendir; bitki örtüsü erozyonu azaltır.','Sabit tutulan etmeni bağımsız değişken saymak.',
 [A('Değişkenleri ayır','Tepsilerde değiştirilen etmen yüzeydeki bitki örtüsü, ölçülen sonuç taşınan topraktır.','bağımsız: örtü · bağımlı: toprak'),A('Sabit etmenleri belirle','Eğim, toprak miktarı ve yağmur her tepside aynıdır.','sabit: eğim, yağmur'),A('Verileri oku','Taşınan toprak 120, 30 ve 10 g’dır.','120 > 30 > 10'),A('İfadeleri ele','Yalnız değişkenleri doğru tanımlayan ifade doğrudur.','Doğru: değişken tanımı')],
 metin='Bir öğrenci, eğimi, toprak miktarını ve toprak cinsini aynı olan üç tepsiden birini çıplak, birini çimle kaplı, birini ağaç fidanlı hazırlamıştır. Üç tepsiye de aynı şiddette ve sürede yağmur yağdırmış, akan suyla taşınan toprağı toplayıp tartmıştır. Sonuçlar grafikte verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Her tepside neyin aynı, neyin farklı olduğunu yaz.'],
 bilgi=[B('Erozyon','Toprağın su ya da rüzgârla taşınmasıdır; bitki örtüsü kökleriyle toprağı tutarak erozyonu azaltır')],puf='Değiştirilen etmen bağımsız, ölçülen sonuç bağımlı değişkendir.',sekil=S23)

# ===== 24 · zor · besin ağı + enerji =====
K24,L24=10000,6000; M24=(K24+L24)//10; N24=M24//10; P24_=N24//10; assert (M24,N24,P24_)==(1600,160,16) and K24//1000==10 and L24//1000==6
P24={'Üretici':(3,0),'K':(.2,1.9),'L':(5.8,1.9),'M':(3,3.8),'N':(3,5.6),'P':(3,7.4)}
S24=ag(P24,[('Üretici','K'),('Üretici','L'),('K','M'),('L','M'),('M','N'),('N','P')],lab={'K':'Otçul K\\\\10000 kJ','L':'Otçul L\\\\6000 kJ','M':'Etçil M','N':'Etçil N','P':'Üst etçil P'})
q('0024','agi','zor','şekilli','Besin ağında enerji','Besin ağında birden çok kaynaktan gelen enerjiyi %10 kuralıyla toplayıp aktarır.','ağda enerji hesabı',
 'Etçil iki otçuldan da %10 alır; sonra üst etçile %10 aktarır.','Yalnız tek kolu hesaplamak; son aktarımı atlamak.',
 [A('Okları oku','M, hem K hem L ile beslenir; N yalnız M’yi, P yalnız N’yi yer.','K, L → M → N → P'),A('M’nin enerjisini bul','K’dan ve L’den %10’ar aktarılır, bunlar toplanır.','10000 × 0,1 + 6000 × 0,1 = 1000 + 600 = 1600'),A('N’ye aktarımı bul','M’deki enerjinin %10’u N’ye geçer.','1600 × 0,1 = 160'),A('P’ye aktarımı bul','N’deki enerjinin %10’u P’ye geçer.','160 × 0,1 = 16'),A('Sonucu yaz','P’nin bu kaynaktan edindiği enerji 16 kJ’dür.','16 kJ')],
 metin='Şekilde bir ekosistemdeki canlılar arasındaki beslenme ilişkisi ve otçul K ile L canlılarının içerdiği enerji miktarları verilmiştir. Oklar enerjinin akış yönünü gösterir. K ve L canlılarını yalnız M, M canlısını yalnız N, N canlısını yalnız P yemektedir. Her canlı, kendisini yiyen canlıya enerjisinin %10’unu aktarmaktadır.\nBuna göre P canlısına aktarılan enerji kaç kJ’dür?',
 dogru=P24_,yan=[(K24//1000,'Yalnız K koluyla hesaplamış; L’den gelen enerjiyi atlamış (10000 × 0,1 × 0,1 × 0,1).','dikkat'),(L24//1000,'Yalnız L koluyla hesaplamış; K’dan gelen enerjiyi atlamış.','dikkat'),(N24,'N’nin enerjisini bulup P’ye aktarımı hesaplamamış.','dikkat'),(K24+L24,'Enerjinin aktarımda azalmadığını sanmış (K + L).','bilgi')],
 istenen='P’ye aktarılan enerji (kJ).',ip=['Aynı basamağa gelen kaynakları nasıl birleştirirsin?'],
 bilgi=[B('%10 kuralı','Her basamakta enerjinin yaklaşık %10’u yiyen canlıya geçer; birden çok kaynak varsa aktarılanlar toplanır')],puf='Önce aynı basamağa gelenleri topla, sonra bir üst basamağa %10’unu aktar.',sekil=S24)

# ===== 25 · zor · grafik (çubuk) · rekabet · öncüllü =====
RK=[('K kabı','Yalnız A',[('A',100)]),('L kabı','Yalnız B',[('B',90)]),('M kabı','A ve B',[('A',0),('B',70)])]
assert RK[2][2][0][1]==0 and RK[1][2][0][1]>RK[2][2][1][1] and RK[0][2][0][1]==100
b=[f'\\draw[thick,{ARR}] (0,0)--(9.0,0);\\draw[thick,{ARR}] (0,0)--(0,4.0);']
for v in (0,50,100): b.append(f'\\draw (0,{v*.034:.2f})--(-.1,{v*.034:.2f}) node[left] {{{v}}};\\draw[gray!35] (0,{v*.034:.2f})--(8.7,{v*.034:.2f});')
x=.7
for kap,alt_,bars in RK:
    x0=x
    for tur,v in bars:
        b.append(f'\\draw[line width=.9pt,fill={"white" if tur=="A" else "gray!45"}] ({x:.2f},0) rectangle ({x+.8:.2f},{v*.034:.2f});\\node[above] at ({x+.4:.2f},{v*.034:.2f}) {{{v}}};\\node[below] at ({x+.4:.2f},-.05) {{{tur}}};')
        x+=.8
    b.append(f'\\node[below,align=center] at ({(x0+x)/2:.2f},-.7) {{{kap}\\\\{alt_}}};'); x+=1.3
b.append('\\node[anchor=south] at (1.4,4.1) {16. gündeki birey sayısı};')
S25=tk(''.join(b))
d={'I':('A türü, B türüyle birlikte yetiştirildiğinde 16. günde ortamda bulunmamaktadır; bu durum rekabetin sonucudur.',True,'M kabında A türü sıfırlanmıştır; iki tür aynı sınırlı besini kullandığı için aralarında rekabet vardır'),
   'II':('B türünün tek başına yetiştirildiği kapta ulaştığı birey sayısı, A türüyle birlikte yetiştirildiği kaptakinden azdır.',False,'B türü L kabında 90, M kabında 70 bireydir; tek başına yetiştirilince sayı daha yüksektir'),
   'III':('K kabında A türünün yaşamını sürdürmesi, M kabında A türünün kaybolmasında B türünün etkili olduğunu gösterir.',True,'A türü tek başına yaşayabilmektedir; M kabında farklı olan yalnız B türünün varlığıdır')}
r=onc(d,'E')
q('0025','iliski','zor','grafik','Rekabet deneyi','Rekabet deneyi sonuçlarını kontrol kabıyla karşılaştırarak yorumlar.','rekabet grafiği, öncüllü',
 'Aynı kaynağı kullanan türlerden biri elenebilir; tek başına yetiştirme kontrol işlevi görür.','Birlikte yetiştirmedeki düşüşü kontrolsüz yorumlamak.',
 oad(d),metin='A ve B adlı tek hücreli iki tür, sınırlı miktarda bulunan aynı besini kullanmaktadır. Bu türler aynı koşullarda üç kapta yetiştirilmiştir: K kabında yalnız A, L kabında yalnız B, M kabında A ve B birlikte. 16. gün sonunda her kaptaki birey sayısı grafikte verilmiştir.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Birlikte yetiştirilen kabı, tek başına yetiştirilenlerle karşılaştır.'],
 bilgi=[B('Rekabet','Aynı sınırlı kaynağı kullanan canlılar arasındaki ilişkidir; sonuçta bir tür azalabilir ya da elenebilir')],puf='Kontrol grubu olarak tek başına yetiştirilen kapları kullan.',sekil=S25)

# ===== 26 · orta · öncüllü · çevre sorunları =====
d={'I':('Kloroflorokarbon (CFC) içeren maddelerin kullanımının artması, ozon tabakasındaki incelmeyi hızlandırır ve canlılara ulaşan mor ötesi ışınları artırır.',True,'CFC ozonu parçalar; incelen tabaka mor ötesi ışınları daha az süzer'),
   'II':('Ormanların yok edilmesi, atmosferdeki karbondioksit miktarını azaltarak sera etkisini zayıflatır.',False,'ağaçlar fotosentezle CO2 kullanır; ormanlar azalınca CO2 daha az uzaklaştırılır ve sera etkisi güçlenebilir'),
   'III':('Eğimli arazide bitki örtüsünün yok edilmesi, toprağın su ve rüzgârla taşınmasını azaltır.',False,'bitki örtüsü kökleriyle toprağı tutar; yok edilince toprak taşınması (erozyon) artar')}
r=onc(d,'A')
q('0026','cevre','kolay','öncüllü','Çevre sorunlarının neden ve sonuçları','Çevre sorunlarının neden–sonuç ilişkilerini doğru kurar.','neden–sonuç, öncüllü',
 'Her çevre sorununun nedeni ve etkisi birbirine karıştırılmadan değerlendirilir.','Bitki örtüsünün yok edilmesinin sera etkisini azalttığını ya da erozyonu azalttığını sanmak.',
 oad(d),metin='İnsan etkinlikleri ozon incelmesi, küresel ısınma ve erozyon gibi çevre sorunlarına yol açmaktadır. Bu sorunların neden ve sonuçlarıyla ilgili aşağıdaki yargılar öne sürülmüştür.\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her yargıda neden ile sonucun yönünü ayrı ayrı sına.'],
 bilgi=[B('Çevre sorunları','Her çevre sorununun kendine özgü nedenleri ve canlılar üzerinde sonuçları vardır')],puf='Neden–sonuç yargılarında önce nedenin etkisinin yönünü bul.')

# ===== 27 · zor · tablo · sürdürülebilirlik =====
T27=[('X',8000,7200,20,55),('Y',5000,5500,35,40),('Z',6000,4500,10,12)]
pct=lambda a,b:Fr(b-a,a)*100
assert pct(8000,7200)==-10 and pct(5000,5500)==10 and pct(6000,4500)==-25 and Fr(25)/10==Fr(5,2)
assert max(T27,key=lambda r:r[4]-r[3])[0]=='X' and 8000-7200<6000-4500
S27=tablo_svg(['Ülke','Orman 2000','Orman 2020','Geri dön. 2000','Geri dön. 2020'],[[a,str(b),str(c),str(dd),str(e)] for a,b,c,dd,e in T27])
it=[('Y ülkesinde orman alanı %5 artmıştır.',False,'Y’de orman alanı 5000’den 5500’e çıkmıştır; 500 ÷ 5000 = %10 artış'),
    ('Z ülkesinde orman alanındaki azalma oranı, X ülkesindekinin 2,5 katıdır.',True,'Z’de azalma 1500 ÷ 6000 = %25, X’te 800 ÷ 8000 = %10’dur; 25 ÷ 10 = 2,5'),
    ('Geri dönüşüm oranı en çok artan ülke Y ülkesidir.',False,'artış puanları X’te 35, Y’de 5, Z’de 2’dir; en çok artan X’tir'),
    ('X ülkesinde hem orman alanı hem geri dönüşüm oranı artmıştır.',False,'X’te orman alanı 8000’den 7200’e azalmıştır'),
    ('Z ülkesindeki orman alanı kaybı, X ülkesindekinden azdır.',False,'Z’de 1500, X’te 800 birimlik kayıp vardır')]
r,g=tek(it,True,'B')
q('0027','surdur','zor','tablo','Doğal kaynakların sürdürülebilirliği','Doğal kaynak kullanımına ilişkin tablo verilerini oranlayarak yorumlar.','tablo, orman ve geri dönüşüm',
 'Değişim oranları verilerden hesaplanıp karşılaştırılır.','Mutlak azalma ile oransal azalmayı karıştırmak.',
 [A('Orman değişimlerini bul','Her ülkede 2020 ile 2000 arasındaki farkı hesapla.','X: −800 · Y: +500 · Z: −1500'),A('Oranlara çevir','Farkı 2000 yılındaki orman alanına böl.','X: %10 azalma · Y: %10 artış · Z: %25 azalma'),A('Geri dönüşümü karşılaştır','Puan artışlarını hesapla.','X: 35 · Y: 5 · Z: 2'),A('İfadeleri ele','Z’nin azalma oranı X’in 2,5 katıdır.','25 ÷ 10 = 2,5')],
 metin='Doğal kaynakların sürdürülebilir kullanımı, bu kaynakların gelecek kuşakların da gereksinimlerini karşılayabilecek biçimde kullanılması demektir. Üç ülkenin 2000 ve 2020 yıllarındaki orman alanları (bin hektar) ile atıkların geri dönüşüm oranları (%) tabloda verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Orman alanı değişimini ilk yıla oranlayarak karşılaştır.'],
 bilgi=[B('Sürdürülebilirlik','Kaynakları yenilenme hızını aşmayacak biçimde kullanmak, geri dönüşümü artırmak ve ormanları korumak sürdürülebilirliği sağlar')],puf='Farkı ilk değere bölerek oransal değişimi bul.',sekil=S27)

# ===== 28 · zor · düzenek · öncüllü =====
def kavanoz(x,bitki,balik):
    b=[f'\\draw[line width=1.2pt] ({x-.9},2.6)--({x-.9},.2) arc (180:270:.25) --({x+.65},-.05) arc (270:360:.25)--({x+.9},2.6);\\draw[line width=1.2pt,fill=black,fill opacity=.15] ({x-1.05},2.6) rectangle ({x+1.05},2.85);\\draw[vurgu,line width=.8pt] ({x-.9},2.1)--({x+.9},2.1);']
    if bitki:
        b.append(f'\\draw[line width=1.1pt] ({x-.5},.2)--({x-.5},1.5);'+''.join(f'\\draw[fill=black,fill opacity=.2] ({x-.5+dx},{y}) ellipse (.22 and .09);' for dx,y in ((.3,.7),(-.3,1.0),(.3,1.3))))
    if balik: b.append(f'\\draw[fill=white,line width=1pt] ({x+.35},.75) ellipse (.32 and .17);\\draw[line width=1pt] ({x+.62},.75)--({x+.85},.9)--({x+.85},.6)--cycle;\\fill ({x+.2},.8) circle (.03);')
    return ''.join(b)
b=[kavanoz(0,True,True),kavanoz(3.4,False,True),'\\node[font=\\small] at (-.15,1.78) {Bitki};\\node[font=\\small] at (.5,1.2) {Balık};\\node[font=\\small] at (3.4+.5,1.2) {Balık};','\\fill[gray!55] (5.55,-.35) rectangle (8.05,3.3);\\fill[white] (6.8,1.25) circle (0);',kavanoz(6.8,True,True),'\\node[font=\\small] at (6.65,1.78) {Bitki};\\node[font=\\small] at (7.3,1.2) {Balık};']
for xx in (0,3.4): b.append(f'\\draw[{ARR},line width=1pt] ({xx-.5},4.1)--({xx-.5},3.15);\\draw[{ARR},line width=1pt] ({xx+.5},4.1)--({xx+.5},3.15);\\node at ({xx},4.4) {{Işık}};')
b.append('\\node[font=\\small] at (6.8,3.6) {Işık girmeyen kutu};')
for i,xx in enumerate((0,3.4,6.8)): b.append(f'\\node[font=\\bfseries] at ({xx},-.7) {{{i+1}}};')
S28=tk(''.join(b))
d={'I':('2 numaralı kavanozdaki balığın ölümü, oksijenin solunumla tükenmesiyle açıklanabilir.',True,'kavanozda oksijen üretecek bitki yoktur; balığın solunumu oksijeni tüketir'),
   'II':('3 numaralı kavanozda bitki fotosentez yapamadığı için oksijen üretimi olmamıştır.',True,'ışıksız ortamda fotosentez gerçekleşmez'),
   'III':('3 numaralı kavanozda bitki solunum yapmadığından oksijen yalnız balık tarafından tüketilmiştir.',False,'bitkiler de hücrelerinde solunum yapar ve oksijen tüketir; ışıksız kutuda oksijeni bitki ile balık birlikte tüketir')}
r=onc(d,'D')
q('0028','dongu','zor','şekilli','Kapalı ortamda madde döngüsü','Kapalı bir sistemde fotosentez ve solunumun oksijen–karbondioksit dengesine etkisini yorumlar.','kapalı kavanoz düzeneği, öncüllü',
 'Bitki ışıkta fotosentezle O2 üretir; hem bitki hem hayvan solunumla O2 tüketir.','Bitkilerin solunum yapmadığını sanmak.',
 oad(d),metin='Aynı büyüklükte, ağzı hava geçirmeyecek biçimde kapatılmış üç kavanoz şekildeki gibi hazırlanmıştır. Kavanozlardaki su miktarı, besin ve sıcaklık koşulları aynıdır; 1 ve 3 numaralı kavanozlarda su bitkisi bulunmaktadır. Bir hafta sonra yalnız 1 numaralı kavanozdaki balığın yaşadığı görülmüştür.\nBuna göre,\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her kavanozda oksijeni kimin ürettiğini, kimin tükettiğini yaz.'],
 bilgi=[B('Fotosentez ve solunum','Fotosentez: ışık + CO2 + su → organik madde + O2 (yalnız ışıkta) · Solunum: organik madde + O2 → CO2 + su + enerji (bütün canlılarda, sürekli)')],puf='Bitki ışıkta hem fotosentez hem solunum yapar, karanlıkta yalnız solunum.',sekil=S28)

# ===== 29 · zor · grafik · biyoçeşitlilik · olumsuz =====
V29=[('A','Doğal\\\\orman',24,120,85),('B','Tek tür\\\\ağaçlandırma',9,40,12),('C','Tarım\\\\alanı',5,22,4)]
assert all(r_[3]>r_[2] for r_ in V29) and abs(85/12-7)<.2 and all(V29[0][i]>V29[1][i]>V29[2][i] for i in (2,3,4))
b=[f'\\draw[thick,{ARR}] (0,0)--(8.2,0);\\draw[thick,{ARR}] (0,0)--(0,4.7);']
for v in (0,60,120): b.append(f'\\draw (0,{v*.034:.2f})--(-.1,{v*.034:.2f}) node[left] {{{v}}};')
FIL=['white','gray!45','black!75']
for i,(k,ad_,*vv) in enumerate(V29):
    x0=.5+i*2.55; b.append(f'\\node[align=center,below] at ({x0+.9:.2f},-.05) {{{k}\\\\{ad_}}};')
    for j,v in enumerate(vv):
        xa=x0+j*.6; b.append(f'\\draw[line width=.9pt,fill={FIL[j]}] ({xa:.2f},0) rectangle ({xa+.6:.2f},{v*.034:.2f});\\node[above,font=\\footnotesize] at ({xa+.3:.2f},{v*.034:.2f}) {{{v}}};')
for j,tx in enumerate(('Kuş','Böcek','Bitki')): b.append(f'\\draw[line width=.9pt,fill={FIL[j]}] ({5.2+j*0:.2f},{4.55-j*.42:.2f}) rectangle ({5.5:.2f},{4.77-j*.42:.2f});\\node[anchor=west] at (5.6,{4.66-j*.42:.2f}) {{{tx}}};')
b.append('\\node[anchor=south] at (1.1,4.8) {Tür sayısı};')
S29=tk(''.join(b))
it=[('Tek tür ağaçlandırılan alan, doğal ormana benzer tür çeşitliliğine sahiptir.',False,'B alanında kuş, böcek ve bitki türü sayıları doğal ormanın çok altındadır'),
    ('Tür çeşitliliği en düşük olan alan tarım alanıdır.',True,'C alanında her üç grupta da en az tür vardır'),
    ('Doğal ormandaki bitki türü sayısı, tek tür ağaçlandırılan alandakinin yaklaşık 7 katıdır.',True,'85 ÷ 12 yaklaşık 7’dir'),
    ('Üç alanda da böcek türü sayısı kuş türü sayısından fazladır.',True,'120 > 24, 40 > 9 ve 22 > 5’tir'),
    ('Doğal ormanın tarım alanına dönüştürülmesi biyolojik çeşitliliğin azalmasına yol açabilir.',True,'A’dan C’ye geçildiğinde her üç grupta da tür sayısı belirgin biçimde azalır')]
r,g=tek(it,False,'A')
q('0029','surdur','zor','grafik','Biyolojik çeşitlilik','Biyolojik çeşitliliği alan kullanımına göre grafikten yorumlar.','tür sayısı grafiği, olumsuz kök',
 'Tür sayıları gruplar ve alanlar arasında karşılaştırılır.','Tek tür ağaçlandırmayı doğal ormanla eş saymak.',
 [A('Grafiği oku','Her alanda kuş, böcek ve bitki türü sayılarını yaz.','A: 24, 120, 85 · B: 9, 40, 12 · C: 5, 22, 4'),A('Alanları karşılaştır','Sayılar A’dan B’ye ve C’ye doğru azalır.','A > B > C'),A('Oranları hesapla','Bitkide 85 ÷ 12 yaklaşık 7 kat fark vardır; böcek sayısı kuştan fazladır.','≈ 7 kat'),A('Sonucu yaz','B alanının doğal ormana benzer çeşitlilikte olduğunu söyleyen ifade yanlıştır.','Yanlış: benzer çeşitlilik')],
 metin='Aynı bölgede bulunan üç alanda (A: doğal orman, B: tek tür ağaçlarla yapılan ağaçlandırma alanı, C: tarım alanı) yaşayan kuş, böcek ve bitki türü sayıları belirlenmiş ve sonuçlar grafikte gösterilmiştir. Üç alanın büyüklüğü eşittir.\nBu verilere göre aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Alanların verilerini grup grup karşılaştır.'],
 bilgi=[B('Biyolojik çeşitlilik','Bir bölgedeki tür, gen ve ekosistem çeşitliliğidir; yaşam alanlarının yok edilmesi ve tek tür kullanımı çeşitliliği azaltır')],puf='Önce sayıları oku, sonra yalnız verinin desteklediği ifadeyi seç.',sekil=S29)

# ===== 30 · orta · düz · biyoçeşitliliğin korunması =====
it=[('Türün tohumlarının gen bankasında saklanması',False,'tohum bankası, türü doğal yaşam alanının dışında korur'),
    ('Türün botanik bahçesinde yetiştirilerek çoğaltılması',False,'botanik bahçesi, türü doğal yaşam alanının dışında korur'),
    ('Türün doku kültürüyle laboratuvarda çoğaltılması',False,'laboratuvarda çoğaltma, türü doğal yaşam alanının dışında korur'),
    ('Türden alınan örneklerin serada yetiştirilmesi',False,'sera, doğal yaşam alanının dışında bir ortamdır'),
    ('Türün yaşadığı yamacın koruma altına alınması',True,'tür doğal yaşam alanında korunmaktadır')]
r,g=tek(it,True,'E')
q('0030','surdur','kolay','hikâyeli','Biyolojik çeşitliliğin korunması','Doğal ortamda ve doğal ortam dışında koruma yöntemlerini ayırt eder.','koruma yöntemleri',
 'Koruma, canlının doğal yaşam alanında ya da dışında yapılabilir.','Her koruma çalışmasını doğal ortamda koruma sanmak.',
 [A('Soruyu çöz','Doğal yaşam alanında koruma, türün yaşadığı ortamın korunmasıdır.','doğal alanda koruma'),A('Dışarıdaki yöntemleri ayır','Gen bankası, botanik bahçesi, doku kültürü ve sera türü doğal alanın dışında tutar.','4 şık: dışarıda'),A('Doğru şıkkı bul','Yaşam alanını koruma altına alan uygulama türü yerinde korur.','Koruma alanı ilanı'),A('Sonucu yaz','Yaşam alanının korunmasını içeren şık doğrudur.','Koruma alanı')],
 metin='Yalnızca bir dağ yamacında yaşayan nesli tehlike altındaki bir bitki türünün korunması için dört kurum farklı çalışmalar yürütmektedir. Çalışmaların bir kısmı türü doğal yaşam alanında, bir kısmı ise bu alanın dışında korumayı hedeflemektedir.\nBuna göre aşağıdakilerden hangisi türün doğal yaşam alanında korunmasına örnektir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğal ortamda koruma örneği.',ip=['Türün korunduğu yerin türün yaşadığı yer olup olmadığına bak.'],
 bilgi=[B('Biyolojik çeşitliliği koruma','Canlı türleri doğal yaşam alanında ya da bu alanın dışında korunabilir')],puf='Koruma yeri türün yaşam alanıysa doğal ortamda korumadır.')

assert len(P.ANA)==30,len(P.ANA)
bitir(P,'ekosistemiki',UK)
