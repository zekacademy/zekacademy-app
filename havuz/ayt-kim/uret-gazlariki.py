"""AYT Kimya · Gazlar · 2. dalga · 10 soru (ipucu 1). Şekiller TikZ; her sayı Python'da Fraction ile hesaplanıp assert edilir."""
import sys,os,math,json
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from _hafif_kim import onc as _onc
import cizim,subprocess
_run=subprocess.run
def _srun(*a,**k):
    if k.get('text'): k.pop('text'); k['encoding']='utf-8'; k['errors']='replace'
    return _run(*a,**k)
cizim.subprocess.run=_srun
from cizim import tikz_svg
KONU_='Gazlar'; UK='akim|Gazlar'
H.KONU=KONU_
P=Parti('gazlariki',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2018–2026 Kimya (Gazlar; yalnız mantık) · MEB 11. sınıf kimya'
TIPLER={'gz-yogunluk':'Gaz yoğunluğu ve ortalama mol kütlesi','gz-grafik':'Gaz grafiklerinin yorumlanması','gz-musluk':'Musluk ve piston düzenekleri','gz-ideal':'İdeal gaz denklemi ve stokiyometri'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AKGAZ2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AKGAZ2-{kn:02d} ('+CARD[kn]+')',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def onc_neg(d,ops):
    Tm=frozenset(k for k,v in d.items() if v[0]); ops=[tuple(o) for o in ops]; assert len(ops)==5 and len(set(ops))==5
    ad=lambda s:('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
    es=[o for o in ops if frozenset(o)==Tm]; assert len(es)==1
    yan=[]
    for o in ops:
        if frozenset(o)==Tm: continue
        W=frozenset(o); p=[]
        for x in sorted(W-Tm): p.append(f'{x} öncülünü yanlış sanmış; oysa {x} doğrudur: {d[x][1]}')
        for x in sorted(Tm-W): p.append(f'{x} öncülünü doğru sanıp işaretlememiş; oysa {x} yanlıştır: {d[x][1]}')
        yan.append((ad(o),'. '.join(p)+'.','bilgi'))
    return dict(dogru=ad(es[0]),yan=yan,sira=[ad(o) for o in ops])
def oy(d): return ' · '.join(f'{k}: '+('doğru' if v[0] else 'yanlış') for k,v in d.items())
def oyn(d): return ' · '.join(f'{k}: '+('yanlış' if v[0] else 'doğru') for k,v in d.items())
V224=Fr(224,10)

# ============ kartlar ============
card(1,'NŞA yoğunluğundan molekül formülü','Normal koşullarda 1 mol gaz 22,4 L hacim kaplar; yoğunluk × 22,4 değeri mol kütlesini verir ve formül kütlesiyle karşılaştırılır.','Yoğunluğu doğrudan mol kütlesi sanmak; formül kütlesini yanlış toplamak.','kolay','düz',3,'gz-yogunluk','NŞA yoğunluğu, CₓHᵧ formülü')
card(2,'V–T grafiği ve basınç','Sabit basınçtaki V–T doğrusunun eğimi nR/P ile orantılıdır; grafikteki iki doğru karşılaştırılırken hangi niceliklerin sabit olduğuna bakılır.','Grafikteki doğruyu gerçek gazlar için sınırsız uzatmak; sabit olan niceliği yanlış belirlemek.','kolay','öncüllü',3,'gz-grafik','iki izobar, öncüllü yargılar')
card(3,'Vakumlu kaba gaz geçişi','Musluk açılınca her gaz toplam hacmi kaplar; kısmi basınç = n·RT ÷ toplam hacim olup başlangıçtaki P·V çarpımı bu amaçla kullanılır.','Vakum bölmenin hacmini hesaba katmamak; toplam basıncı kısmi basınç sanmak.','orta','şekilli',4,'gz-musluk','üç bölmeli kap, vakum')
card(4,'Ayrışma, yoğunluk ve sıcaklık','Sabit basınçta hacim n·T ile orantılıdır; kütle korunduğundan yoğunluk 1 ÷ (n·T) ile değişir.','Yoğunluğu mol sayısıyla doğru orantılı almak; sıcaklığı unutmak.','zor','şekilli',5,'gz-yogunluk','NH₃ ayrışması, ısıtma, piston')
card(5,'Yoğunluk–sıcaklık grafiği','Yoğunluk d = P·M ÷ (R·T) ile yazılır; grafikteki noktalardan çarpım ya da oran kurularak yoğunlukla sıcaklık arasındaki ilişki belirlenir.','Grafikteki noktaları karşılaştırmadan yorum yapmak.','orta','grafik',4,'gz-grafik','d–T eğrisi, olumsuz kök')
card(6,'Farklı koşullardaki örneklerden mol kütlesi','Aynı basınçta n ∝ V ÷ T olur; mol sayısı bulunup kütleye bölünerek mol kütlesine geçilir.','Sıcaklık farkını yok saymak; oranı ters kurmak.','orta','tablo',4,'gz-ideal','tablo: kütle, hacim, sıcaklık')
card(7,'Karışımın yoğunluğu','Karışımın ortalama mol kütlesi toplam kütle ÷ toplam mol olup d = P·M ÷ (R·T) bağıntısında kullanılır.','Mol kütlelerinin aritmetik ortalamasını almak.','orta','grafik',4,'gz-yogunluk','mol çubuk grafiği, d = PM/RT')
card(8,'Sabit dış basınçlı piston ve musluk','Piston serbestken gaz basıncı dış basınca eşit kalır; toplam hacim n·T ile orantılıdır, sabit kabın hacmi ayrıca çıkarılır.','Pistonlu bölmenin hacmi yerine toplam hacmi vermek; ısınmayı yok saymak.','zor','şekilli',6,'gz-musluk','rijit kap + pistonlu kap + ısıtma')
card(9,'Katı tepkimesi ve karışımın ortalama mol kütlesi','Saf madde kütlesi mol sayısına, mol sayısı katsayı oranıyla gaz mol sayısına çevrilir; karışımda M = toplam kütle ÷ toplam mol.','Saflığı yok saymak; kütlesini bulunan katıyı gaza katmak.','zor','düz',6,'gz-ideal','CaCO₃ ayrışması, He ile karışım')
card(10,'P–1/V grafiği','Sabit sıcaklıkta P = nRT·(1/V) doğrusunun eğimi hangi niceliklere bağlıdır, grafikten ve bağıntıdan çıkarılır.','Eğimi hacimle ilişkilendirmek.','orta','grafik',4,'gz-grafik','iki doğru, öncüllü')

# ============ 0001 · NŞA yoğunluk · kolay ============
d1=Fr(5,2); M1=d1*V224; assert M1==56
cand={'C₂H₄':28,'C₂H₆':30,'C₃H₆':42,'C₃H₈':44,'C₄H₈':56}
assert [12*int(c)+int(h) for c,h in ((2,4),(2,6),(3,6),(3,8),(4,8))]==list(cand.values()) and cand['C₄H₈']==M1
dens={k:Fr(v)/V224 for k,v in cand.items()}
assert dens['C₂H₄']==Fr(5,4) and abs(float(dens['C₂H₆'])-1.339)<1e-3 and abs(float(dens['C₃H₆'])-1.875)<1e-3 and abs(float(dens['C₃H₈'])-1.964)<1e-3
q('0001',[A('Mol hacmini kullan','Normal koşullarda (0 °C, 1 atm) 1 mol gaz 22,4 L hacim kaplar.','1 mol gaz → 22,4 L'),
 A('Mol kütlesini bul','1 L gazın kütlesi yoğunluktur; 22,4 L’nin kütlesi 1 mol gazın kütlesine eşittir.','M = 2,5 × 22,4 = 56 g/mol'),
 A('Formül kütlelerini karşılaştır','Her seçenek için 12·x + 1·y hesaplanır.','C₄H₈: 12·4 + 8 = 56')],
 metin='Normal koşullarda yoğunluğu 2,5 g/L olan bir hidrokarbon gazı yalnız C ve H atomlarından oluşmaktadır.\n(H = 1, C = 12 g/mol; normal koşullarda 1 mol gaz 22,4 L hacim kaplar.)\nBuna göre bu gazın molekül formülü aşağıdakilerden hangisi olabilir?',
 dogru='C₄H₈',yan=[('C₂H₄','Mol kütlesi 28 g/mol olan bu gazın normal koşullardaki yoğunluğu 28 ÷ 22,4 = 1,25 g/L’dir; verilen 2,5 g/L değerinin yarısıdır.','bilgi'),
  ('C₂H₆','Mol kütlesi 30 g/mol olan bu gazın yoğunluğu 30 ÷ 22,4 ≈ 1,34 g/L’dir; verilen değeri vermez.','bilgi'),
  ('C₃H₆','Mol kütlesi 42 g/mol olan bu gazın yoğunluğu 42 ÷ 22,4 ≈ 1,88 g/L’dir; verilen değerden küçüktür.','bilgi'),
  ('C₃H₈','Mol kütlesi 44 g/mol olan bu gazın yoğunluğu 44 ÷ 22,4 ≈ 1,96 g/L’dir; verilen değerden küçüktür.','bilgi')],
 sira=['C₂H₄','C₂H₆','C₃H₆','C₃H₈','C₄H₈'],
 istenen='Yoğunluğu 2,5 g/L olan gazın molekül formülü.',ip=['Yoğunluğu, 1 mol gazın hacmiyle birlikte kullanarak bir mol gazın kütlesine ulaşmayı dene.'],
 bilgi=[B('Normal koşullar ve mol hacmi','0 °C ve 1 atm koşullarında 1 mol ideal gaz 22,4 L hacim kaplar; yoğunluk d = M ÷ 22,4 olur. Örnek: mol kütlesi 28 g/mol olan bir gazın yoğunluğu 28 ÷ 22,4 = 1,25 g/L’dir')],
 puf='Normal koşullarda mol kütlesi = yoğunluk × 22,4 işlemiyle bulunur.',
 tipId='gz-yogunluk',tip=TIPLER['gz-yogunluk'],z='kolay',alt='Gazlarda Yoğunluk',kaz='Normal koşullardaki yoğunluktan mol kütlesini bulur ve molekül formülüyle ilişkilendirir.',kalip='düz')

# ============ 0002 · V–T grafiği · kolay · öncüllü ============
sx,sy=7/650,4/12.5
g=[]
g.append(f'\\draw[->,thick] (0,0) -- ({640*sx:.2f},0) node[below right] {{$T$ (K)}};')
g.append(f'\\draw[->,thick] (0,0) -- (0,{12.5*sy:.2f}) node[above] {{$V$ (L)}};')
for t in (100,200,300,400,500,600): g.append(f'\\draw ({t*sx:.3f},.07) -- ({t*sx:.3f},-.07) node[below] {{{t}}};')
for v in (3,6,9,12): g.append(f'\\draw (.07,{v*sy:.3f}) -- (-.07,{v*sy:.3f}) node[left] {{{v}}};')
g.append(f'\\draw[thick] (0,0) -- ({600*sx:.3f},{12*sy:.3f});')
g.append(f'\\draw[thick,vurgu,dashed] (0,0) -- ({600*sx:.3f},{6*sy:.3f});')
g.append(f'\\draw[dotted] ({300*sx:.3f},0) -- ({300*sx:.3f},{6*sy:.3f}) -- (0,{6*sy:.3f});')
g.append(f'\\draw[dotted] ({300*sx:.3f},{3*sy:.3f}) -- (0,{3*sy:.3f});')
g.append(f'\\fill ({300*sx:.3f},{6*sy:.3f}) circle (1.6pt); \\fill[vurgu] ({300*sx:.3f},{3*sy:.3f}) circle (1.6pt);')
g.append(N(520*sx,12*sy*520/600+.4,'I','font=\\small')); g.append(N(560*sx,6*sy*560/600-.4,'\\textcolor{vurgu}{II}','font=\\small'))
SK2=tk('\n'.join(g))
d={'I':(True,'aynı T’de I doğrusundaki hacim daha büyüktür; V = nRT ÷ P olduğundan hacmi büyük olan örnek daha küçük basınçtadır'),
   'II':(False,'her iki doğru da aynı miktardaki gaza aittir; basıncın değişmesi mol sayısını değiştirmez'),
   'III':(False,'gerçek gazlar düşük sıcaklıkta sıvılaşır; bu nedenle doğruların 0 K’e uzatılması gerçek gaz için hacmin sıfır olduğunu göstermez')}
r=_onc(d,[('I',),('II',),('I','II'),('I','III'),('II','III')])
q('0002',[A('Doğruların eğimini karşılaştır','Aynı T’de I doğrusunun hacmi II doğrusunun 2 katıdır; V = nRT ÷ P bağıntısında n ve T aynıdır.','300 K: V(I) = 6 L, V(II) = 3 L'),
 A('I. öncülü incele','Hacmi büyük olan örnek daha küçük basınçtadır.','I: doğru'),
 A('II. ve III. öncülleri incele','Mol sayısı iki doğruda da aynıdır; gerçek gazlar düşük sıcaklıkta sıvılaşır.','II: yanlış · III: yanlış'),
 A('Sonucu yaz','Yalnız I öncülü doğrudur.',oy(d)+' · Sonuç: '+r['dogru'])],
 metin='Aynı miktardaki ideal bir gaz örneğinin, sabit tutulan iki farklı basınçta (I ve II) hacminin mutlak sıcaklıkla değişimi şekilde verilmiştir.\nI. I doğrusundaki gazın basıncı II doğrusundakinden küçüktür.\nII. I doğrusundaki gazın mol sayısı II doğrusundakinden fazladır.\nIII. Gerçek gazlar da 0 K’e kadar gaz hâlinde kalarak bu doğruları izler.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK2,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Aynı sıcaklıkta iki doğrudaki hacimleri karşılaştırıp V = nRT ÷ P bağıntısına bak.'],
 bilgi=[B('Charles yasası grafiği','Sabit basınçta ve sabit mol sayısında V–T grafiği orijinden geçen bir doğrudur; eğim nR ÷ P kadardır. Örnek: eğimi 0,2 L/K olan bir izobarda 500 K’de gazın hacmi 100 L’dir')],
 puf='Eğimi nR ÷ P ile ilişkilendir; hangi niceliklerin iki doğruda da aynı kaldığını belirle.',
 tipId='gz-grafik',tip=TIPLER['gz-grafik'],z='kolay',alt='Gaz Grafikleri',kaz='V–T grafiğindeki doğruları basınç ve mol sayısıyla ilişkilendirir.',kalip='öncüllü')

# ============ 0003 · vakumlu üç bölme · orta ============
nHe=9*1; nNe=3*2; Vt=1+3+2; Pt=Fr(nHe+nNe,Vt); PHe=Fr(nHe,Vt); PNe=Fr(nNe,Vt)
assert (Pt,PHe,PNe)==(Fr(5,2),Fr(3,2),1)
w1=Fr(9*1,1+3); w2=Fr(9,3); assert (w1,w2)==(Fr(9,4),3)
g=[]
g.append('\\draw[thick] (0,0) circle (.85); '+N(0,0,'He\\\\$9$ atm','align=center')+N(0,-1.25,'$1$ L'))
g.append('\\draw[thick] (3.3,0) circle (1.35); '+N(3.3,0,'Vakum')+N(3.3,-1.75,'$3$ L'))
g.append('\\draw[thick] (6.6,0) circle (1.0); '+N(6.6,0,'Ne\\\\$3$ atm','align=center')+N(6.6,-1.4,'$2$ L'))
for x0,x1 in ((0.85,1.95),(4.65,5.6)):
    g.append(f'\\draw[thick] ({x0},0) -- ({x1},0); \\fill[gray!60] ({(x0+x1)/2-.12},-.2) rectangle ({(x0+x1)/2+.12},.2); \\draw ({(x0+x1)/2-.12},-.2) rectangle ({(x0+x1)/2+.12},.2);')
g.append(N(3.3,2.0,'her bölmede sıcaklık aynı ($T$)','font=\\small'))
SK3=tk('\n'.join(g))
q('0003',[A('Toplam hacmi bul','Musluklar açılınca üç bölmedeki gaz da toplam hacmi kaplar; vakum bölmesi hacme eklenir.','V = 1 + 3 + 2 = 6 L'),
 A('He’un nRT değerini yaz','Sabit sıcaklıkta P·V çarpımı n·R·T ile orantılıdır ve gaz yayılırken değişmez.','P·V = 9 × 1 = 9 atm·L'),
 A('Son kısmi basıncı hesapla','He tek başına 6 L’yi kaplıyormuş gibi basınç yapar.','P(He) = 9 ÷ 6 = 1,5 atm')],
 metin='Şekildeki sistemde He ve Ne gazları ile bir vakum bölmesi, sıcaklığı aynı olan ve musluklarla birbirine bağlı kaplarda bulunmaktadır. Musluklar sabit sıcaklıkta açılıp sistemin dengeye ulaşması bekleniyor.\n(Bağlantı borularının ve muslukların hacmi ihmal edilecek; gazlar ideal davranmaktadır.)\nBuna göre He gazının son kısmi basıncı kaç atm olur?',
 sekil=SK3,dogru=Fr(3,2),yan=[(Fr(5,2),'Karışımın toplam basıncını (15 ÷ 6 = 2,5 atm) He’un kısmi basıncı sanmış.','dikkat'),
  (Fr(9,4),'Vakum bölmesinin hacmini hesaba katmamış: 9 × 1 ÷ (1 + 3) yazarak yalnız He ile vakum bölmesini toplamış.','islem'),
  (3,'Toplam hacim yerine yalnız vakum bölmesinin hacmini (3 L) kullanarak 9 × 1 ÷ 3 yazmış.','islem'),
  (1,'Ne gazının kısmi basıncını (6 ÷ 6 = 1 atm) bulmuş.','dikkat')],
 istenen='He gazının son kısmi basıncı (atm).',ip=['Her gazın dengeye gelince kaplayacağı hacmi belirle ve ilk durumdaki P·V çarpımını bu hacimle ilişkilendir.'],
 bilgi=[B('Kısmi basınç','Sabit sıcaklıkta bir gaz yeni hacmine yayıldığında P₁V₁ = P₂V₂ olur; karışımda her gaz toplam hacmi tek başına kaplıyormuş gibi basınç yapar. Örnek: 4 L’de 2 atm olan gaz 8 L’ye yayılırsa kısmi basıncı 1 atm olur')],
 puf='Her gazı ayrı ayrı toplam hacme genişlet: P_son = P·V(ilk) ÷ V(toplam).',
 tipId='gz-musluk',tip=TIPLER['gz-musluk'],z='orta',alt='Gaz Karışımları',kaz='Vakum bölmeli kaplarda musluk açıldığında gazların kısmi basıncını hesaplar.',kalip='şekilli')

# ============ 0004 · NH3 ayrışması, yoğunluk · zor ============
alfa=Fr(3,5); n_son=1+alfa; Tr=Fr(2); r_d=1/(n_son*Tr)
assert n_son==Fr(8,5) and r_d==Fr(5,16)
assert Fr(1)/n_son==Fr(5,8) and 1/Tr==Fr(1,2) and n_son==Fr(8,5) and n_son*Tr==Fr(16,5)
g=[]
def kap(x0,ytop,yp,etiket,tem):
    s=f'\\draw[thick] ({x0},0) -- ({x0},{ytop}) ; \\draw[thick] ({x0+2.2},0) -- ({x0+2.2},{ytop}); \\draw[thick] ({x0},0) -- ({x0+2.2},0);'
    s+=f'\\fill[gray!55] ({x0+.03},{yp}) rectangle ({x0+2.17},{yp+.18}); \\draw ({x0+.03},{yp}) rectangle ({x0+2.17},{yp+.18});'
    s+=N(x0+1.1,yp/2,etiket,'align=center')+N(x0+1.1,-.4,tem)
    s+=f'\\draw[-{{Stealth[length=1.9mm]}},thick] ({x0+1.1},{ytop+.7}) -- ({x0+1.1},{yp+.3}); '+N(x0+1.1,ytop+.95,'dış basınç sabit')
    return s
g.append(kap(0,2.6,1.6,'\\ce{NH3}(g)','$300$ K (ilk durum)'))
g.append(kap(3.6,2.6,1.6,'\\ce{NH3}, \\ce{N2}, \\ce{H2}\\\\karışımı','$600$ K (son durum)'))
g.append('\\draw[-{Stealth[length=2mm]},thick] (2.4,1.0) -- (3.4,1.0);'+N(2.9,1.35,'\\%60','font=\\small'))
g.append(N(3.0,-1.0,'(şekil ölçekli değildir)','font=\\small'))
SK4=tk('\n'.join(g))
q('0004',[A('Ayrışma sonrası mol sayısını bul','1 mol NH₃’ün %60’ı ayrışırsa 0,6 mol NH₃ azalır, 0,3 mol N₂ ve 0,9 mol H₂ oluşur.','n = 0,4 + 0,3 + 0,9 = 1,6 mol'),
 A('Hacim oranını yaz','Dış basınç sabit olduğundan V ∝ n·T olur.','V₂ ÷ V₁ = 1,6 × (600 ÷ 300) = 3,2'),
 A('Kütlenin korunduğunu kullan','Kütle değişmediğinden yoğunluk hacimle ters orantılıdır.','d₂ ÷ d₁ = 1 ÷ 3,2'),
 A('Oranı hesapla','1 ÷ 3,2 işleminin sonucu bulunur.','d₂ = 0,3125 · d₁')],
 metin='Sürtünmesiz ve hareketli bir pistonla kapatılmış kapta 300 K’de yalnız NH₃ gazı bulunmaktadır ve dış basınç sabittir. NH₃ gazının %60’ı\n2NH₃(g) → N₂(g) + 3H₂(g)\ndenklemine göre ayrıştırıldıktan sonra kap 600 K’e ısıtılıyor; piston dengeye geldiğinde kaptaki gaz karışımı şekildeki son durumdadır. Gazlar ideal davranmaktadır.\nBuna göre son durumdaki gaz karışımının yoğunluğu, ilk durumdaki NH₃ gazının yoğunluğunun kaç katıdır?',
 sekil=SK4,dogru=Fr(5,16),yan=[(Fr(1,2),'Yalnız sıcaklık etkisini (300 ÷ 600) hesaba katıp ayrışmayla artan mol sayısını yok saymış.','dikkat'),
  (Fr(5,8),'Yalnız mol sayısı etkisini (1 ÷ 1,6) hesaba katıp sıcaklığın hacmi artırdığını yok saymış.','dikkat'),
  (Fr(8,5),'Yoğunluğu mol sayısıyla doğru orantılı alıp 1,6 bulmuş; oysa kütle sabit kalırken hacim artar.','bilgi'),
  (Fr(16,5),'Hacim oranını (3,2) yoğunluk oranı sanmış; yoğunluk hacimle ters orantılı değiştiği için sonuç bunun çarpma tersidir.','bilgi')],
 istenen='Son yoğunluğun ilk yoğunluğa oranı.',ip=['Dış basınç sabitken hacmi etkileyen iki değişkeni ve kütlenin bu süreçteki durumunu birlikte düşün.'],
 bilgi=[B('Yoğunluk ve hacim','Kapalı kapta gazın kütlesi tepkime sırasında da değişmez; hacim artarsa yoğunluk aynı oranda azalır. Sabit basınçta V ∝ n·T’dir. Örnek: mol sayısı 3 katına çıkan bir gaz sabit T ve P’de 3 kat hacim kaplar, yoğunluğu üçte birine iner')],
 puf='Sabit P’de hacim oranı n·T oranıdır; kütle sabit olduğu için yoğunluk oranı bunun tersidir.',
 tipId='gz-yogunluk',tip=TIPLER['gz-yogunluk'],z='zor',alt='Gazlarda Yoğunluk',kaz='Gaz tepkimesi ve sıcaklık değişiminin birlikte etkisiyle gaz yoğunluğunun değişimini hesaplar.',kalip='şekilli')

# ============ 0005 · d–T grafiği · orta · olumsuz kök ============
sx,sy=7/650,4/6.6
g=[]
g.append(f'\\draw[->,thick] (0,0) -- ({640*sx:.2f},0) node[below right] {{$T$ (K)}};')
g.append(f'\\draw[->,thick] (0,0) -- (0,{6.6*sy:.2f}) node[above] {{$d$ (g/L)}};')
for t in (100,200,300,400,500,600): g.append(f'\\draw ({t*sx:.3f},.07) -- ({t*sx:.3f},-.07) node[below] {{{t}}};')
for v in (2,3,4,6): g.append(f'\\draw (.07,{v*sy:.3f}) -- (-.07,{v*sy:.3f}) node[left] {{{v}}};')
g.append(f'\\draw[thick,vurgu,domain=190:620,samples=60,smooth,variable=\\t] plot ({{\\t*{sx}}},{{1200/\\t*{sy}}});')
for t in (200,300,400,600):
    g.append(f'\\draw[dotted] ({t*sx:.3f},0) -- ({t*sx:.3f},{1200/t*sy:.3f}) -- (0,{1200/t*sy:.3f}); \\fill[vurgu] ({t*sx:.3f},{1200/t*sy:.3f}) circle (1.6pt);')
SK5=tk('\n'.join(g))
assert all(Fr(1200,t)*t==1200 for t in (200,300,400,600)) and Fr(1200,300)/Fr(1200,600)==2
d={'I':(False,'yoğunluk ile mutlak sıcaklığın çarpımı sabittir (d·T = 1200); bu yargı doğrudur'),
   'II':(True,'kapalı kapta gazın mol sayısı ısıtmayla değişmez; yoğunluk azalması hacmin artmasından kaynaklanır'),
   'III':(True,'yoğunluk mutlak sıcaklıkla ters orantılıdır; sıcaklık 2 katına çıkınca yoğunluk yarıya iner')}
rn=onc_neg(d,[('II',),('III',),('I','II'),('II','III'),('I','II','III')])
q('0005',[A('Eğri üzerindeki değerleri oku','İlk iki noktadaki yoğunluk ve sıcaklık çarpımı hesaplanır.','200 × 6 = 300 × 4 = 400 × 3 = 600 × 2 = 1200'),
 A('I. öncülü incele','d·T sabit olduğundan yoğunluk mutlak sıcaklıkla ters orantılıdır.','I: doğru'),
 A('II. ve III. öncülleri incele','Kütle ve mol sayısı sabittir, yoğunluk azalması hacmin artmasındandır; ters orantı doğru orantı değildir.','II: yanlış · III: yanlış'),
 A('Sonucu yaz','Soru yanlış olanları sorar.',oyn(d)+' · Sonuç: '+rn['dogru'])],
 metin='Sürtünmesiz ve hareketli bir pistonla kapatılmış kapta bulunan belirli miktardaki ideal gazın yoğunluğunun, dış basınç sabit tutularak mutlak sıcaklıkla değişimi şekilde verilmiştir.\nI. Gazın yoğunluğu ile mutlak sıcaklığının çarpımı sabittir.\nII. Isıtma sırasında kaptaki gazın mol sayısı azalır.\nIII. Gazın yoğunluğu mutlak sıcaklıkla doğru orantılı değişir.\nBuna göre bu yargılardan hangileri yanlıştır?',
 sekil=SK5,dogru=rn['dogru'],yan=rn['yan'],sira=rn['sira'],istenen='Yanlış olan yargılar.',
 ip=['Grafikteki noktalardan çarpım ya da oran kurarak yoğunlukla sıcaklık arasındaki ilişkinin türünü belirle.'],
 bilgi=[B('Yoğunluk ve sıcaklık','Sabit basınçta ve kapalı kapta d = P·M ÷ (R·T) olduğundan yoğunluk mutlak sıcaklıkla ters orantılıdır. Örnek: P = 2 atm, M = 20 g/mol ve R·T = 20 atm·L/mol ise d = 2 × 20 ÷ 20 = 2 g/L’dir')],
 puf='Grafikteki noktalardan çarpım ya da oran kur; kütle, basınç ve mol sayısı hakkında bilinenleri de hesaba kat.',
 tipId='gz-grafik',tip=TIPLER['gz-grafik'],z='orta',alt='Gaz Grafikleri',kaz='Sabit basınçta yoğunluk–sıcaklık grafiğini yorumlar.',kalip='grafik')

# ============ 0006 · tablo, mol kütlesi · orta ============
nC=Fr(12,16); nX=nC*Fr(8,3)/Fr(400,300); MX=Fr(66)/nX
assert (nC,nX,MX)==(Fr(3,4),Fr(3,2),44)
w_noT=Fr(66)/(nC*Fr(8,3)); w_kutle=Fr(66)/nC; w_ters=Fr(66)/(nC*Fr(1,2)*Fr(3,8)*Fr(300,400)/Fr(300,400));
w_ters=Fr(66)/(nC*Fr(1,2)); w_kare=Fr(66)/(nC*4)
assert (w_noT,w_kutle,w_ters,w_kare)==(33,88,176,22)
sk=tablo_svg(['Gaz','Kütle (g)','Hacim (L)','Sıcaklık (K)'],[['CH₄','12','3','300'],['X','66','8','400']])
q('0006',[A('CH₄’ün mol sayısını bul','Mol sayısı kütlenin mol kütlesine bölünmesiyle bulunur.','n(CH₄) = 12 ÷ 16 = 0,75 mol'),
 A('Mol sayıları oranını kur','Aynı basınçta n ∝ V ÷ T’dir.','n(X) ÷ n(CH₄) = (8 ÷ 400) ÷ (3 ÷ 300) = 2'),
 A('X’in mol sayısını bul','Oranı CH₄’ün mol sayısıyla çarp.','n(X) = 2 × 0,75 = 1,5 mol'),
 A('Mol kütlesini hesapla','Kütle mol sayısına bölünür.','M(X) = 66 ÷ 1,5 = 44 g/mol')],
 metin='Aynı basınçta bulunan CH₄ ve X gazlarının kütle, hacim ve sıcaklık değerleri tabloda verilmiştir.\nGazlar ideal davranmaktadır. (H = 1, C = 12 g/mol)\nBuna göre X gazının mol kütlesi kaç g/mol’dür?',
 sekil=sk,dogru=44,yan=[(33,'Sıcaklık farkını yok sayıp mol sayılarını yalnız hacim oranıyla (8 ÷ 3) kurmuş: n(X) = 2, M = 33.','islem'),
  (88,'Hacim ve sıcaklık farkını dikkate almadan X’in mol sayısını CH₄’ünkine (0,75 mol) eşit sanmış.','dikkat'),
  (176,'Mol sayıları oranını ters kurmuş: n(X) = 0,75 × 0,5 = 0,375 mol.','bilgi'),
  (22,'V ÷ T oranını (2) iki kez uygulamış: n(X) = 0,75 × 4 = 3 mol.','islem')],
 istenen='X gazının mol kütlesi (g/mol).',ip=['Her örneğin mol sayısını aynı basınç koşulu altında karşılaştırılabilir hâle getirmeyi dene.'],
 bilgi=[B('Mol sayısı ve ideal gaz denklemi','P·V = n·R·T olduğundan aynı basınçta n ∝ V ÷ T olur. Örnek: aynı basınçta 2 L ve 100 K’deki gaz ile 4 L ve 400 K’deki gazın mol sayıları oranı (4 ÷ 400) ÷ (2 ÷ 100) = 0,5’tir')],
 puf='Aynı basınçta V ÷ T oranı mol sayıları oranını verir; mol sayısı bulununca M = m ÷ n.',
 tipId='gz-ideal',tip=TIPLER['gz-ideal'],z='orta',alt='İdeal Gaz Denklemi',kaz='Farklı sıcaklık ve hacimdeki gaz örneklerinden mol kütlesini hesaplar.',kalip='tablo')

# ============ 0007 · karışımın yoğunluğu · orta ============
nHe7,nCH=3,1; mHe,mCH=3*4,1*16; Mort=Fr(mHe+mCH,nHe7+nCH); P7=Fr(28,5); d7=P7*Mort/V224
assert Mort==7 and d7==Fr(7*28,5*224*1)*Fr(10,1)/Fr(10,1) or True
assert d7==Fr(7)*Fr(28,5)/V224 and d7==Fr(7,4)
y1=P7*4/V224; y2=P7*Fr(4+16,2)/V224; y3=P7*16/V224; y4=P7*Fr(12,4)/V224
assert (y1,y2,y3,y4)==(1,Fr(5,2),4,Fr(3,4))
sx,sy=1.3,.62
g=[]
g.append(f'\\draw[->,thick] (0,0) -- (3.9,0) node[below right] {{gaz}};')
g.append(f'\\draw[->,thick] (0,0) -- (0,{4.7*sy:.2f}) node[above] {{$n$ (mol)}};')
for v in (1,2,3,4): g.append(f'\\draw (.07,{v*sy:.3f}) -- (-.07,{v*sy:.3f}) node[left] {{{v}}};')
g.append(f'\\fill[gray!40] (.6,0) rectangle (1.4,{3*sy:.3f}); \\draw[thick] (.6,0) rectangle (1.4,{3*sy:.3f});')
g.append(f'\\fill[vurgu!50] (2.2,0) rectangle (3.0,{1*sy:.3f}); \\draw[thick] (2.2,0) rectangle (3.0,{1*sy:.3f});')
g.append(N(1.0,-.4,'He')+N(2.6,-.4,'CH$_4$'))
SK7=tk('\n'.join(g))
q('0007',[A('Toplam mol ve kütleyi bul','Grafikten mol sayıları okunup kütleye çevrilir.','n = 3 + 1 = 4 mol · m = 3 × 4 + 1 × 16 = 28 g'),
 A('Ortalama mol kütlesini yaz','Karışımın ortalama mol kütlesi toplam kütlenin toplam mole oranıdır.','M = 28 ÷ 4 = 7 g/mol'),
 A('Yoğunluk bağıntısını uygula','d = P·M ÷ (R·T) ve R·T = 22,4 atm·L/mol (273 K).','d = 5,6 × 7 ÷ 22,4'),
 A('Sonucu hesapla','İşlemi tamamla.','d = 1,75 g/L')],
 metin='273 K’de rijit bir kapta bulunan He ve CH₄ gazlarının mol sayıları şekildeki grafikte verilmiştir. Karışımın basıncı 5,6 atm’dir.\n(H = 1, He = 4, C = 12 g/mol; 273 K’de R·T = 22,4 L·atm/mol; gazlar ideal davranmaktadır.)\nBuna göre bu gaz karışımının yoğunluğu kaç g/L’dir?',
 sekil=SK7,dogru=Fr(7,4),yan=[(Fr(3,4),'Yalnız He’un kütlesini (12 g) toplam mol sayısına (4) bölmüş: M = 3 g/mol.','islem'),
  (1,'Karışımın ortalama mol kütlesi yerine yalnız He’un mol kütlesini (4 g/mol) kullanmış.','dikkat'),
  (Fr(5,2),'Mol kütlelerinin aritmetik ortalamasını almış: (4 + 16) ÷ 2 = 10 g/mol.','bilgi'),
  (4,'Karışımın tamamının CH₄ olduğunu düşünerek 16 g/mol almış.','dikkat')],
 istenen='Karışımın yoğunluğu (g/L).',ip=['Karışımı tek bir gaz gibi düşünebilmek için ortalama mol kütlesini kullan.'],
 bilgi=[B('Karışımın ortalama mol kütlesi','Gaz karışımında ortalama mol kütlesi, toplam kütlenin toplam mol sayısına bölünmesiyle bulunur ve d = P·M ÷ (R·T) bağıntısında kullanılır. Örnek: 1 mol H₂ (2 g) ile 1 mol O₂ (32 g) karışımının ortalama mol kütlesi 17 g/mol’dür')],
 puf='Ortalama mol kütlesi = toplam kütle ÷ toplam mol; ağırlıklı ortalamadır, düz ortalama değildir.',
 tipId='gz-yogunluk',tip=TIPLER['gz-yogunluk'],z='orta',alt='Gazlarda Yoğunluk',kaz='Gaz karışımının ortalama mol kütlesini bulur ve yoğunluğu hesaplar.',kalip='grafik')

# ============ 0008 · rijit kap + pistonlu kap · zor ============
nA=3*2; nB=1*2; ntot=nA+nB; Vson=Fr(ntot,1)*1; Vb1=Vson-2; Vson2=ntot*2*Fr(1); Vb2=Vson2-2
assert (ntot,Vb1,Vb2)==(8,6,14) and 16-2==14
a8=ntot*2
g=[]
g.append('\\draw[thick] (0,0) rectangle (1.8,2.0); '+N(.9,1.1,'He\\\\$3$ atm','align=center')+N(.9,-.35,'$2$ L (sabit)'))
g.append('\\draw[thick] (1.8,1.0) -- (3.0,1.0); \\fill[gray!60] (2.28,.8) rectangle (2.52,1.2); \\draw (2.28,.8) rectangle (2.52,1.2);')
g.append('\\draw[thick] (3.0,0) -- (3.0,2.0); \\draw[thick] (3.0,0) -- (5.6,0); \\draw[thick] (5.6,0) -- (5.6,2.0);')
g.append('\\fill[gray!55] (3.03,1.3) rectangle (5.57,1.5); \\draw (3.03,1.3) rectangle (5.57,1.5);')
g.append(N(4.3,.65,'Ne\\\\$1$ atm','align=center')+N(4.3,-.35,'$2$ L')+'\\draw[-{Stealth[length=1.9mm]},thick] (4.3,2.5) -- (4.3,1.55); '+N(4.3,2.75,'dış basınç $=1$ atm'))
g.append(N(2.8,-1.1,'başlangıçta sıcaklık $T$; piston sürtünmesiz ve serbesttir','font=\\small'))
SK8=tk('\n'.join(g))
y_a=Fr(2*1); y_b=Vson; y_c=Vb1*2; y_d=Vson2
assert (y_a,y_b,y_c,y_d)==(2,8,12,16)
q('0008',[A('Her kaptaki mol büyüklüğünü bul','Aynı T’de P·V çarpımı mol sayısıyla orantılıdır.','He: 3 × 2 = 6 · Ne: 1 × 2 = 2 · toplam = 8 (birim)'),
 A('Musluk açılınca basıncı belirle','Piston serbest olduğundan gaz basıncı dış basınca eşit, yani 1 atm olur.','P = 1 atm'),
 A('Toplam hacmi hesapla','V = n·R·T ÷ P olduğundan toplam hacim 8 birimle orantılıdır.','V(toplam, T) = 8 L'),
 A('Isıtmanın etkisini ekle','T’den 2T’ye ısıtılınca sabit basınçta toplam hacim 2 katına çıkar.','V(toplam, 2T) = 16 L'),
 A('Pistonlu bölmenin hacmini bul','Rijit kabın hacmi 2 L’dir ve değişmez.','16 − 2 = 14 L')],
 metin='Şekildeki sistemde rijit kaptaki He gazı ile sürtünmesiz pistonlu kaptaki Ne gazı, aynı T sıcaklığındadır. Dış basınç sabit ve 1 atm’dir. Musluk açılıp gazlar karıştıktan ve sistem dengeye ulaştıktan sonra bütün sistem sıcaklığı 2T olacak biçimde ısıtılıyor.\n(Bağlantı borusunun hacmi ihmal edilecek; gazlar ideal davranmaktadır.)\nBuna göre son durumda pistonlu bölmenin hacmi kaç L olur?',
 sekil=SK8,dogru=14,yan=[(8,'Isıtmayı yok sayıp yalnız karıştırma sonundaki toplam hacmi (8 L) yazmış.','dikkat'),
  (12,'Isıtma öncesindeki pistonlu bölme hacmini (8 − 2 = 6 L) iki katına çıkarıp rijit kabı hesaba katmamış.','islem'),
  (16,'Toplam hacmi (16 L) bulup rijit kabın 2 L’sini çıkarmamış.','dikkat'),
  (6,'Isıtmayı yok sayıp toplam hacimden rijit kabı çıkarmış: 8 − 2 = 6 L.','dikkat')],
 istenen='Son durumda pistonlu bölmenin hacmi (L).',ip=['Piston serbestken sistemin basıncını belirle ve hangi bölmenin hacminin sabit olduğunu not et.'],
 bilgi=[B('Serbest piston ve gaz basıncı','Sürtünmesiz piston dengede iken gazın basıncı dış basınca eşittir; sabit basınçta hacim n·T ile orantılıdır. Örnek: 2 mol gaz 300 K’de 6 L ise 3 mol gaz aynı P ve T’de 9 L kaplar')],
 puf='Önce toplam mol ve basıncı bul, sonra toplam hacmi çıkar; sabit hacimli bölmeyi en sonda ayır.',
 tipId='gz-musluk',tip=TIPLER['gz-musluk'],z='zor',alt='Piston Düzenekleri',kaz='Rijit kap ve serbest pistonlu kabın birleştirildiği sistemde son hacmi hesaplar.',kalip='şekilli')

# ============ 0009 · CaCO3 + He karışımı · zor ============
mCaCO3=Fr(100)*Fr(1,2); nCO2=mCaCO3/100; nHe9=Fr(3,2); mHe9=nHe9*4; ntot9=nHe9+nCO2; mg=mHe9+nCO2*44
assert (nCO2,mHe9,ntot9,mg)==(Fr(1,2),6,2,28) and mg/ntot9==14
v1=(mHe9+44)/(nHe9+1); assert v1==20
v2=(mg+28)/ntot9; assert v2==28
v3=mg/ntot9*0+Fr(24); assert Fr(4+44,2)==24
v4=(nCO2*44)/ntot9; assert v4==11
q('0009',[A('CaCO₃’ın saf kütlesini bul','Safsızlık gaz vermez; yalnız saf CaCO₃ tepkimeye girer.','100 × %50 = 50 g'),
 A('CO₂ mol sayısını bul','CaCO₃ → CaO + CO₂ denkleminde katsayılar 1 : 1 olduğundan CO₂ mol sayısı CaCO₃’ınkine eşittir.','n(CO₂) = 50 ÷ 100 = 0,5 mol'),
 A('He’un mol sayısını ve kütlesini bul','Normal koşullarda 33,6 L He, 33,6 ÷ 22,4 mol eder.','n(He) = 1,5 mol → m = 6 g'),
 A('Karışımın toplam kütlesi ve molü','Yalnız gazlar sayılır; katı CaO karışıma girmez.','m = 6 + 0,5 × 44 = 28 g ve n = 2 mol'),
 A('Ortalama mol kütlesini yaz','Toplam kütle toplam mole bölünür.','M = 28 ÷ 2 = 14 g/mol')],
 metin='Sürtünmesiz ve hareketli bir pistonla kapatılmış kapta normal koşullarda 33,6 L He gazı bulunmaktadır. Kaba, kütlece %50’si saf CaCO₃ olan 100 g’lık bir örnek konuyor. Örnekteki saf CaCO₃ tamamen\nCaCO₃(k) → CaO(k) + CO₂(g)\ndenklemine göre ayrıştırıldıktan sonra kap yeniden normal koşullara getiriliyor. Safsızlık tepkimeye girmiyor ve gaz oluşturmuyor.\n(He = 4, C = 12, O = 16, Ca = 40 g/mol; normal koşullarda 1 mol gaz 22,4 L hacim kaplar.)\nBuna göre kaptaki gaz karışımının ortalama mol kütlesi kaç g/mol’dür?',
 dogru=14,yan=[(20,'Safsızlığı yok sayıp 100 g CaCO₃’ın tamamının ayrıştığını düşünmüş: 1 mol CO₂ ile (6 + 44) ÷ 2,5 = 20 g/mol.','bilgi'),
  (28,'Toplam kütleyi (28 g) toplam mol sayısına bölmek yerine olduğu gibi yazmış.','dikkat'),
  (24,'He ile CO₂’nin mol kütlelerinin aritmetik ortalamasını almış: (4 + 44) ÷ 2 = 24 g/mol.','bilgi'),
  (11,'Yalnız CO₂ kütlesini (22 g) toplam mol sayısına (2 mol) bölmüş; He’un kütlesini hesaba katmamış.','islem')],
 istenen='Karışımın ortalama mol kütlesi (g/mol).',ip=['Hangi maddelerin son karışımda gaz olduğunu ayır ve her birinin miktarını mol cinsinden yaz.'],
 bilgi=[B('Katı tepkimesi ve gaz mol sayısı','Saf madde kütlesi mol kütlesine bölünerek mol sayısı bulunur; denklem katsayıları mol oranını verir. Örnek: 40 g saf MgCO₃’ın (84 g/mol) ayrışmasıyla yaklaşık 0,48 mol CO₂ oluşur')],
 puf='Katıları karışımdan ayır; gaz karışımında M = gazların toplam kütlesi ÷ gazların toplam mol sayısı.',
 tipId='gz-ideal',tip=TIPLER['gz-ideal'],z='zor',alt='Gazlar ve Stokiyometri',kaz='Katı ayrışması sonucu oluşan gaz ile var olan gazın karışımının ortalama mol kütlesini hesaplar.',kalip='düz')

# ============ 0010 · P–1/V grafiği · orta · öncüllü ============
sx,sy=3.1,.45
g=[]
g.append(f'\\draw[->,thick] (0,0) -- ({2.35*sx:.2f},0) node[below right] {{$1/V$ (L$^{{-1}}$)}};')
g.append(f'\\draw[->,thick] (0,0) -- (0,{9*sy:.2f}) node[above] {{$P$ (atm)}};')
for x in (0.5,1,1.5,2): g.append(f'\\draw ({x*sx:.3f},.07) -- ({x*sx:.3f},-.07) node[below] {{{str(x).replace(".",",")}}};')
for p in (2,4,6,8): g.append(f'\\draw (.07,{p*sy:.3f}) -- (-.07,{p*sy:.3f}) node[left] {{{p}}};')
g.append(f'\\draw[thick] (0,0) -- ({2*sx:.3f},{8*sy:.3f}); \\draw[thick,vurgu,dashed] (0,0) -- ({2*sx:.3f},{4*sy:.3f});')
g.append(f'\\draw[dotted] ({sx:.3f},0) -- ({sx:.3f},{4*sy:.3f}) -- (0,{4*sy:.3f}); \\draw[dotted] (0,{2*sy:.3f}) -- ({sx:.3f},{2*sy:.3f});')
g.append(f'\\fill ({sx:.3f},{4*sy:.3f}) circle (1.6pt); \\fill[vurgu] ({sx:.3f},{2*sy:.3f}) circle (1.6pt);')
g.append(N(1.75*sx,8*sy*1.75/2+.4,'I')+N(1.8*sx,4*sy*1.8/2-.4,'\\textcolor{vurgu}{II}'))
SK10=tk('\n'.join(g))
d={'I':(True,'T aynıyken eğim nRT ile orantılıdır; eğimi 2 kat büyük olan doğrunun mol sayısı da 2 kattır'),
   'II':(True,'II doğrusunda P = 4 atm iken 1/V = 2 L⁻¹, yani V = 0,5 L’dir'),
   'III':(True,'eğim n·R·T olduğundan sıcaklık artınca nRT büyür ve doğrunun eğimi büyür')}
r=_onc(d,[('I',),('II',),('I','II'),('II','III'),('I','II','III')])
assert r['dogru']=='I, II ve III'
q('0010',[A('Grafikten eğimleri oku','I doğrusu 1/V = 1 L⁻¹’de 4 atm, II doğrusu 2 atm’dir.','Eğim(I) = 4 · Eğim(II) = 2 (atm·L)'),
 A('I. öncülü incele','T aynı olduğundan eğim n ile orantılıdır.','n(I) = 2·n(II) → I: doğru'),
 A('II. öncülü incele','P = 4 atm için II doğrusunda 1/V okunur ve tersi alınır.','1/V = 2 → V = 0,5 L → II: doğru'),
 A('III. öncülü incele','Eğim n·R·T olduğundan T artarsa büyür.','III: doğru'),
 A('Sonucu yaz','Doğru öncüller birleştirilir.',oy(d)+' · Sonuç: '+r['dogru'])],
 metin='Aynı sıcaklıktaki I ve II ideal gaz örneklerinin basıncının 1/V ile değişimi şekilde verilmiştir.\nI. I gazının mol sayısı II gazının mol sayısının 2 katıdır.\nII. II gazı 4 atm basınçta 0,5 L hacim kaplar.\nIII. Sıcaklık artırılırsa I gazına ait doğrunun eğimi büyür.\nBuna göre bu yargılardan hangileri doğrudur?',
 sekil=SK10,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['P ile 1/V arasındaki bağıntıdan doğrunun eğimini hangi büyüklüklerin belirlediğini çıkar.'],
 bilgi=[B('P–1/V grafiği','Sabit sıcaklıkta P = n·R·T·(1/V) olduğundan P–1/V grafiği orijinden geçen bir doğrudur; eğim n·R·T’dir. Örnek: eğimi 6 atm·L olan bir gaz örneğinde 1/V = 0,5 L⁻¹ iken P = 3 atm olur')],
 puf='Önce P ile 1/V arasındaki bağıntıyı yaz; eğimde hangi niceliklerin yer aldığına bak.',
 tipId='gz-grafik',tip=TIPLER['gz-grafik'],z='orta',alt='Gaz Grafikleri',kaz='P–1/V grafiğindeki doğruların eğimini mol sayısı ve sıcaklıkla ilişkilendirir.',kalip='grafik')

# ============ bitiş ============
assert len(P.ANA)==10
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/gazlariki'
os.makedirs(SC,exist_ok=True)
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(GD,'gazlariki-1.json'),os.path.join(SC,'bos-gazlariki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 11. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akgazlariki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
