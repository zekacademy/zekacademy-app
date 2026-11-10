import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..'))
from ortak import *
import gorsel as G
from fractions import Fraction as Fr
def fm(x):
    x=Fr(x).limit_denominator(10**6); n=x<0; x=abs(x)
    if x.denominator==1: s=str(x.numerator)
    else:
        d=x.denominator
        while d%2==0: d//=2
        while d%5==0: d//=5
        assert d==1,'ondalik degil'
        s=f'{float(x):.6f}'.rstrip('0').rstrip('.').replace('.',',')
    return ('−' if n else '')+s
ORT={}; KARTLAR=[]
def kart(id,alt,fikir,tuzak,zorluk,kalip,adim,tipId,tip,kaynak):
    KARTLAR.append(dict(id=id,konu=KONU,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zorluk,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=kaynak))
def mk(P,no,kard=False,metin=None,dogru=None,yan=None,istenen=None,ad=None,sekil=None,sira=None,ip=None,bilgi=None,puf=None,kisa=None,
       tipId=None,tip=None,z=None,alt=None,kaz=None,kalip=None,adim=None,kart=None):
    vals=[dogru]+[y[0] for y in yan]; assert len(vals)==5
    if all(not isinstance(v,str) for v in vals):
        fv=[Fr(v).limit_denominator(10**6) for v in vals]; assert len(set(fv))==5
        order=sorted(range(5),key=lambda i:fv[i]); siklar=[fm(vals[i]) for i in order]
        pos={i:'ABCDE'[j] for j,i in enumerate(order)}
    else:
        assert sira and sorted(sira)==sorted(vals), (sira,vals)
        siklar=list(sira); pos={i:'ABCDE'[sira.index(vals[i])] for i in range(5)}
    sik=pos[0]
    cel={pos[i+1]:y[1] for i,y in enumerate(yan)}; tur={pos[i+1]:y[2] for i,y in enumerate(yan)}
    if not kard:
        ORT[no]=(ip,bilgi,puf,kisa)
        P.R(no,tipId,tip,z,alt,kaz,kalip,adim,kart,metin,siklar,sik,istenen,ip,bilgi,ad,puf,cel,tur,kisa=kisa,sekil=sekil)
    else:
        o=ORT[no]
        P.K(no,metin,siklar,sik,istenen,ip or o[0],bilgi or o[1],ad,puf or o[2],cel,tur,kisa=kisa if kisa is not None else o[3],sekil=sekil)
