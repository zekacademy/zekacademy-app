"""AYT Fizik · Manyetik Alan ve Manyetik Kuvvet · 20 soruluk paket (3 kolay / 11 orta / 6 zor). Kardeş yok, ipucu 1.
Yönler (sağ el kuralı) vektör hesabıyla, büyüklükler Fraction ile hesaplanıp assert edilir; şekil koordinatları aynı verilerden üretilir."""
import sys,os,json,math
from itertools import combinations
ADIR=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(ADIR,'..')
sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,HV)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from fractions import Fraction as Fr
H.KONU='Manyetik Alan ve Manyetik Kuvvet'
UK='afiz|Manyetik Alan ve Manyetik Kuvvet'
P=Parti('manyetik','Manyetik Alan ve Manyetik Kuvvet',UK,ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM 2018–2025 AYT Fizik (manyetik alan, tele ve yüklü parçacığa etkiyen manyetik kuvvet, sağ el kuralı; yalnız mantık) · 345 AYT Fizik · Bilgi Sarmal AYT Fizik denemeleri · MEB 11. sınıf'
g=10
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def dist(v,e): assert len({v,*[x[0] for x in e]})==len(e)+1,(v,e)
def sec(dogru,cands,hedef):
    r='ABCDE'.index(hedef); vs=[c[0] for c in cands]; assert dogru not in vs and len(set(vs))==len(vs),(dogru,vs)
    sm=sorted([c for c in cands if c[0]<dogru],key=lambda c:c[0]); lg=sorted([c for c in cands if c[0]>dogru],key=lambda c:c[0])
    assert len(sm)>=r and len(lg)>=4-r,(dogru,hedef,vs)
    return (sm[len(sm)-r:] if r else [])+lg[:4-r]
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=2mm]}'
def fig(body): return tikz_svg(HEAD+body+TAIL)
MAV='blue!70!black'; KIR='red!70!black'
def cik(x,y,r=.2,col='black'):
    return f'\\draw[thick,{col}] ({x:.3f},{y:.3f}) circle ({r}); \\fill[{col}] ({x:.3f},{y:.3f}) circle ({r*.3:.3f});'
def ici(x,y,r=.2,col='black'):
    d=r*.7071
    return (f'\\draw[thick,{col}] ({x:.3f},{y:.3f}) circle ({r}); \\draw[thick,{col}] ({x-d:.3f},{y-d:.3f}) -- ({x+d:.3f},{y+d:.3f}); '
            f'\\draw[thick,{col}] ({x-d:.3f},{y+d:.3f}) -- ({x+d:.3f},{y-d:.3f});')
def sym(kind,x,y,r=.2,col='black'): return cik(x,y,r,col) if kind=='out' else ici(x,y,r,col)
def legend(x,y):
    return (cik(x,y,.14)+f' \\node[right,font=\\small] at ({x+.22:.2f},{y}) {{sayfadan dışarı}}; '+
            ici(x+2.7,y,.14)+f' \\node[right,font=\\small] at ({x+2.92:.2f},{y}) {{sayfaya içeri}};')
def dseg(p,a,b):
    ax,ay=a; bx,by=b; px,py=p; dx,dy=bx-ax,by-ay; L=dx*dx+dy*dy
    t=0 if L==0 else max(0,min(1,((px-ax)*dx+(py-ay)*dy)/L)); return math.hypot(px-(ax+t*dx),py-(ay+t*dy))
def serbest(pts,segs,pts_ex=(),mind=.4):
    return [p for p in pts if all(dseg(p,a,b)>=mind for a,b in segs) and all(math.hypot(p[0]-e[0],p[1]-e[1])>=mind for e in pts_ex)]
def vk(x1,y1,x2,y2,col='black',w='thick'): return f'\\draw[{col},{w},{ARR}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'
# --- yön ve alan hesabı (vektörel; tek veri kaynağı) ---
def Btel(p,s,I,pt):
    """Sayfaya dik (s=+1 dışarı, −1 içeri) uzun telin pt noktasındaki alanı (μ0/2π çarpanı hariç) — sağ el kuralı: B ∝ s·I·(ẑ×r)/|r|²."""
    rx,ry=Fr(pt[0])-Fr(p[0]),Fr(pt[1])-Fr(p[1]); r2=rx*rx+ry*ry
    return (s*I*(-ry)/r2, s*I*rx/r2)
def kuvvet_xy(l,B,I=1):
    """F = I·(l × B) ; l ve B 3 boyutlu (x,y,z) tuple."""
    return tuple(I*c for c in (l[1]*B[2]-l[2]*B[1], l[2]*B[0]-l[0]*B[2], l[0]*B[1]-l[1]*B[0]))
def yon(v):
    x,y=v[0],v[1]
    if x==0 and y==0: return 'sıfır'
    h='sağa' if x>0 else 'sola' if x<0 else ''; d='yukarı' if y>0 else 'aşağı' if y<0 else ''
    return h or d if not (h and d) else h+'-'+d
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
KUME={'Yalnız I':'I','Yalnız II':'II','Yalnız III':'III','I ve II':'I II','I ve III':'I III','II ve III':'II III','I, II ve III':'I II III'}
def nm(T): return [k for k,v in KUME.items() if v.split()==list(T)][0]
def oncul(T,hedef):
    name=nm(T); p='ABCDE'.index(hedef)
    for c in combinations(range(7),5):
        o=[SIR[i] for i in c]
        if name in o and o.index(name)==p: return o
    raise AssertionError((T,hedef))
def oncq(no,hedef,premise,stm,onadim=(),**k):
    """stm: {'I':(metin,doğru_mu,gerekçe),...} — her öncülün doğruluğu ve gerekçesi TEK yerde; adımlar ve çeldirici açıklamaları buradan üretilir."""
    T=[x for x in ('I','II','III') if stm[x][1]]; dogru=nm(T); sira=oncul(T,hedef)
    yan=[]
    for o in sira:
        if o==dogru: continue
        S=KUME[o].split(); parts=[]
        for x in ('I','II','III'):
            if x in S and x not in T: parts.append(f'{x} yargısını doğru kabul etmiş; oysa bu yargı yanlıştır, çünkü {stm[x][2]}.')
            if x in T and x not in S: parts.append(f'{x} yargısını yanlış kabul etmiş; oysa bu yargı doğrudur, çünkü {stm[x][2]}.')
        assert parts; yan.append((o,' '.join(parts),'bilgi'))
    ad=list(onadim)+[A(f'{x}. yargıyı değerlendir',stm[x][2][0].upper()+stm[x][2][1:]+'.',f'{x} '+('doğru' if stm[x][1] else 'yanlış')) for x in ('I','II','III')]
    ad.append(A('Sonucu yaz',f'Doğru yargılar: {", ".join(T)}.',dogru))
    metin=premise+'\nBuna göre,\n'+'\n'.join(f'{x}. {stm[x][0]}' for x in ('I','II','III'))+'\nyargılarından hangileri doğrudur?'
    q(no,ad,metin=metin,dogru=dogru,yan=yan,sira=sira,istenen='Doğru olan yargılar.',**k)
    return dogru

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
BSIM=B('Yön sembolleri ve sağ el kuralı','⊙ sayfa düzleminden dışarı, ⊗ sayfa düzlemine içeri yönü gösterir. Akım taşıyan düz telde başparmak akım yönünü, kıvrılan dört parmak alan çizgilerinin dönüş yönünü gösterir. Örnek: sayfaya içeri akım taşıyan telin üstündeki noktada alan sağa doğrudur')
BTEL=B('Düz telin manyetik alanı','Uzun düz telde B = μ₀·i ÷ (2π·d) = 2×10⁻⁷·i ÷ d (T; i amper, d metre). Alan akımla doğru, uzaklıkla ters orantılıdır. Örnek: 3 A’lik telden 5 cm uzakta B = 2×10⁻⁷·3 ÷ 0,05 = 1,2×10⁻⁵ T’dır')
BHAL=B('Halka ve bobinin merkezindeki alan','N sarımlı, yarıçapı r olan çembersel bobinin merkezinde B = μ₀·N·i ÷ (2r) olur; yönü sağ el kuralıyla bulunur (parmaklar akım yönünde kıvrılır, başparmak alanı gösterir). Örnek: μ₀ = 4π×10⁻⁷ ve π = 3 için, r = 0,1 m ve tek sarımda 1 A akım 6×10⁻⁶ T alan oluşturur')
BSOL=B('Solenoidin içindeki alan','Uzun solenoidin içinde alan düzgündür: B = μ₀·n·i, n = N ÷ ℓ (birim uzunluktaki sarım sayısı). Alan sarım sayısı ve akımla doğru orantılıdır; solenoidin kesit alanına bağlı değildir. Örnek: 200 sarımlık 0,5 m’lik solenoidde n = 400 sarım/m’dir')
BFT=B('Tele etkiyen manyetik kuvvet','F = B·i·L·sinθ; θ, akım yönü ile B arasındaki açıdır. Yönü sağ el kuralıyla bulunur: dört parmak akımı, avuçtan çıkan yön B’yi gösterecek biçimde açılır; başparmak kuvvetin yönünü verir. Örnek: B = 0,6 T, i = 5 A, L = 0,4 m ve θ = 90° için F = 1,2 N’dur')
BPAR=B('Paralel akımlı teller','Aynı yönlü akımlar birbirini çeker, zıt yönlü akımlar iter. L uzunluğundaki parça için F = 2×10⁻⁷·i₁·i₂·L ÷ d. Etki–tepki gereği iki tele etkiyen kuvvetler eşit büyüklükte ve zıt yönlüdür. Örnek: 20 A ve 40 A’lik teller 0,2 m aralıklıysa 1 m’de F = 2×10⁻⁷·800 ÷ 0,2 = 8×10⁻⁴ N’dur')
BQ=B('Yüklü parçacığa etkiyen kuvvet','F = q·v·B·sinθ; kuvvet hıza ve B’ye diktir, hızın büyüklüğünü değiştirmez. Pozitif yük için yön sağ el kuralıyla (parmaklar v, avuç içi B yönünde) bulunur; negatif yükte kuvvet ters yönlüdür. Örnek: 5 μC’lik yük B = 0,4 T’ye dik 2000 m/s ile girerse F = 4×10⁻³ N’dur')
BR=B('Çembersel yörünge','v ⟂ B ise yük çembersel hareket yapar: q·v·B = m·v² ÷ r → r = m·v ÷ (q·B). Periyot T = 2π·m ÷ (q·B) olup hızdan bağımsızdır. Örnek: m ve q aynı, hız 3 katına çıkarsa yarıçap 3 katına çıkar, periyot değişmez')
BSEL=B('Hız seçici','E ve B birbirine dik olan bölgede q·E = q·v·B ise yük doğrusal gider: v = E ÷ B. Bu hız yükün işaretine, yük miktarına ve kütlesine bağlı değildir. Örnek: E = 600 V/m ve B = 0,3 T için v = 2000 m/s’dir')
BHIZ=B('Potansiyel farkıyla hızlanma','Durgun yük V potansiyel farkıyla hızlanırsa q·V = ½·m·v² olur. Yani kazanılan kinetik enerji yük ve potansiyel farkıyla belirlenir. Örnek: 4 V ile hızlanan 3 C yük 12 J enerji kazanır')
BTOP=B('Alanların bileşkesi','Birden çok kaynağın alanı vektörel toplanır: aynı yönlü alanlar toplanır, zıt yönlüler çıkarılır. Her kaynağın alanı kendi yönü ve büyüklüğüyle ayrı bulunur. Örnek: aynı noktada 4 μT sağa ve 7 μT sola alan varsa bileşke 3 μT soladır')
BTELB=B('Eğri telde kuvvet','Eğri tel küçük doğrusal parçalara bölünür; her parçaya F = B·i·ℓ·sinθ ile kuvvet etkir ve kuvvetler vektörel toplanır. Örnek: aynı telin iki parçasına dik doğrultularda 3 N ve 4 N’luk kuvvetler etkiyorsa bileşke 5 N’dur')
BDEN=B('Denge','Cisim dengedeyse net kuvvet sıfırdır; kuvvetler eğim doğrultusunda ve ona dik doğrultuda bileşenlerine ayrılıp ayrı ayrı eşitlenir. Örnek: eğik düzlemde durgun cismin ağırlığının eğim boyunca bileşeni, ona karşı koyan kuvvetin eğim boyunca bileşenine eşittir')

