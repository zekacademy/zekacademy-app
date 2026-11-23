"""AYT Fizik · Elektrik Alan ve Potansiyel · 20 soru (3 kolay / 11 orta / 6 zor). Şekiller TikZ (cizim.tikz_svg); her cevap ve çeldirici Python'da hesaplanıp assert edilir."""
import sys,os,re,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,radians,sqrt
P=Parti('elalan','Elektrik Alan ve Potansiyel','afiz|Elektrik Alan ve Potansiyel',ders='AYT Fizik',idon='aytfiz')
P.konu_adi='Elektrik Alan ve Potansiyel'; H.KONU='Elektrik Alan ve Potansiyel'
KAY='ÖSYM AYT Fizik 2018–2025 (yalnız mantık) · 345 AYT Fizik s.190–240 · MEB 11. sınıf fizik'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAY)
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
RED,BLUE,GRN,ORG='red!75!black','blue!70!black','green!45!black','orange!90!black'
def tk(govde,ust='[line cap=round,line join=round,font=\\small]'): return tikz_svg('\\begin{tikzpicture}'+ust+'\n'+govde+TAIL)
def yuk(x,y,sg,lab,pos='below',col=None):
    c=col or (RED if sg>0 else BLUE); s='$+$' if sg>0 else '$-$'
    return f'\\node[circle,draw={c},thick,fill={c}!15,inner sep=0pt,minimum size=.55cm,label={{[{c}]{pos}:{lab}}}] at ({x},{y}) {{{s}}};'
def nok(x,y,lab,pos='above'): return f'\\fill ({x},{y}) circle (2pt) node[{pos}] {{{lab}}};'
def olc(x1,x2,y,lab,ust=True):
    sg=1 if y>0 else -1
    g=''.join(f'\\draw[gray!60,thin] ({x},{sg*.32}) -- ({x},{y});' for x in (x1,x2))
    return g+f'\\draw[<->,thin] ({x1},{y}) -- ({x2},{y}) node[midway,{"above" if ust else "below"},fill=white,inner sep=1pt] {{{lab}}};'
def bil(x,y,lab=None,sol=True):
    c='gray!70!black'; n=f'\\node[circle,draw={c},thick,fill=gray!15,inner sep=0pt,minimum size=.55cm,label={{[{c}]above:{lab}}}] at ({x},{y}) {{?}};'
    return n
K9=Fr(9*10**9); MIK=Fr(1,10**6)
def cfm(x): return fm(x)
# ================= KARTLAR =================
kartla('K-AFEA-01','Coulomb kuvveti','İki noktasal yük arasındaki kuvvet F = k·q₁q₂/r² ile bulunur: yüklerin çarpımıyla doğru, uzaklığın karesiyle ters orantılıdır; kuvvetler etki–tepki çiftidir.','Uzaklığı kare almadan kullanmak; yüklerden yalnız birinin değişimini hesaba katmak; iki yüke etki eden kuvvetleri farklı sanmak.','orta','şekilli',3,'ea-coulomb','Coulomb kuvveti ve bileşke kuvvet')
kartla('K-AFEA-02','Noktasal yüklerin elektrik alanı','E = k·q/r²; alan vektörel olup pozitif yükten uzağa, negatif yüke doğrudur. Birden çok yükün alanı vektörel toplanır; iki yük arasındaki sıfır alan noktası büyük yükten uzaktadır.','Alan vektörlerini büyüklük olarak toplamak; yönleri karıştırmak; sıfır noktasını küçük yüke yakın sanmak.','orta','şekilli',4,'ea-alan','Noktasal yüklerin elektrik alanı')
kartla('K-AFEA-03','Elektriksel potansiyel','V = k·q/r skalerdir ve işaretlidir; birden çok yükün potansiyeli cebirsel toplanır; V ile 1/r orantılıdır, 1/r² ile değil.','Potansiyeli vektör gibi toplamak; işareti atlamak; uzaklığın karesini kullanmak.','orta','şekilli',3,'ea-potansiyel','Elektriksel potansiyel ve potansiyel farkı')
kartla('K-AFEA-04','Potansiyel enerji ve iş','Yük taşınırken elektriksel kuvvetin işi W = q(V_i − V_s) ve potansiyel enerji değişimi ΔU = q·ΔV; iş yoldan bağımsız, eş potansiyel yüzeyde sıfırdır. İki yükün enerjisi U = k·q₁q₂/r.','Yükün işaretini atlamak; işin yoldan bağımlı olduğunu sanmak; ΔV yerine V almak.','orta','şekilli',4,'ea-enerji','Elektriksel potansiyel enerji ve iş')
kartla('K-AFEA-05','Düzgün elektrik alan','Düzgün alanda V farkı ΔV = E·d (d alan doğrultusundaki uzaklık); alana dik doğrultuda potansiyel sabittir; yüklü parçacık sabit kuvvetle hızlanır.','Eğik yol uzunluğunu d almak; alana dik bileşeni potansiyel farkına katmak; yükün işaretiyle yönü karıştırmak.','orta','şekilli',4,'ea-duzgun','Düzgün elektrik alan ve yüklü parçacığın hareketi')
kartla('K-AFEA-06','Alan, potansiyel ve enerji kavramları','Alan çizgileri birbirini kesmez; iletken kürelerde değme sonrası potansiyel eşitlenir, yük yarıçapla orantılı dağılır; eşit yüklü bölgelerde alan ve potansiyel farklı büyüklüklerdir.','Alan ile potansiyeli aynı sanmak; yük paylaşımını eşit saymak; skaler–vektör ayrımını unutmak.','orta','öncüllü',3,'ea-kavram','Elektrik alan, potansiyel ve yük dağılımı kavramları')
kartla('K-AFEA-07','Elektriksel denge','Serbest yüklerin dengesinde her yüke etkiyen bileşke kuvvet sıfırdır; asılı yüklü cisimde ip gerilmesi, ağırlık ve elektriksel kuvvet bileşenlerinin dengesi yazılır; ip kopunca net kuvvet gerilmeye eşittir.','Tek yükün dengesiyle yetinmek; elektriksel kuvvetin yönünü ters almak; ip koptuktan sonra ağırlığı tek başına kullanmak.','zor','şekilli',5,'ea-denge','Yüklerin dengesi ve asılı yüklü cisim')
# ================= SORULAR =================
# ---------- 01 · kolay · Coulomb oranı
def Fc(a,b,r): return Fr(a)*Fr(b)/Fr(r)**2
f1=Fr(2)*Fr(2)*Fr(1)/Fr(4)**2; assert f1==Fr(1,4)
assert Fr(4)==Fr(2*2) and Fr(4,4)==1 and Fr(2,4)==Fr('0.5') and 4**2==16
SK=tk('\n'.join([yuk(0,0,1,'K ($+q$)'),yuk(4.2,0,1,'L ($+2q$)'),olc(0,4.2,.9,'$d$')]))
q('0001',tipId='ea-coulomb',tip='Coulomb kuvveti ve bileşke kuvvet',z='kolay',alt='Coulomb Kuvveti',kaz='Coulomb kuvvetinin yüklerin çarpımına ve uzaklığın karesine bağlılığını kullanarak kuvvetin değişimini bulur.',
 kart='K-AFEA-01 (Coulomb oranı) · yükler ×2, uzaklık ×4',kalip='şekilli',
 metin='Şekilde, noktasal K ve L yükleri aralarındaki uzaklık d iken birbirine F büyüklüğünde elektriksel kuvvet uyguluyor. Daha sonra her iki yükün büyüklüğü de iki katına çıkarılıyor ve aralarındaki uzaklık 4d yapılıyor. (Ortam değişmemektedir.)\nBuna göre, yükler arasındaki elektriksel kuvvetin büyüklüğü kaç F olur?',
 dogru=Fr(1,4),yan=[(4,'Uzaklığın etkisini hesaba katmamış; yalnız yüklerin çarpımındaki 2 × 2 = 4 katını almış.','dikkat'),
  (1,'Kuvvetin uzaklıkla ters orantılı olduğunu sanmış: yüklerden gelen 4 katı, uzaklıktan gelen 4’e bölmüş (4 ÷ 4 = 1).','bilgi'),
  (Fr('0.5'),'Yüklerin etkisini yalnız 2 kat almış ve kuvvetin uzaklıkla (karesiyle değil) ters orantılı olduğunu sanmış: 2 ÷ 4 = 0,5.','islem'),
  (16,'Uzaklığı artırdığı için kuvvetin karesiyle arttığını düşünüp yüklerin etkisini katmamış: 4² = 16.','bilgi')],
 istenen='Yeni kuvvetin büyüklüğünün F cinsinden değeri.',ip=['Coulomb bağıntısında yüklerin çarpımının ve uzaklığın nasıl yer aldığına bak; iki değişimi ayrı ayrı oranla.'],
 bilgi=[B('Coulomb kuvveti','İki noktasal yük arasındaki kuvvet, yüklerin çarpımıyla doğru, aralarındaki uzaklığın karesiyle ters orantılıdır. Örnek: uzaklık 3 katına çıkarsa kuvvet 9 kat azalır')],
 ad=[A('Yük etkisi','Kuvvet yüklerin çarpımıyla doğru orantılıdır; iki yük de 2 katına çıkınca çarpım 4 katına çıkar.','2 × 2 = 4'),
     A('Uzaklık etkisi','Kuvvet uzaklığın karesiyle ters orantılıdır; uzaklık 4 katına çıkınca kuvvet 16’ya bölünür.','1 ÷ 4² = 1 ÷ 16'),
     A('Oranı bul','İki değişim birlikte uygulanır.','F′ = F × 4 ÷ 16 = F ÷ 4 = 0,25 F')],
 puf='Bağıntıda yüklerin çarpımı payda, uzaklığın karesi paydada yer alır; iki değişimi ayrı ayrı oranlayıp birleştir.',sekil=SK)
