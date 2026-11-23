"""AYT Fizik · Dalga Mekaniği · 20 soru (kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from math import sin,cos,radians,sqrt,pi,sinh,cosh,asinh,floor
H.KONU='Dalga Mekaniği'
P=Parti('dalga','Dalga Mekaniği','afiz|Dalga Mekaniği',ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM AYT 2020–2026 Fizik (Dalga Mekaniği; yalnız mantık) · 345 AYT Fizik s.301–330 · Bilgi Sarmal AYT Fizik · MEB 11–12. sınıf fizik'
TIPLER={'da-yolfarki':'Yol farkı ve girişim koşulu','da-cift':'Işığın çift yarıkta girişimi','da-kirinim':'Dalgalarda kırınım','da-dugum':'Su dalgalarında girişim deseni',
 'da-kirilma':'Dalga leğeninde kırılma','da-tek':'Işığın tek yarıkta kırınımı','da-doppler':'Doppler olayı','da-grafik':'Dalga grafikleri'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AFDA-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AFDA-{kn:02d} ('+CARD[kn]+')',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
DARR='{Stealth[length=1.7mm,width=1.5mm]}-{Stealth[length=1.7mm,width=1.5mm]}'
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def D(a,b,o='thick'): return f'\\draw[{o}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def AR(a,b,o='vurgu,very thick'): return f'\\draw[{o},{ARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def DM(a,b,o='thin'): return f'\\draw[{o},{DARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def DOT(p,r=1.6): return f'\\fill ({p[0]:.3f},{p[1]:.3f}) circle ({r}pt);'
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos):
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if t}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex: parts.append(f'{n}. yargıyı da doğru sanmış; gerçekte {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
# ---------- bilgi kutuları (örnekler soruların sayılarını kullanmaz)
YF=B('Girişim ve yol farkı','eş fazlı iki kaynakta yol farkı Δx = |r₁ − r₂|; Δx = n × λ ise karın (genlik 2A), Δx = (n + ½) × λ ise düğüm (genlik 0). Kaynaklar zıt fazlı ise bu koşullar yer değiştirir. Örnek: λ = 5 cm iken Δx = 10 cm olan nokta karındır')
DG=B('Düğüm ve karın çizgileri','iki kaynağı birleştiren doğru üzerinde ardışık düğüm noktaları arası λ/2’dir; merkez doğrusu karın çizgisidir. λ küçüldükçe çizgi sayısı artar. Örnek: λ = 6 cm ise ardışık düğüm noktaları 3 cm arayla dizilir')
CY=B('Çift yarıkta saçak aralığı','ardışık aydınlık saçaklar arası ΔX = λ × L ÷ d (L: yarıklardan ekrana uzaklık, d: yarıklar arası uzaklık). Ekranda y konumundaki nokta için yol farkı Δx = d × y ÷ L. Örnek: λ = 400 nm, L = 1 m, d = 0,1 mm ise ΔX = 4 mm')
TY=B('Tek yarıkta kırınım','merkezî aydınlık saçağın genişliği w, λ ve L ile doğru, yarık genişliği a ile ters orantılıdır: w ∝ λ × L ÷ a. Yarık daraldıkça desen genişler. Örnek: yalnız a yarıya inerse w iki katına çıkar')
KR=B('Kırınım','dalga, engelin kenarından ya da dar aralıktan geçerken geometrik gölge bölgesine yayılır. Aralık genişliği dalga boyuna yaklaştıkça kırınım belirginleşir; frekans ve dalga boyu değişmez. Örnek: aralık λ kadar ise dalga yarım daire biçiminde yayılır')
KL=B('Dalganın ortam değiştirmesi','geçişte frekans değişmez; v = λ × f olduğundan hız ve dalga boyu doğru orantılı değişir. Eğik geçişte sinθ₁ ÷ sinθ₂ = v₁ ÷ v₂ = λ₁ ÷ λ₂ (açılar normalle yapılır). Örnek: v yarıya inerse λ da yarıya iner')
DP=B('Doppler olayı','kaynak ile gözlemci arasındaki uzaklık azalıyorsa algılanan frekans, kaynağın frekansından büyük; artıyorsa küçüktür. Hareketli kaynakta önde dalga boyu kısalır, arkada uzar; dalganın ortamdaki hızı değişmez. Örnek: yaklaşan trenin düdüğü daha tiz duyulur')
GR=B('Dalga grafikleri','y–x grafiği bir andaki dalga profilini verir: ardışık iki tepe arası λ. y–t grafiği bir noktanın titreşimini verir: ardışık iki tepe arası T. Hız v = λ ÷ T. Örnek: λ = 10 cm, T = 2 s ise v = 5 cm/s')
# ---------- şekil yardımcıları
def dslit(dlab,Llab,nb=2,dx=.5,Pn=None,dark=False,delta=True,plabel='P'):
    """çift yarık şeması; ekranda parlak saçaklar y=n·dx. Pn: P noktasının ekran konumu (dx birimi)"""
    o=[]; xs=0; xe=4.6
    o.append(D((xs,-1.6),(xs,-.45),'very thick')); o.append(D((xs,-.15),(xs,.15),'very thick')); o.append(D((xs,.45),(xs,1.6),'very thick'))
    o.append(AR((-1.0,.3),(-.1,.3),'thin')); o.append(AR((-1.0,-.3),(-.1,-.3),'thin')); o.append(N(-.55,.62,'ışık','font=\\scriptsize'))
    o.append(D((xe,-nb*dx-.5),(xe,nb*dx+.5),'very thick'))
    for n in range(-nb,nb+1):
        o.append(f'\\fill[vurgu!55] ({xe:.2f},{n*dx-.07:.3f}) rectangle ({xe+.22:.2f},{n*dx+.07:.3f});')
    o.append(D((xs,.3),(xe,0),'thin,gray')); o.append(D((xs,-.3),(xe,0),'thin,gray'))
    o.append(DM((xs-1.15,-.3),(xs-1.15,.3))); o.append(N(xs-1.25,0,dlab,'left,font=\\scriptsize'))
    o.append(DM((xs,-1.9),(xe,-1.9))); o.append(N((xs+xe)/2,-2.15,Llab,'font=\\scriptsize'))
    o.append(DOT((xe,0),1.4)); o.append(N(xe+.35,0,'O','right'))
    if delta:
        o.append(DM((xe+1.05,0),(xe+1.05,dx))); o.append(N(xe+1.15,dx/2,'$\\Delta X$','right,font=\\scriptsize'))
    return o
# ===== 01 kolay · yol farkı, zıt değil eş fazlı
card(1,'Yol farkından genlik','Eş fazlı kaynaklarda yol farkı dalga boyunun yarım katıysa nokta düğümdür; genlik sıfırdır.','Yol farkını ya da yol farkı/λ oranını genlik sanmak; tek kaynağın genliğini yazmak.','kolay','şekilli',3,'da-yolfarki','noktanın iki kaynağa uzaklığı verilir')
r1,r2,dd,lam1,A1=14,20,12,4,2
dx1=abs(r1-r2); n1=Fr(dx1,lam1); assert n1==Fr(3,2) and dd+r1>r2 and abs(r1-r2)<=dd
def gen(dx,lam,A,eş=True):
    k=Fr(dx,lam)*2  # yarım dalga boyu sayısı
    if not eş: k+=1
    return 2*A if k%2==0 else (0 if k%2==1 else None)
assert gen(dx1,lam1,A1)==0 and gen(4,4,2)==4 and gen(0,4,2)==4
sc=.2; px=(r1**2-r2**2+dd**2)/(2*dd); py=sqrt(r1**2-px**2)
S1=(0,0); S2=(dd*sc,0); Pp=(px*sc,py*sc)
o=[D(S1,Pp,'thick'),D(S2,Pp,'thick'),DOT(S1,2.2),DOT(S2,2.2),DOT(Pp,2.2)]
o.append(N(-.2,-.1,'S$_1$','left')); o.append(N(S2[0]+.2,-.1,'S$_2$','right')); o.append(N(Pp[0],Pp[1]+.25,'P'))
o.append(N(Pp[0]*.5-.05,Pp[1]*.5,'14 cm','left,font=\\scriptsize')); o.append(N((S2[0]+Pp[0])/2+.05,(S2[1]+Pp[1])/2+.05,'20 cm','above right,font=\\scriptsize'))
o.append(DM((0,-.45),(S2[0],-.45))); o.append(N(S2[0]/2,-.75,'12 cm','font=\\scriptsize'))
SK=tikz(o)
q('0001',tipId='da-yolfarki',tip=TIPLER['da-yolfarki'],z='kolay',alt='Girişim',kaz='İki eş fazlı kaynağın dalgalarının bir noktadaki yol farkından genliği belirler.',kalip='şekilli',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, S₁ ve S₂ özdeş noktasal kaynakları eş fazlı çalışarak dalga boyu 4 cm olan dairesel su dalgaları üretmektedir. Her kaynağın tek başına oluşturduğu dalganın genliği 2 cm’dir ve dalgalar yayılırken genlik azalmamaktadır. Kaynakların ve P noktasının konumları şekilde gösterilmiştir.\nBuna göre, P noktasındaki su parçacığının titreşim genliği kaç cm’dir?',
 sekil=SK,dogru=0,yan=[(Fr(3,2),'Yol farkının dalga boyuna oranını (6 ÷ 4 = 1,5) genlik olarak yazmış.','dikkat'),(2,'P’de yalnız bir kaynağın dalgasının etkili olduğunu düşünüp tek kaynağın genliğini yazmış.','bilgi'),
  (4,'Dalgaların P’de tepe tepeye geldiğini varsayıp genlikleri toplamış: 2 + 2 = 4 cm.','bilgi'),(6,'Yol farkının sayısal değerini (20 − 14 = 6 cm) genlik olarak yazmış.','dikkat')],
 istenen='P noktasındaki titreşim genliği (cm).',
 ip=['Yol farkını bulup dalga boyuna oranla; sonucun tam sayı mı yoksa yarım katlı mı olduğuna bak.'],
 bilgi=[YF],
 ad=[A('Yol farkını bul','Kaynaklar eş fazlı olduğundan yol farkı iki uzaklığın farkıdır.','Δx = 20 − 14 = 6 cm'),
     A('Dalga boyuna oranla','Oran yarım katlıysa tepe, çukurla üst üste gelir.','Δx ÷ λ = 6 ÷ 4 = 1,5 → (n + ½) × λ'),
     A('Genliği yaz','Düğüm noktasında iki dalga birbirini yok eder.','A = 0 cm')],
 puf='Eş fazlı kaynaklarda yol farkı λ’nın yarım katıysa nokta durgundur; genliği hiçbir zaman “yol farkı” sanma.')
# ===== 02 kolay · çift yarık ΔX
card(2,'Saçak aralığı hesabı','ΔX = λ × L ÷ d ifadesinde birimler metreye çevrilir.','Birim dönüşümünde yarık aralığını yanlış okumak; yarım saçak ya da iki saçak aralığını ΔX sanmak.','kolay','şekilli',3,'da-cift','λ, L, d verilir; ΔX istenir')
lam2,L2,d2=Fr(600,10**9),Fr(3,2),Fr(3,10**4)
dX2=lam2*L2/d2; assert dX2==Fr(3,1000)
mm=lambda x:x*1000
assert mm(lam2*L2/(Fr(3,10**3)))==Fr(3,10) and mm(lam2*L2/Fr(3,10**5))==30 and mm(dX2)/2==Fr(3,2) and 2*mm(dX2)==6
SK=tikz(dslit('$d=0{,}3$ mm','$L=1{,}5$ m',nb=2))
q('0002',tipId='da-cift',tip=TIPLER['da-cift'],z='kolay',alt='Çift Yarıkta Girişim',kaz='Çift yarık düzeneğinde saçak aralığını λ, L ve d değerlerinden hesaplar.',kalip='şekilli',
 metin='Dalga boyu 600 nm olan tek renkli ışıkla çift yarık deneyi yapılıyor. Yarıklar arası uzaklık ve yarıklar düzleminden ekrana olan uzaklık şekilde verilmiştir. Ekranda O merkezî aydınlık saçağı, yanında ardışık aydınlık saçaklar oluşmaktadır.\nBuna göre, ekranda ardışık iki aydınlık saçağın orta noktaları arasındaki uzaklık olan ΔX kaç mm’dir?',
 sekil=SK,dogru=3,yan=[(Fr(3,10),'Yarıklar arası uzaklığı 0,3 mm yerine 3 mm almış; birimi yanlış çevirmiş.','islem'),(30,'Yarıklar arası uzaklığı 0,03 mm almış; ondalık kaydırmayı yanlış yapmış.','islem'),
  (Fr(3,2),'Merkezden ilk karanlık saçağa olan uzaklığı (ΔX ÷ 2) hesaplamış.','bilgi'),(6,'Merkezî saçaktan ikinci aydınlık saçağa uzaklığı (2 × ΔX) yazmış.','dikkat')],
 istenen='Ardışık aydınlık saçaklar arası uzaklık ΔX (mm).',
 ip=['Bütün uzunlukları metreye çevirip saçak aralığı bağıntısında λ, L ve d’nin yerini düşün.'],
 bilgi=[CY],
 ad=[A('Birimleri çevir','Hepsi metre cinsinden yazılır.','λ = 600 × 10⁻⁹ m; d = 0,3 × 10⁻³ m; L = 1,5 m'),
     A('Bağıntıyı uygula','Saçak aralığı dalga boyu ve ekran uzaklığıyla doğru, yarık aralığıyla ters orantılıdır.','ΔX = λ × L ÷ d = (600 × 10⁻⁹ × 1,5) ÷ (0,3 × 10⁻³)'),
     A('Sonucu mm’ye çevir','Hesap metre cinsinden çıkar.','ΔX = 3 × 10⁻³ m = 3 mm')],
 puf='Saçak sorularında önce bütün uzunlukları metreye çevir; yanlış kayan her ondalık sonucu on kat değiştirir.')
# ===== 03 kolay · kırınım koşulları (öncüllü)
card(3,'Kırınımı belirginleştirme','Yarık daraldıkça ve dalga boyu büyüdükçe kırınım belirginleşir; genlik etkili değildir.','Genlik artınca dalganın daha çok yayılacağını sanmak.','kolay','öncüllü',3,'da-kirinim','kırınımı etkileyen nicelikler')
SK=None
q('0003',tipId='da-kirinim',tip=TIPLER['da-kirinim'],z='kolay',alt='Kırınım',kaz='Kırınımın belirginliğini yarık genişliği, dalga boyu ve genlikle ilişkilendirir.',kalip='öncüllü',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, düz su dalgaları yatay doğrultuda yerleştirilmiş iki engel arasındaki dar bir aralıktan geçirilerek aralığın arkasındaki yayılma gözlenmektedir. Dalgaların kaynağı sabit frekansla çalışan bir vurucudur.\nAralığın arkasındaki kırınımın daha belirgin olması için,\nI. aralık genişliğini azaltmak,\nII. vurucunun frekansını azaltmak,\nIII. dalgaların genliğini artırmak\nişlemlerinden hangileri yapılabilir?',
 sekil=None,istenen='Kırınımı belirginleştiren işlemler.',
 ip=['Kırınımın belirginliğini aralık genişliğinin dalga boyuna oranı belirler; frekansın değişimi dalga boyunu nasıl etkiler?'],
 bilgi=[KR],
 ad=[A('I. yargı','Aralık λ’ya göre ne kadar dar ise dalga o kadar çok yayılır.','a azalır → kırınım belirginleşir → I doğru'),
     A('II. yargı','Derinlik sabit olduğundan v değişmez; v = λ × f.','f azalır → λ artar → a ÷ λ küçülür → II doğru'),
     A('III. yargı','Genlik dalganın yayılma doğrultusunu değil, taşıdığı enerjiyi belirler.','Genlik artınca kırınım değişmez → III yanlış')],
 puf='Kırınım a ÷ λ oranına bağlıdır: yarık daralınca ya da dalga boyu büyüyünce belirginleşir; genlik oranı etkilemez.',
 **onc([True,True,False],['aralık daraldıkça dalga daha çok yayılır','frekans azalınca dalga boyu artar ve aralık λ’ya göre dar kalır','genlik kırınımın belirginliğini değiştirmez'],1))
# ===== 04 orta · düğüm çizgisi sayısı
def nodal_lines(d,lam,antiphase=False):
    """kaynakları birleştiren doğrunun iki yanındaki düğüm çizgisi sayısı (eş fazlı)"""
    L=Fr(lam); n=0; k=0
    while (k+Fr(1,2))*L<d: n+=1; k+=1
    assert (k+Fr(1,2))*L!=d
    return 2*n
def karin_lines(d,lam):
    L=Fr(lam); n=0; k=1
    while k*L<d: n+=1; k+=1
    return 1+2*n
def nodal_fig(d,lam,sc,ymax,labelpair=True):
    c=Fr(d,2); o=[]; xs_nodes=[]
    k=0
    while (k+Fr(1,2))*lam<d:
        Dl=(k+Fr(1,2))*lam; a=float(Dl/2); b=sqrt(float(c)**2-a*a); tm=asinh(ymax/b)
        for sg in (1,-1):
            pp=[(sg*a*cosh(-tm+2*tm*i/40)*sc,b*sinh(-tm+2*tm*i/40)*sc) for i in range(41)]
            o.append('\\draw[thick,dash pattern=on 3pt off 2pt,vurgu] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pp)+';')
        xs_nodes.append(a); k+=1
    S1=(-float(c)*sc,0); S2=(float(c)*sc,0)
    o.append(D((-float(c)*sc-.5,0),(float(c)*sc+.5,0),'thin,gray'))
    o.append(DOT(S1,2.4)); o.append(DOT(S2,2.4)); o.append(N(S1[0],-.3,'S$_1$')); o.append(N(S2[0],-.3,'S$_2$'))
    for a in xs_nodes:
        for sg in (1,-1): o.append(DOT((sg*a*sc,0),1.5))
    if labelpair:
        x1,x2=xs_nodes[0]*sc,xs_nodes[1]*sc; yy=.45
        o.append(DM((x1,yy),(x2,yy))); o.append(N((x1+x2)/2,yy+.22,f'${fm(Fr(xs_nodes[1]-xs_nodes[0]).limit_denominator(100))}$ cm','font=\\scriptsize'))
    o.append(DM((S1[0],-ymax*sc-.15),(S2[0],-ymax*sc-.15))); o.append(N(0,-ymax*sc-.4,f'${d}$ cm','font=\\scriptsize'))
    o.append(f'\\draw[thick,dash pattern=on 3pt off 2pt,vurgu] ({-float(c)*sc-.5:.2f},{-ymax*sc-.85:.2f}) -- ++(.7,0); '+N(-float(c)*sc+.35,-ymax*sc-.85,'düğüm çizgisi','right,font=\\scriptsize'))
    return o
from math import cosh
d4,lam4=8,4; sc4=.42
assert nodal_lines(d4,lam4)==4 and nodal_lines(d4,Fr(lam4,2))==8 and nodal_lines(d4,lam4*2)==2 and nodal_lines(d4,Fr(lam4,4))==16 and karin_lines(d4,Fr(lam4,2))==7
card(4,'Frekans ve düğüm çizgisi sayısı','Düğüm noktaları arası λ/2’dir; frekans artınca λ küçülür ve çizgi sayısı artar.','Düğüm noktaları arası uzaklığı λ sanmak; karın çizgilerini saymak.','orta','şekilli',4,'da-dugum','düğüm noktaları aralığından λ, yeni f ile çizgi sayısı')
SK=tikz(nodal_fig(d4,lam4,sc4,6.5))
q('0004',tipId='da-dugum',tip=TIPLER['da-dugum'],z='orta',alt='Girişim Deseni',kaz='Düğüm noktası aralığından dalga boyunu bulur; frekans değişince düğüm çizgisi sayısını belirler.',kalip='şekilli',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, eş fazlı çalışan S₁ ve S₂ özdeş noktasal kaynaklarının oluşturduğu girişim deseninde düğüm çizgileri kesikli çizgilerle gösterilmiştir. Kaynaklar arası uzaklık ve kaynakları birleştiren doğru üzerinde ardışık iki düğüm noktası arasındaki uzaklık şekilde verilmiştir.\nSu derinliği ve kaynaklar arası uzaklık değiştirilmeden kaynakların frekansı iki katına çıkarılıyor.\nBuna göre, yeni girişim deseninde toplam kaç düğüm çizgisi gözlenir?',
 sekil=SK,dogru=8,yan=[(4,'Frekansın dalga boyunu etkilemediğini düşünerek desenin değişmediğini kabul etmiş.','bilgi'),(2,'Frekans artınca dalga boyunun da arttığını sanmış (λ = 8 cm); bu durumda yalnız iki düğüm çizgisi kalır.','bilgi'),
  (7,'Merkez doğrusunu da içine alacak biçimde karın çizgilerini saymış: 1 + 2 × 3 = 7.','dikkat'),(16,'Ardışık düğüm noktaları arası uzaklığı (2 cm) dalga boyu sanmış; yeni λ = 1 cm bularak 16 çizgi saymış.','bilgi')],
 istenen='Frekans iki katına çıkınca oluşan düğüm çizgisi sayısı.',
 ip=['Ardışık düğüm noktaları arası uzaklığın dalga boyuyla ilişkisini kur, sonra yeni λ ile aynı koşulu yeniden sağla.'],
 bilgi=[DG,YF],
 ad=[A('Dalga boyunu bul','Ardışık düğüm noktaları arası λ ÷ 2’dir.','2 = λ ÷ 2 → λ = 4 cm'),
     A('Yeni dalga boyu','Hız sabit, frekans iki katı olunca dalga boyu yarıya iner.','λ′ = 2 cm'),
     A('Düğüm koşulu','Düğüm için yol farkı (n + ½) × λ′ olmalı ve en çok kaynaklar arası uzaklık (8 cm) kadar olabilir.','Δx = 1, 3, 5, 7 cm (9 cm > 8 cm)'),
     A('Çizgileri say','Her yol farkı merkez doğrusunun iki yanında birer çizgi verir.','4 × 2 = 8 düğüm çizgisi')],
 puf='Frekans artınca λ küçülür; aynı kaynak aralığına daha çok yarım dalga boyu sığar, düğüm çizgisi sayısı artar.')
# ===== 05 orta · derin–sığ geçiş (dik) öncüllü
card(5,'Sığ bölgeye dik geçiş','Frekans ve periyot ortam değiştirince değişmez; hız dalga boyuyla orantılı değişir.','Sığ bölgede frekansın azaldığını sanmak.','orta','şekilli',3,'da-kirilma','dalga cephesi aralığından hız ve frekans')
v5,l1,l2=12,6,4; f5=Fr(v5,l1); v52=l2*f5; assert f5==2 and v52==8 and Fr(1,f5)==Fr(1,2) and v5/l1==f5
sc=.2; xb=3.0*1.2
o=[D((xb,-1.5),(xb,1.5),'thick,dashed')]
for n in range(3): o.append(D((xb-.6-n*l1*sc*1.0,-1.2),(xb-.6-n*l1*sc*1.0,1.2),'thick,vurgu'))
for n in range(4): o.append(D((xb+.4+n*l2*sc,-1.2),(xb+.4+n*l2*sc,1.2),'thick,vurgu'))
xa=xb-.6; o.append(DM((xa-l1*sc,1.45),(xa,1.45))); o.append(N(xa-l1*sc/2,1.75,'$6$ cm','font=\\scriptsize'))
xc=xb+.4; o.append(DM((xc,1.45),(xc+l2*sc,1.45))); o.append(N(xc+l2*sc/2,1.75,'$4$ cm','font=\\scriptsize'))
o.append(AR((.1,-1.6),(1.1,-1.6),'thin')); o.append(N(.6,-1.9,'dalga yönü','font=\\scriptsize'))
o.append(N(xb-1.2,-1.0,'derin','font=\\scriptsize')); o.append(N(xb+.8,-1.0,'sığ','font=\\scriptsize'))
SK=tikz(o)
q('0005',tipId='da-kirilma',tip=TIPLER['da-kirilma'],z='orta',alt='Dalga Leğeninde Kırılma',kaz='Su dalgasının derin ortamdan sığ ortama geçişinde frekans, periyot, hız ve dalga boyunu karşılaştırır.',kalip='şekilli',
 metin='Derinliği iki farklı bölgeden oluşan bir dalga leğeninde, derin bölgeden sığ bölgeye düz su dalgaları sınıra dik olarak gelmektedir. Dalga tepelerinin (cephelerinin) konumları, ardışık tepeler arası uzaklıklarla birlikte şekilde verilmiştir. Derin bölgedeki dalgaların yayılma hızı 12 cm/s’dir.\nBuna göre,\nI. sığ bölgede dalgaların frekansı 2 Hz’den küçüktür,\nII. sığ bölgede dalgaların yayılma hızı 8 cm/s’dir,\nIII. dalgaların periyodu iki bölgede de 0,5 s’dir\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Ortam değiştiren dalgada hangi nicelik aynı kalır? Derin bölgedeki verilerden o niceliği hesapla.'],
 bilgi=[KL,GR],
 ad=[A('Derin bölge','Hız ve dalga boyundan frekans bulunur.','f = v ÷ λ = 12 ÷ 6 = 2 Hz · T = 0,5 s'),
     A('Sığ bölge','Frekans ve periyot değişmez; hız yeni dalga boyuyla bulunur.','f = 2 Hz → v′ = λ′ × f = 4 × 2 = 8 cm/s'),
     A('Yargıları değerlendir','I yanlış (f = 2 Hz), II doğru (8 cm/s), III doğru (T = 1 ÷ 2 = 0,5 s).','II ve III doğru')],
 puf='Ortam değiştiren dalgada kaynağa bağlı nicelikle ortama bağlı nicelikleri ayır; verilen veriyi önce hangisinin sabit kaldığına göre kullan.',
 **onc([False,True,True],['frekans ortam değiştirince değişmez, sığ bölgede de 2 Hz’dir','v = λ × f = 4 × 2 olduğundan sığ bölgedeki hız 8 cm/s’dir','periyot frekansın tersidir ve ortam değişince değişmez; T = 0,5 s’dir'],3))
# ===== 06 orta · tek yarık (öncüllü)
def tekfig(a,Llab,alab,w=.6,gapx=.0,pw=1.6,kol=True,ymid=0,xe=4.2,lab=True,sx=0):
    """tek yarık şeması: w = merkezî saçağın yarı genişliği (cm)"""
    o=[]; xs=sx
    o.append(D((xs,-1.7),(xs,-a/2),'very thick')); o.append(D((xs,a/2),(xs,1.7),'very thick'))
    o.append(AR((xs-1.2,0),(xs-.1,0),'thin')); 
    o.append(D((xs+xe,-1.7),(xs+xe,1.7),'very thick'))
    pts=[]
    for i in range(-60,61):
        y=i/60*3*w
        t=0 if y==0 else pi*y/w
        I=1 if y==0 else (sin(t)/t)**2
        pts.append((xs+xe+.12+I*pw,y))
    o.append('\\draw[thick,vurgu] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+';')
    o.append(D((xs+xe+.12,-3*w),(xs+xe+.12,3*w),'thin'))
    o.append(DM((xs+.3,-a/2),(xs+.3,a/2),'thin')); o.append(N(xs+.4,0,alab,'right,font=\\scriptsize'))
    o.append(DM((xs,-1.95),(xs+xe,-1.95))); o.append(N(xs+xe/2,-2.2,Llab,'font=\\scriptsize'))
    return o
card(6,'Merkezî saçak genişliği','Merkezî aydınlık saçağın genişliği λ ve L ile artar, yarık genişliği ile azalır.','Yarık genişlediğinde desenin de genişleyeceğini sanmak.','orta','şekilli',3,'da-tek','w ∝ λ·L/a niteliksel')
SK=tikz(tekfig(.55,'$L$','$a$',w=.55,lab=False))
q('0006',tipId='da-tek',tip=TIPLER['da-tek'],z='orta',alt='Tek Yarıkta Kırınım',kaz='Tek yarıkta merkezî aydınlık saçağın genişliğini etkileyen niceliklerin değişimini yorumlar.',kalip='şekilli',
 metin='Dalga boyu λ olan tek renkli ışık, genişliği a olan tek bir yarıktan geçirilerek yarıktan L uzaklıktaki ekranda kırınım deseni elde ediliyor. Şekilde ekrandaki ışık şiddetinin konuma bağlı değişimi gösterilmiştir.\nMerkezî aydınlık saçağın genişliğini artırmak için, diğer nicelikler değiştirilmeden;\nI. yarık genişliğini artırmak,\nII. dalga boyu daha büyük olan ışık kullanmak,\nIII. ekranı yarıktan daha uzağa yerleştirmek\nişlemlerinden hangileri yapılabilir?',
 sekil=SK,istenen='Merkezî saçağı genişleten işlemler.',
 ip=['Merkezî saçağın genişliğinin yarık genişliği, dalga boyu ve ekran uzaklığıyla orantısını düşün.'],
 bilgi=[TY],
 ad=[A('Bağıntıyı yaz','Merkezî saçak genişliği doğru/ters orantılara bağlıdır.','w ∝ λ × L ÷ a'),
     A('I. yargı','Yarık genişleyince a artar, w azalır.','I yanlış'),
     A('II. ve III. yargılar','λ ya da L artarsa w de artar.','II doğru · III doğru')],
 puf='Merkezî saçak genişliğini yarık genişliği, λ ve L ile ilişkilendiren orantıyı yaz; her niceliğin payda mı pay mı olduğuna bak.',
 **onc([False,True,True],['yarık genişleyince merkezî aydınlık saçak daralır','dalga boyu arttıkça saçak genişler','ekran uzaklaştıkça aynı açısal yayılım daha geniş bir bölgeye düşer'],4))
# ===== 07 orta · engel kenarında kırınım (öncüllü)
lam7=.8
o=[]
for k in range(1,4):
    r=k*lam7; o.append(f'\\draw[thick,vurgu] ({r:.3f},0) arc[start angle=0,end angle=-90,radius={r:.3f}];'); o.append(D((r,0),(r,1.9),'thick,vurgu'))
for k in range(0,3): o.append(D((-.45-k*lam7,-1.9),(-.45-k*lam7,1.9),'thick,vurgu'))
o.append(D((0,-2.1),(0,0),'very thick'))
o.append(f'\\draw[thin] (0,0) circle (1.5pt);')
o.append(N(-.25,-1.2,'engel','left,font=\\scriptsize'))
o.append(DM((-.45-lam7,2.0),(-.45,2.0))); o.append(N(-.45-lam7/2,2.3,'$\\lambda$','font=\\scriptsize'))
SK=tikz(o)
card(7,'Engel kenarında kırınım','Kırınımda f, λ ve v değişmez; dalga engelin gölge bölgesine de yayılır.','Gölge bölgesine geçen dalganın dalga boyunun ya da hızının değiştiğini sanmak.','orta','şekilli',3,'da-kirinim','düz dalgalar engelin kenarından geçer')
q('0007',tipId='da-kirinim',tip=TIPLER['da-kirinim'],z='orta',alt='Dalga Leğeninde Kırınım',kaz='Engel kenarından geçen su dalgalarında değişen ve değişmeyen niceliklere kırınım olayıyla karar verir.',kalip='şekilli',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, sabit frekanslı bir vurucunun oluşturduğu düz su dalgaları, şekildeki gibi yalnızca leğenin alt yarısını kaplayan bir engele doğru ilerlemektedir. Şekilde dalga tepeleri gösterilmiş olup engelin kenarından geçen dalgaların engelin arkasındaki gölge bölgesine de yayıldığı görülmektedir.\nBuna göre,\nI. gölge bölgesindeki dalgaların dalga boyu, engelin üst tarafındaki dalgaların dalga boyundan küçüktür,\nII. gölge bölgesindeki dalgaların frekansı vurucunun frekansına eşittir,\nIII. gölge bölgesindeki dalgaların yayılma hızı, engelin üst tarafındaki dalgaların hızından küçüktür\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargı.',
 ip=['Derinlik her yerde aynı iken dalganın hızını, dalga boyunu ve frekansını hangi etkenlerin belirlediğini düşün.'],
 bilgi=[KR],
 ad=[A('Dalga boyu','Hız ortamla, frekans kaynakla belirlenir; λ = v ÷ f.','v ve f sabit → λ gölgede de aynı → I yanlış'),
     A('Frekans','Frekansı yalnızca vurucu belirler; kırınım bunu değiştirmez.','f(gölge) = f(vurucu) → II doğru'),
     A('Hız','Derinlik her yerde aynı olduğundan dalga hızı her bölgede aynıdır.','v sabit → III yanlış')],
 puf='Kırınımda dalganın yalnızca yayılma doğrultusu değişir; v, f ve λ aynı kalır.',
 **onc([False,True,False],['kırınım dalga boyunu değiştirmez; derinlik sabit olduğundan λ = v ÷ f her yerde aynıdır','frekansı kaynak belirler; kırınım bu değeri değiştirmez','dalganın hızı yalnızca ortama bağlıdır; derinlik sabit olduğundan hız her yerde aynıdır'],0))
# ===== 08/09 Doppler çember şekilleri
vsr8=Fr(1,3); lam08=.85
o=[]
for k in range(1,4): o.append(f'\\draw[thick,vurgu] ({-k*float(vsr8)*lam08:.3f},0) circle ({k*lam08:.3f});')
o.append(DOT((0,0),2.4)); o.append(N(0,-.3,'K','below')); o.append(AR((.12,0),(.75,0),'thin'))
for nm,xx in (('A',1.25),('B',-2.1)):
    o.append(DOT((xx,0),2.2)); o.append(N(xx,.3,nm,'above'))
SK=tikz(o)
vs8,vw8=1,3
f_ahead=lambda f0,vs,vw:f0*vw/(vw-vs); f_back=lambda f0,vs,vw:f0*vw/(vw+vs)
assert f_ahead(1,vs8,vw8)>1>f_back(1,vs8,vw8)
card(8,'Hareketli kaynakta Doppler','Kaynak önünde λ küçük, f büyük; arkasında λ büyük, f küçük; dalga hızı ortama bağlıdır.','Dalga hızının kaynağın yönünde arttığını sanmak.','orta','şekilli',3,'da-doppler','hareketli kaynak ve durgun gözlemciler')
q('0008',tipId='da-doppler',tip=TIPLER['da-doppler'],z='orta',alt='Doppler Olayı',kaz='Hareketli kaynağın oluşturduğu dalga cephelerinden önde ve arkadaki gözlemciler için dalga boyu, frekans ve hızı karşılaştırır.',kalip='şekilli',
 metin='Durgun bir gölde, sabit frekansta dairesel su dalgaları üreten küçük bir şamandıra K, sabit hızla sağa doğru ilerlemektedir. Şamandıranın hızı su dalgalarının hızından küçüktür. Şekilde bu andaki dalga tepeleri gösterilmiştir. Suya göre durgun olan A ve B gözlemcileri K ile aynı doğru üzerindedir.\nBuna göre,\nI. A’da ölçülen dalga boyu B’de ölçülenden küçüktür,\nII. A’da algılanan frekans B’de algılanandan büyüktür,\nIII. dalgaların A’ya ulaşma hızı B’ye ulaşma hızından büyüktür\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Dalga cephelerinin hangi tarafta sıklaştığına bak; dalganın suya göre hızını neyin belirlediğini düşün.'],
 bilgi=[DP],
 ad=[A('Cephelerin dizilişi','Şamandıra ilerlediği için önünde (A tarafında) cepheler sıkışır, arkasında (B tarafında) aralanır.','λ(A) < λ(B) → I doğru'),
     A('Frekans','Hız aynı, dalga boyu küçük olan yerde frekans büyüktür.','f = v ÷ λ → f(A) > f(B) → II doğru'),
     A('Hız','Dalganın suya göre hızı yalnızca ortama bağlıdır, kaynağın hareketinden etkilenmez.','v(A) = v(B) → III yanlış')],
 puf='Hareketli kaynakta hangi niceliklerin kaynağa, hangisinin ortama bağlı olduğunu ayırarak her gözlemciyi ayrı değerlendir.',
 **onc([True,True,False],['kaynağın önünde dalga cepheleri sıklaşır ve dalga boyu kısalır','hız sabit olduğundan dalga boyu küçük olan yerde frekans büyüktür','dalganın suya göre hızı kaynağın hareketinden bağımsızdır ve her iki yönde aynıdır'],1))
# ===== 09 zor · Doppler dalga boyları → kaynak hızı
vw9,lf9,lb9=12,3,5
lam09=Fr(lf9+lb9,2); vs9=Fr(vw9*(lb9-lf9),lb9+lf9); f09=Fr(vw9)/lam09
assert lam09==4 and vs9==3 and f09==3 and (vw9-vs9)/f09==lf9 and (vw9+vs9)/f09==lb9
assert (lb9-lf9)*f09==6 and Fr(vw9*(lb9-lf9),lf9)==8 and lf9*f09==9 and lb9-lf9==2
u9=.3; vsT=float(vs9/f09)  # vs·T (cm)
o=[]
for k in range(1,4): o.append(f'\\draw[thick,vurgu] ({-k*vsT*u9:.3f},0) circle ({k*float(lam09)*u9:.3f});')
o.append(DOT((0,0),2.4)); o.append(N(0,-.3,'K','below')); o.append(AR((.12,0),(.85,0),'thin'))
xf=[(float(lam09)-vsT)*k*u9 for k in (1,2)]; xb=[-(float(lam09)+vsT)*k*u9 for k in (1,2)]
assert abs((xf[1]-xf[0])/u9-lf9)<1e-9 and abs((xb[0]-xb[1])/u9-lb9)<1e-9
o.append(DM((xf[0],.28),(xf[1],.28))); o.append(N((xf[0]+xf[1])/2,.58,'$3$ cm','font=\\scriptsize'))
o.append(DM((xb[1],.28),(xb[0],.28))); o.append(N((xb[0]+xb[1])/2,.58,'$5$ cm','font=\\scriptsize'))
SK=tikz(o)
card(9,'Dalga boylarından kaynak hızı','Önde λ = (v − vₖ)T, arkada λ = (v + vₖ)T; farktan vₖ bulunur.','Önde ve arkadaki dalga boyunu ayrı ayrı ele alıp farkı yarıya bölmeyi unutmak.','zor','şekilli',5,'da-doppler','ön ve arka dalga boyundan kaynak hızı')
q('0009',tipId='da-doppler',tip=TIPLER['da-doppler'],z='zor',alt='Doppler Olayı',kaz='Hareketli kaynağın önündeki ve arkasındaki dalga boylarından kaynağın hızını hesaplar.',kalip='şekilli',
 metin='Durgun bir gölde, sabit frekansla dairesel dalgalar üreten K kaynağı, suya göre sabit hızla sağa doğru ilerlemektedir. Gölde dalgaların suya göre yayılma hızı 12 cm/s’dir. Şekilde kaynağın o andaki konumu ve dalga tepeleri gösterilmiş; kaynağın önünde ve arkasında ardışık iki tepe arası uzaklık verilmiştir.\nBuna göre, K kaynağının suya göre hızı kaç cm/s’dir?',
 sekil=SK,dogru=3,yan=[(2,'Ön ve arka dalga boyları farkını (5 − 3 = 2 cm) doğrudan hız olarak yazmış.','dikkat'),(6,'Dalga boyları farkını (2 cm) kaynak frekansıyla çarpıp (2 × 3 = 6) yarıya bölmeyi unutmuş; oysa fark 2 × vₖ × T’dir.','islem'),
  (8,'Ön dalga boyundan frekansı (12 ÷ 3 = 4 Hz) bulup dalga boyları farkıyla (2 cm) çarpmış: 4 × 2 = 8 cm/s.','bilgi'),(9,'Ön dalga boyu ile kaynak frekansını çarpıp (3 × 3) dalganın kaynağa göre hızını hesaplamış; bu da kaynağın değil v − vₖ değeridir.','bilgi')],
 istenen='K kaynağının suya göre hızı (cm/s).',
 ip=['Kaynak durgun olsaydı ardışık tepeler arası uzaklık kaç olurdu? Önde ve arkada bu değerden ne kadar sapıldığına bak.'],
 bilgi=[DP,GR],
 ad=[A('Ön ve arka dalga boyları','Bir periyotta dalga v × T yol alırken kaynak vₖ × T yol alır.','Önde: λ₁ = (v − vₖ) × T = 3 · Arkada: λ₂ = (v + vₖ) × T = 5'),
     A('Durgun kaynak dalga boyu','İki ifadenin ortalaması vₖ’nın etkisini yok eder.','λ₀ = v × T = (3 + 5) ÷ 2 = 4 cm'),
     A('Periyot ve frekans','Dalga hızı ve λ₀’dan frekans bulunur.','f = v ÷ λ₀ = 12 ÷ 4 = 3 Hz · T = 1/3 s'),
     A('Kaynak hızı','İki dalga boyu farkı 2 × vₖ × T’dir.','5 − 3 = 2 × vₖ × T → vₖ = 2 ÷ (2 × 1/3) = 3 cm/s')],
 puf='Hareketli kaynakta önde ve arkadaki dalga boyları farkı 2 × vₖ × T’dir; ortalaması ise durgun kaynağın dalga boyudur.')
# ===== 10 orta · ışığın Doppler etkisi (öncüllü)
card(10,'Işığın Doppler etkisi','Doppler etkisinde algılanan nicelikler ile kaynaktan bağımsız sabit kalan nicelik ayrı ayrı sorgulanır.','Doppler etkisinde ışığın hızının da değiştiğini sanmak.','orta','öncüllü',3,'da-doppler','uzaklaşan galaksiden gelen ışık')
q('0010',tipId='da-doppler',tip=TIPLER['da-doppler'],z='orta',alt='Doppler Olayı',kaz='Doppler etkisinin elektromanyetik dalgalarda frekans, dalga boyu ve hız üzerindeki sonuçlarını yorumlar.',kalip='öncüllü',
 metin='Bir astronom, uzak bir galaksiden gelen ışığın tayfındaki hidrojen çizgilerinin frekanslarını ölçüyor. Ölçülen frekansların, aynı çizgiler için yer laboratuvarında ölçülen frekanslardan küçük olduğunu görüyor. Bu farkın yalnızca Doppler etkisinden kaynaklandığı kabul ediliyor.\nBuna göre,\nI. galaksi, Dünya’dan uzaklaşmaktadır,\nII. galaksiden gelen ışığın dalga boyu laboratuvarda ölçülenden küçüktür,\nIII. galaksiden gelen ışığın boşluktaki hızı laboratuvarda ölçülenden küçüktür\nyargılarından hangileri kesinlikle doğrudur?',
 sekil=None,istenen='Kesinlikle doğru olan yargı.',
 ip=['Gözlemciden uzaklaşan kaynakta algılanan frekans nasıl değişir? Frekans, dalga boyu ve hız arasındaki bağıntıyı da düşün.'],
 bilgi=[DP,B('Elektromanyetik dalgalarda hız','ışık, boşlukta kaynağın hareketinden bağımsız olarak aynı hızla (c) yayılır; Doppler etkisinde yalnızca frekans ve dalga boyu değişir. Örnek: kaynak hızlansa da ışığın boşluktaki hızı değişmez')],
 ad=[A('Frekans küçülmesinin anlamı','Uzaklaşan kaynaktan gelen dalganın algılanan frekansı küçülür.','f ölçülen < f laboratuvar → uzaklaşma → I doğru'),
     A('Dalga boyu','Boşlukta c = λ × f sabit hızla bağlıdır; frekans küçülünce dalga boyu büyür.','λ ölçülen > λ laboratuvar → II yanlış'),
     A('Hız','Işığın boşluktaki hızı kaynağın hareketinden bağımsızdır.','c sabit → III yanlış')],
 puf='Doppler olayında kaynaktan bağımsız sabit kalan niceliği sorgula; diğer nicelikleri ona bağlı yaz.',
 **onc([True,False,False],['frekansın küçük ölçülmesi kaynağın uzaklaştığını gösterir','boşlukta c = λ × f sabit olduğundan frekans küçük ölçülünce dalga boyu büyük ölçülür','ışığın boşluktaki hızı kaynağın hareketinden bağımsız olarak sabittir'],0))
# ===== 11 orta · tablo: ΔX karşılaştırması
ham=[(400,Fr(1,2),Fr(3,2)),(650,Fr(1,10),Fr(1)),(450,Fr(1,2),Fr(5,2)),(450,Fr(1,5),Fr(3)),(700,Fr(1,5),Fr(5,2))]
deney=[('KLMNP'[i],)+ham[i] for i in range(5)]
def dX(l,d,L): return Fr(l,10**9)*L/(d/1000)*1000   # mm
vals=[dX(l,d,L) for _,l,d,L in deney]; assert max(vals)==vals[4] and sorted(vals)==sorted([Fr(6,5),Fr(13,2),Fr(35,4),Fr(9,4),Fr(27,4)])
kural=lambda f:[f(l,d,L) for _,l,d,L in deney]
def kazan(f):
    v=kural(f); m=max(v); assert v.count(m)==1; return 'KLMNP'[v.index(m)]
w_L=kazan(lambda l,d,L:Fr(l)/d); w_ld=kazan(lambda l,d,L:Fr(l)*d/L); w_Ld=kazan(lambda l,d,L:L/d); w_all=kazan(lambda l,d,L:Fr(l)*L*d)
assert len({w_L,w_ld,w_Ld,w_all,'P'})==5
SK=tablo_svg(['Deney','λ (nm)','d (mm)','L (m)'],[[n,str(l),fm(d),fm(L)] for n,l,d,L in deney])
card(11,'Saçak aralığı karşılaştırması','ΔX = λ·L/d bağıntısıyla farklı düzeneklerin saçak aralıkları karşılaştırılır.','L ya da d’nin etkisini atlayıp yalnız λ’ya bakmak; d’yi payda yerine paya koymak.','orta','tablo',4,'da-cift','tablodan en büyük ΔX')
q('0011',tipId='da-cift',tip=TIPLER['da-cift'],z='orta',alt='Çift Yarıkta Girişim',kaz='Farklı çift yarık düzeneklerinde saçak aralığını λ, L ve d değerleriyle karşılaştırır.',kalip='tablo',
 metin='Beş öğrenci, çift yarık düzeneğiyle tek renkli ışık kullanarak girişim deseni elde ediyor. Her deneyde kullanılan ışığın dalga boyu (λ), yarıklar arası uzaklık (d) ve yarıklar düzleminden ekrana olan uzaklık (L) aşağıdaki tabloda verilmiştir.\nBuna göre, hangi deneyde ekranda ardışık aydınlık saçakların orta noktaları arasındaki uzaklık en büyüktür?',
 sekil=SK,dogru='P deneyi',yan=[(w_L+' deneyi','Saçak aralığının yalnız λ ÷ d oranına bağlı olduğunu düşünüp ekran uzaklığını hesaba katmamış.','dikkat'),(w_ld+' deneyi','Saçak aralığını λ × d ÷ L biçiminde kurmuş; yarık aralığını paya yazmış.','bilgi'),
  (w_Ld+' deneyi','Yalnız L ÷ d oranına bakmış; dalga boyunun etkisini unutmuş.','dikkat'),(w_all+' deneyi','Üç büyüklüğü de çarpıp saçak aralığını λ × L × d ile orantılı sanmış.','bilgi')],
 sira=['K deneyi','L deneyi','M deneyi','N deneyi','P deneyi'],
 istenen='Saçak aralığının en büyük olduğu deney.',
 ip=['Saçak aralığı için λ, L ve d’nin hangisinin payda, hangilerinin pay olduğunu belirle; sonra her satır için oranı karşılaştır.'],
 bilgi=[CY],
 ad=[A('Bağıntı','Saçak aralığı bu üç büyüklükten oluşan orana bağlıdır.','ΔX ∝ λ × L ÷ d'),
     A('Her deney için oran','Birimleri ortak tutup (nm, mm, m) λ × L ÷ d hesaplanır.','K: 400 × 1,5 ÷ 0,5 = 1200 · L: 650 × 1 ÷ 0,1 = 6500 · M: 450 × 2,5 ÷ 0,5 = 2250 · N: 450 × 3 ÷ 0,2 = 6750 · P: 700 × 2,5 ÷ 0,2 = 8750'),
     A('En büyüğü seç','En büyük oran en büyük saçak aralığını verir.','P deneyi')],
 puf='Saçak aralığı karşılaştırmasında her satır için λ × L ÷ d oranını hesapla; tek bir büyüklüğe bakarak karar verme.')
# ===== 12 orta · y–x ve y–t grafikleri
def ax_plot(at,xmax,xt,xl,yl,fn,tit,wd=6.6):
    pts=' '.join(f'({xmax*i/80:.4f},{fn(xmax*i/80):.4f})' for i in range(81))
    return (f'\\begin{{axis}}[at={{(0cm,{at}cm)}},anchor=south west,width={wd}cm,height=3.3cm,xmin=0,xmax={xmax},ymin=-3,ymax=3,xtick={{{xt}}},ytick={{-2,0,2}},grid=both,major grid style={{gray!55,thin}},tick label style={{font=\\scriptsize}},axis lines=left,xlabel={{{xl}}},ylabel={{{yl}}},label style={{font=\\scriptsize}},title={{{tit}}},title style={{font=\\small}}]\n'
            f'\\addplot[thick,vurgu] coordinates {{{pts}}};\n\\end{{axis}}')
lam12,T12=8,Fr(1,2)
SK=tikz_svg(HEAD+ax_plot(4.6,16,'0,2,4,6,8,10,12,14,16','$x$ (cm)','$y$ (cm)',lambda x:2*cos(2*pi*x/lam12),'Şekil I')+'\n'+ax_plot(0,1.0,'0,0.25,0.5,0.75,1.0','$t$ (s)','$y$ (cm)',lambda t:2*cos(2*pi*t/float(T12)),'Şekil II')+TAIL)
v12=Fr(lam12)/T12; assert v12==16 and 1/T12==2 and lam12*T12==4 and Fr(lam12,2)/T12==8 and Fr(lam12)/(T12/2)==32
card(12,'y–x ve y–t grafiklerinden hız','Hız, y–x grafiğinden λ ve y–t grafiğinden T okunarak v = λ ÷ T ile bulunur.','Tepe–çukur arasını λ ya da T saymak; λ ile T’yi karıştırmak.','orta','grafik',3,'da-grafik','iki grafikten dalga hızı')
q('0012',tipId='da-grafik',tip=TIPLER['da-grafik'],z='orta',alt='Dalga Grafikleri',kaz='Dalga profili ve titreşim grafiklerinden λ ve T’yi okuyarak yayılma hızını hesaplar.',kalip='grafik',
 metin='Dalga leğeninde yayılan periyodik bir su dalgasının t = 0 anındaki profili Şekil I’deki y–x grafiğinde, dalganın doğrultusu üzerindeki bir P noktasındaki su parçacığının düşey yer değiştirmesinin zamanla değişimi ise Şekil II’deki y–t grafiğinde verilmiştir.\nBuna göre, dalganın yayılma hızı kaç cm/s’dir?',
 sekil=SK,dogru=16,yan=[(2,'Dalga hızı yerine frekansı (1 ÷ 0,5 = 2 Hz) yazmış.','dikkat'),(4,'Hızı λ × T = 8 × 0,5 biçiminde çarparak bulmuş.','bilgi'),
  (8,'Şekil I’de bir tepe ile komşu çukur arası uzaklığı (4 cm) dalga boyu sanmış: 4 ÷ 0,5 = 8.','bilgi'),(32,'Şekil II’de bir tepe ile komşu çukur arası süreyi (0,25 s) periyot sanmış: 8 ÷ 0,25 = 32.','bilgi')],
 istenen='Dalganın yayılma hızı (cm/s).',
 ip=['λ’yı hangi grafikten, T’yi hangi grafikten okuyacağını belirle; “ardışık iki tepe” arası değerlere bak.'],
 bilgi=[GR],
 ad=[A('Dalga boyunu oku','Şekil I konuma bağlıdır; ardışık iki tepe arası λ’dır.','Tepeler x = 0 ve x = 8 cm’de → λ = 8 cm'),
     A('Periyodu oku','Şekil II zamana bağlıdır; ardışık iki tepe arası T’dir.','Tepeler t = 0 ve t = 0,5 s’de → T = 0,5 s'),
     A('Hızı hesapla','Dalga bir periyotta bir dalga boyu yol alır.','v = λ ÷ T = 8 ÷ 0,5 = 16 cm/s')],
 puf='λ yalnız y–x grafiğinden, T yalnız y–t grafiğinden okunur; her ikisinde de “ardışık iki tepe” bir tam döngüdür.')
# ===== girişim deseni (tepe / çukur çemberleri) yardımcısı
def pat_fig(d,pts,lu=.62,kmax=3,ex=2.8):
    """eş fazlı kaynaklar S1=(0,0), S2=(d,0) (λ biriminde). pts: (ad,r1,r2,işaret) r'ler λ cinsinden"""
    o=[]; x0,x1,yy=-ex*lu,(d+ex)*lu,3.05*lu
    o.append(f'\\begin{{scope}}\n\\clip ({x0:.3f},{-yy:.3f}) rectangle ({x1:.3f},{yy:.3f});')
    for cx in (0,d):
        for k in range(1,kmax+1):
            o.append(f'\\draw[thick,vurgu] ({cx*lu:.3f},0) circle ({k*lu:.3f});')
        for k in range(0,kmax):
            o.append(f'\\draw[thin,dash pattern=on 2pt off 2pt] ({cx*lu:.3f},0) circle ({(k+.5)*lu:.3f});')
    o.append('\\end{scope}')
    o.append(f'\\draw[thin] ({x0:.3f},{-yy:.3f}) rectangle ({x1:.3f},{yy:.3f});')
    o.append(DOT((0,0),2.4)); o.append(DOT((d*lu,0),2.4)); o.append(N(0,-.28,'S$_1$','below')); o.append(N(d*lu,-.28,'S$_2$','below'))
    coords={}
    for nm,a,b,sg in pts:
        x=(a*a-b*b+d*d)/(2*d); y2=a*a-x*x; assert y2>0,(nm,a,b); y=sg*sqrt(y2); coords[nm]=(x,y)
        o.append(DOT((x*lu,y*lu),2.4)); o.append(N(x*lu+.02,y*lu+(.27 if sg>0 else -.27),nm,'font=\\small'))
    yl=-yy-.35
    o.append(f'\\draw[thick,vurgu] ({x0:.2f},{yl:.2f}) -- ++(.6,0); '+N(x0+.7,yl,'tepe','right,font=\\scriptsize'))
    o.append(f'\\draw[thin,dash pattern=on 2pt off 2pt] ({x0+2.2:.2f},{yl:.2f}) -- ++(.6,0); '+N(x0+2.9,yl,'çukur','right,font=\\scriptsize'))
    return o,coords
