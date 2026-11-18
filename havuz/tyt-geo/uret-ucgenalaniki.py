"""TYT Geometri · hafif mod üretici. Şekil koordinatları hesaplanır, TikZ aynı değerlerden üretilir; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
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
def vtx(f,P_,name,ic,d=.3): f.vl(name,P_,sub(P_,ic),d)
def tri(a,b,c,s):
    """BC=a, CA=b, AB=c → A,B,C (B orijin, BC yatay), s ölçek"""
    x=(c*c+a*a-b*b)/(2*a); y=sqrt(c*c-x*x); return (x*s,y*s),(0,0),(a*s,0)
def tri_ac(B_,C_,Bd,Cd):
    """B ve C açıları (derece) ile A (B,C yatay)"""
    a=dist(B_,C_); Ad=180-Bd-Cd; c=a*sin(radians(Cd))/sin(radians(Ad))
    return (B_[0]+c*cos(radians(Bd)),B_[1]+c*sin(radians(Bd)))
def incenter(A_,B_,C_):
    a=dist(B_,C_); b=dist(A_,C_); c=dist(A_,B_); w=a+b+c
    return ((a*A_[0]+b*B_[0]+c*C_[0])/w,(a*A_[1]+b*B_[1]+c*C_[1])/w)
def rot(p,t,o=(0,0)):
    t=radians(t); d=sub(p,o); return (o[0]+d[0]*cos(t)-d[1]*sin(t),o[1]+d[0]*sin(t)+d[1]*cos(t))
def kesis(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4; d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)
TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def bitir_geo(onek,konuad):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def dim(f,p,q_,t,n,off=.6):
    """ölçü oku: p–q doğru parçasını n yönünde off kadar ötele, iki uçlu ok + ortada etiket"""
    n=un(n); p2=add(p,mul(n,off)); q2=add(q_,mul(n,off))
    f.line(p,add(p,mul(n,off+.12)),'thin'); f.line(q_,add(q_,mul(n,off+.12)),'thin')
    f.line(p2,q2,'{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}'); f.node(add(mid(p2,q2),mul(n,.24)),t)
def arct(f,V,a,b,r,n=1):
    """yay + n çentik (eş açı işareti)"""
    f.arc(V,a,b,r)
    a1=degrees(atan2(a[1]-V[1],a[0]-V[0])); a2=degrees(atan2(b[1]-V[1],b[0]-V[0])); d=(a2-a1+180)%360-180; m=radians(a1+d/2)
    e=(cos(m),sin(m)); tg=(-e[1],e[0])
    for i in range(n):
        c=add(V,mul(e,r)); c=add(c,mul(tg,(i-(n-1)/2)*.08))
        f.line(add(c,mul(e,-.07)),add(c,mul(e,.07)))
def foot(P_,A_,B_):
    d=un(sub(B_,A_)); t=(P_[0]-A_[0])*d[0]+(P_[1]-A_[1])*d[1]; return add(A_,mul(d,t))
def ok(a,b,t=1e-9): assert abs(a-b)<t,(a,b)
ONEK='ucgenalaniki'; KONU_AD='Üçgende Alan'
P=Parti(ONEK,KONU_AD,'geo|Üçgende Alan',ders='TYT Geometri',idon='tytgeo')
konu('geo|Üçgende Alan','Üçgende Alan')
TABAN=lambda ornek:B('Üçgenin alanı','alan = taban × yükseklik ÷ 2 dir. Her kenar taban seçilebilir; yükseklik, o kenara karşı köşeden kenarın doğrultusuna inen dikmedir. '+ornek)
SINUS=B('Sinüs ile alan','iki kenarı a, b ve aralarındaki açısı C olan üçgenin alanı ½ × a × b × sin C dir. sin 30° = ½ · sin 45° = √2/2 · sin 60° = √3/2 · sin 90° = 1; ayrıca sin (180° − α) = sin α dır. Örnek: kenarları 5 ve 6, aradaki açısı 90° olan üçgenin alanı ½ × 5 × 6 × 1 = 15')
KOR=B('Kenarortay ve ağırlık merkezi','bir köşeyi karşı kenarın orta noktasına bağlayan doğru parçasına kenarortay denir. Üç kenarortay aynı noktada kesişir; bu nokta ağırlık merkezidir. Örnek: [KL] nin orta noktası M ise |KM| = |ML| dir')
DIKD=B('Dikdörtgen','karşılıklı kenarları paralel ve eşit olan, bütün açıları 90° olan dörtgendir; alanı komşu iki kenarının çarpımıdır. Örnek: 9 cm × 4 cm lik dikdörtgenin alanı 36 cm² dir')
KOOR=B('Doğrunun eksenleri kestiği noktalar','y = mx + n doğrusu y eksenini (0, n) noktasında keser; x eksenini kestiği noktanın apsisi y = 0 yazılarak bulunur. İki doğrunun kesim noktası, denklemlerin ortak çözümüdür. Örnek: y = 3x − 6 doğrusu x eksenini (2, 0) noktasında keser')
ITC=B('İç teğet çember','üçgenin üç kenarına da teğet olan çembere iç teğet çember denir; merkezi I, iç açıortayların kesim noktasıdır. Yarıçap, değme noktasında kenara diktir. Örnek: yarıçapı 3 cm olan çemberin değme noktasına çizilen yarıçap, teğete diktir')
BENZ=B('Benzerlik ve alan','açıları eşit olan iki üçgen benzerdir; benzerlik oranı k ise alanlarının oranı k² dir. Örnek: benzerlik oranı 2 / 5 olan iki üçgenin alanları oranı 4 / 25 tir')
ESK=B('Eşkenar üçgen','üç kenarı eşit, her açısı 60° olan üçgendir; kenarı a ise yüksekliği a√3 / 2 dir. Örnek: kenarı 6 cm olan eşkenar üçgenin yüksekliği 3√3 cm dir')
NOT=lambda: 'Şekil ölçekli değildir.'

# ---- 01 · kolay · farklı tabanlara inen yükseklikler
kartla('K-GUI-01','Üç yükseklik, tek alan','Üçgenin her kenarı taban olabilir; yüksekliği hangi kenara inildiğine göre okunur.','Yüksekliği yanlış tabana ait sanmak; alanı hesaplamadan uzunlukları oranlamak.','kolay',3,'ui-yukseklik','Farklı tabanlara inen yükseklikler')
s=.38; B1=(0,0); C1=(12*s,0); H1=(6*s,0); A1=(6*s,8*s); K1=foot(B1,A1,C1)
ok(dist(A1,C1)/s,10); ok(ang(H1,A1,B1),90); ok(ang(K1,B1,A1),90); ok(dist(B1,K1)/s,9.6); ok(alan([A1,B1,C1])/s**2,48)
assert 0<dist(A1,K1)/dist(A1,C1)<1
f=F(); f.poly([A1,B1,C1]); f.line(A1,H1); f.line(B1,K1); f.dik(H1,A1,B1); f.dik(K1,B1,A1)
ic=cen([A1,B1,C1]); dim(f,B1,C1,'$12$',(0,-1),.7); f.node(add(lerp(H1,A1,.82),(-.25,0)),'$8$'); f.sl('$10$',A1,C1,ic,.3)
f.vl('A',A1,(0,1),.3); f.vl('B',B1,(-1,-.6),.3); f.vl('C',C1,(1,-.5),.3); f.vl('H',H1,(.4,-1),.3); f.vl('K',K1,(1,.4),.3)
SK=f.svg()
q('0001',tipId='ui-yukseklik',tip='Farklı tabanlara inen yükseklikler',z='kolay',kalip='hikâyeli',alt='Yükseklik ve Taban',kaz='Bir üçgende verilen taban–yükseklik çiftinden alanı bulup başka bir tabana inen yüksekliği hesaplar.',
 kart='K-GUI-01 (iki farklı taban–yükseklik çifti) · levha',
 metin='Şekilde, üçgen biçimli bir ahşap levhanın [BC] kenarı 12 cm, A köşesinden [BC] kenarına inen (H ∈ [BC]) [AH] dikmesi 8 cm ve [AC] kenarı 10 cm dir. B köşesinden [AC] kenarına inen [BK] dikmesi de çizilmiştir.\nŞekil ölçekli değildir.\nBuna göre, |BK| kaç cm dir?',
 dogru=9.6,yan=[(4.8,'Alanı bulurken ikiye bölüp, yüksekliği bulurken yine ikiye bölmüş: 12 × 8 ÷ 2 ÷ 10 = 4,8.','islem'),(6,'|HC| = 6 uzunluğunu yükseklik sanmış.','dikkat'),(12,'|BC| uzunluğunu cevap olarak vermiş.','dikkat'),(48,'Üçgenin alanını (48 cm²) bulup orada bırakmış.','dikkat')],
 istenen='|BK| uzunluğu (cm).',
 ip=['Bu levhanın alanını iki farklı yoldan yazabilir misin?'],
 bilgi=[TABAN('Örnek: 10 cm lik kenarına inen yüksekliği 4 cm olan üçgenin alanı 10 × 4 ÷ 2 = 20 cm² dir')],
 ad=[A('Alanı bul','[BC] tabanına inen yükseklik [AH] dir.','Alan = 12 × 8 ÷ 2 = 48 cm²'),A('Başka tabanla yaz','Aynı alan [AC] tabanı ve ona inen [BK] yüksekliğiyle de yazılabilir.','10 × |BK| ÷ 2 = 48'),A('Yüksekliği çöz','Denklemi |BK| için çöz.','|BK| = 96 ÷ 10 = 9,6 cm')],
 puf='Verilen uzunlukların hangi tabana ait olduğunu işaretle; bilinen tabanla alanı önce sayıya çevirmek çoğu zaman işi kolaylaştırır.',sekil=SK)

# ---- 02 · kolay · sinüslü alan, paralelkenar içinde, geniş açı
kartla('K-GUI-02','İki kenar ve aradaki açı','Köşegen paralelkenarda üçgen ayırır; aradaki açı geniş olabilir.','Paralelkenarın alanını cevap sanmak; ½ çarpanını atlamak.','kolay',3,'ui-sinus','İki kenar ve aradaki açıyla alan')
s=.5; A2=(0,0); B2=(7*s,0); D2=(8*s*cos(radians(150)),8*s*sin(radians(150))); C2=add(B2,D2)
ok(ang(A2,B2,D2),150); ok(alan([A2,B2,D2])/s**2,14); ok(alan([A2,B2,C2,D2])/s**2,28)
f=F(); f.fill([A2,B2,D2]); f.poly([A2,B2,C2,D2]); f.line(B2,D2); ic=cen([A2,B2,C2,D2])
f.arc(A2,B2,D2,.5,'$150^\\circ$',.78); f.sl('$7$',A2,B2,ic,.3); f.sl('$8$',A2,D2,ic,.3)
f.vl('A',A2,(-.6,-1),.3); f.vl('B',B2,(1,-.6),.3); f.vl('C',C2,(1,.6),.3); f.vl('D',D2,(-1,.6),.3)
SK=f.svg()
q('0002',tipId='ui-sinus',tip='İki kenar ve aradaki açıyla alan',z='kolay',alt='Paralelkenardan Üçgen',kaz='Paralelkenarın köşegeniyle ayrılan üçgenin alanını iki kenar ve aradaki geniş açıdan hesaplar.',
 kart='K-GUI-02 (iki kenar, geniş aradaki açı) · paralelkenar',
 metin='Şekildeki ABCD paralelkenarında |AB| = 7 cm, |AD| = 8 cm ve m(DAB) = 150° dir. [BD] köşegeni çizilmiştir.\nŞekil ölçekli değildir.\nBuna göre, taralı ABD üçgeninin alanı kaç cm² dir?',
 dogru='14',sira=['14','14√3','28','28√3','56'],
 yan=[('14√3','sin 150° yerine √3/2 almış: ½ × 7 × 8 × √3/2 = 14√3.','bilgi'),('28','Üçgen yerine paralelkenarın alanını (7 × 8 × ½ = 28) vermiş.','dikkat'),('28√3','½ çarpanını atlayıp sin 150° yerine √3/2 almış: 7 × 8 × √3/2 = 28√3.','islem'),('56','Yalnız iki kenarı çarpmış: 7 × 8 = 56.','bilgi')],
 istenen='Taralı ABD üçgeninin alanı (cm²).',
 ip=['ABD üçgeninin hangi iki kenarı ve bu kenarlar arasındaki açı verilmiş?'],
 bilgi=[SINUS],
 ad=[A('Verilenleri belirle','ABD üçgeninde |AB| = 7, |AD| = 8 ve bu iki kenarın arasındaki açı 150° dir.','|AB| = 7, |AD| = 8, m(A) = 150°'),A('Sinüsü bul','150° ile 30° bütünleyen açılardır; sinüsleri eşittir.','sin 150° = sin 30° = ½'),A('Alanı hesapla','Sinüslü alan bağıntısını uygula.','½ × 7 × 8 × ½ = 14 cm²')],
 puf='Önce hangi üçgenin alanının istendiğini belirle; köşegenle ayrılan parçanın kenarlarını ve aralarındaki açıyı şekilden oku.',sekil=SK)

# ---- 03 · orta · alanlardan uzunluk (ortak yükseklik), hikâyeli
kartla('K-GUI-03','Alan bilgisinden uzunluk','Alan bilgisi verilince taban uzunluğu bölünür; yükseklik şekilde görünmez.','Verilen alanı uzunluk sanmak; parçaları yanlış sırayla eşlemek.','orta',4,'ui-oran','Alan bilgisiyle kenar parçalama')
s=.33; B3=(0,0); C3=(16*s,0); A3=(5*s,7*s); D3=(6*s,0)
ok(alan([A3,B3,C3])/s**2,56); ok(alan([A3,B3,D3])/s**2,21); ok(dist(D3,C3)/s,10)
f=F(); f.fill([A3,B3,D3]); f.poly([A3,B3,C3]); f.line(A3,D3); ic=cen([A3,B3,C3])
dim(f,B3,C3,'$16$',(0,-1),.7); f.node(cen([A3,B3,D3]),'$21$')
f.node((8*s,-1.55*s*3),'Alan$(ABC)=56\\ \\mathrm{m}^2$')
f.vl('A',A3,(0,1),.3); f.vl('B',B3,(-1,-.6),.3); f.vl('C',C3,(1,-.6),.3); f.vl('D',D3,(.5,.9),.3)
SK=f.svg()
q('0003',tipId='ui-oran',tip='Alan bilgisiyle kenar parçalama',z='orta',kalip='hikâyeli',alt='Alandan Uzunluğa',kaz='Üçgen bir arsada verilen alanlardan kenar parçasının uzunluğunu bulur.',
 kart='K-GUI-03 (alan bilgisinden taban parçası) · arsa',
 metin='Şekilde alanı 56 m² olan ABC biçimli bir arsa gösterilmiştir. Arsanın [BC] kenarı 16 m dir. A köşesi, [BC] üzerindeki D noktasına bir çitle birleştirilmiş ve ABD bölümünün alanı 21 m² olarak ölçülmüştür.\nŞekil ölçekli değildir.\nBuna göre, |DC| kaç m dir?',
 dogru=10,yan=[(6,'Yanlış parçayı bulmuş: |BD| = 16 × 21 ÷ 56 = 6.','dikkat'),(7,'Arsanın yüksekliğini (56 × 2 ÷ 16 = 7) bulup |DC| sanmış.','dikkat'),(8,'D noktasını [BC] nin orta noktası sanıp 16 ÷ 2 yazmış.','bilgi'),(16,'|BC| uzunluğunu cevap olarak vermiş.','dikkat')],
 istenen='|DC| uzunluğu (m).',
 ip=['Alanı bilinen ABC ve ABD üçgenlerinin ortak özelliği ne?'],
 bilgi=[TABAN('Örnek: 12 cm lik kenarına inen yüksekliği 5 cm olan üçgenin alanı 30 cm² dir')],
 ad=[A('ADC nin alanını bul','ABC arsası ABD ve ADC bölümlerinden oluşur.','56 − 21 = 35 m²'),A('Yüksekliği bul','ABC için taban 16 m ve alan 56 m² dir.','h = 2 × 56 ÷ 16 = 7 m'),A('|DC| yi çöz','ADC üçgeninin yüksekliği de aynı h dir.','|DC| × 7 ÷ 2 = 35 → |DC| = 10 m')],
 puf='Verilen alanları parçalara ayır; her parçanın tabanını ve yüksekliğini ayrı ayrı yazmak bilinmeyeni görünür kılar.',sekil=SK)

# ---- 04 · orta · ağırlık merkezi ve alan
kartla('K-GUI-04','İki kenarortay, alt bölge','Kenarortaylar üçgeni eş alanlı altı parçaya böler; istenen bölge bu parçalardan oluşur.','Yalnız bir parçayı cevap sanmak; tüm alanın yarısını almak.','orta',3,'ui-agirlik','Kenarortaylarla oluşan bölgeler')
Bz=(0,0); Cz=(12*.45,0); Az=(4*.45,9*.45); sz=.45
Dz=mid(Bz,Cz); Ez=mid(Az,Cz); Gz=kesis(Az,Dz,Bz,Ez)
ok(alan([Az,Bz,Cz])/sz**2,54); ok(alan([Cz,Dz,Gz,Ez])/sz**2,18)
for t in ([Bz,Gz,Dz],[Dz,Gz,Cz],[Cz,Gz,Ez],[Ez,Gz,Az],[Az,Gz,Bz]): pass
ok(alan([Dz,Gz,Cz])/sz**2,9); ok(alan([Cz,Gz,Ez])/sz**2,9)
f=F(); f.fill([Cz,Dz,Gz,Ez]); f.poly([Az,Bz,Cz]); f.line(Az,Dz); f.line(Bz,Ez); f.tick(Bz,Dz); f.tick(Dz,Cz); f.tick(Cz,Ez,2); f.tick(Ez,Az,2)
f.node((6*sz,-1.0),'Alan$(ABC)=54\\ \\mathrm{cm}^2$')
f.vl('A',Az,(0,1),.3); f.vl('B',Bz,(-1,-.6),.3); f.vl('C',Cz,(1,-.6),.3); f.vl('D',Dz,(0,-1),.3); f.vl('E',Ez,(1,.5),.3); f.vl('G',Gz,(-.2,-1),.3)
SK=f.svg()
q('0004',tipId='ui-agirlik',tip='Kenarortaylarla oluşan bölgeler',z='orta',alt='Kenarortaylar ve Alan',kaz='İki kenarortayın kesim noktasıyla oluşan bölgelerin alanını bulur.',
 kart='K-GUI-04 (iki kenarortay, dörtgen bölge) · D ve E orta nokta',
 metin='Şekilde alanı 54 cm² olan ABC üçgeninde D, [BC] kenarının; E ise [AC] kenarının orta noktasıdır. [AD] ile [BE] doğru parçalarının kesim noktası G dir.\nŞekil ölçekli değildir.\nBuna göre, taralı CDGE dörtgeninin alanı kaç cm² dir?',
 dogru=18,yan=[(9,'Dörtgeni tek bir köşe üçgeni sanmış: 54 ÷ 6 = 9.','dikkat'),(27,'Taralı bölgeyi üçgenin yarısı sanmış: 54 ÷ 2 = 27.','bilgi'),(36,'Tüm alanın 2/3 ünü almış: 54 × 2 ÷ 3 = 36.','bilgi'),(54,'Üçgenin alanını cevap olarak vermiş.','dikkat')],
 istenen='Taralı CDGE dörtgeninin alanı (cm²).',
 ip=['AD ve BE nin oluşturduğu parçalardan alanı kolayca bulunabilen hangisi?'],
 bilgi=[KOR,TABAN('Örnek: tabanı 6 cm, yüksekliği 5 cm olan üçgenin alanı 15 cm² dir')],
 ad=[A('ADC yi bul','[AD] kenarortay olduğundan ABD ve ADC üçgenlerinin alanları eşittir.','Alan(ADC) = 54 ÷ 2 = 27'),A('AGE yi bul','G ağırlık merkezi olduğundan [CG] de kenarortaydır; kenarortaylar üçgeni eş alanlı altı parçaya böler.','Alan(AGE) = 54 ÷ 6 = 9'),A('Farkı al','CDGE, ADC den AGE çıkarılınca kalır.','27 − 9 = 18 cm²')],
 puf='Şekildeki bölgeyi alanı bilinen daha küçük parçalardan kurmayı dene; kenarortaylar hangi parçaları eş yapıyor?',sekil=SK)

# ---- 05 · orta · dikdörtgenin içindeki nokta
kartla('K-GUI-05','Dikdörtgen içinde bir nokta','İç noktadan köşelere çizilen doğrular dikdörtgeni dört üçgene böler; üçgenlerin tabanları dikdörtgenin kenarlarıdır.','Dört alanı toplayıp dikdörtgenin alanını sanmak; karşılıklı olmayan üçgenleri eşlemek.','orta',4,'ui-ic-nokta','İç noktadan köşelere bölünen alanlar')
Wd,Hd=10.5,96/10.5; sd=.4; Pd=(66/Hd,44/Wd)
Pp=lambda p:(p[0]*sd,p[1]*sd)
Ad,Bd,Cd,Dd=(0,0),(Wd,0),(Wd,Hd),(0,Hd)
areas={'PAB':alan([Pd,Ad,Bd]),'PBC':alan([Pd,Bd,Cd]),'PCD':alan([Pd,Cd,Dd]),'PDA':alan([Pd,Dd,Ad])}
ok(areas['PAB'],22); ok(areas['PBC'],15); ok(areas['PCD'],26); ok(areas['PDA'],33); ok(22+26,15+33)
f=F(); f.poly([Pp(Ad),Pp(Bd),Pp(Cd),Pp(Dd)])
for v in (Ad,Bd,Cd,Dd): f.line(Pp(Pd),Pp(v))
f.node(Pp(cen([Pd,Ad,Bd])),'$22$'); f.node(Pp(cen([Pd,Bd,Cd])),'$15$'); f.node(Pp(cen([Pd,Cd,Dd])),'$26$')
f.vl('A',Pp(Ad),(-1,-.6),.3); f.vl('B',Pp(Bd),(1,-.6),.3); f.vl('C',Pp(Cd),(1,.6),.3); f.vl('D',Pp(Dd),(-1,.6),.3); f.vl('P',Pp(Pd),(0,1),.3)
SK=f.svg()
q('0005',tipId='ui-ic-nokta',tip='İç noktadan köşelere bölünen alanlar',z='orta',kalip='hikâyeli',alt='Dikdörtgende İç Nokta',kaz='Dikdörtgenin içindeki bir noktayla oluşan üçgenlerin alanları arasındaki ilişkiyi kullanarak bilinmeyen alanı bulur.',
 kart='K-GUI-05 (dikdörtgen, iç nokta, dört üçgen) · tarla',
 metin='Dikdörtgen biçimli ABCD tarlasının içindeki P noktasından köşelere birer çit çekilerek tarla dört üçgen bölüme ayrılmıştır. Şekilde PAB, PBC ve PCD bölümlerinin alanları m² cinsinden verilmiştir.\nŞekil ölçekli değildir.\nBuna göre, PDA bölümünün alanı kaç m² dir?',
 dogru=33,yan=[(11,'Alanların farkını almış: 26 − 15 = 11.','islem'),(15,'Karşı üçgenin alanını (PBC = 15) bölüm alanı sanmış.','dikkat'),(22,'Karşısındaki değil bitişik bölümün alanını (PAB = 22) cevap sanmış.','dikkat'),(26,'Karşıt bölümün alanını (PCD = 26) cevap sanmış.','dikkat')],
 istenen='PDA bölümünün alanı (m²).',
 ip=['Hangi iki üçgenin tabanları dikdörtgenin karşılıklı kenarlarıdır?'],
 bilgi=[DIKD,TABAN('Örnek: tabanı 8 cm, yüksekliği 3 cm olan üçgenin alanı 12 cm² dir')],
 ad=[A('Dikmeleri adlandır','|AB| = |CD| = a, P den [AB] ye uzaklık h₁ ve [CD] ye uzaklık h₂ olsun; h₁ + h₂ = |BC| dir.','h₁ + h₂ = |BC|'),A('Karşıt çifti yaz','PAB + PCD alanları a(h₁ + h₂) ÷ 2 yani dikdörtgenin yarısıdır.','PAB + PCD = ABCD ÷ 2'),A('Diğer çifti yaz','Aynı akıl yürütme PBC ve PDA için de geçerlidir.','PBC + PDA = ABCD ÷ 2'),A('Eşitle ve çöz','İki toplam birbirine eşittir.','22 + 26 = 15 + PDA → PDA = 33 m²')],
 puf='İçerideki noktanın yerini bilmesen de, aynı kenara dayanan üçgenleri bir arada düşünmek bilinmeyen alanı sana verir.',sekil=SK)

# ---- 06 · orta · koordinat düzleminde alan
kartla('K-GUI-06','Doğrular ve eksenle sınırlı üçgen','Üçgenin köşeleri doğruların kesişim ve eksen noktalarıdır; taban x ekseni üzerinde, yükseklik kesişimin ordinatıdır.','Eksen kesim noktasını yanlış işaretlemek; kesişimin ordinatı yerine y eksenini kesen değeri kullanmak.','orta',4,'ui-koordinat','Koordinat düzleminde üçgenin alanı')
sk=.45; Ak,Bk,Ck=(-2,0),(7,0),(1,6)
ok(2*(-2)+4,0); ok(-7+7,0); ok(2*1+4,6); ok(-1+7,6); ok(alan([Ak,Bk,Ck]),27)
Pk=lambda p:(p[0]*sk,p[1]*sk)
f=F(); f.fill([Pk(Ak),Pk(Bk),Pk(Ck)]); f.raw(f'\\draw[-{{Stealth[length=2mm]}}] {pt(Pk((-3.3,0)))} -- {pt(Pk((8.4,0)))};'); f.raw(f'\\draw[-{{Stealth[length=2mm]}}] {pt(Pk((0,-1.6)))} -- {pt(Pk((0,8.4)))};')
f.line(Pk((-2.3,-.6)),Pk((1.7,7.4))); f.line(Pk((-.4,7.4)),Pk((7.4,-.4)))
f.node(Pk((8.6,-.5)),'$x$'); f.node(Pk((.5,8.4)),'$y$'); f.node(Pk((-.45,-.5)),'$O$')
f.node(Pk((2.5,7.7)),'$d_1$'); f.node(Pk((-1.0,7.8)),'$d_2$')
f.vl('A',Pk(Ak),(.3,-1),.3); f.vl('B',Pk(Bk),(.7,-1),.3); f.vl('C',Pk(Ck),(1,0),.35)
SK=f.svg()
q('0006',tipId='ui-koordinat',tip='Koordinat düzleminde üçgenin alanı',z='orta',alt='Koordinat Düzleminde Alan',kaz='İki doğru ve x ekseniyle sınırlı üçgenin köşelerini bulup alanını hesaplar.',
 kart='K-GUI-06 (iki doğru ve x ekseni) · d₁, d₂',
 metin='Dik koordinat düzleminde d₁: y = 2x + 4 ve d₂: y = −x + 7 doğruları çizilmiştir. Bu iki doğru ile x ekseninin sınırladığı bölge, köşeleri A, B ve C olan taralı ABC üçgenidir.\nŞekil ölçekli değildir.\nBuna göre, ABC üçgeninin alanı kaç birimkaredir?',
 dogru=27,yan=[(13.5,'Taban ve yükseklikten sonra bir kez daha ikiye bölmüş: 27 ÷ 2 = 13,5.','islem'),(15,'d₁ nin x eksenini kestiği noktayı 2 sanmış: taban |7 − 2| = 5; 5 × 6 ÷ 2 = 15.','dikkat'),(21,'Tabanı 7 almış (d₁ nin eksenle kesişimini unutmuş): 7 × 6 ÷ 2 = 21.','dikkat'),(54,'İkiye bölmeyi unutmuş: 9 × 6 = 54.','bilgi')],
 istenen='ABC üçgeninin alanı (birimkare).',
 ip=['A, B ve C noktalarının koordinatları nasıl bulunur? Hangi kenarı taban almak işini kolaylaştırır?'],
 bilgi=[KOOR,TABAN('Örnek: tabanı 8 birim, yüksekliği 3 birim olan üçgenin alanı 12 birimkaredir')],
 ad=[A('A ve B yi bul','Doğruların x eksenini kestiği noktalar için y = 0 yazılır.','d₁: 0 = 2x + 4 → A(−2, 0) · d₂: 0 = −x + 7 → B(7, 0)'),A('C yi bul','İki doğrunun kesim noktası için denklemler eşitlenir.','2x + 4 = −x + 7 → x = 1, y = 6 → C(1, 6)'),A('Taban ve yükseklik','Taban x ekseni üzerindeki [AB], yükseklik C nin ordinatıdır.','|AB| = 9, h = 6'),A('Alanı hesapla','Alan = taban × yükseklik ÷ 2.','9 × 6 ÷ 2 = 27')],
 puf='Köşe koordinatlarını tek tek bulmadan alan hesaplamaya başlama; hangi köşeler eksen üzerinde?',sekil=SK)

# ---- 07 · orta · iç teğet çemberin yarıçapı
kartla('K-GUI-07','Alan ve iç teğet çember','Üçgenin alanı, iç teğet çemberin merkezinden köşelere bölünen üç üçgenin toplamıdır.','Çevre yerine yarı çevreyi kullanmamak; tabanla yüksekliği karıştırmak.','orta',4,'ui-ic-teget','İç teğet çemberin yarıçapı')
sI=.33; BI,CI,AI=(0,0),(14*sI,0),(5*sI,12*sI); I7=incenter(AI,BI,CI)
ok(dist(AI,BI)/sI,13); ok(dist(AI,CI)/sI,15); ok(alan([AI,BI,CI])/sI**2,84); r7=I7[1]
ok(r7/sI,4); ok(dist(I7,foot(I7,AI,BI))/sI,4); ok(dist(I7,foot(I7,AI,CI))/sI,4)
Dt=(I7[0],0)
f=F(); f.poly([AI,BI,CI]); f.raw(f'\\draw {pt(I7)} circle ({r7:.3f});'); f.line(I7,Dt); f.dik(Dt,I7,CI); f.raw(f'\\fill {pt(I7)} circle (1.4pt);')
ic=I7; f.sl('$13$',AI,BI,ic,.3); f.sl('$15$',AI,CI,ic,.3); f.sl('$14$',BI,CI,ic,.3)
f.node(add(mid(I7,Dt),(.25,0)),'$r$'); f.vl('I',I7,(-.7,.6),.28)
f.vl('A',AI,(0,1),.3); f.vl('B',BI,(-1,-.6),.3); f.vl('C',CI,(1,-.6),.3)
f.node((7*sI,-1.35*sI*3),'Alan$(ABC)=84\\ \\mathrm{cm}^2$')
SK=f.svg()
q('0007',tipId='ui-ic-teget',tip='İç teğet çemberin yarıçapı',z='orta',alt='İç Teğet Çember ve Alan',kaz='Alanı ve kenarları verilen üçgenin iç teğet çemberinin yarıçapını bulur.',
 kart='K-GUI-07 (iç teğet çember yarıçapı) · 13–14–15',
 metin='Şekilde kenar uzunlukları 13 cm, 14 cm ve 15 cm olan, alanı 84 cm² olan ABC üçgeninin iç teğet çemberi çizilmiştir. Çemberin merkezi I, yarıçapı r dir.\nŞekil ölçekli değildir.\nBuna göre, r kaç cm dir?',
 dogru=4,yan=[(2,'Alanı çevreye bölmüş: 84 ÷ 42 = 2 (yarı çevre yerine çevreyi kullanmış).','islem'),(6,'Alanı yalnız bir kenara bölmüş: 84 ÷ 14 = 6.','bilgi'),(12,'Üçgenin yüksekliğini bulup yarıçap sanmış: 2 × 84 ÷ 14 = 12.','dikkat'),(28,'Alanı kenar sayısına bölmüş: 84 ÷ 3 = 28.','bilgi')],
 istenen='İç teğet çemberin yarıçapı r (cm).',
 ip=['Alan ile yarıçap arasında bir bağıntı kurabilir misin?'],
 bilgi=[ITC,TABAN('Örnek: tabanı 9 cm, yüksekliği 4 cm olan üçgenin alanı 18 cm² dir')],
 ad=[A('Üçgeni üçe ayır','[IA], [IB] ve [IC] çizilince ABC; IAB, IBC ve ICA üçgenlerine ayrılır.','Alan(ABC) = Alan(IAB) + Alan(IBC) + Alan(ICA)'),A('Yükseklikleri yaz','Her üçgenin yüksekliği, merkezden kenara indirilen yarıçaptır.','½ × 13 × r + ½ × 14 × r + ½ × 15 × r'),A('Toplamı sadeleştir','Ortak çarpanı dışarı al.','½ × (13 + 14 + 15) × r = 21 r'),A('r yi bul','Toplam alana eşitle.','21 r = 84 → r = 4 cm')],
 puf='Elindeki alan bilgisini kullanmak için ABC yi merkezden parçalara ayırmayı düşün.',sekil=SK)

# ---- 08 · zor · yamukta köşegenlerin ayırdığı alanlar
kartla('K-GUI-08','Yamukta köşegenle dört alan','Köşegenler yamuğu dört üçgene böler; karşılıklı iki üçgen eş alanlıdır ve taban oranı alan oranının karekökü gibi bulunur.','Yamuğun alanını iki bilinen üçgenin toplamı sanmak; yan üçgenleri bilinenlerden birine eşitlemek.','zor',6,'ui-bolge','Köşegen ve doğru parçalarıyla alan bölüşümü')
sy=.5; Dy,Cy=(0,0),(10,0); Ay,By=(1.8,8),(7.8,8); Oy=kesis(Ay,Cy,By,Dy)
Py=lambda p:(p[0]*sy,p[1]*sy)
ok(alan([Ay,Oy,By]),9); ok(alan([Cy,Oy,Dy]),25); ok(alan([Ay,Oy,Dy]),15); ok(alan([By,Oy,Cy]),15); ok(alan([Ay,By,Cy,Dy]),64)
f=F(); f.poly([Py(Ay),Py(By),Py(Cy),Py(Dy)]); f.line(Py(Ay),Py(Cy)); f.line(Py(By),Py(Dy)); f.par(Py(Ay),Py(By)); f.par(Py(Dy),Py(Cy))
f.node(Py(cen([Ay,Oy,By])),'$9$'); f.node(Py(cen([Cy,Oy,Dy])),'$25$')
f.vl('A',Py(Ay),(-1,.6),.3); f.vl('B',Py(By),(1,.6),.3); f.vl('C',Py(Cy),(1,-.6),.3); f.vl('D',Py(Dy),(-1,-.6),.3); f.vl('O',Py(Oy),(1,.15),.28)
SK=f.svg()
q('0008',tipId='ui-bolge',tip='Köşegen ve doğru parçalarıyla alan bölüşümü',z='zor',alt='Yamukta Alan',kaz='Yamuğun köşegenleriyle oluşan üçgenlerin alanlarından yamuğun alanını bulur.',
 kart='K-GUI-08 (yamuk, köşegenler, iki alan) · 9 ve 25',
 metin='Şekilde [AB] // [DC] olan ABCD yamuğunun köşegenleri O noktasında kesişmektedir. AOB üçgeninin alanı 9 cm², COD üçgeninin alanı 25 cm² dir.\nŞekil ölçekli değildir.\nBuna göre, ABCD yamuğunun alanı kaç cm² dir?',
 dogru=64,yan=[(34,'Yalnız verilen iki üçgenin alanlarını toplamış: 9 + 25 = 34.','dikkat'),(43,'AOD ve BOC üçgenlerinden yalnız birini hesaba katıp onu da 9 sanmış: 9 + 25 + 9 = 43.','dikkat'),(52,'AOD ve BOC üçgenlerinin her ikisini de 9 sanmış: 9 + 25 + 9 + 9 = 52.','bilgi'),(59,'AOD üçgenini 25 sanıp BOC üçgenini unutmuş: 9 + 25 + 25 = 59.','dikkat')],
 istenen='ABCD yamuğunun alanı (cm²).',
 ip=['Köşegenler yamuğu kaç üçgene böler, hangilerinin alanı bilinmiyor?'],
 bilgi=[BENZ,TABAN('Örnek: tabanı 10 cm, yüksekliği 3 cm olan üçgenin alanı 15 cm² dir')],
 ad=[A('Benzer üçgenleri bul','[AB] // [DC] olduğundan AOB ile COD üçgenleri benzerdir.','AOB ~ COD'),A('Benzerlik oranını bul','Alanlar oranı benzerlik oranının karesidir.','9 / 25 = k² → k = 3 / 5'),A('Yan üçgenleri bul','AOD ve AOB üçgenlerinin [BD] ye inen yüksekliği ortaktır; alanları |DO| : |OB| = 5 : 3 oranındadır. ABD ve ABC üçgenleri tabanı [AB] ve yüksekliği ortak olduğundan AOD = BOC dir.','AOD = 9 × 5 / 3 = 15 · BOC = 15'),A('Dört parçayı topla','Yamuk dört üçgenin birleşimidir.','9 + 25 + 15 + 15 = 64 cm²')],
 puf='Verilen iki alanla bulunamayan iki bölgeyi başka bir eşitlikten çıkarabilir misin? Aynı tabana ve aynı yüksekliğe sahip üçgenleri ara.',sekil=SK)

# ---- 09 · zor · eşkenar üçgende iç nokta
kartla('K-GUI-09','Eşkenar üçgende iç nokta ve dikmeler','İç noktayı köşelere bağlayınca oluşan üç üçgenin alanları toplamı, bütünün alanıdır; tabanlar eşit olduğundan yükseklikler toplanır.','Dikmelerin toplamını yüksekliğe eşitlemeyi gözden kaçırmak; yüksekliği kenar sanmak.','orta',5,'ui-ic-nokta','İç noktadan köşelere bölünen alanlar')
a9=8*sqrt(3); A9=(a9/2,12); B9=(0,0); C9=(a9,0)
P9=tuple((3*A9[i]+4*B9[i]+5*C9[i])/12 for i in range(2))
D9=foot(P9,B9,C9); E9=foot(P9,C9,A9); F9=foot(P9,A9,B9)
ok(dist(P9,D9),3); ok(dist(P9,E9),4); ok(dist(P9,F9),5); ok(dist(A9,B9),a9); ok(dist(B9,C9),a9); ok(dist(C9,A9),a9); ok(a9*sqrt(3)/2,12)
ok(alan([A9,B9,C9]),sum(a9*d/2 for d in (3,4,5)))
s9=.38; Q9=lambda p:(p[0]*s9,p[1]*s9)
f=F(); f.poly([Q9(A9),Q9(B9),Q9(C9)]); 
for X in (D9,E9,F9): f.line(Q9(P9),Q9(X))
f.dik(Q9(D9),Q9(P9),Q9(C9)); f.dik(Q9(E9),Q9(P9),Q9(A9)); f.dik(Q9(F9),Q9(P9),Q9(A9))
f.raw(f'\\fill {pt(Q9(P9))} circle (1.4pt);')
ic=Q9(cen([A9,B9,C9])); dim(f,Q9(B9),Q9(C9),'$8\\sqrt{3}$',(0,-1),.7)
def sidelab(t,X,Y):
    m=mid(Q9(X),Q9(Y)); d=un(sub(Q9(Y),Q9(X))); n=(-d[1],d[0])
    if n[0]*(m[0]-Q9(P9)[0])+n[1]*(m[1]-Q9(P9)[1])<0: n=(-n[0],-n[1])
    return n
f.node(add(mid(Q9(P9),Q9(D9)),(.25,0)),'$3$'); 
f.node(add(mid(Q9(P9),Q9(E9)),mul(un(sub(Q9(E9),Q9(P9))) if False else (.2,.22),1)),'$4$')
f.node(add(mid(Q9(P9),Q9(F9)),(-.2,.25)),'$x$')
f.vl('A',Q9(A9),(0,1),.3); f.vl('B',Q9(B9),(-1,-.6),.3); f.vl('C',Q9(C9),(1,-.6),.3); f.vl('P',Q9(P9),(-.3,.8),.28)
f.vl('D',Q9(D9),(0,-1),.3); f.vl('E',Q9(E9),(1,.5),.3); f.vl('F',Q9(F9),(-1,.5),.3)
SK=f.svg()
q('0009',tipId='ui-ic-nokta',tip='İç noktadan köşelere bölünen alanlar',z='orta',alt='Eşkenar Üçgende İç Nokta',kaz='Eşkenar üçgenin içindeki bir noktadan kenarlara inilen dikmelerin uzunlukları arasındaki ilişkiyi alan toplamıyla bulur.',
 kart='K-GUI-09 (eşkenar üçgen, iç nokta, üç dikme) · kenar 8√3',
 metin='Şekilde kenar uzunluğu 8√3 cm olan ABC eşkenar üçgeninin iç bölgesinde bir P noktası alınmıştır. P noktasından [BC], [CA] ve [AB] kenarlarına inilen dikmelerin ayakları sırasıyla D, E ve F dir. |PD| = 3 cm, |PE| = 4 cm ve |PF| = x cm dir.\nŞekil ölçekli değildir.\nBuna göre, x kaçtır?',
 dogru=5,yan=[(7,'Verilen iki uzaklığı toplayıp x sanmış: 3 + 4 = 7.','dikkat'),(8,'Yükseklikten yalnız |PE| yi çıkarmış: 12 − 4 = 8.','dikkat'),(9,'Yükseklikten yalnız |PD| yi çıkarmış: 12 − 3 = 9.','dikkat'),(12,'Üçgenin yüksekliğini (8√3 × √3 ÷ 2 = 12) x sanmış.','dikkat')],
 istenen='x = |PF| uzunluğu (cm).',
 ip=['Üçgenin alanını iki farklı yoldan yazabilir misin?'],
 bilgi=[ESK,TABAN('Örnek: tabanı 7 cm, yüksekliği 6 cm olan üçgenin alanı 21 cm² dir')],
 ad=[A('Yardımcı çizim yap','[PA], [PB] ve [PC] çizilirse ABC; PBC, PCA ve PAB üçgenlerine ayrılır. Yükseklikleri sırasıyla 3, 4 ve x tir.','Alan(ABC) = Alan(PBC) + Alan(PCA) + Alan(PAB)'),A('Yüksekliği bul','Kenarı 8√3 olan eşkenar üçgenin yüksekliği a√3 ÷ 2 dir.','h = 8√3 × √3 ÷ 2 = 12 cm'),A('Alanları yaz','Üç üçgenin tabanı da 8√3 tür; ortak çarpan dışarı alınır.','½ × 8√3 × 12 = ½ × 8√3 × (3 + 4 + x)'),A('Çöz','Eşitlikten ortak çarpanları sadeleştir.','12 = 3 + 4 + x → x = 5 cm')],
 puf='Şekilde çizilmeyen doğru parçalarını sen çiz: noktayı köşelerle birleştirince ortaya çıkan parçaların hepsini aynı yöntemle ele al.',sekil=SK)

# ---- 10 · zor · iki çevian, üç alan
kartla('K-GUI-10','İki doğru parçası ve üç alan','Kesişim noktasını üçüncü köşeye bağlayan yardımcı doğru, iki bilinmeyen alanlı denklem kurdurur.','Bilinen alanları toplayıp bütünden çıkarmaya çalışmak; ADP ile AEP üçgenlerini eş sanmak.','zor',6,'ui-bolge','Köşegen ve doğru parçalarıyla alan bölüşümü')
sc=.4; Bc,Cc,Ac=(0,0),(9,0),(2.5,10)
Dc=add(Ac,mul(sub(Bc,Ac),5/9)); Ec=add(Ac,mul(sub(Cc,Ac),3/5)); Pc=kesis(Bc,Ec,Cc,Dc)
ok(alan([Bc,Pc,Dc]),8); ok(alan([Bc,Pc,Cc]),12); ok(alan([Cc,Pc,Ec]),6); ok(alan([Ac,Dc,Pc,Ec]),19); ok(alan([Ac,Bc,Cc]),45)
Qc=lambda p:(p[0]*sc,p[1]*sc)
f=F(); f.fill([Qc(Ac),Qc(Dc),Qc(Pc),Qc(Ec)]); f.poly([Qc(Ac),Qc(Bc),Qc(Cc)]); f.line(Qc(Bc),Qc(Ec)); f.line(Qc(Cc),Qc(Dc))
f.node(Qc(cen([Bc,Pc,Dc])),'$8$'); f.node(Qc(cen([Bc,Pc,Cc])),'$12$'); f.node(Qc(cen([Cc,Pc,Ec])),'$6$')
f.vl('A',Qc(Ac),(0,1),.3); f.vl('B',Qc(Bc),(-1,-.6),.3); f.vl('C',Qc(Cc),(1,-.6),.3); f.vl('D',Qc(Dc),(-1,.2),.3); f.vl('E',Qc(Ec),(1,.3),.3); f.vl('P',Qc(Pc),(.2,.9),.28)
SK=f.svg()
q('0010',tipId='ui-bolge',tip='Köşegen ve doğru parçalarıyla alan bölüşümü',z='zor',alt='Üçgende Bölünen Alanlar',kaz='Üçgen içinde kesişen iki doğru parçasının oluşturduğu bölgelerin alanlarından bilinmeyen dörtgenin alanını bulur.',
 kart='K-GUI-10 (iki doğru parçası, üç alan, dörtgen) · 8, 12, 6',
 metin='Şekilde ABC üçgeninin [AB] kenarı üzerinde D, [AC] kenarı üzerinde E noktası alınmıştır. [BE] ile [CD] doğru parçaları P noktasında kesişmektedir. BPD, BPC ve CPE üçgenlerinin alanları cm² cinsinden şekilde verilmiştir.\nŞekil ölçekli değildir.\nBuna göre, taralı ADPE dörtgeninin alanı kaç cm² dir?',
 dogru=19,yan=[(12,'ADPE dörtgenini BPC üçgenine eş alanlı sanmış.','bilgi'),(14,'Verilen BPD ve CPE alanlarını toplayıp dörtgenin alanı saymış: 8 + 6 = 14.','dikkat'),(24,'ADP ve AEP üçgenlerini eş alanlı alıp (x = y) 12 + 12 = 24 bulmuş.','islem'),(26,'Verilen üç alanı toplayıp bırakmış: 8 + 12 + 6 = 26.','dikkat')],
 istenen='Taralı ADPE dörtgeninin alanı (cm²).',
 ip=['ADPE dörtgenini [AP] ile iki üçgene ayırsan bu üçgenlerin alanları için hangi ortak yükseklik oranlarını yazabilirsin?'],
 bilgi=[TABAN('Örnek: tabanı 14 cm, yüksekliği 5 cm olan üçgenin alanı 35 cm² dir')],
 ad=[A('Yardımcı çizim yap','[AP] çizilir; ADP üçgeninin alanı x, AEP üçgeninin alanı y olsun.','ADPE = x + y'),A('C den D ye oran','A ve B den [CD] ye inen yükseklikler için ADP, APC ve BPD, BPC üçgenlerinde [DP] : [PC] oranı ortaktır.','DP : PC = 8 : 12 = 2 : 3 → x ÷ (y + 6) = 2 ÷ 3'),A('B den E ye oran','Aynı biçimde [BE] üzerinde [EP] : [PB] oranı.','EP : PB = 6 : 12 = 1 : 2 → y ÷ (x + 8) = 1 ÷ 2'),A('Denklemleri çöz','İlk denklemden 3x = 2y + 12, ikinciden 2y = x + 8.','3x = x + 8 + 12 → x = 10 → y = 9'),A('Dörtgeni topla','ADPE = x + y.','10 + 9 = 19 cm²')],
 puf='Doğrudan bulamadığın bölgeyi iki bilinmeyenle adlandır ve alanlarını oranlarla iki farklı yoldan yaz.',sekil=SK)
bitir_geo(ONEK,KONU_AD)
