"""TYT Fizik · Optik (ikinci paket) · 24 soru, hafif mod (kardeş yok, ipucu 1). Şekiller TikZ; koordinatlar ve açılar Python'da hesaplanır
(yansımada eşit açı, kırılmada vektör Snell yasasıyla doğru yön). Her cevap ve öncül Python'da assert edilir."""
import sys,os,math,json,itertools,random
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,asin,acos,pi
from fractions import Fraction as Fr
P=Parti('optikiki','Optik','fiz|Optik',ders='TYT Fizik',idon='tytfiz')
H.KONU='Optik'
TIPK={}
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · Fizikpedia (yalnız mantık) · MEB 10. sınıf fizik'); TIPK[tipId]='fiz|Optik'
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def pt(p): return f'({p[0]:.3f},{p[1]:.3f})'
def seg(a,b,st='thick'): return f'\\draw[{st}] {pt(a)} -- {pt(b)};'
def ray(a,b,col='vurgu',w='thick',at=.55):
    return f'\\draw[{col},{w},postaction={{decorate,decoration={{markings,mark=at position {at} with {{\\arrow{{Stealth[length=1.9mm,width=1.7mm]}}}}}}}}] {pt(a)} -- {pt(b)};'
def nd(p,txt,anc='',st=''):
    return f'\\node[{anc},inner sep=1.5pt{st}] at {pt(p)} {{{txt}}};'
def add(p,q_): return (p[0]+q_[0],p[1]+q_[1])
def mul(p,s): return (p[0]*s,p[1]*s)
def sub(p,q_): return (p[0]-q_[0],p[1]-q_[1])
def dot(p,q_): return p[0]*q_[0]+p[1]*q_[1]
def nrm(p): l=sqrt(dot(p,p)); return (p[0]/l,p[1]/l)
def reflect(d,n): k=dot(d,n); return (d[0]-2*k*n[0],d[1]-2*k*n[1])
def refract(d,n,n1,n2):
    """d: birim gelen yön, n: birim normal (gelen ışığa ters bakar, n·d<0). TIR ise None."""
    c=-dot(n,d); r=n1/n2; k=1-r*r*(1-c*c)
    if k<0: return None
    t=r*c-sqrt(k); return (r*d[0]+t*n[0],r*d[1]+t*n[1])
def ang(d): return degrees(atan2(d[1],d[0]))
def dim(a,b,txt,pos='below',off=''):
    return f'\\draw[<->,thin] {pt(a)} -- {pt(b)}; \\node[{pos},inner sep=1pt,fill=white{off}] at {pt(((a[0]+b[0])/2,(a[1]+b[1])/2))} {{{txt}}};'
ALL=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def kume(t):
    idx=[i for i in range(3) if t[i]]; r=['I','II','III']
    if len(idx)==1: return 'Yalnız '+r[idx[0]]
    if len(idx)==2: return ' ve '.join(r[i] for i in idx)
    return 'I, II ve III'
def onc_sira(dogru,harf):
    k=ALL.index(dogru); p=' ABCDE'.index(harf)-1
    for c in itertools.combinations(range(7),5):
        if k in c and c.index(k)==p: return [ALL[i] for i in c]
    raise AssertionError((dogru,harf))
def qo(no,ad,truth,harf,neden,**k):
    """öncüllü soru: truth=(I,II,III) doğruluk; neden[i]=(açıklama,tür) öğrencinin o yargıyı yanlış değerlendirme nedeni."""
    dg=kume(truth); sira=onc_sira(dg,harf); yan=[]
    for s in sira:
        if s==dg: continue
        cum={'Yalnız I':(1,0,0),'Yalnız II':(0,1,0),'Yalnız III':(0,0,1),'I ve II':(1,1,0),'I ve III':(1,0,1),'II ve III':(0,1,1),'I, II ve III':(1,1,1)}[s]
        fark=[i for i in range(3) if bool(cum[i])!=bool(truth[i])]; assert fark
        txt=' '.join(f"{['I','II','III'][i]}. yargıyı {'yanlış' if truth[i] else 'doğru'} sanmış: {neden[i][0]}" for i in fark)
        yan.append((s,txt,neden[fark[0]][1]))
    q(no,ad,dogru=dg,yan=yan,sira=sira,**k)
def yer(dogru,dig,harf):
    p=' ABCDE'.index(harf)-1; assert 0<=p<=4; s=list(dig[0:p])+[dogru[0]]+list(dig[p:]); return s
def qt(no,ad,dogru,yan,harf,**k):
    """metin şıklı soru: yan=[(değer,cel,tür)x4]; doğru şık istenen harfe yerleşir."""
    sira=yer((dogru,),[y[0] for y in yan],harf); q(no,ad,dogru=dogru,yan=yan,sira=sira,**k)
def yaz(**k): return k

# =============================== AYDINLANMA ===============================
# ---------- 01 · ışık akısı, ışık şiddeti, aydınlanma şiddeti · kolay · öncüllü
kartla('K-FZOP2-01','Aynı demetin farklı uzaklıktaki perdelerde aydınlanması','Işık akısı demetin taşıdığı ışık miktarıdır ve perdenin uzaklığından bağımsızdır; demet kesiti uzaklığın karesiyle büyüdüğünden aydınlanma şiddeti (E = Φ/A) uzaklığın karesiyle ters orantılı azalır.','Aydınlanma şiddetini uzaklıkla doğru orantılı ya da ters orantılı (kare almadan) sanmak; akının uzaklıkla azaldığını düşünmek.','kolay',3,'fz-op2-aydinlanma-demet','Işık akısı ve aydınlanma şiddeti (demet)')
tg=.22; dd=1.5; ds=[1,2,3]
E_=[Fr(1,i*i) for i in ds]; assert E_[1]/E_[0]==Fr(1,4) and E_[0]>E_[1]>E_[2]
fo=[]
fo.append('\\draw[thick,fill=white] (0,0) circle (.13);')
fo.append(nd((0,-.42),'kaynak'))
for sg in (1,-1):
    fo.append(seg((.8,sg*tg*.8),(.8,sg*1.1),'very thick'))
    fo.append(f'\\draw[vurgu,thick] (0,0) -- ({4.8:.3f},{sg*tg*4.8:.3f});')
fo.append(f'\\draw[vurgu,thick,-{{Stealth[length=1.9mm,width=1.7mm]}}] (3.9,{tg*3.9:.3f}) -- (4.05,{tg*4.05:.3f});')
fo.append(f'\\draw[vurgu,thick,-{{Stealth[length=1.9mm,width=1.7mm]}}] (3.9,{-tg*3.9:.3f}) -- (4.05,{-tg*4.05:.3f});')
for i,n_ in zip(ds,'KLM'):
    x=i*dd; fo.append(seg((x,-tg*x),(x,tg*x),'ultra thick')); fo.append(nd((x,tg*x+.3),n_))
for k_,(i,t_) in enumerate(zip(ds,['$d$','$2d$','$3d$'])):
    y=-1.55-.4*k_; fo.append(dim((0,y),(i*dd,y),t_,'right',',xshift=2pt'))
    fo.append(f'\\draw[dotted] ({i*dd:.3f},{-tg*i*dd:.3f}) -- ({i*dd:.3f},{y:.3f});')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0001',[A('Işık akısını karşılaştır','Perdeler demetin tamamını yakaladığı için hepsine aynı miktarda ışık, yani aynı ışık akısı düşer.','Φ_K = Φ_L = Φ_M → I. doğru'),
 A('Alanları karşılaştır','Demetin kesiti uzaklıkla büyür; kesit alanı uzaklığın karesiyle orantılıdır.','A_K : A_L : A_M = 1² : 2² : 3² = 1 : 4 : 9'),
 A('Aydınlanma şiddetini yaz','E = Φ / A olduğundan akı aynı iken alanı en küçük olan perdede aydınlanma şiddeti en büyüktür.','E_K : E_L : E_M = 1 : ¼ : ⅑ → II. doğru'),
 A('L ile K’yı karşılaştır','L perdesinin aydınlanma şiddeti K’ninkinin dörtte biridir, yarısı değildir.','E_L = E_K ÷ 4 → III. yanlış → I ve II')],
 truth=(True,True,False),harf='B',tipId='fz-op2-aydinlanma-demet',tip='Işık akısı ve aydınlanma şiddeti (demet)',z='kolay',alt='Aydınlanma',kaz='Işık akısı ile aydınlanma şiddeti arasındaki farkı ve aydınlanma şiddetinin uzaklığın karesiyle ters orantılı olduğunu yorumlar.',
 kart='K-FZOP2-01 (demet, üç perde) · akı sabit, alan 1:4:9',kalip='öncüllü',
 metin='Noktasal bir ışık kaynağının önüne, ortasında küçük bir açıklık bulunan ışık geçirmeyen bir levha konulmuş ve açıklıktan çıkan ışık demeti, kaynaktan sırasıyla d, 2d ve 3d uzaklıktaki K, L ve M perdelerine düşürülmüştür. Perdeler şekilde gösterildiği gibi demetin tamamını yakalayacak büyüklüktedir ve deneyde birer birer, diğerleri çıkarılarak kullanılmıştır. Kaynağın ışık şiddeti sabittir ve ortam başka ışık almamaktadır.\nBuna göre,\nI. Perdelere düşen ışık akıları birbirine eşittir.\nII. Aydınlanma şiddeti en büyük olan perde K’dir.\nIII. L perdesinin aydınlanma şiddeti, K perdesinin aydınlanma şiddetinin yarısıdır.\nyargılarından hangileri doğrudur?',
 neden=[('akının perdeye uzaklaştıkça azaldığını düşünmüş; oysa perdelerin tamamı aynı demeti yakalar.','bilgi'),('aydınlanma şiddetinin uzaklıkla değişmediğini sanmış; alan büyüdükçe E = Φ/A azalır.','bilgi'),('uzaklık iki katına çıkınca aydınlanma şiddetinin yarıya düştüğünü sanmış; oysa uzaklığın karesiyle ters orantılıdır.','islem')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her perdenin yakaladığı ışık miktarını ve demetin o perdedeki kesit alanını ayrı ayrı düşün.'],
 bilgi=[B('Işık akısı ve aydınlanma şiddeti','ışık akısı (Φ) bir kaynağın birim zamanda yaydığı ışık miktarıdır; aydınlanma şiddeti, yüzeye dik düşen akının yüzey alanına oranıdır: E = Φ/A. Örnek: 12 lümenlik akı 3 m²’ye düşerse E = 4 lüks'),
        B('Uzaklıkla değişim','noktasal kaynağın ışığı uzaklaştıkça yayılır; kesit alanı uzaklığın karesiyle büyür, E uzaklığın karesiyle ters orantılıdır: E = I/d²')],
 puf='Işık akısı uzaklıkla değişmez; aydınlanma şiddeti ise alan uzaklığın karesiyle büyüdüğü için uzaklığın karesiyle azalır.',sekil=SK)

# ---------- 02 · aydınlanma şiddeti oranı · orta · hikâyeli (şekilsiz)
kartla('K-FZOP2-02','İki ayrı lamba–perde düzeninde aydınlanma şiddeti oranı','E = I/d² bağıntısı her düzen için ayrı yazılır; ışık şiddeti ve uzaklığın karesi birlikte değerlendirilir, sonra oran alınır.','Uzaklığın karesini almamak; yalnız ışık şiddetlerini oranlamak; oranı ters yazmak.','orta',3,'fz-op2-aydinlanma-oran','İki ayrı düzende aydınlanma şiddeti oranı','hikâyeli')
EK=Fr(9,9); EL=Fr(2,4); assert EK/EL==2
assert Fr(9,2)==Fr(9,2) and Fr(9*1,3)/Fr(2,2)==3 and EL/EK==Fr(1,2)
qt('0002',[A('Işık şiddeti ve uzaklığı yaz','Her perde kendi lambasına göre ayrı hesaplanır; aydınlanma şiddeti E = I/d² ile bulunur.','K: I = 9I₀, d = 3 m; L: I = 2I₀, d = 2 m'),
 A('K perdesini hesapla','Uzaklığın karesi paydaya girer.','E_K = 9I₀ ÷ 3² = I₀'),
 A('L perdesini hesapla','Aynı bağıntıyı L için uygula.','E_L = 2I₀ ÷ 2² = 0,5 I₀'),
 A('Oranı bul','Sorulan oran K’nin L’ye bölümüdür.','E_K ÷ E_L = I₀ ÷ 0,5 I₀ = 2')],
 dogru=Fr(2),yan=[(Fr(1,2),'Oranı ters yazmış (E_L ÷ E_K); sorulan K’nin L’ye oranıdır.','dikkat'),(Fr(3,2),'Yalnızca uzaklıkların oranına (3 ÷ 2) bakmış; ışık şiddetlerini hesaba katmamış.','bilgi'),(Fr(3),'E = I/d bağıntısını kullanmış (uzaklığın karesini almamış): (9 ÷ 3) ÷ (2 ÷ 2) = 3.','bilgi'),(Fr(9,2),'Uzaklıkları hiç hesaba katmadan yalnız ışık şiddetlerini (9 ÷ 2) oranlamış.','dikkat')],
 harf='C',tipId='fz-op2-aydinlanma-oran',tip='İki ayrı düzende aydınlanma şiddeti oranı',z='orta',alt='Aydınlanma',kaz='Aydınlanma şiddetinin ışık şiddeti ve uzaklığın karesiyle ilişkisini kullanarak iki düzeni oranlar.',
 kart='K-FZOP2-02 (iki lamba, iki perde) · 9I₀ @ 3 m, 2I₀ @ 2 m',kalip='hikâyeli',
 metin='Bir fotoğraf stüdyosunda aynı anda iki ayrı çekim köşesi hazırlanıyor. Birinci köşede ışık şiddeti 9I₀ olan noktasal K lambası, ışığa dik duran bir perdeden 3 m uzaktadır. İkinci köşede ışık şiddeti 2I₀ olan noktasal L lambası, ışığa dik duran başka bir perdeden 2 m uzaktadır. İki köşede de lambalar dışında ışık kaynağı yoktur ve perdeler ışığı yalnızca kendi lambalarından almaktadır.\nBuna göre, K perdesindeki aydınlanma şiddetinin L perdesindeki aydınlanma şiddetine oranı kaçtır?',
 istenen='K perdesindeki aydınlanma şiddetinin L perdesindekine oranı.',
 ip=['Her düzeni kendi ışık şiddeti ve uzaklığıyla ayrı ayrı hesaplayıp sonra oranla.'],
 bilgi=[B('Aydınlanma şiddeti','noktasal kaynağın ışığa dik tuttuğu yüzeydeki aydınlanma şiddeti E = I / d² ile bulunur (I: ışık şiddeti, d: uzaklık). Örnek: I = 8 cd, d = 2 m için E = 8 ÷ 4 = 2 lüks')],
 puf='Aydınlanma şiddetinde uzaklığın karesi paydadadır; iki düzeni karşılaştırırken her birini ayrı yaz, sonra oranla.',sekil=None)

# ---------- 03 · iki lamba aynı doğru üzerinde · zor · öncüllü
kartla('K-FZOP2-03','Aynı doğru üzerindeki iki lambanın bir noktadaki toplam aydınlanması','Her lambanın aydınlanma şiddeti ayrı hesaplanır (E = I/d²) ve toplanır; lamba çıkarılıp yer değiştirildiğinde yeniden hesaplanıp karşılaştırılır.','Lambaların aydınlanmalarını toplamamak; ışık şiddetini daha büyük olan lambanın hep baskın olduğunu sanmak; uzaklığın karesini unutmak.','zor',4,'fz-op2-aydinlanma-iki-lamba','İki lambanın toplam aydınlanma şiddeti (öncüllü)')
K1=Fr(1,400); L1=Fr(4,1600); assert K1==L1; tot=K1+L1; assert tot==2*K1
yeni=Fr(4,20**2); assert yeni==Fr(1,100) and yeni/tot==2 and yeni/tot!=4
fo=[]
fo.append(seg((0,-1.2),(0,1.2),'ultra thick')); fo.append(f'\\fill[pattern=north east lines,pattern color=gray] (-.28,-1.2) rectangle (0,1.2);')
fo.append(nd((-.12,1.3),'perde','above'))
fo.append('\\draw[thin] (0,0) -- (5.0,0); \\fill (0,0) circle (1.5pt); '+nd((.3,.3),'P'))
for x,n_ in ((2.0,'K'),(4.0,'L')):
    fo.append(f'\\draw[thick,fill=white] ({x},0) circle (.14);'); fo.append(nd((x,.45),n_+(' ($I$)' if n_=='K' else ' ($4I$)')))
    fo.append(ray((x-.2,.0),(x-.9,.0),w='thick',at=.9))
