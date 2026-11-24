"""AYT Fizik · Özel Görelilik (postülalar, zaman genişlemesi, boy kısalması, kütle-enerji, Michelson-Morley) · 20 soru.
Kardeş yok, ipucu 1. Sayısal cevap ve çeldiriciler Fraction ile hesaplanıp assert edilir; şekil verileri aynı sayılardan üretilir."""
import sys,os,json
from fractions import Fraction as Fr
from math import isqrt
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
KONU_AD='Özel Görelilik'; KEY='afiz|Özel Görelilik'
P=Parti('gorelilik',KONU_AD,KEY,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Fizik özel görelilik soruları (yalnız mantık) · 345 AYT Fizik s.349–370 · Bilgi Sarmal AYT denemeleri'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
def q(no,ad,**k):
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),**k)

def gam(b):
    """b = v/c (Fraction) için Lorentz çarpanı; tam kare olmalı."""
    b=Fr(b); r=1-b*b; n,d=r.numerator,r.denominator
    assert isqrt(n)**2==n and isqrt(d)**2==d,('gamma tam degil',b)
    return 1/Fr(isqrt(n),isqrt(d))
assert gam(Fr(3,5))==Fr(5,4) and gam(Fr(4,5))==Fr(5,3)

# ---------- TikZ yardımcıları ----------
def tk(body,opt=''): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small'+opt+']\n'+body+'\n\\end{tikzpicture}')
AK='blue!65!black'; KR='red!70!black'
def V(p,q_,lab='',side='above',col='vurgu'):
    n=f' node[midway,{side}] {{{lab}}}' if lab else ''
    return '\\draw[%s,very thick,-{Stealth[length=2mm,width=1.8mm]}] (%.3f,%.3f) -- (%.3f,%.3f)%s;'%(col,p[0],p[1],q_[0],q_[1],n)
def ship(x,y,lab='',w=1.8,h=.5,sol=False,fill='gray!25'):
    s=-1 if sol else 1
    pts=[(x-s*w/2,y-h/2),(x+s*(w/2-.4),y-h/2),(x+s*w/2,y),(x+s*(w/2-.4),y+h/2),(x-s*w/2,y+h/2)]
    t='\\draw[thick,fill=%s,rounded corners=1pt] '%fill+' -- '.join('(%.2f,%.2f)'%p for p in pts)+' -- cycle;'
    if lab: t+='\\node at (%.2f,%.2f) {%s};'%(x-s*.15,y,lab)
    return t
def person(x,y,lab='',side='below'):
    t=('\\draw[thick] (%.2f,%.2f) circle (.1);\\draw[thick] (%.2f,%.2f)--(%.2f,%.2f) (%.2f,%.2f)--(%.2f,%.2f) (%.2f,%.2f)--(%.2f,%.2f) (%.2f,%.2f)--(%.2f,%.2f);'
       %(x,y+.52,x,y+.42,x,y+.18,x,y+.18,x-.1,y,x,y+.18,x+.1,y,x-.14,y+.32,x+.14,y+.32))
    if lab: t+='\\node[%s=1pt,align=center] at (%.2f,%.2f) {%s};'%(side,x,y,lab)
    return t
def ground(x0,x1,y=0): return '\\draw[thick] (%.2f,%.2f) -- (%.2f,%.2f);'%(x0,y,x1,y)
def dim(p,q_,lab,side='above'): return '\\draw[<->,thin] (%.3f,%.3f) -- (%.3f,%.3f) node[midway,%s,fill=white,inner sep=1pt] {%s};'%(p[0],p[1],q_[0],q_[1],side,lab)
def f1(items): return '\n'.join(items)
def table(title,hdr,rows,cw,rh=.7):
    W=sum(cw); Hh=rh*(len(rows)+1); s=[]
    if title: s.append('\\node[font=\\small\\bfseries] at (%.2f,%.2f) {%s};'%(W/2,Hh+.35,title))
    s.append('\\draw[thick] (0,0) rectangle (%.2f,%.2f);'%(W,Hh))
    for i in range(1,len(rows)+1): s.append('\\draw (0,%.2f)--(%.2f,%.2f);'%(i*rh,W,i*rh))
    xs=[0]
    for w in cw: xs.append(xs[-1]+w)
    for x in xs[1:-1]: s.append('\\draw (%.2f,0)--(%.2f,%.2f);'%(x,x,Hh))
    for j,h in enumerate(hdr): s.append('\\node[font=\\small\\bfseries] at (%.2f,%.2f) {%s};'%((xs[j]+xs[j+1])/2,Hh-rh/2,h))
    for i,r in enumerate(rows):
        for j,c in enumerate(r): s.append('\\node at (%.2f,%.2f) {%s};'%((xs[j]+xs[j+1])/2,Hh-rh*(i+1.5),c))
    return '\n'.join(s)

