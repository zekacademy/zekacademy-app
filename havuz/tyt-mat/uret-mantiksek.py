"""Mantık · ŞEKİLLİ paket (6 soru): Venn, doğruluk tablosu, devre şeması, kart tablosu; her doğru ve çeldirici değer doğruluk tablosu taramasıyla doğrulanır. Kardeş yok, ipucu 1."""
import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Mantık'
UK='matd|Mantık'
P=Parti('mantiksek','Mantık',UK)
KY='ÖSYM 2021–2026 TYT Matematik (Mantık, her yıl 1 soru; şekilli/tablolu/devre örnekleri; yalnız mantık) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf Mantık'
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

NIC=B('Niceleyiciler','“Her” (∀) önermesi, kümenin bütün elemanları için doğruysa doğrudur; tek bir karşı örnek onu yanlış yapar. “En az bir” (∃) önermesi, koşulu sağlayan tek bir eleman bulunursa doğrudur. Örnek: A = {2, 4, 6} için (∀x ∈ A) x çifttir doğru, (∃x ∈ A) x > 5 de doğrudur')
OLU=B('Niceleyicinin olumsuzu','(∀x) p(x) önermesinin olumsuzu (∃x) p(x)′, (∃x) p(x) önermesinin olumsuzu (∀x) p(x)′ biçimindedir. Bir önermenin olumsuzunun doğru olması, önermenin yanlış olması demektir. Örnek: “Her kuş uçar” yanlışsa olumsuzu “uçmayan en az bir kuş vardır” doğrudur')
TAB=B('Doğruluk tablosu','Bileşik önermenin değeri, içteki parçalardan başlanarak her satır için ayrı hesaplanır; p ⇒ q yalnız p = 1 ve q = 0 iken 0, p ⇔ q ise p ile q aynı değerde iken 1’dir. Örnek: p′ ∨ q ifadesi p = 1, q = 0 satırında 0 ∨ 0 = 0’dır')
DEV=B('Anahtarlı devre','Seri bağlı anahtarlar “ve” (∧), paralel bağlı anahtarlar “veya” (∨) ile gösterilir; bir anahtar kapalı iken karşılık gelen önerme 1, açık iken 0’dır; p′ yazılı anahtar, p = 0 iken kapalıdır. Örnek: p seri (q paralel r) devresi p ∧ (q ∨ r) ile gösterilir')
DEN=B('Devre sadeleştirme','Aynı ifade çarpanlara ayrılarak ya da doğruluk tablosuyla sadeleştirilir; iki ifade bütün satırlarda aynı değeri veriyorsa denktir. Örnek: (a ∧ b) ∨ (a ∧ c) ifadesi a ∧ (b ∨ c) ile denktir')
KOŞ=B('Koşullu önermenin biçimleri','p ⇒ q için karşıtı q ⇒ p, tersi p′ ⇒ q′, karşıt tersi q′ ⇒ p′’dür; p ⇒ q ile yalnız karşıt tersi (ve p′ ∨ q) her durumda aynı değerdedir. Örnek: “a > 0 ise a² > 0” önermesinin karşıt tersi “a² ≤ 0 ise a ≤ 0”dır')

