"""TYT Biyoloji · Kalıtım · ek paket (kalitimiki): 34 soru, kardeş yok, ipucu 1.
Çaprazlama olasılıkları (Fraction), soy ağacı genotipleri (tüm olası dünyaların taranması), öncül doğruluğu ve çeldirici değerleri Python'da hesaplanır;
şekiller (soy ağacı, Punnett, kromozom, aglütinasyon, sütun grafiği, tablo) aynı verilerden üretilir.
Öncül/ifade doğruluğu betikte TEK yerde (durum sözlüğü) tanımlanır; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,random,itertools,re
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_bio as H
from _hafif_bio import *
from collections import Counter
KONU_='Kalıtım'; UK='bio|Kalıtım'
H.KONU=KONU_
P=Parti('kalitimiki',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 10. sınıf Kalıtım'
TIP={'temel':('by-kl2-temel','Temel kavramlar ve gametler'),
     'capraz':('by-kl2-capraz','Monohibrit ve dihibrit çaprazlama'),
     'baskin':('by-kl2-baskinlik','Baskınlık türleri ve kontrol çaprazlaması'),
     'abo':('by-kl2-abo','Çok alellilik: ABO ve Rh'),
     'eseye':('by-kl2-eseye','Eşeye bağlı kalıtım'),
     'soy':('by-kl2-soyagaci','Soy ağacı analizi'),
     'mut':('by-kl2-mutasyon','Mutasyon, modifikasyon ve varyasyon')}
def q(no,tk,z,alt,kaz,kalip,ne,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1
    tipId,tipad=TIP[tk]; kid=f'K-BYKL2-{no[-2:]}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tipad,KY)
    mk(P,no,ad=ad,adim=len(ad),tipId=tipId,tip=tipad,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'{kid} ({tipad.lower()}) · {ne}',**k)
def sf(x):
    x=Fr(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def frs(dogru,yan):
    """kesir şıkları: değerler Fraction; küçükten büyüğe sıralı metin listesi döndürür"""
    v=[Fr(dogru)]+[Fr(y[0]) for y in yan]; assert len(set(v))==5,v
    return dict(dogru=sf(dogru),yan=[(sf(y[0]),)+tuple(y[1:]) for y in yan],sira=[sf(x) for x in sorted(v)])
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)),sira; return sira
def adlar(s): return ('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
def onc(durum,secenekler,fazla='{x}. öncülü doğru sanmış; oysa yanlıştır: {n}',eksik='{x}. öncülü yanlış sanmış; oysa doğrudur: {n}'):
    """durum {'I':(bool,neden)}: bool = öncül, doğru şık kümesinde mi; secenekler: 5 etiket demeti; tam biri doğru kümeye eşit olmalı."""
    T=frozenset(k for k,v in durum.items() if v[0]); ops=[tuple(s) for s in secenekler]
    assert len(ops)==5 and len(set(ops))==5 and sum(frozenset(o)==T for o in ops)==1,(T,ops)
    yan=[]
    for o in ops:
        W=frozenset(o)
        if W==T: continue
        p=[fazla.format(x=x,n=durum[x][1]) for x in sorted(W-T)]+[eksik.format(x=x,n=durum[x][1]) for x in sorted(T-W)]
        yan.append((adlar(o),' '.join(p),'bilgi'))
    return dict(dogru=adlar([k for k in durum if durum[k][0]]),yan=yan,sira=[adlar(o) for o in ops])
def oncad(durum,ad='{k}. öncülü değerlendir',ev='doğru',hay='yanlış'):
    return [A(ad.format(k=k),v[1],ev if v[0] else hay) for k,v in durum.items()]
def tek(secenekler,hedef=True):
    """[(metin,bool,neden)] 5 adet; hedef=True tek doğru ifade, False tek yanlış ifade."""
    assert len(secenekler)==5; h=[s for s in secenekler if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    yan=[]
    for m,b,n in secenekler:
        if b==hedef: continue
        yan.append((m,(f'Bu ifadeyi doğru sanmış; oysa yanlıştır: {n}' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}'),'bilgi'))
    return dict(dogru=h[0][0],yan=yan,sira=[s[0] for s in secenekler])
def duz(durum): return ' · '.join(f'{k}: '+('doğru' if v[0] else 'yanlış') for k,v in durum.items())
def metin_onc(giris,onc_,kok):
    return giris+'\n'+'\n'.join(f'{k}. {v}' for k,v in onc_.items())+'\n'+kok
# ---------------- genetik yardımcıları ----------------
def gam(g): return [''.join(x) for x in itertools.product(*[g[i:i+2] for i in range(0,len(g),2)])]
def cross(g1,g2):
    c=Counter()
    for a in gam(g1):
        for b in gam(g2): c[''.join(''.join(sorted(a[i]+b[i])) for i in range(len(a)))]+=1
    return c
def pr(c,f): return Fr(sum(v for g,v in c.items() if f(g)),sum(c.values()))
def dm(g,i): return g[2*i].isupper() or g[2*i+1].isupper()      # i. gen çiftinde baskın fenotip
def abo_c(p1,p2):
    c=Counter()
    for a in p1:
        for b in p2:
            s={a,b}; c['AB' if s=={'A','B'} else 'A' if 'A' in s else 'B' if 'B' in s else 'O']+=1
    return c
def grup(g): s=set(g); return 'AB' if s=={'A','B'} else 'A' if 'A' in s else 'B' if 'B' in s else 'O'
# ---------------- bilgi kutuları (örnekler sorulardan bağımsız) ----------------
B_KAV=B('Temel kavramlar','Alel: aynı genin farklı biçimi · Genotip: alel bileşimi, fenotip: gözlenen özellik · Homozigot: iki alel aynı (ör. TT, tt), heterozigot: iki alel farklı (ör. Tt) · Baskın alel heterozigotta da kendini gösterir, çekinik alel yalnız homozigotta görünür')
B_GAM=B('Gamet çeşidi','Her heterozigot gen çifti 2 çeşit alel verir, homozigot çift 1 çeşit · Gamet çeşidi sayısı = 2 üzeri heterozigot çift sayısı (genler bağımsız ayrılıyorsa) · Örnek: PpQq → 2 × 2 = 4 çeşit')
B_CAP=B('Çaprazlama ve Punnett karesi','Önce ebeveynlerin gametlerini yaz, sonra Punnett karesinin kenarlarına yerleştir; kutular eşit olasılıklıdır · Bağımsız iki özellikte olasılıklar çarpılır')
B_KOS=B('Koşullu olasılık','“…olanlar arasından seçilen birey” ifadesinde payda koşulu sağlayan yavruların sayısıdır, tüm yavruların sayısı değil · Olasılık = istenen kutular ÷ koşulu sağlayan kutular')
B_EKS=B('Baskınlık türleri','Heterozigot bireyde alellerin nasıl ifade edildiğine göre tam baskınlık, eksik baskınlık ve eş baskınlık ayırt edilir')
B_TEST=B('Genotip araştırma','Baskın fenotipli bir bireyin genotipi, bu bireyi çekinik homozigotla çaprazlayıp yavrulara bakarak araştırılır')
B_ABO=B('ABO kan grupları','A grubu: AA ya da AO · B grubu: BB ya da BO · AB grubu: AB · O grubu: OO · A ve B aleli O’ya baskın, birbirine eş baskındır · Rh+ baskın (R), Rh− çekinik (r): Rh+ birey RR ya da Rr, Rh− birey rr')
B_ESE=B('Eşeye bağlı kalıtım','Kadın XX, erkek XY · Renk körlüğü ve hemofili gibi özellikler X kromozomu üzerindeki alellerle kalıtılır')
B_SOY=B('Soy ağacı simgeleri','Kare erkek, daire kadın; içi dolu semboller özelliği gösteren bireyleri belirtir · Kalıtım biçimi, ebeveyn–çocuk ilişkilerinden çıkarılır')
B_MUT=B('Mutasyon ve modifikasyon','Mutasyon: DNA’daki kalıcı değişiklik · Modifikasyon: çevre etkisiyle oluşan fenotip değişimi')
# ---------------- TikZ yardımcıları ----------------
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
def soy_cizim(kisi,XY,cift,ybar,R=.28,gen=None,olcek=.95,etiket=True):
    """kisi {ad:(cins,hasta,anne,baba)}; XY {ad:(x,y)}; cift [(a,b)] evlilikler; ybar {(a,b):y} kardeş çubuğu yüksekliği."""
    b=[]
    for a,(x,y) in XY.items():
        s,h=kisi[a][0],kisi[a][1]; fl='fill=black' if h else ''
        b.append(f'\\draw[line width=1pt,{fl}] ({x-R:.2f},{y-R:.2f}) rectangle ({x+R:.2f},{y+R:.2f});' if s=='E' else f'\\draw[line width=1pt,{fl}] ({x:.2f},{y:.2f}) circle ({R});')
        if etiket: b.append(f'\\node[font=\\footnotesize] at ({x:.2f},{y-.55:.2f}) {{{a.split("-")[1]}}};')
    for (a,c) in cift:
        (x1,y1),(x2,y2)=XY[a],XY[c]; assert y1==y2 and x1<x2
        b.append(f'\\draw[line width=1pt] ({x1+R:.2f},{y1:.2f})--({x2-R:.2f},{y2:.2f});')
        ch=[n for n,v in kisi.items() if {v[2],v[3]}=={a,c}]
        if not ch: continue
        m=(x1+x2)/2; yb=ybar[(a,c)]; xs=[XY[n][0] for n in ch]; yc=XY[ch[0]][1]
        b.append(f'\\draw[line width=1pt] ({m:.2f},{y1:.2f})--({m:.2f},{yb:.2f});')
        b.append(f'\\draw[line width=1pt] ({min(xs+[m]):.2f},{yb:.2f})--({max(xs+[m]):.2f},{yb:.2f});')
        for x in xs: b.append(f'\\draw[line width=1pt] ({x:.2f},{yb:.2f})--({x:.2f},{yc+R:.2f});')
    if gen:
        for r,y in gen.items(): b.append(f'\\node[font=\\normalsize\\bfseries] at ({min(x for x,_ in XY.values())-1.0:.2f},{y:.2f}) {{{r}}};')
    return tk('\n'.join(b),olcek)
def punnett(ust,yan,hucre=None,ustbas='',yanbas='',olcek=1.0,w=1.5,h=.95,sol=1.0):
    """ust: üst kenardaki gametler, yan: sol kenardaki gametler; hucre(i,j)->metin ya da None. Kutular eşit olasılıklıdır."""
    b=[]; nx,ny=len(ust),len(yan)
    for j,g in enumerate(ust): b.append(f'\\node[font=\\normalsize\\bfseries] at ({(j+.5)*w:.2f},.42) {{{g}}};')
    for i,g in enumerate(yan): b.append(f'\\node[font=\\normalsize\\bfseries] at ({-sol/2:.2f},{-(i+.5)*h:.2f}) {{{g}}};')
    b.append(f'\\draw[line width=1.3pt] (0,0) rectangle ({nx*w:.2f},{-ny*h:.2f});')
    for j in range(1,nx): b.append(f'\\draw[line width=.8pt] ({j*w:.2f},0)--({j*w:.2f},{-ny*h:.2f});')
    for i in range(1,ny): b.append(f'\\draw[line width=.8pt] (0,{-i*h:.2f})--({nx*w:.2f},{-i*h:.2f});')
    b.append(f'\\draw[line width=.8pt] (-{sol:.2f},0)--(0,0);\\draw[line width=.8pt] (0,0)--(0,.85);')
    if hucre:
        for i in range(ny):
            for j in range(nx):
                t=hucre(i,j)
                if t: b.append(f'\\node[font=\\normalsize] at ({(j+.5)*w:.2f},{-(i+.5)*h:.2f}) {{{t}}};')
    if ustbas: b.append(f'\\node[font=\\small] at ({nx*w/2:.2f},1.05) {{{ustbas}}};')
    if yanbas: b.append(f'\\node[font=\\small,rotate=90] at ({-sol-.35:.2f},{-ny*h/2:.2f}) {{{yanbas}}};')
    return tk('\n'.join(b),olcek)
def kromozom_cifti(x,y0,L,etk_sol,etk_sag,pos=.55,gen=0.0,renk=''):
    """iki homolog kromozom (çubuk) ve aynı gen yerinde alel harfleri; y0 alt uç"""
    b=[]
    for dx,e,yan in ((0,etk_sol,-1),(.62,etk_sag,1)):
        xx=x+dx
        b.append(f'\\draw[line width=1.1pt,rounded corners=4pt,fill=black,fill opacity=.10] ({xx:.2f},{y0:.2f}) rectangle ({xx+.3:.2f},{y0+L:.2f});')
        b.append(f'\\draw[line width=1.1pt,rounded corners=4pt] ({xx:.2f},{y0:.2f}) rectangle ({xx+.3:.2f},{y0+L:.2f});')
        b.append(f'\\draw[line width=1.6pt] ({xx-.03:.2f},{y0+L*.62:.2f})--({xx+.33:.2f},{y0+L*.62:.2f});')   # sentromer
        yy=y0+L*pos
        xs,xe=(xx-.02,xx-.2) if yan<0 else (xx+.32,xx+.5)
        b.append(f'\\draw[line width=1.6pt] ({xs:.2f},{yy:.2f})--({xe:.2f},{yy:.2f});')
        b.append(f'\\node[font=\\large\\bfseries] at ({(xx-.43) if yan<0 else (xx+.76):.2f},{yy:.2f}) {{{e}}};')
    return '\n'.join(b)

# ===================== 0001 · temel · kolay · tablo + öncüllü =====================
G1={'K1':'KK','K2':'Kk','K3':'kk','K4':'Kk'}
sk1=[]
for _i,(_k,_g) in enumerate(G1.items()):
    sk1.append(kromozom_cifti(_i*2.3,0,1.7,_g[0],_g[1],.3)); sk1.append(f'\\node[font=\\normalsize\\bfseries] at ({_i*2.3+.46:.2f},-.5) {{{_k}}};')
SK1=tk('\n'.join(sk1),1.25)
fen=lambda g:'kısa' if 'K' in g else 'uzun'
D1={'I':(fen(G1['K1'])==fen(G1['K2']) and G1['K1']!=G1['K2'],'KK ve Kk genotipli bireylerin ikisi de baskın alel taşıdığı için kısa tüylüdür; genotipleri ise farklıdır.'),
    'II':(len(set(gam(G1['K3'])))==1,'kk homozigot olduğundan yalnız k aleli taşıyan gametler oluşturur.'),
    'III':(fen(G1['K4'])==fen(G1['K3']),'K4 (Kk) kısa tüylü, K3 (kk) uzun tüylüdür; fenotipleri farklıdır.')}
assert [v[0] for v in D1.values()]==[True,True,False]
q('0001','temel','kolay','Genotip ve fenotip','Verilen genotiplerden fenotipi, homozigot–heterozigot ayrımını ve gamet çeşidini yorumlar.','şekilli',
 'şekildeki genotiplerden fenotip ve gamet yorumu','Genotip şemasında baskın alelin varlığı fenotipi, alellerin aynı olup olmaması gamet çeşidini belirler.','Aynı fenotipli bireylerin aynı genotipte olduğunu sanmak.',
 [A('Genotipleri çöz','K1 homozigot baskın, K2 ve K4 heterozigot, K3 homozigot çekiniktir.','KK, Kk, kk, Kk')]+oncad(D1)+[A('Sonuç','Doğru olan öncüller belirlenir.',', '.join(k for k in D1 if D1[k][0]))],
 metin=metin_onc('Kobaylarda kısa tüy (K), uzun tüy (k) üzerine tam baskındır. Şekilde dört kobayın (K1, K2, K3, K4) tüy uzunluğunu belirleyen gen yerinin bulunduğu homolog kromozom çiftleri ve üzerindeki aleller gösterilmiştir.\nBuna göre bu bireylerle ilgili',
   {'I':'K1 ile K2 aynı fenotipe, farklı genotipe sahiptir.','II':'K3 yalnız bir çeşit gamet oluşturur.','III':'K4 ile K3 aynı fenotipe sahiptir.'},'ifadelerinden hangileri doğrudur?'),
 sekil=SK1,
 istenen='Doğru olan ifadeler.',ip=['Önce her genotipin fenotipini yaz, sonra homozigot ve heterozigot bireylerin gamet çeşidini düşün.'],bilgi=[B_KAV,B_GAM],
 puf='Baskın alel taşıyan her birey baskın fenotiplidir; gamet çeşidi yalnız heterozigot çift sayısına bağlıdır.',
 **onc(D1,[('I',),('II',),('III',),('I','II'),('I','III')]))

# ===================== 0002 · temel · kolay · düz =====================
S2=[('Tam baskınlıkta heterozigot birey, baskın homozigot bireyle aynı fenotipi gösterir.',True,'tam baskınlıkta heterozigot birey baskın alelin fenotipini gösterir.'),
    ('Genotipi Aa olan birey, A ve a alelleri bakımından homozigottur.',False,'iki aleli farklı olan birey heterozigottur.'),
    ('Aynı genin farklı biçimleri (alelleri), homolog kromozomların farklı gen yerlerinde bulunur.',False,'aleller homolog kromozomların aynı gen yerinde bulunur.'),
    ('Homozigot bir birey, ilgili gen bakımından iki çeşit gamet oluşturur.',False,'homozigot birey tek çeşit gamet oluşturur.'),
    ('Fenotip, yalnızca genotipe bağlıdır ve çevre koşullarından hiçbir biçimde etkilenmez.',False,'fenotip genotip ile çevrenin birlikte etkisiyle oluşur.')]
q('0002','temel','kolay','Temel kavramlar','Alel, genotip, fenotip, homozigot ve heterozigot kavramlarını doğru kullanır.','düz',
 'temel kavram ifadelerinden doğru olanı bulma','Temel kavramların tanımları ve tam baskınlıkta heterozigotun fenotipi.','Heterozigot bireyin fenotipinin baskın homozigottan farklı olduğunu sanmak.',
 [A('İfadeleri tek tek oku','Her ifadeyi alel, genotip ve fenotip tanımlarıyla karşılaştır.','5 ifade'),A('Tanımlarla sına','Heterozigot, alel, gamet ve fenotip ifadeleri tanımlara uymuyor.','4 ifade yanlış'),A('Tam baskınlığı hatırla','Heterozigot birey baskın alelin fenotipini gösterir; baskın homozigotla aynıdır.','Kk ve KK aynı fenotip'),A('Sonuç','Tanımlara uyan tek ifade tam baskınlık ifadesidir.','Doğru: heterozigot = baskın homozigot fenotipi')],
 metin='Kalıtımın temel kavramları işlenirken alel, genotip, fenotip ve gamet ile ilgili beş ifade verilmiş ve bu ifadelerin yalnızca birinin bilimsel olarak doğru olduğu belirtilmiştir.\nBuna göre aşağıdaki ifadelerden hangisi doğrudur?',
 istenen='Doğru olan ifade.',ip=['Tam baskınlığın tanımını heterozigot genotip üzerinden hatırla.'],bilgi=[B_KAV],
 puf='Tam baskınlıkta heterozigot ile baskın homozigot aynı fenotipi gösterir.',
 **tek([S2[0],S2[1],S2[2],S2[3],S2[4]],hedef=True))

# ===================== 0003 · temel · orta · kromozom şekli · olumsuz =====================
GEN3='AaBbDD'
G3=sorted(set(gam(GEN3))); assert G3==['ABD','AbD','aBD','abD']
sk3=kromozom_cifti(0,0,3.2,'A','a',.84)+'\n'+kromozom_cifti(3.1,.35,2.5,'B','b',.25)+'\n'+kromozom_cifti(6.2,.7,1.9,'D','D',.3)
SK3=tk(sk3,1.3)
yan3=[('ABD','A, B ve D alellerinden birer tanesini taşır; oluşabilir.','bilgi'),('AbD','Her gen çiftinden bir alel içerir; oluşabilir.','bilgi'),('aBD','Her gen çiftinden bir alel içerir; oluşabilir.','bilgi'),('abD','Her gen çiftinden bir alel içerir; oluşabilir.','bilgi')]
yan3=[(a,'Bu gameti oluşamaz sanmış; oysa her gen çiftinden birer alel içerir ve D çiftinin her iki aleli D olduğundan oluşabilir.','bilgi') for a,_,_ in yan3]
assert 'aBd' not in G3
q('0003','temel','orta','Gametler','Homolog kromozom çiftleri üzerindeki alellerden oluşabilecek gametleri belirler.','şekilli',
 'şekildeki kromozomlardan oluşamayacak gamet','Genotip kromozom şemasından okunur; gamet her gen çiftinden birer alel taşır.','Homozigot gen çiftinden bireyde bulunmayan aleli gamette göstermek.',
 [A('Genotipi oku','Üç homolog çiftte aleller Aa, Bb ve DD olarak görülür.','AaBbDD'),A('Gen çiftlerini ayır','Aa ve Bb heterozigot, DD homozigottur; her gamet her çiftten bir alel alır.','2 × 2 × 1 = 4 çeşit'),A('Gametleri yaz','Bağımsız ayrılma ve krossing-over olmaması varsayımıyla dört gamet oluşur.','ABD, AbD, aBD, abD'),A('Şıkları ele','D çiftinin iki aleli de D olduğundan d içeren gamet oluşamaz.','Oluşamayan: d aleli içeren')],
 metin='Şekilde, bir bireyin vücut hücresindeki üç çift homolog kromozom ve bu kromozomlar üzerinde bulunan üç gen yerindeki aleller gösterilmiştir. Gen çiftleri bağımsız ayrılmakta ve krossing-over gerçekleşmemektedir.\nBu bireyin mayoz bölünme sonunda oluşturduğu gametlerden biri aşağıdakilerden hangisi olamaz?',
 sekil=SK3,istenen='Oluşamayan gamet.',ip=['Gametin her gen çiftinden kaç alel taşıdığını düşün.'],bilgi=[B_GAM,B_KAV],
 puf='Gamet, bireyde bulunan alellerden her çiftten birini taşır; bireyde olmayan alel gamette de olmaz.',
 dogru='aBd',yan=yan3,sira=yer('A','aBd',['ABD','AbD','aBD','abD']))

# ===================== 0004 · temel · orta · öncüllü =====================
c4=cross('AaBbCc','AaBbCc')
assert len(set(gam('AaBbCc')))==8 and len(c4)==27 and len({tuple(dm(g,i) for i in range(3)) for g in c4})==8
D4={'I':(len(set(gam('AaBbCc')))==8,'Üç heterozigot çifti olan birey 2 × 2 × 2 = 8 çeşit gamet oluşturur.'),
    'II':(len(c4)==27,'Her gen çifti AA, Aa, aa olmak üzere 3 genotip verir; 3 × 3 × 3 = 27 farklı genotip oluşur.'),
    'III':(len({tuple(dm(g,i) for i in range(3)) for g in c4})==8,'Her özellik için baskın ve çekinik olmak üzere 2 fenotip vardır; 2 × 2 × 2 = 8 farklı fenotip oluşur.')}
assert [v[0] for v in D4.values()]==[True,True,True]
q('0004','temel','orta','Gamet ve döl çeşitleri','Çok gen çiftli çaprazlamada gamet, genotip ve fenotip çeşidi sayılarını belirler.','öncüllü',
 'AaBbCc × AaBbCc çeşit sayıları','Her bağımsız gen çiftinin çeşit sayıları çarpılır: gamet 2, genotip 3, fenotip 2.','Genotip çeşidini 2 üzeri n, ya da gamet çeşidini 4 saymak.',
 [A('Gamet çeşidini bul','Her heterozigot çift 2 çeşit alel verir.','2 × 2 × 2 = 8')]+oncad(D4)+[A('Sonuç','Doğru öncüller seçilir.',', '.join(k for k in D4 if D4[k][0]))],
 metin=metin_onc('Üç gen çifti birbirinden bağımsız ayrılan ve her birinde baskın alelin çekinik aleli tam olarak baskıladığı bir canlı türünde, AaBbCc genotipli iki birey çaprazlanıyor. Krossing-over ve mutasyon gerçekleşmemiştir.\nBuna göre bu çaprazlamayla ilgili',
   {'I':'Her bireyin oluşturabileceği farklı gamet çeşidi sayısı 8’dir.','II':'Yavrularda 27 farklı genotip görülebilir.','III':'Yavrularda 8 farklı fenotip görülebilir.'},'ifadelerinden hangileri doğrudur?'),
 istenen='Doğru olan ifadeler.',ip=['Her gen çiftinin kaç genotip ve kaç fenotip verdiğini ayrı ayrı bul, sonra çarp.'],bilgi=[B_GAM,B_CAP],
 puf='Bağımsız gen çiftlerinde çeşit sayıları çarpılır: tek çiftte gamet 2, genotip 3, fenotip 2.',
 **onc(D4,[('I',),('II',),('I','II'),('II','III'),('I','II','III')]))

# ===================== 0005 · temel · kolay · hikâyeli =====================
F2=1200; sf_=Fr(F2)*cross('Uu','Uu')['UU']/4; assert sf_==300
assert Fr(F2)*Fr(3,4)==900 and Fr(F2)*cross('Uu','Uu')['Uu']/4==600
q('0005','temel','kolay','Mendel çaprazlamaları','Mendel’in monohibrit çaprazlamasında F2 genotip sayılarını hesaplar.','hikâyeli',
 'F2 döl sayıları (saf döl uzun)','F1 heterozigotların kendilenmesinden F2’de UU : Uu : uu = 1 : 2 : 1 oranı çıkar; saf döl = homozigot.','Uzun bitkilerin tümünü saf döl saymak; oranı toplam uzun sayısına uygulamak.',
 [A('F1 genotipini bul','Saf döl UU ile uu çaprazlanınca F1 bitkilerinin hepsi Uu olur.','UU × uu → Uu'),A('F2 oranını yaz','Uu × Uu çaprazlamasında UU : Uu : uu oranı 1 : 2 : 1’dir.','1 : 2 : 1'),A('İstenen grubu seç','Uzun gövdeli saf döl bitkiler yalnız UU genotipli olanlardır.','UU: 1/4'),A('Sayıyı hesapla','Toplam bitki sayısı bu oranla çarpılır.','1200 × 1/4 = 300')],
 metin='Bir öğrenci, Mendel’in deneylerine benzer bir çalışma yapıyor. Saf döl uzun gövdeli (UU) ile saf döl bodur gövdeli (uu) bezelyeleri çaprazlayarak F1 bitkilerini elde ediyor, sonra F1 bitkilerini kendi aralarında çaprazlayıp 1200 bitkilik F2 dölünü yetiştiriyor.\nBuna göre F2 dölünde uzun gövdeli ve saf döl olan bitki sayısı kaçtır?',
 istenen='F2’de uzun gövdeli saf döl bitkilerin sayısı.',ip=['F1 bitkilerinin genotipini bul; saf döl ifadesinin hangi genotip demek olduğunu düşün.'],bilgi=[B_KAV,B('Oran uygulama','Bir oran, toplam sayıya uygulanarak sınıf sayısı bulunur · Örnek: 80 yavrunun 1/4’ü 20 yavrudur')],
 puf='Saf döl = homozigot; Aa × Aa çaprazında homozigot baskın oranı 1/4’tür.',
 dogru=300,yan=[(400,'UU, Uu ve uu sınıflarını eşit sayıp 1200’ü 3’e bölmüş.','bilgi'),(450,'900 uzun bitkinin yarısını saf döl saymış.','bilgi'),(600,'Heterozigot (Uu) bitkilerin sayısını bulmuş.','dikkat'),(900,'Uzun gövdeli tüm bitkileri saf döl saymış.','bilgi')])

# ===================== 0006 · çaprazlama · orta · Punnett · olumsuz =====================
c6=cross('Rr','Rr'); kutu6={'I':'RR','II':'Rr','III':'Rr','IV':'rr'}
assert Counter(kutu6.values())==Counter({'RR':1,'Rr':2,'rr':1}) and sorted(kutu6.values())==sorted(c6.elements())
fe6=lambda g:'yuvarlak' if 'R' in g else 'buruşuk'
S6=[('I ve IV numaralı kutulardaki bireyler homozigottur.',kutu6['I'][0]==kutu6['I'][1] and kutu6['IV'][0]==kutu6['IV'][1],'RR ve rr homozigot genotiplerdir.'),
    ('II ve III numaralı kutulardaki bireylerin genotipleri aynıdır.',kutu6['II']==kutu6['III'],'ikisi de Rr’dir.'),
    ('Yalnız IV numaralı kutudaki birey buruşuk tohumludur.',[k for k,g in kutu6.items() if fe6(g)=='buruşuk']==['IV'],'buruşuk tohum yalnız rr genotipinde görülür.'),
    ('I numaralı kutudaki birey ile IV numaralı kutudaki birey aynı fenotiptedir.',fe6(kutu6['I'])==fe6(kutu6['IV']),'RR yuvarlak, rr buruşuk tohumludur; fenotipleri farklıdır.'),
    ('Kutulardaki bireylerin üçü yuvarlak tohumludur.',sum(fe6(g)=='yuvarlak' for g in kutu6.values())==3,'RR, Rr ve Rr genotipli üç birey yuvarlaktır.')]
SK6=punnett(['R','r'],['R','r'],lambda i,j:['I','II','III','IV'][2*i+j],ustbas='1. birey',yanbas='2. birey',w=1.4,h=.95,olcek=1.5)
q('0006','capraz','orta','Punnett karesi','Punnett karesindeki kutuların genotip ve fenotiplerini yorumlar.','şekilli',
 'Punnett karesinde numaralı kutular','Ebeveyn gametlerinden Punnett karesi doldurulur; kutuların genotip ve fenotipi okunur.','Genotip ayrı, fenotip ayrı olduğunu karıştırmak.',
 [A('Ebeveynleri bul','Her iki kenarda R ve r gametleri vardır; ebeveynler heterozigottur.','Rr × Rr'),A('Kutuları doldur','Gametler birleştirilir: I, II, III ve IV numaralı kutular sırasıyla doldurulur.','RR, Rr, Rr, rr'),A('Fenotipleri yaz','R taşıyan bireyler yuvarlak, rr buruşuktur.','Yuvarlak: I, II, III · Buruşuk: IV'),A('İfadeleri sına','Dört ifade kutulara uyar; I ve IV’ün fenotipi aynı değildir.','Yanlış ifade: fenotipleri aynı')],
 metin='Şekilde, yuvarlak (R) ve buruşuk (r) tohum şekli alelleri taşıyan iki bezelye bitkisinin çaprazlanmasına ait gamet tablosu verilmiştir. Kutular yavru bitkileri göstermekte ve her kutu eşit olasılıklıdır.\nBuna göre numaralı kutulardaki yavrularla ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK6,istenen='Yanlış olan ifade.',ip=['Önce her kutudaki genotipi yaz, sonra fenotipe geç.'],bilgi=[B_CAP,B_KAV],
 puf='Punnett karesinde önce genotipleri, sonra fenotipleri yaz; homozigot baskın ile homozigot çekinik fenotipleri farklıdır.',
 **tek([S6[i] for i in (3,0,1,2,4)],hedef=False))

# ===================== 0007 · çaprazlama · orta · hikâyeli · binom =====================
pb=Fr(1,4); pbs=Fr(3,4); assert pr(cross('Bb','Bb'),lambda g:g=='bb')==pb
d7=3*pb**2*pbs; assert d7==Fr(9,64)
t7=[(Fr(3,64),'Yalnızca belirli bir doğum sırasını (boynuzsuz, boynuzlu, boynuzlu) hesaplamış; üç farklı sırayı saymamış.','islem'),(Fr(27,64),'Boynuzlu ve boynuzsuz buzağı sayılarının olasılıklarını ters kullanmış (iki boynuzsuz, bir boynuzlu).','dikkat'),(Fr(3,16),'Üç buzağı yerine yalnızca iki buzağının olasılığını (3/4 × 1/4) hesaplamış.','islem'),(Fr(1,64),'Üç buzağının da boynuzlu olma olasılığını hesaplamış.','dikkat')]
assert Fr(3,16)==pbs*pb and Fr(1,64)==pb**3 and Fr(3,64)==pbs*pb**2 and Fr(27,64)==3*pb*pbs**2
q('0007','capraz','orta','Monohibrit çaprazlama','Ardışık doğumlarda olasılıkları çarparak ve sıralamaları sayarak hesaplar.','hikâyeli',
 'üç buzağıdan ikisi boynuzlu','Aa × Aa çaprazında çekinik olasılığı 1/4 ve baskın 3/4; ardışık bağımsız olaylar çarpılır, farklı sıralar toplanır.','Sıralamaları saymamak.',
 [A('Genotipleri yaz','Heterozigot boynuzsuz iki sığır Bb × Bb çaprazlanıyor.','Bb × Bb'),A('Tek buzağı olasılıkları','Boynuzlu (bb) olasılığı 1/4, boynuzsuz (B_) olasılığı 3/4’tür.','1/4 ve 3/4'),A('Bir sıralamayı hesapla','İki boynuzlu ve bir boynuzsuz buzağı belirli bir sırada doğarsa olasılık çarpılır.','1/4 × 1/4 × 3/4 = 3/64'),A('Sıralamaları say','Boynuzsuz buzağı üç farklı sırada doğabilir.','3 × 3/64 = 9/64')],
 metin='Sığırlarda boynuzsuzluk (B), boynuzluluk (b) üzerine tam baskındır. Heterozigot boynuzsuz bir inek ile heterozigot boynuzsuz bir boğa çiftleştiriliyor ve bu çiftleşmeden art arda üç buzağı doğuyor. Her doğumda tek buzağı doğmuştur ve buzağıların doğum sırası ile cinsiyeti önemsenmemektedir.\nBuna göre bu üç buzağıdan ikisinin boynuzlu, birinin boynuzsuz olma olasılığı kaçtır?',
 istenen='İki boynuzlu ve bir boynuzsuz buzağı olma olasılığı.',ip=['Tek bir buzağı için iki fenotipin olasılığını bul; sonra boynuzsuz buzağının kaçıncı sırada doğabileceğini say.'],bilgi=[B_CAP],
 puf='Ardışık bağımsız olayların olasılığı çarpılır; sıralama önemli değilse farklı sıralar da toplanır.',
 **frs(d7,t7))

# ===================== 0008 · çaprazlama · orta · tablo · öncüllü =====================
N8=[('Siyah, kısa',91),('Siyah, uzun',29),('Kahverengi, kısa',31),('Kahverengi, uzun',9)]; assert sum(n for _,n in N8)==160
c8=cross('BbDd','BbDd'); assert pr(c8,lambda g:not dm(g,0) and not dm(g,1))==Fr(1,16) and Fr(160,16)==10
_g8=[a+b+c+d for a in('BB','Bb') for b in ('',) for c in('DD','Dd') for d in ('',)]
_ok8=[(x,y) for x in _g8 for y in _g8 if 'bbdd' in cross(x,y)]
assert _ok8==[('BbDd','BbDd')],_ok8
D8={'I':(True,'Kahverengi ve uzun tüylü yavrular doğduğuna göre siyah ve kısa tüylü ebeveynlerin ikisi de b ve d alellerini taşır; hepsi BbDd’dir.'),
    'II':(False,'Siyah, uzun tüylü yavrular B_dd genotiplidir; BBdd ve Bbdd olabilir, hepsi homozigot değildir.'),
    'III':(True,'BbDd × BbDd çaprazında bbdd yavruların 1/16’sıdır.')}
q('0008','capraz','orta','Dihibrit çaprazlama','Yavru sayılarından ebeveyn genotiplerini çıkarır ve beklenen oranı yorumlar.','tablo',
 'tablodan dihibrit ebeveyn genotipi','Çekinik fenotipli yavru doğması iki ebeveynin de çekinik alel taşıdığını gösterir; 9 : 3 : 3 : 1 oranı dihibrit çaprazlamayı gösterir.','Siyah, uzun tüylü yavruların tümünü homozigot sanmak.',
 [A('Çekinik yavrulara bak','Ebeveynler baskın fenotipli iken kahverengi ve uzun yavrular çıkmıştır.','Her ebeveyn b ve d taşır'),A('Ebeveyn genotipini bul','Her iki ebeveyn de iki gen çiftinde heterozigottur.','BbDd × BbDd')]+oncad(D8)+[A('Sonuç','Doğru öncüller seçilir.',', '.join(k for k in D8 if D8[k][0]))],
 metin=metin_onc('Kobaylarda tüy rengi ve tüy uzunluğunu belirleyen genler bağımsız ayrılmaktadır. Siyah ve kısa tüylü iki kobay çaprazlanıyor; elde edilen 160 yavrunun fenotip dağılımı tabloda verilmiştir.\nBuna göre,',
   {'I':'Ebeveynlerin ikisi de iki özellik bakımından heterozigottur.','II':'Siyah, uzun tüylü yavrular iki özellik bakımından da homozigottur.','III':'Beklenen orana göre kahverengi ve uzun tüylü yavrular tüm yavruların 1/16’sini oluşturur.'},'ifadelerinden hangileri doğrudur?'),
 sekil=tablo_svg(['Fenotip','Yavru sayısı'],[[a,str(n)] for a,n in N8]),
 istenen='Doğru olan ifadeler.',ip=['Ebeveynlerin fenotipi baskın iken hangi yavruların doğduğuna bak; bu, ebeveyn genotipini gösterir.'],bilgi=[B_CAP,B_KAV],
 puf='Baskın fenotipli ebeveynlerden çekinik yavru çıkıyorsa ebeveynlerin ikisi de çekinik alel taşır.',
 **onc(D8,[('I',),('II',),('III',),('I','II'),('I','III')]))

# ===================== 0009 · çaprazlama · orta · Punnett (2×4) =====================
p1,p2='RrYy','Rryy'
assert sorted(set(gam(p1)))==sorted(['RY','Ry','rY','ry']) and sorted(set(gam(p2)))==sorted(['Ry','ry'])
c9=cross(p1,p2); d9=pr(c9,lambda g:dm(g,0) and dm(g,1)); assert d9==Fr(3,8)
assert pr(c9,lambda g:dm(g,0))==Fr(3,4) and pr(c9,lambda g:dm(g,1))==Fr(1,2)
SK9=punnett(['RY','Ry','rY','ry'],['Ry','ry'],None,ustbas='1. bireyin gametleri',yanbas='2. bireyin gametleri',w=1.35,h=.95,olcek=1.35)
t9=[(Fr(3,16),'Tabloyu 16 kutu sanıp uygun 3 kutuyu 3/16 olarak yazmış.','islem'),(Fr(1,2),'Yalnız Y özelliğinin baskın olma olasılığını (1/2) vermiş.','dikkat'),(Fr(9,16),'İki ebeveyni de RrYy sanıp 9 : 3 : 3 : 1 oranındaki 9/16 değerini vermiş.','bilgi'),(Fr(3,4),'Yalnız R özelliğinin baskın olma olasılığını (3/4) vermiş.','dikkat')]
q('0009','capraz','orta','Dihibrit çaprazlama','Gamet tablosundan ebeveyn genotiplerini çıkarıp iki özellikli olasılığı hesaplar.','şekilli',
 'gamet tablosundan ebeveyn genotipi ve olasılık','Gamet çeşitleri ebeveyn genotipini verir; iki özellik ayrı ayrı hesaplanıp çarpılır.','Ebeveynlerin ikisini de çift heterozigot sanmak.',
 [A('Gametleri oku','1. birey RY, Ry, rY, ry; 2. birey Ry ve ry gameti vermiştir.','4 çeşit ve 2 çeşit'),A('Genotipleri bul','4 çeşit gamet veren birey çift heterozigottur; 2 çeşit gamet veren birey R için heterozigot, y için homozigot çekiniktir.','RrYy × Rryy'),A('Özellikleri ayır','R_ olasılığı 3/4; Y_ olasılığı yalnız 1. bireyden gelen Y’ye bağlı olduğundan 1/2’dir.','3/4 ve 1/2'),A('Olasılıkları çarp','Bağımsız özelliklerin olasılıkları çarpılır; tabloda 8 kutudan 3’ü uygundur.','3/4 × 1/2 = 3/8')],
 metin='Şekilde, bağımsız ayrılan iki gen çifti (R, r ve Y, y) bakımından iki bireyin gametleri verilmiştir. R ve Y baskın, r ve y çekinik alellerdir. Kutular yavruları göstermektedir ve her kutu eşit olasılıklıdır.\nBuna göre bu çaprazlamadan elde edilen yavruların iki özellik bakımından da baskın fenotipli olma olasılığı kaçtır?',
 sekil=SK9,istenen='İki özellikte de baskın fenotipli yavru olasılığı.',ip=['Gamet çeşitlerinin sayısından her bireyin hangi gen çiftlerinde heterozigot olduğunu çıkar.'],bilgi=[B_GAM,B_CAP],
 puf='Gamet çeşitlerinden ebeveyn genotipi çıkarılır; sonra her özellik ayrı hesaplanıp çarpılır.',
 **frs(d9,t9))

# ===================== 0010 · çaprazlama · zor · koşullu olasılık =====================
c10=cross('AaBb','AaBb'); pay=sum(v for g,v in c10.items() if not (dm(g,0) and dm(g,1))); pey=c10['aabb']; assert (pay,pey)==(7,1)
d10=Fr(pey,pay)
t10=[(Fr(1,16),'Koşulu paydaya katmayıp 16 kutudan 1’ini almış.','dikkat'),(Fr(1,9),'Payda olarak iki özellikte baskın fenotipli grubu (9) almış.','dikkat'),(Fr(1,3),'Çekinik fenotipli grupları üç tür sayıp eşit olasılıklı sanmış.','bilgi'),(Fr(7,16),'Koşulu sağlayan bireylerin oranını sorulan olasılık sanmış.','dikkat')]
q('0010','capraz','zor','Dihibrit çaprazlama','Dihibrit çaprazlamada koşullu olasılığı tümleyen küme ile hesaplar.','düz',
 'en az bir özellikte çekinik koşulu','Koşul “en az bir özellikte çekinik” ise payda 16 − 9 = 7’dir; istenen çift çekinik yavru 1 kutudur.','Paydayı 16 almak.',
 [A('Toplam kutuyu bul','AaBb × AaBb çaprazında 4 × 4 = 16 eşit olasılıklı kutu vardır.','16 kutu'),A('Tümleyeni kullan','İki özellikte baskın fenotipli yavrular A_B_ 9 kutudur.','16 − 9 = 7'),A('Koşulu sağlayanlar','En az bir özellikte çekinik olanlar paydayı oluşturur: 7 kutu.','Payda: 7'),A('Olasılığı yaz','Çift çekinik fenotip yalnız aabb genotipinde, tek kutuda görülür.','1/7')],
 metin='Bağımsız ayrılan, tam baskınlık gösteren iki gen çifti (A, a ve B, b) bakımından AaBb genotipli iki birey çaprazlanıyor. Yavrulardan, en az bir özellik bakımından çekinik fenotipli olanlar arasından rastgele bir birey seçiliyor.\nBuna göre seçilen bireyin iki özellik bakımından da çekinik fenotipli olma olasılığı kaçtır?',
 istenen='Koşullu olasılık.',ip=['Koşulu sağlayan kutuların sayısını bul.'],bilgi=[B_CAP,B_KOS],
 puf='Koşullu olasılıkta önce koşulu sağlayan kutuları say; payda 16 değil, bu sayıdır.',
 **frs(d10,t10))

# ===================== 0011 · çaprazlama · orta · sütun grafiği · öncüllü =====================
N11=[('Mor, düz',48),('Mor, buruşuk',52),('Sarı, düz',51),('Sarı, buruşuk',49)]; assert sum(n for _,n in N11)==200
c11=cross('MmDd','mmdd'); assert set(c11.values())=={4} and len(c11)==4
_g11=['MMDD','MMDd','MmDD','MmDd']
_ok11=[x for x in _g11 if len(cross(x,'mmdd'))==4]
assert _ok11==['MmDd']
D11={'I':(True,'Dört fenotipin yaklaşık eşit çıkması, mor ve düz tohumlu bireyin MmDd olduğunu gösterir.'),
     'II':(False,'mmdd genotipli birey yalnız md gameti oluşturur; tek çeşit gamet verir.'),
     'III':(False,'Mor ve düz tohumlu yavruların tamamı MmDd’dir; MMDD genotipli yavru oluşmaz.')}
assert all(g[0:2]!='MM' and g[2:4]!='DD' for g in c11)
bars=[]; mx=60
for i,(a,n) in enumerate(N11):
    x=.9+i*1.55; bars.append(f'\\draw[line width=1pt,fill=black,fill opacity=.25] ({x-.5:.2f},0) rectangle ({x+.5:.2f},{n/mx*4:.2f});\\draw[line width=1pt] ({x-.5:.2f},0) rectangle ({x+.5:.2f},{n/mx*4:.2f});')
    bars.append(f'\\node[font=\\small,align=center] at ({x:.2f},-.55) {{{a.split(", ")[0]},\\\\{a.split(", ")[1]}}};')
    bars.append(f'\\node[font=\\small] at ({x:.2f},{n/mx*4+.25:.2f}) {{{n}}};')
bars.append('\\draw[line width=1pt] (0,0)--(0,4.4);\\draw[line width=1pt] (0,0)--(6.7,0);')
for t in range(0,61,20): bars.append(f'\\draw[line width=.8pt] (0,{t/mx*4:.2f})--(-.1,{t/mx*4:.2f});\\node[font=\\small,anchor=east] at (-.12,{t/mx*4:.2f}) {{{t}}};')
bars.append('\\node[font=\\small,rotate=90] at (-.95,2.2) {Tohum sayısı};')
SK11=tk('\n'.join(bars),.95)
q('0011','capraz','orta','Kontrol çaprazlaması','Dihibrit kontrol çaprazlaması sonuçlarından ebeveyn genotiplerini çıkarır.','grafik',
 'sütun grafiğinde 1 : 1 : 1 : 1 oranı','Çift çekinik bireyle yapılan çaprazlamada 1 : 1 : 1 : 1 oranı, diğer ebeveynin çift heterozigot olduğunu gösterir.','Çift çekinik ebeveynin birden çok gamet verdiğini sanmak.',
 [A('Grafiği oku','Dört fenotipin sayısı birbirine yakındır.','Yaklaşık 1 : 1 : 1 : 1'),A('Ebeveyn genotipini bul','Çift çekinik ebeveyn yalnız md gameti verir; dört fenotip için diğer ebeveyn dört gamet vermelidir.','Mor, düz ebeveyn: MmDd')]+oncad(D11)+[A('Sonuç','Doğru öncül seçilir.',', '.join(k for k in D11 if D11[k][0]))],
 metin=metin_onc('Mısır bitkisinde mor tohum rengi (M) sarı (m) üzerine, düz tohum yüzeyi (D) buruşuk (d) üzerine tam baskındır; genler farklı kromozom çiftlerindedir. Mor ve düz tohumlu bir bitki, sarı ve buruşuk tohumlu bir bitkiyle çaprazlanıyor ve 200 tohumun fenotip dağılımı grafikte verilmiştir.\nBuna göre,',
   {'I':'Mor ve düz tohumlu ebeveyn iki özellik bakımından heterozigottur.','II':'Sarı ve buruşuk tohumlu ebeveyn dört çeşit gamet oluşturmuştur.','III':'Bazı yavrular iki özellik bakımından homozigot baskındır.'},'ifadelerinden hangileri doğrudur?'),
 sekil=SK11,istenen='Doğru olan ifadeler.',ip=['Çift çekinik ebeveynin kaç çeşit gamet verdiğini düşün; dört fenotip için diğer ebeveynin kaç çeşit gamet vermesi gerekir?'],bilgi=[B_GAM,B_CAP],
 puf='Test çaprazlamasında yavru fenotip çeşitleri, baskın fenotipli ebeveynin gamet çeşitlerini doğrudan gösterir.',
 **onc(D11,[('I',),('II',),('III',),('I','II'),('I','III')]))

# ===================== 0012 · baskınlık · kolay · hikâyeli · eksik baskınlık =====================
c12=cross('KB','KB'); assert (c12['KK'],c12['BK'] if 'BK' in c12 else c12['KB'],c12['BB'])==(1,2,1)
T12=360; kb=T12*Fr(c12['KK'],4); bb=T12*Fr(c12['BB'],4); pm=T12*Fr(c12['BK'],4); assert (kb,pm,bb)==(90,180,90) and kb+bb==180
q('0012','baskin','kolay','Eksik baskınlık','Eksik baskınlıkta F2 genotip ve fenotip sayılarını hesaplar.','hikâyeli',
 'pembe × pembe çiçek sayıları','Eksik baskınlıkta heterozigot × heterozigot çaprazı fenotipte de 1 : 2 : 1 verir.','Eksik baskınlıkta 3 : 1 oranı uygulamak.',
 [A('Genotipleri yaz','Pembe çiçekli bitkiler heterozigottur.','KB × KB'),A('Oranı bul','Eksik baskınlıkta fenotip oranı genotip oranına eşittir.','1 KK : 2 KB : 1 BB'),A('Sayıları hesapla','Kırmızı çiçekli bitkiler 1/4, beyaz çiçekli bitkiler 1/4 oranındadır.','90 kırmızı, 180 pembe, 90 beyaz'),A('Sonuç','Kırmızı ve beyaz çiçekli bitkiler toplanır.','90 + 90 = 180')],
 metin='Gece yarısı çiçeğinde çiçek rengi eksik baskınlıkla kalıtılır: kırmızı çiçekli bitkilerin genotipi KK, beyaz çiçekli bitkilerin genotipi BB, pembe çiçekli bitkilerin genotipi KB’dir. Bir bahçıvan, pembe çiçekli iki bitkiyi çaprazlayarak elde ettiği 360 tohumun hepsini yetiştiriyor.\nBuna göre yetişen bitkilerden kırmızı ya da beyaz çiçekli olanların toplam sayısı kaçtır?',
 istenen='Kırmızı ya da beyaz çiçekli bitkilerin toplam sayısı.',ip=['Pembe çiçekli bitkilerin genotipini yazıp yavru oranını eksik baskınlığa göre kur.'],bilgi=[B_EKS,B_CAP],
 puf='Eksik baskınlıkta Aa × Aa çaprazının fenotip oranı 1 : 2 : 1’dir; üç fenotip de görülür.',
 dogru=180,yan=[(90,'Yalnızca bir homozigot sınıfın (kırmızı ya da beyaz) sayısını bulmuş.','dikkat'),(240,'Üç fenotipin eşit sayıda olduğunu sanıp 360’ın 2/3’ünü almış.','bilgi'),(270,'Tam baskınlıktaki 3 : 1 oranını uygulayıp 360’ın 3/4’ünü almış.','bilgi'),(360,'Tüm bitkilerin kırmızı ya da beyaz olacağını sanmış.','bilgi')])

# ===================== 0013 · baskınlık · orta · hikâyeli · öncüllü · eş baskınlık =====================
assert dict(cross('KB','KB'))=={'KK':1,'BK':2,'BB':1} or dict(cross('KB','KB'))=={'KK':1,'KB':2,'BB':1}
c13=cross('KB','BB'); assert sorted(c13.values())==[2,2] and set(c13)=={'KB','BB'} or set(c13)=={'BK','BB'}
D13={'I':(False,'Alaca bireylerde kırmızı ve beyaz tüylerin ikisi de ayrı ayrı görüldüğü için bu eş baskınlıktır; eksik baskınlıkta ara bir fenotip oluşur.'),
     'II':(True,'KB × KB çaprazında KK : KB : BB oranı 1 : 2 : 1’dir; eş baskınlıkta fenotip oranı da bu oranı izler.'),
     'III':(False,'KB × BB çaprazında yavruların yarısı alaca (KB), yarısı beyaz (BB) olur.')}
q('0013','baskin','orta','Eş baskınlık','Eş baskınlık ile eksik baskınlığı ayırt edip çaprazlama sonuçlarını yorumlar.','öncüllü',
 'alaca tüylü sığırlarda eş baskınlık','Heterozigotta iki alelin ürünü birlikte görülüyorsa eş baskınlıktır; çaprazlama oranları 1 : 2 : 1 ve 1 : 1’dir.','Eş baskınlığı eksik baskınlık sanmak.',
 [A('Baskınlığı belirle','Kırmızı ve beyaz tüylerin ikisi de ayrı ayrı oluşuyor; alaca tüylülük eş baskınlıktır.','Eş baskınlık')]+oncad(D13)+[A('Sonuç','Doğru öncül seçilir.',', '.join(k for k in D13 if D13[k][0]))],
 metin=metin_onc('Bazı sığır ırklarında kırmızı tüylü (KK) ile beyaz tüylü (BB) bireyler çaprazlandığında yavruların tamamı alaca olmaktadır. Alaca bireylerde kırmızı ve beyaz tüylerin her ikisi de ayrı ayrı oluşmaktadır.\nBuna göre,',
   {'I':'Alaca tüylülük eksik baskınlığa örnektir.','II':'Alaca bireylerin kendi aralarında çaprazlanmasında kırmızı, alaca ve beyaz yavrular 1 : 2 : 1 oranında beklenir.','III':'Alaca bir birey ile beyaz tüylü bir birey çaprazlanırsa yavruların tamamı alaca olur.'},'ifadelerinden hangileri doğrudur?'),
 istenen='Doğru olan ifadeler.',ip=['Alaca bireylerde iki alelin ürününün karışmadan ayrı ayrı görüldüğünü hangi baskınlık türüyle ilişkilendirirsin?'],bilgi=[B_EKS],
 puf='Heterozigotta iki aleli ayrı ayrı gözlüyorsan eş baskınlık, ara tonda tek fenotip görüyorsan eksik baskınlık vardır.',
 **onc(D13,[('I',),('II',),('III',),('I','II'),('II','III')]))

# ===================== 0014 · baskınlık · orta · sütun grafiği · öncüllü · kontrol çaprazlaması =====================
N14={1:(7,0),2:(3,4),3:(5,1)}
def mumkun14(gri,beyaz):   # dişi genotipi (GG ya da Gg) beyaz erkek gg ile çaprazlanınca bu yavru dizisi olabilir mi
    return [g for g in('GG','Gg') if (beyaz==0 or 'g' in g)]
assert mumkun14(*N14[1])==['GG','Gg'] and mumkun14(*N14[2])==['Gg'] and mumkun14(*N14[3])==['Gg']
assert Fr(1,2)**7>0       # Gg dişinin 7 yavrunun tamamının gri olması mümkündür (1/128)
D14={'I':(False,'7 gri yavrunun hepsinin gri çıkması, dişinin Gg olma olasılığını ortadan kaldırmaz (Gg × gg’de her yavru 1/2 olasılıkla gridir); homozigot olduğu kesin değildir.'),
     'II':(True,'Beyaz (gg) yavrunun bir g’sini dişi vermiştir; gri olduğu için G de taşır, dolayısıyla Gg’dir.'),
     'III':(True,'Beyaz yavru doğduğuna göre dişi g aleli taşır; gri olduğu için genotipi Gg’dir.')}
b14=[]
for i,(k,(g,b)) in enumerate(N14.items()):
    x=1.2+i*2.3
    for j,(n,dolu) in enumerate(((g,True),(b,False))):
        xx=x+(j-.5)*.8; h=n*.5
        if n>0: b14.append(f'\\draw[line width=1pt{",fill=black,fill opacity=.35" if dolu else ""}] ({xx-.35:.2f},0) rectangle ({xx+.35:.2f},{h:.2f});')
        b14.append(f'\\node[font=\\small] at ({xx:.2f},{h+.25:.2f}) {{{n}}};')
    b14.append(f'\\node[font=\\small] at ({x:.2f},-.4) {{Dişi {k}}};')
b14.append('\\draw[line width=1pt] (0,0)--(0,4.2);\\draw[line width=1pt] (0,0)--(7.0,0);')
for t in (0,2,4,6,8): b14.append(f'\\draw[line width=.8pt] (0,{t*.5:.2f})--(-.1,{t*.5:.2f});\\node[font=\\small,anchor=east] at (-.12,{t*.5:.2f}) {{{t}}};')
b14.append('\\node[font=\\small,rotate=90] at (-.85,2.1) {Yavru sayısı};')
b14.append('\\draw[line width=1pt,fill=black,fill opacity=.35] (5.0,4.6) rectangle (5.3,4.9);\\node[font=\\small,anchor=west] at (5.4,4.75) {Gri};\\draw[line width=1pt] (6.2,4.6) rectangle (6.5,4.9);\\node[font=\\small,anchor=west] at (6.6,4.75) {Beyaz};')
SK14=tk('\n'.join(b14),1.1)
q('0014','baskin','orta','Kontrol çaprazlaması','Kontrol çaprazlaması sonuçlarından hangi bireylerin genotipinin kesin olduğunu belirler.','grafik',
 'kontrol çaprazlamasında kesinlik','Çekinik yavru çıkıyorsa baskın fenotipli ebeveyn kesin heterozigottur; hiç çıkmıyorsa homozigot olduğu kesin söylenemez.','Tüm yavruların baskın çıkmasını homozigotluğun kanıtı saymak.',
 [A('Erkeğin genotipini yaz','Beyaz tüylü erkek çekiniktir ve her yavruya g aleli verir.','Erkek: gg')]+oncad(D14)+[A('Sonuç','Kesinlikle doğru olanlar seçilir.',', '.join(k for k in D14 if D14[k][0]))],
 metin=metin_onc('Farelerde gri tüy rengi (G), beyaz tüy rengi (g) üzerine tam baskındır. Bir araştırmacı, gri tüylü üç dişi fareyi (1, 2 ve 3 numaralı) ayrı ayrı beyaz tüylü bir erkek fareyle çiftleştirip doğan yavruların tüy renklerini grafikte gösteriyor. Yavru sayıları az olduğundan, bir dişinin genotipi yalnızca sonuçlardan zorunlu olarak çıkıyorsa kesin kabul edilecektir.\nBuna göre,',
   {'I':'1 numaralı dişi homozigottur.','II':'2 numaralı dişi heterozigottur.','III':'3 numaralı dişi heterozigottur.'},'ifadelerinden hangileri kesinlikle doğrudur?'),
 sekil=SK14,istenen='Kesinlikle doğru olan ifadeler.',ip=['Her dişi için beyaz yavru doğup doğmadığına bak.'],bilgi=[B_TEST,B_KAV],
 puf='Çekinik yavru çıkması heterozigotluğu kanıtlar; çıkmaması homozigotluğu kanıtlamaz, yalnız olasılığını artırır.',
 **onc(D14,[('I',),('II',),('I','II'),('I','III'),('II','III')]))

# ===================== 0015 · baskınlık · zor · eksik baskın + tam baskın =====================
def fen15(g):  # g: 'KBDd' gibi (renk çifti + yaprak çifti)
    return (''.join(sorted(g[:2])),'düz' if 'D' in g[2:] else 'dişli')
c15=Counter()
for a in gam('KBDd'):
    for b in gam('KBdd'): c15[fen15(''.join(sorted(a[0]+b[0]))+''.join(sorted(a[1]+b[1])))]+=1
assert sum(c15.values())==16 and len(c15)==6 and min(c15.values())==2
n15=len(c15); m15=Fr(min(c15.values()),sum(c15.values())); assert m15==Fr(1,8)
d15=f'{n15} çeşit – {sf(m15)}'
y15=[('4 çeşit – 1/8','Çiçek rengini de tam baskınlıkla düşünüp 2 × 2 = 4 fenotip bulmuş.','bilgi'),('6 çeşit – 1/4','Çeşit sayısını doğru bulmuş; ancak en az görülen fenotipin oranı yerine pembe fenotiplerin toplam oranını (1/4) vermiş.','dikkat'),('8 çeşit – 1/8','Kutu sayısını (8) fenotip çeşidi sanmış.','dikkat'),('4 çeşit – 1/16','Dihibrit çaprazlamadaki 9 : 3 : 3 : 1 oranından 4 fenotip ve 1/16’yı almış.','bilgi')]
q('0015','baskin','zor','Eksik baskınlık ve dihibrit','Biri eksik baskın, biri tam baskın iki özelliğin çaprazlamasında fenotip çeşidini ve oranları hesaplar.','hikâyeli',
 'eksik baskınlık ve tam baskınlık birlikte','Eksik baskın özellikte üç, tam baskın özellikte iki fenotip vardır; çeşit sayıları çarpılır, oranlar birleştirilir.','Eksik baskın özellikte de iki fenotip saymak.',
 [A('Özellikleri ayır','Çiçek rengi eksik baskın (3 fenotip), yaprak kenarı tam baskındır (2 fenotip).','3 × 2'),A('Renk oranı','Pembe × pembe çaprazında yavrular kırmızı, pembe ve beyaz olarak 1 : 2 : 1 oranında görülür.','1/4, 1/2, 1/4'),A('Yaprak oranı','Dd × dd çaprazında düz ve dişli yapraklı yavrular eşittir.','1/2, 1/2'),A('Fenotipleri birleştir','Altı fenotipten renk bakımından pembe olanlar 1/4, diğerleri 1/8 oranındadır.','6 çeşit; en az 1/8')],
 metin='Bir süs bitkisinde çiçek rengi eksik baskınlıkla kalıtılır (kırmızı: KK, pembe: KB, beyaz: BB); düz yaprak kenarı (D), dişli kenar (d) üzerine tam baskındır. İki gen çifti bağımsız ayrılmaktadır. KBDd genotipli bir bitki ile KBdd genotipli bir bitki çaprazlanıyor.\nBuna göre yavrularda kaç çeşit fenotip görülür ve en az oranda görülen fenotiplerden her biri yavruların kaçta kaçını oluşturur?',
 istenen='Fenotip çeşidi sayısı ve en az görülen fenotiplerin oranı.',ip=['Her özelliği ayrı ayrı çaprazla.'],bilgi=[B_EKS,B_CAP],
 puf='Eksik baskın özellik üç, tam baskın özellik iki fenotip verir; bağımsız özelliklerde çeşit sayıları ve oranlar çarpılır.',
 dogru=d15,yan=y15,sira=yer('A',d15,[x[0] for x in y15]))

# ===================== 0016 · baskınlık · kolay · düz olumsuz =====================
S16=[('Tam baskınlıkta heterozigot birey, baskın alelin belirlediği fenotipi gösterir.',True,'tam baskınlıkta heterozigot baskın fenotipi gösterir.'),
     ('Eksik baskınlıkta heterozigot bireyin fenotipi, iki homozigot bireyin fenotipi arasında bir görünümdedir.',True,'eksik baskınlıkta ara fenotip oluşur.'),
     ('Eş baskınlıkta heterozigot bireyde iki alelin etkisi de ayrı ayrı fenotipte görülür.',True,'eş baskınlıkta iki alel de ifade edilir.'),
     ('İnsanlarda AB kan grubu, eş baskınlığa örnektir.',True,'AB grubunda A ve B alelleri birlikte ifade edilir.'),
     ('Eksik baskınlıkta heterozigot bireylerin kendi aralarında çaprazlanmasından elde edilen dölde fenotip oranı 3 : 1’dir.',False,'eksik baskınlıkta döl fenotip oranı 1 : 2 : 1’dir.')]
q('0016','baskin','kolay','Baskınlık türleri','Tam baskınlık, eksik baskınlık ve eş baskınlığı ayırt eder.','düz',
 'baskınlık türleri hakkında yanlış ifade','Üç baskınlık türünün heterozigot fenotipi ve döl oranları.','Eksik baskınlıkta 3 : 1 oranı beklemek.',
 [A('Türleri ayır','Tam baskınlıkta baskın fenotip, eksik baskınlıkta ara fenotip, eş baskınlıkta iki alel de görülür.','3 tür'),A('İfadeleri ele','İlk dört ifade tanımlara uygundur.','4 ifade doğru'),A('Oranı hatırla','Eksik baskınlıkta Aa × Aa çaprazının fenotip oranı 1 : 2 : 1’dir.','Genotip = fenotip oranı'),A('Sonuç','3 : 1 oranını eksik baskınlığa bağlayan ifade yanlıştır.','Yanlış: eksik baskınlıkta 3 : 1')],
 metin='Bir kalıtım ders notunda, tam baskınlık, eksik baskınlık ve eş baskınlık örnekleri karşılaştırılırken beş ifade yer almaktadır. Bu ifadelerden yalnızca biri bilimsel olarak hatalıdır.\nBuna göre bu ifadelerden hangisi yanlıştır?',
 istenen='Yanlış olan ifade.',ip=['Heterozigot × heterozigot çaprazının sonucunu her baskınlık türü için ayrı ayrı yaz.'],bilgi=[B('Çaprazlama oranı','Heterozigot × heterozigot çaprazında genotip oranı 1 : 2 : 1’dir; fenotip oranı baskınlık türüne göre belirlenir')],
 puf='Eksik ve eş baskınlıkta heterozigot × heterozigot çaprazının fenotip oranı 1 : 2 : 1’dir; yalnız tam baskınlıkta 3 : 1’dir.',
 **tek([S16[i] for i in (4,0,1,2,3)],hedef=False))

# ===================== 0017 · abo · kolay · tablo · olumsuz =====================
SATIR={'A':('A grubu','A','Anti-B','AA veya AO'),'B':('B grubu','B','Anti-A','BB veya BO'),'AB':('AB grubu','A, B','Anti-A, anti-B','AB'),'O':('O grubu','Yok','Anti-A, anti-B','OO'),'Rh':('Rh+','Rh','Yok','RR veya Rr')}
# doğru bilgiler (AB satırı hatalı yazılmıştır)
DOGRU17={'A':('A','Anti-B'),'B':('B','Anti-A'),'AB':('A, B','Yok'),'O':('Yok','Anti-A, anti-B')}
sira17=['A','B','O','AB','Rh']; hata17=[k for k in sira17 if k in DOGRU17 and (SATIR[k][1],SATIR[k][2])!=DOGRU17[k]]; assert hata17==['AB']
rows17=[[str(i+1)]+list(SATIR[k][:3]) for i,k in enumerate(sira17)]
ABOR={'A':'A grubunda alyuvarda A antijeni, plazmada anti-B bulunur; genotip AA veya AO’dur.','B':'B grubunda alyuvarda B antijeni, plazmada anti-A bulunur; genotip BB veya BO’dur.','O':'O grubunda alyuvarda antijen yoktur, plazmada anti-A ve anti-B bulunur; genotip OO’dur.','Rh':'Rh+ bireyin alyuvarlarında Rh antijeni vardır ve genotipi RR ya da Rr’dir.'}
y17=[(f'{i+1}. satır','Bu satırdaki bilgi doğrudur: '+ABOR[k],'bilgi') for i,k in enumerate(sira17) if k!='AB']
d17=f'{sira17.index("AB")+1}. satır'
q('0017','abo','kolay','Kan grupları tablosu','ABO ve Rh kan gruplarının antijen, antikor ve genotip bilgilerini ayırt eder.','tablo',
 'kan grubu tablosunda yanlış satır','AB grubunun alyuvarında A ve B antijeni bulunur, plazmasında anti-A ve anti-B antikoru bulunmaz.','AB grubunun plazmasında her iki antikoru da bulunduğunu sanmak.',
 [A('Antijenleri hatırla','Alyuvardaki antijen kan grubunun adını belirler; O grubunda antijen yoktur.','A, B, AB ve O'),A('Antikorları hatırla','Plazma, alyuvarında bulunmayan antijene karşı antikor taşır.','A grubu: anti-B; B grubu: anti-A'),A('Satırları sına','AB grubunda hem A hem B antijeni olduğundan plazmada anti-A ve anti-B bulunamaz.','AB: antikor yok'),A('Sonuç','Yalnızca AB satırındaki antikor bilgisi yanlıştır.','AB satırı yanlış')],
 metin='Bir biyoloji öğretmeni, öğrencilerinden insanlardaki ABO ve Rh kan gruplarının özelliklerini özetleyen bir tablo hazırlamalarını istiyor. Bir öğrencinin hazırladığı tablo aşağıda verilmiştir ve tabloda yalnız bir satırdaki bilgi hatalıdır.\nBuna göre tablonun hangi satırındaki bilgi yanlıştır?',
 sekil=tablo_svg(['Satır','Kan grubu','Alyuvar antijeni','Plazma antikoru'],rows17),
 istenen='Hatalı bilgi içeren satır.',ip=['Satırlardaki antijen–antikor eşleşmesini sına.'],bilgi=[B_ABO],
 puf='Plazma, kendi alyuvarında bulunmayan antijenlere karşı antikor taşır; AB grubunda antikor yoktur.',
 dogru=d17,yan=y17,sira=[f'{i}. satır' for i in range(1,6)])

# ===================== 0018 · abo · orta · aglütinasyon şekli · öncüllü =====================
def uyum(ver,al):
    ABOK={'A':{'A'},'B':{'B'},'AB':{'A','B'},'O':set()}
    return ABOK[ver[0]]<=ABOK[al[0]] and not (ver[1]=='+' and al[1]=='-')
KISI18={'I':('A','+'),'II':('O','-'),'III':('AB','-')}
def kume(g,rh): return [g in('A','AB'),g in('B','AB'),rh=='+']
SON18={k:kume(*v) for k,v in KISI18.items()}
assert SON18=={'I':[True,False,True],'II':[False,False,False],'III':[True,True,False]}
D18={'I':(uyum(KISI18['I'],KISI18['III']),'I numaralı birey Rh+ (A Rh+), III numaralı birey Rh− (AB Rh−) olduğundan Rh+ kan, Rh− bireye verilmez.'),
     'II':(all(uyum(KISI18[x],KISI18['II']) for x in ('I','III')),'II numaralı birey O Rh−’dir; yalnız O Rh− kan alabilir, A Rh+ ve AB Rh− kanını alamaz.'),
     'III':(True,'III numaralı birey AB grubudur; alyuvarında A ve B antijeni bulunduğu için plazmasında anti-A ve anti-B antikoru yoktur.')}
assert [v[0] for v in D18.values()]==[False,False,True]
rnd=random.Random(18)
def damla(cx,cy,kum,R=.46):
    b=[f'\\draw[line width=1pt] ({cx},{cy}) circle ({R});']; p=[]
    if kum:
        for _ in range(4):
            a=rnd.uniform(0,6.28); r=rnd.uniform(0,.22); x=cx+r*math.cos(a); y=cy+r*math.sin(a)
            for _ in range(2):
                p.append(f'({x+rnd.uniform(-.08,.08):.2f},{y+rnd.uniform(-.08,.08):.2f}) circle ({rnd.uniform(.10,.14):.2f})')
    else:
        n=0
        while n<22:
            x=rnd.uniform(-1,1)*(R-.08); y=rnd.uniform(-1,1)*(R-.08)
            if x*x+y*y<(R-.08)**2: p.append(f'({cx+x-.03:.2f},{cy+y-.03:.2f}) rectangle ++(.06,.06)'); n+=1
    b.append('\\fill '+' '.join(p)+';')
    return '\n'.join(b)
b18=[]
for j,t in enumerate(('Anti-A','Anti-B','Anti-Rh')): b18.append(f'\\node[font=\\small\\bfseries] at ({1.5+j*1.3:.2f},3.45) {{{t}}};')
for i,(k,v) in enumerate(SON18.items()):
    y=2.55-i*1.15; b18.append(f'\\node[font=\\normalsize\\bfseries] at (.2,{y:.2f}) {{{k}}};')
    for j,kum in enumerate(v): b18.append(damla(1.5+j*1.3,y,kum))
SK18=tk('\n'.join(b18),1.6)
q('0018','abo','orta','Kan nakli','Aglütinasyon sonuçlarından kan grubunu belirleyip kan nakli uygunluğunu değerlendirir.','şekilli',
 'aglütinasyon sonuçlarından kan nakli yorumu','Serumla kümelenen damla ilgili antijenin varlığını gösterir; nakilde alıcıda ABO ya da Rh uyuşmazlığı oluşmamalıdır.','Rh+ kanın Rh− bireye verilebileceğini sanmak.',
 [A('Kan gruplarını oku','Kümelenme olan serum, kanda o antijenin varlığını gösterir.','I: A Rh+ · II: O Rh− · III: AB Rh−')]+oncad(D18)+[A('Sonuç','Doğru öncül seçilir.',', '.join(k for k in D18 if D18[k][0]))],
 metin=metin_onc('Üç kişinin kan örneklerine anti-A, anti-B ve anti-Rh serumları ayrı ayrı damlatılmış ve sonuçlar şekilde gösterilmiştir. İri kümelerin oluştuğu damlalarda ilgili antijen alyuvarlarda bulunmaktadır. Kan naklinde ABO ya da Rh uyuşmazlığı oluşturacak kan verilmemektedir.\nBuna göre,',
   {'I':'I numaralı bireyin kanı III numaralı bireye verilebilir.','II':'II numaralı birey, diğer iki bireyden kan alabilir.','III':'III numaralı bireyin plazmasında anti-A ve anti-B antikorları bulunmaz.'},'ifadelerinden hangileri doğrudur?'),
 sekil=SK18,istenen='Doğru olan ifadeler.',ip=['Önce her bireyin hangi serumlarda kümelendiğine bakarak kan grubunu ve Rh durumunu belirle.'],bilgi=[B_ABO,B('Aglütinasyon','Serumdaki antikor, kendi antijenini taşıyan alyuvarları kümelendirir')],
 puf='Kümelenen serum antijeni gösterir; nakilde vericinin antijeninin alıcıda antikoru bulunmamalı, Rh+ kan Rh− bireye verilmemelidir.',
 **onc(D18,[('I',),('III',),('I','II'),('I','III'),('II','III')]))

# ===================== 0019 · abo · orta · aile şeması · kesir =====================
FAM={'Anne':('K','A'),'Baba':('E','A'),'Kız':('K','A'),'Oğul':('E','O')}
# O grubu oğul: iki ebeveyn de O aleli taşımalı; ebeveynler A grubu → AO
adaylar=[g for g in('AA','AO')]
tam=[(x,y) for x in adaylar for y in adaylar if abo_c(list(x),list(y))['O']>0]; assert tam==[('AO','AO')]
c19=abo_c(['A','O'],['A','O']); assert c19['A']==3 and c19['O']==1
d19=Fr(1,2)*Fr(c19['A'],4); assert d19==Fr(3,8)
def sembol(x,y,cins,metin_):
    R=.4
    s=f'\\draw[line width=1pt] ({x-R},{y-R}) rectangle ({x+R},{y+R});' if cins=='E' else f'\\draw[line width=1pt] ({x},{y}) circle ({R});'
    return s+f'\\node[font=\\large\\bfseries] at ({x},{y}) {{{metin_}}};'
b19=[sembol(0,2.6,'K',FAM['Anne'][1]),sembol(2,2.6,'E',FAM['Baba'][1]),'\\draw[line width=1pt] (.4,2.6)--(1.6,2.6);',
     '\\draw[line width=1pt] (1,2.6)--(1,1.7);\\draw[line width=1pt] (-.2,1.7)--(2.2,1.7);\\draw[line width=1pt] (-.2,1.7)--(-.2,1.0);\\draw[line width=1pt] (2.2,1.7)--(2.2,1.0);',
     sembol(-.2,.6,'K',FAM['Kız'][1]),sembol(2.2,.6,'E',FAM['Oğul'][1])]
SK19=tk('\n'.join(b19),1.6)
t19=[(Fr(1,8),'Kız olma (1/2) ve O grubundan olma (1/4) olasılıklarını çarpmış; A grubunu istemeyi unutmuş.','dikkat'),(Fr(1,4),'Yalnız AO genotipli çocuk olasılığını (1/2) kızla çarpmış; AA olasılığını atlamış.','bilgi'),(Fr(1,2),'Cinsiyeti hesaba katıp kan grubunun kesin A olacağını sanmış.','dikkat'),(Fr(3,4),'Yalnız A grubundan olma olasılığını (3/4) vermiş; kız olmayı eklememiş.','dikkat')]
q('0019','abo','orta','Aile kan grupları','Ailedeki kan gruplarından ebeveyn genotiplerini çıkarıp cinsiyetle birlikte olasılık hesaplar.','hikâyeli',
 'aile kan gruplarından genotip ve cinsiyetli olasılık','O grubundan çocuk, A grubundan iki ebeveynin de AO olduğunu gösterir; cinsiyet olasılığı ayrıca çarpılır.','Ebeveynleri AA sanmak ya da cinsiyet olasılığını unutmak.',
 [A('Verileri oku','Anne ve baba A grubunda, oğul O, kız A grubundadır.','A × A → A, O'),A('Ebeveyn genotipini bul','O grubundaki oğul her ebeveynden bir O aleli almıştır; ebeveynler A grubundan olduğuna göre AO’dur.','AO × AO'),A('Kan grubu olasılığı','Çaprazda AA, AO, AO, OO oluşur; A grubu üç kutudadır.','3/4'),A('Cinsiyeti ekle','Kız çocuk olma olasılığı bağımsızdır ve 1/2’dir.','3/4 × 1/2 = 3/8')],
 metin='Bir ailede anne ve baba A kan grubundandır; ailenin kız çocuğu A, erkek çocuğu O kan grubundandır. Bu aile bir çocuk daha sahibi olmayı planlamaktadır.\nBuna göre ailenin bir sonraki çocuğunun kız ve A kan grubundan olma olasılığı kaçtır?',
 istenen='Sonraki çocuğun kız ve A grubundan olma olasılığı.',ip=['O grubundan bir çocuğun ebeveynlerinden hangi aleli aldığını düşün; sonra cinsiyeti ayrı bir olay say.'],bilgi=[B_ABO,B_CAP],
 puf='O grubundan çocuk, A ya da B grubundan ebeveynlerin O aleli taşıdığını (AO, BO) kanıtlar.',
 **frs(d19,t19))

# ===================== 0020 · abo · orta · Rh · öncüllü =====================
c20=Counter(''.join(sorted(a+b)) for a in 'Rr' for b in 'rr'); assert c20['Rr']==2 and c20['rr']==2
D20={'I':(True,'Rh− çocuk rr’dir; bir r’yi baba vermiştir. Baba Rh+ olduğundan Rr’dir.'),
     'II':(False,'Rr × rr çaprazında Rh− (rr) yavru olasılığı 1/2’dir; 1/4 değil.'),
     'III':(True,'Anne, Rh antijenine ancak Rh+ bir bebekle ya da Rh+ kanla karşılaşırsa antikor üretir; ilk çocuk Rh− olduğu için böyle bir karşılaşma olmamıştır.')}
q('0020','abo','orta','Rh faktörü','Rh genotiplerini çocuktan çıkarır, olasılık ve antikor oluşumunu yorumlar.','öncüllü',
 'Rh− anne, Rh+ baba, Rh− çocuk','Rh− çocuk babanın heterozigot olduğunu gösterir; Rh antikoru yalnız Rh antijeniyle karşılaşınca oluşur.','Rh− annenin her durumda antikor ürettiğini sanmak.',
 [A('Genotipleri bul','Anne rr, çocuk rr; babadan gelen r nedeniyle baba Rr’dir.','Rr × rr')]+oncad(D20)+[A('Sonuç','Doğru öncüller seçilir.',', '.join(k for k in D20 if D20[k][0]))],
 metin=metin_onc('Rh− bir anne ile Rh+ bir babanın ilk çocuğu Rh− doğmuştur. Annenin daha önce hiç Rh+ kanla karşılaşmadığı bilinmektedir.\nBuna göre,',
   {'I':'Babanın Rh genotipi heterozigottur.','II':'Çiftin ikinci çocuğunun Rh− olma olasılığı 1/4’tür.','III':'Anne, ilk gebeliği sırasında Rh antijenine karşı antikor üretmemiştir.'},'ifadelerinden hangileri doğrudur?'),
 istenen='Doğru olan ifadeler.',ip=['Rh− çocuğun iki r aleline sahip olduğunu ve bunlardan birinin babadan geldiğini kullan.'],bilgi=[B_ABO,B('Antikor','Bağışıklık sistemi, karşılaştığı yabancı antijene karşı antikor üretir')],
 puf='Rh− çocuk, Rh+ babanın heterozigot olduğunu gösterir; antikor oluşumu için Rh antijeniyle karşılaşma gerekir.',
 **onc(D20,[('I',),('II',),('III',),('I','III'),('I','II','III')]))

# ===================== 0021 · abo · zor · olumsuz · baba adayı =====================
ANNE={'ABO':'AO','Rh':'Rr'}; COC=('O','rr')
def baba_olur(gr,rh):   # aday baba grubu/Rh: çocuk O ve Rh− olabilir mi (anne A Rh+)
    abo_ok=any(abo_c(list(ya),list(yb))['O']>0 for ya in ('AO',) for yb in {'A':['AA','AO'],'B':['BB','BO'],'AB':['AB'],'O':['OO']}[gr])
    rh_ok=any('rr' in {''.join(sorted(a+b)) for a in 'Rr' for b in x} for x in {'+':['RR','Rr'],'-':['rr']}[rh])
    return abo_ok and rh_ok
ADAY=[('A','+'),('B','-'),('AB','+'),('O','+'),('O','-')]
imk={a:baba_olur(*a) for a in ADAY}; assert [a for a in ADAY if not imk[a]]==[('AB','+')]
lab=lambda a:f'{a[0]} Rh{"+" if a[1]=="+" else "−"}'
NED21={('A','+'):'AO ve Rr genotipli bir baba O ve rr çocuk verebilir.',('B','-'):'BO ve rr genotipli bir baba O ve rr çocuk verebilir.',('O','+'):'OO ve Rr genotipli bir baba O ve rr çocuk verebilir.',('O','-'):'OO ve rr genotipli bir baba O ve rr çocuk verebilir.'}
y21=[(lab(a),'Bu kan grubundaki bir erkeğin babalığı olabilir; '+NED21[a],'bilgi') for a in ADAY if imk[a]]
q('0021','abo','orta','ABO ve Rh babalık','Çocuğun ve annenin ABO–Rh gruplarından babanın olamayacağı kan grubunu belirler.','hikâyeli',
 'anne A Rh+, çocuk O Rh−: baba olamaz','Çocuğun O ve rr olması annenin AO ve Rr olduğunu gösterir; babanın hem O hem r aleli verebilmesi gerekir.','AB grubundan babanın O aleli veremeyeceğini görmemek.',
 [A('Çocuğu çöz','O grubu çocuk OO, Rh− çocuk rr’dir; her ebeveyn bir O ve bir r vermiştir.','OO ve rr'),A('Anneyi çöz','Anne A grubundan ve Rh+ olduğuna göre O ve r aleli taşıyan AO ve Rr’dir.','AO, Rr'),A('Baba koşulunu yaz','Baba hem O hem r aleli verebilmelidir; AB grubunda O aleli yoktur.','O aleli şart'),A('Adayları ele','Rh+ adaylar Rr olabilir; yalnız AB genotipi O aleli veremez.','AB Rh+ olamaz')],
 metin='Bir hastanede doğan bebeğin kan grubu O Rh−, annenin kan grubu A Rh+ olarak belirlenmiştir. ABO ve Rh özellikleri bağımsız kalıtılmaktadır. Babalık için başvuran beş erkeğin kan grupları aşağıda verilmiştir.\nBuna göre bu erkeklerden hangisi bu bebeğin babası olamaz?',
 istenen='Babalığı mümkün olmayan kan grubu.',ip=['Çocuğun genotipinden annenin hangi alelleri taşıdığını; babanın ise çocuğa hangi aleli vermiş olması gerektiğini çıkar.'],bilgi=[B_ABO,B_CAP],
 puf='O grubu çocuğun iki ebeveyni de O aleli taşır; AB grubundan birey O aleli veremez.',
 dogru=lab(('AB','+')),yan=y21,sira=yer('D',lab(('AB','+')),[lab(a) for a in ADAY if imk[a]]))

# ===================== 0022 · abo · kolay · çok alellilik =====================
GT22=sorted({''.join(sorted(a+b)) for a in 'ABO' for b in 'ABO'}); assert len(GT22)==6
HET22=[g for g in GT22 if g[0]!=g[1]]; assert HET22==['AB','AO','BO'] and len(HET22)==3
q('0022','abo','kolay','Çok alellilik','Çok alelli bir gende genotip çeşitlerini sayar.','hikâyeli',
 'ABO gen yerinde heterozigot genotip sayısı','Üç alelli bir gende altı genotip vardır: üçü homozigot, üçü heterozigot.','AB’yi heterozigot saymamak.',
 [A('Alelleri yaz','ABO sisteminde aynı gen yeri için A, B ve O olmak üzere üç alel vardır.','A, B, O'),A('Genotipleri say','Bir birey bu alellerden ikisini taşır.','AA, BB, OO, AB, AO, BO'),A('Heterozigotları seç','İki aleli farklı olan genotipler heterozigottur.','AB, AO, BO'),A('Sonuç','Heterozigot genotip sayısı üçtür.','3')],
 metin='ABO kan grupları, tek bir gen yerinde bulunabilen üç alelle (A, B ve O) belirlenir. Bir kan bağışı merkezinde çalışan teknisyen, bu gen yeri bakımından bir insan topluluğunda görülebilecek bütün genotipleri sınıflandırmak istiyor.\nBuna göre bu topluluktaki bireylerde görülebilecek heterozigot genotiplerin sayısı kaçtır?',
 istenen='Heterozigot genotip sayısı.',ip=['Bir bireyin kaç alel taşıdığını düşün.'],bilgi=[B_ABO,B_KAV],
 puf='Üç alelli bir gende üç homozigot ve üç heterozigot genotip bulunur.',
 dogru=3,yan=[(1,'Yalnızca AB genotipini heterozigot saymış.','bilgi'),(2,'AO ve BO genotiplerini saymış; AB’nin de heterozigot olduğunu atlamış.','dikkat'),(4,'Dört kan grubunu dört heterozigot genotip sanmış.','bilgi'),(6,'Bütün genotipleri heterozigot saymış.','bilgi')])

# ===================== soy ağacı motoru =====================
def gdom(model,sex):
    if model in('AR','AD'): return (0,1,2)
    if model in('XR','XD'): return (0,1) if sex=='E' else (0,1,2)
    if model=='YL': return (0,1) if sex=='E' else (0,)
def aff(model,sex,g):
    if model=='AR': return g==2
    if model=='AD': return g>=1
    if model=='XR': return g==1 if sex=='E' else g==2
    if model=='XD': return g>=1
    if model=='YL': return sex=='E' and g==1
def trans(model,sex,gm,gf):
    d={}
    def add(g,p): d[g]=d.get(g,0)+p
    if model in('AR','AD'):
        pm=Fr(gm,2); pf=Fr(gf,2)
        for a,pa in((1,pm),(0,1-pm)):
            for b,pb in((1,pf),(0,1-pf)): add(a+b,pa*pb)
    elif model in('XR','XD'):
        pm=Fr(gm,2)
        if sex=='E': add(1,pm); add(0,1-pm)
        else:
            for a,pa in((1,pm),(0,1-pm)): add(a+gf,pa)
    elif model=='YL':
        if sex=='E': add(gf,Fr(1))
        else: add(0,Fr(1))
    return {g:p for g,p in d.items() if p}
class Ped:
    """kisi {ad:(cins,hasta,anne,baba)}; g = hastalık aleli sayısı. Tüm genotip atamaları taranır (fenotip + Mendel aktarımı)."""
    def __init__(s,kisi,model):
        s.k=kisi; s.m=model; s.ad=list(kisi); s.W=[]; dom=[]
        for a in s.ad:
            sx,h=kisi[a][0],kisi[a][1]; dom.append([g for g in gdom(model,sx) if aff(model,sx,g)==bool(h)])
        for tup in itertools.product(*dom):
            G=dict(zip(s.ad,tup)); w=Fr(1)
            for a in s.ad:
                sx,h,an,ba=kisi[a]
                if an is not None: w*=trans(model,sx,G[an],G[ba]).get(G[a],0)
                if w==0: break
            if w: s.W.append((G,w))
    def mumkun(s): return bool(s.W)
    def dest(s,a): return {G[a] for G,w in s.W}
    def T(s): return sum(w for G,w in s.W)
def modeller(K,ms=('AR','AD','XR','XD','YL')): return [m for m in ms if Ped(K,m).mumkun()]
def kesin(K,ms,f):
    return _kesin(K,ms,f) is True
def _kesin(K,ms,f):
    """f(G)->bool; olası modellerin tüm dünyalarında doğruysa True; hiçbirinde değilse False; karışıksa None"""
    v=set()
    for m in ms:
        P_=Ped(K,m)
        for G,w in P_.W: v.add(bool(f(G)))
    return True if v=={True} else False if v=={False} else None
def soy_gen(satirlar): return {r:y for r,y in satirlar}

# ===================== 0023 · eşeye bağlı · kolay · kromozom şeması · öncüllü =====================
def xy_cizim(x,y0,L,etk,tur):
    b=[f'\\draw[line width=1.1pt,rounded corners=4pt,fill=black,fill opacity=.10] ({x:.2f},{y0:.2f}) rectangle ({x+.3:.2f},{y0+L:.2f});',
       f'\\draw[line width=1.1pt,rounded corners=4pt] ({x:.2f},{y0:.2f}) rectangle ({x+.3:.2f},{y0+L:.2f});',
       f'\\draw[line width=1.6pt] ({x-.03:.2f},{y0+L*(.62 if tur=="X" else .5):.2f})--({x+.33:.2f},{y0+L*(.62 if tur=="X" else .5):.2f});',
       f'\\node[font=\\small\\bfseries] at ({x+.15:.2f},{y0-.3:.2f}) {{{tur}}};']
    if etk:
        yy=y0+L*.32; b.append(f'\\draw[line width=1.6pt] ({x+.32:.2f},{yy:.2f})--({x+.52:.2f},{yy:.2f});\\node[font=\\large\\bfseries] at ({x+.76:.2f},{yy:.2f}) {{{etk}}};')
    return '\n'.join(b)
b23=['\\draw[line width=1pt] (1.3,3.9) circle (.4);','\\draw[line width=1pt] (5.1,3.5) rectangle (5.9,4.3);',
     xy_cizim(.2,.8,2.0,'D','X'),xy_cizim(2.0,.8,2.0,'D','X'),xy_cizim(4.5,.8,2.0,'d','X'),xy_cizim(6.1,.8,1.3,None,'Y')]
SK23=tk('\n'.join(b23),1.35)
def cocuk23(ana,baba):  # ana: X alelleri, baba: ('X?','Y')
    return [(a,b) for a in ana for b in baba]
ch=cocuk23(['XD','XD'],['Xd','Y']); kiz=[c for c in ch if c[1]!='Y']; erk=[c for c in ch if c[1]=='Y']
assert all(set(c)=={'XD','Xd'} for c in kiz) and all(c[0]=='XD' for c in erk) and not any(c[0]=='Xd' and c[1]=='Y' for c in ch) and not any(c==('Xd','Xd') for c in ch)
D23={'I':(False,'Kızlar babadan Xd, anneden XD alır; kızların tamamı taşıyıcıdır, yarısı değil.'),
     'II':(False,'Erkekler X’i anneden alır; anne XDXD olduğundan tüm oğullar normal görmelidir.'),
     'III':(True,'Kızlar XDXd (taşıyıcı), oğullar XDY olur; hiçbir çocuk renk körü (XdXd ya da XdY) olmaz.')}
q('0023','eseye','orta','Eşeye bağlı kalıtım','Cinsiyet kromozomlarındaki alellerden çocukların genotip ve fenotiplerini belirler.','şekilli',
 'şekildeki cinsiyet kromozomlarından çocuk fenotipleri','Erkek X’ini anneden, Y’sini babadan alır; kız babanın X’ini mutlaka alır.','Oğulların renk körlüğünü babadan aldığını sanmak.',
 [A('Genotipleri oku','Anne XDXD, baba XdY’dir.','XDXD × XdY'),A('Çocukları yaz','Kızlar annenin XD’sini ve babanın Xd’sini, oğullar annenin XD’sini ve babanın Y’sini alır.','XDXd, XDY')]+oncad(D23)+[A('Sonuç','Doğru öncül seçilir.',', '.join(k for k in D23 if D23[k][0]))],
 metin=metin_onc('Şekilde, bir çiftin cinsiyet kromozomları ve X kromozomları üzerindeki renk körlüğü geninin alelleri gösterilmiştir (D: normal görme, d: renk körlüğü). Bu gen Y kromozomunda bulunmamaktadır ve mutasyon gerçekleşmemiştir.\nBuna göre bu çiftin çocuklarıyla ilgili,',
   {'I':'Kız çocukların yarısı renk körlüğü aleli taşır.','II':'Erkek çocukların tamamı renk körüdür.','III':'Hiçbir çocuk renk körü olmaz.'},'ifadelerinden hangileri doğrudur?'),
 sekil=SK23,istenen='Doğru olan ifadeler.',ip=['Kızların ve oğulların cinsiyet kromozomlarını hangi ebeveynden aldığını ayrı ayrı yaz.'],bilgi=[B_ESE,B_CAP],
 puf='Erkek çocuk X’ini anneden alır; babanın X’i yalnız kızlara geçer.',
 **onc(D23,[('I',),('II',),('III',),('I','II'),('I','III')]))

# ===================== 0024 · eşeye bağlı · orta · Punnett · iki kuşak =====================
ana=['XH','Xh']; bab=['XH','Y']
cocuklar=[(a,b) for a in ana for b in bab]
kizlar=[c for c in cocuklar if c[1]!='Y']; assert len(kizlar)==2 and all(c[1]=='XH' for c in kizlar)
p_tas=Fr(sum(1 for c in kizlar if 'Xh' in c),len(kizlar)); assert p_tas==Fr(1,2)
# taşıyıcı kız × normal erkek (XHY): hasta erkek XhY
yav=[(a,b) for a in ['XH','Xh'] for b in ['XH','Y']]; p_hasta_erkek=Fr(sum(1 for c in yav if c==('Xh','Y')),4); assert p_hasta_erkek==Fr(1,4)
d24=p_tas*p_hasta_erkek; assert d24==Fr(1,8)
SK24=punnett(['X$^{H}$','X$^{h}$'],['X$^{H}$','Y'],None,ustbas='Annenin gametleri',yanbas='Babanın gametleri',w=1.5,h=.95,sol=1.2,olcek=1.4)
t24=[(Fr(1,16),'Hasta erkek olasılığına (1/4) erkek olma olasılığını (1/2) ayrıca eklemiş.','islem'),(Fr(1,4),'Kızın taşıyıcı olma olasılığını kesin (1) sayıp yalnız ikinci kuşağı hesaplamış.','dikkat'),(Fr(3,8),'Olasılıkları çarpmak yerine 1/4 ile 1/8’i toplamış.','islem'),(Fr(1,2),'Yalnız kızın taşıyıcı olma olasılığını (1/2) sonuç sanmış.','dikkat')]
q('0024','eseye','orta','Eşeye bağlı kalıtım','İki kuşaklı eşeye bağlı çaprazlamada taşıyıcı olasılığını ve ikinci kuşak olasılığını çarparak hesaplar.','şekilli',
 'iki kuşaklı hemofili olasılığı','Önce kızın taşıyıcı olma olasılığı, sonra taşıyıcı × normal erkek çaprazından hasta erkek olasılığı çarpılır.','Kızın taşıyıcı olduğunu kesin saymak.',
 [A('İlk çiftin gametlerini oku','Anne XH ve Xh, baba XH ve Y gameti vermiştir.','XHXh × XHY'),A('Kızın genotipi','Kızlar babadan XH alır; anneden XH ya da Xh gelir. Bu iki genotip eşit olasılıklıdır.','XHXH veya XHXh: 1/2'),A('İkinci kuşak','Taşıyıcı kız (XHXh) ile normal erkek (XHY) çaprazında hasta erkek yalnız XhY’dir.','1/4'),A('Olasılıkları çarp','Kızın taşıyıcı olma olasılığı ile hasta erkek olasılığı çarpılır.','1/2 × 1/4 = 1/8')],
 metin='Şekilde, hemofili bakımından bir çiftin gametleri verilmiştir (XH: normal alel, Xh: hemofili aleli). Bu çiftin kızı, hemofili bakımından normal olan ve ailesinde hemofili öyküsü bulunmayan bir erkekle evleniyor. Hemofili yeni bir mutasyonla ortaya çıkmamaktadır.\nBuna göre kızın evliliğinden doğacak ilk çocuğun hemofili hastası bir erkek olma olasılığı kaçtır?',
 sekil=SK24,istenen='İlk çocuğun hemofili hastası erkek olma olasılığı.',ip=['Kızın hangi gametleri aldığına bak.'],bilgi=[B_ESE,B_CAP],
 puf='Olasılığı iki kuşaklı sorularda önce ara kuşağın genotip olasılığını bul, sonra sonraki çaprazlamayla çarp.',
 **frs(d24,t24))

# ===================== 0025 · eşeye bağlı · orta · Y'ye bağlı · öncüllü olumsuz =====================
KY25={'Baba':('E',1,None,None),'Anne':('K',0,None,None),'Oglan':('E',1,'Anne','Baba'),'Kiz':('K',0,'Anne','Baba')}
assert modeller(KY25,('YL',))==['YL']
YM=Ped(KY25,'YL'); assert YM.dest('Oglan')=={1} and YM.dest('Kiz')=={0}      # oğul özelliği gösterir, kız göstermez; özellik Y'dedir
I25={'I':'Özelliği gösteren erkeğin oğullarının tamamı bu özelliği gösterir.','II':'Çiftin kız çocuklarının hiçbiri bu özelliği göstermez.','III':'Özelliği gösteren oğullar, özellik alelini annelerinden almıştır.'}
# durum: öncül "yanlış" mı (doğru şık = yanlış öncüller)
D25={'I':(False,'Y kromozomu babadan oğula geçer; özelliği gösteren erkeğin tüm oğulları bu özelliği gösterir.'),
     'II':(False,'Kızlarda Y kromozomu bulunmaz; hiçbir kız çocuk bu özelliği göstermez.'),
     'III':(True,'Oğullar Y kromozomunu babasından alır; özellik aleli annenin X kromozomunda bulunmaz.')}
q('0025','eseye','orta','Y’ye bağlı kalıtım','Y kromozomuna bağlı kalıtımın özelliklerini yorumlar.','öncüllü',
 'Y’ye bağlı özellikte oğul ve kız yorumu','Y’ye bağlı özellik babadan oğula geçer, kızlarda görülmez.','Y’ye bağlı özelliğin anneden alındığını ya da kızlara geçtiğini sanmak.',
 [A('Kalıtım biçimini hatırla','Y kromozomu yalnız erkeklerde bulunur ve babadan oğula geçer.','Baba → oğul')]+oncad(D25,hay='doğru',ev='yanlış')+[A('Sonuç','Yanlış olan öncül seçilir.',', '.join(k for k in D25 if D25[k][0]))],
 metin=metin_onc('Y kromozomu üzerinde bulunan ve X kromozomunda karşılığı olmayan bir gen yerindeki aleli taşıyan bir erkek, bu aleli taşımayan bir kadınla evleniyor. Özelliğin mutasyonla yeniden ortaya çıkmadığı bilinmektedir.\nBuna göre bu çiftin çocuklarıyla ilgili,',I25,'ifadelerinden hangileri yanlıştır?'),
 istenen='Yanlış olan ifadeler.',ip=['Y kromozomunun hangi ebeveynden hangi çocuklara geçtiğini düşün.'],bilgi=[B('Cinsiyet kromozomları','Kadın XX, erkek XY · Y kromozomu X kromozomundan küçüktür ve X’teki birçok genin karşılığını taşımaz')],
 puf='Y’ye bağlı kalıtımda özellik yalnız erkekte görülür ve baba–oğul çizgisiyle ilerler.',
 **onc(D25,[('I',),('II',),('III',),('I','III'),('II','III')],fazla='{x}. öncülü yanlış sanmış; oysa doğrudur: {n}',eksik='{x}. öncülü doğru sanmış; oysa yanlıştır: {n}'))

# ===================== 0026 · eşeye bağlı · zor · renk körlüğü + ABO =====================
ab=abo_c(['A','O'],['B','O']); pAB=Fr(ab['AB'],4); assert pAB==Fr(1,4)
xs=[(a,b) for a in ['XD','Xd'] for b in ['XD','Y']]; p_rk=Fr(sum(1 for c in xs if c==('Xd','Y')),4); assert p_rk==Fr(1,4)   # renk körü: yalnız XdY (hasta kız olamaz)
assert not any(c==('Xd','Xd') for c in xs)
d26=pAB*p_rk; assert d26==Fr(1,16)
t26=[(Fr(1,32),'Renk körü erkek olma olasılığına cinsiyet olasılığını (1/2) bir kez daha çarpmış.','islem'),(Fr(1,8),'Renk körlüğü olasılığını 1/2 sanmış (yavruların yarısının hasta olduğunu düşünmüş).','bilgi'),(Fr(3,16),'Renk körü olma yerine renk körü olmayan olasılığını (3/4) kullanmış.','dikkat'),(Fr(1,4),'Yalnız bir özelliğin olasılığını (AB ya da renk körü) vermiş.','dikkat')]
q('0026','eseye','zor','Eşeye bağlı kalıtım ve kan grupları','Eşeye bağlı ve otozomal iki özelliği birlikte değerlendirip olasılıkları çarpar.','hikâyeli',
 'renk körlüğü ve ABO birlikte','İlk çocuktan ABO genotipleri çıkarılır; renk körlüğü olasılığı ayrı hesaplanır ve iki bağımsız özellik çarpılır.','Renk körlüğü olasılığını yalnız erkekler üzerinden ya da 1/2 hesaplamak.',
 [A('ABO genotiplerini bul','O grubu çocuk, A ve B grubu ebeveynlerin O aleli taşıdığını gösterir.','AO × BO'),A('AB olasılığı','AO × BO çaprazında AB yalnız bir kutuda çıkar.','1/4'),A('Renk körlüğü olasılığı','Taşıyıcı anne XDXd ve normal baba XDY: renk körü çocuk yalnız XdY olabilir, hasta kız olamaz.','1/4'),A('Çarp','ABO ile renk körlüğü farklı kromozomlarda olduğundan olasılıklar çarpılır.','1/4 × 1/4 = 1/16')],
 metin='Renk körlüğü, X kromozomu üzerindeki çekinik bir alelle (Xd) belirlenir. A kan grubundan ve renk körlüğü bakımından taşıyıcı olan bir anne ile B kan grubundan ve renk körü olmayan bir babanın ilk çocuğu O kan grubundandır. ABO kan grubu geni ile renk körlüğü geni farklı kromozomlar üzerindedir.\nBuna göre bu çiftin ikinci çocuğunun AB kan grubundan ve renk körü olma olasılığı kaçtır?',
 istenen='İkinci çocuğun AB grubundan ve renk körü olma olasılığı.',ip=['ABO için ebeveyn genotiplerini ilk çocuktan çıkar; renk körlüğü için anne ve babanın X kromozomlarını ayrı yaz.'],bilgi=[B_ABO,B_ESE],
 puf='Farklı kromozomlardaki özellikler bağımsızdır; her özelliğin olasılığı ayrı bulunup çarpılır.',
 **frs(d26,t26))

# ===================== 0027 · soy ağacı · orta · X'e bağlı çekinik · öncüllü =====================
K27={'I-1':('E',0,None,None),'I-2':('K',0,None,None),
 'II-1':('E',0,None,None),'II-2':('K',0,'I-2','I-1'),'II-3':('E',1,'I-2','I-1'),'II-4':('E',0,'I-2','I-1'),'II-5':('K',0,None,None),
 'III-1':('E',1,'II-2','II-1'),'III-2':('K',0,'II-2','II-1'),'III-3':('E',0,'II-2','II-1'),'III-4':('K',0,'II-5','II-4')}
assert modeller(K27,('XR',))==['XR']
M27=('XR',)
D27={'I':(kesin(K27,M27,lambda G:G['I-2']==1 and G['II-2']==1),'I-2’nin hasta oğlu (II-3) vardır ve kendisi sağlıklıdır; II-2’nin hasta oğlu (III-1) vardır ve babası II-1 sağlıklıdır. İkisi de XDXd’dir.'),
     'II':(kesin(K27,M27,lambda G:G['III-2']==1),'III-2’nin babası II-1 XDY’dir, annesi XDXd’dir; III-2 XDXD ya da XDXd olabilir, taşıyıcı olması kesin değildir.'),
     'III':(kesin(K27,M27,lambda G:G['II-3']==G['III-1']),'II-3 ve III-1 erkektir ve ikisi de hastadır; erkekte hastalık için tek alel yeterlidir, ikisi de XdY’dir.')}
assert [v[0] for v in D27.values()]==[True,False,True],[v[0] for v in D27.values()]
XY27={'I-1':(2.55,4.4),'I-2':(4.25,4.4),'II-1':(0,2.4),'II-2':(1.7,2.4),'II-3':(3.4,2.4),'II-4':(5.1,2.4),'II-5':(6.8,2.4),'III-1':(-.55,.4),'III-2':(.85,.4),'III-3':(2.25,.4),'III-4':(5.95,.4)}
SK27=soy_cizim(K27,XY27,[('I-1','I-2'),('II-1','II-2'),('II-4','II-5')],{('I-1','I-2'):3.4,('II-1','II-2'):1.4,('II-4','II-5'):1.4},gen={'I':4.4,'II':2.4,'III':.4},olcek=.9)
q('0027','soy','orta','Soy ağacı','X’e bağlı çekinik soy ağacında kesin taşıyıcıları belirler.','şekilli',
 'X’e bağlı çekinik soy ağacı, kesin taşıyıcılar','Hasta oğlu olan sağlıklı anne kesin taşıyıcıdır; kızın genotipi babasından gelen XD nedeniyle belirsiz kalabilir.','Sağlıklı kızı kesin taşıyıcı ya da kesin sağlam saymak.',
 [A('Genotipleri yaz','Hasta erkekler XdY, sağlıklı erkekler XDY’dir.','II-3, III-1: XdY · II-1, II-4, III-3: XDY'),A('Kesin taşıyıcıları bul','Hasta oğlu olan sağlıklı kadınlar XDXd’dir.','I-2 ve II-2: XDXd')]+oncad(D27)+[A('Sonuç','Kesinlikle doğru öncüller seçilir.',', '.join(k for k in D27 if D27[k][0]))],
 metin=metin_onc('Renk körlüğünün X kromozomu üzerindeki çekinik bir alelle belirlendiği bir ailenin üç kuşaklık soy ağacı şekilde verilmiştir. Erkekler kare, kadınlar daire ile; renk körü bireyler içi dolu sembollerle gösterilmiştir. II-1 ve II-5 bireyleri aileye dışarıdan katılmıştır ve mutasyon gerçekleşmemiştir.\nBuna göre,',
   {'I':'I-2 ve II-2 bireyleri taşıyıcıdır.','II':'III-2 bireyi taşıyıcıdır.','III':'II-3 ve III-1 bireylerinin genotipleri aynıdır.'},'ifadelerinden hangileri kesinlikle doğrudur?'),
 sekil=SK27,istenen='Kesinlikle doğru olan ifadeler.',ip=['Hasta erkeklerin X kromozomunu hangi ebeveynden aldığını düşün; sağlıklı kızların genotipini hangi bilgilerin kesinleştirdiğine bak.'],bilgi=[B_SOY,B_ESE],
 puf='Erkekte hastalık X’i anneden gelir; hasta oğlu olan sağlıklı kadın kesin taşıyıcıdır, ama sağlıklı kızı belirsiz olabilir.',
 **onc(D27,[('I',),('II',),('III',),('I','II'),('I','III')]))

# ===================== 0028 · soy ağacı · zor · olamaz · öncüllü =====================
K28={'I-1':('E',0,None,None),'I-2':('K',1,None,None),
 'II-1':('K',0,'I-2','I-1'),'II-2':('E',0,'I-2','I-1'),'II-3':('K',1,'I-2','I-1'),'II-4':('E',1,None,None),
 'III-1':('E',0,'II-3','II-4'),'III-2':('K',1,'II-3','II-4'),'III-3':('E',0,'II-3','II-4')}
mod28=modeller(K28); assert mod28==['AD','XD'],mod28
D28={'I':('AD' not in mod28,'otozomal baskın kalıtımda hasta heterozigot ebeveynler (I-2, II-3, II-4) sağlıklı çocuk da verebilir; soy ağacına uyar.'),
     'II':('AR' not in mod28,'otozomal çekinikte hasta II-3 ile II-4’ün (aa) bütün çocukları hasta olurdu; sağlıklı III-1 ve III-3 bunu dışlar.'),
     'III':('XR' not in mod28,'X’e bağlı çekinikte hasta annenin (I-2) bütün oğulları hasta olurdu; sağlıklı II-2 bunu dışlar.')}
assert [v[0] for v in D28.values()]==[False,True,True]
XY28={'I-1':(1.7,4.4),'I-2':(3.4,4.4),'II-1':(0,2.4),'II-2':(1.7,2.4),'II-3':(3.4,2.4),'II-4':(5.1,2.4),'III-1':(2.9,.4),'III-2':(4.25,.4),'III-3':(5.6,.4)}
SK28=soy_cizim(K28,XY28,[('I-1','I-2'),('II-3','II-4')],{('I-1','I-2'):3.4,('II-3','II-4'):1.4},gen={'I':4.4,'II':2.4,'III':.4},olcek=.9)
q('0028','soy','zor','Soy ağacı','Soy ağacından olası kalıtım biçimlerini eleyerek olanaksız olanları belirler.','şekilli',
 'olası kalıtım biçimlerinin elenmesi','Hasta ebeveynlerden sağlıklı çocuk baskınlığı, hasta annenin sağlıklı oğlu X’e bağlı çekinikliği dışlar.','Hasta ebeveynlerden sağlıklı çocuğu çekinik kalıtımla açıklamaya çalışmak.',
  [A('Hasta ebeveyni incele','II-3 ve II-4 hasta, çocukları III-1 ve III-3 sağlıklıdır.','Hasta × hasta → sağlıklı'),A('Otozomal çekiniği ele','Çekinik hastalıkta iki hasta ebeveynin çocukları hasta olurdu.','Otozomal çekinik olamaz'),A('X’e bağlı çekiniği ele','Hasta I-2 kadınının her oğlu hasta olurdu; II-2 sağlıklı.','X’e bağlı çekinik olamaz'),A('Baskın kalıtımı sına','Heterozigot hasta ebeveynlerin sağlıklı çocuğu olabilir; otozomal baskın uygundur.','Otozomal baskın olabilir')],
 metin='Tek bir gen çiftiyle belirlenen bir özelliğin üç kuşaklık soy ağacı şekilde verilmiştir. Dolu semboller özelliği gösteren, boş semboller göstermeyen bireyleri; kare erkekleri, daire kadınları simgelemektedir. II-4, aileye dışarıdan katılan bir bireydir ve mutasyon gerçekleşmemiştir.\nBuna göre özelliğin kalıtım biçimi,\nI. otozomal baskın,\nII. otozomal çekinik,\nIII. X’e bağlı çekinik\nbiçimlerinden hangileri olamaz?',
 sekil=SK28,istenen='Olanaksız kalıtım biçimleri.',ip=['Her biçimin kuracağı beklentiyi aileye uygula.'],bilgi=[B_SOY],
 puf='Önce hasta ebeveynlerin çocuklarına, sonra hasta annelerin oğullarına bakarak kalıtım biçimlerini tek tek ele.',
 **onc(D28,[('I',),('II',),('I','II'),('I','III'),('II','III')],fazla='{x}. kalıtım biçiminin olamayacağını sanmış; oysa olabilir: {n}',eksik='{x}. kalıtım biçiminin olabileceğini sanmış; oysa olamaz: {n}'))

# ===================== 0029 · soy ağacı · zor · otozomal çekinik olasılık =====================
K29={'I-1':('E',0,None,None),'I-2':('K',0,None,None),'I-3':('E',0,None,None),'I-4':('K',0,None,None),
 'II-1':('K',1,'I-2','I-1'),'II-2':('E',0,'I-2','I-1'),'II-3':('K',0,'I-4','I-3'),'II-4':('E',1,'I-4','I-3')}
assert modeller(K29,('AR',))==['AR']
Pd=Ped(K29,'AR'); assert Pd.dest('I-1')=={1} and Pd.dest('I-4')=={1} and Pd.dest('II-2')=={0,1} and Pd.dest('II-3')=={0,1}
p2=sum(w for G,w in Pd.W if G['II-2']==1)/Pd.T(); p3=sum(w for G,w in Pd.W if G['II-3']==1)/Pd.T(); assert (p2,p3)==(Fr(2,3),Fr(2,3))
K29b=dict(K29); K29b['III-X']=('K',1,'II-3','II-2'); Pb=Ped(K29b,'AR'); pc=Pb.T()/Pd.T(); assert pc==Fr(1,9)
d29=pc*Fr(1,2); assert d29==Fr(1,18)
XY29={'I-1':(0,4.4),'I-2':(1.6,4.4),'I-3':(4.4,4.4),'I-4':(6.0,4.4),'II-1':(0,2.4),'II-2':(1.6,2.4),'II-3':(4.4,2.4),'II-4':(6.0,2.4)}
SK29=soy_cizim(K29,XY29,[('I-1','I-2'),('I-3','I-4'),('II-2','II-3')],{('I-1','I-2'):3.4,('I-3','I-4'):3.4},gen={'I':4.4,'II':2.4},olcek=.95)
t29=[(Fr(1,36),'Kız olma ve hasta olma olasılığından ayrı bir 1/2 çarpanı daha eklemiş.','islem'),(Fr(1,9),'Hasta olma olasılığını bulmuş ama kız çocuk olma olasılığını (1/2) çarpmamış.','dikkat'),(Fr(1,6),'II-2 ve II-3’ün taşıyıcı olma olasılıklarından yalnız birini kullanmış (2/3 × 1/4).','islem'),(Fr(1,4),'II-2 ve II-3’ü kesin taşıyıcı sanıp yalnız Aa × Aa olasılığını (1/4) vermiş.','bilgi')]
q('0029','soy','zor','Soy ağacı','Soy ağacından taşıyıcı olasılıklarını çıkarıp sonraki çocuğun cinsiyetli olasılığını hesaplar.','şekilli',
 'otozomal çekinik, iki aile, evlilik','Hasta çocuğu olan sağlıklı ebeveynler Aa’dır; onların sağlıklı çocuğunun taşıyıcı olma olasılığı 2/3’tür.','Sağlıklı bireyleri kesin taşıyıcı saymak.',
 [A('Ebeveynleri belirle','Her ailede hasta çocuk (aa) vardır; dört ebeveynin hepsi Aa’dır.','I-1, I-2, I-3, I-4: Aa'),A('Taşıyıcı olasılıkları','Aa × Aa çocuğu sağlıklıysa AA (1/3) ya da Aa (2/3) olur.','II-2: 2/3 · II-3: 2/3'),A('Hasta çocuk olasılığı','Ancak ikisi de Aa ise çocuk 1/4 olasılıkla aa olur.','2/3 × 2/3 × 1/4 = 1/9'),A('Cinsiyeti ekle','Çocuğun kız olma olasılığı bağımsızdır ve 1/2’dir.','1/9 × 1/2 = 1/18')],
 metin='Otozomal çekinik bir hastalığa ait iki ailenin soy ağacı şekilde gösterilmiştir. Erkekler kare, kadınlar daire ile; hastalar içi dolu sembollerle gösterilmiştir. II-2 ve II-3 bireyleri evlenmiştir ve mutasyon gerçekleşmemiştir.\nBuna göre bu çiftin doğacak ilk çocuğunun hasta bir kız olma olasılığı kaçtır?',
 sekil=SK29,istenen='İlk çocuğun hasta kız olma olasılığı.',ip=['Hasta çocuğu olan sağlıklı ebeveynlerin genotipini yaz; evlenen sağlıklı çocukların taşıyıcı olma olasılığını ayrı ayrı bul.'],bilgi=[B_SOY,B_KOS],
 puf='Sağlıklı bir bireyin taşıyıcı olma olasılığını hesaplarken payda yalnız sağlıklı yavrulardır: 2/3.',
 **frs(d29,t29))

# ===================== 0030 · soy ağacı · zor · otozomal baskın · kesin heterozigot =====================
K30={'I-1':('E',1,None,None),'I-2':('K',1,None,None),
 'II-1':('K',0,'I-2','I-1'),'II-2':('E',1,'I-2','I-1'),'II-3':('K',0,None,None),'II-4':('K',1,'I-2','I-1'),
 'III-1':('E',1,'II-3','II-2'),'III-2':('K',0,'II-3','II-2')}
M30=modeller(K30,('AR','AD')); assert M30==['AD']
D30={'I':(kesin(K30,M30,lambda G:G['II-1']==G['III-2']),'II-1 ve III-2 sağlıklıdır; baskın kalıtımda sağlıklı bireyler çekinik homozigottur (aa).'),
     'II':(kesin(K30,M30,lambda G:G['III-1']==1),'III-1 hastadır ve annesi II-3 sağlıklı (aa) olduğundan çekinik aleli annesinden almıştır; genotipi Aa’dır.'),
     'III':(kesin(K30,M30,lambda G:G['II-4']==1),'II-4 hasta olduğundan AA ya da Aa olabilir; heterozigot olduğu kesin değildir.')}
assert [v[0] for v in D30.values()]==[True,True,False]
XY30={'I-1':(1.7,4.4),'I-2':(3.4,4.4),'II-1':(0,2.4),'II-2':(1.7,2.4),'II-3':(3.4,2.4),'II-4':(5.1,2.4),'III-1':(1.9,.4),'III-2':(3.2,.4)}
SK30=soy_cizim(K30,XY30,[('I-1','I-2'),('II-2','II-3')],{('I-1','I-2'):3.4,('II-2','II-3'):1.4},gen={'I':4.4,'II':2.4,'III':.4},olcek=.9)
q('0030','soy','zor','Soy ağacı','Soy ağacından baskın kalıtımı çıkarıp hangi bireylerin genotipinin kesin olduğunu belirler.','şekilli',
 'otozomal baskın soy ağacı, kesin genotipler','Hasta ebeveynlerin sağlıklı çocuğu varsa özellik baskındır; hasta bireyin kesin heterozigot olması için sağlıklı (aa) eşinden ya da sağlıklı yavrusundan kanıt gerekir.','Hasta bireyin heterozigot olduğunu varsaymak.',
 [A('Kalıtım biçimini bul','Hasta I-1 ve I-2’nin sağlıklı kızı II-1 vardır; çekinik olsaydı hepsi hasta olurdu.','Otozomal baskın'),A('Sağlıklıların genotipi','Baskın kalıtımda sağlıklı bireyler çekinik homozigottur.','II-1, II-3, III-2: aa')]+oncad(D30)+[A('Sonuç','Kesinlikle doğru öncüller seçilir.',', '.join(k for k in D30 if D30[k][0]))],
 metin=metin_onc('Bir özellik, otozomal kromozomlardaki tek bir gen çiftiyle belirlenmektedir ve bu özelliğe ait üç kuşaklık soy ağacı şekilde verilmiştir. Özelliği gösterenler siyaha boyalı, göstermeyenler boş sembollerle; erkekler kare, kadınlar daire ile gösterilmiştir. II-3 aileye dışarıdan katılmıştır ve mutasyon gerçekleşmemiştir.\nBuna göre,',
   {'I':'II-1 ve III-2 bireylerinin genotipleri aynıdır.','II':'III-1 bireyi heterozigottur.','III':'II-4 bireyi heterozigottur.'},'ifadelerinden hangileri kesinlikle doğrudur?'),
 sekil=SK30,istenen='Kesinlikle doğru olan ifadeler.',ip=['Önce kalıtım biçimini aile ilişkilerinden çıkarmayı dene.'],bilgi=[B_SOY,B_KAV],
 puf='Baskın özellikte sağlıklı olan herkes çekinik homozigottur; hasta birey, sağlıklı bir ebeveyni ya da yavrusu varsa kesin heterozigottur.',
 **onc(D30,[('I',),('II',),('III',),('I','II'),('I','III')]))

# ===================== 0031 · mutasyon · kolay · öncüllü =====================
D31={'I':(True,'Mutasyon, DNA’nın nükleotit dizisinde ya da kromozom yapısında/sayısında meydana gelen kalıcı değişikliktir.'),
     'II':(False,'Vücut (somatik) hücrelerinde olan mutasyonlar eşeyli üremeyle yavrulara aktarılmaz; yalnız gamet hücresindeki mutasyonlar aktarılabilir.'),
     'III':(True,'Gamet hücrelerinde oluşan mutasyonlar döllenmeyle zigota geçer ve yavrulara aktarılabilir.')}
q('0031','mut','kolay','Mutasyon','Mutasyonun tanımını ve kalıtsallığını yorumlar.','öncüllü',
 'mutasyon ifadeleri','Mutasyon DNA’daki kalıcı değişikliktir; yalnız gamet hücresindeki mutasyonlar yavrulara aktarılır.','Her mutasyonun yavrulara geçtiğini sanmak.',
 [A('Mutasyonu tanımla','Mutasyon, genetik bilgideki kalıcı değişikliktir.','Kalıcı değişiklik')]+oncad(D31)+[A('Sonuç','Doğru öncüller seçilir.',', '.join(k for k in D31 if D31[k][0]))],
 metin=metin_onc('Mutasyonlar, canlılarda genetik çeşitliliğe yol açan olaylardan biridir. Bir öğrenci, mutasyonlarla ilgili notlar alırken aşağıdaki ifadeleri yazıyor.\nBuna göre,',
   {'I':'Mutasyon, DNA’da meydana gelen kalıcı bir değişikliktir.','II':'Vücut hücrelerinde meydana gelen mutasyonlar, eşeyli üremeyle yavrulara aktarılır.','III':'Gamet hücrelerinde meydana gelen mutasyonlar yavrulara aktarılabilir.'},'ifadelerinden hangileri doğrudur?'),
 istenen='Doğru olan ifadeler.',ip=['Hangi hücrelerdeki değişikliğin döllenmeyle sonraki nesle geçebileceğini düşün.'],bilgi=[B('Mutasyon','Mutasyon, genetik bilgide meydana gelen kalıcı değişikliktir')],
 puf='Mutasyonun yavruya geçmesi için gamet hücresinde olması gerekir.',
 **onc(D31,[('I',),('II',),('I','II'),('I','III'),('II','III')]))

# ===================== 0032 · mutasyon · orta · tablo deney · öncüllü =====================
T32=[('1','14','42','30'),('2','6','24','31')]
D32={'I':(False,'Çelikle üretilen bitkiler genetik olarak özdeştir; gruplar arasında genotip farkı yoktur, fark çevre koşulundan (ışık) kaynaklanır.'),
     'II':(True,'Genotipleri aynı bitkilerde yalnız ışık süresi farklıdır; çevre etkisiyle oluşan, genotipi değiştirmeyen fenotip farkı modifikasyondur.'),
     'III':(True,'Aynı ortamda yetiştirilen çelik bitkilerin boyları benzer çıkmıştır; ışığa bağlı boy farkı kalıtılmamıştır, yani kalıtsal değildir.')}
q('0032','mut','orta','Modifikasyon','Deney verilerinden modifikasyon ile kalıtsal değişimi ayırt eder.','tablo',
 'ışık süresi ve boy: modifikasyon deneyi','Genotipleri özdeş bireylerde çevreye bağlı fark modifikasyondur ve aynı ortamda yetiştirilince kaybolur.','Çevre kaynaklı boy farkının kalıtsal olduğunu sanmak.',
 [A('Değişkenleri ayır','Bağımsız değişken ışık süresi, bağımlı değişken boydur; genotip aynı tutulmuştur.','Işık → boy')]+oncad(D32)+[A('Sonuç','Doğru öncüller seçilir.',', '.join(k for k in D32 if D32[k][0]))],
 metin=metin_onc('Genetik olarak özdeş bitkiler iki gruba ayrılıyor; diğer koşullar aynıyken 1. gruba günde 14 saat, 2. gruba günde 6 saat ışık veriliyor ve 30 gün sonra boylar ölçülüyor. Her gruptan alınan çelikler, günde 10 saat ışık alan ortak bir ortamda yetiştirilip 30 gün sonra ölçülüyor. Sonuçlar tabloda gösterilmiştir.\nBuna göre,',
   {'I':'Gruplar arasındaki boy farkı genotip farkından kaynaklanmıştır.','II':'Gruplar arasındaki boy farkı, ışık süresinin etkisiyle oluşan bir modifikasyondur.','III':'Çelik bitkilerin boylarının benzer olması, ışığa bağlı boy farkının kalıtsal olmadığını gösterir.'},'ifadelerinden hangileri doğrudur?'),
 sekil=tablo_svg(['Grup','Boy (cm)','Çeliklerin boyu (cm)'],[[r[0],r[2],r[3]] for r in T32]),
 istenen='Doğru olan ifadeler.',ip=['Çeliklerin aynı ortamda yetiştirilince boylarının nasıl çıktığını yorumla.'],bilgi=[B('Modifikasyon','Modifikasyon, çevre koşullarının etkisiyle fenotipte oluşan değişimdir')],
 puf='Genotipleri aynı bireylerdeki çevre kaynaklı fark modifikasyondur; ortam eşitlenince ortadan kalkar.',
 **onc(D32,[('I',),('II',),('III',),('I','II'),('II','III')]))

# ===================== 0033 · mutasyon · kolay · varyasyon kaynakları · olumsuz =====================
V33=[('Mayozda homolog kromozomlar arasında parça değişimi (krossing-over) olması',True,'krossing-over yeni alel birleşimleri oluşturur, genetik çeşitliliği artırır.'),
     ('Mayozda homolog kromozom çiftlerinin gametlere rastgele dağılması',True,'bağımsız dağılım farklı kromozom birleşimleri verir.'),
     ('Döllenmede hangi gametlerin birleşeceğinin şansa bağlı olması',True,'rastgele döllenme farklı genotipler oluşturur.'),
     ('DNA’nın nükleotit dizisini kalıcı olarak değiştiren mutasyonların oluşması',True,'mutasyon yeni aleller meydana getirir.'),
     ('Mitoz bölünmeyle oluşan hücrelerin ana hücreyle aynı genetik bilgiyi taşıması',False,'mitoz genetik olarak özdeş hücre oluşturur; varyasyon sağlamaz.')]
q('0033','mut','kolay','Genetik varyasyon','Eşeyli üremede genetik çeşitliliği sağlayan olayları ayırt eder.','düz',
 'varyasyon kaynakları, yol açmayan olay','Varyasyon kaynakları: krossing-over, bağımsız dağılım, rastgele döllenme, mutasyon; mitoz özdeş hücre verir.','Mitozu varyasyon kaynağı saymak.',
 [A('Varyasyon kaynaklarını say','Mayozda krossing-over ve bağımsız dağılım, döllenme ve mutasyon çeşitlilik sağlar.','4 kaynak'),A('Şıkları ele','İlk dört olay yeni alel ya da kromozom birleşimleri oluşturur.','4 olay varyasyon sağlar'),A('Mitozu değerlendir','Mitoz, ana hücreyle aynı genetik bilgiyi taşıyan hücreler verir.','Özdeş hücre'),A('Sonuç','Varyasyona yol açmayan olay mitozdur.','Mitoz')],
 metin='Bir araştırmacı, eşeyli üreyen canlılarda aynı türün bireyleri arasındaki genetik çeşitliliğin (varyasyonun) kaynaklarını incelemektedir. Aşağıda verilen olaylardan yalnızca biri bu çeşitliliğe yol açmaz.\nBuna göre aşağıdakilerden hangisi genetik çeşitliliğe yol açan bir olay değildir?',
 istenen='Genetik çeşitliliğe yol açmayan olay.',ip=['Varyasyonun yeni alel ya da yeni alel birleşimi demek olduğunu hatırla; her şıkta bunun olup olmadığına bak.'],bilgi=[B('Genetik çeşitlilik','Genetik çeşitlilik, bireyler arasında alel ya da alel birleşimi farkı bulunması demektir')],
 puf='Mayoz ve döllenme çeşitlilik sağlar; mitoz ise genetik olarak özdeş hücreler üretir.',
 **tek([V33[0],V33[1],V33[4],V33[2],V33[3]],hedef=False))

# ===================== 0034 · mutasyon · orta · hikâyeli · mutasyon ve modifikasyon birlikte =====================
S34=[('Beyaz çiçekli dal bir mutasyonla, gölgedeki çiçeklerin solukluğu ise modifikasyonla oluşmuştur.',True,'beyaz dalın alel değişikliği kalıcıdır ve mitozla çelik bitkilere geçer; solukluk çevre etkisidir.'),
     ('Beyaz çiçekli dal, çelikle aktarıldığı için modifikasyonla oluşmuştur.',False,'modifikasyon kalıtsal değildir; çelikle aktarılması mutasyonun mitozla kopyalandığını gösterir.'),
     ('Gölgedeki soluk çiçekler, çelikle üretilecek yeni bitkilere de aynı soluklukla aktarılır.',False,'solukluk çevre etkisidir; aynı ortamda yetişen yeni bitkiler soluk olmaz.'),
     ('Beyaz çiçekli dalın hücreleri ile kırmızı çiçekli dalların hücrelerinin genotipi aynıdır.',False,'beyaz dalda alel değişmiştir; genotip kırmızı dallardan farklıdır.'),
     ('Çiçek renginde görülen iki farklılık da DNA’daki kalıcı bir değişikliğin sonucudur.',False,'gölgedeki solukluk DNA değişikliği değil, çevre etkisidir.')]
q('0034','mut','orta','Mutasyon ve modifikasyon','Bir bitkideki iki farklı değişimi mutasyon ve modifikasyon olarak ayırt eder.','hikâyeli',
 'tek dalda mutasyon, gölgede modifikasyon','Kalıcı alel değişikliği mutasyondur ve mitozla kopyalanır; çevreye bağlı fark modifikasyondur ve kalıtılmaz.','Çelikle aktarılan her değişimi modifikasyon sanmak.',
 [A('Beyaz dalı yorumla','Alel değişikliği hücrelerde kalıcıdır ve mitozla çelikle yeni bitkiye geçer.','Mutasyon'),A('Solukluğu yorumla','Gölgede kalma çevre etkisidir; DNA değişmez ve yeni bitkiye aktarılmaz.','Modifikasyon'),A('İfadeleri ele','Mutasyon ve modifikasyon tanımlarına uyan ifade belirlenir.','Doğru: mutasyon ve modifikasyon ayrımı'),A('Sonuç','İki olay farklı nedenlerle ortaya çıkmıştır.','Mutasyon + modifikasyon')],
 metin='Bir bitki yetiştiricisi, bütün çiçekleri kırmızı olan bir bitkinin yalnızca bir dalında beyaz çiçekler açtığını fark ediyor. Bu daldan alınan çelikle üretilen bitkilerin hepsinde beyaz çiçekler açıyor. Aynı bitkinin gölgede kalan kırmızı çiçekleri ise güneş gören çiçeklere göre daha soluk renkli. Beyaz rengin, dalın hücrelerindeki tek bir alel değişikliğinden kaynaklandığı belirlenmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 istenen='Doğru olan ifade.',ip=['Hangi değişimin çevre koşulundan, hangisinin kalıcı alel değişikliğinden kaynaklandığını ayırarak her ifadeyi sına.'],bilgi=[B_MUT],
 puf='Kalıcı alel değişikliği mutasyondur ve mitozla kopyalanır; çevre kaynaklı değişim modifikasyondur ve kalıtılmaz.',
 **tek([S34[1],S34[2],S34[3],S34[0],S34[4]],hedef=True))

bitir(P,'kalitimiki',UK)
