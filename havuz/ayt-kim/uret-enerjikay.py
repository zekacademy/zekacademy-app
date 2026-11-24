"""AYT Kimya · Enerji Kaynakları ve Bilimsel Gelişmeler · 20 soru (kardeş yok, ipucu 1).
Tüm sayısal cevap ve çeldirici değerleri Fraction ile hesaplanır, assert edilir; öncüllerin doğruluğu tek yerde (stm) tanımlanır."""
import sys,os,math,json
AD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(AD,'..','tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
KONU_='Enerji Kaynakları ve Bilimsel Gelişmeler'; UK='akim|Enerji Kaynakları ve Bilimsel Gelişmeler'
H.KONU=KONU_
P=Parti('enerjikay',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM 2018–2026 AYT Kimya (yalnız mantık) · MEB 11–12. sınıf Enerji Kaynakları ve Bilimsel Gelişmeler'
# ---------------- kartlar ----------------
kart('K-AKENK-01','Fosil yakıtlar','Fosil yakıtlar canlı kalıntılarından uzun jeolojik sürede oluşur, tükenir; yanmaları CO₂ ve (kükürt içerenlerde) SO₂ gibi gazlar açığa çıkarır.','Fosil yakıtları yenilenebilir saymak; yalnız C ve H içerdiklerini sanmak; yanma ürünlerinin atmosferi etkilemediğini düşünmek.','kolay','öncüllü',2,'en-fosil','Fosil yakıtlar',KY)
kart('K-AKENK-02','Yanma entalpisi ve stokiyometri','Yanma entalpisi 1 mol yakıt (denklem katsayısı) için verilir; ısı = mol × molar yanma ısısı; sınırlayıcı bileşen yanan miktarı belirler.','Katsayıyı mole çevirmemek; sınırlayıcı bileşeni atlamak; kütleyi mol kütlesine bölmeden çarpmak.','orta','şekilli',3,'en-yanma','Yanma ısısı hesapları',KY)
kart('K-AKENK-03','Isıl değer (kJ/g)','Isıl değer 1 g yakıtın tam yanmasıyla açığa çıkan ısıdır; toplam ısı kütle ile çarpılarak bulunur.','Farklı yakıtların değerlerini karıştırmak; kütleyi atlayıp yalnız değeri yazmak.','kolay','grafik',2,'en-yanma','Yanma ısısı hesapları',KY)
kart('K-AKENK-04','Kalorimetri ve ısı aktarımı','q = m·c·ΔT; yakıttan suya geçen ısı verimle çarpılır; toplam ısı = suya geçen ısı ÷ verim.','Verimi çarpmak yerine bölmek ya da hiç uygulamamak; kJ ile J’yi karıştırmak.','orta','grafik',4,'en-kalori','Kalorimetri ve ısı aktarımı',KY)
kart('K-AKENK-05','Yenilenebilir ve alternatif enerji','Güneş, rüzgâr, akan su, jeotermal ve biyokütle yenilenebilir kaynaklardır; hidrojen yakıt olarak yandığında ürün sudur.','Hidrojenin yanmasında CO₂ oluştuğunu sanmak; jeotermali fosil yakıtla karıştırmak.','kolay','şekilli',2,'en-alternatif','Yenilenebilir ve alternatif kaynaklar',KY)
kart('K-AKENK-06','Nükleer enerji ve radyoaktiflik','Çekirdek tepkimelerinde toplam kütle numarası ve toplam atom numarası korunur; fisyon ağır çekirdeğin bölünmesi, füzyon hafif çekirdeklerin birleşmesidir; yarı ömür sabittir.','Nötron sayısını kütle numarasıyla karıştırmak; girenlerdeki nötronu saymamak; yarı ömür sayısını yanlış bulmak.','orta','şekilli',3,'en-nukleer','Nükleer enerji',KY)
kart('K-AKENK-07','Karbon ayak izi','Karbon ayak izi, bir etkinliğin doğrudan ya da dolaylı CO₂ salımıdır; yakıtın yanmasından oluşan CO₂ mol sayısı denklemden bulunur.','Salımı kütle yerine mol saymak; yüzde azalmayı toplama göre değil parçaya göre almak.','zor','tablo',4,'en-surdur','Karbon ayak izi ve sürdürülebilirlik',KY)
kart('K-AKENK-08','Enerji tüketimi ve paylar','Pay (%) tek başına miktar değildir; miktar = toplam × pay. Toplam değiştiğinde payın sabit kalması miktarın sabit kaldığı anlamına gelmez.','Payı miktar sanmak; toplamın değiştiğini görmemek.','orta','tablo',3,'en-surdur','Karbon ayak izi ve sürdürülebilirlik',KY)
kart('K-AKENK-09','Yakıt pilleri','Yakıt pilinde yakıtın yükseltgendiği elektrot anot, O₂’nin indirgendiği elektrot katottur; elektronlar dış devrede anottan katota akar; verim elektrik enerjisinin ΔH’a oranıdır.','Elektron yönünü ters almak; anot–katot ayrımını işaretle karıştırmak; verimi uygulamamak.','orta','şekilli',3,'en-pil','Yakıt pilleri',KY)
kart('K-AKENK-10','Nanoteknoloji','1 nm = 10⁻⁹ m; parçacık küçüldükçe birim kütle başına yüzey alanı ve yüzeydeki atom oranı artar; madde miktarı ve yoğunluğu değişmez.','Toplam hacmin ya da yoğunluğun değiştiğini sanmak; yüzey alanı artışını kat sayısıyla karıştırmak.','orta','şekilli',3,'en-nano','Nanoteknoloji',KY)
CARD={c['id']:c for c in H.KARTLAR}
def kk(n,ne): c=CARD[f'K-AKENK-{n}']; return f'K-AKENK-{n} ({c["alt"].lower()}) · {ne}'
def q(no,n,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    c=CARD[f'K-AKENK-{n}']
    mk(P,no,ad=ad,adim=len(ad),tipId=c['tipId'],tip=c['tip'],kart=kk(n,k.pop('ne')),**k)
RM='I II III'.split()
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
NAMES={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(no,n,bag,stm,secenek,tail,ne,fiil=('doğru','yanlış'),**k):
    """stm: (metin, istenen_küme_içinde_mi, açıklama, seçeni_yanlışlıkla_alma_hatası, seçmeme_hatası)."""
    truth={i for i,s in enumerate(stm) if s[1]}
    dogru=[a for a in secenek if NAMES[a]==truth]; assert len(dogru)==1 and len(secenek)==5 and len(set(secenek))==5
    assert [ORD.index(a) for a in secenek]==sorted(ORD.index(a) for a in secenek),'şık sırası'
    dogru=dogru[0]; yan=[]
    for a in secenek:
        if a==dogru: continue
        S=NAMES[a]; parts=[]
        for i in sorted(S^truth):
            parts.append(f'{RM[i]}. ifadeyi {fiil[0]} saymış; {stm[i][3]}' if i in S else f'{RM[i]}. ifadeyi {fiil[1]} saymış; {stm[i][4]}')
        yan.append((a,' '.join(parts),'bilgi'))
    metin=bag+'\n'+'\n'.join(f'{RM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+tail
    ad=[A(f'{RM[i]}. ifadeyi değerlendir',s[2],f'{RM[i]}: {fiil[0] if s[1] else fiil[1]}') for i,s in enumerate(stm)]
    ad.append(A('Sonucu birleştir','İstenen koşulu sağlayan ifadeler birlikte seçilir.',dogru))
    q(no,n,ad,ne=ne,metin=metin,dogru=dogru,sira=list(secenek),yan=yan,**k)
def tek(S,sira):
    assert sum(1 for s in S if s[1])==1
    d=[s for s in S if s[1]][0]
    return d[0],[(s[0],s[2],'bilgi') for s in S if not s[1]],sira
# ---------------- şekil yardımcıları ----------------
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def bars(names,vals,ymax,ystep,ylab):
    sc=3.0/ymax; g=''; n=len(names); W=1.25*n+.5
    g+=f'\\draw[{ARR},thick] (0,0) -- (0,{ymax*sc+.5:.3f}); \\draw[thick] (0,0) -- ({W:.2f},0);'
    for v in range(0,ymax+1,ystep):
        g+=f'\\draw (0,{v*sc:.3f}) -- (-.08,{v*sc:.3f}); \\node[left,inner sep=2pt] at (-.05,{v*sc:.3f}) {{{v}}};'
        if v>0: g+=f'\\draw[gray!50,dashed] (0,{v*sc:.3f}) -- ({W:.2f},{v*sc:.3f});'
    for i,(nm,v) in enumerate(zip(names,vals)):
        x=.75+1.25*i
        g+=f'\\filldraw[fill=vurgu!30,draw=vurgu!60!black,thick] ({x-.4:.2f},0) rectangle ({x+.4:.2f},{v*sc:.3f});'
        g+=f'\\node[above,inner sep=2pt] at ({x:.2f},{v*sc:.3f}) {{{v}}}; \\node[below,inner sep=3pt,align=center] at ({x:.2f},0) {{{nm}}};'
    g+=f'\\node[rotate=90] at (-1.0,{ymax*sc/2:.3f}) {{{ylab}}};'
    return tk(g)
def tablo_tikz(*a): raise NotImplementedError

# =============== 0001 · ısıl değer · kolay · grafik ===============
IV={'X':55,'Y':30,'Z':45}
SK=bars(['X','Y','Z'],[IV[k] for k in 'XYZ'],60,10,'Isıl değer (kJ/g)')
s1=40*IV['Y']+20*IV['Z']; assert s1==2100
d1=40*IV['Y']; d2=(40+20)*IV['Y']; d3=40*IV['Z']+20*IV['Y']; d4=40*IV['X']+20*IV['Z']
assert (d1,d2,d3,d4)==(1200,1800,2400,3100) and len({s1,d1,d2,d3,d4})==5
q('0001','03',[A('Grafiği oku','Her çubuk, 1 g yakıtın tam yanmasıyla açığa çıkan ısıyı gösterir.','Y: 30 kJ/g ; Z: 45 kJ/g'),
 A('Y’nin ısısını bul','Toplam ısı, kütle ile ısıl değerin çarpımıdır.','40 × 30 = 1200 kJ'),
 A('Z’nin ısısını bul','Aynı işlem Z yakıtı için yapılır.','20 × 45 = 900 kJ'),
 A('Toplamı yaz','İki yakıtın verdiği ısılar toplanır.','1200 + 900 = 2100 kJ')],
 ne='iki yakıtın toplam yanma ısısı',metin='Şekilde, X, Y ve Z yakıtlarının 1 gramının tam yanmasıyla açığa çıkan ısı (ısıl değer) verilmiştir.\nBuna göre 40 g Y ile 20 g Z yakıtının tamamen yakılmasıyla toplam kaç kJ ısı açığa çıkar?',
 dogru=s1,yan=[(d1,'Yalnız Y yakıtının ısısını hesaplamış; Z yakıtının verdiği ısıyı toplama katmamış.','dikkat'),(d2,'Toplam kütleyi (60 g) yalnız Y’nin ısıl değeriyle çarpmış; Z için farklı değer okumamış.','dikkat'),(d3,'Yakıtların ısıl değerlerini birbiriyle ters eşleştirmiş (40 g × 45 + 20 g × 30).','dikkat'),(d4,'Y yerine X çubuğunun değerini okumuş (40 g × 55 + 20 g × 45).','dikkat')],
 z='kolay',alt='Isıl Değer',kaz='Grafikten okuduğu ısıl değerlerle farklı yakıtların toplam yanma ısısını hesaplar.',kalip='grafik',sekil=SK,
 istenen='40 g Y ve 20 g Z yakıtından açığa çıkan toplam ısı (kJ).',
 ip=['Her yakıt için ısıyı ayrı ayrı bul; sonra birleştir.'],
 bilgi=[B('Isıl değer','1 g yakıtın tam yanmasıyla açığa çıkan ısıdır; toplam ısı yakıt kütlesiyle çarpılarak bulunur. Örnek: ısıl değeri 20 kJ/g olan yakıttan 3 g yakılırsa 60 kJ ısı açığa çıkar')],
 puf='Toplam ısı = yakıt kütlesi × ısıl değer; her yakıt için ayrı hesaplanır.')

# =============== 0002 · fosil yakıtlar · kolay · öncüllü ===============
onc('0002','01','Fosil yakıtlar günümüzde dünya enerji ihtiyacının büyük bölümünü karşılamaktadır.',
 [('Kömür, petrol ve doğal gaz canlı kalıntılarından milyonlarca yılda oluşmuştur.',True,'Fosil yakıtlar, canlı kalıntılarının uzun jeolojik süreçlerde dönüşmesiyle oluşur.','—','fosil yakıtların oluşumunu canlı kalıntılarıyla ilişkilendirememiş.'),
  ('Fosil yakıtların hepsi yalnızca karbon ve hidrojen elementlerinden oluşur.',False,'Kömür ve ham petrol kükürt, azot gibi elementleri de içerebilir.','fosil yakıtları yalnız hidrokarbon sanıp kükürt ve azot bileşiklerini unutmuş.','—'),
  ('Fosil yakıtların yanması atmosferdeki CO₂ miktarını azaltır.',False,'Yanma sonucu CO₂ açığa çıkar; atmosferdeki CO₂ miktarı artar.','yanma ürünü olan CO₂’nin atmosfere karıştığını görmemiş.','—')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],'Buna göre bu ifadelerden hangileri doğrudur?',
 ne='fosil yakıtlarla ilgili üç ifade',z='kolay',alt='Fosil Yakıtlar',kaz='Fosil yakıtların oluşumu, bileşimi ve yanma ürünleri hakkındaki ifadeleri değerlendirir.',kalip='öncüllü',
 istenen='Doğru olan ifadeler.',
 ip=['Her ifadeyi fosil yakıtların oluşumu ve yanma ürünleri açısından ayrı ayrı sına.'],
 bilgi=[B('Fosil yakıtlar','kömür, petrol ve doğal gazdır; tükenebilir kaynaklardır. İçerdikleri karbonun yanmasıyla CO₂, kükürt bileşiklerinin yanmasıyla SO₂ oluşur. Örnek: S + O₂ → SO₂')],
 puf='Fosil yakıt = canlı kalıntısı kökenli, tükenebilir kaynak; yanınca CO₂ (ve çoğu zaman SO₂) çıkar.')

# =============== 0003 · yenilenebilir kaynak · kolay · şekilli ===============
g=''
rows=[('I','Doğal gaz','Doğal gaz\\\\santrali'),('II','Rüzgâr','Rüzgâr\\\\türbini'),('III','Akan su','Hidroelektrik\\\\santral')]
for i,(r,a,b) in enumerate(rows):
    y=-1.3*i
    g+=f'\\node at (-.6,{y}) {{{r}.}};'
    g+=f'\\node[draw,rounded corners,minimum width=2.2cm,minimum height=.9cm,align=center] (a{i}) at (1.6,{y}) {{{a}}};'
    g+=f'\\node[draw,rounded corners,fill=vurgu!15,minimum width=2.4cm,minimum height=.9cm,align=center] (b{i}) at (5.2,{y}) {{{b}}};'
    g+=f'\\node[draw,rounded corners,minimum width=2.2cm,minimum height=.9cm,align=center] (c{i}) at (8.8,{y}) {{Elektrik\\\\enerjisi}};'
    g+=f'\\draw[{ARR},thick] (a{i}) -- (b{i}); \\draw[{ARR},thick] (b{i}) -- (c{i});'
SK=tk(g)
q('0003','05',[A('Her sistemi incele','Şekilde üç sistemde kullanılan enerji kaynağı yazılıdır.','I: doğal gaz · II: rüzgâr · III: akan su'),
 A('Kaynakları sınıflandır','Doğal gaz fosil yakıttır ve tükenir; rüzgâr ve akan su doğada sürekli yenilenir.','I: tükenebilir · II, III: yenilenebilir'),
 A('Sonucu yaz','Yenilenebilir kaynak kullanan sistemler seçilir.','II ve III')],
 ne='üç elektrik üretim sisteminde kaynağın yenilenebilirliği',metin='Şekilde, I, II ve III ile numaralanmış üç sistemde elektrik enerjisi üretiminde kullanılan enerji kaynağı gösterilmiştir.\nBuna göre bu sistemlerden hangilerinde kullanılan enerji kaynağı yenilenebilirdir?',
 dogru='II ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 yan=[('Yalnız I','Doğal gazı yenilenebilir saymış; fosil yakıtların tükendiğini ve yeniden oluşmadığını bilmiyor.','bilgi'),('Yalnız II','Rüzgârı yenilenebilir bulmuş ama akan suyu da aynı sınıfta görmemiş.','bilgi'),('I ve II','Doğal gazı yenilenebilir saymış ve akan suyu yenilenebilir kaynaklar dışında bırakmış.','bilgi'),('I ve III','Doğal gazı yenilenebilir saymış ve rüzgârı yenilenebilir kaynaklar dışında bırakmış.','bilgi')],
 z='kolay',alt='Yenilenebilir Kaynaklar',kaz='Elektrik üretim sistemlerindeki enerji kaynaklarını yenilenebilir ve tükenebilir olarak sınıflandırır.',kalip='şekilli',sekil=SK,
 istenen='Yenilenebilir kaynak kullanan sistemler.',
 ip=['Kaynağın kısa sürede doğada yeniden oluşup oluşmadığını düşün.'],
 bilgi=[B('Yenilenebilir enerji kaynakları','doğada sürekli yenilenen kaynaklardır: güneş, rüzgâr, akan su, jeotermal, biyokütle. Fosil yakıtlar ise tükenebilir. Örnek: dalga enerjisi yenilenebilir, kömür tükenebilirdir')],
 puf='Yenilenebilir = doğada sürekli yeniden sağlanan; fosil yakıtlar bu sınıfta değildir.')

# =============== 0004 · kalorimetri grafiği · orta · grafik ===============
m4=400; c4=4; sl=15; T0=25; eta=Fr(6,10)
Gs=[(g_,T0+sl*g_) for g_ in range(4)]
su=Fr(m4*c4*sl,1000); top=su/eta; assert (su,top)==(24,40)
w1=su*eta; w2=su/(1-eta); w3=Fr(m4*c4*(Gs[3][1]-T0),1000)
assert (w1,w2,w3)==(Fr(72,5),60,72) and len({top,w1,w2,w3,su})==5
sc_y=.065; sx=1.9
g=f'\\draw[{ARR},thick] (0,0) -- (0,{(70-20)*sc_y+.6:.3f}); \\draw[{ARR},thick] (0,0) -- ({3*sx+.8},0);'
for v in (25,40,55,70):
    yy=(v-20)*sc_y; g+=f'\\draw (0,{yy:.3f}) -- (-.08,{yy:.3f}); \\node[left,inner sep=2pt] at (-.05,{yy:.3f}) {{{v}}};\\draw[gray!60,dashed] (0,{yy:.3f}) -- ({3*sx+.3},{yy:.3f});'
for k in range(4):
    g+=f'\\draw ({k*sx},0) -- ({k*sx},-.08); \\node[below,inner sep=2pt] at ({k*sx},-.05) {{{k}}};\\draw[gray!60,dashed] ({k*sx},0) -- ({k*sx},{(70-20)*sc_y:.3f});'
g+='\\draw[vurgu,very thick] '+' -- '.join(f'({a*sx},{(b-20)*sc_y:.3f})' for a,b in Gs)+';'
for a,b in Gs: g+=f'\\fill[vurgu!70!black] ({a*sx},{(b-20)*sc_y:.3f}) circle (.07);'
g+=f'\\node[rotate=90] at (-1.0,{(50*sc_y)/2:.3f}) {{Suyun sıcaklığı (°C)}}; \\node[below] at ({1.5*sx},-.5) {{Yakılan X kütlesi (g)}};'
SK=tk(g)
q('0004','04',[A('Grafikten eğimi oku','Her 1 g X yakıldığında sıcaklık aynı miktarda artar.','1 g için: 40 − 25 = 15 °C'),
 A('Suyun aldığı ısıyı bul','q = m × c × ΔT bağıntısı kullanılır.','400 × 4 × 15 = 24000 J = 24 kJ'),
 A('Verimi uygula','Açığa çıkan ısının %60’ı suya geçtiğinden toplam ısı suyun aldığı ısıdan büyüktür.','24 ÷ 0,6 = 40 kJ'),
 A('Birimi yaz','Bu ısı 1 g X için hesaplandığından yanma ısısı kJ/g cinsindendir.','40 kJ/g')],
 ne='grafikten verimli ısı aktarımıyla yanma ısısı',metin='Başlangıç sıcaklığı 25 °C olan 400 g saf su içeren bir kalorimetre kabında X yakıtı tam olarak yakılıyor. Açığa çıkan ısının yalnızca %60’ı suya aktarılmaktadır. Şekilde, yakılan X kütlesine karşılık suyun sıcaklığı verilmiştir.\nSuyun öz ısısı 4 J/g·°C olduğuna göre X yakıtının yanma ısısı kaç kJ/g’dır?',
 dogru=top,yan=[(w1,'Suya geçen ısıyı (24 kJ) %60 ile bir kez daha çarpmış; verimi ters uygulamış.','islem'),(su,'Suyun aldığı ısıyı (24 kJ) yakıtın verdiği ısı sanmış; %60 verimi hesaba katmamış.','dikkat'),(w2,'Toplam ısıyı bulmak için 24’ü %40’a bölmüş; kaybı verim yerine kullanmış.','islem'),(w3,'Grafikteki son noktayı (3 g, 70 °C) 1 g için okumuş ve verimi hesaba katmamış.','dikkat')],
 z='orta',alt='Kalorimetri',kaz='Sıcaklık–kütle grafiğinden suya geçen ısıyı ve verimle birlikte yakıtın yanma ısısını hesaplar.',kalip='grafik',sekil=SK,
 istenen='X yakıtının yanma ısısı (kJ/g).',
 ip=['Önce suyun 1 g yakıt için aldığı ısıyı bul; sonra bunun toplam ısının hangi kesri olduğunu düşün.'],
 bilgi=[B('Isı aktarım verimi','yakıttan çıkan ısının yalnız bir kısmı suya geçiyorsa suyun aldığı ısı = verim × yakıtın verdiği ısıdır. Örnek: %50 verimle suya 10 kJ geçmişse yakıt 20 kJ ısı vermiştir')],
 puf='Verim varsa yakıtın verdiği ısı = suyun aldığı ısı ÷ verim.')

# =============== 0005 · karbon ayak izi çubuk grafik · orta ===============
KZ={'Elektrik':160,'Ulaşım':200,'Isınma':120,'Diğer':20}
SK=bars(list(KZ),list(KZ.values()),200,50,'Aylık CO$_2$ salımı (kg)')
tot=sum(KZ.values()); a_u=Fr(KZ['Ulaşım']*40,100); a_e=Fr(KZ['Elektrik']*25,100)
res=(a_u+a_e)/tot*100; assert tot==500 and res==24
e1=a_u/tot*100; e2=Fr(40+25,2); e3=Fr(40); e4=Fr(65)
assert (e1,e2)==(16,Fr(65,2)) and len({res,e1,e2,e3,e4})==5
q('0005','07',[A('Toplam salımı bul','Çubuk değerleri toplanır.','160 + 200 + 120 + 20 = 500 kg'),
 A('Ulaşımdaki azalmayı bul','Ulaşım salımı %40 azalır.','200 × 0,40 = 80 kg'),
 A('Elektrikteki azalmayı bul','Elektrik salımı %25 azalır.','160 × 0,25 = 40 kg'),
 A('Toplam azalmayı yüzdeye çevir','Azalan toplam miktar, ilk toplam salıma oranlanır.','(80 + 40) ÷ 500 = 0,24 = %24')],
 ne='bölümlerdeki azalmalardan toplam yüzde azalma',metin='Şekilde, bir evin aylık karbon ayak izine (CO₂ salımı) katkıda bulunan kaynaklar verilmiştir. Evdeki aileler toplu taşıma kullanarak ulaşımdan kaynaklanan salımı %40, LED lambalara geçerek elektrikten kaynaklanan salımı %25 azaltıyor; diğer kaynaklar değişmiyor.\nBuna göre evin toplam aylık karbon ayak izi yüzde kaç azalır?',
 dogru=res,yan=[(e1,'Yalnız ulaşımdaki azalmayı (80 kg) toplama oranlamış; elektrikteki azalmayı katmamış.','dikkat'),(e2,'İki yüzde azalmanın aritmetik ortalamasını almış; kaynakların farklı payları olduğunu görmemiş.','islem'),(e3,'Ulaşımdaki %40’ı toplam azalma saymış; diğer kaynağı ve toplam salımı hesaba katmamış.','dikkat'),(e4,'İki yüzde değeri doğrudan toplamış (40 + 25); her yüzdenin ayrı bir bölüme ait olduğunu görmemiş.','islem')],
 z='orta',alt='Karbon Ayak İzi',kaz='Karbon ayak izi bileşenlerindeki yüzde azalmalardan toplam azalmayı hesaplar.',kalip='grafik',sekil=SK,
 istenen='Toplam karbon ayak izindeki yüzde azalma.',
 ip=['Yüzdeleri doğrudan toplama; önce kg olarak ne kadar azaldığını bul.'],
 bilgi=[B('Karbon ayak izi','bir etkinliğin ya da kişinin neden olduğu toplam CO₂ salımıdır. Bölümlerin yüzde azalmaları farklı kütlelere uygulandığından önce kütle azalması bulunur. Örnek: 100 kg’lık bölümde %10 azalma 10 kg eder')],
 puf='Farklı bölümlerin yüzdelerini toplama; önce miktara çevir, sonra toplama oranla.')

# =============== 0006 · yakıt pili · orta · öncüllü + şekil ===============
g='\\draw[thick,rounded corners=3pt] (0,0) rectangle (8,3);'
g+='\\fill[vurgu!12] (2.4,.02) rectangle (5.6,2.98);'
g+='\\draw[line width=3pt] (2.4,.3) -- (2.4,2.7); \\draw[line width=3pt] (5.6,.3) -- (5.6,2.7);'
g+='\\node[below] at (2.4,-.02) {Elektrot I}; \\node[below] at (5.6,-.02) {Elektrot II};'
g+=f'\\draw[{ARR},thick] (-1.2,2.0) -- (0,2.0); \\node[left] at (-1.2,2.0) {{\\ce{{H2(g)}}}};'
g+=f'\\draw[{ARR},thick] (9.2,2.0) -- (8,2.0); \\node[right] at (9.2,2.0) {{\\ce{{O2(g)}}}};'
g+=f'\\draw[{ARR},thick] (8,.6) -- (9.2,.6); \\node[right] at (9.2,.6) {{\\ce{{H2O}}}};'
g+='\\node[align=center] at (4,1.5) {H$^+$ iyonlarını\\\\geçiren elektrolit};'
g+='\\draw[thick] (2.4,3.05) -- (2.4,4.1) -- (3.5,4.1); \\draw[thick] (5.6,3.05) -- (5.6,4.1) -- (4.5,4.1);'
g+='\\draw[thick] (4,4.1) circle (.5); \\draw[thick] (3.65,3.75) -- (4.35,4.45); \\draw[thick] (3.65,4.45) -- (4.35,3.75);'
g+='\\node[above] at (4,4.65) {Lamba};'
SK=tk(g)
onc('0006','09','Şekilde, asidik elektrolit kullanan bir hidrojen–oksijen yakıt pili şematik olarak verilmiştir. Pil çalışırken lamba ışık vermektedir.',
 [('Elektronlar dış devrede I numaralı elektrottan II numaralı elektroda doğru akar.',True,'H₂ gazı I numaralı elektrotta yükseltgenir; açığa çıkan elektronlar dış devreden II’ye gider.','—','H₂’nin yükseltgendiği elektrottan elektron çıkışını görmemiş.'),
  ('II numaralı elektrotta O₂ gazı indirgenir.',True,'O₂ gazı II numaralı elektrotta elektron alarak indirgenir ve H⁺ ile su oluşturur.','—','oksijenin elektron alarak indirgendiğini bilmiyor.'),
  ('Elektrolitteki H⁺ iyonları II numaralı elektrottan I numaralı elektroda doğru hareket eder.',False,'H⁺ iyonları I’de oluşur ve II’ye doğru hareket eder; yön ters verilmiş.','H⁺ iyonlarının hareket yönünü ters almış.','—')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],'Buna göre bu pil ile ilgili hangileri doğrudur?',
 ne='yakıt pilinde elektron ve iyon yönleri',z='orta',alt='Yakıt Pilleri',kaz='Yakıt pilinde elektrotlardaki olayları, elektron ve iyon yönlerini yorumlar.',kalip='şekilli',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['H₂ ve O₂’nin hangi elektrotta elektron verip aldığını belirle; sonra yönleri bul.'],
 bilgi=[B('Yakıt pili','yakıtın sürekli verilerek kimyasal enerjinin doğrudan elektrik enerjisine dönüştürüldüğü bir düzenektir. Yükseltgenmenin olduğu elektrot anot, indirgenmenin olduğu elektrot katottur; elektronlar dış devrede anottan katota akar. Örnek: Zn(k) → Zn²⁺ + 2e⁻ anotta olur')],
 puf='Yakıt pilinde yakıt anotta yükseltgenir; elektron anottan katota, katyon elektrolitte anottan katota akar.')

# =============== 0007 · yanma entalpisi diyagramı · orta ===============
dHc=Fr(-890); mCH4=Fr(8); M=Fr(16); n7=mCH4/M; Q7=-dHc*n7; assert n7==Fr(1,2) and Q7==445
y1=-dHc*mCH4; y2=-dHc/mCH4; y3=-dHc*(mCH4/32)
assert (y1,y2,y3)==(7120,Fr(445,4),Fr(445,2)) and len({Q7,y1,y2,y3,-dHc})==5
sc=.0034
g=f'\\draw[{ARR},thick] (0,{-890*sc-.9:.3f}) -- (0,.9); \\node[rotate=90] at (-1.5,{-890*sc/2:.3f}) {{Entalpi (kJ)}};'
g+=f'\\draw[thick] (1.0,0) -- (3.7,0); \\draw[thick] (2.9,{-890*sc:.3f}) -- (5.6,{-890*sc:.3f});'
g+=f'\\draw[dashed,gray] (0,0) -- (1.0,0); \\draw[dashed,gray] (0,{-890*sc:.3f}) -- (2.9,{-890*sc:.3f});'
g+=f'\\draw (0,0) -- (-.08,0); \\node[left,inner sep=2pt] at (-.05,0) {{0}}; \\draw (0,{-890*sc:.3f}) -- (-.08,{-890*sc:.3f}); \\node[left,inner sep=2pt] at (-.05,{-890*sc:.3f}) {{$-890$}};'
g+='\\node[above,align=center] at (2.35,.02) {\\ce{CH4(g) + 2O2(g)}}; '
g+=f'\\node[below,align=center] at (4.25,{-890*sc-.02:.3f}) {{\\ce{{CO2(g) + 2H2O(s)}}}};'
g+=f'\\draw[vurgu,very thick,{ARR}] (3.3,0) -- (3.3,{-890*sc:.3f}); \\node[right] at (3.3,{-445*sc:.3f}) {{$\\Delta H$}};'
SK=tk(g)
q('0007','02',[A('Diyagramdan ΔH’ı oku','Girenlerin entalpisi 0, ürünlerinki −890 kJ olduğundan fark tepkime entalpisidir.','ΔH = −890 − 0 = −890 kJ'),
 A('Denklemin anlamını yaz','Bu değer, denklemdeki 1 mol CH₄ için verilmiştir.','1 mol CH₄ → 890 kJ ısı'),
 A('CH₄ mol sayısını bul','Mol sayısı kütlenin mol kütlesine bölümüdür.','8 ÷ 16 = 0,5 mol'),
 A('Isıyı hesapla','Açığa çıkan ısı, mol sayısı ile 1 mol için verilen ısının çarpımıdır.','0,5 × 890 = 445 kJ')],
 ne='diyagramdaki ΔH’tan kütleyle ısı',metin='Şekilde, CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(s) tepkimesine ait entalpi diyagramı verilmiştir (H: 1, C: 12, O: 16).\nBuna göre 8 g CH₄(g) tamamen yakıldığında açığa çıkan ısı kaç kJ’dir?',
 dogru=Q7,yan=[(-dHc,'1 mol CH₄ için verilen ısıyı (890 kJ) 8 g için de aynen yazmış; mol sayısını hesaba katmamış.','dikkat'),(y1,'Kütleyi (8 g) doğrudan ΔH ile çarpmış; mol sayısına çevirmemiş.','islem'),(y2,'ΔH’ı kütleye bölmüş (890 ÷ 8); mol sayısıyla çarpmak yerine kütleye bölmüş.','islem'),(y3,'O₂’nin mol kütlesini (32) kullanarak 0,25 mol bulmuş; CH₄ yerine yanlış maddeyi almış.','bilgi')],
 z='orta',alt='Yanma Isısı',kaz='Entalpi diyagramından yanma entalpisini okuyup yakılan kütleye göre açığa çıkan ısıyı bulur.',kalip='grafik',sekil=SK,
 istenen='8 g CH₄’nin yanmasıyla açığa çıkan ısı (kJ).',
 ip=['Diyagramdaki ΔH hangi madde miktarı için verilmiştir; 8 g bunun kaç katıdır?'],
 bilgi=[B('Entalpi diyagramı ve mol','girenlerle ürünler arasındaki entalpi farkı, denklemdeki katsayılar kadar madde için ΔH’tır. Örnek: 2 mol X için ΔH = −100 kJ ise 1 mol X için −50 kJ’dir')],
 puf='ΔH denklemdeki katsayılar içindir; ısı = (mol ÷ katsayı) × |ΔH|.')

# =============== 0008 · fisyon denklemi · orta ===============
A_U,Z_U,A_Ba,Z_Ba,nn=235,92,144,56,3
A_Kr=A_U+1-A_Ba-nn; Z_Kr=Z_U-Z_Ba; N_Kr=A_Kr-Z_Kr
assert (A_Kr,Z_Kr,N_Kr)==(89,36,53)
f1=A_U-A_Ba-nn-Z_Kr; f2=A_U+1-A_Ba-Z_Kr
assert (f1,f2)==(52,56) and len({N_Kr,Z_Kr,A_Kr,f1,f2})==5
g='\\node[draw,rounded corners,fill=vurgu!10,inner sep=8pt,font=\\large] at (0,0) {\\ce{^{235}_{92}U} + \\ce{^{1}_{0}n} $\\longrightarrow$ \\ce{^{144}_{56}Ba} + \\ce{^{A}_{Z}Kr} + 3\\,\\ce{^{1}_{0}n}};'
g+=f'\\node[below,align=center,gray!50!black] at (0,-.8) {{\\footnotesize Kütle numarası üstte, atom numarası altta yazılmıştır.}};'
SK=tk(g)
q('0008','06',[A('Kütle numarasını koru','Giren ve çıkan toplam kütle numarası eşittir; girenlerde 1 nötron, ürünlerde 3 nötron vardır.','235 + 1 = 144 + A + 3 ise A = 89'),
 A('Atom numarasını koru','Nötronun atom numarası 0’dır; toplam atom numarası korunur.','92 + 0 = 56 + Z + 0 ise Z = 36'),
 A('Nötron sayısını bul','Nötron sayısı kütle numarası ile atom numarası farkıdır.','89 − 36 = 53')],
 ne='fisyon denklemindeki bilinmeyen çekirdeğin nötron sayısı',metin='Şekilde, ²³⁵U çekirdeğinin bir nötron yakalamasıyla gerçekleşen fisyon tepkimesi verilmiştir.\nBuna göre tepkimede oluşan Kr çekirdeğinin nötron sayısı kaçtır?',
 dogru=N_Kr,yan=[(Z_Kr,'Atom numarasını (36) nötron sayısı sanmış.','bilgi'),(A_Kr,'Kütle numarasını (89) nötron sayısı olarak yazmış; proton sayısını çıkarmamış.','bilgi'),(f1,'Girenlerdeki nötronu saymamış (A = 88); nötron sayısını 52 bulmuş.','dikkat'),(f2,'Ürünlerdeki 3 nötronu saymamış (A = 92); nötron sayısını 56 bulmuş.','dikkat')],
 z='orta',alt='Fisyon',kaz='Çekirdek tepkimesinde kütle ve atom numarasının korunumundan bilinmeyen çekirdeğin nötron sayısını bulur.',kalip='şekilli',sekil=SK,
 istenen='Kr çekirdeğindeki nötron sayısı.',
 ip=['Her iki yanda kütle numaralarının toplamı eşit olmalıdır; nötronları da say.'],
 bilgi=[B('Çekirdek tepkimelerinde korunum','toplam kütle numarası ve toplam atom numarası, tepkimenin iki yanında eşittir. Nötron sayısı = kütle numarası − atom numarası. Örnek: ⁹Be + ⁴He → ¹²C + n için 9 + 4 = 12 + 1 ve 4 + 2 = 6 + 0')],
 puf='Çekirdek denkleminde A ve Z ayrı ayrı korunur; nötron sayısı N = A − Z’dir.')

# =============== 0009 · nükleer enerji · orta · olumsuz kök ===============
d,y,sr=tek([('Fisyon tepkimesinde ağır bir çekirdek, nötron çarpması sonucu daha küçük çekirdeklere bölünür.',False,'Fisyonun tanımına uygun doğru bir ifadeyi yanlış sanmış; ağır çekirdek nötronla bölünür.'),
 ('Zincir tepkimesinin hızı, nötron soğuran kontrol çubuklarıyla ayarlanır.',False,'Reaktörlerde kontrol çubukları nötronları soğurur; doğru bir bilgiyi yanlış saymış.'),
 ('Nükleer santraller çalışırken fosil yakıtlı santraller kadar CO₂ gazı açığa çıkarır.',True,'—'),
 ('Kullanılmış yakıt çubukları radyoaktif atık içerdiğinden uzun süre güvenli biçimde depolanmalıdır.',False,'Nükleer atıkların radyoaktif ve uzun ömürlü olduğunu bilmeyip doğru bir ifadeyi yanlış saymış.'),
 ('Füzyon, hafif çekirdeklerin birleşerek daha ağır bir çekirdek oluşturduğu tepkimedir.',False,'Füzyonun tanımını karıştırıp doğru bir ifadeyi yanlış sanmış.')],
 ['Nükleer santraller çalışırken fosil yakıtlı santraller kadar CO₂ gazı açığa çıkarır.','Fisyon tepkimesinde ağır bir çekirdek, nötron çarpması sonucu daha küçük çekirdeklere bölünür.','Zincir tepkimesinin hızı, nötron soğuran kontrol çubuklarıyla ayarlanır.','Kullanılmış yakıt çubukları radyoaktif atık içerdiğinden uzun süre güvenli biçimde depolanmalıdır.','Füzyon, hafif çekirdeklerin birleşerek daha ağır bir çekirdek oluşturduğu tepkimedir.'])
q('0009','06',[A('Seçenekleri tek tek ele al','Her şık nükleer enerjiyle ilgili bir bilgiyi içerir.','A–E: bilgileri sına'),
 A('Doğru olanları ayıkla','Fisyon, kontrol çubukları, radyoaktif atık ve füzyon tanımları ders kitabı bilgisidir.','4 şık doğru'),
 A('Yanlış ifadeyi bul','Nükleer santrallerde yakıt yanmaz; çekirdek tepkimesi olur ve CO₂ oluşmaz.','Yanlış: CO₂ salımı fosil yakıtlar kadardır')],
 ne='nükleer enerji ile ilgili yanlış ifade',metin='Bir enerji santralinde uranyum çekirdeklerinin bölünmesiyle ısı elde edilir ve bu ısıyla elektrik üretilir.\nBuna göre nükleer enerji ve nükleer santrallerle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=d,sira=sr,yan=y,z='orta',alt='Nükleer Enerji',kaz='Nükleer enerji, fisyon ve füzyon hakkındaki bilgileri doğru–yanlış olarak ayırt eder.',kalip='düz',
 istenen='Yanlış olan ifade.',
 ip=['Nükleer santralde ısının yanma ile mi yoksa çekirdek tepkimesiyle mi elde edildiğini düşün.'],
 bilgi=[B('Fisyon ve füzyon','fisyon ağır bir çekirdeğin nötronla daha küçük çekirdeklere bölünmesi, füzyon hafif çekirdeklerin birleşmesidir; ikisi de çok büyük enerji açığa çıkarır. Örnek: Güneş’te hidrojen çekirdekleri füzyonla helyuma dönüşür')],
 puf='Nükleer santralde ısı yanmadan değil çekirdek tepkimesinden gelir; CO₂ yerine radyoaktif atık sorunu vardır.')

# =============== 0010 · enerji tüketimi payları · orta · öncüllü + tablo ===============
T00,T20=400,500; pay={'Fosil yakıtlar':(80,70),'Nükleer enerji':(10,10),'Yenilenebilir enerji':(10,20)}
mik={k:(Fr(T00*a,100),Fr(T20*b,100)) for k,(a,b) in pay.items()}
assert mik['Fosil yakıtlar']==(320,350) and mik['Nükleer enerji']==(40,50) and mik['Yenilenebilir enerji']==(40,100)
assert mik['Yenilenebilir enerji'][1]/mik['Yenilenebilir enerji'][0]==Fr(5,2)
SK=tablo_svg(['Kaynak','2000 payı (%)','2020 payı (%)'],[[k,str(a),str(b)] for k,(a,b) in pay.items()]+[['Toplam (EJ)',str(T00),str(T20)]])
onc('0010','08','Tabloda, bir ülkenin 2000 ve 2020 yıllarındaki toplam enerji tüketimi (EJ) ile bu tüketimin kaynaklara göre yüzde payları verilmiştir.',
 [('Fosil yakıt tüketimi (EJ) 2000’den 2020’ye azalmıştır.',False,'Fosil yakıt tüketimi 320 EJ’den 350 EJ’ye çıkmıştır; payı azalsa da miktarı artmıştır.','yüzde payının azalmasını tüketim miktarının da azalması saymış.','—'),
  ('Yenilenebilir enerji tüketimi 2020’de 2000’dekinin 2,5 katıdır.',True,'Yenilenebilir tüketim 40 EJ’den 100 EJ’ye çıkmıştır; 100 ÷ 40 = 2,5.','—','payın iki katına çıktığını görüp toplamın da arttığını hesaba katmamış.'),
  ('Nükleer enerji payı sabit kaldığı için nükleer enerji tüketimi de sabit kalmıştır.',False,'Toplam tüketim arttığından nükleer enerji miktarı 40 EJ’den 50 EJ’ye çıkmıştır.','sabit payı sabit miktar sanmış.','—')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],'Buna göre bu ifadelerden hangileri doğrudur?',
 ne='yüzde paylardan miktar karşılaştırması',z='orta',alt='Enerji Tüketimi',kaz='Toplam tüketim ve yüzde paylarından kaynakların tüketim miktarlarını karşılaştırır.',kalip='tablo',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['Her kaynağın EJ cinsinden miktarını toplamla payı çarparak bul.'],
 bilgi=[B('Yüzde pay ve miktar','bir kaynağın miktarı, toplam tüketimle yüzde payının çarpımıdır. Toplam değişirse payı sabit kalan kaynağın miktarı da değişir. Örnek: toplam 200 EJ iken %30 pay 60 EJ eder')],
 puf='Pay (%) miktar değildir; miktarı bulmak için toplamla çarp.')

# =============== 0011 · nano · yüzey alanı · orta · öncüllü + şekil ===============
s=2.0; dx,dy=.8,.55
g=f'\\filldraw[fill=white,thick] (0,0) rectangle ({s},{s}); \\filldraw[fill=vurgu!15,thick] (0,{s}) -- ({s},{s}) -- ({s+dx},{s+dy}) -- ({dx},{s+dy}) -- cycle; \\filldraw[fill=vurgu!30,thick] ({s},0) -- ({s+dx},{dy}) -- ({s+dx},{s+dy}) -- ({s},{s}) -- cycle;'
for i in (1,2):
    t=i*s/3
    g+=f'\\draw[thin] ({t:.3f},0) -- ({t:.3f},{s}); \\draw[thin] (0,{t:.3f}) -- ({s},{t:.3f});'
    g+=f'\\draw[thin] ({t:.3f},{s}) -- ({t+dx:.3f},{s+dy}); \\draw[thin] ({i*dx/3:.3f},{s+i*dy/3:.3f}) -- ({s+i*dx/3:.3f},{s+i*dy/3:.3f});'
    g+=f'\\draw[thin] ({s},{t:.3f}) -- ({s+dx},{t+dy:.3f}); \\draw[thin] ({s+i*dx/3:.3f},{i*dy/3:.3f}) -- ({s+i*dx/3:.3f},{s+i*dy/3:.3f});'
g+=f'\\node[below] at ({s/2},-.05) {{$a$}}; \\draw[{ARR}] ({s/2-.4},-.45) -- ({s/2-.05},-.45)  ;'
g=g.replace(f'\\draw[{ARR}] ({s/2-.4},-.45) -- ({s/2-.05},-.45)  ;','')
g+=f'\\node[align=center] at ({s+dx+2.4},{s/2+.3}) {{Küp, eşit büyüklükte\\\\$3\\times3\\times3=27$ küpe\\\\bölünüyor}};'
SK=tk(g)
a_=Fr(1); S0=6*a_**2; S1=27*6*(a_/3)**2; assert S1/S0==3
V0=a_**3; V1=27*(a_/3)**3; assert V0==V1
onc('0011','10','Şekilde, kenar uzunluğu a olan küp şeklindeki bir madde örneği görülmektedir. Bu örnek, kütlesi ve cinsi değişmeden, kenar uzunluğu a/3 olan 27 eş küçük küpe ayrılıyor.',
 [('Örneğin toplam hacmi değişmez.',True,'Küçük küplerin toplam hacmi 27 × (a/3)³ = a³ olduğundan hacim sabittir.','—','madde miktarı değişmediği hâlde hacmin değiştiğini sanmış.'),
  ('Örneğin toplam yüzey alanı 9 katına çıkar.',False,'Toplam yüzey alanı 27 × 6 × (a/3)² = 18a² olur; ilk değer 6a² olduğundan 3 katına çıkar.','kenar 3’e bölündüğü için yüzey alanının 9 katına çıktığını sanmış.','—'),
  ('Birim kütle başına yüzey alanı artar.',True,'Kütle sabitken yüzey alanı arttığından birim kütle başına yüzey alanı artar.','—','yüzey alanı artışını birim kütleye göre yorumlayamamış.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],'Buna göre bu ifadelerden hangileri doğrudur?',
 ne='küp parçalanınca hacim ve yüzey alanı',z='orta',alt='Nanoteknoloji',kaz='Bir maddenin küçük parçalara ayrılmasıyla hacim ve yüzey alanındaki değişimleri yorumlar.',kalip='şekilli',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['Küçük küplerin toplam hacmini ve toplam yüzey alanını ilk küple karşılaştır.'],
 bilgi=[B('Küpün hacmi ve yüzey alanı','kenarı k olan küpün hacmi k³, yüzey alanı 6k²’dir. Parçalandığında hacim toplamı değişmez, yüzey alanı toplamı artar. Örnek: k = 2 cm ise hacim 8 cm³, yüzey alanı 24 cm²’dir')],
 puf='Parçalanınca toplam hacim sabit kalır, toplam yüzey alanı artar; nano ölçekte tepkime yüzeyinde gerçekleşir.')

# =============== 0012 · nano tablo · orta · öncüllü ===============
NU={'A':(100,30),'B':(50,60),'C':(10,300)}
assert NU['C'][1]/NU['A'][1]==10 and NU['A'][0]*NU['A'][1]==3000 and NU['B'][0]*NU['B'][1]==3000 and NU['C'][0]*NU['C'][1]==3000
SK=tablo_svg(['Numune','Kenar uzunluğu (nm)','Yüzey alanı (m²/g)'],[[k,str(a),str(b)] for k,(a,b) in NU.items()])
onc('0012','10','Aynı maddenin küp şeklindeki parçacıklarından oluşan A, B ve C numunelerinin kenar uzunlukları ile birim kütle başına yüzey alanları tabloda verilmiştir.',
 [('Parçacık boyutu küçüldükçe bir parçacıktaki atom sayısı artar.',False,'Küçük parçacıkta atom sayısı azdır; boyut küçüldükçe parçacıktaki atom sayısı azalır.','boyutu küçük parçacıkta daha çok atom bulunduğunu sanmış.','—'),
  ('C numunesinin 1 g’ı, A numunesinin 1 g’ına göre 10 kat daha geniş yüzeyle temas eder.',True,'Tabloya göre 300 ÷ 30 = 10 olduğundan C’nin yüzey alanı A’nınkinin 10 katıdır.','—','tablodaki yüzey alanı değerlerini oranlayamamış.'),
  ('Aynı koşullarda, aynı kütledeki C numunesi A numunesinden daha hızlı tepkime verir.',True,'Yüzey alanı büyük olan numunede temas yüzeyi fazladır; tepkime hızı artar.','—','yüzey alanı ile tepkime hızı arasındaki ilişkiyi bilmiyor.')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],'Buna göre bu ifadelerden hangileri doğrudur?',
 ne='nano parçacıkta boyut, yüzey alanı ve tepkime hızı',z='orta',alt='Nanoteknoloji',kaz='Tablodan boyut–yüzey alanı ilişkisini yorumlayıp tepkime hızına etkisini belirler.',kalip='tablo',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['Tabloda boyut küçüldükçe yüzey alanının nasıl değiştiğine bak ve bunu tepkime hızıyla ilişkilendir.'],
 bilgi=[B('Nanoparçacıklar','boyutları 1–100 nm arasında olan taneciklerdir (1 nm = 10⁻⁹ m). Boyut küçüldükçe birim kütle başına yüzey alanı artar; katı maddeler yüzeylerinde tepkimeye girdiğinden tepkime hızı artar. Örnek: toz hâldeki katı, bloğa göre daha hızlı yanar')],
 puf='Boyut küçülür, birim kütlenin yüzey alanı artar, tepkime hızı artar.')

# =============== 0013 · sınırlayıcı + yanma ısısı · zor · tanecik ===============
nC,nO=3,4; mol_t=Fr(1,2); dH13=Fr(-800)
CH=Fr(nC); OO=Fr(nO)
yan_CH=min(CH,OO/2); assert yan_CH==2
Q13=-dH13*yan_CH*mol_t; assert Q13==800
z1=-dH13*CH*mol_t; z2=-dH13*(OO*mol_t); z3=-dH13*nC; z4=-dH13*yan_CH*mol_t/2
assert (z1,z2,z3,z4)==(1200,1600,2400,400) and len({Q13,z1,z2,z3,z4})==5
def ch4(x,y): 
    r=f'\\filldraw[fill=gray!35,draw=black] ({x},{y}) circle (.2);'
    for ax,ay in ((.28,.28),(-.28,.28),(.28,-.28),(-.28,-.28)): r+=f'\\filldraw[fill=white,draw=black] ({x+ax:.2f},{y+ay:.2f}) circle (.1); \\draw ({x+ax*.55:.2f},{y+ay*.55:.2f}) -- ({x+ax*.8:.2f},{y+ay*.8:.2f});'
    return r
def o2(x,y): return f'\\filldraw[fill=red!40,draw=black] ({x-.17},{y}) circle (.19); \\filldraw[fill=red!40,draw=black] ({x+.17},{y}) circle (.19);'
g='\\draw[thick,rounded corners=3pt] (0,0) rectangle (6.4,2.6);'
for (x,y) in ((.9,1.9),(2.7,.8),(4.1,2.0)): g+=ch4(x,y)
for (x,y) in ((1.4,.6),(3.4,1.6),(5.1,.8),(5.4,2.0)): g+=o2(x,y)
g+=f'\\draw[thick,fill=gray!35] (.2,-.7) circle (.14); \\node[right] at (.4,-.7) {{\\ce{{CH4}}}}; \\filldraw[fill=red!40,draw=black] (2.0,-.7) circle (.14); \\filldraw[fill=red!40,draw=black] (2.28,-.7) circle (.14); \\node[right] at (2.5,-.7) {{\\ce{{O2}}}};'
SK=tk(g)
q('0013','02',[A('Taneciklerin mol karşılığı','Her tanecik 0,5 mol temsil eder; şekilde 3 CH₄ ve 4 O₂ vardır.','CH₄: 3 × 0,5 = 1,5 mol · O₂: 4 × 0,5 = 2 mol'),
 A('Sınırlayıcı bileşeni bul','1 mol CH₄ için 2 mol O₂ gerekir; 2 mol O₂ ancak 1 mol CH₄ ile tepkimeye girer.','O₂ sınırlayıcıdır; CH₄: 2 ÷ 2 = 1 mol harcanır'),
 A('Isıyı hesapla','ΔH, denklemdeki 1 mol CH₄ için verilmiştir; harcanan CH₄ mol sayısıyla çarpılır.','1 × 800 = 800 kJ')],
 ne='tanecik modelinden sınırlayıcı bileşene göre açığa çıkan ısı',metin='Şekildeki sabit hacimli kapta CH₄ ve O₂ gazlarının tanecik modeli verilmiştir; her bir tanecik 0,5 mol maddeyi temsil etmektedir. Kapta aşağıdaki tepkime tam verimle gerçekleşmektedir.\nCH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g)    ΔH = −800 kJ\nBuna göre tepkime sonunda açığa çıkan ısı kaç kJ’dir?',
 dogru=Q13,yan=[(z1,'CH₄’ün tamamının (1,5 mol) yandığını varsaymış; O₂’nin sınırlayıcı olduğunu görmemiş.','dikkat'),(z2,'O₂’nin mol sayısıyla (2 mol) ΔH’ı çarpmış; ΔH’ın 1 mol CH₄ için verildiğini hesaba katmamış.','bilgi'),(z3,'Tanecik sayısını mol sanmış (3 mol); her taneciğin 0,5 mol olduğunu atlamış.','dikkat'),(z4,'Yanan CH₄’ü 0,5 mol almış; 2 mol O₂’nin 1 mol CH₄ ile tepkimeye girdiğini bulamamış.','islem')],
 z='zor',alt='Yanma Isısı',kaz='Tanecik modelinden sınırlayıcı bileşeni bulup yanma entalpisiyle açığa çıkan ısıyı hesaplar.',kalip='şekilli',sekil=SK,
 istenen='Tepkimede açığa çıkan ısı (kJ).',
 ip=['Önce hangi gazın daha önce biteceğini mol sayılarına göre belirle.'],
 bilgi=[B('Sınırlayıcı bileşen','tepkimede önce biten ve ürün miktarını belirleyen maddedir; denklemin katsayı oranıyla karşılaştırılarak bulunur. Örnek: N₂ + 3H₂ → 2NH₃ tepkimesinde 1 mol N₂ ve 2 mol H₂ varsa H₂ sınırlayıcıdır')],
 puf='Isıyı sınırlayıcı bileşene göre hesapla; ΔH’ı yanan 1 mol CH₄ ile ilişkilendir.')

# =============== 0014 · karbon ayak izi sıralama · zor · tablo ===============
YK={'C(grafit)':(1,400),'CH₄':(1,900),'C₂H₅OH':(2,1350)}
Q_=10800; yk_mol={k:Fr(Q_,e) for k,(c,e) in YK.items()}; co2={k:yk_mol[k]*YK[k][0] for k in YK}
assert yk_mol=={'C(grafit)':27,'CH₄':12,'C₂H₅OH':8} and co2=={'C(grafit)':27,'CH₄':12,'C₂H₅OH':16}
dogru_s=' < '.join(sorted(co2,key=co2.get)); assert dogru_s=='CH₄ < C₂H₅OH < C(grafit)'
e1=' < '.join(sorted(YK,key=lambda k:YK[k][1])); e2=' < '.join(sorted(yk_mol,key=yk_mol.get)); e3=' < '.join(sorted(co2,key=co2.get,reverse=True))
assert (e1,e2,e3)==('C(grafit) < CH₄ < C₂H₅OH','C₂H₅OH < CH₄ < C(grafit)','C(grafit) < C₂H₅OH < CH₄')
e4='CH₄ < C(grafit) < C₂H₅OH'; assert len({dogru_s,e1,e2,e3,e4})==5
SK=tablo_svg(['Yakıt','Yanma entalpisi (kJ/mol)'],[[k,'−'+str(e)] for k,(c,e) in YK.items()])
q('0014','07',[A('Yakılan mol sayılarını bul','10800 kJ ısı için gereken yakıt mol sayısı, ısının yanma entalpisine oranıdır.','C: 10800 ÷ 400 = 27 · CH₄: 10800 ÷ 900 = 12 · C₂H₅OH: 10800 ÷ 1350 = 8'),
 A('CO₂ mol sayısına geç','Her yakıtın formülündeki C sayısı kadar CO₂ oluşur.','C: 27 × 1 = 27 · CH₄: 12 × 1 = 12 · C₂H₅OH: 8 × 2 = 16'),
 A('Sırala','CO₂ miktarı küçükten büyüğe dizilir.','CH₄ < C₂H₅OH < C')],
 ne='aynı ısı için üç yakıtın CO₂ salımı sıralaması',metin='Tabloda, üç yakıtın yaklaşık yanma entalpisi (1 mol yakıtın tam yanması için) verilmiştir.\nBu yakıtlardan her biri ile ayrı ayrı 10800 kJ ısı elde edilmek üzere tam yakılıyor.\nBuna göre oluşan CO₂ mol sayılarının küçükten büyüğe sıralaması aşağıdakilerden hangisidir?',
 dogru=dogru_s,sira=['C(grafit) < C₂H₅OH < CH₄','CH₄ < C(grafit) < C₂H₅OH','C₂H₅OH < CH₄ < C(grafit)','CH₄ < C₂H₅OH < C(grafit)','C(grafit) < CH₄ < C₂H₅OH'],
 yan=[(e1,'Yanma entalpisinin büyüklüğüne göre sıralamış; daha çok ısı veren yakıtın daha çok CO₂ verdiğini sanmış.','bilgi'),(e2,'Yakılan yakıt mol sayısına (8, 12, 27) göre sıralamış; formüldeki C sayısını katmamış.','dikkat'),(e3,'Doğru sıralamayı ters yazmış; en çok ve en az CO₂ veren yakıtı karıştırmış.','dikkat'),(e4,'Yalnız 1 mol yakıttan oluşan CO₂’ye bakıp C₂H₅OH’ı en çok CO₂ veren saymış; ısı için yakılan miktar farkını hesaba katmamış.','bilgi')],
 z='zor',alt='Karbon Ayak İzi',kaz='Yanma entalpisi ve formülden aynı ısı için oluşan CO₂ miktarlarını karşılaştırır.',kalip='tablo',sekil=SK,
 istenen='Oluşan CO₂ mol sayılarının küçükten büyüğe sıralaması.',
 ip=['Aynı ısı için her yakıttan kaç mol yakıldığını, sonra formülünden kaç mol CO₂ oluştuğunu bul.'],
 bilgi=[B('Tam yanmada CO₂','karbon içeren bir yakıtın tam yanmasında formüldeki her C atomu bir CO₂ molekülü verir. Örnek: C₃H₆ tam yanarsa 1 molünden 3 mol CO₂ oluşur')],
 puf='Önce yakılan yakıt molünü, sonra formüldeki C sayısıyla CO₂ molünü bul.')

# =============== 0015 · yakıt pili verimi · zor · şekil ===============
dH15=Fr(572); m15=Fr(4); M15=Fr(2); eta15=Fr(6,10); Pw=40
n15=m15/M15; rx=n15/2; E15=rx*dH15*eta15; t15=E15*1000/Pw
assert (n15,rx,E15,t15)==(2,1,Fr(1716,5),8580)
v1=(m15/4)/2*dH15*eta15*1000/Pw; v2=rx*dH15*1000/Pw; v3=n15*dH15*eta15*1000/Pw; v4=n15*dH15*1000/Pw
assert (v1,v2,v3,v4)==(4290,14300,17160,28600) and len({t15,v1,v2,v3,v4})==5
g=f'\\node[draw,rounded corners,minimum width=2.0cm,minimum height=1.1cm,align=center] (t) at (0,0) {{\\ce{{H2}} deposu}};'
g+='\\node[draw,rounded corners,fill=vurgu!15,minimum width=2.6cm,minimum height=1.1cm,align=center] (p) at (3.9,0) {Yakıt pili};'
g+='\\draw[thick] (7.6,0) circle (.5); \\draw[thick] (7.25,-.35) -- (7.95,.35); \\draw[thick] (7.25,.35) -- (7.95,-.35); \\node[below] at (7.6,-.55) {Lamba: 40 W};'
g+=f'\\draw[{ARR},thick] (t) -- node[above]{{\\ce{{H2}}}} (p); \\draw[{ARR},thick] (p) -- node[above]{{elektrik}} (7.1,0);'
g+=f'\\draw[{ARR},thick,gray!60!black] (3.9,-.55) -- (3.9,-1.5); \\node[below] at (3.9,-1.5) {{ısı kaybı}};'
SK=tk(g)
q('0015','09',[A('H₂ mol sayısını bul','Mol sayısı kütlenin mol kütlesine bölümüdür.','4 ÷ 2 = 2 mol H₂'),
 A('Tepkime sayısını bul','ΔH, denklemdeki 2 mol H₂ için verilmiştir.','2 mol H₂ = 1 tepkime → 572 kJ'),
 A('Elektrik enerjisini bul','Pil, açığa çıkan enerjinin yalnız %60’ını elektriğe dönüştürür.','572 × 0,6 = 343,2 kJ = 343200 J'),
 A('Süreyi hesapla','Güç, birim zamandaki enerjidir; 1 W = 1 J/s.','343200 ÷ 40 = 8580 s')],
 ne='yakıt pilinin verimli enerjisiyle lambanın yanma süresi',metin='Şekilde, hidrojen yakıt pili ile çalıştırılan bir lamba görülmektedir. Pilde 4 g H₂ gazı tamamen tüketiliyor ve H₂’nin O₂ ile tepkimesinden açığa çıkabilecek enerjinin %60’ı elektrik enerjisine dönüşüyor (H: 1, 1 W = 1 J/s).\n2H₂(g) + O₂(g) → 2H₂O(s)    ΔH = −572 kJ\nBu enerji lambaya eksiksiz aktarıldığına göre lamba kaç saniye yanar?',
 dogru=t15,yan=[(v1,'H₂’nin mol kütlesini 4 alıp 1 mol H₂ bulmuş; ΔH’ın yarısını kullanmış.','islem'),(v2,'Elektrik enerjisinin %60 olduğunu hesaba katmamış; açığa çıkabilecek enerjinin tamamını almış.','dikkat'),(v3,'ΔH’ı her 1 mol H₂ için almış (2 × 572 kJ); denklemdeki katsayıyı hesaba katmamış.','bilgi'),(v4,'Hem katsayıyı hesaba katmamış hem de verimi uygulamamış (2 × 572 kJ).','dikkat')],
 z='zor',alt='Yakıt Pilleri',kaz='Yakıt pilinde tüketilen yakıtın enerjisinden verimle elektrik enerjisini bulup süreye çevirir.',kalip='şekilli',sekil=SK,
 istenen='Lambanın yanma süresi (s).',
 ip=['ΔH’ın kaç mol H₂ için verildiğine ve enerjinin ne kadarının elektriğe dönüştüğüne dikkat et.'],
 bilgi=[B('Güç ve enerji','güç, birim zamanda aktarılan enerjidir: P = E ÷ t; 1 W = 1 J/s. Örnek: 10 W’lık lamba 100 J enerjiyi 10 s’de harcar'),B('Yakıt pili verimi','verim = elektrik enerjisi ÷ yakıtın tepkimesinden açığa çıkan enerjidir. Örnek: 200 kJ enerjiden %25 verimle 50 kJ elektrik elde edilir')],
 puf='Önce H₂’nin mol–katsayı oranından enerjiyi, sonra verimi, en son t = E ÷ P ilişkisini kullan.')

# =============== 0016 · karışımın yanma ısısı · zor ===============
dH_H=Fr(300); dH_C=Fr(900); ntop=Fr(1); Qk=Fr(540)
x_H=(dH_C*ntop-Qk)/(dH_C-dH_H); assert x_H==Fr(3,5)
n_C=ntop-x_H; mC=n_C*16; assert mC==Fr(32,5) and dH_H*x_H+dH_C*n_C==Qk
w1=x_H*2; w2=x_H*16; w3=Fr(1,2)*16; w4=Qk/((dH_H+dH_C)/2)*16
assert (w1,w2,w3,w4)==(Fr(6,5),Fr(48,5),8,Fr(72,5)) and len({mC,w1,w2,w3,w4})==5
q('0016','02',[A('Mol sayılarını tanımla','H₂ mol sayısına x dersek CH₄ için 1 − x olur.','n(H₂) = x ; n(CH₄) = 1 − x'),
 A('Isı denklemini kur','Toplam ısı, her yakıtın mol sayısı ile yanma entalpisinin çarpımlarının toplamıdır.','300x + 900(1 − x) = 540'),
 A('Denklemi çöz','Sadeleştirilince x bulunur.','900 − 600x = 540 → x = 0,6 mol H₂'),
 A('CH₄ kütlesini bul','CH₄ mol sayısı 1 − 0,6 = 0,4 mol; kütle mol sayısı ile mol kütlesinin çarpımıdır.','0,4 × 16 = 6,4 g')],
 ne='karışımın yanma ısısından CH₄ kütlesi',metin='H₂(g) ve CH₄(g)’nin yaklaşık yanma entalpileri sırasıyla −300 kJ/mol ve −900 kJ/mol’dür.\nToplam 1 mol olan H₂ ve CH₄ gazları karışımı tamamen yakıldığında 540 kJ ısı açığa çıkıyor (H: 1, C: 12).\nBuna göre karışımdaki CH₄ gazı kaç gramdır?',
 dogru=mC,yan=[(w1,'Karışımdaki H₂ mol sayısı (0,6) ile H₂’nin mol kütlesini (2) çarpmış; CH₄ yerine H₂’nin kütlesini bulmuş.','dikkat'),(w2,'CH₄ mol sayısı yerine H₂ mol sayısını (0,6) CH₄’ün mol kütlesiyle çarpmış.','islem'),(w3,'Isıyı hesaba katmadan karışımın yarısının CH₄ olduğunu (0,5 mol) varsaymış.','bilgi'),(w4,'Ortalama yanma entalpisiyle (600 kJ/mol) 0,9 mol bulup tamamını CH₄ saymış.','bilgi')],
 z='zor',alt='Yanma Isısı',kaz='İki yakıt karışımının toplam yanma ısısından bileşenlerin mol sayısını ve kütlesini bulur.',kalip='düz',
 istenen='Karışımdaki CH₄ gazının kütlesi (g).',
 ip=['Bilinmeyen mol sayısı için bir denklem kur; toplam mol sayısı ile toplam ısıyı kullan.'],
 bilgi=[B('Karışımın yanma ısısı','karışımın verdiği toplam ısı, bileşenlerin mol sayıları ile yanma entalpilerinin çarpımları toplamına eşittir. Örnek: 2 mol X (50 kJ/mol) ile 1 mol Y (80 kJ/mol) toplam 180 kJ verir')],
 puf='Karışım sorularında mol sayısı için x ve (toplam − x) yazıp ısı toplamıyla denklem kur.')

# =============== 0017 · araç CO2 · ağaç · zor · şekil ===============
mk100=Fr(32,10)*1000; km=10000; yil=Fr(km,100)*mk100; nCH=yil/16; mCO2=nCH*44/1000; agac=mCO2/16
assert (nCH,mCO2,agac)==(20000,880,55)
a1=Fr(100,100)*mk100/16*44/1000/16; a2=yil/1000/16; a3=nCH*32/1000/16; a4=nCH*2*44/1000/16
assert (a1,a2,a3,a4)==(Fr(11,20),20,40,110) and len({agac,a1,a2,a3,a4})==5
g='\\node[draw,rounded corners,minimum width=2.6cm,minimum height=1.4cm,align=center] (a) at (0,0) {Araç\\\\100 km yolda\\\\3,2 kg \\ce{CH4}};'
g+='\\node[draw,rounded corners,fill=vurgu!15,minimum width=2.6cm,minimum height=1.4cm,align=center] (b) at (5.2,0) {Atmosfere\\\\\\ce{CO2} karışır};'
g+='\\node[draw,rounded corners,minimum width=2.6cm,minimum height=1.4cm,align=center] (c) at (5.2,-2.5) {Bir ağaç\\\\yılda 16 kg \\ce{CO2}\\\\bağlar};'
g+=f'\\draw[{ARR},thick] (a) -- node[above]{{tam yanma}} (b); \\draw[{ARR},thick] (c) -- node[right]{{tutma}} (b);'
SK=tk(g)
q('0017','07',[A('Yıllık yakıt kütlesini bul','10 000 km, 100 km’nin 100 katıdır.','100 × 3,2 = 320 kg CH₄'),
 A('CH₄ mol sayısını bul','Kütle gramla mol kütlesine bölünür.','320000 ÷ 16 = 20000 mol'),
 A('CO₂ miktarını bul','CH₄ + 2O₂ → CO₂ + 2H₂O denkleminde 1 mol CH₄’ten 1 mol CO₂ oluşur.','20000 × 44 = 880000 g = 880 kg'),
 A('Ağaç sayısını bul','Toplam CO₂ bir ağacın yıllık bağladığı miktara bölünür.','880 ÷ 16 = 55')],
 ne='aracın yıllık CO₂ salımını bağlamak için gereken ağaç sayısı',metin='Şekilde, doğal gazla (CH₄) çalışan bir aracın yakıt tüketimi ile bir ağacın bir yılda bağladığı CO₂ miktarı verilmiştir. Araç yılda 10 000 km yol yapıyor ve yakıtı tam yanıyor (H: 1, C: 12, O: 16).\nBuna göre aracın bir yılda atmosfere verdiği CO₂’yi bağlamak için kaç ağaç gerekir?',
 dogru=agac,yan=[(a1,'Yalnız 100 km’lik yol için hesaplamış; yıllık 10 000 km’yi hesaba katmamış.','dikkat'),(a2,'CH₄’ün kütlesini (320 kg) CO₂ kütlesi sanmış; mol–kütle dönüşümü yapmamış.','bilgi'),(a3,'CO₂’nin mol kütlesini 32 almış; oluşan CO₂ kütlesini eksik bulmuş.','islem'),(a4,'1 mol CH₄’ten 2 mol CO₂ oluştuğunu sanmış; denklem katsayısını yanlış kullanmış.','bilgi')],
 z='zor',alt='Karbon Ayak İzi',kaz='Yakıt tüketiminden oluşan CO₂ kütlesini mol–kütle ilişkisiyle bulup karbon ayak izini yorumlar.',kalip='şekilli',sekil=SK,
 istenen='Gereken ağaç sayısı.',
 ip=['Önce bir yılda yakılan CH₄’ü mol olarak bul; sonra oluşan CO₂’yi kütleye çevir.'],
 bilgi=[B('Yanmadan oluşan CO₂','C içeren yakıtta karbon atomu sayısı kadar CO₂ oluşur; CO₂ kütlesi mol sayısı ile 44 g/mol’ün çarpımıdır. Örnek: 2 mol CH₄’ten 2 mol CO₂, yani 88 g CO₂ oluşur')],
 puf='Kütle → mol → denklem oranı → kütle zincirini kur; en sonda birimleri (g, kg) eşitle.')

# =============== 0018 · yarı ömür · orta · grafik ===============
m0=80; hl=12; pts=[(t,Fr(m0)/2**Fr(t,hl)) for t in (0,12,24,36)]
assert [float(p[1]) for p in pts]==[80,40,20,10]
N0=320; Nf=5; k=Fr(N0,Nf); assert k==64
nh=int(math.log2(k)); assert 2**nh==64; tt=nh*hl; assert tt==72
o1=hl; o2=(nh-1)*hl; o3=nh; o4=int(k)
assert (o2,o3,o4)==(60,6,64) and len({tt,o1,o2,o3,o4})==5
sx=.17; sy=.036
g=f'\\draw[{ARR},thick] (0,0) -- (0,{80*sy+.6:.3f}); \\draw[{ARR},thick] (0,0) -- ({36*sx+.8:.3f},0);'
for v in (10,20,40,80):
    yy=v*sy; g+=f'\\draw (0,{yy:.3f}) -- (-.08,{yy:.3f}); \\node[left,inner sep=2pt] at (-.05,{yy:.3f}) {{{v}}}; \\draw[gray!60,dashed] (0,{yy:.3f}) -- ({36*sx:.3f},{yy:.3f});'
for t in (12,24,36):
    g+=f'\\draw ({t*sx:.3f},0) -- ({t*sx:.3f},-.08); \\node[below,inner sep=2pt] at ({t*sx:.3f},-.05) {{{t}}}; \\draw[gray!60,dashed] ({t*sx:.3f},0) -- ({t*sx:.3f},{80*sy:.3f});'
g+='\\node[below,inner sep=2pt] at (0,-.05) {0};'
cp=' '.join(f'({t*sx:.3f},{float(m0)/2**(t/hl)*sy:.3f})' for t in range(0,37,3))
g+=f'\\draw[vurgu,very thick] plot[smooth] coordinates {{{cp}}};'
for t in (0,12,24,36): g+=f'\\fill[vurgu!70!black] ({t*sx:.3f},{float(m0)/2**(t/hl)*sy:.3f}) circle (.07);'
g+=f'\\node[rotate=90] at (-1.1,{40*sy:.3f}) {{Kalan kütle (g)}}; \\node[below] at ({18*sx:.3f},-.5) {{Zaman (yıl)}};'
SK=tk(g)
q('0018','06',[A('Yarı ömrü oku','Kütlenin 80 g’dan 40 g’a düştüğü süre yarı ömürdür.','t½ = 12 yıl'),
 A('Kütle oranını bul','Başlangıç kütlesi kalan kütleye bölünür.','320 ÷ 5 = 64'),
 A('Yarı ömür sayısını bul','Her yarı ömürde kütle yarıya iner; 2ⁿ = 64 olur.','2⁶ = 64 → n = 6'),
 A('Süreyi hesapla','Süre yarı ömür sayısı ile yarı ömrün çarpımıdır.','6 × 12 = 72 yıl')],
 ne='grafikten yarı ömür ve kalan kütle için gereken süre',metin='Şekilde, radyoaktif bir X izotopunun bir örneğinde kalan X kütlesinin zamanla değişimi verilmiştir.\nBuna göre aynı izotopun 320 g’lık bir örneğinin kütlesinin 5 g’a düşmesi için kaç yıl geçmelidir?',
 dogru=tt,yan=[(o1,'Yarı ömrü (12 yıl) süre olarak yazmış; kütlenin birden çok kez yarılandığını görmemiş.','dikkat'),(o2,'Yarı ömür sayısını 5 bulmuş; 320 g’ın 5 g’a inmesi için 6 yarılanma gerektiğini atlamış.','islem'),(o3,'Yarılanma sayısını (6) süre olarak yazmış; her yarılanmanın 12 yıl sürdüğünü hesaba katmamış.','dikkat'),(o4,'Kütle oranını (64) doğrudan süre olarak yazmış; yarılanma sayısını bulmamış.','bilgi')],
 z='orta',alt='Radyoaktiflik',kaz='Kalan kütle–zaman grafiğinden yarı ömrü okuyup belirli bir kütle azalması için gereken süreyi bulur.',kalip='grafik',sekil=SK,
 istenen='320 g’ın 5 g’a düşme süresi (yıl).',
 ip=['Önce grafikten kütlenin kaç yılda yarıya indiğini oku; sonra kaç kez yarılanması gerektiğini bul.'],
 bilgi=[B('Yarı ömür','radyoaktif bir örneğin yarısının bozunması için geçen sabit süredir; n yarı ömür sonunda kalan kütle ilk kütlenin 1/2ⁿ’sidir. Örnek: 5 yıl yarı ömürlü bir örnekte 15 yıl sonra kütle 1/8’e iner')],
 puf='Yarı ömür sabittir; kalan kesir 1/2ⁿ olduğundan önce n’yi bul, sonra n × t½ hesapla.')

# =============== 0019 · alternatif enerji · orta · olumsuz öncüllü ===============
onc('0019','05','Gelecekte fosil yakıtların yerine kullanılabilecek alternatif enerji kaynakları ve yakıtlar üzerinde çalışılmaktadır.',
 [('Hidrojen gazı yakıt olarak yandığında ürün olarak yalnızca su oluşur.',False,'H₂ yandığında karbon içermediği için CO₂ oluşmaz; ürün H₂O’dur.','doğru bir ifadeyi yanlış saymış; hidrojenin yanmasını karbon içeren yakıtlarla karıştırmış.','—'),
  ('Biyokütleden elde edilen yakıtlar yandığında oluşan CO₂, bitkilerin fotosentezle bağladığı CO₂ ile dengelenebildiği için net salımı düşük kabul edilir.',False,'Biyokütlenin büyümesi sırasında CO₂ bağlandığından net salım fosil yakıtlara göre düşüktür.','doğru bir ifadeyi yanlış saymış; fotosentezle bağlanan CO₂’yi hesaba katmamış.','—'),
  ('Jeotermal enerji, yer kabuğundaki fosil yakıtların yanmasıyla açığa çıkan ısıdır.',True,'Jeotermal enerji yerin derinliklerindeki sıcak su ve buhardan gelir; yanma olayı yoktur.','yanlış bir ifadeyi doğru saymış; jeotermal ısının kaynağını fosil yakıt yanması sanmış.','—')],
 ['Yalnız III','I ve II','I ve III','II ve III','I, II ve III'],'Buna göre bu ifadelerden hangileri yanlıştır?',
 fiil=('yanlış','doğru'),ne='alternatif enerji kaynakları hakkında yanlış ifadeler',z='orta',alt='Alternatif Enerji',kaz='Hidrojen, biyokütle ve jeotermal enerji hakkındaki ifadeleri doğru–yanlış olarak ayırt eder.',kalip='öncüllü',
 istenen='Yanlış olan ifadeler.',
 ip=['Her kaynağın enerjiyi nasıl sağladığını ve yanma ürününü düşün.'],
 bilgi=[B('Alternatif enerji kaynakları','hidrojen, biyokütle (biyoetanol, biyodizel) ve jeotermal gibi kaynaklardır. Hidrojenin yanma ürünü sudur; jeotermal enerji yer ısısından gelir. Örnek: 2H₂ + O₂ → 2H₂O')],
 puf='Yanlış ifadeyi ararken her kaynağın enerjisinin nereden geldiğine ve yanma ürününe bak.')

# =============== 0020 · güneş kolektörü · zor · şekil ===============
I20=Fr(8,10); A20=Fr(5,2); eta20=Fr(1,2); t20=3600; msu=60; c20=4; T020=20
Qk20=I20*A20*eta20*t20; dT=Qk20*1000/(msu*1000*c20); Tf=T020+dT
assert (Qk20,dT,Tf)==(3600,Fr(15,1),35)
u1=dT; u2=T020+I20*1*eta20*t20*1000/(msu*1000*c20); u3=T020+I20*A20*t20*1000/(msu*1000*c20); u4=T020+Qk20/2*1000/(msu*1000*c20)
assert (u2,u3,u4)==(26,50,Fr(55,2)) and len({Tf,u1,u2,u3,u4})==5
g='\\draw[thick,fill=gray!15] (0,3.6) circle (.55); '
for a in range(-60,61,40): g+=f'\\draw[thick] ({.55*math.cos(math.radians(a)):.3f},{3.6+.55*math.sin(math.radians(a)):.3f}) -- ({.8*math.cos(math.radians(a)):.3f},{3.6+.8*math.sin(math.radians(a)):.3f});'
g+='\\fill[vurgu!35,draw=black,thick] (1.5,1.0) -- (4.5,1.7) -- (4.5,2.0) -- (1.5,1.3) -- cycle;'
for k_ in range(3):
    x=2.0+k_*1.1; y=1.3+(x-1.5)*.2333
    g+=f'\\draw[{ARR},thick,vurgu] ({x-.9:.2f},{y+1.5:.2f}) -- ({x:.2f},{y+.05:.2f});'
g+='\\node[right,align=center] at (3.9,3.1) {Işınım şiddeti:\\\\0,8 kW/m$^2$}; \\node[below,align=center] at (3.0,.95) {Kolektör alanı: 2,5 m$^2$};'
g+='\\draw[thick] (4.5,1.5) -- (5.5,1.5) -- (5.5,.5) -- (6.0,.5); \\draw[thick,fill=vurgu!15] (6.0,-.6) rectangle (8.4,1.4); \\fill[white] (6.02,1.2) rectangle (8.38,1.38); \\draw[thick] (6.0,1.4) -- (8.4,1.4);'
g+='\\node[align=center] at (7.2,.4) {60 kg su\\\\20 °C};'
SK=tk(g)
q('0020','04',[A('Kolektöre gelen gücü bul','Güç, ışınım şiddeti ile alanın çarpımıdır.','0,8 × 2,5 = 2 kW'),
 A('Suya aktarılan enerjiyi bul','Gücün yarısı suya geçer; 1 saat = 3600 s ve 1 kW = 1 kJ/s.','2 × 0,5 × 3600 = 3600 kJ'),
 A('Sıcaklık artışını hesapla','q = m × c × ΔT bağıntısında m = 60000 g, c = 4 J/g·°C alınır.','3600000 ÷ (60000 × 4) = 15 °C'),
 A('Son sıcaklığı yaz','Artış başlangıç sıcaklığına eklenir.','20 + 15 = 35 °C')],
 ne='güneş kolektörüyle ısıtılan suyun son sıcaklığı',metin='Şekilde, ışınım şiddeti 0,8 kW/m² olan güneş ışığını toplayan bir güneş kolektörü ve ona bağlı 20 °C’de 60 kg su içeren depo görülmektedir. Kolektöre gelen enerjinin yalnızca %50’si suya aktarılıyor ve 1 saat boyunca ısıtma yapılıyor.\nSuyun öz ısısı 4 J/g·°C ve 1 kW = 1 kJ/s olduğuna göre depodaki suyun son sıcaklığı kaç °C olur?',
 dogru=Tf,yan=[(u1,'Sıcaklık artışını (15 °C) son sıcaklık sanmış; başlangıç sıcaklığını eklememiş.','dikkat'),(u2,'Kolektör alanını hesaba katmamış (1 m² almış); bu yüzden enerjiyi eksik bulmuş.','dikkat'),(u3,'%50 aktarım verimini uygulamamış; gelen enerjinin tamamının suya geçtiğini varsaymış.','dikkat'),(u4,'Aktarım verimini iki kez uygulamış (%50 ve yine yarısı); suya geçen enerjiyi eksik bulmuş.','islem')],
 z='zor',alt='Güneş Enerjisi',kaz='Güneş kolektörüne gelen enerjiyi verimle suya aktarıp sıcaklık değişimini ve son sıcaklığı hesaplar.',kalip='şekilli',sekil=SK,
 istenen='Suyun son sıcaklığı (°C).',
 ip=['Önce kolektöre gelen gücü ve 1 saatte suya geçen enerjiyi bul.'],
 bilgi=[B('Güneş enerjisi ve ısı','güneş kolektörü, ışınım enerjisini ısıya çevirerek suyu ısıtır. Gelen enerji = ışınım şiddeti × alan × süredir; suya geçen kısım verimle bulunur. Örnek: 1 kW’lık güç 10 s’de 10 kJ enerji aktarır')],
 puf='Sıra: güç → verim → enerji → q = m·c·ΔT → son sıcaklık.')

# ---------------- bitir ----------------
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(AD,'enerjikay-1.json'),'/tmp/bos-enerjikay.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Kimya çıkmış soruları, MEB 11–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
 open(os.path.join(AD,'..','kartlar','akenerjikay.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'soru',len(P.ANA))
for q_ in P.ANA: print(q_['id'][-4:],q_['cevap']['sik'],q_['zorluk'],list(q_['siklar'].values()) if len(str(q_['siklar']))<150 else '')