# ---------- kartlar ----------
kartla('K-AFMANYETIK-01','Düz telin çevresindeki alan yönü','Sağ el kuralıyla tele dik düzlemde alanın dönüş yönü ve alanın uzaklıkla ters orantısı yorumlanır.','Alan yönünü telden uzaklaşan sanmak; zıt taraflarda alanı aynı yönde saymak.','kolay','öncüllü',3,'mn-tel','Düz telin manyetik alanı')
kartla('K-AFMANYETIK-02','Düz telin alanı (sayısal)','B = 2×10⁻⁷·i ÷ d formülünde birimler SI’ya çevrilerek uygulanır.','Uzaklığı cm bırakmak; sabiti yanlış almak.','kolay','şekilli',3,'mn-tel','Düz telin manyetik alanı')
kartla('K-AFMANYETIK-03','Düzgün alanda tel','F = B·i·L·sinθ; θ akım ile alan arasındaki açıdır.','cosθ kullanmak; sinθ’yı hiç yazmamak.','kolay','şekilli',3,'mn-kuvvet','Akım taşıyan tele etkiyen kuvvet')
kartla('K-AFMANYETIK-04','Dik alanda üç tel (yön)','Her telin akım yönü ve B yönü için F = i·(l × B) ile kuvvet yönü bulunur.','Kuvveti akım ya da alan doğrultusunda sanmak; sağ el kuralında işaret karıştırmak.','orta','öncüllü',4,'mn-kuvvet','Akım taşıyan tele etkiyen kuvvet')
kartla('K-AFMANYETIK-05','Paralel tellerde kuvvet','F = 2×10⁻⁷·i₁·i₂·L ÷ d bağıntısı; boy ve uzaklık SI’da yazılır.','Akımları toplamak; uzaklığın karesini almak; uzunluğu unutmak.','orta','şekilli',4,'mn-paralel','Paralel akımlı teller')
kartla('K-AFMANYETIK-06','İki zıt telin bileşke alanı','Her telin alanı sağ el kuralıyla yönlendirilip noktada vektörel toplanır; bileşkenin sıfır olduğu nokta bulunur.','Yönleri hesaba katmadan büyüklükleri toplamak; sıfır noktasını iki telin arasında aramak.','orta','öncüllü',5,'mn-tel','Düz telin manyetik alanı')
kartla('K-AFMANYETIK-07','Çembersel bobinin merkezi','B = μ₀·N·i ÷ (2r) ve π = 3 ile işlem; yarıçap metreye çevrilir.','Sarım sayısını unutmak; yarıçap yerine çap yazmak; 2’yi atlamak.','orta','şekilli',4,'mn-halka','Halka ve bobinin alanı')
kartla('K-AFMANYETIK-08','Eş merkezli iki halka','Her halkanın merkezdeki alan yönü akım yönüne, büyüklüğü i ÷ r oranına bağlıdır; bileşke vektörel bulunur.','Akım yönlerini göz ardı etmek; büyük halkanın alanını büyük sanmak.','orta','öncüllü',5,'mn-halka','Halka ve bobinin alanı')
kartla('K-AFMANYETIK-09','Solenoidin içindeki alan','Sargı akımı yönünden alan yönü; B = μ₀·n·i’ye göre n ve i değişiminin etkisi.','Alanı kesit alanına bağlamak; boyu uzatınca alanın arttığını sanmak.','orta','öncüllü',5,'mn-halka','Halka ve bobinin alanı')
kartla('K-AFMANYETIK-10','Dik alanda pozitif ve negatif yük','Pozitif yük için F = q·(v × B); negatif yükte kuvvet ters yönlüdür.','Negatif yükte yönü değiştirmemek; kuvveti hız yönünde sanmak.','orta','öncüllü',4,'mn-yuklu','Yüklü parçacığın manyetik alandaki hareketi')
kartla('K-AFMANYETIK-11','Yörüngeden yük işareti','Sapma yönü ve doğrusal giden yörünge, yükün işaretini ve nötr olup olmadığını belirler.','Doğrusal giden parçacığın yüklü ama hızı alana paralel olduğunu varsaymak; sapma yönünü ters yorumlamak.','orta','öncüllü',4,'mn-yuklu','Yüklü parçacığın manyetik alandaki hareketi')
kartla('K-AFMANYETIK-12','Hız seçici','Elektrik ve manyetik kuvvet eşit: v = E ÷ B, E = V ÷ d.','Gerilimi alan sanmak; v = E·B yazmak; d’yi cm bırakmak.','orta','şekilli',4,'mn-yuklu','Yüklü parçacığın manyetik alandaki hareketi')
kartla('K-AFMANYETIK-13','Proton ve alfa yörüngeleri','r = m·v ÷ (q·B), T = 2π·m ÷ (q·B), F = q·v·B oranları kütle ve yük oranlarıyla yorumlanır.','Kuvveti yükten bağımsız sanmak; periyodu hıza bağlamak.','orta','öncüllü',5,'mn-cember','Yüklü parçacığın çembersel hareketi')
kartla('K-AFMANYETIK-14','Eğri telde net kuvvet','Eğri telin her parçasına etkiyen kuvvetin yönü ve büyüklüğü ayrı bulunup vektörel birleştirilir.','Telin toplam uzunluğunu kullanmak; parçaları skaler toplamak.','orta','şekilli',4,'mn-kuvvet','Akım taşıyan tele etkiyen kuvvet')
kartla('K-AFMANYETIK-15','Kütle spektrometresi','Hız seçiciden çıkan hız ile B₂ bölgesinde çember yarıçapı bulunur; vuruş noktası girişten 2r uzaktadır.','Yarıçapla çapı karıştırmak; hız seçici alanını çember bölgesinde kullanmak.','zor','şekilli',5,'mn-cember','Yüklü parçacığın çembersel hareketi')
kartla('K-AFMANYETIK-16','Eğik düzlemde dengedeki çubuk','Manyetik kuvvetin yönü sağ el kuralıyla bulunur; denge eğim doğrultusunda kurulur.','Kuvveti eğim boyunca saymak; ağırlığın bileşenini yanlış almak.','zor','şekilli',5,'mn-kuvvet','Akım taşıyan tele etkiyen kuvvet')
kartla('K-AFMANYETIK-17','Düz tel + halka alanının sıfırlanması','Tel ve halkanın merkezde zıt yönlü alanları eşitlenir.','Halka formülünü düz tele uygulamak; 2π ve 2 çarpanlarını karıştırmak.','zor','şekilli',5,'mn-halka','Halka ve bobinin alanı')
kartla('K-AFMANYETIK-18','Üç telin net kuvveti','Aynı yönlü akımlar çeker, zıt yönlüler iter; dik iki kuvvet vektörel birleşir.','Kuvvetleri skaler toplamak; çekme/itme yönünü ters almak.','zor','şekilli',5,'mn-paralel','Paralel akımlı teller')
kartla('K-AFMANYETIK-19','Alan bölgesinden sapma açısı','Bölge genişliği d ve sapma θ için r = d ÷ sinθ; eşit q, v ve B’de kütle yarıçapla orantılıdır.','Sapma açısını yarıçapla doğru orantılamak; oranı ters yazmak.','zor','şekilli',5,'mn-cember','Yüklü parçacığın çembersel hareketi')
kartla('K-AFMANYETIK-20','Aynı gerilimle hızlanan parçacıklar','q·V = ½mv² ile hız, ardından r = mv ÷ (qB) ile yarıçap; r ∝ √(m ÷ q).','Aynı gerilimi aynı hız sanmak; yarıçapı doğrudan kütleyle orantılamak.','zor','şekilli',4,'mn-cember','Yüklü parçacığın çembersel hareketi')

def kosul(): pass
# ================= 01 kolay · düz tel çevresi (öncüllü) =================
d1=1
telK,telL,telM=(2,0),(0,4),(-2,0)
bK=Btel((0,0),+1,1,telK); bL=Btel((0,0),+1,1,telL); bM=Btel((0,0),+1,1,telM)
assert bK==(0,Fr(1,2)) and bL==(Fr(-1,4),0) and bM==(0,Fr(-1,2))
assert abs(bK[1])==2*abs(bL[0]) and bK==tuple(-c for c in bM) and yon(bL)=='sola'
body='\\draw[dashed,gray] (0,0) -- (2,0); \\draw[dashed,gray] (0,0) -- (-2,0); \\draw[dashed,gray] (0,0) -- (0,4);\n'
body+=cik(0,0,.24)+' \\node[font=\\small] at (.55,-.42) {$i$}; \\node[font=\\small] at (1,.28) {$d$}; \\node[font=\\small] at (-1,.28) {$d$}; \\node[font=\\small] at (-.38,2) {$2d$};\n'
for nm_,(x,y),pos in (('K',telK,'above right'),('L',telL,'above right'),('M',telM,'above left')):
    body+=f'\\fill ({x},{y}) circle (.08); \\node[font=\\small,{pos}] at ({x},{y}) {{{nm_}}};\n'
body+=legend(-2.4,-1.3)
SK=fig(body)
oncq('0001','A',
 'Sayfa düzlemine dik olan uzun, düz bir telden sayfadan dışarı doğru sabit i akımı geçmektedir. K, L ve M noktaları şekildeki gibi konumlanmıştır; K ve M noktaları tele d, L noktası 2d uzaklıktadır.',
 {'I':('K noktasındaki alanın büyüklüğü, L noktasındakinin 2 katıdır.',True,'alan uzaklıkla ters orantılıdır; K tele d, L ise 2d uzaklıktadır'),
  'II':('K ve M noktalarındaki manyetik alanlar aynı yönlüdür.',False,'telin zıt taraflarındaki K ve M noktalarında alan çizgileri zıt yönlüdür (K’de yukarı, M’de aşağı)'),
  'III':('L noktasındaki manyetik alan, sayfa düzleminde sağa doğrudur.',False,'sağ el kuralına göre telin üstündeki L noktasında alan sola doğrudur')},
 tipId='mn-tel',tip='Düz telin manyetik alanı',z='kolay',alt='Düz Telin Alanı',kaz='Akım taşıyan uzun düz telin çevresindeki manyetik alanın yönünü sağ el kuralıyla belirler, büyüklüğünün uzaklıkla değişimini yorumlar.',
 kart='K-AFMANYETIK-01 (düz tel, ⊙; K, M: d, L: 2d)',kalip='öncüllü',ip=['Alan çizgilerinin tel çevresindeki dönüş yönünü önce sağ el kuralıyla belirle.'],bilgi=[BTEL,BSIM],sekil=SK,
 puf='Her noktadaki alanın yönünü ve büyüklüğünü ayrı ayrı değerlendir.',
 onadim=[A('Alan yönlerini bul','Başparmak sayfadan dışarı, dört parmak saat yönünün tersine döner.',f'K’de {yon(bK)}, M’de {yon(bM)}, L’de {yon(bL)}')])

# ================= 02 kolay · düz telin alanı (sayısal) =================
i2,d2=6,Fr(4,100); B2=Fr(2,10**7)*i2/d2*10**6
assert B2==30
e2=[(Fr(2,10**7)*i2/4*10**6,'Uzaklığı santimetre cinsinden (4) yazmış: B = 2×10⁻⁷·6 ÷ 4 = 3×10⁻⁷ T = 0,3 μT.','islem'),
    (Fr(1,10**7)*i2/d2*10**6,'Sabiti 10⁻⁷ almış (2 çarpanını atlamış): B = 10⁻⁷·6 ÷ 0,04 = 1,5×10⁻⁵ T = 15 μT.','bilgi'),
    (Fr(4,10**7)*i2/d2*10**6,'Sabiti 4×10⁻⁷ almış: B = 4×10⁻⁷·6 ÷ 0,04 = 6×10⁻⁵ T = 60 μT.','bilgi'),
    (Fr(2,10**7)*i2/d2**2*10**6,'Alanı uzaklığın karesiyle ters orantılı sanmış: B = 2×10⁻⁷·6 ÷ 0,04² = 7,5×10⁻⁴ T = 750 μT.','bilgi')]
assert [c[0] for c in e2]==[Fr(3,10),15,60,750]
body=cik(0,0,.24)+' \\node[font=\\small] at (.6,-.45) {$i=6$ A}; \\fill (3.4,0) circle (.08); \\node[font=\\small,above] at (3.4,.05) {P};\n'
body+='\\draw[dashed,gray] (0,0) -- (3.4,0); \\draw[<->] (0,-1.0) -- (3.4,-1.0); \\node[font=\\small,below] at (1.7,-1.0) {4 cm};\n'
body+=legend(-.6,-2.1)
SK=fig(body)
q('0002',tipId='mn-tel',tip='Düz telin manyetik alanı',z='kolay',alt='Düz Telin Alanı',kaz='Uzun düz telin belirli bir uzaklıktaki manyetik alanının büyüklüğünü hesaplar.',
 kart='K-AFMANYETIK-02 (düz tel, 6 A, 4 cm)',kalip='şekilli',
 metin='Sayfa düzlemine dik, çok uzun bir telden şekildeki yönde ve büyüklükte akım geçmektedir. Tele 4 cm uzaklıktaki P noktası da şekilde gösterilmiştir.\n(μ₀ ÷ 2π = 2×10⁻⁷ T·m/A alınız; 1 μT = 10⁻⁶ T)\nBuna göre, P noktasındaki manyetik alanın büyüklüğü kaç μT’dır?',
 dogru=B2,yan=sec(B2,e2,'C'),istenen='P noktasındaki manyetik alanın büyüklüğü (μT).',ip=['Formülde uzaklığın hangi birimde yazılması gerektiğine dikkat et.'],bilgi=[BTEL,BSIM],sekil=SK,
 ad=[A('Birimleri SI’ya çevir','Uzaklık metreye çevrilir.','d = 4 cm = 0,04 m'),
     A('Formülü yaz','Düz telde B = (μ₀ ÷ 2π)·i ÷ d.','B = 2×10⁻⁷ · 6 ÷ 0,04'),
     A('Hesapla','Sonucu teslaya, sonra μT’ya çevir.','B = 3×10⁻⁵ T = 30 μT')],
 puf='Alan, akımla doğru ve uzaklıkla ters orantılıdır; uzaklığı metreye çevirmeyi unutma.')

