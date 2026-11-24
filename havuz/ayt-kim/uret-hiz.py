"""AYT Kimya · Kimyasal Tepkimelerde Hız · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ/tablo; her değer Python'da hesaplanıp assert edilir."""
import sys,os,json,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
H.KONU='Kimyasal Tepkimelerde Hız'
H.HD=GD   # çıktı ayt-kim/ altına
P=Parti('hiz','Kimyasal Tepkimelerde Hız','akim|Kimyasal Tepkimelerde Hız',ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2018–2026 Kimya (yalnız mantık) · MEB 11. sınıf Kimyasal Tepkimelerde Hız'
TIPN={'hz-ifade':'Hız ifadesi ve ortalama hız','hz-denklem':'Hız denklemi ve hız sabiti','hz-mekanizma':'Mekanizma ve hızı belirleyen basamak','hz-enerji':'Aktivasyon enerjisi ve enerji diyagramı','hz-katalizor':'Katalizör ve aktivasyon enerjisi','hz-sicaklik':'Sıcaklık ve kinetik enerji dağılımı','hz-faktor':'Hızı etkileyen faktörler'}
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    kart(f'K-AKHZ-{n}',alt,fikir,tuzak,z,kalip,adim,f'hz-{tipad}',TIPN[f'hz-{tipad}'],KY)
def q(no,**k):
    assert len(k['ip'])==1
    k['tip']=TIPN[k['tipId']]
    mk(P,no,adim=len(k['ad']),ad=k.pop('ad'),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
ROM={'I':1,'II':2,'III':3}
def kume(s):
    s=s.replace('Yalnız ','').replace(' ve ',', ')
    return {ROM[x.strip()] for x in s.split(',')}
RS={1:'I',2:'II',3:'III'}; EK={1:'I’i',2:'II’yi',3:'III’ü'}
def onc(truth,sira,dyd,dyy,tur='bilgi'):
    """truth {1:bool,..}; sira: 5 şık; dyd[i]: i yanlış iken doğru sayan öğrencinin hatası; dyy[i]: i doğru iken yanlış sayan öğrencinin hatası.
    Dönüş: (doğru şık, çeldirici listesi)."""
    T={i for i,v in truth.items() if v}
    dog=[s for s in sira if kume(s)==T]; assert len(dog)==1,(sira,T)
    yan=[]
    for s in sira:
        if s==dog[0]: continue
        K=kume(s); parts=[]
        for i in sorted(truth):
            if i in K and i not in T: parts.append(f'{EK[i]} doğru saymış: {dyd[i]}')
            if i not in K and i in T: parts.append(f'{EK[i]} yanlış saymış: {dyy[i]}')
        assert parts
        yan.append((s,'; '.join(parts)+'.',tur))
    return dog[0],yan
def sirala(*k): return [s for s in ORD if s in k]
def yer(dogru,digerler,poz):
    d=list(digerler); assert dogru not in d and len(d)==4; d.insert(poz,dogru); return d
def mm(x): return f'{x:.3f}'
# ---------- enerji diyagramı ----------
def pe_axes(ymax,ticks,xmax,sc,ytit='Potansiyel enerji (kJ)'):
    g=f'\\draw[thick,{ARR}] (0,0) -- (0,{ymax*sc+.4:.3f}); \\draw[thick,{ARR}] (0,0) -- ({xmax+.4:.3f},0);'
    g+=f'\\node[rotate=90,anchor=south] at (-.95,{ymax*sc/2:.3f}) {{{ytit}}}; \\node[anchor=north] at ({xmax/2:.3f},-.1) {{Tepkime koordinatı}};'
    for t in ticks:
        g+=f'\\draw[thick] (-.08,{t*sc:.3f}) -- (.08,{t*sc:.3f}); \\node[left] at (-.1,{t*sc:.3f}) {{{t}}};'
    return g
def pe_path(pts,sc,style='very thick'):
    s=f'\\draw[{style}] ({pts[0][0]:.3f},{pts[0][1]*sc:.3f})'
    for (xa,ya),(xb,yb) in zip(pts,pts[1:]):
        xm=(xa+xb)/2; s+=f' .. controls ({xm:.3f},{ya*sc:.3f}) and ({xm:.3f},{yb*sc:.3f}) .. ({xb:.3f},{yb*sc:.3f})'
    return s+';'
def guide(y,x1,sc): return f'\\draw[dotted,gray] (0,{y*sc:.3f}) -- ({x1:.3f},{y*sc:.3f});'

# ================= 01 · hız ifadesi · kolay · öncüllü =================
kartla('01','Tepkime hızı ve katsayı ilişkisi','Her maddenin hızı katsayısına bölününce tepkime hızı bulunur: r = −Δ[A]/(aΔt) = Δ[C]/(cΔt).','Maddelerin hızını doğrudan tepkime hızı sanmak; katsayı oranını ters uygulamak.','kolay','öncüllü',3,'ifade','Hız ifadesi ve katsayılar')
rNH3=Fr(6,100); rH2=rNH3*Fr(3,2); rN2=rNH3*Fr(1,2); rxn=rNH3/2
assert rH2==Fr(9,100) and rN2==Fr(3,100) and rxn==Fr(3,100)
tr1={1:True,2:False,3:True}   # I: N2 harcanma 0,03 doğru · II: H2 harcanma 0,06 yanlış · III: tepkime hızı 0,03 doğru
assert rN2==Fr(3,100) and rH2!=Fr(6,100) and rxn==Fr(3,100)
d1,y1=onc(tr1,sirala('Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'),
 {2:'H₂’nin harcanma hızını NH₃’ün oluşma hızıyla aynı almış, 3/2 katsayı oranını uygulamamış'},
 {1:'N₂’nin harcanma hızını NH₃’ünkine eşit ya da ondan büyük sanmış, katsayısı 1 olan N₂’nin hızının yarıya düştüğünü görmemiş',
  3:'tepkime hızını NH₃’ün oluşma hızına eşitlemiş, 2 katsayısına bölmeyi unutmuş'})
q('0001',tipId='hz-ifade',tip='Hız ifadesi ve katsayılar',z='kolay',alt='Tepkime Hızları',kaz='Tepkimedeki maddelerin hızlarını katsayılarla ilişkilendirerek tepkime hızını yorumlar.',kalip='öncüllü',
 kart='K-AKHZ-01 (hız–katsayı ilişkisi) · amonyak sentezi',
 metin='Sabit hacimli kapalı bir kapta N₂(g) + 3H₂(g) → 2NH₃(g) tepkimesi gerçekleşirken belirli bir anda NH₃(g)’ün oluşma hızı 0,06 mol/L·s olarak ölçülüyor.\nI. N₂(g)’nin harcanma hızı 0,03 mol/L·s’dir.\nII. H₂(g)’nin harcanma hızı 0,06 mol/L·s’dir.\nIII. Tepkime hızı 0,03 mol/L·s’dir.\nBuna göre bu anda yukarıdaki yargılardan hangileri doğrudur?',
 dogru=d1,sira=sirala('Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'),yan=y1,
 istenen='Doğru olan yargılar.',ip=['Her maddenin hızını kendi katsayısına bölersen aynı değeri, yani tepkime hızını elde edersin.'],
 bilgi=[B('Tepkime hızı','birim zamanda derişimdeki değişimdir. A + 2B → C gibi bir tepkimede r = −Δ[A]/Δt = −Δ[B]/(2Δt) = Δ[C]/Δt yazılır; katsayısı büyük olan madde daha hızlı tükenir ya da oluşur. Örnek: bir tepkimede katsayısı 4 olan madde, katsayısı 1 olan maddeden 4 kat hızlı değişir')],
 ad=[A('Hızları katsayıyla ilişkilendir','Tepkime hızı her maddenin hızının katsayısına bölünmesiyle bulunur.','r = v(NH₃)/2 = v(N₂)/1 = v(H₂)/3'),
     A('Tepkime hızı ve N₂','NH₃’ün hızı 0,06 mol/L·s.','r = 0,06 ÷ 2 = 0,03 mol/L·s · N₂’nin katsayısı 1 → v(N₂) = 0,03 mol/L·s'),
     A('H₂’nin hızı','H₂’nin katsayısı 3’tür.','v(H₂) = 3 × 0,03 = 0,09 mol/L·s'),
     A('Yargıları değerlendir','I ve III bulunan değerlerle uyuşur, II uyuşmaz.','I: doğru · II: yanlış (0,09) · III: doğru')],
 puf='Maddelerin hız oranı katsayı oranına eşittir; tepkime hızı için maddenin hızını katsayısına böl.')
# not: tr1 gerçeğe göre I ve III doğrudur
# ================= 02 · tanecik modeli · kolay =================
kartla('02','Ortalama hızı tanecik modelinden bulma','Tanecik sayısını mole, mol sayısını hacme bölerek derişimi bul; derişim değişimini süreye böl.','Hacme bölmeyi unutmak; kalan madde miktarını harcanan sanmak.','kolay','şekilli',3,'ifade','Ortalama hız hesabı (tanecik modeli)')
V2=2; mol_t=Fr(1,5); nA0,nA1,nB1=10,4,3; assert nA0-nA1==2*nB1
dA=Fr((nA0-nA1))*mol_t/V2; vA=dA/40; assert vA==Fr(3,200)
yan2=[(Fr(1,100),'Harcanan A yerine kalan A’nın derişimini kullanmış: 4 × 0,2 ÷ 2 ÷ 40.','dikkat'),(Fr(3,400),'Tepkime hızını (A’nın hızının yarısını) A’nın harcanma hızı sanmış.','bilgi'),(Fr(3,100),'Hacme bölmeyi unutmuş: 6 × 0,2 ÷ 40.','dikkat'),(Fr(3,20),'Tanecik sayısını mole ve hacme çevirmeden doğrudan 6 ÷ 40 yapmış.','islem')]
assert Fr(nA1)*mol_t/V2/40==Fr(1,100) and vA/2==Fr(3,400) and Fr(nA0-nA1)*mol_t/40==Fr(3,100) and Fr(nA0-nA1,40)==Fr(3,20)
def kap(x0,nA,nB,posA,posB):
    s=f'\\draw[very thick] ({x0},2.6) -- ({x0},0) -- ({x0+3},0) -- ({x0+3},2.6);'
    for (a,b) in posA[:nA]: s+=f'\\fill ({x0+a:.2f},{b:.2f}) circle (.11);'
    for (a,b) in posB[:nB]: s+=f'\\draw[very thick] ({x0+a:.2f},{b:.2f}) circle (.17);'
    return s
posA=[(.4,.4),(1.2,.35),(2.1,.5),(2.6,.9),(.6,1.1),(1.5,1.0),(2.2,1.6),(.5,1.8),(1.4,1.9),(2.5,2.2)]
posB=[(.5,.5),(1.6,1.5),(2.3,.6)]
posA2=[(.4,1.0),(1.9,.5),(2.4,1.7),(.9,2.0)]
posB2=[(1.1,.5),(2.4,.7),(.5,1.5)]
g=kap(0,10,0,posA,[])+kap(4.2,4,3,posA2,[(1.2,1.3),(2.3,1.0),(.7,.45)])
g+='\\node at (1.5,2.95) {$t=0$}; \\node at (5.7,2.95) {$t=40$ s};'
g+='\\node at (1.5,-.35) {$V=2$ L}; \\node at (5.7,-.35) {$V=2$ L};'
g+='\\fill (.3,-1.1) circle (.11); \\node[anchor=west] at (.55,-1.1) {A (1 tanecik = 0,2 mol)}; \\draw[very thick] (.3,-1.7) circle (.17); \\node[anchor=west] at (.55,-1.7) {B (1 tanecik = 0,2 mol)};'
SK2=tk(g)
q('0002',tipId='hz-ifade',tip='Ortalama hız hesabı (tanecik modeli)',z='kolay',alt='Tepkime Hızları',kaz='Tanecik modelinden derişim değişimini bularak ortalama harcanma hızını hesaplar.',kalip='şekilli',
 kart='K-AKHZ-02 (ortalama hız) · 2A → B tanecik modeli',sekil=SK2,
 metin='Hacmi 2 L olan kapalı bir kapta 2A(g) → B(g) tepkimesi gerçekleşmektedir. Kaptaki taneciklerin başlangıçtaki ve 40. saniyedeki durumu şekilde modellenmiştir. Her tanecik A için de B için de 0,2 mol maddeyi temsil etmektedir.\nBuna göre A’nın ilk 40 saniyedeki ortalama harcanma hızı kaç mol/L·s’dir?',
 dogru=vA,yan=yan2,istenen='A’nın ortalama harcanma hızı (mol/L·s).',ip=['Önce kaç tanecik A harcandığını bul; sonra bunu mole, derişime ve en son zamana çevir.'],
 bilgi=[B('Ortalama hız','bir maddenin ortalama harcanma hızı v = −Δ[A]/Δt’dir; derişim, mol sayısının hacme bölünmesiyle bulunur. Örnek: 3 L’lik kapta 0,6 mol madde 10 s’de harcanırsa Δ[A] = 0,2 mol/L ve v = 0,02 mol/L·s olur')],
 ad=[A('Harcanan A’yı say','Şekilde başlangıçta 10, sonda 4 A tanecik var.','10 − 4 = 6 tanecik'),A('Mole ve derişime çevir','Her tanecik 0,2 mol; hacim 2 L.','6 × 0,2 = 1,2 mol · 1,2 ÷ 2 = 0,6 mol/L'),A('Süreye böl','Hız, derişim değişiminin süreye oranıdır.','0,6 ÷ 40 = 0,015 mol/L·s')],
 puf='Tanecik sayısını önce mole, sonra hacme bölerek derişime çevir; hız için süreye böl.')

# ================= 03 · aktivasyon enerjisi kavramı · kolay · öncüllü =================
kartla('03','Aktivasyon enerjisi ve çarpışma','Tepkime için etkin çarpışma gerekir; aktivasyon enerjisi sıcaklıkla değişmez, ΔH ile eşit değildir.','Her çarpışmanın ürün verdiğini sanmak; sıcaklığın Ea’yı düşürdüğünü sanmak; Ea ile ΔH’yi karıştırmak.','kolay','öncüllü',2,'enerji','Aktivasyon enerjisi ve etkin çarpışma')
tr3={1:True,2:False,3:False}
s3=sirala('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')
d3,y3=onc(tr3,s3,
 {2:'sıcaklık artınca tepkimenin hızlanmasını aktivasyon enerjisinin küçülmesine bağlamış',3:'aktivasyon enerjisini ürünlerle girenlerin enerji farkı (ΔH) sanmış'},
 {1:'her çarpışmanın tepkimeyle sonuçlandığını düşünmüş'})
q('0003',tipId='hz-enerji',tip='Aktivasyon enerjisi ve etkin çarpışma',z='kolay',alt='Aktivasyon Enerjisi',kaz='Çarpışma teorisine göre aktivasyon enerjisi ve etkin çarpışma kavramlarını yorumlar.',kalip='öncüllü',
 kart='K-AKHZ-03 (aktivasyon enerjisi) · çarpışma teorisi',
 metin='Gaz fazında gerçekleşen bir tepkimede girenlerin molekülleri sürekli çarpışmaktadır. Öğrenciler bu tepkime için sıcaklık ve aktivasyon enerjisiyle ilgili aşağıdaki yorumları yapmıştır.\nI. Girenlerin moleküllerinin yaptığı çarpışmaların hepsi ürün oluşumuyla sonuçlanmaz.\nII. Sıcaklık artırıldığında tepkimenin aktivasyon enerjisi küçülür.\nIII. Tepkimenin aktivasyon enerjisi, tepkime entalpisine (ΔH) eşittir.\nBuna göre bu yorumlardan hangileri doğrudur?',
 dogru=d3,sira=s3,yan=y3,istenen='Doğru olan yorumlar.',ip=['Çarpışmanın ürün vermesi için gereken koşulları ve aktivasyon enerjisini neyin değiştirebildiğini düşün.'],
 bilgi=[B('Aktivasyon enerjisi','girenlerin ürüne dönüşebilmesi için aşması gereken enerji engelidir; yalnızca yeterli enerjiyle ve uygun doğrultuda yapılan çarpışmalar (etkin çarpışma) tepkime verir. Aktivasyon enerjisi girenlerin ve ürünlerin enerji farkından bağımsızdır; yol değişirse (ör. katalizör) değişir')],
 ad=[A('I’i değerlendir','Çarpışmaların yalnız bir kısmı etkindir.','I: doğru'),A('II’yi değerlendir','Sıcaklık, taneciklerin kinetik enerjisini artırır; aktivasyon enerjisini değiştirmez.','II: yanlış'),A('III’ü değerlendir','Aktivasyon enerjisi girenlerden aktifleşmiş komplekse; ΔH girenlerden ürünlere farktır.','III: yanlış'),A('Sonuç','Yalnız I doğrudur.','Yalnız I')],
 puf='Aktivasyon enerjisinin hangi büyüklüklere bağlı olduğunu önce listele, sonra her yargıyı bu listeyle sına.')

# ================= 04 · hız denklemi · orta · tablo =================
kartla('04','Hız denklemini tablodan bulma','Bir değişken sabitken öbürünün değişimi hıza oranlanır; hız oranı = derişim oranı üzeri mertebe.','İki değişkeni birden değiştiren deneyleri kıyaslamak; mertebeyi derişim katsayısı sanmak.','orta','tablo',3,'denklem','Hız denklemini deney tablosundan bulma')
NO=[Fr(1,10),Fr(1,10),Fr(1,5)]; O2=[Fr(1,10),Fr(1,5),Fr(1,10)]; k4=2
h4=[k4*n**2*o for n,o in zip(NO,O2)]; assert h4==[Fr(2,1000),Fr(4,1000),Fr(8,1000)]
SK4=tablo_svg(['Deney','[NO] (mol/L)','[O₂] (mol/L)','Hız (10⁻³ mol/L·s)'],[['1','0,10','0,10','2,0'],['2','0,10','0,20','4,0'],['3','0,20','0,10','8,0']])
s4=['r = k[NO][O₂]','r = k[NO]²','r = k[NO]²[O₂]','r = k[NO][O₂]²','r = k[NO]²[O₂]²']
assert h4[2]/h4[0]==4 and h4[1]/h4[0]==2
q('0004',tipId='hz-denklem',tip='Hız denklemini deney tablosundan bulma',z='orta',alt='Hız Denklemi',kaz='Deney verilerinden tepkimenin mertebelerini bularak hız denklemini yazar.',kalip='tablo',
 kart='K-AKHZ-04 (hız denklemi) · 2NO + O₂ → 2NO₂ deney tablosu',sekil=SK4,
 metin='2NO(g) + O₂(g) → 2NO₂(g) tepkimesinin hız denklemini belirlemek için sabit sıcaklıkta üç deney yapılmış ve başlangıç hızları tabloda verilmiştir (k: hız sabiti).\nBuna göre tepkimenin hız denklemi aşağıdakilerden hangisidir?',
 dogru='r = k[NO]²[O₂]',sira=['r = k[NO]²[O₂]','r = k[NO]²','r = k[NO][O₂]','r = k[NO][O₂]²','r = k[NO]²[O₂]²'],
 yan=[('r = k[NO][O₂]','NO’nun derişimi 2 katına çıkınca hızın 4 katına çıkmasını birinci mertebe sanmış.','bilgi'),('r = k[NO][O₂]²','NO ve O₂’nin mertebelerini yer değiştirmiş.','dikkat'),('r = k[NO]²','O₂’nin derişimi 2 katına çıkınca hızın da 2 katına çıktığını (1. deney – 2. deney) görmemiş.','dikkat'),('r = k[NO]²[O₂]²','O₂ için de mertebeyi 2 almış; 2. deneyde hızın yalnız 2 kat arttığını dikkate almamış.','bilgi')],
 istenen='Hız denklemi.',ip=['Derişimlerden yalnız biri değişen deney çiftlerini kıyasla ve hızın kaç kat değiştiğine bak.'],
 bilgi=[B('Mertebe','r = k[A]ᵐ[B]ⁿ denkleminde m ve n deneyle bulunur. Başka maddenin derişimi sabitken A’nın derişimi 2 katına çıkınca hız 2ᵐ katına çıkar. Örnek: derişim 2 katına çıkınca hız 8 katına çıkıyorsa mertebe 3’tür')],
 ad=[A('[O₂] için kıyasla','1. ve 2. deneyde [NO] sabit, [O₂] iki katına çıkıyor.','Hız: 2,0 → 4,0 (2 kat) · 2¹ = 2 → O₂ 1. mertebe'),A('[NO] için kıyasla','1. ve 3. deneyde [O₂] sabit, [NO] iki katına çıkıyor.','Hız: 2,0 → 8,0 (4 kat) · 2² = 4 → NO 2. mertebe'),A('Denklemi yaz','Bulunan mertebeler üs olarak yazılır.','r = k[NO]²[O₂]')],
 puf='Yalnız bir derişimin değiştiği iki deneyi seç; hız oranının derişim oranı olarak üssünü bul.')

# ================= 05 · hız denklemi · orta · öncüllü =================
kartla('05','Mertebe, derece ve hız sabitinin birimi','Her derişimin mertebelerinin toplamı tepkime derecesidir; k’nın birimi dereceye bağlıdır: L^(n−1)·mol^(1−n)·s⁻¹.','Mertebeyi katsayıyla karıştırmak; k’nın biriminin dereceden bağımsız olduğunu sanmak.','orta','öncüllü',4,'denklem','Mertebe, derece ve hız sabiti birimi')
tr5={1:False,2:True,3:True}
q5_s=sirala('Yalnız II','Yalnız III','I ve II','I ve III','II ve III')
d5,y5=onc(tr5,q5_s,{1:'3 katına çıkan derişim için hızın 9 katına çıkmasını birinci mertebe sanmış'},
 {2:'mertebeleri toplamayı bilmeden derecesini 2 ya da 4 bulmuş',3:'hız sabitinin biriminin dereceden bağımsız olduğunu sanmış'})
q('0005',tipId='hz-denklem',tip='Mertebe, derece ve hız sabiti birimi',z='orta',alt='Hız Denklemi',kaz='Deneysel gözlemlerden mertebeyi ve dereceyi bularak hız sabitinin birimini yorumlar.',kalip='öncüllü',
 kart='K-AKHZ-05 (mertebe ve k birimi) · X + Y deneyleri',
 metin='X(g) + 2Y(g) → Z(g) tepkimesi sabit sıcaklıkta incelenmiş ve şu gözlemler yapılmıştır.\n• Y’nin derişimi sabit tutulup X’in derişimi 3 katına çıkarıldığında tepkime hızı 9 katına çıkmıştır.\n• X’in derişimi sabit tutulup Y’nin derişimi 2 katına çıkarıldığında tepkime hızı 2 katına çıkmıştır.\nI. Tepkime X’e göre birinci derecedendir.\nII. Tepkimenin derecesi 3’tür.\nIII. Hız sabitinin (k) birimi L² mol⁻² s⁻¹’dir.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=d5,sira=q5_s,yan=y5,istenen='Doğru olan yargılar.',ip=['Önce her maddenin mertebesini bul; sonra hız eşitliğinde mol/L ve saniye birimlerini yerine yaz.'],
 bilgi=[B('Hız sabitinin birimi','r = k[A]ᵐ[B]ⁿ eşitliğinde derece m + n’dir. r’nin birimi mol/L·s olduğundan k’nın birimi (mol/L)^(1−derece) · s⁻¹ olur. Örnek: derece 1 ise s⁻¹, derece 2 ise L mol⁻¹ s⁻¹’dir')],
 ad=[A('X’in mertebesi','Hız 9 kat, derişim 3 kat arttı.','3ᵐ = 9 → m = 2'),A('Y’nin mertebesi','Hız 2 kat, derişim 2 kat arttı.','2ⁿ = 2 → n = 1 · r = k[X]²[Y]'),A('Derece ve birim','Mertebeler toplanır; k = r ÷ ([X]²[Y]).','derece = 3 · k: (mol L⁻¹ s⁻¹) ÷ (mol³ L⁻³) = L² mol⁻² s⁻¹'),A('Yargıları değerlendir','I yanlış, II ve III doğru.','II ve III')],
 puf='Birimi bulmak için hız eşitliğinde r = mol L⁻¹ s⁻¹ yaz ve k’yı yalnız bırak.')

# ================= 06 · hız denklemi · zor · tablo =================
kartla('06','Hız denklemi, k ve yeni hız','Mertebeler iki deney çiftinden bulunur, k bir deneyden hesaplanır ve istenen derişimlerde hız bulunur.','Bir mertebeyi yanlış almak; k yerine bir deneyin hızını kullanmak.','zor','tablo',5,'denklem','Mertebe, k ve yeni derişimde hız')
Av=[Fr(1,10),Fr(1,5),Fr(1,5)]; Bv=[Fr(1,10),Fr(1,10),Fr(3,10)]
k6=2; h6=[k6*a*b*b for a,b in zip(Av,Bv)]; assert h6==[Fr(2,1000),Fr(4,1000),Fr(36,1000)]
assert h6[1]/h6[0]==2 and h6[2]/h6[1]==9
a_new,b_new=Fr(3,10),Fr(1,5); ans6=k6*a_new*b_new**2; assert ans6==Fr(24,1000)
def pred(a,b):
    kk=h6[0]/(Av[0]**a*Bv[0]**b); return kk*a_new**a*b_new**b
assert pred(1,2)==ans6
cand=[pred(1,1),pred(2,1),pred(0,2),pred(2,2)]; assert len(set(cand+[ans6]))==5 and cand==[Fr(12,1000),Fr(36,1000),Fr(8,1000),Fr(72,1000)]
SK6=tablo_svg(['Deney','[A] (mol/L)','[B] (mol/L)','Başlangıç hızı (10⁻³ mol/L·s)'],[['1','0,10','0,10','2,0'],['2','0,20','0,10','4,0'],['3','0,20','0,30','36,0']])
q('0006',tipId='hz-denklem',tip='Mertebe, k ve yeni derişimde hız',z='zor',alt='Hız Denklemi',kaz='Deney tablosundan hız denklemini ve hız sabitini bulup yeni derişimlerde hızı hesaplar.',kalip='tablo',
 kart='K-AKHZ-06 (hız denklemi, k, yeni hız) · A + 2B → C',sekil=SK6,
 metin='A(g) + 2B(g) → C(g) tepkimesi için sabit sıcaklıkta yapılan deneylerin sonuçları tabloda verilmiştir.\nAynı sıcaklıkta [A] = 0,30 mol/L ve [B] = 0,20 mol/L olan bir karışımda tepkimenin başlangıç hızı kaç mol/L·s olur?',
 dogru=ans6,yan=[(cand[0],'Mertebeleri yanlış bulup B’yi birinci mertebe almış (r = k[A][B]).','bilgi'),(cand[1],'A’yı ikinci, B’yi birinci mertebe almış; mertebeleri yer değiştirmiş.','dikkat'),(cand[2],'A’nın hıza etkisini hiç hesaba katmamış (r = k[B]²).','bilgi'),(cand[3],'Her iki madde için de mertebeyi 2 almış (r = k[A]²[B]²).','bilgi')],
 istenen='Yeni derişimlerdeki başlangıç hızı (mol/L·s).',ip=['Önce hız denklemini iki ayrı deney çiftiyle bul, sonra bir deneyden k’yı hesapla.'],
 bilgi=[B('Hız denklemi ve hız sabiti','r = k[A]ᵐ[B]ⁿ denkleminde mertebeler deneylerden, k ise bir deneyin verileri yerine konarak bulunur; k sıcaklık sabitken değişmez. Örnek: r = k[X]² için [X] = 0,5 mol/L’de hız 0,2 ise k = 0,2 ÷ 0,25 = 0,8’dir')],
 ad=[A('A’nın mertebesi','1. ve 2. deneyde [B] sabit.','[A] 2 kat → hız 2 kat → m = 1'),A('B’nin mertebesi','2. ve 3. deneyde [A] sabit.','[B] 3 kat → hız 9 kat → 3ⁿ = 9 → n = 2'),A('k’yı hesapla','1. deneyin verileri r = k[A][B]² denkleminde yerine konur.','2,0 × 10⁻³ = k × 0,10 × 0,10² → k = 2,0'),A('Yeni hızı bul','Verilen derişimler denkleme yazılır.','r = 2 × 0,30 × 0,20² = 0,024 mol/L·s')],
 puf='Önce mertebeleri, sonra k’yı bul; hız hesabı için tam hız denklemini kullan.')

# ================= 07 · derişim–zaman · orta · öncüllü =================
kartla('07','Derişim–zaman grafiğini yorumlama','Eğimin mutlak değeri hızdır; zamanla derişim azaldıkça hız azalır; iki grafik aynı zaman aralığında kıyaslanır.','Hızın zamanla sabit kaldığını sanmak; ortalama hızı yanlış aralıkta hesaplamak.','orta','grafik',3,'faktor','Derişim–zaman grafiği yorumu')
t=[0,10,20,30]; f1=lambda x:Fr(1,5)+Fr(4,5)*Fr(1,2)**Fr(x,10); f2=lambda x:Fr(1,10)+Fr(9,10)*Fr(1,3)**Fr(x,10)
c1=[Fr(1),Fr(3,5),Fr(2,5),Fr(3,10)]; c2=[Fr(1),Fr(2,5),Fr(1,5),Fr(2,15)]
assert [f1(x) for x in (0,10,20,30)]==c1 and [f2(x) for x in (0,10,20,30)]==c2
v1_010=(c1[0]-c1[1])/10; v2_010=(c2[0]-c2[1])/10; v1_020=(c1[0]-c1[2])/20; v2_1020=(c2[1]-c2[2])/10
assert v2_010>v1_010 and v1_020==Fr(3,100) and v2_1020<v2_010
tr7={1:False,2:True,3:False}
def curve(c,style):
    fn=f1 if c is c1 else f2
    pts=' '.join(f'({tt*.14:.3f},{float(fn(tt))*4:.3f})' for tt in range(0,31,2))
    return f'\\draw[{style}] plot[smooth,tension=.7] coordinates {{{pts}}};'
g='\\draw[thick,-{Stealth}] (0,0) -- (0,4.5); \\draw[thick,-{Stealth}] (0,0) -- (4.9,0);'
g+='\\node[rotate=90,anchor=south] at (-1.2,2.1) {[A] (mol/L)}; \\node[anchor=north] at (2.1,-.35) {Zaman (s)};'
for tt in t: g+=f'\\draw[thick] ({tt*.14:.3f},-.07) -- ({tt*.14:.3f},.07); \\node[below] at ({tt*.14:.3f},-.05) {{{tt}}};'
for v in (0,.2,.4,.6,.8,1.0): g+=f'\\draw[thick] (-.07,{v*4:.3f}) -- (.07,{v*4:.3f}); \\node[left] at (-.1,{v*4:.3f}) {{{str(v).replace(".",",")}}};'
g+=curve(c1,'very thick')+curve(c2,'very thick,dashed')
g+='\\draw[very thick] (3.2,3.9) -- (3.8,3.9); \\node[right] at (3.85,3.9) {Deney 1}; \\draw[very thick,dashed] (3.2,3.4) -- (3.8,3.4); \\node[right] at (3.85,3.4) {Deney 2};'
SK7=tk(g)
s7=sirala('Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III')
d7,y7=onc(tr7,s7,{1:'eğimi daha dik olan eğrinin başlangıçtaki hızını hesaba katmayıp Deney 1’i daha hızlı sanmış',3:'zamanla derişim azaldığında hızın arttığını düşünmüş'},{2:'ortalama hızı derişim değişimini süreye bölmek yerine süreyle çarpmış ya da yanlış aralığı almış'})
q('0007',tipId='hz-faktor',tip='Derişim–zaman grafiği yorumu',z='orta',alt='Tepkime Hızları',kaz='A maddesinin derişim–zaman grafiklerinden ortalama hızları karşılaştırır.',kalip='grafik',
 kart='K-AKHZ-07 (derişim–zaman grafiği) · iki deneyin karşılaştırılması',sekil=SK7,
 metin='Aynı hacimli kapalı iki kapta başlangıç derişimleri eşit olan A(g) maddesi, farklı koşullarda ürüne dönüştürülüyor. Deney 1 ve Deney 2’de A’nın derişiminin zamanla değişimi şekilde verilmiştir.\nI. İlk 10 saniyede A’nın ortalama harcanma hızı Deney 1’de Deney 2’dekinden büyüktür.\nII. Deney 1’de 0–20 saniye aralığında A’nın ortalama harcanma hızı 0,03 mol/L·s’dir.\nIII. Deney 2’de 10–20 saniye aralığındaki ortalama hız, 0–10 saniye aralığındakinden büyüktür.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=d7,sira=s7,yan=y7,istenen='Doğru olan yargılar.',ip=['Her aralıkta derişim değişimini okuyup süreye böl; hızın zamanla nasıl değiştiğine dikkat et.'],
 bilgi=[B('Grafikten ortalama hız','derişim–zaman grafiğinde iki an arasındaki ortalama hız, derişim değişiminin süreye oranıdır. Tepkime ilerledikçe girenlerin derişimi azaldığı için eğim yataylaşır, yani hız düşer. Örnek: 5 saniyede 0,5 mol/L düşen madde için ortalama hız 0,1 mol/L·s’dir')],
 ad=[A('I’i hesapla','0–10 s için iki deneyde derişim düşüşünü karşılaştır.','Deney 1: 0,4 ÷ 10 = 0,04 · Deney 2: 0,6 ÷ 10 = 0,06 → I yanlış'),A('II’yi hesapla','Deney 1’de 0–20 s aralığı.','(1,0 − 0,4) ÷ 20 = 0,03 mol/L·s → II doğru'),A('III’ü hesapla','Deney 2’de iki aralık.','0–10: 0,06 · 10–20: 0,02 → III yanlış'),A('Sonuç','Yalnız II doğrudur.','Yalnız II')],
 puf='Eğri yataylaştıkça hız azalır; ortalama hız için ilgili aralığın derişim farkını süreye böl.')

# ================= 08 · hız–derişim grafiği · orta =================
kartla('08','Hız–derişim grafiğinde birinci mertebe','Başlangıç noktasından geçen doğru birinci mertebeyi gösterir; eğim k’dır.','Doğrusal grafiği derişimle hızın sabit olduğu sanmak; tepkime hızını maddenin hızı sanmak.','orta','grafik',3,'denklem','Hız–derişim grafiği ve katsayı')
kk=Fr(1,20); assert kk*Fr(1,5)==Fr(1,100) and kk*Fr(4,5)==Fr(4,100)
rate04=kk*Fr(2,5); vA8=2*rate04; assert rate04==Fr(2,100) and vA8==Fr(4,100)
g='\\draw[thick,-{Stealth}] (0,0) -- (0,4.4); \\draw[thick,-{Stealth}] (0,0) -- (5.2,0);'
g+='\\node[rotate=90,anchor=south] at (-1.15,2.1) {Tepkime hızı ($10^{-3}$ mol/L$\\cdot$s)}; \\node[anchor=north] at (2.5,-.4) {[A] (mol/L)};'
for v in (0,.2,.4,.6,.8): g+=f'\\draw[thick] ({v*5.5:.3f},-.07) -- ({v*5.5:.3f},.07); \\node[below] at ({v*5.5:.3f},-.05) {{{str(v).replace(".",",")}}};'
for h in (10,20,30,40): g+=f'\\draw[thick] (-.07,{h*.1:.3f}) -- (.07,{h*.1:.3f}); \\node[left] at (-.1,{h*.1:.3f}) {{{h}}};'
g+=f'\\draw[very thick] (0,0) -- ({.8*5.5:.3f},4.0);'
for a,h in ((.2,10),(.8,40)):
    g+=f'\\draw[dashed] ({a*5.5:.3f},0) -- ({a*5.5:.3f},{h*.1:.3f}) -- (0,{h*.1:.3f}); \\fill ({a*5.5:.3f},{h*.1:.3f}) circle (.07);'
SK8=tk(g)
q('0008',tipId='hz-denklem',tip='Hız–derişim grafiği ve katsayı',z='orta',alt='Hız Denklemi',kaz='Hız–derişim grafiğinden mertebeyi ve hız sabitini bularak maddenin harcanma hızını hesaplar.',kalip='grafik',
 kart='K-AKHZ-08 (hız–derişim grafiği) · 2A → B',sekil=SK8,
 metin='Sabit sıcaklıkta gerçekleşen 2A(g) → B(g) tepkimesinde tepkime hızının A’nın derişimine bağlı değişimi şekilde verilmiştir.\nBuna göre [A] = 0,40 mol/L olduğu anda A’nın harcanma hızı kaç mol/L·s’dir?',
 dogru=vA8,yan=[(Fr(1,100),'[A] = 0,20 mol/L değerindeki hızı okumuş.','dikkat'),(Fr(2,100),'Tepkime hızını A’nın harcanma hızı sanmış; 2 katsayısını hesaba katmamış.','bilgi'),(Fr(1,20),'Hız yerine hız sabitinin (k) değerini yazmış.','bilgi'),(Fr(8,100),'A’nın hızını bulduktan sonra 2 katsayısını bir kez daha uygulamış.','islem')],
 istenen='A’nın harcanma hızı (mol/L·s).',ip=['Grafiğin doğrusal ve orijinden geçtiğine dikkat et; noktalardan yararlanarak 0,40 mol/L için tepkime hızını bul.'],
 bilgi=[B('Hız–derişim grafiği','hız–derişim grafiği orijinden geçen doğruysa tepkime o maddeye göre birinci mertebedendir ve eğim hız sabitidir (r = k[A]). Bir maddenin hızı, tepkime hızı ile katsayısının çarpımıdır. Örnek: katsayısı 3 olan maddenin hızı tepkime hızının 3 katıdır')],
 ad=[A('Mertebeyi belirle','Doğru orijinden geçiyor; hız derişimle orantılı.','r = k[A]'),A('Tepkime hızı','[A] = 0,40 mol/L için doğrusal ilişkiyi kullan.','0,20 → 10 × 10⁻³ ise 0,40 → 20 × 10⁻³ = 0,02 mol/L·s'),A('A’nın hızı','Katsayı 2 olduğundan A tepkime hızının 2 katı hızla harcanır.','v(A) = 2 × 0,02 = 0,04 mol/L·s')],
 puf='Tepkime hızını grafikten bul, maddenin hızı için katsayısıyla çarp.')

# ================= 09 · mekanizma · orta =================
kartla('09','Mekanizma ve yavaş basamak','Hız denklemi yavaş basamaktan yazılır; her iki basamakta da görünen ve net tepkimede olmayan tür ara üründür, yeniden oluşan tür katalizördür.','Hız denklemini net tepkimeden yazmak; ara ürünle katalizörü karıştırmak.','orta','düz',4,'mekanizma','Mekanizma, ara ürün ve katalizör')
s9=['Net tepkime 2H₂O₂ → 2H₂O + O₂; hız = k[H₂O₂][I⁻]; I⁻ katalizördür','Net tepkime 2H₂O₂ → 2H₂O + O₂; hız = k[H₂O₂]²; I⁻ katalizördür',
    'Net tepkime 2H₂O₂ → 2H₂O + O₂; hız = k[H₂O₂][I⁻]; IO⁻ katalizördür','Net tepkime H₂O₂ → H₂O + O₂; hız = k[H₂O₂][I⁻]; I⁻ ara üründür','Net tepkime 2H₂O₂ → 2H₂O + O₂; hız = k[H₂O₂]²[I⁻]; IO⁻ ara üründür']
q('0009',tipId='hz-mekanizma',tip='Mekanizma, ara ürün ve katalizör',z='orta',alt='Tepkime Mekanizması',kaz='Çok basamaklı tepkimede yavaş basamaktan hız denklemini yazar; ara ürün ve katalizörü ayırt eder.',kalip='düz',
 kart='K-AKHZ-09 (mekanizma) · H₂O₂ bozunması, I⁻ katalizörü',
 metin='H₂O₂’nin sulu çözeltide I⁻ iyonları varlığında bozunması aşağıdaki iki basamakta gerçekleşir.\n1. basamak (yavaş): H₂O₂ + I⁻ → H₂O + IO⁻\n2. basamak (hızlı): H₂O₂ + IO⁻ → H₂O + O₂ + I⁻\nBuna göre aşağıdakilerden hangisi doğrudur?',
 dogru=s9[0],sira=yer(s9[0],s9[1:],4),
 yan=[(s9[1],'Hız denklemini girenlerin katsayılarından (2H₂O₂) yazmış; yavaş basamakta I⁻’nin de bulunduğunu görmemiş.','bilgi'),(s9[2],'Katalizörle ara ürünün rollerini ters yazmış; 2. basamakta yeniden oluşan türü ara ürün sanmış.','bilgi'),(s9[3],'Basamakları toplarken katsayıları denkleştirmemiş; I⁻’yi ara ürün saymış.','islem'),(s9[4],'Hız denklemini iki basamağın tüm girenlerinden kurmuş; yalnız yavaş basamak hızı belirler.','bilgi')],
 istenen='Doğru ifade.',ip=['Net tepkimeyi bulmak için iki basamağı topla; hız denklemini ise hızı belirleyen basamaktan yaz.'],
 bilgi=[B('Mekanizma','tepkime birden çok basamakta gerçekleşiyorsa en yavaş basamak hızı belirler ve hız denklemi bu basamaktaki girenlerden yazılır. Önce oluşup sonra harcanan tür ara üründür; harcanıp sonra yeniden oluşan tür katalizördür. Örnek: A + B → C (yavaş), C + A → D (hızlı) mekanizmasında C ara üründür, hız = k[A][B]')],
 ad=[A('Net tepkimeyi bul','İki basamağı topla, ortak türleri sadeleştir.','2H₂O₂ + I⁻ + IO⁻ → 2H₂O + O₂ + IO⁻ + I⁻ → 2H₂O₂ → 2H₂O + O₂'),A('Ara ürün ve katalizör','I⁻ önce harcanıp sonra yeniden oluşuyor; IO⁻ oluşup harcanıyor.','I⁻: katalizör · IO⁻: ara ürün'),A('Hız denklemi','Yavaş basamak 1. basamaktır.','hız = k[H₂O₂][I⁻]'),A('Seçeneği belirle','Üç bilgiyi bir arada taşıyan seçenek doğrudur.','2H₂O₂ → 2H₂O + O₂ · k[H₂O₂][I⁻] · I⁻ katalizör')],
 puf='Hız denklemi daima yavaş basamaktan yazılır; her iki basamakta da görünüp net denklemde olmayan tür ara üründür.')

# ================= 10 · iki basamaklı enerji diyagramı · zor · öncüllü =================
kartla('10','İki basamaklı enerji diyagramı','En büyük aktivasyon enerjili basamak hızı belirler; net ΔH ürün–giren farkıdır; ara ürün vadide yer alır.','Basamağın Ea’sını sıfırdan okumak; net ΔH ile basamak ΔH’sini karıştırmak.','orta','öncüllü',5,'enerji','İki basamaklı tepkimede enerji diyagramı')
R,TS1,IM,TS2,PR=20,70,40,100,10
Ea1=TS1-R; Ea2=TS2-IM; dH=PR-R
assert Ea1==50 and Ea2==60 and dH==-10 and Ea2>Ea1
tr10={1:True,2:True,3:False}   # I ekzotermik · II hız belirleyen 2. basamak · III 2. basamağın ileri Ea'sı 80 (yanlış: 60)
sc=.04
pts=[(0,R),(.8,R),(2.0,TS1),(3.2,IM),(3.8,IM),(5.0,TS2),(6.2,PR),(7.0,PR)]
g=pe_axes(110,[10,20,40,70,100],7.2,sc)+pe_path(pts,sc,'very thick')
for yv in (10,20,40,70,100): g+=guide(yv,{10:6.2,20:.8,40:3.2,70:2.0,100:5.0}[yv],sc)
g+=f'\\node[above] at (.4,{R*sc+.05:.3f}) {{A}}; \\node[above] at (3.5,{IM*sc+.05:.3f}) {{B}}; \\node[above] at (6.6,{PR*sc+.05:.3f}) {{C}};'
SK10=tk(g)
s10=sirala('Yalnız III','I ve II','I ve III','II ve III','I, II ve III')
d10,y10=onc(tr10,s10,{3:'ürünlerin enerjisinden girenlerinkini çıkarmak yerine tersini yaparak ΔH’yi +10 kJ bulmuş'},
 {1:'B’nin vadide oluşup sonraki basamakta harcandığını görmemiş',2:'en yüksek tepeyi değil ilk tepeyi hız belirleyen sanmış'})
q('0010',tipId='hz-enerji',tip='İki basamaklı tepkimede enerji diyagramı',z='orta',alt='Aktivasyon Enerjisi',kaz='İki basamaklı tepkimenin enerji diyagramından ara ürünü, ΔH’yi ve hız belirleyen basamağı yorumlar.',kalip='öncüllü',
 kart='K-AKHZ-10 (iki basamaklı diyagram) · A → B → C',sekil=SK10,
 metin='A → C tepkimesi, B ara ürünü üzerinden iki basamakta gerçekleşmektedir. Tepkimenin potansiyel enerji–tepkime koordinatı grafiği şekilde verilmiştir.\nI. B ara üründür.\nII. Tepkime hızını ikinci basamak belirler.\nIII. Tepkimenin net entalpi değişimi (ΔH) +10 kJ’dir.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=d10,sira=s10,yan=y10,istenen='Doğru olan yargılar.',ip=['Her basamağın aktivasyon enerjisini, o basamağın başladığı düzeyden tepe noktasına olan yükseklik olarak bul.'],
 bilgi=[B('İki basamaklı tepkimede enerji','her basamağın aktivasyon enerjisi o basamağın başlangıç düzeyinden tepe noktasına olan farktır; aktivasyon enerjisi en büyük basamak yavaştır ve hızı belirler. Net ΔH, ürünlerin enerjisinden girenlerin enerjisinin çıkarılmasıyla bulunur. Örnek: 10 kJ’den 25 kJ’e çıkan bir basamak için Ea = 15 kJ’dir')],
 ad=[A('Basamak Ea’larını bul','Her basamak kendi başlangıç düzeyinden okunur.','1. basamak: 70 − 20 = 50 kJ · 2. basamak: 100 − 40 = 60 kJ'),A('Hız belirleyeni seç','Ea’sı büyük olan basamak yavaştır.','60 > 50 → 2. basamak hızı belirler → II doğru'),A('Ara ürün','B, ilk basamakta oluşup ikinci basamakta harcanan vadi düzeyidir.','B ara üründür → I doğru'),A('Net ΔH’yi bul','Ürünler 10 kJ, girenler 20 kJ düzeyinde.','ΔH = 10 − 20 = −10 kJ → III yanlış (I ve II doğru)')],
 puf='Her basamağın aktivasyon enerjisini kendi başlangıç düzeyinden tepeye ölç ve karşılaştır.')

# ================= 11 · katalizör · orta · yanlış kök =================
kartla('11','Katalizörün enerji diyagramındaki etkisi','Katalizör aktivasyon enerjisini ileri ve geri yönde eşit miktarda düşürür; ΔH değişmez.','Katalizörün ΔH’yi değiştirdiğini sanmak.','orta','grafik',3,'katalizor','Katalizörün enerji diyagramına etkisi')
Rr,Pp,UP,CP=40,20,100,70
assert UP-Rr==60 and CP-Rr==30 and UP-Pp==80 and CP-Pp==50 and Pp-Rr==-20
sc=.032
g=pe_axes(110,[20,40,70,100],6.2,sc)+pe_path([(0,Rr),(.8,Rr),(3.0,UP),(5.2,Pp),(6.0,Pp)],sc,'very thick')+pe_path([(0,Rr),(.8,Rr),(3.0,CP),(5.2,Pp),(6.0,Pp)],sc,'very thick,dashed')
for yv,x in ((40,.8),(20,5.2),(70,3.0),(100,3.0)): g+=guide(yv,x,sc)
g+=f'\\draw[very thick] (4.2,{105*sc:.3f}) -- (4.8,{105*sc:.3f}); \\node[right] at (4.85,{105*sc:.3f}) {{Katalizörsüz}}; \\draw[very thick,dashed] (4.2,{93*sc:.3f}) -- (4.8,{93*sc:.3f}); \\node[right] at (4.85,{93*sc:.3f}) {{Katalizörlü}};'
SK11=tk(g)
s11=['Katalizörsüz ileri tepkimenin aktivasyon enerjisi 60 kJ’dir.','Katalizör geri tepkimenin aktivasyon enerjisini 30 kJ azaltmıştır.','Katalizör kullanılması tepkime entalpisini −20 kJ’den −50 kJ’e düşürmüştür.','Katalizörlü yolda geri tepkimenin aktivasyon enerjisi 50 kJ’dir.','Tepkime ekzotermiktir ve ΔH değeri −20 kJ’dir.']
q('0011',tipId='hz-katalizor',tip='Katalizörün enerji diyagramına etkisi',z='orta',alt='Katalizör',kaz='Katalizörlü ve katalizörsüz yolların enerji diyagramından aktivasyon enerjisi ve ΔH değişimini yorumlar.',kalip='grafik',
 kart='K-AKHZ-11 (katalizör ve diyagram) · tek basamaklı tepkime',sekil=SK11,
 metin='Bir tepkimenin katalizörsüz ve katalizörlü gerçekleştiği iki yol için potansiyel enerji–tepkime koordinatı grafiği şekilde verilmiştir.\nBuna göre bu tepkimeyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=s11[2],sira=yer(s11[2],[s11[0],s11[1],s11[3],s11[4]],3),
 yan=[(s11[0],'Doğru bir ifadeyi yanlış sanmış: ileri aktivasyon enerjisinin girenlerin düzeyinden (100 − 40) hesaplandığını görmemiş.','dikkat'),(s11[1],'Katalizörün yalnız ileri yönü etkilediğini düşünmüş; tepe 30 kJ alçaldığı için geri Ea da 30 kJ azalır.','bilgi'),(s11[3],'Katalizörlü yolun tepe noktasını (70) ürünlerin düzeyinden (20) ölçmeyi yanlış sanmış.','dikkat'),(s11[4],'Ürünlerin enerjisinin girenlerinkinden düşük olduğunu görmeyip ekzotermik ifadesini yanlış saymış.','dikkat')],
 istenen='Yanlış olan ifade.',ip=['Her ifadeyi ilgili düzeylerin farkı olarak yeniden hesapla ve katalizörün neyi değiştirip neyi değiştirmediğini düşün.'],
 bilgi=[B('Katalizör','tepkimenin başka, daha düşük enerjili bir yoldan gerçekleşmesini sağlar; ileri ve geri aktivasyon enerjisini aynı miktarda azaltır. Girenlerin ve ürünlerin enerjisi değişmediğinden ΔH değişmez, denge kurulmuşsa dengeyi de kaydırmaz. Örnek: tepe 15 kJ alçalırsa ileri ve geri Ea da 15 kJ azalır')],
 ad=[A('Düzeyleri oku','Girenler 40, ürünler 20, katalizörsüz tepe 100, katalizörlü tepe 70 kJ.','R = 40 · P = 20 · 100 / 70'),A('Aktivasyon enerjileri','Her yolda tepeden ilgili düzeyin farkı alınır.','ileri: 60 → 30 · geri: 80 → 50'),A('ΔH’yi bul','Katalizör girenlerin ve ürünlerin düzeyini değiştirmez.','ΔH = 20 − 40 = −20 kJ'),A('Yanlış ifadeyi seç','ΔH’nin −50 kJ olması mümkün değildir.','−20 → −50 ifadesi yanlış')],
 puf='Her ifadeyi ilgili iki düzeyin farkı olarak yaz ve grafikten oku.')

# ================= 12 · kinetik enerji dağılımı · orta · öncüllü =================
kartla('12','Kinetik enerji dağılımı ve sıcaklık','Sıcaklık artınca eşik enerjisini aşan tanecik oranı artar; eşik enerjisi değişmez.','Eşik enerjisinin sıcaklıkla değiştiğini sanmak; eğri altındaki alanı farklı sanmak.','orta','öncüllü',3,'sicaklik','Sıcaklığın kinetik enerji dağılımına etkisi')
def dens(E,th): return math.sqrt(E)*math.exp(-E/th)/(math.gamma(1.5)*th**1.5)
def tail(Ea,th):
    n=4000; hi=40; h=(hi-Ea)/n
    return sum(dens(Ea+(i+.5)*h,th) for i in range(n))*h
th1,th2,Ea12=1.0,1.8,3.0
assert tail(Ea12,th2)>tail(Ea12,th1)
for th in (th1,th2): assert abs(tail(0,th)-1)<2e-3
SXc=.8; SYc=6.0
def dcurve(th,style):
    pts=' '.join(f'({E*SXc:.3f},{dens(E,th)*SYc:.3f})' for E in [0,.05,.1,.2,.3,.4,.5,.6,.8,1,1.2,1.4,1.7,2,2.4,2.8,3.2,3.6,4,4.5,5,5.6,6.2,7,8])
    return f'\\draw[{style}] plot[smooth] coordinates {{{pts}}};'
g='\\draw[thick,-{Stealth}] (0,0) -- (0,3.8); \\draw[thick,-{Stealth}] (0,0) -- (7.2,0);'
g+='\\node[rotate=90,anchor=south] at (-.15,1.9) {Tanecik sayısı}; \\node[anchor=north] at (3.6,-.1) {Kinetik enerji};'
g+=dcurve(th1,'very thick')+dcurve(th2,'very thick,dashed')
g+=f'\\draw[thick,dotted] ({Ea12*SXc:.3f},0) -- ({Ea12*SXc:.3f},3.2); \\node[above] at ({Ea12*SXc:.3f},3.2) {{$E_a$}};'
g+='\\draw[very thick] (4.6,3.4) -- (5.2,3.4); \\node[right] at (5.25,3.4) {$T_1$}; \\draw[very thick,dashed] (4.6,2.9) -- (5.2,2.9); \\node[right] at (5.25,2.9) {$T_2$};'
SK12=tk(g)
tr12={1:True,2:False,3:True}
s12=sirala('Yalnız II','Yalnız III','I ve II','I ve III','II ve III')
d12,y12=onc(tr12,s12,{2:'sıcaklık artınca eşik enerjisinin de değiştiğini sanmış (eşik enerjisi yalnız yolu değiştirince değişir)'},{1:'daha yassı ve sağa kaymış eğriyi düşük sıcaklığa ait sanmış',3:'eşik enerjisinin sağındaki alanın iki eğri için aynı olduğunu düşünmüş'})
q('0012',tipId='hz-sicaklik',tip='Sıcaklığın kinetik enerji dağılımına etkisi',z='orta',alt='Hızı Etkileyen Faktörler',kaz='Kinetik enerji dağılım grafiğinden sıcaklığın etkin çarpışma oranına etkisini yorumlar.',kalip='öncüllü',
 kart='K-AKHZ-12 (enerji dağılımı) · T₁ ve T₂ eğrileri',sekil=SK12,
 metin='Aynı miktarda gaz örneğinin iki farklı sıcaklıkta (T₁ ve T₂) bulunan tanecikleri için kinetik enerji dağılımı ve tepkimenin eşik enerjisi (Eₐ) şekilde gösterilmiştir. Grafik ölçeksiz çizilmiştir.\nI. T₂ sıcaklığı T₁ sıcaklığından yüksektir.\nII. Tepkimenin eşik enerjisi T₂ sıcaklığında, T₁ sıcaklığındakinden küçüktür.\nIII. Eₐ değerinden büyük kinetik enerjili tanecik oranı T₂ sıcaklığında daha fazladır.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=d12,sira=s12,yan=y12,istenen='Doğru olan yargılar.',ip=['Eğrinin yüksekliğini ve sağa kayışını, eşik enerjisinin sağında kalan alanla birlikte düşün.'],
 bilgi=[B('Kinetik enerji dağılımı','bir gaz örneğinde tanecikler farklı kinetik enerjilere sahiptir; sıcaklık artınca eğri yassılaşıp sağa kayar ve eşik enerjisini aşan tanecik oranı artar. Eşik enerjisi (aktivasyon enerjisi) ise sıcaklıkla değişmez. Örnek: sıcaklık artınca eğrinin eşik enerjisinin sağında kalan alanı büyür, etkin çarpışma sayısı artar')],
 ad=[A('Eğrileri karşılaştır','T₂ eğrisi daha alçak ve sağa kaymış.','T₂ > T₁ → I doğru'),A('Eşik enerjisi','Eₐ iki sıcaklık için de aynı çizgidir.','II yanlış'),A('Eşik enerjisinin sağı','T₂ eğrisinin Eₐ sağındaki alanı daha geniştir.','III doğru'),A('Sonuç','I ve III doğrudur.','I ve III')],
 puf='Sıcaklık eşik enerjisini değiştirmez; eşik enerjisini aşan tanecik oranını artırır.')

# ================= 13 · sıcaklık–hız ilişkisi · orta =================
kartla('13','Her 10 °C’de hızın katlanması','Hız ve tamamlanma süresi ters orantılıdır; sıcaklık farkı kaç basamağa bölünürse hız o kadar kez katlanır.','Süreyi hızla aynı yönde çarpmak; basamak sayısını yanlış bulmak.','orta','hikâyeli',3,'sicaklik','Sıcaklık artışında hız ve süre')
fac=3; steps=(50-20)//10; spd=fac**steps; tsure=Fr(81,spd); assert spd==27 and tsure==3
q('0013',tipId='hz-sicaklik',tip='Sıcaklık artışında hız ve süre',z='orta',alt='Hızı Etkileyen Faktörler',kaz='Sıcaklık artışının hıza etkisini kullanarak tamamlanma süresini hesaplar.',kalip='hikâyeli',
 kart='K-AKHZ-13 (sıcaklık ve süre) · her 10 °C’de 3 kat',
 metin='Bir laboratuvarda belli miktarda X maddesinin Y ile verdiği tepkime 20 °C’de 81 dakikada tamamlanmaktadır. Bu tepkimede sıcaklık her 10 °C arttığında tepkime hızı 3 katına çıkmaktadır. Diğer koşullar değişmemektedir.\nBuna göre aynı tepkime 50 °C’de kaç dakikada tamamlanır?',
 dogru=3,yan=[(1,'Sıcaklık farkını 10 °C’lik 4 basamak sayıp hızı 81 kat artırmış.','dikkat'),(9,'Yalnız 2 basamak almış (40 °C’ye kadar): 81 ÷ 9.','dikkat'),(27,'Hızın artış katını (27) tamamlanma süresi sanmış.','islem'),(243,'Hız arttığında sürenin de arttığını sanmış (81 × 3).','bilgi')],
 istenen='Tepkimenin 50 °C’deki tamamlanma süresi (dakika).',ip=['Önce hızın toplam kaç kat arttığını bul; süre hızla ters orantılıdır.'],
 bilgi=[B('Sıcaklık ve hız','sıcaklık artınca taneciklerin kinetik enerjisi ve etkin çarpışma sayısı artar, tepkime hızlanır. Aynı miktar maddenin tepkimeyi tamamlama süresi hızla ters orantılıdır. Örnek: hız 5 kat artarsa tamamlanma süresi 5 kat kısalır')],
 ad=[A('Basamak sayısı','Sıcaklık farkı 10 °C’lik kaç parçadır.','(50 − 20) ÷ 10 = 3'),A('Hızdaki artış','Her basamakta hız 3 kat artar.','3 × 3 × 3 = 27 kat'),A('Süre','Süre hızla ters orantılı olduğundan bölünür.','81 ÷ 27 = 3 dakika')],
 puf='Hız n kat artarsa süre n kat kısalır; basamak sayısını sıcaklık farkını 10’a bölerek bul.')

# ================= 14 · V–t grafiği · orta =================
kartla('14','Hacim–zaman grafiğiyle faktör belirleme','Aynı son hacimde yalnız eğim artmışsa hızı artıran, madde miktarını değiştirmeyen bir etken uygulanmıştır.','Madde miktarını artırmanın hızı artıracağını, ürün miktarını değiştirmeyeceğini sanmak.','orta','grafik',3,'faktor','Hacim–zaman grafiğiyle hız faktörü')
tau1,tau2=30,12
def vt(tau,tt): return 100*(1-math.exp(-tt/tau))
assert vt(tau2,60)>vt(tau1,60) and vt(tau1,150)>99
pts1=' '.join(f'({tt*.03:.3f},{vt(tau1,tt)*.04:.3f})' for tt in range(0,151,10)); pts2=' '.join(f'({tt*.03:.3f},{vt(tau2,tt)*.04:.3f})' for tt in range(0,151,10))
g='\\draw[thick,-{Stealth}] (0,0) -- (0,4.4); \\draw[thick,-{Stealth}] (0,0) -- (5.0,0);'
g+='\\node[rotate=90,anchor=south] at (-1.1,2.1) {H$_2$ hacmi (mL)}; \\node[anchor=north] at (2.3,-.4) {Zaman (s)};'
for tt in (0,50,100,150): g+=f'\\draw[thick] ({tt*.03:.3f},-.07) -- ({tt*.03:.3f},.07); \\node[below] at ({tt*.03:.3f},-.05) {{{tt}}};'
for v in (0,25,50,75,100): g+=f'\\draw[thick] (-.07,{v*.04:.3f}) -- (.07,{v*.04:.3f}); \\node[left] at (-.1,{v*.04:.3f}) {{{v}}};'
g+=f'\\draw[very thick] plot[smooth] coordinates {{{pts1}}}; \\draw[very thick,dashed] plot[smooth] coordinates {{{pts2}}};'
g+='\\draw[very thick] (3.1,1.5) -- (3.7,1.5); \\node[right] at (3.75,1.5) {Deney 1}; \\draw[very thick,dashed] (3.1,.95) -- (3.7,.95); \\node[right] at (3.75,.95) {Deney 2};'
SK14=tk(g)
s14=['Mg şerit miktarı artırılmıştır.','Mg şerit yerine aynı kütlede Mg tozu kullanılmıştır.','HCl çözeltisi seyreltilmiştir.','Tepkime ortamının sıcaklığı düşürülmüştür.','Aynı derişimdeki HCl çözeltisinin hacmi artırılmıştır.']
q('0014',tipId='hz-faktor',tip='Hacim–zaman grafiğiyle hız faktörü',z='orta',alt='Hızı Etkileyen Faktörler',kaz='Hacim–zaman grafiğinden tepkime hızını değiştiren etkeni belirler.',kalip='grafik',
 kart='K-AKHZ-14 (V–t grafiği ve faktör) · Mg + HCl',sekil=SK14,
 metin='Aşırı miktarda HCl çözeltisine belirli kütlede Mg şerit atılarak Mg(k) + 2HCl(suda) → MgCl₂(suda) + H₂(g) tepkimesi gerçekleştiriliyor ve çıkan H₂ gazının hacmi zamanla ölçülüyor (Deney 1). Deneyde yalnız bir değişiklik yapılarak elde edilen sonuç Deney 2 olarak aynı grafikte gösterilmiştir.\nBuna göre Deney 2’de aşağıdakilerden hangisi yapılmıştır?',
 dogru=s14[1],sira=yer(s14[1],[s14[0],s14[2],s14[3],s14[4]],3),
 yan=[(s14[0],'Mg miktarı artınca hızın arttığını düşünmüş; oysa miktar artarsa toplam H₂ hacmi de artardı.','bilgi'),(s14[2],'Derişimi azaltmanın hızı artıracağını sanmış; seyreltme hızı azaltır.','bilgi'),(s14[3],'Sıcaklık değişimini ters yorumlamış; sıcaklık düşünce hız azalır.','bilgi'),(s14[4],'Hacmin artmasını derişimin artması sanmış; derişim aynı kaldığı için hız değişmez.','dikkat')],
 istenen='Deney 2’de yapılan değişiklik.',ip=['İki eğrinin son noktasını ve eğimlerini kıyasla; toplam gaz miktarını değiştiren etkenler elenmeli.'],
 bilgi=[B('Hızı etkileyen faktörler','temas yüzeyinin artması (parçalama), derişim artışı, sıcaklık artışı ve katalizör hızı artırır. Madde miktarı artarsa ürün miktarı artar ama derişim değişmediği için birim zamandaki hız aynı kalır. Örnek: kesme şeker yerine toz şeker daha hızlı çözünür')],
 ad=[A('Son hacmi karşılaştır','İki eğri de aynı hacimde sabitleniyor.','Toplam H₂ hacmi aynı → Mg miktarı aynı'),A('Eğimi karşılaştır','Deney 2’nin eğimi daha diktir.','Hız Deney 2’de daha büyük'),A('Etkenleri ele','Seyreltme, sıcaklık düşürme ve hacim artırma hızı artırmaz.','Hızı artıran: temas yüzeyi'),A('Sonuç','Aynı kütlede toz Mg yüzeyi artırır.','Mg tozu kullanılmıştır')],
 puf='Son hacim aynıysa madde miktarı sabittir; yalnız hızı değiştiren etkeni seç.')

# ================= 15 · hız denklemi ve gaz hacmi · zor =================
kartla('15','Mertebe ve hacim değişiminin birlikte etkisi','Hacim küçülünce gazın derişimi artar; yeni hız derişim oranlarının mertebe kuvvetlerinin çarpımıdır.','Hacim değişimini hıza doğrudan katmak; mol sayısı artışını derişim artışı gibi kullanmak.','zor','düz',4,'denklem','Hız denklemi ve hacim–mol değişimi')
bX,bY=2,1
fA=Fr(2)*1; fB=Fr(2)*3  # hacim yarı (×2), B molü ×3
ans15=fA**bX*fB**bY
assert ans15==24
def r15(a,b,fa=fA,fb=fB): return fa**a*fb**b
c15=[Fr(2)**3,r15(1,1),r15(1,2),r15(2,2)]
assert c15==[8,12,72,144] and len(set(c15+[ans15]))==5
q('0015',tipId='hz-denklem',tip='Hız denklemi ve hacim–mol değişimi',z='zor',alt='Hız Denklemi',kaz='Deneysel verilerle mertebeyi bulup hacim ve mol değişiminin birlikte hıza etkisini hesaplar.',kalip='düz',
 kart='K-AKHZ-15 (hız denklemi ve hacim) · A(g) + B(g)',
 metin='A(g) + B(g) → ürün tepkimesinin hız denklemini belirlemek için sabit sıcaklıkta şu deney sonuçları elde edilmiştir.\n• B’nin derişimi sabit tutulup A’nın derişimi 2 katına çıkarıldığında tepkime hızı 4 katına çıkmıştır.\n• A’nın derişimi sabit tutulup B’nin derişimi 3 katına çıkarıldığında tepkime hızı 3 katına çıkmıştır.\nSabit sıcaklıkta A ve B gazlarının bulunduğu kabın hacmi yarıya düşürülürken aynı anda kaba sabit sıcaklıkta B gazından, kaptaki B’nin mol sayısını 3 katına çıkaracak kadar ekleniyor.\nBuna göre başlangıç tepkime hızı kaç katına çıkar?',
 dogru=24,yan=[(8,'B ilavesini dikkate almamış; yalnız hacmin yarıya inmesiyle hızın 2³ = 8 katına çıktığını bulmuş.','dikkat'),(12,'A’yı birinci mertebe almış: 2 × 6.','bilgi'),(72,'Mertebeleri ters yazmış: A birinci, B ikinci mertebe (2 × 6²).','bilgi'),(144,'Her iki madde için mertebeyi 2 almış (2² × 6²).','bilgi')],
 istenen='Başlangıç hızının kaç kat arttığı.',ip=['Önce her gazın derişiminin kaç katına çıktığını, sonra bu katları mertebeleriyle üslendirerek bul.'],
 bilgi=[B('Gazlarda hacim ve derişim','sabit sıcaklıkta kabın hacmi yarıya inerse bütün gazların derişimi 2 katına çıkar; ek gaz konulursa o gazın mol sayısıyla orantılı olarak derişimi artar. Hız denkleminde her derişimin kat sayısı mertebesiyle üslendirilir. Örnek: r = k[X]² ve [X] 3 katına çıkarsa hız 9 katına çıkar')],
 ad=[A('Mertebeleri bul','A’da 2 kat → 4 kat; B’de 3 kat → 3 kat.','2ᵐ = 4 → m = 2 · 3ⁿ = 3 → n = 1 · r = k[A]²[B]'),A('Derişim katlarını bul','Hacim yarıya inince derişim 2 kat; B’nin molü ayrıca 3 kat.','[A]: × 2 · [B]: × 2 × 3 = × 6'),A('Yeni hızı yaz','Katlar mertebeyle üslendirilir.','r′/r = 2² × 6¹'),A('Hesapla','Katsayıları çarp.','4 × 6 = 24 kat')],
 puf='Hacim değişimi bütün derişimleri aynı katlar; mol eklemek yalnız o maddenin derişimini artırır.')

# ================= 16 · hız sabiti · orta · olumsuz kök =================
kartla('16','Hız sabitinin bağlı olduğu etkenler','k yalnız sıcaklığa, katalizöre ve tepkimeye bağlıdır; derişim ve zamanla değişmez.','k’nın derişimle değiştiğini sanmak.','orta','düz',3,'denklem','Hız sabitinin özellikleri')
s16=['Sıcaklık değiştiğinde hız sabitinin değeri de değişir.','Hız sabitinin birimi tepkimenin derecesine göre değişir.','Katalizör kullanıldığında hız sabitinin değeri değişir.','Girenlerin derişimi değiştirildiğinde hız sabitinin değeri değişmez.','Tepkime ilerledikçe girenlerin derişimi azaldığı için hız sabiti de küçülür.']
q('0016',tipId='hz-denklem',tip='Hız sabitinin özellikleri',z='orta',alt='Hız Denklemi',kaz='Hız sabitinin bağlı olduğu etkenleri ve birimini yorumlar.',kalip='düz',
 kart='K-AKHZ-16 (hız sabiti) · k yargıları',
 metin='Bir tepkimenin hız denklemi r = k[A]ᵐ[B]ⁿ biçiminde yazılmaktadır ve tepkime sabit sıcaklıkta sabit hacimli bir kapta gerçekleştirilmektedir.\nBuna göre hız sabiti (k) ile ilgili aşağıdaki yargılardan hangisi yanlıştır?',
 dogru=s16[4],sira=yer(s16[4],[s16[3],s16[0],s16[1],s16[2]],0),
 yan=[(s16[0],'Sıcaklığın hız sabitine etkisi olmadığını düşünmüş; sıcaklık artınca k büyür.','bilgi'),(s16[1],'k’nın biriminin her tepkimede aynı olduğunu sanmış; birim dereceyle değişir.','bilgi'),(s16[2],'Katalizörün yalnız hızı değiştirip k’yı değiştirmediğini sanmış; katalizör k’yı büyütür.','bilgi'),(s16[3],'Derişimin k’yı etkilediğini düşünmüş; oysa k yalnız sıcaklığa ve katalizöre bağlıdır.','bilgi')],
 istenen='Yanlış olan yargı.',ip=['Hız sabitinin hangi etkenlere bağlı olduğunu ve zamanla değişip değişmediğini düşün.'],
 bilgi=[B('Hız sabiti','r = k[A]ᵐ[B]ⁿ denkleminde k, tepkimeye özgü bir sabittir; sıcaklığa ve katalizöre bağlıdır, derişime ve zamana bağlı değildir. k’nın birimi tepkimenin derecesine göre değişir. Örnek: aynı tepkime iki farklı sıcaklıkta farklı k değerine sahiptir')],
 ad=[A('Her yargıyı sına','k’nın bağlı olduğu etkenler sıcaklık ve katalizördür.','Sıcaklık → k değişir · katalizör → k değişir'),A('Derişim ve zaman','Derişim azalınca hız azalır, k azalmaz.','k sabittir'),A('Birim','Birim dereceye bağlıdır.','k’nın birimi derecesine göre değişir'),A('Yanlışı seç','Tepkime ilerledikçe k küçülmez.','Yanlış: k’nın küçüldüğü yargısı')],
 puf='Hız sabitinin hangi büyüklüklere bağlı olduğunu listele, her yargıyı bu listeyle sına.')

# ================= 17 · mekanizma şeması · zor · öncüllü =================
kartla('17','Mekanizma şeması: ara ürün, net tepkime ve hacim','Yavaş basamaktan hız denklemi yazılır; ara ürün net denklemde yoktur; hacim küçülünce gazların derişimi artar.','Hız denklemini net tepkimeden yazmak; hızdan bağımsız maddeyi hızı değiştiren sanmak.','zor','öncüllü',5,'mekanizma','Mekanizma şeması ve hız değişimi')
tr17={1:True,2:False,3:True}   # I: NO₃ ara ürün (doğru) · II: CO derişimi 2 katına çıkınca hız 2 katına (yanlış) · III: hacim yarıya, hız 4 kat (doğru)
assert Fr(2)**2==4
def box(x,y,t,w=3.1): return f'\\node[draw,thick,rounded corners=2pt,minimum width={w}cm,minimum height=.75cm,align=center] at ({x},{y}) {{{t}}};'
g=box(0,2.6,'\\ce{NO2 + NO2 -> NO3 + NO}',5.4)+'\\node[anchor=west] at (3.0,2.6) {1. basamak (yavaş)};'
g+=box(0,1.0,'\\ce{NO3 + CO -> NO2 + CO2}',5.4)+'\\node[anchor=west] at (3.0,1.0) {2. basamak (hızlı)};'
g+=f'\\draw[{ARR}] (0,2.15) -- (0,1.45);'
SK17=tk(g)
s17=sirala('Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III')
d17,y17=onc(tr17,s17,{2:'CO’yu hız denkleminde sanmış; CO yalnız hızlı basamakta yer aldığından hıza etkisi yoktur'},{1:'NO₃’ün hem oluşup hem harcandığını görmeyip ara ürün saymamış',3:'hız denkleminin NO₂’ye göre ikinci mertebe olduğunu ve hacim yarıya inince derişimin 2 katına çıktığını birleştirememiş'})
q('0017',tipId='hz-mekanizma',tip='Mekanizma şeması ve hız değişimi',z='zor',alt='Tepkime Mekanizması',kaz='Mekanizma şemasından ara ürünü, hız denklemini ve hacim değişiminin hıza etkisini yorumlar.',kalip='öncüllü',
 kart='K-AKHZ-17 (mekanizma şeması) · NO₂ + CO',sekil=SK17,
 metin='NO₂(g) ile CO(g) arasındaki tepkimenin mekanizması şekilde gösterilmiştir. Tepkime sabit sıcaklıkta kapalı bir kapta gerçekleşmektedir.\nI. NO₃ ara üründür.\nII. CO(g)’nin derişimi 2 katına çıkarılırsa tepkime hızı da 2 katına çıkar.\nIII. Kabın hacmi yarıya düşürülürse tepkime hızı 4 katına çıkar.\nBuna göre yukarıdaki yargılardan hangileri doğrudur?',
 dogru=d17,sira=s17,yan=y17,istenen='Doğru olan yargılar.',ip=['Hız denklemini yavaş basamaktan yaz; sonra her yargıdaki değişimin hangi derişimleri etkilediğine bak.'],
 bilgi=[B('Mekanizma ve hız','yavaş basamakta yer alan girenlerin derişimi hızı belirler; hızlı basamakta yer alıp yavaş basamakta bulunmayan madde hız denkleminde görünmez. Ara ürün bir basamakta oluşup sonraki basamakta harcanan türdür. Örnek: yavaş basamak A + B → C ise hız = k[A][B]’dir')],
 ad=[A('Ara ürünü bul','NO₃ ilk basamakta oluşuyor, ikincide harcanıyor.','NO₃ ara üründür → I doğru'),A('Hız denklemini yaz','Yavaş basamak 1. basamaktır; girenler yalnız NO₂.','hız = k[NO₂]²'),A('CO’nun etkisi','CO hız denkleminde yok.','CO derişimi 2 kat → hız değişmez → II yanlış'),A('Hacim değişimi','Hacim yarıya inince bütün derişimler 2 kat olur.','[NO₂] × 2 → hız × 2² = 4 kat → III doğru')],
 puf='Hız denklemini yalnız yavaş basamağın girenlerinden yaz; hızlı basamaktaki madde hızı etkilemez.')

# ================= 18 · derişim–zaman, iki eğri · zor =================
kartla('18','İki maddenin derişim–zaman grafiğinden tepkime hızı','Derişim değişim oranı katsayı oranını verir; tepkime hızı bir maddenin hızının katsayısına bölünmesiyle bulunur.','Eğriyi tanımadan hız hesaplamak; katsayıya bölmeyi unutmak; yanlış aralığı almak.','zor','grafik',5,'ifade','İki eğriden katsayı ve tepkime hızı')
fx=lambda x:Fr(1,5)+Fr(4,5)*Fr(1,2)**Fr(x,10)
X=[fx(0),fx(10),fx(20),fx(30)]; Yv=[(1-v)/2 for v in X]
assert X==[1,Fr(3,5),Fr(2,5),Fr(3,10)] and Yv==[0,Fr(1,5),Fr(3,10),Fr(7,20)]
for xx,yy in zip(X,Yv): assert (1-xx)==2*yy
rate18=(Yv[2]-Yv[1])/10; assert rate18==Fr(1,100) and (X[1]-X[2])/10==Fr(2,100)
alt=[Fr(1,200),rate18,Fr(2,100),Fr(3,100),Fr(4,100)]
assert Fr(1,100)/2==alt[0] and (X[1]-X[2])/10+(Yv[2]-Yv[1])/10==alt[3] and (X[0]-X[1])/10==alt[4]
cx=' '.join(f'({tt*.14:.3f},{float(fx(tt))*5:.3f})' for tt in range(0,31,2)); cy=' '.join(f'({tt*.14:.3f},{float((1-fx(tt))/2)*5:.3f})' for tt in range(0,31,2))
g='\\draw[thick,-{Stealth}] (0,0) -- (0,5.5); \\draw[thick,-{Stealth}] (0,0) -- (4.9,0);'
g+='\\node[rotate=90,anchor=south] at (-1.2,2.6) {Derişim (mol/L)}; \\node[anchor=north] at (2.1,-.35) {Zaman (s)};'
for tt in t: g+=f'\\draw[thick] ({tt*.14:.3f},-.07) -- ({tt*.14:.3f},.07); \\node[below] at ({tt*.14:.3f},-.05) {{{tt}}};'
for v in (0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0): g+=f'\\draw[thick] (-.07,{v*5:.3f}) -- (.07,{v*5:.3f}); \\node[left] at (-.1,{v*5:.3f}) {{{str(v).replace(".",",")}}};'
g+=f'\\draw[very thick] plot[smooth] coordinates {{{cx}}}; \\draw[very thick,dashed] plot[smooth] coordinates {{{cy}}};'
for tt,vx,vy in ((10,.6,.2),(20,.4,.3)):
    g+=f'\\draw[dotted] ({tt*.14:.3f},0) -- ({tt*.14:.3f},{vx*5:.3f}); \\fill ({tt*.14:.3f},{vx*5:.3f}) circle (.06); \\fill ({tt*.14:.3f},{vy*5:.3f}) circle (.06);'
g+='\\draw[very thick] (2.9,5.0) -- (3.5,5.0); \\node[right] at (3.55,5.0) {X(g)}; \\draw[very thick,dashed] (2.9,4.4) -- (3.5,4.4); \\node[right] at (3.55,4.4) {Y(g)};'
SK18=tk(g)
q('0018',tipId='hz-ifade',tip='İki eğriden katsayı ve tepkime hızı',z='zor',alt='Tepkime Hızları',kaz='Derişim–zaman grafiğindeki iki eğriden katsayı oranını bulup tepkime hızını hesaplar.',kalip='grafik',
 kart='K-AKHZ-18 (iki eğri, katsayı ve hız) · aX → bY',sekil=SK18,
 metin='Sabit hacimli kapalı bir kapta yalnız X(g) ve Y(g) arasında gerçekleşen tepkimede X ve Y’nin derişimlerinin zamanla değişimi şekilde verilmiştir. Tepkime en küçük tam sayılı katsayılarla yazılmıştır; X giren, Y ürün maddedir.\nBuna göre tepkimenin 10. saniye ile 20. saniye arasındaki ortalama hızı kaç mol/L·s’dir?',
 dogru=rate18,yan=[(alt[0],'Y’nin oluşma hızını X’in katsayısı olan 2’ye bölmüş.','islem'),(alt[2],'X’in harcanma hızını tepkime hızı sanmış; X’in katsayısına (2) bölmemiş.','bilgi'),(alt[3],'X’in harcanma hızı ile Y’nin oluşma hızını toplamış.','islem'),(alt[4],'İstenen aralık yerine 0–10 s aralığındaki X derişim değişimini (0,4) süreye bölmüş.','dikkat')],
 istenen='Tepkimenin 10–20 s arasındaki ortalama hızı (mol/L·s).',ip=['Önce iki eğrinin aynı sürede ne kadar değiştiğini karşılaştırarak katsayı oranını bul.'],
 bilgi=[B('Katsayı ve derişim değişimi','aA → bB tepkimesinde Δ[A] : Δ[B] = a : b’dir. Tepkime hızı r = −Δ[A]/(aΔt) = Δ[B]/(bΔt) ile bulunur. Örnek: bir madde diğerinden 3 kat fazla değişiyorsa katsayısı da 3 kat büyüktür')],
 ad=[A('Katsayı oranı','Aynı sürede X’in düşüşü Y’nin artışının 2 katıdır.','0. → 20. s: ΔX = 0,6 · ΔY = 0,3 → 2X → Y'),A('Aralıktaki değişim','10–20 s için Y’nin derişimi okunur.','Y: 0,2 → 0,3 → Δ[Y] = 0,1 mol/L'),A('Hızı hesapla','Y’nin katsayısı 1 olduğundan tepkime hızı Y’nin hızıdır.','r = 0,1 ÷ 10 = 0,01 mol/L·s'),A('Doğrula','X’in harcanma hızı r’nin 2 katıdır.','v(X) = (0,6 − 0,4) ÷ 10 = 0,02 = 2 × 0,01')],
 puf='Katsayı oranını eğrilerin toplam değişiminden bul; tepkime hızı için maddenin hızını katsayısına böl.')

# ================= 19 · kontrollü deney · orta · tablo =================
kartla('19','Kontrollü değişken ve deney seçimi','Bir etkenin etkisini görmek için yalnız o etkenin farklı, diğerlerinin aynı olduğu deney çifti seçilir.','Birden fazla etkeni değiştiren deneyleri kıyaslamak.','orta','tablo',3,'faktor','Kontrollü deney çifti seçimi')
exps=[('1',Fr(1,10),Fr(1,2),20),('2',Fr(1,5),Fr(1,2),20),('3',Fr(1,10),Fr(1),20),('4',Fr(1,5),Fr(1),40),('5',Fr(1,10),Fr(1,2),40)]
def fark(a,b): return sum(x!=y for x,y in zip(exps[a][1:],exps[b][1:]))
tek=[(a+1,b+1) for a in range(5) for b in range(a+1,5) if fark(a,b)==1]
assert [c for c in tek if exps[c[0]-1][2]!=exps[c[1]-1][2]]==[(1,3)] and fark(0,1)==1 and fark(0,4)==1 and fark(1,3)==2 and fark(3,4)==2
SK19=tablo_svg(['Deney','[Na₂S₂O₃] (mol/L)','[HCl] (mol/L)','Sıcaklık (°C)'],[[e[0],fm(e[1]),fm(e[2]),str(e[3])] for e in exps])
s19=['1 ve 2','1 ve 3','1 ve 5','2 ve 4','4 ve 5']
q('0019',tipId='hz-faktor',tip='Kontrollü deney çifti seçimi',z='orta',alt='Hızı Etkileyen Faktörler',kaz='Hızı etkileyen bir etkeni belirlemek için kontrollü deney çiftini seçer.',kalip='tablo',
 kart='K-AKHZ-19 (kontrollü deney) · Na₂S₂O₃ + HCl, beş deney',sekil=SK19,
 metin='Na₂S₂O₃(suda) + 2HCl(suda) → 2NaCl(suda) + S(k) + SO₂(g) + H₂O(s) tepkimesinde oluşan katı kükürt çözeltiyi bulandırmaktadır. Hızı etkileyen etkenleri incelemek için aynı hacimli çözeltilerle tabloda verilen beş deney yapılmıştır.\nBuna göre HCl derişiminin tepkime hızına etkisini incelemek için hangi iki deneyin sonuçları karşılaştırılmalıdır?',
 dogru='1 ve 3',sira=s19,
 yan=[(s19[0],'Na₂S₂O₃ derişiminin farklı olduğu çifti seçmiş; bu çift Na₂S₂O₃ derişiminin etkisini inceler.','dikkat'),(s19[2],'Sıcaklığın farklı olduğu çifti seçmiş; bu çift sıcaklığın etkisini inceler.','dikkat'),(s19[3],'HCl derişiminin farklı olduğu bir çift seçmiş ama sıcaklık da farklı; iki etken birlikte değişiyor.','bilgi'),(s19[4],'HCl derişiminin farklı olduğu bir çift seçmiş ama Na₂S₂O₃ derişimi de farklı; iki etken birlikte değişiyor.','bilgi')],
 istenen='HCl derişiminin etkisini inceleyen deney çifti.',ip=['İncelenen etken dışındaki bütün koşulları aynı olan iki deneyi ara.'],
 bilgi=[B('Kontrollü deney','bir etkenin hıza etkisini görmek için yalnız o etken değiştirilir, diğer koşullar sabit tutulur. Aksi hâlde hız farkının hangi etkenden geldiği anlaşılamaz. Örnek: ısı etkisi için iki deneyde yalnız sıcaklık farklı olmalıdır')],
 ad=[A('Koşulları listele','Tabloyu okuyup her deneyin iki derişimine ve sıcaklığına bak.','1: 0,1 · 0,5 · 20 °C ve 3: 0,1 · 1 · 20 °C'),A('HCl’yi ayır','Yalnız [HCl]’in farklı olduğu çiftleri ara.','1 ve 3: Na₂S₂O₃ derişimi ve sıcaklık aynı'),A('Diğer çiftleri ele','Öbür çiftlerde birden çok koşul farklı ya da başka etken değişiyor.','2 ve 4: HCl ve sıcaklık farklı · 4 ve 5: Na₂S₂O₃ ve HCl farklı'),A('Sonuç','Doğru çift 1 ve 3’tür.','1 ve 3')],
 puf='Etkisini incelediğin etken dışında hiçbir koşul farklı olmamalı.')

# ================= 20 · katalizörlü iki basamaklı yol · zor =================
kartla('20','Katalizörlü çok basamaklı yolda hız belirleyen Ea','Katalizörlü yolda en yüksek Ea’lı basamak hızı belirler; katalizörsüz yolla farkı katalizörün sağladığı azalmadır.','Katalizörlü tepenin en yükseğini tek aktivasyon enerjisi sanmak; Ea’yı girenlerden okumak.','zor','grafik',5,'katalizor','Katalizörlü yolda hız belirleyen basamak')
R20,P20,UP20=30,10,90; C1,CI,C2=60,40,50
e1=C1-R20; e2=C2-CI; assert e1==30 and e2==10 and e1>e2 and UP20-R20==60 and (UP20-R20)-e1==30
sc=.04
g=pe_axes(100,[10,30,40,50,60,90],7.0,sc)
g+=pe_path([(0,R20),(.5,R20),(3.0,UP20),(6.2,P20),(7.0,P20)],sc,'very thick')
g+=pe_path([(0,R20),(1.1,R20),(2.1,C1),(3.0,CI),(3.6,CI),(4.4,C2),(5.6,P20),(7.0,P20)],sc,'very thick,dashed')
for yv,x in ((10,5.6),(30,.5),(40,3.0),(50,4.4),(60,2.1),(90,3.0)): g+=guide(yv,x,sc)
g+=f'\\draw[very thick] (5.0,{96*sc:.3f}) -- (5.6,{96*sc:.3f}); \\node[right] at (5.65,{96*sc:.3f}) {{Katalizörsüz}}; \\draw[very thick,dashed] (5.0,{82*sc:.3f}) -- (5.6,{82*sc:.3f}); \\node[right] at (5.65,{82*sc:.3f}) {{Katalizörlü}};'
SK20=tk(g)
q('0020',tipId='hz-katalizor',tip='Katalizörlü yolda hız belirleyen basamak',z='zor',alt='Katalizör',kaz='Katalizörlü iki basamaklı yolda hız belirleyen basamağı bulup katalizörün sağladığı Ea azalmasını hesaplar.',kalip='grafik',
 kart='K-AKHZ-20 (katalizörlü iki basamaklı yol) · katalizörsüz tek basamak',sekil=SK20,
 metin='Bir tepkime katalizörsüz ortamda tek basamakta gerçekleşmektedir. Ortama katalizör eklendiğinde tepkime ara ürün oluşturarak iki basamakta gerçekleşmektedir. İki yol için potansiyel enerji–tepkime koordinatı grafiği şekilde verilmiştir.\nBuna göre katalizörlü yolda hız belirleyen basamağın aktivasyon enerjisi, katalizörsüz yoldaki aktivasyon enerjisinden kaç kJ daha küçüktür?',
 dogru=30,yan=[(10,'Hızlı basamağın aktivasyon enerjisini (10 kJ) doğrudan fark sanmış.','bilgi'),(20,'Tepkime entalpisinin büyüklüğünü (30 − 10) aktivasyon enerjisi farkı sanmış.','bilgi'),(50,'Katalizörlü yolun yavaş basamağı yerine hızlı basamağıyla katalizörsüz Ea’yı kıyaslamış (60 − 10).','islem'),(60,'Katalizörsüz yolun Ea’sının tamamının ortadan kalktığını sanmış.','bilgi')],
 istenen='Ea’daki fark (kJ).',ip=['Katalizörlü yolun her basamağını kendi başlangıç düzeyinden ölçüp hangisinin daha büyük olduğuna bak.'],
 bilgi=[B('Katalizörlü yol','katalizör tepkimeyi daha düşük enerjili, çoğu kez daha çok basamaklı bir yoldan gerçekleştirir. Basamaklı yolda aktivasyon enerjisi en büyük olan basamak hızı belirler. Örnek: iki basamağın Ea’ları 12 ve 8 kJ ise hızı belirleyen 12 kJ’lik basamaktır')],
 ad=[A('Katalizörsüz Ea','Tepe girenlerin düzeyinden okunur.','90 − 30 = 60 kJ'),A('Katalizörlü basamaklar','Her basamak kendi başlangıç düzeyinden ölçülür.','1. basamak: 60 − 30 = 30 kJ · 2. basamak: 50 − 40 = 10 kJ'),A('Hız belirleyen basamak','Ea’sı büyük olan basamak yavaştır.','30 kJ > 10 kJ → 1. basamak'),A('Farkı bul','Katalizörsüz Ea’dan çıkar.','60 − 30 = 30 kJ')],
 puf='Katalizörlü yolda tek bir tepe aramak yerine her basamağın Ea’sını ayrı ölç ve en büyüğünü al.')

bitir(P,'hiz','akim|Kimyasal Tepkimelerde Hız')
os.replace(os.path.join(HV,'kartlar','hiz.json'),os.path.join(HV,'kartlar','akhiz.json'))
