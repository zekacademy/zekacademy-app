"""TYT Fizik · Basınç ikinci paket (20 soru, kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici değer assert edilir.
Öncüllü sorularda her yargının doğru/yanlış değeri ve gerekçesi onc() çağrısında TEK yerde (truth, ex) tanımlanır; adımlar ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,random
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
H.KONU='Basınç'
P=Parti('basinciki','Basınç','fiz|Basınç',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (basınç, yalnız mantık) · MEB 10. sınıf fizik'
TIP={'cevir':('fz-bs2-kati-konum','Cismi çevirince katı basıncı'),
     'kes':('fz-bs2-kesme','Prizmayı kesince ve yeniden dizince basınç'),
     'tab':('fz-bs2-kati-tablo','Katı basıncını karşılaştırma'),
     'sil':('fz-bs2-silindir','Homojen prizma ve silindirde P = d·g·h'),
     'yigin':('fz-bs2-yigin','Üst üste konan bloklarda iki yüzeyin basıncı'),
     'kap':('fz-bs2-kap','Kap şekli ve taban basıncı–kuvveti'),
     'der':('fz-bs2-derinlik','Aynı sıvıda iki derinlik arasındaki basınç farkı'),
     'u':('fz-bs2-uboru','U borusunda özkütle bulma'),
     'kat':('fz-bs2-katman','Üç katmanlı sıvıda ara nokta basıncı'),
     'bil':('fz-bs2-bilesik','Bileşik kapta musluk açılınca akış yönü'),
     'havuz':('fz-bs2-havuz','Sıvı basıncının derinlik ve yönle ilişkisi'),
     'hid':('fz-bs2-hidrolik','Hidrolik pres: kuvvet, yer değiştirme, iş'),
     'fren':('fz-bs2-fren','Hidrolik fren sistemi'),
     'tor':('fz-bs2-torricelli','Torricelli deneyinde tüp değişiklikleri'),
     'man':('fz-bs2-manometre','Açık uçlu manometre'),
     'bar':('fz-bs2-barometre','Barometre ve yükselti'),
     'gaz':('fz-bs2-gaz','Kapalı kapta gaz basıncı'),
     'ber':('fz-bs2-bernoulli-boru','Kesit, hız ve basınç ilişkisi'),
     'gun':('fz-bs2-bernoulli-gunluk','Bernoulli ilkesinin günlük örnekleri'),
     'hal':('fz-bs2-hal-degisimi','Basıncın kaynama sıcaklığına etkisi')}
def K(n,t,alt,fikir,tuzak,z,kalip,adim):
    tid,tad=TIP[t]; kart(f'K-FZBS2-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tid,tad,KY)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
DIM='{Stealth[length=1.6mm,width=1.4mm]}-{Stealth[length=1.6mm,width=1.4mm]}'
def sk(*l,sc=1.0): return tikz_svg(HEAD.replace('[','[scale=%s,'%sc,1)+'\n'.join(l)+TAIL)
ROM={1:'I',2:'II',3:'III'}
def lab(s):
    s=sorted(s); return 'Yalnız '+ROM[s[0]] if len(s)==1 else (ROM[s[0]]+' ve '+ROM[s[1]] if len(s)==2 else 'I, II ve III')
def parse(l):
    return {n for n,r in ROM.items() if r in l.replace('Yalnız','').replace(',',' ').replace('ve',' ').split()}
def onc(no,truth,sira,ex,kok,**k):
    """truth: doğru yargı kümesi; ex[n]: yargının doğru/yanlış olmasının gerekçesi (olgu cümlesi, çeldirici dili içermez)."""
    for l in sira: assert lab(parse(l))==l,l
    assert lab(truth) in sira and len(set(sira))==5
    yan=[]
    for l in sira:
        if l==lab(truth): continue
        S=parse(l); p=[]
        for n in sorted(S-truth): p.append(f'{ROM[n]}. yargıyı doğru saymış; oysa bu yargı yanlıştır: {ex[n]}')
        for n in sorted(truth-S): p.append(f'{ROM[n]}. yargıyı yanlış saymış; oysa bu yargı doğrudur: {ex[n]}')
        yan.append((l,' '.join(p),'bilgi'))
    ad=k.pop('ad_on',[])+[A(f'{ROM[n]}. yargıyı sına',ex[n],'doğru' if n in truth else 'yanlış') for n in (1,2,3)]
    ad.append(A('Sonucu yaz','Doğru olan yargıları birleştir.','Doğru olanlar: '+lab(truth)))
    assert 3<=len(ad)<=7
    q(no,ad=ad,metin=kok,dogru=lab(truth),yan=yan,sira=sira,kalip=k.pop('kalip','öncüllü'),**k)
def q(no,**k):
    assert len(k['ip'])==1
    ad=k.pop('ad'); mk(P,no,ad=ad,adim=len(ad),**k)
def kutu(x,y,w,h,d,s=.1,lw=True):
    W=w*s;H=h*s;dx=d*s*.5;dy=d*s*.35
    o=[f'\\draw[thick,fill=gray!14] ({x:.2f},{y+H:.2f}) -- ({x+dx:.2f},{y+H+dy:.2f}) -- ({x+W+dx:.2f},{y+H+dy:.2f}) -- ({x+W:.2f},{y+H:.2f}) -- cycle;',
       f'\\draw[thick,fill=gray!45] ({x+W:.2f},{y:.2f}) -- ({x+W+dx:.2f},{y+dy:.2f}) -- ({x+W+dx:.2f},{y+H+dy:.2f}) -- ({x+W:.2f},{y+H:.2f}) -- cycle;',
       f'\\draw[thick,fill=gray!26] ({x:.2f},{y:.2f}) rectangle ({x+W:.2f},{y+H:.2f});']
    return o,(W,H,dx,dy)
S7=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def pick(*i): return [S7[j] for j in i]

# ================= 01 · katı basıncı, cismi çevirme · kolay · öncüllü =================
K(1,'cevir','Katı Basıncı','Aynı cismin farklı yüzleri üzerinde durmasında basınç kuvveti (ağırlık) değişmez, temas alanı değişir; basınç alanla ters orantılıdır.','Basınç kuvveti ile basıncı karıştırmak; en büyük yüzü “en büyük basınç” sanmak.','kolay','öncüllü',3)
blk=[('K',20,5,10),('L',20,10,5),('M',10,20,5)]   # (ad, ön genişlik, yükseklik, derinlik) cm
AL={n:w*d for n,w,h,d in blk}; assert AL=={'K':200,'L':100,'M':50} and AL['L']/AL['M']==2 and AL['K']==max(AL.values())
o=[]; x=0.0
for n,w,h,d in blk:
    b,(W,H,dx,dy)=kutu(x,0,w,h,d); o+=b
    o.append(f'\\node[below,font=\\scriptsize] at ({x+W/2:.2f},0) {{${w}$ cm}};')
    o.append(f'\\node[left,font=\\scriptsize] at ({x:.2f},{H/2:.2f}) {{${h}$ cm}};')
    o.append(f'\\node[right,font=\\scriptsize,inner sep=1.5pt] at ({x+W+dx+.02:.2f},{H/2+dy:.2f}) {{${d}$ cm}};')
    o.append(f'\\node[font=\\small\\bfseries] at ({x+W/2:.2f},-.62) {{{n}}};')
    x+=W+dx+1.95
o.append(f'\\draw[thick] (-.7,0) -- ({x-.9:.2f},0);')
SK1=sk(*o)
onc('0001',{1,3},pick(0,1,4,5,6),
 {1:'Blok konum değiştirse de ağırlığı sabittir; yatay masada basınç kuvveti ağırlığa eşit olduğundan üç konumda da aynıdır.',
  2:'Basınç P = F ÷ A’dır; kuvvet sabitken alanı en küçük olan M konumunda (50 cm²) basınç en büyüktür; K konumunda (200 cm²) en küçüktür.',
  3:'Temas alanları L için 5 × 20 = 100 cm², M için 5 × 10 = 50 cm²’dir; alan yarıya inince basınç iki katına çıkar, P_M = 2 · P_L.'},
 'Fizik laboratuvarında homojen, dikdörtgenler prizması biçimindeki bir ahşap blok, yatay masa üzerinde şekilde K, L ve M ile gösterilen üç farklı konumda sırayla durduruluyor. Her konumda bloğun ayrıtlarının uzunlukları şekilde verilmiştir. Blok her konumda dengededir, masa bloğu çökertmeyecek kadar serttir ve yüzeyler tamamen temas etmektedir. Öğrenci, bloğun masaya uyguladığı basınç kuvveti ile basıncı konumlara göre karşılaştırıyor.\nBuna göre,\nI. Bloğun masaya uyguladığı basınç kuvveti üç konumda da eşittir.\nII. Bloğun masaya uyguladığı basınç en büyük K konumundadır.\nIII. M konumundaki basınç, L konumundaki basıncın iki katıdır.\nyargılarından hangileri doğrudur?',
 tipId=TIP['cevir'][0],tip=TIP['cevir'][1],z='kolay',alt='Katı Basıncı',kaz='Aynı cismin farklı yüzeyleri üzerinde durduğunda basınç kuvvetinin sabit, basıncın temas alanıyla ters orantılı değiştiğini yorumlar.',
 kart='K-FZBS2-01 (cismi çevirme) · öncüllü',istenen='Doğru olan yargılar.',ip=['Konum değişirken bloğun ağırlığının ve masaya değen yüzün büyüklüğünün nasıl değiştiğine ayrı ayrı bak.'],
 bilgi=[B('Katı basıncı','P = F ÷ A; yatay zeminde F cismin ağırlığıdır, A temas eden yüzün alanıdır. Kuvvet sabitken alan küçülürse basınç artar. Örnek: 60 N’luk bir kitap 0,03 m² alanla durursa P = 60 ÷ 0,03 = 2000 Pa; yan yatırınca alan 0,01 m² olursa P = 6000 Pa')],
 puf='Cismi çevirince ağırlık (basınç kuvveti) değişmez; yalnız temas alanı, dolayısıyla basınç değişir.',sekil=SK1)

# ================= 02 · tablo, kişi–ayakkabı · kolay =================
K(2,'tab','Katı Basıncı','Basınç P = F ÷ A; her satırda kuvvet ve alandan basınç hesaplanır, sonra en büyük/en küçük karşılaştırılır.','Yalnız ağırlığa ya da yalnız alana bakıp karar vermek; cm²’yi m²’ye çevirirken oranı bozmak.','kolay','tablo',3)
ki=[('Ali','bot',400,200),('Ayşe','kar ayakkabısı',600,1500),('Can','kayak',800,1600)]
pr={n:Fr(F,1)/Fr(A_,10**4) for n,_,F,A_ in ki}
assert pr=={'Ali':20000,'Ayşe':4000,'Can':5000} and pr['Ali']/pr['Ayşe']==5 and pr['Ali']/pr['Can']==4 and Fr(800,400)==2 and Fr(1500,200)==Fr(15,2) and pr['Ayşe']/pr['Ali']==Fr(1,5)
SK2=tablo_svg(['Kişi','Kullandığı araç','Ağırlık (N)','Kar ile toplam temas alanı (cm²)'],[[n,a,F,A_] for n,a,F,A_ in ki])
q('0002',tipId=TIP['tab'][0],tip=TIP['tab'][1],z='kolay',alt='Katı Basıncı',kaz='Ağırlık ve temas alanı verilen kişilerin yüzeye uyguladığı basınçları hesaplayıp karşılaştırır.',kalip='tablo',
 kart='K-FZBS2-02 (basınç karşılaştırma tablosu) · kar, bot–kar ayakkabısı–kayak',
 metin='Kış tatilinde karla kaplı, düz ve yatay bir alanda Ali, Ayşe ve Can birbirinden farklı araçlarla yürüyüş yapıyor. Aşağıdaki tabloda üç kişinin ağırlıkları ile her birinin ayakta dururken kar yüzeyine temas eden toplam alanı (iki bot, iki kar ayakkabısı ya da iki kayak) verilmiştir. Kar, kişilerin ağırlığını bir kuvvet olarak taşımakta ve yüzeyi yatay kalmaktadır.\nBuna göre, kara en büyük basıncı uygulayan kişinin basıncı, en küçük basıncı uygulayan kişinin basıncının kaç katıdır?',
 sekil=SK2,dogru=5,yan=[(0.2,'Oranı ters kurmuş: en küçük basıncı en büyüğe bölmüş (4000 ÷ 20000).','dikkat'),(2,'Yalnız ağırlıklara bakmış: en ağır (800 N) ile en hafif (400 N) kişinin ağırlık oranını almış; alanı hesaba katmamış.','bilgi'),(4,'Can’ı en küçük basınçlı sanmış (Ali ÷ Can = 20000 ÷ 5000); Ayşe’nin basıncını (4000 Pa) hesaplamamış.','dikkat'),(7.5,'Yalnız alanlara bakmış: Ayşe’nin alanını Ali’nin alanına bölmüş (1500 ÷ 200); kuvveti hesaba katmamış.','bilgi')],
 istenen='En büyük basıncın en küçük basınca oranı.',ip=['Her kişi için ağırlığı temas alanına bölüp basıncı ayrı ayrı bul; alanları aynı birime çevirmeyi unutma.'],
 bilgi=[B('Basınç','P = F ÷ A; yatay zeminde F kişinin ağırlığıdır. 1 cm² = 10⁻⁴ m². Örnek: 90 N ağırlıklı bir cisim 30 cm² alanla yere basarsa P = 90 ÷ 0,003 = 30 000 Pa')],
 ad=[A('Alanları metrekareye çevir','1 cm² = 10⁻⁴ m² olduğundan alanlar m² cinsine çevrilir.','200 cm² = 0,02 m² · 1500 cm² = 0,15 m² · 1600 cm² = 0,16 m²'),
     A('Basınçları hesapla','Her kişi için P = F ÷ A uygula.','Ali: 400 ÷ 0,02 = 20 000 Pa · Ayşe: 600 ÷ 0,15 = 4000 Pa · Can: 800 ÷ 0,16 = 5000 Pa'),
     A('En büyük ve en küçüğü seç','En büyük Ali’nin, en küçük Ayşe’nin basıncıdır.','20 000 ÷ 4000 = 5')],
 puf='Basınç yalnız ağırlığa ya da yalnız alana değil, ikisinin oranına bağlıdır; hepsini P = F ÷ A ile hesapla.')

# ================= 03 · kesme · orta · öncüllü =================
K(3,'kes','Katı Basıncı','Homojen prizmada P = d·g·h; yatay kesimde yükseklik, düşey kesimde ağırlık ve alan aynı oranda değişir; üst üste koyma alanı yarıya indirir.','Yarı parçayı atınca basıncın da yarıya ineceğini sanmak (düşey kesimde alan da yarıya iner).','orta','öncüllü',3)
W0,A0,h0=1.0,1.0,1.0   # ağırlık, alan, yükseklik (göreli)
pK=(W0/2)/A0; pL=(W0/2)/(A0/2); pM=W0/(A0/2)
assert pK==.5 and pL==1 and pM==2
def blok2(x,tip):
    o=[f'\\draw[thick,fill=gray!18] ({x},0) rectangle ({x+1.8},1.3);']
    if tip=='y': o+= [f'\\fill[gray!60] ({x},.65) rectangle ({x+1.8},1.3);',f'\\draw[thick,dashed] ({x-.15},.65) -- ({x+1.95},.65);',f'\\draw[thick,{ARR}] ({x+.9},1.4) -- ({x+.9},1.95);',f'\\node[font=\\scriptsize] at ({x+.9},2.15) {{atılıyor}};']
    if tip=='d': o+= [f'\\fill[gray!60] ({x+.9},0) rectangle ({x+1.8},1.3);',f'\\draw[thick,dashed] ({x+.9},-.15) -- ({x+.9},1.45);',f'\\draw[thick,{ARR}] ({x+1.9},.65) -- ({x+2.75},.65);',f'\\node[font=\\scriptsize,anchor=south west] at ({x+1.95},.72) {{atılıyor}};']
    if tip=='u': o+= [f'\\fill[gray!60] ({x+.9},0) rectangle ({x+1.8},1.3);',f'\\draw[thick,dashed] ({x+.9},-.15) -- ({x+.9},1.45);',f'\\draw[thick,{ARR}] ({x+1.45},1.45) .. controls ({x+1.4},2.2) and ({x+.7},2.2) .. ({x+.5},1.45);',f'\\node[font=\\scriptsize] at ({x+.95},2.2) {{üste konuyor}};']
    return o
o=[]
for x,t,n in [(0,'y','K'),(3.4,'d','L'),(6.8,'u','M')]:
    o+=blok2(x,t); o.append(f'\\node[font=\\small\\bfseries] at ({x+.9},-.5) {{{n}}};')
o.append('\\draw[thick] (-.4,0) -- (9.3,0);')
SK3=sk(*o)
onc('0003',{2,3},pick(0,1,2,3,5),
 {1:'Yatay kesimde kalan parçanın ağırlığı da yüksekliği de yarıya iner, alan aynı kalır: P_K = P ÷ 2 olur.',
  2:'Düşey kesimde kalan parçanın hem ağırlığı hem taban alanı yarıya iner; oranları değişmediğinden basınç P olarak kalır (P = d · g · h).',
  3:'Yarı parça üste konunca toplam ağırlık W kalır, taban alanı A ÷ 2 olur; P_M = W ÷ (A ÷ 2) = 2P.'},
 'Yatay bir zemine tam oturan, homojen ve dikdörtgenler prizması biçimli bir blok zemine P basıncı uygulamaktadır. Bu bloğun üç özdeş kopyası, üç ayrı deneyde şekilde kesikli çizgiyle gösterilen düzlemden kesiliyor. K deneyinde yatay kesimle üst yarı atılıyor, L deneyinde düşey kesimle sağ yarı atılıyor, M deneyinde ise düşey kesimle ayrılan sağ yarı atılmayıp sol yarının üst yüzeyine, tabanı tam oturacak biçimde konuyor. Her deneyde kalan düzenin zemine uyguladığı basınç ayrı ayrı belirleniyor.\nBuna göre,\nI. K deneyinde kalan parçanın zemine uyguladığı basınç P’dir.\nII. L deneyinde kalan parçanın zemine uyguladığı basınç P’dir.\nIII. M deneyinde oluşan düzenin zemine uyguladığı basınç 2P’dir.\nyargılarından hangileri doğrudur?',
 tipId=TIP['kes'][0],tip=TIP['kes'][1],z='orta',alt='Katı Basıncı',kaz='Homojen bir prizmanın kesilmesi ve yeniden dizilmesi durumunda ağırlık ile alan değişimini birlikte değerlendirerek basıncı yorumlar.',
 kart='K-FZBS2-03 (kesme ve yeniden dizme) · öncüllü',istenen='Doğru olan yargılar.',ip=['Her deneyde zemine bastıran ağırlığın ve zemine değen alanın ilk duruma göre kaçta kaçına indiğine bak.'],
 bilgi=[B('Homojen prizmada basınç','Dik prizmada P = W ÷ A = (d · V · g) ÷ A = d · g · h olur; basınç yalnız özkütleye ve yüksekliğe bağlıdır. Örnek: d = 2000 kg/m³, h = 0,3 m için P = 2000 × 10 × 0,3 = 6000 Pa; taban genişliği ne olursa olsun aynıdır')],
 puf='Dik homojen prizmada basınç d·g·h olduğundan yükseklik değişmedikçe taban alanı ne kadar küçülürse küçülsün basınç değişmez.',sekil=SK3)

# ================= 04 · homojen silindirler, P = d g h · orta =================
K(4,'sil','Katı Basıncı','Aynı maddeden yapılmış dik silindirlerde basınç yalnız yüksekliğe bağlıdır; yarıçap ağırlığı ve alanı aynı oranda değiştirir.','Daha geniş silindirin daha çok bastığını sanmak; yalnız ağırlık ya da yalnız alan oranını almak.','orta','şekilli',3)
dd=2700; rx,hx,ry_,hy=3,20,6,10
Wx=rx**2*hx; Wy=ry_**2*hy; Ax=rx**2; Ay=ry_**2
rat=Fr(Wx,Ax)/Fr(Wy,Ay)
assert rat==2 and Fr(dd*10*hx,100)==5400 and Fr(dd*10*hy,100)==2700 and Fr(Ax,Ay)==Fr(1,4) and Fr(Wx,Wy)==Fr(1,2) and Fr(Ay,Ax)==4
def silin(x,r,h,et,s=.15):
    rx_=r*s; H=h*s; ry=rx_*.3
    return [f'\\draw[thick,fill=gray!26] ({x-rx_:.2f},{H:.2f}) -- ({x-rx_:.2f},0) arc[start angle=180,end angle=360,x radius={rx_:.2f},y radius={ry:.2f}] -- ({x+rx_:.2f},{H:.2f}) -- cycle;',
            f'\\draw[thick,fill=gray!12] ({x:.2f},{H:.2f}) ellipse[x radius={rx_:.2f},y radius={ry:.2f}];',
            f'\\draw[thick] ({x:.2f},{H:.2f}) -- ({x+rx_:.2f},{H:.2f});',
            f'\\node[above,font=\\scriptsize] at ({x+rx_/2:.2f},{H+ry:.2f}) {{$r={r}$ cm}};',
            f'\\draw[{DIM}] ({x+rx_+.45:.2f},0) -- ({x+rx_+.45:.2f},{H:.2f});',
            f'\\node[right,font=\\scriptsize] at ({x+rx_+.45:.2f},{H/2:.2f}) {{${h}$ cm}};',
            f'\\node[font=\\small\\bfseries] at ({x:.2f},-.62) {{{et}}};']
SK4=sk(*(silin(1.0,rx,hx,'X')+silin(4.6,ry_,hy,'Y')+['\\draw[thick] (-.5,0) -- (7.4,0);']))
q('0004',tipId=TIP['sil'][0],tip=TIP['sil'][1],z='orta',alt='Katı Basıncı',kaz='Aynı maddeden yapılmış dik silindirlerin zemine uyguladığı basınçları özkütle ve yükseklikten karşılaştırır.',kalip='şekilli',
 kart='K-FZBS2-04 (homojen silindir, P = d·g·h) · yarıçap ve yükseklik farklı',
 metin='Bir atölyede aynı alüminyum alaşımından dökülmüş, dik silindir biçimli, homojen iki çubuk hazırlanıyor. Çubukların yarıçapları ve yükseklikleri şekilde verilmiştir. Çubuklar yatay ve düz bir tezgâh üzerine, dairesel tabanları üzerinde dik duracak biçimde konuyor. Tezgâh çubukları çökertmeyecek kadar serttir ve yüzeyler tam temas etmektedir.\nBuna göre, X çubuğunun tezgâha uyguladığı basıncın Y çubuğunun uyguladığı basınca oranı kaçtır?',
 sekil=SK4,dogru=2,yan=[(0.25,'Yalnız taban alanlarını karşılaştırıp X’in alanını Y’ninkine bölmüş (9 ÷ 36); ağırlığı hesaba katmamış.','dikkat'),(0.5,'Yalnız ağırlıkları oranlamış (X’in hacmi Y’ninkinin yarısı); alanların da farklı olduğunu unutmuş.','bilgi'),(1,'Aynı maddeden yapıldıkları için basınçları eşit sanmış; yüksekliklerin farklı olduğunu hesaba katmamış.','bilgi'),(4,'Yalnız taban alanlarını karşılaştırıp Y’nin alanını X’inkine bölmüş (36 ÷ 9); basıncı alanla doğru orantılı sanmış.','dikkat')],
 istenen='P_X ÷ P_Y oranı.',ip=['Silindirlerin zemine bastırdığı basıncı belirleyen niceliklerden hangisi X ve Y için ortaktır, hangisi farklıdır?'],
 bilgi=[B('Dik silindirde basınç','Ağırlık W = d · V · g, V = A · h olduğundan P = W ÷ A = d · g · h; taban alanı sadeleşir. Örnek: d = 1000 kg/m³, h = 0,5 m için P = 1000 × 10 × 0,5 = 5000 Pa')],
 ad=[A('Basınç bağıntısını yaz','Dik homojen silindirde alan sadeleşir.','P = d × g × h'),A('Her çubuğa uygula','Özkütle ve g ortaktır; yalnız yükseklik farklıdır.','P_X = d × g × 0,20; P_Y = d × g × 0,10'),A('Oranla','Ortak çarpanlar sadeleşir.','P_X ÷ P_Y = 20 ÷ 10 = 2'),A('Kontrol et','Ağırlık ve alanla da doğrula: W ∝ r² · h, A ∝ r².','(9 · 20 ÷ 9) ÷ (36 · 10 ÷ 36) = 20 ÷ 10 = 2')],
 puf='Aynı maddeden yapılmış dik prizma ve silindirlerde zemin basıncı yalnız yüksekliğe bağlıdır.')

# ================= 05 · üst üste bloklar · zor · öncüllü =================
K(5,'yigin','Katı Basıncı','K bloğunun L’ye yaptığı basınç K’nin ağırlığı ve temas yüzü ile, L’nin zemine yaptığı basınç ise toplam ağırlık ve L’nin tabanı ile hesaplanır; K’yi çevirince yalnız ilki değişir.','İki basıncı aynı alanla hesaplamak; K’yi çevirince zemindeki basıncın da değiştiğini sanmak.','zor','öncüllü',5)
WK,WL=40,140
pa=Fr(WK)/Fr(10*10,10**4); pb=Fr(WK)/Fr(10*20,10**4); zem=Fr(WK+WL)/Fr(20*20,10**4)
assert pa==4000 and pb==2000 and zem==4500 and pb!=zem
def blk(x,y,w,h,et,sc=.1):
    return f'\\draw[thick,fill=gray!26] ({x:.2f},{y:.2f}) rectangle ({x+w*sc:.2f},{y+h*sc:.2f}); \\node[font=\\scriptsize] at ({x+w*sc/2:.2f},{y+h*sc/2:.2f}) {{{et}}};'
def dimh(x,y0,y1,t,xs=.2): return f'\\draw[{DIM}] ({x:.2f},{y0:.2f}) -- ({x:.2f},{y1:.2f}); \\node[right,font=\\scriptsize] at ({x:.2f},{(y0+y1)/2:.2f}) {{{t}}};'
def dimw(y,x0,x1,t,up=True): return f'\\draw[{DIM}] ({x0:.2f},{y:.2f}) -- ({x1:.2f},{y:.2f}); \\node[{"above" if up else "below"},font=\\scriptsize] at ({(x0+x1)/2:.2f},{y:.2f}) {{{t}}};'
o=[]
for ox,tag,(kw,kh) in [(0,'(a)',(10,20)),(5.0,'(b)',(20,10))]:
    o.append(blk(ox,0,20,10,'L · 140 N'))
    kx=ox+1.0-kw*.1/2
    o.append(blk(kx,1.0,kw,kh,'K · 40 N'))
    o.append(dimw(-.25,ox,ox+2.0,'$20$ cm',up=False))
    o.append(dimh(ox+2.25,0,1.0,'$10$ cm'))
    o.append(dimw(1.0+kh*.1+.2,kx,kx+kw*.1,f'${kw}$ cm'))
    o.append(dimh(kx+kw*.1+.3 if kw==10 else ox+2.25,1.0,1.0+kh*.1,f'${kh}$ cm'))
    o.append(f'\\node[font=\\small\\bfseries] at ({ox+1.0:.2f},-.85) {{{tag}}}; \\draw[thick] ({ox-.4:.2f},0) -- ({ox+2.1:.2f},0);')
SK5=sk(*o)
onc('0005',{1},pick(0,1,2,3,6),
 {1:'(a)’da K’nin ağırlığı 40 N, L’ye değen yüzü 10 × 10 = 100 cm² = 0,01 m²’dir: P = 40 ÷ 0,01 = 4000 Pa.',
  2:'Zemine bastıran toplam ağırlık 40 + 140 = 180 N, L’nin taban alanı 0,04 m²’dir; K nasıl durursa dursun basınç 180 ÷ 0,04 = 4500 Pa olarak değişmez.',
  3:'(b)’de K’nin L’ye basıncı 40 ÷ 0,02 = 2000 Pa, L’nin zemine basıncı 4500 Pa’dır; iki basınç farklıdır, çünkü kuvvetler ve alanlar farklıdır.'},
 'Kare tabanlı, homojen K ve L prizmalarının ağırlıkları şekilde verilmiştir. L bloğu yatay ve sert bir zeminde durmaktadır. K bloğu, (a) durumunda dik, (b) durumunda yatık olacak biçimde L’nin üst yüzeyine yerleştirilmektedir; her iki durumda K’nin tabanı tamamen L’nin üst yüzeyinin içinde kalmakta ve sistem dengede durmaktadır. Blokların ölçüleri şekilde gösterilmiştir. Bir öğrenci iki durumda da K’nin L’ye ve L’nin zemine uyguladığı basınçları hesaplıyor.\nBuna göre,\nI. (a) durumunda K’nin L’ye uyguladığı basınç 4000 Pa’dır.\nII. L’nin zemine uyguladığı basınç, (b) durumunda (a) durumundakinden küçüktür.\nIII. (b) durumunda K’nin L’ye uyguladığı basınç, L’nin zemine uyguladığı basınca eşittir.\nyargılarından hangileri doğrudur?',
 tipId=TIP['yigin'][0],tip=TIP['yigin'][1],z='zor',alt='Katı Basıncı',kaz='Üst üste duran bloklarda her temas yüzeyi için o yüzeye bastıran ağırlık ve temas alanından basıncı hesaplar.',
 kart='K-FZBS2-05 (üst üste bloklar, K döndürülür) · öncüllü',istenen='Doğru olan yargılar.',ip=['Her yüzey için “o yüzeye kimin ağırlığı basıyor ve temas alanı ne kadar” sorusunu ayrı ayrı yanıtla.'],
 bilgi=[B('Üst üste cisimlerde basınç','Her temas yüzeyindeki basınç, o yüzeye bastıran toplam ağırlığın temas alanına oranıdır. Alt cismin zemine basıncında üstteki cismin ağırlığı da eklenir. Örnek: 10 N’luk cismin üstündeki 5 N’luk cisim, alttakinin zemine bastıran kuvvetini 15 N yapar')],
 puf='Üstteki cismin nasıl durduğu, alttakinin zemine bastıran toplam ağırlığını değiştirmez; yalnız temas yüzeyindeki basıncı değiştirir.',sekil=SK5)

# ================= 06 · kap şekli · orta · öncüllü =================
K(6,'kap','Sıvı Basıncı ve Basınç Kuvveti','Sıvı basıncı yalnız derinliğe ve özkütleye bağlıdır; taban kuvveti P·A’dır ve sıvının ağırlığına eşit olmak zorunda değildir.','Kap şeklinin taban basıncını değiştirdiğini sanmak; taban kuvvetini sıvının ağırlığına eşitlemek.','orta','öncüllü',3)
def kap(x,wb,wt,h,et):
    pts=[(x-wt/2,h),(x-wb/2,0),(x+wb/2,0),(x+wt/2,h)]
    po=' -- '.join(f'({a:.2f},{b:.2f})' for a,b in pts)
    return [f'\\fill[vurgu!16] {po} -- cycle;',f'\\draw[thick] ({pts[0][0]:.2f},{h+.25:.2f}) -- {" -- ".join(f"({a:.2f},{b:.2f})" for a,b in pts)} -- ({pts[3][0]:.2f},{h+.25:.2f});',
            f'\\draw[thin] ({pts[0][0]:.2f},{h:.2f}) -- ({pts[3][0]:.2f},{h:.2f});',f'\\node[font=\\small\\bfseries] at ({x:.2f},-.5) {{{et}}};']
o=kap(1.2,1.2,1.2,1.6,'K')+kap(3.9,1.2,2.0,1.6,'L')+kap(6.6,1.2,.6,1.6,'M')
o.append(f'\\draw[{DIM}] (-.35,0) -- (-.35,1.6); \\node[left,font=\\scriptsize] at (-.35,.8) {{$h$}};')
o.append('\\draw[thick] (-.6,0) -- (7.4,0);')
SK6=sk(*o)
onc('0006',{3},pick(2,3,4,5,6),
 {1:'Taban alanları ve sıvı yükseklikleri eşit, sıvı aynı olduğundan taban basınçları eşittir; basınç kuvveti F = P · A da üç kapta eşittir.',
  2:'Kapların biçimi farklı olduğundan sıvı hacimleri, dolayısıyla ağırlıkları farklıdır: L’de en fazla, M’de en azdır.',
  3:'M’de üste doğru daralan yan duvarlar sıvıyı aşağı doğru iter; tabana uygulanan kuvvet sıvının ağırlığından büyüktür.'},
 'Taban alanları birbirine eşit olan, K dik silindir, L üste doğru genişleyen ve M üste doğru daralan biçimli üç kap, şekildeki gibi aynı h yüksekliğine kadar aynı cins sıvıyla doldurulmuştur. Kapların cidarı ince, sıvı durgun ve açık hava basıncı ihmal edilebilir düzeydedir. Basınç kuvveti derken yalnızca sıvının tabana uyguladığı kuvvet, ağırlık derken kaplardaki sıvıların ağırlığı kastedilmektedir; kapların kendi ağırlığı hesaba katılmayacaktır. Bir öğrenci, sıvıların tabana yaptığı etkiyi ve kaplardaki sıvı miktarlarını karşılaştırmak istiyor.\nBuna göre,\nI. Sıvıların tabana uyguladığı basınç kuvvetleri birbirinden farklıdır.\nII. Kaplardaki sıvıların ağırlıkları birbirine eşittir.\nIII. M kabında sıvının tabana uyguladığı basınç kuvveti, M’deki sıvının ağırlığından büyüktür.\nyargılarından hangileri doğrudur?',
 tipId=TIP['kap'][0],tip=TIP['kap'][1],z='orta',alt='Sıvı Basıncı',kaz='Kap şekli farklı olsa da aynı sıvı ve aynı derinlikte taban basıncının eşit olduğunu; taban kuvveti ile sıvı ağırlığının farklı olabileceğini yorumlar.',
 kart='K-FZBS2-06 (kap şekli, taban kuvveti) · öncüllü',istenen='Doğru olan yargılar.',ip=['Taban basıncını belirleyen niceliklere bak; sonra kuvveti basınç ve alandan, sıvının ağırlığını ise sıvı miktarından ayrı ayrı düşün.'],
 bilgi=[B('Sıvı basıncı ve basınç kuvveti','P = d · g · h; basınç kap biçimine bağlı değildir. Tabana uygulanan kuvvet F = P · A’dır ve sıvının ağırlığından farklı olabilir. Örnek: d = 1000 kg/m³, h = 0,4 m, A = 0,01 m² için P = 4000 Pa, F = 40 N')],
 puf='Sıvının tabana uyguladığı basınç ve kuvvet P = d·g·h ile P·A’dan bulunur; kap biçimine ve sıvı ağırlığına değil, derinliğe ve alana bağlıdır.',sekil=SK6)

# ================= 07 · dalgıç, toplam basınç · kolay =================
K(7,'der','Sıvı Basıncı','Sıvı içindeki bir noktada toplam basınç, açık hava basıncı ile sıvı basıncının (d·g·h) toplamıdır.','Yalnız sıvı basıncını ya da yalnız açık hava basıncını vermek; derinliği yanlış birimle kullanmak.','kolay','şekilli',2)
d7,h7,P07=1000,20,10**5
Ps7=d7*10*h7; Pt7=P07+Ps7
assert Ps7==200000 and Pt7==300000 and d7*10*2+P07==120000 and 2*P07+Ps7==400000
o=['\\fill[vurgu!15] (0,-3.2) rectangle (4,0);','\\draw[thick] (-.3,0) -- (4.3,0); \\draw[thick] (0,.3) -- (0,-3.2) -- (4,-3.2) -- (4,.3);',
   '\\fill (2.2,-2.0) circle (2.4pt); \\node[right,font=\\small\\bfseries] at (2.3,-2.0) {dalgıç};',
   f'\\draw[{DIM}] (1.2,0) -- (1.2,-2.0); \\node[left,font=\\scriptsize] at (1.2,-1.0) {{${h7}$ m}};','\\draw[dotted] (1.2,-2.0) -- (2.2,-2.0);']
SK7=sk(*o)
q('0007',tipId=TIP['der'][0],tip=TIP['der'][1],z='kolay',alt='Sıvı Basıncı',kaz='Sıvı içindeki bir noktadaki toplam basıncı açık hava ve sıvı basıncını toplayarak hesaplar.',kalip='şekilli',
 kart='K-FZBS2-07 (toplam basınç, göl) · açık hava + sıvı',
 metin='Bir dalgıç, durgun ve geniş bir gölün yüzeyinden şekilde gösterilen derinliğe iniyor. Göl suyunun özkütlesi 1000 kg/m³, gölün üzerindeki açık hava basıncı 10⁵ Pa’dır; g = 10 m/s² alınacak ve suyun özkütlesinin derinlikle değişmediği kabul edilecektir. Dalgıcın bulunduğu noktada suyun yaptığı basınç ile gölün yüzeyine etki eden açık hava basıncının ikisi birlikte dalgıca etki etmektedir.\nBuna göre, dalgıcın bulunduğu noktadaki toplam basınç kaç Pa’dır?',
 sekil=SK7,dogru=300000,yan=[(100000,'Yalnız açık hava basıncını almış; sıvı basıncını eklememiş.','dikkat'),(120000,'Derinliği 2 m sanmış (20 m’yi yanlış okumuş): 1000 × 10 × 2 + 10⁵.','islem'),(200000,'Yalnız sıvı basıncını hesaplamış; açık hava basıncını eklememiş.','dikkat'),(400000,'Açık hava basıncını iki kez eklemiş (2 × 10⁵ + 2 × 10⁵).','islem')],
 istenen='Dalgıcın bulunduğu noktadaki toplam basınç (Pa).',ip=['Dalgıca basınç uygulayan iki ayrı kaynağı belirle ve her birini ayrı hesapla.'],
 bilgi=[B('Sıvı içinde toplam basınç','Açık bir kaptaki sıvıda toplam basınç P = P₀ + d × g × h’tır (P₀ açık hava basıncı). Örnek: P₀ = 10⁵ Pa, d = 1000 kg/m³, h = 5 m için P = 100 000 + 50 000 = 150 000 Pa')],
 ad=[A('Basıncın kaynaklarını belirle','Dalgıca hem suyun hem de gölün üzerindeki havanın basıncı etki eder.','P = P₀ + P_sıvı'),A('Sıvı basıncını hesapla','Derinlik 20 m’dir; sıvı basıncı d × g × h ile bulunur.','P_sıvı = 1000 × 10 × 20 = 200 000 Pa'),A('Açık hava basıncını ekle','Gölün yüzeyine etki eden açık hava basıncı sıvı içine aynen iletilir.','P = 100 000 + 200 000 = 300 000 Pa')],
 puf='Açık bir sıvıda toplam basınç, açık hava basıncı ile sıvı basıncının toplamıdır.')

# ================= 08 · U borusu · orta =================
K(8,'u','Sıvı Basıncı','Ayrım düzeyinde iki koldaki basınç eşittir: d₁·h₁ = d₂·h₂; sütun yüksekliği ile özkütle ters orantılıdır.','Oranı ters kurmak; yüksekliklerin toplamını ya da farkını kullanmak.','orta','şekilli',3)
hw,hX=16,20; dX=Fr(1000*hw,hX)
assert dX==800 and Fr(1000*hX,hw)==1250 and 1000*Fr(hX-hw,hX)==200 and 1000*Fr(hw+hX,hX)==1800
o=[f'\\fill[vurgu!16] (0,2.8) -- (0,0) -- (2.2,0) -- (2.2,1.2) -- (1.5,1.2) -- (1.5,.7) -- (.7,.7) -- (.7,2.8) -- cycle;',
   '\\fill[gray!38] (1.5,1.2) rectangle (2.2,3.2);',
   '\\draw[thick] (0,3.6) -- (0,0) -- (2.2,0) -- (2.2,3.6);','\\draw[thick] (.7,3.6) -- (.7,.7) -- (1.5,.7) -- (1.5,3.6);',
   '\\draw[dashed] (-.35,1.2) -- (2.55,1.2);',
   f'\\draw[{DIM}] (-.35,1.2) -- (-.35,2.8); \\node[left,font=\\scriptsize] at (-.35,2.0) {{${hw}$ cm}};',
   f'\\draw[{DIM}] (2.55,1.2) -- (2.55,3.2); \\node[right,font=\\scriptsize] at (2.55,2.2) {{${hX}$ cm}};',
   '\\node[font=\\small\\bfseries] at (.35,1.6) {su};','\\node[font=\\small\\bfseries] at (1.85,2.2) {X};']
SK8=sk(*o)
q('0008',tipId=TIP['u'][0],tip=TIP['u'][1],z='orta',alt='Sıvı Basıncı',kaz='U borusunda ayrım düzeyindeki basınç eşitliğinden bilinmeyen sıvının özkütlesini bulur.',kalip='şekilli',
 kart='K-FZBS2-08 (U borusu, su–X) · ayrım sağ kolda',
 metin='Kesit alanı her yerde aynı olan U biçimli bir cam boruya önce su konuyor. Daha sonra sağ koldan, suyla karışmayan ve özkütlesi bilinmeyen X sıvısı dökülüyor. Denge sağlandığında su ile X sıvısının ayrım yüzeyi sağ koldadır. Ayrım düzeyinden itibaren sol koldaki su sütunu ile sağ koldaki X sütununun yükseklikleri şekilde verilmiştir. Suyun özkütlesi 1000 kg/m³’tür ve iki kolun açık uçlarına aynı açık hava basıncı etki etmektedir.\nBuna göre, X sıvısının özkütlesi kaç kg/m³’tür?',
 sekil=SK8,dogru=800,yan=[(200,'Yükseklik farkını (4 cm) X’in yüksekliğine bölüp suyun özkütlesiyle çarpmış.','islem'),(1000,'Sıvıların aynı düzeydeki basıncı eşit olduğundan özkütlelerinin de eşit olması gerektiğini sanmış.','bilgi'),(1250,'Eşitliği ters kurmuş: 1000 × 20 ÷ 16.','dikkat'),(1800,'İki sütunun yüksekliklerini toplayıp suyun özkütlesiyle çarpmış (1000 × 36 ÷ 20).','islem')],
 istenen='X sıvısının özkütlesi (kg/m³).',ip=['Ayrım yüzeyi düzeyindeki iki noktaya, kendi kolundaki sıvı sütunu ne kadar basınç uyguluyor?'],
 bilgi=[B('U borusunda eşit basınç düzlemi','Karışmayan sıvılı U borusunda, ayrım düzeyinden geçen yatay düzlemde iki koldaki basınçlar eşittir: d₁ · h₁ = d₂ · h₂. Örnek: d₁ = 900 kg/m³ ve h₁ = 10 cm iken h₂ = 15 cm ise d₂ = 900 × 10 ÷ 15 = 600 kg/m³')],
 ad=[A('Eşit basınç düzlemini belirle','Ayrım yüzeyinden geçen yatay düzlemde, aynı sıvı içindeki noktalarda basınç eşittir.','P_sol = P_sağ'),A('Basınçları yaz','Sol kolda su sütunu, sağ kolda X sütunu bastırır; g sadeleşir.','1000 × g × 16 = d_X × g × 20'),A('Özkütleyi çöz','Sütun yüksekliği ile özkütle ters orantılıdır.','d_X = 1000 × 16 ÷ 20 = 800 kg/m³')],
 puf='U borusunda ayrım düzeyinde d₁·h₁ = d₂·h₂ yazılır; sütun uzun olan sıvı daha hafiftir.')

# ================= 09 · üç katmanlı sıvı · zor =================
K(9,'kat','Sıvı Basıncı','Katmanlı sıvıda iki nokta arasındaki basınç farkı, aradaki katman parçalarının d·g·h değerlerinin toplamıdır.','K noktasını katman sınırında sanmak; aradaki tüm kalınlığı tek özkütleyle hesaplamak.','zor','şekilli',4)
dX_,hX_,dY_,hY_,dZ_,hZ_=800,15,1000,20,1200,15
PK=dX_*10*Fr(hX_,100)+dY_*10*Fr(hY_,200); PT=dX_*10*Fr(hX_,100)+dY_*10*Fr(hY_,100)+dZ_*10*Fr(hZ_,100)
fark=PT-PK
assert PK==2200 and PT==5000 and fark==2800 and fark==dY_*10*Fr(hY_,200)+dZ_*10*Fr(hZ_,100)
assert PT-(dX_*10*Fr(hX_,100)+dY_*10*Fr(hY_,100))==1800 and PT-dX_*10*Fr(hX_,100)==3800 and dY_*10*Fr(hY_//2+hZ_,100)==2500
s9=.06
yZ=hZ_*s9; yY=yZ+hY_*s9; yX=yY+hX_*s9
o=[f'\\fill[vurgu!34] (0,0) rectangle (3.4,{yZ:.2f});',f'\\fill[vurgu!20] (0,{yZ:.2f}) rectangle (3.4,{yY:.2f});',f'\\fill[vurgu!9] (0,{yY:.2f}) rectangle (3.4,{yX:.2f});',
   f'\\draw[very thick] (0,{yX+.3:.2f}) -- (0,0) -- (3.4,0) -- (3.4,{yX+.3:.2f});',
   f'\\draw (0,{yZ:.2f}) -- (3.4,{yZ:.2f}); \\draw (0,{yY:.2f}) -- (3.4,{yY:.2f}); \\draw (0,{yX:.2f}) -- (3.4,{yX:.2f});']
for nm,d_,y0,y1,hh in [('X',dX_,yY,yX,hX_),('Y',dY_,yZ,yY,hY_),('Z',dZ_,0,yZ,hZ_)]:
    o.append(f'\\node[anchor=west,font=\\scriptsize] at (.1,{(y0+y1)/2:.2f}) {{{nm}: $d={d_}$ kg/m$^3$}};')
    o.append(f'\\draw[{DIM}] (3.75,{y0+.07:.2f}) -- (3.75,{y1-.07:.2f}); \\node[right,font=\\scriptsize] at (3.75,{(y0+y1)/2:.2f}) {{${hh}$ cm}};')
ykk=(yZ+yY)/2
o.append(f'\\fill (2.75,{ykk:.2f}) circle (2.2pt); \\node[right,font=\\small\\bfseries] at (2.8,{ykk:.2f}) {{K}};')
SK9=sk(*o)
q('0009',tipId=TIP['kat'][0],tip=TIP['kat'][1],z='zor',alt='Sıvı Basıncı',kaz='Üç katmanlı sıvıda ara bir nokta ile kap tabanı arasındaki basınç farkını katmanları parçalayarak hesaplar.',kalip='şekilli',
 kart='K-FZBS2-09 (üç katman, K orta noktada) · fark',
 metin='Bir laboratuvarda birbirine karışmayan X, Y ve Z sıvıları, tabanı yatay ve ağzı açık bir kaba şekildeki gibi sırayla dökülmüş ve sıvılar dengeye gelmiştir. Sıvıların özkütleleri ve katman yükseklikleri şekilde verilmiştir. K noktası Y katmanının tam ortasındadır. Açık hava basıncı ihmal edilecek ve g = 10 m/s² alınacaktır.\nBuna göre, kabın tabanındaki sıvı basıncı ile K noktasındaki sıvı basıncı arasındaki fark kaç Pa’dır?',
 sekil=SK9,dogru=2800,yan=[(1800,'K’yi Y katmanının alt sınırında sanmış; yalnız Z katmanının basıncını (1800 Pa) almış.','dikkat'),(2500,'K’den tabana kadar olan 25 cm’lik kalınlığı tek özkütleyle (Y’ninki, 1000) hesaplamış.','bilgi'),(3800,'K’yi Y katmanının üst sınırında sanmış; Y’nin tamamını (2000 Pa) ve Z’yi (1800 Pa) saymış.','dikkat'),(5000,'Farkı almamış, kabın tabanındaki toplam basıncı (1200 + 2000 + 1800) vermiş.','dikkat')],
 istenen='P_taban − P_K farkı (Pa).',ip=['K ile taban arasında hangi katmanların, ne kalınlıkta bulunduğuna bak; her birinin basıncını kendi özkütlesiyle ayrı hesapla.'],
 bilgi=[B('Katmanlı sıvıda basınç','Karışmayan sıvılarda basınç, geçilen her katmanın d × g × h değerlerinin toplamıdır. Örnek: üstte d = 900 kg/m³ ile 0,1 m ve altta d = 1100 kg/m³ ile 0,2 m için P = 900 × 10 × 0,1 + 1100 × 10 × 0,2 = 3100 Pa')],
 ad=[A('K’nin altındaki katmanları belirle','K, Y’nin ortasında olduğundan altında Y’nin yarısı (10 cm) ve Z’nin tamamı (15 cm) vardır.','Y: 10 cm = 0,1 m; Z: 15 cm = 0,15 m'),A('Y parçasının basıncı','Y’nin alt yarısı kendi özkütlesiyle hesaplanır.','1000 × 10 × 0,1 = 1000 Pa'),A('Z katmanının basıncı','Z kendi özkütlesiyle hesaplanır.','1200 × 10 × 0,15 = 1800 Pa'),A('Farkı topla','Fark, K ile taban arasındaki katmanların basınçlarının toplamıdır.','1000 + 1800 = 2800 Pa'),A('Kontrol et','Taban ve K basıncını ayrı bulup çıkar.','P_taban = 1200 + 2000 + 1800 = 5000 Pa · P_K = 1200 + 1000 = 2200 Pa → 2800 Pa')],
 puf='İki nokta arasındaki basınç farkı için yalnızca aradaki katman parçalarını, her birini kendi özkütlesiyle hesaplayıp topla.')

# ================= 10 · bileşik kap + musluk · orta =================
K(10,'bil','Sıvı Basıncı','Farklı sıvılı bağlantılı kaplarda akış yönü, musluk düzeyindeki basınçların karşılaştırılmasıyla belirlenir; yükseklik tek başına belirleyici değildir.','Yüksek olan sıvıdan alçak olana akacağını sanmak; sıvı miktarına bakmak.','orta','şekilli',3)
PLs=1000*10*Fr(30,100); PRs=1200*10*Fr(26,100)
assert PLs==3000 and PRs==3120 and PRs>PLs
o=[f'\\fill[vurgu!14] (0,0) rectangle (1.4,2.4);',f'\\fill[vurgu!38] (2.6,0) rectangle (3.5,2.08);',f'\\fill[vurgu!14] (1.4,0) rectangle (2.0,.22);',f'\\fill[vurgu!38] (2.0,0) rectangle (2.6,.22);',
   '\\draw[thick] (0,2.7) -- (0,0) -- (1.4,0); \\draw[thick] (1.4,.22) -- (2.6,.22); \\draw[thick] (2.6,0) -- (3.5,0) -- (3.5,2.7);',
   '\\draw[thick] (1.4,2.7) -- (1.4,.22); \\draw[thick] (2.6,2.7) -- (2.6,.22);','\\draw[thick] (1.4,0) -- (2.6,0);',
   '\\draw[thick,fill=white] (1.82,.0) -- (2.18,.22) -- (2.18,0) -- (1.82,.22) -- cycle;','\\node[below,font=\\scriptsize] at (2.0,-.02) {musluk};',
   '\\draw[thin] (0,2.4) -- (1.4,2.4); \\draw[thin] (2.6,2.08) -- (3.5,2.08);',
   '\\node[above,font=\\scriptsize,align=center] at (.7,2.75) {su\\\\$1000$ kg/m$^3$};','\\node[above,font=\\scriptsize,align=center] at (3.05,2.75) {tuzlu su\\\\$1200$ kg/m$^3$};',
   f'\\draw[{DIM}] (-.35,0) -- (-.35,2.4); \\node[left,font=\\scriptsize] at (-.35,1.2) {{$30$ cm}};',
   f'\\draw[{DIM}] (3.85,0) -- (3.85,2.08); \\node[right,font=\\scriptsize] at (3.85,1.04) {{$26$ cm}};']
SK10=sk(*o)
sec=['Soldan sağa akar; çünkü sol kaptaki sıvının yüksekliği daha büyüktür.','Sağdan sola akar; çünkü musluk düzeyinde sağ kaptaki sıvının basıncı daha büyüktür.','Akış olmaz; çünkü musluk düzeyinde iki kaptaki sıvı basıncı eşittir.','Soldan sağa akar; çünkü sol kaptaki sıvının özkütlesi daha küçüktür.','Akış olmaz; çünkü sağ kaptaki sıvı miktarı daha azdır.']
q('0010',tipId=TIP['bil'][0],tip=TIP['bil'][1],z='orta',alt='Sıvı Basıncı',kaz='Farklı özkütleli sıvılar içeren bağlantılı kaplarda musluk düzeyindeki basınçları karşılaştırarak akış yönünü belirler.',kalip='şekilli',
 kart='K-FZBS2-10 (bileşik kap, farklı sıvı, musluk) · akış yönü',
 metin='Kesit alanları birbirinden farklı iki kap, tabanlarına çok yakın bir yerden musluklu ince bir boruyla birbirine bağlanmıştır. Musluk kapalıyken sol kapta su, sağ kapta ise suyla karışabilen tuzlu su durgun hâldedir. Sıvıların özkütleleri ve tabandan ölçülen yükseklikleri şekilde verilmiştir. Boru, tabanla aynı düzeydedir ve içindeki sıvı miktarı ihmal edilmektedir. Musluk açıldığı ilk anda sıvıların karışması dikkate alınmayacak; yalnızca ilk andaki akışın yönü incelenecektir.\nBuna göre, musluk açıldığı anda aşağıdakilerden hangisi gerçekleşir?',
 sekil=SK10,dogru=sec[1],sira=sec,yan=[(sec[0],'Akışı yalnız sıvı yüksekliklerine bakarak belirlemiş; farklı özkütleleri hesaba katmamış (sol 3000 Pa, sağ 3120 Pa).','bilgi'),(sec[2],'Bağlantılı kaplarda basıncın eşit olacağını sanmış; musluk düzeyindeki basınçları hesaplamamış (3000 Pa ile 3120 Pa farklıdır).','bilgi'),(sec[3],'Sıvıyı özkütlesi küçük olan taraftan büyük olana akıtmış; akış, basıncı büyük taraftan küçük tarafa doğrudur.','dikkat'),(sec[4],'Basıncı sıvı miktarına bağlamış; oysa musluk düzeyindeki basınç yalnız özkütleye ve yüksekliğe bağlıdır, kesit alanına ya da miktara bağlı değildir.','bilgi')],
 istenen='Musluk açıldığı anda akışın yönü ve nedeni.',ip=['Musluk düzeyinde iki sütunun yaptığı basınç eşit midir?'],
 bilgi=[B('Bağlantılı kaplarda akış yönü','Sıvı, bağlantı düzeyindeki basıncı büyük olan kaptan küçük olana akar; basınç P = d × g × h ile hesaplanır. Örnek: 800 kg/m³ özkütleli 0,5 m’lik sütun 4000 Pa, 1000 kg/m³ özkütleli 0,35 m’lik sütun 3500 Pa basınç yapar; sıvı birinci kaptan ikinciye akar')],
 ad=[A('Musluk düzeyindeki basınçları yaz','İki kap da musluk düzeyinden itibaren kendi sıvı sütununun basıncını uygular; kesit alanı sonucu etkilemez.','P_sol = 1000 × 10 × 0,30; P_sağ = 1200 × 10 × 0,26'),A('Sayısal değerleri bul','Yükseklikler metreye çevrilir.','P_sol = 3000 Pa; P_sağ = 3120 Pa'),A('Yönü belirle','Akış basıncı büyük taraftan küçük tarafa doğrudur.','3120 Pa > 3000 Pa → sağdan sola')],
 puf='Bağlantılı kaplarda farklı sıvı varsa akış yönü yükseklikle değil, bağlantı düzeyindeki basınç karşılaştırmasıyla bulunur.')

# ================= 11 · havuzda basınç · orta · öncüllü =================
K(11,'havuz','Sıvı Basıncı ve Basınç Kuvveti','Sıvı basıncı derinlikle doğru orantılıdır, yatay konuma ve çevredeki su miktarına bağlı değildir; bir noktada her yöne eşit etkir.','Havuzun yatay genişliğine bakmak; basıncın yalnız aşağı yönlü olduğunu sanmak.','orta','öncüllü',3)
dk,dm=Fr(12,10),Fr(36,10)
assert dm/dk==3
s11=.5
o=[f'\\fill[vurgu!15] (0,{-4*s11}) rectangle (6,0);','\\draw[thick] (0,.3) -- (0,-2) -- (6,-2) -- (6,.3);','\\draw[thick] (0,0) -- (6,0);']
for nm,xp,dp in [('K',.7,dk),('L',3.0,dk),('M',4.8,dm)]:
    yp=-float(dp)*s11
    o.append(f'\\fill ({xp},{yp:.2f}) circle (2.4pt); \\node[right,font=\\small\\bfseries] at ({xp+.08},{yp:.2f}) {{{nm}}};')
for xd,dp in [(6.45,dk),(7.15,dm)]:
    yp=-float(dp)*s11
    o.append(f'\\draw[{DIM}] ({xd},0) -- ({xd},{yp:.2f}); \\node[{"left" if xd<7 else "right"},font=\\scriptsize] at ({xd},{yp/2:.2f}) {{${str(dp.numerator/dp.denominator).replace(".","{,}")}$ m}};')
o.append('\\draw[dotted] (.7,-.6) -- (6.45,-.6); \\draw[dotted] (4.8,-1.8) -- (7.15,-1.8);')
SK11=sk(*o)
onc('0011',{2},pick(0,1,3,5,6),
 {1:'Sıvı basıncı yalnız derinliğe, özkütleye ve g’ye bağlıdır; K ve L aynı derinlikte olduğundan basınçları eşittir.',
  2:'P = d · g · h olduğundan basınç derinlikle doğru orantılıdır; M’nin derinliği K’ninkinin 3,6 ÷ 1,2 = 3 katı olduğundan P_M = 3 · P_K.',
  3:'Durgun sıvı, bir noktadaki küçük bir cismin her yüzeyine, yüzeye dik ve eşit büyüklükte basınç uygular; basınç yalnız aşağı yönlü değildir.'},
 'Dikdörtgen kesitli, tabanı yatay bir yüzme havuzu ağzına kadar suyla doludur. Havuzda K noktası kenar duvara yakın, L noktası havuzun ortasında ve K ile aynı derinlikte, M noktası ise daha derindedir. Noktaların yüzeyden olan düşey uzaklıkları şekilde gösterilmiştir. Su durgundur ve açık hava basıncı ihmal edilmektedir. Havuzda bu noktalara bırakılan çok küçük cisimlere suyun uyguladığı basınç inceleniyor.\nBuna göre,\nI. L noktasındaki sıvı basıncı, çevresindeki su miktarı daha fazla olduğundan K noktasındakinden büyüktür.\nII. M noktasındaki sıvı basıncı, K noktasındakinin 3 katıdır.\nIII. K noktasındaki küçük bir cisme sıvı yalnız aşağı doğru basınç uygular.\nyargılarından hangileri doğrudur?',
 tipId=TIP['havuz'][0],tip=TIP['havuz'][1],z='orta',alt='Sıvı Basıncı',kaz='Durgun sıvıda basıncın derinlikle orantılı, yatay konumdan bağımsız ve her yöne eşit etkidiğini yorumlar.',
 kart='K-FZBS2-11 (havuz, derinlik ve yön) · öncüllü',istenen='Doğru olan yargılar.',ip=['Sıvı basıncını hangi niceliklerin belirlediğini düşün; havuzun genişliği bu niceliklerden biri mi?'],
 bilgi=[B('Sıvı basıncının özellikleri','Durgun sıvıda basınç derinlikle doğru orantılıdır (P = d · g · h), aynı derinlikte her noktada eşittir ve bir noktada her yöne eşit büyüklükte etkir. Örnek: derinlik 2 katına çıkarsa basınç da 2 katına çıkar')],
 puf='Sıvı basıncı yalnız derinliğe ve özkütleye bağlıdır; kabın genişliğine ve sıvı miktarına bakma, yönü de önemseme.',sekil=SK11)

# ================= 12 · hidrolik pres · zor · öncüllü =================
K(12,'hid','Pascal İlkesi','Pistonların altında basınç eşittir (F₁ ÷ A₁ = F₂ ÷ A₂); sıvı hacmi korunduğundan yer değiştirmeler alanla ters orantılıdır ve iş değişmez.','Kuvvet kazancını yol ya da iş kazancı sanmak; yer değiştirmeyi alan oranıyla çarpmak.','orta','öncüllü',4)
A1,A2,Wy=5,20,400
F1=Fr(Wy*A1,A2); x1=8; x2=Fr(A1*x1,A2)
assert F1==100 and x2==2 and A2*Fr(x2)==A1*x1 and F1*x1==Wy*x2*Fr(1) and x1*Fr(A2,A1)==32
o=['\\fill[vurgu!16] (0,0) rectangle (.8,1.5); \\fill[vurgu!16] (.8,0) rectangle (2.6,.5); \\fill[vurgu!16] (2.6,0) rectangle (4.2,1.5);',
   '\\draw[thick] (0,2.7) -- (0,0) -- (4.2,0) -- (4.2,2.7);','\\draw[thick] (.8,2.7) -- (.8,.5) -- (2.6,.5) -- (2.6,2.7);',
   '\\draw[thick,fill=gray!45] (.02,1.5) rectangle (.78,1.75);','\\draw[thick,fill=gray!45] (2.62,1.5) rectangle (4.18,1.75);',
   '\\draw[thick,fill=gray!22] (2.95,1.75) rectangle (3.85,2.45); \\node[font=\\scriptsize,align=center] at (3.4,2.1) {yük\\\\$400$ N};',
   f'\\draw[vurgu,very thick,{ARR}] (.4,2.75) -- (.4,1.85); \\node[vurgu,above] at (.4,2.75) {{$F$}};',
   '\\node[below,font=\\scriptsize] at (.4,-.02) {$A_1=5$ cm$^2$}; \\node[below,font=\\scriptsize] at (3.4,-.02) {$A_2=20$ cm$^2$};']
SK12=sk(*o)
onc('0012',{1,3},pick(0,1,2,3,4),
 {1:'Basınç eşit olduğundan F₁ = F₂ · A₁ ÷ A₂ = 400 · 5 ÷ 20 = 100 N gerekir.',
  2:'Sıvı hacmi korunur: A₁ · x₁ = A₂ · x₂ → 5 · 8 = 20 · x₂, x₂ = 2 cm’dir; 32 cm değildir. Kuvvet 4 kat kazanılırken yol 4 kat kaybedilir.',
  3:'Basınç eşit olduğundan yük 2 katına (800 N) çıkarsa denge için küçük pistondaki kuvvet de 2 katına çıkar: F₁ = 800 · 5 ÷ 20 = 200 N.'},
 'Şekildeki hidrolik sistemde sıvı dolu bağlantılı iki silindirin pistonları aynı yatay düzeyde dengededir. Piston alanları ve büyük pistonun üzerindeki yük şekilde verilmiştir. Pistonların ağırlıkları, sürtünmeler ve sıvının sıkışması ihmal edilmekte, sıvı iki silindirde de kesintisiz bir bütün oluşturmaktadır. Bir öğrenci, küçük pistona F kuvveti uygulanarak sistemin dengede tutulduğu durumu ve piston hareketlerini inceliyor.\nBuna göre,\nI. Sistemi dengede tutmak için küçük pistona uygulanması gereken kuvvet 100 N’dur.\nII. Küçük piston 8 cm aşağı itilirse büyük piston 32 cm yukarı çıkar.\nIII. Büyük pistonun üzerindeki yük 800 N yapılırsa dengeyi korumak için küçük pistona uygulanması gereken kuvvet 200 N olur.\nyargılarından hangileri doğrudur?',
 tipId=TIP['hid'][0],tip=TIP['hid'][1],z='orta',alt='Pascal Prensibi',kaz='Hidrolik sistemde kuvvet dengesini, sıvı hacminin korunumundan yer değiştirmeleri ve basınç eşitliğini birlikte yorumlar.',
 kart='K-FZBS2-12 (hidrolik pres, yol ve kuvvet) · öncüllü',istenen='Doğru olan yargılar.',ip=['Kuvvetler için basınç eşitliğini, piston hareketleri için ise sıvının toplam hacminin değişmediğini kullan.'],
 bilgi=[B('Pascal ilkesi','Kapalı kaptaki sıvıya uygulanan basınç her yöne aynen iletilir; F₁ ÷ A₁ = F₂ ÷ A₂. Sıvı sıkışmadığından küçük pistonun süpürdüğü hacim büyük pistonunkine eşittir (A₁ · x₁ = A₂ · x₂). Örnek: alanlar oranı 1 : 3 ise büyük piston yolunun 1 ÷ 3’ü kadar hareket eder')],
 puf='Hidrolik sistem kuvveti alan oranı kadar büyütür; fakat sıvı hacmi korunduğundan yol aynı oranda kısalır ve iş kazancı sağlanmaz.',sekil=SK12)

# ================= 13 · hidrolik fren · zor =================
K(13,'fren','Pascal İlkesi','Ana silindirdeki basınç aynen her tekerlek silindirine iletilir; farklı alanlı silindirlerdeki kuvvetler ortak basınçla kendi alanlarının çarpımıdır, toplam kuvvet bunların toplamıdır.','Alanları toplamak ya da bütün silindirleri aynı alanlı saymak; yalnız bir çifti hesaplamak.','zor','şekilli',4)
Fp,Am,Af,Ar=150,2,8,4
pb_=Fr(Fp,Am); Ff=pb_*Af; Fa=pb_*Ar; Ftop=2*Ff+2*Fa
assert Ff==600 and Fa==300 and Ftop==1800 and 2*Fa==600 and 2*Ff==1200 and 4*Ff==2400 and Fp*(2*Af+2*Ar)==3600
def tek(y,A_,hh,uc):
    return [f'\\draw[thick,fill=vurgu!16] (4.8,{y-hh}) rectangle (5.7,{y+hh});',f'\\draw[thick,fill=gray!45] (5.7,{y-hh}) rectangle (5.9,{y+hh});',f'\\node[font=\\scriptsize] at (5.25,{y}) {{${A_}$ cm$^2$}};',f'\\draw[thick] (3.6,{y}) -- (4.8,{y});',f'\\node[right,font=\\scriptsize] at (6.0,{y}) {{{uc}}};']
o=['\\draw[thick,fill=vurgu!16] (1.5,-.3) rectangle (2.9,.3);','\\draw[thick,fill=gray!45] (1.3,-.3) rectangle (1.5,.3);','\\draw[thick] (.3,0) -- (1.3,0); \\draw[thick] (2.9,0) -- (3.6,0); \\draw[thick] (3.6,-1.8) -- (3.6,1.8);',
   f'\\draw[vurgu,very thick,{ARR}] (-.5,0) -- (.3,0); \\node[vurgu,above] at (-.1,.05) {{$F$}};','\\node[above,font=\\scriptsize] at (2.2,.35) {$2$ cm$^2$};','\\node[below,font=\\scriptsize] at (2.2,-.35) {ana silindir};']
for y,A_,hh,uc in [(1.8,8,.3,'ön'),(.6,8,.3,'ön'),(-.6,4,.21,'arka'),(-1.8,4,.21,'arka')]: o+=tek(y,A_,hh,uc)
SK13=sk(*o)
q('0013',tipId=TIP['fren'][0],tip=TIP['fren'][1],z='zor',alt='Pascal Prensibi',kaz='Farklı alanlı tekerlek silindirleri olan hidrolik fren sisteminde ortak basınçtan toplam kuvveti hesaplar.',kalip='şekilli',
 kart='K-FZBS2-13 (hidrolik fren, ön ve arka silindir) · toplam kuvvet',
 metin='Bir otomobilin hidrolik fren sisteminde, fren pedalından ana silindirin pistonuna 150 N’luk kuvvet iletilmektedir. Ana silindirin, iki ön tekerlek silindirinin ve iki arka tekerlek silindirinin piston alanları şekilde verilmiştir. Sistem sıvıyla tamamen doludur; borular esnemez ve sızdırmazdır, sıvının ağırlığından doğan basınç farkları ve sürtünmeler ihmal edilmektedir. Fren yapıldığında ana silindirde oluşan basınç sıvı içinde her yöne iletilerek dört tekerlek silindirine ulaşmaktadır.\nBuna göre, dört tekerlek silindirinin pistonlarına uygulanan kuvvetlerin toplamı kaç N’dur?',
 sekil=SK13,dogru=1800,yan=[(600,'Yalnız iki arka silindirin kuvvetini toplamış (2 × 300).','dikkat'),(1200,'Yalnız iki ön silindirin kuvvetini toplamış (2 × 600).','dikkat'),(2400,'Dört silindiri de 8 cm² sanıp 4 × 600 almış; arka silindirlerin alanının 4 cm² olduğunu hesaba katmamış.','dikkat'),(3600,'Kuvveti dört silindirin toplam alanıyla (24 cm²) çarpmış (150 × 24); basıncı bulmamış.','islem')],
 istenen='Dört tekerlek silindirindeki kuvvetlerin toplamı (N).',ip=['Önce ana silindirdeki basıncı bul.'],
 bilgi=[B('Pascal ilkesi','Kapalı kaptaki sıvıya uygulanan basınç, sıvının her noktasına ve kap duvarlarına aynen iletilir; bu yüzden F ÷ A her silindirde aynıdır. Örnek: 10 N’luk kuvvet 2 cm²’lik pistona 5 N/cm² basınç yapar; 6 cm²’lik pistonda kuvvet 30 N olur')],
 ad=[A('Ana silindirdeki basıncı bul','Basınç kuvvetin alana oranıdır.','P = 150 ÷ 2 = 75 N/cm²'),A('Ön silindirlerdeki kuvveti bul','Basınç aynen iletilir; kuvvet basınçla alanın çarpımıdır.','F_ön = 75 × 8 = 600 N'),A('Arka silindirlerdeki kuvveti bul','Alan 4 cm² olduğundan kuvvet daha küçüktür.','F_arka = 75 × 4 = 300 N'),A('Toplamı al','İkişer silindir olduğundan her kuvvet iki kez sayılır.','2 × 600 + 2 × 300 = 1800 N')],
 puf='Hidrolik sistemde basınç aynen iletilir; her pistondaki kuvvet, ortak basıncın kendi alanıyla çarpımıdır.')

# ================= 14 · Torricelli · orta · öncüllü =================
K(14,'tor','Açık Hava Basıncı','Torricelli deneyinde cıva sütununun düşey yüksekliği açık hava basıncını belirler; tüpün eğimi, kesiti ve kaptaki yeri bu yüksekliği değiştirmez.','Tüp eğilince ya da kalınlaşınca düşey yüksekliğin değiştiğini sanmak; sütun boyu ile düşey yüksekliği karıştırmak.','orta','öncüllü',3)
hHg=72
s14=.03; cH=hHg*s14; Ltot=3.3
def basin(x): return [f'\\fill[gray!55] ({x-1},-.7) rectangle ({x+1},0);',f'\\draw[thick] ({x-1},.35) -- ({x-1},-.7) -- ({x+1},-.7) -- ({x+1},.35);']
def tube(x,w,ang,col):
    c=math.cos(math.radians(ang)); Lc=col/c; Lt=Ltot; dep=.5/c
    return [f'\\begin{{scope}}[shift={{({x},0)}},rotate={-ang}]',f'\\fill[gray!55] ({-w/2:.3f},{-dep:.3f}) rectangle ({w/2:.3f},{Lc:.3f});',
            f'\\draw[thick] ({-w/2:.3f},{-dep:.3f}) -- ({-w/2:.3f},{Lt:.3f}) -- ({w/2:.3f},{Lt:.3f}) -- ({w/2:.3f},{-dep:.3f});',f'\\draw[thin] ({-w/2:.3f},{Lc:.3f}) -- ({w/2:.3f},{Lc:.3f});','\\end{scope}']
o=[]
for xc,w,ang,nm in [(1.3,.22,0,'K'),(4.4,.22,30,'L'),(8.0,.6,0,'M')]:
    assert Ltot>=cH/math.cos(math.radians(ang))
    o+=basin(xc)+tube(xc,w,ang,cH)+[f'\\node[font=\\small\\bfseries] at ({xc},-1.05) {{{nm}}};']
o+= [f'\\draw[{DIM}] (2.2,0) -- (2.2,{cH:.2f}); \\node[right,font=\\scriptsize] at (2.2,{cH/2:.2f}) {{${hHg}$ cm}};']
SK14=sk(*o)
onc('0014',{1},pick(0,1,2,3,6),
 {1:'Cıva sütununun düşey yüksekliği açık hava basıncına göre belirlenir ve tüpün eğik olmasından etkilenmez: L düzeneğinde de 72 cm’dir.',
  2:'Sütunun düşey yüksekliği tüpün kesit alanına bağlı değildir; geniş tüpte hem ağırlık hem alan artar, basınç (d · g · h) aynı kalır. M’de de 72 cm’dir.',
  3:'Eğik tüpte cıva sütununun boyu, eğik kenar olduğundan düşey yükseklikten (72 cm) büyüktür; 72 cm değildir.'},
 'Aynı yerde ve aynı sıcaklıkta üç ayrı Torricelli düzeneği kuruluyor. K düzeneğinde dik ve ince bir cam tüp, L düzeneğinde K’dakiyle aynı boyda ve aynı kesitte tüp düşeyle bir açı yapacak biçimde eğik, M düzeneğinde ise K’dakinden daha geniş kesitli dik bir tüp kullanılmıştır. Tüplerin hepsi, sütunu alacak kadar uzundur; önce cıvayla doldurulmuş, sonra ağzı kapatılıp büyük birer cıva kabına ters çevrilerek açılmıştır. Tüplerin üst kısmındaki boşlukta hava yoktur ve kaptaki cıva seviyesi değişmemektedir. Şekilde K düzeneğindeki cıva sütununun düşey yüksekliği verilmiştir.\nBuna göre,\nI. L düzeneğinde cıva sütununun düşey yüksekliği 72 cm’dir.\nII. M düzeneğinde cıva sütununun düşey yüksekliği 72 cm’den küçüktür.\nIII. L düzeneğinde tüp içindeki cıva sütununun boyu 72 cm’dir.\nyargılarından hangileri doğrudur?',
 tipId=TIP['tor'][0],tip=TIP['tor'][1],z='orta',alt='Açık Hava Basıncı',kaz='Torricelli deneyinde tüpün eğimi ve kesitinin cıva sütununun düşey yüksekliğini değiştirmediğini yorumlar.',
 kart='K-FZBS2-14 (Torricelli, eğik ve geniş tüp) · öncüllü',istenen='Doğru olan yargılar.',ip=['Cıva sütununu dengede tutan şeyin ne olduğunu ve bu basıncı hangi niceliğin belirlediğini düşün.'],
 bilgi=[B('Torricelli deneyi','Tüpteki cıva sütununun uyguladığı basınç açık hava basıncına eşittir: P₀ = d · g · h. Bu yüzden düşey yükseklik h yalnız açık hava basıncına bağlıdır; tüpün eğimine ve kesitine bağlı değildir. Deniz seviyesinde h ≈ 76 cm’dir (76 cmHg)')],
 puf='Torricelli deneyinde yalnız düşey yükseklik açık hava basıncını gösterir; tüpü eğmek sütun boyunu uzatır, yüksekliği değiştirmez.',sekil=SK14)

# ================= 15 · manometre · kolay =================
K(15,'man','Gaz Basıncı','Açık uçlu manometrede gaz basıncı, açık hava basıncı ile seviye farkının toplamı ya da farkıdır; cıvası daha yüksek olan kol daha düşük basınçtadır.','Seviye farkını yanlış işaretle eklemek; yalnız seviye farkını almak.','kolay','şekilli',2)
P0m,hm=70,15
assert P0m+hm==85 and P0m-hm==55 and P0m+2*hm==100
s15=.08; yL=.9; yR=yL+hm*s15
o=['\\draw[thick,fill=gray!8] (0,1.5) rectangle (1.6,2.8); \\node[font=\\small] at (.8,2.15) {gaz};',
   f'\\fill[gray!55] (3.0,{yL}) -- (3.0,0) -- (4.6,0) -- (4.6,{yR:.2f}) -- (4.2,{yR:.2f}) -- (4.2,.4) -- (3.4,.4) -- (3.4,{yL}) -- cycle;',
   '\\draw[thick] (1.6,1.9) -- (3.4,1.9) -- (3.4,.4) -- (4.2,.4) -- (4.2,3.1);','\\draw[thick] (1.6,2.3) -- (3.0,2.3) -- (3.0,0) -- (4.6,0) -- (4.6,3.1);',
   f'\\draw[dashed] (3.4,{yL}) -- (5.0,{yL}); \\draw[dashed] (4.2,{yR:.2f}) -- (5.0,{yR:.2f});',
   f'\\draw[{DIM}] (5.0,{yL}) -- (5.0,{yR:.2f}); \\node[right,font=\\scriptsize] at (5.0,{(yL+yR)/2:.2f}) {{${hm}$ cm}};',
   '\\node[above,font=\\scriptsize] at (4.4,3.1) {açık uç};']
SK15=sk(*o)
q('0015',tipId=TIP['man'][0],tip=TIP['man'][1],z='kolay',alt='Gaz Basıncı',kaz='Açık uçlu cıvalı manometrede seviye farkından kapalı kaptaki gazın basıncını bulur.',kalip='şekilli',
 kart='K-FZBS2-15 (açık uçlu manometre) · gaz basıncı',
 metin='Bir öğrenci, içinde gaz bulunan kapalı bir kabı şekildeki gibi cıva dolu, bir ucu açık cam U borusuna bağlayarak gazın basıncını ölçmek istiyor. Cıva dengeye geldiğinde iki koldaki cıva seviyeleri arasındaki düşey fark şekilde verilmiştir. Deneyin yapıldığı yerde açık hava basıncı 70 cmHg’dir ve cıva sütununun ağırlığı dışındaki etkiler ihmal edilmektedir.\nBuna göre, kaptaki gazın basıncı kaç cmHg’dir?',
 sekil=SK15,dogru=85,yan=[(15,'Yalnız cıva seviye farkını gaz basıncı sanmış; açık hava basıncını eklememiş.','dikkat'),(55,'Seviye farkını açık hava basıncından çıkarmış; hangi kolda cıvanın yüksek olduğuna bakmamış.','islem'),(70,'Gaz basıncını açık hava basıncına eşit sanmış; seviye farkının basınç farkı yarattığını fark etmemiş.','bilgi'),(100,'Seviye farkını iki kez eklemiş (70 + 2 × 15).','islem')],
 istenen='Kaptaki gazın basıncı (cmHg).',ip=['Cıvanın hangi kolda daha yüksekte durduğuna bakarak gazın basıncının açık hava basıncından büyük mü küçük mü olduğunu belirle.'],
 bilgi=[B('Açık uçlu manometre','Gaz tarafındaki cıva seviyesi alçaksa gaz basıncı açık hava basıncından seviye farkı kadar büyüktür: P_gaz = P₀ + h; gaz tarafı yüksekse P_gaz = P₀ − h. Örnek: P₀ = 76 cmHg, açık kolda cıva 4 cm alçaktaysa P_gaz = 72 cmHg')],
 ad=[A('Seviyeleri karşılaştır','Gaz tarafındaki cıva seviyesi daha aşağıdadır; yani gaz cıvayı açık kola doğru itmektedir.','P_gaz > P₀'),A('Basıncı yaz','Fark, cıva sütununun basıncı kadardır.','P_gaz = P₀ + h = 70 + 15'),A('Sonucu bul','Sonuç cmHg cinsinden verilir.','P_gaz = 85 cmHg')],
 puf='Manometrede cıvanın alçak olduğu taraf yüksek basınçtadır; basınç farkı seviye farkı kadardır.')

# ================= 16 · barometre tablosu · orta · öncüllü =================
K(16,'bar','Açık Hava Basıncı','Yükseldikçe açık hava basıncı azalır; cıvalı barometrede sütun kısalır. Düşük basınçta suyun kaynama sıcaklığı da düşer.','Yükseldikçe basıncın arttığını sanmak; daha kısa cıva sütununu daha düşük rakım sanmak.','orta','tablo',3)
bar=[('K',76),('L',64),('M',70)]
assert min(bar,key=lambda t:t[1])[0]=='L' and bar[2][1]<bar[0][1] and bar[0][1]>bar[2][1]
SK16=tablo_svg(['Nokta','Cıva sütununun düşey yüksekliği (cm)'],[[n,h] for n,h in bar])
onc('0016',{1,2,3},pick(0,1,2,4,6),
 {1:'Yükseldikçe açık hava basıncı azalır; cıva sütunu en kısa (64 cm) olan L’de basınç en küçüktür, yani L en yüksektedir.',
  2:'Açık hava basıncı azaldıkça suyun kaynama sıcaklığı düşer; M’de basınç (70 cmHg) K’dakinden (76 cmHg) küçük olduğundan su daha düşük sıcaklıkta kaynar.',
  3:'Cıva sütununun yüksekliği açık hava basıncını gösterir; K’de 76 cmHg, M’de 70 cmHg olduğundan K’deki basınç büyüktür.'},
 'Coğrafya gezisine çıkan öğrenciler, deniz seviyesinden farklı yüksekliklerdeki K, L ve M noktalarında aynı cıvalı barometreyi kurup cıva sütununun düşey yüksekliğini ölçüyor. Ölçümler aynı sıcaklıkta, tüp dik tutularak yapılmış ve sonuçlar aşağıdaki tabloda toplanmıştır. Her noktada tüpün üst kısmındaki boşlukta hava yoktur ve cıva kabındaki seviye değişmemektedir.\nBuna göre,\nI. Deniz seviyesinden en yüksekteki nokta L’dir.\nII. M noktasında su, K noktasındakinden daha düşük sıcaklıkta kaynar.\nIII. K noktasındaki açık hava basıncı, M noktasındakinden büyüktür.\nyargılarından hangileri doğrudur?',
 tipId=TIP['bar'][0],tip=TIP['bar'][1],z='orta',alt='Açık Hava Basıncı',kaz='Barometre ölçümlerinden yükselti, açık hava basıncı ve kaynama sıcaklığı ilişkisini yorumlar.',
 kart='K-FZBS2-16 (barometre tablosu, yükselti) · öncüllü',istenen='Doğru olan yargılar.',ip=['Cıva sütunu yüksekliğinin hangi basıncı gösterdiğini ve basıncın yükseldikçe nasıl değiştiğini düşün.'],
 bilgi=[B('Açık hava basıncı ve yükselti','Hava tabakası yükseldikçe incelir, açık hava basıncı azalır; cıvalı barometrede sütun kısalır. Basınç azalınca suyun kaynama sıcaklığı da düşer. Örnek: dağ başında deniz seviyesine göre daha kısa cıva sütunu ölçülür')],
 puf='Cıva sütunu ne kadar kısaysa açık hava basıncı o kadar düşüktür; bu da yerin daha yüksekte olduğunu ve suyun daha düşük sıcaklıkta kaynadığını gösterir.',sekil=SK16)

# ================= 17 · kapalı kapta gaz · orta · öncüllü =================
K(17,'gaz','Gaz Basıncı','Gaz basıncı, moleküllerin kap çeperine çarpmasından doğar; molekül sayısı arttıkça ve hacim küçüldükçe ya da sıcaklık arttıkça basınç büyür.','Hacmi büyük kapta basıncın da büyük olacağını sanmak; sıcaklık artınca basıncın azalacağını sanmak.','orta','öncüllü',3)
rng=random.Random(7)
def noktalar(x0,y0,w,h,n):
    pts=[]
    while len(pts)<n:
        p=(x0+.15+rng.random()*(w-.3),y0+.15+rng.random()*(h-.3))
        if all((p[0]-q_[0])**2+(p[1]-q_[1])**2>.065 for q_ in pts): pts.append(p)
    return pts
o=[]
for x0,w,n,et,V in [(0,1.5,6,'K','V'),(2.2,1.5,12,'L','V'),(4.4,3.0,6,'M','2V')]:
    o.append(f'\\draw[thick,fill=gray!6] ({x0},0) rectangle ({x0+w},1.5);')
    for p in noktalar(x0,0,w,1.5,n): o.append(f'\\fill ({p[0]:.2f},{p[1]:.2f}) circle (.06);')
    o.append(f'\\node[font=\\small\\bfseries] at ({x0+w/2},-.35) {{{et}}}; \\node[font=\\scriptsize] at ({x0+w/2},1.75) {{hacim: ${V}$}};')
SK17=sk(*o)
onc('0017',{1,2},pick(0,3,4,5,6),
 {1:'Molekül sayısı ve sıcaklık aynıyken hacim büyüyünce moleküller çeperlere daha seyrek çarpar; M’deki basınç K’dakinden küçüktür.',
  2:'Hacim ve sıcaklık aynıyken molekül sayısı 2 katına çıkınca çeperlere birim zamandaki çarpma sayısı artar; L’deki basınç K’dakinden büyüktür.',
  3:'Hacim sabitken sıcaklık artınca moleküllerin hızı artar, çeperlere daha sık ve daha şiddetli çarparlar; gazın basıncı artar, azalmaz.'},
 'Hacimleri şekilde gösterilen K, L ve M kapalı kaplarında aynı cins gaz bulunmaktadır. Kaplar aynı odada uzun süre bekletildiğinden üç kaptaki gazın sıcaklığı eşittir. Şekildeki her nokta, aynı sayıda molekülü temsil etmektedir ve kapların cidarları sert, sızdırmazdır. Bir öğrenci, kaplardaki gazların basınçlarını moleküllerin kap cidarına çarpması modeliyle karşılaştırıyor.\nBuna göre,\nI. M kabındaki gazın basıncı, K kabındakinden küçüktür.\nII. L kabındaki gazın basıncı, K kabındakinden büyüktür.\nIII. K kabındaki gazın sıcaklığı hacim sabit kalacak biçimde yükseltilirse gazın basıncı azalır.\nyargılarından hangileri doğrudur?',
 tipId=TIP['gaz'][0],tip=TIP['gaz'][1],z='orta',alt='Gaz Basıncı',kaz='Kapalı kaptaki gazın basıncını hacim, molekül sayısı ve sıcaklıkla ilişkilendirerek nitel olarak yorumlar.',
 kart='K-FZBS2-17 (kapalı kapta gaz basıncı) · öncüllü',istenen='Doğru olan yargılar.',ip=['Gaz basıncını, moleküllerin cidara birim alana ve birim zamanda yaptığı çarpma ile ilişkilendirip hangi durumda çarpmaların arttığını düşün.'],
 bilgi=[B('Kapalı kapta gaz basıncı','Gaz moleküllerinin kap çeperine çarpması basınç oluşturur. Molekül sayısı artınca, hacim küçülünce ya da sıcaklık yükselince basınç artar. Örnek: şişirilmiş bir balonu sıkıştırınca içindeki gazın basıncı artar')],
 puf='Gaz basıncı; molekül sayısı ve sıcaklıkla doğru, hacimle ters yönde değişir.',sekil=SK17)

# ================= 18 · Bernoulli, boru · orta · öncüllü =================
K(18,'ber','Akışkanların Basıncı','Kesit alanı küçüldükçe akışkanın hızı artar ve basıncı azalır; kararlı akışta her kesitten birim zamanda geçen hacim aynıdır.','Dar yerde basıncın büyük olduğunu sanmak; hızı kesitle doğru orantılı almak.','orta','öncüllü',3)
Ak,Am_,Al=12,6,3
assert Fr(Al,Ak)==Fr(1,4) and Fr(Ak,Al)==4
o=['\\fill[vurgu!14] (0,.6) -- (1.6,.6) -- (2.4,.425) -- (3.6,.425) -- (4.4,.3) -- (6,.3) -- (6,-.3) -- (4.4,-.3) -- (3.6,-.425) -- (2.4,-.425) -- (1.6,-.6) -- (0,-.6) -- cycle;',
   '\\draw[thick] (0,.6) -- (1.6,.6) -- (2.4,.425) -- (3.6,.425) -- (4.4,.3) -- (6,.3);','\\draw[thick] (0,-.6) -- (1.6,-.6) -- (2.4,-.425) -- (3.6,-.425) -- (4.4,-.3) -- (6,-.3);',
   f'\\draw[vurgu,very thick,{ARR}] (-.9,0) -- (-.1,0); \\node[vurgu,above,font=\\scriptsize] at (-.5,.05) {{akış}};']
for xk,yk,nm,a in [(.8,.65,'K',Ak),(3.0,.5,'M',Am_),(5.2,.35,'L',Al)]:
    o.append(f'\\node[above,font=\\scriptsize] at ({xk},{yk}) {{{nm}: ${a}$ cm$^2$}};')
SK18=sk(*o)
onc('0018',{2,3},pick(0,1,2,3,5),
 {1:'Kararlı akışta A · v sabittir; kesit alanı küçüldükçe hız artar. L’nin kesiti K’ninkinden küçük olduğundan hız L’de daha büyüktür; K’deki hız L’dekinden büyük değildir.',
  2:'Boru yatay olduğundan hız arttıkça basınç azalır (Bernoulli); hızın en büyük olduğu, kesiti en dar L bölgesinde basınç en küçüktür.',
  3:'Sıvı sıkışmaz ve akış kararlıdır; her kesitten birim zamanda geçen hacim (debi, A · v) eşittir.'},
 'Yatay konumdaki, kesit alanı değişen bir borudan sıkıştırılamaz ve sürtünmesi ihmal edilebilir bir sıvı, şekildeki yönde kararlı biçimde akmaktadır. Borunun K, M ve L bölgelerindeki kesit alanları şekilde verilmiştir. Boru yatay olduğundan yükseklik farkından doğan basınç değişimi yoktur ve her bölgede akış, kesit boyunca düzgün kabul edilecektir. Bir öğrenci, sıvının hızı, basıncı ve akış miktarı hakkında çıkarımlar yapıyor.\nBuna göre,\nI. Sıvının hızı K bölgesinde L bölgesindekinden büyüktür.\nII. Sıvının basıncı en küçük L bölgesindedir.\nIII. K, M ve L kesitlerinden birim zamanda geçen sıvı hacmi eşittir.\nyargılarından hangileri doğrudur?',
 tipId=TIP['ber'][0],tip=TIP['ber'][1],z='orta',alt='Akışkanların Basıncı',kaz='Kesit alanı değişen yatay borudaki akışta hız, basınç ve debi ilişkisini süreklilik ve Bernoulli ilkesiyle yorumlar.',
 kart='K-FZBS2-18 (Bernoulli, değişen kesitli boru) · öncüllü',istenen='Doğru olan yargılar.',ip=['Kararlı akışta birim zamanda geçen hacmin her kesitte aynı olduğunu kullanarak önce hız–kesit ilişkisini kur, sonra basınca geç.'],
 bilgi=[B('Bernoulli ilkesi','Yatay akışta akışkanın hızı arttıkça basıncı azalır. Kararlı akışta A · v her kesitte aynıdır; dar kesitte hız büyüktür. Örnek: kesit alanı yarıya inen yerde akışkan 2 kat hızlı akar ve basıncı daha düşüktür')],
 puf='Yatay boruda dar kesitte hız artar, basınç düşer; birim zamanda geçen hacim ise her kesitte aynıdır.',sekil=SK18)

# ================= 19 · iki kâğıt şerit, günlük Bernoulli · kolay =================
K(19,'gun','Akışkanların Basıncı','Hızlı akan havada basınç düşer; aradaki basınç azalınca dışarıdaki büyük basınç cisimleri birbirine yaklaştırır.','Hızlanan havada basıncın arttığını sanmak.','kolay','şekilli',2)
o=['\\draw[thick,fill=gray!40] (-.25,3.0) rectangle (.35,3.3); \\draw[thick,fill=gray!40] (.75,3.0) rectangle (1.35,3.3);',
   '\\draw[thick,fill=gray!15] (0,0) rectangle (.1,3.0); \\draw[thick,fill=gray!15] (1.0,0) rectangle (1.1,3.0);',
   f'\\draw[vurgu,very thick,{ARR}] (.55,3.3) -- (.55,.8); \\node[vurgu,right,font=\\scriptsize,align=center] at (.6,2.2) {{hızlı\\\\hava}};',
   '\\node[left,font=\\scriptsize,align=center] at (-.15,1.4) {durgun\\\\hava}; \\node[right,font=\\scriptsize,align=center] at (1.25,1.4) {durgun\\\\hava};',
   '\\node[font=\\scriptsize] at (.55,-.3) {kâğıt şeritler};']
SK19=sk(*o)
sec19=['Aralarındaki hava hızlandığı için basınç düşer; dıştaki hava şeritleri iter.','Aralarındaki hava hızlandığı için basınç artar; artan basınç şeritleri birbirine doğru iter.','Üflenen hava şeritlere çarparak onları birbirine doğru iter.','Şeritlerin arasında hava sürtünmesi arttığından şeritler akış yönünde birbirine yapışır.','Şeritlerin arasındaki basınç dıştakinden büyük olduğundan şeritler birbirine yaklaşır.']
q('0019',tipId=TIP['gun'][0],tip=TIP['gun'][1],z='kolay',alt='Akışkanların Basıncı',kaz='Hızlı akan havada basıncın azalmasını günlük bir olaya uygulayarak nedenini açıklar.',kalip='şekilli',
 kart='K-FZBS2-19 (iki kâğıt şerit arasına üfleme) · Bernoulli',
 metin='Bir öğrenci, iki ince kâğıt şeridi parmaklarıyla üst uçlarından tutarak şekildeki gibi birbirine paralel ve düşey olarak sarkıtıyor. Daha sonra şeritlerin arasına yukarıdan aşağıya doğru kuvvetle üflediğinde, şeritlerin kendiliğinden birbirine yaklaştığını görüyor. Şeritlerin dış yüzlerinde hava durgundur ve oda sıcaklığı üfleme sırasında değişmemektedir.\nBuna göre, şeritlerin birbirine yaklaşmasının nedeni aşağıdakilerden hangisidir?',
 sekil=SK19,dogru=sec19[0],sira=sec19,yan=[(sec19[1],'Hızlanan havanın basıncının arttığını sanmış; Bernoulli ilkesine göre hız artınca basınç azalır.','bilgi'),(sec19[2],'Üflenen havanın şeritlere çarparak itme etkisi yaptığını sanmış; oysa şeritler üfleme yönünde değil, birbirine doğru hareket eder.','dikkat'),(sec19[3],'Hızlı havanın sürtünmeyle şeritleri yapıştırdığını sanmış; olayı basınç farkıyla değil sürtünmeyle açıklamış.','bilgi'),(sec19[4],'Basıncı büyük olan yerin şeritleri çekeceğini sanmış; basınç farkı, basıncı büyük olan taraftan küçük olana doğru iter.','bilgi')],
 istenen='Şeritlerin birbirine yaklaşma nedeni.',ip=['Şeritlerin arasındaki ve dışındaki havanın hızını karşılaştırıp bunun basıncı nasıl etkilediğini düşün.'],
 bilgi=[B('Bernoulli ilkesi','Akışkanın hızlı aktığı yerde basınç küçük, yavaş ya da durgun olduğu yerde basınç büyüktür. Cisim, basıncın büyük olduğu taraftan küçük olduğu tarafa doğru itilir. Örnek: hızla geçen bir trenin yanındaki yolcu, trene doğru çekilme eğilimi hisseder')],
 ad=[A('Havanın hızını karşılaştır','Arası üflenen şeritlerin iç tarafında hava hızlı, dış tarafında durgundur.','v_iç > v_dış'),A('Basıncı karşılaştır','Bernoulli ilkesine göre hızın büyük olduğu yerde basınç küçüktür.','P_iç < P_dış'),A('Kuvvetin yönünü bul','Dıştaki büyük basınç şeritleri basıncın küçük olduğu iç tarafa iter.','Şeritler birbirine yaklaşır')],
 puf='Hızlı akan havada basınç azalır; cisimler basıncı büyük taraftan küçük tarafa doğru itilir.')

# ================= 20 · hâl değişimi, kaynama sıcaklığı grafiği · orta =================
K(20,'hal','Basıncın Hâl Değişimine Etkisi','Suyun kaynama sıcaklığı dış basınçla artar; grafikten farklı basınçlardaki kaynama sıcaklıkları okunup farkları hesaplanır.','Basınç ile sıcaklık farkını karıştırmak; iki okuma arasındaki yanlış çifti çıkarmak.','orta','grafik',3)
nk,nl,nm=(60,85),(100,100),(200,120)
assert nm[1]-nk[1]==35 and nl[1]-nk[1]==15 and nm[1]-nl[1]==20 and nm[0]-nk[0]==140
cur=[(20,60),(40,75),(60,85),(80,94),(100,100),(150,111),(200,120),(220,123)]
GR='\\begin{axis}[width=8.2cm,height=6.0cm,xmin=0,xmax=230,ymin=55,ymax=130,xtick distance=40,ytick distance=10,minor y tick num=1,grid=both,major grid style={gray!55,thin},minor grid style={gray!30,very thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={Dış basınç (kPa)},ylabel={Kaynama sıcaklığı ($^\\circ$C)},xlabel style={font=\\small},ylabel style={font=\\small}]'
gs=GR+'\\addplot[thick,smooth] coordinates {'+' '.join(f'({a},{b})' for a,b in cur)+'};'+'\\addplot[only marks,mark=*,mark size=2pt,vurgu] coordinates {'+' '.join(f'({a},{b})' for a,b in (nk,nl,nm))+'};'
gs+=f'\\node[above left] at (axis cs:{nk[0]},{nk[1]}) {{K}}; \\node[below right] at (axis cs:{nl[0]},{nl[1]}) {{L}}; \\node[below right] at (axis cs:{nm[0]},{nm[1]}) {{M}};\\end{{axis}}'
SK20=sk(gs)
q('0020',tipId=TIP['hal'][0],tip=TIP['hal'][1],z='orta',alt='Basıncın Hâl Değişimine Etkisi',kaz='Kaynama sıcaklığı–basınç grafiğinden farklı ortamlardaki kaynama sıcaklıklarını okuyup yorumlar.',kalip='grafik',
 kart='K-FZBS2-20 (kaynama sıcaklığı–basınç grafiği) · K, L, M noktaları',
 metin='Bir fizik kitabında, saf suyun kaynamaya başladığı sıcaklığın dış basınca göre değişimini gösteren grafik yer almaktadır. Grafikte üç ortam işaretlenmiştir: çok yüksek bir dağın zirvesi (K), deniz kenarı (L) ve içindeki basıncı yükselten bir düdüklü tencere (M). Her ortamda su açık hava basıncı ya da kapağın uyguladığı basınç altında kaynatılmıştır ve sıcaklıklar grafikten okunacaktır.\nBuna göre, M ortamındaki suyun kaynama sıcaklığı ile K ortamındaki suyun kaynama sıcaklığı arasındaki fark kaç °C’dir?',
 sekil=SK20,dogru=35,yan=[(15,'L ile K noktalarının sıcaklıklarını karşılaştırmış (100 − 85); M’yi hesaba katmamış.','dikkat'),(20,'M ile L noktalarının sıcaklıklarını karşılaştırmış (120 − 100); K’yi hesaba katmamış.','dikkat'),(85,'K noktasının sıcaklığını fark sanmış; M’nin değerini çıkarmamış.','dikkat'),(140,'Sıcaklık farkı yerine basınç farkını (200 − 60) almış.','dikkat')],
 istenen='T_M − T_K (°C).',ip=['Her iki noktanın kaynama sıcaklığını dikey eksenden ayrı ayrı oku, sonra yalnız sıcaklıkları karşılaştır.'],
 bilgi=[B('Basıncın kaynama sıcaklığına etkisi','Dış basınç artınca sıvının kaynama sıcaklığı yükselir, azalınca düşer. Bu yüzden düdüklü tencerede yemek daha çabuk pişer, yüksek dağlarda su daha düşük sıcaklıkta kaynar. Örnek: dağda su 100 °C’den önce kaynar')],
 ad=[A('K noktasını oku','K’nin basıncı 60 kPa’dır; karşısındaki sıcaklık dikey eksenden okunur.','T_K = 85 °C'),A('M noktasını oku','M’nin basıncı 200 kPa’dır.','T_M = 120 °C'),A('Farkı al','Sıcaklıklar birbirinden çıkarılır; basınçlar kullanılmaz.','120 − 85 = 35 °C')],
 puf='Grafikte istenen büyüklüğün eksenini belirle ve yalnız o ekseni okuyarak karşılaştır.')

bitir(P,'basinciki','fiz|Basınç')