# ---------- 02 · kolay · öncüllü · kavram
onc('0002','Elektriksel kuvvet, elektrik alan ve potansiyel kavramlarıyla ilgili aşağıdaki öncüller veriliyor.\nBuna göre,',
 [('Elektrik alan vektörel, elektriksel potansiyel skaler bir niceliktir.',True,'elektrik alan yön taşıyan vektörel, potansiyel ise yön taşımayan skaler bir niceliktir'),
  ('İki noktasal yük arasındaki elektriksel kuvvet, yükler arasındaki uzaklıkla ters orantılıdır.',False,'kuvvet uzaklıkla değil, uzaklığın karesiyle ters orantılıdır'),
  ('Elektrik alan çizgileri hiçbir noktada birbirini kesmez.',True,'bir noktadaki alanın tek bir yönü olduğundan alan çizgileri kesişmez')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],son='öncüllerinden hangileri doğrudur?',
 tipId='ea-kavram',tip='Elektrik alan, potansiyel ve yük dağılımı kavramları',z='kolay',alt='Temel Kavramlar',kaz='Elektriksel kuvvet, alan ve potansiyelin temel özelliklerini ayırt eder.',
 kart='K-AFEA-06 (temel kavramlar) · skaler–vektör, Coulomb bağımlılığı, alan çizgileri',istenen='Doğru olan öncülleri belirlemek.',
 ip=['Her öncülde sözü edilen niceliğin yön taşıyıp taşımadığını ve hangi bağıntıdan geldiğini düşün.'],
 bilgi=[B('Alan çizgileri','Alan çizgilerinin teğeti o noktadaki alanın yönünü verir; bir noktada tek yön olabildiği için çizgiler kesişmez. Örnek: bir noktasal yükün çizgileri yükten ışınsal yayılır'),
        B('Skaler ve vektör','Alan yön taşır, potansiyel yalnız işaretli bir sayıdır; bu yüzden alanlar vektörel, potansiyeller cebirsel toplanır. Örnek: kütle skaler, hız vektöreldir')],
 puf='Alan ve kuvvet vektörel, potansiyel ve potansiyel enerji skalerdir; bağıntılardaki uzaklık üssüne dikkat et.')
# ---------- 03 · kolay · V = kq/r
VK=90; assert VK*2//6==30 and Fr(VK*2,6)==30
SK=tk('\n'.join([yuk(0,0,1,'$+Q$','above'),nok(2,0,'K','above'),nok(-6,0,'L','above'),olc(0,2,-.7,'2 m',False),olc(-6,0,-.7,'6 m',False)]))
q('0003',tipId='ea-potansiyel',tip='Elektriksel potansiyel ve potansiyel farkı',z='kolay',alt='Noktasal Yükün Potansiyeli',kaz='Noktasal bir yükün potansiyelinin uzaklıkla ters orantılı değiştiğini kullanarak potansiyeli hesaplar.',
 kart='K-AFEA-03 (V = kq/r) · 2 m ve 6 m',kalip='şekilli',
 metin='Şekilde sabit noktasal +Q yükünün K ve L noktalarında oluşturduğu elektriksel potansiyeller karşılaştırılacaktır. K noktasındaki potansiyel 90 V’tur. Başka yük yoktur ve potansiyel sonsuzda sıfırdır.\nBuna göre, L noktasındaki potansiyel kaç V’tur?',
 dogru=30,yan=[(810,'Potansiyelin uzaklığın karesiyle doğru orantılı olduğunu sanmış: 90 × 3² = 810 V.','bilgi'),
  (45,'Uzaklığın 2 katına çıktığını düşünmüş: 90 ÷ 2 = 45 V.','dikkat'),
  (90,'Potansiyelin uzaklığa bağlı olmadığını sanmış.','bilgi'),
  (270,'Potansiyelin uzaklıkla doğru orantılı olduğunu sanmış: 90 × 3 = 270 V.','dikkat')],
 istenen='L noktasındaki elektriksel potansiyel (V).',ip=['V = kQ/r bağıntısında uzaklığın değişim oranını yaz.'],
 bilgi=[B('Noktasal yükün potansiyeli','Noktasal yükün r kadar uzağındaki potansiyel V = kq/r’dir ve uzaklıkla ters orantılıdır. Örnek: uzaklık 5 katına çıkarsa potansiyel 5 kat azalır')],
 ad=[A('Uzaklıkları yaz','Şekilden K ve L’nin +Q’ya uzaklıkları okunur.','r_K = 2 m · r_L = 6 m'),
     A('Orantıyı kur','V ile 1/r orantılıdır.','V_L ÷ V_K = r_K ÷ r_L = 2 ÷ 6'),
     A('Potansiyeli bul','Oran K’deki değere uygulanır.','V_L = 90 × 2 ÷ 6 = 30 V')],
 puf='Potansiyel uzaklıkla ters orantılıdır; kareyi alan bağıntı elektrik alana aittir.',sekil=SK)
# ---------- 04 · orta · doğrusal üç yük net kuvvet
qK,qL,qM=Fr(4)*MIK,Fr(2)*MIK,Fr(1)*MIK; rKL,rLM=Fr(3,10),Fr(1,5)
F_KL=K9*qK*qL/rKL**2; F_ML=K9*qM*qL/rLM**2; net=F_KL-F_ML
assert F_KL==Fr('0.8') and F_ML==Fr('0.45') and net==Fr('0.35')
assert K9*qK*qL/rKL==Fr('0.24') and K9*qM*qL/rLM==Fr('0.09') and Fr('0.24')-Fr('0.09')==Fr('0.15') and F_KL+F_ML==Fr('1.25')
SK=tk('\n'.join([yuk(0,0,1,'K ($+4\\,\\mu$C)'),yuk(4.5,0,1,'L ($+2\\,\\mu$C)'),yuk(7.5,0,1,'M ($+1\\,\\mu$C)'),olc(0,4.5,.9,'0,3 m'),olc(4.5,7.5,.9,'0,2 m')]))
q('0004',tipId='ea-coulomb',tip='Coulomb kuvveti ve bileşke kuvvet',z='orta',alt='Bileşke Elektriksel Kuvvet',kaz='Bir doğru üzerindeki noktasal yüklerin bir yüke uyguladığı kuvvetlerin bileşkesini hesaplar.',
 kart='K-AFEA-01 (doğrusal üç yük) · 4 µC, 2 µC, 1 µC',kalip='şekilli',
 metin='Yalıtkan yatay bir zeminde K, L ve M noktasal yükleri bir doğru üzerine şekildeki gibi sabitlenmiştir. Yük miktarları ve yükler arasındaki uzaklıklar şekilde verilmiştir.\n(k = 9·10⁹ N·m²/C²)\nBuna göre, L yüküne etki eden net elektriksel kuvvetin büyüklüğü kaç N’dur?',
 dogru=Fr('0.35'),yan=[(Fr('0.15'),'Coulomb bağıntısında uzaklığın karesi yerine uzaklığı kullanmış: 0,24 − 0,09 = 0,15 N.','islem'),
  (Fr('0.45'),'Yalnız M’nin kuvvetini (0,45 N) hesaplamış; K’nin etkisini katmamış.','dikkat'),
  (Fr('0.8'),'Yalnız K’nin kuvvetini (0,8 N) hesaplamış; M’nin etkisini katmamış.','dikkat'),
  (Fr('1.25'),'İki kuvvetin aynı yönde olduğunu varsayıp toplamış: 0,8 + 0,45 = 1,25 N.','bilgi')],
 istenen='L yüküne etki eden net kuvvetin büyüklüğü (N).',ip=['K ve M’nin L’ye uyguladığı kuvvetlerin yönlerini aynı yüklü olmanın sonucuna göre çiz, sonra ayrı ayrı hesapla.'],
 bilgi=[B('Aynı işaretli yükler','Aynı işaretli yükler birbirini iter. Bir yükün iki yanında aynı işaretli yükler varsa kuvvetler zıt yönlüdür ve büyüklükleri çıkarılır. Örnek: 5 N sağa, 2 N sola kuvvet bileşkesi 3 N sağadır')],
 ad=[A('K’nin kuvveti','K, L’yi M yönüne iter.','F = 9·10⁹ × 4·10⁻⁶ × 2·10⁻⁶ ÷ 0,3² = 0,8 N'),
     A('M’nin kuvveti','M, L’yi K yönüne iter.','F = 9·10⁹ × 1·10⁻⁶ × 2·10⁻⁶ ÷ 0,2² = 0,45 N'),
     A('Yönleri belirle','Kuvvetler zıt yönlüdür; büyük olan K’den gelir.','K → L yönü pozitif alınır'),
     A('Net kuvvet','Zıt yönlü kuvvetler çıkarılır.','0,8 − 0,45 = 0,35 N')],
 puf='Zıt yönlü kuvvetlerin bileşkesi büyüklüklerin farkıdır; yönleri çizmeden toplama yapma.',sekil=SK)
# ---------- 05 · orta · dik bileşke alan
rP=Fr(3); EX=K9*Fr(3)*MIK/rP**2; EY=K9*Fr(4)*MIK/rP**2; assert EX==3000 and EY==4000 and EX**2+EY**2==5000**2 and EX+EY==7000 and EY-EX==1000
SK=tk('\n'.join([nok(0,0,'P','below left'),yuk(0,3,1,'X ($+3\\,\\mu$C)','right'),yuk(3,0,-1,'Y ($-4\\,\\mu$C)','above'),olc(0,3,-.6,'3 m',False),'\\draw[<->,thin] (-.7,0) -- (-.7,3) node[midway,left,fill=white,inner sep=1pt] {3 m};','\\draw[gray!60,thin] (-.7,0) -- (-.1,0);','\\draw[gray!60,thin] (-.7,3) -- (-.32,3);']))
q('0005',tipId='ea-alan',tip='Noktasal yüklerin elektrik alanı',z='orta',alt='Bileşke Elektrik Alan',kaz='Birbirine dik doğrultudaki iki noktasal yükün bir noktada oluşturduğu alanların bileşkesini hesaplar.',
 kart='K-AFEA-02 (dik alanlar) · 3 µC, −4 µC, 3 m',kalip='şekilli',
 metin='Şekilde noktasal X ve Y yükleri, P noktasına 3 m uzaklıkta ve birbirine dik doğrultuda sabitlenmiştir. Yüklerin işaretleri ve miktarları şekilde verilmiştir.\n(k = 9·10⁹ N·m²/C²)\nBuna göre, P noktasındaki bileşke elektrik alanın büyüklüğü kaç N/C’dur?',
 dogru=5000,yan=[(1000,'İki alanı çıkarmış: 4000 − 3000 = 1000 N/C; alanların dik olduğunu görmemiş.','bilgi'),
  (4000,'Yalnız Y yükünün alanını (4000 N/C) almış; X’in etkisini katmamış.','dikkat'),
  (7000,'Alanların büyüklüklerini cebirsel toplamış: 3000 + 4000 = 7000 N/C.','bilgi'),
  (3000,'Yalnız X yükünün alanını (3000 N/C) almış; Y’nin etkisini katmamış.','dikkat')],
 istenen='P noktasındaki bileşke elektrik alanın büyüklüğü (N/C).',ip=['Her yükün P’deki alanını ayrı ayrı hesapla; alanların hangi doğrultularda olduğuna bak.'],
 bilgi=[B('Alan bileşkesi','Elektrik alan vektörel olduğundan birden çok yükün alanı vektörel toplanır; dik alanların bileşkesi Pisagor ile bulunur. Örnek: 6 N/C ve 8 N/C dik alanların bileşkesi 10 N/C’dur')],
 ad=[A('X’in alanı','E = kq/r² bağıntısı kullanılır; alan X’ten uzaklaşan yöndedir (düşey).','E_X = 9·10⁹ × 3·10⁻⁶ ÷ 3² = 3000 N/C'),
     A('Y’nin alanı','Y negatif olduğundan alan Y’ye doğrudur (yatay).','E_Y = 9·10⁹ × 4·10⁻⁶ ÷ 3² = 4000 N/C'),
     A('Doğrultuları gör','Alanlardan biri düşey, diğeri yataydır; birbirine diktir.','E_X ⟂ E_Y'),
     A('Bileşkeyi bul','Pisagor bağıntısı uygulanır.','E = √(3000² + 4000²) = 5000 N/C')],
 puf='Alanları büyüklük olarak toplamadan önce doğrultularını çiz; dik alanlarda Pisagor uygulanır.',sekil=SK)
