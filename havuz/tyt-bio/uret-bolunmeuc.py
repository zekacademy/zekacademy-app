"""TYT Biyoloji · Hücrede Bölünme – Üreme · 3. paket (bolunmeuc): 10 soru, kardeş yok, ipucu 1.
Gamet genotipleri, kromozom sayımları, evre süreleri ve öncül doğrulukları Python'da hesaplanır/assert edilir; şekiller aynı değerlerden çizilir."""
import sys,os,math,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_bio as H
from _hafif_bio3 import *
KONU_='Hücrede Bölünme – Üreme'; UK='bio|'+KONU_; H.KONU=KONU_
P=Parti('bolunmeuc',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 10. sınıf Hücre Bölünmeleri ve Üreme'
TIP={'kromozom':('by-bl3-kromozom','Tür kromozom sayıları tablosu'),'krossing':('by-bl3-krossing','Krossing-over ve gamet genotipi'),'ayrilmama':('by-bl3-ayrilmama','Kromozom ayrılmama hataları'),
     'sayim':('by-bl3-sayim','Mikroskop sayımından evre süresi'),'grafik':('by-bl3-grafik','Hücre döngüsü DNA dağılımı grafiği'),'cesitlilik':('by-bl3-cesitlilik','Mayozda kromozom kökeni ve çeşitlilik'),
     'esesiz':('by-bl3-esesiz','Eşeysiz üreme yöntemleri ve klonlama'),'ikiz':('by-bl3-ikiz','İkizlik ve genetik özdeşlik')}
def kartla(n,tip,alt,fikir,tuzak,z,kalip,adim):
    kart(f'K-BYBL3-{n}',alt,fikir,tuzak,z,kalip,adim,TIP[tip][0],TIP[tip][1],KY)
def q(no,tip,ad,ne,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[tip][0],tip=TIP[tip][1],kart=f"K-BYBL3-{no[-2:]} ({TIP[tip][1].lower()}) · {ne}",**k)
def F(a,b=1): return Fr(a,b)
AX='tick label style={font=\\footnotesize},label style={font=\\small},axis lines=left'

# ============ 0001 · kromozom sayıları tablosu · kolay · olumsuz ============
kartla('01','kromozom','Vücut hücresi, gamet ve zigot kromozom sayıları','Gametler yarı sayıda (n), zigot ve vücut hücreleri tam sayıda (2n) kromozom taşır; döllenme gamet sayılarını toplayarak 2n’yi geri kazandırır.','Zigotta kromozom sayısını gametle aynı sanmak.','kolay','tablo',3)
TUR=[('İnsan',46),('Kedi',38),('Sirke sineği',8),('Bezelye',14),('At',64)]
SAT=[(t,2*n,n,2*n) for t,n in [(a,b//2) for a,b in TUR]]
SAT[4]=('At',64,32,32)
yanlis=[r[0] for r in SAT if not (r[1]==2*r[2] and r[3]==r[1])]; assert yanlis==['At']
S1=[r[0] for r in SAT]
q('0001','kromozom',[A('Kural','Gamet n, vücut hücresi ve zigot 2n kromozomludur; gamet sayısı vücut hücresinin yarısıdır.','Vücut: 2n · Gamet: n · Zigot: 2n'),
   A('Satırları sına','İnsan, kedi, sirke sineği ve bezelyede gamet sayısı yarıdır, zigot vücut hücresiyle aynıdır.','İnsan 46–23–46 · Kedi 38–19–38'),
   A('Hatalı satırı bul','At için zigot 32 yazılmıştır; zigot vücut hücresi kadar (64) kromozom taşımalıdır.','Hatalı: At')],
 'beş canlıda 2n, n ve zigot kromozom sayıları',z='kolay',alt='Eşeyli Üreme',kaz='Canlılarda gamet, zigot ve vücut hücresi kromozom sayılarını ilişkilendirir.',kalip='tablo',
 metin='Bir öğrenci, eşeyli üreyen beş canlının vücut hücresi, gamet ve zigot kromozom sayılarını aşağıdaki tabloya yazıyor. Canlıların hepsinde kromozom sayıları normaldir ve krossing-over gibi olaylar kromozom sayısını değiştirmemektedir.\nBuna göre, hangi canlıya ait satırdaki bilgi yanlıştır?',
 sekil=tablo_dar(['Canlı','Vücut hücresi','Gamet','Zigot'],[[a,str(b),str(c),str(d)] for a,b,c,d in SAT]),
 dogru='At',sira=yer('A','At',['İnsan','Kedi','Sirke sineği','Bezelye']),
 yan=[('İnsan','İnsanda 46 kromozomlu vücut hücresi, 23 kromozomlu gamet ve 46 kromozomlu zigot normaldir; satır doğrudur.','bilgi'),('Kedi','Kedide 38, 19 ve 38 kromozom değerleri tutarlıdır; satır doğrudur.','dikkat'),
      ('Sirke sineği','8, 4 ve 8 değerleri gamet yarı, zigot tam sayı kuralına uyar; satır doğrudur.','bilgi'),('Bezelye','14, 7 ve 14 değerleri kurala uygundur; satır doğrudur.','bilgi')],
 istenen='Bilgisi yanlış olan canlı.',
 ip=['Her satırda gamet sayısının vücut hücresine, zigot sayısının ise vücut hücresine ve gamete göre nasıl olması gerektiğini sına.'],
 bilgi=[B('Kromozom sayıları','Vücut hücreleri 2n, gametler n kromozom taşır · Döllenmede iki gametin kromozomları birleşir')],
 puf='Gamet, zigot ve vücut hücresi sayılarının birbirine oranını sına.')

# ============ 0002 · krossing-over gamet genotipi · orta ============
kartla('02','krossing','Krossing-over sonrası gamet genotipleri','Krossing-over, homolog kromozomların kardeş olmayan kromatitleri arasında parça alışverişidir; iki gen yeri arasında gerçekleşirse bu iki kromatit rekombinant olur, diğer ikisi parental kalır ve dört farklı gamet oluşur.','Kardeş kromatitler arasında alışveriş sanmak; tüm kromatitlerin değiştiğini düşünmek; krossing-overı hesaba katmamak.','orta','şekilli',4)
ch={'I':['A','B'],'II':['A','B'],'III':['a','b'],'IV':['a','b']}
def al(c): return ''.join(c)
ch2={k:list(v) for k,v in ch.items()}; ch2['II'][1],ch2['III'][1]=ch['III'][1],ch['II'][1]
gam=sorted(al(v) for v in ch2.values()); assert gam==sorted(['AB','Ab','aB','ab'])
nocross=sorted(al(v) for v in ch.values()); assert nocross==['AB','AB','ab','ab']
def gs(l): return ', '.join(sorted(l,key=lambda x:(x[0].islower(),x[1].islower(),x)))
G2=[gs(gam),'AB, AB, ab, ab','Ab, Ab, aB, aB','AB, AB, Ab, aB','Ab, aB, ab, ab']
assert gs(gam)=='AB, Ab, aB, ab'
xs={'I':0,'II':.9,'III':2.4,'IV':3.3}; col={'I':'black','II':'black','III':'vurgu','IV':'vurgu'}
b=[]
for k,x in xs.items():
    b.append(f'\\draw[{col[k]},line width=2.6pt] ({x},0)--({x},4);')
    dx=-.32 if k in('I','III') else .32
    for yy,a_ in ((3.2,ch[k][0]),(.8,ch[k][1])): b.append(f'\\node[font=\\normalsize\\bfseries,text={col[k]}] at ({x+dx},{yy}) {{{a_}}};')
    b.append(f'\\node[font=\\normalsize] at ({x},-.5) {{{k}}};')
b.append('\\draw[black,line width=1.6pt] (0,2)--(.9,2);\\draw[vurgu,line width=1.6pt] (2.4,2)--(3.3,2);\\fill (0.45,2) circle (.08);\\fill[vurgu] (2.85,2) circle (.08);')
b.append('\\draw[black,line width=1.1pt] (.9,1.65)--(2.4,1.25);\\draw[black,line width=1.1pt] (.9,1.25)--(2.4,1.65);')
SK2=tk('\n'.join(b),.9)
q('0002','krossing',[A('Gen yerlerini oku','I ve II aynı homolog kromozomun kromatitleri (AB), III ve IV öbür homologun kromatitleridir (ab).','I, II: AB · III, IV: ab'),
   A('Krossing-overı uygula','II ve III arasında A ve B arasındaki parçalar yer değiştirir: II A’yı tutar, B yerine b alır; III a’yı tutar, B alır.','II: Ab · III: aB'),
   A('Dört gameti yaz','I ve IV değişmeden kalır; mayoz sonunda her kromatit ayrı bir gamete gider.','I: AB · II: Ab · III: aB · IV: ab')],
 'tek homolog çifti, II ve III arasında krossing-over',z='orta',alt='Krossing-over',kaz='Şematik homolog çiftinde krossing-over sonrası oluşan gamet genotiplerini belirler.',kalip='şekilli',
 metin='Şekilde, A/a ve B/b gen yerlerini taşıyan ve mayoz bölünmeye giren bir hücredeki homolog kromozom çifti, her kromozom iki kromatitli olarak gösterilmiştir. Kromatitler I, II, III ve IV ile numaralandırılmıştır. Yalnızca II ve III numaralı kromatitler arasında, A ve B gen yerlerinin arasında bir kez krossing-over gerçekleşmiştir. Mayoz bölünme eksiksiz tamamlanmış ve başka bir değişiklik olmamıştır.\nBuna göre, bu hücreden oluşan dört gametin genotipleri aşağıdakilerden hangisinde verilmiştir?',
 sekil=SK2,dogru=G2[0],sira=yer('B',G2[0],G2[1:]),
 yan=[(G2[1],'Krossing-overı hesaba katmamış; parçalar yer değiştirmediği varsayılırsa yalnız ana kromatitler (AB, ab) bulunurdu.','bilgi'),
      (G2[2],'Dört kromatitin hepsinde parça değiştiğini sanmış; oysa yalnız II ve III arasında alışveriş olmuştur.','dikkat'),
      (G2[3],'I ve II’yi aynı kalmış sayıp ab kromatitini unutmuş; IV değişmeden ab olarak kalır.','dikkat'),
      (G2[4],'AB kromatitini unutmuş; I değişmeden AB olarak kalır.','dikkat')],
 istenen='Mayoz sonunda oluşan gametlerin genotipleri.',
 ip=['Hangi iki kromatitin kardeş olmadığını ve parça alışverişinin hangi gen yerini etkilediğini belirle; değişmeyen kromatitleri unutma.'],
 bilgi=[B('Krossing-over','Mayoz I profazında homolog kromozomların kardeş olmayan kromatitleri arasında parça alışverişidir ve gen birleşimlerini değiştirir')],
 puf='Parça alışverişi yalnız ilgili iki kromatiti değiştirir; diğer iki kromatit ana (parental) kalır.')

# ============ 0003 · mayoz II ayrılmama · orta ============
kartla('03','ayrilmama','Mayoz II’de kardeş kromatitlerin ayrılmaması','Mayoz II’de bir kromozomun kardeş kromatitleri ayrılmazsa oluşan dört gametten ikisi normal (n), biri n+1, biri n−1 kromozomlu olur; mayoz I’de homologlar ayrılmazsa dört gametin hepsi anormal olur.','Mayoz I ve II hatalarını karıştırmak; normal gametlerin bulunmasını yok saymak.','orta','şekilli',4)
GAM3={'I':['S'],'II':['L','S'],'III':['L','L','S'],'IV':['L','S']}
assert sorted(len(v) for v in GAM3.values())==[1,2,2,3] and sum(len(v) for v in GAM3.values())==8
normal=[k for k,v in GAM3.items() if sorted(v)==['L','S']]; assert len(normal)==2
b=[]
for i,(k,v) in enumerate(GAM3.items()):
    cx=i*2.1
    b.append(f'\\draw[line width=1.2pt] ({cx},0) circle (.85);')
    n=len(v); offs=[(i2-(n-1)/2)*.38 for i2 in range(n)]
    for o,c in zip(offs,sorted(v)):
        h=.62 if c=='L' else .34
        b.append(f'\\draw[line width=2.6pt] ({cx+o},{-h/2})--({cx+o},{h/2});')
    b.append(f'\\node[font=\\normalsize] at ({cx},-1.35) {{{k}}};')
SK3=tk('\n'.join(b),.95)
S3=['Mayoz II’de bir kromozomun kardeş kromatitleri ayrılmamıştır.','Mayoz I’de bir homolog çiftinin üyeleri ayrılmamıştır.','Mitoz sırasında kromatitler ayrılmamıştır.','Krossing-over sırasında kromozomlar parça değiştirmiştir.','Döllenme sırasında yumurtaya iki sperm girmiştir.']
q('0003','ayrilmama',[A('Gametleri say','I: 1, II: 2, III: 3, IV: 2 kromozom; normal gamet 2 kromozomludur (bir uzun, bir kısa).','Normal: II, IV · Anormal: I, III'),
   A('Hata türünü ayır','Dört gametin ikisi normalse hata yalnız bir ikinci bölünme hücresinde olmuştur; mayoz I’de ayrılmama dört gametin hepsini bozardı.','Normal gamet var → mayoz II hatası'),
   A('Nedeni bul','Uzun kromozomun kardeş kromatitleri bir kutba gitmiş; o kutupta 3, öbür kutupta 1 kromozom oluşmuştur.','Cevap: mayoz II’de kardeş kromatitler ayrılmamış')],
 'dört gamet, kromozom sayıları 2n=4',z='orta',alt='Ayrılmama',kaz='Gametlerin kromozom sayılarından ayrılmama hatasının hangi bölünmede olduğunu belirler.',kalip='şekilli',
 metin='Şekilde, 2n = 4 kromozomlu bir canlının tek bir üreme ana hücresinden mayoz bölünmeyle oluşan dört hücre (I, II, III ve IV) gösterilmiştir. Uzun ve kısa çubuklar, iki farklı homolog çiftinin kromozomlarını simgelemektedir. Bölünme sırasında yalnızca bir hata olmuştur ve krossing-over gerçekleşmemiştir.\nBuna göre, aşağıdakilerden hangisi bu hatayı doğru biçimde açıklar?',
 sekil=SK3,dogru=S3[0],sira=yer('E',S3[0],S3[1:]),
 yan=[(S3[1],'Mayoz I’de homologlar ayrılmasaydı dört gametin hepsi anormal olurdu (ikisi 3, ikisi 1 kromozomlu); şekilde iki normal gamet vardır.','bilgi'),
      (S3[2],'Mitoz bölünme gamet oluşumunda görev almaz; şekildeki dört hücre mayozla oluşmuştur.','dikkat'),
      (S3[3],'Krossing-over kromozom sayısını değiştirmez; gametlerdeki sayı farkı parça alışverişiyle açıklanamaz.','bilgi'),
      (S3[4],'Döllenme gamet oluşumundan sonra olur; şekildeki hücreler gamet oluşumu sırasındaki hatayı gösterir.','bilgi')],
 istenen='Gametlerdeki kromozom sayılarını açıklayan hata.',
 ip=['Dört gametteki kromozom sayılarını yaz ve normal gametlerin bulunup bulunmadığına bak.'],
 bilgi=[B('Ayrılmama','Bölünme sırasında kromozomların ya da kromatitlerin ayrılmaması gametlerde kromozom sayısının artıp azalmasına yol açar')],
 puf='Normal gamet kalıyorsa hata ikinci bölünmededir; normal gamet kalmıyorsa hata birinci bölünmededir.')

# ============ 0004 · sayım tablosu · orta ============
kartla('04','sayim','Mikroskop sayımından evre süresi','Eş zamanlı olmayan bölünen hücre toplulukları incelendiğinde bir evrede sayılan hücre oranı, o evrenin döngü içindeki süre oranına eşittir; evre süresi = döngü süresi × evrenin hücre oranı.','Hücre sayısını doğrudan dakika sanmak; evreleri tek tek toplamamak; oranı döngü süresiyle çarpmamak.','orta','tablo',4)
SAY={'İnterfaz':160,'Profaz':20,'Metafaz':8,'Anafaz':4,'Telofaz':8}; TOP=sum(SAY.values()); assert TOP==200
DONGU=1200; dk=lambda e:Fr(DONGU*SAY[e],TOP); assert dk('Anafaz')==24 and dk('Telofaz')==48 and dk('Anafaz')+dk('Telofaz')==72 and dk('Profaz')==120
q('0004','sayim',[A('Sayımı yorumla','Hücreler eş zamanlı olmadığından her evrede sayılan hücre oranı o evrenin süre oranını verir.','Evre süresi ∝ hücre sayısı'),
   A('Bir hücrenin süre karşılığını bul','Döngü 20 saat = 1200 dk, sayılan hücre 200 olduğundan her hücre 6 dk’ya karşılık gelir.','1200 / 200 = 6 dk'),
   A('Evre sürelerini hesapla','Anafaz 4 hücre, telofaz 8 hücredir.','Anafaz: 24 dk · Telofaz: 48 dk'),
   A('Toplamı bul','İkisi toplanır.','24 + 48 = 72 dk')],
 'kök ucu hücre sayımı, 200 hücre, 20 saatlik döngü',z='orta',alt='Hücre Döngüsü',kaz='Mikroskopta sayılan hücre dağılımından evrelerin süresini hesaplar.',kalip='tablo',
 metin='Bir araştırmacı, kök ucu hücrelerinden hazırladığı preparatta rastgele seçtiği 200 hücrenin bulunduğu evreleri sayıyor ve sonuçları aşağıdaki tabloda gösteriyor. Hücreler eş zamanlı olmayan biçimde bölünmektedir ve tüm hücreler hücre döngüsündedir. Bu hücrelerde bir hücre döngüsü 20 saat sürmektedir.\nBuna göre, anafaz ve telofaz evrelerinin toplam süresi kaç dakikadır?',
 sekil=tablo_dar(['Evre','Hücre sayısı'],[[k,str(v)] for k,v in SAY.items()]),
 dogru=72,yan=[(12,'Anafaz ve telofazdaki hücre sayısını (4 + 8) dakika olarak yazmış; sayı süreye çevrilmemiştir.','dikkat'),(24,'Yalnızca anafaz süresini bulmuş; telofazı toplamaya katmamıştır.','dikkat'),
   (48,'Yalnızca telofaz süresini bulmuş; anafazı toplamaya katmamıştır.','dikkat'),(120,'Profaz süresini (20 hücre × 6 dk) bulmuş; istenen evreler anafaz ve telofazdır.','dikkat')],
 istenen='Anafaz ve telofazın toplam süresi (dakika).',
 ip=['Sayılan hücrelerin neyi temsil ettiğini düşün.'],
 bilgi=[B('Hücre döngüsü','Hücre döngüsü interfaz ve mitozdan oluşur · Mitoz profaz, metafaz, anafaz ve telofaz evrelerini içerir')],
 puf='Eş zamanlı olmayan hücrelerde evredeki hücre oranı o evrenin süre oranını yansıtır.')

# ============ 0005 · DNA dağılımı grafiği · zor · öncüllü ============
kartla('05','grafik','Hücre başına DNA miktarı dağılımı ve ilaç etkisi','Hücre başına DNA miktarı 2 birim olanlar G1 evresindedir, 2–4 birim S evresinde, 4 birim olanlar G2 ya da mitoz evresindedir; ilaçlı grupta 4 birimlik hücrelerin oranı artıyorsa hücreler G2/mitozda birikmiştir.','G1 oranının arttığını sanmak; DNA eşlenmesinin tamamen durduğunu düşünmek.','orta','öncüllü',4)
KON=[60,15,25]; ILA=[25,10,65]; assert sum(KON)==sum(ILA)==100
d5={'I':(False,'İlaçlı grupta 2 birim DNA’lı (G1) hücrelerin oranı %60’tan %25’e düşmüştür; G1’deki hücre yüzdesi artmamıştır.'),
    'II':(False,'İlaçlı grupta DNA’sı 4 birime ulaşan hücrelerin oranı artmıştır; yani DNA eşlenmesi gerçekleşmiştir, tamamen engellenmemiştir.'),
    'III':(True,'4 birim DNA’lı hücrelerin oranı %25’ten %65’e çıkmıştır; hücreler G2 ya da mitoz evresinde birikmiştir.')}
r=onc(d5,True,'C')
b=['\\begin{axis}[ybar,width=7.8cm,height=5.4cm,xmin=.4,xmax=3.6,xtick={1,2,3},xticklabels={2 birim,2–4 birim,4 birim},ymin=0,ymax=80,ytick={0,20,40,60,80},xlabel={Hücre başına DNA miktarı},ylabel={Hücre oranı (\\%)},bar width=14pt,legend style={font=\\small,at={(0.5,1.04)},anchor=south,legend columns=2},'+AX+']',
   '\\addplot[fill=white,draw=black,line width=1pt] coordinates {'+' '.join(f'({i+1},{v})' for i,v in enumerate(KON))+'};\\addlegendentry{Kontrol}',
   '\\addplot[fill=vurgu!45,draw=black,line width=1pt] coordinates {'+' '.join(f'({i+1},{v})' for i,v in enumerate(ILA))+'};\\addlegendentry{İlaçlı}','\\end{axis}']
SK5=tk('\n'.join(b),1.0)
q('0005','grafik',[A('Grafiği oku','Kontrolde 2 birimlik hücreler %60, 4 birimlikler %25’tir; ilaçlıda sırasıyla %25 ve %65’tir.','2 birim: 60 → 25 · 4 birim: 25 → 65'),
   adim_onc(d5,'I'),adim_onc(d5,'II'),adim_onc(d5,'III'),sonuc(r,True)],
 'ilaçlı ve ilaçsız hücre grupları, DNA miktarı dağılımı',z='orta',alt='Hücre Döngüsü',kaz='Hücre başına DNA dağılımı grafiğinden ilacın hücre döngüsüne etkisini yorumlar.',kalip='öncüllü',
 metin='Bölünebilen hücreler iki gruba ayrılıyor; birine bir ilaç uygulanıyor, diğeri kontrol olarak bırakılıyor. Bir süre sonra her gruptaki hücrelerin DNA miktarı ölçülüyor ve hücreler, hücre başına DNA miktarına göre üç sınıfa ayrılıyor. G1 evresindeki hücreler 2 birim, DNA eşlenmesini tamamlamış G2 ve mitoz evresindeki hücreler 4 birim DNA içermektedir. Sonuçlar grafikte gösterilmiştir.\nBuna göre,\nI. İlaç, G1 evresindeki hücrelerin oranını artırmıştır.\nII. İlaç, DNA eşlenmesini tamamen engellemiştir.\nIII. İlaçlı grupta hücrelerin bir bölümü G2 ya da mitoz evresinde birikmiştir.\nyargılarından hangileri doğrudur?',
 sekil=SK5,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['İki grubun her DNA sınıfındaki hücre oranlarını karşılaştır ve hangi sınıfın arttığına bak.'],
 bilgi=[B('Hücre döngüsünde DNA','G1’de DNA miktarı 2 birimdir, S evresinde eşlenir ve 4 birime çıkar · Mitoz sonunda DNA miktarı yeniden 2 birime iner')],
 puf='Oranı artan sınıfın hangi evreye karşılık geldiğine bak.')

# ============ 0006 · metafaz I kromozom kökeni · orta ============
kartla('06','cesitlilik','Metafaz I dizilişi ve kutuptaki gametlerin kökeni','Metafaz I’de her homolog çiftinin hangi üyesinin hangi kutba gideceği şekildeki dizilişle belirlenir; bir kutuptaki hücre mayoz II’de ikiye bölünerek kardeş kromatitleri iki gamete dağıtır, bu yüzden kutuptaki her kromozom iki gamette bulunur.','Kardeş kromatitleri hesaba katmamak; öbür kutbu da saymak; kromozom kökenini renkle karıştırmak.','orta','şekilli',4)
DIZ=[('B','G'),('G','B'),('B','G')]    # sol, sağ: B=siyah(anne) G=yeşil(baba)
sol=[x[0] for x in DIZ]; sag=[x[1] for x in DIZ]
cevap=2*sol.count('B'); assert (sol.count('B'),sag.count('B'),cevap)==(2,1,4)
CM={'B':'black','G':'vurgu'}; LEN=[.62,.46,.32]; YP=[.8,0,-.8]
def kr(x,y,h,c):    # çift kromatitli kromozom: iki yan yana çizgi + sentromer
    return (f'\\draw[{CM[c]},line width=2pt] ({x-.05},{y-h/2})--({x-.05},{y+h/2});\\draw[{CM[c]},line width=2pt] ({x+.05},{y-h/2})--({x+.05},{y+h/2});'
            f'\\fill[{CM[c]}] ({x},{y}) circle (.045);')
b=['\\draw[line width=1.1pt] (0,0) ellipse (1.7 and 1.5);\\draw[dashed,line width=.6pt,gray] (0,-1.5)--(0,1.5);']
for i2,(l,rr) in enumerate(DIZ):
    y=YP[i2]; h=LEN[i2]
    b.append(kr(-.2,y,h,l)+kr(.2,y,h,rr))
    b.append(f'\\draw[gray,line width=.5pt] (-1.5,0)--(-.28,{y});\\draw[gray,line width=.5pt] (1.5,0)--(.28,{y});')
b.append('\\fill (-1.5,0) circle (.06);\\fill (1.5,0) circle (.06);')
b.append('\\node[font=\\small,anchor=west] at (2.0,.4) {\\textcolor{black}{\\rule{8pt}{3pt}}~anneden};\\node[font=\\small,anchor=west] at (2.0,-.1) {\\textcolor{vurgu}{\\rule{8pt}{3pt}}~babadan};')
SK6=tk('\n'.join(b),1.0)
q('0006','cesitlilik',[A('Sol kutba giden kromozomları oku','Sol kutba soldaki üç kromozom gider: siyah, yeşil, siyah.','Sol kutup: 2 siyah, 1 yeşil'),
   A('Mayoz II’yi uygula','Sol kutuptaki hücre mayoz II’de ikiye bölünür; her kromozomun kardeş kromatitleri ayrı gametlere gider.','2 gamet, her biri 2 siyah + 1 yeşil'),
   A('Siyah kromozomları topla','Her gametin iki siyah kromozomu vardır.','2 gamet × 2 siyah = 4')],
 '2n=6, metafaz I dizilişi, sol kutuptaki hücre',z='orta',alt='Mayozda Çeşitlilik',kaz='Metafaz I dizilişinden bir kutuptaki hücrenin oluşturacağı gametlerin anne kökenli kromozomlarını sayar.',kalip='şekilli',
 metin='Şekilde, 2n = 6 kromozomlu bir hayvanın üreme ana hücresi, mayoz I’in metafaz evresinde gösterilmiştir. Siyah kromozomlar anneden, yeşil kromozomlar babadan gelmiştir. Hücre krossing-over olmadan bölünmesini tamamlayacaktır.\nBuna göre, sol kutba giden hücrenin mayoz II’yi tamamlaması sonucu oluşan iki gametin toplamında anneden gelen kaç kromozom bulunur?',
 sekil=SK6,dogru=4,yan=[(2,'Yalnızca bir gametin siyah kromozomlarını saymış; sol kutuptaki hücre iki gamet oluşturur.','dikkat'),(3,'Sol kutuptaki üç kromozomun hepsini anne kökenli saymış; oysa içlerinden biri yeşildir.','dikkat'),
   (6,'İki gametteki bütün kromozomları (2 × 3) anne kökenli saymış; kökenler renklerden okunmalıdır.','islem'),(8,'Dört gametin hepsini hesaba katmış; soru yalnız sol kutuptaki hücrenin gametlerini sorar.','dikkat')],
 istenen='Sol kutuptaki hücreden oluşan iki gametin toplamındaki anne kökenli kromozom sayısı.',
 ip=['Sol kutba giden kromozomları şekilden oku ve mayoz II’de kardeş kromatitlerin nereye gittiğini düşün.'],
 bilgi=[B('Mayozda dağılım','Mayoz I’de homologlar kutuplara ayrılır; mayoz II’de her kromozomun kardeş kromatitleri ayrılarak iki ayrı gamete gider')],
 puf='Önce kutba giden kromozomların kökenini oku, sonra gametlere dağılımı düşün.')

# ============ 0007 · aşılama · kolay · olumsuz ============
kartla('07','esesiz','Aşılama (kalem–anaç) ve genotip','Aşılama eşeysiz bir üremedir; aşılanan dalın hücreleri mitozla çoğalır ve kalemin genotipini taşır, anaç dalın genotipini değiştirmez. Tohumlar ise eşeyli üremenin ürünüdür ve genotipleri farklıdır.','Tohumdan gelen bitkinin kalemle özdeş olduğunu sanmak; anaçtan genotip geçtiğini sanmak.','kolay','hikâyeli',3)
S7=['Aşılanan dalda oluşan elmaların tohumlarından yetişen bitkiler, kalemle aynı genotipi taşır.','Aşılama, eşeysiz üreme yöntemlerinden biridir.','Aşılanan dalın hücreleri mitozla çoğalır ve genotipi kalemin genotipiyle aynıdır.','Anaç ağacın hücreleri, aşılanan dalın genotipini değiştirmez.','Aşılanan dalda oluşan elmanın kabuk ve et dokuları kalemin genotipini taşır.']
q('0007','esesiz',[A('Aşılamayı tanımla','Aşılama, kalemin anaca bağlanıp gelişmesiyle yapılan eşeysiz üremedir.','Aşılama = eşeysiz'),
   A('İfadeleri sına','Dal mitozla çoğaldığı için kalemle aynıdır; anaç bunu değiştirmez; meyve dokuları da kalemin dokularıdır.','4 ifade doğru'),
   A('Tohumu ele','Tohum, çiçekte gametlerin birleşmesiyle (eşeyli üreme) oluşur; genotipi kalemden farklı olabilir.','Tohumdan gelen bitki ≠ kalem')],
 'tatlı elma kalemi, ekşi elma anacı',z='kolay',alt='Eşeysiz Üreme',kaz='Aşılamanın eşeysiz üreme olduğunu ve genotip aktarımını yorumlar.',kalip='hikâyeli',
 metin='Bir meyve bahçesinde, tatlı elma veren bir elma ağacının dalı (kalem), ekşi elma veren başka bir elma ağacının gövdesine (anaç) aşılanıyor. Aşılanan dal gelişiyor, çiçek açıyor ve meyve veriyor. Ağaçlarda mutasyon gerçekleşmemiştir.\nBu aşılama ile ilgili aşağıdakilerden hangisi söylenemez?',
 dogru=S7[0],sira=yer('A',S7[0],S7[1:]),
 yan=[(S7[1],'Aşılama bitkilerde yapay eşeysiz üreme yöntemidir; ifade doğrudur.','bilgi'),(S7[2],'Dal, mitoz bölünmeyle çoğalır; hücreler kalemle genetik olarak özdeştir. İfade doğrudur.','bilgi'),
      (S7[3],'Anaç yalnızca su ve besin sağlar; kalemin genotipi değişmez. İfade doğrudur.','dikkat'),(S7[4],'Meyvenin kabuk ve et dokuları dalın vücut hücrelerinden oluşur; kalemin genotipini taşır. İfade doğrudur.','dikkat')],
 istenen='Aşılama ile ilgili söylenemeyen ifade.',
 ip=['Hangi yapıların mitozla, hangilerinin gametlerin birleşmesiyle oluştuğunu ayır.'],
 bilgi=[B('Eşeysiz ve eşeyli üreme','Eşeysiz üremede yavrular mitozla oluşur ve ana canlıyla genetik olarak özdeştir · Eşeyli üremede gametlerin birleşmesiyle genetik çeşitlilik doğar')],
 puf='Mitozla oluşan dokularla gametlerin birleşmesiyle oluşan yapıları ayır.')

# ============ 0008 · ikizler · orta · öncüllü · olumsuz ============
kartla('08','ikiz','Tek yumurta ve çift yumurta ikizleri','Tek yumurta ikizleri bir zigotun mitozla ayrılmasıyla oluşur, genetik olarak özdeştir ve aynı cinsiyettedir; çift yumurta ikizleri iki yumurtanın iki ayrı sperm tarafından döllenmesiyle oluşur ve genetik olarak sıradan kardeşler gibidir.','Tüm ikizleri genetik özdeş sanmak; tek yumurta ikizlerinde cinsiyetin farklı olabileceğini düşünmek.','kolay','öncüllü',4)
d8={'I':(True,'Tek yumurta ikizleri aynı zigotun mitozla bölünmesinden oluştuğundan genetik materyalleri aynıdır.'),
    'II':(False,'Çift yumurta ikizleri tek bir zigottan değil, iki ayrı yumurtanın iki ayrı spermle döllenmesinden oluşur; tek bir zigotun ayrılması tek yumurta ikizlerini tanımlar.'),
    'III':(False,'Tek yumurta ikizleri aynı zigottan oluştuğundan cinsiyet kromozomları da aynıdır; mutasyon yoksa aynı cinsiyettedirler, farklı cinsiyette olamazlar.')}
r=onc(d8,False,'E')
q('0008','ikiz',[A('İkiz türlerini ayır','Tek yumurta ikizi bir zigottan, çift yumurta ikizi iki zigottan oluşur.','Tek: 1 zigot · Çift: 2 zigot'),
   adim_onc(d8,'I'),adim_onc(d8,'II'),adim_onc(d8,'III'),sonuc(r,False)],
 'insanda tek ve çift yumurta ikizleri',z='kolay',alt='İnsanda Üreme',kaz='Tek yumurta ve çift yumurta ikizlerinin oluşumunu ve genetik özelliklerini karşılaştırır.',kalip='öncüllü',
 metin='İnsanda tek yumurta ikizleri, bir zigotun erken evrede mitozla bölünüp iki ayrı embriyoya dönüşmesiyle oluşur; çift yumurta ikizleri ise farklı bir yolla oluşur. Ailelerde mutasyon gerçekleşmediği varsayılmaktadır.\nBu ikizlerle ilgili,\nI. Tek yumurta ikizlerinin genetik materyali aynıdır.\nII. Çift yumurta ikizleri, tek bir zigotun mitozla ayrılmasıyla oluşur.\nIII. Tek yumurta ikizleri farklı cinsiyette olabilir.\nyargılarından hangileri söylenemez?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Söylenemeyen yargılar.',
 ip=['Her ikiz türünün kaç zigottan oluştuğunu ve zigotun nasıl bölündüğünü düşün.'],
 bilgi=[B('Zigot ve mitoz','Zigot, iki gametin birleşmesiyle oluşan ilk hücredir · Mitozla oluşan hücreler birbirinin genetik kopyasıdır')],
 puf='İkizliğin oluşum yolunu ve zigot sayısını sorgula.')

# ============ 0009 · klonlama şeması · orta · öncüllü ============
kartla('09','esesiz','Hücre çekirdeği aktarımıyla klonlama','Vücut hücresi çekirdeği, çekirdeği çıkarılmış yumurtaya aktarılarak oluşan hücre mitozla bölünür ve embriyo olur; yavrunun çekirdek DNA’sı çekirdek vericisiyle aynıdır ve bu yöntem gametlerin birleşmesi olmadığından eşeysiz üremeye benzer.','Yavruyu taşıyıcı ananın ya da yumurta vericinin klonu sanmak; döllenme olduğunu düşünmek.','orta','öncüllü',4)
d9={'I':(True,'Yavrunun çekirdekteki DNA’sı, çekirdeği aktarılan vücut hücresinin sahibi olan koyun A ile aynıdır.'),
    'II':(False,'Taşıyıcı ana C yalnızca embriyoyu rahminde taşır; yavrunun çekirdek DNA’sı C’den değil A’dan gelir. Yavru C’nin klonu değildir.'),
    'III':(True,'Bu yöntemde gametlerin birleşmesi (döllenme) olmaz ve yavru bir vücut hücresi çekirdeğinden gelişir; bu nedenle eşeysiz üremeye benzer.')}
r=onc(d9,True,'D')
bx=lambda n,x,y,t:f'\\node[draw,rounded corners=3pt,inner sep=4pt,align=center,text width=2.9cm,font=\\small,line width=.9pt] ({n}) at ({x},{y}) {{{t}}};'
bl=[bx('a',0,4.2,'Koyun A:\\\\vücut hücresi'),bx('bb',4.6,4.2,'Koyun B: çekirdeği\\\\çıkarılmış\\\\yumurta hücresi'),
    bx('c',2.3,2.2,'A’nın çekirdeği,\\\\B’nin yumurtasına\\\\aktarılır'),bx('d',2.3,0.4,'Oluşan hücre bölünerek\\\\embriyo olur'),bx('e',2.3,-1.4,'Embriyo, Koyun C’nin\\\\rahmine yerleştirilir'),bx('f',2.3,-3.2,'Yavru doğar')]
for a_,b_ in [('a','c'),('bb','c'),('c','d'),('d','e'),('e','f')]: bl.append(f'\\draw[{OKU},line width=1pt] ({a_})--({b_});')
SK9=tk('\n'.join(bl),.9)
q('0009','esesiz',[A('Şemayı oku','A’nın vücut hücresinin çekirdeği, çekirdeği çıkarılmış B yumurtasına aktarılır; embriyo C’nin rahminde gelişir.','A: çekirdek verici · B: sitoplazma verici · C: taşıyıcı'),
   adim_onc(d9,'I'),adim_onc(d9,'II'),adim_onc(d9,'III'),sonuc(r,True)],
 'koyun A çekirdeği, B yumurtası, C rahmi',z='orta',alt='Klonlama',kaz='Çekirdek aktarımıyla klonlamada yavrunun kalıtımsal kaynağını ve üreme türünü yorumlar.',kalip='öncüllü',
 metin='Şekilde, bir koyun klonlama deneyinin aşamaları gösterilmiştir.\nBuna göre,\nI. Doğan yavrunun çekirdeğindeki DNA, Koyun A’nınkiyle aynıdır.\nII. Doğan yavru, Koyun C’nin genetik olarak klonudur.\nIII. Bu yöntemle yavru oluşumu eşeysiz üremeye benzer.\nyargılarından hangileri doğrudur?',
 sekil=SK9,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Çekirdeğin hangi koyundan geldiğine ve bu üretimde gametlerin birleşmesi olup olmadığına bak.'],
 bilgi=[B('Klonlama','Bir canlıyla genetik olarak özdeş yavru elde etmeye klonlama denir · Eşeysiz üremede yavrular gametlerin birleşmesi olmadan oluşur')],
 puf='Çekirdek DNA’sı çekirdeğin kaynağından gelir; taşıyıcı ana yalnızca gelişimi barındırır.')

# ============ 0010 · mayoz I ayrılmama · zor · öncüllü ============
kartla('10','ayrilmama','Mayoz I’de homolog çiftinin ayrılmaması','Mayoz I’de bir homolog çifti ayrılmazsa mayoz II sonunda oluşan dört gametin ikisi n+1, ikisi n−1 kromozomlu olur ve hiçbiri normal değildir; mayoz II’de ayrılmamada ise ikisi normaldir.','Mayoz I ve II hatalarının sonuçlarını karıştırmak; normal gamet kaldığını sanmak.','orta','öncüllü',5)
n=23
m1=sorted([n+1,n+1,n-1,n-1]); m2=sorted([n+1,n-1,n,n])
assert all(x!=n for x in m1) and sum(x==n for x in m2)==2
d10={'I':(True,'Mayoz I’de homolog çifti ayrılmazsa oluşan iki hücrenin biri 24, diğeri 22 kromozomlu olur ve mayoz II bunları değiştirmez; dört gametin hiçbiri 23 kromozomlu (normal) değildir.'),
     'II':(True,'Dört gametin ikisi 24 (n+1), ikisi 22 (n−1) kromozom taşır.'),
     'III':(False,'Aynı çiftte ayrılmama mayoz II’de olsaydı dört gametin ikisi normal (23) olurdu; bu yüzden hiçbir normal sperm oluşmayacağı doğru değildir.')}
r=onc(d10,True,'B')
q('0010','ayrilmama',[A('Mayoz I hatasını uygula','Homolog çifti ayrılmayınca bir hücre iki üyeyi de alır (24), öbürü hiç almaz (22).','Mayoz I sonu: 24 ve 22'),
   adim_onc(d10,'I'),adim_onc(d10,'II'),adim_onc(d10,'III'),sonuc(r,True)],
 'insan sperm ana hücresi, 21. çift ayrılmıyor',z='orta',alt='Ayrılmama',kaz='Mayoz I’deki ayrılmama hatasının gametlerin kromozom sayısına etkisini yorumlar.',kalip='öncüllü',
 metin='İnsanda bir sperm ana hücresinin mayoz I bölünmesinde 21. homolog kromozom çifti ayrılmıyor ve çiftin ikisi de aynı kutba gidiyor. Başka bir hata olmuyor, bölünmelerin diğer bütün basamakları normal gerçekleşiyor ve mayoz II eksiksiz tamamlanıyor.\nBuna göre,\nI. Oluşan dört spermin hiçbiri 23 kromozomlu değildir.\nII. Spermlerin ikisi 24, ikisi 22 kromozomludur.\nIII. Aynı çiftteki ayrılmama mayoz II’de olsaydı yine hiçbir normal sperm oluşmazdı.\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Ayrılmayan çiftin gittiği kutbu izle.'],
 bilgi=[B('Ayrılmama','Gametlerde kromozom sayısının normalden farklı olması ayrılmamadan kaynaklanır · Mayoz II sırasında kardeş kromatitler ayrılır')],
 puf='Önce mayoz I sonundaki iki hücreyi yaz, sonra her birinin mayoz II’de ikiye bölündüğünü uygula.')

bitir(P,'bolunmeuc',UK)
