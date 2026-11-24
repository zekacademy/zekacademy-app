"""AYT Fizik · Modern Fiziğin Teknolojideki Uygulamaları · 20 soru (kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from math import sin,cos,tan,radians,sqrt,pi,asin,degrees
KON='Modern Fiziğin Teknolojideki Uygulamaları'
H.KONU=KON
P=Parti('teknoloji',KON,'afiz|'+KON,ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM AYT 2018–2025 Fizik (modern fiziğin teknolojideki uygulamaları; yalnız mantık) · 345 AYT Fizik s.382–392 · Bilgi Sarmal AYT Fizik · MEB 12. sınıf fizik'
TIPLER={'te-lazer':'Lazer ışığı ve uyarılmış emisyon','te-goruntu':'Tıbbi görüntüleme (röntgen, MR, PET)','te-led':'LED ve diyot','te-yari':'Yarı iletkenler ve elektronik devre elemanları',
 'te-gunes':'Güneş pili','te-super':'Süper iletkenler','te-nano':'Nanoteknoloji','te-fiber':'Fiber optik'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AFTE-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AFTE-{kn:02d} ('+CARD[kn]+')',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
CHEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def D(a,b,o='thick'): return f'\\draw[{o}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def AR(a,b,o='vurgu,very thick'): return f'\\draw[{o},{ARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def tikz(lines,head=HEAD): return tikz_svg(head+'\n'.join(lines)+TAIL)
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
LZ=B('Lazer ışığı','uyarılmış emisyonla oluşur; fotonlar aynı frekanslı (tek renkli), aynı fazlı (eş fazlı) ve aynı doğrultuludur; demet çok az dağılır. Atom E₂ → E₁ geçişinde E = E₂ − E₁ enerjili foton yayar. Örnek: 3 eV’luk iki düzey arası geçişte 3 eV’luk foton çıkar')
FE=B('Foton enerjisi','E = h × f = h × c ÷ λ. h × c = 1240 eV·nm alınırsa λ(nm) = 1240 ÷ E(eV) olur. Örnek: E = 4 eV ise λ = 310 nm')
GRN=B('Görüntüleme yöntemleri','röntgen ve bilgisayarlı tomografi (BT) X ışınlarıyla, MR güçlü manyetik alan ve radyo dalgalarıyla, PET hastaya verilen radyoaktif izleyicinin yaydığı pozitronun elektronla yok olurken oluşturduğu gama fotonlarıyla görüntü verir. X ışını ve gama ışını iyonlaştırıcıdır; MR’da iyonlaştırıcı ışınım yoktur')
YI=B('Yarı iletkenler','silisyum ve germanyum gibi son yörüngesinde 4 elektron bulunan maddelerdir. Katkı ile n tipi (serbest elektron fazla) ya da p tipi (deşik fazla) elde edilir. Diyot p–n birleşimidir; p ucu üretecin (+) kutbuna bağlıysa akım geçirir, ters bağlıysa geçirmez. Yarı iletkenin direnci sıcaklık artınca azalır')
DY=B('Diyot ve LED','ideal diyot ileri yönde dirençsiz iletir, ters yönde hiç iletmez; sembolde üçgenin gösterdiği yön akımın geçebildiği yöndür. LED ışık yayan diyottur; ileri gerilim düşümü Vd olan LED’le seri direnç üzerindeki gerilim V − Vd’dir')
SP=B('Süper iletkenler','kritik sıcaklığın (T_c) altında direnci sıfır olur; akım ısı kaybı olmadan taşınır (P = i²R = 0). Mıknatıs alanını içine almaz (Meissner olayı), bu yüzden mıknatıs üzerinde havada durur. Kullanım: MR bobinleri, maglev treni, parçacık hızlandırıcıları')
GP=B('Güneş pili','yarı iletken p–n birleşimidir. Foton enerjisi yarı iletkenin yasak bant aralığından büyükse elektron–deşik çifti oluşur ve devrede doğru akım geçer. Işık şiddeti artınca birim zamanda yutulan foton sayısı ve akım artar')
NN=B('Nanoteknoloji','1 nm = 10⁻⁹ m. Madde 1–100 nm ölçeğinde işlenir; boyut küçüldükçe yüzey/hacim oranı artar ve elektrik, manyetik, optik özellikler değişebilir. Kenarı a olan küpte yüzey alanı/hacim = 6 ÷ a')
FB=B('Fiber optik','ışık, kırıcılık indisi büyük çekirdek ile küçük kılıf arasında tam yansımayla taşınır. Tam yansıma için gelme açısı kritik açıdan büyük olmalıdır: sinθ_c = n_kılıf ÷ n_çekirdek. Havadan uca gelen ışık için Snell yasası n₁ × sinθ₁ = n₂ × sinθ₂ uygulanır')
# ===== 01 kolay · lazer öncüllü
card(1,'Lazer ışığının özellikleri','Lazer, uyarılmış emisyonla oluşan eş fazlı, tek renkli ve az dağılan ışıktır.','Lazerin sıradan lamba gibi her yöne yayıldığını sanmak.','kolay','öncüllü',3,'te-lazer','lazerin üç özelliği yargı olarak sorulur')
q('0001',tipId='te-lazer',tip=TIPLER['te-lazer'],z='kolay',alt='Lazer',kaz='Lazer ışığının oluşumunu ve özelliklerini ayırt eder.',kalip='öncüllü',
 metin='Bir lazer işaretleyiciden çıkan ışık, karşı duvarda küçük ve parlak bir nokta oluşturmaktadır. Aynı odada bulunan sıradan bir akkor lamba ise odayı her yönde aydınlatmaktadır.\nBuna göre lazer ışığı ile ilgili,\nI. Atomların kendiliğinden foton yaymasıyla oluşur.\nII. Fotonları aynı fazdadır.\nIII. Işık kaynağından uzaklaştıkça demet geniş bir açıyla dağılır.\nyargılarından hangileri doğrudur?',
 sekil=None,istenen='Lazer ışığı için doğru yargılar.',
 ip=['Lazerin nasıl oluştuğunu ve fotonlarının birbirine göre durumunu düşün; demetin yayılma biçimini lambayla karşılaştır.'],
 bilgi=[LZ],
 ad=[A('I. yargı','Lazerde uyarılmış düzeydeki atomlar gelen fotonla aynı özellikte foton yayar; kendiliğinden yayınlama lazeri oluşturmaz.','Uyarılmış emisyon → I yanlış'),
     A('II. yargı','Uyarılmış emisyonla çıkan fotonlar gelen fotonla aynı fazlı ve aynı doğrultudadır.','Eş fazlı → II doğru'),
     A('III. yargı','Lazer demeti paralele yakındır ve çok az dağılır; geniş açıyla dağılan sıradan lambadır.','III yanlış')],
 puf='Lazer = uyarılmış emisyon + eş faz + tek renk + paralel demet.',
 **onc([False,True,False],['lazer kendiliğinden yayınlamayla değil, uyarılmış emisyonla oluşur','uyarılmış emisyonla çıkan fotonlar aynı fazlıdır','lazer demeti çok az dağılır, geniş açıyla yayılmaz'],0))
# ===== 02 kolay · enerji düzeyleri
E1,E2,E3=Fr(0),Fr(2),Fr(5,2); HC=1240
lam=lambda e:Fr(HC)/Fr(e)
assert lam(E2-E1)==620 and lam(E3-E1)==496 and lam(E3-E2)==2480 and lam((E2-E1)*2)==310 and lam((E2-E1)/2)==1240
card(2,'Uyarılmış emisyonda foton dalga boyu','Yayılan fotonun enerjisi iki düzey arası farktır; λ = 1240 ÷ E.','Üst düzeyin ya da komşu düzeyin enerjisini foton enerjisi sanmak.','kolay','şekilli',3,'te-lazer','düzey şemasından foton dalga boyu')
o=[]
for e,nm in ((E1,'E_1'),(E2,'E_2'),(E3,'E_3')):
    y=float(e)*1.6; o.append(D((0,y),(3.2,y),'thick')); o.append(N(-.2,y,f'${nm}={fm(e)}$ eV','left,font=\\scriptsize'))
o.append(AR((1.2,float(E2)*1.6),(1.2,float(E1)*1.6),'thick,dashed')); o.append(N(1.5,1.6,'$h f$','right,font=\\scriptsize'))
o.append(f'\\fill (1.2,{float(E2)*1.6:.2f}) circle (2.6pt);'); o.append(N(2.5,float(E2)*1.6+.35,'atom','font=\\scriptsize'))
SK=tikz(o)
q('0002',tipId='te-lazer',tip=TIPLER['te-lazer'],z='kolay',alt='Lazer',kaz='Enerji düzeyi şemasından uyarılmış emisyonla yayılan fotonun dalga boyunu hesaplar.',kalip='şekilli',
 metin='Bir lazerin aktif ortamındaki atomların enerji düzeyleri şekilde verilmiştir. E₂ düzeyinde uyarılmış hâlde bekleyen bir atoma, E₂ → E₁ geçişine karşılık gelen enerjide bir foton çarpmakta ve atom uyarılmış emisyon yapmaktadır. h × c = 1240 eV·nm alınacaktır.\nBuna göre, atomdan çıkan fotonların her birinin dalga boyu kaç nm’dir?',
 sekil=SK,dogru=620,yan=[(496,'E₃ ile E₁ arasındaki farkı (2,5 eV) foton enerjisi almış.','dikkat'),(2480,'E₃ ile E₂ arasındaki farkı (0,5 eV) foton enerjisi almış.','dikkat'),
  (310,'İki foton çıktığı için enerjiyi 4 eV almış ve dalga boyunu yarıya indirmiş.','bilgi'),(1240,'Enerjiyi iki foton arasında paylaştırıp 1 eV almış; oysa her foton 2 eV enerjilidir.','bilgi')],
 istenen='Çıkan fotonların dalga boyu (nm).',
 ip=['Foton enerjisini hangi iki düzey arasındaki farkın belirlediğine bak, sonra enerjiyi dalga boyuna çevir.'],
 bilgi=[LZ,FE],
 ad=[A('Foton enerjisi','Yayılan foton, geçişin yapıldığı iki düzey arasındaki farka eşit enerji taşır.','E = E₂ − E₁ = 2,0 − 0 = 2,0 eV'),
     A('Dalga boyuna çevir','Verilen h × c çarpımı kullanılır.','λ = 1240 ÷ 2,0'),
     A('Sonuç','Uyarılmış emisyondaki fotonlar aynı enerjilidir.','λ = 620 nm')],
 puf='Foton enerjisi geçişe giren iki düzeyin farkıdır; diğer düzeyler soruya katılmaz.')
# ===== 03 kolay · görüntüleme tablo öncüllü
card(3,'Cihaz–ilke eşleşmesi','Röntgen X ışını, MR manyetik alan ve radyo dalgası, PET gama fotonu kullanır.','PET’i ultrasonla ya da MR’ı iyonlaştırıcı ışınla karıştırmak.','kolay','tablo',3,'te-goruntu','cihaz ve ilkesi tablosu')
SK=tablo_svg(['Yargı','Cihaz','Görüntü elde etmede kullanılan'],[['I','Röntgen','X ışınları'],['II','MR','Radyoaktif izleyicinin yaydığı gama ışınları'],['III','PET','Pozitron–elektron yok olmasıyla oluşan gama fotonları']])
q('0003',tipId='te-goruntu',tip=TIPLER['te-goruntu'],z='kolay',alt='Görüntüleme',kaz='Röntgen, MR ve PET cihazlarının görüntü oluşturma ilkelerini ayırt eder.',kalip='tablo',
 metin='Bir hastanede kullanılan üç görüntüleme cihazı ile her cihazın görüntü elde etmede yararlandığı ışınım aşağıdaki tabloda eşleştirilmiştir.\nBuna göre tablodaki I, II ve III numaralı eşleştirmelerden hangileri doğrudur?',
 sekil=SK,istenen='Doğru eşleştirmeler.',
 ip=['Her cihazın görüntüyü hangi fiziksel olaydan elde ettiğini ayrı ayrı düşün.'],
 bilgi=[GRN],
 ad=[A('Röntgen','Röntgen cihazı, dokularda farklı soğurulan X ışınlarıyla görüntü verir.','I: X ışını → doğru'),
     A('MR','MR güçlü manyetik alan ve radyo dalgası kullanır; radyoaktif izleyici gerekmez.','II: gama ışını → yanlış'),
     A('PET','PET’te pozitron ile elektron yok olurken zıt yönlü gama fotonları çıkar.','III: gama fotonu → doğru')],
 puf='Röntgen: X ışını · MR: manyetik alan ve radyo dalgası · PET: yok olma gamaları.',
 **onc([True,False,True],['röntgen X ışınlarıyla görüntü verir','MR radyoaktif izleyicinin gamasıyla değil, manyetik alan ve radyo dalgalarıyla çalışır','PET pozitron–elektron yok olmasından çıkan gamaları kullanır'],4))
# ===== 04 zor · diyotlu paralel kollar
card(4,'Diyot yönü ve kol akımları','İdeal diyot yalnız ileri yönde iletir; ileten kolların akımları lamba direncinden hesaplanır ve toplanır.','Ters bağlı diyotlu kolu da ileten saymak ya da seri iki lambayı tek lamba gibi hesaplamak.','zor','şekilli',5,'te-yari','dört kollu diyotlu devrede pil akımı')
Vb=6; Rl=Fr(6**2,3); assert Rl==12
iK=Fr(Vb)/Rl; iL=0; iM=Fr(Vb)/(2*Rl); iN=Fr(Vb)/Rl; Itop=iK+iL+iM+iN
assert (iK,iM,Itop)==(Fr(1,2),Fr(1,4),Fr(5,4))
assert iL+iK*0+0+Fr(1,2)==Fr(1,2) and 3*iK==Fr(3,2) and iK+iK+iM+iN==Fr(7,4) and 4*iK==2
o=['\\draw (0,4) to[battery1] (0,0);','\\draw (0,4) -- (8.5,4); \\draw (0,0) -- (8.5,0);',N(-.45,3.5,'$+$'),N(-.45,.5,'$-$'),N(-.9,2,'$6$ V','font=\\scriptsize')]
xs=[2,4.2,6.4,8.5]
o+=[f'\\draw ({xs[0]},4) to[D] ({xs[0]},2.8) to[lamp] ({xs[0]},1.4) -- ({xs[0]},0);',
    f'\\draw ({xs[1]},0) to[D] ({xs[1]},1.2) to[lamp] ({xs[1]},2.6) -- ({xs[1]},4);',
    f'\\draw ({xs[2]},4) to[D] ({xs[2]},3.0) to[lamp] ({xs[2]},1.9) to[lamp] ({xs[2]},.8) -- ({xs[2]},0);',
    f'\\draw ({xs[3]},4) to[D] ({xs[3]},2.8) to[lamp] ({xs[3]},1.4) -- ({xs[3]},0);']
for x,nm in zip(xs,'KLMN'): o.append(N(x,4.4,nm,'font=\\small\\bfseries'))
o+=[f'\\fill ({x},4) circle (1.6pt) ({x},0) circle (1.6pt);' for x in xs[:3]]
SK=tikz(o,CHEAD)
q('0004',tipId='te-yari',tip=TIPLER['te-yari'],z='zor',alt='Diyot',kaz='Diyotlu paralel kolların hangisinin ilettiğini belirleyip ideal pilden çekilen akımı hesaplar.',kalip='şekilli',
 metin='Şekildeki devrede iç direnci ihmal edilen üretecin gerilimi 6 V’tur. Devredeki lambaların hepsi özdeştir ve üzerlerinde “6 V – 3 W” yazmaktadır; lamba dirençleri sabit alınacaktır. Diyotlar idealdir ve sembollerdeki üçgenin gösterdiği yön akımın geçebildiği yöndür.\nBuna göre, üretecin ana koldan verdiği akım kaç A’dir?',
 sekil=SK,dogru=Fr(5,4),yan=[(Fr(1,2),'Diyot yönlerini ters okuyup yalnız L kolunu ileten saymış; bu kolda 0,5 A akım geçer.','bilgi'),(Fr(3,2),'M kolundaki iki seri lambayı tek lamba gibi hesaplamış: 3 × 0,5 = 1,5 A.','islem'),
  (Fr(7,4),'Ters bağlı diyotlu L kolunu da ileten saymış: 0,5 + 0,5 + 0,25 + 0,5 = 1,75 A.','bilgi'),(2,'Dört kolu da 0,5 A akım geçiriyor sanmış; hem diyot yönünü hem seri lambaları dikkate almamış.','dikkat')],
 istenen='Üretecin verdiği akım (A).',
 ip=['Önce her kolda akımın geçip geçmediğine diyot yönünden karar ver; geçen kollarda lamba sayısına bak.'],
 bilgi=[DY],
 ad=[A('Lamba direnci','Lambanın üzerindeki değerlerden direnç bulunur.','R = V² ÷ P = 36 ÷ 3 = 12 Ω'),
     A('Hangi kollar iletir','K, M ve N kollarında diyot ileri yönde; L kolunda ters yöndedir.','L kolunda akım = 0'),
     A('Kol akımları','Her ileten kol 6 V’a bağlıdır; M kolunda iki lamba seri.','i_K = i_N = 6 ÷ 12 = 0,5 A · i_M = 6 ÷ 24 = 0,25 A'),
     A('Ana kol akımı','Paralel kolların akımları toplanır.','i = 0,5 + 0 + 0,25 + 0,5 = 1,25 A')],
 puf='Diyotlu devrede önce hangi kolun ilettiğini belirle, sonra ileten kolların akımlarını topla.')
# ===== 05 orta · süper iletken R–T grafiği öncüllü
TK=lambda t:Fr(0) if t<=50 else (Fr(4)*(t-50)/10 if t<=60 else 4+Fr(2,40)*(t-60))
TL=lambda t:1+Fr(3,100)*t
assert TK(30)==0 and TK(70)==Fr(9,2) and TL(70)==Fr(31,10) and TK(70)>TL(70) and all(TL(t)>0 for t in range(0,101))
gx=['\\begin{axis}[width=6.6cm,height=5.2cm,xmin=0,xmax=100,ymin=0,ymax=7,xtick distance=10,ytick distance=1,grid=both,major grid style={gray!45,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$T$ (K)},ylabel={$R$ ($\\Omega$)},xlabel style={font=\\small},ylabel style={font=\\small}]',
 '\\addplot[thick,vurgu] coordinates {(0,0) (50,0) (60,4) (100,6)};','\\addplot[thick,dashed] coordinates {(0,1) (100,4)};',
 '\\node[font=\\small\\bfseries,vurgu] at (axis cs:88,6.5) {K};','\\node[font=\\small\\bfseries] at (axis cs:90,3.35) {L};','\\end{axis}']
SK=tikz(gx)
card(5,'Direnç–sıcaklık grafiği','Süper iletkende T_c altında R = 0; ısı açığa çıkmaz. Normal iletkende direnç sıfırlanmaz.','Grafikten değer okurken K ve L eğrilerini karıştırmak; L’nin de sıfıra gideceğini sanmak.','orta','grafik',3,'te-super','iki telin R–T grafiği üç yargı')
q('0005',tipId='te-super',tip=TIPLER['te-super'],z='orta',alt='Süper İletkenlik',kaz='Direnç–sıcaklık grafiğinden süper iletken ile normal iletkenin davranışını karşılaştırır.',kalip='grafik',
 metin='K ve L tellerinin dirençlerinin sıcaklıkla değişimi grafikte verilmiştir. Teller aynı boyutta olup uçlarına ayrı ayrı sabit akım uygulanmaktadır.\nBuna göre,\nI. 30 K’de K telinden geçen akım telde ısı açığa çıkarmaz.\nII. 70 K’de K telinin direnci L telinin direncinden büyüktür.\nIII. L teli, grafikte gösterilen sıcaklıklarda süper iletken değildir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Grafikte her yargının sözünü ettiği sıcaklıkta iki eğrinin değerini ayrı ayrı oku.'],
 bilgi=[SP],
 ad=[A('I. yargı','30 K’de K telinin direnci sıfırdır; ısı gücü i² × R ile bulunur.','R = 0 → P = 0 → I doğru'),
     A('II. yargı','70 K’de K eğrisi yaklaşık 4,5 Ω, L eğrisi yaklaşık 3,1 Ω’dur.','R_K > R_L → II doğru'),
     A('III. yargı','L eğrisi hiçbir sıcaklıkta sıfıra inmez.','L süper iletken değil → III doğru')],
 puf='Grafikte direnci sıfır olan bölge süper iletken haldir; sıfıra inmeyen eğri normal iletkendir.',
 **onc([True,True,True],['K telinin direnci 30 K’de sıfırdır ve ısı oluşmaz','70 K’de K telinin direnci L telinden büyüktür','L telinin direnci hiçbir sıcaklıkta sıfır olmaz'],4))
# ===== 06 orta · güneş pili şeması
o=['\\draw[thick] (0,1.3) rectangle (4,2.0); \\draw[thick] (0,.6) rectangle (4,1.3);',N(2,1.65,'N tipi yarı iletken'),N(2,.95,'P tipi yarı iletken'),
   '\\draw[thick,fill=gray!40] (0,2.0) rectangle (1.0,2.15); \\draw[thick,fill=gray!40] (0,.45) rectangle (4,.6);',N(.3,2.45,'üst kontak','left,font=\\scriptsize'),
   D((.5,2.15),(.5,3.0)),D((.5,3.0),(5.3,3.0)),'\\draw (5.3,3.0) to[lamp] (5.3,1.0); \\draw (5.3,1.0) -- (5.3,.3) -- (2,.3) -- (2,.45);',N(2.2,.12,'alt kontak','font=\\scriptsize')]
for x in (1.7,2.5,3.3): o.append(AR((x-.9,3.1),(x,2.02),'thick,vurgu'))
o.append(N(1.2,3.5,'Güneş ışığı (fotonlar)','font=\\scriptsize'))
SK=tikz(o,CHEAD)
card(6,'Güneş pilinin çalışması','Foton enerjisi elektron–deşik çifti oluşturur; ışık şiddeti arttıkça akım artar; akım doğru akımdır.','Güneş pilini ısıtıcı ya da alternatif akım kaynağı sanmak.','orta','şekilli',3,'te-gunes','güneş pili şeması üç yargı')
q('0006',tipId='te-gunes',tip=TIPLER['te-gunes'],z='orta',alt='Güneş Pili',kaz='Güneş pilinin çalışma ilkesini ve ışık şiddetinin etkisini yargılar.',kalip='şekilli',
 metin='Şekildeki düzenekte p–n birleşimli bir güneş pili, bir lambaya bağlanmıştır. Pilin üst yüzeyine tek renkli ışık gönderilmekte ve lamba yanmaktadır.\nBuna göre,\nI. Pil, ışık enerjisini ısı enerjisine dönüştürerek lambayı yakar.\nII. Yüzeye düşen fotonlar, yarı iletkende elektron–deşik çiftleri oluşturur.\nIII. Işığın dalga boyu değişmeden şiddeti artırılırsa lambadan geçen akım artar.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Pilin çıkışındaki enerji türünü ve ışığın pilde yaptığı etkiyi ayrı ayrı düşün.'],
 bilgi=[GP],
 ad=[A('I. yargı','Güneş pili ışık enerjisini doğrudan elektrik enerjisine dönüştürür.','I yanlış'),
     A('II. yargı','Foton yeterli enerjiliyse yarı iletkende elektron–deşik çifti oluşur.','II doğru'),
     A('III. yargı','Şiddet artınca birim zamanda yutulan foton sayısı artar.','akım artar → III doğru')],
 puf='Güneş pili: foton → elektron–deşik çifti → akım; şiddet arttıkça akım artar.',
 **onc([False,True,True],['pil ışık enerjisini doğrudan elektrik enerjisine dönüştürür','fotonlar elektron–deşik çifti oluşturur','şiddet arttıkça yutulan foton sayısı ve akım artar'],4))
# ===== 07 orta · LED tablo
Eg={'K':Fr(31,20),'L':Fr(2),'M':Fr(31,10)}; lm={k:Fr(1240)/v for k,v in Eg.items()}
assert lm=={'K':800,'L':620,'M':400} and lm['K']-lm['M']==400 and lm['L']-lm['M']==220 and lm['K']-lm['L']==180 and lm['K']+lm['L']==1420
SK=tablo_svg(['LED','Yasak bant aralığı (eV)'],[['K','1,55'],['L','2,0'],['M','3,1']])
card(7,'LED ışığının dalga boyu','LED’in yaydığı fotonun enerjisi yasak bant aralığına eşittir; λ = 1240 ÷ E.','Bant aralığını dalga boyu sanmak ya da yanlış LED’leri karşılaştırmak.','orta','tablo',4,'te-led','üç LED için dalga boyu farkı')
q('0007',tipId='te-led',tip=TIPLER['te-led'],z='orta',alt='LED',kaz='Yasak bant aralığından LED’in yaydığı ışığın dalga boyunu hesaplar.',kalip='tablo',
 metin='Farklı yarı iletkenlerden yapılmış K, L ve M LED’lerinin yasak bant aralıkları tabloda verilmiştir. LED’ler ileri yönde çalıştırıldığında yaydıkları fotonun enerjisi, yasak bant aralığına eşit alınacaktır. h × c = 1240 eV·nm’dir.\nBuna göre, K LED’inin yaydığı ışığın dalga boyu L LED’inin yaydığı ışığınkinden kaç nm fazladır?',
 sekil=SK,dogru=180,yan=[(220,'L ile M LED’lerinin dalga boylarını karşılaştırmış: 620 − 400 = 220 nm.','dikkat'),(400,'K ile M LED’lerinin dalga boylarını karşılaştırmış: 800 − 400 = 400 nm.','dikkat'),
  (800,'Yalnız K LED’inin dalga boyunu hesaplayıp L ile farkını almayı unutmuş.','dikkat'),(1420,'Dalga boylarının farkı yerine toplamını almış: 800 + 620 = 1420 nm.','islem')],
 istenen='K ve L LED’lerinin ışık dalga boyları farkı (nm).',
 ip=['İki LED için de foton enerjisinden dalga boyunu ayrı ayrı bul, sonra farkı al.'],
 bilgi=[DY,FE],
 ad=[A('K LED’i','Foton enerjisi bant aralığına eşittir.','λ_K = 1240 ÷ 1,55 = 800 nm'),
     A('L LED’i','Aynı bağıntı L için uygulanır.','λ_L = 1240 ÷ 2,0 = 620 nm'),
     A('Fark','İstenen K’nin L’den fazlalığıdır.','800 − 620 = 180 nm')],
 puf='LED’de bant aralığı büyüdükçe foton enerjisi artar, dalga boyu kısalır.')
# ===== 08 orta · LED + seri direnç
Vs,Vd,Ia=6,2,Fr(20,1000); Rr=(Vs-Vd)/Ia
assert Rr==200 and Fr(Vd)/Ia==100 and Fr(Vs)/Ia==300 and Fr(Vs+Vd)/Ia==400 and (Vs-Vd)*20==80
o=['\\draw (0,3) to[battery1,l=$6$ V] (0,0);',N(-.45,2.6,'$+$'),N(-.45,.4,'$-$'),'\\draw (0,3) -- (1.2,3) to[R,l=$R$] (3.4,3) -- (4.4,3);','\\draw (4.4,3) to[leD,l=LED] (4.4,0);','\\draw (4.4,0) -- (0,0);']
SK=tikz(o,CHEAD)
card(8,'LED’e seri direnç','LED üzerinde ileri gerilim düşümü kadar gerilim düşer; kalanı seri dirence düşer.','Direnç hesabında LED gerilimini hesaba katmamak ya da eklemek.','orta','şekilli',3,'te-led','LED akımına göre seri direnç')
q('0008',tipId='te-led',tip=TIPLER['te-led'],z='orta',alt='LED',kaz='LED’in ileri gerilim düşümünü kullanarak seri direnç değerini hesaplar.',kalip='şekilli',
 metin='Şekildeki devrede 6 V’luk üretecin iç direnci ihmal edilmiştir. LED ileri yönde çalışırken uçları arasında 2 V’luk sabit gerilim düşmekte ve LED’den 20 mA akım geçmektedir.\nBuna göre, R direnci kaç Ω’dur?',
 sekil=SK,dogru=200,yan=[(80,'Gerilim farkını (4 V) akımla çarpmış: 4 × 20 = 80.','islem'),(100,'Yalnız LED’in gerilimini (2 V) akıma bölmüş.','dikkat'),(300,'Üretecin gerilimini LED gerilimini hesaba katmadan akıma bölmüş: 6 ÷ 0,02 = 300 Ω.','dikkat'),(400,'LED gerilimini üreteç gerilimine eklemiş: (6 + 2) ÷ 0,02 = 400 Ω.','bilgi')],
 istenen='R direnci (Ω).',
 ip=['Seri devrede üreteç gerilimi LED ile direnç arasında paylaşılır; direnç üzerindeki gerilimi bul.'],
 bilgi=[DY],
 ad=[A('Direnç gerilimi','Üreteç gerilimi LED ve dirençte paylaşılır.','V_R = 6 − 2 = 4 V'),
     A('Akım birimi','mA, A’e çevrilir.','20 mA = 0,02 A'),
     A('Ohm yasası','Seri devrede akım ortaktır.','R = 4 ÷ 0,02 = 200 Ω')],
 puf='LED’li devrede direnç, üreteç gerilimiyle LED gerilimi farkı üzerinden hesaplanır.')
# ===== 09 orta · fiber optik tam yansıma öncüllü
n1,n2=Fr(3,2),Fr(6,5); th=60
s60=sqrt(3)/2
assert n2/n1==Fr(4,5) and s60>0.8 and Fr(7,5)/n1==Fr(14,15) and 14/15>s60
tn=tan(radians(30)); pts=[(0,.7),(.7/tn,1.4),(1.4/tn+.7/tn,0.0),(5.0,(5.0-(1.4/tn+.7/tn))*tn)]
o=['\\fill[gray!25] (0,1.4) rectangle (5,2.0); \\fill[gray!25] (0,-.6) rectangle (5,0);','\\draw[thick] (0,1.4) -- (5,1.4); \\draw[thick] (0,0) -- (5,0);',
   N(4.3,1.75,'kılıf  $n_2=1{,}2$','font=\\scriptsize'),N(4.3,-.3,'kılıf  $n_2=1{,}2$','font=\\scriptsize'),N(3.0,1.1,'çekirdek  $n_1=1{,}5$','font=\\scriptsize')]
for a,b in zip(pts,pts[1:]): o.append(AR(a,b,'thick,vurgu') if b==pts[-1] else D(a,b,'thick,vurgu'))
hx=pts[1][0]; o.append(D((hx,.9),(hx,1.9),'thin,dashed')); o.append(f'\\draw ({hx:.3f},1.4)+(-150:.55) arc (-150:-90:.55);'); o.append(N(hx-.62,.82,'$60^\\circ$','font=\\scriptsize'))
SK=tikz(o)
card(9,'Fiber optikte tam yansıma','Çekirdekten kılıfa gelen ışın kritik açıdan büyük açıyla gelirse tam yansır; kritik açı sinθ_c = n₂ ÷ n₁.','Kılıfın indisi artınca tam yansımanın kolaylaştığını sanmak; ışık hızını indisle doğru orantılı bulmak.','orta','öncüllü',4,'te-fiber','çekirdek–kılıf sınırında tam yansıma yargıları')
q('0009',tipId='te-fiber',tip=TIPLER['te-fiber'],z='orta',alt='Fiber Optik',kaz='Çekirdek–kılıf sınırında kritik açıyı karşılaştırarak tam yansımayı yorumlar.',kalip='öncüllü',
 metin='Bir fiber optik kablonun çekirdeğinin kırıcılık indisi 1,5, kılıfının kırıcılık indisi 1,2’dir. Çekirdek içinde ilerleyen bir ışık ışını, çekirdek–kılıf sınırına şekildeki gibi normalle 60° açı yaparak gelmektedir. sin 60° ≈ 0,87 alınacaktır.\nBuna göre,\nI. Işın çekirdek–kılıf sınırında tam yansımaya uğrar.\nII. Kılıfın kırıcılık indisi 1,4 yapılırsa ışın yine tam yansır.\nIII. Işığın çekirdekteki hızı kılıftakinden büyüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Kritik açının sinüsünü kılıf ve çekirdek indislerinin oranından bul, gelme açısının sinüsüyle karşılaştır.'],
 bilgi=[FB],
 ad=[A('I. yargı','Kritik açının sinüsü indis oranıdır.','sinθ_c = 1,2 ÷ 1,5 = 0,8 < 0,87 → tam yansıma → I doğru'),
     A('II. yargı','Yeni oran: 1,4 ÷ 1,5 ≈ 0,93.','0,87 < 0,93 → ışın kılıfa geçer → II yanlış'),
     A('III. yargı','Hız v = c ÷ n olduğundan indisi büyük ortamda hız küçüktür.','v_çekirdek < v_kılıf → III yanlış')],
 puf='Tam yansıma için sin(gelme açısı) > n_kılıf ÷ n_çekirdek olmalıdır; kılıfın indisi büyüdükçe koşul zorlaşır.',
 **onc([True,False,False],['gelme açısının sinüsü (0,87) kritik açının sinüsünden (0,8) büyüktür','kılıfın indisi 1,4 olunca kritik açının sinüsü 0,93 olur ve ışın kılıfa geçer','ışık indisi büyük ortamda daha yavaş yayılır; çekirdekte hız daha küçüktür'],0))
# ===== 10 zor · fiber optik giriş açısı
nf=Fr(5,4); sc_=1/nf; cth=sqrt(1-float(sc_)**2); sin_max=nf*Fr(3,5)
assert sc_==Fr(4,5) and sin_max==Fr(3,4) and Fr(3,5)/nf==Fr(12,25) and sin_max!=1
thv=30; beta=degrees(asin(sin(radians(thv))/float(nf))); tb=tan(radians(beta)); Hh=1.4
o=['\\fill[gray!15] (0,0) rectangle (5.2,1.4);','\\draw[thick] (0,1.4) -- (5.2,1.4); \\draw[thick] (0,0) -- (5.2,0); \\draw[thick] (0,0) -- (0,1.4);',
   N(3.0,.45,'$n=1{,}25$','font=\\scriptsize'),N(3.0,1.75,'hava ($n=1$)','font=\\scriptsize'),N(3.0,-.3,'hava ($n=1$)','font=\\scriptsize')]
y0=.7; xo=-1.7; yo=y0-(-xo)*tan(radians(thv))
x1=(Hh-y0)/tb; x2=x1+Hh/tb
o+=[AR((xo,yo),(0,y0),'thick,vurgu'),D((0,y0),(x1,Hh),'thick,vurgu'),D((x1,Hh),(x2,0),'thick,vurgu'),AR((x2,0),(5.1,(5.1-x2)*tb),'thick,vurgu'),D((-1.2,y0),(.8,y0),'thin,dashed')]
o.append(f'\\draw (0,{y0})+({180+thv}:.8) arc ({180+thv}:180:.8);'); o.append(N(-1.15,y0-.25,'$\\theta$','font=\\small'))
SK=tikz(o)
card(10,'Fiberde en büyük giriş açısı','Ucu hava içindeki fiberde tam yansıma için Snell yasası ile kritik açı birlikte kullanılır: sinθ_maks = √(n² − 1).','Kritik açının sinüsünü (0,8) ya da kırılma açısının sinüsünü (0,6) giriş açısı sanmak.','zor','şekilli',5,'te-fiber','hava içinde fiber ucuna giriş açısı')
q('0010',tipId='te-fiber',tip=TIPLER['te-fiber'],z='zor',alt='Fiber Optik',kaz='Fiber ucuna gelen ışının tam yansıma yapabilmesi için gerekli en büyük giriş açısını Snell yasası ve kritik açıyla bulur.',kalip='şekilli',
 metin='Kırıcılık indisi 1,25 olan ve kılıfı bulunmayan, havada duran bir fiber optik çubuğun ucuna hava ortamından ışık gönderiliyor. Işın, uç yüzeyin normaliyle θ açısı yapacak biçimde şekildeki gibi gelmektedir; ışının çubuğun yan yüzeyinde tam yansıma yaparak ilerleyebilmesi isteniyor.\nBuna göre, θ açısının sinüsü en çok kaç olabilir?',
 sekil=SK,dogru=Fr(3,4),yan=[(Fr(12,25),'Uçta kırılma açısının sinüsünü (0,6) bulup hava–çubuk geçişindeki 1,25 oranına bölmüş: 0,6 ÷ 1,25 = 0,48.','islem'),(Fr(3,5),'Yan yüzeydeki kritik açıdan bulunan 0,6 değerini uçtaki gelme açısının sinüsü sanmış; Snell yasasını uç yüzeye uygulamamış.','bilgi'),
  (Fr(4,5),'Yan yüzeydeki kritik açının sinüsünü (1 ÷ 1,25 = 0,8) giriş açısının sinüsü sanmış.','bilgi'),(1,'Uç yüzeye gelen her ışının çubukta tam yansıyarak ilerleyeceğini düşünüp en büyük değeri 1 yazmış.','dikkat')],
 istenen='θ açısının sinüsünün en büyük değeri.',
 ip=['Önce yan yüzeydeki sınır koşulundan uçtaki kırılma açısını bul, sonra uç yüzeyde Snell yasasını yaz.'],
 bilgi=[FB],
 ad=[A('Yan yüzey','Tam yansımanın sınır durumunda gelme açısı kritik açıdır.','sinθ_c = 1 ÷ 1,25 = 0,8'),
     A('Uçtaki kırılma açısı','Uçta kırılan ışının yan yüzeye gelme açısı ile kırılma açısı birbirini 90°’ye tamamlar.','sinβ = cosθ_c = 0,6'),
     A('Uçta Snell yasası','Hava indisi 1, çubuk indisi 1,25’tir.','1 × sinθ = 1,25 × 0,6'),
     A('Sonuç','Daha büyük θ’da yan yüzeye gelme açısı kritik açıdan küçük kalır.','sinθ_maks = 0,75')],
 puf='Fiberin kabul açısı iki sınırın birleşimidir: yan yüzeyde kritik açı, uç yüzeyde Snell yasası.')
# ===== 11 orta · röntgen tüpü
Vk=31; lmin=Fr(HC,Vk*1000); assert lmin==Fr(1,25) and Fr(HC,Vk*100)==Fr(2,5) and Fr(HC,Vk)==40
assert Fr(HC,Vk*1000)==Fr(4,100) and Fr(HC,2*Vk*1000)==Fr(2,100) and Fr(HC,Vk*500)==Fr(8,100)
o=['\\draw[thick,rounded corners=10pt] (0,0) rectangle (5,2.4);','\\draw[thick] (.7,1.0) -- (.9,1.4) -- (1.1,1.0) -- (1.3,1.4) -- (1.5,1.0);',N(.95,.55,'katot','font=\\scriptsize'),
   '\\draw[thick,fill=gray!40] (3.6,.7) -- (4.2,.7) -- (4.2,1.7) -- (3.6,1.7) -- cycle;',N(4.45,.5,'anot','font=\\scriptsize')]
for y in (1.1,1.3): o.append(AR((1.7,y),(3.5,y),'thick,vurgu'))
o.append(N(2.6,1.65,'elektronlar','font=\\scriptsize')); o.append(AR((3.9,.9),(3.9,-1.0),'thick'));o.append(N(3.9,-1.25,'X ışını','font=\\scriptsize'))
o.append('\\draw (1.1,1.4) -- (1.1,3.4) -- (2.0,3.4); \\draw (4.2,3.4) to[battery1,l=$31$ kV] (2.0,3.4); \\draw (4.2,3.4) -- (4.2,1.7);'); o.append(N(.8,2.9,'$-$')); o.append(N(4.55,2.9,'$+$'))
SK=tikz(o,CHEAD)
card(11,'X ışınının en kısa dalga boyu','Elektronun kazandığı enerji eV kadardır; en kısa dalga boyunda bu enerjinin tamamı tek fotona gider.','kV’u V sanmak, dönüşümü yanlış yapmak ya da enerjiyi yarıya bölmek.','orta','şekilli',3,'te-goruntu','röntgen tüpünde gerilimden λ_min')
q('0011',tipId='te-goruntu',tip=TIPLER['te-goruntu'],z='orta',alt='Röntgen',kaz='Röntgen tüpünün hızlandırma geriliminden üretilen X ışınının en kısa dalga boyunu hesaplar.',kalip='şekilli',
 metin='Şekildeki röntgen tüpünde katottan kopan elektronlar, 31 kV’luk gerilimle hızlandırılarak anoda çarpmakta ve X ışını oluşmaktadır. Elektronların katottan kopma anındaki kinetik enerjisi ihmal edilecektir. Bir elektronun kinetik enerjisinin tamamı tek bir X ışını fotonuna dönüştüğünde en kısa dalga boylu foton elde edilir. h × c = 1240 eV·nm’dir.\nBuna göre, tüpten çıkan X ışınlarının en kısa dalga boyu kaç nm’dir?',
 sekil=SK,dogru=Fr(4,100),yan=[(Fr(2,100),'Elektronun enerjisini iki katı (62 keV) almış.','bilgi'),(Fr(8,100),'Enerjinin yarısının (15,5 keV) fotona gittiğini düşünmüş.','bilgi'),(Fr(4,10),'31 kV’u 3100 V almış; ondalık kaydırmayı yanlış yapmış.','islem'),(40,'31 kV’u 31 V yani 31 eV almış; kilo çevirmesini unutmuş.','islem')],
 istenen='En kısa dalga boylu X ışınının dalga boyu (nm).',
 ip=['Elektronun anoda varırken kazandığı enerjiyi eV cinsinden yaz; bu enerji foton enerjisinin üst sınırıdır.'],
 bilgi=[FE,GRN],
 ad=[A('Elektron enerjisi','Elektron 31 kV’luk gerilimle hızlanır.','E = e × V = 31 000 eV'),
     A('En kısa dalga boyu','Enerjinin tamamı tek fotona gidince foton enerjisi en büyük olur.','λ_min = 1240 ÷ 31 000'),
     A('Sonuç','Bölme yapılır.','λ_min = 0,04 nm')],
 puf='Röntgen tüpünde gerilim büyüdükçe fotonun enerjisinin üst sınırı artar, en kısa dalga boyu küçülür.')
# ===== 12 zor · PET zaman farkı
cc=3*10**8; dt=Fr(5,10**10); xm=cc*dt/2*100
assert xm==Fr(15,2) and cc*dt*100==15 and cc*dt*100/4==Fr(15,4) and 2*cc*dt*100==30 and 3*10**9*dt*100/2==75
o=['\\draw[thick] (0,0) circle (2.2);','\\draw[dashed,gray] (0,0) ellipse (1.2 and .8);',N(0,-.5,'hasta','font=\\scriptsize'),'\\fill[gray!55] (-2.45,-.3) rectangle (-2.15,.3); \\fill[gray!55] (2.15,-.3) rectangle (2.45,.3);',
   N(-2.85,0,'D$_1$'),N(2.85,0,'D$_2$'),'\\fill (0,0) circle (1.5pt);',N(0,.25,'O','font=\\scriptsize'),'\\fill[vurgu] (.55,0) circle (2.4pt);',N(.55,.35,'E','font=\\small\\bfseries,vurgu'),
   AR((.5,0.04),(2.1,.04),'thick,vurgu'),AR((.6,-.04),(-2.1,-.04),'thick,vurgu'),N(1.4,.6,'foton','font=\\scriptsize'),N(-1.4,.6,'foton','font=\\scriptsize')]
SK=tikz(o)
card(12,'PET’te varış zamanı farkı','Zıt yönlü iki foton merkezden x kaymış noktadan çıkarsa yol farkı 2x olur; Δt = 2x ÷ c.','Yol farkını x sanıp 2 çarpanını atlamak ya da gereksiz bölmek.','zor','şekilli',4,'te-goruntu','PET yok olma noktasının merkezden uzaklığı')
q('0012',tipId='te-goruntu',tip=TIPLER['te-goruntu'],z='zor',alt='PET',kaz='PET’te zıt yönlü iki fotonun dedektörlere varış zamanı farkından yok olma noktasının konumunu bulur.',kalip='şekilli',
 metin='Bir PET cihazında, hastaya verilen radyoaktif izleyiciden salınan pozitron bir elektronla yok olduğunda zıt yönlerde iki gama fotonu yayılır. Fotonlar, halka biçimindeki dedektör düzeneğinin çap uçlarındaki D₁ ve D₂ dedektörlerine ulaşmıştır; yok olma noktası E, halkanın merkezi O ile D₂ dedektörünün arasındaki doğru parçası üzerindedir. D₂’ye ulaşan foton, D₁’e ulaşandan 0,5 ns önce kaydedilmiştir. Işık hızı 3 × 10⁸ m/s’dir.\nBuna göre, E noktasının O merkezine uzaklığı kaç cm’dir?',
 sekil=SK,dogru=Fr(15,2),yan=[(Fr(15,4),'Yol farkını ikiye, sonra uzaklığı bir kez daha ikiye bölmüş: 15 ÷ 4 = 3,75 cm.','islem'),(15,'Zaman farkındaki yol farkını (c × Δt = 15 cm) doğrudan uzaklık sanmış; yol farkının 2x olduğunu görmemiş.','bilgi'),(30,'Yol farkını iki katına çıkarmış: 2 × 15 = 30 cm.','islem'),(75,'Işık hızını 3 × 10⁹ m/s alarak hesaplamış.','islem')],
 istenen='E noktasının merkeze uzaklığı (cm).',
 ip=['İki fotonun aldığı yollar arasındaki farkı, E’nin merkezden kayma miktarıyla ilişkilendir.'],
 bilgi=[GRN],
 ad=[A('Yol farkı','Fotonlar ışık hızıyla gider; zaman farkı yol farkını verir.','Δs = c × Δt = 3 × 10⁸ × 0,5 × 10⁻⁹ = 0,15 m = 15 cm'),
     A('Geometri','E merkezden x kadar D₂ yönündeyse D₁’e olan yol D₂’ye olandan 2x fazladır.','Δs = (R + x) − (R − x) = 2x'),
     A('Uzaklık','Yol farkı iki x’e eşitlenir.','x = 15 ÷ 2 = 7,5 cm')],
 puf='PET’te iki foton zıt yöndedir: merkezden x kayma, yol farkında 2x olarak görünür.')
# ===== 13 orta · MR grafiği
gB=Fr(3,2); gf=63; k=Fr(gf)/gB; assert k==42 and 3*k==126 and Fr(126)/gf==2 and 126-gf==63 and 126*Fr(3,2)==189
gx=['\\begin{axis}[width=6.6cm,height=5.2cm,xmin=0,xmax=3.5,ymin=0,ymax=160,xtick distance=.5,ytick distance=20,grid=both,major grid style={gray!45,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$B$ (T)},ylabel={$f$ (MHz)},xlabel style={font=\\small},ylabel style={font=\\small}]',
 f'\\addplot[thick,vurgu] coordinates {{(0,0) (3.5,{float(k*Fr(7,2))})}};','\\addplot[only marks,mark=*,mark size=2pt] coordinates {(1.5,63)};','\\node[font=\\scriptsize,anchor=south east] at (axis cs:1.45,66) {K};','\\end{axis}']
SK=tikz(gx)
card(13,'MR’da rezonans frekansı','MR’da hidrojen çekirdeklerinin rezonans frekansı manyetik alanla doğru orantılıdır.','Orantıyı kurmadan oranı ya da farkı doğrudan cevap saymak.','orta','grafik',3,'te-goruntu','f–B grafiğinden alan bulma')
q('0013',tipId='te-goruntu',tip=TIPLER['te-goruntu'],z='orta',alt='MR',kaz='MR cihazında rezonans frekansı ile manyetik alanın doğru orantılı değişimini grafikten yorumlar.',kalip='grafik',
 metin='Bir MR cihazında hidrojen çekirdeklerinin rezonans frekansının, cihazın oluşturduğu manyetik alan şiddetiyle değişimi grafikte verilmiştir. Grafikteki K noktası, 1,5 T’lık alandaki ölçümü göstermektedir.\nBuna göre, rezonans frekansının 126 MHz olması için manyetik alan şiddeti kaç T olmalıdır?',
 sekil=SK,dogru=3,yan=[(2,'Frekansların oranını (126 ÷ 63 = 2) doğrudan alan şiddeti sanmış.','dikkat'),(63,'Frekanslar farkını (126 − 63 = 63) alan şiddeti olarak yazmış.','dikkat'),(126,'Frekansın sayısal değerini alan şiddeti olarak yazmış.','dikkat'),(189,'126 değerini 1,5 ile çarpmış; doğru orantı yerine ters işlem yapmış.','islem')],
 istenen='Rezonans için gerekli manyetik alan şiddeti (T).',
 ip=['Grafik doğrusal ve orijinden geçiyor; K noktasından f ÷ B oranını bul.'],
 bilgi=[GRN],
 ad=[A('Orantı sabiti','Doğru orijinden geçtiği için f ÷ B sabittir.','f ÷ B = 63 ÷ 1,5 = 42 MHz/T'),
     A('Alanı bul','İstenen frekansı sabite böl.','B = 126 ÷ 42'),
     A('Sonuç','Bölme yapılır.','B = 3 T')],
 puf='Orijinden geçen doğru grafiği doğru orantı demektir: bir noktadan sabit oranı bul, diğer değeri o oranla hesapla.')
# ===== 14 orta · Meissner öncüllü
o=['\\fill[gray!35] (-2.2,0) rectangle (2.2,.5); \\draw[thick] (-2.2,0) rectangle (2.2,.5);',N(0,.25,'süper iletken disk ($T<T_c$)','font=\\scriptsize')]
for rx in (1.3,1.9): o.append(f'\\draw[vurgu] (0,1.55) ellipse ({rx} and .85);')
o.append('\\draw[thick,fill=white] (-.6,1.3) rectangle (0,1.8); \\draw[thick,fill=gray!20] (0,1.3) rectangle (.6,1.8);'); o.append(N(-.3,1.55,'N','font=\\scriptsize')); o.append(N(.3,1.55,'S','font=\\scriptsize'))
o.append(N(2.3,1.55,'mıknatıs','right,font=\\scriptsize')); o.append(N(0,-.4,'sıvı azotla soğutulmuş','font=\\scriptsize'))
SK=tikz(o)
card(14,'Süper iletken üzerinde mıknatıs','Süper iletken manyetik alan çizgilerini içine almaz; mıknatıs ile disk arasındaki kuvvet itmedir ve T_c altında direnç sıfırdır.','Kuvvetin çekim olduğunu sanmak; Meissner olayını dirençle karıştırmak.','orta','öncüllü',3,'te-super','mıknatısın süper iletken diskte havada kalması')
q('0014',tipId='te-super',tip=TIPLER['te-super'],z='orta',alt='Süper İletkenlik',kaz='Süper iletken üzerinde mıknatısın havada kalmasını Meissner olayı ve sıfır direnç ile açıklar.',kalip='öncüllü',
 metin='Sıvı azotla kritik sıcaklığının altına soğutulmuş süper iletken bir diskin üzerine küçük bir mıknatıs bırakıldığında mıknatıs, şekildeki gibi disk ile temas etmeden havada durmaktadır.\nBuna göre,\nI. Disk ile mıknatıs arasındaki kuvvet çekim kuvvetidir.\nII. Mıknatısın manyetik alan çizgileri disk içine girmez.\nIII. Diskin elektrik direnci sıfırdır.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Mıknatısın havada kalabilmesi için diskin ona uyguladığı kuvvetin yönünü ve diskin kritik sıcaklığın altındaki özelliklerini düşün.'],
 bilgi=[SP],
 ad=[A('I. yargı','Mıknatıs havada kaldığına göre disk onu ağırlığına zıt yönde, yani yukarı doğru iter.','itme → I yanlış'),
     A('II. yargı','Süper iletken alan çizgilerini içine almaz (Meissner olayı).','II doğru'),
     A('III. yargı','Kritik sıcaklığın altında direnç sıfırdır.','III doğru')],
 puf='Süper iletken = sıfır direnç + alanı dışlama; mıknatıs bu yüzden itilir ve havada durur.',
 **onc([False,True,True],['disk mıknatısı itmektedir; kuvvet çekim kuvveti değildir','alan çizgileri süper iletken içine girmez','kritik sıcaklığın altında direnç sıfırdır'],4))
# ===== 15 zor · nano küp
Lc=10**-2; ac=10*10**-9
assert Fr(1,100)/Fr(10,10**9)==10**6 and (10**6)**3==10**18
assert Fr(10**7)/Fr(10,1)==10**6 and Fr(10**7)/1==10**7 and Fr(10**9)/10==10**8 and (10**6)**2==10**12
def cube(x,y,a,lab,lab2):
    d=.45*a; r=[f'\\draw[thick,fill=gray!15] ({x},{y}) rectangle ({x+a},{y+a});',f'\\draw[thick] ({x},{y+a}) -- ({x+d},{y+a+d}) -- ({x+a+d},{y+a+d}) -- ({x+a+d},{y+d}) -- ({x+a},{y});',f'\\draw[thick] ({x+a},{y+a}) -- ({x+a+d},{y+a+d});',
       N(x+a/2,y+a/2,lab,'font=\\small\\bfseries'),N(x+a/2,y-.3,lab2,'font=\\scriptsize')]
    return r
SK=tikz(cube(0,0,1.8,'K','kenar: 1 cm')+cube(4.2,0,.55,'L','kenar: 10 nm')+[N(3.55,.9,'$\\Rightarrow$','font=\\large'),N(5.3,1.35,'özdeş L küpleri','font=\\scriptsize')])
card(15,'Nano ölçekte yüzey alanı artışı','Hacim sabit tutulup kenar a’ya düşürülürse toplam yüzey alanı L ÷ a kat artar (6L³ ÷ a).','Birim dönüşümü hatası; alan oranı, küp sayısı ya da kenar oranını birbirine karıştırmak.','zor','şekilli',5,'te-nano','küpün nano küplere bölünmesinde yüzey alanı')
q('0015',tipId='te-nano',tip=TIPLER['te-nano'],z='zor',alt='Nanoteknoloji',kaz='Madde nano boyuta küçüldüğünde toplam yüzey alanının nasıl arttığını hesaplar.',kalip='şekilli',
 metin='Bir araştırmacı, kenarı 1 cm olan bir K küpünü, toplam hacmi değişmeyecek biçimde kenarı 10 nm olan özdeş L küplerine ayırıyor. Ayırma sırasında madde kaybı olmuyor; ayrılmış küplerin hepsinin yüzeyi açıktır. 1 cm = 10⁷ nm’dir.\nBuna göre, tüm L küplerinin toplam yüzey alanı K küpünün yüzey alanının kaç katıdır?',
 sekil=SK,dogru='10⁶',yan=[('10⁷','10 nm’yi 1 nm almış: 10⁷ ÷ 1 = 10⁷.','islem'),('10⁸','1 cm’yi 10⁹ nm sanmış: 10⁹ ÷ 10 = 10⁸.','islem'),('10¹²','Yüzey alanı oranını kenar oranının karesi (10⁶)² olarak yazmış.','bilgi'),('10¹⁸','L küplerinin sayısını (10⁶)³ = 10¹⁸ bulup bunu yüzey alanı oranı sanmış.','bilgi')],
 sira=['10⁶','10⁷','10⁸','10¹²','10¹⁸'],
 istenen='Toplam yüzey alanının kaç kat arttığı.',
 ip=['Küçük küplerin sayısını hacim eşitliğinden bul; her birinin yüzey alanını da yazıp toplam alanı K’ninkiyle karşılaştır.'],
 bilgi=[NN],
 ad=[A('Kenar oranı','1 cm = 10⁷ nm olduğundan kenar oranı bulunur.','L_K ÷ a = 10⁷ ÷ 10 = 10⁶'),
     A('Küp sayısı','Hacim eşitliği: n × a³ = L_K³.','n = (10⁶)³ = 10¹⁸'),
     A('Toplam alan','Her küçük küpün alanı 6a²’dir.','A_toplam = 10¹⁸ × 6a²'),
     A('Oran','K’nin alanı 6L_K²’dir.','A_toplam ÷ A_K = 10¹⁸ × (a ÷ L_K)² = 10¹⁸ × 10⁻¹² = 10⁶')],
 puf='Hacim sabitken kenar kaç kat küçülürse toplam yüzey alanı o kadar kat büyür.')
# ===== 16 orta · lazer düzeneği
o=['\\draw[thick,fill=gray!15] (1,0) rectangle (4,1.2);',N(2.5,.6,'aktif ortam','font=\\scriptsize'),'\\draw[line width=3pt] (.9,-.2) -- (.9,1.4);','\\draw[line width=3pt,gray] (4.1,-.2) -- (4.1,1.4);',
   N(.9,1.7,'M$_1$'),N(4.1,1.7,'M$_2$')]
o+=[AR((1.8,2.2),(1.8,1.3),'thick'),AR((3.2,2.2),(3.2,1.3),'thick'),N(2.5,2.45,'pompa (enerji kaynağı)','font=\\scriptsize'),AR((4.3,.6),(5.6,.6),'very thick,vurgu'),N(5.0,.95,'lazer demeti','font=\\scriptsize')]
SK=tikz(o)
card(16,'Lazer düzeneğinde ışığın kuvvetlenmesi','Pompa atomları uyarır; aynalar arasında gidip gelen fotonlar uyarılmış emisyonu tetikleyerek ışığı kuvvetlendirir.','Pompanın atomları taban düzeye indirdiğini ya da lazerin kendiliğinden yayılmayla oluştuğunu sanmak.','orta','şekilli',3,'te-lazer','lazer düzeneğinin çalışma ilkesi')
dg='Aynalar arasında gidip gelen fotonlar, uyarılmış atomların aynı özellikte foton yaymasını sağlar ve ışık şiddeti artar.'
q('0016',tipId='te-lazer',tip=TIPLER['te-lazer'],z='orta',alt='Lazer',kaz='Lazer düzeneğinin bölümlerinin işlevini ve ışığın kuvvetlenmesini açıklar.',kalip='şekilli',
 metin='Şekildeki basit lazer düzeneğinde aktif ortam, iki ayna arasına yerleştirilmiştir. M₁ aynası ışığın tamamını yansıtırken M₂ aynası ışığın bir bölümünü geçirir; pompa ise ortamdaki atomlara dışarıdan enerji verir.\nBuna göre, düzeneğin çalışmasıyla ilgili aşağıdakilerden hangisi doğrudur?',
 sekil=SK,dogru=dg,yan=[('Pompa, atomları taban düzeye indirerek foton yayılmasını sağlar.','Pompanın atomları taban düzeye indirdiğini sanmış; oysa pompa atomları uyarılmış düzeye çıkarır.','bilgi'),
  ('Işığın dalga boyu aynalardan her yansımada artarak demet kuvvetlenir.','Kuvvetlenmeyi dalga boyunun artışına bağlamış; oysa dalga boyu değişmez, foton sayısı artar.','bilgi'),
  ('Demetteki fotonların fazları rastgeledir ve demet geniş açıyla dağılır.','Lazer ışığını sıradan ışığa benzetmiş; oysa fotonlar aynı fazlı ve aynı doğrultudadır.','bilgi'),
  ('Lazer ışığı, atomların kendiliğinden yayınlamasıyla oluşur.','Kendiliğinden yayınlamayı lazerin oluşum yolu sanmış; oysa lazer uyarılmış emisyonla oluşur.','bilgi')],
 sira=['Pompa, atomları taban düzeye indirerek foton yayılmasını sağlar.','Işığın dalga boyu aynalardan her yansımada artarak demet kuvvetlenir.','Demetteki fotonların fazları rastgeledir ve demet geniş açıyla dağılır.',dg,'Lazer ışığı, atomların kendiliğinden yayınlamasıyla oluşur.'],
 istenen='Lazer düzeneği için doğru ifade.',
 ip=['Her seçenekte pompanın, aynaların ve uyarılmış emisyonun görevini ayrı ayrı sına.'],
 bilgi=[LZ],
 ad=[A('Pompa','Pompa atomları uyarılmış düzeye çıkarır.','taban düzey → uyarılmış düzey'),
     A('Aynalar','Fotonlar aktif ortamdan defalarca geçer ve uyarılmış emisyonu tetikler.','foton sayısı artar, dalga boyu değişmez'),
     A('Seçenekler','Çıkan demet eş fazlı ve paraleldir; yalnız bir ifade bu işleyişe uyar.','Doğru ifade: gidip gelen fotonlar uyarılmış emisyonla ışığı kuvvetlendirir')],
 puf='Lazerde pompa uyarır, aynalar geri besleme yapar, uyarılmış emisyon ışığı kuvvetlendirir.')
# ===== 17 orta · yarı iletken öncüllü
card(17,'Katkılı yarı iletkenler','Beş değerlik elektronlu katkı n tipi, üç değerlik elektronlu katkı p tipi verir; yarı iletkende sıcaklık artınca direnç azalır.','p tipinde çoğunluk taşıyıcıyı elektron sanmak.','orta','öncüllü',3,'te-yari','n/p tipi ve sıcaklık etkisi yargıları')
q('0017',tipId='te-yari',tip=TIPLER['te-yari'],z='orta',alt='Yarı İletkenler',kaz='Katkılı yarı iletkenlerin türlerini ve yarı iletkende direncin sıcaklıkla değişimini yargılar.',kalip='öncüllü',
 metin='Bir öğrenci, silisyum kristaline katkı atomları ekleyerek yarı iletken malzemeleri inceliyor ve saf silisyumun sıcaklıkla elektriksel davranışını gözlemliyor.\nBuna göre,\nI. Silisyuma beş değerlik elektronlu bir atom katkılanırsa n tipi yarı iletken oluşur.\nII. p tipi yarı iletkende çoğunluk yük taşıyıcıları serbest elektronlardır.\nIII. Saf silisyumun sıcaklığı artırılırsa direnci azalır.\nyargılarından hangileri doğrudur?',
 sekil=None,istenen='Doğru yargılar.',
 ip=['Katkı atomunun değerlik elektronu sayısının kristale ne kazandırdığını ve sıcaklığın serbest yük sayısını nasıl etkilediğini düşün.'],
 bilgi=[YI],
 ad=[A('I. yargı','Beş değerlik elektronlu atomun fazla elektronu serbest kalır.','n tipi → I doğru'),
     A('II. yargı','p tipinde üç değerlik elektronlu katkı deşik oluşturur; çoğunluk taşıyıcı deşiklerdir.','II yanlış'),
     A('III. yargı','Sıcaklık artınca serbest yük sayısı artar, direnç azalır.','III doğru')],
 puf='n tipi: fazla elektron; p tipi: fazla deşik; yarı iletkenin direnci ısındıkça azalır.',
 **onc([True,False,True],['beş değerlik elektronlu katkı serbest elektron fazlalığı oluşturur','p tipinde çoğunluk yük taşıyıcıları serbest elektronlar değil deşiklerdir','sıcaklık artınca serbest yük sayısı artar ve direnç azalır'],3))
# ===== 18 zor · lazer foton sayısı
eV=Fr(16,10)*Fr(1,10**19); Eph=2*eV; Pw=Fr(32,10)*Fr(1,1000)
Nph=Pw/Eph
assert lam(2)==620 and Nph==10**16 and Pw*1000/Eph==10**19 and Pw/1000/Eph==10**13 and Pw/eV==2*10**16 and Pw/(4*eV)==5*10**15
card(18,'Lazerin birim zamandaki foton sayısı','N = P ÷ E_foton; foton enerjisi 1240 ÷ λ (eV) ile bulunup joule’e çevrilir.','mW–W dönüşümünü ve eV–J dönüşümünü karıştırmak.','zor','düz',4,'te-lazer','lazer gücü ve foton sayısı')
q('0018',tipId='te-lazer',tip=TIPLER['te-lazer'],z='zor',alt='Lazer',kaz='Lazerin gücü ve dalga boyundan saniyede yaydığı foton sayısını hesaplar.',kalip='düz',
 metin='Dalga boyu 620 nm olan bir lazer işaretleyici, tek renkli ışığı 3,2 mW’lık sabit güçle yaymaktadır. Işığın tamamının lazer demeti olarak çıktığı kabul edilecektir. h × c = 1240 eV·nm ve 1 eV = 1,6 × 10⁻¹⁹ J’dir.\nBuna göre, lazerin 1 saniyede yaydığı foton sayısı kaçtır?',
 sekil=None,dogru='1 × 10¹⁶',yan=[('1 × 10¹³','Gücü 3,2 mW yerine 3,2 µW almış.','islem'),('5 × 10¹⁵','Foton enerjisini 4 eV bulmuş; dalga boyunu 310 nm gibi hesaba katmış.','islem'),('2 × 10¹⁶','Foton enerjisini 1 eV bulmuş.','islem'),('1 × 10¹⁹','Gücü 3,2 W almış; mW’ı W’a çevirmemiş.','islem')],
 sira=['1 × 10¹³','5 × 10¹⁵','1 × 10¹⁶','2 × 10¹⁶','1 × 10¹⁹'],
 istenen='Lazerin 1 saniyede yaydığı foton sayısı.',
 ip=['Bir fotonun enerjisini joule cinsinden bul; saniyedeki enerji ile karşılaştır.'],
 bilgi=[FE],
 ad=[A('Foton enerjisi','Verilen h × c çarpımı kullanılır.','E = 1240 ÷ 620 = 2 eV'),
     A('Joule’e çevir','1 eV = 1,6 × 10⁻¹⁹ J.','E = 3,2 × 10⁻¹⁹ J'),
     A('Güç','mW, W’a çevrilir.','P = 3,2 × 10⁻³ W = 3,2 × 10⁻³ J/s'),
     A('Foton sayısı','Saniyedeki enerji, foton enerjisine bölünür.','N = 3,2 × 10⁻³ ÷ 3,2 × 10⁻¹⁹ = 10¹⁶')],
 puf='Saniyedeki foton sayısı, ışınım gücünün bir fotonun enerjisine oranıdır; birimleri W ve J’de eşitle.')
# ===== 19 orta · güneş pili hücreleri
assert 6//Fr(1,2)==12 and Fr(4,2)==2 and 12*2==24 and 12+2==14 and 12*4==48
card(19,'Güneş pili hücrelerinin bağlanması','Gerilim için hücreler seri, akım için paralel kol eklenir; toplam hücre sayısı kol sayısı ile kol başına hücre sayısının çarpımıdır.','Yalnız gerilim ya da yalnız akım koşulunu düşünmek; sayıları toplamak.','orta','düz',4,'te-gunes','hücrelerden panel oluşturma')
q('0019',tipId='te-gunes',tip=TIPLER['te-gunes'],z='orta',alt='Güneş Pili',kaz='Özdeş güneş pili hücrelerini seri ve paralel bağlayarak istenen gerilim ve akımı sağlayan en az hücre sayısını bulur.',kalip='düz',
 metin='Her biri tam ışık altında 0,5 V gerilim ve en çok 2 A akım verebilen özdeş güneş pili hücreleri, bir panel oluşturmak için seri ve paralel bağlanacaktır. Panel, 6 V gerilimde 4 A akım çeken bir cihazı besleyecektir; hücrelerin iç dirençleri ve bağlantı kayıpları ihmal edilmektedir.\nBuna göre, panelde en az kaç hücre kullanılmalıdır?',
 sekil=None,dogru=24,yan=[(2,'Yalnızca akım koşulunu düşünüp 4 ÷ 2 = 2 hücre bulmuş.','dikkat'),(12,'Yalnızca gerilim koşulunu düşünüp 6 ÷ 0,5 = 12 hücre bulmuş.','dikkat'),(14,'Seri hücre sayısı ile paralel kol sayısını çarpmak yerine toplamış: 12 + 2 = 14.','islem'),(48,'Paralel kol sayısı olarak akım değerini (4) almış: 12 × 4 = 48.','islem')],
 istenen='Gerekli en az hücre sayısı.',
 ip=['Gerilimi sağlayan seri kolu ve akımı sağlamak için gereken kol sayısını ayrı ayrı bul.'],
 bilgi=[GP],
 ad=[A('Seri hücreler','Gerilimler seri bağlamada toplanır.','6 ÷ 0,5 = 12 hücre'),
     A('Paralel kollar','Akımlar paralel kollarda toplanır; her kol en çok 2 A verir.','4 ÷ 2 = 2 kol'),
     A('Toplam','Hücre sayısı kol sayısı ile kol başına hücre sayısının çarpımıdır.','12 × 2 = 24 hücre')],
 puf='Gerilim hücreleri seri ekleyerek, akım kolları paralel ekleyerek sağlanır; toplam sayı çarpımdır.')
# ===== 20 zor · süper iletken hat
Rkm=Fr(1,2); Lh=8; Rh=2*Lh*Rkm; Ih=100; Ph=Ih**2*Rh/1000; Eh=Ph*3
assert Rh==8 and Ph==80 and Eh==240 and Ih**2*Lh*Rkm/1000*3==120 and Ph==80 and Ih**2*Lh*Rkm/1000==40 and Ih**2*(2*Rh)/1000*3==480
card(20,'Süper iletken hatla önlenen kayıp','Joule kaybı P = i²R; gidiş–dönüş iki tel olduğundan toplam direnç iki katıdır; enerji = güç × süre.','Dönüş telini unutmak ya da süreyi katmadan kW’ı kWh yazmak.','zor','düz',5,'te-super','iletim hattında önlenen Joule kaybı')
q('0020',tipId='te-super',tip=TIPLER['te-super'],z='zor',alt='Süper İletkenlik',kaz='Süper iletken kablo kullanılınca önlenen Joule kaybını, hat direncinden ve süreden hesaplar.',kalip='düz',
 metin='Bir tesisi besleyen 8 km uzunluğundaki bakır hat, gidiş ve dönüş olmak üzere iki telden oluşmaktadır; her telin direnci kilometre başına 0,5 Ω’dur. Hattan 3 saat boyunca sabit 100 A akım geçmektedir. Bu hat, aynı akımı taşıyan ve kritik sıcaklığın altında tutulan süper iletken bir kabloyla değiştiriliyor.\nBuna göre, 3 saatte hatta ısıya dönüşen ve süper iletken kabloyla önlenen enerji kaç kWh’tir?',
 sekil=None,dogru=240,yan=[(40,'Yalnız gidiş telini (4 Ω) hesaba katıp süreyi hesaba katmamış: 40 kW.','dikkat'),(80,'Gücü doğru bulmuş (80 kW) ama süre ile çarpmayı unutmuş.','dikkat'),(120,'Yalnız gidiş telinin direncini (4 Ω) alıp süreyle çarpmış: 40 × 3 = 120 kWh.','dikkat'),(480,'Gidiş–dönüş direncini bir kez daha ikiye katlayarak 16 Ω almış: 160 kW × 3 = 480 kWh.','islem')],
 istenen='Önlenen enerji (kWh).',
 ip=['Akımın dolaştığı toplam tel uzunluğunu bul, ısıya dönüşen gücü hesapla, sonra süreyle ilişkilendir.'],
 bilgi=[SP],
 ad=[A('Toplam direnç','Akım gidiş ve dönüş tellerinden geçer.','R = 2 × 8 × 0,5 = 8 Ω'),
     A('Isıya dönüşen güç','Joule ısınması i²R ile bulunur.','P = 100² × 8 = 80 000 W = 80 kW'),
     A('Enerji','Enerji güç ile süre çarpımıdır.','E = 80 × 3 = 240 kWh'),
     A('Süper iletken kablo','Kritik sıcaklığın altında R = 0 olduğundan bu enerji kaybı olmaz.','Önlenen enerji = 240 kWh')],
 puf='Süper iletkende P = i²R = 0’dır; önlenen kayıp, eski hattın i²R × süre değeridir.')
# ===== yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/tekn'
P.yaz(os.path.join(GD,'teknoloji-1.json'),os.path.join(SC,'bos.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|'+KON))['kartlar'].append(c['id'])
json.dump(dict(konu=KON,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Fizik (yalnız mantık), 345 AYT Fizik, Bilgi Sarmal AYT Fizik, MEB 12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afteknoloji.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