# ---------- 06 · orta · öncüllü · alanın sıfır olduğu nokta
def Ex(pos,qs,x): return sum(Fr(qq)*(1 if x>p else -1)/Fr(x-p)**2 for p,qq in zip(pos,qs))   # birim kq/d² ; + = Y yönü
pos6=[0,6]; qs6=[4,1]
E_K,E_L,E_M=Ex(pos6,qs6,2),Ex(pos6,qs6,4),Ex(pos6,qs6,5)
assert E_K!=0 and E_L==0 and E_M<0 and E_K>0 and abs(E_M)>Fr(4,25)
s6=1.15
SK=tk('\n'.join([yuk(0,0,1,'X ($+4q$)','above'),yuk(6*s6,0,1,'Y ($+q$)','above')]+[nok(x*s6,0,n,'below') for x,n in [(2,'K'),(4,'L'),(5,'M')]]+['\\draw[gray] (.3,0) -- (%f,0);'%(6*s6-.3)]+[f'\\draw[gray] ({i*s6},-.12) -- ({i*s6},.12);' for i in range(7)]+[olc(0,s6,-1.1,'$d$',False)]))
onc('0006','Bir doğru üzerinde eşit aralıklı noktalara sabitlenen X (+4q) ve Y (+q) yükleri ile K, L, M noktaları şekilde gösterilmiştir. İki ardışık nokta arasındaki uzaklık d’dir.\nBuna göre,',
 [('K noktasındaki net elektrik alan sıfırdır.',False,'K noktasında X’in alanı baskındır; net alan sıfır değil, Y yönündedir'),
  ('L noktasındaki net elektrik alan sıfırdır.',True,'L noktasında X ve Y’nin alanları eşit büyüklükte ve zıt yöndedir, net alan sıfırdır'),
  ('M noktasındaki net elektrik alan X yönündedir.',True,'M noktasında Y’nin alanı baskındır ve net alan X yönündedir')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],son='yargılarından hangileri doğrudur?',
 tipId='ea-alan',tip='Noktasal yüklerin elektrik alanı',z='orta',alt='Alanın Sıfır Olduğu Nokta',kaz='İki aynı işaretli yükün bulunduğu doğruda net alanın sıfır olduğu noktayı ve alan yönlerini belirler.',
 kart='K-AFEA-02 (sıfır alan noktası) · +4q ve +q, 6d',istenen='Doğru olan yargıları belirlemek.',
 ip=['Her noktada iki yükün alanlarını ayrı ayrı yönleriyle çiz; kq/r² değerlerini kıyasla.'],
 bilgi=[B('Sıfır alan noktası','Aynı işaretli iki yükün arasında alanlar zıt yönlüdür; net alanın sıfır olduğu nokta küçük yüke daha yakındır. Örnek: yük oranı 9 ise nokta, uzaklıkların oranı 3 olan yerdedir')],
 puf='Net alan sıfır olacaksa iki alanın büyüklüğü eşit ve yönü zıt olmalıdır; büyük yükün alanı uzaklıkla sönmek zorundadır.',sekil=SK)
# ---------- 07 · orta · kare köşelerinde potansiyel
qq7=[3,-1,2,-2]; assert sum(qq7)==2 and sum(x for x in qq7 if x<0)==-3 and sum(x for x in qq7 if x>0)==5
SK=tk('\n'.join(['\\draw[gray,thick] (-1.6,-1.6) rectangle (1.6,1.6);','\\draw[gray,dashed] (-1.6,-1.6) -- (1.6,1.6) (-1.6,1.6) -- (1.6,-1.6);',
  yuk(-1.6,1.6,1,'$+3q$','above left'),yuk(1.6,1.6,-1,'$-q$','above right'),yuk(1.6,-1.6,1,'$+2q$','below right'),yuk(-1.6,-1.6,-1,'$-2q$','below left'),
  nok(0,0,'O','below'),'\\draw[black,thin,-{Stealth[length=1.6mm]}] (0,0) -- (1.0,1.0) node[midway,above left,inner sep=1pt] {$r$};']))
q7=Fr(2)*MIK; r7=Fr(9,5); vO=K9*q7*sum(qq7)/r7; W7=Fr(5)*MIK*vO
assert vO==20000 and W7==Fr(1,10) and Fr(5)*MIK*K9*q7*5/r7==Fr(1,4) and Fr(5)*MIK*K9*q7*(-3)/r7==Fr(-3,20)
q('0007',tipId='ea-potansiyel',tip='Elektriksel potansiyel ve potansiyel farkı',z='orta',alt='Potansiyelin Cebirsel Toplamı',kaz='Birden çok noktasal yükün merkezde oluşturduğu potansiyeli cebirsel toplayıp yük getirmek için gereken işi bulur.',
 kart='K-AFEA-03 (kare köşeleri) · +3q, −q, +2q, −2q, q = 2 µC',kalip='şekilli',
 metin='Şekildeki karenin köşelerine noktasal +3q, −q, +2q ve −2q yükleri sabitlenmiştir. Burada q = 2 µC’dur; karenin merkezi O noktasının her köşeye uzaklığı r = 1,8 m’dir. Potansiyel sonsuzda sıfırdır.\n(k = 9·10⁹ N·m²/C²)\nBuna göre, +5 µC’luk noktasal bir yük sonsuzdan O noktasına yavaşça getirilirken dış kuvvetin yaptığı iş kaç mJ’dür?',
 dogru=100,yan=[(0,'İki pozitif, iki negatif yük bulunduğundan O’daki potansiyeli sıfır sanmış; iş de sıfır çıkmış.','bilgi'),
  (250,'Yalnız pozitif yüklerin potansiyelini katmış: 5q → 50000 V; 5 µC × 50000 V = 250 mJ.','dikkat'),
  (-3*50,'Yalnız negatif yüklerin potansiyelini katmış: −3q → −30000 V; 5 µC × (−30000 V) = −150 mJ.','dikkat'),
  (-100,'Potansiyelin işaretini ters yazmış: 5 µC × (−20000 V) = −100 mJ.','islem')],
 istenen='Dış kuvvetin yaptığı iş (mJ).',ip=['Önce O noktasındaki toplam potansiyeli bul; sonra yükün sonsuzdan O’ya gelişindeki enerji değişimini düşün.'],
 bilgi=[B('Potansiyelde toplama','Potansiyel skalerdir; birden çok yükün potansiyeli işaretleriyle toplanır. Örnek: +2q ve −5q yüklerinin eşit uzaklıktaki potansiyeli −3kq/r’dir')],
 ad=[A('Uzaklıkları gör','Her köşe O’ya r kadar uzaktır.','r₁ = r₂ = r₃ = r₄ = 1,8 m'),
     A('Potansiyeli bul','Yükler işaretleriyle toplanır.','V = k(3 − 1 + 2 − 2)q ÷ r = 9·10⁹ × 2 × 2·10⁻⁶ ÷ 1,8 = 20000 V'),
     A('İşi yaz','Dış kuvvetin işi, yükün enerji değişimine eşittir (sonsuzda V = 0).','W = qV = 5·10⁻⁶ × 20000'),
     A('Sonucu yaz','Joule mJ’ye çevrilir.','W = 0,1 J = 100 mJ')],
 puf='Skaler niceliklerde yön değil, işaret hesaba katılır.',sekil=SK)
# ---------- 08 · orta · öncüllü · eş potansiyel eğrileri
Vk,Vl,Vm,Vn=60,20,40,40; q8=Fr(2)*MIK
W_KL=q8*(Vk-Vl); assert W_KL==Fr(80)*MIK and Vm==Vn
dU=(-q8)*(Vm-Vl); assert dU==-Fr(40)*MIK
import math
def ep(a,b,ang): return (a*cos(radians(ang)),b*sin(radians(ang)))
E1,E2,E3=(1.0,.7),(2.2,1.5),(3.4,2.3)
pk=ep(*E1,90); pl=ep(*E3,55); pm=ep(*E2,155); pn=ep(*E2,25)
SK=tk('\n'.join([f'\\draw[blue!60!black,thick,dashed] (0,0) ellipse ({a} and {b});' for a,b in (E1,E2,E3)]+
  [f'\\node[fill=white,inner sep=1pt,font=\\small] at ({ep(*E,270)[0]:.2f},{ep(*E,270)[1]:.2f}) {{{v} V}};' for E,v in ((E1,60),(E2,40),(E3,20))]+
  [nok(pk[0],pk[1],'K','above'),nok(pl[0],pl[1],'L','above right'),nok(pm[0],pm[1],'M','above left'),nok(pn[0],pn[1],'N','below right')]))
onc('0008','Kesikli çizgiler, bir elektrik alanın eş potansiyel eğrilerini göstermektedir. Her eğrinin alt ucuna o eğrinin potansiyeli yazılmıştır; K, L, M ve N noktaları eğriler üzerindedir.\nBuna göre,',
 [('+2 µC yük K noktasından L noktasına götürülürken elektriksel kuvvetin yaptığı iş 80 µJ’dür.',True,'elektriksel kuvvetin yaptığı iş q(V_K − V_L) = 2 µC × 40 V = 80 µJ’dür'),
  ('Bir yük M noktasından N noktasına götürülürken elektriksel kuvvetin yaptığı iş sıfırdır.',True,'M ve N aynı eş potansiyel eğrisi üzerindedir, bu yüzden iş sıfırdır'),
  ('−2 µC yük L noktasından M noktasına götürülürken potansiyel enerjisi 40 µJ artar.',False,'−2 µC yükün potansiyel enerjisi q·ΔV = (−2 µC)(+20 V) = −40 µJ değişir, yani 40 µJ azalır')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],son='yargılarından hangileri doğrudur?',
 tipId='ea-enerji',tip='Elektriksel potansiyel enerji ve iş',z='orta',alt='Eş Potansiyel Eğrileri ve İş',kaz='Eş potansiyel eğrilerinden potansiyel farkını okuyup elektriksel kuvvetin işini ve potansiyel enerji değişimini bulur.',
 kart='K-AFEA-04 (eş potansiyel eğrileri) · 60 V, 40 V, 20 V',istenen='Doğru olan yargıları belirlemek.',
 ip=['Her noktanın bulunduğu eğrinin potansiyelini oku; iş ve enerji için potansiyel farkının işaretine dikkat et.'],
 bilgi=[B('Elektriksel kuvvetin işi','Elektriksel kuvvetin yaptığı iş W = q(V_ilk − V_son)’dur; eş potansiyel yüzeyde iş sıfırdır, potansiyel enerji değişimi ΔU = −W’dir. Örnek: +1 µC yük 30 V’tan 10 V’a giderse iş 20 µJ’dür')],
 puf='İş ve potansiyel enerji için önce potansiyel farkını, sonra yükün işaretini düşün; yolun şekli önemli değildir.',sekil=SK)