# ================= 03 kolay · tele etkiyen kuvvet =================
B3,i3,L3,sin37=Fr(1,2),4,Fr(1,2),Fr(6,10); F3=B3*i3*L3*sin37
assert F3==Fr(3,5)
lb=kuvvet_xy((Fr(8,10),Fr(6,10),0),(1,0,0)); assert lb[2]==Fr(-6,10)     # kuvvet sayfaya içeri, büyüklük 0,6
e3=[(B3*i3*L3*sin37**2,'sinθ yerine sin²θ almış: F = 0,5·4·0,5·0,36 = 0,36 N.','islem'),
    (B3*i3*L3*Fr(8,10),'Alanla akım arasındaki açıyı 37° yerine 53° almış (cos37° kullanmış): F = 0,5·4·0,5·0,8 = 0,8 N.','dikkat'),
    (B3*i3*L3,'Açının etkisini hiç hesaba katmamış (sinθ = 1 almış): F = 0,5·4·0,5 = 1 N.','bilgi'),
    (B3*i3*sin37,'Telin uzunluğunu çarpmayı unutmuş: F = 0,5·4·0,6 = 1,2 N.','dikkat')]
assert [c[0] for c in e3]==[Fr(36,100),Fr(8,10),1,Fr(12,10)]
body=''.join(vk(0,y,7.6,y,MAV,'thick') for y in (0,1.3,2.6,3.9))+'\\node[font=\\small,'+MAV+'] at (7.9,4.5) {$\\vec B$}; \\node[font=\\small,right,'+MAV+'] at (7.7,2.0) {0,5 T};\n'
body+='\\draw[dashed,gray] (1.5,.65) -- (3.4,.65); \\draw[very thick,'+f'{ARR}'+'] (1.5,.65) -- (4.7,3.05);\n'
body+='\\draw (2.3,.65) arc (0:37:.8); \\node[font=\\small] at (2.95,.93) {$37^\\circ$};\n'
body+='\\node[font=\\small,anchor=east] at (2.95,1.75) {$L=0{,}5$ m}; \\node[font=\\small,right] at (4.8,3.0) {$i=4$ A};\n'
SK=fig(body)
q('0003',tipId='mn-kuvvet',tip='Akım taşıyan tele etkiyen kuvvet',z='kolay',alt='Tele Etkiyen Manyetik Kuvvet',kaz='Düzgün manyetik alan içinde akım taşıyan teli etkileyen kuvvetin büyüklüğünü açıya bağlı olarak hesaplar.',
 kart='K-AFMANYETIK-03 (sin37, B=0,5 T, i=4 A, L=0,5 m)',kalip='şekilli',
 metin='Sayfa düzleminde bulunan düzgün bir manyetik alan içine, 0,5 m uzunluğundaki doğrusal bir tel şekildeki gibi yerleştirilmiş ve telden şekilde verilen yönde ve büyüklükte akım geçirilmiştir. Tel, alan çizgileriyle 37° açı yapmaktadır.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre, tele etkiyen manyetik kuvvetin büyüklüğü kaç N’dur?',
 dogru=F3,yan=sec(F3,e3,'B'),istenen='Tele etkiyen manyetik kuvvetin büyüklüğü (N).',ip=['Kuvvetin büyüklüğü, akım ile alan çizgileri arasındaki açıya nasıl bağlıdır?'],bilgi=[BFT,BSIM],sekil=SK,
 ad=[A('Açıyı belirle','Akım yönü ile B arasındaki açı 37°’dir.','θ = 37°'),
     A('Formülü yaz','F = B·i·L·sinθ.','F = 0,5 · 4 · 0,5 · 0,6'),
     A('Hesapla','Çarpımı yap.','F = 0,6 N')],
 puf='Kuvvet, akım ile alan arasındaki açının sinüsüyle orantılıdır.')

# ================= 04 orta · üç tel, kuvvet yönü (öncüllü) =================
B4=(0,0,-1)      # içeri
FK=kuvvet_xy((1,0,0),B4); FL=kuvvet_xy((0,1,0),B4); FM=kuvvet_xy((-1,0,0),B4)
assert FK[:2]==(0,1) and FL[:2]==(-1,0) and FM[:2]==(0,-1)
wires=[((1.4,4.0),(4.2,4.0)),((5.6,1.0),(5.6,3.6)),((8.6,1.0),(6.8,1.0))]
cand=[(x,y) for x in (.7,2.4,4.1,7.6,8.5) for y in (.5,2.3,4.4)]+[(5.6,.5),(5.6,4.4),(7.0,2.5),(3.0,2.3)]
fr=serbest(cand,wires,mind=.6)
body='\\draw[gray,thin] (0,0) rectangle (9.2,5.0);\n'+''.join(ici(x,y,.15,MAV) for x,y in fr)+'\n'
for (a,b),nmx,pos in zip(wires,'KLM',('above','left','below')):
    body+=vk(a[0],a[1],b[0],b[1],'black','very thick')
    mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
    body+=f'\\node[font=\\small,{pos}] at ({mx},{my}) {{{nmx}}};\n'
body+=legend(0,-.7)+' \\node[font=\\small,'+MAV+',right] at (6.6,-.7) {$\\vec B$ içeri}; '
SK=fig(body)
oncq('0004','B',
 'Şekildeki gibi, düzgün ve sayfa düzlemine içeri doğru yönelmiş bir manyetik alan içine, sayfa düzleminde bulunan K, L ve M telleri yerleştirilmiştir. Üç telin uzunlukları ve içlerinden geçen akımların büyüklükleri eşit olup akımların yönleri oklarla gösterilmiştir. Tellerin birbirine etkisi önemsizdir.',
 {'I':('K teline etkiyen manyetik kuvvet, sayfa düzleminde yukarı doğrudur.',True,'sağ el kuralına göre sağa doğru akım ve içeri doğru alan için kuvvet yukarı yöndedir'),
  'II':('L teline etkiyen manyetik kuvvet, sayfa düzleminde sola doğrudur.',True,'yukarı doğru akım ve içeri doğru alan için kuvvet sağ el kuralına göre sola doğrudur'),
  'III':('M teline etkiyen manyetik kuvvet, sayfa düzleminde yukarı doğrudur.',False,'sola doğru akım ve içeri doğru alan için kuvvet sağ el kuralına göre aşağı yöndedir')},
 tipId='mn-kuvvet',tip='Akım taşıyan tele etkiyen kuvvet',z='orta',alt='Tele Etkiyen Manyetik Kuvvet',kaz='Düzgün manyetik alandaki akım taşıyan tellere etkiyen kuvvetin yönünü sağ el kuralıyla belirler.',
 kart='K-AFMANYETIK-04 (B içeri; K →, L ↑, M ←)',kalip='öncüllü',ip=['Her tel için akım yönü, B yönü ve kuvvet yönünün birbirine dik olduğunu kullan.'],bilgi=[BFT,BSIM],sekil=SK,
 puf='Akım yönü ters çevrilince kuvvet de ters yönlü olur.',
 onadim=[A('Kuvvet yönlerini bul','Sağ el kuralını her tele uygula.',f'K: {yon(FK)}, L: {yon(FL)}, M: {yon(FM)}')])

# ================= 05 orta · paralel teller =================
i1,i2b,d5,L5=30,50,Fr(1,10),2
F5=Fr(2,10**7)*i1*i2b/d5*L5*1000
assert F5==6
e5=[(Fr(2,10**7)*i1*i2b/d5*1000,'Tel uzunluğunu (2 m) çarpmayı unutmuş: F = 2×10⁻⁷·1500 ÷ 0,1 = 3×10⁻³ N = 3 mN.','dikkat'),
    (Fr(2,10**7)*i1*i2b/10*L5*1000,'Uzaklığı santimetre cinsinden (10) yazmış: F = 2×10⁻⁷·1500 ÷ 10·2 = 6×10⁻⁵ N = 0,06 mN.','islem'),
    (Fr(2,10**7)*(i1+i2b)/d5*L5*1000,'Akımları çarpmak yerine toplamış: F = 2×10⁻⁷·80 ÷ 0,1·2 = 3,2×10⁻⁴ N = 0,32 mN.','islem'),
    (Fr(2,10**7)*i1*i2b/d5**2*L5*1000,'Kuvveti uzaklığın karesiyle ters orantılı sanmış: F = 2×10⁻⁷·1500 ÷ 0,01·2 = 0,06 N = 60 mN.','bilgi')]
assert [c[0] for c in e5]==[3,Fr(6,100),Fr(32,100),60]
body='\\draw[very thick] (0,2.2) -- (7,2.2); \\draw[very thick] (0,0) -- (7,0);\n'+vk(6.2,2.2,7.3,2.2,'black','very thick')+vk(6.2,0,7.3,0,'black','very thick')+'\n'
body+='\\node[font=\\small,above] at (1.0,2.25) {X: $i_1=30$ A}; \\node[font=\\small,below] at (1.0,-.05) {Y: $i_2=50$ A};\n'
body+='\\draw[<->] (-.5,0) -- (-.5,2.2); \\node[font=\\small,left] at (-.55,1.1) {10 cm};\n'
body+='\\draw[|<->|] (2.0,3.0) -- (5.4,3.0); \\node[font=\\small,above] at (3.7,3.0) {2 m}; \\draw[dotted] (2.0,3.0) -- (2.0,0); \\draw[dotted] (5.4,3.0) -- (5.4,0);\n'
SK=fig(body)
q('0005',tipId='mn-paralel',tip='Paralel akımlı teller',z='orta',alt='Paralel Akımlı Teller',kaz='Birbirine paralel, akım taşıyan iki telin birbirine uyguladığı kuvvetin büyüklüğünü hesaplar.',
 kart='K-AFMANYETIK-05 (30 A, 50 A, 10 cm, 2 m)',kalip='şekilli',
 metin='Sayfa düzleminde, birbirine paralel ve çok uzun X ve Y telleri şekildeki gibi yerleştirilmiş; tellerden aynı yönlü akımlar geçmektedir. Akım şiddetleri ve teller arasındaki uzaklık şekilde verilmiştir.\n(μ₀ ÷ 2π = 2×10⁻⁷ T·m/A alınız; 1 mN = 10⁻³ N)\nBuna göre, tellerin şekilde gösterilen 2 m’lik kısımları arasındaki karşılıklı çekme kuvvetinin büyüklüğü kaç mN’dur?',
 dogru=F5,yan=sec(F5,e5,'D'),istenen='2 m’lik kısımlar arasındaki kuvvetin büyüklüğü (mN).',ip=['Önce bir telin diğerinin bulunduğu yerde oluşturduğu alanı düşün.'],bilgi=[BPAR,BTEL],sekil=SK,
 ad=[A('Birimleri hazırla','Uzaklık metreye çevrilir.','d = 10 cm = 0,1 m'),
     A('Bir telin alanını bul','Y telinin X’in bulunduğu yerdeki alanı.','B = 2×10⁻⁷ · 50 ÷ 0,1 = 10⁻⁴ T'),
     A('Kuvveti yaz','F = B·i·L, X teline.','F = 10⁻⁴ · 30 · 2 = 6×10⁻³ N'),
     A('Birimi çevir','Newton’dan milinewtona.','F = 6 mN')],
 puf='İki tel arasındaki kuvvet, akımların çarpımıyla ve uzunlukla doğru, uzaklıkla ters orantılıdır.')

# ================= 06 orta · iki telin bileşke alanı (öncüllü) =================
X6,Y6=(0,0),(4,0)
bK6=tuple(a+b for a,b in zip(Btel(X6,+1,1,(2,0)),Btel(Y6,-1,2,(2,0))))
bL6=tuple(a+b for a,b in zip(Btel(X6,+1,1,(-2,0)),Btel(Y6,-1,2,(-2,0))))
bN6=tuple(a+b for a,b in zip(Btel(X6,+1,1,(-4,0)),Btel(Y6,-1,2,(-4,0))))
assert bK6==(0,Fr(3,2)) and bL6==(0,Fr(-1,6)) and bN6==(0,0)
u=.9
body='\\draw[dashed,gray] (%.2f,0) -- (%.2f,0);\n'%(-4.6*u,4.6*u)
body+=cik(0,0,.24)+f' \\node[font=\\small] at (0,.7) {{X, $i$}}; '+ici(4*u,0,.24)+f' \\node[font=\\small] at ({4*u},.7) {{Y, $2i$}};\n'
for nmx,x in (('K',2),('L',-2),('N',-4)):
    body+=f'\\fill ({x*u:.2f},0) circle (.08); \\node[font=\\small,above] at ({x*u:.2f},.08) {{{nmx}}};\n'
