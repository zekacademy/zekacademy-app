"""Fonksiyonlar · parti 1: 8 ana + 8 kardeş. Her cevap kodla doğrulanır; grafik değerleri çizimle aynı noktalardan hesaplanır."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *

P=Parti('fonksiyon','Fonksiyonlar','matd|Fonksiyonlar')
TT=lambda **k:k
M=lambda v:(f'−{-v}' if v<0 else str(v))   # eksi işareti U+2212

def tek_dogru(siklar,sik,deger):
    S=dict(zip('ABCDE',siklar)); assert S[sik]==M(deger) and list(S.values()).count(M(deger))==1,(siklar,sik,deger)

# ---------- parçalı doğrusal grafik ----------
def pl(nok):
    """nok: [(x, y), …] köşe noktaları → x’te değer veren fonksiyon (Fraction)."""
    def f(x):
        x=Fr(x)
        for (x1,y1),(x2,y2) in zip(nok,nok[1:]):
            if x1<=x<=x2: return Fr(y1)+Fr(y2-y1,x2-x1)*(x-x1)
        raise ValueError('tanım dışı')
    return f
def grafik(nok,yr,ad='f',vurgu=()):
    """Birim kareli dik koordinat düzleminde parçalı doğrusal grafik. vurgu: [(x, y)] kesikli izdüşümlü noktalar."""
    xmin,xmax=nok[0][0],nok[-1][0]; xa,xb=min(xmin,0)-1,max(xmax,0)+1; ya,yb=min(yr[0],0)-1,max(yr[1],0)+1
    u=min(280/(xb-xa),26); W=330; ox=(W-(xb-xa)*u)/2; oy=14
    X=lambda x:ox+(x-xa)*u; Y=lambda y:oy+(yb-y)*u; Hh=oy+(yb-ya)*u+14; b=[]
    for x in range(xa,xb+1): b.append(f'<line x1="{X(x):.1f}" y1="{Y(yb):.1f}" x2="{X(x):.1f}" y2="{Y(ya):.1f}" stroke-width=".6" opacity=".18"/>')
    for y in range(ya,yb+1): b.append(f'<line x1="{X(xa):.1f}" y1="{Y(y):.1f}" x2="{X(xb):.1f}" y2="{Y(y):.1f}" stroke-width=".6" opacity=".18"/>')
    b.append(f'<path d="M{X(xa):.1f} {Y(0):.1f} H{X(xb):.1f} m-7 -4 l7 4 l-7 4" stroke-width="1.4"/>')
    b.append(f'<path d="M{X(0):.1f} {Y(ya):.1f} V{Y(yb):.1f} m-4 7 l4 -7 l4 7" stroke-width="1.4"/>')
    b.append(G._t(X(xb)-4,Y(0)+16,'x',size=12,bold=True)); b.append(G._t(X(0)+12,Y(yb)+10,'y',size=12,bold=True))
    et=[]   # eksen etiketleri en son, zemin renginde haleyle (çizgi üstünden okunur)
    hale=lambda x,y,s,anc='middle':f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anc}" font-size="10" style="fill:currentColor;stroke:var(--bg,#fff);stroke-width:3;paint-order:stroke">{s}</text>'
    for x in range(xa+1,xb):
        if x: et.append(hale(X(x),Y(0)+14,M(x)))
    for y in range(ya+1,yb):
        if y: et.append(hale(X(0)-6,Y(y)+4,M(y),'end'))
    et.append(hale(X(0)-5,Y(0)+14,'O','end'))
    for x,y in vurgu:
        b.append(f'<path d="M{X(x):.1f} {Y(0):.1f} V{Y(y):.1f} H{X(0):.1f}" stroke-dasharray="3 3" stroke-width="1.2" style="stroke:{G.ACC}"/>')
    b.append(f'<path d="M{" L".join(f"{X(x):.1f} {Y(y):.1f}" for x,y in nok)}" stroke-width="2.4" stroke-linejoin="round"/>')
    for x,y in (nok[0],nok[-1]): b.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3.2" style="fill:currentColor"/>')
    for x,y in vurgu: b.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.5" style="fill:{G.ACC};stroke:{G.ACC}"/>')
    b+=et
    lx,ly=nok[-1]; b.append(G._t(X(lx)+4,Y(ly)-8,f'y = {ad}(x)',size=11,bold=True,anchor='end' if X(lx)>W-50 else 'start'))
    return G._svg(W,round(Hh),''.join(b))

DEG=B('Fonksiyonda değer','kuralda x gördüğün her yere parantez içindeki sayı yazılır. Örnek: f(x) = 2x + 3 ise f(4) = 2 × 4 + 3 = 11')
GRF=B('Grafikten değer okuma','f(a), grafiğin x = a’daki noktasının y koordinatıdır. Örnek: grafik (3, 5)’ten geçiyorsa f(3) = 5; nokta x ekseninin altındaysa değer negatiftir')
TERS=B('Ters fonksiyon','f(a) = b ise f⁻¹(b) = a’dır. Örnek: f(2) = 7 ise f⁻¹(7) = 2. f(x) = x + 4 ise f⁻¹(x) = x − 4 (işlem tersine döner)')
BIL=B('Bileşke','(f ∘ g)(x) = f(g(x)): önce g, sonra f uygulanır. Örnek: g(1) = 4 ve f(4) = 9 ise (f ∘ g)(1) = 9; sıra değişirse sonuç değişebilir')
ISL=B('Fonksiyonlarda işlem','(f + g)(x) = f(x) + g(x), (f − g)(x) = f(x) − g(x), (f · g)(x) = f(x) × g(x). Örnek: f(1) = 3, g(1) = 4 ⇒ (f · g)(1) = 12')
PAR=B('Parçalı fonksiyon','her kural yalnızca kendi aralığında geçerlidir; bir kuraldan bulduğun x o aralıkta değilse atılır. Örnek: “x < 1 ise” kuralından x = 2 çıkarsa geçersizdir')
KARE=B('Kare','x² = x × x. Örnek: 7² = 49, (−4)² = 16')

# ===== 0001 değer KOLAY (K-FN-01)
f=lambda x:2*x+3; a=[x for x in range(-50,51) if f(x)==13]; assert a==[5]; v=f(2*5); assert v==23
assert 2*f(5)==26 and 2*5+3==13 and f(16)==35
s=['10','13','23','26','35']; tek_dogru(s,'C',v)
P.R('0001','fn-deger','Fonksiyonda değer bulma','kolay','Fonksiyonda Değer','Doğrusal fonksiyonda verilen değerden bilinmeyen girdiyi bulup yeni bir girdide değer hesaplar.','düz',2,
 'K-FN-01 (girdiyi bulup yeni girdide değer) · istenen f(2a)',
 'Gerçel sayılar kümesi üzerinde tanımlı f fonksiyonu\nf(x) = 2x + 3\nbiçiminde veriliyor.\nf(a) = 13 olduğuna göre f(2a) kaçtır?',
 s,'C','f fonksiyonunun 2a’daki değeri.',
 ['f(a)’yı kurala göre a cinsinden yaz.','Denklemi çözüp a’yı bul.','f(2a) için kuralda x yerine 2a’nın sayı değerini yaz.'],[DEG],
 [A('a’yı bul','f(a), kuralda x yerine a yazılarak bulunur.','2a + 3 = 13 ⇒ a = 5'),
  A('Girdiyi hesapla','f(2a) için girdi 2a’dır.','2a = 10'),
  A('Değeri bul','Kuralda x yerine 10 yaz.','f(10) = 2 × 10 + 3 = 23')],
 'f(2a) ile 2 × f(a) farklıdır: önce girdiyi hesapla, sonra kurala yerleştir.',
 dict(A='10, 2a’nın değeri; istenen f(2a).',B='13, f(2a)’yı 2a + 3 sanıp 10 + 3 hesaplamak; x’in katsayısı olan 2 unutulmuş.',D='26, 2 × f(a) hesaplamak; f(2a), f(a)’nın iki katı değildir.',E='35, 2a + 3 = 13’ü 2a = 16 diye çözüp a = 8 bulmak.'),
 TT(A='dikkat',B='islem',D='bilgi',E='islem'))
g=lambda x:4*x-1; b=[x for x in range(-50,51) if g(x)==19]; assert b==[5]; v=g(5+3); assert v==31
assert g(5)+3==22 and g(5)+g(3)==30 and 4*8+1==33
s=['8','22','30','31','33']; tek_dogru(s,'D',v)
P.K('0001','Gerçel sayılarda tanımlı g fonksiyonu için\ng(x) = 4x − 1\ndir.\ng(b) = 19 olduğuna göre g(b + 3) kaçtır?',
 s,'D','g fonksiyonunun b + 3’teki değeri.',
 ['g(b) = 19 eşitliğinden b’yi bul.','b + 3’ün sayı değerini hesapla.','Bu sayıyı kurala yerleştir.'],[DEG],
 [A('b’yi bul','Kuralda x yerine b yaz.','4b − 1 = 19 ⇒ b = 5'),
  A('Girdi','İstenen girdi b + 3.','b + 3 = 8'),
  A('Değer','Kurala 8 yaz.','g(8) = 4 × 8 − 1 = 31')],
 'Girdiye eklenen sayı çıktıya aynen eklenmez; önce yeni girdiyi bul, sonra kurala koy.',
 dict(A='8, b + 3’ün değeri; istenen g(b + 3).',B='22, g(b) + 3 hesaplamak; girdiye 3 eklemek çıktıya 3 eklemek değildir.',C='30, g(b) + g(3) = 19 + 11 hesaplamak; g(b + 3), g(b) + g(3)’e eşit değildir.',E='33, g(8)’i 4 × 8 + 1 hesaplamak; kuralda −1 var.'),
 TT(A='dikkat',B='bilgi',C='bilgi',E='islem'))

# ===== 0002 grafik okuma KOLAY (K-FN-02)
N2=[(-2,1),(0,3),(2,3),(4,-1),(5,1)]; f=pl(N2)
assert f(-1)==2 and f(4)==-1 and f(-2)==1 and f(0)==3
v=f(-1)+f(4); assert v==1
assert -1+f(4)==-2 and f(-2)+f(4)==0 and f(0)+f(4)==2 and f(-1)+1==3
s=['−2','0','1','2','3']; tek_dogru(s,'C',v)
P.R('0002','fn-grafik','Grafikten değer okuma','kolay','Grafik','Grafikten verilen noktalardaki fonksiyon değerlerini işaretiyle okur.','grafik',2,
 'K-FN-02 (grafikten değer okuma) · bir değer x ekseninin altında',
 'Dik koordinat düzleminde [−2, 5] aralığında tanımlı y = f(x) fonksiyonunun grafiği aşağıda verilmiştir.\nBuna göre f(−1) + f(4) toplamı kaçtır?',
 s,'C','f(−1) ile f(4)’ün toplamı.',
 ['f(−1) için x = −1’den dikey çık; grafiğe değdiğin yerin yüksekliği nedir?','x = 4’te grafik x ekseninin üstünde mi, altında mı?','İki değeri işaretleriyle topla.'],[GRF],
 [A('f(−1)’i oku','x = −1’den dikey çık; grafiğe değdiğin noktanın y değerini al.','f(−1) = 2'),
  A('f(4)’ü oku','x = 4’te grafik x ekseninin altında.','f(4) = −1',grafik(N2,(-1,3),vurgu=[(-1,2),(4,-1)])),
  A('Topla','İki değeri işaretleriyle topla.','2 + (−1) = 1')],
 'Grafikte f(a), x = a’daki noktanın yüksekliğidir; x ekseninin altındaki nokta negatif değer verir.',
 dict(A='−2, f(−1)’i −1 sanmak; f(−1), x = −1’deki noktanın y değeridir.',B='0, f(−1)’i x = −2’deki değerden (1) okumak.',D='2, f(−1) yerine f(0) = 3’ü okumak: 3 + (−1).',E='3, f(4)’ü 1 almak; nokta x ekseninin altında, f(4) = −1.'),
 TT(A='bilgi',B='dikkat',D='dikkat',E='islem'),sekil=grafik(N2,(-1,3)))
N2k=[(-3,-1),(-1,3),(2,0),(4,0),(5,2)]; g=pl(N2k)
assert g(-3)==-1 and g(0)==2 and g(3)==0 and g(-1)==3
v=g(-3)+g(0)+g(3); assert v==1
assert -1+3+0==2 and 1+2+0==3 and -1+2+3==4 and 3+2+0==5
s=['1','2','3','4','5']; tek_dogru(s,'A',v)
P.K('0002','Aşağıda [−3, 5] aralığında tanımlı y = g(x) fonksiyonunun grafiği dik koordinat düzleminde gösterilmiştir.\nBuna göre g(−3) + g(0) + g(3) toplamı kaçtır?',
 s,'A','Üç fonksiyon değerinin toplamı.',
 ['Her x değeri için dikey çizgiyle grafiğe ulaş ve y değerini oku.','x = −3’teki nokta x ekseninin hangi tarafında?','x = 3’te grafik x ekseninin üzerinde mi duruyor?'],[GRF],
 [A('g(−3)','Grafiğin başlangıç noktası x ekseninin altında.','g(−3) = −1'),
  A('g(0) ve g(3)','x = 0’da grafik 2 yüksekliğinde; x = 3’te x ekseni üzerinde.','g(0) = 2 · g(3) = 0',grafik(N2k,(-1,3),ad='g',vurgu=[(-3,-1),(0,2),(3,0)])),
  A('Topla','Değerleri işaretleriyle topla.','−1 + 2 + 0 = 1')],
 'Grafik x ekseni üzerindeyse değer 0, altındaysa negatiftir; okuduğun her değeri işaretiyle yaz.',
 dict(B='2, g(0)’ı x = −1’deki tepe değeri (3) sanmak: −1 + 3 + 0.',C='3, g(−3)’ü 1 almak; nokta x ekseninin altında.',D='4, g(3)’ü 3 sanmak; x değerini y değeri yerine koymak.',E='5, g(−3) yerine tepe noktasındaki 3’ü okumak: 3 + 2 + 0.'),
 TT(B='dikkat',C='islem',D='bilgi',E='dikkat'),sekil=grafik(N2k,(-1,3),ad='g'))

# ===== 0003 ters fonksiyon ORTA (K-FN-04)
a_=[a for a in range(-20,21) if a*3-6==9]; assert a_==[5]
f=lambda x:5*x-6; finv=lambda y:Fr(y+6,5)
assert all(finv(f(x))==x for x in range(-10,11)) and finv(9)==3
v=finv(24); assert v==6
assert [a for a in range(-20,21) if 9*a-6==3]==[1] and (24+6)//1==30 and f(24)==114
s=['3','5','6','30','114']; tek_dogru(s,'C',v)
P.R('0003','fn-ters','Ters fonksiyon','orta','Ters Fonksiyon','Ters fonksiyonun bir değerinden kuraldaki parametreyi bulur ve başka bir ters değeri hesaplar.','düz',3,
 'K-FN-04 (ters değerden parametre) · doğrusal kural, istenen başka bir ters değer',
 'a bir gerçel sayı olmak üzere, gerçel sayılar kümesinde tanımlı ve birebir örten f fonksiyonu\nf(x) = ax − 6\nbiçimindedir.\nf⁻¹(9) = 3 olduğuna göre f⁻¹(24) kaçtır?',
 s,'C','f⁻¹(24)’ün değeri.',
 ['f⁻¹(9) = 3 bilgisini f cinsinden yaz.','Bu eşitlikten a’yı bul.','f⁻¹(24) = k dersen f(k) kaça eşit olur?'],[TERS],
 [A('Tersi çevir','f⁻¹(9) = 3 demek, f’nin 3’teki değeri 9 demektir.','f(3) = 9'),
  A('a’yı bul','Kuralda x yerine 3 yaz.','3a − 6 = 9 ⇒ a = 5'),
  A('Ters değeri bul','f⁻¹(24) = k ise f(k) = 24.','5k − 6 = 24 ⇒ k = 6')],
 'f⁻¹(b) = a gördüğün an f(a) = b yaz; ters fonksiyonun kuralını bulmadan da çözebilirsin.',
 dict(A='3, f⁻¹(9)’un değeri; soru f⁻¹(24)’ü soruyor.',B='5, a’nın değeri; istenen f⁻¹(24).',D='30, f⁻¹(9) = 3’ü f(9) = 3 sanmak: 9a − 6 = 3 ⇒ a = 1 ve f⁻¹(24) = 30.',E='114, f⁻¹(24) yerine f(24) = 5 × 24 − 6 hesaplamak.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='bilgi'))
b_=[b for b in range(-20,21) if 4*(-1)+b==2]; assert b_==[6]
g=lambda x:4*x+6; ginv=lambda y:Fr(y-6,4); assert all(ginv(g(x))==x for x in range(-10,11))
v=ginv(18); assert v==3 and 18-6==12 and g(18)==78
s=['−1','3','6','12','78']; tek_dogru(s,'B',v)
P.K('0003','b bir gerçel sayı olmak üzere birebir ve örten g: ℝ → ℝ fonksiyonu\ng(x) = 4x + b\nkuralıyla tanımlanıyor.\ng⁻¹(2) = −1 olduğuna göre g⁻¹(18) kaçtır?',
 s,'B','g⁻¹(18)’in değeri.',
 ['g⁻¹(2) = −1 eşitliğini g ile yaz.','b’yi bul.','g⁻¹(18) = k ise g(k) = 18 denklemini çöz.'],[TERS],
 [A('Tersi çevir','g⁻¹(2) = −1 ise g’nin −1’deki değeri 2’dir.','g(−1) = 2'),
  A('b’yi bul','Kuralda x yerine −1 yaz.','−4 + b = 2 ⇒ b = 6'),
  A('Ters değer','g⁻¹(18) = k ise g(k) = 18.','4k + 6 = 18 ⇒ 4k = 12 ⇒ k = 3')],
 'Ters fonksiyonda girdi ile çıktı yer değiştirir: g⁻¹(b) = a ⇔ g(a) = b.',
 dict(A='−1, g⁻¹(2)’nin değeri; soru g⁻¹(18)’i soruyor.',C='6, b’nin değeri; istenen g⁻¹(18).',D='12, 4k = 12 eşitliğinde 4’e bölmeyi unutmak.',E='78, g⁻¹(18) yerine g(18) = 4 × 18 + 6 hesaplamak.'),
 TT(A='dikkat',C='dikkat',D='islem',E='bilgi'))

# ===== 0004 bileşke ORTA (K-FN-05)
f=lambda x:2*x+1; g=lambda x:x*x-3
a_=[Fr(n,4) for n in range(1,81) if f(g(Fr(n,4)))==13]; assert a_==[3]
v=g(f(3)); assert v==46 and g(3)==6 and f(3)==7 and f(3)**2==49
s=['6','7','13','46','49']; tek_dogru(s,'D',v)
P.R('0004','fn-bileske','Bileşke fonksiyon','orta','Bileşke','Bir bileşke değerinden bilinmeyeni bulur ve ters sıradaki bileşkeyi hesaplar.','düz',3,
 'K-FN-05 (bileşkeden a, ters sıralı bileşke) · doğrusal ve ikinci dereceden kural',
 'Gerçel sayılar kümesinde tanımlı f ve g fonksiyonları\nf(x) = 2x + 1\ng(x) = x² − 3\nbiçiminde veriliyor.\na pozitif bir gerçel sayı ve (f ∘ g)(a) = 13 olduğuna göre (g ∘ f)(a) kaçtır?',
 s,'D','(g ∘ f)(a)’nın değeri.',
 ['(f ∘ g)(a) = f(g(a)): önce hangi fonksiyon uygulanır?','f(g(a))’yı a cinsinden yazıp a’yı bul; a pozitif.','(g ∘ f)(a) için önce f(a)’yı bul, sonra g’ye ver.'],[BIL,KARE],
 [A('Bileşkeyi aç','Önce g, sonra f uygulanır.','f(g(a)) = 2 × (a² − 3) + 1 = 2a² − 5'),
  A('a’yı bul','a pozitif olduğu için negatif kök alınmaz.','2a² − 5 = 13 ⇒ a² = 9 ⇒ a = 3'),
  A('Ters sıra','(g ∘ f)(3) için önce f(3).','f(3) = 2 × 3 + 1 = 7'),
  A('Sonuç','Bulduğun 7’yi g’ye ver.','g(7) = 49 − 3 = 46')],
 'Bileşkede sağdaki fonksiyon önce çalışır; (f ∘ g) ile (g ∘ f) genellikle farklıdır.',
 dict(A='6, g(a) = g(3)’ün değeri; bileşke tamamlanmamış.',B='7, f(a) = f(3)’ün değeri; g uygulanmamış.',C='13, (g ∘ f)(a)’yı (f ∘ g)(a) ile aynı sanmak; bileşkede sıra önemlidir.',E='49, g(7)’de −3’ü unutmak (yalnızca 7²).'),
 TT(A='dikkat',B='dikkat',C='bilgi',E='islem'))
f=lambda x:3*x-2; g=lambda x:x*x+1
a_=[Fr(n,6) for n in range(-60,61) if g(f(Fr(n,6)))==17]; assert sorted(a_)==[Fr(-2,3),2]
v=f(g(2)); assert v==13 and f(2)==4 and g(2)==5 and f(4)==10
s=['4','5','10','13','17']; tek_dogru(s,'D',v)
P.K('0004','f ve g, gerçel sayılarda\nf(x) = 3x − 2\ng(x) = x² + 1\nkurallarıyla tanımlı fonksiyonlardır.\na pozitif bir tam sayı olmak üzere (g ∘ f)(a) = 17 olduğuna göre (f ∘ g)(a) kaçtır?',
 s,'D','(f ∘ g)(a)’nın değeri.',
 ['(g ∘ f)(a) = g(f(a)): önce f.','(3a − 2)² + 1 = 17 denkleminde a pozitif tam sayı olmalı.','(f ∘ g)(a) için önce g(a), sonra f.'],[BIL,KARE],
 [A('Bileşkeyi aç','Önce f, sonra g uygulanır.','g(f(a)) = (3a − 2)² + 1'),
  A('a’yı bul','Karesi 16 olan sayılar 4 ve −4. 3a − 2 = −4 tam sayı a vermez.','(3a − 2)² = 16 ⇒ 3a − 2 = 4 ⇒ a = 2'),
  A('Ters sıra','(f ∘ g)(2) için önce g(2).','g(2) = 4 + 1 = 5'),
  A('Sonuç','5’i f’ye ver.','f(5) = 15 − 2 = 13')],
 'Bileşkeden bilinmeyen bulurken koşulu (pozitif, tam sayı) kullanarak fazla kökü ele.',
 dict(A='4, f(a) = f(2)’nin değeri.',B='5, g(a) = g(2)’nin değeri; f uygulanmamış.',C='10, g(2)’yi 4 alıp +1’i unutmak: f(4) = 10.',E='17, (f ∘ g)(a)’yı (g ∘ f)(a) ile aynı sanmak.'),
 TT(A='dikkat',B='dikkat',C='islem',E='bilgi'))

# ===== 0005 dört işlem ORTA (K-FN-07)
a_=[a for a in range(-20,21) if (a*2+2)-(2-a)==9]; assert a_==[3]
f=lambda x:3*x+2; g=lambda x:x-3
v=f(4)*g(4); assert v==14 and f(g(4))==5 and g(f(4))==11 and f(4)+g(4)==15 and f(4)*(4+3)==98
s=['5','11','14','15','98']; tek_dogru(s,'C',v)
P.R('0005','fn-islem','Fonksiyonlarda dört işlem','orta','Fonksiyonlarda İşlem','Fark fonksiyonunun bir değerinden parametreyi bulur, çarpım fonksiyonunun değerini hesaplar.','düz',3,
 'K-FN-07 (işlemden parametre, çarpım fonksiyonu) · fark ile verilen koşul',
 'a bir gerçel sayı olmak üzere gerçel sayılar kümesinde tanımlı f ve g fonksiyonları\nf(x) = ax + 2\ng(x) = x − a\nbiçimindedir.\n(f − g)(2) = 9 olduğuna göre (f · g)(4) kaçtır?',
 s,'C','(f · g)(4)’ün değeri.',
 ['(f − g)(2) = f(2) − g(2) olarak aç.','Parantezleri dikkatle açıp a’yı bul.','(f · g)(4) = f(4) × g(4).'],[ISL],
 [A('Farkı aç','(f − g)(2) = f(2) − g(2); ikinci parantezin önündeki eksi her terimi etkiler.','(2a + 2) − (2 − a) = 3a'),
  A('a’yı bul','Eşitliğin iki yanını 3’e böl.','3a = 9 ⇒ a = 3'),
  A('Değerler','Kurallar f(x) = 3x + 2 ve g(x) = x − 3 olur.','f(4) = 14 · g(4) = 1'),
  A('Çarp','Çarpım fonksiyonu değerlerin çarpımıdır.','f(4) × g(4) = 14 × 1 = 14')],
 '(f · g)(x) bir çarpımdır, bileşke değildir: iki değeri ayrı bul, sonra çarp.',
 dict(A='5, (f · g)(4)’ü f(g(4)) = f(1) sanmak; çarpım bileşke değildir.',B='11, g(f(4)) = g(14) hesaplamak; istenen çarpım.',D='15, f(4) + g(4) toplamı; istenen çarpım.',E='98, g(4)’ü 4 + 3 = 7 almak; g(x) = x − a.'),
 TT(A='bilgi',B='bilgi',D='dikkat',E='islem'))
b_=[b for b in range(-20,21) if (2*2-b)+(b*2+1)==13]; assert b_==[8]
f=lambda x:2*x-8; g=lambda x:8*x+1
v=f(3)*g(3); assert v==-50 and g(f(3))==-15 and f(3)+g(3)==23 and f(g(3))==42
s=['−50','−15','23','42','50']; tek_dogru(s,'A',v)
P.K('0005','b bir gerçel sayı olmak üzere f ve g fonksiyonları gerçel sayılarda\nf(x) = 2x − b\ng(x) = bx + 1\nkurallarıyla tanımlanıyor.\n(f + g)(2) = 13 olduğuna göre (f · g)(3) kaçtır?',
 s,'A','(f · g)(3)’ün değeri.',
 ['(f + g)(2) = f(2) + g(2).','b’yi bulup iki kuralı yeniden yaz.','f(3) ve g(3)’ü ayrı ayrı bul ve çarp; işarete dikkat.'],[ISL],
 [A('Toplamı aç','f(2) ile g(2)’yi topla.','(4 − b) + (2b + 1) = 5 + b'),
  A('b’yi bul','İki yandan 5 çıkar.','5 + b = 13 ⇒ b = 8'),
  A('Değerler','Kurallar f(x) = 2x − 8, g(x) = 8x + 1 olur.','f(3) = −2 · g(3) = 25'),
  A('Çarp','Negatif ile pozitifin çarpımı negatiftir.','f(3) × g(3) = −2 × 25 = −50')],
 'Çarpım fonksiyonunda her değeri işaretiyle bul; tek bir negatif çarpan sonucu negatif yapar.',
 dict(B='−15, g(f(3)) = g(−2) hesaplamak; çarpım bileşke değildir.',C='23, f(3) + g(3) toplamı; istenen çarpım.',D='42, f(g(3)) = f(25) hesaplamak.',E='50, f(3)’ü 2 almak; 6 − 8 = −2.'),
 TT(B='bilgi',C='dikkat',D='bilgi',E='islem'))

# ===== 0006 grafikte bileşke ORTA (K-FN-03)
N6=[(-3,-1),(-1,3),(1,1),(3,1),(4,3)]; f=pl(N6)
assert f(-3)==-1 and f(-2)==1 and f(-1)==3 and f(1)==1
v=f(f(-3))+f(f(-2)); assert v==4
assert f(-3)+f(-2)==0 and f(-3)**2+f(-2)**2==2 and f(f(-3))==3 and f(f(-2))==1
s=['0','1','2','3','4']; tek_dogru(s,'E',v)
P.R('0006','fn-grafik','Grafikten değer okuma','orta','Grafik','Grafikten bileşke değerleri iki aşamalı okuma ile bulur.','grafik',3,
 'K-FN-03 (grafikte bileşke) · iki bileşke değerinin toplamı',
 'Dik koordinat düzleminde [−3, 4] aralığında tanımlı f fonksiyonunun grafiği aşağıda verilmiştir.\nBuna göre (f ∘ f)(−3) + (f ∘ f)(−2) toplamı kaçtır?',
 s,'E','İki bileşke değerinin toplamı.',
 ['(f ∘ f)(−3) = f(f(−3)): önce içteki değeri oku.','Bulduğun sayıyı yeni x değeri gibi kullanıp grafikten tekrar oku.','Aynı işlemi −2 için yap ve topla.'],[BIL,GRF],
 [A('İçteki değerler','Önce f(−3) ve f(−2)’yi grafikten oku.','f(−3) = −1 · f(−2) = 1'),
  A('Dıştaki değerler','Bulduğun sayıları yeniden f’ye ver: x = −1 ve x = 1’de oku.','f(−1) = 3 · f(1) = 1',grafik(N6,(-1,3),vurgu=[(-1,3),(1,1)])),
  A('Topla','İki bileşke değerini topla.','3 + 1 = 4')],
 'Grafikte bileşke iki kez okumaktır: çıkan y değeri bir sonraki adımın x değeri olur.',
 dict(A='0, f’yi bir kez uygulamak: f(−3) + f(−2) = −1 + 1.',B='1, yalnızca (f ∘ f)(−2)’yi almak; toplamın ilk terimi unutulmuş.',C='2, (f ∘ f)(x)’i f(x) × f(x) sanmak: (−1)² + 1².',D='3, yalnızca (f ∘ f)(−3)’ü almak; ikinci terim unutulmuş.'),
 TT(A='bilgi',B='dikkat',C='bilgi',D='dikkat'),sekil=grafik(N6,(-1,3)))
N6k=[(-2,0),(0,4),(2,2),(4,-2),(5,0)]; g=pl(N6k)
assert g(-1)==2 and g(4)==-2 and g(2)==2 and g(-2)==0 and g(1)==3
v=g(g(-1))+g(g(4)); assert v==2
assert g(-1)+g(4)==0 and g(1)+g(-2)==3 and g(2)+g(2)==4 and g(-1)**2+g(4)**2==8
s=['0','2','3','4','8']; tek_dogru(s,'B',v)
P.K('0006','Aşağıdaki dik koordinat düzleminde [−2, 5] aralığında tanımlı g fonksiyonunun grafiği gösterilmiştir.\nBuna göre (g ∘ g)(−1) + (g ∘ g)(4) toplamı kaçtır?',
 s,'B','İki bileşke değerinin toplamı.',
 ['İçteki değerleri (g(−1) ve g(4)) grafikten oku.','x = 4’te grafik x ekseninin altında; değeri işaretiyle al.','Bulduğun değerleri yeni x olarak grafikte tekrar oku.'],[BIL,GRF],
 [A('İçteki değerler','g(−1) ve g(4)’ü grafikten oku.','g(−1) = 2 · g(4) = −2'),
  A('Dıştaki değerler','x = 2 ve x = −2’de grafiği oku.','g(2) = 2 · g(−2) = 0',grafik(N6k,(-2,4),ad='g',vurgu=[(2,2),(-2,0)])),
  A('Topla','İki bileşke değerini topla.','2 + 0 = 2')],
 'İçteki değer negatifse grafikte sola, x ekseninin negatif tarafına git.',
 dict(A='0, g’yi bir kez uygulamak: g(−1) + g(4) = 2 + (−2).',C='3, g(2) yerine komşu x = 1’deki değeri (3) okumak.',D='4, g(4)’ü 2 alıp g(2) = 2 bulmak; x = 4’te grafik eksenin altında.',E='8, (g ∘ g)(x)’i g(x) × g(x) sanmak: 2² + (−2)².'),
 TT(A='bilgi',C='dikkat',D='islem',E='bilgi'),sekil=grafik(N6k,(-2,4),ad='g'))

# ===== 0007 bileşke + ters ZOR (K-FN-06)
f=lambda x:3*x-2; finv=lambda y:Fr(y+2,3); g=lambda x:x+4; ginv=lambda y:y-4
assert all(finv(f(x))==x and ginv(g(x))==x for x in range(-10,11))
a_=[a for a in range(-50,51) if finv(g(a))==5]; assert a_==[9]
v=ginv(f(9)); assert v==21 and f(9)==25 and f(9)+4==29
aw=[a for a in range(-50,51) if Fr(a+4-2,3)==5]; assert aw==[13] and f(13)-4==33
s=['9','21','25','29','33']; tek_dogru(s,'B',v)
P.R('0007','fn-bileske','Bileşke fonksiyon','zor','Bileşke','Ters fonksiyon içeren bileşkeden bilinmeyeni bulur ve başka bir ters-bileşke değeri hesaplar.','düz',4,
 'K-FN-06 (ters ve bileşke birlikte) · (f⁻¹ ∘ g) verilip (g⁻¹ ∘ f) isteniyor',
 'Gerçel sayılarda tanımlı f ve g fonksiyonları\nf(x) = 3x − 2\ng(x) = x + 4\nolarak veriliyor.\n(f⁻¹ ∘ g)(a) = 5 olduğuna göre (g⁻¹ ∘ f)(a) kaçtır?',
 s,'B','(g⁻¹ ∘ f)(a)’nın değeri.',
 ['(f⁻¹ ∘ g)(a) = f⁻¹(g(a)) = 5 ise g(a), f’nin hangi değerine eşittir?','g(a) = a + 4 eşitliğinden a’yı bul.','g⁻¹ kuralında işlem tersine döner: 4 eklemenin tersi 4 çıkarmaktır.'],[TERS,BIL],
 [A('Dıştaki tersi kaldır','f⁻¹(g(a)) = 5 ise g(a) = f(5).','g(a) = 3 × 5 − 2 = 13'),
  A('a’yı bul','g(a) = a + 4.','a + 4 = 13 ⇒ a = 9'),
  A('İçi hesapla','(g⁻¹ ∘ f)(9) için önce f(9).','f(9) = 27 − 2 = 25'),
  A('Tersi uygula','g 4 ekliyorsa g⁻¹ 4 çıkarır.','g⁻¹(x) = x − 4 ⇒ g⁻¹(25) = 21')],
 'f⁻¹(k) = m ise k = f(m): ters fonksiyonu kaldırmak için diğer tarafa f uygula.',
 dict(A='9, a’nın değeri; istenen (g⁻¹ ∘ f)(a).',C='25, f(a) = f(9); g⁻¹ uygulanmamış.',D='29, g⁻¹(x)’i x + 4 sanmak; tersinde işlem tersine döner.',E='33, f⁻¹(x)’i (x − 2)/3 sanıp a = 13 bulmak.'),
 TT(A='dikkat',C='dikkat',D='bilgi',E='bilgi'))
f=lambda x:2*x+5; finv=lambda y:Fr(y-5,2); g=lambda x:x-3; ginv=lambda y:y+3
assert all(finv(f(x))==x and ginv(g(x))==x for x in range(-10,11))
a_=[a for a in range(-50,51) if ginv(f(a))==12]; assert a_==[2]
v=f(ginv(2)); assert v==15 and f(g(2))==3
aw=[a for a in range(-50,51) if f(a)-3==12]; assert aw==[5] and f(5-3)==9
s=['2','3','9','12','15']; tek_dogru(s,'E',v)
P.K('0007','f ve g fonksiyonları gerçel sayılarda\nf(x) = 2x + 5\ng(x) = x − 3\nbiçiminde tanımlıdır.\n(g⁻¹ ∘ f)(a) = 12 olduğuna göre (f ∘ g⁻¹)(a) kaçtır?',
 s,'E','(f ∘ g⁻¹)(a)’nın değeri.',
 ['g⁻¹(f(a)) = 12 ise f(a) = g(12).','f(a)’dan a’yı bul.','g 3 çıkarıyorsa g⁻¹ ne yapar? Önce g⁻¹(a), sonra f.'],[TERS,BIL],
 [A('Tersi kaldır','g⁻¹(f(a)) = 12 ise f(a) = g(12).','f(a) = 12 − 3 = 9'),
  A('a’yı bul','f(a) = 2a + 5.','2a + 5 = 9 ⇒ a = 2'),
  A('g⁻¹ kuralı','g 3 çıkarıyorsa g⁻¹ 3 ekler.','g⁻¹(x) = x + 3 ⇒ g⁻¹(2) = 5'),
  A('Sonuç','Bulduğun 5’i f’ye ver.','f(5) = 10 + 5 = 15')],
 'Tersin kuralını yazarken işlemi tersine çevir: “3 çıkar”ın tersi “3 ekle”dir.',
 dict(A='2, a’nın değeri; istenen (f ∘ g⁻¹)(a).',B='3, g⁻¹ yerine g kullanmak: f(g(2)) = f(−1).',C='9, g⁻¹’i x − 3 sanmak; a = 5 ve f(2) = 9 bulunur.',D='12, verilen (g⁻¹ ∘ f)(a) değeri; istenen bileşke farklı.'),
 TT(A='dikkat',B='bilgi',C='bilgi',D='dikkat'))

# ===== 0008 parçalı ZOR (K-FN-08)
def parcali(p,c,q,r):
    f=lambda x:(x+p) if x<c else (q*x+r)
    def coz(y):
        """f(x) = y: her kuraldan aday ve geçerli mi?"""
        return [(Fr(y-p),Fr(y-p)<c),(Fr(y-r,q),Fr(y-r,q)>=c)]
    return f,coz
f,coz=parcali(2,1,2,-6)
ts=[t for t,ok in coz(2) if ok]; assert ts==[0,4]
ad=[(a,ok) for t in ts for a,ok in coz(t)]; S=sorted(a for a,ok in ad if ok); assert S==[-2,3,5] and [a for a,ok in ad if not ok]==[2]
tarama=sorted({Fr(n,12) for n in range(-240,241) if f(f(Fr(n,12)))==2}); assert tarama==S
v=sum(S); assert v==6
assert [a for a in range(-20,21) if (a+2)+2==2]==[-2] and [Fr(n,4) for n in range(-80,81) if 2*(2*Fr(n,4)-6)-6==2]==[5] and sum(ts)==4 and v+2==8
s=['−2','4','5','6','8']; tek_dogru(s,'D',v)
P.R('0008','fn-parcali','Parçalı fonksiyon','zor','Parçalı Fonksiyon','Parçalı fonksiyonda f(f(a)) = k denklemini her kuralı kendi aralığında deneyerek çözer.','düz',4,
 'K-FN-08 (parçalı fonksiyonda iç içe denklem) · bir aday aralık dışında kalıyor',
 'Gerçel sayılar kümesinde tanımlı f fonksiyonu\nf(x) = x + 2, x < 1 ise\nf(x) = 2x − 6, x ≥ 1 ise\nbiçiminde tanımlanıyor.\nf(f(a)) = 2 eşitliğini sağlayan a gerçel sayılarının toplamı kaçtır?',
 s,'D','f(f(a)) = 2 denkleminin çözümlerinin toplamı.',
 ['Önce f(t) = 2 olan t değerlerini bul; f(a) bu değerlerden biri olmalı.','Her denklemi iki kuralla ayrı ayrı çöz.','Bulduğun her x’in o kuralın aralığında olup olmadığını kontrol et.'],[PAR],
 [A('Dıştan başla','f(t) = 2 olan t’leri bul; her kuralı kendi aralığında dene.','t < 1: t + 2 = 2 ⇒ t = 0 ✓ · t ≥ 1: 2t − 6 = 2 ⇒ t = 4 ✓'),
  A('f(a) = 0','İki kuralı dene, aralığı kontrol et.','a < 1: a + 2 = 0 ⇒ a = −2 ✓ · a ≥ 1: 2a − 6 = 0 ⇒ a = 3 ✓'),
  A('f(a) = 4','Aralık kontrolü burada bir adayı eler.','a < 1: a + 2 = 4 ⇒ a = 2 ✗ (2 < 1 değil) · a ≥ 1: 2a − 6 = 4 ⇒ a = 5 ✓'),
  A('Topla','Geçerli a değerleri −2, 3 ve 5.','−2 + 3 + 5 = 6')],
 'Parçalı fonksiyonda her adayı bulduğun kuralın aralığına geri koyup kontrol et.',
 dict(A='−2, her yerde yalnızca x < 1 kuralını kullanmak: (a + 2) + 2 = 2.',B='4, f(a)’nın alabileceği değerleri (0 ve 4) toplamak; istenen a değerleri.',C='5, her yerde yalnızca x ≥ 1 kuralını kullanmak: 2(2a − 6) − 6 = 2.',E='8, x < 1 kuralından çıkan a = 2’yi de saymak; 2 bu aralıkta değil.'),
 TT(A='bilgi',B='dikkat',C='bilgi',E='dikkat'))
f,coz=parcali(2,0,2,-5)
ts=[t for t,ok in coz(1) if ok]; assert ts==[-1,3]
ad=[(a,ok) for t in ts for a,ok in coz(t)]; S=sorted(a for a,ok in ad if ok); assert S==[-3,2,4] and [a for a,ok in ad if not ok]==[1]
tarama=sorted({Fr(n,12) for n in range(-240,241) if f(f(Fr(n,12)))==1}); assert tarama==S
v=sum(S); assert v==3 and sum(ts)==2 and v+1==4 and 2+4==6
assert [a for a in range(-20,21) if (a+2)+2==1]==[-3]
s=['−3','2','3','4','6']; tek_dogru(s,'C',v)
P.K('0008','f: ℝ → ℝ fonksiyonu\nf(x) = x + 2, x < 0 ise\nf(x) = 2x − 5, x ≥ 0 ise\nkuralıyla veriliyor.\nf(f(a)) = 1 olacak biçimdeki tüm a gerçel sayılarının toplamı kaçtır?',
 s,'C','f(f(a)) = 1 denkleminin çözümlerinin toplamı.',
 ['f(t) = 1 olan t değerlerini bul.','f(a) = t denklemlerini iki kuralla ayrı ayrı çöz.','Her adayın kendi kuralının aralığında olup olmadığına bak.'],[PAR],
 [A('Dıştan başla','f(t) = 1 için iki kuralı dene.','t < 0: t + 2 = 1 ⇒ t = −1 ✓ · t ≥ 0: 2t − 5 = 1 ⇒ t = 3 ✓'),
  A('f(a) = −1','İki kural da geçerli aday verir.','a < 0: a = −3 ✓ · a ≥ 0: 2a − 5 = −1 ⇒ a = 2 ✓'),
  A('f(a) = 3','Bir aday aralık dışında kalır.','a < 0: a + 2 = 3 ⇒ a = 1 ✗ (1 < 0 değil) · a ≥ 0: 2a − 5 = 3 ⇒ a = 4 ✓'),
  A('Topla','Geçerli çözümler −3, 2, 4.','−3 + 2 + 4 = 3')],
 'İki katmanlı denklemde dıştan içe çöz ve her adımda aralık kontrolü yap.',
 dict(A='−3, her yerde yalnızca x < 0 kuralını kullanmak.',B='2, f(a)’nın alabileceği değerleri (−1 ve 3) toplamak; istenen a değerleri.',D='4, aralık dışında kalan a = 1’i de saymak.',E='6, f(a) = −1 için x < 0 kuralını denemeyip a = −3’ü kaçırmak.'),
 TT(A='bilgi',B='dikkat',D='dikkat',E='dikkat'))

P.yaz(os.path.join(H,'fonksiyon-1.json'),os.path.join(H,'fonksiyon-1-kardes.json'))
