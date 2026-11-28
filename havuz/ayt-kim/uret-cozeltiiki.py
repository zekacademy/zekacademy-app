"""AYT Kimya · Sıvı Çözeltiler · 2. dalga · 10 soru (ipucu 1). Şekiller TikZ; her sayı Python'da Fraction ile hesaplanıp assert edilir."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
KONUAD='Sıvı Çözeltiler'
UK='akim|'+KONUAD
P=Parti('cozeltiiki',KONUAD,UK,ders='AYT Kimya',idon='aytkim')
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
# ---- bilgi kutuları (örnekler soruların sayılarından farklı)
B_SEY=B('Seyreltme','Saf su eklenince çözünenin mol sayısı ve kütlesi değişmez; çözücü miktarı, toplam hacim ve çözelti kütlesi artar, derişim azalır. M₁V₁ = M₂V₂. Örnek: 1 M’lık 50 mL çözelti 250 mL’ye tamamlanırsa derişim 0,2 M olur')
B_GAZ=B('Gazların çözünürlüğü','Gazların sudaki çözünürlüğü sabit sıcaklıkta basınçla doğru orantılı artar (Henry yasası); sıcaklık arttıkça azalır. Örnek: gazlı içecek şişesi açılınca basınç düşer ve gaz çıkar')
B_PPM=B('ppm derişimi','1 ppm, 10⁶ g çözeltide 1 g çözünen demektir. Seyreltik sulu çözeltilerde yoğunluk 1 g/mL alınırsa 1 ppm = 1 mg/L olur. Örnek: 46 ppm Na⁺ içeren suda Na⁺ derişimi 46 mg/L, yani 2 mmol/L’dir (Na = 23 g/mol)')
B_OZ=B('Ozmos yönü','Yalnız çözücüyü geçiren zarda net su geçişi, çözünen taneciklerin toplam derişiminin (i × M) küçük olduğu taraftan büyük olduğu tarafa doğrudur; değerler eşitse net geçiş olmaz. Örnek: 0,5 M üre çözeltisi ile 0,1 M KBr çözeltisi (0,2) arasında su, üreli tarafa geçer')
B_YOR=B('Çözünürlük eğrisi','Eğri üzerindeki noktalar doygun, eğrinin altındaki noktalar doymamış çözeltiyi gösterir. Doymamış çözeltide aynı sıcaklıkta eğri değeri ile nokta arasındaki fark kadar daha madde çözünebilir. Örnek: 50 °C’de eğri 40, nokta 25 ise 100 g suya 15 g daha çözünür')
B_BUH=B('Buharlaştırma ve çökelme','Doygun çözeltiden su buharlaşırsa o suda çözünmüş olan madde çöker. Sabit sıcaklıkta çöken ek madde = buharlaşan su kütlesi × (çözünürlük ÷ 100). Örnek: çözünürlüğü 30 g/100 g su olan bir çözeltiden 20 g su buharlaşırsa 6 g madde çöker')
B_I=B('Tuzların iyon derişimi','Suda tamamen iyonlaşan bir tuzda iyon derişimi, tuz derişimi ile formüldeki iyon sayısının çarpımıdır. Örnek: 0,3 M MgCl₂ çözeltisinde [Mg²⁺] = 0,3 M, [Cl⁻] = 0,6 M olur')
B_C=B('Çözünürlük ve doygunluk','Çözünürlük, belirli sıcaklıkta 100 g suda çözünebilen en çok madde kütlesidir. Doygun çözeltide çözünen/çözücü oranı çözünürlüğe eşittir. Örnek: çözünürlüğü 20 g/100 g su olan tuzun doygun çözeltisinin kütlece yüzdesi 20/120 oranından bulunur')
B_K=B('Çözeltileri karıştırma','Karışımda her çözünenin mol sayısı toplanır; yeni derişim toplam mol ÷ toplam hacimdir. Reaksiyon vermeyen iyonların mol sayısı korunur. Örnek: 0,2 M 100 mL ile 0,4 M 300 mL çözelti karışınca toplam mol 0,14, hacim 0,4 L olur')
B_M=B('Molalite','Molalite, 1 kg çözücüde çözünen maddenin mol sayısıdır: m = n(çözünen) ÷ kg çözücü. Sıcaklıkla değişmez. Örnek: 1 mol şeker 500 g suda çözünürse 2 molal olur')
B_KOL=B('Koligatif özellikler','Uçucu olmayan çözünenin çözücüdeki tanecik sayısına bağlı özellikleri: buhar basıncı düşer, kaynama noktası yükselir, donma noktası düşer, ozmotik basınç artar. ΔT = i · K · m; i, çözünenin suda oluşturduğu tanecik sayısıdır. Örnek: 1 molal şeker çözeltisinde i = 1, 1 molal KBr çözeltisinde i = 2 alınır')
B_EN=B('Çözünme entalpisi','Çözünme iki basamaklıdır: kristal kafesin dağılması (endotermik, +) ve iyonların hidratasyonu (egzotermik, −). ΔH(çözünme) = ΔH(kafes) + ΔH(hidratasyon). Örnek: +700 kJ/mol ve −650 kJ/mol ise ΔH = +50 kJ/mol olur')
B_KAL=B('Çözünme ısısı ve sıcaklık değişimi','Çözünürken alınan ya da verilen ısı q = n × ΔH(çözünme) ile bulunur. Isı alan (endotermik) çözünmede çözelti soğur: q = m × c × ΔT. Örnek: 0,1 mol madde ΔH = +10 kJ/mol ile 100 g suda çözünürse q = 1 kJ’dür')
# ================= KARTLAR =================
kartla('K-AKCOZ2-01','Seyreltme','Su eklemek çözünenin mol sayısını değiştirmez; derişim ve yoğunluk azalırken hacim ve çözücü miktarı artar.','Çözücünün de sabit kaldığını sanmak; derişimin hacimle doğru orantılı değiştiğini düşünmek.','kolay','öncüllü',3,'cozeltiiki-derisim','Derişim birimleri ve dönüşümleri')
kartla('K-AKCOZ2-02','Gazların çözünürlüğü','Gaz çözünürlüğü basınç ve sıcaklıkla değişir; iki eğri aynı basınçta karşılaştırılarak yorum yapılır.','Katılardaki sıcaklık eğilimini gazlara uygulamak.','kolay','grafik',2,'cozeltiiki-cozunurluk','Çözünürlük ve çözünürlüğü etkileyen faktörler')
kartla('K-AKCOZ2-03','ppm derişimi','ppm kütlece oranı verir; seyreltik suda mg/L’ye eşit alınır, mol/L’ye mol kütlesiyle, yük derişimine iyon yüküyle geçilir.','Birimleri (mg ve g) karıştırmak; iyon yükünü hesaba katmamak.','orta','tablo',3,'cozeltiiki-derisim','Derişim birimleri ve dönüşümleri')
kartla('K-AKCOZ2-04','Ozmos yönü','Net su geçişi, toplam çözünen tanecik derişimi (i × M) küçük olan taraftan büyük olan tarafa doğrudur; eşitse geçiş olmaz.','Yalnız mol/L değerine bakıp iyonlaşmayı unutmak.','orta','şekilli',3,'cozeltiiki-koligatif-yorum','Koligatif özelliklerin yorumlanması')
kartla('K-AKCOZ2-05','Çözünürlük eğrisi üzerindeki noktalar','Eğri üstündeki nokta doygun, altındaki doymamış çözeltidir; yüzde ve çökelme için su kütlesi esas alınır.','Doymamış noktayı doygun saymak; 100 g su yerine çözelti kütlesiyle işlem yapmak.','orta','grafik',3,'cozeltiiki-cozunurluk','Çözünürlük ve çözünürlüğü etkileyen faktörler')
kartla('K-AKCOZ2-06','Kaynama noktası yükselmesi grafiği','ΔT–molalite doğrusunun eğimi i × K değerini verir; moleküler çözünenin eğimi K’dır, iyonik tuzun eğimi bunun i katıdır.','Eğimi molalite sanmak; tanecik sayısını hesaba katmamak.','orta','grafik',3,'cozeltiiki-koligatif-yorum','Koligatif özelliklerin yorumlanması')
kartla('K-AKCOZ2-07','Karıştırma ve buharlaştırma','Her iyonun mol sayısı ayrı bulunup toplanır; buharlaşma mol sayısını değiştirmez, yalnız son hacmi küçültür.','Buharlaşan hacmi mol sayısından düşmek; iyon katsayısını atlamak.','orta','şekilli',4,'cozeltiiki-karisim','Çözeltileri karıştırma ve iyon derişimi')
kartla('K-AKCOZ2-08','Eş donma noktası','Donma noktaları eşit olan çözeltilerde i × m değerleri eşittir; molaliteden mol sayısı ve kütle bulunur.','İyon sayısını atlamak; başka kaptaki çözücü kütlesini kullanmak.','zor','şekilli',4,'cozeltiiki-koligatif-hesap','Koligatif özelliklerle hesaplama')
kartla('K-AKCOZ2-09','Soğutma ve buharlaştırmayla çökelme','Doygun çözeltide su ve çözünen kütlesi çözünürlükle ayrılır; her işlemde çözünebilen miktar yeni su kütlesine göre bulunur.','Buharlaşan suyu 100 g suya göre almak; yanlış sıcaklığın çözünürlüğünü kullanmak.','zor','tablo',5,'cozeltiiki-cozunurluk','Çözünürlük ve çözünürlüğü etkileyen faktörler')
kartla('K-AKCOZ2-10','Çözünme ısısı ve kalorimetre','Kafes ve hidratasyon entalpileri toplanarak ΔH(çözünme) bulunur; endotermik çözünmede alınan ısı sudan çekilir ve sıcaklık düşer.','Işaret hatası yapmak; mol sayısını kullanmadan ısıyı mol başına almak.','zor','şekilli',5,'cozeltiiki-cozunme-enerji','Çözünme sürecinde enerji')
def bk(x,y,w,h,lvl,l1,l2,fill='vurgu!15'):
    return (f'\\fill[{fill}] ({x},{y}) rectangle ({x+w},{y+lvl}); \\draw[thick] ({x},{y+h}) -- ({x},{y}) -- ({x+w},{y}) -- ({x+w},{y+h});'
            f'\\node[below,align=center] at ({x+w/2},{y-.05}) {{{l1}\\\\{l2}}};')
def kgraf(egriler,xt,yt,xl,yl,xmax,ymax,sx,sy,noktalar=(),extra=''):
    p=[f'\\draw[->,thick] (0,0) -- ({xmax*sx+.3:.2f},0) node[anchor=north east,yshift=-14pt] {{{xl}}};',f'\\draw[->,thick] (0,0) -- (0,{ymax*sy+.3:.2f}) node[above] {{{yl}}};']
    for t in xt: p.append(f'\\draw[gray!40] ({t*sx:.2f},0) -- ({t*sx:.2f},{ymax*sy:.2f}); \\node[below] at ({t*sx:.2f},0) {{{fm(F(t)) if not isinstance(t,int) else t}}};')
    for v in yt: p.append(f'\\draw[gray!40] (0,{v*sy:.2f}) -- ({xmax*sx:.2f},{v*sy:.2f}); \\node[left] at (0,{v*sy:.2f}) {{{fm(F(v)) if not isinstance(v,int) else v}}};')
    for nm,pts,stil,lab in egriler:
        cs=' '.join(f'({a*sx:.2f},{b*sy:.2f})' for a,b in pts)
        p.append(f'\\draw[thick,{stil}] plot coordinates {{{cs}}};')
        a,b=lab; p.append(f'\\node[font=\\small\\bfseries] at ({a*sx:.2f},{b*sy:.2f}) {{{nm}}};')
    for nm,a,b,dx,dy in noktalar:
        p.append(f'\\fill[red!70!black] ({a*sx:.2f},{b*sy:.2f}) circle (.07); \\node[font=\\small\\bfseries] at ({a*sx+dx:.2f},{b*sy+dy:.2f}) {{{nm}}};')
    return p+[extra]
def tek(sec,hedef=True,tur='bilgi'):
    assert len(sec)==5; h=[x for x in sec if x[1]==hedef]; assert len(h)==1
    yan=[(m,f'Bu ifadeyi yanlış sanmış; oysa doğrudur, çünkü {n}.',tur) for m,b,n in sec if b!=hedef]
    return dict(dogru=h[0][0],yan=yan,sira=[x[0] for x in sec])
# ================= 01 · kolay · seyreltme (öncüllü) =================
V0,M0,Vsu=F('0.2'),F('0.5'),F('0.3'); n0=V0*M0; M01=n0/(V0+Vsu)
assert (n0,M01)==(F('0.1'),F('0.2'))
truth={'I':True,'II':False,'III':False}
reasons={'I':'su eklemek çözünenin mol sayısını değiştirmez, yalnız hacmi artırır','II':'eklenen su çözücü miktarını artırır; su molekülü sayısı değişmez denemez','III':'Na⁺ mol sayısı 0,1 mol ve son hacim 0,5 L olduğundan derişim 0,1 ÷ 0,5 = 0,2 M olur, 0,5 M değildir'}
dg,yn,ad=onc(truth,reasons,['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'])
sk=fig(bk(0,0,1.5,2.4,.8,'200 mL','0,5 M \\ce{NaCl}'),'\\node at (2.1,.8) {\\Large $+$};',bk(2.6,0,1.5,2.4,1.2,'300 mL','saf su','blue!12'),
 '\\draw[->,thick] (4.5,.8) -- (5.2,.8);',bk(5.6,0,1.5,2.4,2.0,'Son çözelti','(500 mL)','vurgu!8'))
q('0001',tipId='cozeltiiki-derisim',tip='Derişim birimleri ve dönüşümleri',z='kolay',alt='Derişim Birimleri',kaz='Çözeltiye su eklendiğinde mol sayısı, hacim ve derişim değişimini yorumlar.',
 kart='K-AKCOZ2-01 (seyreltme) · NaCl çözeltisine su ekleme',kalip='öncüllü',
 metin='Şekilde, aynı sıcaklıkta bir NaCl sulu çözeltisine saf su ekleniyor ve çözelti karıştırılıyor. (Hacimlerin toplanabildiği ve NaCl’nin suda tamamen iyonlarına ayrışarak çözündüğü varsayılacaktır.)\nI. Çözeltideki NaCl’nin mol sayısı değişmez.\nII. Çözeltideki su molekülü sayısı değişmez.\nIII. Son çözeltide Na⁺ iyonlarının derişimi 0,5 M’dır.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=dg,yan=yn,sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],istenen='Doğru olan öncüller.',
 ip=['Su eklenince hangi niceliklerin sabit kaldığını, hangilerinin arttığını ayrı ayrı düşün.'],bilgi=[B_SEY,B_I],ad=ad,
 puf='Seyreltmede çözünen miktarı sabit kalır; değişen yalnız çözücü miktarı, hacim ve derişimdir.',sekil=sk)
# ================= 02 · kolay · gaz çözünürlüğü (olumsuz) =================
sk=fig(*kgraf([('$T_1$',[(0,0),(4,80)],'vurgu!70!black',(4.35,80)),('$T_2$',[(0,0),(4,40)],'orange!80!black',(4.35,40))],[1,2,3,4],[20,40,60,80],'Basınç (atm)','Çözünürlük (mg/L)',4,80,1.2,.04))
S=[('Gazın sudaki çözünmesi endotermiktir.',False,'çözünürlük düşük sıcaklıkta daha yüksek olduğundan çözünme ısı veren bir süreçtir'),
   ('T₂ sıcaklığı, T₁ sıcaklığından yüksektir.',True,'aynı basınçta T₂’deki çözünürlük daha düşüktür ve gazın çözünürlüğü sıcaklıkla azalır'),
   ('Sabit sıcaklıkta basınç artırılırsa gazın çözünürlüğü artar.',True,'her iki doğru da orijinden geçen artan doğrulardır'),
   ('T₁ sıcaklığında 4 atm’deki çözünürlük, 2 atm’dekinin iki katıdır.',True,'çözünürlük basınçla doğru orantılıdır: 80 mg/L, 40 mg/L’nin iki katıdır'),
   ('3 atm basınçta T₂ sıcaklığındaki çözünürlük, T₁ sıcaklığındakinden küçüktür.',True,'3 atm’de T₂ için 30 mg/L, T₁ için 60 mg/L okunur')]
r=tek(S,False)
q('0002',tipId='cozeltiiki-cozunurluk',tip='Çözünürlük ve çözünürlüğü etkileyen faktörler',z='kolay',alt='Çözünürlük',kaz='Gaz çözünürlüğünün basınç ve sıcaklıkla değişimini grafikten yorumlar.',
 kart='K-AKCOZ2-02 (gazların çözünürlüğü) · iki sıcaklıkta gaz çözünürlüğü',kalip='grafik',
 metin='Şekilde, bir gazın iki farklı sıcaklıktaki (T₁ ve T₂) sudaki çözünürlüğünün basınçla değişimi verilmiştir.\nBuna göre aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=['T₂ sıcaklığı, T₁ sıcaklığından yüksektir.','Sabit sıcaklıkta basınç artırılırsa gazın çözünürlüğü artar.','T₁ sıcaklığında 4 atm’deki çözünürlük, 2 atm’dekinin iki katıdır.','3 atm basınçta T₂ sıcaklığındaki çözünürlük, T₁ sıcaklığındakinden küçüktür.','Gazın sudaki çözünmesi endotermiktir.'],istenen='Yanlış olan yargı.',
 ip=['Aynı basınçta iki eğrinin değerlerini karşılaştırıp bu farkın sıcaklıkla ilişkisini düşün.'],bilgi=[B_GAZ],
 ad=[A('Eğrileri karşılaştır','Aynı basınçta T₁ eğrisi daha yüksek çözünürlük verir.','S(T₁) > S(T₂)'),A('Sıcaklığı yorumla','Gazın çözünürlüğü sıcaklık arttıkça azalır; çözünürlüğü küçük olan eğri yüksek sıcaklığa aittir.','T₂ > T₁'),A('Çözünme ısısını yorumla','Düşük sıcaklıkta çözünürlüğün artması çözünmenin ısı veren (egzotermik) olduğunu gösterir.','Egzotermik'),A('İfadeleri ele','Çözünmenin endotermik olduğunu söyleyen ifade yanlıştır.','Yanlış olan: endotermik')],
 puf='Eğrileri aynı basınçta karşılaştır; her ifadeyi grafikten okuduğun değerlerle sına.',sekil=sk)
# ================= 03 · orta · ppm tablo =================
ppm={'Ca':(F(80),F(40),2),'Mg':(F(24),F(24),2),'Na':(F(23),F(23),1)}
mmol={k:v[0]/v[1] for k,v in ppm.items()}; yuk=sum(mmol[k]*ppm[k][2] for k in ppm)
assert mmol=={'Ca':2,'Mg':1,'Na':1} and yuk==7
d_a=sum(mmol.values()); d_b=mmol['Ca']*2+mmol['Mg']*2; d_c=yuk/2; d_d=yuk*2
assert (d_a,d_b,d_c,d_d)==(4,6,F('3.5'),14) and len({yuk,d_a,d_b,d_c,d_d})==5
sk=tablo_svg(['Katyon','Derişim (ppm)'],[['Ca²⁺','80'],['Mg²⁺','24'],['Na⁺','23']])
q('0003',tipId='cozeltiiki-derisim',tip='Derişim birimleri ve dönüşümleri',z='orta',alt='Derişim Birimleri',kaz='ppm derişimini mmol/L’ye çevirip yük dengesinden anyon derişimini bulur.',
 kart='K-AKCOZ2-03 (ppm derişimi) · maden suyundaki katyonlar',kalip='tablo',
 metin='Tabloda, bir maden suyu örneğinde çözünmüş hâlde bulunan katyonların derişimleri ppm cinsinden verilmiştir. Çözeltideki tek anyon Cl⁻ iyonudur ve çözeltinin elektrikçe nötr olduğu bilinmektedir.\nBuna göre bu örnekte Cl⁻ iyonlarının derişimi kaç mmol/L’dir? (Ca = 40, Mg = 24, Na = 23 g/mol; çözeltinin yoğunluğu 1 g/mL ve 1 ppm = 1 mg/L alınacaktır.)',
 dogru=yuk,yan=[(d_a,'İyon yüklerini hesaba katmamış: 2 + 1 + 1 = 4.','dikkat'),(d_b,'Na⁺ iyonlarını saymayı unutmuş: 2 × 2 + 1 × 2 = 6.','bilgi'),(d_c,'Toplam yükü 2’ye bölmüş: 7 ÷ 2 = 3,5.','islem'),(d_d,'Cl⁻ iyonlarının sayısını yükle iki kez çarpmış: 7 × 2 = 14.','islem')],
 istenen='Cl⁻ iyonlarının derişimi (mmol/L).',ip=['Her katyonun mmol/L değerini ve taşıdığı toplam pozitif yükü bulup nötrlük koşuluyla ilişkilendirmeyi dene.'],bilgi=[B_PPM],
 ad=[A('mmol/L’ye çevir','1 ppm = 1 mg/L olduğundan mg değeri mol kütlesine bölünür.','Ca²⁺: 2, Mg²⁺: 1, Na⁺: 1 mmol/L'),A('Pozitif yükü bul','Her iyonun mmol/L değeri yüküyle çarpılır.','2·2 + 1·2 + 1·1 = 7 mmol/L'),A('Nötrlüğü kullan','Negatif yük toplamı pozitif yük toplamına eşittir; Cl⁻ yükü −1’dir.','[Cl⁻] = 7 mmol/L')],
 puf='ppm değeri mg/L sayılır, mol kütlesine bölünüp yükle çarpılır; elektrik nötrlüğü anyon derişimini verir.',sekil=sk)
# ================= 04 · orta · ozmos, üç düzenek (öncüllü) =================
sat=[('K','0,2 M \\ce{C6H12O6}',F('0.2')*1,'0,1 M \\ce{NaCl}',F('0.1')*2),('L','0,2 M \\ce{NaCl}',F('0.2')*2,'0,1 M \\ce{CaCl2}',F('0.1')*3),('M','0,3 M \\ce{C6H12O6}',F('0.3')*1,'0,1 M \\ce{Al(NO3)3}',F('0.1')*4)]
assert [(a[2],a[4]) for a in sat]==[(F('0.2'),F('0.2')),(F('0.4'),F('0.3')),(F('0.3'),F('0.4'))]
parts=[]
for i,(ad_,sl,a,sr,b) in enumerate(sat):
    y=-i*1.55
    parts.append(f'\\fill[vurgu!15] (0.7,{y}) rectangle (5.7,{y+1.0}); \\draw[thick] (0.7,{y+1.3}) -- (0.7,{y}) -- (5.7,{y}) -- (5.7,{y+1.3}); \\draw[dashed,very thick] (3.2,{y+1.3}) -- (3.2,{y});')
    parts.append(f'\\node at (.25,{y+.6}) {{\\textbf{{{ad_}}}}}; \\node[align=center] at (1.95,{y+.5}) {{{sl}}}; \\node[align=center] at (4.45,{y+.5}) {{{sr}}};')
sk=fig(*parts)
truth={'I':True,'II':False,'III':False}
reasons={'I':'K düzeneğinde iki tarafın toplam çözünen tanecik derişimi eşittir (0,2 ve 0,2); net su geçişi olmaz','II':'L düzeneğinde sol tarafın toplam tanecik derişimi 0,4, sağ tarafınki 0,3’tür; su sağdan sola geçer, soldan sağa geçmez','III':'M düzeneğinde sağ taraf daha derişiktir (0,4 > 0,3); su soldan sağa geçer ve sol kolun düzeyi düşer'}
S4=['Yalnız I','Yalnız III','I ve II','II ve III','I, II ve III']
dg,yn,ad=onc(truth,reasons,S4)
q('0004',tipId='cozeltiiki-koligatif-yorum',tip='Koligatif özelliklerin yorumlanması',z='orta',alt='Koligatif Özellikler',kaz='Yarı geçirgen zarla ayrılmış çözeltilerde net su geçişinin yönünü belirler.',
 kart='K-AKCOZ2-04 (ozmos yönü) · üç zarlı düzenek',kalip='öncüllü',
 metin='Şekildeki K, L ve M düzeneklerinde, yalnız su moleküllerini geçiren yarı geçirgen bir zar (kesikli çizgi) her kabı eşit hacimli iki bölmeye ayırmaktadır. Başlangıçta bölmelerdeki sıvı düzeyleri aynıdır ve çözünenlerin suda tamamen iyonlaştığı (şeker moleküler çözünür) varsayılacaktır.\nI. K düzeneğinde net su geçişi olmaz.\nII. L düzeneğinde su, sol bölmeden sağ bölmeye geçer.\nIII. M düzeneğinde sol bölmedeki sıvı düzeyi yükselir.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=dg,yan=yn,sira=S4,istenen='Doğru olan öncüller.',
 ip=['Her bölmedeki toplam çözünen tanecik derişimini (iyonlar dahil) ayrı ayrı bulup karşılaştırmayı dene.'],bilgi=[B_OZ,B_KOL],ad=ad,
 puf='Ozmosta karşılaştırılan değer mol/L değil, iyonlaşma dahil toplam çözünen tanecik derişimidir.',sekil=sk)
# ================= 05 · orta · çözünürlük eğrisi üzerinde noktalar (öncüllü) =================
S20,S60=F(20),F(45); L60=F(30)
yK=S60/(100+S60)*100; yL=L60/(100+L60)*100; assert yK>yL and S60-S20==25 and S60-L60==15
sk=fig(*kgraf([('X',[(0,12),(20,20),(40,30),(60,45),(80,65)],'vurgu!70!black',(85,67))],[20,40,60,80],[20,30,45,60],'Sıcaklık ($^\\circ$C)','Çözünürlük (g/100 g su)',85,70,.055,.05,
  noktalar=[('K',60,45,-.3,.3),('L',60,30,.3,-.25),('M',20,20,.3,-.25)],extra='\\draw[dotted] (3.3,0) -- (3.3,1.5);'))
truth={'I':False,'II':True,'III':True}
reasons={'I':'M noktası eğri üzerindedir ama L noktası eğrinin altındadır, L doymamıştır; 100 g su 60 °C’de 45 g X çözebilirken L’de 30 g vardır','II':'K’nın kütlece yüzdesi 45 ÷ 145 yaklaşık %31, L’ninki 30 ÷ 130 yaklaşık %23’tür','III':'60 °C’de 100 g suda 45 g, 20 °C’de 20 g X çözünür; fark 25 g’dır'}
S5d=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III']
dg,yn,ad=onc(truth,reasons,S5d)
q('0005',tipId='cozeltiiki-cozunurluk',tip='Çözünürlük ve çözünürlüğü etkileyen faktörler',z='orta',alt='Çözünürlük',kaz='Çözünürlük eğrisi ve eğri üzerindeki noktalardan doygunluk ve çökelmeyi yorumlar.',
 kart='K-AKCOZ2-05 (çözünürlük eğrisi üzerindeki noktalar) · X katısı, K L M noktaları',kalip='öncüllü',
 metin='Şekilde, X katısının sudaki çözünürlük eğrisi ile K, L ve M noktalarına karşılık gelen üç sulu çözelti gösterilmiştir. Her noktada çözelti 100 g su içerir.\nI. L ve M noktalarındaki çözeltilerin ikisi de doygundur.\nII. K noktasındaki çözeltinin kütlece yüzdesi, L noktasındakinden büyüktür.\nIII. K noktasındaki çözelti 20 °C’ye soğutulursa 25 g X çöker.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=dg,yan=yn,sira=S5d,istenen='Doğru olan öncüller.',
 ip=['Her noktanın eğriye göre konumunu ve noktaların 100 g sudaki çözünen kütlelerini karşılaştırmayı dene.'],bilgi=[B_YOR,B_C],ad=ad,
 puf='Eğri üzerindeki nokta doygun, altındaki doymamış çözeltidir; çökelme miktarı iki sıcaklıktaki çözünürlük farkıdır.',sekil=sk)
# ================= 06 · orta · kaynama noktası yükselmesi grafiği =================
sk=fig(*kgraf([('X',[(0,0),(2,1)],'vurgu!70!black',(2.15,1.0)),('Y',[(0,0),(1,1.5),(2,3)],'orange!80!black',(2.15,3.0))],[.5,1,1.5,2],[.5,1,1.5,2,2.5,3],'Molalite (m)','$\\Delta T_k$ ($^\\circ$C)',2.2,3,2.0,1.1,
  extra='\\draw[dotted] (2.0,0) -- (2.0,1.65); \\draw[dotted] (2.0,.55) -- (0,.55); \\draw[dotted] (2.0,1.65) -- (0,1.65);'))
sira6=['Al(NO₃)₃','KCl','Fe₂(SO₄)₃','NaNO₃','CaCl₂']
q('0006',tipId='cozeltiiki-koligatif-yorum',tip='Koligatif özelliklerin yorumlanması',z='orta',alt='Koligatif Özellikler',kaz='Kaynama noktası yükselmesi–molalite grafiğinden çözünenin iyon sayısını belirler.',
 kart='K-AKCOZ2-06 (kaynama noktası yükselmesi grafiği) · X ve Y çözünenleri',kalip='grafik',
 metin='Şekilde, X ve Y maddelerinin suda çözünmesiyle hazırlanan çözeltilerin kaynama noktası yükselmesinin (ΔT) molaliteyle değişimi verilmiştir. X, suda moleküler olarak çözünen uçucu olmayan bir maddedir; Y ise suda tamamen iyonlarına ayrışarak çözünen bir tuzdur.\nBuna göre Y’nin formülü aşağıdakilerden hangisi olabilir?',
 dogru='CaCl₂',yan=[('KCl','Eğimi iki katı saymış (i = 2) ve iyon sayısı 2 olan KCl’yi seçmiş.','bilgi'),('NaNO₃','Eğimi iki katı saymış (i = 2) ve iyon sayısı 2 olan NaNO₃’ü seçmiş.','bilgi'),('Al(NO₃)₃','Eğimi dört katı saymış (i = 4) ve iyon sayısı 4 olan Al(NO₃)₃’ü seçmiş.','dikkat'),('Fe₂(SO₄)₃','Eğimi beş katı saymış (i = 5) ve iyon sayısı 5 olan Fe₂(SO₄)₃’ü seçmiş.','dikkat')],
 sira=sira6,istenen='Y’nin olabileceği formül.',
 ip=['İki doğrunun aynı molalitedeki ΔT değerlerini karşılaştırıp tanecik sayısıyla ilişkilendirmeyi dene.'],bilgi=[B_KOL],
 ad=[A('X’in eğimi','Moleküler çözünende i = 1’dir; 1 m’da ΔT = K.','K = 0,5 °C/m'),A('Y’nin eğimi','1 m’da Y için ΔT 1,5 °C okunur.','i × K = 1,5'),A('i değerini bul','Eğim oranı tanecik sayısı katsayısını verir.','i = 1,5 ÷ 0,5 = 3'),A('Formülü seç','Suda 3 iyon veren tuz CaCl₂’dür (Ca²⁺ + 2 Cl⁻).','CaCl₂')],
 puf='ΔT–molalite eğimi i × K değeridir; moleküler maddeye göre eğim oranı iyon sayısını verir.',sekil=sk)
# ================= 07 · orta · karıştırma + buharlaştırma =================
Vn,Mn,Vm,Mm_=F('0.1'),F('0.6'),F('0.2'),F('0.3'); Vson=F('0.2')
cln=Mn*Vn; clm=Mm_*Vm*2; cl=cln+clm; M07=cl/Vson
assert (cln,clm,cl,M07)==(F('0.06'),F('0.12'),F('0.18'),F('0.9'))
d_a=cl/(Vn+Vm); d_b=cln/Vson; d_c=cl/F('0.1'); d_d=(cln+Mm_*Vm*3)/Vson
assert (d_a,d_b,d_c,d_d)==(F('0.6'),F('0.3'),F('1.8'),F('1.2')) and len({M07,d_a,d_b,d_c,d_d})==5
sk=fig(bk(0,0,1.5,2.0,.6,'100 mL','0,6 M \\ce{NaCl}'),'\\node at (2.1,.6) {\\Large $+$};',bk(2.6,0,1.5,2.0,1.1,'200 mL','0,3 M \\ce{MgCl2}'),
 '\\draw[->,thick] (4.5,.6) -- (5.5,.6); \\node[above,align=center] at (5.0,.7) {Su\\\\buharlaşır};',bk(6.0,0,1.5,2.0,.8,'Son çözelti','(200 mL)','vurgu!8'))
q('0007',tipId='cozeltiiki-karisim',tip='Çözeltileri karıştırma ve iyon derişimi',z='orta',alt='Derişim Birimleri',kaz='Çözeltiler karıştırılıp su buharlaştırıldığında iyon derişimini hesaplar.',
 kart='K-AKCOZ2-07 (karıştırma ve buharlaştırma) · NaCl + MgCl₂',kalip='şekilli',
 metin='Sıcaklıkları aynı olan şekildeki NaCl ve MgCl₂ sulu çözeltileri karıştırılıyor ve aynı sıcaklıkta su buharlaştırılarak karışımın hacmi 200 mL’ye düşürülüyor.\nBuna göre son çözeltideki Cl⁻ iyonlarının derişimi kaç molardır? (Tuzların suda tamamen iyonlarına ayrışarak çözündüğü ve karıştırmada toplam hacmin değişmediği varsayılacaktır.)',
 dogru=M07,yan=[(d_a,'Buharlaşmayı hesaba katmamış: 0,18 ÷ 0,3 = 0,6.','dikkat'),(d_b,'MgCl₂’den gelen klorürü saymamış: 0,06 ÷ 0,2 = 0,3.','bilgi'),(d_c,'Buharlaşan hacmi iki kez çıkarıp 100 mL almış: 0,18 ÷ 0,1 = 1,8.','islem'),(d_d,'MgCl₂ için klorür sayısını 3 almış: (0,06 + 0,18) ÷ 0,2 = 1,2.','dikkat')],
 istenen='Son çözeltideki Cl⁻ derişimi (M).',ip=['Buharlaşmanın hangi niceliği değiştirip hangisini değiştirmediğini düşünerek iki tuzdan gelen klorürü ayrı ayrı bulmayı dene.'],bilgi=[B_I,B_K],
 ad=[A('NaCl’den gelen Cl⁻','Formülde 1 klorür vardır.','0,6 × 0,1 = 0,06 mol'),A('MgCl₂’den gelen Cl⁻','Formülde 2 klorür vardır.','0,3 × 2 × 0,2 = 0,12 mol'),A('Toplam mol','Buharlaşma mol sayısını değiştirmez.','0,06 + 0,12 = 0,18 mol'),A('Derişim','Mol sayısı son hacme bölünür.','0,18 ÷ 0,2 = 0,9 M')],
 puf='Buharlaşma yalnız hacmi azaltır; mol sayısı sabittir ve son hacme bölünür.',sekil=sk)
# ================= 08 · zor · eş donma noktası =================
mK=F(36)/F(180); mwK=F(200)/1000; mmK=mK/mwK; iL=3; mwL=F(300)/1000
mL=mmK/iL; nL=mL*mwL; xL=nL*111
assert (mmK,mL,nL,xL)==(1,F(1,3),F('0.1'),F('11.1'))
d_a=mmK*mwL*111; d_b=mmK/2*mwL*111; d_c=mmK/iL*mwK*111; d_d=d_a*3
assert (d_a,d_b,d_c,d_d)==(F('33.3'),F('16.65'),F('7.4'),F('99.9')) and len({xL,d_a,d_b,d_c,d_d})==5
sk=fig(bk(0,0,2.0,1.8,1.2,'K kabı','200 g su','vurgu!15'),'\\node at (1.0,.6) {36 g \\ce{C6H12O6}};',
 bk(3.4,0,2.0,1.8,1.5,'L kabı','300 g su','vurgu!15'),'\\node at (4.4,.75) {$x$ g \\ce{CaCl2}};')
sk=sk.replace('','') if False else sk
q('0008',tipId='cozeltiiki-koligatif-hesap',tip='Koligatif özelliklerle hesaplama',z='zor',alt='Koligatif Özellikler',kaz='Donma noktaları eşit olan iki çözeltiden bilinmeyen çözünen kütlesini bulur.',
 kart='K-AKCOZ2-08 (eş donma noktası) · glikoz ve CaCl₂ çözeltileri',kalip='şekilli',
 metin='Şekildeki K ve L kaplarında hazırlanan sulu çözeltiler, aynı dış basınçta aynı sıcaklıkta donmaya başlamaktadır.\nBuna göre x kaçtır? (C₆H₁₂O₆ = 180 g/mol, CaCl₂ = 111 g/mol; C₆H₁₂O₆ moleküler olarak, CaCl₂ tamamen iyonlarına ayrışarak çözünmüştür.)',
 dogru=xL,yan=[(d_a,'CaCl₂’nin iyonlaştığını dikkate almamış (i = 1): m = 1 olup n = 0,3 mol ve x = 33,3.','bilgi'),(d_b,'CaCl₂ için i = 2 almış: m = 0,5, n = 0,15 mol ve x = 16,65.','dikkat'),(d_c,'L kabındaki molaliteyi K’nın 200 g suyuna uygulamış: n = 1/3 × 0,2 ve x ≈ 7,4.','islem'),(d_d,'i = 3 ile molaliteyi çarpmış (3 × 33,3): x = 99,9.','islem')],
 istenen='L kabındaki CaCl₂ kütlesi x (g).',ip=['Donma noktası alçalmasının tanecik sayısıyla molaliteye bağlı olduğunu kullanıp iki kaptaki bu çarpımı karşılaştırmayı dene.'],bilgi=[B_KOL,B_M],
 ad=[A('K kabının molalitesi','Glikoz moleküler çözünür (i = 1).','n = 36 ÷ 180 = 0,2 mol; m = 0,2 ÷ 0,2 = 1'),A('Eşitliği kur','Donma noktaları eşit olduğundan i × m değerleri eşittir.','3 × m(L) = 1 × 1'),A('L kabının molalitesi','CaCl₂ için i = 3’tür.','m(L) = 1/3 molal'),A('Mol ve kütle','Mol sayısı 0,3 kg suyla, kütle molar kütleyle bulunur.','n = 0,1 mol; x = 0,1 × 111 = 11,1 g')],
 puf='Donma noktası eşitse i × m eşittir; her kabın kendi çözücü kütlesi kullanılır.',sekil=sk)
# ================= 09 · zor · soğutma + buharlaştırma, çökelme =================
S70,S20=F(60),F(25); m70=F(320); w=m70/(1+S70/100); sol70=w*S70/100
assert (w,sol70)==(200,120)
cok1=sol70-w*S20/100; w2=w-40; cok2=sol70-w2*S20/100
assert (cok1,cok2)==(70,80)
d_a=cok1; d_b=cok1+F(40)*S70/100; d_c=sol70; d_d=cok1-F(40)*S20/100
assert (d_b,d_d)==(94,60) and len({cok2,d_a,d_b,d_c,d_d})==5
sk=tablo_svg(['Sıcaklık (°C)','Çözünürlük (g X / 100 g su)'],[['20','25'],['70','60']])
q('0009',tipId='cozeltiiki-cozunurluk',tip='Çözünürlük ve çözünürlüğü etkileyen faktörler',z='zor',alt='Çözünürlük',kaz='Soğutma ve buharlaştırma sonunda çöken katı kütlesini çözünürlük verisiyle hesaplar.',
 kart='K-AKCOZ2-09 (soğutma ve buharlaştırmayla çökelme) · X katısı, 320 g doygun çözelti',kalip='tablo',
 metin='Tabloda, X katısının sudaki çözünürlüğü iki sıcaklık için verilmiştir. 70 °C’de hazırlanan 320 g doygun X sulu çözeltisi 20 °C’ye soğutuluyor. Daha sonra sıcaklık 20 °C’de sabit tutularak çözeltideki sudan 40 g buharlaştırılıyor.\nBuna göre bu işlemler sonunda toplam kaç gram X katısı çökmüştür?',
 dogru=cok2,yan=[(d_a,'Buharlaşmayı hesaba katmamış: yalnız soğutmada çöken 70 g.','dikkat'),(d_b,'Buharlaşan suya 70 °C’deki çözünürlüğü uygulamış: 70 + 40 × 0,6 = 94.','islem'),(d_c,'Çözünen X’in tamamının çöktüğünü sanmış: 120.','bilgi'),(d_d,'Buharlaşmada çöken miktarı çıkarmış: 70 − 40 × 0,25 = 60.','islem')],
 istenen='Toplam çöken X kütlesi (g).',ip=['Önce 70 °C’deki doygun çözeltinin su ve çözünen kütlesini ayırıp her aşamada çözünebilen miktarı yeni su kütlesine göre bulmayı dene.'],bilgi=[B_C,B_BUH],
 ad=[A('Su ve X kütlesi','70 °C’de 160 g doygun çözeltide 100 g su vardır.','Su: 200 g, X: 120 g'),A('Soğutma','20 °C’de 200 g su en çok 50 g X çözer.','Çöken: 120 − 50 = 70 g'),A('Buharlaşma','Kalan su 160 g olur ve 160 g su en çok 40 g X çözer.','Yeni çözünebilen: 40 g'),A('Toplam','Başlangıçtaki X’ten çözünmüş kalan çıkarılır.','120 − 40 = 80 g')],
 puf='Her aşamada çözünebilen X, o andaki su kütlesi ve sıcaklığa göre bulunur; toplam çöken = başlangıçtaki X − sonda çözünmüş kalan.',sekil=sk)
# ================= 10 · zor · çözünme ısısı, kalorimetre =================
kafes=F(810); hid=F(-780); dH=kafes+hid; nMX=F(48)/F(60); q_=nMX*dH*1000; dT=q_/(F(300)*4); Tson=25-dT
assert (dH,nMX,q_,dT,Tson)==(30,F('0.8'),24000,20,5)
d_a=25+dT; d_b=25-dH*1000/(300*4); d_c=dT; d_d=25-(q_/(600*4))
assert (d_a,d_b,d_c,d_d)==(45,0,20,15) and len({Tson,d_a,d_b,d_c,d_d})==5
h=lambda e: float(e)*2.2/810
sk=fig('\\draw[->,thick] (0,-.2) -- (0,3.2) node[above] {Enerji};',
 f'\\draw[thick] (.6,0) -- (2.2,0); \\node[below] at (1.4,0) {{MX(k)}};',
 f'\\draw[thick] (3.6,{h(810):.2f}) -- (5.6,{h(810):.2f}); \\node[above] at (4.6,{h(810):.2f}) {{$\\mathrm{{M^+(g)+X^-(g)}}$}};',
 f'\\draw[thick] (6.7,{h(30):.2f}) -- (8.3,{h(30):.2f}); \\node[below] at (7.5,{h(30):.2f}) {{$\\mathrm{{M^+(suda)+X^-(suda)}}$}};',
 f'\\draw[->,thick,vurgu!70!black] (2.9,0) -- (2.9,{h(810):.2f}); \\draw[dashed,gray] (2.2,0) -- (3.6,0); \\draw[dashed,gray] (2.2,{h(810):.2f}) -- (3.6,{h(810):.2f}); \\node[left,align=right] at (2.85,1.1) {{+810 kJ/mol}};',
 f'\\draw[->,thick,orange!80!black] (6.1,{h(810):.2f}) -- (6.1,{h(30):.2f}); \\draw[dashed,gray] (5.6,{h(810):.2f}) -- (6.7,{h(810):.2f}); \\draw[dashed,gray] (6.1,{h(30):.2f}) -- (6.7,{h(30):.2f}); \\node[right] at (6.15,1.3) {{$-780$ kJ/mol}};')
q('0010',tipId='cozeltiiki-cozunme-enerji',tip='Çözünme sürecinde enerji',z='zor',alt='Çözünme Entalpisi',kaz='Çözünme entalpisini enerji diyagramından bulup çözeltinin son sıcaklığını hesaplar.',
 kart='K-AKCOZ2-10 (çözünme ısısı ve kalorimetre) · MX katısı, 300 g su',kalip='şekilli',
 metin='Şekilde, iyonik MX katısının suda çözünmesine ait enerji değişimleri verilmiştir. 25 °C’deki 300 g suya aynı sıcaklıktaki 48 g MX katısı ekleniyor ve katı tamamen çözünüyor.\nBuna göre çözünme sonunda çözeltinin sıcaklığı kaç °C olur? (MX = 60 g/mol; suyun öz ısısı 4 J/g·°C; ısı alışverişinin yalnız MX ile 300 g su arasında olduğu, çözünenin ve kabın ısı sığasının ihmal edildiği varsayılacaktır.)',
 dogru=Tson,yan=[(d_a,'Çözünmeyi ısı veren sanmış: sıcaklık 25 + 20 = 45.','dikkat'),(d_b,'Isıyı mol başına almış (30 kJ): ΔT = 25, sıcaklık 25 − 25 = 0.','islem'),(d_c,'Sıcaklık düşüşünü son sıcaklık olarak yazmış: 20.','dikkat'),(d_d,'Isıyı 600 g suya dağıtmış: ΔT = 10, sıcaklık 25 − 10 = 15.','islem')],
 istenen='Çözeltinin son sıcaklığı (°C).',ip=['Önce diyagramdan çözünmenin entalpisini bulup ısı alışverişinin yönünü ve büyüklüğünü mol sayısıyla ilişkilendirmeyi dene.'],bilgi=[B_EN,B_KAL],
 ad=[A('Çözünme entalpisi','Kafes ve hidratasyon entalpileri toplanır.','ΔH = +810 + (−780) = +30 kJ/mol'),A('Mol sayısı','MX kütlesi molar kütleye bölünür.','n = 48 ÷ 60 = 0,8 mol'),A('Alınan ısı','Çözünme endotermik olduğundan ısı sudan alınır.','q = 0,8 × 30 = 24 kJ = 24000 J'),A('Sıcaklık düşüşü','q = m × c × ΔT.','ΔT = 24000 ÷ (300 × 4) = 20 °C'),A('Son sıcaklık','Su soğur.','25 − 20 = 5 °C')],
 puf='Endotermik çözünmede alınan ısı q = n × ΔH sudan çekilir ve ΔT = q ÷ (m × c) kadar soğuma olur.',sekil=sk)
# ================= yaz =================
assert len(P.ANA)==10,len(P.ANA)
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/cozeltiiki'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'cozeltiiki-1.json'),os.path.join(SC,'bos-cozeltiiki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 12. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akcozeltiiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