# ---------- kartlar ----------
kartla('K-MNS-01','Venn şemasında niceleyiciler','Şemadaki elemanlar bölgelerden okunur; “her” için karşı örnek, “en az bir” için örnek aranır.','“Her” önermesini tek örnekle doğrulamak; kesişimi boş sanmak; dışarıdaki elemanları unutmak.','kolay','öncüllü',3,'mns-venn','Venn şeması ve niceleyiciler')
kartla('K-MNS-02','Niceleyicili önermenin olumsuzu ve Venn','Olumsuzu doğru olan, kendisi yanlış olan önermedir; her önerme şemadaki elemanlarla sınanır.','Olumsuzu alıp yanlış yöne yorumlamak; “her”i tek örnekle doğrulamak.','orta','şekilli',4,'mns-nicelik','Olumsuzu doğru olan önerme')
kartla('K-MNS-03','Doğruluk tablosunda bilinmeyen hücreler','Bileşik önerme, her satırdaki p, q, r değerleriyle içten dışa hesaplanır.','⇒ işlemini “ve” gibi hesaplamak; olumsuzu atlamak; ⇔ ile ⇒’yı karıştırmak.','orta','tablo',4,'mns-tablo','Doğruluk tablosu tamamlama')
kartla('K-MNS-04','Anahtarlı devrede akım geçen durumlar','Seri “ve”, paralel “veya” ile ifade yazılır; anahtar durumları taranıp akım geçenler sayılır.','Seri ile paraleli karıştırmak; yalnız akım geçmeyenleri saymak.','orta','şekilli',4,'mns-devre','Devre durumları sayma')
kartla('K-MNS-05','Devrenin denk ifadesi','Devrenin ifadesi yazılıp sadeleştirilir; seçenekler doğruluk tablosuyla sınanır.','Alt koldaki ortak anahtarı unutmak; seri-paralel yerini değiştirmek.','zor','şekilli',5,'mns-denk','Devrenin sade ifadesi')
kartla('K-MNS-06','Karşıt, ters ve karşıt ters kartları','Kartlardaki koşullu cümleler p ve q ile ifade edilir; p ⇒ q doğru iken her durumda doğru kalanlar seçilir.','Tersi ile karşıt tersi karıştırmak; karşıtı denk sanmak.','kolay','tablo',4,'mns-kart','Koşullu önerme kartları')

# ===== yardımcı: önerme ifade değerlendirme =====
def tara(f,n): return [f(*v) for v in itertools.product((1,0),repeat=n)]
imp=lambda a,b: int((not a) or b)
iff=lambda a,b: int(a==b)

# ================= 01 kolay · Venn + niceleyici (öncüllü) =================
U=['Ali','Banu','Cem','Defne','Emre','Faruk','Gül','Hakan']
S={'Ali','Banu','Cem'}; R={'Cem','Defne','Emre'}
I1=any(x in S and x in R for x in U); I2=all((x in R) for x in S); I3=any((x not in S and x not in R) for x in U)
assert (I1,I2,I3)==(True,False,True)
o=['\\draw[thick] (-0.4,-1.9) rectangle (6.6,2.1);',
   '\\draw[thick] (2.1,0.1) circle (1.5); \\draw[thick] (4.1,0.1) circle (1.5);',
   '\\node at (1.5,1.95) {};','\\node[above] at (1.7,1.55) {Satranç}; \\node[above] at (4.5,1.55) {Resim};',
   '\\node at (1.45,0.45) {Ali}; \\node at (1.45,-0.35) {Banu}; \\node at (3.1,0.05) {Cem};',
   '\\node at (4.75,0.45) {Defne}; \\node at (4.75,-0.35) {Emre};',
   '\\node at (0.2,-1.4) {Faruk}; \\node at (6.0,-1.4) {Gül};']
SK=fig('\n'.join(o))
oncul=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III']
q('0001',tipId='mns-venn',tip='Venn şeması ve niceleyiciler',z='kolay',alt='Niceleyiciler',kaz='Venn şemasındaki elemanlara bakarak “her” ve “en az bir” önermelerinin doğruluğunu belirler.',kalip='öncüllü',
 kart='K-MNS-01 (Venn ve niceleyiciler) · 8 öğrenci, 2 kurs',
 metin='Bir ortaokulda sekiz öğrencinin satranç ve resim kurslarına katılım durumu, şekildeki Venn şemasıyla gösterilmiştir; şemadaki dikdörtgen sekiz öğrencinin tamamını göstermektedir.\nI. Her iki kursa da katılan en az bir öğrenci vardır.\nII. Satranç kursuna katılan her öğrenci resim kursuna da katılmaktadır.\nIII. Kurslardan hiçbirine katılmayan en az bir öğrenci vardır.\nBu önermelerden hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','III. önermedeki Faruk ile Gül’ü kursa katılıyor sanmış; dikdörtgenin dışında kalanları atlamış.','dikkat'),('Yalnız II','II. önermeyi Cem örneğiyle doğru sanmış; kesişimi ve dikdörtgenin dışında kalanları saymadığı için I ve III’ü yanlış bulmuş.','dikkat'),('II ve III','II. önermeyi tek örnekle (Cem) doğru sanmış; I. önermeyi de kesişimi boş sanarak yanlış bulmuş.','dikkat'),('I, II ve III','II. önermeyi Cem örneğiyle doğru sanmış.','dikkat')],
 sira=oncul,istenen='Doğru olan önermeler.',ip=['“Her” ve “en az bir” önermelerini şemadaki isimlere bakarak ayrı ayrı sına.'],bilgi=[NIC],sekil=SK,
 ad=[A('I. önerme','Kesişimde bir isim aranır.','Cem iki kursta → doğru'),A('II. önerme','Satranç kursundaki herkes resimdedir mi? Ali yalnız satranç kursundadır.','Karşı örnek Ali → yanlış'),A('III. önerme','Dikdörtgenin içinde ama iki dairenin dışında kalan isimlere bakılır.','Faruk ve Gül → doğru'),A('Sonuç','Doğru olanlar belirlenir.','I ve III')],
 puf='“Her” için bir karşı örnek yeter; “en az bir” için bir örnek yeter.')

