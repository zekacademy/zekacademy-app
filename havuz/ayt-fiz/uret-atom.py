"""AYT Fizik · Atom Modelleri · 20 soru (kardeş yok, ipucu 1). Şekil verileri ve her cevap/çeldirici Python'da hesaplanıp assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
KONUAD='Atom Modelleri'; KK='afiz|Atom Modelleri'
P=Parti('atom',KONUAD,KK,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONUAD
ALT='Atom Modelleri ve Enerji Düzeyleri'
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-AFATOM-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM AYT 2018–2026 Fizik (yalnız mantık) · 345 AYT Fizik SB · MEB 12. sınıf fizik')
def q(no,n,**k):
    assert len(k['ip'])==1 and 3<=len(k['ad'])<=7
    mk(P,str(no),adim=len(k['ad']),alt=ALT,kart=f'K-AFATOM-{n:02d}',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'; TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.2f},{y:.2f}) {{{t}}};'
def E(n,Z=1): return -Fr(68,5)*Z*Z/Fr(n*n)
ROM=('I','II','III')
def onc(truth,reasons,sira):
    def kume(l): return set(ROM) if l=='I, II ve III' else set(x for x in l.replace('Yalnız ','').replace(' ve ',' ').split())
    gercek={k for k,v in truth.items() if v}
    dog=[l for l in sira if kume(l)==gercek]; assert len(dog)==1,(sira,gercek)
    yan=[]
    for l in sira:
        if l==dog[0]: continue
        k=kume(l); c=[]
        for x in ROM:
            if x in k and x not in gercek: c.append(f'{x}. öncülü doğru saymıştır; oysa yanlıştır: {reasons[x]}')
            if x in gercek and x not in k: c.append(f'{x}. öncülünü yanlış saymıştır; oysa doğrudur: {reasons[x]}')
        yan.append((l,' '.join(c),'bilgi'))
    ad=[A(f'{x}. öncülü incele',reasons[x],f'{x}: '+('doğru' if truth[x] else 'yanlış')) for x in ROM]
    ad.append(A('Sonuca var','Doğru öncülleri birleştir.','Doğru: '+', '.join(x for x in ROM if truth[x])))
    return dog[0],yan,ad
S5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
# ---------- bilgi kutuları ----------
B_MOD=B('Üç atom modeli','Thomson: pozitif yük atom hacmine düzgün dağılmış kürenin içinde elektronlar gömülüdür. Rutherford: pozitif yük ve kütle küçük bir çekirdekte toplanmıştır, elektronlar çevresinde dolanır. Bohr: elektronlar yalnız belirli yörüngelerde bulunur ve bu yörüngelerde ışıma yapmaz; ışıma yörünge değiştirirken olur. Örnek: α saçılması deneyi çekirdeğin varlığını gösterir')
B_THO=B('Hız seçici','Elektrik ve manyetik alanın birlikte bulunduğu bölgede sapmadan geçen yüklü parçacıkta qE = qvB olduğundan v = E/B bulunur. Örnek: E = 800 V/m ve B = 0,4 T alanlarında sapmadan geçen parçacığın hızı 800 ÷ 0,4 = 2000 m/s olur')
B_RUT=B('En yakın yaklaşma','Çekirdeğe doğru gelen α parçacığı en yakın noktada durur; bu noktada kinetik enerji tamamen elektriksel potansiyel enerjiye dönüşmüştür: Ek = k·(2e)(Ze)/d. Örnek: ke² = 1,44 MeV·fm olmak üzere Z = 10 için, Ek = 2,88 MeV ise d = 2 × 10 × 1,44 ÷ 2,88 = 10 fm')
B_BOH=B('Bohr modelinde yörünge nicelikleri','Hidrojen atomunda n. yörüngenin yarıçapı r ∝ n², hızı v ∝ 1/n, kinetik enerjisi 13,6/n² eV, toplam enerjisi E = −13,6/n² eV, açısal momentumu L = n·h/2π ve dolanma periyodu T ∝ n³ olur. Örnek: n = 5 yörüngesinde toplam enerji −13,6 ÷ 25 = −0,544 eV')
B_SEV=B('Düzeyler arası geçiş','Elektron üst düzeyden alt düzeye inerken enerjileri farkı kadar foton yayımlar: hf = hc/λ = Eüst − Ealt. Fotonun enerjisi büyüdükçe dalga boyu küçülür. Örnek: −2 eV düzeyinden −7 eV düzeyine inişte 5 eV’luk foton yayımlanır')
B_UYA=B('Uyarılma ve iyonlaşma','Foton yalnız enerjisi iki düzey farkına tam eşitse soğurulur; elektron çarpışmasında ise enerjinin yalnız gereken kısmı aktarılabilir. İyonlaşma enerjisi, bulunulan düzeyin enerjisinin büyüklüğüdür; fazla enerji elektronun kinetik enerjisi olur. Örnek: −5 eV düzeyindeki elektrona 7 eV’luk foton gelirse elektron 2 eV kinetik enerjiyle kopar')
B_SPE=B('Çizgi spektrumu','Atomun yayımladığı her çizgi iki düzey arasındaki bir geçişe karşılık gelir; n. düzeyden başlayan atom topluluğunda n(n − 1)/2 farklı çizgi gözlenebilir. Hidrojende n = 1’e inişler Lyman (morötesi), n = 2’ye inişler Balmer (görünür), n = 3’e inişler Paschen (kızılötesi) serisidir. 1/λ ∝ ΔE ile birlikte hc = 1240 eV·nm’dir')
B_BEN=B('Hidrojen benzeri iyonlar','Tek elektronlu iyonlarda (He⁺, Li²⁺ …) yarıçap r = a₀n²/Z, hız v = v₁Z/n ve enerji E = −13,6Z²/n² eV bağıntılarıyla bulunur. Örnek: Z = 3, n = 1’de enerji −13,6 × 9 = −122,4 eV’tur')
# ================= KARTLAR =================
kartla(1,'Atom modellerinin karşılaştırılması','Thomson, Rutherford ve Bohr modellerinin kabulleri ve açıklayamadıkları: çekirdek, kararlılık, çizgi spektrumu.','Elektronların yörüngelerde dolanmasını Thomson’a, çok elektronlu atomun spektrumunu Bohr’a yüklemek.','kolay','öncüllü',3,'atom-model','Atom modellerinin karşılaştırılması')
kartla(2,'Thomson deneyi','Elektron ışınının elektrik ve manyetik alandaki dengesi qE = qvB ve v = E/B.','mT, μT gibi birimleri tesla’ya çevirmemek; E ile B’yi çarpmak.','orta','şekilli',3,'atom-thomson','Thomson deneyi ve hız seçici')
kartla(3,'Rutherford saçılması','α saçılmasından çekirdek sonucu; en yakın yaklaşmada Ek = k(2e)(Ze)/d.','α yükünü e almak; kinetik enerjiye bölmeyi unutmak; yük/kütle oranlarını karıştırmak.','zor','şekilli',4,'atom-rutherford','Rutherford saçılması ve çekirdek')
kartla(4,'Bohr yörünge nicelikleri','r ∝ n², v ∝ 1/n, T ∝ n³, Ek = 13,6/n², E = −13,6/n², L = nh/2π.','Toplam enerjinin işaretini ve kinetik enerjinin n ile azaldığını karıştırmak.','orta','öncüllü',4,'atom-bohr','Bohr modelinde yörünge nicelikleri')
kartla(5,'Enerji düzeyleri ve geçişler','Geçişte yayımlanan ya da soğurulan foton enerjisi düzeylerin farkıdır; dalga boyu enerjiyle ters orantılıdır.','Düzey enerjisini foton enerjisi sanmak; enerjileri toplamak; dalga boyunu enerjiyle doğru orantılı almak.','orta','şekilli',3,'atom-seviye','Enerji düzeyleri ve foton geçişleri')
kartla(6,'Uyarılma ve iyonlaşma','Foton için tam uyum, elektron çarpışması için eşik koşulu; iyonlaşmada fazla enerji kinetik enerji olur.','Fotonun enerjisinin bir kısmının soğurulabileceğini sanmak; iyonlaşma eşiğini temel haldeki değerle karıştırmak.','zor','şekilli',4,'atom-uyarma','Uyarılma ve iyonlaşma')
kartla(7,'Spektrum çizgileri ve seriler','Çizgi sayısı n(n − 1)/2; en kısa dalga boyu en büyük enerji farkı; seri sınırları.','Seri adlarını ve alt düzeyleri karıştırmak; enerji ile dalga boyunu doğru orantılı almak.','orta','grafik',3,'atom-spektrum','Spektrum çizgileri ve seriler')
kartla(8,'Hidrojen benzeri iyonlar','Z ile ölçekleme: r ∝ 1/Z, v ∝ Z, E ∝ Z²; Z ve n’yi birlikte yönetmek.','Z’yi hız ve yarıçap bağıntısında yanlış yere yazmak; Z² yerine Z almak.','zor','grafik',4,'atom-benzeri','Hidrojen benzeri iyonlar')
# ================= 01 · kolay · öncüllü · Thomson modeli =================
pos=[(-0.65,0.7),(0.55,0.75),(-0.2,-0.05),(0.75,-0.3),(-0.85,-0.55),(0.1,-0.85),(0.1,0.05),(-0.2,0.55)]
pos=[(-0.7,0.65),(0.6,0.7),(-0.1,0.0),(0.85,-0.25),(-0.8,-0.5),(0.2,-0.85),(-0.1,0.9)]
el=''.join(f'\\draw[thick,fill=white] ({x},{y}) circle (.14); '+N(x,y,'$-$','font=\\scriptsize') for x,y in pos)
sk=fig('\\draw[thick,fill=gray!14] (0,0) circle (1.4);',el,'\\draw[thick,fill=white] (2.4,0.1) circle (.14);',N(2.4,.1,'$-$','font=\\scriptsize'),N(2.65,.1,'elektron','right'))
tr={'I':True,'II':False,'III':False}
rs={'I':'Şekildeki modelde pozitif yük atomun bütün hacmine düzgün dağılmış bir küredir; elektronlar bu kürenin içine gömülüdür.','II':'Elektronların çekirdek etrafında yörüngelerde dolanması Rutherford ve Bohr modellerinin kabulüdür; şekildeki modelde çekirdek ve yörünge yoktur.','III':'Kütlenin merkezde küçük bir çekirdekte toplanması Rutherford saçılma deneyinden çıkan sonuçtur; şekildeki modelde böyle bir bölge yoktur.'}
d1,y1,ad1=onc(tr,rs,S5)
q('0001',1,z='kolay',kalip='öncüllü',tipId='atom-model',tip='Atom modellerinin karşılaştırılması',kaz='Şekli verilen atom modelinin kabullerini yorumlar.',
 metin='Şekilde, atomun yapısını açıklamak için ortaya atılan bir model gösterilmiştir.\nBuna göre, bu modelle ilgili;\nI. Atomun pozitif yükü atom hacmine düzgün dağılmıştır.\nII. Elektronlar, atomun merkezindeki çekirdeğin etrafında yörüngelerde dolanır.\nIII. Atomun kütlesinin büyük bölümü merkezde küçük bir hacimde toplanmıştır.\nyargılarından hangileri doğrudur?',
 dogru=d1,yan=y1,sira=S5,istenen='Modelle uyumlu yargılar.',ip=['Şekilde elektronların nerede bulunduğuna ve atom içinde ayrı bir merkez bölge çizilip çizilmediğine bak.'],bilgi=[B_MOD],ad=ad1,
 puf='Thomson modelinde çekirdek ve yörünge yoktur; elektronlar pozitif kürenin içindedir.',sekil=sk)
# ================= 02 · kolay · α saçılması =================
sk=fig('\\fill (0,0) circle (.1);',
 f'\\draw[thick,{ARR}] (-4,3.3) -- (4,3.3);',N(-4.3,3.3,'K','left'),
 f'\\draw[thick,vurgu,{ARR}] (-4,-1.0) .. controls (-.8,-1.0) and (1,-1.3) .. (3.6,-2.8);',N(-4.3,-1.0,'L','left'),
 f'\\draw[thick,{ARR}] (-4,.22) -- (-.55,.22) .. controls (-.2,.22) and (-.15,1.1) .. (-2.4,2.6);',N(-4.3,.22,'M','left'),
 N(0.25,-0.3,'atomun merkezi','font=\\footnotesize,anchor=north west'))
q('0002',3,z='kolay',kalip='şekilli',tipId='atom-rutherford',tip='Rutherford saçılması ve çekirdek',kaz='α saçılması gözleminden atomun yapısıyla ilgili sonuç çıkarır.',
 metin='İnce bir altın folyoya gönderilen α parçacıklarından üçünün, bir atomun merkezi yakınındaki yolları şekilde gösterilmiştir. Parçacıkların büyük çoğunluğu K’nin yolu gibi doğrultusundan sapmadan geçerken çok azı L’nin, çok az bir kısmı ise M’nin yolu gibi sapmaktadır.\nBuna göre, bu gözlemlere dayanarak atomla ilgili aşağıdakilerden hangisi söylenebilir?',
 dogru='Atomun büyük kısmı boşluktur; pozitif yük küçük bir merkezde toplanmıştır.',
 yan=[('Pozitif yük atomun bütün hacmine düzgün biçimde dağılmıştır.','Pozitif yükü atom hacmine düzgün dağıtmıştır; oysa böyle bir dağılımda α parçacıkları neredeyse hiç geri dönmezdi.','bilgi'),('Elektronlar yalnızca belirli enerjili yörüngelerde dolanabilir.','Saçılma gözlemini Bohr’un yörünge kabulüyle karıştırmıştır; gözlem enerji düzeyleriyle ilgili bir bilgi vermez.','bilgi'),('Elektronlar α parçacıklarını geri döndürecek kadar ağırdır.','Geri dönmeyi elektronlara bağlamıştır; elektron kütlesi α parçacığınınkinden çok küçüktür, geri döndüremez.','bilgi'),('Atomun kütlesi merkez ile elektronlar arasında eşit paylaşılmıştır.','Kütlenin dağılımı hakkında gözlemden dayanaksız bir sonuç çıkarmıştır; kütlenin büyük bölümü merkezdedir.','bilgi')],
 sira=['Atomun büyük kısmı boşluktur; pozitif yük küçük bir merkezde toplanmıştır.','Pozitif yük atomun bütün hacmine düzgün biçimde dağılmıştır.','Elektronlar yalnızca belirli enerjili yörüngelerde dolanabilir.','Elektronlar α parçacıklarını geri döndürecek kadar ağırdır.','Atomun kütlesi merkez ile elektronlar arasında eşit paylaşılmıştır.'],
 istenen='Gözlemin atom yapısı hakkında verdiği sonuç.',ip=['Çoğu parçacığın sapmadan geçmesinin ve çok azının geri dönmesinin, pozitif yükün atom içindeki dağılımı hakkında ne anlattığını düşün.'],bilgi=[B_MOD],
 ad=[A('Gözlemi ayır','Çoğu parçacık sapmadan geçiyor, çok azı büyük açıyla sapıyor.','K: sapmaz · L: az sapar · M: geri döner'),A('Sapmasızlığı yorumla','Parçacıkların çoğu engelsiz geçtiğinden atomun büyük bölümü boş olmalıdır.','Büyük bölüm boş'),A('Geri dönmeyi yorumla','Geri dönme, parçacığı güçlü biçimde iten küçük ve yoğun pozitif yüklü bir merkez gerektirir.','Küçük, yoğun, pozitif merkez'),A('Sonuca var','İki gözlem birlikte Rutherford’un çekirdekli atom modelini verir.','Doğru: büyük kısmı boş, pozitif yük küçük merkezde')],
 puf='Sapmayan çoğunluk boşluğu, geri dönen azınlık yoğun çekirdeği gösterir.',sekil=sk)
# ================= 03 · kolay · enerji düzeyleri =================
yy={1:0,2:2.2,3:3.3,4:3.9}; yinf=4.6
EL={1:'-13{,}6',2:'-3{,}4',3:'-1{,}51',4:'-0{,}85'}
lev=''.join(f'\\draw[thick] (0,{yy[n]}) -- (3.2,{yy[n]}); '+N(-.1,yy[n],f'$n={n}$','left')+N(3.3,yy[n],'$'+EL[n]+'$ eV','right') for n in (1,2,3,4))
sk=fig(lev,f'\\draw[thick,dashed] (0,{yinf}) -- (3.2,{yinf}); '+N(-.1,yinf,'$n=\\infty$','left')+N(3.3,yinf,'$0$','right'),
 f'\\draw[very thick,vurgu,{ARR}] (1.6,{yy[2]}) -- (1.6,.05);')
assert E(2)-E(1)==Fr(51,5)
q('0003',5,z='kolay',kalip='şekilli',tipId='atom-seviye',tip='Enerji düzeyleri ve foton geçişleri',kaz='Düzeyler arası geçişte yayımlanan fotonun enerjisini hesaplar.',
 metin='Şekilde, Bohr atom modeline göre hidrojen atomunun bazı enerji düzeyleri gösterilmiştir (düzeyler ölçekli değildir). Şekildeki ok, elektronun yaptığı geçişi göstermektedir.\nBuna göre, bu geçiş sırasında atomun yayımladığı fotonun enerjisi kaç eV’tur?',
 dogru=Fr(51,5),yan=[(Fr(68,5),'Fotonun enerjisini temel düzeyin enerjisinin büyüklüğü olan 13,6 eV almıştır.','dikkat'),(Fr(17,5),'Fotonun enerjisini başlangıç düzeyinin enerjisinin büyüklüğü olan 3,4 eV almıştır.','dikkat'),(Fr(17),'İki düzeyin enerjilerinin büyüklüklerini toplamıştır: 13,6 + 3,4 = 17 eV.','islem'),(Fr(51,4),'4. düzeyden 1. düzeye inişin enerjisini (−0,85 − (−13,6) = 12,75 eV) hesaplamıştır; oku yanlış okumuştur.','dikkat')],
 istenen='Yayımlanan fotonun enerjisi (eV).',ip=['Okun hangi düzeyden hangisine doğru olduğunu belirle; foton enerjisini düzey enerjilerinin farkı olarak düşün.'],bilgi=[B_SEV],
 ad=[A('Geçişi oku','Ok 2. düzeyden 1. düzeye doğrudur; elektron alt düzeye iner ve foton yayımlar.','n = 2 → n = 1'),A('Düzey enerjilerini yaz','Şekilden iki düzeyin enerjilerini oku.','E₂ = −3,4 eV · E₁ = −13,6 eV'),A('Farkı hesapla','Foton enerjisi üst düzey ile alt düzey enerjilerinin farkıdır.','E = −3,4 − (−13,6) = 10,2 eV')],
 puf='Yayımlanan foton enerjisi iki düzeyin enerji farkına eşittir; iki enerjiyi toplama.',sekil=sk)
# ================= 04 · orta · yaklaşma uzaklığı =================
Zc,Ek4=20,Fr(24,5); kC=Fr(144,100)
d4=2*Zc*kC/Ek4
assert d4==12 and Zc*kC/Ek4==6 and 4*Zc*kC/Ek4==24 and 2*Zc*kC==Fr(288,5) and Zc*kC==Fr(144,5)
sk=fig('\\fill[vurgu!45!black] (3.6,0) circle (.28);',N(3.6,-.62,'$Z=20$',''),f'\\draw[thick,{ARR}] (0,0) -- (2.4,0);',N(0.5,.45,'$\\alpha$'),N(1.9,.5,'$E_k=4{,}8$ MeV',''))
q('0004',3,z='orta',kalip='şekilli',tipId='atom-rutherford',tip='Rutherford saçılması ve çekirdek',kaz='α parçacığının çekirdeğe en yakın yaklaşma uzaklığını hesaplar.',
 metin='Kinetik enerjisi şekilde verilen bir α parçacığı, atom numarası şekilde verilen hareketsiz bir çekirdeğin merkezine doğru doğrusal yörüngede gönderiliyor. Parçacık, çekirdeğe yaklaşırken yalnızca elektriksel itme kuvvetinin etkisinde kalıyor ve çekirdeğe en yakın noktada anlık olarak duruyor.\nke² = 1,44 MeV·fm olduğuna göre (1 fm = 10⁻¹⁵ m), parçacığın çekirdeğe en yakın olduğu uzaklık kaç fm’dir?',
 dogru=d4,yan=[(Zc*kC/Ek4,'α parçacığının yükünü 2e yerine e almıştır: 20 × 1,44 ÷ 4,8 = 6 fm.','bilgi'),(4*Zc*kC/Ek4,'Yük çarpımına bir kez daha 2 katmıştır: 4 × 20 × 1,44 ÷ 4,8 = 24 fm.','islem'),(Zc*kC,'α yükünü e almış ve kinetik enerjiye bölmeyi unutmuştur: 20 × 1,44 = 28,8 fm.','islem'),(2*Zc*kC,'Kinetik enerjiye bölmeyi unutmuştur: 2 × 20 × 1,44 = 57,6 fm.','islem')],
 istenen='Parçacığın çekirdeğe en yakın uzaklığı (fm).',ip=['En yakın noktada parçacığın kinetik enerjisinin ne olduğunu düşün ve enerjinin korunumunu yaz.'],bilgi=[B_RUT],
 ad=[A('Enerji korunumunu kur','En yakın noktada parçacık durur; bütün kinetik enerji elektriksel potansiyel enerjiye dönüşür.','Ek = k·(2e)(Ze)/d'),A('Yükleri belirle','α parçacığının yükü 2e, çekirdeğin yükü Ze’dir.','q₁q₂ = 2Z·e² = 40e²'),A('d’yi çek','ke² değerini kullanarak d’yi yalnız bırak.','d = 40 × 1,44 ÷ 4,8'),A('Hesapla','Sayıları işleme koy.','d = 57,6 ÷ 4,8 = 12 fm')],
 puf='En yakın yaklaşmada Ek = k·q₁q₂/d; α yükü 2e’dir.',sekil=sk)
# ================= 05 · orta · öncüllü · Bohr yörüngeleri =================
orb=''.join(f'\\draw[thick] (0,0) circle ({.3*n*n}); '+N(.3*n*n*0.7071+.1,.3*n*n*0.7071+.1,f'$n={n}$','font=\\footnotesize,anchor=south west') for n in (1,2,3))
orb+='\\draw[thick,fill=gray!40] (0,0) circle (.12); '+N(0,0,'$+$','font=\\tiny')
orb+=''.join(f'\\fill[vurgu!70!black] ({.3*n*n*c:.2f},{.3*n*n*s:.2f}) circle (.09);' for n,(c,s) in zip((1,2,3),[(-.7071,-.7071),(-.7071,.7071),(.9,-.4359)]))
sk=fig(orb)
assert Fr(27,8)==Fr(3**3,2**3) and Fr(2,3)==Fr(1,3)/Fr(1,2) and E(3)>E(2) and 1/Fr(9)<1/Fr(4)
tr={'I':False,'II':True,'III':True}
rs={'I':'Kinetik enerji 13,6/n² ile değiştiğinden n = 2’den n = 3’e çıkarken 3,4 eV’tan yaklaşık 1,51 eV’a düşer, yani azalır.','II':'T ∝ n³ olduğundan dolanma periyodu (3/2)³ = 27/8 katına çıkar, yani artar.','III':'Toplam enerji −13,6/n² olduğundan −3,4 eV’tan −1,51 eV’a çıkar, yani artar.'}
d5,y5,ad5=onc(tr,rs,S5)
q('0005',4,z='orta',kalip='öncüllü',tipId='atom-bohr',tip='Bohr modelinde yörünge nicelikleri',kaz='Bohr modelinde yörünge değişiminde nicelikler arasındaki değişimi yorumlar.',
 metin='Şekilde, Bohr atom modeline göre hidrojen atomunun ilk üç yörüngesi ve bu yörüngelerdeki elektronun konumu gösterilmiştir. Atomun elektronu, bir foton soğurarak 2. yörüngeden 3. yörüngeye çıkıyor.\nBuna göre, bu olay sırasında;\nI. elektronun kinetik enerjisi artar.\nII. elektronun yörüngedeki dolanma periyodu artar.\nIII. atomun toplam enerjisi artar.\nyargılarından hangileri doğrudur?',
 dogru=d5,yan=y5,sira=S5,istenen='Doğru olan yargılar.',ip=['Elektronun hızının ve toplam enerjisinin yörünge numarasıyla nasıl değiştiğini ayrı ayrı düşün.'],bilgi=[B_BOH],ad=ad5,
 puf='Dış yörüngede hız ve kinetik enerji azalır, periyot ve toplam enerji artar.',sekil=sk)
# ================= 06 · orta · dalga boyu sıralaması =================
sc=.22; ye={1:0,2:12*sc,3:15*sc}
lev=''.join(f'\\draw[thick] (0,{ye[n]}) -- (4.6,{ye[n]}); '+N(-.1,ye[n],f'$n={n}$','left')+N(4.7,ye[n],'$'+('-' if True else '')+str(abs(v))+'$ eV','right') for n,v in ((1,18),(2,6),(3,3)))
sk=fig(lev,
 f'\\draw[very thick,{ARR}] (1.0,{ye[3]}) -- (1.0,.05);'+N(1.0,-.35,'K',''),
 f'\\draw[very thick,{ARR}] (2.3,{ye[2]}) -- (2.3,.05);'+N(2.3,-.35,'L',''),
 f'\\draw[very thick,{ARR}] (3.6,{ye[3]}) -- (3.6,{ye[2]+.05});'+N(3.6,ye[2]-.3,'M',''))
gK,gL,gM=Fr(-3)-Fr(-18),Fr(-6)-Fr(-18),Fr(-3)-Fr(-6)
assert (gK,gL,gM)==(15,12,3)
q('0006',5,z='orta',kalip='şekilli',tipId='atom-seviye',tip='Enerji düzeyleri ve foton geçişleri',kaz='Düzeyler arası geçişlerde yayımlanan fotonların dalga boylarını karşılaştırır.',
 metin='Şekilde, üç enerji düzeyi gösterilen bir atomda elektronun yaptığı K, L ve M geçişleri okla gösterilmiştir. Bu geçişlerde yayımlanan fotonların dalga boyları sırasıyla λ_K, λ_L ve λ_M’dir (düzeyler ölçekli çizilmemiştir).\nBuna göre, λ_K, λ_L ve λ_M arasındaki ilişki aşağıdakilerden hangisidir?',
 dogru='λ_M > λ_L > λ_K',yan=[('λ_K > λ_L > λ_M','Dalga boyunu enerji farkıyla doğru orantılı almıştır; enerji farkı büyük olan geçişin dalga boyu küçüktür.','bilgi'),('λ_L > λ_K > λ_M','Dalga boylarını geçişin başladığı düzeyin sırasına göre dizmiştir; foton yalnız enerji farkına bağlıdır.','dikkat'),('λ_K > λ_M > λ_L','Geçişleri kendi aralarında karıştırmış, M geçişinin enerji farkını L’ninkinden büyük sanmıştır.','dikkat'),('λ_L > λ_M > λ_K','L geçişinin enerji farkını (12 eV) en küçük sanmıştır; en küçük fark M’ninki olan 3 eV’tur.','islem')],
 sira=['λ_K > λ_L > λ_M','λ_L > λ_K > λ_M','λ_K > λ_M > λ_L','λ_L > λ_M > λ_K','λ_M > λ_L > λ_K'],
 istenen='Dalga boyları arasındaki sıralama.',ip=['Her okun başladığı ve bittiği düzeylerin enerjilerinden foton enerjisini bul; sonra dalga boyunun enerjiyle ilişkisini düşün.'],bilgi=[B_SEV],
 ad=[A('Enerji farklarını bul','Her geçişte foton enerjisi iki düzeyin enerji farkıdır.','K: −3 − (−18) = 15 eV · L: −6 − (−18) = 12 eV · M: −3 − (−6) = 3 eV'),A('Enerjileri sırala','Enerjiler arasındaki sıra:','E_K > E_L > E_M'),A('Dalga boyuna geç','Dalga boyu foton enerjisiyle ters orantılıdır (λ = hc/E).','Enerji büyük → dalga boyu küçük'),A('Sonuç','Sıralamayı ters çevir.','λ_M > λ_L > λ_K')],
 puf='Dalga boyu ile foton enerjisi ters orantılıdır; en büyük enerji farkı en kısa dalga boyunu verir.',sekil=sk)
# ================= 07 · zor · tablo · dalga boyu oranı =================
LV={1:Fr(-13),2:Fr(-5),3:Fr(-5,2),4:Fr(-1)}
gaps=[LV[j]-LV[i] for i in LV for j in LV if j>i]; assert len(gaps)==6
r7=max(gaps)/min(gaps); assert r7==8 and max(gaps)==12 and min(gaps)==Fr(3,2)
assert (LV[2]-LV[1])/(LV[3]-LV[2])==Fr(16,5) and max(gaps)/(LV[4]-LV[2])==3 and max(gaps)/(LV[3]-LV[2])==Fr(24,5) and max(gaps)/(-LV[4])==12
sk=tablo_svg(['Düzey (n)','Enerji (eV)'],[[str(n),fm(v)] for n,v in LV.items()])
q('0007',5,z='zor',kalip='tablo',tipId='atom-seviye',tip='Enerji düzeyleri ve foton geçişleri',kaz='Çok düzeyli bir atomda yayımlanabilecek en uzun ve en kısa dalga boylu ışımaların oranını bulur.',
 metin='Bir atomun ilk dört enerji düzeyi aşağıdaki tabloda verilmiştir. 4. düzeye uyarılmış çok sayıda atomdan oluşan bir gazda elektronlar, her seferinde bir alt düzeye ya da daha alt bir düzeye inerek foton yayımlıyor; bütün olası geçişler gerçekleşiyor.\nBuna göre, yayımlanan fotonlar arasında en büyük dalga boylunun, en küçük dalga boylunun kaç katı olduğu kaçtır?',
 dogru=r7,yan=[(3,'En uzun dalga boylu ışımayı 4 → 2 geçişi (4 eV) sanmıştır: 12 ÷ 4 = 3.','dikkat'),(Fr(16,5),'En kısa dalga boyunu 2 → 1 (8 eV), en uzununu 3 → 2 (2,5 eV) sanmış, 4. düzeyi hesaba katmamıştır: 8 ÷ 2,5 = 3,2.','dikkat'),(Fr(24,5),'En uzun dalga boylu ışımayı 3 → 2 geçişi (2,5 eV) sanmıştır: 12 ÷ 2,5 = 4,8.','dikkat'),(12,'En küçük enerji farkı yerine 4. düzeyin enerjisinin büyüklüğünü (1 eV) almıştır: 12 ÷ 1 = 12.','dikkat')],
 istenen='En büyük dalga boyunun en küçük dalga boyuna oranı.',ip=['Dalga boyu en büyük ve en küçük olan ışımalar, enerji farkı sırasıyla en küçük ve en büyük olan geçişlerdir; tüm olası geçişlerin farklarını karşılaştır.'],bilgi=[B_SEV,B_SPE],
 ad=[A('Geçişleri listele','4. düzeyden başlayan gazda toplam 4·3/2 = 6 farklı geçiş vardır.','4→3, 4→2, 4→1, 3→2, 3→1, 2→1'),A('Enerji farklarını bul','Tablodaki değerlerin farklarını hesapla.','4→3: 1,5 · 3→2: 2,5 · 4→2: 4 · 2→1: 8 · 3→1: 10,5 · 4→1: 12 eV'),A('Uçları seç','En büyük enerji farkı en küçük dalga boyunu, en küçük fark en büyük dalga boyunu verir.','ΔE_büyük = 12 eV (4→1) · ΔE_küçük = 1,5 eV (4→3)'),A('Oranla','λ ∝ 1/ΔE olduğundan oran enerji oranının tersidir.','λ_büyük ÷ λ_küçük = 12 ÷ 1,5 = 8')],
 puf='Dalga boyu oranı, ters enerji oranıdır; en uç farkları bulmak için tüm geçişleri tara.',sekil=sk)
# ================= 08 · orta · öncüllü · fotonlar tablo =================
fot={'I':Fr(51,5),'II':Fr(11),'III':Fr(51,4)}
def soğur(e):
    t=E(1)+e
    return any(E(n)==t for n in range(2,60))
assert soğur(fot['I']) and not soğur(fot['II']) and soğur(fot['III'])
sk=tablo_svg(['Foton','Enerji (eV)'],[[k,fm(v)] for k,v in fot.items()])
tr={'I':True,'II':False,'III':True}
rs={'I':'10,2 eV, n = 1 ile n = 2 düzeyleri arasındaki farka (−3,4 − (−13,6)) eşittir; bu foton soğurulur.','II':'11 eV hiçbir düzey farkına eşit değildir: −13,6 + 11 = −2,6 eV bir düzey enerjisi değildir ve 11 eV iyonlaşma için de yetersizdir; foton soğurulmaz.','III':'12,75 eV ile −13,6 + 12,75 = −0,85 eV olur; bu n = 4 düzeyinin enerjisidir, foton soğurulur.'}
d8,y8,ad8=onc(tr,rs,S5)
q('0008',6,z='orta',kalip='öncüllü',tipId='atom-uyarma',tip='Uyarılma ve iyonlaşma',kaz='Temel haldeki hidrojen atomunun hangi fotonları soğurabileceğini belirler.',
 metin='Temel hâldeki hidrojen atomlarından oluşan bir gaza, enerjileri tabloda verilen I, II ve III fotonları ayrı ayrı gönderiliyor. Hidrojen atomunun n. düzeyinin enerjisi E_n = −13,6/n² eV’tur ve her foton atomla tek bir etkileşim yapabilmektedir.\nBuna göre, hangi fotonlar atom tarafından soğurulur?',
 dogru=d8,yan=y8,sira=S5,istenen='Soğurulan fotonlar.',ip=['Foton enerjisini temel düzeyin enerjisine ekleyerek elde edilen değerin bir düzey enerjisi olup olmadığına bak.'],bilgi=[B_UYA,B_SEV],ad=ad8,
 puf='Foton ancak enerjisi iki düzey farkına tam eşitse soğurulur; “yaklaşık” yetmez.',sekil=sk)
# ================= 09 · orta · iyonlaşma =================
Ef=Fr(5); KE=Ef+E(2); assert KE==Fr(8,5) and -E(2)==Fr(17,5) and Ef-E(1)-0==Fr(93,5)
atom='\\draw[thick] (0,0) circle (1.1); \\draw[thick,fill=gray!40] (0,0) circle (.16);'+N(0,-1.45,'$n=2$','')+'\\fill[vurgu!70!black] (0.78,0.78) circle (.11);'
sk=fig(atom,'\\draw[thick,decorate,decoration={snake,amplitude=1.2mm,segment length=4mm},-{Stealth}] (-3.6,.78) -- (.6,.78);'+N(-2.1,1.3,'foton, $5$ eV',''),
 f'\\draw[thick,{ARR}] (.95,.95) -- (3.3,2.2);'+N(3.4,2.3,'$e^-$','right'))
q('0009',6,z='orta',kalip='şekilli',tipId='atom-uyarma',tip='Uyarılma ve iyonlaşma',kaz='Uyarılmış hidrojen atomunun iyonlaşmasında kopan elektronun kinetik enerjisini hesaplar.',
 metin='Hidrojen atomunun n. düzeyinin enerjisi E_n = −13,6/n² eV’tur. 2. düzeyde bulunan elektrona sahip bir hidrojen atomu, şekilde enerjisi verilen fotonu soğuruyor ve elektron atomdan kopuyor. Kopan elektronun, atomdan yeterince uzaklaştığında çekirdeğe göre potansiyel enerjisi sıfırdır.\nBuna göre, kopan elektronun kinetik enerjisi kaç eV’tur?',
 dogru=KE,yan=[(Fr(17,5),'Elektronun iyonlaşma enerjisini (3,4 eV) kinetik enerji olarak almıştır.','dikkat'),(Fr(5),'Fotonun bütün enerjisinin elektronun kinetik enerjisi olduğunu sanmıştır.','bilgi'),(Fr(42,5),'Foton enerjisine iyonlaşma enerjisini eklemiştir: 5 + 3,4 = 8,4 eV.','islem'),(Fr(93,5),'Temel düzeyin enerjisini kullanarak 5 + 13,6 = 18,6 eV bulmuştur; elektron 2. düzeydedir.','dikkat')],
 istenen='Kopan elektronun kinetik enerjisi (eV).',ip=['Önce 2. düzeydeki elektronu koparmak için gereken en küçük enerjiyi bul; fotonun enerjisiyle karşılaştır.'],bilgi=[B_UYA],
 ad=[A('İyonlaşma enerjisini bul','2. düzeydeki elektronun enerjisi −3,4 eV olduğundan elektronu koparmak için 3,4 eV gerekir.','E₂ = −13,6 ÷ 4 = −3,4 eV'),A('Fotonu karşılaştır','Foton enerjisi iyonlaşma enerjisinden büyüktür; elektron kopar.','5 eV > 3,4 eV'),A('Fazlayı hesapla','Fazla enerji elektronun kinetik enerjisi olur.','Ek = 5 − 3,4 = 1,6 eV')],
 puf='İyonlaşmada kinetik enerji = foton enerjisi − bulunulan düzeyin iyonlaşma enerjisi.',sekil=sk)
# ================= 10 · orta · öncüllü · seri aralıkları =================
sx=8/2000
bars=[('K',91,122),('L',365,656),('M',820,1875)]
ax='\\draw[thick] (0,0) -- (8.4,0);'+''.join(f'\\draw[thick] ({v*sx:.2f},0) -- ({v*sx:.2f},-.12); '+N(v*sx,-.38,str(v),'font=\\footnotesize') for v in (0,500,1000,1500,2000))
ax+=N(4.2,-.95,'dalga boyu (nm)','')
bs=''.join(f'\\draw[thick,fill=vurgu!35] ({a*sx:.2f},.1) rectangle ({b*sx:.2f},.6); '+N((a+b)/2*sx,.95,g,'') for g,a,b in bars)
sk=fig(ax,bs)
tr={'I':True,'II':True,'III':False}
rs={'I':'Şekilde K grubunun dalga boyları L grubundakilerden daha küçüktür; dalga boyu küçük olan fotonun enerjisi büyüktür.','II':'L grubu n = 2’ye inişlerdir; bunların arasında en küçük enerji farkı 3 → 2 geçişine aittir ve en küçük enerji en büyük dalga boyunu verir.','III':'M grubu n = 3 düzeyine inişlerdir; temel hâle (n = 1) inişler K grubunu oluşturur.'}
d10,y10,ad10=onc(tr,rs,S5)
q('0010',7,z='orta',kalip='grafik',tipId='atom-spektrum',tip='Spektrum çizgileri ve seriler',kaz='Hidrojen spektrumunun seri aralıklarından enerji ve geçiş çıkarımları yapar.',
 metin='Uyarılmış hidrojen atomlarının yayımladığı çizgilerden K, L ve M gruplarında elektronlar sırasıyla n = 1, n = 2 ve n = 3 düzeylerine iniyor. Şekilde her grubun kapsadığı dalga boyu aralığı verilmiştir.\nBuna göre;\nI. K grubundaki her fotonun enerjisi, L grubundaki her fotonun enerjisinden büyüktür.\nII. L grubundaki en büyük dalga boylu çizgi, elektronun 3. düzeyden 2. düzeye inmesiyle oluşur.\nIII. M grubundaki çizgiler, elektronun temel düzeye inmesiyle oluşur.\nyargılarından hangileri doğrudur?',
 dogru=d10,yan=y10,sira=S5,istenen='Doğru olan yargılar.',ip=['Dalga boyu aralıklarını enerjiye çevirirken dalga boyu ile enerjinin ters orantılı olduğunu ve her grubun hangi alt düzeye indiğini kullan.'],bilgi=[B_SPE],ad=ad10,
 puf='Dalga boyu küçüldükçe enerji büyür; seriyi alt düzey belirler.',sekil=sk)
# ================= 11 · orta · grafik · Z =================
sk=tikz_svg(HEAD+'\\begin{axis}[width=6.4cm,height=5.2cm,xmin=0,xmax=0.5,ymin=0,ymax=120,xtick={0,0.25,0.5},ytick={0,20,40,60,80,100,120},grid=both,major grid style={gray!55,thin},tick label style={font=\\footnotesize},axis lines=left,xlabel={$1/n^2$},ylabel={$E_k$ (eV)},xlabel style={font=\\small},ylabel style={font=\\small}]\n'
 '\\addplot[thick,vurgu,domain=0:0.5] {217.6*x};\n\\addplot[only marks,mark=*,mark size=2pt] coordinates {(0.25,54.4)};\n\\draw[dashed] (axis cs:0.25,0) -- (axis cs:0.25,54.4) -- (axis cs:0,54.4);\n\\node[anchor=north west,font=\\footnotesize] at (axis cs:0.27,50) {$E_k=54{,}4$ eV};\n\\end{axis}'+TAIL)
Z11=4
assert Fr(68,5)*Z11**2/4==Fr(272,5)
assert Fr(272,5)/Fr(68,5)==4 and Fr(272,5)/Fr(68,5)/4==1 and Fr(272,5)*2/Fr(68,5)==8 and Fr(272,5)*4/Fr(68,5)==16
q('0011',8,z='orta',kalip='grafik',tipId='atom-benzeri',tip='Hidrojen benzeri iyonlar',kaz='Hidrojen benzeri iyonun kinetik enerji grafiğinden atom numarasını bulur.',
 metin='Bohr modeline göre, tek elektronlu bir iyonda elektronun n. yörüngedeki kinetik enerjisi E_k = 13,6·Z²/n² eV bağıntısıyla verilir (Z: atom numarası). Bu bağıntıya uyan bir iyonun elektronunun kinetik enerjisinin 1/n² ile değişimi şekilde gösterilmiştir. Grafikte işaretli nokta, elektronun 2. yörüngede bulunduğu durumu göstermektedir.\nBuna göre, iyonun atom numarası kaçtır?',
 dogru=Z11,yan=[(1,'Nokta için 54,4 = 13,6 × Z² × 4 yazıp Z² = 1 bulmuştur; 1/n²’nin yerine n² kullanmıştır.','islem'),(2,'n² çarpanını hesaba katmadan 54,4 = 13,6·Z² yazıp Z² = 4, Z = 2 bulmuştur.','dikkat'),(8,'Bağıntıyı E_k = 13,6·Z/n sanıp 54,4 = 13,6·Z/2 ile Z = 8 bulmuştur.','bilgi'),(16,'Z² = 16 değerini bulup karekökünü almadan atom numarası olarak yazmıştır.','islem')],
 istenen='İyonun atom numarası.',ip=['İşaretli noktanın 1/n² değerini ve kinetik enerjisini bağıntıda yerine yazıp Z’yi çek.'],bilgi=[B_BEN,B_BOH],
 ad=[A('Noktayı oku','2. yörüngede 1/n² = 1/4 ve kinetik enerji 54,4 eV’tur.','n = 2 → 1/n² = 0,25 · E_k = 54,4 eV'),A('Bağıntıya yaz','Verilen bağıntıda değerleri yerine koy.','54,4 = 13,6 × Z² × 0,25'),A('Z²’yi bul','Eşitliği düzenle.','Z² = 54,4 ÷ 3,4 = 16'),A('Z’yi bul','Karekök al.','Z = 4')],
 puf='Z² çarpan olarak girer; son adımda karekök almayı unutma.',sekil=sk)
# ================= 12 · orta · öncüllü · model panelleri =================
def sphere(cx):
    s=f'\\draw[thick,fill=gray!14] ({cx},0) circle (1.3);'
    for x,y in [(-.6,.55),(.5,.6),(-.1,0),(.7,-.3),(-.7,-.5),(.2,-.8)]:
        s+=f'\\fill[vurgu!70!black] ({cx+x:.2f},{y:.2f}) circle (.1);'
    return s
def rut(cx):
    return (f'\\draw[thick,fill=gray!50] ({cx},0) circle (.14); \\draw[thick] ({cx},0) circle (1.1); \\fill[vurgu!70!black] ({cx+.78:.2f},.78) circle (.1);'
            f'\\draw[thick,{ARR}] ({cx+.78:.2f},.78) -- ({cx+.55:.2f},1.08);')
def boh(cx):
    s=f'\\draw[thick,fill=gray!50] ({cx},0) circle (.14);'
    for n,r in ((1,.45),(2,.9),(3,1.35)):
        s+=f'\\draw[thick] ({cx},0) circle ({r}); '+N(cx,r,f'$n={n}$','font=\\scriptsize,fill=white,inner sep=1pt')
    c=.7071
    s+=f'\\fill[vurgu!70!black] ({cx+1.35*c:.2f},{-1.35*c:.2f}) circle (.1);'
    s+=f'\\draw[thick,dashed] ({cx+.9*c:.2f},{-.9*c:.2f}) circle (.1);'
    s+=f'\\draw[thick,decorate,decoration={{snake,amplitude=.8mm,segment length=3mm}},{ARR}] ({cx+1.35*c+.15:.2f},{-1.35*c-.15:.2f}) -- ({cx+1.35*c+.95:.2f},{-1.35*c-.95:.2f});'
    return s
sk=fig(sphere(0),rut(4.2),boh(8.6),N(0,-2.6,'K',''),N(4.2,-2.6,'L',''),N(8.6,-2.6,'M',''))
tr={'I':False,'II':True,'III':False}
rs={'I':'K, elektronların pozitif bir kürenin içine gömülü olduğu Thomson modelidir; bu modelde çekirdek yoktur, kütle atom hacmine yayılmıştır.','II':'L, Rutherford modelidir; yörüngede ivmeli dolanan elektron klasik elektromanyetizmaya göre ışıma yaparak enerji kaybeder ve çekirdeğe düşmelidir.','III':'M, Bohr modelidir; yalnız hidrojen ve hidrojen benzeri tek elektronlu atomların spektrumlarını açıklar, çok elektronlu atomları açıklayamaz.'}
d12,y12,ad12=onc(tr,rs,S5)
q('0012',1,z='orta',kalip='öncüllü',tipId='atom-model',tip='Atom modellerinin karşılaştırılması',kaz='Şekilleri verilen atom modellerini tanıyıp başarı ve sınırlarını değerlendirir.',
 metin='Şekilde, K, L ve M ile gösterilen üç atom modeli çizilmiştir.\nBuna göre;\nI. K modeline göre atomun kütlesinin büyük bölümü merkezdeki çekirdekte toplanmıştır.\nII. L modeline göre çekirdek etrafında dolanan elektron, klasik elektromanyetizmaya göre enerji yayarak çekirdeğe düşmelidir.\nIII. M modeli, çok elektronlu atomların çizgi spektrumlarını başarıyla açıklar.\nyargılarından hangileri doğrudur?',
 dogru=d12,yan=y12,sira=S5,istenen='Doğru olan yargılar.',ip=['Önce her şeklin hangi atom modeline ait olduğunu elektronların ve çekirdeğin çizimine bakarak belirle.'],bilgi=[B_MOD],ad=ad12,
 puf='Thomson’da çekirdek yok, Rutherford’da kararlılık sorunu var, Bohr yalnız tek elektronlu atomlarda başarılı.',sekil=sk)
# ================= 13 · orta · spektrum çizgisi λ =================
sx=8/200
ax='\\draw[thick] (0,0) -- (8.4,0);'+''.join(f'\\draw[thick] ({v*sx:.2f},0) -- ({v*sx:.2f},-.12); '+N(v*sx,-.38,str(v),'font=\\footnotesize') for v in (0,50,100,150,200))
ax+=N(4.2,-.95,'dalga boyu (nm)','')
ln=f'\\draw[very thick,vurgu] ({100*sx},0) -- ({100*sx},1.0); '+N(100*sx,1.3,'K','')+f'\\draw[very thick,vurgu] ({150*sx},0) -- ({150*sx},1.0); '+N(150*sx,1.3,'L','')
sk=fig(ax,ln)
l31,l21=Fr(100),Fr(150); l32=1/(1/l31-1/l21)
assert l32==300 and l21-l31==50 and l31*l21/(l31+l21)==60 and (l31+l21)/2==125 and l31+l21==250 and l31/l21*0==0
q('0013',7,z='orta',kalip='grafik',tipId='atom-spektrum',tip='Spektrum çizgileri ve seriler',kaz='Üç düzeyli atomda iki çizgiden üçüncünün dalga boyunu bulur.',
 metin='Üç enerji düzeyi (n = 1, 2, 3) bulunan bir atomun yayımladığı çizgi spektrumunun iki çizgisi şekilde gösterilmiştir. K çizgisi elektronun 3. düzeyden 1. düzeye, L çizgisi ise 2. düzeyden 1. düzeye inmesiyle oluşmaktadır.\nBuna göre, elektronun 3. düzeyden 2. düzeye inmesiyle oluşan çizginin dalga boyu kaç nm’dir?',
 dogru=l32,yan=[(50,'Dalga boylarının farkını almıştır: 150 − 100 = 50 nm.','bilgi'),(60,'Enerjiler toplanırken yanlışlıkla 1/λ değerlerini toplamıştır: 1/λ = 1/100 + 1/150 → 60 nm.','islem'),(125,'Dalga boylarının ortalamasını almıştır: (100 + 150) ÷ 2 = 125 nm.','bilgi'),(250,'Dalga boylarını toplamıştır: 100 + 150 = 250 nm.','bilgi')],
 istenen='3 → 2 geçişinde yayımlanan fotonun dalga boyu (nm).',ip=['Üç düzey arasındaki enerji farklarını yaz; 3 → 2 enerjisi diğer ikisinin farkıdır; enerjiyi dalga boyuyla ilişkilendir.'],bilgi=[B_SPE,B_SEV],
 ad=[A('Enerji ilişkisini kur','3 → 1 geçişi, 3 → 2 ve 2 → 1 geçişlerinin toplamıdır.','E₃₁ = E₃₂ + E₂₁'),A('Dalga boyuna çevir','E = hc/λ olduğundan her enerji 1/λ ile orantılıdır.','1/λ₃₁ = 1/λ₃₂ + 1/λ₂₁'),A('Değerleri yaz','Şekilden λ₃₁ = 100 nm ve λ₂₁ = 150 nm okunur.','1/λ₃₂ = 1/100 − 1/150 = 1/300'),A('Sonuç','Tersini al.','λ₃₂ = 300 nm')],
 puf='Enerjiler toplanır, dalga boyları değil; 1/λ üzerinden işlem yap.',sekil=sk)
# ================= 14 · orta · öncüllü · metin =================
r2,r4=Fr(2)**2,Fr(4)**2; assert r4/r2==4 and Fr(4,2)==2 and (Fr(1,16))/(Fr(1,4))==Fr(1,4)
tr={'I':True,'II':True,'III':True}
rs={'I':'L = n·h/2π olduğundan n 2’den 4’e çıkınca açısal momentum 2 katına çıkar.','II':'r ∝ n² olduğundan yarıçap 16/4 = 4 katına çıkar.','III':'E_k ∝ 1/n² olduğundan kinetik enerji 4/16 = 1/4’üne iner, yani 4 kat azalır.'}
S14=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']
d14,y14,ad14=onc(tr,rs,S14)
q('0014',4,z='orta',kalip='öncüllü',tipId='atom-bohr',tip='Bohr modelinde yörünge nicelikleri',kaz='Bohr modelinde yörünge numarası değişince açısal momentum, yarıçap ve kinetik enerji değişimini yorumlar.',
 metin='Bohr atom modeline göre hidrojen atomunun elektronu, enerji alarak 2. yörüngeden 4. yörüngeye çıkıyor.\nBuna göre, bu değişimle ilgili;\nI. Elektronun açısal momentumu 2 katına çıkar.\nII. Elektronun yörünge yarıçapı 4 katına çıkar.\nIII. Elektronun kinetik enerjisi 4 kat azalır.\nyargılarından hangileri doğrudur?',
 dogru=d14,yan=y14,sira=S14,istenen='Doğru olan yargılar.',ip=['Açısal momentum, yarıçap ve kinetik enerjinin yörünge numarası n ile nasıl orantılı olduğunu ayrı ayrı yaz.'],bilgi=[B_BOH],ad=ad14,
 puf='L ∝ n, r ∝ n², E_k ∝ 1/n²: oranları n’lerin oranından kur.')
# ================= 15 · zor · He+ → H =================
EHe=lambda n: E(n,2)
fo=EHe(4)-EHe(2); assert fo==Fr(51,5)==E(2)-E(1)
assert E(1,1)+fo==E(2) and -E(2,1)==Fr(17,5)
f_noz=E(4)-E(2); assert f_noz==Fr(51,20) and E(1)+f_noz<E(2)
assert (EHe(4)-EHe(1))>Fr(68,5)
assert Fr(68,5)-fo==Fr(17,5) and Fr(68,5)/Fr(17,5)==4 and E(3)!=E(2)
q('0015',6,z='zor',kalip='yeni nesil',tipId='atom-uyarma',tip='Uyarılma ve iyonlaşma',kaz='Hidrojen benzeri iyonun yaydığı fotonun temel haldeki hidrojen atomunda yol açacağı uyarılmayı bulur.',
 metin='Tek elektronlu bir iyonun n. düzeyinin enerjisi E_n = −13,6·Z²/n² eV’tur. He⁺ iyonunun (Z = 2) elektronu 4. düzeyden 2. düzeye inerken bir foton yayımlıyor. Bu foton, temel hâldeki bir hidrojen atomuna (Z = 1) gönderiliyor ve atom tarafından soğuruluyor.\nBuna göre, hidrojen atomunun elektronu hangi duruma geçer?',
 dogru='n = 2 düzeyine çıkar',yan=[('Soğurulamaz, n = 1’de kalır','Z² çarpanını katmadan fotonun enerjisini 2,55 eV bulmuştur; bu enerji hiçbir düzey farkına uymaz.','dikkat'),('Elektron atomdan kopar','Yayımlanan fotonun enerjisini 13,6 eV bulup iyonlaşma enerjisine eşitlemiştir; oysa foton 10,2 eV’tur.','islem'),('n = 3 düzeyine çıkar','13,6 − 10,2 = 3,4 eV’u 3. düzeyin enerjisi sanmıştır; 3,4 eV, 2. düzeyin enerjisinin büyüklüğüdür.','bilgi'),('n = 4 düzeyine çıkar','3,4 = 13,6/n eşitliğinden n = 4 bulmuştur; enerji n² ile ters orantılıdır, n ile değil.','islem')],
 sira=['Soğurulamaz, n = 1’de kalır','Elektron atomdan kopar','n = 2 düzeyine çıkar','n = 3 düzeyine çıkar','n = 4 düzeyine çıkar'],
 istenen='Hidrojen atomunun elektronunun ulaştığı durum.',ip=['Önce He⁺ iyonunun yaydığı fotonun enerjisini bul; sonra hidrojen atomunun hangi düzey farkının buna eşit olduğuna bak.'],bilgi=[B_BEN,B_UYA],
 ad=[A('İki düzey enerjisi','He⁺ için Z = 2 alarak 2. ve 4. düzeylerin enerjilerini yaz.','E₂ = −13,6 × 4 ÷ 4 = −13,6 eV · E₄ = −13,6 × 4 ÷ 16 = −3,4 eV'),A('Foton enerjisi','Yayımlanan foton enerjisi düzeylerin farkıdır.','E = −3,4 − (−13,6) = 10,2 eV'),A('Hidrojenin hâli','Temel haldeki hidrojenin E₁ = −13,6 eV değerine foton enerjisini ekle.','−13,6 + 10,2 = −3,4 eV'),A('Düzeyi bul','−3,4 eV, hidrojenin hangi düzeyinin enerjisidir?','−13,6 ÷ n² = −3,4 → n = 2'),A('Sonuç','Foton tam uyduğundan soğurulur.','n = 1 → n = 2')],
 puf='Hidrojen benzeri iyonda Z² çarpanı, aynı foton enerjisini farklı düzey çiftlerinde üretebilir.')
# ================= 16 · zor · elektron çarpışması =================
Vh=Fr(25,2); Eex=lambda n: E(n)-E(1)
assert Eex(2)==Fr(51,5) and Eex(3)<Vh<Eex(4) and Eex(4)==Fr(51,4) and Eex(5)>Vh
nmax=max(n for n in range(2,60) if Eex(n)<=Vh); assert nmax==3
cizgi=lambda n: n*(n-1)//2
assert cizgi(3)==3 and cizgi(2)==1 and cizgi(4)==6 and cizgi(5)==10
sk=fig('\\draw[thick] (1.3,-.8) rectangle (7.3,.8);',
 '\\draw[very thick] (.2,.5) -- (.2,-.5); '+N(.2,.85,'$-$','font=\\footnotesize')+'\\draw[thick,dashed] (1.0,.7) -- (1.0,-.7); '+N(1.0,.9,'$+$','font=\\footnotesize'),
 '\\draw[thick] (.2,-.5) -- (.2,-2.2) -- (.4,-2.2); \\draw[thick] (.6,-2.2) -- (1.0,-2.2) -- (1.0,-.7);\\draw[very thick] (.4,-2.0) -- (.4,-2.4); \\draw[very thick] (.6,-1.9) -- (.6,-2.5);',
 N(.5,-2.85,'$12{,}5$ V',''),
 f'\\draw[thick,vurgu,{ARR}] (1.2,0) -- (3.0,0);'+N(2.1,.4,'$e^-$',''),
 ''.join(f'\\draw[thick,fill=gray!25] ({x},{y}) circle (.2); '+N(x,y,'H','font=\\scriptsize') for x,y in [(4.0,.35),(5.0,-.3),(6.0,.3),(6.6,-.35),(4.6,.45)]))
q('0016',6,z='zor',kalip='şekilli',tipId='atom-uyarma',tip='Uyarılma ve iyonlaşma',kaz='Elektron çarpışmasıyla uyarılan hidrojen gazında gözlenebilecek çizgi sayısını bulur.',
 metin='Şekildeki düzenekte, durgun halden 12,5 V’luk potansiyel farkıyla hızlandırılan elektronlar, temel hâldeki hidrojen atomlarından oluşan seyreltik bir gazdan geçiyor. Elektronlar atomlarla çarpışarak enerjilerinin bir kısmını aktarabilmektedir; hidrojenin n. düzeyinin enerjisi E_n = −13,6/n² eV’tur ve her atom en fazla bir çarpışma yapmaktadır.\nBuna göre, gazdan yayımlanan ışığın spektrumunda en çok kaç farklı çizgi gözlenebilir?',
 dogru=3,yan=[(1,'Yalnız 1 → 2 uyarılmasının (10,2 eV) olabileceğini düşünmüştür; 12,09 eV da aktarılabilir ve 3. düzeye çıkış mümkündür.','dikkat'),(2,'Yalnız temel hâle inen çizgileri (3 → 1 ve 2 → 1) saymış, 3 → 2 çizgisini unutmuştur.','dikkat'),(6,'4. düzeye çıkışı mümkün sanmıştır; oysa bunun için 12,75 eV gerekir ve 12,5 eV yetmez.','dikkat'),(10,'5. düzeye kadar uyarılabileceğini düşünmüştür; oysa bunun için 13,06 eV gerekir ve 12,5 eV yetmez.','dikkat')],
 istenen='Gözlenebilecek en çok farklı çizgi sayısı.',ip=['Elektronların her çarpışmada atoma aktarabileceği en büyük enerjiyi bulup temel düzeyden hangi düzeylere çıkılabileceğini belirle; sonra çizgi sayısını say.'],bilgi=[B_UYA,B_SPE],
 ad=[A('Elektron enerjisini bul','Potansiyel farkıyla hızlanan elektronun kinetik enerjisi e·V’dir.','Ek = 12,5 eV'),A('Uyarılma eşiklerini bul','Temel düzeyden n. düzeye çıkış için gereken enerji E_n − E₁’dir.','n=2: 10,2 · n=3: ≈ 12,09 · n=4: 12,75 · n=5: ≈ 13,06 eV'),A('Ulaşılabilen düzeyi seç','Aktarılabilen en büyük enerji 12,5 eV olduğundan yalnız eşiği bundan küçük düzeylere çıkılır.','n = 2 ve n = 3 (en çok 3. düzey)'),A('Çizgileri say','3. düzeye uyarılmış atomlar 3 → 2, 3 → 1 ve 2 → 1 geçişlerini yapar.','Çizgi sayısı = 3·2/2 = 3')],
 puf='Elektron çarpışmasında eşik koşulu vardır: enerji “en az” gereken değere eşit ya da fazla olmalıdır; foton ise tam uyum ister.',sekil=sk)
# ================= 17 · zor · proton ve α · en yakın yaklaşma =================
qa,ma,qp,mp=2,4,1,1
d_ratio=Fr(qa,1)/(Fr(ma,1))*Fr(mp,qp)   # d ∝ q/(m v²)
assert d_ratio==Fr(1,2) and Fr(1,ma)==Fr(1,4) and qa==2 and qa**2==4
def para(y,ad,isim): return f'\\draw[thick,{ARR}] (-3.2,{y}) -- (-.5,{y});'+N(-3.6,y,isim,'left')+N(-1.85,y+.45,ad,'')+N(-1.85,y-.45,'$v$ hızıyla','font=\\footnotesize')+f'\\fill[vurgu!45!black] (1.2,{y}) circle (.25);'+N(1.2,y-.6,'$+Ze$','')
sk=fig(para(1.6,'$+e$, $m$','Deney 1'),para(-.6,'$+2e$, $4m$','Deney 2'))
q('0017',3,z='zor',kalip='şekilli',tipId='atom-rutherford',tip='Rutherford saçılması ve çekirdek',kaz='Aynı hızlı farklı yük ve kütleli iki parçacığın en yakın yaklaşma uzaklıklarını karşılaştırır.',
 metin='Özdeş ve hareketsiz iki ağır çekirdeğin merkezlerine doğru, iki ayrı deneyde şekildeki gibi proton (yükü +e, kütlesi m) ve α parçacığı (yükü +2e, kütlesi 4m) aynı büyüklükte v hızıyla doğrusal yörüngede gönderiliyor. Parçacıklar çekirdeğe yaklaşırken yalnızca elektriksel itme kuvvetinin etkisinde kalıyor ve çekirdeğe en yakın noktada anlık olarak duruyorlar.\nBuna göre, α parçacığının çekirdeğe en yakın olduğu uzaklığın protonunkine oranı kaçtır?',
 dogru='1/2',yan=[('1/4','Yalnızca kütleyi hesaba katmış, yük farkını unutmuştur: kinetik enerji 4 kat, uzaklık 1/4.','dikkat'),('1','Aynı hızla gönderildikleri için uzaklıkların da aynı olacağını sanmıştır; oysa kinetik enerji ve yük farklıdır.','bilgi'),('2','Yalnızca yük oranını almıştır: (2e)/(e) = 2; kinetik enerji farkını katmamıştır.','dikkat'),('4','Yük oranının karesini almıştır: 2² = 4; uzaklık yükle doğru orantılıdır, yükün karesiyle değil.','islem')],
 sira=['1/4','1/2','1','2','4'],
 istenen='Uzaklıkların oranı d_α / d_p.',ip=['Her parçacık için en yakın noktada enerjinin korunumunu yaz; kinetik enerjiyi kütle ve hızla, potansiyel enerjiyi yükle ifade et.'],bilgi=[B_RUT],
 ad=[A('Enerji korunumu','Her deneyde ½mv² = k·q·(Ze)/d.','d = 2kqZe / (mv²)'),A('Oranları oku','Yük ve kütle oranları: q_α/q_p = 2, m_α/m_p = 4; hız aynı.','q: 2 kat · m: 4 kat'),A('d oranı','d, yük ile doğru, kütle ile ters orantılıdır (v aynı).','d_α/d_p = 2/4'),A('Sadeleştir','Oranı yaz.','d_α/d_p = 1/2')],
 puf='En yakın yaklaşma uzaklığı d ∝ q/(m·v²): yük ile doğru, kinetik enerji ile ters orantılı.',sekil=sk)
# ================= 18 · zor · He+ ve H · r, v =================
rr,vv=Fr(2**2,2)/1,Fr(2,2)/1; assert rr==2 and vv==1
assert Fr(2**2)==4 and Fr(1,2)==Fr(1)/2 and Fr(2**2*2)==8 and Fr(2,1)==2 and Fr(1,2**2*Fr(1,1))*4==1
q('0018',8,z='zor',kalip='yeni nesil',tipId='atom-benzeri',tip='Hidrojen benzeri iyonlar',kaz='Hidrojen benzeri iyonun yarıçap ve hız niceliklerini hidrojeninkilerle karşılaştırır.',
 metin='Bohr modeline göre, atom numarası Z olan tek elektronlu bir iyonda elektronun n. yörüngedeki yarıçapı r = a₀·n²/Z, hızı ise v = v₁·Z/n bağıntılarıyla bulunur. Burada a₀ ve v₁, hidrojen atomunun temel hâldeki elektronunun yarıçapı ve hızıdır.\nBuna göre, He⁺ iyonunun (Z = 2) 2. yörüngesindeki elektronun yarıçapı ve hızı, hidrojen atomunun temel hâldeki elektronununkilerle karşılaştırıldığında aşağıdakilerden hangisi doğru olur?',
 dogru='r: 2 katı · v: aynı',yan=[('r: 4 katı · v: yarısı','Z’yi bağıntılara katmamıştır: r = a₀·4 ve v = v₁/2 bulmuştur.','dikkat'),('r: 8 katı · v: aynı','Yarıçap bağıntısında Z’yi paya yazmıştır: r = a₀·4·2 = 8a₀.','bilgi'),('r: 2 katı · v: 2 katı','Hız bağıntısında n’yi unutmuştur: v = v₁·Z = 2v₁.','islem'),('r: aynı · v: 2 katı','Yarıçapta Z²’ye bölmüş (4/4 = 1) ve hızda n’yi unutmuştur.','bilgi')],
 sira=['r: 2 katı · v: aynı','r: 4 katı · v: yarısı','r: 8 katı · v: aynı','r: 2 katı · v: 2 katı','r: aynı · v: 2 katı'],
 istenen='İki atomun yarıçap ve hız karşılaştırması.',ip=['Verilen bağıntılarda He⁺ için Z = 2, n = 2; hidrojen için Z = 1, n = 1 yazıp oranları ayrı ayrı bul.'],bilgi=[B_BEN],
 ad=[A('He⁺ yarıçapı','Bağıntıda Z = 2, n = 2 yaz.','r = a₀·4/2 = 2a₀'),A('He⁺ hızı','Aynı değerlerle hızı bul.','v = v₁·2/2 = v₁'),A('Hidrojen değerleri','Temel hâl için n = 1, Z = 1.','r = a₀ · v = v₁'),A('Karşılaştır','Oranla.','r: 2 katı · v: aynı')],
 puf='Z, yarıçapı küçültür ve hızı artırır; n ise yarıçapı n² ile büyütür, hızı n ile küçültür.')
# ================= 19 · orta · Thomson deneyi =================
Eal,Bal=Fr(3000),Fr(3,2000); v19=Eal/Bal; assert v19==2*10**6 and Eal*Bal==Fr(9,2) and Bal/Eal==Fr(1,2*10**6)
assert Eal/(Fr(3,2))==2000 and Eal/(Fr(3,2)*Fr(1,10**6))==2*10**9
dots=''.join(f'\\draw[thick] ({x},{y}) circle (.1); \\fill ({x},{y}) circle (.03);' for x in (1.0,2.3,3.6,4.9) for y in (.4,1.2))
sk=fig('\\draw[very thick] (.5,1.7) -- (5.5,1.7); \\draw[very thick] (.5,-.1) -- (5.5,-.1);',
 ''.join(N(x,1.95,'$-$','font=\\footnotesize')+N(x,-.35,'$+$','font=\\footnotesize') for x in (1.0,2.0,3.0,4.0,5.0)),
 dots,f'\\draw[thick,vurgu,{ARR}] (-.9,.8) -- (5.9,.8);'+N(-1.1,.8,'$e^-$','left'),
 f'\\draw[thick,{ARR}] (6.7,.1) -- (6.7,1.5);'+N(6.9,.8,'$E=3000$ V/m','right'),
 N(3.0,-.95,'$\\odot$: $B=1{,}5$ mT (sayfa düzleminden dışarı)',''))
q('0019',2,z='orta',kalip='şekilli',tipId='atom-thomson',tip='Thomson deneyi ve hız seçici',kaz='Elektrik ve manyetik alanın birlikte bulunduğu bölgede sapmadan geçen elektronun hızını hesaplar.',
 metin='Şekilde, yatay ve düzgün bir elektrik alanın ve sayfa düzleminden dışarı yönlü düzgün bir manyetik alanın birlikte bulunduğu bölgeye soldan giren elektron, doğrultusundan sapmadan geçmektedir. Alanların büyüklükleri şekilde verilmiştir. Elektronun ağırlığı ihmal edilmektedir.\nBuna göre, elektronun hızı kaç m/s’dir?',
 dogru='2 × 10⁶',yan=[('5 × 10⁻⁷','Hızı B/E oranı olarak yazmıştır; doğru bağıntı v = E/B’dir.','bilgi'),('4,5','Hızı E ile B’nin çarpımı olarak yazmıştır: 3000 × 0,0015 = 4,5.','bilgi'),('2 × 10³','mT’yi tesla’ya çevirmeden B = 1,5 alıp 3000 ÷ 1,5 = 2000 bulmuştur.','islem'),('2 × 10⁹','mT’yi μT gibi çevirip B = 1,5 × 10⁻⁶ T almıştır: 3000 ÷ (1,5 × 10⁻⁶) = 2 × 10⁹.','islem')],
 sira=['5 × 10⁻⁷','4,5','2 × 10³','2 × 10⁶','2 × 10⁹'],
 istenen='Elektronun hızı (m/s).',ip=['Elektronun sapmadan gitmesi için elektrik ve manyetik kuvvetler arasındaki ilişkiyi yaz ve birimleri SI’ya çevir.'],bilgi=[B_THO],
 ad=[A('Sapmama koşulu','Elektron sapmadığına göre elektriksel ve manyetik kuvvetler eşit büyüklüktedir.','qE = qvB'),A('Hız bağıntısı','Yük sadeleşir ve hız bulunur.','v = E/B'),A('Birimi çevir','1 mT = 10⁻³ T olduğundan B = 1,5 × 10⁻³ T.','B = 1,5 × 10⁻³ T'),A('Hesapla','Değerleri yaz.','v = 3000 ÷ (1,5 × 10⁻³) = 2 × 10⁶ m/s')],
 puf='Hız seçicide v = E/B; mT, μT gibi birimleri önce tesla’ya çevir.',sekil=sk)
# ================= 20 · zor · Lyman/Balmer =================
lL=1/(1-Fr(1,4)); lB=1/(Fr(1,4)-Fr(1,9)); r20=lB/lL
assert r20==Fr(27,5) and lL/lB==Fr(5,27) and Fr(9,4)==Fr(3**2,2**2) and Fr(3**2,1**2)==9
q('0020',7,z='zor',kalip='yeni nesil',tipId='atom-spektrum',tip='Spektrum çizgileri ve seriler',kaz='Hidrojenin Lyman ve Balmer serilerinin en uzun dalga boylu çizgilerinin dalga boyu oranını bulur.',
 metin='Hidrojen atomunun çizgi spektrumunda, elektronun n = 1 düzeyine inişleriyle Lyman serisi, n = 2 düzeyine inişleriyle Balmer serisi oluşur. Lyman serisinin en büyük dalga boylu çizgisinin dalga boyu λ_L, Balmer serisinin en büyük dalga boylu çizgisinin dalga boyu λ_B’dir.\nBuna göre, λ_B / λ_L oranı kaçtır?',
 dogru='27/5',yan=[('5/27','Oranı ters yazmıştır: λ_L/λ_B = 5/27; dalga boyu enerjiyle ters orantılıdır ve istenen λ_B/λ_L’dir.','islem'),('9/4','Seri sınırlarını üst düzeylerin n² değerleri olarak alıp (3/2)² = 9/4 bulmuştur.','bilgi'),('3','Serilerin en büyük dalga boylu çizgilerini üst düzey numaralarının oranıyla (3/1) karşılaştırmıştır.','bilgi'),('9','Üst düzeyi 3, alt düzeyi 1 alıp n² oranını almıştır: 3²/1² = 9; enerji farklarını hesaplamamıştır.','bilgi')],
 sira=['5/27','9/4','3','27/5','9'],
 istenen='λ_B/λ_L oranı.',ip=['Her serinin en büyük dalga boylu çizgisinin, serinin en küçük enerji farklı geçişi olduğunu kullan; enerji farklarını 1/n² terimleriyle yaz.'],bilgi=[B_SPE],
 ad=[A('Çizgileri belirle','Her serinin en büyük dalga boylu çizgisi o serinin en küçük enerji farkı olan, bir üst düzeyden gelen geçiştir.','Lyman: 2 → 1 · Balmer: 3 → 2'),A('Enerji farklarını yaz','ΔE ∝ 1/n_alt² − 1/n_üst².','ΔE_L ∝ 1 − 1/4 = 3/4 · ΔE_B ∝ 1/4 − 1/9 = 5/36'),A('Dalga boyuna geç','λ ∝ 1/ΔE olduğundan oran enerji oranının tersidir.','λ_B/λ_L = ΔE_L/ΔE_B'),A('Hesapla','Kesirleri böl.','(3/4) ÷ (5/36) = 27/5')],
 puf='Dalga boyu oranı, ters enerji oranıdır; en uzun dalga boyu en küçük enerji farkıdır.')
# ================= yaz =================
def bitir_af():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'atom-1.json'),'/tmp/bos-atom.json')
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik (yalnız mantık), MEB 12. sınıf fizik müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','afatom.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_af()
