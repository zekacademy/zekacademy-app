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
    P.yaz(os.path.join(HD,f'{onek}-1.json'),os.path.join(HD,f'{onek}-1-kardes.json'))
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Fizik çıkmış soruları, MEB 9–10. sınıf müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def T(x,y,s,**k): return G._t(x,y,s,**k)
def kap(x0,seviye,cisim=None,etiket='',w=96,h=110,top=26):
    """Kap çizimi: seviye 0–1 (kap yüksekliğine oran). cisim: dict(f=batık oran, w, h, tas=False, ip=None|'alt'|'ust', yuk=None, etk='')."""
    yb=top+h; yl=yb-seviye*h; o=[]
    o.append(f'<rect x="{x0}" y="{yl:.1f}" width="{w}" height="{yb-yl:.1f}" style="fill:currentColor;stroke:none;opacity:.13"/>')
    o.append(f'<path d="M{x0} {top} L{x0} {yb} L{x0+w} {yb} L{x0+w} {top}" stroke-width="2"/>')
    o.append(f'<line x1="{x0+2}" y1="{yl:.1f}" x2="{x0+w-2}" y2="{yl:.1f}" stroke-width="1.2" stroke-dasharray="4 3" opacity=".7"/>')
    if cisim:
        c=cisim; cw,ch=c.get('w',36),c.get('h',40); cx=x0+w/2; f=c['f']
        if c.get('ip')=='alt': yo=yb-34-ch
        elif c.get('yuk'): yo=yl
        elif c.get('ip')=='ust' or f>=1: yo=yl+14
        else: yo=yl-(1-f)*ch
        o.append(f'<rect x="{cx-cw/2:.1f}" y="{yo:.1f}" width="{cw}" height="{ch}" stroke-width="2" style="fill:currentColor;fill-opacity:.28"/>')
        if c.get('tas'): o.append(f'<circle cx="{cx:.1f}" cy="{yo+ch*0.6:.1f}" r="6" style="fill:currentColor;stroke:none"/>')
        if c.get('ip')=='alt': o.append(f'<line x1="{cx}" y1="{yo+ch:.1f}" x2="{cx}" y2="{yb}" stroke-width="1.6"/>')
        if c.get('ip')=='ust':
            o.append(f'<line x1="{x0-8}" y1="{top-14}" x2="{x0+w+8}" y2="{top-14}" stroke-width="3"/><line x1="{cx}" y1="{top-14}" x2="{cx}" y2="{yo:.1f}" stroke-width="1.6"/>')
        if c.get('yuk'):
            o.append(f'<rect x="{cx-12:.1f}" y="{yo-16:.1f}" width="24" height="16" stroke-width="2" style="fill:{G.ACC};fill-opacity:.35;stroke:{G.ACC}"/>'); o.append(T(cx+16,yo-4,c['yuk'],anchor='start',size=11,renk=G.ACC,bold=True))
        if c.get('etk'): o.append(T(cx+cw/2+6,yo+ch/2+4,c['etk'],anchor='start',size=11,bold=True))
    if etiket: o.append(T(x0+w/2,yb+17,etiket,size=12,bold=True))
    return ''.join(o)
