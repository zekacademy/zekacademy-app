"""Denklem Çözme · parti 1: 8 ana + 8 kardeş. Her cevap ve çeldirici kodla yeniden çözülür."""
import sys,os
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
P=Parti('denklem','Denklem Çözme','mat|Denklem Çözme')
TT=lambda **k:k
def coz(f,ara=None):
    """f(x) = 0 olan değerler (kesirli arama)"""
    ara=ara or [Fr(n,d) for d in (1,2,3,5,7) for n in range(-400,401)]
    return sorted(set(x for x in ara if f(x)==0))
DAG=B('Dağılma','parantezin önündeki sayı içerideki her terimle çarpılır. Örnek: −3(x − 5) = −3x + 15')
ISR=B('İşaret kuralı','eksi × eksi = artı, eksi × artı = eksi. Örnek: (−3) × (−5) = 15 · (−2) × 4 = −8')
KOKU=B('Denklemin çözümü (kökü)','denklemi sağlayan x değeridir; yerine konunca eşitlik doğru olur. Örnek: 2x − 1 = 5 için x = 3 çözümdür, çünkü 2 × 3 − 1 = 5')
YOK=B('Yok etme yöntemi','denklemleri uygun sayılarla çarpıp taraf tarafa toplayınca bir bilinmeyen gider. Örnek: x + y = 5 ve x − y = 1 ⇒ 2x = 6')
TTI=B('Taraf tarafa işlem','eşitlikler taraf tarafa toplanıp çıkarılabilir. Örnek: a + b = 7 ve b + c = 5 ⇒ (a + b) − (b + c) = a − c = 2')
AXB=B('ax = b denkleminin çözümü','a ≠ 0 ise tek çözüm x = b ÷ a · a = 0 ve b = 0 ise her x çözüm · a = 0 ve b ≠ 0 ise çözüm yok (boş küme). Örnek: 0 × x = 5 hiçbir x için sağlanmaz')

# ===== 0001 KOLAY dn-dogrusal (K-DN-01)
assert coz(lambda x:4*(x-3)-3*(x-5)-11)==[8] and 4*5-3*3==11
assert coz(lambda x:(4*x-3)-3*(x-5)-11)==[-1] and coz(lambda x:x-3-11)==[14] and coz(lambda x:4*x-12-3*x+5-11)==[18] and coz(lambda x:4*x-12-3*x-15-11)==[38]
P.R('0001','dn-dogrusal','Birinci dereceden denklem çözme','kolay','Parantezli Denklem','Parantezli birinci dereceden denklemi dağılma ve işaret kurallarıyla çözer.','düz',2,
 'K-DN-01 (parantez açma, eksi katsayı) · yeni katsayılar',
 '4(x − 3) − 3(x − 5) = 11\ndenkleminde x kaçtır?',
 ['−1','8','14','18','38'],'B','Denklemin çözümü.',
 ['Önce iki parantezi aç; −3’ü iki terimle de çarp.','(−3) × (−5) kaç eder?','Benzer terimleri topla, sabiti karşıya geçir.'],[DAG,ISR],
 [A('Parantezleri aç','4 ve −3, parantezdeki her terimle çarpılır.','4x − 12 − 3x + 15 = 11'),
  A('Benzer terimler','4x − 3x = x, −12 + 15 = 3.','x + 3 = 11'),
  A('Çöz ve kontrol et','3’ü karşıya eksi olarak geçir.','x = 8 · kontrol: 4 × 5 − 3 × 3 = 20 − 9 = 11 ✓')],
 'Eksi katsayılı parantezi açarken her terimin işaretini değiştir: −3(x − 5) = −3x + 15.',
 dict(A='−1, 4(x − 3)’ü 4x − 3 yazmak; 4, −3 ile de çarpılmalı.',C='14, x + 3 = 11’de 3’ü karşıya artı geçirmek.',D='18, −3(x − 5)’i −3x + 5 yazmak; −3, −5 ile de çarpılmalı.',E='38, −3(x − 5)’i −3x − 15 yazmak; eksi × eksi = artı.'),
 TT(A='bilgi',C='islem',D='bilgi',E='islem'))
assert coz(lambda x:2*(x+7)-3*(x-2)-9)==[11] and 2*18-3*9==9
assert coz(lambda x:2*x+14-3*x-6-9)==[-1] and coz(lambda x:2*x+7-3*x+6-9)==[4] and coz(lambda x:2*x+14-3*x+2-9)==[7]
P.K('0001','2(x + 7) − 3(x − 2) = 9\neşitliğini sağlayan x değeri kaçtır?',
 ['−11','−1','4','7','11'],'E','Denklemin çözümü.',
 ['İki parantezi de aç.','−3 × (−2) işaretine dikkat.','−x’li bir denklem çıkarsa son adımda işareti kontrol et.'],[DAG,ISR],
 [A('Parantezleri aç','2 ve −3 her terimle çarpılır.','2x + 14 − 3x + 6 = 9'),
  A('Benzer terimler','2x − 3x = −x, 14 + 6 = 20.','−x + 20 = 9 ⇒ −x = −11'),
  A('Çöz ve kontrol et','İki tarafı −1 ile çarp.','x = 11 · kontrol: 2 × 18 − 3 × 9 = 36 − 27 = 9 ✓')],
 '−x = −11 gibi bir sonuçta iki tarafı −1 ile çarpmayı unutma.',
 dict(A='−11, −x = −11’de eksiyi atmayı unutmak; x = 11.',B='−1, −3(x − 2)’yi −3x − 6 yazmak; eksi × eksi = artı.',C='4, 2(x + 7)’yi 2x + 7 yazmak; 2, 7 ile de çarpılmalı.',D='7, −3(x − 2)’yi −3x + 2 yazmak; −3, −2 ile de çarpılmalı.'),
 TT(A='islem',B='islem',C='bilgi',D='bilgi'))