# ---------- 09 · orta · öncüllü · düzgün alan
Eu=500; bol=Fr(1,10); pts={'K':(1,1),'L':(1,4),'M':(4,1),'N':(5,3)}
VKL=Eu*bol*(pts['L'][0]-pts['K'][0]); VKM=Eu*bol*(pts['M'][0]-pts['K'][0]); VKN=Eu*bol*(pts['N'][0]-pts['K'][0])
assert VKL==0 and VKM==150 and VKN==200 and Fr(2)*MIK*VKN==Fr(400)*MIK
f=['\\draw[gray!60,thin,dashed] (0,0) grid (6,5);','\\draw[black,thin] (0,0) rectangle (6,5);']
for y in (2,3.5): f.append(f'\\draw[{BLUE},thick,{ARR}] (0.15,{y}) -- (5.85,{y});')
f.append(f'\\node[{BLUE},fill=white,inner sep=1pt] at (3.2,2.35) {{$\\vec E$ = 500 N/C}};')
f+= [nok(x,y,n,'above right' if n!='L' else 'above right') for n,(x,y) in pts.items()]
f.append('\\node[gray!40!black,font=\\footnotesize] at (3,-.45) {her bölme 0,1 m};')
SK=tk('\n'.join(f))
onc('0009','Düzgün bir elektrik alanda, kenarları 0,1 m olan eşit bölmeli kareli zemin üzerindeki K, L, M ve N noktaları şekilde gösterilmiştir. Alan büyüklüğü 500 N/C olup yatay ve sağa doğrudur.\nBuna göre,',
 [('K noktasının potansiyeli L noktasının potansiyelinden büyüktür.',False,'K ve L alana dik bir doğru üzerindedir, potansiyelleri eşittir'),
  ('M noktasının potansiyeli K noktasının potansiyelinden 150 V büyüktür.',False,'alan yönünde ilerledikçe potansiyel azalır; M’nin potansiyeli K’ninkinden 150 V küçüktür'),
  ('+2 µC yük K noktasından N noktasına götürülürken elektriksel kuvvetin yaptığı iş 400 µJ’dür.',True,'alan doğrultusundaki uzaklık 0,4 m olduğundan potansiyel farkı 200 V ve iş 2 µC × 200 V = 400 µJ’dür')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],son='yargılarından hangileri doğrudur?',
 tipId='ea-duzgun',tip='Düzgün elektrik alan ve yüklü parçacığın hareketi',z='orta',alt='Düzgün Alanda Potansiyel Farkı',kaz='Düzgün alanda ΔV = E·d bağıntısıyla potansiyel farkını ve yapılan işi hesaplar.',
 kart='K-AFEA-05 (düzgün alanda ΔV = Ed) · 500 N/C, 0,1 m bölme',istenen='Doğru olan yargıları belirlemek.',
 ip=['Her iki nokta arasındaki uzaklığın yalnız alan doğrultusundaki bileşenini kullan; alan yönünde potansiyelin nasıl değiştiğini düşün.'],
 bilgi=[B('Düzgün alanda potansiyel','Düzgün alanda alan yönünde ilerledikçe potansiyel azalır; iki nokta arasındaki fark V = E·d’dir ve d alan doğrultusundaki uzaklıktır. Örnek: E = 100 N/C ve d = 0,5 m ise fark 50 V’tur')],
 puf='Alana dik doğrultuda potansiyel değişmez; yalnız alan doğrultusundaki uzaklık potansiyel farkını belirler.',sekil=SK)
# ---------- 10 · orta · enerji korunumu, levhalar
qp=Fr(1)*MIK; mp=Fr(2,10**6); dV=100; KE=qp*dV; v2=2*KE/mp
assert v2==100 and qp*dV/mp==50 and qp*dV/(2*mp)==25 and qp*dV/(4*mp)==Fr(25,2)
assert 5**2==25 and 10**2==100
SK=tk('\n'.join(['\\draw[very thick,red!75!black] (0,-1.5) -- (0,1.5);','\\draw[very thick,blue!70!black] (4.2,-1.5) -- (4.2,1.5);',
  '\\node[red!75!black,above] at (0,1.5) {K: 100 V};','\\node[blue!70!black,above] at (4.2,1.5) {L: 0};']+
  [f'\\draw[gray,{ARR}] (.9,{y}) -- (3.6,{y});' for y in (-.9,.9)]+['\\node[gray,font=\\small] at (2.25,.35) {$\\vec E$};',
  yuk(.7,-.2,1,'2 mg, $+1\\,\\mu$C','right')]))
q('0010',tipId='ea-duzgun',tip='Düzgün elektrik alan ve yüklü parçacığın hareketi',z='orta',alt='Yüklü Parçacığın Hızlanması',kaz='Potansiyel farkı altında hızlanan yüklü parçacığın hızını enerji korunumuyla bulur.',
 kart='K-AFEA-05 (levhalar arasında hızlanma) · 100 V, 1 µC, 2 mg',kalip='şekilli',
 metin='Yer çekiminin ihmal edildiği bir ortamda, paralel K ve L levhalarının potansiyelleri şekilde verilmiştir. Kütlesi ve yükü şekilde verilen parçacık K levhasının yüzeyinden ilk hızsız bırakılıyor ve L levhasına çarpıyor.\nBuna göre, parçacığın L levhasına çarptığı andaki hızı kaç m/s’dir?',
 dogru=10,yan=[(5,'Kinetik enerjiyi ½mv² yerine 2mv² yazmış: v² = qΔV ÷ 2m = 25, v = 5 m/s.','islem'),
  (25,'Kinetik enerjiyi 2mv² yazmış ve karekök almayı unutup v² değerini (25) hız sanmış.','dikkat'),
  (50,'Kinetik enerjiyi m·v olarak yazmış: v = qΔV ÷ m = 50 m/s.','bilgi'),
  (100,'Enerji denkleminden v² = 2qΔV ÷ m = 100 bulup karekök almayı unutmuş.','islem')],
 istenen='Parçacığın L levhasına çarpma hızı (m/s).',ip=['Parçacığın kazandığı kinetik enerjiyi, levhalar arasındaki potansiyel farkı ve yükle ilişkilendir.'],
 bilgi=[B('Enerji korunumu','Elektriksel kuvvetin yaptığı iş kinetik enerji değişimine eşittir: q·ΔV = ½mv². Örnek: 4 µC’luk bir yük 25 V’luk farkta 100 µJ kinetik enerji kazanır')],
 ad=[A('Birimleri SI’ya çevir','Yük ve kütle SI birimlerine çevrilir.','q = 1·10⁻⁶ C ; m = 2·10⁻⁶ kg'),
     A('Elektriksel işi yaz','Parçacık 100 V’tan 0 V’a gider.','W = qΔV = 1·10⁻⁶ × 100 = 1·10⁻⁴ J'),
     A('Enerji korunumunu kur','İş kinetik enerjiye dönüşür.','½ × 2·10⁻⁶ × v² = 1·10⁻⁴'),
     A('Hızı bul','v² çözülür.','v² = 100 → v = 10 m/s')],
 puf='Düzgün alanda mesafe verilmese de potansiyel farkı ve yükle kazanılan enerji bulunur.',sekil=SK)
# ---------- 11 · orta · V–r grafiği
kQ=3*60; assert kQ==180 and Fr(kQ,36)==5 and Fr(60,6)==10 and Fr(kQ,9)==20 and Fr(kQ,6)==30
gx=['\\begin{axis}[width=6.8cm,height=5.4cm,xmin=0,xmax=9,ymin=0,ymax=190,xtick={0,1,2,3,4,5,6,7,8,9},ytick={0,60,120,180},grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$r$ (m)},ylabel={$V$ (V)},xlabel style={font=\\small},ylabel style={font=\\small}]',
    '\\addplot[thick,vurgu,domain=1:9,samples=60,smooth]{180/x};','\\addplot[only marks,mark=*,mark size=2pt,black] coordinates {(3,60)};',
    '\\draw[dashed,black] (axis cs:3,0) -- (axis cs:3,60) -- (axis cs:0,60);','\\end{axis}']
SK=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(gx)+TAIL)
q('0011',tipId='ea-potansiyel',tip='Elektriksel potansiyel ve potansiyel farkı',z='orta',alt='Potansiyel–Uzaklık Grafiği',kaz='Noktasal yükün V–r grafiğinden kQ çarpımını bulup elektrik alan şiddetini hesaplar.',
 kart='K-AFEA-03 (V–r grafiği) · 3 m’de 60 V',kalip='grafik',
 metin='Sabit noktasal +Q yükünün oluşturduğu elektriksel potansiyelin, yükten olan r uzaklığına bağlı değişimi şekildeki grafikteki gibidir. Potansiyel sonsuzda sıfırdır.\nBuna göre, yükten 6 m uzaklıktaki bir noktada elektrik alanın büyüklüğü kaç N/C’dur?',
 dogru=5,yan=[(10,'Alanı E = V ÷ r diye düşünüp 3 m’deki potansiyeli (60 V) 6 m’ye bölmüş: 60 ÷ 6 = 10 N/C.','bilgi'),
  (20,'Alanı 3 m’deki noktada hesaplamış: 180 ÷ 3² = 20 N/C; uzaklığı 6 m almamış.','dikkat'),
  (30,'Alan yerine 6 m’deki potansiyeli (180 ÷ 6 = 30 V) yazmış.','bilgi'),
  (60,'Grafikteki işaretli noktanın potansiyelini (60 V) alan sanmış.','dikkat')],
 istenen='6 m uzaklıkta elektrik alan şiddeti (N/C).',ip=['Grafikteki işaretli noktadan kQ çarpımını bul; sonra alan bağıntısını yaz.'],
 bilgi=[B('V ve E ilişkisi','Noktasal yükte V = kQ/r ve E = kQ/r² olduğundan E = V/r’dir. Örnek: 5 m’de 40 V ise bu noktada alan 8 N/C’dur')],
 ad=[A('Noktayı oku','Grafikte r = 3 m için potansiyel okunur.','V = 60 V'),
     A('kQ’yu bul','V = kQ/r bağıntısından çarpım bulunur.','kQ = 60 × 3 = 180 V·m'),
     A('Alanı yaz','6 m’de E = kQ/r² hesaplanır.','E = 180 ÷ 6² = 5 N/C')],
 puf='V–r grafiğinde bir nokta kQ çarpımını verir; alan, aynı çarpımın uzaklığın karesine bölünmesidir.',sekil=SK)