def kaplar(*ks,W=330,H=170): return G._svg(W,H,''.join(ks))
KONU='Sıvıların Kaldırma Kuvveti'
P=Parti('kaldirma','Sıvıların Kaldırma Kuvveti','fiz|Sıvıların Kaldırma Kuvveti',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (kaldırma kuvveti) · MEB 10. sınıf'
kart('K-FZKA-01','Yüzen cisim','Yüzen cisimde batan hacim oranı özkütle oranına eşittir: d_cisim = d_sıvı × batan oran.','Dışta kalan oranı özkütle sanmak; oranı ters kurmak.','kolay','şekilli',2,'fz-kl-yuzme','Yüzen cismin batan hacmi',KY)
kart('K-FZKA-02','Dinamometre','Havadaki ve sıvıdaki ağırlık farkı kaldırma kuvvetidir; F = d g V ile hacim, kütleyle özkütle bulunur.','Okunan ağırlığı gerçek ağırlık sanmak; g’yi atlamak.','orta','hikâyeli',4,'fz-kl-dinamometre','Dinamometre ve kaldırma kuvveti',KY)
kart('K-FZKA-03','Farklı sıvılarda yüzme','Aynı cisim iki sıvıda yüzüyorsa d₁ × V₁ = d₂ × V₂ (batan hacimler ters orantılı).','Oranı ters yazmak; oranları toplamak ya da çarpmak.','orta','şekilli',3,'fz-kl-yuzme','Yüzen cismin batan hacmi',KY)
kart('K-FZKA-04','İp gerilmesi','Tamamen batık, ipli cisimde kuvvetler dengelenir: ip, kaldırma kuvveti ile ağırlığın farkı kadardır.','İp gerilmesini kaldırma kuvvetine ya da ağırlığa eşit saymak.','orta','şekilli',4,'fz-kl-ip-gerilme','İple bağlı cismin dengesi',KY)
kart('K-FZKA-05','Yükle batırma','Cisim üstüne yük konup tamamen batırılırsa yük ağırlığı = sıvı ağırlığı farkı: m = (d_sıvı − d_cisim) × V.','Cismin kütlesini ya da sıvı kütlesini yükle karıştırmak.','zor','şekilli',4,'fz-kl-yuk-batma','Yük konan cismin batması',KY)
kart('K-FZKA-06','Buz erirse seviye','Yüzen buz erirken yer değiştiren hacim ile erimiş suyun hacmi karşılaştırılır; içindeki cismin özkütlesi sonucu belirler.','Buz eridiğinde seviyenin her zaman değiştiğini ya da hep sabit kaldığını sanmak.','zor','öncüllü',5,'fz-kl-buz','Buz erirken su seviyesi',KY)
KAL=B('Kaldırma kuvveti','F = d_sıvı × V_batan × g; yer değiştiren sıvının ağırlığına eşittir. Örnek: suda (1000 kg/m³) 2 × 10⁻³ m³ batan cisme 1000 × 2 × 10⁻³ × 10 = 20 N etki eder')
YUZ=B('Yüzme koşulu','yüzen cisimde kaldırma kuvveti ağırlığa eşittir: d_cisim × V = d_sıvı × V_batan; yani d_cisim = d_sıvı × (batan hacim ÷ toplam hacim). Örnek: yarısı batıksa d_cisim = d_sıvı ÷ 2')
# ---- 0001
d=Fr(15,10)*Fr(4,5); assert d==Fr(12,10) and Fr(15,10)/Fr(4,5)==Fr(15,8)
mk(P,'0001',tipId='fz-kl-yuzme',tip='Yüzen cismin batan hacmi',z='kolay',alt='Kaldırma Kuvveti',kaz='Yüzen cismin batan hacim oranından özkütlesini bulur.',kalip='şekilli',adim=2,
 kart='K-FZKA-01 (yüzen cisim) · yeni sıvı özkütlesi ve batan oran',
 metin='Özkütlesi 1,5 g/cm³ olan sıvıda şekildeki gibi dengede yüzen bir cismin hacminin 1/5’i sıvının dışında kalıyor.\nBuna göre cismin özkütlesi kaç g/cm³’tür?',
 sekil=kaplar(kap(115,0.72,dict(f=0.8,w=40,h=44),'1,5 g/cm³ sıvı')),
 dogru=Fr(12,10),yan=[(Fr(3,10),'Dışta kalan oranı (1/5) ile sıvının özkütlesini çarpmış.','dikkat'),(Fr(8,10),'Batan hacim oranını (4/5) özkütle sanmış; sıvının özkütlesiyle çarpmayı atlamış.','dikkat'),(Fr(15,10),'Cismin özkütlesini sıvınınkine eşit sanmış.','bilgi'),(Fr(15,8),'Oranı ters kurup 1,5 ÷ (4/5) hesaplamış.','islem')],
 istenen='Cismin özkütlesi (g/cm³).',
 ip=['Yüzen cisimde kaldırma kuvveti cismin ağırlığına eşittir.','Batan hacim, toplam hacmin kaçta kaçı? Dışta kalan 1/5 ise batan…','d_cisim × V = d_sıvı × V_batan eşitliğini kur.'],
 bilgi=[YUZ,KAL],
 ad=[A('Batan oran','Hacmin 1/5’i dışarıda olduğundan 4/5’i sıvının içindedir.','V_batan = 4/5 V'),A('Dengeyi yaz','Yüzen cismin ağırlığı kaldırma kuvvetine eşittir.','d × V = 1,5 × (4/5) V'),A('Sonuç','V sadeleşir.','d = 1,5 × 0,8 = 1,2 g/cm³')],
 puf='Yüzen cisimde özkütle = sıvının özkütlesi × batan hacim oranıdır.')
d=Fr(2)*Fr(3,4); assert d==Fr(3,2)
mk(P,'0001',True,metin='Özkütlesi 2 g/cm³ olan sıvıda şekildeki gibi yüzen bir cismin hacminin 1/4’ü sıvının dışındadır.\nBuna göre cismin özkütlesi kaç g/cm³’tür?',
 sekil=kaplar(kap(115,0.72,dict(f=0.75,w=40,h=44),'2 g/cm³ sıvı')),
 dogru=Fr(15,10),yan=[(Fr(5,10),'Dışta kalan oranı (1/4) ile sıvının özkütlesini çarpmış.','dikkat'),(Fr(75,100),'Batan hacim oranını (3/4) özkütle sanmış; sıvının özkütlesiyle çarpmayı atlamış.','dikkat'),(1,'Cismin yarısının battığını sanmış (2 × 1/2).','dikkat'),(2,'Cismin özkütlesini sıvınınkine eşit sanmış.','bilgi')],
 istenen='Cismin özkütlesi (g/cm³).',
 ad=[A('Batan oran','Hacmin 1/4’ü dışarıda olduğundan 3/4’ü sıvının içindedir.','V_batan = 3/4 V'),A('Dengeyi yaz','Yüzen cismin ağırlığı kaldırma kuvvetine eşittir.','d × V = 2 × (3/4) V'),A('Sonuç','V sadeleşir.','d = 2 × 0,75 = 1,5 g/cm³')])
# ---- 0002
F_=50-30; V_=Fr(F_,1000*10); m_=Fr(50,10); assert V_==Fr(2,1000) and m_/V_==2500 and Fr(30,10)/V_==1500 and Fr(50)/V_==25000 and m_/Fr(1,1000)==5000
mk(P,'0002',tipId='fz-kl-dinamometre',tip='Dinamometre ve kaldırma kuvveti',z='orta',alt='Kaldırma Kuvveti',kaz='Dinamometre okumalarından kaldırma kuvvetini, hacmi ve cismin özkütlesini bulur.',kalip='hikâyeli',adim=4,
 kart='K-FZKA-02 (dinamometre ve özkütle) · yeni ağırlıklar',
 metin='Bir cisim havada dinamometreyle ölçüldüğünde 50 N, tamamen suya batırıldığında 30 N okunuyor.\nSuyun özkütlesi 1000 kg/m³ ve g = 10 m/s² olduğuna göre cismin özkütlesi kaç kg/m³’tür?',
 dogru=2500,yan=[(1000,'Suyun özkütlesini cismin özkütlesi sanmış.','dikkat'),(1500,'Sudaki okumayı (30 N) cismin ağırlığı sanıp kütleyi 3 kg bulmuş.','dikkat'),(5000,'Hacmi 1 × 10⁻³ m³ bulmuş (20 N yerine 10 N kaldırma kuvveti kullanmış).','islem'),(25000,'Ağırlığı (50 N) kütle sanmış; g’ye bölmeyi atlamış.','islem')],
 istenen='Cismin özkütlesi (kg/m³).',
 ip=['Havadaki ve sudaki okuma farkı kaldırma kuvvetidir.','Kaldırma kuvvetinden cismin hacmini bul: F = d × V × g.','Havadaki ağırlıktan kütleyi, kütle ve hacimden özkütleyi bul.'],
 bilgi=[KAL,B('Özkütle ve ağırlık','özkütle d = m ÷ V; ağırlık G = m × g. Örnek: 50 N ağırlıklı cismin kütlesi 5 kg’dır (g = 10)')],
 ad=[A('Kaldırma kuvveti','Havadaki ağırlıktan sudaki okuma çıkarılır.','F = 50 − 30 = 20 N'),A('Hacim','Cisim tamamen batık olduğundan batan hacim cismin hacmidir.','20 = 1000 × V × 10 · V = 2 × 10⁻³ m³'),A('Kütle','Havadaki okuma cismin ağırlığıdır.','m = 50 ÷ 10 = 5 kg'),A('Özkütle','Kütle hacme bölünür.','d = 5 ÷ (2 × 10⁻³) = 2500 kg/m³')],
 puf='Dinamometre sorularında önce okuma farkından kaldırma kuvvetini, ondan hacmi bul; kütle için havadaki okumayı kullan.')
F_=36-24; V_=Fr(F_,10000); m_=Fr(36,10); assert V_==Fr(12,10000) and m_/V_==3000 and Fr(36,24)*1000==1500 and m_/(V_*10)==300 and m_/V_/10==300 and Fr(36)/V_==30000 and m_/V_==3000
mk(P,'0002',True,metin='Bir metal blok, havada dinamometreyle ölçüldüğünde 36 N, tamamen suya batırıldığında 24 N okunuyor.\nSuyun özkütlesi 1000 kg/m³ ve g = 10 m/s² olduğuna göre bloğun özkütlesi kaç kg/m³’tür?',
 dogru=3000,yan=[(300,'Hacmi 1,2 × 10⁻² m³ bulmuş (üs hatası yapmış).','islem'),(1000,'Suyun özkütlesini bloğun özkütlesi sanmış.','dikkat'),(1500,'Özkütleyi 1000 × 36 ÷ 24 olarak hesaplamış; sudaki okumayı kaldırma kuvveti yerine kullanmış.','bilgi'),(2000,'Sudaki okumayı (24 N) bloğun ağırlığı sanıp özkütleyi 2,4 kg ÷ 1,2 × 10⁻³ m³ bulmuş.','dikkat')],
 istenen='Bloğun özkütlesi (kg/m³).',
 ad=[A('Kaldırma kuvveti','Havadaki ağırlıktan sudaki okuma çıkarılır.','F = 36 − 24 = 12 N'),A('Hacim','Blok tamamen batıktır.','12 = 1000 × V × 10 · V = 1,2 × 10⁻³ m³'),A('Kütle','Havadaki okuma bloğun ağırlığıdır.','m = 36 ÷ 10 = 3,6 kg'),A('Özkütle','Kütle hacme bölünür.','d = 3,6 ÷ (1,2 × 10⁻³) = 3000 kg/m³')])
# ---- 0003
assert Fr(1,3)/Fr(1,2)==Fr(2,3)
R3=['1/6','2/3','5/6','3/2','6']
mk(P,'0003',tipId='fz-kl-yuzme',tip='Yüzen cismin batan hacmi',z='orta',alt='Kaldırma Kuvveti',kaz='Aynı cismin iki farklı sıvıdaki batan hacim oranlarından sıvıların özkütle oranını bulur.',kalip='şekilli',adim=3,
 kart='K-FZKA-03 (farklı sıvılarda yüzme) · yeni batan oranlar',
 metin='Şekildeki gibi aynı cisim, özkütleleri d_X ve d_Y olan X ve Y sıvılarında yüzmektedir. Cismin hacminin X sıvısında 1/2’si, Y sıvısında 1/3’ü sıvı içindedir.\nBuna göre d_X / d_Y oranı kaçtır?',
 sekil=kaplar(kap(30,0.7,dict(f=0.5,w=40,h=44),'X sıvısı'),kap(190,0.7,dict(f=1/3,w=40,h=44),'Y sıvısı')),
 dogru='2/3',sira=R3,yan=[('1/6','Batan hacim oranlarını (1/2 × 1/3) çarpmış.','islem'),('5/6','Batan hacim oranlarını (1/2 + 1/3) toplamış.','islem'),('3/2','Oranı ters kurmuş: d_X ÷ d_Y yerine d_Y ÷ d_X.','islem'),('6','Batan oranlarını çarpmanın tersini almış (1 ÷ (1/6)).','islem')],
 istenen='X ve Y sıvılarının özkütle oranı (d_X / d_Y).',
 ip=['Aynı cisim iki sıvıda da yüzüyor: kaldırma kuvveti her iki durumda da cismin ağırlığına eşittir.','İki durumu eşitle: d_X × V_X batan = d_Y × V_Y batan.','Özkütle oranını çekmek için batan hacimleri oranla.'],
 bilgi=[YUZ],
 ad=[A('Her sıvı için denge','Kaldırma kuvveti iki durumda da cismin ağırlığına eşit.','d_X × (V ÷ 2) = G · d_Y × (V ÷ 3) = G'),A('Eşitle','Ağırlık aynı olduğundan iki kaldırma kuvveti eşittir; V sadeleşir.','d_X ÷ 2 = d_Y ÷ 3'),A('Sonuç','Oran çekilir.','d_X ÷ d_Y = (1/3) ÷ (1/2) = 2/3')],
 puf='Aynı cisim iki sıvıda yüzüyorsa özkütle × batan hacim iki durumda da eşittir; sıvıların özkütleleri batan hacimlerle ters orantılıdır.')
assert Fr(3,4)/Fr(3,5)==Fr(5,4) and Fr(3,4)-Fr(3,5)==Fr(3,20) and Fr(3,4)+Fr(3,5)==Fr(27,20) and Fr(3,4)*Fr(3,5)==Fr(9,20)
R3k=['3/20','9/20','4/5','5/4','27/20']
mk(P,'0003',True,metin='Şekildeki gibi aynı cisim, özkütleleri d_K ve d_L olan K ve L sıvılarında yüzmektedir. Cismin hacminin K sıvısında 3/5’i, L sıvısında 3/4’ü sıvı içindedir.\nBuna göre d_K / d_L oranı kaçtır?',
 sekil=kaplar(kap(30,0.7,dict(f=0.6,w=40,h=44),'K sıvısı'),kap(190,0.7,dict(f=0.75,w=40,h=44),'L sıvısı')),
 dogru='5/4',sira=R3k,yan=[('3/20','Batan hacim oranlarının farkını (3/4 − 3/5) almış.','islem'),('9/20','Batan hacim oranlarını (3/5 × 3/4) çarpmış.','islem'),('4/5','Oranı ters kurmuş: d_L ÷ d_K.','islem'),('27/20','Batan hacim oranlarını (3/5 + 3/4) toplamış.','islem')],
 istenen='K ve L sıvılarının özkütle oranı (d_K / d_L).',
 ad=[A('Her sıvı için denge','Kaldırma kuvveti iki durumda da cismin ağırlığına eşit.','d_K × (3V ÷ 5) = G · d_L × (3V ÷ 4) = G'),A('Eşitle','Ağırlık aynı olduğundan iki kaldırma kuvveti eşittir; V sadeleşir.','3 d_K ÷ 5 = 3 d_L ÷ 4'),A('Sonuç','Oran çekilir.','d_K ÷ d_L = (3/4) ÷ (3/5) = 5/4')])
# ---- 0004
V=Fr(4,1000); Tg=1000*10*V-600*V*10; assert 1000*10*V==40 and 600*10*V==24 and Tg==16 and 40+24==64
mk(P,'0004',tipId='fz-kl-ip-gerilme',tip='İple bağlı cismin dengesi',z='orta',alt='Kaldırma Kuvveti',kaz='İple bağlı, tamamen batık cismin ip gerilmesini kuvvet dengesinden bulur.',kalip='şekilli',adim=4,
 kart='K-FZKA-04 (ip gerilmesi) · yeni hacim ve özkütle, ip tabana bağlı',
 metin='Hacmi 4 L (4 × 10⁻³ m³), özkütlesi 600 kg/m³ olan bir cisim, şekildeki gibi kabın tabanına bağlı bir iple suyun içinde tamamen batık olarak dengededir.\nSuyun özkütlesi 1000 kg/m³ ve g = 10 m/s² olduğuna göre ipteki gerilme kuvveti kaç N’dur?',
 sekil=kaplar(kap(115,0.8,dict(f=1,w=40,h=40,ip='alt'),'su')),
 dogru=16,yan=[(24,'Cismin ağırlığını (24 N) ip gerilmesi sanmış.','dikkat'),(40,'Kaldırma kuvvetini (40 N) ip gerilmesi sanmış; ağırlığı çıkarmamış.','dikkat'),(64,'Kuvvetleri toplamış: 40 + 24; ağırlığın aşağı, ipin de aşağı yönlü olduğunu karıştırmış.','bilgi'),(160,'Hacmi litre olarak (4) kullanıp kaldırma kuvvetini 400 N bulmuş.','islem')],
 istenen='İpteki gerilme kuvveti (N).',
 ip=['Cisim denge halinde; kuvvetlerin yönlerini çiz: yukarı ve aşağı.','Kaldırma kuvveti yukarı, ağırlık ve ip gerilmesi aşağı yönlüdür.','Kaldırma kuvvetini ve ağırlığı ayrı ayrı hesapla.'],
 bilgi=[KAL,B('Ağırlık','G = d × V × g. Örnek: 2 × 10⁻³ m³ hacimli, 500 kg/m³ özkütleli cismin ağırlığı 500 × 2 × 10⁻³ × 10 = 10 N')],
 ad=[A('Kaldırma kuvveti','Cisim tamamen batık; batan hacim 4 × 10⁻³ m³.','F = 1000 × 4 × 10⁻³ × 10 = 40 N'),A('Ağırlık','Cismin özkütlesi 600 kg/m³.','G = 600 × 4 × 10⁻³ × 10 = 24 N'),A('Kuvvet dengesi','Kaldırma kuvveti ağırlıktan büyük olduğundan cisim yukarı çıkmak ister; ip aşağı çeker.','F = G + T'),A('Sonuç','T çekilir.','T = 40 − 24 = 16 N')],
 puf='İple tabana bağlı batık cisimde T = F_kaldırma − G; iple tavana asılı cisimde T = G − F_kaldırma.')
V=Fr(3,1000); Fk=800*V*10; assert Fk==24 and 50-Fk==26 and 50+Fk==74 and 800*3*10==24000
mk(P,'0004',True,metin='Ağırlığı 50 N olan bir cisim, hacmi 3 L (3 × 10⁻³ m³) olacak biçimde tamamen yağın içinde, şekildeki gibi tavana bağlı bir iple dengede tutuluyor.\nYağın özkütlesi 800 kg/m³ ve g = 10 m/s² olduğuna göre ipteki gerilme kuvveti kaç N’dur?',
 sekil=kaplar(kap(115,0.8,dict(f=1,w=40,h=40,ip='ust'),'yağ')),
 dogru=26,yan=[(24,'Kaldırma kuvvetini (24 N) ip gerilmesi sanmış.','dikkat'),(50,'Cismin ağırlığını (50 N) ip gerilmesi sanmış; kaldırma kuvvetini çıkarmamış.','dikkat'),(74,'Kaldırma kuvveti ile ağırlığı toplamış (24 + 50).','bilgi'),(240,'Hacmi litre olarak kullanıp kaldırma kuvvetini 240 N bulmuş.','islem')],
 istenen='İpteki gerilme kuvveti (N).',
 ip=['Cisim denge halinde; yukarı ve aşağı yönlü kuvvetleri belirle.','İp tavana bağlı: ip ve kaldırma kuvveti yukarı, ağırlık aşağı yönlüdür.','Önce yağın uyguladığı kaldırma kuvvetini hesapla.'],
 bilgi=[KAL,B('Kuvvet dengesi','dengedeki cisimde yukarı yönlü kuvvetlerin toplamı aşağı yönlülere eşittir. Örnek: ağırlık 30 N, kaldırma kuvveti 10 N ise ip 20 N’dur')],
 ad=[A('Kaldırma kuvveti','Cisim tamamen batık; hacim 3 × 10⁻³ m³.','F = 800 × 3 × 10⁻³ × 10 = 24 N'),A('Kuvvetleri yaz','İp ve kaldırma kuvveti yukarı, ağırlık aşağı yönlüdür.','T + F = G'),A('Değerleri koy','Ağırlık 50 N, kaldırma kuvveti 24 N.','T + 24 = 50'),A('Sonuç','T çekilir.','T = 26 N')])
# ---- 0005
m=(1-Fr(6,10))*500; assert m==200 and Fr(6,10)*500==300 and 1*500==500 and (1+Fr(6,10))*500==800 and m*2==400
mk(P,'0005',tipId='fz-kl-yuk-batma',tip='Yük konan cismin batması',z='zor',alt='Kaldırma Kuvveti',kaz='Yüzen cismin üstüne konan yükle tamamen batması için gereken kütleyi bulur.',kalip='şekilli',adim=4,
 kart='K-FZKA-05 (yükle batırma) · yeni hacim ve özkütle, istenen yük kütlesi',
 metin='Hacmi 500 cm³, özkütlesi 0,6 g/cm³ olan bir cisim, özkütlesi 1 g/cm³ olan suda yüzmektedir. Cismin üzerine kütlesi m olan bir yük konulunca cisim yalnızca tamamen suya batıyor (yük suya değmiyor); sistem dengededir (şekil).\nBuna göre m kaç gramdır?',
 sekil=kaplar(kap(115,0.7,dict(f=1,w=40,h=40,yuk='m'),'su')),
 dogru=200,yan=[(300,'Cismin kütlesini (0,6 × 500) yükün kütlesi sanmış.','dikkat'),(400,'Doğru değeri (200 g) 2 ile çarpmış; kaldırma kuvvetinin ağırlıkla eşitliğini yanlış kurmuş.','islem'),(500,'Cismin hacmini (500) yükün kütlesi sanmış.','dikkat'),(800,'Özkütleleri toplayıp (1 + 0,6) × 500 hesaplamış.','islem')],
 istenen='Yükün kütlesi (g).',
 ip=['Sistemin (cisim + yük) toplam ağırlığı, tamamen batan cismin kaldırma kuvvetine eşit olmalıdır.','Kaldırma kuvveti, 500 cm³ suyun ağırlığıdır.','Cismin kendi ağırlığını bu kuvvetten çıkar.'],
 bilgi=[KAL,B('Kütle ve özkütle','m = d × V. Örnek: özkütlesi 0,6 g/cm³, hacmi 100 cm³ olan cismin kütlesi 60 g’dır')],
 ad=[A('Kaldırma kuvveti','Cisim tamamen batık: 500 cm³ suyun kütlesi, yer değiştiren sıvının kütlesidir.','m_su = 1 × 500 = 500 g'),A('Cismin kütlesi','Özkütle ile hacmin çarpımı.','m_cisim = 0,6 × 500 = 300 g'),A('Denge','Cisim ve yükün toplam kütlesi, yer değiştiren suyun kütlesine eşittir.','300 + m = 500'),A('Sonuç','m çekilir.','m = 200 g')],
 puf='Yükle tamamen batırmada cisim + yükün kütlesi, cismin hacmi kadar sıvının kütlesine eşittir: m_yük = (d_sıvı − d_cisim) × V.')
m=(Fr(12,10)-Fr(8,10))*600; assert m==240 and Fr(8,10)*600==480 and Fr(12,10)*600==720 and (Fr(12,10)+Fr(8,10))*600==1200 and m/2==120
mk(P,'0005',True,metin='Hacmi 600 cm³, özkütlesi 0,8 g/cm³ olan bir tahta blok, özkütlesi 1,2 g/cm³ olan tuzlu suda yüzmektedir. Bloğun üzerine kütlesi m olan bir yük konulunca blok yalnızca tamamen sıvıya batıyor (yük sıvıya değmiyor); sistem dengededir (şekil).\nBuna göre m kaç gramdır?',
 sekil=kaplar(kap(115,0.7,dict(f=1,w=40,h=40,yuk='m'),'tuzlu su')),
 dogru=240,yan=[(120,'Gerekli yükün yarısını almış; kaldırma kuvvetinin yalnız yarısını hesaba katmış.','islem'),(480,'Bloğun kütlesini (0,8 × 600) yükün kütlesi sanmış.','dikkat'),(720,'Yer değiştiren sıvının kütlesini (1,2 × 600) yükün kütlesi sanmış.','dikkat'),(1200,'Özkütleleri toplayıp (1,2 + 0,8) × 600 hesaplamış.','islem')],
 istenen='Yükün kütlesi (g).',
 ad=[A('Yer değiştiren sıvı','Blok tamamen batık: 600 cm³ tuzlu suyun kütlesi.','m_sıvı = 1,2 × 600 = 720 g'),A('Bloğun kütlesi','Özkütle ile hacmin çarpımı.','m_blok = 0,8 × 600 = 480 g'),A('Denge','Blok ve yükün toplam kütlesi, yer değiştiren sıvının kütlesine eşittir.','480 + m = 720'),A('Sonuç','m çekilir.','m = 240 g')])
# ---- 0006 buz erirse
Mi,Ms,ds=900,60,3; Vi=Fr(Mi)/Fr(9,10); Vs=Fr(Ms,ds); assert (Mi+Ms)/(Vi+Vs)<1 and Vi+Vs>0
yer0=Mi+Ms; yer1=Mi+Vs; assert yer1<yer0 and ds>1
S6=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
mk(P,'0006',tipId='fz-kl-buz',tip='Buz erirken su seviyesi',z='zor',alt='Kaldırma Kuvveti',kaz='İçinde cisim bulunan buz erirken su seviyesindeki ve basınçtaki değişimi yorumlar.',kalip='öncüllü',adim=5,
 kart='K-FZKA-06 (buz erirse seviye) · içinde taş olan buz, öncüllü',
 metin='Şekildeki kapta su ve içinde özkütlesi 3 g/cm³ olan bir taş bulunan, yüzen bir buz parçası vardır. Buz parçasının ve taşın birlikte özkütlesi suyun özkütlesinden küçüktür.\nBuz tamamen eriyip dengeye ulaştığında;\nI. Kaptaki su seviyesi alçalır.\nII. Taş kabın dibine batar.\nIII. Kabın tabanındaki sıvı basıncı artar.\nifadelerinden hangileri doğrudur?',
 sekil=kaplar(kap(115,0.7,dict(f=0.9,w=44,h=40,tas=True,etk='buz'),'su')),
 dogru='I ve II',sira=S6,yan=[('Yalnız I','Eriyen buzdan çıkan taşın dibe battığını (II) atlamış.','dikkat'),('Yalnız II','Taşın suyun içinde kalıp seviyeyi alçalttığını (I) atlamış.','dikkat'),('I ve III','Seviye alçaldığında taban basıncının da azalacağını görmemiş (III yanlış).','bilgi'),('II ve III','Seviyenin alçaldığını (I) fark etmemiş; basıncın artacağını sanmış.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['Buz + taş yüzerken yer değiştirdiği suyun kütlesi, ikisinin toplam kütlesine eşittir.','Buz erirse taş ne olur? Özkütlesi suyunkinden büyük mü, küçük mü?','Erimeden sonra yer değiştiren sıvı hacmi ile önceki hacmi karşılaştır.'],
 bilgi=[YUZ,B('Taban basıncı','sıvının taban basıncı P = d × g × h; derinlik h azalırsa basınç azalır')],
 ad=[A('Eriyen buzun taşı','Buz eriyince taş serbest kalır; özkütlesi (3 g/cm³) sudan büyük olduğundan batar.','II doğru'),A('Önceki durum','Buz ve taş birlikte yüzerken yer değiştirdikleri su kütlesi, kendi toplam kütlelerine eşittir.','900 + 60 = 960 g su yer değiştirir (960 cm³)'),A('Sonraki durum','Eriyen buz 900 g su olur (900 cm³). Taş 60 ÷ 3 = 20 cm³ su yer değiştirir.','900 + 20 = 920 cm³'),A('Seviye','Yer değiştiren hacim 960’tan 920’ye düşer; su seviyesi alçalır.','I doğru'),A('Basınç','Seviye alçaldığından taban basıncı azalır; III yanlış.','I ve II')],
 puf='Yüzen buz eriyince seviye değişmez; içindeki cisim özkütlesi sudan büyükse seviye alçalır, küçükse değişmez.')
Mi,Mk,dk=900,20,Fr(1,2); Vk=Mk/dk; assert (Mi+Mk)/(Mi/Fr(9,10)+Vk)<1; yer0=Mi+Mk; yer1=Mi+Mk; assert yer0==yer1 and dk<1
S6k=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
mk(P,'0006',True,metin='Şekildeki kapta su ve içinde özkütlesi 0,5 g/cm³ olan bir mantar parçası bulunan, yüzen bir buz parçası vardır. Buz parçasının ve mantarın birlikte özkütlesi suyun özkütlesinden küçüktür.\nBuz tamamen eriyip dengeye ulaştığında;\nI. Kaptaki su seviyesi değişmez.\nII. Mantar kabın dibine batar.\nIII. Kabın tabanındaki sıvı basıncı değişmez.\nifadelerinden hangileri doğrudur?',
 sekil=kaplar(kap(115,0.7,dict(f=0.88,w=44,h=40,etk='buz'),'su')),
 dogru='I ve III',sira=S6k,yan=[('Yalnız I','Seviyenin değişmemesinin taban basıncını da değiştirmediğini (III) atlamış.','dikkat'),('Yalnız II','Mantarın özkütlesi sudan küçük; mantar batmaz, yüzer.','bilgi'),('Yalnız III','Seviyenin değişmediğini (I) görmemiş.','dikkat'),('I ve II','Mantarın dibe battığını sanmış; özkütlesi sudan küçük olduğundan yüzer.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['Mantarın özkütlesi suyunkinden küçük mü? Buz eriyince mantara ne olur?','Önce yer değiştiren su kütlesi, buz ile mantarın toplam kütlesine eşit.','Erimeden sonra buzun suyu ve yüzen mantar toplam kaç gram sıvı yer değiştirir?'],
 ad=[A('Eriyen buzun mantarı','Buz eriyince mantar serbest kalır; özkütlesi (0,5 g/cm³) sudan küçük olduğundan yüzer.','II yanlış'),A('Önceki durum','Buz ve mantar birlikte yüzerken yer değiştirdikleri su kütlesi, kendi toplam kütlelerine eşittir.','900 + 20 = 920 g su yer değiştirir'),A('Sonraki durum','Eriyen buz 900 g su olur; yüzen mantar kendi kütlesi kadar (20 g) su yer değiştirir.','900 + 20 = 920 g'),A('Seviye ve basınç','Yer değiştiren su miktarı aynı kaldığından seviye değişmez; taban basıncı da değişmez.','I doğru · III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')])
bitir(P,'kaldirma','fiz|Sıvıların Kaldırma Kuvveti')