# ===== 0002 KOLAY dn-parametre (K-DN-03)
f=lambda a,x:(a+2)*x-3*a-14
assert coz(lambda a:f(a,4))==[6]
assert coz(lambda a:a+8-14)==[6] and -6==8-14 and coz(lambda a:a+2*4-3*a-14)==[-3] and coz(lambda a:4*a+2-3*a-14)==[12] and 14+8==22
P.R('0002','dn-parametre','Kök ve çözüm kümesi koşulları','kolay','Verilen Kök','Çözümü verilen denklemde x yerine koyarak parametreyi bulur.','düz',2,
 'K-DN-03 (kök verilip katsayı istenmesi) · parametre parantez içinde',
 'x = 4 değeri\n(a + 2)x − 3a = 14\ndenkleminin bir çözümü olduğuna göre a kaçtır?',
 ['−6','−3','6','12','22'],'C','a’nın değeri.',
 ['“x = 4 çözüm” ne demek? x yerine 4 yaz.','(a + 2) × 4’ü dağıt.','a’lı terimleri topla, a’yı yalnız bırak.'],[KOKU,DAG],
 [A('Yerine koy','x = 4 denklemi sağlar.','(a + 2) × 4 − 3a = 14'),
  A('Dağıt ve topla','4a + 8 − 3a = 14.','a + 8 = 14'),
  A('Çöz','8’i karşıya geçir.','a = 6 · kontrol: 8 × 4 − 18 = 14 ✓')],
 'Kökü verilen denklemde önce x’i yerine koy; geriye yalnız parametreli basit bir denklem kalır.',
 dict(A='−6, a + 8 = 14’te a = 8 − 14 yazmak; 8 karşıya eksi geçer: a = 14 − 8.',B='−3, (a + 2)x’i a + 2x gibi okumak; x, parantezin tamamıyla çarpılır.',D='12, (a + 2) × 4’ü 4a + 2 yazmak; 4, 2 ile de çarpılmalı.',E='22, 8’i karşıya artı geçirmek: 14 + 8.'),
 TT(A='islem',B='bilgi',D='bilgi',E='islem'))
g=lambda a,x:(a-4)*x+2*a-11
assert coz(lambda a:g(a,-3))==[1] and g(1,-3)==0
assert coz(lambda a:-3*a-12+2*a-11)==[-23] and coz(lambda a:-3*a-4+2*a-11)==[-15] and coz(lambda a:-5*a+12-11)==[Fr(1,5)]
P.K('0002','x = −3,\n(a − 4)x + 2a = 11\ndenklemini sağladığına göre a kaçtır?',
 ['−23','−15','−1','1/5','1'],'E','a’nın değeri.',
 ['x yerine −3 yaz.','(a − 4) × (−3)’ü dağıtırken iki işarete de dikkat.','a’lı terimleri topla: −3a + 2a kaç eder?'],[KOKU,DAG,ISR],
 [A('Yerine koy','x = −3 denklemi sağlar.','(a − 4) × (−3) + 2a = 11'),
  A('Dağıt','(−3) × a = −3a ve (−3) × (−4) = +12.','−3a + 12 + 2a = 11 ⇒ −a + 12 = 11'),
  A('Çöz','−a = −1.','a = 1 · kontrol: (−3) × (−3) + 2 = 11 ✓')],
 'Negatif bir kök yerine konduğunda her çarpımın işaretini ayrı ayrı yaz.',
 dict(A='−23, (−3) × (−4)’ü −12 almak; eksi × eksi = artı.',B='−15, (a − 4)x’i ax − 4 yazmak; x, −4 ile de çarpılmalı.',C='−1, −a = −1’de eksiyi bir tarafta bırakmak; a = 1.',D='1/5, −3a + 2a’yı −5a hesaplamak; −3a + 2a = −a.'),
 TT(A='islem',B='bilgi',C='islem',D='islem'))

