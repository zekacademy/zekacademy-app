"""TYT Fizik · Optik (üçüncü paket) · 10 soru, hafif mod (kardeş yok, ipucu 1). Şekiller TikZ; koordinatlar ve açılar Python'da hesaplanır
(yansımada eşit açı, kırılmada vektör Snell yasasıyla doğru yön). Her cevap ve öncül Python'da assert edilir."""
import sys,os,math,json,itertools,random
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,asin,acos,pi
from fractions import Fraction as Fr
P=Parti('optikuc','Optik','fiz|Optik',ders='TYT Fizik',idon='tytfiz')
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
def arka(p1,p2,gerisi,uz=.2,n=14):
    """aynanın arka yüzüne tarama çizgileri: gerisi = arkaya doğru birim vektör"""
    o=[seg(p1,p2,'very thick')]
    for i in range(n+1):
        t=i/n; p=(p1[0]+(p2[0]-p1[0])*t,p1[1]+(p2[1]-p1[1])*t)
        q_=add(p,mul(gerisi,uz)); q_=add(q_,mul(nrm(sub(p2,p1)),-uz*.8))
        o.append(f'\\draw[thin] {pt(p)} -- {pt(q_)};')
    return '\n'.join(o)
def sc(body,s): return f'\\begin{{scope}}[scale={s}]\n{body}\n\\end{{scope}}'
def dot_(p,txt,anc='above right',r=.09): return f'\\fill {pt(p)} circle ({r}); '+nd(p,txt,anc)
# =============================== 01 · düzlem aynada görülebilen noktalar (öncüllü) ===============================
kartla('K-FZOP3-01','Düzlem aynada gözün görebildiği cisimler','Cismin aynadaki görüntüsü, aynaya göre simetrik noktada çizilir; göz ile bu görüntüyü birleştiren doğru aynanın kenarları arasından geçiyorsa cisim görülür.','Cismin kendisinden aynaya çizilen doğruya bakmak; görüntü–göz doğrusunun ayna dışında kalmasını fark etmemek.','orta',5,'fz-op3-gorus-noktalar','Düzlem aynada görülebilen cisimler')
AY=(-2,2); E1=(1,-2); K1=(-4,-1); L1=(2,-1); M1=(-3+1,-3)
def cap(E,O):
    ex,ey=E; ox,oy=O; t=Fr(-ey,-oy-ey); return ex+t*(ox-ex)          # göz–görüntü doğrusunun aynayı kestiği x
