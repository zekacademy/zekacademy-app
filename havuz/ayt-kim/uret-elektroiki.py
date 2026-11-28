"""AYT Kimya · Kimya ve Elektrik · 2. dalga (10 soru), kardeş yok, ipucu 1. Şekil verileri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as K
from _hafif_kim2 import *
from cizim import tikz_svg
KONU_='Kimya ve Elektrik'; UK='akim|Kimya ve Elektrik'
K.KONU=KONU_
P=Parti('elektroiki',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM 2018–2026 AYT Kimya (yalnız mantık) · MEB 11–12. sınıf Kimya ve Elektrik'
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    kart(f'K-AKELEK2-{n}',alt,fikir,tuzak,z,kalip,adim,f'elk2-{tipad}',tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
D=Fr
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
S5=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
S5b=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
S5c=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']

# ---------- şekil yardımcıları ----------
def pil(ox,oy,solL,solR,elL,elR,volt=None):
    s=''
    for bx,sol in [(ox,solL),(ox+3.6,solR)]:
        s+='\\fill[vurgu!15] (%g,%g) rectangle (%g,%g);'%(bx,oy,bx+2.3,oy+1.7)
        s+='\\draw[thick] (%g,%g) -- (%g,%g) -- (%g,%g) -- (%g,%g);'%(bx,oy+2.3,bx,oy,bx+2.3,oy,bx+2.3,oy+2.3)
        s+='\\node[below,align=center] at (%g,%g) {%s};'%(bx+1.15,oy-0.05,sol)
    xl,xr=ox+0.6,ox+5.3
    for x in (xl,xr):
        s+='\\draw[thick,fill=gray!45] (%g,%g) rectangle (%g,%g);'%(x-0.14,oy+0.25,x+0.14,oy+3.0)
    s+='\\node[right] at (%g,%g) {%s};'%(xl+0.2,oy+0.6,elL)
    s+='\\node[left] at (%g,%g) {%s};'%(xr-0.2,oy+0.6,elR)
    s+='\\draw[line width=6pt,gray!55] (%g,%g) -- (%g,%g) -- (%g,%g) -- (%g,%g);'%(ox+1.7,oy+0.9,ox+1.7,oy+2.55,ox+4.2,oy+2.55,ox+4.2,oy+0.9)
    s+='\\draw[line width=4pt,white] (%g,%g) -- (%g,%g) -- (%g,%g) -- (%g,%g);'%(ox+1.7,oy+0.95,ox+1.7,oy+2.55,ox+4.2,oy+2.55,ox+4.2,oy+0.95)
    s+='\\node[above] at (%g,%g) {Tuz köprüsü};'%(ox+2.95,oy+2.62)
    s+='\\draw[thick] (%g,%g) -- (%g,%g) -- (%g,%g);'%(xl,oy+3.0,xl,oy+3.7,ox+2.65,oy+3.7)
    s+='\\draw[thick] (%g,%g) -- (%g,%g) -- (%g,%g);'%(ox+3.25,oy+3.7,xr,oy+3.7,xr,oy+3.0)
    s+='\\draw[thick,fill=white] (%g,%g) circle (.3);\\node at (%g,%g) {V};'%(ox+2.95,oy+3.7,ox+2.95,oy+3.7)
    if volt: s+='\\node[above] at (%g,%g) {%s};'%(ox+2.95,oy+4.05,volt)
    return s
def bat(x,y,wl,wr):
    return ('\\draw[thick] (%g,%g) -- (%g,%g);\\draw[line width=2pt] (%g,%g) -- (%g,%g);'%(wl,y,x-0.1,y,x-0.1,y-0.15,x-0.1,y+0.15)+
            '\\draw[line width=2pt] (%g,%g) -- (%g,%g);\\draw[thick] (%g,%g) -- (%g,%g);'%(x+0.1,y-0.3,x+0.1,y+0.3,x+0.1,y,wr,y)+
            '\\node[above left] at (%g,%g) {$-$};\\node[above right] at (%g,%g) {$+$};'%(x-0.1,y+0.1,x+0.1,y+0.1))
def beaker(bx,w,h,lvl,oy=0):
    return ('\\fill[vurgu!15] (%g,%g) rectangle (%g,%g);\\draw[thick] (%g,%g) -- (%g,%g) -- (%g,%g) -- (%g,%g);'%
            (bx,oy,bx+w,oy+lvl,bx,oy+h,bx,oy,bx+w,oy,bx+w,oy+h))
def elek(x,y0,y1):
    return '\\draw[thick,fill=gray!45] (%g,%g) rectangle (%g,%g);'%(x-0.14,y0,x+0.14,y1)

# ============ 01 · Al–Cu galvanik hücre, öncüllü · kolay · şekil ============
kartla('01','Galvanik hücrede elektron yönü, derişim değişimi ve hücre potansiyeli','Küçük E°’lu elektrot anottur; elektronlar dış devrede anottan katoda akar, anot yarı hücresinde katyon derişimi artar, katot yarı hücresinde azalır; hücre potansiyeli E°(katot) − E°(anot) farkıdır.','Elektron yönünü ters almak; E° farkını hesaplarken değerleri toplamak.','kolay','öncüllü',3,'galvanik','Galvanik hücre yorumu')
assert D('0.34')-D('-1.66')==D('2.00') and D('-1.66')<D('0.34')
SK=tk(pil(0,0.3,'1 M \\ce{Al^{3+}}\\\\(suda)','1 M \\ce{Cu^{2+}}\\\\(suda)','Al','Cu'))
q('0001',tipId='elk2-galvanik',tip='Galvanik hücre yorumu',z='kolay',alt='Elektrotlar ve Elektrokimyasal Hücreler',kaz='Galvanik hücrede elektron yönünü, derişim değişimini ve standart hücre potansiyelini yorumlar.',kalip='öncüllü',
 kart='K-AKELEK2-01 (galvanik hücre yorumu) · Al–Cu hücresi',sekil=SK,
 metin='Bir öğrenci 25 °C’de, şekilde gösterilen düzeneği kurarak 1 M derişimli çözeltilerle bir galvanik hücre hazırlamıştır. Devre tamamlandığında hücre çalışmaya başlamıştır.\nAl³⁺(suda) + 3e⁻ → Al(k)  E° = −1,66 V\nCu²⁺(suda) + 2e⁻ → Cu(k)  E° = +0,34 V\nI. Dış devrede elektronlar Cu elektrottan Al elektroda doğru akar.\nII. Zamanla Al³⁺ iyonlarının derişimi artar.\nIII. Hücrenin standart potansiyeli 2,00 V’tur.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='II ve III',sira=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III'],yan=[('Yalnız I','I’i doğru, II ve III’ü yanlış saymış; elektronların aktif metalden değil Cu’dan aktığını düşünmüştür. Oysa Al anottur ve elektronlar Al’dan Cu’ya akar.','bilgi'),('Yalnız II','III’ü yanlış saymış; E°(katot) − E°(anot) = 0,34 − (−1,66) = 2,00 V olduğunu görmemiştir.','islem'),('I ve III','I’i doğru ve II’yi yanlış saymış; elektron yönünü ters almış ve anotta Al³⁺ derişiminin arttığını görmemiştir.','bilgi'),('I, II ve III','Üç yargıyı da doğru sanmış; elektronların anottan değil katottan anota aktığını düşünmüştür.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['E° değerlerini karşılaştırıp anot ve katodu belirle; sonra elektron yönünü, derişim değişimini ve E° farkını ayrı ayrı sına.'],
 bilgi=[B('Galvanik hücre','Küçük E°’lu elektrot anot, büyük E°’lu elektrot katottur; elektronlar dış devrede anottan katoda akar. Anotta yükseltgenen metal çözeltiye katyon verir, katotta katyon indirgenir. Örnek: Mg–Ag hücresinde Mg anot, Ag katottur ve elektronlar Mg’den Ag’ye akar')],
 ad=[A('Anot ve katodu bul','E° değeri küçük olan Al yükseltgenir, Cu²⁺ indirgenir.','Anot: Al · Katot: Cu'),A('I’i değerlendir','Elektronlar anottan katoda akar.','Al → Cu → I yanlış'),A('II’yi değerlendir','Anotta Al, Al³⁺ iyonuna dönüşür.','[Al³⁺] artar → II doğru'),A('III’ü değerlendir','E° = E°(katot) − E°(anot).','0,34 − (−1,66) = 2,00 V → III doğru')],
 puf='Elektron yönünü ve derişim değişimini her yarı hücre için ayrı düşün.')

# ============ 02 · erimiş NaBr elektrolizi, yanlış ifade · kolay · şekil ============
kartla('02','Erimiş tuz elektrolizi','Elektroliz hücresinde üretecin (+) kutbuna bağlı elektrot anottur; anyonlar anotta yükseltgenir, katyonlar katotta indirgenir; elektronlar anottan üretece, üreteçten katoda akar; katyonlar katoda, anyonlar anoda gider.','İyonların yönünü galvanik hücre gibi düşünmek.','kolay','şekilli',3,'elektroliz','Elektroliz')
g=beaker(0,3.8,2.6,2.0)+elek(0.9,0.5,3.2)+elek(2.9,0.5,3.2)
g+='\\draw[thick] (0.9,3.2) -- (0.9,4.3) -- (1.55,4.3);\\draw[thick] (2.9,3.2) -- (2.9,4.3) -- (2.25,4.3);'+bat(1.9,4.3,1.55,2.25)
g+='\\node[right] at (1.05,0.8) {X};\\node[left] at (2.75,0.8) {Y};\\node[below] at (1.9,-0.05) {Erimiş \\ce{NaBr}, grafit elektrot};'
SK=tk(g)
S2=['Y elektrotunda Br₂ gazı oluşur.','X elektrotunda Na metali oluşur.','Dış devrede elektronlar Y elektrottan X elektroda doğru akar.','Elektroliz ilerledikçe kaptaki Na⁺ iyonlarının sayısı azalır.','Na⁺ iyonları Y elektroduna doğru hareket eder.']
q('0002',tipId='elk2-elektroliz',tip='Elektroliz',z='kolay',alt='Elektroliz',kaz='Erimiş tuz elektrolizinde elektrotları, ürünleri ve iyon–elektron akış yönünü belirler.',kalip='şekilli',
 kart='K-AKELEK2-02 (erimiş tuz elektrolizi) · NaBr, grafit elektrotlar',sekil=SK,
 metin='Şekildeki düzenekte, erimiş NaBr içine daldırılan iki grafit elektrot bir üretece bağlanmıştır. Üretecin gerilimi elektrolizin başlaması için yeterlidir ve kaptaki Na⁺ ile Br⁻ iyonlarından başka tanecik yoktur.\nBuna göre bu elektroliz hücresiyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=S2[4],sira=[S2[4],S2[0],S2[1],S2[2],S2[3]],yan=[(S2[0],'Bu ifade doğrudur; öğrenci Y’yi katot sanıp anotta Br₂ oluşmayacağını düşünmüş. Y, üretecin (+) kutbuna bağlı olduğundan anottur ve Br⁻ yükseltgenerek Br₂ verir.','bilgi'),(S2[1],'Bu ifade doğrudur; öğrenci X’i anot sanmış. X üretecin (−) kutbuna bağlı katottur ve Na⁺ indirgenerek Na metali oluşur.','bilgi'),(S2[2],'Bu ifade doğrudur; öğrenci elektronların katottan anoda aktığını düşünmüş. Elektronlar yükseltgenmenin olduğu anottan dış devreye verilir.','bilgi'),(S2[3],'Bu ifade doğrudur; öğrenci Na⁺ iyonlarının elektroliz boyunca sabit kaldığını sanmış. Na⁺ katotta Na’ya indirgendiği için sayısı azalır.','dikkat')],
 istenen='Yanlış olan ifade.',ip=['Önce üretecin hangi kutbuna hangi elektrotun bağlı olduğunu belirle; katyonların ve anyonların hangi elektrota çekildiğini düşün.'],
 bilgi=[B('Elektroliz hücresinde iyon yönleri','elektroliz hücresinde katyonlar (−) kutba bağlı katoda, anyonlar (+) kutba bağlı anoda gider. Elektronlar anottan üretece, üreteçten katoda akar. Örnek: erimiş KI elektrolizinde K⁺ katoda, I⁻ anoda yönelir')],
 ad=[A('Elektrotları belirle','Y, üretecin (+) kutbuna; X, (−) kutbuna bağlıdır.','Y: anot, X: katot'),A('Ürünleri yaz','Anotta Br⁻ yükseltgenir, katotta Na⁺ indirgenir.','2Br⁻ → Br₂ + 2e⁻ · Na⁺ + e⁻ → Na'),A('İyon ve elektron yönü','Katyonlar katoda, anyonlar anoda gider; elektronlar anottan katoda dış devreden akar.','Na⁺ → X, Br⁻ → Y, e⁻: Y → X'),A('İfadeleri ele','Na⁺ iyonları X’e gider, Y’ye değil.','Yanlış: Na⁺ iyonları Y’ye hareket eder')],
 puf='Elektrolizde katyonlar katoda, anyonlar anoda gider; (+) kutba bağlı elektrot anottur.')

# ============ 03 · E–log Q grafiği · zor · grafik ============
kartla('03','Hücre potansiyeli–logaritmik Q grafiği','E = E° − (0,059/n)·log Q; grafikte kesim noktası E°’yi, eğim −0,059/n’yi verir; n eğimden bulunur.','Eğimden n’yi bulmadan 0,059 almak; grafikte okunan değeri yanıt sanmak.','zor','grafik',5,'nernst','Nernst eşitliği')
E0=D('1.2'); slope=(D('1.082')-D('1.2'))/4; assert slope==D('-0.0295')
n3=D('0.059')/(-slope); assert n3==2
logQ=6; r_dog=E0-D('0.059')/2*logQ; assert r_dog==D('1.023')
r_n1=E0-D('0.059')*logQ; assert r_n1==D('0.846')
r_x4=D('1.082')-D('0.059')/2*logQ; assert r_x4==D('0.905')
r_oku=D('1.082')
r_isr=E0+D('0.059')/2*logQ; assert r_isr==D('1.377')
g='''\\begin{axis}[width=7cm,height=5.8cm,xmin=0,xmax=4.6,ymin=1.05,ymax=1.25,xtick={0,2,4},ytick={1.082,1.141,1.2},yticklabels={1{,}082,1{,}141,1{,}200},tick label style={font=\\small},axis lines=left,xlabel={$\\log Q$},ylabel={$E$ (V)},label style={font=\\small},grid=both,grid style={dotted,gray!50}]
\\addplot[thick,vurgu,mark=*,mark size=1.6pt] coordinates {(0,1.2) (2,1.141) (4,1.082)};
\\end{axis}'''
SK=tk(g)
q('0003',tipId='elk2-nernst',tip='Nernst eşitliği',z='zor',alt='Elektrot Potansiyelleri',kaz='Hücre potansiyeli–log Q grafiğinden E° ve elektron sayısını bulup Nernst eşitliğiyle potansiyel hesaplar.',kalip='grafik',
 kart='K-AKELEK2-03 (E–log Q grafiği) · eğimden n, kesimden E°',sekil=SK,
 metin='Bir öğrenci, 25 °C’de çalışan bir galvanik hücrenin potansiyelini (E), hücre tepkimesinin derişimler türünden denge kesrine (Q) bağlı olarak ölçmüş ve sonuçları şekildeki grafiğe işlemiştir. Tepkimede aktarılan elektron sayısı (n) verilmemiştir.\n(25 °C’de Nernst eşitliğinde logaritmik terimin katsayısı 0,059/n alınacaktır.)\nBuna göre aynı hücrede Q = 10⁶ olduğunda hücre potansiyeli kaç volt olur?',
 dogru=r_dog,yan=[(r_n1,'Eğimden n’yi bulmayıp n = 1 almış; E = 1,200 − 0,059 × 6 = 0,846 V hesaplamıştır.','bilgi'),(r_x4,'E° yerine grafikte log Q = 4 için okuduğu 1,082 V’u almış; 1,082 − 0,0295 × 6 = 0,905 V bulmuştur.','dikkat'),(r_oku,'Q = 10⁶ için hesap yapmayıp grafikteki son noktayı (log Q = 4) okuyarak 1,082 V demiştir.','dikkat'),(r_isr,'Logaritmik terimin işaretini ters alarak E = E° + (0,059/n)·log Q yazmış; 1,200 + 0,0295 × 6 = 1,377 V bulmuştur.','islem')],
 istenen='Q = 10⁶ iken hücre potansiyeli (V).',ip=['Grafiğin kesim noktası ve eğimi hangi büyüklüklerle ilişkilidir? Eğimi iki noktadan hesapla.'],
 bilgi=[B('Nernst eşitliğinin grafiği','E = E° − (0,059/n)·log Q doğrusunda, log Q = 0 iken E = E°’dir ve doğrunun eğimi −0,059/n’dir. Örnek: eğimi −0,0197 olan bir doğruda n = 0,059 ÷ 0,0197 = 3’tür')],
 ad=[A('E°’yi oku','log Q = 0 noktasında E = E° olur.','E° = 1,200 V'),A('Eğimi bul','İki noktadan eğim: (1,082 − 1,200) ÷ (4 − 0).','Eğim = −0,0295 V'),A('n’yi hesapla','Eğim −0,059/n’ye eşittir.','n = 0,059 ÷ 0,0295 = 2'),A('Q = 10⁶ için E','log 10⁶ = 6 yazılır.','E = 1,200 − 0,0295 × 6'),A('Sonucu yaz','Çarpma ve çıkarma yapılır.','E = 1,200 − 0,177 = 1,023 V')],
 puf='Nernst doğrusunda kesim E°, eğim −0,059/n’dir.')

# ============ 04 · galvanizli ve kalaylı levha · orta · öncüllü · şekil ============
kartla('04','Kaplamalı demir ve korozyon','Kaplama çizilince açıkta kalan demir ile kaplama metali bir pil oluşturur; bu pilde E° değeri küçük olan metal anot olur ve yükseltgenir.','Çizildiğinde her kaplamanın demiri koruyacağını sanmak; elektron yönünü ters almak.','orta','öncüllü',4,'korozyon','Korozyon ve kaplamalı metaller')
EZ,EF,ES=D('-1.66'),D('-0.44'),D('-0.25')
assert EZ<EF<ES
I4=[False,True,False]  # I: 1. levhada demir anot (yanlış) · II: 2. levhada yükseltgenen Fe (doğru) · III: 1. levhada e⁻ Fe→Zn (yanlış)
g=''
for ox,ad_,kp in [(0,'1. levha','Al'),(4.6,'2. levha','Ni')]:
    g+='\\draw[thick,fill=gray!45] (%g,0) rectangle (%g,0.9);'%(ox,ox+3.4)
    g+='\\node at (%g,0.45) {Fe};'%(ox+1.7)
    g+='\\draw[thick,fill=vurgu!30] (%g,0.9) rectangle (%g,1.25);\\draw[thick,fill=vurgu!30] (%g,0.9) rectangle (%g,1.25);'%(ox,ox+1.35,ox+2.05,ox+3.4)
    g+='\\node[above] at (%g,1.55) {%s kaplama};'%(ox+1.7,kp)
    g+='\\draw[thick,fill=white] (%g,1.25) ellipse (0.55 and 0.25);\\node at (%g,1.25) {\\small H$_2$O};'%(ox+1.7,ox+1.7)
    g+='\\node[below] at (%g,-0.05) {%s};'%(ox+1.7,ad_)
SK=tk(g)
S4=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
q('0004',tipId='elk2-korozyon',tip='Korozyon ve kaplamalı metaller',z='orta',alt='Korozyon',kaz='Kaplamalı demirde çizik oluştuğunda anot–katot ve elektron akışını E° değerlerine göre yorumlar.',kalip='öncüllü',
 kart='K-AKELEK2-04 (galvanizli–kalaylı levha) · çizik ve nemli ortam',sekil=SK,
 metin='Demir levhaların yüzeyi, şekilde görüldüğü gibi biri alüminyum, diğeri nikel ile kaplanmıştır. Her iki levhanın kaplaması çizilerek demir açığa çıkarılmış ve çizik bölgeye su damlatılmıştır. Çiziklerde, açıkta kalan metallerle kaplama arasında bir pil oluşmaktadır.\nAl³⁺ + 3e⁻ → Al  E° = −1,66 V\nFe²⁺ + 2e⁻ → Fe  E° = −0,44 V\nNi²⁺ + 2e⁻ → Ni  E° = −0,25 V\nI. 1. levhada çizik bölgede demir anot olarak davranır.\nII. 2. levhada çizik bölgede yükseltgenen metal demirdir.\nIII. 1. levhada dış devrede elektronlar demirden alüminyuma doğru akar.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='Yalnız II',sira=S4,yan=[('Yalnız I','I’i doğru, II’yi yanlış saymış; alüminyumu demirden az aktif sanıp demirin yükseltgeneceğini düşünmüş. E° değeri küçük olan alüminyum yükseltgenir.','bilgi'),('I ve II','I’i de doğru saymış; kaplamayı koruyucu sanma düşüncesiyle iki levhada da demirin anot olduğunu düşünmüştür. 1. levhada anot alüminyumdur.','bilgi'),('I ve III','II’yi yanlış saymış; nikelin demirden daha aktif olduğunu düşünüp demirin korunacağını sanmıştır. Ni’nin E° değeri demirinkinden büyüktür.','bilgi'),('I, II ve III','Üç yargıyı da doğru sanmış; elektronların aktifliği az olan metalden fazla olana aktığını düşünmüştür. Elektronlar anot olan alüminyumdan demire akar.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Her çizikte pili oluşturan iki metalin E° değerlerini karşılaştır; küçük olan hangi levhada hangi metaldir?'],
 bilgi=[B('Kaplamalı metaller ve pil','nemli ortamda birbirine değen iki metal bir pil oluşturur; E° değeri küçük olan metal anot olur, yükseltgenir ve çözünür; büyük olan katot olur. Örnek: Zn–Cu çifti nemli ortamda temas ederse Zn anot, Cu katot olur')],
 ad=[A('1. levhayı incele','Al’nin E° değeri Fe’ninkinden küçüktür.','Anot: Al · Katot: Fe → I yanlış'),A('2. levhayı incele','Ni’nin E° değeri Fe’ninkinden büyüktür.','Anot: Fe · Katot: Ni → II doğru'),A('Elektron yönünü bul','1. levhada elektronlar anottan katoda akar.','Al → Fe → III yanlış'),A('Sonuç','Yalnız II doğrudur.','Yalnız II')],
 puf='Çizikte oluşan pilde iki metalin E° değerlerini karşılaştır.')

# ============ 05 · Zn–Ag Nernst, potansiyel değişimi · orta · düz ============
kartla('05','Nernst eşitliği ile potansiyel değişimi','Q’da ürün derişimleri paya, girenler paydaya yazılır ve katsayılar üs olur; derişimler değişince potansiyel farkı, (0,059/n) ile log Q farkının çarpımıdır.','Gümüş derişiminin karesini almamak; n yerine 1 almak; log Q farkının işaretini karıştırmak.','orta','düz',4,'nernst','Nernst eşitliği')
EAg,EZn5=D('0.80'),D('-0.76'); E05=EAg-EZn5; assert E05==D('1.56')
Q1=D('0.1')/D('0.1')**2; Q2=D('1')/D('0.01')**2; assert (Q1,Q2)==(10,10000)
dE=D('0.059')/2*(4-1); assert dE==D('0.0885')
d_n1=D('0.059')*3; assert d_n1==D('0.177')
d_us=D('0.059')/2*(2-0); assert d_us==D('0.059')     # Ag⁺ derişimi karesiz: Q1=1, Q2=100
d_top=D('0.059')/2*(4+1); assert d_top==D('0.1475')
d_zn=D('0.059')/2*4; assert d_zn==D('0.118')
q('0005',tipId='elk2-nernst',tip='Nernst eşitliği',z='orta',alt='Elektrot Potansiyelleri',kaz='Derişimleri değiştirilen hücrenin potansiyelindeki değişimi Nernst eşitliğiyle hesaplar.',kalip='düz',
 kart='K-AKELEK2-05 (Nernst, potansiyel değişimi) · Zn–Ag hücresi',
 metin='25 °C’de şematik gösterimi aşağıda verilen bir galvanik hücre hazırlanmıştır.\nZn(k) | Zn²⁺(suda, 0,1 M) || Ag⁺(suda, 0,1 M) | Ag(k)\nZn²⁺(suda) + 2e⁻ → Zn(k)  E° = −0,76 V\nAg⁺(suda) + e⁻ → Ag(k)  E° = +0,80 V\nBu hücrede Zn²⁺ derişimi 1 M’a çıkarılıp Ag⁺ derişimi 0,01 M’a düşürülüyor.\n(25 °C’de Nernst eşitliğinde logaritmik terimin katsayısı 0,059/n alınacaktır; n, tepkimede aktarılan elektron sayısıdır.)\nBuna göre hücre potansiyeli kaç volt azalır?',
 dogru=dE,yan=[(d_zn,'Başlangıç Q’yu bulurken Ag⁺ derişiminin karesini almamış (Q₁ = 1, log Q₁ = 0); (0,059 ÷ 2) × (4 − 0) = 0,118 V bulmuştur.','bilgi'),(d_us,'Ag⁺ derişiminin karesini almamış; Q’yu 1’den 100’e giden bir değişim sanıp (0,059 ÷ 2) × 2 = 0,059 V bulmuştur.','bilgi'),(d_top,'log Q değerlerini çıkarmak yerine toplamış (1 + 4 = 5); (0,059 ÷ 2) × 5 = 0,1475 V bulmuştur.','islem'),(d_n1,'Aktarılan elektron sayısını 1 almış; 0,059 × 3 = 0,177 V bulmuştur.','bilgi')],
 istenen='Hücre potansiyelindeki azalma (V).',ip=['Hücre tepkimesini elektron sayıları eşit olacak biçimde yazıp her iki durum için Q’yu katsayıları üs yaparak kur.'],
 bilgi=[B('Q yazımı','denge kesrinde saf katılar yer almaz, her iyonun derişimi tepkimedeki katsayısı kadar üs alır. Örnek: Zn + 2Fe³⁺ → Zn²⁺ + 2Fe²⁺ tepkimesi için Q = [Zn²⁺][Fe²⁺]² ÷ [Fe³⁺]² olur')],
 ad=[A('Hücre tepkimesi','Zn anot, Ag katottur; Ag yarı tepkimesi 2 ile çarpılır.','Zn + 2Ag⁺ → Zn²⁺ + 2Ag · n = 2'),A('İlk Q','Q = [Zn²⁺] ÷ [Ag⁺]².','0,1 ÷ (0,1)² = 10 → log Q = 1'),A('Son Q','Yeni derişimler yazılır.','1 ÷ (0,01)² = 10⁴ → log Q = 4'),A('Potansiyel farkı','E = E° − (0,059 ÷ n) log Q olduğundan fark log Q farkıyla orantılıdır.','ΔE = (0,059 ÷ 2) × (4 − 1)'),A('Sonuç','Çarpımı hesapla.','0,0295 × 3 = 0,0885 V azalır')],
 puf='Q’da katsayılar üs olur; potansiyel farkı log Q farkından bulunur.')

# ============ 06 · seri bağlı NaCl ve CuSO4 elektrolizi, gaz mol oranı · zor · şekil ============
kartla('06','Seri bağlı elektroliz kapları ve gaz miktarı','Seri bağlı kaplardan aynı yük geçer; her kapta elektrot ürünü o kaptaki iyonlara ve suya göre belirlenir, ürün miktarı geçen elektron mol sayısıyla ilişkilendirilir.','Anotta Cl⁻ ya da su ayrımını yapmamak; elektron mol sayısını gaz mol sayısına doğrudan eşitlemek.','zor','şekilli',5,'elektroliz','Elektroliz')
i6,t6=D('1.93'),5000; Q6=i6*t6; ne6=Q6/96500; assert Q6==9650 and ne6==D('0.1')
n1=ne6/2+ne6/2; n2=ne6/4; assert (n1,n2)==(D('0.1'),D('0.025')) and n1/n2==4
r_cl=(ne6/2)/n2; assert r_cl==2
r_o2=(ne6/2+ne6/4)/n2; assert r_o2==3
r_8=n1/(ne6/8); assert r_8==8
r_1=n1/ne6; assert r_1==1
g=beaker(0,3.6,2.6,2.0)+elek(0.9,0.5,3.2)+elek(2.7,0.5,3.2)+beaker(4.6,3.6,2.6,2.0)+elek(5.5,0.5,3.2)+elek(7.3,0.5,3.2)
g+='\\draw[thick] (0.9,3.2) -- (0.9,4.4) -- (3.8,4.4);\\draw[thick] (4.4,4.4) -- (7.3,4.4) -- (7.3,3.2);'+bat(4.1,4.4,3.8,4.4)
g+='\\draw[thick] (2.7,3.2) -- (2.7,3.75) -- (5.5,3.75) -- (5.5,3.2);'
for bx,by in [(0.65,1.0),(0.8,1.5),(0.7,1.9),(2.95,1.1),(2.85,1.6),(3.0,1.95),(7.55,1.2),(7.45,1.7)]:
    g+='\\draw[thin] (%g,%g) circle (0.08);'%(bx,by)
g+='\\node[below,align=center] at (1.8,-0.05) {I. kap\\\\\\ce{NaCl}(suda)};\\node[below,align=center] at (6.4,-0.05) {II. kap\\\\\\ce{CuSO4}(suda)};'
g+='\\node[align=left,right] at (8.5,2.0) {Pt elektrot\\\\$i=1{,}93$ A\\\\$t=5000$ s};'
SK=tk(g)
q('0006',tipId='elk2-elektroliz',tip='Elektroliz',z='zor',alt='Elektroliz',kaz='Seri bağlı sulu NaCl ve CuSO₄ elektrolizinde elektrot ürünlerini belirleyip toplanan gaz mol sayılarını karşılaştırır.',kalip='şekilli',
 kart='K-AKELEK2-06 (seri bağlı kaplar, gaz oranı) · Pt elektrot, sabit akım',sekil=SK,
 metin='Platin elektrotlar kullanılarak sulu NaCl ve sulu CuSO₄ çözeltileri, şekilde verilen seri bağlı düzenekte akım ve süre koşullarında elektroliz edilmektedir. Elektrotlarda oluşan gazların tamamı toplanmakta ve gazların suda çözünmediği kabul edilmektedir.\n(1 mol elektronun yükü = 96500 C)\nBuna göre I. kapta toplanan gazların toplam mol sayısının, II. kapta toplanan gazın mol sayısına oranı kaçtır?',
 dogru=D(4),yan=[(r_cl,'I. kapta yalnız anottaki Cl₂’yi saymış; 0,05 ÷ 0,025 = 2 bulmuştur, katottaki H₂’yi unutmuştur.','dikkat'),(r_o2,'I. kapta anotta Cl₂ yerine O₂ çıktığını düşünmüş; (0,05 + 0,025) ÷ 0,025 = 3 bulmuştur.','bilgi'),(r_8,'II. kapta 1 mol O₂ için 8 mol elektron gerektiğini varsaymış; 0,1 ÷ 0,0125 = 8 bulmuştur.','bilgi'),(r_1,'II. kapta anotta 0,1 mol gaz çıktığını (elektron mol sayısı kadar) sanmış; 0,1 ÷ 0,1 = 1 bulmuştur.','bilgi')],
 istenen='I. kaptaki toplam gaz mol sayısının II. kaptaki gaz mol sayısına oranı.',ip=['Seri bağlı kaplardan geçen yükü ve her kapta her elektrotta hangi taneciğin tepkime verdiğini ayrı ayrı belirle.'],
 bilgi=[B('Elektroliz ve geçen yük','Geçen yük Q = i × t bağıntısıyla bulunur; yükü 96500’e bölmek elektronun mol sayısını verir. Sulu çözeltide katotta ve anotta tepkime veren tanecik, iyonların ve suyun yükseltgenme–indirgenme eğilimine göre belirlenir. Örnek: 2 A akım 965 s geçince 1930 C yük, yani 0,02 mol elektron geçer')],
 ad=[A('Elektron mol sayısı','Seri bağlı kaplardan aynı yük geçer; Q = i × t ve elektron mol sayısı yükten bulunur.','1,93 × 5000 = 9650 C → 0,1 mol e⁻'),A('I. kapı çöz','Katotta su indirgenir (H₂), anotta Cl⁻ yükseltgenir (Cl₂); her gazın 1 molü için 2 mol e⁻ gerekir.','H₂ = 0,05 mol · Cl₂ = 0,05 mol → 0,1 mol'),A('II. kapı çöz','Katotta Cu²⁺ indirgenir (gaz yok), anotta su yükseltgenir ve O₂ çıkar; 1 mol O₂ için 4 mol e⁻ gerekir.','O₂ = 0,1 ÷ 4 = 0,025 mol'),A('Oranla','I. kaptaki toplam gaz mol sayısı II. kaptaki gaza bölünür.','0,1 ÷ 0,025 = 4')],
 puf='Her kapta elektrotlardaki tepkimeyi ayrı yaz.')

# ============ 07 · SHE hücresi, derişim bulma · orta · şekil ============
kartla('07','Standart hidrojen elektrodu ile derişim bulma','E = E° − (0,059/n)·log Q; ölçülen E ve E° bilinirse Q’dan derişim bulunur. Hidrojen elektrodunda H₂ 1 atm ve H⁺ 1 M’dir.','n yerine 1 almak; log Q işaretini ters kullanmak; ölçülen değeri standart sanmak.','orta','şekilli',4,'nernst','Nernst eşitliği')
EY=D('0.34'); Em=D('0.281')
# Q = [H+]^2/[Y2+] = 1/x ; E = E° - 0,0295 log(1/x) = E° + 0,0295 log x
logx=(Em-EY)/(D('0.059')/2); assert logx==-2
logx_n1=(Em-EY)/D('0.059'); assert logx_n1==-1
logx_isr=(EY-Em)/(D('0.059')/2); assert logx_isr==2
logx_ikisi=(EY-Em)/D('0.059'); assert logx_ikisi==1
SK=tk(pil(0,0.3,'1 M \\ce{H+}\\\\\\ce{H2}(g, 1 atm)','$x$ M \\ce{Y^{2+}}\\\\(suda)','Pt','Y',volt='0,281 V'))
q('0007',tipId='elk2-nernst',tip='Nernst eşitliği',z='orta',alt='Elektrot Potansiyelleri',kaz='Standart hidrojen elektrodu içeren hücrenin ölçülen potansiyelinden iyon derişimini hesaplar.',kalip='şekilli',
 kart='K-AKELEK2-07 (SHE ve voltmetre okuması) · Y²⁺ derişimi',sekil=SK,
 metin='25 °C’de, Pt elektrotlu standart hidrojen yarı hücresi ile x M Y²⁺(suda) çözeltisine daldırılmış Y(k) elektrottan oluşan galvanik hücre, tuz köprüsüyle şekildeki gibi kurulmuş ve voltmetrede okunan değer şekilde verilmiştir.\nY²⁺(suda) + 2e⁻ → Y(k)  E° = +0,34 V\n2H⁺(suda) + 2e⁻ → H₂(g)  E° = 0,00 V\n(25 °C’de Nernst eşitliğinde logaritmik terimin katsayısı 0,059/n alınacaktır; n, tepkimede aktarılan elektron sayısıdır.)\nBuna göre Y²⁺ derişimi (x) kaç molardır?',
 dogru=D('0.01'),yan=[(D('0.1'),'Aktarılan elektron sayısını 1 almış; 0,281 = 0,34 + 0,059·log x eşitliğinden log x = −1, yani x = 0,1 bulmuştur.','bilgi'),(D(1),'Hücrenin standart koşulda olduğunu varsayıp derişimi 1 M almıştır; oysa ölçülen potansiyel E°’den farklıdır.','dikkat'),(D(10),'Hem n’yi 1 almış hem de logaritmik terimin işaretini ters yazmış; 0,281 = 0,34 − 0,059·log x eşitliğinden log x = 1 bulmuştur.','islem'),(D(100),'Logaritmik terimin işaretini ters yazmış; 0,281 = 0,34 − 0,0295·log x eşitliğinden log x = 2, yani x = 100 bulmuştur.','islem')],
 istenen='Y²⁺ derişimi (M).',ip=['Hücre tepkimesini yazıp denge kesrinde hangi iyonun payda, hangisinin pay olduğuna dikkat et.'],
 bilgi=[B('Hidrojen elektrodu','standart hidrojen elektrodunda H₂ basıncı 1 atm, H⁺ derişimi 1 M ve E° = 0,00 V’tur; bu nedenle hücre potansiyelinin E°’den farkı yalnız diğer yarı hücrenin derişiminden gelir. Örnek: H₂ | H⁺ (1 M) || Z⁺ (y M) | Z hücresinde Q = 1/y olur')],
 ad=[A('Hücre tepkimesi','Y katot, hidrojen anottur.','H₂ + Y²⁺ → 2H⁺ + Y, n = 2'),A('E° ve Q','E° = 0,34 − 0 = 0,34 V.','Q = [H⁺]² ÷ [Y²⁺] = 1 ÷ x'),A('Nernst eşitliği','Ölçülen 0,281 V yazılır.','0,281 = 0,34 − 0,0295 × log(1/x)'),A('Logaritmayı çöz','Eşitlik düzenlenir.','log x = (0,281 − 0,34) ÷ 0,0295 = −2'),A('Derişim','x = 10⁻².','x = 0,01 M')],
 puf='Ölçülen E, E°’den farklıysa Nernst’te Q’yu hücre tepkimesine göre kur.')

# ============ 08 · karışımlı sulu çözelti elektrolizi · zor · tablo ============
kartla('08','Katyon karışımının elektrolizinde sıra ve kütle','Katotta indirgenme potansiyeli (E°) büyük olan katyon önce indirgenir; sulu çözeltide E° değeri sudan küçük olan katyonlar (Na⁺) indirgenmez. Her mol e⁻ için mol metal = 1/n.','Sırayı yanlış kurmak; Cu²⁺ için 2 e⁻’yi unutmak; tüm iyonların çöktüğünü sanmak.','zor','tablo',5,'elektroliz','Elektroliz')
mAg,mCu=D(108),D(64)
i8,t8=D('4.825'),3000; Q8=i8*t8; ne8=Q8/96500; assert Q8==D(14475) and ne8==D('0.15')
nAg=D('0.1'); ne_kalan=ne8-nAg*1; assert ne_kalan==D('0.05')
nCu=ne_kalan/2; assert nCu==D('0.025') and nCu<D('0.1')
m_dog=nAg*mAg+nCu*mCu; assert m_dog==D('12.4')
m_cuonce=(ne8/2)*mCu; assert m_cuonce==D('4.8') and ne8/2<D('0.1')
m_yalnizAg=nAg*mAg; assert m_yalnizAg==D('10.8')
m_n1=nAg*mAg+ne_kalan*mCu; assert m_n1==D('14.0')
m_hepsi=nAg*mAg+D('0.1')*mCu; assert m_hepsi==D('17.2')
rows=[['Na⁺ + e⁻ → Na','−2,71'],['2H₂O + 2e⁻ → H₂ + 2OH⁻','−0,83'],['Cu²⁺ + 2e⁻ → Cu','+0,34'],['Ag⁺ + e⁻ → Ag','+0,80']]
SK=tablo_svg(['Yarı hücre tepkimesi','E° (V)'],rows)
q('0008',tipId='elk2-elektroliz',tip='Elektroliz',z='zor',alt='Elektroliz',kaz='Birden fazla katyon içeren sulu çözeltinin elektrolizinde indirgenme sırasını E° tablosundan belirleyip biriken metal kütlesini hesaplar.',kalip='tablo',
 kart='K-AKELEK2-08 (katyon karışımı) · Ag⁺, Cu²⁺, Na⁺ ve su',sekil=SK,
 metin='25 °C’de 0,1 mol AgNO₃, 0,1 mol Cu(NO₃)₂ ve bol miktarda NaNO₃ içeren sulu çözelti, platin elektrotlarla 4,825 A’lık sabit akımla 3000 saniye elektroliz edilmektedir. Katotta yalnız indirgenme potansiyeli (E°) büyük olan taneciğin indirgendiği ve her taneciğin kendi derişimi bitmeden bir sonrakinin indirgenmediği kabul edilmektedir. İlgili yarı hücre tepkimelerinin E° değerleri tabloda verilmiştir.\n(Ag = 108 g/mol; Cu = 64 g/mol; 1 mol elektronun yükü = 96500 C)\nBuna göre katotta biriken toplam metal kütlesi kaç gramdır?',
 dogru=m_dog,yan=[(m_cuonce,'Cu²⁺’nın Ag⁺’dan önce indirgendiğini sanmış; 0,15 mol elektronun tamamını Cu’ya (0,075 mol) verip 4,8 g bulmuştur.','bilgi'),(m_yalnizAg,'Yalnız Ag’nin biriktiğini düşünmüş; 0,1 mol Ag için 10,8 g bulup Cu’yu hesaba katmamıştır.','dikkat'),(m_n1,'Cu için kalan 0,05 mol elektronu doğrudan 0,05 mol Cu saymış; 2 elektron gerektiğini unutarak 10,8 + 3,2 = 14,0 g bulmuştur.','islem'),(m_hepsi,'Çözeltideki bütün Ag⁺ ve Cu²⁺ iyonlarının indirgendiğini sanmış; 10,8 + 6,4 = 17,2 g bulmuştur.','dikkat')],
 istenen='Katotta biriken toplam metal kütlesi (g).',ip=['Tablodan katotta indirgenme sırasını belirle; geçen elektron mol sayısını bu sıraya göre paylaştır.'],
 bilgi=[B('İndirgenme sırası','katotta birden fazla katyon varsa E° değeri en büyük olan önce indirgenir; sulu çözeltide E° değeri suyunkinden küçük olan katyonlar yerine su indirgenir. Örnek: Au³⁺ ve Zn²⁺ içeren sulu çözeltide önce Au³⁺ indirgenir')],
 ad=[A('Sırayı belirle','Katotta E° büyük olan önce indirgenir.','Ag⁺ (+0,80) → Cu²⁺ (+0,34) → su, Na⁺ değil'),A('Elektron mol sayısı','Q = i × t, sonra 96500’e bölünür.','Q = 4,825 × 3000 = 14475 C → 0,15 mol e⁻'),A('Ag⁺ tamamen biter','0,1 mol Ag⁺ için 0,1 mol e⁻ gerekir.','Ag: 0,1 mol → 10,8 g · kalan e⁻ = 0,05 mol'),A('Cu birikimi','Cu²⁺ + 2e⁻ → Cu; kalan elektronla Cu²⁺ bitmez.','Cu: 0,05 ÷ 2 = 0,025 mol → 1,6 g'),A('Toplam kütle','İki metalin kütlesi toplanır.','10,8 + 1,6 = 12,4 g')],
 puf='Önce E° sırasına bak; elektronları sırayla tüket, bitmeyen iyon kalırsa sonraki indirgenmez.')

# ============ 09 · bakır arıtma · orta · öncüllü · şekil ============
kartla('09','Elektrolitik metal arıtma','Ham metal anot, saf metal katot yapılır; anotta Cu ve ondan aktif metaller çözünür, daha az aktif metaller anot çamuru olarak dibe çöker; katotta yalnız Cu birikir.','Anot–katot kütle yönünü karıştırmak; aktif safsızlığın çözeltide kaldığını görmemek.','orta','öncüllü',4,'elektroliz','Elektroliz')
EZn,ECu,EAg9=D('-0.76'),D('0.34'),D('0.80')
assert EZn<ECu<EAg9
I9=[False,True,True]  # I: katot kütlesi azalır (yanlış) · II: Zn²⁺ derişimi artar (doğru) · III: Ag anot çamuru (doğru)
g=beaker(0,4.2,2.6,2.0)+elek(1.0,0.5,3.2)+elek(3.2,0.5,3.2)
g+='\\draw[thick] (1.0,3.2) -- (1.0,4.3) -- (1.75,4.3);\\draw[thick] (3.2,3.2) -- (3.2,4.3) -- (2.45,4.3);'+bat(2.1,4.3,1.75,2.45)
g+='\\node[align=center,above] at (1.0,0.2) {};'
g+='\\node[align=center] at (0.45,3.5) {Saf Cu};\\node[align=center] at (3.75,3.5) {Ham Cu};'
g+='\\node[below] at (2.1,-0.05) {\\ce{CuSO4}(suda)};'
SK=tk(g)
q('0009',tipId='elk2-elektroliz',tip='Elektroliz',z='orta',alt='Elektroliz',kaz='Elektrolitik arıtmada elektrotlardaki değişimleri ve safsızlıkların davranışını yorumlar.',kalip='öncüllü',
 kart='K-AKELEK2-09 (bakır arıtma) · Zn ve Ag safsızlığı',sekil=SK,
 metin='Zn ve Ag safsızlıkları içeren ham bakır levha ile saf bakır levha, şekildeki gibi CuSO₄(suda) çözeltisine daldırılarak üretece bağlanmıştır. Elektroliz, Cu’nun yükseltgenmeye başladığı en küçük gerilimden biraz büyük bir gerilimde yürütülmektedir.\nZn²⁺ + 2e⁻ → Zn  E° = −0,76 V\nCu²⁺ + 2e⁻ → Cu  E° = +0,34 V\nAg⁺ + e⁻ → Ag  E° = +0,80 V\nI. Saf bakır levhanın kütlesi zamanla azalır.\nII. Çözeltide Zn²⁺ iyonlarının derişimi zamanla artar.\nIII. Ag, çözünmeden kaptan dibe çöker.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='II ve III',sira=S5b,yan=[('Yalnız I','Saf bakırı anot sanmış; saf levha üretecin (−) kutbuna bağlı katottur ve üzerinde Cu birikerek kütlesi artar.','bilgi'),('Yalnız III','II’yi yanlış saymış; Zn’nin katotta da biriktiğini düşünmüş. Cu²⁺ daha büyük E°’ya sahip olduğu için katotta Zn²⁺ indirgenmez, çözeltide kalır.','bilgi'),('I ve II','I’i doğru saymış; katot kütlesinin azalacağını düşünmüştür. Katotta Cu biriktiği için kütle artar.','bilgi'),('I ve III','I’i doğru saymış ve II’yi yanlış saymıştır; katot kütlesinin arttığını ve Zn²⁺’nın çözeltide biriktiğini görmemiştir.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Üretecin (+) kutbuna bağlı levhayı belirle; sonra ham bakırdaki her metalin E° değerini Cu ile karşılaştır.'],
 bilgi=[B('Anot çamuru','ham metalin anotta çözünmesi sırasında metalden daha az aktif olan safsızlıklar yükseltgenmez ve anot çamuru olarak dibe çöker; daha aktif safsızlıklar iyon olarak çözeltide kalır. Örnek: ham nikel anodunda altın çamur olur, demir çözeltide kalır')],
 ad=[A('Elektrotları belirle','Ham levha (+) kutba, saf levha (−) kutba bağlıdır.','Ham Cu: anot · Saf Cu: katot'),A('I’i değerlendir','Katotta Cu²⁺ indirgenir.','Cu²⁺ + 2e⁻ → Cu → katot kütlesi artar → I yanlış'),A('II’yi değerlendir','Zn yükseltgenir; Zn²⁺ katotta indirgenmez.','Zn → Zn²⁺ + 2e⁻ → [Zn²⁺] artar → II doğru'),A('III’ü değerlendir','Ag yükseltgenmediği için anot çamuru olur.','Ag çöker → III doğru')],
 puf='Arıtmada Cu’dan aktif safsızlık çözeltide kalır, Cu’dan az aktif olan çamur olur.')

# ============ 10 · Al–Fe E° ve katsayı · orta · öncüllü · tablo ============
kartla('10','Standart hücre potansiyeli ve katsayı','E° hücre = E°(katot) − E°(anot); yarı tepkime katsayısı ile çarpılsa da E° değişmez; aktarılan elektron sayısı katsayılardan bulunur.','Katsayı arttıkça E°’nin de arttığını sanmak; aktarılan elektron sayısını yanlış bulmak.','orta','öncüllü',4,'potansiyel','Standart hücre potansiyeli')
EAl,EFe10=D('-1.66'),D('-0.44'); E10=EFe10-EAl; assert E10==D('1.22')
n10=2*3; assert n10==6 and 3*2==6
I10=[True,False,True]
rows=[['Al³⁺ + 3e⁻ → Al','−1,66'],['Zn²⁺ + 2e⁻ → Zn','−0,76'],['Fe²⁺ + 2e⁻ → Fe','−0,44'],['Cu²⁺ + 2e⁻ → Cu','+0,34']]
SK=tablo_svg(['Yarı hücre tepkimesi','E° (V)'],rows)
q('0010',tipId='elk2-potansiyel',tip='Standart hücre potansiyeli',z='orta',alt='Elektrot Potansiyelleri',kaz='Standart elektrot potansiyellerinden hücre potansiyelini ve aktarılan elektron sayısını hesaplayıp katsayıyla ilişkisini yorumlar.',kalip='öncüllü',
 kart='K-AKELEK2-10 (E° ve katsayı) · Al–Fe hücresi, E° tablosu',sekil=SK,
 metin='25 °C’de standart koşullarda çalışan bir galvanik hücrede gerçekleşen tepkime aşağıda verilmiştir. Bazı yarı hücre tepkimelerinin standart indirgenme potansiyelleri tabloda verilmiştir.\n2Al(k) + 3Fe²⁺(suda) → 2Al³⁺(suda) + 3Fe(k)\nI. Standart hücre potansiyeli 1,22 V’tur.\nII. Tepkimenin tüm katsayıları 2 katına çıkarılırsa standart hücre potansiyeli 2,44 V olur.\nIII. Tepkimede toplam 6 mol elektron aktarılır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve III',sira=S5,yan=[('Yalnız I','III’ü yanlış saymış; 2 mol Al’nin her biri 3 elektron verdiği için aktarılan elektronun 6 mol olduğunu görmemiştir.','dikkat'),('Yalnız II','Yalnız II’yi doğru saymış; E°’nin katsayıyla çarpıldığını düşünmüştür. E° bir derişim ya da miktar değil, birim yük başına potansiyeldir ve değişmez.','bilgi'),('Yalnız III','Yalnız III’ü doğru bulmuş, I’i yanlış saymıştır; E° farkını −1,66 + (−0,44) = −2,10 V gibi toplayarak bulmuştur. Oysa E° = −0,44 − (−1,66) = 1,22 V’tur.','islem'),('I ve II','II’yi doğru saymış ve III’ü yanlış saymıştır; E°’nin katsayıyla orantılı olduğunu düşünmüş, elektron sayısını da hesaplayamamıştır.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Anot ve katodu E° değerlerinden belirle; katsayı değişince hangi büyüklüklerin değiştiğini ayır.'],
 bilgi=[B('E° ve katsayı','standart hücre potansiyeli E°(katot) − E°(anot) farkıdır; tepkime katsayılarla çarpılsa bile değişmez, çünkü potansiyel bir şiddet özelliğidir. Aktarılan elektron sayısı ise katsayılarla birlikte değişir. Örnek: Zn + Cu²⁺ tepkimesi 3 ile çarpılırsa E° aynı kalır, aktarılan elektron 2’den 6’ya çıkar')],
 ad=[A('Anot ve katodu bul','Al yükseltgenir, Fe²⁺ indirgenir.','Anot: Al · Katot: Fe'),A('I’i hesapla','E°(katot) − E°(anot).','−0,44 − (−1,66) = 1,22 V → I doğru'),A('II’yi değerlendir','E° katsayıdan bağımsızdır.','E° = 1,22 V kalır → II yanlış'),A('III’ü değerlendir','2 Al atomu, her biri 3 e⁻ verir.','2 × 3 = 6 mol e⁻ → III doğru')],
 puf='Katsayı değişince E° değişmez; aktarılan elektron sayısı değişir.')

# ---------- bitir ----------
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/elektroiki'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'elektroiki-1.json'),os.path.join(SC,'bos-elektroiki.json'))
tipler={}
for c in K.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Kimya (yalnız mantık), MEB 11–12. sınıf kimya.',kartlar=K.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akelektroiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