# ================= 02 orta · Venn + olumsuzu doğru olan =================
E2=set(range(1,11)); A2={2,3,5,7}; B2={1,3,5,7,9}
ST=[
 ('(∀x ∈ B) x ∈ A',lambda:all(x in A2 for x in B2),'B kümesinde A’da olmayan 1 (ve 9) vardır; önerme yanlış, olumsuzu doğrudur.'),
 ('(∃x ∈ A) x ∉ B',lambda:any(x not in B2 for x in A2),'2, A’da olup B’de olmadığından önerme doğrudur; olumsuzu yanlıştır.'),
 ('(∀x ∈ A) x > 1',lambda:all(x>1 for x in A2),'A’nın bütün elemanları 1’den büyüktür; önerme doğrudur, olumsuzu yanlıştır.'),
 ('(∃x ∈ E) x ∉ A ∧ x ∉ B',lambda:any(x not in A2 and x not in B2 for x in E2),'4, iki kümenin de dışındadır; önerme doğrudur, olumsuzu yanlıştır.'),
 ('(∀x ∈ B) x < 10',lambda:all(x<10 for x in B2),'B’nin en büyük elemanı 9’dur; önerme doğrudur, olumsuzu yanlıştır.'),
]
dg=[f() for _,f,_ in ST]; assert dg==[False,True,True,True,True]
o=['\\draw[thick] (-0.3,-2.0) rectangle (6.7,2.2);',
   '\\draw[thick] (2.2,0.1) circle (1.6); \\draw[thick] (4.2,0.1) circle (1.6);',
   '\\node[above] at (1.5,1.62) {A}; \\node[above] at (4.9,1.62) {B};',
   '\\node at (1.3,0.1) {2}; \\node at (3.2,0.75) {3}; \\node at (3.2,0.1) {5}; \\node at (3.2,-0.55) {7};',
   '\\node at (5.1,0.55) {1}; \\node at (5.1,-0.3) {9};',
   '\\node at (0.3,-1.5) {4}; \\node at (1.0,-1.5) {6}; \\node at (5.6,-1.5) {8}; \\node at (6.2,-1.5) {10};']
SK=fig('\n'.join(o))
sirasi=[ST[0][0]]+[ST[i][0] for i in (1,2,3,4)]
q('0002',tipId='mns-nicelik',tip='Olumsuzu doğru olan önerme',z='orta',alt='Niceleyiciler',kaz='Venn şemasındaki elemanlarla niceleyicili önermeleri sınayıp olumsuzu doğru olanı bulur.',kalip='şekilli',
 kart='K-MNS-02 (olumsuzu doğru olan) · A = {2,3,5,7}, B = {1,3,5,7,9}',
 metin='Şekilde, E = {1, 2, …, 10} evrensel kümesinin A ve B alt kümeleri Venn şemasıyla gösterilmiştir; şemadaki dikdörtgen E kümesini göstermektedir.\nBuna göre, aşağıdaki önermelerden hangisinin olumsuzu doğrudur?',
 dogru=ST[0][0],yan=[(ST[i][0],ST[i][2],'dikkat') for i in (1,2,3,4)],sira=sirasi,istenen='Olumsuzu doğru olan, yani kendisi yanlış olan önerme.',
 ip=['Olumsuzunun doğru olması için önermenin kendisi yanlış olmalıdır; her seçeneği şemadaki elemanlarla sına.'],bilgi=[NIC,OLU],sekil=SK,
 ad=[A('Koşulu çevir','Olumsuzu doğru olan, kendisi yanlış olan önermedir.','Yanlış önermeyi ara'),A('Önermeleri sına','Her seçenek şemadaki elemanlarla denetlenir.','Üç “∀” ve iki “∃”'),A('Karşı örnek','(∀x ∈ B) x ∈ A için B’de A’nın dışında 1 ve 9 vardır.','Önerme yanlış'),A('Sonuç','Diğer dört önerme doğrudur.','(∀x ∈ B) x ∈ A')],
 puf='“Olumsuzu doğru” demek “kendisi yanlış” demektir.')

