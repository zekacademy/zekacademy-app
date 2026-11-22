"""AYT Matematik · Eşitsizlikler 2. dalga (20 soru): tam sayı sayma, parametre, işaret tablosu, ters mühendislik, grafik, öncül.
Her doğru ve çeldirici değer koddan hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _esz import *
import _hafif_mat as H
from _hafif_mat import kart,mk,tablo_svg
from ortak import Parti,A,B
H.KONU='Eşitsizlikler'
UK='amat|Eşitsizlikler'
P=Parti('esitsiziki','Eşitsizlikler',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2025 AYT Matematik (tam sayı çözümü, eşitsizlik sistemi, öncüllü sıralama, işaret tablosu; yalnız mantık) · 345 AYT Soru Bankası (mantık) · MEB 10–12. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
Fi=Fr
def Y(v,e,t): return (v,e,t)
def tams(pred,lo,hi): return [x for x in range(lo,hi+1) if okpred(pred)(Fi(x))]

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
TAMB=B('Çözüm kümesindeki tam sayılar','Çözüm aralığının uçları kökler olduğundan uçların dahil olup olmadığı eşitsizliğin “<, ≤” türüne bağlıdır. Örnek: (x − 1)(x − 6) < 0 için çözüm (1, 6) olup tam sayılar 2, 3, 4, 5’tir; “≤” olsaydı 1 ve 6 da alınırdı')
SIS=B('Eşitsizlik sistemi','Sistemin çözümü, çözüm kümelerinin kesişimidir; sayı doğrusunda hepsinin taralı olduğu bölge alınır, uçların dahil olma durumu kesişimde yeniden kontrol edilir. Örnek: [0, 8] ile (5, ∞) kümelerinin kesişimi (5, 8]’dir')
TAB=B('İşaret tablosu','Çarpım ya da bölümün işareti, çarpanların işaretlerinin çarpımıdır. Köklerin her biri için ayrıca ifadenin değeri incelenir. Örnek: f(x) > 0 ve g(x) < 0 ise f(x)/g(x) < 0’dır')
DEL=B('Her x için eşitsizlik','x² + bx + c > 0 eşitsizliği her gerçel x için sağlanıyorsa başkatsayı pozitiftir ve Δ = b² − 4c < 0 olmalıdır. Örnek: x² + 4x + n ifadesinin x ekseniyle ortak noktası olmaması için parabolün konumu incelenir')
GRF=B('Grafikten eşitsizlik','f(x) < g(x) eşitsizliğinde f’nin grafiğinin g’nin grafiğinin altında kaldığı x değerleri alınır; grafiklerin kesiştiği noktalarda f(x) = g(x) olur. Örnek: grafikler x = 1 ve x = 4’te kesişiyorsa ve f aradaki bölgede altta ise f(x) < g(x) çözümü (1, 4)’tür')
KOK=B('Eşitsizlik sistemi ve kümeler','Çözüm kümesinin uç noktaları ilgili ikinci derece ifadenin kökleridir. Başkatsayısı 1 olan x² + ax + b için a = −(kökler toplamı), b = kökler çarpımıdır. Örnek: kökler 2 ve 7 ise x² − 9x + 14 olur')
ARG=B('Grafikle eşitsizlik','f(u) için işaret bilgisi u değişkeni üzerinden okunur, sonra u yerine verilen ifade yazılıp x için çözülür. Örnek: f(u) > 0 çözümü u < 1 ya da u > 5 ise f(4x + 3) > 0 için x’in hangi değerler alacağı u = 4x + 3 dönüşümüyle bulunur')
UYG=B('Eşitsizlikle model kurma','Koşullar ikinci derece ya da doğrusal eşitsizliğe çevrilir; uzunluk, fiyat gibi niceliklerin pozitifliği ve tam sayı olma koşulu çözüm aralığıyla kesiştirilir. Örnek: bir kenar x − 3 ise x > 3 koşulu da eklenir')
SRL=B('Sıralama ve öncüller','Eşitsizlikte negatif bir sayıyla çarpıldığında ya da bölündüğünde yön değişir. Bir öncülün “kesinlikle doğru” olması, verilen koşulu sağlayan bütün durumlarda doğru olmasıdır; bir karşı örnek yeterince çürütür. Örnek: 0 < t < 1 ise t² < t’dir')
NOK=B('Sayı doğrusunda konum','Sayı doğrusunda işaretli noktaların hangi aralıkta olduğu bilgisi, çarpımın ve toplamın işaretini belirler. Örnek: p ∈ (−1, 0) ve r ∈ (1, 2) ise p · r negatiftir ve p + r pozitiftir')

# ---------- kartlar ----------
kartla('K-AESZ2-01','Tam sayı çözümlerini sayma ve toplama','Çözüm aralığı bulunur, uçların dahil olup olmadığına karar verilir ve içindeki tam sayılar yazılır; sayma ya da toplama istenene göre işlem yapılır.','Açık ucu dahil etmek; uç sayısını (fark) tam sayı sayısı sanmak; yalnız pozitif ya da negatif tam sayıları almak.','kolay','düz',3,'esz2-tamsayi','Çözüm kümesindeki tam sayılar')
kartla('K-AESZ2-02','Parametreli eşitsizlik','Parametre kökün yerini belirler; kökün büyük ya da küçük olması durumlarına ayrılıp her durumda tam sayı koşulu denenir.','Yalnız bir durumu incelemek; kökün çakıştığı tek nokta durumunu atlamak.','zor','düz',5,'esz2-parametre','Parametreli eşitsizlik')
kartla('K-AESZ2-03','Her x için sağlanan ikinci derece eşitsizlik','Başkatsayının pozitifliği ve Δ < 0 koşulu kurulur; elde edilen parametre eşitsizliği çözülüp tam sayılar bulunur.','Δ ≤ 0 almak; Δ’yı yanlış hesaplamak; çözüm kümesinin uçlarını dahil etmek.','orta','düz',4,'esz2-parametre','Parametreli eşitsizlik')
kartla('K-AESZ2-04','Grafikle eşitsizlik','Grafiklerin kesiştiği noktalar okunur; hangi aralıkta hangisinin altta olduğu belirlenir; verilen aralıktaki tam sayılar listelenir.','Uç noktaları dahil etmek; < ile > yönünü karıştırmak; tüm aralığı çözüm sanmak.','orta','grafik',4,'esz2-grafik','Grafikle eşitsizlik')
kartla('K-AESZ2-05','Argümanı değişmiş fonksiyonla çarpım eşitsizliği','Grafikten f’nin işareti okunur; argüman eşitsizliği x için çözülür; diğer çarpanla birlikte işaret tablosu kurulur; verilen aralıktaki tam sayılar sayılır.','Argümanı hiç dönüştürmeden f(x)’in kökleriyle çalışmak; ikinci çarpanı unutmak; çarpım yerine birleşim almak.','zor','grafik',5,'esz2-grafik','Grafikle eşitsizlik')
kartla('K-AESZ2-06','Eşitsizlik sistemi ve kümeler','Ortak çözümün uç noktaları hangi eşitsizliğe ait olduğuna göre eşlenir; kök toplamı ve çarpımından katsayılar bulunur.','Uç noktaları yanlış eşlemek; kök toplamının işaretini ters almak.','orta','şekilli',4,'esz2-sistem','Eşitsizlik sistemi ve kümeler')
kartla('K-AESZ2-07','Eşitsizlik sistemi ve kümeler','Her küme sayı doğrusunda okunur ya da eşitsizlikten çıkarılır; kesişim, birleşim gibi işlem uçların dahil olma durumuna dikkat edilerek yapılır.','Kesişimle birleşimi karıştırmak; içi boş noktayı kümeye dahil etmek.','kolay','şekilli',3,'esz2-sistem','Eşitsizlik sistemi ve kümeler')
kartla('K-AESZ2-08','Bölüm eşitsizliği','Pay ve payda çarpanlara ayrılır; sadeleşen çarpanın kökü ve çift katlı kök ayrıca değerlendirilir; paydayı sıfır yapan değerler çözümden çıkarılır.','Sadeleşen çarpanın kökünü çözüme katmak; çift katlı köke işaret değişimi tanımak ya da tek başına kalan sıfırı atlamak.','zor','düz',5,'esz2-bolum','Bölüm eşitsizliği')
kartla('K-AESZ2-09','İşaret tablosundan çıkarım','Tablodaki sıfırlar ve işaretler okunur; çarpım ya da bölümün işareti aralık aralık bulunur; sıfır noktaları ve tanımsız noktalar ayrıca ele alınır.','Çift katlı kökü atlamak; ortak sıfırda bölümü tanımlı sanmak; sistemde kesişimi birleşim gibi okumak.','zor','tablo',5,'esz2-tablo','İşaret tablosundan çıkarım')
kartla('K-AESZ2-10','Sıralama ve öncüllü eşitsizlik','Verilen eşitsizlikten değişkenlerin işaret ve büyüklük aralıkları çıkarılır; her öncül bu aralıklar için, gerekirse karşı örnekle, değerlendirilir.','Negatifle çarparken yönü korumak; “bazen doğru” ile “kesinlikle doğru”yu karıştırmak.','orta','öncüllü',4,'esz2-oncul','Sıralama ve öncüllü eşitsizlik')
kartla('K-AESZ2-11','Eşitsizlikle model kurma','Koşullar eşitsizliğe çevrilir, çözüm aralıkları kesiştirilir; tam sayı ya da pozitiflik koşulu eklenir.','Bir koşulu unutmak; eşitlik durumunu yanlış yorumlamak; tabloyu okuyup modeli yanlış kurmak.','orta','hikâyeli',5,'esz2-uygulama','Eşitsizlikle model kurma')

SK_DIZ=lambda s:s
def nl_rows(lo,hi,rows,sx=0.62,dy=1.1):
    o=[]
    for r,(lab,segs,col) in enumerate(rows):
        y0=-r*dy
        o.append(f'\\draw[-{{Stealth}},thick] ({(lo-0.6)*sx:.3f},{y0:.2f}) -- ({(hi+0.8)*sx:.3f},{y0:.2f}) node[right] {{$x$}};')
        o.append(f'\\node[font=\\small\\bfseries,text={col}] at ({(lo-1.3)*sx:.3f},{y0+0.28:.2f}) {{{lab}}};')
        for t in range(lo,hi+1): o.append(f'\\draw[thick] ({t*sx:.3f},{y0-0.1:.2f}) -- ({t*sx:.3f},{y0+0.1:.2f}); \\node[below=3pt,font=\\small] at ({t*sx:.3f},{y0:.2f}) {{${t}$}};'.replace('$-','$-'))
        for a,b,lc,rc in segs:
            xa=(lo-0.5)*sx if a is None else a*sx; xb=(hi+0.5)*sx if b is None else b*sx
            o.append(f'\\draw[line width=4pt,{col},opacity=.55] ({xa:.3f},{y0+0.28:.2f}) -- ({xb:.3f},{y0+0.28:.2f});')
            if b is None: o.append(f'\\fill[{col},opacity=.55] ({xb:.3f},{y0+0.28+0.2:.2f}) -- ({xb+0.3:.3f},{y0+0.28:.2f}) -- ({xb:.3f},{y0+0.28-0.2:.2f}) -- cycle;')
            if a is not None: o.append(f'\\draw[thick,{col}!70!black,fill={col if lc else "white"}] ({xa:.3f},{y0+0.28:.2f}) circle (0.11);')
            if b is not None: o.append(f'\\draw[thick,{col}!70!black,fill={col if rc else "white"}] ({xb:.3f},{y0+0.28:.2f}) circle (0.11);')
    return '\n'.join(o)
def dot(x,y,sx,sy,col): return f'\\fill[{col}] ({x*sx:.3f},{y*sy:.3f}) circle (2.4pt);'
def lab(x,y,sx,sy,txt,col,pos='above right'): return f'\\node[{pos},font=\\small,text={col},inner sep=1pt] at ({x*sx:.3f},{y*sy:.3f}) {{{txt}}};'

# =============== 01 · kolay · tam sayı sayma ===============
f1=lambda x:-x*x+2*x+15
c=tams(lambda x:f1(x)>=0,-20,20); assert c==list(range(-3,6)) and len(c)==9
w_a=len(tams(lambda x:f1(x)>0,-20,20)); w_b=5-(-3); w_c=len(tams(lambda x:f1(x)>=0 and x>=0,-20,20)); w_d=len(tams(lambda x:f1(x)>=0 and x>0,-20,20))
assert (w_a,w_b,w_c,w_d)==(7,8,6,5)
q('0001',tipId='esz2-tamsayi',tip='Çözüm kümesindeki tam sayılar',z='kolay',alt='Tam Sayı Çözümleri',kaz='Başkatsayısı negatif olan ikinci derece eşitsizliğin kapalı aralık çözümündeki tam sayıları sayar.',kalip='düz',
 kart='K-AESZ2-01 (kapalı aralık, negatif başkatsayı) · −x² + 2x + 15 ≥ 0',
 metin='−x² + 2x + 15 ≥ 0\n\neşitsizliğini sağlayan kaç tane x tam sayısı vardır?',
 dogru=9,yan=[Y(7,'Kökleri −3 ve 5 bulmuş, ancak “≥” olduğu hâlde uç değerleri dışarıda bırakmış: −2, −1, …, 4 olmak üzere 7 sayı.','dikkat'),Y(8,'Tam sayı sayısını uçların farkı olarak 5 − (−3) = 8 bulmuş; kapalı aralıkta uçlar da sayıldığı için bir fazlası alınır.','islem'),Y(6,'Yalnız negatif olmayan çözümleri saymış: 0, 1, …, 5.','dikkat'),Y(5,'Yalnız pozitif tam sayıları saymış: 1, 2, 3, 4, 5.','dikkat')],
 istenen='Eşitsizliği sağlayan tam sayıların sayısı.',ip=['Önce başkatsayısını pozitif yapacak biçimde eşitsizliği düzenle.'],bilgi=[TAMB],
 ad=[A('Başkatsayıyı pozitif yap','−1 ile çarpılınca eşitsizliğin yönü değişir.','x² − 2x − 15 ≤ 0'),A('Kökleri bul','Çarpanlara ayrılır.','(x − 5)(x + 3) ≤ 0 → kökler −3 ve 5'),A('Çözüm aralığını yaz','Kökler arasındaki değerlerde ifade negatiftir; “≤” olduğundan uçlar dahildir.','−3 ≤ x ≤ 5'),A('Tam sayıları say','−3’ten 5’e kadar uçlar dahil.','−3, −2, …, 5 → 9 tane')],
 puf='Kapalı aralıkta tam sayı sayısı = (büyük uç − küçük uç) + 1.')

# =============== 02 · kolay · grafik ===============
f2=lambda x:-(x+1)*(x-5)
c=tams(lambda x:f2(x)>0,-10,10); assert c==[0,1,2,3,4]
w_a=len(tams(lambda x:f2(x)>=0,-10,10)); w_b=len(tams(lambda x:f2(x)>0 or x==5,-10,10)); w_c=len([x for x in range(1,5)]); w_d=f2(2)
assert (w_a,w_b,w_c,w_d)==(7,6,4,9)
sx,sy=0.55,0.3
SK=fig('\n'.join([axes(-2,6,-1,10,sx,sy,xt=list(range(-2,7)),yt=[5,9]),curve(f2,-1.8,5.8,sx,sy,-1,10,'blue!70!black'),dot(-1,0,sx,sy,'blue!70!black'),dot(5,0,sx,sy,'blue!70!black'),dot(0,5,sx,sy,'blue!70!black'),lab(4.4,7.2,sx,sy,'$f$','blue!70!black','right')]))
q('0002',tipId='esz2-grafik',tip='Grafikle eşitsizlik',z='kolay',alt='Grafikten Tam Sayı',kaz='Grafiği verilen parabolün x eksenine göre konumundan f(x) > 0 koşulunu sağlayan tam sayıları sayar.',kalip='grafik',
 kart='K-AESZ2-04 (tek grafik) · aşağı açık parabol; f(x) > 0 için tam sayı sayısı',
 metin='Şekilde, gerçel sayılar kümesi üzerinde tanımlı f ikinci derece fonksiyonunun grafiği verilmiştir.\n\nBuna göre f(x) > 0 eşitsizliğini sağlayan kaç tane x tam sayısı vardır?',
 dogru=5,yan=[Y(7,'Kökleri de çözüme katmış; f(−1) = f(5) = 0 olduğundan “>” için bu iki değer alınmaz: −1, 0, …, 5 olmak üzere 7 sayı.','dikkat'),Y(6,'Yalnız bir kökü (x = 5) çözüme katmış; iki kök de f(x) = 0 verir.','dikkat'),Y(4,'1, 2, 3, 4 tam sayılarını alıp grafiğin y eksenini kestiği x = 0 değerini atlamış.','islem'),Y(9,'Parabolün en büyük y değerini (tepe noktasının ordinatı, 9) tam sayı sayısı sanmış.','bilgi')],
 istenen='f(x) > 0 eşitsizliğini sağlayan tam sayıların sayısı.',ip=['Grafiğin x eksenine göre hangi aralıkta üstte kaldığına bak.'],bilgi=[GRF,TAMB],sekil=SK,
 ad=[A('Kökleri oku','Grafik x eksenini iki noktada kesiyor.','x = −1 ve x = 5'),A('Pozitif bölgeyi bul','Grafik bu iki nokta arasında eksenin üstünde; köklerde f(x) = 0.','−1 < x < 5'),A('Tam sayıları say','Uçlar dahil değil.','0, 1, 2, 3, 4 → 5 tane')],
 puf='Grafiğin x ekseninin üstünde kaldığı aralığı oku.')

# =============== 03 · kolay · iki küme, sayı doğrusu ===============
A3=[(-2,4,True,True)]; B3=[(1,None,False,False)]
a3=set(range(-2,5)); b3=set(range(2,40)); cor=sum(sorted(a3&b3)); assert cor==9
w_a=sum(set(range(-2,5))&set(range(1,40))); w_b=sum(set(range(-2,4))&set(range(2,40))); w_c=sum(a3); w_d=len(a3&b3)
assert (w_a,w_b,w_c,w_d)==(10,5,7,3)
SK=fig(nl_rows(-3,6,[('$A$',[(-2,4,True,True)],'blue'),('$B$',[(1,None,False,False)],'orange!85!black')],sx=0.62,dy=1.35))
q('0003',tipId='esz2-sistem',tip='Eşitsizlik sistemi ve kümeler',z='kolay',alt='Kesişimdeki Tam Sayılar',kaz='Sayı doğrusunda verilen iki kümenin kesişimini uçların dahil olma durumuna göre bulur.',kalip='şekilli',
 kart='K-AESZ2-07 (iki küme) · A = [−2, 4], B = (1, ∞); kesişimdeki tam sayıların toplamı',
 metin='Aşağıdaki sayı doğrularında A ve B kümeleri taralı olarak gösterilmiştir; içi dolu nokta o değerin kümeye ait olduğunu, içi boş nokta ait olmadığını belirtir.\n\nBuna göre A ∩ B kümesinin tam sayı elemanlarının toplamı kaçtır?',
 dogru=9,yan=[Y(10,'B kümesinin başlangıcındaki içi boş noktayı dolu gibi okuyup 1’i de saymış: 1 + 2 + 3 + 4.','dikkat'),Y(5,'A kümesinin 4’teki dolu noktasını boş gibi okuyup 4’ü dışarıda bırakmış: 2 + 3.','dikkat'),Y(7,'Yalnız A kümesine bakmış: −2 + (−1) + … + 4.','islem'),Y(3,'Toplam yerine kesişimdeki tam sayıların sayısını yazmış.','dikkat')],
 istenen='A ∩ B kümesindeki tam sayıların toplamı.',ip=['Kesişim, iki kümenin birlikte taralı olduğu bölgedir; uçlardaki noktaların türüne bak.'],bilgi=[SIS],sekil=SK,
 ad=[A('Kümeleri oku','A kapalı aralık, B ise 1’den büyük her sayıyı kapsıyor (1 dahil değil).','A = [−2, 4], B = (1, ∞)'),A('Kesişimi bul','İki kümenin birlikte taralı olduğu bölge.','A ∩ B = (1, 4]'),A('Tam sayıları topla','2, 3, 4 kesişimdedir.','2 + 3 + 4 = 9')],
 puf='Kesişimde uçları tek tek kontrol et.')

# =============== 04 · orta · ters mühendislik, sayı doğrusu ===============
r,u,v,s=-3,-1,2,5
a4,b4,c4,d4=-(r+s),r*s,-(u+v),u*v; cor=a4+b4+c4+d4; assert (a4,b4,c4,d4)==(-2,-15,-1,-2) and cor==-20
g1=lambda x:x*x+a4*x+b4<=0; g2=lambda x:x*x+c4*x+d4>=0
common=S(lambda x:g1(x) and g2(x),[-3,-1,2,5]); assert common=='[−3, −1] ∪ [2, 5]'
w_a=(r+s)+r*s+(u+v)+u*v; w_b=-(r+s)-r*s-(u+v)-u*v; w_c=a4+c4; w_d=(-(r+u)+(r*u))+(-(v+s)+v*s)
assert (w_a,w_b,w_c,w_d)==(-14,14,-3,10)
w_d=-(r+u)+r*u-(v+s)+v*s; assert w_d==(4+3)+(-7+10)
SK=fig(nl_rows(-4,6,[('',[(-3,-1,True,True),(2,5,True,True)],'blue')],sx=0.62))
q('0004',tipId='esz2-sistem',tip='Eşitsizlik sistemi ve kümeler',z='orta',alt='Sistemin Katsayıları',kaz='Eşitsizlik sisteminin ortak çözüm kümesinden her eşitsizliğin köklerini eşleyip katsayıları bulur.',kalip='şekilli',
 kart='K-AESZ2-06 (ters mühendislik) · ≤ 0 ve ≥ 0 iki eşitsizlik, ortak çözüm iki aralık',
 metin='a, b, c ve d gerçel sayılar olmak üzere,\n\nx² + ax + b ≤ 0\n\nx² + cx + d ≥ 0\n\neşitsizlik sisteminin çözüm kümesi şekildeki sayı doğrusunda taralı olarak gösterilmiştir.\n\nBuna göre, a + b + c + d toplamı kaçtır?',
 dogru=cor,yan=[Y(w_a,'Kök toplamlarının işaretini ters almış (a = r + s, c = u + v); çarpımlar doğru: 2 − 15 + 1 − 2.','islem'),Y(w_b,'Yalnız çarpımların işaretini ters almış (b = 15, d = 2); toplamlar doğru: −2 + 15 − 1 + 2.','islem'),Y(w_c,'Yalnız x’li terimlerin katsayılarını toplamış (a + c); sabit terimleri unutmuş.','dikkat'),Y(w_d,'İlk eşitsizliği soldaki iki uca, ikinciyi sağdaki iki uca ait sanmış: kökler (−3, −1) ve (2, 5) alınınca 4 + 3 − 7 + 10.','bilgi')],
 istenen='a + b + c + d toplamı.',ip=['Her eşitsizliğin çözümünün tek aralık mı, iki parça mı olduğuna bak.'],bilgi=[KOK,SIS],sekil=SK,
 ad=[A('Uçları eşle','x² + ax + b ≤ 0 çözümü kapalı tek aralıktır; bu aralığın uçları çözümün en dış uçlarıdır. x² + cx + d ≥ 0 çözümü kökler dışıdır; kökleri içteki uçlardır.','Birinci kökler: −3 ve 5 · ikinci kökler: −1 ve 2'),A('a ve b’yi bul','Kök toplamı −a, çarpımı b.','a = −2, b = −15'),A('c ve d’yi bul','Aynı kural.','c = −1, d = −2'),A('Topla','Dört katsayı toplanır.','−2 − 15 − 1 − 2 = −20')],
 puf='Ortak çözümün uçlarını hangi eşitsizliğin verdiğini belirle.')

# =============== 05 · orta · bölüm eşitsizliği ===============
f5=lambda x:(x*x-4*x-5)/(2-x)
c=tams(lambda x:f5(x)>=0,-3,6); assert c==[-3,-2,-1,3,4,5] and sum(c)==6
w_a=sum(tams(lambda x:f5(x)>=0,-3,6))+2; w_b=sum(tams(lambda x:f5(x)>=0 and x!=-1,-3,6)); w_c=sum(tams(lambda x:(x*x-4*x-5)/(x-2)>=0,-3,6)); w_d=sum(tams(lambda x:f5(x)>0 and x not in(5,),-3,6))
w_d=sum(tams(lambda x:f5(x)>0,-3,6));
assert (w_a,w_b,w_c)==(8,7,11)
dog=6
q('0005',tipId='esz2-bolum',tip='Bölüm eşitsizliği',z='orta',alt='Paydası Ters İşaretli Bölüm',kaz='Paydasındaki x’in katsayısı negatif olan bölüm eşitsizliğini işaret tablosuyla çözer ve verilen aralıktaki tam sayıları toplar.',kalip='düz',
 kart='K-AESZ2-08 (bölüm) · (x² − 4x − 5)/(2 − x) ≥ 0; aralıkta tam sayı toplamı',
 metin='x ∈ [−3, 6] olmak üzere,\n\n(x² − 4x − 5)/(2 − x) ≥ 0\n\neşitsizliğini sağlayan x tam sayılarının toplamı kaçtır?',
 dogru=6,yan=[Y(8,'Paydayı sıfır yapan x = 2 değerini de çözüme katmış; bölümde payda sıfır olamaz: 6 + 2.','dikkat'),Y(7,'Payın kökü x = −1’i “≥” olduğu hâlde dışarıda bırakmış: 6 − (−1).','dikkat'),Y(11,'Paydayı (x − 2) gibi alıp işareti ters başlatmış; çözümü [−1, 2) ∪ [5, 6] bulup −1 + 0 + 1 + 5 + 6 yazmış.','islem'),Y(w_d,'Payın köklerini (−1 ve 5) çözümden çıkarmış, yalnız “>” bölgelerini almış.','dikkat')],
 istenen='Eşitsizliği sağlayan tam sayıların toplamı.',ip=['Payın ve paydanın köklerini sırala; paydadaki x’in katsayısının işaretine dikkat ederek tabloyu kur.'],bilgi=[TAB,TAMB],
 ad=[A('Kökleri bul','Pay (x − 5)(x + 1); payda 2 − x.','x = −1, 5 (pay) ve x = 2 (payda)'),A('Tabloyu kur','x > 5 için pay +, payda − → bölüm −. Her tek katlı kökte işaret değişir.','(5, ∞): − · (2, 5): + · (−1, 2): − · (−∞, −1): +'),A('Çözümü yaz','Pay sıfır olabilir; payda sıfır olamaz.','(−∞, −1] ∪ (2, 5]'),A('[−3, 6]’daki tam sayıları topla','−3, −2, −1, 3, 4, 5','−6 + 12 = 6')],
 puf='Paydasında x’in katsayısı negatifse tabloya sağdan “−” ile başla; payda kökü hep “açık” kalır.')
assert w_d==sum([-3,-2,3,4]) and len({6,8,7,11,w_d})==5

# =============== 06 · orta · parabol ve doğru ===============
f6=lambda x:x*x-2*x-3; g6=lambda x:-x+3
assert f6(-2)==g6(-2)==5 and f6(3)==g6(3)==0
c=tams(lambda x:f6(x)<g6(x),-2,4); assert c==[-1,0,1,2] and sum(c)==2
w_a=sum(tams(lambda x:f6(x)<=g6(x),-2,4)); w_b=sum(tams(lambda x:f6(x)>g6(x),-2,4)); w_c=sum(tams(lambda x:f6(x)>=g6(x),-2,4)); w_d=sum(range(-2,5))
assert (w_a,w_b,w_c,w_d)==(3,4,5,7)
sx,sy=0.58,0.34
SK=fig('\n'.join([axes(-3,5,-4,7,sx,sy,xt=list(range(-3,6)),yt=list(range(-4,8))),curve(f6,-2,4,sx,sy,-5,8,'blue!70!black'),curve(g6,-2,4,sx,sy,-5,8,'orange!85!black'),dot(-2,5,sx,sy,'black'),dot(3,0,sx,sy,'black'),lab(4.05,5,sx,sy,'$f$','blue!70!black','right'),lab(4.05,-1.1,sx,sy,'$g$','orange!85!black','right')]))
q('0006',tipId='esz2-grafik',tip='Grafikle eşitsizlik',z='orta',alt='f(x) < g(x)',kaz='Bir parabol ile bir doğrunun grafiğinden f(x) < g(x) çözümünü okur ve verilen aralıktaki tam sayıları toplar.',kalip='grafik',
 kart='K-AESZ2-04 (parabol ve doğru) · kesişim noktaları ızgarada; [−2, 4] aralığında f < g',
 metin='Şekilde, [−2, 4] aralığında tanımlı f fonksiyonunun grafiği (mavi) ile g fonksiyonunun grafiği (turuncu) verilmiştir; grafikler ızgara çizgilerinin kesiştiği noktalarda birbirini kesmektedir.\n\nBuna göre f(x) < g(x) eşitsizliğini sağlayan x tam sayılarının toplamı kaçtır?',
 dogru=2,yan=[Y(w_a,'Grafiklerin kesiştiği iki x değerini de çözüme katmış (f(x) ≤ g(x) çözmüş): −2 − 1 + 0 + 1 + 2 + 3.','dikkat'),Y(w_b,'Yönü karıştırıp f(x) > g(x) bölgesini almış: x = 3’ten büyük, yani 4.','islem'),Y(w_c,'Eşitliğin sağlandığı x = −2’yi ve “f üstte” bölgeyi birlikte almış: f(x) ≥ g(x) → −2 + 3 + 4.','islem'),Y(w_d,'Aralığın tamamını çözüm sanmış: −2, −1, …, 4.','bilgi')],
 istenen='f(x) < g(x) eşitsizliğini sağlayan tam sayıların toplamı.',ip=['Mavi grafiğin turuncu grafiğin altında kaldığı x aralığını bul.'],bilgi=[GRF,TAMB],sekil=SK,
 ad=[A('Kesişimleri oku','İki grafik x = −2 ve x = 3 noktalarında kesişiyor.','f(−2) = g(−2) = 5, f(3) = g(3) = 0'),A('Altta olan bölgeyi bul','Ara bir noktada (x = 0) f(0) = −3, g(0) = 3; yani f altta.','−2 < x < 3'),A('Tam sayıları topla','−1, 0, 1, 2','−1 + 0 + 1 + 2 = 2')],
 puf='İki grafiği kıyaslarken kesişim noktalarını bulup ara bir değerde hangisinin altta kaldığına bak.')
assert len({2,w_a,w_b,w_c,w_d})==5

# =============== 07 · orta · öncüllü, sayı doğrusunda a,b,c ===============
import itertools
va=[Fi(-k,10) for k in range(1,10)]; vb=[Fi(k,10) for k in range(1,10)]; vc=[Fi(10+k,10) for k in range(1,10)]
tr=lambda p:[p(a,b,c) for a in va for b in vb for c in vc]
I7=tr(lambda a,b,c:a*c<a*b); II7=tr(lambda a,b,c:b*b<b); III7=tr(lambda a,b,c:a*b*c>0)
assert all(I7) and all(II7) and not any(III7)
SK=fig('\n'.join([nl_rows(-2,3,[('',[],'blue')],sx=0.9),dot(-0.6,0,0.9,1,'red!70!black').replace('circle (2.4pt)','circle (3pt)'),dot(0.4,0,0.9,1,'blue!70!black'),dot(1.6,0,0.9,1,'green!50!black'),lab(-0.6,0.1,0.9,1,'$a$','red!70!black','above'),lab(0.4,0.1,0.9,1,'$b$','blue!70!black','above'),lab(1.6,0.1,0.9,1,'$c$','green!50!black','above')]))
sira7=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
q('0007',tipId='esz2-oncul',tip='Sıralama ve öncüllü eşitsizlik',z='orta',alt='Sayı Doğrusunda Üç Sayı',kaz='Sayı doğrusundaki konumlarından a, b, c sayılarının işaret ve büyüklük ilişkilerini öncüllerle değerlendirir.',kalip='öncüllü',
 kart='K-AESZ2-10 (sayı doğrusu) · a ∈ (−1,0), b ∈ (0,1), c ∈ (1,2); I ve II doğru',
 metin='Aşağıdaki sayı doğrusunda a, b ve c gerçel sayılarına karşılık gelen noktalar gösterilmiştir.\n\nBuna göre,\n\nI. a · c < a · b\nII. b² < b\nIII. a · b · c > 0\n\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve II',yan=[Y('Yalnız I','I’i doğru bulmuş; b² < b için 0 < b < 1 olduğundan b’nin karesinin b’den küçük olduğunu görmemiş.','dikkat'),Y('Yalnız II','b² < b’yi doğru bulmuş; I’de negatif a ile çarparken c > b ilişkisinin yönünün değiştiğini fark etmemiş.','islem'),Y('I ve III','a · b · c çarpımında a negatif, b ve c pozitif olduğu hâlde çarpımı pozitif sanmış; II’yi de atlamış.','islem'),Y('II ve III','II’yi doğru bulmuş; III için “üç sayı çarpımı” işaretinde negatif sayıyı unutmuş, I’i de yanlış sanmış.','dikkat')],
 sira=sira7,istenen='Kesinlikle doğru olan öncüller.',ip=['Sayı doğrusundan a’nın negatif, b’nin 0 ile 1 arasında, c’nin 1’den büyük olduğunu oku.'],bilgi=[SRL,NOK],sekil=SK,
 ad=[A('Konumları oku','a negatif; b ile c pozitif; b < 1 < c.','a < 0 < b < 1 < c'),A('I’i incele','c > b olduğundan a ile çarpınca (a negatif) yön değişir.','a × c < a × b → doğru'),A('II ve III’ü incele','0 < b < 1 ise b’nin karesi b’den küçüktür. a negatif, b ve c pozitif → çarpım negatif.','b² < b doğru; a × b × c < 0 olduğundan III yanlış'),A('Sonuç','I ve II doğru.','I ve II')],
 puf='Negatifle çarpma ya da bölmede eşitsizlik yönü değişir; üç çarpandaki negatif sayı adedine bak.')

# =============== 08 · orta · mutlak değer ve ikinci derece sistemi ===============
s1=lambda x:abs(x-2)<4; s2=lambda x:x*x-2*x-3>=0
c=tams(lambda x:s1(x) and s2(x),-20,20); assert c==[-1,3,4,5] and len(c)==4
w_a=len(tams(lambda x:abs(x-2)<=4 and s2(x),-20,20)); w_b=len(tams(s1,-20,20)); w_c=len(tams(lambda x:s1(x) and x*x-2*x-3<=0,-20,20)); w_d=len(tams(lambda x:s1(x) and x*x-2*x-3>0,-20,20))
assert (w_a,w_b,w_c,w_d)==(6,7,5,2)
q('0008',tipId='esz2-tamsayi',tip='Çözüm kümesindeki tam sayılar',z='orta',alt='Mutlak Değer ve İkinci Derece',kaz='Mutlak değerli ve ikinci dereceden eşitsizliklerden oluşan sistemin çözümündeki tam sayıları sayar.',kalip='düz',
 kart='K-AESZ2-01 (sistem) · |x − 2| < 4 ve x² − 2x − 3 ≥ 0; tam sayı sayısı',
 metin='|x − 2| < 4\n\nx² − 2x − 3 ≥ 0\n\neşitsizlik sistemini sağlayan kaç tane x tam sayısı vardır?',
 dogru=4,yan=[Y(w_a,'Mutlak değerli eşitsizliği “≤” gibi çözüp −2 ve 6’yı da almış: −2, −1, 3, 4, 5, 6.','dikkat'),Y(w_b,'Yalnız mutlak değerli eşitsizliğe bakmış: −1, 0, …, 5.','islem'),Y(w_c,'İkinci eşitsizliği “≤ 0” gibi çözmüş: [−1, 3] ile (−2, 6) kesişimi −1, 0, 1, 2, 3.','islem'),Y(w_d,'İkinci eşitsizlikte “>” alıp kökleri −1 ve 3’ü dışarıda bırakmış: yalnız 4 ve 5 kalmış.','dikkat')],
 istenen='Sistemi sağlayan tam sayıların sayısı.',ip=['İki eşitsizliğin çözümlerini ayrı ayrı sayı doğrusunda göstermek işini kolaylaştırır.'],bilgi=[SIS,TAMB],
 ad=[A('Mutlak değeri çöz','|u| < 4 ⇔ −4 < u < 4.','−2 < x < 6'),A('İkinci eşitsizliği çöz','(x − 3)(x + 1) ≥ 0, kökler dahil.','x ≤ −1 veya x ≥ 3'),A('Kesiştir','(−2, 6) ile (−∞, −1] ∪ [3, ∞).','(−2, −1] ∪ [3, 6)'),A('Tam sayıları say','−1, 3, 4, 5','4 tane')],
 puf='Sistemde önce her eşitsizliği ayrı çöz, sonra yalnız ortak bölgedeki tam sayıları say.')
assert len({4,w_a,w_b,w_c,w_d})==5

# =============== 09 · orta · çerçeve (şekil) ===============
sc=0.3; xx=2
body=[f'\\fill[orange!30] (0,0) rectangle ({(12+2*xx)*sc},{(8+2*xx)*sc});',f'\\draw[thick,orange!70!black] (0,0) rectangle ({(12+2*xx)*sc},{(8+2*xx)*sc});',
 f'\\fill[white] ({xx*sc},{xx*sc}) rectangle ({(12+xx)*sc},{(8+xx)*sc});',f'\\draw[thick,blue!70!black] ({xx*sc},{xx*sc}) rectangle ({(12+xx)*sc},{(8+xx)*sc});',
 f'\\node[font=\\small,text=blue!70!black] at ({(6+xx)*sc},{(4+xx)*sc+0.35}) {{Resim}};',
 f'\\draw[{{Stealth}}-{{Stealth}}] ({xx*sc+0.15},{xx*sc+0.5}) -- ({(12+xx)*sc-0.15},{xx*sc+0.5}); \\node[font=\\small,fill=white,inner sep=1pt] at ({(6+xx)*sc},{xx*sc+0.5}) {{$12$ cm}};',
 f'\\draw[{{Stealth}}-{{Stealth}}] ({xx*sc+0.5},{xx*sc+0.15}) -- ({xx*sc+0.5},{(8+xx)*sc-0.15}); \\node[font=\\small,fill=white,inner sep=1pt,rotate=90] at ({xx*sc+0.5},{(4+xx)*sc-0.4}) {{$8$ cm}};',
 f'\\node[font=\\small] at ({(6+xx)*sc},{(8+xx)*sc+xx*sc/2}) {{$x$}};',f'\\node[font=\\small] at ({xx*sc/2},{(4+xx)*sc}) {{$x$}};',f'\\node[font=\\small] at ({(12+xx)*sc+xx*sc/2},{(4+xx)*sc}) {{$x$}};',f'\\node[font=\\small] at ({(6+xx)*sc},{xx*sc/2}) {{$x$}};']
SK=fig('\n'.join(body))
alan=lambda x:(12+2*x)*(8+2*x)-96; cev=lambda x:2*((12+2*x)+(8+2*x))
c=[x for x in range(1,40) if alan(x)>=96 and cev(x)<=88]; assert c==[2,3,4,5,6] and sum(c)==20
w_a=sum(x for x in range(1,40) if alan(x)>96 and cev(x)<=88); al2=lambda x:(12+x)*(8+x)-96; cv2=lambda x:2*((12+x)+(8+x))
w_b=sum(x for x in range(1,40) if al2(x)>=96 and cv2(x)<=88); w_c=sum(x for x in range(1,40) if cev(x)<=88); w_d=sum(x for x in range(1,40) if alan(x)>=96 and cev(x)<88)
assert (w_a,w_b,w_c,w_d)==(18,72,21,14)
q('0009',tipId='esz2-uygulama',tip='Eşitsizlikle model kurma',z='orta',alt='Çerçeve Problemi',kaz='Bir çerçeve problemini alan ve çevre koşullarıyla ikinci derece ve doğrusal eşitsizliğe çevirip tam sayı çözümlerini toplar.',kalip='hikâyeli',
 kart='K-AESZ2-11 (çerçeve) · alan ≥ 96 ve çevre ≤ 88; x tam sayı',
 metin='Bir atölyede, şekildeki dikdörtgen biçimli resmin dört kenarı boyunca eşit genişlikte, x cm kalınlığında bir çerçeve yapılacaktır. Çerçevenin alanının (çerçevenin kapladığı bölge, resim hariç) en az 96 cm² olması ve çerçeveli dikdörtgenin dış çevresinin en çok 88 cm olması istenmektedir.\n\nx bir pozitif tam sayı olduğuna göre, x’in alabileceği değerlerin toplamı kaçtır?',
 dogru=20,yan=[Y(w_a,'Alan koşulunu “>” almış; x = 2 için alan tam 96 olduğundan bu değer dışarıda kalmış: 3 + 4 + 5 + 6.','dikkat'),Y(w_b,'Çerçeveyi yalnız bir kenar boyunca x kadar saymış (boyutlar 12 + x ve 8 + x); koşullar x ≥ 4 ve x ≤ 12 çıkmış: 4 + 5 + … + 12.','islem'),Y(w_c,'Alan koşulunu unutup yalnız çevre koşuluna bakmış: 1 + 2 + … + 6.','dikkat'),Y(w_d,'Çevre koşulunu “<” almış; x = 6 için çevre tam 88 olduğundan dışarıda bırakmış: 2 + 3 + 4 + 5.','dikkat')],
 istenen='x’in alabileceği tam sayı değerlerinin toplamı.',ip=['Dış dikdörtgenin boyutlarını x cinsinden yaz.'],bilgi=[UYG,TAMB],sekil=SK,
 ad=[A('Boyutları yaz','Çerçeve her kenarda x kalınlığında olduğundan her boyut 2x artar.','Dış boyutlar: 12 + 2x ve 8 + 2x'),A('Alan koşulu','Dış alan − resim alanı ≥ 96.','(12 + 2x)(8 + 2x) − 96 ≥ 96 → x² + 10x − 24 ≥ 0 → x ≥ 2 (x > 0)'),A('Çevre koşulu','Dış çevre en çok 88.','2(20 + 4x) ≤ 88 → x ≤ 6'),A('Tam sayıları topla','2 ≤ x ≤ 6','2 + 3 + 4 + 5 + 6 = 20')],
 puf='Çerçeve problemlerinde dış boyut her kenardan değil, iki kenardan gelen 2x kadar artar.')

# =============== 10 · orta · parametre, her x için ===============
cond=lambda m:(m*m-4*(m+3))<0
c=[m for m in range(-30,30) if cond(m)]; assert c==list(range(-1,6)) and sum(c)==14
w_a=sum(m for m in range(-30,30) if m*m-4*(m+3)<=0); w_b=len(c); w_c=sum(m for m in range(1,30) if cond(m)); w_d=sum(m for m in range(-30,30) if (m-6)*(m-2)<0)
assert (w_a,w_b,w_c,w_d)==(18,7,15,12)
q('0010',tipId='esz2-parametre',tip='Parametreli eşitsizlik',z='orta',alt='Her x İçin',kaz='x² − mx + m + 3 > 0 eşitsizliğinin her x için sağlanması koşulundan m’nin tam sayı değerlerini bulur.',kalip='düz',
 kart='K-AESZ2-03 (Δ < 0) · x² − mx + m + 3 > 0 her x için; m tam sayı toplamı',
 metin='m bir tam sayı olmak üzere,\n\nx² − mx + m + 3 > 0\n\neşitsizliği her x gerçel sayısı için sağlanıyor.\n\nBuna göre m’nin alabileceği değerlerin toplamı kaçtır?',
 dogru=14,yan=[Y(w_a,'Δ ≤ 0 almış; Δ = 0 iken ifade bir noktada sıfır olur ve “>” sağlanmaz. −2’den 6’ya kadar toplamış.','dikkat'),Y(w_b,'Toplam yerine m’nin alabileceği değer sayısını yazmış.','dikkat'),Y(w_c,'Yalnız pozitif m değerlerini toplamış: 1 + 2 + 3 + 4 + 5.','dikkat'),Y(w_d,'Δ = m² − 4m − 12’yi (m − 6)(m − 2) diye çarpanlarına ayırmış; 3 + 4 + 5.','islem')],
 istenen='m’nin alabileceği tam sayı değerlerinin toplamı.',ip=['Parabolün x eksenine göre konumunu düşün.'],bilgi=[DEL,TAMB],
 ad=[A('Koşulu kur','Başkatsayı pozitif; her x için pozitif olması Δ < 0 demektir.','Δ = m² − 4(m + 3) < 0'),A('Δ’yı çarpanlarına ayır','m² − 4m − 12 = (m − 6)(m + 2).','(m − 6)(m + 2) < 0'),A('Çözüm aralığı','Kökler arasında negatif.','−2 < m < 6'),A('Tam sayıları topla','−1, 0, 1, 2, 3, 4, 5','14')],
 puf='“Her x için pozitif” koşulunda eşitlik (Δ = 0) durumu “>” için hep dışarıda kalır.')

# =============== 11 · zor · tam sayı çözümü verilen parametre ===============
def toplam_a(a): 
    s=[x for x in range(-40,41) if (x-a)*(x+4)<=0]; return sum(s)
A11=[a for a in range(-40,41) if toplam_a(a)==-4]; assert A11==[-4,3] and sum(A11)==-1
assert toplam_a(4)==0 and sum([3,4])==7
q('0011',tipId='esz2-parametre',tip='Parametreli eşitsizlik',z='zor',alt='Toplamı Verilen Tam Sayılar',kaz='Parametreli çarpım eşitsizliğinin tam sayı çözümlerinin toplamı verildiğinde parametrenin değerlerini iki durumu ayırarak bulur.',kalip='düz',
 kart='K-AESZ2-02 (iki durum) · (x − a)(x + 4) ≤ 0, tam sayı çözümlerin toplamı −4',
 metin='a bir tam sayı olmak üzere,\n\n(x − a)(x + 4) ≤ 0\n\neşitsizliğini sağlayan x tam sayılarının toplamı −4’tür.\n\nBuna göre, a’nın alabileceği değerlerin toplamı kaçtır?',
 dogru=-1,yan=[Y(3,'Yalnız a ≥ −4 durumunu düşünmüş: −4’ten a’ya kadar toplam −4 olan a = 3’ü bulmuş; a = −4 durumunu (tek çözüm x = −4) atlamış.','dikkat'),Y(-4,'Yalnız a = −4 durumunu (çözüm kümesi {−4}) düşünmüş; −4’ten 3’e kadar toplamın da −4 olduğunu görmemiş.','dikkat'),Y(0,'Toplamı −4 olan çözüm aralığının simetrik olduğunu varsayıp a = 4 ve a = −4 almış; [−4, 4]’ün toplamı −4 değil 0’dır.','bilgi'),Y(7,'[−4, 4] aralığında +4’ü toplamaya katmayı unutup toplamı −4 bulmuş, a = 4’ü de uygun sanarak 3 + 4 almış.','islem')],
 istenen='a’nın alabileceği değerlerin toplamı.',ip=['a’nın −4’ten büyük, küçük ya da eşit olmasına göre çözüm aralığının biçimini ayrı ayrı yaz.'],bilgi=[TAMB],
 ad=[A('Kökleri sırala','Kökler a ve −4; çözüm kökler arasındaki kapalı aralık.','a ≥ −4 ise [−4, a]; a < −4 ise [a, −4]'),A('a ≥ −4 durumu','−4’ten a’ya kadar tam sayıların toplamı −4 olmalı.','−4 − 3 − 2 − 1 + 0 + 1 + 2 + 3 = −4 → a = 3 · a = −4 için çözüm {−4}, toplam −4 → uygun'),A('a < −4 durumu','a’dan −4’e kadar toplam −4’ten küçük olur.','a + … + (−4) < −4 → uygun değer yok'),A('Toplamı bul','a ∈ {−4, 3}','−4 + 3 = −1')],
 puf='Parametre köklerden biriyse köklerin sırasına göre iki ayrı aralık yazıp ikisini de dene; çakışan kök özel durumdur.')
assert len({-1,3,-4,0,7})==5

# =============== 12 · zor · öncüllü sıralama ===============
vals=[Fi(k,4) for k in range(-24,25) if k!=0]
S12=[(x,y) for x in vals for y in vals if x*x*y<x<x*y]; assert S12
chk=lambda p:[p(x,y) for x,y in S12]
assert all(chk(lambda x,y:x<1)) and all(chk(lambda x,y:x*y>0)) and any(chk(lambda x,y:y>1)) and not all(chk(lambda x,y:y>1)) and S12
sira12=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
q('0012',tipId='esz2-oncul',tip='Sıralama ve öncüllü eşitsizlik',z='zor',alt='Zincir Eşitsizlik',kaz='x² · y < x < x · y zincir eşitsizliğinden x ve y için kesin çıkarımları öncüllerle değerlendirir.',kalip='öncüllü',
 kart='K-AESZ2-10 (zincir) · x²y < x < xy; I ve III doğru',
 metin='x ve y gerçel sayıları için\n\nx² · y < x < x · y\n\neşitsizliği veriliyor.\n\nBuna göre,\n\nI. x < 1\nII. y > 1\nIII. x · y > 0\n\nifadelerinden hangileri kesinlikle doğrudur?',
 dogru='I ve III',yan=[Y('Yalnız I','x < 1’i doğru bulmuş; x · y > x ve x < 1 bilgisiyle x · y’nin işaretini çıkaramamış.','dikkat'),Y('Yalnız III','x · y > 0’ı bulmuş, ancak x² · y < x eşitsizliğinden x < 1 çıkarımını yapmamış.','dikkat'),Y('I ve II','x pozitif durumunu düşünüp y > 1 bulmuş; x negatif durumunda y’nin negatif olduğunu (y > 1 sağlanmadığını) görmemiş.','islem'),Y('II ve III','x pozitif varsayıp y > 1 sonucunu genellemiş; x < 1 öncülünü de yanlış sanmış.','islem')],
 sira=sira12,istenen='Kesinlikle doğru olan öncüller.',ip=['x’in işareti hakkında ne söyleyebilirsin?'],bilgi=[SRL],
 ad=[A('x > 0 durumu','x > 0 ise eşitsizliğin her yanı x’e bölünür, yön değişmez.','xy < 1 < y → y > 1, x < 1/y < 1'),A('x < 0 durumu','x < 0 ise x’e bölününce yön değişir.','xy > 1 > y → y < 0 ve xy > 1; x < 1 yine sağlanır'),A('Öncülleri değerlendir','x < 1 iki durumda da doğru; x · y her iki durumda pozitif; y > 1 yalnız ilk durumda.','I ve III doğru, II bazen yanlış'),A('Sonuç','Kesinlikle doğru: I ve III.','I ve III')],
 puf='Çarpımlı zincirde değişkenin işareti bilinmiyorsa pozitif ve negatif durumları ayrı ayrı incele.')

# =============== 13 · zor · iki grafik, bölüm ===============
f13=lambda x:x*x-4; g13=lambda x:-x+1
c=tams(lambda x:f13(x)/g13(x)>=0 ,-3,3); assert c==[-3,-2,2] and len(c)==3
w_a=len(tams(lambda x:f13(x)*g13(x)>=0,-3,3)); w_b=len(tams(lambda x:f13(x)/g13(x)<=0,-3,3)); w_c=len(tams(lambda x:f13(x)/g13(x)>0,-3,3)); w_d=len(tams(lambda x:f13(x)>=0 and g13(x)>0,-3,3))
assert (w_a,w_b,w_c,w_d)==(4,5,1,2)
sx,sy=0.65,0.42
SK=fig('\n'.join([axes(-3,3,-4,5,sx,sy,xt=list(range(-3,4)),yt=list(range(-4,6))),curve(f13,-3,3,sx,sy,-5,6,'blue!70!black'),curve(g13,-3,3,sx,sy,-5,6,'orange!85!black'),dot(-2,0,sx,sy,'black'),dot(2,0,sx,sy,'black'),dot(1,0,sx,sy,'black'),lab(3.05,5,sx,sy,'$f$','blue!70!black','right'),lab(3.05,-2,sx,sy,'$g$','orange!85!black','right')]))
q('0013',tipId='esz2-grafik',tip='Grafikle eşitsizlik',z='orta',alt='Grafikle Bölüm Eşitsizliği',kaz='Grafikleri verilen iki fonksiyonun bölümünün işaretini aralıklara ayırıp paydanın sıfır olduğu noktayı dışarıda bırakarak tam sayıları sayar.',kalip='grafik',
 kart='K-AESZ2-04 (bölüm) · parabol ve doğru; f(x)/g(x) ≥ 0 tam sayı sayısı',
 metin='Şekilde, [−3, 3] aralığında tanımlı f fonksiyonunun grafiği (mavi) ile g fonksiyonunun grafiği (turuncu) verilmiştir; grafikler x eksenini ızgara çizgilerinin kesiştiği noktalarda kesmektedir.\n\nBuna göre,\n\nf(x)/g(x) ≥ 0\n\neşitsizliğini sağlayan kaç tane x tam sayısı vardır?',
 dogru=3,yan=[Y(w_a,'Bölüm yerine çarpıma bakmış (f(x) · g(x) ≥ 0); paydanın sıfır olduğu x = 1’i de saymış: −3, −2, 1, 2.','dikkat'),Y(w_b,'Yönü ters okumuş (f(x)/g(x) ≤ 0): −2, −1, 0, 2, 3.','islem'),Y(w_c,'Eşitlik durumunu atmış (f(x)/g(x) > 0): yalnız x = −3 kalmış.','dikkat'),Y(w_d,'Yalnız f ≥ 0 ve g > 0 bölgesini almış (−3, −2); (1, 2] aralığındaki iki negatif bölgeyi unutmuş.','islem')],
 istenen='f(x)/g(x) ≥ 0 eşitsizliğini sağlayan tam sayıların sayısı.',ip=['İki grafiğin işaretlerini aynı sayı doğrusunda aralık aralık yaz; paydanın sıfır olduğu yere dikkat et.'],bilgi=[TAB,GRF],sekil=SK,
 ad=[A('Kökleri oku','f x eksenini −2 ve 2’de, g x = 1’de kesiyor.','f: −2, 2 · g: 1'),A('İşaretleri belirle','f(x) > 0: x < −2 ya da x > 2; g(x) > 0: x < 1.','Tablo: x < −2 → (+, +); −2 < x < 1 → (−, +); 1 < x < 2 → (−, −); x > 2 → (+, −)'),A('Bölümün işaretini bul','Aynı işaretli bölgeler pozitif; f = 0 noktaları dahil, x = 1 değil.','(−∞, −2] ∪ (1, 2]'),A('[−3, 3]’teki tam sayıları say','−3, −2, 2','3 tane')],
 puf='Aralık aralık işaret tablosu kur.')
assert len({3,w_a,w_b,w_c,w_d})==5

# =============== 14 · zor · argümanı değişmiş fonksiyon, grafik ===============
f14=lambda x:Fi(1,2)*(x+2)*(x-4)
assert f14(0)==-4 and f14(-2)==0 and f14(4)==0
c=[x for x in range(-3,5) if f14(2*x-1)*(x-1)>=0]; assert c==[0,1,3,4]
w_a=len([x for x in range(-3,5) if f14(2*x-1)>=0]); w_b=len([x for x in range(-3,5) if f14(2*x-1)<=0]); w_c=len([x for x in range(-3,5) if f14(2*x-1)>=0 and x-1>=0]); w_d=len([x for x in range(-3,5) if f14(2*x-1)>=0 or x-1>=0])
assert (w_a,w_b,w_c,w_d)==(5,3,2,7)
sx,sy=0.55,0.4
SK=fig('\n'.join([axes(-3,5,-5,4,sx,sy,xt=list(range(-3,6)),yt=list(range(-5,5))),curve(f14,-3,5,sx,sy,-6,5,'blue!70!black'),dot(-2,0,sx,sy,'black'),dot(4,0,sx,sy,'black'),dot(0,-4,sx,sy,'black'),lab(4.3,2.2,sx,sy,'$f$','blue!70!black')]))
q('0014',tipId='esz2-grafik',tip='Grafikle eşitsizlik',z='zor',alt='f(2x − 1) · (x − 1)',kaz='Parabolün grafiğinden f(2x − 1) işaretini dönüştürüp (x − 1) çarpanıyla birlikte çarpım eşitsizliğinin tam sayı çözümlerini sayar.',kalip='grafik',
 kart='K-AESZ2-05 (argüman dönüşümü) · f(2x − 1) · (x − 1) ≥ 0; [−3, 4] aralığında tam sayı sayısı',
 metin='Şekilde, ikinci dereceden f fonksiyonunun grafiği verilmiştir; grafik, x eksenini ve y eksenini ızgara çizgilerinin kesiştiği noktalarda kesmektedir.\n\nBuna göre, x ∈ [−3, 4] olmak üzere,\n\nf(2x − 1) · (x − 1) ≥ 0\n\neşitsizliğini sağlayan kaç tane x tam sayısı vardır?',
 dogru=4,yan=[Y(w_a,'(x − 1) çarpanını unutup yalnız f(2x − 1) ≥ 0 çözmüş: x ≤ −1/2 ya da x ≥ 5/2 → −3, −2, −1, 3, 4.','dikkat'),Y(w_b,'Yalnız f(2x − 1) ≤ 0 bölgesini almış: −1/2 ≤ x ≤ 5/2 → 0, 1, 2; ikinci çarpanı ve x = 3, 4’ü yok saymış.','dikkat'),Y(w_c,'Çarpımı iki ayrı koşul gibi okumuş: f(2x − 1) ≥ 0 ve x − 1 ≥ 0 birlikte → 3, 4.','islem'),Y(w_d,'Çarpım yerine birleşim almış: f(2x − 1) ≥ 0 ya da x ≥ 1 → −3, −2, −1, 1, 2, 3, 4.','islem')],
 istenen='Eşitsizliği sağlayan tam sayıların sayısı.',ip=['f(2x − 1)’in sıfır olduğu x değerlerini bul.'],bilgi=[ARG,TAB],sekil=SK,
 ad=[A('f’nin işaretini oku','Kökler −2 ve 4; grafik bu ikisi arasında eksenin altında.','f(u) ≤ 0 ⇔ −2 ≤ u ≤ 4'),A('Argümanı dönüştür','u = 2x − 1 yazılır.','f(2x − 1) ≤ 0 ⇔ −1/2 ≤ x ≤ 5/2'),A('Çarpımı incele','(x − 1) için x = 1 kök. −1/2 < x < 1: (−)(−) = +; 1 < x < 5/2: (−)(+) = −; x > 5/2: (+)(+) = +; x < −1/2: (+)(−) = −.','Çözüm: [−1/2, 1] ∪ [5/2, ∞)'),A('[−3, 4]’teki tam sayıları say','0, 1, 3, 4','4 tane')],
 puf='f(g(x)) işaretini x için değil, g(x)’in aldığı değerler için f’nin grafiğinden okuyup sonra x’e dön.')
assert len({4,w_a,w_b,w_c,w_d})==5

# =============== 15 · zor · sadeleşen çarpan, çift kök ===============
f15=lambda x:(x*x+3*x+2)*(x-3)**2/(x*x-1)
c=tams(lambda x:f15(x)<=0,-4,4); assert c==[-2,0,3]
w_a=len(tams(lambda x:(x+2)*(x-3)**2/(x-1)<=0,-4,4)); w_b=len(tams(lambda x:f15(x)<=0 and x!=3,-4,4)); w_c=len([-2,-1,0,1,3]); w_d=len(tams(lambda x:f15(x)>=0,-4,4))
assert (w_a,w_b,w_c,w_d)==(4,2,5,6)
q('0015',tipId='esz2-bolum',tip='Bölüm eşitsizliği',z='zor',alt='Sadeleşen Çarpan ve Çift Kök',kaz='Sadeleşen çarpanı ve çift katlı kökü ayrı ayrı değerlendirerek bölüm eşitsizliğinin tam sayı çözümlerini sayar.',kalip='düz',
 kart='K-AESZ2-08 (sadeleşen çarpan, çift kök) · (x² + 3x + 2)(x − 3)²/(x² − 1) ≤ 0',
 metin='x ∈ [−4, 4] olmak üzere,\n\n(x² + 3x + 2)(x − 3)²/(x² − 1) ≤ 0\n\neşitsizliğini sağlayan kaç tane x tam sayısı vardır?',
 dogru=3,yan=[Y(w_a,'(x + 1) çarpanını sadeleştirip kökünü çözüm kümesinde bırakmış: x = −1’de payda sıfır olduğundan ifade tanımsızdır; −2, −1, 0, 3 saymış.','dikkat'),Y(w_b,'(x − 3)² çarpanının ifadeyi x = 3’te sıfır yaptığını görmeden yalnız [−2, 1) aralığına bakmış: −2, 0.','dikkat'),Y(w_c,'Paydanın iki kökünü de (−1 ve 1) çözüme katmış: −2, −1, 0, 1, 3.','dikkat'),Y(w_d,'Yönü ters alıp “≥ 0” bölgesini bulmuş: −4, −3, −2, 2, 3, 4.','islem')],
 istenen='Eşitsizliği sağlayan tam sayıların sayısı.',ip=['Pay ve paydayı çarpanlarına ayır.'],bilgi=[TAB,TAMB],
 ad=[A('Çarpanlara ayır','Pay (x + 1)(x + 2)(x − 3)²; payda (x − 1)(x + 1).','x ≠ 1 ve x ≠ −1'),A('Sadeleştir','(x + 1) sadeleşir ama x = −1 tanımsızdır.','(x + 2)(x − 3)²/(x − 1) ≤ 0, x ≠ ±1'),A('İşaret tablosu','(x − 3)² ≥ 0; sıfır değilken işareti belirleyen (x + 2)/(x − 1) ≤ 0 → −2 ≤ x < 1. Ayrıca x = 3’te ifade sıfırdır.','[−2, 1) ∪ {3}, x ≠ −1'),A('Tam sayıları say','−2, 0, 3','3 tane')],
 puf='Her kökü ayrı ayrı değerlendir.')
assert len({3,w_a,w_b,w_c,w_d})==5

# =============== 16 · zor · öncüllü işaret tablosu ===============
crit16=[-4,-1,2,5]
f16=lambda x:(x+4)*(x-2)**2*(x-5); g16=lambda x:(x+1)*(x-5)
def isaretler(fn,crit):
    mids=[crit[0]-1]+[Fi(crit[i]+crit[i+1],2) for i in range(len(crit)-1)]+[crit[-1]+1]
    return ['+' if fn(m)>0 else '−' for m in mids]
fs16=isaretler(f16,crit16); gs16=isaretler(g16,crit16)
assert fs16==['+','−','−','−','+'] and gs16==['+','+','−','−','+']
zr_f={i:'0' for i,cc in enumerate(crit16) if f16(cc)==0}; zr_g={i:'0' for i,cc in enumerate(crit16) if g16(cc)==0}
assert zr_f=={0:'0',2:'0',3:'0'} and zr_g=={1:'0',3:'0'}
SK=fig(sign_table(crit16,[('$f(x)$',fs16,zr_f),('$g(x)$',gs16,zr_g)]))
I16=S(lambda x:f16(x)*g16(x)<0,crit16); assert I16=='(−4, −1)'
II16=S(lambda x:g16(x)!=0 and f16(x)/g16(x)>=0,crit16); assert II16=='(−∞, −4] ∪ (−1, 5) ∪ (5, ∞)'
III16=[x for x in range(-20,21) if f16(x)*g16(x)<=0 and x>0]; assert III16==[2,5]
sira16=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
q('0016',tipId='esz2-tablo',tip='İşaret tablosundan çıkarım',z='zor',alt='İki Polinomun İşaret Tablosu',kaz='İki polinomun işaret tablosundan çarpım ve bölüm eşitsizliklerinin çözüm kümelerini yorumlar; çift katlı kök ve tanımsız noktayı ayırt eder.',kalip='öncüllü',
 kart='K-AESZ2-09 (tablo, çift kök) · çarpım < 0 açık aralık, bölüm ≥ 0, çarpım ≤ 0 pozitif tam sayılar',
 metin='Aşağıdaki tabloda f ve g polinomlarının x’in farklı aralıklarındaki işaretleri verilmiş, sıfır oldukları noktalar 0 ile belirtilmiştir.\n\nBuna göre,\n\nI. f(x) · g(x) < 0 eşitsizliğinin çözüm kümesi (−4, −1] aralığıdır.\nII. f(x)/g(x) ≥ 0 eşitsizliğinin çözüm kümesi ℝ − ((−4, −1] ∪ {5}) kümesidir.\nIII. f(x) · g(x) ≤ 0 eşitsizliğini sağlayan pozitif tam sayılar 2 ve 5’tir.\n\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',yan=[Y('Yalnız I','Çarpımın negatif olduğu aralığı doğru bulmuş ama x = −1’de g(x) = 0 olduğundan çarpımın sıfır olduğunu, “<” için dışarıda kalacağını görmemiş; II ve III’ü de yanlış sanmış.','dikkat'),Y('Yalnız II','II’yi doğru bulmuş; “≤ 0” için çift katlı kök x = 2’de ve x = 5’te çarpımın sıfır olduğunu, bu değerlerin çözüme girdiğini atlamış.','dikkat'),Y('I ve II','I’de uç x = −1’i dahil sanmış; III’te yalnız işaret değiştiren sıfırları aramış.','islem'),Y('I ve III','III’ü doğru bulmuş; I’de x = −1’de çarpımın sıfır olduğunu, II’de ise bölümün x = −1 ve x = 5’te tanımsız olduğunu görmemiş.','dikkat')],
 sira=sira16,istenen='Doğru olan öncüller.',ip=['Çarpımın ve bölümün işaretini her aralıkta tablodan çarparak bul; sıfır noktalarını ayrıca yaz.'],bilgi=[TAB],sekil=SK,
 ad=[A('Çarpımın işaretini bul','Aralıklarda f ve g’nin işaretleri çarpılır.','x < −4: + · (−4, −1): − · (−1, 2): + · (2, 5): + · x > 5: +'),A('I’i değerlendir','Çarpım yalnız (−4, −1) aralığında negatif; x = −1’de g = 0 olduğundan çarpım sıfırdır.','Çözüm (−4, −1) → I yanlış'),A('II’yi değerlendir','Bölüm: f = 0 olan x = −4 ve x = 2 dahil, g = 0 olan x = −1 ve x = 5 dışarıda; çarpım negatifken bölüm de negatif.','(−∞, −4] ∪ (−1, 5) ∪ (5, ∞) = ℝ − ((−4, −1] ∪ {5}) → II doğru'),A('III’ü değerlendir','Çarpım ≤ 0: (−4, −1) ve sıfır noktaları −4, −1, 2, 5; pozitif olanlar 2 ve 5 → III doğru.','II ve III doğru')],
 puf='Sıfır noktalarını çarpım ve bölüm için ayrı ayrı değerlendir.')
assert sorted(sira16)==sorted(['II ve III','Yalnız I','Yalnız II','I ve II','I ve III'])

# =============== 17 · orta · tablo, f'yi bulma, öncüllü ===============
f17=lambda x:x*x-2*x-8
assert (f17(0),f17(1),f17(3))==(-8,-9,-5)
a17=Fi(1)  # çözüm: f(0)=c, f(1)=a+b+c, f(3)=9a+3b+c
c17=-8; ab=-9-c17; a17=(-5-c17-3*ab)/Fi(6); b17=ab-a17; assert (a17,b17)==(1,-2)
I17=S(lambda x:f17(x)<0,[-2,4]); assert I17=='(−2, 4)'
II17=S(lambda x:f17(x)>=-8,[0,2]); assert II17=='(−∞, 0] ∪ [2, ∞)'
III17=all(f17(Fi(k,4))+9>0 for k in range(-40,40)); assert not III17 and f17(1)+9==0
SK=tablo_svg(['x','0','1','3'],[['f(x)','−8','−9','−5']])
sira17=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
q('0017',tipId='esz2-tablo',tip='İşaret tablosundan çıkarım',z='orta',alt='Tablodan Fonksiyon ve Eşitsizlik',kaz='Üç değeri tabloda verilen ikinci derece fonksiyonu bulup üç eşitsizliğin çözümünü öncüllerle değerlendirir.',kalip='öncüllü',
 kart='K-AESZ2-09 (tablodan f) · f(x) = x² − 2x − 8; üç öncül',
 metin='f(x) = ax² + bx + c ikinci dereceden bir fonksiyondur. Bu fonksiyonun bazı x değerleri için aldığı değerler aşağıdaki tabloda verilmiştir.\n\nBuna göre,\n\nI. f(x) < 0 eşitsizliğinin çözüm kümesi (−2, 4) aralığıdır.\nII. f(x) ≥ −8 eşitsizliğinin çözüm kümesi [0, 2] aralığıdır.\nIII. f(x) + 9 > 0 eşitsizliği her x gerçel sayısı için sağlanır.\n\nifadelerinden hangileri doğrudur?',
 dogru='Yalnız I',yan=[Y('Yalnız II','f(x) ≥ −8 için x² − 2x ≥ 0 çözerken kökleri 0 ve 2 bulup köklerin arasını almış; “≥ 0” için kökler dışının alınması gerektiğini atlamış.','islem'),Y('I ve II','I’i doğru bulmuş; II’de aralığın kökler arası mı dışı mı olduğunu karıştırmış.','islem'),Y('I ve III','I’i doğru bulmuş; III’te f(1) + 9 = 0 olduğunu, “> 0” için x = 1’in sağlamadığını görmemiş.','dikkat'),Y('I, II ve III','Üç öncülde de kökleri bulup işareti kontrol etmeden doğru kabul etmiş.','dikkat')],
 sira=sira17,istenen='Doğru olan öncüller.',ip=['Tablodaki üç değerle a, b ve c’yi bul; sonra her öncülü ayrı ayrı çöz.'],bilgi=[TAMB,DEL],sekil=SK,
 ad=[A('c’yi bul','x = 0 için f(0) = c.','c = −8'),A('a ve b’yi bul','f(1) = a + b − 8 = −9 ve f(3) = 9a + 3b − 8 = −5.','a + b = −1, 3a + b = 1 → a = 1, b = −2'),A('I ve II’yi çöz','x² − 2x − 8 < 0 → (x − 4)(x + 2) < 0 → (−2, 4) doğru. x² − 2x − 8 ≥ −8 → x(x − 2) ≥ 0 → x ≤ 0 ya da x ≥ 2; [0, 2] yanlış.','I doğru, II yanlış'),A('III’ü çöz','f(x) + 9 = x² − 2x + 1 = (x − 1)² ≥ 0; x = 1’de sıfır olduğundan “> 0” her x için sağlanmaz.','III yanlış → Yalnız I')],
 puf='Tabloda verilen üç noktadan ikinci derece fonksiyonu bulmak için önce x = 0 değerinden c’yi oku.')

# =============== 18 · orta · sayı doğrusu, A ve B kümeleri ===============
A18=lambda x:(-4<=x<-1) or (1<x<=6); B18=lambda x:x*x-3*x-10<=0
c=tams(lambda x:A18(x) and B18(x),-20,20); assert c==[-2,2,3,4,5] and len(c)==5
w_a=len(tams(lambda x:((-4<=x<=-1) or (1<=x<=6)) and B18(x),-20,20)); w_b=len(tams(lambda x:A18(x) and x*x-3*x-10<0,-20,20)); w_c=len(tams(lambda x:A18(x) or B18(x),-20,20)); w_d=len(tams(lambda x:1<x<=5,-20,20))
assert (w_a,w_b,w_c,w_d)==(7,3,11,4)
SK=fig(nl_rows(-5,7,[('$A$',[(-4,-1,True,False),(1,6,False,True)],'blue')],sx=0.55))
q('0018',tipId='esz2-sistem',tip='Eşitsizlik sistemi ve kümeler',z='orta',alt='Sayı Doğrusu ve Eşitsizlik',kaz='Sayı doğrusunda verilen küme ile ikinci dereceden eşitsizlikle tanımlı kümenin kesişimindeki tam sayıları sayar.',kalip='şekilli',
 kart='K-AESZ2-07 (sayı doğrusu ve eşitsizlik) · A iki aralık, B = {x : x² − 3x − 10 ≤ 0}',
 metin='Aşağıdaki sayı doğrusunda taralı bölge A kümesini göstermektedir; içi dolu nokta o değerin kümeye ait olduğunu, içi boş nokta ait olmadığını belirtir.\n\nB = {x : x² − 3x − 10 ≤ 0, x ∈ ℝ}\n\nolduğuna göre, A ∩ B kümesinin kaç tane tam sayı elemanı vardır?',
 dogru=5,yan=[Y(w_a,'A kümesinin uçlarındaki içi boş noktaları dolu gibi okuyup −1 ve 1’i de saymış: −2, −1, 1, 2, 3, 4, 5.','dikkat'),Y(w_b,'B kümesini “< 0” gibi çözüp uç noktaları −2 ve 5’i dışarıda bırakmış: yalnız 2, 3, 4.','dikkat'),Y(w_c,'Kesişim yerine birleşimi bulup −4’ten 6’ya kadar tüm tam sayıları saymış.','islem'),Y(w_d,'A’nın yalnız sağdaki parçasını almış; (1, 5] aralığındaki 2, 3, 4, 5’i bulup −2’yi atlamış.','dikkat')],
 istenen='A ∩ B kümesindeki tam sayıların sayısı.',ip=['B kümesinin çözümünü de sayı doğrusuna taşıyıp A ile birlikte taralı bölgeyi bul.'],bilgi=[SIS,TAMB],sekil=SK,
 ad=[A('A’yı oku','İki parçalı: −4 dahil, −1 dahil değil; 1 dahil değil, 6 dahil.','A = [−4, −1) ∪ (1, 6]'),A('B’yi çöz','(x − 5)(x + 2) ≤ 0, uçlar dahil.','B = [−2, 5]'),A('Kesişimi bul','Ortak taralı bölge.','A ∩ B = [−2, −1) ∪ (1, 5]'),A('Tam sayıları say','−2, 2, 3, 4, 5','5 tane')],
 puf='Kesişimde her parçanın uçlarını ayrı ayrı kontrol et; küçük uç B’den, büyük uç A’dan gelebilir.')
assert len({5,w_a,w_b,w_c,w_d})==5

# =============== 19 · zor · tablo + sistem (f·g ≥ 0 ve f/g ≤ 0) ===============
crit19=[-3,0,3,5,6]
f19=lambda x:(x+3)*x*(x-3)**2*(x-6); g19=lambda x:x*(x-5)
fs19=isaretler(f19,crit19); gs19=isaretler(g19,crit19)
zr_f19={i:'0' for i,cc in enumerate(crit19) if f19(cc)==0}; zr_g19={i:'0' for i,cc in enumerate(crit19) if g19(cc)==0}
assert zr_f19=={0:'0',1:'0',2:'0',4:'0'} and zr_g19=={1:'0',3:'0'}
SK=fig(sign_table(crit19,[('$f(x)$',fs19,zr_f19),('$g(x)$',gs19,zr_g19)]))
ok19=lambda x:g19(x)!=0 and f19(x)*g19(x)>=0 and f19(x)/g19(x)<=0
c=[x for x in range(-20,21) if ok19(x)]; assert c==[-3,3,6]
w_a=len([x for x in range(-20,21) if f19(x)==0]); w_b=len({x for x in range(-20,21) if f19(x)==0 or g19(x)==0}); w_c=len([x for x in range(-20,21) if f19(x)==0])+len([x for x in range(-20,21) if g19(x)==0]); w_d=len([x for x in range(-20,21) if ok19(x) and f19(x-1+1)*0==0 and (x!=3)])
assert (w_a,w_b,w_c,w_d)==(4,5,6,2)
q('0019',tipId='esz2-tablo',tip='İşaret tablosundan çıkarım',z='zor',alt='Çarpım ve Bölüm Sistemi',kaz='İşaret tablosundan çarpım ve bölüm eşitsizliklerinin ortak çözümünün yalnız payın sıfırlarından oluştuğunu görür; ortak sıfır ve çift katlı kökü ayırt eder.',kalip='tablo',
 kart='K-AESZ2-09 (sistem) · f·g ≥ 0 ve f/g ≤ 0; ortak sıfır, çift katlı kök',
 metin='İki polinom fonksiyon olan f ve g’nin işaret tablosu şekilde verilmiştir; tabloda 0, ilgili fonksiyonun o noktada (işaret değiştirmese bile) sıfır olduğunu gösterir.\n\nBuna göre,\n\nf(x) · g(x) ≥ 0\n\nf(x)/g(x) ≤ 0\n\neşitsizlik sisteminin çözüm kümesinin kaç tane elemanı vardır?',
 dogru=3,yan=[Y(w_a,'Çözümü f’nin dört sıfırı sanmış; x = 0’da g(x) = 0 olduğundan bölüm tanımsızdır, bu değer çözüme girmez.','dikkat'),Y(w_b,'f ve g’nin sıfırlarının hepsini (ortak sıfır bir kez) çözüm kümesi sanmış.','dikkat'),Y(w_c,'Sıfırların toplam sayısını yazmış: f’nin 4, g’nin 2 sıfırı.','islem'),Y(w_d,'Yalnız işaretin değiştiği sıfırları aramış; çift katlı kök x = 3’te f(x) = 0 olduğunu, bu değerin sistemi sağladığını atlamış.','dikkat')],
 istenen='Çözüm kümesinin eleman sayısı.',ip=['İki eşitsizliği aynı anda sağlayan x değerlerinde bölümün ve çarpımın işareti ne olmalı?'],bilgi=[TAB,SIS],sekil=SK,
 ad=[A('Sistemi yorumla','f/g ≤ 0 ise f ve g zıt işaretli ya da f = 0; f·g ≥ 0 ise aynı işaretli ya da biri sıfır. İkisi birlikte yalnız f(x) = 0 iken (ve g(x) ≠ 0) sağlanabilir.','Çözüm: f(x) = 0 ve g(x) ≠ 0'),A('f’nin sıfırlarını oku','Tabloda f’nin sıfır olduğu yerler (çift katlı x = 3 dahil).','x = −3, 0, 3, 6'),A('g’nin sıfırlarını çıkar','x = 0’da g(x) = 0 olduğundan bölüm tanımsız.','x = 0 çözüm değil'),A('Say','−3, 3, 6','3 eleman')],
 puf='İki eşitsizliği aynı x için birlikte yorumla.')
assert len({3,w_a,w_b,w_c,w_d})==5

# =============== 20 · orta · tablo, talep ===============
talep=lambda p:120-10*p
assert (talep(4),talep(6),talep(8))==(80,60,40)
c=[p for p in range(1,13) if p*talep(p)>=350 and talep(p)<=60]; assert c==[6,7] and sum(c)==13
w_a=sum(p for p in range(1,13) if p*talep(p)>=350); w_b=sum(p for p in range(1,13) if p*talep(p)>=350 and talep(p)>=60); w_c=sum(p for p in range(1,13) if p*talep(p)>350 and talep(p)<=60); w_d=sum(p for p in range(1,13) if p*talep(p)>=350 and talep(p)<60)
assert (w_a,w_b,w_c,w_d)==(18,11,6,7)
SK=tablo_svg(['Birim fiyat (TL)','4','6','8'],[['Günlük satış (adet)','80','60','40']])
q('0020',tipId='esz2-uygulama',tip='Eşitsizlikle model kurma',z='orta',alt='Fiyat, Talep ve Hasılat',kaz='Tabloda verilen doğrusal talep ilişkisinden hasılat ve stok koşullarını eşitsizliğe çevirip tam sayı fiyatları bulur.',kalip='tablo',
 kart='K-AESZ2-11 (talep) · hasılat ≥ 350 ve satış ≤ 60; fiyat tam sayı',
 metin='Bir kırtasiyede bir defterin günlük satış adedi, birim fiyatı arttıkça doğrusal biçimde azalmaktadır. Üç farklı birim fiyat için günlük satış adedi aşağıdaki tabloda verilmiştir.\n\nBirim fiyat p TL (p bir tam sayı), günlük hasılat p ile satış adedinin çarpımıdır. Günlük hasılatın en az 350 TL olması ve günlük satış adedinin en çok 60 olması isteniyor.\n\nBuna göre p’nin alabileceği değerlerin toplamı kaçtır?',
 dogru=13,yan=[Y(w_a,'Satış adedi koşulunu unutup yalnız hasılat koşuluna bakmış: 5 + 6 + 7.','dikkat'),Y(w_b,'Satış adedi koşulunu ters yorumlayıp “en az 60” almış: p ≤ 6 → 5 + 6.','islem'),Y(w_c,'Hasılat koşulunu “>” almış; p = 5 ve p = 7’de hasılat tam 350 olduğundan bu değerler dışarıda kalmış: yalnız 6.','dikkat'),Y(w_d,'Satış adedi koşulunu “<” almış; p = 6 için satış tam 60 olduğundan dışarıda bırakmış: yalnız 7.','dikkat')],
 istenen='p’nin alabileceği tam sayı değerlerinin toplamı.',ip=['Tablodaki üç noktanın bir doğru üzerinde olduğunu kullan.'],bilgi=[UYG],sekil=SK,
 ad=[A('Talep doğrusunu bul','Fiyat 2 TL artınca satış 20 azalıyor.','satış = 120 − 10p'),A('Hasılat koşulu','p(120 − 10p) ≥ 350 → p² − 12p + 35 ≤ 0','(p − 5)(p − 7) ≤ 0 → 5 ≤ p ≤ 7'),A('Satış koşulu','120 − 10p ≤ 60','p ≥ 6'),A('Kesiştir ve topla','6 ≤ p ≤ 7','6 + 7 = 13')],
 puf='Tablodaki üç noktanın doğrusal olduğunu kontrol edip ilişkiyi p cinsinden yazmak modeli kurmanın ilk adımıdır.')
assert len({13,w_a,w_b,w_c,w_d})==5

# ---------- bitir ----------
from collections import Counter
for qq in P.ANA: qq['kardes']=None
assert len(P.ANA)==20
HD=os.path.dirname(os.path.abspath(__file__))
json.dump(P.ANA,open(os.path.join(HD,'esitsiziki-1.json'),'w'),ensure_ascii=False,indent=1)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu='Eşitsizlikler',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 10–12. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HD,'..','kartlar','esitsiziki.json'),'w'),ensure_ascii=False,indent=1)
print('harf',sorted(Counter(x['cevap']['sik'] for x in P.ANA).items()),'zorluk',dict(Counter(x['zorluk'] for x in P.ANA)),'tip',len(tipler),'şekilli',sum(1 for x in P.ANA if x['sekil']),'öncüllü',sum(1 for x in P.ANA if x['kalip']=='öncüllü'))