def tip(r):  # r (λ cinsinden): tepe = tam sayı, çukur = yarım tam
    r=Fr(r).limit_denominator(100); return 'tepe' if r.denominator==1 else 'çukur'
def tur_(a,b,anti=False):
    dx=abs(Fr(a)-Fr(b)).limit_denominator(100)
    if anti: dx+=Fr(1,2)
    return 'karın' if dx.denominator==1 else 'düğüm'
# ===== 13 orta · tepe-çukur çemberleri, karın–düğüm (öncüllü)
d13=3; pts13=[('P',2,2,1),('R',Fr(3,2),Fr(5,2),-1),('S',3,Fr(5,2),1)]
pts13f=[(n,float(a),float(b),sg) for n,a,b,sg in pts13]
assert [tur_(a,b) for n,a,b,sg in pts13]==['karın','karın','düğüm'] and [tip(a)+'-'+tip(b) for n,a,b,sg in pts13]==['tepe-tepe','çukur-çukur','tepe-çukur']
# faz: Δ=0 → +, Δ=λ → − (ardışık karın çizgileri zıt fazlı); R: r1=1,5 r2=2,5
import cmath
def disp(a,b,t=0): return cos(2*pi*(float(a)-t))+cos(2*pi*(float(b)-t))
assert disp(2,2)>1.99 and disp(Fr(3,2),Fr(5,2))<-1.99 and abs(disp(3,Fr(5,2)))<1e-9
for tt in (.1,.2,.33,.6): assert disp(2,2,tt)*disp(Fr(3,2),Fr(5,2),tt)<0
o,_=pat_fig(d13,pts13f)
SK=tikz(o)
card(13,'Tepe–çukur kesişimlerinde genlik','Tepe–tepe ve çukur–çukur kesişimleri karın, tepe–çukur kesişimleri düğümdür; aynı frekanslı iki noktadan biri tepede diğeri çukurdaysa zıt yönde hareket ederler.','Karın noktalarının hepsinin aynı anda tepede olduğunu sanmak.','orta','şekilli',4,'da-dugum','çemberlerin kesiştiği noktalarda genlik ve faz')
q('0013',tipId='da-dugum',tip=TIPLER['da-dugum'],z='orta',alt='Girişim Deseni',kaz='Dalga leğeninde tepe ve çukur çemberlerinin kesişim noktalarındaki genlik ve titreşim yönünü karşılaştırır.',kalip='şekilli',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, eş fazlı çalışan özdeş S₁ ve S₂ noktasal kaynakları dairesel su dalgaları üretmektedir. Şekilde bir andaki dalga tepeleri sürekli çizgilerle, dalga çukurları kesikli çizgilerle gösterilmiş; P, R ve S noktaları işaretlenmiştir. Dalgaların genliği yayılırken değişmemektedir.\nBuna göre,\nI. P ve R noktalarındaki su parçacıklarının genlikleri eşittir,\nII. S noktasındaki su parçacığının genliği, her bir kaynağın tek başına oluşturduğu dalganın genliğine eşittir,\nIII. P ve R noktalarındaki su parçacıkları her an zıt yönde hareket eder\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Her noktanın hangi iki çemberin üzerinde bulunduğuna bak; sonra iki dalganın aynı anda tepe, çukur ya da farklı durumda olduğuna göre karar ver.'],
 bilgi=[YF],
 ad=[A('Noktaların konumu','Şekildeki çizim stiline göre her noktanın iki kaynağa göre dalga durumu okunur.','P: tepe + tepe · R: çukur + çukur · S: tepe + çukur'),
     A('I ve II','Aynı türden kesişim karın, farklı tür düğümdür.','P ve R karındır → genlikleri eşit (2A) → I doğru · S düğümdür, genliği 0 → II yanlış'),
     A('III. yargı','P’de tepe + tepe, R’de çukur + çukur vardır; ikisi de 2A genlikli ve aynı frekanslı olduğundan bu noktalar aynı anda zıt uçlardadır ve her an zıt yönde hareket eder.','P: +2A, R: −2A → III doğru')],
 puf='Tepe–tepe ve çukur–çukur kesişimleri karındır; genliği ve frekansı aynı olan iki noktadan biri tepede, diğeri çukurdaysa her an zıt yönde hareket ederler.',
 **onc([True,False,True],['P (tepe + tepe) ve R (çukur + çukur) karın noktalarıdır, ikisinin de genliği 2A’dır','S, bir tepe ile bir çukurun kesiştiği düğüm noktasıdır; su parçacığı hareketsiz kalır','P’de tepe + tepe, R’de çukur + çukur olduğundan ikisi de 2A genlikli ve zıt uçtadır; aynı frekansla titreştiklerinden her an zıt yönde hareket ederler'],3))