# ================= 03 orta · doğruluk tablosu =================
E3=lambda p,q,r: iff(imp(p,1-q),r)
HM=[(lambda p,q,r:iff(int(p and (1-q)),r),'p ⇒ q′ yerine p ∧ q′ almış.','islem'),
    (lambda p,q,r:iff(imp(p,q),r),'q′ yerine q almış (olumsuzu atlamış).','dikkat'),
    (lambda p,q,r:imp(imp(p,1-q),r),'⇔ yerine ⇒ işlemi yapmış.','islem'),
    (lambda p,q,r:iff(imp(1-q,p),r),'p ⇒ q′ koşulunu ters yönde (q′ ⇒ p) okumuş.','dikkat'),
    (lambda p,q,r:iff(imp(1-p,1-q),r),'p yerine p′ almış (olumsuzu yanlış yere koymuş).','dikkat'),
    (lambda p,q,r:int(imp(p,1-q) and r),'⇔ yerine ∧ işlemi yapmış.','islem')]
tum=list(itertools.product((1,0),repeat=3))
def coz(f,rw,k,sonuc):
    """rw satırında k. hücre bilinmiyor; sonucu veren değer (tek ise) ya da None"""
    c=[]
    for d in (1,0):
        t=list(rw); t[k]=d
        if f(*t)==sonuc: c.append(d)
    return c[0] if len(c)==1 else None
import random as _r
rg=_r.Random(11); sec=None
for deneme in range(400000):
    rr=[rg.choice(tum) for _ in range(4)]; kk=[rg.choice((0,1,2,2,2)) for _ in range(4)]
    if len(set(rr))<4: continue
    sn=[E3(*r_) for r_ in rr]
    dv=[coz(E3,r_,k_,sn_) for r_,k_,sn_ in zip(rr,kk,sn)]
    if None in dv or [r_[k_] for r_,k_ in zip(rr,kk)]!=dv: continue
    if len(set(sn))<2: continue
    ev=[[coz(h[0],r_,k_,sn_) for r_,k_,sn_ in zip(rr,kk,sn)] for h in HM]
    ok_=[i for i,e_ in enumerate(ev) if None not in e_ and e_!=dv]
    sc=[]; gor=set()
    for i in ok_:
        if tuple(ev[i]) not in gor: gor.add(tuple(ev[i])); sc.append(i)
    if len(sc)>=4: sec=(rr,kk,sn,dv,[ev[i] for i in sc[:4]],sc[:4]); break
assert sec; rr,kk,sn,dv,ev,hi=sec
sat=[]
for r_,k_,sn_ in zip(rr,kk,sn):
    h=[str(x) for x in r_]; h[k_]='abcd'[len(sat)]; sat.append(h+[str(sn_)])
