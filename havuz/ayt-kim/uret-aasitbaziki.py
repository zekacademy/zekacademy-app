"""AYT Kimya · Asit-Baz Dengesi · 2. dalga (aasitbaziki) · 10 soru. Her sayı Python'da hesaplanıp assert edilir."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
from _hafif_kim import onc,tek,etk
KONUAD='Asit-Baz Dengesi'
H.KONU=KONUAD
P=Parti('aasitbaziki',KONUAD,'akim|'+KONUAD,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2018–2026 Kimya (Asit-Baz Dengesi, titrasyon, tampon; yalnız mantık) · MEB 12. sınıf kimya'
TIPLER={'ab-ph':'pH, pOH ve seyrelme/karıştırma hesapları','ab-bl':'Brønsted–Lowry asit–baz kavramı','ab-notrles':'Nötrleşme hesabı ve indikatör seçimi',
 'ab-titra':'Titrasyon eğrisi okuma ve yorumlama','ab-tampon':'Tampon çözelti: oluşum, etki ve pH hesabı','ab-ka':'Ka, Kb, asit kuvveti ve iyonlaşma yüzdesi'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AKASB2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,cn,ad,**k):
    mk(P,no,ad=ad,adim=len(ad),kart=f'K-AKASB2-{cn:02d} ('+CARD[cn]+')',tip=TIPLER[k['tipId']],**k)
SUP=str.maketrans('0123456789-+','⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺')
def e(m,n): return f'{m}·10{str(n).translate(SUP)}'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
def pg(opts,body):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}['+opts+']\n'+body+'\n\\end{axis}\n\\end{tikzpicture}')
def co(pts): return ' '.join(f'({x:.3f},{y:.3f})' for x,y in pts)
def kap(cx,ic,alt,h=1.5,w=1.15,t=2.2):
    s=[f'\\draw[thick] ({cx-w:.2f},{t}) -- ({cx-w:.2f},0) -- ({cx+w:.2f},0) -- ({cx+w:.2f},{t});',
       f'\\fill[vurgu!15] ({cx-w+.02:.2f},.02) rectangle ({cx+w-.02:.2f},{h});\\draw[vurgu] ({cx-w+.02:.2f},{h}) -- ({cx+w-.02:.2f},{h});']
    for i,l in enumerate(ic): s.append(f'\\node at ({cx:.2f},{h-.4-i*.42:.2f}) {{{l}}};')
    if alt: s.append(f'\\node[below=2pt] at ({cx:.2f},0) {{{alt}}};')
    return s
# ---------- titrasyon eğrisi çözücüleri (mmol, mL)
Kw=1e-14
def _bis(f):
    lo,hi=-14.0,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if f(10**m)>0: hi=m
        else: lo=m
    return -(lo+hi)/2
def ph_acid(Ka,nA,cNaOH,VB,VA):   # nA mmol HA, VA mL; NaOH cNaOH M, VB mL
    V=VA+VB; CT=nA/V; Na=cNaOH*VB/V
    return _bis(lambda h:h+Na-CT*Ka/(Ka+h)-Kw/h)
def ph_base(Kb,nB,cHCl,VA,VB):   # nB mmol baz, VB mL; HCl cHCl M, VA mL
    V=VA+VB; CT=nB/V; Cl=cHCl*VA/V; Kab=Kw/Kb
    return _bis(lambda h:h+CT*h/(h+Kab)-Cl-Kw/h)
L1=[('I',),('II',),('III',),('I','II'),('I','III')]
L2=[('I',),('I','II'),('I','III'),('II','III'),('I','II','III')]
# =============== BİLGİ KUTULARI (örnekler sorulardan farklı)
B_PH=B('pH, pOH ve H⁺/OH⁻ derişimi','25 °C’de pH = −log[H⁺], pOH = −log[OH⁻] ve pH + pOH = 14’tür; [H⁺]·[OH⁻] = 10⁻¹⁴’tür. pH ölçeğinde bir birim fark, H⁺ derişiminde 10 kat fark demektir. Örnek: pH değeri 4 olan çözeltide [H⁺] = 10⁻⁴ M ve [OH⁻] = 10⁻¹⁰ M’dir')
B_BL=B('Brønsted–Lowry asit–baz','Proton (H⁺) veren tür asit, proton alan tür bazdır. Asit proton verince eşlenik bazına, baz proton alınca eşlenik asidine dönüşür. Hem proton verebilen hem alabilen türlere amfoter denir. Örnek: HF + CN⁻ ⇌ F⁻ + HCN tepkimesinde HF asit, CN⁻ bazdır')
B_SEY=B('Seyrelme','Çözeltiye su eklenince çözünenin mol sayısı değişmez, derişim toplam hacimle ters orantılı azalır: M₁V₁ = M₂V₂. Kuvvetli monoprotik asitte [H⁺] = C, zayıf monoprotik asitte [H⁺] = √(Ka·C) alınır. Örnek: Ka = 1·10⁻⁶ olan 0,01 M zayıf asitte [H⁺] = √(10⁻⁶·10⁻²) = 10⁻⁴ M’dir')
B_KA=B('Ka, Kb ve iyonlaşma yüzdesi','HA ⇌ H⁺ + A⁻ için Ka = [H⁺][A⁻]/[HA]’dır; zayıf asitte [H⁺] ≈ [A⁻] ve [HA] ≈ başlangıç derişimidir. İyonlaşma yüzdesi = (iyonlaşan/başlangıç)·100’dür. Baz için Kb aynı biçimde yazılır. Örnek: 0,4 M HA’da [H⁺] = 2·10⁻³ M ise Ka = (2·10⁻³)²/0,4 = 1·10⁻⁵’tir')
B_NOT=B('Nötrleşme','H⁺ + OH⁻ → H₂O; tam nötrleşmede asidin verebileceği H⁺ mol sayısı bazın verebileceği OH⁻ mol sayısına eşitlenir ve n = M·V ile hesaplanır. Örnek: 40 mL 0,05 M KOH’ı nötrleştirmek için 0,1 M HNO₃’ten 20 mL gerekir')
B_TIT=B('Titrasyon eğrisi','Eşdeğerlik hacmi titre edilen maddenin mol sayısını verir (n = M·V). Zayıf asit–kuvvetli baz titrasyonunda yarı eşdeğerlik noktasında [HA] = [A⁻] olduğundan pH = pKa’dır; zayıf baz için aynı noktada pOH = pKb’dir. Eşdeğerlikte oluşan tuz hidroliz eder. Örnek: 25 mL 0,2 M HNO₃’ün eşdeğerliği için 0,1 M KOH’tan 50 mL gerekir')
B_TAM=B('Tampon çözelti','Zayıf asit ile eşlenik bazı (ya da zayıf baz ile eşlenik asidi) birlikte bulunan çözeltidir. pH = pKa + log([A⁻]/[HA]) bağıntısı kullanılır; oran mol sayılarıyla da yazılabilir. Eklenen OH⁻ asidik bileşeni, eklenen H⁺ bazik bileşeni harcar. Örnek: [A⁻]/[HA] = 10 ise pH = pKa + 1’dir')
B_HID=B('Tuzların hidrolizi','Zayıf asidin eşlenik bazı olan anyon suyla OH⁻ oluşturur (bazik); zayıf bazın eşlenik asidi olan katyon H⁺ oluşturur (asidik). A⁻ + H₂O ⇌ HA + OH⁻ için Kb = Kw/Ka ve [OH⁻] = √(Kb·C)’dir; BH⁺ için Ka = Kw/Kb ve [H⁺] = √(Ka·C)’dir. Örnek: Ka = 1·10⁻⁶ ise 0,01 M NaA’da Kb = 10⁻⁸’dir')
# =============== KARTLAR
card(1,'pH ölçeği ve seyrelme','pH ölçeğinde her birim H⁺ derişiminde 10 kat fark yaratır; seyrelmede kuvvetli asidin pH’ı hacim oranının logaritması kadar, zayıf asidinki bunun yarısı kadar artar.','pH ile pOH’u karıştırmak; zayıf asidin seyrelince kuvvetli asit gibi davrandığını sanmak.','orta','grafik',3,'ab-ph','pH ölçeği ve seyrelme grafiği')
card(2,'Brønsted–Lowry asit ve baz','Proton veren asit, proton alan bazdır; aynı tür tepkimeye göre hem asit hem baz olabilir, su amfoterdir.','Suyun her tepkimede asit ya da her tepkimede baz olduğunu sanmak.','kolay','tablo',3,'ab-bl','Brønsted–Lowry tanımı ve amfoter türler')
card(3,'Aynı pH’lı kuvvetli ve zayıf asit','Aynı pH’ta zayıf asidin derişimi çok büyüktür; nötrleşmede asidin başlangıç mol sayısı hesaba katılır, o anki iyon sayısı değil.','Aynı pH’lı asitlerin aynı miktarda baz harcadığını sanmak.','orta','şekilli',4,'ab-notrles','Aynı pH’lı kuvvetli–zayıf asidin nötrleştirilmesi')
card(4,'Titrasyon eğrisinden sabit okuma','Eşdeğerlik hacminden derişim, başlangıç ve yarı eşdeğerlik pH’ından Ka–Kb ve tuz pH’ı bulunur.','Yarı eşdeğerlik ile eşdeğerlik noktasını karıştırmak; asit tuzunun pH’ını pKa sanmak.','orta','grafik',4,'ab-titra','Titrasyon eğrisinden Ka, Kb ve tuz pH’ı')
card(5,'Tampon oluşumu ve hazırlama','Tampon, tepkime sonunda zayıf asit ve eşlenik bazının birlikte artması ile oluşur; mol sayıları tepkimeye göre güncellenip Henderson bağıntısı uygulanır.','Tepkimede harcanan miktarı güncellememek; oranı ters yazmak; kuvvetli asit/baz artığını tampon saymak.','orta','tablo',4,'ab-tampon','Tampon oluşumu, pH ve hazırlama')
card(6,'Kuvvetli ve zayıf baz karşılaştırması','Aynı derişimli kuvvetli ve zayıf bazda OH⁻ derişimi ve iyonlaşma yüzdesi farklıdır; tam nötrleşme için gereken asit miktarı ise toplam mol sayısına bağlıdır.','İyonlaşma yüzdesini pH’tan doğrudan okumak; zayıf bazın daha az asit harcadığını sanmak.','orta','şekilli',3,'ab-ka','Kuvvetli–zayıf baz karşılaştırması')
# ======================================================================
# 0001 · kolay · pH ölçeği, öncüllü  (A: Yalnız I)
# ======================================================================
pHs={'X':2,'Y':5,'Z':9,'T':12}
assert 10**(pHs['Y']-pHs['X'])==1000 and 14-pHs['Z']==5 and 14-pHs['T']==2
sc=.5; p=['\\draw[thick] (0,0) -- (%.2f,0);'%(14*sc)]
for i in range(15): p.append(f'\\draw (%.2f,.08) -- (%.2f,-.08); \\node[below=1pt] at (%.2f,-.08) {{{i}}};'%(i*sc,i*sc,i*sc))
for n,v in pHs.items(): p.append(f'\\draw[vurgu,very thick,-{{Stealth[length=2.4mm]}}] (%.2f,1.0) -- (%.2f,.15); \\node[above] at (%.2f,1.0) {{\\textbf{{{n}}}}};'%(v*sc,v*sc,v*sc))
p+=['\\node[anchor=west] at (%.2f,0) {pH};'%(14*sc+.15),'\\node at (%.2f,-.95) {asidik};'%(3.2*sc),'\\node at (%.2f,-.95) {nötr};'%(7*sc),'\\node at (%.2f,-.95) {bazik};'%(10.8*sc),
    '\\draw[dashed,gray] (%.2f,-.55) -- (%.2f,-1.25);'%(6.5*sc,6.5*sc),'\\draw[dashed,gray] (%.2f,-.55) -- (%.2f,-1.25);'%(7.5*sc,7.5*sc)]
sk=fig(*p)
d={'I':(True,'pH değeri 2 olan çözeltide [H⁺] = 10⁻² M, pH değeri 5 olanda 10⁻⁵ M olduğundan oran 1000’dir'),
   'II':(False,'pH değeri 9 olan Z çözeltisinde [H⁺] = 10⁻⁹ M ve [OH⁻] = 10⁻⁵ M’dir; 10⁻⁹ M, H⁺ derişimidir'),
   'III':(False,'pH değeri 12 olan T çözeltisinin pOH değeri 14 − 12 = 2’dir')}
r=onc(d,L1)
q('0001',1,[A('I. yargı','pH farkı 5 − 2 = 3 olduğundan H⁺ derişimleri oranı 10³’tür.','[H⁺]ₓ/[H⁺]ᵧ = 1000 → doğru'),
   A('II. yargı','pH = 9 için [H⁺] = 10⁻⁹ M olur; [OH⁻] = 10⁻¹⁴/10⁻⁹ bulunur.','[OH⁻] = 10⁻⁵ M → yanlış'),
   A('III. yargı','pOH = 14 − pH bağıntısı kullanılır.','pOH = 2 → yanlış'),
   A('Sonuç','Yalnız I. yargı doğrudur.','Yalnız I')],
 tipId='ab-ph',z='kolay',alt='pH Ölçeği',kaz='pH ölçeğindeki değerlerden H⁺ ve OH⁻ derişimlerini ve pOH değerini yorumlar.',kalip='grafik',
 metin='25 °C’de hazırlanan X, Y, Z ve T sulu çözeltilerinin pH değerleri pH ölçeği üzerinde gösterilmiştir. Çözeltilerin hiçbirinde başka bir asit ya da baz bulunmamaktadır.\nBuna göre,\nI. X çözeltisindeki H⁺ derişimi, Y çözeltisindekinin 1000 katıdır.\nII. Z çözeltisinde [OH⁻] = 10⁻⁹ M’dir.\nIII. T çözeltisinin pOH değeri 12’dir.\nyargılarından hangileri doğrudur?',
 sekil=sk,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her yargı için ölçekten okuduğun pH değerini H⁺, OH⁻ ya da pOH’a çevir.'],bilgi=[B_PH],
 puf='pH’tan [H⁺] = 10⁻ᵖᴴ, pOH = 14 − pH ve [OH⁻] = 10⁻ᵖᴼᴴ biçiminde ilerle.')
# ======================================================================
# 0002 · kolay · Brønsted–Lowry tablo, olumsuz kök  (A: yanlış ifade)
# ======================================================================
rows=[['1','HCl(suda) + H₂O(s) → H₃O⁺(suda) + Cl⁻(suda)'],['2','NH₃(suda) + H₂O(s) ⇌ NH₄⁺(suda) + OH⁻(suda)'],['3','HCO₃⁻(suda) + H₂O(s) ⇌ H₂CO₃(suda) + OH⁻(suda)'],
      ['4','HCO₃⁻(suda) + H₂O(s) ⇌ CO₃²⁻(suda) + H₃O⁺(suda)'],['5','CH₃COOH(suda) + H₂O(s) ⇌ CH₃COO⁻(suda) + H₃O⁺(suda)']]
sk=tablo_svg(['Tepkime no','Tepkime'],rows)
S=[('5. tepkimede H₂O, asit olarak davranır.',False,''),
   ('1. tepkimede H₂O, baz olarak davranır.',True,'HCl proton verir, H₂O proton alarak H₃O⁺ oluşturur; proton alan tür baz olduğundan ifade doğrudur.'),
   ('2. tepkimede H₂O, asit olarak davranır.',True,'H₂O, NH₃’e proton verip OH⁻ oluşturur; proton veren tür asit olduğundan ifade doğrudur.'),
   ('3. tepkimede HCO₃⁻, baz olarak davranır.',True,'HCO₃⁻ proton alarak H₂CO₃ olur; proton alan tür baz olduğundan ifade doğrudur.'),
   ('4. tepkimede HCO₃⁻, asit olarak davranır.',True,'HCO₃⁻ proton verip CO₃²⁻ olur; proton veren tür asit olduğundan ifade doğrudur.')]
r=tek(S,False)
q('0002',2,[A('Protonun yönünü bul','Her tepkimede protonu kimin verdiğine ve kimin aldığına bakılır.','Proton veren asit, proton alan baz'),
   A('Yargıları sına','1–4. tepkimelerde belirtilen türlerin görevleri proton alışverişiyle uyumludur.','1, 2, 3 ve 4 doğru'),
   A('5. tepkimeyi incele','CH₃COOH proton verir, H₂O bu protonu alarak H₃O⁺ olur; yani H₂O baz gibi davranır.','5. yargı yanlış')],
 tipId='ab-bl',z='kolay',alt='Brønsted–Lowry Asit ve Baz',kaz='Tepkimelerde proton alışverişine göre türlerin asit ya da baz olarak davrandığını belirler.',kalip='tablo',
 metin='Brønsted–Lowry tanımına göre proton veren tür asit, proton alan tür bazdır. Bazı sulu çözelti tepkimeleri tabloda verilmiştir.\nBuna göre, tablodaki tepkimelerle ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
 sekil=sk,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',
 ip=['Her tepkimede belirtilen türün proton verip vermediğine ya da alıp almadığına bak.'],bilgi=[B_BL],
 puf='Tepkimenin girenlerindeki türün hangi proton değişimini yaptığına bakarak görevini belirle; suyun görevi tepkimeye göre değişir.')
# ======================================================================
# 0003 · orta · seyrelme grafiği, öncüllü  (E: I ve III)
# ======================================================================
Ka3=Fr(1,10**5); C3y=Fr(1,10); C3x=Fr(1,1000)
assert math.isclose(math.sqrt(float(Ka3*C3y)),1e-3) and C3y/C3x==100
pX=lambda n:3+math.log10(n); pY=lambda n:-math.log10(math.sqrt(1e-5*0.1/n))
assert [round(pX(n),6) for n in (1,10,100)]==[3,4,5] and [round(pY(n),6) for n in (1,10,100)]==[3,3.5,4]
cx=[(0,3),(1,4),(2,5)]; cy=[(0,3),(1,3.5),(2,4)]
sk=pg('width=7.2cm,height=5.2cm,axis lines=left,xmin=-.1,xmax=2.3,ymin=2,ymax=6,xtick={0,1,2},xticklabels={1,10,100},ytick={2,3,4,5,6},grid=major,grid style={gray!30},xlabel={Seyrelme katı},ylabel={pH},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black,mark=*] coordinates {{{co(cx)}}};\n\\addplot[thick,dashed,color=red!70!black,mark=square*] coordinates {{{co(cy)}}};\n\\node[anchor=south east,font=\\small] at (axis cs:2.0,5.0) {{\\textbf{{X}}}};\n\\node[anchor=north,font=\\small] at (axis cs:2.0,3.85) {{\\textbf{{Y}}}};')
d={'I':(True,'X’in pH değeri seyrelme katı 10 olunca 1 birim arttığı için kuvvetli, Y’ninki yalnız 0,5 birim arttığı için zayıf asittir'),
   'II':(False,'başlangıç pH değerleri eşit olsa da zayıf asit kısmen iyonlaştığından Y’nin molar derişimi X’inkinden çok büyüktür'),
   'III':(True,'seyrelme katı 100 iken X’in pH değeri 5, Y’ninki 4 olduğundan fark 1’dir')}
r=onc(d,L1)
q('0003',1,[A('Grafiği oku','Seyrelme katı 1’den 100’e çıkarken X’in pH değeri 3’ten 5’e, Y’ninki 3’ten 4’e çıkar.','X: +2 birim, Y: +1 birim'),
   A('Asit kuvvetini belirle','Kuvvetli asitte [H⁺] doğrudan derişimdir ve 100 kat seyrelmede pH 2 birim artar; zayıf asitte [H⁺] = √(Ka·C) olduğundan pH 1 birim artar.','X kuvvetli, Y zayıf → I doğru'),
   A('Derişimleri kıyasla','Aynı [H⁺] için zayıf asidin derişimi, C = [H⁺]²/Ka bağıntısıyla çok daha büyüktür.','II yanlış'),
   A('pH farkı','Seyrelme katı 100’de X’in pH değeri 5, Y’ninki 4’tür.','Fark = 1 → III doğru')],
 tipId='ab-ph',z='orta',alt='Seyrelme ve pH Değişimi',kaz='Kuvvetli ve zayıf asit çözeltilerinin seyrelmesiyle pH değişimini grafikten yorumlar.',kalip='grafik',
 metin='25 °C’de X ve Y monoprotik asitlerinin sulu çözeltilerinden biri kuvvetli, diğeri zayıf asit çözeltisidir. İki çözeltinin de başlangıç pH değeri 3’tür. Çözeltilerin her birine saf su eklenerek seyreltiliyor ve pH değerinin, toplam hacmin başlangıç hacmine oranı (seyrelme katı) ile değişimi grafikte gösteriliyor.\nBuna göre,\nI. X kuvvetli, Y zayıf asit çözeltisidir.\nII. Seyreltmeden önce X ve Y çözeltilerinin molar derişimleri eşittir.\nIII. Seyrelme katı 100 olduğunda iki çözeltinin pH değerleri arasındaki fark 1’dir.\nyargılarından hangileri doğrudur?',
 sekil=sk,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Seyrelme katı arttıkça iki eğrinin pH değerlerinin hangi miktarlarda değiştiğini karşılaştır.'],bilgi=[B_SEY,B_PH],
 puf='Kuvvetli asitte pH değişimi log(seyrelme katı) kadar, zayıf asitte bunun yarısı kadardır.')
# ======================================================================
# 0004 · orta · eşit pH'lı HCl ve HA, NaOH hacim farkı  (C)
# ======================================================================
VA=Fr(50,1000); nHCl=Fr(1,100)*VA; cHA=Fr(1,1000)**2/Ka3; nHA=cHA*VA; cN=Fr(1,10)
vHCl=nHCl/cN*1000; vHA=nHA/cN*1000
assert cHA==Fr(1,10) and vHCl==5 and vHA==50 and vHA-vHCl==45
sk=fig(*kap(0,['50 mL','\\ce{HCl}(suda)','pH $=2$'],'I'),*kap(3.4,['50 mL','\\ce{HA}(suda)','pH $=3$'],'II'))
q('0004',3,[A('HCl için NaOH','pH = 2 ise [H⁺] = 10⁻² M; n(HCl) = 0,01 · 0,05 = 5·10⁻⁴ mol ve bu kadar OH⁻ gerekir.','V = 5·10⁻⁴/0,1 = 5 mL'),
   A('HA derişimi','pH = 3 ise [H⁺] = [A⁻] = 10⁻³ M; Ka = [H⁺]²/[HA] bağıntısından başlangıç derişimi bulunur.','[HA] = (10⁻³)²/10⁻⁵ = 0,1 M'),
   A('HA için NaOH','Nötrleşmede asidin toplam mol sayısı hesaba katılır.','n(HA) = 0,1 · 0,05 = 5·10⁻³ mol → V = 50 mL'),
   A('Fark','İki hacmin farkı alınır.','50 − 5 = 45 mL')],
 tipId='ab-notrles',z='orta',alt='Aynı pH’lı Asitlerin Nötrleşmesi',kaz='Aynı pH değerine sahip kuvvetli ve zayıf asit çözeltilerini nötrleştirmek için gereken baz hacimlerini karşılaştırır.',kalip='şekilli',
 metin='25 °C’de şekilde verilen I. kapta 50 mL HCl, II. kapta 50 mL zayıf monoprotik HA asidinin sulu çözeltisi bulunmaktadır. HA’nın Ka değeri 1·10⁻⁵’tir ve HA çözeltisinde denge anında [HA] derişiminin başlangıç derişimine eşit olduğu kabul edilecektir.\nİki çözelti de ayrı ayrı 0,1 M NaOH çözeltisiyle tamamen nötrleştirildiğine göre, II. kap için harcanan NaOH çözeltisi hacmi, I. kap için harcananından kaç mL fazladır?',
 sekil=sk,dogru=45,yan=[(0,'İki asit çözeltisinin hacimleri ve pH değerleri benzer görünse de aynı miktarda NaOH harcayacaklarını sanarak farkı 0 bulmuştur.','dikkat'),
   (5,'Yalnız HCl çözeltisinin harcadığı NaOH hacmini (5 mL) hesaplamış ve fark almayı atlamıştır.','islem'),
   (50,'Yalnız HA çözeltisinin harcadığı NaOH hacmini (50 mL) vermiş; HCl’nin harcadığı 5 mL’yi çıkarmamıştır.','islem'),
   (55,'İki hacmi çıkarmak yerine toplamıştır (50 + 5).','islem')],
 istenen='İki nötrleşme arasındaki NaOH hacim farkı (mL).',ip=['Her asidin başlangıçtaki toplam mol sayısını ayrı ayrı bulmaya çalış.'],bilgi=[B_KA,B_NOT],
 puf='Nötrleşmede çözeltideki toplam asit miktarı belirleyicidir; pH yalnız iyonlaşmış kısmı gösterir.')
# ======================================================================
# 0005 · orta · zayıf baz titrasyon eğrisi, Kb  (C)
# ======================================================================
Kb5=2e-5; pts=[]
for v in list(range(0,16))+[17,18,19,19.5,19.9,20,20.1,20.5,21,22,24,26,28,30,34,38,40]: pts.append((v,ph_base(Kb5,1.0,0.05,v,20)))
assert abs(pts[0][1]-11)<.01 and 5<pts[[p[0] for p in pts].index(20)][1]<6
CB=Fr(5,100)*Fr(20,20); OH5=Fr(1,1000); assert (OH5**2/CB)==Fr(2,10**5) and (OH5**2)==Fr(1,10**6) and OH5**2/(Fr(1,1000)*Fr(1,40)*20/Fr(1,1)*Fr(1,1))>=0
assert OH5**2/Fr(25,1000)==Fr(4,10**5) and Fr(1,10**14)/Fr(2,10**5)==Fr(5,10**10)
sk=pg('width=7.4cm,height=5.4cm,axis lines=left,xmin=0,xmax=40,ymin=0,ymax=14,xtick={0,10,20,30,40},ytick={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14},grid=major,grid style={gray!30},xlabel={HCl çözeltisi hacmi (mL)},ylabel={pH},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(pts)}}};')
sira5=[e(5,-10),e(1,-6),e(2,-5),e(4,-5),e(1,-3)]
q('0005',4,[A('Baz derişimi','Eşdeğerlik 20 mL HCl ile sağlanıyor; n(B) = n(HCl) = 0,05 · 0,02 = 10⁻³ mol ve çözelti hacmi 20 mL’dir.','[B] = 10⁻³/0,02 = 0,05 M'),
   A('OH⁻ derişimi','Grafikte başlangıç pH değeri 11, yani pOH = 3’tür.','[OH⁻] = 10⁻³ M'),
   A('Kb','Kb = [BH⁺][OH⁻]/[B] ve [BH⁺] = [OH⁻]; [B] ≈ 0,05 M alınır.','Kb = (10⁻³)²/0,05 = 2·10⁻⁵')],
 tipId='ab-titra',z='orta',alt='Zayıf Baz Titrasyonu',kaz='Zayıf baz–kuvvetli asit titrasyon eğrisinden bazın derişimini ve Kb değerini hesaplar.',kalip='grafik',
 metin='25 °C’de 20 mL’lik zayıf B bazı çözeltisi 0,05 M HCl çözeltisiyle titre ediliyor ve pH değerinin eklenen HCl çözeltisi hacmiyle değişimi grafikte verilmiştir. Denge anında B derişiminin başlangıç derişimine eşit olduğu kabul edilecektir.\nBuna göre, B bazının Kb değeri kaçtır?',
 sekil=sk,dogru=e(2,-5),yan=[(e(5,-10),'Kb yerine eşlenik asidin Ka değerini (Kw/Kb = 5·10⁻¹⁰) vermiştir.','bilgi'),
   (e(1,-6),'Kb ifadesinde paydadaki B derişimini yazmayı unutup yalnız [OH⁻]² = 1·10⁻⁶ bulmuştur.','islem'),
   (e(4,-5),'Baz derişimini 0,025 M alarak (karışımın toplam hacmine bölerek) Kb = 4·10⁻⁵ bulmuştur.','islem'),
   (e(1,-3),'[OH⁻] derişimini (1·10⁻³ M) doğrudan Kb olarak vermiştir.','dikkat')],
 sira=sira5,istenen='B bazının Kb değeri.',ip=['Bazın başlangıç derişimini ve çözeltideki OH⁻ derişimini grafikten okunabilen değerlerle bulmaya çalış.'],bilgi=[B_KA,B_TIT],
 puf='Eşdeğerlik hacmi derişimi, başlangıç pH değeri OH⁻ derişimini verir; Kb bu ikisinden çıkar.')
# ======================================================================
# 0006 · orta · tampon karışımları, tablo, öncüllü  (B: I ve II)
# ======================================================================
nHA6,nNaOH6=Fr(2,10),Fr(1,10); assert nHA6-nNaOH6==nNaOH6
assert Fr(1,10)-Fr(1,10)==0
nNaA,nHCl6=Fr(2,10),Fr(3,10); assert nHCl6-nNaA==Fr(1,10)>0
assert -math.log10(1e-5)+math.log10(1)==5
sk=tablo_svg(['Karışım','Karıştırılan maddeler'],[['1','0,2 mol HA + 0,1 mol NaOH'],['2','0,1 mol HA + 0,1 mol NaOH'],['3','0,2 mol NaA + 0,3 mol HCl']])
d={'I':(True,'0,1 mol NaOH, 0,1 mol HA’yı nötrleştirir; 0,1 mol HA ile 0,1 mol A⁻ kalır ve pH = pKa = 5’tir'),
   'II':(True,'tam nötrleşme sonunda yalnız NaA kalır; A⁻ hidroliz olup OH⁻ verdiğinden pH 7’den büyüktür'),
   'III':(False,'0,2 mol HCl, 0,2 mol A⁻’yi harcar ve ortamda 0,1 mol HCl artar; zayıf asit–eşlenik baz çifti oluşmadığından karışım tampon değildir')}
r=onc(d,L2)
q('0006',5,[A('1. karışım','NaOH, HA ile 1 : 1 tepkime verir; 0,1 mol HA harcanır ve 0,1 mol A⁻ oluşur.','n(HA) = 0,1 mol, n(A⁻) = 0,1 mol → tampon, pH = 5'),
   A('2. karışım','HA ve NaOH eşit mol olduğundan tamamen nötrleşir.','Ortamda yalnız NaA var → A⁻ hidrolizi, pH > 7'),
   A('3. karışım','HCl önce A⁻’nin tamamını HA’ya çevirir ve geriye HCl artar.','0,2 mol HA + 0,1 mol HCl → tampon değil'),
   A('Sonuç','I ve II doğru, III yanlıştır.','I ve II')],
 tipId='ab-tampon',z='orta',alt='Tampon Oluşumu',kaz='Zayıf asit ve tuzu ile kuvvetli asit–baz karışımlarında tampon oluşup oluşmadığını ve pH değerini belirler.',kalip='tablo',
 metin='Ka değeri 1·10⁻⁵ olan monoprotik zayıf HA asidi ve sodyum tuzu NaA ile kuvvetli NaOH ve HCl kullanılarak 25 °C’de üç ayrı sulu karışım hazırlanıyor. Karışımların içeriği tabloda verilmiştir ve tepkimelerin tam gerçekleştiği kabul edilecektir.\nBuna göre,\nI. 1. karışım tampon çözeltidir ve pH değeri 5’tir.\nII. 2. karışımın pH değeri 7’den büyüktür.\nIII. 3. karışım tampon çözeltidir.\nyargılarından hangileri doğrudur?',
 sekil=sk,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her karışımda tepkimeden sonra hangi maddelerin ve ne miktarda kaldığını yaz.'],bilgi=[B_TAM,B_HID],
 puf='Önce kuvvetli asit ya da bazın zayıf asit–eşlenik bazı üzerindeki tepkimesini yaz, sonra kalan türlere bak.')
# ======================================================================
# 0007 · orta · NaOH ve B kapları, öncüllü  (D: II ve III)
# ======================================================================
OHn=Fr(1,10); OHb=Fr(1,10**4); Cb=Fr(1,10); assert OHb/Cb*100==Fr(1,10) and OHn/OHb==1000
sk=fig(*kap(0,['100 mL','0,1 M \\ce{NaOH}','pH $=13$'],'I'),*kap(3.4,['100 mL','0,1 M B','pH $=10$'],'II'))
d={'I':(False,'B çözeltisinde pH 10 olduğundan [OH⁻] = 10⁻⁴ M’dir ve iyonlaşma yüzdesi (10⁻⁴/0,1)·100 = %0,1’dir'),
   'II':(True,'[OH⁻] NaOH’de 10⁻¹ M, B’de 10⁻⁴ M olduğundan oran 1000’dir'),
   'III':(True,'iki çözeltide de bazın toplam mol sayısı eşit olduğundan nötrleşme için aynı mol H⁺ gerekir')}
r=onc(d,L2)
q('0007',6,[A('OH⁻ derişimleri','NaOH’de pOH = 1, B’de pOH = 4’tür.','[OH⁻]: 10⁻¹ M ve 10⁻⁴ M'),
   A('İyonlaşma yüzdesi','B için (10⁻⁴/0,1)·100 hesaplanır.','%0,1 → I yanlış'),
   A('Derişim oranı','10⁻¹/10⁻⁴ oranı alınır.','1000 kat → II doğru'),
   A('Nötrleşme','Her iki çözeltide 0,01 mol baz vardır ve aynı derişimli HCl’nin eşit hacmi gerekir.','III doğru → II ve III')],
 tipId='ab-ka',z='orta',alt='Kuvvetli ve Zayıf Baz',kaz='Aynı derişimli kuvvetli ve zayıf bazın OH⁻ derişimini, iyonlaşma yüzdesini ve nötrleşme miktarını karşılaştırır.',kalip='şekilli',
 metin='25 °C’de hazırlanan, aynı hacimli ve aynı derişimli NaOH ve zayıf monoprotik B bazı çözeltileri ile bu çözeltilerin pH değerleri şekilde verilmiştir.\nBuna göre,\nI. B bazının iyonlaşma yüzdesi %1’dir.\nII. NaOH çözeltisindeki OH⁻ derişimi, B çözeltisindekinin 1000 katıdır.\nIII. Çözeltilerin tamamen nötrleşmesi için aynı derişimli HCl çözeltisinden eşit hacim gerekir.\nyargılarından hangileri doğrudur?',
 sekil=sk,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['Her çözeltide pH değerinden OH⁻ derişimini bul; bazın toplam miktarı ile iyonlaşan kısmını ayrı düşün.'],bilgi=[B_KA,B_NOT],
 puf='pH iyonlaşan kısmı, nötrleşme miktarı ise bazın toplam mol sayısını gösterir.')
# ======================================================================
# 0008 · zor · NH4Cl pH → tampon pH  (E: 9,6)
# ======================================================================
C8=Fr(1,10); Ka8=Fr(1,10**5)**2/C8; assert Ka8==Fr(1,10**9) and Fr(1,10**14)/Ka8==Fr(1,10**5)
nNH4=C8*Fr(100,1000); nOH=Fr(1,10)*Fr(80,1000); assert nNH4==Fr(1,100) and nOH==Fr(8,1000)
nNH3=nOH; nNH4r=nNH4-nOH; assert nNH4r==Fr(2,1000) and nNH3/nNH4r==4
L2_=0.3; pH8=9+2*L2_; pOH8=5-2*L2_; assert abs(pH8-9.6)<1e-9 and abs(pOH8-4.4)<1e-9 and abs((5+2*L2_)-5.6)<1e-9 and abs(9-2*L2_-8.4)<1e-9
sk=fig(*kap(0,['100 mL','0,1 M \\ce{NH4Cl}','pH $=5$'],''),'\\node at (1.95,1.0) {\\Large $+$};',*kap(3.9,['80 mL','0,1 M \\ce{NaOH}'],''),
 '\\draw[-{Stealth[length=2.2mm]},thick] (5.2,1.0) -- (6.3,1.0);',*kap(7.6,['180 mL','karışım','pH $=\\,?$'],''))
q('0008',5,[A('Ka değeri','NH₄⁺ ⇌ NH₃ + H⁺ dengesinde [H⁺] = 10⁻⁵ M ve [NH₄⁺] ≈ 0,1 M alınır.','Ka = (10⁻⁵)²/0,1 = 10⁻⁹ (pKa = 9)'),
   A('Mol sayıları','n(NH₄⁺) = 0,1 · 0,1 ve n(OH⁻) = 0,1 · 0,08 hesaplanır.','10⁻² mol NH₄⁺, 8·10⁻³ mol OH⁻'),
   A('Tepkime sonrası','NH₄⁺ + OH⁻ → NH₃ + H₂O tepkimesinde OH⁻ tükenir.','NH₃ = 8·10⁻³ mol, NH₄⁺ = 2·10⁻³ mol → tampon'),
   A('pH','Henderson bağıntısında log 4 = 2 log 2 = 0,6 alınır.','pH = 9 + log(8/2) = 9,6')],
 tipId='ab-tampon',z='zor',alt='Tuz Çözeltisinden Tampon Hazırlama',kaz='Tuz çözeltisinin pH değerinden Ka’yı bulur ve kuvvetli baz ilavesiyle oluşan tamponun pH değerini hesaplar.',kalip='şekilli',
 metin='25 °C’de 100 mL 0,1 M NH₄Cl çözeltisinin pH değeri 5 olarak ölçülüyor. Bu çözeltiye 0,1 M NaOH çözeltisinden 80 mL ekleniyor ve karışımın hacminin toplam hacme eşit olduğu, tepkimenin tam gerçekleştiği kabul ediliyor. NH₄⁺ iyonunun hidroliz eden miktarı başlangıç derişimine göre ihmal edilecek ve log 2 = 0,3 alınacaktır.\nBuna göre, oluşan çözeltinin pH değeri kaçtır?',
 sekil=sk,dogru=Fr(96,10),yan=[(Fr(44,10),'Tampon çözeltideki pOH değerini (4,4) pH olarak vermiştir.','dikkat'),(Fr(56,10),'Oranı ters yazarak pOH = 5 + 0,6 = 5,6 bulmuş ve bunu pH olarak vermiştir.','islem'),
   (Fr(84,10),'[NH₃]/[NH₄⁺] oranını ters yazarak pH = 9 − 0,6 = 8,4 bulmuştur.','islem'),(Fr(90,10),'Tamponda pH = pKa olduğunu sanarak 9 bulmuştur; oysa oran 1 değildir.','bilgi')],
 istenen='Oluşan çözeltinin pH değeri.',ip=['Tuz çözeltisinin pH değerinden eşlenik çiftin sabitini bul, sonra NaOH ekledikten sonra ortamda ne kaldığına bak.'],bilgi=[B_HID,B_TAM],
 puf='Önce hidrolizden pKa’yı bul, sonra tepkimeye göre mol sayılarını güncelleyip Henderson bağıntısını uygula.')
# ======================================================================
# 0009 · zor · tanecik modeli, tampon hazırlama  (B: 300)
# ======================================================================
tan=Fr(1,100); HAn,Aan=8*tan,2*tan; assert 5+2*0.3==5.6
x9=Fr(6,100); assert (Aan+x9)/(HAn-x9)==4 and x9/Fr(2,10)*1000==300
assert (Aan+Fr(3,100))/(HAn-Fr(3,100))==1 and Fr(3,100)/Fr(2,10)*1000==150
x2=Fr(64,1000); assert x2/(HAn-x2)==4 and x2/Fr(2,10)*1000==320
assert HAn/Fr(2,10)*1000==400
x4=4*HAn-Aan; assert x4==Fr(3,10) and x4/Fr(2,10)*1000==1500
poz=[(-1.2,1.65),(-.4,1.65),(.4,1.65),(1.2,1.65),(-1.2,1.0),(-.4,1.0),(.4,1.0),(1.2,1.0)]
s=['\\draw[thick] (-1.7,2.3) -- (-1.7,-.1) -- (1.7,-.1) -- (1.7,2.3);','\\draw[vurgu] (-1.68,2.05) -- (1.68,2.05);']
for (x,y) in poz: s.append(f'\\draw[fill=white] ({x-.1:.2f},{y:.2f}) circle (.1); \\draw[fill=gray!35] ({x+.07:.2f},{y:.2f}) circle (.17);')
for (x,y,kind) in [(-1.2,.35,'A'),(-.4,.35,'N'),(.4,.35,'A'),(1.2,.35,'N')]:
    if kind=='A': s.append(f'\\draw[fill=gray!35] ({x:.2f},{y:.2f}) circle (.2); \\node[font=\\small] at ({x:.2f},{y:.2f}) {{$-$}};')
    else: s.append(f'\\draw[fill=white] ({x:.2f},{y:.2f}) circle (.17); \\node[font=\\small] at ({x:.2f},{y:.2f}) {{$+$}};')
s+=['\\draw[fill=white] (2.2,1.9) circle (.1); \\draw[fill=gray!35] (2.37,1.9) circle (.17); \\node[anchor=west] at (2.7,1.9) {\\ce{HA}};',
    '\\draw[fill=gray!35] (2.35,1.25) circle (.2); \\node[font=\\small] at (2.35,1.25) {$-$}; \\node[anchor=west] at (2.7,1.25) {\\ce{A-}};',
    '\\draw[fill=white] (2.35,.6) circle (.17); \\node[font=\\small] at (2.35,.6) {$+$}; \\node[anchor=west] at (2.7,.6) {\\ce{Na+}};']
sk=fig(*s)
q('0009',5,[A('Mol sayıları','Her tanecik 0,01 mol olduğundan şekildeki sayılar mole çevrilir.','n(HA) = 0,08 mol, n(A⁻) = 0,02 mol'),
   A('Hedef oran','pH = pKa + log([A⁻]/[HA]) bağıntısında pKa = 5 ve log 4 = 0,6 alınır.','5,6 = 5 + log oran → oran = 4'),
   A('NaOH mol sayısı','x mol NaOH, x mol HA’yı harcar ve x mol A⁻ oluşturur: (0,02 + x)/(0,08 − x) = 4.','x = 0,06 mol'),
   A('Hacim','V = n/M bağıntısı kullanılır.','V = 0,06/0,2 = 0,3 L = 300 mL')],
 tipId='ab-tampon',z='zor',alt='Tamponun pH Değerini Ayarlama',kaz='Tanecik modelinden mol sayılarını okuyarak hedef pH için eklenmesi gereken kuvvetli baz hacmini hesaplar.',kalip='şekilli',
 metin='Ka değeri 1·10⁻⁵ olan zayıf HA asidinin sulu çözeltisine bir miktar NaOH eklenmesiyle hazırlanan çözeltideki taneciklerin modeli şekilde verilmiştir (su molekülleri gösterilmemiştir). Şekildeki her tanecik 0,01 mol’ü temsil etmektedir.\nBu çözeltiye 0,2 M NaOH çözeltisinden bir miktar eklenerek pH değeri 5,6 olan bir çözelti elde edilecektir. NaOH’nin HA ile tam tepkime verdiği ve hacimlerin toplanabildiği kabul edilecektir. (log 2 = 0,3)\nBuna göre, kaç mL NaOH çözeltisi eklenmelidir?',
 sekil=sk,dogru=300,yan=[(150,'Hedef pH’ı pKa’ya eşit sanarak [A⁻] = [HA] koşulunu kurmuş ve 150 mL bulmuştur.','dikkat'),(320,'Çözeltide başlangıçtan beri bulunan 0,02 mol A⁻’yi yok sayarak 320 mL bulmuştur.','islem'),
   (400,'Tüm HA’yı (0,08 mol) nötrleştirmek için gereken hacmi (400 mL) vermiştir.','dikkat'),(1500,'HA mol sayısını azaltmayı unutup (0,02 + x) = 4 · 0,08 yazarak 1500 mL bulmuştur.','islem')],
 istenen='Eklenmesi gereken NaOH çözeltisi hacmi (mL).',ip=['Şekildeki tanecik sayılarını mol sayısına çevir ve hedef pH’ın hangi mol oranını gerektirdiğini düşün.'],bilgi=[B_TAM,B_NOT],
 puf='Eklenen NaOH, HA’dan ne kadar azaltıyorsa A⁻’yi o kadar artırır; oranı bu iki değişimle kur.')
# ======================================================================
# 0010 · zor · iki zayıf asit titrasyonu → NaX pH  (D: 8)
# ======================================================================
KaX,KaY=1e-4,1e-6
def egr(Ka): return [(v,ph_acid(Ka,2.0,0.1,v,20)) for v in list(range(0,16))+[17,18,19,19.5,19.9,20,20.1,20.5,21,22,24,26,28,30,34,38,40]]
cX,cY=egr(KaX),egr(KaY)
d10=dict(cX); assert abs(d10[10]-4)<.06 and abs(dict(cY)[10]-6)<.06
Kb=Fr(1,10**14)/Fr(1,10**4); assert Kb==Fr(1,10**10) and math.isclose(math.sqrt(float(Kb*Fr(1,100))),1e-6)
KbY=Fr(1,10**14)/Fr(1,10**6); assert math.isclose(math.sqrt(float(KbY*Fr(1,100))),1e-5)
sk=pg('width=7.4cm,height=5.4cm,axis lines=left,xmin=0,xmax=40,ymin=0,ymax=14,xtick={0,10,20,30,40},ytick={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14},grid=major,grid style={gray!30},xlabel={NaOH çözeltisi hacmi (mL)},ylabel={pH},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(cX)}}};\n\\addplot[thick,dashed,color=red!70!black] coordinates {{{co(cY)}}};\n\\node[anchor=north west,font=\\small] at (axis cs:11,3.3) {{\\textbf{{X}}}};\n\\node[anchor=south east,font=\\small] at (axis cs:9.3,7) {{\\textbf{{Y}}}};')
q('0010',4,[A('Ka değerini bul','Eşdeğerlik 20 mL’dedir; yarı eşdeğerlik noktası 10 mL’de [HX] = [X⁻] olur ve pH = pKa’dır. X eğrisinde bu noktada pH = 4’tür.','pKa = 4 → Ka = 10⁻⁴'),
   A('Kb değerini bul','Eşlenik baz için Kb = Kw/Ka kullanılır.','Kb(X⁻) = 10⁻¹⁴/10⁻⁴ = 10⁻¹⁰'),
   A('Hidroliz','X⁻ + H₂O ⇌ HX + OH⁻ dengesinde [OH⁻] = √(Kb·C).','[OH⁻] = √(10⁻¹⁰ · 10⁻²) = 10⁻⁶ M'),
   A('pH','pOH = 6 olduğundan pH = 14 − 6.','pH = 8')],
 tipId='ab-titra',z='zor',alt='Titrasyon Eğrisi ve Tuz Çözeltisi',kaz='İki titrasyon eğrisinden zayıf asidin Ka değerini okur ve bu asidin tuz çözeltisinin pH değerini hesaplar.',kalip='grafik',
 metin='25 °C’de X ve Y monoprotik zayıf asitlerinin 20 mL’lik 0,1 M sulu çözeltileri ayrı ayrı 0,1 M NaOH çözeltisiyle titre ediliyor ve pH–NaOH hacmi grafikleri aynı eksende şekilde verilmiştir. Hidroliz eden iyon miktarı başlangıç derişimine göre ve suyun iyonlaşması ihmal edilecek; Kw = 1·10⁻¹⁴ alınacaktır.\nBuna göre, X asidinin sodyum tuzu olan NaX’in 0,01 M’lik sulu çözeltisinin pH değeri kaçtır?',
 sekil=sk,dogru=8,yan=[(4,'X eğrisinin yarı eşdeğerlik pH değerini (4) tuz çözeltisinin pH değeri sanmıştır.','dikkat'),(6,'Y eğrisinin yarı eşdeğerlik pH değerini (6) okuyup tuz çözeltisinin pH değeri olarak vermiştir.','dikkat'),
   (7,'NaX tuzunun hidroliz etmediğini düşünüp çözeltinin nötr (pH = 7) olduğunu sanmıştır.','bilgi'),(9,'X yerine Y asidinin tuzu için hesap yaparak [OH⁻] = 10⁻⁵ M ve pH = 9 bulmuştur.','islem')],
 istenen='NaX çözeltisinin pH değeri.',ip=['Grafikten X’in Ka değerine ulaşmanın yolunu ara; sonra tuzun suda nasıl davrandığını düşün.'],bilgi=[B_TIT,B_HID],
 puf='Önce yarı eşdeğerlikten Ka’yı, sonra Kb = Kw/Ka ile tuzun hidrolizini kur.')
# ====================== BİTİŞ ======================
for x in P.ANA: x['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/aasb'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'aasitbaziki-1.json'),os.path.join(SC,'bos-aasitbaziki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='akim|'+KONUAD))['kartlar'].append(c['id'])
json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 12. sınıf kimya müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akasitbaziki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