# ===== 14 zor · çift yarık, P noktası (öncüllü)
d14,L14,y14=Fr(1,4)*Fr(1,1000),Fr(1),Fr(5,1000)
dl14=d14*y14/L14; lam14=dl14/Fr(5,2); assert dl14==Fr(125,10**8) and lam14==Fr(500,10**9)
assert dl14/Fr(625,10**9)==2                                  # 625 nm: tam sayı → aydınlık
assert (2*d14)*y14/L14/lam14==5                               # d iki katı: 5λ → aydınlık
dX14=lam14*L14/d14; assert dX14==Fr(2,1000) and y14/dX14==Fr(5,2)
o=dslit('$d=0{,}25$ mm','$L=1$ m',nb=3,delta=False)
dxu=.5; yp=2.5*dxu; xe=4.6
o.append(DOT((xe,yp),2.2)); o.append(N(xe+.5,yp+.2,'P','right'))
o.append(DM((xe+1.05,0),(xe+1.05,yp))); o.append(N(xe+1.15,yp/2,'$5$ mm','right,font=\\scriptsize'))
SK=tikz(o)
card(14,'P noktasında yol farkı','Ekran üzerindeki yol farkı Δx = d·y/L; karanlık saçak için (n − ½)λ, aydınlık için nλ.','Karanlık saçak sırasını yol farkına yanlış çevirmek (3. karanlık için 3,5λ ya da 3λ yazmak).','zor','şekilli',5,'da-cift','P noktasının saçak türü ve λ')
q('0014',tipId='da-cift',tip=TIPLER['da-cift'],z='zor',alt='Çift Yarıkta Girişim',kaz='Çift yarık düzeneğinde bir noktadaki yol farkından dalga boyunu bulur ve düzenek değişince noktanın saçak türünü belirler.',kalip='şekilli',
 metin='Tek renkli ışıkla yapılan çift yarık deneyinde ekranda oluşan aydınlık saçaklar şekilde işaretlenmiştir. O merkezî aydınlık saçaktır; P noktası, O’dan 5 mm uzaklıktadır. Yarıklar arası uzaklık ve yarıklar düzleminden ekrana olan uzaklık şekilde verilmiştir. Aşağıdaki değişikliklerde yalnız belirtilen nicelik değiştirilmekte, P noktasının ekran üzerindeki konumu aynı alınmaktadır.\nBuna göre,\nI. deneyde kullanılan ışığın dalga boyu 500 nm’dir,\nII. dalga boyu 625 nm olan ışık kullanılırsa P noktasında karanlık saçak oluşur,\nIII. yarıklar arası uzaklık iki katına çıkarılırsa P noktasında aydınlık saçak oluşur\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['P noktasının saçak sırasını şekilden bul, bu noktadaki yol farkını geometriyle hesapla ve her değişiklikte yol farkını dalga boyuyla oranla.'],
 bilgi=[CY],
 ad=[A('P’nin saçak sırası','Ardışık aydınlık saçaklar arasındaki karanlık saçaklar sırayla sayılır; P iki aydınlık saçağın arasında üçüncü karanlık bölgededir.','3. karanlık saçak → Δx = 2,5 × λ'),
     A('Yol farkını hesapla','Ekran üzerinde yol farkı Δx = d × y ÷ L.','Δx = (0,25 × 10⁻³ × 5 × 10⁻³) ÷ 1 = 1250 nm'),
     A('I. yargı','Δx = 2,5 × λ koşulundan dalga boyu bulunur.','λ = 1250 ÷ 2,5 = 500 nm → I doğru'),
     A('II. yargı','Yol farkı aynı kalır (1250 nm); yeni dalga boyuyla oranlanır.','1250 ÷ 625 = 2 (tam sayı) → aydınlık → II yanlış'),
     A('III. yargı','d iki katı olunca yol farkı da iki katı olur.','Δx′ = 2500 nm = 5 × 500 nm → aydınlık → III doğru')],
 puf='Çift yarıkta bir noktadaki saçak türünü yol farkı ÷ λ oranı belirler: tam sayı aydınlık, yarım katlı karanlık.',
 **onc([True,False,True],['yol farkı Δx = 2,5 × λ olduğundan λ = 1250 ÷ 2,5 = 500 nm’dir','yol farkı 1250 nm’dir ve 625 nm’nin tam 2 katı olduğundan P’de aydınlık saçak oluşur','d iki katına çıkınca Δx = 2500 nm = 5 × 500 nm olur ve P aydınlık saçaktır'],2))