SK=tablo_svg(['p','q','r','(p ⇒ q′) ⇔ r'],sat)
fm_=lambda t:', '.join(map(str,t))
sira3=[fm_(dv)]+[fm_(t) for t in ev]; _r.Random(7).shuffle(sira3)
q('0003',tipId='mns-tablo',tip='Doğruluk tablosu tamamlama',z='orta',alt='Bileşik Önermeler',kaz='Bileşik önermenin sonucu verilen satırlardan eksik doğruluk değerlerini bulur.',kalip='tablo',
 kart='K-MNS-03 (doğruluk tablosu, eksik hücre) · (p ⇒ q′) ⇔ r',
 metin='Aşağıdaki tablonun her satırında p, q ve r önermelerinin bir doğruluk değeri durumu ile bu durumda (p ⇒ q′) ⇔ r bileşik önermesinin değeri yazılmıştır. Her satırda yalnız bir hücrenin değeri a, b, c ve d harfleriyle gizlenmiştir.\nBuna göre, gizlenen a, b, c, d değerleri sırasıyla aşağıdakilerden hangisidir?',
 dogru=fm_(dv),yan=[(fm_(ev[j]),HM[hi[j]][1],HM[hi[j]][2]) for j in range(4)],
 sira=sira3,istenen='Gizlenen a, b, c, d değerleri.',ip=['Her satırda bilinen değerlerle önermeyi hesapla; sonucun tablodaki değerle uyması için gizli hücrenin ne olması gerektiğine bak.'],bilgi=[TAB],sekil=SK,
 ad=[A('Satırları oku','Her satırda bir hücre gizli, sonuç biliniyor.',', '.join(''.join(h_[:3]) for h_ in sat)),A('p ⇒ q′ değerini bul','⇔ ile r’nin sonucu verdiği değeri sağlayan p ⇒ q′ değeri her satırda belirlenir.','Her satırda tek değer'),A('Gizli hücreyi çöz','Gizli hücreye hangi değer verilirse p ⇒ q′ gereken değeri alıyor, denenir.',f'Değerler: {fm_(dv)}'),A('Sonuç','a, b, c, d sırasıyla.',fm_(dv))],
 puf='Her satırı ayrı çöz: gizli hücreye 1 ve 0 yazıp hangisinin tablodaki sonucu verdiğine bak.')

# ================= 04 orta · devre şeması (akım geçen durum sayısı) =================
def sw(x,y,lab,w=1.0,under=False):
    a=x+0.25; b=x+w-0.25
    t=[f'\\draw[thick] ({x:.2f},{y}) -- ({a:.2f},{y}); \\draw[thick] ({a:.2f},{y}) -- ({b-0.05:.2f},{y+0.32}); \\draw[thick] ({b:.2f},{y}) -- ({x+w:.2f},{y});',
       f'\\fill ({a:.2f},{y}) circle (0.05); \\fill ({b:.2f},{y}) circle (0.05);']
    t.append(f'\\node[below=3pt] at ({x+w/2:.2f},{y-0.02}) {{{lab}}};' if under else f'\\node[above=5pt] at ({x+w/2:.2f},{y+0.1}) {{{lab}}};')
    return t
