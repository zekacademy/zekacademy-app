"""AYT Kimya · Kimya ve Elektrik · 20 soru, kardeş yok, ipucu 1. Şekil verileri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as K
from _hafif_kim2 import *
from cizim import tikz_svg
KONU_='Kimya ve Elektrik'; UK='akim|Kimya ve Elektrik'
K.KONU=KONU_
P=Parti('elektro',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM 2018–2026 AYT Kimya (yalnız mantık) · MEB 11–12. sınıf Kimya ve Elektrik'
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    kart(f'K-AKELEK-{n}',alt,fikir,tuzak,z,kalip,adim,f'el-{tipad}',tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
D=Fr
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
S_STD=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def f(x,n=3):
    """virgüllü ondalık metin"""
    return fm(x)

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
    """yatay üreteç: sol levha kısa (−), sağ levha uzun (+)"""
    return ('\\draw[thick] (%g,%g) -- (%g,%g);\\draw[line width=2pt] (%g,%g) -- (%g,%g);'%(wl,y,x-0.1,y,x-0.1,y-0.15,x-0.1,y+0.15)+
            '\\draw[line width=2pt] (%g,%g) -- (%g,%g);\\draw[thick] (%g,%g) -- (%g,%g);'%(x+0.1,y-0.3,x+0.1,y+0.3,x+0.1,y,wr,y)+
            '\\node[above left] at (%g,%g) {$-$};\\node[above right] at (%g,%g) {$+$};'%(x-0.1,y+0.1,x+0.1,y+0.1))
def beaker(bx,w,h,lvl,oy=0):
    return ('\\fill[vurgu!15] (%g,%g) rectangle (%g,%g);\\draw[thick] (%g,%g) -- (%g,%g) -- (%g,%g) -- (%g,%g);'%
            (bx,oy,bx+w,oy+lvl,bx,oy+h,bx,oy,bx+w,oy,bx+w,oy+h))
def elek(x,y0,y1):
    return '\\draw[thick,fill=gray!45] (%g,%g) rectangle (%g,%g);'%(x-0.14,y0,x+0.14,y1)

# ============ 01 · yükseltgenme basamağı toplamı · kolay ============
kartla('01','Yükseltgenme basamağı hesabı','Bileşikte yükseltgenme basamakları toplamı yüke eşittir; H +1, O çoğunlukla −2, peroksitte −1 alınır.','Peroksitte oksijeni −2 almak; çok atomlu iyonda atom sayısını (alt simgeyi) hesaba katmamak.','kolay','düz',3,'yukseltgenme','Yükseltgenme basamağı bulma')
mn=7; cr=D(12,2); nn=-3; oo=-1
assert mn-8==-1 and 2*cr-14==-2 and nn+4==1 and 2*1+2*oo==0
top=mn+cr+nn+oo; assert top==9
assert 7+6-3-2==8 and 7+6+3-1==15 and 4+6-3-1==6 and 7+6+3+1==17
q('0001',tipId='el-yukseltgenme',tip='Yükseltgenme basamağı bulma',z='kolay',alt='Yükseltgenme Basamağı',kaz='Bileşik ve iyonlarda belirtilen atomun yükseltgenme basamağını bulur.',kalip='düz',
 kart='K-AKELEK-01 (yükseltgenme basamağı toplamı) · dört taneciğin dört atomu',
 metin='Bir laboratuvarda öğrenciler, redoks tepkimelerinde sıkça kullanılan taneciklerdeki yükseltgenme basamaklarını karşılaştırmaktadır. İncelenen atomlar; MnO₄⁻ iyonundaki Mn, Cr₂O₇²⁻ iyonundaki Cr, NH₄⁺ iyonundaki N ve H₂O₂ bileşiğindeki O atomlarıdır.\n(Bileşiklerde H’nin yükseltgenme basamağı +1 alınacaktır.)\nBuna göre, bu dört atomun yükseltgenme basamaklarının toplamı kaçtır?',
 dogru=9,yan=[(8,'H₂O₂’deki oksijeni −2 almış; peroksitlerde oksijenin yükseltgenme basamağı −1’dir. Bu durumda 7 + 6 − 3 − 2 = 8 bulmuş.','bilgi'),(15,'NH₄⁺ iyonunda azotu +3 almış; iyonun +1 yükü ve dört H’nin +4’ü düşünüldüğünde azot −3 olmalıdır. Böylece 7 + 6 + 3 − 1 = 15 bulmuş.','islem'),(6,'MnO₄⁻ iyonunda Mn’yi MnO₂’deki gibi +4 almış; oysa dört oksijenin −8’i ve iyonun −1 yükü Mn’yi +7 yapar. Böylece 4 + 6 − 3 − 1 = 6 bulmuş.','bilgi'),(17,'Yükseltgenme basamaklarının işaretlerini hesaba katmayıp 7 + 6 + 3 + 1 = 17 bulmuş.','dikkat')],
 istenen='Dört atomun yükseltgenme basamakları toplamı.',ip=['Çok atomlu bir iyonda yükseltgenme basamaklarının toplamı iyonun yüküne eşittir; alt simgeleri hesaba kat.'],
 bilgi=[B('Yükseltgenme basamağı kuralları','bir tanecikte bütün atomların yükseltgenme basamakları toplamı taneciğin yüküne eşittir. Bileşiklerde H genellikle +1, O genellikle −2’dir; H₂O₂ gibi peroksitlerde O −1’dir. Örnek: SO₄²⁻ iyonunda S + 4(−2) = −2 olduğundan S = +6’dır')],
 ad=[A('Mn’yi bul','Dört O’nun toplamı −8, iyon yükü −1.','Mn + 4(−2) = −1 → Mn = +7'),A('Cr’yi bul','Alt simge 2 olduğundan iki Cr atomu vardır.','2Cr + 7(−2) = −2 → Cr = +6'),A('N ve O’yu bul','NH₄⁺ iyonunda dört H +4 verir; H₂O₂’de H +1 olduğundan O −1’dir.','N + 4(+1) = +1 → N = −3 · 2(+1) + 2O = 0 → O = −1'),A('Topla','Dört değer işaretleriyle toplanır.','+7 + 6 + (−3) + (−1) = +9')],
 puf='Önce iyonun yüküne bak, alt simgeyle çarp; peroksitte oksijen −1’dir.')

# ============ 02 · Fe2O3 + CO redoks · kolay · öncüllü ============
kartla('02','Redoks tepkimesinde yükseltgen–indirgen ve elektron alışverişi','İndirgenen madde yükseltgen, yükseltgenen madde indirgendir; alınan elektron sayısı yükseltgenme basamağı farkı ve atom sayısıyla bulunur.','İndirgenen maddeye “indirgen” demek; atom sayısını katmadan elektron saymak.','kolay','öncüllü',3,'yukseltgenme','Yükseltgenme basamağı bulma')
# Fe2O3 +3 -> Fe 0 (indirgenir, yükseltgen); C +2 -> +4; 1 mol Fe2O3: 2 Fe x 3 = 6 mol e-
assert 2*3==6 and 4-2==2
q('0002',tipId='el-yukseltgenme',tip='Yükseltgenme basamağı bulma',z='kolay',alt='Redoks Tepkimeleri',kaz='Redoks tepkimesinde yükseltgen, indirgen ve elektron alışverişini yükseltgenme basamağı değişimiyle belirler.',kalip='öncüllü',
 kart='K-AKELEK-02 (redoks yorumu) · yüksek fırında demir cevheri indirgenmesi',
 metin='Yüksek fırınlarda demir cevheri, karbon monoksit gazıyla aşağıdaki tepkimeye göre demire dönüştürülür.\nFe₂O₃(k) + 3CO(g) → 2Fe(k) + 3CO₂(g)\nI. Fe₂O₃ yükseltgen olarak davranmıştır.\nII. CO’daki karbonun yükseltgenme basamağı +2’den +4’e yükselmiştir.\nIII. 1 mol Fe₂O₃ tepkimeye girdiğinde 3 mol elektron alınmıştır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve II',sira=S_STD,yan=[('Yalnız I','II’yi doğru bulamamış; CO’daki karbonun yükseltgenme basamağını +2 olarak bulamayıp artışı fark etmemiş.','bilgi'),('Yalnız II','I’i yanlış saymış; Fe₂O₃’ün indirgendiğini görüp onu “indirgen” sanmış. İndirgenen madde diğerini yükseltgediği için yükseltgendir.','bilgi'),('I ve III','III’ü doğru saymış ve II’yi atlamış; elektron sayısını CO’nun katsayısı olan 3 ile karıştırmış, iki demir atomunun toplam 6 elektron aldığını görmemiş.','islem'),('I, II ve III','III’ü de doğru saymış; Fe₂O₃ formülündeki iki Fe atomunu hesaba katmayıp +3’ten 0’a tek atomun 3 elektron aldığını düşünmüş.','islem')],
 istenen='Doğru olan yargılar.',ip=['Tepkimede yükseltgenme basamağı değişen atomları bulup her birinin elektron alışverişini atom sayısıyla çarp.'],
 bilgi=[B('Yükseltgen ve indirgen','elektron alan (yükseltgenme basamağı azalan) madde indirgenir ve karşı maddeyi yükseltgediği için yükseltgendir. Elektron veren madde yükseltgenir ve indirgen olarak davranır. Örnek: Zn + Cu²⁺ → Zn²⁺ + Cu tepkimesinde Zn indirgen, Cu²⁺ yükseltgendir')],
 ad=[A('Basamakları yaz','Fe₂O₃’te O −2 olduğundan Fe +3’tür; CO’da C +2, CO₂’de +4’tür.','Fe: +3 → 0 · C: +2 → +4'),A('I’i değerlendir','Fe indirgenmiştir; indirgenen madde yükseltgendir.','I doğru'),A('II’yi değerlendir','Karbon elektron vermiştir.','II doğru: +2 → +4'),A('III’ü değerlendir','İki Fe atomu, her biri 3 elektron alır.','2 × 3 = 6 mol e⁻ → III yanlış'),A('Sonuç','I ve II doğrudur.','I ve II')],
 puf='Elektron alan indirgenir ve yükseltgen sayılır; elektron sayısını atom sayısıyla çarp.')

# ============ 03 · E° tablosu, istemli tepkime · kolay · öncüllü · tablo ============
kartla('03','Elektrot potansiyeli tablosundan istemlilik','E° değeri küçük olan metal yükseltgenir; E° değeri büyük olan metal iyonu indirgenir. Metal, kendinden E° değeri büyük iyonun çözeltisinde kendiliğinden çözünür.','Yönü ters yorumlamak; E° büyük olan metalin aktif sanılması.','kolay','öncüllü',4,'potansiyel','Elektrot potansiyeli ve istemlilik')
E={'Mg':D('-2.37'),'Zn':D('-0.76'),'Ni':D('-0.25'),'Cu':D('0.34'),'Ag':D('0.80')}
assert E['Ag']>E['Cu'] and not E['Zn']>E['Ni'] and E['Ni']>E['Mg']
rows=[['Mg²⁺ + 2e⁻ → Mg','−2,37'],['Zn²⁺ + 2e⁻ → Zn','−0,76'],['Ni²⁺ + 2e⁻ → Ni','−0,25'],['Cu²⁺ + 2e⁻ → Cu','+0,34'],['Ag⁺ + e⁻ → Ag','+0,80']]
SK=tablo_svg(['Yarı hücre tepkimesi','E° (V)'],rows)
q('0003',tipId='el-potansiyel',tip='Elektrot potansiyeli ve istemlilik',z='kolay',alt='Elektrot Potansiyelleri',kaz='Standart elektrot potansiyeli tablosundan metal–iyon tepkimelerinin istemliliğini yorumlar.',kalip='öncüllü',
 kart='K-AKELEK-03 (E° tablosu) · beş metalin indirgenme potansiyelleri',sekil=SK,
 metin='Bir öğrenci, 25 °C’de bazı yarı hücre tepkimelerinin standart indirgenme potansiyellerini tabloda göstermiştir. Ardından 1 M derişimli çözeltilerle aşağıdaki işlemleri gerçekleştirmeyi planlamaktadır.\nI. Cu(k) çubuğunu AgNO₃(suda) çözeltisine batırmak\nII. Ni(k) çubuğunu ZnSO₄(suda) çözeltisine batırmak\nIII. Mg(k) şeridini NiSO₄(suda) çözeltisine batırmak\nBuna göre bu işlemlerden hangilerinde standart koşullarda kendiliğinden tepkime gerçekleşir?',
 dogru='I ve III',sira=S_STD,yan=[('Yalnız I','III’ü gözden kaçırmış; Mg’nin E° değerinin Ni’den küçük olduğunu, dolayısıyla Mg’nin Ni²⁺ iyonlarını indirgeyebileceğini fark etmemiş.','dikkat'),('Yalnız II','Yönü ters yorumlamış: E° değeri büyük olan metalin, E° değeri küçük olan metal iyonunu indirgeyebileceğini düşünmüş.','bilgi'),('I ve II','II’de yönü ters yorumlamış (Ni’nin Zn²⁺’yı indirgeyeceğini sanmış) ve III’ü atlamıştır.','bilgi'),('I, II ve III','Her metal–iyon çiftinde tepkime olacağını sanmış; Ni’nin E° değerinin Zn’den büyük olduğunu, Zn²⁺’yı indirgeyemeyeceğini görmemiş.','dikkat')],
 istenen='Tepkimenin kendiliğinden gerçekleştiği işlemler.',ip=['Çubuk metalin E° değerini, çözeltideki iyonun E° değeriyle karşılaştır; hangisi elektron verebilir?'],
 bilgi=[B('İstemlilik ve E°','bir metal, E° değeri kendisinden büyük olan metalin iyonlarına elektron verebilir; yani küçük E°’lu metal yükseltgenir. Örnek: E°(Pb²⁺/Pb) = −0,13 V ve E°(Hg²⁺/Hg) = +0,85 V olduğundan Pb, Hg²⁺ çözeltisinde çözünür, Hg ise Pb²⁺ çözeltisinde çözünmez')],
 ad=[A('I’i değerlendir','Cu’nun E° değeri +0,34 V, Ag⁺’nın +0,80 V’tur.','Cu elektron verir, Ag⁺ alır → tepkime olur'),A('II’yi değerlendir','Ni’nin E° değeri −0,25 V, Zn²⁺’nın −0,76 V’tur.','Ni, Zn²⁺’ya elektron veremez → tepkime olmaz'),A('III’ü değerlendir','Mg’nin E° değeri −2,37 V, Ni²⁺’nın −0,25 V’tur.','Mg yükseltgenir, Ni²⁺ indirgenir → tepkime olur'),A('Sonuç','I ve III’te tepkime gerçekleşir.','I ve III')],
 puf='Metalin E° değeri çözeltideki iyonunkinden küçükse tepkime kendiliğinden olur.')

# ============ 04 · galvanik hücre, yanlış ifade · orta · şekil ============
kartla('04','Galvanik hücre yorumu','Küçük E°’lu elektrot anot (−), büyük E°’lu katot (+); elektronlar anottan katoda, anyonlar tuz köprüsünde anoda doğru akar.','Tuz köprüsünde iyon yönünü karıştırmak; Ehücre’yi E° toplamı almak.','orta','şekilli',4,'galvanik','Galvanik hücre yorumu')
assert D('0.80')-D('-0.44')==D('1.24')
SK=tk(pil(0,0.3,'1 M \\ce{Fe^{2+}}\\\\(suda)','1 M \\ce{Ag+}\\\\(suda)','Fe','Ag'))
S4=['Fe elektrot anottur ve kütlesi zamanla azalır.','Dış devrede elektronlar Fe elektrottan Ag elektroda doğru akar.','Standart hücre potansiyeli 1,24 V’tur.','Ag⁺ iyonlarının derişimi zamanla azalır.','Tuz köprüsündeki NO₃⁻ iyonları Ag⁺ çözeltisine doğru hareket eder.']
q('0004',tipId='el-galvanik',tip='Galvanik hücre yorumu',z='orta',alt='Elektrotlar ve Elektrokimyasal Hücreler',kaz='Galvanik hücrede anot–katot, elektron ve iyon akış yönlerini yorumlar.',kalip='şekilli',
 kart='K-AKELEK-04 (galvanik hücre) · Fe–Ag hücresi, KNO₃ tuz köprüsü',sekil=SK,
 metin='Bir öğrenci 25 °C’de, şekilde gösterilen düzeneği kullanarak 1 M derişimli çözeltilerle bir galvanik hücre hazırlamıştır. Tuz köprüsünde KNO₃(suda) bulunmaktadır; devre tamamlandığında hücre çalışmaya başlamıştır.\nFe²⁺(suda) + 2e⁻ → Fe(k)  E° = −0,44 V\nAg⁺(suda) + e⁻ → Ag(k)  E° = +0,80 V\nBuna göre bu hücreyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=S4[4],sira=S4,yan=[(S4[0],'Bu ifade doğrudur; öğrenci Fe’yi katot sanarak kütlesinin arttığını düşünmüş. Oysa E° değeri küçük olan Fe yükseltgenerek çözünür.','bilgi'),(S4[1],'Bu ifade doğrudur; öğrenci elektronların potansiyeli büyük elektrottan küçüğe aktığını düşünmüş. Elektronlar anot olan Fe’den katot olan Ag’ye akar.','bilgi'),(S4[2],'Bu ifade doğrudur; öğrenci 0,80 − 0,44 = 0,36 V bulmuş. Hücre potansiyeli E°(katot) − E°(anot) = 0,80 − (−0,44) = 1,24 V’tur.','islem'),(S4[3],'Bu ifade doğrudur; öğrenci Ag⁺ derişiminin arttığını sanmış. Katotta Ag⁺ + e⁻ → Ag tepkimesiyle Ag⁺ tükenir, derişimi azalır.','bilgi')],
 istenen='Yanlış olan ifade.',ip=['Önce anot ve katodu belirle; sonra tuz köprüsünün yük dengesini nasıl sağladığını düşün.'],
 bilgi=[B('Tuz köprüsü','tuz köprüsü iyonların akışıyla yarı hücrelerde yük dengesini sağlar. Anotta çözeltiye geçen katyonlar nedeniyle anyonlar anot yarı hücresine, katotta tükenen katyonlar nedeniyle katyonlar katot yarı hücresine doğru gider. Örnek: Zn–Cu hücresinde SO₄²⁻ iyonları Zn yarı hücresine yönelir')],
 ad=[A('Anot ve katodu bul','E° değeri küçük olan Fe anot, büyük olan Ag katottur.','Anot: Fe → Fe²⁺ + 2e⁻ · Katot: Ag⁺ + e⁻ → Ag'),A('Elektron yönü','Elektronlar anottan dış devreden katoda akar.','Fe → Ag'),A('Potansiyeli hesapla','E°hücre katot ile anot farkıdır.','0,80 − (−0,44) = 1,24 V'),A('Derişimler','Katotta Ag⁺ tükenir; anotta Fe²⁺ oluşur.','[Ag⁺] azalır, [Fe²⁺] artar'),A('Tuz köprüsü','Anyonlar anot yarı hücresine yönelir, yani Fe²⁺ çözeltisine.','NO₃⁻ Fe²⁺ çözeltisine gider → son ifade yanlış')],
 puf='Tuz köprüsünde anyonlar anoda, katyonlar katoda doğru hareket eder.')

# ============ 05 · SHE ile iki hücre · orta · şekil ============
kartla('05','Standart hidrojen elektrodu ile potansiyel bulma','SHE’nin E° değeri 0 V’tur; ölçülen hücre potansiyeli bilinmeyen elektrodun E° değerini verir (işaret anot–katot rolünden).','Elektrodun anot–katot rolüne bakmadan işaret vermek; iki hücre değerini çıkarmak.','orta','şekilli',4,'potansiyel','Elektrot potansiyeli ve istemlilik')
EX=D('0.34'); EY=D('-0.76')
assert 0+EX==D('0.34') and 0-EY==D('0.76') and EX-EY==D('1.10')
assert abs(EX-EY-D('1.10'))==0 and D('0.76')-D('0.34')==D('0.42') and (D('0.34')+D('0.76'))/2==D('0.55')
g=pil(0,6.3,'1 M \\ce{H+}\\\\ \\ce{H2}(g), 1 atm','1 M \\ce{X^{2+}}\\\\(suda)','Pt','X','0,34 V')
g+=pil(0,0.0,'1 M \\ce{H+}\\\\ \\ce{H2}(g), 1 atm','1 M \\ce{Y^{2+}}\\\\(suda)','Pt','Y','0,76 V')
g+='\\node[anchor=west] at (6.1,8.3) {I. hücre}; \\node[anchor=west] at (6.1,2.0) {II. hücre};'
SK=tk(g)
q('0005',tipId='el-potansiyel',tip='Elektrot potansiyeli ve istemlilik',z='orta',alt='Elektrot Potansiyelleri',kaz='Standart hidrojen elektroduyla ölçülen hücre potansiyellerinden elektrot potansiyellerini ve yeni hücre potansiyelini bulur.',kalip='şekilli',
 kart='K-AKELEK-05 (SHE ile potansiyel) · iki ayrı hücre, elektrot kütle değişimi',sekil=SK,
 metin='Bir araştırma laboratuvarında, standart hidrojen elektrodu (SHE) ile X ve Y metallerinden hazırlanan iki ayrı galvanik hücre kuruluyor. Her iki hücre de standart koşullardadır ve voltmetre değerleri şekilde verilmiştir. I. hücrede X elektrodunun kütlesinin zamanla arttığı, II. hücrede Y elektrodunun kütlesinin zamanla azaldığı gözlenmiştir. X ve Y, bileşiklerinde +2 yüklü katyon oluşturmaktadır.\nBuna göre X ve Y elektrotlarından oluşturulan galvanik hücrenin standart hücre potansiyeli kaç volttur?',
 dogru=D('1.10'),yan=[(D('0.34'),'Yalnız I. hücrenin potansiyelini almış; Y’nin E° değerinin −0,76 V olduğunu hücre potansiyeline katmamış.','dikkat'),(D('0.42'),'İki voltmetre değerinin farkını almış: 0,76 − 0,34 = 0,42 V. Oysa Y anot olduğundan E°(Y) = −0,76 V’tur ve hücre potansiyeli 0,34 − (−0,76) olur.','islem'),(D('0.55'),'İki voltmetre değerinin ortalamasını almış: (0,34 + 0,76) ÷ 2 = 0,55 V.','bilgi'),(D('0.76'),'Yalnız II. hücrenin potansiyelini almış; X’in E° değerinin +0,34 V olduğunu hücre potansiyeline katmamış.','dikkat')],
 istenen='X–Y galvanik hücresinin standart hücre potansiyeli (V).',ip=['Her hücrede kütlesi artan elektrodun katot, azalanın anot olduğunu kullanarak X ve Y’nin E° değerlerini ayrı ayrı bul.'],
 bilgi=[B('SHE','standart hidrojen elektrodunun potansiyeli tanım gereği 0 V’tur. Bir metal elektrot SHE ile eşleştirildiğinde ölçülen değer, o metalin E° değerinin büyüklüğüne eşittir; metal katot ise E° pozitif, anot ise E° negatiftir. Örnek: SHE ile birleştirilen bir metalin anot olduğu ve 0,50 V ölçüldüğü bir hücrede E° = −0,50 V’tur')],
 ad=[A('X’in E° değeri','Kütlesi artan X katottur; anot SHE’dir (0 V).','E°hücre = E°(X) − 0 = 0,34 → E°(X) = +0,34 V'),A('Y’nin E° değeri','Kütlesi azalan Y anottur; katot SHE’dir.','E°hücre = 0 − E°(Y) = 0,76 → E°(Y) = −0,76 V'),A('Roller','E° değeri büyük olan X katot, küçük olan Y anot olur.','Y(k) | Y²⁺ || X²⁺ | X(k)'),A('Hücre potansiyeli','Katot eksi anot.','0,34 − (−0,76) = 1,10 V')],
 puf='SHE ile ölçülen hücrede kütlesi artan elektrodun E° değeri pozitif, azalanınki negatiftir.')

# ============ 06 · CuCl2 elektrolizi · orta · öncüllü · şekil ============
kartla('06','Sulu CuCl₂ elektrolizi','Elektroliz hücresinde üretecin (−) kutbuna bağlı elektrot katottur; katotta indirgenme, anotta yükseltgenme olur.','Elektrolizde anot–katot işaretini galvanik hücre gibi düşünmek.','orta','öncüllü',4,'elektroliz','Elektroliz hücresi ve ürünler')
g=beaker(0,3.8,2.6,2.0)+elek(0.9,0.5,3.2)+elek(2.9,0.5,3.2)
g+='\\draw[thick] (0.9,3.2) -- (0.9,4.3) -- (1.55,4.3);\\draw[thick] (2.9,3.2) -- (2.9,4.3) -- (2.25,4.3);'+bat(1.9,4.3,1.55,2.25)
g+='\\node[right] at (1.05,0.8) {K};\\node[left] at (2.75,0.8) {L};\\node[below] at (1.9,-0.05) {\\ce{CuCl2}(suda), Pt elektrot};'
SK=tk(g)
q('0006',tipId='el-elektroliz',tip='Elektroliz hücresi ve ürünler',z='orta',alt='Elektroliz',kaz='Elektroliz hücresinde elektrotların rolünü ve tepkime ürünlerini üreteç bağlantısından belirler.',kalip='öncüllü',
 kart='K-AKELEK-06 (sulu CuCl₂) · inert elektrotlar, üreteç',sekil=SK,
 metin='Bir öğrenci, derişik CuCl₂ çözeltisini şekildeki düzenekle elektroliz etmektedir. K ve L elektrotları inert platinden yapılmıştır ve her ikisi de başlangıçta çözeltiye tamamen daldırılmıştır. Üretecin gerilimi elektrolizin başlaması için yeterlidir.\nI. K elektrotu katottur ve kütlesi zamanla artar.\nII. L elektrotunda Cu²⁺ iyonları indirgenir.\nIII. Elektroliz boyunca çözeltideki Cu²⁺ derişimi sabit kalır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='Yalnız I',sira=S_STD,yan=[('Yalnız II','I’i yanlış, II’yi doğru saymış; üretecin (−) kutbuna bağlı elektrodu anot sanıp indirgenmenin L’de olacağını düşünmüş.','bilgi'),('I ve II','Elektrolizde yalnız katotta indirgenme olduğunu atlayıp iki elektrodu da indirgenme yeri saymış.','bilgi'),('I ve III','III’ü doğru saymış; Cu²⁺ iyonları katotta Cu olarak biriktiği için derişimin azaldığını fark etmemiş.','dikkat'),('I, II ve III','Hem II’yi hem III’ü doğru sanmış; anotta Cl⁻ iyonlarının yükseltgendiğini ve Cu²⁺ derişiminin azaldığını görmemiş.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Üretecin hangi kutbuna bağlı olan elektrotta elektron fazlası bulunduğunu düşün; indirgenme orada olur.'],
 bilgi=[B('Elektroliz hücresi','elektroliz hücresinde üretecin (−) kutbuna bağlı elektrot katot, (+) kutbuna bağlı elektrot anottur. Katotta katyonlar indirgenir, anotta anyonlar yükseltgenir. Örnek: erimiş NaBr elektrolizinde katotta Na, anotta Br₂ oluşur')],
 ad=[A('Elektrotları belirle','K, üretecin (−) kutbuna; L, (+) kutbuna bağlıdır.','K: katot · L: anot'),A('I’i değerlendir','Katotta Cu²⁺ + 2e⁻ → Cu olur; elektrot kütlesi artar.','I doğru'),A('II’yi değerlendir','L anottur; orada Cl⁻ yükseltgenir, Cu²⁺ indirgenmez.','2Cl⁻ → Cl₂ + 2e⁻ → II yanlış'),A('III’ü değerlendir','Cu²⁺ katotta tükenir.','[Cu²⁺] azalır → III yanlış')],
 puf='Elektrolizde (−) kutba bağlı elektrot katottur; indirgenme orada olur.')

# ============ 07 · X–Y galvanik hücresi, kütle–zaman · orta · grafik ============
kartla('07','Elektrot kütle değişiminden mol kütlesi','Galvanik hücrede iki elektrotta aktarılan elektron mol sayısı eşittir; aynı yükte mol sayıları eşitlenir.','Kütle değişimini mol kütlesi sanmak; mol sayılarını farklı almak.','orta','grafik',4,'galvanik','Galvanik hücre yorumu')
mx=65; dx=D('6.5'); dy=D('6.4')
nxm=dx/mx; assert nxm==D('0.1'); MY=dy/nxm; assert MY==64
assert dy==D('6.4') and dy/D('0.05')==128 and mx*2==130
g='''\\begin{axis}[width=7cm,height=5.6cm,xmin=0,xmax=34,ymin=10,ymax=30,xtick={0,10,20,30},ytick={13.5,20,26.4},yticklabels={13{,}5,20,26{,}4},tick label style={font=\\small},axis lines=left,xlabel={Zaman (dakika)},ylabel={Elektrot kütlesi (g)},xlabel style={font=\\small},ylabel style={font=\\small},ymajorgrids,grid style={dotted,gray}]
\\addplot[thick,vurgu,mark=*,mark size=1.4pt] coordinates {(0,20) (10,17.8) (20,15.6) (30,13.5)};
\\addplot[thick,mark=square*,mark size=1.4pt] coordinates {(0,20) (10,22.1) (20,24.3) (30,26.4)};
\\node[anchor=south west] at (axis cs:2,13.7) {X};\\node[anchor=north west] at (axis cs:2,26.3) {Y};
\\end{axis}'''
SK=tk(g)
q('0007',tipId='el-galvanik',tip='Galvanik hücre yorumu',z='orta',alt='Elektrotlar ve Elektrokimyasal Hücreler',kaz='Galvanik hücrede elektrot kütle değişimlerinden bilinmeyen metalin mol kütlesini hesaplar.',kalip='grafik',
 kart='K-AKELEK-07 (kütle–zaman grafiği) · X–Y hücresi, mol kütlesi',sekil=SK,
 metin='X(k) elektrodu X²⁺ iyonları içeren çözeltiye, Y(k) elektrodu Y²⁺ iyonları içeren çözeltiye daldırılmış ve çözeltiler tuz köprüsüyle birleştirilerek bir galvanik hücre oluşturulmuştur. Hücre belirli bir süre çalıştırılırken elektrotların kütlelerindeki değişim grafikte gösterilmiştir. Çözeltilerin hacmi yeterince büyüktür ve elektrotlarda başka bir tepkime gerçekleşmemiştir.\nX’in mol kütlesi 65 g/mol olduğuna göre, Y’nin mol kütlesi kaç g/mol’dür?',
 dogru=64,yan=[(D('6.4'),'Y elektrodundaki kütle artışını (6,4 g) doğrudan mol kütlesi olarak yazmış.','dikkat'),(65,'İki elektrotta kütle değişimlerinin aynı olacağını sanıp Y’nin mol kütlesini X ile aynı almış; oysa kütle değişimleri farklıdır.','bilgi'),(128,'Y’nin mol sayısını yarıya indirip 0,05 mol bulmuş; 6,4 ÷ 0,05 = 128 g/mol hesaplamış.','islem'),(130,'X’in mol kütlesini 2 ile çarpmış: 65 × 2 = 130 g/mol.','bilgi')],
 istenen='Y’nin mol kütlesi (g/mol).',ip=['Her iki elektrotta aktarılan elektron sayısı eşit olduğundan X’in mol sayısı ile Y’nin mol sayısını ilişkilendir.'],
 bilgi=[B('Elektron aktarımı','galvanik hücrede anottan verilen elektron mol sayısı katotta alınan elektron mol sayısına eşittir. İyonların yükü eşitse tepkimeye giren ve oluşan metallerin mol sayıları da eşit olur. Örnek: Mg + Fe²⁺ → Mg²⁺ + Fe tepkimesinde 1 mol Mg çözünürken 1 mol Fe birikir')],
 ad=[A('Grafikten oku','X kütlesi 20 g’dan 13,5 g’a, Y kütlesi 20 g’dan 26,4 g’a değişmiştir.','X: −6,5 g; Y: +6,4 g'),A('X’in mol sayısı','Çözünen X kütlesini mol kütlesine böl.','6,5 ÷ 65 = 0,1 mol X'),A('Mol sayılarını eşitle','İki iyon da +2 yüklüdür; aynı elektron sayısı aktarılır.','n(Y) = n(X) = 0,1 mol'),A('Mol kütlesini bul','Biriken Y kütlesini mol sayısına böl.','6,4 ÷ 0,1 = 64 g/mol')],
 puf='İyon yükleri eşitse elektrotlardaki mol değişimleri de eşittir.')

# ============ 08 · Ag derişim pili · orta · şekil ============
kartla('08','Derişim pili potansiyeli','Derişim pilinde E° = 0’dır; E = (0,059/n)·log([seyreltik]/[derişik]) ile bulunur, seyreltik yarı hücre anottur.','Logaritmanın işaretini ve n’yi karıştırmak; derişimleri ters oranlamak.','orta','şekilli',4,'derisim','Derişim pili ve Nernst eşitliği')
E8=D('0.059')*2; assert E8==D('0.118')
assert D('0.059')==D('0.059')*1 and D('0.059')/2*1==D('0.0295') and -E8==D('-0.118') and D('0.059')*100==D('5.9')
g=pil(0,0.3,'0,01 M \\ce{Ag+}\\\\(suda)','1 M \\ce{Ag+}\\\\(suda)','Ag','Ag','?')
SK=tk(g)
q('0008',tipId='el-derisim',tip='Derişim pili ve Nernst eşitliği',z='orta',alt='Elektrot Potansiyelleri',kaz='Derişim pilinin hücre potansiyelini Nernst eşitliğiyle hesaplar.',kalip='şekilli',
 kart='K-AKELEK-08 (Ag derişim pili) · 0,01 M ve 1 M Ag⁺',sekil=SK,
 metin='Aynı metal elektrotlardan oluşan ve yalnız çözelti derişimleri farklı olan bir derişim pili, şekilde görüldüğü gibi 25 °C’de kurulmuştur. İki yarı hücre de aynı hacimde çözelti içerir ve devre tuz köprüsüyle tamamlanmıştır. Elektrokimyasal hücreler için Nernst eşitliği E = E° − (0,059/n)·logQ biçimindedir; burada n, hücre tepkimesinde aktarılan elektron sayısı, Q tepkime denklemindeki derişim oranıdır.\nBuna göre bu pilin başlangıçtaki hücre potansiyeli kaç volttur?',
 dogru=D('0.118'),yan=[(D('0.059'),'n’yi 2 alıp (0,059/2)·log100 = 0,059 V bulmuş; Ag⁺ + e⁻ → Ag olduğundan n = 1’dir.','bilgi'),(D('-0.118'),'Q oranını ters yazarak logaritmanın işaretini değiştirmiş; seyreltik yarı hücre anot olduğundan hücre potansiyeli pozitiftir.','islem'),(D('0.0295'),'Hem n değerini 2 almış hem de derişim oranını 10 sanmış: (0,059/2) × log10 = 0,0295 V.','islem'),(D('5.9'),'Logaritma almayı unutup 0,059 × 100 = 5,9 bulmuş.','islem')],
 istenen='Başlangıçtaki hücre potansiyeli (V).',ip=['Derişim pilinde iki elektrot aynı olduğundan E° değeri sıfırdır; Q oranını anot ve katot yarı hücre derişimleriyle yaz.'],
 bilgi=[B('Derişim pili','iki yarı hücrede aynı metal ve iyon bulunur, yalnız derişimler farklıdır. Seyreltik çözeltideki elektrot anot, derişik çözeltideki katottur; E° = 0 olduğundan potansiyeli yalnız derişim farkı belirler. Örnek: Zn elektrotlu 0,2 M ve 2 M çözeltilerden oluşan pilde (n = 2) potansiyel (0,059/2)·log10 = 0,0295 V’tur')],
 ad=[A('Tepkimeyi yaz','Anotta seyreltik taraf yükseltgenir, katotta derişik taraf indirgenir.','Anot: Ag → Ag⁺ + e⁻ · Katot: Ag⁺ + e⁻ → Ag · n = 1'),A('Q’yu yaz','Q = [anot Ag⁺] ÷ [katot Ag⁺].','Q = 0,01 ÷ 1 = 10⁻²'),A('E°’yi belirle','Aynı elektrotlarda E° = 0.','E° = 0 V'),A('Nernst','E = E° − (0,059/1) · logQ.','E = 0 − 0,059 × (−2) = 0,118 V')],
 puf='Derişim pilinde E° = 0’dır; seyreltik taraf anot olur ve potansiyel pozitif çıkar.')

# ============ 09 · Faraday: Cu kütlesi · orta ============
kartla('09','Faraday hesabı: katotta biriken kütle','Q = i·t; mol elektron = Q/96500; biriken mol = mol e⁻/n.','n yerine 1 almak; F sabitini yanlış kullanmak.','orta','hikâyeli',4,'faraday','Faraday yasaları hesabı')
i9,t9=D('9.65'),1000; Q9=i9*t9; ne9=Q9/96500; assert ne9==D('0.1'); m9=ne9/2*64; assert m9==D('3.2')
assert ne9*64==D('6.4') and ne9*2*64==D('12.8') and Q9/9650/2*64==32 and Q9/9650*64==64
q('0009',tipId='el-faraday',tip='Faraday yasaları hesabı',z='orta',alt='Elektroliz',kaz='Elektrolizde akım ve süreden katotta biriken madde kütlesini hesaplar.',kalip='hikâyeli',
 kart='K-AKELEK-09 (Cu kaplama) · akım ve süreden kütle',
 metin='Bir öğrenci, bakır kaplama deneyinde CuSO₄ çözeltisine daldırdığı platin elektrotları üretece bağlamıştır. Çözeltide Cu²⁺ iyonları fazlasıyla bulunmakta ve katotta yalnız Cu metali toplanmaktadır. Devreden 1000 saniye boyunca sabit 9,65 A’lık akım geçirilmiştir.\n(Cu = 64 g/mol; 1 mol elektronun yükü = 96500 C)\nBuna göre katotta toplanan bakırın kütlesi kaç gramdır?',
 dogru=D('3.2'),yan=[(D('6.4'),'Cu²⁺ iyonunun yükünü 1 almış; 0,1 mol elektrondan 0,1 mol Cu elde edilip 6,4 g bulunmuştur. Oysa 1 mol Cu için 2 mol elektron gerekir.','bilgi'),(D('12.8'),'Elektron mol sayısını (0,1) 2 ile çarpıp 0,2 mol Cu bulmuş; 2 yerine bölmesi gerekirdi.','islem'),(32,'Yükü 96500 yerine 9650 C/mol ile bölmüş: 9650 ÷ 9650 = 1 mol elektron, 0,5 mol Cu, 32 g.','islem'),(64,'Hem 9650 C/mol kullanmış hem de Cu²⁺ yükünü 1 almış; 1 mol Cu, yani 64 g bulmuş.','islem')],
 istenen='Katotta toplanan bakırın kütlesi (g).',ip=['Önce geçen yükü bul, sonra yükten mol elektron sayısına, oradan Cu mol sayısına geç.'],
 bilgi=[B('Faraday hesabı','geçen yük Q = i·t’dir. 96500 C, 1 mol elektronun yüküdür. Katotta M+ⁿ + ne⁻ → M tepkimesinde biriken madde mol sayısı, elektron mol sayısının n’ye bölünmesiyle bulunur. Örnek: 1 A akım 965 s geçerse 965 C, yani 0,01 mol elektron geçmiştir')],
 ad=[A('Yükü bul','Q = i × t.','Q = 9,65 × 1000 = 9650 C'),A('Elektron mol sayısı','Yükü 96500’e böl.','9650 ÷ 96500 = 0,1 mol e⁻'),A('Cu mol sayısı','Cu²⁺ + 2e⁻ → Cu olduğundan elektron sayısı 2’ye bölünür.','0,1 ÷ 2 = 0,05 mol Cu'),A('Kütleyi bul','Mol sayısı mol kütlesiyle çarpılır.','0,05 × 64 = 3,2 g')],
 puf='Önce Q = i·t, sonra mol e⁻ = Q/96500, sonra katsayıyla mol madde.')

# ============ 10 · korozyon · orta · şekil · yanlış öncül ============
kartla('10','Korozyon ve katodik koruma','Demirden daha aktif metalle temas eden demir korunur (kurban anot); daha az aktif metalle temas eden demir daha hızlı paslanır.','Demirle temastaki metalin rolünü karıştırmak; korozyon hızı sıralamasını ters yazmak.','orta','şekilli',3,'korozyon','Korozyon ve korunma')
Ee={'Mg':D('-2.37'),'Fe':D('-0.44'),'Cu':D('0.34')}
assert Ee['Mg']<Ee['Fe']<Ee['Cu']
def civi(bx,sarg):
    s=beaker(bx,1.9,2.6,2.0)+'\\draw[line width=3pt,gray!70] (%g,%g) -- (%g,%g);'%(bx+0.7,2.9,bx+0.7,0.3)
    if sarg:
        s+='\\draw[thick,fill=white] (%g,%g) rectangle (%g,%g);'%(bx+0.52,0.7,bx+0.88,1.8)
        s+='\\node[right] at (%g,%g) {%s};'%(bx+0.95,1.25,sarg)
    return s
g=civi(0,'Mg')+civi(2.6,'Cu')+civi(5.2,'')
g+=''.join('\\node[below] at (%g,-0.05) {%s};'%(x+0.95,n) for x,n in [(0,'1. kap'),(2.6,'2. kap'),(5.2,'3. kap')])
g+='\\node[below] at (3.5,-0.6) {Üç kapta da \\ce{NaCl}(suda)};'
SK=tk(g)
q('0010',tipId='el-korozyon',tip='Korozyon ve korunma',z='orta',alt='Korozyon',kaz='Demirin başka metallerle temasında korozyon yönünü ve hızını E° değerlerine göre yorumlar.',kalip='şekilli',
 kart='K-AKELEK-10 (üç çivi) · Mg, Cu sargılı ve tek çivi',sekil=SK,
 metin='Bir öğrenci, özdeş üç demir çiviyi şekilde görüldüğü gibi aynı derişimli NaCl çözeltilerine daldırmıştır. 1. ve 2. kaptaki çivilerin gövdesine sırasıyla Mg şerit ve Cu tel sıkıca sarılmış, 3. kaptaki çivi yalnız bırakılmıştır. Öğrenci bir süre sonra çivilerin korozyon durumunu karşılaştıracaktır.\nMg²⁺ + 2e⁻ → Mg  E° = −2,37 V\nFe²⁺ + 2e⁻ → Fe  E° = −0,44 V\nCu²⁺ + 2e⁻ → Cu  E° = +0,34 V\nI. 1. kaptaki çivide Fe anot olarak davranır.\nII. 2. kaptaki çivide Cu katot olarak davranır ve Fe’nin yükseltgenmesi hızlanır.\nIII. Korozyon hızı 3. kapta 2. kaptakinden büyüktür.\nBuna göre bu yargılardan hangileri yanlıştır?',
 dogru='I ve III',sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],yan=[('Yalnız I','III’ü doğru saymış; Cu ile temasın Fe’yi koruduğunu düşünerek 3. kaptaki korozyonu 2. kaptakinden hızlı bulmuş.','bilgi'),('Yalnız II','II’yi yanlış saymış; Cu’nun E° değerinin Fe’den büyük olduğunu, dolayısıyla Cu’nun katot olup Fe’nin çözünmesini hızlandırdığını görmemiş.','bilgi'),('I ve II','II’yi de yanlış saymış ve III’ü doğru bulmuş; Cu’nun yaptığı etkiyi tersine yorumlamış.','bilgi'),('II ve III','I’i doğru saymış; Mg ile temasta Fe’nin anot olduğunu düşünmüş, oysa daha aktif Mg anot olur ve Fe korunur.','bilgi')],
 istenen='Yanlış olan yargılar.',ip=['Çivinin temas ettiği metalin E° değerini Fe ile karşılaştır; daha küçük E°’lu metal anot olur.'],
 bilgi=[B('Katodik koruma','demirden daha küçük E° değerine sahip bir metalle (Zn, Mg gibi) temas eden demir katot olur ve paslanmaz; bu metal kurban anot olarak çözünür. Demirden büyük E° değerli metalle temasta ise demir anot olur ve daha hızlı korozyona uğrar. Örnek: çinko kaplı (galvanizli) saç')],
 ad=[A('I’i değerlendir','Mg’nin E° değeri Fe’den küçüktür; Mg anot, Fe katot olur.','Fe anot değildir → I yanlış'),A('II’yi değerlendir','Cu’nun E° değeri Fe’den büyüktür; Fe anot, Cu katot olur ve Fe daha hızlı çözünür.','II doğru'),A('III’ü değerlendir','2. kapta Fe, Cu ile temas ettiğinden 3. kaptaki yalnız çividen daha hızlı korozyona uğrar.','Hız: 2. kap > 3. kap → III yanlış'),A('Sonuç','Yanlış olanlar I ve III’tür.','I ve III')],
 puf='Demirle temas eden metal Fe’den daha aktifse demir korunur; daha az aktifse korozyon hızlanır.')

# ============ 11 · E° tablosu, en küçük hücre potansiyeli · orta · tablo ============
kartla('11','Hücre potansiyeli karşılaştırması','E°hücre = E°(katot) − E°(anot); E° farkı en küçük olan pil en düşük potansiyeli verir.','Farkı mutlak almayı unutmak; anot–katodu karıştırıp negatif bulmak.','orta','tablo',3,'potansiyel','Elektrot potansiyeli ve istemlilik')
E2={'Al':D('-1.66'),'Fe':D('-0.44'),'Sn':D('-0.14'),'Cu':D('0.34'),'Hg':D('0.85')}
pair={'AlFe':E2['Fe']-E2['Al'],'FeSn':E2['Sn']-E2['Fe'],'SnCu':E2['Cu']-E2['Sn'],'FeCu':E2['Cu']-E2['Fe'],'CuHg':E2['Hg']-E2['Cu']}
assert pair=={'AlFe':D('1.22'),'FeSn':D('0.30'),'SnCu':D('0.48'),'FeCu':D('0.78'),'CuHg':D('0.51')}
assert min(pair,key=pair.get)=='FeSn' and len(set(pair.values()))==5
rows11=[['Al³⁺ + 3e⁻ → Al','−1,66'],['Fe²⁺ + 2e⁻ → Fe','−0,44'],['Sn²⁺ + 2e⁻ → Sn','−0,14'],['Cu²⁺ + 2e⁻ → Cu','+0,34'],['Hg²⁺ + 2e⁻ → Hg','+0,85']]
SK=tablo_svg(['Yarı hücre tepkimesi','E° (V)'],rows11)
S11=['Sn(k) | Sn²⁺(suda) || Cu²⁺(suda) | Cu(k)','Fe(k) | Fe²⁺(suda) || Sn²⁺(suda) | Sn(k)','Fe(k) | Fe²⁺(suda) || Cu²⁺(suda) | Cu(k)','Al(k) | Al³⁺(suda) || Fe²⁺(suda) | Fe(k)','Cu(k) | Cu²⁺(suda) || Hg²⁺(suda) | Hg(k)']
q('0011',tipId='el-potansiyel',tip='Elektrot potansiyeli ve istemlilik',z='orta',alt='Elektrot Potansiyelleri',kaz='Standart elektrot potansiyellerinden galvanik hücrelerin standart hücre potansiyellerini hesaplayıp karşılaştırır.',kalip='tablo',
 kart='K-AKELEK-11 (hücre potansiyeli karşılaştırma) · beş hücre gösterimi',sekil=SK,
 metin='Bir laboratuvarda 25 °C’de, standart indirgenme potansiyelleri tabloda verilen yarı hücrelerden ikişer tanesi seçilip tuz köprüsüyle birleştirilerek galvanik hücreler hazırlanacaktır. Her hücrede çözeltilerin derişimi 1 M’dir ve hücreler gösterimde sol taraftaki elektrot anot olacak biçimde yazılmıştır.\nBuna göre aşağıdaki hücrelerden hangisinin standart hücre potansiyeli en küçüktür?',
 dogru=S11[1],sira=S11,yan=[(S11[0],'Sn–Cu hücresini seçmiş; E° farkı 0,34 − (−0,14) = 0,48 V’tur, Fe–Sn hücresinin 0,30 V’undan büyüktür.','islem'),(S11[2],'Fe–Cu hücresini seçmiş; E° farkı 0,34 − (−0,44) = 0,78 V’tur, Fe–Sn hücresinin 0,30 V’undan büyüktür.','islem'),(S11[3],'E°(anot) − E°(katot) farkını alıp işareti yok saymış; Al–Fe hücresinde |−1,66 − (−0,44)| = 1,22 V bulmuş, bunu yanlışlıkla en küçük sanmıştır. Oysa diğer hücrelerden büyüktür.','dikkat'),(S11[4],'Cu–Hg hücresini seçmiş; E° farkı 0,85 − 0,34 = 0,51 V’tur, Fe–Sn hücresinin 0,30 V’undan büyüktür.','islem')],
 istenen='Standart hücre potansiyeli en küçük olan hücre.',ip=['Her hücre için katodun E° değerinden anodunkini çıkararak beş değeri karşılaştır.'],
 bilgi=[B('Standart hücre potansiyeli','E°hücre = E°katot − E°anot’tur; iki E° değeri arasındaki fark ne kadar küçükse pil o kadar düşük gerilim verir. Örnek: E° = −0,13 V olan Pb ile E° = +0,80 V olan Ag’den oluşan hücrede 0,80 − (−0,13) = 0,93 V elde edilir')],
 ad=[A('Her hücreyi hesapla','Sağdaki yarı hücre katot, soldaki anottur.','Al–Fe: 1,22 V; Sn–Cu: 0,48 V; Fe–Cu: 0,78 V; Cu–Hg: 0,51 V'),A('Fe–Sn hücresi','Katot Sn²⁺/Sn (−0,14), anot Fe²⁺/Fe (−0,44).','−0,14 − (−0,44) = 0,30 V'),A('Karşılaştır','Beş değerin en küçüğü seçilir.','0,30 < 0,48 < 0,51 < 0,78 < 1,22'),A('Sonuç','En küçük potansiyel Fe–Sn hücresindedir.','Fe | Fe²⁺ || Sn²⁺ | Sn')],
 puf='Hücre potansiyeli, iki elektrodun E° farkıdır; farkı küçük olan pil daha düşük gerilim verir.')

# ============ 12 · CuSO4 elektrolizi, pH · zor ============
kartla('12','Elektroliz ve çözelti pH değişimi','İnert elektrotlu CuSO₄ elektrolizinde anotta su yükseltgenir (4 mol e⁻ başına 4 mol H⁺ oluşur); H⁺ mol sayısı elektron mol sayısına eşittir.','Anotta H⁺ yerine OH⁻ oluştuğunu sanmak; n’yi atlamak.','zor','hikâyeli',5,'faraday','Faraday yasaları hesabı')
i12,t12=2,9650; Q12=i12*t12; ne12=D(Q12,96500); assert ne12==D('0.2')
hmol=ne12  # 2H2O -> O2 + 4H+ + 4e-
V12=2; assert hmol/V12==D('0.1')
import math
assert round(-math.log10(hmol/V12))==1
assert D(Q12,9650)/V12==1 and D(1930,96500)/V12==D('0.01') and 14-1==13
q('0012',tipId='el-faraday',tip='Faraday yasaları hesabı',z='zor',alt='Elektroliz',kaz='İnert elektrotlu CuSO₄ elektrolizinde geçen yükten oluşan H⁺ miktarını ve çözeltinin pH değerini hesaplar.',kalip='hikâyeli',
 kart='K-AKELEK-12 (CuSO₄ elektrolizi, pH) · anotta su yükseltgenmesi',
 metin='Bir laboratuvarda 2 L hacimli, 0,5 M CuSO₄ sulu çözeltisi platin elektrotlar kullanılarak 25 °C’de elektroliz edilmektedir. Sabit 2 A’lık akım 9650 saniye boyunca geçirilmiştir. Katotta yalnız Cu metali, anotta ise yalnız O₂ gazı oluşmuştur. Çözeltinin başlangıçtaki pH değeri ve suyun iyonlaşmasından gelen H⁺ iyonları ile hacim değişimi ihmal edilecektir.\n(1 mol elektronun yükü = 96500 C)\nBuna göre elektroliz sonunda çözeltinin pH değeri kaçtır?',
 dogru=1,yan=[(0,'Geçen yükü 96500 C ile değil 9650 C ile bölüp 2 mol elektron, 2 mol H⁺ bulmuş; [H⁺] = 1 M, pH = 0 hesaplamıştır.','islem'),(2,'Geçen yükü 1930 C hesaplayıp 0,02 mol elektron bulmuş; [H⁺] = 0,02 ÷ 2 = 0,01 M, pH = 2 olarak yazmıştır.','islem'),(7,'CuSO₄’ın nötr bir tuz olduğunu düşünerek elektrolizin pH’ı değiştirmeyeceğini sanmıştır.','bilgi'),(13,'Anotta OH⁻ iyonlarının oluştuğunu sanmış: [OH⁻] = 0,1 M, pOH = 1, pH = 14 − 1 = 13 hesaplamıştır.','bilgi')],
 istenen='Elektroliz sonundaki pH değeri.',ip=['Anotta oluşan ürünün yanında çözeltiye hangi iyonun geçtiğini yaz; elektron sayısını bu iyonun mol sayısıyla ilişkilendir.'],
 bilgi=[B('Elektrolizde pH değişimi','inert elektrotlarla derişik oksijenli asit tuzlarının çözeltisinde anotta su yükseltgenir: 2H₂O → O₂ + 4H⁺ + 4e⁻. Çözeltiye geçen H⁺ mol sayısı, devreden geçen elektron mol sayısına eşittir ve pH = −log[H⁺] ile bulunur. Örnek: 0,05 mol elektron geçen 5 L çözeltide [H⁺] = 0,01 M, pH = 2’dir')],
 ad=[A('Yükü bul','Q = i × t.','Q = 2 × 9650 = 19300 C'),A('Elektron mol sayısı','Yük, 96500 C/mol’e bölünür.','19300 ÷ 96500 = 0,2 mol e⁻'),A('Anot tepkimesi','Anotta su yükseltgenir; 4 mol e⁻ başına 4 mol H⁺ oluşur.','2H₂O → O₂ + 4H⁺ + 4e⁻ → n(H⁺) = 0,2 mol'),A('Derişim','Hacim 2 L’dir.','[H⁺] = 0,2 ÷ 2 = 0,1 M'),A('pH değeri','pH = −log[H⁺].','pH = −log 10⁻¹ = 1')],
 puf='CuSO₄ elektrolizinde oluşan H⁺ mol sayısı, geçen elektron mol sayısına eşittir.')

# ============ 13 · Nernst öncüllü · zor ============
kartla('13','Nernst eşitliği ile derişim etkisi','E = E° − (0,059/n)·log([ürün]/[girenler]); ürün derişimi artarsa E azalır, giren derişimi artarsa E artar.','log işaretini ters kullanmak; 10 kat artışın (0,059/n) kadar etki ettiğini unutmak.','zor','öncüllü',5,'derisim','Derişim pili ve Nernst eşitliği')
E0=D('1.10'); k=D('0.059')/2
def Eh(zn,cu): return E0-k*zn_cu_log(zn,cu)
def zn_cu_log(zn,cu):
    r=D(zn)/D(cu); l=0
    while r>1: r/=10; l+=1
    while r<1: r*=10; l-=1
    assert r==1; return l
assert Eh('0.001','0.1')==D('1.159')>E0
assert Eh('0.1','0.1')==E0
assert Eh('0.001','1')-Eh('0.001','0.1')==D('0.0295') and Eh('0.001','1')-Eh('0.001','0.1')!=D('0.059')
q('0013',tipId='el-derisim',tip='Derişim pili ve Nernst eşitliği',z='zor',alt='Elektrot Potansiyelleri',kaz='Nernst eşitliğini kullanarak derişim değişiminin hücre potansiyeline etkisini yorumlar.',kalip='öncüllü',
 kart='K-AKELEK-13 (Nernst, Zn–Cu hücresi) · derişim değişimleri',
 metin='25 °C’de Zn(k) | Zn²⁺(suda) || Cu²⁺(suda) | Cu(k) hücresi, [Zn²⁺] = 0,001 M ve [Cu²⁺] = 0,1 M olacak biçimde hazırlanmıştır. Hücre tepkimesi Zn(k) + Cu²⁺(suda) → Zn²⁺(suda) + Cu(k) için standart hücre potansiyeli 1,10 V’tur. Nernst eşitliğinde logaritmik terimin katsayısı 0,059/n alınacaktır; burada n, tepkimede aktarılan elektron sayısıdır.\nI. Bu hücrenin potansiyeli 1,10 V’tan büyüktür.\nII. Zn²⁺ derişimi 0,1 M’a çıkarılırsa hücre potansiyeli 1,10 V olur.\nIII. Cu²⁺ derişimi 10 katına çıkarılırsa hücre potansiyeli 0,059 V artar.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve II',sira=S_STD,yan=[('Yalnız I','II’yi yanlış saymış; derişimler eşit olduğunda Q = 1 ve logQ = 0 olduğundan potansiyelin E°’ye eşit olacağını fark etmemiş.','bilgi'),('Yalnız II','I’i yanlış saymış; Q = 0,01 olduğunda logQ negatif olur ve −(0,059/2)·logQ terimi pozitif katkı yapar, potansiyel 1,10 V’tan büyük çıkar.','islem'),('I ve III','III’ü doğru bulmuş; n = 2 olduğunu unutup logaritmik terimin katsayısını 0,059 almış, 10 katlık artışta 0,0295 V artış olduğunu görmemiştir.','islem'),('I, II ve III','III’ü de doğru bulmuş; 10 kat artışın etkisini 0,059 V sanmış, n = 2 olduğundan gerçek artışın 0,0295 V olduğunu hesaplamamıştır.','islem')],
 istenen='Doğru olan yargılar.',ip=['Q = [Zn²⁺]/[Cu²⁺] değerini her yargı için ayrı hesapla ve logaritmasının işaretine dikkat et.'],
 bilgi=[B('Nernst eşitliği','25 °C’de E = E° − (0,059/n)·logQ’dur; Q, ürün derişimlerinin giren derişimlerine oranıdır (katılar yazılmaz). Q < 1 ise E > E°, Q = 1 ise E = E°, Q > 1 ise E < E°’dir. Örnek: n = 2 için Q 10 kat küçülürse potansiyel 0,0295 V artar')],
 ad=[A('Q’yu yaz','Q = [Zn²⁺] ÷ [Cu²⁺].','Q = 0,001 ÷ 0,1 = 10⁻²'),A('I’i hesapla','n = 2 için E = 1,10 − 0,0295 × (−2).','E = 1,10 + 0,059 = 1,159 V > 1,10 → I doğru'),A('II’yi hesapla','Zn²⁺ = 0,1 M olunca Q = 1.','log1 = 0 → E = 1,10 V → II doğru'),A('III’ü hesapla','Cu²⁺ 10 kat artarsa Q 10 kat küçülür; logQ bir birim azalır.','ΔE = +0,0295 V ≠ 0,059 V → III yanlış'),A('Sonuç','I ve II doğrudur.','I ve II')],
 puf='n = 2 iken Q’daki 10 katlık değişim potansiyeli 0,0295 V değiştirir.')

# ============ 14 · seri bağlı elektroliz · zor · şekil ============
kartla('14','Seri bağlı elektroliz kapları','Seri devrede her kaptan aynı elektron mol sayısı geçer; ürün miktarları elektron mol sayısı ve iyon yüküyle bulunur.','Elektron sayısını aynı alıp iyon yüklerini atlamak; sulu çözeltide anot ürününü yanlış seçmek.','zor','şekilli',5,'faraday','Faraday yasaları hesabı')
nAl=D('5.4')/27; ne14=nAl*3; assert nAl==D('0.2') and ne14==D('0.6')
mCu=ne14/2*64; vO2=ne14/4*D('22.4'); assert mCu==D('19.2') and vO2==D('3.36')
e1=nAl; assert e1/2*64==D('6.4') and e1/4*D('22.4')==D('1.12')       # n(e-) = n(Al) alınırsa
assert ne14*64==D('38.4')                                             # Cu n=1
assert (nAl*2)/2*64==D('12.8') and (nAl*2)/4*D('22.4')==D('2.24')   # Al yükü 2 alınırsa
assert D('19.2')==mCu and ne14/2*D('22.4')==D('6.72')                 # gaz 2e- alınırsa
g=beaker(0,2.4,2.6,2.0)+beaker(3.6,2.4,2.6,2.0)+elek(0.6,0.4,3.0)+elek(1.8,0.4,3.0)+elek(4.2,0.4,3.0)+elek(5.4,0.4,3.0)
g+='\\draw[thick] (0.6,3.0) -- (0.6,5.0) -- (2.6,5.0);\\draw[thick] (5.4,3.0) -- (5.4,5.0) -- (3.4,5.0);\\draw[thick] (1.8,3.0) -- (1.8,3.9) -- (4.2,3.9) -- (4.2,3.0);'+bat(3.0,5.0,2.6,3.4)
g+='\\node[below,align=center] at (1.2,-0.05) {1. kap\\\\erimiş \\ce{Al2O3}\\\\(kriyolitli)\\\\katotta 5,4 g Al};\\node[below,align=center] at (4.8,-0.05) {2. kap\\\\\\ce{CuSO4}(suda)};'
SK=tk(g)
ops14=['19,2 g – 3,36 L','6,4 g – 1,12 L','38,4 g – 3,36 L','19,2 g – 6,72 L','12,8 g – 2,24 L']
q('0014',tipId='el-faraday',tip='Faraday yasaları hesabı',z='zor',alt='Elektroliz',kaz='Seri bağlı elektroliz kaplarında geçen elektron miktarından ürün kütle ve hacimlerini hesaplar.',kalip='şekilli',
 kart='K-AKELEK-14 (seri bağlı iki kap) · erimiş Al₂O₃ ve sulu CuSO₄',sekil=SK,
 metin='Şekildeki düzenekte, platin elektrotlu iki elektroliz kabı üretece seri bağlanmıştır. 1. kapta kriyolit içeren erimiş Al₂O₃, 2. kapta yeterince derişik CuSO₄ sulu çözeltisi bulunmaktadır. Elektroliz sırasında 1. kaptaki katotta toplanan Al kütlesi şekilde verilmiştir. 2. kapta katotta yalnız Cu metali, anotta yalnız O₂ gazı oluşmuştur.\n(Al = 27 g/mol; Cu = 64 g/mol; NŞA’da 1 mol gaz 22,4 L hacim kaplar)\nBuna göre aynı sürede 2. kaptaki katotta toplanan Cu kütlesi ile anotta oluşan O₂ gazının NŞA’daki hacmi sırasıyla aşağıdakilerden hangisidir?',
 dogru=ops14[0],sira=ops14,yan=[(ops14[1],'Elektron mol sayısını Al mol sayısına (0,2) eşit almış; Al³⁺ iyonunun 3 yükünü hesaba katmamış. Bu durumda 0,1 mol Cu (6,4 g) ve 0,05 mol O₂ (1,12 L) bulmuştur.','bilgi'),(ops14[2],'Cu²⁺ iyonunun yükünü 1 almış; 0,6 mol elektronla 0,6 mol Cu (38,4 g) bulmuş, O₂ hacmini doğru hesaplamıştır.','bilgi'),(ops14[3],'Cu kütlesini doğru bulmuş ama anotta 1 mol O₂ için 2 mol elektron gerektiğini sanmış; 0,3 mol O₂, yani 6,72 L hesaplamıştır.','bilgi'),(ops14[4],'Al³⁺ iyonunun yükünü 2 almış; 0,4 mol elektronla 0,2 mol Cu (12,8 g) ve 0,1 mol O₂ (2,24 L) bulmuştur.','bilgi')],
 istenen='2. kapta katotta biriken Cu kütlesi ve anotta oluşan O₂ hacmi.',ip=['Seri bağlı kaplardan geçen elektron mol sayısı aynıdır; bunu önce 1. kaptan hesapla.'],
 bilgi=[B('Seri bağlı kaplar','seri devrede her elektrolit kabından aynı yük, yani aynı mol sayısında elektron geçer. Bir kaptan hesaplanan elektron mol sayısı, diğer kaptaki ürün miktarını bulmak için kullanılır. Sulu CuSO₄ elektrolizinde anotta su yükseltgenir: 2H₂O → O₂ + 4H⁺ + 4e⁻. Örnek: 0,4 mol elektron geçen bir kapta 0,1 mol O₂ oluşur')],
 ad=[A('Al mol sayısı','Katotta toplanan Al kütlesi mol kütlesine bölünür.','5,4 ÷ 27 = 0,2 mol Al'),A('Elektron sayısı','Al³⁺ + 3e⁻ → Al olduğundan her mol Al için 3 mol elektron gerekir.','0,2 × 3 = 0,6 mol e⁻'),A('Cu kütlesi','Cu²⁺ + 2e⁻ → Cu; aynı 0,6 mol elektron geçer.','0,6 ÷ 2 = 0,3 mol Cu → 0,3 × 64 = 19,2 g'),A('O₂ hacmi','4 mol elektron başına 1 mol O₂ oluşur.','0,6 ÷ 4 = 0,15 mol O₂'),A('Hacmi bul','NŞA’da 1 mol gaz 22,4 L’dir.','0,15 × 22,4 = 3,36 L')],
 puf='Seri devrede önce bir kaptan elektron mol sayısını bul, diğer kaptaki ürünü o sayıdan hesapla.')

# ============ 15 · metal–çözelti tablosu · zor · öncüllü · tablo ============
kartla('15','Metal–çözelti tablosundan aktiflik ve pil','Metal, kendinden daha az aktif metalin iyonunu çözeltisinde indirger; tablodan aktiflik sırası çıkarılır.','Tablodaki “var/yok”ları ters yorumlamak; hücre gösteriminde anot–katot yönünü karıştırmak.','zor','öncüllü',5,'potansiyel','Elektrot potansiyeli ve istemlilik')
act={'Y':3,'X':2,'Z':1}
def tep(m,ion): return act[m]>act[ion]   # metal m, ion ion²⁺ çözeltisinde tepkime olur mu
assert tep('Y','X') and tep('Y','Z') and tep('X','Z') and not tep('X','Y') and not tep('Z','X') and not tep('Z','Y')
def ev(a,k): return act[a]>act[k]    # a anot, k katot: istemli mi (a daha aktif)
assert not ev('X','Y') and ev('Y','Z') and ev('X','Z')
cell=lambda a,k: act[a]-act[k]
assert cell('Y','Z')>cell('X','Z')
v='var'; y='yok'
rows15=[['X(k)','—',y,v],['Y(k)',v,'—',v],['Z(k)',y,y,'—']]
SK=tablo_svg(['Metal','X²⁺(suda)','Y²⁺(suda)','Z²⁺(suda)'],rows15)
q('0015',tipId='el-potansiyel',tip='Elektrot potansiyeli ve istemlilik',z='zor',alt='Elektrotlar ve Elektrokimyasal Hücreler',kaz='Metal–iyon tepkime tablosundan aktiflik sırasını çıkarır ve galvanik hücre yorumunu yapar.',kalip='öncüllü',
 kart='K-AKELEK-15 (metal–çözelti tablosu) · X, Y, Z metalleri',sekil=SK,
 metin='Bir öğrenci, X, Y ve Z metallerinin +2 yüklü iyonlarını içeren 1 M derişimli çözeltilerle üç metali ayrı ayrı denemiştir. Metal çubuk her çözeltiye daldırıldığında tepkime olup olmadığını tabloda “var” ya da “yok” olarak işaretlemiştir; metallerin kendi iyonlarının çözeltisindeki hücreler çizgiyle gösterilmiştir.\nI. Aktiflik sırası Y > X > Z’dir.\nII. Y(k) | Y²⁺(suda) || Z²⁺(suda) | Z(k) hücresinin standart hücre potansiyeli, X(k) | X²⁺(suda) || Z²⁺(suda) | Z(k) hücresininkinden büyüktür.\nIII. X(k) | X²⁺(suda) || Y²⁺(suda) | Y(k) hücresinde standart koşullarda kendiliğinden tepkime gerçekleşmez.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I, II ve III',sira=S_STD,yan=[('Yalnız I','II ve III’ü doğru bulamamış; en aktif metalle en az aktif metal arasındaki potansiyel farkının büyük olacağını ve X’in Y²⁺’yı indirgeyemeyeceğini kullanmamıştır.','dikkat'),('Yalnız II','I’i yanlış saymış; tabloyu ters okuyup X’in Y²⁺ ile tepkimeye gireceğini sanmış ve aktiflik sırasını belirleyememiştir.','bilgi'),('I ve II','III’ü yanlış saymış; X’in Y²⁺ çözeltisinde “yok” olduğunu, dolayısıyla X anot, Y katot olan hücrenin istemsiz olduğunu görmemiştir.','dikkat'),('I ve III','II’yi yanlış saymış; E° farkı daha büyük olan hücrenin Y–Z hücresi olduğunu, X ile Z arasındaki farkın daha küçük olduğunu hesaba katmamıştır.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Önce her metalin hangi iyonları indirgediğini tablodan okuyup üç metali aktifliğine göre sırala.'],
 bilgi=[B('Aktiflik ve tepkime','bir metal, kendinden daha az aktif metalin iyonlarını çözeltisinde indirger ve kendisi çözünür; daha aktif metalin iyonuyla tepkime vermez. Aktifliği fazla olan metalin E° değeri küçüktür. Örnek: Fe, Cu²⁺ çözeltisine batırılınca Cu birikir; Cu ise Fe²⁺ çözeltisinde değişmez')],
 ad=[A('Tabloyu oku','Y hem X²⁺ hem Z²⁺ ile, X yalnız Z²⁺ ile tepkime verir; Z hiçbirini indirgemez.','Y > X > Z'),A('I’i değerlendir','Aktiflik sırası Y > X > Z’dir.','I doğru'),A('II’yi değerlendir','E° farkı, aktiflik farkı büyük olan Y–Z hücresinde daha büyüktür.','Y–Z > X–Z → II doğru'),A('III’ü değerlendir','X anot, Y katot olursa X, Y²⁺’yı indirgemelidir; tablo “yok” diyor.','Hücre istemsiz → III doğru'),A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],
 puf='Tablodaki “var” yerleri, çözünen metalin daha aktif olduğunu gösterir; sıralamayı ondan çıkar.')

# ============ 16 · derişim–zaman, Nernst (Cu–Ag) · zor · grafik ============
kartla('16','Hücre çalışırken derişim değişimi ve potansiyel','Pil çalışırken ürün derişimi artar, giren derişimi azalır; Q büyür ve E düşer. Q yazılırken katsayılar üs olur.','Derişimin katsayısını üs almamak; Q’yu ters yazmak; n’yi yanlış almak.','zor','grafik',5,'derisim','Derişim pili ve Nernst eşitliği')
E16=D('0.46'); assert D('0.80')-D('0.34')==E16
def E_(cu,ag):
    r=D(cu)/D(ag)**2; l=0
    while r>1: r/=10; l+=1
    while r<1: r*=10; l-=1
    assert r==1; return E16-D('0.059')/2*l
assert E_('1.0','0.1')==D('0.401')
assert E16-D('0.059')/2*1==D('0.4305') and E16+D('0.059')==D('0.519') and E16+D('0.059')*2==D('0.578')
assert D('0.1')+D('0.9')==1 and D('1.9')-2*D('0.9')==D('0.1')
g=r"""\begin{axis}[width=7cm,height=5.6cm,xmin=0,xmax=64,ymin=0,ymax=2.1,xtick={0,60},ytick={0.1,1.0,1.9},yticklabels={0{,}1,1{,}0,1{,}9},tick label style={font=\small},axis lines=left,xlabel={Zaman (dakika)},ylabel={Derişim (M)},xlabel style={font=\small},ylabel style={font=\small},ymajorgrids,grid style={dotted,gray}]
\addplot[thick,vurgu,mark=*,mark size=1.4pt] coordinates {(0,0.1) (15,0.55) (30,0.8) (45,0.95) (60,1.0)};
\addplot[thick,mark=square*,mark size=1.4pt] coordinates {(0,1.9) (15,1.0) (30,0.5) (45,0.2) (60,0.1)};
\node[anchor=south west] at (axis cs:40,0.5) {$\ce{Cu^{2+}}$};\node[anchor=south west] at (axis cs:3,1.7) {$\ce{Ag+}$};
\end{axis}"""
SK=tk(g)
q('0016',tipId='el-derisim',tip='Derişim pili ve Nernst eşitliği',z='zor',alt='Elektrot Potansiyelleri',kaz='Derişim–zaman grafiğinden hücre tepkimesinin Q değerini bulup Nernst eşitliğiyle hücre potansiyelini hesaplar.',kalip='grafik',
 kart='K-AKELEK-16 (derişim–zaman grafiği) · Cu–Ag hücresi, çalışma boyunca potansiyel',sekil=SK,
 metin='25 °C’de Cu(k) | Cu²⁺(suda) || Ag⁺(suda) | Ag(k) hücresi çalıştırılırken yarı hücrelerdeki iyon derişimlerinin zamanla değişimi grafikte verilmiştir. Hücre tepkimesi Cu(k) + 2Ag⁺(suda) → Cu²⁺(suda) + 2Ag(k) olup standart hücre potansiyeli E° = 0,46 V’tur. Nernst eşitliğinde logaritmik terimin katsayısı 0,059/n alınacaktır; burada n, tepkimede aktarılan elektron sayısıdır.\nBuna göre hücre, grafikteki 60. dakikaya geldiğinde hücre potansiyeli kaç volttur?',
 dogru=D('0.401'),yan=[(D('0.4305'),'Q’yu yazarken Ag⁺ derişiminin katsayısını üs almamış: Q = 1,0/0,1 = 10 bulup E = 0,46 − 0,0295 × 1 = 0,4305 V hesaplamıştır.','islem'),(D('0.46'),'Derişimlerin 1 M olduğunu düşünüp Q = 1 almış; logQ = 0 olduğundan E = E° = 0,46 V bulmuştur.','bilgi'),(D('0.519'),'Q’yu ters yazmış: Q = 0,01/1,0 = 10⁻²; E = 0,46 + 0,0295 × 2 = 0,519 V bulmuştur.','islem'),(D('0.578'),'Q’yu ters yazmış ve n yerine 1 almıştır: E = 0,46 + 0,059 × 2 = 0,578 V.','islem')],
 istenen='60. dakikadaki hücre potansiyeli (V).',ip=['Grafikten 60. dakikadaki iki derişimi oku; Q’yu yazarken katsayıların üs olduğunu unutma ve n’yi tepkimeden bul.'],
 bilgi=[B('Hücre çalışırken Q','hücre çalışırken ürün derişimi artar, giren derişimi azalır; Q büyür ve E, E° değerinden uzaklaşarak azalır. Q ifadesinde her derişim, tepkime denklemindeki katsayısı kadar üs alır. Hücre dengeye ulaşınca Q = K olur ve E = 0 olur. Örnek: Q = 1 iken E = E°’dir')],
 ad=[A('Grafikten oku','60. dakikada Cu²⁺ 1,0 M, Ag⁺ 0,1 M’dır.','[Cu²⁺] = 1,0; [Ag⁺] = 0,1'),A('Q’yu yaz','Ag⁺’nın katsayısı 2 olduğundan derişimin karesi alınır.','Q = [Cu²⁺] ÷ [Ag⁺]² = 1,0 ÷ 0,01 = 10²'),A('n’yi belirle','Cu → Cu²⁺ + 2e⁻ olduğundan n = 2’dir.','0,059 ÷ 2 = 0,0295'),A('Nernst','E = E° − (0,059/n)·logQ.','E = 0,46 − 0,0295 × 2 = 0,401 V')],
 puf='Q yazılırken derişimler katsayı kadar üs alır; pil çalıştıkça Q büyür ve potansiyel düşer.')

# ============ 17 · Pt'li hücre · zor ============
kartla('17','İnert elektrotlu hücre yorumu','Aynı elementin iki yükseltgenme basamağını içeren yarı hücrede inert elektrot (Pt) elektron ileticidir; kütlesi değişmez.','Pt elektrodu anot ya da çözünen sanmak; Ehücre’yi E° farkıyla bulmayı unutmak.','orta','düz',5,'galvanik','Galvanik hücre yorumu')
E17=D('0.77')-D('-0.76'); assert E17==D('1.53')
S17=['Standart hücre potansiyeli 0,01 V’tur.','Pt elektrot anottur ve kütlesi zamanla azalır.','Zn elektrodun kütlesi zamanla artar.','Dış devrede elektronlar Pt elektrottan Zn elektroda doğru akar.','Hücre çalışırken Fe²⁺ derişimi artar ve Pt elektrodun kütlesi değişmez.']
assert D('0.77')+D('-0.76')==D('0.01')
q('0017',tipId='el-galvanik',tip='Galvanik hücre yorumu',z='orta',alt='Elektrotlar ve Elektrokimyasal Hücreler',kaz='İnert elektrotlu galvanik hücrede elektrot rollerini, elektron akışını ve derişim değişimlerini yorumlar.',kalip='düz',
 kart='K-AKELEK-17 (Zn | Fe³⁺, Fe²⁺ | Pt hücresi) · inert elektrot',
 metin='Standart koşullarda hazırlanan bir elektrokimyasal hücrenin şematik gösterimi aşağıda verilmiştir.\nZn(k) | Zn²⁺(suda, 1 M) || Fe³⁺(suda, 1 M), Fe²⁺(suda, 1 M) | Pt(k)\nBu hücrede KNO₃ içeren tuz köprüsü kullanılmaktadır.\nZn²⁺(suda) + 2e⁻ → Zn(k)  E° = −0,76 V\nFe³⁺(suda) + e⁻ → Fe²⁺(suda)  E° = +0,77 V\nBuna göre bu hücreyle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=S17[4],sira=S17,yan=[(S17[0],'E° değerlerini işaretleriyle toplamış: 0,77 + (−0,76) = 0,01 V. Hücre potansiyeli E°(katot) − E°(anot) = 0,77 − (−0,76) = 1,53 V’tur.','islem'),(S17[1],'Pt elektrodu anot ve çözünen bir elektrot sanmış; Pt inerttir, E° değeri büyük olan Fe³⁺/Fe²⁺ yarı hücresi katottur ve Pt’de yalnız elektron aktarımı olur.','bilgi'),(S17[2],'Zn’yi katot sanmış; E° değeri küçük olan Zn yükseltgenerek çözünür ve kütlesi azalır.','bilgi'),(S17[3],'Elektron yönünü ters yazmış; elektronlar anot olan Zn’den dış devreden katot olan Pt elektroda akar.','bilgi')],
 istenen='Doğru olan ifade.',ip=['Hangi yarı hücrede yükseltgenmenin, hangisinde indirgenmenin olduğunu E° değerlerinden belirle; Pt’nin yalnızca elektron ileten bir elektrot olduğunu unutma.'],
 bilgi=[B('İnert elektrot','çözeltideki iyonlar arasında elektron alışverişinin olduğu ve katı metal bulunmayan yarı hücrelerde Pt gibi inert elektrot kullanılır. İnert elektrot tepkimeye girmez, kütlesi değişmez; yalnız elektronu iletir. Örnek: Pt | Sn⁴⁺, Sn²⁺ yarı hücresi')],
 ad=[A('Anot ve katot','E° değeri küçük olan Zn anot, büyük olan Fe³⁺/Fe²⁺ yarı hücresi katottur.','Anot: Zn → Zn²⁺ + 2e⁻ · Katot: Fe³⁺ + e⁻ → Fe²⁺'),A('Hücre tepkimesi','Elektron sayıları eşitlenir.','Zn + 2Fe³⁺ → Zn²⁺ + 2Fe²⁺'),A('Hücre potansiyeli','Katot eksi anot.','0,77 − (−0,76) = 1,53 V'),A('Elektron yönü','Elektronlar Zn’den Pt’ye akar; Zn çözünür, Pt değişmez.','Zn kütlesi azalır · Pt kütlesi sabit'),A('Derişimler','Katot yarı hücresinde Fe³⁺ azalır, Fe²⁺ oluşur.','[Fe²⁺] artar → son ifade doğru')],
 puf='Pt gibi inert elektrotlar tepkimeye girmez; kütleleri değişmez.')

# ============ 18 · redoks denkleştirme · orta ============
kartla('18','Redoks tepkimesi denkleştirme','Elektron kazancı ve kaybı eşitlenir, sonra O ve H dengelenir (asidik ortam).','H₂O katsayısını O atomu sayımıyla yanlış bulmak; elektron eşitlemesini atlamak.','orta','düz',5,'yukseltgenme','Yükseltgenme basamağı bulma')
# Cr2O7^2- + 6Fe2+ + 14H+ -> 2Cr3+ + 6Fe3+ + 7H2O
a=dict(Cr2O7=1,Fe2=6,H=14,Cr3=2,Fe3=6,H2O=7)
assert 2*3==a['Fe2']*1 and a['Cr2O7']*7+0==a['H2O'] and a['H']==2*a['H2O']
assert a['Cr2O7']*(-2)+a['Fe2']*2+a['H']==a['Cr3']*3+a['Fe3']*3   # yük
assert a['Fe2']+a['H2O']==13 and a['Cr3']+a['H2O']==9 and a['H']+a['H2O']==21 and 6+6==12
q('0018',tipId='el-yukseltgenme',tip='Yükseltgenme basamağı bulma',z='orta',alt='Redoks Tepkimeleri',kaz='Asidik ortamda redoks tepkimesini yükseltgenme basamağı değişimine göre denkleştirir.',kalip='düz',
 kart='K-AKELEK-18 (Cr₂O₇²⁻ + Fe²⁺) · asidik ortam denkleştirme',
 metin='Turuncu renkli dikromat iyonları, asidik ortamda Fe²⁺ iyonlarını Fe³⁺ iyonlarına yükseltgerken kendileri yeşil renkli Cr³⁺ iyonlarına indirgenir. Bu olay, soluk testlerinde de kullanılan bir renk değişimidir. Tepkimenin denkleştirilmemiş denklemi aşağıda verilmiştir.\nCr₂O₇²⁻(suda) + Fe²⁺(suda) + H⁺(suda) → Cr³⁺(suda) + Fe³⁺(suda) + H₂O(s)\nBu tepkime en küçük tam sayılarla denkleştirildiğinde Fe²⁺ ile H₂O’nun katsayıları toplamı kaç olur?',
 dogru=13,yan=[(7,'Yalnız H₂O’nun katsayısını (7) toplam sanmış; Fe²⁺’nın katsayısını dikkate almamıştır.','dikkat'),(9,'Cr³⁺ ile H₂O’nun katsayılarını toplamış: 2 + 7 = 9.','dikkat'),(12,'Fe²⁺’yı doğru bulmuş (6) ancak H₂O’yu da 6 bulmuş; yedi oksijenin yedi H₂O oluşturduğunu görmemiştir.','islem'),(21,'H⁺ ile H₂O’nun katsayılarını toplamış: 14 + 7 = 21.','dikkat')],
 istenen='Fe²⁺ ile H₂O katsayılarının toplamı.',ip=['Önce Cr ve Fe’nin yükseltgenme basamağı değişimlerini bulup elektron sayılarını eşitle; O ve H’yi en sonda dengele.'],
 bilgi=[B('Redoks denkleştirme','önce yükseltgenme basamağı değişen atomlar ve verilen/alınan elektron sayıları bulunur; elektron sayıları katsayılarla eşitlenir. Asidik ortamda oksijenler H₂O ile, hidrojenler H⁺ ile dengelenir; son olarak yük denkliği kontrol edilir. Örnek: MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O')],
 ad=[A('Basamak değişimi','Cr +6’dan +3’e (iki atom), Fe +2’den +3’e çıkar.','Cr₂O₇²⁻: 2 × 3 = 6 e⁻ alır · Fe²⁺: 1 e⁻ verir'),A('Elektronları eşitle','Alınan 6 elektron için 6 Fe²⁺ gerekir.','1 Cr₂O₇²⁻ + 6Fe²⁺ → 2Cr³⁺ + 6Fe³⁺'),A('O dengesi','Yedi O atomu 7 H₂O oluşturur.','H₂O = 7'),A('H dengesi','7 H₂O’da 14 H vardır.','H⁺ = 14'),A('Toplam','Fe²⁺ + H₂O katsayıları.','6 + 7 = 13')],
 puf='Önce elektronları eşitle, sonra O için H₂O, H için H⁺ ekle.')

# ============ 19 · Hofmann voltametresi · orta · öncüllü · şekil ============
kartla('19','Suyun elektrolizi (Na₂SO₄ çözeltisi)','Na₂SO₄ çözeltisinde elektroliz yalnız suyu ayrıştırır: katotta H₂, anotta O₂ (hacim oranı 2:1); tuz miktarı değişmez, derişimi artar.','Na⁺ iyonlarının katotta indirgendiğini sanmak; tuz miktarının azaldığını düşünmek.','orta','öncüllü',4,'elektroliz','Elektroliz hücresi ve ürünler')
assert 20/10==2
g='\\fill[vurgu!15] (0,0.2) rectangle (3.0,0.5);\\fill[vurgu!15] (0,0.5) rectangle (0.8,2.5);\\fill[vurgu!15] (2.2,0.5) rectangle (3.0,3.5);\\fill[vurgu!15] (1.2,0.5) rectangle (1.8,4.0);'
g+='\\draw[thick] (0,4.5) -- (0,0.2) -- (3.0,0.2) -- (3.0,4.5);\\draw[thick] (0.8,4.5) -- (0.8,0.5) -- (1.2,0.5) -- (1.2,4.5);\\draw[thick] (1.8,4.5) -- (1.8,0.5) -- (2.2,0.5) -- (2.2,4.5);\\draw[thick] (0,4.5) -- (0.8,4.5);\\draw[thick] (2.2,4.5) -- (3.0,4.5);'
g+=elek(0.4,0.5,1.4)+elek(2.6,0.5,1.4)
g+='\\draw[thick] (0.4,0.5) -- (0.4,-0.3) -- (1.3,-0.3);\\draw[thick] (2.6,0.5) -- (2.6,-0.3) -- (1.7,-0.3);'+bat(1.5,-0.3,1.3,1.7)
g+='\\draw[<->] (-0.35,2.5) -- (-0.35,4.5);\\node[left] at (-0.35,3.5) {20 mL};\\draw[<->] (3.35,3.5) -- (3.35,4.5);\\node[right] at (3.35,4.0) {10 mL};'
g+='\\node[anchor=east] at (-0.1,1.0) {K};\\node[anchor=west] at (3.1,1.0) {L};\\node[above] at (1.5,4.55) {\\ce{Na2SO4}(suda)};'
SK=tk(g)
q('0019',tipId='el-elektroliz',tip='Elektroliz hücresi ve ürünler',z='orta',alt='Elektroliz',kaz='Hofmann düzeneğinde Na₂SO₄ çözeltisinin elektrolizinde ürünleri ve çözelti değişimini yorumlar.',kalip='öncüllü',
 kart='K-AKELEK-19 (Hofmann voltametresi) · Na₂SO₄ çözeltisi',sekil=SK,
 metin='Şekildeki Hofmann voltametresine Na₂SO₄ sulu çözeltisi doldurulmuş, K ve L platin elektrotları bir üretece bağlanarak elektroliz başlatılmıştır. Belirli bir süre sonra tüplerde toplanan gazların hacimleri şekilde verilmiştir. Gazlar aynı sıcaklık ve basınçtadır; çözeltinin sıcaklığı sabit tutulmuştur.\nI. K tüpünde H₂, L tüpünde O₂ gazı toplanmıştır.\nII. L elektrodu çevresinde çözeltinin pH değeri azalır.\nIII. Elektroliz boyunca çözeltideki Na₂SO₄’ün mol sayısı azalır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve II',sira=S_STD,yan=[('Yalnız I','II’yi yanlış saymış; anotta 2H₂O → O₂ + 4H⁺ + 4e⁻ tepkimesiyle H⁺ oluştuğunu, çevrenin asitleştiğini görmemiş.','bilgi'),('Yalnız II','I’i yanlış saymış; hacmi büyük olan tüpte H₂ toplandığını, katotta Na⁺ yerine suyun indirgendiğini kavrayamamış.','bilgi'),('I ve III','III’ü doğru bulmuş; Na₂SO₄’ün tepkimeye girmediğini, yalnız suyun tükendiğini görmemiş. II’yi de atlamış.','dikkat'),('I, II ve III','III’ü de doğru bulmuş; tuzun elektroliz sırasında harcandığını düşünmüş, oysa yalnız su ayrışır ve tuzun mol sayısı sabit kalır.','bilgi')],
 istenen='Doğru olan yargılar.',ip=['Katotta ve anotta oluşan gazların hacim oranını, ürünlerin mol oranıyla ilişkilendir; çözeltide tüketilen maddenin ne olduğunu düşün.'],
 bilgi=[B('Suyun elektrolizi','Na⁺, K⁺ gibi aktif metal katyonları sulu çözeltide indirgenmez; suyun kendisi indirgenir. SO₄²⁻ gibi oksijenli asit anyonları da yükseltgenmez; su yükseltgenir. Katotta 2H₂O + 2e⁻ → H₂ + 2OH⁻, anotta 2H₂O → O₂ + 4H⁺ + 4e⁻ olur; H₂ hacmi O₂’nin iki katıdır')],
 ad=[A('Gazları belirle','Hacmi büyük olan tüpte H₂, küçük olanda O₂ toplanır.','K: 20 mL H₂ · L: 10 mL O₂ → I doğru'),A('Anot çevresi','L anotta su yükseltgenir ve H⁺ oluşur.','2H₂O → O₂ + 4H⁺ + 4e⁻ → pH azalır → II doğru'),A('Tuzun durumu','Yalnız su harcanır; Na₂SO₄ tepkimeye girmez.','n(Na₂SO₄) sabit → III yanlış'),A('Sonuç','I ve II doğrudur.','I ve II')],
 puf='Na₂SO₄ gibi tuzların sulu çözeltisinin elektrolizinde yalnız su ayrışır; tuz miktarı sabit kalır.')

# ============ 20 · m–Q grafiği · orta · grafik ============
kartla('20','Kütle–yük grafiğinden iyon yükü','Biriken mol = m/M; elektron mol = Q/96500; iyon yükü n = mol e⁻ / mol madde.','Yükü ve kütleyi farklı noktalardan okumak; n yerine 1 almak.','orta','grafik',4,'faraday','Faraday yasaları hesabı')
nX=(D(19300)/96500)/(D('6.4')/64); nY=(D(19300)/96500)/(D('1.8')/27)
assert nX==2 and nY==3 and nX+nY==5
nX1=(D(9650)/96500)/(D('6.4')/64); assert nX1==1 and nX1+nY==4
nX2=(D(19300)/96500)/(D('3.2')/64); assert nX2==4 and nX2+nY==7
nY2=(D(19300)/96500)/(D('0.9')/27); assert nY2==6 and nX+nY2==8
assert nX2+nY2==10
g='''\\begin{axis}[width=7cm,height=5.6cm,xmin=0,xmax=21000,scaled x ticks=false,ymin=0,ymax=7.2,xtick={0,9650,19300},xticklabels={0,9650,19300},ytick={0.9,1.8,3.2,6.4},yticklabels={0{,}9,1{,}8,3{,}2,6{,}4},tick label style={font=\\small},axis lines=left,xlabel={Geçen yük (C)},ylabel={Katotta biriken kütle (g)},xlabel style={font=\\small},ylabel style={font=\\small},ymajorgrids,xmajorgrids,grid style={dotted,gray}]
\\addplot[thick,vurgu,mark=*,mark size=1.4pt] coordinates {(0,0) (9650,3.2) (19300,6.4)};
\\addplot[thick,mark=square*,mark size=1.4pt] coordinates {(0,0) (9650,0.9) (19300,1.8)};
\\node[anchor=south east] at (axis cs:17500,5.6) {X};\\node[anchor=south east] at (axis cs:17500,2.2) {Y};
\\end{axis}'''
SK=tk(g)
q('0020',tipId='el-faraday',tip='Faraday yasaları hesabı',z='orta',alt='Elektroliz',kaz='Kütle–yük grafiğinden elektroliz sonucu biriken metallerin iyon yüklerini hesaplar.',kalip='grafik',
 kart='K-AKELEK-20 (kütle–yük grafiği) · X ve Y metalleri',sekil=SK,
 metin='Bir öğrenci, X ve Y metallerinin tuzlarının erimiş hâllerini ayrı ayrı elektroliz ederek her deneyde katotta biriken metal kütlesini, devreden geçen yüke karşı grafiğe işlemiştir. X ve Y metallerinin mol kütleleri sırasıyla 64 g/mol ve 27 g/mol’dür; katotta yalnız bu metaller birikmiştir. İyonlar X^(a+) ve Y^(b+) biçimindedir.\n(1 mol elektronun yükü = 96500 C)\nBuna göre a + b toplamı kaçtır?',
 dogru=5,yan=[(4,'X için 9650 C yükünü, 6,4 g kütleyle eşleştirmiş; böylece a = 1 bulup 1 + 3 = 4 hesaplamıştır.','dikkat'),(7,'X’in 3,2 g kütlesini 19300 C yüküyle eşleştirip a = 4 bulmuş; 4 + 3 = 7 hesaplamıştır.','dikkat'),(8,'Y’nin 0,9 g kütlesini 19300 C yüküyle eşleştirip b = 6 bulmuş; 2 + 6 = 8 hesaplamıştır.','dikkat'),(10,'Hem X hem Y için kütleyi yanlış yük değeriyle eşleştirip a = 4 ve b = 6 bulmuş; toplamı 10 yazmıştır.','dikkat')],
 istenen='X ve Y iyon yüklerinin toplamı.',ip=['Grafikte aynı yük değerinde (bir noktada) her iki metalin kütlesini oku; mol elektron sayısını mol metal sayısına böl.'],
 bilgi=[B('Grafikten iyon yükü','katotta Mⁿ⁺ + ne⁻ → M olduğundan, aynı noktada mol elektron sayısının mol metal sayısına oranı iyon yükünü verir: n = (Q/96500) ÷ (m/M). Örnek: 4825 C’de 1,35 g biriken, mol kütlesi 27 g/mol olan bir metalin yükü 0,05 mol elektronun 0,05 mol metale bölünmesiyle 1 bulunur')],
 ad=[A('Aynı noktayı seç','Q = 19300 C’de X 6,4 g, Y 1,8 g’dır.','n(e⁻) = 19300 ÷ 96500 = 0,2 mol'),A('X’in yükü','Metal mol sayısı: 6,4 ÷ 64 = 0,1 mol.','a = 0,2 ÷ 0,1 = 2'),A('Y’nin yükü','Metal mol sayısı: 1,8 ÷ 27 = 1/15 mol.','b = 0,2 ÷ (1/15) = 3'),A('Topla','Yüklerin toplamı istenir.','a + b = 2 + 3 = 5')],
 puf='Grafikte her iki değeri aynı yük noktasında oku; sonra mol elektron ÷ mol metal.')

# ---------- bitir ----------
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(GD,'elektro-1.json'),'/tmp/bos-elektro.json')
tipler={}
for c in K.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Kimya çıkmış soruları (yalnız mantık), MEB 11–12. sınıf müfredatı.',kartlar=K.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akelektro.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
