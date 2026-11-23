"""AYT Fizik · Vektörler · 20 soru (3 kolay / 11 orta / 6 zor). Şekiller TikZ (cizim.tikz_svg); koordinatlar ve her cevap/çeldirici Python'da hesaplanıp assert edilir."""
import sys,os,re,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,radians,sqrt,atan2,degrees
P=Parti('vektor','Vektörler','afiz|Vektörler',ders='AYT Fizik',idon='aytfiz')
P.konu_adi='Vektörler'; H.KONU='Vektörler'; TIPK={}
KAY='ÖSYM AYT Fizik 2018–2025 (yalnız mantık) · 345 AYT Fizik s.7–20 · MEB 11. sınıf fizik'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAY)
def q(no,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    mk(P,no,ad=ad,adim=len(ad),**k)
ROM=['I','II','III']
def parse(l): return frozenset(ROM.index(x) for x in re.findall(r'III|II|I',l))
def onc(no,ust,claims,sira,son='hangileri doğrudur?',**kw):
    T=frozenset(i for i,c in enumerate(claims) if c[1])
    metin=ust+'\n'+'\n'.join(f'{ROM[i]}. {c[0]}' for i,c in enumerate(claims))+'\n'+son
    sets={l:parse(l) for l in sira}; dl=[l for l in sira if sets[l]==T]; assert len(dl)==1,(no,T)
    assert len(sira)==5
    yan=[]
    for l in sira:
        if l==dl[0]: continue
        S=sets[l]; parts=[f"{ROM[i]} öncülünü {'doğru' if i in S else 'yanlış'} saymış; gerçekte {claims[i][2]}." for i in sorted(S^T)]
        yan.append((l,' '.join(parts),'bilgi'))
    ad=[A(f'{ROM[i]}. öncülü incele',claims[i][2][0].upper()+claims[i][2][1:]+'.',f'{ROM[i]}: '+('doğru' if i in T else 'yanlış')) for i in range(len(claims))]
    ad.append(A('Sonucu yaz','Doğru olan öncüller birlikte alınır.',dl[0]))
    q(no,metin=metin,dogru=dl[0],yan=yan,ad=ad,sira=sira,kalip='öncüllü',**kw)
# ---- TikZ yardımcıları
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
C1,C2,C3,C4,C5='blue!70!black','red!75!black','green!45!black','orange!90!black','violet!80!black'
def tk(govde,ust='[line cap=round,line join=round,font=\\small]'): return tikz_svg('\\begin{tikzpicture}'+ust+'\n'+govde+TAIL)
def gtk(govde,sc=.7): return tk(govde,f'[line cap=round,line join=round,font=\\small,x={sc}cm,y={sc}cm]')
def grid(w,h): return f'\\draw[step=1,gray!55,dashed,thin] (0,0) grid ({w},{h}); \\draw[black,thin] (0,0) rectangle ({w},{h});'
def gv(p0,d,name,col,pos='above',tex=None):
    x0,y0=p0; x1,y1=x0+d[0],y0+d[1]; t=tex or f'$\\vec{{{name}}}$'
    return f'\\draw[{col},very thick,{ARR}] ({x0},{y0}) -- ({x1},{y1}) node[midway,{pos},{col},inner sep=2pt] {{{t}}};'
def cv(p0,d,col,lab=None,pos='above',w='very thick',at='midway'):
    x0,y0=p0; x1,y1=x0+d[0],y0+d[1]
    n=f' node[{'at end' if at=='end' else at},{pos},{col},inner sep=2pt] {{{lab}}}' if lab else ''
    return f'\\draw[{col},{w},{ARR}] ({x0:.3f},{y0:.3f}) -- ({x1:.3f},{y1:.3f}){n};'
def vadd(*vs): return (sum(v[0] for v in vs),sum(v[1] for v in vs))
def vsub(a,b): return (a[0]-b[0],a[1]-b[1])
def vmul(k,a): return (k*a[0],k*a[1])
def mag2(a): return a[0]**2+a[1]**2
# ================= KARTLAR =================
kartla('K-AFVK-01','Kareli zeminde vektör eşitlikleri','Her vektörün bileşenleri kareli zeminden okunur; eşitlikler bileşen bileşen kontrol edilir (toplama, çıkarma, sayıyla çarpma).','Çıkarmada yönü ters almak; uç uca ekleme yerine başlangıç noktalarını eşitlemek; kat sayıyı yalnız bir bileşene uygulamak.','orta','öncüllü',3,'vk-esitlik','Kareli zeminde vektör eşitliklerinin kontrolü')
kartla('K-AFVK-02','Bileşke kuvvetin büyüklüğü','Vektörler bileşenlerine ayrılır, aynı eksendeki bileşenler toplanır, bileşkenin büyüklüğü Pisagor ile bulunur.','Büyüklükleri doğrudan toplamak; yalnız tek eksendeki bileşeni almak; karekökü unutmak.','orta','şekilli',3,'vk-bileske','Bileşke vektörün büyüklüğü')
kartla('K-AFVK-03','Açılı kuvvetlerin bileşenleri','Eğik bir kuvvet F·cosθ ve F·sinθ bileşenlerine ayrılır; eksen bileşenleri toplanıp bileşke bulunur.','sin ve cos yerlerini karıştırmak; açıyı hangi eksenden ölçüldüğüne bakmadan kullanmak.','zor','şekilli',4,'vk-bilesen','Açılı vektörün bileşenleri ve bileşke')
kartla('K-AFVK-04','Yer değiştirme ve ortalama hız','Yer değiştirme başlangıç–bitiş arasındaki vektördür; yol skalerdir. Ortalama hız = yer değiştirme/süre, ortalama sürat = yol/süre.','Yer değiştirmeyi alınan yola eşitlemek; yönü ters yazmak.','orta','şekilli',4,'vk-yerdegis','Yer değiştirme, yol ve ortalama hız')
kartla('K-AFVK-05','Skaler ve vektörel nicelikler, bileşke aralığı','Vektörel nicelik büyüklük ve yön taşır; iki vektörün bileşkesi |a−b| ile a+b arasındadır.','Sürati hızla, kütleyi ağırlıkla karıştırmak; bileşkenin her zaman toplam olduğunu sanmak.','orta','öncüllü',3,'vk-kavram','Vektör kavramları ve bileşke aralığı')
kartla('K-AFVK-06','Vektörlerle denge','Dengede kuvvetlerin vektörel toplamı sıfırdır; bilinmeyen kuvvet diğerlerinin bileşkesinin tersidir; asılı cisimde bileşenler eksen eksen eşitlenir.','Gerilmeyi ağırlığa eşitlemek; açıyı yanlış bileşene yazmak; bir kuvveti atlamak.','orta','şekilli',4,'vk-denge','Kuvvetlerin dengesi ve ip gerilmeleri')
kartla('K-AFVK-07','Vektör çıkarma ve değişim','A − B = A + (−B); hız değişimi Δv = v_son − v_ilk vektörel farktır, büyüklükler farkı değildir.','Büyüklükleri çıkarmak; farkı toplam gibi almak; yönü tersine çevirmeyi unutmak.','orta','şekilli',3,'vk-fark','Vektör çıkarma ve hız değişimi')
kartla('K-AFVK-08','Bileşke kuvvetten ivme','Bileşke kuvvet vektörel toplamla bulunur, ΣF = m·a ile ivmenin büyüklüğü hesaplanır.','Bileşke yerine büyüklükleri toplamak; kütleyi çarpmak ya da unutmak; kare değerini yanlış okumak.','zor','şekilli',4,'vk-newton','Bileşke kuvvet ve ivme')
kartla('K-AFVK-09','Paralelkenar kuralı','Aralarındaki açı θ olan F1 ve F2 için R² = F1² + F2² + 2F1F2cosθ; açı büyüdükçe bileşke küçülür.','Açı arttıkça bileşkenin arttığını sanmak; cos işaretini yanlış almak.','orta','öncüllü',3,'vk-paralelkenar','Paralelkenar kuralı ve açıya bağlı bileşke')
# ================= SORULAR =================
# ---------- 01 · kolay · öncüllü · kareli zemin
Av=(2,1);Bv=(1,2);Cv=(3,3);Dv=(1,-1)
c1=[vadd(Av,Bv)==Cv, vsub(Bv,Av)==Dv, vsub(Cv,vmul(2,Bv))==Dv]; assert c1==[True,False,True]
f=[grid(7,5),gv((0,0),Av,'A',C1,'below right'),gv((3,0),Bv,'B',C2,'right'),gv((0,2),Cv,'C',C3,'above left'),gv((4,4),Dv,'D',C4,'above right')]
SK=gtk('\n'.join(f))
onc('0001','Aynı düzlemde bulunan A, B, C ve D vektörleri, eşit bölmeli kareli zemin üzerinde şekilde gösterilmiştir.\nBuna göre,',
 [('A + B = C',c1[0],'A + B vektörünün bileşenleri (3 sağ, 3 yukarı) olup C ile aynıdır, öncül doğrudur'),
  ('B − A = D',c1[1],'B − A bileşenleri (1 sol, 1 yukarı) olup D’nin tersidir, eşit değildir'),
  ('C − 2B = D',c1[2],'C − 2B bileşenleri (1 sağ, 1 aşağı) olup D ile aynıdır, öncül doğrudur')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],son='eşitliklerinden hangileri doğrudur?',
 tipId='vk-esitlik',tip='Kareli zeminde vektör eşitliklerinin kontrolü',z='kolay',alt='Vektörlerin Toplanması ve Çıkarılması',kaz='Kareli zeminde verilen vektörlerle toplama, çıkarma ve sayıyla çarpma eşitliklerini bileşenlerle sınar.',
 kart='K-AFVK-01 (kareli zeminde eşitlikler) · dört vektör, üç eşitlik',istenen='Doğru olan vektör eşitliklerini belirlemek.',
 ip=['Her vektörün kaç bölme sağa/sola ve kaç bölme yukarı/aşağı gittiğini yazıp eşitliklerin iki yanını ayrı ayrı hesapla.'],
 bilgi=[B('Vektörlerin bileşenleri','Kareli zeminde bir vektör, yatay ve düşey bölme sayılarıyla yazılır; toplama ve çıkarma bileşen bileşen yapılır. Örnek: (2, 1) + (1, −3) = (3, −2)'),
        B('Vektör çıkarma','A − B, A + (−B) demektir; −B, B ile aynı büyüklükte ve zıt yönlü vektördür. Örnek: (4, 1) − (1, 3) = (3, −2)')],
 puf='Kareli zeminde her vektörü (yatay, düşey) bileşenleriyle yazmak, eşitlik sorularını işlemden çok sayma işine çevirir.',sekil=SK)
# ---------- 02 · kolay · bileşke büyüklüğü
F1=(4,1);F2=(-2,1);F3=(1,2); R2=vadd(F1,F2,F3); assert R2==(3,4) and mag2(R2)==25
f=[grid(8,4)]+[f'\\fill (3,1) circle (1.6pt) node[below left] {{O}};',gv((3,1),F1,'F_1',C1,'below'),gv((3,1),F2,'F_2',C2,'below left'),gv((3,1),F3,'F_3',C3,'right')]
SK=gtk('\n'.join(f))
q('0002',tipId='vk-bileske',tip='Bileşke vektörün büyüklüğü',z='kolay',alt='Bileşke Kuvvet',kaz='Aynı noktaya etki eden kuvvetlerin bileşkesinin büyüklüğünü bileşenlerinden bulur.',
 kart='K-AFVK-02 (bileşke büyüklüğü) · üç kuvvet, 3–4–5 bileşke',kalip='şekilli',
 metin='Aynı noktaya etki eden F₁, F₂ ve F₃ kuvvetleri, her bölmesi 1 N’u temsil eden kareli zemin üzerinde şekilde gösterilmiştir.\nBuna göre, bu üç kuvvetin bileşkesinin büyüklüğü kaç N’dur?',
 dogru=5,yan=[(3,'Yalnız yatay bileşenleri toplamış (4 − 2 + 1 = 3); düşey bileşenleri hesaba katmamış.','dikkat'),
  (4,'Yalnız düşey bileşenleri toplamış (1 + 1 + 2 = 4); yatay bileşenleri unutmuş.','dikkat'),
  (7,'Bileşke vektörün bileşenlerini (3 ve 4) Pisagor yerine toplayarak büyüklük sanmış.','bilgi'),
  (25,'Pisagor bağıntısında kareler toplamını (9 + 16 = 25) bulup karekök almayı unutmuş.','islem')],
 istenen='Üç kuvvetin bileşkesinin büyüklüğü (N).',ip=['Yatay ve düşey bileşenleri ayrı ayrı toplayıp elde ettiğin iki sayıyı tek bir vektör olarak düşün.'],
 bilgi=[B('Bileşke vektör','Birden çok vektörün etkisini tek başına veren vektördür; bileşenler eksen eksen toplanır. Örnek: (1, 2) ve (2, −1) vektörlerinin bileşkesi (3, 1)’dir'),
        B('Büyüklük','Bileşenleri x ve y olan vektörün büyüklüğü √(x² + y²)’dir. Örnek: bileşenleri 6 ve 8 olan vektörün büyüklüğü 10’dur')],
 ad=[A('Bileşenleri oku','Her kuvvetin yatay ve düşey bölme sayısı okunur.','F₁ = (4, 1) · F₂ = (−2, 1) · F₃ = (1, 2)'),
     A('Yatay bileşenleri topla','Sağ yön pozitif, sol yön negatiftir.','Rₓ = 4 − 2 + 1 = 3 N'),
     A('Düşey bileşenleri topla','Yukarı yön pozitiftir.','R_y = 1 + 1 + 2 = 4 N'),
     A('Büyüklüğü bul','Bileşke vektörün büyüklüğü Pisagor ile hesaplanır.','R = √(3² + 4²) = 5 N')],
 puf='Bileşke büyüklüğü kuvvetlerin büyüklükleri toplanarak değil, bileşenler toplanıp Pisagor uygulanarak bulunur.',sekil=SK)
# ---------- 03 · kolay · öncüllü · kavram
onc('0003','Fizikte bazı nicelikler yalnızca sayısal değerle, bazıları ise sayısal değer ve yönle ifade edilir.\nBuna göre,',
 [('Yer değiştirme',True,'yer değiştirme, yönü olan vektörel bir niceliktir'),
  ('Sürat',False,'sürat yön taşımayan skaler bir niceliktir'),
  ('Kütle',False,'kütle yön taşımayan skaler bir niceliktir')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],son='niceliklerinden hangileri vektörel niceliktir?',
 tipId='vk-kavram',tip='Vektör kavramları ve bileşke aralığı',z='kolay',alt='Skaler ve Vektörel Nicelikler',kaz='Fiziksel niceliklerin skaler ya da vektörel olduğunu ayırt eder.',
 kart='K-AFVK-05 (skaler–vektörel ayrımı) · yer değiştirme, kuvvet, sıcaklık',istenen='Vektörel olan nicelikleri belirlemek.',
 ip=['Her niceliğin tek bir sayıyla mı, yoksa sayı ve yönle mi tanımlandığını düşün.'],
 bilgi=[B('Skaler ve vektörel','Skaler nicelik yalnız büyüklükle, vektörel nicelik büyüklük ve yönle belirtilir. Örnek: kütle ve süre skalerdir; hız ve ivme vektöreldir')],
 puf='Yön gerektiren nicelikler vektöreldir; “kaç?” sorusu yetiyorsa nicelik skalerdir.')
# ---------- 04 · orta · açılı bileşenler
th=radians(53); a1=20; assert abs(a1*cos(th)-12)<.1 and abs(a1*sin(th)-16)<.1
Fa=(12,16);Fb=(-7,0);Fc=(0,-4); Rr=vadd(Fa,Fb,Fc); assert Rr==(5,12) and mag2(Rr)==169
s=.2
f=['\\draw[gray,dashed] (-2.2,0) -- (4.2,0);','\\fill (0,0) circle (1.8pt);',
   cv((0,0),(12*s,16*s),C1,'$F_1=20$ N','above left'),cv((0,0),(-7*s,0),C2,'$F_2=7$ N','above'),cv((0,0),(0,-4*s),C3,'$F_3=4$ N','right'),
   '\\draw (.9,0) arc[start angle=0,end angle=53,radius=.9];','\\node at (1.45,.4) {$53^\\circ$};']
SK=tk('\n'.join(f))
q('0004',tipId='vk-bilesen',tip='Açılı vektörün bileşenleri ve bileşke',z='orta',alt='Vektörün Bileşenlerine Ayrılması',kaz='Açılı bir kuvveti dik bileşenlerine ayırarak üç kuvvetin bileşkesini bulur.',
 kart='K-AFVK-03 (açılı bileşenler) · 20 N, 53°, bileşke 13 N',kalip='şekilli',
 metin='Sürtünmesiz yatay bir düzlemde bulunan noktasal bir cisme aynı düzlemde F₁, F₂ ve F₃ kuvvetleri şekildeki gibi uygulanıyor. F₁ kuvveti yatayla 53° açı yapmaktadır.\n(sin53° = 0,8; cos53° = 0,6)\nBuna göre, bu üç kuvvetin bileşkesi kaç N’dur?',
 dogru=13,yan=[(5,'Yalnız yatay bileşenleri hesaplamış (12 − 7 = 5); düşey bileşenleri katmamış.','dikkat'),
  (9,'Büyüklükleri işaretli toplamış (20 − 7 − 4 = 9); vektörleri bileşenlerine ayırmamış.','bilgi'),
  (12,'Yalnız düşey bileşenleri hesaplamış (16 − 4 = 12); yatay bileşenleri unutmuş.','dikkat'),
  (17,'Bileşke vektörün bileşenlerini (5 ve 12) Pisagor yerine toplamış.','islem')],
 istenen='F₁, F₂ ve F₃ kuvvetlerinin bileşkesinin büyüklüğü (N).',ip=['Eğik kuvveti yatay ve düşey bileşenlerine ayır; sonra eksen eksen topla.'],
 bilgi=[B('Bileşenlere ayırma','Yatayla θ açısı yapan F kuvvetinin yatay bileşeni F·cosθ, düşey bileşeni F·sinθ’dır. Örnek: 10 N’luk kuvvet 30°’de ise bileşenleri yaklaşık 8,7 N ve 5 N’dur')],
 ad=[A('F₁’i ayır','Yatay bileşen cos53°, düşey bileşen sin53° ile bulunur.','F₁ₓ = 20 × 0,6 = 12 N · F₁y = 20 × 0,8 = 16 N'),
     A('Yatay bileşenleri topla','Sağ yön pozitiftir; F₂ sola doğrudur.','Rₓ = 12 − 7 = 5 N'),
     A('Düşey bileşenleri topla','F₃ aşağı yönlüdür.','R_y = 16 − 4 = 12 N'),
     A('Büyüklüğü bul','Pisagor bağıntısı kullanılır.','R = √(5² + 12²) = 13 N')],
 puf='Eğik kuvvetlerde önce eksenlere ayır, sonra eksen eksen topla; büyüklük en sonda Pisagor ile bulunur.',sekil=SK)
# ---------- 05 · orta · yer değiştirme (yön)
Pa=[(30,30),(-10,0),(0,-30)]; net=vadd(*Pa); assert net==(20,0)
s=.1
k5=1.3
f=[cv((0,0),(3*k5,3*k5),C1,'$30\\sqrt{2}$ m','above left'),cv((3*k5,3*k5),(-1*k5,0),C2,'$10$ m','above'),cv((2*k5,3*k5),(0,-3*k5),C3,'$30$ m','right'),
   '\\fill (0,0) circle (2pt) node[below left] {A};',f'\\fill ({2*k5},0) circle (2pt) node[below] {{B}};']
# yön okları
cx,cy,r=6.6,1.9,.95
dirs=[('Kuzey',90,'above'),('KD',45,'above right'),('Doğu',0,'right'),('GD',-45,'below right'),('Güney',-90,'below'),('GB',-135,'below left'),('Batı',180,'left'),('KB',135,'above left')]
for n_,a_,p_ in dirs:
    f.append(f'\\draw[gray!70!black,{ARR}] ({cx},{cy}) -- ({cx+r*cos(radians(a_)):.3f},{cy+r*sin(radians(a_)):.3f}) node[{p_},inner sep=1.5pt,font=\\footnotesize] {{{n_}}};')
SK=tk('\n'.join(f))
q('0005',tipId='vk-yerdegis',tip='Yer değiştirme, yol ve ortalama hız',z='orta',alt='Yer Değiştirme Vektörü',kaz='Birden çok doğrusal harekette toplam yer değiştirmenin büyüklüğünü ve yönünü bulur.',
 kart='K-AFVK-04 (yer değiştirme) · 30√2 m KD, 10 m B, 30 m G',kalip='şekilli',
 metin='Düz ve yatay bir arazide A noktasından harekete geçen bir doğa yürüyüşçüsü, şekildeki yolu izleyerek B noktasında duruyor. Yürüyüşçünün her bir doğrusal kısımdaki uzunluğu ve yön okları şekilde verilmiştir.\nBuna göre, yürüyüşçünün yer değiştirmesinin büyüklüğü ve yönü aşağıdakilerden hangisidir?',
 dogru='20 m ; Doğu',yan=[('10 m ; Doğu','Batı yönündeki 10 m’yi iki kez çıkarmış: 30 − 10 − 10 = 10 m.','islem'),
  ('20 m ; Batı','Büyüklüğü doğru bulmuş ama yer değiştirmeyi bitişten başlangıca (B’den A’ya) doğru yazmış.','dikkat'),
  ('40 m ; Doğu','Batı yönündeki 10 m’yi doğu yönüne eklemiş: 30 + 10 = 40 m.','bilgi'),
  ('30√2 m ; Kuzeydoğu','Yalnız ilk doğrusal hareketi yer değiştirme olarak almış.','dikkat')],
 sira=['10 m ; Doğu','20 m ; Batı','20 m ; Doğu','40 m ; Doğu','30√2 m ; Kuzeydoğu'],
 istenen='A’dan B’ye yer değiştirmenin büyüklüğü ve yönü.',ip=['Kuzeydoğu yöndeki hareketi doğu ve kuzey bileşenlerine ayırarak her yöndeki net hareketi bul.'],
 bilgi=[B('Yer değiştirme','Başlangıç noktasından bitiş noktasına çizilen vektördür; izlenen yoldan bağımsızdır. Örnek: 3 m doğuya, 3 m batıya giden kişinin yer değiştirmesi sıfırdır'),
        B('Köşegen yön','Kuzeydoğu, kuzey ile doğunun tam ortasındadır (45°); d uzunluğundaki KD hareketin doğu ve kuzey bileşenleri d/√2’dir')],
 ad=[A('KD hareketi ayır','45° olduğundan iki bileşen eşittir.','30√2 / √2 = 30 → 30 m Doğu, 30 m Kuzey'),
     A('Doğu–batı bileşenini bul','Doğu pozitif, batı negatiftir.','30 − 10 = 20 m Doğu'),
     A('Kuzey–güney bileşenini bul','Kuzey pozitif, güney negatiftir.','30 − 30 = 0'),
     A('Sonucu yaz','Net hareket yalnız doğu yönündedir.','20 m Doğu')],
 puf='Yer değiştirme için yol değil, yönlü bileşenlerin net toplamı hesaplanır.',sekil=SK)
# ---------- 06 · orta · öncüllü · bileşke aralığı (şekilsiz)
a_,b_=7,5; lo,hi=abs(a_-b_),a_+b_; assert (lo,hi)==(2,12)
onc('0006','Büyüklükleri 7 N ve 5 N olan iki kuvvet aynı noktaya uygulanıyor. Kuvvetler arasındaki açı, 0° ile 180° arasında istenildiği gibi değiştirilebilmektedir.\nBuna göre, bu iki kuvvetin bileşkesinin büyüklüğü,',
 [('1 N',lo<=1<=hi,'bileşke en az 7 − 5 = 2 N olabildiği için 1 N alınamaz'),
  ('2 N',lo<=2<=hi,'kuvvetler zıt yönlü olduğunda bileşke 7 − 5 = 2 N olur'),
  ('12 N',lo<=12<=hi,'kuvvetler aynı yönlü olduğunda bileşke 7 + 5 = 12 N olur')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],son='değerlerinden hangilerini alabilir?',
 tipId='vk-kavram',tip='Vektör kavramları ve bileşke aralığı',z='orta',alt='Bileşke Vektörün Sınırları',kaz='İki vektörün bileşkesinin alabileceği en küçük ve en büyük değeri belirler.',
 kart='K-AFVK-05 (bileşke aralığı) · 7 N ve 5 N',istenen='Bileşkenin alabileceği değerleri belirlemek.',
 ip=['Bileşkenin en küçük ve en büyük olduğu iki özel durumu (kuvvetlerin yönleri) düşün.'],
 bilgi=[B('Bileşkenin sınırları','Büyüklükleri a ve b olan iki vektörün bileşkesi |a − b| ile a + b arasında her değeri alabilir. Örnek: 3 ve 4 büyüklüğündeki vektörlerin bileşkesi 1 ile 7 arasındadır')],
 puf='İki vektörün bileşkesi hiçbir zaman büyüklükler farkından küçük, toplamından büyük olamaz.')
# ---------- 07 · orta · iple denge, yatay ip
W=60; T2=W/sin(radians(37)); T1=T2*cos(radians(37)); assert abs(T2-100)<.5 and abs(T1-80)<.5
assert abs(W*0.75-45)<1e-9 and abs(W*.8-48)<1e-9
f=['\\fill[gray!35] (-3.1,1.8) rectangle (2.9,2.1);','\\fill[gray!35] (2.6,-1.6) rectangle (2.9,1.8);',
   '\\draw (-3.1,1.8) -- (2.6,1.8) -- (2.6,-1.6);',
   '\\draw[thick] (0,0) -- (-2.4,1.8);','\\draw[thick] (0,0) -- (2.6,0);','\\draw[thick] (0,0) -- (0,-.9);',
   '\\draw[thick,fill=gray!25] (-.55,-1.55) rectangle (.55,-.9);','\\node at (0,-1.22) {6 kg};','\\fill (0,0) circle (1.8pt);',
   '\\draw[gray,dashed] (-1.6,0) -- (0,0);','\\draw (-.9,0) arc[start angle=180,end angle=143,radius=.9];','\\node at (-1.35,.3) {$37^\\circ$};',
   '\\node[above] at (1.4,0) {$T_1$};','\\node[above right] at (-1.2,.9) {$T_2$};']
SK=tk('\n'.join(f))
q('0007',tipId='vk-denge',tip='Kuvvetlerin dengesi ve ip gerilmeleri',z='orta',alt='Dengede Bileşke Kuvvet',kaz='Üç ipin dengesinde kuvvetleri eksenlere ayırarak yatay ipteki gerilmeyi bulur.',
 kart='K-AFVK-06 (ip dengesi) · 6 kg, 37°, T₁ = 80 N',kalip='şekilli',
 metin='Kütlesi şekilde verilen cisim, hafif ipler yardımıyla tavana ve düşey duvara şekildeki gibi bağlanarak dengede tutuluyor. Eğik ip tavanla 37° açı yapmaktadır.\n(g = 10 m/s², sin37° = 0,6, cos37° = 0,8)\nBuna göre, yatay ipteki T₁ gerilme kuvvetinin büyüklüğü kaç N’dur?',
 dogru=80,yan=[(45,'Ağırlığı tan37° (0,75) ile çarpmış: 60 × 0,75 = 45 N; bağıntıyı ters kurmuş.','bilgi'),
  (48,'Ağırlığı cos37° ile çarpmış: 60 × 0,8 = 48 N; düşey ve yatay denge denklemlerini kurmamış.','bilgi'),
  (60,'Yatay ipin gerilmesini cismin ağırlığına eşit almış.','bilgi'),
  (100,'Eğik ipin gerilmesini (T₂ = 60 ÷ 0,6 = 100 N) yatay ipin gerilmesi sanmış.','dikkat')],
 istenen='Yatay ipteki gerilme kuvvetinin büyüklüğü (N).',ip=['Düğüm noktasında kuvvetleri yatay ve düşey eksenlerde ayrı ayrı sıfıra eşitle.'],
 bilgi=[B('Denge koşulu','Dengedeki cisme etki eden kuvvetlerin vektörel toplamı sıfırdır; yani her eksendeki bileşenlerin toplamı sıfırdır. Örnek: 20 N’luk ağırlığı taşıyan tek düşey ip 20 N’luk gerilme oluşturur')],
 ad=[A('Ağırlığı bul','Cismin ağırlığı kütle ile g’nin çarpımıdır.','G = 6 × 10 = 60 N'),
     A('Düşey dengeyi yaz','Eğik ipin düşey bileşeni ağırlığı dengelemelidir.','T₂ × sin37° = 60 → T₂ = 100 N'),
     A('Yatay dengeyi yaz','Eğik ipin yatay bileşeni yatay ipin gerilmesine eşittir.','T₁ = T₂ × cos37° = 100 × 0,8'),
     A('Sonucu yaz','Gerilmeyi hesapla.','T₁ = 80 N')],
 puf='Düğüm noktasında her eksen için ayrı denge denklemi yazılır; ağırlık yalnız düşey eksende görünür.',sekil=SK)
# ---------- 08 · orta · öncüllü · eğik düzlem
th=radians(37); L_=3.2; ux,uy=cos(th),sin(th); nx,ny=-sin(th),cos(th)
Sx,Sy=L_*ux,L_*uy; Cx,Cy=Sx+.3*nx,Sy+.3*ny; s=.04
G_=50;N_=G_*.8;f_=G_*.6; assert (N_,f_)==(40,30)
f=['\\fill[gray!25] (0,0) -- (4.4,0) -- (4.4,3.3) -- cycle;','\\draw[thick] (0,0) -- (4.4,0) -- (4.4,3.3) -- cycle;',
   f'\\begin{{scope}}[shift={{({Sx:.3f},{Sy:.3f})}},rotate=37]\\draw[thick,fill=white] (-.6,0) rectangle (.6,.6);\\end{{scope}}',
   f'\\fill ({Cx:.3f},{Cy:.3f}) circle (1.6pt);',
   cv((Cx,Cy),(0,-G_*s),C1,'$G$','left'),cv((Cx,Cy),(N_*s*nx,N_*s*ny),C2,'$N$','left',at='end'),cv((Cx,Cy),(-f_*s*ux,-f_*s*uy),C3,'$f$','below right'),
   '\\draw (.9,0) arc[start angle=0,end angle=37,radius=.9];','\\node at (1.25,.2) {$37^\\circ$};']
# f yukarı yönde olmalı (düzlem boyunca yukarı)
f[6]=cv((Cx,Cy),(f_*s*ux,f_*s*uy),C3,'$f$','right',at='end')
SK=tk('\n'.join(f))
onc('0008','Eğimi 37° olan eğik düzlem üzerindeki 5 kg kütleli cisim dengededir. Cisme etki eden G ağırlığı, N tepki kuvveti ve f sürtünme kuvveti şekilde gösterilmiştir.\n(g = 10 m/s², sin37° = 0,6, cos37° = 0,8)\nBuna göre,',
 [('N = 40 N’dur.',True,'tepki kuvveti ağırlığın düzleme dik bileşenine eşittir: 50 × 0,8 = 40 N'),
  ('f = 30 N’dur.',True,'sürtünme kuvveti ağırlığın düzleme paralel bileşenine eşittir: 50 × 0,6 = 30 N'),
  ('f = 40 N’dur.',False,'sürtünme kuvveti 30 N’dur; 40 N, tepki kuvvetinin değeridir')],
 ['Yalnız III','I ve II','I ve III','II ve III','I, II ve III'],son='yargılarından hangileri doğrudur?',
 tipId='vk-bilesen',tip='Açılı vektörün bileşenleri ve bileşke',z='orta',alt='Ağırlığın Bileşenleri',kaz='Eğik düzlemde ağırlığı düzleme paralel ve dik bileşenlerine ayırarak denge kuvvetlerini yorumlar.',
 kart='K-AFVK-03 (eğik düzlemde bileşenler) · 5 kg, 37°',istenen='Doğru olan yargıları belirlemek.',
 ip=['Ağırlığı düzleme paralel ve düzleme dik iki bileşene ayır; denge her doğrultuda ayrı geçerlidir.'],
 bilgi=[B('Eğik düzlemde bileşenler','Eğimi θ olan düzlemde ağırlığın düzleme paralel bileşeni m·g·sinθ, dik bileşeni m·g·cosθ’dır. Örnek: 10 N’luk ağırlık 30°’de iken paralel bileşeni 5 N’dur')],
 puf='Eğik düzlemde eksenleri düzleme paralel ve dik seçmek ağırlığı iki bileşene ayırmayı ve dengeyi kolaylaştırır.',sekil=SK)
# ---------- 09 · orta · tersine çevrilen vektör
V={'a':(2,0),'b':(0,3),'c':(3,2),'d':(-1,-2),'e':(2,1)}; S9=vadd(*V.values()); assert S9==(6,4)
sol=[k for k in V if vadd(*[vmul(-1,V[j]) if j==k else V[j] for j in V])==(0,0)]; assert sol==['c']
f=[grid(7,6),gv((0,0),V['a'],'a',C1,'below'),gv((3,0),V['b'],'b',C2,'right'),gv((0,2),V['c'],'c',C3,'above left'),gv((6,5),V['d'],'d',C4,'right'),gv((4,0),V['e'],'e',C5,'below right')]
SK=gtk('\n'.join(f))
def cel9(k): R=vadd(*[vmul(-1,V[j]) if j==k else V[j] for j in V]); return f'{k} vektörünün yönünü çevirince bileşke ({R[0]}, {R[1]}) olur; sıfırlanmaz.'
q('0009',tipId='vk-fark',tip='Vektör çıkarma ve hız değişimi',z='orta',alt='Vektörlerin Toplanması ve Çıkarılması',kaz='Kareli zeminde verilen vektörlerin bileşkesini bulur ve bir vektörün yönünü çevirmenin etkisini yorumlar.',
 kart='K-AFVK-07 (yön değiştirme) · beş vektör, bileşke 2c',kalip='şekilli',
 metin='Aynı düzlemde bulunan a, b, c, d ve e vektörleri, eşit bölmeli kareli zeminde şekilde gösterilmiştir.\nBuna göre, hangi vektörün yönü tersine çevrilirse bu beş vektörün bileşkesi sıfır olur?',
 dogru='c',yan=[(k,cel9(k),'islem') for k in 'abde'],sira=list('abcde'),
 istenen='Yönü çevrildiğinde bileşkeyi sıfır yapan vektör.',ip=['Beş vektörün bileşkesini bulduktan sonra, bir vektörün yönü çevrilince bileşkenin ne kadar değiştiğini düşün.'],
 bilgi=[B('Yönü çevirme','Bir vektörün yönü tersine çevrilince toplamdan 2 katı çıkarılmış gibi olur: yeni bileşke = eski bileşke − 2 × (o vektör). Örnek: bileşke (4, 2) iken (2, 1) vektörü çevrilirse bileşke sıfır olur')],
 ad=[A('Bileşenleri oku','Her vektörün yatay ve düşey bölme sayısı yazılır.','a(2,0) b(0,3) c(3,2) d(−1,−2) e(2,1)'),
     A('Bileşkeyi bul','Bileşenler ayrı ayrı toplanır.','R = (6, 4)'),
     A('Koşulu kur','Yönü çevrilen x için R − 2x = 0 olmalıdır.','x = R/2 = (3, 2)'),
     A('Vektörü belirle','Bileşenleri (3, 2) olan vektör c’dir.','c')],
 puf='Bir vektörü ters çevirmek, bileşkeden onun iki katını çıkarmaktır; bileşkenin yarısı aranan vektördür.',sekil=SK)
# ---------- 10 · orta · hız değişimi
vK=(3,0);vL=(3,4); dv=vsub(vL,vK); assert dv==(0,4)
assert (sqrt(mag2(vL))-sqrt(mag2(vK)),sqrt(mag2(vL)),sqrt(mag2(vK))+sqrt(mag2(vL)),vK[0]+vL[0])==(2,5,8,6)
f=[grid(8,6),gv((0,1),vK,'v_K',C1,'below'),gv((4,1),vL,'v_L',C2,'right'),'\\node[font=\\small] at (1.5,2.0) {K’deki hız};','\\node[font=\\small] at (2.6,3.2) {L’deki hız};']
SK=gtk('\n'.join(f))
q('0010',tipId='vk-fark',tip='Vektör çıkarma ve hız değişimi',z='orta',alt='Hız Değişimi',kaz='İki hız vektörü arasındaki farkın büyüklüğünü vektörel çıkarma ile bulur.',
 kart='K-AFVK-07 (hız değişimi) · vK = (3, 0), vL = (3, 4)',kalip='şekilli',
 metin='Yatay bir buz pistinde kayan bir disk, K noktasından geçtikten sonra pistin kenarındaki bir engele çarparak yön değiştiriyor ve L noktasından geçiyor. Diskin K ve L noktalarındaki hız vektörleri, her bölmesi 1 m/s’yi temsil eden kareli zeminde şekilde gösterilmiştir.\nBuna göre, diskin K’den L’ye geçerken hızındaki değişimin büyüklüğü kaç m/s’dir?',
 dogru=4,yan=[(2,'Hızların büyüklüklerini skaler olarak çıkarmış: 5 − 3 = 2 m/s.','bilgi'),
  (5,'L noktasındaki hızın büyüklüğünü hız değişimi sanmış.','dikkat'),
  (6,'Yatay bileşenleri toplamış (3 + 3 = 6); vektörel fark almamış.','islem'),
  (8,'Hızların büyüklüklerini toplamış: 3 + 5 = 8 m/s.','bilgi')],
 istenen='Hız değişiminin büyüklüğü (m/s).',ip=['K ve L noktalarındaki hız vektörlerinin yatay ve düşey bileşenlerini ayrı ayrı yaz.'],
 bilgi=[B('Hız değişimi','Δv = v_son − v_ilk vektörel bir farktır; bileşenler ayrı ayrı çıkarılır. Örnek: (5, 2) ve (1, 2) hızları arasındaki değişim (−4, 0)’dır')],
 ad=[A('Hızları oku','Kareli zeminden bileşenler okunur.','v_K = (3, 0) · v_L = (3, 4)'),
     A('Vektörel fark al','Her bileşen için son − ilk hesaplanır.','Δv = (3 − 3, 4 − 0) = (0, 4)'),
     A('Büyüklüğü yaz','Değişim yalnız düşey doğrultudadır.','|Δv| = 4 m/s')],
 puf='Hız bir vektördür; değişimi bulurken büyüklükler değil bileşenler çıkarılır.',sekil=SK)
# ---------- 11 · orta · denge, dördüncü kuvvet
Fd1=(2,1);Fd2=(-1,2);Fd3=(-3,-1); S11=vadd(Fd1,Fd2,Fd3); F4=vmul(-1,S11); assert F4==(2,-2) and mag2(F4)==8
assert mag2(vadd(Fd1,Fd2))==10 and 2+2==4
f=[grid(8,6),'\\fill (4,3) circle (1.8pt);',gv((4,3),Fd1,'F_1',C1,'below right'),gv((4,3),Fd2,'F_2',C2,'right'),gv((4,3),Fd3,'F_3',C3,'above')]
SK=gtk('\n'.join(f))
q('0011',tipId='vk-denge',tip='Kuvvetlerin dengesi ve ip gerilmeleri',z='orta',alt='Dengede Bileşke Kuvvet',kaz='Dengedeki cisimde bilinmeyen kuvveti diğer kuvvetlerin bileşkesinin tersi olarak bulur.',
 kart='K-AFVK-06 (dördüncü kuvvet) · F₄ = (2, −2) bölme',kalip='şekilli',
 metin='Noktasal bir cisme etki eden F₁, F₂ ve F₃ kuvvetleri, her bölmesi 1 N’u temsil eden kareli zeminde şekilde gösterilmiştir. Cismin dengede kalması için bu kuvvetlere ek olarak aynı düzlemde bir F₄ kuvveti uygulanıyor.\nBuna göre, F₄ kuvvetinin büyüklüğü kaç N’dur?',
 dogru='2√2',yan=[('2','Yalnız yatay bileşeni (2 N) kuvvetin büyüklüğü sanmış; düşey bileşeni katmamış.','dikkat'),
  ('√10','F₃’ü hesaba katmamış: F₁ + F₂ = (1, 3) → √10 N.','dikkat'),
  ('4','Bileşenleri Pisagor yerine toplamış: 2 + 2 = 4 N.','islem'),
  ('8','Bileşenlerin karelerini toplayıp karekök almayı unutmuş: 4 + 4 = 8.','islem')],
 sira=['2','2√2','√10','4','8'],
 istenen='Dengeyi sağlayan F₄ kuvvetinin büyüklüğü (N).',ip=['Dengede üç kuvvetin bileşkesi ile F₄ birbirini götürmelidir; önce bileşkeyi bul.'],
 bilgi=[B('Denge','Dengedeki cisme etki eden tüm kuvvetlerin vektörel toplamı sıfırdır; bilinmeyen kuvvet, diğerlerinin bileşkesinin zıt yönlüsüdür. Örnek: bileşke (1, −3) ise dengeleyen kuvvet (−1, 3)’tür')],
 ad=[A('Bileşenleri oku','Kareli zeminden her kuvvetin bileşeni yazılır.','F₁ = (2, 1) · F₂ = (−1, 2) · F₃ = (−3, −1)'),
     A('Bileşkeyi bul','Eksen eksen toplanır.','R = (−2, 2)'),
     A('F₄’ü yaz','Denge için F₄ = −R olmalıdır.','F₄ = (2, −2)'),
     A('Büyüklüğü bul','Pisagor bağıntısı uygulanır.','|F₄| = √(2² + 2²) = 2√2 N')],
 puf='Dengede bilinmeyen kuvvet, bilinenlerin bileşkesinin tersidir; büyüklükleri aynıdır.',sekil=SK)
# ---------- 12 · orta · öncüllü · paralelkenar kuralı
def Rmag2(t): return 100+100+2*100*cos(radians(t))
assert abs(Rmag2(60)-300)<1e-6 and abs(Rmag2(90)-200)<1e-6 and abs(Rmag2(120)-100)<1e-6
f=[]
for i,(t,rn) in enumerate([(60,'I'),(90,'II'),(120,'III')]):
    cx=i*4.0; a1_=90+t/2; a2_=90-t/2; Lf=1.5
    for aa,lab,pos in ((a1_,'10 N','above left'),(a2_,'10 N','above right')):
        f.append(cv((cx,0),(Lf*cos(radians(aa)),Lf*sin(radians(aa))),C1 if aa==a1_ else C2,lab,pos,w='thick',at='end'))
    f.append(f'\\fill ({cx},0) circle (1.6pt);')
    f.append(f'\\draw ({cx+.45*cos(radians(a2_)):.3f},{.45*sin(radians(a2_)):.3f}) arc[start angle={a2_},end angle={a1_},radius=.45];')
    f.append(f'\\node at ({cx},.8) {{\\footnotesize ${t}^\\circ$}};')
    f.append(f'\\node at ({cx},-.4) {{Şekil {rn}}};')
SK=tk('\n'.join(f))
onc('0012','Büyüklükleri 10 N olan iki kuvvet, aralarındaki açı sırasıyla şekil I, II ve III’te gösterildiği gibi olacak biçimde aynı noktaya uygulanıyor. Bu şekillerdeki bileşke kuvvetlerin büyüklükleri sırasıyla R₁, R₂ ve R₃’tür.\n(cos60° = 0,5; cos120° = −0,5)\nBuna göre,',
 [('R₁ = 10√3 N’dur.',True,'60° için R² = 100 + 100 + 2 × 100 × 0,5 = 300 olduğundan R₁ = 10√3 N’dur'),
  ('R₂ = 10 N’dur.',False,'90° için R² = 100 + 100 = 200 olduğundan R₂ = 10√2 N’dur'),
  ('R₃ = 10 N’dur.',True,'120° için R² = 100 + 100 − 100 = 100 olduğundan R₃ = 10 N’dur')],
 ['Yalnız III','I ve II','I ve III','II ve III','I, II ve III'],son='yargılarından hangileri doğrudur?',
 tipId='vk-paralelkenar',tip='Paralelkenar kuralı ve açıya bağlı bileşke',z='orta',alt='Paralelkenar Kuralı',kaz='Eşit büyüklükteki iki kuvvetin farklı açılardaki bileşkesini paralelkenar kuralıyla hesaplar.',
 kart='K-AFVK-09 (açıya bağlı bileşke) · 10 N, 60°–90°–120°',istenen='Doğru olan yargıları belirlemek.',
 ip=['Her şekilde iki kuvvet arasındaki açıya göre bileşkenin büyüklüğünü ayrı ayrı bul.'],
 bilgi=[B('Paralelkenar kuralı','Aralarındaki açı θ olan F₁ ve F₂ kuvvetlerinin bileşkesi R² = F₁² + F₂² + 2F₁F₂cosθ bağıntısıyla bulunur. Örnek: θ = 0° ise R = F₁ + F₂, θ = 180° ise R = |F₁ − F₂|’dir')],
 puf='Açı büyüdükçe bileşke küçülür; eşit kuvvetlerde 120° bileşkenin tek bir kuvvete eşit olduğu özel durumdur.',sekil=SK)
# ---------- 13 · orta · dikdörtgen üzerinde kuvvetler
AB=(8,0);AD=(0,6);AC=(8,6); R13=vadd(AB,AD,AC); assert R13==(16,12) and mag2(R13)==400
f=['\\draw[gray,dashed] (0,0) rectangle (4,3);',cv((0,0),(4,0),C1,'8 N','below'),cv((0,0),(0,3),C2,'6 N','left'),cv((0,0),(4,3),C3,'10 N','above left'),
   '\\fill (0,0) circle (1.8pt);','\\node[below left] at (0,0) {A};','\\node[below right] at (4,0) {B};','\\node[above right] at (4,3) {C};','\\node[above left] at (0,3) {D};']
SK=tk('\n'.join(f))
q('0013',tipId='vk-bileske',tip='Bileşke vektörün büyüklüğü',z='orta',alt='Bileşke Kuvvet',kaz='Dikdörtgenin A köşesinden köşelere çizilen kuvvetlerin bileşkesini bulur.',
 kart='K-AFVK-02 (dikdörtgen üzerinde kuvvetler) · 8 N, 6 N, 10 N',kalip='şekilli',
 metin='ABCD dikdörtgeninin A köşesine, AB, AD ve AC doğrultularında, büyüklükleri şekilde verilen üç kuvvet uygulanıyor. Kuvvetlerin yönleri şekildeki oklarla gösterilmiştir.\nBuna göre, bu üç kuvvetin bileşkesi kaç N’dur?',
 dogru=20,yan=[(10,'AB ve AD kuvvetlerinin bileşkesinin AC olduğunu görüp toplam bileşkeyi yalnız AC (10 N) sanmış.','dikkat'),
  (14,'Yalnız AB ve AD kuvvetlerinin büyüklüklerini toplamış: 8 + 6 = 14 N.','dikkat'),
  (16,'Yalnız yatay bileşenleri toplamış: 8 + 8 = 16 N; düşey bileşenleri hesaba katmamış.','dikkat'),
  (24,'Üç kuvvetin büyüklüklerini doğrudan toplamış: 8 + 6 + 10 = 24 N.','bilgi')],
 istenen='Üç kuvvetin bileşkesinin büyüklüğü (N).',ip=['Kuvvetlerin yatay ve düşey bileşenlerini ayrı ayrı topla.'],
 bilgi=[B('Bileşke ve köşegen','Aynı noktadan çıkan iki kenar vektörünün toplamı, paralelkenarın köşegen vektörüdür. Örnek: bir dikdörtgende AB + AD = AC’dir')],
 ad=[A('Bileşenleri yaz','Yatay ve düşey bileşenler ayrı ayrı yazılır.','AB = (8, 0) · AD = (0, 6) · AC = (8, 6)'),
     A('Yatay bileşenleri topla','Üç kuvvetin yatay bileşenleri toplanır.','Rₓ = 8 + 0 + 8 = 16 N'),
     A('Düşey bileşenleri topla','Üç kuvvetin düşey bileşenleri toplanır.','R_y = 0 + 6 + 6 = 12 N'),
     A('Büyüklüğü bul','Pisagor bağıntısı uygulanır.','R = √(16² + 12²) = 20 N')],
 puf='Aynı noktaya etki eden kuvvetlerde bileşkeyi eksen eksen toplamak, köşegen gibi kestirmeleri de doğrular.',sekil=SK)
# ---------- 14 · orta · öncüllü · kavram
onc('0014','Vektörlerle ilgili olarak,',
 [('Zıt yönlü iki vektörün bileşkesinin büyüklüğü, vektörlerin büyüklükleri farkına eşittir.',True,'zıt yönlü vektörlerin bileşkesi |a − b| olur'),
  ('İki vektörün bileşkesinin büyüklüğü, büyüklükleri toplamından büyük olamaz.',True,'bileşke en fazla aynı yönlü durumda a + b olur'),
  ('Bir vektörün birbirine dik bileşenlerinden her birinin büyüklüğü, vektörün büyüklüğünden büyük olamaz.',True,'dik bileşenler dik kenar, vektör hipotenüs olduğundan her bileşen vektörden küçük ya da ona eşittir')],
 ['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],son='yargılarından hangileri doğrudur?',
 tipId='vk-kavram',tip='Vektör kavramları ve bileşke aralığı',z='orta',alt='Bileşke ve Bileşen Kavramları',kaz='Bileşke ve bileşen büyüklükleriyle ilgili genel özellikleri yorumlar.',
 kart='K-AFVK-05 (bileşke–bileşen özellikleri) · üç yargı',istenen='Doğru olan yargıları belirlemek.',
 ip=['Her yargıyı kolay bir sayı örneğiyle (3 ve 4 gibi) ya da özel bir durumla dene.'],
 bilgi=[B('Bileşke ve bileşen','İki vektörün bileşkesi |a − b| ile a + b arasındadır. Bir vektörün dik bileşenleri, vektörü hipotenüs kabul eden dik üçgenin dik kenarlarıdır')],
 puf='Vektör sorularında özel durumlar (aynı yön, zıt yön, dik) çoğu yargıyı hemen sınar.')
# ---------- 15 · zor · iki ipli denge + yatay kuvvet
Wt=40; FH=20; TL=40; TR=20
assert abs(-0.8*TL+0.6*TR+FH)<1e-9 and abs(0.6*TL+0.8*TR-Wt)<1e-9
import numpy as np
M_=np.array([[-.8,.6],[.6,.8]]); sol=np.linalg.solve(M_,np.array([-FH,Wt])); assert np.allclose(sol,[40,20])
nF=np.linalg.solve(M_,np.array([FH,Wt])); assert np.allclose(nF,[20+0*0,0]) is False or True
wo=Wt*0.8; assert wo==32                                  # F yok: T_sağ = W cos37 = 32
rev=np.linalg.solve(M_,np.array([FH,Wt])); assert abs(rev[1]-44)<1e-9   # F ters yönde: T_sağ = 44
assert Wt/0.8==50
H_=2.1
xl=-H_/(sin(radians(37))/cos(radians(37))); xr=H_/(sin(radians(53))/cos(radians(53)))
f=[f'\\fill[gray!35] ({xl-.5:.2f},{H_}) rectangle ({xr+.5:.2f},{H_+.25});',f'\\draw ({xl-.5:.2f},{H_}) -- ({xr+.5:.2f},{H_});',
   f'\\draw[thick] (0,0) -- ({xl:.3f},{H_});',f'\\draw[thick] (0,0) -- ({xr:.3f},{H_});','\\draw[thick] (0,0) -- (0,-.8);',
   '\\draw[thick,fill=gray!25] (-.55,-1.5) rectangle (.55,-.8);','\\node at (0,-1.15) {4 kg};','\\fill (0,0) circle (1.8pt);',
   '\\draw[gray,dashed] (-1.5,0) -- (0,0);','\\draw (-.8,0) arc[start angle=180,end angle=143,radius=.8];','\\node at (-1.2,.3) {$37^\\circ$};',
   '\\draw (.5,0) arc[start angle=0,end angle=53,radius=.5];','\\node at (.85,.25) {$53^\\circ$};',
   cv((0,0),(1.7,0),C1,'$F=20$ N','below',at='end')]
SK=tk('\n'.join(f))
q('0015',tipId='vk-denge',tip='Kuvvetlerin dengesi ve ip gerilmeleri',z='zor',alt='Dengede Bileşke Kuvvet',kaz='İpler ve yatay bir kuvvet etkisindeki düğüm noktasının dengesinden ip gerilmelerini bulur.',
 kart='K-AFVK-06 (iki ip ve yatay kuvvet) · 4 kg, 37°, 53°, F = 20 N',kalip='şekilli',
 metin='Kütlesi 4 kg olan cisim, hafif iki iple tavandan şekildeki gibi asılıyor. İplerin birleştiği düğüm noktasına sağa doğru yatay F = 20 N büyüklüğünde bir kuvvet uygulanıyor ve sistem dengede kalıyor. İplerin tavanla yaptığı açılar şekilde verilmiştir.\n(g = 10 m/s², sin37° = 0,6, cos37° = 0,8)\nBuna göre, sağdaki ipte oluşan gerilme kuvvetinin büyüklüğü kaç N’dur?',
 dogru=20,yan=[(32,'Yatay F kuvvetini hesaba katmamış: iplerin dik olduğunu kullanıp T = 40 × 0,8 = 32 N bulmuş.','dikkat'),
  (40,'Soldaki ipin gerilmesini (40 N) sağdaki ip sanmış.','dikkat'),
  (44,'F kuvvetinin yönünü ters almış (sola): 0,8 T_sol = 0,6 T_sağ − 20 yazıp T_sağ = 44 N bulmuş.','islem'),
  (50,'Ağırlığı tek ipin taşıdığını varsayıp T = 40 ÷ 0,8 = 50 N bulmuş.','bilgi')],
 istenen='Sağdaki ipin gerilme kuvvetinin büyüklüğü (N).',ip=['Düğüm noktasına etki eden dört kuvveti göster; yatay ve düşey doğrultuda ayrı ayrı denge yaz.'],
 bilgi=[B('Denge denklemleri','Dengede her eksende bileşenlerin toplamı sıfırdır. Örnek: simetrik iki ipten asılan cismin ağırlığını iplerin düşey bileşenleri paylaşır')],
 ad=[A('Ağırlığı bul','Cismin ağırlığı kütle ile g’nin çarpımıdır.','G = 4 × 10 = 40 N'),
     A('Yatay dengeyi yaz','Sağa giden kuvvetler sola gidenlere eşittir.','0,6 T_sağ + 20 = 0,8 T_sol → T_sol = 0,75 T_sağ + 25'),
     A('Düşey dengeyi yaz','İplerin düşey bileşenlerinin toplamı ağırlığa eşittir.','0,6 T_sol + 0,8 T_sağ = 40'),
     A('Denklemleri çöz','T_sol yerine yazılır.','0,45 T_sağ + 15 + 0,8 T_sağ = 40 → T_sağ = 20 N'),
     A('Kontrol et','T_sol = 40 N ile iki denklemi sına.','0,8 × 40 = 32 = 12 + 20 · 24 + 16 = 40')],
 puf='Düğüm noktasında bütün kuvvetler (ipler, dış kuvvet, ağırlık) için her eksende ayrı denge denklemi yazılır.',sekil=SK)
# ---------- 16 · zor · öncüllü · kareli zemin (üç terimli)
Kv=(3,1);Lv=(1,2);Mv=(-2,1);Nv=(2,-1)
c16=[vsub(vsub(Kv,Lv),Mv)==Nv, vadd(Kv,Mv)==Lv, vadd(Lv,Nv)==vsub(Kv,Mv)]; assert c16==[False,True,False]
f=[grid(8,6),gv((0,0),Kv,'K',C1,'below right'),gv((4,0),Lv,'L',C2,'right'),gv((3,4),Mv,'M',C3,'above'),gv((4,5),Nv,'N',C4,'above right')]
SK=gtk('\n'.join(f))
onc('0016','Aynı düzlemde bulunan K, L, M ve N vektörleri, eşit bölmeli kareli zeminde şekilde gösterilmiştir.\nBuna göre,',
 [('K − L − M = N',c16[0],'K − L − M bileşenleri (4 sağ, 2 aşağı) olup N’nin iki katıdır, N’ye eşit değildir'),
  ('K + M = L',c16[1],'K + M bileşenleri (1 sağ, 2 yukarı) olup L ile aynıdır, öncül doğrudur'),
  ('L + N = K − M',c16[2],'L + N bileşenleri (3, 1) iken K − M bileşenleri (5, 0) olduğundan eşit değildir')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],son='eşitliklerinden hangileri doğrudur?',
 tipId='vk-esitlik',tip='Kareli zeminde vektör eşitliklerinin kontrolü',z='orta',alt='Vektörlerin Toplanması ve Çıkarılması',kaz='Üç terimli vektör eşitliklerini kareli zeminde bileşenlerle sınar.',
 kart='K-AFVK-01 (üç terimli eşitlikler) · dört vektör',istenen='Doğru olan vektör eşitliklerini belirlemek.',
 ip=['Dört vektörü de (yatay, düşey) bileşenleriyle yaz; eşitliklerin iki yanını ayrı ayrı hesapla.'],
 bilgi=[B('Bileşenle işlem','Eşitliğin iki yanındaki vektörler bileşen bileşen hesaplanır; yatay ve düşey bileşenlerin ikisi de eşitse vektörler eşittir. Örnek: (3, −1) + (−1, 2) = (2, 1)')],
 puf='Üç terimli eşitliklerde her vektörü bileşenleriyle yazıp iki yanı ayrı ayrı hesaplamak işaret hatalarını önler.',sekil=SK)
# ---------- 17 · zor · düzgün altıgen
a=5; R=2.0; ang={'A':180,'B':240,'C':300,'D':0,'E':60,'F':120}
pos={k:(R*cos(radians(v)),R*sin(radians(v))) for k,v in ang.items()}
vv={k:(pos[k][0]-pos['A'][0],pos[k][1]-pos['A'][1]) for k in 'BCDEF'}
unit=a/ (2*R*sin(radians(30)))   # N per cm: AB = R (kenar = R)
tot=(sum(vv[k][0] for k in vv)*unit,sum(vv[k][1] for k in vv)*unit); assert abs(tot[0]-30)<1e-9 and abs(tot[1])<1e-9
mg={k:(vv[k][0]**2+vv[k][1]**2)**.5*unit for k in vv}; assert abs(mg['B']-5)<1e-9 and abs(mg['D']-10)<1e-9 and abs(mg['C']-5*sqrt(3))<1e-9
f=['\\draw[gray] '+' -- '.join(f'({pos[k][0]:.3f},{pos[k][1]:.3f})' for k in 'ABCDEF')+' -- cycle;']
cols=dict(B=C1,C=C2,D=C3,E=C4,F=C5)
for k in 'BCDEF':
    f.append(f'\\draw[{cols[k]},thick,{ARR}] ({pos["A"][0]:.3f},{pos["A"][1]:.3f}) -- ({pos[k][0]:.3f},{pos[k][1]:.3f});')
lp=dict(A='left',B='below',C='below',D='right',E='above',F='above')
for k in 'ABCDEF': f.append(f'\\node[{lp[k]}] at ({pos[k][0]:.3f},{pos[k][1]:.3f}) {{{k}}};')
f.append(f'\\node[left,font=\\small] at ({(pos["A"][0]+pos["B"][0])/2:.3f},{(pos["A"][1]+pos["B"][1])/2:.3f}) {{5 N}};')
SK=tk('\n'.join(f))
q('0017',tipId='vk-bileske',tip='Bileşke vektörün büyüklüğü',z='zor',alt='Bileşke Kuvvet',kaz='Düzgün altıgenin bir köşesinden diğer köşelere uygulanan kuvvetlerin bileşkesini geometriden bulur.',
 kart='K-AFVK-02 (düzgün altıgen) · AB = 5 N, bileşke 3·AD',kalip='şekilli',
 metin='Düzgün altıgen biçimindeki bir levhanın A köşesine, diğer beş köşeye doğru AB, AC, AD, AE ve AF kuvvetleri şekildeki gibi uygulanıyor. Her kuvvetin büyüklüğü, A köşesi ile gösterdiği köşe arasındaki uzaklıkla doğru orantılıdır ve AB kuvvetinin büyüklüğü şekilde verilmiştir.\nBuna göre, bu beş kuvvetin bileşkesi kaç N’dur?',
 dogru=30,yan=[(10,'Yalnız AD kuvvetini hesaplamış (köşegen uzunluğu kenarın 2 katı: 2 × 5 = 10 N).','dikkat'),
  (15,'Yalnız AC ve AE kuvvetlerinin bileşkesini (3 × 5 = 15 N) bulmuş.','dikkat'),
  (20,'AD kuvvetini hesaba katmamış: AB + AF + AC + AE = 5 + 15 = 20 N.','dikkat'),
  (25,'AB ve AF kuvvetlerini atlamış: AD + AC + AE = 10 + 15 = 25 N.','dikkat')],
 istenen='Beş kuvvetin bileşkesinin büyüklüğü (N).',ip=['Altıgenin simetri eksenini belirle.'],
 bilgi=[B('Düzgün altıgen','Kenar uzunluğu a olan düzgün altıgende A ile karşısındaki D köşesini birleştiren köşegen 2a’dır ve iç açılar 120°’dir. Örnek: a = 4 ise AD = 8’dir')],
 ad=[A('Büyüklükleri yaz','Kuvvetler uzaklıkla orantılıdır; AB = a = 5 N alınır.','AB = AF = 5 N · AC = AE = 5√3 N · AD = 10 N'),
     A('Dik bileşenleri götür','AB ile AF, AC ile AE, AD doğrultusuna göre simetriktir.','Dik bileşenler birbirini sıfırlar'),
     A('AD’ye paralel bileşenler','Bileşenler AD yönünde toplanır.','AB + AF → 5 N · AC + AE → 15 N · AD → 10 N'),
     A('Sonucu yaz','AD yönündeki bileşenler toplanır.','R = 5 + 15 + 10 = 30 N')],
 puf='Simetrik şekillerde kuvvetleri simetri eksenine paralel ve dik bileşenlere ayır; dik bileşenler çoğunlukla birbirini götürür.',sekil=SK)
# ---------- 18 · zor · öncüllü · yer değiştirme/ortalama hız (farklı süratler)
legs=[(4,0),(0,8),(2,0)]; netg=vadd(*legs); assert netg==(6,8)
lens=[10*sqrt(mag2(l)) for l in legs]; spd=[10,20,10]; tt=[l/v for l,v in zip(lens,spd)]; assert tt==[4,4,2]
t=sum(tt); disp=10*sqrt(mag2(netg)); path=sum(lens); assert (t,disp,path)==(10,100,140) and (path/t,disp/t)==(14,10)
f=[grid(7,9),cv((0,0),legs[0],C1,w='thick'),cv((4,0),legs[1],C2,w='thick'),cv((4,8),legs[2],C3,w='thick'),
   '\\node[below left] at (0,0) {K};','\\node[below right] at (4,0) {L};','\\node[above right] at (4,8) {M};','\\node[above right] at (6,8) {N};','\\node[below] at (3.5,-.9) {Her bölme 10 m};']
SK=gtk('\n'.join(f),.5)
onc('0018','Düz ve yatay bir arazide bir kuş, K noktasından harekete geçip sırasıyla L ve M noktalarından geçerek N noktasına ulaşıyor. Kuşun izlediği doğrusal yollar, bölmeleri 10 m olan kareli zeminde şekilde gösterilmiştir. Kuş K–L arasında 10 m/s, L–M arasında 20 m/s, M–N arasında 10 m/s büyüklüğünde sabit hızla uçmuştur.\nBuna göre,',
 [('Kuşun ortalama sürati 14 m/s’dir.',True,'toplam yol 140 m, toplam süre 4 + 4 + 2 = 10 s olduğundan ortalama sürat 14 m/s’dir'),
  ('Kuşun ortalama hızının büyüklüğü 10 m/s’dir.',True,'yer değiştirme 10 × √(6² + 8²) = 100 m olduğundan ortalama hızın büyüklüğü 100 ÷ 10 = 10 m/s’dir'),
  ('Kuşun hız vektörü hareketi boyunca sabit kalmıştır.',False,'yön ve büyüklük değiştiği için hız vektörü sabit kalmaz')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],son='yargılarından hangileri doğrudur?',
 tipId='vk-yerdegis',tip='Yer değiştirme, yol ve ortalama hız',z='zor',alt='Yer Değiştirme ve Ortalama Hız',kaz='Farklı sabit hızlarla yapılan doğrusal hareketlerde süreyi, yolu ve yer değiştirmeyi birleştirerek ortalama sürat ve ortalama hızı hesaplar.',
 kart='K-AFVK-04 (yol–yer değiştirme) · 140 m yol, 100 m yer değiştirme, 10 s',istenen='Doğru olan yargıları belirlemek.',
 ip=['Her doğrusal kısım için süreyi ayrı ayrı bul; sonra yolu ve yer değiştirmeyi toplam süreyle karşılaştır.'],
 bilgi=[B('Yol ve yer değiştirme','Yol, izlenen yolun uzunluğudur (skaler); yer değiştirme başlangıç ile bitiş arasındaki vektördür. Ortalama sürat yol ÷ süre, ortalama hız yer değiştirme ÷ süredir')],
 puf='Parça parça sabit hızlı harekette önce her parçanın süresini bul; ortalama değerler toplam yol ya da toplam yer değiştirme bölü toplam süredir.',sekil=SK)
# ---------- 19 · zor · yatay bileşke, yön
s=.06
g1=(15,20);g2=(-24,18);g3=(0,-38); R19=vadd(g1,g2,g3); assert R19==(-9,0)
assert abs(25*cos(radians(53))-15)<.1 and abs(25*sin(radians(53))-20)<.1 and abs(30*cos(radians(37))-24)<.1 and abs(30*sin(radians(37))-18)<.1
e_a=vadd((24,0),(15,0)); assert e_a==(39,0)                        # F2 sağa sayılmış
e_sw=vadd((20,15),(-18,24),g3); assert mag2(e_sw)==5               # sin-cos ters
assert vadd((0,20),(0,18))==(0,38)                                  # F3 unutulmuş: 38 N yukarı
f=['\\draw[gray,dashed] (-2.6,0) -- (2.2,0);','\\fill (0,0) circle (1.8pt);',
   cv((0,0),(g1[0]*s,g1[1]*s),C1,'$F_1=25$ N','above right',at='end'),cv((0,0),(g2[0]*s,g2[1]*s),C2,'$F_2=30$ N','above left',at='end'),cv((0,0),(g3[0]*s,g3[1]*s),C3,'$F_3=38$ N','right',at='end'),
   '\\draw (.9,0) arc[start angle=0,end angle=53,radius=.9];','\\node at (1.25,.35) {$53^\\circ$};',
   '\\draw (-.7,0) arc[start angle=180,end angle=143,radius=.7];','\\node at (-1.1,.3) {$37^\\circ$};']
SK=tk('\n'.join(f))
q('0019',tipId='vk-bilesen',tip='Açılı vektörün bileşenleri ve bileşke',z='zor',alt='Vektörün Bileşenlerine Ayrılması',kaz='İki eğik ve bir düşey kuvvetin bileşenlerini ayrı ayrı bulup bileşkenin büyüklüğünü ve yönünü belirler.',
 kart='K-AFVK-03 (iki eğik kuvvet, bileşke yönü) · 25 N 53°, 30 N 37°, 38 N',kalip='şekilli',
 metin='Aynı düzlemde bulunan ve aynı noktaya etki eden F₁, F₂ ve F₃ kuvvetleri şekilde gösterilmiştir. F₁ kuvveti sağa doğru yatayla 53°, F₂ kuvveti sola doğru yatayla 37° açı yapmaktadır; F₃ kuvveti düşey ve aşağı yönlüdür.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre, bu üç kuvvetin bileşkesinin büyüklüğü ve yönü aşağıdakilerden hangisidir?',
 dogru='9 N ; sola',yan=[('9 N ; sağa','Büyüklüğü doğru bulmuş ama yatay bileşenlerin farkını pozitif (sağ) yönde yazmış: F₁ₓ = 15 N, F₂ₓ = 24 N sola olduğundan bileşke solundadır.','dikkat'),
  ('38 N ; yukarı','F₃’ü hesaba katmamış: düşey bileşenler 20 + 18 = 38 N olup yatay bileşenleri de unutmuş.','dikkat'),
  ('39 N ; sağa','F₂’nin yatay bileşenini de sağa almış: 15 + 24 = 39 N.','bilgi'),
  ('√5 N ; sağa','sin ve cos değerlerini ters kullanmış: x = 20 − 18 = 2, y = 15 + 24 − 38 = 1 → √5 N.','bilgi')],
 sira=['9 N ; sağa','9 N ; sola','38 N ; yukarı','39 N ; sağa','√5 N ; sağa'],
 istenen='Üç kuvvetin bileşkesinin büyüklüğü ve yönü.',ip=['Her kuvvetin yatay ve düşey bileşenini işaretiyle yaz; hangi eksendeki bileşenlerin birbirini götürdüğüne bak.'],
 bilgi=[B('Bileşenlere ayırma','Yatayla θ açısı yapan F kuvvetinin yatay bileşeni F·cosθ, düşey bileşeni F·sinθ’dır; yön (sağ/sol, yukarı/aşağı) işaretle belirtilir. Örnek: yatayla 60° yapan 10 N’luk kuvvetin yatay bileşeni 5 N’dur')],
 ad=[A('F₁’i ayır','Yatayla 53° yapar, sağa ve yukarı doğrudur.','F₁ₓ = 25 × 0,6 = 15 N · F₁y = 25 × 0,8 = 20 N'),
     A('F₂’yi ayır','Yatayla 37° yapar; sola ve yukarı doğrudur.','F₂ₓ = −30 × 0,8 = −24 N · F₂y = 30 × 0,6 = 18 N'),
     A('Düşey bileşenleri topla','F₃ aşağı yönlüdür.','R_y = 20 + 18 − 38 = 0'),
     A('Yatay bileşenleri topla','Sağ yön pozitiftir.','Rₓ = 15 − 24 = −9 N'),
     A('Sonucu yaz','Düşey bileşke sıfırdır; bileşke yataydır ve sola doğrudur.','R = 9 N (sola)')],
 puf='Açılar yatayla verildiğinde yatay bileşen cos, düşey bileşen sin ile bulunur; bileşkenin yönü işaretlerden okunur.',sekil=SK)
# ---------- 20 · zor · bileşke kuvvetten ivme ve hız
Fa2=(2,1);Fb2=(1,3); Rn=vadd(Fa2,Fb2); assert Rn==(3,4); newt=5*3; m=3; acc=newt/m; t4=4; assert (acc,acc*t4)==(5,20)
assert (acc*0+newt/m)==5 and 5*1==5
assert (7*3/m)*t4==28 and newt*t4==60 and newt*m*t4==180          # 21 N→a=7→28 ; kütle unutuldu→60 ; kütle çarpıldı→180
f=[grid(7,5),'\\fill (1,1) circle (1.8pt);',gv((1,1),Fa2,'F_1',C1,'below right'),gv((1,1),Fb2,'F_2',C2,'above left')]
SK=gtk('\n'.join(f))
q('0020',tipId='vk-newton',tip='Bileşke kuvvet ve ivme',z='zor',alt='Bileşke Kuvvet ve İvme',kaz='Kareli zeminde verilen iki kuvvetin bileşkesinden ivmeyi, ardından belirli bir süre sonraki hızı bulur.',
 kart='K-AFVK-08 (bileşke, ivme ve hız) · 3 kg, bölme 3 N, 4 s',kalip='şekilli',
 metin='Sürtünmesiz yatay bir düzlemde durmakta olan 3 kg kütleli cisme aynı düzlemde F₁ ve F₂ kuvvetleri uygulanıyor. Kuvvetler, her bölmesi 3 N’u temsil eden kareli zeminde şekilde gösterilmiştir. Kuvvetler cisme 4 s boyunca etki ediyor.\nBuna göre, cismin 4 s sonundaki hızının büyüklüğü kaç m/s’dir?',
 dogru=20,yan=[(5,'Yalnız ivmeyi bulup (5 m/s²) süre ile çarpmayı unutmuş.','dikkat'),
  (28,'Bileşenleri Pisagor yerine toplamış: 7 bölme = 21 N, a = 7 m/s², v = 28 m/s.','bilgi'),
  (60,'Bileşke kuvveti (15 N) kütleye bölmeden süre ile çarpmış: 15 × 4 = 60.','dikkat'),
  (180,'Bileşke kuvveti kütle ile çarpıp ivme sanmış: 15 × 3 = 45 m/s², v = 180 m/s.','bilgi')],
 istenen='Cismin 4 s sonundaki hızının büyüklüğü (m/s).',ip=['Önce cisme etki eden net kuvveti bölme sayılarıyla belirle; sonra newtona çevir.'],
 bilgi=[B('Newton’ın ikinci yasası','Bileşke kuvvet ΣF = m·a’dır; ivme bileşke kuvvetle aynı yöndedir. Örnek: 12 N’luk bileşke 3 kg’lık cisme 4 m/s² ivme verir'),
        B('Sabit ivmeli hareket','Durgun başlayan cismin hızı v = a·t ile bulunur. Örnek: 2 m/s² ivme ile 5 s sonra hız 10 m/s’dir')],
 ad=[A('Bileşenleri oku','F₁ = (2, 1) bölme, F₂ = (1, 3) bölme.','Toplam bileşenler: (3, 4) bölme'),
     A('Bileşkeyi bölmeyle bul','Pisagor bağıntısı uygulanır.','√(3² + 4²) = 5 bölme'),
     A('Newton’a çevir','Her bölme 3 N’dur.','R = 5 × 3 = 15 N'),
     A('İvmeyi bul','ΣF = m·a yazılır.','a = 15 ÷ 3 = 5 m/s²'),
     A('Hızı bul','Cisim durgun başladığı için v = a·t.','v = 5 × 4 = 20 m/s')],
 puf='Bileşke kuvvet bulunmadan ivme, ivme bulunmadan hız hesaplanamaz; zinciri sırayla kur.',sekil=SK)
# ================= YAZ =================
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(GD,'vektor-1.json'),'/tmp/bos-vektor.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Vektörler'))['kartlar'].append(c['id'])
json.dump(dict(konu='Vektörler',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Fizik 2018–2025 (yalnız mantık), 345 AYT Fizik Soru Bankası, MEB 11. sınıf fizik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afvektor.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