for a,b in ((-4,-2),(-2,0),(0,2),(2,4)):
    body+=f'\\draw[|<->|] ({a*u:.2f},-.75) -- ({b*u:.2f},-.75); \\node[font=\\small,below] at ({(a+b)/2*u:.2f},-.75) {{$2d$}};\n'
body+=legend(-3.3,-2.0)
SK=fig(body)
oncq('0006','E',
 'Sayfa düzlemine dik, çok uzun X ve Y telleri şekildeki gibi yerleştirilmiştir. X telinden sayfadan dışarı doğru i, Y telinden sayfaya içeri doğru 2i akımı geçmektedir. K, L ve N noktaları ile teller aynı doğru üzerindedir ve komşu noktalar arası uzaklık 2d’dir.',
 {'I':('K noktasındaki bileşke manyetik alan, sayfa düzleminde aşağı doğrudur.',False,'X’in ve Y’nin K’deki alanları yukarı yönlüdür; bileşke de yukarı doğrudur'),
  'II':('L noktasındaki bileşke manyetik alan, sayfa düzleminde aşağı doğrudur.',True,'L’de X’in aşağı doğru alanı, Y’nin yukarı doğru alanından büyüktür (L tele daha yakındır)'),
  'III':('N noktasındaki bileşke manyetik alan sıfırdır.',True,'N’de X’in alanı i ÷ 4d, Y’ninki 2i ÷ 8d olup zıt yönlü ve eşit büyüklüktedir')},
 tipId='mn-tel',tip='Düz telin manyetik alanı',z='orta',alt='Düz Telin Alanı',kaz='Birden çok telin oluşturduğu manyetik alanların bileşkesini yön ve büyüklük bakımından yorumlar.',
 kart='K-AFMANYETIK-06 (X ⊙ i, Y ⊗ 2i; K, L, N)',kalip='öncüllü',ip=['Noktanın her tele uzaklığını ve alanların yönlerini ayrı ayrı belirle.'],bilgi=[BTEL,BTOP],sekil=SK,
 puf='Her telin alanını ayrı ayrı vektörel çizip noktada birleştir.',
 onadim=[A('Her telin alanını bul','Alan yönleri sağ el kuralıyla, büyüklükleri i ÷ d ile bulunur (μ₀ ÷ 2π ortak).','K: X ve Y yukarı; L ve N: X aşağı, Y yukarı')])

# ================= 07 orta · çembersel bobinin merkezi =================
N7,i7,r7=10,2,Fr(5,100); mu0=12*Fr(1,10**7)   # μ0 = 4π·10⁻⁷, π = 3
B7=mu0*N7*i7/(2*r7)*10**6
assert B7==240
e7=[(mu0*i7/(2*r7)*10**6,'Sarım sayısını (10) hesaba katmamış: B = 12×10⁻⁷·2 ÷ 0,1 = 2,4×10⁻⁵ T = 24 μT.','dikkat'),
    (mu0*N7*i7/(2*Fr(10,100))*10**6,'Yarıçap yerine çapı (10 cm) yazmış: B = 12×10⁻⁷·20 ÷ 0,2 = 1,2×10⁻⁴ T = 120 μT.','islem'),
    (mu0*N7*i7/r7*10**6,'Paydadaki 2 çarpanını atlamış: B = 12×10⁻⁷·20 ÷ 0,05 = 4,8×10⁻⁴ T = 480 μT.','bilgi'),
    (mu0*N7*i7/(2*5)*10**6,'Yarıçapı santimetre cinsinden (5) yazmış: B = 12×10⁻⁷·20 ÷ 10 = 2,4×10⁻⁶ T = 2,4 μT.','islem')]
assert [c[0] for c in e7]==[24,120,480,Fr(24,10)]
body='\\draw[very thick] (0,0) circle (1.8); \\draw[very thick,'+ARR+'] (1.55,.9) arc (30:62:1.8); \\draw[very thick,'+ARR+'] (-1.55,-.9) arc (210:242:1.8);\n'
body+='\\fill (0,0) circle (.08); \\node[font=\\small,below left] at (0,0) {O}; \\draw[dashed,gray] (0,0) -- (-1.8,0); \\node[font=\\small,above] at (-.9,0) {$r=5$ cm};\n'
body+='\\node[font=\\small,right] at (2.0,0) {$i=2$ A};\n'
SK=fig(body)
q('0007',tipId='mn-halka',tip='Halka ve bobinin alanı',z='orta',alt='Halka ve Bobin',kaz='Çembersel bobinin merkezindeki manyetik alanın büyüklüğünü sarım sayısı, akım ve yarıçapa bağlı olarak hesaplar.',
 kart='K-AFMANYETIK-07 (N=10, i=2 A, r=5 cm, π=3)',kalip='şekilli',
 metin='Sarım sayısı 10 olan, yarıçapı ve içinden geçen akım şekilde verilen ince çembersel bir bobin sayfa düzlemindedir.\n(μ₀ = 4π×10⁻⁷ T·m/A ve π = 3 alınız; 1 μT = 10⁻⁶ T)\nBuna göre, O merkezindeki manyetik alanın büyüklüğü kaç μT’dır?',
 dogru=B7,yan=sec(B7,e7,'D'),istenen='O noktasındaki manyetik alanın büyüklüğü (μT).',ip=['Bobinin tüm sarımlarının merkezde oluşturduğu alanların aynı yönde toplandığını düşün.'],bilgi=[BHAL,BSIM],sekil=SK,
 ad=[A('Birimleri hazırla','Yarıçap metreye, μ₀ π = 3 ile sayıya çevrilir.','r = 0,05 m, μ₀ = 12×10⁻⁷'),
     A('Tek sarımın alanını yaz','Merkezde B₁ = μ₀·i ÷ 2r.','B₁ = 12×10⁻⁷·2 ÷ 0,1 = 2,4×10⁻⁵ T'),
     A('Sarım sayısıyla çarp','Sarımların alanları aynı yönlüdür.','B = 10 · 2,4×10⁻⁵ = 2,4×10⁻⁴ T'),
     A('Birimi çevir','Tesladan μT’ya.','B = 240 μT')],
 puf='Bobinin sarımları merkezde aynı yönde alan oluşturduğundan alan sarım sayısıyla orantılıdır.')

# ================= 08 orta · eş merkezli iki halka (öncüllü) =================
rX,rY,iX,iY=Fr(12,10),Fr(24,10),1,3
BXc=Fr(iX)/rX; BYc=Fr(iY)/rY         # μ0/2 çarpanı ortak; X ccw (+ dışarı), Y cw (− içeri)
net=BXc-BYc
assert BYc/BXc==Fr(3,2) and net<0 and abs(net)==BXc/2
body='\\draw[very thick] (0,0) circle (1.2); \\draw[very thick] (0,0) circle (2.4);\n'
body+='\\draw[very thick,'+ARR+'] (1.04,.6) arc (30:62:1.2); \\draw[very thick,'+ARR+'] (-1.04,-.6) arc (210:242:1.2);\n'      # X: saat yönünün tersi
body+='\\draw[very thick,'+ARR+'] (2.08,1.2) arc (30:2:2.4); \\draw[very thick,'+ARR+'] (-2.08,-1.2) arc (210:182:2.4);\n' # Y: saat yönü
body+='\\fill (0,0) circle (.08); \\node[font=\\small,above right] at (0,0) {O}; \\node[font=\\small] at (0,-.75) {X}; \\node[font=\\small] at (0,-1.8) {Y};\n'
body+='\\node[font=\\small,anchor=west] at (-2.4,-3.1) {X: $i$ (saat yönünün tersi)}; \\node[font=\\small,anchor=west] at (-2.4,-3.6) {Y: $3i$ (saat yönünde)};\n'
SK=fig(body)
oncq('0008','E',
 'Yarıçapları r ve 2r olan, eş merkezli ve aynı düzlemde bulunan X ve Y halkalarından sırasıyla i ve 3i büyüklüğünde akımlar şekilde gösterilen yönlerde geçmektedir. X’ten geçen akımın yönü saat yönünün tersi, Y’ninki saat yönündedir.',
 {'I':('X halkasının O merkezinde oluşturduğu alan, Y halkasınınkinden büyüktür.',False,'merkezdeki alan i ÷ r ile orantılıdır: X için i ÷ r, Y için 3i ÷ 2r olup Y’ninki 1,5 kat büyüktür'),
  'II':('O noktasındaki bileşke manyetik alan sayfa düzlemine diktir ve içeri doğrudur.',True,'X sayfadan dışarı, daha büyük olan Y ise içeri alan oluşturur; bileşke içeri yönlüdür'),
  'III':('O noktasındaki bileşke alanın büyüklüğü, X’in tek başına oluşturduğu alanın yarısına eşittir.',True,'bileşke 3i ÷ 2r − i ÷ r = i ÷ 2r olup X’in tek başına oluşturduğu i ÷ r değerinin yarısıdır')},
 tipId='mn-halka',tip='Halka ve bobinin alanı',z='orta',alt='Halka ve Bobin',kaz='Eş merkezli akımlı halkaların merkezdeki alanlarını yön ve büyüklük bakımından karşılaştırıp bileşkesini yorumlar.',
 kart='K-AFMANYETIK-08 (r ve 2r; i ccw, 3i cw)',kalip='öncüllü',ip=['Her halkanın merkezdeki alanının yönünü akımın dönüş yönünden, büyüklüğünü akım ve yarıçaptan belirle.'],bilgi=[BHAL,BTOP],sekil=SK,
 puf='Halkanın merkezdeki alanı akımla doğru, yarıçapla ters orantılıdır.',
 onadim=[A('Her halkanın alanını bul','Saat yönünün tersi → dışarı, saat yönü → içeri; büyüklük i ÷ r.','X: i ÷ r (dışarı), Y: 3i ÷ 2r (içeri)')])

# ================= 09 orta · solenoid (öncüllü) =================
# kesit: üst sargılar ⊗ (içeri), alt sargılar ⊙ (dışarı). Alan yönü: dönüş eksen etrafında; L_x = y·v_z
ust_vz=-1; Bx=1 if (+1)*ust_vz>0 else -1          # üst tel (y>0), v_z=-1  → B_x = -1 (sola)
assert Bx==-1
body='\\draw[dashed,gray] (-.3,1.2) -- (7.7,1.2); \\draw[gray] (0,.0) rectangle (7.4,2.4);\n'
for k in range(6):
    x=.6+k*1.2; body+=ici(x,2.0,.2)+ cik(x,.4,.2)
body+='\\node[font=\\small,above] at (3.7,2.4) {kesit görünüşü}; \\node[font=\\small] at (-.6,2.0) {üst}; \\node[font=\\small] at (-.6,.4) {alt};\n'
body+='\\draw[|<->|] (0,-.5) -- (7.4,-.5); \\node[font=\\small,below] at (3.7,-.5) {$\\ell$};\n'+legend(.4,-1.5)
SK=fig(body)
oncq('0009','A',
 'Uzunluğu ℓ, sarım sayısı N olan uzun bir solenoidden geçen i akımının sargılardaki yönü, kesit görünüşünde ⊗ ve ⊙ sembolleriyle gösterilmiştir: üst sargılarda akım sayfaya içeri, alt sargılarda sayfadan dışarı doğrudur. Solenoidin içi boştur.',
 {'I':('Solenoidin içindeki manyetik alan, eksen boyunca sağa doğrudur.',False,'sağ el kuralına göre üstte içeri, altta dışarı akım için alan eksen boyunca sola doğrudur'),
  'II':('Akım ve sarım sayısı değişmeden solenoidin boyu 2 katına çıkarılırsa içindeki alan 2 katına çıkar.',False,'B = μ₀·N·i ÷ ℓ olduğundan boy 2 katına çıkınca alan yarıya düşer'),
  'III':('Sarım sayısı yarıya indirilip akım 2 katına çıkarılırsa (boy sabit) içindeki alan değişmez.',True,'B ∝ N·i olduğundan N·i çarpımı değişmediği için alan aynı kalır')},
 tipId='mn-halka',tip='Halka ve bobinin alanı',z='orta',alt='Halka ve Bobin',kaz='Solenoidin içindeki manyetik alanın yönünü sağ el kuralıyla bulur ve sarım sayısı, akım, boy ile ilişkisini yorumlar.',
 kart='K-AFMANYETIK-09 (kesit, üst ⊗ alt ⊙; B ∝ N·i ÷ ℓ)',kalip='öncüllü',ip=['Solenoidin içindeki alanın hangi niceliklerle orantılı olduğunu yazıp değişimleri tek tek uygula.'],bilgi=[BSOL,BSIM],sekil=SK,
 puf='Solenoidin içinde alan, birim uzunluktaki sarım sayısı ile akımın çarpımıyla orantılıdır.')

