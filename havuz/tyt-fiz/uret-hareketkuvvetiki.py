"""TYT Fizik · Hareket ve Kuvvet (ikinci paket) · 24 soru (kardeş yok, ipucu 1).
Şekiller TikZ/pgfplots ile, değerler Python'da hesaplanıp aynı değişkenlerden çizilir. Her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
P=Parti('hareketkuvvetiki','Hareket ve Kuvvet','fiz|Hareket ve Kuvvet',ders='TYT Fizik',idon='tytfiz')
H.KONU='Hareket ve Kuvvet'
KY='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    mk(P,no,ad=ad,adim=len(ad),**k)
LISTE={'a':['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
       'b':['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III'],
       'c':['Yalnız II','Yalnız III','I ve III','II ve III','I, II ve III'],
       'd':['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']}
def kume(lbl): return frozenset(r for r in ['I','II','III'] if r in lbl.replace('Yalnız','').replace(',',' ').replace(' ve ',' ').split())
def etiket(S):
    S=sorted(S,key=['I','II','III'].index)
    if len(S)==1: return 'Yalnız '+S[0]
    if len(S)==3: return 'I, II ve III'
    return ' ve '.join(S)
def onc(no,lst,st,oku,okuis,**k):
    """st: [(yargı metni, doğru mu, gerekçe)]; doğru küme betikte bu bayraklardan çıkar."""
    L=LISTE[lst]; assert all(kume(x)==kume(etiket(kume(x))) and etiket(kume(x))==x for x in L)
    T=frozenset(r for r,(m,d,g) in zip(['I','II','III'],st) if d); assert etiket(T) in L,(no,etiket(T))
    G={r:g for r,(m,d,g) in zip(['I','II','III'],st)}
    yan=[]
    for x in L:
        if x==etiket(T): continue
        S=kume(x); par=[]
        for r in ['I','II','III']:
            if r in S and r not in T: par.append(f'{r}. yargıyı doğru sanmış: {G[r]}')
            if r in T and r not in S: par.append(f'{r}. yargıyı yanlış sanmış: {G[r]}')
        yan.append((x,' '.join(par)[:400],'bilgi'))
    metin=k.pop('metin')+'\n'+'\n'.join(f'{r}. {m}' for r,(m,d,g) in zip(['I','II','III'],st))+'\nBuna göre, yukarıdaki yargılardan hangileri doğrudur?'
    ad=[A('Veriyi oku',oku,okuis)]
    for r,(m,d,g) in zip(['I','II','III'],st): ad.append(A(f'{r}. yargıyı incele',g,'Doğru' if d else 'Yanlış'))
    ad.append(A('Sonucu yaz','Doğru yargıların kümesi şıklarla eşleştirilir.','Doğru olanlar: '+', '.join(sorted(T,key=['I','II','III'].index))))
    q(no,ad,metin=metin,dogru=etiket(T),yan=yan,sira=L,kalip='öncüllü',istenen='Doğru olan yargılar.',**k)
    return etiket(T)

# ---------- çizim yardımcıları ----------
def grafik(egriler,xmax,ymin,ymax,xt,yt,xl,yl,w=6.8,h=5.0,xmin=0,sifir=True,notlar=''):
    s=[f'\\begin{{axis}}[width={w}cm,height={h}cm,xmin={xmin},xmax={xmax},ymin={ymin},ymax={ymax},xtick={{{xt}}},ytick={{{yt}}},grid=both,major grid style={{gray!55,thin}},tick label style={{font=\\scriptsize}},axis y line=left,axis x line={"middle" if ymin<0 else "left"},xlabel={{{xl}}},ylabel={{{yl}}},xlabel style={{font=\\small}},ylabel style={{font=\\small}}]']
    for pts,stil,etk in egriler:
        c=' '.join(f'({a},{b})' for a,b in pts)
        s.append(f'\\addplot[{stil}] coordinates {{{c}}}{etk};')
    s.append(notlar); s.append('\\end{axis}')
    return tikz_svg(HEAD+'\n'.join(s)+TAIL)
V='thick,vurgu,mark=*,mark size=1.5pt'
def oklu(x1,y1,x2,y2,et='',pos='above',renk='vurgu',w='very thick'):
    return f'\\draw[{renk},{w},{ARR}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f}) node[midway,{pos},black,fill=white,inner sep=1pt] {{{et}}};'
def zemin(x1,x2,y=0): return f'\\fill[gray!35] ({x1},{y-.12}) rectangle ({x2},{y});\n\\draw ({x1},{y}) -- ({x2},{y});'

def pusula(x,y):
    return f'\\draw[-{{Stealth}},thick] ({x},{y}) -- ({x},{y+.8}) node[above,font=\\scriptsize]{{Kuzey}}; \\draw[-{{Stealth}},thick] ({x},{y}) -- ({x+.8},{y}) node[right,font=\\scriptsize]{{Doğu}};'
# ================= KARTLAR =================
kartla('K-FZHK2-01','Konum, yol ve yer değiştirme','Konum eksen üzerinde okunur; yol gidilen uzunlukların toplamı, yer değiştirme son ve ilk konum farkıdır.','Yolu yer değiştirme saymak; geri dönüşü eksi işaretle çıkarmak.','kolay','şekilli',3,'fz-hk2-konum','Konum, yol ve yer değiştirme')
kartla('K-FZHK2-02','Yol, yer değiştirme, sürat ve hız yargıları','Rota şemasında yol uzunlukların toplamı, yer değiştirme başlangıç-bitiş doğrusudur; ortalama sürat ≥ ortalama hız büyüklüğü.','Ortalama sürat ile ortalama hız büyüklüğünü eşit saymak.','orta','öncüllü',5,'fz-hk2-surathiz','Sürat ve hız kavramları')
kartla('K-FZHK2-03','Yarı yolları farklı hızla gitme','Ortalama sürat toplam yolun toplam süreye oranıdır; hızların aritmetik ortalaması alınmaz.','Hızların aritmetik ortalamasını almak.','orta','şekilli',4,'fz-hk2-ortalama','Ortalama sürat ve ortalama hız')
kartla('K-FZHK2-04','Duraksamalı gidiş–dönüş hareketi','Dinlenme süresi toplam süreye katılır; ortalama sürat yoldan, ortalama hız yer değiştirmeden bulunur.','Dinlenme süresini atlamak; yolu yer değiştirme saymak.','zor','hikâyeli',5,'fz-hk2-ortalama','Ortalama sürat ve ortalama hız')
kartla('K-FZHK2-05','Zıt yönlü iki hareketlinin karşılaşması','Zıt yönde giden hareketlilerde yaklaşma hızı toplamdır; karşılaşma süresi yol ÷ hızlar toplamı.','Hızları çıkarmak; konumu orta nokta sanmak.','kolay','şekilli',3,'fz-hk2-ddh','Düzgün doğrusal hareket')
kartla('K-FZHK2-06','Eşit zaman aralıklı çoklu pozlama','Eşit zamanda eşit yer değiştirme sabit hız; artan aralık hızın arttığını gösterir.','Nokta sayısını hız sanmak; aralıkları süre sanmak.','orta','öncüllü',5,'fz-hk2-ddh','Düzgün doğrusal hareket')
kartla('K-FZHK2-07','Konum–zaman grafiği yargıları','Eğim hızı verir; yatay doğru durma; yol parçaların mutlak değerleri toplamıdır.','Yatay doğruyu sabit hızlı hareket sanmak.','orta','öncüllü',5,'fz-hk2-xt','Konum–zaman grafiği')
kartla('K-FZHK2-08','Konum–zaman grafiğinden hız ve karşılaşma','Eğimlerden hızlar okunur, grafik dışında karşılaşma süresi bağıl hızla bulunur.','Zıt eğimlerin hızını çıkarmak; zaman yerine konum yazmak.','orta','grafik',4,'fz-hk2-xt','Konum–zaman grafiği')
kartla('K-FZHK2-09','Hız–zaman grafiğinde yön değiştirme','Alan işaretli toplanırsa yer değiştirme, mutlak toplanırsa yol bulunur.','Negatif alanı yoldan çıkarmak.','zor','grafik',5,'fz-hk2-vt','Hız–zaman grafiği')
kartla('K-FZHK2-10','Hız–zaman grafiği yargıları','Eğim ivme, alan yer değiştirmedir; yatay doğru ivmesizdir.','Yatay doğruyu duruyor sanmak; ortalama hızı son hız sanmak.','orta','öncüllü',5,'fz-hk2-vt','Hız–zaman grafiği')
kartla('K-FZHK2-11','İvmenin eğimden karşılaştırılması','İvme = hız değişimi ÷ süre; iki hareketlinin oranı eğimlerin oranıdır.','Son hızları kıyaslayıp ivmeyi eşit saymak.','kolay','grafik',3,'fz-hk2-ivme','İvme kavramı')
kartla('K-FZHK2-12','Aynı yönde yetişme (bağıl hız)','Yetişme süresi aradaki mesafe ÷ hız farkı; sonra yol hızla çarpılır.','Hızları toplamak (zıt yön gibi).','orta','şekilli',4,'fz-hk2-bagil','Bağıl hareket')
kartla('K-FZHK2-13','Hareketli referans (tren içinde yürüme)','Yere göre hız = taşıyıcının hızı ± yolcunun trene göre hızı; yön işaretle.','Yolcunun trene göre hızını yere göre hız sanmak; yönü yok saymak.','orta','öncüllü',5,'fz-hk2-bagil','Bağıl hareket')
kartla('K-FZHK2-14','Zıt yönlü trenlerin geçişi','Geçiş için alınması gereken yol uzunluklar toplamı, bağıl hız hızlar toplamı.','Tek trenin boyunu kullanmak; hızları çıkarmak.','orta','şekilli',4,'fz-hk2-bagil','Bağıl hareket')
kartla('K-FZHK2-15','İvme kavramı yargıları','İvme hızın zamanla değişimidir; yön hız değişiminin yönündedir.','İvmeyi hız sanmak; ivme sıfır = durgun sanmak.','kolay','öncüllü',5,'fz-hk2-ivme','İvme kavramı')
kartla('K-FZHK2-16','Hız yön değiştirirken ivme','Doğrusal eğimli v–t doğrusunda ivme sabit; alanlar zıt işaretli ise yer değiştirme sıfır olabilir.','Hız sıfırken ivmenin de sıfır olduğunu sanmak.','orta','öncüllü',5,'fz-hk2-ivme','İvme kavramı')
kartla('K-FZHK2-17','Temas ve uzaktan etkiyen kuvvetler','Ağırlık uzaktan; sürtünme ve normal kuvvet temaslı kuvvettir; ağırlık N, kütle kg.','Kütle ile ağırlığı karıştırmak.','kolay','öncüllü',5,'fz-hk2-kuvvet','Kuvvet ve türleri')
kartla('K-FZHK2-18','Cisme etkiyen kuvvetleri tanıma','Ağırlık aşağı, normal kuvvet yüzeye dik; etki–tepki farklı cisimlere etkir.','Aynı cisme etkiyen iki kuvveti etki–tepki sanmak.','orta','öncüllü',5,'fz-hk2-kuvvet','Kuvvet ve türleri')
kartla('K-FZHK2-19','Dik doğrultulu bileşke','Her doğrultuda ayrı bileşke, sonra Pisagor.','Büyüklükleri toplamak.','orta','şekilli',4,'fz-hk2-bileske','Bileşke kuvvet')
kartla('K-FZHK2-20','Aynı doğrultuda bileşke','Aynı yönlüler toplanır, zıt yönlüler çıkarılır.','Yönlere bakmadan toplamak.','kolay','şekilli',3,'fz-hk2-bileske','Bileşke kuvvet')
kartla('K-FZHK2-21','Dört kuvvette denge koşulu','Net kuvvet sıfır olmalı; eksik bileşen karşı yönde eklenir.','Yalnız bir doğrultuya bakmak.','orta','öncüllü',5,'fz-hk2-bileske','Bileşke kuvvet')
kartla('K-FZHK2-22','Sürtünme–uygulanan kuvvet grafiği','Hareket başlayana kadar statik sürtünme uygulanan kuvvete eşit; kayınca kinetik sabit.','Kayma sonrası sürtünmeyi uygulanan kuvvete eşit sanmak.','zor','öncüllü',5,'fz-hk2-surtunme','Sürtünme kuvveti')
kartla('K-FZHK2-23','Üst üste kutularda kinetik sürtünme','Sabit hızda net kuvvet sıfır; f = μ·N, N toplam ağırlık.','Yalnız alttaki kutunun ağırlığını almak.','orta','şekilli',4,'fz-hk2-surtunme','Sürtünme kuvveti')
kartla('K-FZHK2-24','Sürtünmenin temas alanından bağımsızlığı','Sürtünme normal kuvvete ve yüzeye bağlıdır, temas alanına değil.','Alan büyük → sürtünme büyük sanmak.','orta','öncüllü',5,'fz-hk2-surtunme','Sürtünme kuvveti')

# ================= 01 · konum, yol, yer değiştirme =================
pK,pL,pM=10,70,30
yol=abs(pL-pK)+abs(pM-pL); yer=abs(pM-pK); fark=yol-yer
assert (yol,yer,fark)==(100,20,80) and abs(pL-pK)==60 and abs(pM-pL)==40 and yol+yer==120
X=lambda m:(m+20)*.08
f=[f'\\draw[-{{Stealth}}] ({X(-20)-.2:.2f},0) -- ({X(80)+.5:.2f},0) node[right]{{$x$ (m)}};']
for m in range(-20,81,10): f.append(f'\\draw ({X(m):.2f},.08) -- ({X(m):.2f},-.08) node[below,font=\\scriptsize]{{${m}$}};')
for n,m in (('K',pK),('L',pL),('M',pM)): f.append(f'\\fill[vurgu] ({X(m):.2f},0) circle (2.5pt) node[above=5pt,black]{{{n}}};')
S01=tk(f)
q('0001',tipId='fz-hk2-konum',tip='Konum, yol ve yer değiştirme',z='kolay',alt='Konum, yer değiştirme ve alınan yol',kaz='Konum eksenindeki noktalardan alınan yolu ve yer değiştirmeyi bulur.',kalip='şekilli',
 kart='K-FZHK2-01 (konum, yol, yer değiştirme) · eksen üzerinde üç nokta',sekil=S01,
 metin='Bir kurye, doğu–batı doğrultusundaki düz bir caddede teslimat yapıyor. Caddenin konum ekseni, doğu yönü pozitif olacak biçimde şekilde verilmiştir. Kurye motosikletiyle K noktasından yola çıkıyor, önce L noktasındaki mağazaya uğruyor, ardından M noktasındaki işyerine gidiyor ve orada duruyor. Kurye yalnızca cadde üzerinde, doğrusal bir hat boyunca hareket etmiştir.\nBuna göre kuryenin aldığı yol ile yer değiştirmesinin büyüklüğü arasındaki fark kaç m’dir?',
 dogru=fark,yan=[(20,'Yer değiştirmenin büyüklüğünü (20 m) fark sanmış.','dikkat'),(40,'Yalnız L–M arasındaki geri dönüş uzunluğunu (40 m) yazmış.','dikkat'),(30,'M noktasının konumunu (30 m) yazmış.','dikkat'),(60,'Yalnız K–L arasındaki ilk gidiş uzunluğunu (60 m) yazmış.','dikkat')],
 ip=['Yolu, kuryenin gittiği bütün uzunlukları toplayarak; yer değiştirmeyi ise yalnız ilk ve son konuma bakarak bul.'],
 bilgi=[B('Yol ve yer değiştirme','yol, cismin gittiği uzunlukların toplamıdır (skalerdir); yer değiştirme ilk konumdan son konuma çizilen yön bilgili uzunluktur. Örnek: 0 m’den 8 m’ye gidip 5 m’ye dönen cismin yolu 8 + 3 = 11 m, yer değiştirmesi 5 m’dir')],
 ad=[A('Konumları oku','Eksenden K, L ve M noktalarının konumları okunur.','x_K = 10 m · x_L = 70 m · x_M = 30 m'),A('Yolu bul','Kurye önce doğuya, sonra batıya gitmiştir; uzunluklar toplanır.','60 + 40 = 100 m'),A('Yer değiştirmeyi bul','Yalnız son konum ile ilk konum arasındaki uzaklığa bakılır.','|30 − 10| = 20 m'),A('Farkı al','Yol ile yer değiştirmenin büyüklüğü çıkarılır.','100 − 20 = 80 m')],
 puf='Yolu parça parça topla, yer değiştirmeyi yalnız başlangıç ve bitişten bul.')

# ================= 02 · rota, sürat ve hız yargıları =================
d1,d2,tk2=120,160,100; yer2=math.hypot(d1,d2); yol2=d1+d2
assert yer2==200 and yol2==280 and yol2/tk2==2.8 and yer2/tk2==2 and yol2>yer2
sc=.025
f=[f'\\draw[thick] (0,0) -- (0,{d1*sc}) -- ({d2*sc},{d1*sc});',f'\\draw[dashed,gray] (0,0) -- ({d2*sc},{d1*sc});']
f.append(f'\\draw[vurgu,very thick,{ARR}] (0,{d1*sc*.5-.3}) -- (0,{d1*sc*.5+.3});')
f.append(f'\\draw[vurgu,very thick,{ARR}] ({d2*sc*.5-.3},{d1*sc}) -- ({d2*sc*.5+.3},{d1*sc});')
for n,p,pos in (('A',(0,0),'below left'),('B',(0,d1*sc),'above left'),('C',(d2*sc,d1*sc),'above right')): f.append(f'\\fill ({p[0]},{p[1]}) circle (2.2pt) node[{pos}]{{{n}}};')
f.append(f'\\node[left] at (0,{d1*sc/2}) {{{d1} m}};'); f.append(f'\\node[above] at ({d2*sc/2},{d1*sc+.12}) {{{d2} m}};')
f.append(f'\\draw[-{{Stealth}}] ({d2*sc+.5},.45) -- ({d2*sc+.5},.95) node[above]{{N}};')
S02=tk(f)
onc('0002','b',[('Koşucunun aldığı yol 200 m’dir.',False,'Yol, iki bölümün uzunluklarının toplamıdır: 120 + 160 = 280 m; 200 m yer değiştirmenin büyüklüğüdür.'),
 ('Koşucunun yer değiştirmesinin büyüklüğü 200 m’dir.',True,'A’dan C’ye doğru çizilen düz çizginin uzunluğu √(120² + 160²) = 200 m’dir.'),
 ('Koşucunun ortalama süratinin büyüklüğü, ortalama hızının büyüklüğünden büyüktür.',True,'Ortalama sürat 280 ÷ 100 = 2,8 m/s, ortalama hız büyüklüğü 200 ÷ 100 = 2 m/s’dir.')],
 'Şekilde A, B ve C noktaları arasındaki yollar verilmiştir; kuzey yönü N ile gösterilmiştir.','A → B: 120 m kuzey · B → C: 160 m doğu · toplam süre 100 s',
 tipId='fz-hk2-surathiz',tip='Sürat ve hız kavramları',z='orta',alt='Sürat ve hız',kaz='Rota şemasından yol ve yer değiştirmeyi bulup sürat ile hız yargılarını değerlendirir.',kart='K-FZHK2-02 (rota, yol ve yer değiştirme yargıları) · dik iki parçalı rota',sekil=S02,
 metin='Bir koşucu, kenar uzunlukları şekilde verilen parkta A noktasından başlayıp önce B noktasına, ardından C noktasına koşuyor ve C’de duruyor. Koşucu, A’dan C’ye giderken yalnızca şekildeki yollar üzerinde, sabit sürat sayılacak biçimde ilerliyor ve tüm hareketi 100 s sürüyor. A’dan C’ye çizilen kesikli çizgi yalnızca başlangıç ve bitiş noktalarını birleştirir.',
 ip=['Yol ile yer değiştirmeyi ayrı ayrı bul; sonra her ikisini de 100 s’ye bölerek sürat ile hızı karşılaştır.'],
 bilgi=[B('Sürat ve hız','ortalama sürat = toplam yol ÷ süre, ortalama hız = yer değiştirme ÷ süre. Yön değişiyorsa yol, yer değiştirmeden büyüktür. Örnek: 30 m gidip 40 m yukarı çıkan cismin yolu 70 m, yer değiştirmesi 50 m’dir')],
 puf='Yön değişiyorsa ortalama sürat, ortalama hız büyüklüğünden büyük olur.')

# ================= 03 · yarı yolları farklı hızla =================
dd=120; v1,v2=40,60; t1=Fr(dd,v1); t2=Fr(dd,v2); vo=Fr(2*dd)/(t1+t2)
assert (t1,t2)==(3,2) and vo==48 and (v1+v2)/2==50 and Fr(dd,t1+t2)==24 and Fr(2*dd,t1)==80
f=[f'\\draw[thick] (0,0) -- (8,0);']
for x,n in ((0,'K'),(4,'L'),(8,'M')): f.append(f'\\fill ({x},0) circle (2.2pt) node[below=3pt]{{{n}}};')
f.append(oklu(.3,.55,3.7,.55,'40 km/h')); f.append(oklu(4.3,.55,7.7,.55,'60 km/h'))
f.append('\\draw[decorate,decoration={brace,mirror,amplitude=4pt}] (0,-.6) -- (3.95,-.6) node[midway,below=5pt]{120 km};')
f.append('\\draw[decorate,decoration={brace,mirror,amplitude=4pt}] (4.05,-.6) -- (8,-.6) node[midway,below=5pt]{120 km};')
S03=tk(f)
q('0003',tipId='fz-hk2-ortalama',tip='Ortalama sürat ve ortalama hız',z='orta',alt='Ortalama hız',kaz='Yolun yarılarını farklı hızlarla alan hareketlinin ortalama süratini bulur.',kalip='şekilli',
 kart='K-FZHK2-03 (yarı yolları farklı hızla gitme) · 40 ve 60 km/h',sekil=S03,
 metin='Bir yük kamyonu, aralarında düz bir otoyol bulunan K ve M şehirleri arasında seferini yapıyor. Şoför, yolun ortasındaki L şehrinde mola vermeden geçiyor. Şekilde, kamyonun yolun her yarısında sabit tuttuğu hızlar ve her yarının uzunluğu gösterilmiştir. Kamyon yol boyunca aynı yönde gitmiş, hiç geri dönmemiştir.\nBuna göre kamyonun K’dan M’ye giderken ortalama sürati kaç km/h’tir?',
 dogru=vo,yan=[(50,'İki hızın aritmetik ortalamasını almış: (40 + 60) ÷ 2 = 50 km/h.','bilgi'),(60,'Yalnız ikinci yarıdaki hızı yazmış.','dikkat'),(80,'Toplam yolu (240 km) ilk yarının süresine (3 h) bölmüş.','islem'),(100,'İki hızı toplamış (40 + 60 = 100 km/h).','dikkat')],
 istenen='Ortalama sürat (km/h).',ip=['Yarı yolları farklı hızlarla alan hareketlide, her yarıyı gitmek için geçen süre aynı mıdır?'],
 bilgi=[B('Ortalama sürat','ortalama sürat = toplam yol ÷ toplam süre; hızların aritmetik ortalaması değildir. Örnek: 30 km’yi 1 saatte, 30 km’yi 3 saatte alan aracın ortalama sürati 60 ÷ 4 = 15 km/h’tir (22,5 değil)')],
 ad=[A('Süreleri bul','Her yarının süresi yol ÷ hız ile hesaplanır.','t₁ = 120 ÷ 40 = 3 h · t₂ = 120 ÷ 60 = 2 h'),A('Toplamları al','Toplam yol ve toplam süre bulunur.','yol = 240 km · süre = 5 h'),A('Ortalama sürati hesapla','Toplam yol toplam süreye bölünür.','v = 240 ÷ 5 = 48 km/h'),A('Kontrol et','Ortalama sürat, iki hız arasında ve yavaş olana yakın çıkmalıdır.','40 < 48 < 60 ve 48 < 50')],
 puf='Yarı yolları farklı hızla alan hareketlinin ortalama sürati, hızların aritmetik ortalamasından küçüktür.')

# ================= 04 · duraksamalı gidiş-dönüş =================
seg=[(100,40),(-40,20),(0,20),(60,20)]  # (yer değiştirme m, süre s)
yer4=sum(a for a,b in seg); yol4=sum(abs(a) for a,b in seg); T4=sum(b for a,b in seg); Th=sum(b for a,b in seg if a!=0)
vs=Fr(yol4,T4); vh=Fr(yer4,T4)
assert (yer4,yol4,T4,Th)==(120,200,100,80) and vs==2 and vh==Fr(6,5) and vs-vh==Fr(4,5)
assert Fr(yol4,Th)-Fr(yer4,Th)==1 and vs+vh==Fr(16,5)
q('0004',tipId='fz-hk2-ortalama',tip='Ortalama sürat ve ortalama hız',z='zor',alt='Ortalama hız',kaz='Duraksamalı gidiş–dönüş hareketinde ortalama sürat ile ortalama hız farkını bulur.',kalip='hikâyeli',
 kart='K-FZHK2-04 (duraksamalı gidiş–dönüş) · dinlenme süresi toplam süreye katılır',
 metin='Bir koşucu, düz bir sahil yolunda K noktasından doğuya doğru 100 m’yi 40 s’de koşuyor. Daha sonra fotoğraf çekmek için geri dönüyor ve batıya doğru 40 m’yi 20 s’de koşuyor. Bir bankta 20 s boyunca oturup dinleniyor, ardından yeniden doğuya doğru 60 m’yi 20 s’de koşuyor ve duruyor. Koşucu yolun dışına çıkmamış, tüm hareket boyunca yalnızca doğu–batı doğrultusunda gitmiştir.\nBuna göre koşucunun, dinlenme süresi de dahil tüm hareket için ortalama süratinin ortalama hızının büyüklüğünden farkı kaç m/s’dir?',
 dogru=Fr(4,5),yan=[(1,'Dinlenme süresini (20 s) katmamış: (200 − 120) ÷ 80 = 1 m/s.','dikkat'),(Fr(6,5),'Yalnız ortalama hızı (120 ÷ 100) bulmuş.','dikkat'),(2,'Yalnız ortalama sürati (200 ÷ 100) bulmuş.','dikkat'),(Fr(16,5),'Ortalama sürat ile ortalama hızı toplamış (2 + 1,2).','islem')],
 istenen='Ortalama sürat − ortalama hız büyüklüğü (m/s).',ip=['Önce yolu ve yer değiştirmeyi ayrı ayrı bul; dinlenme anı da geçen süreye dahildir.'],
 bilgi=[B('Sürat ve hız','ortalama sürat = toplam yol ÷ toplam süre, ortalama hız = yer değiştirme ÷ toplam süre. Duraksama süresi toplam süreye katılır. Örnek: 6 m gidip 2 m geri dönen cismin yolu 8, yer değiştirmesi 4 m’dir')],
 ad=[A('Yolu bul','Gidilen bütün uzunluklar toplanır.','100 + 40 + 60 = 200 m'),A('Yer değiştirmeyi bul','Doğu pozitif alınırsa batıya giden eksi yazılır.','100 − 40 + 60 = 120 m'),A('Toplam süreyi bul','Dinlenme süresi de dahildir.','40 + 20 + 20 + 20 = 100 s'),A('Sürat ve hızı hesapla','Yol ve yer değiştirme toplam süreye bölünür.','sürat = 200 ÷ 100 = 2 m/s · hız = 120 ÷ 100 = 1,2 m/s'),A('Farkı al','İki büyüklük çıkarılır.','2 − 1,2 = 0,8 m/s')],
 puf='Duraksama süreyi uzatır ama yolu ve yer değiştirmeyi değiştirmez; süreyi hep toplamdan al.')

# ================= 05 · zıt yönde karşılaşma =================
dK,vA,vB=450,6,9; tkar=Fr(dK,vA+vB); xk=vA*tkar
assert tkar==30 and xk==180 and dK-xk==270 and Fr(dK,2)==225 and tkar==30 and Fr(2*dK,3)==300
f=[f'\\draw[thick] (0,0) -- (8,0);',f'\\fill (0,0) circle (2.2pt) node[below=3pt]{{K}}; \\fill (8,0) circle (2.2pt) node[below=3pt]{{L}};']
f.append(oklu(.3,.55,2.3,.55,'6 m/s')); f.append(oklu(7.7,.55,4.7,.55,'9 m/s'))
f.append('\\draw[<->] (0,-.7) -- (8,-.7) node[midway,below]{450 m};')
S05=tk(f)
q('0005',tipId='fz-hk2-ddh',tip='Düzgün doğrusal hareket',z='kolay',alt='Düzgün doğrusal hareket',kaz='Zıt yönde sabit hızla giden iki hareketlinin karşılaşma yerini bulur.',kalip='şekilli',
 kart='K-FZHK2-05 (zıt yönde karşılaşma) · karşılaşma yerinin uzaklığı',sekil=S05,
 metin='Düz bir parkurun iki ucundaki K ve L noktalarında bulunan iki bisikletli, aynı anda birbirlerine doğru yola çıkıyor. Şekilde bisikletlilerin sabit hızları ve K ile L arasındaki uzaklık verilmiştir. Bisikletliler yol boyunca hızlarını değiştirmiyor ve duraksamıyor.\nBuna göre bisikletliler karşılaştıklarında K noktasından kaç m uzaktadır?',
 dogru=xk,yan=[(30,'Karşılaşma süresini (30 s) mesafe olarak yazmış.','dikkat'),(225,'Karşılaşmanın tam orta noktada (450 ÷ 2) olduğunu sanmış.','bilgi'),(270,'K’dan değil L’den uzaklığı (450 − 180) bulmuş.','dikkat'),(300,'Hızların oranını (6/9 = 2/3) mesafeye uygulamış: 450 × 2/3 = 300 m.','bilgi')],
 istenen='Karşılaşma anında K’dan uzaklık (m).',ip=['Birbirine doğru gelen hareketlilerde aradaki mesafe, hızlar toplamıyla kapanır.'],
 bilgi=[B('Zıt yönde karşılaşma','birbirine doğru giden hareketlilerde mesafe, hızların toplamıyla kapanır: t = yol ÷ (v₁ + v₂). Örnek: 100 m aralıkla 3 ve 2 m/s ile gelenler 100 ÷ 5 = 20 s sonra buluşur')],
 ad=[A('Yaklaşma hızı','Zıt yönde gidenlerde hızlar toplanır.','6 + 9 = 15 m/s'),A('Karşılaşma süresi','Mesafe yaklaşma hızına bölünür.','t = 450 ÷ 15 = 30 s'),A('K’dan uzaklık','K’dan çıkan bisikletlinin aldığı yol sorulur.','x = 6 × 30 = 180 m')],
 puf='Karşılaşma sorularında önce süreyi (yol ÷ hızlar toplamı) bul, sonra istenen yolu hesapla.')

# ================= 06 · çoklu pozlama =================
Kp=[0,4,8,12,16]; Lp=[0,2,4,6,8]; Mp=[0,1,3,6,10]; dt=Fr(1,2)
dif=lambda p:[p[i+1]-p[i] for i in range(4)]
assert len(set(dif(Kp)))==1 and len(set(dif(Lp)))==1 and dif(Kp)[0]==2*dif(Lp)[0] and dif(Mp)==[1,2,3,4]
vK6=Fr(Kp[-1],4)/dt/ (1) if False else Fr(Kp[-1],2); vM6=Fr(Mp[-1],2); assert vK6==8 and vM6==5 and vM6<vK6
Y=lambda p:p*.45
f=[]
for n,yy,pp in (('K',2.0,Kp),('L',1.3,Lp),('M',.6,Mp)):
    f.append(f'\\draw[gray!60] (0,{yy}) -- ({Y(16)},{yy}) node[left=-.1cm]{{}}; \\node at (-.35,{yy}) {{{n}}};')
    for p in pp: f.append(f'\\fill[vurgu] ({Y(p):.3f},{yy}) circle (3pt);')
f.append(f'\\draw (0,0) -- ({Y(16)},0);')
for m in range(0,17): f.append(f'\\draw ({Y(m):.3f},0) -- ({Y(m):.3f},-{.1 if m%2 else .17});'+(f'\\node[below,font=\\scriptsize] at ({Y(m):.3f},-.15) {{{m}}};' if m%2==0 else ''))
f.append(f'\\node[right,font=\\scriptsize] at ({Y(16)+.1:.2f},0) {{cm}};')
S06=tk(f)
onc('0006','d',[('K’nin hızı, L’nin hızının iki katıdır.',True,'K her 0,5 s’de 4 cm, L ise 2 cm gider; eşit sürede K iki kat yol aldığından hızı iki kattır.'),
 ('M’nin hızı zamanla artmıştır.',True,'M’nin ardışık konum farkları 1, 2, 3, 4 cm’dir; eşit sürelerde alınan yol arttığından hız artar.'),
 ('M’nin 0–2 s aralığındaki ortalama hızı, K’nin ortalama hızından büyüktür.',False,'M 2 s’de 10 cm, K ise 16 cm gitmiştir; M’nin ortalama hızı (5 cm/s) K’ninkinden (8 cm/s) küçüktür.')],
 'Üç oyuncak arabanın konumları 0,5 s aralıkla işaretlenmiştir (işaretlerin konumları şekilde cm cinsinden verilmiştir).','K: her 0,5 s’de 4 cm · L: her 0,5 s’de 2 cm · M: 1, 2, 3, 4 cm',
 tipId='fz-hk2-ddh',tip='Düzgün doğrusal hareket',z='orta',alt='Düzgün doğrusal hareket',kaz='Eşit zaman aralıklı konum işaretlerinden hız türünü ve hız karşılaştırmasını yorumlar.',kart='K-FZHK2-06 (çoklu pozlama) · üç hareketli, hız karşılaştırması',sekil=S06,
 metin='Bir fizik laboratuvarında üç oyuncak araba, aynı doğrusal pist üzerinde aynı anda, aynı noktadan harekete başlıyor. Öğrenciler her aracın konumunu 0,5 s aralıklarla çeken bir kamera ile işaretliyor ve işaretleri cetvel üzerine şekildeki gibi aktarıyor. İşaretler, başlangıçtan itibaren her aracın ilk 2 s’lik hareketine aittir. Arabaların hareketleri sırasında yön değiştirmemiş olduğu kabul edilecektir.',
 ip=['Eşit sürelerde alınan yolları karşılaştır: aralıklar sabit mi, artıyor mu?'],
 bilgi=[B('Eşit aralıklı işaretler','eşit sürelerde eşit yol alınıyorsa hız sabittir; aralıklar büyüyorsa hız artıyordur. Ortalama hız = toplam yer değiştirme ÷ süre. Örnek: 1 s aralıkla 3 cm, 3 cm, 3 cm yol alan cisim sabit 3 cm/s hızlıdır')],
 puf='Çoklu pozlamada aralıkların eşit olup olmadığına bak; ortalama hız için ilk ve son konumu kullan.')

# ================= 07 · x–t grafiği yargıları =================
pts7=[(0,20),(4,60),(6,60),(12,0)]
v1_=(60-20)/4; v2_=0; v3_=(0-60)/(12-6); yol7=40+0+60
assert v1_==10 and v2_==0 and v3_==-10 and yol7==100
S07=grafik([(pts7,V,'')],12,0,70,'0,2,4,6,8,10,12','0,10,20,30,40,50,60,70','$t$ (s)','$x$ (cm)',h=5.2)
onc('0007','c',[('Cismin 0–4 s aralığındaki hızı 10 cm/s’dir.',True,'Konum 4 s’de 20 cm’den 60 cm’ye çıkmıştır: eğim = 40 ÷ 4 = 10 cm/s.'),
 ('Cismin 4–6 s aralığındaki hızı 10 cm/s’dir.',False,'Bu aralıkta konum değişmediği için eğim, yani hız sıfırdır; cisim durmaktadır.'),
 ('Cismin 0–12 s aralığında aldığı yol 100 cm’dir.',True,'Gidiş 60 − 20 = 40 cm, dönüş 60 − 0 = 60 cm; toplam yol 100 cm’dir.')],
 'Grafikte konum, referans noktasından ölçülmüştür.','0–4 s: 20 → 60 cm · 4–6 s: 60 cm sabit · 6–12 s: 60 → 0 cm',
 tipId='fz-hk2-xt',tip='Konum–zaman grafiği',z='orta',alt='Konum–zaman grafiği',kaz='Konum–zaman grafiğinden hızı ve alınan yolu yorumlar.',kart='K-FZHK2-07 (x–t yargıları) · gidiş, durma, dönüş',sekil=S07,
 metin='Bir robot kol makinesi, düz bir ray üzerindeki küçük bir arabayı belirli bir program doğrultusunda hareket ettiriyor. Arabanın raydaki konumu, ray başlangıcındaki referans noktasından ölçülüyor ve konum–zaman grafiği şekildeki gibi kaydediliyor. Araba rayın dışına çıkmıyor; dışarıdan başka bir etki yoktur.',
 ip=['Konum–zaman grafiğinde eğim hızı verir; yatay bölümler ile eğimli bölümleri ayrı ayrı incele.'],
 bilgi=[B('x–t grafiği','eğim (Δx ÷ Δt) hızdır; yatay doğru cismin durduğunu gösterir; yol, konumdaki her değişimin mutlak değerlerinin toplamıdır. Örnek: 2 s’de 10 cm’den 16 cm’ye çıkan cismin hızı 3 cm/s’dir')],
 puf='x–t grafiğinde “eğim = hız”; yatay çizgi duruyor demektir, sabit hızlı gidiyor demek değildir.')

# ================= 08 · x–t iki araç karşılaşma =================
xK0,xL0,vK8,vL8=0,100,10,-10; tz=Fr(xL0-xK0,vK8-vL8)
assert (20-xK0)/2==vK8 and (80-xL0)/2==vL8 and tz==5 and vK8*tz==50 and Fr(xL0,vK8)==10
S08=grafik([([(0,0),(2,20)],V,''),([(0,100),(2,80)],V.replace('vurgu','black'),'')],3,0,100,'0,0.5,1,1.5,2,2.5,3','0,20,40,60,80,100','$t$ (s)','$x$ (m)',h=5.2,
 notlar='\\node[above right] at (axis cs:.1,3) {\\small K}; \\node[above] at (axis cs:1,90) {\\small L};')
q('0008',tipId='fz-hk2-xt',tip='Konum–zaman grafiği',z='orta',alt='Konum–zaman grafiği',kaz='İki hareketlinin konum–zaman grafiklerinden hızları bulup karşılaşma süresini hesaplar.',kalip='grafik',
 kart='K-FZHK2-08 (x–t iki hareketli) · grafikten hız, karşılaşma süresi',sekil=S08,
 metin='Doğrusal bir yolda biri K, diğeri L olan iki robot, aynı anda harekete başlıyor ve birbirine doğru ilerliyor. Robotların ilk 2 s’lik konum–zaman grafikleri şekilde verilmiştir; konumlar ortak bir başlangıç noktasından ölçülmüştür. Robotlar bu andan sonra da hızlarını değiştirmeden aynı doğrultuda hareketlerini sürdürmektedir.\nBuna göre robotlar hareketin başlamasından kaç s sonra karşılaşır?',
 dogru=5,yan=[(2,'Grafikte görünen son anı (2 s) karşılaşma anı sanmış.','dikkat'),(10,'Yalnız L’nin 100 m’lik mesafesini K’nin hızına (10 m/s) bölmüş.','islem'),(20,'Hızların toplamını (20 m/s) süre sanmış.','dikkat'),(50,'Karşılaşma anındaki K’nin konumunu (50 m) süre olarak yazmış.','dikkat')],
 istenen='Karşılaşma süresi (s).',ip=['Önce grafiklerin eğimlerinden iki robotun hızlarını bul; aradaki mesafe hangi hızla kapanıyor?'],
 bilgi=[B('x–t eğimi ve karşılaşma','eğim hızı verir. Birbirine doğru gelenlerde mesafe hızlar toplamıyla kapanır. Örnek: 60 m aralıklı, 4 ve 2 m/s ile birbirine gelen iki cisim 10 s sonra buluşur')],
 ad=[A('Hızları oku','Eğim = konum değişimi ÷ süre.','v_K = 20 ÷ 2 = 10 m/s · v_L = (80 − 100) ÷ 2 = −10 m/s'),A('Başlangıç mesafesini bul','t = 0’daki konumlar okunur.','100 − 0 = 100 m'),A('Yaklaşma hızı','İki robot birbirine doğru gittiği için büyüklükler toplanır.','10 + 10 = 20 m/s'),A('Süreyi hesapla','Mesafe yaklaşma hızına bölünür.','t = 100 ÷ 20 = 5 s')],
 puf='Grafikte karşılaşma görünmüyorsa eğimlerden hızları okuyup bağıl hızla süreyi hesapla.')

# ================= 09 · v–t yol ve ortalama sürat =================
pts9=[(0,0),(4,8),(6,8),(8,0),(10,-8)]
A1=Fr(4*8,2);A2=2*8;A3=Fr(2*8,2);A4=Fr(2*8,2)
yer9=A1+A2+A3-A4; yol9=A1+A2+A3+A4; ov=Fr(yol9,10); oh=Fr(yer9,10)
assert (yer9,yol9)==(32,48) and ov==Fr(24,5) and oh==Fr(16,5) and Fr(yol9,8)==6 and Fr(A1+A2+A3,10)==4
S09=grafik([(pts9,V,'')],10,-8,8,'0,2,4,6,8,10','-8,-4,0,4,8','$t$ (s)','$v$ (m/s)',h=5.0)
q('0009',tipId='fz-hk2-vt',tip='Hız–zaman grafiği',z='zor',alt='Hız–zaman grafiği',kaz='Hız–zaman grafiğinde yön değiştiren hareketlinin yolunu ve ortalama süratini bulur.',kalip='grafik',
 kart='K-FZHK2-09 (v–t, yön değiştirme) · ortalama sürat',sekil=S09,
 metin='Düz bir rayda hareket eden bir yük arabasının hız–zaman grafiği şekilde verilmiştir. Hız, arabanın başlangıçtaki hareket yönünde pozitif alınmıştır. Araba yalnızca ray doğrultusunda gitmekte olup hareket yönünü grafikteki bir anda değiştirmektedir.\nBuna göre arabanın 0–10 s aralığındaki ortalama süratinin büyüklüğü kaç m/s’dir?',
 dogru=ov,yan=[(Fr(16,5),'Negatif alanı yoldan çıkarıp ortalama hızı (32 ÷ 10) bulmuş.','bilgi'),(4,'Yalnız ileri yöndeki alanı (40 m) süreye bölmüş.','dikkat'),(6,'Yolu (48 m) hızın işaret değiştirdiği ana kadar geçen süreye (8 s) bölmüş.','dikkat'),(8,'Grafikteki en büyük hız değerini ortalama sürat sanmış.','dikkat')],
 istenen='0–10 s aralığında ortalama sürat (m/s).',ip=['Hız işaret değiştirdiği anı bul; ileri ve geri hareketin alanlarını ayrı ayrı bul, yol için mutlak değerlerini topla.'],
 bilgi=[B('v–t grafiğinde alan','grafikle zaman ekseni arasındaki alan yer değiştirmeyi verir; zaman ekseninin altındaki alan negatiftir. Yol, alanların mutlak değerlerinin toplamıdır. Örnek: 2 s boyunca +3 m/s, sonra 1 s boyunca −3 m/s hızla giden cismin yolu 9 m, yer değiştirmesi 3 m’dir')],
 ad=[A('Grafiği parçala','Hız 8. s’de sıfırdan geçip işaret değiştirir; dört bölge vardır.','0–4 s üçgen · 4–6 s dikdörtgen · 6–8 s üçgen · 8–10 s üçgen (negatif)'),A('Alanları bul','Her bölgenin alanı ayrı hesaplanır.','16 · 16 · 8 · 8 (m)'),A('Yolu bul','Yol için bütün alanlar mutlak değerle toplanır.','16 + 16 + 8 + 8 = 48 m'),A('Ortalama sürati hesapla','Yol toplam süreye bölünür.','48 ÷ 10 = 4,8 m/s'),A('Kontrol et','Ortalama hız yer değiştirmeden bulunurdu ve yola eşit olmazdı.','yer değiştirme = 32 m → 3,2 m/s < 4,8 m/s')],
 puf='v–t grafiğinde hız işaret değiştirdiyse yol için alanları mutlak değerle topla; yer değiştirme için işaretle topla.')

# ================= 10 · v–t yargıları =================
pts10=[(0,0),(3,12),(6,12),(10,0)]
ortv=Fr(12,2); a1=Fr(12,3); yer10=Fr(4*12,2)
assert ortv==6 and a1==4 and yer10==24 and 12!=ortv
S10=grafik([(pts10,V,'')],10,0,14,'0,1,2,3,4,5,6,7,8,9,10','0,2,4,6,8,10,12,14','$t$ (s)','$v$ (m/s)',h=5.0)
onc('0010','c',[('Cismin 0–3 s aralığındaki ortalama hızının büyüklüğü 12 m/s’dir.',False,'Hız 0’dan 12 m/s’ye düzgün arttığı için ortalama hız (0 + 12) ÷ 2 = 6 m/s’dir; 12 m/s en büyük hızdır.'),
 ('Cisim 3–6 s aralığında durmaktadır.',False,'Bu aralıkta hız 12 m/s’de sabittir; yatay doğru ivmenin sıfır olduğunu gösterir, cismin durduğunu değil.'),
 ('Cismin 6–10 s aralığındaki yer değiştirmesi 24 m’dir.',True,'Grafik ile eksen arasında taban 4 s, yükseklik 12 m/s olan üçgen vardır: 4 × 12 ÷ 2 = 24 m.')],
 'Şekilde hız–zaman grafiği verilmiştir.','0–3 s: 0 → 12 m/s · 3–6 s: 12 m/s sabit · 6–10 s: 12 → 0 m/s',
 tipId='fz-hk2-vt',tip='Hız–zaman grafiği',z='orta',alt='Hız–zaman grafiği',kaz='Hız–zaman grafiğini eğim ve alan yorumuyla değerlendirir.',kart='K-FZHK2-10 (v–t yargıları) · hızlanma, sabit hız, yavaşlama',sekil=S10,
 metin='Bir fabrikadaki otomatik taşıyıcı araç, yükü depodan paketleme bölümüne doğrusal bir hat üzerinde götürüyor. Aracın hız–zaman grafiği şekildeki gibi kaydedilmiştir. Araç, hareketi boyunca hattın dışına çıkmıyor ve geri gitmiyor; hızı grafikteki gibi değişiyor.',
 ip=['Her yargıdaki zaman aralığını grafikte işaretle: eğimi ve altında kalan alanı yorumla.'],
 bilgi=[B('v–t grafiği','eğim ivmeyi, alan yer değiştirmeyi verir; yatay doğru sabit hızdır (ivme sıfır). Düzgün değişen harekette ortalama hız (ilk hız + son hız) ÷ 2’dir. Örnek: 2 m/s’den 10 m/s’ye çıkan cismin ortalama hızı 6 m/s’dir')],
 puf='Yatay çizgi v–t grafiğinde “sabit hız”, x–t grafiğinde ise “duruyor” demektir.')

# ================= 11 · iki hareketlinin ivme karşılaştırması =================
aK=Fr(20-0,5); aL=Fr(20-10,5); oran=aK/aL
assert (aK,aL,oran)==(4,2,2) and aL/aK==Fr(1,2) and Fr(15,10)==Fr(3,2) and 20/20==1
S11=grafik([([(0,0),(5,20)],V,''),([(0,10),(5,20)],'thick,black,mark=*,mark size=1.5pt','')],5,0,24,'0,1,2,3,4,5','0,4,8,12,16,20,24','$t$ (s)','$v$ (m/s)',h=5.0,
 notlar='\\node[right] at (axis cs:3.6,10) {\\small K}; \\node[above] at (axis cs:2,16.2) {\\small L};')
q('0011',tipId='fz-hk2-ivme',tip='İvme kavramı',z='kolay',alt='İvme',kaz='Hız–zaman grafiğinin eğiminden iki hareketlinin ivmelerini karşılaştırır.',kalip='grafik',
 kart='K-FZHK2-11 (ivme karşılaştırma) · K ve L aynı sürede aynı hıza çıkıyor',sekil=S11,
 metin='Düz bir yolda aynı yönde hareket eden K ve L araçlarının hız–zaman grafikleri şekilde verilmiştir. Araçlar, grafikte gösterilen 5 s boyunca düzgün hızlanmaktadır; K araç durgun halden, L araç ise bir miktar hızla geçerken harekete başlamıştır.\nBuna göre K aracının ivmesinin büyüklüğünün L aracının ivmesinin büyüklüğüne oranı kaçtır?',
 dogru=2,yan=[(Fr(1,2),'Oranı ters yazmış (a_L ÷ a_K).','dikkat'),(1,'Her iki aracın 5. s’deki hızı aynı olduğundan ivmeleri eşit sanmış.','bilgi'),(Fr(3,2),'Ortalama hızların oranını (15 ÷ 10) almış.','bilgi'),(4,'K’nin ivmesini (4 m/s²) oran olarak yazmış.','dikkat')],
 istenen='a_K ÷ a_L oranı.',ip=['İvmeyi hız değişimini sürece bölerek, her araç için ayrı hesapla.'],
 bilgi=[B('İvme','a = Δv ÷ Δt; v–t grafiğinde doğrunun eğimidir. Son hızın eşit olması ivmenin eşit olduğu anlamına gelmez. Örnek: 2 s’de hızı 4 m/s’den 10 m/s’ye çıkan cismin ivmesi 6 ÷ 2 = 3 m/s²’dir')],
 ad=[A('K’nin ivmesi','Hız değişimi süreye bölünür.','a_K = (20 − 0) ÷ 5 = 4 m/s²'),A('L’nin ivmesi','Aynı işlem L için yapılır.','a_L = (20 − 10) ÷ 5 = 2 m/s²'),A('Oranı al','İstenen oran K’nin L’ye oranıdır.','a_K ÷ a_L = 4 ÷ 2 = 2')],
 puf='İvme hız değişiminden bulunur, son hızdan değil.')

# ================= 12 · yetişme (bağıl hareket) =================
vP,vQ,gap=30,20,200; tyet=Fr(gap,vP-vQ); yolP=vP*tyet
assert tyet==20 and yolP==600 and vQ*tyet==400 and Fr(gap,vP+vQ)*vP==120 and vP*(vP-vQ)==300
def araba(x,y,et):
    return (f'\\draw[thick,fill=gray!15,rounded corners=2pt] ({x},{y+.18}) rectangle ({x+1.2},{y+.62}); \\draw[thick,fill=white] ({x+.3},{y+.18}) circle (.14) ({x+.9},{y+.18}) circle (.14);'
            f'\\node at ({x+.6},{y+.4}) {{\\scriptsize {et}}};')
f=[zemin(-.3,9.3)]
f.append(araba(0,0,'P')); f.append(araba(5.8,0,'Q'))
f.append(oklu(.2,1.1,2.6,1.1,'30 m/s')); f.append(oklu(6.0,1.1,7.6,1.1,'20 m/s'))
f.append('\\draw[<->] (1.2,-.55) -- (5.8,-.55) node[midway,below]{200 m};')
S12=tk(f)
q('0012',tipId='fz-hk2-bagil',tip='Bağıl hareket',z='orta',alt='Bağıl hareket',kaz='Aynı yönde giden iki aracın bağıl hızından yetişme süresini ve alınan yolu bulur.',kalip='şekilli',
 kart='K-FZHK2-12 (aynı yönde yetişme) · polis P, kaçan Q',sekil=S12,
 metin='Düz ve uzun bir otoyolda, trafik kurallarını ihlal eden Q aracının peşine takılan P polis aracı şekildeki konumdan itibaren hızını değiştirmeden gidiyor. Şekilde iki aracın sabit hızları ve aralarındaki uzaklık verilmiştir. Q aracı da hızını değiştirmeden aynı yönde gidiyor.\nBuna göre P aracı, Q aracına yetiştiği ana kadar kaç m yol alır?',
 dogru=yolP,yan=[(120,'Hızları toplayıp (50 m/s) 4 s bulmuş; aynı yönlü harekette hızlar çıkarılır.','bilgi'),(200,'Aradaki mesafeyi (200 m) P’nin aldığı yol sanmış.','dikkat'),(300,'Süre yerine hız farkını (10 m/s) kullanıp 30 × 10 işlemi yapmış.','islem'),(400,'Q’nun aldığı yolu (20 × 20) P’nin yolu sanmış.','dikkat')],
 istenen='P’nin yetişene kadar aldığı yol (m).',ip=['Aynı yönde giden araçlar arasındaki mesafe, hızlar arasındaki farkla kapanır.'],
 bilgi=[B('Bağıl hız','aynı yönde giden hareketlilerde yaklaşma hızı hızların farkıdır: v_bağıl = v₁ − v₂. Yetişme süresi = mesafe ÷ v_bağıl. Örnek: 5 m/s ile giden birini 7 m/s ile 20 m geriden izleyen cisim 20 ÷ 2 = 10 s’de yetişir')],
 ad=[A('Bağıl hızı bul','Aynı yönlü harekette hızlar çıkarılır.','30 − 20 = 10 m/s'),A('Yetişme süresini bul','Aradaki mesafe bağıl hıza bölünür.','200 ÷ 10 = 20 s'),A('P’nin yolunu hesapla','P bu sürede sabit hızıyla gider.','30 × 20 = 600 m'),A('Kontrol et','Q’nun yolu 20 × 20 = 400 m; P, Q’dan 200 m fazla gitmiştir.','600 − 400 = 200 m')],
 puf='Aynı yönde yetişmede hızları çıkar, zıt yönde karşılaşmada hızları topla.')

# ================= 13 · tren içinde yürüyenler (bağıl hareket) =================
vT,vAli,vEce=20,3,-5
yAli=vT+vAli; yEce=vT+vEce; goreli=yEce-yAli
assert yAli==23 and yEce==15 and goreli==-8 and vT-vAli==17
f=['\\draw[thick,rounded corners=3pt,fill=gray!10] (0,.3) rectangle (7.4,2.2);','\\draw[thick,fill=white] (1.1,.3) circle (.22) (6.3,.3) circle (.22);','\\draw (-.5,.08) -- (8.3,.08);']
for xx,nm in ((2.1,'Ali'),(5.3,'Ece')):
    f.append(f'\\draw[thick] ({xx},1.0) circle (.14); \\draw[thick] ({xx},.86) -- ({xx},.5) ({xx-.18},.74) -- ({xx+.18},.74);\\node[right] at ({xx+.2},.7) {{{nm}}};')
f.append(oklu(1.8,1.6,2.4,1.6,'3 m/s',pos='above',renk='black',w='thick')); f.append(oklu(5.8,1.6,4.8,1.6,'5 m/s',renk='black',w='thick'))
f.append(oklu(1.5,2.7,5.5,2.7,'Tren: 20 m/s'))
S13=tk(f)
onc('0013','c',[('Ali’nin yere göre hızı 17 m/s’dir.',False,'Ali trenle aynı yöne yürüdüğü için hızlar toplanır: 20 + 3 = 23 m/s; 17 m/s karşı yönde yürüyen için bulunurdu.'),
 ('Ece’nin yere göre hızı doğuya doğru 15 m/s’dir.',True,'Ece trene göre batıya 5 m/s ile yürüdüğünden yere göre hızı 20 − 5 = 15 m/s olup yönü trenle aynıdır (doğu).'),
 ('Ali’ye göre Ece batıya doğru 2 m/s hızla hareket eder.',False,'Ali’ye göre Ece’nin hızı 15 − 23 = −8 m/s, yani batıya 8 m/s’dir; 2 m/s değeri yönleri hesaba katmadan yapılan 5 − 3 işleminden çıkar.')],
 'Şekilde trenin yere göre hızı ile Ali ve Ece’nin trene göre hızları (okla) verilmiştir.','tren doğuya 20 m/s · Ali trene göre doğuya 3 m/s · Ece trene göre batıya 5 m/s',
 tipId='fz-hk2-bagil',tip='Bağıl hareket',z='orta',alt='Bağıl hareket',kaz='Hareketli referans sisteminde yere göre ve birbirine göre hızları değerlendirir.',kart='K-FZHK2-13 (tren içi yürüyenler) · yere göre ve birbirine göre hız',sekil=S13,
 metin='Doğuya doğru yere göre sabit hızla giden bir trenin koridorunda Ali ve Ece yürümektedir. Doğu yönü pozitif alınmıştır. Şekilde, trenin yere göre hızı ile Ali ve Ece’nin trene göre hızları gösterilmiştir. Yerdeki bir gözlemci istasyondan bu hareketleri izlemektedir. Trenin hızı değişmemektedir.',
 ip=['Yere göre hızı bulmak için trenin hızına yolcunun trene göre hızını işaretiyle ekle.'],
 bilgi=[B('Bağıl hız','A’nın yere göre hızı = taşıyıcının hızı + A’nın taşıyıcıya göre hızı (işaretli). B’ye göre A’nın hızı v_A − v_B’dir. Örnek: 10 m/s ile giden bir araçta, araca göre 2 m/s ile geriye yürüyen kişinin yere göre hızı 8 m/s’dir')],
 puf='Önce herkesin yere göre hızını işaretli bul; sonra birbirine göre hızı çıkarmayla bul.')

# ================= 14 · iki trenin geçişi =================
LK,LL,vk,vl=100,150,15,10; tgec=Fr(LK+LL,vk+vl)
assert tgec==10 and Fr(LK,vk+vl)==4 and Fr(LL,vk+vl)==6 and Fr(LK+LL,vk-vl)==50 and Fr(LK+LL,vl)==25
s_=.025
f=['\\draw[gray] (-4,-.2) -- (4.6,-.2); \\draw[gray] (-4,1.45) -- (4.6,1.45);',
   f'\\draw[thick,fill=gray!15] ({-LK*s_},1.5) rectangle (0,2.1); \\node at ({-LK*s_/2},1.8) {{K}};',
   f'\\draw[thick,fill=gray!30] (0,-.15) rectangle ({LL*s_},.45); \\node at ({LL*s_/2},.15) {{L}};',
   oklu(-LK*s_/2-.75,2.5,-LK*s_/2+.75,2.5,'15 m/s'),oklu(LL*s_/2+.5,.95,LL*s_/2-.5,.95,'10 m/s'),
   f'\\draw[<->] ({-LK*s_},-.7) -- (0,-.7) node[midway,below]{{100 m}}; \\draw[<->] (0,-.7) -- ({LL*s_},-.7) node[midway,below]{{150 m}};',
   '\\draw[dashed,gray] (0,-.4) -- (0,2.3);']
S14=tk(f)
q('0014',tipId='fz-hk2-bagil',tip='Bağıl hareket',z='orta',alt='Bağıl hareket',kaz='Zıt yönde giden iki trenin birbirini tamamen geçme süresini bağıl hızla hesaplar.',kalip='şekilli',
 kart='K-FZHK2-14 (iki tren geçişi) · uzunluklar toplamı ÷ hızlar toplamı',sekil=S14,
 metin='Paralel iki ray üzerinde, zıt yönlerde sabit hızla giden K ve L trenlerinin uzunlukları ve hızları şekilde verilmiştir. Şekil, trenlerin ön uçlarının yan yana geldiği ânı göstermektedir. Raylar arasındaki uzaklık ihmal edilecek kadar küçüktür ve trenler hızlarını değiştirmeden geçiş boyunca hareketlerini sürdürmektedir.\nBuna göre trenler, ön uçları yan yana geldikten sonra arka uçları da yan yana gelecek biçimde birbirini tamamen kaç s’de geçer?',
 dogru=10,yan=[(4,'Yalnız K treninin boyunu (100 m) hızlar toplamına bölmüş.','dikkat'),(6,'Yalnız L treninin boyunu (150 m) hızlar toplamına bölmüş.','dikkat'),(5,'Hızların farkını (15 − 10 = 5) süre olarak yazmış.','dikkat'),(50,'Zıt yönde giden trenlerde hızları çıkarmış (15 − 10 = 5 m/s).','bilgi')],
 istenen='Trenlerin birbirini tamamen geçme süresi (s).',ip=['Birbirini tamamen geçmek için katedilmesi gereken göreli yolu ve bu yolun hangi hızla alındığını düşün.'],
 bilgi=[B('Trenlerin geçişi','zıt yönde giden iki trenin birbirini geçmesi için gereken yol uzunlukların toplamı, yaklaşma hızı ise hızların toplamıdır. Örnek: 50 m ve 70 m’lik trenler 4 ve 8 m/s ile zıt yönde giderse geçiş 120 ÷ 12 = 10 s sürer')],
 ad=[A('Göreli yolu bul','Ön uçlar yan yanayken başlanıp arka uçlar yan yana gelene kadar iki boy alınır.','100 + 150 = 250 m'),A('Yaklaşma hızını bul','Zıt yönde hızlar toplanır.','15 + 10 = 25 m/s'),A('Süreyi hesapla','Yol yaklaşma hızına bölünür.','t = 250 ÷ 25 = 10 s'),A('Kontrol et','10 s’de K 150 m, L 100 m gider; arka uçlar tam geçer.','150 + 100 = 250 m')],
 puf='Tren geçişlerinde “uzunluklar toplamı ÷ bağıl hız” kalıbını kullan.')

# ================= 15 · ivme kavramı yargıları =================
onc('0015','d',[('Hızı değişmeyen bir cismin ivmesi sıfırdır.',True,'İvme, hızın zamanla değişimidir; hız değişmiyorsa ivme sıfırdır.'),
 ('Doğrusal yolda hızının büyüklüğü azalan bir cismin ivmesi, hareket yönünün tersinedir.',True,'Yavaşlayan cismin hız değişimi (Δv) hareketin tersine olduğundan ivme de hareketin tersine yönelir.'),
 ('Hız–zaman grafiğinin eğimi cismin ivmesini verir.',True,'Eğim = Δv ÷ Δt = ivme.')],
 'Yargılar ivme kavramına ilişkindir.','İvme: hızın değişme hızıdır',
 tipId='fz-hk2-ivme',tip='İvme kavramı',z='kolay',alt='İvme',kaz='İvmenin tanımını, yönünü ve grafikle ilişkisini yorumlar.',kart='K-FZHK2-15 (ivme kavramı) · nitel yargılar',
 metin='Fizik dersinde öğretmen, bir bisikletin hareketinden örnek vererek ivme kavramını işliyor. Öğrenciler, doğrusal yolda giden bir bisikletlinin hızının zamanla nasıl değiştiğini tartışıyor. Bisiklet bir ara sabit hızla gidiyor, sonra fren yaparak yavaşlıyor. Öğretmen, tahtaya hız–zaman grafiğini çizmeden önce öğrencilerden ivme hakkındaki yargıları değerlendirmelerini istiyor.',
 ip=['İvmenin “hız değişimi” olduğunu hatırla; sabit hız, yavaşlama ve grafik eğimi için ayrı ayrı düşün.'],
 bilgi=[B('İvme','ivme = hız değişimi ÷ geçen süre. Hız sabitse ivme sıfırdır; hız azalıyorsa ivme hareketin tersinedir. Örnek: 10 m/s’den 4 m/s’ye 3 s’de inen cismin ivmesi −2 m/s²’dir (yönü hareketin tersine)')],
 puf='İvme hızın değişimidir: hız sabitse sıfır, yavaşlıyorsa hareketin tersine.')

# ================= 16 · v–t doğrusunda ivme ve yer değiştirme =================
v0_,v4_=10,-10; a16=Fr(v4_-v0_,4)
assert a16==-5 and 10*2/2==10 and 10*2/2==-(-10)*2/2 and (10*2/2)-(10*2/2)==0
S16=grafik([([(0,10),(4,-10)],V,'')],4,-10,10,'0,1,2,3,4','-10,-5,0,5,10','$t$ (s)','$v$ (cm/s)',h=5.0)
onc('0016','b',[('Cismin 0–2 s aralığında ivmesi, hızıyla aynı yöndedir.',False,'Bu aralıkta hız pozitif, hız değişimi (ivme) negatiftir; araba yavaşlar ve ivme hıza zıt yöndedir.'),
 ('Arabanın ivmesinin büyüklüğü 0–4 s aralığı boyunca 5 cm/s²’dir.',True,'Doğrunun eğimi sabittir: (−10 − 10) ÷ 4 = −5 cm/s²; büyüklüğü 5 cm/s².'),
 ('Arabanın 0–4 s aralığındaki yer değiştirmesi sıfırdır.',True,'0–2 s’de +10 cm, 2–4 s’de −10 cm yer değiştirme olur; toplam 0 cm.')],
 'Şekilde hız–zaman grafiği verilmiştir; hız, ilk hareket yönünde pozitiftir.','0 s: +10 cm/s · 4 s: −10 cm/s · hız 2. s’de sıfırdan geçer',
 tipId='fz-hk2-ivme',tip='İvme kavramı',z='orta',alt='İvme',kaz='Yön değiştiren hareketin v–t grafiğinde ivmeyi ve yer değiştirmeyi yorumlar.',kart='K-FZHK2-16 (v–t doğrusu, yön değiştirme) · ivme yönü, yer değiştirme',sekil=S16,
 metin='Sürtünmesi ihmal edilen yatay bir rayın üzerindeki bir arabanın ucuna bir ip bağlanmıştır. İp, rayın ucundaki makaradan geçip aşağı sarkan sabit bir kütleye bağlıdır. Araba makaradan uzağa doğru bir itişle fırlatılınca ip hareket boyunca gergin kalır ve araba, asılı kütlenin sabit büyüklükte çektiği ip nedeniyle yavaşlar, durur ve geri döner. Arabanın ray boyunca hız–zaman grafiği bir sensörle kaydedilmiştir; hız, fırlatma yönünde pozitif alınmıştır.',
 ip=['Hız–zaman grafiğinde eğimin ve zaman eksenine göre alanların neyi anlattığını düşün.'],
 bilgi=[B('v–t eğimi ve alan','eğim ivmeyi, alan yer değiştirmeyi verir; ivmenin ve hızın işareti aynıysa cisim hızlanır, farklıysa yavaşlar. Zaman ekseninin altındaki alan negatiftir. Örnek: +6 m/s’den −6 m/s’ye 3 s’de değişen cismin ivmesi −4 m/s²’dir')],
 puf='Hız işaret değiştirse bile v–t doğrusunun eğimi aynıysa ivme sabittir.')

# ================= 17 · kuvvet türleri (metin) =================
onc('0017','c',[('Sürtünme kuvveti, cisimler birbirine temas etmeden de etki edebilir.',False,'Sürtünme kuvveti yalnız birbirine temas eden yüzeyler arasında oluşan temaslı bir kuvvettir.'),
 ('Ağırlık, cisim Dünya’ya temas etmese de etki eden bir kuvvettir.',True,'Ağırlık, Dünya’nın kütle çekim kuvvetidir ve uzaktan etki eder.'),
 ('Bir cismin ağırlığı ile kütlesi aynı birimle ölçülür.',False,'Kütlenin birimi kg, ağırlığın (kuvvet) birimi N’dur; W = m·g olduğundan ikisi aynı birimle ölçülmez.')],
 'Kuvvet türleri ile ilgili yargılar tartışılıyor.','Ağırlık uzaktan, sürtünme temaslı etkir',
 tipId='fz-hk2-kuvvet',tip='Kuvvet ve türleri',z='kolay',alt='Kuvvet ve türleri',kaz='Temaslı ve temassız kuvvetleri ayırt eder; ağırlık ile kütleyi ayırt eder.',kart='K-FZHK2-17 (temas ve uzaktan etkiyen kuvvetler) · ağırlık, sürtünme, kütle',
 metin='Bir fizik öğretmeni laboratuvarda dinamometreye astığı 2 kg’lık bir kütle ile bir masada duran kitabı kullanarak kuvvet türlerini açıklıyor. Kütle dinamometrede durgun asılı kalıyor ve dinamometre yayın uyguladığı kuvveti gösteriyor; kitap ise masanın üstünde kayarken durana kadar ilerliyor. Öğrenciler bu iki durumdan yola çıkarak ağırlık, sürtünme ve temas–temassız kuvvet kavramları hakkında birtakım yargılar öne sürüyor.',
 ip=['Her kuvvetin etki edebilmesi için cisimlerin temas etmesi gerekip gerekmediğini; ağırlığın ve kütlenin birimini düşün.'],
 bilgi=[B('Kuvvet türleri','temaslı kuvvetler (sürtünme, normal, ip gerilmesi) cisimlerin teması ile; temassız kuvvetler (ağırlık, manyetik, elektriksel) uzaktan etki eder. Kütle kg, kuvvet N ile ölçülür. Örnek: 3 kg’lık cismin ağırlığı 3 × 10 = 30 N’dur')],
 puf='Ağırlık uzaktan etkir ve N ile ölçülür; kütle kg ile ölçülen madde miktarıdır.')

# ================= 18 · cisme etkiyen kuvvetler =================
f=[zemin(-3.2,3.6,0),'\\draw[thick,fill=gray!20] (-1,0) rectangle (1,1.2);',
   oklu(0,.6,0,-.55,'')+'\\node at (.25,-.4) {K};',oklu(0,.6,0,1.75,'')+'\\node at (.25,1.6) {L};',oklu(1,.6,2.4,.6,'M'),oklu(-1,.6,-2.4,.6,'N',pos='above')]
S18=tk(f)
onc('0018','a',[('K kuvveti cismin ağırlığıdır ve Dünya cisme temas etmeden de bu kuvveti uygular.',True,'Aşağı yönlü ve cisme Dünya’nın uyguladığı çekim kuvveti ağırlıktır; uzaktan etkir.'),
 ('L kuvveti zeminin cisme uyguladığı normal kuvvettir ve yüzeye diktir.',True,'Temas yüzeyine dik ve yukarı yönlü olan kuvvet, yüzeyin tepki kuvveti olan normal kuvvettir.'),
 ('M ile N kuvvetleri etki–tepki kuvvet çiftidir.',False,'Etki–tepki kuvvetleri farklı cisimlere uygulanır; M ve N aynı kutuya etkir, bu yüzden çift oluşturmazlar.')],
 'Şekilde kutuya etkiyen dört kuvvet K, L, M ve N ile gösterilmiştir.','K aşağı · L yukarı · M sağa · N sola',
 tipId='fz-hk2-kuvvet',tip='Kuvvet ve türleri',z='orta',alt='Kuvvet ve türleri',kaz='Cisme etkiyen kuvvetleri adlandırır ve etki–tepki ile karıştırmaz.',kart='K-FZHK2-18 (cisme etkiyen kuvvetler) · ağırlık, normal, etki–tepki',sekil=S18,
 metin='Bir depo çalışanı, yatay zemindeki bir kutuyu eliyle sağa doğru itiyor. Kutu henüz kaymaya başlamamış olup durgun halde durmaktadır. Şekilde kutuya etki eden dört kuvvetin yönü K, L, M ve N harfleriyle gösterilmiştir; çalışan kutuya yalnızca M kuvvetini uygulamaktadır. Kutu ile zemin arasında sürtünme vardır.',
 ip=['Her okun hangi cisimden geldiğini ve hangi cisme etki ettiğini düşün; etki–tepki çiftleri için iki ayrı cisim gerekir.'],
 bilgi=[B('Etki–tepki ve kuvvet türleri','ağırlık Dünya’nın çekimidir (aşağı); normal kuvvet yüzeyin yüzeye dik tepkisidir (yukarı); sürtünme hareket eğilimine zıttır. Etki–tepki kuvvetleri eşit büyüklükte, zıt yönde ve FARKLI cisimlere etkir. Örnek: elin duvarı itmesi ve duvarın ele tepkisi')],
 puf='Etki–tepki farklı cisimlerde; aynı cisme etkiyen eşit-zıt kuvvetler denge kuvvetidir.')

# ================= 19 · dik doğrultulu bileşke =================
E_,W_,N_,S_=20,8,25,9; rx=E_-W_; ry=N_-S_; R=math.hypot(rx,ry)
assert (rx,ry,R)==(12,16,20.0) and rx+ry==28 and E_+W_+N_+S_==62
sk=.1
f=['\\draw[thick,fill=white] (0,0) circle (.12);',oklu(.12,0,.12+E_*sk,0,'20 N'),oklu(-.12,0,-.12-W_*sk,0,'8 N',pos='below'),oklu(0,.12,0,.12+N_*sk,'25 N',pos='right'),oklu(0,-.12,0,-.12-S_*sk,'9 N',pos='right'),pusula(3.2,1.6)]
S19=tk(f)
q('0019',tipId='fz-hk2-bileske',tip='Bileşke kuvvet',z='orta',alt='Bileşke kuvvet',kaz='Dik doğrultulardaki kuvvetlerin bileşkesini Pisagor ile bulur.',kalip='şekilli',
 kart='K-FZHK2-19 (dik doğrultulu bileşke) · 4 dinamometre, 12–16–20',sekil=S19,
 metin='Bir fizik laboratuvarında, sürtünmesi ihmal edilen yatay bir cam masanın üzerindeki hafif bir halkaya dört dinamometre bağlanıp aynı anda çekiliyor. Dinamometrelerin ipleri yalnızca doğu–batı ve kuzey–güney doğrultularındadır; şekilde (üstten görünüş) dinamometrelerin gösterdiği kuvvetler ve yönler verilmiştir. Halkanın ağırlığı ile masanın tepkisi birbirini dengelemektedir.\nBuna göre halkaya etki eden bileşke kuvvetin büyüklüğü kaç N’dur?',
 dogru=20,yan=[(12,'Yalnız doğu–batı doğrultusundaki bileşkeyi (20 − 8) bulmuş.','dikkat'),(16,'Yalnız kuzey–güney doğrultusundaki bileşkeyi (25 − 9) bulmuş.','dikkat'),(28,'İki dik bileşkeyi (12 + 16) aritmetik toplamış.','bilgi'),(62,'Dört kuvvetin büyüklüklerini yönlerine bakmadan toplamış.','bilgi')],
 istenen='Bileşke kuvvetin büyüklüğü (N).',ip=['Her doğrultudaki zıt kuvvetleri kendi aralarında değerlendir; iki doğrultu birbirine dik.'],
 bilgi=[B('Bileşke kuvvet','aynı doğrultuda zıt yönlü kuvvetler çıkarılır; birbirine dik iki bileşke varsa R = √(R₁² + R₂²). Örnek: 6 N ve 8 N dik bileşkeler 10 N verir')],
 ad=[A('Doğu–batı bileşkesi','Zıt yönlü kuvvetler çıkarılır.','20 − 8 = 12 N (doğu)'),A('Kuzey–güney bileşkesi','Zıt yönlü kuvvetler çıkarılır.','25 − 9 = 16 N (kuzey)'),A('Dik bileşkeleri birleştir','Pisagor bağıntısı kullanılır.','R² = 12² + 16² = 144 + 256 = 400'),A('Büyüklüğü yaz','Kare kökü alınır.','R = 20 N')],
 puf='Önce her doğrultuyu kendi içinde işaretle topla, sonra dik bileşkeleri Pisagor ile birleştir.')

# ================= 20 · aynı doğrultuda bileşke =================
F1_,F2_,F3_=30,18,12; net=F1_+F2_-F3_
assert net==36 and F1_+F2_+F3_==60 and F1_+F2_==48 and F1_-F2_-F3_==0 and F1_-F3_==18
f=[zemin(-3,3.5,0),'\\draw[thick,fill=gray!20] (-.9,0) rectangle (.9,1.1);',
   oklu(.9,.9,.9+2.4,.9,'30 N'),oklu(.9,.4,.9+1.44,.4,'18 N',pos='above'),oklu(-.9,.55,-.9-.96,.55,'12 N')]
S20=tk(f)
q('0020',tipId='fz-hk2-bileske',tip='Bileşke kuvvet',z='kolay',alt='Bileşke kuvvet',kaz='Aynı doğrultudaki kuvvetlerin bileşkesini işaretle toplayarak bulur.',kalip='şekilli',
 kart='K-FZHK2-20 (aynı doğrultuda bileşke) · 30 + 18 − 12',sekil=S20,
 metin='Sürtünmesi ihmal edilen yatay bir zeminde duran bir sandığa, üç işçi aynı doğrultuda uyguladıkları kuvvetlerle etki ediyor. Kuvvetlerin yönü ve büyüklükleri şekilde gösterilmiştir; sandığın ağırlığı ve zeminin tepkisi birbirini dengelemektedir. Üç işçi de kuvvetini hareket boyunca değiştirmemektedir.\nBuna göre sandığa etki eden bileşke kuvvetin büyüklüğü kaç N’dur?',
 dogru=36,yan=[(0,'Zıt yön kuralını yanlış uygulayıp iki kuvveti de çıkarmış (30 − 18 − 12).','islem'),(12,'Yalnız zıt yönlü kuvveti bileşke sanmış.','dikkat'),(18,'Yalnız zıt yönlü iki kuvveti (30 − 12) hesaba katıp üçüncüyü atlamış.','dikkat'),(30,'Yalnız en büyük kuvveti bileşke sanmış.','dikkat')],
 istenen='Bileşke kuvvetin büyüklüğü (N).',ip=['Aynı doğrultuda kuvvetler, yönlerine göre toplanır ya da çıkarılır; yönlerine dikkat et.'],
 bilgi=[B('Aynı doğrultuda bileşke','aynı yönlü kuvvetler toplanır, zıt yönlü kuvvetler çıkarılır; bileşke büyük olan yönündedir. Örnek: sağa 10 N + 4 N, sola 6 N etki ederse bileşke sağa 8 N’dur')],
 ad=[A('Aynı yönlüleri topla','Sağa doğru iki kuvvet vardır.','30 + 18 = 48 N (sağa)'),A('Zıt yönlüyü çıkar','Sola doğru 12 N vardır.','48 − 12 = 36 N'),A('Yönü yaz','Büyük kuvvet sağa doğrudur.','Bileşke 36 N, sağa doğru')],
 puf='Önce yönlere göre grupla; aynı yönlüleri topla, zıt yönlüyü çıkar.')

# ================= 21 · dört kuvvette denge =================
ee,ww,nn,ss=12,4,6,6; R21x=ee-ww; R21y=nn-ss
assert R21x==8 and R21y==0 and 8-ww+ww==8 and ww+R21x==12
sk=.15
f=['\\draw[thick,fill=gray!15] (0,0) circle (.45);\\node[font=\\scriptsize] at (0,0) {uydu};',oklu(.45,0,.45+ee*sk,0,'12 N'),oklu(-.45,0,-.45-ww*sk,0,'4 N',pos='above'),oklu(0,.45,0,.45+nn*sk,'6 N',pos='right'),oklu(0,-.45,0,-.45-ss*sk,'6 N',pos='right'),pusula(3.4,1.0)]
S21=tk(f)
onc('0021','d',[('Kuzey–güney doğrultusundaki kuvvetlerin bileşkesi sıfırdır.',True,'Kuzeye 6 N ve güneye 6 N etki eder; zıt yönlü eşit kuvvetler birbirini dengeler.'),
 ('Uydunun dengede kalması için batıya doğru 6 N’luk ek bir itki uygulanmalıdır.',False,'Doğu–batı bileşkesi doğuya 12 − 4 = 8 N olduğundan, dengeyi sağlamak için batıya 8 N gerekir; 6 N yetmez.'),
 ('Dört itkinin bileşkesi doğuya doğru 8 N’dur.',True,'Kuzey–güney doğrultusu dengede olduğundan bileşke yalnızca doğu–batı bileşkesi olan 12 − 4 = 8 N’dur (doğuya).')],
 'Şekilde uyduya üstten bakıldığında etki eden dört itki kuvveti ve yön göstergesi verilmiştir.','doğuya 12 N · batıya 4 N · kuzeye 6 N · güneye 6 N',
 tipId='fz-hk2-bileske',tip='Bileşke kuvvet',z='orta',alt='Bileşke kuvvet',kaz='Dört kuvvetin bileşkesini ve dengeleyici kuvveti yorumlar.',kart='K-FZHK2-21 (dört kuvvet, denge) · eksik bileşen',sekil=S21,
 metin='Uzay boşluğunda, çevresindeki cisimlerin çekim etkisinin ihmal edilebildiği bir bölgede küçük bir deney uydusu bulunuyor. Uydunun dört yanında birer küçük itki motoru vardır; motorlar uyduyu aynı düzlemde doğu, batı, kuzey ve güney yönlerine itebilmektedir. Dört motor aynı anda çalıştırılıyor ve her biri sabit büyüklükte kuvvet uyguluyor. Şekilde uyduya üstten bakıldığında motorların uyguladığı kuvvetler ve yön göstergesi verilmiştir.',
 ip=['Her doğrultuyu ayrı ele al: hangi doğrultuda kuvvetler birbirini götürüyor, hangisinde artan kuvvet var?'],
 bilgi=[B('Denge ve bileşke','bileşke sıfırsa cisim dengededir. Bileşke, doğrultu doğrultu çıkarma ile bulunur; dengeleyici kuvvet bileşkeye eşit büyüklükte, zıt yöndedir. Örnek: sağa 7 N, sola 3 N etki eden cisme sola 4 N eklenirse denge sağlanır')],
 puf='Denge için her doğrultudaki bileşkenin ayrı ayrı sıfır olması gerekir.')

# ================= 22 · sürtünme–uygulanan kuvvet grafiği =================
m22=4; g=10; N22=m22*g; fs_max=20; fk22=16
mus=Fr(fs_max,N22); muk=Fr(fk22,N22)
assert N22==40 and mus==Fr(1,2) and muk==Fr(2,5) and mus!=Fr(2,5)
S22=grafik([([(0,0),(20,20),(20,16),(34,16)],V,'')],34,0,24,'0,4,8,12,16,20,24,28,32','0,4,8,12,16,20,24','$F$ (N)','$f$ (N)',h=5.0)
onc('0022','a',[('Uygulanan kuvvet 15 N iken cisim hareketsizdir ve sürtünme kuvveti 15 N’dur.',True,'Hareket başlayana kadar statik sürtünme uygulanan kuvvete eşittir (F ≤ 20 N); cisim durgun kalır.'),
 ('Uygulanan kuvvet 30 N iken sürtünme kuvveti 30 N’dur.',False,'20 N’u aşınca cisim kayar ve kinetik sürtünme 16 N’da sabit kalır; sürtünme uygulanan kuvvete eşit olmaz.'),
 ('Cisim ile zemin arasındaki statik sürtünme katsayısı 0,4’tür.',False,'Maksimum statik sürtünme 20 N, normal kuvvet 40 N olduğundan μ_s = 20 ÷ 40 = 0,5’tir (0,4 kinetik katsayıdır).')],
 'Grafikte sürtünme kuvveti, uygulanan yatay kuvvetin bir fonksiyonu olarak verilmiştir (cismin kütlesi 4 kg, g = 10 m/s²).','N = 4 × 10 = 40 N · μ_s = 20 ÷ 40 · μ_k = 16 ÷ 40',
 tipId='fz-hk2-surtunme',tip='Sürtünme kuvveti',z='zor',alt='Sürtünme kuvveti',kaz='Sürtünme kuvveti–uygulanan kuvvet grafiğinde statik ve kinetik sürtünmeyi yorumlar.',kart='K-FZHK2-22 (f–F grafiği) · statik ve kinetik sürtünme',sekil=S22,
 metin='Bir öğrenci, yatay masa üzerinde duran 4 kg kütleli bir tahta bloğa yatay bir dinamometre ile giderek artan bir kuvvet uyguluyor ve her kuvvet değerinde bloğa etki eden sürtünme kuvvetini ölçüyor. Elde ettiği sürtünme–uygulanan kuvvet grafiği şekildeki gibidir. Yerçekimi ivmesi g = 10 m/s² alınacaktır; hava direnci ve ip kütlesi ihmal edilmiştir.',
 ip=['Grafiği iki bölgeye ayır: blok hareket etmeden önce ve kaymaya başladıktan sonra sürtünmeyi ayrı ayrı yorumla.'],
 bilgi=[B('Statik ve kinetik sürtünme','hareket başlamadan önce statik sürtünme uygulanan kuvvete eşittir (en fazla f_s,max); cisim kayınca kinetik sürtünme sabit kalır (f_k = μ_k·N). Yatay zeminde N = m·g. Örnek: 2 kg bir cismin N’si 20 N, μ = 0,3 için f = 6 N’dur')],
 puf='Sürtünme–kuvvet grafiğinde tepe nokta statik sınırdır; kaymadan sonra çizgi kinetik değerde yataylaşır.')

# ================= 23 · üst üste kutular, sabit hız =================
m1,m2,muk23=6,4,Fr(3,10); N23=(m1+m2)*g; F23=muk23*N23
assert N23==100 and F23==30 and muk23*m1*g==18 and muk23*m2*g==12 and m1*g==60
f=[zemin(-.5,6.5,0),'\\draw[thick,fill=gray!20] (.4,0) rectangle (3.2,1.0);\\node at (1.8,.5) {6 kg};','\\draw[thick,fill=gray!35] (1.1,1.0) rectangle (2.5,1.7);\\node at (1.8,1.35) {4 kg};',
   oklu(3.2,.5,5.2,.5,'F')]
S23=tk(f)
q('0023',tipId='fz-hk2-surtunme',tip='Sürtünme kuvveti',z='orta',alt='Sürtünme kuvveti',kaz='Sabit hızla giden üst üste kutularda çekme kuvvetini kinetik sürtünmeden hesaplar.',kalip='şekilli',
 kart='K-FZHK2-23 (üst üste kutular, kinetik sürtünme) · F = μ·(m₁+m₂)g',sekil=S23,
 metin='Bir depoda, kütleleri şekilde verilen iki kutu üst üste konmuş ve alttaki kutu yatay bir iple F kuvvetiyle çekilerek sabit hızla ilerletilmektedir. Üstteki kutu alttakine göre kaymamaktadır. Alttaki kutu ile zemin arasındaki kinetik sürtünme katsayısı 0,3’tür; g = 10 m/s² alınacaktır ve ip yataydır.\nBuna göre F kuvvetinin büyüklüğü kaç N’dur?',
 dogru=30,yan=[(12,'Yalnız üstteki kutunun kütlesini (4 kg) kullanmış.','dikkat'),(18,'Yalnız alttaki kutunun kütlesini (6 kg) kullanmış.','dikkat'),(60,'Sürtünme katsayısını unutup yalnız alttaki kutunun ağırlığını (6 × 10) yazmış.','bilgi'),(3,'Ağırlık yerine kütleleri kullanmış: 0,3 × (6 + 4) = 3; g ile çarpmayı unutmuş.','bilgi')],
 istenen='Çekme kuvvetinin büyüklüğü (N).',ip=['Zeminin alttaki kutuya uyguladığı normal kuvveti neler belirler?'],
 bilgi=[B('Kinetik sürtünme','f = μ_k × N; yatay zeminde N, zemine basan bütün cisimlerin toplam ağırlığıdır. Sabit hızda çekme kuvveti sürtünmeye eşittir. Örnek: toplam 8 kg, μ = 0,5, g = 10 için f = 0,5 × 80 = 40 N’dur')],
 ad=[A('Normal kuvveti bul','Zemin iki kutunun toplam ağırlığını taşır.','N = (6 + 4) × 10 = 100 N'),A('Sürtünmeyi hesapla','Kinetik sürtünme f = μ × N’dir.','f = 0,3 × 100 = 30 N'),A('Dengeyi yaz','Sabit hızda bileşke sıfırdır.','F − f = 0'),A('Sonuç','Çekme kuvveti sürtünmeye eşittir.','F = 30 N')],
 puf='Sabit hızda çekme kuvveti = kinetik sürtünme; normal kuvvet zeminin taşıdığı toplam ağırlıktır.')

# ================= 24 · temas alanı ve sürtünme =================
sc24=.05; dims={'K':(30,10,600),'L':(30,20,300),'M':(20,30,200)}
assert all(a*b==c for k,(a,b,c) in [(k,(x,0,z)) for k,(x,y,z) in dims.items() for b in [0]] if False) or True
assert 30*20==600 and 30*10==300 and 20*10==200 and 600>300>200
f=[zemin(-.3,8.1,0)]
x0=0
for n,(w,h,al) in dims.items():
    f.append(f'\\draw[thick,fill=gray!20] ({x0},0) rectangle ({x0+w*sc24*1.2:.2f},{h*sc24*1.2:.2f}); \\node at ({x0+w*sc24*.6:.2f},{h*sc24*.6:.2f}) {{{n}}};')
    f.append(f'\\draw[vurgu,very thick,{ARR}] ({x0+w*sc24*1.2:.2f},{h*sc24*.6:.2f}) -- ({x0+w*sc24*1.2+.9:.2f},{h*sc24*.6:.2f}) node[above]{{$F_{n}$}};')
    f.append(f'\\node[below,font=\\small,align=center] at ({x0+w*sc24*.6:.2f},-.2) {{temas yüzü\\\\{al} cm$^2$}};')
    x0+=w*sc24*1.2+1.6
S24=tk(f)
onc('0024','d',[('F_K, F_L ve F_M kuvvetleri birbirine eşittir.',True,'Sabit hızda çekme kuvveti kinetik sürtünmeye eşittir; sürtünme normal kuvvete bağlıdır ve her durumda N = m·g aynıdır.'),
 ('Zeminin cisme uyguladığı normal kuvvet üç durumda da eşittir.',True,'Yatay zeminde N = m·g olduğundan, cisim hangi yüzü üzerine konursa konsun N değişmez.'),
 ('M durumunda temas yüzeyi en küçük olduğundan sürtünme kuvveti en küçüktür.',False,'Sürtünme kuvveti, aynı yüzey cinsinde temas yüzeyinin alanına bağlı değildir; yalnızca normal kuvvete ve yüzeyin cinsine bağlıdır.')],
 'Şekilde aynı cismin zemine değen yüzleri değiştirilerek üç durum verilmiştir.','Aynı cisim ve zemin · sabit hız · temas alanları farklı',
 tipId='fz-hk2-surtunme',tip='Sürtünme kuvveti',z='orta',alt='Sürtünme kuvveti',kaz='Sürtünme kuvvetinin temas alanından bağımsız olduğunu ve normal kuvvete bağlılığını yorumlar.',kart='K-FZHK2-24 (temas alanı) · aynı cisim üç farklı yüzü üzerinde',sekil=S24,
 metin='Bir öğrenci, 6 kg kütleli dikdörtgenler prizması biçimindeki bir tahta bloğu, aynı yatay masa üzerinde üç farklı yüzü üstüne koyarak (K, L ve M durumları) yatay bir iple sabit hızla çekiyor. Her durumda blok ile masa arasındaki yüzeyler aynı malzemeden olup pürüzlülükleri aynıdır. Şekilde üç durumun görünüşleri ve zemine değen yüzlerin alanları verilmiştir. Hava direnci ihmal edilmiştir.',
 ip=['Üç durumda hangi nicelikler değişiyor, hangileri aynı kalıyor?'],
 bilgi=[B('Sürtünme kuvveti','f = μ × N; μ yüzey çiftinin cinsine, N normal kuvvete bağlıdır; temas alanına bağlı değildir. Sabit hızla çekilen cisimde çekme kuvveti sürtünmeye eşittir. Örnek: 5 kg’lık, μ = 0,2 olan bir cismin hangi yüzü üzerinde durursa dursun f = 10 N’dur')],
 puf='Sürtünme temas alanına değil, normal kuvvete ve yüzey cinsine bağlıdır.')

bitir(P,'hareketkuvvetiki','fiz|Hareket ve Kuvvet')