# ===== 15 orta · eğik geçiş, dalga boyu
th1,th2=radians(53),radians(37); l2_15,f15=3,4
v2=l2_15*f15; s53,s37=Fr(4,5),Fr(3,5)
v1=Fr(v2)*s53/s37; l1_15=v1/f15
assert v2==12 and v1==16 and l1_15==4 and abs(sin(th1)-.8)<.005 and abs(sin(th2)-.6)<.005
assert Fr(l2_15)*s37/s53==Fr(9,4) and v2==12 and v1==16
sc=.3; sp=float(l1_15)*sc/.8; assert abs(sp-float(l2_15)*sc/.6)<1e-9
xc=2.3; o=[D((0,0),(5.0,0),'very thick'),D((xc,-1.9),(xc,1.9),'thin,dashed')]
for n in range(0,4):
    xn=.2+n*sp
    o.append(D((xn,0),(xn+1.5*cos(th1),1.5*sin(th1)),'thick,vurgu'))
    o.append(D((xn,0),(xn-1.4*cos(th2),-1.4*sin(th2)),'thick,vurgu'))
o.append(AR((xc-1.5*sin(th1),1.5*cos(th1)),(xc,0),'thin')); o.append(AR((xc,0),(xc+1.3*sin(th2),-1.3*cos(th2)),'thin'))
o.append(f'\\draw[thin] ({xc:.2f},.55) arc[start angle=90,end angle=143,radius=.55]'+';'); o.append(N(xc-.55,.85,'$53^\\circ$','font=\\scriptsize'))
o.append(f'\\draw[thin] ({xc:.2f},-.55) arc[start angle=-90,end angle=-53,radius=.55]'+';'); o.append(N(xc+.55,-.85,'$37^\\circ$','font=\\scriptsize'))
o.append(N(4.9,1.6,'derin','left,font=\\scriptsize')); o.append(N(4.9,-1.6,'sığ','left,font=\\scriptsize'))
SK=tikz(o)
card(15,'Eğik geçişte dalga boyu','sinθ₁ ÷ sinθ₂ = λ₁ ÷ λ₂; frekans ortam değişince sabit kalır.','Frekansın değiştiğini ya da dalga boyunu hız sanarak karıştırmak; oranı ters kurmak.','orta','şekilli',4,'da-kirilma','eğik geçiş, açılardan λ')
q('0015',tipId='da-kirilma',tip=TIPLER['da-kirilma'],z='orta',alt='Dalga Leğeninde Kırılma',kaz='Dalga leğeninde derin ortamdan sığ ortama eğik geçen dalganın dalga boyunu açı oranından hesaplar.',kalip='şekilli',
 metin='Derinliği iki farklı bölgeden oluşan bir dalga leğeninde derin bölgeden sığ bölgeye geçen periyodik su dalgalarının cepheleri ve ışın doğrultuları şekilde gösterilmiştir. Işın doğrultularının sınıra çizilen normalle yaptığı açılar şekilde verilmiştir. Sığ bölgede dalgaların frekansı 4 Hz, dalga boyu 3 cm’dir.\n(sin 53° = 0,8; sin 37° = 0,6)\nBuna göre, derin bölgedeki dalga boyu kaç cm’dir?',
 sekil=SK,dogru=4,yan=[(Fr(9,4),'Açıların sinüs oranını ters kurmuş: 3 × 0,6 ÷ 0,8 = 2,25 cm.','islem'),(3,'Dalga boyunun ortam değiştirirken değişmediğini düşünmüş.','bilgi'),
  (12,'Sığ bölgedeki dalga hızını (3 × 4 = 12 cm/s) dalga boyu olarak yazmış.','dikkat'),(16,'Derin bölgedeki dalga hızını (16 cm/s) bulup dalga boyuna çevirmeyi unutmuş.','dikkat')],
 istenen='Derin bölgedeki dalga boyu (cm).',
 ip=['Ortam değiştiren dalgada sabit kalan niceliği kullanarak önce sığ bölgedeki hızı bul; sonra açı oranını hıza uygula.'],
 bilgi=[KL],
 ad=[A('Sığ bölge hızı','Hız dalga boyu ile frekansın çarpımıdır.','v₂ = λ₂ × f = 3 × 4 = 12 cm/s'),
     A('Derin bölge hızı','Kırılmada sinüs oranı hız oranına eşittir.','v₁ ÷ v₂ = sin53° ÷ sin37° = 0,8 ÷ 0,6 → v₁ = 12 × 4/3 = 16 cm/s'),
     A('Derin bölge dalga boyu','Frekans iki bölgede de 4 Hz’dir.','λ₁ = v₁ ÷ f = 16 ÷ 4 = 4 cm')],
 puf='Dalga ortam değiştirince frekans sabit kalır; λ₁ ÷ λ₂ = v₁ ÷ v₂ = sinθ₁ ÷ sinθ₂ (θ normalle yapılan açı).')