# ================= 10 orta · yüklü parçacıklara kuvvet (öncüllü) =================
qFK=kuvvet_xy((1,0,0),(0,0,-1)); qFM=kuvvet_xy((0,1,0),(0,0,-1))      # pozitif yük: F ∝ v × B
assert qFK[:2]==(0,1) and qFM[:2]==(-1,0)
qFL=tuple(-c for c in qFK)               # elektron
assert qFL[:2]==(0,-1)
grid=[(x,y) for x in (.8,2.4,4.0,5.6,7.2) for y in (.5,2.2,3.9)]
body='\\draw[gray,thin] (0,0) rectangle (8.0,4.4);\n'+''.join(ici(x,y,.15,MAV) for x,y in grid)+'\n'
def part(x,y,sign,lab): return f'\\draw[thick,fill=white] ({x},{y}) circle (.24); \\node[font=\\small] at ({x},{y}) {{{sign}}}; \\node[font=\\small,above left] at ({x-.2},{y+.15}) {{{lab}}};'
body+=part(1.6,3.05,'+','K')+vk(1.9,3.05,3.4,3.05,'black','very thick')+'\n'+part(1.6,1.35,'$-$','L')+vk(1.9,1.35,3.4,1.35,'black','very thick')+'\n'
body+=part(6.4,.9,'+','M')+vk(6.4,1.2,6.4,2.7,'black','very thick')+'\n'
body+='\\node[font=\\small,'+MAV+',right] at (8.2,2.2) {$\\vec B$ içeri}; \\node[font=\\small] at (2.65,3.35) {$\\vec v$}; \\node[font=\\small] at (2.65,1.65) {$\\vec v$}; \\node[font=\\small] at (6.8,1.95) {$\\vec v$};\n'
body+=legend(0,-.7)
SK=fig(body)
oncq('0010','A',
 'Sayfa düzlemine dik ve içeri doğru yönelmiş düzgün bir manyetik alanın bulunduğu bölgeye, şekilde gösterilen yönlerde ve eşit büyüklükte hızlarla K, L ve M parçacıkları giriyor. K ve M parçacıkları protonu (+), L parçacığı elektronu (−) temsil etmektedir. Başka kuvvetler önemsizdir.',
 {'I':('K parçacığına, girdiği anda sayfa düzleminde yukarı yönde kuvvet etkir.',True,'sağa giden pozitif yüklü parçacığa içeri doğru alanda sağ el kuralına göre yukarı yönde kuvvet etkir'),
  'II':('L parçacığına, girdiği anda sayfa düzleminde yukarı yönde kuvvet etkir.',False,'L negatif yüklü olduğundan K ile aynı hızda ve aynı alanda kuvvet ters, yani aşağı yöndedir'),
  'III':('M parçacığına, girdiği anda sayfa düzleminde sağa doğru kuvvet etkir.',False,'yukarı giden pozitif yüklü parçacığa içeri doğru alanda kuvvet sola doğrudur')},
 tipId='mn-yuklu',tip='Yüklü parçacığın manyetik alandaki hareketi',z='orta',alt='Yüklü Parçacığa Etkiyen Kuvvet',kaz='Düzgün manyetik alana giren pozitif ve negatif yüklü parçacıklara etkiyen kuvvetin yönünü sağ el kuralıyla belirler.',
 kart='K-AFMANYETIK-10 (B içeri; proton →, elektron →, proton ↑)',kalip='öncüllü',ip=['Yükün işaretinin kuvvetin yönüne nasıl yansıdığını düşünerek her parçacık için yönü ayrı bul.'],bilgi=[BQ,BSIM],sekil=SK,
 puf='Yükün işareti değişince kuvvetin yönü de değişir; hız ters çevrilince de kuvvet ters yönlü olur.',
 onadim=[A('Kuvvet yönlerini bul','Pozitif yükte F ∝ v × B; negatifte ters.',f'K: {yon(qFK)}, L: {yon(qFL)}, M: {yon(qFM)}')])

# ================= 11 orta · yörüngeden yük işareti (öncüllü) =================
# B dışarı (+z), v = +x : pozitif yükte F ∝ v × B = −y (aşağı); negatif yükte yukarı
fpos=kuvvet_xy((1,0,0),(0,0,1)); assert fpos[:2]==(0,-1)
yK,yL,yM=3.2,2.0,.8
body='\\draw[gray,thin] (3,-1.3) rectangle (9.3,5.0);\n'
cands=[(x,y) for x in (3.8,5.6,7.4,8.6) for y in (-.8,.4,1.4,2.6,3.8,4.5)]
yolK=(3.0,yK,6.5,-90,-48); yolM=(3.0,yM,6.5,90,48)
def arc_pts(c,n=40):
    cx,cy,R,a0,a1=c; return [(cx+R*math.cos(math.radians(a0+(a1-a0)*k/n)),cy+R*math.sin(math.radians(a0+(a1-a0)*k/n))) for k in range(n+1)]
ptsK=arc_pts((3.0,yK+6.5,6.5,-90,-48)); ptsM=arc_pts((3.0,yM-6.5,6.5,90,48))
segs=list(zip(ptsK,ptsK[1:]))+list(zip(ptsM,ptsM[1:]))+[((3,yL),(9.3,yL))]
fr=serbest(cands,segs,mind=.5)
body+=''.join(cik(x,y,.15,MAV) for x,y in fr)+'\n'
body+=f'\\draw[very thick] (0,{yK}) -- (3,{yK}); \\draw[very thick,{ARR}] (3,{yK}) arc (-90:-48:6.5);\n'
body+=f'\\draw[very thick,{ARR}] (0,{yL}) -- (9.3,{yL});\n'
body+=f'\\draw[very thick] (0,{yM}) -- (3,{yM}); \\draw[very thick,{ARR}] (3,{yM}) arc (90:48:6.5);\n'
for nmx,y in (('K',yK),('L',yL),('M',yM)): body+=f'\\node[font=\\small,above] at (.4,{y}) {{{nmx}}};\n'
body+='\\node[font=\\small,'+MAV+',anchor=west] at (3.1,5.3) {$\\vec B$ dışarı}; \\node[font=\\small,anchor=east] at (2.9,5.3) {$\\vec v$ sağa};\n'+legend(3.2,-1.9)
SK=fig(body)
oncq('0011','A',
 'Parçacıklar, sayfa düzlemine dik ve dışarı doğru yönelmiş düzgün bir manyetik alanın bulunduğu bölgeye sayfa düzleminde, sağa doğru ve eşit büyüklükte hızlarla giriyor. Bölgede başka alan yoktur; K, L ve M parçacıklarının şekildeki yollarla hareket ettiği gözlenmiştir. Kütle çekim ve sürtünme önemsizdir.',
 {'I':('K parçacığı pozitif yüklüdür.',False,'sağa giden pozitif yüklü parçacık dışarı doğru alanda aşağı sapar; K yukarı saptığına göre negatif yüklüdür'),
  'II':('L parçacığı yüksüzdür.',True,'hızı alana dik olduğu hâlde sapmayan parçacığa manyetik kuvvet etki etmediğinden yüksüzdür'),
  'III':('K ve M parçacıklarının yükleri aynı işaretlidir.',False,'K yukarı, M aşağı sapmıştır; zıt yönlere sapan parçacıkların yükleri zıt işaretlidir')},
 tipId='mn-yuklu',tip='Yüklü parçacığın manyetik alandaki hareketi',z='orta',alt='Yüklü Parçacığa Etkiyen Kuvvet',kaz='Parçacıkların manyetik alandaki yörüngelerinden yüklerinin işaretini ve yüklü olup olmadığını belirler.',
 kart='K-AFMANYETIK-11 (B dışarı; K yukarı, L düz, M aşağı)',kalip='öncüllü',ip=['Hız ve alan yönü bilindiğine göre pozitif yükün hangi yöne sapacağını önce kendin belirle.'],bilgi=[BQ,BSIM],sekil=SK,
 puf='Pozitif yükün sapacağı yönü önce sağ el kuralıyla bul.',
 onadim=[A('Pozitif yükün sapma yönünü bul','Sağ el kuralı: dışarı doğru alanda sağa giden pozitif yük aşağı sapar.','pozitif: aşağı, negatif: yukarı')])

# ================= 12 orta · hız seçici =================
V12,dd12,Bs12=200,Fr(5,100),Fr(2,10); E12=Fr(V12)/dd12; v12=E12/Bs12
assert E12==4000 and v12==20000
e12=[(Fr(V12)/5/Bs12,'Levhalar arası uzaklığı santimetre cinsinden (5) yazmış: E = 200 ÷ 5 = 40 V/m, v = 40 ÷ 0,2 = 200 m/s.','islem'),
     (E12*0+ (Fr(V12)/dd12)*Bs12,'Hızı E·B olarak yazmış: v = 4000 · 0,2 = 800 m/s.','bilgi'),
     (Fr(V12)/Bs12,'Gerilimi elektrik alan sanıp levha aralığını hesaba katmamış: v = 200 ÷ 0,2 = 1000 m/s.','dikkat'),
     (E12/Bs12**2,'v = E ÷ B² yazmış: v = 4000 ÷ 0,04 = 100000 m/s.','bilgi')]
assert [c[0] for c in e12]==[200,800,1000,100000]
body='\\draw[very thick] (0,2.4) -- (5,2.4); \\draw[very thick] (0,0) -- (5,0); \\node[font=\\small,above] at (2.5,2.45) {$+$}; \\node[font=\\small,below] at (2.5,-.05) {$-$};\n'
body+='\\draw (0,2.4) -- (-.9,2.4) -- (-.9,1.5); \\draw[very thick] (-1.25,1.5) -- (-.55,1.5); \\draw[very thick] (-1.05,1.15) -- (-.75,1.15); \\draw (-.9,1.15) -- (-.9,0) -- (0,0);\n'
body+='\\node[font=\\small,anchor=east] at (-1.35,1.3) {$V=200$ V};\n'
body+=''.join(ici(x,y,.15,MAV) for x in (1.3,2.5,3.7) for y in (.55,1.85))
body+='\\draw[thick,fill=white] (.5,1.2) circle (.15); \\node[font=\\scriptsize] at (.5,1.2) {$q$}; \\draw[dashed,gray] (.65,1.2) -- (1.0,1.2); '+vk(1.0,1.2,4.9,1.2,'black','thick')+'\n'
body+='\\draw[<->] (5.4,0) -- (5.4,2.4); \\node[font=\\small,right] at (5.45,1.0) {$d=5$ cm}; \\node[font=\\small,'+MAV+',right] at (5.45,1.7) {$B=0{,}2$ T};\n'
body+=legend(-1.2,-.9)
SK=fig(body)
q('0012',tipId='mn-yuklu',tip='Yüklü parçacığın manyetik alandaki hareketi',z='orta',alt='Hız Seçici',kaz='Elektrik ve manyetik alanın birlikte bulunduğu bölgede doğrusal giden parçacığın hızını bulur.',
 kart='K-AFMANYETIK-12 (V=200 V, d=5 cm, B=0,2 T)',kalip='şekilli',
 metin='Paralel iki iletken levha arasındaki bölgede, levhalara paralel ve sayfaya içeri doğru yönelmiş düzgün bir manyetik alan vardır. Levhalara şekildeki gibi bir üretecin bağlanmasıyla aralarında düzgün bir elektrik alan oluşmuştur. Levhalara paralel olarak giren yüklü bir parçacık bu bölgede doğrusal yörünge izlemektedir. Kütle çekim etkisi önemsizdir.\nBuna göre, parçacığın hızının büyüklüğü kaç m/s’dir?',
 dogru=v12,yan=sec(v12,e12,'D'),istenen='Parçacığın hızının büyüklüğü (m/s).',ip=['Doğrusal giden parçacığa etkiyen kuvvetlerin bileşkesi hakkında ne söylenebilir?'],bilgi=[BSEL,BQ],sekil=SK,
 ad=[A('Elektrik alanı bul','Düzgün alan E = V ÷ d.','E = 200 ÷ 0,05 = 4000 V/m'),
     A('Kuvvetleri eşitle','Doğrusal harekette elektrik ve manyetik kuvvetler dengelenir.','q·E = q·v·B'),
     A('Hızı çöz','Yük sadeleşir.','v = E ÷ B = 4000 ÷ 0,2'),
     A('Sonucu yaz','Hız büyüklüğü.','v = 20000 m/s')],
 puf='Doğrusal gidiş, elektrik ve manyetik kuvvetin eşit büyüklükte olduğunu gösterir.')

# ================= 13 orta · proton ve alfa (öncüllü) =================
mp,qp=1,1; ma,qa=4,2
rK13=Fr(14,10); rL13=Fr(28,10)
assert Fr(ma,qa)/Fr(mp,qp)==2 and Fr(ma,qa)==2 and Fr(qa,qp)==2
# r = m v/(q B): α yörüngesi protonunkinin 2 katı (L). T = 2πm/(qB): α 2 kat. F = qvB: α 2 kat.
cand=[(x,y) for x in (.3,1.1,1.9,2.7,3.5,4.3,5.1) for y in (.6,1.5,2.4,3.3)]
def dyay(r): return [(r+r*math.cos(math.radians(a)),r*math.sin(math.radians(a))) for a in range(0,181,6)]
segs=[]
for r in (1.4,2.8):
    pp=dyay(r); segs+=list(zip(pp,pp[1:]))
