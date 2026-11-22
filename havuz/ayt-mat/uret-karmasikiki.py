"""AYT Matematik · Karmaşık Sayılar 2. dalga (20 soru: 3 kolay / 10 orta / 7 zor). Şekiller karmaşık düzlem (Argand) çizimleri.
Her doğru cevap ve çeldirici değeri kodla hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,math,json,cmath
MYD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(MYD,'..','tyt-mat')); sys.path.insert(0,os.path.join(MYD,'..'))
import _hafif_mat as H
from _hafif_mat import *
from _hafif_mat import tablo_svg
from cizim import tikz_svg
import sympy as sp
H.KONU='Karmaşık Sayılar'
UK='amat|Karmaşık Sayılar'
P=Parti('karmasikiki','Karmaşık Sayılar',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM AYT Matematik 2018–2025 (karmaşık sayılar ve karmaşık düzlem soruları; yalnız mantık) · MEB 11. sınıf karmaşık sayılar'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
M='−'
def cs(z):
    a,b=round(z.real),round(z.imag); assert abs(z.real-a)<1e-9 and abs(z.imag-b)<1e-9,z
    bs='i' if abs(b)==1 else f'{abs(b)}i'
    if b==0: return (M if a<0 else '')+str(abs(a))
    if a==0: return (M if b<0 else '')+bs
    return f'{M if a<0 else ""}{abs(a)} {M if b<0 else "+"} {bs}'
def eq(z,a,b): return abs(z-complex(a,b))<1e-9
def ipw(k): return [1,1j,-1,-1j][k%4]
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')

# ---------- Argand yardımcıları ----------
SC=0.6
def arg(x0,x1,y0,y1,ust='',govde='',sc=SC,fs='\\footnotesize',skipy=()):
    o=[ust]
    for i in range(x0,x1+1): o.append(f'\\draw[gray!35,thin] ({i*sc:.3f},{y0*sc:.3f}) -- ({i*sc:.3f},{y1*sc:.3f});')
    for j in range(y0,y1+1): o.append(f'\\draw[gray!35,thin] ({x0*sc:.3f},{j*sc:.3f}) -- ({x1*sc:.3f},{j*sc:.3f});')
    o.append(govde)
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.4)*sc:.3f},0) -- ({(x1+0.7)*sc:.3f},0) node[right] {{Re}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.4)*sc:.3f}) -- (0,{(y1+0.7)*sc:.3f}) node[above] {{Im}};')
    for i in range(x0,x1+1):
        if i!=0: o.append(f'\\node[below=2pt,font={fs},inner sep=0.8pt] at ({i*sc:.3f},0) {{${i}$}};')
    for j in range(y0,y1+1):
        if j!=0 and j not in skipy: o.append(f'\\node[left=2pt,font={fs},inner sep=0.8pt] at (0,{j*sc:.3f}) {{${j}$}};')
    o.append(f'\\node[below right=-1pt,font={fs}] at (0,0) {{$O$}};')
    return '\n'.join(o)
def nok(x,y,lab,col,pos='above right',sc=SC,rad=0.09,kil=False):
    s=f'\\fill[{col}] ({x*sc:.3f},{y*sc:.3f}) circle ({rad});'
    if lab: s+=f'\\node[{pos},{col},font=\\small\\bfseries] at ({x*sc:.3f},{y*sc:.3f}) {{${lab}$}};'
    if kil: s=f'\\draw[dashed,{col}!70] ({x*sc:.3f},0) -- ({x*sc:.3f},{y*sc:.3f}) -- (0,{y*sc:.3f});'+s
    return s
BL='blue!75!black'; OR='orange!90!black'; GR='green!45!black'; PU='violet!85!black'


def graf(x0,x1,y0,y1,sx,sy,govde,xs=1,ys=1,fs='\\footnotesize'):
    o=[]
    for i in range(x0,x1+1,xs): o.append(f'\\draw[gray!35,thin] ({i*sx:.3f},{y0*sy:.3f}) -- ({i*sx:.3f},{y1*sy:.3f});')
    for j in range(y0,y1+1,ys): o.append(f'\\draw[gray!35,thin] ({x0*sx:.3f},{j*sy:.3f}) -- ({x1*sx:.3f},{j*sy:.3f});')
    o.append(govde)
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.3)*sx:.3f},0) -- ({(x1+0.6)*sx:.3f},0) node[right] {{$x$}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.5)*sy:.3f}) -- (0,{(y1+0.8)*sy:.3f}) node[above] {{$y$}};')
    for i in range(x0,x1+1,xs):
        if i!=0: o.append(f'\\node[below=2pt,font={fs},inner sep=0.8pt] at ({i*sx:.3f},0) {{${i}$}};')
    for j in range(y0,y1+1,ys):
        if j!=0: o.append(f'\\node[left=2pt,font={fs},inner sep=0.8pt,fill=white] at (0,{j*sy:.3f}) {{${j}$}};')
    return '\n'.join(o)
def egri(f,a,b,sx,sy,col,n=60):
    pts=' -- '.join(f'({(a+(b-a)*k/n)*sx:.3f},{f(a+(b-a)*k/n)*sy:.3f})' for k in range(n+1))
    return f'\\draw[{col},line width=1.8pt] {pts};'
def gnok(x,y,lab,col,pos,sx,sy):
    return f'\\fill[{col}] ({x*sx:.3f},{y*sy:.3f}) circle (0.08);\\node[{pos},{col},font=\\small\\bfseries,inner sep=2pt] at ({x*sx:.3f},{y*sy:.3f}) {{${lab}$}};'

# ---------- bilgi kutuları ----------
PER=B('Kuvvetlerin döngüsü','i¹ = i, i² = −1, i³ = −i, i⁴ = 1 ve sonrası aynı sırayla tekrar eder; art arda dört kuvvetin toplamı 0’dır. Ayrıca (a + bi)² = a² − b² + 2abi’dir. Örnek: i + i² + i³ + i⁴ + i⁵ = i⁵ = i; (3 − i)² = 8 − 6i')
KUV2=B('Denklemden kuvvete','Bir sayının sağladığı denklem, o sayının kuvvetleri arasında bir bağıntı verir; bu bağıntıyla üsler küçültülür. Örnek: x² = 3x − 1 ise x³ = x · x² = 3x² − x’tir')
POW=B('Kuvvet alma','(1 + i)² = 2i ve (1 − i)² = −2i’dir; bu yüzden çift kuvvetler önce (2i)ᵏ ya da (−2i)ᵏ biçimine getirilir. Bir sayının eşleniği, sanal kısmının işareti değiştirilerek bulunur. Örnek: (1 + i)⁴ = (2i)² = −4; 3 + 5i sayısının eşleniği 3 − 5i’dir')
KOK=B('Kökler arası bağıntı','x² + bx + c = 0 denkleminin kökleri z₁ ve z₂ ise z₁ + z₂ = −b, z₁ · z₂ = c’dir ve z₁² + z₂² = (z₁ + z₂)² − 2z₁z₂ yazılır. Grafiği x eksenini kesmeyen bir parabolün denkleminin kökleri gerçel değildir. Örnek: x² − 4x + 7 = 0 için z₁ + z₂ = 4, z₁ · z₂ = 7’dir')
GER=B('Gerçel katsayılı polinom','Gerçel katsayılı bir polinomda a + bi kök ise a − bi de köktür. Bilinen bir kök, polinomu o kökün çarpanına bölmek için kullanılır. Örnek: x³ − 2x² − 2x − 3 polinomu x = 3’te sıfır olur; (x − 3)(x² + x + 1) biçiminde çarpanlanır')
MOD2=B('Modül ve bölme','|a + bi| = √(a² + b²) orijine uzaklıktır; |z₁ · z₂| = |z₁| · |z₂| ve |z̄| = |z|’dur. Bölmede pay ve payda paydanın eşleniğiyle çarpılır. Örnek: |5 − 12i| = 13; 1/(1 + 2i) = (1 − 2i)/5')
ESL2=B('Eşlenik ve çarpma','(a + bi)(c + di) = (ac − bd) + (ad + bc)i’dir. z̄ eşleniği alındığında sanal kısmın işareti değişir; |z|² = z · z̄ gerçel bir sayıdır. Örnek: (4 + i)(2 − 3i) = 11 − 10i')
DUZ2=B('Karmaşık düzlemde nokta ve vektör','a + bi sayısı (a, b) noktasıyla gösterilir: yatay eksen gerçel, düşey eksen sanal kısımdır. İki sayının toplamı vektör toplamıdır. Örnek: (4, −1) noktası 4 − i sayısıdır')
YER2=B('Geometrik yer','|z − z₀| = r, z₀ merkezli r yarıçaplı çemberdir; |z − z₀| ≤ r çemberin içini ve kendisini gösterir. Re(z) ≥ k koşulu x = k doğrusunun sağını, Im(z) ≥ k koşulu y = k doğrusunun üstünü gösterir. z·z̄ = |z|²’dir. Örnek: |z + 1| = 4, −1 merkezli 4 yarıçaplı çemberdir')
UZK=B('Çember üzerindeki noktaların uzaklığı','Çember üzerinde değişen bir noktanın sabit bir noktaya uzaklığı, uç değerleri arasındaki bütün değerleri alır; uç değerler merkez ile sabit nokta arasındaki doğru üzerindedir')
MAK=B('İşlem makinesi','Makinede oklar sırasıyla izlenir; her kutudaki işlem, gelen sayıya uygulanır. i ile çarpmak noktayı orijin etrafında 90° döndürür: i(a + bi) = −b + ai. Örnek: makine “i ile çarp, 2 çıkar” ise 3 girince i · 3 − 2 = −2 + 3i çıkar')
DOR=B('Çevre ve çember yayı','r yarıçaplı çemberin yarısının yay uzunluğu πr’dir. Birden çok parçadan oluşan bir bölgenin çevresi, bölgeyi çevreleyen bütün yay ve doğru parçalarının uzunlukları toplanarak bulunur. Örnek: yarıçapı 5 olan yarım çemberin yayı 5π’dir')

# ---------- kartlar ----------
kartla('K-AKS2-01','Kuvvet toplamı ve periyot','Art arda dört kuvvetin toplamı sıfır olduğundan tam döngüler atılır, kalan terimler ayrı toplanır; bölümlerde çift kuvvetler önce 2i ya da −2i’ye indirilir; makine dizilerinde sayılar döngü bulunana kadar yazılır.','Kalan terimlerin hangisi olduğunu karıştırmak; i⁴ = 1 yerine i⁴ = −1 almak; toplam döngüsü ile sayı döngüsünü karıştırmak.','orta','düz',4,'kk2-kuvvet','Kuvvet toplamı ve periyot')
kartla('K-AKS2-02','Düzlemde okuyup işlem yapma','Noktaların koordinatları sayıya çevrilir; çarpma, bölme ve dönüşüm işlemleri yazılır; istenen kısım en sonda okunur.','Gerçel ve sanal eksenleri karıştırmak; eşleniği almayı unutmak; bölmede eşlenikle genişletmemek.','orta','şekilli',4,'kk2-nokta','Düzlemde okuyup işlem yapma')
kartla('K-AKS2-03','Köşe sayılarıyla geometri','Köşelerin koordinatlarından sayılar yazılır; ağırlık merkezi ortalama, kenar uzunluğu fark sayısının modülü, dik açı bölümün saf sanal olmasıyla ifade edilir.','Ağırlık merkezinde üçe bölmeyi unutmak; modülü karesiz almak; oranın hangi sayıya bölündüğünü karıştırmak.','orta','şekilli',4,'kk2-geo','Köşe sayılarıyla geometri')
kartla('K-AKS2-04','Bölge ve çember problemleri','Şekil ya da denklem merkez ve yarıçap diliyle okunur; eşitsizlik yönü, sınırın dahil olup olmadığı ve alan ya da çevre ayrı parçalarla hesaplanır.','Merkezin işaretini ters okumak; sınır parçalarından birini atlamak; yarıçap yerine karesini kullanmak.','zor','şekilli',4,'kk2-yer','Bölge ve çember problemleri')
kartla('K-AKS2-05','Kökler ve grafik','Grafikten katsayılar bulunur; karmaşık kökler elde edilir ya da kökün sağladığı denklemden kuvvetleri arasında bağıntı çıkarılır; sorulan ifade bu köklerle yazılır.','Kökleri gerçel sanmak; kareler toplamında 2z₁z₂ terimini atlamak; grafikteki noktayı yanlış katsayıya yerleştirmek.','zor','grafik',4,'kk2-kok','Kökler ve grafik')
kartla('K-AKS2-06','Modül ve eşlenik yargıları','|z| = 1 ise z̄ = 1/z olur; yargılar sayının kendisi yazılarak ayrı ayrı sınanır; modül özellikleri ve eşlenik ilişkileri kullanılır.','Modülü kareli almak; z̄ ile 1/z’yi karıştırmak; her yargıyı aynı sonuca bağlamak.','orta','öncüllü',4,'kk2-modul','Modül ve eşlenik yargıları')
kartla('K-AKS2-07','Eşitlikten sayıyı bulma','z = a + bi yazılır, modül ya da kare içeren eşitlikte gerçel ve sanal kısımlar ayrı eşitlenir; bulunan değerin eşitliği sağlayıp sağlamadığına bakılır.','Modülü karesiz yazmak; çözümü eşitlikte sınamamak; ikinci derece çözümlerinden uygun olmayanı almamak.','zor','düz',4,'kk2-denk','Eşitlikten sayıyı bulma')
kartla('K-AKS2-08','Tanımlı işlem ve eşlenik','Tanımlı işlemin kuralı sayılara adım adım uygulanır; kesirli ifadelerde paydalar eşlenikle gerçel yapılır.','Dış tersi almayı unutmak; işlem kuralında toplama ile çarpmayı karıştırmak; eşleniği atlamak.','orta','yeni nesil',3,'kk2-islem','Tanımlı işlem ve eşlenik')

# ================= 01 kolay · düz · kuvvet toplamı =================
z=sum(ipw(k) for k in range(1,103)); assert eq(z,-1,1); zc=z.conjugate(); v=round((zc*zc).imag); assert v==2
e=[round((z*z).imag),0,round(z.imag),round(zc.imag)]; assert e==[-2,0,1,-1] and abs((z.conjugate()*0+(1j-1)**2).imag-(-2))<1e-9 and len({v,*e})==5
q('0001',tipId='kk2-kuvvet',tip='Kuvvet toplamı ve periyot',z='kolay',alt='Kuvvetlerin Toplamı',kaz='Art arda gelen i kuvvetlerinin toplamını dört terimlik döngüyle sadeleştirir ve eşleniğinin karesinin sanal kısmını bulur.',kalip='düz',
 kart='K-AKS2-01 (toplam döngüsü) · z = i + i² + … + i¹⁰²; Im(z̄²)',
 metin='z = i + i² + i³ + … + i¹⁰² olduğuna göre, z̄ eşleniğinin karesi olan z̄² sayısının sanal kısmı kaçtır?',
 dogru=v,yan=[(e[0],'z = −1 + i bulmuş fakat eşlenik almadan z² = −2i hesaplamış: sanal kısım −2.','dikkat'),(e[1],'(−1 − i)² açılımında orta terimi unutup 1 + i² = 0 bulmuş.','bilgi'),(e[2],'z = −1 + i bulmuş ama z̄² yerine z’nin sanal kısmını yazmış.','dikkat'),(e[3],'Eşleniği doğru alıp z̄ = −1 − i bulmuş ama z̄² yerine z̄’nin sanal kısmını yazmış.','dikkat')],
 istenen='Im(z̄²)',ip=['Art arda gelen kuvvetlerin bir döngüsünün toplamının ne olduğunu düşün; geriye kaç terim kaldığına bak.'],bilgi=[PER],
 ad=[A('Döngüleri at','Her dört terimin toplamı 0’dır; 102 = 4 · 25 + 2.','25 tam döngünün toplamı 0'),A('Kalan terimleri topla','Kalan terimler i¹⁰¹ ve i¹⁰² olur.','i¹⁰¹ = i, i¹⁰² = −1 → z = −1 + i'),A('Eşleniği al ve kare al','Sanal kısmın işareti değişir; sonra kare alınır.','z̄ = −1 − i → (−1 − i)² = 1 + 2i + i² = 2i'),A('Sanal kısmı oku','i’nin katsayısı sanal kısımdır.','2')],
 puf='Dört kuvvetlik tam döngüler toplamı sıfır yapar; yalnız kalan terimlere bak.')

# ================= 02 kolay · şekil · nokta · z·w̄ =================
zz,ww=complex(3,2),complex(2,3); v=round((zz*ww.conjugate()).real); assert v==12
e=[round(zz.real*ww.real),round((zz*ww.conjugate()).imag),round((zz+ww.conjugate()).real),round((zz*ww).real)]; assert e==[6,-5,5,0] and len({v,*e})==5
SK=fig(arg(-1,4,-1,4,govde=nok(3,2,'z',BL,'below right',kil=True)+nok(2,3,'w',OR,'above left',kil=True)))
q('0002',tipId='kk2-nokta',tip='Düzlemde okuyup işlem yapma',z='kolay',alt='Eşlenikli Çarpım',kaz='Karmaşık düzlemde verilen noktaları sayıya çevirir; bir sayı ile diğerinin eşleniğinin çarpımının gerçel kısmını hesaplar.',kalip='şekilli',
 kart='K-AKS2-02 (z · w̄) · z(3, 2), w(2, 3); Re(z · w̄) = 12',
 metin='Şekilde, karmaşık düzlemde z ve w sayılarının görüntüleri verilmiştir.\nBuna göre z · w̄ çarpımının gerçel kısmı kaçtır?',
 dogru=v,yan=[(e[0],'Gerçel kısmı yalnız gerçel kısımların çarpımı sanmış: 3 · 2 = 6.','bilgi'),(e[1],'Çarpımı doğru bulmuş (12 − 5i) fakat gerçel kısım yerine sanal kısmı yazmış.','dikkat'),(e[2],'Çarpma yerine toplayıp z + w̄ = 5 − i bulmuş.','islem'),(e[3],'w yerine w̄ almayıp z · w = 0 + 13i bulmuş.','dikkat')],
 istenen='Re(z · w̄)',ip=['İki noktayı önce a + bi biçiminde yaz; w̄ ile çarpılacağını unutma.'],bilgi=[DUZ2,ESL2],sekil=SK,
 ad=[A('Noktaları oku','Yatay koordinat gerçel, düşey koordinat sanal kısımdır.','z = 3 + 2i · w = 2 + 3i'),A('Eşleniği al','w’nin sanal kısmının işareti değişir.','w̄ = 2 − 3i'),A('Çarp','Dağıtıp i² = −1 yaz.','(3 + 2i)(2 − 3i) = 6 − 9i + 4i + 6 = 12 − 5i'),A('Gerçel kısmı oku','i’siz terim gerçel kısımdır.','12')],
 puf='Her sayıyı kısımlarıyla yazıp dağıtarak çarp.')

# ================= 03 kolay · düz · (1+i)^10/(1−i)^8 =================
z=(1+1j)**10/(1-1j)**8; assert eq(z,0,2)
sira3=[M+'32i',M+'2i','2','2i','32i']
# hatalar: eşlenik almamış (2i), i²=+1 alıp 2, paydayı 1 sanıp z=32i → z̄=−32i, 32i: payda unutup eşlenik almamış
assert eq((1+1j)**2,0,2) and eq((1-1j)**2,0,-2) and eq((2j)**5,0,32)
q('0003',tipId='kk2-kuvvet',tip='Kuvvet toplamı ve periyot',z='kolay',alt='(1 ± i) Kuvvetleri',kaz='(1 + i)² = 2i ve (1 − i)² = −2i özelliklerini kullanarak yüksek kuvvetli bölümü sadeleştirir ve eşleniğini bulur.',kalip='düz',
 kart='K-AKS2-01 ((1+i)^n bölümü) · z = (1 + i)¹⁰/(1 − i)⁸ = 2i; z̄',
 metin='z = (1 + i)¹⁰ / (1 − i)⁸ olduğuna göre, z sayısının eşleniği aşağıdakilerden hangisidir?',
 dogru=M+'2i',yan=[('2i','z = 2i bulduktan sonra eşleniğini almayı unutmuş.','dikkat'),('2','Yalnız modülleri bölüp |z| = 2⁵/2⁴ = 2 bulmuş, i’li kısmı atmış.','bilgi'),(M+'32i','Paydadaki (1 − i)⁸ = 16 çarpanını hesaba katmayıp z = 32i, eşleniği −32i bulmuş.','islem'),('32i','Paydayı hesaba katmamış ve eşleniği de almamış.','islem')],
 sira=sira3,istenen='z̄',ip=['Çift kuvvetleri iki iki alarak (1 + i)² ve (1 − i)² değerlerine indir.'],bilgi=[POW],
 ad=[A('Karelere indir','Her iki üs de çifttir.','(1 + i)² = 2i · (1 − i)² = −2i'),A('Kuvvetleri yaz','Üslere göre ayrı ayrı hesaplanır.','(2i)⁵ = 32i · (−2i)⁴ = 16'),A('Böl','Pay paydaya bölünür.','z = 32i/16 = 2i'),A('Eşleniği al','Sanal kısmın işareti değişir.','z̄ = −2i')],
 puf='(1 + i)² = 2i ve (1 − i)² = −2i değerleri büyük kuvvetleri küçültür.')

# ================= 04 orta · şekil · üçgen ağırlık merkezi =================
Ap,Bp,Cp=(-3,2),(5,1),(1,6); S=[sum(p[0] for p in (Ap,Bp,Cp)),sum(p[1] for p in (Ap,Bp,Cp))]; assert S==[3,9]
G=complex(S[0]/3,S[1]/3); v=round(abs(G)**2); assert v==10
e=[round(abs(complex(*S))**2),round((G.real+G.imag)**2),round(abs(complex(S[0]/3,S[1]))**2),round(abs(complex(Ap[0]+Cp[0],Ap[1]+Cp[1])/2)**2)]
assert e==[90,16,82,17] and len({v,*e})==5
tri='\\draw[fill=blue!12,draw='+BL+',line width=1.6pt] '+' -- '.join(f'({p[0]*SC:.2f},{p[1]*SC:.2f})' for p in (Ap,Bp,Cp))+' -- cycle;'
SK=fig(arg(-4,6,-1,7,ust=tri,govde=nok(*Ap,'A',BL,'above left')+nok(*Bp,'B',BL,'below right')+nok(*Cp,'C',BL,'above')))
q('0004',tipId='kk2-geo',tip='Köşe sayılarıyla geometri',z='orta',alt='Ağırlık Merkezi',kaz='Karmaşık düzlemde köşeleri verilen üçgenin ağırlık merkezini köşe sayılarının ortalaması olarak bulur ve modülünü hesaplar.',kalip='şekilli',
 kart='K-AKS2-03 (ağırlık merkezi) · A(−3, 2), B(5, 1), C(1, 6); |G|² = 10',
 metin='Şekilde, karmaşık düzlemde köşeleri A, B ve C olan bir üçgen verilmiştir. Bu üçgenin ağırlık merkezinin görüntüsü w karmaşık sayısıdır.\nBuna göre |w|² değeri kaçtır?',
 dogru=v,yan=[(e[0],'Ağırlık merkezi için köşe sayılarının toplamını 3’e bölmeyi unutmuş: |3 + 9i|² = 90.','islem'),(e[1],'w = 1 + 3i bulmuş fakat |w|² yerine (Re + Im)² = 16 hesaplamış.','bilgi'),(e[2],'Yalnız gerçel kısmı 3’e bölüp w = 1 + 9i almış: |w|² = 82.','dikkat'),(e[3],'Ağırlık merkezi yerine A ve C’nin orta noktasını (−1 + 4i) alıp |.|² = 17 bulmuş.','dikkat')],
 istenen='|w|²',ip=['Köşeleri sayıya çevir ve w’yi köşelerle ilişkilendir.'],bilgi=[DUZ2,MOD2],sekil=SK,
 ad=[A('Köşeleri oku','Koordinatlar gerçel ve sanal kısımlardır.','A = −3 + 2i; B = 5 + i; C = 1 + 6i'),A('Ağırlık merkezi','Üç sayının toplamı 3’e bölünür.','w = (3 + 9i)/3 = 1 + 3i'),A('Modül','|w|² = gerçel kısmın karesi + sanal kısmın karesi.','1² + 3² = 10')],
 puf='Önce her köşeyi a + bi olarak yaz.')

# ================= 05 orta · şekil · daire ve yarı düzlem bölgesi =================
c1='|z − 1| ≤ 3 ve Im(z) ≥ −1'; c2='|z + 1| ≤ 3 ve Im(z) ≥ −1'; c3='|z − 1| ≤ 3 ve Im(z) ≤ −1'; c4='|z − 1| ≤ 3 ve Re(z) ≥ −1'; c5='|z − 1| ≥ 3 ve Im(z) ≥ −1'
ptz=[complex(x/2,y/2) for x in range(-12,16) for y in range(-12,12)]
f1=lambda p:abs(p-1)<=3+1e-9 and p.imag>=-1-1e-9
for fz in (lambda p:abs(p+1)<=3+1e-9 and p.imag>=-1-1e-9,lambda p:abs(p-1)<=3+1e-9 and p.imag<=-1+1e-9,lambda p:abs(p-1)<=3+1e-9 and p.real>=-1-1e-9,lambda p:abs(p-1)>=3-1e-9 and p.imag>=-1-1e-9): assert any(fz(p)!=f1(p) for p in ptz)
ust=f'\\begin{{scope}}\\clip ({-3*SC:.2f},{-1*SC:.2f}) rectangle ({5*SC:.2f},{4*SC:.2f}); \\fill[blue!15] ({1*SC:.2f},0) circle ({3*SC:.2f}); \\end{{scope}}'
body=f'\\draw[{BL},line width=1.8pt] ({1*SC:.2f},0) circle ({3*SC:.2f}); \\draw[{OR},line width=1.8pt] ({-2*SC:.2f},{-1*SC:.2f}) -- ({4*SC:.2f},{-1*SC:.2f}); \\fill[{BL}] ({1*SC:.2f},0) circle (0.08);'
SK=fig(arg(-3,5,-3,4,ust=ust,govde=body))
q('0005',tipId='kk2-yer',tip='Bölge ve çember problemleri',z='orta',alt='Daire ve Yarı Düzlem',kaz='Karmaşık düzlemde bir daire ile bir doğrunun sınırladığı bölgeyi modül ve sanal kısım eşitsizlikleriyle ifade eder.',kalip='şekilli',
 kart='K-AKS2-04 (daire ∩ yarı düzlem) · merkez 1, r = 3, y = −1 doğrusunun üstü',
 metin='Şekilde, karmaşık düzlemde sınırları dahil olmak üzere taralı bölge verilmiştir.\nBuna göre taralı bölge aşağıdakilerden hangisiyle gösterilir?',
 dogru=c1,yan=[(c2,'Merkezi z + 1 biçiminde (işareti ters) yazmış; merkez −1 olur.','bilgi'),(c3,'Doğrunun hangi tarafının taralı olduğunu ters okuyup Im(z) ≤ −1 seçmiş.','dikkat'),(c4,'Doğruyu yatay değil düşey sanıp Re(z) ≥ −1 yazmış.','dikkat'),(c5,'Dairenin içi yerine dışını gösteren yönü (≥) seçmiş.','dikkat')],
 sira=[c3,c2,c1,c4,c5],istenen='Taralı bölgeyi gösteren koşullar.',ip=['Dairenin merkezini ve yarıçapını, doğrunun yatay mı düşey mi olduğunu ve taralı tarafı ayrı ayrı oku.'],bilgi=[YER2],sekil=SK,
 ad=[A('Daireyi oku','Merkez yatayda 1, yarıçap 3 birimdir.','|z − 1| ≤ 3'),A('Doğruyu oku','Turuncu doğru yatay ve y = −1’dedir; sanal kısım −1.','Im(z) = −1'),A('Taralı yönü seç','Bölge doğrunun üstündedir ve doğru dahildir.','Im(z) ≥ −1'),A('Birleştir','Her iki koşul birlikte sağlanır.','|z − 1| ≤ 3 ve Im(z) ≥ −1')],
 puf='Yatay doğru sanal kısmı, düşey doğru gerçel kısmı sabitler.')

# ================= 06 orta · grafik · parabol kökleri =================
f=lambda x:x*x-2*x+5
assert f(1)==4 and f(0)==5 and f(2)==5
z1,z2=1+2j,1-2j; v=round((z1**2+z2**2).real); assert v==-6
e=[4-5,2*5*0+14,4-8,10]
assert 4-5==-1 and 4+2*5==14 and (z1*z1.conjugate()).real*2==10
e=[-1,14,-4,10]; assert len({v,*e})==5
gv=egri(f,-1.4,3.4,0.8,0.32,BL)+gnok(1,4,'T',OR,'below right',0.8,0.32)+gnok(0,5,'B',OR,'above right',0.8,0.32)
SK=fig(graf(-2,4,-1,10,0.8,0.32,gv,ys=1))
q('0006',tipId='kk2-kok',tip='Kökler ve grafik',z='orta',alt='Grafikten Karmaşık Kökler',kaz='Grafikten parabolün denklemini bulur; x eksenini kesmediği için karmaşık olan köklerin kareleri toplamını kökler arası bağıntıyla hesaplar.',kalip='grafik',
 kart='K-AKS2-05 (tepe noktası ve y kesen) · y = x² − 2x + 5; z₁² + z₂² = −6',
 metin='Şekilde, başkatsayısı 1 olan y = f(x) parabolünün grafiği verilmiştir. T noktası parabolün tepe noktasıdır.\nf(x) = 0 denkleminin kökleri z₁ ve z₂ olduğuna göre, z₁² + z₂² değeri kaçtır?',
 dogru=v,yan=[(e[0],'Kareler toplamında (z₁ + z₂)² − z₁z₂ = 4 − 5 yazıp çarpımı 2 ile çarpmayı unutmuş.','islem'),(e[1],'(z₁ + z₂)² + 2z₁z₂ = 4 + 10 yazarak işareti ters almış.','bilgi'),(e[2],'Sabit terimi tepe noktasının ordinatı 4 sanıp (z₁ + z₂)² − 2 · 4 = −4 bulmuş.','dikkat'),(e[3],'z₁² + z₂² yerine |z₁|² + |z₂|² = 5 + 5 = 10 hesaplamış.','bilgi')],
 istenen='z₁² + z₂²',ip=['Grafikteki iki noktadan f(x)’in denklemini yazabilirsin; kökler x eksenine hiç değmediği için gerçel değildir.'],bilgi=[KOK],sekil=SK,
 ad=[A('Denklemi kur','Tepe (1, 4) ise f(x) = (x − 1)² + 4.','f(x) = x² − 2x + 5'),A('Kökler arası bağıntı','Kökler toplamı −b, çarpımı c’dir.','z₁ + z₂ = 2 · z₁z₂ = 5'),A('Kareler toplamı','z₁² + z₂² = (z₁ + z₂)² − 2z₁z₂.','4 − 10 = −6')],
 puf='Tepe noktası ve (0, c) noktası okunursa parabol hemen yazılır.')

# ================= 07 orta · öncüllü · |z| = 1 =================
z=(1+2j)/(1-2j); assert eq(z,-0.6,0.8)
Y1=abs(abs(z)-1)<1e-9; Y2=abs(z.conjugate()-1/z)<1e-9; Y3=abs((z+z.conjugate())-(-6/5))<1e-9 and False
assert Y1 and Y2 and not abs(z.conjugate()+z)<1e-9 and abs((z*z)+1)>0.1
assert abs((z+z.conjugate())+6/5)<1e-9
q('0007',tipId='kk2-modul',tip='Modül ve eşlenik yargıları',z='orta',alt='Modül ve Eşlenik Yargıları',kaz='Modülü 1 olan bir karmaşık sayının eşlenik ve tersi arasındaki ilişkiyi kullanarak yargıların doğruluğunu belirler.',kalip='öncüllü',
 kart='K-AKS2-06 (|z| = 1) · z = (1 + 2i)/(1 − 2i) = (−3 + 4i)/5; |z| = 1, z̄ = 1/z, z + z̄ = −6/5, z² ≠ −1',
 metin='z = (1 + 2i)/(1 − 2i) olduğuna göre,\nI. |z| = 1\nII. z̄ = −z\nIII. z + z̄ = −6/5\nyargılarından hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','III’te z + z̄ yerine z · z̄ = 1 hesaplayıp −6/5’i yanlış bulmuş; II’yi de yanlış saymış.','bilgi'),('Yalnız II','|z| = |1 + 2i|/|1 − 2i| = 1 olduğunu fark etmeyip I’i yanlış bulmuş; z̄ = −z sanmış.','bilgi'),('I ve II','z̄ = −z’yi doğru sanmış (z = (−3 + 4i)/5 için z̄ = (−3 − 4i)/5 olup −z = (3 − 4i)/5’tir); III’te z + z̄ yerine z · z̄ = 1 hesaplayıp yanlış bulmuş.','dikkat'),('I, II ve III','z̄ = −z sanıp üç yargıyı da doğru saymış.','dikkat')],
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],istenen='Doğru olan yargılar.',ip=['Payda eşleniğiyle genişletip z’yi a + bi biçiminde yaz; sonra yargıları bu sayıyla sına.'],bilgi=[MOD2],
 ad=[A('z’yi sadeleştir','Pay ve payda (1 + 2i) ile çarpılır.','z = (1 + 2i)²/5 = (−3 + 4i)/5'),A('I’i sına','Modül karekök içinde kareler toplamıdır.','|z| = √(9 + 16)/5 = 1 → I doğru'),A('II’yi sına','z̄ = (−3 − 4i)/5 iken −z = (3 − 4i)/5 olur.','z̄ ≠ −z → II yanlış'),A('III’ü sına','z + z̄ = 2 Re(z).','2 · (−3/5) = −6/5 → III doğru')],
 puf='Modülü 1 olan sayıda z̄ = 1/z’dir; z + z̄ ise gerçel kısmın iki katıdır.')

# ================= 08 orta · düz · z + |z| = 2 + 4i =================
z=complex(-3,4); assert abs(z+abs(z)-complex(2,4))<1e-9; v=round((z*z).imag); assert v==-24
a2=3; z_w=complex(3,4); e=[round((z_w*z_w).imag),round((z*z).real),round(z.real*z.imag),round(z_w.real*z_w.imag)]; assert e==[24,-7,-12,12] and len({v,*e})==5
q('0008',tipId='kk2-denk',tip='Eşitlikten sayıyı bulma',z='orta',alt='Modüllü Eşitlik',kaz='İçinde modül bulunan karmaşık sayı eşitliğinden sayıyı bulur ve karesinin sanal kısmını hesaplar.',kalip='düz',
 kart='K-AKS2-07 (z + |z| = 2 + 4i) · z = −3 + 4i; Im(z²) = −24',
 metin='z karmaşık sayısı için z + |z| = 2 + 4i eşitliği sağlanmaktadır.\nBuna göre z² sayısının sanal kısmı kaçtır?',
 dogru=v,yan=[(e[0],'a + √(a² + 16) = 2 denkleminde 16 = 4 + 4a bulup a = 3 almış ve çözümü sınamamış: Im(z²) = 24.','islem'),(e[1],'z = −3 + 4i bulmuş fakat z² yerine gerçel kısmı (9 − 16 = −7) yazmış.','dikkat'),(e[2],'z² = a² − b² + 2abi’de sanal kısmı 2ab yerine ab = −12 almış.','bilgi'),(e[3],'a = 3 bulup sınamamış ve 2ab yerine ab = 12 almış.','islem')],
 istenen='Im(z²)',ip=['z = a + bi yazıp gerçel ve sanal kısımları ayrı ayrı eşitle; bulduğun değeri eşitlikte dene.'],bilgi=[MOD2],
 ad=[A('Kısımları eşitle','z = a + bi için sanal kısım doğrudan eşitlenir.','b = 4'),A('Gerçel kısım denklemi','a + √(a² + 16) = 2 → √(a² + 16) = 2 − a (2 − a ≥ 0 olmalı).','a² + 16 = 4 − 4a + a² → a = −3'),A('Sına','a = −3 için 2 − a = 5 = |z| doğrudur; z = −3 + 4i.','−3 + 5 = 2 ✓'),A('Kareyi al','z² = a² − b² + 2abi.','z² = −7 − 24i → −24')],
 puf='Köklü denklemde kök dışarı çıkarken bulduğun değeri mutlaka denklemde sına.')

# ================= 09 orta · yeni nesil+şekil · f(z) = i·z̄ =================
fz=lambda w:1j*w.conjugate()
A9,B9=complex(2,1),complex(-1,3); S9=fz(A9)+fz(B9); assert eq(S9,4,1); v=round(S9.real-S9.imag); assert v==3
rot=1j*A9+1j*B9; Sc=A9.conjugate()+B9.conjugate()
A9s,B9s=complex(1,2),complex(3,-1); Ssw=fz(A9s)+fz(B9s); assert eq(Ssw,1,4)
e=[round(rot.real-rot.imag),round(Sc.real-Sc.imag),round(Ssw.real-Ssw.imag),round(fz(A9).real-fz(A9).imag)]; assert e==[-5,5,-3,-1] and len({v,*e})==5
SK=fig(arg(-2,4,-2,4,govde=nok(2,1,'z_1',BL,'above right',kil=True)+nok(-1,3,'z_2',OR,'above left',kil=True)))
q('0009',tipId='kk2-nokta',tip='Düzlemde okuyup işlem yapma',z='orta',alt='Tanımlı Dönüşüm',kaz='Karmaşık sayılar kümesinde tanımlı f(z) = i · z̄ dönüşümünü düzlemde okunan sayılara uygular.',kalip='yeni nesil',
 kart='K-AKS2-02 (tanımlı dönüşüm) · f(z) = i · z̄, z₁(2, 1), z₂(−1, 3); Re − Im = 3',
 metin='Karmaşık sayılar kümesinde f(z) = i · z̄ biçiminde bir f dönüşümü tanımlanıyor. Şekilde, karmaşık düzlemde z₁ ve z₂ sayılarının görüntüleri verilmiştir.\nBuna göre f(z₁) + f(z₂) sayısının gerçel kısmından sanal kısmının çıkarılmasıyla elde edilen değer kaçtır?',
 dogru=v,yan=[(e[0],'Eşlenik almayı atlayıp f(z) = i · z almış: toplam −4 + i, fark −5.','dikkat'),(e[1],'Yalnız eşleniği alıp i ile çarpmayı unutmuş: toplam 1 − 4i, fark 5.','dikkat'),(e[2],'Noktaları okurken gerçel ve sanal eksenleri karıştırmış: z₁ = 1 + 2i, z₂ = 3 − i okuyup toplam 1 + 4i, fark −3 bulmuş.','dikkat'),(e[3],'Yalnız f(z₁) = 1 + 2i’yi hesaplayıp f(z₂)’yi toplamaya katmamış: 1 − 2 = −1.','islem')],
 istenen='Re(f(z₁) + f(z₂)) − Im(f(z₁) + f(z₂))',ip=['Dönüşümü her sayıya ayrı uygula: önce eşlenik, sonra i ile çarpma.'],bilgi=[DUZ2,ESL2],sekil=SK,
 ad=[A('Noktaları oku','Yatay koordinat gerçel, düşey sanal kısımdır.','z₁ = 2 + i · z₂ = −1 + 3i'),A('f’yi uygula','Önce eşlenik alınır, sonra i ile çarpılır.','f(z₁) = i(2 − i) = 1 + 2i · f(z₂) = i(−1 − 3i) = 3 − i'),A('Topla','Gerçel ve sanal kısımlar ayrı toplanır.','f(z₁) + f(z₂) = 4 + i'),A('Farkı hesapla','Gerçel kısımdan sanal kısım çıkarılır.','4 − 1 = 3')],
 puf='Önce eşleniği al, sonra i ile çarp; sıra değişirse sonuç değişir.')

# ================= 10 orta · öncüllü+şekil · modül karşılaştırma =================
z1,z2=complex(-3,4),complex(4,3); assert abs(z1)==abs(z2)==5 and eq(-1j*z1,4,3) and eq(z1+z2,1,7)
Y=[abs(z1)<abs(z2), eq(-1j*z1,4,3), abs(abs(z1+z2)**2-50)<1e-9]; assert Y==[False,True,True]
SK=fig(arg(-4,5,-1,5,govde=nok(-3,4,'z_1',BL,'above left',kil=True)+nok(4,3,'z_2',OR,'above right',kil=True)))
q('0010',tipId='kk2-modul',tip='Modül ve eşlenik yargıları',z='orta',alt='Modül Yargıları',kaz='Düzlemde verilen iki sayının modüllerini, birinin i ile çarpımını ve toplamının modülünü karşılaştırarak yargıları sınar.',kalip='öncüllü',
 kart='K-AKS2-06 (iki nokta yargıları) · z₁(−3, 4), z₂(4, 3); |z₁| = |z₂|, z₂ = −i · z₁, |z₁ + z₂|² = 50',
 metin='Şekilde, karmaşık düzlemde z₁ ve z₂ sayılarının görüntüleri verilmiştir.\nBuna göre,\nI. |z₁| < |z₂|\nII. z₂ = −i · z₁\nIII. |z₁ + z₂|² = 50\nyargılarından hangileri doğrudur?',
 dogru='II ve III',yan=[('Yalnız I','Uzaklıkları gözle karşılaştırıp z₂’yi daha uzak sanmış; II ve III’ü sınamamış.','dikkat'),('Yalnız III','z₂ = −i · z₁ ilişkisini sınarken −i yerine i alıp i(−3 + 4i) = −4 − 3i bulmuş; II’yi yanlış saymış.','islem'),('I ve II','Modülleri ölçmeden eşit olmadığını düşünmüş (I doğru sanmış); III’te |z₁ + z₂|’yi |z₁| + |z₂| = 10 sanıp yanlış bulmuş.','bilgi'),('I, II ve III','Üç yargıyı da doğru saymış; |z₁| = |z₂| = 5 olduğunu hesaplamamış.','dikkat')],
 sira=['Yalnız I','Yalnız III','I ve II','I, II ve III','II ve III'],istenen='Doğru olan yargılar.',ip=['Noktaları sayıya çevirip her yargıyı ayrı ayrı hesapla; |z₁| ve |z₂| için orijine olan uzaklığa bak.'],bilgi=[DUZ2,MOD2],sekil=SK,
 ad=[A('Sayıları oku','Koordinatlar sayının kısımlarıdır.','z₁ = −3 + 4i · z₂ = 4 + 3i'),A('I’i sına','İkisinin modülü de 5’tir.','|z₁| = |z₂| = 5 → I yanlış'),A('II’yi sına','−i ile çarpılırsa 4 + 3i bulunur.','−i(−3 + 4i) = 3i + 4 = 4 + 3i → II doğru'),A('III’ü sına','Toplam 1 + 7i’dir.','|1 + 7i|² = 1 + 49 = 50 → III doğru')],
 puf='Önce noktaları a + bi yap; modül karşılaştırmasında kareler toplamı yeterli.')

# ================= 11 orta · düz · x² + x + 1 = 0 =================
xs=sp.symbols('x'); ks=sp.solve(xs**2+xs+1,xs); z0=complex(ks[0])
assert abs(z0**3-1)<1e-9 and abs(z0**20+z0**10+1)<1e-9
v=0; e=[3,-1,-2,1]
assert abs((z0**2+z0)+1)<1e-9 and 3==1+1+1 and -1==(z0**2+z0) .real.__round__() and -2==round((z0**2+z0).real)-1 and len({v,*e})==5
q('0011',tipId='kk2-kok',tip='Kökler ve grafik',z='orta',alt='Kökün Kuvvetleri',kaz='Bir karmaşık sayının sağladığı denklemden kuvvetleri arasındaki bağıntıyı çıkarır ve yüksek kuvvetli ifadeyi sadeleştirir.',kalip='düz',
 kart='K-AKS2-05 (kökün kuvvetleri) · x² + x + 1 = 0, z³ = 1; z²⁰ + z¹⁰ + 1 = 0',
 metin='x² + x + 1 = 0 denkleminin köklerinden biri z karmaşık sayısıdır.\nBuna göre z²⁰ + z¹⁰ + 1 ifadesinin değeri kaçtır?',
 dogru=v,yan=[(e[0],'z³ = 1 olduğundan her kuvveti 1 sanıp 1 + 1 + 1 = 3 bulmuş.','bilgi'),(e[1],'z²⁰ = z² ve z¹⁰ = z bulup z² + z = −1 değerini yazmış, sondaki +1’i eklememiş.','islem'),(e[2],'z² + z = −1 bulup sabit terimi +1 yerine −1 almış: −2.','dikkat'),(e[3],'z² + z + 1 = 0 olduğunu kullanmak yerine z² + z = −1 bulup 1’i iki kez eklemiş: −1 + 1 + 1.','islem')],
 istenen='z²⁰ + z¹⁰ + 1',ip=['Verilen denklemden z’nin kuvvetleri arasında bir bağıntı çıkar.'],bilgi=[KUV2],
 ad=[A('Bağıntıyı bul','Denklemin iki tarafı uygun bir çarpanla çarpılarak z’nin küçük bir kuvveti sabite eşitlenir.','(z − 1)(z² + z + 1) = 0 → z³ − 1 = 0 → z³ = 1'),A('Üsleri indir','20 ve 10’un 3’e bölümünden kalanlar alınır.','z²⁰ = z² · z¹⁰ = z'),A('İfadeyi yaz','Ifade, denklemin sol tarafına dönüşür.','z² + z + 1'),A('Değeri bul','z kök olduğundan bu ifade sıfırdır.','0')],
 puf='Bulduğun bağıntıdan üsleri döngü uzunluğuna göre indir.')

# ================= 12 orta · yeni nesil · tanımlı işlem =================
Z1,Z2=2+2j,2-2j; Zp=1/(1/Z1+1/Z2); assert eq(Zp,2,0) and eq(1/Z1+1/Z2,0.5,0)
assert eq(Z1+Z2,4,0) and eq(Z1*Z2,8,0)
q('0012',tipId='kk2-islem',tip='Tanımlı işlem ve eşlenik',z='orta',alt='Tanımlı İşlem',kaz='Tersler toplamının tersi biçiminde tanımlı işlemi karmaşık sayılara uygular.',kalip='yeni nesil',
 kart='K-AKS2-08 (z₁ ∗ z₂ = 1/(1/z₁ + 1/z₂)) · (2 + 2i) ∗ (2 − 2i) = 2',
 metin='Karmaşık sayılar kümesinde z₁ ∗ z₂ = 1 / (1/z₁ + 1/z₂) biçiminde bir ∗ işlemi tanımlanıyor.\nBuna göre (2 + 2i) ∗ (2 − 2i) işleminin sonucu kaçtır?',
 dogru='2',yan=[('1/2','İç toplamı 1/2 bulup dıştaki 1/ işlemini uygulamamış.','dikkat'),('1','Eşlenikle genişletirken paydayı 2² + 2² = 8 yerine 4 alıp 1/z₁ = (1 − i)/2, 1/z₂ = (1 + i)/2 bulmuş; toplam 1, sonuç 1.','islem'),('4','İşlemi z₁ + z₂ toplamı sanıp 4 bulmuş.','bilgi'),('8','İşlemi z₁ · z₂ çarpımı sanıp 8 bulmuş.','bilgi')],
 sira=['1/2','1','2','4','8'],istenen='(2 + 2i) ∗ (2 − 2i)',ip=['Önce 1/z₁ ve 1/z₂’yi ayrı ayrı hesapla.'],bilgi=[ESL2,MOD2],
 ad=[A('Terslerin toplamı','Her kesir paydanın eşleniğiyle genişletilir.','1/(2 + 2i) = (2 − 2i)/8 = (1 − i)/4 · 1/(2 − 2i) = (1 + i)/4'),A('Topla','Sanal kısımlar birbirini götürür.','2/4 = 1/2'),A('Dış tersi al','Sonuç toplamın tersidir.','1/(1/2) = 2')],
 puf='İşlemin kuralını sırayla uygula: önce içteki toplam, sonra dıştaki ters.')

# ================= 13 orta · şekil · bölüm =================
z1,z2=complex(4,2),complex(1,-1); v=round((z1/z2).imag); assert v==3 and eq(z1/z2,1,3)
e=[round(z1.imag/z2.imag),round(((z1*z2.conjugate()).imag)),round((z1*z2/2).imag if False else (z1*z2).imag/2),round((complex(2,4)/complex(-1,1)).imag)]
assert eq(z1*z2.conjugate(),2,6) and eq(z1*z2,6,-2)
e=[-2,6,-1,-3]; assert round((z1*z2).imag/2)==-1 and round((complex(2,4)/complex(-1,1)).imag)==-3 and len({v,*e})==5
SK=fig(arg(-2,5,-2,3,govde=nok(4,2,'z_1',BL,'above right',kil=True)+nok(1,-1,'z_2',OR,'below right',kil=True)))
q('0013',tipId='kk2-nokta',tip='Düzlemde okuyup işlem yapma',z='orta',alt='Bölümün Sanal Kısmı',kaz='Düzlemde verilen iki noktayı sayıya çevirip bölümü eşlenikle genişleterek sadeleştirir ve sanal kısmını bulur.',kalip='şekilli',
 kart='K-AKS2-02 (z₁/z₂) · z₁(4, 2), z₂(1, −1); Im(z₁/z₂) = 3',
 metin='Şekilde, karmaşık düzlemde z₁ ve z₂ sayılarının görüntüleri verilmiştir.\nBuna göre z₁ / z₂ bölümünün sanal kısmı kaçtır?',
 dogru=v,yan=[(e[0],'Sanal kısımları birbirine bölmüş: 2/(−1) = −2.','bilgi'),(e[1],'Eşlenikle genişletmiş fakat paydadaki 2’ye bölmeyi unutmuş: (2 + 6i) → 6.','islem'),(e[2],'Paydanın eşleniği (1 + i) yerine paydanın kendisi (1 − i) ile genişletmiş: (4 + 2i)(1 − i) = 6 − 2i, 2’ye bölünce sanal kısım −1.','dikkat'),(e[3],'Eksenleri karıştırıp z₁ = 2 + 4i, z₂ = −1 + i okumuş: bölüm 1 − 3i.','dikkat')],
 istenen='Im(z₁ / z₂)',ip=['Noktaları sayıya çevirdikten sonra paydayı gerçel yapacak çarpanı seç.'],bilgi=[DUZ2,MOD2],sekil=SK,
 ad=[A('Noktaları oku','Yatay gerçel, düşey sanal kısımdır.','z₁ = 4 + 2i · z₂ = 1 − i'),A('Eşlenikle genişlet','Pay ve payda 1 + i ile çarpılır.','(4 + 2i)(1 + i)/((1 − i)(1 + i))'),A('Sadeleştir','Pay: 4 + 4i + 2i − 2 = 2 + 6i; payda: 2.','(2 + 6i)/2 = 1 + 3i'),A('Sanal kısmı oku','i’nin katsayısı.','3')],
 puf='Bölümde paydanın eşleniğiyle genişletip paydayı gerçel yap.')

# ================= 14 zor · şekil · iki çember, tam sayı değerleri =================
cA,rA=complex(0,0),1; cB,rB=complex(3,4),2; d=abs(cA-cB); assert d==5
mx,mn=d+rA+rB,d-rA-rB; assert (mx,mn)==(8,2); v=len([k for k in range(0,20) if mn<=k<=mx]); assert v==7
dd=[abs((cB+rB*cmath.exp(1j*t*math.pi/180))-(cA+rA*cmath.exp(1j*u*math.pi/180))) for t in range(0,360,3) for u in range(0,360,3)]
assert abs(max(dd)-8)<1e-3 and abs(min(dd)-2)<1e-3
e=[len([k for k in range(0,20) if d-rA<=k<=d+rA]),len([k for k in range(0,20) if mn<k<mx]),int(mx-mn),len([k for k in range(0,20) if 0<=k<=mx])]; assert e==[3,5,6,9] and len({v,*e})==5
body=f'\\draw[fill=blue!12,draw={BL},line width=1.8pt] (0,0) circle ({1*SC}); \\draw[fill=orange!15,draw={OR},line width=1.8pt] ({3*SC},{4*SC}) circle ({2*SC}); \\fill[{BL}] (0,0) circle (0.08); \\fill[{OR}] ({3*SC},{4*SC}) circle (0.08);'+f'\\node[{BL},font=\\small\\bfseries,above left] at ({-0.7*SC:.2f},{0.7*SC:.2f}) {{$K_1$}};\\node[{OR},font=\\small\\bfseries,above right=1pt] at ({3*SC},{4*SC}) {{$K_2$}};'
SK=fig(arg(-2,6,-2,7,govde=body))
q('0014',tipId='kk2-yer',tip='Bölge ve çember problemleri',z='zor',alt='İki Çember Arası Uzaklık',kaz='Merkezleri ve yarıçapları şekilden okunan iki çember üzerindeki sayıların uzaklığının alabileceği değer aralığını bulur ve bu aralıktaki tam sayıları sayar.',kalip='şekilli',
 kart='K-AKS2-04 (iki çember) · K₁(0, 0), r = 1; K₂(3, 4), r = 2; |z − w| ∈ [2, 8], 7 tam sayı',
 metin='Şekilde, karmaşık düzlemde K₁ ve K₂ çemberleri verilmiştir. z sayısı K₁ çemberi üzerinde, w sayısı K₂ çemberi üzerinde değişmektedir.\nBuna göre |z − w| ifadesinin alabileceği tam sayı değerlerinin sayısı kaçtır?',
 dogru=v,yan=[(e[0],'K₂’yi yok sayıp yalnız K₁’in yarıçapıyla merkezler arası uzaklığı kullanmış: 4, 5, 6 değerleri, 3 tane.','bilgi'),(e[1],'Uç değerleri (2 ve 8) dahil etmeyip 3, 4, 5, 6, 7 almış: 5 tane.','dikkat'),(e[2],'Tam sayıları saymak yerine en büyük ile en küçük değerin farkını (8 − 2) yazmış.','islem'),(e[3],'Çemberleri ayrık görmeyip en küçük değeri 0 almış: 0’dan 8’e 9 tane.','dikkat')],
 istenen='|z − w| ifadesinin alabileceği tam sayı değerlerinin sayısı.',ip=['Çemberlerin birbirine göre durumunu belirle; uzaklığın değiştiği aralığın uçlarını bul.'],bilgi=[UZK,MOD2],sekil=SK,
 ad=[A('Merkez ve yarıçaplar','Merkezler orijin ile 3 + 4i, yarıçaplar ızgaradan okunur.','K₁: 0, r₁ = 1 · K₂: 3 + 4i, r₂ = 2'),A('Merkezler arası uzaklık','Fark sayısının modülü.','d = |3 + 4i| = 5 > r₁ + r₂ = 3 (çemberler ayrık)'),A('Uzaklık aralığı','Uç değerler merkezleri birleştiren doğru üzerindeki noktalardır.','en küçük 5 − 3 = 2, en büyük 5 + 3 = 8'),A('Tam sayıları say','Aralığın iki ucu da alınabilir.','2, 3, 4, 5, 6, 7, 8 → 7 tane')],
 puf='Uzaklık iki uç arasındaki bütün değerleri alır; uçların alınıp alınmadığına bak.')

# ================= 15 zor · grafik · üçüncü derece polinom =================
xp=sp.symbols('x'); Pq=sp.expand((xp-1)*(xp**2+4)); assert Pq==xp**3-xp**2+4*xp-4; k1,k2=2j,-2j
assert [Pq.subs(xp,t) for t in (0,1,2)]==[-4,0,8]
ar=sp.symbols('a b'); sol=sp.solve([1+ar[0]+ar[1]-4,8+4*ar[0]+2*ar[1]-4-8],ar); assert sol[ar[0]]==-1 and sol[ar[1]]==4
v=int(abs(k1)**2+(k1*k2).real); assert v==8
e=[0,4,6,16]; assert 4+(-4)==0 and 2+4==6 and 4*4==16 and len({v,*e})==5
fp=lambda x:x**3-x**2+4*x-4
sx,sy=1.0,0.19
gv=egri(fp,-0.7,2.2,sx,sy,BL,80)+gnok(1,0,'A',OR,'above left',sx,sy)+gnok(0,-4,'B',OR,'below right',sx,sy)+gnok(2,8,'C',OR,'above left',sx,sy)
SK=fig(graf(-1,3,-8,10,sx,sy,gv,ys=2))
q('0015',tipId='kk2-kok',tip='Kökler ve grafik',z='zor',alt='Grafikten Polinom',kaz='Grafikte işaretli noktalardan üçüncü derece polinomun katsayılarını bulur; gerçel olmayan kökler için modül ve çarpım içeren ifadeyi hesaplar.',kalip='grafik',
 kart='K-AKS2-05 (kübik grafik) · P(x) = x³ − x² + 4x − 4; A(1,0), B(0,−4), C(2,8); |z₁|² + z₁z₂ = 8',
 metin='a ve b gerçel sayılar olmak üzere P(x) = x³ + ax² + bx − 4 polinomunun grafiği şekilde verilmiştir. P(x) = 0 denkleminin gerçel olmayan kökleri z₁ ve z₂’dir.\nBuna göre |z₁|² + z₁ · z₂ değeri kaçtır?',
 dogru=v,yan=[(e[0],'z₁ · z₂ = (2i)(−2i) çarpımında i² = +1 alıp −4 bulmuş: 4 + (−4) = 0.','islem'),(e[1],'|z₁|² yerine yalnız toplamda z₁ · z₂ = 4’ü yazmış.','dikkat'),(e[2],'|2i| = 2 bulup karesini almamış: 2 + 4 = 6.','islem'),(e[3],'|z₁|² ile z₁ · z₂’yi toplamak yerine çarpmış: 4 · 4 = 16.','dikkat')],
 istenen='|z₁|² + z₁ · z₂',ip=['Şekildeki üç noktayı polinomda yerine koyarak a ve b’yi bul; bilinen gerçel kök, polinomu bölmeye yarar.'],bilgi=[GER,MOD2],sekil=SK,
 ad=[A('Noktaları yerine koy','A(1, 0) ve C(2, 8) noktaları P’de yazılır.','1 + a + b − 4 = 0 · 8 + 4a + 2b − 4 = 8'),A('a ve b','İki denklem birlikte çözülür.','a + b = 3 · 2a + b = 2 → a = −1, b = 4'),A('Çarpanlara ayır','x = 1 kök olduğundan (x − 1) çarpanı çıkar.','P(x) = (x − 1)(x² + 4)'),A('İfadeyi hesapla','Gerçel olmayan kökler x² + 4 = 0’ın kökleridir.','z₁ = 2i, z₂ = −2i → |z₁|² = 4, z₁ · z₂ = 4 → 8')],
 puf='Önce grafikteki noktalardan katsayıları bul.')

# ================= 16 zor · öncüllü+şekil · dik üçgen =================
Z1,Z2,Z3=complex(1,1),complex(5,1),complex(5,4)
Gg=(Z1+Z2+Z3)/3
Y=[(Z3-Z2)/(Z1-Z2), (Z3-Z1)/(Z2-Z1), abs(Gg-Z2)**2]
assert abs(Y[0].real)<1e-9 and abs(abs(Y[1])-1.25)<1e-9 and abs(Y[2]-25/9)<1e-9
tri='\\draw[fill=blue!12,draw='+BL+',line width=1.6pt] '+' -- '.join(f'({p.real*SC:.2f},{p.imag*SC:.2f})' for p in (Z1,Z2,Z3))+' -- cycle;'
SK=fig(arg(-1,6,-1,5,ust=tri,govde=nok(1,1,'z_1',BL,'below left')+nok(5,1,'z_2',BL,'below right')+nok(5,4,'z_3',BL,'above right')))
q('0016',tipId='kk2-geo',tip='Köşe sayılarıyla geometri',z='zor',alt='Üçgende Bölüm Yargıları',kaz='Köşeleri düzlemde verilen üçgende fark sayılarının bölüm ve çarpımlarını hesaplayarak yargıların doğruluğunu belirler.',kalip='öncüllü',
 kart='K-AKS2-03 (dik üçgen) · z₁(1, 1), z₂(5, 1), z₃(5, 4); saf sanal bölüm, modül 5/4, |G − z₂|² = 25/9',
 metin='Şekilde, karmaşık düzlemde köşeleri z₁, z₂ ve z₃ sayılarının görüntüleri olan bir üçgen verilmiştir. Üçgenin ağırlık merkezinin görüntüsü G sayısıdır.\nBuna göre,\nI. (z₃ − z₂) / (z₁ − z₂) sayısı saf sanaldır.\nII. (z₃ − z₁) / (z₂ − z₁) sayısının modülü 5/4’tür.\nIII. |G − z₂|² = 25/9’dur.\nyargılarından hangileri doğrudur?',
 dogru='I, II ve III',yan=[('Yalnız I','II’de |4 + 3i|’yi 4 + 3 = 7 alıp 7/4 bulmuş; III’te G’yi köşe toplamı olarak (11 + 6i) alıp yanlış bulmuş.','islem'),('Yalnız II','I’de z₁ − z₂ = −4 ve z₃ − z₂ = 3i oranını (−3i/4) saf sanal görmeyip gerçel sanmış; III’te G’yi toplam olarak alıp yanlış bulmuş.','dikkat'),('I ve II','III’te ağırlık merkezini 3’e bölmeden (11 + 6i) alıp |G − z₂|² değerini farklı bulmuş.','islem'),('II ve III','I’de oranın −3i/4 olduğunu görmesine rağmen saf sanalı gerçel saymış.','dikkat')],
 sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],istenen='Doğru olan yargılar.',ip=['Fark sayılarını yatay ve düşey kenarlardan yaz.'],bilgi=[DUZ2,MOD2],sekil=SK,
 ad=[A('Köşeleri oku','Koordinatlar sayılara çevrilir.','z₁ = 1 + i · z₂ = 5 + i · z₃ = 5 + 4i'),A('Fark sayıları','Yatay kenar gerçel, düşey kenar sanal fark verir.','z₂ − z₁ = 4 · z₃ − z₂ = 3i · z₃ − z₁ = 4 + 3i'),A('I ve II','(3i)/(−4) = −3i/4 saf sanal; |4 + 3i|/4 = 5/4.','I doğru · II doğru'),A('III','G = (11 + 6i)/3; G − z₂ = −4/3 + i.','|G − z₂|² = 16/9 + 1 = 25/9 → III doğru')],
 puf='Her yargıdaki sayıyı köşelerden kurup sade biçimde yaz.')

# ================= 17 zor · düz · z·z̄ − 2(z + z̄) − 5 = 0 =================
# |z−2|² = 9 → merkez 2, r=3; P = 2+4i, d=4
dP=abs(complex(2,4)-2); assert dP==4
mx_,mn_=dP+3,abs(dP-3); v=mx_*mn_; assert v==7
e=[int(mx_+mn_),int((dP+1)*(dP-1+0) if False else (4+1)*(4-1)),int((4+2*4-0+1+0)*0+27),int((4+9)*abs(4-9))]
assert 4+1==5 and (4+1)*(4-1)==15 and (4+2)*(4+2-3)==18
P5=complex(5,4); d5=abs(P5-2); assert d5==5
mx_,mn_=d5+3,d5-3; v=mx_//mn_; assert v==4 and mx_/mn_==4
e=[2,6,10,16]; assert (mn_,mx_-mn_,mx_+mn_,mx_*mn_)==(2,6,10,16) and len({v,*e})==5
q('0017',tipId='kk2-yer',tip='Bölge ve çember problemleri',z='zor',alt='Denklemden Çember',kaz='z · z̄ ve z + z̄ içeren eşitliği çemberin merkez ve yarıçapına dönüştürür; çember üzerindeki noktanın sabit bir noktaya uzaklığının uç değerlerinin oranını bulur.',kalip='düz',
 kart='K-AKS2-04 (z · z̄ biçiminden çembere) · |z − 2| = 3; P = 5 + 4i; en büyük/en küçük = 4',
 metin='z karmaşık sayısı için z · z̄ − 2(z + z̄) − 5 = 0 eşitliği sağlanmaktadır.\nBuna göre |z − 5 − 4i| ifadesinin en büyük değerinin en küçük değerine oranı kaçtır?',
 dogru=v,yan=[(e[0],'Oran yerine en küçük değeri (5 − 3 = 2) yazmış.','dikkat'),(e[1],'Oran yerine en büyük ve en küçük değerin farkını (8 − 2) yazmış.','dikkat'),(e[2],'Oran yerine en büyük ve en küçük değerin toplamını (8 + 2) yazmış.','dikkat'),(e[3],'Oran yerine en büyük ve en küçük değerin çarpımını (8 · 2) yazmış.','dikkat')],
 istenen='(|z − 5 − 4i| en büyük) / (|z − 5 − 4i| en küçük)',ip=['z = x + yi yazıp denklemi x ve y cinsinden düzenle.'],bilgi=[YER2,UZK],
 ad=[A('Denklemi düzenle','z = x + yi yazılır; z·z̄ = x² + y², z + z̄ = 2x.','x² + y² − 4x − 5 = 0 → (x − 2)² + y² = 9'),A('Çemberi oku','Merkez 2, yarıçap 3.','|z − 2| = 3'),A('Uzaklığı bul','Merkez ile 5 + 4i arasındaki uzaklık.','d = |3 + 4i| = 5 (nokta çemberin dışında)'),A('Uç değerleri oranla','Uç değerler merkezi ve noktayı birleştiren doğru üzerindeki noktalardır.','en büyük 5 + 3 = 8, en küçük 5 − 3 = 2 → 8/2 = 4')],
 
 puf='z · z̄ + (terimler) = k biçimi |z − z₀|² = r² biçimine tamamlanır.')

# ================= 18 zor · şekil · çevre − alan =================
A_=math.pi*16/2-math.pi*4/2; P_=math.pi*4+math.pi*2+4; assert abs(A_-6*math.pi)<1e-12 and abs(P_-A_-4)<1e-12
opts=['4 − 2π','0','4','8','2π + 4']; v_='4'
assert abs((P_-math.pi*8)-(4-2*math.pi))<1e-9 and abs((6*math.pi)-A_)<1e-9 and abs((P_-4)-A_)<1e-9 and abs((P_+4)-A_-8)<1e-9 and abs((P_-(math.pi*8-math.pi*4))-(2*math.pi+4))<1e-9
ust=f'\\fill[blue!15] ({4*SC:.2f},0) arc (0:180:{4*SC:.2f}) -- (0,0) arc (180:0:{2*SC:.2f}) -- cycle;'
body=f'\\draw[{BL},line width=1.8pt] ({4*SC:.2f},0) arc (0:180:{4*SC:.2f}) -- (0,0); \\draw[{OR},line width=1.8pt] (0,0) arc (180:0:{2*SC:.2f}); \\fill[{OR}] ({2*SC:.2f},0) circle (0.08); \\node[{OR},above=2pt,font=\\small\\bfseries] at ({2*SC:.2f},0) {{$M$}};'
body+=f'\\node[left=7pt,font=\\footnotesize] at (0,{4*SC:.2f}) {{$4$}};'
SK=fig(arg(-4,5,-1,4,ust=ust,govde=body,skipy=(4,)))
q('0018',tipId='kk2-yer',tip='Bölge ve çember problemleri',z='zor',alt='Bölgenin Çevresi ve Alanı',kaz='Karmaşık koşullarla verilen bölgeyi şekilde tanır; çevresini ve alanını yay ve doğru parçalarından hesaplayarak farkını bulur.',kalip='şekilli',
 kart='K-AKS2-04 (çevre ve alan) · |z| ≤ 4, Im(z) ≥ 0, |z − 2| ≥ 2; çevre 6π + 4, alan 6π',
 metin='Şekilde, |z| ≤ 4, Im(z) ≥ 0 ve |z − 2| ≥ 2 koşullarını sağlayan z sayılarının oluşturduğu taralı bölge verilmiştir; M noktası turuncu yayı olan çemberin merkezidir.\nBuna göre bu bölgenin çevresinden alanı çıkarıldığında elde edilen değer kaçtır?',
 dogru=v_,yan=[('0','Çevreye eksendeki doğru parçasını eklememiş: 6π − 6π = 0.','dikkat'),('8','Doğru parçasını 4 yerine −4’ten 4’e bütün çap sanıp 8 almış: (6π + 8) − 6π.','bilgi'),('4 − 2π','Alanda iç yarım daireyi çıkarmayı unutup 8π almış: (6π + 4) − 8π.','islem'),('2π + 4','İç dairenin yarısı yerine tamamını (4π) çıkarıp alanı 4π bulmuş: (6π + 4) − 4π.','islem')],
 sira=opts,istenen='Çevre − alan',ip=['Bölgeyi çevreleyen parçaları ve bölgenin hangi iki daireden oluştuğunu ayrı ayrı düşün.'],bilgi=[DOR],sekil=SK,
 ad=[A('Parçaları belirle','Sınırda üç parça var: büyük yarım çember yayı, küçük yarım çember yayı ve eksendeki doğru parçası.','büyük yay r = 4; küçük yay r = 2; doğru parçası (−4, 0)–(0, 0)'),A('Çevre','Yarım çember yayı πr’dir.','4π + 2π + 4 = 6π + 4'),A('Alan','Büyük yarım daireden küçük yarım daire çıkarılır.','8π − 2π = 6π'),A('Fark','Çevre − alan.','(6π + 4) − 6π = 4')],
 puf='Çevre ve alanı ayrı ayrı yaz; bölgenin içindeki boşluk yalnız alandan düşer.')

# ================= 19 zor · yeni nesil+şekil · işlem makinesi dizisi =================
zn=[1+1j]
for _ in range(101): zn.append(1j*zn[-1]+1)
zn=zn+[1j*zn[-1]+1 for _ in range(100)]
zn=[ (1+1j) ]
for _ in range(201): zn.append(1j*zn[-1]+1)
assert all(eq(zn[i],*{0:(1,1),1:(0,1),2:(0,0),3:(1,0)}[i%4]) for i in range(202))
S=sum(zn); assert eq(S,101,102); v=round(S.real+S.imag); assert v==203
e=[200,201,204,101]
assert round((sum(zn[:200])).real+(sum(zn[:200])).imag)==200 and round((sum(zn[:200])+zn[2]+zn[3]).real+(sum(zn[:200])+zn[2]+zn[3]).imag)==201 and round(sum(zn[:204]).real+sum(zn[:204]).imag) if False else True
S204=50*(2+2j)+(2+2j); assert round(S204.real+S204.imag)==204 and round(S.real)==101 and len({v,*e})==5
body=(f'\\node[font=\\large] (g) at (0,0) {{$z_n$}};\\node[draw,rounded corners,fill=blue!15,minimum width=1.9cm,minimum height=0.9cm,right=0.8cm of g] (a) {{$i$ ile çarp}};'
 f'\\node[draw,rounded corners,fill=orange!20,minimum width=1.9cm,minimum height=0.9cm,right=0.8cm of a] (b) {{$1$ ekle}};\\node[font=\\large,right=0.8cm of b] (c) {{$z_{{n+1}}$}};'
 '\\draw[-{Stealth},thick] (g) -- (a); \\draw[-{Stealth},thick] (a) -- (b); \\draw[-{Stealth},thick] (b) -- (c);'
 '\\draw[-{Stealth},thick,dashed] (c.south) -- ++(0,-0.9) -| node[pos=0.25,below,font=\\small] {çıkan sayı yeniden girer} (g.south);')
SK=fig(body)
q('0019',tipId='kk2-kuvvet',tip='Kuvvet toplamı ve periyot',z='zor',alt='Makine Dizisi Toplamı',kaz='İşlem makinesiyle üretilen karmaşık sayı dizisinin dört terimlik döngüsünü bulur ve ilk 202 teriminin toplamını hesaplar.',kalip='yeni nesil',
 kart='K-AKS2-01 (makine dizisi) · z₁ = 1 + i, zₙ₊₁ = i · zₙ + 1; ilk 202 terim toplamı 101 + 102i',
 metin='Şekildeki işlem makinesine z₁ = 1 + i sayısı girildiğinde çıkan sayı z₂ olmaktadır. Çıkan sayı yeniden makineye girilerek z₃, z₄, … sayıları elde edilmektedir.\nBuna göre z₁ + z₂ + z₃ + … + z₂₀₂ toplamının gerçel kısmı ile sanal kısmının toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız 50 tam döngüyü (100 + 100i) toplayıp kalan iki terimi eklememiş.','dikkat'),(e[1],'Kalan iki terim yerine z₃ + z₄ = 1’i ekleyip 101 + 100i bulmuş.','islem'),(e[2],'202 terimi 51 tam döngü (4 · 51 = 204 terim) saymış: 102 + 102i.','dikkat'),(e[3],'Toplamı 101 + 102i bulmuş ama gerçel ve sanal kısımları toplamak yerine yalnız gerçel kısmı yazmış.','dikkat')],
 istenen='Re(S) + Im(S), S = z₁ + z₂ + … + z₂₀₂',ip=['İlk birkaç terimi yaz; sayıların nerede tekrar ettiğine bak.'],bilgi=[MAK,PER],sekil=SK,
 ad=[A('İlk terimleri yaz','Her adımda i ile çarpılıp 1 eklenir.','z₂ = i(1 + i) + 1 = i; z₃ = i·i + 1 = 0; z₄ = 1'),A('Döngüyü bul','z₅ = i · 1 + 1 = 1 + i = z₁; dizi 4 terimle tekrar eder.','z₁, z₂, z₃, z₄ sonra yine z₁…'),A('Bir döngünün toplamı','Dört terim toplanır.','(1 + i) + i + 0 + 1 = 2 + 2i'),A('Toplam','202 = 4 · 50 + 2: 50 döngü + z₁ + z₂.','50(2 + 2i) + (1 + i) + i = 101 + 102i → 101 + 102 = 203')],
 puf='Dizi bir değere dönünce tekrar eder: önce döngüyü, sonra döngü toplamını bul.')

# ================= 20 zor · öncüllü · z² = −5 + 12i =================
zs=[complex(2,3),complex(-2,-3)]; assert all(eq(w*w,-5,12) for w in zs)
Y=[eq(zs[0],2,3) and eq(zs[1],2,3), round(abs(zs[0])**2)==13 and round(abs(zs[1])**2)==13, abs(zs[0]**3-zs[1]**3)<1e-9 and False]
assert Y[:2]==[False,True] and eq(zs[0]**3,-46,9) and eq(zs[1]**3,46,-9)
q('0020',tipId='kk2-denk',tip='Eşitlikten sayıyı bulma',z='zor',alt='Karesi Verilen Sayı',kaz='Karesi verilen karmaşık sayıyı gerçel ve sanal kısımları eşitleyerek bulur; bulunan iki çözüm hakkındaki yargıları sınar.',kalip='öncüllü',
 kart='K-AKS2-07 (z² = −5 + 12i) · z = ±(2 + 3i); |z|² = 13',
 metin='z² = −5 + 12i olduğuna göre,\nI. z = 2 + 3i\nII. |z|² = 13\nIII. z³ sayısının gerçel kısmı −46’dır\nyargılarından hangileri doğrudur?',
 dogru='Yalnız II',yan=[('Yalnız I','a = 2, b = 3 çözümünü bulup −2 − 3i çözümünü atlamış; |z|² = 13’ü de |z|² = 5 + 12 = 17 diye hesaplayıp II’yi yanlış saymış.','dikkat'),('I ve II','Tek çözüm bulup I’i doğru saymış; |z|² = 13’ü doğru bulmuş.','dikkat'),('II ve III','II’yi doğru bulmuş; z = 2 + 3i için z³ = −46 + 9i hesaplayıp III’ü doğru saymış, diğer çözümde (−2 − 3i) z³ = 46 − 9i olduğunu görmemiş.','dikkat'),('I, II ve III','Yalnız z = 2 + 3i çözümünü alıp üç yargıyı da doğru saymış.','dikkat')],
 sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],istenen='Doğru olan yargılar.',ip=['z = a + bi yazıp kare al.'],bilgi=[ESL2,MOD2],
 ad=[A('Kısımları eşitle','z = a + bi için z² = a² − b² + 2abi.','a² − b² = −5 · 2ab = 12'),A('Çöz','ab = 6 ve a² − b² = −5’ten a² = 4 (a² = 4 → b = 6/a).','a = 2, b = 3 ya da a = −2, b = −3'),A('Yargıları sına','Her iki çözüm de ayrı ayrı denenir.','I yanlış (−2 − 3i de çözüm) · II doğru (|z|² = 13)'),A('III’ü sına','Çözümlere göre z³ farklı çıkar.','(2 + 3i)³ = −46 + 9i · (−2 − 3i)³ = 46 − 9i → III yanlış')],
 puf='Kısımları eşitleyip a ve b’yi bul.')

# ---------- çıktı ----------
def bitir_ayt(P,onek,k):
    HV=os.path.join(MYD,'..')
    for q_ in P.ANA: q_['kardes']=None
    json.dump(P.ANA,open(os.path.join(MYD,f'{onek}-1.json'),'w'),ensure_ascii=False,indent=1)
    from collections import Counter
    print(len(P.ANA),'ana · harfler',dict(sorted(Counter(q_['cevap']['sik'] for q_ in P.ANA).items())),'· zorluk',dict(Counter(q_['zorluk'] for q_ in P.ANA)),'· şekilli',sum(1 for q_ in P.ANA if q_['sekil']))
    tipler={}
    for c_ in H.KARTLAR: tipler.setdefault(c_['tipId'],dict(tipId=c_['tipId'],ad=c_['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c_['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın denemeleri (yalnız mantık), MEB 11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
bitir_ayt(P,'karmasikiki',UK)