# ===== 16 zor · zıt fazlı kaynaklar, tablo (öncüllü)
lam16=4; d16=12
nok=[('K',9,7),('L',15,7),('M',6,12)]
for n,a,b in nok: assert abs(a-b)<=d16<=a+b
tr=lambda a,b:tur_(Fr(abs(a-b),lam16),0,anti=True)
assert [tr(a,b) for n,a,b in nok]==['karın','düğüm','karın']       # zıt fazlı kaynaklar
assert [tur_(Fr(abs(a-b),lam16),0) for n,a,b in nok]==['düğüm','karın','düğüm']   # eş fazlı olsaydı
SK=tablo_svg(['Nokta','S1’e uzaklık (cm)','S2’ye uzaklık (cm)'],[[n,str(a),str(b)] for n,a,b in nok])
card(16,'Zıt fazlı kaynaklarda girişim','Kaynaklar zıt fazlıysa karın koşulu (n + ½)λ, düğüm koşulu nλ olur.','Eş fazlı kaynak koşullarını zıt fazlı durumda da kullanmak.','zor','tablo',5,'da-dugum','zıt fazlı kaynaklar, tablodaki uzaklıklar')
q('0016',tipId='da-dugum',tip=TIPLER['da-dugum'],z='zor',alt='Girişim Deseni',kaz='Zıt fazlı iki kaynağın girişiminde noktaların karın ya da düğüm olduğunu yol farkından belirler.',kalip='tablo',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, aralarındaki uzaklık 12 cm olan özdeş S₁ ve S₂ noktasal kaynakları dalga boyu 4 cm olan dairesel su dalgaları üretmektedir. Kaynaklar zıt fazlıdır; yani S₁ dalga tepesi üretirken S₂ dalga çukuru üretmektedir. Dalgaların genliği yayılırken değişmemekte ve her kaynağın tek başına oluşturduğu dalganın genliği A’dır. K, L ve M noktalarının kaynaklara uzaklıkları tabloda verilmiştir.\nBuna göre,\nI. K noktasındaki su parçacığı titreşim yapmaz,\nII. L noktasındaki su parçacığının genliği 2A’dır,\nIII. M noktasındaki su parçacığının genliği K noktasındakine eşittir\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargı.',
 ip=['Her noktanın yol farkını dalga boyuyla oranla; kaynakların zıt fazlı olmasının karın ve düğüm koşullarını nasıl etkilediğini düşün.'],
 bilgi=[YF],
 ad=[A('Yol farkları','Her nokta için iki uzaklığın farkı alınır.','K: 9 − 7 = 2 cm · L: 15 − 7 = 8 cm · M: 12 − 6 = 6 cm'),
     A('Oranlar','Yol farkı dalga boyuna oranlanır.','K: 2 ÷ 4 = 0,5 · L: 8 ÷ 4 = 2 · M: 6 ÷ 4 = 1,5'),
     A('Zıt fazlı kaynak koşulu','Başlangıç fazı farkı yarım dalga boyu kadar yol farkı gibi davranır: tam sayı oranı düğüm, yarım katlı oran karın verir.','K: karın (2A) · L: düğüm (0) · M: karın (2A)'),
     A('Yargılar','I yanlış (K karın), II yanlış (L düğüm), III doğru (ikisi de 2A).','Yalnız III doğru')],
 puf='Kaynaklar zıt fazlıysa eş fazlı durumun tersi olur: yol farkı nλ ise düğüm, (n + ½)λ ise karın.',
 **onc([False,False,True],['K noktasının yol farkı 0,5λ’dır; zıt fazlı kaynaklarda bu karın koşuludur ve genlik 2A’dır','L noktasının yol farkı 2λ’dır; zıt fazlı kaynaklarda bu düğüm koşuludur ve genlik 0’dır','K ve M noktalarının ikisi de karındır ve genlikleri 2A’dır'],0))