def bitir(P,onek,k):
    HV=os.path.join(HD,'..')
    for q in P.ANA: q['kardes']=None
    P.yaz(os.path.join(HD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Fizik çıkmış soruları, MEB 9–10. sınıf müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def T(x,y,s,**k): return G._t(x,y,s,**k)
KONU='Dinamik'
P=Parti('dinamik','Dinamik','fiz|Dinamik',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 (Newton’ın hareket yasaları, sürtünme) · MEB 9. sınıf'
def kutu(x,y,w,h,et): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke-width="1.8"/>'+T(x+w/2,y+h/2+4,et,bold=True)
def sag_ok(x0,x1,y,et):
    return (f'<path d="M{x0} {y} L{x1} {y}" stroke-width="2.2" style="stroke:var(--acc,#16A34A)"/><polygon points="{x1},{y} {x1-9},{y-5} {x1-9},{y+5}" style="fill:var(--acc,#16A34A);stroke:none"/>'+T((x0+x1)/2,y-8,et,bold=True))
def sekil_iki_kutle(sol,sag,F):
    o=['<path d="M20 120 L310 120" stroke-width="1.8"/>',kutu(50,70,70,50,sol),'<path d="M120 95 L170 95" stroke-width="1.6" stroke-dasharray="4 3"/>',kutu(170,78,56,42,sag),sag_ok(226,296,99,F)]
    o.append(T(145,86,'ip',size=11)); return G._svg(330,150,''.join(o))
def sekil_makara(m1,m2):
    o=['<path d="M20 90 L210 90" stroke-width="1.8"/>','<path d="M214 83 L214 90" stroke-width="1.4"/>',kutu(80,52,70,38,m1),'<path d="M150 71 L210 71" stroke-width="1.6"/>','<circle cx="214" cy="74" r="9" stroke-width="1.8"/>','<path d="M214 65 L214 70" stroke-width="1.4"/>','<path d="M223 74 L223 118" stroke-width="1.6"/>',kutu(197,118,52,40,m2),T(110,108,'yüzey: sürtünmeli',size=11)]
    return G._svg(330,176,''.join(o))
kart('K-FZDN-01','Sürtünmeli yüzeyde ivme','Net kuvvet = uygulanan kuvvet − sürtünme; a = Fnet ÷ m.','Sürtünmeyi atlamak ya da eklemek.','kolay','hikâyeli',2,'fz-dn-surtunme','Net kuvvet ve ivme',KY)
kart('K-FZDN-02','İp gerilmesi','Ortak ivme bütün sistemden bulunur; ip gerilmesi arkadaki kütle için T = m·a.','Gerilmeyi uygulanan kuvvetle karıştırmak.','orta','şekilli',3,'fz-dn-ip','İpteki gerilme kuvveti',KY)
kart('K-FZDN-03','Asansörde tepki kuvveti','Yukarı ivmeli asansörde N = m(g + a).','Ağırlığı değişmez sanmak; g − a almak.','orta','hikâyeli',3,'fz-dn-asansor','Asansörde görünür ağırlık',KY)
kart('K-FZDN-04','Makara sistemi','Asılı ağırlık − sürtünme = toplam kütle × ivme.','Sürtünmeyi atlamak ya da yalnız bir kütleye bölmek.','zor','şekilli',5,'fz-dn-makara','Makaralı sistem ve sürtünme',KY)
# 0001
m,F,f=4,40,12; a=Fr(F-f,m); assert a==7 and Fr(F,m)==10 and Fr(F+f,m)==13 and F-f==28 and F+f==52
mk(P,'0001',tipId='fz-dn-surtunme',tip='Net kuvvet ve ivme',z='kolay',alt='Newton’ın Hareket Yasaları',kaz='Sürtünmeli yatay yüzeyde net kuvvetten ivmeyi hesaplar.',kalip='hikâyeli',adim=2,
 kart='K-FZDN-01 (sürtünmeli yüzeyde a = Fnet/m) · yeni değerler',
 metin='Yatay ve sürtünmeli bir zeminde durmakta olan 4 kg kütleli cisme yatay doğrultuda 40 N’luk kuvvet uygulanıyor. Cisme zeminin uyguladığı sürtünme kuvveti 12 N’dur.\nBuna göre cismin ivmesi kaç m/s² olur?',
 dogru=7,yan=[(10,'Sürtünme kuvvetini hesaba katmamış (40 ÷ 4).','dikkat'),(13,'Sürtünmeyi uygulanan kuvvete eklemiş (52 ÷ 4).','bilgi'),(28,'Net kuvveti (28 N) ivme sanmış; kütleye bölmemiş.','islem'),(52,'Kuvvetle sürtünmeyi toplayıp kütleye bölmemiş.','bilgi')],
 istenen='Cismin ivmesi (m/s²).',ip=['Sürtünme hareketi engelleyen yöndedir; önce net kuvveti bul.'],
 bilgi=[B('Newton’ın ikinci yasası','Fnet = m × a. Hareket yönündeki kuvvetlerden zıt yöndekiler çıkarılır. Örnek: 5 kg’lık cisme 30 N çekim, 10 N sürtünme varsa a = 20 ÷ 5 = 4 m/s²')],
 ad=[A('Net kuvvet','Sürtünme uygulanan kuvvete zıt yöndedir, çıkarılır.','Fnet = 40 − 12 = 28 N'),A('Yasayı yaz','Net kuvvet kütle ile ivmenin çarpımıdır.','Fnet = m × a'),A('İvmeyi bul','Net kuvvet kütleye bölünür.','a = 28 ÷ 4 = 7 m/s²')],
 puf='Sürtünmeli sorularda önce net kuvveti bul, sonra kütleye böl.')
# 0002
mf,mg,F=2,3,40; a=Fr(F,mf+mg); Tg=mg*a; assert a==8 and Tg==24 and mf*a==16 and F//2==20 and F-a==32
mk(P,'0002',tipId='fz-dn-ip',tip='İpteki gerilme kuvveti',z='orta',alt='Newton’ın Hareket Yasaları',kaz='İpe bağlı iki cisimden oluşan sistemde ortak ivmeyi ve ip gerilmesini bulur.',kalip='şekilli',adim=3,
 kart='K-FZDN-02 (ip gerilmesi) · yeni kütleler, gerilme geride kalan kütle üzerinden',
 metin='Sürtünmesiz yatay yüzeyde, kütleleri 3 kg ve 2 kg olan cisimler şekildeki gibi hafif bir iple bağlanmıştır. 2 kg’lık cisme yatay 40 N’luk kuvvet uygulanıyor ve cisimler birlikte hareket ediyor.\nBuna göre ipteki gerilme kuvveti kaç N’dur?',
 sekil=sekil_iki_kutle('3 kg','2 kg','F = 40 N'),
 dogru=24,yan=[(8,'Ortak ivmeyi (8 m/s²) gerilme kuvveti sanmış.','dikkat'),(16,'İpi 2 kg’lık cisme bağlı sayıp 2 × 8 hesaplamış; ip 3 kg’lık cismi çeker.','dikkat'),(32,'Uygulanan kuvvetten ivmeyi çıkarmış (40 − 8); farklı büyüklükleri çıkarmış.','bilgi'),(40,'Uygulanan kuvveti ipteki gerilme sanmış.','dikkat')],
 istenen='İpteki gerilme kuvveti (N).',ip=['İp, arkadaki 3 kg’lık cismi hızlandıran tek yatay kuvvettir.'],
 bilgi=[B('Newton’ın ikinci yasası','Fnet = m × a. Birlikte hareket eden cisimlerde ivme ortaktır: a = Fnet ÷ (toplam kütle). Örnek: 6 kg toplam kütleye 12 N uygulanırsa a = 2 m/s²')],
 ad=[A('Ortak ivme','Sistemin tamamı 40 N’luk kuvvetle hızlanır; toplam kütle 5 kg’dır.','a = 40 ÷ (3 + 2) = 8 m/s²'),A('Arkadaki cisme bak','3 kg’lık cismi hızlandıran tek yatay kuvvet ipteki gerilmedir.','T = m × a'),A('Gerilmeyi bul','Değerleri yerine koy.','T = 3 × 8 = 24 N'),A('Kontrol','2 kg’lık cisimde F − T net kuvvettir.','40 − 24 = 16 N = 2 × 8')],
 puf='İp gerilmesinde önce ortak ivmeyi bul, sonra ipin hızlandırdığı kütleyi seç: T = m × a.')
# 0003
m,a,g=60,2,10; N=m*(g+a); assert N==720 and m*a==120 and m*(g-a)==480 and m*g==600 and m*g*a==1200
mk(P,'0003',tipId='fz-dn-asansor',tip='Asansörde görünür ağırlık',z='orta',alt='Newton’ın Hareket Yasaları',kaz='İvmeli asansörde kişiye etkiyen tepki kuvvetini hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-FZDN-03 (asansörde tepki kuvveti) · yeni değerler',
 metin='Kütlesi 60 kg olan bir kişi, yukarı doğru hızı artan bir asansörün içinde duruyor. Asansörün ivmesi 2 m/s²’dir (g = 10 m/s²).\nBuna göre asansör tabanının kişiye uyguladığı tepki kuvveti kaç N’dur?',
 dogru=720,yan=[(120,'Yalnızca m × a (60 × 2) hesaplamış; ağırlığı katmamış.','dikkat'),(480,'İvmeyi ağırlıktan çıkarmış (g − a); asansör yukarı hızlanırken tepki ağırlıktan büyüktür.','bilgi'),(600,'Asansörü duruyormuş gibi sayıp yalnız ağırlığı yazmış.','dikkat'),(1200,'Kütle, g ve ivmeyi çarpmış (60 × 10 × 2).','bilgi')],
 istenen='Tepki kuvveti (N).',ip=['İvme yukarı yönlü olduğundan net kuvvet de yukarıdır; tepki kuvveti ağırlıktan büyük olmalı.'],
 bilgi=[B('Asansörde tepki kuvveti','kişiye yukarı N (tepki), aşağı mg (ağırlık) etkir. Yukarı yönlü ivme a ise N − mg = m × a, yani N = m × (g + a). Örnek: 50 kg kişi, a = 2 m/s² yukarı: N = 50 × 12 = 600 N')],
 ad=[A('Kuvvetleri belirle','Yukarı tepki N, aşağı ağırlık mg etkir; ivme yukarı yönlüdür.','Fnet = N − mg'),A('Yasayı uygula','Net kuvvet kütle ile ivmenin çarpımıdır.','N − 60 × 10 = 60 × 2'),A('Tepkiyi bul','Ağırlığı sağ tarafa geçir.','N = 120 + 600 = 720 N')],
 puf='İvme yukarıysa tepki ağırlıktan büyük, aşağıysa küçüktür: N = m × (g ± a).')
# 0004
m1,m2,k,g=4,6,Fr(1,4),10; f=k*m1*g; a=Fr(m2*g-f,m1+m2); Tg=m2*(g-a); assert f==10 and a==5 and Tg==30 and m1*a+f==Tg and Fr(m2*g,m1+m2)==6 and Fr(m2*g,m1)==15 and Fr(m2*g-2*f,m1+m2)==4
mk(P,'0004',tipId='fz-dn-makara',tip='Makaralı sistem ve sürtünme',z='zor',alt='Sürtünme Kuvveti',kaz='Sürtünmeli masa ve asılı kütleden oluşan sistemin ivmesini bulur.',kalip='şekilli',adim=5,
 kart='K-FZDN-04 (makara ve sürtünme) · yeni değerler, ivme istenen',
 metin='Şekildeki sistemde 4 kg kütleli cisimle yatay masa arasındaki kinetik sürtünme katsayısı 0,25’tir. Cisim, masanın kenarındaki makaradan geçen iple 6 kg kütleli asılı cisme bağlıdır. İp ve makara hafif, makara sürtünmesizdir; g = 10 m/s².\nSistem serbest bırakıldığında cisimlerin ivmesi kaç m/s² olur?',
 sekil=sekil_makara('4 kg','6 kg'),
 dogru=5,yan=[(4,'Sürtünme kuvvetini iki kat almış (20 N).','islem'),(6,'Sürtünme kuvvetini hiç hesaba katmamış (60 ÷ 10).','dikkat'),(10,'Asılı cismi serbest düşüyormuş gibi sayıp ivmeyi g almış.','bilgi'),(15,'Net kuvveti yalnız masadaki cismin kütlesine bölmüş (60 ÷ 4).','dikkat')],
 istenen='Cisimlerin ivmesi (m/s²).',ip=['Önce masadaki cisme etkiyen sürtünme kuvvetini f = k × N ile bul.'],
 bilgi=[B('Sürtünme kuvveti','kinetik sürtünme f = k × N; yatay yüzeyde N = m × g. Örnek: k = 0,5, m = 2 kg → f = 0,5 × 20 = 10 N'),B('Newton’ın ikinci yasası','sistemin ivmesi a = Fnet ÷ (toplam kütle); ip gerilmesi iç kuvvettir, net kuvvette görünmez')],
 ad=[A('Sürtünme kuvveti','Masadaki cismin normal kuvveti ağırlığına eşittir.','N = 4 × 10 = 40 N ; f = 0,25 × 40 = 10 N'),A('Hareketi sağlayan kuvvet','Asılı cismin ağırlığı sistemi çeker.','W = 6 × 10 = 60 N'),A('Net kuvvet','Sürtünme harekete zıttır.','Fnet = 60 − 10 = 50 N'),A('Toplam kütle','İpteki cisimler aynı ivmeyle hareket eder.','m = 4 + 6 = 10 kg'),A('İvme','Net kuvvet toplam kütleye bölünür.','a = 50 ÷ 10 = 5 m/s²')],
 puf='Makaralı sistemde ip gerilmesi iç kuvvettir; dış kuvvetlerin (ağırlık, sürtünme) farkını toplam kütleye böl.')
bitir(P,'dinamik','fiz|Dinamik')
