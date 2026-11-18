"""AYT Matematik · Türev (20 soru). Her doğru ve çeldirici değer kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json
HV='/home/claude/zekacademy-app/havuz'; HD=os.path.join(HV,'ayt-mat')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
import sympy as sp
H.KONU='Türev'
UK='amat|Türev'
P=Parti('turev','Türev',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2025 AYT Matematik çıkmış türev soruları (türev tanımı, kurallar, teğet, f′ grafiği, ekstremum, optimizasyon, hız-ivme; yalnız mantık) · MEB 12. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def uniq(v,e): assert len({Fr(x) for x in [v]+list(e)})==5,(v,e)
x,t=sp.symbols('x t')
def R(v): return Fr(int(sp.numer(sp.nsimplify(v))),int(sp.denom(sp.nsimplify(v))))
MAVI='blue!70!black'; TUR='orange!90!black'; MOR='violet!80!black'; YES='vurgu!80!black'
OZ=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']

# ---------- bilgi kutuları (örnekler soruların sayılarından ve kurgusundan farklı) ----------
TAN=B('Türevin tanımı','f′(a) = lim h→0 [f(a + h) − f(a)] / h = lim x→a [f(x) − f(a)] / (x − a) değeri, f’nin x = a noktasındaki anlık değişim oranıdır. Pay ve payda aynı anda sıfıra giderken türev tanımına benzetilebilen limitler f′(a) ile yazılır. Örnek: f(x) = x² için lim x→3 (x² − 9)/(x − 3) = f′(3) = 6’dır')
KUR=B('Türev kuralları','(u·v)′ = u′·v + u·v′ · (u/v)′ = (u′·v − u·v′)/v² · (f ∘ g)′(x) = f′(g(x))·g′(x) · (sin ax)′ = a·cos ax · (cos ax)′ = −a·sin ax. Örnek: (x²·sin x)′ = 2x·sin x + x²·cos x’tir')
TEG=B('Teğet ve normal','y = f(x) eğrisinin x = a apsisli noktasındaki teğetinin eğimi f′(a)’dır; teğet denklemi y − f(a) = f′(a)·(x − a), normal denklemi eğimi −1/f′(a) olan doğrudur. Örnek: f(x) = x² ise x = 3 noktasındaki teğetin eğimi 6, denklemi y − 9 = 6(x − 3)’tür')
ART=B('Artan, azalan ve yerel ekstremum','Bir aralıkta f′ > 0 ise f artan, f′ < 0 ise f azalandır. f′’nün işareti − ’den + ’ya geçen noktada yerel minimum, + ’dan − ’ye geçen noktada yerel maksimum vardır; işareti değişmeyen noktada ekstremum yoktur. f″’nün işaret değiştirdiği noktada büküm noktası bulunur. Örnek: f′(x) = (x − 5)(x + 1) ise f, x = −1’de yerel maksimum, x = 5’te yerel minimum alır')
OPT=B('Enbüyük ve enküçük değer problemleri','Değeri en büyük ya da en küçük yapılacak büyüklük tek değişkene bağlı yazılır; türevi sıfıra eşitlenerek bulunan değerin gerçekten uç değer verdiği işaret değişimiyle ya da uç noktalarla kontrol edilir. Örnek: toplamı 10 olan iki sayının çarpımı x(10 − x) ile yazılır, türev sıfır olduğunda x = 5 ve çarpım 25’tir')
HAR=B('Hız ve ivme','Doğrusal harekette konum s(t) ise anlık hız v(t) = s′(t), ivme a(t) = v′(t) = s″(t)’dir. Hızın işaret değiştirdiği anda cisim yön değiştirir; bir aralıktaki ortalama hız (s(b) − s(a))/(b − a)’dır. Örnek: s(t) = t² + 3t ise v(2) = 7, a(2) = 2’dir')
ZIN=B('Zincir kuralı ve tablo okuma','(f ∘ g)′(a) = f′(g(a))·g′(a): önce iç fonksiyonun a’daki değeri bulunur, f′ o değerde okunur, g′(a) ile çarpılır. Örnek: g(1) = 4, f′(4) = 3 ve g′(1) = 2 ise (f ∘ g)′(1) = 3 · 2 = 6’dır')

# ---------- kartlar ----------
kartla('K-ATRV-01','Türev tanımı ve limit','Limit ifadesi türev tanımının kalıbına dönüştürülür ya da pay sıfırlanıyorsa terimler ayrılıp f′(a) ve f(a) ile yazılır.','Limit değerini f(a) sanmak; h yerine −h ya da 2h yazılınca katsayıyı atlamak; paydaki işareti kaçırmak.','orta','düz',4,'tur-tanim','Türev tanımı ve limit')
kartla('K-ATRV-02','Türev kuralları ve bileşke','Çarpım, bölüm ve zincir kuralı sırayla uygulanır; iç fonksiyonun türevi çarpılır; verilen noktada değer hesaplanır.','Çarpımın türevini türevlerin çarpımı sanmak; zincirde iç türevi unutmak; trigonometrik türevde işaret ve katsayı hatası.','orta','düz',4,'tur-kural','Türev kuralları ve bileşke')
kartla('K-ATRV-03','Teğet, normal ve eğim','Değme noktasının koordinatı ve eğim f′(a) ile teğet denklemi kurulur; eksenlerle ya da başka bir eğriyle ilişkisi kurulur.','f′(a) yerine f(a)’yı eğim sanmak; teğet ile normali karıştırmak; ortak teğette yalnız değer eşitliğini kullanmak.','orta','grafik',4,'tur-teget','Teğet, normal ve eğim')
kartla('K-ATRV-04','f′ grafiğinden f’yi yorumlama','f′’nün işareti f’nin yönünü, işaret değişimi ekstremumu, f′’nün tepe noktası f’nin bükümünü; f′ ile eksen arasındaki işaretli alan f’nin değişimini verir.','f′ artıyor diye f’yi artan sanmak; sıfırlardan her birini ekstremum saymak; alanı işaretsiz toplamak.','zor','grafik',5,'tur-fgraf','f′ grafiğinden f’yi yorumlama')
kartla('K-ATRV-05','Ekstremum ve değişim','Türevin köklerinde işaret incelenir; yerel uç değerler hesaplanır; denklemin kök sayısı yerel uç değerlerle yatay doğrunun konumundan bulunur.','Kritik noktayı otomatik ekstremum saymak; uç değerleri dahil/hariç karıştırmak; maksimum ile minimum adlarını ters kullanmak.','orta','öncüllü',4,'tur-ekstrem','Ekstremum ve değişim')
kartla('K-ATRV-06','Enbüyük ve enküçük değer problemleri','Büyüklük tek değişkenli yazılır, türev sıfırlanır, bulunan değer istenen ölçüye (çevre, yüzey alanı, hacim) taşınır.','Değişkeni yanlış kurmak; ara bölme ya da kenar sayısını yanlış saymak; istenen büyüklük yerine ara sonucu yazmak.','zor','hikâyeli',5,'tur-optim','Enbüyük ve enküçük değer problemleri')
kartla('K-ATRV-07','Hız, ivme ve konum grafiği','Konum fonksiyonunun türevi hız, hızın türevi ivmedir; hızın sıfırlandığı an yön değişimini verir; yol ile yer değiştirme ayrılır.','Konumu hız sanmak; yer değiştirmeyi alınan yol saymak; ortalama hız ile anlık hızı karıştırmak.','orta','öncüllü',4,'tur-hareket','Hız, ivme ve konum grafiği')
kartla('K-ATRV-08','Tablodan bileşke ve çarpım türevi','Tabloda verilen f, g, f′ ve g′ değerleri doğru kurallara yerleştirilir; bileşkede iç değer önce bulunup f′ o noktada okunur.','Zinciri unutmak; f′’yi iç fonksiyonun değerinde değil x’te okumak; çarpım kuralının bir terimini düşürmek.','kolay','tablo',3,'tur-tablo','Tablodan bileşke ve çarpım türevi')

# ================= şekil yardımcıları =================
def graf(x0,x1,y0,y1,sx,sy,govde,xt=None,yt=None,gx=True,gy=True,xlab='x',ylab='y',fs='\\footnotesize',ax=0.8):
    o=[]
    if gx:
        for i in range(x0,x1+1): o.append(f'\\draw[gray!30,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    if gy:
        for j in range(y0,y1+1): o.append(f'\\draw[gray!30,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(govde)
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3)*sx:.3f},0) -- ({(x1+ax)*sx:.3f},0) node[right] {{${xlab}$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.3)*sy:.3f}) -- (0,{(y1+ax*1.2)*sy:.3f}) node[above] {{${ylab}$}};')
    for i in (xt if xt is not None else [i for i in range(x0,x1+1) if i]):
        if i!=0: o.append(f'\\node[below=2pt,font={fs}] at ({i*sx:.3f},0) {{${i}$}};')
    for j in (yt if yt is not None else [j for j in range(y0,y1+1) if j]):
        if j!=0: o.append(f'\\node[left=2pt,font={fs},fill=white,inner sep=0.6pt] at (0,{j*sy:.3f}) {{${j}$}};')
    return '\n'.join(o)
def egri(pts,sx,sy,renk,w='1.8pt',extra=''):
    return f'\\draw[{renk},line width={w}{extra}] '+' -- '.join(f'({a*sx:.3f},{b*sy:.3f})' for a,b in pts)+';'
def ornek(fn,a,b,n=60):
    return [(a+(b-a)*i/n,float(fn(a+(b-a)*i/n))) for i in range(n+1)]
def nokta(a,b,sx,sy,renk='black',r='2.2pt'):
    return f'\\fill[{renk}] ({a*sx:.3f},{b*sy:.3f}) circle ({r});'
def cizgi(a1,b1,a2,b2,sx,sy,renk,w='1pt',st='dashed'):
    return f'\\draw[{renk},{st},line width={w}] ({a1*sx:.3f},{b1*sy:.3f}) -- ({a2*sx:.3f},{b2*sy:.3f});'
def etiket(a,b,sx,sy,s,pos='above right',renk='black',fs='\\footnotesize'):
    return f'\\node[{pos},font={fs},text={renk},inner sep=1.5pt] at ({a*sx:.3f},{b*sy:.3f}) {{{s}}};'

# ================= 01 kolay · grafik: eğri ve teğet doğrusu, çarpımın türevi =================
f1=lambda u:Fr(1,2)*u*u+1; df1=lambda u:Fr(1)*u
a=2; assert f1(a)==3 and df1(a)==2
d1=lambda u:2*u-1; assert d1(0)==-1 and d1(4)==7 and d1(a)==f1(a)    # d doğrusu A(2,3)’ten geçer, eğimi 2
v=f1(a)+a*df1(a); assert v==7
e=[a*df1(a),f1(a)+df1(a),f1(a)*df1(a),f1(a)]
assert e==[4,5,6,3]; uniq(v,e)
body=graf(-1,5,-2,10,0.85,0.36,'\n'.join([
 egri(ornek(f1,-1.4,4.4),0.85,0.36,MAVI,'1.9pt'),
 egri([(-0.6,d1(-0.6)),(4.4,d1(4.4))],0.85,0.36,TUR,'1.6pt'),
 nokta(2,3,0.85,0.36,'black','2.6pt'),nokta(0,-1,0.85,0.36,TUR,'2.2pt'),nokta(4,7,0.85,0.36,TUR,'2.2pt'),
 etiket(2,3,0.85,0.36,'$A(2,\\,3)$','below right'),
 etiket(0,-1,0.85,0.36,'$(0,\\,-1)$','below right',TUR),etiket(4,7,0.85,0.36,'$(4,\\,7)$','below right',TUR),
 etiket(3.3,2.4,0.85,0.36,'$f$','right',MAVI,'\\small\\bfseries'),etiket(4.4,d1(4.4),0.85,0.36,'$d$','above',TUR,'\\small\\bfseries')]),
 xt=[-1,1,2,3,4,5],yt=[2,4,6,8,10],gy=False)
SK=fig(body)
q('0001',tipId='tur-teget',tip='Teğet, normal ve eğim',z='kolay',alt='Teğet ve Eğim',kaz='Grafikte verilen eğri ve teğet doğrusundan f(a) ile f′(a) değerlerini okuyup çarpımın türevini hesaplar.',kalip='grafik',
 kart='K-ATRV-03 (eğri ve teğet doğrusu grafiği) · A noktasında teğet doğrusundan eğim; g(x) = x · f(x)',
 metin='Şekilde, gerçel sayılar kümesinde türevlenebilir bir f fonksiyonunun grafiği ile bu grafiğe A noktasında teğet olan d doğrusu verilmiştir.\ng(x) = x · f(x)\nolduğuna göre, g′(2) değeri kaçtır?',
 dogru=v,yan=[(e[0],'Çarpımın türevini yalnız ikinci çarpanın türeviyle almış: 2 × f′(2) = 2 × 2.','bilgi'),(e[1],'Çarpım kuralında x’in türevi olan 1’i kullanmış ama ikinci terimdeki x çarpanını yazmamış: f(2) + f′(2).','bilgi'),(e[2],'Çarpım kuralını f(2) · f′(2) biçiminde uygulamış; x çarpanını hiç hesaba katmamış.','bilgi'),(e[3],'Türev almak yerine A noktasının ordinatı olan f(2) değerini yazmış.','dikkat')],
 istenen='g(x) = x · f(x) fonksiyonunun türevinin x = 2’deki değeri.',ip=['Teğet doğrusunun eğimi f′’nün değme noktasındaki değerini verir.'],bilgi=[TEG,KUR],sekil=SK,
 ad=[A('f(2) değerini oku','A noktası eğri üzerindedir; koordinatı şekilde yazılıdır.','f(2) = 3'),A('f′(2) değerini bul','d doğrusu (0, −1) ve (4, 7) noktalarından geçer; eğim değme noktasındaki türevdir.','f′(2) = (7 − (−1)) / (4 − 0) = 2'),A('Çarpım kuralını yaz','g′(x) = 1 · f(x) + x · f′(x) olur.','g′(2) = f(2) + 2 × f′(2)'),A('Değerleri yerleştir','Okunan değerler yerine yazılır.','g′(2) = 3 + 2 × 2 = 7')],
 puf='Grafikte teğet verilmişse değme noktasının ordinatı f(a), doğrunun eğimi f′(a) olur; ikisini ayrı ayrı oku.')

# ================= 02 kolay · tablo: çarpımın türevi =================
Tx=[1,2,3]; Tf=[4,1,3]; Tdf=[2,5,-1]; Tg=[3,2,6]; Tdg=[-2,4,1]
i=Tx.index(2); v=Tdf[i]*Tg[i]+Tf[i]*Tdg[i]; assert v==14
e=[Tf[i]*Tg[i],Tf[i]*Tdg[i],Tdf[i]+Tdg[i],Tdf[i]*Tg[i]]; assert e==[2,4,9,10]; uniq(v,e)
SK=tablo_svg(['x','1','2','3'],[['f(x)']+[str(z).replace('-','−') for z in Tf],['f′(x)']+[str(z).replace('-','−') for z in Tdf],['g(x)']+[str(z).replace('-','−') for z in Tg],['g′(x)']+[str(z).replace('-','−') for z in Tdg]])
q('0002',tipId='tur-tablo',tip='Tablodan bileşke ve çarpım türevi',z='kolay',alt='Tablodan Türev',kaz='Tabloda verilen fonksiyon ve türev değerlerinden çarpım fonksiyonunun türevini bir noktada hesaplar.',kalip='tablo',
 kart='K-ATRV-08 (f, g, f′, g′ tablosu) · h = f · g için h′ değeri',
 metin='Gerçel sayılar kümesinde türevlenebilir f ve g fonksiyonlarının x = 1, x = 2 ve x = 3 noktalarındaki değerleri ile bu noktalardaki türev değerleri aşağıdaki tabloda verilmiştir.\nh(x) = f(x) · g(x)\nolduğuna göre, h′(2) değeri kaçtır?',
 dogru=v,yan=[(e[0],'h′(2) yerine h(2) = f(2) · g(2) değerini hesaplamış.','bilgi'),(e[1],'Çarpım kuralında yalnız f(2) · g′(2) terimini yazmış; f′(2) · g(2) terimini atlamış.','dikkat'),(e[2],'Çarpımın türevini türevlerin toplamı sanmış: f′(2) + g′(2).','bilgi'),(e[3],'Çarpım kuralında yalnız f′(2) · g(2) terimini yazmış; f(2) · g′(2) terimini atlamış.','dikkat')],
 istenen='h(x) = f(x) · g(x) fonksiyonunun türevinin x = 2’deki değeri.',ip=['Çarpımın türevinde iki terim vardır; ikisinde de hangi fonksiyonun türevinin alındığına dikkat et.'],bilgi=[KUR],sekil=SK,
 ad=[A('Kuralı yaz','Çarpım kuralı uygulanır.','h′(x) = f′(x) × g(x) + f(x) × g′(x)'),A('Tablodan oku','x = 2 sütunundaki dört değer okunur.','f(2) = 1 · f′(2) = 5 · g(2) = 2 · g′(2) = 4'),A('Hesapla','Değerler yerine yazılır.','h′(2) = 5 × 2 + 1 × 4 = 14')],
 puf='Tabloda kural önce harflerle yazılır, sonra yalnız istenen sütundaki değerler yerleştirilir.')

# ================= 03 kolay · türev tanımı ile limit =================
fT=lambda u:u**4-3*u**2+2*u; dfT=lambda u:4*u**3-6*u+2
v=dfT(2); assert v==22 and fT(2)==8
sx_=sp.limit((x**4-3*x**2+2*x-8)/(x-2),x,2); assert sx_==22
e=[fT(2),32-12,4*8-3*2+2,32+12+2]; assert e==[8,20,28,46]; uniq(v,e)
q('0003',tipId='tur-tanim',tip='Türev tanımı ve limit',z='kolay',alt='Türevin Tanımı',kaz='Fark bölümü limitini türev tanımı olarak tanıyıp polinomun türevinin değerini hesaplar.',kalip='düz',
 kart='K-ATRV-01 (türev tanımı limiti) · fark bölümü limitinin f′(a) ile yazılması',
 metin='f(x) = x⁴ − 3x² + 2x\nfonksiyonu için\nlim x→2  [f(x) − f(2)] / (x − 2)\nlimitinin değeri kaçtır?',
 dogru=v,yan=[(e[0],'Limitin değerini f(2) = 8 sanmış; ifadenin türev tanımı olduğunu görmemiş.','bilgi'),(e[1],'2x teriminin türevini 0 alıp 4 · 8 − 6 · 2 = 20 bulmuş.','islem'),(e[2],'−3x²’nin türevini −6x yerine −3x yazmış: 32 − 6 + 2.','islem'),(e[3],'−3x² teriminin türevinin işaretini ters yazmış: 32 + 12 + 2.','islem')],
 istenen='Verilen limitin değeri.',ip=['Limitteki payın ve paydanın neyin farkı olduğuna bak.'],bilgi=[TAN],
 ad=[A('Tanıma bak','Limit, f′(2) için yazılan fark bölümüdür.','lim x→2 [f(x) − f(2)] / (x − 2) = f′(2)'),A('Türevi bul','Her terimin türevi ayrı alınır.','f′(x) = 4x³ − 6x + 2'),A('x = 2 yaz','Değer yerine yazılır.','f′(2) = 4 × 8 − 6 × 2 + 2'),A('Sonuç','İşlemler tamamlanır.','32 − 12 + 2 = 22')],
 puf='Limitleri değerlendirirken türev tanımının fark bölümü kalıbını arayın.')

# ================= 04 kolay · hız (hikâyeli) =================
sT=lambda u:u**3-6*u**2+9*u+2; vT=lambda u:3*u**2-12*u+9; aT=lambda u:6*u-12
v=vT(4); assert v==9
e=[3*16-12*4,sT(4),Fr(sT(4)-sT(0),4),aT(4)]; assert e==[0,6,1,12]; uniq(v,e)
q('0004',tipId='tur-hareket',tip='Hız, ivme ve konum grafiği',z='kolay',alt='Anlık Hız',kaz='Konum fonksiyonunun türeviyle verilen anda anlık hızı hesaplar.',kalip='hikâyeli',
 kart='K-ATRV-07 (robot rayda hareketi) · konum fonksiyonundan t anındaki anlık hız',
 metin='Doğrusal bir rayda hareket eden bir robotun, hareketin başladığı andan t saniye sonra başlangıç noktasına olan konumu metre cinsinden\ns(t) = t³ − 6t² + 9t + 2\nbağıntısıyla veriliyor.\nBuna göre, robotun t = 4. saniyedeki anlık hızı kaç m/sn’dir?',
 dogru=v,yan=[(e[0],'9t teriminin türevini yazmayı unutmuş: 3 × 16 − 12 × 4 = 0.','islem'),(e[1],'Hız yerine t = 4’teki konumu hesaplamış: s(4).','bilgi'),(e[2],'Anlık hız yerine 0 ile 4. saniye arasındaki ortalama hızı bulmuş.','bilgi'),(e[3],'Hız yerine hızın türevi olan ivmeyi, yani s″(4) değerini hesaplamış.','bilgi')],
 istenen='Robotun t = 4. saniyedeki anlık hızı.',ip=['Anlık hız, konum fonksiyonunun zamana göre değişim oranıdır.'],bilgi=[HAR],
 ad=[A('Hız fonksiyonunu yaz','Anlık hız konumun türevidir.','v(t) = s′(t) = 3t² − 12t + 9'),A('t = 4 yaz','İstenen anın değeri yerine konur.','v(4) = 3 × 16 − 12 × 4 + 9'),A('Hesapla','Sayılar işlenir.','48 − 48 + 9 = 9 m/sn')],
 puf='Konumdan hıza bir türev, hızdan ivmeye bir türev daha; istenen büyüklüğün kaçıncı türev olduğunu önce belirle.')

# ================= 05 orta · öncüllü, f′ parabolü grafiği =================
f1p=lambda u:u*(u-4)
assert f1p(0)==0 and f1p(4)==0 and f1p(2)==-4
dd=lambda u:2*u-4; assert dd(2)==0 and dd(1)<0 and dd(3)>0
I_=True; II_=True; III_=False        # I: (0,4) f′<0 azalan · II: f″ x=2’de − → + büküm · III: x=4’te f′ − → +: yerel minimum
assert f1p(1)<0 and f1p(3)<0 and f1p(5)>0
body=graf(-1,5,-4,5,0.85,0.42,'\n'.join([
 egri(ornek(f1p,-1,5),0.85,0.42,MAVI,'2pt'),
 nokta(0,0,0.85,0.42),nokta(4,0,0.85,0.42),nokta(2,-4,0.85,0.42,TUR,'2.6pt'),
 cizgi(2,-4,2,0,0.85,0.42,TUR),cizgi(2,-4,0,-4,0.85,0.42,TUR),
 etiket(2,-4,0.85,0.42,'$(2,\\,-4)$','below',TUR),
 etiket(4.3,4.4,0.85,0.42,'$y=f\'(x)$','left',MAVI,'\\small\\bfseries')]),xt=[-1,1,2,3,4,5],yt=[-4,-2,2,4])
SK=fig(body)
q('0005',tipId='tur-fgraf',tip='f′ grafiğinden f’yi yorumlama',z='orta',alt='f′ Grafiği',kaz='Türev fonksiyonunun grafiğinden asıl fonksiyonun artan-azalan aralıklarını, ekstremum ve büküm noktalarını yorumlar.',kalip='öncüllü',
 kart='K-ATRV-04 (f′ parabolü grafiği) · artanlık, ekstremum türü ve f″’nün tepe noktasından büküm',
 metin='Gerçel sayılar kümesinde iki kez türevlenebilen bir f fonksiyonunun türevi olan f′ fonksiyonunun grafiği, tepe noktası şekilde gösterilen bir paraboldür.\nBuna göre,\nI. f, (0, 4) aralığında azalandır.\nII. f fonksiyonunun grafiğinin x = 2 apsisli noktasında büküm noktası vardır.\nIII. f, x = 4 apsisli noktasında yerel maksimuma sahiptir.\nifadelerinden hangileri doğrudur?',
 dogru='I ve II',yan=[('Yalnız I','f′ fonksiyonunun tepe noktasının f için bir anlam taşımadığını düşünüp II’yi yanlış saymış; f″’nün x = 2’de işaret değiştirdiğini görmemiş.','bilgi'),('Yalnız II','f′’nün (0, 4)’te negatif değerler aldığını okumayıp parabol “aşağı açık” görünümünden f’yi artan sanmış; I’i yanlış saymış.','dikkat'),('I ve III','II’yi yanlış sanmış; ayrıca x = 4’te f′’nün − ’den + ’ya geçmesini yerel maksimum sanarak III’ü doğru saymış.','bilgi'),('I, II ve III','x = 4’te f′’nün işaret değişimini ters okumuş: − ’den + ’ya geçişi yerel maksimum sanmış.','bilgi')],sira=OZ,
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Önce f′’nün işaretini üç aralıkta belirle; ardından f′’nün kendi artış–azalışına bak.'],bilgi=[ART],sekil=SK,
 ad=[A('f′’nün işaretini oku','Parabol x = 0 ve x = 4’te eksenle kesişiyor; arası eksenin altında.','x < 0: f′ > 0 · 0 < x < 4: f′ < 0 · x > 4: f′ > 0'),A('I’i değerlendir','f′ negatifken f azalandır.','(0, 4)’te f azalan → I doğru'),A('II’yi değerlendir','f′ x = 2’de en küçük değerini alır; f″ = (f′)′ orada − ’den + ’ya geçer.','f″(2) = 0 ve işaret değişir → büküm → II doğru'),A('III’ü değerlendir','x = 4’te f′ − ’den + ’ya geçer; bu geçiş yerel minimumdur.','x = 4 yerel minimum → III yanlış'),A('Sonuç','Doğru olanlar I ve II’dir.','I ve II')],
 puf='f′ grafiğini üç ayrı bilgi için oku: işaret, işaret değişimi, kendi artış–azalışı.')

# ================= 06 orta · grafik: yerel ekstremum değerleri farkı =================
f2=lambda u:u**3-3*u**2-9*u+4
df2=lambda u:3*u**2-6*u-9
assert df2(-1)==0 and df2(3)==0 and f2(0)==4
ymax=f2(-1); ymin=f2(3); assert (ymax,ymin)==(9,-23); v=ymax-ymin; assert v==32
# yanlış zincir: f′ = 3x² + 2ax + b yerine kökleri yanlış yerleştirme: a = −6, b = −9 (2a katsayısını unutma)
f2y=lambda u:u**3-6*u**2-9*u+4; assert (f2y(-1),f2y(3))==(6,-50)
e=[ymax,ymax+ymin,-ymin,-ymin-ymax]; assert e==[9,-14,23,14]; uniq(v,e)
S2x,S2y=0.72,0.17
body=graf(-3,5,-25,12,S2x,S2y,'\n'.join([
 egri(ornek(f2,-3,5,80),S2x,S2y,MAVI,'2pt'),
 cizgi(-1,0,-1,9,S2x,S2y,TUR),cizgi(3,0,3,-23,S2x,S2y,TUR),
 nokta(-1,9,S2x,S2y,TUR,'2.6pt'),nokta(3,-23,S2x,S2y,TUR,'2.6pt'),nokta(0,4,S2x,S2y,'black','2.4pt'),
 etiket(0,4,S2x,S2y,'$4$','left'),
 etiket(1.6,10,S2x,S2y,'$y=f(x)$','right',MAVI,'\\small\\bfseries')]),xt=[-3,-2,-1,1,2,3,4,5],yt=[],gy=False)
SK=fig(body)
q('0006',tipId='tur-ekstrem',tip='Ekstremum ve değişim',z='orta',alt='Yerel Ekstremum Değerleri',kaz='Grafikten yerel ekstremum apsislerini ve y-kesimini okuyup polinomu belirleyerek yerel uç değerlerini hesaplar.',kalip='grafik',
 kart='K-ATRV-05 (üçüncü derece polinom grafiği) · ekstremum apsislerinden f′ ile katsayılar; uç değerlerin farkı',
 metin='Gerçel katsayılı f(x) = x³ + ax² + bx + c polinomunun grafiği şekildeki gibidir.\nBuna göre, f fonksiyonunun yerel maksimum değeri ile yerel minimum değeri arasındaki fark kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız yerel maksimum değerini bulup farkı almayı unutmuş.','dikkat'),(e[1],'Farkı almak yerine iki yerel uç değerin toplamını yazmış: 9 + (−23).','dikkat'),(e[2],'Yerel minimum değerinin mutlak değerini yazmış; maksimum değerini hesaba katmamış.','dikkat'),(e[3],'Yerel minimum değerinin mutlak değeri olan 23’ten yerel maksimum değeri 9’u çıkarmış.','islem')],
 istenen='Yerel maksimum ile yerel minimum değerlerinin farkı.',ip=['Yerel ekstremum apsisleri f′’nün kökleridir; grafikteki kesim noktası da bir denklem verir.'],bilgi=[ART],sekil=SK,
 ad=[A('f′’nün köklerini kur','Ekstremum apsisleri −1 ve 3 olduğundan f′ bu köklerle yazılır.','f′(x) = 3(x + 1)(x − 3) = 3x² − 6x − 9'),A('a ve b’yi bul','f′(x) = 3x² + 2ax + b ile katsayılar karşılaştırılır.','2a = −6, b = −9 → a = −3, b = −9'),A('c’yi bul','Grafik y eksenini 4’te kesiyor.','f(0) = c = 4'),A('Uç değerleri hesapla','f(x) = x³ − 3x² − 9x + 4’te iki apsis yazılır.','f(−1) = 9 · f(3) = −23'),A('Farkı al','Yerel maksimum − yerel minimum.','9 − (−23) = 32')],
 puf='Grafikte okunan ekstremum apsisleri f′’nün köküdür; kökleri bilinen f′ baş katsayıyla birlikte yazılır.')

# ================= 07 orta · şekilli: parabolün teğeti ve eksenlerle üçgen =================
fp=lambda u,c:u*u+c
c0=5; a=1
yk=c0-a*a; eg=2*a; xk=Fr(-yk,eg); assert (yk,xk)==(4,-2)
v=Fr(1,2)*abs(xk)*yk; assert v==4
c_=lambda eg_,yk_:Fr(1,2)*abs(Fr(-yk_,eg_))*yk_
e=[Fr(1,2)*a*yk,c_(a,yk),c_(2,fp(1,c0)),2*c_(a,yk)]      # taban A’nın apsisi · eğim 1 · y-kesimi f(1) · eğim 1 ve ½ unutulmuş
assert e==[2,8,9,16]; uniq(v,e)
S3x,S3y=0.95,0.3
tg=lambda u:2*u+4
body=graf(-3,3,-2,14,S3x,S3y,'\n'.join([
 f'\\fill[vurgu!25] ({-2*S3x:.3f},0) -- (0,0) -- (0,{4*S3y:.3f}) -- cycle;',
 egri(ornek(lambda u:u*u+5,-2.9,2.9),S3x,S3y,MAVI,'2pt'),
 egri([(-2.6,tg(-2.6)),(2.2,tg(2.2))],S3x,S3y,TUR,'1.7pt'),
 cizgi(1,0,1,6,S3x,S3y,'black'),
 nokta(1,6,S3x,S3y,'black','2.6pt'),nokta(0,4,S3x,S3y,TUR,'2.4pt'),
 etiket(1,6,S3x,S3y,'$A$','above left'),
 etiket(-2.6,tg(-2.6),S3x,S3y,'$d$','left',TUR,'\\small\\bfseries'),
 etiket(2.9,14,S3x,S3y,'$y=x^2+c$','right',MAVI,'\\small\\bfseries')]),xt=[1],yt=[4],gx=False,gy=False)
SK=fig(body)
q('0007',tipId='tur-teget',tip='Teğet, normal ve eğim',z='orta',alt='Teğet ve Alan',kaz='Parabole verilen apsisli noktadaki teğetin denklemini y-kesiminden kurup eksenlerle oluşturduğu üçgenin alanını hesaplar.',kalip='şekilli',
 kart='K-ATRV-03 (parabolün teğeti) · teğetin y-kesiminden c’yi bulup eksenlerle üçgen alanı',
 metin='c bir gerçel sayı olmak üzere şekilde y = x² + c parabolü ile bu parabole A noktasında teğet olan d doğrusu çizilmiştir.\nBuna göre, d doğrusu ile koordinat eksenleri arasında kalan boyalı üçgensel bölgenin alanı kaç birimkaredir?',
 dogru=v,yan=[(e[0],'Üçgenin tabanı olarak A’nın apsisi olan 1’i almış: ½ × 1 × 4.','dikkat'),(e[1],'Eğimi türevin tamamı yerine x olarak alıp (f′(x) = x) x eksenini −4’te kesen bir doğru bulmuş: ½ × 4 × 4.','islem'),(e[2],'Doğrunun y eksenini kestiği noktayı 4 yerine A’nın ordinatı olan 6 almış: ½ × 3 × 6.','dikkat'),(e[3],'Eğimi 1 almış ve ½ çarpanını unutmuş: 4 × 4.','islem')],
 istenen='d doğrusu ve eksenler arasında kalan üçgenin alanı.',ip=['Teğetin y ekseniyle kesim noktası c değerini bulmak için bir denklem verir.'],bilgi=[TEG],sekil=SK,
 ad=[A('Teğetin eğimini yaz','A’nın apsisi 1 olduğundan eğim f′(1) olur.','f′(x) = 2x → eğim = 2'),A('Teğet denklemini kur','Değme noktası (1, 1 + c); doğru y = 2x + c − 1 olur.','y = 2(x − 1) + (1 + c) = 2x + c − 1'),A('c’yi bul','Doğru y eksenini 4’te kesiyor.','c − 1 = 4 → c = 5'),A('x kesimini bul','y = 0 için x değeri bulunur.','2x + 4 = 0 → x = −2'),A('Alanı hesapla','Dik kenarlar 2 ve 4 birimdir.','½ × 2 × 4 = 4')],
 puf='Teğetin y-kesimi bilindiğinde c ve eğim birlikte çözülür; üçgen alanı için kesim noktalarının mutlak değerleri alınır.')

# ================= 08 orta · öncüllü, polinomun ekstremum ve büküm incelemesi =================
f8=lambda u:2*u**3-3*u**2-12*u+1
df8=lambda u:6*u**2-6*u-12
assert df8(-1)==0 and df8(2)==0 and df8(0)<0 and f8(3)==-8 and f8(0)==1
I8=False; II8=True; III8=f8(3)<f8(0)
assert (I8,II8,III8)==(False,True,True)          # I: x=2 yerel maks (aslında min)
f8bad=2*27-3*9+12*3+1; assert f8bad==64 and f8bad>f8(0)
assert 6*0**2-6*0+12==12
q('0008',tipId='tur-ekstrem',tip='Ekstremum ve değişim',z='orta',alt='Ekstremum İncelemesi',kaz='Polinom fonksiyonun türevinin işaret incelemesiyle artan-azalan aralıklarını ve yerel ekstremum türünü belirleyerek değer karşılaştırır.',kalip='öncüllü',
 kart='K-ATRV-05 (üçüncü derece polinom incelemesi) · işaret tablosu, ekstremum türü ve iki değerin karşılaştırılması',
 metin='f(x) = 2x³ − 3x² − 12x + 1\nfonksiyonu için\nI. f, x = 2 apsisli noktasında yerel maksimuma sahiptir.\nII. f, (−1, 2) aralığında azalandır.\nIII. f(3) < f(0) dır.\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',yan=[('Yalnız II','f(3)’ü hesaplarken −12x terimini +36 yazıp f(3) = 64 bulmuş; III’ü yanlış saymış.','islem'),('Yalnız III','f′(0)’ı −12 yerine +12 bulup (−1, 2)’de f′’yü pozitif sanmış; II’yi yanlış saymış.','islem'),('I ve III','f′’nün işaretini ters okumuş (+, −, +  yerine −, +, −): x = 2’yi maksimum, (−1, 2)’yi artan sanmış.','bilgi'),('I, II ve III','x = 2’de f′’nün − ’den + ’ya geçişini yerel maksimum sanmış; diğer incelemeleri doğru yapmış.','bilgi')],sira=['Yalnız II','Yalnız III','I ve III','II ve III','I, II ve III'],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['f′’nün köklerini bulup aralıklardaki işaretini belirle; III için iki değeri ayrı ayrı hesapla.'],bilgi=[ART],
 ad=[A('Türevi çarpanlarına ayır','Kritik noktalar türevin köklerindedir.','f′(x) = 6x² − 6x − 12 = 6(x + 1)(x − 2)'),A('İşareti incele','Üç aralıktan birer değer seçilir.','x < −1: + · −1 < x < 2: − · x > 2: +'),A('I ve II’yi değerlendir','x = 2’de f′ − ’den + ’ya geçer, yani yerel minimum vardır; (−1, 2)’de f′ negatiftir.','I yanlış · II doğru'),A('III’ü değerlendir','İki değer ayrı hesaplanır.','f(3) = 54 − 27 − 36 + 1 = −8 · f(0) = 1 → f(3) < f(0)'),A('Sonuç','Doğru olanlar II ve III’tür.','II ve III')],
 puf='f′’nün işaret değişimi ekstremum türünü belirler: − ’den + ’ya geçiş yerel minimum, + ’dan − ’ye geçiş yerel maksimumdur.')

# ================= 09 orta · tablo: bileşke ve çarpımın türevi =================
Tx=[1,2,3,4]; Tf=[3,4,1,2]; Tdf=[5,-2,6,3]; Tg=[2,3,4,1]; Tdg=[4,1,-3,7]
fd=dict(zip(Tx,Tf)); dfd=dict(zip(Tx,Tdf)); gd=dict(zip(Tx,Tg)); dgd=dict(zip(Tx,Tdg))
v=fd[gd[1]]+1*dfd[gd[1]]*dgd[1]; assert v==-4
e=[fd[gd[1]],fd[gd[1]]+dfd[gd[1]],dfd[1]*dgd[1],fd[gd[1]]+dfd[1]*dgd[1]]; assert e==[4,2,20,24]; uniq(v,e)
mn=lambda z:str(z).replace('-','−')
SK=tablo_svg(['x','1','2','3','4'],[['f(x)']+[mn(z) for z in Tf],['f′(x)']+[mn(z) for z in Tdf],['g(x)']+[mn(z) for z in Tg],['g′(x)']+[mn(z) for z in Tdg]])
q('0009',tipId='tur-tablo',tip='Tablodan bileşke ve çarpım türevi',z='orta',alt='Tablodan Zincir Kuralı',kaz='Tabloda verilen değerlerle çarpım ve bileşke içeren fonksiyonun türevini zincir kuralıyla bir noktada hesaplar.',kalip='tablo',
 kart='K-ATRV-08 (f, g, f′, g′ tablosu) · h = x · f(g(x)) için h′ değeri; zincir ve çarpım birlikte',
 metin='Gerçel sayılar kümesinde türevlenebilir f ve g fonksiyonlarının bazı noktalardaki değerleri ile türev değerleri aşağıdaki tabloda verilmiştir.\nh(x) = x · f(g(x))\nolduğuna göre, h′(1) değeri kaçtır?',
 dogru=v,yan=[(e[0],'Çarpım kuralının yalnız 1 · f(g(1)) terimini yazmış; x · (f ∘ g)′(1) terimini atlamış.','dikkat'),(e[1],'Zincir kuralında iç fonksiyonun türevini çarpmamış: f(g(1)) + f′(g(1)).','bilgi'),(e[2],'(f ∘ g)′ türevini f′(1) · g′(1) sanmış ve çarpım kuralının ilk terimini yazmamış.','bilgi'),(e[3],'Çarpım kuralını doğru kurmuş ama f′’yü g(1) = 2 yerine x = 1’de okumuş: f(2) + f′(1) · g′(1).','dikkat')],
 istenen='h(x) = x · f(g(x)) fonksiyonunun türevinin x = 1’deki değeri.',ip=['Önce g(1) değerini bul; f′’nün hangi noktada okunacağını bu değer belirler.'],bilgi=[ZIN,KUR],sekil=SK,
 ad=[A('Çarpım kuralını yaz','h iki çarpanın çarpımıdır: x ve f(g(x)).','h′(x) = 1 × f(g(x)) + x × f′(g(x)) × g′(x)'),A('İç değeri bul','Tablodan g(1) okunur.','g(1) = 2'),A('Tablodan değerleri oku','f f′ değerleri x = 2’de, g′ değeri x = 1’de okunur.','f(2) = 4 · f′(2) = −2 · g′(1) = 4'),A('Yerine koy','h′(1) hesaplanır.','h′(1) = 4 + 1 × (−2) × 4 = −4')],
 puf='Bileşkenin türevinde f′ iç fonksiyonun değerinde okunur, g′ ise x’in kendisinde; iki okuma noktasını ayrı ayrı yaz.')

# ================= 10 orta · trigonometrik türev =================
f10=sp.sin(2*x)*sp.cos(x); d10=sp.diff(f10,x); val=d10.subs(x,sp.pi/3); assert sp.simplify(val)==sp.Rational(-5,4)
v=Fr(-5,4)
c2=sp.cos(2*sp.pi/3); s2=sp.sin(2*sp.pi/3); c1=sp.cos(sp.pi/3); s1=sp.sin(sp.pi/3)
ev=[c2*c1-s2*s1, 2*c2*c1+s2*s1, -s2*s1, 2*c2*c1]
e=[R(sp.simplify(z)) for z in ev]; assert e==[-1,Fr(1,4),Fr(-3,4),Fr(-1,2)]; uniq(v,e)
q('0010',tipId='tur-kural',tip='Türev kuralları ve bileşke',z='orta',alt='Trigonometrik Türev',kaz='Trigonometrik fonksiyonların çarpımının türevini zincir ve çarpım kuralıyla alıp verilen noktada hesaplar.',kalip='düz',
 kart='K-ATRV-02 (trigonometrik çarpım) · sin 2x · cos x türevinin π/3’teki değeri',
 metin='f(x) = sin 2x · cos x\nolduğuna göre, f′(π/3) değeri kaçtır?',
 dogru=v,yan=[(e[0],'sin 2x’in türevinde iç fonksiyonun türevi olan 2’yi yazmamış: cos 2x · cos x − sin 2x · sin x.','bilgi'),(e[1],'cos x’in türevini −sin x yerine +sin x almış: 2 cos 2x · cos x + sin 2x · sin x.','bilgi'),(e[2],'Çarpım kuralının ilk terimini atlayıp yalnız sin 2x · (−sin x) terimini hesaplamış.','dikkat'),(e[3],'Çarpım kuralının ikinci terimini atlayıp yalnız 2 cos 2x · cos x terimini hesaplamış.','dikkat')],
 istenen='f′(π/3) değeri.',ip=['Çarpım kuralında iki terim vardır; sin 2x’in türevi için iç fonksiyonu unutma.'],bilgi=[KUR],
 ad=[A('Çarpım kuralını yaz','Birinci çarpan sin 2x, ikinci çarpan cos x.','f′(x) = (sin 2x)′ × cos x + sin 2x × (cos x)′'),A('Türevleri al','sin 2x için zincir kuralı gerekir.','f′(x) = 2 cos 2x × cos x − sin 2x × sin x'),A('x = π/3 değerlerini yaz','Trigonometrik değerler yerleştirilir.','cos 2π/3 = −1/2 · cos π/3 = 1/2 · sin 2π/3 = √3/2 · sin π/3 = √3/2'),A('Hesapla','Terimler toplanır.','f′(π/3) = 2 × (−1/2) × (1/2) − (√3/2) × (√3/2) = −1/2 − 3/4 = −5/4')],
 puf='Trigonometrik fonksiyonun içinde bir ifade varsa türevine iç fonksiyonun türevi çarpan olarak eklenir.')

# ================= 11 orta · hikâyeli şekil: ara bölmeli arsa =================
A11=lambda xx:xx*Fr(120-3*xx,2)
xs=sp.symbols('xs'); Ax=xs*(120-3*xs)/2; sol=sp.solve(sp.diff(Ax,xs),xs); assert sol==[20]
v=A11(20); assert v==600 and (120-60)/2==30
e=[900,1200,400,A11(10)]; assert A11(10)==450 and e==[900,1200,400,450]; uniq(v,e)
assert 2*30+2*30==120 and 30*30==900 and 20*(120-3*20)==1200 and (120/3)**2/4*1==400.0 and 120/6==20
body='\n'.join([
 '\\draw[line width=2.4pt,'+MAVI+'] (0,0) rectangle (5.4,2.6);',
 '\\draw[line width=2.4pt,'+TUR+'] (2.7,0) -- (2.7,2.6);',
 '\\draw[{Stealth}-{Stealth}] (0,-0.3) -- (5.4,-0.3); \\node[below,font=\\small] at (2.7,-0.3) {$y$};',
 '\\node[left,font=\\small] at (-0.1,1.3) {$x$};','\\node[right,font=\\small] at (5.5,1.3) {$x$};',
 '\\node[above,font=\\small,text='+TUR+'] at (2.7,2.7) {ara bölme};',
 '\\node[font=\\small] at (1.35,1.3) {arsa};','\\node[font=\\small] at (4.05,1.3) {arsa};',
 '\\draw[line width=2.4pt,'+MAVI+'] (6.6,2.1) -- (7.4,2.1); \\node[right,font=\\footnotesize] at (7.5,2.1) {dış sınır teli};',
 '\\draw[line width=2.4pt,'+TUR+'] (6.6,1.4) -- (7.4,1.4); \\node[right,font=\\footnotesize] at (7.5,1.4) {ara bölme teli};'])
SK=fig(body)
q('0011',tipId='tur-optim',tip='Enbüyük ve enküçük değer problemleri',z='orta',alt='Tel ile Alan Optimizasyonu',kaz='Ara bölmeli dikdörtgen arsanın tel uzunluğu kısıtından alan fonksiyonu kurup türevle en büyük alanı bulur.',kalip='hikâyeli',
 kart='K-ATRV-06 (ara bölmeli arsa) · kısıt denkleminden tek değişkenli alan fonksiyonu; en büyük alan',
 metin='Bir köy kooperatifi, dikdörtgen biçimli bir arsayı şekildeki gibi, kenarlarından birine paralel bir ara bölmeyle iki eş parçaya ayıracaktır. Hem dış sınır hem de ara bölme için kullanılacak telin toplam uzunluğu 120 metredir ve tel hiç artmayacak biçimde tamamen kullanılacaktır.\nBuna göre, arsanın alanı en çok kaç metrekare olabilir?',
 dogru=v,yan=[(e[0],'Ara bölmeyi hesaba katmamış: 2x + 2y = 120 için kare olan 30 × 30’luk arsayı en büyük sanmış.','dikkat'),(e[1],'Kısıttan y = (120 − 3x)/2 yerine y = 120 − 3x yazmış; x = 20 için 20 × 60.','islem'),(e[2],'Ara bölmeyi de dört kenar gibi sayıp 3x + 3y = 120 almış: x = y = 20.','dikkat'),(e[3],'Alan fonksiyonunun türevini 60 − 3x yerine 60 − 6x yazıp x = 10 bulmuş: 10 × 45.','islem')],
 istenen='Arsanın alabileceği en büyük alan.',ip=['Telin toplam uzunluğundan bir denklem kurup alanı tek değişkene indir.'],bilgi=[OPT],sekil=SK,
 ad=[A('Kısıtı yaz','x uzunluklu üç parça, y uzunluklu iki parça tel gerekir.','3x + 2y = 120 → y = (120 − 3x)/2'),A('Alan fonksiyonunu kur','Alan, iki kenarın çarpımıdır.','A(x) = x × (120 − 3x)/2 = 60x − 1,5x²'),A('Türevi sıfırla','A′(x) = 0 çözülür.','A′(x) = 60 − 3x = 0 → x = 20'),A('İşareti kontrol et','A″ negatif, yani parabol aşağı açık; bulunan değer maksimumdur.','A″(x) = −3 < 0'),A('Alanı hesapla','y de bulunur.','y = (120 − 60)/2 = 30 → A = 20 × 30 = 600')],
 puf='Kısıt denkleminden bir değişkeni yok edip alanı tek değişkenli yazmak optimizasyonun ilk adımıdır.')

# ================= 12 orta · öncüllü, konum–zaman grafiği =================
s12=lambda u:-u**2+8*u; v12=lambda u:-2*u+8
assert s12(0)==0 and s12(8)==0 and s12(4)==16 and v12(4)==0
ort13=Fr(s12(3)-s12(1),2); assert ort13==4 and v12(2)==4
yol=(s12(4)-s12(0))+(s12(4)-s12(8)); assert yol==32 and s12(4)==16
assert Fr(s12(3)-s12(1),3+1)==2          # II’yi doğru saydıran hata: payda 3 + 1
S12x,S12y=0.72,0.27
gridh=''.join(f'\\draw[gray!30,thin] (0,{j*S12y:.3f}) -- ({8*S12x:.3f},{j*S12y:.3f});' for j in (4,8,12,16))
body=graf(0,8,0,16,S12x,S12y,gridh+'\n'+'\n'.join([
 egri(ornek(s12,0,8),S12x,S12y,MAVI,'2pt'),
 nokta(4,16,S12x,S12y,TUR,'2.6pt'),nokta(8,0,S12x,S12y,'black'),
 cizgi(4,16,4,0,S12x,S12y,TUR),cizgi(4,16,0,16,S12x,S12y,TUR),
 etiket(4,16,S12x,S12y,'$(4,\\,16)$','above right',TUR),
 etiket(6.2,15,S12x,S12y,'$s(t)$','right',MAVI,'\\small\\bfseries')]),xt=list(range(1,9)),yt=[4,8,12,16],gy=False,xlab='t',ylab='s')
SK=fig(body)
q('0012',tipId='tur-hareket',tip='Hız, ivme ve konum grafiği',z='orta',alt='Konum–Zaman Grafiği',kaz='Konum–zaman parabolünden konum fonksiyonunu kurup hız, ortalama hız ve alınan yol hakkındaki yargıları değerlendirir.',kalip='öncüllü',
 kart='K-ATRV-07 (konum–zaman parabolü) · anlık hız sıfırı, ortalama hız ve yol–yer değiştirme ayrımı',
 metin='Doğrusal bir yolda hareket eden bir cismin başlangıç noktasına olan konumu, t saniye için s(t) metredir. Cismin konum–zaman grafiği, şekilde görülen bir parabol parçasıdır (0 ≤ t ≤ 8).\nBuna göre,\nI. t = 4 anında cismin hızı sıfırdır ve cisim yön değiştirir.\nII. t = 1 ile t = 3 anları arasındaki ortalama hız 2 m/sn’dir.\nIII. Cisim 0 ≤ t ≤ 8 aralığında toplam 16 m yol alır.\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız I',yan=[('Yalnız III','Hızın sıfır olduğu anda cismin durup aynı yönde devam ettiğini düşünmüş; I’i yanlış saymış; yolu yalnız ilk yarı hareketle (16 m) hesaplayıp III’ü doğru bulmuş.','bilgi'),('I ve II','Ortalama hızı hesaplarken payı (15 − 7) = 8, paydayı 3 + 1 = 4 almış; II’yi doğru saymış.','islem'),('I ve III','Cismin yalnız t = 4’e kadar aldığı yolu (16 m) toplam yol sanmış; dönüşteki 16 m’yi eklememiş.','dikkat'),('I, II ve III','Ortalama hızın paydasını 3 + 1 = 4 almış ve toplam yol olarak yalnız ilk yarıdaki 16 m’yi yazmış.','islem')],sira=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['Grafikteki üç noktadan s(t) kuralını kur; hız onun türevidir, yol için hareketin yönünü ayrı incele.'],bilgi=[HAR],sekil=SK,
 ad=[A('Konum fonksiyonunu kur','Parabol t = 0 ve t = 8’de sıfır, t = 4’te 16 değerini alıyor.','s(t) = −t² + 8t'),A('Hızı bul','Türev alınır.','v(t) = −2t + 8 → v(4) = 0, t = 4’te işaret + ’dan − ’ye döner → I doğru'),A('Ortalama hızı bul','Konum farkı süre farkına bölünür.','s(3) = 15 · s(1) = 7 → (15 − 7)/(3 − 1) = 4 → II yanlış'),A('Yolu hesapla','Cisim 4. saniyeye kadar ileri, sonra aynı mesafeyi geri gider; yol yön değişimleri toplanarak bulunur.','16 + 16 = 32 m → III yanlış'),A('Sonuç','Yalnız I doğrudur.','Yalnız I')],
 puf='Hız konumun türevidir; ortalama hız ile anlık hız, yer değiştirme ile alınan yol ayrı kavramlardır.')

# ================= 13 orta · öncüllü, f′ işaret çizelgesi =================
f13p=lambda u:-(u+2)*(u-1)**2*(u-4)
assert f13p(-3)<0 and f13p(0)>0 and f13p(2)>0 and f13p(5)<0
I13=False; II13=True; III13=False
cols=[1.9,3.0,4.1,5.2,6.3,7.4,8.5]
o=['\\draw[thick] (0,0) rectangle (9.3,-1.8);','\\draw[thick] (0,-0.9) -- (9.3,-0.9);','\\draw[thick] (1.3,0) -- (1.3,-1.8);',
 '\\node[font=\\small] at (0.65,-0.45) {$x$};','\\node[font=\\small] at (0.65,-1.35) {$f\'(x)$};']
for cx,tx in zip(cols[1::2],['-2','1','4']):
    o.append(f'\\node[font=\\small] at ({cx:.2f},-0.45) {{${tx}$}};')
    o.append(f'\\node[font=\\small] at ({cx:.2f},-1.35) {{$0$}};')
for cx,sg in zip(cols[0::2],['-','+','+','-']):
    o.append(f'\\node[font=\\Large,text={"orange!90!black" if sg=="-" else "blue!70!black"}] at ({cx:.2f},-1.35) {{${sg}$}};')
SK=fig('\n'.join(o))
q('0013',tipId='tur-ekstrem',tip='Ekstremum ve değişim',z='orta',alt='f′ İşaret Çizelgesi',kaz='Türev fonksiyonunun işaret çizelgesinden f’nin artan-azalan aralıklarını ve ekstremum noktalarının türünü yorumlar.',kalip='öncüllü',
 kart='K-ATRV-05 (f′ işaret çizelgesi) · çift katlı kök: işaret değişmez, ekstremum yok',
 metin='Gerçel sayılar kümesinde türevlenebilir bir f fonksiyonunun türevi olan f′ fonksiyonunun işaret çizelgesi aşağıda verilmiştir.\nBuna göre,\nI. f, x = 1 apsisli noktasında yerel ekstremuma sahiptir.\nII. f, (−2, 4) aralığında artandır.\nIII. f, x = 4 apsisli noktasında yerel minimuma sahiptir.\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız II',yan=[('Yalnız I','f′(1) = 0 olduğu için x = 1’i ekstremum saymış; aynı noktada aralığı bölünmüş sanıp II’yi yanlış bulmuş.','bilgi'),('I ve II','f′’nün sıfır olduğu her noktayı ekstremum sanıp I’i doğru bulmuş; III’ü doğru saymamış.','bilgi'),('I ve III','Sıfır olan her noktayı ekstremum sanmış; x = 4’te + ’dan − ’ye geçişi minimum sanmış; II’yi yanlış saymış.','bilgi'),('I, II ve III','Sıfır olan her noktayı ekstremum saymış ve x = 4’te + ’dan − ’ye geçişi yerel minimum sanmış.','bilgi')],sira=OZ,
 istenen='Doğru olan öncüllerin hangileri olduğu.',ip=['f′’nün işaretini her aralıkta ayrı ayrı oku.'],bilgi=[ART],sekil=SK,
 ad=[A('İşareti oku','Çizelgeden aralıklara göre f′’nün işareti okunur.','x < −2: − · −2 < x < 1: + · 1 < x < 4: + · x > 4: −'),A('I’i değerlendir','x = 1’de f′ sıfır ama işaret + ’dan + ’ya devam eder.','Ekstremum yok → I yanlış'),A('II’yi değerlendir','(−2, 1) ve (1, 4)’te f′ pozitiftir; x = 1’de f sürekli artmayı sürdürür.','(−2, 4)’te f artan → II doğru'),A('III’ü değerlendir','x = 4’te f′ + ’dan − ’ye geçer; bu yerel maksimumdur.','Yerel minimum değil → III yanlış'),A('Sonuç','Yalnız II doğrudur.','Yalnız II')],
 puf='f′ = 0 olmak ekstremum için yetmez; işaretin değişip değişmediğine bak.')

# ================= 14 orta · türev tanımıyla limit =================
f2v,df2v=3,5
sx_=sp.Symbol('u'); ff=sp.Function('ff')
v=-4*df2v+f2v*4; assert v==-8
e=[-4*df2v,f2v*4,4*df2v+f2v*4,4*df2v-f2v*4]; assert e==[-20,12,32,8]; uniq(v,e)
# sayısal doğrulama: f(x) = 3 + 5(x−2) + (x−2)²
fq=lambda u:3+5*(u-2)+(u-2)**2
assert fq(2)==3 and sp.diff(3+5*(x-2)+(x-2)**2,x).subs(x,2)==5
assert sp.limit((x**2*3-4*(3+5*(x-2)+(x-2)**2))/(x-2),x,2)==-8
q('0014',tipId='tur-tanim',tip='Türev tanımı ve limit',z='orta',alt='Türev Tanımıyla Limit',kaz='Paydası sıfıra giden limitte payı f(2) ve f(x) cinsinden ayırarak türev tanımıyla limitin değerini hesaplar.',kalip='düz',
 kart='K-ATRV-01 (türev tanımı limiti) · iki parçaya ayrılan pay: f′(a) ve f(a)’lı terimler',
 metin='Gerçel sayılar kümesinde türevlenebilen bir f fonksiyonu için f(2) = 3 ve f′(2) = 5’tir.\nBuna göre,\nlim x→2  [x² · f(2) − 4 · f(x)] / (x − 2)\nlimitinin değeri kaçtır?',
 dogru=v,yan=[(e[0],'Payı ayırırken yalnız −4 · [f(x) − f(2)] / (x − 2) terimini düşünmüş: −4 · f′(2).','dikkat'),(e[1],'Yalnız f(2) · (x² − 4)/(x − 2) terimini hesaplamış: 3 × 4.','dikkat'),(e[2],'−4 · f′(2) terimini +20 yazıp iki terimi toplamış: 20 + 12.','islem'),(e[3],'Terimlerin işaretini ters yazıp 4 · f′(2) − 3 · 4 hesaplamış.','islem')],
 istenen='Verilen limitin değeri.',ip=['Pay x = 2’de 0 olur; türev tanımındaki fark bölümüne benzer bir terim ayırabilir misin?'],bilgi=[TAN],
 ad=[A('Payın sıfırlandığını gör','x = 2 için pay 4 · 3 − 4 · 3 = 0 olur; limit 0/0 belirsizliğindedir.','Pay(2) = 12 − 12 = 0'),A('Payı ayır','4 · f(2) ekleyip çıkararak iki fark oluşturulur.','x² · f(2) − 4f(x) = f(2)(x² − 4) − 4[f(x) − f(2)]'),A('Terimleri limite çevir','Her fark bölümü kendi limitine gider.','f(2) · lim (x + 2) − 4 · f′(2)'),A('Hesapla','Değerler yerine yazılır.','3 × 4 − 4 × 5 = −8')],
 puf='Belirsiz limitte pay ve paydaya f(a) ekleyip çıkararak türev tanımının fark bölümü elde edilebilir.')

# ================= 15 zor · f′ grafiği ve alanlar: f(x) = 5 denkleminin kök sayısı =================
A1,A2,A3=5,-3,4; f0=2
fv=[f0,f0+A1,f0+A1+A2,f0+A1+A2+A3]; assert fv==[2,7,4,8]
def kok(vals,k):
    n=0
    for p,q_ in zip(vals,vals[1:]):
        if (p-k)*(q_-k)<0: n+=1
        assert (p-k)!=0 and (q_-k)!=0
    return n
v=kok(fv,5); assert v==3
yanl_isaret=[f0,f0+A1,f0+A1+abs(A2),f0+A1+abs(A2)+A3]; assert kok(yanl_isaret,5)==1      # alanları işaretsiz toplama
yanl_son=[f0,f0+A1,f0+A1+A2,f0+A1+A2-A3]; assert yanl_son==[2,7,4,0] and kok(yanl_son,5)==2  # üçüncü bölgeyi çıkarma
assert fv[0]!=5 and fv[3]!=5          # uçlar kök değildir
e=[0,1,2,4]; uniq(v,e)
S1x,S1y=0.85,0.85
import math
def seg1(u): return 1.6*math.sin(math.pi*u/2)
def seg2(u): return -1.1*math.sin(math.pi*(u-2)/3)
def seg3(u): return 1.3*math.sin(math.pi*(u-5)/3)
def alan_poly(fn,a,b,renk):
    pts=ornek(fn,a,b,40)
    return f'\\fill[{renk}] ({a*S1x:.3f},0) -- '+' -- '.join(f'({p*S1x:.3f},{r*S1y:.3f})' for p,r in pts)+f' -- ({b*S1x:.3f},0) -- cycle;'
o=[alan_poly(seg1,0,2,'blue!22'),alan_poly(seg2,2,5,'orange!30'),alan_poly(seg3,5,8,'blue!22'),
 egri(ornek(seg1,0,2,40)+ornek(seg2,2,5,40)[1:]+ornek(seg3,5,8,40)[1:],S1x,S1y,MAVI,'2pt'),
 f'\\draw[-{{Stealth}},thick] (-0.3,0) -- ({8.9*S1x:.3f},0) node[right] {{$x$}};',
 f'\\draw[-{{Stealth}},thick] (0,{-1.6*S1y:.3f}) -- (0,{2.2*S1y:.3f}) node[above] {{$y$}};',
 etiket(1,0.5,S1x,S1y,'$A_1 = 5$','anchor=center'),etiket(3.5,-0.45,S1x,S1y,'$A_2 = 3$','anchor=center'),etiket(6.5,0.5,S1x,S1y,'$A_3 = 4$','anchor=center'),
 etiket(7.4,1.7,S1x,S1y,'$y=f\'(x)$','right',MAVI,'\\small\\bfseries')]
for tx in (2,5,8): o.append(f'\\draw ({tx*S1x:.3f},0.07) -- ({tx*S1x:.3f},-0.07); \\node[below=3pt,font=\\footnotesize] at ({tx*S1x:.3f},0) {{${tx}$}};')
o.append('\\node[below left=1pt,font=\\footnotesize] at (0,0) {$0$};')
SK=fig('\n'.join(o))
q('0015',tipId='tur-fgraf',tip='f′ grafiğinden f’yi yorumlama',z='zor',alt='f′ Grafiği ve Alanlar',kaz='f′ grafiği ile eksen arasındaki işaretli alanlardan f’nin değişimini bulup bir yatay doğruyla kesişim sayısını belirler.',kalip='grafik',
 kart='K-ATRV-04 (f′ grafiği ve işaretli alanlar) · alanlardan f’nin uç değerleri; yatay doğruyla kök sayısı',
 metin='Şekilde, türevlenebilir bir f fonksiyonu için y = f′(x) eğrisinin [0, 8] aralığındaki parçası ile x ekseninin sınırladığı üç bölge boyanmış ve her bölgenin alanı yazılmıştır.\nf(0) = 2\nolduğuna göre, [0, 8] aralığında f(x) = 5 denkleminin kaç farklı kökü vardır?',
 dogru=v,yan=[(e[0],'Yalnız uç noktalara bakmış: f(0) = 2 ve f(8) = 8 değerlerinin ikisi de 5 olmadığından kök yok sanmış.','dikkat'),(e[1],'Alanları işaretsiz toplayıp f(2) = 7, f(5) = 10, f(8) = 14 bulmuş; f’yi sürekli artan sanıp tek kök görmüş.','bilgi'),(e[2],'Üçüncü bölgenin alanını (eksenin üstünde) çıkarıp f(8) = 0 bulmuş; son artışta oluşan kökü saymamış.','dikkat'),(e[3],'Uç noktalar x = 0, 8 ile kritik noktalar x = 2, 5’in her birini bir kök sayıp 4 bulmuş.','dikkat')],
 istenen='f(x) = 5 denkleminin [0, 8] aralığındaki kök sayısı.',ip=['Bölgelerin eksenin üstünde ya da altında olması f için ne anlama gelir?'],bilgi=[ART,B('Alan ve değişim','f′ ile x ekseni arasındaki bölgenin alanı, f’nin o aralıktaki değişiminin büyüklüğüdür; bölge eksenin üstündeyse f artmış, altındaysa azalmıştır. Örnek: f′ eksenin üstünde 6 birimkarelik bir bölge çiziyorsa f bu aralıkta 6 artar')],sekil=SK,
 ad=[A('f′’nün işaretini oku','f′ eksenin üstündeyse f artar, altındaysa azalır.','[0, 2]: artan · [2, 5]: azalan · [5, 8]: artan'),A('Alanlardan değişimi bul','İşaretli alan, f’nin değişimine eşittir; altta kalan alan eksi alınır.','f(2) − f(0) = 5 · f(5) − f(2) = −3 · f(8) − f(5) = 4'),A('Kritik değerleri hesapla','f(0) = 2’den başlanır.','f(2) = 7 · f(5) = 4 · f(8) = 8'),A('Eğriyi yatay doğruyla kes','y = 5 doğrusu 2 → 7, 7 → 4 ve 4 → 8 yükselişlerinin her birini ayrı ayrı keser.','Üç aralıkta da 5 değeri alınır'),A('Kök sayısını yaz','Her aralıkta tam bir kök vardır.','3 kök')],
 puf='f′ ile eksen arasındaki alanlar f’nin değişimini işaretiyle verir; f’nin ardışık uç değerlerini bulunca kök sayısı yatay doğrunun kestiği parçalardan sayılır.')

# ================= 16 zor · hikâyeli şekil: kare kartondan kutu =================
Vf=(18-2*x)**2*x; sol=sp.solve(sp.diff(Vf,x),x); assert sorted(sol)==[3,9]
assert sp.diff(Vf,x,2).subs(x,3)<0
xo=3; tb=18-2*xo; v=tb**2+4*tb*xo; assert (tb,v)==(12,288) and v==18**2-4*xo**2
Vo=tb**2*xo; assert Vo==432
x6=6; tb6=18-2*x6; assert tb6==6 and Fr(tb6**2+4*tb6*x6)==180
e=[Vo,tb**2,18**2,tb6**2+4*tb6*x6]; assert e==[432,144,324,180]; uniq(v,e)
u=0.30; side=18*u; xd=1.15
o=['\\fill[orange!35] (0,0) rectangle (%.2f,%.2f);'%(xd,xd),'\\fill[orange!35] (%.2f,0) rectangle (%.2f,%.2f);'%(side-xd,side,xd),
 '\\fill[orange!35] (0,%.2f) rectangle (%.2f,%.2f);'%(side-xd,xd,side),'\\fill[orange!35] (%.2f,%.2f) rectangle (%.2f,%.2f);'%(side-xd,side-xd,side,side),
 '\\draw[thick] (0,0) rectangle (%.2f,%.2f);'%(side,side),
 '\\draw[dashed,thick,blue!70!black] (%.2f,0) -- (%.2f,%.2f); \\draw[dashed,thick,blue!70!black] (%.2f,0) -- (%.2f,%.2f);'%(xd,xd,side,side-xd,side-xd,side),
 '\\draw[dashed,thick,blue!70!black] (0,%.2f) -- (%.2f,%.2f); \\draw[dashed,thick,blue!70!black] (0,%.2f) -- (%.2f,%.2f);'%(xd,side,xd,side-xd,side,side-xd),
 '\\node[font=\\small] at (%.2f,%.2f) {$x$};'%(xd/2,xd/2),'\\node[font=\\small] at (%.2f,%.2f) {$x$};'%(side-xd/2,xd/2),
 '\\node[font=\\small] at (%.2f,%.2f) {$x$};'%(xd/2,side-xd/2),'\\node[font=\\small] at (%.2f,%.2f) {$x$};'%(side-xd/2,side-xd/2),
 '\\draw[{Stealth}-{Stealth}] (0,-0.35) -- (%.2f,-0.35); \\node[below,font=\\small] at (%.2f,-0.35) {$18$ cm};'%(side,side/2),
 '\\node[font=\\small,text=blue!70!black] at (%.2f,%.2f) {katlanacak taban};'%(side/2,side/2),
 '\\draw[fill=orange!35] (%.2f,%.2f) rectangle (%.2f,%.2f); \\node[right,font=\\footnotesize] at (%.2f,%.2f) {kesilen kare};'%(side+0.5,side-0.5,side+0.9,side-0.1,side+1.0,side-0.3)]
SK=fig('\n'.join(o))
q('0016',tipId='tur-optim',tip='Enbüyük ve enküçük değer problemleri',z='zor',alt='Kutu Hacmi Optimizasyonu',kaz='Kare kartondan köşe kesilerek yapılan kutunun hacmini x’e bağlı yazıp türevle en büyük hacmi veren x’i bulur ve yüzey alanını hesaplar.',kalip='hikâyeli',
 kart='K-ATRV-06 (köşeleri kesilen kare karton) · hacim fonksiyonundan x; ardından üstü açık kutunun yüzey alanı',
 metin='Bir atölyede, kenar uzunluğu şekilde verilen kare biçimli bir kartonun dört köşesinden birer kenarı x olan eş kareler kesiliyor. Kalan kısım kesikli çizgilerden katlanarak üstü açık dikdörtgenler prizması biçiminde bir kutu yapılıyor.\nKutunun hacmi en büyük olacak biçimde x seçildiğinde, bu kutunun yüzey alanı kaç santimetrekare olur?',
 dogru=v,yan=[(e[0],'Sorulan yüzey alanı yerine, en büyük hacmin değerini yazmış: 12² × 3.','dikkat'),(e[1],'Yüzey alanı olarak yalnız taban alanını almış: 12².','dikkat'),(e[2],'Kesilen karelerin alanını çıkarmayı unutup kartonun tüm alanını yazmış: 18².','dikkat'),(e[3],'Türevin çarpanını 18 − 6x yerine 18 − 3x yazıp x = 6 bulmuş: taban 6, alan 6² + 4 × 6 × 6.','islem')],
 istenen='En büyük hacimli kutunun yüzey alanı (üstü açık).',ip=['Önce taban kenarını x cinsinden yaz, sonra hacim fonksiyonunun türevinin köklerinden uygun olanı seç.'],bilgi=[OPT],sekil=SK,
 ad=[A('Hacmi x cinsinden yaz','Taban kenarı 18 − 2x, yükseklik x olur.','V(x) = (18 − 2x)² × x, 0 < x < 9'),A('Türevi al','Çarpım ve zincir kuralı uygulanır.','V′(x) = (18 − 2x)² + x × 2(18 − 2x)(−2) = (18 − 2x)(18 − 6x)'),A('Uygun kökü seç','Kökler 3 ve 9’dur; x = 9 için taban sıfır olur, x = 3 maksimumdur.','x = 3 → taban kenarı 12'),A('Yüzey alanını kur','Üstü açık kutunun alanı tabana dört yan yüzün eklenmesiyle bulunur.','12² + 4 × 12 × 3'),A('Hesapla','Toplanır.','144 + 144 = 288 cm²')],
 puf='Yüzey alanını kartonun alanından çıkarma yoluyla da kontrol edebilirsin.')

# ================= 17 zor · şekilli: parabolün içine yerleştirilen dikdörtgenin çevresi =================
a_=sp.symbols('a'); Aa=2*a_*(12-a_**2); sa=[s_ for s_ in sp.solve(sp.diff(Aa,a_),a_) if s_>0]; assert sa==[2]
w,h=4,8; assert w*h==32 and 12-4==8
v=2*(w+h); assert v==24
e=[w*h,w+h,2*(2+8),2*(4+10)]; assert e==[32,12,20,28]; uniq(v,e)
S3x,S3y=0.8,0.27
pa=lambda u:12-u*u; aa=1.5
o=[f'\\fill[vurgu!25] ({-aa*S3x:.3f},0) rectangle ({aa*S3x:.3f},{pa(aa)*S3y:.3f});',
 f'\\draw[{TUR},line width=1.8pt] ({-aa*S3x:.3f},0) rectangle ({aa*S3x:.3f},{pa(aa)*S3y:.3f});',
 egri(ornek(pa,-3.6,3.6),S3x,S3y,MAVI,'2pt'),
 f'\\draw[-{{Stealth}},thick] ({-4.2*S3x:.3f},0) -- ({4.4*S3x:.3f},0) node[right] {{$x$}};',
 f'\\draw[-{{Stealth}},thick] (0,-0.2) -- (0,{13.2*S3y:.3f}) node[above] {{$y$}};',
 nokta(0,12,S3x,S3y),f'\\node[left=2pt,font=\\footnotesize] at (0,{12*S3y:.3f}) {{$12$}};',
 etiket(2.3,9.6,S3x,S3y,'$y = 12 - x^2$','anchor=west',MAVI,'\\small\\bfseries'),
 nokta(aa,pa(aa),S3x,S3y,TUR),nokta(-aa,pa(aa),S3x,S3y,TUR),nokta(aa,0,S3x,S3y,TUR),nokta(-aa,0,S3x,S3y,TUR)]
SK=fig('\n'.join(o))
q('0017',tipId='tur-optim',tip='Enbüyük ve enküçük değer problemleri',z='zor',alt='Parabol İçinde Dikdörtgen',kaz='Parabol ile x ekseni arasına yerleştirilen simetrik dikdörtgenin alanını tek değişkenle yazıp türevle en büyük alanlı dikdörtgenin çevresini bulur.',kalip='şekilli',
 kart='K-ATRV-06 (parabol altında dikdörtgen) · alan fonksiyonunun maksimumu; istenen büyüklük çevre',
 metin='Şekilde, bir kenarı x ekseni üzerinde, üst köşeleri parabol üzerinde olan ve y eksenine göre simetrik bir dikdörtgen çizilmiştir.\nBu dikdörtgenin alanı en büyük olduğunda dikdörtgenin çevresi kaç birimdir?',
 dogru=v,yan=[(e[0],'Sorulan çevre yerine en büyük alanın değerini yazmış: 4 × 8.','dikkat'),(e[1],'Çevre yerine yarım çevreyi yazmış: 4 + 8.','dikkat'),(e[2],'Dikdörtgenin genişliğini 2a yerine a = 2 almış: 2(2 + 8).','islem'),(e[3],'Yüksekliği 12 − a² yerine 12 − a = 10 almış: 2(4 + 10).','islem')],
 istenen='Alanı en büyük olan dikdörtgenin çevresi.',ip=['Sağ üst köşenin apsisine a de; genişlik ve yüksekliği a cinsinden yaz.'],bilgi=[OPT],sekil=SK,
 ad=[A('Ölçüleri a cinsinden yaz','Sağ üst köşe (a, 12 − a²) noktasıdır; simetriden genişlik 2a olur.','Genişlik = 2a · Yükseklik = 12 − a²'),A('Alan fonksiyonunu kur','Alan, genişlik ile yüksekliğin çarpımıdır.','A(a) = 2a(12 − a²) = 24a − 2a³'),A('Türevi sıfırla','A′(a) = 0 çözülür ve pozitif kök alınır.','A′(a) = 24 − 6a² = 0 → a = 2'),A('Ölçüleri bul','a değeri yerine yazılır.','Genişlik 4 · yükseklik 12 − 4 = 8'),A('Çevreyi hesapla','Çevre, iki kenar toplamının iki katıdır.','2 × (4 + 8) = 24')],
 puf='Simetrik yerleştirilen şekillerde yarım genişliği değişken seç; istenen büyüklük (alan, çevre) için en sonda ölçüleri ayrı ayrı yaz.')

# ================= 18 zor · grafik: iki parabolün ortak teğeti =================
fa=lambda u:u**2+1
aa_,bb_=sp.symbols('aa bb')
sol=sp.solve([ -1+aa_+bb_-2, -2+aa_-2],[aa_,bb_]); assert sol=={aa_:4,bb_:-1}
ga=lambda u:-u**2+4*u-1
assert ga(1)==fa(1)==2 and sp.diff(-x**2+4*x-1,x).subs(x,1)==sp.diff(x**2+1,x).subs(x,1)==2
v=sp.Rational(ga(2)); assert v==3
sa_=sp.nsimplify  # yanlış zincirler
g_bad=-x**2+3*x+0                                        # türev katsayısı (2) unutulmuş: −x + a = 2 → a = 3, b = 0
a3=3; b3=2-(-1+a3); assert b3==0
mx_bad=sp.Rational(a3**2,4)+b3; assert mx_bad==sp.Rational(9,4)
e=[Fr(-1),Fr(1),Fr(2),Fr(9,4)]; uniq(Fr(3),e)
S4x,S4y=0.95,0.5
gc=lambda u:float(-u*u+4*u-1)
body=graf(-1,4,-1,7,S4x,S4y,'\n'.join([
 egri([(u/10,min(float(fa(u/10)),7.0)) for u in range(-8,25)],S4x,S4y,MAVI,'2pt'),
 egri([(u/10,gc(u/10)) for u in range(1,40)],S4x,S4y,TUR,'2pt'),
 egri([(-0.7,-1.4),(3.0,6.0)],S4x,S4y,YES,'1.6pt',',dashed'),
 cizgi(1,2,1,0,S4x,S4y,'black'),cizgi(1,2,0,2,S4x,S4y,'black'),nokta(1,2,S4x,S4y,'black','2.8pt'),
 etiket(1,2,S4x,S4y,'$A$','above left'),
 etiket(-0.8,1.7,S4x,S4y,'$f$','above',MAVI,'\\small\\bfseries'),etiket(3.3,float(gc(3.3)),S4x,S4y,'$g$','above right',TUR,'\\small\\bfseries'),
 etiket(3.0,6.0,S4x,S4y,'$d$','right',YES,'\\small\\bfseries')]),xt=[1],yt=[2],gx=False,gy=False)
SK=fig(body)
q('0018',tipId='tur-teget',tip='Teğet, normal ve eğim',z='zor',alt='Ortak Teğet',kaz='İki parabolün ortak noktada ortak teğete sahip olması koşuluyla değer ve türev eşitliklerinden katsayıları bulup yeni parabolün en büyük değerini hesaplar.',kalip='grafik',
 kart='K-ATRV-03 (iki parabolün ortak teğeti) · değer ve eğim eşitliğinden a, b; tepe ordinatı',
 metin='a ve b gerçel sayılar olmak üzere şekilde, f(x) = x² + 1 ve g(x) = −x² + ax + b parabollerinin grafikleri ile bu iki grafiğe A noktasında teğet olan d doğrusu verilmiştir.\nBuna göre, g fonksiyonunun alabileceği en büyük değer kaçtır?',
 dogru=3,yan=[(e[0],'a ve b değerlerinden sabit terimi b = −1’i en büyük değer sanmış.','dikkat'),(e[1],'A noktasının apsisini en büyük değer sanmış.','dikkat'),(e[2],'A noktasının ordinatını ya da tepe apsisi olan 2’yi en büyük değer olarak yazmış.','dikkat'),(e[3],'g′(x) = −2x + a yerine −x + a yazıp a = 3, b = 0 bulmuş: en büyük değer 9/4.','islem')],
 istenen='g fonksiyonunun en büyük değeri.',ip=['A noktasında iki fonksiyonun hem değerleri hem de türevleri eşittir.'],bilgi=[TEG],sekil=SK,
 ad=[A('A’nın koordinatını oku','Şekilde A’nın apsisi 1, ordinatı 2’dir; A her iki eğri üzerindedir.','f(1) = 2 = g(1)'),A('Değer eşitliğini yaz','g(1) = 2 koşulu bir denklem verir.','−1 + a + b = 2 → a + b = 3'),A('Eğim eşitliğini yaz','Ortak teğette türevler eşittir.','f′(1) = 2 · g′(1) = −2 + a = 2 → a = 4'),A('b’yi bul','a değeri yerine yazılır.','b = 3 − 4 = −1 → g(x) = −x² + 4x − 1'),A('En büyük değeri bul','Tepe apsisi x = 2’dir.','g(2) = −4 + 8 − 1 = 3')],
 puf='Ortak teğet, ortak noktada hem fonksiyon değerlerinin hem de türev değerlerinin eşit olması demektir; iki koşul iki bilinmeyeni verir.')

# ================= 19 zor · tablo: değişim tablosu ve f(x) = m denklemi =================
f19=x**3-3*x**2+5
assert sp.diff(f19,x)==3*x**2-6*x and f19.subs(x,0)==5 and f19.subs(x,2)==1
ms=[m for m in range(-10,20) if len(sp.Poly(f19-m,x).real_roots())==3 and len(set(sp.Poly(f19-m,x).real_roots()))==3]
assert ms==[2,3,4]; v=sum(ms); assert v==9
e=[len(ms),sum(range(1,6)),sum(range(2,6)),sum(range(1,5))]; assert e==[3,15,14,10]; uniq(v,e)
SK=tablo_svg(['x','(−∞, 0)','0','(0, 2)','2','(2, ∞)'],[['f′(x)','+','0','−','0','+'],['f(x)','artan','5','azalan','?','artan']])
q('0019',tipId='tur-ekstrem',tip='Ekstremum ve değişim',z='zor',alt='Değişim Tablosu ve Kök Sayısı',kaz='Değişim tablosundan polinomun katsayılarını belirleyip yerel uç değerleri ile yatay doğrunun üç farklı noktada kesilmesi koşulunu kullanır.',kalip='tablo',
 kart='K-ATRV-05 (değişim tablosu) · tabloda bilinmeyen uç değer; f(x) = m için üç farklı kök koşulu',
 metin='a, b ve c gerçel sayılar olmak üzere f(x) = x³ + ax² + bx + c polinom fonksiyonunun değişim tablosu aşağıda verilmiştir. Tabloda “?” ile gösterilen değer bilinmemektedir.\nBuna göre, f(x) = m denkleminin farklı üç gerçel kökü olması için m’nin alabileceği tam sayı değerlerinin toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Toplam yerine m’nin alabileceği tam sayı değerlerinin sayısını yazmış.','dikkat'),(e[1],'Uç değerleri de dahil edip m = 1, 2, 3, 4, 5 değerlerini toplamış.','dikkat'),(e[2],'Yalnız üst uç değeri dahil edip 2 + 3 + 4 + 5 toplamış.','dikkat'),(e[3],'Yalnız alt uç değeri dahil edip 1 + 2 + 3 + 4 toplamış.','dikkat')],
 istenen='m’nin alabileceği tam sayı değerlerinin toplamı.',ip=['Tablodaki sıfırlar f′’nün köküdür; bu iki koşul a ve b’yi, tablodaki değer c’yi verir.'],bilgi=[ART],sekil=SK,
 ad=[A('f′’yü kur','f′’nün kökleri 0 ve 2’dir; f′(x) = 3x² + 2ax + b.','f′(x) = 3x(x − 2) = 3x² − 6x'),A('a ve b’yi bul','Katsayılar karşılaştırılır.','2a = −6 → a = −3 · b = 0'),A('c’yi bul','Tabloda f(0) = 5’tir.','c = 5 → f(x) = x³ − 3x² + 5'),A('Bilinmeyen değeri bul','Yerel minimum x = 2’de oluşur.','f(2) = 8 − 12 + 5 = 1'),A('Kök koşulunu uygula','y = m doğrusu eğriyi üç noktada kesmeli: yerel minimum ile yerel maksimum arasında kalmalı, uçlar dahil değil.','1 < m < 5 → m = 2, 3, 4'),A('Topla','Tam sayılar toplanır.','2 + 3 + 4 = 9')],
 puf='Kök sayısı, y = m doğrusunun eğriyi kaç noktada kestiğinden bulunur.')

# ================= 20 zor · grafik: doğrusal f ve g′ grafikleri, zincir ve çarpım =================
f20=lambda u:2*u+1; dg=lambda u:5-u
assert f20(0)==1 and f20(2)==5 and dg(1)==4 and dg(5)==0
g1=2; assert f20(g1)==5
v=2*1*f20(g1)+1*2*dg(1); assert v==18
e=[2*f20(g1)+2,2*f20(g1),1*2*dg(1),2*1*f20(1)+1*2*dg(1)]; assert e==[12,10,8,14]; uniq(v,e)
S6x,S6y=0.85,0.4
body=graf(0,5,0,11,S6x,S6y,'\n'.join([
 egri([(0,1),(5,11)],S6x,S6y,MAVI,'2pt'),egri([(0,5),(5,0)],S6x,S6y,TUR,'2pt'),
 nokta(0,1,S6x,S6y,MAVI),nokta(2,5,S6x,S6y,MAVI),nokta(1,4,S6x,S6y,TUR),nokta(5,0,S6x,S6y,TUR),
 etiket(3.2,9.8,S6x,S6y,'$y=f(x)$','left',MAVI,'\\small\\bfseries'),etiket(0.1,5.1,S6x,S6y,'$y=g\'(x)$','above right',TUR,'\\small\\bfseries')]),xt=[1,2,3,4,5],yt=list(range(1,12)))
SK=fig(body)
q('0020',tipId='tur-kural',tip='Türev kuralları ve bileşke',z='zor',alt='Grafikten Zincir ve Çarpım',kaz='Doğrusal f ve g′ grafiklerini okuyup çarpım ve zincir kuralını birlikte uygulayarak bir noktadaki türevi hesaplar.',kalip='grafik',
 kart='K-ATRV-02 (iki doğru grafiği, g′ verilmiş) · k(x) = x² · f(g(x)) türevi; çarpım ve zincir birlikte',
 metin='Türevlenebilir f ve g fonksiyonları için, şekilde y = f(x) doğrusu ile g fonksiyonunun türev fonksiyonunun grafiği olan y = g′(x) doğrusu çizilmiştir.\ng(1) = 2 ve k(x) = x² · f(g(x))\nolduğuna göre, k′(1) değeri kaçtır?',
 dogru=v,yan=[(e[0],'Zincir kuralında iç türev g′(1) = 4’ü çarpmamış: 2 × 5 + 2.','bilgi'),(e[1],'Çarpım kuralının yalnız x² türevi olan ilk terimini hesaplamış: 2 × 1 × 5.','dikkat'),(e[2],'Çarpım kuralının yalnız ikinci terimini hesaplamış: 1 × 2 × 4.','dikkat'),(e[3],'f(g(1)) yerine f(1) = 3 okumuş: 2 × 3 + 2 × 4.','dikkat')],
 istenen='k(x) = x² · f(g(x)) fonksiyonunun türevinin x = 1’deki değeri.',ip=['Önce g(1) değerinde f’nin değerini ve eğimini bul; g′(1) değerini ikinci grafikten oku.'],bilgi=[KUR,ZIN],sekil=SK,
 ad=[A('Kuralı yaz','Çarpım kuralı ve iç içe fonksiyon için zincir kuralı birlikte kullanılır.','k′(x) = 2x × f(g(x)) + x² × f′(g(x)) × g′(x)'),A('f doğrusunu oku','Grafik (0, 1) ve (2, 5) noktalarından geçer; f(2) ve f′ bulunur.','f(x) = 2x + 1 → f′(x) = 2'),A('g′(1) değerini oku','g′ grafiği (1, 4) noktasından geçer.','g′(1) = 4'),A('x = 1 yaz','g(1) = 2 olduğundan f 2’de okunur.','f(g(1)) = f(2) = 5 · f′(g(1)) = 2'),A('Hesapla','Değerler yerine yazılır.','k′(1) = 2 × 5 + 1 × 2 × 4 = 18')],
 puf='Bileşkede f değeri de f′ değeri de iç fonksiyonun değerinde (burada g(1)) okunur; g′ ise x’in kendisinde okunur.')

# ---------- yazım ----------
import collections
for q_ in P.ANA: q_['kardes']=None
tmp='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/turev/bos.json'
P.yaz(os.path.join(HV,'ayt-mat','turev-1.json'),tmp)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Türev',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 12. sınıf matematik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','turev.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'şekilli',sum(1 for q_ in P.ANA if q_['sekil']))