o=[]
o.append('\\draw[thick] (0,1.5) -- (0.4,1.5);'); o+=sw(0.4,1.5,'$p$')
o.append('\\draw[thick] (1.4,1.5) -- (1.9,1.5); \\draw[thick] (1.9,2.1) -- (1.9,0.9);')
o.append('\\draw[thick] (1.9,2.1) -- (2.2,2.1);'); o+=sw(2.2,2.1,'$q$'); o.append('\\draw[thick] (3.2,2.1) -- (3.5,2.1);')
o.append('\\draw[thick] (1.9,0.9) -- (2.2,0.9);'); o+=sw(2.2,0.9,'$r$',under=True); o.append('\\draw[thick] (3.2,0.9) -- (3.5,0.9);')
o.append('\\draw[thick] (3.5,2.1) -- (3.5,0.9); \\draw[thick] (3.5,1.5) -- (4.1,1.5);')
o.append('\\draw[thick] (0,-0.3) -- (1.3,-0.3);'); o+=sw(1.3,-0.3,'$s$',w=1.1,under=True); o.append('\\draw[thick] (2.4,-0.3) -- (4.1,-0.3);')
o.append('\\draw[thick] (0,1.5) -- (0,-0.3); \\draw[thick] (4.1,1.5) -- (4.1,-0.3);')
o.append('\\draw[thick] (-0.6,0.6) -- (0,0.6); \\draw[thick] (4.1,0.6) -- (4.7,0.6); \\node[left] at (-0.6,0.6) {A}; \\node[right] at (4.7,0.6) {B};')
o.append('\\fill (0,0.6) circle (0.05); \\fill (4.1,0.6) circle (0.05);')
SK=fig('\n'.join(o))
ak=lambda p,q,r,s: int((p and (q or r)) or s)
v=sum(tara(ak,4)); assert v==11
h1=sum(tara(lambda p,q,r,s:int(p and q and r and s),4))                 # hepsi seri
h2=16-v                                                                   # akım geçmeyen
h3=sum(tara(lambda p,q,r,s:s,4))                                          # yalnız s kolu
h4=sum(tara(lambda p,q,r,s:int(p or q or r or s),4))                      # hepsi paralel
assert [h1,h2,h3,h4]==[1,5,8,15] and len({v,h1,h2,h3,h4})==5
q('0004',tipId='mns-devre',tip='Devre durumları sayma',z='orta',alt='Devre Şemaları',kaz='Anahtarlı devrenin ifadesini yazıp akım geçen anahtar durumlarının sayısını bulur.',kalip='şekilli',
 kart='K-MNS-04 (devre, akım geçen durum) · (p ∧ (q ∨ r)) ∨ s',
 metin='Şekildeki devrede p, q, r ve s anahtarlarının her biri açık ya da kapalı olabilir. Seri bağlı anahtarlar “ve”, paralel bağlı anahtarlar “veya” işlemine karşılık gelir; bir anahtar kapalı iken karşılık gelen önermenin doğruluk değeri 1, açık iken 0 kabul edilmektedir. Dört anahtarın bütün açık–kapalı durumları (16 durum) ayrı ayrı düşünülmektedir.\nBuna göre, A ile B arasında akımın geçtiği kaç farklı durum vardır?',
 dogru=v,yan=[(h1,'Bütün anahtarların seri bağlı olduğunu düşünerek yalnız hepsinin kapalı olduğu durumu saymış.','dikkat'),(h2,'Akımın geçmediği durumların sayısını (16 − 11) yazmış.','dikkat'),(h3,'Yalnız s anahtarının bulunduğu kolu hesaba katmış (s = 1 olan 8 durum).','dikkat'),(h4,'Bütün anahtarların paralel bağlı olduğunu düşünüp en az biri kapalı olan durumları saymış.','dikkat')],
 istenen='Akımın geçtiği durum sayısı.',ip=['Devrenin “ve”–“veya” ile ifadesini yazıp hangi anahtar durumlarında akım geçtiğine bak.'],bilgi=[DEV],sekil=SK,
 ad=[A('Devreyi yaz','p seri (q paralel r) kolu ile s koluna paraleldir.','(p ∧ (q ∨ r)) ∨ s'),A('s kapalıyken','s = 1 ise akım geçer; diğer üç anahtar serbesttir.','2³ = 8 durum'),A('s açıkken','s = 0 iken p = 1 ve q, r’den en az biri 1 olmalıdır.','1 · 3 = 3 durum'),A('Topla','İki durum ayrık olduğundan toplanır.','8 + 3 = 11')],
 puf='Önce s anahtarının kapalı ve açık olduğu iki durumu ayrı ele al.')

# ================= 05 zor · devrenin denk ifadesi =================
def sw2(x,y,lab,w=1.0):
    a=x+0.25; b=x+w-0.25
    return [f'\\draw[thick] ({x:.2f},{y}) -- ({a:.2f},{y}); \\draw[thick] ({a:.2f},{y}) -- ({b-0.05:.2f},{y+0.32}); \\draw[thick] ({b:.2f},{y}) -- ({x+w:.2f},{y});',
            f'\\fill ({a:.2f},{y}) circle (0.05); \\fill ({b:.2f},{y}) circle (0.05); \\node[above=5pt] at ({x+w/2:.2f},{y+0.1}) {{{lab}}};']
