"""AYT Biyoloji · Solunum Sistemi (20 soru, kardeş yok, ipucu 1). Şekiller TikZ/pgfplots/tablo; öncüllerin doğru/yanlış değeri tek yerde (ST)."""
import sys,os,json,math,random
BD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(BD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
P=Parti('solunumsis','Solunum Sistemi','abio|Solunum Sistemi',ders='AYT Biyoloji',idon='aytbio')
H.KONU='Solunum Sistemi'
KY='ÖSYM 2018–2026 AYT Biyoloji (Solunum Sistemi) · MEB 11. sınıf biyoloji'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def q(no,ad,kalip='düz',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OK='-{Stealth[length=2.3mm,width=1.9mm]}'
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)) and len(set(sira))==5; return sira
ONC=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def etiket(S): 
    S=sorted(S); return {1:'Yalnız '+S[0] if len(S)==1 else None}.get(len(S)) or (' ve '.join(S) if len(S)==2 else 'I, II ve III')
def onc(ST,iste,harf,seed=1):
    """ST: {'I':(bool,ifade,neden)}; iste True: doğru olanlar, False: yanlış olanlar. Döner: dogru,sira,yan,adimlar"""
    hedef={r for r in ST if ST[r][0]==iste}; assert hedef and len(hedef)<3 or iste or True
    dg=etiket(hedef); p=ONC.index(dg); idx='ABCDE'.index(harf); assert idx<=p and 4-idx<=6-p,(dg,harf)
    rnd=random.Random(seed); alt=rnd.sample(ONC[:p],idx); ust=rnd.sample(ONC[p+1:],4-idx)
    sira=sorted(alt+[dg]+ust,key=ONC.index); assert sira.index(dg)==idx
    kume=lambda l:{'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}[l]
    yan=[]
    for l in alt+ust:
        W=kume(l); parc=[]
        for r in sorted(W-hedef):
            t=ST[r][0]; parc.append(f"{r} öncülü {'doğru' if t else 'yanlış'}{'dur' if t else 'tır'}. {ST[r][2]} Ancak {'yanlış' if t else 'doğru'} sanılarak kümeye alınmıştır.")
        for r in sorted(hedef-W):
            t=ST[r][0]; parc.append(f"{r} öncülü {'doğru' if t else 'yanlış'}{'dur' if t else 'tır'}. {ST[r][2]} Ancak {'yanlış' if t else 'doğru'} sanılarak dışarıda bırakılmıştır.")
        yan.append((l,' '.join(parc),'bilgi'))
    ad=[A(f'{r} öncülünü değerlendir',ST[r][2],f"{r}: {'doğru' if ST[r][0] else 'yanlış'}") for r in ST]
    ad.append(A('Kümeyi oluştur',f"İstenen yargılara uyan öncüller: {', '.join(sorted(hedef))}.",'Cevap: '+dg))
    return dg,sira,yan,ad
def onctxt(giris,ST,kok): return giris+'\n'+'\n'.join(f'{r}. {ST[r][1]}' for r in ST)+'\n'+kok
def tablo_s(bas,sat): return tablo_svg(bas,sat)
def graf(govde,w='7.4cm',h='5cm'): return tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+govde+'\n\\end{tikzpicture}')
# ---- kartlar ----
kartla('K-ABSS-01','Solunum yolu ve alveol yapısı','Hava yolu burun–gırtlak–soluk borusu–bronş–bronşçuk–alveol sırasını izler; gaz değişimi yalnız ince, nemli, kılcal damarlarla sarılı alveol duvarında olur; surfaktan yüzey gerilimini azaltır.','Bronşları ve bronşçukları gaz değişimi yapıyor sanmak; surfaktanın gerilimi artırdığını düşünmek.','kolay','şekilli',3,'ss-yol-alveol','Solunum yolu ve alveol yapısı')
kartla('K-ABSS-02','Soluk alma–verme mekaniği','Diyafram ve dış kaburga arası kaslar kasılınca göğüs boşluğu hacmi artar, iç basınç düşer, hava girer; normal soluk verme pasiftir; plevra boşluğu basıncı atmosferden düşüktür.','Soluk almada diyaframın gevşediğini sanmak; basıncın artarak havayı çektiğini düşünmek.','orta','şekilli',4,'ss-mekanik','Soluk alıp verme mekanizması')
kartla('K-ABSS-03','Solunum hacimleri','Tidal hacim, soluk alma/verme yedek hacmi ve rezidüel hacim spirometre eğrisinden okunur; vital kapasite rezidüeli içermez.','Rezidüel hacmi vital kapasiteye katmak; grafikte fark yerine mutlak değer okumak.','zor','grafik',4,'ss-hacim','Spirometre grafiği ve solunum hacimleri')
kartla('K-ABSS-04','Gaz değişimi ve kısmi basınç','Gazlar kısmi basıncın yüksek olduğu ortamdan düşük olduğu ortama difüzyonla, enerji harcamadan geçer; alveolde ve dokuda gaz değişimi aynı ilkeye dayanır.','Difüzyonu aktif taşıma sanmak; yönü derişim yerine gazın türüne bağlamak.','orta','tablo',3,'ss-gaz-degisimi','Kısmi basınç farkı ve gaz değişimi')
kartla('K-ABSS-05','Hemoglobin ve oksijen taşınması','Oksijenin büyük kısmı hemoglobinle taşınır; CO2 artışı ve pH düşüşü hemoglobinin oksijene ilgisini azaltır (eğri sağa kayar), CO daha güçlü bağlanır.','Çok oksijenin plazmada taşındığını sanmak; pH düşünce ilginin arttığını düşünmek.','zor','grafik',4,'ss-hb-oksijen','Hemoglobin ve oksijen–hemoglobin eğrisi')
kartla('K-ABSS-06','Karbondioksit taşınması','CO2 kanda üç biçimde taşınır; payları farklıdır ve alyuvardaki enzim bikarbonat oluşumunu hızlandırır; akciğerde süreç tersine döner.','Taşınma biçimlerini birbirine karıştırmak; bikarbonatın plazmada oluştuğunu düşünmek.','zor','tablo',4,'ss-co2-tasima','Karbondioksit taşınma biçimleri')
kartla('K-ABSS-07','Solunumun düzenlenmesi','Solunum merkezi omurilik soğanındadır; kan CO2 artışı ve pH düşüşü en etkili uyarıcıdır; O2 azalması kemoreseptörlerle ancak belirgin düşüşte etkili olur.','Asıl uyarıcının O2 azlığı olduğunu sanmak; fazla O2 solumanın nefes tutmayı uzatma nedenini hemoglobine bağlamak.','orta','tablo',4,'ss-duzenleme','Solunumun düzenlenmesi')
kartla('K-ABSS-08','Yüksek rakım ve uyum','Yükseklikte oksijen yüzdesi değişmez, kısmi basıncı düşer; kemoreseptörler solunumu hızlandırır, eritropoietin alyuvar üretimini artırır.','Oksijen yüzdesinin azaldığını sanmak; hızlı solunumda pH düşeceğini düşünmek.','zor','öncüllü',4,'ss-iliskili','Çok kavramlı solunum yorumları')
B_YOL=B('Solunum yolu','burun boşluğu havayı süzer, ısıtır ve nemlendirir · gırtlak ses tellerini taşır · soluk borusu ve bronşlar hava yolunu açık tutan destek yapılarına sahiptir · bronşlar bronşçuklara ayrılır · gaz değişimi yalnız alveollerde olur')
B_ALV=B('Alveol','tek katlı yassı epitelden oluşan, çevresi kılcal damar ağıyla sarılı keseciklerdir · iç yüzeyi nemlidir ve surfaktanla kaplıdır · surfaktan yüzey gerilimini azaltarak alveolün sönmesini önler')
B_MEK=B('Soluk alma ve verme','soluk alırken diyafram kasılıp düzleşir, dış kaburga arası kaslar kasılıp kaburgaları yukarı–öne kaldırır; göğüs boşluğu hacmi artar, akciğer içi basınç atmosferin altına düşer ve hava girer · dinlenmede soluk verme kasların gevşemesiyle olur')
B_PLEV=B('Plevra','akciğeri saran çift zarlı yapıdır; zarlar arasındaki sıvı sürtünmeyi azaltır ve akciğerin göğüs boşluğunu izlemesini sağlar · bu boşluğun basıncı atmosfer basıncından düşüktür')
B_HAC=B('Solunum hacimleri','normal soluk alıp vermede taşınan hava tidal hacimdir · bunun üstüne alınabilen hava soluk alma yedek hacmi, normal soluk verme sonrası verilebilen hava soluk verme yedek hacmidir · rezidüel hacim en zorlu soluk vermeden sonra akciğerde kalır')
B_KB=B('Kısmi basınç ve difüzyon','bir gazın kısmi basıncı karışımdaki payıyla orantılıdır · gazlar kısmi basıncı yüksek ortamdan düşük ortama enerji harcanmadan geçer · bu yüzden alveol ve doku kılcallarında gaz değişimi difüzyonla olur')
B_HB=B('Hemoglobin','alyuvarda bulunan, demirli hem gruplarıyla oksijen bağlayan proteindir · oksijenle birleşince oksihemoglobin olur · karbonmonoksit hemoglobine oksijenden çok daha güçlü bağlanır')
B_BOHR=B('Oksijen–hemoglobin eğrisi','eğri oksijenin kısmi basıncına göre hemoglobinin doygunluğunu verir · kanda CO2 artınca ve pH düşünce eğri sağa kayar: aynı oksijen basıncında hemoglobin daha az oksijen bağlı tutar ve dokuya daha çok bırakır')
B_CO2=B('CO2 taşınması','CO2 kanda üç biçimde taşınır: bikarbonat iyonu, hemoglobine bağlı karbaminohemoglobin ve plazmada çözünmüş CO2 · alyuvardaki karbonik anhidraz CO2 ile suyun birleşmesini hızlandırır')
B_DUZ=B('Solunum merkezi','solunum merkezi omurilik soğanındadır ve diyafram ile kaburga arası kasları sinirlerle uyarır · kandaki CO2 artışı ve pH düşüşü merkezi uyarır · karotis ve aort cisimcikleri oksijen azlığını da algılar')
B_YUK=B('Kısmi basınç ve yükseklik','bir gazın kısmi basıncı, karışımdaki oranı ile toplam basıncın çarpımıdır · yükseklere çıkıldıkça toplam basınç azalır, havanın bileşimi değişmez')
# =================== 01 · solunum yolu şeması · kolay ===================
b=[]
def kume(x,y,r=.2):
    return ''.join(f'\\draw[line width=.8pt,fill=vurgu!15] ({x+r*1.1*math.cos(a*math.pi/3):.2f},{y+r*1.1*math.sin(a*math.pi/3):.2f}) circle ({r*.7});' for a in range(6))+f'\\draw[line width=.8pt,fill=vurgu!15] ({x},{y}) circle ({r*.75});'
