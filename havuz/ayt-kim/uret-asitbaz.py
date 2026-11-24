"""AYT Kimya · Asit-Baz Dengesi · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ/tablo; her sayı Python'da (Fraction/float) hesaplanıp assert edilir."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
from _hafif_kim import onc,tek,etk
KONUAD='Asit-Baz Dengesi'
H.KONU=KONUAD
P=Parti('asitbaz',KONUAD,'akim|'+KONUAD,ders='AYT Kimya',idon='aytkim')
ALT='Asit-Baz Dengesi'
KY='ÖSYM AYT 2018–2026 Kimya (yalnız mantık) · MEB 12. sınıf kimya'
def q(no,**k):
    assert len(k['ip'])==1
    mk(P,no,adim=len(k['ad']),ad=k.pop('ad'),**k)
SUP=str.maketrans('0123456789-+','⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺')
def e(m,n): return f'{m}·10{str(n).translate(SUP)}'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\footnotesize]\n'
TAIL='\n\\end{tikzpicture}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
def lg(x):
    x=Fr(x); n,d=x.numerator,x.denominator
    if n==1 and d>=1:
        k=0
        while d>1: assert d%10==0; d//=10; k+=1
        return k            # -log10(x)
    raise AssertionError(x)
def pHof(h): return lg(h)
# ---------------- titrasyon eğrisi yardımcıları ----------------
def ph_weak(Ka,nA,nB,V):   # nA, nB mmol; V mL; Ka mol/L (HA + NaOH)
    CT=nA/V; Na=nB/V; Kw=1e-14
    lo,hi=-14.0,1.0
    for _ in range(200):
        m=(lo+hi)/2; h=10**m
        f=h+Na-CT*Ka/(Ka+h)-Kw/h
        if f>0: hi=m
        else: lo=m
    return -(lo+hi)/2
def ph_strong(nA,nB,V):
    net=(nA-nB)/V
    h=(net+math.sqrt(net*net+4e-14))/2
    return -math.log10(h)
def egri(curves,xmax,xt,xlab,sx=.14,sy=.34,ytick=1):
    """curves: [(noktalar,stil,etiket,(lx,ly))] ; stil TikZ."""
    W=xmax*sx; Hh=14*sy; p=[]
    for y in range(0,15): p.append(f'\\draw[gray!35,very thin] (0,{y*sy:.2f}) -- ({W:.2f},{y*sy:.2f});')
    for x in xt: p.append(f'\\draw[gray!35,very thin] ({x*sx:.2f},0) -- ({x*sx:.2f},{Hh:.2f});')
    p.append(f'\\draw[thick] (0,{Hh+.15:.2f}) -- (0,0) -- ({W+.15:.2f},0);')
    for y in range(0,15,ytick): p.append(f'\\node[left=1pt] at (0,{y*sy:.2f}) {{{y}}};')
    for x in xt: p.append(f'\\node[below=1pt] at ({x*sx:.2f},0) {{{x}}};')
    p.append(f'\\node[above] at (0,{Hh+.1:.2f}) {{pH}};')
    p.append(f'\\node[below=11pt] at ({W/2:.2f},0) {{{xlab}}};')
    for pts,stil,et,(lx,ly) in curves:
        co=' '.join(f'({x*sx:.3f},{y*sy:.3f})' for x,y in pts)
        p.append(f'\\draw[{stil}] plot coordinates {{{co}}};')
        if et: p.append(f'\\node at ({lx*sx:.2f},{ly*sy:.2f}) {{{et}}};')
    return p
def kap(cx,etiket_ic,alt,h=1.5,sivi=True):
    w=1.15; t=2.1
    s=[f'\\draw[thick] ({cx-w:.2f},{t}) -- ({cx-w:.2f},0) -- ({cx+w:.2f},0) -- ({cx+w:.2f},{t});']
    if sivi: s.append(f'\\fill[vurgu!15] ({cx-w+.02:.2f},.02) rectangle ({cx+w-.02:.2f},{h});\\draw[vurgu] ({cx-w+.02:.2f},{h}) -- ({cx+w-.02:.2f},{h});')
    for i,l in enumerate(etiket_ic): s.append(f'\\node at ({cx:.2f},{h-.4-i*.42:.2f}) {{{l}}};')
    s.append(f'\\node[below=2pt,align=center] at ({cx:.2f},0) {{{alt}}};')
    return s
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
S5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
S5b=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
# =============== BİLGİ KUTULARI (örnekler sorulardan farklı) ===============
B_PH=B('pH, pOH ve H⁺/OH⁻ derişimi','25 °C’de pH = −log[H⁺], pOH = −log[OH⁻] ve pH + pOH = 14’tür; [H⁺]·[OH⁻] = 10⁻¹⁴’tür. Kuvvetli asit ve bazlar tamamen iyonlaşır, bazın formülündeki OH⁻ sayısı derişimi katlar. Örnek: 0,02 M KOH çözeltisinde [OH⁻] = 2·10⁻² M’dir')
B_SEY=B('Seyrelme ve karıştırma','Çözeltiye su eklenince mol sayısı değişmez, derişim toplam hacimle ters orantılı azalır: M₁V₁ = M₂V₂. Asit ve baz karışınca önce mol sayıları karşılaştırılır, artan madde toplam hacme bölünür. Örnek: 10 mL 0,5 M çözelti 100 mL’ye tamamlanırsa derişim 0,05 M olur')
B_KA=B('Ka, Kb ve iyonlaşma yüzdesi','HA ⇌ H⁺ + A⁻ için Ka = [H⁺][A⁻]/[HA]’dır; zayıf asitte [H⁺] ≈ [A⁻] ve [HA] ≈ başlangıç derişimidir. İyonlaşma yüzdesi = (iyonlaşan/başlangıç) · 100’dür. Baz için Kb aynı biçimde yazılır. Örnek: 0,2 M HA’da [H⁺] = 2·10⁻³ M ise Ka = (2·10⁻³)²/0,2 = 2·10⁻⁵’tir')
B_KAK=B('Asit kuvveti','Ka büyüdükçe asit kuvvetlenir, aynı derişimde iyonlaşma yüzdesi ve [H⁺] artar. Asit güçlendikçe eşlenik bazı zayıflar; Ka·Kb = Kw = 10⁻¹⁴’tür. Örnek: Ka’sı büyük olan asidin aynı derişimdeki çözeltisinin pH’ı daha küçüktür')
B_TIT=B('Titrasyon eğrisi','Eşdeğerlik noktasında asit ve bazın mol sayıları (ağırlıklı katsayılarla) eşittir: n(H⁺) = n(OH⁻). Kuvvetli asit–kuvvetli baz eşdeğerliğinde pH = 7, zayıf asit–kuvvetli baz eşdeğerliğinde pH > 7, zayıf baz–kuvvetli asit eşdeğerliğinde pH < 7’dir. Zayıf asitte yarı eşdeğerlik noktasında pH = pKa’dır. Örnek: 20 mL 0,1 M HCl’yi nötrleştiren 0,2 M NaOH hacmi 10 mL’dir')
B_TAM=B('Tampon çözelti','Zayıf asit ile eşlenik bazı (ya da zayıf baz ile eşlenik asidi) birlikte bulunan çözeltidir; az miktarda asit ya da baz eklenince pH çok az değişir. pH = pKa + log([A⁻]/[HA]) bağıntısı kullanılır. Eklenen H⁺ bazik bileşeni (A⁻), eklenen OH⁻ asidik bileşeni (HA) harcar. Örnek: [A⁻] = [HA] ise pH = pKa’dır')
B_HID=B('Tuzların hidrolizi','Zayıf asidin eşlenik bazı olan anyon suyla tepkimeye girip OH⁻ oluşturur (bazik); zayıf bazın eşlenik asidi olan katyon H⁺ oluşturur (asidik). Kuvvetli asit/baz iyonları hidroliz olmaz. A⁻ + H₂O ⇌ HA + OH⁻ için Kb = Kw/Ka’dır. Örnek: NaCl çözeltisi hidroliz olmadığı için nötrdür')
B_NOT=B('Nötrleşme ve indikatör','H⁺ + OH⁻ → H₂O; mol hesabında asidin verdiği H⁺ sayısı ile bazın verdiği OH⁻ sayısı eşitlenir (H₂SO₄ 2, Ba(OH)₂ 2 yük taşır). İndikatör, renk değiştirdiği pH aralığı eşdeğerlik noktasındaki pH’ı içeriyorsa uygundur. Örnek: pH 7’de nötr, pH 10’da bazik; renk aralığı 6–8 olan indikatör pH 7 eşdeğerliği için uygundur')
# =============== KARTLAR ===============
kartla('K-AKASB-01','pH, pOH ve karışımlar','pH = −log[H⁺] ve pH + pOH = 14 ile çözeltinin pH’ı bulunur; seyrelmede mol sabit kalır, asit–baz karışımında artan madde toplam hacme bölünür.','pH ile pOH’u karıştırmak; baz formülündeki OH⁻ sayısını unutmak; mL–L dönüşümü ve toplam hacmi atlamak.','orta','şekilli',3,'ab-ph','pH, pOH ve seyrelme/karıştırma hesapları')
kartla('K-AKASB-02','Ka, Kb ve iyonlaşma','Zayıf asit–bazda Ka (Kb) = [iyon]²/[başlangıç]; iyonlaşma yüzdesi seyrelmeyle artar, Ka yalnız sıcaklığa bağlıdır.','Ka’yı başlangıç derişimiyle karıştırmak; iyonlaşma yüzdesini derişimle doğru orantılı sanmak; Ka’nın derişimle değiştiğini düşünmek.','orta','şekilli',4,'ab-ka','Ka, Kb, asit kuvveti ve iyonlaşma yüzdesi')
kartla('K-AKASB-03','Titrasyon eğrisi okuma','Eğrinin sıçrama noktası eşdeğerliği verir; başlangıç pH, eşdeğerlik pH ve yarı eşdeğerlik pH’ından asit türü, derişim ve Ka çıkarılır.','Eşdeğerlik pH’ını her zaman 7 sanmak; yarı eşdeğerlik noktasını eşdeğerlik noktasıyla karıştırmak.','orta','grafik',4,'ab-titra','Titrasyon eğrisinden asit türü, derişim ve Ka çıkarma')
kartla('K-AKASB-04','Tampon çözelti','Tampon HA/A⁻ çiftidir; pH = pKa + log([A⁻]/[HA]); eklenen H⁺ A⁻’yi, eklenen OH⁻ HA’yı harcar.','Eklenen kuvvetli asit/baz sonrası mol sayısını güncellememek; oranı ters yazmak; yarı nötrleşmeyi tam nötrleşme sanmak.','orta','şekilli',4,'ab-tampon','Tampon çözelti: oluşum, etki ve pH hesabı')
kartla('K-AKASB-05','Tuz çözeltilerinin hidrolizi','Zayıf asidin tuzu bazik, zayıf bazın tuzu asidik çözelti verir; Kb(A⁻) = Kw/Ka ile pH ve Ka birbirine dönüştürülür.','Her tuzun nötr olduğunu sanmak; Ka yerine Kb kullanmak; hidroliz derişimini başlangıç derişimiyle karıştırmak.','orta','tablo',4,'ab-hidroliz','Tuz çözeltilerinin hidrolizi, pH ve Ka ilişkisi')
kartla('K-AKASB-06','Nötrleşme hesabı ve indikatör','Tam nötrleşmede n(H⁺) = n(OH⁻); titrasyonda büret okumasından hacim, eşdeğerlik pH’ından uygun indikatör bulunur.','Çok değerlikli asit/bazda katsayıyı atlamak; büret son okumasını hacim saymak; eşdeğerlik pH’ını 7 almak.','orta','şekilli',4,'ab-notrles','Nötrleşme hesabı ve indikatör seçimi')
# ========================================================================
# 0001 · kolay · tablo: [H⁺] → pOH
# ========================================================================
tab=[('X',e(1,-3)),('Y',e(1,-11)),('Z',e(1,-5)),('T',e(1,-13)),('U',e(1,-9))]
pHs={'X':3,'Y':11,'Z':5,'T':13,'U':9}
pOH={k:14-v for k,v in pHs.items()}; assert [k for k,v in pOH.items() if v==5]==['U'] and pOH['Z']==9 and pOH['Y']==3 and pOH['X']==11 and pOH['T']==1
sk=tablo_svg(['Çözelti','[H⁺] (mol/L)'],[list(r) for r in tab])
q('0001',tipId='ab-ph',tip='pH, pOH ve seyrelme/karıştırma hesapları',z='kolay',alt=ALT,kaz='H⁺ derişiminden pH ve pOH değerlerini hesaplar.',kalip='tablo',
 kart='K-AKASB-01 (pH–pOH) · tabloda [H⁺] verilmiş, pOH = 5 aranıyor',
 metin='Bir öğrenci 25 °C’de hazırladığı beş farklı sulu çözeltinin H⁺ derişimini ölçüyor ve sonuçları tabloya kaydediyor. Çözeltilerin hiçbirinde başka bir asit ya da baz bulunmamaktadır.\nBuna göre, hangi çözeltinin pOH değeri 5’tir?',
 dogru='U',yan=[('X','X çözeltisinin pH değeri 3, pOH değeri 11’dir; öğrenci pH’ı yanlış yöne çevirmiştir.','dikkat'),('Y','Y çözeltisinin pH değeri 11, pOH değeri 3’tür.','bilgi'),('Z','Z çözeltisinin pH değeri 5’tir; öğrenci pH ile pOH’u karıştırmıştır, pOH değeri 9’dur.','dikkat'),('T','T çözeltisinin pH değeri 13, pOH değeri 1’dir.','bilgi')],
 sira=['X','Y','Z','T','U'],istenen='pOH değeri 5 olan çözelti.',ip=['pOH değerini, pH ile aralarındaki bağıntıyı kullanarak H⁺ derişimine çevir.'],
 bilgi=[B_PH],sekil=sk,
 ad=[A('pH’ı bul','pH + pOH = 14 olduğundan pOH = 5 ise pH = 14 − 5 değerindedir.','pH = 9'),A('H⁺ derişimini yaz','pH = 9 için [H⁺] = 10⁻⁹ M olur.','[H⁺] = 1·10⁻⁹ M'),A('Tabloyla eşleştir','Bu değer tabloda U çözeltisine aittir.','U')],
 puf='pOH’tan pH’a, oradan [H⁺] derişimine geç; aranan üs sayısı hep pH’tır.')
# ========================================================================
# 0002 · kolay · öncüllü pH
# ========================================================================
d={'I':(True,'HCl kuvvetli asit olduğundan 0,01 M çözeltisinde [H⁺] = 10⁻² M’dir ve pH = 2’dir'),
   'II':(False,'0,01 M NaOH çözeltisinde [OH⁻] = 10⁻² M, yani pOH = 2’dir; pH değeri 12’dir'),
   'III':(True,'pH = 3 ise [H⁺] = 10⁻³ M olur ve [OH⁻] = 10⁻¹⁴/10⁻³ = 10⁻¹¹ M’dir')}
assert Fr(1,10**14)/Fr(1,10**3)==Fr(1,10**11)
r=onc(d,[('I',),('I','II'),('I','III'),('II','III'),('I','II','III')])
q('0002',tipId='ab-ph',tip='pH, pOH ve seyrelme/karıştırma hesapları',z='kolay',alt=ALT,kaz='Kuvvetli asit ve bazların pH ve pOH değerlerini yorumlar.',kalip='öncüllü',
 kart='K-AKASB-01 (pH–pOH) · 0,01 M HCl, 0,01 M NaOH, pH = 3',
 metin='HCl ve NaOH, sulu çözeltilerinde tamamen iyonlaşan kuvvetli elektrolitlerdir. Aynı sıcaklıkta (25 °C) yapılan değerlendirmede aşağıdaki yargılar ileri sürülüyor.\nI. 0,01 M HCl çözeltisinin pH değeri 2’dir.\nII. 0,01 M NaOH çözeltisinin pH değeri 2’dir.\nIII. pH değeri 3 olan çözeltide OH⁻ derişimi 10⁻¹¹ M’dir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her çözeltide önce iyonlaşma ürünü olan iyonun derişimini yaz, sonra pH ve pOH bağıntısına git.'],
 bilgi=[B_PH],
 ad=[A('I. yargı','HCl tamamen iyonlaşır, [H⁺] = 0,01 M.','pH = 2 → doğru'),A('II. yargı','NaOH’tan gelen OH⁻ derişimi 0,01 M’dir; bu pOH’tır.','pOH = 2, pH = 12 → yanlış'),A('III. yargı','pH = 3 ise [H⁺] = 10⁻³ M’dir; [H⁺][OH⁻] = 10⁻¹⁴.','[OH⁻] = 10⁻¹¹ M → doğru'),A('Sonuç','Doğru yargılar birleştirilir.',etk(d)+' · Sonuç: I ve III')],
 puf='Bazın çözeltisinde derişimden doğrudan pOH bulunur; pH için 14’ten çıkarmayı unutma.')
# ========================================================================
# 0003 · kolay · tablo Ka, olumsuz kök
# ========================================================================
Ka3={'HX':Fr(1,10**3),'HY':Fr(1,10**5),'HZ':Fr(1,10**8),'HT':Fr(1,10**10)}
sk=tablo_svg(['Asit','Ka (25 °C)'],[['HX',e(1,-3)],['HY',e(1,-5)],['HZ',e(1,-8)],['HT',e(1,-10)]])
S=[('En küçük pH değerine sahip çözelti HX çözeltisidir.',True,'Ka değeri en büyük olan HX en çok iyonlaşır, [H⁺] en büyük olur ve pH en küçüktür'),
   ('İyonlaşma yüzdesi en küçük olan asit HT’dir.',True,'Ka değeri en küçük olan HT en az iyonlaşır'),
   ('Z⁻ iyonu, Y⁻ iyonundan daha kuvvetli bir bazdır.',True,'HZ, HY’den daha zayıf asit olduğundan eşlenik bazı Z⁻ daha kuvvetlidir'),
   ('T⁻ iyonu, dört anyon arasında en kuvvetli bazdır.',True,'en zayıf asit olan HT’nin eşlenik bazı en kuvvetlidir'),
   ('HY çözeltisinin [H⁺] derişimi, HZ çözeltisininkinden küçüktür.',False,'Ka(HY) > Ka(HZ) olduğundan HY çözeltisinde [H⁺] daha büyüktür')]
assert Ka3['HX']>Ka3['HY']>Ka3['HZ']>Ka3['HT']
r=tek(S,False)
q('0003',tipId='ab-ka',tip='Ka, Kb, asit kuvveti ve iyonlaşma yüzdesi',z='kolay',alt=ALT,kaz='Ka değerlerinden asit kuvveti, pH ve eşlenik baz kuvveti karşılaştırması yapar.',kalip='tablo',
 kart='K-AKASB-02 (asit kuvveti) · dört asidin Ka tablosu',
 metin='Tabloda dört monoprotik zayıf asidin 25 °C’deki iyonlaşma sabitleri (Ka) verilmiştir. Bu asitlerin aynı derişimli ve aynı sıcaklıktaki sulu çözeltileri hazırlanıyor.\nBuna göre aşağıdaki yargılardan hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yargı.',ip=['Ka büyüdükçe asidin ve eşlenik bazının kuvvetinin nasıl değiştiğini düşün.'],
 bilgi=[B_KAK],sekil=sk,
 ad=[A('Asit kuvveti sırası','Ka büyüklüğüne göre sıralanır.','HX > HY > HZ > HT'),A('Eşlenik baz sırası','Asit zayıfladıkça eşlenik baz kuvvetlenir.','X⁻ < Y⁻ < Z⁻ < T⁻'),A('Yargıları tek tek sına','pH, iyonlaşma yüzdesi ve [H⁺] aynı sıralamayı izler; HY çözeltisinin [H⁺] derişimi HZ’ninkinden büyüktür.','Yanlış yargı: HY’nin [H⁺] derişimi HZ’ninkinden küçüktür.')],
 puf='Asit kuvveti ile eşlenik baz kuvveti zıt yönlü, asit kuvveti ile [H⁺] aynı yönlüdür.')
# ========================================================================
# 0004 · orta · seyrelme pH 2 → 3
# ========================================================================
h0=Fr(1,100); V0=50; Vs=450; Vt=V0+Vs; h1=h0*V0/Vt; assert h1==Fr(1,1000) and pHof(h1)==3
assert pHof(h0*V0/Vt/10)==4 and pHof(h0)==2 and pHof(h0*V0/Vt/100)==5
sk=fig(*kap(0,['50 mL','\\ce{HCl}(suda)','pH $=2$'],'',h=1.5),
 '\\node at (1.95,1.0) {\\Large $+$};',
 *kap(3.9,['450 mL','saf su'],'',h=1.5),
 '\\draw[-{Stealth[length=2.2mm]},thick] (5.35,1.0) -- (6.35,1.0);',
 *kap(7.9,['500 mL','\\ce{HCl}(suda)','pH $=\\,?$'],'',h=1.5))
q('0004',tipId='ab-ph',tip='pH, pOH ve seyrelme/karıştırma hesapları',z='orta',alt=ALT,kaz='Kuvvetli asit çözeltisinin seyrelmesiyle pH değişimini hesaplar.',kalip='şekilli',
 kart='K-AKASB-01 (seyrelme) · pH = 2 çözeltisi 10 kat seyreltiliyor',
 metin='Bir öğrenci, 25 °C’de kuvvetli bir asit olan HCl’nin sulu çözeltisi ile şekildeki işlemi yapıyor. Kaplardaki sıvılar tamamen karıştırılıyor ve hacimlerin toplandığı kabul ediliyor.\nBuna göre, son kaptaki çözeltinin pH değeri kaçtır?',
 dogru=3,yan=[(5,'[H⁺] derişimini hacim oranının üçüncü kuvveti kadar (1000 kat) azaltmış.','islem'),(2,'Seyrelmeyle pH değerinin değişmediğini sanmış.','bilgi'),(4,'[H⁺] derişimini hacim oranının karesi kadar (100 kat) azaltmış.','islem'),(7,'Asit çözeltisinin su ekledikçe nötr hâle geldiğini sanmış.','bilgi')],
 istenen='Son çözeltinin pH değeri.',ip=['Seyrelmede H⁺ mol sayısının değişmediğini, derişimin ise toplam hacme bağlı olduğunu kullan.'],
 bilgi=[B_SEY,B_PH],sekil=sk,
 ad=[A('Başlangıç [H⁺]','pH = 2 için [H⁺] = 10⁻² M.','[H⁺] = 0,01 M'),A('H⁺ mol sayısı','Mol sayısı derişim ile hacmin çarpımıdır.','n = 0,01 · 0,05 = 5·10⁻⁴ mol'),A('Yeni derişim','Toplam hacim 500 mL = 0,5 L.','[H⁺] = 5·10⁻⁴/0,5 = 10⁻³ M'),A('pH','pH = −log[H⁺].','pH = 3')],
 puf='Seyrelmede mol sayısı sabit kalır; derişim, toplam hacme bölünerek yeniden bulunur.')
# ========================================================================
# 0005 · orta · öncüllü zayıf baz, %iyonlaşma
# ========================================================================
C5=Fr(1,2); al=Fr(2,1000); OH=C5*al; Kb5=OH**2/C5
assert OH==Fr(1,1000) and Kb5==Fr(2,10**6) and pHof(OH)==3 and 14-3==11
d={'I':(True,'OH⁻ derişimi 0,5 M · 0,002 = 10⁻³ M’dir'),
   'II':(True,'pOH = 3 olduğundan pH = 14 − 3 = 11’dir'),
   'III':(True,'Kb = (10⁻³)²/0,5 = 2·10⁻⁶’dır')}
r=onc(d,[('I',),('I','II'),('I','III'),('II','III'),('I','II','III')])
q('0005',tipId='ab-ka',tip='Ka, Kb, asit kuvveti ve iyonlaşma yüzdesi',z='orta',alt=ALT,kaz='Zayıf bazın iyonlaşma yüzdesinden OH⁻ derişimi, pH ve Kb değerini hesaplar.',kalip='öncüllü',
 kart='K-AKASB-02 (Kb) · 0,5 M baz, %0,2 iyonlaşma',
 metin='25 °C’de 0,5 M’lik zayıf B bazının sulu çözeltisinde, çözünen B moleküllerinin %0,2’si aşağıdaki denkleme göre iyonlaşmaktadır.\nB(suda) + H₂O(s) ⇌ BH⁺(suda) + OH⁻(suda)\nDenge anında B derişiminin başlangıç derişimine eşit olduğu kabul edilirse,\nI. çözeltideki OH⁻ derişimi 1·10⁻³ M’dir.\nII. çözeltinin pH değeri 11’dir.\nIII. B bazının iyonlaşma sabiti (Kb) 2·10⁻⁶’dır.\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['İyonlaşma yüzdesini derişime çevirerek OH⁻ derişimini bul, sonra bu değeri diğer büyüklüklere taşı.'],
 bilgi=[B_KA],
 ad=[A('OH⁻ derişimi','İyonlaşan B derişimi kadar OH⁻ oluşur.','[OH⁻] = 0,5 · 0,002 = 10⁻³ M → I doğru'),A('pH','pOH = 3 olduğundan pH = 14 − pOH.','pH = 11 → II doğru'),A('Kb','Denge ifadesinde [BH⁺] = [OH⁻] ve [B] ≈ 0,5.','Kb = (10⁻³)²/0,5 = 2·10⁻⁶ → III doğru'),A('Sonuç','Üç yargı da doğrudur.',etk(d)+' · Sonuç: I, II ve III')],
 puf='Yüzdeyi önce kesre çevir; iyonlaşan miktar ile başlangıç derişimini çarp.')
# ========================================================================
# 0006 · orta · tanecik modeli → Ka
# ========================================================================
HA,Hp,Am=8,2,2; u=Fr(5,100); cHA,cH,cA=HA*u,Hp*u,Am*u
Ka6=cH*cA/cHA; assert Ka6==Fr(25,1000) and cH*cA/(10*u)==Fr(2,100) and cH==Fr(1,10) and cH/cHA==Fr(1,4) and Fr(Hp*Am,HA)==Fr(1,2)
def tane():
    # kap içinde sabit konumlar; HA = iki bitişik daire (küçük H + büyük A), H+ = küçük daire +, A- = büyük daire −
    pos=[(-1.4,1.45),(-.5,1.45),(.4,1.45),(1.3,1.45),(-1.35,.8),(-.45,.8),(.45,.8),(1.35,.8),(-1.1,.2),(-.25,.25),(.55,.2),(1.25,.2)]
    HAp=pos[:8]; rest=pos[8:]
    s=['\\draw[thick] (-1.9,2.1) -- (-1.9,-.1) -- (1.9,-.1) -- (1.9,2.1);','\\draw[vurgu] (-1.88,1.85) -- (1.88,1.85);']
    for (x,y) in HAp: s.append(f'\\draw[fill=white] ({x-.1:.2f},{y:.2f}) circle (.1); \\draw[fill=gray!30] ({x+.07:.2f},{y:.2f}) circle (.17);')
    hp=[(-1.5,.2),(.1,.5)]; am=[(.9,.5),(-.7,.45)]
    # H⁺ ve A⁻ konumları (HA ile çakışmayacak biçimde ikinci satıra yerleştirilir)
    hp=[(-1.45,.2),(.05,.2)]; am=[(-.6,.2),(.95,.2)]
    for (x,y) in hp: s.append(f'\\draw[fill=white] ({x:.2f},{y:.2f}) circle (.15); \\node[font=\\footnotesize] at ({x:.2f},{y:.2f}) {{$+$}};')
    for (x,y) in am: s.append(f'\\draw[fill=gray!30] ({x:.2f},{y:.2f}) circle (.2); \\node[font=\\footnotesize] at ({x:.2f},{y:.2f}) {{$-$}};')
    return s
sk=fig(*tane(),
 '\\draw (2.6,1.75) circle (.1); \\draw[fill=gray!30] (2.77,1.75) circle (.17); \\node[right] at (3.05,1.75) {HA};',
 '\\draw[fill=white] (2.7,1.15) circle (.12); \\node[font=\\footnotesize] at (2.7,1.15) {$+$}; \\node[right] at (3.05,1.15) {\\ce{H+}};',
 '\\draw[fill=gray!30] (2.7,.55) circle (.2); \\node[font=\\footnotesize] at (2.7,.55) {$-$}; \\node[right] at (3.05,.55) {\\ce{A-}};',
 '\\node[right] at (2.4,-.3) {1 tanecik $=0{,}05$ M};')
q('0006',tipId='ab-ka',tip='Ka, Kb, asit kuvveti ve iyonlaşma yüzdesi',z='orta',alt=ALT,kaz='Tanecik modelinden denge derişimlerini okuyup Ka değerini hesaplar.',kalip='şekilli',
 kart='K-AKASB-02 (Ka, tanecik) · 8 HA, 2 H⁺, 2 A⁻',
 metin='25 °C’de monoprotik zayıf bir HA asidinin sulu çözeltisinde denge anındaki tanecikler şekildeki gibi modellenmiştir (su molekülleri gösterilmemiştir). Şekilde bir tanecik 0,05 M derişimi temsil etmektedir.\nBuna göre, HA asidinin iyonlaşma sabiti (Ka) kaçtır?',
 dogru='2,5·10⁻²',yan=[('2·10⁻²','Paydaya denge derişimi yerine başlangıç derişimi (0,5 M) yazmış: (0,1·0,1)/0,5.','dikkat'),('1·10⁻¹','Ka’yı H⁺ derişimine eşit almış.','bilgi'),('2,5·10⁻¹','Ka’yı [H⁺]/[HA] oranı olarak yazmış, A⁻ derişimini payda unutmuş.','islem'),('5·10⁻¹','Derişim yerine tanecik sayılarını kullanmış: (2·2)/8.','dikkat')],
 sira=['2·10⁻²','2,5·10⁻²','1·10⁻¹','2,5·10⁻¹','5·10⁻¹'],istenen='HA asidinin Ka değeri.',ip=['Ka bağıntısına tanecik sayısını değil, denge derişimlerini koymalısın.'],
 bilgi=[B_KA],sekil=sk,
 ad=[A('Derişimleri bul','Her tanecik 0,05 M’dir; şekilde 8 HA, 2 H⁺ ve 2 A⁻ vardır.','[HA] = 0,40 M · [H⁺] = [A⁻] = 0,10 M'),A('Ka bağıntısı','Ka = [H⁺][A⁻]/[HA].','Ka = (0,10 · 0,10)/0,40'),A('Hesapla','Çarpım ve bölme yapılır.','Ka = 2,5·10⁻²')],
 puf='Tanecik modellerinde önce sayıyı derişime çevir, sonra Ka’ya git.')
# ========================================================================
# 0007 · orta · öncüllü zayıf asit titrasyon eğrisi
# ========================================================================
Ka7=1e-5; nA7=2.5;
pts7=[]
for i in range(0,201):
    v=i*0.25
    pts7.append((v,ph_weak(Ka7,0.05*50,0.1*v,50+v)))
ph_eq7=ph_weak(Ka7,2.5,2.5,75); ph0_7=pts7[0][1]; ph_half=ph_weak(Ka7,2.5,1.25,62.5)
assert 8.7<ph_eq7<8.9 and 3.1<ph0_7<3.2 and abs(ph_half-5)<0.02 and -math.log10(0.05)<1.31
sk=fig(*egri([(pts7,'very thick','',(0,0))],50,[0,10,20,30,40,50],'Eklenen 0,1 M NaOH hacmi (mL)',sx=.16,sy=.3))
d={'I':(True,'başlangıç derişimi 0,05 M olan kuvvetli bir asidin pH değeri yaklaşık 1,3 olurdu; eğrinin başlangıç pH değeri 3 civarında olduğundan asit zayıftır'),
   'II':(True,'zayıf asidin tuzu eşdeğerlik noktasında hidroliz olup OH⁻ oluşturur; eğride bu noktanın pH değeri 7’nin üzerindedir'),
   'III':(False,'eşdeğerlik 25 mL NaOH ile sağlandığından n(HA) = 0,1 · 0,025 = 2,5 mmol ve derişim 2,5/50 = 0,05 M’dir')}
r=onc(d,[('I',),('I','II'),('I','III'),('II','III'),('I','II','III')])
q('0007',tipId='ab-titra',tip='Titrasyon eğrisinden asit türü, derişim ve Ka çıkarma',z='orta',alt=ALT,kaz='Titrasyon eğrisinden asidin türünü, derişimini ve eşdeğerlik noktasındaki karakteri yorumlar.',kalip='grafik',
 kart='K-AKASB-03 (eğri okuma) · 50 mL HA, 0,1 M NaOH',
 metin='25 °C’de 50 mL HA asidi çözeltisi 0,1 M NaOH çözeltisi ile titre ediliyor ve pH–NaOH hacmi grafiği çiziliyor.\nGrafiğe göre,\nI. HA zayıf bir asittir.\nII. eşdeğerlik noktasında çözeltinin pH değeri 7’den büyüktür.\nIII. HA çözeltisinin başlangıç derişimi 0,1 M’dir.\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Sıçrama noktasındaki hacimden asit derişimini bul, sonra başlangıç pH’ını bu derişimdeki kuvvetli asitle karşılaştır.'],
 bilgi=[B_TIT],sekil=sk,
 ad=[A('Eşdeğerlik hacmi','Grafikte pH’ın hızla yükseldiği nokta 25 mL’dir.','V(NaOH) = 25 mL'),A('Asit derişimi','n(HA) = n(NaOH) eşitliğiyle derişim bulunur.','M = 0,1 · 25/50 = 0,05 M → III yanlış'),A('Asit türü','0,05 M kuvvetli asidin pH’ı yaklaşık 1,3 olurdu; grafikte başlangıç pH 3 civarındadır.','HA zayıf → I doğru'),A('Eşdeğerlik pH’ı','Eğri bu noktada 7’nin üzerindedir.','pH > 7 → II doğru · Sonuç: I ve II')],
 puf='Önce sıçrama noktasındaki hacimden derişimi bul; başlangıç pH’ını o derişimdeki kuvvetli asitle kıyasla.')
# ========================================================================
# 0008 · zor · eğriden Ka → tuz pH
# ========================================================================
Ka8=1e-5; C8=0.1; V8=40; Cb8=0.2
pts8=[]
for i in range(0,161):
    v=i*0.25; pts8.append((v,ph_weak(Ka8,C8*V8,Cb8*v,V8+v)))
ph10=ph_weak(Ka8,C8*V8,Cb8*10,V8+10); assert abs(ph10-5)<0.01 and Cb8*20==C8*V8
Kh=Fr(1,10**14)/Fr(1,10**5); assert Kh==Fr(1,10**9); OH8=math.sqrt(1e-9*0.1); assert abs(OH8-1e-5)<1e-12
assert math.sqrt(1e-5*0.1)-1e-3<1e-12 and abs(-math.log10(OH8)-5)<1e-9
sk=fig(*egri([(pts8,'very thick','',(0,0))],40,[0,10,20,30,40],'Eklenen 0,2 M NaOH hacmi (mL)',sx=.2,sy=.3))
q('0008',tipId='ab-titra',tip='Titrasyon eğrisinden asit türü, derişim ve Ka çıkarma',z='zor',alt=ALT,kaz='Titrasyon eğrisinden Ka değerini bulup eşlenik bazın tuz çözeltisinin pH’ını hesaplar.',kalip='grafik',
 kart='K-AKASB-03 (eğri okuma, yarı eşdeğerlik) + K-AKASB-05 (hidroliz) · 40 mL HA, 0,2 M NaOH',
 metin='25 °C’de 40 mL HA zayıf asit çözeltisi 0,2 M NaOH çözeltisi ile titre ediliyor ve grafikteki titrasyon eğrisi elde ediliyor. Tuzun hidrolizi dışındaki dengeler ihmal edilecek ve Kw = 1·10⁻¹⁴ alınacaktır.\nBuna göre, aynı sıcaklıkta 0,1 M NaA tuzunun sulu çözeltisinin pH değeri kaçtır?',
 dogru=9,yan=[(3,'NaA çözeltisini asit gibi düşünüp [H⁺] = √(Ka·C) = 10⁻³ M almış.','bilgi'),(5,'Yarı eşdeğerlik noktasındaki pH değerini (pKa) tuz çözeltisinin pH’ı saymış.','dikkat'),(7,'Tuzun suda nötr çözelti oluşturduğunu sanmış.','bilgi'),(11,'Kb yerine Ka’yı kullanmış: [OH⁻] = √(Ka·C) = 10⁻³ M ve pH = 11.','islem')],
 istenen='0,1 M NaA çözeltisinin pH değeri.',ip=['Yarı eşdeğerlik noktasının hacmini önce eşdeğerlik hacminden bul; o noktadaki pH sana asidin kuvvetini verir.'],
 bilgi=[B_TIT,B_HID],sekil=sk,
 ad=[A('Eşdeğerlik hacmi','Sıçrama noktası grafikte 20 mL’dedir; yarı eşdeğerlik bunun yarısıdır.','V = 20 mL → yarı eşdeğerlik 10 mL'),A('Ka değeri','Yarı eşdeğerlikte pH = pKa; grafikten bu noktada pH = 5 okunur.','Ka = 10⁻⁵'),A('Eşlenik baz sabiti','A⁻ + H₂O ⇌ HA + OH⁻ için Kb = Kw/Ka.','Kb = 10⁻¹⁴/10⁻⁵ = 10⁻⁹'),A('OH⁻ derişimi','Zayıf bazın derişimi 0,1 M için [OH⁻] = √(Kb·C).','[OH⁻] = √(10⁻⁹·0,1) = 10⁻⁵ M'),A('pH','pOH = 5 olduğundan pH = 14 − 5.','pH = 9')],
 puf='Yarı eşdeğerlik noktasındaki pH, asidin kuvvetine dair bilgi verir.')
# ========================================================================
# 0009 · orta · büret okuması, H₂SO₄ derişimi
# ========================================================================
r0,r1=2.0,32.0; Vb=Fr(30); Cb=Fr(2,10); nOH=Cb*Vb/1000; nA=nOH/2; Va=Fr(20,1000); Mac=nA/Va
assert Mac==Fr(15,100)
w1=Cb*Fr(32)/1000/2/Va; w2=Cb*Fr(32)/1000/Va; w3=nOH/Va; w4=nOH*2/Va
assert (w1,w2,w3,w4)==(Fr(16,100),Fr(32,100),Fr(3,10),Fr(6,10)) and len({Mac,w1,w2,w3,w4})==5
def buret(cx,okuma,baslik):
    s=[f'\\draw[thick] ({cx-.3:.2f},0) -- ({cx-.3:.2f},-5.2) -- ({cx+.3:.2f},-5.2) -- ({cx+.3:.2f},0);']
    s.append(f'\\fill[vurgu!20] ({cx-.28:.2f},{-okuma*.1:.2f}) rectangle ({cx+.28:.2f},-5.18);')
    s.append(f'\\draw[vurgu,thick] ({cx-.3:.2f},{-okuma*.1:.2f}) -- ({cx+.3:.2f},{-okuma*.1:.2f});')
    s.append(f'\\draw[vurgu,dashed] ({cx-.9:.2f},{-okuma*.1:.2f}) -- ({cx-.3:.2f},{-okuma*.1:.2f});')
    for m in range(0,51):
        L_=.1 if m%5 else (.2 if m%10 else .32)
        s.append(f'\\draw ({cx-.3:.2f},{-m*.1:.2f}) -- ({cx-.3-L_:.2f},{-m*.1:.2f});')
        if m%10==0: s.append(f'\\node[left=2pt] at ({cx-.58:.2f},{-m*.1:.2f}) {{{m}}};')
    s.append(f'\\node[above=3pt,align=center] at ({cx:.2f},0) {{{baslik}}};')
    return s
sk=fig(*buret(0,r0,'Başlangıç'),*buret(3.6,r1,'Dönüm\\\\noktası'),'\\node[right] at (4.6,-2.6) {mL};')
q('0009',tipId='ab-notrles',tip='Nötrleşme hesabı ve indikatör seçimi',z='orta',alt=ALT,kaz='Büret okumalarından harcanan baz hacmini bulup çok değerlikli asidin derişimini hesaplar.',kalip='şekilli',
 kart='K-AKASB-06 (titrasyon hesabı) · 20 mL H₂SO₄, 0,2 M NaOH',
 metin='Erlene konulan 20 mL H₂SO₄ çözeltisi, birkaç damla indikatör eşliğinde büretteki 0,2 M NaOH çözeltisiyle titre ediliyor. Büretteki NaOH düzeyi titrasyonun başında ve indikatörün renk değiştirdiği dönüm noktasında şekildeki gibidir.\nBuna göre, H₂SO₄ çözeltisinin derişimi kaç M’dir?',
 dogru=Fr(15,100),yan=[(w1,'Büretteki son okumayı (32 mL) harcanan hacim saymış; başlangıç okumasını çıkarmamış.','dikkat'),(w3,'H₂SO₄’ün iki değerlikli olduğunu unutmuş, n(H₂SO₄) = n(NaOH) almış.','bilgi'),(w2,'Hem son okumayı hacim saymış hem de asidin değerliğini unutmuş.','dikkat'),(w4,'H₂SO₄ mol sayısını NaOH’ın iki katı almış; mol oranını ters kullanmış.','islem')],
 istenen='H₂SO₄ çözeltisinin derişimi (M).',ip=['Önce harcanan NaOH hacmini iki okumanın farkından bul; sonra H⁺ ve OH⁻ mol sayılarını eşitle.'],
 bilgi=[B_NOT],sekil=sk,
 ad=[A('Harcanan hacim','Son okumadan başlangıç okuması çıkarılır.','32 − 2 = 30 mL'),A('NaOH mol sayısı','n = M · V.','n = 0,2 · 0,030 = 6·10⁻³ mol'),A('H₂SO₄ mol sayısı','H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O; asit mol sayısı bazın yarısıdır.','n = 3·10⁻³ mol'),A('Derişim','M = n/V.','M = 3·10⁻³/0,020 = 0,15 M')],
 puf='Bürette hacim, iki okumanın farkıdır; iki değerlikli asitte mol oranı 1 : 2’dir.')
# ========================================================================
# 0010 · orta · öncüllü tuz hidrolizi (tablo)
# ========================================================================
sk=tablo_svg(['Asit','Ka (25 °C)'],[['HX',e(1,-4)],['HY',e(1,-6)],['HZ',e(1,-9)]])
sk=tablo_svg(['Çözünen madde','İyonlaşma sabiti (25 °C)'],[['NH₃ (Kb)',e(1,-5)],['HA (Ka)',e(1,-7)]])
assert math.isclose(math.sqrt(1e-9*0.1),1e-5) and math.isclose(math.sqrt(1e-7*0.1),1e-4)   # [H+] = 1e-5 (NH4Cl, pH 5); [OH-] = 1e-4 (NaA, pH 10)
d={'I':(False,'NaCl kuvvetli asit ve kuvvetli bazdan oluştuğu için iyonları hidroliz olmaz; çözelti nötrdür (pH = 7)'),
   'II':(True,'NH₄⁺ için Ka = 10⁻¹⁴/10⁻⁵ = 10⁻⁹ olduğundan [H⁺] = √(10⁻⁹·0,1) = 10⁻⁵ M ve pH = 5’tir'),
   'III':(True,'A⁻ için Kb = 10⁻¹⁴/10⁻⁷ = 10⁻⁷ olduğundan [OH⁻] = √(10⁻⁷·0,1) = 10⁻⁴ M, pOH = 4 ve pH = 10’dur')}
r=onc(d,[('I',),('II',),('I','II'),('I','III'),('II','III')])
q('0010',tipId='ab-hidroliz',tip='Tuz çözeltilerinin hidrolizi, pH ve Ka ilişkisi',z='orta',alt=ALT,kaz='Farklı tuz çözeltilerinin hidroliz özelliğini ve pH değerlerini sayısal olarak karşılaştırır.',kalip='öncüllü',
 kart='K-AKASB-05 (hidroliz) · NaCl, NH₄Cl ve NaA çözeltileri',
 metin='Tabloda NH₃ bazının Kb ve zayıf HA asidinin Ka değerleri 25 °C’de verilmiştir. Bu sıcaklıkta NaCl, NH₄Cl ve NaA tuzlarının her birinden 0,1 M’lik sulu çözeltiler hazırlanıyor. Hidroliz olan iyon miktarı başlangıç derişimine göre ihmal edilecek ve Kw = 1·10⁻¹⁴ alınacaktır.\nBuna göre,\nI. NaCl çözeltisinin pH değeri 7’den büyüktür.\nII. NH₄Cl çözeltisinin pH değeri 5’tir.\nIII. NaA çözeltisinin pH değeri 10’dur.\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her tuzu oluşturan iyonların hangi asit ve bazdan geldiğini belirleyip hidroliz eden iyon için uygun denge sabitini bul.'],
 bilgi=[B_HID,B_PH],sekil=sk,
 ad=[A('NaCl','Na⁺ ve Cl⁻ kuvvetli baz ve asit iyonlarıdır; hidroliz olmaz.','pH = 7 → I yanlış'),A('NH₄Cl','NH₄⁺ eşlenik asittir: Ka = Kw/Kb; [H⁺] = √(Ka·C).','Ka = 10⁻⁹ · [H⁺] = 10⁻⁵ M → pH = 5 → II doğru'),A('NaA','A⁻ eşlenik bazdır: Kb = Kw/Ka; [OH⁻] = √(Kb·C).','Kb = 10⁻⁷ · [OH⁻] = 10⁻⁴ M → pH = 10 → III doğru'),A('Sonuç','Doğru yargılar toplanır.',etk(d)+' · Sonuç: II ve III')],
 puf='Tuzun hangi iyonunun hidroliz olduğunu belirle; sonra o iyonun denge sabitini Kw ile bul.')
# 0011 · orta · tampon, pH
# ========================================================================
nHA=Fr(11,100)*Fr(1,10); nB=Fr(1,10)*Fr(10,1000); rest=nHA-nB; ratio=nB/rest
assert nHA==Fr(11,1000) and nB==Fr(1,1000) and rest==Fr(1,100) and ratio==Fr(1,10)  # pH = 5 + log(1/10) = 4
sk=fig(*kap(0,['100 mL','0,11 M HA'],'',h=1.5),'\\node at (1.95,1.0) {\\Large $+$};',*kap(3.9,['10 mL','0,1 M NaOH'],'',h=1.5),
 '\\draw[-{Stealth[length=2.2mm]},thick] (5.35,1.0) -- (6.35,1.0);',*kap(7.9,['Son','çözelti'],'',h=1.5))
q('0011',tipId='ab-tampon',tip='Tampon çözelti: oluşum, etki ve pH hesabı',z='orta',alt=ALT,kaz='Zayıf asit ile kuvvetli bazın kısmi nötrleşmesinden oluşan tamponun pH değerini hesaplar.',kalip='şekilli',
 kart='K-AKASB-04 (tampon pH) · HA + NaOH, oran 1/10',
 metin='25 °C’de Ka değeri 1·10⁻⁵ olan monoprotik zayıf HA asidinin çözeltisi ile NaOH çözeltisi şekildeki gibi karıştırılıyor ve tam olarak tepkime vermeleri bekleniyor. Karışım sonunda suyun iyonlaşması ve hacim değişimi dışındaki etkiler ihmal edilecektir.\nBuna göre, son çözeltinin pH değeri kaçtır?',
 dogru=4,yan=[(5,'Çözeltiyi yarı nötrleşmiş sanmış; pH = pKa = 5 almış.','dikkat'),(6,'[A⁻]/[HA] oranını ters yazmış (10 almış): pH = 5 + log10 = 6.','islem'),(7,'Karışımı tam nötrleşmiş ve nötr sanmış.','bilgi'),(9,'Tam nötrleşme sonucu oluşan bazik tuz çözeltisini düşünmüş.','bilgi')],
 istenen='Karışımın pH değeri.',ip=['Tepkimeden sonra hangi maddelerin kaldığını mol sayılarıyla belirle; sonuç bir tampon çiftidir.'],
 bilgi=[B_TAM],sekil=sk,
 ad=[A('Başlangıç mol sayıları','n = M · V.','n(HA) = 0,11 · 0,1 = 1,1·10⁻² mol · n(NaOH) = 0,1 · 0,01 = 1·10⁻³ mol'),A('Tepkime sonrası','HA + OH⁻ → A⁻ + H₂O; NaOH tükenir.','n(HA) = 1·10⁻² mol · n(A⁻) = 1·10⁻³ mol'),A('Oran','Hacim aynı olduğundan oran mol sayılarından alınır.','[A⁻]/[HA] = 1/10'),A('pH','pH = pKa + log([A⁻]/[HA]) ve pKa = 5.','pH = 5 + log(1/10) = 4')],
 puf='Önce tepkimeyi bitir, kalanları belirle; sonra tampon bağıntısını uygula.')
# ========================================================================
# 0012 · zor · Ba(OH)₂ + HCl karışımı
# ========================================================================
nOH12=2*Fr(5,100)*Fr(200,1000); nH12=Fr(5,100)*Fr(300,1000); Vtop=Fr(500,1000)
assert nOH12==Fr(1,50) and nH12==Fr(3,200) and (nOH12-nH12)==Fr(1,200) and (nOH12-nH12)/Vtop==Fr(1,100)
w_a=(nH12-nOH12/2)/Vtop; assert w_a==Fr(1,100)   # katsayı unutulursa asit artar, pH 2
assert (nOH12-nH12)/Fr(50,1000)==Fr(1,10) and (nOH12-nH12)/Fr(5)==Fr(1,1000)
sk=fig(*kap(0,['200 mL','0,05 M','\\ce{Ba(OH)2}'],'',h=1.5),'\\node at (1.95,1.0) {\\Large $+$};',*kap(3.9,['300 mL','0,05 M','\\ce{HCl}'],'',h=1.5),
 '\\draw[-{Stealth[length=2.2mm]},thick] (5.35,1.0) -- (6.35,1.0);',*kap(7.9,['Karışım','pH $=\\,?$'],'',h=1.5))
q('0012',tipId='ab-ph',tip='pH, pOH ve seyrelme/karıştırma hesapları',z='orta',alt=ALT,kaz='Kuvvetli baz ve kuvvetli asit çözeltilerinin karışımından artan iyonun derişimiyle pH hesaplar.',kalip='şekilli',
 kart='K-AKASB-01 (karışım) + K-AKASB-06 (nötrleşme) · Ba(OH)₂ + HCl',
 metin='Kuvvetli elektrolitler olan Ba(OH)₂ ve HCl’nin 25 °C’deki sulu çözeltileri şekildeki gibi karıştırılıyor. Karıştırmada hacimler toplanıyor ve oluşan tuz suda çözünmüş kalıyor.\nBuna göre, karışımın pH değeri kaçtır?',
 dogru=12,yan=[(2,'Ba(OH)₂’nin iki OH⁻ verdiğini unutmuş; bu durumda asit artar ve pH 2 bulunur.','bilgi'),(7,'Asit ve bazın aynı derişimde olmasından tam nötrleşme beklemiş.','dikkat'),(11,'Artan OH⁻ mol sayısını 500 mL yerine 5 L’ye bölmüş (mL–L dönüşüm hatası).','dikkat'),(13,'Artan OH⁻ mol sayısını 500 mL yerine 50 mL’ye bölmüş (mL–L dönüşüm hatası).','dikkat')],
 istenen='Karışımın pH değeri.',ip=['Bazdan gelen OH⁻ ile asitten gelen H⁺ mol sayılarını ayrı ayrı bulup karşılaştır.'],
 bilgi=[B_NOT,B_SEY],sekil=sk,
 ad=[A('OH⁻ mol sayısı','Ba(OH)₂ başına 2 OH⁻ vardır.','n(OH⁻) = 2 · 0,05 · 0,2 = 2·10⁻² mol'),A('H⁺ mol sayısı','HCl başına 1 H⁺.','n(H⁺) = 0,05 · 0,3 = 1,5·10⁻² mol'),A('Artan iyon','OH⁻ fazladır; fark alınır.','5·10⁻³ mol OH⁻'),A('Derişim','Toplam hacim 0,5 L.','[OH⁻] = 5·10⁻³/0,5 = 10⁻² M'),A('pH','pOH = 2 olduğundan pH = 14 − 2.','pH = 12')],
 puf='Bazın katsayısını (OH⁻ sayısını) mol hesabına kat; sonra artanı toplam hacme böl.')
# ========================================================================
# 0013 · orta · öncüllü tampon, çubuk grafik
# ========================================================================
def cubuk():
    s=[];
    for y in range(0,11,2): s.append(f'\\draw[gray!35,very thin] (0,{y*.35:.2f}) -- (4.6,{y*.35:.2f}); \\node[left=1pt] at (0,{y*.35:.2f}) {{{y}}};')
    s.append('\\draw[thick] (0,3.9) -- (0,0) -- (4.8,0); \\node[above] at (0,3.95) {mol sayısı (mmol)};')
    bars=[('HA',1.0,6,4),('\\ce{A-}',3.0,6,8)]
    for ad,x,b,a in bars:
        s.append(f'\\draw[fill=white,thick] ({x-.7:.2f},0) rectangle ({x-.05:.2f},{b*.35:.2f});')
        s.append(f'\\draw[fill=gray!35,thick,pattern=north east lines] ({x+.05:.2f},0) rectangle ({x+.7:.2f},{a*.35:.2f});')
        s.append(f'\\node[below=1pt] at ({x:.2f},0) {{{ad}}};')
    s.append('\\draw[fill=white,thick] (5.2,3.3) rectangle (5.5,3.5); \\node[right] at (5.55,3.4) {İşlemden önce};')
    s.append('\\draw[pattern=north east lines,thick] (5.2,2.8) rectangle (5.5,3.0); \\node[right] at (5.55,2.9) {İşlemden sonra};')
    return s
sk=fig(*cubuk())
d={'I':(False,'HNO₃ ortama H⁺ verir; H⁺ A⁻ ile tepkimeye girip HA’yı artırır ve A⁻’yi azaltır, grafikteki değişimin tersi olur'),
   'II':(False,'NaA katısı yalnızca A⁻ ekler; HA’nın mol sayısı grafikteki gibi azalmaz'),
   'III':(True,'NaOH’tan gelen OH⁻ HA ile tepkimeye girer; HA azalır, A⁻ aynı miktarda artar')}
r=onc(d,[('I',),('III',),('I','II'),('II','III'),('I','II','III')])
q('0013',tipId='ab-tampon',tip='Tampon çözelti: oluşum, etki ve pH hesabı',z='orta',alt=ALT,kaz='Tampon çözeltideki HA ve A⁻ mol sayılarının değişiminden eklenen maddeyi belirler.',kalip='öncüllü',
 kart='K-AKASB-04 (tampon etkisi) · HA/A⁻ çubuk grafiği',
 metin='Zayıf HA asidi ile NaA tuzundan hazırlanan bir tampon çözeltide, bir madde eklenmeden önce ve eklendikten sonra çözeltideki HA ve A⁻ mol sayıları grafikte verilmiştir. Eklenen madde, çözeltide başka bir tepkimeyle HA ve A⁻ dışındaki türleri değiştirmemektedir.\nBuna göre bu çözeltiye,\nI. HNO₃ çözeltisi,\nII. NaA katısı,\nIII. NaOH katısı\nmaddelerinden hangileri eklenmiş olabilir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Eklenmiş olabilecek maddeler.',ip=['Grafikte hangi bileşenin azalıp hangisinin arttığını ve azalan miktarın artana eşit olup olmadığını incele.'],
 bilgi=[B_TAM],sekil=sk,
 ad=[A('Grafikten değişim','HA 6 mmol’den 4 mmol’e iner, A⁻ 6 mmol’den 8 mmol’e çıkar.','ΔHA = −2 mmol, ΔA⁻ = +2 mmol (eşit büyüklükte, zıt yönlü)'),A('I. madde','H⁺, A⁻ ile tepkimeye girip HA’yı artırır.','HA artar, A⁻ azalır → I yanlış'),A('II. madde','Tuz yalnız A⁻ ekler.','HA değişmez → II yanlış'),A('III. madde','OH⁻ + HA → A⁻ + H₂O.','HA azalır, A⁻ artar → III doğru · Sonuç: Yalnız III')],
 puf='Tampon çiftinde bir bileşenin azalması kadar diğerinin artması, kuvvetli asit ya da bazla etkileşime işaret eder.')
# ========================================================================
# 0014 · orta · iki titrasyon eğrisi, olumsuz kök
# ========================================================================
ptsX=[(i*.25,ph_strong(2.5,0.1*i*.25,25+i*.25)) for i in range(0,201)]
ptsY=[(i*.25,ph_weak(1e-5,2.5,0.1*i*.25,25+i*.25)) for i in range(0,201)]
assert ptsX[0][1]<ptsY[0][1] and abs(ph_strong(2.5,2.5,50)-7)<1e-6 and ph_weak(1e-5,2.5,2.5,50)>8
sk=fig(*egri([(ptsX,'very thick','',(0,0)),(ptsY,'very thick,dashed','',(0,0))],50,[0,10,20,30,40,50],'Eklenen 0,1 M NaOH hacmi (mL)',sx=.16,sy=.3),
 '\\draw[very thick] (5.2,1.0) -- (5.9,1.0); \\node[right] at (5.95,1.0) {X çözeltisi};',
 '\\draw[very thick,dashed] (5.2,.5) -- (5.9,.5); \\node[right] at (5.95,.5) {Y çözeltisi};')
S=[('Başlangıç pH değeri X çözeltisinde Y çözeltisinden küçüktür.',True,'X kuvvetli asit olduğundan aynı derişimde [H⁺] daha büyüktür'),
   ('Y çözeltisine 12,5 mL NaOH eklendiğinde ortamda tampon çözelti oluşur.',True,'bu noktada HA ve A⁻ birlikte bulunur'),
   ('Her iki çözeltide de eşdeğerlik noktasında pH değeri 7’dir.',False,'Zayıf asit titrasyonunda eşdeğerlik noktasında tuzun hidrolizi nedeniyle pH 7’den büyüktür'),
   ('İki çözelti de eşdeğerlik noktasına aynı hacimde NaOH eklenince ulaşır.',True,'asit mol sayıları eşittir'),
   ('Y çözeltisinin eşdeğerlik noktasındaki pH değeri, X çözeltisinin eşdeğerlik noktasındaki pH değerinden büyüktür.',True,'Y’nin tuzu bazik, X’in tuzu nötrdür')]
r=tek(S,False)
q('0014',tipId='ab-titra',tip='Titrasyon eğrisinden asit türü, derişim ve Ka çıkarma',z='orta',alt=ALT,kaz='Kuvvetli ve zayıf asit titrasyon eğrilerini karşılaştırarak yanlış yargıyı bulur.',kalip='grafik',
 kart='K-AKASB-03 (iki eğri) · kuvvetli ve zayıf asit',
 metin='25 °C’de X ve Y monoprotik asitlerinin eşit hacimli ve eşit derişimli sulu çözeltileri, 0,1 M NaOH çözeltisi ile ayrı ayrı titre ediliyor. Her iki titrasyonda elde edilen pH–NaOH hacmi grafikleri aynı eksen takımında verilmiştir. X asitlerden biri kuvvetli, diğeri zayıftır.\nBuna göre, aşağıdaki yargılardan hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yargı.',ip=['İki eğrinin başlangıç noktasını, sıçrama noktasını ve eşdeğerlik noktasındaki pH değerlerini ayrı ayrı karşılaştır.'],
 bilgi=[B_TIT],sekil=sk,
 ad=[A('Eğrilerin başlangıcı','X eğrisi daha düşük pH’tan başlıyor; bu kuvvetli asittir.','X: kuvvetli · Y: zayıf'),A('Sıçrama noktası','İki eğri de 25 mL’de sıçrıyor.','V(eşdeğerlik) = 25 mL'),A('Eşdeğerlik pH’ı','X’te tuz nötr, Y’de tuzun anyonu hidroliz olup bazik.','X: pH = 7 · Y: pH > 7'),A('Yanlış yargıyı bul','“İkisinde de pH = 7” yargısı Y için geçerli değildir.','Yanlış: iki çözeltide de eşdeğerlikte pH = 7')],
 puf='Zayıf asit titrasyonunda eşdeğerlik noktası 7’nin üzerindedir; yalnız kuvvetli–kuvvetli çiftte pH = 7’dir.')
# ========================================================================
# 0015 · orta · öncüllü iyonlaşma yüzdesi grafiği
# ========================================================================
Ka15=Fr(4,10**6)
def al15(C): return 100*math.sqrt(float(Ka15)/C)
assert abs(al15(0.04)-1)<1e-9 and abs(al15(0.01)-2)<1e-9 and abs(al15(0.0025)-4)<1e-9
assert Fr(1,100)*Fr(4,100)==Fr(4,10**4) and Fr(4,100)*Fr(25,10000)==Fr(1,10**4) and Fr(1,10**4)<Fr(4,10**4)
assert (Fr(4,10**4))**2/Fr(4,100)==Ka15 and (Fr(1,10**4))**2/Fr(25,10000)==Ka15
def gra15():
    sx=170.; sy=.62; s=[]   # 1 M -> 170 cm gibi değil; x: 0.05 M = 8.5 cm
    sx=8.5/0.05
    for y in range(0,6): s.append(f'\\draw[gray!35,very thin] (0,{y*sy:.2f}) -- (8.7,{y*sy:.2f}); \\node[left=1pt] at (0,{y*sy:.2f}) {{{y}}};')
    for x in (0.0025,0.01,0.02,0.03,0.04,0.05):
        lab=str(x).replace('.','{,}'); s.append(f'\\draw[gray!35,very thin] ({x*sx:.2f},0) -- ({x*sx:.2f},{5*sy:.2f}); \\node[below=1pt] at ({x*sx:.2f},0) {{{lab}}};')
    s.append(f'\\draw[thick] (0,{5*sy+.15:.2f}) -- (0,0) -- (8.85,0); \\node[above] at (0,{5*sy+.1:.2f}) {{İyonlaşma yüzdesi (\\%)}};')
    s.append(f'\\node[below=11pt] at (4.3,0) {{HA derişimi (mol/L)}};')
    co=' '.join(f'({c*sx:.3f},{al15(c)*sy:.3f})' for c in [0.0025+i*0.0005 for i in range(0,96)])
    s.append(f'\\draw[very thick] plot coordinates {{{co}}};')
    for c in (0.0025,0.01,0.04): s.append(f'\\draw[fill=white,thick] ({c*sx:.3f},{al15(c)*sy:.3f}) circle (.09);')
    return s
sk=fig(*gra15())
d={'I':(True,'grafikte derişim azaldıkça iyonlaşma yüzdesi yükselmektedir (0,04 M’de %1, 0,0025 M’de %4)'),
   'II':(False,'[H⁺] = iyonlaşma yüzdesi · derişim olduğundan 0,0025 M çözeltide 1·10⁻⁴ M, 0,04 M çözeltide 4·10⁻⁴ M’dir; yani küçüktür'),
   'III':(False,'Ka yalnızca sıcaklığa bağlıdır; iki çözeltide de Ka = 4·10⁻⁶’dır')}
r=onc(d,[('I',),('II',),('I','II'),('I','III'),('I','II','III')])
q('0015',tipId='ab-ka',tip='Ka, Kb, asit kuvveti ve iyonlaşma yüzdesi',z='orta',alt=ALT,kaz='İyonlaşma yüzdesi–derişim grafiğinden H⁺ derişimini ve Ka değerini yorumlar.',kalip='grafik',
 kart='K-AKASB-02 (seyrelme, iyonlaşma yüzdesi) · HA grafiği',
 metin='Monoprotik zayıf HA asidinin 25 °C’de farklı derişimlerdeki sulu çözeltilerinde iyonlaşma yüzdesinin derişimle değişimi grafikte verilmiştir. Grafikteki işaretli noktalar 0,0025 M, 0,01 M ve 0,04 M derişimlerine karşılık gelmektedir.\nBuna göre,\nI. Çözelti seyreltildikçe HA’nın iyonlaşma yüzdesi artar.\nII. 0,0025 M çözeltideki H⁺ derişimi, 0,04 M çözeltidekinden büyüktür.\nIII. 0,0025 M çözeltideki Ka değeri, 0,04 M çözeltidekinin 16 katıdır.\nyargılarından hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['İyonlaşma yüzdesini derişimle çarparak iyonlaşan HA derişimini, yani H⁺ derişimini bul; Ka’nın neye bağlı olduğunu da hatırla.'],
 bilgi=[B_KA],sekil=sk,
 ad=[A('I. yargı','Derişim azaldıkça eğri yukarı çıkar.','%1 → %2 → %4 · I doğru'),A('II. yargı','[H⁺] = (α/100) · C.','0,04 M: 4·10⁻⁴ M · 0,0025 M: 1·10⁻⁴ M → II yanlış'),A('III. yargı','Ka sıcaklığa bağlıdır; iki derişim için de Ka = [H⁺]²/C.','Ka = 4·10⁻⁶ (her ikisi) → III yanlış'),A('Sonuç','Doğru yargı yalnızca I’dir.',etk(d)+' · Sonuç: Yalnız I')],
 puf='İyonlaşma yüzdesi artsa bile [H⁺]’ın arttığı anlamına gelmez; derişimle çarpmayı unutma.')
# ========================================================================
# 0016 · orta · Kb, iyonlaşma yüzdesi
# ========================================================================
Kb16=Fr(1,10**5); C16=Fr(1,10); OH16=Fr(1,1000); assert OH16**2/C16==Kb16 and OH16/C16*100==1
assert OH16/(C16*10)*100==Fr(1,10)==Fr(1,10) and OH16*Fr(100)==Fr(1,10)
w16=[Fr(1,100),Fr(1,10),Fr(10),Fr(100)]; assert OH16/C16==Fr(1,100) and OH16/1*100==Fr(1,10) and OH16/Fr(1,100)*100==10
q('0016',tipId='ab-ka',tip='Ka, Kb, asit kuvveti ve iyonlaşma yüzdesi',z='orta',alt=ALT,kaz='Kb değerinden zayıf bazın iyonlaşma yüzdesini hesaplar.',kalip='hikâyeli',
 kart='K-AKASB-02 (Kb, iyonlaşma yüzdesi) · Kb = 1·10⁻⁵, 0,1 M',
 metin='Kb değeri 1·10⁻⁵ olan monoprotik zayıf bir bazın 25 °C’deki 0,1 M’lik sulu çözeltisi hazırlanıyor. Bir öğrenci bu çözeltide baz moleküllerinin ne kadarının suyla tepkimeye girip iyonlaştığını merak ediyor. Denge anında bazın derişiminin başlangıç derişimine eşit olduğu varsayılacaktır.\nBuna göre, bazın iyonlaşma yüzdesi kaçtır?',
 dogru=1,yan=[(Fr(1,100),'Oranı yüzdeye çevirmemiş: 10⁻³/0,1 = 0,01 değerini yazmış.','dikkat'),(Fr(1,10),'Başlangıç derişimini 1 M alıp [OH⁻]/C · 100 = 0,1 bulmuş.','dikkat'),(10,'[OH⁻] derişimini başlangıç derişimine bölerken 0,01 M kullanmış.','islem'),(100,'Zayıf bazın tamamen iyonlaştığını sanmış.','bilgi')],
 istenen='Bazın iyonlaşma yüzdesi (%).',ip=['Önce iyonlaşan baz derişimini Kb bağıntısından bul, sonra başlangıç derişimine oranla.'],
 bilgi=[B_KA],
 ad=[A('Kb ifadesi','Denge anında [BH⁺] = [OH⁻] = x ve [B] ≈ 0,1.','Kb = x²/0,1 = 10⁻⁵'),A('x değeri','x² = 10⁻⁶.','x = 10⁻³ M'),A('İyonlaşma yüzdesi','İyonlaşan/başlangıç · 100.','10⁻³/0,1 · 100 = %1')],
 puf='İyonlaşma yüzdesi için son adımda 100 ile çarpmayı unutma.')
# ========================================================================
# 0017 · zor · NaA pH → Ka → HA çözeltisi pH
# ========================================================================
Kw=Fr(1,10**14); C17=Fr(2,10); OH17=Fr(1,10**5); Kb17=OH17**2/C17; Ka17=Kw/Kb17
assert Kb17==Fr(5,10**10) and Ka17==Fr(2,10**5)
C17b=Fr(5,100); H17=Fr(1,10**3); assert H17**2==Ka17*C17b and pHof(H17)==3
assert H17**2==Ka17*C17b and OH17**2==Kb17*C17      # [OH-] = 1e-5 ; [H+] = 1e-3
assert math.isclose(math.sqrt(float(Ka17*C17b)),1e-3)
q('0017',tipId='ab-hidroliz',tip='Tuz çözeltilerinin hidrolizi, pH ve Ka ilişkisi',z='zor',alt=ALT,kaz='Tuz çözeltisinin pH değerinden Ka değerini bulup aynı asidin çözeltisinin pH değerini hesaplar.',kalip='hikâyeli',
 kart='K-AKASB-05 (hidroliz) + K-AKASB-02 (Ka) · 0,2 M NaA pH = 9, 0,05 M HA',
 metin='Bir öğrenci, monoprotik zayıf HA asidinin sodyum tuzu olan NaA’yı suda çözerek 25 °C’de 0,2 M’lik sulu çözelti hazırlıyor ve pH değerini 9 olarak ölçüyor. Aynı sıcaklıkta aynı asidin 0,05 M’lik sulu çözeltisi de hazırlanıyor. Her iki çözeltide yalnızca tuzun ya da asidin tek denge tepkimesi dikkate alınacak, iyonlaşan ya da hidroliz olan miktar başlangıç derişimine göre ihmal edilecek ve Kw = 1·10⁻¹⁴ alınacaktır.\nBuna göre, 0,05 M HA çözeltisinin pH değeri kaçtır?',
 dogru=3,yan=[(5,'Tuz çözeltisinin pOH değerini (5) asit çözeltisinin pH’ı olarak yazmış.','dikkat'),(7,'Zayıf asit çözeltisini nötr sanmış.','bilgi'),(9,'Tuz çözeltisinin pH değerini asit çözeltisinin pH’ı olarak almış.','dikkat'),(11,'Ka yerine Kb kullanıp [OH⁻] = √(Kb·0,05) yerine √(Ka·0,05) = 10⁻³ M bulmuş ve pH = 11 yazmış.','islem')],
 istenen='0,05 M HA çözeltisinin pH değeri.',ip=['Tuz çözeltisindeki pH değerinden asidin Ka değerine ulaşmak için hidrolizin denge ifadesini kullan.'],
 bilgi=[B_HID,B_KA],
 ad=[A('OH⁻ derişimi','pH = 9 ise pOH = 5.','[OH⁻] = 10⁻⁵ M'),A('Hidroliz sabiti','A⁻ + H₂O ⇌ HA + OH⁻ için [HA] = [OH⁻].','Kb = (10⁻⁵)²/0,2 = 5·10⁻¹⁰'),A('Ka değeri','Ka · Kb = Kw.','Ka = 10⁻¹⁴/(5·10⁻¹⁰) = 2·10⁻⁵'),A('Asit çözeltisinin pH’ı','[H⁺] = √(Ka · C).','[H⁺] = √(2·10⁻⁵ · 0,05) = 10⁻³ M → pH = 3')],
 puf='Önce tuz çözeltisinden asidin Ka değerine ulaş, sonra o değeri asit çözeltisinde kullan.')
# ========================================================================
# 0018 · zor · tampon + HCl
# ========================================================================
nB18=Fr(10,100); nHCl=Fr(6,100); nNH3=nB18-nHCl; nNH4=nB18+nHCl
assert (nNH3,nNH4)==(Fr(4,100),Fr(16,100)) and nNH4/nNH3==4
pOH18=5+2*Fr(3,10); assert pOH18==Fr(56,10) and 14-pOH18==Fr(84,10) and 14-(5-2*Fr(3,10))==Fr(96,10)
q('0018',tipId='ab-tampon',tip='Tampon çözelti: oluşum, etki ve pH hesabı',z='zor',alt=ALT,kaz='Bazik tampon çözeltiye kuvvetli asit eklenince oluşan yeni pH değerini hesaplar.',kalip='hikâyeli',
 kart='K-AKASB-04 (tampon, HCl ekleme) · NH₃/NH₄Cl',
 metin='25 °C’de 1 L’lik bir çözeltide 0,10 mol NH₃ ve 0,10 mol NH₄Cl çözünmüştür. Bu çözeltiye 0,06 mol HCl gazı çözülüyor. Çözeltinin hacminin değişmediği, HCl’nin tamamen çözündüğü, NH₃’ün Kb değerinin 1·10⁻⁵ ve Kw değerinin 1·10⁻¹⁴ olduğu biliniyor (log 2 = 0,3).\nBuna göre, son çözeltinin pH değeri kaçtır?',
 dogru=Fr(84,10),yan=[(5,'Kb ifadesini pH’a yazıp pH = pKb = 5 almış.','dikkat'),(7,'HCl ekleyince çözeltinin nötr olacağını sanmış.','bilgi'),(9,'Tamponun pH’ının değişmediğini sanmış; eklenen HCl’yi hesaba katmamış.','bilgi'),(Fr(96,10),'[NH₄⁺]/[NH₃] oranını ters yazmış: pOH = 5 − 0,6 = 4,4 ve pH = 9,6.','islem')],
 istenen='Son çözeltinin pH değeri.',ip=['HCl’nin hangi bileşenle tepkimeye girdiğini belirleyip mol sayılarını güncelle; tampon bağıntısını güncel mollerle kur.'],
 bilgi=[B_TAM,B_PH],
 ad=[A('Tepkime','NH₃ + H⁺ → NH₄⁺; HCl NH₃’ü harcar.','NH₃: 0,10 − 0,06 · NH₄⁺: 0,10 + 0,06'),A('Yeni mol sayıları','Çıkarma ve toplama yapılır.','n(NH₃) = 0,04 mol · n(NH₄⁺) = 0,16 mol'),A('pOH','pOH = pKb + log([NH₄⁺]/[NH₃]); pKb = 5.','pOH = 5 + log 4 = 5 + 0,6 = 5,6'),A('pH','pH = 14 − pOH.','pH = 8,4')],
 puf='Tampon bağıntısına eklemeden sonraki mol sayılarını koy; asit baz bileşenini harcar.')
# ========================================================================
# 0019 · zor · indikatör seçimi (pH aralıkları)
# ========================================================================
C19=Fr(1,10); Kb19=Fr(1,10**5); Ka19=Kw/Kb19; H19=Fr(1,10**5); assert Ka19==Fr(1,10**9) and H19**2==Ka19*C19 and pHof(H19)==5
bandlar=[('X',1,3),('Y',6.5,8),('Z',11,13),('T',4,6),('U',8,10)]
assert [b[0] for b in bandlar if b[1]<=5<=b[2]]==['T']
def band():
    sx=.5; s=[]
    for p in range(0,15): s.append(f'\\draw[gray!35,very thin] ({p*sx:.2f},-.2) -- ({p*sx:.2f},{5*.55+.1:.2f}); \\node[below=2pt] at ({p*sx:.2f},-.2) {{{p}}};')
    s.append(f'\\draw[thick] (0,-.2) -- ({14*sx+.1:.2f},-.2); \\node[below=14pt] at ({7*sx:.2f},-.2) {{pH}};')
    for i,(ad,a,b) in enumerate(bandlar):
        y=(4-i)*.55+.15
        s.append(f'\\draw[thick,fill=gray!25] ({a*sx:.2f},{y-.17:.2f}) rectangle ({b*sx:.2f},{y+.17:.2f}); \\node[left=2pt] at (-.05,{y:.2f}) {{{ad}}};')
    s.append('\\node[above] at (3.5,3.0) {İndikatörün renk değiştirdiği pH aralığı};')
    return s
sk=fig(*band())
q('0019',tipId='ab-notrles',tip='Nötrleşme hesabı ve indikatör seçimi',z='zor',alt=ALT,kaz='Zayıf baz–kuvvetli asit titrasyonunda eşdeğerlik pH’ını hesaplayıp uygun indikatörü seçer.',kalip='şekilli',
 kart='K-AKASB-06 (indikatör) + K-AKASB-05 (hidroliz) · NH₃ + HCl',
 metin='25 °C’de 50 mL 0,2 M NH₃ çözeltisi, 0,2 M HCl çözeltisiyle titre edilecektir. NH₃’ün Kb değeri 1·10⁻⁵’tir. Beş farklı indikatörün renk değiştirdiği pH aralıkları şekilde verilmiştir. Kw = 1·10⁻¹⁴ alınacak ve hidroliz eden katyon miktarı başlangıç derişimine göre ihmal edilecektir.\nBuna göre eşdeğerlik noktasını belirlemek için hangi indikatör kullanılmalıdır?',
 dogru='T',yan=[('X','pH 1–3 aralığında renk değiştiren X’i seçmiş; eşdeğerlikte kuvvetli asit varmış gibi düşünmüş.','bilgi'),('Y','Eşdeğerlikte pH = 7 olduğunu varsaymış ve 6,5–8 aralığındaki Y’yi seçmiş.','dikkat'),('U','Zayıf baz titrasyonunda eşdeğerlik pH’ını bazik sanıp 8–10 aralığındaki U’yu seçmiş.','bilgi'),('Z','pH’ı baz fazlasının olduğu bölgeye taşımış ve Z’yi seçmiş.','dikkat')],
 sira=['X','Y','Z','T','U'],istenen='Uygun indikatör.',ip=['Eşdeğerlik noktasında çözeltide hangi tuzun ve hangi derişimde bulunduğunu belirle.'],
 bilgi=[B_NOT,B_HID],sekil=sk,
 ad=[A('Tuzun derişimi','50 mL NH₃ ile 50 mL HCl tam tepkimeye girer; toplam hacim 100 mL.','n(NH₄Cl) = 0,2 · 0,05 = 0,01 mol → [NH₄⁺] = 0,1 M'),A('Ka değeri','NH₄⁺ eşlenik asittir: Ka = Kw/Kb.','Ka = 10⁻⁹'),A('H⁺ derişimi','[H⁺] = √(Ka · C).','[H⁺] = √(10⁻⁹ · 0,1) = 10⁻⁵ M → pH = 5'),A('İndikatör','pH = 5’i kapsayan aralık aranır.','T (4–6)')],
 puf='Zayıf baz–kuvvetli asit titrasyonunda eşdeğerlik pH’ı asidik bölgededir; aralığı pH’ı içeren indikatörü seç.')
# ========================================================================
# 0020 · zor · tampon hazırlama (hacim)
# ========================================================================
nHA20=Fr(15,100)*Fr(1,10); x20=Fr(125,10000); assert nHA20==Fr(15,1000) and (nHA20-x20)==Fr(25,10000) and x20/(nHA20-x20)==5
V20=x20/Fr(1,10)*1000; assert V20==125 and math.isclose(5+math.log10(5),5.7,abs_tol=0.01) and 5+(1-0.3)==5.7
w20=[Fr(25,10000)/Fr(1,10)*1000, nHA20/2/Fr(1,10)*1000, nHA20*Fr(8,10)/Fr(1,10)*1000, nHA20/Fr(1,10)*1000]
assert w20==[25,Fr(75),Fr(120),Fr(150)] and len({V20,*w20})==5
q('0020',tipId='ab-tampon',tip='Tampon çözelti: oluşum, etki ve pH hesabı',z='zor',alt=ALT,kaz='İstenen pH değerinde tampon hazırlamak için gereken kuvvetli baz hacmini hesaplar.',kalip='hikâyeli',
 kart='K-AKASB-04 (tampon hazırlama) + K-AKASB-06 (nötrleşme) · HA + NaOH, pH = 5,7',
 metin='25 °C’de Ka değeri 1·10⁻⁵ olan monoprotik zayıf HA asidinin 100 mL’lik 0,15 M çözeltisine 0,1 M NaOH çözeltisinden belirli bir hacim ekleniyor ve pH değeri 5,7 olan bir tampon çözelti hazırlanıyor. Tamponda [A⁻]/[HA] oranı mol sayılarından bulunabilir; hacim değişimi bu oranı etkilemez (log 2 = 0,3).\nBuna göre, eklenen NaOH çözeltisinin hacmi kaç mL’dir?',
 dogru=125,yan=[(25,'[A⁻]/[HA] oranını ters yazmış (1/5) ve 25 mL bulmuş.','islem'),(75,'pH = pKa varsayıp yarı nötrleşme için gereken hacmi bulmuş.','dikkat'),(120,'Oranı “asidin %80’i nötrleşir” biçiminde yorumlamış.','dikkat'),(150,'Asidin tamamını nötrleştirmek için gereken hacmi bulmuş.','bilgi')],
 istenen='Eklenen NaOH çözeltisinin hacmi (mL).',ip=['pH değerinden [A⁻]/[HA] oranını bul, sonra NaOH’ın harcayacağı HA mol sayısını bu orana göre kur.'],
 bilgi=[B_TAM,B_NOT],
 ad=[A('Oran','pH = pKa + log([A⁻]/[HA]), pKa = 5 ve log 5 = 1 − log 2 = 0,7.','5,7 = 5 + log([A⁻]/[HA]) → oran = 5'),A('Toplam mol','Başlangıçta HA mol sayısı.','n(HA)₀ = 0,15 · 0,1 = 1,5·10⁻² mol'),A('NaOH mol sayısı','n(A⁻) = x, n(HA) = 1,5·10⁻² − x, x/(1,5·10⁻² − x) = 5.','x = 1,25·10⁻² mol'),A('Hacim','V = n/M.','V = 1,25·10⁻²/0,1 = 0,125 L = 125 mL')],
 puf='Verilen pH’tan oranı bulup toplam mol ile oranı birlikte çöz.')
# ====================== BİTİŞ ======================
for x in P.ANA: x['kardes']=None
P.yaz(os.path.join(GD,'asitbaz-1.json'),'/tmp/bos-aytasitbaz.json')
tipler={}
for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='akim|'+KONUAD))['kartlar'].append(c['id'])
json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 12. sınıf kimya müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akasitbaz.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'kart',len(KARTLAR))