o=[]
o.append('\\draw[thick] (0,1.0) -- (0.4,1.0);'); o+=sw2(0.4,1.0,'$p$'); o.append('\\draw[thick] (1.4,1.0) -- (1.6,1.0);'); o+=sw2(1.6,1.0,'$q$'); o.append('\\draw[thick] (2.6,1.0) -- (5.2,1.0);')
o.append('\\draw[thick] (0,-0.8) -- (0.4,-0.8);'); o+=sw2(0.4,-0.8,'$p$'); o.append('\\draw[thick] (1.4,-0.8) -- (1.6,-0.8);'); o+=sw2(1.6,-0.8,'$q\'$'); o.append('\\draw[thick] (2.6,-0.8) -- (2.8,-0.8);'); o+=sw2(2.8,-0.8,'$r$'); o.append('\\draw[thick] (3.8,-0.8) -- (5.2,-0.8);')
o.append('\\draw[thick] (0,1.0) -- (0,-0.8); \\draw[thick] (5.2,1.0) -- (5.2,-0.8);')
o.append('\\draw[thick] (-0.6,0.1) -- (0,0.1); \\draw[thick] (5.2,0.1) -- (5.8,0.1); \\node[left] at (-0.6,0.1) {A}; \\node[right] at (5.8,0.1) {B}; \\fill (0,0.1) circle (0.05); \\fill (5.2,0.1) circle (0.05);')
SK=fig('\n'.join(o))
dev=lambda p,q,r: int((p and q) or (p and (1-q) and r))
sade=lambda p,q,r: int(p and (q or r))
assert tara(dev,3)==tara(sade,3)
sec5=[
 ('p ∧ (q ∨ r)',sade,None),
 ('(p ∧ q) ∨ r',lambda p,q,r:int((p and q) or r),'Alt koldaki p ve q′ anahtarlarını yazmayıp yalnız r’yi almış.'),
 ('p ∨ (q ∧ r)',lambda p,q,r:int(p or (q and r)),'İfadeyi p’yi dışarı alırken seri ile paralel işaretlerini karıştırmış.'),
 ('p ∧ q ∧ r',lambda p,q,r:int(p and q and r),'Bütün anahtarları seri bağlı sanmış.'),
 ('(p ∧ q) ∨ (q′ ∧ r)',lambda p,q,r:int((p and q) or ((1-q) and r)),'Alt koldaki p anahtarını yazmamış.'),
]
for ad_,f_,_ in sec5[1:]: assert tara(f_,3)!=tara(dev,3),ad_
sira5=[sec5[1][0],sec5[2][0],sec5[3][0],sec5[4][0],sec5[0][0]]
q('0005',tipId='mns-denk',tip='Devrenin sade ifadesi',z='zor',alt='Devre Şemaları',kaz='Anahtarlı devrenin ifadesini yazıp sadeleştirerek denk olan ifadeyi bulur.',kalip='şekilli',
 kart='K-MNS-05 (devrenin denk ifadesi) · (p∧q)∨(p∧q′∧r)',
 metin='Şekildeki devrede aynı p anahtarı iki kolda da kullanılmıştır. Seri bağlı anahtarlar “ve”, paralel bağlı anahtarlar “veya” işlemine karşılık gelir; q′ yazılı anahtar, q önermesinin doğruluk değeri 0 iken kapalı, 1 iken açıktır. Bir anahtar kapalı iken karşılık gelen önermenin doğruluk değeri 1 kabul edilmektedir.\nBuna göre, A ile B arasında akımın geçmesi için gerek ve yeter koşulu gösteren aşağıdaki ifadelerden hangisi, devrenin ifadesine denktir?',
 dogru=sec5[0][0],yan=[(a,c,'dikkat') for a,_,c in sec5[1:]],sira=sira5,istenen='Devrenin ifadesine denk olan önerme.',
 ip=['Devrenin ifadesini iki kolu paralel yazarak elde et; seçenekleri doğruluk tablosu ya da çarpanlara ayırma ile karşılaştır.'],bilgi=[DEV,DEN],sekil=SK,
 ad=[A('Üst ve alt kol','Üst kol p ve q seri; alt kol p, q′, r seri.','(p ∧ q) ∨ (p ∧ q′ ∧ r)'),A('Ortak çarpan','p iki kolda ortaktır.','p ∧ (q ∨ (q′ ∧ r))'),A('Sadeleştir','q ∨ (q′ ∧ r) ifadesi q ∨ r’ye denktir (q = 1 ise 1; q = 0 ise r).','p ∧ (q ∨ r)'),A('Seçenekleri sına','Diğer seçenekler bir satırda farklı değer verir; örneğin p = 0, q = 0, r = 1 için (p ∧ q) ∨ r değeri 1’dir.','Doğru: p ∧ (q ∨ r)'),A('Sonuç','Denk ifade bulunur.','p ∧ (q ∨ r)')],
 puf='Ortak anahtarı dışarı al; kalan ifade iki anahtarın “veya”sına dönüşür.')