fr=[p for p in serbest(cand,segs,mind=.5,pts_ex=[(1.4,1.7),(2.8,3.1)]) if p[1]>.3 and p[0]>.0 and p[0]<5.9]
body='\\draw[gray,thin] (-.6,0) -- (6.2,0);\n'+''.join(cik(x,y,.15,MAV) for x,y in fr)+'\n'
body+=f'\\draw[very thick,{KIR}] (0,0) arc (180:0:1.4); \\draw[very thick,{MAV}] (0,0) arc (180:0:2.8);\n'
body+='\\node[font=\\small,'+KIR+'] at (1.4,1.7) {K}; \\node[font=\\small,'+MAV+'] at (2.8,3.1) {L};\n'
body+=vk(0,-1.0,0,-.15,'black','very thick')+'\\node[font=\\small,left] at (-.05,-.7) {$\\vec v$}; \\fill (0,0) circle (.07); \\node[font=\\small,below left] at (0,0) {O};\n'
body+=legend(-.4,-1.7)+' \\node[font=\\small,'+MAV+',right] at (3.3,-1.0) {$\\vec B$ dışarı};'
SK=fig(body)
oncq('0013','E',
 'Sayfa düzlemine dik ve dışarı doğru yönelmiş düzgün bir manyetik alanın bulunduğu bölgeye, proton ve alfa parçacığı (helyum çekirdeği; kütlesi protonun 4 katı, yükü 2 katı) O noktasından sayfa düzleminde yukarı doğru ve aynı büyüklükte hızla ayrı ayrı giriyor. Parçacıklar şekildeki K ve L yarım çemberlerini çizmektedir. Başka kuvvetler önemsizdir.',
 {'I':('Alfa parçacığı L yörüngesini izlemiştir.',True,'r = m·v ÷ (q·B) olduğundan alfa parçacığının yarıçapı (4m ÷ 2q) protonunkinin 2 katıdır; büyük yarıçaplı yörünge L’dir'),
  'II':('Alfa parçacığı yarım çemberi, protondan daha kısa sürede tamamlar.',False,'yarım turun süresi π·m ÷ (q·B) ile orantılıdır; alfa için m ÷ q değeri protonunkinin 2 katı olduğundan süre 2 kat uzundur'),
  'III':('Alfa parçacığına etkiyen manyetik kuvvetin büyüklüğü, protona etkiyenin 2 katıdır.',True,'F = q·v·B olup hız ve alan aynı, yük 2 katı olduğundan kuvvet 2 katıdır')},
 tipId='mn-cember',tip='Yüklü parçacığın çembersel hareketi',z='orta',alt='Çembersel Yörünge',kaz='Manyetik alanda çembersel hareket yapan parçacıkların yarıçap, periyot ve kuvvet büyüklüklerini kütle ve yük oranlarıyla karşılaştırır.',
 kart='K-AFMANYETIK-13 (proton ve alfa, aynı v)',kalip='öncüllü',ip=['Yarıçap, süre ve kuvvet bağıntılarını kütle ve yük cinsinden yazıp oranları karşılaştır.'],bilgi=[BR,BQ],sekil=SK,
 puf='Yarıçap ve periyot bağıntılarını kütle ile yük cinsinden yaz.')

# ================= 14 orta · eğri telde net kuvvet =================
a14,b14=Fr(3,10),Fr(4,10); B14,i14=Fr(2,10),4
Le=Fr(int(math.hypot(3,4)),10); assert Le==Fr(1,2) and a14**2+b14**2==Le**2
F14=B14*i14*Le; assert F14==Fr(2,5)
Fh=B14*i14*a14; Fv=B14*i14*b14; assert Fh**2+Fv**2==F14**2
e14=[(B14*i14*(a14+b14),'Telin toplam uzunluğunu (0,3 + 0,4 = 0,7 m) kullanmış: F = 0,2·4·0,7 = 0,56 N.','dikkat'),
     (B14*i14*b14,'Yalnız dik kenarı (0,4 m) hesaba katmış: F = 0,2·4·0,4 = 0,32 N.','dikkat'),
     (B14*i14*a14,'Yalnız yatay kenarı (0,3 m) hesaba katmış: F = 0,2·4·0,3 = 0,24 N.','dikkat'),
     (B14*i14*(b14-a14),'Dik iki kuvveti zıt yönlü sanıp skaler çıkarmış: 0,32 − 0,24 = 0,08 N (= 0,2·4·0,1).','islem')]
assert [c[0] for c in e14]==[Fr(56,100),Fr(32,100),Fr(24,100),Fr(8,100)]
wr=[((0,0),(3,0)),((3,0),(3,4))]
cand=[(x,y) for x in (.7,1.9,4.2,5.2) for y in (.8,1.9,3.0,4.0)]
fr=[p for p in serbest(cand,wr,mind=.5) if math.hypot(p[0]-3.6,p[1]-1.0)>.8]
body=''.join(cik(x,y,.15,MAV) for x,y in fr)+'\n'
body+='\\draw[very thick] (0,0) -- (3,0) -- (3,4); '+vk(1.2,0,1.6,0,'black','very thick')+vk(3,1.7,3,2.1,'black','very thick')+'\n'
body+='\\node[font=\\small,below left] at (0,0) {A}; \\node[font=\\small,below right] at (3,0) {B}; \\node[font=\\small,above right] at (3,4) {C};\n'
body+='\\node[font=\\small,below] at (1.5,-.45) {30 cm}; \\node[font=\\small,right] at (3.1,.9) {40 cm}; \\node[font=\\small,above left] at (.3,.35) {$i=4$ A};\n'
body+='\\node[font=\\small,'+MAV+',right] at (3.9,4.85) {$B=0{,}2$ T}; '+legend(-.3,-1.4)
SK=fig(body)
q('0014',tipId='mn-kuvvet',tip='Akım taşıyan tele etkiyen kuvvet',z='orta',alt='Tele Etkiyen Manyetik Kuvvet',kaz='Düzgün manyetik alandaki eğri telin tamamına etkiyen net kuvvetin büyüklüğünü uç noktalar arasındaki uzaklıktan bulur.',
 kart='K-AFMANYETIK-14 (A–B 30 cm, B–C 40 cm, B=0,2 T, i=4 A)',kalip='şekilli',
 metin='Sayfa düzleminde, birbirine dik iki doğrusal parçadan oluşan ABC telinden şekildeki yönde i akımı geçmektedir. Tel, sayfadan dışarı doğru yönelmiş düzgün bir manyetik alan içindedir; parça uzunlukları, alan ve akım şekilde verilmiştir.\nBuna göre, telin tamamına etkiyen net manyetik kuvvetin büyüklüğü kaç N’dur?',
 dogru=F14,yan=sec(F14,e14,'D'),istenen='Telin tamamına etkiyen net manyetik kuvvetin büyüklüğü (N).',ip=['Her parçaya etkiyen kuvvetin yönünü belirle; sonuçların nasıl birleştiğini düşün.'],bilgi=[BFT,BTELB],sekil=SK,
 ad=[A('Parçalara etkiyen kuvvetleri bul','AB’ye aşağı, BC’ye sağa doğru kuvvet etkir (birbirine dik).','F₁ = 0,2·4·0,3 = 0,24 N, F₂ = 0,2·4·0,4 = 0,32 N'),
     A('Bileşkeyi bul','Dik iki kuvvet Pisagor ile birleşir.','F = √(0,24² + 0,32²) = 0,4 N'),
     A('Kısa yoldan doğrula','Etkin uzunluk AC doğru parçasıdır: √(0,3² + 0,4²) = 0,5 m.','F = 0,2 · 4 · 0,5 = 0,4 N')],
 puf='Her parçanın kuvvetini ayrı yönüyle bul.')

# ================= 15 zor · kütle spektrometresi =================
E15,B1,B2,m15,q15=2000,Fr(5,10),Fr(2,10),Fr(2,10**11),Fr(2,10**6)
v15=E15/B1; r15=m15*v15/(q15*B2); x15=2*r15*100
assert v15==4000 and r15==Fr(1,5) and x15==40
e15=[(r15*100,'Vuruş noktasını girişten r kadar uzakta sanmış (yarım çemberin çapı 2r olduğunu unutmuş): x = 20 cm.','dikkat'),
     (2*m15*(E15*B1)/(q15*B2)*100,'Hızı E·B = 1000 m/s almış: r = 2×10⁻¹¹·1000 ÷ (2×10⁻⁶·0,2) = 0,05 m, x = 2r = 10 cm.','bilgi'),
     (2*m15*v15/(q15*B1)*100,'Yarıçapta B₂ yerine B₁’i (0,5 T) kullanmış: r = 0,08 m, x = 16 cm.','islem'),
     (2*m15*(E15/B2)/(q15*B2)*100,'Hızı E ÷ B₂ = 10000 m/s almış (seçicinin alanını yanlış kullanmış): r = 0,5 m, x = 100 cm.','islem')]
assert [c[0] for c in e15]==[20,10,16,100]
r_=2.2; xs=.8
pp=[(xs+r_+r_*math.cos(math.radians(a)),3+r_*math.sin(math.radians(a))) for a in range(0,181,6)]
segsA=list(zip(pp,pp[1:]))+[((.8,3.4),(5.2,3.4))]
cand=[(x,y) for x in (1.6,2.6,3.6,4.6,5.6,6.4) for y in (3.7,4.4,5.1)]
fr=serbest(cand,segsA,mind=.5)
fr=[p for p in fr if not (abs(math.hypot(p[0]-(xs+r_),p[1]-3)-r_)<.5) and math.hypot(p[0]-6.3,p[1]-4.7)>1.3]
body='\\draw[very thick] (0,0) -- (0,3.0); \\draw[very thick] (1.6,0) -- (1.6,3.0); \\node[font=\\small,below] at (0,0) {$+$}; \\node[font=\\small,below] at (1.6,0) {$-$};\n'
body+=''.join(ici(x,y,.15,MAV) for x in (.4,1.2) for y in (.6,1.5,2.4))
body+='\\draw[very thick] (-.8,3.0) -- (.55,3.0); \\draw[very thick] (1.05,3.0) -- (7,3.0);\n'
body+=vk(.8,-.9,.8,2.0,'black','thick')+f'\\draw[very thick,{ARR}] (.8,2.0) -- (.8,3.0); \\draw[very thick,{ARR}] (.8,3.0) arc (180:0:2.2);\n'
body+=''.join(cik(x,y,.15,MAV) for x,y in fr)
body+='\\draw[<->] (.8,3.4) -- (5.2,3.4); \\node[font=\\small,above] at (3.0,3.4) {$x$}; \\draw[very thick,'+KIR+'] (5.2,2.85) -- (5.2,3.15);\n'
body+='\\node[font=\\small,anchor=east] at (-.3,1.5) {$E=2000$ N/C}; \\node[font=\\small,anchor=west] at (1.75,1.5) {$B_1=0{,}5$ T}; \\node[font=\\small,anchor=west,'+MAV+'] at (5.4,4.7) {$B_2=0{,}2$ T};\n'
body+=legend(-.8,-1.6)
SK=fig(body)
q('0015',tipId='mn-cember',tip='Yüklü parçacığın çembersel hareketi',z='zor',alt='Kütle Spektrometresi',kaz='Hız seçici ve çembersel yörüngeyi birleştirerek parçacığın ikinci alan bölgesindeki vuruş noktasını hesaplar.',
 kart='K-AFMANYETIK-15 (E=2000, B1=0,5, B2=0,2; m=2×10⁻¹¹ kg, q=2 μC)',kalip='şekilli',
 metin='Şekildeki düzenekte, levhalar arasında birbirine dik düzgün E elektrik alanı ile içeri doğru B₁ manyetik alanı vardır. Kütlesi 2×10⁻¹¹ kg, yükü +2 μC (2×10⁻⁶ C) olan bir parçacık, levhalar arasından doğrusal giderek yatay duvardaki aralıktan çıkıyor ve duvarın üstünde, dışarı doğru yönelmiş B₂ alanının bulunduğu bölgede yarım çember çizerek duvara çarpıyor. Alanlar şekilde verilmiştir; kütle çekim etkisi önemsizdir.\nBuna göre, parçacığın duvardaki aralıktan çarpma noktasına olan uzaklığı x kaç cm’dir?',
 dogru=x15,yan=sec(x15,e15,'D'),istenen='Çarpma noktasının aralığa uzaklığı x (cm).',ip=['Levhalar arasında parçacığın doğrusal gitmesinin hangi koşulu verdiğini düşün; duvarın üstündeki bölgede ise yalnız B₂ etkilidir.'],bilgi=[BSEL,BR],sekil=SK,
 ad=[A('Hızı bul','Levhalar arasında doğrusal gidiş: q·E = q·v·B₁.','v = 2000 ÷ 0,5 = 4000 m/s'),
     A('Yarıçapı yaz','B₂ bölgesinde q·v·B₂ = m·v² ÷ r.','r = m·v ÷ (q·B₂) = 2×10⁻¹¹ · 4000 ÷ (2×10⁻⁶ · 0,2)'),
     A('Yarıçapı hesapla','Sayıları yerine koy.','r = 0,2 m = 20 cm'),
     A('Uzaklığı bul','Yarım çember çizdiğinden çarpma noktası aralıktan 2r uzaktadır.','x = 2r = 40 cm')],
 puf='Seçici bölgede hangi iki kuvvetin dengelendiğini düşün.')

