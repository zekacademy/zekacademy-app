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

TIPK={}
def konu(k,ad): P.k=k; P.konu_adi=ad; H.KONU=ad
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM 2018–2026 TYT Geometri soruları (yalnız mantık) · MEB 9–10. sınıf geometri'); TIPK[tipId]=P.k
def q(no,ad,kalip='şekilli',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def bitir_geo(onek,adi):
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
    json.dump(dict(konu=adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Geometri çıkmış soruları (yalnız mantık), MEB 9–10. sınıf geometri müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
P=Parti('ozeldortgen','Özel Dörtgenler','geo|Özel Dörtgenler',ders='TYT Geometri',idon='tytgeo')
GON='TYT Geometri'
OZ=B('Özel dörtgenlerin köşegenleri','Paralelkenarda köşegenler birbirini ortalar. Dikdörtgende köşegenler eşittir; eşkenar dörtgende köşegenler birbirini dik ortalar ve köşe açılarını ikiye böler; karede bu özelliklerin hepsi vardır. Örnek: kenarları 3 ve 4 olan dikdörtgenin köşegenleri 5 ve 5’tir, birbirine dik değildir')
ESK=B('Eşkenar dörtgen','dört kenarı eşit, karşılıklı kenarları paralel olan dörtgendir; köşegenleri birbirini dik ortalar. Örnek: köşegenleri 10 ve 24 olan eşkenar dörtgenin kenarı yarı köşegenlerle Pisagordan √(5² + 12²) = 13’tür')
PAR=B('Paralelkenar tanımı','karşılıklı kenarları paralel olan dörtgendir; karşılıklı açıları eşit, köşegenleri birbirini ortalar. Köşegenleri birbirini ortalayan her dörtgen paralelkenardır. Örnek: karşılıklı açıları 80° ve 100° olan dörtgen paralelkenardır')
ORTA=B('Kenar orta noktalarını birleştirme','dikdörtgenin kenar orta noktaları sırayla birleştirilirse dört kenarı eşit bir dörtgen (eşkenar dörtgen) oluşur. Örnek: bu dörtgenin karşılıklı kenarları birbirine paraleldir ve köşegenleri dikdörtgenin kenarlarına paraleldir')
SERIT=B('Şerit genişliği ve yükseklik','şeridin genişliği, ortak kısmın o şeride ait yüksekliğidir. 30°–60°–90° üçgeninde 30°’nin karşısındaki kenar hipotenüsün yarısıdır. Örnek: hipotenüs 10 ise bu kenar 5’tir')
SEMA=B('Dörtgenlerin sınıflandırılması','kare, hem dikdörtgenin hem eşkenar dörtgenin özelliklerini taşır; dikdörtgen de eşkenar dörtgen de paralelkenarın özel halidir. Dikdörtgende köşegenler eşit ama dik değildir (kare hariç); eşkenar dörtgende köşegenler dik ama eşit değildir (kare hariç)')

# ===== 01 · tablo · orta =====
konu('geo|Özel Dörtgenler','Özel Dörtgenler')
kartla('K-GOD-01','Özellik tablosunda hata','Her dörtgenin köşegen özelliklerini (eşit, dik, açıortay) tek tek hatırlayıp tablodaki yanlış işareti bulmak.','Eşkenar dörtgende köşegenleri eşit sanmak; dikdörtgende köşegenleri açıortay sanmak.','orta',4,'ge-od-tablo','Özellik tablosunda hatalı hücreyi bulma','tablo')
SK1=tablo_svg(['Dörtgen','Eşit','Dik','Açıortay'],[['Kare','+','+','+'],['Dikdörtgen','+','−','−'],['Eşkenar dörtgen','+','+','+'],['Paralelkenar','−','−','−']])
q('0001',tipId='ge-od-tablo',tip='Özellik tablosunda hatalı hücreyi bulma',z='orta',alt='Özellik Tablosu',kaz='Özel dörtgenlerin köşegen özelliklerini karşılaştırarak hatalı işaretlemeyi bulur.',kalip='tablo',
 kart='K-GOD-01 (özellik tablosu) · dört dörtgen, üç köşegen özelliği',
 metin='Bir öğrenci, aşağıdaki tabloda dörtgenlerin köşegen özelliklerini işaretlemiştir. “+” işareti, o dörtgenin köşegenlerinin ilgili özelliği her zaman taşıdığını; “−” işareti ise her zaman taşımadığını gösterir.\n“Eşit”: köşegenler eşit uzunluktadır, “Dik”: köşegenler birbirine diktir, “Açıortay”: köşegenler köşe açılarını iki eş parçaya böler.\nTablodaki hücrelerden yalnız biri hatalı işaretlendiğine göre, hatalı hücre aşağıdakilerden hangisinde yer almaktadır?',
 dogru='Eşkenar dörtgen · Eşit',sira=['Eşkenar dörtgen · Eşit','Dikdörtgen · Dik','Dikdörtgen · Açıortay','Kare · Açıortay','Paralelkenar · Dik'],
 yan=[('Dikdörtgen · Dik','Dikdörtgenin köşegenlerinin dik olduğunu sanıp bu hücreyi hatalı bulmuş.','bilgi'),('Dikdörtgen · Açıortay','Dikdörtgende köşegenlerin köşe açılarını ikiye böldüğünü sanmış; bu özellik yalnız eşkenar dörtgen ve karede vardır.','bilgi'),('Kare · Açıortay','Karenin köşegenlerinin açıortay olduğunu bilmeyip doğru işareti hatalı saymış.','bilgi'),('Paralelkenar · Dik','Paralelkenarın köşegenlerinin dik olduğunu sanıp “−” işaretini hatalı bulmuş.','bilgi')],
 istenen='Hatalı işaretlenmiş hücrenin yeri.',
 ip=['Her satırı soldan sağa tek tek incele: köşegenleri eşit uzunlukta olan hangi dörtgenler vardır ve hangileri yalnız dik kesişir?'],
 bilgi=[OZ],
 ad=[A('Kareyi kontrol et','Karede üç özellik de vardır.','Kare: + + + (doğru)'),A('Dikdörtgeni kontrol et','Köşegenleri eşit, dik değil, açıortay değil.','Dikdörtgen: + − − (doğru)'),A('Eşkenar dörtgeni kontrol et','Köşegenleri dik ve açıortaydır; eşit olmaları gerekmez, kare olmadıkça eşit değildir.','Eşit: − olmalı, tabloda + · Dik + · Açıortay +'),A('Paralelkenarı kontrol et','Genel paralelkenarda köşegenler yalnız birbirini ortalar.','Paralelkenar: − − − (doğru)')],
 puf='Köşegen özellikleri: eşit → dikdörtgen ve kare; dik ve açıortay → eşkenar dörtgen ve kare; paralelkenarda hiçbiri kesin değil.',sekil=SK1)

# ===== 02 · öncüllü + şekil · orta =====
kartla('K-GOD-02','Köşegen bilgisinden dörtgen türü','Köşegenlerin birbirini ortalaması paralelkenarı, ek olarak dik olması eşkenar dörtgeni verir; eşit olması bilinmeden kare ya da dikdörtgen denemez.','Dik ortalamayı kare sanmak; eşkenar dörtgenin paralelkenar olduğunu unutmak.','orta',3,'ge-od-oncul','Köşegen bilgisinden dörtgen türünü belirleme','öncüllü')
c0=(3,2); hA,hB=2.9,1.8
A2=add(c0,(-hA,0)); C2=add(c0,(hA,0)); B2=add(c0,(0,hB)); D2=add(c0,(0,-hB)); E2=c0
assert abs(dist(E2,A2)-dist(E2,C2))<1e-9 and abs(dist(E2,B2)-dist(E2,D2))<1e-9 and abs(ang(E2,A2,B2)-90)<1e-9
assert len({round(dist(A2,B2),6),round(dist(B2,C2),6),round(dist(C2,D2),6),round(dist(D2,A2),6)})==1 and abs(dist(A2,C2)-dist(B2,D2))>1
f=F(); f.poly([A2,B2,C2,D2]); f.line(A2,C2); f.line(B2,D2)
f.tick(A2,E2); f.tick(E2,C2); f.tick(B2,E2,2); f.tick(E2,D2,2); f.dik(E2,C2,B2,.25)
f.vl('A',A2,(-1,0),.3); f.vl('B',B2,(0,1),.3); f.vl('C',C2,(1,0),.3); f.vl('D',D2,(0,-1),.3); f.node(add(E2,(-.28,-.24)),'$E$')
SK2=f.svg()
q('0002',tipId='ge-od-oncul',tip='Köşegen bilgisinden dörtgen türünü belirleme',z='orta',alt='Dörtgen Türünü Belirleme',kaz='Köşegenlerin özelliklerinden dörtgenin hangi özel dörtgen olduğunu kesin olarak belirler.',kalip='öncüllü',
 kart='K-GOD-02 (köşegen bilgisi) · köşegenler birbirini dik ortalıyor',
 metin='Bir tasarımcı, şekildeki ABCD dörtgenini çizerken köşegenlerin E noktasında kesiştiğini ve aynı sayıda çizgiyle işaretlenmiş parçaların eşit uzunlukta olduğunu belirtmiştir. Şekil ölçekli değildir.\nBuna göre,\nI. ABCD bir paralelkenardır.\nII. ABCD bir eşkenar dörtgendir.\nIII. ABCD bir karedir.\nyargılarından hangileri kesinlikle doğrudur?',
 dogru='I ve II',sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 yan=[('Yalnız I','Köşegenleri dik ortalayan dörtgenin dört kenarının eşit olduğunu görememiş; eşkenar dörtgeni elemiş.','bilgi'),('I ve III','Dik ortalamayı yalnız kareye özgü sanıp eşkenar dörtgeni (II) elemiş, kareyi (III) kabul etmiş.','bilgi'),('II ve III','Eşkenar dörtgenin paralelkenar olmadığını sanıp I’i elemiş, dik ortalamayı kare saymış.','bilgi'),('I, II ve III','Köşegenlerin eşit uzunlukta olduğu verilmediği halde dörtgeni kare kabul etmiş.','dikkat')],
 istenen='Kesinlikle doğru olan yargılar.',
 ip=['Köşegenler birbirini ortalıyorsa dörtgen hangi özel dörtgendir? Bir de dik kesişim bilgisini ekle; köşegenlerin uzunluğuyla ilgili bir bilgi verilmiş mi?'],
 bilgi=[PAR,ESK],
 ad=[A('Ortalamayı yorumla','|AE| = |EC| ve |BE| = |ED| olduğundan köşegenler birbirini ortalar.','Köşegenleri birbirini ortalayan dörtgen paralelkenardır → I doğru'),A('Dikliği ekle','Paralelkenarın köşegenleri birbirine dikse kenarlar eşit çıkar.','AC ⊥ BD → ABCD eşkenar dörtgen → II doğru'),A('Kareyi ele','Kare için köşegenlerin eşit uzunlukta olması da gerekir; böyle bir bilgi verilmemiştir.','|AC| = |BD| bilinmiyor → III kesin değil'),A('Sonuç','Yalnız I ve II kesindir.','I ve II')],
 puf='Köşegenler birbirini ortalıyorsa paralelkenar; ayrıca dikse eşkenar dörtgen, eşitse dikdörtgen, ikisi birden ise kare olur.',sekil=SK2)

# ===== 03 · belirleme · kolay =====
kartla('K-GOD-03','Açı ve kenardan dörtgen türü','Karşılıklı açıları eşit dörtgen paralelkenardır; yanındaki iki kenar da eşitse eşkenar dörtgen olur; açılar 90° olmadığından dikdörtgen ya da kare değildir.','Açıları ikişer ikişer eşit görüp dikdörtgen demek; eşkenar dörtgeni yamukla karıştırmak.','kolay',3,'ge-od-belirle','Açı ve kenar bilgisinden dörtgen türünü belirleme')
sd=3.3; A3=(0,0); B3=(sd,0); D3=(sd*cos(radians(110)),sd*sin(radians(110))); C3=add(B3,D3)
assert abs(ang(A3,B3,D3)-110)<1e-9 and abs(ang(B3,A3,C3)-70)<1e-9 and abs(ang(C3,B3,D3)-110)<1e-9 and abs(ang(D3,A3,C3)-70)<1e-9
assert abs(dist(A3,B3)-dist(B3,C3))<1e-9
f=F(); f.poly([A3,B3,C3,D3]); f.tick(A3,B3); f.tick(B3,C3)
f.arc(A3,B3,D3,.45,'$110^\\circ$',1.0); f.arc(B3,C3,A3,.45,'$70^\\circ$',1.0); f.arc(C3,D3,B3,.45,'$110^\\circ$',1.0); f.arc(D3,A3,C3,.45,'$70^\\circ$',1.0)
f.vl('A',A3,(-1,-1),.3); f.vl('B',B3,(1,-1),.3); f.vl('C',C3,(1,1),.3); f.vl('D',D3,(-1,1),.3)
SK3=f.svg()
q('0003',tipId='ge-od-belirle',tip='Açı ve kenar bilgisinden dörtgen türünü belirleme',z='kolay',alt='Dörtgenin Türü',kaz='Açı ve kenar bilgilerinden dörtgenin hangi özel dörtgen olduğunu bulur.',
 kart='K-GOD-03 (dörtgen türü) · 110°/70° açılar, |AB| = |BC|',
 metin='Bir halı tasarımında kullanılacak ABCD biçimindeki motifin açıları ve iki kenarı şekilde işaretlenmiştir. Şekil ölçekli değildir.\nBuna göre, ABCD dörtgeni aşağıdakilerden hangisidir?',
 dogru='Eşkenar dörtgen',sira=['Dik yamuk','İkizkenar yamuk','Dikdörtgen','Kare','Eşkenar dörtgen'],
 yan=[('Dik yamuk','Dik açı olmadığı halde 110° açıyı bir yan kenar açısı sayıp dik yamuk demiş.','dikkat'),('İkizkenar yamuk','Eşit açıları görüp ikizkenar yamuk demiş; ancak burada karşılıklı açılar eşit, paralel kenar çiftleri iki tanedir.','bilgi'),('Dikdörtgen','Açıların ikişer ikişer eşit olmasını dikdörtgen sanmış; dikdörtgenin tüm açıları 90°’dir.','bilgi'),('Kare','Kenarları eşit görüp kare demiş; karede açıların 90° olması gerekir.','bilgi')],
 istenen='ABCD dörtgeninin türü.',
 ip=['Karşılıklı açıları eşit olan dörtgen hangi ailedendir? Sonra eşit işaretli iki kenarı yorumla.'],
 bilgi=[PAR,ESK],
 ad=[A('Karşılıklı açıları incele','m(A) = m(C) ve m(B) = m(D) olduğundan karşılıklı açılar eşittir.','Karşılıklı açıları eşit → paralelkenar'),A('Kenarları incele','Paralelkenarda komşu iki kenar eşitse dört kenar da eşittir.','|AB| = |BC| → dört kenar eşit'),A('Dik açıyı ara','Açılar 110° ve 70°’dir, hiçbiri 90° değildir.','Dikdörtgen ve kare olamaz → eşkenar dörtgen')],
 puf='Karşılıklı açıları eşit dörtgen paralelkenardır; komşu iki kenarı eşitse eşkenar dörtgen, açısı 90° ise dikdörtgen ya da kare olur.',sekil=SK3)

# ===== 04 · şeritlerin kesişimi · zor =====
kartla('K-GOD-04','Kâğıt şeritlerin kesişimi','Eşit genişlikli iki şeridin ortak parçası eşkenar dörtgendir; kenar, genişlik ve şeritler arasındaki açıdan 30°–60°–90° üçgeniyle bulunur.','Genişliği kenar sanmak; alan ile çevreyi karıştırmak; 30°’nin karşısındaki kenarı yanlış katlamak.','zor',4,'ge-od-kagit','Kâğıt kesme ve şeritle oluşan dörtgen')
w4=3; th=30; sc=.4; h4=w4*sc/2; Ls=4.2; cs,sn=cos(radians(th)),sin(radians(th))
V1=(h4*(cs-1)/sn,h4); V2=(h4*(cs+1)/sn,h4); V3=(-V1[0],-h4); V4=(-V2[0],-h4)
side=dist(V1,V2)/sc; assert abs(side-w4/sin(radians(th)))<1e-9 and abs(side-6)<1e-9 and abs(dist(V2,V3)/sc-6)<1e-9
assert abs(ang(V2,V1,V3)-30)<1e-9 and abs(4*side-24)<1e-9
assert abs(w4*side-18)<1e-9 and 4*w4==12 and 4*(w4*3)==36 and abs(4*(w4*sin(radians(th)))-6)<1e-9
uu=(cs,sn); nn_=(-sn,cs)
S1=[(-Ls,-h4),(Ls,-h4),(Ls,h4),(-Ls,h4)]
S2=[add(mul(uu,-Ls),mul(nn_,-h4)),add(mul(uu,Ls),mul(nn_,-h4)),add(mul(uu,Ls),mul(nn_,h4)),add(mul(uu,-Ls),mul(nn_,h4))]
f=F(); f.fill(S1,'fill=black!6'); f.fill(S2,'fill=black!6'); f.fill([V1,V2,V3,V4],'fill=vurgu!30'); f.poly(S1); f.poly(S2)
f.raw(f'\\draw[<->] ({-Ls+.55:.3f},{-h4:.3f}) -- ({-Ls+.55:.3f},{h4:.3f});'); f.node((-Ls+1.05,.0),'$3\\,\\mathrm{cm}$')
q0=add(mul(uu,Ls-.55),mul(nn_,-h4)); q1=add(mul(uu,Ls-.55),mul(nn_,h4))
f.raw(f'\\draw[<->] {pt(q0)} -- {pt(q1)};'); f.node(add(mul(uu,Ls-1.55),(.0,.0)),'$3\\,\\mathrm{cm}$')
f.arc(V2,add(V2,(1,0)),add(V2,uu),.8,'$30^\\circ$',1.55)
SK4=f.svg()
q('0004',tipId='ge-od-kagit',tip='Kâğıt kesme ve şeritle oluşan dörtgen',z='zor',alt='Kâğıt Şeritlerin Kesişimi',kaz='Eşit genişlikli şeritlerin ortak parçasının eşkenar dörtgen olduğunu görüp kenarını bularak çevresini hesaplar.',
 kart='K-GOD-04 (şeritlerin kesişimi) · genişlik 3 cm, açı 30°',
 metin='Bir atölyede genişlikleri eşit olan iki düz kâğıt şerit, aralarındaki açı şekildeki gibi olacak biçimde üst üste yapıştırılıyor. Şeritlerin ortak kısmı taralı dörtgendir.\nŞekil ölçekli değildir.\nBuna göre, taralı dörtgenin çevresi kaç cm’dir?',
 dogru=24,yan=[(6,'Kenarı 3 · sin 30° = 1,5 bularak (sinüsü yanlış yere koyup) çevreyi 6 bulmuş.','islem'),(12,'Şerit genişliğini dörtgenin kenarı sanıp 4 × 3 = 12 yazmış.','bilgi'),(18,'Alanı (3 × 6) hesaplayıp çevre sanmış.','dikkat'),(36,'30° görünce kenarı genişliğin 3 katı almış: 4 × 9 = 36.','islem')],
 istenen='Taralı dörtgenin çevresi (cm).',
 ip=['Taralı dörtgenin kenarları hangi özelliği taşır? Genişlik, dörtgenin hangi doğru parçasına karşılık gelir ve hangi dik üçgeni oluşturur?'],
 bilgi=[SERIT,ESK],
 ad=[A('Dörtgenin türünü bul','Ortak parça paralelkenardır; iki şerit de aynı genişlikte olduğundan paralelkenarın iki yüksekliği eşittir. Alan taban × yükseklikle iki biçimde yazılınca komşu kenarlar eşit çıkar.','Yükseklikler eşit → komşu kenarlar eşit → eşkenar dörtgen'),A('Dik üçgeni kur','Genişlik, 30° açının karşısındaki dik kenardır; hipotenüs eşkenar dörtgenin kenarıdır.','3 = kenar × sin 30°'),A('Kenarı hesapla','30°’nin karşısındaki kenar hipotenüsün yarısıdır.','kenar = 3 × 2 = 6'),A('Çevreyi yaz','Eşkenar dörtgenin dört kenarı eşittir.','4 × 6 = 24')],
 puf='Eşit genişlikli iki şerit kesişince eşkenar dörtgen oluşur; kenar = genişlik ÷ sin(açı).',sekil=SK4)

# ===== 05 · orta noktaları birleştirme · orta =====
kartla('K-GOD-05','Kâğıt kesme: kenar orta noktaları','Dikdörtgenin kenar orta noktaları birleştirilince eşkenar dörtgen oluşur; kenarı yarı kenarlardan Pisagorla bulunur.','Kenarı yarı kenarların toplamı sanmak; dikdörtgenin çevresini vermek; yalnız bir kenarı yazmak.','orta',3,'ge-od-kagit','Kâğıt kesme ve şeritle oluşan dörtgen')
a5,b5=16,12; s5=.3
R=[(0,0),(a5*s5,0),(a5*s5,b5*s5),(0,b5*s5)]; M=[mid(R[0],R[1]),mid(R[1],R[2]),mid(R[2],R[3]),mid(R[3],R[0])]
ks=[dist(M[i],M[(i+1)%4])/s5 for i in range(4)]; assert all(abs(k-10)<1e-9 for k in ks)
assert sum(ks)==40 and 2*(a5+b5)==56 and (a5+b5)==28 and 4*12==48 and 10==ks[0] and abs(alan(M)/s5**2-96)<1e-9
f=F(); f.fill(M); f.poly(R)
f.poly(M)
for i in range(4): f.tick(R[i],M[i],1 if i%2==0 else 2); f.tick(M[i],R[(i+1)%4],1 if i%2==0 else 2)
f.sl('$16$',R[0],R[1],cen(R),.3); f.sl('$12$',R[1],R[2],cen(R),.3)
f.vl('A',R[0],(-1,-1),.3); f.vl('B',R[1],(1,-1),.3); f.vl('C',R[2],(1,1),.3); f.vl('D',R[3],(-1,1),.3)
SK5=f.svg()
q('0005',tipId='ge-od-kagit',tip='Kâğıt kesme ve şeritle oluşan dörtgen',z='orta',alt='Kâğıttan Dörtgen Kesme',kaz='Dikdörtgen kâğıdın kenar orta noktalarını birleştirerek oluşan eşkenar dörtgenin kenarını ve çevresini bulur.',
 kart='K-GOD-05 (kâğıt kesme) · 16 × 12 dikdörtgen, orta noktalar',
 metin='Kenar uzunlukları şekilde cm cinsinden verilen ABCD dikdörtgeni biçimindeki bir kâğıdın her kenarının orta noktası işaretlenmiş ve bu orta noktalar sırayla birleştirilmiştir. Kâğıt, bu doğru parçaları boyunca kesilerek ortadaki taralı parça ayrılıyor.\nBuna göre, ayrılan taralı parçanın çevresi kaç cm’dir?',
 dogru=40,yan=[(20,'Taralı parçanın yalnız bir kenarını (10) bulup yanında bırakmış, yarı çevre 20 demiş.','dikkat'),(28,'Dikdörtgenin yarı çevresini (16 + 12) yazmış.','dikkat'),(48,'Kenarı, dikdörtgenin 12 cm’lik kenarına eşit alıp 4 × 12 yazmış.','bilgi'),(56,'Dikdörtgenin çevresini vermiş; kesilen parçanın kenarlarını yarı kenarların toplamı (8 + 6) sanmış.','bilgi')],
 istenen='Taralı parçanın çevresi (cm).',
 ip=['Taralı parçanın kenarlarından birini, köşedeki dik üçgenin hangi kenarı olarak görebilirsin? O üçgenin dik kenarları şekilde kaç cm?'],
 bilgi=[ORTA],
 ad=[A('Parçanın türünü söyle','Dikdörtgenin orta noktaları birleştirilince dört kenarı eşit bir dörtgen oluşur.','Taralı parça: eşkenar dörtgen'),A('Dik kenarları yaz','Her köşede, yarı kenarlardan oluşan dik üçgen vardır.','Dik kenarlar: 16 ÷ 2 = 8 ve 12 ÷ 2 = 6'),A('Kenarı bul','Pisagor bağıntısını uygula.','kenar² = 8² + 6² = 100 → kenar = 10'),A('Çevreyi yaz','Dört kenar eşittir.','4 × 10 = 40')],
 puf='Dikdörtgenin kenar orta noktalarından oluşan eşkenar dörtgenin kenarı √((a/2)² + (b/2)²) dir.',sekil=SK5)

# ===== 06 · küme şeması · zor =====
kartla('K-GOD-06','Dörtgen sınıflandırma şeması','Paralelkenar, dikdörtgen ve eşkenar dörtgen kümelerinin kesişimi karedir; köşegen özellikleri hangi bölgeye ait olduğunu belirler.','Karenin yalnız dikdörtgen bölgesinde sanılması; eşit ve dik köşegen özelliklerinin karıştırılması.','orta',4,'ge-od-sema','Dörtgen şemasında bölge eşleştirme')
f=F(); f.raw('\\draw[rounded corners=4pt] (0,0) rectangle (7,4.2);')
f.raw('\\draw (2.6,2.1) circle (1.35);'); f.raw('\\draw (4.4,2.1) circle (1.35);')
f.node((.45,3.8),'$P$'); f.node((1.45,3.55),'$D$'); f.node((5.55,3.55),'$E$')
f.node((2.0,2.1),'$2$'); f.node((3.5,2.1),'$3$'); f.node((5.0,2.1),'$4$'); f.node((3.5,.55),'$1$')
SK6=f.svg()
q('0006',tipId='ge-od-sema',tip='Dörtgen şemasında bölge eşleştirme',z='orta',alt='Dörtgenlerin Sınıflandırılması',kaz='Köşegen özelliklerini kullanarak dörtgenleri küme şemasındaki bölgelerle eşleştirir.',
 kart='K-GOD-06 (küme şeması) · P, D, E kümeleri ve dört bölge',
 metin='Şekilde P kümesi paralelkenarları, D kümesi dikdörtgenleri, E kümesi eşkenar dörtgenleri göstermektedir. Bölgeler 1, 2, 3 ve 4 ile numaralanmıştır.\nI. Köşegenleri hem eşit uzunlukta hem birbirine dik olan dörtgen\nII. Köşegenleri birbirine dik olan, ancak eşit uzunlukta olmayan paralelkenar\nIII. Köşegenleri eşit uzunlukta olan, ancak birbirine dik olmayan paralelkenar\nBu dörtgenler hangi numaralı bölgelerde yer alır?',
 dogru='I–3, II–4, III–2',sira=['I–2, II–4, III–3','I–3, II–2, III–4','I–3, II–4, III–1','I–3, II–4, III–2','I–4, II–3, III–2'],
 yan=[('I–2, II–4, III–3','Kareyi yalnız dikdörtgen sanıp 2’ye, dikdörtgeni kesişime koymuş.','bilgi'),('I–3, II–2, III–4','Köşegenleri dik olanı dikdörtgen, eşit olanı eşkenar dörtgen sanmış (özellikleri ters eşleştirmiş).','bilgi'),('I–3, II–4, III–1','Köşegenleri eşit olan dikdörtgeni D kümesine değil, genel paralelkenar bölgesine koymuş.','bilgi'),('I–4, II–3, III–2','Kareyi yalnız eşkenar dörtgen bölgesine, eşkenar dörtgeni kesişime yerleştirmiş.','bilgi')],
 istenen='I, II ve III’ün bölgeleri.',
 ip=['Önce her özelliğin hangi kümeye ait olduğunu belirle; sonra kümelerin kesiştiği yerin ne anlama geldiğini düşün.'],
 bilgi=[SEMA],
 ad=[A('Özellikleri kümelere bağla','Köşegenlerin eşit olması D’nin, dik olması E’nin özelliğidir.','eşit → D · dik → E'),A('I. ifadeyi yerleştir','Hem eşit hem dik olan dörtgen karedir; kare iki kümenin ortak elemanıdır.','I → kesişim bölgesi: 3'),A('II. ifadeyi yerleştir','Dik, ama eşit değil: yalnız E kümesinde.','II → yalnız E bölgesi: 4'),A('III. ifadeyi yerleştir','Eşit, ama dik değil: yalnız D kümesinde.','III → yalnız D bölgesi: 2')],
 puf='Şemada kesişim bölgesi her zaman iki özelliği birden taşıyan dörtgendir: D ∩ E = kare.',sekil=SK6)
bitir_geo('ozeldortgen','Özel Dörtgenler')
