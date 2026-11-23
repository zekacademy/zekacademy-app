"""AYT Fizik · Basit Makineler · 20 soru (kardeş yok, ipucu 1). Şekil koordinatları ve cevaplar Python'da hesaplanır; TikZ gövdesi aynı değerlerden üretilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,radians,degrees,atan2,sqrt,pi,acos,hypot
from fractions import Fraction as Fr
ONEK='makine'
P=Parti(ONEK,'Basit Makineler','afiz|Basit Makineler',ders='AYT Fizik',idon='aytfiz')
P.konu_adi='Basit Makineler'; H.KONU='Basit Makineler'
TIPK={}
KAY='ÖSYM AYT Fizik 2019, 2020, 2026 · 345 AYT Fizik Soru Bankası · Bilgi Sarmal AYT Fizik (yalnız mantık)'
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,KAY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def fig(lst): return tikz_svg(HEAD+'\n'.join(lst)+TAIL)
def hatch(xa,xb,y,up=True,n=None):
    n=n or max(3,int((xb-xa)/.22)); d=(xb-xa)/n; s=.14 if up else -.14
    return f'\\draw ({xa:.2f},{y:.2f}) -- ({xb:.2f},{y:.2f});'+''.join(f'\\draw[thin] ({xa+i*d:.2f},{y:.2f}) -- ({xa+i*d+.1:.2f},{y+s:.2f});' for i in range(n+1))

# ---------------- makara / palanga ----------------
def palanga(k,off=0.0,load='',blok='',yt=3.0,yb=1.3,r=.3,ceil=4.1,flab='F',name=''):
    sp=2*r; xs=[off+i*sp for i in range(k)]; o=[]
    ytb=yt+.55; ybar=yb-.55
    tops=[x for i,x in enumerate(xs) if i%2==0]; bots=[x for i,x in enumerate(xs) if i%2==1]
    last=xs[-1]+r
    if k%2==0: tops=tops+[last]
    else: bots=bots+[last]
    xa,xb=min(tops)-.3,max(tops)+.3
    o.append(hatch(xa,xb,ceil)); o.append(f'\\draw[thick] ({xa:.2f},{ytb:.2f}) -- ({xb:.2f},{ytb:.2f});')
    o.append(f'\\draw ({xa:.2f},{ytb:.2f}) -- ({xa:.2f},{ceil:.2f}) ({xb:.2f},{ytb:.2f}) -- ({xb:.2f},{ceil:.2f});')
    ba,bb=min(bots)-.3,max(bots)+.3
    o.append(f'\\draw[thick] ({ba:.2f},{ybar:.2f}) -- ({bb:.2f},{ybar:.2f});')
    for i,x in enumerate(xs):
        y=yt if i%2==0 else yb; yy=ytb if i%2==0 else ybar
        o.append(f'\\draw ({x:.3f},{y:.3f}) -- ({x:.3f},{yy:.3f});')
        o.append(f'\\draw[fill=white] ({x:.3f},{y:.3f}) circle ({r}); \\fill ({x:.3f},{y:.3f}) circle (1.3pt);')
    # ip
    x0=xs[0]-r
    o.append(f'\\draw[thick] ({x0:.3f},{yt-1.1:.3f}) -- ({x0:.3f},{yt:.3f}) arc[start angle=180,end angle=0,radius={r}];')
    for i in range(1,k):
        x=xs[i]-r; ya=yt if (i-1)%2==0 else yb; yb_=yt if i%2==0 else yb
        o.append(f'\\draw[thick] ({x:.3f},{ya:.3f}) -- ({x:.3f},{yb_:.3f});')
        if i%2==0: o.append(f'\\draw[thick] ({x:.3f},{yt:.3f}) arc[start angle=180,end angle=0,radius={r}];')
        else: o.append(f'\\draw[thick] ({x:.3f},{yb:.3f}) arc[start angle=180,end angle=360,radius={r}];')
    yl=yt if (k-1)%2==0 else yb; ye=ybar if (k-1)%2==0 else ytb
    o.append(f'\\draw[thick] ({last:.3f},{yl:.3f}) -- ({last:.3f},{ye:.3f});')
    o.append(f'\\draw[vurgu,very thick,{ARR}] ({x0:.3f},{yt-1.1:.3f}) -- ({x0:.3f},{yt-1.9:.3f});')
    o.append(f'\\node[vurgu,left] at ({x0-.05:.3f},{yt-1.55:.3f}) {{${flab}$}};')
    xm=(ba+bb)/2
    o.append(f'\\draw ({xm:.3f},{ybar:.3f}) -- ({xm:.3f},{ybar-.3:.3f});')
    o.append(f'\\draw[fill=gray!25,thick] ({xm-.5:.3f},{ybar-.3:.3f}) rectangle ({xm+.5:.3f},{ybar-.85:.3f}); \\node at ({xm:.3f},{ybar-.575:.3f}) {{{load}}};')
    if blok: o.append(f'\\node[right,align=left] at ({bb+.05:.3f},{ybar+.05:.3f}) {{{blok}}};')
    if name: o.append(f'\\node at ({xm:.3f},{ybar-1.25:.3f}) {{\\textbf{{{name}}}}};')
    return '\n'.join(o)

# ---------------- kaldıraç ----------------
def lever(items,x0,x1,xf,u=.8,yo=0.0,name=None,fb=.5):
    X=lambda x:x*u; o=[]
    o.append(f'\\draw[very thick] ({X(x0):.2f},{yo:.2f}) -- ({X(x1):.2f},{yo:.2f});')
    for i in range(x0,x1+1): o.append(f'\\draw[thin] ({X(i):.2f},{yo-.07:.2f}) -- ({X(i):.2f},{yo+.07:.2f});')
    o.append(f'\\draw[fill=gray!45] ({X(xf):.2f},{yo-.04:.2f}) -- ({X(xf)-.28:.2f},{yo-fb:.2f}) -- ({X(xf)+.28:.2f},{yo-fb:.2f}) -- cycle;')
    o.append(f'\\draw ({X(xf)-.5:.2f},{yo-fb:.2f}) -- ({X(xf)+.5:.2f},{yo-fb:.2f});')
    for it in items:
        kind,x,lab=it[:3]
        if kind=='box':
            o.append(f'\\draw ({X(x):.2f},{yo:.2f}) -- ({X(x):.2f},{yo-.35:.2f}); \\draw[fill=gray!25,thick] ({X(x)-.38:.2f},{yo-.35:.2f}) rectangle ({X(x)+.38:.2f},{yo-.95:.2f}); \\node[align=center] at ({X(x):.2f},{yo-.65:.2f}) {{{lab}}};')
        elif kind=='dn':
            o.append(f'\\draw[vurgu,very thick,{ARR}] ({X(x):.2f},{yo+.95:.2f}) -- ({X(x):.2f},{yo+.05:.2f}); \\node[vurgu,above] at ({X(x):.2f},{yo+.92:.2f}) {{{lab}}};')
        elif kind=='up':
            o.append(f'\\draw[vurgu,very thick,{ARR}] ({X(x):.2f},{yo-1.05:.2f}) -- ({X(x):.2f},{yo-.05:.2f}); \\node[vurgu,below] at ({X(x):.2f},{yo-1.02:.2f}) {{{lab}}};')
        elif kind=='wt':
            o.append(f'\\draw[thick,{ARR}] ({X(x):.2f},{yo:.2f}) -- ({X(x):.2f},{yo-.85:.2f}); \\node[right,align=left] at ({X(x)+.03:.2f},{yo-.55:.2f}) {{{lab}}};')
    if name: o.append(f'\\node at ({X(x0)-.45:.2f},{yo:.2f}) {{\\textbf{{{name}}}}};')
    return '\n'.join(o)

# ---------------- çıkrık ----------------
def cikrik(R,r,sc,yuk,Rlab,rlab,Flab='F'):
    R*=sc; r*=sc; o=[]
    o.append(f'\\draw[thick,fill=gray!20] (0,0) circle ({r:.3f}); \\fill (0,0) circle (1.6pt);')
    o.append(f'\\draw[very thick] (0,0) -- ({-R:.3f},0);')
    o.append(f'\\draw[fill=gray!60] ({-R-.06:.3f},-.1) rectangle ({-R+.06:.3f},.1);')
    o.append(f'\\draw[vurgu,very thick,{ARR}] ({-R:.3f},-.1) -- ({-R:.3f},-1.2); \\node[vurgu,left] at ({-R-.02:.3f},-.8) {{${Flab}$}};')
    o.append(f'\\draw[thick] ({r:.3f},0) -- ({r:.3f},-2.0); \\draw[fill=gray!25,thick] ({r-.45:.3f},-2.0) rectangle ({r+.45:.3f},-2.55); \\node at ({r:.3f},-2.275) {{{yuk}}};')
    yd=r+.35
    o.append(f'\\draw[thin,gray] ({-R:.3f},.12) -- ({-R:.3f},{yd+.1:.3f}); \\draw[thin,gray] (0,{r:.3f}) -- (0,{yd+.1:.3f});')
    o.append(f'\\draw[<->,thin] ({-R:.3f},{yd:.3f}) -- (0,{yd:.3f}); \\node[above] at ({-R/2:.3f},{yd-.02:.3f}) {{{Rlab}}};')
    a=radians(-40); o.append(f'\\draw[->,thin] (0,0) -- ({r*cos(a):.3f},{r*sin(a):.3f}); \\node[right] at ({r+.12:.3f},{r*sin(a)-.55:.3f}) {{{rlab}}};')
    return '\n'.join(o)

# ---------------- eğik düzlem ----------------
def incline(ox,b,h,frac,bw,bh,blab,flab,Flen,llab=None,hlab=None,ang=False,name=None):
    L=hypot(b,h); u=(b/L,h/L); n=(-h/L,b/L); o=[]
    o.append(f'\\draw[thick] ({ox:.3f},0) -- ({ox+b:.3f},0) -- ({ox+b:.3f},{h:.3f}) -- cycle;')
    S=(ox+u[0]*frac*L,u[1]*frac*L)
    c=[(S[0]-u[0]*bw/2,S[1]-u[1]*bw/2),(S[0]+u[0]*bw/2,S[1]+u[1]*bw/2)]
    c+=[(c[1][0]+n[0]*bh,c[1][1]+n[1]*bh),(c[0][0]+n[0]*bh,c[0][1]+n[1]*bh)]
    o.append('\\draw[thick,fill=gray!25] '+' -- '.join(f'({p[0]:.3f},{p[1]:.3f})' for p in c)+' -- cycle;')
    mid=(S[0]+n[0]*bh/2,S[1]+n[1]*bh/2)
    if blab: o.append(f'\\node[rotate={degrees(atan2(u[1],u[0])):.1f},font=\\scriptsize] at ({mid[0]:.3f},{mid[1]:.3f}) {{{blab}}};')
    f0=(S[0]+u[0]*bw/2+n[0]*bh/2,S[1]+u[1]*bw/2+n[1]*bh/2); f1=(f0[0]+u[0]*Flen,f0[1]+u[1]*Flen)
    o.append(f'\\draw[vurgu,very thick,{ARR}] ({f0[0]:.3f},{f0[1]:.3f}) -- ({f1[0]:.3f},{f1[1]:.3f});')
    if flab: o.append(f'\\node[vurgu] at ({f1[0]+n[0]*.3:.3f},{f1[1]+n[1]*.3:.3f}) {{{flab}}};')
    if llab:
        M=(ox+b/2,h/2); o.append(f'\\node[rotate={degrees(atan2(u[1],u[0])):.1f}] at ({M[0]-n[0]*.3:.3f},{M[1]-n[1]*.3:.3f}) {{{llab}}};')
    if hlab: o.append(f'\\node[right] at ({ox+b+.05:.3f},{h/2:.3f}) {{{hlab}}};')
    if ang: o.append(f'\\draw ({ox+.8:.3f},0) arc[start angle=0,end angle={degrees(atan2(h,b)):.2f},radius=.8]; \\node at ({ox+1.15:.3f},.2) {{${ang}$}};')
    if name: o.append(f'\\node at ({ox+b/2:.3f},-.35) {{\\textbf{{{name}}}}};')
    return '\n'.join(o)

# ---------------- dişli ----------------
KD=.06
def gear(cx,cy,N,fill='gray!12',lw=2.6):
    r=N*KD; a=2*pi*r*28.4528/(2*N)
    return (f'\\fill[{fill}] ({cx:.3f},{cy:.3f}) circle ({r-.04:.3f});'
            f'\\draw[line width={lw}pt,gray!70,dash pattern=on {a:.2f}pt off {a:.2f}pt] ({cx:.3f},{cy:.3f}) circle ({r:.3f});'
            f'\\draw[thin] ({cx:.3f},{cy:.3f}) circle ({r-.1:.3f});\\fill ({cx:.3f},{cy:.3f}) circle (1.4pt);')
def cw_arrow(cx,cy,r):
    ra=r+.28; return f'\\draw[vurgu,very thick,{ARR}] ({cx+ra*cos(radians(150)):.3f},{cy+ra*sin(radians(150)):.3f}) arc[start angle=150,end angle=75,radius={ra:.3f}];'

# ---------------- öncüllü yardımcı ----------------
KUME=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETLER=[(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)]
ROM=['I','II','III']
def oncul(stm,idx):
    """stm: [(metin, doğru_mu, neden, islem)] → (metin_öncüller, doğru, sira, yan(wrong list), adım listesi)"""
    truth=tuple(i for i,s in enumerate(stm) if s[1]); p=SETLER.index(truth)
    lo=p-idx; assert lo>=0 and lo+4<=6,(p,idx)
    sira=KUME[lo:lo+5]; ok=KUME[p]; assert sira[idx]==ok
    yan=[]
    for j in range(lo,lo+5):
        if j==p: continue
        s=SETLER[j]; parts=[]
        for i in range(3):
            if i in s and i not in truth: parts.append(f'{ROM[i]}. yargıyı doğru saymış; oysa {stm[i][2]}.')
            if i in truth and i not in s: parts.append(f'{ROM[i]}. yargıyı yanlış saymış; oysa {stm[i][2]}.')
        yan.append((KUME[j],' '.join(parts),'bilgi'))
    met='\n'.join(f'{ROM[i]}. {stm[i][0]}' for i in range(3))
    return met,ok,sira,yan
def oncul_adim(stm,ilk,son):
    ad=[A(ilk[0],ilk[1],ilk[2])]
    for i,s in enumerate(stm): ad.append(A(f'{ROM[i]}. yargıyı incele',s[2][0].upper()+s[2][1:]+'.',s[3]+(' → doğru' if s[1] else ' → yanlış')))
    ad.append(A('Sonucu yaz',son[0],son[1])); return ad

SK={}
# =========================================================================================
# KARTLAR
kartla('K-AFMAK-01','Makara sistemlerinde kuvvet kazancı','Yükü taşıyan ip sayısı n ise ideal sistemde F = (G + hareketli makara ağırlığı)/n; ipi n kat fazla çekmek gerekir.','Sabit makarayı kuvvet kazancı sanmak; ip sayısını yanlış saymak; hareketli makara ağırlığını unutmak.','orta',3,'bm-makara','Makara ve palanga sistemlerinde kuvvet kazancı')
kartla('K-AFMAK-02','Kaldıraçta tork dengesi','Mesnede göre torkların toplamı sıfır: ΣF·d(sol) = ΣF·d(sağ); kuvvet kolu mesnede dik uzaklıktır.','Kuvvetleri toplamak; çubuğun ağırlığını unutmak; kolu mesnetten değil uçtan ölçmek.','orta',4,'bm-kaldirac','Kaldıraçta tork dengesi ve kuvvet kazancı')
kartla('K-AFMAK-03','Çıkrıkta denge','F·R = G·r; kol uzar ya da silindir incelirse kuvvet azalır, yol artar.','Kuvvet kolu ile yük kolunu ters yazmak; yarıçaplar yerine farkı almak.','orta',3,'bm-cikrik','Çıkrıkta kuvvet ve yol ilişkisi')
kartla('K-AFMAK-04','Eğik düzlem','Sürtünmesiz eğik düzlemde F·l = G·h; iş sabit, kuvvet azalırsa yol artar.','h/l yerine cos ya da tersini kullanmak; sürtünmeli ve sürtünmesizi karıştırmak.','kolay',2,'bm-egik','Eğik düzlemde kuvvet, yol ve iş')
kartla('K-AFMAK-05','Dişli sistemleri','Birbirine geçen dişlilerde diş sayısı × tur sayısı eşit, yön zıt; ortak eksenli dişliler aynı turu atar.','Ortak eksenli dişliyi atlamak; oranı ters kullanmak; yönü yanlış saymak.','orta',4,'bm-disli','Dişlilerde tur sayısı ve dönüş yönü')
kartla('K-AFMAK-06','Verim','η = yararlı iş / harcanan iş; sürtünmeli makinede η < 1, gereken kuvvet ideal kuvvetin 1/η katıdır.','Oranı ters yazmak; verimi kuvvet değeriyle karıştırmak.','orta',4,'bm-verim','Verim hesabı')
kartla('K-AFMAK-07','Grafikle makine analizi','Doğrunun eğimi ve kesim noktası makinenin özelliğini verir (ip sayısı, makara ağırlığı, verim).','Eğimi ters yorumlamak; kesim noktasını ağırlık sanmak.','zor',4,'bm-grafik','Grafikten verim ve kuvvet bulma')
kartla('K-AFMAK-08','Basit makine kavramları','Basit makine iş kazancı sağlamaz; kuvvetten kazanç yoldan kayıptır; verim 1’i aşmaz.','Kuvvet kazancını iş kazancı sanmak.','kolay',2,'bm-kavram','Basit makinelerde kuvvet–yol–iş ilişkisi')

# =========================================================================================
# 01 · makara · kolay
f1=[palanga(2,load='$60$ N')]
SK[1]=fig(f1)
G=60; assert Fr(G,2)==30
q('0001',[A('Düzeneği tanı','Şekilde bir sabit, bir hareketli makara vardır; ip ve makaralar ağırlıksız, sürtünme yoktur.','G = 60 N (şekilde)'),
          A('İp sayısını bul','Hareketli makarayı iki ip kolu taşır; sabit makara yalnızca yön değiştirir.','Yükü taşıyan ip sayısı n = 2'),
          A('Kuvveti yaz','Ağırlıksız makarada F = G ÷ n.','F = 60 ÷ 2 = 30 N')],
  tipId='bm-makara',tip='Makara ve palanga sistemlerinde kuvvet kazancı',z='kolay',alt='Makara Sistemleri',kaz='Bir sabit ve bir hareketli makaradan oluşan sistemde dengeleyen kuvveti bulur.',kalip='şekilli',
  kart='K-AFMAK-01 (makara, ip sayısı) · bir sabit + bir hareketli makara',
  metin='Ağırlıksız bir iple ve ağırlıksız makaralarla kurulan şekildeki düzenekte yük, ip ucuna uygulanan F kuvvetiyle sabit hızla yukarı çekilmektedir. Sürtünmeler önemsizdir.\nBuna göre, F kuvvetinin büyüklüğü kaç N’dur?',
  dogru=30,yan=[(15,'Her iki makarayı da hareketli sanıp yükü 4 ip kolunun taşıdığını düşünmüş: F = 60 ÷ 4 = 15 N.','bilgi'),
                (20,'Sabit makaradaki ipi de sayıp 3 kol almış: F = 60 ÷ 3 = 20 N; sabit makara yük taşımaz.','bilgi'),
                (60,'Makaraların kuvvetten kazanç sağlamadığını düşünmüş: F = G = 60 N.','bilgi'),
                (120,'Kuvvet kazancını ters yorumlayıp yükü iki katına çıkarmış: F = 2 · 60 = 120 N.','dikkat')],
  istenen='Yükü sabit hızla çeken F kuvvetinin büyüklüğü (N).',ip=['Yükün ağırlığını kaç ip kolunun paylaştığını şekilden say.'],
  bilgi=[B('Hareketli makara','yükle birlikte hareket eden makaradır; ağırlıksız ve sürtünmesizse yükü taşıyan ip kolları kuvveti eşit paylaşır. Örnek: 100 N’luk yükü iki kol taşırsa her koldaki gerilme 50 N olur'),
         B('Sabit makara','yalnız kuvvetin yönünü değiştirir; kuvvetten kazanç sağlamaz. Örnek: 40 N’luk yükü sabit makarayla dengelemek için 40 N gerekir')],
  puf='Palangada kuvvet kazancı, yükü taşıyan ip kolu sayısına eşittir; sabit makarayı ip kolu olarak sayma.',sekil=SK[1])

# 02 · makara · orta
f2=[palanga(4,load='$150$ N',blok='makara\\\\bloğu:\\\\$10$ N')]
SK[2]=fig(f2)
G2,Gb=150,10; n2=4; F2=Fr(G2+Gb,n2); assert F2==40
assert Fr(G2,4)==Fr(75,2) and Fr(G2,3)==50 and Fr(G2+Gb,2)==80 and G2+Gb==160
q('0002',[A('Taşıyan ip sayısını bul','Hareketli bloğa bağlı ip kollarını say; serbest uç sayılmaz, bloğa bağlanan uç sayılır.','n = 4'),
          A('Bloğu yüke ekle','Hareketli makara bloğu da yükle birlikte yükselir; ip kollarının taşıdığı toplam ağırlık bulunur.','G + G_blok = 150 + 10 = 160 N'),
          A('Kuvveti hesapla','Kollardaki gerilme eşittir ve F’ye eşittir.','F = 160 ÷ 4 = 40 N')],
  tipId='bm-makara',tip='Makara ve palanga sistemlerinde kuvvet kazancı',z='orta',alt='Makara Sistemleri',kaz='Hareketli makara bloğunun ağırlığını da katarak palangada dengeleyen kuvveti bulur.',kalip='şekilli',
  kart='K-AFMAK-01 (makara, ip sayısı) · 4 kollu palanga, ağırlıklı blok',
  metin='Şekildeki palanga düzeneğinde yük, ip ucuna uygulanan F kuvvetiyle sabit hızla yükseltilmektedir. İp ve üst bloktaki makaralar ağırlıksızdır, sürtünmeler önemsizdir; yükün ve alt makara bloğunun ağırlıkları şekilde verilmiştir.\nBuna göre, F kuvvetinin büyüklüğü kaç N’dur?',
  dogru=40,yan=[(37.5,'Alt makara bloğunun ağırlığını unutmuş: F = 150 ÷ 4 = 37,5 N.','dikkat'),
                (50,'Bloğa bağlı ip kollarından yalnız 3’ünü saymış: F = 150 ÷ 3 = 50 N.','bilgi'),
                (80,'Yalnız iki ip kolu saymış: F = (150 + 10) ÷ 2 = 80 N.','bilgi'),
                (160,'Toplam ağırlığı ip kollarına bölmeden F = G + G_blok = 160 N almış.','islem')],
  istenen='Sistemi sabit hızla yükselten F kuvvetinin büyüklüğü (N).',ip=['Alt bloğa bağlı ip kollarının sayısını, bloğun kendi ağırlığını unutmadan değerlendir.'],
  bilgi=[B('Palanga','hareketli bloğa bağlı n ip kolu varsa ideal durumda F = (yük + blok ağırlığı) ÷ n olur. Örnek: 90 N’luk toplam ağırlığı 3 kol taşırsa F = 30 N'),
         B('Yol–kuvvet','ip ucu yükten n kat fazla yol alır; F·(n·h) = (yük + blok)·h. Örnek: 3 kollu sistemde yük 1 m yükselirken ip ucu 3 m çekilir')],
  puf='Hareketli makara bloğunun ağırlığı varsa önce toplam ağırlığı bul, sonra ip kolu sayısına böl.',sekil=SK[2])

# 03 · kaldıraç · orta
f3=[lever([('box',0,'$50$ N'),('box',6,'$20$ N'),('dn',8,'$F$')],0,8,4)]
SK[3]=fig(f3)
a3=50*4; b3=20*2; F3=Fr(a3-b3,4); assert F3==40 and Fr(a3,4)==Fr(50) and Fr(a3-b3,8)==20 and Fr(a3,8)==Fr(25) and 50-20==30
q('0003',[A('Kuvvet kollarını oku','Kolu, mesnetten kuvvetin etki çizgisine olan dik uzaklıktır; bölmeleri say.','50 N → 4 bölme · 20 N → 2 bölme · F → 4 bölme'),
          A('Dengeyi yaz','Çubuk dengede: saat yönü torklarının toplamı saat yönünün tersindekilere eşit.','50 × 4 = 20 × 2 + F × 4'),
          A('F’yi çöz','Önce torkları hesapla, sonra F’yi bul.','200 = 40 + 4F → F = 40 N')],
  tipId='bm-kaldirac',tip='Kaldıraçta tork dengesi ve kuvvet kazancı',z='orta',alt='Kaldıraç',kaz='Ağırlıksız çubuğun mesnede göre tork dengesini yazarak bilinmeyen kuvveti bulur.',kalip='şekilli',
  kart='K-AFMAK-02 (kaldıraç tork dengesi) · mesnet bir yanda iki yük, öbür yanda F',
  metin='Ağırlıksız çubuk, bölmeleri eşit aralıklı olacak biçimde şekildeki gibi mesnet üzerinde yatay dengededir. Çubuğa asılan yüklerin ağırlıkları ve ucuna uygulanan F kuvveti şekilde gösterilmiştir.\nBuna göre, F kuvvetinin büyüklüğü kaç N’dur?',
  dogru=40,yan=[(20,'Torkları doğru bulup (200 − 40 = 160) kuvvet kolunu çubuğun tamamı sanarak 8 bölmeye bölmüş: F = 160 ÷ 8 = 20 N.','islem'),
                (25,'20 N’luk yükü hiç katmamış ve kolu 8 bölme almış: F = 200 ÷ 8 = 25 N.','dikkat'),
                (30,'Tork yerine kuvvetleri karşılaştırıp 50 − 20 = 30 N bulmuş.','bilgi'),
                (50,'Sağdaki 20 N’luk yükün torkunu hesaba katmamış: F = 200 ÷ 4 = 50 N.','dikkat')],
  istenen='Çubuğu dengede tutan F kuvvetinin büyüklüğü (N).',ip=['Mesnede göre her kuvvetin torkunu (kuvvet × kol) yazıp iki taraf için karşılaştır.'],
  bilgi=[B('Tork','τ = F·d; d, mesnetten kuvvetin etki çizgisine dik uzaklıktır. Örnek: 10 N’luk kuvvet mesnetten 3 bölme uzakta ise tork 30 N·bölmedir'),
         B('Denge koşulu','ağırlıksız çubuk dengede iken mesnede göre toplam tork sıfırdır; saat yönündeki torklar toplamı, tersindekilerin toplamına eşittir')],
  puf='Kaldıraç sorusunda kuvvetleri değil torkları dengele; kolu her zaman mesnetten ölç.',sekil=SK[3])

# 04 · kaldıraç öncüllü · orta (A)
u4=.85
f4=[lever([('box',0,'$G$'),('dn',4,'$F$')],0,4,1,u=u4,yo=0,name='X'),
    lever([('up',1,'$F$'),('box',3,'$G$')],0,4,0,u=u4,yo=-3.1,name='Y'),
    lever([('box',0,'$G$'),('dn',4,'$F$')],0,4,2,u=u4,yo=-6.2,name='Z')]
SK[4]=fig(f4)
st4=[('X kaldıracında uygulanan F kuvveti, yükün ağırlığından küçüktür.',True,'X’te yük kolu 1 bölme, kuvvet kolu 3 bölmedir; F × 3 = G × 1 olduğundan F = G ÷ 3 < G','F × 3 = G × 1'),
     ('Y kaldıracında uygulanan F kuvveti, yükün ağırlığından küçüktür.',False,'Y’de mesnet çubuğun ucundadır; kuvvet kolu 1 bölme, yük kolu 3 bölmedir; F × 1 = G × 3 olduğundan F = 3G > G','F × 1 = G × 3'),
     ('Z kaldıracında uygulanan F kuvveti, yükün ağırlığından büyüktür.',False,'Z’de iki kol da 2 bölmedir; F × 2 = G × 2 olduğundan F = G','F × 2 = G × 2')]
m4,d4,s4,y4=oncul(st4,0)
q('0004',oncul_adim(st4,('Kolları belirle','Her kaldıraçta kuvvet ve yük kolunu bölmelerden oku.','X: 3 ve 1 · Y: 1 ve 3 · Z: 2 ve 2'),('Doğru yargıyı seç','Yalnız I doğrudur.','Yalnız I')),
  tipId='bm-kaldirac',tip='Kaldıraçta tork dengesi ve kuvvet kazancı',z='orta',alt='Kaldıraç',kaz='Farklı türdeki kaldıraçlarda kuvvet ve yük kollarını karşılaştırarak kuvvet kazancını yorumlar.',kalip='öncüllü',
  kart='K-AFMAK-02 (kaldıraç tork dengesi) · üç tür kaldıraç, kuvvet kazancı yorumu',
  metin='Ağırlıksız çubuklardan oluşan X, Y ve Z kaldıraçlarında özdeş G ağırlıklı yükler şekillerdeki gibi asılmıştır. Bölmeler eşit aralıklıdır ve her kaldıraç, çubuğa dik uygulanan F kuvvetiyle yatay dengede tutulmaktadır.\nBuna göre,\n'+m4+'\nyargılarından hangileri doğrudur?',
  dogru=d4,yan=y4,sira=s4,
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Her kaldıraçta kuvvetin kolunu yükün koluyla kıyasla; hangisi daha uzun?'],
  bilgi=[B('Kuvvet kazancı','kuvvet kolu yük kolundan uzunsa F < G olur; kollar eşitse F = G, kuvvet kolu kısaysa F > G. Örnek: kuvvet kolu 4, yük kolu 2 ise F = G ÷ 2'),
         B('Kaldıraç türleri','mesnet iki kuvvetin arasındaysa, yük ortadaysa ya da kuvvet ortadaysa tork dengesi aynı yazılır; yalnız kolların uzunluğu önemlidir')],
  puf='Kuvvet kazancı yalnızca kolların oranına bağlıdır; mesnedin çubuğun neresinde olduğu değil, kolların uzunluğu belirleyicidir.',sekil=SK[4])

# 05 · kaldıraç ağırlıklı çubuk · zor (E)
f5=[lever([('dn',0,'$F$'),('wt',4,'çubuk\\\\$40$ N'),('box',7,'$20$ N')],0,8,2)]
SK[5]=fig(f5)
Gc,Q5=40,20; F5=Fr(Gc*2+Q5*5,2); assert F5==90
assert Fr(Gc*2,2)==40 and Fr(Q5*5,2)==50 and Gc+Q5==60 and Fr(Gc*2+Q5*4,2)==80
Nt=F5+Gc+Q5; assert Nt==150 and Gc+Q5==60 and F5==90 and F5+Q5==110 and F5+Gc==130
q('0005',[A('Çubuğun ağırlığını yerleştir','Türdeş çubuğun ağırlığı orta noktasında (4. bölme) etki eder; mesnet 2. bölmededir.','Kol: 4 − 2 = 2 bölme'),
          A('Tork dengesiyle F’yi bul','Mesnede göre: F sol uçta (kol 2), 20 N’luk yük sağ uçtan 1 bölme içeridedir (kol 5).','F × 2 = 40 × 2 + 20 × 5 → F = 90 N'),
          A('Kuvvet dengesini yaz','Çubuk durgun: yukarı yönlü tepki, aşağı yönlü kuvvetlerin toplamına eşittir.','N = F + 40 + 20'),
          A('Tepkiyi hesapla','Değerleri yerleştir.','N = 90 + 40 + 20 = 150 N')],
  tipId='bm-kaldirac',tip='Kaldıraçta tork dengesi ve kuvvet kazancı',z='zor',alt='Kaldıraç',kaz='Çubuk ağırlığını da katan tork dengesiyle bilinmeyen kuvveti, ardından kuvvet dengesiyle mesnet tepkisini bulur.',kalip='şekilli',
  kart='K-AFMAK-02 (kaldıraç tork dengesi) · türdeş çubuk, mesnet tepkisi (tork + kuvvet dengesi)',
  metin='Türdeş çubuk, bölmeleri eşit aralıklı olacak biçimde şekildeki gibi mesnet üzerinde yatay dengede tutulmaktadır. Çubuğun ağırlığı ve çubuğa asılan yükün ağırlığı şekilde gösterilmiştir; sol uca düşey, aşağı yönlü F kuvveti uygulanmaktadır.\nBuna göre, mesnedin çubuğa uyguladığı tepki kuvveti kaç N’dur?',
  dogru=150,yan=[(60,'Yalnız çubuğun ve yükün ağırlıklarını toplamış: 40 + 20 = 60 N; F’yi katmamış.','dikkat'),
                (90,'Tork dengesinden F’yi bulup (90 N) tepkiyi F’ye eşit almış.','dikkat'),
                (110,'Tepkiyi F + yük = 90 + 20 = 110 N bulmuş; çubuğun ağırlığını katmamış.','islem'),
                (130,'Tepkiyi F + çubuk ağırlığı = 90 + 40 = 130 N bulmuş; asılı yükü katmamış.','islem')],
  istenen='Mesnedin çubuğa uyguladığı tepki kuvvetinin büyüklüğü (N).',ip=['Önce çubuğun dönmemesi için gereken F’yi bul; sonra çubuğun ötelenmemesi için düşey kuvvetleri dengele.'],
  bilgi=[B('Türdeş çubuk','ağırlık merkezi çubuğun orta noktasıdır; ağırlık orada tek bir kuvvet gibi etki eder. Örnek: 1 m’lik türdeş çubuğun ağırlık merkezi uçtan 50 cm uzaktadır'),
         B('Denge koşulları','durgun çubukta hem mesnede göre toplam tork hem de düşey kuvvetlerin toplamı sıfırdır')],
  puf='Dengedeki çubukta iki koşul birlikte kullanılır: torklar bilinmeyen kuvveti, kuvvet dengesi mesnet tepkisini verir.',sekil=SK[5])

# 06 · çıkrık · orta (A)
SK[6]=fig([cikrik(40,10,.05,'$200$ N','$R=40$ cm','$r=10$ cm')])
R6,r6,G6=40,10,200; F6=Fr(G6*r6,R6); assert F6==50 and Fr(G6,2)==100 and G6*(R6-r6)/R6==150 and G6*R6//r6==800
q('0006',[A('Dengeyi tanıt','Sabit hızda çıkrığın dönme dengesi: kuvvetin torku yükün torkuna eşittir.','F × R = G × r'),
          A('Değerleri yerleştir','Yarıçapları aynı birimde (cm) kullan.','F × 40 = 200 × 10'),
          A('F’yi bul','Denklemi çöz.','F = 2000 ÷ 40 = 50 N')],
  tipId='bm-cikrik',tip='Çıkrıkta kuvvet ve yol ilişkisi',z='orta',alt='Çıkrık',kaz='Çıkrıkta kol uzunluğu ve silindir yarıçapı ile yükü dengeleyen kuvveti bulur.',kalip='şekilli',
  kart='K-AFMAK-03 (çıkrık, F·R = G·r) · sayısal denge',
  metin='Şekildeki çıkrıkta silindire sarılı ağırlıksız ipin ucundaki yük, kolun ucuna dik uygulanan F kuvvetiyle dengelenmektedir. Kol uzunluğu, silindirin yarıçapı ve yükün ağırlığı şekilde verilmiştir; sürtünmeler önemsizdir.\nBuna göre, F kuvvetinin büyüklüğü kaç N’dur?',
  dogru=50,yan=[(100,'Çıkrığı hareketli makara gibi düşünüp yükü ikiye bölmüş: F = 200 ÷ 2 = 100 N.','bilgi'),
                (150,'Yük kolunu r yerine R − r = 30 cm almış: F = 200 × 30 ÷ 40 = 150 N.','islem'),
                (200,'Kuvvetten kazanç olmadığını düşünüp F = G = 200 N yazmış.','bilgi'),
                (800,'Yarıçap oranını ters yazmış: F = 200 × 40 ÷ 10 = 800 N.','islem')],
  istenen='Yükü dengeleyen F kuvvetinin büyüklüğü (N).',ip=['Silindirin ve kolun merkeze uzaklıklarını kuvvet kolu olarak kullan.'],
  bilgi=[B('Çıkrık','silindir ve ona bağlı koldan oluşan kaldıraç türüdür; denge koşulu F·R = G·r’dir. Örnek: R = 30 cm, r = 5 cm ise 12 N’luk kuvvet 72 N’luk yükü dengeler')],
  puf='Çıkrıkta kuvvet kazancı R ÷ r kadardır; büyük yarıçapa uygulanan kuvvet küçük yarıçaptaki yükü dengeler.',sekil=SK[6])

# 07 · çıkrık öncüllü · orta (C)
SK[7]=fig([cikrik(40,10,.05,'yük','$R$','$r$')])
st7=[('Yük aynı kalmak koşuluyla R artırılırsa yükü dengeleyen F azalır.',True,'denge koşulu F × R = G × r olduğundan R arttıkça F = G × r ÷ R azalır','F ∝ 1/R'),
     ('Yük aynı kalmak koşuluyla r küçültülürse yükü dengeleyen F azalır.',True,'F = G × r ÷ R olduğundan r küçüldükçe F azalır','F ∝ r'),
     ('r küçültülürse yük aynı yüksekliğe çıkarılırken kolun döndürülmesi gereken tur sayısı azalır.',False,'ip silindirin çevresine sarıldığından yükselme h = n × 2πr’dir; r küçüldükçe aynı h için n artar','n = h ÷ 2πr')]
m7,d7,s7,y7=oncul(st7,2)
q('0007',oncul_adim(st7,('Dengeyi yaz','Çıkrıkta kuvvet ve yük torkları eşittir.','F × R = G × r'),('Doğru yargıları seç','I ve II doğru, III yanlıştır.','I ve II')),
  tipId='bm-cikrik',tip='Çıkrıkta kuvvet ve yol ilişkisi',z='orta',alt='Çıkrık',kaz='Çıkrıkta kol uzunluğu ve silindir yarıçapı değişince kuvvet ve yolun nasıl değiştiğini yorumlar.',kalip='öncüllü',
  kart='K-AFMAK-03 (çıkrık, F·R = G·r) · nitel değişim, tur sayısı',
  metin='Şekildeki çıkrıkta silindire sarılı ağırlıksız ipin ucundaki yük, kolun ucuna dik uygulanan F kuvvetiyle dengelenmektedir. Kol uzunluğu R, silindirin yarıçapı r ile gösterilmiştir; sürtünmeler önemsizdir.\nBuna göre,\n'+m7+'\nyargılarından hangileri doğrudur?',
  dogru=d7,yan=y7,sira=s7,
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Denge bağıntısını yazıp hangi nicelik değişince F’nin nasıl değiştiğine bak; tur sayısı için ipin sarıldığı çevreyi düşün.'],
  bilgi=[B('Çıkrık dengesi','F·R = G·r; kuvvet kolu R uzadıkça ya da yük kolu r kısaldıkça gereken kuvvet azalır. Örnek: R iki katına çıkarsa aynı yük için F yarıya iner'),
         B('Silindirde sarılan ip','silindir bir tur döndüğünde 2πr uzunluğunda ip sarılır; yük de bu kadar yükselir')],
  puf='Çıkrıkta kuvvetten kazandığın kadar yoldan (dönme sayısından) kaybedersin.',sekil=SK[7])

# 08 · eğik düzlem · kolay (D)
SK[8]=fig([incline(0,4,3,.5,.85,.5,'$60$ N','$F$',1.0,llab='$l=5$ m',hlab='$h=3$ m')]+['\\draw (3.8,0) -- (3.8,.2) -- (4,.2);','\\draw (-.4,0) -- (4.6,0);'])
G8,h8,l8=60,3,5; F8=Fr(G8*h8,l8); assert F8==Fr(36) and Fr(G8,l8)==12 and Fr(G8,h8)==20 and Fr(G8*h8,l8+h8)==Fr(45,2) and G8*4//5==48
q('0008',[A('Verileri oku','Şekilden yükseklik ve yol uzunluğu okunur.','G = 60 N; h = 3 m; l = 5 m'),
          A('İş korunumunu yaz','Sürtünme yoksa F’nin yaptığı iş, yükün potansiyel enerji artışına eşittir.','F × l = G × h'),
          A('F’yi hesapla','Değerleri yerleştir.','F = (60 × 3) ÷ 5 = 36 N')],
  tipId='bm-egik',tip='Eğik düzlemde kuvvet, yol ve iş',z='kolay',alt='Eğik Düzlem',kaz='Sürtünmesiz eğik düzlemde yükü sabit hızla çeken kuvveti yükseklik ve yol oranıyla bulur.',kalip='şekilli',
  kart='K-AFMAK-04 (eğik düzlem, F·l = G·h) · sürtünmesiz',
  metin='Sürtünmesiz bir rampa üzerindeki cisim, rampaya paralel F kuvvetiyle sabit hızla yukarı doğru çekilmektedir. Cismin ağırlığı ve rampanın ölçüleri şekilde gösterilmiştir.\nBuna göre, F kuvvetinin büyüklüğü kaç N’dur?',
  dogru=36,yan=[(12,'Ağırlığı yalnız yol uzunluğuna bölmüş: F = 60 ÷ 5 = 12 N.','islem'),
                (20,'Ağırlığı yüksekliğe bölmüş: F = 60 ÷ 3 = 20 N.','islem'),
                (22.5,'Yolu (l + h = 8 m) almış: F = 60 × 3 ÷ 8 = 22,5 N.','bilgi'),
                (48,'Yükseklik yerine tabanı (4 m) kullanmış: F = 60 × 4 ÷ 5 = 48 N.','bilgi')],
  istenen='Cismi sabit hızla çeken F kuvvetinin büyüklüğü (N).',ip=['Sürtünme yokken yapılan işin, yük için kazanılan yükseklik enerjisine eşit olduğunu kullan.'],
  bilgi=[B('Eğik düzlem','sürtünmesizken F × l = G × h; l, düzlem boyu, h yüksekliktir. Örnek: h = 2 m, l = 8 m ise 100 N’luk yük 25 N’la çekilir')],
  puf='Eğik düzlemde kuvvet h/l oranı kadar küçülür; yol aynı oranda uzar, iş değişmez.',sekil=SK[8])

# 09 · verim eğik düzlem · orta (C)
b9=sqrt(100-16); sc9=.5
SK[9]=fig([incline(0,b9*sc9,4*sc9,.5,.8,.46,'$200$ N','$100$ N',1.0,llab='$l=10$ m',hlab='$h=4$ m')]+[f'\\draw (-.4,0) -- ({b9*sc9+.6:.2f},0);'])
G9,h9,l9,F9=200,4,10,100; W9=G9*h9; T9=F9*l9; eta9=Fr(W9,T9); assert eta9==Fr(4,5) and 100-80==20 and Fr(h9,l9)==Fr(2,5) and Fr(T9,W9)==Fr(5,4)
q('0009',[A('Yararlı işi bul','Yararlı iş, yükün potansiyel enerji artışıdır.','W_yararlı = G × h = 200 × 4 = 800 J'),
          A('Harcanan işi bul','Sürtünmeli düzlemde F kuvveti l boyunca iş yapar.','W_toplam = F × l = 100 × 10 = 1000 J'),
          A('Verimi hesapla','Verim, yararlı işin harcanan işe oranıdır.','η = 800 ÷ 1000 = 0,8 → %80')],
  tipId='bm-verim',tip='Verim hesabı',z='orta',alt='Verim',kaz='Sürtünmeli eğik düzlemde yararlı ve harcanan işi karşılaştırarak verimi hesaplar.',kalip='şekilli',
  kart='K-AFMAK-06 (verim) · sürtünmeli eğik düzlem',
  metin='Bir depo çalışanı, sürtünmeli bir rampa üzerindeki yükü rampaya paralel bir kuvvetle sabit hızla yukarı çekmektedir. Yükün ağırlığı, uygulanan kuvvet ve rampanın boyutları şekilde verilmiştir.\nBuna göre, eğik düzlemin verimi yüzde kaçtır?',
  dogru=80,yan=[(20,'Kaybedilen işin oranını (%20) verim sanmış.','dikkat'),
                (40,'Eğik düzlemin eğimini (h ÷ l = 0,4) verim olarak yorumlamış.','bilgi'),
                (100,'F’nin değerini (100 N) yüzde olarak yazmış.','dikkat'),
                (125,'Oranı ters alıp harcanan işi yararlı işe bölmüş: 1000 ÷ 800 = 1,25.','islem')],
  istenen='Eğik düzlemin verimi (%).',ip=['Yükü yükseltmek için gereken en az işi ile kuvvetin gerçekte yaptığı işi ayrı ayrı bul.'],
  bilgi=[B('Verim','η = yararlı iş ÷ harcanan iş; sürtünme varsa 1’den küçüktür. Örnek: 90 J yararlı iş için 120 J harcanıyorsa η = 0,75')],
  puf='Verim her zaman “çıkan iş ÷ giren iş” olarak yazılır ve gerçek makinelerde %100’ü geçmez.',sekil=SK[9])

# 10 · dişli zinciri · zor (E)
cA,cB,cC,cD=(0,0),(1.5*1.0+.0,0),None,None
A_,B_,C_,D_=10,30,20,10
rA,rB,rC,rD=A_*KD,B_*KD,C_*KD,D_*KD
Ax,Ay=0,0; Bx,By=rA+rB,0; Bx,By=rA+rB,0; Cx,Cy=Bx+rB+rC+.9,0; Dx,Dy=Cx+rC+rD,0
f10=[gear(Ax,Ay,A_,'gray!25'),gear(Bx,By,B_,'gray!12'),gear(Cx,Cy,C_,'gray!30'),gear(Dx,Dy,D_,'gray!25'),
     f'\\draw[line width=3pt] ({Bx:.3f},{By}) -- ({Cx:.3f},{Cy}); \\fill ({Bx:.3f},{By}) circle (2pt) ({Cx:.3f},{Cy}) circle (2pt);',
     cw_arrow(Ax,Ay,rA),
     f'\\node[align=center] at ({Ax},{Ay}) {{A\\\\${A_}$ diş}};',f'\\node[align=center,fill=gray!12,inner sep=1pt] at ({Bx},{By-.55}) {{B\\\\${B_}$ diş}};',
     f'\\node[align=center,fill=gray!30,inner sep=1pt] at ({Cx:.3f},{Cy-.5}) {{C\\\\${C_}$ diş}};',
     f'\\node[align=center] at ({Dx:.3f},{Dy:.3f}) {{D\\\\${D_}$ diş}};',
     f'\\node[above,font=\\footnotesize] at ({(Bx+rB+Cx-rC)/2:.3f},.1) {{ortak eksen}};']
SK[10]=fig(f10)
nA=6; nB=Fr(nA*A_,B_); nC=nB; nD=nC*C_/D_; assert (nB,nD)==(2,4)
assert Fr(nB*B_,D_)==6 and Fr(nC*D_,C_)==1 and Fr(nA*A_,D_)==6
q('0010',[A('A ile B’yi eşle','Birbirine geçen dişlilerde diş sayısı × tur sayısı eşittir; yönler zıttır.','10 × 6 = 30 × n_B → n_B = 2 tur (A’ya zıt yönde)'),
          A('Ortak ekseni kullan','C, B ile aynı eksene bağlı; aynı yönde ve aynı sayıda tur atar.','n_C = 2 tur (A’ya zıt yönde)'),
          A('C ile D’yi eşle','C ve D birbirine geçmiştir; yön yine tersine döner.','20 × 2 = 10 × n_D → n_D = 4 tur'),
          A('Yönü belirle','Art arda iki geçişte yön iki kez tersine döner.','A ile aynı yönde, 4 tur')],
  tipId='bm-disli',tip='Dişlilerde tur sayısı ve dönüş yönü',z='orta',alt='Dişli Sistemleri',kaz='Ortak eksenli dişlileri içeren dişli zincirinde tur sayısını ve dönüş yönünü bulur.',kalip='şekilli',
  kart='K-AFMAK-05 (dişli, diş × tur) · ortak eksenli iki kademeli zincir',
  metin='Şekildeki dişli sisteminde A ve B dişlileri birbirine, C ve D dişlileri de birbirine geçmiştir. B ve C dişlileri aynı eksene sağlam biçimde bağlıdır ve birlikte döner. Diş sayıları şekilde verilmiştir. A dişlisi şekildeki ok yönünde 6 tur döndürülmektedir.\nBuna göre, D dişlisinin dönüş yönü ve tur sayısı nedir?',
  dogru='A ile aynı yönde, 4 tur',yan=[('A ile aynı yönde, 1 tur','C ile D’nin diş oranını ters kullanmış: 2 × 10 ÷ 20 = 1 tur.','islem'),
          ('A ile ters yönde, 2 tur','C’nin dönüşünü D’ye eşit almış ve iki geçişte yönün değişmeyeceğini unutmuş.','bilgi'),
          ('A ile aynı yönde, 2 tur','D’nin turunu C’nin turuna eşit sanmış (diş sayılarını katmamış).','bilgi'),
          ('A ile ters yönde, 4 tur','Tur sayısını doğru bulmuş; ancak iki dişli çifti arasında yönün iki kez değiştiğini görmemiş.','dikkat')],
  sira=['A ile aynı yönde, 1 tur','A ile ters yönde, 2 tur','A ile aynı yönde, 2 tur','A ile ters yönde, 4 tur','A ile aynı yönde, 4 tur'],
  istenen='D dişlisinin dönüş yönü ve tur sayısı.',ip=['Önce A’dan B’ye geç; ortak eksenli dişlinin turunu B ile karşılaştır, sonra C’den D’ye ilerle.'],
  bilgi=[B('Geçmiş dişliler','birbirine geçmiş dişlilerde diş sayısı × tur sayısı eşittir ve dişliler zıt yönde döner. Örnek: 20 dişli 3 tur atarsa 60 dişli ona geçmişse 1 tur atar'),
         B('Ortak eksen','aynı eksene bağlı dişliler birlikte döner; tur sayıları ve dönme yönleri aynıdır, diş sayıları farklı olabilir')],
  puf='Dişli zincirinde iki geçiş yönü eski haline getirir; ortak eksenli dişli sayıyı değiştirmez, yalnız diş oranını değiştirir.',sekil=SK[10])

# 11 · dişli öncüllü · orta (B)
X_,Y_=12,24
rX,rY=X_*KD,Y_*KD
f11=[gear(0,0,X_,'gray!25'),gear(rX+rY,0,Y_,'gray!12'),cw_arrow(0,0,rX),f'\\node[align=center] at (0,0) {{X\\\\${X_}$ diş}};',f'\\node[align=center] at ({rX+rY:.3f},0) {{Y\\\\${Y_}$ diş}};']
SK[11]=fig(f11)
st11=[('Y dişlisinin açısal hızı, X dişlisinin açısal hızından küçüktür.',True,'diş sayısı × açısal hız çarpımı eşittir; Y’nin diş sayısı X’in 2 katı olduğundan açısal hızı X’in yarısıdır','24 × ω_Y = 12 × ω_X'),
      ('Dişlilerin birbirine değdiği noktalardaki çizgisel hızlar eşittir.',True,'dişliler kaymadan döndüğü için temas noktasındaki çizgisel hızlar eşit olur','v_X = v_Y'),
      ('X ve Y dişlileri aynı yönde döner.',False,'birbirine geçmiş dişliler zıt yönde döner','X saat yönünde ise Y ters yönde')]
m11,d11,s11,y11=oncul(st11,1)
q('0011',oncul_adim(st11,('Verileri oku','Y dişlisinin diş sayısı X’inkinin iki katıdır.','24 = 2 × 12'),('Doğru yargıları seç','I ve II doğrudur.','I ve II')),
  tipId='bm-disli',tip='Dişlilerde tur sayısı ve dönüş yönü',z='orta',alt='Dişli Sistemleri',kaz='Birbirine geçmiş dişlilerin açısal hız, çizgisel hız ve dönüş yönü ilişkisini yorumlar.',kalip='öncüllü',
  kart='K-AFMAK-05 (dişli, diş × tur) · açısal–çizgisel hız yorumu',
  metin='Şekilde birbirine geçmiş X ve Y dişlileri görülmektedir. X dişlisi, okla gösterilen yönde sabit açısal hızla döndürülmektedir ve dişliler kaymadan dönmektedir. Diş sayıları şekilde verilmiştir.\nBuna göre,\n'+m11+'\nyargılarından hangileri doğrudur?',
  dogru=d11,yan=y11,sira=s11,
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Temas noktasında dişlilerin birbirine göre kayıp kaymadığını ve diş sayısının dönüşe etkisini düşün.'],
  bilgi=[B('Dişli oranı','geçmiş iki dişlide diş sayısı büyük olan daha yavaş döner: N₁·ω₁ = N₂·ω₂. Örnek: 10 dişli dişli 30 dişliye geçmişse 30 dişli üçte biri hızla döner'),
         B('Çizgisel hız','kaymadan dönen dişlilerin temas noktasında çizgisel hızlar eşittir; ancak açısal hızlar yarıçapla ters orantılıdır')],
  puf='Geçmiş dişlilerde çizgisel hız ortak, açısal hız yarıçapla ters orantılı, yön zıttır.',sekil=SK[11])

# 12 · bisiklet · orta (D)
rw,rs,rp=1.3,16*.0185,48*.0185; dpc=3.2
psi=acos((rs-rp)/dpc)
def tg(sg): return (rs*cos(psi),sg*rs*sin(psi)),(dpc+rp*cos(psi),sg*rp*sin(psi))
(p1,p2),(p3,p4)=tg(1),tg(-1)
a_=2*pi*rs*28.4528/32; b_=2*pi*rp*28.4528/96
f12=[f'\\draw[very thick] ({-rw-.5:.2f},{-rw:.2f}) -- ({dpc+rp+.6:.2f},{-rw:.2f});',
     f'\\draw[thick] (0,0) circle ({rw}); \\draw[thin] (0,0) circle ({rw-.12});',
     f'\\fill[gray!15] (0,0) circle ({rs}); \\draw[line width=2.2pt,gray!70,dash pattern=on {a_:.2f}pt off {a_:.2f}pt] (0,0) circle ({rs});\\fill (0,0) circle (1.4pt);',
     f'\\fill[gray!15] ({dpc},0) circle ({rp}); \\draw[line width=2.6pt,gray!70,dash pattern=on {b_:.2f}pt off {b_:.2f}pt] ({dpc},0) circle ({rp});\\fill ({dpc},0) circle (1.4pt);',
     f'\\draw[thick] ({p1[0]:.3f},{p1[1]:.3f}) -- ({p2[0]:.3f},{p2[1]:.3f}); \\draw[thick] ({p3[0]:.3f},{p3[1]:.3f}) -- ({p4[0]:.3f},{p4[1]:.3f});',
     f'\\draw[very thick] ({dpc},0) -- ({dpc+.15:.2f},{-rp-.35:.2f}); \\draw[fill=gray!60] ({dpc+.15-.25:.2f},{-rp-.35-.05:.2f}) rectangle ({dpc+.15+.25:.2f},{-rp-.35+.05:.2f});',
     f'\\node[above] at (0,{rw+.05:.2f}) {{tekerlek}};',f'\\node[above] at ({dpc},{rp+.05:.2f}) {{pedal dişlisi: $48$ diş}};',f'\\node[below] at (0,{-rs-.08:.2f}) {{$16$ diş}};']
SK[12]=fig(f12)
tur12=5*Fr(48,16); yol12=tur12*2*3*Fr(4,10); assert (tur12,yol12)==(15,36)
assert 5*Fr(16,48)*2*3*Fr(4,10)==4 and 5*2*3*Fr(4,10)==12 and tur12*3*Fr(4,10)==18 and tur12*2*3*Fr(8,10)==72
q('0012',[A('Arka dişlinin turunu bul','Zincirle bağlı dişlilerde diş sayısı × tur sayısı eşittir.','48 × 5 = 16 × n → n = 15 tur'),
          A('Tekerleğin turunu bul','Arka dişli ile tekerlek ortak eksenlidir; aynı sayıda tur atar.','n_tekerlek = 15'),
          A('Yolu hesapla','Kaymadan dönen tekerlek bir turda çevresi kadar yol alır.','2πr = 2 × 3 × 0,4 = 2,4 m → 15 × 2,4 = 36 m')],
  tipId='bm-disli',tip='Dişlilerde tur sayısı ve dönüş yönü',z='orta',alt='Dişli Sistemleri',kaz='Zincirli dişli sisteminde pedal turundan tekerleğin aldığı yolu hesaplar.',kalip='şekilli',
  kart='K-AFMAK-05 (dişli, diş × tur) · zincir, ortak eksenli tekerlek',
  metin='Şekilde bir bisikletin pedal dişlisi, arka dişlisi ve arka tekerleği görülmektedir. Pedal dişlisi zincirle arka dişliyi döndürmektedir; arka dişli ile tekerlek ortak eksenlidir. Diş sayıları şekilde verilmiştir. Tekerleğin yarıçapı 0,4 m’dir ve tekerlek kaymadan ilerlemektedir. (π = 3)\nBuna göre, pedal dişlisi 5 tur döndürüldüğünde bisiklet kaç m yol alır?',
  dogru=36,yan=[(4,'Diş oranını ters kullanmış: 5 × 16 ÷ 48 = 5/3 tur; yol = 5/3 × 2,4 = 4 m.','islem'),
                (12,'Pedalın turunu doğrudan tekerleğin turu sanmış: 5 × 2,4 = 12 m.','bilgi'),
                (18,'Çevreyi 2πr yerine πr almış: 15 × 1,2 = 18 m.','islem'),
                (72,'Yarıçap yerine çapı (0,8 m) kullanmış: 15 × 2 × 3 × 0,8 = 72 m.','dikkat')],
  istenen='Bisikletin aldığı yol (m).',ip=['Önce pedal dişlisinin turundan arka dişlinin turunu bul; tekerleğin turu ona eşittir.'],
  bilgi=[B('Zincirli dişli','zincirle bağlı iki dişlide zincir aynı hızla hareket eder; N₁·n₁ = N₂·n₂ ve dişliler aynı yönde döner. Örnek: 40 dişli 2 tur atarsa 10 dişli 8 tur atar'),
         B('Kaymadan yuvarlanma','tekerlek bir tam turda çevresi 2πr kadar yol alır. Örnek: r = 0,5 m, π = 3 için bir turda 3 m')],
  puf='Pedalda diş çok, arka dişlide az olduğundan tekerlek pedaldan çok daha fazla döner; yol kazancı kuvvet kaybı demektir.',sekil=SK[12])

# 13 · grafik · orta (B)
g13=r'''\begin{tikzpicture}[font=\small]
\begin{axis}[width=6.4cm,height=6cm,xmin=0,xmax=100,ymin=0,ymax=100,xtick={0,20,40,60,80,100},ytick={0,10,20,30,40,50,60,70,80,90,100},yticklabel style={font=\footnotesize},grid=both,minor tick num=0,xlabel={Harcanan iş (J)},ylabel={Yararlı iş (J)},every axis label/.append style={font=\small}]
\addplot[thick,vurgu] coordinates {(0,0)(100,80)}; \addplot[thick,black,dashed] coordinates {(0,0)(100,50)};
\node[vurgu,above] at (axis cs:78,70) {X}; \node[below right] at (axis cs:70,32) {Y};
\addplot[only marks,mark=*,mark size=1.6pt,vurgu] coordinates {(100,80)}; \addplot[only marks,mark=*,mark size=1.6pt,black] coordinates {(100,50)};
\end{axis}\end{tikzpicture}'''
SK[13]=tikz_svg(g13)
eX,eY=Fr(4,5),Fr(1,2); tY=Fr(60)/eY; tX=Fr(60)/eX; assert (tY,tX,tY-tX)==(120,75,45) and 60*(eX-eY)==18 and tY-60==60
q('0013',[A('Verimleri oku','Doğrunun eğimi verimi verir; x = 100 J için yararlı işleri oku.','η_X = 80 ÷ 100 = 0,8 · η_Y = 50 ÷ 100 = 0,5'),
          A('Y’ye verilen işi bul','Yararlı iş 60 J olacak biçimde harcanan işi hesapla.','W_Y = 60 ÷ 0,5 = 120 J'),
          A('X’e verilen işi bul','Aynı yararlı iş için X’in harcayacağı iş.','W_X = 60 ÷ 0,8 = 75 J'),
          A('Farkı al','İki harcanan işin farkı istenir.','120 − 75 = 45 J')],
  tipId='bm-grafik',tip='Grafikten verim ve kuvvet bulma',z='orta',alt='Verim',kaz='İş–iş grafiğinde doğruların eğiminden verimi bulup harcanan işleri karşılaştırır.',kalip='grafik',
  kart='K-AFMAK-07 (grafikle makine analizi) · yararlı iş – harcanan iş doğruları',
  metin='X ve Y basit makinelerinin yaptığı yararlı iş, makinelere verilen (harcanan) işe bağlı olarak şekildeki grafikte gösterilmiştir.\nBuna göre, Y makinesinin 60 J yararlı iş yapması için verilen iş, X makinesinin aynı yararlı işi yapması için verilen işten kaç J fazladır?',
  dogru=45,yan=[(18,'Verimlerin farkını (0,8 − 0,5 = 0,3) 60 J ile çarpıp iş farkı sanmış.','islem'),
                (60,'Y’nin yararlı işi ile harcadığı işin farkını (120 − 60) almış.','dikkat'),
                (75,'Yalnız X’e verilen işi (60 ÷ 0,8) bulup Y ile karşılaştırmamış.','dikkat'),
                (120,'Yalnız Y’ye verilen işi (60 ÷ 0,5) bulmuş, X’inkini çıkarmamış.','dikkat')],
  istenen='Y ile X makinelerine verilen işlerin farkı (J).',ip=['Her doğrunun eğimi, o makinenin harcadığı işin ne kadarını yararlı işe çevirdiğini söyler.'],
  bilgi=[B('Yararlı iş grafiği','yararlı iş – harcanan iş doğrusunun eğimi verimi verir. Örnek: eğimi 0,6 olan makinede 50 J harcanırsa 30 J yararlı iş elde edilir')],
  puf='Yararlı iş – harcanan iş grafiğinde eğim = verim; eğimi küçük olan makine aynı yararlı iş için daha çok iş harcar.',sekil=SK[13])

# 14 · grafik makara verim · zor (B)
g14=r'''\begin{tikzpicture}[font=\small]
\begin{axis}[width=6.4cm,height=5.8cm,xmin=0,xmax=60,ymin=0,ymax=40,xtick={0,20,40,60},ytick={0,10,20,30,40},grid=both,xlabel={$G$ (N)},ylabel={$F$ (N)},every axis label/.append style={font=\small}]
\addplot[thick,vurgu] coordinates {(0,10)(60,40)};
\addplot[only marks,mark=*,mark size=1.8pt,vurgu] coordinates {(20,20)(60,40)};
\end{axis}\end{tikzpicture}'''
SK[14]=tikz_svg(g14)
Gm=20; Fg=lambda G:Fr(G+Gm,2); assert Fg(20)==20 and Fg(60)==40 and Fg(0)==10 and Fg(80)==50
eta14=Fr(80,2*Fg(80)); assert eta14==Fr(4,5) and Fr(Fg(80),80)*100==Fr(125,2) and 80*100//100==80 and Fr(100,80)*100==125 and Fr(80,Fg(80))*100==160
q('0014',[A('Doğrunun denklemini bul','Grafikteki iki noktadan eğim ve kesim noktası okunur.','eğim = (40 − 20) ÷ (60 − 20) = 0,5 · F = 0,5G + 10'),
          A('Kuvveti hesapla','G = 80 N için grafiği aynı doğruyla uzat.','F = 0,5 × 80 + 10 = 50 N'),
          A('Yararlı ve harcanan işi karşılaştır','İp, yükten 2 kat fazla yol alır; yük h yükselirken ip 2h çekilir.','W_yararlı = 80h · W_toplam = 50 × 2h = 100h'),
          A('Verimi bul','Verim, yararlı işin harcanan işe oranıdır.','η = 80h ÷ 100h = 0,8 → %80')],
  tipId='bm-grafik',tip='Grafikten verim ve kuvvet bulma',z='zor',alt='Verim',kaz='Kuvvet–yük grafiğinden hareketli makaralı sistemin kuvvetini bulur ve verimini hesaplar.',kalip='grafik',
  kart='K-AFMAK-07 (grafikle makine analizi) · F–G doğrusu, ağırlıklı hareketli makara',
  metin='Bir sabit ve bir hareketli makaradan oluşan bir sistemde, hareketli makara bloğunun ağırlığı önemsiz değildir; ip ve sabit makara ağırlıksızdır, sürtünmeler önemsizdir. Yükü iki ip kolu taşımaktadır; yararlı iş, yükün potansiyel enerji artışıdır. Yükün ağırlığı G değiştirilerek yükü sabit hızla yükselten F kuvveti ölçülmüş ve şekildeki grafik çizilmiştir. Grafikteki doğrusal ilişkinin G = 80 N için de geçerli olduğu bilinmektedir.\nBuna göre, G = 80 N’luk yük için sistemin verimi yüzde kaçtır?',
  dogru=80,yan=[(62.5,'F ÷ G oranını (50 ÷ 80 = 0,625) verim yapmış.','islem'),
                (100,'Sistemin ideal olduğunu varsayıp hareketli makaranın ağırlığını yok saymış.','dikkat'),
                (125,'Oranı ters yazmış: harcanan iş ÷ yararlı iş = 100 ÷ 80 = 1,25.','islem'),
                (160,'Yük ÷ kuvvet oranını (80 ÷ 50 = 1,6) doğrudan verim sanmış; ip yolunun 2 katı olduğunu hesaba katmamış.','bilgi')],
  istenen='G = 80 N için sistemin verimi (%).',ip=['Doğrunun hangi noktalarından geçtiğine bakarak F ile G arasındaki bağıntıyı yaz; sonra yararlı işi ve harcanan işi karşılaştır.'],
  bilgi=[B('Doğrusal grafik','iki noktası bilinen doğrunun eğimi (Δy ÷ Δx), kesim noktası y eksenini kestiği değerdir. Örnek: (10, 12) ve (30, 22) noktalarından geçen doğrunun eğimi 0,5’tir'),
         B('Makara verimi','n kollu sistemde ip ucu yükün n katı yol alır; η = G ÷ (n·F). Örnek: n = 2, G = 60 N, F = 40 N ise η = 0,75')],
  puf='Kuvvet–yük grafiğinde doğru orijinden geçmiyorsa makara ya da blok ağırlığı vardır; verim yük büyüdükçe artar.',sekil=SK[14])

# 15 · kavram öncüllü · kolay (E)
st15=[('Kuvvetten kazanç sağlayan her basit makine aynı zamanda yoldan da kazanç sağlar.',False,'kuvvetten kazanç, yoldan kayıpla birlikte gelir; iş değişmez (W = F·x)','F azalır, x artar'),
      ('Sürtünmeli bir eğik düzlemde yükü sabit hızla çıkarmak için gereken kuvvet, sürtünmesiz duruma göre büyüktür.',True,'sürtünme kuvveti de hareket yönünün tersine etki ettiğinden, düzleme paralel çekme kuvveti büyür','F = G·h/l + f'),
      ('Bir basit makinenin verimi, yararlı işin harcanan işe oranıdır ve sürtünme varsa 1’den küçüktür.',True,'sürtünmeyle bir miktar iş ısıya dönüşür; yararlı iş harcanan işten küçük kalır','η = W_yararlı ÷ W_harcanan < 1')]
m15,d15,s15,y15=oncul(st15,4)
q('0015',oncul_adim(st15,('Kavramları hatırla','Basit makineler işi artırmaz; yalnız kuvvetin büyüklüğünü ya da yönünü değiştirir.','W = F × x'),('Doğru yargıları seç','II ve III doğrudur.','II ve III')),
  tipId='bm-kavram',tip='Basit makinelerde kuvvet–yol–iş ilişkisi',z='kolay',alt='Basit Makine Kavramları',kaz='Basit makinelerde kuvvet, yol, iş ve verim kavramlarını yorumlar.',kalip='öncüllü',
  kart='K-AFMAK-08 (basit makine kavramları) · kuvvet–yol–iş–verim yargıları',
  metin='Basit makineler günlük yaşamda yükleri daha kolay kaldırmak ya da taşımak için kullanılır.\nBuna göre, basit makinelerle ilgili,\n'+m15+'\nyargılarından hangileri doğrudur?',
  dogru=d15,yan=y15,sira=s15,
  istenen='Doğru olan yargıların belirlenmesi.',ip=['İş = kuvvet × yol bağıntısını ve sürtünme varlığında işin nereye gittiğini düşün.'],
  bilgi=[B('İş ve basit makine','basit makineler iş kazancı sağlamaz; kuvvet kazancı yol kaybıyla, yol kazancı kuvvet kaybıyla dengelenir. Örnek: kuvvet yarıya inerse yol iki katına çıkar'),
         B('Verim','η = yararlı iş ÷ harcanan iş; sürtünmesiz (ideal) makinede 1, gerçek makinede 1’den küçüktür')],
  puf='Basit makine işi değil, kuvvetle yolun çarpımını paylaştırır; kayıp varsa verim 1’in altındadır.',sekil=None)

# 16 · çıkrık + verim · zor (C)
SK[16]=fig([cikrik(50,10,.05,'$400$ N','$R=50$ cm','$r=10$ cm')])
R16,r16,G16,eta16=50,10,400,Fr(4,5); F0=Fr(G16*r16,R16); F16=F0/eta16
assert (F0,F16)==(80,100) and F0*eta16==64 and F0/eta16**2==125 and Fr(G16)/eta16==500
q('0016',[A('Verimsiz çıkrığı düşün','Sürtünme yokken denge: F₀ × R = G × r.','F₀ = (400 × 10) ÷ 50 = 80 N'),
          A('Verim bağıntısını yaz','Silindir h yükselirken kol, kuvvet doğrultusunda h × R ÷ r kadar yol alır.','η = (G × h) ÷ (F × h × R ÷ r) = F₀ ÷ F'),
          A('F’yi çöz','Gerçek kuvvet, ideal kuvvetin 1/η katıdır.','F = 80 ÷ 0,8 = 100 N')],
  tipId='bm-verim',tip='Verim hesabı',z='zor',alt='Verim',kaz='Çıkrıkta ideal kuvvetle verimi birleştirerek gerçek kuvveti bulur.',kalip='şekilli',
  kart='K-AFMAK-06 (verim) · çıkrık + verim, iki kavram',
  metin='Şekildeki çıkrıkla yük, kolun ucuna dik uygulanan F kuvvetiyle sabit hızla yükseltilmektedir. Kol uzunluğu, silindirin yarıçapı ve yükün ağırlığı şekilde verilmiştir. İp ağırlıksızdır ve çıkrığın verimi %80’dir.\nBuna göre, F kuvveti kaç N’dur?',
  dogru=100,yan=[(64,'Verimi ideal kuvvetle çarpmış: 80 × 0,8 = 64 N.','islem'),
                 (80,'Verimi hesaba katmamış; sürtünmesiz çıkrığın kuvvetini (80 N) bulmuş.','dikkat'),
                 (125,'Verimle iki kez bölmüş: 80 ÷ 0,8 ÷ 0,8 = 125 N.','islem'),
                 (500,'Yükü doğrudan verime bölmüş: 400 ÷ 0,8 = 500 N; çıkrığın kuvvet kazancını unutmuş.','bilgi')],
  istenen='Yükü sabit hızla çeken F kuvvetinin büyüklüğü (N).',ip=['Önce sürtünmesiz çıkrık için gereken kuvveti bul; verimli makinede bu kuvvet yeterli olur mu?'],
  bilgi=[B('Çıkrıkta verim','gerçek F kuvveti, ideal F₀ = G·r ÷ R kuvvetinden büyüktür: F = F₀ ÷ η. Örnek: F₀ = 30 N, η = 0,6 ise F = 50 N'),
         B('İş ve verim','η = yararlı iş ÷ harcanan iş; verimi küçük makinede aynı yükü kaldırmak için daha büyük kuvvet gerekir')],
  puf='Verim hesaplı sorularda önce ideal (sürtünmesiz) kuvveti bul, sonra verimle böl: F = F₀ ÷ η.',sekil=SK[16])

# 17 · kaldıraç öncüllü · zor (D)
w=dict(X=(40,1),Y=(30,6),Z=(20,7)); xf=4
def tork(w,xf):
    L=sum(F*(xf-x) for F,x in w.values() if x<xf); R=sum(F*(x-xf) for F,x in w.values() if x>xf); return L,R
assert tork(w,xf)==(120,120)
w1={k:(F,x+1 if x<xf else x-1) for k,(F,x) in w.items()}; L1,R1=tork(w1,xf); assert L1>R1 and (L1,R1)==(80,70)
assert tork({k:(2*F,x) for k,(F,x) in w.items()},xf)==(240,240)
w3=dict(X=w['X'],Y=(30,7),Z=(20,6)); L3,R3=tork(w3,xf); assert (L3,R3)==(120,130) and L3!=R3
f17=[lever(u=1.0,items=[('box',1,'\\scriptsize $X$\\\\$40$ N'),('box',6,'\\scriptsize $Y$\\\\$30$ N'),('box',7,'\\scriptsize $Z$\\\\$20$ N')],x0=0,x1=8,xf=4)]
SK[17]=fig(f17)
st17=[('Üç yükün hepsi mesnede doğru 1 bölme kaydırılırsa çubuk, X yükünün bulunduğu taraftan aşağı döner.',True,'kaydırma sonrası sol tork 40 × 2 = 80, sağ tork 30 × 1 + 20 × 2 = 70 olur; sol taraf ağır basar','sol: 80 · sağ: 70'),
      ('Üç yükün ağırlıkları da iki katına çıkarılırsa çubuk dengede kalır.',True,'tork toplamlarının ikisi de iki katına çıkar (240 = 240), oran değişmez','sol: 240 · sağ: 240'),
      ('Y ve Z yükleri birbiriyle yer değiştirirse çubuk dengede kalır.',False,'yer değiştirince sağ tork 30 × 3 + 20 × 2 = 130 olur; sol tork 120 kalır','sol: 120 · sağ: 130')]
m17,d17,s17,y17=oncul(st17,3)
q('0017',oncul_adim(st17,('Başlangıç dengesini kontrol et','Mesnetten kolları oku ve torkları hesapla.','sol: 40 × 3 = 120 · sağ: 30 × 2 + 20 × 3 = 120'),('Doğru yargıları seç','I ve II doğrudur.','I ve II')),
  tipId='bm-kaldirac',tip='Kaldıraçta tork dengesi ve kuvvet kazancı',z='zor',alt='Kaldıraç',kaz='Dengedeki kaldıraçta yük konumları ya da ağırlıkları değişince tork dengesinin nasıl bozulduğunu değerlendirir.',kalip='öncüllü',
  kart='K-AFMAK-02 (kaldıraç tork dengesi) · üç yük, konum/ağırlık değişimi',
  metin='Ağırlıksız çubuk, bölmeleri eşit aralıklı olacak biçimde şekildeki gibi mesnet üzerinde yatay dengededir. X, Y ve Z yüklerinin ağırlıkları şekilde verilmiştir.\nBuna göre,\n'+m17+'\nyargılarından hangileri doğrudur?',
  dogru=d17,yan=y17,sira=s17,
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Her yargıdaki değişiklikten sonra mesnede göre sol ve sağ tork toplamlarını yeniden hesapla.'],
  bilgi=[B('Denge bozulursa','çubuk, tork toplamı büyük olan taraftan aşağı döner. Örnek: sol tork 60, sağ tork 50 N·bölme ise çubuk soldan aşağı iner'),
         B('Tork ve ağırlık','tüm ağırlıklar aynı oranda değişirse iki tork toplamı da aynı oranda değişir; denge korunur')],
  puf='Dengeli çubukta ağırlıkları aynı oranda değiştirmek dengeyi bozmaz; konum değişimi ise torkların oranını değiştirir.',sekil=SK[17])

# 18 · iki palanga öncüllü · orta (A)
f18=[palanga(3,off=0,load='$90$ N',name='X',flab='F_X'),palanga(2,off=3.4,load='$90$ N',blok='makara\\\\$10$ N',name='Y',flab='F_Y')]
SK[18]=fig(f18)
FX=Fr(90,3); FY=Fr(90+10,2); assert (FX,FY)==(30,50) and FX*3==90 and FY*2==100
st18=[('F_X kuvveti, F_Y kuvvetinden küçüktür.',True,'X’te üç kol 90 N’u taşıdığından F_X = 30 N; Y’de iki kol 90 + 10 = 100 N’u taşıdığından F_Y = 50 N','30 N < 50 N'),
      ('Yükler h kadar yükseltilirken iki düzenekte de ip ucu aynı miktarda çekilir.',False,'ip ucu X’te 3h, Y’de 2h çekilir; çünkü ip yolu taşıyan kol sayısı kadar katlanır','3h ≠ 2h'),
      ('Yükler h kadar yükseltilirken F_X ve F_Y kuvvetlerinin yaptığı işler eşittir.',False,'W_X = 30 × 3h = 90h; W_Y = 50 × 2h = 100h; Y’de makaranın da yükseltilmesi için ek iş gerekir','90h ≠ 100h')]
m18,d18,s18,y18=oncul(st18,0)
q('0018',oncul_adim(st18,('Kuvvetleri hesapla','Taşıyan ip kollarını sayıp her düzenek için F’yi bul.','F_X = 90 ÷ 3 = 30 N · F_Y = (90 + 10) ÷ 2 = 50 N'),('Doğru yargıyı seç','Yalnız I doğrudur.','Yalnız I')),
  tipId='bm-makara',tip='Makara ve palanga sistemlerinde kuvvet kazancı',z='orta',alt='Makara Sistemleri',kaz='İki makara düzeneğinde kuvvet, ip yolu ve iş ilişkisini karşılaştırır.',kalip='öncüllü',
  kart='K-AFMAK-01 (makara, ip sayısı) · iki düzeneğin karşılaştırılması',
  metin='Şekildeki X ve Y düzenekleriyle özdeş yükler sabit hızla yükseltilmektedir. İplerin, X’teki makaraların ve sabit makaraların ağırlıkları önemsizdir; Y düzeneğindeki hareketli makaranın ağırlığı şekilde verilmiştir. Sürtünmeler önemsizdir.\nBuna göre,\n'+m18+'\nyargılarından hangileri doğrudur?',
  dogru=d18,yan=y18,sira=s18,
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Her düzenekte yükü (ve varsa makarayı) taşıyan ip kollarını say; ip yolu ve iş için bu sayıyı kullan.'],
  bilgi=[B('Palanga yolu','n kollu düzenekte yük h yükselirken ip ucu n·h kadar çekilir. Örnek: 4 kollu sistemde yük 0,5 m yükselirse ip ucu 2 m çekilir'),
         B('İş','F’nin yaptığı iş W = F × (ip yolu) kadardır; hareketli makara da yükseltildiği için ağırlığı işe katılır')],
  puf='Makarada kuvvetten kazanç ip yolunun uzamasıyla ödenir; hareketli makaranın ağırlığı varsa harcanan iş yararlı işten büyük olur.',sekil=SK[18])

# 19 · iki eğik düzlem öncüllü · orta (E)
h19=1.4
f19=[incline(0,4.4,h19,.6,.6,.4,'','$F_K$',.8,name='K'),incline(5.6,1.8,h19,.55,.6,.4,'','$F_L$',.8,name='L'),
     f'\\draw[dashed,thin] (4.4,{h19}) -- (7.4,{h19}); \\draw[<->,thin] (7.55,0) -- (7.55,{h19}); \\node[right] at (7.55,{h19/2}) {{$h$}};',
     '\\draw (-.4,0) -- (8.0,0);']
SK[19]=fig(f19)
st19=[('F_K, F_L’den küçüktür.',True,'sürtünme yokken F = G·h ÷ l’dir; K’nin boyu daha uzun olduğundan F_K daha küçüktür','l_K > l_L → F_K < F_L'),
      ('Cismin çıkarılması sırasında K’de yapılan iş, L’de yapılandan küçüktür.',False,'sürtünme yokken iki düzlemde de iş cismin potansiyel enerji artışına, yani G·h’a eşittir','W_K = W_L = G·h'),
      ('Cismin çıkarılması sırasında K’de alınan yol, L’de alınandan büyüktür.',True,'K’nin boyu L’nin boyundan uzundur ve cisim düzlem boyunca ilerler','l_K > l_L')]
m19,d19,s19,y19=oncul(st19,4)
q('0019',oncul_adim(st19,('Verileri oku','İki düzlemin yüksekliği aynıdır; K’nin boyu L’ninkinden uzundur.','h aynı · l_K > l_L'),('Doğru yargıları seç','I ve III doğrudur.','I ve III')),
  tipId='bm-egik',tip='Eğik düzlemde kuvvet, yol ve iş',z='orta',alt='Eğik Düzlem',kaz='Aynı yüksekliğe çıkan iki eğik düzlemde kuvvet, yol ve iş ilişkisini karşılaştırır.',kalip='öncüllü',
  kart='K-AFMAK-04 (eğik düzlem, F·l = G·h) · iki düzlem karşılaştırma',
  metin='Sürtünmesiz K ve L eğik düzlemlerinde özdeş cisimler, düzeye paralel F_K ve F_L kuvvetleriyle sabit hızla aynı h yüksekliğine çıkarılmaktadır.\nBuna göre,\n'+m19+'\nyargılarından hangileri doğrudur?',
  dogru=d19,yan=y19,sira=s19,
  istenen='Doğru olan yargıların belirlenmesi.',ip=['Sürtünme yokken yükü h kadar yükseltmek için gereken iş eğik düzlemin biçimine bağlı mıdır?'],
  bilgi=[B('Eğik düzlem','sürtünmesizken F × l = G × h; aynı yüksekliğe çıkarken uzun düzlem daha küçük kuvvet ister, ancak yapılan iş değişmez. Örnek: h = 1 m, l = 4 m için F = G ÷ 4')],
  puf='Eğik düzlemin boyu uzadıkça kuvvet azalır, yol artar; iş aynı kalır.',sekil=SK[19])

# 20 · eğik düzlem + makara · zor (A)
th=radians(37); u=(.8,.6); n=(-.6,.8); b,hh=4.0,3.0; hb=.5; bw=.8; r=.3; rm=.35; sp=.6
Tc=(b,hh); S=(2.2*u[0],2.2*u[1])
cbl=[(S[0]-u[0]*bw/2,S[1]-u[1]*bw/2),(S[0]+u[0]*bw/2,S[1]+u[1]*bw/2)]; cbl+=[(cbl[1][0]+n[0]*hb,cbl[1][1]+n[1]*hb),(cbl[0][0]+n[0]*hb,cbl[0][1]+n[1]*hb)]
face=(S[0]+u[0]*bw/2+n[0]*hb/2,S[1]+u[1]*bw/2+n[1]*hb/2)
C=(Tc[0]+n[0]*(hb/2-r)+u[0]*sp,Tc[1]+n[1]*(hb/2-r)+u[1]*sp); Tp=(C[0]+n[0]*r,C[1]+n[1]*r)
assert abs((Tp[1]-face[1])*u[0]-(Tp[0]-face[0])*u[1])<1e-9
Mx=C[0]+r+rm; My=C[1]-1.6; ytop=C[1]+.85
f20=[f'\\draw (-.4,0) -- (6.9,0);',f'\\draw[thick] (0,0) -- (4,0) -- (4,3) -- cycle;',
     '\\draw[thick,fill=gray!25] '+' -- '.join(f'({p[0]:.3f},{p[1]:.3f})' for p in cbl)+' -- cycle;',
     f'\\node[rotate=36.9,font=\\scriptsize] at ({S[0]+n[0]*hb/2:.3f},{S[1]+n[1]*hb/2:.3f}) {{$50$ N}};',
     f'\\draw ({Tc[0]},{Tc[1]}) -- ({C[0]:.3f},{C[1]:.3f}); \\draw[fill=white] ({C[0]:.3f},{C[1]:.3f}) circle ({r}); \\fill ({C[0]:.3f},{C[1]:.3f}) circle (1.3pt);',
     f'\\draw[thick] ({face[0]:.3f},{face[1]:.3f}) -- ({Tp[0]:.3f},{Tp[1]:.3f}) arc[start angle={degrees(atan2(n[1],n[0])):.2f},end angle=0,radius={r}] -- ({C[0]+r:.3f},{My:.3f});',
     f'\\draw[fill=white] ({Mx:.3f},{My:.3f}) circle ({rm}); \\fill ({Mx:.3f},{My:.3f}) circle (1.3pt);',
     f'\\draw[thick] ({C[0]+r:.3f},{My:.3f}) arc[start angle=180,end angle=360,radius={rm}] -- ({Mx+rm:.3f},{ytop:.3f});',
     hatch(Mx-.3,Mx+rm+.5,ytop),
     f'\\draw ({Mx:.3f},{My-rm:.3f}) -- ({Mx:.3f},{My-rm-.45:.3f}); \\draw[fill=gray!25,thick] ({Mx-.45:.3f},{My-rm-.45:.3f}) rectangle ({Mx+.45:.3f},{My-rm-1.0:.3f}); \\node at ({Mx:.3f},{My-rm-.725:.3f}) {{$P$}};',
     f'\\node[right,align=left] at ({Mx+rm+.08:.3f},{My:.3f}) {{makara\\\\$10$ N}};',
     f'\\draw (.8,0) arc[start angle=0,end angle=36.87,radius=.8]; \\node at (1.1,.25) {{$37^\\circ$}};']
SK[20]=fig(f20)
Gbl=50; T20=Fr(Gbl*3,5); Pp=2*T20-10; assert (T20,Pp)==(30,50) and 2*T20==60 and 2*Gbl-10==90 and 2*Gbl==100 and 2*Gbl+10==110
q('0020',[A('İp gerilmesini bul','Cisim sürtünmesiz düzlemde dengede; ip düzleme paralel olduğundan T, ağırlığın düzleme paralel bileşenine eşittir.','T = G × sin37° = 50 × 0,6 = 30 N'),
          A('Makaraya uygula','İpin aynı gerilmesi iki kolu boyunca etki eder; hareketli makara ve P onların taşıdığı toplam ağırlıktır.','2T = P + G_makara → 60 = P + 10'),
          A('P’yi çöz','Denklemden P bulunur.','P = 50 N')],
  tipId='bm-egik',tip='Eğik düzlemde kuvvet, yol ve iş',z='zor',alt='Eğik Düzlem ve Makara',kaz='Eğik düzlem ile hareketli makarayı birleştirip dengedeki sistemde asılı yükü bulur.',kalip='şekilli',
  kart='K-AFMAK-04 (eğik düzlem, F·l = G·h) · eğik düzlem + hareketli makara birleşimi',
  metin='Şekildeki sistem dengededir. Eğik düzlem sürtünmesizdir; ip ve sabit makara ağırlıksızdır, ip eğik düzleme paraleldir. Cismin ve hareketli makaranın ağırlıkları şekilde verilmiştir. (sin 37° = 0,6; cos 37° = 0,8)\nBuna göre, P yükünün ağırlığı kaç N’dur?',
  dogru=50,yan=[(60,'Hareketli makaranın ağırlığını hesaba katmamış: P = 2T = 60 N.','dikkat'),
                (90,'Eğimi hesaba katmayıp T = 50 N almış: P = 2 × 50 − 10 = 90 N.','bilgi'),
                (100,'Hem eğimi hem makara ağırlığını yok saymış: P = 2 × 50 = 100 N.','dikkat'),
                (110,'T = 50 N alıp makara ağırlığını ters işaretle eklemiş: P = 2 × 50 + 10 = 110 N.','islem')],
  istenen='Dengeyi sağlayan P yükünün ağırlığı (N).',ip=['Önce eğik düzlemdeki cismi dengede tutan ip gerilmesini bul; sonra hareketli makaraya kaç ip kolunun etki ettiğine bak.'],
  bilgi=[B('Eğik düzlemde denge','sürtünmesizken ipin gerilmesi, ağırlığın düzleme paralel bileşenine eşittir: T = G·sinθ. Örnek: G = 20 N, sinθ = 0,5 ise T = 10 N'),
         B('Hareketli makara','ideal ipte gerilme her yerde aynıdır; hareketli makara ve yükü iki kolla taşınır: 2T = yük + makara ağırlığı')],
  puf='Birleşik sistemlerde ipin gerilmesi ortak büyüklüktür; önce bir tarafı çöz, sonra aynı T’yi öbür tarafa taşı.',sekil=SK[20])

# =========================================================================================
for qq in P.ANA: qq['kardes']=None
os.makedirs(GD,exist_ok=True)
P.yaz(os.path.join(GD,f'{ONEK}-1.json'),f'/tmp/bos-{ONEK}.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Basit Makineler'))['kartlar'].append(c['id'])
json.dump(dict(konu='Basit Makineler',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Fizik çıkmış soruları (yalnız mantık), MEB 11–12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar',f'af{ONEK}.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
