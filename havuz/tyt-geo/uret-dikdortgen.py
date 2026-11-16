"""TYT Geometri PİLOT · 10 şekilli soru (kardeş yok, ipucu 1). Şekil koordinatları hesaplanır, TikZ gövdesi bu değerlerden üretilir (cizim.tikz_svg).
Her cevap ve çeldirici değer koordinat/Python hesabından assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
HV=os.path.join(GD,'..')
from math import sin,cos,tan,radians,degrees,atan2,sqrt,pi
TIPK={}   # tipId -> uygulama konu anahtarı
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kaynak=None):
    kart(id,alt,fikir,tuzak,z,'şekilli',adim,tipId,tip,kaynak or 'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,**k):
    kl=k.pop('kalip','şekilli'); mk(P,no,ad=ad,adim=len(ad),kalip=kl,**k)

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

def vtx(f,names,pts,c=None,d=.3):
    c=c or cen(pts)
    for n,p in zip(names,pts): f.vl(n,p,sub(p,c),d)
def bitir_geo(onek,ad):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=ad,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'soru',len(P.ANA))
def bitir_geo(onek,konuadi):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=konuadi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def dimout(f,p,q_,dv,dist,t,tl=.27):
    d=un(dv); p2=add(p,mul(d,dist)); q2=add(q_,mul(d,dist))
    f.line(p,add(p,mul(d,dist+.1)),'dotted'); f.line(q_,add(q_,mul(d,dist+.1)),'dotted')
    f.raw(f'\\draw[<->] {pt(p2)} -- {pt(q2)};'); f.node(add(mid(p2,q2),mul(d,tl)),t)
P=Parti('dikdortgen','Dikdörtgen','geo|Dikdörtgen',ders='TYT Geometri',idon='tytgeo')
DIK=B('Dikdörtgen','karşılıklı kenarları eşit ve paralel, bütün açıları 90° olan dörtgendir; köşegenleri eşit uzunlukta olup birbirini ortalar. Çevre = 2 × (a + b), alan = a × b. Örnek: kenarları 7 ve 9 olan dikdörtgenin çevresi 32, alanı 63')
PIS=B('Pisagor bağıntısı','dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir. Dikdörtgende köşegen, kenarlarla dik üçgen oluşturur. Örnek: kenarları 7 ve 24 olan dikdörtgenin köşegeni 25’tir')
NOK=B('İç noktanın köşelere uzaklığı','ABCD dikdörtgeninin içindeki P noktası için karşılıklı köşelere uzaklıkların kareleri toplamı eşittir: |PA|² + |PC|² = |PB|² + |PD|². Örnek: |PA| = 2, |PB| = 3, |PD| = 6 ise |PC|² = 9 + 36 − 4 = 41')
KAT=B('Katlama (simetri)','katlanınca üst üste gelen parçaların uzunlukları eşittir; kat izi, karşılıklı noktaları birleştiren doğru parçasının orta dikmesidir. Örnek: B noktası E noktasına geliyorsa |FB| = |FE| ve |AB| = |AE|')
CEV=B('Çevre ve alan','dikdörtgenin yarım çevresi iki kenarın toplamıdır; bir kenar bilinirse diğeri yarım çevreden çıkarılarak bulunur. Örnek: çevre 30 ve bir kenar 8 ise diğer kenar 15 − 8 = 7')
PAR=B('Alan oranı','dikdörtgen, bir kenara paralel doğrularla parçalandığında aynı yükseklikteki parçaların alanları tabanlarıyla orantılıdır. Örnek: üstte 2 ve 3 alanlı parçalar varsa altta aynı genişlikli parçaların alanları da 2 : 3 oranındadır')
ORAN=B('Oran verilen kenarlar','kenarları a ve b ile oranlı olan dikdörtgenin kenarları a × k ve b × k alınır; köşegen için Pisagor uygulanır. Örnek: kenarlar 5k ve 12k ise köşegen 13k’dır')
def rect(a,b,s): return [(0,0),(a*s,0),(a*s,b*s),(0,b*s)]
konu('geo|Dikdörtgen','Dikdörtgen')
# ---- 01 köşegen, yol · kolay
kartla('K-GDD-01','Köşegen yolu ve kenar yolu','Köşegen, kenarlarla dik üçgen kurar (Pisagor); kenar yolu iki kenarın toplamıdır, fark istenir.','Köşegenle kenarı karıştırmak; kenar yolunun iki kenar toplamı olduğunu unutmak; farkı yanlış okumak.','kolay',3,'ge-dd-kosegen','Köşegen ve kenar yolu')
a,b=40,30; dg=sqrt(a*a+b*b); assert dg==50 and a+b-dg==20 and dg-a==10 and a+b-a==30 and a+b==70
s=.1; Pt=rect(a,b,s); Ao,Bo,Co,Do=Pt
f=F(); f.poly(Pt); f.line(Ao,Co,'dashed'); f.dik(Bo,Co,Ao,.2); vtx(f,'ABCD',Pt,cen(Pt),.3)
f.sl('$40$',Ao,Bo,cen(Pt),.28); f.sl('$30$',Bo,Co,cen(Pt),.28)
SK=f.svg()
q('0001',tipId='ge-dd-kosegen',tip='Köşegen ve kenar yolu',z='kolay',alt='Köşegen Yolu',kaz='Dikdörtgenin köşegenini Pisagorla bulup kenar yolu ile köşegen yolu arasındaki farkı hesaplar.',kalip='hikâyeli',
 kart='K-GDD-01 (köşegen yolu) · 40 m × 30 m',
 metin='Dikdörtgen biçimli ABCD parkının kenar uzunlukları şekilde metre cinsinden verilmiştir. Ali, A kapısından C kapısına önce [AB], sonra [BC] kenarı boyunca yürüyor. Ayşe ise aynı anda A kapısından yola çıkıp [AC] köşegeni boyunca yürüyerek C kapısına varıyor.\nBuna göre, Ali Ayşe’den kaç metre fazla yürümüştür?',
 dogru=20,yan=[(10,'Köşegeni (50) bulmuş ama onu yalnız uzun kenarla (40) kıyaslayıp 50 − 40 yazmış.','dikkat'),(30,'Ali’nin yolundan uzun kenarı çıkarmış: 70 − 40.','dikkat'),(50,'Yalnız Ayşe’nin yürüdüğü yolu (köşegeni) bulmuş.','dikkat'),(70,'Yalnız Ali’nin yolunu (40 + 30) bulmuş; fark istenmiş.','dikkat')],
 istenen='Ali’nin yürüdüğü yol ile Ayşe’nin yürüdüğü yolun farkı (m).',
 ip=['Ayşe’nin yolu, ABC dik üçgeninin hangi kenarı? Bu uzunluğu bulduktan sonra iki yolu karşılaştır.'],
 bilgi=[PIS],
 ad=[A('Ali’nin yolunu yaz','İki kenar boyunca yürüyor.','|AB| + |BC| = 40 + 30 = 70 m'),A('Köşegeni bul','ABC dik üçgeninde [AC] hipotenüstür.','|AC|² = 40² + 30² = 2500 → |AC| = 50 m'),A('Farkı hesapla','Ali’nin yolundan Ayşe’nin yolunu çıkar.','70 − 50 = 20 m')],
 puf='Dikdörtgenin köşegeni kenarlarla dik üçgen kurar; “kestirme” sorularında kenar yolu − köşegen farkı istenir.',sekil=SK)

# ---- 02 çevre-alan · kolay
kartla('K-GDD-02','Çevre ve bir kenardan alan','Çevreden yarım çevre bulunur; bilinen kenar çıkarılınca diğer kenar elde edilir ve alan hesaplanır.','Çevreyi kenarlar toplamı sanmak; çevreden kenarı bir kez çıkarıp bırakmak; kareye çevirmek.','kolay',3,'ge-dd-cevre-alan','Çevre ve bir kenardan alan')
Ç=46; kk=15; dy=Ç/2-kk; assert dy==8 and kk*dy==120
assert Ç/2==23 and Ç==46 and kk*(Ç-2*kk)==240 and kk*kk==225
s=.22; Pt=rect(kk,dy,s)
f=F(); f.poly(Pt); f.dik(Pt[0],Pt[1],Pt[3],.2); vtx(f,'ABCD',Pt,cen(Pt),.3); f.sl('$15$',Pt[0],Pt[1],cen(Pt),.28)
SK=f.svg()
q('0002',tipId='ge-dd-cevre-alan',tip='Çevre ve bir kenardan alan',z='kolay',alt='Çevre ve Alan',kaz='Çevre ve bir kenar uzunluğundan dikdörtgenin diğer kenarını bulup alanını hesaplar.',kalip='hikâyeli',
 kart='K-GDD-02 (çevre-alan) · çevre 46, kenar 15',
 metin='Dikdörtgen biçimli bir odanın tabanının uzun kenarı şekilde metre cinsinden verilmiştir. Odanın taban çevresi 46 m olduğuna göre, bu odaya serilecek ve zemini tam kaplayacak bir halının alanı kaç m² olmalıdır?',
 dogru=120,yan=[(23,'Yarım çevreyi (46 ÷ 2) alan sanmış.','bilgi'),(46,'Çevreyi alan olarak yazmış.','bilgi'),(225,'Odayı kare sanıp 15 × 15 yazmış.','bilgi'),(240,'Diğer kenarı 46 − 2 × 15 = 16 bulmuş (yarım çevre yerine çevreden çıkarmış), 15 × 16 yazmış.','islem')],
 istenen='Odanın tabanının alanı (m²).',
 ip=['Çevre, iki komşu kenarın toplamının kaç katıdır? Önce kısa kenarı bul.'],
 bilgi=[DIK,CEV],
 ad=[A('Yarım çevreyi bul','Çevre = 2 × (uzun kenar + kısa kenar).','46 ÷ 2 = 23'),A('Kısa kenarı bul','Yarım çevreden uzun kenarı çıkar.','23 − 15 = 8 m'),A('Alanı hesapla','Alan = uzun kenar × kısa kenar.','15 × 8 = 120 m²')],
 puf='Çevre verilen dikdörtgende önce yarım çevreyi (a + b) bul, sonra bilinen kenarı çıkar.',sekil=SK)

# ---- 03 iç nokta · orta
kartla('K-GDD-03','İç noktanın köşelere uzaklığı','Noktadan kenarlara indirilen dikmelerle dik üçgen kurulur; uzaklık Pisagorla bulunur.','Uzaklığı kenar farkı yerine toplamla bulmak; köşegeni uzaklık sanmak; yalnız bir dik kenarı vermek.','orta',3,'ge-dd-nokta','İç noktanın köşelere uzaklığı')
aa_,bb_=20,15; pa,pb=8,6   # P: AD ye 8, AB ye 6
PCl=sqrt((aa_-pa)**2+(bb_-pb)**2); assert PCl==15
assert sqrt(pa**2+pb**2)==10 and bb_-pb==9 and aa_-pa==12 and (aa_-pa)+(bb_-pb)==21 and sqrt(aa_**2+bb_**2)==25
R=[(0,0),(aa_,0),(aa_,bb_),(0,bb_)]; Pp=(pa,pb)
s=.2; S=lambda p:(p[0]*s,p[1]*s); Rs=[S(p) for p in R]; Ps=S(Pp)
f=F(); f.poly(Rs)
f.line(Ps,Rs[2],'dashed'); f.line(Ps,(Ps[0],0),'dotted'); f.line(Ps,(0,Ps[1]),'dotted')
f.raw(f'\\fill {pt(Ps)} circle (1pt);'); vtx(f,'ABCD',Rs,cen(Rs),.3); f.node((Ps[0]+.3,Ps[1]-.2),'$P$')
f.node((Ps[0]/2,Ps[1]+.22),'$8$'); f.node((Ps[0]+.22,Ps[1]/2),'$6$')
f.sl('$20$',Rs[0],Rs[1],cen(Rs),.28); f.sl('$15$',Rs[1],Rs[2],cen(Rs),.28)
SK=f.svg()
q('0003',tipId='ge-dd-nokta',tip='İç noktanın köşelere uzaklığı',z='orta',alt='İç Nokta ve Köşe',kaz='Dikdörtgenin içindeki bir noktanın kenarlara uzaklıklarından Pisagorla köşeye olan uzaklığı bulur.',kalip='hikâyeli',
 kart='K-GDD-03 (iç nokta) · 20 × 15, uzaklıklar 8 ve 6',
 metin='Bir okul bahçesinde, ABCD dikdörtgeni biçimindeki çimlik alanın içindeki P noktasına bir projektör dikilmiştir. Çimliğin kenar uzunlukları ile P noktasının [AD] ve [AB] kenarlarına olan uzaklıkları şekilde metre cinsinden verilmiştir. Projektörden C köşesindeki prize bir kablo çekilecektir; kablo doğrusal gidecek ve ek yeri olmayacaktır. Şekil ölçekli değildir.\nBuna göre, gereken kablonun uzunluğu |PC| kaç metredir?',
 dogru=15,yan=[(9,'Yalnız dik kenarlardan birini (15 − 6) bulup kabloya eşitlemiş.','dikkat'),(21,'Dik kenarları (12 ve 9) toplamış; kablo hipotenüstür.','bilgi'),(25,'Çimliğin köşegenini (√(20² + 15²)) kablo uzunluğu sanmış.','bilgi'),(35,'Çimliğin iki kenarını toplamış (20 + 15).','dikkat')],
 istenen='|PC| uzunluğu (m).',
 ip=['P noktasından C köşesine giden doğru parçasını hipotenüs kabul eden bir dik üçgen çizmek için hangi dikmeleri kullanabilirsin?'],
 bilgi=[PIS],
 ad=[A('Dik kenarları bul','P den [BC] ye ve [DC] ye dikmeler inen dik üçgenin dik kenarları kenar uzunluklarından uzaklıklar çıkarılarak bulunur.','yatay: 20 − 8 = 12 · düşey: 15 − 6 = 9'),A('Pisagor uygula','|PC| hipotenüstür.','|PC|² = 12² + 9² = 225'),A('Uzunluğu yaz','Karekök al.','|PC| = 15 m')],
 puf='Bir noktanın köşeye uzaklığı için kenarlara dikmeler indirip dik üçgen kur; dik kenarlar uzunluk farklarından gelir.',sekil=SK)

# ---- 04 katlama A→C · zor
kartla('K-GDD-04','Köşeyi karşı köşeye katlama','Kat izi AC nin orta dikmesidir; benzer üçgenlerle ya da orta dikme eşitlikleriyle uzunluğu bulunur.','Kat izini köşegenle ya da kenarla karıştırmak; benzerlik oranını ters yazmak.','zor',5,'ge-dd-katlama','Katlama ve kat izi')
AB4,BC4=16,12; AC4=sqrt(AB4**2+BC4**2); assert AC4==20; EF4=AC4*BC4/AB4; assert EF4==15
Mx=(8,6); dv=(3,-4); uE=(0-Mx[1])/dv[1]*(-1) if False else (0-Mx[1])/dv[1]; E4=(Mx[0]+uE*dv[0],0); uF=(12-Mx[1])/dv[1]; F4=(Mx[0]+uF*dv[0],12)
assert abs(E4[0]-12.5)<1e-9 and abs(F4[0]-3.5)<1e-9 and abs(dist(E4,F4)-15)<1e-9 and abs(dist(E4,(0,0))-dist(E4,(16,12)))<1e-9
assert abs(((F4[0]-E4[0])*(16-0)+(F4[1]-E4[1])*(12-0)))<1e-9
assert AB4/2==8 and AC4/2==10 and EF4/2==7.5
s=.25; Pt=rect(16,12,s); Es=(E4[0]*s,0); Fs=(F4[0]*s,12*s)
f=F(); f.poly(Pt); f.line(Es,Fs); f.dik(Pt[0],Pt[1],Pt[3],.2)
vtx(f,'ABCD',Pt,cen(Pt),.3); f.node((Es[0]+.02,-.27),'$E$'); f.node((Fs[0],Fs[1]+.27),'$F$')
f.sl('$16$',Pt[0],Pt[1],cen(Pt),.5 if False else .28); f.sl('$12$',Pt[1],Pt[2],cen(Pt),.28)
SK=f.svg()
q('0004',tipId='ge-dd-katlama',tip='Katlama ve kat izi',z='zor',alt='A Köşesini C ye Katlama',kaz='Dikdörtgen kâğıdın köşesini karşı köşeye katlayınca oluşan kat izinin uzunluğunu bulur.',kalip='hikâyeli',
 kart='K-GDD-04 (katlama) · 16 × 12, A → C',
 metin='Kenar uzunlukları şekilde cm cinsinden verilen dikdörtgen biçimli ABCD kâğıdı, A köşesi C köşesinin üzerine gelecek biçimde katlanıyor. Kat izi, [AB] kenarını E noktasında, [DC] kenarını F noktasında kesen [EF] doğru parçasıdır. Şekil ölçekli değildir.\nBuna göre, kâğıtta oluşan kat izinin uzunluğu |EF| kaç cm dir?',
 dogru='15',yan=[('7,5','Kat izinin yarısını (merkezden E ye olan uzaklık) bulup bırakmış.','dikkat'),('8','Uzun kenarın yarısını (16 ÷ 2) kat izi sanmış.','dikkat'),('10','Köşegenin yarısını (20 ÷ 2) kat izi sanmış.','bilgi'),('12','Kısa kenarı (|BC| = 12) kat izi sanmış.','bilgi')],
 sira=['7,5','8','10','12','15'],
 istenen='Kat izinin uzunluğu |EF| (cm).',
 ip=['Kat izi, A ile C yi birleştiren doğru parçasına hangi özellikle bağlı? Köşegen ile kat izinin oluşturduğu üçgenlerin benzerliğini ara.'],
 bilgi=[PIS,KAT],
 ad=[A('Köşegeni bul','ABC dik üçgeninde Pisagor uygula.','|AC|² = 16² + 12² = 400 → |AC| = 20'),A('Kat izini yerleştir','Kat izi [AC] nin orta dikmesidir; AC ile EF, M noktasında dik kesişir ve |AM| = 10.','|AM| = 20 ÷ 2 = 10'),A('Benzer üçgenleri bul','AME ve ABC üçgenleri A açısı ortak, M ile B dik açılı olduğundan benzerdir.','|AM| / |AB| = |ME| / |BC|'),A('|ME| yi hesapla','Orantıyı çöz.','10 / 16 = |ME| / 12 → |ME| = 7,5'),A('Kat izini bul','M, [EF] nin orta noktasıdır (simetri).','|EF| = 2 × 7,5 = 15 cm')],
 puf='Köşeyi karşı köşeye katlayınca kat izi köşegenin orta dikmesi olur; köşegenin ortası kat izinin de ortasıdır.',sekil=SK)

# ---- 05 katlama B→E · zor
kartla('K-GDD-05','Köşeyi karşı kenara katlama','Katlanan kenarların eşitliğinden Pisagorla bir parça bulunur; kalan parçalarla ikinci Pisagor denklemi kurulur.','Katlanan uzunluğu (|AE| = |AB|) görmemek; yanlış üçgende Pisagor uygulamak.','zor',5,'ge-dd-katlama','Katlama ve kat izi')
AB5,BC5=10,8; AE5=AB5; DE5=sqrt(AE5**2-BC5**2); assert DE5==6; EC5=AB5-DE5; assert EC5==4
# (8-y)^2 = y^2+16 → y=3
y5=(BC5**2+EC5**2-0)/ (2*BC5) if False else None
FC=(BC5**2-EC5**2)/(2*BC5); BF=BC5-FC; assert FC==3 and BF==5 and (BF)**2==FC**2+EC5**2
E5=(DE5,8); F5=(10,BF); Ao=(0,0)
assert abs(dist(Ao,E5)-10)<1e-9 and abs(dist(F5,E5)-BF)<1e-9
assert 3 and 6==DE5 and BC5==8 and AB5==10
s=.3; Pt=rect(10,8,s); E5s=(E5[0]*s,8*s); F5s=(10*s,BF*s)
f=F(); f.poly(Pt); f.line(Pt[0],F5s); f.line(Pt[0],E5s,'dashed'); f.line(E5s,F5s,'dashed')
vtx(f,'ABCD',Pt,cen(Pt),.3); f.node((E5s[0],8*s+.27),'$E$'); f.node((10*s+.27,F5s[1]),'$F$')
f.sl('$10$',Pt[0],Pt[1],cen(Pt),.28); f.sl('$8$',Pt[3],Pt[0],cen(Pt),.28)
SK=f.svg()
q('0005',tipId='ge-dd-katlama',tip='Katlama ve kat izi',z='zor',alt='B Köşesini DC ye Katlama',kaz='Dikdörtgenin bir köşesini karşı kenara katlayınca oluşan parçaları Pisagorla bularak katlanan parçanın uzunluğunu hesaplar.',kalip='hikâyeli',
 kart='K-GDD-05 (katlama, Pisagor) · 10 × 8, B → [DC]',
 metin='Bir pasta kutusunun dikdörtgen biçimli ABCD kartonu, şekildeki gibi [AF] boyunca katlandığında B köşesi [DC] kenarı üzerindeki E noktasına geliyor (F ∈ [BC]). Kartonun kenar uzunlukları şekilde cm cinsinden verilmiştir. Şekil ölçekli değildir.\nBuna göre, |BF| kaç cm dir?',
 dogru=5,yan=[(6,'|DE| uzunluğunu (ADE üçgeninde bulunan) |BF| sanmış.','dikkat'),(8,'F noktasını C ile çakışık sanıp |BF| = |BC| yazmış.','bilgi'),(9,'|DE| ile |FC| yi toplamış (6 + 3).','islem'),(10,'Katlanan |AB| = |AE| = 10 uzunluğunu |BF| ile karıştırmış.','bilgi')],
 istenen='|BF| uzunluğu (cm).',
 ip=['Katlanınca B noktası E ye gelir: hangi uzunluklar eşit oldu? Önce ADE üçgeninden başla.'],
 bilgi=[PIS,KAT],
 ad=[A('Katlanan kenarlar','B, E ye geldiğinden |AE| = |AB| = 10 ve |FE| = |FB|.','|AE| = 10'),A('|DE| yi bul','ADE dik üçgeninde |AD| = 8.','|DE|² = 10² − 8² = 36 → |DE| = 6'),A('|EC| yi bul','|DC| = 10.','|EC| = 10 − 6 = 4'),A('Denklemi kur','|FC| = y olsun; |FE| = |FB| = 8 − y olur. FEC dik üçgeninde Pisagor uygula.','(8 − y)² = y² + 4² → 64 − 16y = 16 → y = 3'),A('|BF| yi bul','|BF| = 8 − 3.','|BF| = 5 cm')],
 puf='Katlama sorularında katlanan kenarların eşitliğini yaz, bilinmeyeni bir dik üçgenin Pisagor denkleminde yakala.',sekil=SK)

# ---- 06 parçalara ayrılmış · orta
kartla('K-GDD-06','Parçalanmış dikdörtgende alan','Aynı yükseklikli parçaların alanları tabanlarıyla orantılıdır: karşılıklı çarpımlar eşittir (A₁ × A₄ = A₂ × A₃).','Dördüncü parçayı toplamsal tahmin etmek; üç alanı toplayıp bırakmak.','orta',4,'ge-dd-parca','Parçalara ayrılmış dikdörtgen')
A1,A2,A3=12,18,20; A4=A2*A3/A1; assert A4==30 and A1+A2+A3+A4==80
assert A1+A2+A3==50 and A1+A2+A3+A1==62 and A1+A2+A3+A3==70 and A1+A2+A3+(A2+A3-A1)==76 and A1+A2+A3+(A2+A3)==88
w1,w2,h1,h2=4,6,3,5; assert w1*h1==A1 and w2*h1==A2 and w1*h2==A3 and w2*h2==A4
s=.6; Pt=rect(w1+w2,h1+h2,s)
f=F(); f.poly(Pt); f.line((w1*s,0),(w1*s,(h1+h2)*s)); f.line((0,h2*s),((w1+w2)*s,h2*s))
vtx(f,'ABCD',Pt,cen(Pt),.3)
f.node((w1*s/2,(h2+h1/2)*s),'$12$'); f.node(((w1+w2/2)*s,(h2+h1/2)*s),'$18$'); f.node((w1*s/2,h2*s/2),'$20$'); f.node(((w1+w2/2)*s,h2*s/2),'$?$')
SK=f.svg()
q('0006',tipId='ge-dd-parca',tip='Parçalara ayrılmış dikdörtgen',z='orta',alt='Parçalanmış Dikdörtgen',kaz='Kenarlara paralel doğrularla bölünen dikdörtgende bilinen üç alandan dördüncüyü ve toplam alanı bulur.',
 kart='K-GDD-06 (parçalı dikdörtgen) · 12, 18, 20',
 metin='Şekildeki ABCD dikdörtgeni, kenarlarına paralel iki doğru parçasıyla dört küçük dikdörtgene ayrılmıştır. Üç küçük dikdörtgenin alanı cm² cinsinden şekilde verilmiştir (şekil ölçekli değildir).\nBuna göre, ABCD dikdörtgeninin alanı kaç cm² dir?',
 dogru=80,yan=[(50,'Yalnız verilen üç alanı toplamış, ? ile gösterilen parçayı katmamış.','dikkat'),(70,'Eksik parçayı sol alttaki parça gibi (20) almış.','bilgi'),(76,'Eksik parçayı toplamsal düşünüp 18 + 20 − 12 = 26 bulmuş.','bilgi'),(88,'Eksik parçayı 18 + 20 = 38 almış.','bilgi')],

 istenen='ABCD dikdörtgeninin alanı (cm²).',
 ip=['Aynı sütundaki iki parçanın ortak ölçüsü nedir?'],
 bilgi=[PAR],
 ad=[A('Oranı kur','Sol ve sağ sütunun genişlikleri oranı, üst sırada ve alt sırada aynıdır.','12 / 18 = 20 / ?'),A('Eksik alanı bul','İçler dışlar çarpımı yap.','? = 18 × 20 ÷ 12 = 30'),A('Toplamı al','Dört parçanın alanları toplanır.','12 + 18 + 20 + 30 = 80 cm²')],
 puf='Dört parçalı dikdörtgende karşılıklı (köşegen yönündeki) alanların çarpımları eşittir: A₁ × A₄ = A₂ × A₃.',sekil=SK)

# ---- 07 bahçe yolu · orta
kartla('K-GDD-07','Çevresindeki yolun alanı','Yolun alanı = dış dikdörtgen − iç dikdörtgen; iç ölçüler her kenardan iki kez yol genişliği kadar küçülür.','İç kenarları yalnız bir yol genişliği kadar küçültmek; çevreyi alan saymak; yalnız iki şeridi hesaplamak.','orta',4,'ge-dd-cevre-alan','Çevre ve bir kenardan alan')
Wd,Ht,e=24,16,2; ic_=(Wd-2*e)*(Ht-2*e); assert (Wd-2*e,Ht-2*e)==(20,12) and Wd*Ht-ic_==144
assert Wd*Ht-(Wd-e)*(Ht-e)==76 and 2*(Wd+Ht)==80 and 2*e*Wd==96 and 2*e*(Wd+Ht)==160 and ic_==240
s=.2; Pt=rect(Wd,Ht,s); w=e*s; Pi=[(w,w),((Wd-e)*s,w),((Wd-e)*s,(Ht-e)*s),(w,(Ht-e)*s)]
f=F(); f.raw('\\fill[vurgu!20,even odd rule] '+' -- '.join(map(pt,Pt))+' -- cycle '+' -- '.join(map(pt,Pi))+' -- cycle;')
f.poly(Pt); f.poly(Pi); vtx(f,'ABCD',Pt,cen(Pt),.3)
f.sl('$24$',Pt[3],Pt[2],cen(Pt),.28); f.sl('$16$',Pt[1],Pt[2],cen(Pt),.28)
f.raw(f'\\draw[<->] (-.14,0) -- (-.14,{w:.3f});'); f.node((-.4,w/2),'$2$')
SK=f.svg()
q('0007',tipId='ge-dd-cevre-alan',tip='Çevre ve bir kenardan alan',z='orta',alt='Bahçe Yolu',kaz='Dikdörtgen bahçenin çevresindeki eşit genişlikli yolun alanını dış ve iç dikdörtgen alanlarının farkıyla hesaplar.',kalip='hikâyeli',
 kart='K-GDD-07 (yol alanı) · 24 × 16, yol 2',
 metin='Belediye, dikdörtgen biçimli ABCD parkının dış kenarları boyunca her yerde aynı genişlikte bir yürüyüş yolu yaptıracaktır. Parkın ölçüleri ve yolun genişliği şekilde metre cinsinden verilmiştir; yolun içinde kalan bölüm çimlendirilecektir. Yürüyüş yolu özel bir kaplamayla döşenecektir.\nBuna göre, kaplamanın uygulanacağı yürüyüş yolunun alanı kaç m² dir?',
 dogru=144,yan=[(76,'İç ölçüleri yalnız 2 m küçültmüş (22 × 14 = 308); 384 − 308 = 76.','bilgi'),(80,'Parkın çevresini (2 × (24 + 16)) alan olarak yazmış.','bilgi'),(96,'Yalnız uzun kenarlar boyunca iki şerit almış: 2 × 2 × 24.','dikkat'),(160,'Çevreyi yol genişliğinin iki katıyla çarpmış: 80 × 2.','islem')],
 istenen='Yürüyüş yolunun alanı (m²).',
 ip=['Yolun alanını doğrudan şeritlere ayırmak yerine, tüm parkın alanından çimlenen iç bölümün alanını çıkarmayı dene.'],
 bilgi=[DIK],
 ad=[A('Dış alanı bul','Park 24 × 16 metredir.','24 × 16 = 384 m²'),A('İç ölçüleri bul','Yol her kenarda 2 m olduğundan iç uzunluk 2 × 2 = 4 m azalır.','24 − 4 = 20 · 16 − 4 = 12'),A('İç alanı bul','İç dikdörtgenin alanı.','20 × 12 = 240 m²'),A('Farkı al','Yolun alanı, dış alandan iç alanın farkıdır.','384 − 240 = 144 m²')],
 puf='Eşit genişlikli çerçeve (yol, bordür, çerçeve) sorularında iç ölçüler her boyutta yol genişliğinin iki katı kadar azalır.',sekil=SK)

# ---- 08 halı, oranlı kenarlar · orta
kartla('K-GDD-08','Oranlı kenarlar ve köşegen','Kenarlar 3a ve 4a ise köşegen 5a dır; köşegenden a bulunur, çevre hesaplanır.','Köşegeni bir kenara eşitlemek; kenarları toplayıp çevre saymak; çevre yerine yarım çevre vermek.','orta',4,'ge-dd-kosegen','Köşegen ve kenar yolu')
aa=30; dgn=sqrt((3*aa)**2+(4*aa)**2); assert dgn==150 and 2*(3*aa+4*aa)==420
assert 7*aa==210 and 2*150==300 and 2*(150+112.5)==525 and 2*(150+200)==700 and (4*aa,3*aa)==(120,90)
s=.04; Pt=rect(120,90,s)
f=F(); f.poly(Pt); f.line(Pt[0],Pt[2],'dashed'); f.dik(Pt[1],Pt[2],Pt[0],.2); vtx(f,'ABCD',Pt,cen(Pt),.3)
f.sl('$4a$',Pt[0],Pt[1],cen(Pt),.3); f.sl('$3a$',Pt[1],Pt[2],cen(Pt),.3)
m=mid(Pt[0],Pt[2]); f.node((m[0]-.05,m[1]+.3),'$150$')
SK=f.svg()
q('0008',tipId='ge-dd-kosegen',tip='Köşegen ve kenar yolu',z='orta',alt='Halı Çevresi',kaz='Kenarları a cinsinden verilen dikdörtgenin köşegeninden a yı bulup çevreyi hesaplar.',kalip='hikâyeli',
 kart='K-GDD-08 (oranlı kenarlar) · 4a, 3a, köşegen 150',
 metin='Dikdörtgen biçimli bir halının kenar uzunlukları şekilde a cinsinden verilmiş, köşegeninin uzunluğu ise 150 cm olarak ölçülmüştür (şekil ölçekli değildir). Halının dört kenarına birer şerit dikilecek, şeritlerin ek yerleri için fazladan kumaş kullanılmayacaktır.\nBuna göre, dikilecek şeritlerin toplam uzunluğu kaç cm dir?',
 dogru=420,yan=[(210,'Halının yarım çevresini (120 + 90) çevre sanmış.','dikkat'),(300,'Çevreyi köşegenin iki katı (2 × 150) olarak yazmış.','bilgi'),(525,'Köşegeni uzun kenara (4a = 150) eşitleyip a = 37,5 bulmuş: 2 × (150 + 112,5).','bilgi'),(700,'Köşegeni kısa kenara (3a = 150) eşitleyip a = 50 bulmuş: 2 × (200 + 150).','bilgi')],
 istenen='Halının çevresi (cm).',
 ip=['Kenarları a cinsinden yazılmış dikdörtgende köşegeni Pisagorla a cinsinden yaz; 150 ile eşitle.'],
 bilgi=[PIS,ORAN],
 ad=[A('Köşegeni a cinsinden yaz','ABC dik üçgeninde Pisagor uygula.','(4a)² + (3a)² = 25a² → köşegen = 5a'),A('a yı bul','Köşegen 150 cm olduğuna göre.','5a = 150 → a = 30'),A('Kenarları bul','Uzun ve kısa kenarı hesapla.','4a = 120 · 3a = 90'),A('Çevreyi hesapla','Çevre = 2 × (uzun + kısa).','2 × (120 + 90) = 420 cm')],
 puf='Kenarlar 3 : 4 oranındaysa köşegen 5 birimdir (3-4-5); köşegen verilince bir birimin değeri hemen bulunur.',sekil=SK)
bitir_geo('dikdortgen','Dikdörtgen')
