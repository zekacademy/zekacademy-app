"""AYT Fizik · Radyoaktivite · 20 soru (kardeş yok, ipucu 1). Cevap ve çeldiriciler Python'da hesaplanıp assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from math import sqrt,exp
H.KONU='Radyoaktivite'
P=Parti('radyo','Radyoaktivite','afiz|Radyoaktivite',ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM AYT 2018–2025 Fizik (Radyoaktivite, çekirdek tepkimeleri; yalnız mantık) · 345 AYT Fizik s.331–392 · Bilgi Sarmal AYT Fizik · MEB 12. sınıf fizik'
TIPLER={'ra-bozunma':'Alfa, beta ve gama bozunmaları','ra-isinim':'Işımaların özellikleri','ra-yarisure':'Yarı ömür','ra-zincir':'Bozunma zincirleri',
 'ra-tepkime':'Çekirdek tepkimeleri','ra-fisfuz':'Fisyon ve füzyon','ra-baglanma':'Bağlanma enerjisi','ra-enerji':'Kütle–enerji dönüşümü'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AFRA-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AFRA-{kn:02d} ('+CARD[kn]+')',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=1.9mm]}'
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def D(a,b,o='thick'): return f'\\draw[{o}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def AR(a,b,o='vurgu,very thick'): return f'\\draw[{o},{ARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def DOT(p,r=2.0,o=''): return f'\\fill[{o}] ({p[0]:.3f},{p[1]:.3f}) circle ({r}pt);'
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
def nk(A,Z,s='',t=None):
    return f'${{}}^{{{A}}}_{{{Z}}}\\mathrm{{{s}}}$'
SUP=str.maketrans('0123456789','⁰¹²³⁴⁵⁶⁷⁸⁹'); SUB=str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')
def u(A,Z,s): return str(A).translate(SUP)+str(Z).translate(SUB)+s
def dec(n,k):
    A,Z=n
    return {'a':(A-4,Z-2),'b-':(A,Z+1),'b+':(A,Z-1),'g':(A,Z)}[k]
def sci(c,e): return f'{fm(c)} × 10'+str(e).translate(SUP)
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
# ---------- bilgi kutuları (örnekler sorulardaki sayıları kullanmaz)
BZ=B('Bozunma türleri','α bozunmasında ⁴₂He çekirdeği yayınlanır: A 4, Z 2 azalır. β⁻ bozunmasında bir nötron protona dönüşür: A değişmez, Z 1 artar. β⁺ bozunmasında bir proton nötrona dönüşür: Z 1 azalır. γ ışımasında A ve Z değişmez. Her bozunmada toplam A ve toplam Z korunur. Örnek: ¹⁵⁰₆₀X α yayınlarsa ¹⁴⁶₅₈Y oluşur')
IS=B('Işımaların özellikleri','α (He çekirdeği, +2e) iyonlaştırması en büyük, nüfuz gücü en küçüktür; kâğıt durdurur. β (elektron ya da pozitron) alüminyum levhada durur. γ yüksüz bir elektromanyetik dalgadır, alanlarda sapmaz ve en fazla işler; kalın kurşun şiddetini azaltır. Örnek: elektrik alanda en çok sapan ışıma, yük ÷ kütle oranı en büyük olan parçacıklardan oluşur')
YO=B('Yarı ömür','Kalan çekirdek sayısı N = N₀ × (½)^(t ÷ T) bağıntısıyla bulunur; T sıcaklık, basınç ve kimyasal bağdan bağımsızdır. Aktivite (bozunma hızı) kalan çekirdek sayısıyla doğru orantılıdır ve her yarı ömürde yarıya iner. Örnek: T = 4 saat ise 12 saat sonra kalan sayı N₀ ÷ 8 olur')
TP=B('Çekirdek tepkimelerinde korunum','girenlerin ve ürünlerin kütle numaraları toplamı ile atom numaraları (yük) toplamı eşittir. Bilinmeyen parçacık bu iki toplamdan bulunur: A = 1, Z = 1 proton; A = 1, Z = 0 nötron; A = 0, Z = −1 elektron; A = 0, Z = +1 pozitron. Örnek: ¹⁴₇N + ¹₀n → ¹⁴₆C + ᴬ_ZX tepkimesinde X, protondur')
FF=B('Fisyon ve füzyon','Fisyonda ağır bir çekirdek nötron yakalayıp daha hafif iki çekirdeğe ve birkaç nötrona bölünür; füzyonda hafif çekirdekler birleşir. İkisinde de ürünlerin toplam kütlesi girenlerinkinden küçüktür ve fark E = Δm × c² kadar enerjiye dönüşür. Füzyon için çok yüksek sıcaklık gerekir. Örnek: yıldızlarda hidrojen çekirdekleri helyuma dönüşür')
BE=B('Bağlanma enerjisi','nükleon başına bağlanma enerjisi (Eb ÷ A) A ≈ 56 civarında en büyüktür. Toplam bağlanma enerjisi A × (Eb ÷ A) ile bulunur. Bir tepkimede açığa çıkan enerji, ürünlerin toplam bağlanma enerjisi ile girenlerinkinin farkıdır. Örnek: 40 nükleonlu bir çekirdekte nükleon başına 8 MeV ise toplam bağlanma enerjisi 320 MeV’dir')
ME=B('Kütle–enerji eşdeğerliği','kütlesi Δm olan bir kütle farkı E = Δm × c² kadar enerjiye karşılık gelir (c = 3 × 10⁸ m/s). Güç, birim zamandaki enerjidir: P = E ÷ t. Örnek: 2 kg’lık kütle kaybı için E = 2 × 9 × 10¹⁶ J = 1,8 × 10¹⁷ J olur')
NZ=B('N–Z düzleminde bozunma','proton sayısı Z’ye, nötron sayısı N’ye karşı çizilirse α bozunması (N − 2, Z − 2), β⁻ bozunması (N − 1, Z + 1), β⁺ bozunması (N + 1, Z − 1) yönünde ok verir. Aynı Z izotop, aynı N izoton, aynı A = N + Z izobar çekirdeklerdir. Örnek: (N = 20, Z = 18) ile (N = 22, Z = 18) çekirdekleri izotoptur')
MO=B('Bozunmada momentum korunumu','durgun çekirdek iki parçaya ayrılırsa parçaların momentumları büyüklükçe eşit, yönce zıttır. K = p² ÷ 2m olduğundan kinetik enerjiler kütlelerle ters orantılıdır. Kütleler kütle numaralarıyla orantılı alınır. Örnek: kütleleri 1 ve 9 birim olan iki parçanın kinetik enerjileri 9 : 1 oranındadır')
YT=B('Radyoaktif yaş tayini','kayada başlangıçta yalnız ana çekirdek varsa, bozunan çekirdek sayısı kadar yavru çekirdek oluşur. Ana çekirdeğin kalan oranı ½ⁿ ise geçen süre n yarı ömürdür. Örnek: ana çekirdek oranı başlangıcın ⅛’i ise 3 yarı ömür geçmiştir')
# ===== 01 kolay · alfa bozunmasında nötron sayısı
card(1,'Alfa bozunmasında nükleon sayıları','α bozunmasında A 4, Z 2 azalır; nötron sayısı N = A − Z yeni değerlerle bulunur.','Nötron sayısının değişmediğini ya da A’yı sabit bırakıp yalnız Z’yi değiştirmeyi sanmak.','kolay','şekilli',3,'ra-bozunma','α yayan çekirdeğin ürünündeki nötron sayısı')
n1=(226,88); p1=dec(n1,'a'); N1=p1[0]-p1[1]; assert p1==(222,86) and N1==136
e1=n1[0]-n1[1]; e2=e1-4; e3=p1[0]-(n1[1]+2); e4=n1[0]-p1[1]
assert (e1,e2,e3,e4)==(138,134,132,140) and len({N1,e1,e2,e3,e4})==5
o=[r'\node[draw,rounded corners=3pt,very thick,inner sep=6pt] (a) at (0,0) {'+nk(226,88,'Ra')+'};',
   AR((1.0,0),(2.5,0)),N(1.75,.42,r'$\alpha$ yayınlanır','font=\\scriptsize'),
   r'\node[draw,rounded corners=3pt,very thick,inner sep=6pt] at (3.4,0) {$\mathrm{X}$};',N(4.25,0,'+'),
   r'\node[draw,rounded corners=3pt,thick,inner sep=6pt] at (5.2,0) {'+nk(4,2,'He')+'};']
SK=tikz(o)
q('0001',tipId='ra-bozunma',tip=TIPLER['ra-bozunma'],z='kolay',alt='Alfa Bozunması',kaz='α bozunmasında kütle ve atom numarasının değişimini kullanarak ürün çekirdeğin nötron sayısını bulur.',kalip='şekilli',
 metin='Kararsız bir Ra çekirdeği, şekilde gösterildiği gibi α parçacığı yayınlayarak X çekirdeğine dönüşmektedir.\nBuna göre, X çekirdeğinin nötron sayısı kaçtır?',
 sekil=SK,dogru=N1,yan=[(e1,f'α bozunmasında nötron sayısının değişmediğini düşünüp Ra çekirdeğinin nötron sayısını ({n1[0]} − {n1[1]} = {e1}) yazmış.','bilgi'),
  (e2,f'α parçacığıyla çekirdekten 4 nötron ayrıldığını sanmış: {e1} − 4 = {e2}.','bilgi'),
  (e3,f'Atom numarasını 2 artırıp (Z = {n1[1]+2}) {p1[0]} − {n1[1]+2} = {e3} bulmuş.','islem'),
  (e4,f'Kütle numarasını {n1[0]} bırakıp yalnız atom numarasını düşürmüş: {n1[0]} − {p1[1]} = {e4}.','islem')],
 istenen='X çekirdeğinin nötron sayısı.',
 ip=['Önce ürün çekirdeğin kütle ve atom numarasını bulmak için α parçacığının taşıdığı nükleonları düşün.'],
 bilgi=[BZ],
 ad=[A('Kütle numarası','α parçacığı 4 nükleon taşır; kütle numaraları toplamı korunur.','A = 226 − 4 = 222'),
     A('Atom numarası','α parçacığı 2 proton taşır; atom numaraları toplamı korunur.','Z = 88 − 2 = 86'),
     A('Nötron sayısı','Nötron sayısı kütle numarası ile atom numarasının farkıdır.','N = 222 − 86 = 136')],
 puf='α bozunmasında ana çekirdek 2 proton ve 2 nötron kaybeder; nötron sayısı da 2 azalır.')
# ===== 02 kolay · elektrik alanda ışımalar (öncüllü)
card(2,'Elektrik alanda ışımaların sapması','Sapmanın yönü yükün işaretini, miktarı yük ÷ kütle oranını verir; yüksüz ışıma sapmaz ve en fazla işler.','Sapmayan ışımanın alan yönüne göre yolunu değiştireceğini sanmak; ağır parçacığın daha çok saptığını düşünmek.','kolay','öncüllü',3,'ra-isinim','alan içinde üç ışımanın izleri')
o=[D((0,1.05),(2.6,1.05),'ultra thick'),D((0,-1.05),(2.6,-1.05),'ultra thick'),N(1.3,1.45,'(+) levha'),N(1.3,-1.45,'($-$) levha'),
   r'\fill[gray!60] (-1.3,-.5) rectangle (-.4,.5);',N(-.85,0,'kaynak','font=\\scriptsize,white'),
   AR((-.4,0),(.3,0),'thick')]
def yol(k,x0=.3,xe=2.6,xs=5.0):
    pts=[]; 
    for i in range(0,25):
        x=x0+(xe-x0)*i/24; pts.append((x,k*(x-x0)**2))
    y1=k*(xe-x0)**2; sl=2*k*(xe-x0); return pts,(xs,y1+sl*(xs-xe)),(xe,y1)
for k,nm in ((-.035,'X'),(0,'Y'),(.095,'Z')):
    pts,pe,pm=yol(k)
    o.append('\\draw[vurgu,very thick] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+f' -- ({pe[0]:.3f},{pe[1]:.3f});')
    o.append(N(pe[0]+.3,pe[1],nm,'font=\\small\\bfseries'))
o.append(D((5.0,-1.2),(5.0,1.9),'thick'))
SK=tikz(o)
tr2=[True,False,True]
q('0002',tipId='ra-isinim',tip=TIPLER['ra-isinim'],z='kolay',alt='Işımaların Özellikleri',kaz='Düzgün elektrik alanda sapan ve sapmayan ışımaların özelliklerini karşılaştırır.',kalip='öncüllü',
 metin='Bir radyoaktif kaynaktan çıkan ışımalar, şekilde gösterildiği gibi düzgün bir elektrik alanın bulunduğu bölgeden geçirilerek üç ayrı demete (X, Y ve Z) ayrılıyor ve ekranda üç noktaya çarpıyor.\nBuna göre,\nI. X ışımasını oluşturan parçacıkların kütlesi, Z ışımasını oluşturanlarınkinden büyüktür.\nII. Alanın yönü ters çevrilirse Y ışımasının doğrultusu değişir.\nIII. Y ışıması, üç ışıma arasında madde içine en fazla işleyendir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Demetlerin sapma yönü ve miktarı ile hiç sapmayan demetin yükü hakkında ne söylenebileceğini düşün.'],
 bilgi=[IS],
 ad=[A('X ve Z demetleri','Zıt yönlerde saparlar; Z daha çok saptığından yük ÷ kütle oranı daha büyüktür, yani daha hafif parçacıklardan oluşur.','X ağır (α), Z hafif (β⁻) → I doğru'),
     A('Y demeti','Sapmayan demet yüksüzdür; elektrik alan yük taşımayan ışımaya kuvvet uygulamaz.','Alan yönü değişse de Y sapmaz → II yanlış'),
     A('Nüfuz gücü','Yüksüz γ ışıması α ve β’dan daha fazla işler.','III doğru')],
 puf='Elektrik alanda sapmayan ışıma yüksüzdür (γ); kütlesi küçük olan parçacık aynı alanda daha çok sapar.',
 **onc(tr2,['α parçacıkları elektronlardan binlerce kat ağırdır','Y demeti yüksüz olduğundan alan yönü değişse de doğrultusu değişmez','Y demeti γ ışımasıdır ve diğerlerinden çok daha fazla işler'],4))
# ===== 03 kolay · N–t grafiği
card(3,'Yarı ömür grafiği','Grafikte N’nin yarıya indiği süre yarı ömürdür; sonraki süreler için N₀ ÷ 2ⁿ kullanılır.','Çekirdek sayısının zamanla doğrusal azaldığını ya da kalan sayıyı bölme sayısıyla bölmeyi (N₀ ÷ n) düşünmek.','kolay','grafik',3,'ra-yarisure','N–t grafiğinden yarı ömür ve kalan sayı')
T3=6; N03=800; t3=30; n3=t3//T3
assert 30%6==0 and N03//2**n3*1==25 and Fr(N03,2**n3)==25 and Fr(N03,2**4)==50 and Fr(N03,5)==160 and Fr(N03,2**6)==Fr(25,2)
f=lambda t:N03*2**(-t/T3)
pts=' '.join(f'({24*i/60:.3f},{f(24*i/60):.2f})' for i in range(61))
SK=tikz_svg(HEAD+r'''\begin{axis}[width=7.2cm,height=5cm,xmin=0,xmax=26,ymin=0,ymax=900,xtick={0,6,12,18,24},ytick={0,200,400,600,800},grid=both,major grid style={gray!50,thin},tick label style={font=\scriptsize},axis lines=left,xlabel={$t$ (gün)},ylabel={$N$},label style={font=\small},every axis y label/.style={at={(axis description cs:0,1.04)},anchor=south east}]
\addplot[very thick,vurgu] coordinates {'''+pts+r'''};
\addplot[only marks,mark=*,mark size=2pt,vurgu] coordinates {(0,800) (6,400)};
\end{axis}'''+TAIL)
q('0003',tipId='ra-yarisure',tip=TIPLER['ra-yarisure'],z='kolay',alt='Yarı Ömür',kaz='N–t grafiğinden yarı ömrü okuyarak daha sonraki bir andaki çekirdek sayısını bulur.',kalip='grafik',
 metin='Tek tür radyoaktif çekirdek içeren bir örnekte, bozunmamış çekirdek sayısı N’nin zamanla değişimi grafikte verilmiştir.\nBuna göre, t = 30 günde örnekte bozunmamış kaç çekirdek vardır?',
 sekil=SK,dogru=25,yan=[(50,'Grafiğin bittiği t = 24 gündeki değeri (800 ÷ 2⁴ = 50) 30. gündeki değer sanmış.','dikkat'),(Fr(25,2),'30 ÷ 6 = 5 yarı ömüre bir daha eklemiş: 800 ÷ 2⁶ = 12,5.','islem'),
  (100,'Üçüncü yarı ömürdeki değeri (800 ÷ 2³ = 100) almış; süreyi 18 gün saymış.','dikkat'),(160,'Başlangıç sayısını bölme sayısına bölmüş: 800 ÷ 5 = 160.','bilgi')],
 istenen='t = 30 günde bozunmamış çekirdek sayısı.',
 ip=['Grafikte sayının yarıya indiği süreyi bul; 30 günün bu süreden kaç tane içerdiğine bak.'],
 bilgi=[YO],
 ad=[A('Yarı ömrü oku','Başlangıçtaki 800 sayısı yarıya inince 400 olur; bu değer grafikte 6. günde görülür.','T = 6 gün'),
     A('Yarı ömür sayısı','Geçen süre yarı ömre bölünür.','n = 30 ÷ 6 = 5'),
     A('Kalan sayı','Her yarı ömürde sayı yarıya iner.','N = 800 ÷ 2⁵ = 25')],
 puf='Yarı ömür geçtikçe sayı N₀ ÷ 2ⁿ ile azalır; N₀ ÷ n biçiminde doğrusal azalma yoktur.')
# ===== 04 orta · bozunma zinciri (öncüllü)
card(4,'Zincirde izotop, izobar ve nötron sayısı','Her bozunmada A ve Z yeni değerleri bulunur; aynı Z izotop, aynı A izobar, N = A − Z karşılaştırılır.','β⁻ bozunmasında kütle numarasının da değiştiğini sanmak; izotop ile izobarı karıştırmak.','orta','öncüllü',4,'ra-zincir','K→L→M→N→P zinciri')
K4=(238,92); L4=dec(K4,'a'); M4=dec(L4,'b-'); N4=dec(M4,'b-'); P4=dec(N4,'a')
assert (L4,M4,N4,P4)==((234,90),(234,91),(234,92),(230,90))
nt=lambda x:x[0]-x[1]
t4=[K4[1]==N4[1],L4[0]==M4[0],nt(P4)>nt(N4)]; assert t4==[True,True,False] and nt(P4)==140 and nt(N4)==142
o=[]; xs=[0,2.3,4.6,6.9,9.2]; names=[nk(238,92,'K'),r'$\mathrm{L}$',r'$\mathrm{M}$',r'$\mathrm{N}$',r'$\mathrm{P}$']
for x,nmx in zip(xs,names): o.append(r'\node[draw,rounded corners=3pt,very thick,inner sep=5pt,minimum width=1.0cm] at ('+f'{x},0'+') {'+nmx+'};')
for i,lab in enumerate([r'$\alpha$',r'$\beta^-$',r'$\beta^-$',r'$\alpha$']): o.append(AR((xs[i]+.6,0),(xs[i+1]-.6,0))); o.append(N((xs[i]+xs[i+1])/2,.4,lab))
SK=tikz(o)
q('0004',tipId='ra-zincir',tip=TIPLER['ra-zincir'],z='orta',alt='Bozunma Zinciri',kaz='Art arda bozunmalarda çekirdeklerin kütle ve atom numaralarını izleyerek izotop, izobar ve nötron sayısı yargılarını değerlendirir.',kalip='öncüllü',
 metin='K çekirdeği art arda dört bozunma geçirerek L, M, N ve P çekirdeklerine dönüşmektedir. Bozunma türleri şekildeki oklar üzerinde gösterilmiştir.\nBuna göre,\nI. K ile N çekirdekleri izotoptur.\nII. L ile M çekirdekleri izobardır.\nIII. P çekirdeğinin nötron sayısı, N çekirdeğininkinden fazladır.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Her adımda çekirdeğin A ve Z değerini yaz; sonra izotop, izobar ve nötron sayısı tanımlarına bak.'],
 bilgi=[BZ,NZ],
 ad=[A('Zinciri izle','α: A − 4, Z − 2; β⁻: Z + 1.','K(238, 92) → L(234, 90) → M(234, 91) → N(234, 92) → P(230, 90)'),
     A('I ve II','Aynı Z izotop, aynı A izobardır.','K ve N: Z = 92 (izotop); L ve M: A = 234 (izobar) → I, II doğru'),
     A('III','Nötron sayısı A − Z ile bulunur.','N: 234 − 92 = 142; P: 230 − 90 = 140 → III yanlış')],
 puf='β⁻ bozunmasında kütle numarası değişmez (izobar kalır), atom numarası 1 artar.',
 **onc(t4,['K ile N’nin atom numaraları aynıdır (92)','L ve M’nin kütle numaraları aynıdır (234)','P’nin nötron sayısı 140, N’ninki ise 142’dir'],3))
# ===== 05 orta · Th → Pb, β⁻ sayısı
card(5,'Bozunma sayısı','Kütle numarası farkından α sayısı, atom numarası farkından β⁻ sayısı bulunur.','α sayısı ile β⁻ sayısını karıştırmak; α’nın Z’yi 2 azalttığını hesaba katmamak.','orta','grafik',3,'ra-bozunma','başlangıç ve son çekirdekten bozunma sayısı')
Xa,Xz,Ya,Yz=232,90,208,82
na=(Xa-Ya)//4; assert (Xa-Ya)%4==0; nb=Yz-(Xz-2*na); assert (na,nb)==(6,4); top=na+nb; assert top==10
assert Xz-Yz==8 and Xa-Ya==24 and len({top,na,nb,8,24})==5
SK=tikz_svg(HEAD+r'''\begin{axis}[width=7cm,height=5.2cm,xmin=204,xmax=236,ymin=80,ymax=92,xtick={208,216,224,232},ytick={82,84,86,88,90},grid=both,major grid style={gray!50,thin},tick label style={font=\scriptsize},axis lines=left,xlabel={Kütle numarası},ylabel={Atom numarası},label style={font=\small},every axis y label/.style={at={(axis description cs:0,1.04)},anchor=south east}]
\addplot[only marks,mark=*,mark size=2.6pt,vurgu] coordinates {(232,90) (208,82)};
\node[anchor=south east] at (axis cs:232,90.3) {\small X};
\node[anchor=south west] at (axis cs:208.4,82.3) {\small Y};
\end{axis}'''+TAIL)
q('0005',tipId='ra-bozunma',tip=TIPLER['ra-bozunma'],z='orta',alt='Bozunma Sayısı',kaz='Başlangıç ve son çekirdeğin numaralarından yayınlanan α ve β⁻ parçacıklarının toplam sayısını hesaplar.',kalip='grafik',
 metin='Radyoaktif bir X çekirdeği, art arda gerçekleşen bozunmalarla kararlı Y çekirdeğine dönüşmektedir. X ve Y çekirdeklerinin kütle numarası ve atom numarası grafikte noktalarla gösterilmiştir. Bu süreçte yalnızca α ve β⁻ ışıması yapılmaktadır.\nBuna göre, X’in Y’ye dönüşümü sırasında toplam kaç tane α ve β⁻ parçacığı yayınlanmıştır?',
 sekil=SK,dogru=top,yan=[(na,'Yalnız α sayısını (24 ÷ 4 = 6) yazmış; β⁻ parçacıklarını saymamış.','dikkat'),(nb,'Yalnız β⁻ sayısını (82 − 78 = 4) yazmış; α parçacıklarını saymamış.','dikkat'),
  (Xz-Yz,'Atom numarası farkını (90 − 82 = 8) bozunma sayısı sanmış.','islem'),(Xa-Ya,'Kütle numarası farkını (232 − 208 = 24) bozunma sayısı sanmış.','islem')],
 istenen='Yayınlanan α ve β⁻ parçacıklarının toplam sayısı.',
 ip=['Önce kütle numarasındaki azalmadan α sayısını bul; sonra atom numarasındaki değişimi iki tür bozunmaya paylaştır.'],
 bilgi=[BZ],
 ad=[A('α sayısı','Yalnız α kütle numarasını 4 azaltır.','n(α) = (232 − 208) ÷ 4 = 6'),
     A('β⁻ sayısı','6 α, atom numarasını 12 azaltır (90 − 12 = 78); her β⁻ atom numarasını 1 artırır ve 82’ye çıkılmıştır.','n(β⁻) = 82 − 78 = 4'),
     A('Toplam','İki türün sayıları toplanır.','6 + 4 = 10')],
 puf='Önce kütle numarası farkından α sayısını bul; kalan atom numarası farkını β⁻ ile kapat, sonra topla.')
# ===== 06 zor · iki örneğin çekirdek sayılarının eşitlenmesi
card(6,'Çekirdek sayılarının eşitlenmesi','İki örnekteki N = N₀ ÷ 2^(t ÷ T) ifadeleri eşitlenir; üsler arasındaki fark başlangıç oranına eşit olur.','Başlangıç sayıları oranını doğrudan yarı ömür sayısı sanmak; yarı ömürleri toplamak.','zor','tablo',4,'ra-yarisure','farklı yarı ömürlü iki örnek')
rows6=[('K',25600,2),('L',3200,3)]
sol=[t for t in range(1,100) if abs(25600*2**(-t/2)-3200*2**(-t/3))<1e-9]
assert sol==[18] and 25600//2**9==50==3200//2**6
assert 3*2==6 and 3*3==9 and 2+3==5 and 8*3==24 and 25600//3200==8
SK=tablo_svg(['Örnek','Başlangıçtaki çekirdek sayısı','Yarı ömür (gün)'],[[r[0],str(r[1]),str(r[2])] for r in rows6])
q('0006',tipId='ra-yarisure',tip=TIPLER['ra-yarisure'],z='zor',alt='Yarı Ömür',kaz='Farklı yarı ömürlü iki örneğin çekirdek sayılarının eşit olacağı anı bulur.',kalip='tablo',
 metin='Her biri tek tür radyoaktif çekirdek içeren K ve L örneklerinin başlangıçtaki çekirdek sayıları ile yarı ömürleri aşağıdaki tabloda verilmiştir.\nBuna göre, başlangıçtan kaç gün sonra iki örnekteki bozunmamış çekirdek sayıları ilk kez eşit olur?',
 sekil=SK,dogru=18,yan=[(6,'Başlangıç sayıları oranını (25600 ÷ 3200 = 8) K’nın üç yarı ömrü sanmış: 3 × 2 = 6.','bilgi'),(9,'Oranın 8 olduğunu düşünüp L’nin üç yarı ömrünü almış: 3 × 3 = 9.','bilgi'),
  (5,'İki yarı ömrü toplamış: 2 + 3 = 5.','islem'),(24,'Başlangıç sayıları oranını (8) süre sanıp L’nin yarı ömrüyle çarpmış: 8 × 3 = 24.','islem')],
 istenen='Çekirdek sayılarının eşitleneceği süre (gün).',
 ip=['Her örnek için kalan sayıyı t ve yarı ömürle yaz; K’nın L’den kaç kat hızlı azaldığını sayıların oranıyla ilişkilendir.'],
 bilgi=[YO],
 ad=[A('Kalan sayılar','Her örnekte sayı 2’nin kuvvetiyle bölünür.','N(K) = 25600 ÷ 2^(t ÷ 2); N(L) = 3200 ÷ 2^(t ÷ 3)'),
     A('Eşitle','Eşitlikte 2’nin kuvvetleri oranı başlangıç sayıları oranına eşittir.','2^(t ÷ 2 − t ÷ 3) = 25600 ÷ 3200 = 8 = 2³'),
     A('Süreyi bul','Üsler eşitlenir.','t ÷ 2 − t ÷ 3 = t ÷ 6 = 3 → t = 18 gün'),
     A('Kontrol','On sekizinci günde iki sayı da aynıdır.','K: 25600 ÷ 2⁹ = 50; L: 3200 ÷ 2⁶ = 50')],
 puf='İki örnek eşitlenirken “başlangıç sayıları oranı = bölünme çarpanları oranı” koşulunu yaz; üsleri eşitle.')
# ===== 07 orta · çekirdek tepkimeleri X ve Y
card(7,'Tepkimede bilinmeyen parçacıklar','Toplam A ve Z korunur; kalan A ve Z’ye göre parçacık adlandırılır.','Pozitron ile elektronu, nötron ile protonu karıştırmak.','orta','şekilli',4,'ra-tepkime','iki basamaklı yapay radyoaktiflik tepkimesi')
a1=27+4-30; z1=13+2-15; a2=30-30; z2=15-14
assert (a1,z1)==(1,0) and (a2,z2)==(0,1)
o=[N(0,.9,'I.','left'),N(.55,.9,r'$'+r'{}^{27}_{13}\mathrm{Al}+{}^{4}_{2}\mathrm{He}\rightarrow{}^{30}_{15}\mathrm{P}+\mathrm{X}$','right'),
   N(0,-.2,'II.','left'),N(.55,-.2,r'$'+r'{}^{30}_{15}\mathrm{P}\rightarrow{}^{30}_{14}\mathrm{Si}+\mathrm{Y}$','right')]
SK=tikz(o)
SR=['nötron, pozitron','proton, pozitron','nötron, elektron','proton, elektron','nötron, gama ışını']; SRS=SR[1:]+SR[:1]
q('0007',tipId='ra-tepkime',tip=TIPLER['ra-tepkime'],z='orta',alt='Çekirdek Tepkimeleri',kaz='Kütle ve yük korunumunu kullanarak çekirdek tepkimelerindeki bilinmeyen parçacıkları belirler.',kalip='şekilli',
 metin='Alüminyum bir hedef α parçacıklarıyla bombardıman edildiğinde, şekildeki I. tepkimeyle kararsız fosfor çekirdeği ve X parçacığı oluşmaktadır. Oluşan fosfor çekirdeği ise II. tepkimeyle bozunarak Y parçacığını yayınlamaktadır.\nBuna göre, X ve Y parçacıkları sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
 sekil=SK,dogru=SR[0],sira=SRS,yan=[(SR[1],'Kütle numarasının 1 olmasından X’i proton sanmış; atom numaralarının tepkimede değişmediğini (X’in yüksüz olduğunu) görmemiş.','dikkat'),
  (SR[2],'Atom numarası 15’ten 14’e inerken yayınlanan parçacığı negatif yüklü sanmış; elektron yayınlansaydı Z 16 olurdu.','bilgi'),
  (SR[3],'X için protonu, Y için elektronu seçerek hem yük korunumunu hem de Z’nin azalmasını yanlış yorumlamış.','bilgi'),
  (SR[4],'Atom numarasındaki 1 birimlik azalmayı fark etmeyip Y’yi yüksüz ve kütlesiz γ ışını sanmış.','dikkat')],
 istenen='X ve Y parçacıkları.',
 ip=['Her tepkimede sol ve sağ taraftaki kütle ve atom numaraları toplamını ayrı ayrı eşitle.'],
 bilgi=[TP],
 ad=[A('I. tepkime','A: 27 + 4 = 31 = 30 + A(X); Z: 13 + 2 = 15 = 15 + Z(X).','X: A = 1, Z = 0 → nötron'),
     A('II. tepkime','A: 30 = 30 + A(Y); Z: 15 = 14 + Z(Y).','Y: A = 0, Z = +1 → pozitron'),
     A('Sonuç','İki parçacık birlikte yazılır.','X: nötron, Y: pozitron')],
 puf='Tepkimede A ve Z toplamlarını ayrı ayrı eşitle; A = 0, Z = +1 parçacık pozitrondur, elektron değildir.')
# ===== 08 orta · uranyum fisyonu (öncüllü)
card(8,'Fisyon tepkimesi yargıları','Korunumdan bilinmeyen çekirdek bulunur; fisyonda kütle azalır ve ürünler daha sıkı bağlıdır.','Fisyon ürünlerinin bağlanma enerjisinin daha küçük olduğunu ya da kütlenin korunduğunu sanmak.','orta','öncüllü',4,'ra-fisfuz','nötronla uyarılan U fisyonu')
a8=235+1-141-3; z8=92-56; n8=a8-z8
assert (a8,z8,n8)==(92,36,56)
t8=[z8==38,True,True]; assert t8==[False,True,True]
o=[N(0,.5,r'$'+r'{}^{235}_{92}\mathrm{U}+{}^{1}_{0}\mathrm{n}\rightarrow{}^{141}_{56}\mathrm{Ba}+\mathrm{X}+3\,{}^{1}_{0}\mathrm{n}+\text{enerji}$','right')]
SK=tikz(o)
q('0008',tipId='ra-fisfuz',tip=TIPLER['ra-fisfuz'],z='orta',alt='Fisyon',kaz='Fisyon tepkimesinde korunum ve bağlanma enerjisi ilişkisini yorumlar.',kalip='öncüllü',
 metin='Düşük enerjili bir nötron, kararsız bir çekirdeğe çarparak şekilde verilen fisyon tepkimesini başlatmaktadır. Tepkimede Ba çekirdeği, X çekirdeği, üç nötron ve enerji açığa çıkmaktadır.\nBuna göre,\nI. X çekirdeğinin proton sayısı 38’dir.\nII. Girenlerin toplam kütlesi, ürünlerin toplam kütlesinden büyüktür.\nIII. Ba ve X çekirdeklerinin her birinin nükleon başına bağlanma enerjisi, ilk çekirdeğinkinden büyüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['X çekirdeğinin numaralarını korunumdan bul; enerjinin kaynağını kütle ve bağlanma enerjisi açısından düşün.'],
 bilgi=[TP,FF],
 ad=[A('X çekirdeği','Kütle numaraları ve atom numaraları toplamı korunur.','A(X) = 235 + 1 − 141 − 3 = 92; Z(X) = 92 − 56 = 36 → I yanlış'),
     A('Kütle ve enerji','Enerji açığa çıktığına göre ürünlerin kütlesi daha küçüktür.','Δm = m(giren) − m(ürün) > 0 → II doğru'),
     A('Bağlanma enerjisi','Ürünler daha kararlıdır; nükleon başına bağlanma enerjileri ağır çekirdeğinkinden büyüktür (≈ 8,4 MeV ve ≈ 7,6 MeV).','III doğru')],
 puf='Fisyonda ürünler orta kütleli çekirdeklerdir; nükleon başına bağlanma enerjisi arttığı için enerji açığa çıkar ve kütle azalır.',
 **onc(t8,['X çekirdeğinin atom numarası 92 − 56 = 36’dır','enerji açığa çıktığından girenlerin kütlesi ürünlerinkinden büyüktür','fisyon ürünleri ağır çekirdekten daha sıkı bağlıdır'],4))
# ===== 09 orta · Eb/A grafiği (öncüllü)
card(9,'Eb÷A grafiğinde enerji yönü','Tepkimede ürünlerin toplam bağlanma enerjisi girenlerinkinden büyükse enerji açığa çıkar; A ≈ 56 tepe noktasıdır.','Füzyon ve fisyonun her çekirdek için enerji verdiğini sanmak; tepe çekirdeğin bölünmesini de enerji verici saymak.','orta','öncüllü',3,'ra-baglanma','Eb ÷ A–A grafiği')
BEV=[(1,0),(2,1.11),(4,7.07),(8,7.06),(12,7.68),(16,7.98),(20,8.03),(28,8.45),(40,8.55),(56,8.79),(80,8.71),(100,8.6),(120,8.5),(160,8.2),(200,7.9),(235,7.6)]
def be_graf(pts,lab,ymax=10,xt='0,50,100,150,200,250',yt='0,2,4,6,8,10',ex=''):
    cs=' '.join(f'({a},{b})' for a,b in BEV)
    return (HEAD+r'\begin{axis}[width=7.6cm,height=5.2cm,xmin=0,xmax=250,ymin=0,ymax='+str(ymax)+r',xtick={'+xt+r'},ytick={'+yt+r'},grid=both,major grid style={gray!50,thin},tick label style={font=\scriptsize},axis lines=left,xlabel={Kütle numarası ($A$)},ylabel={$E_b \div A$ (MeV)},label style={font=\small},every axis y label/.style={at={(axis description cs:0,1.04)},anchor=south east}]'+'\n'
        r'\addplot[very thick,vurgu] coordinates {'+cs+'};\n'+ex+lab+'\n\\end{axis}'+TAIL)
lab9=(r'\addplot[only marks,mark=*,mark size=2.2pt] coordinates {(2,1.11) (4,7.07) (56,8.79) (235,7.6)};'+'\n'
      r'\node[anchor=north west,font=\small] at (axis cs:3,1.1) {${}^{2}$H};\node[anchor=north,font=\small] at (axis cs:12,6.6) {${}^{4}$He};'
      r'\node[anchor=south,font=\small] at (axis cs:56,9.0) {${}^{56}$Fe};\node[anchor=north,font=\small] at (axis cs:235,7.2) {${}^{235}$U};')
SK=tikz_svg(be_graf(None,lab9))
t9=[True,False,False]
q('0009',tipId='ra-baglanma',tip=TIPLER['ra-baglanma'],z='orta',alt='Bağlanma Enerjisi',kaz='Nükleon başına bağlanma enerjisi grafiğinden fisyon ve füzyonun enerji açığa çıkarıp çıkarmadığını yorumlar.',kalip='öncüllü',
 metin='Çekirdeklerin nükleon başına bağlanma enerjisinin (Eb ÷ A) kütle numarasına bağlı değişimi grafikte verilmiştir.\nBuna göre,\nI. İki ²H çekirdeğinin birleşerek ⁴He çekirdeğini oluşturması enerji açığa çıkarır.\nII. ⁵⁶Fe çekirdeğinin daha küçük iki çekirdeğe bölünmesi enerji açığa çıkarır.\nIII. ²³⁵U çekirdeğinin kütle numarası yaklaşık eşit iki çekirdeğe bölündüğünde, ürünlerin toplam bağlanma enerjisi ²³⁵U çekirdeğinin bağlanma enerjisinden küçüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Enerji açığa çıkması için ürünlerin toplam bağlanma enerjisinin girenlerinkinden büyük olması gerektiğini, grafikteki eğimle birleştir.'],
 bilgi=[BE,FF],
 ad=[A('Füzyon','²H’den ⁴He’ye geçişte nükleon başına bağlanma enerjisi yaklaşık 1,1’den 7,1 MeV’e çıkar.','Ürün daha sıkı bağlı → enerji açığa çıkar → I doğru'),
     A('⁵⁶Fe','Grafiğin tepe noktasıdır; bölününce nükleon başına bağlanma enerjisi küçülür.','Enerji gerekir → II yanlış'),
     A('²³⁵U fisyonu','Ürünlerin nükleon başına değeri (≈ 8,5) U’nunkinden (≈ 7,6) büyüktür, nükleon sayısı aynıdır.','Toplam bağlanma enerjisi artar → III yanlış')],
 puf='Grafiğin tepesi (A ≈ 56) en kararlı bölgedir: solda füzyon, sağda fisyon enerji açığa çıkarır.',
 **onc(t9,['iki ²H birleşince nükleon başına bağlanma enerjisi artar','⁵⁶Fe en kararlı çekirdektir; bölünmesi enerji gerektirir','ürünlerin toplam bağlanma enerjisi ²³⁵U’nunkinden büyüktür'],0))
# ===== 10 orta · Güneş kütle kaybı
card(10,'Güç ve kütle kaybı','Güç, birim zamandaki enerjidir; kütle kaybı Δm = E ÷ c² ile bulunur.','c yerine c² almamak, ya da c² ile çarpmak; üslerde hata yapmak.','orta','düz',3,'ra-enerji','Güneş’in saniyedeki kütle kaybı')
Pg=Fr(36,10)*Fr(10)**26; c=3*10**8; dm=Pg/c**2; assert dm==4*10**9
assert Pg/c==Fr(12,10)*10**18 and Pg/(3*10**16)==Fr(12,10)*10**10 and Pg/(9*10**15)==4*10**10 and Pg*c**2==Fr(324,100)*10**43
s10=[sci(4,9),sci(Fr(12,10),10),sci(4,10),sci(Fr(12,10),18),sci(Fr(324,100),43)]
q('0010',tipId='ra-enerji',tip=TIPLER['ra-enerji'],z='orta',alt='Kütle–Enerji',kaz='Çekirdek tepkimelerinde açığa çıkan gücü kütle kaybıyla ilişkilendirir.',kalip='düz',
 metin='Güneş’te gerçekleşen füzyon tepkimelerinde her saniye ortalama 3,6 × 10²⁶ J enerji açığa çıkmaktadır. Işığın boşluktaki hızı c = 3 × 10⁸ m/s alınacaktır.\nBuna göre, Güneş’in kütlesi her saniye yaklaşık kaç kg azalır?',
 sekil=None,dogru=s10[0],sira=s10,yan=[(s10[1],'c² yerine (3 × 10⁸)² = 3 × 10¹⁶ yazmış: 3,6 × 10²⁶ ÷ 3 × 10¹⁶ = 1,2 × 10¹⁰.','islem'),(s10[2],'c² değerini 9 × 10¹⁵ almış: 3,6 × 10²⁶ ÷ 9 × 10¹⁵ = 4 × 10¹⁰.','islem'),
  (s10[3],'c’nin karesini almayıp enerjiyi c ile bölmüş: 3,6 × 10²⁶ ÷ 3 × 10⁸ = 1,2 × 10¹⁸.','bilgi'),(s10[4],'Enerjiyi c² ile bölmek yerine çarpmış: 3,6 × 10²⁶ × 9 × 10¹⁶ = 3,24 × 10⁴³.','bilgi')],
 istenen='Güneş’in saniyedeki kütle kaybı (kg).',
 ip=['Enerji ile kütle arasındaki bağıntıyı yaz; ışık hızının karesinin hangi üste sahip olduğuna dikkat et.'],
 bilgi=[ME],
 ad=[A('Bağıntı','Kütle kaybı enerjinin ışık hızının karesine bölümüdür.','Δm = E ÷ c²'),
     A('Işık hızının karesi','Üs işlemi dikkatle yapılır.','c² = (3 × 10⁸)² = 9 × 10¹⁶ m²/s²'),
     A('Hesap','Saniyedeki enerji doğrudan bağıntıya yazılır.','Δm = 3,6 × 10²⁶ ÷ 9 × 10¹⁶ = 4 × 10⁹ kg')],
 puf='E = Δm × c² bağıntısında c² = 9 × 10¹⁶ alınır; bölme/çarpma ve üs işlemlerini ayrı ayrı yaz.')
# ===== 11 orta · tablo, kalan kütle
card(11,'Tablodan yarı ömür','Tablodaki iki değerden yarı ömür bulunur; hedef kütle için gereken yarı ömür sayısı kütle oranından çıkarılır.','Oranı (kütle bölümünü) doğrudan süre sanmak; yarı ömür sayısını bir eksik ya da fazla almak.','orta','tablo',3,'ra-yarisure','kütle–zaman tablosu')
T11=10; m11=[(0,960),(10,480),(30,120)]
assert all(Fr(m11[0][1],2**(t//T11))==m for t,m in m11)
n11=6; assert Fr(960,2**n11)==15 and n11*T11==60
assert 960//60==16 and T11*4==40 and T11*5==50 and T11*7==70 and Fr(960,15)==64
SK=tablo_svg(['Zaman (gün)','Bozunmamış kütle (mg)'],[[str(a),str(b)] for a,b in m11])
q('0011',tipId='ra-yarisure',tip=TIPLER['ra-yarisure'],z='orta',alt='Yarı Ömür',kaz='Tabloda verilen ölçümlerden yarı ömrü bulup belirli bir kütleye ulaşılan süreyi hesaplar.',kalip='tablo',
 metin='Tek tür radyoaktif çekirdek içeren bir örneğin bozunmamış kütlesi, farklı zamanlarda ölçülerek aşağıdaki tabloya yazılmıştır.\nBuna göre, örnekte bozunmamış kütle 15 mg olduğunda başlangıçtan kaç gün geçmiştir?',
 sekil=SK,dogru=60,yan=[(40,'Kalan kütleyi 15 mg yerine 60 mg okumuş: 960 ÷ 60 = 16 = 2⁴ olduğundan 4 × 10 = 40.','dikkat'),(50,'5 yarı ömür saymış (960 ÷ 2⁵ = 30 mg’de durmuş): 5 × 10 = 50.','islem'),
  (64,'Kütle oranını (960 ÷ 15 = 64) doğrudan süre olarak yazmış.','bilgi'),(70,'7 yarı ömür saymış (960 ÷ 2⁷ = 7,5 mg): 7 × 10 = 70.','islem')],
 istenen='Bozunmamış kütlenin 15 mg olduğu an (gün).',
 ip=['Tablodaki ilk iki satırdan yarı ömrü bul; 960 mg’ın 15 mg olması için kaç kez yarıya inmesi gerektiğini düşün.'],
 bilgi=[YO],
 ad=[A('Yarı ömür','Kütle 0. günde 960, 10. günde 480 mg’dır.','T = 10 gün'),
     A('Yarı ömür sayısı','960 ÷ 15 = 64 = 2⁶','n = 6'),
     A('Süre','Süre yarı ömür sayısı ile yarı ömrün çarpımıdır.','t = 6 × 10 = 60 gün')],
 puf='Önce yarı ömrü bul, sonra kütle oranını 2’nin kuvveti olarak yaz; üs yarı ömür sayısıdır.')
# ===== 12 orta · nüfuz deneyi (öncüllü)
card(12,'Nüfuz gücünden ışımayı tanıma','Kâğıtta duran α, alüminyumda duran β, kurşunda ancak azalan γ’dır; buna göre özellikler yorumlanır.','γ ışımasının kurşunda tamamen durduğunu ya da β’nın yüksüz olduğunu sanmak.','orta','öncüllü',3,'ra-isinim','üç kaynağın levhalardan geçişi')
o=[]
for x,w,fc,nm in ((2.4,.12,'gray!25','kâğıt'),(3.9,.3,'gray!55','alüminyum'),(5.4,.7,'gray!85','kurşun')):
    o.append(f'\\fill[{fc}] ({x-w/2:.2f},-3.1) rectangle ({x+w/2:.2f},.7);'+f'\\draw[thick] ({x-w/2:.2f},-3.1) rectangle ({x+w/2:.2f},.7);')
    o.append(N(x,1.0,nm,'font=\\scriptsize'))
for i,nm in enumerate('KLM'):
    y=-i*1.3; o.append(f'\\node[draw,thick,fill=gray!15,minimum width=.7cm,minimum height=.7cm] at (0,{y}) {{{nm}}};')
o.append(AR((.4,0),(2.25,0))); o.append(AR((.4,-1.3),(3.7,-1.3))); o.append(AR((.4,-2.6),(5.0,-2.6)))
o.append(D((5.8,-2.6),(7.3,-2.6),'vurgu,thin')); o.append(f'\\draw[vurgu,thin,{ARR}] (6.9,-2.6) -- (7.3,-2.6);')
SK=tikz(o)
t12=[True,True,True]
q('0012',tipId='ra-isinim',tip=TIPLER['ra-isinim'],z='orta',alt='Işımaların Nüfuz Gücü',kaz='Levhalardan geçiş gözleminden ışımaların türünü belirleyip özelliklerini karşılaştırır.',kalip='öncüllü',
 metin='K, L ve M radyoaktif kaynaklarının her biri yalnızca tek tür ışıma yayınlamaktadır. Şekilde, her kaynağın ışıması kâğıt, alüminyum ve kurşun levhalardan geçirilirken ışımanın nerede durduğu (ok ucu) gösterilmiştir. M’nin ışıması kurşun levhadan sonra zayıflamış olarak çıkmaktadır.\nBuna göre,\nI. K’nin yaydığı ışımanın iyonlaştırma gücü, L ve M’ninkilerden büyüktür.\nII. L’nin yaydığı ışıma elektrik alanda sapar.\nIII. M’nin yaydığı ışıma elektromanyetik dalgadır.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Levhaların ışımayı durdurma sırasına bakarak her kaynağın hangi tür ışıma yaydığını belirle.'],
 bilgi=[IS],
 ad=[A('Işımaları tanı','K kâğıtta, L alüminyumda durur; M kurşunu bile geçer.','K: α, L: β, M: γ'),
     A('I','En az işleyen ışımanın iyonlaştırma gücü en büyüktür.','K (α) en çok iyonlaştırır → I doğru'),
     A('II ve III','β parçacıkları yüklüdür, γ ise elektromanyetik dalgadır.','II doğru, III doğru')],
 puf='Kâğıtta duran α, alüminyumda duran β; kurşunu geçen γ’dır. Nüfuz gücü arttıkça iyonlaştırma gücü azalır.',
 **onc(t12,['kâğıtta duran α, iyonlaştırması en büyük ışımadır','alüminyumda duran β parçacıkları yüklüdür ve alanda sapar','kurşunu geçen γ ışıması elektromanyetik dalgadır'],4))
# ===== 13 orta · N–Z düzleminde zincir, A farkı
def nz(pts,arrs,N0,N1,Z0,Z1,s=.62,lab={}):
    o=[]
    for n in range(N0,N1+1): o.append(f'\\draw[gray!45,thin] ({(n-N0)*s:.3f},0) -- ({(n-N0)*s:.3f},{(Z1-Z0)*s:.3f});'); o.append(N((n-N0)*s,-.28,str(n),'font=\\scriptsize'))
    for z in range(Z0,Z1+1): o.append(f'\\draw[gray!45,thin] (0,{(z-Z0)*s:.3f}) -- ({(N1-N0)*s:.3f},{(z-Z0)*s:.3f});'); o.append(N(-.3,(z-Z0)*s,str(z),'font=\\scriptsize'))
    o.append(D((0,0),((N1-N0)*s+.3,0),'thick')); o.append(D((0,0),(0,(Z1-Z0)*s+.3),'thick'))
    o.append(N((N1-N0)*s+.45,-.28,'$N$','font=\\small')); o.append(N(-.3,(Z1-Z0)*s+.5,'$Z$','font=\\small'))
    P_={k:((v[0]-N0)*s,(v[1]-Z0)*s) for k,v in pts.items()}
    for a,b in arrs:
        (x1,y1),(x2,y2)=P_[a],P_[b]; d=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/d,(y2-y1)/d
        o.append(AR((x1+ux*.12,y1+uy*.12),(x2-ux*.12,y2-uy*.12),'vurgu,thick'))
    for k,(x,y) in P_.items():
        o.append(DOT((x,y),2.4)); dx,dy=lab.get(k,(.0,.28)); o.append(N(x+dx,y+dy,k,'font=\\small\\bfseries'))
    return o
card(13,'N–Z düzleminde bozunma türü','Okun yönünden bozunma türü anlaşılır: (−2, −2) α, (−1, +1) β⁻; A = N + Z değişimi bulunur.','β⁻ bozunmasında A’nın da azaldığını sanmak; okların sayısıyla α sayısını karıştırmak.','orta','şekilli',4,'ra-zincir','N–Z düzleminde dört adımlı zincir')
pt13={'K':(146,92),'L':(144,90),'M':(143,91),'P':(141,89),'R':(140,90)}
A13={k:v[0]+v[1] for k,v in pt13.items()}
assert A13=={'K':238,'L':234,'M':234,'P':230,'R':230} and A13['K']-A13['R']==8
tp13=[('K','L'),('L','M'),('M','P'),('P','R')]
ty13=[]
for a,b in tp13:
    d=(pt13[b][0]-pt13[a][0],pt13[b][1]-pt13[a][1]); ty13.append({(-2,-2):'a',(-1,1):'b-',(1,-1):'b+'}[d])
assert ty13==['a','b-','a','b-']
SK=tikz(nz(pt13,tp13,139,147,88,93,lab={'K':(.0,.3),'L':(-.28,-.1),'M':(.28,.12),'P':(-.28,-.1),'R':(-.28,.12)}))
q('0013',tipId='ra-zincir',tip=TIPLER['ra-zincir'],z='orta',alt='N–Z Düzlemi',kaz='N–Z düzlemindeki okların yönünden bozunma türlerini belirleyip kütle numarası değişimini bulur.',kalip='şekilli',
 metin='K çekirdeği art arda gerçekleşen dört bozunmayla R çekirdeğine dönüşmektedir. Çekirdeklerin nötron sayısı (N) ve proton sayısı (Z), şekildeki düzlemde nokta ile gösterilmiştir.\nBuna göre, R çekirdeğinin kütle numarası K çekirdeğininkinden kaç eksiktir?',
 sekil=SK,dogru=8,yan=[(4,'Yalnızca bir α bozunması saymış: 1 × 4 = 4.','dikkat'),(10,'α’da 4, β⁻’da 1 azalma varsaymış: 2 × 4 + 2 × 1 = 10.','bilgi'),(12,'Dört bozunmanın üçünü α saymış: 3 × 4 = 12.','dikkat'),(16,'Dört bozunmanın hepsinde kütle numarasının 4 azaldığını sanmış: 4 × 4 = 16.','bilgi')],
 istenen='K ile R arasındaki kütle numarası farkı.',
 ip=['Her okun nötron ve proton sayısındaki değişimine bakarak bozunmanın türünü belirle.'],
 bilgi=[NZ,BZ],
 ad=[A('Bozunma türleri','(N, Z) değişimi: K→L (−2, −2), L→M (−1, +1), M→P (−2, −2), P→R (−1, +1).','α, β⁻, α, β⁻'),
     A('Kütle numaraları','Yalnız α, kütle numarasını 4 azaltır; β⁻’da değişmez.','A(K) = 146 + 92 = 238; A(R) = 140 + 90 = 230'),
     A('Fark','İki α bozunması vardır.','238 − 230 = 8')],
 puf='N–Z düzleminde (−2, −2) adımı α, (−1, +1) adımı β⁻ demektir; yalnız α kütle numarasını değiştirir.')
# ===== 14 zor · N–Z düzleminde yargılar (öncüllü)
card(14,'N–Z düzleminde yön ve çekirdek ilişkileri','Okların yönü bozunma türünü, noktaların koordinatları izotop/izobar ilişkisini verir.','β⁺ ile β⁻ yönünü karıştırmak; izobar ile izotopu karıştırmak.','zor','öncüllü',5,'ra-zincir','β⁻, α, β⁺ adımlı zincir')
pt14={'X$_1$':(118,80),'X$_2$':(117,81),'X$_3$':(115,79),'X$_4$':(116,78)}
k1,k2,k3,k4='X$_1$','X$_2$','X$_3$','X$_4$'
tp14=[(k1,k2),(k2,k3),(k3,k4)]
ty14=[]
for a_,b_ in tp14:
    d=(pt14[b_][0]-pt14[a_][0],pt14[b_][1]-pt14[a_][1]); ty14.append({(-2,-2):'a',(-1,1):'b-',(1,-1):'b+'}[d])
assert ty14==['b-','a','b+']
A14={k:v[0]+v[1] for k,v in pt14.items()}; assert A14[k3]==A14[k4]==194 and A14[k1]==198
t14=[ty14[0]=='b+',A14[k3]==A14[k4],A14[k1]==A14[k3]]
assert t14==[False,True,False]
SK=tikz(nz(pt14,tp14,114,119,77,82,s=.8,lab={k1:(.0,.34),k2:(.0,.34),k3:(-.42,0),k4:(.42,-.05)}))
q('0014',tipId='ra-zincir',tip=TIPLER['ra-zincir'],z='zor',alt='N–Z Düzlemi',kaz='N–Z düzlemindeki bozunma zincirinde bozunma türlerini ve çekirdekler arası ilişkileri değerlendirir.',kalip='öncüllü',
 metin='X₁ çekirdeği art arda üç bozunma geçirerek X₂, X₃ ve X₄ çekirdeklerine dönüşmektedir. Çekirdeklerin nötron sayısı (N) ve proton sayısı (Z) şekildeki düzlemde gösterilmiştir.\nBuna göre,\nI. X₁ → X₂ bozunmasında yayınlanan parçacığın yükü pozitiftir.\nII. X₃ → X₄ bozunmasında kütle numarası değişmez.\nIII. X₁ ile X₃ çekirdekleri izobardır.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Her okun (N, Z) değişiminden bozunma türünü bul; izobar için kütle numarası A = N + Z’yi hesapla.'],
 bilgi=[NZ,BZ],
 ad=[A('Bozunma türleri','X₁→X₂: (−1, +1); X₂→X₃: (−2, −2); X₃→X₄: (+1, −1).','β⁻, α, β⁺'),
     A('I ve II','β⁻ negatif yüklü elektron yayar; β⁺ yalnız Z’yi 1 azaltır, A sabit kalır.','I yanlış, II doğru'),
     A('III','A(X₁) = 118 + 80 = 198; A(X₃) = 115 + 79 = 194.','Kütle numaraları farklı → III yanlış')],
 puf='N–Z düzleminde yön, bozunma türünü verir: (+1, −1) β⁺, (−1, +1) β⁻, (−2, −2) α; yalnız α kütle numarasını değiştirir.',
 **onc(t14,['X₁→X₂ adımı (−1, +1) olduğundan β⁻ yayınlanır ve yük negatiftir','X₃→X₄ adımı (+1, −1) olduğundan A = N + Z değişmez','X₁’in kütle numarası 198, X₃’ünki 194’tür'],0))
# ===== 15 orta · yarı ömür kavramları (öncüllü)
card(15,'Yarı ömür kavramı','Yarı ömür dış koşullardan bağımsızdır; aktivite kalan çekirdek sayısıyla orantılı ve yarı ömrü kısa olanda daha büyüktür.','Isıtmayla bozunmanın hızlanacağını ya da kısa yarı ömürlü örneğin daha uzun süre kalacağını sanmak.','orta','öncüllü',3,'ra-yarisure','yarı ömür ve aktivite yargıları')
t15=[False,True,False]
q('0015',tipId='ra-yarisure',tip=TIPLER['ra-yarisure'],z='orta',alt='Yarı Ömür',kaz='Yarı ömür ve aktivite kavramlarını farklı örnekler için karşılaştırır.',kalip='öncüllü',
 metin='Aynı sayıda radyoaktif çekirdek içeren, yarı ömürleri farklı iki örnekten K’nın yarı ömrü L’ninkinden kısadır.\nBuna göre,\nI. K örneği ısıtılırsa yarı ömrü kısalır.\nII. Başlangıçta K örneğinin bozunma hızı (aktivitesi) L’ninkinden büyüktür.\nIII. Aynı süre sonunda K örneğindeki bozunmamış çekirdek sayısı, L örneğindekinden fazladır.\nyargılarından hangileri doğrudur?',
 sekil=None,istenen='Doğru yargılar.',
 ip=['Yarı ömrün hangi koşullara bağlı olduğunu ve kısa yarı ömrün bozunma hızıyla ilişkisini düşün.'],
 bilgi=[YO],
 ad=[A('I','Yarı ömür çekirdeğin kendi özelliğidir; sıcaklık, basınç ya da kimyasal bağdan etkilenmez.','I yanlış'),
     A('II','Yarı ömrü kısa olan çekirdek birim zamanda daha çok bozunur; aynı sayıda çekirdekte aktivite daha büyüktür.','II doğru'),
     A('III','K daha hızlı bozunduğundan aynı sürede daha çok çekirdeği bozunmuş, daha azı kalmıştır.','III yanlış')],
 puf='Yarı ömür dış koşullara bağlı değildir; kısa yarı ömür demek, daha hızlı bozunma ve daha büyük aktivite demektir.',
 **onc(t15,['yarı ömür sıcaklık gibi dış koşullardan bağımsızdır','yarı ömrü kısa olan örneğin aktivitesi aynı sayıdaki çekirdekte daha büyüktür','yarı ömrü kısa olan örnekte aynı sürede daha az çekirdek kalır'],0))
# ===== 16 zor · yaş tayini
card(16,'Radyoaktif yaş tayini','Ana ve yavru çekirdek sayıları toplamı başlangıçtaki ana çekirdek sayısıdır; kalan oranı 1/2ⁿ ise n yarı ömür geçmiştir.','Pb ÷ U oranını doğrudan yarı ömür sayısı sanmak.','zor','şekilli',4,'ra-yarisure','U–Pb oranından kayanın yaşı')
Uq,Pq=2,6; frac=Fr(Uq,Uq+Pq); assert frac==Fr(1,4); n16=2; assert Fr(1,2**n16)==frac
T16=Fr(45,10); yas=n16*T16; assert yas==9
assert T16==Fr(9,2) and 3*T16==Fr(27,2) and 4*T16==18 and 8*T16==36 and T16*1==Fr(9,2)
o=[D((-.4,0),(5.4,0),'thick'),
   r'\fill[gray!55] (.5,0) rectangle (1.7,.9);',r'\draw[thick] (.5,0) rectangle (1.7,.9);',
   r'\fill[vurgu!70] (3.2,0) rectangle (4.4,2.7);',r'\draw[thick] (3.2,0) rectangle (4.4,2.7);',
   N(1.1,1.25,r'$2\times10^{20}$','font=\\small'),N(3.8,3.05,r'$6\times10^{20}$','font=\\small'),
   N(1.1,-.4,r'${}^{238}\mathrm{U}$'),N(3.8,-.4,r'${}^{206}\mathrm{Pb}$'),N(2.45,-1.0,'atom sayısı','font=\\scriptsize')]
SK=tikz(o)
q('0016',tipId='ra-yarisure',tip=TIPLER['ra-yarisure'],z='zor',alt='Yaş Tayini',kaz='Ana ve yavru çekirdek sayılarından kalan oranını bulup kayanın yaşını hesaplar.',kalip='şekilli',
 metin='Bir kaya örneğinde bulunan ²³⁸U ve ²⁰⁶Pb atomlarının sayıları şekilde verilmiştir. Kaya oluştuğunda içinde ²⁰⁶Pb yoktur; örnekteki ²⁰⁶Pb atomlarının tümü ²³⁸U çekirdeklerinin bozunmasıyla oluşmuştur ve ara ürünlerin yarı ömürleri ihmal edilmektedir. ²³⁸U’nun yarı ömrü 4,5 milyar yıldır.\nBuna göre, kayanın yaşı kaç milyar yıldır?',
 sekil=SK,dogru=yas,yan=[(Fr(9,2),'Bozunan sayısının (6) kalan sayısının (2) üç katı olduğunu görüp yalnız bir yarı ömür geçtiğini sanmış: 4,5.','bilgi'),
  (Fr(27,2),'Pb ÷ U = 3 olduğundan 3 yarı ömür geçtiğini düşünmüş: 3 × 4,5 = 13,5.','dikkat'),(18,'Toplam atom sayısının U sayısına oranını (8 ÷ 2 = 4) yarı ömür sayısı almış: 4 × 4,5 = 18.','dikkat'),
  (36,'Pb ÷ U = 3 oranını 2’nin kuvveti sanıp 2³ = 8 yarı ömür hesaplamış: 8 × 4,5 = 36.','islem')],
 istenen='Kayanın yaşı (milyar yıl).',
 ip=['Kayanın oluştuğu andaki ²³⁸U sayısını, Pb atomlarının nereden geldiğini düşünerek belirle.'],
 bilgi=[YT,YO],
 ad=[A('Başlangıçtaki U sayısı','Her Pb atomu bir U çekirdeğinin bozunmasından gelmiştir.','N₀ = 2 × 10²⁰ + 6 × 10²⁰ = 8 × 10²⁰'),
     A('Kalan oranı','Kalan U sayısının başlangıca oranı 2’nin kuvvetidir.','2 ÷ 8 = ¼ = (½)²'),
     A('Yaş','İki yarı ömür geçmiştir.','t = 2 × 4,5 = 9 milyar yıl')],
 puf='Yaş tayininde kalan ana çekirdek sayısını başlangıç sayısıyla (ana + yavru) karşılaştır; Pb ÷ U oranını doğrudan yarı ömür sayısı yapma.')
# ===== 17 zor · proton–proton zinciri
card(17,'Füzyon zincirinde sayım','Zincirin sonunda bir ⁴He için ilk iki tepkime ikişer kez gerçekleşir; ışımalar bu sayıya göre sayılır.','Her tepkimeyi bir kez saymak ya da nötrinoyu da sayıma katmak.','zor','şekilli',4,'ra-fisfuz','proton–proton zinciri')
r1,r2,r3=2,2,1
assert 2*r3==r2==r1  # iki ³He için ilk iki tepkime ikişer kez
pozitron=r1; foton=r2; nu=r1; toplam=pozitron+foton; assert toplam==4
assert (1+1,2+1,toplam,toplam+1,toplam+nu)==(2,3,4,5,6)
o=[N(0,1.3,'I.','left'),N(.6,1.3,r'${}^{1}_{1}\mathrm{H}+{}^{1}_{1}\mathrm{H}\rightarrow{}^{2}_{1}\mathrm{H}+{}^{\;0}_{+1}\mathrm{e}+\nu$','right'),
   N(0,.35,'II.','left'),N(.6,.35,r'${}^{2}_{1}\mathrm{H}+{}^{1}_{1}\mathrm{H}\rightarrow{}^{3}_{2}\mathrm{He}+\gamma$','right'),
   N(0,-.6,'III.','left'),N(.6,-.6,r'${}^{3}_{2}\mathrm{He}+{}^{3}_{2}\mathrm{He}\rightarrow{}^{4}_{2}\mathrm{He}+2\,{}^{1}_{1}\mathrm{H}$','right')]
SK=tikz(o)
q('0017',tipId='ra-fisfuz',tip=TIPLER['ra-fisfuz'],z='zor',alt='Füzyon',kaz='Füzyon zincirinde tepkimelerin tekrar sayısını belirleyip yayınlanan parçacıkları sayar.',kalip='şekilli',
 metin='Yıldızlarda hidrojenin helyuma dönüştüğü zincirin üç tepkimesi şekilde verilmiştir. Zincir yalnızca bu üç tepkimeden oluşmakta ve tam olarak bir tane ⁴₂He çekirdeği oluşana kadar sürmektedir. Tepkimelerde yayınlanan parçacıklardan pozitronlar ile γ fotonlarının sayısı birlikte düşünülecektir; nötrinolar sayılmayacaktır.\nBuna göre, bu süreçte yayınlanan pozitron ve γ fotonlarının toplam sayısı kaçtır?',
 sekil=SK,dogru=4,yan=[(2,'Her tepkimenin bir kez gerçekleştiğini düşünmüş: 1 pozitron + 1 foton = 2.','dikkat'),(3,'I. tepkimeyi iki kez, II. tepkimeyi bir kez saymış: 2 + 1 = 3.','islem'),
  (5,'III. tepkimede de bir foton yayınlandığını varsayıp 2 + 2 + 1 = 5 bulmuş.','bilgi'),(6,'Nötrinoları da sayıma katmış: 2 pozitron + 2 foton + 2 nötrino = 6.','dikkat')],
 istenen='Yayınlanan pozitron ve γ fotonlarının toplam sayısı.',
 ip=['III. tepkimeden başlayarak, bir ⁴He için gereken ³He sayısını ve bunların hangi tepkimelerle oluştuğunu geriye doğru say.'],
 bilgi=[FF,TP],
 ad=[A('III. tepkime','Bir ⁴He için iki ³He gerekir.','III: 1 kez'),
     A('II. tepkime','Her ³He bir II. tepkimeden gelir.','II: 2 kez → 2 foton'),
     A('I. tepkime','Her II. tepkime için bir ²H, yani bir I. tepkime gerekir.','I: 2 kez → 2 pozitron'),
     A('Toplam','Pozitron ve fotonlar toplanır; III. tepkimede ışıma yoktur.','2 + 2 = 4')],
 puf='Zincirde sayımı sondan başa yap: ürünü oluşturan tepkime sayısından önceki tepkimelerin tekrar sayısını çıkar.')
# ===== 18 zor · bağlanma enerjisinden fisyon enerjisi
card(18,'Bağlanma enerjisi farkıyla fisyon enerjisi','Açığa çıkan enerji = ürünlerin toplam bağlanma enerjisi − girenin toplam bağlanma enerjisi; her biri A × (Eb ÷ A) ile bulunur.','Nükleon başına farkı toplam enerji sanmak; yalnız tek ürünü hesaba katmak; tüm ürünlere aynı değeri uygulamak.','zor','grafik',4,'ra-baglanma','Eb ÷ A grafiğinden fisyon enerjisi')
Ag=[(236,Fr(76,10)),(140,Fr(84,10)),(96,Fr(87,10))]
assert Ag[1][0]+Ag[2][0]==Ag[0][0]
E18=Ag[1][0]*Ag[1][1]+Ag[2][0]*Ag[2][1]-Ag[0][0]*Ag[0][1]; assert E18==Fr(2176,10)
v1=Ag[0][0]*(Ag[1][1]-Ag[0][1]); v2=Ag[0][0]*(Ag[2][1]-Ag[0][1]); v3=Ag[1][0]*(Ag[1][1]-Ag[0][1])
assert (v1,v2,v3)==(Fr(1888,10),Fr(2596,10),112) and len({E18,v1,v2,v3,Ag[1][0]*Ag[1][1]+Ag[2][0]*Ag[2][1]})==5
lab18=(r'\addplot[only marks,mark=*,mark size=2.4pt] coordinates {(96,8.7) (140,8.4) (236,7.6)};'+'\n'
       r'\draw[dashed] (axis cs:96,0) -- (axis cs:96,8.7);\draw[dashed] (axis cs:140,0) -- (axis cs:140,8.4);\draw[dashed] (axis cs:236,0) -- (axis cs:236,7.6);'+'\n'
       r'\node[anchor=south,font=\small] at (axis cs:96,8.95) {$8{,}7$};\node[anchor=south west,font=\small] at (axis cs:140,8.55) {$8{,}4$};\node[anchor=south,font=\small] at (axis cs:236,7.75) {$7{,}6$};')
SK=tikz_svg(be_graf(None,lab18,xt='0,96,140,236',yt='0,2,4,6,8,10'))
q('0018',tipId='ra-baglanma',tip=TIPLER['ra-baglanma'],z='zor',alt='Bağlanma Enerjisi',kaz='Nükleon başına bağlanma enerjisi grafiğinden fisyon sırasında açığa çıkan toplam enerjiyi hesaplar.',kalip='grafik',
 metin='Kütle numarası 236 olan kararsız bir çekirdek, nötron yayınlamadan kütle numaraları 140 ve 96 olan iki çekirdeğe bölünmektedir. Bu üç çekirdeğin nükleon başına bağlanma enerjisi (Eb ÷ A) grafikte işaretlenmiştir.\nBuna göre, bu bölünmede açığa çıkan enerji kaç MeV’dir?',
 sekil=SK,dogru=E18,yan=[(v1,'Ürünlerin ikisi için de 8,4 MeV kullanıp 236 × (8,4 − 7,6) = 188,8 bulmuş.','islem'),(v2,'Ürünlerin ikisi için de 8,7 MeV kullanıp 236 × (8,7 − 7,6) = 259,6 bulmuş.','islem'),
  (v3,'Yalnız 140 nükleonlu ürünün kazancını hesaplamış: 140 × (8,4 − 7,6) = 112.','dikkat'),(Ag[1][0]*Ag[1][1]+Ag[2][0]*Ag[2][1],'Ürünlerin toplam bağlanma enerjisini (1176 + 835,2 = 2011,2) açığa çıkan enerji sanmış.','bilgi')],
 istenen='Açığa çıkan enerji (MeV).',
 ip=['Bir çekirdeğin toplam bağlanma enerjisinin grafikteki değerden nasıl bulunacağını ve açığa çıkan enerjinin neye bağlı olduğunu düşün.'],
 bilgi=[BE],
 ad=[A('Ürünlerin bağlanma enerjisi','Her ürün için A × (Eb ÷ A).','140 × 8,4 + 96 × 8,7 = 1176 + 835,2 = 2011,2 MeV'),
     A('Girenin bağlanma enerjisi','236 nükleonun her biri 7,6 MeV ile bağlıdır.','236 × 7,6 = 1793,6 MeV'),
     A('Fark','Açığa çıkan enerji ürünlerle girenin bağlanma enerjileri farkıdır.','2011,2 − 1793,6 = 217,6 MeV')],
 puf='Fisyon enerjisini nükleon başına farktan değil, ürünler ve girenin toplam bağlanma enerjilerinin farkından hesapla.')
# ===== 19 orta · reaktörde fisyon sayısı
card(19,'Reaktör gücünden fisyon sayısı','Saniyedeki fisyon sayısı = güç ÷ bir fisyonun enerjisi (joule).','MeV’i joule’e çevirirken üssü yanlış almak ya da MeV yerine eV kullanmak.','orta','düz',3,'ra-fisfuz','reaktörde saniyedeki fisyon sayısı')
Pr=Fr(32,10)*10**8; Ef=200*Fr(16,10)*Fr(1,10**13); rate=Pr/Ef; assert Ef==Fr(32,10)*Fr(1,10**11) and rate==10**19
def rt(E): return Pr/E
assert rt(200*Fr(16,10)*Fr(1,10**10))==10**16 and rt(200*Fr(16,10)*Fr(1,10**16))==10**22 and rt(20*Fr(16,10)*Fr(1,10**13))==10**20 and rt(200*Fr(16,10)*Fr(1,10**19))==10**25
s19=[f'10{str(k).translate(SUP)}' for k in (16,19,20,22,25)]
q('0019',tipId='ra-fisfuz',tip=TIPLER['ra-fisfuz'],z='orta',alt='Fisyon',kaz='Nükleer reaktörün gücünden birim zamandaki fisyon sayısını hesaplar.',kalip='düz',
 metin='Bir nükleer reaktörde ²³⁵U çekirdeklerinin her fisyonunda ortalama 200 MeV enerji açığa çıkmaktadır. Reaktörün ısıl gücü sabit olup 3,2 × 10⁸ W’tır ve bu enerjinin tamamı fisyonlardan gelmektedir. 1 MeV = 1,6 × 10⁻¹³ J alınacaktır.\nBuna göre, reaktörde her saniye yaklaşık kaç fisyon gerçekleşir?',
 sekil=None,dogru=s19[1],sira=s19,yan=[(s19[0],'1 MeV’i 1,6 × 10⁻¹⁰ J almış: 3,2 × 10⁸ ÷ (200 × 1,6 × 10⁻¹⁰) = 10¹⁶.','islem'),(s19[2],'Fisyon başına enerjiyi 200 yerine 20 MeV almış: 3,2 × 10⁸ ÷ (20 × 1,6 × 10⁻¹³) = 10²⁰.','islem'),
  (s19[3],'1 MeV’i 1,6 × 10⁻¹⁶ J almış: 3,2 × 10⁸ ÷ (200 × 1,6 × 10⁻¹⁶) = 10²².','islem'),(s19[4],'200 MeV yerine 200 eV kullanmış (1 eV = 1,6 × 10⁻¹⁹ J): 3,2 × 10⁸ ÷ (200 × 1,6 × 10⁻¹⁹) = 10²⁵.','dikkat')],
 istenen='Reaktörde saniyedeki fisyon sayısı.',
 ip=['Gücün ve bir fisyonun enerjisinin aynı birimde olması gerektiğini düşün.'],
 bilgi=[FF,ME],
 ad=[A('Birim dönüşümü','1 MeV değeri joule cinsinden yazılır.','1 MeV = 1,6 × 10⁻¹³ J'),
     A('Bir fisyonun enerjisi','200 MeV joule’e çevrilir.','E = 200 × 1,6 × 10⁻¹³ = 3,2 × 10⁻¹¹ J'),
     A('Saniyedeki fisyon sayısı','Güç, saniyedeki toplam enerjidir.','n = P ÷ E = 3,2 × 10⁸ ÷ 3,2 × 10⁻¹¹ = 10¹⁹')],
 puf='Reaktör gücü, fisyon başına enerji ile saniyedeki fisyon sayısının çarpımıdır; önce MeV’i joule’e çevir.')
# ===== 20 zor · α bozunmasında momentum ve kinetik enerji
card(20,'Alfa bozunmasında enerji paylaşımı','Momentumlar eşit büyüklükte olduğundan kinetik enerjiler kütlelerle ters orantılıdır; hafif parçacık enerjinin büyük kısmını alır.','Enerjinin eşit paylaşıldığını ya da kütle ile doğru orantılı bölüneceğini sanmak.','zor','şekilli',4,'ra-bozunma','durgun çekirdeğin α bozunması')
Q20=Fr(52,10); mA,mP=4,204; Ea=Q20*mP/(mP+mA); Ep=Q20*mA/(mP+mA); assert Ea==Fr(51,10) and Ep==Fr(1,10) and Ea+Ep==Q20 and Ea/Ep==51
assert Q20/2==Fr(26,10) and Q20/4==Fr(13,10) and Q20*mA/208==Fr(1,10)
o=[r'\node[draw,rounded corners=3pt,very thick,inner sep=6pt] at (0,1.6) {${}^{208}\mathrm{Po}$ (durgun)};',
   N(-2.3,1.6,'önce','font=\\small,right'),N(-2.3,-.55,'sonra','font=\\small,right'),
   r'\draw[dashed,gray] (-3.0,.5) -- (4.6,.5);',
   r'\node[draw,rounded corners=3pt,very thick,inner sep=6pt] (b) at (0,-.55) {${}^{204}\mathrm{Pb}$};',
   r'\node[draw,rounded corners=3pt,very thick,inner sep=5pt] (c) at (2.2,-.55) {$\alpha$};',
   AR((-.8,-.55),(-1.3,-.55)),AR((2.9,-.55),(4.5,-.55))]
SK=tikz(o)
q('0020',tipId='ra-bozunma',tip=TIPLER['ra-bozunma'],z='zor',alt='Bozunmada Enerji Paylaşımı',kaz='Momentum korunumunu kullanarak α bozunmasında parçacıkların kinetik enerjilerini hesaplar.',kalip='şekilli',
 metin='Durgun hâldeki bir Po çekirdeği, şekilde gösterildiği gibi α parçacığı yayınlayarak Pb çekirdeğine dönüşmektedir. Bozunmada açığa çıkan enerjinin tamamı α parçacığı ile Pb çekirdeğinin kinetik enerjisine dönüşmekte ve bu enerji toplamı 5,2 MeV’dir. Parçacıkların kütleleri kütle numaralarıyla orantılı alınacaktır.\nBuna göre, α parçacığının kinetik enerjisi kaç MeV’dir?',
 sekil=SK,dogru=Ea,yan=[(Q20/2,'Enerjinin iki parçacık arasında eşit paylaşıldığını düşünmüş: 5,2 ÷ 2 = 2,6.','bilgi'),(Fr(1,10),'Kinetik enerjileri kütleyle doğru orantılı sanıp α’nın payını 4 ÷ 208 almış: 5,2 × 4 ÷ 208 = 0,1.','bilgi'),
  (Q20/4,'Toplam enerjiyi α’nın kütle numarası olan 4’e bölmüş: 5,2 ÷ 4 = 1,3.','islem'),(Q20,'Pb çekirdeğinin hareketsiz kaldığını varsayıp tüm enerjiyi α’ya vermiş.','dikkat')],
 istenen='α parçacığının kinetik enerjisi (MeV).',
 ip=['Bozunma öncesi toplam momentum sıfırdır; iki parçacığın momentum büyüklüklerinin kinetik enerjilerle ilişkisini kur.'],
 bilgi=[MO,BZ],
 ad=[A('Momentum korunumu','Durgun çekirdekte toplam momentum sıfırdır; parçacıkların momentum büyüklükleri eşittir.','p(α) = p(Pb)'),
     A('Enerji oranı','K = p² ÷ 2m olduğundan kinetik enerjiler kütlelerle ters orantılıdır.','K(α) ÷ K(Pb) = 204 ÷ 4 = 51'),
     A('Paylaşım','Toplam 5,2 MeV, 51 : 1 oranında bölünür.','K(α) = 5,2 × 51 ÷ 52 = 5,1 MeV')],
 puf='Durgun çekirdeğin bozunmasında hafif parçacık, enerjinin büyük kısmını alır: kinetik enerjiler kütlelerle ters orantılıdır.')
# ===== yaz
for qq in P.ANA: qq['kardes']=None
SC=os.path.join(os.environ.get('RADYO_SC','/tmp'),'bos-radyo.json')
P.yaz(os.path.join(GD,'radyo-1.json'),SC)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Radyoaktivite'))['kartlar'].append(c['id'])
json.dump(dict(konu='Radyoaktivite',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Fizik (yalnız mantık), 345 AYT Fizik, Bilgi Sarmal AYT Fizik, MEB 12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afradyo.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