# ---------- 12 · orta · öncüllü · potansiyel enerji, +Q çevresinde
rr=[1,2,3]
Uf=lambda sg,r: Fr(sg)/r   # U = k Q q_sign / r (birim kQq)
assert Uf(-1,rr[1])>Uf(-1,rr[0])
assert Fr(1)/rr[1]-Fr(1)/rr[2]>0
assert (Uf(1,3)-Uf(1,1))==-(Uf(-1,3)-Uf(-1,1))!=0
s12=1.5
SK=tk('\n'.join([yuk(0,0,1,'$+Q$','above')]+[nok(s12*x,0,n,'above') for x,n in [(1,'K'),(2,'L'),(3,'M')]]+[olc(0,s12,-.8,'$r$',False),olc(s12,2*s12,-.8,'$r$',False),olc(2*s12,3*s12,-.8,'$r$',False)]+['\\draw[gray] (.3,0) -- (%f,0);'%(3*s12+.3)]))
onc('0012','Sabit +Q yükünün bulunduğu doğru üzerindeki K, L ve M noktaları şekilde verilmiştir. Ardışık noktalar arasındaki uzaklık r’dir; yükler yalnız elektriksel kuvvetin etkisindedir.\nBuna göre,',
 [('−q yükü K noktasından L noktasına götürülürken sistemin potansiyel enerjisi azalır.',False,'−q yükü +Q’dan uzaklaşırken potansiyel enerjisi negatif değerden sıfıra yaklaşır, yani artar'),
  ('+q yükü L noktasından M noktasına götürülürken elektriksel kuvvetin yaptığı iş pozitiftir.',True,'+q yük +Q’nun itmesiyle uzaklaştığından elektriksel kuvvet yer değiştirme yönündedir ve iş pozitiftir'),
  ('+q yükünün K’dan M’ye götürülürken potansiyel enerjisindeki değişim, −q yükünün aynı yoldaki değişimiyle aynıdır.',False,'iki yükün potansiyel enerji değişimleri aynı büyüklükte fakat zıt işaretlidir')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],son='yargılarından hangileri doğrudur?',
 tipId='ea-enerji',tip='Elektriksel potansiyel enerji ve iş',z='orta',alt='Potansiyel Enerji Değişimi',kaz='Yük işaretine göre potansiyel enerji değişiminin ve elektriksel kuvvetin işinin işaretini belirler.',
 kart='K-AFEA-04 (potansiyel enerji işareti) · +Q, K, L, M',istenen='Doğru olan yargıları belirlemek.',
 ip=['Yükün işaretini ve yükten uzaklaşıp yaklaşmasını dikkate alarak kuvvetin yönünü ve U = kQq/r’nin işaretini düşün.'],
 bilgi=[B('Potansiyel enerji','İki noktasal yükün potansiyel enerjisi U = kq₁q₂/r’dir; aynı işaretli yüklerde pozitif, zıt işaretlilerde negatiftir. Örnek: yükler yaklaşırken itme varsa enerji artar')],
 puf='Elektriksel kuvvet yer değiştirme yönündeyse iş pozitiftir ve potansiyel enerji azalır; ters yönde ise artar.',sekil=SK)
# ---------- 13 · orta · öncüllü · iletken küreler
Rx,Ry=Fr(1),Fr(2); Qt=Fr(6)
qX=Qt*Rx/(Rx+Ry); qY=Qt*Ry/(Rx+Ry); assert qX==2 and qY==4 and qX/Rx==qY/Ry
assert qX/Rx**2==2*(qY/Ry**2) and qY!=2
SK=tk('\n'.join(['\\draw[thick,fill=red!10,draw=red!75!black] (0,0) circle (.8);','\\node[red!75!black] at (0,0) {$+6q$};','\\node[above] at (0,.95) {X ($r$)};',
  '\\draw[thick,fill=gray!10,draw=black] (4.6,0) circle (1.6);','\\node at (4.6,0) {nötr};','\\node[above] at (4.6,1.75) {Y ($2r$)};',
  '\\draw[thick] (.8,0) -- (3.0,0);','\\draw[thick] (1.2,0) -- (1.2,0);','\\node[font=\\footnotesize,below] at (1.9,-.1) {ince tel};']))
onc('0013','Yarıçapları r ve 2r olan iletken X ve Y küreleri birbirinden çok uzaktadır. Başlangıçta X küresi +6q yüklü, Y küresi nötrdür. Küreler ince bir iletken telle birbirine bağlanıyor ve yük akışı bittikten sonra bekleniyor. (Telin yükü ve kürelerin birbirini etkilemesi ihmal edilmektedir.)\nBuna göre,',
 [('Son durumda kürelerin potansiyelleri eşittir.',True,'iletken tel küreleri aynı iletken yapar ve potansiyelleri eşitler'),
  ('Son durumda X küresinde 4q yük kalır.',False,'yük yarıçapla orantılı paylaşılır; X’te 2q, Y’de 4q yük kalır'),
  ('Son durumda kürelerin yüzeylerindeki elektrik alan şiddetleri eşittir.',False,'yüzeydeki elektrik alan E = kq/R² ile bulunur; X’inki Y’ninkinin 2 katıdır, eşit değildir')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],son='yargılarından hangileri doğrudur?',
 tipId='ea-kavram',tip='Elektrik alan, potansiyel ve yük dağılımı kavramları',z='orta',alt='İletken Kürelerde Yük Paylaşımı',kaz='Telle bağlanan iletken kürelerde potansiyelin eşitlendiğini, yükün yarıçapla orantılı dağıldığını ve yüzeydeki elektrik alan şiddetlerini karşılaştırır.',
 kart='K-AFEA-06 (iletken küreler) · r, 2r, +6q',istenen='Doğru olan yargıları belirlemek.',
 ip=['Potansiyel eşitliğinden yüklerin yarıçapla ilişkisini kur; yüzeydeki elektrik alan için E = kq/R² bağıntısını kullan.'],
 bilgi=[B('İletken kürelerde paylaşım','Telle bağlanan iletken kürelerde potansiyel eşitlenir: kq₁/R₁ = kq₂/R₂; yük yarıçapla orantılı dağılır, toplam yük korunur. Örnek: yarıçapları 1 ve 3 olan kürelerde yükler 1:3 oranındadır')],
 puf='Bağlanan iletkenlerde eşitlenen nicelik yük değil potansiyeldir; alan şiddetini ise yarıçapın karesi belirler.',sekil=SK)
# ---------- 14 · orta · öncüllü · V–x grafiği
Vp=[(0,40),(2,20),(4,20),(6,50)]
E1=-Fr(Vp[1][1]-Vp[0][1],Vp[1][0]-Vp[0][0]); E2=-Fr(Vp[2][1]-Vp[1][1],2); E3=-Fr(Vp[3][1]-Vp[2][1],2)
assert E1==10 and E2==0 and E3==-15
W3=Fr(2)*MIK*(Vp[0][1]-Vp[3][1]); assert W3==-Fr(20)*MIK
gx=['\\begin{axis}[width=6.8cm,height=5.2cm,xmin=0,xmax=6,ymin=0,ymax=60,xtick={0,1,2,3,4,5,6},ytick={0,10,20,30,40,50,60},grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$x$ (m)},ylabel={$V$ (V)},xlabel style={font=\\small},ylabel style={font=\\small}]',
    '\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {(0,40) (2,20) (4,20) (6,50)};','\\end{axis}']
SK=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(gx)+TAIL)
onc('0014','Yalnız x doğrultusunda olan bir elektrik alanın bulunduğu bölgede, elektriksel potansiyelin x konumuna bağlı değişimi şekildeki grafikteki gibidir.\nBuna göre,',
 [('0–2 m aralığında elektrik alanın büyüklüğü 10 N/C olup +x yönündedir.',True,'0–2 m aralığında potansiyel 10 V/m eğimle azaldığından alan +x yönündedir ve büyüklüğü 10 N/C’dur'),
  ('2–4 m aralığında bir noktasal yüke elektriksel kuvvet etki etmez.',True,'2–4 m aralığında potansiyel sabittir, alan sıfırdır ve elektriksel kuvvet etki etmez'),
  ('+2 µC yük x = 0’dan x = 6 m’ye götürülürken elektriksel kuvvetin yaptığı iş −20 µJ’dür.',True,'elektriksel kuvvetin işi 2 µC × (40 − 50) V = −20 µJ’dür')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],son='yargılarından hangileri doğrudur?',
 tipId='ea-duzgun',tip='Düzgün elektrik alan ve yüklü parçacığın hareketi',z='orta',alt='Potansiyel–Konum Grafiği',kaz='V–x grafiğinin eğiminden alanı bulur, uç noktalardaki potansiyellerden işi hesaplar.',
 kart='K-AFEA-05 (V–x grafiği) · 40, 20, 20, 50 V',istenen='Doğru olan yargıları belirlemek.',
 ip=['Grafiğin eğimiyle elektrik alanı ilişkilendir; iş için yalnız uç noktalardaki potansiyellere bak.'],
 bilgi=[B('Alan ve eğim','Bir doğrultuda E = −ΔV/Δx’tir: V–x grafiğinin eğimi alanın büyüklüğünü verir ve alan, potansiyelin azaldığı yönü gösterir. Örnek: potansiyel 4 m’de 12 V azalıyorsa alan 3 N/C’dur')],
 puf='Grafikte eğim alanı, iki uç arasındaki fark ise işi verir; eğimin işaretini yöne çevirmeyi unutma.',sekil=SK)