# ===== 0003 ORTA dn-sistem (K-DN-05)
v=[(x,y) for x in range(-30,31) for y in range(-30,31) if 5*x-2*y==4 and 3*x+4*y==18]; assert v==[(2,3)]
assert 2+3==5 and 2*3==6 and 2+(-3)==-1
P.R('0003','dn-sistem','Denklem sistemleri','orta','İki Bilinmeyenli Sistem','İki bilinmeyenli denklem sistemini yok etme yöntemiyle çözer ve istenen ifadeyi hesaplar.','düz',3,
 'K-DN-05 (yok etme yöntemi) · katsayı eşitleme gerekiyor, istenen x + y',
 '5x − 2y = 4\n3x + 4y = 18\nolduğuna göre x + y toplamı kaçtır?',
 ['−1','2','3','5','6'],'D','x + y toplamı.',
 ['y’nin katsayıları −2 ve 4; birini öbürünün tersi yapacak çarpanı bul.','İlk denklemi 2 ile çarpıp ikinciyle topla.','x’i bulunca bir denklemde yerine koy.'],[YOK],
 [A('Katsayıyı eşitle','İlk denklemi 2 ile çarp; y’nin katsayısı −4 olur.','10x − 4y = 8'),
  A('Taraf tarafa topla','−4y ile +4y gider.','10x − 4y + 3x + 4y = 8 + 18 ⇒ 13x = 26 ⇒ x = 2'),
  A('y’yi bul','İlk denklemde x = 2 yaz.','10 − 2y = 4 ⇒ −2y = −6 ⇒ y = 3'),
  A('Sonuç','İstenen toplam.','x + y = 2 + 3 = 5')],
 'Yok etmede katsayıları zıt işaretli yapacak en küçük çarpanı seç; sonunda sorulan ifadeye dön.',
 dict(A='−1, −2y = −6’dan y = −3 bulmak; eksi bölü eksi artıdır.',B='2, x’in değeri; soru x + y’yi soruyor.',C='3, y’nin değeri; soru x + y’yi soruyor.',E='6, x × y’nin değeri; soru toplamı soruyor.'),
 TT(A='islem',B='dikkat',C='dikkat',E='dikkat'))