# ---------- öncüllü yardımcısı (doğrulukların tek kaynağı stm) ----------
ROM=['I','II','III']
COMB=[('Yalnız I',{0}),('Yalnız II',{1}),('Yalnız III',{2}),('I ve II',{0,1}),('I ve III',{0,2}),('II ve III',{1,2}),('I, II ve III',{0,1,2})]
def onc(no,hedef,giris,stm,ip,bilgi,puf,istenen,tipId,tip,z,alt,kaz,kart,kalip,sekil=None,kok='yargılarından hangileri doğrudur?'):
    T={i for i,s in enumerate(stm) if s[1]}
    idx=[i for i,(a,b) in enumerate(COMB) if b==T]; assert len(idx)==1; ci=idx[0]; p='ABCDE'.index(hedef)
    assert p<=ci and 4-p<=6-ci,(no,ci,p)
    win=COMB[ci-p:ci-p+5]; assert len(win)==5 and win[p][1]==T
    yan=[]
    for a,b in win:
        if b==T: continue
        d=sorted(b^T)
        cel=' '.join(stm[i][3] for i in d)
        yan.append((a,cel,'bilgi'))
    metin=giris+'\nBuna göre,\n'+'\n'.join(f'{ROM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+kok
    ad=[A(f'{ROM[i]}. yargıyı incele',s[2],f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış')) for i,s in enumerate(stm)]
    ad.append(A('Sonucu yaz','Doğru olan yargıları birleştir.',' · '.join(f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış') for i,s in enumerate(stm))+' → '+COMB[ci][0]))
    q(no,ad,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kart=kart,kalip=kalip,metin=metin,dogru=COMB[ci][0],yan=yan,sira=[a for a,b in win],
      istenen=istenen,ip=ip,bilgi=bilgi,puf=puf,sekil=sekil)

# ================= KARTLAR =================
kartla('K-AFGR-01','Postülalar ve ışık hızının değişmezliği','Fizik yasaları tüm eylemsiz sistemlerde aynıdır; ışığın boşluktaki hızı c, kaynağın ve gözlemcinin hareketinden bağımsızdır. Hızlar klasik biçimde toplanıp çıkarılmaz.','Işık hızına kaynak ya da gözlemci hızını eklemek; postülalarla sonuçları karıştırmak.','kolay','şekilli',2,'gr-postula','Postülalar ve ışık hızı')
kartla('K-AFGR-02','Michelson–Morley deneyi','Dik iki koldan gelen ışınların girişiminde esirden beklenen saçak kayması görülmemiştir; ışık hızı doğrultudan ve Dünya’nın hareketinden bağımsızdır, esir varsayımı desteklenmez.','Deneyin ışık hızının kaynağa eklendiğini ya da zamanın yavaşladığını gösterdiğini sanmak.','kolay','şekilli',2,'gr-mm','Michelson–Morley deneyi')
kartla('K-AFGR-03','Zaman genişlemesi','Özel zaman aralığını olayların aynı yerde olduğu gözlemci ölçer ve en kısadır; hareketli saat için diğer gözlemci Δt = γΔt₀ ölçer. Hareket karşılıklıdır.','Hareketli gözlemcinin kendi saatinin yavaşladığını sanmak; genişlemeyi mutlak saymak.','orta','şekilli',3,'gr-zaman','Zaman genişlemesi')
kartla('K-AFGR-04','Boy kısalması','Yalnız hareket doğrultusundaki uzunluk kısalır: L = L₀/γ; durgun (öz) uzunluk en büyüktür, dik boyutlar değişmez.','Dik boyutları da kısaltmak; öz uzunluğu ölçen gözlemciyi karıştırmak.','orta','şekilli',3,'gr-boy','Boy kısalması')
kartla('K-AFGR-05','Kütle–enerji eşdeğerliği','Durgun enerji E₀ = mc²; kütle farkı Δm, ΔE = Δm c² kadar enerjiye karşılık gelir. Durgun kütle hızla değişmez.','Kütleyi enerjiye çevirirken c’yi karesiz kullanmak; birim dönüşümünü atlamak.','orta','tablo',3,'gr-kutle','Kütle–enerji eşdeğerliği')
kartla('K-AFGR-06','Zaman genişlemesi ve boy kısalmasının birlikte kullanımı','Aynı yolculuk yer gözlemcisinde uzun süre ve uzun yol, hareketli gözlemcide kısa süre ve kısa yol olarak ölçülür; iki bakış tutarlıdır.','Genişleme ile kısalmayı aynı gözlemciye uygulamak.','zor','şekilli',4,'gr-birlesik','Zaman genişlemesi ve boy kısalması birlikte')
kartla('K-AFGR-07','Kütleli cisim ve ışık hızı sınırı','Kütleli cisme enerji verildikçe hız artar ama ışık hızına ulaşamaz; hız–zaman eğrisi c’ye yaklaşır.','Newton’daki doğrusal artışı hızın sınırsız artması saymak.','orta','grafik',3,'gr-isik-siniri','Kütleli cisim ve ışık hızı sınırı')
kartla('K-AFGR-08','Karşılıklı zaman genişlemesi','Eylemsiz iki gözlemcinin her biri, diğerinin saatinin kendi saatine göre yavaş işlediğini ölçer; mutlak durgunluk yoktur.','Birinin gerçekten yavaş olduğunu, ölçümün çeliştiğini sanmak.','zor','şekilli',3,'gr-zaman','Zaman genişlemesi')

# ============== SORULAR ==============
# ---- 01 kolay · ışık hızı ve araç (şekil) ----
b1=Fr(1,2); cc1=1
assert cc1==1 and 1+b1==Fr(3,2) and 1-b1==Fr(1,2) and 1+b1/2==Fr(5,4)
SK=tk(f1([ground(-.3,7.2),ship(1.2,1.5,'Araç'),V((1.2,2.0),(2.2,2.0),'$0{,}5c$','above',AK),
  V((2.2,1.5),(5.2,1.5),'ışık atımı','above'),person(6.3,0,'Yerdeki\\\\gözlemci')]))
q('0001',[A('Postülayı hatırla','Işığın boşluktaki hızı, kaynağın ve gözlemcinin hareketinden bağımsız olarak c’dir.','v_ışık = c'),
  A('Araç hızını ele','Araç hızı, ışığın hızına eklenip çıkarılmaz; klasik hız toplamı geçerli değildir.','c + 0,5c ya da c − 0,5c uygulanmaz'),
  A('Gözlemciye uygula','Yerdeki gözlemci de ışığı aynı büyüklükte ölçer.','v_ölçülen = c')],
 tipId='gr-postula',tip='Postülalar ve ışık hızı',z='kolay',alt='Postülalar',kaz='Işık hızının kaynağın hareketinden bağımsız olduğunu kullanarak ölçülen ışık hızını belirler.',
 kart='K-AFGR-01 (hareketli kaynak) · ileri yönde ışık atımı',kalip='şekilli',
 metin='Bir uzay aracı, yere göre sabit 0,5c büyüklüğündeki hızla ilerlerken ilerleme yönünde bir ışık atımı gönderiyor. Atımın hızı yerde duran bir gözlemci tarafından ölçülüyor (c: ışığın boşluktaki hızı).\nBuna göre, yerdeki gözlemcinin ölçtüğü ışık hızı kaçtır?',
 dogru='c',yan=[('0,5c','Işığın hızından aracın hızını çıkarmış: c − 0,5c = 0,5c.','dikkat'),('1,25c','Araç hızının yarısını ışık hızına eklemiş: c + 0,25c.','bilgi'),('1,5c','Araç hızını ışık hızına eklemiş: c + 0,5c; klasik hız toplamasını uygulamış.','bilgi'),('2c','Işığın aracın içinde de, yerde de c ölçüleceğini görüp iki değeri toplamış: c + c.','bilgi')],
 sira=['0,5c','c','1,25c','1,5c','2c'],istenen='Yerdeki gözlemcinin ölçtüğü ışık hızı.',ip=['Işığın boşluktaki hızı, kaynağın hızına göre değişir mi?'],
 bilgi=[B('İkinci postüla','Işığın boşluktaki hızı tüm eylemsiz gözlemciler için aynı c değeridir; kaynağın ve gözlemcinin hızı buna eklenmez. Örnek: yere göre hareketli bir lambanın ışığını yerdeki ve lambaya yakın duran gözlemciler aynı c hızıyla ölçer')],
 puf='Işığın boşluktaki hızı hangi gözlemci, hangi kaynak olursa olsun c’dir.',sekil=SK)

# ---- 02 kolay · postülalar öncüllü ----
onc('0002','B','Einstein tarafından geliştirilen özel görelilik kuramı iki temel varsayım (postüla) üzerine kurulmuştur.',
 [('Hareketli cisimlerin boyu hareket doğrultusunda kısalır.',False,'Boy kısalması kuramın bir sonucudur; temel varsayım olarak alınmaz.','I numaralı yargıda kuramın bir sonucunu varsayım saymış.'),
  ('Işığın boşluktaki hızı, ışık kaynağının hareketinden bağımsızdır.',True,'Bu ifade ikinci postülanın kapsamındadır: ışık hızı kaynağın hareketine bağlı değildir.','II numaralı yargıda ışık hızının kaynak hızına bağlı olduğunu sanmış.'),
  ('Zaman, tüm gözlemciler için aynı hızda akar.',False,'Kuramda zaman mutlak değildir; hareketli gözlemciler için farklı akar. Bu ifade postülalarla çelişir.','III numaralı yargıda Newton mekaniğindeki mutlak zamanı postüla sanmış.')],
 ['Her yargının kuramın temel varsayımı mı yoksa varsayımlardan çıkan sonuç mu olduğunu ayır.'],
 [B('Postülalar ve sonuçlar','Özel görelilik iki postülaya dayanır: fizik yasaları tüm eylemsiz sistemlerde aynıdır; ışığın boşluktaki hızı c’dir ve gözlemciden ve kaynaktan bağımsızdır. Zaman genişlemesi ile boy kısalması bunlardan çıkan sonuçlardır')],
 'Postüla kuramın başlangıç varsayımıdır; zaman genişlemesi ve boy kısalması sonuçtur.','Kuramın postülaları arasında yer alan yargılar.','gr-postula','Postülalar ve ışık hızı','kolay','Postülalar','Özel görelilik postülalarını bu kuramın sonuçlarından ayırt eder.','K-AFGR-01 (postüla–sonuç ayrımı) · nitel öncüllü','öncüllü',kok='yargılarından hangileri bu kuramın postülaları arasında yer alır?')

# ---- 03 kolay · Michelson–Morley düzeneği (şekil) ----
SK=tk(f1(['\\node[left] at (-.1,0) {ışık kaynağı};\\draw[thick] (-.1,0) circle (.08);',
  V((0,0),(1.2,0),'','above'),'\\draw[thick,fill=blue!10] (1.3,-.28) -- (1.7,.28) -- (1.75,.24) -- (1.35,-.32) -- cycle;\\node[below left,align=right] at (1.3,-.3) {yarı geçirgen\\\\ayna};',
  V((1.5,.3),(1.5,1.8),'','right'),'\\draw[ultra thick] (1.0,2.0) -- (2.0,2.0);\\node[left] at (1.0,2.0) {ayna 1};',
  V((1.8,0),(3.6,0),'','above'),'\\draw[ultra thick] (3.8,-.5) -- (3.8,.5);\\node[above] at (3.8,.5) {ayna 2};',
  V((1.5,-.3),(1.5,-1.4),'','right'),'\\draw[thick] (.9,-1.6) -- (2.1,-1.6);\\node[below] at (1.5,-1.6) {ekran (girişim deseni)};',
  V((3.0,-2.6),(4.6,-2.6),'','above'),'\\node[right] at (4.7,-2.6) {Dünya’nın hareket yönü};']))
q('0003',[A('Beklentiyi yaz','Esir kabul edilseydi iki kolda gidiş–dönüş süreleri farklı olur, saçaklar kayardı.','Beklenen: saçak kayması'),
  A('Sonuca bak','Düzenek döndürülse de kayma görülmemiştir; ışık hızı doğrultuya ve Dünya’nın hareketine bağlı değildir.','Gözlenen: kayma yok'),
  A('Şıkkı seç','Bu sonuç esir fikrini desteklemez; ışık hızının her doğrultuda aynı olduğunu destekler.','Doğru: Dünya’nın hareketinden ve doğrultudan bağımsızdır')],
 tipId='gr-mm',tip='Michelson–Morley deneyi',z='kolay',alt='Michelson–Morley',kaz='Michelson–Morley deneyinin sonucunu yorumlar.',
 kart='K-AFGR-02 (düzenek ve sonuç) · saçak kayması yok',kalip='şekilli',
 metin='Michelson–Morley deneyinde bir ışık demeti, yarı geçirgen aynada birbirine dik iki ışına ayrılır; ışınlar aynalardan yansıyıp ekranda girişim deseni oluşturur (şekil). Esir adı verilen bir ortam bulunsaydı Dünya’nın hareket doğrultusundaki kol ile buna dik kolda ışığın gidiş–dönüş süreleri farklı olacağından girişim saçakları kayacaktı. Düzenek döndürülerek yapılan ölçümlerde beklenen kayma gözlenmemiştir.\nBuna göre, bu sonuç aşağıdakilerden hangisini destekler?',
 dogru='Işığın hızı, Dünya’nın hareketinden ve yayılma doğrultusundan bağımsızdır.',
 yan=[('Işığın yayılması için esir adı verilen bir ortam gereklidir.','Beklentiyle sonucu karıştırmış; kayma gözlenmediği için esir desteklenmemiştir.','bilgi'),
  ('Işığın hızı, kaynağın hızına eklenerek ölçülür.','Deneyi kaynak hızıyla ilgili sanmış; deneyde kaynak hızı değiştirilmemiştir.','bilgi'),
  ('Işığın hızı, Dünya’nın hareket yönünde diğer doğrultudan büyüktür.','Kayma olmadığı hâlde hızın doğrultuya bağlı olduğunu düşünmüş.','dikkat'),
  ('Işığın hızı, ışığı yayan kaynağın kütlesine bağlıdır.','Deneyde kaynağın kütlesi hiç incelenmediği hâlde bu sonuca varmış.','bilgi')],
 sira=['Işığın yayılması için esir adı verilen bir ortam gereklidir.','Işığın hızı, kaynağın hızına eklenerek ölçülür.','Işığın hızı, Dünya’nın hareket yönünde diğer doğrultudan büyüktür.','Işığın hızı, ışığı yayan kaynağın kütlesine bağlıdır.','Işığın hızı, Dünya’nın hareketinden ve yayılma doğrultusundan bağımsızdır.'],
 istenen='Deney sonucunun desteklediği yargı.',ip=['Saçak kayması olmaması, iki kolda ışığın hızı hakkında ne söyler?'],
 bilgi=[B('Girişim ve yol farkı','İki ışın farklı sürelerde dönerse girişim deseni kayar; süreler eşitse desen değişmez. Örnek: bir koldaki ışının dönüş süresi diğerinden farklı olsaydı ekrandaki parlak saçaklar yer değiştirirdi')],
 puf='Michelson–Morley’de kayma olmaması, ışık hızının doğrultudan ve gözlemcinin hareketinden bağımsız olduğunu gösterir.',sekil=SK)

# ---- 04 orta · A–B yolculuğu öncüllü (şekil) ----
b4=Fr(4,5); g4=gam(b4); assert g4==Fr(5,3)
SK=tk(f1([ground(-.3,7.2),'\\fill (.5,0) circle (2.2pt);\\node[below] at (.5,0) {A};\\fill (6.2,0) circle (2.2pt);\\node[below] at (6.2,0) {B};',
  dim((.5,-.7),(6.2,-.7),'$d$','below'),ship(1.5,1.3,'yolcu'),V((1.5,1.8),(2.8,1.8),'$0{,}8c$','above',AK),
  person(3.5,0,'Yer gözlemcisi')]))
onc('0004','D','A ve B istasyonları birbirine göre durgun olup aralarındaki uzaklık d’dir. Bir uzay aracı A’dan B’ye yere göre sabit 0,8c büyüklüğündeki hızla gidiyor. A’dan ayrılma ve B’ye varma olaylarının arasındaki süreyi hem araçtaki yolcu hem de A ve B’ye göre durgun olan yer gözlemcisi ölçüyor.',
 [('Yolcu, yolculuk süresini yer gözlemcisinden daha uzun ölçer.',False,'Yolcu için iki olay aynı yerde (aracın içinde) gerçekleşir; yolculuk süresini yer gözlemcisinden kısa ölçer.','I numaralı yargıda hareketli gözlemcinin süresinin genişlediğini düşünmüş.'),
  ('Yolcu, A–B uzaklığını yer gözlemcisinden daha kısa ölçer.',True,'A–B uzaklığı yer gözlemcisine göre durgundur ve onun için en büyüktür; yolcuya göre hareket doğrultusunda kısalır.','II numaralı yargıda uzaklığın tüm gözlemciler için aynı ölçüldüğünü sanmış.'),
  ('Olaylar arasındaki süreyi en kısa ölçen gözlemci yolcudur.',True,'İki olay yolcunun bulunduğu yerde gerçekleştiğinden yolcu özel zaman aralığını, yani en kısa süreyi ölçer.','III numaralı yargıda en kısa süreyi ölçenin yer gözlemcisi olduğunu sanmış.')],
 ['İki olayın hangi gözlemciye göre aynı yerde gerçekleştiğine bak.'],
 [B('Özel zaman aralığı','İki olayın aynı yerde gerçekleştiği gözlemcinin ölçtüğü süre en kısadır; diğer gözlemciler daha uzun ölçer. Örnek: uçan bir araçtaki yolcunun koltuğunda geçen iki olay için yolcunun ölçtüğü süre, yerdeki gözlemcininkinden kısadır')],
 'Olayların aynı yerde olduğu gözlemci en kısa süreyi, uzunluğun durgun olduğu gözlemci en büyük uzunluğu ölçer.','Doğru olan yargılar.','gr-zaman','Zaman genişlemesi','orta','Zaman Genişlemesi','Zaman genişlemesi ve boy kısalmasını iki gözlemcinin ölçümleri üzerinde değerlendirir.','K-AFGR-03 (A–B yolculuğu) · iki gözlemci','öncüllü',sekil=SK)

# ---- 05 orta · iki çubuk öncüllü (şekil) ----
SK=tk(f1([ship(1.6,.9,'',w=3.0,h=.6),'\\draw[ultra thick,vurgu] (.4,1.5) -- (1.9,1.5);\\node[above] at (1.15,1.5) {K};','\\draw[ultra thick,vurgu] (2.4,1.25) -- (2.4,2.6);\\node[right] at (2.4,1.9) {L};',
  V((3.2,.9),(4.6,.9),'$0{,}8c$','above',AK),ground(-.3,5.4,-.4),person(4.6,-.4,'Yer\\\\gözlemcisi')]))
onc('0005','A','Özdeş K ve L çubukları, yere göre sabit hızla hareket eden bir uzay aracına sabitlenmiştir. K çubuğu hareket doğrultusuna paralel, L çubuğu ise bu doğrultuya diktir. Araçtaki gözlemciye göre iki çubuğun boyu eşittir; aracın yere göre hızı 0,8c’dir. Yer gözlemcisi ile araçtaki gözlemci çubukların boylarını ölçüyor.',
 [('Yer gözlemcisi, K çubuğunun boyunu araçtaki gözlemciden daha kısa ölçer.',True,'K çubuğu yer gözlemcisine göre hareket doğrultusundadır; boyu bu doğrultuda kısalır.','I numaralı yargıda kısalmanın hareket doğrultusunda olmadığını sanmış.'),
  ('Yer gözlemcisi, L çubuğunun boyunu araçtaki gözlemciden daha kısa ölçer.',False,'L çubuğu hareket doğrultusuna diktir; dik boyutlar değişmez, yer gözlemcisi L’yi araçtaki gözlemciyle aynı ölçer.','II numaralı yargıda dik boyutun da kısaldığını sanmış.'),
  ('Araçtaki gözlemci, K çubuğunun boyunu L çubuğunun boyundan daha kısa ölçer.',False,'Çubuklar araçtaki gözlemciye göre durgundur; ikisini de durgun boylarıyla, yani eşit ölçer.','III numaralı yargıda araçtaki gözlemcinin de kendi çubuğunu kısalmış gördüğünü sanmış.')],
 ['Her yargıda ölçümü yapan gözlemcinin çubuğa göre hareketli mi durgun mu olduğuna ve çubuğun doğrultusuna bak.'],
 [B('Boy kısalması','Bir cismin boyu, yalnız cisme göre hareketli gözlemci tarafından ve yalnız hareket doğrultusunda kısa ölçülür; cisme göre durgun gözlemci durgun boyunu ölçer. Örnek: yere göre hareket eden bir levhanın hareket doğrultusundaki kenarı kısalır, dik kenarı değişmez')],
 'Boy kısalması yalnız hareket doğrultusunda ve yalnız cisme göre hareketli gözlemci için geçerlidir.','Doğru olan yargılar.','gr-boy','Boy kısalması','orta','Boy Kısalması','Boy kısalmasının doğrultuya ve gözlemciye bağlılığını ayırt eder.','K-AFGR-04 (paralel ve dik çubuk) · nitel öncüllü','öncüllü',sekil=SK)

# ---- 06 orta · Michelson–Morley öncüllü ----
onc('0006','C','Michelson–Morley deneyinde Dünya’nın hareket yönündeki ve buna dik kollardan gelen ışınların oluşturduğu girişim deseninde, esir varsayımından beklenen kayma gözlenmemiştir.',
 [('Esir ortamı var olsaydı, ışığın Dünya’ya göre hızının doğrultuya bağlı olması beklenirdi.',True,'Dünya esire göre hareket ediyor olsaydı, ışığın Dünya’ya göre hızı hareket yönünde ve buna dik doğrultuda farklı ölçülürdü.','I numaralı yargıda esir varsayımının ışık hızını doğrultudan bağımsız kıldığını sanmış.'),
  ('Deney sonucu, ışığın hızının kaynağın hızına eklendiğini göstermiştir.',False,'Deneyde kaynağın hızı değiştirilmemiştir; sonuç ışık hızının doğrultudan bağımsız olduğuyla ilgilidir.','II numaralı yargıda deneyi kaynak hızıyla ilgili sanmış.'),
  ('Deney sonucu, ışık hızının gözlemciden bağımsız olduğu fikrinin ortaya atılmasına zemin hazırlamıştır.',True,'Beklenen kaymanın görülmemesi, ışık hızının gözlemcinin hareketinden bağımsız olduğu ikinci postülasının önünü açmıştır.','III numaralı yargıda deneyin kurama katkısını yok saymış.')],
 ['Deneyde neyin değiştirildiğini (kaynak mı, doğrultu mu) ve esir olsaydı neyin beklendiğini düşün.'],
 [B('Esir varsayımı','Esir, ışığın yayılması için gerekli sayılan varsayımsal bir ortamdı. Esire göre hareket eden bir gözlemci için ışığın hızının doğrultuya göre değişmesi beklenirdi. Örnek: akıntıya karşı ve akıntı yönünde yüzen yüzücünün hızı farklıdır')],
 'Deneyde beklenen kaymanın olmaması, esirin gereksizliğini ve ışık hızının değişmezliğini işaret eder.','Deneyle ilgili doğru yargılar.','gr-mm','Michelson–Morley deneyi','orta','Michelson–Morley','Michelson–Morley deneyinin beklentisini ve kurama katkısını yargılarla değerlendirir.','K-AFGR-02 (beklenti ve katkı) · nitel öncüllü','öncüllü',kok='yargılarından hangileri doğrudur?')

# ---- 07 orta · γ grafiği (grafik) ----
b7=Fr(4,5); r7=gam(b7); T0=6; Tg=T0*r7
assert r7==Fr(5,3) and Tg==10 and T0*b7==Fr(24,5) and T0*gam(Fr(3,5))==Fr(15,2) and T0*2==12 and T0/b7==Fr(15,2)
SK=tk('\\begin{axis}[width=6.4cm,height=5.6cm,axis lines=left,xlabel={$v/c$},ylabel={$\\Delta t/\\Delta t_0$},xmin=0,xmax=1,ymin=1,ymax=3,xtick={0,0.2,0.4,0.6,0.8,1},ytick={1,2,3},grid=major,grid style={gray!30},tick label style={font=\\small},label style={font=\\small},x tick label style={/pgf/number format/use comma},scaled ticks=false]\n'
  '\\addplot[vurgu,very thick,domain=0:0.95,samples=80]{1/sqrt(1-x^2)};\n\\addplot[only marks,mark=*,mark size=2pt]coordinates{(0.6,1.25)(0.8,1.66667)};\n'
  '\\draw[dashed] (axis cs:0.6,1) -- (axis cs:0.6,1.25) -- (axis cs:0,1.25);\\draw[dashed] (axis cs:0.8,1) -- (axis cs:0.8,1.66667) -- (axis cs:0,1.66667);\n'
  '\\node[font=\\small,fill=white,inner sep=1pt,anchor=south west] at (axis cs:0.01,1.25) {$5/4$};\\node[font=\\small,fill=white,inner sep=1pt,anchor=south west] at (axis cs:0.01,1.67) {$5/3$};\n\\end{axis}')
q('0007',[A('Grafikten oranı oku','v = 0,8c noktasına karşılık gelen değer eksenden okunur.','Δt/Δt₀ = 5/3'),A('Özel zamanı belirle','Araçtaki saatin ölçtüğü 6 saat, özel zaman aralığıdır.','Δt₀ = 6 saat'),A('Yer süresini hesapla','Yer gözlemcisi, araç saatindeki süreyi oran kadar uzun ölçer.','Δt = 6 × 5/3 = 10 saat')],
 tipId='gr-zaman',tip='Zaman genişlemesi',z='orta',alt='Zaman Genişlemesi',kaz='Zaman genişlemesi grafiğinden okuduğu orana göre yer gözlemcisinin ölçtüğü süreyi bulur.',
 kart='K-AFGR-03 (γ grafiği) · grafikten oran okuma',kalip='grafik',
 metin='Bir uzay aracındaki saat, yere göre sabit hızla hareket ederken ölçülen süre Δt₀ ile, aynı olayın yer gözlemcisi tarafından ölçülen süresi Δt ile gösteriliyor. Δt/Δt₀ oranının aracın hızına (v/c) bağlı değişimi şekildeki grafikte verilmiştir. Araç yere göre 0,8c büyüklüğündeki hızla gidiyor.\nBuna göre, araçtaki saat 6 saatlik süre ölçtüğünde yer gözlemcisi kaç saatlik süre ölçer?',
 dogru=Tg,yan=[(Fr(24,5),'Oranı kullanmak yerine hızla çarpmış: 6 × 0,8 = 4,8; hareketli saatin süresini kısalttığını sanmış.','bilgi'),(T0,'Zaman genişlemesini hiç uygulamamış; süreyi her gözlemci için aynı almış.','bilgi'),(Fr(15,2),'Grafikte 0,6c noktasındaki oranı okumuş: 6 × 5/4 = 7,5.','dikkat'),(12,'Eksendeki 2 değerini oran almış: 6 × 2 = 12.','dikkat')],
 istenen='Yer gözlemcisinin ölçtüğü süre (saat).',ip=['Grafikte yatay eksende 0,8 değerine karşılık gelen oran kaçtır?'],
 bilgi=[B('Zaman genişlemesi','Hareketli saatin ölçtüğü özel zaman Δt₀ ise, ona göre hareketli gözlemci Δt = γΔt₀ ölçer; γ ≥ 1’dir. Örnek: γ = 2 ise araçtaki 3 saatlik süre yerde 6 saat ölçülür')],
 puf='Genişleme oranı hız arttıkça büyür ve v → c iken sınırsız artar; süre her zaman uzar.',sekil=SK)

# ---- 08 orta · kütle kaybından enerji (tablo) ----
m_once,m_sonra=Fr(1000),Fr(998); dm8=(m_once-m_sonra)/1000; E8=dm8*9*10**16
assert dm8==Fr(2,1000) and E8==Fr(18,10)*10**14 and dm8*3*10**8==6*10**5 and E8/2==9*10**13 and 2*9*10**16==18*10**16 and Fr(2,10**6)*9*10**16==18*10**10
SK=tk(table('Tepkime öncesi ve sonrası',['Durum','Toplam kütle (g)'],[('Tepkimeden önce','1000'),('Tepkimeden sonra','998')],[3.2,3.0]))
q('0008',[A('Kütle farkını bul','Tepkimede kaybolan kütle, önceki ve sonraki kütlelerin farkıdır.','Δm = 1000 − 998 = 2 g'),A('Birimi çevir','Enerji joule olarak istendiğinden kütle kg olmalıdır.','Δm = 2 × 10⁻³ kg'),
  A('Enerjiyi hesapla','Kütle farkı ΔE = Δm c² kadar enerjiye karşılık gelir.','ΔE = 2 × 10⁻³ × (3 × 10⁸)² = 1,8 × 10¹⁴ J')],
 tipId='gr-kutle',tip='Kütle–enerji eşdeğerliği',z='orta',alt='Kütle–Enerji',kaz='Tepkimedeki kütle kaybından açığa çıkan enerjiyi E = mc² ile hesaplar.',
 kart='K-AFGR-05 (kütle kaybı tablosu) · gramdan jule',kalip='tablo',
 metin='Bir nükleer tepkimeye girenlerin ve ürünlerin toplam kütleleri tabloda verilmiştir. Kaybolan kütlenin tamamı enerjiye dönüşmektedir (c = 3 × 10⁸ m/s).\nBuna göre, tepkimede açığa çıkan enerji kaç joule’dür?',
 dogru='1,8 × 10¹⁴',yan=[('6 × 10⁵','Enerjiyi Δm × c olarak hesaplamış; c’nin karesini almamış.','islem'),('1,8 × 10¹¹','Gramı kilograma çevirirken 10⁻⁶ ile çarpmış: 2 × 10⁻⁶ × 9 × 10¹⁶.','islem'),('9 × 10¹³','Enerjiyi ½Δm c² almış; kinetik enerji formülüyle karıştırmış.','bilgi'),('1,8 × 10¹⁷','Gramı kilograma çevirmemiş: 2 × 9 × 10¹⁶.','dikkat')],
 sira=['6 × 10⁵','1,8 × 10¹¹','9 × 10¹³','1,8 × 10¹⁴','1,8 × 10¹⁷'],istenen='Açığa çıkan enerji (J).',ip=['Önce kaybolan kütleyi bul, sonra birimini kilograma çevir.'],
 bilgi=[B('Kütle–enerji eşdeğerliği','Δm kütle kaybına karşılık gelen enerji ΔE = Δm c²’dir; kütle kg, c m/s alınınca enerji joule olur. Örnek: 1 mg kütle, 10⁻⁶ kg olduğundan 10⁻⁶ × 9 × 10¹⁶ = 9 × 10¹⁰ J enerjiye karşılık gelir')],
 puf='E = mc² kullanırken kütleyi önce kg’a çevir ve c’yi kare al.',sekil=SK)

# ---- 09 orta · kütle-enerji nitel öncüllü ----
onc('0009','E','Durgun kütlesi m olan bir cisim, durgun hâlden ışık hızına yakın bir hıza kadar hızlandırılıyor.',
 [('Cismin toplam enerjisi, durgun enerjisinden büyük olur.',True,'Hızlanan cisme enerji verilmiştir; toplam enerji, durgun enerji mc² ile hareket enerjisinin toplamıdır, yani mc²’den büyüktür.','I numaralı yargıda hız artsa da toplam enerjinin mc²’de kaldığını sanmış.'),
  ('Cismin durgun enerjisi, hızından bağımsızdır.',True,'Durgun enerji E = mc² durgun kütleye bağlıdır ve cismin hızıyla değişmez.','II numaralı yargıda durgun enerjinin hızla arttığını sanmış.'),
  ('Sonlu miktarda enerji verilerek cismin hızı ışık hızına ulaştırılamaz.',True,'Hız c’ye yaklaştıkça hızı biraz daha artırmak için gereken enerji çok büyür; c’ye ulaşmak için sonsuz enerji gerekir.','III numaralı yargıda yeterince enerji verilirse hızın c’ye ulaşabileceğini sanmış.')],
 ['Durgun enerji ile toplam enerjiyi birbirinden ayır; hızlandırmak için verilen enerji nereye gider?'],
 [B('Durgun enerji','Durgun kütlesi m olan cismin durgun enerjisi E₀ = mc²’dir ve hızdan bağımsızdır. Hareket eden cismin toplam enerjisi E₀’dan büyüktür. Örnek: durgun kütlesi 2 kg olan cismin durgun enerjisi 2 × 9 × 10¹⁶ J’dür')],
 'Hız artsa da durgun enerji sabittir; toplam enerji artar ve ışık hızı sonlu enerjiyle aşılamaz.','Doğru olan yargılar.','gr-kutle','Kütle–enerji eşdeğerliği','orta','Kütle–Enerji','Durgun enerji, toplam enerji ve ışık hızı sınırını nitel olarak değerlendirir.','K-AFGR-05 (durgun ve toplam enerji) · nitel öncüllü','öncüllü')

# ---- 10 orta · platform uzunluğu (şekil) ----
L10=150; g10=gam(Fr(4,5)); Lp=Fr(L10)/g10
assert g10==Fr(5,3) and Lp==90 and L10*Fr(4,5)==120 and Fr(L10)/Fr(4,5)==Fr(375,2) and L10*g10==250
SK=tk(f1([ground(-.3,7.2),'\\draw[ultra thick,vurgu] (.6,0) -- (6.0,0);',dim((.6,-.5),(6.0,-.5),'150 m','below'),ship(1.6,1.3,'yolcu'),V((1.6,1.8),(3.0,1.8),'$0{,}8c$','above',AK),
  '\\node[above] at (4.8,.1) {platform};',person(6.8,0,'Yer\\\\gözlemcisi')]))
q('0010',[A('Öz uzunluğu belirle','Platform yer gözlemcisine göre durgundur; 150 m onun durgun (öz) uzunluğudur.','L₀ = 150 m'),A('Kısalmayı uygula','Platforma göre hareketli olan yolcu, hareket doğrultusundaki uzunluğu 1/γ katı ölçer.','L = L₀/γ = 150 ÷ (5/3)'),A('Hesapla','Bölme işlemi yapılır.','L = 150 × 3/5 = 90 m')],
 tipId='gr-boy',tip='Boy kısalması',z='orta',alt='Boy Kısalması',kaz='Hareketli gözlemcinin ölçtüğü uzunluğu öz uzunluk ve γ ile bulur.',
 kart='K-AFGR-04 (platform ve araç) · hareketli gözlemcinin ölçümü',kalip='şekilli',
 metin='Yere göre durgun bir platformun uzunluğu, yerdeki gözlemci tarafından 150 m ölçülüyor. Bir uzay aracı platformun uzunluğu doğrultusunda yere göre sabit 0,8c hızıyla geçiyor (şekil). 0,8c hızı için γ = 5/3’tür ve hareket doğrultusundaki uzunluklar, öz uzunluğun 1/γ katı olarak ölçülür.\nBuna göre, araçtaki yolcunun ölçtüğü platform uzunluğu kaç m’dir?',
 dogru=Lp,yan=[(120,'Uzunluğu hız oranıyla çarpmış: 150 × 0,8 = 120.','bilgi'),(150,'Boy kısalmasını uygulamamış; platformu yerdeki gibi ölçmüş.','bilgi'),(Fr(375,2),'Uzunluğu hız oranına bölmüş: 150 ÷ 0,8 = 187,5.','islem'),(250,'Kısalma yerine γ ile çarpmış: 150 × 5/3 = 250.','dikkat')],
 istenen='Yolcunun ölçtüğü platform uzunluğu (m).',ip=['Platformun öz uzunluğunu hangi gözlemci ölçer?'],
 bilgi=[B('Öz uzunluk','Bir cisme göre durgun gözlemcinin ölçtüğü uzunluk öz uzunluk L₀’dır ve en büyüktür; cisme göre hareketli gözlemci hareket doğrultusunda L = L₀/γ ölçer. Örnek: γ = 2 ise 10 m’lik bir çubuk hareketli gözlemciye 5 m görünür')],
 puf='Öz uzunluğu çubuğa göre durgun gözlemci ölçer; hareketli gözlemci daha kısa ölçer.',sekil=SK)

# ---- 11 orta · üç araç (şekil) ----
sc=3.0; vs=[Fr(3,10),Fr(6,10),Fr(9,10)]
gs=[1/(1-v*v) for v in vs]
assert gs[0]<gs[1]<gs[2]
SK=tk(f1([ship(1.2,2.2,'K',w=1.6),V((2.0,2.2),(2.0+vs[0]*sc,2.2),'$0{,}3c$','above',AK),ship(1.2,1.1,'L',w=1.6),V((2.0,1.1),(2.0+vs[1]*sc,1.1),'$0{,}6c$','above',AK),ship(1.2,0,'M',w=1.6),V((2.0,0),(2.0+vs[2]*sc,0),'$0{,}9c$','above',AK)]))
q('0011',[A('Özel zamanı belirle','Her araçtaki saat 1 saat ölçer; bu, özel zaman aralığıdır ve hepsi için aynıdır.','Δt₀ = 1 saat (K, L, M)'),A('Hıza göre karşılaştır','Hız arttıkça γ büyür; yer gözlemcisinin ölçtüğü Δt = γΔt₀ uzar.','γ_K < γ_L < γ_M'),A('Sırala','Δt₀ eşit olduğundan süreler γ ile aynı sırada olur.','t_K < t_L < t_M')],
 tipId='gr-zaman',tip='Zaman genişlemesi',z='orta',alt='Zaman Genişlemesi',kaz='Farklı hızlardaki hareketli saatler için yer gözlemcisinin ölçtüğü süreleri hıza göre sıralar.',
 kart='K-AFGR-03 (üç araç) · hıza göre süre sıralaması',kalip='şekilli',
 metin='Özdeş saatler taşıyan K, L ve M uzay araçları, yere göre sırasıyla 0,3c, 0,6c ve 0,9c büyüklüğündeki sabit hızlarla aynı yönde gidiyor (şekil). Her araçtaki gözlemci kendi saatinde 1 saatlik süre ölçtüğünde, yerdeki gözlemci bu süreyi kendi saatiyle ölçüyor. Yer gözlemcisinin ölçtüğü süreler t_K, t_L ve t_M’dir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru='t_K < t_L < t_M',yan=[('t_M < t_L < t_K','Hız arttıkça yerde ölçülen sürenin kısaldığını sanmış.','bilgi'),('t_K = t_L = t_M = 1 saat','Zaman genişlemesini hiç uygulamamış; süreyi gözlemciden bağımsız almış.','bilgi'),('t_K = t_L = t_M > 1 saat','Genişlemenin var olduğunu bilmiş ama hıza bağlı olmadığını düşünmüş.','bilgi'),('t_K = t_L = t_M < 1 saat','Hareketli saat için yerde daha kısa süre ölçüleceğini sanmış.','bilgi')],
 sira=['t_K < t_L < t_M','t_M < t_L < t_K','t_K = t_L = t_M = 1 saat','t_K = t_L = t_M > 1 saat','t_K = t_L = t_M < 1 saat'],istenen='Yer gözlemcisinin ölçtüğü sürelerin sıralaması.',ip=['Hız arttıkça hareketli saat için yerde ölçülen süre nasıl değişir?'],
 bilgi=[B('Hıza bağlılık','Zaman genişlemesi çarpanı γ = 1/√(1 − v²/c²) hız arttıkça büyür ve v = 0’da 1’dir. Örnek: 0,6c’de γ = 1,25, 0,8c’de γ = 5/3’tür; hız büyüdükçe genişleme artar')],
 puf='Aynı özel zaman için hız ne kadar büyükse yerde ölçülen süre o kadar uzundur.',sekil=SK)
# not: ilk sıra doğru şık A olsun diye sira başında

# ---- 12 orta · birinci postüla (şekilsiz) ----
q('0012',[A('Birinci postülayı hatırla','Fizik yasaları tüm eylemsiz referans sistemlerinde aynıdır.','Sabit hızlı vagon eylemsiz sistemdir'),A('Vagona uygula','Kapalı vagondaki yolcu, yaptığı deneylerle sabit hızla hareket ettiğini anlayamaz.','Deney sonuçları durgun laboratuvardakiyle aynı'),A('Şıkları ele','Yalnız sabit hız sonucu vagonu mutlak hareketli kılan bir deney yoktur.','Doğru: hareket deneyle belirlenemez')],
 tipId='gr-postula',tip='Postülalar ve ışık hızı',z='orta',alt='Postülalar',kaz='Birinci postülayı eylemsiz referans sistemlerindeki deney sonuçlarına uygular.',
 kart='K-AFGR-01 (birinci postüla) · kapalı vagon',kalip='yeni nesil',
 metin='Sabit hızla düz raylarda giden kapalı bir vagonun içindeki yolcu, elindeki mekanik düzeneklerle çeşitli deneyler yapıyor. Aynı deneyleri yerdeki özdeş bir laboratuvarda duran bir öğrenci de yapıyor. Sürtünmeler ve titreşimler önemsizdir.\nBuna göre, özel görelilik kuramının birinci postülasına göre aşağıdakilerden hangisi doğrudur?',
 dogru='Yolcu, vagon içinde yaptığı mekanik deneylerle vagonun sabit hızla gittiğini belirleyemez.',
 yan=[('Vagonun hızı arttıkça yolcunun ölçtüğü serbest düşme ivmesi değişir.','Hız arttıkça fizik yasalarının değiştiğini sanmış; oysa yasalar eylemsiz sistemlerde aynıdır.','bilgi'),
  ('Yolcu ve öğrenci için fizik yasaları, vagon hareketli olduğu için farklıdır.','Hareketli sistem için yasaların farklı olduğunu düşünmüş; birinci postüla bunu reddeder.','bilgi'),
  ('Yolcu, aynı deneyleri tekrarlayarak vagonun mutlak hızını bulabilir.','Eylemsiz sistemde mutlak hızın deneyle bulunabileceğini sanmış.','bilgi'),
  ('Öğrenci, deney sonuçlarından vagonun mutlak durgun olmadığını kanıtlayabilir.','Yerdeki sistemi mutlak durgun kabul etmiş.','bilgi')],
 sira=['Vagonun hızı arttıkça yolcunun ölçtüğü serbest düşme ivmesi değişir.','Yolcu ve öğrenci için fizik yasaları, vagon hareketli olduğu için farklıdır.','Yolcu, aynı deneyleri tekrarlayarak vagonun mutlak hızını bulabilir.','Öğrenci, deney sonuçlarından vagonun mutlak durgun olmadığını kanıtlayabilir.','Yolcu, vagon içinde yaptığı mekanik deneylerle vagonun sabit hızla gittiğini belirleyemez.'],
 istenen='Birinci postülaya uygun yargı.',ip=['Sabit hızla giden bir sistem ile durgun bir sistemde yapılan deneyler arasında fark var mıdır?'],
 bilgi=[B('Eylemsiz referans sistemi','Durgun ya da sabit hızla giden sistemler eylemsizdir; birinci postüla, fizik yasalarının bu sistemlerin hepsinde aynı olduğunu söyler. Örnek: sabit hızlı bir gemide kapalı kamarada bırakılan cisim, limandaki odada olduğu gibi düşer')],
 puf='Sabit hızlı kapalı bir sistemde hareket, fizik deneyleriyle belirlenemez.')

# ---- 13 zor · karşılıklı zaman genişlemesi (şekil) ----
SK=tk(f1(['\\node[font=\\small\\bfseries,anchor=west] at (-.2,2.9) {K gözlemcisine göre};',ship(.9,2.1,'K',w=1.4),ship(3.4,2.1,'L',w=1.4),V((4.2,2.1),(5.7,2.1),'$0{,}6c$','above',AK),
  '\\draw[dashed,gray] (-.2,1.35) -- (6.2,1.35);',
  '\\node[font=\\small\\bfseries,anchor=west] at (-.2,1.0) {L gözlemcisine göre};',ship(.9,.2,'L',w=1.4),ship(5.2,.2,'K',w=1.4,sol=True),V((4.4,.2),(2.9,.2),'$0{,}6c$','above',AK)]))
onc('0013','B','K ve L uzay araçları, uzayda doğrusal doğrultuda birbirinin yanından, birbirine göre sabit 0,6c büyüklüğündeki hızla geçiyor. Her araçta özdeş birer saat ve bir gözlemci vardır; iki araç da eylemsiz referans sistemidir (şekilde her gözlemcinin bakış açısı gösterilmiştir).',
 [('K’deki gözlemci, L’deki saatin kendi saatine göre yavaş işlediğini ölçer.',True,'K’ye göre L hareketlidir; hareketli saat K’deki gözlemciye yavaş işliyor görünür.','I numaralı yargıda yavaş işleyen saatin her zaman diğer araçta olmadığını göz ardı etmiş.'),
  ('L’deki gözlemci, K’deki saatin kendi saatine göre yavaş işlediğini ölçer.',True,'L’ye göre K hareketlidir; durum simetriktir ve L’deki gözlemci de K’nin saatini yavaş ölçer.','II numaralı yargıda yalnız bir saatin yavaşladığını düşünmüş.'),
  ('Bu iki ölçüm birbiriyle çeliştiğinden ölçümlerden biri yanlıştır.',False,'Her gözlemci diğerinin saatini kendi sistemine göre ölçer; iki ölçüm farklı referans sistemlerine aittir ve çelişmez.','III numaralı yargıda iki ölçümün aynı sistemde yapıldığını sanmış.')],
 ['Her gözlemciye göre öbür aracın hareketli olduğunu ve eylemsiz sistemlerin eşdeğerliğini hatırla.'],
 [B('Karşılıklılık','Birbirine göre sabit hızla hareket eden iki eylemsiz gözlemciden hiçbiri ayrıcalıklı değildir; her biri, diğerinin saatinin kendi saatine göre yavaş işlediğini ölçer. Örnek: tren ve istasyon gözlemcisi birbirinin saatini yavaş görür')],
 'Eylemsiz sistemler eşdeğerdir: zaman genişlemesi her iki yönde de geçerlidir.','Doğru olan yargılar.','gr-zaman','Zaman genişlemesi','zor','Zaman Genişlemesi','Eylemsiz iki gözlemcinin birbirinin saatini yavaş ölçtüğünü ve bunun çelişki olmadığını bulur.','K-AFGR-08 (karşılıklı genişleme) · iki bakış açısı','öncüllü',sekil=SK)

# ---- 14 zor · gezegen yolculuğu (şekil) ----
d14=15; b14=Fr(3,5); g14=gam(b14); t_yer=Fr(d14)/b14; t0=t_yer/g14; dp=Fr(d14)/g14
assert t_yer==25 and t0==20 and dp==12 and dp/b14==20 and t_yer*g14==Fr(125,4) and Fr(d14)==15 and t_yer*b14==15
SK=tk(f1(['\\fill[blue!25] (.2,0) circle (.45);\\node at (.2,0) {Dünya};','\\fill[orange!35] (6.6,0) circle (.35);\\node at (6.6,0) {G};','\\node[below] at (6.6,-.45) {gezegen};',
  dim((.2,-1.0),(6.6,-1.0),'15 ışık-saati','below'),ship(1.8,.9,'araç',w=1.5),V((1.8,1.35),(3.0,1.35),'$0{,}6c$','above',AK)]))
q('0014',[A('Yer gözlemcisinin süresi','Dünya ve gezegen birbirine göre durgun; yolculuk süresi uzaklık bölü hızdır.','t = 15 ÷ 0,6 = 25 saat'),A('Özel zamanı bul','Araçtaki yolcu, iki olayı da kendi yerinde ölçer; özel zaman daha kısadır.','t₀ = t ÷ γ = 25 ÷ 1,25 = 20 saat'),
  A('Kontrol et','Yolcuya göre uzaklık kısalmıştır: 15 ÷ 1,25 = 12 ışık-saati; bu uzaklık 0,6c ile alınır.','12 ÷ 0,6 = 20 saat')],
 tipId='gr-birlesik',tip='Zaman genişlemesi ve boy kısalması birlikte',z='zor',alt='Birlikte Uygulama',kaz='Aynı yolculuğu yer gözlemcisi ve araçtaki yolcu açısından zaman genişlemesi ve boy kısalmasıyla tutarlı biçimde hesaplar.',
 kart='K-AFGR-06 (gezegen yolculuğu) · iki bakış açısı',kalip='şekilli',
 metin='Birbirine göre durgun Dünya ile bir gezegen arasındaki uzaklık, 15 ışık-saatidir (ışığın 15 saatte aldığı yol). Bir uzay aracı Dünya’dan gezegene yere göre sabit 0,6c büyüklüğündeki hızla gidiyor. 0,6c hızı için γ = 5/4’tür.\nBuna göre, yolculuk süresi araçtaki yolcu tarafından kendi saatiyle kaç saat ölçülür?',
 dogru=t0,yan=[(12,'Yolcunun ölçtüğü kısalmış uzaklığı (12 ışık-saati) süre olarak okumuş.','dikkat'),(15,'Uzaklığı ışık hızıyla bölmüş: 15 ÷ 1 = 15 saat; aracın hızı 0,6c olduğunu unutmuş.','dikkat'),(25,'Yer gözlemcisinin ölçtüğü süreyi (15 ÷ 0,6) yolcu için de almış.','bilgi'),(Fr(125,4),'Yer süresini bir de γ ile çarpmış: 25 × 5/4 = 31,25; genişlemeyi yanlış gözlemciye uygulamış.','bilgi')],
 istenen='Yolcunun kendi saatiyle ölçtüğü yolculuk süresi (saat).',ip=['Önce yer gözlemcisinin ölçtüğü süreyi bul; sonra iki olayın hangi gözlemci için aynı yerde olduğunu belirle.'],
 bilgi=[B('Özel zaman ve kısalan uzaklık','Hareketli gözlemci hem süreyi hem uzaklığı daha kısa ölçer, ama iki ölçüm birbiriyle tutarlıdır. Örnek: yer gözlemcisi 10 saat ve 8 ışık-saati ölçen bir yolculukta γ = 2 ise hareketli gözlemci 5 saat ve 4 ışık-saati ölçer')],
 puf='Uzaklık yerde, süre araçta ölçülürken γ ile bölme gerekir; ışık-saatinde hız c’nin kesri olarak alınır.',sekil=SK)

# ---- 15 zor · müon (şekil) ----
b15=Fr(3,5); g15=gam(b15); tau0=2; tau=tau0*g15; c15=3*10**8; yol=b15*c15*tau*Fr(1,10**6)
assert tau==Fr(5,2) and yol==450 and b15*c15*tau0*Fr(1,10**6)==360
assert b15*c15*tau0*Fr(1,10**6)==360 and Fr(360)/g15==288 and c15*tau0*Fr(1,10**6)==600 and c15*tau*Fr(1,10**6)==750
SK=tk(f1(['\\fill[blue!8] (-.2,.6) rectangle (3.6,3.6);\\node[font=\\small,anchor=west] at (-.1,3.3) {atmosfer};','\\draw[thick] (-.2,.6) -- (3.6,.6);\\node[font=\\small] at (1.7,.35) {yer};',
  '\\fill (1.7,2.9) circle (2.5pt);\\node[right,align=left] at (1.85,2.9) {müon\\\\oluşumu};',V((1.7,2.8),(1.7,.9),'','right'),'\\node[right] at (1.9,1.8) {$0{,}6c$};',
  '\\node[right,align=left,font=\\small] at (4.0,1.9) {durgun ömür:\\\\$2\\,\\mu$s};','\\fill (1.7,.62) circle (2.5pt);\\node[right,font=\\small] at (1.85,.95) {bozunma};']))
q('0015',[A('Genişlemiş ömrü bul','Yerdeki gözlemciye göre müon hareketlidir; ömrü γ kat uzar.','t = γ t₀ = 5/4 × 2 = 2,5 µs'),A('Hızı yaz','Hız ışık hızının 0,6 katıdır.','v = 0,6 × 3 × 10⁸ = 1,8 × 10⁸ m/s'),A('Yolu hesapla','Yol, yere göre hız ile yerde ölçülen sürenin çarpımıdır.','x = 1,8 × 10⁸ × 2,5 × 10⁻⁶ = 450 m')],
 tipId='gr-birlesik',tip='Zaman genişlemesi ve boy kısalması birlikte',z='zor',alt='Birlikte Uygulama',kaz='Müonun yerde ölçülen ömrünü zaman genişlemesiyle bulup aldığı yolu hesaplar.',
 kart='K-AFGR-06 (müon) · genişlemiş ömürle yol',kalip='şekilli',
 metin='Kozmik ışınların atmosferin üst katmanlarında oluşturduğu bir müon, yere doğru yere göre sabit 0,6c büyüklüğündeki hızla ilerliyor. Müonun kendisine göre ölçülen ömrü (durgun ömrü) 2 µs’dir. 0,6c hızı için γ = 5/4’tür ve c = 3 × 10⁸ m/s alınacaktır. Yerdeki gözlemci müonun oluşumundan bozunmasına kadar aldığı yolu ölçüyor.\nBuna göre, müonun yere göre aldığı yol kaç m’dir?',
 dogru=yol,yan=[(288,'Ömrü γ ile bölerek kısaltmış: 0,6c × 2 µs ÷ 1,25.','bilgi'),(360,'Zaman genişlemesini uygulamamış; yolu durgun ömürle hesaplamış: 1,8 × 10⁸ × 2 × 10⁻⁶.','bilgi'),(600,'Hız yerine ışık hızını almış ve genişlemeyi unutmuş: 3 × 10⁸ × 2 × 10⁻⁶.','dikkat'),(750,'Genişlemiş ömürle ışık hızını çarpmış: 3 × 10⁸ × 2,5 × 10⁻⁶; müonun hızı 0,6c’dir.','dikkat')],
 istenen='Müonun yere göre aldığı yol (m).',ip=['Yerdeki gözlemciye göre müonun ömrü durgun ömründen büyük mü, küçük mü?'],
 bilgi=[B('Hareketli parçacığın ömrü','Parçacığın kendi ölçtüğü ömür özel zamandır; yerdeki gözlemci ömrü γ kat uzun ölçer ve yolu bu süreyle hesaplar. Örnek: ömrü 1 µs olan bir parçacık için γ = 3 ise yerde 3 µs ölçülür')],
 puf='Yerdeki yolu hesaplarken yerde ölçülen (genişlemiş) süreyi ve yere göre hızı kullan.',sekil=SK)

# ---- 16 orta · v–t grafiği öncüllü (grafik) ----
SK=tk('\\begin{axis}[width=6.2cm,height=5.4cm,axis lines=left,xlabel={$t$},ylabel={$v$},xmin=0,xmax=3,ymin=0,ymax=1.5,xtick=\\empty,ytick={0,1},yticklabels={0,$c$},grid=major,grid style={gray!30},tick label style={font=\\small},label style={font=\\small}]\n'
  '\\addplot[blue!65!black,very thick,domain=0:2.9]{0.5*x};\n\\addplot[vurgu,very thick,domain=0:2.9,samples=60]{tanh(0.5*x)};\n\\addplot[dashed,gray,thick,domain=0:3]{1};\n'
  '\\node[font=\\small\\bfseries,blue!65!black,fill=white,inner sep=1pt] at (axis cs:2.55,1.38) {K};\\node[font=\\small\\bfseries,vurgu,fill=white,inner sep=1pt] at (axis cs:2.6,0.72) {L};\n\\end{axis}')
onc('0016','A','Durgun hâlden hızlandırılan kütleli bir cismin hız–zaman grafiği için K ve L eğrileri önerilmiştir (c: ışığın boşluktaki hızı).',
 [('K eğrisi, özel görelilik kuramıyla uyumludur.',False,'K eğrisinde hız zamanla doğrusal artarak c’yi aşıyor; kütleli bir cismin hızı c’ye ulaşamaz, K bu nedenle kuramla uyumlu değildir.','I numaralı yargıda hızın sınırsız artabileceğini kabul etmiş.'),
  ('L eğrisine göre cisim sonlu bir sürede ışık hızına ulaşır.',False,'L eğrisi c çizgisine sürekli yaklaşır ama hiçbir sonlu anda ona ulaşmaz.','II numaralı yargıda eğrinin c çizgisine değdiğini sanmış.'),
  ('Özel görelilik kuramıyla uyumlu olan eğri L’dir.',True,'L eğrisi başlangıçta hızı artırır, c’ye yaklaştıkça artışı yavaşlatır ve c’yi aşmaz; kütleli cisimler için kuramın öngördüğü budur.','III numaralı yargıda kuramla uyumlu olanın doğrusal eğri olduğunu sanmış.')],
 ['Kütleli cisim için hızın alabileceği en büyük değeri ve eğrilerin bu değere göre davranışını incele.'],
 [B('Işık hızı sınırı','Kütleli bir cismin hızı ışık hızına yaklaşabilir ama ulaşamaz; çünkü c’ye yaklaştıkça hızı artırmak için gereken enerji hızla büyür. Örnek: hızı 0,9c olan bir cismin hızını 0,99c’ye çıkarmak, 0,1c’den 0,2c’ye çıkarmaktan çok daha fazla enerji ister')],
 'Kütleli cismin v–t eğrisi c çizgisine yaklaşır, onu kesmez.','Doğru olan yargılar.','gr-isik-siniri','Kütleli cisim ve ışık hızı sınırı','orta','Işık Hızı Sınırı','Kütleli cismin hızının ışık hızına ulaşamayacağını grafikte yorumlar.','K-AFGR-07 (v–t grafiği) · Newton ve görelilik eğrileri','öncüllü',sekil=SK)

# ---- 17 orta · durgun enerji tablosu (tablo) ----
mK,mL,mM=2,3,1; assert mL>mK>mM
SK=tk(table('Cisimlerin özellikleri',['Cisim','Durgun kütle (kg)','Yere göre hız'],[('K','2','$0{,}1c$'),('L','3','0'),('M','1','$0{,}9c$')],[1.6,3.6,3.0]))
q('0017',[A('Durgun enerjiyi yaz','Durgun enerji yalnız durgun kütleye bağlıdır.','E₀ = mc²'),A('Kütleleri karşılaştır','Hız bu enerjiyi değiştirmez; tablodaki kütleler karşılaştırılır.','m_L = 3 kg > m_K = 2 kg > m_M = 1 kg'),A('Sırala','Kütle büyüdükçe durgun enerji büyür.','E_L > E_K > E_M')],
 tipId='gr-kutle',tip='Kütle–enerji eşdeğerliği',z='orta',alt='Kütle–Enerji',kaz='Durgun enerjinin yalnız durgun kütleye bağlı olduğunu kullanarak cisimleri sıralar.',
 kart='K-AFGR-05 (durgun enerji tablosu) · hızı dikkate almama',kalip='tablo',
 metin='Tabloda K, L ve M cisimlerinin durgun kütleleri ile yere göre hızları verilmiştir. Cisimlerin durgun enerjileri E_K, E_L ve E_M’dir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru='E_L > E_K > E_M',yan=[('E_M > E_K > E_L','Durgun enerjinin hızla arttığını düşünmüş; hızı en büyük olanı en büyük almış.','bilgi'),('E_K > E_L > E_M','Durgun kütlesi en büyük olan L’nin hareketsiz olması nedeniyle enerjisinin düşük olduğunu sanmış.','bilgi'),('E_L > E_M > E_K','K’nin hızını küçük bulup enerjisini en küçük almış; hızı hesaba katmış.','bilgi'),('E_K = E_L = E_M','Durgun enerjinin kütleden bağımsız, tüm cisimler için aynı olduğunu sanmış.','bilgi')],
 sira=['E_M > E_K > E_L','E_L > E_K > E_M','E_K > E_L > E_M','E_L > E_M > E_K','E_K = E_L = E_M'],istenen='Durgun enerjilerin sıralaması.',ip=['Durgun enerji hangi nicelikle belirlenir: kütle mi, hız mı?'],
 bilgi=[B('Durgun enerji','Cismin durgun enerjisi E₀ = mc²’dir; yalnız durgun kütleye bağlıdır, hızdan bağımsızdır. Örnek: 4 kg ve 5 kg durgun kütleli iki cisimden 5 kg’lık olanın durgun enerjisi daha büyüktür, hızları ne olursa olsun')],
 puf='Durgun enerjiyi karşılaştırırken yalnız durgun kütleye bak; hızı yok say.',sekil=SK)

# ---- 18 zor · silindirlerin hacmi (şekil) ----
g18=gam(Fr(4,5)); V0=Fr(1); VK=V0/g18; VL=V0/g18
assert g18==Fr(5,3) and VK==VL==Fr(3,5) and VK<V0
def cyl_h(x,y,lab): return '\\draw[thick,fill=gray!20] (%.2f,%.2f) rectangle (%.2f,%.2f);\\draw[thick,fill=gray!35] (%.2f,%.2f) ellipse (.15 and .38);\\node at (%.2f,%.2f) {%s};'%(x-.8,y-.38,x+.8,y+.38,x+.8,y,x-.05,y,lab)
def cyl_v(x,y,lab): return '\\draw[thick,fill=gray!20] (%.2f,%.2f) rectangle (%.2f,%.2f);\\draw[thick,fill=gray!35] (%.2f,%.2f) ellipse (.38 and .15);\\node at (%.2f,%.2f) {%s};'%(x-.38,y-.7,x+.38,y+.7,x,y+.7,x,y-.1,lab)
SK=tk(f1([cyl_h(1.1,2.5,'K'),V((2.3,2.5),(3.7,2.5),'$0{,}8c$','above',AK),cyl_v(1.1,.5,'L'),V((2.3,.5),(3.7,.5),'$0{,}8c$','above',AK),person(5.6,0.3,'Yer\\\\gözlemcisi')]))
q('0018',[A('Kısalan doğrultuyu belirle','Hareket doğrultusundaki her uzunluk 1/γ katına iner; dik uzunluklar değişmez.','L = L₀/γ yalnız hareket doğrultusunda'),A('K için hacmi yaz','K’nin boyu hareket doğrultusundadır, kesit alanı değişmez.','V_K = V₀/γ'),
  A('L için hacmi yaz','L’nin çapı hareket doğrultusunda kısalır, yüksekliği değişmez; kesit alanı 1/γ katına iner.','V_L = V₀/γ'),A('Karşılaştır','İki hacim de aynı çarpanla azalır.','V_K = V_L < V₀')],
 tipId='gr-boy',tip='Boy kısalması',z='zor',alt='Boy Kısalması',kaz='Hareket doğrultusuna göre farklı yönelmiş cisimlerin hacimlerini boy kısalmasıyla karşılaştırır.',
 kart='K-AFGR-04 (iki silindir) · paralel ve dik yönelim',kalip='şekilli',
 metin='Durgun hâldeki hacimleri V₀ olan özdeş K ve L silindirleri, yere göre aynı büyüklükte 0,8c hızla şekildeki gibi hareket ediyor: K’nin ekseni hareket doğrultusuna paralel, L’nin ekseni ise bu doğrultuya diktir. Yerdeki gözlemci K ve L’nin hacimlerini V_K ve V_L olarak ölçüyor.\nBuna göre, V_K, V_L ve V₀ arasındaki ilişki aşağıdakilerden hangisidir?',
 dogru='V_K = V_L < V₀',yan=[('V_K < V_L = V₀','Yalnız ekseni hareket yönünde olan silindirin küçüldüğünü, dikinin değişmediğini sanmış.','bilgi'),('V_L < V_K < V₀','Dik yönelmiş silindirin daha çok küçüldüğünü düşünmüş.','bilgi'),('V_K = V_L = V₀','Boy kısalmasının hacmi etkilemediğini sanmış.','bilgi'),('V_K = V_L > V₀','Kısalma yerine uzama olduğunu düşünmüş.','bilgi')],
 sira=['V_K < V_L = V₀','V_L < V_K < V₀','V_K = V_L = V₀','V_K = V_L < V₀','V_K = V_L > V₀'],istenen='Yer gözlemcisinin ölçtüğü hacimlerin karşılaştırması.',ip=['L silindirinde hareket doğrultusu boyunca hangi boyut yer alır?'],
 bilgi=[B('Hareket doğrultusu ve hacim','Hareket doğrultusundaki her uzunluk 1/γ katına iner, dik uzunluklar değişmez; bu nedenle cismin hacmi yönelimine bakılmaksızın 1/γ katına iner. Örnek: hareket doğrultusunda 4 m olan bir küp biçimindeki cisim 2 m’ye indiğinde hacmi yarıya düşer')],
 puf='Hacim değişimi, hareket doğrultusundaki boyutun kısalmasına bağlıdır; yönelim fark etmez.',sekil=SK)

# ---- 19 zor · kütle kaybı ve güç (şekilsiz) ----
dm19=(Fr(1000)-Fr(999))/1000; E19=dm19*9*10**16; P19=9*10**7; t19=E19/P19
assert dm19==Fr(1,1000) and E19==9*10**13 and t19==10**6 and (1*9*10**16)/P19==10**9 and Fr(P19)/E19==Fr(10**-6).limit_denominator(10**9) and E19/2/P19==5*10**5 and E19==9*10**13
q('0019',[A('Kütle kaybını bul','Tepkimede kaybolan kütle girenlerle ürünlerin kütle farkıdır.','Δm = 1,000 − 0,999 = 0,001 kg'),A('Enerjiyi hesapla','Kütle kaybı ΔE = Δm c² kadar enerjiye dönüşür.','ΔE = 10⁻³ × 9 × 10¹⁶ = 9 × 10¹³ J'),A('Süreyi bul','Enerji, güç ile süre çarpımıdır; süre enerjinin güce oranıdır.','t = 9 × 10¹³ ÷ 9 × 10⁷ = 10⁶ s')],
 tipId='gr-kutle',tip='Kütle–enerji eşdeğerliği',z='zor',alt='Kütle–Enerji',kaz='Kütle kaybından enerjiyi bulup güç ve süre ilişkisiyle birleştirir.',
 kart='K-AFGR-05 (kütle kaybı ve güç) · iki adımlı enerji',kalip='hikâyeli',
 metin='Bir nükleer santralde kütlesi 1,000 kg olan yakıt, tepkimeler sonunda toplam kütlesi 0,999 kg olan ürünlere dönüşüyor. Kaybolan kütlenin tamamı enerjiye dönüşmekte ve bu enerji santralde 9 × 10⁷ W’lık sabit güçle kullanılmaktadır (c = 3 × 10⁸ m/s).\nBuna göre, bu enerji kaç saniye yeter?',
 dogru='1 × 10⁶',yan=[('1 × 10⁻⁶','Süreyi gücün enerjiye oranı olarak bulmuş: 9 × 10⁷ ÷ 9 × 10¹³.','islem'),('5 × 10⁵','Enerjiyi ½Δm c² almış: 4,5 × 10¹³ ÷ 9 × 10⁷.','bilgi'),('1 × 10⁹','Yakıtın tüm kütlesini enerjiye çevirmiş: 1 × 9 × 10¹⁶ ÷ 9 × 10⁷.','dikkat'),('9 × 10¹³','Enerjiyi süre sanıp güce bölmeden yazmış.','dikkat')],
 sira=['1 × 10⁻⁶','5 × 10⁵','1 × 10⁶','1 × 10⁹','9 × 10¹³'],istenen='Enerjinin yettiği süre (s).',ip=['Önce hangi kütlenin enerjiye dönüştüğünü belirle.'],
 bilgi=[B('Güç ve enerji','Güç, birim zamanda kullanılan enerjidir: P = E/t. Süre, enerjinin güce oranıdır. Örnek: 600 J’lük enerji 20 W’lık güçle 30 s’de tüketilir')],
 puf='Önce yalnız kaybolan kütleyi enerjiye çevir, sonra güce böl.')

# ---- 20 zor · ışık saatleri öncüllü (şekil) ----
SK=tk(f1([ship(2.2,1.1,'',w=4.4,h=2.3),
  '\\draw[ultra thick] (.7,.55) -- (1.4,.55);\\draw[ultra thick] (.7,1.65) -- (1.4,1.65);\\draw[vurgu,<->,thick] (1.05,.6) -- (1.05,1.6);\\node at (1.05,2.0) {K};',
  '\\draw[ultra thick] (2.7,1.6) -- (2.7,.6);\\draw[ultra thick] (3.7,1.6) -- (3.7,.6);\\draw[vurgu,<->,thick] (2.75,1.1) -- (3.65,1.1);\\node at (3.2,2.0) {L};',
  V((4.7,1.1),(6.1,1.1),'$0{,}6c$','above',AK),person(6.9,.1,'Yer\\\\gözlemcisi')]))
onc('0020','E','Her biri iki ayna arasında gidip gelen bir ışık atımıyla çalışan özdeş K ve L ışık saatleri, yere göre sabit 0,6c hızla hareket eden bir uzay aracına yerleştirilmiştir. K saatinin aynaları hareket doğrultusuna paralel, L saatinin aynaları ise bu doğrultuya dik düzlemlerdedir; araçtaki gözlemciye göre ikisinde de aynalar arası uzaklık eşittir.',
 [('Araçtaki gözlemci, iki saatin de aynı hızda işlediğini ölçer.',True,'İki saat de araçtaki gözlemciye göre durgundur ve özdeştir; aynı hızda işler.','I numaralı yargıda saatlerin yönelimi nedeniyle farklı işlediğini sanmış.'),
  ('Yer gözlemcisi, K saatinin L saatinden daha yavaş işlediğini ölçer.',False,'Zaman genişlemesi saatin yönelimine değil, hareketine bağlıdır; yer gözlemcisi iki saati de aynı oranda yavaş ölçer.','II numaralı yargıda genişlemenin saatin yönelimine bağlı olduğunu sanmış.'),
  ('Yer gözlemcisi, iki saatin de kendi saatine göre yavaş işlediğini ölçer.',True,'İki saat de yer gözlemcisine göre hareketlidir; ikisini de kendi saatine göre yavaş ölçer.','III numaralı yargıda yalnız birinin yavaşladığını sanmış.')],
 ['Zaman genişlemesinin saatin yönelimine mi, yoksa hareketine mi bağlı olduğunu düşün.'],
 [B('Işık saati','Işık saati, iki ayna arasında gidip gelen ışık atımıyla çalışır. Hareketli gözlemciye göre her tik daha uzun sürer; bu, saatin yönelimine değil hızına bağlıdır. Örnek: yatay ya da dikey kurulmuş özdeş iki ışık saati, hareketli gözlemciye göre aynı oranda yavaşlar')],
 'Zaman genişlemesi saatin türüne ya da yönelimine değil, gözlemciye göre hareketine bağlıdır.','Doğru olan yargılar.','gr-zaman','Zaman genişlemesi','zor','Zaman Genişlemesi','Işık saatlerinin yönelimi farklı olsa da zaman genişlemesinin aynı olduğunu yargılarla değerlendirir.','K-AFGR-03 (iki ışık saati) · yönelimden bağımsızlık','öncüllü',sekil=SK)

# ---------- yaz ----------
for x in P.ANA: x['kardes']=None
SCR=os.environ.get('SCRATCH','/tmp')
P.yaz(os.path.join(GD,'gorelilik-1.json'),os.path.join(SCR,'bos-gorelilik.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik, MEB 12. sınıf özel görelilik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','afgorelilik.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