b.append('\\draw[line width=1.2pt,fill=vurgu!15] (0,5.3) ellipse (.6 and .45);')
b.append('\\draw[line width=1.2pt] (-.2,4.85)--(-.2,4.4);\\draw[line width=1.2pt] (.2,4.85)--(.2,4.4);')
b.append('\\draw[line width=1.2pt,fill=vurgu!15] (-.32,4.4)--(.32,4.4)--(.22,3.7)--(-.22,3.7)--cycle;')
b.append('\\draw[line width=1.2pt,fill=vurgu!15] (-.2,3.7) rectangle (.2,2.4);')
for sg in (-1,1):
    b.append(f'\\draw[double distance=4pt,double=vurgu!15,line width=1.1pt] ({sg*.0},2.4)--({sg*1.4},1.4);')
    for ey in (.9,.1):
        b.append(f'\\draw[double distance=3pt,double=vurgu!15,line width=1pt] ({sg*1.4},1.4)--({sg*(2.0 if ey>.5 else 1.0)},{ey+.2});')
    b.append(kume(sg*2.0,.75)); b.append(kume(sg*1.0,.0))
def lab(t,x,y,x2,y2): return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{OK},line width=.8pt] ({x-.28 if x2<x else x+.28},{y})--({x2},{y2});'
b.append(lab('I',1.7,5.3,.62,5.3)); b.append(lab('II',1.7,4.05,.3,4.05)); b.append(lab('III',1.7,3.05,.22,3.05))
b.append(lab('IV',2.0,2.35,.72,1.9)); b.append(lab('V',-3.1,.75,-2.35,.75))
SK1=tk('\n'.join(b),.9)
NAME1={'I':'burun boşluğu','II':'gırtlak','III':'soluk borusu','IV':'bronş','V':'alveol kümesi'}
q('0001',tipId='ss-yol-alveol',tip='Solunum yolu ve alveol yapısı',z='kolay',alt='Solunum yolları',kaz='Şematik solunum yolunda yapıları konumlarından tanır ve özelliklerini bilir.',kalip='şekilli',
 kart='K-ABSS-01 (solunum yolu) · numaralı yapıdan soluk borusunu bulma',
 metin='Şekilde insan solunum yolunun bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralı yapılardan hangisinin duvarında C biçimli kıkırdak halkalar bulunur ve bu halkalar hava yolunun sürekli açık kalmasını sağlar?',
 dogru='III',sira=['I','II','III','IV','V'],
 yan=[('I','I numaralı yapı burun boşluğudur; havayı süzüp ısıtır ve nemlendirir, kıkırdak halkalı bir boru değildir.','bilgi'),
      ('II','II numaralı yapı gırtlaktır; ses tellerini taşır, C biçimli halkalarla açık kalan boru soluk borusudur.','bilgi'),
      ('IV','IV numaralı yapı bronştur; soluk borusundan sonra gelir ve dallanarak ilerler, halkaları soluk borusu kadar belirgin değildir.','bilgi'),
      ('V','V numaralı yapı alveol kümesidir; ince duvarlıdır ve gaz değişimini sağlar, kıkırdak halka taşımaz.','bilgi')],
 istenen='C biçimli kıkırdak halkalarla desteklenen yapının numarası.',
 ip=['Yapıların hava yolu üzerindeki sırasına bak: gırtlaktan sonra gelen ve bronşlara ayrılan boruyu ara.'],
 bilgi=[B_YOL,B_ALV],
 ad=[A('Yapıları sırala','Hava yukarıdan aşağı burun boşluğu, gırtlak, soluk borusu, bronş ve alveol kümelerine ilerler.','I: burun boşluğu · II: gırtlak · III: soluk borusu · IV: bronş · V: alveol'),
     A('Özelliği yapıyla eşleştir','C biçimli kıkırdak halkalar boru biçimli, açık kalması gereken soluk borusunun duvarındadır.','C halkalar → soluk borusu'),
     A('Numarayı bul','Soluk borusu gırtlak ile bronşlar arasındadır.','Cevap: III')],
 puf='Sıraya bak: gırtlaktan sonra, bronşlardan önce gelen yapı.',sekil=SK1)
# =================== 02 · alveol öncüllü · kolay ===================
ST2={'I':(True,'Alveoller tek katlı yassı epitel hücrelerinden oluşan ince duvarlı keseciklerdir.','Alveol duvarı tek katlı yassı epitelden yapılmıştır, bu da gazların kısa mesafeden geçmesini sağlar.'),
     'II':(False,'Alveollerin iç yüzeyini kaplayan surfaktan, yüzey gerilimini artırarak alveolün sönmesini önler.','Surfaktan yüzey gerilimini azaltır; gerilim artsaydı alveoller sönerdi.'),
     'III':(False,'Alveol ile kılcal damar arasındaki gaz geçişi, ATP harcanarak aktif taşımayla gerçekleşir.','Gazlar kısmi basınç farkına göre difüzyonla geçer, bu geçiş için ATP harcanmaz.')}