# ---------- 15 · zor · üç yükten oluşan sistemin enerjisi
qa,qb,qc=Fr(4)*MIK,-Fr(2)*MIK,Fr(1)*MIK; rab,rm=Fr(3,10),Fr(3,20)
Uab=K9*qa*qb/rab; Uac=K9*qa*qc/rm; Ubc=K9*qb*qc/rm; Ut=Uab+Uac+Ubc
assert Uab==Fr('-0.24') and Uac==Fr('0.24') and Ubc==Fr('-0.12') and Ut==Fr('-0.12') and Uac+Ubc==Fr('0.12') and abs(Uab)+abs(Uac)+abs(Ubc)==Fr('0.6')
SK=tk('\n'.join([yuk(0,0,1,'A ($+4\\,\\mu$C)','below'),yuk(6,0,-1,'B ($-2\\,\\mu$C)','below'),yuk(3,0,1,'M ($+1\\,\\mu$C)','above',col=GRN),olc(0,6,-1.3,'0,3 m',False)]))
q('0015',tipId='ea-enerji',tip='Elektriksel potansiyel enerji ve iş',z='zor',alt='Yük Sisteminin Potansiyel Enerjisi',kaz='Üç yükten oluşan sistemin toplam elektriksel potansiyel enerjisini ikili enerjileri işaretleriyle toplayarak bulur.',
 kart='K-AFEA-04 (üç yüklü sistem) · +4 µC, −2 µC, +1 µC',kalip='şekilli',
 metin='Şekilde A ve B noktasal yükleri aralarındaki uzaklık 0,3 m olacak biçimde sabitlenmiştir. Sonsuzdan getirilen +1 µC’lik noktasal bir yük, AB doğrusunun orta noktası M’ye sabitleniyor.\n(k = 9·10⁹ N·m²/C²)\nBuna göre, üç yükten oluşan sistemin elektriksel potansiyel enerjisi kaç J’dür?',
 dogru=Fr('-0.12'),yan=[(Fr('-0.24'),'Yalnız A ve B ikilisinin enerjisini hesaplamış (−0,24 J); M’deki yükü katmamış.','dikkat'),
  (Fr('0.12'),'Üçüncü yükü sonsuzdan getirmek için yapılan işi (0,24 − 0,12 = 0,12 J) sistemin toplam enerjisi sanmış.','bilgi'),
  (Fr('0.24'),'Yalnız A ile M yüklerinin ikilisinin enerjisini (0,24 J) almış.','dikkat'),
  (Fr('0.6'),'Üç ikilinin enerjilerini işaretlerini atarak toplamış: 0,24 + 0,24 + 0,12 = 0,6 J.','bilgi')],
 istenen='Üç yüklü sistemin toplam elektriksel potansiyel enerjisi (J).',ip=['Sistemde kaç yük çifti olduğunu say; her çiftin enerjisini işaretiyle hesaplayıp topla.'],
 bilgi=[B('Sistemin enerjisi','Birden çok yükün sistem enerjisi, tüm yük çiftlerinin U = kq₁q₂/r değerlerinin işaretli toplamıdır. Örnek: iki yük için tek çift, üç yük için üç çift vardır')],
 ad=[A('Çiftleri say','Üç yükten üç çift oluşur: AB, AM, BM.','AB: 0,3 m · AM = BM = 0,15 m'),
     A('AB enerjisi','Zıt işaretli yükler negatif enerji verir.','U_AB = 9·10⁹ × 4·10⁻⁶ × (−2·10⁻⁶) ÷ 0,3 = −0,24 J'),
     A('AM enerjisi','Aynı işaretli yükler pozitif enerji verir.','U_AM = 9·10⁹ × 4·10⁻⁶ × 1·10⁻⁶ ÷ 0,15 = +0,24 J'),
     A('BM enerjisi','Zıt işaretli yükler negatif enerji verir.','U_BM = 9·10⁹ × (−2·10⁻⁶) × 1·10⁻⁶ ÷ 0,15 = −0,12 J'),
     A('Toplamı yaz','Üç enerji işaretleriyle toplanır.','U = −0,24 + 0,24 − 0,12 = −0,12 J')],
 puf='Sistemin enerjisi, getirilen yükün iş katkısını da içeren tüm çiftlerin işaretli toplamıdır.',sekil=SK)
# ---------- 16 · zor · serbest üç yükün dengesi
def kuv(i,pos,qs):
    return sum(Fr(qs[i])*Fr(qs[j])*(1 if pos[i]>pos[j] else -1)/Fr(pos[i]-pos[j])**2 for j in range(len(pos)) if j!=i)
posd=[0,2,3]; qd=[4,Fr(-4,9),1]; assert all(kuv(i,posd,qd)==0 for i in range(3))
for qy in (Fr(4,9),Fr(2,3)*-1,Fr(-9,4),Fr(-1,9)): assert any(kuv(i,posd,[4,qy,1])!=0 for i in range(3))
assert Fr(4)*Fr(1,9)/Fr(4)==Fr(1,9)
d6=1.4
SK=tk('\n'.join([yuk(0,0,1,'X ($+4q$)','above'),bil(2*d6,0,'Y'),yuk(3*d6,0,1,'Z ($+q$)','above'),'\\draw[gray] (.3,0) -- (%f,0);'%(2*d6-.3),'\\draw[gray] (%f,0) -- (%f,0);'%(2*d6+.3,3*d6-.3),
   olc(0,2*d6,-1.0,'$2d$',False),olc(2*d6,3*d6,-1.0,'$d$',False)]))
q('0016',tipId='ea-denge',tip='Yüklerin dengesi ve asılı yüklü cisim',z='zor',alt='Serbest Yüklerin Dengesi',kaz='Bir doğru üzerindeki üç serbest yükün dengesinden bilinmeyen yükün işaretini ve büyüklüğünü bulur.',
 kart='K-AFEA-07 (üç serbest yük) · +4q, Y, +q; 2d, d',kalip='şekilli',
 metin='Sürtünmesiz yalıtkan bir düzlemde bulunan noktasal X, Y ve Z yükleri bir doğru üzerinde, aralarındaki uzaklıklar şekilde verildiği gibi serbest bırakılıyor. X ve Z yüklerinin işaretleri ve miktarları şekilde verilmiştir. Yükler yalnız birbirinin etkisindedir ve üçü de dengede kalmıştır.\nBuna göre, Y yükü kaç q’dur?',
 dogru='−4q/9',sira=['−9q/4','−2q/3','−4q/9','−q/9','+4q/9'],
 yan=[('+4q/9','Y’nin işaretini pozitif almış; aynı işaretli yükler X ve Z’yi dengeleyemez, Y negatif olmak zorundadır.','dikkat'),
  ('−2q/3','Coulomb bağıntısında uzaklığın karesi yerine uzaklığı kullanmış: |q_Y| ÷ 2 = 1 ÷ 3 → 2q/3.','islem'),
  ('−9q/4','X’in dengesinde (2d)² ile (3d)² oranını ters kurmuş: |q_Y| = q·(3d)² ÷ (2d)² = 9q/4.','bilgi'),
  ('−q/9','X ile Y arasındaki uzaklıkla Y ile Z arasındaki uzaklığı karıştırmış.','dikkat')],
 istenen='Y yükünün işareti ve büyüklüğü (q cinsinden).',ip=['Üç yükten birinin dengesini yazarken diğer ikisinin ona uyguladığı kuvvetlerin yönlerini çiz.'],
 bilgi=[B('Serbest yüklerin dengesi','Dengedeki her yüke etkiyen bileşke kuvvet sıfırdır. Aynı işaretli iki yükün arasındaki yük, uçlardaki yükleri dengelemek için zıt işaretli olmalıdır. Örnek: uçlardaki yükler eşitse ortadaki yük orta noktadadır')],
 ad=[A('İşareti belirle','Y, X ve Z’nin ikisini de çekmeli; X ve Z’yi itişlerini dengeleyebilmek için Y negatif olmalıdır.','q_Y < 0'),
     A('X’in dengesi','X’i Y çeker (+ yön), Z iter (− yön).','k·4q·|q_Y| ÷ (2d)² = k·4q·q ÷ (3d)²'),
     A('Büyüklüğü bul','Eşitlik sadeleştirilir.','|q_Y| ÷ 4 = q ÷ 9 → |q_Y| = 4q/9'),
     A('Z’nin dengesini sına','Z’yi Y çeker, X iter.','k·q·(4q/9) ÷ d² = k·q·4q ÷ (3d)²'),
     A('Sonucu yaz','İşaret negatiftir.','q_Y = −4q/9')],
 puf='Serbest yüklerin dengesinde bir yükün dengesinden bilinmeyen çözülür, ikinci yükün dengesi sağlama olur.',sekil=SK)
# ---------- 17 · zor · V = 0 noktaları
def V17(x): return Fr(4)/abs(Fr(x))-Fr(1)/abs(Fr(x)-3)
xi=Fr(12,5); xd=Fr(4); assert V17(xi)==0 and V17(xd)==0 and xd-xi==Fr(8,5) and 3-xi==Fr(3,5) and xd-3==1
assert all(V17(x)!=0 for x in (Fr(1),Fr(2),Fr(5),Fr(-1)))
s17=1.5
SK=tk('\n'.join([yuk(0,0,1,'A ($+4q$)','above'),yuk(3*s17,0,-1,'B ($-q$)','above'),'\\draw[gray] (.3,0) -- (%f,0);'%(3*s17-.3),'\\draw[gray] (%f,0) -- (%f,0);'%(3*s17+.3,3*s17+2.2),
  olc(0,3*s17,-.9,'$3d$',False)]))
q('0017',tipId='ea-potansiyel',tip='Elektriksel potansiyel ve potansiyel farkı',z='zor',alt='Potansiyelin Sıfır Olduğu Noktalar',kaz='Zıt işaretli iki yükün bulunduğu doğruda potansiyelin sıfır olduğu noktaları ayrı bölgeler için bulur.',
 kart='K-AFEA-03 (V = 0 noktaları) · +4q, −q, 3d',kalip='şekilli',
 metin='Şekilde A ve B noktasal yükleri aralarındaki uzaklık 3d olacak biçimde sabitlenmiştir. Yüklerin bulunduğu doğru üzerinde, sonsuz hariç, potansiyelin sıfır olduğu iki nokta vardır.\nBuna göre, bu iki nokta arasındaki uzaklık kaç d’dir?',
 dogru=Fr(8,5),yan=[(Fr(3,5),'Yalnız B ile A–B arasındaki sıfır potansiyel noktası arasındaki uzaklığı vermiş: 3d − 2,4d = 0,6d.','dikkat'),
  (1,'B’nin dışındaki sıfır noktasının B’ye uzaklığını (4d − 3d = d) vermiş.','dikkat'),
  (Fr(12,5),'A ile A–B arasındaki sıfır potansiyel noktası arasındaki uzaklığı (2,4d) vermiş.','dikkat'),
  (4,'B’nin dışındaki sıfır noktasının A’ya uzaklığını (4d) vermiş.','dikkat')],
 istenen='Potansiyelin sıfır olduğu iki nokta arasındaki uzaklık (d).',ip=['Her bölgede iki yükün potansiyellerinin toplamını sıfıra eşitle; uzaklıkları mutlak değerle düşün.'],
 bilgi=[B('Sıfır potansiyel noktası','İşaretleri zıt iki yükün potansiyelleri toplamı sıfır olan noktalar, küçük yüke daha yakın bölgelerde bulunur. Örnek: +9q ve −q için iç noktada uzaklıkların oranı 9:1’dir')],
 ad=[A('Koşulu yaz','Potansiyellerin toplamı sıfır olmalıdır.','k·4q/x = k·q/|x − 3d|'),
     A('A–B arasında','Nokta A’dan x uzaklıktadır (0 < x < 3d).','4(3d − x) = x → x = 2,4d'),
     A('B’nin ötesinde','Nokta A’dan x uzaklıktadır (x > 3d).','4(x − 3d) = x → x = 4d'),
     A('Uzaklığı bul','İki noktanın A’ya uzaklıkları çıkarılır.','4d − 2,4d = 1,6d')],
 puf='Zıt işaretli yüklerde potansiyelin sıfır olduğu nokta küçük yükün hem iç hem dış tarafında bulunur; iki bölgeyi ayrı hesapla.',sekil=SK)