# ================= 16 zor · eğik düzlemde dengedeki çubuk =================
m16,L16,B16,tan37=Fr(80,1000),Fr(1,2),Fr(4,10),Fr(3,4)
sin_,cos_=Fr(6,10),Fr(8,10); assert sin_/cos_==tan37
i16=m16*g*tan37/(B16*L16); assert i16==3
# kuvvet yönü: B yukarı (+y), akım içeri (−z): F = I l × B = (−z)×(+y) = +x → yatay, eğimin yukarısına doğru
assert kuvvet_xy((0,0,-1),(0,1,0))[:2]==(1,0)
e16=[(m16*g*sin_/(B16*L16),'Manyetik kuvveti eğim boyunca saymış: B·i·L = m·g·sin37° → i = 0,8·0,6 ÷ 0,2 = 2,4 A.','islem'),
     (m16*g*cos_/(B16*L16),'Ağırlığın bileşenlerini ters yazmış: B·i·L = m·g·cos37° → i = 0,8·0,8 ÷ 0,2 = 3,2 A.','islem'),
     (m16*g/(B16*L16),'Dengeyi düşeyde kurmuş (B·i·L = m·g): i = 0,8 ÷ 0,2 = 4 A.','dikkat'),
     (m16*g*tan37/B16,'Telin uzunluğunu (0,5 m) formüle katmamış: i = 0,6 ÷ 0,4 = 1,5 A.','dikkat')]
assert [c[0] for c in e16]==[Fr(12,5),Fr(16,5),4,Fr(3,2)]
sx=3.0; sy=sx*.75; cx,cy=sx-.18,sy+.24
body='\\fill[gray!25] (0,0) -- (6,0) -- (6,4.5) -- cycle; \\draw[very thick] (0,0) -- (6,0) -- (6,4.5) -- cycle; \\draw (1.2,0) arc (0:37:1.2); \\node[font=\\small] at (1.65,.36) {$37^\\circ$};\n'
body+=f'\\draw[thick,fill=white] ({cx:.2f},{cy:.2f}) circle (.3); '+ici(cx,cy,.3)+'\n'
for x in (.9,4.5,5.4): body+=vk(x,x*.75+.25,x,x*.75+1.75,MAV,'thick')+'\n'
body+='\\node[font=\\small,'+MAV+',anchor=west] at (1.3,3.3) {$B=0{,}4$ T}; \\node[font=\\small,above] at (3.05,.0) {}; '+legend(0,-.8)
SK=fig(body)
q('0016',tipId='mn-kuvvet',tip='Akım taşıyan tele etkiyen kuvvet',z='zor',alt='Tele Etkiyen Manyetik Kuvvet',kaz='Düzgün manyetik alanda eğik düzlem üzerinde dengede kalan akımlı çubuğun akım şiddetini denge koşullarından bulur.',
 kart='K-AFMANYETIK-16 (37° eğim, düşey B=0,4 T, m=80 g, L=0,5 m)',kalip='şekilli',
 metin='Sürtünmesiz, 37° eğimli bir eğik düzlem üzerinde, sayfa düzlemine dik doğrultuda yatay duran 80 g kütleli, 0,5 m uzunluğundaki iletken bir çubuk bulunmaktadır. Düzlem, düşey ve yukarı yönlü düzgün bir manyetik alan içindedir. Çubuktan sayfaya içeri doğru sabit bir i akımı geçirildiğinde çubuk eğik düzlem üzerinde dengede kalmaktadır.\n(g = 10 m/s²; sin37° = 0,6; cos37° = 0,8; B şekilde verilmiştir)\nBuna göre, çubuktan geçen akım kaç A’dir?',
 dogru=i16,yan=sec(i16,e16,'C'),istenen='Çubuktan geçen akım şiddeti (A).',ip=['Manyetik kuvvetin doğrultusunu belirleyip ağırlıkla birlikte eğim doğrultusundaki bileşenlerini karşılaştır.'],bilgi=[BFT,BDEN],sekil=SK,
 ad=[A('Manyetik kuvvetin yönünü bul','Akım içeri, B yukarı: sağ el kuralıyla kuvvet yatay ve eğimin yukarısına doğrudur.','F yatay, F = B·i·L'),
     A('Eğim doğrultusunda dengeyi yaz','Yatay kuvvetin eğim boyunca bileşeni, ağırlığın bileşenine eşittir.','F·cos37° = m·g·sin37° → F = m·g·tan37°'),
     A('Kuvveti hesapla','Sayıları yerine koy.','F = 0,08 · 10 · 0,75 = 0,6 N'),
     A('Akımı bul','F = B·i·L.','i = 0,6 ÷ (0,4 · 0,5) = 3 A')],
 puf='Dengeyi eğim doğrultusunda kurmak için kuvvetlerin bileşenlerini ayrı ayrı düşün.')

# ================= 17 zor · düz tel + halka, merkezde sıfır alan =================
I17=30; rr=Fr(1,10)    # r değeri sadeleşir
mu0=12*Fr(1,10**7)
Bw=Fr(2,10**7)*I17/rr; i17=Bw*2*rr/mu0
assert i17==10 and Btel((0,0),1,1,(Fr(3,2),0))[1]>0  # tel yukarı akım: merkezde içeri; halka saat yönünün tersi: dışarı
wire_up=kuvvet_xy((0,1,0),(1,0,0))   # l × r̂ → alan: y × x = −z (içeri)
assert wire_up[2]==-1
e17=[(Fr(I17),'Düz telin alanını halka formülüyle (μ₀·i ÷ 2r) yazmış; iki alanı eşitleyince akımı telinkine (30 A) eşit bulmuş.','bilgi'),
     (Fr(5),'Halkanın merkezindeki alanı μ₀·i ÷ r almış (2’yi atlamış): 2×10⁻⁷·30 = 12×10⁻⁷·i₂ → i₂ = 5 A.','islem'),
     (Fr(20),'Düz telin alanını μ₀·i ÷ (π·r) yazmış (2 çarpanını atlamış): 4×10⁻⁷·30 = 6×10⁻⁷·i₂ → i₂ = 20 A.','islem'),
     (Fr(90),'Oranı ters yazmış: 2×10⁻⁷·i₂ = 6×10⁻⁷·30 → i₂ = 90 A.','islem')]
assert Fr(2,10**7)*30/Fr(12,10**7)==5 and Fr(4,10**7)*30/Fr(6,10**7)==20 and Fr(6,10**7)*30/Fr(2,10**7)==90 and Fr(6,10**7)*30/Fr(6,10**7)==30
body='\\draw[very thick] (0,-2.8) -- (0,2.8); '+vk(0,1.8,0,2.8,'black','very thick')+' \\node[font=\\small,left] at (-.1,2.4) {$i_1=30$ A};\n'
body+='\\draw[very thick] (1.5,0) circle (1.5); \\draw[very thick,'+ARR+'] (2.99,.3) arc (11:35:1.5); \\draw[very thick,'+ARR+'] (.01,-.3) arc (191:215:1.5);\n'
body+='\\fill (1.5,0) circle (.07); \\node[font=\\small,above right] at (1.5,0) {O}; \\draw[dashed,gray] (0,0) -- (1.5,0); \\node[font=\\small,below] at (.8,-.02) {$r$}; \\node[font=\\small,right] at (3.1,.9) {$i_2$};\n'
body+='\\node[font=\\small,anchor=west] at (3.3,-1.2) {halka: saat}; \\node[font=\\small,anchor=west] at (3.3,-1.65) {yönünün tersi};\n'
SK=fig(body)
q('0017',tipId='mn-halka',tip='Halka ve bobinin alanı',z='zor',alt='Halka ve Bobin',kaz='Düz telin ve çembersel halkanın merkezde oluşturduğu zıt yönlü alanları eşitleyerek akımı hesaplar.',
 kart='K-AFMANYETIK-17 (düz tel 30 A, halka teğet, B=0)',kalip='şekilli',
 metin='Sayfa düzleminde bulunan, yarıçapı r olan çembersel bir halka ile sayfa düzleminde uzanan çok uzun düz bir tel, halkaya şekildeki gibi teğet ve birbirine değmeden (yalıtkan kaplı) yerleştirilmiştir. Düz telden i₁ = 30 A akım şekildeki yönde geçmektedir. Halkadan geçen i₂ akımı saat yönünün tersinedir ve halkanın O merkezindeki bileşke manyetik alan sıfırdır.\n(μ₀ = 4π×10⁻⁷ T·m/A ve π = 3 alınız.)\nBuna göre, i₂ akımı kaç A’dir?',
 dogru=i17,yan=sec(i17,e17,'B'),istenen='Halkadan geçen i₂ akımı (A).',ip=['Telin ve halkanın O’da oluşturduğu alanların yönlerini sağ el kuralıyla bul; sıfır bileşke ne demek?'],bilgi=[BTEL,BHAL],sekil=SK,
 ad=[A('Yönleri bul','Yukarı akımlı telin sağındaki O’da alan içeri; saat yönünün tersindeki halkanın merkezinde alan dışarı yönlüdür.','Alanlar zıt yönlü → birbirini götürebilir'),
     A('Düz telin alanı','Telin O’ya uzaklığı r’dir: B₁ = 2×10⁻⁷·i₁ ÷ r.','B₁ = 2×10⁻⁷·30 ÷ r = 6×10⁻⁶ ÷ r'),
     A('Halkanın alanı','B₂ = μ₀·i₂ ÷ 2r, μ₀ = 12×10⁻⁷.','B₂ = 6×10⁻⁷·i₂ ÷ r'),
     A('Eşitle','B₁ = B₂.','i₂ = 6×10⁻⁶ ÷ 6×10⁻⁷ = 10 A')],
 puf='Bileşke alanın sıfır olması için zıt yönlü iki alanın büyüklükleri eşit olmalıdır.')

# ================= 18 zor · üç telin net kuvveti =================
Ix,Iy,Iz,dd=10,15,20,Fr(1,10); L18=2
def kuv(ap,sa,Ia,bp,sb,Ib):
    Bv=Btel(bp,sb,Ib,ap); return kuvvet_xy((0,0,sa),(Bv[0],Bv[1],0),Ia)
