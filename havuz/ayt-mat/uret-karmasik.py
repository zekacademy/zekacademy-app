"""AYT Matematik · Karmaşık Sayılar (20 soru: 4 kolay / 10 orta / 6 zor). Şekiller karmaşık düzlem (Argand) çizimleri.
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
P=Parti('karmasik','Karmaşık Sayılar',UK,ders='AYT Matematik',idon='aytmat')
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
def arg(x0,x1,y0,y1,ust='',govde='',sc=SC,fs='\\footnotesize'):
    o=[ust]
    for i in range(x0,x1+1): o.append(f'\\draw[gray!35,thin] ({i*sc:.3f},{y0*sc:.3f}) -- ({i*sc:.3f},{y1*sc:.3f});')
    for j in range(y0,y1+1): o.append(f'\\draw[gray!35,thin] ({x0*sc:.3f},{j*sc:.3f}) -- ({x1*sc:.3f},{j*sc:.3f});')
    o.append(govde)
    o.append(f'\\draw[-{{Stealth}},thick] ({(x0-0.4)*sc:.3f},0) -- ({(x1+0.7)*sc:.3f},0) node[right] {{Re}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,{(y0-0.4)*sc:.3f}) -- (0,{(y1+0.7)*sc:.3f}) node[above] {{Im}};')
    for i in range(x0,x1+1):
        if i!=0: o.append(f'\\node[below=2pt,font={fs},inner sep=0.8pt] at ({i*sc:.3f},0) {{${i}$}};')
    for j in range(y0,y1+1):
        if j!=0: o.append(f'\\node[left=2pt,font={fs},inner sep=0.8pt] at (0,{j*sc:.3f}) {{${j}$}};')
    o.append(f'\\node[below right=-1pt,font={fs}] at (0,0) {{$O$}};')
    return '\n'.join(o)
def nok(x,y,lab,col,pos='above right',sc=SC,rad=0.09,kil=False):
    s=f'\\fill[{col}] ({x*sc:.3f},{y*sc:.3f}) circle ({rad});'
    if lab: s+=f'\\node[{pos},{col},font=\\small\\bfseries] at ({x*sc:.3f},{y*sc:.3f}) {{${lab}$}};'
    if kil: s=f'\\draw[dashed,{col}!70] ({x*sc:.3f},0) -- ({x*sc:.3f},{y*sc:.3f}) -- (0,{y*sc:.3f});'+s
    return s
BL='blue!75!black'; OR='orange!90!black'; GR='green!45!black'; PU='violet!85!black'

# ---------- bilgi kutuları (yalnız tanım/kural; örnekler sorulardan bağımsız) ----------
IKB=B('i’nin kuvvetleri','i² = −1 olduğundan i⁴ = 1’dir ve kuvvetler i, −1, −i, 1 diye döngü yapar; iⁿ için n’nin 4’e bölümünden kalana bakılır. Örnek: i⁹ = i¹ = i, i¹⁴ = i² = −1')
ESL=B('Eşlenik','z = a + bi için z̄ = a − bi’dir; z · z̄ = a² + b² gerçel bir sayıdır. Bölmede pay ve payda paydanın eşleniğiyle genişletilir. Örnek: 1/(2 + i) = (2 − i)/((2 + i)(2 − i)) = (2 − i)/5')
CRP=B('Çarpma','(a + bi)(c + di) = (ac − bd) + (ad + bc)i’dir; çünkü i² = −1’dir. Örnek: (1 + 2i)(3 + i) = 3 + i + 6i + 2i² = 1 + 7i')
DUZ=B('Karmaşık düzlem','a + bi sayısı düzlemde (a, b) noktasıyla gösterilir: yatay eksen gerçel kısım (Re), düşey eksen sanal kısım (Im) içindir. Örnek: (−1, 3) noktası −1 + 3i sayısıdır; eşleniği (−1, −3) noktasıdır')
MOD=B('Modül','|a + bi| = √(a² + b²) sayının orijine uzaklığıdır; |z₁ − z₂| iki nokta arasındaki uzaklıktır. |z|² = z · z̄ ve |z̄| = |z| doğrudur. Örnek: |6 + 8i| = 10')
YER=B('Geometrik yer','|z − z₀| = r denklemi z₀ merkezli r yarıçaplı çemberi, |z − z₀| ≤ r içi ve çemberi, |z − z₁| = |z − z₂| denklemi z₁ ve z₂’ye eşit uzaklıktaki noktaları (orta dikmeyi) verir. Örnek: |z − 4i| = 2, 4i merkezli 2 yarıçaplı çemberdir')
IKI=B('Gerçel katsayılı denklem','ax² + bx + c = 0 denkleminde Δ < 0 ise kökler birbirinin eşleniği olan iki karmaşık sayıdır; kökler toplamı −b/a, çarpımı c/a’dır. Örnek: x² + 2x + 10 = 0 için Δ = −36, kökler −1 ± 3i’dir')
DON=B('i ile çarpma','z sayısını i ile çarpmak noktasını orijin etrafında saat yönünün tersine 90° döndürür: i(a + bi) = −b + ai. Bir noktayı başka bir merkez etrafında döndürmek için önce merkezden olan fark i ile çarpılır, sonra merkez eklenir. Örnek: i(5 + 2i) = −2 + 5i')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-AKS-01','i’nin kuvvetleri ve üslü ifade','Kuvvetin 4’e bölümünden kalan ya da özel bir özdeşlik (z³ = −1 gibi) bulunup üssün periyodu belirlenir; sonuç bu döngüden okunur.','Kalanı yanlış almak; i² = 1 sanmak; (−1) üssünün işaretini karıştırmak.','orta','düz',3,'kk-kuvvet','i’nin kuvvetleri ve üslü ifade')
kartla('K-AKS-02','Dört işlem, eşlenik ve tablo','Verilen gerçel ve sanal kısımlarla çarpma ve bölme i² = −1 ile yapılır; bölmede eşlenikle genişletilir; istenen kısım en sonda okunur.','Çarpmada i² = 1 almak; çapraz terimin işaretini karıştırmak; eşleniği ya da paydayı atlamak.','orta','tablo',4,'kk-islem','Dört işlem, eşlenik ve tablo')
kartla('K-AKS-03','Karmaşık düzlemde nokta ve vektör','Noktaların koordinatları sayıya çevrilir; paralelkenar, simetri ve toplama vektör toplama gibi yorumlanır; eşlenik eksene göre yansımadır.','Gerçel ve sanal eksenleri karıştırmak; köşe sırasını yanlış yorumlamak; −z ile z̄’yi karıştırmak.','orta','şekilli',3,'kk-duzlem','Karmaşık düzlemde nokta ve vektör')
kartla('K-AKS-04','Modül ve uzaklık','Modül orijine ya da iki nokta arasındaki uzaklıktır; |z|² = z · z̄ ve modülün çarpımsallığı kullanılır; kısımlar sayı çiftlerinden bulunur.','Karekök almayı unutmak; |z|² ile |z|’yu karıştırmak; uzaklığı koordinat farklarının toplamı sanmak.','orta','şekilli',4,'kk-modul','Modül ve uzaklık')
kartla('K-AKS-05','Karmaşık sayı denklemi ve tanımlı işlem','z = a + bi yazılır, denklem gerçel ve sanal kısımlar ayrı eşitlenir; tanımlı işlem kuralına göre adım adım uygulanır.','Eşleniği almadan çözmek; tanımlı işlemde sırayı değiştirmek; sanal kısmı i ile birlikte yazmak.','zor','yeni nesil',4,'kk-denklem','Karmaşık sayı denklemi ve tanımlı işlem')
kartla('K-AKS-06','İkinci derece denklemin karmaşık kökleri','Δ < 0 ise kökler eşleniktir; kökler toplamı ve çarpımı katsayılardan, gerçel katsayılı polinomda bir kök verilmişse eşleniği de kök olarak kullanılır.','Eşlenik kökü unutmak; kökler toplamı ve çarpımının işaretini karıştırmak; |z|’yu |z|² ile karıştırmak.','zor','öncüllü',4,'kk-ikinci','İkinci derece denklemin karmaşık kökleri')
kartla('K-AKS-07','Geometrik yer ve bölge','Eşitsizlik ya da şekil, merkez ve yarıçap (ya da eşit uzaklık) diliyle karşılıklı çevrilir; en kısa ve en uzun uzaklık merkezden uzaklığa ± yarıçapla bulunur; alan ilgili çember dilimlerinden hesaplanır.','Merkezin işaretini ters okumak; yarıçap yerine karesini yazmak; eşitsizlik yönünü ve sınırı karıştırmak.','zor','şekilli',4,'kk-yer','Geometrik yer ve bölge')
kartla('K-AKS-08','Döndürme ile köşe bulma','Merkezden köşeye giden vektör i ile çarpılarak 90° döndürülür; sonuç merkeze eklenir; yön saat yönünün tersi ise i, tersi ise −i ile çarpılır.','Merkez yerine orijin etrafında döndürmek; yönü ters almak; merkezi eklemeyi unutmak.','zor','şekilli',4,'kk-donme','Döndürme ile köşe bulma')

# ================= 01 kolay · düz · i kuvvetleri =================
z=2*ipw(47)-3*ipw(82)+ipw(105); assert eq(z,3,-1); v=3-(-1)
z_a=2*(1j)-3*ipw(82)+ipw(105)
z_b=2*ipw(47)-3*(1)+ipw(105)
z_c=2*ipw(47)-3*ipw(82)+(-1j)
e=[round(t.real-t.imag) for t in (z_a,z_b,z_c)]+[round(z.real+z.imag)]
assert e==[0,-2,6,2] and len({v,*e})==5
q('0001',tipId='kk-kuvvet',tip='i’nin kuvvetleri ve üslü ifade',z='kolay',alt='i’nin Kuvvetleri',kaz='i’nin kuvvetlerini 4’e bölümünden kalanla sadeleştirir; bir karmaşık sayının gerçel ve sanal kısımlarını belirler.',kalip='düz',
 kart='K-AKS-01 (üç terimli i kuvveti toplamı) · z = 2i⁴⁷ − 3i⁸² + i¹⁰⁵; Re(z) − Im(z)',
 metin='z = 2i⁴⁷ − 3i⁸² + i¹⁰⁵ olduğuna göre, z karmaşık sayısının gerçel kısmından sanal kısmının çıkarılmasıyla elde edilen değer kaçtır?',
 dogru=v,yan=[(e[0],'i⁴⁷ için kalanı 3 yerine 1 alıp i⁴⁷ = i bulmuş: z = 3 + 3i, fark 3 − 3 = 0.','islem'),(e[1],'i² = 1 sanıp i⁸² = 1 almış: z = −3 − i, fark −3 − (−1) = −2.','bilgi'),(e[2],'i¹⁰⁵ için kalanı 1 yerine 3 alıp i¹⁰⁵ = −i bulmuş: z = 3 − 3i, fark 3 − (−3) = 6.','islem'),(e[3],'Doğru z = 3 − i bulmuş, fakat fark yerine Re(z) + Im(z) = 3 + (−1) toplamını yazmış.','dikkat')],
 istenen='Re(z) − Im(z) farkı.',ip=['Üslerin her birini, kuvvetlerin kendini tekrar ettiği döngüdeki yerine indirerek yaz.'],bilgi=[IKB],
 ad=[A('Üsleri sadeleştir','Her üssün 4’e bölümünden kalan bulunur; i⁴ = 1 olduğundan yalnız kalan önemlidir.','47 = 4·11 + 3 · 82 = 4·20 + 2 · 105 = 4·26 + 1'),A('Kuvvetleri yaz','Kalanlara karşılık gelen kuvvetler yerine konur.','i⁴⁷ = i³ = −i · i⁸² = i² = −1 · i¹⁰⁵ = i'),A('z’yi bul','Değerler yerine yazılıp toplanır.','z = −2i + 3 + i = 3 − i'),A('Farkı hesapla','Gerçel kısım 3, sanal kısım −1’dir (i yazılmaz).','3 − (−1) = 4')],
 puf='Büyük üssü 4’e bölüp yalnız kalanı kullan.')

# ================= 02 kolay · şekil · iki nokta, çarpım =================
A2,B2=(2,3),(1,-2)
z1,z2=complex(*A2),complex(*B2); v=round((z1*z2).imag); assert v==-1
e_a=A2[1]*B2[1]
e_b=round((z1*z2.conjugate()).imag)
e_c=A2[0]*B2[1]-A2[1]*B2[0]
e_d=round((z1*complex(-2,1)).imag)
e=[e_a,e_b,e_c,e_d]; assert e==[-6,7,-7,-4] and len({v,*e})==5
body=nok(*A2,'A',BL,kil=True)+nok(*B2,'B',OR,'below right',kil=True)
SK=fig(arg(-3,4,-3,4,govde=body))
q('0002',tipId='kk-duzlem',tip='Karmaşık düzlemde nokta ve vektör',z='kolay',alt='Düzlemde Gösterim',kaz='Karmaşık düzlemdeki noktaları karmaşık sayı olarak okur ve çarpımlarının sanal kısmını hesaplar.',kalip='şekilli',
 kart='K-AKS-03 (iki nokta) · A(2, 3), B(1, −2); Im(z₁ z₂)',
 metin='Şekilde, karmaşık düzlemde A ve B noktaları verilmiştir. A noktası z₁ karmaşık sayısının, B noktası z₂ karmaşık sayısının görüntüsüdür.\nBuna göre z₁ · z₂ çarpımının sanal kısmı kaçtır?',
 dogru=v,yan=[(e[0],'Çarpımın sanal kısmını sanal kısımların çarpımı sanmış: 3 × (−2) = −6.','bilgi'),(e[1],'z₂ yerine eşleniğini alıp (2 + 3i)(1 + 2i) = −4 + 7i bulmuş.','dikkat'),(e[2],'Çapraz terimleri çıkarmış: 2 × (−2) − 3 × 1 = −7.','islem'),(e[3],'B noktasını −2 + i diye okuyup (gerçel ve sanal eksenleri karıştırıp) çarpmış: 2 × 1 + 3 × (−2) = −4.','dikkat')],
 istenen='z₁ · z₂ çarpımının sanal kısmı.',ip=['Noktaların yatay ve düşey koordinatlarını sayının hangi kısmına karşılık geldiğiyle eşleştir.'],bilgi=[DUZ,CRP],sekil=SK,
 ad=[A('Noktaları oku','Yatay koordinat gerçel, düşey koordinat sanal kısımdır.','A(2, 3) → z₁ = 2 + 3i · B(1, −2) → z₂ = 1 − 2i'),A('Çarp','Dağıtım yapılır ve i² = −1 yazılır.','(2 + 3i)(1 − 2i) = 2 − 4i + 3i − 6i² = 8 − i'),A('Sanal kısmı oku','i’nin katsayısı sanal kısımdır.','Im(z₁ · z₂) = −1')],
 puf='Önce noktaları a + bi olarak yaz, sonra işlem yap.')

# ================= 03 kolay · hikâyeli · bölme =================
zz=(7+1j)/(1-1j); assert eq(zz,3,4); v=-4
e_a=4
z_b=(7+1j)*(1-1j)/2; assert eq(z_b,4,-3); e_b=round(-z_b.imag)
z_c=(7+1j)*(1+1j); e_c=round(-z_c.imag)
e_d=round(z_c.imag)
e=[e_a,e_b,e_c,e_d]; assert e==[4,3,-8,8] and len({v,*e})==5
q('0003',tipId='kk-islem',tip='Dört işlem, eşlenik ve tablo',z='kolay',alt='Bölme ve Eşlenik',kaz='Bir karmaşık sayı bölümünü eşlenikle genişleterek sadeleştirir ve eşleniğinin sanal kısmını bulur.',kalip='hikâyeli',
 kart='K-AKS-02 (bölme) · (7 + i)/(1 − i) = 3 + 4i; Im(z̄)',
 metin='Bir mobil oyunda karakterin ekrandaki konumu, z = (7 + i)/(1 − i) karmaşık sayısıyla kodlanmaktadır. Oyun, karakterin aynadaki görüntüsünü z sayısının eşleniğiyle hesaplamaktadır.\nBuna göre z̄ sayısının sanal kısmı kaçtır?',
 dogru=v,yan=[(e[0],'Sonucu doğru bulmuş (z = 3 + 4i) fakat eşleniği almadan sanal kısmı 4 yazmış.','dikkat'),(e[1],'Payı ve paydayı (1 − i) ile genişleterek z = 4 − 3i bulmuş; bu yüzden z̄ = 4 + 3i olup sanal kısım 3 çıkmış.','bilgi'),(e[2],'Paydadaki 2’ye bölmeyi unutmuş: (7 + i)(1 + i) = 6 + 8i, eşleniği 6 − 8i.','islem'),(e[3],'Hem 2’ye bölmeyi unutmuş hem eşleniği almamış: sanal kısmı 8 yazmış.','islem')],
 istenen='z̄ sayısının sanal kısmı.',ip=['Paydadaki sayıyı gerçel yapmak için payı ve paydayı uygun bir sayıyla genişlet.'],bilgi=[ESL],
 ad=[A('Paydayı gerçel yap','Pay ve payda, paydanın eşleniği 1 + i ile çarpılır.','(7 + i)(1 + i) / ((1 − i)(1 + i))'),A('Sadeleştir','Pay: 7 + 7i + i + i² = 6 + 8i; payda: 1 − i² = 2.','z = (6 + 8i)/2 = 3 + 4i'),A('Eşleniği al','Sanal kısmın işareti değişir.','z̄ = 3 − 4i'),A('Sanal kısmı oku','i’nin katsayısı sanal kısımdır.','Im(z̄) = −4')],
 puf='Bölmede paydanın eşleniğiyle genişletmek paydayı gerçel yapar.')

# ================= 04 kolay · şekil · eşlenik =================
zA=complex(-3,2); topl=lambda w:round(w.real+w.imag); v=topl(2*zA+zA.conjugate()); assert v==-7
e_a=topl(2*zA-zA); e_b=topl(2*zA+zA)
zr=complex(2,-3); e_c=topl(2*zr+zr.conjugate())
w=2*zA+zA.conjugate(); e_d=round(w.real-w.imag)
e=[e_a,e_b,e_c,e_d]; assert e==[-1,-3,3,-11] and len({v,*e})==5
SK=fig(arg(-4,3,-1,4,govde=nok(-3,2,'z',BL,'above left',kil=True)))
q('0004',tipId='kk-duzlem',tip='Karmaşık düzlemde nokta ve vektör',z='kolay',alt='Eşlenik ve Düzlem',kaz='Düzlemde verilen noktanın sayısını okur; eşlenik içeren ifadeyi hesaplayarak gerçel ve sanal kısımlarını toplar.',kalip='şekilli',
 kart='K-AKS-03 (tek nokta) · z(−3, 2); 2z + z̄ ifadesinin Re + Im toplamı',
 metin='Şekilde, karmaşık düzlemde z karmaşık sayısının görüntüsü olan nokta verilmiştir.\nBuna göre 2z + z̄ sayısının gerçel kısmı ile sanal kısmının toplamı kaçtır?',
 dogru=v,yan=[(e[0],'z̄ yerine −z alıp (eşlenik almayı işaret değiştirmek sanıp) 2z − z = z = −3 + 2i bulmuş: −3 + 2 = −1.','bilgi'),(e[1],'Eşleniği almayı unutup 2z + z = 3z = −9 + 6i bulmuş: −9 + 6 = −3.','dikkat'),(e[2],'Noktanın eksenlerini karıştırıp z = 2 − 3i okumuş: 2z + z̄ = 6 − 3i, toplam 3.','dikkat'),(e[3],'Doğru sonuç −9 + 2i’yi bulmuş, fakat kısımları toplamak yerine gerçel kısımdan sanal kısmı çıkarmış: −9 − 2 = −11.','islem')],
 istenen='2z + z̄ sayısının gerçel kısmı ile sanal kısmının toplamı.',ip=['Önce noktayı sayıya çevir; eşleniğin sanal kısmının işareti ne olur?'],bilgi=[DUZ],sekil=SK,
 ad=[A('Noktayı oku','Yatay koordinat −3, düşey koordinat 2’dir.','z = −3 + 2i'),A('Eşleniği yaz','Sanal kısmın işareti değişir.','z̄ = −3 − 2i'),A('İfadeyi hesapla','2z ve z̄ toplanır.','2z + z̄ = −6 + 4i − 3 − 2i = −9 + 2i'),A('Kısımları topla','Gerçel kısım −9, sanal kısım 2’dir.','−9 + 2 = −7')],
 puf='z + z̄ = 2Re(z) olduğunu da akılda tut: eşlenik toplamda sanal kısmı yok eder.')

# ================= 05 orta · öncüllü · modül =================
zq=(2+1j)**2; assert eq(zq,3,4)
I1=abs(abs(zq)-5)<1e-9; I2=abs(abs(zq**2)-5)<1e-9; I3=eq(zq-zq.conjugate(),0,8)
assert (I1,I2,I3)==(True,False,True)
q('0005',tipId='kk-modul',tip='Modül ve uzaklık',z='orta',alt='Modül ve Eşlenik',kaz='Modül, eşlenik ve kuvvet özelliklerini kullanarak karmaşık sayı yargılarının doğruluğunu belirler.',kalip='öncüllü',
 kart='K-AKS-04 (modül yargıları) · z = (2 + i)² = 3 + 4i; |z|, |z²|, z − z̄',
 metin='Bir matematik kulübünde z = (2 + i)² karmaşık sayısı için öğrencilerden aşağıdaki yargıların doğruluğunu incelemeleri isteniyor:\nI. |z| = 5\nII. |z²| = 5\nIII. z − z̄ = 8i\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='I ve III',yan=[('Yalnız I','z − z̄ farkında gerçel kısımlar çıkarıp sanal kısımlar da yok olur sanarak III’ü yanlış bulmuş (aslında 2 · 4i = 8i).','bilgi'),('Yalnız III','|3 + 4i| = 3² + 4² = 25 diye karekök almadan hesaplayıp I’i yanlış bulmuş.','islem'),('I ve II','|z²| = |z| sanıp II’yi doğru bulmuş, III’te z − z̄’yi gerçel sayı saymış.','bilgi'),('II ve III','|3 + 4i|’yi karekök almadan 25 bulup I’i yanlış saymış; |z²| = |z| sanıp II’yi doğru kabul etmiş.','dikkat')],
 sira=['Yalnız I','Yalnız III','I ve II','II ve III','I ve III'],istenen='Doğru olan yargılar.',ip=['Önce z’yi a + bi biçiminde yaz, sonra her yargıyı ayrı ayrı sına.'],bilgi=[MOD,ESL],
 ad=[A('z’yi aç','Kare alınır ve i² = −1 yazılır.','(2 + i)² = 4 + 4i + i² = 3 + 4i'),A('I’i incele','Modül karekökle bulunur.','|z| = √(9 + 16) = 5 → doğru'),A('II’yi incele','Kuvvetin modülü modülün kuvvetidir.','|z²| = |z|² = 25 → yanlış'),A('III’ü incele','Eşlenik çıkarılınca gerçel kısım yok olur, sanal kısım iki katına çıkar.','z − z̄ = 8i → doğru')],
 puf='Modül hesabında karekök almayı, kuvvette ise |zⁿ| = |z|ⁿ özelliğini unutma.')

# ================= 06 orta · hikâyeli · denklem =================
a_,b_=3,2; zc=complex(a_,b_); assert eq(2*zc-zc.conjugate(),3,6); v=a_**2+b_**2
e=[3**2+6**2,1**2+6**2,a_+b_,a_**2]; assert e==[45,37,5,9] and len({v,*e})==5
q('0006',tipId='kk-denklem',tip='Karmaşık sayı denklemi ve tanımlı işlem',z='orta',alt='Eşlenikli Denklem',kaz='Eşlenik içeren karmaşık sayı denklemini gerçel ve sanal kısımları eşitleyerek çözer.',kalip='hikâyeli',
 kart='K-AKS-05 (eşlenikli denklem) · 2z − z̄ = 3 + 6i; |z|²',
 metin='Bir şifreleme uygulamasında gizli anahtar, 2z − z̄ = 3 + 6i eşitliğini sağlayan z karmaşık sayısıdır. Uygulama, anahtarın gücünü |z|² değeriyle ölçmektedir.\nBuna göre anahtarın gücü kaçtır?',
 dogru=v,yan=[(e[0],'2z − z̄’yi 2z − z = z gibi okuyup z = 3 + 6i bulmuş: |z|² = 45.','bilgi'),(e[1],'Eşitliği 2z + z̄ gibi çözüp gerçel kısım için 3a = 3, sanal kısım için b = 6 almış: |z|² = 1 + 36.','islem'),(e[2],'Doğru z = 3 + 2i’yi bulmuş, fakat |z|² yerine Re(z) + Im(z) toplamını yazmış.','dikkat'),(e[3],'|z|² = a² + b² yerine yalnız gerçel kısmın karesini almış: 3² = 9.','islem')],
 istenen='|z|² değeri.',ip=['z = a + bi alıp eşlenikli eşitliğin gerçel ve sanal kısımlarını ayrı ayrı yaz.'],bilgi=[ESL],
 ad=[A('z’yi yaz','z = a + bi ve z̄ = a − bi alınır.','2(a + bi) − (a − bi) = 3 + 6i'),A('Kısımları ayır','Gerçel kısım a, sanal kısım 3b olur.','a + 3bi = 3 + 6i'),A('Eşitle','Gerçel ve sanal kısımlar ayrı ayrı eşitlenir.','a = 3 · 3b = 6 → b = 2'),A('Modülün karesi','|z|² = a² + b²’dir.','|z|² = 9 + 4 = 13')],
 puf='Eşlenikli denklemde z = a + bi yazıp gerçel ve sanal kısımları ayrı eşitle.')

# ================= 07 orta · şekil · paralelkenar =================
Ap,Bp,Cp=(-3,2),(0,-1),(4,2)
zA_,zB_,zC_=map(lambda t:complex(*t),(Ap,Bp,Cp)); zD=zA_+zC_-zB_; assert eq(zD,1,5); v=cs(zD.conjugate()); assert v=='1 − 5i'
e1=cs(zD); e2=cs((zB_+zC_-zA_).conjugate()); e3=cs((zA_+zB_-zC_).conjugate()); e4=cs((zA_+zB_+zC_).conjugate())
assert e2=='7 + i' and e3==M+'7 + i' and e4=='1 − 3i' and len({v,e1,e2,e3,e4})==5
SK=fig(arg(-4,5,-2,6,govde='\\draw[line width=1.8pt,'+BL+'] '+f'({Ap[0]*SC},{Ap[1]*SC}) -- ({Bp[0]*SC},{Bp[1]*SC}) -- ({Cp[0]*SC},{Cp[1]*SC});'+nok(*Ap,'A',BL,'above left')+nok(*Bp,'B',BL,'below left')+nok(*Cp,'C',BL,'above right')))
q('0007',tipId='kk-duzlem',tip='Karmaşık düzlemde nokta ve vektör',z='orta',alt='Paralelkenar Köşesi',kaz='Karmaşık düzlemde verilen üç köşeden paralelkenarın dördüncü köşesini vektör toplamıyla bulur ve eşleniğini yazar.',kalip='şekilli',
 kart='K-AKS-03 (üç köşe) · A(−3, 2), B(0, −1), C(4, 2); D = A + C − B',
 metin='Bir mimar, karmaşık düzlemde köşeleri sırasıyla A, B, C ve D olan paralelkenar biçiminde bir bahçe tasarlıyor. Şekilde, bahçenin A, B ve C köşelerinin görüntüleri verilmiştir; D köşesi henüz çizilmemiştir.\nBuna göre D köşesinin görüntüsü olan karmaşık sayının eşleniği aşağıdakilerden hangisidir?',
 dogru=v,yan=[(e1,'D köşesini doğru bulmuş (1 + 5i), fakat sorulan eşleniği almayı unutmuş.','dikkat'),(e2,'Paralelkenarda D = A + C − B yerine B + C − A almış: 7 − i, eşleniği 7 + i.','bilgi'),(e3,'D = A + B − C bağıntısını kurmuş: −7 − i, eşleniği −7 + i.','bilgi'),(e4,'Üç köşeyi toplayıp D = A + B + C = 1 + 3i bulmuş ve eşleniğini yazmış.','islem')],
 sira=['1 − 5i','1 + 5i','7 + i',M+'7 + i','1 − 3i'],
 istenen='D köşesinin görüntüsü olan sayının eşleniği.',ip=['Paralelkenarın köşegenlerinin orta noktaları aynıdır; bunu sayılarla yaz.'],bilgi=[DUZ],sekil=SK,
 ad=[A('Köşeleri oku','Her köşenin koordinatları sayı olarak yazılır.','A = −3 + 2i; B = −i; C = 4 + 2i'),A('Köşegenleri eşitle','AC ve BD köşegenlerinin orta noktaları aynı olduğundan A + C = B + D’dir.','D = A + C − B'),A('D’yi hesapla','Değerler yerine konur.','D = (−3 + 2i) + (4 + 2i) − (−i) = 1 + 5i'),A('Eşleniği yaz','Sanal kısmın işareti değiştirilir.','D̄ = 1 − 5i')],
 puf='Paralelkenarda karşılıklı köşelerin toplamı eşittir: A + C = B + D.')

# ================= 08 orta · şekil · iki nokta arası uzaklık =================
Ar,Br=(-2,1),(4,9); d=abs(complex(*Ar)-complex(*Br)); assert abs(d-10)<1e-9; v=10
dx,dy=Br[0]-Ar[0],Br[1]-Ar[1]; e=[dx,dy,dx+dy,dx**2+dy**2]; assert e==[6,8,14,100] and len({v,*e})==5
S8=0.5
SK=fig(arg(-3,5,-1,10,sc=S8,govde='\\draw[dashed,'+BL+',thick] (%.2f,%.2f) -- (%.2f,%.2f);'%(Ar[0]*S8,Ar[1]*S8,Br[0]*S8,Br[1]*S8)+nok(*Ar,'A',BL,'above left',sc=S8)+nok(*Br,'B',OR,'above right',sc=S8)))
q('0008',tipId='kk-modul',tip='Modül ve uzaklık',z='orta',alt='Modül ve Uzaklık',kaz='Karmaşık düzlemdeki iki noktanın sayılarını okuyup farklarının modülünü uzaklık olarak hesaplar.',kalip='şekilli',
 kart='K-AKS-04 (iki nokta arası uzaklık) · A(−2, 1), B(4, 9); |z₁ − z₂|',
 metin='Şekilde, karmaşık düzlemde A ve B noktaları gösterilmiştir. A noktası z₁ sayısının, B noktası z₂ sayısının görüntüsüdür.\nBuna göre |z₁ − z₂| değeri kaçtır?',
 dogru=v,yan=[(e[0],'Uzaklık olarak yalnız yatay farkı (6) almış.','dikkat'),(e[1],'Uzaklık olarak yalnız düşey farkı (8) almış.','dikkat'),(e[2],'Yatay ve düşey farkların toplamını uzaklık sanmış: 6 + 8.','bilgi'),(e[3],'6² + 8² = 100’ü bulup karekök almayı unutmuş.','islem')],
 istenen='|z₁ − z₂| değeri.',ip=['Fark sayısının gerçel ve sanal kısımlarını koordinat farklarından yaz.'],bilgi=[MOD],sekil=SK,
 ad=[A('Noktaları oku','Her noktanın koordinatı sayının gerçel ve sanal kısmıdır.','z₁ = −2 + i · z₂ = 4 + 9i'),A('Farkı al','Gerçel ve sanal kısımlar ayrı ayrı çıkarılır.','z₁ − z₂ = −6 − 8i'),A('Modülü hesapla','Modül, kısımların karelerinin toplamının karekökü olur.','|z₁ − z₂| = √(36 + 64) = 10')],
 puf='|z₁ − z₂| iki nokta arasındaki uzaklıktır; koordinat farklarıyla Pisagor kur.')

# ================= 09 orta · şekil · daire bölgesi =================
cm,r=(2,-1),3
c1='|z − 2 + i| ≤ 3'; c2='|z + 2 − i| ≤ 3'; c3='|z − 2 + i| < 3'; c4='|z − 2 − i| ≤ 3'; c5='|z − 2 + i| ≥ 3'
f1=lambda p:abs(p-complex(2,-1))<=3+1e-9
f2=lambda p:abs(p+complex(2,-1))<=3+1e-9
f3=lambda p:abs(p-complex(2,-1))<3-1e-9
f4=lambda p:abs(p-complex(2,1))<=3+1e-9
f5=lambda p:abs(p-complex(2,-1))>=3-1e-9
ts=[complex(x/2,y/2) for x in range(-12,16) for y in range(-14,10)]
for f in (f2,f3,f4,f5): assert any(f(p)!=f1(p) for p in ts)
ust=f'\\fill[blue!18] ({cm[0]*SC:.3f},{cm[1]*SC:.3f}) circle ({r*SC:.3f});'
body=f'\\draw[{BL},line width=1.8pt] ({cm[0]*SC:.3f},{cm[1]*SC:.3f}) circle ({r*SC:.3f});\\fill[{BL}] ({cm[0]*SC:.3f},{cm[1]*SC:.3f}) circle (0.08);'
SK=fig(arg(-2,6,-5,3,ust=ust,govde=body))
q('0009',tipId='kk-yer',tip='Geometrik yer ve bölge',z='orta',alt='Daire Bölgesi',kaz='Karmaşık düzlemde verilen daire bölgesini merkez ve yarıçapı okuyarak modül eşitsizliğiyle ifade eder.',kalip='şekilli',
 kart='K-AKS-07 (daire bölgesi) · merkez (2, −1), yarıçap 3; |z − (2 − i)| ≤ 3',
 metin='Bir yazılım şirketi, haritadaki bir bölgeyi karmaşık düzlemde gösteriyor. Şekilde, çember dahil olmak üzere taralı bölge verilmiştir; bölgedeki her noktanın görüntüsü z karmaşık sayısıdır.\nBuna göre taralı bölgeyi tam olarak gösteren eşitsizlik aşağıdakilerden hangisidir?',
 dogru=c1,yan=[(c2,'Merkezin görüntüsünü ters işaretle (z + 2 − i) yazmış: merkez −2 + i olur.','bilgi'),(c3,'Çember dahil olduğunu görmeyip sınırı dışarıda bırakan < işaretini seçmiş; çember üzerindeki noktalar bu eşitsizliği sağlamaz.','dikkat'),(c4,'Merkezin sanal kısmını −1 yerine +1 okumuş: z − 2 − i.','dikkat'),(c5,'Daire bölgesi yerine bölgenin dışını gösteren yönü (≥) seçmiş.','dikkat')],
 sira=[c2,c1,c4,c3,c5],istenen='Taralı bölgeyi gösteren eşitsizlik.',ip=['Çemberin merkezini ve yarıçapını ızgaradan oku; |z − merkez| ≤ yarıçap kalıbına yerleştir.'],bilgi=[YER],sekil=SK,
 ad=[A('Merkezi oku','Çemberin merkezi yatayda 2, düşeyde −1 noktasındadır.','merkez = 2 − i'),A('Yarıçapı oku','Merkezden çembere olan yatay uzaklık 3 birimdir.','r = 3'),A('Eşitsizliği yaz','Bölge çemberin içi ve kendisidir; merkez z − (2 − i) biçiminde yazılır.','|z − (2 − i)| ≤ 3 → |z − 2 + i| ≤ 3')],
 puf='Merkez z₀ ise ifade z − z₀’dır: merkezin işareti ifadede ters görünür.')

# ================= 10 orta · şekil · yarı düzlem =================
A10,B10=(-2,1),(2,3); zA10,zB10=complex(*A10),complex(*B10)
assert eq((zA10+zB10)/2,0,2)
n1='|z + 2 − i| ≤ |z − 2 − 3i|'; n2='|z + 2 − i| ≥ |z − 2 − 3i|'; n3='|z − 2 + i| ≤ |z + 2 + 3i|'; n4='|z + 2 − i| ≤ |z − 2 + 3i|'; n5='|z + 2 − i| = |z − 2 − 3i|'
g=lambda p:abs(p-zA10)<=abs(p-zB10)+1e-9
h1=lambda p:abs(p+complex(2,-1))<=abs(p-complex(2,3))+1e-9
h2=lambda p:abs(p+complex(2,-1))>=abs(p-complex(2,3))-1e-9
h3=lambda p:abs(p-complex(2,-1))<=abs(p+complex(2,3))+1e-9
h4=lambda p:abs(p+complex(2,-1))<=abs(p-complex(2,-3))+1e-9
h5=lambda p:abs(abs(p+complex(2,-1))-abs(p-complex(2,3)))<1e-9
ts=[complex(x/2,y/2) for x in range(-10,11) for y in range(-6,16)]
assert all(g(p)==h1(p) for p in ts)
for h in (h2,h3,h4,h5): assert any(h(p)!=g(p) for p in ts)
poly=[(-4,-2),(2,-2),(-2,6),(-4,6)]
assert all(g(complex(x,y)) for x,y in poly)
ust='\\fill[blue!15] '+' -- '.join(f'({x*SC:.2f},{y*SC:.2f})' for x,y in poly)+' -- cycle;'
body=f'\\draw[{BL},line width=1.8pt] ({2*SC:.2f},{-2*SC:.2f}) -- ({-2*SC:.2f},{6*SC:.2f});'+nok(*A10,'A',BL,'above left')+nok(*B10,'B',OR,'above right')
SK=fig(arg(-4,4,-2,6,ust=ust,govde=body))
q('0010',tipId='kk-yer',tip='Geometrik yer ve bölge',z='orta',alt='Eşit Uzaklık Bölgesi',kaz='İki noktaya uzaklıkları karşılaştıran bölgeyi (yarı düzlem) modül eşitsizliğiyle ifade eder.',kalip='şekilli',
 kart='K-AKS-07 (orta dikme ve yarı düzlem) · A(−2, 1), B(2, 3); |z − z₁| ≤ |z − z₂|',
 metin='Bir kargo firması, A ve B noktalarındaki iki şubesinden hangisine daha yakın olunduğunu karmaşık düzlemde gösteriyor. Şekilde A noktası z₁ sayısının, B noktası z₂ sayısının görüntüsüdür; taralı bölge, doğru dahil olmak üzere A şubesine daha yakın ya da eşit uzaklıktaki noktaları göstermektedir.\nBuna göre taralı bölgedeki her z sayısı aşağıdakilerden hangisini sağlar?',
 dogru=n1,yan=[(n2,'Doğru ikilinin uzaklıklarını yazmış fakat eşitsizliğin yönünü ters kurup B’ye daha yakın olanı göstermiş.','dikkat'),(n3,'Merkezleri z − z₁ yerine z + z₁ biçiminde (işaretlerini ters) yazmış.','bilgi'),(n4,'B’nin sanal kısmının işaretini ters yazmış: z − 2 + 3i.','dikkat'),(n5,'Yalnız orta dikme doğrusunu gösteren eşitliği seçmiş; taralı bölge bir yarı düzlemdir.','bilgi')],
 sira=[n2,n3,n4,n1,n5],istenen='Taralı bölgeyi gösteren bağıntı.',ip=['A’ya uzaklığı z − z₁ ile, B’ye uzaklığı z − z₂ ile yaz ve hangisinin küçük olduğuna bak.'],bilgi=[YER,MOD],sekil=SK,
 ad=[A('Noktaları oku','Her noktanın koordinatları sayının gerçel ve sanal kısmıdır.','z₁ = −2 + i · z₂ = 2 + 3i'),A('Uzaklıkları yaz','A’ya uzaklık |z − z₁|, B’ye uzaklık |z − z₂|’dir.','|z + 2 − i| ve |z − 2 − 3i|'),A('Yönü belirle','Taralı bölge A’ya daha yakın noktaları ve doğrunun kendisini içerir.','|z − z₁| ≤ |z − z₂|'),A('Yaz','Sayılar yerine konur.','|z + 2 − i| ≤ |z − 2 − 3i|')],
 puf='Hangisine “daha yakın” ise onun uzaklığı eşitsizliğin küçük tarafında yer alır.')

# ================= 11 orta · öncüllü · ikinci derece kökleri =================
xx=sp.symbols('x'); ks=sp.solve(xx**2-6*xx+13,xx); assert set(ks)=={3+2*sp.I,3-2*sp.I}
k1,k2=3+2*sp.I,3-2*sp.I
assert (not (k1.is_real or k2.is_real)) and abs(k1)==abs(k2) and sp.expand(k1**2+k2**2)==10 and 2*sp.expand(k1*k2)==26
q('0011',tipId='kk-ikinci',tip='İkinci derece denklemin karmaşık kökleri',z='orta',alt='Karmaşık Kökler',kaz='Δ < 0 olan ikinci derece denklemin kökleri hakkındaki yargıların doğruluğunu belirler.',kalip='öncüllü',
 kart='K-AKS-06 (Δ < 0) · x² − 6x + 13 = 0; kökler 3 ± 2i; yargılar: gerçellik, modül, kareler toplamı',
 metin='x² − 6x + 13 = 0 denkleminin kökleri z₁ ve z₂ karmaşık sayılarıdır. Bir öğrenci bu köklerle ilgili aşağıdaki yargıları öne sürüyor:\nI. z₁ ve z₂ gerçel sayılardır.\nII. |z₁| = |z₂| eşitliği sağlanır.\nIII. z₁² + z₂² = 26 olur.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru='Yalnız II',yan=[('Yalnız I','Δ < 0 olduğunu görmeyip kökleri gerçel sanmış; z₁ ve z₂ farklı sayılar olduğundan modüllerini de farklı bulmuş.','bilgi'),('I ve II','Δ < 0 olduğunu görmeyip kökleri gerçel sanmış; modüllerin eşitliğini ise doğru bulmuş.','bilgi'),('I ve III','Kökleri gerçel sanmış; z₁ ve z₂ farklı olduğundan modüllerini farklı bulmuş; III’te z₁² + z₂² yerine 2z₁z₂ = 26 hesaplamış.','islem'),('II ve III','Kökleri doğru bulmuş ve modülleri eşit görmüş; III’te (z₁ + z₂)² terimini atlayıp yalnız 2z₁z₂ = 26 almış.','islem')],
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],istenen='Doğru olan yargılar.',ip=['Kökleri bulup yargıların her birini bu köklerle ayrı ayrı sına.'],bilgi=[IKI,MOD],
 ad=[A('Diskriminantı bul','Δ negatif olduğundan kökler gerçel olmaz.','Δ = 36 − 52 = −16 → I yanlış'),A('Kökleri yaz','Δ’nın karekökü 4i olur.','x = (6 ± 4i)/2 = 3 ± 2i'),A('II’yi sına','Kökler birbirinin eşleniğidir; eşleniklerin modülü eşittir.','|3 + 2i| = |3 − 2i| = √13 → II doğru'),A('III’ü sına','Kareler toplamı kökler toplamı ve çarpımıyla bulunur.','z₁² + z₂² = 6² − 2 × 13 = 10 → III yanlış')],
 puf='Gerçel katsayılı denklemde Δ < 0 ise kökler gerçel olmaz, birbirinin eşleniği olur.')

# ================= 12 orta · öncüllü · şekil =================
zz_,ww_,uu_,tt_=complex(3,2),complex(-3,-2),complex(3,-2),complex(-2,3)
J1=abs(uu_+zz_)<1e-9; J2=abs(ww_+zz_)<1e-9; J3=abs(tt_-1j*zz_)<1e-9
assert (J1,J2,J3)==(False,True,True) and abs(uu_-zz_.conjugate())<1e-9
body=nok(3,2,'z',BL,'above right')+nok(-3,-2,'w',OR,'below left')+nok(3,-2,'u',GR,'below right')+nok(-2,3,'t',PU,'above left')
SK=fig(arg(-4,4,-3,4,govde=body))
q('0012',tipId='kk-duzlem',tip='Karmaşık düzlemde nokta ve vektör',z='orta',alt='Simetri ve Dönme',kaz='Karmaşık düzlemde verilen noktalar arasındaki simetri ve dönme ilişkilerini sayı eşitlikleriyle yorumlar.',kalip='öncüllü',
 kart='K-AKS-03 (dört nokta) · z(3, 2), w(−3, −2), u(3, −2), t(−2, 3); −z, z̄, iz',
 metin='Şekilde, karmaşık düzlemde sırasıyla z, w, u ve t sayılarının görüntüleri verilmiştir.\nBuna göre,\nI. u = −z\nII. w = −z\nIII. t = i · z\neşitliklerinden hangileri doğrudur?',
 dogru='II ve III',yan=[('Yalnız I','u noktasını z’nin orijine göre simetriği sanmış; oysa u, z’nin gerçel eksene göre simetriği olan eşleniğidir.','bilgi'),('Yalnız II','i ile çarpmanın noktayı 90° döndürdüğünü bilmeyip III’ü yanlış saymış.','bilgi'),('Yalnız III','−z sayısının orijine göre simetrik nokta olduğunu fark etmeyip II’yi yanlış bulmuş.','bilgi'),('I ve II','z̄ ile −z’yi karıştırıp I’i de doğru saymış; i ile çarpmanın döndürme olduğunu bilmeyip III’ü yanlış bulmuş.','dikkat')],
 sira=['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],istenen='Doğru olan eşitlikler.',ip=['Her noktanın koordinatlarından sayısını yaz; sonra eşitliklerin iki tarafını karşılaştır.'],bilgi=[DUZ,DON],sekil=SK,
 ad=[A('Noktaları oku','Her noktanın koordinatları sayıya çevrilir.','z = 3 + 2i · w = −3 − 2i · u = 3 − 2i · t = −2 + 3i'),A('I’i sına','−z = −3 − 2i’dir; u ise z’nin eşleniğidir.','u = z̄ ≠ −z → yanlış'),A('II’yi sına','w, z’nin orijine göre simetriğidir.','w = −3 − 2i = −z → doğru'),A('III’ü sına','i ile çarpmak 90° döndürür.','i(3 + 2i) = −2 + 3i = t → doğru')],
 puf='Eşlenik gerçel eksene, −z orijine göre simetriktir; i ile çarpma 90° döndürür.')

# ================= 13 orta · düz · toplam ve çarpım =================
zt=complex(3,-4); assert eq(zt+zt.conjugate(),6,0) and abs(zt*zt.conjugate()-25)<1e-9; v=round((zt**2).imag); assert v==-24
e=[24,-12,-4,-7]; assert e==[24,round(zt.real*zt.imag),round(zt.imag),round((zt**2).real)] and len({v,*e})==5
q('0013',tipId='kk-modul',tip='Modül ve uzaklık',z='orta',alt='Toplam ve Çarpım Koşulu',kaz='z + z̄ ve z · z̄ değerlerinden z’yi bulup karesinin sanal kısmını hesaplar.',kalip='düz',
 kart='K-AKS-04 (eşlenik toplamı ve çarpımı) · z + z̄ = 6, z · z̄ = 25, Im(z) < 0; Im(z²)',
 metin='z karmaşık sayısının sanal kısmı negatiftir ve z + z̄ = 6, z · z̄ = 25 eşitlikleri sağlanmaktadır.\nBuna göre z² sayısının sanal kısmı kaçtır?',
 dogru=v,yan=[(e[0],'Sanal kısmın negatif olması koşulunu atlayıp z = 3 + 4i almış: Im(z²) = 24.','dikkat'),(e[1],'z² = a² − b² + 2abi’de 2 çarpanını unutup yalnız ab = −12 almış.','islem'),(e[2],'z = 3 − 4i’yi bulup z²’nin sanal kısmı yerine z’nin sanal kısmını (−4) yazmış.','dikkat'),(e[3],'z² = −7 − 24i’yi doğru bulmuş fakat sanal kısım yerine gerçel kısmı (−7) okumuş.','dikkat')],
 istenen='z² sayısının sanal kısmı.',ip=['z = a + bi alıp iki eşitlikten a ve b hakkında ne söylenebileceğine bak.'],bilgi=[ESL],
 ad=[A('Toplamı yaz','z + z̄ = 2a olduğundan gerçel kısım bulunur.','2a = 6 → a = 3'),A('Çarpımı yaz','z · z̄ = a² + b²’dir.','9 + b² = 25 → b = ±4'),A('İşareti seç','Sanal kısım negatif olmalıdır.','b = −4 → z = 3 − 4i'),A('Kareyi al','İki terimin karesi açılır ve i² = −1 yazılır.','z² = 9 − 24i + 16i² = −7 − 24i → Im(z²) = −24')],
 puf='z + z̄ gerçel kısmı, z · z̄ modülün karesini verir: ikisi birlikte z’yi belirler.')

# ================= 14 orta · tablo =================
T14=[('z₁',2,-3),('z₂',1,4),('z₃',-1,2)]
c=[complex(a,b) for _,a,b in T14]
v=round((c[0]*c[1]-c[2]**2).imag); assert v==9
e_a=round((c[0]*c[1]+c[2]**2).imag)
e_b=round(c[0].real*c[1].imag-c[0].imag*c[1].real)-round((c[2]**2).imag)
e_c=round((c[0]*c[1]).imag)
e_d=round((c[0]*c[1].conjugate()).imag-(c[2]**2).imag)
assert sorted([e_d,e_a,e_c,e_b])==[-7,1,5,15] and len({v,e_d,e_a,e_c,e_b})==5
fm_=lambda t:(M if t<0 else '')+str(abs(t))
SK=tablo_svg(['Sayı','Gerçel kısım','Sanal kısım'],[[n,fm_(a),fm_(b)] for n,a,b in T14])
q('0014',tipId='kk-islem',tip='Dört işlem, eşlenik ve tablo',z='orta',alt='Tablodan İşlem',kaz='Tabloda gerçel ve sanal kısımları verilen karmaşık sayılarla çarpma ve çıkarma yaparak sonucun sanal kısmını bulur.',kalip='tablo',
 kart='K-AKS-02 (tablo) · z₁ = 2 − 3i, z₂ = 1 + 4i, z₃ = −1 + 2i; Im(z₁z₂ − z₃²)',
 metin='Bir sinyal işleme laboratuvarında üç ölçümün karmaşık sayı karşılıkları z₁, z₂ ve z₃ olarak adlandırılıyor. Bu sayıların gerçel ve sanal kısımları aşağıdaki tabloda verilmiştir.\nBuna göre z₁ · z₂ − z₃² sayısının sanal kısmı kaçtır?',
 dogru=v,yan=[(e_d,'z₁ · z₂ yerine z₁ · z̄₂ alıp sanal kısmı −11 bulmuş: −11 − (−4) = −7.','bilgi'),(e_a,'Çıkarma yerine toplama yapmış: 5 + (−4) = 1.','dikkat'),(e_c,'z₃²’yi hesaplamayı unutup yalnız z₁ · z₂ sayısının sanal kısmını (5) yazmış.','dikkat'),(e_b,'z₁ · z₂ çarpımında çapraz terimi çıkarıp sanal kısmı 11 bulmuş: 11 − (−4) = 15.','islem')],
 istenen='z₁ · z₂ − z₃² sayısının sanal kısmı.',ip=['Tablodan üç sayıyı yazıp çarpımı ve kareyi ayrı hesapla; sonra çıkar.'],bilgi=[CRP],sekil=SK,
 ad=[A('Sayıları yaz','Tablodaki kısımlar a + bi biçiminde yazılır.','z₁ = 2 − 3i · z₂ = 1 + 4i · z₃ = −1 + 2i'),A('Çarpımı bul','Dağıtım yapılıp i² = −1 yazılır.','z₁z₂ = 2 + 8i − 3i − 12i² = 14 + 5i'),A('z₃²’yi bul','Kare alınır.','z₃² = 1 − 4i + 4i² = −3 − 4i'),A('Çıkarıp oku','Sanal kısımlar çıkarılır.','z₁z₂ − z₃² = 17 + 9i → Im = 9')],
 puf='Çarpımda çapraz terimleri toplarken i² = −1’i yalnız gerçel kısma yaz.')

# ================= 15 zor · yeni nesil · tanımlı işlem =================
def yild(a,b): return a*b.conjugate()
zs=complex(3,1); assert eq(yild(1+1j,zs),4,2); v=round(yild(zs,1-1j).imag); assert eq(yild(zs,1-1j),2,4) and v==4
z_b=complex(3,-1); e_a=round(yild(z_b,1-1j).imag)
e_b=round(yild(1-1j,zs).imag); e_c=round((zs*(1-1j)).imag); e_d=round(zs.imag)
assert sorted([e_a,e_b,e_c,e_d])==[-4,-2,1,2] and len({v,e_a,e_b,e_c,e_d})==5
q('0015',tipId='kk-denklem',tip='Karmaşık sayı denklemi ve tanımlı işlem',z='zor',alt='Tanımlı İşlem',kaz='Eşlenik içeren tanımlı bir işlemin kuralını uygulayarak bilinmeyen karmaşık sayıyı bulur ve işlemin sonucunu hesaplar.',kalip='yeni nesil',
 kart='K-AKS-05 (tanımlı işlem) · a ∗ b = a · b̄; (1 + i) ∗ z = 4 + 2i; z ∗ (1 − i)',
 metin='Karmaşık sayılar kümesinde, a ∗ b = a · b̄ biçiminde bir ∗ işlemi tanımlanıyor (b̄, b sayısının eşleniğidir).\n(1 + i) ∗ z = 4 + 2i\neşitliğini sağlayan z karmaşık sayısı için z ∗ (1 − i) sayısının sanal kısmı kaçtır?',
 dogru=v,yan=[(e_b,'İşlemde sırayı değiştirip (1 − i) ∗ z = (1 − i) · z̄ almış: sanal kısım −4.','dikkat'),(e_c,'İkinci adımda (1 − i)’nin eşleniğini almayı unutup z · (1 − i) = 4 − 2i hesaplamış.','dikkat'),(e_d,'z’yi doğru bulmuş (3 + i); sorulan işlemi yapmak yerine z’nin sanal kısmını yazmış.','dikkat'),(e_a,'z̄’yi bulup z diye kullanmış (z = 3 − i): (3 − i)(1 + i) = 4 + 2i, sanal kısım 2.','bilgi')],
 istenen='z ∗ (1 − i) sayısının sanal kısmı.',ip=['Önce tanımı uygulayıp z̄’yi, sonra z’yi bul; ikinci işlemde yine tanımdaki eşleniği hatırla.'],bilgi=[ESL],
 ad=[A('Tanımı uygula','(1 + i) ∗ z = (1 + i) · z̄ olduğundan z̄ çözülür.','(1 + i) · z̄ = 4 + 2i'),A('z̄’yi bul','Eşitliğin iki tarafı 1 + i’nin eşleniğiyle genişletilerek bölünür.','z̄ = (4 + 2i)(1 − i)/2 = 3 − i'),A('z’yi bul','Eşleniğin eşleniği sayının kendisidir.','z = 3 + i'),A('İşlemi hesapla','z ∗ (1 − i) = z · (1 + i) (eşlenik alınır).','(3 + i)(1 + i) = 2 + 4i → Im = 4')],
 puf='Tanımlı işlemde hangi sayının eşleniğinin alındığına işlem sırasını bozmadan dikkat et.')

# ================= 16 zor · şekil · halka dilimi alanı =================
def alan(ri,ro,aci): return aci/360*math.pi*(ro**2-ri**2)
assert abs(alan(1,3,90)-2*math.pi)<1e-9 and abs(alan(0,3,90)-9*math.pi/4)<1e-9 and abs(alan(1,3,180)-4*math.pi)<1e-9 and abs(alan(1,3,360)-8*math.pi)<1e-9 and abs(math.pi/4*(3-1)**2-math.pi)<1e-9
ust=f'\\fill[blue!22] (45:{1*SC:.3f}) arc (45:135:{1*SC:.3f}) -- (135:{3*SC:.3f}) arc (135:45:{3*SC:.3f}) -- cycle;'
body=f'\\draw[gray!70,dashed] (0,0) circle ({1*SC:.3f}); \\draw[gray!70,dashed] (0,0) circle ({3*SC:.3f});'
body+=f'\\draw[dashed,{OR},thick] ({-3.6*SC:.3f},{-3.6*SC:.3f}) -- ({3.6*SC:.3f},{3.6*SC:.3f}); \\draw[dashed,{OR},thick] ({-3.6*SC:.3f},{3.6*SC:.3f}) -- ({3.6*SC:.3f},{-3.6*SC:.3f});'
body+=f'\\draw[{BL},line width=1.8pt] (45:{1*SC:.3f}) arc (45:135:{1*SC:.3f}) -- (135:{3*SC:.3f}) arc (135:45:{3*SC:.3f}) -- cycle;'
SK=fig(arg(-4,4,-4,4,ust=ust,govde=body))
q('0016',tipId='kk-yer',tip='Geometrik yer ve bölge',z='orta',alt='Halka Dilimi Alanı',kaz='Karmaşık düzlemde iki çember ve iki doğruyla sınırlanan bölgenin alanını çember dilimi alanıyla hesaplar.',kalip='şekilli',
 kart='K-AKS-07 (halka dilimi) · 1 ≤ |z| ≤ 3, y = ±x doğruları arasındaki bölge; alan 2π',
 metin='Şekilde, karmaşık düzlemde merkezi orijin olan iki çember ile orijinden geçen turuncu renkli iki kesikli doğru çizilmiştir. Taralı bölge, çemberler arasında kalan ve iki doğru arasındaki, 2i sayısının görüntüsünü içeren (üstteki) dilimdir; sınır çizgileri bölgeye dahildir.\nBuna göre taralı bölgenin alanı kaç birim karedir?',
 dogru='2π',yan=[('π/4','Yalnız iç çemberin (yarıçap 1) dörtte birini almış: π · 1²/4.','dikkat'),('π','Çember yarıçaplarının farkının karesinin dörtte biri olarak (3 − 1)² · π/4 hesaplamış.','islem'),('9π/4','İç çemberin deliğini düşünmeyip dış çemberin dörtte birini (π · 3²/4) almış.','dikkat'),('4π','İki doğru arasındaki açıyı 180° (yarım halka) alıp π(9 − 1)/2 bulmuş.','bilgi')],
 sira=['π/4','π','2π','9π/4','4π'],istenen='Taralı bölgenin alanı.',ip=['Taralı bölgenin hangi merkez açıya karşılık geldiğini doğruların eğimlerinden bul.'],bilgi=[YER],sekil=SK,
 ad=[A('Açıyı bul','y = x ve y = −x doğruları x ekseniyle 45° ve 135° yapar; aralarındaki açı 90°’dir.','135° − 45° = 90°'),A('Çemberleri oku','Yarıçaplar eksen üzerindeki işaretlerden 1 ve 3 okunur.','r₁ = 1, r₂ = 3'),A('Halka alanını yaz','Tam halkanın alanı π(r₂² − r₁²)’dir.','π(9 − 1) = 8π'),A('Dilimi al','90°, tam açının dörtte biridir.','8π/4 = 2π')],
 puf='Halka dilimi alanı = (açı/360°) · π(R² − r²).')

# ================= 17 zor · düz · gerçel katsayılı polinom =================
xs_=sp.symbols('x'); Pp=sp.expand((xs_-3)*(xs_**2-2*xs_+5)); assert Pp==xs_**3-5*xs_**2+11*xs_-15
assert sp.expand(Pp.subs(xs_,1+2*sp.I))==0 and Pp.subs(xs_,0)==-15; v=int(Pp.subs(xs_,2)); assert v==-5
e_a=(2+3)*(4-4+5); e_b=(4-4+5); e_c=(2-3)*(4-4+3); e_d=(2-3)*(4-4-3)
assert [e_a,e_b,e_c,e_d]==[25,5,-3,3] and len({v,e_a,e_b,e_c,e_d})==5
q('0017',tipId='kk-ikinci',tip='İkinci derece denklemin karmaşık kökleri',z='zor',alt='Gerçel Katsayılı Polinom',kaz='Gerçel katsayılı polinomun karmaşık kökünün eşleniğinin de kök olduğunu kullanarak polinomu belirler ve değerini hesaplar.',kalip='düz',
 kart='K-AKS-06 (eşlenik kök teoremi) · P(x) = x³ + ax² + bx + c, P(1 + 2i) = 0, P(0) = −15; P(2)',
 metin='a, b ve c gerçel sayılar olmak üzere P(x) = x³ + ax² + bx + c polinomu için P(1 + 2i) = 0 ve P(0) = −15’tir.\nBuna göre P(2) değeri kaçtır?',
 dogru=v,yan=[(e_a,'Kökler çarpımını c’ye eşitleyip gerçel kökü −3 bulmuş: P(2) = (2 + 3)(4 − 4 + 5) = 25.','bilgi'),(e_b,'Gerçel kök çarpanını (x − 3) yazmayı unutup yalnız x² − 2x + 5 ifadesinin değerini almış: 5.','dikkat'),(e_c,'İki kökün çarpımını 5 yerine gerçel ve sanal kısımlarını toplayarak 3 bulmuş: P(2) = (−1)(3) = −3.','islem'),(e_d,'İkinci çarpanda i² = +1 alıp x² − 2x − 3 bulmuş: P(2) = (−1)(−3) = 3.','bilgi')],
 istenen='P(2) değeri.',ip=['Katsayılar gerçelse köklerin bir özelliği var; bunun sonucunda verilen kök tek başına kalmaz.'],bilgi=[IKI],
 ad=[A('Eşlenik kökü ekle','Gerçel katsayılı polinomda 1 + 2i kökse eşleniği 1 − 2i de köktür.','kökler: 1 + 2i, 1 − 2i, r'),A('Çarpanı kur','İki eşlenik kökün çarpanı gerçel katsayılı ikinci derece ifadedir.','(x − 1)² + 4 = x² − 2x + 5'),A('Gerçel kökü bul','P(x) = (x − r)(x² − 2x + 5) ve P(0) = −15’tir.','−5r = −15 → r = 3'),A('P(2)’yi hesapla','Çarpanlar x = 2 için hesaplanır.','P(2) = (2 − 3)(4 − 4 + 5) = −5')],
 puf='Gerçel katsayılı polinomda karmaşık kökler eşlenikleriyle çift gelir.')

# ================= 18 zor · şekil · çember üzerinde uzaklık =================
cc,rr=(0,3),2; Pn_=(4,0); dd=abs(complex(*cc)-complex(*Pn_)); assert abs(dd-5)<1e-9
mn,mx=dd-rr,dd+rr; assert (mn,mx)==(3,7); v=int(mn*mx); assert v==21
e=[5,10,25,35]; assert [round(dd),round(mn+mx),round(dd**2),round(dd*mx)]==e and len({v,*e})==5
# tarama: çember üzerindeki noktalarla en küçük ve en büyük uzaklık
ds=[abs(complex(0,3)+2*cmath.exp(1j*t*math.pi/1800)-4) for t in range(3600)]; assert abs(min(ds)-3)<1e-3 and abs(max(ds)-7)<1e-3
ust=f'\\fill[blue!15] ({cc[0]*SC:.3f},{cc[1]*SC:.3f}) circle ({rr*SC:.3f});'
body=f'\\draw[{BL},line width=1.8pt] ({cc[0]*SC:.3f},{cc[1]*SC:.3f}) circle ({rr*SC:.3f}); \\fill[{BL}] ({cc[0]*SC:.3f},{cc[1]*SC:.3f}) circle (0.08);'+nok(*Pn_,'P',OR,'above right')
SK=fig(arg(-3,6,-2,6,ust=ust,govde=body))
q('0018',tipId='kk-yer',tip='Geometrik yer ve bölge',z='orta',alt='Çember Üzerinde Uzaklık',kaz='Çember üzerindeki noktaların sabit bir noktaya en küçük ve en büyük uzaklığını merkez uzaklığından bulup çarpar.',kalip='şekilli',
 kart='K-AKS-07 (çember ve nokta) · merkez 3i, r = 2, P(4, 0); en küçük × en büyük uzaklık',
 metin='Bir drone, karmaşık düzlemde şekildeki çember üzerinde dolanıyor; drone’un konumu z karmaşık sayısıyla gösterilmektedir. Kontrol merkezi P noktasındadır ve P noktası 4 sayısının görüntüsüdür.\nDrone ile kontrol merkezi arasındaki uzaklık |z − 4| ile ölçüldüğüne göre bu uzaklığın alabileceği en küçük değer ile en büyük değerin çarpımı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız merkezden P’ye olan uzaklığı (5) bulup onu yazmış.','dikkat'),(e[1],'En küçük ve en büyük uzaklıkları (3 ve 7) doğru bulmuş fakat çarpım yerine toplamlarını (10) yazmış.','dikkat'),(e[2],'Merkezden P’ye uzaklığın karesini (25) çarpım sanmış.','bilgi'),(e[3],'En küçük uzaklık yerine merkez uzaklığını (5) alıp en büyük uzaklıkla (7) çarpmış.','bilgi')],
 istenen='|z − 4| uzaklığının en küçük ve en büyük değerlerinin çarpımı.',ip=['P noktasını çemberin merkezine bağlayan doğru üzerinde, çembere en yakın ve en uzak noktaları düşün.'],bilgi=[MOD,YER],sekil=SK,
 ad=[A('Merkezi ve yarıçapı oku','Çember 3i merkezli, yarıçapı 2’dir.','merkez = 3i · r = 2'),A('P’ye uzaklığı bul','Merkez (0, 3), P (4, 0) olduğundan uzaklık 3-4-5 üçgeninin hipotenüsüdür.','d = √(16 + 9) = 5'),A('Uç değerleri bul','En yakın nokta merkez uzaklığından yarıçap kadar azdır, en uzak nokta yarıçap kadar fazladır.','en küçük = 5 − 2 = 3 · en büyük = 5 + 2 = 7'),A('Çarp','İki uç değer çarpılır.','3 × 7 = 21')],
 puf='Bir noktanın çembere en küçük ve en büyük uzaklığı merkez uzaklığından yarıçap çıkarılıp eklenerek bulunur.')

# ================= 19 zor · şekil · kare köşesi =================
A19,C19=(-1,1),(5,3); zA19,zC19=complex(*A19),complex(*C19); M19=(zA19+zC19)/2; assert eq(M19,2,2)
B19=M19+1j*(zA19-M19); D19=M19-1j*(zA19-M19); assert eq(B19,3,-1) and eq(D19,1,5)
assert abs(abs(B19-zA19)-abs(B19-zC19))<1e-9 and abs(((B19-M19)*(zA19-M19).conjugate()).real)<1e-9
cr=lambda p,q_:(p.conjugate()*q_).imag
assert cr(B19-zA19,zC19-B19)>0 and cr(zC19-B19,D19-zC19)>0     # A,B,C,D saat yönünün tersine
v=cs(B19); w1=cs(D19); w2=cs(1j*zA19); w3=cs(1j*(zA19-M19)); w4=cs(zA19+1j*(zC19-zA19))
assert (v,w1,w2,w3,w4)==('3 − i','1 + 5i',M+'1 − i','1 − 3i',M+'3 + 7i') and len({v,w1,w2,w3,w4})==5
body='\\draw[dashed,'+BL+',thick] (%.2f,%.2f) -- (%.2f,%.2f);'%(A19[0]*SC,A19[1]*SC,C19[0]*SC,C19[1]*SC)+nok(*A19,'A',BL,'above left')+nok(*C19,'C',OR,'above right')
SK=fig(arg(-2,6,-2,6,govde=body))
q('0019',tipId='kk-donme',tip='Döndürme ile köşe bulma',z='zor',alt='Kare Köşesi',kaz='Karşılıklı iki köşesi verilen karenin diğer köşesini merkez etrafında 90° döndürerek karmaşık sayı olarak bulur.',kalip='şekilli',
 kart='K-AKS-08 (kare köşegeni) · A(−1, 1), C(5, 3); B = M + i(A − M)',
 metin='Bir peyzaj tasarımcısı, karmaşık düzlemde ABCD karesi biçiminde bir havuz planlıyor; köşeler A, B, C, D sırasıyla saat yönünün tersine dizilmiştir. Şekilde, havuzun karşılıklı A ve C köşeleri verilmiştir.\nBuna göre B köşesinin görüntüsü olan karmaşık sayı aşağıdakilerden hangisidir?',
 dogru=v,yan=[(w1,'Saat yönünün tersi yerine saat yönünde döndürüp (−i ile çarpıp) B yerine D köşesini bulmuş.','dikkat'),(w2,'A sayısını orijin etrafında i ile çarpmış: i(−1 + i) = −1 − i; karenin merkezini kullanmamış.','bilgi'),(w3,'Merkezden A’ya giden vektörü i ile döndürüp merkezi eklemeyi unutmuş: i(−3 − i) = 1 − 3i.','dikkat'),(w4,'Merkez yerine A köşesi etrafında AC vektörünü döndürmüş: A + i(C − A).','bilgi')],
 sira=['1 + 5i',M+'1 − i','1 − 3i',M+'3 + 7i','3 − i'],istenen='B köşesinin görüntüsü olan karmaşık sayı.',ip=['Köşegenler hakkında bildiklerini sayılara dök.'],bilgi=[DON,DUZ],sekil=SK,
 ad=[A('Merkezi bul','Köşegenlerin orta noktası karenin merkezidir.','M = (−1 + i + 5 + 3i)/2 = 2 + 2i'),A('Vektörü yaz','Merkezden A’ya giden vektör bulunur.','A − M = −3 − i'),A('Döndür','Köşeler saat yönünün tersine dizili olduğundan A’dan B’ye 90° saat yönünün tersine dönülür.','i(−3 − i) = 1 − 3i'),A('Merkezi ekle','Dönmüş vektör merkeze eklenir.','B = (2 + 2i) + (1 − 3i) = 3 − i')],
 puf='Bir noktayı bir merkez etrafında 90° döndürmek için merkezden farkı i ile çarpıp merkezi tekrar ekle.')

# ================= 20 zor · öncüllü · z + 1/z = 1 =================
zr=cmath.rect(1,math.pi/3); assert abs(zr+1/zr-1)<1e-12 and abs(zr.imag)>0.1
Y1=abs(zr**3+1)<1e-9; Y2=abs(zr**2025-1)<1e-9; Y3=abs(zr**2026-zr**2)<1e-9
assert (Y1,Y2,Y3)==(True,False,False) and abs(zr**2025+1)<1e-9 and abs(zr**2026+zr)<1e-9
q('0020',tipId='kk-kuvvet',tip='i’nin kuvvetleri ve üslü ifade',z='zor',alt='Büyük Kuvvet ve Periyot',kaz='z + 1/z = 1 koşulundan z³ = −1 özelliğini çıkarıp büyük üslerin değerini periyotla belirler.',kalip='öncüllü',
 kart='K-AKS-01 (z + 1/z = 1) · z³ = −1, z⁶ = 1; z²⁰²⁵ = −1, z²⁰²⁶ = −z',
 metin='z, gerçel sayı olmayan bir karmaşık sayı olmak üzere z + 1/z = 1 eşitliği sağlanmaktadır.\nBuna göre,\nI. z³ = −1\nII. z²⁰²⁵ = 1\nIII. z²⁰²⁶ = z²\nyargılarından hangileri doğrudur?',
 dogru='Yalnız I',yan=[('Yalnız II','z³ = 1 sanıp I’i yanlış, II’yi doğru bulmuş; III’te z²⁰²⁶ = z çıktığından z²’yi yanlış saymış.','bilgi'),('I ve II','z³ = −1’i doğru bulmuş; (−1)⁶⁷⁵ = +1 sanıp II’yi doğru saymış, III’te z²⁰²⁶ = z çıktığından z²’yi yanlış bulmuş.','islem'),('I ve III','z³ = −1’i doğru bulmuş; kuvvetleri i’nin kuvvetleri gibi 4’e göre indirgeyip z²⁰²⁵ = z, z²⁰²⁶ = z² bulmuş: II’yi yanlış, III’ü doğru saymış.','bilgi'),('I, II ve III','z³ = −1’i bulduktan sonra yargıları kuvvet döngüsünü incelemeden hepsini doğru saymış.','dikkat')],
 sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],istenen='Doğru olan yargılar.',ip=['Eşitliği kök biçimine getirip z’nin hangi küçük üssünün sade bir değer aldığını bul.'],bilgi=[IKB],
 ad=[A('Denklemi kur','Eşitliğin iki tarafı z ile çarpılır.','z² + 1 = z → z² − z + 1 = 0'),A('Küp özdeşliğini kullan','(z + 1)(z² − z + 1) = z³ + 1 olduğundan z³ + 1 = 0 bulunur.','z³ = −1 → I doğru'),A('II’yi incele','2025 = 3 × 675 olduğundan z²⁰²⁵ = (z³)⁶⁷⁵ olur.','(−1)⁶⁷⁵ = −1 → II yanlış'),A('III’ü incele','z²⁰²⁶ = z²⁰²⁵ · z olduğundan sonuç −z’dir; z² = z − 1 ise −z’ye eşit değildir.','z²⁰²⁶ = −z ≠ z² → III yanlış')],
 puf='z² − z + 1 = 0 ise z³ = −1 ve z⁶ = 1’dir; büyük üsleri 6’ya (ya da 3’e) göre indir.')

# ---------- çıktı ----------
def bitir_ayt(P,onek,k):
    HV=os.path.join(MYD,'..')
    for q_ in P.ANA: q_['kardes']=None
    json.dump(P.ANA,open(os.path.join(MYD,f'{onek}-1.json'),'w'),ensure_ascii=False,indent=1)
    from collections import Counter
    print(len(P.ANA),'ana · harfler',dict(sorted(Counter(q_['cevap']['sik'] for q_ in P.ANA).items())),'· zorluk',dict(Counter(q_['zorluk'] for q_ in P.ANA)),'· şekilli',sum(1 for q_ in P.ANA if q_['sekil']))
    print([q_['cevap']['sik'] for q_ in P.ANA])
    tipler={}
    for c_ in H.KARTLAR: tipler.setdefault(c_['tipId'],dict(tipId=c_['tipId'],ad=c_['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c_['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın denemeleri (yalnız mantık), MEB 11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
bitir_ayt(P,'karmasik',UK)