# ---------- 18 · zor · asılı yüklü cisim, ip kopması
m18=Fr(4,1000); g=10; a37=Fr(5,4)*g  # a = g/cos37
assert Fr(1,Fr(4,5))*g==Fr(25,2)
a=Fr(g)/Fr(4,5); v=a*Fr(2,5); KE18=m18*v*v/2; assert a==Fr(25,2) and v==5 and KE18==Fr('0.05')
assert (m18*(g*Fr(3,4)*Fr(2,5))**2/2)==Fr('0.018') and (m18*(g*Fr(2,5))**2/2)==Fr('0.032') and (m18*(g*Fr(7,4)*Fr(2,5))**2/2)==Fr('0.098') and m18*v*v==Fr('0.1')
pv=(0,4); L18=3.0; bx,by=L18*0.6,4-L18*0.8
f=['\\draw[thick] (-1.3,4) -- (3.4,4);']+[f'\\draw[gray,thin] ({x},4) -- ({x-.2},4.25);' for x in [-1.1+.4*i for i in range(12)]]
f+=['\\draw[dashed,gray] (0,4) -- (0,.9);',f'\\draw[thick] (0,4) -- ({bx},{by});']
f+=[f'\\draw[gray!70!black,{ARR}] (-1.3,{y}) -- (3.9,{y});' for y in (.6,2.2,3.4)]
f+=['\\node[gray!70!black,fill=white,inner sep=1pt] at (-.8,2.55) {$\\vec E$};','\\draw (0,3.2) arc[start angle=-90,end angle=-53,radius=.8];','\\node at (.35,2.95) {$37^\\circ$};']
f+=[yuk(bx,by,1,'$+q$','right')]
SK=tk('\n'.join(f))
q('0018',tipId='ea-denge',tip='Yüklerin dengesi ve asılı yüklü cisim',z='zor',alt='Alan İçinde Asılı Yüklü Cisim',kaz='Düzgün alanda dengedeki asılı yüklü cismin ip koptuktan sonraki hareketini bileşke kuvvetle çözer.',
 kart='K-AFEA-07 (ip kopması) · 4 g, 37°, 0,4 s',kalip='şekilli',
 metin='Düzgün yatay bir elektrik alanda, kütlesi 4 g olan yüklü bir cisim yalıtkan bir iple şekildeki gibi dengede tutuluyor; ip düşeyle 37° açı yapıyor. İp koptuktan 0,4 s sonra cismin kinetik enerjisi ölçülecektir. Cisim bu sürede alandan çıkmıyor ve yükü değişmiyor; hava direnci ihmal edilmektedir.\n(g = 10 m/s², sin37° = 0,6, cos37° = 0,8)\nBuna göre, ip koptuktan 0,4 s sonra cismin kinetik enerjisi kaç mJ’dür?',
 dogru=50,yan=[(18,'Cismi yalnız elektriksel kuvvetin ivmelendirdiğini sanmış: a = g·tan37° = 7,5 m/s², v = 3 m/s, E_k = 18 mJ.','bilgi'),
  (32,'Ağırlıktan başka kuvvet olmadığını sanmış: a = 10 m/s², v = 4 m/s, E_k = 32 mJ.','dikkat'),
  (98,'Ağırlık ve elektriksel kuvvetin büyüklüklerini toplamış: a = 10 + 7,5 = 17,5 m/s², v = 7 m/s, E_k = 98 mJ.','islem'),
  (100,'Kinetik enerjiyi ½ çarpanını unutarak m·v² = 100 mJ bulmuş.','islem')],
 istenen='İp koptuktan 0,4 s sonra cismin kinetik enerjisi (mJ).',ip=['İp koptuğunda cisme etki eden iki kuvvetin bileşkesini, koptuktan önceki dengeden yararlanarak bul.'],
 bilgi=[B('Dengeden hareket','Üç kuvvet dengedeyken biri kalkarsa kalan iki kuvvetin bileşkesi, kalkan kuvvetin büyüklüğünde ve zıt yöndedir. Örnek: 10 N’luk gerilme kalkarsa kalan kuvvetlerin bileşkesi 10 N olur')],
 ad=[A('Ağırlığı yaz','Kütle SI birimine çevrilir.','mg = 0,004 × 10 = 0,04 N'),
     A('Gerilmeyi bul','Düşey dengede T·cos37° = mg.','T = 0,04 ÷ 0,8 = 0,05 N'),
     A('İvmeyi bul','İp koptuğunda bileşke kuvvet T’ye eşittir ve sabittir.','a = 0,05 ÷ 0,004 = 12,5 m/s²'),
     A('Hızı bul','Cisim durgun başladığı için v = a·t.','v = 12,5 × 0,4 = 5 m/s'),
     A('Kinetik enerjiyi yaz','E_k = ½mv² hesaplanır.','E_k = ½ × 0,004 × 5² = 0,05 J = 50 mJ')],
 puf='Dengedeki cismin bir kuvveti kalkınca, kalan kuvvetlerin bileşkesi kalkan kuvvetin tersine eşittir.',sekil=SK)
# ---------- 19 · zor · alana dik giren parçacık
q19=Fr(2)*MIK; m19=Fr(1,10**6); E19=500; v0=15; L19=Fr(3,10)
a19=q19*E19/m19; t19=L19/v0; vy=a19*t19; vf2=v0**2+vy**2; y19=a19*t19**2/2
assert a19==1000 and t19==Fr(1,50) and vy==20 and vf2==625 and y19==Fr(1,5) and y19<Fr(3,10)
assert v0+vy==35 and vy-v0==5
f=['\\draw[very thick,red!75!black] (0,4.5) -- (4.5,4.5);','\\draw[very thick,blue!70!black] (0,-4.5) -- (4.5,-4.5);']
f+=['\\node[red!75!black,font=\\large] at (%f,4.85) {$+$};'%x for x in (.5,1.5,2.5,3.5)]+['\\node[blue!70!black,font=\\large] at (%f,-4.85) {$-$};'%x for x in (.5,1.5,2.5,3.5)]
f+=[f'\\draw[gray,{ARR}] ({x},3.9) -- ({x},2.6);' for x in (1.0,3.5)]+['\\node[gray] at (2.25,3.2) {$\\vec E$};']
f+=['\\draw[thick,black,dashed] (-1.2,0) -- (0,0) -- plot[domain=0:4.5,samples=20] (\\x,{-3*(\\x/4.5)^2});']
f+=[f'\\draw[black,thick,{ARR}] (-2.2,0) -- (-1.2,0);','\\node[above] at (-1.3,.3) {$v_0$ = 15 m/s};',yuk(-2.7,0,1,'','below'),olc(0,4.5,-5.6,'0,3 m',False),'\\draw[<->,thin] (5.1,-4.5) -- (5.1,4.5) node[midway,right,fill=white,inner sep=1pt] {0,6 m};']
SK=tk('\n'.join(f))
q('0019',tipId='ea-duzgun',tip='Düzgün elektrik alan ve yüklü parçacığın hareketi',z='zor',alt='Alana Dik Giren Yüklü Parçacık',kaz='Düzgün alana dik giren yüklü parçacığın hareketini iki doğrultuda inceleyip çıkış hızını bulur.',
 kart='K-AFEA-05 (alana dik giriş) · 2 µC, 1 mg, 500 N/C',kalip='şekilli',
 metin='Yer çekiminin ihmal edildiği bir ortamda, paralel levhalar arasındaki düzgün elektrik alanın büyüklüğü 500 N/C’dur. Yükü +2 µC, kütlesi 1 mg olan parçacık, levhalara paralel ve şekildeki hızla alana giriyor; levhalara çarpmadan çıkıyor. Parçacık, 0,6 m aralıklı levhaların orta çizgisinden girmektedir; levha uzunluğu şekilde verilmiştir.\nBuna göre, parçacığın levhalardan çıkarken hızının büyüklüğü kaç m/s’dir?',
 dogru=25,yan=[(5,'Hız bileşenlerini çıkarmış: 20 − 15 = 5 m/s.','bilgi'),
  (15,'Alanın parçacığın hızını değiştirmediğini düşünüp giriş hızını vermiş.','bilgi'),
  (20,'Yalnız alan doğrultusundaki hız bileşenini (a·t = 20 m/s) vermiş.','dikkat'),
  (35,'Hız bileşenlerini cebirsel toplamış: 15 + 20 = 35 m/s.','bilgi')],
 istenen='Parçacığın levhalardan çıkış hızının büyüklüğü (m/s).',ip=['Hareketi alana dik ve alana paralel iki doğrultuda ayrı incele; alana dik doğrultuda hız değişmez.'],
 bilgi=[B('Alana dik giriş','Alana dik giren yüklü parçacıkta alan doğrultusunda sabit ivme, alana dik doğrultuda sabit hız vardır; iki bileşen dik olduğundan Pisagorla birleştirilir. Örnek: bileşenler 6 ve 8 m/s ise hız 10 m/s’dir')],
 ad=[A('İvmeyi bul','Elektriksel kuvvet tek kuvvettir (a = qE ÷ m).','a = 2·10⁻⁶ × 500 ÷ 10⁻⁶ = 1000 m/s²'),
     A('Geçiş süresi','Alana dik doğrultudaki hız sabittir.','t = 0,3 ÷ 15 = 0,02 s'),
     A('Alan yönündeki hız','İlk hız bu doğrultuda sıfırdır.','v_y = 1000 × 0,02 = 20 m/s'),
     A('Hızı birleştir','Bileşenler birbirine diktir.','v = √(15² + 20²) = 25 m/s')],
 puf='Yer çekimi yokken yatay atış gibi çalış: alan doğrultusunda ivmeli, diğerinde sabit hızlı hareket vardır.',sekil=SK)