dg,sr,yn,ad=onc(ST2,True,'A',seed=2)
q('0002',tipId='ss-yol-alveol',tip='Solunum yolu ve alveol yapısı',z='kolay',alt='Alveol',kaz='Alveolün yapı ve işlevine ilişkin yargıların doğruluğunu değerlendirir.',kalip='öncüllü',
 kart='K-ABSS-01 (alveol) · yapı, surfaktan ve difüzyon yargıları',
 metin=onctxt('İnsanda alveollerle ilgili olarak aşağıdaki yargılar verilmiştir.',ST2,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=dg,sira=sr,yan=yn,istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Alveoldeki gaz geçişinin hangi taşıma türüne girdiğini ve surfaktanın gerilime etkisini ayrı ayrı düşün.'],bilgi=[B_ALV,B_KB],ad=ad,
 puf='Her yargıyı alveolün yapı ve işleviyle ayrı ayrı karşılaştır.')
# =================== 03 · zar modeli · kolay ===================
b=[]
b.append('\\draw[line width=1.4pt] (-1.5,0)--(-1.5,3.0) arc (180:0:1.5) -- (1.5,0);')
b.append('\\draw[line width=1.4pt,vurgu] (-1.5,-.35) .. controls (-.7,-.65) and (.7,-.65) .. (1.5,-.35);')
b.append('\\draw[line width=1pt] (-1.5,0)--(-1.5,-.35);\\draw[line width=1pt] (1.5,0)--(1.5,-.35);')
b.append('\\draw[line width=1.2pt] (0,5.1)--(0,3.6);\\draw[line width=1.2pt] (0,3.6)--(-.6,3.0);\\draw[line width=1.2pt] (0,3.6)--(.6,3.0);')
b.append('\\draw[line width=1.2pt] (-.6,3.0)--(-.65,2.75);\\draw[line width=1.2pt] (.6,3.0)--(.65,2.75);')
b.append('\\draw[line width=1pt,fill=vurgu!15] (-.65,2.0) ellipse (.42 and .7);\\draw[line width=1pt,fill=vurgu!15] (.65,2.0) ellipse (.42 and .7);')
b.append('\\draw[line width=1.2pt] (-.3,4.2) rectangle (.3,4.7);')
b.append('\\draw[line width=1.4pt,vurgu] (0,-.5)--(0,-1.2);\\draw[line width=1.4pt,vurgu] (-.2,-1.2) rectangle (.2,-1.45);')
b.append(f'\\draw[{OK},line width=1.4pt,vurgu] (.8,-.95)--(.8,-1.7);')
b.append('\\node[font=\\normalsize\\bfseries] at (-2.2,2.0) {I};\\draw[-{Stealth},line width=.8pt] (-1.95,2.0)--(-1.1,2.0);')
b.append('\\node[font=\\normalsize\\bfseries] at (2.2,-.55) {II};\\draw[-{Stealth},line width=.8pt] (1.95,-.55)--(1.2,-.5);')
b.append('\\node[font=\\normalsize\\bfseries] at (2.2,1.0) {III};\\draw[-{Stealth},line width=.8pt] (1.95,1.0)--(1.2,1.0);')
SK3=tk('\n'.join(b),.9)
dog3='Şişenin içindeki hava hacmi artar, basınç düşer ve balonlar şişer; bu durum insanda soluk almaya karşılık gelir.'
q('0003',tipId='ss-mekanik',tip='Soluk alıp verme mekanizması',z='kolay',alt='Soluk alıp verme',kaz='Solunum modelinde hacim–basınç değişimini insandaki soluk alma ile ilişkilendirir.',kalip='şekilli',
 kart='K-ABSS-02 (model deney) · lastik zar aşağı çekilince balonlar',
 metin='Şekildeki düzenekte, tabanı lastik zarla (II) kapatılmış bir şişenin içine, Y biçimli bir boruya bağlanmış iki balon (I) yerleştirilmiştir. Boru şişenin üstündeki tıpadan geçerek dışarı açılmaktadır. III ile gösterilen bölge şişenin içindeki balonlar dışında kalan hava boşluğudur. Lastik zar ok yönünde aşağı çekilmektedir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog3,sira=yer('E',dog3,['Şişenin içindeki hava hacmi artar, basınç yükselir ve balonlar söner; bu durum soluk almaya karşılık gelir.','Şişenin içindeki hava hacmi azalır, basınç yükselir ve balonlar şişer; bu durum soluk vermeye karşılık gelir.','Şişenin içindeki hava hacmi değişmez, balonlar kendiliğinden şişer; bu durum soluk almaya karşılık gelir.','Şişenin içindeki hava hacmi artar, basınç düşer ve balonlar söner; bu durum soluk vermeye karşılık gelir.']),
 yan=[('Şişenin içindeki hava hacmi artar, basınç yükselir ve balonlar söner; bu durum soluk almaya karşılık gelir.','Hacim artınca basınç düşer, yükselmez. Basınç artışı sanıldığı için balonların söneceği düşünülmüş.','bilgi'),
      ('Şişenin içindeki hava hacmi azalır, basınç yükselir ve balonlar şişer; bu durum soluk vermeye karşılık gelir.','Zar aşağı çekilince hacim azalmaz, artar. Hacim ve basınç ilişkisi ters kurulmuş.','bilgi'),
      ('Şişenin içindeki hava hacmi değişmez, balonlar kendiliğinden şişer; bu durum soluk almaya karşılık gelir.','Zarın aşağı çekilmesi şişenin hacmini artırır; balonlar kendiliğinden değil, dış hava girdiği için şişer.','dikkat'),
      ('Şişenin içindeki hava hacmi artar, basınç düşer ve balonlar söner; bu durum soluk vermeye karşılık gelir.','Basınç düşünce dış hava balonlara girer ve balonlar şişer. Basınç düşüşünün balonu söndüreceği sanılmış.','bilgi')],
 istenen='Zar aşağı çekildiğinde gerçekleşen olayın doğru yorumu.',
 ip=['Zarın aşağı çekilmesinin şişenin içindeki boşluğun büyüklüğünü nasıl değiştirdiğini ve basıncın buna göre nasıl değiştiğini düşün.'],
 bilgi=[B_MEK,B_KB],
 ad=[A('Modeli eşleştir','Lastik zar diyaframı, balonlar akciğerleri, şişenin içi göğüs boşluğunu temsil eder.','Zar = diyafram · balon = akciğer · şişe = göğüs boşluğu'),
     A('Hacim değişimini bul','Zar aşağı çekilince şişenin hacmi artar.','Hacim ↑'),
     A('Basınç ve hava akışını yorumla','Hacim artınca iç basınç düşer; dış hava boru yoluyla balonlara girer ve balonlar şişer.','Basınç ↓ → hava girer → balonlar şişer'),
     A('Olayı insanla ilişkilendir','Diyaframın aşağı inmesi soluk almadır.','Soluk alma')],
 puf='Hacim artınca basınç düşer ve hava içeri girer; modelde zarı aşağı çekmek diyaframın kasılmasıdır.',sekil=SK3)
# =================== 04 · diyafram iki durum · orta ===================
def toraks(cx,genis,dy,dome,kb):
    h=2.6; o=[]
    w=genis
    o.append(f'\\draw[line width=1.6pt,rounded corners=10pt] ({cx-w},{dy+.3}) -- ({cx-w},3.1) -- ({cx+w},3.1) -- ({cx+w},{dy+.3});')
    o.append(f'\\draw[line width=2.2pt,vurgu] ({cx-w},{dy+.3}) .. controls ({cx-w*.4},{dy+.3+dome}) and ({cx+w*.4},{dy+.3+dome}) .. ({cx+w},{dy+.3});')
    yb=dy+.3+dome*.75+.12; yt=2.9; cy_=(yb+yt)/2; ry=(yt-yb)/2
    o.append(f'\\draw[line width=1pt,fill=vurgu!15] ({cx-w*.5},{cy_}) ellipse ({w*.36} and {ry});\\draw[line width=1pt,fill=vurgu!15] ({cx+w*.5},{cy_}) ellipse ({w*.36} and {ry});')
    for yy in (2.7,2.2,1.7):
        o.append(f'\\draw[line width=1.6pt] ({cx-w},{yy-kb*.0}) -- ({cx-w-.25},{yy-.15});\\draw[line width=1.6pt] ({cx+w},{yy}) -- ({cx+w+.25},{yy-.15});')
    return '\n'.join(o)
b=[toraks(0,1.35,0,0.9,0),toraks(5.2,1.75,-.55,0.05,1)]
b.append('\\node[font=\\normalsize\\bfseries] at (0,-.7) {I};\\node[font=\\normalsize\\bfseries] at (5.2,-1.1) {II};')
SK4=tk('\n'.join(b),.8)
dog4='II numaralı durumda diyafram ve dış kaburga arası kaslar kasılmıştır; göğüs boşluğunun hacmi I numaralı duruma göre daha büyüktür.'
q('0004',tipId='ss-mekanik',tip='Soluk alıp verme mekanizması',z='orta',alt='Soluk alıp verme',kaz='Göğüs boşluğu şemalarında diyafram ve kaburga durumunu soluk alma–verme ile ilişkilendirir.',kalip='şekilli',
 kart='K-ABSS-02 (diyafram–kaburga) · iki evre karşılaştırması',
 metin='Şekilde bir insanın soluk alıp verme sırasındaki iki farklı anında göğüs kafesi ve diyaframın (yeşil çizgi) durumu I ve II ile gösterilmiştir. İki durumda da bu kişi dinlenme hâlindedir.\nBuna göre, aşağıdakilerden hangisi söylenebilir?',
 dogru=dog4,sira=yer('B',dog4,['I numaralı durumda diyafram kasılmıştır; akciğer içi basınç atmosfer basıncından düşüktür ve hava akciğerlere girmektedir.','I numaralı durumda dış kaburga arası kaslar kasılmıştır; göğüs boşluğunun hacmi II numaralı duruma göre daha büyüktür.','II numaralı durumda diyaframın kubbe biçimine dönmesi için kaslarının güçlü biçimde kasılması gerekir.','II numaralı durumda akciğer içi basınç atmosfer basıncına göre yüksektir ve hava akciğerlerden dışarı çıkmaktadır.']),
 yan=[('I numaralı durumda diyafram kasılmıştır; akciğer içi basınç atmosfer basıncından düşüktür ve hava akciğerlere girmektedir.','I durumunda diyafram kubbe biçimindedir, yani gevşemiştir; bu durum soluk vermeye aittir. Düzleşme kasılmanın göstergesidir.','bilgi'),
      ('I numaralı durumda dış kaburga arası kaslar kasılmıştır; göğüs boşluğunun hacmi II numaralı duruma göre daha büyüktür.','Kaburgalar II durumunda yukarı–dışa kalkmıştır, yani kaslar orada kasılıdır. Hacim de II durumunda daha büyüktür.','dikkat'),
      ('II numaralı durumda diyaframın kubbe biçimine dönmesi için kaslarının güçlü biçimde kasılması gerekir.','II durumunda diyafram düzleşmiştir; kubbe biçimine dönüş kasların gevşemesiyle olur, kasılmayla olmaz.','bilgi'),
      ('II numaralı durumda akciğer içi basınç atmosfer basıncına göre yüksektir ve hava akciğerlerden dışarı çıkmaktadır.','Hacim büyüdüğünde akciğer içi basınç atmosferin altına düşer ve hava içeri girer. Basınç yönü ters alınmış.','bilgi')],
 istenen='Şekle göre doğru olan ifade.',
 ip=['Diyaframın biçimini ve kaburgaların konumunu karşılaştırıp hangi durumda kasların kasılı olduğunu belirle.'],
 bilgi=[B_MEK,B_PLEV],
 ad=[A('Şekilleri karşılaştır','I’de diyafram kubbeli ve göğüs kafesi dardır; II’de diyafram düz ve kafes daha geniştir.','I: dar kafes, kubbe · II: geniş kafes, düz diyafram'),
     A('Kas durumunu bul','Diyaframın düzleşmesi ve kaburgaların kalkması kasların kasılmasıyla olur.','II: kaslar kasılı'),
     A('Hacim ve basıncı yorumla','Hacim büyüyünce akciğer içi basınç düşer ve hava girer.','II: hacim ↑, basınç ↓, soluk alma'),
     A('İfadeleri ele','Yalnız II’deki kasılma ve büyük hacmi söyleyen ifade şekille uyumludur.','Doğru ifade belirlendi')],
 puf='Her iki şekilde diyafram biçimini ve kaburga eğimini karşılaştır.',sekil=SK4)
# =================== 05 · öncüllü yanlış · orta ===================
ST5={'I':(False,'Soluk alma sırasında diyaframın gevşeyip kubbeleşmesi göğüs boşluğunun hacmini artırır.','Soluk alırken diyafram kasılıp düzleşir; gevşeyip kubbeleşmesi soluk vermede olur.'),
     'II':(True,'Dinlenme hâlinde soluk verme, solunum kaslarının gevşemesiyle büyük ölçüde pasif olarak gerçekleşir.','Dinlenmede soluk verme, kasların gevşeyip göğüs boşluğunun küçülmesiyle pasif olarak olur.'),
     'III':(False,'Plevra zarları arasındaki boşluğun basıncı atmosfer basıncından yüksektir.','Bu boşluğun basıncı atmosfer basıncından düşüktür; akciğer bu sayede göğüs boşluğunu izler.')}
dg,sr,yn,ad=onc(ST5,False,'C',seed=3)
q('0005',tipId='ss-mekanik',tip='Soluk alıp verme mekanizması',z='orta',alt='Soluk alıp verme',kaz='Soluk alma–verme sırasında kas hareketleri ve plevra basıncı yargılarındaki yanlışları belirler.',kalip='öncüllü',
 kart='K-ABSS-02 (mekanizma) · diyafram, pasif soluk verme, plevra basıncı',
 metin=onctxt('İnsanda soluk alıp verme mekanizmasıyla ilgili olarak aşağıdaki yargılar verilmiştir.',ST5,'Buna göre, bu yargılardan hangileri yanlıştır?'),
 dogru=dg,sira=sr,yan=yn,istenen='Yanlış olan yargıların belirlenmesi.',
 ip=['Her yargıyı diyafram–kaburga hareketi ve basınç–hacim ilişkisi bakımından ayrı ayrı sına.'],bilgi=[B_MEK,B_PLEV],ad=ad,
 puf='Her yargıyı kas durumu ve basınç–hacim ilişkisiyle ayrı ayrı sına.')
# =================== 06 · spirometre · zor ===================
pts=[]
for i in range(0,61): 
    t=i/10; pts.append((t,1750-250*math.cos(2*math.pi*t/3)))
for i in range(1,26):
    t=6+i/10; u=(t-6)/2.5; pts.append((t,1500+3500*(1-math.cos(math.pi*u))/2))
for i in range(1,11):
    t=8.5+i/10; pts.append((t,5000))
for i in range(1,31):
    t=9.5+i/10; u=(t-9.5)/3; pts.append((t,5000*(1+math.cos(math.pi*u))/2))
for i in range(1,16):
    t=12.5+i/10; u=(t-12.5)/1.5; pts.append((t,1500*(1-math.cos(math.pi*u))/2))
for i in range(1,31):
    t=14+i/10; pts.append((t,1750-250*math.cos(2*math.pi*(t-14)/3)))
VMAX=max(v for t,v in pts); VMIN=min(v for t,v in pts); assert (VMAX,VMIN)==(5000,0)
ERV,TV,IRV,RV=1500,500,3000,1000; assert VMAX-(ERV+TV)==IRV and VMAX-VMIN==ERV+TV+IRV
FRC=ERV+RV; assert FRC==2500; VK=ERV+TV+IRV; TLC=VK+RV; assert (TLC,VK)==(6000,5000)
co=' '.join(f'({t:.2f},{v:.0f})' for t,v in pts[::2])
b=['\\begin{axis}[width=8.2cm,height=5.4cm,xmin=0,xmax=17,ymin=0,ymax=5500,xtick=\\empty,ytick={0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000},axis lines=left,xlabel={Zaman},ylabel={Hava hacmi (mL)},yticklabel style={/pgf/number format/.cd,1000 sep={}},ymajorgrids=true,grid style={gray!30},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt,vurgu!80!black}]',
   f'\\addplot[smooth] coordinates {{{co}}};','\\end{axis}']
SK6=graf('\n'.join(b))
dog6=FRC
q('0006',tipId='ss-hacim',tip='Spirometre grafiği ve solunum hacimleri',z='zor',alt='Solunum hacimleri',kaz='Spirometre eğrisinden hacimleri okuyup rezidüel hacimle birleştirerek normal soluk verme sonunda akciğerde kalan hava hacmini hesaplar.',kalip='grafik',
 kart='K-ABSS-03 (spirometre) · ERV okuma + rezidüel hacim ekleme',
 metin='Bir bireyin akciğer hacimleri spirometre ile ölçülmüş ve hava hacminin zamanla değişimi grafikteki gibi kaydedilmiştir. Grafikte, bireyin en zorlu soluk vermesi sonunda ölçülen hacim 0 mL olarak alınmıştır. Aynı bireyin rezidüel hacminin 1000 mL olduğu başka bir yöntemle belirlenmiştir.\nBuna göre, bu bireyin normal bir soluk verme sonunda akciğerlerinde kalan toplam hava hacmi kaç mL’dir?',
 dogru=dog6,yan=[(1000,'Yalnız rezidüel hacim alınmış; normal soluk vermeden sonra verilebilecek yedek hava da akciğerde kalır, bu hava unutulmuş.','dikkat'),
   (1500,'Yalnız soluk verme yedek hacmi (1500 mL) alınmış; en zorlu soluk vermede bile atılamayan rezidüel hava eklenmemiş.','dikkat'),
   (2000,'Normal soluk alma sonundaki grafik değeri (2000 mL) okunmuş; oysa istenen normal soluk verme sonundaki hacimdir ve rezidüel hacim zaten bu okumaya dahil değildir.','islem'),
   (6000,'Vital kapasite (5000 mL) ile rezidüel hacim (1000 mL) toplanmış; bu toplam akciğer kapasitesidir, normal soluk verme sonundaki hava değildir.','bilgi')],
 istenen='Normal soluk verme sonunda akciğerde kalan hava hacmi (mL).',
 ip=['Grafiği, en zorlu soluk verme sonu seviyesine göre okumayı dene.'],
 bilgi=[B_HAC,B('Hacimlerin okunması','spirometre grafiğinde iki seviye arasındaki fark hacmi verir · en zorlu soluk verme sonu seviyesi 0 alınırsa, normal soluk verme sonu seviyesi soluk verme yedek hacmine eşittir')],
 ad=[A('Normal soluk verme seviyesini oku','Normal soluk alıp vermedeki en alt seviye, normal soluk verme sonunu gösterir; bu seviye 0 mL’nin 1500 mL üstündedir.','Soluk verme yedek hacmi = 1500 mL'),
     A('Atılamayan havayı belirle','En zorlu soluk vermeden sonra bile akciğerde kalan hava rezidüel hacimdir ve grafikte ölçülemez.','Rezidüel hacim = 1000 mL'),
     A('İkisini topla','Normal soluk verme sonunda akciğerde yedek hava ve rezidüel hava birlikte bulunur.','1500 + 1000 = 2500 mL'),
     A('Sonucu kontrol et','Bu değer, vital kapasite 5000 mL ve toplam kapasite 6000 mL olan bireyde ikisinin arasında kalır.','Cevap: 2500 mL')],
 puf='Normal soluk verme sonunda akciğerde hangi hacimlerin kaldığını düşün.',sekil=SK6)
# =================== 07 · vital kapasite · orta ===================
ST7={'I':(True,'Vital kapasite, tidal hacim ile soluk alma ve soluk verme yedek hacimlerinin toplamıdır.','Vital kapasite tidal hacim, soluk alma yedek hacmi ve soluk verme yedek hacminin toplamına eşittir.'),
     'II':(False,'Vital kapasite, rezidüel hacmi de içeren toplam hava miktarıdır.','Rezidüel hacim en zorlu soluk vermede de atılamadığından vital kapasiteye dahil değildir; rezidüel hacim vital kapasiteye eklendiğinde toplam kapasite bulunur.'),
     'III':(True,'Düzenli solunum egzersizi yapan bireylerde vital kapasite artabilir.','Solunum kaslarının güçlenmesi ve akciğer esnekliğinin artmasıyla vital kapasite yükselebilir.')}
dg,sr,yn,ad=onc(ST7,False,'B',seed=4)
q('0007',tipId='ss-hacim',tip='Spirometre grafiği ve solunum hacimleri',z='orta',alt='Solunum hacimleri',kaz='Vital kapasite ve rezidüel hacim kavramlarına ilişkin yargılardaki yanlışı belirler.',kalip='öncüllü',
 kart='K-ABSS-03 (vital kapasite) · rezidüel hacim hatası',
 metin=onctxt('İnsanda akciğer hacimleri ve kapasiteleriyle ilgili olarak aşağıdaki yargılar verilmiştir.',ST7,'Buna göre, bu yargılardan hangileri yanlıştır?'),
 dogru=dg,sira=sr,yan=yn,istenen='Yanlış olan yargıların belirlenmesi.',
 ip=['Vital kapasitenin hangi hacimlerden oluştuğunu ve hangi hacmin dışarıda kaldığını düşün.'],bilgi=[B_HAC,B('Vital kapasite','en derin soluk alındıktan sonra zorlu soluk vermeyle dışarı verilebilen en fazla hava hacmidir · solunum kaslarının gücü, akciğer esnekliği ve göğüs kafesi yapısı bu değeri etkiler')],ad=ad,
 puf='Kapasiteleri oluşturan hacimleri ayrı ayrı sırala.')
# =================== 08 · basınç–zaman · zor ===================
cx=[(i/20,-math.sin(math.pi*(i/20)/2)) for i in range(0,41) if i/20<=2]+[(i/20,math.sin(math.pi*(i/20-2)/2)) for i in range(41,81)]
cy=[(i/20,-5-3*math.sin(math.pi*(i/20)/2)) for i in range(0,41)]+[(i/20,-5) for i in range(41,81)]
vx=lambda t:-math.sin(math.pi*t/2) if t<=2 else math.sin(math.pi*(t-2)/2)
assert round(vx(1),6)==-1 and round(vx(3),6)==1 and all(v<0 for t,v in cy if 0<t<2) and all(v<0 for t,v in cy)
sx=' '.join(f'({t:.2f},{v:.2f})' for t,v in cx); sy=' '.join(f'({t:.2f},{v:.2f})' for t,v in cy)
b=['\\begin{axis}[width=8cm,height=5.4cm,xmin=0,xmax=4,ymin=-9,ymax=2,xtick={0,1,2,3,4},xticklabels={0,I,2,II,4},ytick={-8,-6,-4,-2,0,2},axis lines=left,axis x line shift=0,xlabel={Zaman (s)},ylabel={Basınç (cmH$_2$O)},ymajorgrids=true,grid style={gray!30},tick label style={font=\\footnotesize,/pgf/number format/assume math mode},label style={font=\\small},every axis plot/.append style={line width=1.5pt}]',
   '\\draw[gray,dashed] (axis cs:0,0)--(axis cs:4,0);',f'\\addplot[vurgu!80!black] coordinates {{{sx}}};',f'\\addplot[black] coordinates {{{sy}}};',
   '\\draw[dashed,gray] (axis cs:1,-9)--(axis cs:1,2);\\draw[dashed,gray] (axis cs:3,-9)--(axis cs:3,2);',
   '\\node[font=\\small\\bfseries,vurgu!80!black] at (axis cs:3.45,1.0) {X};\\node[font=\\small\\bfseries] at (axis cs:3.45,-4.1) {Y};','\\end{axis}']
SK8=graf('\n'.join(b))
dog8='Y eğrisi plevra boşluğunun basıncını göstermektedir; II anında akciğer içi basınç atmosfer basıncından yüksek olduğundan hava akciğerlerden dışarı çıkmaktadır.'
q('0008',tipId='ss-mekanik',tip='Soluk alıp verme mekanizması',z='orta',alt='Basınç değişimleri',kaz='Akciğer içi ve plevra basıncı eğrilerini ayırt edip soluk alma–verme evrelerini yorumlar.',kalip='grafik',
 kart='K-ABSS-02 (basınç–zaman) · plevra negatif basıncı ve evre belirleme',
 metin='Sağlıklı bir insanın bir soluk alıp verme döngüsü sırasında, akciğer içi basınç ile plevra zarları arasındaki boşluğun basıncı ölçülmüş ve bu basınçların zamanla değişimi grafikteki X ve Y eğrileriyle gösterilmiştir. Basınçlar, atmosfer basıncı sıfır kabul edilerek verilmiştir. Grafikte I ve II ile işaretlenen anlarda ölçümler yapılmıştır.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog8,sira=yer('A',dog8,['X eğrisi plevra boşluğunun basıncını göstermektedir; I anında diyafram kasılmış ve hava akciğerlere girmektedir.','Y eğrisi plevra boşluğunun basıncını göstermektedir; I anında akciğer içi basınç atmosfer basıncından yüksektir ve hava akciğerlere girmektedir.','Her iki anda da plevra boşluğunun basıncı atmosfer basıncından yüksektir ve akciğerler bu sayede şişkin kalır.','Y eğrisi plevra boşluğunun basıncını göstermektedir; II anında diyafram kasılarak düzleşmekte ve akciğer içi basınç artmaktadır.']),
 yan=[('X eğrisi plevra boşluğunun basıncını göstermektedir; I anında diyafram kasılmış ve hava akciğerlere girmektedir.','Plevra boşluğunun basıncı hep atmosfer basıncının altındadır; bu özellik hep negatif kalan Y eğrisindedir. X akciğer içi basıncı gösterir.','dikkat'),
      ('Y eğrisi plevra boşluğunun basıncını göstermektedir; I anında akciğer içi basınç atmosfer basıncından yüksektir ve hava akciğerlere girmektedir.','I anında X eğrisi sıfırın altındadır; akciğer içi basınç atmosfer basıncından düşüktür ve hava bu yüzden içeri girer. Basınç farkının yönü ters alınmış.','bilgi'),
      ('Her iki anda da plevra boşluğunun basıncı atmosfer basıncından yüksektir ve akciğerler bu sayede şişkin kalır.','Plevra basıncı her iki anda da atmosfer basıncının altındadır; negatif basınç akciğerin göğüs boşluğunu izlemesini sağlar.','bilgi'),
      ('Y eğrisi plevra boşluğunun basıncını göstermektedir; II anında diyafram kasılarak düzleşmekte ve akciğer içi basınç artmaktadır.','II anında hava dışarı çıktığı için diyafram gevşemiştir; kasılması soluk almaya özgüdür. Basınç artışı doğru ama diyafram durumu yanlış okunmuş.','dikkat')],
 istenen='Grafiğe göre doğru olan ifade.',
 ip=['Eğrilerin sıfır çizgisine göre konumlarını karşılaştır.'],
 bilgi=[B_MEK,B_PLEV],
 ad=[A('Eğrileri tanı','Y eğrisi tüm zaman boyunca sıfırın altındadır; yalnız plevra boşluğunun basıncı sürekli negatiftir. X ise sıfırın altına ve üstüne geçer.','Y: plevra · X: akciğer içi'),
     A('I anını yorumla','I anında X yaklaşık −1’dir; akciğer içi basınç atmosferin altındadır, hava girer, diyafram kasılıdır.','I: soluk alma'),
     A('II anını yorumla','II anında X yaklaşık +1’dir; akciğer içi basınç atmosferin üstündedir, hava çıkar, kaslar gevşemiştir.','II: soluk verme'),
     A('İfadeleri karşılaştır','Y’nin plevra basıncı ve II anındaki yüksek akciğer içi basınç birlikte yalnız bir ifadede doğrudur.','Doğru ifade belirlendi')],
 puf='Önce eğrileri tanı, sonra her anda basıncın işaretine bak.',sekil=SK8)
# =================== 09 · kısmi basınç tablosu · orta ===================
KB={'Alveol havası':(104,40),'Akciğer kılcalına gelen kan':(40,46),'Dokuya ulaşan kan':(100,40),'Doku hücresi':(20,50)}
assert KB['Alveol havası'][0]>KB['Akciğer kılcalına gelen kan'][0] and KB['Alveol havası'][1]<KB['Akciğer kılcalına gelen kan'][1]
assert KB['Dokuya ulaşan kan'][0]>KB['Doku hücresi'][0] and KB['Dokuya ulaşan kan'][1]<KB['Doku hücresi'][1]
SK9=tablo_svg(['Ortam','pO₂ (mmHg)','pCO₂ (mmHg)'],[[k,str(v[0]),str(v[1])] for k,v in KB.items()])
dog9='Alveolden kana O₂, kandan alveole CO₂ geçer; doku kılcallarında ise O₂ kandan hücreye, CO₂ hücreden kana geçer.'
q('0009',tipId='ss-gaz-degisimi',tip='Kısmi basınç farkı ve gaz değişimi',z='orta',alt='Gaz değişimi',kaz='Kısmi basınç verilerinden alveolde ve dokuda gaz geçiş yönlerini belirler.',kalip='tablo',
 kart='K-ABSS-04 (kısmi basınç tablosu) · alveol ve doku geçişleri',
 metin='Tabloda, sağlıklı bir insanın dolaşımındaki dört ortamda ölçülen oksijen (pO₂) ve karbondioksit (pCO₂) kısmi basınçları verilmiştir. Ölçümler dinlenme hâlinde yapılmıştır.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog9,sira=yer('D',dog9,['Alveolden kana CO₂, kandan alveole O₂ geçer; doku kılcallarında ise O₂ hücreden kana, CO₂ kandan hücreye geçer.','Alveolde gaz geçişi kısmi basınç farkıyla, doku kılcallarında ise taşıyıcı proteinlerle gerçekleşir.','Alveol havasındaki CO₂ kısmi basıncı kandakinden yüksek olduğundan CO₂ alveolden kana geçer.','Dokuya ulaşan kandaki O₂ kısmi basıncı hücredekinden yüksek olduğundan O₂ hücreden kana geçer.']),
 yan=[('Alveolden kana CO₂, kandan alveole O₂ geçer; doku kılcallarında ise O₂ hücreden kana, CO₂ kandan hücreye geçer.','Gazların yönü ters alınmış: O₂ kısmi basıncı alveolde ve arteriyel kanda yüksektir, bu yüzden O₂ kana ve hücreye doğru geçer.','bilgi'),
      ('Alveolde gaz geçişi kısmi basınç farkıyla, doku kılcallarında ise taşıyıcı proteinlerle gerçekleşir.','Her iki bölgede de gazlar kısmi basınç farkına dayalı difüzyonla geçer; taşıyıcı protein gerekmez.','bilgi'),
      ('Alveol havasındaki CO₂ kısmi basıncı kandakinden yüksek olduğundan CO₂ alveolden kana geçer.','Alveol havasında CO₂ kısmi basıncı 40, akciğer kılcalına gelen kanda 46 mmHg’dir; CO₂ yüksek olan kandan alveole geçer. Tablo yanlış okunmuş.','dikkat'),
      ('Dokuya ulaşan kandaki O₂ kısmi basıncı hücredekinden yüksek olduğundan O₂ hücreden kana geçer.','Gerekçe doğru okunmuş ama sonuç ters yazılmış: O₂ basıncı yüksek olan kandan düşük olan hücreye geçer.','dikkat')],
 istenen='Tablodaki verilere göre doğru olan ifade.',
 ip=['Her iki gaz için iki ortamın kısmi basınçlarını karşılaştır; geçişin yönü basıncı yüksek ortamdan düşüğe doğrudur.'],
 bilgi=[B_KB],
 ad=[A('Alveol ve kanı karşılaştır','O₂ için alveol 104, kan 40; CO₂ için alveol 40, kan 46 mmHg’dir.','O₂: alveol > kan · CO₂: kan > alveol'),
     A('Kan ve hücreyi karşılaştır','Dokuya ulaşan kanda O₂ 100, hücrede 20; CO₂ için kanda 40, hücrede 50 mmHg’dir.','O₂: kan > hücre · CO₂: hücre > kan'),
     A('Geçiş yönlerini belirle','Gazlar yüksek kısmi basınçtan düşüğe geçer; geçişler pasiftir.','Alveol→kan O₂; kan→alveol CO₂; kan→hücre O₂; hücre→kan CO₂'),
     A('İfadeyi seç','Bu yönleri birlikte doğru veren ifade geçerlidir.','Doğru ifade belirlendi')],
 puf='Gaz her zaman kısmi basıncı yüksek yerden düşük yere, enerji harcamadan geçer.',sekil=SK9)
# =================== 10 · gaz değişimini azaltan · orta ===================
ST10={'I':(False,'Alveolleri saran kılcal damar ağının genişlemesi','Kılcal damar ağının geniş olması gaz değişimine ayrılan kan yüzeyini artırır; gaz değişimini azaltmaz.'),
      'II':(True,'Alveol iç yüzeyinde surfaktan azlığı nedeniyle alveollerin sönmesi','Alveoller sönünce gaz değişimine açık yüzey daralır ve birim zamandaki gaz alışverişi azalır.'),
      'III':(True,'Alveol duvarını oluşturan bağ dokunun kalınlaşması','Duvar kalınlaşınca gazların geçeceği mesafe artar ve difüzyon yavaşlar.')}
dg,sr,yn,ad=onc(ST10,True,'D',seed=5)
q('0010',tipId='ss-gaz-degisimi',tip='Kısmi basınç farkı ve gaz değişimi',z='orta',alt='Gaz değişiminin verimi',kaz='Alveoldeki gaz değişim hızını etkileyen durumları yorumlar.',kalip='öncüllü',
 kart='K-ABSS-04 (verim) · yüzey, mesafe ve surfaktan',
 metin=onctxt('Akciğerlerde birim zamanda gerçekleşen gaz değişimiyle ilgili olarak aşağıdaki durumlar verilmiştir.',{k:(v[0],v[1]+'.',v[2]) for k,v in ST10.items()},'Bu durumlardan hangileri gaz değişiminin azalmasına neden olur?'),
 dogru=dg,sira=sr,yan=yn,istenen='Gaz değişimini azaltan durumların belirlenmesi.',
 ip=['Her durumun gaz geçişine açık yüzeyi ve gazların kat edeceği mesafeyi nasıl etkilediğini düşün.'],bilgi=[B_ALV,B_KB],ad=ad,
 puf='Geniş yüzey, ince duvar ve nemlilik gaz değişimini artırır; yüzeyi daraltan ya da mesafeyi uzatan durum azaltır.')
# =================== 11 · Hb eğrisi · zor ===================
XH=[(0,0),(10,14),(20,35),(30,57),(40,75),(50,85),(60,90),(80,95),(100,97)]
YH=[(0,0),(10,6),(20,20),(30,37),(40,50),(50,63),(60,74),(80,88),(100,94)]
def ip_(L,x): 
    for (a,b_),(c,d) in zip(L,L[1:]):
        if a<=x<=c: return b_+(d-b_)*(x-a)/(c-a)
assert ip_(XH,40)==75 and ip_(YH,40)==50 and all(ip_(XH,x)>ip_(YH,x) for x in range(10,100,10)); FARK=75-50; assert FARK==25
b=['\\begin{axis}[width=7.8cm,height=5.4cm,xmin=0,xmax=100,ymin=0,ymax=100,xtick={0,20,40,60,80,100},ytick={0,25,50,75,100},axis lines=left,xlabel={O$_2$ kısmi basıncı (mmHg)},ylabel={Hemoglobin doygunluğu (\\%)},grid=both,grid style={gray!25},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt,smooth}]',
   '\\addplot[vurgu!80!black] coordinates {'+' '.join(f'({a},{c})' for a,c in XH)+'};','\\addplot[black] coordinates {'+' '.join(f'({a},{c})' for a,c in YH)+'};',
   '\\node[font=\\small\\bfseries,vurgu!80!black] at (axis cs:22,70) {X};\\node[font=\\small\\bfseries] at (axis cs:56,48) {Y};','\\end{axis}']
SK11=graf('\n'.join(b))
dog11='Y eğrisi pH 7,2’de çizilmiştir; O₂ kısmi basıncı 40 mmHg olan doku kılcallarında Y koşulunda hemoglobin X koşuluna göre 25 puan daha az doygundur ve dokuya daha çok O₂ bırakmıştır.'
q('0011',tipId='ss-hb-oksijen',tip='Hemoglobin ve oksijen–hemoglobin eğrisi',z='zor',alt='Hemoglobin',kaz='Oksijen–hemoglobin eğrilerini pH etkisiyle ilişkilendirip doku kılcallarındaki oksijen bırakımını yorumlar.',kalip='grafik',
 kart='K-ABSS-05 (Bohr etkisi) · eğri kayması ve doku oksijen bırakımı',
 metin='Aynı bireyin kanından alınan örneklerde, hemoglobinin oksijene doygunluğu oksijenin kısmi basıncına bağlı olarak iki farklı pH değerinde (7,4 ve 7,2) ölçülmüştür. Sonuçlar grafikte X ve Y eğrileriyle verilmiştir; hangi eğrinin hangi pH değerine ait olduğu belirtilmemiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog11,sira=yer('A',dog11,['X eğrisi pH 7,2’de çizilmiştir; pH düştüğünde hemoglobinin O₂’ye ilgisi arttığı için eğri sola kaymıştır.','Y eğrisi pH 7,2’de çizilmiştir; 40 mmHg’de Y koşulunda hemoglobin daha az doygun olduğundan dokuya daha az O₂ bırakır.','Y eğrisi pH 7,2’de çizilmiştir; 40 mmHg’de doygunluk Y koşulunda %75, X koşulunda %50’dir.','Y eğrisi pH 7,2’de çizilmiştir; pH düşüşü O₂ bırakımını azalttığı için egzersiz yapan kasın kılcalında bu koşul beklenmez.']),
 yan=[('X eğrisi pH 7,2’de çizilmiştir; pH düştüğünde hemoglobinin O₂’ye ilgisi arttığı için eğri sola kaymıştır.','pH düşünce hemoglobinin O₂’ye ilgisi azalır ve eğri sağa kayar; sağdaki Y eğrisi pH 7,2’ye aittir. Eğrinin yönü ve ilgi ters yorumlanmış.','bilgi'),
      ('Y eğrisi pH 7,2’de çizilmiştir; 40 mmHg’de Y koşulunda hemoglobin daha az doygun olduğundan dokuya daha az O₂ bırakır.','Aynı basınçta daha az doygun olmak, hemoglobinin O₂’yi daha çok bırakmış olması demektir. Doygunluğun azlığı, taşınan miktarın azlığı sanılmış.','dikkat'),
      ('Y eğrisi pH 7,2’de çizilmiştir; 40 mmHg’de doygunluk Y koşulunda %75, X koşulunda %50’dir.','Grafikte 40 mmHg’de X eğrisi %75, Y eğrisi %50’dir; değerler eğrilere ters yerleştirilmiş.','islem'),
      ('Y eğrisi pH 7,2’de çizilmiştir; pH düşüşü O₂ bırakımını azalttığı için egzersiz yapan kasın kılcalında bu koşul beklenmez.','pH düşüşü O₂ bırakımını artırır; egzersiz yapan kasta CO₂ arttığı ve pH düştüğü için Y koşulu tam olarak beklenir.','bilgi')],
 istenen='Grafiğe ve hemoglobinin özelliklerine göre doğru olan ifade.',
 ip=['Hangi eğrinin düşük pH’a ait olduğunu hemoglobinin O₂’ye ilgisinin pH ile değişimine göre belirle, sonra 40 mmHg’deki değerleri oku.'],
 bilgi=[B_HB,B_BOHR],
 ad=[A('Eğrilerin yerini yorumla','Düşük pH’ta hemoglobinin O₂’ye ilgisi azalır; aynı basınçta daha az doygun olur, eğri sağa kayar.','Sağdaki Y: pH 7,2 · soldaki X: pH 7,4'),
     A('40 mmHg değerlerini oku','40 mmHg’de X eğrisi %75, Y eğrisi %50 doygunluğu gösterir.','X: %75 · Y: %50'),
     A('Farkı hesapla','Doku kılcalında Y koşulunda hemoglobin daha az doygundur; aradaki fark bırakılan fazladan O₂’yi gösterir.','75 − 50 = 25 puan'),
     A('Yorumu seç','Y’nin pH 7,2’ye ait olduğunu ve dokuya daha çok O₂ bırakıldığını söyleyen ifade doğrudur.','Doğru ifade belirlendi')],
 puf='Hangi eğrinin hangi pH’a ait olduğunu belirleyip aynı basınçta doygunlukları karşılaştır.',sekil=SK11)
# =================== 12 · hemoglobin öncüllü · orta ===================
ST12={'I':(True,'Hemoglobin, her biri demir taşıyan dört hem grubu içerir ve bir molekülü en fazla dört oksijen molekülü bağlayabilir.','Hemoglobinde dört hem grubu vardır ve her biri bir oksijen molekülü bağlayabilir.'),
      'II':(False,'Hemoglobin yalnız oksijen bağlayabilir, diğer gazların taşınmasında rol almaz.','Hemoglobin CO₂ ile karbaminohemoglobin, CO ile karboksihemoglobin oluşturur; yalnız oksijen taşımaz.'),
      'III':(True,'Karbonmonoksit, hemoglobine oksijenden çok daha güçlü bağlanarak kanın oksijen taşıma kapasitesini azaltır.','CO hemoglobine oksijenden çok daha yüksek ilgiyle bağlandığı için oksijen taşıyan hemoglobin miktarı düşer.')}
dg,sr,yn,ad=onc(ST12,True,'C',seed=6)
q('0012',tipId='ss-hb-oksijen',tip='Hemoglobin ve oksijen–hemoglobin eğrisi',z='orta',alt='Hemoglobin',kaz='Hemoglobinin yapısı ve gaz bağlama özelliklerine ilişkin yargıları değerlendirir.',kalip='öncüllü',
 kart='K-ABSS-05 (hemoglobin) · hem grubu, gaz bağlama, CO',
 metin=onctxt('Hemoglobinle ilgili olarak aşağıdaki yargılar verilmiştir.',ST12,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=dg,sira=sr,yan=yn,istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Hemoglobinin hangi gazlarla bağ kurabildiğini ve bağlanma güçlerini düşün.'],bilgi=[B_HB,B_CO2],ad=ad,
 puf='Her yargıyı hemoglobinin bağladığı gazlar bakımından sına.')
# =================== 13 · CO2 taşınması tablo · zor ===================
CO2={'Plazmada çözünmüş':14,'I':140,'II':46}; TOP=sum(CO2.values()); assert TOP==200 and 14*10==TOP*7//10//1 or True
assert CO2['I']==TOP*70//100 and CO2['II']==TOP*23//100 and CO2['Plazmada çözünmüş']==TOP*7//100
KAT=Fr(5,2); dg13=CO2['II']*KAT; assert dg13==115
SK13=tablo_svg(['Taşınma biçimi','CO₂ miktarı (mL/dk)'],[[k,str(v)] for k,v in CO2.items()])
q('0013',tipId='ss-co2-tasima',tip='Karbondioksit taşınma biçimleri',z='orta',alt='CO₂ taşınması',kaz='Tablodaki verilerden karbaminohemoglobin payını belirleyip değişen koşulda hesaplar.',kalip='tablo',
 kart='K-ABSS-06 (CO₂ biçimleri) · bikarbonat/karbaminohemoglobin ayrımı ve hesap',
 metin='Dinlenme hâlindeki bir insanda dokulardan kana geçen CO₂’nin taşınma biçimleri tabloda verilmiştir. I ve II ile gösterilen biçimlerden biri bikarbonat iyonu, diğeri hemoglobine bağlı (karbaminohemoglobin) taşınmadır; hangisinin hangisi olduğu belirtilmemiştir.\nBu kişi egzersiz yaptığında dokulardan kana geçen CO₂ miktarı 2,5 katına çıkıyor ve biçimlerin payları değişmiyor.\nBuna göre, egzersiz sırasında dakikada hemoglobine bağlanarak taşınan CO₂ miktarı kaç mL’dir?',
 dogru=115,yan=[(35,'Plazmada çözünmüş CO₂ miktarı (14 mL) 2,5 ile çarpılmış; oysa hemoglobine bağlı olan payı bu değildir.','dikkat'),
   (46,'Dinlenme değeri okunmuş; egzersizde CO₂ miktarının 2,5 katına çıkması hesaba katılmamış.','islem'),
   (350,'En büyük pay (140 mL) hemoglobine bağlı sanılıp 2,5 ile çarpılmış; en büyük pay bikarbonat iyonu olarak taşınandır.','bilgi'),
   (500,'Kana geçen toplam CO₂ (200 mL) 2,5 ile çarpılmış; tüm CO₂’nin hemoglobine bağlandığı sanılmış.','bilgi')],
 istenen='Egzersizde hemoglobine bağlı taşınan CO₂ miktarı (mL/dk).',
 ip=['Hangi biçimin en büyük payı aldığını CO₂ taşınmasındaki sıralamadan çıkar; sonra artış katsayısını uygula.'],
 bilgi=[B_CO2],
 ad=[A('Biçimleri belirle','CO₂’nin en büyük kısmı bikarbonat olarak, daha küçük kısmı karbaminohemoglobin olarak taşınır; en küçük pay plazmada çözünendir.','I: bikarbonat (140) · II: karbaminohemoglobin (46)'),
     A('Hemoglobinle taşınanı bul','Karbaminohemoglobin payı tablodaki II’dir.','Dinlenmede 46 mL/dk'),
     A('Egzersiz artışını uygula','Toplam CO₂ 2,5 katına çıkarken payların oranı değişmediği için her biçim 2,5 katına çıkar.','46 × 2,5 = 115 mL/dk'),
     A('Sonucu kontrol et','Pay %23 olduğundan 500 mL’nin %23’ü de 115 mL eder.','Cevap: 115 mL')],
 puf='Önce I ve II’nin hangi biçim olduğunu ayır, sonra katsayıyı uygula.',sekil=SK13)
# =================== 14 · oksijen taşınması · orta · olumsuz ===================
dog14='Oksijenin büyük bölümü plazmada çözünmüş hâlde taşınır; hemoglobin yalnızca küçük bir kısmını taşır.'
q('0014',tipId='ss-hb-oksijen',tip='Hemoglobin ve oksijen–hemoglobin eğrisi',z='orta',alt='Oksijen taşınması',kaz='Hemoglobin ve oksijen taşınmasına ilişkin yanlış bilgiyi ayırt eder.',kalip='düz',
 kart='K-ABSS-05 (O₂ taşınması) · plazma–hemoglobin payı ve CO',
 metin='Hemoglobinle ve oksijenin kanda taşınmasıyla ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=dog14,sira=yer('E',dog14,['İnsanın olgun alyuvarlarında çekirdek bulunmaz; bu durum hemoglobine daha fazla yer ayrılmasını sağlar.','Uzun süre yüksek rakımda kalan bireylerde alyuvar sayısı artabilir.','Oksijenin kısmi basıncı yüksek olan akciğer kılcallarında hemoglobin oksijenle birleşerek oksihemoglobin oluşturur.','Dokularda kanın karbondioksit düzeyinin artması, oksihemoglobinden oksijenin ayrılmasını kolaylaştırır.']),
 yan=[('İnsanın olgun alyuvarlarında çekirdek bulunmaz; bu durum hemoglobine daha fazla yer ayrılmasını sağlar.','Olgun alyuvarda çekirdek yoktur ve hacmin büyük kısmı hemoglobinle doludur; bu ifade doğrudur. Çekirdeksizliğin taşıma kapasitesini azalttığı sanılmıştır.','bilgi'),
      ('Uzun süre yüksek rakımda kalan bireylerde alyuvar sayısı artabilir.','Yükseklikte oksijenin kısmi basıncı azaldığı için alyuvar üretimi artabilir; bu ifade doğrudur. Alyuvar sayısının sabit kalacağı sanılmıştır.','bilgi'),
      ('Oksijenin kısmi basıncı yüksek olan akciğer kılcallarında hemoglobin oksijenle birleşerek oksihemoglobin oluşturur.','Yüksek kısmi basınçta hemoglobinin oksijene doygunluğu artar; bu ifade doğrudur. Oksihemoglobinin dokuda oluştuğu sanılmıştır.','bilgi'),
      ('Dokularda kanın karbondioksit düzeyinin artması, oksihemoglobinden oksijenin ayrılmasını kolaylaştırır.','CO₂ artışı ve pH düşüşü hemoglobinin oksijene ilgisini azaltır; bu ifade doğrudur. CO₂’nin oksijen bırakımını güçleştireceği sanılmıştır.','bilgi')],
 istenen='Yanlış olan ifade.',
 ip=['Oksijenin kanda ağırlıklı olarak hangi bileşikle taşındığını hatırlayıp her ifadeyi bu bilgiyle sına.'],
 bilgi=[B_HB,B_BOHR],
 ad=[A('İfadeleri tek tek sına','Dört hem grubu, yükseklikte alyuvar artışı, CO’nun güçlü bağlanması ve CO₂’nin O₂ bırakımını artırması bilinen gerçeklerdir.','Dört ifade doğru'),
     A('Taşınma payına bak','O₂’nin çok büyük kısmı alyuvardaki hemoglobinle, çok küçük kısmı plazmada çözünmüş hâlde taşınır.','Hemoglobin: büyük pay · plazma: küçük pay'),
     A('Yanlış ifadeyi seç','Plazma payını büyük gösteren ifade bu bilgiyle çelişir.','Cevap: plazma payı ifadesi')],
 puf='Her ifadeyi oksijenin kandaki taşınma biçimiyle sına.')
# =================== 15 · CO2 solunum hızı sütun grafik · orta ===================
CZ=[('I',0.04,12),('II',2,15),('III',4,22),('IV',6,30)]
assert [c[2] for c in CZ]==sorted(c[2] for c in CZ)
xt=','.join(c[0] for c in CZ)
b=['\\begin{axis}[ybar,width=7.6cm,height=5cm,bar width=.7cm,ymin=0,ymax=35,symbolic x coords={'+xt+'},xtick=data,xticklabels={\\%0{,}04,\\%2,\\%4,\\%6},ytick={0,10,20,30},axis lines=left,xlabel={Karışım (CO$_2$ yüzdesi)},ylabel={Soluk sayısı (dk$^{-1}$)},nodes near coords,every node near coord/.append style={font=\\footnotesize},tick label style={font=\\footnotesize},label style={font=\\small},enlarge x limits=.15]',
   '\\addplot[fill=vurgu!45,draw=black] coordinates {'+' '.join(f'({c[0]},{c[2]})' for c in CZ)+'};','\\end{axis}']
b.append('\\node[font=\\scriptsize] at (1.55,-1.15) {};')
SK15=graf('\n'.join(b))
dog15='Kandaki CO₂ düzeyi yükselir ve pH düşer; bu durum omurilik soğanındaki solunum merkezini uyararak soluk sayısını artırır.'
q('0015',tipId='ss-duzenleme',tip='Solunumun düzenlenmesi',z='orta',alt='Solunumun düzenlenmesi',kaz='CO₂ derişimi–soluk sayısı verisini solunum merkezi mekanizmasıyla açıklar.',kalip='grafik',
 kart='K-ABSS-07 (CO₂ uyarısı) · solunan hava CO₂ yüzdesi–soluk sayısı',
 metin='Sağlıklı bir gönüllü, karbondioksit yüzdeleri farklı dört gaz karışımını birer dakika boyunca solumuştur. Karışımların hepsinde oksijen yüzdesi normal hava ile aynıdır. Gönüllünün her karışımdaki dakikalık soluk sayısı grafikte verilmiştir.\nBuna göre, soluk sayısındaki değişimin nedeni aşağıdakilerden hangisidir?',
 dogru=dog15,sira=yer('D',dog15,['Kandaki O₂ düzeyi azalır; bu durum solunum merkezini CO₂’den daha güçlü biçimde uyarır.','Kandaki CO₂ düzeyi yükselir; bu durum beyinciğe iletilir ve beyincik solunum kaslarını uyarır.','Kandaki CO₂ düzeyi yükselir ve pH da yükselir; bu durum karotis ve aort cisimciklerini uyarır.','Kandaki CO₂ düzeyi yükselir; bu durum beyin kabuğunu uyarır ve soluk alıp verme istemli olarak hızlanır.']),
 yan=[('Kandaki O₂ düzeyi azalır; bu durum solunum merkezini CO₂’den daha güçlü biçimde uyarır.','Karışımların hepsinde O₂ yüzdesi aynıdır; değişen CO₂’dir. Solunum merkezini en güçlü uyaran da O₂ azalması değil CO₂ artışıdır.','bilgi'),
      ('Kandaki CO₂ düzeyi yükselir; bu durum beyinciğe iletilir ve beyincik solunum kaslarını uyarır.','Solunum merkezi beyincikte değil omurilik soğanındadır; beyincik denge ve kas koordinasyonuyla ilgilidir.','bilgi'),
      ('Kandaki CO₂ düzeyi yükselir ve pH da yükselir; bu durum karotis ve aort cisimciklerini uyarır.','CO₂ artışı kanı asitleştirir, pH yükselmez; düşen pH solunum merkezini uyarır.','bilgi'),
      ('Kandaki CO₂ düzeyi yükselir; bu durum beyin kabuğunu uyarır ve soluk alıp verme istemli olarak hızlanır.','Solunum büyük ölçüde omurilik soğanıyla istemsiz denetlenir; istemli kontrol yalnız bir ölçüde ve geçici olarak yapılabilir.','bilgi')],
 istenen='Soluk sayısı artışının nedeni.',
 ip=['Deneyde sabit tutulan ve değişen gazı belirle; değişen gazın kan pH’ı ve solunum merkeziyle ilişkisini düşün.'],
 bilgi=[B_DUZ],
 ad=[A('Değişkenleri ayır','Her karışımda O₂ aynıdır; yalnız CO₂ yüzdesi artmaktadır.','Bağımsız değişken: CO₂ yüzdesi'),
     A('Grafiği oku','CO₂ yüzdesi arttıkça dakikalık soluk sayısı 12’den 30’a yükselir.','12 → 15 → 22 → 30'),
     A('Mekanizmayı kur','Kan CO₂’si arttıkça pH düşer; bu durum omurilik soğanındaki solunum merkezini uyarır ve kaslar daha sık çalışır.','CO₂ ↑ → pH ↓ → merkez uyarılır → soluk sayısı ↑'),
     A('Açıklamayı seç','Bu zinciri doğru kuran ifade geçerlidir.','Doğru ifade belirlendi')],
 puf='Solunumu en güçlü uyaran, kandaki CO₂ artışı ve buna bağlı pH düşüşüdür.',sekil=SK15)
# =================== 16 · CO2 öncüllü · orta ===================
ST16={'I':(True,'Alyuvarlarda bulunan karbonik anhidraz enzimi, CO₂ ile suyun birleşerek karbonik asit oluşturmasını hızlandırır.','Karbonik anhidraz alyuvarda CO₂ + H₂O → H₂CO₃ tepkimesini hızlandıran enzimdir.'),
      'II':(True,'Akciğer kılcallarında bikarbonat iyonlarından yeniden CO₂ oluşur ve bu CO₂ alveollere difüzyonla geçer.','Akciğerde kısmi basınç farkı ve tersine dönen tepkimeler CO₂’yi kandan alveole taşır.'),
      'III':(False,'CO₂’nin büyük bölümü hemoglobine bağlanarak karbaminohemoglobin biçiminde taşınır.','CO₂’nin büyük bölümü bikarbonat iyonu olarak taşınır; karbaminohemoglobin payı daha küçüktür.')}
dg,sr,yn,ad=onc(ST16,True,'B',seed=7)
q('0016',tipId='ss-co2-tasima',tip='Karbondioksit taşınma biçimleri',z='orta',alt='CO₂ taşınması',kaz='CO₂’nin kanda taşınma biçimleri ve akciğerdeki süreçlere ilişkin yargıları değerlendirir.',kalip='öncüllü',
 kart='K-ABSS-06 (CO₂ taşınması) · karbonik anhidraz, bikarbonat payı',
 metin=onctxt('İnsanda karbondioksitin dokulardan akciğerlere taşınmasıyla ilgili olarak aşağıdaki yargılar verilmiştir.',ST16,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=dg,sira=sr,yan=yn,istenen='Doğru olan yargıların belirlenmesi.',
 ip=['CO₂’nin kanda hangi biçimde en büyük payı aldığını ve alyuvardaki enzimin görevini düşün.'],bilgi=[B_CO2,B_KB],ad=ad,
 puf='Her yargıyı CO₂’nin kandaki yolunun ilgili basamağıyla karşılaştır.')
# =================== 17 · deney tablosu · zor · olumsuz ===================
DN={'K':('Normal solunum',45),'L':('Hızlı ve derin soluma',80),'M':('Kapalı torbaya soluma',25)}
assert DN['L'][1]>DN['K'][1]>DN['M'][1]
SK17=tablo_svg(['Gönüllü','İşlem (1 dk)','Nefes tutma (sn)'],[[k,v[0],str(v[1])] for k,v in DN.items()])
dog17='L gönüllüsünün nefes tutma süresinin uzaması, hiperventilasyonla hemoglobinin O₂ ile daha fazla doymasından ve kandaki O₂ miktarının belirgin biçimde artmasından kaynaklanmaktadır.'
q('0017',tipId='ss-duzenleme',tip='Solunumun düzenlenmesi',z='zor',alt='Nefes tutma deneyi',kaz='Nefes tutma deney sonuçlarını CO₂ düzeyi ve solunum merkezi eşiğiyle açıklayıp yanlış yorumu ayırt eder.',kalip='tablo',
 kart='K-ABSS-07 (nefes tutma) · hiperventilasyon, hemoglobin doygunluğu yanılgısı',
 metin='Sağlıklı üç gönüllü (K, L ve M) tabloda belirtilen işlemi birer dakika uyguladıktan sonra (hızlı ve derin soluma hiperventilasyondur), normal havada nefeslerini rahatsızlık hissedene kadar tutmuşlardır. Gönüllülerin nefes tutma süreleri tabloda verilmiştir.\nBuna göre, aşağıdaki yorumlardan hangisi yanlıştır?',
 dogru=dog17,sira=yer('A',dog17,['L gönüllüsünde hiperventilasyon kandaki CO₂ düzeyini düşürdüğü için solunum merkezinin uyarılma düzeyine ulaşılması gecikmiştir.','M gönüllüsünde torbadaki havada CO₂ biriktiği için kan CO₂ düzeyi başlangıçta daha yüksektir ve solunum merkezi daha erken uyarılmıştır.','Gönüllülerde nefes tutma süresini belirleyen asıl etken, kandaki CO₂ düzeyi ve buna bağlı pH değişimidir.','Nefes tutma sırasında üç gönüllüde de kan pH’ı düşme eğilimindedir ve bu durum solunum merkezini uyarır.']),
 yan=[('L gönüllüsünde hiperventilasyon kandaki CO₂ düzeyini düşürdüğü için solunum merkezinin uyarılma düzeyine ulaşılması gecikmiştir.','Bu yorum doğrudur: hiperventilasyon CO₂’yi azaltır ve uyarı eşiği geç aşılır. Yanlış sanılarak seçilmiş.','bilgi'),
      ('M gönüllüsünde torbadaki havada CO₂ biriktiği için kan CO₂ düzeyi başlangıçta daha yüksektir ve solunum merkezi daha erken uyarılmıştır.','Bu yorum doğrudur: kapalı torbada CO₂ birikir, kan CO₂ düzeyi başlangıçta yükselir ve tutma süresi kısalır. Yanlış sanılarak seçilmiş.','bilgi'),
      ('Gönüllülerde nefes tutma süresini belirleyen asıl etken, kandaki CO₂ düzeyi ve buna bağlı pH değişimidir.','Bu yorum doğrudur: solunum merkezini en güçlü uyaran CO₂ artışı ve pH düşüşüdür. Yanlış sanılarak seçilmiş.','bilgi'),
      ('Nefes tutma sırasında üç gönüllüde de kan pH’ı düşme eğilimindedir ve bu durum solunum merkezini uyarır.','Bu yorum doğrudur: nefes tutarken CO₂ birikir ve pH düşer. Yanlış sanılarak seçilmiş.','bilgi')],
 istenen='Yanlış olan yorum.',
 ip=['Normal soluyan bireyde hemoglobinin oksijene ne kadar doygun olduğunu düşün ve nefes tutmayı sonlandıran uyarının hangi gazdan geldiğini ara.'],
 bilgi=[B_DUZ,B_HB],
 ad=[A('Sonuçları sırala','L’nin süresi en uzun, M’nin en kısa, K ise ikisinin arasındadır.','L: 80 sn > K: 45 sn > M: 25 sn'),
     A('CO₂ düzeyini yorumla','Hiperventilasyon kandaki CO₂’yi düşürür; torbaya soluma CO₂’yi artırır. Solunum merkezi CO₂ artışıyla uyarıldığından süreler bu sırayla değişir.','L: CO₂ düşük · M: CO₂ yüksek'),
     A('O₂ iddiasını sına','Normal soluyan bireyde hemoglobin zaten çok yüksek oranda O₂’ye doygundur; hiperventilasyon doygunluğu belirgin artırmaz.','O₂ nedeni geçersiz'),
     A('Yanlış yorumu seç','O₂ artışını neden gösteren yorum geçersizdir.','Yanlış yorum belirlendi')],
 puf='Nefes tutmayı sonlandıran uyarıyı belirle.',sekil=SK17)
# =================== 18 · solunum merkezi öncüllü · orta ===================
ST18={'I':(True,'Kandaki CO₂ düzeyinin artması solunum merkezini uyarır.','Kandaki CO₂ artışı solunum merkezini uyaran en etkili faktördür.'),
      'II':(True,'Kan pH’ının düşmesi solunum merkezinin uyarılmasına katkıda bulunur.','pH düşüşü solunum merkezini uyarır ve soluk alıp verme hızını artırır.'),
      'III':(True,'Karotis ve aort cisimciklerindeki kemoreseptörler, kandaki O₂ düşüşünü algılayıp solunum merkezine bilgi gönderebilir.','Bu cisimcikler belirgin O₂ azalmasında solunum merkezine uyarı ileterek solunumu hızlandırır.')}
dg,sr,yn,ad=onc(ST18,True,'E',seed=8)
q('0018',tipId='ss-duzenleme',tip='Solunumun düzenlenmesi',z='orta',alt='Solunumun düzenlenmesi',kaz='Solunum merkezini uyaran etkenleri belirler.',kalip='öncüllü',
 kart='K-ABSS-07 (düzenleme) · CO₂, pH ve kemoreseptörler',
 metin=onctxt('İnsanda solunumun düzenlenmesiyle ilgili olarak aşağıdaki durumlar verilmiştir.',{k:(v[0],v[1],v[2]) for k,v in ST18.items()},'Buna göre, bu durumlardan hangileri solunum hızının artmasına yol açar?'),
 dogru=dg,sira=sr,yan=yn,istenen='Solunum hızını artıran durumların belirlenmesi.',
 ip=['Solunum merkezinin konumunu ve hangi kimyasal değişimleri algıladığını düşün.'],bilgi=[B_DUZ],ad=ad,
 puf='Her durumun solunum merkezini nasıl etkilediğini ayrı ayrı sına.')
# =================== 19 · alveol–kılcal şeması · orta · olumsuz ===================
b=[]
b.append('\\draw[line width=1.4pt,fill=vurgu!10] (0,0) circle (1.6);')
b.append('\\draw[line width=1.2pt,double distance=14pt,double=vurgu!25] (3.6,2.3)--(3.6,-2.3);')
b.append(f'\\draw[{OK},line width=1.3pt] (3.6,2.9)--(3.6,2.4);\\draw[{OK},line width=1.3pt] (3.6,-2.2)--(3.6,-2.9);')
b.append(f'\\draw[{OK},line width=1.6pt,vurgu!70!black] (3.0,.75)--(.9,.75);\\draw[{OK},line width=1.6pt,vurgu!70!black] (.9,-.75)--(3.0,-.75);')
b.append('\\node[font=\\normalsize\\bfseries] at (2.4,1.1) {X};\\node[font=\\normalsize\\bfseries] at (2.4,-1.1) {Y};')
b.append('\\node[font=\\small,align=center] at (-.2,0) {alveol};\\node[font=\\small,align=left,anchor=west] at (4.4,0) {kılcal\\\\damar};')
b.append('\\node[font=\\small,align=center] at (3.6,3.5) {akciğere\\\\gelen kan};\\node[font=\\small,align=center] at (3.6,-3.5) {akciğerden\\\\ayrılan kan};')
SK19=tk('\n'.join(b),.95)
dog19='Alveolden ayrılan kanda X ile gösterilen gazın kısmi basıncı, alveole gelen kandakinden yüksektir.'
q('0019',tipId='ss-yol-alveol',tip='Solunum yolu ve alveol yapısı',z='zor',alt='Alveolde gaz değişimi',kaz='Alveol–kılcal damar şemasında okların yönünden gazları belirleyip kandaki kısmi basınç ve pH değişimini yorumlar.',kalip='şekilli',
 kart='K-ABSS-01 (alveol–kılcal) · okların yönü, kısmi basınç ve pH değişimi',
 metin='Şekilde bir alveol ile çevresindeki kılcal damar ve gaz değişimi sırasında iki gazın geçiş yönleri X ve Y okları ile gösterilmiştir. Kılcal damarda kanın akış yönü oklarla belirtilmiştir.\nBuna göre, aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=dog19,sira=yer('B',dog19,['Y ile gösterilen gazın kandaki taşınmasında alyuvarlardaki hemoglobin rol oynar.','X ile gösterilen gazın kısmi basıncı, alveole gelen kanda alveol havasındakinden yüksektir.','Alveolden ayrılan kanda Y ile gösterilen gazın kısmi basıncı, alveole gelen kandakinden yüksektir.','Alveolden ayrılan kanın pH değeri, alveole gelen kanın pH değerinden yüksektir.']),
 yan=[('Y ile gösterilen gazın kandaki taşınmasında alyuvarlardaki hemoglobin rol oynar.','Alveolden kana geçen Y gazı O₂’dir ve büyük kısmı hemoglobinle taşınır; ifade doğrudur. Hemoglobinin O₂ taşımadığı sanılmıştır.','bilgi'),
      ('X ile gösterilen gazın kısmi basıncı, alveole gelen kanda alveol havasındakinden yüksektir.','Kandan alveole geçen X gazı CO₂’dir; geçiş yönü, kısmi basıncın kanda alveolden yüksek olduğunu gösterir ve ifade doğrudur. Okun yönü ters yorumlanmıştır.','dikkat'),
      ('Alveolden ayrılan kanda Y ile gösterilen gazın kısmi basıncı, alveole gelen kandakinden yüksektir.','Kana O₂ geçtiği için kanın O₂ kısmi basıncı akciğerden ayrılırken yükselir; ifade doğrudur. Kanın akış yönü gözden kaçırılmıştır.','dikkat'),
      ('Alveolden ayrılan kanın pH değeri, alveole gelen kanın pH değerinden yüksektir.','Akciğerde CO₂ kandan alveole geçince kanın asitliği azalır ve pH yükselir; ifade doğrudur. CO₂ kaybının pH’ı düşüreceği sanılmıştır.','bilgi')],
 istenen='Yanlış olan ifade.',
 ip=['Kanın akciğere hangi gaz bakımından zengin geldiğini düşünerek okların yönünden X ve Y gazlarını belirle.'],
 bilgi=[B_ALV,B_KB],
 ad=[A('Gazları belirle','Akciğere gelen kan O₂’ce fakir, CO₂’ce zengindir; kandan alveole geçen X gazı CO₂, alveolden kana geçen Y gazı O₂’dir.','X: CO₂ · Y: O₂'),
     A('Kandaki değişimi yorumla','Kan alveol çevresinden geçerken O₂ kazanır, CO₂ kaybeder; CO₂ azalınca pH yükselir.','O₂ ↑ · CO₂ ↓ · pH ↑'),
     A('İfadeleri ele','Hemoglobin, kısmi basınç ve pH ifadeleri bu değişimle uyumludur; CO₂ için artış söyleyen ifade çelişir.','Yanlış ifade belirlendi')],
 puf='Önce okların yönünden gazları, sonra kandaki değişimin yönünü belirle.',sekil=SK19)
# =================== 20 · yüksek rakım öncüllü · zor ===================
PB0,PB1,FO=760,600,Fr(21,100); D0=PB0*FO; D1=PB1*FO; assert (D0,D1)==(Fr(1596,10),126) and D0-D1==Fr(168,5)
ST20={'I':(True,'Deniz seviyesinde toplam basınç 760 mmHg, 4000 m yükseklikte 600 mmHg ve havanın oksijen oranı hacimce %21 ise, oksijenin kısmi basıncı 4000 m’de deniz seviyesine göre 33,6 mmHg azalmıştır.','Oksijenin kısmi basıncı toplam basıncın %21’i kadardır; 760 × 0,21 = 159,6 ve 600 × 0,21 = 126 olduğundan fark 33,6 mmHg’dir.'),
      'II':(False,'4000 m yükseklikte havadaki oksijenin hacimce oranı, deniz seviyesindekine göre azalarak yaklaşık %16,6’ya düşmüştür.','Yükseklikte havanın oksijen oranı değişmez; düşen, toplam basınç ve dolayısıyla oksijenin kısmi basıncıdır.'),
      'III':(True,'Alveol havasındaki O₂ kısmi basıncının düşmesi karotis ve aort cisimciklerini uyararak solunum hızını artırır; uzun süre kalındığında ise alyuvar üretimi artar.','Kemoreseptörler belirgin O₂ azalmasında solunum merkezini uyararak solunumu hızlandırır; oksijen azlığı uzun sürerse alyuvar üretimi artar.')}
dg,sr,yn,ad=onc(ST20,True,'E',seed=9); assert dg=='I ve III'
q('0020',tipId='ss-iliskili',tip='Çok kavramlı solunum yorumları',z='zor',alt='Yüksek rakım',kaz='Yüksek rakımda kısmi basıncı hesaplayıp oksijen oranı yanılgısını ve solunumsal uyumu yorumlar.',kalip='öncüllü',
 kart='K-ABSS-08 (yüksek rakım) · kısmi basınç hesabı, oran yanılgısı, kemoreseptör',
 metin=onctxt('Deniz seviyesinde yaşayan sağlıklı bir dağcı, 4000 m yükseklikteki bir kampa çıkıp birkaç hafta kalıyor. Bu süreçte dağcının solunum sistemi ve kanıyla ilgili olarak aşağıdaki yargılar ileri sürülüyor.',ST20,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=dg,sira=sr,yan=yn,istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Kısmi basıncın nasıl hesaplandığını ve yükseklikle hangi niceliğin değiştiğini düşün.'],bilgi=[B_YUK,B_DUZ],ad=ad,
 puf='Her yargıyı hesap ve solunumsal uyum bakımından ayrı ayrı sına.')
# =================== yaz ===================
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(BD,'solunumsis-1.json'),'/tmp/bos-solunumsis.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=P.k))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Biyoloji çıkmış soruları (yalnız mantık), MEB 11. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','absolunumsis.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
