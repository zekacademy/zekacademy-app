"""TYT Geometri · Eşkenar Üçgen (hafif mod; kardeş yok, ipucu 1). Koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap/çeldirici assert."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
P=Parti('eskenarucgen','Eşkenar Üçgen','geo|Eşkenar Üçgen',ders='TYT Geometri',idon='tytgeo')
TIPK={}   # tipId -> uygulama konu anahtarı
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)

# ---------------- çizim yardımcıları (cm cinsinden koordinatlar) ----------------
def add(p,q_): return (p[0]+q_[0],p[1]+q_[1])
def sub(p,q_): return (p[0]-q_[0],p[1]-q_[1])
def mul(p,s): return (p[0]*s,p[1]*s)
def ln(p): return math.hypot(*p)
def un(p): n=ln(p); return (p[0]/n,p[1]/n)
def mid(p,q_): return ((p[0]+q_[0])/2,(p[1]+q_[1])/2)
def lerp(p,q_,t): return (p[0]+(q_[0]-p[0])*t,p[1]+(q_[1]-p[1])*t)
def dist(p,q_): return ln(sub(p,q_))
def cen(ps): return (sum(p[0] for p in ps)/len(ps),sum(p[1] for p in ps)/len(ps))
def pt(p): return f'({p[0]:.3f},{p[1]:.3f})'
def ang(V,a,b):
    u=sub(a,V); v=sub(b,V); return degrees(math.acos((u[0]*v[0]+u[1]*v[1])/(ln(u)*ln(v))))
def alan(ps): return abs(sum(ps[i][0]*ps[(i+1)%len(ps)][1]-ps[(i+1)%len(ps)][0]*ps[i][1] for i in range(len(ps))))/2
class F:
    def __init__(s): s.o=[]
    def raw(s,t): s.o.append(t)
    def line(s,p,q_,st=''): s.o.append(f'\\draw[{st}] {pt(p)} -- {pt(q_)};')
    def poly(s,ps,st=''): s.o.append(f'\\draw[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def fill(s,ps,st='fill=vurgu!25'): s.o.append(f'\\fill[{st}] '+' -- '.join(map(pt,ps))+' -- cycle;')
    def node(s,p,t,st=''): s.o.append(f'\\node[{st}] at {pt(p)} {{{t}}};')
    def vl(s,t,p,dv,d=.3): s.node(add(p,mul(un(dv),d)),f'${t}$')       # köşe harfi: dv yönünde dışarıda
    def sl(s,t,p,q_,ic,d=.3):                                           # kenar uzunluğu: kenar ortasında, ic noktasının tersi tarafta
        m=mid(p,q_); e=un(sub(q_,p)); n=(-e[1],e[0])
        if n[0]*(m[0]-ic[0])+n[1]*(m[1]-ic[1])<0: n=(-n[0],-n[1])
        s.node(add(m,mul(n,d)),t)
    def arc(s,V,a,b,r,lab=None,lr=None,st=''):
        a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180
        s.o.append(f'\\draw[{st}] ({V[0]+r*cos(radians(a1)):.3f},{V[1]+r*sin(radians(a1)):.3f}) arc[start angle={a1:.2f},delta angle={d:.2f},radius={r}];')
        if lab: m=radians(a1+d/2); s.node((V[0]+lr*cos(m),V[1]+lr*sin(m)),lab)
    def dik(s,V,a,b,z=.22): u=un(sub(a,V)); v=un(sub(b,V)); s.o.append(f'\\draw {pt(add(V,mul(u,z)))} -- {pt(add(add(V,mul(u,z)),mul(v,z)))} -- {pt(add(V,mul(v,z)))};')
    def tick(s,p,q_,n=1,h=.09):
        m=mid(p,q_); e=un(sub(q_,p)); nn=(-e[1],e[0])
        for i in range(n):
            c=add(m,mul(e,(i-(n-1)/2)*.1)); s.line(add(c,mul(nn,h)),sub(c,mul(nn,h)))
    def par(s,p,q_):
        m=mid(p,q_); e=un(sub(q_,p)); s.o.append(f'\\draw[-{{Stealth[length=1.9mm,width=1.7mm]}}] {pt(sub(m,mul(e,.07)))} -- {pt(add(m,mul(e,.07)))};')
    def body(s): return '\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+'\n'.join(s.o)+'\n\\end{tikzpicture}'
    def svg(s): return tikz_svg(s.body())


def rk(a,b=1):
    """a√b biçimi (tam sayı çifti); b kareden arınmış olmalı. -> (metin, değer)"""
    assert a>0 and b>0 and all(b%(d*d) for d in range(2,int(b**.5)+2) if d*d<=b),(a,b)
    return (str(a) if b==1 else (f'{a}√{b}' if a!=1 else f'√{b}')), a*math.sqrt(b)
def kare_esit(a,b,n,d=1):
    """(a√b)² = a²b == n/d (tam sayı/Fraction kanıtı)"""
    from fractions import Fraction as Fr
    assert Fr(a*a*b)==Fr(n,d),(a,b,n,d)
def qk(no,ad,dogru,yan,**k):
    """kök içeren şıklı soru: dogru=(a,b), yan=[((a,b),cel,tur)]; şıklar değere göre sıralanır"""
    D=rk(*dogru); Y=[(rk(*v),c,t) for v,c,t in yan]
    vals=[D[1]]+[y[0][1] for y in Y]; assert len(set(round(v,9) for v in vals))==5
    sira=[s for s,_ in sorted([D]+[y[0] for y in Y],key=lambda x:x[1])]
    q(no,ad,dogru=D[0],yan=[(y[0][0],y[1],y[2]) for y in Y],sira=sira,**k)
def bitir_geo():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'eskenarucgen-1.json'),'/tmp/bos-eskenarucgen.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu='Eşkenar Üçgen',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','eskenarucgen.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))

EKN=B('Eşkenar üçgen','üç kenarı da eşit, her iç açısı 60° olan üçgendir. Kenarı a ise yüksekliği h = a√3 ÷ 2, alanı a² × √3 ÷ 4 dür. Örnek: a = 4 için h = 2√3 ve alan 4√3’tür')
VIV=B('İç noktadan kenarlara uzaklıklar','eşkenar üçgenin içindeki bir noktadan üç kenara olan dik uzaklıkların toplamı, üçgenin yüksekliğine eşittir (üçgen üç küçük üçgene bölünüp alanlar toplanır). Örnek: kenarı 8 olan eşkenar üçgende bu toplam 4√3’tür')
BENZ=B('Eşkenar üçgenlerle bölünme','kenarlara paralel doğrularla bölünen eşkenar üçgende parçalar da eşkenardır; kenarı k kat küçük üçgenin alanı büyüğün alanının 1/k² sidir. Örnek: kenarı 6 olan eşkenar üçgen, kenarları ikiye bölünerek 4 eş üçgene ayrılırsa her birinin alanı 9√3 ÷ 4 dür')
KAREUC=B('Kare ve eşkenar üçgen','karenin dört kenarı eşittir; ortak bir kenara çizilen eşkenar üçgenin kenarı karenin kenarına eşit olduğundan oluşan üçgenler ikizkenardır. Örnek: tepe açısı 30° olan ikizkenar üçgende taban açıları 75°’dir')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Örnek: dik kenarları 6 ve 8 olan üçgende hipotenüs 10’dur. Eşkenar üçgende yükseklik tabanı ortalar')

# =================== 01 · yükseklik · kolay · hikâyeli ===================
konu('geo|Eşkenar Üçgen','Eşkenar Üçgen')
kartla('K-GEU-01','Eşkenar üçgenin yüksekliği','Yükseklik tabanı ortalar; 30°-60°-90° üçgenden h = a√3/2 bulunur.','Yüksekliği kenara ya da yarım kenara eşitlemek; √3 yerine √2 almak; kenarı √3 ile çarpmak.','kolay',2,'ge-eu-yukseklik','Eşkenar üçgende yükseklik',kalip='hikâyeli')
a1=8; kare_esit(4,3,a1*a1*3,4)       # (4√3)^2 = 48 = 64*3/4
s=.55; B1=(0,0); C1=(a1*s,0); A1=(a1*s/2,a1*s*sqrt(3)/2); D1=(a1*s/2,0)
assert abs(dist(A1,B1)-dist(B1,C1))<1e-9 and abs(dist(A1,C1)-dist(B1,C1))<1e-9 and abs(dist(A1,D1)/s-4*sqrt(3))<1e-9
f=F(); f.poly([A1,B1,C1]); f.line(A1,D1,'dashed'); f.dik(D1,A1,C1,.2); f.tick(A1,B1); f.tick(A1,C1); f.tick(B1,C1)
f.sl('$8$',B1,C1,A1,.4); f.node((A1[0]+.25,A1[1]/2),'$x$')
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(-1,-.6),.3); f.vl('C',C1,(1,-.6),.3); f.vl('D',D1,(-.9,.6),.3)
SK1=f.svg()
qk('0001',[A('Dik üçgeni belirle','Eşkenar üçgende yükseklik tabanı ortalar; ABD yarım eşkenar (30°-60°-90°) üçgendir.','|BD| = 8 ÷ 2 = 4 · hipotenüs |AB| = 8'),A('Pisagor’u uygula','ABD dik üçgeninde hipotenüs 8, dik kenar 4’tür.','x² = 8² − 4² = 48'),A('Kökü sadeleştir','48 = 16 × 3 olduğundan karekök 4√3 olur.','x = 4√3')],
 (4,3),[((4,2),'Yarım kenara 45° kuralını (√2) uygulamış: 4√2.','bilgi'),((8,1),'Yüksekliği kenara eşit sanmış.','bilgi'),((8,2),'Kenarı √2 ile çarpıp yükseklik yazmış.','bilgi'),((8,3),'Kenarı √3 ile çarpmış: 8√3 (yarısını almamış).','islem')],
 tipId='ge-eu-yukseklik',tip='Eşkenar üçgende yükseklik',z='kolay',alt='Levha Yüksekliği',kaz='Eşkenar üçgende yüksekliğin a√3/2 olduğunu kullanıp yüksekliği köklü ifade olarak bulur.',kalip='hikâyeli',
 kart='K-GEU-01 (yükseklik) · a = 8, h = 4√3',
 metin='Eşkenar üçgen biçimindeki bir reklam panosunun kenar uzunluğu şekilde desimetre cinsinden verilmiştir. Panonun tepe noktasından taban kenarının orta noktasına, yere dik olarak [AD] destek çubuğu yerleştirilmiştir. Şekil ölçekli değildir.\nBuna göre, çubuğun uzunluğu olan x kaç desimetredir?',
 istenen='Destek çubuğunun uzunluğu x (dm).',
 ip=['Çubuk tabanı hangi noktada keser? Oluşan iki dik üçgenin açıları ve kenarları hakkında ne söyleyebilirsin?'],
 bilgi=[EKN,PIS],
 puf='Kenarı a olan eşkenar üçgenin yüksekliği a√3 ÷ 2’dir; yüksekliğin tabanı ortaladığını kullanıp Pisagor’la da bulunur.',sekil=SK1)

# =================== 02 · alan · kolay ===================
kartla('K-GEU-02','Eşkenar üçgenin alanı','Alan = a²√3/4; a = 6 için 9√3. Alternatif: yükseklik 3√3 ve taban 6 ile 6 × 3√3 ÷ 2.','√3 çarpanını unutmak; yarıyı unutmak; 45° kuralını uygulamak.','kolay',2,'ge-eu-alan','Eşkenar üçgenin alanı')
a2=6; kare_esit(3,3,a2*a2*3,4); kare_esit(9,3,a2**4*3,16)   # h=3√3; alan=9√3: (9√3)^2=243=1296*3/16
h2=3*sqrt(3); assert abs(a2*h2/2-9*sqrt(3))<1e-9 and abs(a2*a2*sqrt(3)/4-9*sqrt(3))<1e-9
assert abs(a2*h2-18*sqrt(3))<1e-9 and abs(a2**2*sqrt(3)-36*sqrt(3))<1e-9
s=.6; B2=(0,0); C2=(a2*s,0); A2=(a2*s/2,a2*s*sqrt(3)/2)
f=F(); f.poly([A2,B2,C2]); f.tick(A2,B2); f.tick(A2,C2); f.tick(B2,C2)
f.sl('$6$',B2,C2,A2,.4)
f.vl('A',A2,(0,1),.3); f.vl('B',B2,(-1,-.6),.3); f.vl('C',C2,(1,-.6),.3)
SK2=f.svg()
qk('0002',[A('Yüksekliği bul','Eşkenar üçgende yükseklik a√3 ÷ 2’dir.','h = 6√3 ÷ 2 = 3√3'),A('Alan formülünü yaz','Alan = taban × yükseklik ÷ 2.','6 × 3√3 ÷ 2'),A('Hesapla','Çarpıp ikiye böl.','Alan = 9√3')],
 (9,3),[((3,3),'Yüksekliği (3√3) alan sanmış.','dikkat'),((9,1),'Alan = a² ÷ 4 = 9 yazmış; √3 çarpanını unutmuş.','bilgi'),((9,2),'√3 yerine √2 kullanmış: 6² × √2 ÷ 4.','bilgi'),((18,3),'Taban × yükseklik = 6 × 3√3 = 18√3 bulup ikiye bölmeyi unutmuş.','islem')],
 tipId='ge-eu-alan',tip='Eşkenar üçgenin alanı',z='kolay',alt='Eşkenar Üçgen Alanı',kaz='Kenarı verilen eşkenar üçgenin alanını a²√3/4 bağıntısıyla köklü ifade olarak hesaplar.',
 kart='K-GEU-02 (alan) · a = 6, alan 9√3',
 metin='Şekilde, üç kenarı da eşit uzunlukta olan bir ABC üçgeni verilmiştir: |AB| = |BC| = |CA|. Kenarlardan birinin uzunluğu cm cinsinden gösterilmiştir (eşit çentikli kenarların uzunlukları eşittir).\nBuna göre, ABC üçgeninin alanı kaç cm²’dir?',
 istenen='ABC üçgeninin alanı (cm²).',
 ip=['Alanı taban ve yükseklikle yazmak için önce yüksekliği bulman gerekir; eşkenar üçgenin yüksekliği kenardan nasıl hesaplanır?'],
 bilgi=[EKN],
 puf='Eşkenar üçgenin alanı a² × √3 ÷ 4 dür; yüksekliği a√3 ÷ 2 ile bulup taban × yükseklik ÷ 2 de yazabilirsin.',sekil=SK2)

# =================== 03 · iç noktadan uzaklıklar · orta · hikâyeli ===================
kartla('K-GEU-03','İç noktadan kenarlara uzaklıklar toplamı','Uzaklıklar toplamı yüksekliğe eşittir; yükseklikten kenar a = 2h ÷ √3 ile bulunur.','Toplamı kenar sanmak; a = h√3 yazmak; 2 katını unutmak.','orta',3,'ge-eu-uzaklik','Eşkenar üçgende iç noktanın uzaklıkları toplamı',kalip='hikâyeli')
d_=(2,3,4); h3=sum(d_); assert h3==9; kare_esit(6,3,(2*h3)**2,3)   # a=6√3: 108 = 324/3
s=.46; a3=6*sqrt(3)*s; B3=(0,0); C3=(a3,0); A3=(a3/2,a3*sqrt(3)/2)
assert abs(dist(A3,B3)-dist(B3,C3))<1e-9 and abs(A3[1]/s-9)<1e-9
P3=((2*A3[0]+3*B3[0]+4*C3[0])/9,(2*A3[1]+3*B3[1]+4*C3[1])/9)
def ayak(P,V,W):
    u=un(sub(W,V)); t=(P[0]-V[0])*u[0]+(P[1]-V[1])*u[1]; return add(V,mul(u,t))
Fa=ayak(P3,B3,C3); Fb=ayak(P3,C3,A3); Fc=ayak(P3,A3,B3)
assert abs(dist(P3,Fa)/s-2)<1e-9 and abs(dist(P3,Fb)/s-3)<1e-9 and abs(dist(P3,Fc)/s-4)<1e-9
assert abs(alan([A3,B3,C3])/s**2-27*sqrt(3))<1e-9
assert 18==2*h3 and abs(6*sqrt(3)-18/sqrt(3))<1e-9
f=F(); f.poly([A3,B3,C3]); f.line(P3,Fa); f.line(P3,Fb); f.line(P3,Fc); f.dik(Fa,P3,C3,.14); f.dik(Fb,P3,A3,.14); f.dik(Fc,P3,B3,.14)
f.node(add(mid(P3,Fa),(.3,.0)),'$2$'); f.node(add(mid(P3,Fb),(.3,.3)),'$3$'); f.node(add(mid(P3,Fc),(-.3,.3)),'$4$')
f.vl('A',A3,(0,1),.3); f.vl('B',B3,(-1,-.6),.3); f.vl('C',C3,(1,-.6),.3); f.vl('P',P3,(0,1),.3) if False else f.node(add(P3,(.0,.28)),'$P$')
SK3=f.svg()
qk('0003',[A('Alanları topla','P noktasını köşelere birleştirince ABC üçgeni üç üçgene ayrılır; her birinin tabanı a, yükseklikleri 2, 3 ve 4’tür.','Alan(ABC) = a × 2 ÷ 2 + a × 3 ÷ 2 + a × 4 ÷ 2 = a × 9 ÷ 2'),A('Yüksekliği yaz','Alan aynı zamanda a × h ÷ 2 dir; buradan h = 2 + 3 + 4 olur.','h = 9'),A('Kenarı bul','Eşkenar üçgende h = a√3 ÷ 2 olduğundan a = 2h ÷ √3.','a = 18 ÷ √3 = 6√3')],
 (6,3),[((18,3),'a = 2h × √3 = 18√3 yazmış (√3’e bölmek yerine çarpmış).','islem'),((18,1),'a = 2h = 18 yazmış; √3’e bölmeyi unutmuş.','islem'),((9,2),'Kenarı yükseklikten 45° kuralıyla (√2) bulmuş: 9√2.','bilgi'),((9,3),'a = h × √3 yazmış: 9√3.','bilgi')],
 tipId='ge-eu-uzaklik',tip='Eşkenar üçgende iç noktanın uzaklıkları toplamı',z='orta',alt='Parktaki Çeşme',kaz='Eşkenar üçgenin içindeki bir noktanın kenarlara uzaklıkları toplamının yüksekliğe eşitliğinden kenar uzunluğunu bulur.',kalip='hikâyeli',
 kart='K-GEU-03 (Viviani) · uzaklıklar 2, 3, 4',
 metin='Eşkenar üçgen biçimindeki ABC parkının içindeki P noktasına bir çeşme yapılmıştır. Çeşmenin park kenarlarına olan dik uzaklıkları şekilde metre cinsinden gösterilmiştir. Çeşme parkın içindedir ve kenarların hiçbiri üzerinde değildir. Şekil ölçekli değildir.\nBuna göre, parkın bir kenarının uzunluğu kaç metredir?',
 istenen='Parkın bir kenarının uzunluğu (m).',
 ip=['P noktasını köşelerle birleştirirsen üç üçgen elde edersin; bu üçgenlerin alanlarının toplamı ile büyük üçgenin alanını karşılaştır.'],
 bilgi=[VIV,EKN],
 puf='Eşkenar üçgende iç noktadan kenarlara dik uzaklıklar toplamı yüksekliğe eşittir; yükseklikten kenara a = 2h ÷ √3 ile geçilir.',sekil=SK3)

# =================== 04 · kare ve eşkenar üçgen · orta ===================
kartla('K-GEU-04','Karenin içinde eşkenar üçgen','ABE eşkenar olduğundan |AE| = |AD| ve m(DAE) = 30°; ADE üçgeni ikizkenar (75°-75°). Aynı biçimde BEC. DEC açısı 360° içinden çıkarılır.','AED açısını DEC sanmak; 60° + 60° gibi yanlış toplam; 90° − 60° = 30°da bırakmak.','orta',4,'ge-eu-bilesik','Eşkenar üçgenlerle oluşan şekiller')
f4=6; s=.8; A4=(0,0); B4=(f4*s,0); C4=(f4*s,f4*s); D4=(0,f4*s); E4=(f4*s*cos(radians(60)),f4*s*sin(radians(60)))
assert abs(dist(A4,E4)-dist(A4,B4))<1e-9 and abs(dist(B4,E4)-dist(A4,B4))<1e-9 and E4[1]<D4[1]
assert abs(ang(A4,D4,E4)-30)<1e-9 and abs(ang(E4,A4,D4)-75)<1e-9 and abs(ang(E4,B4,C4)-75)<1e-9 and abs(ang(E4,D4,C4)-150)<1e-9
assert 90-60==30 and 180-75==105 and 60+60==120 and 360-60-75-75==150
f=F(); f.poly([A4,B4,C4,D4]); f.line(A4,E4); f.line(B4,E4); f.line(D4,E4); f.line(C4,E4)
for p,q_ in [(A4,B4),(B4,C4),(D4,A4),(A4,E4),(B4,E4)]: f.tick(p,q_)
f.dik(A4,B4,D4,.2); f.arc(E4,D4,C4,.3,'$x$',.52)
f.vl('A',A4,(-1,-1),.3); f.vl('B',B4,(1,-1),.3); f.vl('C',C4,(1,1),.3); f.vl('D',D4,(-1,1),.3); f.vl('E',E4,(0,-1),.3)
SK4=f.svg()
q('0004',tipId='ge-eu-bilesik',tip='Eşkenar üçgenlerle oluşan şekiller',z='orta',alt='Kare İçinde Eşkenar Üçgen',kaz='Kare ve eşkenar üçgenin ortak kenarından oluşan ikizkenar üçgenlerin açılarıyla bir açıyı bulur.',
 kart='K-GEU-04 (kare + eşkenar) · ABCD kare, ABE eşkenar, m(DEC)',
 metin='Şekilde ABCD bir kare, ABE bir eşkenar üçgendir ve E noktası karenin içindedir. E noktası, D ve C köşeleriyle birleştirilmiştir. Eşit çentikli doğru parçalarının uzunlukları eşittir. Şekil ölçekli değildir.\nBuna göre, x = m(DEC) kaç derecedir?',
 dogru=150,yan=[(30,'m(DAE) = 90° − 60° = 30°’yi bulup bırakmış.','dikkat'),(75,'ADE üçgeninin taban açısını (75°) x sanmış.','dikkat'),(105,'180° − 75° = 105° yazmış (AED’nin bütünleyeni).','bilgi'),(120,'Eşkenar üçgenin 60°’sini iki kez toplamış: 60° + 60° = 120°.','bilgi')],
 istenen='x = m(DEC) açısının ölçüsü.',
 ip=['|AD| ile |AE| arasındaki ilişkiyi kullanıp ADE üçgeninin açılarını bul; E noktası etrafındaki açıların toplamına dikkat et.'],
 bilgi=[KAREUC,EKN],
 ad=[A('DAE açısını bul','Karenin dik açısından eşkenar üçgenin 60°’si çıkarılır.','m(DAE) = 90° − 60° = 30°'),A('ADE üçgenini çöz','|AE| = |AB| = |AD| olduğundan ADE ikizkenardır; taban açıları eşit.','m(AED) = (180° − 30°) ÷ 2 = 75°'),A('Simetriyi kullan','BEC üçgeni de aynı biçimdedir (|BE| = |BC|).','m(BEC) = 75°'),A('E etrafındaki açıları topla','E noktası etrafında 360° vardır; AEB = 60°.','x = 360° − 60° − 75° − 75° = 150°')],
 puf='Kare ile eşkenar üçgenin ortak kenarından oluşan üçgenler ikizkenardır; tamamlayıcı açılarla (360°) istenen açı bulunur.',sekil=SK4)

# =================== 05 · eşkenar üçgenlerden oluşan şekil · orta ===================
kartla('K-GEU-05','Kenarları üçe bölünmüş eşkenar üçgen','Kenarlara paralel doğrular 9 eş eşkenar üçgen oluşturur; her birinin alanı büyüğün 1/9’udur ve taralı alan sayılıp çarpılır.','Küçük üçgenleri yanlış saymak; küçük üçgenin kenarını 3 sanmak; tüm alanı taralı sanmak.','orta',4,'ge-eu-bilesik','Eşkenar üçgenlerle oluşan şekiller')
a5=12; k5=3; u_=(a5/k5,0); v_=(a5/k5/2,a5/k5*sqrt(3)/2); sc=.36
def Lp(i,j): return ((i*u_[0]+j*v_[0])*sc,(i*u_[1]+j*v_[1])*sc)
ups={(i,j):[Lp(i,j),Lp(i+1,j),Lp(i,j+1)] for i in range(3) for j in range(3) if i+j<=2}
dws={(i,j):[Lp(i+1,j),Lp(i,j+1),Lp(i+1,j+1)] for i in range(3) for j in range(3) if i+j<=1}
assert len(ups)==6 and len(dws)==3
gol=[ups[(0,2)],dws[(0,1)],ups[(0,0)],ups[(1,0)],ups[(2,0)]]
tum=alan([Lp(0,0),Lp(3,0),Lp(0,3)])/sc**2; assert abs(tum-36*sqrt(3))<1e-9
ar=sum(alan(t_) for t_ in gol)/sc**2; assert abs(ar-20*sqrt(3))<1e-9 and all(abs(alan(t_)/sc**2-4*sqrt(3))<1e-9 for t_ in ups.values())
assert 36*sqrt(3)/9*4==16*sqrt(3) and 36*sqrt(3)/9*6==24*sqrt(3) and 36*sqrt(3)/9*5==20*sqrt(3) and 20<16*sqrt(3)
kare_esit(4,3,16*3); kare_esit(5,3,25*3)
f=F()
for t_ in gol: f.fill(t_)
f.poly([Lp(0,0),Lp(3,0),Lp(0,3)])
for i in (1,2):
    f.line(Lp(i,0),Lp(i,3-i)); f.line(Lp(0,i),Lp(3-i,i)); f.line(Lp(i,0),Lp(0,i))
f.sl('$12$',Lp(0,0),Lp(3,0),Lp(0,3),.3)
f.vl('A',Lp(0,3),(0,1),.3); f.vl('B',Lp(0,0),(-1,-.6),.3); f.vl('C',Lp(3,0),(1,-.6),.3)
SK5=f.svg()
qk('0005',[A('Küçük üçgenin alanını bul','Her kenar 3 eş parçaya bölündüğünden şekil 9 eş eşkenar üçgendir; küçük üçgenin kenarı 12 ÷ 3 = 4’tür.','a² × √3 ÷ 4 = 16 × √3 ÷ 4 = 4√3'),A('Taralı üçgenleri say','Şekilde taralı olan küçük üçgenlerin sayısı sayılır.','5 küçük üçgen'),A('Alanı hesapla','Taralı alan = sayı × bir küçük üçgenin alanı.','5 × 4√3 = 20√3')],
 (20,3),[((20,1),'Bir küçük üçgenin alanını 4 (√3 çarpanı olmadan) alıp 5 ile çarpmış.','bilgi'),((16,3),'Taralı üçgenlerden birini saymamış (4 küçük üçgen).','dikkat'),((24,3),'Taralı olmayan bir üçgeni de saymış (6 küçük üçgen).','dikkat'),((36,3),'Tüm üçgenin alanını (12² × √3 ÷ 4) taralı alan sanmış.','dikkat')],
 tipId='ge-eu-bilesik',tip='Eşkenar üçgenlerle oluşan şekiller',z='orta',alt='Bölünmüş Eşkenar Üçgen',kaz='Kenarları eş parçaya bölünmüş eşkenar üçgende küçük eşkenar üçgenlerin alanından taralı bölgenin alanını bulur.',
 kart='K-GEU-05 (bölünmüş eşkenar) · a = 12, 9 eş üçgen, 5 taralı',
 metin='Şekilde kenar uzunluğu 12 cm olan ABC eşkenar üçgeninin her kenarı 3 eş parçaya bölünmüş ve bölme noktaları, kenarlara paralel doğru parçalarıyla birleştirilmiştir. Oluşan küçük üçgenlerin bir kısmı taranmıştır.\nBuna göre, taralı bölgelerin alanları toplamı kaç cm²’dir?',
 istenen='Taralı bölgelerin alanları toplamı (cm²).',
 ip=['Küçük üçgenlerin kenarı kaç cm? Hepsi eşkenar mı? Taralı olanları dikkatle say.'],
 bilgi=[EKN,BENZ],
 puf='Paralel doğrularla bölünen eşkenar üçgende küçük parçaların hepsi eşkenardır; bir parçanın alanı × parça sayısı = taralı alan.',sekil=SK5)

# =================== 06 · AD uzunluğu · zor ===================
kartla('K-GEU-06','Eşkenar üçgende kenar üzerindeki noktaya uzaklık','A’dan BC’ye inen yükseklikle ADH dik üçgeni kurulur: |AH| = 6√3, |HD| = 2; Pisagor ile |AD| = 4√7.','D’yi orta nokta sanmak; ABD’yi dik üçgen sanıp Pisagor uygulamak; 30°-60°-90° kuralını D için kullanmak.','orta',5,'ge-eu-yukseklik','Eşkenar üçgende yükseklik',kalip='şekilli')
a6=12; bd6=4; mh6=a6//2-bd6; assert mh6==2; ah2=(a6**2*3)//4; assert ah2==108
ad2=ah2+mh6**2; assert ad2==112==16*7; kare_esit(4,7,112)
assert (a6**2+bd6**2)==160 and 160==16*10 and bd6**2*3==48 and 48==16*3 and 10**2<112<11**2 and 4**2*3==48
kare_esit(6,3,108); kare_esit(4,10,160); kare_esit(4,3,48)
s=.4; B6=(0,0); C6=(a6*s,0); A6=(a6*s/2,a6*s*sqrt(3)/2); D6=(bd6*s,0)
assert abs(dist(A6,D6)/s-sqrt(112))<1e-9
f=F(); f.poly([A6,B6,C6]); f.line(A6,D6); f.tick(A6,B6); f.tick(A6,C6); f.tick(B6,C6)
f.raw(f'\\draw[<->,thin] ({B6[0]:.3f},-.75) -- ({C6[0]:.3f},-.75);'); f.node((C6[0]/2,-1.0),'$12$'); f.node((D6[0]/2,-.3),'$4$')
f.vl('A',A6,(0,1),.3); f.vl('B',B6,(-1,-.6),.3); f.vl('C',C6,(1,-.6),.3); f.vl('D',D6,(.3,-1),.3)
SK6=f.svg()
qk('0006',[A('Yüksekliği çiz','A’dan [BC]’ye inen yükseklik tabanı ortalar; ayağı H olsun. |BH| = 6 ve |AH| = 6√3.','|AH| = 12 × √3 ÷ 2 = 6√3'),A('|HD|’yi bul','D, B’den 4 uzaklıkta, H ise 6 uzaklıktadır.','|HD| = 6 − 4 = 2'),A('Pisagor’u uygula','AHD dik üçgeninde hipotenüs [AD]’dir.','|AD|² = (6√3)² + 2² = 108 + 4 = 112'),A('Kökü sadeleştir','112 = 16 × 7 olduğundan karekök 4√7 olur.','|AD| = 4√7')],
 (4,7),[((4,3),'ABD’yi 30°-60°-90° sanıp 4 × √3 = 4√3 yazmış.','bilgi'),((8,1),'|AB| − |BD| = 12 − 4 = 8 yazmış (iki uzunluğun farkını almış).','bilgi'),((6,3),'D’yi [BC]’nin orta noktası sanıp yüksekliği (6√3) yazmış.','dikkat'),((4,10),'ABD’yi dik üçgen sanmış: 12² + 4² = 160, |AD| = 4√10.','bilgi')],
 tipId='ge-eu-yukseklik',tip='Eşkenar üçgende yükseklik',z='orta',alt='Köşeden Kenar Üzerindeki Noktaya',kaz='Eşkenar üçgende yükseklik çizerek oluşan dik üçgende Pisagor ile köşeden taban üzerindeki bir noktaya uzaklığı bulur.',
 kart='K-GEU-06 (yükseklik + Pisagor) · a = 12, |BD| = 4',
 metin='Şekilde ABC bir eşkenar üçgendir ve kenar uzunluğu 12 cm’dir. D noktası [BC] kenarı üzerinde olup |BD| = 4 cm dir. A köşesi ile D noktası bir doğru parçasıyla birleştirilmiştir. Şekil ölçekli değildir.\nBuna göre, |AD| kaç cm’dir?',
 istenen='|AD| uzunluğu (cm).',
 ip=['A köşesinden [BC] kenarına bir yükseklik çizip D noktasının yüksekliğin ayağına göre yerini belirle.'],
 bilgi=[EKN,PIS],
 puf='Eşkenar üçgende bir köşeden karşı kenar üzerindeki noktaya uzaklık için yükseklik çiz: yarım kenar ve yükseklikle dik üçgen kurup Pisagor uygula.',sekil=SK6)

bitir_geo()