# ---------- 20 · zor · itişen iki yüklü cisim
qq=Fr(4)*MIK; r20=Fr(3,10); U20=K9*qq*qq/r20; m1,m2=Fr(1),Fr(2)
# momentum: m1 v1 = m2 v2 ; E1 = U m2/(m1+m2)
E1=U20*m2/(m1+m2); E2=U20*m1/(m1+m2)
assert U20==Fr('0.48') and E1==Fr('0.32') and E2==Fr('0.16') and U20/2==Fr('0.24') and K9*qq*qq/r20**2==Fr('1.6')
v1=Fr(4,5); v2=Fr(2,5); assert m1*v1**2/2==E1 and m2*v2**2/2==E2 and m1*v1==m2*v2
SK=tk('\n'.join(['\\draw[thick] (-.8,-.65) -- (6.7,-.65);',yuk(0,0,1,'$m_1$ = 1 kg, $+4\\,\\mu$C','above'),yuk(5.9,0,1,'$m_2$ = 2 kg, $+4\\,\\mu$C','above'),olc(0,5.9,-1.3,'0,3 m',False)]).replace('(0,0)','(0,0)'))
q('0020',tipId='ea-enerji',tip='Elektriksel potansiyel enerji ve iş',z='zor',alt='Potansiyel Enerjiden Kinetik Enerjiye',kaz='İki yüklü cismin itişmesinde potansiyel enerjinin momentum korunumuyla kinetik enerjilere paylaşımını hesaplar.',
 kart='K-AFEA-04 (itişen yükler, momentum) · 1 kg, 2 kg, 4 µC',kalip='şekilli',
 metin='Sürtünmesiz yatay bir düzlemde, şekildeki yüklü m₁ ve m₂ cisimleri aralarındaki uzaklık 0,3 m iken serbest bırakılıyor. Cisimler yalnız birbirinin elektriksel kuvvetinin etkisinde birbirinden uzaklaşıyor ve çok uzaklaştıklarında elektriksel etkileşim ihmal ediliyor.\n(k = 9·10⁹ N·m²/C²)\nBuna göre, cisimler çok uzaklaştığında m₁ kütleli cismin kinetik enerjisi kaç J’dür?',
 dogru=Fr('0.32'),yan=[(Fr('0.16'),'Enerjinin büyük payının hafif cisme gideceğini görmeyip ağır cismin payını (0,16 J) vermiş.','dikkat'),
  (Fr('0.24'),'Toplam enerjiyi cisimler arasında eşit paylaştırmış: 0,48 ÷ 2 = 0,24 J.','bilgi'),
  (Fr('0.48'),'Sistemin toplam potansiyel enerjisini (0,48 J) m₁’in kinetik enerjisi sanmış.','bilgi'),
  (Fr('1.6'),'Enerji yerine kuvveti k·q₁q₂ ÷ r² = 1,6 değeriyle hesaplayıp enerji sanmış.','islem')],
 istenen='m₁ kütleli cismin kinetik enerjisi (J).',ip=['Başlangıçtaki toplam enerjiyi bul; momentum korunumundan kinetik enerjilerin kütlelerle nasıl bölüşüldüğünü çıkar.'],
 bilgi=[B('Enerji ve momentum','Sistemin potansiyel enerjisi kinetik enerjiye dönüşür; dış kuvvet yoksa toplam momentum sıfır kalır ve kinetik enerjiler kütlelerle ters orantılı bölüşülür. Örnek: kütle oranı 1:3 ise enerji oranı 3:1’dir')],
 ad=[A('Başlangıç enerjisini bul','İki yükün potansiyel enerjisi U = kq₁q₂/r ile hesaplanır.','U = 9·10⁹ × 4·10⁻⁶ × 4·10⁻⁶ ÷ 0,3 = 0,48 J'),
     A('Momentumu yaz','Toplam momentum sıfır kalır.','m₁v₁ = m₂v₂ → v₁ = 2v₂'),
     A('Enerji oranını bul','Kinetik enerji ½mv² ile hesaplanır.','E₁ ÷ E₂ = (1 × 4) ÷ (2 × 1) = 2'),
     A('Enerjileri paylaştır','Toplam enerji E₁ + E₂ = 0,48 J’dür.','E₁ = 0,48 × 2/3 = 0,32 J')],
 puf='İtişen iki cismin kinetik enerjileri kütlelerle ters orantılıdır; hafif cisim enerjinin büyük payını alır.',sekil=SK)

# ---- ipucu/püf/bilgi yumuşatma (anahtar fikri söylemesin)
OVR={
'0001':dict(puf='Önce iki değişimi ayrı ayrı bağıntıya yerleştir, sonra birleştir.'),
'0002':dict(puf='Her öncülde geçen niceliğin tanımına ve bağıntısına geri dön.',bilgi=[B('Alan ve potansiyel','Elektrik alan, birim pozitif yüke etkiyen kuvvet (E = F/q); potansiyel ise birim yükün elektriksel potansiyel enerjisidir (V = U/q). Örnek: 2 C’luk yüke 6 N’luk kuvvet etki ediyorsa alan 3 N/C’dur')]),
'0003':dict(puf='Noktasal yükte potansiyelin uzaklığa nasıl bağlandığını bağıntıdan hatırla.'),
'0004':dict(puf='Hesaptan önce her kuvvetin yönünü yük işaretlerine göre belirle.',bilgi=[B('Kuvvetin yönü','Aynı işaretli yükler birbirini iter, zıt işaretli yükler çeker; kuvvetin yönü bu kurala göre çizilir. Örnek: iki pozitif yükten soldaki, sağdakini sağa iter')]),
'0005':dict(puf='Alanların doğrultularını çizdikten sonra uygun toplama yöntemini seç.',bilgi=[B('Noktasal yükün alanı','E = kq/r² alanın büyüklüğünü verir; alan pozitif yükten uzağa, negatif yüke doğrudur ve vektörel toplanır. Örnek: 4 µC’luk yükün 2 m uzağındaki alan 9000 N/C’dur')]),
'0006':dict(puf='Her noktada iki alanı ayrı ayrı çizip büyüklüklerini kq/r² ile kıyasla.',bilgi=[B('Net alan','Bir noktadaki net alan, vektörel toplamdır; zıt yönlü alanlarda büyüklüğü fazla olan alan yönündedir. Örnek: 5 N/C sağa ve 3 N/C sola alanların bileşkesi 2 N/C sağadır')]),
'0007':dict(puf='Skaler niceliklerde yön değil, işaret hesaba katılır.'),
'0009':dict(puf='Alan doğrultusunu ve yönünü işaretleyip noktaların konumlarını bu doğrultuda karşılaştır.',bilgi=[B('Düzgün alanda potansiyel farkı','İki nokta arasındaki potansiyel farkı ΔV = E·d ile bulunur; d noktaların alan doğrultusundaki uzaklığıdır. Örnek: E = 100 N/C, d = 0,5 m ise ΔV = 50 V’tur')]),
'0010':dict(puf='Kuvvetin ya da mesafenin bilinmediği durumlarda iş ve enerji kavramlarını düşün.'),
'0011':dict(puf='Grafikteki işaretli noktadan hangi sabit niceliğin bulunabileceğini düşün.'),
'0012':dict(puf='Önce yükün işaretine göre kuvvetin yönünü çiz, sonra yer değiştirmeyle karşılaştır.'),
'0013':dict(puf='İletkenler birbirine bağlandığında hangi niceliklerin eşitleneceğini önce belirle.',bilgi=[B('İletken kürede nicelikler','İletken kürede yük yüzeyde toplanır; yüzeydeki potansiyel V = kq/R, yüzey yakınındaki alan E = kq/R²’dir. Örnek: yarıçap 2 katına çıkarsa aynı yükte alan 4 kat azalır')]),
'0014':dict(puf='Grafikteki eğimin ve uç değerlerin hangi fiziksel niceliklerle ilişkili olduğunu düşün.'),
'0015':dict(ip=['Üç yükün birbirine göre konumlarından, sistemin enerjisine katkı yapan nicelikleri belirle.'],puf='Potansiyel enerjinin işareti yüklerin işaretine bağlıdır; hesapta işaretleri taşı.',bilgi=[B('Yük çiftinin enerjisi','İki noktasal yükün potansiyel enerjisi U = kq₁q₂/r’dir; aynı işaretli yüklerde pozitif, zıt işaretli yüklerde negatiftir. Örnek: 2 µC ve 3 µC’lik yükler 0,9 m arayla ise U = 0,06 J’dür')]),
'0016':dict(puf='Her yük için net kuvvetin sıfır olduğunu ayrı ayrı düşün.',bilgi=[B('Dengede kuvvet','Dengedeki her yüke etkiyen bileşke kuvvet sıfırdır; bu koşul her yük için ayrı yazılabilir. Örnek: bir yükün iki yanındaki yükler ona eşit büyüklükte, zıt yönlü kuvvet uygular')]),
'0017':dict(puf='Toplam potansiyel ifadesini önce yaz, sonra sıfıra eşitle.',bilgi=[B('Toplam potansiyel','Birden çok yükün toplam potansiyeli cebirsel toplamdır: V = kq₁/r₁ + kq₂/r₂. Örnek: +2q ve −q yükleri 1 m ve 2 m uzaktaki noktada kq(2 − 0,5) = 1,5 kq potansiyel oluşturur')]),
'0018':dict(puf='İp koptuğunda hangi kuvvetlerin kaldığını ve hangisinin kalktığını yazmak, hareket sorularının ilk adımıdır.',bilgi=[B('Sabit kuvvetle hareket','Sabit bileşke kuvvet etkisinde ilk hızsız cisim doğru boyunca düzgün ivmeli gider: v = a·t ve E_k = ½mv². Örnek: a = 3 m/s² ve t = 2 s ise v = 6 m/s’dir')]),
'0019':dict(puf='Hızı bileşenlerine ayırıp her doğrultudaki kuvveti ayrı incele.'),
'0020':dict(ip=['Sistemde korunan niceliklerin hangileri olduğunu ve başlangıç enerjisinin ne olduğunu düşün.'],puf='Hem enerji hem momentum korunumunu yazmak, iki bilinmeyenli problemi çözülebilir yapar.',bilgi=[B('Korunum yasaları','Dış kuvvet yokken sistemin toplam momentumu korunur ve elektriksel potansiyel enerji kinetik enerjiye dönüşür. Örnek: 2 J’lük enerjili sistem tam dönüşümle 2 J kinetik enerji verir')]),
}
for qq_ in P.ANA:
    o=OVR.get(qq_['id'][-4:])
    if o:
        if 'puf' in o: qq_['puf']=o['puf']
        if 'bilgi' in o: qq_['bilgi']=o['bilgi']
        if 'ip' in o: qq_['ipuclari']=o['ip']
# ================= YAZ =================
for qq_ in P.ANA: qq_['kardes']=None
P.yaz(os.path.join(GD,'elalan-1.json'),'/tmp/bos-elalan.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Elektrik Alan ve Potansiyel'))['kartlar'].append(c['id'])
json.dump(dict(konu='Elektrik Alan ve Potansiyel',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Fizik 2018–2025 (yalnız mantık), 345 AYT Fizik Soru Bankası, MEB 11. sınıf fizik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afelalan.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