# ===== 17 orta · tek yarık, iki deney
w1,(l1,a1,L1)=8,(500,Fr(1,4),Fr(2)); l2,a2,L2=750,Fr(1,8),Fr(3,2)
fac=lambda lr,ar,Lr:Fr(w1)*lr*Lr/ar
lr,ar_,Lr_=Fr(l2,l1),a2/a1,L2/L1
assert (lr,ar_,Lr_)==(Fr(3,2),Fr(1,2),Fr(3,4))
assert fac(lr,ar_,Lr_)==18 and fac(lr,ar_,1)==24 and fac(1,ar_,Lr_)==12 and fac(1/lr,ar_,Lr_)==8 and fac(lr,1,Lr_)==9
o=['\\begin{scope}[scale=.95]']
o+=tekfig(.5,'$L=2$ m','$0{,}25$ mm',w=.5,pw=1.1,xe=3.2,sx=0)
o.append(DM((3.2-.35,-.5),(3.2-.35,.5))); o.append(N(3.2-.42,0,'8 mm','left,font=\\scriptsize'))
o.append(N(1.6,2.2,'Şekil I: $\\lambda=500$ nm','font=\\scriptsize'))
o+=tekfig(.3,'$L=1{,}5$ m','$0{,}125$ mm',w=.42,pw=1.1,xe=3.4,sx=6.7)
o.append(DM((6.7+3.4-.35,-.42),(6.7+3.4-.35,.42))); o.append(N(6.7+3.4-.42,0,'$w$','left,font=\\scriptsize'))
o.append(N(8.4,2.2,'Şekil II: $\\lambda=750$ nm','font=\\scriptsize'))
o.append('\\end{scope}')
SK=tikz(o)
card(17,'İki tek yarık deneyini karşılaştırma','w ∝ λ·L/a oranlarıyla ikinci deneyin merkezî saçak genişliği bulunur.','Yarık genişliğinin oranını ters kurmak; ekran uzaklığını ya da dalga boyunu atlamak.','orta','şekilli',4,'da-tek','iki deneyde w oranı')
q('0017',tipId='da-tek',tip=TIPLER['da-tek'],z='orta',alt='Tek Yarıkta Kırınım',kaz='Tek yarıkta merkezî aydınlık saçak genişliğinin λ, L ve a ile orantısını kullanarak ikinci deneyde saçak genişliğini hesaplar.',kalip='şekilli',
 metin='Tek renkli ışıkla iki ayrı tek yarık kırınım deneyi yapılıyor. Her deneyde kullanılan ışığın dalga boyu, yarık genişliği ve yarıktan ekrana olan uzaklık şekillerde verilmiştir. Şekil I’deki deneyde ekranda oluşan merkezî aydınlık saçağın genişliği 8 mm olarak ölçülmüştür.\nBuna göre, Şekil II’deki deneyde oluşan merkezî aydınlık saçağın genişliği w kaç mm’dir?',
 sekil=SK,dogru=18,yan=[(8,'Dalga boyu oranını ters kurmuş: saçak genişliğini λ ile ters orantılı saymış (8 × 2/3 × 2 × 3/4 = 8).','bilgi'),(9,'Yarık genişliğinin değişimini hesaba katmamış; yalnız λ ve L oranlarını uygulamış (8 × 3/2 × 3/4 = 9).','dikkat'),
  (12,'Dalga boyunun değişimini atlamış; yalnız a ve L oranlarını uygulamış (8 × 2 × 3/4 = 12).','dikkat'),(24,'Ekran uzaklığının değişimini hesaba katmamış; yalnız λ ve a oranlarını uygulamış (8 × 3/2 × 2 = 24).','dikkat')],
 istenen='Şekil II’deki merkezî aydınlık saçağın genişliği (mm).',
 ip=['Merkezî saçak genişliğinin λ, L ve a ile nasıl orantılı olduğunu yaz; ikinci deneyin her niceliğini birinciye oranla.'],
 bilgi=[TY],
 ad=[A('Orantıyı yaz','Merkezî saçak genişliği doğru ve ters orantı terimlerine bağlıdır.','w ∝ λ × L ÷ a'),
     A('Oranları bul','İkinci deneyin değerleri birinciye bölünür.','λ: 750 ÷ 500 = 3/2 · L: 1,5 ÷ 2 = 3/4 · a: 0,125 ÷ 0,25 = 1/2'),
     A('Genişlik oranı','a ters orantılı olduğundan 2 çarpanı gelir.','w₂ ÷ w₁ = (3/2) × (3/4) ÷ (1/2) = 9/4'),
     A('Sonuç','Birinci deneydeki genişlikle çarpılır.','w₂ = 8 × 9/4 = 18 mm')],
 puf='Orantılı büyüklüklerde her niceliğin değişim oranını ayrı yaz; ters orantılı olanın oranını ters çevirmeyi unutma.')
