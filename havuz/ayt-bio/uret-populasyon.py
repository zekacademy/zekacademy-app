"""AYT Biyoloji · Komünite ve Popülasyon Ekolojisi · 20 soru (kardeş yok, ipucu 1).
Şekil verileri, sayısal sonuçlar ve öncül doğrulukları Python'da hesaplanır; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,random,json
BD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(BD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Komünite ve Popülasyon Ekolojisi'; UK='abio|Komünite ve Popülasyon Ekolojisi'; H.KONU=KONU_
P=Parti('populasyon',KONU_,UK,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM 2018–2026 AYT Biyoloji (yalnız mantık) · MEB 12. sınıf Komünite ve Popülasyon Ekolojisi'
TIP={'buyume':'Popülasyon büyüme eğrileri','kapasite':'Taşıma kapasitesi ve sınırlayıcı etkenler','yapi':'Popülasyonun yapısı: yaş piramidi, dağılım, hayatta kalma',
     'iliski':'Türler arası ilişkiler','rekabet':'Rekabet ve ekolojik niş','sukses':'Süksesyon','komunite':'Komünite yapısı ve kilit taşı türler'}
USED=[]
def q(no,tp,z,kalip,alt,kaz,ne,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1 and no not in USED; USED.append(no)
    kart(f'K-ABPOP-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),'ab-pop-'+tp,TIP[tp],KY)
    mk(P,no,ad=ad,adim=len(ad),tipId='ab-pop-'+tp,tip=TIP[tp],z=z,kalip=kalip,alt=alt,kaz=kaz,kart=f'K-ABPOP-{no[-2:]} ({TIP[tp].lower()}) · {ne}',**k)
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS=[('I',),('II',),('III',),('I','II'),('I','III'),('II','III'),('I','II','III')]
def onc(d,harf,neg=False):
    T_=tuple(k for k in d if d[k][1]!=neg); i=SETS.index(T_); p='ABCDE'.index(harf)
    assert i-2<=p<=i,('harf uygun degil',T_,harf)
    ops=SETS[:i][:p]+[T_]+SETS[i+1:][:4-p]; assert len(ops)==5
    sira=[ORD[SETS.index(o)] for o in ops]; yan=[]
    for o in ops:
        if o==T_: continue
        pr=[]
        for x in sorted(set(o)-set(T_),key=lambda z:'I II III'.split().index(z)):
            pr.append(f'{x} öncülünü '+('doğru' if not neg else 'yanlış')+' sanmış; oysa '+('yanlıştır' if not neg else 'doğrudur')+f': {d[x][2]}')
        for x in sorted(set(T_)-set(o),key=lambda z:'I II III'.split().index(z)):
            pr.append(f'{x} öncülünü '+('yanlış' if not neg else 'doğru')+' sanmış; oysa '+('doğrudur' if not neg else 'yanlıştır')+f': {d[x][2]}')
        yan.append((ORD[SETS.index(o)],'. '.join(pr)+'.','bilgi'))
    return dict(dogru=ORD[i],yan=yan,sira=sira)
def omet(giris,d,kok): return giris+'\n'+'\n'.join(f'{x}. {d[x][0]}' for x in d)+'\n'+kok
def oad(d,neg=False,bas=None):
    a=list(bas or [])
    for x in d: a.append(A(f'{x}. öncülü incele',d[x][2][0].upper()+d[x][2][1:]+'.',('doğru' if d[x][1] else 'yanlış')))
    T_=[x for x in d if d[x][1]!=neg]
    a.append(A('Sonucu yaz','Köke uygun öncüller bir arada yazılır.',' ve '.join(T_) if len(T_)<3 else 'I, II ve III' if len(T_)==3 else T_[0]))
    return a
def tek(items,hedef,harf):
    h=[s for s in items if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    dg=h[0]; dig=[s for s in items if s[1]!=hedef]; assert len(dig)==4
    sira=dig[:]; sira.insert('ABCDE'.index(harf),dg)
    yan=[(m,(f'Bu ifadeyi doğru sanmış; oysa yanlıştır: {n}.' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}.'),'bilgi') for m,b,n in dig]
    return dict(dogru=dg[0],yan=yan,sira=[s[0] for s in sira]),dg[2]
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
import re as _re
def tk(g): return _re.sub(r'(\d{2,}\.\d)\d+',r'\1',_re.sub(r'(\d+\.\d{2})\d+',r'\1',tikz_svg(HEAD+g+TAIL)))
def eks(w,h,xl='',yl='',xo=-.0):
    s=f'\\draw[-{{Stealth[length=2.4mm]}},line width=1pt] (0,0)--({w+.35},0);\\draw[-{{Stealth[length=2.4mm]}},line width=1pt] (0,0)--(0,{h+.35});'
    if xl: s+=f'\\node[below] at ({w/2},-.05) {{{xl}}};'
    if yl: s+=f'\\node[rotate=90,above] at (-.1,{h/2}) {{{yl}}};'
    return s
def egr(pts,st='line width=1.6pt'):
    return f'\\draw[{st}] plot[smooth] coordinates {{'+' '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+'};'
def seri(f,a,b,n=40): return [(a+(b-a)*i/n,f(a+(b-a)*i/n)) for i in range(n+1)]
SADE=lambda s:s.replace('.','')

# ===== 01 · kolay · grafik · olumsuz · S tipi büyüme =====
def S(t): return 3.2/(1+math.exp(-0.9*(t-5)))
ta,tb=2.6,7.0
assert S(ta)<0.4*3.2*0.4 and S(tb)>0.8*3.2   # I: yavaş, III: platoya yakın
g=eks(6.4,3.7,'Zaman','Popülasyon büyüklüğü')
g+=egr([(0.6*t,S(t)) for t in [i*0.25 for i in range(0,41)]])
for tt in (ta,tb): g+=f'\\draw[dashed,line width=.6pt] ({0.6*tt:.2f},0)--({0.6*tt:.2f},3.55);'
g+=f'\\node at ({0.6*1.3:.2f},3.7) {{\\textbf{{I}}}};\\node at ({0.6*4.8:.2f},3.7) {{\\textbf{{II}}}};\\node at ({0.6*8.5:.2f},3.7) {{\\textbf{{III}}}};'
SEK01=tk(g)
it=[('I. evrede popülasyonun büyüme hızı, II. evredekinden düşüktür.',True,'I. evrede birey sayısı az olduğundan artış yavaştır; II. evrede eğrinin eğimi en büyüktür'),
 ('II. evrede doğum sayısı ölüm sayısından fazladır.',True,'II. evrede popülasyon büyüklüğü artmaktadır, bu da doğumların ölümlerden fazla olduğunu gösterir'),
 ('III. evrede popülasyon büyüklüğü, ortamın taşıma kapasitesi çevresinde dalgalanır.',True,'S tipi büyümede popülasyon, taşıma kapasitesine ulaşınca bu değer çevresinde dengelenir'),
 ('III. evrede doğum hızı ile ölüm hızı yaklaşık olarak eşittir.',True,'III. evrede eğri yataydır; net artış sıfıra yakın olduğundan doğum ve ölüm hızları dengelenmiştir'),
 ('II. evrede çevre direnci, popülasyonun biyotik potansiyelinden büyüktür.',False,'II. evrede popülasyon hızla büyüdüğünden biyotik potansiyel çevre direncinden büyüktür; ikisi ancak III. evrede dengelenir')]
r,gz=tek(it,False,'D')
q('0001','buyume','kolay','grafik','S tipi büyüme eğrisinin evreleri','S tipi büyüme eğrisinin evrelerinde doğum, ölüm, biyotik potansiyel ve çevre direncini ilişkilendirir.','S eğrisi evrelerini yorumlama',
 'S tipi büyümede biyotik potansiyel ile çevre direncinin göreli büyüklüğü evreden evreye değişir.','Çevre direncinin büyüme boyunca hep fazla olduğunu sanmak.',
 [A('Eğriyi evrelere ayır','I. evrede eğri çok az yükselir, II. evrede dik yükselir, III. evrede yataylaşır.','I: yavaş · II: hızlı · III: denge'),
  A('Evreleri yorumla','Eğim büyüdükçe net artış büyür; yatay bölümde net artış sıfırdır.','III: doğum ≈ ölüm'),
  A('Biyotik potansiyeli karşılaştır','Popülasyon büyürken biyotik potansiyel baskındır; denge evresinde çevre direnci ona eşitlenir.','II: biyotik potansiyel > çevre direnci'),
  A('Yanlış ifadeyi seç','Çevre direncinin II. evrede daha büyük olduğunu söyleyen ifade yanlıştır.','yanlış ifade belirlendi')],
 metin='Sınırlı kaynaklara sahip bir ortama bırakılan böcek popülasyonunun büyüklüğünün zamana göre değişimi şekilde verilmiştir. Eğri üzerindeki I, II ve III ile gösterilen bölümler, büyümenin birbirinden farklı evrelerini göstermektedir.\nBuna göre aşağıdakilerden hangisi yanlıştır?',
 sekil=SEK01,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Her evrede eğrinin eğimine ve doğum ile ölüm sayılarına bak.'],
 bilgi=[B('S tipi büyüme','Sınırlı kaynak olan ortamda popülasyon yavaş başlar, hızlanır ve taşıma kapasitesine yaklaşınca dengelenir'),B('Büyümeyi belirleyen etkenler','Biyotik potansiyel büyümeyi artırır; çevre direnci (besin, alan, hastalık, avcı) büyümeyi sınırlar')],
 puf='Eğim, net artışı gösterir; eğri yatay ise doğum ve ölüm hızları dengededir.')

# ===== 02 · kolay · tablo · sayısal · yoğunluk =====
satir={'K':(240,36,20,8,12,4),'L':(300,50,25,10,30,5),'M':(180,24,18,6,6,3)}
def yil_sonu(b,d,o,gi,gc): return b+d-o+gi-gc
b,d,o,gi,gc,alan=satir['L']
son=yil_sonu(b,d,o,gi,gc); assert son==305 and son/alan==61
yog=son/alan
yan02=[(73,'Göçle ayrılan 30 bireyi de çıkarmak yerine eklemiş; (300 + 50 − 25 + 10 + 30) = 365 birey bulup 5 km²ye bölmüştür.','islem'),
       (65,'Göçle gelen ve ayrılan bireyleri hesaba katmamış; (300 + 50 − 25) = 325 birey bulup 5 km²ye bölmüştür.','dikkat'),
       (70,'Yalnız doğumları eklemiş; ölümleri ve göçleri hesaba katmadan (300 + 50) = 350 birey bulup 5 km²ye bölmüştür.','dikkat'),
       (305,'Yıl sonundaki birey sayısını bulmuş, ancak alana bölerek yoğunluğa çevirmemiştir.','dikkat')]
assert (300+50-25+10+30)/5==73 and (300+50-25)/5==65 and (300+50)/5==70 and 300+50-25+10-30==305
SEK02=tablo_svg(['Popülasyon','Yıl başı','Doğum','Ölüm','Göçle giren','Göçle çıkan','Alan (km²)'],[[k]+list(map(str,v)) for k,v in satir.items()])
q('0002','kapasite','kolay','tablo','Popülasyon büyüklüğü ve yoğunluğu','Doğum, ölüm ve göç verilerinden popülasyon büyüklüğünü ve yoğunluğunu hesaplar.','yıl sonu yoğunluk hesabı',
 'Popülasyon büyüklüğü doğum ve göçle gelenlerle artar, ölüm ve göçle ayrılanlarla azalır; yoğunluk birey sayısının alana oranıdır.','Göçleri yok saymak ya da göçle ayrılanları sayıya eklemek.',
 [A('Değişim kalemlerini ayır','Doğum ve göçle gelen bireyler sayıyı artırır; ölüm ve göçle ayrılan bireyler azaltır.','artıran: doğum + gelen · azaltan: ölüm + ayrılan'),
  A('L için yıl sonu sayısını bul','Yıl başı sayıya artıranlar eklenir, azaltanlar çıkarılır.','300 + 50 + 10 − 25 − 30 = 305'),
  A('Yoğunluğu hesapla','Yoğunluk, birey sayısı bölü alandır.','305 ÷ 5 = 61 birey/km²')],
 metin='Aynı bölgedeki üç farklı geyik popülasyonuna ait bir yıllık veriler tabloda verilmiştir. Tablodaki sayılar birey sayısıdır; yıl içinde doğum, ölüm ve göç dışında başka bir değişim olmamıştır.\nBuna göre L popülasyonunun yıl sonundaki yoğunluğu kaç birey/km² olur?',
 sekil=SEK02,dogru=61,yan=yan02,istenen='L popülasyonunun yıl sonu yoğunluğu (birey/km²).',ip=['Önce yıl sonundaki birey sayısını bul, sonra alana böl.'],
 bilgi=[B('Popülasyon büyüklüğü','Popülasyon büyüklüğü = başlangıç + doğum + göçle gelen − ölüm − göçle ayrılan'),B('Popülasyon yoğunluğu','Birim alandaki birey sayısıdır: yoğunluk = birey sayısı ÷ alan')],
 puf='Önce bireyleri say (artıran − azaltan), sonra alana böl.')

# ===== 03 · kolay · şekil · dağılım =====
rng=random.Random(11)
def kume():
    c=[(.55,.6),(1.55,1.45),(.65,1.62)]; n=[6,5,5]; pts=[]
    for (cx,cy),k in zip(c,n):
        for _ in range(k): pts.append((min(2.0,max(.2,rng.gauss(cx,.14))),min(2.0,max(.2,rng.gauss(cy,.14)))))
    return pts
def duzen(): return [(.28+.55*i+rng.uniform(-.04,.04),.28+.55*j+rng.uniform(-.04,.04)) for i in range(4) for j in range(4)]
def rast():
    while True:
        pts=[(rng.uniform(.15,2.05),rng.uniform(.15,2.05)) for _ in range(16)]
        d=[min(math.dist(a,b) for b in pts if b is not a) for a in pts]
        if min(d)>.2 and max(d)<.75 and sorted(d)[8]<.5 and sorted(d)[8]>.3: return pts
DAG={'K':kume(),'L':duzen(),'M':rast()}
assert all(len(v)==16 for v in DAG.values())
g=''
for i,(ad_,pts) in enumerate(DAG.items()):
    x0=i*3.0
    g+=f'\\draw[line width=1pt] ({x0},0) rectangle ({x0+2.2},2.2);'
    for x,y in pts: g+=f'\\fill ({x0+x:.2f},{y:.2f}) circle (.075);'
    g+=f'\\node at ({x0+1.1},-.4) {{\\textbf{{{ad_}}}}};'
SEK03=tk(g)
gercek={'I':'L','II':'K','III':'M'}   # I düzenli, II kümeli, III rastgele
tur_ad={'L':'düzenli','K':'kümeli','M':'rastgele'}
perms=[('K','L','M'),('L','K','M'),('L','M','K'),('M','K','L'),('K','M','L')]
def pad(p): return f'I: {p[0]}, II: {p[1]}, III: {p[2]}'
dog=('L','K','M'); yan03=[]
for p in perms:
    if p==dog: continue
    pr=[f'{rom} durumunu {x} popülasyonuyla eşlemiş; oysa o durum {gercek[rom]} popülasyonundaki ({tur_ad[gercek[rom]]}) dağılımdır' for rom,x in zip(('I','II','III'),p) if x!=gercek[rom]]
    yan03.append((pad(p),'. '.join(pr)+'.','bilgi'))
sira03=[pad(p) for p in [('K','M','L'),('M','K','L'),('K','L','M'),('L','K','M'),('L','M','K')]]; assert 'ABCDE'[sira03.index(pad(dog))]=='D'
q('0003','yapi','kolay','şekilli','Popülasyonların yayılış biçimleri','Kümeli, düzenli ve rastgele yayılış biçimlerini örneklerle eşleştirir.','yayılış biçimi eşleştirme',
 'Bireylerin birbirine uzaklığı yayılış biçimini belirler: gruplar kümeli, eşit aralıklar düzenli, belirli bir kural yoksa rastgele.','Kaynak için rekabeti kümeli dağılımla ilişkilendirmek.',
 [A('Şekillerdeki dağılımı tanı','K’de bireyler gruplar halinde, L’de eşit aralıklarla, M’de belirli bir kurala uymadan dağılmıştır.','K: kümeli · L: düzenli · M: rastgele'),
  A('Örnekleri yorumla','Suyu paylaşmayan çalılar eşit aralıklı, nemli kütükte biriken mantarlar gruplu, rüzgârla savrulan tohumlar kuralsız yerleşir.','I: düzenli · II: kümeli · III: rastgele'),
  A('Eşleştirmeyi yap','Her durum, benzeyen dağılımı gösteren şekille eşleştirilir.','I: L, II: K, III: M')],
 metin='Şekilde, aynı büyüklükteki üç alanda yaşayan K, L ve M popülasyonlarına ait bireylerin (●) alandaki yayılışları gösterilmiştir. Aşağıda üç farklı canlı popülasyonunun yayılışı tanımlanmıştır.\nI. Çölde, köklerinin su alanı birbirini kapsamayacak biçimde yerleşen çalı bireyleri\nII. Ormanda, yalnızca nemli ve çürümekte olan kütüklerin üzerinde birikerek yaşayan mantar bireyleri\nIII. Rüzgârla savrulup gelişigüzel düşen tohumlardan oluşan ve kendine özgü bir yerleşim kuralı bulunmayan ot bireyleri\nBu popülasyonlar şekildeki popülasyonlarla eşleştirildiğinde sonuç aşağıdakilerden hangisi olur?',
 sekil=SEK03,dogru=pad(dog),yan=yan03,sira=sira03,istenen='Durumlara uyan popülasyonlar.',ip=['Bireyler arası uzaklıkların düzenli mi, gruplu mu, kuralsız mı olduğuna bak.'],
 bilgi=[B('Yayılış biçimleri','Kümeli: bireyler gruplar halinde · Düzenli: bireyler arası uzaklık hemen hemen eşit · Rastgele: bireylerin yeri birbirinden bağımsız')],
 puf='Bireyler arası uzaklıklar eşitse düzenli, gruplar varsa kümeli, ikisi de yoksa rastgele dağılımdır.')

# ===== 04 · orta · yaş piramidi · öncüllü =====
def piramit(x0,vals,ad_,sc=0.034,sayi=False,etiket=False):
    s=''
    for i,v in enumerate(vals):
        hw=v*sc; y0=i*.85
        s+=f'\\draw[fill=black,fill opacity=.18,line width=1pt] ({x0-hw:.2f},{y0}) rectangle ({x0+hw:.2f},{y0+.75});'
        if sayi: s+=f'\\node at ({x0},{y0+.375}) {{\\%{v}}};'
    s+=f'\\node at ({x0},-.45) {{\\textbf{{{ad_}}}}};'
    if etiket:
        for i,n in enumerate(['Üreme öncesi','Üreme çağı','Üreme sonrası']): s+=f'\\node[left] at ({x0-1.65:.2f},{i*.85+.375}) {{{n}}};'
    return s
PIR={'K':(50,35,15),'L':(33,34,33),'M':(18,32,50)}
assert all(sum(v)==100 for v in PIR.values())
g=''
for i,(a_,v) in enumerate(PIR.items()): g+=piramit(3.0+i*3.2,v,a_,sc=.028,etiket=(i==0))
SEK04=tk(g)
d={'I':('K popülasyonunda üreme öncesi grubun geniş olması, göç olmadığı koşullarda popülasyonun ilerleyen yıllarda büyümesinin beklendiğini gösterir.',True,'geniş tabanlı piramitte üreme çağına girecek birey sayısı fazladır, bu nedenle popülasyonun büyümesi beklenir'),
   'II':('L popülasyonunda doğum sayısı, ölüm sayısından her zaman fazladır.',False,'üç yaş grubunun yaklaşık eşit olduğu piramit durağan popülasyonu gösterir; durağan popülasyonda doğum ve ölüm sayıları yaklaşık eşittir'),
   'III':('M popülasyonunda üreme sonrası grubun geniş olması, göç olmadığı koşullarda popülasyonun küçülmeye yöneldiğini gösterir.',True,'üreme öncesi grubun dar olması, üreme çağına girecek birey sayısının azalacağını gösterir ve popülasyon küçülür')}
r=onc(d,'C')
q('0004','yapi','orta','öncüllü','Yaş piramitleri','Yaş piramidinin biçiminden popülasyonun büyüme eğilimini yorumlar.','piramit yorumlama',
 'Yaş piramidinde üreme öncesi grubun genişliği popülasyonun geleceğini belirler.','Geniş piramit tabanını geniş üreme sonrası grubuyla karıştırmak.',
 oad(d,bas=[A('Piramitleri incele','K’de taban geniş, L’de üç grup yaklaşık eşit, M’de taban dardır.','K: geniş taban · L: dikdörtgen · M: dar taban')]),
 metin=omet('Şekilde, göçün olmadığı üç farklı popülasyona ait yaş piramitleri verilmiştir. Piramitlerde her basamağın genişliği, ilgili yaş grubundaki bireylerin popülasyondaki oranını göstermektedir.\nBuna göre,',d,'yargılarından hangileri doğrudur?'),
 sekil=SEK04,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Üreme öncesi grubun diğer gruplara göre genişliğine bak.'],
 bilgi=[B('Yaş grupları','Üreme öncesi, üreme çağı ve üreme sonrası gruplarının oranları popülasyonun gelecekteki büyüklüğünü belirler'),B('Piramit biçimleri','Geniş tabanlı: büyüyen · dikdörtgene yakın: durağan · dar tabanlı: küçülen popülasyon')],
 puf='Tabana bak: geniş taban büyüme, dar taban küçülme, eşit gruplar durağanlık demektir.')

# ===== 05 · orta · hayatta kalma · öncüllü =====
def tipI(x): return 1000*(1-x**6)
def tipII(x): return 1000*10**(-2.6*x)
def tipIII(x): return 1000*10**(-2.6*x**0.28)
def ly(n): return 1.1*math.log10(n)
g=eks(5.6,3.6,'','')+'\\node[rotate=90,above] at (-.75,1.8) {Hayatta kalan birey sayısı};\\node[below] at (2.8,-.7) {Yaş};'
for n in (1,10,100,1000): g+=f'\\draw (0,{ly(n):.2f})--(-.1,{ly(n):.2f});\\node[left] at (-.1,{ly(n):.2f}) {{{n}}};'
for n,x in zip(['Genç','Ergin','Yaşlı'],[.7,2.8,4.9]): g+=f'\\node[below] at ({x},-.0) {{{n}}};'
cur={'K':tipII,'L':tipIII,'M':tipI}
for ad_,f in cur.items():
    xs=[i/60*0.99 for i in range(61)]
    g+=egr([(5.3*x,ly(max(f(x),1))) for x in xs])
g+=f'\\node[above right] at ({5.3*.62:.2f},{ly(tipII(.62)):.2f}) {{\\textbf{{K}}}};\\node[above right] at ({5.3*.17:.2f},{ly(tipIII(.17)):.2f}) {{\\textbf{{L}}}};\\node[above right] at ({5.3*.55:.2f},{ly(tipI(.55))+.05:.2f}) {{\\textbf{{M}}}};'
SEK05=tk(g)
# doğrulama: K logaritmik ölçekte doğrusal (sabit ölüm oranı), L'de erken kayıp, M'de geç kayıp
sl=lambda f,a,b:(math.log10(f(b))-math.log10(f(a)))/(b-a)
assert abs(sl(tipII,.1,.4)-sl(tipII,.6,.9))<1e-9
assert tipIII(.2)<0.1*tipIII(0) and tipI(.5)>0.95*tipI(0)*0.9 and tipI(.95)<tipI(.5)*.5
d={'I':('K popülasyonunda her yaş döneminde ölen bireylerin oranı hemen hemen aynıdır.',True,'logaritmik ölçekte doğrusal inen eğri, her dönemde bireylerin aynı oranının öldüğünü gösterir'),
   'II':('L popülasyonunda doğan bireylerin büyük bölümü ergin döneme ulaşamadan ölür.',True,'L eğrisi genç dönemde çok dik indiğinden ölümler büyük oranda erken yaşlarda olur'),
   'III':('M popülasyonunda ölümler en çok genç dönemde gerçekleşir.',False,'M eğrisi genç dönemde neredeyse yataydır; bireylerin çoğu ileri yaşlara ulaşır, ölümler ağırlıklı olarak yaşlı dönemde görülür')}
r=onc(d,'B')
q('0005','yapi','orta','öncüllü','Hayatta kalma eğrileri','Hayatta kalma eğrilerinden yaş gruplarına göre ölüm oranını yorumlar.','hayatta kalma eğrisi',
 'Logaritmik ölçekte eğrinin eğimi, o yaş döneminde ölen bireylerin oranını gösterir.','Doğrusal inen eğriyi (logaritmik ölçekte) sabit ölüm sayısı sanmak.',
 oad(d,bas=[A('Eğrilerin biçimine bak','K logaritmik ölçekte doğrusal iner, L başta çok dik iner, M başta yataydır ve sonda diker.','K: doğrusal · L: erken dik · M: geç dik')]),
 metin=omet('Hayatta kalma eğrileri, bir popülasyonda doğan bireylerin yaşa göre kaçının hayatta kaldığını gösterir. Şekilde, K, L ve M popülasyonlarına ait hayatta kalma eğrileri verilmiştir. Hayatta kalan birey sayısı logaritmik ölçekte gösterilmiştir.\nBuna göre,',d,'yargılarından hangileri doğrudur?'),
 sekil=SEK05,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Eğrinin hangi yaş döneminde dik indiğine bak.'],
 bilgi=[B('Hayatta kalma eğrisi','Her yaşta hayatta kalan birey sayısının grafiğidir; dik inen bölüm o dönemde ölümlerin fazla olduğunu gösterir'),B('Eğri türleri','Geç dönemde ölümlerin çok olduğu, her dönemde oranın sabit olduğu ve erken dönemde ölümlerin çok olduğu üç temel biçim vardır')],
 puf='Eğri nerede dik iniyorsa ölümler o yaş döneminde yoğundur.')

# ===== 06 · orta · tablo · lojistik büyüme · sayısal =====
NT=[20,60,160,340,560,750,880,950,980]; KK=1000
art=[NT[i+1]-NT[i] for i in range(len(NT)-1)]; assert art.index(max(art))==3 and max(art)==220
oran=[art[i]/NT[i] for i in range(len(art))]; assert oran.index(max(oran))==0
assert art[2]==180 and art[4]==190 and NT[3]<KK/2<NT[4]
SEK06=tablo_svg(['Yıl']+[str(i) for i in range(9)],[['Birey sayısı']+[str(x) for x in NT]])
ar=lambda i:f'{i}–{i+1}. yıllar arası'
sira06=[ar(0),ar(2),ar(3),ar(4),ar(7)]
q('0006','buyume','orta','tablo','Logaritmik büyüme ve en yüksek artış','S tipi büyüme verisinden net artışın en yüksek olduğu aralığı belirler.','net artış karşılaştırması',
 'S tipi büyümede net artış, popülasyon büyüklüğü taşıma kapasitesinin yarısına yakınken en yüksektir.','Birey başına artış oranı ile toplam net artışı karıştırmak.',
 [A('Her aralıktaki net artışı bul','Ardışık yıllardaki birey sayıları farkı alınır.','40, 100, 180, 220, 190, 130, 70, 30'),
  A('En büyük artışı seç','Yıllık net artış 3–4. yıllar arasında 220 ile en büyüktür.','560 − 340 = 220'),
  A('Taşıma kapasitesiyle karşılaştır','Bu aralık, K/2 = 500 değerini içerir; S tipi büyümede en hızlı artış beklenen yerdir.','340 < 500 < 560')],
 metin='Taşıma kapasitesi 1000 birey olan bir adada yaşayan bir kuş popülasyonunun 0’dan 8. yıla kadar her yıl başında sayılan birey sayıları tabloda verilmiştir.\nBuna göre popülasyonun yıllık net artışı (birey/yıl) hangi zaman aralığında en fazladır?',
 sekil=SEK06,dogru=ar(3),yan=[(ar(0),'Birey başına artış oranına bakmış; ilk aralıkta oran 2’dir, ancak toplam artış yalnız 40 bireydir.','dikkat'),
   (ar(2),'Birey sayısı K/2 = 500’e ulaşmadan hızın en yüksek olduğunu sanmış; bu aralıkta artış 340 − 160 = 180’dir.','bilgi'),
   (ar(4),'Artışın K/2’yi geçtikten sonra da arttığını sanmış; bu aralıkta artış 750 − 560 = 190’dır.','bilgi'),
   (ar(7),'Birey sayısı en fazla olan aralığı seçmiş; oysa bu aralıkta artış 980 − 950 = 30’dur ve çevre direnci büyüktür.','bilgi')],
 sira=sira06,istenen='Net artışın en fazla olduğu aralık.',ip=['Ardışık yılların birey sayıları arasındaki farklara bak.'],
 bilgi=[B('Net artış','Net artış, iki ölçüm arasındaki birey sayısı farkıdır'),B('Taşıma kapasitesi','Bir ortamın uzun süre besleyebileceği en fazla birey sayısıdır; S tipi büyümede popülasyon bu değere yaklaşınca artış yavaşlar')],
 puf='S eğrisinde en dik bölüm, taşıma kapasitesinin yarısı civarındadır.')

# ===== 07 · orta · rekabet deneyi · olumsuz =====
def lj(K_,a,r_): return lambda t:K_/(1+a*math.exp(-r_*t))
xa=lj(120,11,.35); ya=lj(160,15,.35); yb=lj(140,15,.30)
xb_pts=[(0,10),(4,32),(8,50),(12,38),(16,18),(20,5),(24,0)]
assert yb(24)>130 and ya(24)>150 and xa(24)>115 and max(p[1] for p in xb_pts)<xa(24)
def panel(x0,title,curves,etk=None):
    s=f'\\draw[-{{Stealth[length=2mm]}},line width=.9pt] ({x0},0)--({x0+2.9},0);\\draw[-{{Stealth[length=2mm]}},line width=.9pt] ({x0},0)--({x0},2.35);'
    for v in (0,50,100,150):
        yy=v*2.0/175; s+=f'\\draw ({x0},{yy:.2f})--({x0-.08},{yy:.2f});\\node[left] at ({x0-.08},{yy:.2f}) {{\\footnotesize {v}}};'
    for gun in (0,24): s+=f'\\draw ({x0+gun/24*2.6:.2f},0)--({x0+gun/24*2.6:.2f},-.08);\\node[below] at ({x0+gun/24*2.6:.2f},-.05) {{\\footnotesize {gun}}};'
    s+=f'\\node[above] at ({x0+1.4},2.35) {{\\small {title}}};\\node[below] at ({x0+1.4},-.4) {{\\footnotesize Gün}};'
    for pts,st in curves: s+=egr([(x0+t/24*2.6,v*2.0/175) for t,v in pts],st)
    return s
g=panel(0,'X tek başına',[(seri(xa,0,24,14),'line width=1.5pt')])
g+=panel(3.7,'Y tek başına',[(seri(ya,0,24,14),'line width=1.5pt,dashed')])
g+=panel(7.4,'X ve Y birlikte',[(xb_pts,'line width=1.5pt'),(seri(yb,0,24,14),'line width=1.5pt,dashed')])
g+='\\node[rotate=90,above] at (-.85,1.1) {\\small Popülasyon yoğunluğu};'
g+=f'\\draw[line width=1.5pt] (4.0,3.25)--(4.6,3.25);\\node[right] at (4.6,3.25) {{X türü}};\\draw[line width=1.5pt,dashed] (6.2,3.25)--(6.8,3.25);\\node[right] at (6.8,3.25) {{Y türü}};'
SEK07=tk(g)
it=[('Y türü, X türüyle birlikte yetiştirildiğinde tek başına yetiştirildiğine göre daha düşük popülasyon yoğunluğuna ulaşmıştır.',True,'Y tek başına yaklaşık 160, birlikte yaklaşık 140 yoğunluğa ulaşmıştır'),
 ('Birlikte yetiştirme koşulunda X türünün ortamdan çekilmesi rekabetten dışlama ile açıklanabilir.',True,'aynı kaynakları kullanan iki türden biri, rekabette üstün olan tür karşısında ortamdan dışlanabilir'),
 ('Deneyde Y türü, X türünü avlayarak ortamdan uzaklaştırmıştır.',False,'deneyde türlerin birbirini avladığına dair bir veri yoktur; X türü rekabette üstün olan Y türü karşısında ortamdan çekilmiştir'),
 ('Her iki tür de tek başına yetiştirildiğinde kültür ortamının kaynakları sınırlayıcı olmuştur.',True,'iki türün de eğrisi bir üst değerde dengelenmiştir; bu, sınırlı kaynakların büyümeyi sınırladığını gösterir'),
 ('X türü, Y türüyle birlikte yetiştirildiğinde popülasyon yoğunluğu önce artmış, sonra azalarak sıfıra yaklaşmıştır.',True,'birlikte yetiştirme grafiğinde X eğrisi yaklaşık 8. günde tepe yapıp sonra sıfıra inmektedir')]
r,gz=tek(it,False,'A')
q('0007','rekabet','orta','grafik','Rekabetten dışlama deneyi','Ayrı ve birlikte yetiştirme deneyinden türler arası rekabeti yorumlar.','rekabet deneyi yorumlama',
 'Aynı kaynakları kullanan iki tür birlikte yetişince birinin yoğunluğu azalıyor ya da sıfırlanıyorsa ilişki rekabettir.','Rekabette üstünlüğü avlanma sanmak.',
 [A('Ayrı yetiştirmeyi oku','X tek başına yaklaşık 120, Y tek başına yaklaşık 160 yoğunlukta dengelenir.','X: ≈120 · Y: ≈160'),
  A('Birlikte yetiştirmeyi oku','Birlikte yetişince X önce artar, sonra sıfıra iner; Y ise tek başına olduğundan daha düşük bir değerde dengelenir.','X → 0 · Y: ≈140'),
  A('İlişkiyi yorumla','İki türün de yoğunluğu birlikteyken olumsuz etkilenmiştir; bu rekabettir. Avlanmaya ilişkin bir veri yoktur.','ilişki: rekabet'),
  A('Yanlış ifadeyi seç','Avlanma ile ilgili ifade verilerle çelişir.','yanlış ifade belirlendi')],
 metin='Aynı tip besinle beslenen X ve Y türleri, önce ayrı ayrı, sonra aynı kültür ortamında birlikte yetiştirilmiştir. Üç ayrı deneyde, ortama yeterli ancak sınırlı miktarda besin konmuştur ve popülasyon yoğunluklarının günlere göre değişimi şekilde gösterilmiştir.\nBu deney ve sonuçlarına göre aşağıdakilerden hangisi yanlıştır?',
 sekil=SEK07,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Birlikte yetiştirme grafiğinde iki türün yoğunluğunun nasıl değiştiğine bak.'],
 bilgi=[B('Rekabet','Aynı sınırlı kaynağı kullanan canlılar arasındaki ilişkidir; en az birinin yoğunluğunu azaltır'),B('Rekabetten dışlama','Benzer niş gereksinimi olan iki türden biri, rekabette üstün olan tür karşısında ortamdan çekilebilir')],
 puf='Birlikte yetişen türlerden birinin yoğunluğu sıfırlanıyorsa ve avlanma yoksa ilişki rekabettir.')

# ===== 08 · orta · öncüllü · simbiyotik ilişkiler =====
d={'I':('Termitlerin sindirim kanalında yaşayan ve selülozu sindiren flagellat protistler ile termit arasındaki ilişki kommensalizmdir.',False,'protistler barınak ve besin bulur, termit ise selülozu sindirebilmekten yararlanır; her iki tür de yarar sağladığı için bu ilişki mutualizmdir'),
   'II':('Ağaç gövdesine tutunarak ışığa daha yakın yaşayan epifit orkide ile ağaç arasındaki ilişki kommensalizmdir.',True,'orkide ışıktan yararlanırken ağaç bu durumdan belirgin biçimde etkilenmez; bu ilişki kommensalizmdir'),
   'III':('Penisilin salgılayarak çevresindeki bakterilerin gelişmesini engelleyen küf mantarı ile bakteriler arasındaki ilişki amensalizmdir.',True,'bakteriler zarar görür, küf ise bundan etkilenmez; bu ilişki amensalizmdir')}
r=onc(d,'D')
q('0008','iliski','orta','öncüllü','Simbiyotik ilişkiler','Mutualizm, kommensalizm ve amensalizm örneklerini ayırt eder.','ilişki türü eşleştirme',
 'İlişki türü, tarafların yarar, zarar ya da etkilenmeme durumlarına göre belirlenir.','Barınma ve besin sağlanan her ilişkiyi kommensalizm saymak.',
 oad(d,bas=[A('Tarafların durumunu belirle','Her örnekte hangi canlının yarar sağladığı, zarar gördüğü ya da etkilenmediği belirlenir.','yarar · zarar · etkilenmeme')]),
 metin=omet('Aşağıda canlı çiftleri arasındaki bazı ilişkiler ve bu ilişkilerin türleri verilmiştir.',d,'Bu eşleştirmelerden hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru eşleştirmeler.',ip=['Her örnekte iki canlıdan hangisinin yarar, zarar ya da etkilenmeme durumunda olduğuna bak.'],
 bilgi=[B('İlişki türleri','Mutualizm: iki tür de yarar sağlar · Kommensalizm: biri yarar sağlar, diğeri etkilenmez · Amensalizm: biri zarar görür, diğeri etkilenmez')],
 puf='Önce her tarafı yarar (+), zarar (−) ya da etkilenmeme (0) olarak işaretle, sonra ilişkiyi adlandır.')

# ===== 09 · orta · metin · olumsuz · ilişki örnekleri =====
it=[('Arı – çiçekli bitki: mutualizm',True,'arı nektar ve polen elde ederken bitki tozlaşır; iki tür de yarar sağlar'),
 ('Tenya – insan: parazitlik',True,'tenya konağın sindirim kanalındaki besinden yararlanırken konak zarar görür'),
 ('Aslan – zebra: av–avcı ilişkisi',True,'aslan, zebrayı besin olarak kullanır; biri yarar sağlar, diğeri zarar görür'),
 ('Mantar – alg (liken): mutualizm',True,'mantar alge su ve mineral ile barınak sağlarken alg fotosentezle ürettiği besini mantarla paylaşır'),
 ('Aynı otlakta otlayan zebra – antilop: kommensalizm',False,'aynı sınırlı kaynağı kullanan zebra ve antilop birbirinin besin miktarını azalttığı için bu ilişki rekabettir')]
r,gz=tek(it,False,'A')
q('0009','iliski','orta','düz','Canlı çiftleri ve ilişki türleri','Verilen örneklerde ilişki türünün doğru adlandırılıp adlandırılmadığını değerlendirir.','yanlış eşleşmeyi bulma',
 'Her ilişki türü tarafların etkilenme biçimiyle tanımlanır; ortak kaynak kullanımı rekabete işaret eder.','Aynı ortamda yaşamayı kommensalizm saymak.',
 [A('Her çiftin durumunu belirle','Her örnekte hangi tarafın yarar sağladığı ya da zarar gördüğü düşünülür.','yarar · zarar · etkilenmeme'),
  A('Rekabeti ayır','Aynı sınırlı kaynağı kullanan iki tür birbirini olumsuz etkiler.','zebra – antilop: iki taraf da zarar görür'),
  A('Yanlış eşleşmeyi seç','Rekabet örneği kommensalizm olarak adlandırıldığı için yanlıştır.','yanlış eşleşme belirlendi')],
 metin='Aşağıda bazı canlı çiftleri ve aralarındaki ilişkiler eşleştirilmiştir. Bu eşleştirmelerden biri hatalıdır.\nBuna göre aşağıdaki eşleştirmelerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış eşleştirme.',ip=['Her çiftte iki canlının yarar mı zarar mı gördüğünü ayrı ayrı düşün.'],
 bilgi=[B('Ekolojik ilişkiler','Taraflardan her biri yarar (+), zarar (−) ya da etkilenmeme (0) durumunda olabilir'),B('Rekabet','İki tarafın da sınırlı bir kaynak yüzünden olumsuz etkilendiği ilişkidir')],
 puf='İki tarafın da zarar gördüğü ilişki rekabettir.')

# ===== 10 · orta · av–avcı grafiği · öncüllü =====
Tp=4.0
av=lambda t:100+60*math.sin(2*math.pi*t/Tp); avc=lambda t:50+30*math.sin(2*math.pi*(t-1)/Tp)
assert abs(av(1)-160)<1e-9 and abs(avc(2)-80)<1e-9 and abs(av(3)-40)<1e-9 and abs(avc(4)-20)<1e-9
assert av(2)<av(1) and avc(2)>avc(1) and av(3)<av(4) and avc(3)>avc(4)
sx=1.1; sy=3.0/180
g=eks(5.6,3.3,'','Popülasyon yoğunluğu')+'\\node[below] at (2.8,-.55) {Zaman};'
g+=egr([(sx*t,av(t)*sy) for t in [i*.125 for i in range(0,45)]])
g+=egr([(sx*t,avc(t)*sy) for t in [i*.125 for i in range(0,45)]],'line width=1.6pt,dashed')
for k_ in range(1,5): g+=f'\\draw[dotted,line width=.7pt] ({sx*k_},0)--({sx*k_},3.2);\\node[below] at ({sx*k_},-.05) {{$t_{k_}$}};'
g+=f'\\draw[line width=1.6pt] (4.3,3.75)--(4.9,3.75);\\node[right] at (4.9,3.75) {{Av}};\\draw[line width=1.6pt,dashed] (4.3,3.35)--(4.9,3.35);\\node[right] at (4.9,3.35) {{Avcı}};'
SEK10=tk(g)
d={'I':('t₁ anında avcı popülasyonunun yoğunluğu en yüksek değerine ulaşmıştır.',False,'avcı yoğunluğunun en yüksek olduğu an t₂’dir; t₁ anı av yoğunluğunun en yüksek olduğu andır'),
   'II':('t₁ ile t₂ arasında av yoğunluğu azalırken avcı yoğunluğu artmaktadır.',True,'bu aralıkta av eğrisi iner, avcı eğrisi çıkar'),
   'III':('t₃ anında hem av hem de avcı popülasyonunun yoğunluğu en düşük değerindedir.',False,'t₃ anında yalnız av yoğunluğu en düşüktür; avcı yoğunluğunun en düşük olduğu an t₄’tür')}
r=onc(d,'B')
q('0010','iliski','orta','öncüllü','Av–avcı popülasyon grafiği','Av ve avcı popülasyonlarının zamana göre değişimini yorumlar.','av–avcı dalgalanması',
 'Avcı popülasyonunun değişimi, av popülasyonunun değişimini bir süre gecikmeyle izler.','Av ve avcının aynı anda en yüksek değere ulaştığını sanmak.',
 oad(d,bas=[A('Tepe ve dip noktalarını bul','Av yoğunluğu t₁’de en yüksek, t₃’te en düşüktür; avcı yoğunluğu t₂’de en yüksek, t₄’te en düşüktür.','av: t₁ tepe, t₃ dip · avcı: t₂ tepe, t₄ dip')]),
 metin=omet('Bir ekosistemde yaşayan av ve avcı popülasyonlarının yoğunluklarının zamanla değişimi şekilde gösterilmiştir. Şekilde dikey kesikli çizgiler t₁, t₂, t₃ ve t₄ anlarını göstermektedir.\nBuna göre,',d,'yargılarından hangileri doğrudur?'),
 sekil=SEK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her yargıda belirtilen anlarda iki eğrinin yönüne ve yüksekliğine bak.'],
 bilgi=[B('Av–avcı ilişkisi','Avcı sayısı arttıkça av azalır; av azalınca avcının besini azalır ve avcı sayısı da düşer'),B('Dalgalanma','Bu karşılıklı etki, iki popülasyonun birbirini gecikmeyle izleyen salınımlar yapmasına yol açar')],
 puf='Avcı eğrisi, av eğrisinin bir süre gerisinden gelir; önce av tepe yapar.')

# ===== 11 · orta · süksesyon şeması · olumsuz =====
adlar=['Çıplak kaya','Likenler ve karayosunları','Otsu bitkiler','Çalılar','Orman']
g=''
for i,a_ in enumerate(adlar):
    x0=i*2.25
    g+=f'\\draw[rounded corners=3pt,line width=1pt,fill=black,fill opacity=.08] ({x0},0) rectangle ({x0+1.95},1.4);\\draw[rounded corners=3pt,line width=1pt] ({x0},0) rectangle ({x0+1.95},1.4);'
    g+=f'\\node[text width=1.8cm,align=center] at ({x0+.975},.7) {{\\footnotesize {a_}}};\\node at ({x0+.975},1.75) {{\\textbf{{{["I","II","III","IV","V"][i]}}}}};'
    if i<4: g+=f'\\draw[-{{Stealth[length=2.2mm]}},line width=1pt] ({x0+1.97},.7)--({x0+2.23},.7);'
SEK11=tk(g)
it=[('Şekilde gösterilen süreç birincil süksesyondur.',True,'süreç, daha önce hiç canlı bulunmayan çıplak kayada başlamıştır; bu nedenle birincil süksesyondur'),
 ('II. basamaktaki canlılar, kayanın ayrışmasına ve toprak oluşumuna katkı sağlayarak III. basamaktaki bitkilerin yerleşmesini kolaylaştırır.',True,'öncü türler ortamı değiştirerek sonraki türlerin yerleşmesine zemin hazırlar'),
 ('Süksesyon ilerledikçe ortamdaki toprak miktarı ve kalınlığı azalır.',False,'toprak miktarı ve kalınlığı, ölü organik maddenin birikmesi ve kayanın ayrışması sayesinde süksesyon boyunca artar'),
 ('V. basamakta oluşan komünitenin, ortam koşulları değişmedikçe görece kararlı kalması beklenir.',True,'süksesyonun son basamağında oluşan klimaks komünite, koşullar değişmedikçe kararlı kalır'),
 ('I. basamaktan V. basamağa doğru ilerledikçe komünitedeki tür çeşitliliğinin genel olarak arttığı görülür.',True,'öncü basamakta birkaç tür bulunurken ileri basamaklarda daha fazla tür bulunur')]
r,gz=tek(it,False,'E')
q('0011','sukses','orta','şekilli','Birincil süksesyon basamakları','Birincil süksesyonun basamaklarını ve toprak oluşumunu yorumlar.','süksesyon basamakları',
 'Birincil süksesyon, hiç toprak bulunmayan yerde öncü türlerle başlar ve ortam koşulları değiştikçe komünite değişir.','Süksesyonda toprağın azaldığını sanmak.',
 [A('Süreci tanımla','Başlangıçta toprak ve canlı bulunmadığından süreç birincil süksesyondur.','I: çıplak kaya → birincil'),
  A('Basamaklardaki değişimi yorumla','Öncü türler toprağı oluşturur; sonraki basamaklarda toprak kalınlaşır ve tür çeşitliliği artar.','toprak ↑ · çeşitlilik ↑'),
  A('Yanlış ifadeyi seç','Toprağın azaldığını söyleyen ifade yanlıştır.','yanlış ifade belirlendi')],
 metin='Volkanik püskürmeyle oluşan, üzerinde hiç toprak ve canlı bulunmayan bir kaya yüzeyinde zaman içinde gelişen komünite basamakları, I\'den V\'e doğru şekilde gösterilmiştir.\nBu süreçle ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SEK11,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Sürecin başlangıcında toprak olup olmadığına ve toprağın zamanla nasıl değiştiğine bak.'],
 bilgi=[B('Süksesyon','Bir alanda komünitenin zaman içinde birbirini izleyen değişimlerle değişmesidir'),B('Birincil süksesyon','Toprağın bulunmadığı alanlarda başlar; öncü türler (liken, karayosunu) toprağın oluşmasını sağlar')],
 puf='Toprak yoksa birincil, toprak varsa ikincil süksesyon söz konusudur.')

# ===== 12 · orta · öncüllü · ikincil süksesyon =====
d={'I':('Toprakta kalan tohumlar ve kök sürgünleri, bitki örtüsünün yeniden oluşmasını hızlandırabilir.',True,'toprakta kalan tohumlar ve kökler, bitki örtüsünün toprak oluşumunu beklemeden yeniden gelişmesini sağlar'),
   'II':('Yangından sonra alana ilk yerleşen canlılar, kayalık yüzeylerde yaşayabilen likenler ve karayosunlarıdır.',False,'toprağı ve tohumları yanmayan bir ormanda ilk önce toprakta bulunan tohum ve köklerden otsu bitkiler çıkar; liken öncülüğü çıplak kayada görülür'),
   'III':('Süreç boyunca ortamdaki organik madde miktarı azalır.',False,'bitkilerin ölü kalıntıları toprağa karıştığından organik madde miktarı süreç boyunca artar')}
r=onc(d,'A')
q('0012','sukses','orta','öncüllü','İkincil süksesyon','İkincil süksesyonun başlangıç koşullarını ve ilerleyişini birincil süksesyonla karşılaştırır.','ikincil süksesyon yorumu',
 'Süksesyonun başlangıç koşulları, sürecin hızını ve öncü türleri belirler.','Yangın sonrası sürecin öncü türlerinin liken olduğunu sanmak.',
 oad(d,bas=[A('Başlangıç koşulunu belirle','Yangında yalnız ağaçlar yanmış; toprak ve tohumlar durmaktadır.','toprak var')]),
 metin=omet('Bir çam ormanında çıkan yangın sonucunda ağaçlar yanmış, ancak toprak ve toprak altındaki tohumlar zarar görmemiştir. Yıllar içinde alanın bitki örtüsü yeniden oluşmuştur.\nBu süreçle ilgili,',d,'yargılarından hangileri doğrudur?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Yangından sonra toprağın ve tohumların korunup korunmadığını düşün.'],
 bilgi=[B('İkincil süksesyon','Yangın, sel ya da tarımın bırakılması gibi nedenlerle bozulmuş, ancak toprağı korunmuş alanlarda başlar'),B('Hız','Toprağın hazır olması nedeniyle birincil süksesyondan daha hızlı ilerler')],
 puf='Önce alanda toprağın ve tohumun korunup korunmadığını belirle, sonra öncü türleri düşün.')

# ===== 13 · orta · niş örtüşmesi · öncüllü =====
def ga(t,m,s): return 3.0*math.exp(-((t-m)**2)/(2*s*s))
mp,mr,ms=1.4,2.9,5.2; sd=.55
def ort(m1,m2): return sum(min(ga(t/20,m1,sd),ga(t/20,m2,sd)) for t in range(0,141))
assert ort(mp,mr)>ort(mr,ms)>ort(mp,ms) and ort(mp,ms)<0.1*ort(mp,mr) and ort(mr,ms)<0.4*ort(mp,mr)
g=eks(6.4,3.4,'Kaynak büyüklüğü','Kullanım düzeyi')
for ad_,m,st in (('P',mp,'line width=1.6pt'),('R',mr,'line width=1.6pt,dashed'),('S',ms,'line width=1.8pt,dotted')):
    g+=egr([(0.9*t,ga(t,m,sd)*1.0) for t in [i*.1 for i in range(0,71)]],st)
    g+=f'\\node[above] at ({0.9*m:.2f},{3.0+.03:.2f}) {{\\textbf{{{ad_}}}}};'
SEK13=tk(g)
d={'I':('R ile S türleri arasındaki rekabet, P ile R türleri arasındaki rekabetten daha şiddetlidir.',False,'P ile R’nin kaynak kullanım aralıkları R ile S’ninkinden daha çok örtüşür; örtüşme arttıkça rekabet de şiddetlenir'),
   'II':('P ile S türleri arasında şekildeki kaynak bakımından şiddetli rekabet vardır.',False,'P ile S’nin kullandığı kaynak aralıkları birbirinden ayrıdır; bu kaynak bakımından aralarında şiddetli rekabet beklenmez'),
   'III':('P türü ortamdan uzaklaşırsa R türünün kullandığı kaynak aralığının genişlemesi beklenebilir.',True,'rekabet ettiği türün ortamdan ayrılması, R türünün kullanabileceği kaynakları artırdığı için kaynak kullanım aralığının genişlemesine olanak verir')}
r=onc(d,'C')
q('0013','rekabet','orta','öncüllü','Ekolojik niş ve rekabet','Kaynak kullanım örtüşmesinden rekabetin şiddetini ve niş değişimini yorumlar.','niş örtüşmesi yorumu',
 'İki türün kaynak kullanım aralıkları ne kadar örtüşürse aralarındaki rekabet o kadar şiddetlidir.','Birbirine yakın yaşayan türlerin kaynak kullanımının hep örtüştüğünü sanmak.',
 oad(d,bas=[A('Örtüşmeleri karşılaştır','P ile R eğrileri belirgin biçimde örtüşür; R ile S az, P ile S ise neredeyse hiç örtüşmez.','P–R > R–S > P–S')]),
 metin=omet('Aynı habitatta yaşayan P, R ve S türlerinin kullandıkları kaynağın büyüklüğüne göre kaynak kullanım düzeyleri şekilde verilmiştir.\nBuna göre,',d,'yargılarından hangileri doğrudur?'),
 sekil=SEK13,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Eğrilerin ortak kalan bölgelerinin büyüklüğüne bak.'],
 bilgi=[B('Ekolojik niş','Bir türün kullandığı kaynakların ve yaşam koşullarının bütünüdür'),B('Rekabet ve niş','Niş örtüşmesi arttıkça rekabet artar; rekabet eden türler kaynak kullanımını değiştirerek rekabeti azaltabilir')],
 puf='Eğriler ne kadar çok örtüşürse rekabet o kadar şiddetlidir.')

# ===== 14 · orta · olumsuz · kilit taşı tür =====
it=[('Deniz yıldızı bu komünitede kilit taşı tür olarak değerlendirilebilir.',True,'deniz yıldızı kaldırılınca komünitenin yapısı belirgin biçimde bozulmuştur; bu, kilit taşı türün özelliğidir'),
 ('Deniz yıldızının uzaklaştırılması, rekabet üstünlüğü olan midyenin yayılmasına yol açmıştır.',True,'avcı baskısı kalkınca rekabette üstün olan midye çoğalıp diğer türlerin yerini almıştır'),
 ('Deniz yıldızı, komünitede popülasyon yoğunluğu en fazla olan tür olduğu için kilit taşı türdür.',False,'kilit taşı tür olmak için popülasyon yoğunluğunun fazla olması gerekmez; belirleyici olan, komünite yapısı üzerindeki etkisidir'),
 ('Kilit taşı bir türün komüniteden çıkması, tür çeşitliliğinin azalmasına yol açabilir.',True,'kilit taşı türün kaybı, komünitedeki diğer türlerin birey sayılarını değiştirerek tür çeşitliliğini azaltabilir'),
 ('Bu deney, avcı baskısının bazı komünitelerde tür çeşitliliğinin korunmasını sağlayabildiğini göstermektedir.',True,'avcının varlığında rekabette üstün tür baskın hale gelemediğinden daha fazla tür bir arada yaşayabilir')]
r,gz=tek(it,False,'B')
q('0014','komunite','orta','düz','Kilit taşı türler','Kilit taşı türün komünite yapısı üzerindeki etkisini deney sonuçlarından yorumlar.','kilit taşı tür yorumu',
 'Kilit taşı türün rolü deney verisinden yorumlanır.','Kilit taşı özelliğini tanımda yer almayan bir ölçüte bağlamak.',
 [A('Deney sonucunu yorumla','Avcı kaldırılınca midye baskın hale gelmiş ve tür sayısı azalmıştır.','avcı yok → midye çoğalır → çeşitlilik azalır'),
  A('Kilit taşı tür kavramını hatırla','Kilit taşı tür, komünite yapısı üzerindeki etkisiyle tanımlanır.','tanım: komünite etkisi'),
  A('Yanlış ifadeyi seç','Kilit taşı olmayı yoğunluğa bağlayan ifade yanlıştır.','yanlış ifade belirlendi')],
 metin='Kayalık bir kıyı komünitesinde deniz yıldızı, midyeleri ve diğer kabuklu canlıları avlayan bir türdür. Bilim insanları bir kıyı kesitinde deniz yıldızlarını uzaklaştırmış; zamanla midyelerin kıyıyı kapladığı ve alandaki tür sayısının 15’ten 8’e düştüğü, deniz yıldızlarının bırakıldığı kesitte ise tür sayısının değişmediği gözlenmiştir.\nBu deneyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Deney sonucundan bir türün hangi özelliği çıkarılabilir, hangisi çıkarılamaz?'],
 bilgi=[B('Kilit taşı tür','Komünitenin yapısı üzerinde, sayısıyla orantısız büyük etkisi olan türdür; çoğu kez bir avcıdır'),B('Avcının rolü','Avcı, rekabette üstün türün çoğalmasını sınırlayarak diğer türlerin yaşamasını sağlayabilir')],
 puf='Bir türün komünitedeki rolünü, kaldırılınca komüniteye etkisine bakarak değerlendir.')

# ===== 15 · zor · doğum–ölüm oranı grafiği · sayısal =====
b_=lambda N:0.6-0.005*N; d_=lambda N:0.1+0.005*N
assert abs(b_(50)-d_(50))<1e-12 and abs(b_(20)-.5)<1e-12 and abs(d_(20)-.2)<1e-12
g=eks(6.2,3.9,'Popülasyon yoğunluğu (birey/ha)','')+'\\node[rotate=90,above] at (-.8,1.9) {Birey başına yıllık oran};'; sx_=.1; sy_=5.0
for v in range(10,61,10): g+=f'\\draw[gray!50,line width=.5pt] ({v*sx_:.2f},0)--({v*sx_:.2f},3.7);\\node[below] at ({v*sx_:.2f},-.0) {{\\footnotesize {v}}};'
for v in range(1,8): g+=f'\\draw[gray!50,line width=.5pt] (0,{v*.1*sy_:.2f})--(6.1,{v*.1*sy_:.2f});\\node[left] at (0,{v*.1*sy_:.2f}) {{\\footnotesize 0,{v}}};'
g+=f'\\draw[line width=1.7pt] ({0:.2f},{b_(0)*sy_:.2f})--({60*sx_:.2f},{b_(60)*sy_:.2f});\\draw[line width=1.7pt,dashed] (0,{d_(0)*sy_:.2f})--({60*sx_:.2f},{d_(60)*sy_:.2f});'
g+=f'\\node[above right] at (.1,{b_(3)*sy_+.05:.2f}) {{Doğum oranı}};\\node[above left] at (6.1,{d_(60)*sy_+.05:.2f}) {{Ölüm oranı}};'
g=g.replace('\\node[below] at (3.1,-.05)','\\node[below] at (3.1,-.5)')
SEK15=tk(g)
N0=20; alan=10; net=b_(N0)-d_(N0); assert abs(net-.3)<1e-12
dog15=N0*(1+net); assert abs(dog15-26)<1e-9
yan15=[(30,'Ölüm oranını hesaba katmamış; yalnız doğum oranını kullanarak 20 × (1 + 0,5) = 30 bulmuştur.','islem'),
       (16,'Doğum oranını hesaba katmamış; yalnız ölüm oranını kullanarak 20 × (1 − 0,2) = 16 bulmuştur.','islem'),
       (50,'Doğum ve ölüm oranlarının eşitlendiği 50 birey/ha değerini, bir yıl sonraki yoğunluk sanmıştır; oysa bu değer taşıma kapasitesidir.','bilgi'),
       (260,'Yıl sonu birey sayısını (10 ha × 26 = 260) bulmuş, ancak soruda istenen yoğunluğu hesaplamamıştır.','dikkat')]
assert 20*(1+.5)==30 and 20*(1-.2)==16 and 26*alan==260
q('0015','kapasite','zor','grafik','Yoğunluğa bağlı doğum ve ölüm oranları','Yoğunluğa bağlı doğum ve ölüm oranlarından net artışı ve taşıma kapasitesini hesaplar.','yoğunluğa bağlı büyüme hesabı',
 'Doğum oranı yoğunlukla azalır, ölüm oranı artar; ikisinin kesiştiği yoğunluk taşıma kapasitesidir ve net artış oradaki oranlar farkıyla bulunur.','Yoğunluk ile birey sayısını karıştırmak.',
 [A('Oranları oku','20 birey/ha yoğunlukta doğum oranı 0,5, ölüm oranı 0,2’dir.','b = 0,5 · d = 0,2'),
  A('Net artış oranını bul','Birey başına net artış, doğum oranından ölüm oranının çıkarılmasıyla bulunur.','0,5 − 0,2 = 0,3'),
  A('Yeni yoğunluğu hesapla','Göç yoksa yoğunluk, mevcut yoğunluğun net artış oranı kadar artmış hâlidir.','20 × (1 + 0,3) = 26'),
  A('Sonucu kontrol et','26 birey/ha, doğum ve ölüm oranlarının eşitlendiği 50 birey/ha değerinden küçüktür; popülasyon hâlâ büyüyebilir.','26 < 50')],
 metin='Şekilde, bir geyik popülasyonunda yoğunluğa göre birey başına yıllık doğum oranı ve ölüm oranı verilmiştir. Alanı 10 hektar olan bir ormanda yaşayan bu popülasyonun yoğunluğu 20 birey/ha iken ortama göç olmamakta ve ortamdan ayrılan birey bulunmamaktadır.\nBuna göre bu popülasyonun bir yıl sonraki yoğunluğu kaç birey/ha olur?',
 sekil=SEK15,dogru=26,yan=yan15,istenen='Bir yıl sonraki yoğunluk (birey/ha).',ip=['Önce 20 birey/ha yoğunluğunda iki oranı grafikten oku.'],
 bilgi=[B('Yoğunluğa bağlı etkenler','Yoğunluk arttıkça doğum oranı azalır, ölüm oranı artar; popülasyon büyüme hızı yavaşlar'),B('Taşıma kapasitesi','Doğum ve ölüm oranlarının eşit olduğu yoğunlukta popülasyon büyümesi durur')],
 puf='Net artış oranı = doğum oranı − ölüm oranı; yoğunluk bu oran kadar büyür.')

# ===== 16 · zor · sayısal · lojistik + göç =====
Kc=800; rr=.4
def dN(N): 
    v=rr*N*(Kc-N)/Kc; assert abs(v-round(v))<1e-9; return round(v)
N1=200+dN(200); assert N1==260
N1g=N1+40; assert N1g==300
N2=N1g+dN(N1g); assert N2==375 and dN(300)==75
e1=200*1.4; e2=(e1+40)*1.4; assert abs(e2-448)<1e-9
assert 260+40==300 and 260+75==335 and 300*1.4==420
yan16=[(448,'Çevre direncini hiç hesaba katmamış; her yıl birey sayısını 1,4 ile çarpıp (200 × 1,4 + 40) × 1,4 = 448 bulmuştur.','bilgi'),
       (300,'Yalnız ilk yılın sonucunu ve göçü hesaplamıştır; 260 + 40 = 300 bulup ikinci yılın artışını eklememiştir.','dikkat'),
       (335,'İkinci yılın artışını doğru hesaplamış (75), ancak ilk yıl sonundaki 260 bireye eklemiş; göçle gelen 40 bireyi sonuca katmamıştır.','dikkat'),
       (420,'İlk yılı ve göçü doğru hesaplamış, ancak ikinci yılda çevre direncini yok sayarak 300 × 1,4 = 420 bulmuştur.','bilgi')]
q('0016','buyume','zor','düz','Lojistik büyüme ve göç','Lojistik büyüme modelini göç ile birlikte iki yıl boyunca uygulayarak popülasyon büyüklüğünü hesaplar.','lojistik model + göç',
 'Her yılın artışı o yılın başındaki birey sayısıyla hesaplanır; göçle gelenler artış hesabından önce sayıya eklenir.','Göçle gelen bireyleri ilk yılın artışına ya da ikinci yılın sonuna katmak.',
 [A('1. yılın artışını hesapla','Yıllık artış, r · N · (K − N) ÷ K ile bulunur.','0,4 × 200 × 600 ÷ 800 = 60'),
  A('1. yıl sonunu ve göçü ekle','İlk yıl sonunda 260 birey vardır; yıl sonunda gelen 40 birey sayıya katılır.','200 + 60 + 40 = 300'),
  A('2. yılın artışını hesapla','İkinci yılın artışı 300 birey üzerinden bulunur.','0,4 × 300 × 500 ÷ 800 = 75'),
  A('2. yıl sonunu bul','Yıl başındaki sayıya yıllık artış eklenir.','300 + 75 = 375')],
 metin='Taşıma kapasitesi (K) 800 birey olan bir adada yaşayan bir tavşan popülasyonunun birey sayısı 200’dür. Popülasyonun yıllık birey sayısı artışı (ΔN), birey başına en yüksek büyüme hızı r = 0,4 olmak üzere ΔN = r · N · (K − N) ÷ K bağıntısıyla bulunmaktadır. İlk yılın sonunda adaya, başka bir bölgeden 40 tavşan getirilmiş; sonraki yıl boyunca başka bir değişim olmamıştır.\nBuna göre ikinci yılın sonunda adadaki tavşan sayısı kaç olur?',
 dogru=375,yan=yan16,istenen='İkinci yıl sonundaki birey sayısı.',ip=['Her yılın artışını o yılın başındaki birey sayısıyla hesapla.'],
 bilgi=[B('Lojistik büyüme','Birey sayısı arttıkça (K − N) ÷ K çarpanı küçülür; bu çarpan çevre direncini temsil eder'),B('Göç','Göçle gelen bireyler popülasyon büyüklüğünü doğrudan artırır')],
 puf='Her adımda önce yıl başındaki sayıyı belirle, sonra artışı hesapla.')

# ===== 17 · zor · iki yaş piramidi · sayısal yorum =====
A_=(50,35,15); B_=(20,35,45); NA,NB=1200,1800
sa=[NA*v//100 for v in A_]; sb=[NB*v//100 for v in B_]
assert sa==[600,420,180] and sb==[360,630,810]
assert sa[0]-sb[0]==240 and sa[1]<sb[1] and sa[0]<sb[1] and sa[2]!=sb[2]
g=piramit(2.2,A_,'A',sc=.035,sayi=True,etiket=True)+piramit(7.6,B_,'B',sc=.035,sayi=True)
SEK17=tk(g)
it=[('Üreme çağındaki birey sayısı, A popülasyonunda B popülasyonundakinden fazladır.',False,'iki popülasyonda üreme çağı oranı eşittir, ancak A’da 1200 × 0,35 = 420, B’de 1800 × 0,35 = 630 birey bulunur'),
 ('Üreme öncesi birey sayısı, A popülasyonunda B popülasyonundaki üreme çağındaki birey sayısından fazladır.',False,'A’da üreme öncesi birey sayısı 600, B’de üreme çağındaki birey sayısı 630’dur; 600 < 630’dur'),
 ('Üreme sonrası grupta her iki popülasyonda da eşit sayıda birey bulunur.',False,'A’da üreme sonrası grup 1200 × 0,15 = 180, B’de 1800 × 0,45 = 810 bireydir'),
 ('Göç olmadığı koşulda, A popülasyonunun küçülmesi, B popülasyonunun ise büyümesi beklenir.',False,'A geniş tabanlı olduğundan büyüme, B dar tabanlı olduğundan küçülme eğilimindedir'),
 ('Üreme öncesi grupta A popülasyonunda, B popülasyonundakinden 240 fazla birey bulunur.',True,'A’da 1200 × 0,50 = 600, B’de 1800 × 0,20 = 360 birey vardır; fark 240’tır')]
r,gz=tek(it,True,'D')
q('0017','yapi','zor','şekilli','İki popülasyonun yaş piramidi karşılaştırması','İki yaş piramidindeki oranları popülasyon büyüklüğüyle birleştirerek birey sayılarını karşılaştırır.','oran ve sayı karşılaştırması',
 'Piramit oranları, popülasyon büyüklüğüyle çarpılınca birey sayısı verir; oranı eşit olan gruplar farklı sayıda birey içerebilir.','Oranları eşit olan grupların birey sayısının da eşit olduğunu sanmak.',
 [A('Her gruptaki birey sayısını bul','Her yaş grubunun oranı toplam birey sayısıyla çarpılır.','A: 600, 420, 180 · B: 360, 630, 810'),
  A('Üreme gruplarını karşılaştır','Üreme çağı oranları eşit olsa da A’da 420, B’de 630 birey vardır; 600 < 630’dur.','420 < 630 · 600 < 630'),
  A('Büyüme eğilimini ve farkı bul','A geniş tabanlı (büyüyen), B dar tabanlıdır (küçülen). Üreme öncesi grupta A, B’den 240 birey fazladır.','600 − 360 = 240')],
 metin='Şekilde, göçün olmadığı A ve B popülasyonlarının yaş piramitleri verilmiştir. Her basamaktaki sayı, o yaş grubundaki bireylerin popülasyonun tamamına oranını (%) göstermektedir. A popülasyonunda 1200, B popülasyonunda 1800 birey bulunmaktadır.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SEK17,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Yüzdeleri popülasyonun toplam birey sayısıyla çarparak grupları sayıya çevir.'],
 bilgi=[B('Yaş piramidi','Yaş gruplarının oranını gösterir; oran aynı olsa da birey sayısı popülasyon büyüklüğüne göre değişir')],
 puf='Önce yüzdeleri birey sayısına çevir, sonra karşılaştır.')

# ===== 18 · zor · öncüllü · ikincil süksesyon + rekabet =====
d={'I':('Süreç ilerledikçe baskın bitkilerin boyu genel olarak kısalır.',False,'baskın bitkiler yıllık otlardan çalılara ve ağaçlara geçtiğinden boy genel olarak uzar'),
   'II':('Çalıların büyümesiyle zemine ulaşan ışığın azalması, ışık isteyen otların rekabette zayıflamasına yol açabilir.',True,'yoğun çalı örtüsü zemini gölgelediğinden ışık isteyen otların rekabet gücü azalır ve yerlerini gölgeye dayanıklı türler alabilir'),
   'III':('Süksesyonun ilerleyen basamaklarında türler arası rekabet tamamen ortadan kalkar.',False,'rekabet süksesyonun her basamağında vardır; yalnız rekabette üstün türler değişir')}
r=onc(d,'E',neg=True)
q('0018','sukses','orta','öncüllü','İkincil süksesyonda tür değişimi','İkincil süksesyonu ve rekabetin tür değişimindeki rolünü birlikte yorumlar.','süksesyon + rekabet',
 'Süksesyonda ortamı değiştiren türler, rekabette üstün olan türleri değiştirir; rekabet hiçbir basamakta bitmez.','Rekabetin yalnız öncü basamakta etkili olduğunu sanmak.',
 oad(d,neg=True,bas=[A('Baskın bitkileri sırala','Otlardan çalılara, çalılardan ağaçlara doğru bir değişim vardır.','ot → çalı → ağaç')]),
 metin=omet('Terk edilmiş bir buğday tarlasında önce yıllık otlar, birkaç yıl sonra çok yıllık otlar, daha sonra çalılar ve son olarak ışık seven ağaçlar baskın hale gelmiştir. Yıllar sonra ağaçların gölgesinde, gölgede yetişebilen ağaç türleri çoğalmaya başlamıştır.\nBu süreçle ilgili,',d,'yargılarından hangileri yanlıştır?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yargılar.',ip=['Başlangıçta toprağın hazır olup olmadığını ve ışığın türler arası rekabeti nasıl etkilediğini düşün.'],
 bilgi=[B('Süksesyonda tür değişimi','Her basamaktaki türler ortamı (ışık, toprak, nem) değiştirir; bu değişim sonraki türlerin rekabet gücünü etkiler'),B('Rekabet','Süksesyonun tüm basamaklarında görülür; rekabet gücü üstün tür değiştikçe komünite de değişir')],
 puf='Süksesyonda rekabet bitmez; ortam değiştikçe rekabette üstün olan tür değişir.')

# ===== 19 · zor · sütun grafiği · kilit taşı deneyi =====
TA=(15,15,14,15); TB=(15,12,9,7); XA=(30,32,31,30); XB=(30,45,62,80)
assert XB[3]/XB[0]>2 and TB[3]<TB[0]/2 and TA[2]!=TA[0]
def bars(x0,A_,B_,ymax,ticks,title):
    sc=2.5/ymax; s=f'\\draw[-{{Stealth[length=2mm]}},line width=.9pt] ({x0},0)--({x0+4.2},0);\\draw[-{{Stealth[length=2mm]}},line width=.9pt] ({x0},0)--({x0},2.8);'
    for v in ticks: s+=f'\\draw ({x0},{v*sc:.2f})--({x0-.08},{v*sc:.2f});'
    for i in range(4):
        xx=x0+.25+i*1.0
        s+=f'\\draw[fill=black,fill opacity=.12,line width=.8pt] ({xx:.2f},0) rectangle ({xx+.4:.2f},{A_[i]*sc:.2f});\\draw[fill=black,fill opacity=.6,line width=.8pt] ({xx+.4:.2f},0) rectangle ({xx+.8:.2f},{B_[i]*sc:.2f});'
        s+=f'\\node[above] at ({xx+.2:.2f},{A_[i]*sc:.2f}) {{\\footnotesize {A_[i]}}};\\node[above] at ({xx+.6:.2f},{B_[i]*sc:.2f}) {{\\footnotesize {B_[i]}}};\\node[below] at ({xx+.4:.2f},0) {{\\footnotesize {i}}};'
    s+=f'\\node[above] at ({x0+2.1},2.85) {{\\small {title}}};\\node[below] at ({x0+2.1},-.4) {{\\footnotesize Yıl}};'
    return s
g=bars(0,TA,TB,20,(0,5,10,15),'Tür sayısı')+bars(5.6,XA,XB,100,(0,25,50,75),'X türünün kaplama oranı (\\%)')
g+='\\draw[fill=black,fill opacity=.12,line width=.8pt] (1.2,-1.5) rectangle (1.5,-1.25);\\node[right] at (1.55,-1.375) {\\footnotesize A alanı};\\draw[fill=black,fill opacity=.6,line width=.8pt] (3.6,-1.5) rectangle (3.9,-1.25);\\node[right] at (3.95,-1.375) {\\footnotesize B alanı};'
SEK19=tk(g)
it=[('A alanında tür sayısı yıllar içinde sürekli artmıştır.',False,'A alanında tür sayısı 15, 15, 14, 15 olarak değişmiştir; belirgin bir artış yoktur'),
 ('B alanında X türünün kaplama oranı arttıkça tür sayısı da artmıştır.',False,'B alanında X türünün kaplama oranı artarken tür sayısı 15’ten 7’ye düşmüştür'),
 ('Otçul tür, X türünün popülasyonunu tamamen yok ettiği için A alanında tür sayısı sabit kalmıştır.',False,'A alanında X türünün kaplama oranı yaklaşık %30 düzeyinde kalmıştır; otçul tür X türünü yok etmemiştir'),
 ('Deney, otçul türün komünitedeki en kalabalık popülasyon olduğunu göstermektedir.',False,'deney otçul türün popülasyon yoğunluğuna ilişkin bir veri vermez; yalnız otçulun varlığı ve yokluğunun etkisini gösterir'),
 ('B alanında X türünün kaplama oranı 2 katından fazla artarken tür sayısı yarıdan fazla azalmıştır.',True,'X türünün kaplama oranı %30’dan %80’e (2 katından fazla), tür sayısı 15’ten 7’ye (yarıdan fazla) değişmiştir')]
r,gz=tek(it,True,'E')
q('0019','komunite','zor','grafik','Otçul uzaklaştırma deneyi','Otçul uzaklaştırma deneyinde iki grafikteki verileri birlikte yorumlayarak kilit taşı türün etkisini değerlendirir.','iki grafik birlikte yorum',
 'Kilit taşı otçul kalkınca rekabette üstün tür çoğalır ve tür çeşitliliği azalır.','Tür sayısının azalmasını yalnız otçulun varlığına bağlamak.',
 [A('A alanını oku','Otçul varken tür sayısı yaklaşık 15’te, X türünün kaplama oranı yaklaşık %30’da kalır.','A: ≈15 tür · ≈%30'),
  A('B alanını oku','Otçul uzaklaştırılınca X türünün kaplama oranı %30’dan %80’e çıkar, tür sayısı 15’ten 7’ye iner.','B: %30 → %80 · 15 → 7'),
  A('Oranları karşılaştır','80 ÷ 30 yaklaşık 2,7 olduğundan kaplama 2 katından fazla artmıştır; 7 sayısı 15’in yarısından (7,5) küçüktür.','2,7 > 2 · 7 < 7,5'),
  A('Doğru ifadeyi seç','Bu iki bulguyu birlikte veren ifade doğrudur.','doğru ifade belirlendi')],
 metin='Bir çayır komünitesinde, rekabette üstün olan X türünü tüketen bir otçul türün etkisini araştırmak için iki alanda üç yıl süren bir deney yapılmıştır. A alanında otçul tür bırakılmış, B alanında ise otçul tür uzaklaştırılmıştır. Alanlardaki tür sayısı ve X türünün kaplama oranı (%) her yılın sonunda ölçülmüştür. Sonuçlar şekilde verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SEK19,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['İki grafiği aynı alan için birlikte oku.'],
 bilgi=[B('Otçul baskısı ve çeşitlilik','Otçul baskısı kalkınca rekabette üstün tür aşırı çoğalıp diğer türlerin elenmesine yol açabilir')],
 puf='İki grafiği aynı alan için birlikte okuyup her ifadeyi verilerle sına.')

# ===== 20 · zor · öncüllü · besin zinciri etkisi =====
d={'I':('Küçük balıkların popülasyon yoğunluğu azalabilir.',True,'turna balığı küçük balıkları avladığından sayısı artınca küçük balıkların yoğunluğu azalabilir'),
   'II':('Su pirelerinin popülasyon yoğunluğu artabilir.',True,'küçük balıkların azalması, su pirelerinin avcı baskısını azaltır ve su pirelerinin çoğalmasına yol açabilir'),
   'III':('Kabuklu türün popülasyon yoğunluğu azalabilir.',True,'su pirelerinin artması, aynı alglerden yararlanan kabuklu türle rekabeti artırır ve kabuklunun yoğunluğunu azaltabilir')}
r=onc(d,'E')
q('0020','komunite','zor','öncüllü','Besin zincirinde dolaylı etkiler','Komünitedeki bir türün sayısının değişmesinin besin zinciri boyunca dolaylı etkilerini yorumlar.','dolaylı etki zinciri',
 'Komünitede bir türdeki değişim, besin ilişkileri yoluyla birbirini izleyen türlerin yoğunluğunu da değiştirir.','Etkinin yalnız doğrudan avlanan türle sınırlı olduğunu sanmak.',
 oad(d,bas=[A('Besin zincirini ve rekabeti kur','Su pireleri ile kabuklu tür aynı alglerden yararlanır; zincir alg, su piresi, küçük balık ve turna şeklindedir.','turna ↑ → küçük balık ↓ → pire ↑ → ?')]),
 metin=omet('Bir göl komünitesinde su pireleri algleri, küçük balıklar su pirelerini, turna balıkları ise küçük balıkları tüketmektedir. Algleri tüketen bir kabuklu tür de su pireleriyle aynı alglerden yararlanmakta, ancak turna balığının ve küçük balıkların besini olmamaktadır. Başka bir göldeki turna balığı, bu göle çok sayıda bırakılmış ve popülasyonu hızla büyümüştür. Gölde başka bir değişiklik olmamıştır.\nBu durumda,',d,'yargılarından hangilerinin gerçekleşmesi beklenebilir?'),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Gerçekleşmesi beklenebilen yargılar.',ip=['Değişimin her basamakta hangi türü, nasıl etkilediğini sırayla izle.'],
 bilgi=[B('Besin ilişkileri ve komünite','Komünitedeki türler besin ilişkileriyle birbirine bağlıdır; bir türün sayısındaki değişim zincirdeki diğer türleri dolaylı olarak etkiler')],
 puf='Etkiyi basamak basamak izle ve besin ilişkisinin yanında rekabeti de ele al.')

# ===== bitiş =====
assert len(USED)==20
P.ANA.sort(key=lambda x:x['id'])
for x in P.ANA: x['kardes']=None
out=os.path.join(BD,'populasyon-1.json')
P.yaz(out,'/tmp/bos-populasyon.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Biyoloji çıkmış soruları (mantık), MEB 12. sınıf.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abpopulasyon.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