# ================= 06 kolay · karşıt / ters / karşıt ters kartları =================
KRT=[
 ('Hava yağmurlu değilse şemsiye açılmaz.',lambda p,q:imp(1-p,1-q)),       # I tersi
 ('Şemsiye açılmazsa hava yağmurlu değildir.',lambda p,q:imp(1-q,1-p)),    # II karşıt tersi
 ('Şemsiye açılırsa hava yağmurludur.',lambda p,q:imp(q,p)),               # III karşıtı
 ('Hava yağmurlu değildir ya da şemsiye açılır.',lambda p,q:int((not p) or q)), # IV
 ('Hava yağmurlu olup şemsiye açılmaz.',lambda p,q:int(p and not q)),      # V
]
kesin=[all(f(p,q) for p,q in itertools.product((1,0),repeat=2) if imp(p,q)) for _,f in KRT]
assert kesin==[False,True,False,True,False]
SK=tablo_svg(['Kart','Önerme'],[[r,t] for r,(t,_) in zip(['I','II','III','IV','V'],KRT)])
sira6=['Yalnız II','I ve III','II ve IV','I, II ve IV','II, IV ve V']
q('0006',tipId='mns-kart',tip='Koşullu önerme kartları',z='kolay',alt='Koşullu Önerme',kaz='Karşıt, ters ve karşıt ters önermeleri tanıyıp p ⇒ q doğru iken kesinlikle doğru olanları belirler.',kalip='öncüllü',
 kart='K-MNS-06 (karşıt, ters, karşıt ters kartları) · yağmur–şemsiye',
 metin='“Hava yağmurluysa şemsiye açılır.” önermesi doğrudur. Bu önerme ile ilgili olarak beş kartta yazan önermeler aşağıdaki tabloda verilmiştir.\nBuna göre, hangi kartlardaki önermelerin doğruluk değeri kesinlikle 1’dir?',
 dogru='II ve IV',yan=[('Yalnız II','IV. karttaki “ya da” önermesinin de p ⇒ q ile denk olduğunu görmemiş.','dikkat'),('I ve III','Tersini (I) ve karşıtını (III) p ⇒ q ile denk sanmış.','dikkat'),('II, IV ve V','V. kartın “ve” ile kurulu olduğunu, p ⇒ q doğruyken yanlış olduğunu fark etmemiş.','dikkat'),('I, II ve IV','I. kartı (tersi) denk sanmış.','dikkat')],
 sira=sira6,istenen='Doğruluk değeri kesinlikle 1 olan kartlar.',ip=['Cümleleri p : “Hava yağmurludur.”, q : “Şemsiye açılır.” ile yazıp her kartın hangi biçimde olduğunu belirle.'],bilgi=[KOŞ],sekil=SK,
 ad=[A('Önermeleri yaz','p : Hava yağmurludur; q : Şemsiye açılır.','Verilen önerme p ⇒ q'),A('Kartları çevir','I: p′ ⇒ q′ (tersi); II: q′ ⇒ p′ (karşıt tersi); III: q ⇒ p (karşıtı); IV: p′ ∨ q; V: p ∧ q′.','Kartlar sembolle yazıldı'),A('Denklikleri kontrol et','p ⇒ q ile karşıt tersi ve p′ ∨ q denktir; V ise p ⇒ q’nun olumsuzudur.','II ve IV denk'),A('Sonuç','Kesinlikle doğru olanlar seçilir.','II ve IV')],
 puf='p ⇒ q ile her durumda aynı değeri veren iki biçim vardır: karşıt tersi ve p′ ∨ q.')

bitir(P,'mantiksek',UK)
