"""AYT Kimya · Sıvı Çözeltiler · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ; her sayı Python'da Fraction ile hesaplanıp assert edilir."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
KONUAD='Sıvı Çözeltiler'
UK='akim|'+KONUAD
P=Parti('cozelti',KONUAD,UK,ders='AYT Kimya',idon='aytkim')
H.KONU=KONUAD
F=Fr
KY='ÖSYM AYT 2018–2026 Kimya (yalnız mantık) · MEB 12. sınıf kimya'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
import re
def q(no,ad,**k):
    assert len(k['ip'])==1
    mm=re.match(r'^(.*)\n([^\n]*\?) (\(.*\))$',k['metin'],re.S)
    if mm: k['metin']=mm.group(1)+'\n'+mm.group(3)+'\n'+mm.group(2)
    assert k['metin'].rstrip().endswith('?'),no
    mk(P,no,adim=len(ad),ad=ad,**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
def fmx(x): return fm(F(x))
def onc(truth,reasons,sira,neg=False):
    cap=lambda t:(t[0].upper()+t[1:]).rstrip('.')+'.'
    def kume(l):
        if l=='I, II ve III': return {'I','II','III'}
        return set(l.replace('Yalnız ','').replace(' ve ',' ').split())
    hedef={k for k,v in truth.items() if v!=neg}
    dog=[l for l in sira if kume(l)==hedef]; assert len(dog)==1,(sira,hedef)
    yan=[]
    for l in sira:
        if l==dog[0]: continue
        k=kume(l); c=[]
        for x in ('I','II','III'):
            if x in k and x not in hedef:
                c.append(f'{x}. öncülü '+('yanlış' if neg else 'doğru')+f' saymış, oysa '+('doğrudur' if neg else 'yanlıştır')+f': {reasons[x]}.')
            if x in hedef and x not in k:
                c.append(f'{x}. öncülünü '+('doğru' if neg else 'yanlış')+f' saymış, oysa '+('yanlıştır' if neg else 'doğrudur')+f': {reasons[x]}.')
        yan.append((l,' '.join(c),'bilgi'))
    ad=[A(f'{x}. öncülü incele',cap(reasons[x]),f'{x}: '+('doğru' if truth[x] else 'yanlış')) for x in ('I','II','III')]
    ad.append(A('Sonuca var',('Yanlış olan öncüller seçilir.' if neg else 'Doğru öncüller birleştirilir.'),('Yanlış: ' if neg else 'Doğru: ')+', '.join(sorted(hedef))))
    return dog[0],yan,ad
S5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
S5b=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']
S5c=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
# ---- bilgi kutuları
B_M=B('Molarite ve molalite','Molarite (M) = çözünenin mol sayısı ÷ çözeltinin hacmi (L); molalite (m) = çözünenin mol sayısı ÷ çözücünün kütlesi (kg). Molarite sıcaklıkla (hacim) değişir, molalite değişmez. Örnek: 4 mol çözünen 2 kg çözücüde ise molalite 2 m olur')
B_Y=B('Yüzde, yoğunluk ve molarite','1 L çözeltinin kütlesi = d × 1000 g olur; bunun kütlece yüzdesi kadarı çözünendir. Molarite = (10 × yüzde × d) ÷ molar kütle bağıntısıyla da bulunur. Örnek: %20’lik, d = 1,1 g/mL, molar kütlesi 55 g/mol olan çözeltide M = 10 × 20 × 1,1 ÷ 55 = 4 M’dır')
B_I=B('İyon derişimi','Suda tamamen iyonlaşan bir tuzun iyon derişimi, tuz derişimi ile formüldeki iyon sayısının çarpımıdır. Örnek: 0,1 M CaCl₂ çözeltisinde Ca²⁺ 0,1 M, Cl⁻ ise 0,2 M’dır')
B_K=B('Çözeltileri karıştırma','Aynı iyonun mol sayıları toplanır, toplam hacme bölünür: M = (M₁V₁ + M₂V₂) ÷ (V₁ + V₂). Su eklemek hacmi artırır, mol sayısını değiştirmez; M₁V₁ = M₂V₂ yazılabilir. Örnek: 2 M’lık 100 mL çözeltiye su eklenerek 400 mL yapılırsa derişim 0,5 M olur')
B_S=B('Kütlece yüzde','Kütlece yüzde = çözünen kütlesi ÷ çözelti kütlesi × 100. Çözeltiler karıştırılırken çözünen kütleleri ve çözelti kütleleri ayrı ayrı toplanır; buharlaşan su yalnız çözelti kütlesini azaltır. Örnek: 80 g çözeltide 8 g çözünen varsa yüzde 10’dur')
B_KOL=B('Koligatif özellikler','Uçucu olmayan bir madde çözününce buhar basıncı düşer, kaynama noktası yükselir, donma noktası düşer. Değişim çözünen taneciklerin sayısına bağlıdır: ΔT = i × K × m (i: iyonlaşma sonucu tanecik sayısı katsayısı). Örnek: 1 m şekerli suda i = 1, 1 m CaCl₂ çözeltisinde i = 3 alınır')
B_KY=B('Koligatif özelliklerin karşılaştırılması','Aynı çözücüde i × m değeri büyük olan çözeltinin buhar basıncı daha düşük, kaynama noktası daha yüksek, donma noktası daha düşüktür. Örnek: 0,1 m NaCl (i × m = 0,2) çözeltisi, 0,1 m şekerli (i × m = 0,1) çözeltiden daha yüksek sıcaklıkta kaynar')
B_O=B('Ozmos','Çözücü taneciklerinin yalnız çözücüyü geçiren yarı geçirgen bir zardan, seyreltik çözeltiden derişik çözeltiye doğru net geçişine ozmos denir. Derişik tarafta sıvı yükselir ve oluşan hidrostatik basınç ozmotik basıncı dengeler. Örnek: saf su ile tuzlu su zarla ayrılırsa su, tuzlu suya geçer')
B_C=B('Çözünürlük','Belirli sıcaklıkta 100 g suda çözünebilen en çok madde kütlesidir. Doygun çözeltide su kütlesi ile çözünen kütlesi orantılıdır. Soğutmada çöken madde = (başlangıçtaki çözünen) − (yeni sıcaklıktaki su kütlesine göre çözünebilen). Örnek: 25 °C’de 40 g/100 g su ise 50 g suda en çok 20 g çözünür')
B_E=B('Çözünürlüğü etkileyen faktörler','Katıların çözünme ısısı pozitifse (endotermik) çözünürlük sıcaklıkla artar, negatifse azalır. Gazların çözünmesi genellikle egzotermiktir; sıcaklık artınca çözünürlük azalır, basınç artınca artar (Henry yasası). Örnek: soda şişesi açılınca basınç düşer, gaz çıkar')
B_EN=B('Çözünme entalpisi','Çözünme iki basamaklıdır: kristal kafesin dağılması (endotermik, +) ve iyonların su ile sarılması, yani hidratasyon (egzotermik, −). ΔH(çözünme) = ΔH(kafes) + ΔH(hidratasyon). Örnek: +700 kJ/mol ve −650 kJ/mol ise ΔH = +50 kJ/mol olur, çözünme endotermiktir')
# ================= KARTLAR =================
kartla('K-AKCOZ-01','Molarite','Molarite çözünenin mol sayısının çözelti hacmine (L) oranıdır; kütle önce mole çevrilir.','Kütleyi mole çevirmemek; hacmi mL olarak bölmek.','kolay','şekilli',3,'cozelti-derisim','Derişim birimleri ve dönüşümleri')
kartla('K-AKCOZ-02','Yüzde–yoğunluk–molarite','1 L çözeltinin kütlesi yoğunluktan, çözünen kütlesi yüzdeden bulunur; mol sayısı molarite verir.','Yoğunluğu hiç kullanmamak; 10 çarpanını atlamak.','orta','tablo',3,'cozelti-derisim','Derişim birimleri ve dönüşümleri')
kartla('K-AKCOZ-03','Molalite','Molalitede payda çözücünün kütlesidir (kg); çözelti kütlesinden çözücü bulunur.','Çözelti kütlesini çözücü kütlesi sanmak; çözünenin mol sayısı yerine kütle yazmak.','orta','şekilli',3,'cozelti-derisim','Derişim birimleri ve dönüşümleri')
kartla('K-AKCOZ-04','İyon derişimi ve karıştırma','Her iyonun mol sayısı tuz mol sayısı × formüldeki iyon sayısıdır; toplam mol toplam hacme bölünür.','İyon katsayısını atlamak; derişimlerin ortalamasını almak.','orta','şekilli',4,'cozelti-karisim-iyon','Çözeltileri karıştırma ve iyon derişimi')
kartla('K-AKCOZ-05','Seyreltme ve buharlaştırma','Su ekleme ya da buharlaştırmada çözünen miktarı sabittir: M₁V₁ = M₂V₂ ya da çözünen kütlesi sabit.','Eklenen su ile son hacmi karıştırmak; buharlaşan suyu çözeltiye eklemek.','orta','şekilli',4,'cozelti-seyreltme','Seyreltme, buharlaştırma ve karıştırma')
kartla('K-AKCOZ-06','Koligatif özellik hesabı','ΔT = i × K × m; tanecik sayısı katsayısı i ve molalite birlikte kullanılır.','i’yi atlamak; molalite yerine mol sayısı yazmak; donma noktası düşmesini artış saymak.','orta','şekilli',4,'cozelti-koligatif-hesap','Koligatif özelliklerle hesaplama')
kartla('K-AKCOZ-07','Koligatif özellik yorumu','Aynı çözücüde i × m büyüdükçe buhar basıncı azalır, kaynama noktası artar, donma noktası düşer.','Yalnız derişime bakıp iyon sayısını unutmak; buhar basıncı ile kaynama noktasını karıştırmak.','orta','öncüllü',3,'cozelti-koligatif-yorum','Koligatif özelliklerin yorumlanması')
kartla('K-AKCOZ-08','Ozmos','Çözücü, seyreltik taraftan derişik tarafa geçer; derişik koldaki sıvı yükselir.','Çözünenin zardan geçtiğini sanmak; dengede derişimlerin eşitleneceğini düşünmek.','orta','şekilli',3,'cozelti-koligatif-yorum','Koligatif özelliklerin yorumlanması')
kartla('K-AKCOZ-09','Çözünürlük ve çökelme','Doygun çözeltide su kütlesi ile çözünürlük orantılıdır; soğutmada çöken = eldeki çözünen − yeni çözünebilen.','100 g su için verilen değeri gerçek su kütlesine ölçeklememek.','orta','tablo',4,'cozelti-cozunurluk-hesap','Çözünürlük hesapları')
kartla('K-AKCOZ-10','Çözünürlüğü etkileyen faktörler','Çözünürlüğün sıcaklıkla değişimi çözünme ısısının işaretini verir; gaz çözünürlüğü sıcaklıkla azalır.','Her katının sıcaklıkla çözünürlüğünün arttığını sanmak.','orta','grafik',3,'cozelti-cozunurluk-etken','Çözünürlüğü etkileyen faktörler')
kartla('K-AKCOZ-11','Çözünme entalpisi','ΔH(çözünme) kafes enerjisi ile hidratasyon enerjisinin toplamıdır; işaret çözünürlüğün sıcaklık davranışını ve ortam sıcaklığını belirler.','Hidratasyonu endotermik saymak; iki terimin işaretini karıştırmak.','orta','şekilli',3,'cozelti-cozunme-enerji','Çözünme sürecinde enerji')
kartla('K-AKCOZ-12','Molar kütle ve koligatif özellik','Koligatif değişimden molalite, oradan mol sayısı ve molar kütle bulunur.','Çözücü kütlesini yanlış birimle kullanmak; oranı ters almak.','zor','grafik',5,'cozelti-koligatif-hesap','Koligatif özelliklerle hesaplama')
kartla('K-AKCOZ-13','Derişim dönüşümü ve kaynama noktası','Molarite ve yoğunluktan çözücü kütlesi, oradan molalite ve kaynama noktası yükselmesi bulunur.','Çözücü kütlesi yerine çözelti kütlesi kullanmak; i’yi atlamak.','zor','şekilli',5,'cozelti-koligatif-hesap','Koligatif özelliklerle hesaplama')
g=lambda *a: None
# ================= 01 · kolay · molarite (balon joje) =================
m_s=F(20); Mm=F(40); V=F('0.25'); n=m_s/Mm; M1=n/V
assert (n,M1)==(F(1,2),2)
d_a=n; d_b=n*V; d_c=n/F(250); d_d=m_s/V
assert len({M1,d_a,d_b,d_c,d_d})==5
sk=fig('\\draw[thick,fill=vurgu!15] (0,0) circle (1.15);',
 '\\fill[vurgu!15] (-.28,.9) rectangle (.28,1.85);',
 '\\draw[thick] (-.28,.98) -- (-.28,2.7) (.28,.98) -- (.28,2.7);',
 '\\draw[thick] (-.42,2.7) -- (.42,2.7);',
 '\\draw[very thick,vurgu!70!black] (-.28,1.85) -- (.28,1.85);',
 '\\draw[dashed] (.28,1.85) -- (1.5,1.85);',
 '\\node[right] at (1.5,1.85) {250 mL işareti};',
 '\\node[left] at (-1.3,.3) {\\begin{tabular}{r}20 g NaOH\\\\su ile\\\\tamamlandı\\end{tabular}};')
q('0001',tipId='cozelti-derisim',tip='Derişim birimleri ve dönüşümleri',z='kolay',alt='Derişim Birimleri',kaz='Kütlesi ve hacmi verilen çözeltinin molaritesini hesaplar.',
 kart='K-AKCOZ-01 (molarite) · 20 g NaOH, 250 mL',kalip='şekilli',
 metin='Bir öğrenci 20 g NaOH katısını suda çözerek şekildeki ölçülü balon jojenin 250 mL işaretine kadar su ile tamamlıyor.\nBuna göre hazırlanan çözeltinin molaritesi kaç M’dır? (NaOH = 40 g/mol)',
 dogru=M1,yan=[(d_a,'Mol sayısını hacme bölmeden doğrudan molarite saymış: 20 ÷ 40 = 0,5.','dikkat'),(d_b,'Mol sayısını hacimle çarpmış: 0,5 × 0,25 = 0,125.','islem'),(d_c,'Hacmi litreye çevirmeden mL ile bölmüş: 0,5 ÷ 250 = 0,002.','dikkat'),(d_d,'Kütleyi mole çevirmeden hacme bölmüş: 20 ÷ 0,25 = 80.','bilgi')],
 istenen='Çözeltinin molaritesi (M).',ip=['Molarite hesabında çözünen madde miktarı mol, hacim ise litre cinsinden alınır.'],bilgi=[B_M],
 ad=[A('Mol sayısını bul','Çözünen kütlesi molar kütleye bölünür.','n = 20 ÷ 40 = 0,5 mol'),A('Hacmi litreye çevir','250 mL, 0,25 L’dir.','V = 0,25 L'),A('Molariteyi hesapla','Molarite, mol sayısının hacme oranıdır.','M = 0,5 ÷ 0,25 = 2 M')],
 puf='Molaritede kütle önce mole, hacim önce litreye çevrilir.',sekil=sk)
# ================= 02 · kolay · P-T grafiği (olumsuz) =================
def ptegri(x0,k=.9,ymax=3.45):
    pts=[]; x=x0-2.4
    while x<=x0+math.log(ymax/2)/k+1e-9:
        y=2*math.exp(k*(x-x0))
        if y>=.05: pts.append((x,y))
        x+=.1
    return ' '.join(f'({a:.2f},{b:.2f})' for a,b in pts), x0+math.log(ymax/2)/k
def eksen(xw,yw,xl,yl):
    return [f'\\draw[->,thick] (0,0) -- ({xw},0) node[below left] {{{xl}}};',f'\\draw[->,thick] (0,0) -- (0,{yw}) node[left] {{{yl}}};']
a1,e1=ptegri(3.0); a2,e2=ptegri(3.7)
sk=fig(*eksen(5.6,3.9,'Sıcaklık','Buhar basıncı'),
 '\\draw[dashed,gray] (0,2) -- (4.4,2); \\node[left] at (0,2) {1 atm};',
 f'\\draw[thick,vurgu!70!black] plot[smooth] coordinates {{{a1}}}; \\node[above] at ({e1:.2f},3.45) {{\\textbf{{X}}}};',
 f'\\draw[thick,dashed,orange!80!black] plot[smooth] coordinates {{{a2}}}; \\node[above] at ({e2:.2f},3.45) {{\\textbf{{Y}}}};',
 '\\draw[dotted] (3.0,2) -- (3.0,0) node[below] {$T_1$}; \\draw[dotted] (3.7,2) -- (3.7,0) node[below] {$T_2$};')
S=[('Y çözeltisinin donma noktası saf suyun donma noktasından yüksektir.',False,'çözünen donma noktasını düşürür, yükseltmez'),
   ('X eğrisi saf suya aittir.',True,'aynı sıcaklıkta buhar basıncı en yüksek olan eğri saf çözücüdür'),
   ('Y çözeltisi, 1 atm basınçta saf sudan daha yüksek sıcaklıkta kaynar.',True,'buhar basıncı 1 atm’ye daha yüksek sıcaklıkta ulaşır'),
   ('Aynı sıcaklıkta Y çözeltisinin buhar basıncı saf suyunkinden düşüktür.',True,'uçucu olmayan çözünen buhar basıncını düşürür'),
   ('Y çözeltisinin kaynama noktası ile saf suyun kaynama noktası arasındaki fark T₂ − T₁’dir.',True,'şekilde kaynama noktaları 1 atm doğrusunun eğrileri kestiği sıcaklıklardır')]
def tek(sec,hedef=True,tur='bilgi'):
    assert len(sec)==5; h=[s for s in sec if s[1]==hedef]; assert len(h)==1
    yan=[(m,(f'Bu ifadeyi doğru sanmış; oysa doğrudur: {n}.' if not hedef else f'Bu ifadeyi yanlış sanmış; oysa {n}.'),tur) for m,b,n in sec if b!=hedef]
    # hedef False: aranan yanlış ifade; diğerleri doğru (yanlış sanma hatası)
    if not hedef: yan=[(m,f'Bu ifadeyi yanlış sanmış; oysa doğrudur, çünkü {n}.',tur) for m,b,n in sec if b!=hedef]
    return dict(dogru=h[0][0],yan=yan,sira=[s[0] for s in sec])
r=tek(S,False)
q('0002',tipId='cozelti-koligatif-yorum',tip='Koligatif özelliklerin yorumlanması',z='kolay',alt='Koligatif Özellikler',kaz='Buhar basıncı–sıcaklık grafiğinden saf çözücü ve çözeltinin özelliklerini karşılaştırır.',
 kart='K-AKCOZ-07 (koligatif yorum) · saf su ve şekerli su eğrileri',kalip='grafik',
 metin='Şekilde saf suya ve uçucu olmayan bir maddenin sulu çözeltisine ait buhar basıncı–sıcaklık grafikleri verilmiştir.\nBuna göre aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yargı.',
 ip=['Koligatif özelliklerde çözünen eklenince buhar basıncı, kaynama noktası ve donma noktasının hangi yönde değiştiğini düşün.'],bilgi=[B_KOL],
 ad=[A('Eğrileri tanı','Aynı sıcaklıkta buhar basıncı yüksek olan eğri saf suya aittir.','X: saf su, Y: çözelti'),A('Kaynama noktalarını oku','1 atm doğrusunu eğrilerin kestiği sıcaklıklar kaynama noktalarıdır.','T₁ < T₂'),A('Donma noktasını yorumla','Çözünen donma noktasını düşürür.','Y çözeltisinin donma noktası saf sudan düşüktür'),A('İfadeleri ele','Donma noktasının yükseldiğini söyleyen ifade yanlıştır.','Yanlış olan ifade: donma noktasının yüksek olması')],
 puf='Uçucu olmayan çözünen buhar basıncını ve donma noktasını düşürür, kaynama noktasını yükseltir.',sekil=sk)
# ================= 03 · kolay · tanecik modeli (öncüllü) =================
def molek(cx,cy,pos): return ''.join(f'\\draw[fill=gray!35] ({cx+x:.2f},{cy+y:.2f}) circle (.13);' for x,y in pos)
def kap(x,y,w,h,lvl): return f'\\fill[vurgu!12] ({x},{y}) rectangle ({x+w},{y+lvl}); \\draw[thick] ({x},{y+h}) -- ({x},{y}) -- ({x+w},{y}) -- ({x+w},{y+h});'
def iyon(x,y,s,kat=True):
    return (f'\\draw[fill=orange!35] ({x:.2f},{y:.2f}) circle (.17); \\node[font=\\scriptsize] at ({x:.2f},{y:.2f}) {{{s}}};' if kat else
            f'\\draw[fill=blue!15] ({x:.2f},{y:.2f}) circle (.14); \\node[font=\\scriptsize] at ({x:.2f},{y:.2f}) {{{s}}};')
P1=[(.3,.4),(.9,.8),(1.5,.35),(.5,1.0),(1.2,1.2),(1.55,.9)][:3]; P1=[(.35,.45),(1.2,.7),(.7,1.1)]
parts=[kap(0,0,2.4,1.9,1.5),molek(0,0,[(.5,.5),(1.4,.9),(.9,1.1)]),'\\node at (1.2,-.35) {X};',
 kap(3.0,0,2.4,1.9,1.5)]
Y=[(3.0+.5,.5,'+',True),(3.0+1.0,.45,'$-$',False),(3.0+1.6,.9,'+',True),(3.0+2.0,.5,'$-$',False),(3.0+.7,1.1,'+',True),(3.0+1.3,1.2,'$-$',False)]
parts+=[iyon(*t) for t in Y]+['\\node at (4.2,-.35) {Y};']
parts+=[kap(6.0,0,2.4,1.9,1.5)]
Z=[(6.0+.45,.45,'2+',True),(6.0+1.0,.4,'$-$',False),(6.0+1.5,.5,'$-$',False),(6.0+.8,1.05,'2+',True),(6.0+1.9,.45,'$-$',False),(6.0+.3,1.15,'$-$',False),(6.0+1.4,1.1,'2+',True),(6.0+1.05,.75,'$-$',False),(6.0+1.95,1.15,'$-$',False)]
parts+=[iyon(*t) for t in Z]+['\\node at (7.2,-.35) {Z};']
sk=fig(*parts)
truth={'I':True,'II':True,'III':False}
reasons={'I':'her kapta 3 formül birimi çözündüğünden tanecik sayısı Z’de 9, Y’de 6 ve X’te 3’tür; tanecik sayısı en çok olan Z’nin kaynama noktası en yüksektir',
 'II':'X çözeltisinde iyon yoktur, moleküller serbestçe hareket eden yük taşıyıcı olmadığından elektrik akımı iletilmez',
 'III':'Y çözeltisinde 6, Z çözeltisinde 9 tanecik bulunur; tanecik sayıları farklı olduğundan donma noktası alçalmaları da farklıdır'}
dg,yn,ad=onc(truth,reasons,S5c)
q('0003',tipId='cozelti-koligatif-yorum',tip='Koligatif özelliklerin yorumlanması',z='kolay',alt='Koligatif Özellikler',kaz='Çözünmüş tanecik modellerinden elektrik iletkenliğini ve koligatif özellikleri yorumlar.',
 kart='K-AKCOZ-07 (koligatif yorum) · X, Y, Z tanecik modelleri',kalip='öncüllü',
 metin='Şekilde, aynı sıcaklıktaki eşit hacimli X, Y ve Z sulu çözeltilerindeki çözünmüş taneciklerin modeli gösterilmiştir. Her kapta 3 formül birimi (ya da molekül) çözünmüştür; X moleküler, Y ve Z iyonik bir maddedir ve su molekülleri gösterilmemiştir.\nI. Kaynamaya başlama sıcaklığı en yüksek olan çözelti Z’dir.\nII. X çözeltisi elektrik akımını iletmez.\nIII. Y ve Z çözeltilerinin donmaya başlama sıcaklıkları eşittir.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=dg,yan=yn,sira=S5c,istenen='Doğru olan öncüller.',
 ip=['Koligatif özellikler çözünen taneciklerin cinsine değil toplam sayısına bağlıdır; her kaptaki tanecikleri say.'],bilgi=[B_KOL,B_KY],ad=ad,
 puf='Tanecik sayısı çok olan çözelti daha yüksek sıcaklıkta kaynar ve daha düşük sıcaklıkta donar; iyon yoksa akım iletilmez.',sekil=sk)
# ================= 04 · orta · yüzde–yoğunluk–molarite (etiket) =================
pct=F(49); d=F('1.4'); Ms=F(98)
M4=F(10)*pct*d/Ms; assert M4==7
d_a=pct*d/Ms; d_b=F(10)*pct/Ms; d_c=M4*2; d_d=F(10)*pct*d
assert d_a==F(7,10) and d_b==5 and d_c==14 and d_d==686 and len({M4,d_a,d_b,d_c,d_d})==5
sk=fig('\\draw[thick] (-.5,2.6) -- (-.5,2.9) -- (.5,2.9) -- (.5,2.6);',
 '\\draw[thick,fill=vurgu!10] (-1.5,0) rectangle (1.5,2.6);',
 '\\draw[thick,fill=white] (-1.3,.4) rectangle (1.3,2.0);',
 '\\node at (0,1.65) {\\textbf{\\ce{H2SO4} çözeltisi}};',
 '\\node at (0,1.2) {kütlece \\%49};',
 '\\node at (0,.75) {$d=1{,}4$ g/mL};')
q('0004',tipId='cozelti-derisim',tip='Derişim birimleri ve dönüşümleri',z='orta',alt='Derişim Birimleri',kaz='Kütlece yüzde ve yoğunluğu verilen çözeltinin molaritesini hesaplar.',
 kart='K-AKCOZ-02 (yüzde–yoğunluk–molarite) · %49 H₂SO₄, d = 1,4',kalip='şekilli',
 metin='Şekildeki şişenin etiketinde, laboratuvarda kullanılan sülfürik asit çözeltisinin kütlece yüzdesi ve yoğunluğu verilmiştir.\nBuna göre bu çözeltinin molaritesi kaç M’dır? (H₂SO₄ = 98 g/mol)',
 dogru=M4,yan=[(d_a,'Bağıntıdaki 10 çarpanını atlamış: 49 × 1,4 ÷ 98 = 0,7.','islem'),(d_b,'Yoğunluğu kullanmamış: 10 × 49 ÷ 98 = 5.','bilgi'),(d_c,'Molar kütle yerine 49 g/mol (yarısı) kullanmış: 10 × 49 × 1,4 ÷ 49 = 14.','dikkat'),(d_d,'Molar kütleye bölmeyi unutmuş: 10 × 49 × 1,4 = 686.','dikkat')],
 istenen='Çözeltinin molaritesi (M).',ip=['1 L çözeltinin kütlesini yoğunluktan, içindeki asit kütlesini de yüzdeden bulmayı dene.'],bilgi=[B_Y],
 ad=[A('1 L çözeltinin kütlesi','Yoğunluk 1,4 g/mL olduğundan 1000 mL çözelti 1400 g gelir.','m = 1400 g'),A('Asit kütlesi','Kütlece %49 olduğundan çözünen kütlesi bulunur.','1400 × 0,49 = 686 g'),A('Mol sayısı','Kütle molar kütleye bölünür.','686 ÷ 98 = 7 mol'),A('Molarite','1 L çözeltideki mol sayısı molaritedir.','M = 7 M')],
 puf='Yüzde ve yoğunluk verilmişse 1 L çözeltiyi (1000 mL) esas alıp kütleden mole git.',sekil=sk)
# ================= 05 · orta · molalite (çubuk) =================
m_n=F(20); m_su=F(80); n5=m_n/F(40); m5=n5/(m_su/1000)
assert m5==F('6.25')
d_a=n5; d_b=n5/F('0.1'); d_c=m_n/(m_su/1000); d_d=n5/F('0.008')
assert d_b==5 and d_c==250 and d_a==F(1,2) and len({m5,d_a,d_b,d_c})==4
d_d=F(25)  # 20/0.8: kütleyi mol yerine g alıp 0,8 kg ile bölmüş
assert m_n/m_su==F('0.25') and n5/F('0.8')==F('0.625') and len({m5,F(1,2),F(5),F('0.625'),F('0.25')})==5
sk=fig('\\fill[vurgu!35] (0,0) rectangle (1.2,.9); \\fill[gray!15] (1.2,0) rectangle (6,.9); \\draw[thick] (0,0) rectangle (6,.9); \\draw[thick] (1.2,0) -- (1.2,.9);',
 '\\node at (.6,.45) {\\small NaOH}; \\node at (3.6,.45) {su};',
 '\\draw[<->] (0,-.35) -- (1.2,-.35) node[midway,below] {20 g}; \\draw[<->] (1.2,-.35) -- (6,-.35) node[midway,below] {80 g};',
 '\\node[above] at (3,.95) {100 g NaOH sulu çözeltisi};')
q('0005',tipId='cozelti-derisim',tip='Derişim birimleri ve dönüşümleri',z='orta',alt='Derişim Birimleri',kaz='Çözeltinin kütle bileşiminden molalitesini hesaplar.',
 kart='K-AKCOZ-03 (molalite) · 20 g NaOH, 80 g su',kalip='şekilli',
 metin='Şekilde, belirli bir sıcaklıktaki 100 g NaOH sulu çözeltisinin kütle bileşimi gösterilmiştir.\nBuna göre bu çözeltinin molalitesi kaç molaldır? (NaOH = 40 g/mol)',
 dogru=m5,yan=[(F(1,2),'Çözünenin mol sayısını molalite saymış; çözücü kütlesine bölmemiş: 20 ÷ 40 = 0,5.','dikkat'),(F(5),'Çözücü yerine çözelti kütlesini kullanmış: 0,5 ÷ 0,1 = 5.','bilgi'),(F('0.625'),'80 g çözücüyü 0,8 kg almış: 0,5 ÷ 0,8 = 0,625.','islem'),(F('0.25'),'Kütle oranını molalite saymış: 20 ÷ 80 = 0,25.','dikkat')],
 istenen='Çözeltinin molalitesi (molal).',ip=['Molalitede payda, çözelti değil yalnız çözücünün kütlesidir; kg cinsinden alınır.'],bilgi=[B_M],
 ad=[A('NaOH mol sayısı','Çözünen kütlesi molar kütleye bölünür.','n = 20 ÷ 40 = 0,5 mol'),A('Çözücü kütlesi','Şekilde su 80 g’dır; kg’a çevrilir.','80 g = 0,08 kg'),A('Molalite','Mol sayısı çözücü kütlesine (kg) bölünür.','m = 0,5 ÷ 0,08 = 6,25 molal')],
 puf='Molalitede çözücünün kütlesi (kg) paydadadır; çözeltinin kütlesi değil.',sekil=sk)
# ================= 06 · orta · karıştırma, iyon derişimi =================
V1,M1_,V2,M2_=F('0.2'),F('0.5'),F('0.3'),F('0.2')
so4=M1_*3*V1+M2_*1*V2; M6=so4/(V1+V2); assert so4==F('0.36') and M6==F('0.72')
d_a=(M1_*V1+M2_*V2)/(V1+V2); d_b=so4/1; d_c=(M1_*3+M2_*1)/2; d_d=(M1_*1*V1+M2_*V2)/(V1+V2)
assert d_a==F('0.32') and d_b==F('0.36') and d_c==F('0.85') and d_d==F('0.32')
d_d=(M1_*2*V1+M2_*V2)/(V1+V2); assert d_d==F('0.52')
assert len({M6,d_a,d_b,d_c,d_d})==5
def bk(x,y,w,h,lvl,l1,l2,fill='vurgu!15'):
    return (f'\\fill[{fill}] ({x},{y}) rectangle ({x+w},{y+lvl}); \\draw[thick] ({x},{y+h}) -- ({x},{y}) -- ({x+w},{y}) -- ({x+w},{y+h});'
            f'\\node[below,align=center] at ({x+w/2},{y-.05}) {{{l1}\\\\{l2}}};')
sk=fig(bk(0,0,1.6,1.8,1.2,'200 mL','0,5 M \\ce{Al2(SO4)3}'),'\\node at (2.35,.8) {\\Large $+$};',
 bk(3.0,0,1.6,1.8,1.5,'300 mL','0,2 M \\ce{Na2SO4}'),'\\draw[->,thick] (5.0,.8) -- (5.8,.8);',
 bk(6.2,0,1.6,1.8,1.5,'Karışım','(hacim 500 mL)'))
q('0006',tipId='cozelti-karisim-iyon',tip='Çözeltileri karıştırma ve iyon derişimi',z='orta',alt='Derişim Birimleri',kaz='İki çözeltinin karışımındaki iyon derişimini hesaplar.',
 kart='K-AKCOZ-04 (iyon derişimi ve karıştırma) · Al₂(SO₄)₃ + Na₂SO₄',kalip='şekilli',
 metin='Sıcaklıkları aynı olan şekildeki Al₂(SO₄)₃ ve Na₂SO₄ sulu çözeltileri karıştırılıyor.\nBuna göre oluşan karışımdaki SO₄²⁻ iyonlarının derişimi kaç molardır? (Tuzların suda tamamen iyonlarına ayrışarak çözündüğü ve toplam hacmin 500 mL olduğu varsayılacaktır.)',
 dogru=M6,yan=[(d_a,'İyon katsayılarını yazmadan tuz mollerini toplamış: (0,1 + 0,06) ÷ 0,5 = 0,32.','dikkat'),(d_b,'Toplam mol sayısını hacme bölmemiş: 0,36 mol ÷ 1 L = 0,36.','islem'),(d_c,'İki çözeltideki sülfat derişimlerinin aritmetik ortalamasını almış: (1,5 + 0,2) ÷ 2 = 0,85.','bilgi'),(d_d,'Al₂(SO₄)₃ için sülfat sayısını 2 almış: (0,2 + 0,06) ÷ 0,5 = 0,52.','dikkat')],
 istenen='Karışımdaki SO₄²⁻ derişimi (M).',ip=['Her çözeltideki sülfat iyonunun mol sayısını ayrı ayrı bulup toplam hacme oranlamayı dene.'],bilgi=[B_I,B_K],
 ad=[A('Birinci çözelti','Al₂(SO₄)₃ formülünde 3 sülfat vardır.','0,5 × 3 × 0,2 = 0,3 mol'),A('İkinci çözelti','Na₂SO₄ formülünde 1 sülfat vardır.','0,2 × 1 × 0,3 = 0,06 mol'),A('Toplam mol','Sülfat mol sayıları toplanır.','0,3 + 0,06 = 0,36 mol'),A('Derişim','Toplam mol, toplam hacme (0,5 L) bölünür.','0,36 ÷ 0,5 = 0,72 M')],
 puf='Karışımda önce her iyonun mol sayısını bul, sonra toplam hacme böl; derişimlerin ortalaması alınmaz.',sekil=sk)
# ================= 07 · orta · seyreltme grafiği =================
V07=F(150); C0=F('1.2'); C1=F('0.4'); n07=V07/1000*C0; V2=n07/C1*1000; ek=V2-V07
assert (n07,V2,ek)==(F('0.18'),450,300)
d_a=V2; d_b=V07/3; d_c=V07*(C0/C1+1); d_d=V07*6
assert d_c==600 and len({ek,d_a,d_b,d_c,d_d})==5
# eğri C = 1.2*150/(150+v)  ; çizim: x: v 0..600 -> 0..5.4 (0,009 cm/mL) ; y: C 0..1.4 -> 0..3.5 (2.5 cm/M)
xs=[0,50,100,150,200,300,400,500,600]
pts=' '.join(f'({v*0.009:.3f},{1.2*150/(150+v)*2.5:.3f})' for v in xs)
yc=lambda c: float(c)*2.5
sk=fig(*eksen(5.8,3.8,'Eklenen su hacmi','Derişim (M)'),
 f'\\draw[thick,vurgu!70!black] plot[smooth] coordinates {{{pts}}};',
 f'\\foreach \\c/\\t in {{{yc(1.2):.2f}/1{{,}}2,{yc(.8):.2f}/0{{,}}8,{yc(.4):.2f}/0{{,}}4}} {{\\draw (-.08,\\c) -- (.08,\\c); \\node[left] at (0,\\c) {{\\t}};}}',
 f'\\draw[dashed,gray] (0,{yc(.4):.2f}) -- (2.7,{yc(.4):.2f}); \\fill (2.7,{yc(.4):.2f}) circle (.07); \\node[above right] at (2.7,{yc(.4):.2f}) {{P}};',
 f'\\draw[dashed,gray] (2.7,{yc(.4):.2f}) -- (2.7,0); \\node[below] at (2.7,0) {{$V$}};')
q('0007',tipId='cozelti-seyreltme',tip='Seyreltme, buharlaştırma ve karıştırma',z='orta',alt='Derişim Birimleri',kaz='Seyreltme grafiğinden eklenen su hacmini hesaplar.',
 kart='K-AKCOZ-05 (seyreltme) · 150 mL, 1,2 M',kalip='grafik',
 metin='Başlangıçta 150 mL hacimli bir çözeltiye belirli sıcaklıkta su eklendikçe çözeltinin derişiminin değişimi şekildeki grafikte verilmiştir.\nBuna göre grafikteki P noktasına gelindiğinde çözeltiye eklenen su hacmi (V) kaç mL’dir? (Çözelti hacminin, çözelti ve eklenen su hacimlerinin toplamına eşit olduğu varsayılacaktır.)',
 dogru=ek,yan=[(d_a,'Son hacmi eklenen su sanmış: 0,18 ÷ 0,4 = 0,45 L = 450 mL.','dikkat'),(d_b,'Başlangıç hacmini seyrelme oranına bölmüş: 150 ÷ 3 = 50.','islem'),(d_c,'Seyrelme oranına 1 ekleyip başlangıç hacmiyle çarpmış: 150 × (3 + 1) = 600.','bilgi'),(d_d,'Oranı iki katına çıkararak hesaplamış: 150 × 6 = 900.','islem')],
 istenen='Eklenen su hacmi (mL).',ip=['Su eklenince çözünenin mol sayısı değişmez; başlangıç ve son durumda mol sayısını eşitle.'],bilgi=[B_K],
 ad=[A('Grafikten oku','Başlangıçta derişim 1,2 M, P noktasında 0,4 M’dır.','M₁ = 1,2 M, M₂ = 0,4 M'),A('Mol sayısı sabit','Seyreltmede M₁V₁ = M₂V₂ yazılır.','1,2 × 150 = 0,4 × V₂'),A('Son hacim','V₂ bulunur.','V₂ = 450 mL'),A('Eklenen su','Son hacimden başlangıç hacmi çıkarılır.','450 − 150 = 300 mL')],
 puf='Su eklemede çözünenin mol sayısı sabit kalır; eklenen su, son hacim ile başlangıç hacminin farkıdır.',sekil=sk)
# ================= 08 · orta · donma noktası (NaCl, kap) =================
nNa=F('11.7')/F('58.5'); mm=nNa/F('0.4'); i=2; Kd=F('1.86'); dT=Kd*i*mm; T8=-dT
assert (nNa,mm,dT)==(F('0.2'),F('0.5'),F('1.86'))
d_a=-Kd*mm; d_b=Kd*mm; d_c=-Kd*nNa; d_d=dT
assert d_a==F('-0.93') and d_b==F('0.93') and d_c==F('-0.372') and len({T8,d_a,d_b,d_c,d_d})==5
sk=fig(bk(0,0,2,1.9,1.4,'11,7 g NaCl','400 g su'),'\\node[right,align=left] at (2.5,1.2) {Saf suyun donma\\\\noktası: $0\\,^\\circ$C};')
q('0008',tipId='cozelti-koligatif-hesap',tip='Koligatif özelliklerle hesaplama',z='orta',alt='Koligatif Özellikler',kaz='İyonik çözünenin sulu çözeltisinin donma noktasını hesaplar.',
 kart='K-AKCOZ-06 (koligatif hesap) · NaCl, 400 g su',kalip='şekilli',
 metin='Şekildeki kapta 11,7 g NaCl, 400 g suda tamamen çözünmüştür.\nBuna göre bu çözelti kaç °C’de donmaya başlar? (NaCl = 58,5 g/mol; suyun molal donma noktası alçalması sabiti Kd = 1,86 °C/m; NaCl’nin suda tamamen iyonlarına ayrışarak çözündüğü varsayılacaktır.)',
 dogru=T8,yan=[(d_a,'NaCl’nin iyonlaştığını dikkate almamış (i = 1): −1,86 × 0,5 = −0,93.','bilgi'),(d_b,'NaCl’nin iyonlaştığını dikkate almamış ve alçalmayı sıcaklık saymış: +0,93.','islem'),(d_c,'Molalite yerine mol sayısını kullanmış: −1,86 × 0,2 = −0,372.','dikkat'),(d_d,'Donma noktası alçalmasını sıcaklık olarak yazmış, işareti atlamış: +1,86.','dikkat')],
 istenen='Çözeltinin donmaya başladığı sıcaklık (°C).',ip=['Önce molaliteyi bulup, tamamen iyonlaşan tuz için tanecik sayısını hesaba katmayı dene.'],bilgi=[B_KOL],
 ad=[A('Mol sayısı','Tuzun kütlesi molar kütleye bölünür.','n = 11,7 ÷ 58,5 = 0,2 mol'),A('Molalite','Mol sayısı çözücü kütlesine (0,4 kg) bölünür.','m = 0,2 ÷ 0,4 = 0,5 molal'),A('Donma noktası alçalması','NaCl, Na⁺ ve Cl⁻ olmak üzere 2 iyon verir (i = 2).','ΔT = 2 × 1,86 × 0,5 = 1,86 °C'),A('Donma noktası','Saf suyun donma noktası 0 °C’den alçalma çıkarılır.','T = 0 − 1,86 = −1,86 °C')],
 puf='Donma noktası alçalmasında ΔT = i × Kd × m; sonuç saf çözücünün donma noktasından çıkarılır.',sekil=sk)
# ================= 09 · orta · üç eğri (öncüllü) =================
a3,e3=ptegri(2.7); a4,e4=ptegri(3.35); a5,e5=ptegri(4.0)
sk=fig(*eksen(5.8,3.9,'Sıcaklık','Buhar basıncı'),'\\draw[dashed,gray] (0,2) -- (4.7,2); \\node[left] at (0,2) {1 atm};',
 f'\\draw[thick,vurgu!70!black] plot[smooth] coordinates {{{a3}}}; \\node[above] at ({e3:.2f},3.45) {{\\textbf{{M}}}};',
 f'\\draw[thick,dashed,orange!80!black] plot[smooth] coordinates {{{a4}}}; \\node[above] at ({e4:.2f},3.45) {{\\textbf{{L}}}};',
 f'\\draw[thick,blue!60!black,dash dot] plot[smooth] coordinates {{{a5}}}; \\node[above] at ({e5:.2f},3.45) {{\\textbf{{K}}}};',
 '\\draw[dotted] (2.7,2) -- (2.7,0) node[below] {$T_1$}; \\draw[dotted] (3.35,2) -- (3.35,0) node[below] {$T_2$}; \\draw[dotted] (4.0,2) -- (4.0,0) node[below] {$T_3$};')
truth={'I':False,'II':True,'III':True}
reasons={'I':'tanecik sayısı en fazla olan 0,2 m NaCl çözeltisinin (i × m = 0,4) kaynama noktası en yüksektir ve bu eğri K’dır; K eğrisi glikoz çözeltisine ait değildir',
 'II':'aynı sıcaklıkta buhar basıncı en yüksek olan eğri saf su olan M’dir; çözünen buhar basıncını düşürür',
 'III':'L eğrisi glikoz çözeltisine aittir (i × m = 0,2), donma noktası saf su olan M’ninkinden düşüktür'}
dg,yn,ad=onc(truth,reasons,S5)
q('0009',tipId='cozelti-koligatif-yorum',tip='Koligatif özelliklerin yorumlanması',z='orta',alt='Koligatif Özellikler',kaz='Buhar basıncı–sıcaklık grafiğinden çözeltileri ayırt eder ve özelliklerini yorumlar.',
 kart='K-AKCOZ-07 (koligatif yorum) · saf su, glikoz ve NaCl çözeltisi',kalip='öncüllü',
 metin='Şekilde, saf su ile 0,2 molal C₆H₁₂O₆ ve 0,2 molal NaCl sulu çözeltilerinin buhar basıncı–sıcaklık grafikleri karışık sırayla K, L ve M harfleriyle gösterilmiştir. Çözeltilerde çözünenler uçucu değildir ve NaCl suda tamamen iyonlaşmıştır.\nI. K eğrisi C₆H₁₂O₆ çözeltisine aittir.\nII. Aynı sıcaklıkta buhar basıncı en yüksek olan M’dir.\nIII. L çözeltisinin donmaya başlama sıcaklığı, M’ninkinden düşüktür.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=dg,yan=yn,sira=S5,istenen='Doğru olan öncüller.',
 ip=['Her çözeltinin i × m değerini bulup, bu değerin eğrilerin konumuyla ilişkisini düşün.'],bilgi=[B_KOL,B_KY],ad=ad,
 puf='Büyük i × m değeri, 1 atm doğrusunun kesildiği noktayı sağa, yani daha yüksek kaynama noktasına kaydırır.',sekil=sk)
# ================= 10 · orta · çözünürlük grafiği, soğutma =================
def cgraf(egriler,xt,yt,xmax=100,ymax=110,sx=0.055,sy=0.035,extra=''):
    p=[f'\\draw[->,thick] (0,0) -- ({xmax*sx+.3:.2f},0) node[anchor=north east,yshift=-14pt] {{Sıcaklık ($^\\circ$C)}};',f'\\draw[->,thick] (0,0) -- (0,{ymax*sy+.3:.2f}) node[above] {{Çözünürlük (g/100 g su)}};']
    for t in xt: p.append(f'\\draw[gray!40] ({t*sx:.2f},0) -- ({t*sx:.2f},{ymax*sy:.2f}); \\node[below] at ({t*sx:.2f},0) {{{t}}};')
    for v in yt: p.append(f'\\draw[gray!40] (0,{v*sy:.2f}) -- ({xmax*sx:.2f},{v*sy:.2f}); \\node[left] at (0,{v*sy:.2f}) {{{v}}};')
    for nm,pts,stil,lab in egriler:
        cs=' '.join(f'({a*sx:.2f},{b*sy:.2f})' for a,b in pts)
        p.append(f'\\draw[thick,{stil}] plot coordinates {{{cs}}};')
        a,b=lab; p.append(f'\\node[font=\\small\\bfseries] at ({a*sx:.2f},{b*sy:.2f}) {{{nm}}};')
    return p+[extra]
SX=lambda T: T+10
chk=240; X50=SX(50); su=F(chk)*100/(100+X50); xk=chk-su; kalan=su/100*SX(20); cok=xk-kalan
assert (X50,su,xk,kalan,cok)==(60,150,90,45,45)
d_a=SX(50); d_b=su; d_c=xk; d_d=xk+kalan
assert (d_a,d_b,d_c,d_d)==(60,150,90,135) and len({cok,d_a,d_b,d_c,d_d})==5
sk=fig(*cgraf([('X',[(0,10),(100,110)],'vurgu!70!black',(92,100))],[20,50,80],[30,60,90]))
q('0010',tipId='cozelti-cozunurluk-hesap',tip='Çözünürlük hesapları',z='orta',alt='Çözünürlük',kaz='Çözünürlük–sıcaklık grafiğinden soğutmada çöken madde miktarını hesaplar.',
 kart='K-AKCOZ-09 (çözünürlük ve çökelme) · X katısı, 240 g doygun çözelti',kalip='grafik',
 metin='X katısının sudaki çözünürlüğünün sıcaklıkla değişimi şekildeki grafikte verilmiştir.\n50 °C’de hazırlanan 240 g doygun X sulu çözeltisi 20 °C’a soğutulduğunda dibe çöken X katısı kaç gramdır?',
 dogru=cok,yan=[(d_a,'50 °C’deki çözünürlük değerini çöken miktar saymış: 60.','bilgi'),(d_b,'Çözeltideki su kütlesini çöken X kütlesi saymış: 150.','dikkat'),(d_c,'Çözeltideki tüm X’i çöken saymış: 240 × 60 ÷ 160 = 90.','islem'),(d_d,'Çözeltide kalan X ile başlangıçtaki X’i toplamış: 90 + 45 = 135.','dikkat')],
 istenen='Çöken X katısının kütlesi (g).',ip=['Önce çözeltideki su kütlesini bulup, o su kütlesinin 20 °C’de en çok ne kadar X çözebileceğini hesaplamayı dene.'],bilgi=[B_C],
 ad=[A('Grafikten oku','50 °C’de çözünürlük 60, 20 °C’de 30 g/100 g sudur.','S₅₀ = 60, S₂₀ = 30'),A('Çözeltiyi parçala','100 g suya 60 g X çözünür; çözelti 160 g olur. 240 g için oranla.','Su = 150 g, X = 90 g'),A('20 °C’de çözünebilen','150 g su, 20 °C’de 30 × 1,5 kadar X çözer.','45 g X çözeltide kalır'),A('Çöken','Başlangıçtaki X’ten kalan çıkarılır.','90 − 45 = 45 g')],
 puf='Çözünürlük 100 g su içindir; önce gerçek su kütlesine ölçekle, sonra çıkar.',sekil=sk)
# ================= 11 · orta · çözünürlük eğrileri (öncüllü) =================
sk=fig(*cgraf([('K',[(0,20),(100,95)],'vurgu!70!black',(92,102)),('L',[(0,60),(100,20)],'orange!80!black',(8,66)),('M',[(0,35),(100,40)],'blue!60!black',(10,31))],[20,50,80],[20,40,60,80],ymax=105))
truth={'I':True,'II':False,'III':True}
reasons={'I':'sıcaklık arttıkça K’nın çözünürlüğü artar; bu, çözünmenin ortamdan ısı alan (endotermik) bir süreç olduğunu gösterir',
 'II':'L’nin çözünürlüğü sıcaklıkla azaldığından çözünmesi ortama ısı veren (egzotermik) bir süreçtir; ΔH sıfırdan küçüktür',
 'III':'M’nin çözünürlüğü sıcaklıkla çok az değişir; bu, çözünmenin ısı alışverişinin çok küçük olduğunu gösterir'}
dg,yn,ad=onc(truth,reasons,S5)
q('0011',tipId='cozelti-cozunurluk-etken',tip='Çözünürlüğü etkileyen faktörler',z='orta',alt='Çözünürlük',kaz='Çözünürlük–sıcaklık eğrilerinden çözünme ısısının işaretini yorumlar.',
 kart='K-AKCOZ-10 (çözünürlük faktörleri) · K, L ve M katıları',kalip='öncüllü',
 metin='Şekilde, K, L ve M katılarının sudaki çözünürlüklerinin sıcaklıkla değişimi verilmiştir.\nI. K’nın suda çözünmesi endotermiktir.\nII. L’nin çözünme entalpisi (ΔH) sıfırdan büyüktür.\nIII. M’nin suda çözünmesi sırasındaki ısı alışverişi, K ve L’ninkine göre çok küçüktür.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=dg,yan=yn,sira=S5,istenen='Doğru olan öncüller.',
 ip=['Eğrilerin eğimini, çözünme entalpisiyle ilişkilendirmeyi dene.'],bilgi=[B_E],ad=ad,
 puf='Çözünürlük eğrisinin eğimi, çözünmenin ısı alışverişi hakkında bilgi verir.',sekil=sk)
# ================= 12 · orta · enerji diyagramı (öncüllü) =================
kafes=F(800); hid=F(-780); dH=kafes+hid; assert dH==20
h=lambda e: float(e)*2.2/800
sk=fig('\\draw[->,thick] (0,-.2) -- (0,3.2) node[above] {Enerji};',
 f'\\draw[thick] (.6,{h(0)+.0:.2f}) -- (2.2,{h(0):.2f}); \\node[below] at (1.4,0) {{MX(k)}};',
 f'\\draw[thick] (3.6,{h(800):.2f}) -- (5.6,{h(800):.2f}); \\node[above] at (4.6,{h(800):.2f}) {{$\\mathrm{{M^+(g)+X^-(g)}}$}};',
 f'\\draw[thick] (6.7,{h(20)+.0:.2f}) -- (8.3,{h(20):.2f}); \\node[below] at (7.4,{h(20):.2f}) {{$\\mathrm{{M^+(suda)+X^-(suda)}}$}};',
 f'\\draw[->,thick,vurgu!70!black] (2.9,{h(0):.2f}) -- (2.9,{h(800):.2f}); \\draw[dashed,gray] (2.2,0) -- (3.6,0); \\draw[dashed,gray] (2.2,{h(800):.2f}) -- (3.6,{h(800):.2f}); \\node[left,align=right] at (2.85,1.1) {{+800 kJ/mol}};',
 f'\\draw[->,thick,orange!80!black] (6.1,{h(800):.2f}) -- (6.1,{h(20):.2f}); \\draw[dashed,gray] (5.6,{h(800):.2f}) -- (6.7,{h(800):.2f}); \\draw[dashed,gray] (6.1,{h(20):.2f}) -- (6.7,{h(20):.2f}); \\node[right] at (6.15,1.3) {{$-780$ kJ/mol}};')
truth={'I':True,'II':True,'III':False}
reasons={'I':'ΔH(çözünme) = +800 + (−780) = +20 kJ/mol olduğundan çözünme ısı alan (endotermik) bir süreçtir',
 'II':'çözünme ortamdan ısı aldığı için çözelti soğur ve sıcaklığı düşer',
 'III':'çözünme endotermik olduğundan sıcaklık arttıkça denge çözünme yönüne kayar ve çözünürlük artar, azalmaz'}
dg,yn,ad=onc(truth,reasons,S5)
q('0012',tipId='cozelti-cozunme-enerji',tip='Çözünme sürecinde enerji',z='orta',alt='Çözünme Süreci',kaz='Enerji diyagramından çözünme entalpisini ve sonuçlarını yorumlar.',
 kart='K-AKCOZ-11 (çözünme entalpisi) · MX katısı',kalip='öncüllü',
 metin='Şekilde, iyonik MX katısının suda çözünmesine ilişkin enerji değişimleri verilmiştir.\nI. MX’in suda çözünmesi endotermiktir.\nII. MX çözünürken çözeltinin sıcaklığı düşer.\nIII. Sıcaklık arttıkça MX’in sudaki çözünürlüğü azalır.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=dg,yan=yn,sira=S5,istenen='Doğru olan öncüller.',
 ip=['Kafesin dağılması ve iyonların hidratasyonu sırasındaki enerji değişimlerini toplayarak net işareti bulmayı dene.'],bilgi=[B_EN],ad=ad,
 puf='Kafesin dağılması ve hidratasyonun enerjilerini işaretleriyle topla.',sekil=sk)
# ================= 13 · orta · ozmos U tüpü (olumsuz, öncüllü) =================
sk=fig('\\fill[vurgu!12] (0,0) rectangle (1,2.0); \\fill[vurgu!12] (1,0) rectangle (1.45,.6);',
 '\\fill[vurgu!45] (1.9,0) rectangle (2.9,2.0); \\fill[vurgu!45] (1.45,0) rectangle (1.9,.6);',
 '\\draw[thick] (0,3.4) -- (0,0) -- (2.9,0) -- (2.9,3.4); \\draw[thick] (1,3.4) -- (1,.6) -- (1.9,.6) -- (1.9,3.4);',
 '\\draw[very thick,dash pattern=on 3pt off 2pt,orange!80!black] (1.45,0) -- (1.45,.6);',
 '\\node at (.5,1.2) {0,1 M}; \\node at (2.4,1.2) {0,3 M};',
 '\\draw[dashed,gray] (-.3,2.0) -- (3.2,2.0); \\node[right] at (3.2,2.0) {başlangıç düzeyi};',
 '\\node[align=center,font=\\footnotesize] at (1.45,-.55) {yarı geçirgen zar};')
truth={'I':True,'II':True,'III':False}
reasons={'I':'su molekülleri seyreltik çözeltiden (0,1 M) derişik çözeltiye (0,3 M) doğru net geçer',
 'II':'net su geçişi derişik çözeltiye doğru olduğundan sağ koldaki sıvı yükselir',
 'III':'denge, derişimlerin eşitlenmesiyle değil, iki kol arasındaki hidrostatik basınç farkının ozmotik basıncı dengelemesiyle kurulur; çözünen zardan geçmediğinden derişimler hiçbir zaman eşitlenmez'}
dg,yn,ad=onc(truth,reasons,S5b,neg=True)
q('0013',tipId='cozelti-koligatif-yorum',tip='Koligatif özelliklerin yorumlanması',z='orta',alt='Koligatif Özellikler',kaz='Yarı geçirgen zarlı düzenekte ozmos olayını yorumlar.',
 kart='K-AKCOZ-08 (ozmos) · U tüpü, 0,1 M ve 0,3 M çözelti',kalip='öncüllü',
 metin='Şekildeki U borusunun orta bölümüne yalnız su moleküllerini geçiren yarı geçirgen bir zar yerleştirilmiş; zarın solundaki kola 0,1 M, sağındaki kola 0,3 M glikoz sulu çözeltisi eşit yükseklikte konulmuştur.\nI. Su molekülleri soldan sağa doğru net geçiş yapar.\nII. Zamanla sağ koldaki sıvı düzeyi yükselir.\nIII. Denge kurulduğunda iki koldaki glikoz derişimleri eşit olur.\nBuna göre yukarıdaki yargılardan hangileri yanlıştır?',
 dogru=dg,yan=yn,sira=S5b,istenen='Yanlış olan öncüller.',
 ip=['Zardan yalnız çözücünün geçtiğini göz önüne alıp suyun hangi yöne ve neden geçtiğini düşün.'],bilgi=[B_O],ad=ad,
 puf='Zardan geçebilen ve geçemeyen maddeyi ayırt edip net akışın yönünü belirle.',sekil=sk)
# ================= 14 · orta · karıştırma + buharlaştırma =================
a_,pa,b_,pb,bf=F(200),F(10),F(100),F(40),F(100)
cs=a_*pa/100+b_*pb/100; ct=a_+b_; p14=cs/(ct-bf)*100
assert (cs,ct,p14)==(60,300,30)
d_a=cs/ct*100; d_b=(pa+pb)/2; d_c=cs/(ct+bf)*100; d_d=pa
assert (d_a,d_b,d_c)==(20,25,15) and len({p14,d_a,d_b,d_c,d_d})==5
sk=fig(bk(0,0,1.5,1.7,1.3,'200 g','kütlece \\%10'),'\\node at (2.0,.8) {\\Large $+$};',bk(2.5,0,1.5,1.7,.9,'100 g','kütlece \\%40'),'\\draw[->,thick] (4.4,.8) -- (5.1,.8);',
 bk(5.5,0,1.5,1.7,1.4,'Karışım',''),'\\draw[->,thick] (7.3,.8) -- (8.0,.8) node[above,midway,font=\\footnotesize] {};',
 '\\node[align=center] at (9.0,.9) {100 g su\\\\buharlaştırılır};')
q('0014',tipId='cozelti-seyreltme',tip='Seyreltme, buharlaştırma ve karıştırma',z='orta',alt='Derişim Birimleri',kaz='İki çözeltinin karışımından su buharlaştırıldığında kütlece yüzdeyi hesaplar.',
 kart='K-AKCOZ-05 (seyreltme ve buharlaştırma) · %10 ve %40 çözeltiler',kalip='şekilli',
 metin='Şekilde, belirli bir sıcaklıkta aynı maddenin kütlece %10’luk 200 g ve kütlece %40’lık 100 g sulu çözeltileri karıştırılıyor; ardından oluşan karışımdan aynı sıcaklıkta 100 g su buharlaştırılıyor.\nBuna göre son çözeltinin kütlece yüzdesi kaçtır?',
 dogru=p14,yan=[(d_a,'Buharlaştırmayı hesaba katmamış: 60 ÷ 300 = %20.','dikkat'),(d_b,'Yüzdelerin aritmetik ortalamasını almış: (10 + 40) ÷ 2 = 25.','bilgi'),(d_c,'Buharlaşan suyu çözeltiye eklemiş: 60 ÷ 400 = %15.','islem'),(d_d,'Yalnız 200 g’lık çözeltinin yüzdesini yazmış: 10.','dikkat')],
 istenen='Son çözeltideki kütlece yüzde.',ip=['Çözünen kütlelerini toplayıp, buharlaşan su kadar azalan çözelti kütlesine oranlamayı dene.'],bilgi=[B_S],
 ad=[A('Çözünen kütleleri','Her çözeltideki çözünen ayrı hesaplanır.','200 × 0,10 = 20 g, 100 × 0,40 = 40 g'),A('Karışım','Çözünen ve çözelti kütleleri toplanır.','Çözünen 60 g, çözelti 300 g'),A('Buharlaştırma','Su gidince çözünen aynı kalır, çözelti kütlesi azalır.','300 − 100 = 200 g çözelti'),A('Yüzde','Çözünenin çözeltiye oranı yüzdeyle yazılır.','60 ÷ 200 × 100 = %30')],
 puf='Buharlaşan su yalnız çözelti kütlesini azaltır; çözünen kütlesi sabit kalır.',sekil=sk)
# ================= 15 · zor · M → molalite → kaynama noktası =================
M15=F(2); d15=F('1.08'); mNaOH=F(40); Vl=F(1000)
msol=d15*Vl; mn=M15*mNaOH; msu=msol-mn; mol15=M15/(msu/1000); Kk=F('0.52'); ik=2
Tb=100+Kk*ik*mol15
assert (msol,mn,msu,mol15,Tb)==(1080,80,1000,2,F('102.08'))
d_a=100+Kk*mol15; d_b=100+Kk*3*mol15; d_c=100-Kk*ik*mol15; d_d=Kk*ik*mol15
assert (d_a,d_b,d_c,d_d)==(F('101.04'),F('103.12'),F('97.92'),F('2.08')) and len({Tb,d_a,d_b,d_c,d_d})==5
sk=fig('\\draw[thick] (-.35,2.9) -- (-.35,3.2) -- (.35,3.2) -- (.35,2.9);','\\draw[thick,fill=vurgu!10] (-1.5,0) rectangle (1.5,2.9);','\\draw[thick,fill=white] (-1.3,.4) rectangle (1.3,2.3);',
 '\\node at (0,1.85) {\\textbf{NaOH çözeltisi}};','\\node at (0,1.35) {2 M};','\\node at (0,.85) {$d=1{,}08$ g/mL};')
q('0015',tipId='cozelti-koligatif-hesap',tip='Koligatif özelliklerle hesaplama',z='zor',alt='Koligatif Özellikler',kaz='Molarite ve yoğunluktan molaliteyi bulup kaynama noktasını hesaplar.',
 kart='K-AKCOZ-13 (derişim dönüşümü ve kaynama noktası) · 2 M NaOH, d = 1,08',kalip='şekilli',
 metin='Şekildeki şişenin etiketinde NaOH sulu çözeltisinin molaritesi ve yoğunluğu verilmiştir.\nBuna göre bu çözelti 1 atm basınçta kaç °C’de kaynamaya başlar? (NaOH = 40 g/mol; suyun molal kaynama noktası yükselmesi sabiti Kk = 0,52 °C/m; saf suyun kaynama noktası 100 °C; NaOH’nin suda tamamen iyonlarına ayrışarak çözündüğü varsayılacaktır.)',
 dogru=Tb,yan=[(d_a,'NaOH’nin iyonlaştığını göz ardı etmiş (i = 1): 100 + 0,52 × 2 = 101,04.','bilgi'),(d_b,'Tanecik sayısını 3 almış: 100 + 0,52 × 3 × 2 = 103,12.','dikkat'),(d_c,'Kaynama noktasını yükselme yerine alçalma saymış: 100 − 2,08 = 97,92.','dikkat'),(d_d,'Yalnız yükselme miktarını sıcaklık olarak yazmış: 2,08.','islem')],
 istenen='Çözeltinin kaynamaya başladığı sıcaklık (°C).',ip=['Önce 1 L çözeltiden çözücü kütlesini bulup molaliteye geç, sonra tanecik sayısını hesaba kat.'],bilgi=[B_M,B_KOL],
 ad=[A('1 L çözeltinin kütlesi','Yoğunluk kullanılır.','1000 × 1,08 = 1080 g'),A('NaOH kütlesi','2 mol NaOH bulunur.','2 × 40 = 80 g'),A('Çözücü kütlesi','Çözeltiden çözünen çıkarılır.','1080 − 80 = 1000 g = 1 kg'),A('Molalite','Mol sayısı çözücü kütlesine bölünür.','m = 2 ÷ 1 = 2 molal'),A('Kaynama noktası yükselmesi','NaOH, Na⁺ ve OH⁻ olmak üzere 2 iyon verir.','ΔT = 2 × 0,52 × 2 = 2,08 °C'),A('Sonuç','Yükselme saf suyun kaynama noktasına eklenir.','100 + 2,08 = 102,08 °C')],
 puf='Molariteden molaliteye geçerken 1 L çözeltinin kütlesinden çözünen kütlesini çıkar; iyonlaşan maddede i ile çarp.',sekil=sk)
# ================= 16 · zor · iki tuz + su ekleme =================
Va,Ma,Vb,Mb,Vsu=F('0.1'),F('0.4'),F('0.2'),F('0.3'),F('0.3')
no3=Ma*3*Va+Mb*2*Vb; Vt=Va+Vb+Vsu; M16=no3/Vt
assert (no3,Vt,M16)==(F('0.24'),F('0.6'),F('0.4'))
d_a=no3/(Va+Vb); d_b=no3/1; d_c=Ma*3*Va/Vt; d_d=(Ma*3*Va+Mb*3*Vb)/Vt
assert (d_a,d_b,d_c,d_d)==(F('0.8'),F('0.24'),F('0.2'),F('0.5')) and len({M16,d_a,d_b,d_c,d_d})==5
sk=fig(bk(0,0,1.5,1.7,.9,'100 mL','0,4 M \\ce{Al(NO3)3}'),'\\node at (2.0,.8) {\\Large $+$};',bk(2.5,0,1.5,1.7,1.2,'200 mL','0,3 M \\ce{Ca(NO3)2}'),
 '\\node at (4.5,.8) {\\Large $+$};',bk(5.0,0,1.3,1.7,1.0,'300 mL','su','blue!12'),
 '\\draw[->,thick] (6.7,.8) -- (7.4,.8);',bk(7.8,0,1.5,1.7,1.5,'Son çözelti',''))
q('0016',tipId='cozelti-karisim-iyon',tip='Çözeltileri karıştırma ve iyon derişimi',z='zor',alt='Derişim Birimleri',kaz='İki tuz çözeltisi karıştırılıp seyreltildiğinde iyon derişimini hesaplar.',
 kart='K-AKCOZ-04 (iyon derişimi ve karıştırma) · Al(NO₃)₃, Ca(NO₃)₂ ve su',kalip='şekilli',
 metin='Sıcaklıkları aynı olan şekildeki Al(NO₃)₃ ve Ca(NO₃)₂ sulu çözeltileri karıştırılıyor, ardından karışıma 300 mL su ekleniyor.\nBuna göre son çözeltideki NO₃⁻ iyonunun derişimi kaç molardır? (Tuzların suda tamamen iyonlarına ayrışarak çözündüğü ve hacimlerin toplanabildiği varsayılacaktır.)',
 dogru=M16,yan=[(d_a,'Eklenen suyun hacmini toplam hacme katmamış: 0,24 ÷ 0,3 = 0,8.','dikkat'),(d_b,'Toplam mol sayısını hacme bölmemiş: 0,24 mol ÷ 1 L = 0,24.','islem'),(d_c,'Yalnız Al(NO₃)₃’ten gelen nitratı saymış: 0,12 ÷ 0,6 = 0,2.','bilgi'),(d_d,'Ca(NO₃)₂ için nitrat sayısını 3 almış: (0,12 + 0,18) ÷ 0,6 = 0,5.','dikkat')],
 istenen='Son çözeltideki NO₃⁻ derişimi (M).',ip=['Her tuzdan gelen nitrat mol sayısını ayrı bulup, suyun da katıldığı toplam hacme oranlamayı dene.'],bilgi=[B_I,B_K],
 ad=[A('Al(NO₃)₃ çözeltisi','Formülde 3 nitrat vardır.','0,4 × 3 × 0,1 = 0,12 mol'),A('Ca(NO₃)₂ çözeltisi','Formülde 2 nitrat vardır.','0,3 × 2 × 0,2 = 0,12 mol'),A('Toplam mol','Nitrat mol sayıları toplanır.','0,12 + 0,12 = 0,24 mol'),A('Toplam hacim','Su da hacme katılır.','100 + 200 + 300 = 600 mL'),A('Derişim','Mol sayısı toplam hacme bölünür.','0,24 ÷ 0,6 = 0,4 M')],
 puf='Su eklemek mol sayısını değiştirmez, yalnız toplam hacmi artırır; iyon katsayıları mol sayısına çarpılır.',sekil=sk)
# ================= 17 · zor · tablo, i × m (öncüllü) =================
def tab(bas,sat):
    return tablo_svg(bas,sat)
dat=[('X','C₆H₁₂O₆',F(18),F(180),F(500),1),('Y','NaCl',F('5.85'),F('58.5'),F(250),2),('Z','CaCl₂',F('11.1'),F(111),F(500),3)]
im={a[0]:(a[2]/a[3])/(a[4]/1000)*a[5] for a in dat}
assert im=={'X':F('0.2'),'Y':F('0.8'),'Z':F('0.6')}
sk=tab(['Çözelti','Çözünen','Çözünenin kütlesi (g)','Su kütlesi (g)'],[[a[0],a[1],fm(a[2]),fm(a[4])] for a in dat])
truth={'I':False,'II':True,'III':True}
reasons={'I':'i × m değerleri X: 0,2, Z: 0,6 ve Y: 0,8 olduğundan kaynama noktaları Y > Z > X sırasındadır; Z > Y > X sırası yanlıştır',
 'II':'i × m değeri büyük olan çözeltinin buhar basıncı daha çok düşer; 25 °C’de buhar basınçları X > Z > Y sırasındadır',
 'III':'i × m değeri en büyük olan Y’nin donma noktası en düşüktür; Z’ninki Y’den yüksektir'}
dg,yn,ad=onc(truth,reasons,S5)
q('0017',tipId='cozelti-koligatif-yorum',tip='Koligatif özelliklerin yorumlanması',z='zor',alt='Koligatif Özellikler',kaz='Kütle verilerinden i × m değerlerini bulup koligatif özellikleri karşılaştırır.',
 kart='K-AKCOZ-07 (koligatif yorum) · glikoz, NaCl, CaCl₂ tablosu',kalip='öncüllü',
 metin='Tabloda, uçucu olmayan üç maddenin suda çözünmesiyle hazırlanan X, Y ve Z çözeltilerine ait veriler verilmiştir. Çözeltilerin tamamı aynı sıcaklıktadır ve NaCl ile CaCl₂ suda tamamen iyonlarına ayrışmıştır.\nI. 1 atm basınçta kaynamaya başlama sıcaklıkları Z > Y > X sırasındadır.\nII. 25 °C’de buhar basınçları X > Z > Y sırasındadır.\nIII. Donmaya başlama sıcaklığı en düşük olan çözelti Y’dir.\nBuna göre yukarıdaki yargılardan hangileri doğrudur? (C₆H₁₂O₆ = 180 g/mol, NaCl = 58,5 g/mol, CaCl₂ = 111 g/mol)',
 dogru=dg,yan=yn,sira=S5,istenen='Doğru olan öncüller.',
 ip=['Her çözelti için önce molaliteyi, sonra tanecik sayısını katarak i × m değerini hesaplamayı dene.'],bilgi=[B_KOL,B_KY],ad=ad,
 puf='Sıralamada yalnız kütleye ya da yalnız mol sayısına bakma; i × m değerini hesapla.',sekil=sk)
# ================= 18 · zor · çözünürlük tablosu, su ekleme + soğutma =================
S20,S60=F(40),F(90); mc=F(380); su60=mc*100/(100+S60); x60=mc-su60; su2=su60+100; kal=su2/100*S20; c18=x60-kal
assert (su60,x60,su2,kal,c18)==(200,180,300,120,60)
d_a=x60-su60/100*S20; d_b=S60; d_c=x60; d_d=kal
assert (d_a,d_b,d_c,d_d)==(100,90,180,120) and len({c18,d_a,d_b,d_c,d_d})==5
sk=tab(['Sıcaklık (°C)','Çözünürlük (g X/100 g su)'],[['20','40'],['60','90']])
q('0018',tipId='cozelti-cozunurluk-hesap',tip='Çözünürlük hesapları',z='zor',alt='Çözünürlük',kaz='Su eklenip soğutulan doygun çözeltide çöken madde miktarını hesaplar.',
 kart='K-AKCOZ-09 (çözünürlük ve çökelme) · X katısı, 380 g, su ekleme',kalip='tablo',
 metin='X katısının sudaki çözünürlüğü, tabloda verilen sıcaklıklarda gösterilmiştir.\n60 °C’de hazırlanan 380 g doygun X sulu çözeltisine 100 g su ekleniyor ve çözelti 20 °C’a soğutuluyor.\nBuna göre bu işlemde dibe çöken X katısı kaç gramdır?',
 dogru=c18,yan=[(d_a,'Eklenen suyu hesaba katmamış: 180 − 200 ÷ 100 × 40 = 100.','dikkat'),(d_b,'60 °C’deki çözünürlük değerini çöken miktar saymış: 90.','bilgi'),(d_c,'Çözeltideki tüm X’in çöktüğünü sanmış: 380 × 90 ÷ 190 = 180.','dikkat'),(d_d,'Soğutmada çözeltide kalan X miktarını çöken saymış: 300 ÷ 100 × 40 = 120.','islem')],
 istenen='Çöken X katısının kütlesi (g).',ip=['Önce ilk durumdaki çözeltinin su ve X kütlesini bulup, son durumdaki su kütlesine göre çözünebilen X’i hesaplamayı dene.'],bilgi=[B_C],
 ad=[A('60 °C’de bileşim','100 g suya 90 g X çözünür; çözelti 190 g olur. 380 g çözelti için oranla.','Su = 200 g, X = 180 g'),A('Su eklenince','Çözücü kütlesi artar.','200 + 100 = 300 g su'),A('20 °C’de çözünebilen','300 g su, 20 °C’de 40 × 3 kadar X çözer.','120 g X çözeltide kalır'),A('Çöken','Eldeki X’ten kalan çıkarılır.','180 − 120 = 60 g')],
 puf='Çözünürlük 100 g su içindir; su eklenmişse son su kütlesiyle oranla ve çözünen kütlesinin değişmediğini unutma.',sekil=sk)
# ================= 19 · zor · iki tuzun ayrılması =================
SXf=lambda T: T+10; SY=lambda T: F(40)+F(T-20)/3
xm,ym=F(70),F(36); assert SXf(80)==90 and SY(80)==60 and SXf(20)==30 and SY(20)==40
assert xm<=SXf(80) and ym<=SY(80) and ym<=SY(20) and xm>SXf(20)
cok19=xm-SXf(20); assert cok19==40
d_a=ym; d_b=xm; d_c=xm+ym; d_d=SXf(80)-SXf(20)
assert d_d==60 and len({cok19,d_a,d_b,d_c,d_d})==5
sk=fig(*cgraf([('X',[(0,10),(100,110)],'vurgu!70!black',(95,103)),('Y',[(0,F(100,3).__float__() +0),(20,40),(80,60),(100,F(200,3))],'orange!80!black',(92,76))],[20,80],[30,40,60,90],ymax=115))
q('0019',tipId='cozelti-cozunurluk-hesap',tip='Çözünürlük hesapları',z='orta',alt='Çözünürlük',kaz='Çözünürlük eğrilerinden iki katının soğutmayla ayrılmasını yorumlar.',
 kart='K-AKCOZ-09 (çözünürlük ve çökelme) · X ve Y katılarının karışımı',kalip='grafik',
 metin='X ve Y katılarının sudaki çözünürlüklerinin sıcaklıkla değişimi şekildeki grafikte verilmiştir.\n70 g X ve 36 g Y katıları karışımı 80 °C’de 100 g suda tamamen çözülüyor. Sonra çözelti 20 °C’a soğutuluyor.\nBuna göre dibe çöken katı kaç gramdır? (X ve Y birbirinin çözünürlüğünü etkilemez.)',
 dogru=cok19,yan=[(d_a,'Çöken katıyı Y sanmış: 36.','bilgi'),(d_b,'Soğutmada X’in tamamının çöktüğünü sanmış: 70.','dikkat'),(d_c,'Her iki katının da tamamının çöktüğünü sanmış: 70 + 36 = 106.','dikkat'),(d_d,'X’in 80 °C ve 20 °C’deki çözünürlük farkını çöken saymış: 90 − 30 = 60.','dikkat')],
 istenen='Çöken katının kütlesi (g).',ip=['Her katı için 20 °C’de 100 g suda çözünebilen en çok miktarı, eldeki miktarla ayrı ayrı karşılaştırmayı dene.'],bilgi=[B_C],
 ad=[A('Grafikten oku','20 °C’de 100 g su en çok 30 g X ve 40 g Y çözer.','S(X) = 30, S(Y) = 40'),A('X için karşılaştır','Eldeki 70 g X, çözünebilen 30 g’dan fazladır.','Fazlası çöker'),A('Y için karşılaştır','Eldeki 36 g Y, çözünebilen 40 g’dan azdır.','Y çökmez'),A('Çöken','Yalnız X çöker.','70 − 30 = 40 g')],
 puf='Her katıyı kendi çözünürlüğüyle karşılaştır; eldeki miktar çözünürlükten büyükse fazlası çöker.',sekil=sk)
# ================= 20 · zor · soğutma eğrisi, molar kütle =================
dT20=F('3.72'); Kd=F('1.86'); mol20=dT20/Kd; nn=mol20*F('0.25'); Mmol=F(40)/nn
assert (mol20,nn,Mmol)==(2,F('0.5'),80)
d_a=F(40)/(mol20*1); d_b=F(40)/((Kd/dT20)*F('0.25')); d_c=F(40)/((dT20/Kd/2)*F('0.25')); d_d=F(40)/(mol20*F('2.5'))
assert d_a==20 and d_b==320 and d_c==160 and d_d==8 and len({Mmol,d_a,d_b,d_c,d_d})==5
sk=fig('\\draw[->,thick] (0,0) -- (6.4,0) node[below left] {Zaman}; \\draw[->,thick] (0,0) -- (0,4.4) node[above] {Sıcaklık ($^\\circ$C)};',
 '\\draw (-.08,3.3) -- (.08,3.3); \\node[left] at (0,3.3) {0}; \\draw (-.08,1.6) -- (.08,1.6); \\node[left] at (0,1.6) {$-3{,}72$};',
 '\\draw[thick,vurgu!70!black] (0,4.0) -- (1.4,3.3) -- (3.6,3.3) -- (4.2,.5) -- (5.8,.2); \\node[font=\\small\\bfseries] at (2.5,3.65) {Saf su};',
 '\\draw[thick,orange!80!black,dashed] (0,4.0) -- (1.9,1.6) -- (3.8,1.2) -- (5.8,.5); \\node[font=\\small\\bfseries] at (5.1,1.15) {Çözelti};',
 '\\draw[dotted,gray] (1.9,1.6) -- (0,1.6);')
q('0020',tipId='cozelti-koligatif-hesap',tip='Koligatif özelliklerle hesaplama',z='zor',alt='Koligatif Özellikler',kaz='Soğuma eğrisinden donma noktası alçalmasını okuyup molar kütleyi hesaplar.',
 kart='K-AKCOZ-12 (molar kütle ve koligatif özellik) · 40 g X, 250 g su',kalip='grafik',
 metin='Saf su ile 250 g suda 40 g X maddesinin çözünmesiyle hazırlanan çözeltinin soğuma eğrileri şekilde verilmiştir. X, uçucu olmayan ve suda moleküler olarak çözünen bir maddedir.\nBuna göre X’in molar kütlesi kaç g/mol’dür? (Suyun molal donma noktası alçalması sabiti Kd = 1,86 °C/m)',
 dogru=Mmol,yan=[(d_a,'Çözücüyü 1 kg almış: n = 2 mol, M = 40 ÷ 2 = 20.','dikkat'),(d_b,'Oranı ters almış: m = 1,86 ÷ 3,72 = 0,5, n = 0,125 ve M = 40 ÷ 0,125 = 320.','islem'),(d_c,'X’i iyonlaşıyor saymış (i = 2): m = 1, n = 0,25 ve M = 160.','bilgi'),(d_d,'250 g suyu 2,5 kg almış: n = 5 mol, M = 8.','dikkat')],
 istenen='X’in molar kütlesi (g/mol).',ip=['Eğriden çözeltinin donma noktası alçalmasını okuyup önce molaliteye, sonra mol sayısına geçmeyi dene.'],bilgi=[B_KOL,B_M],
 ad=[A('Alçalmayı oku','Saf su 0 °C’de, çözelti −3,72 °C’de donmaya başlar.','ΔT = 3,72 °C'),A('Molalite','Moleküler çözünende i = 1’dir; ΔT = Kd × m.','m = 3,72 ÷ 1,86 = 2 molal'),A('Mol sayısı','Molalite çözücü kütlesiyle (0,25 kg) çarpılır.','n = 2 × 0,25 = 0,5 mol'),A('Molar kütle','Kütle mol sayısına bölünür.','M = 40 ÷ 0,5 = 80 g/mol')],
 puf='Donma noktası alçalmasından molalite, molaliteden mol sayısı, oradan da molar kütle bulunur; çözücü kütlesini kg’a çevir.',sekil=sk)
# ================= yaz =================
assert len(P.ANA)==20,len(P.ANA)
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(GD,'cozelti-1.json'),'/tmp/bos-cozelti.json')
tipler={}
for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 12. sınıf kimya müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akcozelti.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'kart',len(KARTLAR))