# ===== 18 zor · S2 ters fazlı yapılırsa (öncüllü)
d18=Fr(5,2); pts18=[('K',2,Fr(5,2),-1),('L',2,2,1),('M',3,2,1)]
pts18f=[(n,float(a),float(b),sg) for n,a,b,sg in pts18]
once=[tur_(a,b) for n,a,b,sg in pts18]; sonra=[tur_(a,b,anti=True) for n,a,b,sg in pts18]
assert once==['düğüm','karın','karın'] and sonra==['karın','düğüm','düğüm']
o,_=pat_fig(float(d18),pts18f)
SK=tikz(o)
card(18,'Kaynağın fazı değişince desen','S₂ ters fazlı yapılırsa karın ve düğüm koşulları yer değiştirir.','Faz değişimini yok sayıp noktaların türünün aynı kaldığını düşünmek.','zor','şekilli',5,'da-dugum','eş fazlı desenden zıt fazlıya geçiş')
q('0018',tipId='da-dugum',tip=TIPLER['da-dugum'],z='zor',alt='Girişim Deseni',kaz='Kaynaklardan birinin fazı değiştirildiğinde seçilen noktaların genliklerinin nasıl değiştiğini yorumlar.',kalip='şekilli',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, eş fazlı çalışan özdeş S₁ ve S₂ noktasal kaynakları dairesel su dalgaları üretmektedir. Şekilde bu eş fazlı çalışma sırasında bir andaki dalga tepeleri sürekli çizgilerle, dalga çukurları kesikli çizgilerle gösterilmiştir. Daha sonra S₂ kaynağının fazı, S₁’e göre ters (zıt fazlı) olacak biçimde değiştiriliyor; frekans, genlik ve kaynakların konumu aynı kalıyor.\nBu değişiklikten sonra,\nI. K noktasındaki su parçacığının genliği, değişiklikten önceki genliğinden büyük olur,\nII. L noktasındaki su parçacığı titreşim yapmaz,\nIII. M noktasındaki su parçacığının genliği L noktasındakine eşit olur\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru olan yargılar.',
 ip=['Önce her noktanın şekildeki eş fazlı durumda karın mı düğüm mü olduğunu bul; sonra zıt fazlı kaynakta bu koşulların nasıl değiştiğini düşün.'],
 bilgi=[YF],
 ad=[A('Eş fazlı durum','K: çukur + tepe (düğüm) · L: tepe + tepe (karın) · M: tepe + tepe (karın) — yol farkları sırasıyla 0,5λ, 0, 1λ.','K düğüm · L karın · M karın'),
     A('Zıt fazlı durum','S₂ ters fazlı olunca karın koşulu (n + ½)λ, düğüm koşulu nλ olur.','K: 0,5λ → karın · L: 0 → düğüm · M: 1λ → düğüm'),
     A('Yargılar','K’nin genliği 0’dan 2A’ya çıkar, L ve M hareketsiz kalır.','I doğru · II doğru · III doğru (ikisinin de genliği 0)')],
 puf='Bir kaynağın fazı ters çevrilince karınlar düğüme, düğümler karına dönüşür; yol farkı koşulları yer değiştirir.',
 **onc([True,True,True],['K noktası değişiklikten önce düğümdür; değişiklikten sonra yol farkı 0,5λ olduğundan karın olur ve genliği 2A’dır','L noktasının yol farkı sıfırdır; zıt fazlı kaynaklarda bu düğüm koşuludur','L ve M’nin yol farkları (0 ve 1λ) tam sayı katlı olduğundan ikisi de düğüm olur ve genlikleri sıfırdır'],4))