xK,xL,xM=cap(E1,K1),cap(E1,L1),cap(E1,M1)
assert (xK,xL,xM)==(Fr(-7,3),Fr(5,3),Fr(-1,5))
vK,vL,vM=[AY[0]<x<AY[1] for x in (xK,xL,xM)]; assert (vK,vL,vM)==(False,True,True)
assert min(abs(xK-AY[0]),abs(xL-AY[1]),abs(xM-AY[0]),abs(xM-AY[1]))>=Fr(1,5)
fo=['\\draw[gray!45,very thin] (-5,-3.5) grid (4,0);']
fo.append(arka((AY[0],0),(AY[1],0),(0,1),.28,12))
fo.append(nd((0,.55),'ayna','above'))
fo.append(f'\\draw[thick,fill=white] {pt(E1)} circle (.14); '+nd((E1[0]+.2,E1[1]-.15),'göz','below right'))
for p,t in ((K1,'$K$'),(L1,'$L$'),(M1,'$M$')): fo.append(dot_(p,t,'above left' if t=='$K$' else 'above right'))
SK=tikz_svg(HEAD+sc('\n'.join(fo),.62)+TAIL)
qo('0001',[A('Görme koşulunu yaz','Aynadaki görüntü, cisme göre aynanın öbür yanında simetrik noktada oluşur. Göz ile görüntüyü birleştiren doğru aynanın uçları arasında kalıyorsa cisim görülür.','göz–görüntü doğrusu ∈ ayna'),
  A('K noktasını incele','K’nin görüntüsü aynanın arkasında, K ile aynaya göre simetrik noktadadır. Gözden bu görüntüye çizilen doğru aynanın sol ucunun yaklaşık 1/3 birim dışından geçer.','K: ayna dışında → görülmez → I. yanlış'),
  A('L noktasını incele','L’nin görüntüsü ile göz arasındaki doğru aynanın sağ ucunun yaklaşık 1/3 birim içinden geçer.','L: ayna üzerinde → görülür → II. doğru'),
  A('M noktasını incele','M’nin görüntüsü ile göz arasındaki doğru aynanın ortasına yakın bir noktadan geçer.','M: ayna üzerinde → görülür → III. doğru'),
  A('Sonucu belirle','Doğru olan yargıları birleştir.','II ve III')],
 truth=(vK,vL,vM),harf='D',tipId='fz-op3-gorus-noktalar',tip='Düzlem aynada görülebilen cisimler',z='orta',alt='Düzlem Ayna',kaz='Düzlem aynada cismin görüntüsünü çizerek gözün hangi noktalardaki cisimleri görebildiğini belirler.',
 kart='K-FZOP3-01 (gözün görebildiği cisimler) · kareli zeminde üç nokta',kalip='şekilli',
 metin='Bir odanın yukarıdan görünümü şekilde verilmiştir; kareler birer birim kenarlıdır. Boyutları ihmal edilecek kadar küçük bir göz, düzlem ayna ve K, L, M noktalarındaki küçük cisimler şekildeki konumlarda durmaktadır. Göz yerinden hiç kıpırdamamaktadır.\nBuna göre,\nI. K noktasındaki cisim, göz tarafından aynada görülebilir.\nII. L noktasındaki cisim, göz tarafından aynada görülebilir.\nIII. M noktasındaki cisim, göz tarafından aynada görülebilir.\nyargılarından hangileri doğrudur?',
 neden=[('K’nin görüntüsü ile göz arasındaki doğrunun ayna dışında kaldığını fark etmemiş; cismin aynaya yakın olmasını yeterli saymış.','dikkat'),
        ('L’nin ayna uzantısının dışında kaldığını düşünmüş; oysa göz–görüntü doğrusu aynanın içinden geçer.','dikkat'),
        ('M’nin gözden uzak ve aynaya göre yan konumda olduğunu görüp görülemeyeceğini düşünmüş; görüntü–göz doğrusu aynadan geçer.','dikkat')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her cismin aynadaki görüntüsünü aynanın arkasında simetrik olarak işaretle; sonra göz ile görüntü arasına doğru çiz.'],
 bilgi=[B('Düzlem aynada görüntü','görüntü, cismin aynaya göre simetriğindedir. Gözün bir cismi görebilmesi için göz ile görüntüsünü birleştiren doğrunun aynayı kesmesi gerekir. Örnek: ayna önündeki cismin görüntüsü, aynanın arkasında cisim kadar uzakta oluşur')],
 puf='Düzlem aynada cismi görmek için cismin görüntüsünü çiz; göz–görüntü doğrusu aynadan geçiyorsa cisim görülür.',sekil=SK)

# =============================== 02 · 45° eğimli aynada yansıyan ışın (nokta) ===============================
kartla('K-FZOP3-02','Eğimli düzlem aynada yansıyan ışının yolu','Yansıma yasasına göre gelen ve yansıyan ışın normalle eşit açı yapar; 45° eğimli aynada ışının yatay ve düşey adımları yer değiştirir ve yansıyan ışının geçtiği nokta kareli zeminde okunur.','Aynanın yatay ya da düşey olduğunu varsaymak; ışını normal boyunca yansıtmak; ışının doğrultusunu değiştirmeden sürdürmek.','orta',4,'fz-op3-yansiyan-isin','Eğimli aynada yansıyan ışının yolu')
Sx=(0,4); Px=(3,0); d_in=(3,-4); u=nrm((1,1)); nn_=(-u[1],u[0])
dR=reflect(d_in,nn_); assert abs(dR[0]+4)<1e-9 and abs(dR[1]-3)<1e-9
assert dot(d_in,nn_)<0 and abs(dot(d_in,nn_))/5 > 0 and abs(abs(dot(d_in,nn_))-abs(dot(dR,nn_)))<1e-9         # gelme açısı = yansıma açısı
pts={'K':(0,3),'L':(-1,3),'M':(6,4),'N':(6,-4),'P':(0,-4)}
on=lambda p: abs((p[0]-Px[0])*dR[1]-(p[1]-Px[1])*dR[0])<1e-9 and (p[0]-Px[0])*dR[0]+(p[1]-Px[1])*dR[1]>0
assert [k for k,p in pts.items() if on(p)]==['L']
hm=lambda dv: (Px[0]+dv[0],Px[1]+dv[1])
assert hm((-3,3))==pts['K'] and hm((3,4))==pts['M'] and hm(d_in)==pts['N'] and hm((-3,-4))==pts['P']
fo=['\\draw[gray!45,very thin] (-2,-4.5) grid (7,5);']
fo.append('\\draw[very thick] (2,-1) -- (4,1);')
for i in range(7):
    t=i/6; p=(2+2*t,-1+2*t); fo.append(f'\\draw[thin] {pt(p)} -- {pt((p[0]+.3,p[1]-.3))};')
fo.append(ray(Sx,Px,at=.5)); fo.append(f'\\fill {pt(Sx)} circle (.09); '+nd(Sx,'lazer','above left'))
for k,p in pts.items(): fo.append(dot_(p,f'${k}$','below left' if k=='K' else ('above left' if k=='L' else 'above right')))
SK=tikz_svg(HEAD+sc('\n'.join(x for x in fo if x),.5)+TAIL)
q('0002',[A('Normali ve açıları belirle','Ayna 45° eğimlidir; gelen ışın aynaya 3 kare sağa ve 4 kare aşağı doğru gelir. Yansıma yasasına göre ışın, normale göre simetrik yönde gider.','gelen: 3 sağ, 4 aşağı'),
  A('Yansıyan yönü bul','45° eğimli bir aynada ışının yatay ve düşey adımları yer değiştirir; sağa giden sola, aşağı giden yukarı döner.','yansıyan: 4 sol, 3 yukarı'),
  A('Noktayı işaretle','Işının aynaya çarptığı noktadan 4 kare sola, 3 kare yukarı gidilir.','(3, 0) → (−1, 3): L noktası'),
  A('Diğer noktaları ele','Diğer noktalar farklı yönlerde kalır; yatay ya da düşey ayna, ışığın doğrultusunu sürdürmesi ya da normal boyunca gitmesi gibi hatalı yolları gösterir.','yalnız L doğru')],
 dogru='L',yan=[('K','Işığı aynanın normali doğrultusunda (1 sol, 1 yukarı) göndermiş; yansıma yasasında yansıyan ışın gelen ışınla normale göre simetriktir.','bilgi'),
  ('M','Aynayı yatay sanmış: ışının yalnız düşey adımını ters çevirmiş (3 sağ, 4 yukarı).','bilgi'),
  ('N','Işığın aynaya çarptıktan sonra doğrultusunu değiştirmeden (3 sağ, 4 aşağı) devam ettiğini sanmış.','bilgi'),
  ('P','Aynayı düşey sanmış: ışının yalnız yatay adımını ters çevirmiş (3 sol, 4 aşağı).','bilgi')],
 sira=['K','L','M','N','P'],
 tipId='fz-op3-yansiyan-isin',tip='Eğimli aynada yansıyan ışının yolu',z='orta',alt='Düzlem Ayna',kaz='45° eğimli düzlem aynaya gelen ışının yansıma yönünü yansıma yasasıyla bulur ve geçeceği noktayı belirler.',
 kart='K-FZOP3-02 (eğimli ayna, yansıyan ışın) · 45° ayna, kareli zemin',kalip='şekilli',
 metin='Kareli zemin üzerinde, şekildeki konumda duran 45° eğimli düzlem aynaya, lazer işaretleyiciden çıkan ince bir ışık demeti gönderiliyor. Şekilde ışının gelen kısmı gösterilmiştir; K, L, M, N ve P noktaları kare köşelerindedir.\nBuna göre, aynadan yansıyan ışın aşağıdaki noktalardan hangisinden geçer?',
 istenen='Yansıyan ışının geçtiği nokta.',
 ip=['Gelen ışının ayna yüzeyine göre yaptığı açıyı belirle; yansıyan ışın da ayna yüzeyiyle aynı açıyı yapar.'],
 bilgi=[B('Yansıma yasası','gelen ışın, yansıyan ışın ve normal aynı düzlemdedir; gelme açısı yansıma açısına eşittir. Örnek: yatay aynaya yatayla 30° yaparak gelen ışın, yatayla yine 30° yaparak yansır')],
 puf='Yansıyan ışını çizerken normali çiz; gelme ve yansıma açıları normale göre eşit ve ters yönlüdür.',sekil=SK)

# =============================== 03 · geniş kaynak: tam gölge ve yarı gölge noktaları ===============================
kartla('K-FZOP3-03','Geniş ışık kaynağında perdedeki gölge bölgeleri','Geniş kaynağın uç noktalarından engelin zıt kenarlarına çizilen ışınlar tam gölge ve yarı gölge sınırlarını verir; benzer üçgenlerle sınırların perdedeki yeri bulunur.','Yarı gölgeyi tam gölge sanmak; gölgeli bölgenin tamamını yarı gölge saymak; sınırları engel boyuyla karıştırmak.','zor',5,'fz-op3-genis-golge','Geniş kaynakta tam gölge ve yarı gölge')
hs,hb=1,Fr(3,2); ds,db=3,3            # kaynak yarı boyu, engel yarı boyu, kaynak–engel, engel–perde
def bolge(y):
    ys=Fr(y); kor=0; tum=0
    for s in (Fr(-1),Fr(-1,2),Fr(0),Fr(1,2),Fr(1)):                    # kaynak noktaları
        tum+=1; x3=(s+ys)/2                                            # engel düzleminde geçiş
        kor+= abs(x3)<hb
    return 'tam' if kor==tum else ('aydınlık' if kor==0 else 'yarı')
pts3={'K':Fr(-7,2),'L':Fr(-1),'M':Fr(3,2),'N':Fr(3),'P':Fr(5)}
bl={k:bolge(v) for k,v in pts3.items()}; assert bl=={'K':'yarı','L':'tam','M':'tam','N':'yarı','P':'aydınlık'}
assert hb+(hb-hs)*Fr(db,ds)==2 and hb+(hb+hs)*Fr(db,ds)==4
fo=[]
fo.append('\\draw[very thick] (0,-1) -- (0,1); '+nd((0,1),'kaynak','above'))
fo.append('\\draw[very thick] (3,-1.5) -- (3,1.5); '+nd((3,1.5),'engel','above'))
fo.append('\\draw[very thick] (6,-5.6) -- (6,5.6); '+nd((6,5.6),'perde','above'))
for k in range(-5,6): fo.append(f'\\draw[thin] (6,{k}) -- (6.18,{k}); \\node[font=\\scriptsize,anchor=west,inner sep=1pt] at (6.2,{k}) {{${k}$}};')
for k,v in pts3.items(): fo.append(f'\\fill ({6},{float(v):.2f}) circle (.1); '+nd((5.82,float(v)),f'${k}$','left'))
fo.append(dim((-.6,-1),(-.6,1),'$2$','left'))
fo.append(dim((0,-6.4),(3,-6.4),'$3$','below')); fo.append(dim((3,-6.4),(6,-6.4),'$3$','below'))
fo.append(dim((3.55,-1.5),(3.55,1.5),'$3$','right'))
SK=tikz_svg(HEAD+sc('\n'.join(fo),.5)+TAIL)
qt('0003',[A('Sınırları hesapla','Kaynağın uç noktalarından engelin zıt kenarlarına doğrular çiz; benzer üçgenlerle perdedeki sınırları bul. Kaynağın üst ucu ile engelin alt kenarından geçen ışın perdeye 4 birim aşağıda ulaşır.','yarı gölgenin dış sınırı: ±4'),
   A('Tam gölgeyi bul','Kaynağın alt ucu ile engelin alt kenarından geçen ışın 2 birim aşağıda ulaşır; yukarıda da simetriği vardır. Bu iki sınır arasında kaynağın hiçbir noktası görülmez.','tam gölge: −2 ile 2 arası'),
   A('Yarı gölgeyi bul','Tam gölgenin dışında, ±4’ün içinde kalan bölgelerde kaynağın yalnızca bir kısmı görülür.','yarı gölge: 2 ile 4 arası (iki yanda)'),
   A('Noktaları sınıfla','K = −3,5 ve N = 3 yarı gölgede; L = −1 ve M = 1,5 tam gölgede; P = 5 aydınlıkta.','Yarı gölge: K ve N')],
 'K ve N',[('L ve M','Tam gölgedeki noktaları yarı gölge sanmış; yarı gölgede kaynağın bir kısmı görülür, tam gölgede hiçbir kısmı görülmez.','bilgi'),
  ('Yalnız P','Işığı en çok alan noktayı yarı gölge saymış; P kaynağın tamamını görür, aydınlıktadır.','bilgi'),
  ('K, L, M ve N','Gölgeli bölgenin tamamını yarı gölge saymış; tam gölge ile yarı gölgeyi ayırmamış.','bilgi'),
  ('K, N ve P','Yarı gölge dışındaki noktalardan yalnız tam gölgeyi ayırmış; aydınlık noktayı da yarı gölgeye katmış.','dikkat')],harf='E',
 tipId='fz-op3-genis-golge',tip='Geniş kaynakta tam gölge ve yarı gölge',z='zor',alt='Gölge',kaz='Geniş ışık kaynağının engel arkasında oluşturduğu tam gölge ve yarı gölge bölgelerini benzer üçgenlerle belirler.',
 kart='K-FZOP3-03 (geniş kaynak, perde noktaları) · kaynak 2, engel 3, aralıklar 3 + 3',kalip='şekilli',
 metin='Şekilde, uzunluğu 2 birim olan çubuk biçimli geniş bir ışık kaynağı, uzunluğu 3 birim olan ışık geçirmeyen bir engel ve bir perde verilmiştir; kaynak, engel ve perde birbirine paraleldir ve ortaları aynı doğru üzerindedir. Perde üzerindeki sayılar, perdenin ortasından olan uzaklığı birim cinsinden göstermektedir. K, L, M, N ve P noktaları perde üzerindedir.\nBuna göre, perde üzerindeki hangi noktalar yarı gölgededir?',
 istenen='Yarı gölgede kalan noktalar.',
 ip=['Kaynağın uçlarından engelin kenarlarına çizilen ışınların perdeye ulaştığı noktaları benzer üçgenlerle bul.'],
 bilgi=[B('Tam ve yarı gölge','geniş kaynağın hiçbir noktasından ışık almayan bölge tam gölge, yalnız bazı noktalarından ışık alan bölge yarı gölgedir. Örnek: kaynağın yarısı görülebilen noktada yarı gölge vardır')],
 puf='Geniş kaynakta sınırlar için kaynağın uçlarından engelin zıt kenarlarına ışın çiz; iki sınır arası tam gölge, dışı yarı gölgedir.',sekil=SK)

# =============================== 04 · ışık spotları örtüşmesi (renk) ===============================
kartla('K-FZOP3-04','Üst üste binen renkli ışık spotlarının renkleri','Beyaz perdede kırmızı + yeşil = sarı, yeşil + mavi = camgöbeği, kırmızı + mavi = macenta, üç ana ışık birlikte = beyaz görünür.','Işıkları boya gibi karıştırıp koyulaşacağını düşünmek; yeşil ile mavinin birleşimini macenta sanmak.','kolay',3,'fz-op3-spot-renk','Işık spotlarının örtüşmesinde renkler')
rr=1.35; Cr=(-.75,.45); Cg=(.75,.45); Cb=(0,-.85)
def ic(p,c): return (p[0]-c[0])**2+(p[1]-c[1])**2<rr*rr
reg={'K':(0,1.05),'L':(.9,-.35),'M':(-.9,-.35),'N':(0,.1)}
rg={k:(ic(p,Cr),ic(p,Cg),ic(p,Cb)) for k,p in reg.items()}
assert rg=={'K':(True,True,False),'L':(False,True,True),'M':(True,False,True),'N':(True,True,True)}
fo=[]
for c in (Cr,Cg,Cb): fo.append(f'\\draw[thick] {pt(c)} circle ({rr});')
fo+= [nd((-1.35,1.0),'kırmızı\\\\ışık','',',align=center'),nd((1.35,1.0),'yeşil\\\\ışık','',',align=center'),nd((0,-1.6),'mavi ışık')]
for k,p in reg.items(): fo.append(f'\\node[font=\\small\\bfseries] at {pt(p)} {{${k}$}};')
SK=tikz_svg(HEAD+sc('\n'.join(fo),1.15)+TAIL)
qo('0004',[A('Bölgelerdeki ışıkları belirle','Her bölgede hangi ana ışıkların üst üste bindiğine bak: K’de kırmızı ve yeşil, L’de yeşil ve mavi, M’de kırmızı ve mavi, N’de üçü birden vardır.','K: kırmızı + yeşil; L: yeşil + mavi; M: kırmızı + mavi; N: üçü birden'),
  A('K bölgesini incele','Kırmızı ve yeşil ışık birleşince sarı ışık görülür; beyaz perde bu ışığı olduğu gibi yansıtır.','K: sarı → I. doğru'),
  A('L bölgesini incele','Yeşil ve mavi ışığın birleşimi camgöbeğidir; macenta, kırmızı ile mavinin birleşimidir.','L: camgöbeği → II. yanlış'),
  A('N bölgesini incele','Üç ana ışık birlikte beyaz ışık verir; ışıklar karışınca boya gibi koyulaşmaz, aydınlanma artar.','N: beyaz → III. yanlış'),
  A('Sonucu belirle','Doğru olan yargıları birleştir.','Yalnız I')],
 truth=(True,False,False),harf='A',tipId='fz-op3-spot-renk',tip='Işık spotlarının örtüşmesinde renkler',z='kolay',alt='Işık ve Renk',kaz='Üst üste binen ana renkli ışıkların beyaz perdede oluşturduğu renkleri belirler.',
 kart='K-FZOP3-04 (kırmızı–yeşil–mavi spotlar) · ışık toplaması',kalip='şekilli',
 metin='Karanlık bir odada, beyaz bir perdeye kırmızı, yeşil ve mavi ışık veren üç projektör şekildeki gibi yönlendirilmiştir. Her projektör, perdede kendi renginde bir daire oluşturmakta; dairelerin üst üste bindiği bölgeler K, L, M ve N ile gösterilmektedir. Perde, üzerine düşen bütün renkleri yansıtır ve ortamda başka ışık kaynağı yoktur.\nBuna göre,\nI. K bölgesi sarı görünür.\nII. L bölgesi macenta görünür.\nIII. N bölgesi siyah görünür.\nyargılarından hangileri doğrudur?',
 neden=[('kırmızı ile yeşil ışığın birleşiminin sarı olduğunu bilmemiş.','bilgi'),
        ('yeşil ile mavi ışığın birleşimini macenta sanmış; macenta kırmızı ile mavinin birleşimidir.','bilgi'),
        ('ışıkların da boya gibi karışınca koyulaşıp siyah vereceğini düşünmüş.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her bölgede hangi renkli ışıkların üst üste bindiğini yaz; ışıklar toplanır, boyalar gibi soğurulmaz.'],
 bilgi=[B('Işık renklerinin toplanması','kırmızı, yeşil ve mavi ana ışıklardır; ışıklar üst üste bindiğinde renkler toplanır, beyaz perde gelen ışığı olduğu gibi yansıtır')],
 puf='Işık renkleri toplanır: iki ana ışık ikincil rengi, üçü birden beyazı verir.',sekil=SK)

# =============================== 05 · boya karışımı (öncüllü, metin) ===============================
kartla('K-FZOP3-05','Boyaların karışımında yansıtılan renk','Boyalar kendi renklerini oluşturan ana ışıkları yansıtıp diğerlerini soğurur; karışımda yalnız ortak yansıtılan ışık görülür.','Boyaları ışık gibi toplamak; karışımın daha açık renk vereceğini sanmak.','kolay',4,'fz-op3-boya-karisim','Boya karışımı ve görünen renk',kalip='öncüllü')
yans={'sarı':{'K','Y'},'camgöbeği':{'Y','M'},'macenta':{'K','M'}}
def karis(*b):
    r=set('KYM')
    for x in b: r&=yans[x]
    return r
assert karis('sarı','camgöbeği')=={'Y'} and karis('macenta','camgöbeği')=={'M'} and karis('sarı','macenta')=={'K'} and karis('sarı','camgöbeği','macenta')==set()
qo('0005',[A('Boyaların yansıttıklarını yaz','Sarı kırmızı ve yeşili, camgöbeği yeşil ve maviyi, macenta kırmızı ve maviyi yansıtır.','sarı: kırmızı + yeşil; camgöbeği: yeşil + mavi; macenta: kırmızı + mavi'),
  A('I. karışımı incele','Karışımda yalnız her iki boyanın da yansıttığı ışık görülür: sarı ve camgöbeği boyanın ortağı yeşildir.','sarı ∩ camgöbeği = yeşil → I. doğru'),
  A('II. karışımı incele','Macenta ve camgöbeği boyanın ortak yansıttığı ışık mavidir.','macenta ∩ camgöbeği = mavi → II. doğru'),
  A('III. karışımı incele','Sarı ve macenta boyanın ortak yansıttığı ışık kırmızıdır, mavi değil.','sarı ∩ macenta = kırmızı → III. yanlış'),
  A('Sonucu belirle','Doğru olan yargıları birleştir.','I ve II')],
 truth=(True,True,False),harf='C',tipId='fz-op3-boya-karisim',tip='Boya karışımı ve görünen renk',z='kolay',alt='Işık ve Renk',kaz='İdeal boyaların karışımında ortak yansıtılan ana ışığa bakarak görünen rengi belirler.',
 kart='K-FZOP3-05 (boya karışımı) · sarı–camgöbeği–macenta',kalip='öncüllü',
 metin='Bir ressam, ideal pigmentli boyalar kullanıyor: her boya yalnızca kendi rengini oluşturan ana ışıkları yansıtır, diğerlerini tamamen soğurur. Ressam boyaları karıştırıp karışımları beyaz ışık altında inceliyor.\nBuna göre,\nI. Sarı ve camgöbeği boyaların karışımı yeşil görünür.\nII. Macenta ve camgöbeği boyaların karışımı mavi görünür.\nIII. Sarı ve macenta boyaların karışımı mavi görünür.\nyargılarından hangileri doğrudur?',
 neden=[('sarı ile camgöbeği boyanın ortak yansıttığı ışığın yeşil olduğunu görmemiş.','bilgi'),
        ('macenta ile camgöbeği boyanın ortak yansıttığı ışığın mavi olduğunu görmemiş.','bilgi'),
        ('sarı ile macenta boyanın ortak yansıttığı ışığın kırmızı olduğunu bilmeyip mavi sanmış.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her boyanın yansıttığı iki ana ışığı yaz; karışımda yalnız ortak olanı kalır.'],
 bilgi=[B('Cisim rengi','bir cisim, kendi renginin ana ışık bileşenlerini yansıtır, diğerlerini soğurur. Örnek: sarı cisim beyaz ışıkta kırmızı ve yeşil bileşenleri yansıtır')],
 puf='Boyalar karışınca ışık soğurulur: yalnız iki boyanın da yansıttığı ortak ana ışık kalır.',sekil=None)

# =============================== 06 · normalden uzaklaşarak kırılma (öncüllü) ===============================
kartla('K-FZOP3-06','Kırılmada hız, dalga boyu ve frekans','Işık ortam değiştirirken frekansı sabit kalır; hızı ve dalga boyu ortama göre değişir. Normalden uzaklaşma, ışığın daha seyrek ortama geçtiğini ve hızının arttığını gösterir.','Frekansın da değiştiğini sanmak; hız arttığında dalga boyunun küçüldüğünü düşünmek.','orta',5,'fz-op3-kirilma-nitel','Kırılmada hız, dalga boyu ve frekans')
n1,n2=Fr(3,2),Fr(1); th1=radians(30); L0=2.4
d=(sin(th1),-cos(th1)); nrmv=(0,1); d2=refract(d,nrmv,float(n1),float(n2)); th2=degrees(atan2(abs(d2[0]),abs(d2[1])))
assert th2>45 and abs(th2-degrees(asin(1.5*sin(th1))))<1e-6          # normalden uzaklaşır
vy_x=Fr(1)/n2 > Fr(1)/n1; assert vy_x                                 # v ∝ 1/n : Y'de hız büyük
lam_ratio=(Fr(1)/n2)/(Fr(1)/n1); assert lam_ratio==Fr(3,2) and lam_ratio>1   # λ = v/f, f sabit
fo=['\\draw[thick] (-3,0) -- (3,0);','\\draw[dashed,thin] (0,-2.6) -- (0,2.6);']
fo.append(nd((-2.9,1.6),'X ortamı','right')); fo.append(nd((-2.9,-1.6),'Y ortamı','right'))
a0=(-L0*sin(th1),L0*cos(th1)); a1=(L0*d2[0],L0*d2[1])
fo.append(ray(a0,(0,0),at=.55)); fo.append(ray((0,0),a1,at=.6))
fo.append(nd((0.1,2.4),'normal','right'))
SK=tikz_svg(HEAD+sc('\n'.join(fo),.9)+TAIL)
qo('0006',[A('Kırılma yönünü yorumla','Işın, X’ten Y’ye geçerken normalden uzaklaşıyor. Normalden uzaklaşma, ışığın daha seyrek ortama (kırılma indisi küçük) geçtiğini gösterir.','X → Y: n_Y < n_X'),
  A('I. yargıyı incele','Işığın hızı ortamın kırılma indisiyle ters orantılıdır (v = c/n); Y’de n küçük olduğundan hız büyüktür.','v_Y > v_X → I. doğru'),
  A('II. yargıyı incele','Frekans sabit kaldığından λ = v/f ile dalga boyu hızla aynı yönde değişir; hız arttığı için dalga boyu büyür.','λ_Y > λ_X → II. yanlış'),
  A('III. yargıyı incele','Ortam değişirken ışığın frekansı kaynağa bağlıdır, ortama değil.','f_X = f_Y → III. doğru'),
  A('Sonucu belirle','Doğru olan yargıları birleştir.','I ve III')],
 truth=(True,False,True),harf='D',tipId='fz-op3-kirilma-nitel',tip='Kırılmada hız, dalga boyu ve frekans',z='orta',alt='Işığın Kırılması',kaz='Işığın normalden uzaklaşarak kırılmasından ortamları karşılaştırır; hız, dalga boyu ve frekansın değişimini yorumlar.',
 kart='K-FZOP3-06 (kırılma, normalden uzaklaşma) · hız–λ–f',kalip='şekilli',
 metin='Tek renkli bir ışık ışını, birbirinden farklı şeffaf X ve Y ortamlarını ayıran düzlem yüzeye şekildeki gibi gelip kırılarak Y ortamına geçiyor.\nBuna göre,\nI. Işığın Y ortamındaki hızı, X ortamındakinden büyüktür.\nII. Işığın Y ortamındaki dalga boyu, X ortamındakinden küçüktür.\nIII. Işığın frekansı iki ortamda da aynıdır.\nyargılarından hangileri doğrudur?',
 neden=[('normalden uzaklaşan ışının hızının arttığını (seyrek ortama geçtiğini) görmemiş.','bilgi'),
        ('hız arttığında dalga boyunun da küçüleceğini sanmış; λ = v/f ve f sabit olduğundan hız artınca λ artar.','bilgi'),
        ('ortam değişince ışığın frekansının da değiştiğini düşünmüş.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Işın normalden uzaklaştığına göre hangi ortamın daha seyrek olduğunu belirle; sonra hız, dalga boyu ve frekansı v = λ·f ilişkisiyle karşılaştır.'],
 bilgi=[B('Kırılma ve hız','ışık yoğun ortamda daha yavaştır; ışığın hızı, dalga boyu ve frekansı v = λ·f ilişkisiyle bağlıdır')],
 puf='Işık ortam değiştirirken frekansı sabit kalır; hız ve dalga boyu aynı yönde değişir, normalden uzaklaşma hızın arttığını gösterir.',sekil=SK)

# =============================== 07 · dik prizmada tam yansıma ===============================
kartla('K-FZOP3-07','Dik ikizkenar prizmada tam yansıma','Işık prizmaya yüzeye dik girerse sapmaz; hipotenüse 45° ile çarpar. Cam için sınır açısı 45°’den küçük olduğundan ışın tam yansır ve dik açıyla yön değiştirir.','Işığın hipotenüsten kırılarak çıktığını sanmak; 45°’yi sınır açısıyla karşılaştırmamak; doğrultunun değişmediğini düşünmek.','orta',5,'fz-op3-prizma-tir','Dik prizmada tam yansıma')
dI=(0,1); nH=nrm((1,1)); ci=abs(dot(dI,nH)); inc=degrees(acos(ci)); assert abs(inc-45)<1e-9 and inc>42        # 45° > sınır açısı 42°
assert 1/1.5 < sin(radians(45)) and degrees(asin(1/1.5))<45
dY=reflect(dI,nH); assert abs(dY[0]+1)<1e-9 and abs(dY[1])<1e-9       # sola, yatay
Hit=(1.5,2.5); assert abs(Hit[0]+Hit[1]-4)<1e-9
cand={'K':(0,1),'L':(1,3),'M':(1,1),'N':(1,-2),'P':(-1,0)}
fo=['\\draw[thick] (0,0) -- (4,0) -- (0,4) -- cycle;','\\draw (0,.3) -- (.3,.3) -- (.3,0);']
fo.append(nd((2.65,.7),'cam'))
fo.append(ray((1.5,-1.3),(1.5,0),at=.5)); fo.append(seg((1.5,0),Hit,'very thick,vurgu'))
ends={'K':(1.5,4.5),'L':(2.25,4.75),'M':(3.5,4.5),'N':(3.35,-1.2),'P':(-1.7,2.5)}
for k,e in ends.items():
    if k=='N': fo.append(f'\\draw[gray,thin,dashed] {pt(Hit)} -- (2.75,0) -- {pt(e)};')
    else: fo.append(f'\\draw[gray,thin,dashed] {pt(Hit)} -- {pt(e)};')
lab={'K':((1.5,4.5),'above'),'L':((2.25,4.75),'above'),'M':((3.5,4.5),'right'),'N':((3.35,-1.2),'below'),'P':((-1.7,2.5),'left')}
for k,(p,an) in lab.items(): fo.append(nd(p,f'${k}$',an))
SK=tikz_svg(HEAD+sc('\n'.join(fo),.8)+TAIL)
qr=dict(tipId='fz-op3-prizma-tir',tip='Dik prizmada tam yansıma',z='orta',alt='Tam Yansıma',kaz='Dik ikizkenar cam prizmada ışının hipotenüse 45° ile çarpmasını sınır açısıyla karşılaştırıp çıkış yolunu belirler.',kart='K-FZOP3-07 (dik ikizkenar prizma) · cam, sınır açısı 42°',kalip='şekilli')
q('0007',[A('Girişte sapma var mı?','Işın alt yüzeye dik gönderildiğinden sapmadan girer ve düz ilerleyerek hipotenüse ulaşır.','alt yüzeyde sapma yok'),
  A('Gelme açısını bul','Dik ikizkenar üçgenin hipotenüsü dik kenarlarla 45° yapar; yukarı giden ışın hipotenüsün normaliyle de 45° yapar.','gelme açısı = 45°'),
  A('Sınır açısıyla karşılaştır','Gelme açısı camın sınır açısından (42°) büyük olduğundan ışın hipotenüsten dışarı çıkamaz, tam yansır.','45° > 42° → tam yansıma'),
  A('Yansıma yolunu bul','Normalle 45° yapan ışın, normalin öbür yanında 45° ile yansır; ışın 90° sapar ve sola gider. Sol dik yüzeye dik çarptığı için sapmadan çıkar.','çıkış yolu: P')],
 dogru='P',yan=[('K','Işığın hipotenüsten, doğrultusunu hiç değiştirmeden çıktığını sanmış; tam yansıma koşulunu denetlememiş.','bilgi'),
  ('L','Işığın hipotenüste kırılıp normale doğru yaklaşarak dışarı çıktığını düşünmüş; gelme açısı sınır açısından büyüktür.','bilgi'),
  ('M','Işığın hipotenüsten normal boyunca dışarı çıktığını sanmış; tam yansıma olduğundan ışık dışarı çıkamaz.','bilgi'),
  ('N','Işığın prizmanın içinde ilerleyip alt yüzeyden çıktığını düşünmüş; ışın hipotenüste tam yansıyıp sola yönelir.','dikkat')],
 sira=['K','L','M','N','P'],
 metin='Kesiti şekildeki gibi dik ikizkenar üçgen olan cam bir prizma havada durmaktadır. Camın havaya göre sınır açısı 42°’dir. Tek renkli bir ışık ışını, prizmanın alt yüzeyine yüzeye dik olarak gönderilmektedir. Şekilde ışının hipotenüse çarptığı noktadan çıkan, K, L, M, N ve P ile gösterilen beş yoldan yalnızca biri ışının gerçekte izlediği yoldur.\nBuna göre, ışık ışını prizmadan hangi yoldan çıkar?',
 istenen='Işının izlediği yol.',
 ip=['Işının hipotenüse hangi açıyla çarptığını bul ve bu açıyı camın sınır açısıyla karşılaştır.'],
 bilgi=[B('Tam yansıma','yoğun ortamdan seyrek ortama giden ışının gelme açısı sınır açısından büyükse ışık sınırdan dışarı çıkamaz, tamamen yansır. Örnek: sınır açısı 40° olan bir ortamda 50° ile gelen ışın tam yansır')],
 puf='Gelme açısını sınır açısıyla karşılaştır: büyükse ışın kırılmaz, yansıma yasasına göre tamamen geri döner.',sekil=SK,**qr)

# =============================== 08 · tümsek ayna özel ışınlar (öncüllü) ===============================
kartla('K-FZOP3-08','Tümsek aynada özel ışınlar','Tümsek aynada eksene paralel ışın, yansıyınca uzantısı odak noktasından geçecek biçimde ayrılır; odağa yönelen ışın eksene paralel yansır; merkeze yönelen ışın aynı yoldan geri döner.','Tümsek aynayı çukur ayna gibi çizmek (ışının odakta toplanması); odağa yönelen ışının yansımasını yanlış çizmek.','orta',5,'fz-op3-tumsek-ozel','Tümsek aynada özel ışınlar')
Rr=4; Fp=(2,0); Cm=(4,0)
xq=lambda h: Rr-sqrt(Rr*Rr-h*h)
def Q(h): return (xq(h),h)
hX,hY,hZ=-1.1,.4,1.6
QX,QY,QZ=Q(hX),Q(hY),Q(hZ)
aimF=lambda Qp,x0: (x0, Fp[1]+(Qp[1]-Fp[1])*(x0-Fp[0])/(Qp[0]-Fp[0]))
aimC=lambda Qp,x0: (x0, Cm[1]+(Qp[1]-Cm[1])*(x0-Cm[0])/(Qp[0]-Cm[0]))
sY=aimF(QY,-4.5); sZ=aimC(QZ,-4.5); assert sZ[1]<4 and abs(sY[1])<1.5
fo=[]
arcpts=' -- '.join(pt(Q(h)) for h in [x/10 for x in range(-19,20)])
fo.append(f'\\draw[very thick] {arcpts};')
for h in [x/10 for x in range(-18,19,3)]: fo.append(f'\\draw[thin] {pt(Q(h))} -- {pt((xq(h)+.28,h-.0))};')
fo.append('\\draw[thin] (-4.7,0) -- (5,0);')
for p,t in ((Fp,'$F$'),(Cm,'$M$')): fo.append(f'\\fill {pt(p)} circle (.08); '+nd((p[0],-.12),t,'below'))
# X: eksene paralel gelir; (YANLIŞ) yansıması eksene doğru toplanır çizilmiş
fo.append(ray((-4.5,hX),QX,at=.5)); fo.append(ray(QX,(-4.5,-.2),at=.55)); fo.append(nd((-4.5,hX),'$X$','left'))
# Y: F'ye yönelir; yansıması eksene paralel (DOĞRU)
fo.append(ray(sY,QY,at=.5)); fo.append(f'\\draw[gray,thin,dashed] {pt(QY)} -- {pt(Fp)};'); fo.append(ray(QY,(-4.5,hY),at=.55)); fo.append(nd(sY,'$Y$','left'))
# Z: M'ye yönelir; (YANLIŞ) yansıması eksene paralel çizilmiş
fo.append(ray(sZ,QZ,at=.5)); fo.append(f'\\draw[gray,thin,dashed] {pt(QZ)} -- {pt(Cm)};'); fo.append(ray(QZ,(-4.5,hZ),at=.55)); fo.append(nd(sZ,'$Z$','left'))
SK=tikz_svg(HEAD+sc('\n'.join(fo),.62)+TAIL)
# doğruluk: X: paralel gelen ışının doğru yansıması uzantısı F'den geçer (ayrılır); çizilen ise eksene yaklaşır → yanlış
dxc=(-4.5-QX[0],-.2-hX); dcor=(QX[0]-Fp[0],QX[1]-Fp[1]); assert dxc[1]>0 and dcor[1]<0          # çizilen yukarı (eksene doğru), doğrusu aşağı (ayrılır)
assert hY<hZ and True
qo('0008',[A('X ışınını incele','Eksene paralel gelen ışın, tümsek aynadan yansıyınca ayrılır; yansıyan ışının uzantısı odak noktasından geçer. Çizilen yansıma eksene yaklaşıyor (toplanıyor).','X: yanlış → I. yanlış'),
  A('Y ışınını incele','Odak noktasına yönelen ışın yansıyınca eksene paralel gider; çizim bu kurala uygundur.','Y: doğru → II. doğru'),
  A('Z ışınını incele','Eğrilik merkezine yönelen ışın aynaya dik çarptığı için aynı yoldan geri döner; çizilen yansıma eksene paraleldir.','Z: yanlış → III. yanlış'),
  A('Sonucu belirle','Doğru olan yargıları birleştir.','Yalnız II')],
 truth=(False,True,False),harf='A',tipId='fz-op3-tumsek-ozel',tip='Tümsek aynada özel ışınlar',z='orta',alt='Küresel Ayna',kaz='Tümsek aynada eksene paralel, odağa ve merkeze yönelen ışınların yansıma kurallarını uygulayarak çizimleri değerlendirir.',
 kart='K-FZOP3-08 (tümsek ayna, X–Y–Z ışınları) · özel ışın kuralları',kalip='şekilli',
 metin='Şekilde odak noktası F, eğrilik merkezi M olan bir tümsek aynaya gelen X, Y ve Z ışınlarının yansıma yolları çizilmiştir. Kesikli çizgiler, ışınların ayna arkasındaki doğrultularını göstermektedir.\nBuna göre,\nI. X ışınının yansıma yolu doğru çizilmiştir.\nII. Y ışınının yansıma yolu doğru çizilmiştir.\nIII. Z ışınının yansıma yolu doğru çizilmiştir.\nyargılarından hangileri doğrudur?',
 neden=[('tümsek aynada da paralel ışının eksene doğru toplandığını (çukur ayna gibi) düşünmüş.','bilgi'),
        ('odağa yönelen ışının yansıyınca eksene paralel gideceğini bilmemiş.','bilgi'),
        ('merkeze yönelen ışının da odağa yönelen ışın gibi eksene paralel yansıdığını sanmış.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her ışın için aynaya gelen doğrultuya bak: eksene paralel mi, odağa mı, merkeze mi yönelmiş? Tümsek aynada bu üç özel ışının yansıma kuralını hatırla.'],
 bilgi=[B('Tümsek ayna','ışınları ayırır; oluşan görüntü sanaldır')],
 puf='Tümsek aynada ışın hep ayrılır; odağa yönelen ışın eksene paralel, merkeze yönelen ışın geldiği yoldan yansır.',sekil=SK)

# =============================== 09 · mercek: yarısı kapatılınca görüntü ===============================
kartla('K-FZOP3-09','Merceğin yarısı kapatılınca görüntü','Cismin her noktasından çıkan ışınlar merceğin her yerinden geçip görüntü noktasında toplanır; mercek kısmen kapatılırsa görüntü yine tam oluşur, yalnız ışık miktarı azaldığı için sönükleşir.','Görüntünün de yarı yarıya kaybolacağını sanmak; merceğin tamamı olmadan görüntünün oluşmayacağını düşünmek.','orta',3,'fz-op3-mercek-yarisi','Merceğin yarısı kapatılınca görüntü')
f9,u9=2,3; v9=Fr(f9*u9,u9-f9); assert v9==6 and v9>2*f9                                  # gerçek, ters; görüntü 2F′ ötesinde
fo=['\\draw[thin] (-6,0) -- (7.5,0);','\\draw[{Stealth[length=2.2mm,width=2mm]}-{Stealth[length=2.2mm,width=2mm]},thick] (0,-1.9) -- (0,1.9);']
fo.append('\\draw[very thick] (.13,-1.9) -- (.13,0); '+nd((.3,-1.0),'karton','right'))
fo.append(f'\\draw[thick,-{{Stealth[length=2mm]}}] (-{u9},0) -- (-{u9},1.0); '+nd((-u9,0.55),'cisim','left'))
for x,t in ((-2,'$F$'),(2,'$F^\\prime$'),(-4,'$2F$'),(4,'$2F^\\prime$')): fo.append(f'\\draw[thin] ({x},-.12) -- ({x},.12); '+nd((x,-.12),t,'below'))
fo.append(f'\\draw[very thick] ({v9},-1.9) -- ({v9},1.9);'+''.join(f'\\draw[thin] ({v9},{y/2-1.9}) -- ({v9+.2},{y/2-1.7});' for y in range(0,19))+nd((v9,1.9),'perde','above'))
SK=tikz_svg(HEAD+sc('\n'.join(fo),.6)+TAIL)
qt('0009',[A('Görüntü nasıl oluşur?','Cismin bir noktasından çıkan ışınların hepsi merceğin her bölgesinden kırılıp aynı görüntü noktasında toplanır; bu ışınların bir kısmı kapatılsa da kalanlar aynı noktaya gider.','görüntü noktası ışınların sayısına bağlı değil'),
  A('Kartonun etkisini yorumla','Alt yarı kapatılınca görüntüye giden ışınların yalnız bir kısmı kalır; görüntünün her noktası yine oluşur, ancak o noktaya giden ışık azalır.','görüntü: tam, yeri aynı'),
  A('Parlaklığı karşılaştır','Işık miktarı yaklaşık yarıya düştüğü için görüntü daha sönük olur.','görüntü: daha sönük')],
 'Görüntü aynı yerde ve tam oluşur, ancak daha sönük görünür.',[
  ('Görüntünün yalnızca üst yarısı oluşur.','Kapatılan yarının görüntünün de bir yarısını yok edeceğini sanmış; oysa görüntünün her noktası merceğin tüm yüzeyinden gelen ışınlarla oluşur.','bilgi'),
  ('Görüntü hiç oluşmaz.','Görüntünün oluşması için merceğin tamamının açık olması gerektiğini düşünmüş.','bilgi'),
  ('Görüntü aynı yerde ve tam oluşur; parlaklığı da değişmez.','Işık miktarının mercek yüzeyinin büyüklüğüne bağlı olduğunu unutmuş; kapatılan yarı ışık geçirmez.','dikkat'),
  ('Görüntü merceğe yaklaşır ve küçülür.','Kapatılan yarının merceğin odak uzaklığını ya da görüntü konumunu değiştireceğini düşünmüş.','bilgi')],harf='C',
 tipId='fz-op3-mercek-yarisi',tip='Merceğin yarısı kapatılınca görüntü',z='orta',alt='Mercek',kaz='İnce kenarlı merceğin bir bölümü kapatıldığında görüntünün konumu, boyu ve parlaklığındaki değişimi yorumlar.',
 kart='K-FZOP3-09 (ince kenarlı mercek, yarısı kapalı) · görüntü sönükleşir',kalip='şekilli',
 metin='İnce kenarlı bir merceğin önüne, optik ekseni üzerine bir cisim konulmuş ve merceğin diğer yanında, şekildeki konumdaki perdede cismin net bir görüntüsü elde edilmiştir. Daha sonra merceğin alt yarısı, ışık geçirmeyen bir kartonla şekildeki gibi kapatılıyor. Cisim, mercek ve perde yerinden oynatılmamaktadır.\nBuna göre, perdedeki görüntü için aşağıdakilerden hangisi doğrudur?',
 istenen='Karton konulduktan sonraki görüntünün özelliği.',
 ip=['Cismin bir noktasından çıkan ışınların merceğin hangi bölgelerinden geçebildiğini ve bu ışınların görüntü noktasında nasıl toplandığını düşün.'],
 bilgi=[B('Merceğin görüntü oluşturması','cismin bir noktasından çıkan ve merceğe gelen bütün ışınlar kırıldıktan sonra görüntü noktasında toplanır. Örnek: merceğin ortasından geçen tek bir ışın bile görüntü noktasını belirler')],
 puf='Merceğin bir kısmı kapatılırsa görüntü yine tam oluşur; yalnız geçen ışık azaldığı için sönükleşir.',sekil=SK)

# =============================== 10 · aynadaki saat ===============================
kartla('K-FZOP3-10','Aynadaki saat görüntüsünden gerçek saati bulma','Düzlem aynada görüntü sağ–sol yer değiştirmiş (yatay ters) görünür; aynada okunan saat T ise gerçek saat 12.00 − T’dir.','Aynada okunan saati olduğu gibi yazmak; dakikayı simetrikleyip saati simetriklememek; 12 − T’de dakikadan saate borç almayı unutmak.','kolay',3,'fz-op3-ayna-saat','Aynadaki saatten gerçek saati bulma')
def acik(h,m): return ((h%12)*30+m*.5, m*6)                                      # saat, dakika ibresinin 12'den saat yönündeki açısı
ah,am=acik(7,20); assert (ah,am)==(220.0,120)
gerceh,gercm=acik(4,40); assert abs((-ah)%360-gerceh)<1e-9 and abs((-am)%360-gercm)<1e-9      # aynada x ters: açı → −açı
gercek=(12*60-(7*60+20))%720; assert divmod(gercek,60)==(4,40)
assert divmod((12*60-(7*60+20)+60)%720,60)==(5,40)
fo=['\\draw[thick] (0,0) circle (1.7);']
for k in range(12):
    a=radians(k*30); r0=1.7-(.28 if k%3==0 else .14); w='thick' if k%3==0 else 'thin'
    fo.append(f'\\draw[{w}] ({r0*sin(a):.3f},{r0*cos(a):.3f}) -- ({1.7*sin(a):.3f},{1.7*cos(a):.3f});')
fo.append(f'\\draw[line width=2.4pt] (0,0) -- ({.85*sin(radians(ah)):.3f},{.85*cos(radians(ah)):.3f});')
fo.append(f'\\draw[line width=1.4pt] (0,0) -- ({1.3*sin(radians(am)):.3f},{1.3*cos(radians(am)):.3f});')
fo.append('\\fill (0,0) circle (.07);')
SK=tikz_svg(HEAD+sc('\n'.join(fo),.9)+TAIL)
q('0010',[A('Aynadaki görüntüyü yorumla','Düzlem aynada sağ ile sol yer değiştirir; ibrelerin 12’den saat yönündeki açıları ters yönde ölçülür.','görüntü: 7.20 gibi okunur'),
  A('Gerçek saatle ilişkiyi kur','Aynada okunan zaman T ise gerçek zaman 12.00 − T’dir.','12.00 − 7.20'),
  A('Çıkarmayı yap','12.00 = 11 saat 60 dakika; dakikadan çıkarmak için saatten borç alınır.','11.60 − 7.20 = 4.40')],
 dogru='04.40',yan=[('04.20','Saatin ibrelerinden yalnız saati simetrikledi; dakika ibresinin de ters yönde değiştiğini (20 → 40) hesaba katmamış.','bilgi'),
  ('05.40','12 − 7 = 5 saat ve 60 − 20 = 40 dakika bulmuş; dakikadan çıkarırken saatten 1 borç almayı unutmuş.','islem'),
  ('07.20','Aynada gördüğü saati olduğu gibi gerçek saat sanmış.','dikkat'),
  ('07.40','Yalnız dakikayı simetrikleyip saati olduğu gibi bırakmış.','bilgi')],
 sira=['04.20','04.40','05.40','07.20','07.40'],
 tipId='fz-op3-ayna-saat',tip='Aynadaki saatten gerçek saati bulma',z='kolay',alt='Düzlem Ayna',kaz='Düzlem aynadaki saat görüntüsünden gerçek saati bulur.',
 kart='K-FZOP3-10 (aynadaki saat) · 12.00 − T',kalip='şekilli',
 metin='Bir öğrenci, odasındaki duvar saatinin düzlem aynadaki görüntüsüne bakıyor ve görüntüyü şekildeki gibi görüyor. Saatin kadranında rakam yoktur; kadrandaki dört uzun çizgiden üstte olanı 12’yi, kısa kalın ibre akrebi, uzun ibre yelkovanı göstermektedir.\nBuna göre, duvar saati gerçekte kaçı göstermektedir?',
 istenen='Duvar saatinin gösterdiği zaman.',
 ip=['Düzlem aynada görüntünün sağı solu yer değiştirir; ibrelerin 12’ye göre konumunu bu durumda gerçek saate nasıl çevirirsin?'],
 bilgi=[B('Aynada saat','düzlem aynada görüntü cisme göre simetriktir; sağ ile sol yer değiştirir')],
 puf='Aynadaki saati 12.00’den çıkar; dakikadan çıkarırken saatten borç almayı unutma.',sekil=SK)

bitir(P,'optikuc','fiz|Optik')
