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
KONU='Isı, Sıcaklık ve Genleşme'
P=Parti('isi','Isı, Sıcaklık ve Genleşme','fiz|Isı, Sıcaklık ve Genleşme',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 (ısıl denge, enerji iletimi, genleşme) · MEB 9. sınıf'
kart('K-FZIS-01','Isıl denge sıcaklığı','Aynı maddeden karışımda Tson = (m₁T₁ + m₂T₂)/(m₁ + m₂).','Ortalama almak ya da kütleleri ters yerleştirmek.','kolay','düz',2,'fz-is-denge','Isıl denge',KY)
kart('K-FZIS-02','Q = m·c·ΔT','Verilen ısıdan sıcaklık artışı, oradan son sıcaklık bulunur.','Öz ısıyı unutmak; ΔT’yi son sıcaklık sanmak.','orta','hikâyeli',3,'fz-is-q','Isı alışverişi ve öz ısı',KY)
kart('K-FZIS-03','Öz ısı oranı (tablo)','Aynı ısıtıcıda Q = P·t; c = P·t / (m·ΔT).','Yalnız süre ya da yalnız ΔT oranına bakmak.','orta','tablo',3,'fz-is-ozisi','Öz ısı karşılaştırması',KY)
kart('K-FZIS-04','Enerji iletim yolları','İletim ve konveksiyon maddesel ortam ister; ışıma boşlukta da olur.','Işımayı da ortam gerektiriyor sanmak.','orta','öncüllü',2,'fz-is-iletim','Enerji iletim yolları',KY)
kart('K-FZIS-05','Boyca genleşme oranları','ΔL = α·L·ΔT; ilişkili oranlar birlikte uygulanır.','Bir oranı atlamak.','zor','hikâyeli',4,'fz-is-genlesme','Boyca genleşme',KY)
kart('K-FZIS-06','Buz–su karışımı','Önce suyun 0 °C’ye inerken verdiği ısı ile buzun erime ısısı karşılaştırılır; artan ısı tüm kütleyi ısıtır.','Erime ısısını unutmak.','zor','hikâyeli',5,'fz-is-hal','Hâl değişimi ve ısıl denge',KY)
# 0001
m1,T1,m2,T2=200,20,300,70; Ts=Fr(m1*T1+m2*T2,m1+m2); assert Ts==50 and Fr(m1*T2+m2*T1,m1+m2)==40 and (T1+T2)/2==Fr(45)
mk(P,'0001',tipId='fz-is-denge',tip='Isıl denge',z='kolay',alt='Isıl Denge',kaz='Aynı maddeden sıvıların karışımında ısıl denge sıcaklığını bulur.',kalip='düz',adim=2,
 kart='K-FZIS-01 (aynı maddeden karışım) · yeni kütle ve sıcaklıklar',
 metin='Sıcaklığı 20 °C olan 200 g su ile sıcaklığı 70 °C olan 300 g su yalıtılmış bir kapta karıştırılıyor.\nIsı kaybı olmadığına göre ısıl denge sıcaklığı kaç °C olur?',
 dogru=50,yan=[(20,'Soğuk suyun sıcaklığını denge sıcaklığı sanmış.','dikkat'),(40,'Kütleleri ters yerleştirmiş: 200 × 70 ile 300 × 20’yi toplamış.','dikkat'),(45,'İki sıcaklığın aritmetik ortalamasını almış; kütlelerin farklı olduğunu hesaba katmamış.','bilgi'),(70,'Sıcak suyun sıcaklığını denge sıcaklığı sanmış.','dikkat')],
 istenen='Isıl denge sıcaklığı (°C).',ip=['Soğuyan suyun verdiği ısı, ısınan suyun aldığı ısıya eşittir.'],
 bilgi=[B('Isıl denge','sıcak madde verdiği kadar ısıyı soğuk madde alır: Q(verilen) = Q(alınan), Q = m × c × ΔT. Aynı maddede c sadeleşir. Örnek: 100 g 10 °C ile 100 g 30 °C su karışınca denge 20 °C’de olur')],
 ad=[A('Eşitliği kur','Verilen ısı alınan ısıya eşit; aynı maddede c sadeleşir.','m₁ × (T − T₁) = m₂ × (T₂ − T)'),A('Değerleri yaz','Soğuk su 20 °C’den, sıcak su 70 °C’den denge sıcaklığı T’ye gelir.','200 × (T − 20) = 300 × (70 − T)'),A('T’yi çöz','Parantezleri aç, T’li terimleri topla.','200T − 4000 = 21000 − 300T · 500T = 25000'),A('Sonuç','Denge sıcaklığı iki sıcaklık arasında kalır.','T = 50 °C')],
 puf='Aynı maddelerde Tson = (m₁T₁ + m₂T₂) ÷ (m₁ + m₂); çok kütleli olan sıcaklığa daha yakındır.')
# 0002
m,c,Q,Ti=250,Fr(2,5),4000,20; 
assert m*c*(60-Ti)==Q and m*c*Ti==2000 and m*60*c==6000 and m*(60-Ti)==10000 and m*c*(60+Ti)==8000
mk(P,'0002',tipId='fz-is-q',tip='Isı alışverişi ve öz ısı',z='orta',alt='Isı ve Sıcaklık',kaz='Madde için alınan ısıyı Q = m·c·ΔT bağıntısıyla hesaplar.',kalip='hikâyeli',adim=3,
 kart='K-FZIS-02 (Q = m c ΔT) · yeni madde, ısı istenen',
 metin='Öz ısısı 0,4 cal/g·°C olan maddeden yapılmış 250 g kütleli bir cismin sıcaklığı 20 °C’den 60 °C’ye çıkarılıyor.\nBuna göre cismin aldığı ısı kaç cal’dir?',
 dogru=4000,yan=[(2000,'ΔT yerine ilk sıcaklığı (20 °C) kullanmış.','dikkat'),(6000,'ΔT yerine son sıcaklığı (60 °C) kullanmış.','dikkat'),(8000,'Sıcaklıkları toplamış (20 + 60) ve ΔT almamış.','bilgi'),(10000,'Öz ısıyı çarpıma katmamış (250 × 40).','dikkat')],
 istenen='Cismin aldığı ısı (cal).',ip=['ΔT son ve ilk sıcaklığın farkıdır; Q = m × c × ΔT.'],
 bilgi=[B('Öz ısı ve ısı','1 g maddenin sıcaklığını 1 °C artırmak için gereken ısıya öz ısı (c) denir. Alınan ısı Q = m × c × ΔT. Örnek: 100 g su (c = 1 cal/g·°C) 10 °C ısınırsa 100 × 1 × 10 = 1000 cal alır')],
 ad=[A('Sıcaklık değişimi','ΔT, son sıcaklıktan ilk sıcaklığın çıkarılmasıdır.','ΔT = 60 − 20 = 40 °C'),A('Bağıntıyı yaz','Kütle, öz ısı ve ΔT çarpılır.','Q = m × c × ΔT'),A('Hesapla','Değerleri yerine koy.','Q = 250 × 0,4 × 40 = 4000 cal')],
 puf='Isı sorularında önce ΔT’yi bul; sonra m × c × ΔT çarpımını yap.')
# 0003 tablo
tX,dX,tY,dY=2,20,4,10; r=Fr(tX,dX)/Fr(tY,dY); assert r==Fr(1,4) and Fr(tX,tY)==Fr(1,2) and Fr(dX,dY)==2 and 1/r==4
mk(P,'0003',tipId='fz-is-ozisi',tip='Öz ısı karşılaştırması',z='orta',alt='Isı ve Sıcaklık',kaz='Aynı ısıtıcıyla ısıtılan eşit kütleli sıvıların öz ısılarını karşılaştırır.',kalip='tablo',adim=3,
 kart='K-FZIS-03 (aynı ısıtıcıyla öz ısı oranı) · yeni süreler ve sıcaklık artışları',
 metin='Kütleleri eşit X ve Y sıvıları, birim zamanda sabit ısı veren özdeş ısıtıcılarla ısıtılıyor. Isı kaybı yoktur.\nSıvı | Isıtma süresi | Sıcaklık artışı\nX | 2 dk | 20 °C\nY | 4 dk | 10 °C\nBuna göre X’in öz ısısının Y’nin öz ısısına oranı (cX/cY) kaçtır?',
 dogru=Fr(1,4),yan=[(Fr(1,2),'Yalnızca süre oranına (2/4) bakmış; sıcaklık artışlarını katmamış.','dikkat'),(1,'Öz ısıların eşit olduğunu düşünmüş.','bilgi'),(2,'Yalnızca sıcaklık artışı oranına (20/10) bakmış.','dikkat'),(4,'Oranı ters yazmış (cY/cX).','islem')],
 istenen='cX/cY oranı.',ip=['Alınan ısı süreyle orantılıdır; c = Q ÷ (m × ΔT).'],
 bilgi=[B('Öz ısı','c = Q ÷ (m × ΔT). Sabit ısıtıcıda Q, ısıtma süresiyle orantılıdır. Örnek: aynı kütlede 3 kat ısı alıp aynı ısınan maddenin öz ısısı 3 kat büyüktür')],
 ad=[A('Isıyı süreyle ilişkilendir','Isıtıcı birim zamanda sabit ısı verir; QX = P × 2, QY = P × 4.','QX : QY = 2 : 4'),A('Bağıntıyı kur','Kütleler eşit olduğundan sadeleşir.','c = Q ÷ (m × ΔT)'),A('Oranla','Değerleri yerine koy.','cX/cY = (2 ÷ 20) ÷ (4 ÷ 10) = 0,1 ÷ 0,4'),A('Sonuç','Oran sadeleştirilir.','cX/cY = 1/4')],
 puf='Aynı ısıtıcı ve eşit kütlede öz ısı oranı = (süre ÷ ΔT) oranıdır.')
# 0004
S=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
mk(P,'0004',tipId='fz-is-iletim',tip='Enerji iletim yolları',z='orta',alt='Enerji İletim Yolları ve Enerji İletim Hızı',kaz='İletim, konveksiyon ve ışıma yollarının maddesel ortam gereksinimini ayırt eder.',kalip='öncüllü',adim=2,
 kart='K-FZIS-04 (iletim yolları) · yeni günlük örnekler',
 metin='I. Çay bardağına konulan metal kaşığın sapının ısınması\nII. Kaynayan tencerede suyun alt ve üst katmanlarının ısınması\nIII. Güneş’ten gelen enerjinin Dünya’ya ulaşması\nYukarıdaki olaylardan hangilerinde enerji aktarımı için maddesel bir ortam gereklidir?',
 dogru='I ve II',sira=S,yan=[('Yalnız I','II’deki sıvı akışıyla (konveksiyon) olan aktarımın da maddesel ortam istediğini görememiş.','dikkat'),('Yalnız III','Güneş enerjisinin ışımayla ve boşlukta yayıldığını (ortam gerektirmediğini) bilememiş.','bilgi'),('I ve III','II’yi atlayıp III’ü maddesel ortam gerektiriyor sanmış.','bilgi'),('II ve III','Işımayı ortam gerektiren sanmış; I’deki iletimi atlamış.','bilgi')],
 istenen='Maddesel ortam gerektiren olayların hangileri olduğu.',ip=['Işıma yolunda enerji boşlukta da yayılabilir.'],
 bilgi=[B('Enerji iletim yolları','iletim: maddenin molekülleri aracılığıyla (metal çubuk) · konveksiyon: sıvı ve gazlarda akışkanın yer değiştirmesiyle · ışıma: ortam gerekmez, boşlukta da yayılır (Güneş’ten Dünya’ya)')],
 ad=[A('Her olayın yolu','Metal sapta iletim, kaynayan suda konveksiyon, Güneş’ten ışıma vardır.','I: iletim · II: konveksiyon · III: ışıma'),A('Ortam gereksinimi','İletim ve konveksiyonda enerji madde ile taşınır; ışıma boşlukta yayılır.','I: gerekli · II: gerekli · III: gerekmez'),A('Sonuç','Maddesel ortam gereken olaylar I ve II’dir.','I ve II')],
 puf='Işıma dışındaki iki yolda (iletim, konveksiyon) madde şarttır; ışıma boşlukta da olur.')
# 0005
dL=1; f=dL*2*3*4; assert f==24 and dL*3*4==12 and dL*2*4==8 and dL*2*3==6 and dL*(2+3+4)==9
mk(P,'0005',tipId='fz-is-genlesme',tip='Boyca genleşme',z='zor',alt='Genleşme',kaz='Boyca uzamanın boy, madde cinsi ve sıcaklık değişimiyle orantısını birlikte uygular.',kalip='hikâyeli',adim=4,
 kart='K-FZIS-05 (boyca genleşme oranları) · üç oran birlikte',
 metin='X çubuğunun sıcaklığı bir miktar artırıldığında boyu 1 mm uzuyor. Y çubuğunun ilk boyu X’inkinin 2 katı, Y’yi oluşturan maddenin boyca genleşme katsayısı X’i oluşturan maddeninkinin 3 katı, Y’nin sıcaklık artışı ise X’inkinin 4 katıdır.\nBuna göre Y çubuğunun boyu kaç mm uzar?',
 dogru=24,yan=[(6,'Sıcaklık artışının 4 katı olduğunu hesaba katmamış.','dikkat'),(8,'Genleşme katsayısının 3 kat farkını atlamış.','dikkat'),(9,'Üç oranı toplamış (2 + 3 + 4); genleşme oranları çarpılır.','bilgi'),(12,'Boy oranını (2 kat) hesaba katmamış.','dikkat')],
 istenen='Y çubuğunun boyundaki uzama (mm).',ip=['ΔL = α × L₀ × ΔT bağıntısındaki her büyüklüğün oranını ayrı ayrı bul.'],
 bilgi=[B('Boyca genleşme','ΔL = α × L₀ × ΔT (α: boyca genleşme katsayısı, L₀: ilk boy, ΔT: sıcaklık artışı). Uzama bu üç büyüklükle doğru orantılıdır. Örnek: boy 2 katı, ΔT 3 katı → uzama 6 katı')],
 ad=[A('Oranları yaz','X’e göre Y’de α 3 kat, boy 2 kat, ΔT 4 kat büyüktür.','αY/αX = 3 · L₀Y/L₀X = 2 · ΔTY/ΔTX = 4'),A('Uzamayı oranla','Üç oran çarpılır.','ΔLY/ΔLX = 3 × 2 × 4 = 24'),A('Hesapla','X’in uzaması 1 mm’dir.','ΔLY = 24 × 1 = 24 mm')],
 puf='Genleşmede uzama oranı = katsayı oranı × ilk boy oranı × sıcaklık değişimi oranıdır.')
# 0006
mb,ms,Ts,L=100,400,40,80
ver=ms*Ts; erime=mb*L; assert ver>erime; kal=ver-erime; T=Fr(kal,mb+ms)
assert T==16 and Fr(ver,mb+ms)==32 and Fr(kal,ms)==20
mk(P,'0006',tipId='fz-is-hal',tip='Hâl değişimi ve ısıl denge',z='zor',alt='Hâl Değişimi',kaz='Buz–su karışımında erime ısısını da katarak son sıcaklığı bulur.',kalip='hikâyeli',adim=5,
 kart='K-FZIS-06 (buz–su karışımı) · yeni kütleler',
 metin='0 °C’de 100 g buz, 40 °C’de 400 g suyun bulunduğu yalıtılmış kaba konuyor. Buzun erime ısısı 80 cal/g, suyun öz ısısı 1 cal/g·°C’dir ve ısı kaybı yoktur.\nBuna göre ısıl denge sıcaklığı kaç °C olur?',
 dogru=16,yan=[(0,'Buzun tamamen erimediğini düşünmüş; su 0 °C’ye inerken verdiği ısının buzu eritmeye yettiğini hesaplamamış.','dikkat'),(20,'Erimiş buzun da ısınacağını katmamış; yalnız suyun kütlesine bölmüş.','dikkat'),(32,'Erime ısısını hiç hesaba katmamış.','bilgi'),(40,'Suyun sıcaklığının hiç değişmediğini sanmış.','dikkat')],
 istenen='Isıl denge sıcaklığı (°C).',ip=['Önce suyun 0 °C’ye inerken vereceği ısı ile buzu tamamen eritmek için gereken ısıyı karşılaştır.'],
 bilgi=[B('Erime ısısı','erime sırasında sıcaklık değişmeden Q = m × L ısı alınır (L: erime ısısı). Örnek: 10 g buzu eritmek için 10 × 80 = 800 cal gerekir'),B('Isıl denge','verilen ısı alınan ısıya eşittir; Q = m × c × ΔT')],
 ad=[A('Suyun verebileceği ısı','Su 40 °C’den 0 °C’ye inerken verir.','Q = 400 × 1 × 40 = 16000 cal'),A('Buzun erime ısısı','Buz 0 °C’de erirken ısı alır.','Q = 100 × 80 = 8000 cal'),A('Karşılaştır','16000 > 8000 olduğundan buzun tamamı erir, artan ısı 500 g suyu ısıtır.','kalan ısı = 16000 − 8000 = 8000 cal'),A('Son sıcaklık','Artan ısı toplam su kütlesinin (400 + 100) sıcaklığını yükseltir.','8000 = 500 × 1 × T'),A('Sonuç','T hesaplanır.','T = 16 °C')],
 puf='Buz–su karışımında önce “buz tamamen erir mi?” sorusunu ısıları karşılaştırarak yanıtla.')
bitir(P,'isi','fiz|Isı, Sıcaklık ve Genleşme')