fo.append(dim((0,-.8),(2,-.8),'$20$ cm','below')); fo.append(dim((0,-1.55),(4,-1.55),'$40$ cm','below'))
fo.append('\\draw[dotted] (2,-.1) -- (2,-.85); \\draw[dotted] (4,-.1) -- (4,-1.6);')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0003',[A('K ve L’nin aydınlanmalarını bul','E = I/d² ile her lambayı ayrı hesapla.','E_K = I ÷ 20² = I/400 · E_L = 4I ÷ 40² = I/400'),
 A('Eşitliği değerlendir','İki aydınlanma şiddeti eşittir.','E_K = E_L → II. doğru'),
 A('Toplamı yorumla','Aydınlanma şiddetleri toplanır; toplam tek lambanınkinin iki katıdır.','E_toplam = I/400 + I/400 = 2 × E_K → III. doğru'),
 A('Yeni düzeni hesapla','K kaldırılıp L perdeye 20 cm kalırsa E = 4I ÷ 20² = I/100; bu ilk toplamın (I/200) 2 katıdır, 4 katı değil.','I/100 ÷ (I/200) = 2 → I. yanlış → II ve III')],
 truth=(False,True,True),harf='E',tipId='fz-op2-aydinlanma-iki-lamba',tip='İki lambanın toplam aydınlanma şiddeti (öncüllü)',z='zor',alt='Aydınlanma',kaz='Birden fazla kaynağın bir noktadaki aydınlanma şiddetini kaynakların katkılarını ayrı hesaplayıp toplayarak yorumlar.',
 kart='K-FZOP2-03 (iki lamba, bir perde) · I @ 20 cm, 4I @ 40 cm',kalip='öncüllü',
 metin='Şekildeki düzenekte ışık şiddetleri sırasıyla I ve 4I olan, boyutları ihmal edilebilecek kadar küçük K ve L lambaları, ışığı soğuran bir perdeye dik olan aynı doğru üzerindedir. Lambalar birbirinin ışığını engellemez, ortamda başka ışık kaynağı yoktur ve perdedeki P noktasının aydınlanma şiddeti, lambaların tek başına oluşturduğu aydınlanma şiddetlerinin toplamıdır.\nBuna göre,\nI. K lambası kaldırılıp L lambası perdeye 20 cm uzaklığa getirilirse P noktasındaki aydınlanma şiddeti ilk değerin 4 katı olur.\nII. K ve L lambalarının P noktasında oluşturduğu aydınlanma şiddetleri birbirine eşittir.\nIII. Her iki lamba da yanarken P noktasındaki aydınlanma şiddeti, yalnız K yanarken oluşandan 2 kat büyüktür.\nyargılarından hangileri doğrudur?',
 neden=[('lambanın yaklaşmasıyla yalnız ışık şiddetinin 4 katı etkili olur sanmış; ilk toplamın iki lambadan oluştuğunu hesaba katmamış.','dikkat'),('4I şiddetli lambanın uzaklığı iki katı olsa da daha baskın olacağını düşünmüş; uzaklığın karesini hesaba katmamış.','bilgi'),('toplam aydınlanmanın lambaların aydınlanmalarının toplamı olduğunu unutmuş.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Önce her lambanın P noktasındaki aydınlanma şiddetini ayrı ayrı I cinsinden yaz.'],
 bilgi=[B('Birden çok kaynak','bir noktadaki toplam aydınlanma şiddeti, her kaynağın o noktada tek başına oluşturduğu aydınlanma şiddetlerinin toplamıdır. Örnek: 3 lüks ve 5 lüks oluşturan iki kaynak birlikte 8 lüks verir'),
        B('Uzaklığın etkisi','E = I/d²; uzaklık 2 katına çıkarsa aynı kaynağın E değeri 4 kat azalır')],
 puf='Önce her kaynağın katkısını E = I/d² ile ayrı bul; kaynaklar yer değiştirirse hesabı baştan kur.',sekil=SK)

# =============================== GÖLGE ===============================
# ---------- 04 · geniş kaynakta tam gölge / yarı gölge · kolay · öncüllü
kartla('K-FZOP2-04','Geniş (çubuk) kaynakla oluşan tam gölge ve yarı gölge bölgeleri','Kaynağın hiçbir noktasından ışık alamayan bölge tam gölge, bir kısmından ışık alan bölge yarı gölgedir; engel kaynağa yaklaşırsa yarı gölge genişler.','Yarı gölgeyi kaynağın tüm noktalarından ışık alan bölge sanmak; tam gölgeyi perdeye ışık gelmeyen her yer saymak.','kolay',3,'fz-op2-golge-genis','Geniş kaynakta tam gölge ve yarı gölge (öncüllü)')
s_,r_,a_,b_=.4,.7,2.2,5.0
def golge(s,r,a,b): return s+(r-s)*b/a, -s+(r+s)*b/a          # tam gölge yarı genişliği, yarı gölgenin dış sınırı
def gorulen(y,s,r,a,b,n=401):                                  # perde noktasından görülen kaynak oranı
    vis=0
    for i in range(n):
        ys=-s+2*s*i/(n-1); h=ys+(y-ys)*a/b
        if abs(h)>r: vis+=1
    return vis/n
u_,pn_=golge(s_,r_,a_,b_); assert u_>0 and pn_>u_
assert gorulen(0,s_,r_,a_,b_)==0 and gorulen((u_+pn_)/2,s_,r_,a_,b_)>0 and gorulen((u_+pn_)/2,s_,r_,a_,b_)<1 and gorulen(pn_+.2,s_,r_,a_,b_)==1
assert abs(gorulen(u_-.02,s_,r_,a_,b_))==0 and gorulen(u_+.02,s_,r_,a_,b_)>0
w1=golge(s_,r_,a_,b_); w2=golge(s_,r_,a_-.4,b_); assert (w2[1]-w2[0])>(w1[1]-w1[0])
Hs=3.0; ym=[(pn_+Hs)/2,(u_+pn_)/2,0,-(u_+pn_)/2,-(pn_+Hs)/2]
fo=[]
fo.append(seg((0,-s_),(0,s_),'ultra thick,vurgu')); fo.append(nd((0,-s_-.1),'kaynak','below'))
fo.append(seg((a_,-r_),(a_,r_),'ultra thick')); fo.append(nd((a_,-r_-.1),'engel','below'))
fo.append(seg((b_,-Hs),(b_,Hs),'ultra thick')); fo.append(nd((b_,-Hs-.1),'perde','below'))
for sg in (1,-1):
    fo.append(ray((0,sg*s_),(a_,sg*r_),at=.5)); fo.append(f'\\draw[vurgu,thick] ({a_},{sg*r_}) -- ({b_},{sg*u_:.3f});')
    fo.append(ray((0,-sg*s_),(a_,sg*r_),at=.5)); fo.append(f'\\draw[vurgu,thick] ({a_},{sg*r_}) -- ({b_},{sg*pn_:.3f});')
