"""AYT Biyoloji · Canlılar ve Çevre · 20 soru (kardeş yok, ipucu 1). Şekil verileri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_bio as H
from _hafif_bio import *
H.KONU='Canlılar ve Çevre'
P=Parti('cevre','Canlılar ve Çevre','abio|Canlılar ve Çevre',ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2026 Biyoloji (Canlılar ve Çevre; yalnız mantık) · MEB 12. sınıf biyoloji'
TIPLER={'cv-karbon':'Karbon döngüsü','cv-azot':'Azot ve fosfor döngüsü','cv-su':'Su döngüsü ve bitki örtüsü','cv-enerji':'Enerji akışı ve besin piramitleri',
 'cv-birikim':'Biyolojik birikim','cv-sorun':'Çevre sorunları','cv-bioc':'Biyoçeşitlilik','cv-koruma':'Koruma ve sürdürülebilir kullanım'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-ABCEV-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-ABCEV-{kn:02d} ('+CARD[kn]+')',**k)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)),'yer'; return sira
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
def pg(axis_body,extra=''): return tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+axis_body+'\n\\end{tikzpicture}')
OKS='-{Stealth[length=2.4mm,width=2mm]}'
# ---------- öncüllü yardımcı (şık sırası alışılmış: Yalnız I … I, II ve III)
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
    ad=[A(f'{n}. yargıyı değerlendir',why[i][0].upper()+why[i][1:]+'.',f'{n}. yargı '+('doğru' if truth[i] else 'yanlış')) for i,n in enumerate(nm)]
    ad.append(A('Sonucu yaz','Doğru yargılar bir arada okunur.',f'Doğru olan: {dogru}'))
    return dict(dogru=dogru,sira=sira,yan=yan,ad=ad)
def qo(no,truth,why,pos,**k):
    o=onc(truth,why,pos); q(no,o['ad'],dogru=o['dogru'],sira=o['sira'],yan=o['yan'],**k)
# ---------- şekil yardımcıları
def barplot(labels,series,ymax,yl,ytick,width=8.2,bw=6,rot=0,xl=''):
    n=len(labels); xt=','.join(str(i) for i in range(n)); lab=','.join(labels)
    ax=(f'\\begin{{axis}}[ybar,bar width={bw}pt,width={width}cm,height=5.8cm,ymin=0,ymax={ymax},xmin=-.6,xmax={n-.4},xtick={{{xt}}},xticklabels={{{lab}}},ytick={{{ytick}}},axis lines=left,'
        f'ylabel={{{yl}}},xlabel={{{xl}}},nodes near coords,every node near coord/.append style={{font=\\scriptsize}},tick label style={{font=\\footnotesize}},label style={{font=\\small}},'
        f'x tick label style={{rotate={rot},anchor={"east" if rot else "north"},align=center}},legend style={{at={{(0.5,1.03)}},anchor=south,font=\\footnotesize,draw=none,legend columns=-1}}]')
    body=[ax]
    for nm,fill,vals in series:
        body.append(f'\\addplot[draw=black,fill={fill}] coordinates {{'+' '.join(f'({i},{v})' for i,v in enumerate(vals))+'};')
    body.append('\\legend{'+','.join(s[0] for s in series)+'}'); body.append('\\end{axis}')
    return pg('\n'.join(body))
def kutu(x,y,t,w=2.3): return f'\\node[draw,rounded corners=2pt,inner sep=3pt,line width=.9pt,font=\\footnotesize,minimum width={w}cm,align=center] at ({x},{y}) {{{t}}};'
def rakam(x,y,n): return f'\\node[circle,draw,inner sep=1.2pt,fill=white,font=\\footnotesize\\bfseries] at ({x},{y}) {{{n}}};'

# ===================== bilgi kutuları
KAR=B('Karbon döngüsü','karbon; atmosfer, canlılar, toprak, okyanus ve fosil yakıt yatakları arasında dolaşır. Depolar arasındaki geçişler fotosentez, solunum, ayrışma, çözünme ve yanma gibi olaylarla gerçekleşir. Örnek: okyanus suyunda çözünen karbondioksit, atmosferden okyanus deposuna geçen karbondur')
KOS=B('Derişim değişimi ve hızlar','kapalı bir ortamdaki CO₂ derişimi, CO₂ bağlanma hızı (fotosentez) ile CO₂ salınma hızı (solunum, ayrışma) arasındaki farka göre değişir: salınım fazlaysa derişim artar, bağlanma fazlaysa azalır, ikisi eşitse değişmez. Örnek: ışığı kesilen kapalı bir kapta fotosentez durursa CO₂ derişimi artmaya başlar')
AZO=B('Azot döngüsünün basamakları','azot; N₂, amonyak/amonyum, nitrit, nitrat ve organik azot biçimleri arasında değişir. Azot bağlama, nitrifikasyon, denitrifikasyon ve ayrışma bu dönüşümlerin adlarıdır; her birini farklı canlı grupları gerçekleştirir')
NIT=B('Nitrifikasyon ve kontrol grubu','toprakta amonyum (NH₄⁺), bakteriler aracılığıyla önce nitrite (NO₂⁻), sonra nitrata (NO₃⁻) yükseltgenir; ara ürünün derişimi önce artıp sonra azalabilir. Canlı etkinliğini görmek için aynı örneğin bakterileri ısıtmayla öldürülmüş hâli kontrol olarak kullanılır')
FOS=B('Fosfor döngüsü','fosfor; ATP, nükleik asit ve fosfolipit gibi moleküllerin yapısında bulunur. Doğadaki fosfat bileşikleri kayaç, toprak, su ve canlılar arasında aktarılır; gübre kullanımı bu döngüyü etkileyen insan etkinliklerinden biridir')
SUD=B('Su döngüsü','su; buharlaşma ve bitkilerin terlemesiyle atmosfere, yağışla yeryüzüne geçer. Yağan suyun bir bölümü yüzeyden akar, bir bölümü toprağa sızarak yer altı suyuna karışır; bitki örtüsü bu dağılımı değiştirir')
ENJ=B('Enerji akışı','bir basamağın aldığı enerji; solunumda harcanır (ısı olarak kaybolur), ayrıştırıcılara geçen ölü ve atık maddede kalır ya da bir üst basamağa aktarılır. Enerji korunur: aldığı = solunum + ayrıştırıcıya geçen + üst basamağa geçen. Örnek: aldığı 500 birim olan basamak 300 birimini solunumda harcar, 50 birimini üst basamağa aktarırsa 150 birimi ayrıştırıcılara geçer')
BNE=B('Brüt ve net üretim','üreticilerin fotosentezle bağladığı toplam enerji brüt üretimdir; bundan kendi solunumlarında harcananın çıkarılmasıyla net üretim bulunur. Besin zincirinde bir basamakta depolanan enerjinin yaklaşık %10’u bir üst basamağa aktarılır. Örnek: brüt üretimi 1000 birim olan ve %30’unu solunumda harcayan üreticinin net üretimi 700 birimdir')
BIR=B('Biyolojik birikim','canlı vücudundan atılamayan ya da çok yavaş atılan, doğada da kolay parçalanmayan maddeler dokularda birikir ve besin zincirinde yukarı çıkıldıkça derişimleri artar. Kolay atılan ya da parçalanan maddeler birikmez')
BIK=B('Basamak başına katsayı','birikim her basamakta aynı katsayıyla artıyorsa, n basamak sonraki derişim = ilk derişim × katsayı üzeri n olur. Katsayı, ardışık iki basamağın derişim oranından bulunur')
PIR=B('Biyokütle ve üretim','biyokütle, bir basamaktaki canlıların belirli bir andaki toplam kütlesidir; yıllık üretim ise o basamakta bir yıl içinde oluşan organik madde miktarıdır. İkisi farklı kavramlardır; enerji piramidi yıllık üretim (enerji) değerlerine dayanır')
SER=B('Sera etkisi','atmosferdeki sera gazları (karbondioksit, metan, su buharı gibi) yeryüzünden yayılan ısı ışınlarının bir bölümünü tutar ve yeryüzüne geri gönderir. Doğal sera etkisi yeryüzünü yaşanabilir sıcaklıkta tutar; sera gazı derişimi arttıkça etki güçlenir')
ASI=B('Asit yağmuru','fosil yakıtlar yandığında atmosfere kükürt dioksit ve azot oksitler karışır; bu gazlar su buharıyla tepkimeye girerek asitleri oluşturur ve yağışın pH değerini düşürür. Örnek: pH değeri 5,6’nın altına inen yağışlar asit yağmuru sayılır')
OZO=B('Ozon tabakası','stratosferdeki ozon, Güneş’ten gelen mor ötesi (UV) ışınların büyük bölümünü soğurur. Kloroflorokarbon (CFC) gibi bileşikler stratosfere ulaştığında ozonu parçalar; bu bileşiklerin kullanımı uluslararası anlaşmalarla sınırlandırılmıştır')
OTR=B('Ötrofikasyon','sucul ekosistemde azot ve fosfor gibi besin tuzlarının artmasıyla alg ve su bitkilerinin aşırı çoğalmasıdır. Suda yaşayan birçok canlı, çözünmüş oksijen derişimine bağımlıdır')
CES=B('Tür çeşitliliği','bir alandaki tür çeşitliliği, tür sayısına (tür zenginliği) ve bireylerin türlere ne kadar dengeli dağıldığına bağlıdır. Örnek: aynı toplam bireyin dört türe eşit dağılması, bir türün çok baskın olduğu dağılımdan daha yüksek çeşitlilik demektir')
DUS=B('Biyoçeşitlilik düzeyleri','genetik çeşitlilik: bir türün bireyleri ve popülasyonları arasındaki gen ve alel farklılığı; tür çeşitliliği: bir bölgedeki tür sayısı ve dağılımı; ekosistem çeşitliliği: bölgedeki yaşam ortamı (ekosistem) türlerinin çeşitliliği')
TEH=B('Biyoçeşitliliği azaltan etkenler','yaşam alanının yok edilmesi ve parçalanması, aşırı avlanma, çevre kirliliği, iklim değişikliği ve yabancı (istilacı) türlerin girişi biyoçeşitliliği azaltır')
KOR=B('Koruma yöntemleri','türü doğal yaşam alanında korumaya yerinde (in situ), doğal ortamı dışında korumaya yer dışı (ex situ) koruma denir. Örnek: bir yaban hayatı geliştirme sahasının kurulması yerinde, bir türün hücrelerinin gen bankasında saklanması yer dışı korumadır')
SUR=B('Sürdürülebilir kullanım','yenilenebilir bir kaynağın kullanım hızı yenilenme hızını aşmazsa kaynak tükenmez; aşıldığında stok azalır. Yüzde artış, her yıl o yılın başındaki değer üzerinden hesaplanır')

# ===================== 01 · kolay · karbon (öncüllü)
card(1,'Karbon döngüsünde olaylar','Karbon fotosentezle organik moleküle bağlanır, yanma ve solunumla atmosfere döner; hayvanlar karbonu besinle alır.','Hayvanların karbondioksiti doğrudan alıp organik madde yaptığını sanmak; fosil yakıtları döngü dışı saymak.','kolay','öncüllü',3,'cv-karbon','karbon döngüsü, üç yargı')
qo('0001',[True,False,True],['fotosentez, atmosferdeki karbondioksitin karbonunu organik moleküllere bağlar',
  'hayvanlar karbonu, başka canlıların organik maddelerini besin olarak alarak sağlar ve karbondioksiti doğrudan organik maddeye çevirmez',
  'fosil yakıtlar yandığında yer altında depolanmış karbon karbondioksit olarak atmosfere geçer'],2,
 tipId='cv-karbon',tip=TIPLER['cv-karbon'],z='kolay',alt='Madde Döngüleri',kaz='Karbonun doğada atmosfer, canlılar ve fosil yakıtlar arasındaki dolaşımını açıklar.',kalip='öncüllü',
 metin='Karbon, ekosistemde canlılar ile cansız ortam arasında sürekli dolaşan temel elementlerden biridir. Buna göre, karbon döngüsüyle ilgili,\nI. Fotosentez yapan canlılar, atmosferdeki karbondioksitin karbonunu organik moleküllerin yapısına katar.\nII. Hayvanlar, atmosferdeki karbondioksiti doğrudan alarak vücutlarındaki organik maddeleri sentezler.\nIII. Fosil yakıtların yakılması, uzun süre yer altında depolanmış karbonu karbondioksit olarak atmosfere verir.\nyargılarından hangileri doğrudur?',
 istenen='Karbon döngüsüyle ilgili doğru yargılar.',ip=['Her yargıda karbonun hangi depodan hangi depoya, hangi olayla geçtiğini ve bu olayı hangi canlı grubunun yapabildiğini düşün.'],
 bilgi=[KAR],puf='Karbonu atmosferden organik maddeye bağlayan yol fotosentezdir; hayvanlar karbonu hazır organik madde olarak besinle alır.')

# ===================== 02 · kolay · koruma tablosu
card(2,'Yerinde ve yer dışı koruma','Türün doğal yaşam alanında korunması yerinde, yaşam alanı dışında (bank, bahçe, üretim) korunması yer dışı korumadır.','Tohum ya da gen bankasını yerinde koruma saymak; alanı koruma altına almayı yer dışı koruma saymak.','kolay','tablo',3,'cv-koruma','tabloda yanlış eşleştirilen satırı bulma')
SATIR=[('I','Tohum bankasında saklama','Doğal ortamında koruma',False),('II','Milli park ilan etme','Doğal ortamında koruma',True),('III','Hayvanat bahçesinde üretme','Doğal ortam dışında koruma',True),
       ('IV','Sulak alanı koruma altına alma','Doğal ortamında koruma',True),('V','Botanik bahçesinde yetiştirme','Doğal ortam dışında koruma',True)]
YERINDE={'Tohum bankasında saklama':False,'Milli park ilan etme':True,'Hayvanat bahçesinde üretme':False,'Sulak alanı koruma altına alma':True,'Botanik bahçesinde yetiştirme':False}
for s in SATIR: assert s[3]==(YERINDE[s[1]]==(s[2]=='Doğal ortamında koruma'))
assert [s[0] for s in SATIR if not s[3]]==['I']
SK=tablo_svg(['Satır','Koruma çalışması','Koruma yöntemi'],[[s[0],s[1],s[2]] for s in SATIR])
YAN2={'II':'Milli park ilanıyla tür, doğal yaşam alanında korunur; yerinde koruma doğru eşleştirilmiştir.','III':'Hayvanat bahçesinde üretme, türü doğal ortamının dışında korur; yer dışı koruma doğru eşleştirilmiştir.',
 'IV':'Sulak alanın koruma altına alınması türleri yaşam alanlarında korur; yerinde koruma doğru eşleştirilmiştir.','V':'Botanik bahçesinde yetiştirme bitkiyi doğal ortamı dışında korur; yer dışı koruma doğru eşleştirilmiştir.'}
q('0002',tipId='cv-koruma',tip=TIPLER['cv-koruma'],z='kolay',alt='Biyoçeşitliliğin Korunması',kaz='Yerinde ve yer dışı koruma yöntemlerini örneklerle ayırt eder.',kalip='tablo',
 metin='Biyoçeşitliliğin korunmasında kullanılan çalışmalar, türün doğal yaşam alanında korunması ya da doğal ortamının dışında korunması biçiminde gruplandırılır. Aşağıdaki tabloda beş koruma çalışması ve her birinin hangi koruma yöntemi kapsamında değerlendirildiği verilmiştir.\nBuna göre, tablodaki hangi satırda koruma yöntemi yanlıştır?',
 sekil=SK,dogru='I. satır',sira=['I. satır','II. satır','III. satır','IV. satır','V. satır'],
 yan=[('II. satır',YAN2['II'],'dikkat'),('III. satır',YAN2['III'],'dikkat'),('IV. satır',YAN2['IV'],'dikkat'),('V. satır',YAN2['V'],'dikkat')],
 istenen='Koruma yöntemi yanlış verilen satır.',ip=['Çalışmanın türü doğal yaşam alanında mı yoksa o alanın dışındaki bir yerde mi koruduğuna bak.'],bilgi=[KOR],
 ad=[A('Yöntemlerin tanımını hatırla','Doğal yaşam alanında koruma yerinde, alan dışındaki koruma yer dışı korumadır.','Yerinde: alan korunur · Yer dışı: bank, bahçe, üretim'),
     A('Satırları tek tek ele','Milli park ve sulak alan koruması alanı korur; hayvanat ve botanik bahçesi türü alan dışında tutar.','II, III, IV, V doğru eşleşmiş'),
     A('Hatalı satırı bul','Tohum bankası, tohumları yaşam alanından alıp depoda saklar; bu yer dışı korumadır.','I. satırda yöntem “yerinde” yazılmış → yanlış')],
 puf='Önce çalışmanın “nerede” yapıldığına bak: tür kendi ortamında kalıyorsa yerinde, bir bank, bahçe ya da üretim tesisindeyse yer dışı korumadır.')

# ===================== 03 · kolay · asit yağmuru (olumsuz)
card(3,'Asit yağmurunun nedeni ve etkisi','Asit yağmuru kükürt dioksit ve azot oksitlerden oluşur; ozon incelmesine yol açan CFC gazlarıyla karıştırılmamalıdır.','Asit yağmuru ile ozon incelmesinin gazlarını ve sonuçlarını birbirine karıştırmak.','kolay','düz',3,'cv-sorun','asit yağmuru, söylenemeyen ifade')
D3='Oluşumunda en etkili gazlar, ozon tabakasının incelmesine yol açan CFC gazlarıdır.'
Y3=['Yağmur suyunun pH değerinin normal yağmur suyuna göre daha düşük olmasına yol açar.','Göl sularının pH değerini düşürerek sucul canlıların yaşamını olumsuz etkileyebilir.',
    'Toprağın kimyasal yapısını değiştirerek bitkilerin mineral alımını güçleştirebilir.','Mermer ve kireç taşı gibi yapı malzemelerinin aşınmasını hızlandırır.']
q('0003',tipId='cv-sorun',tip=TIPLER['cv-sorun'],z='kolay',alt='Çevre Sorunları',kaz='Asit yağmurunun oluşumunu ve ekosistem üzerindeki etkilerini açıklar.',kalip='düz',
 metin='Fosil yakıtların yanması sonucu atmosfere karışan bazı gazlar, havadaki su buharıyla tepkimeye girerek yağışın normalden daha asidik olmasına neden olur. Bu yağışlar ormanlara, göllere ve yapılara zarar verir.\nBuna göre, asit yağmurlarıyla ilgili aşağıdakilerden hangisi söylenemez?',
 sekil=None,dogru=D3,sira=yer('D',D3,Y3),
 yan=[(Y3[0],'Asit yağmurunun tanımı budur; yağışın pH değeri normalin altındadır. Bu ifade söylenebilir.','dikkat'),(Y3[1],'Göllere karışan asidik yağış pH değerini düşürür ve balık gibi canlıları etkiler. Bu ifade söylenebilir.','dikkat'),
      (Y3[2],'Asidik yağış toprakta mineral dengesini bozar ve bitkilerin beslenmesini olumsuz etkileyebilir. Bu ifade söylenebilir.','dikkat'),(Y3[3],'Kireç taşı ve mermer asitlerle tepkimeye girer; asit yağmurları bu malzemeleri aşındırır. Bu ifade söylenebilir.','dikkat')],
 istenen='Asit yağmurlarıyla ilgili söylenemeyen ifade.',ip=['Asit yağmurunu oluşturan gazların hangi etkinliklerden geldiğini ve ozon tabakasını inceltenlerle aynı olup olmadığını düşün.'],bilgi=[ASI],
 ad=[A('Nedeni hatırla','Asit yağmuru, yanma ürünü kükürt dioksit ve azot oksitlerden oluşur.','Neden: SO₂ ve NOx'),
     A('Etkileri ele','Düşük pH göl, toprak ve yapılar üzerinde olumsuz etki yapar.','Dört ifade bu etkilerle uyumlu'),
     A('Yanlış ifadeyi seç','CFC gazları ozon tabakasını inceltir; asit yağmurunun asıl nedeni değildir.','CFC ifadesi söylenemez')],
 puf='Asit yağmuru: SO₂ ve NOx, ozon incelmesi: CFC, sera etkisi: CO₂ ve CH₄ gibi gazlar. Üç sorunu gazlarıyla eşleştir.')

# ===================== 04 · orta · karbon dioksit günlük grafik (öncüllü)
card(4,'Günlük CO₂ derişimi grafiği','Derişimin artması salımın bağlanmadan, azalması bağlanmanın salımdan fazla olduğunu; sabit kalması ikisinin eşit olduğunu gösterir; solunum gün boyu sürer.','Gündüz solunumun durduğunu sanmak; derişimin en düşük olduğu noktada fotosentezin en hızlı olduğunu sanmak.','orta','grafik',4,'cv-karbon','orman havasında günlük CO₂ eğrisi')
def C4(t): return 385+25*math.cos(2*math.pi*(t-6)/24)
pts4=' '.join(f'({t:.1f},{C4(t):.2f})' for t in range(0,25))
assert C4(2)>C4(1.5) and C4(12)<C4(11.5) and abs(C4(18)-360)<1e-9 and min(C4(t/10) for t in range(241))>=360-1e-9
b=['\\begin{axis}[width=8.4cm,height=5.4cm,xmin=0,xmax=24,ymin=350,ymax=420,xtick={0,6,12,18,24},ytick={360,380,400},axis lines=left,xlabel={Günün saati},ylabel={CO$_2$ derişimi (ppm)},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
   f'\\addplot[black,smooth] coordinates {{{pts4}}};',
   f'\\addplot[only marks,mark=*,mark size=2.4pt,vurgu] coordinates {{(2,{C4(2):.2f}) (12,{C4(12):.2f}) (18,{C4(18):.2f})}};',
   f'\\node[font=\\small\\bfseries,above left] at (axis cs:2,{C4(2)+.5:.1f}) {{K}};\\node[font=\\small\\bfseries,above right] at (axis cs:12,{C4(12)+1:.1f}) {{L}};\\node[font=\\small\\bfseries,below] at (axis cs:18,{C4(18)-2:.1f}) {{M}};','\\end{axis}']
SK=pg('\n'.join(b))
qo('0004',[True,True,False],['K noktasında derişim artmaktadır; bu, salınan karbondioksidin bağlanandan fazla olduğunu gösterir',
  'M noktasında derişim değişmemektedir (eğrinin en düşük noktası); bu, bağlanan ve salınan karbondioksit miktarlarının eşit olduğunu gösterir',
  'L noktasında derişimin azalması, bağlanmanın salımdan fazla olmasındandır; hücresel solunum gündüz de sürer'],1,
 tipId='cv-karbon',tip=TIPLER['cv-karbon'],z='orta',alt='Madde Döngüleri',kaz='Ekosistemde günlük karbondioksit derişimi değişimini fotosentez ve solunum hızlarıyla ilişkilendirir.',kalip='grafik',
 metin='Büyük bir ormanın içinde, tepe tacı yüksekliğindeki havada ölçülen karbondioksit derişiminin bir gün boyunca değişimi grafikte gösterilmiştir. Orman havasının dış ortamla karbondioksit alışverişi ihmal edilmekte, K, L ve M noktaları grafik üzerinde işaretlenmektedir.\nBuna göre,\nI. K noktasında ekosistemdeki karbondioksit salımı, karbondioksit bağlanmasından fazladır.\nII. M noktasında fotosentezle bağlanan karbondioksit miktarı, solunumla salınan karbondioksit miktarına eşittir.\nIII. L noktasında hücresel solunum durmuştur.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Grafiğe göre doğru yargılar.',ip=['Eğrinin eğiminin yönüne ve eğimin sıfır olduğu noktaya bak: derişim artıyor, azalıyor ya da değişmiyor olabilir.'],bilgi=[KOS],
 puf='Derişimin yönünü bağlanma–salım farkı belirler; solunum canlıda gün boyu sürdüğü için “solunum durdu” yargısı hiçbir noktada doğru olmaz.')

# ===================== 05 · zor · nitrifikasyon grafiği
card(5,'Nitrifikasyon deneyi ve kontrol','Ardışık dönüşümde ara ürünün derişimi önce artıp sonra azalır; son ürün sürekli artar; bakterileri öldürülmüş kontrol grubunda dönüşüm gözlenmez.','Ara ürünün tepe yaptığı anda son ürünün henüz oluşmadığını sanmak; ısıtılmış toprakta dönüşümün kendiliğinden süreceğini sanmak.','zor','grafik',5,'cv-azot','nitrifikasyon: amonyum–nitrit–nitrat eğrileri ve kontrol')
k1,k2=0.20,0.15
NH=lambda t:100*math.exp(-k1*t); NO2=lambda t:400*(math.exp(-k2*t)-math.exp(-k1*t)); NO3=lambda t:100-NH(t)-NO2(t)
tp=math.log(k1/k2)/(k1-k2); assert 5<tp<6.5
g=[i/2 for i in range(0,61)]
assert all(NH(a)>NH(b) for a,b in zip(g,g[1:])) and all(NO3(a)<NO3(b) for a,b in zip(g,g[1:])) and NO3(0.5)>NO3(0) and NO2(tp)==max(NO2(t) for t in g+[tp])
assert all(NO2(a)>NO2(b) for a,b in zip(g,g[1:]) if a>7) and abs(NH(10)+NO2(10)+NO3(10)-100)<1e-9 and NO3(30)>90
cv=lambda f:' '.join(f'({t:.1f},{f(t):.2f})' for t in g[::2])
b=['\\begin{axis}[width=8.4cm,height=5.6cm,xmin=0,xmax=30,ymin=0,ymax=105,xtick={0,5,10,15,20,25,30},ytick={0,50,100},axis lines=left,xlabel={Zaman (gün)},ylabel={Derişim (göreli birim)},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
   f'\\addplot[black,smooth] coordinates {{{cv(NH)}}};',f'\\addplot[vurgu,smooth] coordinates {{{cv(NO2)}}};',f'\\addplot[black,dashed,smooth] coordinates {{{cv(NO3)}}};',
   '\\node[font=\\small,anchor=west] at (axis cs:2.2,80) {\\ce{NH4+}};\\node[font=\\small,anchor=west,vurgu] at (axis cs:9.5,43) {\\ce{NO2-}};\\node[font=\\small,anchor=south] at (axis cs:24,95) {\\ce{NO3-}};','\\end{axis}']
SK=pg('\n'.join(b))
D5='Nitrit derişimi en yüksek değerine ulaştıktan sonra azalırken nitrat derişimi artmaktadır; ısıtılmış toprakta amonyumun nitrite ve nitrata dönüşümü gözlenmez.'
Y5=['Nitrit derişiminin en yüksek değere ulaştığı ana kadar nitrat oluşumu hiç başlamamıştır; ısıtılmış toprakta da dönüşümler aynı hızda sürer.',
    'Nitrat derişimi artarken amonyum derişimi de artmaktadır; ısıtılmış toprakta dönüşümler gözlenmez.',
    'Nitrit derişimi en yüksek değerine ulaştıktan sonra azalırken nitrat derişimi artmaktadır; ısıtılmış toprakta dönüşümler canlı etkinliği olmadan da aynı hızda sürer.',
    'Amonyumun nitrata dönüşümü oksijensiz ortamda hızlanır; ısıtılmış toprakta dönüşümler gözlenmez.']
q('0005',tipId='cv-azot',tip=TIPLER['cv-azot'],z='zor',alt='Azot Döngüsü',kaz='Nitrifikasyon deneyinin zaman grafiğini yorumlar ve kontrol grubu sonucunu öngörür.',kalip='grafik',
 metin='Havalandırılan ve nemli tutulan, bitkisiz bir toprak örneğine deneyin başında amonyum tuzu eklenmiş; topraktaki amonyum, nitrit ve nitrat iyonlarının derişimleri 30 gün boyunca ölçülmüş ve sonuçlar grafikte gösterilmiştir. Aynı deney, aynı topraktan alınıp ısıtılarak içindeki bakterileri öldürülmüş bir örnekle de yürütülmüştür.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 sekil=SK,dogru=D5,sira=yer('E',D5,Y5),
 yan=[(Y5[0],'Grafikte nitrat derişimi başlangıçtan itibaren artmaktadır; nitrit tepe yaparken nitrat oluşumu çoktan başlamıştır. Isıtılmış toprakta bakteriler öldüğü için dönüşüm de gözlenmez.','bilgi'),
      (Y5[1],'Amonyum derişimi grafikte sürekli azalmaktadır; amonyum nitrite ve nitrata dönüşerek tükenir.','dikkat'),
      (Y5[2],'Nitrit ve nitrat gelişimi bu yargıda doğru okunmuş; ancak dönüşümü yapan canlılar ısıtmayla öldürüldüğünden kontrol örneğinde dönüşüm gözlenmez.','bilgi'),
      (Y5[3],'Amonyumun nitrite ve nitrata yükseltgenmesi oksijen gerektirir; oksijensiz ortamda yavaşlar. Isıtılmış topraktaki sonuç doğru ama nedeni yanlış öngörülmüş.','bilgi')],
 istenen='Grafik ve kontrol deneyi sonucuna göre doğru ifade.',ip=['Üç eğrinin zamanla nasıl değiştiğini ayrı ayrı oku; bakterilerin öldürülmesinin dönüşümleri nasıl etkileyeceğini düşün.'],bilgi=[AZO,NIT],
 ad=[A('Eğrileri oku','Amonyum sürekli azalır, nitrat sürekli artar, nitrit önce artıp sonra azalır.','NH₄⁺ azalır, NO₃⁻ artar, NO₂⁻ tepe yapar'),
     A('Ara ürünü yorumla','Nitrit tepe yaptıktan sonra azaldığı hâlde nitrat artmaya devam eder; nitrit, nitrata dönüşmektedir.','Nitrit azalışı = nitrat artışı'),
     A('Kontrol örneğini düşün','Dönüşümleri bakteriler yapar; ısıtılmış toprakta bakteri yoktur.','Isıtılmış toprakta dönüşüm yok'),
     A('İfadeleri karşılaştır','Yalnız bir ifade hem grafiği hem kontrolü doğru yorumlar.','Doğru ifade bulundu')],
 puf='Ardışık dönüşümlerde ara ürün önce birikir sonra azalır, son ürün sürekli artar; canlı etkinliğiyle yürüyen süreç, canlıları öldürülmüş kontrolde durur.')

# ===================== 06 · orta · azot döngüsü (öncüllü)
card(6,'Azot bağlama ve denitrifikasyon','Nodül bakterileri N₂’yi amonyağa çevirir; denitrifikasyon nitratı N₂’ye çevirir ve oksijensiz toprakta artar; bitkiler N₂ kullanamaz.','Nodül bakterilerinin N₂’yi doğrudan nitrata çevirdiğini sanmak; bitkilerin atmosferik azotu doğrudan aldığını sanmak.','orta','öncüllü',3,'cv-azot','azot döngüsü, üç yargı')
qo('0006',[False,True,False],['nodül bakterileri azot gazını amonyağa (amonyuma) çevirir; nitrata dönüşüm başka bakterilerce yapılır',
  'oksijeni az ortamda denitrifikasyon bakterileri nitratı azot gazına çevirir ve toprak azot kaybeder',
  'bitkiler azot gazını doğrudan kullanamaz; azotu toprakta amonyum ve nitrat iyonları olarak alır'],0,
 tipId='cv-azot',tip=TIPLER['cv-azot'],z='orta',alt='Azot Döngüsü',kaz='Azot bağlama, nitrifikasyon ve denitrifikasyonun gerçekleştiği koşulları ve canlı gruplarını ayırt eder.',kalip='öncüllü',
 metin='Azot, proteinlerin ve nükleik asitlerin yapısında bulunan, doğada döngüsel olarak dolaşan bir elementtir. Buna göre azot döngüsüyle ilgili,\nI. Baklagil köklerindeki nodüllerde yaşayan bakteriler, atmosferdeki azot gazını doğrudan nitrata dönüştürür.\nII. Su altında kalıp oksijeni azalan topraklarda nitratı azot gazına çeviren bakteriler, toprağın azotça fakirleşmesine neden olabilir.\nIII. Bitkiler, protein sentezi için gereken azotu atmosferdeki azot gazından yaprak gözenekleriyle doğrudan alır.\nyargılarından hangileri doğrudur?',
 istenen='Azot döngüsüyle ilgili doğru yargılar.',ip=['Her yargıda azotun hangi biçimden hangi biçime geçtiğini ve bunu hangi canlı grubunun hangi koşulda yaptığını sorgula.'],bilgi=[AZO],
 puf='Azot gazını bağlayan nodül bakterileri amonyak üretir; nitrata dönüşüm nitrifikasyon bakterilerinindir; N₂’ye dönüş ise denitrifikasyondur.')

# ===================== 07 · orta · biyolojik birikim sütun grafiği (öncüllü)
card(7,'İki maddenin birikimini karşılaştırma','Birikim yapan madde basamak yükseldikçe artar ve son basamakta en yüksektir; birikmeyen madde basamaklar arasında belirgin değişmez.','Son basamağı ilk basamak sanmak; derişimi sabit kalan maddenin de biriktiğini sanmak.','orta','grafik',3,'cv-birikim','X artan, Y sabit sütun grafiği')
ORG=['Fitoplankton','Zooplankton','Küçük balık','Büyük balık','Balıkçıl']
XV=[1,3,9,27,81]; YV=[4,3,4,4,3]
assert all(XV[i+1]==3*XV[i] for i in range(4)) and max(YV)-min(YV)<=1 and XV.index(max(XV))==4
SK=barplot(['Fito-\\\\plankton','Zoo-\\\\plankton','Küçük\\\\balık','Büyük\\\\balık','Balıkçıl'],[('X maddesi','vurgu!70',XV),('Y maddesi','gray!35',YV)],95,'µg/kg','0,20,40,60,80',width=8.2,bw=7,rot=0)
qo('0007',[False,True,True],['X’in derişimi basamak yükseldikçe artar ve en yüksek değere zincirin son basamağında ulaşır',
  'X’in derişimi basamaklar boyunca artmaktadır, Y’nin derişimi ise belirgin biçimde değişmemektedir',
  'derişimi basamaklarla artan bir madde canlı vücudundan atılamıyor ya da çok yavaş atılıyordur'],3,
 tipId='cv-birikim',tip=TIPLER['cv-birikim'],z='orta',alt='Biyolojik Birikim',kaz='Besin zincirinde derişimi basamaklarla değişen maddelerin grafiğini yorumlayarak biyolojik birikimi açıklar.',kalip='grafik',
 metin='Bir göldeki besin zincirinde yer alan beş canlı grubunun dokularında X ve Y adlı iki yabancı maddenin derişimi ölçülmüş ve sonuçlar grafikte gösterilmiştir. Canlılar, fitoplanktondan balıkçıl kuşuna doğru zincirdeki sıralarına göre verilmiştir.\nBuna göre,\nI. X maddesinin derişimi, zincirin ilk basamağındaki canlıda en yüksektir.\nII. X maddesi biyolojik birikime uğrarken, Y maddesi için grafikte böyle bir birikim görülmemektedir.\nIII. X maddesinin, canlı vücudundan atılamayan ya da çok yavaş atılan bir madde olması beklenir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Grafiğe göre doğru yargılar.',ip=['İki maddenin derişimlerini zincirin ilk ve son basamağında karşılaştır; basamak yükseldikçe ne olduğuna bak.'],bilgi=[BIR],
 puf='Basamak yükseldikçe derişimi artan madde biriken maddedir; en yüksek derişim zincirin en üst basamağındaki canlıdadır.')

# ===================== 08 · zor · enerji tablosu (çok adımlı)
card(8,'Enerji tablosunda eksik değer','Her basamakta aldığı enerji solunum, ayrıştırıcıya geçen ve üst basamağa geçenin toplamına eşittir; üst basamağa geçen sonraki basamağın aldığıdır.','Üst basamağa geçeni toplamdan düşmemek; ayrıştırıcılara geçeni solunum sanmak; %10 kuralını tabloya zorla uygulamak.','zor','tablo',5,'cv-enerji','kJ tablosunda üç basamaklı enerji dengesi')
U0=80000-32000-40000; assert U0==8000
D1=U0-4000-800; assert D1==3200
X8=800-280-160; assert X8==360
assert 4000+800+D1==8000 and 360+280+160==800
q8=[[ 'Üretici','80000','32000','40000','—'],['Birincil tüketici','—','4000','—','800'],['İkincil tüketici','—','X','280','160']]
SK=tablo_svg(['Basamak','Aldığı','Solunum','Ayrıştırıcı','Üst basamak'],q8)
q('0008',tipId='cv-enerji',tip=TIPLER['cv-enerji'],z='zor',alt='Enerji Akışı',kaz='Besin zincirinde enerji dengesini kullanarak tablodaki bilinmeyen enerji değerini hesaplar.',kalip='tablo',
 metin='Bir ekosistemde üretici, birincil tüketici ve ikincil tüketici basamaklarının bir yıl boyunca aldığı enerjinin nerelerde kullanıldığı tabloda kJ cinsinden verilmiştir. Bir basamağın aldığı enerji; solunumda harcanan, ayrıştırıcılara geçen ve bir üst basamağa aktarılan enerjilerin toplamına eşittir. Birincil tüketicinin aldığı enerji, üreticiden ona aktarılan enerjidir; ikincil tüketici için de aynı durum geçerlidir. Tabloda “—” ile gösterilen değerler verilmemiştir.\nBuna göre, tablodaki X değeri kaç kJ’dür?',
 sekil=SK,dogru=360,yan=[(80,'İkincil tüketicinin aldığı 800 kJ’nin %10’u olan 80 kJ alınmış; tabloda üst basamağa geçen 160 kJ olarak verilmiştir ve %10 kuralı zorla uygulanmamalıdır.','bilgi'),
  (280,'Ayrıştırıcılara geçen enerji (280 kJ), solunumda harcanan enerji sanılmış.','dikkat'),(520,'800 − 280 işlemi yapılmış; üst basamağa geçen 160 kJ da düşülmelidir.','islem'),
  (640,'800 − 160 işlemi yapılmış; ayrıştırıcılara geçen 280 kJ da düşülmelidir.','islem')],
 istenen='İkincil tüketicinin solunumda harcadığı enerji X (kJ).',ip=['Önce birincil tüketicinin aldığı enerjiyi üreticinin satırından bul; sonra ikincil tüketicinin aldığını ve enerji dengesini yaz.'],bilgi=[ENJ],
 ad=[A('Birincil tüketicinin aldığını bul','Üreticinin aldığından solunum ve ayrıştırıcıya geçen çıkarılınca kalan, üst basamağa geçendir.','80000 − 32000 − 40000 = 8000 kJ'),
     A('İkincil tüketicinin aldığını bul','Birincil tüketicinin üst basamağa geçirdiği enerji, ikincil tüketicinin aldığıdır.','Aldığı = 800 kJ'),
     A('Enerji dengesini kur','İkincil tüketicinin aldığı enerji üç kalemin toplamıdır.','800 = X + 280 + 160'),
     A('X’i hesapla','Bilinen iki kalem çıkarılır.','X = 800 − 280 − 160 = 360 kJ')],
 puf='Tablo sorularında satır dengesi (aldığı = harcanan + ayrıştırıcı + aktarılan) ile “bir basamağın aktardığı = sonrakinin aldığı” bağını birlikte kullan.')

# ===================== 09 · orta · CFC–ozon grafiği (öncüllü)
card(9,'CFC ve ozon eğrilerini birlikte okuma','Ozonun yeniden artışı CFC azalışından sonra gecikmeli başlar; ozon incelmesi UV ışınlarını artırır.','CFC azalmaya başlayınca ozonun hemen arttığını sanmak.','orta','grafik',4,'cv-sorun','CFC ve ozon göreli eğrileri')
CF=lambda t:100*math.exp(-(((t-30)/(14 if t<30 else 24))**2))
S9=lambda t:1/(1+math.exp(-(t-22)/6)); S92=lambda t:1/(1+math.exp(-(t-52)/5))
OZ=lambda t:100-30*S9(t)+22*S92(t)
g9=[i/2 for i in range(0,121)]
tmax=max(g9,key=CF); tmin=min(g9,key=OZ); assert tmax==30 and tmin-tmax>=7 and OZ(60)<95 and OZ(0)>97 and CF(0)<2 and CF(60)>15
assert all(OZ(a)>OZ(b) for a,b in zip(g9,g9[1:]) if b<=tmin) and OZ(60)>OZ(tmin)
c9=lambda f:' '.join(f'({t:.1f},{f(t):.2f})' for t in g9[::4])
b=['\\begin{axis}[width=8.4cm,height=5.6cm,xmin=0,xmax=60,ymin=0,ymax=110,xtick={0,10,20,30,40,50,60},ytick={0,50,100},axis lines=left,xlabel={Zaman (yıl)},ylabel={Göreli değer (\\%)},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
   f'\\addplot[black,smooth] coordinates {{{c9(CF)}}};',f'\\addplot[vurgu,smooth] coordinates {{{c9(OZ)}}};',
   '\\node[font=\\small,anchor=west] at (axis cs:2,55) {CFC derişimi};\\node[font=\\small,anchor=south,vurgu] at (axis cs:52,86) {Ozon miktarı};','\\end{axis}']
SK=pg('\n'.join(b))
qo('0009',[False,True,True],['ozon miktarı, CFC derişimi azalmaya başladıktan sonra da bir süre daha azalmış; ozonun yeniden artışı gecikmeli başlamıştır',
  'ozon incelmesi, DNA’ya zarar verebilen mor ötesi (UV) ışınların yeryüzüne ulaşmasını kolaylaştırır ve mutasyon ile cilt kanseri riskini artırır',
  'CFC derişimi azaldıktan sonra da ozon uzun süre düşük kalmıştır; ozonun eski düzeyine dönmesi hızlı değildir'],4,
 tipId='cv-sorun',tip=TIPLER['cv-sorun'],z='orta',alt='Çevre Sorunları',kaz='Ozon tabakasının incelmesi ile CFC derişimi arasındaki ilişkiyi grafikten yorumlar ve sonuçlarını açıklar.',kalip='grafik',
 metin='Atmosferdeki CFC derişimi ile stratosferdeki ozon miktarının uzun yıllar boyunca değişimi, her birinin kendi en yüksek değerine göre yüzde olarak grafikte gösterilmiştir. Bu süre içinde CFC kullanımı sınırlandırılmıştır.\nBuna göre,\nI. CFC derişimi azalmaya başladığı anda ozon miktarı da artmaya başlamıştır.\nII. Ozon tabakasındaki incelme, yeryüzüne ulaşan mor ötesi ışınların artmasına yol açar.\nIII. CFC kullanımının sınırlandırılması, ozon miktarını kısa sürede eski düzeyine döndürmemiştir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Grafiğe ve ozon incelmesinin sonuçlarına göre doğru yargılar.',ip=['CFC eğrisinin en yüksek olduğu zamanı ve ozon eğrisinin en düşük olduğu zamanı karşılaştır; ozonun düşük kalma süresine bak.'],bilgi=[OZO],
 puf='İki eğri aynı anda dönmez: ozon, CFC azalışından sonra bir süre daha düşer ve geç toparlanır.')

# ===================== 10 · orta · tür çeşitliliği sütun grafiği
card(10,'Tür sayısı ve dağılım','Tür çeşitliliği hem tür sayısına hem de bireylerin türlere dengeli dağılımına bağlıdır; toplam birey sayısı çeşitliliği belirlemez.','Yalnız tür sayısına bakmak; baskın tür çok olan alanı çeşitli sanmak.','orta','grafik',4,'cv-bioc','üç alanda tür dağılımı')
DAG={'X':[25,25,25,25],'Y':[85,5,5,5],'Z':[50,50,0,0]}
sh=lambda v:-sum(x/100*math.log(x/100) for x in v if x)
rich={k:sum(1 for x in v if x) for k,v in DAG.items()}; assert all(sum(v)==100 for v in DAG.values()) and rich=={'X':4,'Y':4,'Z':2} and sh(DAG['X'])>sh(DAG['Y']) and sh(DAG['X'])>sh(DAG['Z'])
SER10=[(t,f,[DAG[a][i] for a in 'XYZ']) for i,(t,f) in enumerate([('K','gray!20'),('L','gray!45'),('M','gray!70'),('N','vurgu!70')])]
SK=barplot(['Alan X','Alan Y','Alan Z'],SER10,112,'Birey sayısı','0,25,50,75,100',width=10.2,bw=11)
D10='Y alanındaki tür sayısı X alanıyla aynıdır; ancak bireyler türlere dengesiz dağıldığı için Y alanının tür çeşitliliği daha düşüktür.'
Y10=['X ve Y alanlarında tür sayısı farklı olduğundan, bu alanların tür çeşitlilikleri de farklıdır.','Z alanı, en çok türü barındırdığı için en yüksek tür çeşitliliğine sahiptir.',
     'Üç alanda da toplam birey sayısı aynı olduğundan, tür çeşitlilikleri de aynıdır.','Y alanında tek bir türün birey sayısı çok fazla olduğundan, Y alanı en yüksek tür çeşitliliğine sahiptir.']
q('0010',tipId='cv-bioc',tip=TIPLER['cv-bioc'],z='orta',alt='Biyoçeşitlilik',kaz='Tür sayısı ve bireylerin türlere dağılımını birlikte değerlendirerek tür çeşitliliğini karşılaştırır.',kalip='grafik',
 metin='Aynı iklim kuşağında bulunan, büyüklükleri eşit üç alanda (X, Y, Z) K, L, M ve N türlerine ait bireyler sayılmıştır. Her alanda toplam 100 birey sayılmış ve sonuçlar grafikte gösterilmiştir. Bir alanın tür çeşitliliği, yalnız tür sayısına değil bireylerin türlere ne kadar dengeli dağıldığına da bağlıdır.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 sekil=SK,dogru=D10,sira=yer('B',D10,Y10),
 yan=[(Y10[0],'X ve Y alanlarının her ikisinde de dört tür vardır; tür sayısı eşittir. Çeşitlilik farkı dağılımdan gelir.','dikkat'),(Y10[1],'Z alanında yalnız iki tür vardır; en çok türü barındıran alan X ve Y’dir.','dikkat'),
      (Y10[2],'Toplam birey sayısı eşit olsa da bireylerin türlere dağılımı alanlarda farklıdır; çeşitlilik eşit değildir.','bilgi'),(Y10[3],'Bir türün baskın olması çeşitliliği azaltır; en yüksek çeşitlik bireylerin eşit dağıldığı X alanındadır.','bilgi')],
 istenen='Grafiğe göre doğru ifade.',ip=['Her alanda kaç türün bulunduğunu ve bireylerin türlere eşit dağılıp dağılmadığını ayrı ayrı belirle.'],bilgi=[CES],
 ad=[A('Tür sayılarını bul','Sıfırdan farklı sütunlar tür sayısını verir.','X: 4 tür · Y: 4 tür · Z: 2 tür'),
     A('Dağılımı değerlendir','X’te bireyler eşit dağılmıştır; Y’de tek tür baskındır; Z’de iki tür eşit dağılmıştır.','X dengeli, Y dengesiz'),
     A('Çeşitliliği karşılaştır','Tür sayısı eşit olan X ve Y’den dağılımı dengeli olan daha çeşitlidir.','Y’nin çeşitliliği X’ten düşük')],
 puf='Tür çeşitliliğini karşılaştırırken önce tür sayısına, sonra bireylerin türlere dağılımının dengesine bak; toplam birey sayısı belirleyici değildir.')

# ===================== 11 · zor · göl kesiti diyagramı (öncüllü)
card(11,'Besin zenginleşmesinin sonuçları','Alg örtüsü ışığı keser, ölü maddenin ayrışması oksijen harcar; dipte oksijen azalınca oksijene bağımlı canlılar zarar görür.','Ayrışmanın oksijen harcamadığını sanmak; yalnız yüzeyde sorun olduğunu düşünmek.','zor','şekilli',5,'cv-sorun','göl kesitinde üç bölge ve gübre akışı')
b=[]
b.append('\\draw[thick,fill=black!25] (-.4,3.6)--(1.7,3.35)--(1.7,3.1)--(-.4,3.1)--cycle;')
b.append('\\node[font=\\footnotesize] at (.6,4.05) {Tarla};')
lake='(1.7,3.35) .. controls (1.9,-1.6) and (7.9,-1.6) .. (8.1,3.35)'
b.append('\\begin{scope}\\clip '+lake+' -- cycle;')
b.append('\\fill[vurgu!45] (1,2.75) rectangle (9,3.4);\\fill[black!8] (1,.7) rectangle (9,2.75);\\fill[black!30] (1,-1) rectangle (9,.7);\\end{scope}')
b.append('\\draw[thick] '+lake+';\\draw[thick] (1.7,3.35)--(8.1,3.35);')
b.append(f'\\draw[{OKS},line width=1pt] (.9,3.45)--(2.3,3.25);')
for x in (3.9,5,6.1): b.append(f'\\draw[{OKS},line width=.8pt] ({x},2.65)--({x},1.0);')
b+= [rakam(7.3,3.07,'1'),rakam(7.0,1.7,'2'),rakam(5,-.1,'3')]
SK=tk('\n'.join(b),.95)
qo('0011',[True,False,True],['yüzeydeki yoğun alg örtüsü ışığı tutar; derindeki su bitkileri yeterli ışık alamaz ve fotosentezleri azalır',
  'ölü organik maddeyi ayrıştıran oksijenli solunum yapan canlılar oksijen harcar; dip suyunun oksijeni azalır',
  'dipte oksijen azalınca oksijene gereksinimi olan canlılar zarar görür; oksijensiz solunum yapan bakteriler çoğalabilir'],2,
 tipId='cv-sorun',tip=TIPLER['cv-sorun'],z='zor',alt='Çevre Sorunları',kaz='Besin tuzu zenginleşmesinin ışık ve oksijen koşullarını nasıl değiştirdiğini ve sucul canlılara etkisini açıklar.',kalip='şekilli',
 metin='Şekilde, çevresindeki tarım alanından gübreli su akan bir göl kesiti verilmiştir. Yüzeye yakın bölge 1, orta derinlik 2 ve dip 3 ile gösterilmiştir. Gübrelerle taşınan azot ve fosfor nedeniyle 1. bölgede algler çok çoğalmış, ölen algler dibe çökmüştür.\nBuna göre,\nI. 1. bölgedeki yoğun alg örtüsü, derindeki su bitkilerinin fotosentezini azaltır.\nII. 3. bölgede ölü algleri ayrıştıran canlılar oksijen harcamadığından dip suyunun oksijeni artar.\nIII. 3. bölgede oksijen derişiminin azalması, oksijene gereksinimi olan canlıların ölümüne yol açabilir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Göldeki değişimlerle ilgili doğru yargılar.',ip=['Yüzeydeki alg tabakasının ışığa, dipteki ayrışmanın ise oksijene etkisini ayrı ayrı düşün.'],bilgi=[OTR],
 puf='Besin tuzu artışı önce yüzeyde alg patlaması, sonra dipte ayrışma ve oksijen azalması getirir; sorun iki aşamalıdır.')

# ===================== 12 · orta · su döngüsü, orman kesimi (olumsuz)
card(12,'Ormansızlaşmanın su ve karbon dengesine etkisi','Bitki örtüsü yok olunca terleme, sızma ve karbon bağlama azalır; yüzey akışı ve erozyon artar.','Ağaç kesilince fotosentezle bağlanan karbonun arttığını sanmak.','orta','düz',4,'cv-su','ormansızlaşma ve su döngüsü')
D12='Bölgede fotosentezle bağlanan karbondioksit miktarı artar; bu nedenle atmosferden karbondioksit çekilmesi hızlanır.'
Y12=['Yüzey akışı artar ve verimli üst toprak katmanı erozyonla taşınır.','Toprağa sızan su miktarı azalır; yer altı suyunun beslenmesi zayıflar.',
     'Bitkilerin terlemesiyle atmosfere verilen su buharı miktarı azalır.','Toprak yüzeyi doğrudan güneş ışığı aldığından sıcaklık dalgalanmaları artar.']
q('0012',tipId='cv-su',tip=TIPLER['cv-su'],z='orta',alt='Madde Döngüleri',kaz='Bitki örtüsünün yok edilmesinin su ve karbon döngüsüne etkilerini açıklar.',kalip='düz',
 metin='Yıllık yağışın fazla olduğu eğimli bir bölgede, ormanla kaplı bir yamacın bütün ağaçları kesilmiş ve alan bitki örtüsü olmadan bırakılmıştır. Yamaçtaki bitki örtüsünün yok olması, suyun doğadaki dolaşımını ve bölgedeki çevresel koşulları değiştirmiştir.\nBuna göre, bu değişimle ilgili aşağıdakilerden hangisi söylenemez?',
 sekil=None,dogru=D12,sira=yer('E',D12,Y12),
 yan=[(Y12[0],'Bitki kökleri toprağı tutmaz olunca yüzeyden akan su artar ve erozyon hızlanır. Bu ifade söylenebilir.','dikkat'),(Y12[1],'Kök ve yaprak örtüsü kalkınca suyun toprağa sızması azalır. Bu ifade söylenebilir.','dikkat'),
      (Y12[2],'Ağaçlar yok olunca terlemeyle atmosfere geçen su azalır. Bu ifade söylenebilir.','dikkat'),(Y12[3],'Gölgeleyen bitki örtüsü kalkınca toprak yüzeyi doğrudan ısınır. Bu ifade söylenebilir.','dikkat')],
 istenen='Orman kesiminin etkileriyle ilgili söylenemeyen ifade.',ip=['Ağaçların su ve karbon döngüsündeki görevlerini (terleme, kök tutunması, fotosentez) düşün ve kesilince hangilerinin azaldığına bak.'],bilgi=[SUD,KAR],
 ad=[A('Ağaçların görevlerini listele','Bitki örtüsü toprağı tutar, suyu sızdırır, terler ve fotosentezle karbon bağlar.','Tutma, sızma, terleme, karbon bağlama'),
     A('Kesimin sonucunu yaz','Bu görevlerin hepsi azalır; yüzey akışı ve erozyon artar.','Sızma ↓, terleme ↓, karbon bağlama ↓, akış ↑'),
     A('Uyumsuz ifadeyi bul','Fotosentez yapan ağaçlar kesilince karbon bağlama artmaz, azalır.','Karbon bağlanmasının artması söylenemez')],
 puf='Ormansızlaşmada bağlanan karbon, terleme ve sızma azalırken yüzey akışı ve erozyon artar; yönleri tersine karıştırma.')

# ===================== 13 · orta · istilacı tür (olumsuz)
card(13,'İstilacı türün biyoçeşitliliğe etkisi','İstilacı türün artışı yerli türleri azaltabilir; toplam birey sayısı artsa bile tür çeşitliliği düşebilir.','Toplam birey artınca çeşitliliğin de arttığını sanmak.','orta','grafik',4,'cv-bioc','istilacı tür girişi öncesi ve sonrası sütun grafiği')
GZ={'Başlangıç':[400,300,250,0],'10. yıl':[300,150,100,450],'20. yıl':[150,0,0,900]}
tot={k:sum(v) for k,v in GZ.items()}; assert tot=={'Başlangıç':950,'10. yıl':1000,'20. yıl':1050}
rich13={k:sum(1 for x in v if x) for k,v in GZ.items()}; assert rich13=={'Başlangıç':3,'10. yıl':4,'20. yıl':2}
assert any(GZ['10. yıl'][i]<GZ['Başlangıç'][i] for i in range(3)) and GZ['20. yıl'][0]<GZ['Başlangıç'][0]/2
SER13=[(t,f,[GZ[a][i] for a in GZ]) for i,(t,f) in enumerate([('K','gray!20'),('L','gray!45'),('M','gray!70'),('İ','vurgu!70')])]
SK=barplot(['Başlangıç','10. yıl','20. yıl'],SER13,1100,'Birey sayısı','0,300,600,900',width=10.2,bw=11)
D13='10. yılda yerli türlerin hiçbirinin birey sayısı azalmamıştır.'
Y13=['20. yılda gölde yaşayan toplam birey sayısı başlangıçtakinden fazla olduğu hâlde tür sayısı azalmıştır.','İstilacı türün birey sayısındaki artış, yerli türlerin birey sayısındaki azalışla aynı dönemde gerçekleşmiştir.',
     'İstilacı türün yerli türlerle aynı kaynakları kullanması, bu sonucun nedenlerinden biri olabilir.','20. yılda K türünün birey sayısı, başlangıçtaki değerin yarısından azdır.']
q('0013',tipId='cv-bioc',tip=TIPLER['cv-bioc'],z='orta',alt='Biyoçeşitlilik',kaz='İstilacı bir türün yerli türlere ve tür çeşitliliğine etkisini verilerden yorumlar.',kalip='grafik',
 metin='Bir göle dışarıdan istilacı bir balık türü (İ) bırakılmış; gölde yaşayan yerli K, L ve M türlerinin ve istilacı türün birey sayıları başlangıçta, 10. yılda ve 20. yılda sayılarak grafikte gösterilmiştir. Başlangıçta göle istilacı tür girmemiş, başka bir değişiklik de olmamıştır.\nBuna göre, grafikle ilgili aşağıdakilerden hangisi söylenemez?',
 sekil=SK,dogru=D13,sira=yer('A',D13,Y13),
 yan=[(Y13[0],'Toplam birey sayısı 950’den 1050’ye çıkmış, tür sayısı 3’ten 2’ye düşmüştür. Bu ifade doğrudur.','dikkat'),(Y13[1],'İ artarken K, L ve M azalmaktadır; iki değişim aynı dönemdedir. Bu ifade doğrudur.','dikkat'),
      (Y13[2],'Aynı yaşam alanı ve besin için rekabet, yerli türleri azaltan nedenlerden biri olabilir. Bu ifade söylenebilir.','dikkat'),(Y13[3],'K türü 400’den 150’ye düşmüştür; 150, 400’ün yarısı olan 200’den azdır. Bu ifade doğrudur.','dikkat')],
 istenen='Grafikle ilgili söylenemeyen ifade.',ip=['Yerli türlerin her birinin 10. yıldaki sayısını başlangıçtakiyle ayrı ayrı karşılaştır.'],bilgi=[TEH],
 ad=[A('Sütunları oku','Her tür için üç zamandaki birey sayıları karşılaştırılır.','K: 400→300→150 · L: 300→150→0 · M: 250→100→0 · İ: 0→450→900'),
     A('Genel eğilimi belirle','İstilacı tür artarken yerli türler azalmış, tür sayısı düşmüştür.','Tür sayısı 3 → 4 → 2'),
     A('Söylenemeyeni bul','Başlangıç ile 10. yıl karşılaştırılınca K, L ve M’nin üçünde de azalma görülür.','Hiçbirinin azalmaması söylenemez')],
 puf='“Hiçbiri” ya da “her zaman” gibi kesin ifadeleri tek bir karşı örnekle sına; grafikte bir tür bile azalmışsa ifade yanlıştır.')

# ===================== 14 · zor · ters biyokütle piramidi tablosu
card(14,'Biyokütle ve yıllık üretim farkı','Hızlı yenilenen üreticilerin biyokütlesi az olsa da yıllık üretimi çoktur; biyokütle piramidi ters olabilir, enerji (üretim) piramidi düz kalır.','Biyokütlesi az olan basamağın enerjisinin de az olduğunu sanmak; ters biyokütle piramidinin enerji kuralını bozduğunu sanmak.','zor','tablo',5,'cv-enerji','açık denizde biyokütle ve yıllık üretim tablosu')
BM={'Fitoplankton':(4,600),'Zooplankton':(20,100),'Balıklar':(8,15)}
tn={k:v[1]/v[0] for k,v in BM.items()}; assert BM['Fitoplankton'][0]<BM['Zooplankton'][0] and BM['Fitoplankton'][1]>BM['Zooplankton'][1]>BM['Balıklar'][1]
assert tn['Fitoplankton']==150 and tn['Zooplankton']==5 and tn['Fitoplankton']>tn['Zooplankton']
SK=tablo_svg(['Canlı grubu','Biyokütle (g/m²)','Yıllık üretim (g/m²)'],[[k,str(v[0]),str(v[1])] for k,v in BM.items()])
D14='Fitoplanktonun biyokütlesi zooplanktonunkinden az olsa da yıllık üretiminin biyokütlesine oranı çok daha büyüktür; bu nedenle biyokütle piramidi ters olsa da yıllık üretim (enerji) piramidi düzdür.'
Y14=['Biyokütle piramidi her ekosistemde düzdür; bu nedenle tabloda yanlış değer verilmiştir.','Zooplanktonun yıllık üretimi fitoplanktonunkinden fazladır; çünkü biyokütlesi daha büyüktür.',
     'Fitoplanktonun biyokütlesi az olduğundan, bu basamak ekosisteme en az enerjiyi sağlayan basamaktır.','Balıkların yıllık üretiminin zooplanktonunkinden fazla olması, enerji piramidinin ters olmasına yol açmıştır.']
q('0014',tipId='cv-enerji',tip=TIPLER['cv-enerji'],z='zor',alt='Besin Piramitleri',kaz='Biyokütle ile yıllık üretimi ayırt ederek ters biyokütle piramidi ile düz enerji piramidini birlikte yorumlar.',kalip='tablo',
 metin='Açık denizde yaşayan, besin zincirini oluşturan üç canlı grubunun bir andaki toplam biyokütlesi ile bir yıl içinde ürettikleri organik madde miktarı, deniz yüzeyinin birim alanı için tabloda verilmiştir. Üretim değerleri, her basamağın zincire sağladığı enerjiyle orantılı kabul edilecektir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 sekil=SK,dogru=D14,sira=yer('D',D14,Y14),
 yan=[(Y14[0],'Tabloda fitoplanktonun biyokütlesi (4) zooplanktonunkinden (20) azdır; bu, bazı ekosistemlerde biyokütle piramidinin ters olabileceğini gösterir, değerler yanlış değildir.','bilgi'),
      (Y14[1],'Zooplanktonun yıllık üretimi 100, fitoplanktonunki 600 g/m²’dir; biyokütle büyük olsa da üretim küçüktür.','dikkat'),
      (Y14[2],'Fitoplanktonun yıllık üretimi (600) en yüksektir; bu basamak zincire en çok enerji sağlayandır.','bilgi'),
      (Y14[3],'Balıkların yıllık üretimi (15), zooplanktonunkinden (100) azdır; enerji piramidi düzdür.','dikkat')],
 istenen='Tabloya göre doğru ifade.',ip=['Biyokütle sütununu ve yıllık üretim sütununu ayrı ayrı sıralayıp iki sıralamanın uyuşup uyuşmadığını karşılaştır.'],bilgi=[PIR],
 ad=[A('Biyokütle sıralamasını yaz','Biyokütle sütununa göre en büyük zooplanktondur.','Zooplankton 20 > Balıklar 8 > Fitoplankton 4'),
     A('Üretim sıralamasını yaz','Yıllık üretim üreticiden üst basamağa doğru azalır.','Fitoplankton 600 > Zooplankton 100 > Balıklar 15'),
     A('Yenilenme hızını hesapla','Yıllık üretimin biyokütleye oranı, basamağın yılda kaç kez yenilendiğini gösterir.','Fitoplankton: 600 ÷ 4 = 150 · Zooplankton: 100 ÷ 20 = 5'),
     A('Sonucu yaz','Üretim piramidi düz, biyokütle piramidi ters olabilir.','Biyokütle ters, enerji düz')],
 puf='Biyokütle “bir anda var olan”, üretim “bir yılda oluşan” demektir; hızlı yenilenen basamak az biyokütleyle çok enerji sağlayabilir.')

# ===================== 15 · zor · besin zinciri, birikim katsayısı
card(15,'Birikim katsayısıyla derişim tahmini','Her basamakta derişim aynı katsayıyla artıyorsa iki basamak arasındaki oran katsayının karesidir; son basamak ilk derişim × katsayı üzeri basamak sayısıdır.','İki basamağın oranını tek basamağın katsayısı sanmak; basamak sayısını yanlış saymak.','zor','şekilli',4,'cv-birikim','besin zincirinde ilk ve üçüncü basamak derişimi verilir')
c0,c2=2,18; f=int(math.isqrt(c2//c0)); assert f*f==c2//c0==9 and f==3
C15=[c0*f**i for i in range(5)]; assert C15==[2,6,18,54,162] and C15[2]==c2
assert c2*f**2==162 and c2*f==54 and c2*(c2//c0)==162 and c2*(c2//c0)**1==162
assert c0*9**4==13122 and c2*(c2//c0)**2==1458 and c2*18==324 and c2*f**3==486
b=[kutu(0,0,'Fitoplankton\\\\2 µg/kg'),kutu(3.5,0,'Zooplankton\\\\?'),kutu(7,0,'Küçük balık\\\\18 µg/kg'),kutu(7,-2.3,'Büyük balık\\\\?'),kutu(3.5,-2.3,'Balıkçıl\\\\X')]
b+=[f'\\draw[{OKS},line width=.9pt] (1.2,0)--(2.3,0);',f'\\draw[{OKS},line width=.9pt] (4.7,0)--(5.8,0);',f'\\draw[{OKS},line width=.9pt] (7,-.6)--(7,-1.7);',f'\\draw[{OKS},line width=.9pt] (5.8,-2.3)--(4.7,-2.3);']
SK=tk('\n'.join(b),1.0)
q('0015',tipId='cv-birikim',tip=TIPLER['cv-birikim'],z='zor',alt='Biyolojik Birikim',kaz='Besin zincirinde basamak başına sabit katsayıyla artan derişimden üst basamaktaki derişimi hesaplar.',kalip='şekilli',
 metin='Şekilde, bir göldeki besin zincirinde yer alan canlılar ve bazılarının dokularında ölçülen, doğada kolay ayrışmayan bir zehirli maddenin derişimi gösterilmiştir. Oklar yenen canlıdan yiyen canlıya doğrudur. Zincirdeki her basamakta bu maddenin derişimi, bir önceki basamaktaki derişimin aynı katı kadar artmaktadır; şekilde “?” ile gösterilen değerler ölçülmemiştir.\nBuna göre, balıkçıl kuşunun dokularındaki bu maddenin derişimi olan X kaç µg/kg’dır?',
 sekil=SK,dogru=162,yan=[(54,'Büyük balığın derişimi bulunmuş; balıkçıl bir basamak daha yukarıdadır.','dikkat'),(324,'Küçük balıktaki derişim 18’in kendisiyle çarpılmış; katsayı 3 yerine 18 alınmıştır.','islem'),
  (486,'Küçük balıktan balıkçıla iki değil üç basamak çıkılmış gibi hesaplanmıştır.','islem'),(1458,'İlk iki basamak arasındaki toplam oran (9) her basamağın katsayısı sanılmış; 18, iki basamak için 9 ile iki kez çarpılmıştır.','bilgi')],
 istenen='Balıkçıl kuşundaki derişim X (µg/kg).',ip=['Fitoplankton ile küçük balık arasında kaç basamak olduğunu say; iki basamak için toplam oranı bulup basamak başına katsayıya çevir.'],bilgi=[BIR,BIK],
 ad=[A('Basamak sayısını bul','Fitoplanktondan küçük balığa iki basamak çıkılmıştır.','Fitoplankton → zooplankton → küçük balık: 2 basamak'),
     A('Toplam oranı hesapla','Küçük balıktaki derişim, fitoplanktondakinin kaç katıdır?','18 ÷ 2 = 9'),
     A('Basamak başına katsayıyı bul','İki basamak için oran 9 ise her basamakta 3 katına çıkılmıştır.','3 × 3 = 9 → katsayı 3'),
     A('X’i hesapla','Küçük balıktan balıkçıla iki basamak daha vardır.','18 × 3 × 3 = 162 µg/kg')],
 puf='Basamak başına katsayı, iki basamak arasındaki oranın kökü kadardır; basamak sayısını okla saymadan önce kutuları say.')

# ===================== 16 · orta · sera etkisi (olumsuz)
card(16,'Sera gazı artışında ışın akışları','Sera gazları arttıkça yeryüzüne geri gönderilen ısı artar, uzaya çıkan azalır.','Uzaya çıkan ışınların arttığını sanmak; geri gönderilen ışınların azaldığını sanmak.','orta','şekilli',4,'cv-sorun','sera etkisi şemasında numaralı oklar')
b=['\\draw[thick,fill=black!25] (0,0) rectangle (8,.45);\\node[font=\\small] at (6.95,-.3) {Yeryüzü};',
   '\\draw[thick,fill=vurgu!14] (0,2.5) rectangle (8,3.6);\\node[font=\\small,anchor=east] at (7.9,3.05) {Atmosfer};',
   '\\node[font=\\small] at (6.95,5.9) {Uzay};\\draw[thick,fill=black!6] (.9,5.3) circle (.62);\\node[font=\\footnotesize] at (.9,5.3) {Güneş};',
   f'\\draw[{OKS},line width=1.4pt] (1.6,4.75)--(2.4,.55);',
   f'\\draw[{OKS},line width=1.4pt] (3.5,.55)--(3.5,2.5);',
   f'\\draw[{OKS},line width=1.4pt] (4.5,2.5)--(4.5,.55);',
   f'\\draw[{OKS},line width=1.4pt] (5.5,3.6)--(5.5,5.55);']
b+=[rakam(1.2,4.2,'1'),rakam(3.1,1.5,'2'),rakam(4.9,1.5,'3'),rakam(5.9,4.4,'4')]
SK=tk('\n'.join(b),1.0)
D16='3 numaralı ışınların miktarı azalır, 4 numaralı ışınların miktarı artar.'
Y16=['1 numaralı ışınların kaynağı Güneş olduğundan, bu ışınların miktarı sera gazı derişimi artışından doğrudan etkilenmez.','2 numaralı ışınların miktarı, yeryüzünün ısınmasıyla artabilir.',
     '3 numaralı ışınların miktarı artar ve yeryüzünün ortalama sıcaklığı yükselir.','4 numaralı ışınların miktarı azalır; çünkü yeryüzünden yayılan ısının daha büyük bölümü atmosferde tutulur.']
q('0016',tipId='cv-sorun',tip=TIPLER['cv-sorun'],z='orta',alt='Çevre Sorunları',kaz='Sera etkisinin şemasını yorumlayıp sera gazı derişimi arttığında ısı ışınlarının yön ve miktarlarının nasıl değiştiğini açıklar.',kalip='şekilli',
 metin='Şekilde sera etkisi şematik olarak gösterilmiştir. 1 numaralı ok Güneş’ten gelen ışınları, 2 numaralı ok yeryüzünden yayılan ısı ışınlarını, 3 numaralı ok sera gazlarınca tutulup yeryüzüne geri gönderilen ısı ışınlarını, 4 numaralı ok ise atmosferi geçip uzaya çıkan ısı ışınlarını göstermektedir.\nAtmosferdeki sera gazı derişimi arttığında bu ışınlarla ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK,dogru=D16,sira=yer('C',D16,Y16),
 yan=[(Y16[0],'Güneş’ten gelen ışınların miktarını sera gazları değil Güneş belirler. Bu ifade doğrudur.','dikkat'),(Y16[1],'Yeryüzü ısındıkça yaydığı ısı ışınları artabilir. Bu ifade doğrudur.','dikkat'),
      (Y16[2],'Sera gazları arttıkça geri gönderilen ısı çoğalır ve yeryüzü ısınır. Bu ifade doğrudur.','dikkat'),(Y16[3],'Tutulan ısı arttığından atmosferden uzaya çıkan ısı azalır. Bu ifade doğrudur.','dikkat')],
 istenen='Sera gazı derişimi arttığında yanlış olan ifade.',ip=['Sera gazlarının ısı ışınlarını tutup hangi yöne gönderdiğini düşün; tutulan ısı artarsa uzaya çıkan ısının ne olacağına bak.'],bilgi=[SER],
 ad=[A('Okların anlamını yaz','Numaralı oklar sırasıyla gelen, yayılan, geri gönderilen ve uzaya çıkan ışınlardır.','1 gelen · 2 yayılan · 3 geri gönderilen · 4 uzaya çıkan'),
     A('Derişim artışını uygula','Daha fazla sera gazı, ısı ışınlarının daha büyük bölümünü tutar.','3 artar, 4 azalır'),
     A('Yanlış ifadeyi bul','Ters yönde verilen değişim yanlıştır.','3 azalır, 4 artar ifadesi yanlış')],
 puf='Sera gazı artınca atmosferde tutulan ve yeryüzüne geri dönen ısı artar; uzaya kaçan ısı azalır.')

# ===================== 17 · zor · brüt üretim hesabı
card(17,'Net üretimden brüt üretime','Etçildeki enerjiden basamak basamak geri gidilip net üretim bulunur; brüt üretim, solunumda harcanan yüzde çıkarılmış kalanın tamamlanmasıyla bulunur.','Net üretimi brüt sanmak; solunum yüzdesini net üretime eklemek.','zor','düz',5,'cv-enerji','etçilden geriye brüt üretim hesabı')
et=90; ot=et*10; net=ot*10; brut=Fr(net)/Fr(60,100); assert (ot,net,brut)==(900,9000,15000)
assert net*Fr(6,10)==5400 and net*Fr(14,10)==12600 and brut*Fr(6,10)==net
q('0017',tipId='cv-enerji',tip=TIPLER['cv-enerji'],z='zor',alt='Enerji Akışı',kaz='Besin zincirinde basamaklar arası aktarım yüzdesi ve solunum kaybını kullanarak brüt üretimi hesaplar.',kalip='düz',
 metin='Bir tarla ekosisteminde üreticiler, fotosentezle bağladıkları enerjinin (brüt üretim) %40’ını kendi solunumlarında harcamakta, kalan enerji (net üretim) ise üreticilerde depolanmaktadır. Zincirde her basamakta depolanan enerjinin yaklaşık %10’u bir üst basamağa aktarılmaktadır. Zincir üretici → birincil tüketici → ikincil tüketici biçimindedir ve ikincil tüketicilere 90 kJ enerji ulaşmıştır.\nBuna göre, üreticilerin brüt üretimi kaç kJ’dür?',
 sekil=None,dogru=15000,yan=[(900,'Birincil tüketicilerde depolanan enerji (900 kJ) bulunmuş; üreticilere kadar geri gidilmemiştir.','dikkat'),(5400,'Net üretimin %60’ı alınmış; brüt üretim net üretimden büyüktür.','islem'),
  (9000,'Net üretim (9000 kJ) brüt üretim sanılmış; solunumda harcanan %40 eklenmemiştir.','dikkat'),(12600,'Net üretime %40 eklenmiş (9000 × 1,4); oysa net üretim brüt üretimin %60’ıdır.','islem')],
 istenen='Üreticilerin brüt üretimi (kJ).',ip=['İkincil tüketiciden başlayıp her basamakta %10 kuralını tersine uygulayarak üreticilerdeki enerjiye ulaş; sonra solunum kaybını hesaba kat.'],bilgi=[BNE],
 ad=[A('Birincil tüketiciyi bul','İkincil tüketiciye ulaşan enerji, birincil tüketicide depolananın %10’udur.','90 ÷ 0,1 = 900 kJ'),
     A('Net üretimi bul','Birincil tüketiciye ulaşan enerji, üreticilerde depolananın %10’udur.','900 ÷ 0,1 = 9000 kJ'),
     A('Net üretimin payını yaz','Net üretim, brüt üretimin solunum çıkarıldıktan sonra kalan kısmıdır.','Net = brüt × 0,60'),
     A('Brüt üretimi hesapla','Net üretim, brüt üretimin %60’ına eşittir.','Brüt = 9000 ÷ 0,6 = 15000 kJ')],
 puf='Brüt üretimden net üretime geçerken solunum payı çıkarılır; tersini yaparken net üretimi (1 − solunum oranı)’na bölmek gerekir.')

# ===================== 18 · orta · fosfor döngüsü (öncüllü)
card(18,'Fosfor döngüsünün özellikleri','Fosforun atmosferik evresi önemsizdir; bitkiler fosfatı topraktan alıp ATP ve nükleik asitlere katar; gübrenin bir kısmı sulara karışır.','Fosforun azot gibi atmosferden bağlandığını sanmak; gübrenin tamamının bitkilerce alındığını sanmak.','orta','öncüllü',3,'cv-azot','fosfor döngüsü, üç yargı')
qo('0018',[True,True,False],['fosfor döngüsünde azot ve karbon döngülerinden farklı olarak önemli bir atmosferik (gaz) evre bulunmaz; fosfor kayaç ve topraktan canlılara geçer',
  'bitkiler fosforu topraktan fosfat iyonu olarak alır ve ATP ile nükleik asit gibi moleküllerin yapısına katar',
  'gübredeki fosfatın bir bölümü bitkilerce alınmadan yüzey sularına karışabilir'],1,
 tipId='cv-azot',tip=TIPLER['cv-azot'],z='orta',alt='Madde Döngüleri',kaz='Fosfor döngüsünün diğer döngülerden farkını ve fosforun canlılardaki görevini açıklar.',kalip='öncüllü',
 metin='Fosfor, canlıların yapısında bulunan ve doğada çoğunlukla kayaçlarda ile toprakta fosfat bileşikleri hâlinde bulunan bir elementtir. Buna göre fosfor döngüsüyle ilgili,\nI. Azot ve karbon döngülerinden farklı olarak, önemli bir atmosferik (gaz) evresi bulunmaz.\nII. Bitkiler fosforu topraktan fosfat iyonu olarak alır ve ATP ile nükleik asit gibi moleküllerin yapısına katar.\nIII. Tarım alanlarına verilen fosfatlı gübrelerin tamamı bitkiler tarafından alınır, yüzey sularına karışması mümkün değildir.\nyargılarından hangileri doğrudur?',
 istenen='Fosfor döngüsüyle ilgili doğru yargılar.',ip=['Fosforun doğada hangi biçimlerde ve hangi ortamlarda bulunduğunu, canlıların onu hangi biçimde aldığını düşün.'],bilgi=[FOS],
 puf='Fosfor döngüsünde gaz evresi yoktur; fosfat kayaç, toprak, su ve canlılar arasında dolaşır, fazlası sulara karıştığında ötrofikasyona yol açabilir.')

# ===================== 19 · orta · biyoçeşitlilik düzeyleri (öncüllü)
card(19,'Genetik çeşitlilikteki azalma','Aynı türün alel ya da çeşit çeşitliliğinin azalması genetik çeşitlilik kaybıdır; ekosistem kaybı ayrı bir düzeydir.','Ekosistemin yok olmasını genetik çeşitlilik kaybı saymak.','orta','öncüllü',3,'cv-bioc','biyoçeşitlilik düzeylerine örnek durumlar')
qo('0019',[True,False,True],['popülasyondaki alel çeşitliliğinin azalması, genetik çeşitliliğin azalmasıdır',
  'bir yaşam ortamının yok olması, ekosistem çeşitliliğindeki azalmadır; genetik çeşitlilik aynı türün gen farklılığını anlatır',
  'tarımda yerel çeşitlerin kaybolması, aynı türün gen havuzundaki çeşitliliğin azalmasıdır'],3,
 tipId='cv-bioc',tip=TIPLER['cv-bioc'],z='orta',alt='Biyoçeşitlilik',kaz='Genetik, tür ve ekosistem çeşitliliği düzeylerini örneklerle ayırt eder.',kalip='öncüllü',
 metin='Biyoçeşitlilik; genetik, tür ve ekosistem çeşitliliği düzeylerinde incelenir. İnsan etkinliklerinin yol açtığı bazı değişiklikler bu düzeylere göre sınıflandırılacaktır. Buna göre,\nI. Birkaç bireye düşen nesli tehlikedeki bir türün popülasyonunda alel çeşitliliğinin azalması\nII. Bir sulak alanın kurutularak tarım alanına çevrilmesiyle bu alana özgü yaşam ortamının yok olması\nIII. Tarımda yalnız yüksek verimli tek bir çeşidin ekilmesiyle aynı bitki türünün yerel çeşitlerinin kaybolması\ndurumlarından hangileri genetik çeşitlilikteki azalmaya örnektir?',
 istenen='Genetik çeşitlilikteki azalmaya örnek olan durumlar.',ip=['Her durumda kaybedilen şeyin aynı türün genleri mi, farklı türler mi yoksa bir yaşam ortamı mı olduğuna bak.'],bilgi=[DUS],
 puf='Genetik çeşitlilik “aynı tür içindeki” farklılıktır; tür sayısı ya da yaşam ortamı kaybı farklı düzeylerdir.')

# ===================== 20 · orta · sürdürülebilir kullanım, stok
card(20,'Balık stoğunda yıllık değişim','Stok her yıl başındaki değer üzerinden artar ve avlanma sonrası kalan bir sonraki yılın başlangıcıdır; avlanma üremeyi aşarsa stok azalır.','Artışı sabit saymak; avlanma sonrası kalan yerine öncesi değeri almak.','orta','düz',4,'cv-koruma','balık stoğu üç yıllık değişim')
s=10000; ARR=[]
for _ in range(3):
    s=s+s*Fr(20,100)-2500; ARR.append(s)
assert ARR==[9500,8900,8180] and 10000+3*(2000-2500)==8500 and 10000==10000 and 8900*Fr(12,10)==10680
q('0020',tipId='cv-koruma',tip=TIPLER['cv-koruma'],z='orta',alt='Sürdürülebilirlik',kaz='Yenilenebilir bir kaynağın yıllık yenilenme ve kullanım miktarını karşılaştırarak stok değişimini hesaplar.',kalip='düz',
 metin='Bir kıyı bölgesinde ticari değeri olan bir balık türünün popülasyonu yılın başında 10000 bireydir. Doğal üreme sonucu her yıl, o yılın başındaki birey sayısının %20’si kadar yeni birey popülasyona katılmaktadır. Balıkçılar her yıl üreme dönemi bittikten sonra 2500 birey avlamaktadır. Göç ve diğer ölüm nedenleri yoktur ve bu uygulama aynı biçimde sürmektedir.\nBuna göre, 3. yılın sonunda avlanma yapıldıktan sonra popülasyonda kaç birey kalır?',
 sekil=None,dogru=8180,yan=[(8500,'Yıllık artış 2000 birey gibi sabit alınmış; oysa artış her yıl o yılın başındaki sayının %20’sidir ve sayı azaldıkça artış da azalır.','bilgi'),
  (9500,'Yalnız 1. yılın sonundaki sayı bulunmuş; 3 yıl sonrası istenmektedir.','dikkat'),(10000,'Avlanmanın üremeyle dengelendiği sanılmış; oysa üreme 2000, avlanma 2500 bireydir.','bilgi'),
  (10680,'3. yılın avlanmadan önceki sayısı bulunmuş; avlanma yapıldıktan sonra kalan sayı istenmektedir.','dikkat')],
 istenen='3. yılın sonunda avlanma sonrası birey sayısı.',ip=['Yılı yıla bağla: bir yılın sonunda avlanmadan sonra kalan sayı, sonraki yılın başlangıç sayısıdır.'],bilgi=[SUR],
 ad=[A('1. yılı hesapla','Yıl başındaki sayıya %20 eklenir, avlanma çıkarılır.','10000 + 2000 − 2500 = 9500'),
     A('2. yılı hesapla','Kalan sayı 2. yılın başlangıcıdır.','9500 + 1900 − 2500 = 8900'),
     A('3. yılı hesapla','Aynı işlem 3. yılda yinelenir.','8900 + 1780 − 2500 = 8180'),
     A('Sonucu yorumla','Avlanma yıllık artıştan fazla olduğundan stok her yıl azalır.','Kullanım yenilenmeyi aşıyor → sürdürülebilir değil')],
 puf='Yıllık artışı her yıl yeniden, o yılın başındaki sayı üzerinden hesapla; avlanma artıştan fazlaysa stok sürekli küçülür.')

# ===================== yaz
H.KONU='Canlılar ve Çevre'
for qq in P.ANA: qq['kardes']=None
P.konu_adi='Canlılar ve Çevre'
os.makedirs(os.path.join(GD),exist_ok=True)
P.yaz(os.path.join(GD,'cevre-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-cevre.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='abio|Canlılar ve Çevre'))['kartlar'].append(c['id'])
json.dump(dict(konu='Canlılar ve Çevre',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji (yalnız mantık), MEB 12. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abcevre.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