v=[(x,y) for x in range(-30,31) for y in range(-30,31) if 3*x+5*y==1 and 2*x-3*y==7]; assert v==[(2,-1)] and 2*(-1)==-2 and 2+(-1)==1 and 2-(-1)==3
P.K('0003','3x + 5y = 1\n2x − 3y = 7\ndenklem sistemine göre x · y çarpımı kaçtır?',
 ['−2','−1','1','2','3'],'A','x × y çarpımı.',
 ['x’in katsayılarını eşitlemek için denklemleri hangi sayılarla çarparsın?','İlkini 2, ikincisini 3 ile çarp; sonra çıkar.','y’yi bulunca x’e geç; işaretlere dikkat.'],[YOK],
 [A('Katsayıyı eşitle','x’in katsayıları 6 olsun.','6x + 10y = 2 · 6x − 9y = 21'),
  A('Taraf tarafa çıkar','6x’ler gider; 10y − (−9y) = 19y.','19y = 2 − 21 = −19 ⇒ y = −1'),
  A('x’i bul','İlk denklemde y = −1 yaz.','3x − 5 = 1 ⇒ x = 2'),
  A('Sonuç','İstenen çarpım.','x × y = 2 × (−1) = −2')],
 'Taraf tarafa çıkarırken ikinci denklemin her teriminin işaretini değiştir: −(−9y) = +9y.',
 dict(B='−1, y’nin değeri; soru x × y’yi soruyor.',C='1, x + y’nin değeri; soru çarpımı soruyor.',D='2, x’in değeri; soru x × y’yi soruyor.',E='3, x − y’nin değeri; soru çarpımı soruyor.'),
 TT(B='dikkat',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0004 ORTA dn-terazi (K-DN-07)
def terazi_iki(s1,s2,ek1=None,ek2=None):
    """s1, s2: (sol, sağ) listeleri; öğe 'U' (üçgen), 'D' (daire), 'K' (kare) ya da '450 g' gibi ağırlık"""
    b=[]
    def oge(x,y,o):
        if o=='U': return f'<path d="M{x-8} {y} L{x} {y-15} L{x+8} {y} Z" stroke-width="1.4" style="stroke:{G.ACC};fill:{G.ACC}" fill-opacity=".35"/>',19
        if o=='D': return f'<circle cx="{x}" cy="{y-8}" r="7.5" stroke-width="1.4"/>',19
        if o=='K': return f'<rect x="{x-7.5}" y="{y-15}" width="15" height="15" stroke-width="1.4" style="fill:currentColor" fill-opacity=".2"/>',19
        return f'<rect x="{x-21}" y="{y-18}" width="42" height="18" rx="3" stroke-width="1.4"/>'+G._t(x,y-5,o,size=10,bold=True),46
    def kefe(cx,y,liste):
        g=[oge(0,0,o)[1] for o in liste]; x=cx-sum(g)/2; s=''
        for o,w in zip(liste,g): s+=oge(x+w/2,y,o)[0]; x+=w
        return s
    for i,(sol,sag) in enumerate([s1,s2]):
        ox=12+i*236; cx=ox+106; y=70
        b.append(f'<path d="M{cx-13} 104 L{cx} {y+2} L{cx+13} 104 Z" stroke-width="1.4"/>')
        b.append(f'<line x1="{ox}" y1="{y}" x2="{ox+212}" y2="{y}" stroke-width="2.4"/>')
        for px in (ox+48,ox+164): b.append(f'<line x1="{px-44}" y1="{y-3}" x2="{px+44}" y2="{y-3}" stroke-width="1" opacity=".5"/>')
        b.append(kefe(ox+48,y-4,sol)); b.append(kefe(ox+164,y-4,sag))
        b.append(G._t(cx,122,f'Şekil {i+1}',size=11))
        e=[ek1,ek2][i]
        if e: b.append(G._t(cx,140,e,size=11,bold=True,renk=G.ACC))
    return G._svg(484,148 if (ek1 or ek2) else 132,''.join(b))
U,D=Fr(300),Fr(200); assert 2*U+D==4*D and U+3*D==900
v=[(u,d) for u in range(1,1000) for d in range(1,1000) if 2*u+d==4*d and u+3*d==900]; assert v==[(300,200)]
assert 900//4==225 and [(u,d) for u in range(1,1000) for d in range(1,1000) if u==3*d and u+3*d==900]==[(450,150)] and 300+200==500
P.R('0004','dn-terazi','Terazi ve şekille denklem kurma','orta','Terazi','Dengedeki terazilerden denklem kurar, ortak nesneleri sadeleştirerek nesnelerin kütlesini bulur.','şekilli',3,
 'K-DN-07 (iki terazi, oran + toplam) · üçgen ve daire bloklar, ağırlık 900 g',
 'Özdeş üçgen bloklar ve özdeş daire bloklar ile kurulan aşağıdaki eşit kollu teraziler dengededir. Terazilerin kendi kütleleri önemsizdir.\nŞekil 1’de sol kefede 2 üçgen ve 1 daire, sağ kefede 4 daire; Şekil 2’de sol kefede 1 üçgen ve 3 daire, sağ kefede 900 gramlık bir ağırlık vardır.\nBuna göre bir üçgen bloğun kütlesi kaç gramdır?',
 ['200','225','300','450','500'],'C','Bir üçgen bloğun kütlesi.',
 ['Dengede iki kefedeki kütleler eşittir; Şekil 1’i denklem olarak yaz.','İki kefede de bulunan daireyi iki taraftan at.','Bulduğun ilişkiyi Şekil 2’de kullan.'],[B('Dengedeki terazi','eşit kollu terazi dengedeyse iki kefedeki toplam kütleler eşittir; iki kefeden aynı nesne atılınca denge bozulmaz')],
 [A('Şekil 1’i yaz','Üçgen u, daire d gram olsun; birer daireyi iki kefeden at.','2u + d = 4d ⇒ 2u = 3d ⇒ u = 3d ÷ 2'),
  A('Şekil 2’yi yaz','Sol kefe 900 grama eşit.','u + 3d = 900 ⇒ 3d ÷ 2 + 3d = 900 ⇒ 9d ÷ 2 = 900 ⇒ d = 200'),
  A('Üçgeni bul','u = 3 × 200 ÷ 2.','u = 300 · kontrol: 300 + 600 = 900 ✓',terazi_iki((['U','U','D'],['D','D','D','D']),(['U','D','D','D'],['900 g']),'2u = 3d','u = 300 g · d = 200 g'))],
 'Terazide iki kefede ortak olan nesneleri at; kalan eşitlik nesneler arasındaki oranı verir.',
 dict(A='200, bir dairenin kütlesi; soru üçgeni soruyor.',B='225, üçgen ile daireyi eşit kütleli sanıp 900 ÷ 4 almak.',D='450, 2u = 3d’den u = 3d yazmak; 2’ye bölmek unutulmuş.',E='500, bir üçgen ile bir dairenin toplamı.'),
 TT(A='dikkat',B='bilgi',D='islem',E='dikkat'),sekil=terazi_iki((['U','U','D'],['D','D','D','D']),(['U','D','D','D'],['900 g'])))
v=[(k,d) for k in range(1,500) for d in range(1,500) if 3*k==k+4*d and 2*k+d==450]; assert v==[(180,90)]
assert [d for d in range(1,500) if 2*(4*d)+d==450]==[50] and 450//3==150 and 180+90==270
P.K('0004','Özdeş kare bloklar ve özdeş daire bloklar ile kurulan aşağıdaki eşit kollu teraziler dengededir. Terazilerin kendi kütleleri önemsizdir.\nŞekil 1’de sol kefede 3 kare, sağ kefede 1 kare ve 4 daire; Şekil 2’de sol kefede 2 kare ve 1 daire, sağ kefede 450 gramlık bir ağırlık vardır.\nBuna göre bir daire bloğun kütlesi kaç gramdır?',
 ['50','90','150','180','270'],'B','Bir daire bloğun kütlesi.',
 ['Şekil 1’de iki kefede de kare var; birer kareyi at.','Kalan eşitlikten bir karenin kaç daireye denk olduğunu bul.','Şekil 2’de kareleri daire cinsinden yaz.'],[B('Dengedeki terazi','eşit kollu terazi dengedeyse iki kefedeki toplam kütleler eşittir; iki kefeden aynı nesne atılınca denge bozulmaz')],
 [A('Şekil 1’i yaz','Kare k, daire d gram; birer kareyi iki kefeden at.','3k = k + 4d ⇒ 2k = 4d ⇒ k = 2d'),
  A('Şekil 2’yi yaz','Kareleri daire cinsinden yaz.','2k + d = 450 ⇒ 4d + d = 450 ⇒ 5d = 450'),
  A('Daireyi bul','5’e böl.','d = 90 · k = 180 · kontrol: 360 + 90 = 450 ✓',terazi_iki((['K','K','K'],['K','D','D','D','D']),(['K','K','D'],['450 g']),'k = 2d','d = 90 g · k = 180 g'))],
 'Önce nesneler arasındaki oranı bul (k = 2d), sonra her şeyi tek nesne cinsinden yaz.',
 dict(A='50, 2k = 4d’den k = 4d yazmak; iki tarafı 2’ye bölmek unutulmuş.',C='150, kare ile daireyi eşit kütleli sanıp 450 ÷ 3 almak.',D='180, bir karenin kütlesi; soru daireyi soruyor.',E='270, bir kare ile bir dairenin toplamı.'),
 TT(A='islem',C='bilgi',D='dikkat',E='dikkat'),sekil=terazi_iki((['K','K','K'],['K','D','D','D','D']),(['K','K','D'],['450 g'])))

# ===== 0005 ORTA dn-hikaye (K-DN-08)
v=[p for p in range(0,71) if 15*p+20*(70-p)==1200]; assert v==[40] and 70-40==30 and 70//2==35 and 1200//20==60 and 1200//15==80
P.R('0005','dn-hikaye','Sözel durumdan denklem kurma','orta','Adet ve Tutar','Toplam adet ve toplam tutar verilen iki ürün için tek bilinmeyenli denklem kurup çözer.','hikâyeli',3,
 'K-DN-08 (toplam adet + toplam tutar) · yeni kurgu (fırın), istenen ucuz ürün',
 'Bir fırında poğaçanın tanesi 15 TL, açmanın tanesi 20 TL’dir. Bu fırın bir sabah yalnızca poğaça ve açma satmış; toplam 70 ürün satarak 1200 TL kazanmıştır.\nBuna göre bu sabah kaç poğaça satılmıştır?',
 ['30','35','40','60','80'],'C','Satılan poğaça sayısı.',
 ['Poğaça sayısına p dersen açma sayısı ne olur?','Toplam tutarı p cinsinden yaz.','Bulduğun sayının poğaçaya mı açmaya mı ait olduğunu kontrol et.'],[DAG],
 [A('Bilinmeyeni seç','Toplam 70 ürün var.','poğaça = p · açma = 70 − p'),
  A('Denklemi kur','Toplam tutar 1200 TL.','15p + 20 × (70 − p) = 1200 ⇒ 15p + 1400 − 20p = 1200'),
  A('Çöz ve kontrol et','−5p = −200.','p = 40 · kontrol: 40 × 15 + 30 × 20 = 600 + 600 = 1200 ✓')],
 'İki ürünlü adet-tutar sorularında birine x de, öbürünü “toplam − x” yaz; tek bilinmeyen yeter.',
 dict(A='30, açma sayısı; soru poğaça sayısını soruyor.',B='35, iki üründen eşit sayıda satıldığını varsaymak; tutar koşulu kullanılmamış.',D='60, 1200’ü açma fiyatına bölmek; tüm ürünler açma değil.',E='80, 1200’ü poğaça fiyatına bölmek; toplam ürün 70.'),
 TT(A='dikkat',B='dikkat',D='islem',E='islem'),
 kisa='Hepsi açma olsaydı 70 × 20 = 1400 TL olurdu; 200 TL eksik ve her poğaça 5 TL eksik getirir: 200 ÷ 5 = 40.')
v=[t for t in range(0,51) if 12*(50-t)+18*t==744]; assert v==[24] and 50-24==26 and 144//12==12 and 744//12==62
P.K('0005','Bir kırtasiyede kurşun kalemin tanesi 12 TL, tükenmez kalemin tanesi 18 TL’dir. Bir okul bu kırtasiyeden yalnızca bu iki çeşit kalemden toplam 50 tane alıp 744 TL ödemiştir.\nBuna göre okul kaç tükenmez kalem almıştır?',
 ['12','24','25','26','62'],'B','Alınan tükenmez kalem sayısı.',
 ['Tükenmez kalem sayısına t dersen kurşun kalem sayısı kaç olur?','Toplam ödemeyi t cinsinden yaz.','Bulduğun sayı hangi kaleme ait?'],[DAG],
 [A('Bilinmeyeni seç','Toplam 50 kalem.','tükenmez = t · kurşun = 50 − t'),
  A('Denklemi kur','Toplam ödeme 744 TL.','12 × (50 − t) + 18t = 744 ⇒ 600 + 6t = 744'),
  A('Çöz ve kontrol et','6t = 144.','t = 24 · kontrol: 26 × 12 + 24 × 18 = 312 + 432 = 744 ✓')],
 'Pahalı ürünün sayısı, fazladan ödenen tutarın fiyat farkına bölümüdür.',
 dict(A='12, 144’ü fiyat farkı 6 yerine 12’ye bölmek.',C='25, iki çeşitten eşit sayıda alındığını varsaymak.',D='26, kurşun kalem sayısı; soru tükenmez kalemi soruyor.',E='62, 744’ü kurşun kalem fiyatına bölmek; tümü kurşun kalem değil.'),
 TT(A='islem',C='dikkat',D='dikkat',E='islem'),
 kisa='Hepsi kurşun kalem olsaydı 50 × 12 = 600 TL olurdu; 144 TL fazla ve her tükenmez 6 TL fazla: 144 ÷ 6 = 24.')

# ===== 0006 ORTA dn-dogrusal (K-DN-02)
assert coz(lambda x:(x+1)/3-(x-2)/4-2)==[14] and Fr(15,3)-Fr(12,4)==2
assert coz(lambda x:4*(x+1)-3*(x-2)-2)==[-8] and coz(lambda x:4*x+1-3*x+6-24)==[17] and coz(lambda x:4*x+4-3*x-6-24)==[26] and coz(lambda x:x-10-24)==[34]
P.R('0006','dn-dogrusal','Birinci dereceden denklem çözme','orta','Kesirli Denklem','Paydaları EKOK ile eşitleyerek kesirli birinci dereceden denklemi çözer.','düz',3,
 'K-DN-02 (paydaları eşitleme) · iki kesirli terim ve sabit',
 '(x + 1)/3 − (x − 2)/4 = 2\nolduğuna göre x kaçtır?',
 ['−8','14','17','26','34'],'B','Denklemin çözümü.',
 ['3 ve 4’ün EKOK’u kaç? Her terimi onunla çarp.','Sağdaki 2’yi de çarpmayı unutma.','Payları parantez içinde tut; eksiyi iki terime de dağıt.'],[B('Paydaları eşitleme','her terim paydaların EKOK’u ile çarpılır. Örnek: x/2 + x/3 = 5 ⇒ 3x + 2x = 30'),DAG],
 [A('Paydalardan kurtul','EKOK(3, 4) = 12; her terimi 12 ile çarp.','4(x + 1) − 3(x − 2) = 24'),
  A('Parantezleri aç','−3 × (−2) = +6.','4x + 4 − 3x + 6 = 24'),
  A('Çöz ve kontrol et','x + 10 = 24.','x = 14 · kontrol: 15/3 − 12/4 = 5 − 3 = 2 ✓')],
 'Paydaları eşitlerken eşitliğin iki tarafındaki her terimi aynı sayıyla çarp.',
 dict(A='−8, sağdaki 2’yi 12 ile çarpmamak: x + 10 = 2.',C='17, 4(x + 1)’i 4x + 1 yazmak; 4, 1 ile de çarpılmalı.',D='26, −3(x − 2)’yi −3x − 6 yazmak; eksi × eksi = artı.',E='34, x + 10 = 24’te 10’u karşıya artı geçirmek.'),
 TT(A='bilgi',C='bilgi',D='islem',E='islem'))
assert coz(lambda x:(2*x-1)/5-(x-3)/2-1)==[3] and Fr(5,5)-Fr(0,2)==1
assert coz(lambda x:4*x-2-5*x-15-10)==[-27] and coz(lambda x:4*x-1-5*x+15-10)==[4] and coz(lambda x:4*x-2-5*x+15-1)==[12]
P.K('0006','(2x − 1)/5 − (x − 3)/2 = 1\ndenklemini sağlayan x kaçtır?',
 ['−27','−3','3','4','12'],'C','Denklemin çözümü.',
 ['5 ve 2’nin EKOK’u kaç?','Her terimi (sağdaki 1 dahil) EKOK ile çarp.','−5’i ikinci parantezin iki terimine de dağıt.'],[B('Paydaları eşitleme','her terim paydaların EKOK’u ile çarpılır. Örnek: x/2 + x/3 = 5 ⇒ 3x + 2x = 30'),DAG],
 [A('Paydalardan kurtul','EKOK(5, 2) = 10.','2(2x − 1) − 5(x − 3) = 10'),
  A('Parantezleri aç','−5 × (−3) = +15.','4x − 2 − 5x + 15 = 10 ⇒ −x + 13 = 10'),
  A('Çöz ve kontrol et','−x = −3.','x = 3 · kontrol: 5/5 − 0/2 = 1 ✓')],
 'Kesirli denklemde payı parantez içine al; çarpım tüm paya dağılır.',
 dict(A='−27, −5(x − 3)’ü −5x − 15 yazmak; eksi × eksi = artı.',B='−3, −x = −3’te eksiyi atmayı unutmak.',D='4, 2(2x − 1)’i 4x − 1 yazmak; 2, −1 ile de çarpılmalı.',E='12, sağdaki 1’i 10 ile çarpmamak: −x + 13 = 1.'),
 TT(A='islem',B='islem',D='bilgi',E='bilgi'))

# ===== 0007 ZOR dn-sistem (K-DN-06)
cozler=[(a,b,c,d) for a in range(0,11) for b in range(0,11) for c in range(0,14) for d in range(0,10) if a+b==10 and b+c==13 and c+d==9]
assert cozler and {a+d for a,b,c,d in cozler}=={6} and len(cozler)>1
assert 10+13+9==32 and 32//2==16 and 13+9-10==12 and 6//2==3
P.R('0007','dn-sistem','Denklem sistemleri','zor','Zincir Toplamlar','Bilinmeyen sayısı denklemden fazla olan sistemde istenen toplamı taraf tarafa işlemle bulur.','hikâyeli',4,
 'K-DN-06 (ikili toplamlardan istenen toplam) · dört kişi zincir biçiminde, tek tek değerler bulunamaz',
 'Ali, Berk, Can ve Deniz’in her birinin bir miktar bilyesi vardır.\nAli ile Berk’in bilyelerinin toplamı 10,\nBerk ile Can’ın bilyelerinin toplamı 13,\nCan ile Deniz’in bilyelerinin toplamı 9’dur.\nBuna göre Ali ile Deniz’in bilyelerinin toplamı kaçtır?',
 ['3','6','12','16','32'],'B','Ali ile Deniz’in bilyelerinin toplamı.',
 ['Dört bilinmeyen, üç denklem var; herkesi tek tek bulmak zorunda mısın?','a + d’yi elde etmek için hangi denklemleri toplayıp hangisini çıkarmalısın?','b ve c’nin yok olmasını sağla.'],[TTI],
 [A('Denklemleri yaz','Ali a, Berk b, Can c, Deniz d bilye.','a + b = 10 · b + c = 13 · c + d = 9'),
  A('Planı kur','Dört bilinmeyen ve üç denklem olduğu için kişiler tek tek bulunamaz; a + d doğrudan elde edilmeli.','(a + b) − (b + c) + (c + d) = a + d'),
  A('Hesapla','b ve c sadeleşir.','10 − 13 + 9 = 6'),
  A('Kontrol','Örneğin a = 4, b = 6, c = 7, d = 2 ya da a = 3, b = 7, c = 6, d = 3; ikisinde de a + d = 6.','a + d = 6')],
 'Bilinmeyenleri tek tek bulamıyorsan istenen ifadeyi denklemlerin toplamı ve farkı olarak yazmaya çalış.',
 dict(A='3, 6’yı ikiye bölüp bir kişinin bilyesini bulmaya çalışmak; soru toplamı soruyor.',C='12, (b + c) + (c + d) − (a + b) hesaplamak; bu a + d değil, 2c + d − a verir.',D='16, üç toplamı toplayıp ikiye bölmek; bu kalıp yalnızca üç kişinin ikişerli toplamlarında işe yarar.',E='32, üç toplamı toplamak; b ve c iki kez sayılır.'),
 TT(A='dikkat',C='islem',D='bilgi',E='islem'))
cozler=[(k,l,m,n) for k in range(0,22) for l in range(0,16) for m in range(0,16) for n in range(0,19) if k+l==21 and l+m==15 and m+n==18]
assert cozler and {k+n for k,l,m,n in cozler}=={24} and len(cozler)>1 and 21+15+18==54 and 54//2==27 and 15+18-21==12 and 21-15==6
P.K('0007','Yan yana dizilmiş K, L, M ve N kutularının her birinde bir miktar kalem vardır.\nK ve L kutularındaki kalemlerin toplamı 21,\nL ve M kutularındaki kalemlerin toplamı 15,\nM ve N kutularındaki kalemlerin toplamı 18’dir.\nBuna göre K ve N kutularındaki kalemlerin toplamı kaçtır?',
 ['6','12','24','27','54'],'C','K ve N kutularındaki kalemlerin toplamı.',
 ['Dört bilinmeyenin her birini bulmak gerekmiyor.','K + N’yi elde etmek için hangi toplamları ekleyip hangisini çıkarmalısın?','L ve M’nin sadeleşmesini sağla.'],[TTI],
 [A('Denklemleri yaz','Kutulardaki kalemler k, l, m, n.','k + l = 21 · l + m = 15 · m + n = 18'),
  A('Planı kur','Kutular tek tek bulunamaz; istenen toplamı doğrudan oluştur.','(k + l) − (l + m) + (m + n) = k + n'),
  A('Hesapla','l ve m sadeleşir.','21 − 15 + 18 = 24'),
  A('Kontrol','Örneğin k = 10, l = 11, m = 4, n = 14 ya da k = 12, l = 9, m = 6, n = 12; ikisinde de k + n = 24.','k + n = 24')],
 'Zincir biçimindeki ikili toplamlarda uçtakilerin toplamı: birinci − ikinci + üçüncü.',
 dict(A='6, yalnızca 21 − 15 hesaplamak; bu k − m’dir, m + n eklenmeli.',B='12, (l + m) + (m + n) − (k + l) hesaplamak; bu 2m + n − k verir.',D='27, üç toplamı toplayıp ikiye bölmek; bu kalıp üç kutunun ikişerli toplamlarında geçerlidir.',E='54, üç toplamı toplamak; l ve m iki kez sayılır.'),
 TT(A='dikkat',B='islem',D='bilgi',E='islem'))
assert 4+6==10 and 6+7==13 and 7+2==9 and 3+7==10 and 7+6==13 and 6+3==9 and 10+11==21 and 11+4==15 and 4+14==18 and 12+9==21 and 9+6==15 and 6+12==18

# ===== 0008 ZOR dn-parametre (K-DN-04)
def durum(k,s):
    return 'tek' if k!=0 else ('her' if s==0 else 'yok')
v=[a for a in range(-50,51) if durum(a*a-9,a*a-3*a)=='yok']; assert v==[-3]
assert durum(0,9-9)=='her' and durum(-9,0)=='tek' and 9+9==18
P.R('0008','dn-parametre','Kök ve çözüm kümesi koşulları','zor','Boş Küme','Parametreli birinci dereceden denklemde katsayı ve sabitin durumuna göre çözüm kümesinin boş olduğu değeri bulur.','düz',4,
 'K-DN-04 (ax = b’de a = 0, b ≠ 0) · katsayı ve sabit parametreye bağlı, sonsuz çözüm tuzağı',
 'a bir gerçel sayı olmak üzere, x’e bağlı\n(a² − 9)x = a² − 3a\ndenkleminin çözüm kümesi boş küme olduğuna göre a kaçtır?',
 ['−3','0','3','9','18'],'A','Çözüm kümesini boş yapan a değeri.',
 ['ax = b biçimindeki bir denklemin hiç çözümü olmaması için a ve b ne olmalı?','x’in katsayısını sıfır yapan a değerlerini bul; iki tane var.','Her biri için sağ tarafı hesapla: 0 mı, değil mi?'],[AXB,B('Karesi verilen sayı','a² = 9 ise a = 3 ya da a = −3; iki değer de kontrol edilmeli')],
 [A('Boş küme koşulu','Hiç çözüm yoksa x’in katsayısı 0, sağ taraf 0’dan farklı olmalı.','a² − 9 = 0 ve a² − 3a ≠ 0'),
  A('Katsayıyı sıfırla','a² = 9.','a = 3 ya da a = −3'),
  A('Sağ tarafı dene','a = 3: sağ taraf 9 − 9 = 0 ⇒ 0 × x = 0, her x çözüm. a = −3: sağ taraf 9 + 9 = 18 ⇒ 0 × x = 18, çözüm yok.','a = 3 olmaz · a = −3 olur'),
  A('Sonuç','Boş kümeyi veren tek değer.','a = −3')],
 'Katsayıyı sıfır yapan her değeri sağ tarafta da dene: sağ taraf 0 ise sonsuz çözüm, değilse boş küme.',
 dict(B='0, sağ tarafın 0 olmasını koşul sanmak; a = 0 için −9x = 0 ⇒ x = 0 tek çözüm.',C='3, a = 3 için 0 × x = 0 olur; her gerçel sayı çözümdür, küme boş değildir.',D='9, a² = 9’dan a = 9 bulmak; karesi 9 olan sayılar 3 ve −3’tür.',E='18, a = −3 için sağ tarafın değeri; soru a’yı soruyor.'),
 TT(B='bilgi',C='bilgi',D='islem',E='dikkat'))
v=[a for a in range(-50,51) if durum(a*a-16,a*a+4*a)=='yok']; assert v==[4]
assert durum(0,16-16)=='her' and durum(-16,0)=='tek' and 16+16==32
P.K('0008','a bir gerçel sayı olmak üzere, x’e bağlı\n(a² − 16)x = a² + 4a\ndenkleminin hiçbir gerçel çözümü olmadığına göre a kaçtır?',
 ['−16','−4','0','4','16'],'D','Denklemi çözümsüz yapan a değeri.',
 ['Çözüm olmaması için x’in katsayısı ve sağ taraf nasıl olmalı?','a² − 16 = 0’ı sağlayan iki değeri bul.','Her biri için sağ taraftaki ifadeyi hesapla.'],[AXB,B('Karesi verilen sayı','a² = 16 ise a = 4 ya da a = −4; iki değer de kontrol edilmeli')],
 [A('Çözümsüzlük koşulu','x’in katsayısı 0, sağ taraf 0’dan farklı.','a² − 16 = 0 ve a² + 4a ≠ 0'),
  A('Katsayıyı sıfırla','a² = 16.','a = 4 ya da a = −4'),
  A('Sağ tarafı dene','a = −4: 16 − 16 = 0 ⇒ her x çözüm. a = 4: 16 + 16 = 32 ⇒ 0 × x = 32, çözüm yok.','a = −4 olmaz · a = 4 olur'),
  A('Sonuç','Çözümsüzlüğü veren değer.','a = 4')],
 '0 × x = 0 sonsuz çözüm, 0 × x = (sıfırdan farklı sayı) çözümsüzlük demektir.',
 dict(A='−16, a² = 16’dan a = −16 bulmak; karesi 16 olan sayılar 4 ve −4’tür.',B='−4, a = −4 için 0 × x = 0 olur; her gerçel sayı çözümdür.',C='0, sağ tarafın 0 olmasını koşul sanmak; a = 0 için −16x = 0 ⇒ x = 0 bir çözümdür.',E='16, a² = 16’dan a = 16 bulmak; karekök alınmalı.'),
 TT(A='islem',B='bilgi',C='bilgi',E='islem'))

P.yaz(os.path.join(H,'denklem-1.json'),os.path.join(H,'denklem-1-kardes.json'))