for y in (pn_,u_,-u_,-pn_): fo.append(seg((b_-.12,y),(b_+.12,y),'thick'))
for y,n_ in zip(ym,'KLMNP'): fo.append(nd((b_+.12,y),n_,'right'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0004',[A('Bölgelerin ışık alışını incele','Engelin kenarlarından geçen ışınlar bölgelerin sınırlarını verir; M bölgesine kaynağın hiçbir noktasından ışık ulaşmaz.','M: tam gölge → I. doğru'),
 A('L bölgesini değerlendir','L ve N bölgeleri kaynağın yalnızca bir kısmından ışık alır; hepsinden değil. Bu yüzden yarı gölgedir, en aydınlık bölge K ve P’dir.','L: yarı gölge → II. yanlış'),
 A('Engelin yaklaşmasını incele','Engel kaynağa yaklaştıkça iki kenar ışını arasındaki açı büyür, yarı gölge bölgeleri genişler.','Kaynak–engel uzaklığı azalır → yarı gölge genişler → III. doğru → I ve III')],
 truth=(True,False,True),harf='D',tipId='fz-op2-golge-genis',tip='Geniş kaynakta tam gölge ve yarı gölge (öncüllü)',z='kolay',alt='Gölge',kaz='Geniş ışık kaynağıyla oluşan tam gölge ve yarı gölge bölgelerini ayırt eder, engelin konumunun etkisini yorumlar.',
 kart='K-FZOP2-04 (çubuk kaynak, engel, perde) · beş bölge',kalip='öncüllü',
 metin='Çubuk biçimli geniş bir ışık kaynağı ile ışığı geçirmeyen bir engel ve perde, şekildeki gibi yerleştirilmiştir. Şekilde kaynağın uçlarından çıkıp engelin kenarlarından geçen ışınlar, perdede ise K, L, M, N ve P bölgeleri gösterilmiştir. Perde ve engel, kaynağa dik doğrultuda sabit duran düzlemsel yüzeylerdir ve ortamda başka ışık yoktur.\nBuna göre,\nI. M bölgesine kaynağın hiçbir noktasından ışık ulaşmaz.\nII. L bölgesi kaynağın bütün noktalarından ışık aldığı için perdenin en aydınlık bölgesidir.\nIII. Engel, perde yerinde sabit kalacak biçimde kaynağa yaklaştırılırsa yarı gölge bölgeleri genişler.\nyargılarından hangileri doğrudur?',
 neden=[('perdenin ortasına ışık gelmeyen her yerin tam gölge olmadığını, M bölgesinde kaynağın hiçbir noktasının görülmediğini fark etmemiş.','bilgi'),('yarı gölge bölgesinin kaynağın tüm noktalarından ışık aldığını düşünmüş; oysa yalnızca bir kısmından alır.','bilgi'),('engel kaynağa yaklaşınca gölgenin değişmeyeceğini ya da yarı gölgenin daralacağını sanmış.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Perdedeki her bölgeden bakıldığında kaynağın ne kadarının görülebildiğini düşün.'],
 bilgi=[B('Tam ve yarı gölge','geniş bir kaynağın ışığı bir engelle kesilirse kaynağın hiçbir noktasından ışık alamayan bölge tam gölge, yalnızca bir kısmından ışık alan bölge yarı gölgedir. Örnek: yarı gölgede duran biri kaynağın bir ucunu görür, öbür ucunu göremez')],
 puf='Bir noktadan kaynağa bakıldığında kaynağın tamamı görünüyorsa aydınlık, bir kısmı görünüyorsa yarı gölge, hiç görünmüyorsa tam gölgedir.',sekil=SK)

# ---------- 05 · noktasal kaynakla gölge boyu · orta · hikâyeli şekilli
kartla('K-FZOP2-05','Noktasal kaynakta engel kayınca gölge çapı','Benzer üçgenlerden gölge boyu = engel boyu × (kaynak–perde uzaklığı) ÷ (kaynak–engel uzaklığı); engel perdeye yaklaşınca gölge küçülür.','Gölgenin değişmediğini sanmak; engeli kaynağa yaklaşmış gibi hesaplamak; oranı ters yazmak.','orta',3,'fz-op2-golge-boyut','Noktasal kaynakta gölge çapı (benzer üçgen)')
dsk=12; a0,b0,k_=30,60,10
g0=Fr(dsk*b0,a0); g1=Fr(dsk*b0,a0+k_); gyan=Fr(dsk*b0,a0-k_); gters=Fr(dsk*(a0+k_),b0)
assert (g0,g1,gyan,gters)==(24,18,36,8)
sc=.1; fo=[]
fo.append('\\fill (0,0) circle (2pt);'); fo.append(nd((0,.32),'kaynak'))
fo.append(seg((a0*sc,-dsk/2*sc),(a0*sc,dsk/2*sc),'ultra thick')); fo.append(nd((a0*sc,.95),'disk'))
fo.append(seg((b0*sc,-1.9),(b0*sc,1.9),'ultra thick')); fo.append(nd((b0*sc,-2.0),'perde','below'))
yh=float(g0)/2*sc
for sg in (1,-1):
    fo.append(f'\\draw[vurgu,thick] (0,0) -- ({b0*sc:.3f},{sg*yh:.3f});')
    fo.append(f'\\draw[vurgu,thick,-{{Stealth[length=1.9mm,width=1.7mm]}}] (0,0) -- ({a0*sc*.55:.3f},{sg*yh*.55/2*1:.3f});')
fo.append(f'\\draw[dashed,thick] ({(a0+k_)*sc},{-dsk/2*sc}) -- ({(a0+k_)*sc},{dsk/2*sc});')
fo.append(f'\\draw[->,thick] ({a0*sc+.1},-1.3) -- ({(a0+k_)*sc-.1},-1.3); '+nd((((a0+k_/2)*sc),-1.3),'$10$ cm','below'))
fo.append(f'\\draw[<->,thin] ({a0*sc-.35},{-dsk/2*sc}) -- ({a0*sc-.35},{dsk/2*sc}); '+nd((a0*sc-.35,0),'$12$ cm','left'))
fo.append(dim((0,-2.55),(a0*sc,-2.55),'$30$ cm','below')); fo.append(dim((a0*sc,-2.55),(b0*sc,-2.55),'$30$ cm','below'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qt('0005',[A('Benzer üçgenleri kur','Kaynaktan çıkan ışınlar iki benzer üçgen oluşturur; gölge boyu engel boyuyla uzaklık oranı kadar büyür.','gölge ÷ disk = kaynak–perde ÷ kaynak–disk'),
 A('Yeni uzaklığı yaz','Disk perdeye doğru 10 cm ilerlediği için kaynak–disk uzaklığı artar, kaynak–perde uzaklığı sabit kalır.','30 + 10 = 40 cm'),
 A('Gölge çapını hesapla','Disk perdeye yaklaştığı için gölge küçülür.','gölge = 12 × 60 ÷ 40 = 18 cm')],
 dogru=Fr(18),yan=[(Fr(8),'Oranı ters yazmış: 12 × 40 ÷ 60 = 8 cm; gölge diskten küçük çıkamaz.','islem'),(Fr(12),'Gölge çapını diskin çapına eşit sanmış; ışık noktasal kaynaktan yayıldığı için gölge büyür.','bilgi'),(Fr(24),'Kaymanın gölgeyi etkilemediğini düşünmüş; ilk durumdaki gölge çapını yazmış.','dikkat'),(Fr(36),'Diski kaynağa doğru 10 cm kaydırılmış gibi almış: 12 × 60 ÷ 20 = 36 cm.','dikkat')],
 harf='C',tipId='fz-op2-golge-boyut',tip='Noktasal kaynakta gölge çapı (benzer üçgen)',z='orta',alt='Gölge',kaz='Noktasal kaynakta engelin konumu değişince oluşan gölgenin boyutunu benzer üçgenlerle bulur.',
 kart='K-FZOP2-05 (nokta kaynak, disk, perde) · 12 cm, 30–60 cm, 10 cm kayma',kalip='şekilli',
 metin='Bir fen kulübü öğrencileri, noktasal bir ışık kaynağı ile dik duran bir perde arasına, yüzeyi perdeye paralel olan ve ışığı geçirmeyen 12 cm çaplı bir disk yerleştiriyor. Kaynak ile perde arasındaki uzaklık 60 cm, kaynak ile disk arasındaki uzaklık 30 cm’dir ve disk, kaynak–perde doğrusu üzerinde ortalanmıştır. Öğrenciler diski, kaynağı ve perdeyi hareket ettirmeden, doğru boyunca perdeye doğru 10 cm kaydırıyor (şekilde kesik çizgiyle gösterilmiştir).\nBuna göre, perdede oluşan tam gölgenin çapı kaç cm olur?',
 istenen='Kayma sonrası perdedeki tam gölgenin çapı (cm).',
 ip=['Kaynaktan diskin kenarlarına ve oradan perdeye giden ışınların oluşturduğu iki üçgeni karşılaştır.'],
 bilgi=[B('Gölge boyutu','noktasal kaynakta ışınlar doğrusal yayılır; engel ve gölge, kaynakta birleşen benzer üçgenler oluşturur. Örnek: kaynaktan 10 cm’deki 2 cm’lik engelin 40 cm’deki perdede oluşturduğu gölge 8 cm’dir')],
 puf='Noktasal kaynakta gölge çapı = engel çapı × (kaynak–perde) ÷ (kaynak–engel); engel perdeye yaklaşınca gölge küçülür.',sekil=SK)

# ---------- 06 · Güneş ve Ay tutulması · zor · öncüllü
kartla('K-FZOP2-06','Güneş–Dünya–Ay konumlarına göre tutulma türü','Ay Güneş ile Dünya arasındayken Ay’ın gölgesi Dünya’ya düşer (Güneş tutulması); Ay, Dünya’nın tam gölgesine girerse tam Ay tutulması, yalnız yarı gölgesine girerse tam tutulma olmaz.','Ay’ın yarı gölgeye girmesini tam Ay tutulması sanmak; Güneş tutulmasını Ay tutulması ile karıştırmak.','orta',4,'fz-op2-tutulma','Güneş ve Ay tutulması (öncüllü)')
Rs,Re_,Dse,Rm=1.2,.45,4.5,.2
xu=Dse*Re_/(Rs-Re_); xi=-Dse*Re_/(Rs+Re_); assert abs(xu-2.7)<1e-9 and abs(xi+1.2273)<.001
um=lambda x: Re_*(1-x/xu); pm=lambda x: Re_*(1-x/xi)
posK=(-.9,0); posL=(1.1,0); posM=(1.7,.62)
assert um(posL[0])>Rm and posM[1]-Rm>um(posM[0]) and posM[1]+Rm<pm(posM[0])
Dm=Dse+posK[0]; lum=Dm*Rm/(Rs-Rm); assert lum>abs(posK[0])-Re_   # Ay'ın tam gölgesi Dünya'ya ulaşır
Xe=3.4; fo=[]
fo.append(f'\\fill[gray!15] (0,{Re_}) -- ({Xe},{pm(Xe):.3f}) -- ({Xe},{-pm(Xe):.3f}) -- (0,{-Re_}) -- cycle;')
fo.append(f'\\fill[gray!65] (0,{Re_}) -- ({xu},0) -- (0,{-Re_}) -- cycle;')
fo.append(f'\\draw[thick,fill=vurgu!25] ({-Dse},0) circle ({Rs});'); fo.append(nd((-Dse,0),'Güneş'))
fo.append(f'\\draw[thick,fill=white] (0,0) circle ({Re_});'); fo.append(nd((0,-Re_-.05),'Dünya','below'))
sph=(Rs-Re_)/Dse; ph=asin(sph); Ts=(-Dse+Rs*sin(ph),Rs*cos(ph)); Te=(Re_*sin(ph),Re_*cos(ph))
for sg in (1,-1):
    fo.append(f'\\draw[thin,dashed] ({Ts[0]:.3f},{sg*Ts[1]:.3f}) -- ({xu},0);')
th=asin(Re_/-xi); n_=(-sin(th),cos(th)); Ts2=add((-Dse,0),mul(n_,-Rs)); assert abs(dot(n_,sub((xi,0),(-Dse,0)))*-1)>0
for sg in (1,-1):
    fo.append(f'\\draw[thin,dashed] ({Ts2[0]:.3f},{sg*Ts2[1]:.3f}) -- ({Xe},{sg*pm(Xe):.3f});')
fo.append(f'\\fill[gray!65] ({posK[0]},{Rm}) -- ({posK[0]+lum:.3f},0) -- ({posK[0]},{-Rm}) -- cycle;')
for (x,y),n__ in ((posK,'K'),(posL,'L'),(posM,'M')):
    fo.append(f'\\draw[thick,fill=white] ({x},{y}) circle ({Rm});'); fo.append(nd((x,y+Rm+.17),n__,st=',fill=white'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0006',[A('Ay’ın konumlarını belirle','K konumunda Ay, Güneş ile Dünya arasındadır; Ay’ın gölgesi Dünya’ya düşer.','K: Güneş tutulması → I. yanlış (Ay tutulması değil)'),
 A('L konumunu incele','L konumunda Ay’ın tamamı Dünya’nın tam gölgesindedir; Güneş ışığı Ay’a hiç ulaşmaz.','L: tam Ay tutulması → II. doğru'),
 A('M konumunu incele','M konumunda Ay, Dünya’nın yarı gölgesindedir; Güneş’in bir kısmından ışık almaya devam eder.','M: yarı gölge → tam tutulma olmaz → III. yanlış → Yalnız II')],
 truth=(False,True,False),harf='B',tipId='fz-op2-tutulma',tip='Güneş ve Ay tutulması (öncüllü)',z='orta',alt='Gölge',kaz='Güneş, Dünya ve Ay’ın konumlarına göre oluşan tam gölge ve yarı gölgeyi yorumlayarak tutulma türünü belirler.',
 kart='K-FZOP2-06 (Güneş–Dünya–Ay, üç konum) · tam gölge, yarı gölge',kalip='öncüllü',
 metin='Şekilde Güneş, Dünya ve Ay’ın bulunabileceği üç konum (K, L ve M) ölçeksiz olarak gösterilmiştir. Koyu renkli bölge Dünya’nın ya da Ay’ın tam gölgesini, açık gri bölge Dünya’nın yarı gölgesini temsil etmektedir. Ay, bu konumlardan yalnızca birinde bulunur ve Güneş ışığı dışında ışık kaynağı yoktur.\nBuna göre,\nI. Ay K konumundayken Dünya’dan bakıldığında Ay tutulması gözlenir.\nII. Ay L konumundayken tam Ay tutulması gözlenir.\nIII. Ay M konumundayken Ay, Dünya’nın tam gölgesinde kaldığı için tam Ay tutulması gözlenir.\nyargılarından hangileri doğrudur?',
 neden=[('Ay’ın Güneş ile Dünya arasında olduğu durumda gözlenen olayın Güneş tutulması olduğunu unutmuş.','bilgi'),('Ay’ın Dünya’nın tam gölgesine girmesinin tam Ay tutulması olduğunu bilmemiş.','bilgi'),('yarı gölgeyi tam gölge sanmış; yarı gölgede Ay Güneş ışığının bir kısmını almaya devam eder.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her konumda Ay’ın Güneş ışığını tamamen, kısmen ya da hiç alıp almadığını Dünya’nın gölge bölgelerine göre düşün.'],
 bilgi=[B('Güneş tutulması','Ay, Güneş ile Dünya arasına girdiğinde Ay’ın gölgesi Dünya’nın bir bölgesine düşer; o bölgedeki gözlemciler Güneş tutulmasını görür'),
        B('Ay tutulması','Ay, Dünya’nın tam gölgesine girerse tam Ay tutulması, yalnızca yarı gölgesine girerse tam olmayan soluklaşma gözlenir; Ay tutulmasında sıra Güneş–Dünya–Ay’dır')],
 puf='Sıra Güneş–Ay–Dünya ise Güneş tutulması; Güneş–Dünya–Ay ise Ay tutulması olur, Ay tam gölgeye girdiğinde tutulma tamdır.',sekil=SK)

# =============================== YANSIMA VE DÜZLEM AYNA ===============================
def arka(p1,p2,gerisi,uz=.2,n=14):
    """aynanın arka yüzüne tarama çizgileri: gerisi = arkaya doğru birim vektör"""
    o=[seg(p1,p2,'very thick')]
    for i in range(n+1):
        t=i/n; p=(p1[0]+(p2[0]-p1[0])*t,p1[1]+(p2[1]-p1[1])*t)
        q_=add(p,mul(gerisi,uz)); q_=add(q_,mul(nrm(sub(p2,p1)),-uz*.8))
        o.append(f'\\draw[thin] {pt(p)} -- {pt(q_)};')
    return '\n'.join(o)
def yay(c,r,a1,a2,txt=None,rt=None,pos=''):
    s=f'\\draw[thin] ({c[0]+r*cos(radians(a1)):.3f},{c[1]+r*sin(radians(a1)):.3f}) arc[start angle={a1},end angle={a2},radius={r}];'
    if txt:
        am=radians((a1+a2)/2); rt=rt or r+.28; s+=nd((c[0]+rt*cos(am),c[1]+rt*sin(am)),txt,pos)
    return s
# ---------- 07 · yansıma yasası · kolay
kartla('K-FZOP2-07','Yansıma yasasıyla gelen ve yansıyan ışın arasındaki açı','Gelme açısı normalle ölçülür ve yansıma açısına eşittir; yüzeyle yapılan açı verildiyse normalle açı 90°’den çıkarılarak bulunur, gelen ve yansıyan ışın arasındaki açı bunların toplamıdır.','Yüzeyle yapılan açıyı gelme açısı sanmak; gelen–yansıyan arasını yüzeyle yapılan açı ya da gelme açısı olarak yazmak.','kolay',3,'fz-op2-yansima-aci','Yansıma yasası ile ışınlar arası açı')
th_y=30; dg=(cos(radians(th_y)),-sin(radians(th_y))); rf=reflect(dg,(0,1)); assert abs(ang(rf)-th_y)<1e-9
gel=degrees(acos(dot(mul(dg,-1),rf))); assert abs(gel-120)<1e-9 and 90-th_y==60 and 180-th_y==150 and th_y+60==90
L_=2.6; Sg=(-L_*cos(radians(th_y)),L_*sin(radians(th_y)))
fo=[arka((-3,0),(3,0),(0,-1),.2,16)]
fo.append(f'\\draw[dashed] (0,0) -- (0,2.2); \\node[above,inner sep=1pt] at (0,2.2) {{normal}};')
fo.append(ray(Sg,(0,0),at=.5)); fo.append(ray((0,0),(L_*rf[0],L_*rf[1]),at=.6))
fo.append(yay((0,0),1.15,180-th_y,180,'$30^\\circ$',rt=1.55))
fo.append(nd((3.0,.3),'ayna','right'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0007',[A('Gelme açısını bul','Gelme açısı normalle ölçülür; ışın yüzeyle 30° yaptığına göre normalle 90° − 30° yapar.','θ_gelme = 90° − 30° = 60°'),
 A('Yansıma yasasını uygula','Yansıma açısı gelme açısına eşittir ve ışın normalin öbür tarafına yansır.','θ_yansıma = 60°'),
 A('Işınlar arasındaki açıyı bul','Normalin iki yanındaki açılar toplanır.','60° + 60° = 120°')],
 dogru=120,yan=[(30,'Aynayla yapılan 30°’lik açıyı gelen ve yansıyan ışın arasındaki açı sanmış.','dikkat'),(60,'Gelme açısını (60°) sorulan açı sanmış; sorulan gelen ve yansıyan ışın arasındaki açıdır.','dikkat'),(90,'30° ve 60°’yi toplamış: yüzeyle yapılan açı ile gelme açısını karıştırmış.','islem'),(150,'180° − 30° işlemini yapmış; ışınlar arasındaki açıyı normale göre değil yüzeye göre kurmuş.','islem')],
 tipId='fz-op2-yansima-aci',tip='Yansıma yasası ile ışınlar arası açı',z='kolay',alt='Yansıma Yasaları',kaz='Yansıma yasasını kullanarak gelen ve yansıyan ışın arasındaki açıyı bulur.',
 kart='K-FZOP2-07 (yansıma yasası) · yüzeyle 30°',kalip='şekilli',
 metin='Bir fizik laboratuvarında öğrenci, lazer göstericiden çıkan ince ışık demetini, yatay masa üzerine konulmuş pürüzsüz bir düzlem aynaya şekildeki gibi gönderiyor. Işın, ayna yüzeyiyle şekilde gösterilen 30°’lik açıyı yapacak biçimde aynaya çarpıyor ve yansıyor. Öğrenci aynanın yüzeyine dik olan normal doğrusunu kesik çizgiyle işaretlemiştir; ayna ışığın tamamını yansıtmaktadır.\nBuna göre, gelen ışın ile yansıyan ışın arasındaki açı kaç derecedir?',
 istenen='Gelen ışın ile yansıyan ışın arasındaki açı (derece).',
 ip=['Gelme açısının hangi doğruya göre ölçüldüğünü hatırla ve yansıyan ışının normalin diğer tarafında hangi açıyla gittiğini düşün.'],
 bilgi=[B('Yansıma yasaları','gelen ışın, normal ve yansıyan ışın aynı düzlemdedir; gelme açısı yansıma açısına eşittir ve ikisi de normalden ölçülür. Örnek: normalle 40° yapan ışın normalin öbür yanında 40° ile yansır')],
 puf='Açılar normalden ölçülür: yüzeyle yapılan açı verilmişse önce 90°’den çıkar, sonra yansıma açısını ekle.',sekil=SK)

# ---------- 08 · dönen ayna · orta
kartla('K-FZOP2-08','Düzlem ayna döndürülünce yansıyan ışının dönmesi','Gelen ışın sabitken ayna α kadar dönerse yansıyan ışın 2α kadar döner (normal de α döner, gelme ve yansıma açıları ikişer kez değişir).','Işının da aynayla aynı açıda döndüğünü sanmak; yansıyan ışının yarım açı döndüğünü düşünmek.','orta',3,'fz-op2-ayna-donme','Dönen düzlem aynada yansıyan ışının dönme açısı')
al=12; din=(cos(radians(-40)),sin(radians(-40))); n0=(0,1); r0=reflect(din,n0)
nm=(-sin(radians(al)),cos(radians(al))); r1=reflect(din,nm)
assert abs(ang(r0)-40)<1e-9 and abs(ang(r1)-64)<1e-9 and abs(ang(r1)-ang(r0)-2*al)<1e-9
assert 40+al==52
O_=(0,0); La=2.5
fo=[]
fo.append(f'\\draw[dashed] (-2.6,0) -- (2.6,0);')
m1=(-2.4*cos(radians(al)),-2.4*sin(radians(al))); m2=(2.4*cos(radians(al)),2.4*sin(radians(al)))
fo.append(arka(m1,m2,(-sin(radians(al))*-1*-1*0+sin(radians(al)),-cos(radians(al))),.18,16))
fo.append('\\fill (0,0) circle (2pt); '+nd((0,-.15),'O','below',',xshift=-6pt'))
fo.append(ray((-La*cos(radians(40)),La*sin(radians(40))),(0,0),at=.5))
fo.append(f'\\draw[vurgu,thick,dashed] (0,0) -- ({La*r0[0]:.3f},{La*r0[1]:.3f});')
fo.append(ray((0,0),(La*r1[0],La*r1[1]),at=.7))
fo.append(yay((0,0),2.05,0,al,'$12^\\circ$',rt=2.5)); fo.append(yay((0,0),1.0,140,180,'$40^\\circ$',rt=1.45))
fo.append(yay((0,0),1.35,ang(r0),ang(r1),'?',rt=1.7))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0008',[A('Aynanın dönmesini yorumla','Ayna 12° dönünce normal de 12° döner; gelen ışın sabit olduğundan gelme açısı 12° değişir.','Δθ_gelme = 12°'),
 A('Yansıma açısını yaz','Yansıma açısı da gelme açısı kadar değişir; yansıyan ışın normalin öbür yanında kalır.','Δθ_yansıma = 12°'),
 A('Yansıyan ışının dönmesini bul','Gelme ve yansıma açılarındaki değişimler aynı yönde toplanır.','12° + 12° = 24°')],
 dogru=24,yan=[(6,'Yansıyan ışının aynanın yarısı kadar döndüğünü sanmış: 12° ÷ 2.','bilgi'),(12,'Yansıyan ışının aynayla birlikte aynı açıda döndüğünü düşünmüş.','bilgi'),(48,'Gelme ve yansıma açılarındaki değişimin iki katını da ayrıca ikiye katlamış: 2 × 24°.','islem'),(52,'Gelen ışının aynayla yaptığı yeni açıyı (40° + 12°) dönme miktarı sanmış.','dikkat')],
 tipId='fz-op2-ayna-donme',tip='Dönen düzlem aynada yansıyan ışının dönme açısı',z='orta',alt='Düzlem Ayna',kaz='Düzlem ayna döndürüldüğünde yansıyan ışının dönme açısının ayna dönme açısının iki katı olduğunu kullanır.',
 kart='K-FZOP2-08 (dönen ayna) · 12° dönme',kalip='şekilli',
 metin='Bir lazer işaretleyici, sabit tutulan bir konumdan, O noktası çevresinde çizim düzlemine dik eksen etrafında döndürülebilen düzlem aynaya ince bir ışın gönderiyor. Gelen ışın, ayna ilk konumundayken (kesik çizgi) yüzeyle 40° yapmaktadır. Işın doğrultusu sabit kalırken ayna, ilk konumundan (kesik çizgi) şekilde gösterilen konuma 12° döndürülüyor. Yansıyan ışının ilk doğrultusu kesik çizgiyle, yeni doğrultusu sürekli çizgiyle gösterilmiştir.\nBuna göre, ayna 12° döndürülürken yansıyan ışın kaç derece döner?',
 istenen='Yansıyan ışının dönme açısı (derece).',
 ip=['Ayna döndüğünde normalin de aynı açıda döndüğünü ve gelen ışınla normal arasındaki açının değiştiğini düşün.'],
 bilgi=[B('Dönen ayna','gelen ışın sabit tutulup ayna α kadar döndürülürse yansıyan ışın 2α kadar döner, çünkü hem gelme hem yansıma açısı α değişir. Örnek: ayna 5° dönerse yansıyan ışın 10° döner')],
 puf='Ayna α döndüğünde yansıyan ışın 2α döner; gelen ışını sabit tutmak ve açıyı normalden ölçmek yeterlidir.',sekil=SK)

# ---------- 09 · düzlem aynada görüntü uzaklığı · orta · öncüllü
kartla('K-FZOP2-09','Düzlem aynada görüntü uzaklığı ve ayna kaydırma','Görüntü, aynanın cisim kadar gerisinde sanal ve düz oluşur; ayna cisme x kadar yaklaşırsa cisimle görüntü arası 2x azalır; görüntünün boyu aynanın boyutundan bağımsızdır.','Ayna x kadar kayınca görüntünün de yalnız x kadar kaydığını sanmak; aynanın boyutuyla görüntü boyunu ilişkilendirmek.','orta',3,'fz-op2-duzlem-goruntu','Düzlem aynada görüntü uzaklığı (öncüllü)')
d0=3; d1=2
assert 2*d0==6 and 2*d1==4 and 2*d0-2*d1==2
sc9=1.1; fo=[]
fo.append(arka((0,-1.5),(0,1.5),(1,0),.2,14))
fo.append(f'\\draw[thick,dashed] ({-1*sc9:.3f},-1.5) -- ({-1*sc9:.3f},1.5);')
fo.append(f'\\draw[->,thick] (-.15,1.75) -- ({-sc9+.15:.3f},1.75); '+nd((-sc9/2,1.75),'$1$ m','above'))
fo.append(f'\\fill (-{d0*sc9:.3f},0) circle (2.4pt); '+nd((-d0*sc9,.3),'K'))
fo.append(dim((-d0*sc9,-1.05),(0,-1.05),'$3$ m','below'))
fo.append(f'\\draw[dotted] (-{d0*sc9:.3f},-.1) -- (-{d0*sc9:.3f},-1.1);')
fo.append(nd((.0,-1.75),'ayna','below',',xshift=2pt'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0009',[A('İlk görüntü uzaklığını bul','Düzlem aynada görüntü aynanın gerisinde, aynadan cisim kadar uzakta oluşur.','Cisim–ayna 3 m → ayna–görüntü 3 m → cisim–görüntü 6 m → I. doğru'),
 A('Aynayı kaydır','Ayna 1 m yaklaşınca cisim–ayna uzaklığı 2 m olur; görüntü de aynanın 2 m gerisindedir.','2 m + 2 m = 4 m; azalma 6 − 4 = 2 m → II. yanlış (1 m değil)'),
 A('Ayna boyutunu yorumla','Görüntünün boyu cismin boyuna eşittir; aynanın boyutu yalnızca görüntünün ne kadarının görüleceğini belirler.','III. yanlış → Yalnız I')],
 truth=(True,False,False),harf='A',tipId='fz-op2-duzlem-goruntu',tip='Düzlem aynada görüntü uzaklığı (öncüllü)',z='orta',alt='Düzlem Ayna',kaz='Düzlem aynada görüntünün konumunu ve ayna kayınca cisimle görüntü arasındaki uzaklığın değişimini yorumlar.',
 kart='K-FZOP2-09 (düzlem ayna, kayan ayna) · 3 m, 1 m',kalip='öncüllü',
 metin='Düzlem bir aynanın önünde duran K noktasal cismi, aynadan 3 m uzaktadır. Cisim yerinde sabit tutulurken ayna, cisme doğru 1 m ilerletiliyor; aynanın yeni konumu şekilde kesik çizgiyle gösterilmiştir. Cismin görüntüsü, ayna ilerletilirken ve ilerletildikten sonra aynanın önünden bakan bir gözlemci tarafından izlenmektedir.\nBuna göre,\nI. Ayna ilerletilmeden önce cisim ile görüntüsü arasındaki uzaklık 6 m’dir.\nII. Ayna ilerletildiğinde cisim ile görüntüsü arasındaki uzaklık 1 m azalır.\nIII. Aynanın boyutu küçültülürse görüntünün boyu da küçülür.\nyargılarından hangileri doğrudur?',
 neden=[('görüntünün aynadan itibaren cisim kadar uzakta değil de aynanın yüzeyinde oluştuğunu düşünmüş.','bilgi'),('ayna 1 m kayınca görüntü uzaklığının yalnız 1 m değiştiğini sanmış; hem cisim–ayna hem ayna–görüntü uzaklığı 1 m azalır.','islem'),('aynanın küçülünce görüntünün de küçüleceğini sanmış; görüntü boyu cismin boyuna eşittir.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Görüntünün aynaya göre nerede oluştuğunu ve ayna kayınca bu uzaklığın nasıl değiştiğini ayrı ayrı yaz.'],
 bilgi=[B('Düzlem aynada görüntü','görüntü aynanın arkasında, aynadan cisim kadar uzakta oluşur; sanaldır, düzdür ve cisimle aynı boydadır. Örnek: aynadan 2 m uzaktaki cismin görüntüsü aynanın 2 m gerisindedir, aralarındaki uzaklık 4 m’dir')],
 puf='Cisimle görüntü arası uzaklık, cismin ayna uzaklığının iki katıdır; ayna x kayınca bu uzaklık 2x değişir.',sekil=SK)

# ---------- 10 · görüş alanı · zor
kartla('K-FZOP2-10','Düzlem aynada görüş alanı (gözün görüntüsünden bakış)','Gözün görüntüsü aynanın arkasında göz kadar uzakta bulunur; ayna kenarlarından geçen doğrular gözün görüntüsünden çıkıyormuş gibi çizilip karşı duvarda görülebilen bölüm benzer üçgenlerle bulunur.','Ayna genişliğini görüş alanı sanmak; gözün aynaya olan uzaklığını iki kez saymak ya da hiç saymamak.','orta',4,'fz-op2-gorus-alani','Düzlem aynada görüş alanı')
ay_w,ay_d,ay_D=40,50,150
gor=Fr(ay_w*(ay_d+ay_D),ay_d); assert gor==160 and Fr(ay_w*ay_D,ay_d)==120 and Fr(ay_w*2*ay_D,ay_d)==240 and 2*ay_w==80
sc10=1/25; xe=-ay_d*sc10; xw=-ay_D*sc10-0; xw=-(ay_D+0)*sc10  # duvar aynadan 150 cm
xe=-ay_d*sc10; xw=-ay_D*sc10; hw=ay_w/2*sc10; Yw=hw*(ay_d+ay_D)/ay_d; assert abs(2*Yw*25-160)<1e-9
fo=[arka((0,-hw),(0,hw),(1,0),.16,10)]
fo.append(f'\\draw[thick,fill=white] ({xe:.3f},0) circle (.13); '+nd((xe,.35),'göz'))
for sg in (1,-1):
    fo.append(ray((xe,0),(0,sg*hw),at=.5)); fo.append(ray((0,sg*hw),(xw,sg*Yw),at=.5))
fo.append(seg((xw,-3.7),(xw,3.7),'very thick')); fo.append(f'\\fill[pattern=north east lines,pattern color=gray] ({xw-.2:.3f},-3.7) rectangle ({xw:.3f},3.7);')
fo.append(nd((xw-.1,-3.85),'duvar','below'))
fo.append(f'\\draw[<->,thin] ({xw+.45:.3f},{-Yw:.3f}) -- ({xw+.45:.3f},{Yw:.3f}); '+nd((xw+.45,0),'?','',',fill=white'))
fo.append(dim((xe+.13,0),(0,0),'$50$ cm','above'))
fo.append('\\node at (.9,0) {};')
fo.append(dim((xw,-3.45),(0,-3.45),'$150$ cm','below'))
fo.append(f'\\draw[<->,thin] (.55,{-hw}) -- (.55,{hw}); '+nd((.55,0),'$40$ cm','right'))
fo.append(nd((0,hw+.25),'ayna','above'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0010',[A('Gözün görüntüsünü bul','Ayna gözün görüntüsünü aynanın arkasında, gözle aynı uzaklıkta (50 cm) oluşturur.','Göz–görüntü: 50 + 50 = 100 cm'),
 A('Kenar ışınlarını çiz','Aynanın iki kenarından geçen ışınlar, görüntüden çıkıyormuş gibi duvara uzanır; görülen bölge bu iki doğru arasındadır.','Görüntüden duvara uzaklık: 50 + 150 = 200 cm'),
 A('Benzer üçgeni kur','Görüntüden aynaya 50 cm, duvara 200 cm; ayna genişliği 40 cm.','duvar bölümü ÷ 40 = 200 ÷ 50'),
 A('Genişliği hesapla','Oran 4 olduğundan duvardaki görülebilen bölüm ayna genişliğinin 4 katıdır.','40 × 4 = 160 cm')],
 dogru=160,yan=[(40,'Görüş alanını ayna genişliğine (40 cm) eşit almış; ışınlar duvara doğru açılır.','bilgi'),(80,'Gözle görüntüsü arasındaki 100 cm’yi duvar uzaklığı almış: 40 × 100 ÷ 50 = 80 cm.','islem'),(120,'Oranı 150 ÷ 50 = 3 almış; gözün görüntüsünün aynanın arkasında olduğunu (200 ÷ 50) hesaba katmamış.','dikkat'),(240,'Duvar uzaklığını iki katına çıkarıp (2 × 150) 40 × 300 ÷ 50 hesaplamış.','islem')],
 tipId='fz-op2-gorus-alani',tip='Düzlem aynada görüş alanı',z='orta',alt='Düzlem Ayna',kaz='Düzlem aynanın görüş alanını gözün görüntüsünden geçen ışınlarla ve benzer üçgenlerle belirler.',
 kart='K-FZOP2-10 (görüş alanı) · 40 cm ayna, 50 cm, 150 cm',kalip='şekilli',
 metin='Bir odanın yukarıdan görünümü şekilde verilmiştir. Boyutları ihmal edilecek kadar küçük bir göz, genişliği 40 cm olan düzlem aynanın tam karşısında, aynanın orta noktasından geçen dikmenin üzerinde ve aynaya 50 cm uzaklıkta durmaktadır. Gözün arkasındaki duvar aynaya paraleldir ve aynaya 150 cm uzaklıktadır. Göz, aynadan bakarak duvarın bir bölümünü görebilmektedir; ışınların izlediği yollar şekilde gösterilmiştir.\nBuna göre, gözün aynadan görebildiği duvar bölümünün genişliği kaç cm’dir?',
 istenen='Duvarın aynadan görülebilen bölümünün genişliği (cm).',
 ip=['Gözün aynadaki görüntüsünün nerede oluştuğunu bul ve ayna kenarlarından geçen ışınları o noktadan çıkıyormuş gibi uzat.'],
 bilgi=[B('Düzlem aynada görüş alanı','gözün görüntüsü aynanın arkasında, aynadan göz kadar uzakta oluşur; gözün aynadan görebildiği bölge, bu görüntüden aynanın kenarlarına çizilen doğruların arasında kalır. Örnek: görüntüden aynaya 1 birim, duvara 3 birim ise duvar bölümü ayna genişliğinin 3 katıdır')],
 puf='Görüş alanında gözün aynadaki görüntüsünden bak: ayna kenarlarından geçen doğrularla benzer üçgen kur.',sekil=SK)

# ---------- 11 · dik iki düzlem aynada ışın yolu · orta · öncüllü
kartla('K-FZOP2-11','Birbirine dik iki düzlem aynada ışının yolu','Dik iki düzlem aynaya gelen ışın iki yansımadan sonra gelen ışına paralel ve ters yönde çıkar; ikinci aynadaki gelme açısı birinci aynadakinin tamamlayıcısıdır.','Çıkan ışının gelen ışına dik ya da aynı yönlü olduğunu sanmak; ikinci yansımada açıyı birinci aynaya göre ölçmek.','orta',3,'fz-op2-kesisen-ayna','Dik iki düzlem aynada ışın yolu (öncüllü)')
al11=35; dI=(-cos(radians(al11)),-sin(radians(al11)))
Aa=(2.2,0); d1_=reflect(dI,(0,1)); Bb=(0,Aa[1]+(0-Aa[0])/d1_[0]*d1_[1]) if False else (0,2.2*tan(radians(al11)))
d2_=reflect(d1_,(1,0))
assert abs(d2_[0]+dI[0])<1e-9 and abs(d2_[1]+dI[1])<1e-9          # çıkan ışın gelene paralel, ters yönde
assert abs(d1_[0]/d1_[1]*-1-1/tan(radians(al11)))<1e-9
i1_=degrees(acos(-dot(dI,(0,1)))); i2_=degrees(acos(-dot(d1_,(1,0)))); assert abs(i1_+i2_-90)<1e-9
for a_ in (20,35,50,70):                                           # açı değişse de paralellik korunur
    d_=(-cos(radians(a_)),-sin(radians(a_))); assert reflect(reflect(d_,(0,1)),(1,0))==(-d_[0],-d_[1]) or max(abs(x+y) for x,y in zip(reflect(reflect(d_,(0,1)),(1,0)),d_))<1e-9
Sg=sub(Aa,mul(dI,2.6)); Eo=add(Bb,mul(d2_,3.0))
fo=[arka((0,0),(3.4,0),(0,-1),.2,13),arka((0,0),(0,3.4),(-1,0),.2,13)]
fo.append(f'\\draw[dashed,thin] ({Aa[0]},.0) -- ({Aa[0]},1.1); \\draw[dashed,thin] (0,{Bb[1]:.3f}) -- (1.1,{Bb[1]:.3f});')
fo.append(ray(Sg,Aa,at=.5)); fo.append(ray(Aa,Bb,at=.5)); fo.append(ray(Bb,Eo,at=.5))
fo.append(yay(Aa,.8,180+0,180+0.0001) if False else '')
fo.append(nd((Aa[0]+.55,.25),'$35^\\circ$'))
fo.append(f'\\draw[thin] ({Aa[0]+1.0:.3f},0) arc[start angle=0,end angle={al11},radius=1.0];')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0011',[A('Birinci yansımayı incele','Işın yatay aynaya çarpıp dik aynaya doğru yansır; gelme açısı kadar yansıma açısı oluşur.','yatay aynada: gelme = yansıma'),
 A('İkinci yansımayı incele','Dik aynanın normali yatay olduğundan ikinci aynadaki gelme açısı, birinci aynadakinin tamamlayıcısıdır.','θ₁ + θ₂ = 90° → II. doğru'),
 A('Çıkan ışının yönünü bul','İki yansımanın sonunda ışının hem yatay hem düşey bileşeni ters döner; çıkan ışın gelen ışına paralel ve zıt yönlüdür.','çıkan ∥ gelen → I. doğru'),
 A('Açı değişince kontrol et','Gelen ışının açısı değişse de iki aynadaki yansımalar yine bileşenleri ters çevirir; paralellik korunur.','III. doğru → I, II ve III')],
 truth=(True,True,True),harf='E',tipId='fz-op2-kesisen-ayna',tip='Dik iki düzlem aynada ışın yolu (öncüllü)',z='orta',alt='Düzlem Ayna',kaz='Birbirine dik iki düzlem aynada ışının yansıma yolunu çizerek yorumlar.',
 kart='K-FZOP2-11 (dik iki ayna, ışın yolu) · çıkan ışın gelene paralel',kalip='öncüllü',
 metin='Kenarları birleştirilmiş iki düzlem ayna, birbirine dik olacak biçimde şekildeki gibi tutulmuştur. Bir lazer göstericiden çıkan ince ışın, yatay aynaya şekilde gösterilen açıyla gelmekte, önce yatay aynadan sonra dik aynadan yansıyarak aynaların arasından çıkmaktadır. Işının yolu ile iki aynadaki normaller çizilmiştir; aynalar ışığı tamamen yansıtır ve ışın aynaların kesişim doğrusundan uzak noktalara çarpmaktadır.\nBuna göre,\nI. Işın aynalardan çıktığında gelen ışına paralel, ters yönde ilerler.\nII. Işının ikinci aynadaki gelme açısı, birinci aynadaki gelme açısının tamamlayıcısıdır.\nIII. Gelen ışının yatay aynayla yaptığı açı değiştirilirse çıkan ışın yine gelen ışına paralel olur.\nyargılarından hangileri doğrudur?',
 neden=[('çıkan ışının gelen ışına dik ya da farklı bir doğrultuda çıkacağını düşünmüş; iki yansımada ışının iki bileşeni de ters döner.','bilgi'),('ikinci aynadaki gelme açısını birinci aynadakiyle aynı sanmış; dik aynalarda iki açı birbirini 90°’ye tamamlar.','bilgi'),('paralelliğin yalnız şekildeki özel açıda geçerli olduğunu sanmış; açı değişse de iki dik aynadan yansıyan ışın gelene paraleldir.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her yansımada ışının hangi bileşeninin (yatay ya da düşey) yön değiştirdiğini düşün.'],
 bilgi=[B('Yansıma yasası','gelme açısı yansıma açısına eşittir ve ikisi de normalden ölçülür. Yatay aynada ışının düşey bileşeni, düşey aynada yatay bileşeni yön değiştirir. Örnek: yatay aynaya yukarıdan inen ışın, yatay doğrultudaki ilerleyişini korur ve yukarı doğru yansır')],
 puf='Dik iki aynada her yansıma ışının bir bileşenini ters çevirir; iki yansıma sonunda ışın geldiği yola paralel döner.',sekil=SK)

# =============================== KÜRESEL AYNALAR ===============================
def cember(p0,d,C,R,ilk=True):
    """ışının çembere çarpma noktası (t>0): ilk=True en yakın, False en uzak"""
    f_=sub(p0,C); b=2*dot(f_,d); c=dot(f_,f_)-R*R; D=b*b-4*c; assert D>=0
    ts=sorted(t for t in ((-b-sqrt(D))/2,(-b+sqrt(D))/2) if t>1e-9); return add(p0,mul(d,ts[0] if ilk else ts[-1]))
def kure_ayna(C,R,ymax,yon,n=24,tick=.14):
    """yon=+1: merkez sol, ayna sağda (çukur, ışık soldan); yon=-1 tümsek. Eğriyi ve arka taramayı çizer."""
    pts=[]
    for i in range(n+1):
        y=-ymax+2*ymax*i/n; x=C[0]+yon*sqrt(R*R-y*y); pts.append((x,y))
    o=['\\draw[very thick] '+' -- '.join(pt(p) for p in pts)+';']
    for p in pts[::2]:
        nn=nrm(sub(p,C)); nn=mul(nn,-1 if yon>0 else 1)   # merkezden dışarı (ayna arkası)
        if yon>0: nn=nrm(sub(p,C))
        else: nn=nrm(sub(C,p))
        q_=add(add(p,mul(nn,tick)),(0,-tick*.6)); o.append(f'\\draw[thin] {pt(p)} -- {pt(q_)};')
    return '\n'.join(o)
# ---------- 12 · çukur ayna özel ışınlar · kolay · öncüllü
kartla('K-FZOP2-12','Çukur aynada özel ışınların yansıma yolları','Optik eksene paralel gelen ışın yansıyınca odaktan geçer; odaktan gelen ışın eksene paralel yansır; eğrilik merkezinden gelen ışın aynaya dik çarpar ve kendi üzerinden döner.','Paralel ışının eğrilik merkezinden geçeceğini sanmak; merkezden gelen ışının odaktan geçeceğini düşünmek.','kolay',3,'fz-op2-cukur-ozel','Çukur aynada özel ışınlar (öncüllü)')
Rc=4.0; Cc=(-Rc,0); Fc=(-Rc/2,0)
H1=cember((-6.2,1.5),(1,0),Cc,Rc,False); n1=nrm(sub(Cc,H1)); r1c=reflect((1,0),(-n1[0],-n1[1]) if False else n1)
# gerçek yansıma: F'den geçer (küçük küresel sapma)
tF=(Fc[0]-H1[0])/r1c[0]; yF=H1[1]+tF*r1c[1]; assert abs(yF)<.25
H2=(-Rc+sqrt(Rc*Rc-1.2**2),-1.2)
d2=nrm(sub(H2,Fc)); S2=sub(Fc,mul(d2,1.1)); n2=nrm(sub(Cc,H2)); r2c=reflect(d2,n2); assert abs(r2c[1])<.15 and r2c[0]<0
H3=(-Rc+sqrt(Rc*Rc-.45**2),.45); d3=nrm(sub(H3,Cc)); S3=sub(Cc,mul(d3,2.0)); assert reflect(d3,mul(d3,-1))==(-d3[0],-d3[1])
fo=[kure_ayna(Cc,Rc,2.0,1)]
fo.append('\\draw[thin] (-6.7,0) -- (.8,0); '+nd((.8,0),'optik eksen','right'))
fo.append(f'\\fill {pt(Fc)} circle (1.6pt) {pt(Cc)} circle (1.6pt); '+nd((Fc[0],-.1),'F','below')+nd((Cc[0],-.1),'M','below'))
fo.append(ray((-6.2,1.5),H1,at=.35)); fo.append(ray(H1,Cc,at=.6)); fo.append(nd((-6.35,1.5),'1','left'))
fo.append(ray(S2,H2,at=.35)); fo.append(ray(H2,(-6.2,H2[1]+(-6.2-H2[0])*r2c[1]/r2c[0]),at=.5)); fo.append(nd((S2[0]-.08,S2[1]),'2','left'))
fo.append(ray(S3,H3,at=.25)); fo.append(ray(H3,S3,at=.18)); fo.append(nd((S3[0],S3[1]-.15),'3','below'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0012',[A('1 numaralı ışını incele','Optik eksene paralel gelen ışın yansıdıktan sonra odak noktasından (F) geçmelidir; çizimde ise eğrilik merkezine (M) gidiyor.','Paralel ışın → F’den geçer; çizim yanlış → I. yanlış'),
 A('2 numaralı ışını incele','Odak noktasından geçerek gelen ışın optik eksene paralel yansır; çizim buna uygundur.','F’den gelen → eksene paralel → II. doğru'),
 A('3 numaralı ışını incele','Eğrilik merkezinden geçen ışın aynaya dik çarpar ve aynı yoldan geri döner; çizim doğrudur.','M’den gelen → kendi üzerinden döner → III. doğru → II ve III')],
 truth=(False,True,True),harf='D',tipId='fz-op2-cukur-ozel',tip='Çukur aynada özel ışınlar (öncüllü)',z='kolay',alt='Küresel Aynalar',kaz='Çukur aynaya gelen özel ışınların yansıma yollarının doğru çizilip çizilmediğini belirler.',
 kart='K-FZOP2-12 (çukur ayna, üç özel ışın) · biri yanlış çizilmiş',kalip='öncüllü',
 metin='Bir öğrenci, odak noktası F ve eğrilik merkezi M olan çukur aynaya gelen üç ışının yansıma yollarını şekildeki gibi çizmiştir. 1 numaralı ışın optik eksene paralel gelmektedir, 2 numaralı ışın odak noktasından geçerek aynaya ulaşmaktadır, 3 numaralı ışın ise aynanın eğrilik merkezinden geçerek aynaya gelmektedir. Çizilen yansıyan ışınların bazıları yanlış olabilir.\nBuna göre,\nI. 1 numaralı ışının yansıma yolu doğru çizilmiştir.\nII. 2 numaralı ışının yansıma yolu doğru çizilmiştir.\nIII. 3 numaralı ışının yansıma yolu doğru çizilmiştir.\nyargılarından hangileri doğrudur?',
 neden=[('paralel gelen ışının yansıyınca eğrilik merkezinden geçtiğini sanmış; oysa odak noktasından geçer.','bilgi'),('odak noktasından gelen ışının eksene paralel yansıdığını bilmemiş.','bilgi'),('merkezden gelen ışının aynaya dik çarptığı için kendi üzerinden geri döneceğini fark etmemiş.','bilgi')],
 istenen='Yansıma yolu doğru çizilen ışınların belirlenmesi.',
 ip=['Her gelen ışının hangi özel ışın türüne girdiğini belirle ve o türün yansıma kuralını hatırla.'],
 bilgi=[B('Çukur aynada özel ışınlar','optik eksene paralel gelen ışın yansıyınca odak noktasından geçer; odak noktasından gelen ışın eksene paralel yansır; eğrilik merkezinden gelen ışın aynaya dik çarptığından kendi üzerinden geri döner. Örnek: eksene paralel gelen her ışın yansıdıktan sonra aynı noktada (F) birleşir')],
 puf='Paralel ↔ odak; merkezden gelen ışın aynı yoldan geri döner. Bu üç kuralla çukur aynadaki her çizimi denetleyebilirsin.',sekil=SK)

# ---------- 13 · çukur ayna görüntü özellikleri · orta · öncüllü
kartla('K-FZOP2-13','Çukur aynada F ile M arasındaki cismin görüntü özellikleri','Cisim F ile M arasındayken görüntü M’nin ötesinde, gerçek, ters ve cisimden büyük oluşur; perdede yakalanabilir.','Görüntüyü F ile ayna arasında sanmak; gerçek görüntünün düz olduğunu düşünmek.','orta',3,'fz-op2-cukur-goruntu','Çukur aynada görüntü özellikleri (öncüllü)')
fa=Rc/2; dc=3.0; v=1/(1/fa-1/dc); mm_=-v/dc
assert fa<dc<2*fa and v>2*fa and v>0 and mm_<-1 and abs(v-6)<1e-9
fo=[kure_ayna(Cc,Rc,1.8,1)]
fo.append('\\draw[thin] (-5.2,0) -- (.8,0);')
Xc=-dc
fo.append(f'\\draw[very thick,-{{Stealth[length=2mm,width=1.8mm]}}] ({Xc},0) -- ({Xc},.65); '+nd((Xc,-.1),'cisim','below'))
fo.append(f'\\fill {pt(Fc)} circle (1.6pt) {pt(Cc)} circle (1.6pt); '+nd((Fc[0],.1),'F','above')+nd((Cc[0],.1),'M','above'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0013',[A('Cismin konumunu belirle','Cisim F ile M arasında, yani odak uzaklığı ile eğrilik yarıçapı arasındadır.','f < d < 2f'),
 A('Görüntüyü yorumla','Bu konumda görüntü M’nin ötesinde, gerçek, ters ve cisimden büyük oluşur; perde üzerinde yakalanabilir.','gerçek, ters, büyük → I. doğru, III. doğru'),
 A('Konumu kontrol et','Görüntü ayna ile F arasında değil, M’nin ötesinde oluşur; II. yanlış.','görüntü M’nin ötesinde → I ve III')],
 truth=(True,False,True),harf='C',tipId='fz-op2-cukur-goruntu',tip='Çukur aynada görüntü özellikleri (öncüllü)',z='orta',alt='Küresel Aynalar',kaz='Çukur aynada F ile M arasına konan cismin görüntüsünün konumunu ve özelliklerini nitel olarak belirler.',
 kart='K-FZOP2-13 (çukur ayna, cisim F ile M arası) · gerçek, ters, büyük',kalip='öncüllü',
 metin='Odak noktası F ve eğrilik merkezi M olan çukur aynanın optik ekseni üzerinde, aynaya dik duran küçük bir ok biçimli cisim, F ile M arasında şekildeki konuma yerleştirilmiştir. Öğrenci, ayna önüne bir perde koyup perdeyi ayna ile cisim arasından uzağa doğru yavaşça hareket ettirerek cismin görüntüsünü yakalamaya çalışıyor.\nBuna göre,\nI. Cismin görüntüsü gerçektir ve perde üzerinde yakalanabilir.\nII. Görüntü ayna ile F noktası arasında oluşur.\nIII. Görüntü cisimden büyük ve terstir.\nyargılarından hangileri doğrudur?',
 neden=[('görüntünün sanal olduğunu sanmış; çukur aynada F’nin dışındaki cisimlerin görüntüsü gerçektir.','bilgi'),('görüntünün konumunu F ile ayna arasında sanmış; cisim F ile M arasındayken görüntü M’nin ötesindedir.','bilgi'),('F ile M arasındaki cismin görüntüsünün küçük ve düz olduğunu düşünmüş.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Cismin F, M noktalarına göre konumunu belirleyip bu konumdaki görüntünün yerini ve özelliklerini düşün.'],
 bilgi=[B('Çukur aynada görüntü','cisim F’nin dışındaysa görüntü gerçek ve terstir; F ile M arasındaysa görüntü M’nin ötesinde ve büyüktür, M’nin dışındaysa görüntü F ile M arasında ve küçüktür. Cisim F ile ayna arasındaysa görüntü sanal, düz ve büyüktür')],
 puf='Çukur aynada cisim F’den uzaktaysa görüntü gerçek ve terstir; cisim aynaya yaklaştıkça görüntü uzaklaşır ve büyür.',sekil=SK)

# ---------- 14 · tümsek ayna · kolay · tek cevap
kartla('K-FZOP2-14','Tümsek aynada görüntü ve kullanım alanı','Tümsek aynada cisim nerede olursa olsun görüntü ayna arkasında sanal, düz ve küçük oluşur; geniş görüş alanı sağladığı için dikiz aynası ve güvenlik aynası olarak kullanılır.','Çukur aynadaki gerçek–ters görüntü kurallarını tümsek aynaya uygulamak; ışınların yansıdıktan sonra odakta kesiştiğini sanmak.','kolay',3,'fz-op2-tumsek','Tümsek aynada görüntü ve kullanım alanı')
Rv=4.0; Cv=(Rv,0); Fv=(Rv/2,0)
yh=.9; Hp=cember((-3.3,yh),(1,0),Cv,Rv,True); assert abs(Hp[0]-(Rv-sqrt(Rv*Rv-yh*yh)))<1e-9
nv=nrm(sub(Hp,Cv)); rv=reflect((1,0),nv); assert rv[0]<0 and rv[1]>0
tb=(Fv[0]-Hp[0])/rv[0]; assert abs(Hp[1]+tb*rv[1])<.12                                   # uzantı F'den geçer (küçük küresel sapma)
S2v=(-3.3,yh); H2v=cember(S2v,nrm(sub(Cv,S2v)),Cv,Rv,True); d2v=nrm(sub(Cv,H2v))
fo=[kure_ayna(Cv,Rv,1.7,-1)]
fo.append('\\draw[thin] (-4.9,0) -- (4.9,0);')
fo.append(f'\\fill {pt(Fv)} circle (1.6pt) {pt(Cv)} circle (1.6pt); '+nd((Fv[0],-.1),'F','below')+nd((Cv[0],-.1),'M','below'))
fo.append(f'\\draw[very thick,-{{Stealth[length=2mm,width=1.8mm]}}] (-3.3,0) -- (-3.3,{yh}); '+nd((-3.3,-.1),'araç','below'))
fo.append(ray((-3.3,yh),Hp,at=.5)); fo.append(ray(Hp,add(Hp,mul(rv,2.4)),at=.55))
fo.append(ray(S2v,H2v,at=.45)); fo.append(ray(H2v,S2v,at=.12))
fo.append(f'\\draw[dashed] {pt(Hp)} -- {pt(Fv)}; \\draw[dashed] {pt(H2v)} -- {pt(Cv)};')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
dg_t='Görüntü, araç nerede olursa olsun aynanın arkasında sanal, düz ve araçtan küçük oluşur.'
qt('0014',[A('Özel ışınları oku','Optik eksene paralel gelen ışın yansıdıktan sonra ıraksar; uzantısı ayna arkasındaki F noktasından geçer.','Yansıyan ışınlar kesişmez, ıraksar'),
 A('Görüntüyü belirle','Işınlar kesişmediği için gerçek görüntü oluşmaz; uzantıların kesiştiği yerde sanal, düz ve küçük görüntü görülür.','sanal, düz, küçük'),
 A('Kullanım alanını bağla','Görüntünün küçük olması geniş görüş alanı sağlar; bu yüzden dikiz ve güvenlik aynalarında kullanılır.','geniş görüş alanı → dikiz aynası'),
 A('Şıkları ele','Gerçek, ters ya da perdede yakalanabilen görüntü iddiaları tümsek ayna için yanlıştır.','Doğru ifade: sanal, düz, küçük')],
 dogru=dg_t,yan=[('Araç F noktasının dışında bulunduğunda görüntü, aynanın önünde gerçek ve ters oluşur; araç yaklaşırsa büyür.','Çukur aynanın kuralını tümsek aynaya uygulamış; tümsek aynada gerçek görüntü oluşmaz.','bilgi'),
  ('Araç aynaya yaklaştıkça görüntüsü büyür ve sonunda araçtan daha büyük hâle gelerek ters döner.','Görüntü yaklaştıkça büyür ama hiçbir zaman cisimden büyük olmaz; tümsek ayna her konumda küçültür.','bilgi'),
  ('Yansıyan ışınlar odak noktasında kesiştiğinden görüntü bir perde üzerinde net olarak yakalanabilir.','Işınların odakta kesiştiğini sanmış; tümsek aynada yansıyan ışınlar ıraksar, kesişmez.','bilgi'),
  ('Bu ayna düz aynaya göre daha dar bir görüş alanı sağladığı için dikiz aynası olarak tercih edilir.','Görüş alanının daralacağını düşünmüş; tümsek ayna geniş görüş alanı sağlar.','bilgi')],
 harf='A',tipId='fz-op2-tumsek',tip='Tümsek aynada görüntü ve kullanım alanı',z='kolay',alt='Küresel Aynalar',kaz='Tümsek aynada oluşan görüntünün özelliklerini ve kullanım alanlarını belirtir.',
 kart='K-FZOP2-14 (tümsek ayna) · sanal, düz, küçük',kalip='şekilli',
 metin='Bir sitenin otopark çıkışında, köşeyi dönen sürücülerin karşıdan gelen araçları önceden görebilmesi için tümsek (dışbükey) bir ayna asılmıştır. Şekilde aynanın optik ekseni üzerinde duran bir araç ile aynanın arkasında kalan odak noktası F ve eğrilik merkezi M işaretlenmiştir. Araçtan çıkıp aynaya gelen iki özel ışının yansıma yolları da çizilmiştir.\nBuna göre, bu ayna ile ilgili aşağıdaki ifadelerden hangisi doğrudur?',
 istenen='Tümsek aynayla ilgili doğru ifade.',
 ip=['Yansıyan ışınların kesişip kesişmediğine bak; kesişmiyorlarsa görüntünün hangi türde olacağını düşün.'],
 bilgi=[B('Tümsek ayna','tümsek aynada yansıyan ışınlar ıraksar; uzantıları ayna arkasında kesişir. Cisim nerede olursa olsun görüntü sanal, düz ve küçüktür; geniş görüş alanı sağladığından dikiz ve güvenlik aynalarında kullanılır. Örnek: araç aynasında aynı araç gerçek boyundan küçük görünür')],
 puf='Tümsek ayna: her zaman sanal, düz, küçük görüntü ve geniş görüş alanı.',sekil=SK)

# =============================== KIRILMA ===============================
# ---------- 15 · üç ortamda kırılma · orta · öncüllü
kartla('K-FZOP2-15','Üç ortamdan geçen ışının yoluna göre ışık hızı ve kırılma indisi','Işık normale yaklaşarak kırılıyorsa ikinci ortamın kırılma indisi daha büyük, ışığın hızı daha küçüktür; gelme (kırılma) açısı büyük olan ortamda kırılma indisi küçük, ışık hızı büyüktür.','Normale yaklaşan ışığın hızlandığını sanmak; kırılma açısı büyük olan ortamın daha yoğun olduğunu düşünmek.','orta',4,'fz-op2-kirilma-ortamlar','Üç ortamda kırılma, ışık hızı ve kırılma indisi (öncüllü)')
nK,nL,nM=1.3,1.7,1.1; tK=radians(50)
tL=asin(nK*sin(tK)/nL); tM=asin(nK*sin(tK)/nM)
assert degrees(tL)<50<degrees(tM) and nL>nK>nM and abs(degrees(tL)-35.9)<.1 and abs(degrees(tM)-64.9)<.2
yK,yL,yM,yB=2.7,1.5,.3,-.9; x0=-1.5
x1=x0+(yK-yL)*tan(tK); x2=x1+(yL-yM)*tan(tL); x3=x2+(yM-yB)*tan(tM)
fo=[]
for y in (yK,yL,yM,yB): fo.append(seg((-2.7,y),(3.4,y),'thick' if y in (yK,yB) else 'thick'))
fo.append(seg((-2.7,yB),(-2.7,yK),'thick')); fo.append(seg((3.4,yB),(3.4,yK),'thick'))
for y,n_ in ((2.1,'K'),(.9,'L'),(-.3,'M')): fo.append(nd((3.0,y),n_))
for x,y in ((x1,yL),(x2,yM)): fo.append(f'\\draw[dashed,thin] ({x:.3f},{y+.6:.3f}) -- ({x:.3f},{y-.6:.3f});')
fo.append(f'\\draw[dashed,thin] ({x0:.3f},{yK+.4:.3f}) -- ({x0:.3f},{yK-.5:.3f});')
fo.append(ray((x0,yK),(x1,yL),at=.5)); fo.append(ray((x1,yL),(x2,yM),at=.5)); fo.append(ray((x2,yM),(x3,yB),at=.5))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0015',[A('K’den L’ye geçişi incele','Işın normale yaklaşıyor; L’nin kırılma indisi K’ninkinden büyüktür, ışık L’de daha yavaştır.','n_L > n_K'),
 A('L’den M’ye geçişi incele','Işın normalden uzaklaşıyor; M’nin kırılma indisi L’ninkinden küçüktür. M’deki açı K’dakinden de büyük olduğundan n_M < n_K.','n_M < n_K < n_L'),
 A('Hızları sırala','Kırılma indisi büyük olan ortamda ışık yavaştır: en yavaş L, en hızlı M.','v_M > v_K > v_L → I. ve II. doğru'),
 A('III. yargıyı denetle','K’nin kırılma indisi M’ninkinden küçük değil, büyüktür.','n_K > n_M → III. yanlış → I ve II')],
 truth=(True,True,False),harf='C',tipId='fz-op2-kirilma-ortamlar',tip='Üç ortamda kırılma, ışık hızı ve kırılma indisi (öncüllü)',z='orta',alt='Kırılma',kaz='Işığın ortam değiştirirken normale yaklaşma ya da uzaklaşma yönüne göre ortamların kırılma indisini ve ışık hızını sıralar.',
 kart='K-FZOP2-15 (üç ortam, kırılma yönü) · n_L > n_K > n_M',kalip='öncüllü',
 metin='Tek renkli bir ışık ışını, paralel yüzlü ve şeffaf üç ortamdan (K, L ve M) oluşan bir levhaya, şekildeki gibi üstten gönderilmiştir. Işının her ara yüzeyde izlediği yol ve ara yüzeylere çizilen normaller şekilde gösterilmiştir. Ortamlar homojendir ve ışın yalnızca kırılma yoluyla ilerlemektedir.\nBuna göre,\nI. Işığın en yavaş ilerlediği ortam L’dir.\nII. Işığın en hızlı ilerlediği ortam M’dir.\nIII. K ortamının kırılma indisi, M ortamının kırılma indisinden küçüktür.\nyargılarından hangileri doğrudur?',
 neden=[('normale yaklaşan ışının hızlandığını düşünmüş; normale yaklaşırken ışık yavaşlar.','bilgi'),('M’deki kırılma açısının büyük olmasını, M’nin daha yoğun olduğu biçiminde yorumlamış; açı büyük olan ortamda ışık daha hızlıdır.','bilgi'),('K’deki açının M’deki açıdan küçük olmasını K’nin kırılma indisinin daha küçük olduğu biçiminde yorumlamış; açı küçük olan ortamın kırılma indisi daha büyüktür.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Işın her ara yüzeyde normale yaklaşıyor mu uzaklaşıyor mu? Bunu ortamların yoğunluğu ve ışık hızıyla ilişkilendir.'],
 bilgi=[B('Normale göre kırılma','ışık kırılma indisi küçük ortamdan büyük ortama geçerken normale yaklaşır ve yavaşlar; büyükten küçüğe geçerken normalden uzaklaşır ve hızlanır. Örnek: havadan suya geçen ışın normale yaklaşır, sudaki hızı havadakinden küçüktür'),
        B('Açı ve kırılma indisi','normalle yapılan açı büyükse o ortamın kırılma indisi küçük, ışık hızı büyüktür')],
 puf='Normale yaklaşan ışık yavaş (yoğun) ortama, normalden uzaklaşan ışık hızlı (az yoğun) ortama geçmiştir.',sekil=SK)

# ---------- 16 · görünür derinlik · orta · tek cevap
kartla('K-FZOP2-16','Sudaki cismin görünür derinliği ve ışının kırılma yönü','Sudan havaya geçen ışın normalden uzaklaşır; gözlemci ışının uzantısında gördüğü için sudaki cismi gerçek konumundan daha sığda görür.','Işığın doğrusal gittiği için cismin gerçek yerinde görüneceğini sanmak; ışının sudan havaya geçerken normale yaklaştığını düşünmek.','orta',3,'fz-op2-gorunur-derinlik','Görünür derinlik ve ışının kırılma yönü')
nw=4/3; Kp=(0,-2.2); Ey=(4.2,1.6)
def gfun(xs): return nw*xs/sqrt(xs*xs+2.2**2)-(Ey[0]-xs)/sqrt((Ey[0]-xs)**2+Ey[1]**2)
lo,hi=0.0,Ey[0]
for _ in range(80):
    mid=(lo+hi)/2
    if gfun(mid)<0: lo=mid
    else: hi=mid
xs=(lo+hi)/2; Sp=(xs,0.0); uE=nrm(sub(Ey,Sp)); tL_=xs/uE[0]; yL_=-tL_*uE[1]
th1=atan2(xs,2.2); th2=atan2(Ey[0]-xs,Ey[1]); assert abs(nw*sin(th1)-sin(th2))<1e-9 and th2>th1 and -2.2<yL_<0
fo=[f'\\fill[fill=vurgu!12] (-1.2,0) rectangle (5.3,-3.1);']
fo.append('\\draw[thick] (-1.2,0) -- (5.3,0); '+nd((-1.15,.2),'hava','above right')+nd((-1.15,-.2),'su','below right'))
fo.append(f'\\fill {pt(Kp)} circle (2.2pt); '+nd((Kp[0]-.15,Kp[1]),'K','left'))
fo.append(f'\\draw[thick] {pt((0,yL_))} circle (.08); '+nd((-.15,yL_),'L','left'))
fo.append(f'\\draw[dashed,thin] ({xs:.3f},.7) -- ({xs:.3f},-.7);')
fo.append(ray(Kp,Sp,at=.5)); fo.append(ray(Sp,Ey,at=.5))
fo.append(f'\\draw[dashed,thick] {pt(Sp)} -- {pt((0,yL_))};')
fo.append(f'\\draw[thick,fill=white] {pt(Ey)} circle (.15); '+nd((Ey[0],Ey[1]+.3),'gözlemci'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
dg_t='Işık sudan havaya geçerken normalden uzaklaşır; bu nedenle balık L noktasında, gerçek derinliğinden daha sığda görünür.'
qt('0016',[A('Işığın yolunu oku','Balıktan çıkan ışın su yüzeyinde kırılıp gözlemciye ulaşıyor; sudan havaya geçerken normalden uzaklaşıyor.','suda θ₁ < havada θ₂'),
 A('Gözün gördüğü yeri bul','Göz, ışının geldiği doğrultuyu geriye doğru uzatır; uzantılar L noktasında buluşur.','görüntü L noktasında'),
 A('Konumu karşılaştır','L noktası K’dan yüzeye daha yakındır: balık gerçek derinliğinden daha sığda görünür.','görünür derinlik < gerçek derinlik')],
 dogru=dg_t,yan=[('Işık doğrusal yayıldığı için balık gözlemciye gerçek konumu olan K noktasında görünür.','Işığın su yüzeyinde kırıldığını ve gözün ışının uzantısında gördüğünü hesaba katmamış.','bilgi'),
  ('Işık sudan havaya geçerken normale yaklaşır; bu yüzden balık gerçek derinliğinden daha derinde görünür.','Işının kırılma yönünü ters yorumlamış; sudan havaya geçen ışın normalden uzaklaşır ve görüntü yüzeye yaklaşır.','bilgi'),
  ('Işığın havadaki hızı sudakinden küçük olduğu için kırılma olur ve balık K noktasının altında görünür.','Işığın hızının havada daha büyük olduğunu bilmemiş; görüntü K’nın üstünde, yüzeye yakın oluşur.','bilgi'),
  ('Balığın L noktasındaki görüntüsü gerçek ve terstir; bu yüzden gözlemci balığı K’dan daha derinde görür.','Kırılma sonucu oluşan görüntünün sanal olduğunu ve daha sığda göründüğünü bilmemiş.','bilgi')],
 harf='B',tipId='fz-op2-gorunur-derinlik',tip='Görünür derinlik ve ışının kırılma yönü',z='orta',alt='Kırılma',kaz='Su içindeki cismin görünür konumunu, ışığın sudan havaya kırılma yönüyle ilişkilendirir.',
 kart='K-FZOP2-16 (havuz, balık, görünür derinlik) · nitel',kalip='şekilli',
 metin='Bir akvaryumun yandan görünümü şekilde verilmiştir. Akvaryumdaki K balığından çıkan bir ışın su yüzeyinde kırılarak kenarda duran gözlemcinin gözüne ulaşmakta, gözlemci ise balığı ışının geldiği doğrultunun uzantısındaki L noktasında görmektedir. Işının su yüzeyindeki normali kesik çizgiyle gösterilmiştir ve gözlemci akvaryumun dışındadır.\nBuna göre, bu olayla ilgili aşağıdakilerden hangisi doğrudur?',
 istenen='Balığın görünür konumu ve kırılma yönüyle ilgili doğru ifade.',
 ip=['Işın su yüzeyini geçerken normale göre hangi yöne kırılıyor? Gözün ışığı hangi doğrultuda geliyormuş gibi algıladığını düşün.'],
 bilgi=[B('Görünür derinlik','sudan havaya geçen ışın normalden uzaklaşır; göz ışığın havadaki doğrultusunu geriye uzatarak cismi görür. Bu yüzden sudaki cisimler gerçek derinliklerinden daha sığda (yüzeye yakın) görünür. Örnek: havuzun tabanı olduğundan daha yakın görünür')],
 puf='Sudaki cisimler olduklarından daha yüzeye yakın görünür; çünkü ışık sudan havaya geçerken normalden uzaklaşır.',sekil=SK)

# ---------- 17 · tam yansıma ve sınır açısı · zor · öncüllü
kartla('K-FZOP2-17','Cam–hava ara yüzeyinde sınır açısı ve tam yansıma','Işık yoğun ortamdan az yoğun ortama geçerken gelme açısı sınır açısından küçükse kırılır, sınır açısına eşitse kırılma açısı 90° olur, büyükse tam yansıma yapar; tam yansıma yalnız yoğun ortamdan az yoğun ortama gelirken olur.','Sınır açısından küçük açıyı tam yansıma sanmak; tam yansımanın havadan cama geçerken de olabileceğini düşünmek.','orta',4,'fz-op2-tam-yansima','Sınır açısı ve tam yansıma (öncüllü)')
nc=1.5; thc=asin(1/nc); assert abs(degrees(thc)-41.81)<.01
a1,a2=radians(25),radians(60); assert a1<thc<a2
b1=asin(nc*sin(a1)); assert degrees(b1)>25 and nc*sin(a2)>1
Lr=1.9; x1_,x3_,x2_=-3.4,-.7,2.5
fo=['\\fill[gray!15] (-4.3,0) rectangle (4.3,-2.1);','\\draw[thick] (-4.3,0) -- (4.3,0);',nd((-4.25,.25),'hava','above right'),nd((-4.25,-.25),'cam','below right')]
for x in (x1_,x3_,x2_): fo.append(f'\\draw[dashed,thin] ({x},{1.5}) -- ({x},-1.5);')
for x,a_,n_ in ((x1_,a1,'1'),(x3_,thc,'3'),(x2_,a2,'2')):
    S=(x-Lr*sin(a_),-Lr*cos(a_)); fo.append(ray(S,(x,0),at=.5)); fo.append(nd((S[0]-.05,S[1]),n_,'left'))
fo.append(ray((x1_,0),(x1_+Lr*sin(b1),Lr*cos(b1)),at=.5))
fo.append(f'\\draw[vurgu,thick,postaction={{decorate,decoration={{markings,mark=at position .6 with {{\\arrow{{Stealth[length=1.9mm,width=1.7mm]}}}}}}}}] ({x3_},0) -- ({x3_+1.6},0);')
fo.append(ray((x2_,0),(x2_+Lr*sin(a2),-Lr*cos(a2)),at=.55))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0017',[A('1 numaralı ışını incele','Işın havaya kırılarak geçiyor; bu, gelme açısının sınır açısından küçük olduğunu gösterir.','θ₁ < θ_sınır → I. yanlış'),
 A('2 numaralı ışını incele','Işın ara yüzeyden geri dönüyor; gelme açısı sınır açısından büyük olduğundan tam yansıma gerçekleşir.','θ₂ > θ_sınır → II. doğru'),
 A('Havadan cama geçişi düşün','Tam yansıma yalnız yoğun ortamdan az yoğun ortama gelirken olur; havadan cama gelen ışık hep kırılır.','III. yanlış → Yalnız II')],
 truth=(False,True,False),harf='A',tipId='fz-op2-tam-yansima',tip='Sınır açısı ve tam yansıma (öncüllü)',z='orta',alt='Kırılma',kaz='Işığın yoğun ortamdan az yoğun ortama geçerken sınır açısına göre kırılma ve tam yansıma durumlarını ayırt eder.',
 kart='K-FZOP2-17 (cam–hava, üç ışın) · θ < θc, θ = θc, θ > θc',kalip='öncüllü',
 metin='Cam bir levhanın içindeki üç ışın, levhanın hava ile sınırındaki yüzeye farklı açılarla çarpmaktadır. Şekilde bu ışınların ara yüzeyden sonraki yolları ve ara yüzeye çizilen normaller gösterilmiştir. 3 numaralı ışın ara yüzey boyunca hava tarafına doğru ilerlemektedir. Cam homojen ve şeffaftır, ışınlar tek renklidir.\nBuna göre,\nI. 1 numaralı ışın havaya geçebilmiştir, çünkü gelme açısı sınır açısından büyüktür.\nII. 2 numaralı ışın tam yansımaya uğramıştır, çünkü gelme açısı sınır açısından büyüktür.\nIII. Işık havadan cama gelirken gelme açısı yeterince büyükse tam yansıma gözlenebilir.\nyargılarından hangileri doğrudur?',
 neden=[('1 numaralı ışının havaya geçmesini, gelme açısının büyük olmasına bağlamış; havaya geçebilmesi için gelme açısı sınır açısından küçük olmalıdır.','bilgi'),('gelme açısı sınır açısını aştığında ışığın havaya geçmeyip yansıdığını bilmemiş.','bilgi'),('tam yansımanın havadan cama geçerken de olabileceğini sanmış; yalnız yoğun ortamdan az yoğun ortama gelirken olur.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['3 numaralı ışının hangi özel durumu gösterdiğini bul; diğer ışınları bu ışınla gelme açısı bakımından karşılaştır.'],
 bilgi=[B('Sınır açısı ve tam yansıma','ışık yoğun ortamdan az yoğun ortama geçerken kırılma açısının 90° olduğu gelme açısına sınır açısı denir. Gelme açısı sınır açısından büyükse ışık yeni ortama geçemez, tamamen yansır. Örnek: sudan havaya gelen ışın için sınır açısından büyük her açıda tam yansıma olur')],
 puf='Tam yansıma için iki koşul: ışık yoğun ortamdan az yoğun ortama gitmeli ve gelme açısı sınır açısından büyük olmalı.',sekil=SK)

# ---------- 18 · fiber optik · orta · tek cevap
kartla('K-FZOP2-18','Fiber optik kablonun çalışma ilkesi','Fiber optik kabloda çekirdeğin kırılma indisi kılıftan büyüktür; ışık çekirdek–kılıf ara yüzeyine sınır açısından büyük açıyla çarpıp tam yansıyarak ilerler.','Işığın kılıfa kırılarak geçtiğini sanmak; kılıfın kırılma indisinin daha büyük olması gerektiğini düşünmek.','orta',3,'fz-op2-fiber','Fiber optik kabloda tam yansıma')
nco,ncl=1.5,1.3; thc2=asin(ncl/nco); inc=radians(70); assert inc>thc2 and degrees(thc2)<61
al_=radians(20); pts=[(0,-.2)]; x_,y_=0,-.2; dy=1
while True:
    tgt=.5 if dy>0 else -.5; xn=x_+(tgt-y_)/(dy*tan(al_))
    if xn>7.0: pts.append((7.0,y_+dy*(7.0-x_)*tan(al_))); break
    pts.append((xn,tgt)); x_,y_=xn,tgt; dy=-dy
fo=['\\draw[thick] (0,-.5) rectangle (7,.5);',
    '\\fill[gray!25] (0,.5) rectangle (7,.85); \\fill[gray!25] (0,-.5) rectangle (7,-.85);','\\draw[thick] (0,.85) -- (7,.85); \\draw[thick] (0,-.85) -- (7,-.85);','\\draw[thick] (0,-.5) -- (7,-.5); \\draw[thick] (0,.5) -- (7,.5);',
    nd((-.1,.0),'çekirdek','left'),nd((3.5,1.1),'kılıf','above'),nd((3.5,-1.1),'kılıf','below')]
for a,b in zip(pts,pts[1:]): fo.append(ray(a,b,at=.5))
bx=pts[1]; fo.append(f'\\draw[dashed,thin] ({bx[0]:.3f},.5) -- ({bx[0]:.3f},-.2); '+f'\\draw[thin] ({bx[0]:.3f},-.0) arc[start angle=-90,end angle=-90+0,radius=.3];')
fo.append(f'\\node at ({bx[0]+.4:.3f},.12) {{$\\theta$}};')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
dg_t='Çekirdeğin kırılma indisi kılıfınkinden büyüktür ve ışık sınır açısından büyük açıyla çarptığı için tam yansıyarak ilerler.'
qt('0018',[A('Işının yolunu oku','Işın çekirdek–kılıf ara yüzeyinden kılıfa geçmiyor; her çarpmada çekirdeğe geri yansıyor.','tam yansıma tekrarlanıyor'),
 A('Kırılma indislerini karşılaştır','Tam yansıma için ışık yoğun ortamdan az yoğun ortama gelmelidir; çekirdek daha yoğundur.','n_çekirdek > n_kılıf'),
 A('Açı koşulunu ekle','Gelme açısı (normalle) sınır açısından büyük olduğundan ışık kılıfa geçemez.','θ > θ_sınır'),
 A('Doğru şıkkı seç','Ele alınan ifade bu üç koşulu birlikte içerir.','çekirdek yoğun + θ > sınır → tam yansıma')],
 dogru=dg_t,yan=[('Işık çekirdek–kılıf ara yüzeyinde kırılarak kılıfa geçer; bu yüzden kablonun uzunluğu boyunca kılıfta da ilerler.','Işığın kılıfa geçtiğini sanmış; fiberde ışık tam yansımayla çekirdekte hapsolur.','bilgi'),
  ('Tam yansımanın olabilmesi için kılıfın kırılma indisinin çekirdeğinkinden büyük olması gerekir.','Koşulu tersine yazmış; tam yansıma yoğun ortamdan az yoğun ortama gelirken olur.','bilgi'),
  ('Işık çekirdek–kılıf ara yüzeyine sınır açısından küçük bir açıyla çarptığında kablo boyunca ilerleyebilir.','Sınır açısından küçük açıda ışığın kırılıp kılıfa geçeceğini göz ardı etmiş.','bilgi'),
  ('Kablo bükülürse çekirdekteki ışığın tamamı bir anda kılıfa kırılır ve iletim tamamen durur.','Sınır açısı koşulu sağlandıkça kablo bükülse de ışık ilerleyebileceğini bilmemiş.','dikkat')],
 harf='A',tipId='fz-op2-fiber',tip='Fiber optik kabloda tam yansıma',z='orta',alt='Kırılma',kaz='Fiber optik kabloda ışığın tam yansımayla iletilmesinin koşullarını açıklar.',
 kart='K-FZOP2-18 (fiber optik) · çekirdek–kılıf, tam yansıma',kalip='şekilli',
 metin='Bir internet servis sağlayıcısı, veriyi ışık sinyalleriyle taşıyan fiber optik kablo kullanmaktadır. Kablonun uzunlamasına kesiti şekilde gösterilmiştir: çekirdeğe giren bir ışın, çekirdek ile kılıf arasındaki ara yüzeylerde ardışık yansımalar yaparak ilerlemekte ve ilk çarpma noktasında normalle θ açısı yapmaktadır. Kablodaki ışık tek renklidir ve çekirdek ile kılıf şeffaf malzemelerdir.\nBuna göre, bu kablonun çalışmasıyla ilgili aşağıdakilerden hangisi doğrudur?',
 istenen='Fiber optik kablodaki ışık iletimiyle ilgili doğru ifade.',
 ip=['Işık çekirdek–kılıf ara yüzeyinde kılıfa geçiyor mu yoksa geri mi dönüyor? Bunun hangi koşullarla mümkün olduğunu düşün.'],
 bilgi=[B('Fiber optik kablo','çekirdeği kılıfından daha büyük kırılma indisli şeffaf bir malzemeden yapılmış ince kablodur. Işık, ara yüzeye sınır açısından büyük açıyla çarptığı için her seferinde tam yansır ve kayıpsıza yakın biçimde taşınır. Örnek: internet ve tıbbi endoskopide kullanılır')],
 puf='Fiber optikte iki koşul: çekirdek kılıftan yoğun olmalı ve ışık ara yüzeye sınır açısından büyük açıyla gelmelidir.',sekil=SK)

# =============================== MERCEKLER ===============================
ARR2='{Stealth[length=2.2mm,width=2mm]}'
def ince_mercek(h=1.7): return f'\\draw[{ARR2}-{ARR2},thick] (0,{-h}) -- (0,{h});'
def kalin_mercek(h=1.5):
    return f'\\draw[thick] (-.2,{h}) -- (.2,{h}) .. controls (.03,{h/3}) and (.03,{-h/3}) .. (.2,{-h}) -- (-.2,{-h}) .. controls (-.03,{-h/3}) and (-.03,{h/3}) .. (-.2,{h}) -- cycle;'
# ---------- 19 · ıraksak mercek · kolay · tek cevap
kartla('K-FZOP2-19','Kalın kenarlı (ıraksak) merceğin görüntü özellikleri','Kalın kenarlı mercek cismin konumu ne olursa olsun mercek önünde sanal, düz ve cisimden küçük görüntü verir; miyop gözlüklerinde kullanılır.','İnce kenarlı merceğin gerçek–ters görüntü kurallarını kalın kenarlı mercek için de geçerli saymak.','kolay',3,'fz-op2-iraksak','Kalın kenarlı merceğin görüntü özellikleri')
fl=-1.6; dl=3.4; vl=1/(1/fl-1/dl); assert vl<0 and abs(vl)<dl and abs(vl/dl)<1
fo=[kalin_mercek(1.5),'\\draw[thin] (-4.5,0) -- (4.5,0);']
for x,n_ in ((-1.6,'F'),(1.6,'F$^\\prime$'),(-3.2,'2F'),(3.2,'2F$^\\prime$')): fo.append(f'\\fill ({x},0) circle (1.4pt); '+nd((x,.1),n_,'above'))
fo.append(f'\\draw[very thick,-{{Stealth[length=2mm,width=1.8mm]}}] (-3.9,0) -- (-3.9,.8); '+nd((-3.9,-.1),'cisim','below'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
dg_t='Sanal, düz ve cisimden küçük'
qt('0019',[A('Mercek türünü belirle','Kenarları ortasından kalın olan mercek ıraksak mercektir; ışınları dağıtır.','kalın kenarlı mercek = ıraksak'),
 A('Işınları izle','Eksene paralel gelen ışın odaktan açılıyormuş gibi dağılır; ışınlar gerçekte kesişmez.','yansıyan ışınların uzantıları kesişir → sanal'),
 A('Görüntüyü yaz','Uzantıların kesiştiği nokta mercek ile cisim arasında kalır; görüntü düz ve küçük görünür.','sanal, düz, cisimden küçük')],
 dogru=dg_t,yan=[('Gerçek, ters ve cisimden küçük','Cisim 2F’nin ötesinde olduğundan ince kenarlı mercek gibi gerçek ve ters küçük görüntü beklemiş.','bilgi'),
  ('Sanal, düz ve cisimden büyük','Büyüteç gibi sanal ve büyük görüntü beklemiş; kalın kenarlı mercek her zaman küçültür.','bilgi'),
  ('Gerçek, ters ve cisimden büyük','Cismin konumunu F ile 2F arasında sanıp ince kenarlı mercekteki durumu uygulamış.','bilgi'),
  ('Sanal, ters ve cisimden küçük','Sanal görüntünün ters olabileceğini düşünmüş; kalın kenarlı mercekte görüntü her zaman düzdür.','bilgi')],
 harf='B',tipId='fz-op2-iraksak',tip='Kalın kenarlı merceğin görüntü özellikleri',z='kolay',alt='Mercekler',kaz='Kalın kenarlı merceğin oluşturduğu görüntünün özelliklerini nitel olarak belirtir.',
 kart='K-FZOP2-19 (kalın kenarlı mercek) · sanal, düz, küçük',kalip='şekilli',
 metin='Bir miyop gözlüğünün camı, şekilde gösterildiği gibi kenarları ortasından daha kalın olan bir mercektir. Merceğin optik ekseni üzerinde, mercek önünde odak uzaklığının iki katından daha uzakta duran ok biçimli bir cisim vardır ve merceğin her iki yanındaki F, F′ odak noktaları ile 2F, 2F′ noktaları işaretlenmiştir. Cisim tek renkli ışıkla aydınlatılmakta, mercekten bakan bir gözlemci ve mercek arkasına tutulan bir perde ile görüntü incelenmektedir.\nBuna göre, cismin görüntüsü için aşağıdakilerden hangisi doğrudur?',
 istenen='Kalın kenarlı merceğin oluşturduğu görüntünün özellikleri.',
 ip=['Mercek ışınları toplar mı dağıtır mı? Işınlar gerçekte kesişiyor mu, yoksa yalnızca uzantıları mı kesişiyor?'],
 bilgi=[B('Kalın kenarlı mercek','kenarları kalın olan mercek ıraksak mercektir; paralel ışınları dağıtır. Cismin konumu ne olursa olsun görüntü mercek tarafında, sanal, düz ve cisimden küçük oluşur ve miyop gözlüklerinde kullanılır. Örnek: kalın kenarlı mercekten bakıldığında nesneler küçük görünür')],
 puf='Kalın kenarlı mercek her konumda tek tür görüntü verir: sanal, düz ve küçük.',sekil=SK)

# ---------- 20 · ince kenarlı mercek görüntü özellikleri · orta · öncüllü
kartla('K-FZOP2-20','İnce kenarlı merceğin farklı cisim konumlarında görüntü özellikleri','Cisim 2F’nin ötesindeyse görüntü F ile 2F arasında küçük ve ters, F ile 2F arasındaysa 2F’nin ötesinde büyük ve ters, F içindeyse sanal, düz ve büyüktür.','Görüntü konumunu cismin konumuyla karıştırmak; F içindeki cismin görüntüsünü gerçek sanmak.','orta',4,'fz-op2-mercek-konum','İnce kenarlı merceğin görüntü özellikleri (öncüllü)')
f2=1.5
def vm(d): 
    v=1/(1/f2-1/d); return v,-v/d
dK,dL,dM=4.3,2.2,.8
vK,mK=vm(dK); vL,mL=vm(dL); vM,mM=vm(dM)
assert 0<abs(mK)<1 and f2<vK<2*f2 and vL>2*f2 and mL<-1 and vM<0 and mM>1
fo=[ince_mercek(1.7),'\\draw[thin] (-5.0,0) -- (5.0,0);']
for x,n_ in ((-1.5,'F'),(1.5,'F$^\\prime$'),(-3.0,'2F'),(3.0,'2F$^\\prime$')): fo.append(f'\\fill ({x},0) circle (1.4pt); '+nd((x,.1),n_,'above'))
for d_,n_ in ((dK,'K'),(dL,'L'),(dM,'M')): fo.append(f'\\draw[thick,-{{Stealth[length=1.8mm,width=1.6mm]}}] ({-d_},0) -- ({-d_},.55); '+nd((-d_,-.1),n_,'below'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0020',[A('K konumunu incele','Cisim 2F’nin ötesinde; görüntü F′ ile 2F′ arasında, küçük, gerçek ve terstir. Görüntü cisimden büyük değildir.','K: görüntü küçük → I. yanlış'),
 A('L konumunu incele','Cisim F ile 2F arasında; görüntü 2F′ noktasının ötesinde, gerçek, ters ve büyüktür.','L: görüntü 2F′’nün ötesinde → II. doğru'),
 A('M konumunu incele','Cisim F ile mercek arasında; ışınlar kesişmez, görüntü sanal ve düzdür.','M: sanal, düz, büyük → III. doğru → II ve III')],
 truth=(False,True,True),harf='E',tipId='fz-op2-mercek-konum',tip='İnce kenarlı merceğin görüntü özellikleri (öncüllü)',z='orta',alt='Mercekler',kaz='İnce kenarlı merceğin önündeki cismin konumuna göre görüntünün yerini ve özelliklerini nitel olarak belirler.',
 kart='K-FZOP2-20 (ince kenarlı mercek, üç cisim konumu)',kalip='öncüllü',
 metin='Odak noktaları F ve F′ olan ince kenarlı bir merceğin optik ekseni boyunca, merceğin iki yanındaki F, 2F ve F′, 2F′ noktaları şekilde işaretlenmiştir. Bir öğrenci aynı küçük oku sırayla K, L ve M noktalarına koyuyor; her seferinde bir perdeyi hareket ettirerek görüntüyü yakalamaya, yakalayamazsa mercekten bakarak incelemeye çalışıyor. Ok her konumda optik eksene diktir.\nBuna göre,\nI. Ok K noktasındayken görüntü cisimden büyüktür.\nII. Ok L noktasındayken görüntü 2F′ noktasının ötesinde oluşur.\nIII. Ok M noktasındayken görüntü sanal ve düzdür.\nyargılarından hangileri doğrudur?',
 neden=[('2F’nin ötesindeki cismin görüntüsünün büyük olduğunu sanmış; bu konumda görüntü küçülür.','bilgi'),('F ile 2F arasındaki cismin görüntüsünün 2F′’nün ötesinde değil, F′ ile 2F′ arasında oluştuğunu sanmış.','bilgi'),('F içindeki cismin görüntüsünün de gerçek ve ters olduğunu düşünmüş; bu durumda ışınlar kesişmez ve görüntü sanaldır.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her konumun F ve 2F noktalarına göre nerede olduğunu belirle; özel ışınlarla görüntünün yerini kabaca çiz.'],
 bilgi=[B('İnce kenarlı mercek','cisim 2F’nin ötesindeyse görüntü F′ ile 2F′ arasında, gerçek, ters ve küçüktür; cisim F ile 2F arasındaysa görüntü 2F′’nün ötesinde, gerçek, ters ve büyüktür; cisim F içindeyse görüntü sanal, düz ve büyüktür (büyüteç).')],
 puf='Cisim merceğe yaklaştıkça gerçek görüntü uzaklaşır ve büyür; F içine girince görüntü sanal ve düz olur.',sekil=SK)

# ---------- 21 · göz kusuru · orta · tek cevap
kartla('K-FZOP2-21','Göz kusurunun ışın çiziminden belirlenmesi ve gözlük seçimi','Uzaktan gelen paralel ışınlar retinadan önce toplanıyorsa miyoplukturr ve ışınları dağıtan kalın kenarlı mercekli gözlükle düzeltilir; retinadan sonra toplanıyorsa hipermetroptur, ince kenarlı mercek gerekir.','Miyop gözün ince kenarlı mercekle düzeltildiğini sanmak; miyopluk ile hipermetropluğu karıştırmak.','orta',3,'fz-op2-goz-kusuru','Göz kusuru ve gözlük türü')
cx,cy_,rx,ry=2.2,0,2.3,1.5; xl=.35; xf=3.3
def elips_cik(p,d):
    t=0
    for i in range(1,2000):
        tt=i*.005; q_=(p[0]+d[0]*tt,p[1]+d[1]*tt)
        if ((q_[0]-cx)/rx)**2+(q_[1]/ry)**2>=1: return q_
    raise AssertionError
fo=[f'\\draw[thick] ({cx},0) ellipse ({rx} and {ry});',
    f'\\draw[line width=2.2pt,gray] ({cx+rx*cos(radians(-48)):.3f},{ry*sin(radians(-48)):.3f}) arc[start angle=-48,end angle=48,x radius={rx},y radius={ry}];',
    f'\\draw[thick,fill=white] ({xl},0) ellipse (.12 and .7);']
fo.append(nd((cx+rx+.05,.9),'retina','right')+f'\\draw[thin] ({cx+rx+.0:.3f},.9) -- ({cx+rx*cos(radians(30))+.02:.3f},{ry*sin(radians(30)):.3f});')
fo.append(nd((-1.0,1.35),'göz merceği','above')+f'\\draw[thin] (-.5,1.35) -- ({xl-.05},.68);')
for y0 in (.5,0,-.5):
    p0=(-1.8,y0); pl=(xl,y0); fo.append(ray(p0,pl,at=.5))
    d=nrm(sub((xf,0),pl)); pe=elips_cik(pl,d); fo.append(ray(pl,pe,at=.45))
    if y0!=0: assert pe[0]>xf
assert xf<cx+rx-.4
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
dg_t='Miyop; kalın kenarlı mercekli gözlük'
qt('0021',[A('Işınların toplandığı yeri bul','Paralel ışınlar retinadan önce, bir noktada kesişip sonra retinaya dağılarak ulaşıyor.','odak noktası retinanın önünde'),
 A('Kusuru belirle','Odak noktası retinanın önündeyse göz miyoplukturr; uzaktaki cisimler net görülmez.','miyop'),
 A('Düzeltmeyi seç','Işınların retinaya kadar toplanmaması için gözlük ışınları önceden dağıtmalıdır; bu iş kalın kenarlı mercekle yapılır.','miyop → kalın kenarlı (ıraksak) mercek')],
 dogru=dg_t,yan=[('Miyop; ince kenarlı mercekli gözlük','Kusuru doğru bulmuş ama ışınları toplayan ince kenarlı mercek miyoplukta odağı retinadan daha da öne çeker.','bilgi'),
  ('Hipermetrop; ince kenarlı mercekli gözlük','Odağın retinanın önünde olduğunu fark etmemiş; hipermetropta odak retinanın arkasındadır.','bilgi'),
  ('Hipermetrop; kalın kenarlı mercekli gözlük','Işınların retinadan önce toplanmasını hipermetropluk sanmış.','bilgi'),
  ('Gözde kusur yoktur; gözlük gerekmez','Işınların retinada değil retinadan önce toplandığını görmemiş; net görüntü retinada oluşmalıdır.','dikkat')],
 harf='D',tipId='fz-op2-goz-kusuru',tip='Göz kusuru ve gözlük türü',z='orta',alt='Mercekler',kaz='Işın çiziminden göz kusurunu belirler ve düzeltilmesi için gereken mercek türünü seçer.',
 kart='K-FZOP2-21 (göz kusuru) · odak retina önünde',kalip='şekilli',
 metin='Bir öğrencinin gözünün kesiti şekilde verilmiştir. Uzaktaki bir noktadan gelen, optik eksene paralel üç ışının göz merceğinden geçtikten sonra izlediği yollar çizilmiştir. Öğrenci göz doktoruna giderek gözündeki kusurun ne olduğunu ve bu kusuru gidermek için gözlük camının hangi tür mercek olması gerektiğini soruyor. Göz merceği ve gözlük camı birbirine çok yakın kabul edilecektir.\nBuna göre, doktorun yanıtı aşağıdakilerden hangisi olur?',
 istenen='Göz kusuru ve düzeltici gözlük camının türü.',
 ip=['Paralel ışınların nerede toplandığına bak; net görüntü retinada oluşmalıdır. Gözlük ışınları toplamalı mı dağıtmalı mı?'],
 bilgi=[B('Göz kusurları','miyopta uzaktaki cismin görüntüsü retinadan önce oluşur ve kalın kenarlı (ıraksak) mercekle düzeltilir; hipermetropta görüntü retinadan sonra oluşur ve ince kenarlı (yakınsak) mercekle düzeltilir. Örnek: yakını net gören, uzağı bulanık gören kişi miyoptur')],
 puf='Odak retinanın önündeyse miyop → kalın kenarlı mercek; retinanın arkasındaysa hipermetrop → ince kenarlı mercek.',sekil=SK)

# =============================== PRİZMA VE RENK ===============================
# ---------- 22 · prizmada ışığın renklere ayrılması · zor · öncüllü
kartla('K-FZOP2-22','Prizmada ışığın renklere ayrılması, kırılma indisi, hız ve frekans','Beyaz ışık prizmada renklere ayrılır; kırmızı en az, mor en çok kırılır; kırılma indisi mor için en büyük, ışık hızı mor için en küçük, frekans mor için en büyüktür.','Çok kırılan ışığın hızının daha büyük olduğunu sanmak; frekansın kırılma indisiyle ters ilişkili olduğunu düşünmek.','zor',4,'fz-op2-prizma','Prizmada renklere ayrılma (öncüllü)')
A60=radians(60); n_out_l=(-sin(A60),cos(A60)*0+.5)  # (-.866,.5)
n_out_l=(-sqrt(3)/2,.5); n_out_r=(sqrt(3)/2,.5)
B1,B2,Tp=(-1.6,0),(1.6,0),(0,1.6*sqrt(3))
phi=radians(20); din=(cos(phi),sin(phi))
yP=.7; P0=(-1.6+yP/sqrt(3),yP)
cn={'K':1.58,'L':1.65,'M':1.75}
cik={}
for k_,n_ in cn.items():
    d1=refract(din,n_out_l,1.0,n_)
    # sağ yüzeyle kesişim: x = 1.6 - y/sqrt(3)
    tt=None
    for i in range(1,4000):
        t=i*.001; q_=add(P0,mul(d1,t))
        if q_[0]>=1.6-q_[1]/sqrt(3): tt=t; break
    Q_=add(P0,mul(d1,tt)); assert Q_[1]<Tp[1]-.1
    d2=refract(d1,mul(n_out_r,-1),n_,1.0); assert d2 is not None
    cik[k_]=(Q_,d2)
dev={k:ang(v[1]) for k,v in cik.items()}
assert dev['K']>dev['L']>dev['M'] and dev['K']-dev['M']>6, dev
assert cn['K']<cn['L']<cn['M']
vel={k:1/n for k,n in cn.items()}; assert vel['L']>vel['M']        # III. yargı yanlış: L'nin hızı M'ninkinden büyük
fo=['\\draw[thick] '+' -- '.join(pt(p) for p in (B1,B2,Tp))+' -- cycle;']
S0=sub(P0,mul(din,2.0)); fo.append(ray(S0,P0,at=.55)); fo.append(nd((S0[0],S0[1]+.15),'beyaz ışık','above'))
for k_ in 'KLM':
    d1=refract(din,n_out_l,1.0,cn[k_]); Q_,d2=cik[k_]
    fo.append(f'\\draw[vurgu,thin] {pt(P0)} -- {pt(Q_)};')
    E=add(Q_,mul(d2,3.0)); fo.append(ray(Q_,E,at=.6)); fo.append(nd(add(E,(.08,0)),k_+(' (yeşil)' if k_=='L' else ''),'right'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0022',[A('Işınların sırasını belirle','Prizma beyaz ışığı tabanına doğru en çok sapan ışın mor tarafta, en az sapan kırmızı tarafta olacak biçimde ayırır. M en çok, K en az kırılmıştır.','K: kırmızıya yakın · L: yeşil · M: mora yakın'),
 A('Kırılma indislerini karşılaştır','Çok kırılan ışığın prizma maddesindeki kırılma indisi daha büyüktür.','n_K < n_L < n_M → I. doğru'),
 A('Frekansı yorumla','Mor tarafta frekans en büyüktür; frekans ortam değiştirmekle değişmez.','f_M > f_K → II. doğru'),
 A('Hızı karşılaştır','Kırılma indisi küçük olan ışığın hızı büyüktür; L’nin hızı M’ninkinden büyüktür.','v_L > v_M → III. yanlış → I ve II')],
 truth=(True,True,False),harf='B',tipId='fz-op2-prizma',tip='Prizmada renklere ayrılma (öncüllü)',z='zor',alt='Prizma ve Renk',kaz='Prizmada beyaz ışığın renklere ayrılmasını kırılma indisi, ışık hızı ve frekans bakımından yorumlar.',
 kart='K-FZOP2-22 (prizma, K–L–M ışınları)',kalip='öncüllü',
 metin='Cam bir prizmaya gönderilen beyaz ışık, şekilde gösterildiği gibi prizmadan çıkarken K, L ve M ışınlarına ayrılmıştır. L ışını yeşil renklidir ve ışınların yönleri ölçeksiz olarak çizilmiştir. Işınlar yalnızca prizmanın yüzeylerinde kırılmaktadır; K ışını prizmanın tabanından en uzak, M ışını tabanına en yakın doğrultuda ilerlemektedir.\nBuna göre,\nI. K ışığının prizma maddesindeki kırılma indisi, M ışığınınkinden küçüktür.\nII. M ışığının frekansı, K ışığının frekansından büyüktür.\nIII. Prizma içinde L ışığının hızı, M ışığının hızından küçüktür.\nyargılarından hangileri doğrudur?',
 neden=[('en çok kırılan ışığın kırılma indisinin en küçük olduğunu düşünmüş; çok kırılan ışığın indisi büyüktür.','bilgi'),('frekansın renge göre değişmediğini ya da K tarafında büyük olduğunu sanmış; mor tarafta frekans daha büyüktür.','bilgi'),('en çok kırılan ışığın prizmada daha hızlı olduğunu düşünmüş; kırılma indisi büyük olan ışık yavaş ilerler.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Hangi ışının tabana doğru en çok saptığını belirle; çok sapan ışığın kırılma indisini, hızını ve renk sırasındaki yerini ilişkilendir.'],
 bilgi=[B('Işığın renklere ayrılması','prizma ışığın rengine göre farklı kırılma indisi gösterdiği için beyaz ışığı renklere ayırır: kırmızı en az, mor en çok kırılır. Kırılma indisi büyük olan renkte ışık yavaş ilerler. Örnek: camda mor ışık kırmızı ışıktan yavaştır'),
        B('Frekans','bir ışığın frekansı kaynağı tarafından belirlenir, ortam değiştirmekle değişmez; mor ışığın frekansı kırmızıdan büyüktür')],
 puf='Çok kırılan = mora yakın = kırılma indisi büyük = prizmada yavaş = frekansı büyük.',sekil=SK)

# ---------- 23 · ışık filtreleri · orta · tek cevap
kartla('K-FZOP2-23','Ardışık ışık filtrelerinden geçen beyaz ışık','Her filtre yalnızca kendi renginin bileşenlerini (kırmızı, yeşil, mavi ana ışıklardan) geçirir; ardışık filtrelerde son görülen renk, filtrelerin ortak geçirdiği ana ışıktır.','Yalnız ilk ya da son filtreye bakmak; ortak ana ışık olmayınca siyah sanmak.','orta',3,'fz-op2-filtre','Ardışık filtreler ve perdede görülen renk')
RGB={'sarı':{'K','Y'},'macenta':{'K','M'}}
sar={'K','Y'}; mac={'K','M'}; son=sar&mac; assert son=={'K'}    # K: kırmızı, Y: yeşil, M: mavi
fo=[]
for yy in (-.5,0,.5): fo.append(ray((0,yy),(1.2,yy),at=.6))
fo.append(nd((-.05,0),'beyaz ışık','left'))
fo.append('\\draw[thick] (1.5,-.95) rectangle (1.75,.95); '+nd((1.62,1.1),'sarı filtre','above'))
fo.append('\\draw[thick] (3.3,-.95) rectangle (3.55,.95); '+nd((3.42,1.1),'macenta filtre','above'))
for yy in (-.5,0,.5):
    fo.append(ray((1.75,yy),(3.3,yy),at=.55)); fo.append(ray((3.55,yy),(5.1,yy),at=.55))
fo.append(seg((5.2,-1.1),(5.2,1.1),'ultra thick')); fo.append(f'\\fill[pattern=north east lines,pattern color=gray] (5.2,-1.1) rectangle (5.4,1.1);'); fo.append(nd((5.3,1.2),'beyaz perde','above'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qt('0023',[A('Ana renkleri yaz','Beyaz ışık kırmızı, yeşil ve mavi ışığın birleşimidir; sarı = kırmızı + yeşil, macenta = kırmızı + mavi.','beyaz = K + Y + M'),
 A('İlk filtreden geçeni bul','Sarı filtre kırmızı ve yeşili geçirir, maviyi soğurur.','K + Y geçer'),
 A('İkinci filtreden geçeni bul','Macenta filtre kırmızı ve maviyi geçirir; yeşili soğurur.','K + Y → yalnız K geçer'),
 A('Perdedeki rengi yaz','Beyaz perde gelen ışığı yansıtır; perdeye yalnızca kırmızı ışık ulaşmıştır.','perdede kırmızı görülür')],
 dogru='Kırmızı',yan=[('Beyaz','Filtrelerin beyaz ışığı değiştirmeden geçirdiğini sanmış; filtreler kendi renkleri dışındaki ışıkları soğurur.','bilgi'),
  ('Sarı','Yalnız ilk filtrenin etkisini hesaba katmış; ikinci filtrenin yeşil ışığı da soğurduğunu unutmuş.','dikkat'),
  ('Macenta','Yalnız son filtrenin rengine bakmış; ilk filtre maviyi zaten soğurmuştur.','dikkat'),
  ('Siyah','Sarı ve macenta filtrelerin ortak ışığı olmadığını düşünmüş; ikisi de kırmızı ışığı geçirir.','bilgi')],
 harf='E',tipId='fz-op2-filtre',tip='Ardışık filtreler ve perdede görülen renk',z='orta',alt='Prizma ve Renk',kaz='Ardışık ışık filtrelerinden geçen ışığın rengini ana ışık bileşenlerini izleyerek belirler.',
 kart='K-FZOP2-23 (sarı + macenta filtre, beyaz perde)',kalip='şekilli',
 metin='Bir sahne tasarımcısı, beyaz ışık veren bir projektörün önüne, şekildeki gibi önce sarı, sonra macenta renkli iki filtre yerleştiriyor. Filtreler idealdir: her biri yalnızca kendi rengini oluşturan ana ışık bileşenlerini geçirir, diğerlerini tamamen soğurur. Işık bu filtrelerden geçtikten sonra beyaz bir perdeye düşüyor. Beyaz perde üzerine gelen bütün renkleri yansıtır ve ortamda başka ışık kaynağı yoktur.\nBuna göre, perdede hangi renk görülür?',
 istenen='Perdede görülen rengin belirlenmesi.',
 ip=['Beyaz ışığı oluşturan üç ana ışığı düşün ve her filtreden hangilerinin geçip hangilerinin soğurulduğunu sırayla izle.'],
 bilgi=[B('Işık renkleri ve filtreler','beyaz ışık kırmızı, yeşil ve mavi ana ışıkların birleşimidir; sarı ışık kırmızı + yeşil, macenta ışık kırmızı + mavi, camgöbeği ışık yeşil + mavi içerir. Bir filtre kendi renginin bileşenlerini geçirir, diğerlerini soğurur. Örnek: camgöbeği filtre kırmızıyı soğurur, yeşil ve maviyi geçirir')],
 puf='Ardışık filtrelerde geçen renk, tüm filtrelerin ortak geçirdiği ana ışıktır.',sekil=SK)

# ---------- 24 · cisimlerin renkli ışıkta görünümü · zor · öncüllü
kartla('K-FZOP2-24','Renkli ışık altında cisimlerin görünen rengi','Bir cisim, rengini oluşturan ana ışıklardan yalnız gelen ışıkta bulunanları yansıtır; hiçbirini bulamazsa siyah görünür.','Cismin rengini ışığın rengiyle karıştırmak; sarı cismin macenta ışıkta sarı kaldığını sanmak.','zor',4,'fz-op2-cisim-renk','Renkli ışıkta cisimlerin görünümü (öncüllü)')
tabl=[('K','Kırmızı',{'K'}),('L','Yeşil',{'Y'}),('M','Sarı',{'K','Y'}),('N','Mavi',{'M'})]
isik={'K','M'}   # macenta
gor_={n_:(p&isik) for n_,_,p in tabl}
assert gor_['K']=={'K'} and gor_['M']=={'K'} and gor_['L']==set() and gor_['N']=={'M'}
T1=(gor_['K']==gor_['M']); T2=(gor_['L']=={'Y'}); T3=(gor_['N']=={'K','M'}); assert (T1,T2,T3)==(True,False,False)
fo=['\\draw[thick] (0,0) rectangle (5.8,-2.5);','\\draw[thick] (0,-.5) -- (5.8,-.5); \\draw[thin] (1.2,0) -- (1.2,-2.5);']
fo.append(nd((.6,-.25),'Cisim')); fo.append(nd((3.5,-.25),'Beyaz ışıkta görünen renk'))
for i,(n_,r_,_) in enumerate(tabl):
    y=-.5-.5*i-.25; fo.append(nd((.6,y),n_)); fo.append(nd((3.5,y),r_))
    if i<3: fo.append(f'\\draw[thin] (0,{-.5-.5*(i+1)}) -- (5.8,{-.5-.5*(i+1)});')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0024',[A('Işığın bileşenlerini yaz','Macenta ışık kırmızı ve mavi ışıktan oluşur; yeşil ışık içermez.','ışık = kırmızı + mavi'),
 A('Cisimleri tek tek incele','Her cisim kendi bileşenlerinden yalnız ışıkta bulunanları yansıtır: kırmızı cisim kırmızıyı, sarı cisim (kırmızı + yeşil) yalnız kırmızıyı, mavi cisim maviyi yansıtır; yeşil cisim hiçbirini yansıtmaz.','K: kırmızı · L: siyah · M: kırmızı · N: mavi'),
 A('Yargıları değerlendir','K ve M aynı renk (kırmızı) görünür; L siyah görünür, yeşil değil; N mavi görünür, macenta değil.','I. doğru · II. yanlış · III. yanlış → Yalnız I')],
 truth=(True,False,False),harf='A',tipId='fz-op2-cisim-renk',tip='Renkli ışıkta cisimlerin görünümü (öncüllü)',z='zor',alt='Prizma ve Renk',kaz='Renkli ışık altında cisimlerin rengini, cismin yansıttığı ve ışığın içerdiği ana ışıkları karşılaştırarak belirler.',
 kart='K-FZOP2-24 (macenta ışık, dört cisim) · tablo',kalip='öncüllü',
 metin='Bir tiyatro sahnesindeki dört dekor parçasının beyaz ışık altında görünen renkleri tabloda verilmiştir. Sahne, kırmızı ve mavi ışık veren iki projektörün aynı noktaya yönlendirilmesiyle oluşan macenta ışıkla aydınlatılmakta, başka ışık kaynağı bulunmamaktadır. Parçalar ideal pigmentlerle boyanmıştır: her parça yalnızca kendi rengini oluşturan ana ışıkları yansıtır, diğerlerini soğurur.\nBuna göre,\nI. K ve M parçaları aynı renkte görünür.\nII. L parçası yeşil görünür.\nIII. N parçası macenta görünür.\nyargılarından hangileri doğrudur?',
 neden=[('sarı parçanın macenta ışıkta sarı kalacağını düşünmüş; sarı parça yalnız kırmızı ışığı yansıtır ve kırmızı görünür.','bilgi'),('yeşil parçanın ışıkta yeşil bileşen olmadığını göz ardı etmiş; L parçası siyah görünür.','dikkat'),('mavi parçanın macenta ışığın rengini alacağını sanmış; N parçası yalnız maviyi yansıtır, mavi görünür.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Işıktaki ana renkleri ve her parçanın yansıtabildiği ana renkleri ayrı ayrı yaz; ortak olanlar görünen rengi verir.'],
 bilgi=[B('Cisimlerin rengi','bir cisim, rengini oluşturan ana ışıklardan yalnız üzerine gelen ışıkta bulunanları yansıtır. Beyaz ışıkta kırmızı görünen cisim kırmızıyı, sarı görünen cisim kırmızı ve yeşili yansıtır. Hiçbirini bulamazsa cisim siyah görünür. Örnek: mavi ışıkta kırmızı cisim siyah görünür')],
 puf='Görünen renk = cismin yansıttığı ana ışıklar ∩ ışığın içerdiği ana ışıklar; kesişim boşsa cisim siyah görünür.',sekil=SK)

# =============================== YAZ ===============================
assert len(P.ANA)==24
from collections import Counter
print('zorluk',Counter(x['zorluk'] for x in P.ANA),'harf',sorted(Counter(x['cevap']['sik'] for x in P.ANA).items()))
bitir(P,'optikiki','fiz|Optik')