# ===== 19 zor · zıt fazlı kaynaklar, frekans değişimi, düğüm noktası sayısı
v19,f19,f19b,d19=20,5,10,12
def noktalar(v,f,d,anti=True,kaynak=False,merkez=True):
    lam=Fr(v,f); n=0; k=0 if anti else Fr(1,2)
    # düğüm: zıt fazlıda Δx = kλ → merkezden x = kλ/2 ; eş fazlıda Δx = (k+½)λ
    xs=[]; 
    while True:
        x=(k)*lam/2 if anti else k*lam/2
        if x>Fr(d,2) or (x==Fr(d,2) and not kaynak): break
        xs.append(x); k+=1
    sayi=sum(1 if x==0 else 2 for x in xs)
    if not merkez: sayi-=1
    return sayi
assert noktalar(v19,f19b,d19)==11 and noktalar(v19,f19,d19)==5 and noktalar(v19,f19b,d19,anti=False)==12 and noktalar(v19,f19b,d19,kaynak=True)==13 and noktalar(v19,f19b,d19,merkez=False)==10
card(19,'Zıt fazlı kaynaklarda düğüm noktası','Zıt fazlı kaynaklarda düğüm koşulu Δx = nλ’dır (merkez noktası dâhil); ardışık düğüm noktaları λ/2 arayla dizilir.','Eş fazlı koşulu kullanmak; kaynak noktalarını ya da merkezi saymada hata yapmak.','zor','hikâyeli',5,'da-dugum','zıt fazlı kaynaklar arasındaki doğruda düğüm sayısı')
q('0019',tipId='da-dugum',tip=TIPLER['da-dugum'],z='zor',alt='Girişim Deseni',kaz='Zıt fazlı iki kaynağın hız ve frekansından dalga boyunu bulup kaynakları birleştiren doğru üzerindeki düğüm noktası sayısını belirler.',kalip='hikâyeli',
 metin='Bir laboratuvarda, derinliği her yerde aynı olan bir dalga leğeninde aralarındaki uzaklık 12 cm olan özdeş S₁ ve S₂ noktasal kaynakları zıt fazlı çalıştırılıyor; yani S₁ dalga tepesi üretirken S₂ dalga çukuru üretmektedir. Kaynaklar 5 Hz frekansla titreştirilerek girişim deseni elde ediliyor; leğendeki su dalgalarının yayılma hızı 20 cm/s’dir. Daha sonra su derinliği değiştirilmeden kaynakların frekansı 10 Hz’e çıkarılıyor.\nBuna göre, frekans 10 Hz iken S₁ ile S₂ arasındaki doğru parçası üzerinde (kaynakların bulunduğu noktalar dışında) genliğin sıfır olduğu kaç nokta vardır?',
 sekil=None,dogru=11,yan=[(5,'Frekansın değişiminin düğüm sayısını etkilemediğini düşünüp ilk durumdaki 5 noktayı yazmış.','bilgi'),(10,'Doğru parçasının tam ortasındaki noktanın (yol farkı sıfır) zıt fazlı kaynaklarda da düğüm olduğunu görememiş; yalnız ±1, ±2, …, ±5 cm noktalarını saymış.','dikkat'),
  (12,'Kaynakları eş fazlı gibi düşünüp düğüm koşulunu (n + ½) × λ almış; merkezin iki yanındaki 0,5; 1,5; …; 5,5 cm noktalarını (6 + 6) saymış.','bilgi'),(13,'Kaynakların bulunduğu noktaları da (yol farkı 12 cm = 6 × λ) düğüm olarak sayıp 11 + 2 = 13 bulmuş.','dikkat')],
 istenen='Frekans 10 Hz iken doğru parçası üzerindeki düğüm noktası sayısı.',
 ip=['Yeni dalga boyunu bul; zıt fazlı kaynaklarda yol farkının hangi değerlerinde dalgaların birbirini yok ettiğini düşün ve merkezden başlayarak say.'],
 bilgi=[DG,B('Dalga boyu','v = λ × f; derinlik sabitse v değişmez. Örnek: v = 30 cm/s ve f = 6 Hz ise λ = 5 cm')],
 ad=[A('Yeni dalga boyu','Derinlik değişmediği için hız sabittir.','λ′ = v ÷ f′ = 20 ÷ 10 = 2 cm'),
     A('Düğüm koşulu','Kaynaklar zıt fazlı olduğundan iki dalga yol farkı tam sayı katlı olan noktalarda birbirini yok eder.','Δx = n × λ′ = 0, 2, 4, … cm'),
     A('Konumları bul','Doğru parçası üzerinde merkezden x uzaklıktaki noktanın yol farkı 2x’tir.','x = n × λ′ ÷ 2 = 0, 1, 2, 3, 4, 5 cm (6 cm kaynağın konumudur)'),
     A('Say','Merkez noktası bir, diğerleri iki yanda ikişer tanedir.','1 + 5 × 2 = 11 nokta')],
 puf='Zıt fazlı kaynaklarda koşullar eş fazlının tersidir: yol farkı nλ olan noktalar düğümdür; kaynaklar arası doğruda merkez de dâhil sayılır.')
# ===== 20 orta · kavram
card(20,'Girişim deseni özellikleri','Frekans artınca λ küçülür ve düğüm çizgileri birbirine yaklaşır; karın noktalar da titreşir.','Karın noktalarının hareketsiz olduğunu ya da merkez doğrusunun düğüm olduğunu sanmak.','orta','düz',2,'da-dugum','girişim deseni için doğru yargı')
q('0020',tipId='da-dugum',tip=TIPLER['da-dugum'],z='orta',alt='Girişim Deseni',kaz='Su dalgalarında girişim deseninin özelliklerini kaynak niceliklerinin değişimiyle ilişkilendirir.',kalip='düz',
 metin='Derinliği her yerde aynı olan bir dalga leğeninde, eş fazlı çalışan özdeş iki noktasal kaynakla girişim deseni elde ediliyor. Kaynaklar aynı frekansta ve aynı genlikte titreşmektedir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=None,dogru='Kaynakların frekansı artırılırsa ardışık düğüm çizgileri birbirine yaklaşır.',
 yan=[('Karın çizgileri üzerindeki noktalar hiçbir zaman denge konumundan geçmez.','Karın noktasının sürekli yüksekte kaldığını düşünmüş; oysa bu noktalar da denge konumu etrafında titreşir.','bilgi'),
      ('Kaynakların genliği artırılırsa düğüm çizgileri üzerindeki noktalar da titreşmeye başlar.','Genlik artınca düğümlerin de hareket edeceğini sanmış; oysa iki dalga her zaman birbirini yok eder ve genlik sıfır kalır.','bilgi'),
      ('Kaynaklar arasındaki uzaklık değiştirilirse merkez doğrusu düğüm çizgisi olabilir.','Merkez doğrusunun türünün kaynak aralığına bağlı olduğunu düşünmüş; oysa eş fazlı kaynaklarda merkez doğrusu daima karındır.','bilgi'),
      ('Merkez doğrusu üzerindeki noktalar kaynaklara eşit uzaklıkta olduğundan düğüm noktasıdır.','Eşit uzaklığı yok olma sanmış; yol farkı sıfırdır ve dalgalar aynı fazda toplanarak genliği 2A yapar.','bilgi')],
 sira=['Karın çizgileri üzerindeki noktalar hiçbir zaman denge konumundan geçmez.','Kaynakların genliği artırılırsa düğüm çizgileri üzerindeki noktalar da titreşmeye başlar.','Kaynaklar arasındaki uzaklık değiştirilirse merkez doğrusu düğüm çizgisi olabilir.','Merkez doğrusu üzerindeki noktalar kaynaklara eşit uzaklıkta olduğundan düğüm noktasıdır.','Kaynakların frekansı artırılırsa ardışık düğüm çizgileri birbirine yaklaşır.'],
 istenen='Girişim deseni için doğru ifade.',
 ip=['Her seçenekte karın ve düğüm koşulunu yol farkı ile frekansın dalga boyuna etkisi üzerinden sına.'],
 bilgi=[YF,DG],
 ad=[A('Yol farkı koşulları','Merkez doğrusunda yol farkı sıfırdır (karın); düğümlerde yol farkı (n + ½)λ’dır.','Merkez doğrusu: karın'),
     A('Genlik ve frekans','Düğüm noktasında genlik sıfırdır; frekans artınca λ küçülür.','f ↑ → λ ↓ → düğüm çizgileri sıklaşır'),
     A('Seçenekleri ele','Karın noktaları titreşir; düğümler titreşmez; merkez daima karındır.','Yalnızca “frekans artınca düğüm çizgileri yaklaşır” doğrudur')],
 puf='Eş fazlı kaynaklarda merkez doğrusu karındır; frekans artınca λ küçülür, düğüm çizgileri birbirine yaklaşır.')
# ===== yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/dalga'
P.yaz(os.path.join(GD,'dalga-1.json'),os.path.join(SC,'bos-dalga.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Dalga Mekaniği'))['kartlar'].append(c['id'])
json.dump(dict(konu='Dalga Mekaniği',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2020–2026 Fizik (yalnız mantık), 345 AYT Fizik, Bilgi Sarmal AYT Fizik, MEB 11–12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afdalga.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
