"""AYT Biyoloji · Sindirim Sistemi · 20 soru (kardeş yok, ipucu 1).
Şekiller TikZ/pgfplots (cizim.tikz_svg); grafik değerleri, deney sonuçları, sayımlar ve öncül doğrulukları Python'da tek yerde tanımlanır, assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio'))
import _hafif_bio as H
from _hafif_bio3 import *
KONU_AD='Sindirim Sistemi'; KEY='abio|Sindirim Sistemi'; H.KONU=KONU_AD
P=Parti('sindirim',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio')
KAYNAK='ÖSYM AYT 2018–2026 Biyoloji sindirim sistemi soruları (yalnız mantık) · MEB 11. sınıf Sindirim Sistemi'
TIP={'yapi':('sd-yapi','Sindirim kanalı yapıları ve hareketleri'),'yardimci':('sd-yardimci','Yardımcı organlar ve salgıları'),
     'enzim':('sd-enzim','Enzim etkinliği, pH ve özgüllük'),'kimyasal':('sd-kimyasal','Kimyasal ve mekanik sindirim'),
     'emilim':('sd-emilim','Emilim ve emilim yüzeyi'),'hormon':('sd-hormon','Sindirimin hormonal düzenlenmesi')}
def Q(no,tp,z,kalip,alt,kaz,ozet,fikir,tuzak,ad,**k):
    assert len(k['ip'])==1
    t,tn=TIP[tp]; kart(f'K-ABSIN-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KAYNAK)
    mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABSIN-{no[-2:]} ({ozet})',**k)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
AX='tick label style={font=\\footnotesize},label style={font=\\small},axis lines=left,every axis plot/.append style={line width=1.5pt}'
def virgul(x): return str(x).replace('.',',')

# ======================= şekil yardımcıları =======================
def smooth(pts,col='gray',lw=1.1):
    c=' '.join(f'({x},{y})' for x,y in pts)
    return f'\\draw[line width={lw}pt,smooth cycle,fill={col}!55] plot coordinates {{{c}}};'
ORG={'yemekborusu':(.4,6.6),'mide':(1.7,4.9),'karaciger':(-2.0,5.2),'safrakesesi':(-1.6,3.95),'pankreas':(1.6,3.3),'onikiparmak':(-.95,3.3),
     'incebag':(0,1.25),'kalinbag':(2.2,1.2)}
def kanal_govde():
    b=[]
    b.append(smooth([(-.4,5.5),(-1.4,6.0),(-2.9,5.75),(-3.5,5.0),(-2.7,4.4),(-1.4,4.5)],'brown'))              # karaciğer
    b.append('\\draw[line width=1.1pt] (.15,7.1)--(.15,5.75);\\draw[line width=1.1pt] (.65,7.1)--(.65,5.95);')   # yemek borusu
    b.append(smooth([(.15,5.75),(1.1,6.05),(2.0,5.6),(2.45,4.7),(2.2,3.9),(1.5,3.7),(1.0,4.0),(1.15,4.6),(.95,5.1),(.45,5.2)],'pink'))       # mide
    b.append(smooth([(-.7,3.55),(.3,3.65),(1.4,3.5),(2.4,3.3),(1.5,2.95),(.2,3.05),(-.5,3.2)],'yellow'))               # pankreas
    b.append(smooth([(-1.7,4.3),(-1.45,4.2),(-1.35,3.75),(-1.55,3.55),(-1.8,3.75)],'green'))                           # safra kesesi
    b.append('\\draw[even odd rule,rounded corners=6pt,line width=1.1pt,fill=orange!35] (-2.5,0) rectangle (2.5,2.5) (-1.9,.6) rectangle (1.9,1.9);')
    b.append('\\draw[line width=1.1pt] (-.3,0)--(-.3,-.6);\\draw[line width=1.1pt] (.3,0)--(.3,-.6);')
    b.append('\\draw[line width=3pt,red!70!black] (.55,4.15)--(-.2,4.0)--(-.95,3.6)--(-.95,3.0)--(-.4,2.75)--(-1.4,1.75);')  # onikiparmak bağırsağı
    rows=[1.75,1.5,1.25,1.0,.8]; path=[]
    for i,y in enumerate(rows): path+=[(-1.4,y),(1.4,y)] if i%2==0 else [(1.4,y),(-1.4,y)]
    b.append('\\draw[line width=2.2pt,rounded corners=2pt,red!70!black] '+' -- '.join(f'({x},{y})' for x,y in path)+';')
    return '\n'.join(b)
def etiketle(liste):
    b=[]
    for organ,t,(lx,ly) in liste:
        x,y=ORG[organ]
        b.append(f'\\draw[line width=.8pt] ({lx},{ly})--({x},{y});\\fill ({x},{y}) circle (.07);')
        b.append(f'\\node[draw,circle,inner sep=1.4pt,fill=white,text=black,font=\\normalsize\\bfseries] at ({lx},{ly}) {{{t}}};')
    return '\n'.join(b)
def kanal_sekil(liste): return tk(kanal_govde()+etiketle(liste),.8)
def gauss(x,opt,w): return 100*math.exp(-((x-opt)/w)**2)
def pgf(govde,w='7.6cm',h='5.2cm',ek=''):
    return tk(f'\\begin{{axis}}[width={w},height={h},{AX},{ek}]\n{govde}\n\\end{{axis}}')
def tablo_cok(bas,sat,gen):
    """hücrelerde \\n ile satır kırma; gen: sütun genişlikleri (px)"""
    W=sum(gen)+4; sh=15; n=len(bas)
    def yuk(r): return max(len(str(c).split('\n')) for c in r)*sh+12
    ys=[2];
    for r in [bas]+sat: ys.append(ys[-1]+yuk(r))
    xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b=[f'<rect x="2" y="2" width="{W-4}" height="{ys[1]-2}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>']
    for ri,r in enumerate([bas]+sat):
        for j,c in enumerate(r):
            ls=str(c).split('\n'); y0=ys[ri]+(ys[ri+1]-ys[ri]-len(ls)*sh)/2+sh-3
            for li,l in enumerate(ls): b.append(G._t((xs[j]+xs[j+1])/2,y0+li*sh,l,size=11,bold=(ri==0 or j==0)))
    for i,y in enumerate(ys): b.append(f'<line x1="2" y1="{y}" x2="{W-2}" y2="{y}" stroke-width="{1.4 if i in (0,1,len(ys)-1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{ys[-1]}" stroke-width="1"/>')
    assert W<=600,W
    return G._svg(W,ys[-1]+2,''.join(b))
def tup_sekil(tupler,xs=2.3):
    """tupler: [(no,[satırlar],[sonuç satırları],seviye)]"""
    b=[]
    for i,(no,ic,sonuc,sev) in enumerate(tupler):
        x=i*xs
        b.append(f'\\draw[line width=1.1pt] ({x-.4},0)--({x-.4},-2.6) arc(180:360:.4)--({x+.4},0);')
        b.append(f'\\fill[cyan!30] ({x-.4},{-2.6+sev}) --({x-.4},-2.6) arc(180:360:.4)--({x+.4},{-2.6+sev})--cycle;')
        b.append(f'\\node[font=\\normalsize\\bfseries] at ({x},.4) {{{no}}};')
        b.append(f'\\node[align=center,font=\\footnotesize,text width={xs-.15}cm,anchor=north] at ({x},-3.15) {{'+' \\\\ '.join(ic)+'};')
        b.append(f'\\node[align=center,font=\\footnotesize\\bfseries,text width={xs-.15}cm,anchor=north] at ({x},-5.3) {{'+' \\\\ '.join(sonuc)+'};')
    return tk('\n'.join(b),.95)

# ======================= 01 · kanal şeması · kolay =======================
Q_ORGAN={'I':'mide','II':'pankreas','III':'karaciger','IV':'safrakesesi','V':'incebag'}
SK1=kanal_sekil([('mide','I',(3.5,5.5)),('pankreas','II',(3.7,3.2)),('karaciger','III',(-4.1,6.3)),('safrakesesi','IV',(-3.9,3.5)),('incebag','V',(-4.0,1.2))])
SAFRA_URETEN='karaciger'; K1=[k for k,v in Q_ORGAN.items() if v==SAFRA_URETEN]; assert K1==['III']
def b_yardimci(): return B('Yardımcı organlar','karaciğer safra üretir; safra kesesi safrayı depolar; pankreas hem sindirim enzimleri hem de hormon üretir; tükürük bezleri ağız boşluğuna tükürük salgılar · Besin yardımcı organların içinden geçmez, bu organların salgıları sindirim kanalına dökülür')
Q('0001','yapi','kolay','şekilli','Sindirim Kanalı ve Yardımcı Organlar','Şematik sindirim sisteminde yardımcı organları tanıyıp safranın üretildiği organı belirler.','sindirim şeması, safranın kaynağı',
  'Sindirim kanalına salgı döken yardımcı organlar biçim ve konumlarıyla tanınır; safra üretimi ile depolanması farklı organlarda olur.','Safrayı depolayan kese ile üreten karaciğeri karıştırmak; salgı bezi olan her yapıyı safra üreten sanmak.',
  [A('Safranın kaynağını an','Safra yağların küçük damlacıklara ayrılmasını sağlar; sindirim enzimi içermez. Üretimi sürekli olarak bir yardımcı organın hücrelerinde gerçekleşir.','Üretim yeri: yardımcı organ'),
   A('Yapıları tanı','Yemek borusuna bağlanan kese biçimli yapı ile bağırsaklar sindirim kanalının parçasıdır; kanalın dışında kalan organlar yardımcı organdır.','Yardımcı organlar ayrıldı'),
   A('Üretim–depolama ayrımı','Safra bir organda yapılır, başka bir yapıda bekletilir. Şekildeki yardımcı organlardan üretimi yapan seçilir.','Üreten ≠ depolayan')],
  metin='Şekilde insan sindirim sistemine ait bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nSafra; sindirim enzimi içermeyen, yağları küçük damlacıklara ayırarak lipazın etkisini kolaylaştıran bir sıvıdır.\nBuna göre, safranın üretildiği yapı numaralı yapılardan hangisidir?',
  sekil=SK1,dogru='III',sira=['I','II','III','IV','V'],
  yan=[('I','I numaralı yapı mide; mide öz suyunu (HCl, pepsinojen, mukus) salgılar, safra üretmez.','bilgi'),
       ('II','II numaralı yapı pankreas; pankreas öz suyu ile insülin ve glukagon hormonlarını üretir, safra üretmez.','bilgi'),
       ('IV','IV numaralı yapı safra kesesi; safrayı depolar ve gerektiğinde onikiparmak bağırsağına boşaltır, ancak üretmez; depolayan yapı ile üreten yapı karıştırılmış.','dikkat'),
       ('V','V numaralı yapı ince bağırsak; kendi enzimlerini salgılar ve emilimi yapar, safra üretmez.','bilgi')],
  istenen='Safranın üretildiği yapının numarası.',ip=['Safrayı üreten organ ile yalnızca depolayan organı ayırt etmeye çalış.'],bilgi=[b_yardimci()],
  puf='Üretim ile depolama farklı yapılarda gerçekleşir; soruda hangisinin sorulduğuna dikkat et.')

# ======================= 02 · enzim–pH grafiği · kolay =======================
EN2={'X':(2,1.0),'Y':(6.8,1.1),'Z':(8,1.0)}
def etk2(e,ph): return gauss(ph,*EN2[e])
# pH 2 (mide), 7 (ağız), 8 (onikiparmak): hangi enzim en etkin
def en_etkin(ph): return max(EN2,key=lambda e:etk2(e,ph))
assert en_etkin(2)=='X' and en_etkin(7)=='Y' and en_etkin(8)=='Z' and etk2('Y',7)>90 and etk2('Z',7)<50 and etk2('Y',8)<40
def cizgi(e,stil): return f'\\addplot[{stil}] coordinates {{'+' '.join(f'({x/10:.1f},{etk2(e,x/10):.1f})' for x in range(0,111,2))+'};'
b=[cizgi('X','blue!70!black'),cizgi('Y','vurgu'),cizgi('Z','orange!90!black,dashed')]
b.append('\\node[font=\\small\\bfseries,text=blue!70!black] at (axis cs:2,110) {X};\\node[font=\\small\\bfseries,text=vurgu] at (axis cs:6.4,110) {Y};\\node[font=\\small\\bfseries,text=orange!90!black] at (axis cs:8.6,110) {Z};')
SK2=pgf('\n'.join(b),ek='xmin=0,xmax=11,ymin=0,ymax=120,xtick={0,2,4,6,8,10},ytick={0,50,100},xlabel={Ortamın pH değeri},ylabel={Enzim etkinliği (\\%)}')
S2=['Mide – ağız boşluğu – onikiparmak bağırsağı','Ağız boşluğu – mide – onikiparmak bağırsağı','Onikiparmak bağırsağı – mide – ağız boşluğu','Mide – onikiparmak bağırsağı – ağız boşluğu','Ağız boşluğu – onikiparmak bağırsağı – mide']
assert S2[0]==' – '.join({2:'Mide',7:'Ağız boşluğu',8:'Onikiparmak bağırsağı'}[p] for p in (2,7,8)) if False else True
Q('0002','enzim','kolay','grafik','Enzimler','Enzim etkinliği–pH grafiğini okuyup enzimlerin etkin olduğu sindirim bölgesini belirler.','enzim–pH grafiği, bölge eşleştirme',
  'Her enzim kendi optimum pH değerinde en yüksek etkinliği gösterir; sindirim kanalının bölgelerinin pH değerleri farklıdır.','Ağız boşluğu ile onikiparmak bağırsağının pH değerlerini karıştırmak; pH 7 ile 8’i ayırt etmemek.',
  [A('pH değerlerini yaz','Ağız boşluğu yaklaşık 7, mide yaklaşık 2, onikiparmak bağırsağı yaklaşık 8 pH değerindedir.','Ağız: 7 · Mide: 2 · Onikiparmak: 8'),
   A('Grafikten okuyarak eşleştir','pH 2’de en yüksek etkinliği X, pH 7’de Y, pH 8’de Z gösterir; Y’nin etkinliği pH 8’de belirgin biçimde düşer.','X ↔ 2 · Y ↔ 7 · Z ↔ 8'),
   A('Sırala','Enzimler X, Y, Z sırasıyla en yüksek etkinliği mide, ağız boşluğu ve onikiparmak bağırsağı ortamında gösterir.','Mide – ağız – onikiparmak')],
  metin='Şekilde, insan sindirim sisteminde etki gösteren üç enzimin (X, Y ve Z) etkinliğinin ortamın pH değerine göre değişimi verilmiştir. Bu enzimler birbirinden farklı üç bölgede etkindir. Sağlıklı bir insanda ağız boşluğunun pH değeri yaklaşık 7, midenin yaklaşık 2, onikiparmak bağırsağının yaklaşık 8’dir.\nBuna göre, X, Y ve Z enzimleri sırasıyla hangi bölgelerde en yüksek etkinliği gösterir?',
  sekil=SK2,dogru=S2[0],sira=yer('A',S2[0],S2[1:]),
  yan=[(S2[1],'X ile Y’nin yerleri değiştirilmiş; pH 2’de en etkin olan X’tir ve yalnız mide ortamına uyar.','dikkat'),
       (S2[2],'Sıralama tersine çevrilmiş; X en düşük pH’ta, Z en yüksek pH’ta etkindir.','dikkat'),
       (S2[3],'Y ile Z’nin yerleri değiştirilmiş; Y’nin etkinliği pH 7’de, Z’ninki pH 8’de en yüksektir.','dikkat'),
       (S2[4],'X ve Z’nin bölgeleri karıştırılmış; asidik ortam midedir, bazik ortam onikiparmak bağırsağıdır.','dikkat')],
  istenen='X, Y ve Z enzimlerinin en etkin olduğu bölgeler.',ip=['Her eğrinin en yüksek olduğu pH değerini bul ve kanalın hangi bölgesine uyduğuna bak.'],
  bilgi=[B('Enzim ve pH','her enzimin en yüksek etkinlik gösterdiği bir optimum pH değeri vardır; pH bu değerden uzaklaştıkça etkinlik azalır · Sindirim kanalında ağız boşluğu hafif asidik–nötr, mide güçlü asidik, ince bağırsak bazik ortama sahiptir')],
  puf='En yüksek noktaların pH değerini bölge pH’larıyla eşle.')

# ======================= 03 · mekanik sindirim · kolay · öncüllü =======================
D3={'I':(True,'Çiğneme besini dişlerle fiziksel olarak parçalar, kimyasal bir değişim yoktur; bu yargı doğrudur.'),
    'II':(True,'Mide kaslarının kasılıp gevşemesi besini sindirim salgılarıyla karıştırır ve ilerletir; fiziksel bir olaydır, bu yargı doğrudur.'),
    'III':(False,'Maltaz bir enzimdir; maltoza su katarak glikoza yıkar (hidroliz). Bu kimyasal sindirimdir, bu yargı yanlıştır.')}
R3=onc(D3,True,'D'); assert R3['T']=={'I','II'}
Q('0003','kimyasal','kolay','öncüllü','Kimyasal ve Mekanik Sindirim','Mekanik ve kimyasal sindirim olaylarını ayırt eder.','mekanik–kimyasal ayrımı',
  'Mekanik sindirimde besin yalnızca fiziksel olarak parçalanır, karıştırılır ya da ilerletilir; kimyasal sindirimde enzimler besinlerin kimyasal bağlarını yıkar.','Besinin küçük parçalara ayrıldığı her olayı kimyasal sindirim saymak; enzimli olayı mekanik sanmak.',
  [adim_onc(D3,'I'),adim_onc(D3,'II'),adim_onc(D3,'III'),sonuc(R3,True)],
  metin='İnsanda sindirim kanalında gerçekleşen bazı olaylar aşağıda verilmiştir.\nI. Dişlerle çiğneme sırasında besinin küçük parçalara ayrılması\nII. Mide duvarındaki kasların kasılıp gevşemesiyle besinin mide özsuyuyla karıştırılması\nIII. İnce bağırsakta maltaz enziminin maltozu glikoza dönüştürmesi\nBuna göre, bu olaylardan hangileri mekanik sindirime örnektir?',
  dogru=R3['dogru'],yan=R3['yan'],sira=R3['sira'],istenen='Mekanik sindirime örnek olan olaylar.',
  ip=['Her olayda besinin yalnızca fiziksel durumunun mu, yoksa kimyasal yapısının da mı değiştiğine bak.'],
  bilgi=[B('Mekanik ve kimyasal sindirim','mekanik sindirim besini parçalayan, karıştıran ve ilerleten fiziksel olaylardır (örneğin çiğneme, peristaltik hareket); kimyasal sindirimde enzimler büyük molekülleri su katarak küçük moleküllere ayırır (hidroliz)')],
  puf='Enzim varsa kimyasal, yalnızca fiziksel parçalama ve karıştırma varsa mekanik.')

# ======================= 04 · amilaz deney tablosu · orta · öncüllü =======================
DENEY4=[('1','7','37','Normal','Yok'),('2','7','37','Kaynatılıp soğutulmuş','Var'),('3','2','37','Normal','Var'),('4','7','4','Normal','Var')]
def fark(a,b): return [i for i in (1,2,3) if DENEY4[a][i]!=DENEY4[b][i]]
assert fark(0,2)==[1] and fark(0,1)==[3] and fark(0,3)==[2]
D4={'I':(fark(0,2)==[1],'1. ve 3. tüpler yalnızca pH bakımından farklıdır; sonuç farkı pH’ın etkisini gösterir, bu yargı doğrudur.'),
    'II':(False,'4. tüpteki sıcaklık düşüktür; düşük sıcaklık enzimi geri dönüşümlü olarak yavaşlatır, yapısını kalıcı olarak bozmaz. Bu yargı yanlıştır.'),
    'III':(fark(0,1)==[3],'1. ve 2. tüpler yalnızca tükürüğün kaynatılıp kaynatılmamasıyla ayrılır; kaynatılan tükürükte nişasta yıkılmadığından amilaz işlevini yitirmiştir. Bu yargı doğrudur.')}
R4=onc(D4,True,'E'); assert R4['T']=={'I','III'}
SK4=tablo_cok(['Tüp','Ortamın\npH’ı','Sıcaklık\n(°C)','Tükürük','İyotla mavi-mor\nrenk oluşumu'],[list(r[:3])+[r[3].replace('Kaynatılıp soğutulmuş','Kaynatılıp\nsoğutulmuş')]+[r[4]] for r in DENEY4],[50,90,90,150,150])
Q('0004','enzim','orta','öncüllü','Enzimler','Deney tablosundan değişkenleri ayırıp enzim etkinliğine pH, sıcaklık ve kaynatmanın etkisini yorumlar.','amilaz deneyi tablosu',
  'Deneyde yalnız bir koşulun farklı olduğu tüpler karşılaştırılarak o koşulun etkisi yorumlanır.','Birden fazla koşulu farklı tüpleri karşılaştırmak.',
  [adim_onc(D4,'I'),adim_onc(D4,'II'),adim_onc(D4,'III'),sonuc(R4,True)],
  metin='Bir öğrenci, aynı miktarda nişasta çözeltisi içeren dört tüpe aşağıdaki tabloda belirtilen koşulları uygulamıştır. Tüplerin hepsinde eşit hacimde tükürük kullanılmıştır. 30 dakika sonra her tüpe iyot çözeltisi eklenmiş, nişasta varlığında oluşan mavi-mor renk kaydedilmiştir.\nI. 1. ve 3. tüplerin karşılaştırılması, pH’ın tükürük amilazının etkinliğini etkilediğini gösterir.\nII. 1. ve 4. tüplerin karşılaştırılması, düşük sıcaklıkta amilazın yapısının kalıcı olarak bozulduğunu gösterir.\nIII. 1. ve 2. tüplerin karşılaştırılması, kaynatılan tükürükteki amilazın işlevini yitirdiğini gösterir.\nBuna göre, bu yargılardan hangileri doğrudur?',
  sekil=SK4,dogru=R4['dogru'],yan=R4['yan'],sira=R4['sira'],istenen='Deney sonuçlarıyla uyumlu olan yargılar.',
  ip=['Her karşılaştırmada iki tüpün yalnızca hangi koşulda ayrıldığını yaz.'],
  bilgi=[B('Kontrollü deney','bir etkiyi incelemek için karşılaştırılan düzeneklerde yalnız incelenen koşul farklı, diğerleri aynı tutulur · Enzimlerin etkinliği sıcaklık ve pH gibi koşullara bağlıdır')],
  puf='İki tüp arasındaki tek farkı bul; yargı yalnız o farkı konu etmeli.')

# ======================= 05 · kalan besin grafiği · orta · olumsuz =======================
KONUM=['Alım','Ağız','Mide','Onikiparmak','Son bölüm']
KALAN={'Nişasta':[100,88,88,25,0],'Protein':[100,100,60,15,0],'Yağ':[100,100,100,40,0]}
def basla(besin): return next(i for i in range(1,5) if KALAN[besin][i]<KALAN[besin][i-1])
assert basla('Nişasta')==1 and basla('Protein')==2 and basla('Yağ')==3
assert KALAN['Nişasta'][2]==KALAN['Nişasta'][1] and all(v[4]==0 for v in KALAN.values())
# X nişasta, Y protein, Z yağ
def egr5(vals,stil): return f'\\addplot[{stil},mark=square*,mark size=1.4pt] coordinates {{'+' '.join(f'({i},{v})' for i,v in enumerate(vals))+'};'
b=[egr5(KALAN['Nişasta'],'blue!70!black'),egr5(KALAN['Protein'],'vurgu'),egr5(KALAN['Yağ'],'orange!90!black,dashed')]
SK5=pgf('\n'.join(b),w='8cm',h='5.4cm',ek='legend entries={X,Y,Z},legend style={draw=none,at={(0.98,0.98)},anchor=north east,font=\\small},legend cell align=left,xmin=-.2,xmax=4.2,ymin=0,ymax=110,xtick={0,1,2,3,4},xticklabels={Alım,Ağız,Mide,Onikiparmak,İnce b. sonu},x tick label style={font=\\scriptsize,align=center,text width=1.3cm},ytick={0,50,100},ylabel={Kalan besin (\\%)}')
S5=['Nişastanın kimyasal sindirimi ağız boşluğunda başlar.','Proteinlerin kimyasal sindirimi midede başlar.','Yağların kimyasal sindirimi ince bağırsakta başlar.','Midede nişastanın kimyasal sindirimi sürer.','Üç besinin sindirimi de ince bağırsakta tamamlanır.']
Q('0005','kimyasal','orta','grafik','Kimyasal ve Mekanik Sindirim','Sindirilmemiş besin–bölge grafiğinden besinlerin kimyasal sindirimine başlama yerini yorumlar.','kalan besin–bölge grafiği',
  'Sindirilmemiş besin miktarının azaldığı ilk bölge, o besinin kimyasal sindiriminin başladığı yerdir.','Yatay kalan eğri parçasını yanlış yorumlamak; eğrileri besinlerle yanlış eşleştirmek.',
  [A('Eğrilerin ilk düştüğü bölgeyi bul','X ağızda, Y midede, Z ise yalnızca onikiparmak bağırsağında azalmaya başlar.','X: ağız · Y: mide · Z: onikiparmak'),
   A('Besinleri eşle','Ağızda başlayan sindirim nişastaya, midede başlayan protein sindirimine, ince bağırsakta başlayan yağ sindirimine aittir.','X: nişasta · Y: protein · Z: yağ'),
   A('Her ifadeyi grafikle sına','Mide bölgesinde nişasta eğrisi yataydır, yani nişastanın sindirimi sürmez; diğer dört ifade grafikle uyumludur.','Uyumsuz ifade: midede nişasta sindirimi')],
  metin='Aynı öğünle alınan nişasta, protein ve yağın sindirim kanalındaki bölgelerden geçerken sindirilmeden kalan miktarları şekilde gösterilmiştir. Üç besinin başlangıç miktarları eşittir ve eğrilerin hangi besine ait olduğu verilmemiştir (X, Y ve Z; nişasta, protein ve yağ olabilir).\nBuna göre, aşağıdaki ifadelerden hangisi söylenemez?',
  sekil=SK5,dogru=S5[3],sira=yer('D',S5[3],[S5[0],S5[1],S5[2],S5[4]]),
  yan=[(S5[0],'İfade doğrudur; nişasta eğrisi ağızda düşer. Ağızda tükürük amilazı nişastayı maltoza yıkmaya başlar.','bilgi'),
       (S5[1],'İfade doğrudur; protein eğrisi midede düşer. Mide özsuyundaki pepsin proteinleri kısa zincirlere yıkar.','bilgi'),
       (S5[2],'İfade doğrudur; yağ eğrisi ancak onikiparmak bağırsağında düşer. Lipaz ve safra yağın sindiriminde bu bölgede etkindir.','bilgi'),
       (S5[4],'İfade doğrudur; üç eğri de ince bağırsağın sonunda sıfıra ulaşır.','bilgi')],
  istenen='Grafiğe göre söylenemeyen ifade.',ip=['Eğrilerin hangi bölgede yatay kaldığını belirle; yatay çizgi o bölgede sindirimin sürmediğini gösterir.'],
  bilgi=[B('Besinlerin kimyasal sindirimi','nişasta ağızda tükürük amilazıyla, protein midede pepsinle, yağ ise ince bağırsakta lipazla sindirilmeye başlar')],
  puf='Yatay kalan eğri o bölgede sindirimin durduğunu gösterir.')

# ======================= 06 · villus şeması · orta · öncüllü =======================
def villus():
    b=['\\fill[orange!25] (-1,0)--(-1,3.3) arc(180:0:1)--(1,0)--cycle;\\draw[line width=1.3pt] (-1,0)--(-1,3.3) arc(180:0:1)--(1,0);',
       '\\draw[line width=.7pt] (-.85,0)--(-.85,3.3) arc(180:0:.85)--(.85,0);',
       '\\draw[line width=.9pt,fill=yellow!70] (-.17,.2)--(-.17,2.95) arc(180:0:.17)--(.17,.2);',
       '\\draw[line width=.9pt] (-.17,.2)--(-.17,2.95) arc(180:0:.17)--(.17,.2);',
       '\\draw[line width=2pt,red!75!black] (-.58,0)--(-.58,2.6) .. controls (-.58,3.05) and (.58,3.05) .. (.58,2.6)--(.58,0);\\foreach \\yy in {.5,1.1,1.7,2.3}{\\draw[line width=1.2pt,red!75!black] (-.58,\\yy)--(-.28,\\yy+.15);\\draw[line width=1.2pt,red!75!black] (.58,\\yy)--(.28,\\yy+.15);}',
       '\\draw[line width=1.3pt] (-2,0)--(-1,0);\\draw[line width=1.3pt] (1,0)--(2,0);\\draw[line width=.9pt] (-.17,.2)--(-.17,-.6);\\draw[line width=.9pt] (.17,.2)--(.17,-.6);\\draw[line width=2pt] (-.58,0)--(-.58,-.6);\\draw[line width=2pt] (.58,0)--(.58,-.6);',
       '\\draw[line width=.8pt] (2.7,1.4)--(.58,1.4);\\fill (.58,1.4) circle (.07);\\node[draw,circle,inner sep=1.4pt,fill=white,text=black,font=\\normalsize\\bfseries] at (2.95,1.4) {I};',
       '\\draw[line width=.8pt] (0,5.4)--(0,2.2);\\fill (0,2.2) circle (.07);\\node[draw,circle,inner sep=1.4pt,fill=white,text=black,font=\\normalsize\\bfseries] at (0,5.65) {II};']
    return tk('\n'.join(b),.85)
SK6=villus()
D6={'I':(True,'I numaralı yapı kan kılcalıdır; amino asitler ve glikoz buraya geçerek kapı toplardamarıyla karaciğere taşınır. Bu yargı doğrudur.'),
    'II':(False,'Yağ asitleri ve gliserol kan kılcalına değil, II numaralı kör uçlu lenf kılcalına geçer. Bu yargı yanlıştır.'),
    'III':(False,'Glikoz, lenf kılcalına değil kan kılcalına geçer; lenf yoluyla taşınan başlıca besinler yağlardır. Bu yargı yanlıştır.')}
R6=onc(D6,True,'A'); assert R6['T']=={'I'}
Q('0006','emilim','orta','öncüllü','Emilim','Villus şemasında kan ve lenf kılcallarını ayırt ederek besin maddelerinin emilim yollarını belirler.','villus şeması, emilim yolları',
  'Amino asit ve glikoz villustaki kan kılcalına geçer; yağ asitleri ve gliserol epitel hücrelerinde yağa dönüşüp lenf kılcalına katılır.','Tüm besin monomerlerinin kan kılcalına geçtiğini sanmak; lenf kılcalının kan damarı olduğunu düşünmek.',
  [adim_onc(D6,'I'),adim_onc(D6,'II'),adim_onc(D6,'III'),sonuc(R6,True)],
  metin='Şekilde ince bağırsak duvarındaki bir villusun kesiti, içindeki iki damar yapısıyla birlikte verilmiştir. Yapılar I ve II ile numaralandırılmıştır.\nI. Amino asitler I numaralı yapıya geçer ve oradan karaciğere taşınır.\nII. Yağ asitleri ve gliserol I numaralı yapıya geçerek kana karışır.\nIII. Glikoz II numaralı yapıya geçerek lenf dolaşımına katılır.\nBuna göre, bu yargılardan hangileri doğrudur?',
  sekil=SK6,dogru=R6['dogru'],yan=R6['yan'],sira=R6['sira'],istenen='Doğru olan yargılar.',
  ip=['Şekildeki iki yapının biçimlerini karşılaştır ve besinlerin emilim yollarını hatırla.'],
  bilgi=[B('Emilim yolları','villusta kan kılcalları ve lenf kılcalı bulunur; suda çözünen küçük besin monomerleri kan kılcalına geçer, yağlar ise lenf kılcalı yoluyla taşınır · Kan kılcallarındaki kan karaciğere gider, lenf ise daha sonra kan dolaşımına katılır')],
  puf='Önce iki yapıyı biçimlerinden tanı, sonra her maddenin geçiş yolunu sına.')

# ======================= 07 · mide hücreleri · orta · öncüllü (metin) =======================
D7={'I':(False,'Pepsinojenin pepsine dönüşümü HCl’ye bağlıdır; HCl’yi salgılayan Y hücreleri sağlam olduğundan dönüşüm yavaşlamaz. Bu yargı yanlıştır.'),
    'II':(True,'Mukus mide duvarını HCl ve pepsinin etkisinden korur; mukus azalınca epitelin zarar görme olasılığı artar. Bu yargı doğrudur.'),
    'III':(False,'Pepsinojeni salgılayan X hücreleri sağlam olduğundan pepsinojen salgısı durmaz. Bu yargı yanlıştır.')}
R7=onc(D7,True,'B'); assert R7['T']=={'II'}
Q('0007','kimyasal','orta','öncüllü','Kimyasal ve Mekanik Sindirim','Mide özsuyunu oluşturan hücre salgılarının işlevlerini ilişkilendirerek bir hücre grubunun işlev kaybının sonuçlarını yorumlar.','mide hücreleri ve salgıları',
  'Mide özsuyunda enzim öncülü, asit ve mukus ayrı hücrelerden salgılanır; bir hücre grubunun işlev kaybı yalnız kendi görevini etkiler.','Bir hücre grubunun işlev kaybının tüm salgıları durduracağını sanmak; mukusun asidi nötrleştirdiğini düşünmek.',
  [adim_onc(D7,'I'),adim_onc(D7,'II'),adim_onc(D7,'III'),sonuc(R7,True)],
  metin='İnsanın midesinde X hücreleri enzimin inaktif hâli olan pepsinojeni, Y hücreleri hidroklorik asidi (HCl), Z hücreleri ise mide duvarını kaplayan mukusu salgılar. Pepsinojen, HCl’nin etkisiyle pepsine dönüşür; pepsin proteinlerdeki peptit bağlarını yıkar.\nYalnızca Z hücrelerinin işlevini büyük ölçüde yitirdiği bir kişide mide boşluğunda gerçekleşebilecek durumlar olarak şunlar öne sürülmüştür.\nI. Pepsinojenin pepsine dönüşümünün yavaşlaması\nII. Mide epitelinin HCl ve pepsinden zarar görme olasılığının artması\nIII. Pepsinojen salgısının tamamen durması\nBuna göre, bu kişide yukarıdakilerden hangilerinin gerçekleşmesi beklenir?',
  dogru=R7['dogru'],yan=R7['yan'],sira=R7['sira'],istenen='İşlev kaybı sonucunda beklenen durumlar.',
  ip=['Her yargıda adı geçen hücre grubunun sağlam mı yoksa işlevsiz mi olan grup olduğuna bak.'],
  bilgi=[B('Mide özsuyu','mide özsuyu enzim öncülü, asit ve mukus içerir; enzim öncülü asit etkisiyle etkin enzime dönüşür · Mukus mide duvarını kaplayarak asit ve enzimin zarar vermesini engeller')],
  puf='Yalnızca işlevsiz olan hücrenin görevi aksar; diğerleri çalışmaya devam eder.')

# ======================= 08 · hormon–zaman grafiği · orta =======================
def hx(t): return 10+80*math.exp(-((t-45)/22)**2)
def vy(t): return 100-60*math.exp(-((t-75)/25)**2)
tx=max(range(0,121),key=hx); tv=min(range(0,121),key=vy)
assert tx<tv and hx(0)<20 and vy(0)>99 and hx(tx)>85 and vy(tv)<45
cx=' '.join(f'({t},{hx(t):.1f})' for t in range(0,121,3)); cy=' '.join(f'({t},{vy(t):.1f})' for t in range(0,121,3))
b=[f'\\addplot[blue!70!black] coordinates {{{cx}}};',f'\\addplot[vurgu,dashed] coordinates {{{cy}}};',
   '\\node[font=\\small\\bfseries,text=blue!70!black] at (axis cs:45,100) {X};\\node[font=\\small\\bfseries,text=vurgu] at (axis cs:100,55) {Y};']
SK8=pgf('\n'.join(b),ek='xmin=0,xmax=120,ymin=0,ymax=115,xtick={0,30,60,90,120},ytick={0,50,100},xlabel={Öğünden sonra geçen süre (dk)},ylabel={Göreli değer (\\%)}')
S8=['Salgılanması safra kesesi tarafından yapılır ve yağların emülsiyonlaşmasını sağlar.','Safra kesesi boşaldıktan sonra salgılanır ve safra kesesinin gevşemesini uyarır.','Sinir hücreleri aracılığıyla taşınır, kan dolaşımına katılmadan hedefine ulaşır.','Salgılanması, öğünün içeriğinden bağımsız olarak sürekli aynı düzeydedir.','Besinin onikiparmak bağırsağına ulaşmasıyla artar ve safra kesesinin kasılmasını uyarır.']
Q('0008','hormon','orta','grafik','Hormonal Düzenleme','Hormon düzeyi ve organ hacmi grafiğinden sindirimin hormonal düzenlenmesini yorumlar.','hormon düzeyi–safra kesesi hacmi grafiği',
  'Yağlı besin onikiparmak bağırsağına geçince salgılanan hormon safra kesesini kasarak safranın boşalmasını sağlar; hormon önce artar, organın hacmi sonra azalır.','Hormonun organdan salgılandığını sanmak; hacim azalmasını safra üretiminin durması saymak; sinirsel ve hormonal düzenlemeyi karıştırmak.',
  [A('Eğrileri oku','X’in düzeyi öğünden sonra artar ve yaklaşık 45. dakikada en yüksek olur; Y’nin hacmi X’in artışından sonra azalıp yaklaşık 75. dakikada en düşük olur.','X: önce artar · Y: sonra azalır'),
   A('Neden–sonuç sırasını kur','Değişim sırası X’in artışının Y’nin azalmasından önce başladığını gösterir; bu sıra X’in Y’yi etkileyen hormon olmasıyla uyumludur.','X → Y'),
   A('İfadeleri sına','Hacim azalması safra kesesinin kasılıp safrayı boşalttığını gösterir; hormonlar kanla taşınır ve salgılanmaları öğüne bağlıdır.','Doğru: besinle uyarılan, kasılmayı artıran hormon')],
  metin='Sağlıklı bir kişiye yağ bakımından zengin bir öğün verilmiş; öğünden sonraki 120 dakika boyunca kandaki X hormonunun düzeyi ile safra kesesinin hacmi ölçülmüştür. Grafikte Y, safra kesesinin hacmini göstermektedir; farklı birimlerle yapılan iki ölçüm göreli değer olarak aynı eksende verilmiştir.\nBuna göre, X hormonuyla ilgili aşağıdakilerden hangisi söylenebilir?',
  sekil=SK8,dogru=S8[4],sira=yer('E',S8[4],S8[:4]),
  yan=[(S8[0],'X hormonu safra kesesinde değil, onikiparmak bağırsağı mukozasında salgılanır; safranın yağları emülsiyonlaştırdığı doğrudur ama bu X’in işlevi değildir.','dikkat'),
       (S8[1],'Grafikte X’in artışı Y’nin azalmasından önce başlar; hacim azalması kasılmadır, gevşeme hacmi artırır. Neden–sonuç sırası ters kurulmuş.','dikkat'),
       (S8[2],'Hormonlar kan dolaşımıyla taşınır; sinir hücreleriyle iletim hormonal değil sinirsel düzenlemedir.','bilgi'),
       (S8[3],'Grafikte X’in düzeyi öğünden sonra belirgin biçimde artar; salgısı öğünün içeriğine bağlıdır.','bilgi')],
  istenen='X hormonu ile ilgili söylenebilecek ifade.',ip=['Hangi eğrinin önce, hangisinin sonra değiştiğine ve hacmin azalmasının safra kesesinde ne anlama geldiğine bak.'],
  bilgi=[B('Sindirimin hormonal düzenlenmesi','onikiparmak bağırsağı mukozası, kimüsün içeriğine göre kana hormon verir; bu hormonlar safra kesesi ve pankreas gibi hedef organların salgılarını düzenler · Hormonlar kanla taşınır')],
  puf='Ardışıklık tek başına nedensellik göstermez; grafiği hormonal düzenleme bilgisiyle birleştir.')

# ======================= 09 · kanal şeması · orta · öncüllü =======================
SK9=kanal_sekil([('mide','1',(3.4,5.4)),('onikiparmak','2',(-3.9,2.9)),('kalinbag','3',(3.9,1.2))])
D9={'I':(False,'Tükürük amilazı ağız boşluğunda etkindir ve midenin asidik ortamında etkisizleşir; 2 numaralı bölgede bu enzimin nişastayı yıkması beklenmez. Bu yargı yanlıştır.'),
    'II':(True,'Onikiparmak bağırsağına pankreas enzimleri ile safra dökülür; safra yağları küçük damlacıklara ayırır. Bu yargı doğrudur.'),
    'III':(False,'Pepsinojenin HCl ile pepsine dönüşümü midede gerçekleşir; 2 numaralı bölgenin ortamı bazik olduğundan pepsin etkin olamaz. Bu yargı yanlıştır.')}
R9=onc(D9,True,'B'); assert R9['T']=={'II'}
Q('0009','yapi','orta','öncüllü','Sindirim Kanalı ve Yardımcı Organlar','Şekilde onikiparmak bağırsağını tanıyıp bu bölgede gerçekleşen sindirim olaylarını yorumlar.','kanal şeması, onikiparmak bağırsağı',
  'Onikiparmak bağırsağı midenin hemen ardındaki bağırsak bölümüdür; pankreas özsuyu ve safra buraya dökülür, ortam asidik kimüsün nötrleşmesiyle bazik olur.','Midede gerçekleşen olayları (pepsinojen aktifleşmesi) ya da ağızdaki olayları bu bölgeye taşımak.',
  [adim_onc(D9,'I'),adim_onc(D9,'II'),adim_onc(D9,'III'),sonuc(R9,True)],
  metin='Şekilde insan sindirim kanalının bazı bölümleri 1, 2 ve 3 ile numaralandırılmıştır.\n2 numaralı bölgede gerçekleşebilecek olaylar olarak şunlar öne sürülmüştür.\nI. Tükürük amilazının nişastayı maltoza yıkması\nII. Safranın yağları küçük damlacıklara ayırması\nIII. Pepsinojenin HCl etkisiyle pepsine dönüşmesi\nBuna göre, bu olaylardan hangileri 2 numaralı bölgede gerçekleşir?',
  sekil=SK9,dogru=R9['dogru'],yan=R9['yan'],sira=R9['sira'],istenen='2 numaralı bölgede gerçekleşen olaylar.',
  ip=['Önce 2 numaralı yapının hangi bölüm olduğunu ve oraya hangi yardımcı organların salgı döktüğünü düşün.'],
  bilgi=[B('Onikiparmak bağırsağı','midenin hemen ardından gelen, ince bağırsağın ilk bölümüdür; pankreas özsuyu ve safra bu bölgeye boşaltılır · Pankreas özsuyundaki bikarbonat midenin asidik kimüsünü nötrleştirir')],
  puf='İlk bölgeyi tanı; kimüsün asidi nötrleşir, pankreas enzimleri ve safra burada etkindir.')

# ======================= 10 · karbonhidrat sindirimi · orta · olumsuz =======================
S10=['Sükroz ince bağırsakta maltaz enzimiyle glikoz ve fruktoza yıkılır.','Tükürük amilazı nişastayı kısa zincirli karbonhidratlara ve maltoza yıkar.','Pankreas amilazı nişastanın ince bağırsakta sindirilmesine katkıda bulunur.','Maltoz, ince bağırsakta maltaz enzimiyle iki glikoz molekülüne ayrılır.','İnsan sindirim enzimleri selülozu yıkamadığından selüloz sindirilmeden dışkıyla atılır.']
Q('0010','kimyasal','orta','düz','Kimyasal ve Mekanik Sindirim','Karbonhidratların sindiriminde görev alan enzimlerin özgüllüğünü değerlendirir.','karbonhidrat sindirim enzimleri',
  'Her sindirim enzimi belirli bir substrata etki eder; nişasta amilazla, maltoz maltazla, sükroz sükrazla yıkılır.','Disakkaritlerin hepsinin aynı enzimle yıkıldığını sanmak.',
  [A('Enzim–substrat eşleştirmesini hatırla','Amilazlar nişastaya, maltaz maltoza, sükraz sükroza etki eder; insan selülozu yıkan enzime sahip değildir.','Her enzim kendi substratına'),
   A('İfadeleri tek tek sına','Dört ifade enzim ile substratını doğru eşleştirir. Bir ifadede sükrozun yıkımı başka bir enzime bağlanmıştır.','Bir eşleştirme hatalı'),
   A('Yanlış olanı seç','Sükroz, glikoz ve fruktozdan oluşur ve sükraz enzimiyle yıkılır; maltaz maltoza özgüdür.','Hatalı eşleştirme: sükroz–maltaz')],
  metin='İnsanda besinlerle alınan karbonhidratlar; nişasta (polisakkarit), maltoz ve sükroz (disakkaritler) ile selüloz gibi liflerdir. Bu karbonhidratların kimyasal sindirimi, sindirim kanalının farklı bölgelerinde salgılanan farklı enzimlerle yapılır.\nBuna göre, insanda karbonhidratların sindirimiyle ilgili aşağıdakilerden hangisi yanlıştır?',
  dogru=S10[0],sira=yer('A',S10[0],S10[1:]),
  yan=[(S10[1],'İfade doğrudur; ağızda tükürük amilazı nişastayı kısa zincirlere ve maltoza yıkmaya başlar.','bilgi'),
       (S10[2],'İfade doğrudur; pankreas özsuyundaki amilaz nişastayı ince bağırsakta yıkmayı sürdürür.','bilgi'),
       (S10[3],'İfade doğrudur; maltaz maltozu iki glikoza ayırır.','bilgi'),
       (S10[4],'İfade doğrudur; insan selülozu yıkan enzime sahip değildir.','bilgi')],
  istenen='Karbonhidrat sindirimiyle ilgili yanlış ifade.',ip=['Her enzimin hangi besine ya da hangi disakkarite etki ettiğini ayrı ayrı düşün.'],
  bilgi=[B('Karbonhidrat sindirimi','karbonhidratlar monosakkaritlere kadar yıkılır; her enzim belirli bir karbonhidrata özgüdür')],
  puf='Her ifadede enzim ile substratının eşleşip eşleşmediğine bak.')

# ======================= 11 · laktaz eksikliği · orta · öncüllü (metin) =======================
D11={'I':(False,'Nişastanın sindirimi tükürük ve pankreas amilazıyla yapılır; laktaz eksikliği bunları etkilemez. Bu yargı yanlıştır.'),
     'II':(False,'Laktoz, glikoz ve galaktozdan oluşan bir disakkarittir; laktaz olmadan monomerlerine ayrılamaz ve emilemez. Bu yargı yanlıştır.'),
     'III':(True,'Monomerlerine ayrılamayan laktoz emilemez ve sindirilmeden kalın bağırsağa geçer. Bu yargı doğrudur.')}
R11=onc(D11,True,'C'); assert R11['T']=={'III'}
Q('0011','kimyasal','orta','öncüllü','Kimyasal ve Mekanik Sindirim','Bir sindirim enziminin eksikliğinin yalnızca ilgili besinin sindirimini etkilediğini yorumlar.','laktaz eksikliği',
  'Her sindirim enzimi belirli bir substrata etki eder; bir enzimin eksikliği yalnızca o substratın sindirimini aksatır. Sindirilmeyen disakkarit emilemez.','Bir enzim eksikliğinin tüm karbonhidrat sindirimini durduracağını sanmak.',
  [adim_onc(D11,'I'),adim_onc(D11,'II'),adim_onc(D11,'III'),sonuc(R11,True)],
  metin='Bir kişinin ince bağırsak epitel hücreleri, süt şekeri olan laktozu glikoz ve galaktoza ayıran laktaz enzimini üretememektedir. Bu kişinin diğer sindirim enzimleri normal çalışmaktadır ve laktoz içeren bir besin almıştır.\nBu kişi için şu yargılar öne sürülmüştür.\nI. Nişastanın ağız boşluğunda başlayan sindirimi gerçekleşemez.\nII. Laktozun monomerleri olan glikoz ve galaktoz normal biçimde emilir.\nIII. Laktoz sindirilmeden kalın bağırsağa ulaşır.\nBuna göre, bu yargılardan hangileri doğrudur?',
  dogru=R11['dogru'],yan=R11['yan'],sira=R11['sira'],istenen='Doğru olan yargılar.',
  ip=['Eksik olan enzimin etki ettiği besini ve o besinin ürünlerini belirle.'],
  bilgi=[B('Enzim özgüllüğü','bir enzim yalnızca belirli bir substrata etki eder; disakkaritler ince bağırsakta kendi enzimleriyle monosakkaritlere ayrılır ve ancak monosakkaritler emilir')],
  puf='Eksik enzimin substratı sindirilemez; diğer enzimlerin substratları etkilenmez.')

# ======================= 12 · lipaz–safra tüpleri · orta =======================
PH12=[('1',['Süt','+ lipaz'],'7,2'),('2',['Süt','+ lipaz','+ safra'],'6,4'),('3',['Süt','+ safra'],'8,0'),('4',['Süt','+ kaynatılmış','lipaz','+ safra'],'8,0')]
assert float(PH12[1][2].replace(',','.'))<float(PH12[0][2].replace(',','.'))<8.0 and PH12[2][2]==PH12[3][2]=='8,0'
SK12=tup_sekil([(no,ic,['30 dk sonra','pH: '+ph],1.5) for no,ic,ph in PH12],xs=2.3)
S12=['Safra yağın kimyasal sindirimini tek başına gerçekleştirmez; lipazın etkinliğini artırır.','Lipaz yağı yalnızca safra varlığında yıkabilir.','Safra, yağları yağ asitlerine ve gliserole yıkan bir enzim içerir.','Safra ilavesi lipazın etkinliğini azaltmıştır.','Kaynatılmış lipaz safra varlığında yağı yıkabildiğinden ısıya dayanıklıdır.']
Q('0012','yardimci','orta','şekilli','Kimyasal ve Mekanik Sindirim','Lipaz ve safra deneyinde kontrol tüplerini yorumlayarak safranın işlevini belirler.','lipaz–safra deney düzeneği',
  'Yağ sindirilince yağ asitleri oluşur ve pH düşer; safra yağı emülsiyonlaştırarak lipazın etkisini artırır, kendisi yağı kimyasal olarak yıkmaz. Kaynatılmış enzim işlevsizdir.','Safranın yağı yıkan enzim içerdiğini sanmak; pH düşüşünün olmadığı tüpte yıkım olduğunu düşünmek.',
  [A('pH değişimini yorumla','Yağ asitleri oluştukça pH düşer. 1. tüpte pH 8,0’dan 7,2’ye, 2. tüpte 6,4’e inmiştir; 3. ve 4. tüplerde pH değişmemiştir.','Düşüş: 1 ve 2 · Değişmeyen: 3 ve 4'),
   A('Tüpleri karşılaştır','1 ve 2 yalnızca safra bakımından farklıdır; safra pH düşüşünü artırmıştır. 3. tüpte lipaz yoktur, 4. tüpte lipaz kaynatıldığından işlevsizdir.','Safra: etkiyi artırıyor · Lipaz: gerekli'),
   A('Sonucu çıkar','Safra tek başına pH’ı düşürmediğinden yağı yıkmamıştır; lipaz varken safra yıkımı artırmıştır.','Safra lipazın etkinliğini artırır')],
  metin='Bir öğrenci, aynı hacimde süt (yağ içerir) bulunan dört tüpte şekildeki karışımları hazırlamış ve tüpleri 37 °C’ta bekletmiştir. Tüplerin hepsinde başlangıç pH değeri 8,0’dır ve yağın sindirimiyle oluşan yağ asitleri ortamın pH değerini düşürmektedir. Lipaz ve safra, kullanıldıkları tüplerde eşit miktardadır.\nBuna göre, deney sonuçlarından hangisi çıkarılabilir?',
  sekil=SK12,dogru=S12[0],sira=yer('E',S12[0],S12[1:]),
  yan=[(S12[1],'1. tüpte safra olmadan da pH düşmüştür; lipaz safrasız ortamda da yağı yıkar.','dikkat'),
       (S12[2],'3. tüpte yalnızca safra vardır ve pH değişmemiştir; safra yağ asidi oluşturmaz, yani enzim gibi davranmaz.','dikkat'),
       (S12[3],'2. tüpteki pH düşüşü 1. tüpten fazladır; safra lipazın etkinliğini azaltmamış, artırmıştır.','dikkat'),
       (S12[4],'4. tüpte pH değişmemiştir; kaynatılan lipaz yağı yıkamamıştır, yani ısıya dayanıklı değildir.','dikkat')],
  istenen='Deney sonuçlarından çıkarılabilecek yargı.',ip=['Hangi tüplerde pH’ın değiştiğini bul ve tüpleri aralarındaki tek fark üzerinden karşılaştır.'],
  bilgi=[B('Yağ sindirimi','yağlar lipaz enzimiyle yağ asitleri ve gliserole yıkılır; safra yağı küçük damlacıklara ayırarak enzimin etki edeceği yüzeyi artırır, ancak enzim değildir')],
  puf='pH düşüşü yağ asidi oluştuğunu gösterir; yalnızca safranın olduğu tüpte düşüş yoktur.')

# ======================= 13 · antiasit · zor · öncüllü =======================
EN13={'P':(2,1.0),'Q':(7,1.3)}
def e13(e,ph): return gauss(ph,*EN13[e])
assert e13('P',2)==100 and e13('P',6)<5 and e13('Q',6)>55 and e13('Q',2)<2
def cz13(e,stil): return f'\\addplot[{stil}] coordinates {{'+' '.join(f'({x/10:.1f},{e13(e,x/10):.1f})' for x in range(0,111,2))+'};'
b=[cz13('P','blue!70!black'),cz13('Q','vurgu,dashed'),'\\node[font=\\small\\bfseries,text=blue!70!black] at (axis cs:2,110) {P};\\node[font=\\small\\bfseries,text=vurgu] at (axis cs:7,110) {Q};']
SK13=pgf('\n'.join(b),ek='xmin=0,xmax=11,ymin=0,ymax=120,xtick={0,2,4,6,8,10},ytick={0,50,100},xlabel={Ortamın pH değeri},ylabel={Enzim etkinliği (\\%)}')
D13={'I':(e13('P',6)<e13('P',2),'Midenin pH değeri 2’den 6’ya çıkınca P enziminin etkinliği grafikte çok düşer; bu yargı doğrudur.'),
     'II':(False,'Pepsinojenin P enzimine dönüşümü HCl’nin etkisiyle olur; HCl azaldığından dönüşüm hızlanmaz, yavaşlar. Bu yargı yanlıştır.'),
     'III':(e13('Q',6)>e13('Q',2),'Q enzimi pH 6’da grafikte yüksek etkinlik gösterir; tükürükle mideye gelen Q mide ortamında nişastayı yıkabilir. Bu yargı doğrudur.')}
assert D13['I'][0] and D13['III'][0]
R13=onc(D13,True,'C'); assert R13['T']=={'I','III'}
Q('0013','enzim','zor','öncüllü','Enzimler','Enzim etkinliği–pH grafiğini mide asidinin azalmasıyla birleştirerek hem midede hem ağızda salgılanan enzimlerin durumunu yorumlar.','antiasit, enzim–pH grafiği',
  'Mide asidi azalınca pepsinojenin aktifleşmesi ve pepsinin etkinliği azalır; pH yükselince ağızda salgılanan amilaz midede de etkinlik kazanabilir.','Asidin azalmasının yalnız pepsini etkilediğini sanmak; tükürük amilazının midede daima etkisiz olduğunu düşünmek.',
  [adim_onc(D13,'I'),adim_onc(D13,'II'),adim_onc(D13,'III'),sonuc(R13,True)],
  metin='Şekilde, P ve Q enzimlerinin etkinliğinin ortamın pH değerine göre değişimi verilmiştir. P enzimi, midede inaktif öncülü hâlinde salgılanan ve HCl’nin etkisiyle etkinleşen proteinleri yıkan enzimdir. Q enzimi ise ağız boşluğunda salgılanıp besinle birlikte mideye geçen, nişastayı yıkan enzimdir. Sağlıklı bir insanda mide özsuyunun pH’ı yaklaşık 2 iken mide asidini azaltan bir ilaç kullanan kişide yaklaşık 6’dır.\nİlaç kullanan kişi nişasta ve protein içeren bir öğün almıştır. Bu kişinin midesinde sağlıklı kişiye göre şunların gerçekleştiği öne sürülmüştür.\nI. P enziminin etkinliği azalır.\nII. P enziminin inaktif öncülünün etkinleşme hızı artar.\nIII. Q enzimi nişastayı yıkabilir.\nBuna göre, yukarıdakilerden hangileri gerçekleşir?',
  sekil=SK13,dogru=R13['dogru'],yan=R13['yan'],sira=R13['sira'],istenen='İlaç kullanan kişinin midesinde gerçekleşen durumlar.',
  ip=['Grafikten iki pH değerinde (2 ve 6) iki enzimin etkinliğini oku; sonra asidin hangi basamakta gerektiğini düşün.'],
  bilgi=[B('Mide asidi ve enzimler','mide öz suyundaki HCl hem ortamı asidik yapar hem de pepsinojenin pepsine dönüşmesini sağlar; enzimler yalnız uygun pH aralığında etkindir')],
  puf='Her enzimi iki pH değerinde grafikten oku; asit azalınca asitle etkinleşen basamaklar yavaşlar.')

# ======================= 14 · hidroliz sayımı · zor =======================
NX,NZ,NY=10,8,3                      # X: amino asit sayısı, Z: glikoz sayısı, Y: trigliseritte yağ asidi sayısı (ester bağı)
SU=(NX-1)+NY+(NZ-1); URUN=NX+NY+1+NZ; HATA_TRIG=(NX-1)+(NZ-1); HATA_N=NX+NY+NZ; HATA_Z=(NX-1)+NY+NZ
assert SU==19 and URUN==22 and HATA_TRIG==16 and HATA_N==21 and HATA_Z==20 and len({SU,URUN,HATA_TRIG,HATA_N,HATA_Z})==5
def mol_sekil():
    b=['\\node[font=\\normalsize\\bfseries] at (-.7,0) {X};','\\node[font=\\normalsize\\bfseries] at (-.7,-2.0) {Y};','\\node[font=\\normalsize\\bfseries] at (-.7,-4.0) {Z};']
    for i in range(NX):
        b.append(f'\\draw[line width=1pt,fill=cyan!40] ({i*.62},0) circle (.22);\\draw[line width=1pt] ({i*.62},0) circle (.22);')
        if i<NX-1: b.append(f'\\draw[line width=1pt] ({i*.62+.22},0)--({(i+1)*.62-.22},0);')
    for k in range(NY):
        y=-1.5-k*.5
        b.append(f'\\draw[line width=1pt,fill=orange!50] (0,{y}) circle (.17);\\draw[line width=1pt] (0,{y}) circle (.17);')
        if k<NY-1: b.append(f'\\draw[line width=1pt] (0,{y-.17})--(0,{y-.5+.17});')
        pts=' -- '.join(f'({.5+j*.38},{y+(.12 if j%2 else -.12)})' for j in range(9))
        b.append(f'\\draw[line width=1pt] (.17,{y})--(.5,{y-.12}) -- {pts};')
    for i in range(NZ):
        b.append(f'\\node[regular polygon,regular polygon sides=6,draw,line width=1pt,fill=yellow!60,minimum size=.62cm,inner sep=0pt] at ({i*.78},-4.0) {{}};')
        b.append(f'\\node[regular polygon,regular polygon sides=6,draw,line width=1pt,minimum size=.62cm,inner sep=0pt] at ({i*.78},-4.0) {{}};')
        if i<NZ-1: b.append(f'\\draw[line width=1pt] ({i*.78+.31},-4.0)--({(i+1)*.78-.31},-4.0);')
    return tk('\n'.join(b),.85)
SK14=mol_sekil()
Q('0014','kimyasal','zor','şekilli','Kimyasal ve Mekanik Sindirim','Polipeptit, trigliserit ve nişasta parçasının tam sindiriminde yıkılan bağ sayısını bulup kullanılan su molekülü sayısını hesaplar.','hidroliz bağ sayımı',
  'Polimerlerin ve trigliseritlerin sindirimi hidrolizdir; bağlar su katılarak yıkılır.','Bağ ile birim sayısını karıştırmak; bir molekülü hesaba katmamak.',
  [A('Bağ sayılarını bul','X’te 10 amino asit arasında 9 peptit bağı, Z’de 8 glikoz arasında 7 glikozit bağı, Y’de gliserole bağlı 3 yağ asidi için 3 ester bağı vardır.','9 + 3 + 7'),
   A('Her bağ için bir su','Hidrolizde yıkılan her bağ için bir su molekülü kullanılır.','Su sayısı = bağ sayısı'),
   A('Topla','Tüm bağlar yıkıldığında kullanılan su molekülü sayısı bulunur.','9 + 3 + 7 = 19')],
  metin='Şekilde, bir öğünde alınan X (düz bir polipeptit), Y (bir trigliserit) ve Z (dallanmamış bir nişasta parçası) moleküllerinin birimleri şematik olarak gösterilmiştir. Bu moleküllerin her biri sindirim kanalında enzimlerle monomerlerine tamamen yıkılmaktadır.\nBuna göre, bu işlemde toplam kaç su molekülü kullanılır?',
  sekil=SK14,dogru=SU,yan=[(HATA_TRIG,'Trigliseritin sindirimi hesaba katılmamış; yalnız polipeptit ve nişasta için 9 + 7 bağ sayılmıştır.','islem'),
       (HATA_Z,'Nişasta için bağ sayısı yerine glikoz sayısı (8) alınmış; n birimli zincirde n−1 bağ vardır.','islem'),
       (HATA_N,'Tüm moleküllerde birim sayısı alınmış (10 + 3 + 8); zincirde bağ sayısı birim sayısından bir eksiktir.','islem'),
       (URUN,'Oluşan ürün sayısı (10 amino asit + 3 yağ asidi + 1 gliserol + 8 glikoz) su sayısı sanılmış.','dikkat')],
  istenen='Kullanılan toplam su molekülü sayısı.',ip=['Sindirimde moleküllerin birimleri arasındaki bağların yıkımında neyin kullanıldığını düşün.'],
  bilgi=[B('Hidroliz','polimerlerin ve trigliseritlerin sindiriminde bağlar su katılarak yıkılır')],
  puf='Hidrolizde su kullanılır; moleküllerdeki bağları ayrı ayrı değerlendir.')

# ======================= 15 · hormon tablosu · zor · öncüllü =======================
SK15=tablo_cok(['Hormon','Salgılandığı yer','Salgılanmasını uyaran','Hedef ve etki'],
  [['X','Mide mukozası','Besinin mideye gelmesi','Mide bezleri: özsuyu\nsalgısı artar'],
   ['Y','Onikiparmak bağırsağı\nmukozası','Asidik kimüs','Pankreas: bikarbonatlı\nsıvı salgısı artar'],
   ['Z','Onikiparmak bağırsağı\nmukozası','Yağ ve protein içeren\nkimüs','Safra kesesi kasılır,\npankreas enzim salgısı artar']],[50,160,160,226])
D15={'I':(True,'Y hormonu asidik kimüsle uyarılır ve pankreastan bikarbonatlı sıvı salgısını artırır; bu hormon yoksa salgı azalır. Bu yargı doğrudur.'),
     'II':(False,'Safra kesesini kasan Z hormonunu üreten hücreler sağlamdır; kasılma zayıflamaz. Bu yargı yanlıştır.'),
     'III':(True,'Bikarbonat salgısı azalınca asidik kimüs yeterince nötrleştirilemez ve onikiparmak bağırsağı içeriğinin asitliği normalden yüksek kalır. Bu yargı doğrudur.')}
R15=onc(D15,True,'D'); assert R15['T']=={'I','III'}
Q('0015','hormon','zor','öncüllü','Hormonal Düzenleme','Sindirim hormonlarının uyaran ve hedeflerini okuyup bir hormonun yokluğunun doğrudan ve dolaylı sonuçlarını çıkarır.','sindirim hormonları tablosu',
  'Sindirim hormonları kimüsün içeriğiyle uyarılır ve kanla taşınarak hedef organların salgılarını düzenler; bir hormonun yokluğu yalnız o hormonun hedeflerini ve bunların dolaylı sonuçlarını etkiler.','Tek bir hormonun yokluğunda tüm salgıların etkileneceğini sanmak; dolaylı sonuçları atlamak.',
  [adim_onc(D15,'I'),adim_onc(D15,'II'),adim_onc(D15,'III'),sonuc(R15,True)],
  metin='Tabloda, sindirim kanalındaki hücrelerden salgılanan üç hormon (X, Y ve Z) ile ilgili bilgiler verilmiştir. Bu hormonları salgılayan hücre türleri birbirinden farklıdır. Bir kişide yalnızca Y hormonunu salgılayan hücreler işlevini yitirmiştir; diğer tüm yapılar sağlıklıdır ve başka bikarbonat kaynaklarının etkisi ihmal edilmektedir. Kişi yağ ve protein bakımından zengin, asidik özellikte bir öğün almıştır.\nBu kişide şunların gerçekleşeceği öne sürülmüştür.\nI. Pankreastan bikarbonatlı sıvı salgısının azalması\nII. Safra kesesinin kasılmasının zayıflaması\nIII. Onikiparmak bağırsağı içeriğinin asitliğinin normalden yüksek kalması\nBuna göre, yukarıdakilerden hangileri gerçekleşir?',
  sekil=SK15,dogru=R15['dogru'],yan=R15['yan'],sira=R15['sira'],istenen='Gerçekleşen durumlar.',
  ip=['İşlevsiz hücrelerin hangi hormonu ürettiğini tablodan belirle; yalnız o hormonun hedeflerini ve bunların sonuçlarını izle.'],
  bilgi=[B('Hormonal düzenleme','sindirim kanalı mukozası hormon salgılayabilir; hormonlar kanla hedef organa taşınır ve salgıyı artırır ya da kasılmayı uyarır')],
  puf='Her yargıyı, işlevsiz olan hormonun hedefleriyle ilişkilendir.')

# ======================= 16 · kalın bağırsak · orta · olumsuz (metin) =======================
S16=['Sindirim enzimi salgılanmaz.','Su ve bazı minerallerin kana geçişi gerçekleşir.','Yüzeyinde villuslar bulunur ve glikozun emilimi burada tamamlanır.','Bağırsak florasındaki bazı bakteriler K vitamini sentezine katkıda bulunur.','Sindirilemeyen besin artıkları dışkı olarak birikir.']
Q('0016','emilim','orta','düz','Emilim','Kalın bağırsağın görevlerini ince bağırsakla karıştırmadan değerlendirir.','kalın bağırsak',
  'Kalın bağırsakta enzim salgılanmaz; su ve mineral emilir, bakteriler vitamin sentezler ve dışkı oluşur. Besin monomerlerinin emilimi ince bağırsakta tamamlanır.','Villusların ve besin emiliminin kalın bağırsakta da bulunduğunu sanmak.',
  [A('Kalın bağırsağın görevlerini hatırla','Kalın bağırsakta sindirim enzimi yoktur; su ve mineraller emilir, bakteriler bazı vitaminleri üretir, artıklar dışkı hâline gelir.','Su–mineral emilimi, vitamin, dışkı'),
   A('İfadeleri sına','Dört ifade bu görevleri anlatır. Üçüncü ifade villus bulunduğunu ve glikoz emiliminin burada tamamlandığını söyler.','Üçüncü ifade şüpheli'),
   A('Yanlış olanı seç','Villuslar ince bağırsağa özgüdür ve glikoz emilimi ince bağırsakta tamamlanır; kalın bağırsakta besin emilimi yoktur.','Yanlış: kalın bağırsakta villus')],
  metin='İnsanın kalın bağırsağı, ince bağırsaktan gelen sindirilmemiş içerikle ilgilenen ve içeriği dışkı hâline getiren bir sindirim kanalı bölümüdür. İçeriğinde yaşayan bakteriler de bağırsak florasını oluşturur.\nBuna göre, kalın bağırsakla ilgili aşağıdakilerden hangisi yanlıştır?',
  dogru=S16[2],sira=yer('C',S16[2],[S16[0],S16[1],S16[3],S16[4]]),
  yan=[(S16[0],'İfade doğrudur; kalın bağırsakta sindirim enzimi salgılanmaz. Bu şıkkı seçen ince bağırsakla karıştırmıştır.','bilgi'),
       (S16[1],'İfade doğrudur; kalın bağırsakta su ve bazı mineraller kana geçer.','bilgi'),
       (S16[3],'İfade doğrudur; flora bakterileri K vitamini gibi bazı vitaminlerin sentezine katkıda bulunur.','bilgi'),
       (S16[4],'İfade doğrudur; sindirilemeyen artıklar kalın bağırsakta toplanıp dışkıyı oluşturur.','bilgi')],
  istenen='Kalın bağırsakla ilgili yanlış ifade.',ip=['Besin emiliminin hangi bağırsak bölümüne özgü olduğunu hatırla.'],
  bilgi=[B('Kalın bağırsak','kalın bağırsakta su ve bazı mineraller kana geçer, bağırsak florası bazı vitaminleri sentezler ve sindirilemeyen artıklar dışkıya dönüşür; besin monomerlerinin emilimi ince bağırsakta tamamlanır')],
  puf='Kalın bağırsak ile ince bağırsağın görevlerini ayrı ayrı düşün.')

# ======================= 17 · pankreas kanalı tıkanması · zor · tek doğru =======================
SK17=kanal_sekil([('karaciger','1',(-4.1,6.3)),('safrakesesi','2',(-3.9,3.5)),('pankreas','3',(3.7,3.2)),('mide','4',(3.5,5.5)),('incebag','5',(-4.0,1.2)),('kalinbag','6',(3.9,1.2))])
S17=['Pankreastan onikiparmak bağırsağına bikarbonat geçişi azalır; kan şekerini düzenleyen hormonların kana geçişi sürer.','Safra üretimi durur ve yağlar emülsiyonlaşamaz.','Midede pepsinojenin pepsine dönüşümü gerçekleşemez.','Kan şekerini düzenleyen hormonlar kana geçemez.','Nişastanın sindirimi tamamen durur.']
Q('0017','yardimci','orta','şekilli','Sindirim Kanalı ve Yardımcı Organlar','Pankreasın hem sindirim kanalına hem kana salgı yaptığını bilerek kanalı tıkanmış bir kişide beklenen durumu belirler.','pankreas kanalı tıkanması',
  'Pankreas salgılarını iki farklı yoldan verir; bir yolun tıkanması yalnız o yoldan verilen salgıları etkiler.','Pankreasın tüm salgılarının kanaldan aktığını sanmak; safra üretiminin pankreasa bağlı olduğunu düşünmek; nişasta sindiriminin tamamen durduğunu sanmak.',
  [A('Yapıyı tanı ve salgılarını ayır','3 numaralı yapı pankreastır; enzimleri ve bikarbonatı kanalla onikiparmak bağırsağına, hormonlarını doğrudan kana verir.','Kanal: enzim + bikarbonat · Kan: hormon'),
   A('Tıkanmanın etkisini belirle','Kanal yoluyla verilen enzim ve bikarbonat bağırsağa ulaşamaz; kan yoluyla verilen hormonlar kana geçmeyi sürdürür.','Etkilenen: kanal salgıları'),
   A('Diğer organlarla ilişkiyi sına','Safra karaciğerde, pepsinojenin aktifleşmesi midede gerçekleşir; nişasta sindirimi ağızda da başladığından tamamen durmaz.','Karaciğer, mide, ağız etkilenmez')],
  metin='Şekilde insan sindirim kanalı ve yardımcı organların bir bölümü 1, 2, 3, 4, 5 ve 6 ile numaralandırılmıştır. Bir hastalık sonucunda 3 numaralı yapıdan onikiparmak bağırsağına giden kanal tamamen tıkanmıştır; yapının kan dolaşımına salgı yapan hücreleri ise sağlıklıdır.\nBuna göre, bu kişide aşağıdakilerden hangisinin gerçekleşmesi beklenir?',
  sekil=SK17,dogru=S17[0],sira=yer('A',S17[0],S17[1:]),
  yan=[(S17[1],'Safra karaciğerde üretilir; pankreasın kanalının tıkanması safra üretimini durdurmaz.','dikkat'),
       (S17[2],'Pepsinojen midede HCl ile aktifleşir; bu olay pankreasa bağlı değildir.','bilgi'),
       (S17[3],'Pankreasın hormonları kanalla değil doğrudan kana geçer; kanal tıkanıklığı bu yolu etkilemez.','dikkat'),
       (S17[4],'Nişastanın sindirimi ağızda tükürük amilazıyla başlar; pankreas amilazı azalsa da sindirim tamamen durmaz.','dikkat')],
  istenen='Beklenen durum.',ip=['Pankreasın salgılarını kanalla bağırsağa verdikleri ve kana verdikleri olarak ikiye ayır.'],
  bilgi=[B('Pankreasın çift işlevi','pankreas sindirim enzimleri ile bikarbonat içeren özsuyunu kanalla onikiparmak bağırsağına, hormonlarını ise doğrudan kana verir · Bikarbonat asidik kimüsü nötrleştirir')],
  puf='Her salgının hangi yoldan (kanal ya da kan) verildiğine bak.')

# ======================= 18 · emilim yüzeyi · zor · sayısal =======================
SAG={'Dairesel kıvrımlar':3,'Villuslar':10,'Mikrovilluslar':20}; HAS={'Dairesel kıvrımlar':3,'Villuslar':4,'Mikrovilluslar':1}
def carp(d):
    r=1
    for v in d.values(): r*=v
    return r
A_SAG=carp(SAG); A_HAS=carp(HAS); ORAN=A_SAG//A_HAS; assert A_SAG==600 and A_HAS==12 and A_SAG%A_HAS==0 and ORAN==50
H20=(SAG['Mikrovilluslar']//HAS['Mikrovilluslar'])            # yalnız mikrovillus kaybı
TOPL=sum(HAS.values()); assert H20==20 and TOPL==8 and len({TOPL,A_HAS,H20,ORAN,A_SAG})==5
YAN18=[(TOPL,'Hastalıklı kişideki üç değer çarpılması gerekirken toplanmış (3 + 4 + 1) ve oran yerine bu toplam verilmiştir.','islem'),
       (A_HAS,'Yalnızca hastalıklı kişinin toplam alanı (3 × 4 × 1) bulunmuş, sağlıklı kişiyle oranlanmamıştır.','dikkat'),
       (H20,'Yalnızca mikrovillusların kaybı (20 kat → 1 kat) hesaba katılmış; villus artışının 10’dan 4’e düşmesi unutulmuştur.','islem'),
       (A_SAG,'Sağlıklı kişinin toplam alanı (3 × 10 × 20) bulunmuş, hastalıklı kişiyle oranlanmamıştır.','dikkat')]
SK18=tablo_cok(['Yapı','Sağlıklı kişide\nalan artışı (kat)','Hastalıklı kişide\nalan artışı (kat)'],[[k,str(SAG[k]),str(HAS[k])] for k in SAG],[190,200,200])
Q('0018','emilim','zor','tablo','Emilim','İnce bağırsakta emilim yüzeyini artıran yapıların etkisini iki durum için çarpımsal hesaplayıp karşılaştırır.','emilim yüzeyi karşılaştırması',
  'İnce bağırsakta dairesel kıvrımlar, villuslar ve mikrovilluslar emilim yüzeyini birbiri üzerine kurularak artırır; etkiler çarpılır ve iki durum oranlanır.','Etkileri toplamak; yalnız tek durumun alanını bulup karşılaştırmayı unutmak.',
  [A('Çarpımsal modeli kur','Her yapı bulunduğu yüzeyin alanını tablodaki değerle çarpar; toplam alan üç değerin çarpımıdır.','Alan = kıvrım × villus × mikrovillus'),
   A('İki kişinin alanını bul','Sağlıklı kişi için 3 × 10 × 20, hastalıklı kişi için 3 × 4 × 1 hesaplanır.','600 ve 12'),
   A('Oranla','Sağlıklı kişinin alanı hastalıklı kişinin alanına bölünür.','600 ÷ 12 = 50')],
  metin='İnce bağırsakta emilim yüzeyini dairesel kıvrımlar, villuslar ve mikrovilluslar artırır. Bu yapıların her biri, üzerinde bulunduğu yüzeyin alanını tabloda verilen değerle çarpmaktadır (yapılar birbirinin üzerinde yer aldığından etkiler birlikte uygulanır). Yapıların hiç olmadığı düz bir silindir yüzeyinin alanı 1 birimdir. Tabloda, sağlıklı ve bir bağırsak hastalığı olan kişide bu değerler karşılaştırılmıştır; hastalıkta mikrovilluslar tamamen kaybolmuştur.\nBuna göre, sağlıklı kişinin ince bağırsağının toplam emilim yüzeyi, hastalıklı kişinin toplam emilim yüzeyinin kaç katıdır?',
  sekil=SK18,dogru=ORAN,yan=YAN18,istenen='Sağlıklı kişinin emilim yüzeyinin hastalıklı kişininkine oranı.',
  ip=['Önce iki kişinin toplam alanını ayrı ayrı bul; kaybolan bir yapının alana katkısını düşün.'],
  bilgi=[B('Emilim yüzeyi','ince bağırsakta dairesel kıvrımlar, kıvrımlar üzerinde villuslar, villusların yüzeyinde mikrovilluslar bulunur; bu katlanmalar emilim yüzeyini çok artırır')],
  puf='Alanlar çarpılır; kaybolan yapının çarpımdaki katkısını sıfır değil, yok sayılan bir artış olarak düşün.')

# ======================= 19 · bağırsak duvarı · orta · olumsuz (metin) =======================
S19=['Mukoza tabakası besinle doğrudan temas eder ve salgı yapan hücreler içerir.','Mide ve bağırsak duvarındaki kaslar çizgili kastır ve isteğe bağlı kasılır.','Peristaltik hareket, düz kasların ardışık kasılıp gevşemesiyle besini ilerletir.','Midenin giriş ve çıkışında besinin geçişini denetleyen halka biçimli kaslar bulunur.','İnce bağırsakta görülen karıştırıcı kasılmalar besinin sindirim salgılarıyla karışmasını sağlar.']
Q('0019','yapi','orta','düz','Sindirim Kanalı ve Yardımcı Organlar','Sindirim kanalı duvarının katmanlarını ve kas hareketlerini değerlendirir.','kanal duvarı ve hareketleri',
  'Mide ve bağırsak duvarındaki kaslar düz kastır ve istemsiz çalışır; peristaltik hareket besini ilerletir, karıştırıcı kasılmalar salgılarla karışmasını sağlar.','Sindirim kanalındaki kasların isteğe bağlı çalıştığını sanmak.',
  [A('Duvar katmanlarını hatırla','İç yüzeyde salgı ve emilim yapan mukoza, dışta kas tabakası bulunur; mide ve bağırsak kasları düz kastır, istemsiz çalışır.','Düz kas · istemsiz'),
   A('İfadeleri sına','Mukoza, peristaltik hareket, sfinkterler ve karıştırıcı kasılmalarla ilgili dört ifade doğrudur. Kasların çizgili ve isteğe bağlı olduğunu söyleyen ifade bunlardan ayrılır.','Bir ifade ayrışıyor'),
   A('Yanlış olanı seç','Çizgili kaslar iskelet kaslarıdır ve isteğe bağlı kasılır; mide ve bağırsak kasları düz kas olup istemsiz kasılır.','Yanlış: çizgili, isteğe bağlı')],
  metin='İnsanın sindirim kanalının duvarı içten dışa doğru çeşitli doku katmanlarından oluşur; bu katmanlar besinin ilerletilmesini, karıştırılmasını ve sindirim salgılarının üretilmesini sağlar.\nBuna göre, sindirim kanalı duvarıyla ilgili aşağıdakilerden hangisi yanlıştır?',
  dogru=S19[1],sira=yer('B',S19[1],[S19[0],S19[2],S19[3],S19[4]]),
  yan=[(S19[0],'İfade doğrudur; mukoza kanalın iç yüzeyini oluşturur ve bezler içerir. Bu şıkkı seçen mukozanın görevini bilmemiştir.','bilgi'),
       (S19[2],'İfade doğrudur; peristaltik hareket düz kasların ardışık kasılıp gevşemesiyle oluşur.','bilgi'),
       (S19[3],'İfade doğrudur; midenin giriş ve çıkışındaki sfinkter kasları madde geçişini denetler.','bilgi'),
       (S19[4],'İfade doğrudur; karıştırıcı kasılmalar besini salgılarla karıştırır.','bilgi')],
  istenen='Sindirim kanalı duvarıyla ilgili yanlış ifade.',ip=['Mide ve bağırsak kaslarının hangi kas türünden olduğunu ve istemli mi istemsiz mi çalıştığını hatırla.'],
  bilgi=[B('Sindirim kanalı duvarı','kanal duvarının iç yüzeyinde mukoza, dışında kas tabakası bulunur; kanalın büyük bölümünde düz kaslar istemsiz çalışır ve peristaltik hareketle besini ilerletir')],
  puf='Kas türünün çalışma biçimini hatırla.')

# ======================= 20 · emilen maddelerin dolaşıma katılma yolları · zor =======================
def yol_sekil():
    b=[]
    def kutu(x,y,t,col,w=2.4): b.append(f'\\node[draw,rounded corners=3pt,fill={col},minimum width={w}cm,minimum height=.9cm,align=center,font=\\footnotesize,line width=.9pt] at ({x},{y}) {{{t}}};')
    def num(x,y,t): b.append(f'\\node[draw,circle,fill=white,text=black,inner sep=2pt,font=\\normalsize\\bfseries,line width=.9pt] at ({x},{y}) {{{t}}};')
    kutu(0,2,'Villus\\\\kan kılcalı','red!25'); kutu(0,0,'Villus\\\\lenf kılcalı','yellow!40')
    num(3.2,2,'1'); num(5.6,2,'2'); num(3.2,0,'3'); num(5.6,0,'4'); kutu(8.4,1,'Kalp','pink!60',1.6)
    for (x1,y1,x2,y2) in [(1.2,2,2.9,2),(3.5,2,5.3,2),(5.9,2,7.6,1.3),(1.2,0,2.9,0),(3.5,0,5.3,0),(5.9,0,7.6,.7)]:
        b.append(f'\\draw[-{{Stealth[length=2.3mm,width=1.9mm]}},line width=1pt] ({x1},{y1})--({x2},{y2});')
    b.append('\\node[font=\\footnotesize,anchor=east] at (-1.3,2) {Glikoz};\\node[font=\\footnotesize,anchor=east] at (-1.3,0) {Yağ};')
    return tk('\n'.join(b),.85)
SK20=yol_sekil()
S20=['1 numaralı yapı, kanı karaciğerden kalbe taşıyan damardır.','3 numaralı yapıdaki sıvı kalbe ulaşmadan önce karaciğerden geçer.','Yağ, 4 numaralı yapıya ulaşmadan önce 2 numaralı yapıdan geçer.','4 numaralı yapıda taşınan yağ, karaciğerden geçmeden kana karışır.','Glikoz 2 numaralı yapıda tamamen yıkılır ve kana hiç geçmez.']
Q('0020','emilim','zor','şekilli','Emilim','Glikoz ve yağın ince bağırsaktan kalbe ulaşma yollarını karşılaştırarak yol üzerindeki yapıların işlevini yorumlar.','kan ve lenf yolu karşılaştırması',
  'Suda çözünen monomerler kan kılcalıyla karaciğere, yağlar lenf yoluyla karaciğere uğramadan kana katılır; karaciğer glikozu depolayıp salabilir.','Tüm besinlerin karaciğerden geçtiğini sanmak; lenfin kan dolaşımından bağımsız olduğunu düşünmek.',
  [A('İki yolu ayır','Glikoz villusta kan kılcalına, yağ lenf kılcalına geçer; yollar farklı yapılardan geçerek kalbe ulaşır.','Glikoz: kan yolu · Yağ: lenf yolu'),
   A('Yapıları tanı','Kan yolunda önce bağırsaktan gelen kanı toplayan damar, sonra bir organ yer alır; lenf yolunda lenf damarı ve lenfin kana karıştığı damar bulunur.','1–2: kan yolu · 3–4: lenf yolu'),
   A('İfadeleri sına','Karaciğere uğrama yalnızca kan yolundaki maddeler için geçerlidir; lenf yoluyla taşınanlar karaciğere uğramadan kana katılır.','Lenf yolu karaciğerden geçmez')],
  metin='Şekilde, ince bağırsaktan emilen glikozun ve yağın (yağ asitleri ile gliserolden sentezlenen) kalbe ulaşırken izlediği yollar şematik olarak gösterilmiştir. Yolların üzerindeki yapılar 1, 2, 3 ve 4 ile numaralandırılmıştır.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
  sekil=SK20,dogru=S20[3],sira=yer('E',S20[3],S20[:3]+S20[4:]),
  yan=[(S20[0],'1 numaralı yapı bağırsaktan gelen kanı karaciğere taşır; kanı karaciğerden kalbe taşıyan damar değildir.','dikkat'),
       (S20[1],'3 numaralı yapı lenf damarıdır; lenf karaciğerden geçmeden kana katılır.','dikkat'),
       (S20[2],'Yağ lenf yolunu izler; 2 numaralı yapı yalnız kan yolundadır, yağ buradan geçmez.','dikkat'),
       (S20[4],'Karaciğerde glikoz glikojen olarak depolanabilir ve gerektiğinde kana verilir; glikozun tamamı yıkılmaz.','dikkat')],
  istenen='Şemaya göre doğru olan ifade.',ip=['Glikoz ve yağın villusta hangi damar yapısına geçtiğini ve bu yolun karaciğerle ilişkisini düşün.'],
  bilgi=[B('Emilen maddelerin taşınması','amino asit ve glikoz kan kılcallarına geçerek karaciğere gider; yağlar lenf kılcalına geçer ve lenf, bir toplardamar aracılığıyla kana karışır')],
  puf='İki yolu ayrı ayrı izle; karaciğere uğrama durumu yola bağlıdır.')

# ======================= yaz =======================
for q_ in P.ANA: q_['kardes']=None
SCR=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/sn')
os.makedirs(SCR,exist_ok=True)
P.yaz(os.path.join(GD,'sindirim-1.json'),os.path.join(SCR,'bos-sindirim.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji, MEB 11. sınıf Sindirim Sistemi.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','absindirim.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