FYv=kuvvet_xy((0,0,1),(*Btel((3,0),+1,Iy,(0,0)),0),Ix); FZv=kuvvet_xy((0,0,1),(*Btel((0,3),-1,Iz,(0,0)),0),Ix)
assert FYv[0]>0 and FYv[1]==0 and FZv[0]==0 and FZv[1]<0 and FYv[0]/(-FZv[1])==Fr(3,4)
Fy=Fr(2,10**7)*Ix*Iy/dd*L18; Fz=Fr(2,10**7)*Ix*Iz/dd*L18
assert Fy==Fr(6,10**4) and Fz==Fr(8,10**4) and Fy**2+Fz**2==Fr(1,10**3)**2
net18='1 mN, ↘'
sira18=['1 mN, ↗','1 mN, ↘','1 mN, ↙','1 mN, ↖','1,4 mN, ↘']
assert (Fy+Fz)==Fr(14,10**4)*1  and (Fy+Fz)*1000==Fr(14,10)
body=cik(0,0,.24)+' \\node[font=\\small,below left] at (-.1,-.15) {X, $10$ A}; '+cik(3,0,.24)+' \\node[font=\\small,below right] at (3.1,-.15) {Y, $15$ A}; '+ici(0,3,.24)+' \\node[font=\\small,above left] at (-.1,3.15) {Z, $20$ A};\n'
body+='\\draw[dashed,gray] (0,0) -- (3,0); \\draw[dashed,gray] (0,0) -- (0,3); \\draw (.28,0) -- (.28,.28) -- (0,.28);\n'
body+='\\draw[<->] (0,-1.0) -- (3,-1.0); \\node[font=\\small,below] at (1.5,-1.0) {10 cm}; \\draw[<->] (-1.3,0) -- (-1.3,3); \\node[font=\\small,left] at (-1.3,1.5) {10 cm};\n'
body+=legend(-1.4,-2.2)
SK=fig(body)
q('0018',tipId='mn-paralel',tip='Paralel akımlı teller',z='zor',alt='Paralel Akımlı Teller',kaz='Üç paralel telde bir tele etkiyen net kuvvetin büyüklüğünü ve yönünü, çekme–itme etkilerini vektörel birleştirerek bulur.',
 kart='K-AFMANYETIK-18 (X ⊙ 10 A, Y ⊙ 15 A, Z ⊗ 20 A; 10 cm dik)',kalip='şekilli',
 metin='Sayfa düzlemine dik, çok uzun ve sabit X, Y ve Z telleri şekildeki konumlardadır. X ve Y’den sayfadan dışarı, Z’den sayfaya içeri doğru akımlar geçmektedir; X, Y’nin ve X, Z’nin arasındaki uzaklıklar 10 cm’dir. Akım şiddetleri şekilde verilmiştir.\n(μ₀ ÷ 2π = 2×10⁻⁷ T·m/A alınız; yön olarak sayfa düzleminde sağ, yukarı gibi yönler kullanılacaktır.)\nBuna göre, X telinin 2 m’lik kısmına etkiyen net manyetik kuvvetin büyüklüğü ve yönü aşağıdakilerden hangisidir?',
 dogru=net18,yan=[('1 mN, ↗','Y’nin X’i çektiğini, Z’nin de X’i çektiğini sanmış: zıt yönlü akımların birbirini ittiğini hesaba katmamış; kuvvetler sağa 0,6 mN ve yukarı 0,8 mN olduğundan 1 mN, ↗.','bilgi'),
  ('1 mN, ↙','Her iki telin de X’i ittiğini düşünmüş: aynı yönlü akımların çektiğini unutmuş; kuvvetler sola 0,6 mN ve aşağı 0,8 mN olduğundan 1 mN, ↙.','bilgi'),
  ('1 mN, ↖','Y’nin X’i ittiğini, Z’nin ise çektiğini sanmış (çekme–itmeyi ters yorumlamış); kuvvetler sola 0,6 mN ve yukarı 0,8 mN olduğundan 1 mN, ↖.','bilgi'),
  ('1,4 mN, ↘','Yönü doğru bulmuş, ancak dik iki kuvveti skaler toplamış: 0,6 + 0,8 = 1,4 mN; oysa dik kuvvetler Pisagor ile birleşir.','islem')],
 sira=sira18,istenen='X teline etkiyen net kuvvetin büyüklüğü ve yönü.',ip=['Y ve Z’nin X’e uyguladığı kuvvetlerin yönlerini aynı/zıt yönlü akım ilişkisinden belirle.'],bilgi=[BPAR,BTOP],sekil=SK,
 ad=[A('Y’nin etkisini bul','Aynı yönlü akımlar çeker: kuvvet Y’ye doğru (sağa).','F₁ = 2×10⁻⁷·10·15 ÷ 0,1·2 = 6×10⁻⁴ N'),
     A('Z’nin etkisini bul','Zıt yönlü akımlar iter: kuvvet Z’den uzağa (aşağı).','F₂ = 2×10⁻⁷·10·20 ÷ 0,1·2 = 8×10⁻⁴ N'),
     A('Bileşkeyi bul','Dik iki kuvvet Pisagor ile birleşir.','F = √(0,6² + 0,8²) = 1 mN'),
     A('Yönü yaz','Bileşke sağa ve aşağıya doğrudur.','1 mN, ↘')],
 puf='Her telin X’e uyguladığı kuvveti ayrı ayrı bul.')

# ================= 19 zor · alan bölgesinden sapma =================
dK,dL=Fr(1),Fr(1); sK,sL=Fr(1,2),Fr(8,10)
rK=dK/sK; rL=dL/sL; ratio=rK/rL
assert rK==2 and rL==Fr(5,4) and ratio==Fr(8,5)
e19=[(Fr(5,8),'Yarıçapı r = d·sinθ yazmış: r_K = 0,5d, r_L = 0,8d ve oran 0,5 ÷ 0,8 = 0,625.','islem'),
     (rK-rL,'Yarıçapları oranlamak yerine çıkarmış: 2d − 1,25d = 0,75d, yani 0,75.','islem'),
     (rK/(dL/Fr(6,10)),'L’nin sapma açısını 37° (53°’nin tümleyeni) almış: r_L = d ÷ 0,6, oran 2 ÷ (5/3) = 1,2.','dikkat'),
     (ratio**2,'Yarıçapı kütlenin karesiyle orantılı sanmış: (1,6)² = 2,56.','bilgi')]
assert rK/(dL/Fr(6,10))==Fr(6,5)
assert [c[0] for c in e19]==[Fr(5,8),Fr(3,4),Fr(6,5),Fr(64,25)]
def sapma(y0,th,etiket,col):
    r=1/math.sin(math.radians(th))*2.4; dx=2.4
    ex=dx; ey=y0+r*(1-math.cos(math.radians(th)))
    s=f'\\draw[very thick,{col}] (-1.2,{y0}) -- (0,{y0}); \\draw[very thick,{col},{ARR}] (0,{y0}) arc (-90:{-90+th}:{r:.3f});'
    # çıkış doğrusu (teğet) ve yatay kılavuz
    tx,ty=math.cos(math.radians(th)),math.sin(math.radians(th))
    s+=f'\\draw[dashed,{col}] ({ex:.3f},{ey:.3f}) -- ({ex+1.6*tx:.3f},{ey+1.6*ty:.3f}); \\draw[dashed,gray] ({ex:.3f},{ey:.3f}) -- ({ex+1.8:.3f},{ey:.3f});'
    s+=f'\\draw ({ex+1.0:.3f},{ey:.3f}) arc (0:{th}:1.0); \\node[font=\\small] at ({ex+1.4*math.cos(math.radians(th/2)):.3f},{ey+1.4*math.sin(math.radians(th/2))+.0:.3f}) {{${etiket}^\\circ$}};'
    return s,ey
sK_,eyK=sapma(3.4,30,30,KIR); sL_,eyL=sapma(.8,53,53,MAV)
fr=[(.8,2.4),(1.6,2.4),(.8,4.7),(1.6,4.7),(1.2,0.1),(1.2,5.4)]
body='\\draw[gray,thin] (0,-.4) rectangle (2.4,5.7); \\draw[gray,thin] (0,-.4) -- (0,5.7);\n'+''.join(cik(x,y,.15,MAV) for x,y in fr)+'\n'+sK_+sL_+'\n'
body+='\\node[font=\\small,above] at (-.8,3.4) {K}; \\node[font=\\small,above] at (-.8,.8) {L}; \\draw[<->] (0,5.95) -- (2.4,5.95); \\node[font=\\small,above] at (1.2,5.95) {$d$};\n'
body+=legend(-1.4,-1.1)+' \\node[font=\\small,'+MAV+',right] at (-1.4,-1.7) {$\\vec B$ dışarı};'
SK=fig(body)
q('0019',tipId='mn-cember',tip='Yüklü parçacığın çembersel hareketi',z='zor',alt='Çembersel Yörünge',kaz='Manyetik alan bölgesinden sapma açılarını yarıçaplarla ilişkilendirip kütle oranını bulur.',
 kart='K-AFMANYETIK-19 (d, sapma 30° ve 53°, eşit q, v, B)',kalip='şekilli',
 metin='Genişliği d olan, sayfa düzlemine dik ve dışarı doğru yönelmiş düzgün bir manyetik alan bölgesine eşit büyüklükte hız ve eşit büyüklükte yüke sahip K ve L parçacıkları, bölgenin sınırına dik olarak giriyor. Parçacıklar bölgeyi, ilk doğrultularına göre şekilde gösterilen açılar kadar sapmış olarak terk ediyor. Alan dışında kuvvet yoktur.\n(sin30° = 0,5; sin53° = 0,8)\nBuna göre, K’nin kütlesinin L’nin kütlesine oranı m_K ÷ m_L kaçtır?',
 dogru=ratio,yan=sec(ratio,e19,'D'),istenen='Kütle oranı m_K ÷ m_L.',ip=['Sapma açısı ile yarıçap ve bölge genişliği arasındaki geometrik ilişkiyi çiz.'],bilgi=[BR,BQ],sekil=SK,
 ad=[A('Geometriyi kur','Giriş doğrultusuna dik yarıçap çizilince sınırdan çıkış anında sinθ = d ÷ r olur.','r = d ÷ sinθ'),
     A('Yarıçapları bul','Açılar 30° ve 53°.','r_K = d ÷ 0,5 = 2d, r_L = d ÷ 0,8 = 1,25d'),
     A('Kütleyi yarıçapla ilişkilendir','r = m·v ÷ (q·B); q, v ve B eşit olduğundan m ∝ r.','m_K ÷ m_L = r_K ÷ r_L'),
     A('Oranı hesapla','Yarıçap oranı.','m_K ÷ m_L = 2 ÷ 1,25 = 1,6')],
 puf='Eşit yük, hız ve alan için kütle yarıçapla doğru orantılıdır.')

# ================= 20 zor · aynı gerilimle hızlanan parçacıklar =================
mK_,qK_,mL_,qL_=1,1,8,2
oran=Fr(mL_,qL_)/Fr(mK_,qK_)         # r ∝ √(m/q) → (r_L/r_K)² = 4
assert oran==4
import math as _m
rr20=_m.isqrt(int(oran)); assert rr20**2==oran and rr20==2
e20=[(Fr(oran),'Hızların eşit olduğunu düşünmüş: r = m·v ÷ (q·B) ile r_L ÷ r_K = (8m ÷ 2q) ÷ (m ÷ q) = 4.','bilgi'),
     (Fr(mL_,mK_),'Yarıçapı yalnız kütleyle orantılamış: r_L ÷ r_K = 8m ÷ m = 8.','dikkat'),
     (Fr(1,rr20),'Oranı ters yazmış: r_K ÷ r_L = 1 ÷ 2 = 0,5.','islem'),
     (Fr(1,4),'Hızları eşit kabul edip oranı ters yazmış: r_K ÷ r_L = (m ÷ q) ÷ (8m ÷ 2q) = 0,25.','islem')]
assert [c[0] for c in e20]==[4,8,Fr(1,2),Fr(1,4)]
def serit(y,lab,col):
    s=f'\\draw[very thick] (0,{y-.8}) -- (0,{y+.8}); \\draw[very thick] (.9,{y-.8}) -- (.9,{y+.8}); \\node[font=\\small,above] at (.45,{y+.8}) {{$V$}};\n'
    s+=f'\\draw[thick,fill=white] (-.45,{y}) circle (.28); \\node[font=\\small] at (-.45,{y}) {{{lab[0]}}}; \\node[font=\\small,anchor=east] at (-.8,{y}) {{{lab[1]}}};\n'
    s+=vk(.95,y,3.9,y,col,'very thick')
    return s
body='\\draw[gray,thin] (3.4,-1.0) rectangle (8.2,3.8);\n'+''.join(ici(x,y,.15,MAV) for x in (4.4,5.6,6.8,7.7) for y in (-.6,1.5,3.4))
body+=serit(2.8,('K','K: $m$, $q$'),'black'); body+=serit(.2,('L','L: $8m$, $2q$'),'black')
body+='\\node[font=\\small,'+MAV+',anchor=west] at (3.5,4.1) {$\\vec B$ içeri}; \\node[font=\\small,anchor=west] at (4.6,4.1) {$\\vec v\\perp\\vec B$}; '+legend(-1.0,-1.8)
SK=fig(body)
q('0020',tipId='mn-cember',tip='Yüklü parçacığın çembersel hareketi',z='orta',alt='Çembersel Yörünge',kaz='Aynı potansiyel farkıyla hızlandırılan parçacıkların manyetik alandaki yarıçaplarını kütle ve yük oranına bağlı olarak karşılaştırır.',
 kart='K-AFMANYETIK-20 (K: m,q ; L: 8m,2q ; aynı V)',kalip='şekilli',
 metin='Kütle ve yükleri şekilde verilen K ve L parçacıkları, durgun hâlden başlayarak aynı V potansiyel farkıyla ayrı ayrı hızlandırılıyor ve sayfa düzlemine dik, içeri doğru yönelmiş düzgün bir manyetik alan bölgesine alana dik olarak giriyor. Parçacıklar bu bölgede çembersel yörünge çiziyor. Kütle çekim ve sürtünme önemsizdir.\nBuna göre, L’nin yörünge yarıçapının K’ninkine oranı r_L ÷ r_K kaçtır?',
 dogru=Fr(2),yan=sec(Fr(2),e20,'C'),istenen='Yarıçap oranı r_L ÷ r_K.',ip=['Hızı, gerilimle kazanılan kinetik enerjiden bul; sonra yarıçap bağıntısına yaz.'],bilgi=[BHIZ,BR],sekil=SK,
 ad=[A('Hızı gerilimle ilişkilendir','Hızlanma: q·V = ½·m·v².','v = √(2qV ÷ m)'),
     A('Yarıçapa yaz','r = m·v ÷ (q·B) ifadesine v’yi koy.','r = (1 ÷ B)·√(2mV ÷ q) → r ∝ √(m ÷ q)'),
     A('Oranı hesapla','K için m ÷ q = m ÷ q, L için 8m ÷ 2q = 4·(m ÷ q).','r_L ÷ r_K = √4 = 2')],
 puf='Hızı önce gerilimden bul.')

# ---------- bitir ----------
for q_ in P.ANA: q_['kardes']=None
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/man/bos.json'
P.yaz(os.path.join(ADIR,'manyetik-1.json'),SCR)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Fizik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11. sınıf fizik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afmanyetik.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
