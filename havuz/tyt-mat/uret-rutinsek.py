"""Rutin Olmayan Problemler · ŞEKİLLİ paket (10 soru): şekil/tablo veri taşır; her doğru ve çeldirici değer kodla (tarama/DP/BFS) doğrulanır. Kardeş yok, ipucu 1."""
import sys,os,math,itertools,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from collections import deque
H.KONU='Rutin Olmayan Problemler'
UK='prob|Rutin Olmayan Problemleri'
P=Parti('rutinsek','Rutin Olmayan Problemler',UK)
KY='ÖSYM 2018–2026 TYT Matematik (rutin olmayan problemler; şekilli/tablolu örüntü, sayma, mantık soruları; yalnız mantık) · MEB 9. sınıf'
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

ORU=B('Şekil örüntüsü','Adımlar arasındaki artış sabitse n. adımdaki parça sayısı, artış ve ilk adım kullanılarak yazılır. Örnek: her adımda 4 çöp artan, ilk adımı 6 çöp olan bir dizilimde n. adım 4n + 2 çöptür')
YOL=B('Izgarada yol sayma','Her kavşağa gelen yol sayısı, o kavşağa girebilen komşu kavşakların yol sayıları toplanarak bulunur; kapalı yollar toplama katılmaz. Örnek: yalnız sağa ve yukarı gidilen 2 × 2 karelik ızgarada kavşak değerleri 1, 1, 1 / 1, 2, 3 / 1, 3, 6 biçiminde dolar')
ELE=B('Eleme ağacı','Eleme usulünde her maçı kazanan bir üst tura çıkar; bir takımın oynadığı maçlar, ağaçta yukarı doğru izlenen yol üzerindeki karşılaşmalardır. Örnek: 4 takımlı turnuvada şampiyon 2 maç yapar')
TAK=B('Takvim ve periyot','Haftanın günleri 7 günde bir tekrar eder; iki düzen birlikte yinelenecekse ortak yinelenme süresi, iki periyodun ortak katıdır. Örnek: 3 günde bir ve haftalık düzenler 21 günde bir çakışır')
KOD=B('Şifre bulma','Her ipucu, olası şifreleri eler; ipuçları tek tek şifreyle karşılaştırılıp çelişen adaylar atılır. Örnek: “doğru yerde 0” ipucu, o denemedeki her rakamın o basamakta bulunmadığını söyler')
KUP=B('Yığılmış küpler','Bir küpün bir yüzü, başka bir küple ya da zeminle temas ediyorsa dışarıya açık değildir; açık yüzler yönlere göre (üst, ön, arka, sağ, sol) ayrı ayrı sayılabilir. Örnek: tek bir küpün zemin hariç 5 yüzü açıktır')
KES=B('Kesişen kesim çizgileri','Her yeni kesim, onu daha önce kesen çizgilerin sayısının bir fazlası kadar parçayı ikiye böler. Örnek: bir dikdörtgeni önce bir çizgiyle (2 parça), sonra ilkini 1 yerde kesen ikinci çizgiyle keserseniz 4 parça olur')
SIR=B('Koşullu yerleştirme','Her koşul, bir kişinin olası yerlerini daraltır; kesin yeri belli olan kişiden başlayıp diğerleri sırayla yerleştirilir. Örnek: “A, B’nin hemen arkasında” ise A’nın yeri, B’nin yerinden bir sıra aşağıdadır')
TER=B('Terazi denklemleri','Dengede olan terazide iki kefenin ağırlıkları eşittir; bir cismin ağırlığı başka bir cisim cinsinden yazılıp yerine konabilir. Örnek: 2 elma = 3 armut ve 1 armut = 2 kiraz ise 2 elma = 6 kirazdır')
KUT=B('Komşu aktarmalar','Yalnız yan yana kutular arasında aktarma yapılıyorsa uzaktaki fazlalık, ara kutulardan geçerek taşınır; her komşu kutu çiftinden geçmesi gereken topların toplamı gereken hamleyi belirler. Örnek: 3 kutuda 4, 0, 2 top varsa her kutuda 2 top için 2 + 2 = 4 hamle gerekir')

# ---------- kartlar ----------
kartla('K-RTS-01','Şekil örüntüsü (kibrit üçgenleri)','Şekildeki ilk adımlardan çöp sayısının her adımda sabit arttığı görülür; n. adımdaki çöp sayısı yazılıp eldeki çöp sayısına göre en büyük n bulunur.','Çöp sayısını 3n sanmak; ortak kenarı iki kez saymak; kalan çöpü hesaba katmamak.','kolay','hikâyeli',3,'rts-oruntu','Kibrit çöpü örüntüsü')
kartla('K-RTS-02','Kapalı yollu ızgara','Her kavşağa gelen yol sayısı, solundaki ve altındaki kavşakların toplamıdır; kapalı yol toplamaya katılmaz.','Kapalı yolu hiç hesaba katmamak; yalnız bir kapalı yolu çıkarmak; iki kez çıkarmak.','orta','hikâyeli',5,'rts-yol','Kapalı yollu ızgarada yol sayma')
kartla('K-RTS-03','Eleme ağacı','Puanı büyük olan kazanır; şampiyonun karşılaştığı takımlar ağaçta yukarı doğru izlenerek bulunur.','Yenilen takımları değil bütün takımları toplamak; yarı finaldeki rakibi yanlış belirlemek.','kolay','hikâyeli',4,'rts-turnuva','Eleme ağacı ve maç eşleşmeleri')
kartla('K-RTS-04','Takvim yaprağı ve düzenli nöbet','Takvimden ayın ilk günü ve nöbet aralığı okunur; nöbet günleri ile haftanın günü aynı anda taranır.','Yalnız bir koşulu hesaba katmak; ilk çakışmayı son sanmak; sayı yerine tarih toplamak istenenini karıştırmak.','orta','hikâyeli',4,'rts-takvim','Takvim yaprağında periyot')
kartla('K-RTS-05','İpuçlu şifre tablosu','Her deneme satırı, rakam ve yer bilgisiyle adayları eler; bütün satırlara uyan tek şifre kalır.','Bir satırı hesaba katmamak; “yanlış yerde” bilgisini “şifrede yok” sanmak.','zor','yeni nesil',5,'rts-sifre','İpuçlu şifre bulma')
kartla('K-RTS-06','Yığılmış küpler','Şekildeki sütun yükseklikleri okunur; zemin hariç dışa bakan yüzler yönlere göre sayılır, görünmeyen arka yüzler de unutulmaz.','Yalnız görünen yüzleri saymak; tabanı da saymak; arka yüzleri simetriden varsaymak.','zor','yeni nesil',5,'rts-kup','Yığılmış küplerde boyalı yüz sayma')
kartla('K-RTS-07','Kesim çizgileri ve parça sayısı','Parça sayısı = 1 + kesim sayısı + kesim çizgilerinin kâğıdın içinde kesiştiği nokta sayısı.','Her kesimde parçaların ikiye katlandığını sanmak; yalnız çizgi sayısına bakmak.','kolay','hikâyeli',3,'rts-kesim','Kesilen kâğıtta parça sayma')
kartla('K-RTS-08','Oturma planı','Planın düzeni (sıra, sütun, koridor) şekilden okunur; koşullar sırayla uygulanıp herkesin yeri belirlenir.','Koridorun iki yanını yan yana saymak; “hemen arkasında” koşulunu yanlış yöne uygulamak.','zor','hikâyeli',5,'rts-oturma','Planda koşullu yerleştirme')
kartla('K-RTS-09','Terazi denklemleri','Dengelenen iki terazi, cisimlerin ağırlıkları arasında oran verir; üçüncü kefedeki cisimler bir cins cinsinden yazılır.','Oranı ters kurmak; bir kefedeki cismin sayısını unutmak.','orta','yeni nesil',4,'rts-terazi','Dengede teraziler')
kartla('K-RTS-10','Kutu ve top aktarma','Her kutudaki fazla ya da eksik top sayısı ortalamaya göre bulunur; komşu kutular arası geçişte biriken fark hamle sayısını verir.','Yalnız fazlaların toplamını almak; komşu olmayan kutular arasında doğrudan aktarmayı serbest sanmak.','orta','hikâyeli',4,'rts-kutu','Komşu kutular arasında aktarma')

# ================= 01 kolay · kibrit üçgenleri =================
sc=1.0; h=0.866*sc
def uc_cubuk(n): return 2*n+1
o=[]; x0s=[0,2.4,5.2]
for n,x0 in zip((1,2,3),x0s):
    pts=[(x0+0.5*sc*j,0 if j%2==0 else h) for j in range(n+2)]
    for j in range(n+1): o.append(f'\\draw[line width=2.2pt] ({pts[j][0]:.3f},{pts[j][1]:.3f}) -- ({pts[j+1][0]:.3f},{pts[j+1][1]:.3f});')
    for j in range(n): o.append(f'\\draw[line width=2.2pt] ({pts[j][0]:.3f},{pts[j][1]:.3f}) -- ({pts[j+2][0]:.3f},{pts[j+2][1]:.3f});')
    o.append(f'\\node[below=5pt] at ({x0+0.25*sc*(n+1):.3f},0) {{{n}. adım}};')
o.append('\\node at (7.7,0.43) {$\\cdots$};')
assert [uc_cubuk(n) for n in (1,2,3)]==[3,5,7]
SK=fig('\n'.join(o))
tot=90; n=(tot-1)//2; v=n; kal=tot-uc_cubuk(n)
e=[tot//3,tot//2,(tot-3)//2,uc_cubuk(n)]
assert v==44 and kal==1 and e==[30,45,43,89] and len({v,*e})==5
q('0001',tipId='rts-oruntu',tip='Kibrit çöpü örüntüsü',z='kolay',alt='Kibrit Örüntüsü',kaz='Şekil örüntüsünden n. adımdaki çöp sayısını yazar ve eldeki çöpe göre en büyük adımı bulur.',kalip='hikâyeli',
 kart='K-RTS-01 (kibrit üçgenleri) · 3, 5, 7 çöp; 90 çöp',
 metin='Teknoloji tasarım dersinde Bora, kibrit çöplerini ucundan ucuna ekleyerek yan yana üçgenlerden oluşan bir şerit yapıyor. Şekilde bu şeridin ilk üç adımı gösterilmiştir; her adımda şeride bir üçgen daha eklenmekte ve komşu üçgenler ortak çöpü paylaşmaktadır. Bora’nın elinde 90 kibrit çöpü vardır ve çöpleri bölmeden kullanacaktır.\nBuna göre, Bora bu örüntüyü sürdürerek en çok kaç üçgenli şerit yapabilir?',
 dogru=v,yan=[(e[0],'Her üçgen için ayrı 3 çöp harcandığını sanmış: 90 ÷ 3.','dikkat'),(e[1],'Çöp sayısını 2n almış, ortak kenar nedeniyle gelen 1 çöpü eklememiş: 90 ÷ 2.','dikkat'),(e[2],'İlk üçgeni toplama katmayıp 3 + 2n ≤ 90 koşulundan n = 43 bulmuş.','islem'),(e[3],'44 üçgenli şeridin kullandığı gerçek çöp sayısını (89) üçgen sayısı sanmış.','dikkat')],
 istenen='Yapılabilecek en büyük üçgen sayısı.',ip=['Şekildeki üç adımın çöp sayılarını yazıp her adımda çöp sayısının nasıl değiştiğine bak.'],bilgi=[ORU],sekil=SK,
 ad=[A('Çöp sayılarını oku','Şekildeki adımlar sayılır.','1. adım 3, 2. adım 5, 3. adım 7 çöp'),A('Kuralı yaz','Her adımda 2 çöp artar; n. adım için çöp sayısı 2n + 1’dir.','Ç(n) = 2n + 1'),A('Eşitsizliği çöz','Elindeki çöp sayısı yetmelidir.','2n + 1 ≤ 90 → n ≤ 44,5'),A('En büyük n','n tam sayı olmalıdır.','n = 44 (89 çöp, 1 çöp artar)')],
 puf='Her adım 2 çöp artıyor; ilk adım 3 çöp: n. adım 2n + 1.')

# ================= 02 orta · kapalı yollu ızgara =================
W,Hh=4,3; kapali=[((1,1),(2,1)),((2,1),(2,2))]
def yollar(kap):
    f={(0,0):1}
    for y in range(Hh+1):
        for x in range(W+1):
            if (x,y)==(0,0): continue
            s=0
            if x>0 and ((x-1,y),(x,y)) not in kap: s+=f[(x-1,y)]
            if y>0 and ((x,y-1),(x,y)) not in kap: s+=f[(x,y-1)]
            f[(x,y)]=s
    return f[(W,Hh)]
tamam=yollar([]); k1=yollar([kapali[0]]); k2=yollar([kapali[1]]); v=yollar(kapali)
# bir kapalı yoldan geçen yol sayıları (dogrudan sayim) ve ikisinden geçen
def gec(e):
    (a,b)=e
    return yollar([])-yollar([e])
g1,g2=gec(kapali[0]),gec(kapali[1])
e=[tamam,g2,tamam-g2,tamam-g1-g2]
assert tamam==35 and v==(tamam-g1-g2+(g1+g2-(tamam-v))) and len({v,*e})==5,(tamam,g1,g2,v,e)
o=[];s=1.15
for y in range(Hh+1):
    for x in range(W):
        if ((x,y),(x+1,y)) not in kapali: o.append(f'\\draw[line width=1.6pt] ({x*s},{y*s}) -- ({(x+1)*s},{y*s});')
for x in range(W+1):
    for y in range(Hh):
        if ((x,y),(x,y+1)) not in kapali: o.append(f'\\draw[line width=1.6pt] ({x*s},{y*s}) -- ({x*s},{(y+1)*s});')
for (a,b) in kapali:
    o.append(f'\\draw[dashed,thin] ({a[0]*s},{a[1]*s}) -- ({b[0]*s},{b[1]*s}); \\node[fill=white,inner sep=1.5pt] at ({(a[0]+b[0])*s/2},{(a[1]+b[1])*s/2}) {{$\\times$}};')
for y in range(Hh+1):
    for x in range(W+1): o.append(f'\\fill ({x*s},{y*s}) circle (0.06);')
o.append(f'\\node[below left] at (0,0) {{A}}; \\node[above right] at ({W*s},{Hh*s}) {{B}};')
o.append(f'\\node[anchor=west] at ({W*s+0.9},{Hh*s/2+0.3}) {{$\\times$ : kapalı yol}};')
SK=fig('\n'.join(o))
q('0002',tipId='rts-yol',tip='Kapalı yollu ızgarada yol sayma',z='orta',alt='Izgarada Yol',kaz='Kapalı yolları dikkate alarak ızgarada en kısa yol sayısını bulur.',kalip='hikâyeli',
 kart='K-RTS-02 (kapalı yollu ızgara) · 4 doğu, 3 kuzey; iki kapalı yol',
 metin='Bir mahallede sokaklar şekildeki gibi birbirini dik kesmektedir; kesikli çizgiyle gösterilen iki sokak yol çalışması nedeniyle trafiğe kapatılmıştır. A noktasından çıkan bir kurye, paketi B noktasına götürürken her adımda yalnızca doğuya (sağa) ya da kuzeye (yukarı) gitmekte ve yalnızca açık sokakları kullanmaktadır.\nBuna göre, kurye A’dan B’ye kaç farklı yoldan gidebilir?',
 dogru=v,yan=[(e[0],'Kapalı yolları hiç hesaba katmamış: C(7, 3).','dikkat'),(e[1],'İkinci kapalı yoldan geçen yolların sayısını, yani çıkarılması gerekeni cevap sanmış.','dikkat'),(e[2],'Yalnız ikinci kapalı yolu (dikey) hesaba katıp ondan geçen yolları çıkarmış.','dikkat'),(e[3],'İki kapalı yoldan geçen yolları ayrı ayrı çıkarmış; ikisinden birden geçenleri iki kez çıkarmış.','islem')],
 istenen='A’dan B’ye gidebilecek farklı yol sayısı.',ip=['Her kavşağa kaç farklı yoldan gelinebileceğini A’dan başlayarak sırayla yaz.'],bilgi=[YOL],sekil=SK,
 ad=[A('Tüm yollar','Kapalılar yokmuş gibi 4 doğu, 3 kuzey adımı sıralanır.','C(7, 3) = 35'),A('Birinci kapalı yol','Bu yoldan geçen yollar A’dan o yola gelişlerin, yoldan sonra B’ye gidişlerle çarpımıdır.',f'{g1} yol'),A('İkinci kapalı yol','Aynı biçimde sayılır.',f'{g2} yol'),A('İkisini birlikte çıkar','İkisinden birden geçenler iki kez çıkarıldığı için bir kez geri eklenir; kavşak kavşak sayımla da doğrulanır.',f'{tamam} − {g1} − {g2} + {g1+g2-(tamam-v)} = {v}')],
 puf='Kavşak kavşak ilerle: her kavşakta solundaki ve altındaki kavşağın yol sayısını topla.')

# ================= 03 kolay · eleme ağacı =================
tk=[('Kartal',64),('Yıldız',52),('Şimşek',71),('Bulut',48),('Fırtına',57),('Aslan',80),('Kaplan',39),('Yavuz',66)]
def mac(a,b): return a if a[1]>b[1] else b
r1=[mac(tk[0],tk[1]),mac(tk[2],tk[3]),mac(tk[4],tk[5]),mac(tk[6],tk[7])]
r2=[mac(r1[0],r1[1]),mac(r1[2],r1[3])]; sam=mac(r2[0],r2[1])
assert sam==('Aslan',80)
yenilen=[tk[4][1],mac(r1[2],r1[3])==r1[2] and r1[3][1],r2[0][1]]
# Aslan: 1. tur Fırtına(57), yarı final Yavuz(66), final Şimşek(71)
yen=[57,66,71]; assert yen==[tk[4][1],r1[3][1],r2[0][1]]; v=sum(yen)
e=[yen[1]+yen[2],tk[4][1]+tk[6][1]+yen[2],v+80,yen[0]+yen[1]]
assert v==194 and e==[137,167,274,123] and len({v,*e})==5
o=[];ys=[7-0.8*i for i in range(8)];
for i,(nm,pt) in enumerate(tk): o.append(f'\\node[anchor=east] at (0,{ys[i]:.2f}) {{{nm}\\ \\textbf{{{pt}}}}};')
cur=ys; x=0
for tur in range(3):
    nx=x+1.5; yeni=[]
    for i in range(0,len(cur),2):
        a,b=cur[i],cur[i+1]; m=(a+b)/2
        o.append(f'\\draw ({x},{a:.2f}) -- ({nx},{a:.2f}) -- ({nx},{b:.2f}) -- ({x},{b:.2f});'); yeni.append(m)
    cur=yeni; x=nx
o.append(f'\\draw ({x},{cur[0]:.2f}) -- ({x+0.6},{cur[0]:.2f});')
o.append(f'\\node[above] at (-1.2,7.35) {{Takım\\ \\ \\textbf{{güç puanı}}}};')
SK=fig('\n'.join(o))
q('0003',tipId='rts-turnuva',tip='Eleme ağacı ve maç eşleşmeleri',z='kolay',alt='Eleme Turnuvası',kaz='Eleme ağacında şampiyonun yendiği takımları belirleyip güç puanlarını toplar.',kalip='hikâyeli',
 kart='K-RTS-03 (eleme ağacı) · 8 takım; şampiyon Aslan',
 metin='Bir okul bahçesinde düzenlenen 8 takımlı eleme turnuvasında eşleşmeler şekildeki gibidir; her maçta güç puanı büyük olan takım kazanmakta, kazanan bir üst tura çıkmakta ve maçlar berabere bitmemektedir. Takımların güç puanları hiçbir maçta değişmemektedir.\nBuna göre, şampiyon olan takımın turnuva boyunca yendiği takımların güç puanları toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Şampiyonun ilk turdaki rakibini (57) hesaba katmamış: 66 + 71.','dikkat'),(e[1],'Yarı finaldeki rakip yerine, o yarı finalde yer alan diğer ilk tur maçının yenileni Kaplan’ı (39) almış: 57 + 39 + 71.','dikkat'),(e[2],'Yendiği takımların toplamına şampiyonun kendi puanını (80) da eklemiş.','dikkat'),(e[3],'Finaldeki rakibi (71) hesaba katmamış: 57 + 66.','dikkat')],
 istenen='Şampiyonun yendiği takımların güç puanları toplamı.',ip=['Her maçın kazananını yukarı doğru ilerleterek bulunuz; şampiyonun hangi takımlarla karşılaştığını izleyiniz.'],bilgi=[ELE],sekil=SK,
 ad=[A('İlk tur','Eşleşmelerde puanı büyük olan geçer: Kartal, Şimşek, Aslan, Yavuz.','4 kazanan'),A('Yarı final ve final','Kartal–Şimşek: Şimşek (71); Aslan–Yavuz: Aslan (80); final Şimşek–Aslan.','Şampiyon Aslan (80)'),A('Aslan’ın rakipleri','Fırtına (57), Yavuz (66), Şimşek (71).','3 rakip'),A('Topla','Puanlar toplanır.','57 + 66 + 71 = 194')],
 puf='Şampiyonun yolunu yukarı izle: her turda tek bir rakibi yenmiştir.')

# ================= 04 orta · takvim =================
gun=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz']; ilk=4; ay=31; nobet0,per=3,4; golge=[3,7,11]
assert [nobet0+per*i for i in range(3)]==golge
pazar=[d for d in range(1,ay+1) if (ilk+d-1)%7==6]
duty=[d for d in range(nobet0,ay+1,per)]
ortak=[d for d in duty if d in pazar]; v=sum(ortak)
p3=[d for d in range(nobet0,ay+1,3) if d in pazar]
e=[ortak[0],ortak[-1],sum(p3),28]
assert pazar==[3,10,17,24,31] and ortak==[3,31] and v==34 and p3==[3,24] and e==[3,31,27,28] and len({v,*e})==5
o=[];cw,ch=0.95,0.72
for j,g in enumerate(gun): o.append(f'\\node[font=\\small\\bfseries] at ({(j+0.5)*cw:.2f},{0.5*ch:.2f}) {{{g}}};')
for d in range(1,ay+1):
    idx=ilk+d-1; r,c=idx//7,idx%7; x,y=c*cw,-r*ch
    fill='fill=vurgu!25,' if d in golge else ''
    o.append(f'\\draw[{fill}thin] ({x:.2f},{y:.2f}) rectangle ({x+cw:.2f},{y-ch:.2f}); \\node at ({x+cw/2:.2f},{y-ch/2:.2f}) {{{d}}};')
o.append(f'\\node[above=8pt] at ({3.5*cw:.2f},{ch:.2f}) {{\\textbf{{Ağustos}}}};')
SK=fig('\n'.join(o))
q('0004',tipId='rts-takvim',tip='Takvim yaprağında periyot',z='orta',alt='Takvim Düzeni',kaz='Takvim yaprağından ayın ilk gününü ve nöbet aralığını okuyup iki düzenin çakıştığı günleri bulur.',kalip='hikâyeli',
 kart='K-RTS-04 (takvim, nöbet) · ayın 1’i Cuma; nöbet 3, 7, 11, …',
 metin='Bir apartman yönetimi, nöbetçi çocukların çizelgesini şekildeki ay takviminde göstermiştir. Gölgeli günler, Ayşe’nin ilk üç nöbet günüdür; nöbet düzeni aynı aralıkla ayın son gününe kadar sürmektedir. Yönetim, Pazar günlerine denk gelen nöbetler için Ayşe’ye ek harçlık verecektir.\nBuna göre, Ayşe’nin Pazar gününe denk gelen nöbet günlerinin tarihleri toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız ilk çakışmayı (3) bulup ayın sonunda yeniden çakışabileceğini düşünmemiş.','dikkat'),(e[1],'Yalnız son çakışmayı (31) yazmış.','dikkat'),(e[2],'Nöbet aralığını 4 yerine 3 gün sanıp 3, 6, 9, … günlerinden Pazar olanları (3 ve 24) toplamış.','dikkat'),(e[3],'İki düzenin ortak yinelenme aralığını (28 gün) tarihler toplamı olarak yazmış.','dikkat')],
 istenen='Pazar günlerine denk gelen nöbet tarihlerinin toplamı.',ip=['Takvimden ayın kaç gün sürdüğünü, ayın ilk gününü ve nöbetler arasındaki gün sayısını belirle.'],bilgi=[TAK],sekil=SK,
 ad=[A('Takvimi oku','Ayın 1’i Cuma, 31 gün; Pazar günleri 3, 10, 17, 24, 31.','Pazarlar: 3, 10, 17, 24, 31'),A('Nöbet aralığı','Gölgeli günler 3, 7, 11: 4 günde bir.','Nöbet: 3, 7, 11, …, 31'),A('Ortak günler','Nöbet günü olan Pazarlar seçilir (3 ve 31).','3 ve 31'),A('Topla','Tarihler toplanır.','3 + 31 = 34')],
 puf='Pazar günleri 7’şer, nöbetler 4’er gün arayla gelir; ikisinin ortak yinelenmesi 28 günde bir olur.')

# ================= 05 zor · ipuçlu şifre =================
def fb(g,c):
    d=sum(a==b for a,b in zip(g,c)); k=len(set(g)&set(c)); return (d,k-d)
tum=[''.join(c) for c in itertools.permutations('0123456789',4)]
sifre='7509'; den=['4139','5836','8542','0529']; geri=[fb(g,sifre) for g in den]
assert geri==[(1,0),(0,1),(1,0),(2,1)]
uyan=[c for c in tum if all(fb(g,c)==f for g,f in zip(den,geri))]; assert uyan==[sifre]
def gevsek(i): return sorted(c for c in tum if c!=sifre and all(fb(g,c)==f for j,(g,f) in enumerate(zip(den,geri)) if j!=i))
random.seed(3); ds=[]
for i in range(4):
    gv=[c for c in gevsek(i) if c<sifre and c not in ds]; assert gv,(i,gevsek(i)); ds.append(random.choice(gv))
assert len(set(ds))==4 and sifre not in ds
SK=tablo_svg(['Deneme','Denenen kod','Doğru yerde','Yanlış yerde'],[[str(i+1),' '.join(g),str(f[0]),str(f[1])] for i,(g,f) in enumerate(zip(den,geri))])
v=sifre; siralama=sorted([sifre]+ds)
q('0005',tipId='rts-sifre',tip='İpuçlu şifre bulma',z='zor',alt='Şifre Bulma',kaz='Deneme tablosundaki ipuçlarını birlikte uygulayarak tek şifreyi bulur.',kalip='yeni nesil',
 kart='K-RTS-05 (ipuçlu şifre) · 4 deneme',
 metin='Rakamları birbirinden farklı olan 4 basamaklı bir şifre (ilk rakamı 0 da olabilir) aşağıdaki kurala göre sınanmıştır: Bir deneme kodunda, şifrede de bulunan rakamlardan şifredeki basamağıyla aynı basamakta olanların sayısı “Doğru yerde”; şifrede bulunup başka basamakta yer alanların sayısı “Yanlış yerde” sütununa yazılır. Dört denemenin sonuçları tabloda verilmiştir.\nBuna göre, şifre aşağıdakilerden hangisidir?',
 dogru=v,yan=[(ds[i],f'{i+1}. denemeyi hesaba katmamış; kalan üç satıra uyan bu kod {i+1}. denemede {fb(den[i],ds[i])[0]} doğru yerde, {fb(den[i],ds[i])[1]} yanlış yerde verir (tabloda {geri[i][0]} ve {geri[i][1]}).','dikkat') for i in range(4)],
 istenen='Şifre.',ip=['Her adayı dört satırın hepsiyle sına; hangi rakamların şifrede olabileceğini satırlar arasında karşılaştırarak daralt.'],bilgi=[KOD],sekil=SK,sira=siralama,
 ad=[A('Satırları oku','Her denemenin “doğru yerde” ve “yanlış yerde” sayıları ayrı bilgidir.','1: (1, 0); 2: (0, 1); 3: (1, 0); 4: (2, 1)'),A('5 rakamını sına','8 şifrede olsaydı 3. satırda 5, 4, 2 elenir, 4. satırda 0, 5, 2, 9’dan üçüne ulaşılamazdı; o hâlde 5 şifrededir, 2. ve 3. satırlar da bunu destekler; 8, 3, 6, 4, 2 şifrede yoktur.','Şifrede 5 var, ikinci basamakta'),A('Diğer rakamlar','4. satırda 0, 5, 2, 9’dan üçü şifrededir; 2 yok, o halde 0, 5, 9 şifrededir. 1. satırda yalnız 9 doğru yerdedir.','9 dördüncü basamakta'),A('Kalan rakamı ve yerleri bul','Kalan tek rakam 7’dir; 4. satırda 0 yanlış yerde olduğundan 7 ve 0, birinci ve üçüncü basamaklara 7 5 0 9 biçiminde yerleşir.','7 5 0 9'),A('Doğrula','Dört satırın tamamı şifre 7509 ile denenir.','Dört satıra da uyar')],
 puf='Önce bir rakamın şifrede olup olmadığını sına; birden çok satırı tek varsayımla çözebilirsin.')

# ================= 06 zor · yığılmış küpler =================
hm=[[1,1,2],[1,2,3],[2,3,3]]   # hm[x][y] : yükseklik; x,y arttıkça (arkaya doğru) azalmayan
for x in range(3):
    for y in range(3):
        if x>0: assert hm[x][y]>=hm[x-1][y]
        if y>0: assert hm[x][y]>=hm[x][y-1]
kup={(x,y,z) for x in range(3) for y in range(3) for z in range(hm[x][y])}
yonler=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1)]  # zemin (0,0,-1) hariç
acik={}
for c in kup:
    for d in yonler:
        n=(c[0]+d[0],c[1]+d[1],c[2]+d[2])
        if n not in kup: acik[(c,d)]=1
toplam=len(acik)
gorunen=sum(1 for (c,d) in acik if d in ((-1,0,0),(0,-1,0),(0,0,1)))
sutun=9; v=toplam; arka=toplam-gorunen
e=[gorunen,toplam+sutun,toplam+arka,gorunen+toplam]
assert len(kup)==18 and gorunen==25 and arka==16 and v==41 and e==[25,50,57,66] and len({v,*e})==5,(len(kup),gorunen,arka,v,e)
c30,s30=0.866,0.5; u=0.8
def pr(x,y,z): return ((x-y)*c30*u,((x+y)*s30+z)*u)
o=[]
for c in sorted(kup,key=lambda c:-(c[0]+c[1]-c[2])):
    x,y,z=c
    def pg(pp,fill):
        return '\\filldraw[fill='+fill+',thick] '+' -- '.join(f'({pr(*p)[0]:.3f},{pr(*p)[1]:.3f})' for p in pp)+' -- cycle;'
    o.append(pg([(x,y,z),(x,y+1,z),(x,y+1,z+1),(x,y,z+1)],'black!8'))
    o.append(pg([(x,y,z),(x+1,y,z),(x+1,y,z+1),(x,y,z+1)],'black!22'))
    o.append(pg([(x,y,z+1),(x+1,y,z+1),(x+1,y+1,z+1),(x,y+1,z+1)],'white'))
    if z==hm[x][y]-1: o.append(f'\\node[font=\\footnotesize\\bfseries] at ({pr(x+.5,y+.5,z+1)[0]:.3f},{pr(x+.5,y+.5,z+1)[1]:.3f}) {{{hm[x][y]}}};')
SK=fig('\n'.join(o))
q('0006',tipId='rts-kup',tip='Yığılmış küplerde boyalı yüz sayma',z='zor',alt='Yığılmış Küpler',kaz='Yığılmış birim küplerde dışa açık yüzleri yönlere göre sayarak boyanacak kare sayısını bulur.',kalip='yeni nesil',
 kart='K-RTS-06 (yığılmış küpler) · yükseklikler 1-1-2 / 1-2-3 / 2-3-3',
 metin='Özdeş birim küplerden, şekilde görünen boşluksuz bir yığın yapılmıştır; her sütunun üst yüzündeki sayı, o sütundaki küp sayısını göstermektedir. Yığın zemin üzerine yerleştirilmiş ve her küp tabandan itibaren üst üste dizilmiştir. Yığının yalnız yere değen yüzleri hariç, bir başka küple temas etmeyen bütün yüzleri (arka ve yan yüzler dâhil) boyanacaktır.\nBuna göre, boyanan birim kare sayısı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız şekilde görünen yüzleri (üst, sol ve sağ) saymış.','dikkat'),(e[1],'Boyanmayan yere değen 9 kareyi de sayıma katmış: 41 + 9.','dikkat'),(e[2],'Arka ve yan gizli yüzleri iki kez saymış: 25 + 16 + 16.','islem'),(e[3],'Görünen yüzleri (25) bir kez daha sayıp toplama eklemiş: 25 + 41.','islem')],
 istenen='Boyanan birim kare sayısı.',ip=['Yığının her sütununun yüksekliğini şekilden oku; görünmeyen yüzleri de yönlere ayırarak say.'],bilgi=[KUP],sekil=SK,
 ad=[A('Yükseklikleri oku','Sütunların üstündeki sayılar toplanır.','Toplam 18 küp'),A('Görünen yüzler','Üst, sol ve sağ yüzler şekilden sayılır.','25 kare'),A('Arka ve yan gizli yüzler','Arkaya ve yana bakan açık yüzler sütun farklarından bulunur.','16 kare'),A('Topla','Görünen ve görünmeyen açık yüzler toplanır.','25 + 16 = 41')],
 puf='Yönlere ayır: üst, sağ, sol, arka, öndeki açık yüzleri ayrı ayrı say.')

# ================= 07 kolay · kesim çizgileri =================
Rw,Rh=6,4
seg=[((0,Fr(7,2)),(6,Fr(1,2))),((0,Fr(1,2)),(6,Fr(7,2))),((2,0),(2,4)),((0,Fr(23,10)),(Fr(16,5),4))]
def kes(a,b):
    (x1,y1),(x2,y2)=a;(x3,y3),(x4,y4)=b
    d=(x2-x1)*(y4-y3)-(y2-y1)*(x4-x3)
    if d==0: return None
    t=Fr((x3-x1)*(y4-y3)-(y3-y1)*(x4-x3),1)/d; s=Fr((x3-x1)*(y2-y1)-(y3-y1)*(x2-x1),1)/d
    if 0<t<1 and 0<s<1: return (x1+t*(x2-x1),y1+t*(y2-y1))
nk=[(i,j,kes(seg[i],seg[j])) for i in range(4) for j in range(i+1,4) if kes(seg[i],seg[j])]
pts=[p for _,_,p in nk]; assert len(set(pts))==len(pts)
I=len(nk); v=1+4+I
# bağımsız doğrulama: örnek noktaların işaret vektörleri
def isr(x,y,sg):
    (x1,y1),(x2,y2)=sg; return (x2-x1)*(y-y1)-(y2-y1)*(x-x1)>0
vec=set()
for i in range(1,600):
    for j in range(1,400):
        x=Fr(i*6,600)+Fr(1,997); y=Fr(j*4,400)+Fr(1,991)
        vec.add(tuple(isr(x,y,sg) for sg in seg))
assert len(vec)==v==10 and I==5,(len(vec),v,I)
e=[1+4+6,1+4+2*I,2**4,4*I]; assert e==[11,15,16,20] and len({v,*e})==5
o=[f'\\draw[thick] (0,0) rectangle ({Rw},{Rh});']
for a,b in seg: o.append(f'\\draw[dashed,line width=1.2pt] ({float(a[0]):.3f},{float(a[1]):.3f}) -- ({float(b[0]):.3f},{float(b[1]):.3f});')
SK=fig('\n'.join(o))
q('0007',tipId='rts-kesim',tip='Kesilen kâğıtta parça sayma',z='kolay',alt='Kesilen Kâğıt',kaz='Kesim çizgilerinin kesiştiği noktaları sayarak parça sayısını bulur.',kalip='hikâyeli',
 kart='K-RTS-07 (kesim çizgileri) · 4 çizgi, 5 kesişme',
 metin='Zeynep, dikdörtgen biçimli bir fon kartonunu, üzerine kalemle çizdiği dört doğrusal kesim çizgisi boyunca makasla kesecektir. Çizgiler şekilde kesikli olarak gösterilmiştir; her çizgi kartonun bir kenarından başlayıp bir başka kenarında bitmektedir ve kesim sırasında parçalar yerinden oynatılmamaktadır.\nBuna göre, bütün çizgiler boyunca kesildiğinde karton kaç parçaya ayrılır?',
 dogru=v,yan=[(e[0],'Her iki çizginin kartonun içinde kesiştiğini sanmış: 1 + 4 + 6.','dikkat'),(e[1],'Her kesişmenin parça sayısını iki artırdığını sanmış: 1 + 4 + 2 · 5.','islem'),(e[2],'Her kesimin parça sayısını iki katına çıkardığını sanmış: 2⁴.','islem'),(e[3],'Çizgi sayısı ile kesişme sayısını çarpmış: 4 × 5.','islem')],
 istenen='Karton parça sayısı.',ip=['Çizgileri tek tek ekle; her yeni çizginin daha önceki çizgileri kartonun içinde kaç noktada kestiğine bak.'],bilgi=[KES],sekil=SK,
 ad=[A('Kesişmeleri say','Çizgi çiftlerinin karton içinde kesiştiği noktalar sayılır.','5 kesişme noktası'),A('Formülü kur','Parça sayısı = 1 + çizgi sayısı + kesişme sayısı.','1 + 4 + 5'),A('Sonuç','Toplama yapılır.','10 parça')],
 puf='Yeni çizgi, her kesiştiği noktadan sonra bir parçayı daha böler.')

# ================= 08 zor · oturma planı =================
ISIM=['Ali','Burcu','Cem','Deniz','Ece','Fatih','Gül','Hakan']; ix={n:i for i,n in enumerate(ISIM)}
def ps(s): return ((s-1)//4,(s-1)%4)
KOS=[
 ('Fatih, Burcu’nun sağındadır; ikisi aynı yatay sıradadır.',lambda s:ps(s[5])[0]==ps(s[1])[0] and ps(s[5])[1]>ps(s[1])[1]),
 ('Burcu, Hakan’ın sağındadır; ikisi aynı yatay sıradadır.',lambda s:ps(s[1])[0]==ps(s[7])[0] and ps(s[1])[1]>ps(s[7])[1]),
 ('Gül, Ali’nin hemen arkasındadır.',lambda s:s[6]==s[0]+4),
 ('Fatih, koridora komşu olan sütunlardan birindedir.',lambda s:ps(s[5])[1] in (1,2)),
 ('Fatih, Deniz’in hemen arkasındadır.',lambda s:s[5]==s[3]+4),
 ('Ece, Cem’in sağındadır; ikisi aynı yatay sıradadır.',lambda s:ps(s[4])[0]==ps(s[2])[0] and ps(s[4])[1]>ps(s[2])[1]),
]
hepsi=list(itertools.permutations(range(1,9)))
cozum=[p for p in hepsi if all(f(p) for _,f in KOS)]
assert len(cozum)==1,len(cozum)
S=cozum[0]; assert dict(zip(ISIM,S))=={'Ali':4,'Burcu':6,'Cem':1,'Deniz':3,'Ece':2,'Fatih':7,'Gül':8,'Hakan':5}
v=S[ix['Ece']]+S[ix['Hakan']]; assert v==7
ds=[]
for i in range(6):
    gv=[p for p in hepsi if all(f(p) for j,(_,f) in enumerate(KOS) if j!=i)]
    ds.append(sorted({p[ix['Ece']]+p[ix['Hakan']] for p in gv if p!=S}-{v}))
sec=[]; kul=set()
for i,l in enumerate(ds):
    for d in l:
        if d not in kul: sec.append((i,d)); kul.add(d); break
assert len(sec)>=4,ds
sec=sec[:4]; e8=[d for _,d in sec]; assert len({v,*e8})==5
o=[];cw,ch=1.0,0.9; gap=1.0
for r in range(2):
    for c in range(4):
        n=r*4+c+1; x=c*cw+(gap if c>=2 else 0); y=-r*ch
        o.append(f'\\draw[thick] ({x:.2f},{y:.2f}) rectangle ({x+cw*0.9:.2f},{y-ch*0.8:.2f}); \\node at ({x+cw*0.45:.2f},{y-ch*0.4:.2f}) {{{n}}};')
W8=4*cw+gap
o.append(f'\\draw[thick,fill=black!10] (0,0.35) rectangle ({W8-0.1:.2f},0.75); \\node at ({(W8-0.1)/2:.2f},0.55) {{Tahta}};')
o.append(f'\\node[rotate=90,font=\\small] at ({2*cw+gap/2-0.05:.2f},{-ch*0.8:.2f}) {{koridor}};')
o.append(f'\\node[rotate=90,font=\\small] at (-0.4,{-ch*0.8:.2f}) {{Pencere}}; \\node[anchor=west,font=\\small] at ({W8+0.1:.2f},{-ch*0.4:.2f}) {{Kapı}}; \\path ({W8+1.2:.2f},0);')
SK=fig('\n'.join(o))
kosmetin='\n'.join('• '+t for t,_ in KOS)
q('0008',tipId='rts-oturma',tip='Planda koşullu yerleştirme',z='zor',alt='Oturma Planı',kaz='Plandaki sıra ve koridor düzenini kullanarak koşullardan herkesin yerini bulur.',kalip='hikâyeli',
 kart='K-RTS-08 (oturma planı) · 8 kişi, 6 koşul',
 metin='Bir yazılım atölyesinde sekiz katılımcı, şekildeki numaralı yerlere birer kişi olacak biçimde oturmuştur. Katılımcıların adları Ali, Burcu, Cem, Deniz, Ece, Fatih, Gül ve Hakan’dır. Aynı yatay sıradaki iki kişiden biri diğerinin “sağında” ise tahtaya bakıldığında daha sağdaki yerdedir. Oturma düzeni için şunlar bilinmektedir:\n'+kosmetin+'\nBuna göre, Ece ile Hakan’ın oturduğu yerlerin numaraları toplamı kaçtır?',
 dogru=v,yan=[(d,f'“{KOS[i][0][:-1]}” koşulunu hesaba katmamış; diğer koşullara uyan bir yerleşimde Ece ile Hakan’ın numaraları toplamı {d} çıkmıştır.','dikkat') for i,d in sec],
 istenen='Ece ile Hakan’ın yer numaraları toplamı.',ip=['Yeri doğrudan bulunabilen kişiden başlayıp koşulları sırayla uygulayarak diğerlerinin yerini belirle.'],bilgi=[SIR],sekil=SK,
 ad=[A('Planı oku','Yerler 1–8 numaralıdır; koridor 2 ile 3 arasındadır; 1–4 ön, 5–8 arka yatay sıradır.','Ön sıra: 1, 2, 3, 4'),A('Arkasındakileri yerleştir','Fatih, Deniz’in; Gül de Ali’nin hemen arkasındadır; Fatih koridora komşu sütundadır.','Fatih 6 ya da 7'),A('Arka sıra','Hakan–Burcu–Fatih sağa doğru dizilir; Fatih koridora komşu olduğundan 3. sütundadır (Fatih 7), Burcu 6, Hakan 5 olur; Gül de arka sıradadır.','Hakan 5, Burcu 6, Fatih 7, Gül 8'),A('Ön sıra','Gül 8 ise Ali 4, Fatih 7 ise Deniz 3; kalan Cem ve Ece ön sıradadır, Ece Cem’in sağındadır.','Cem 1, Ece 2'),A('Toplamı bul','Ece 2, Hakan 5.','2 + 5 = 7')],
 puf='Önce “hemen arkasında” koşullarını yan yana getir; arka sıradaki dört kişiyi belirlerler.')

# ================= 09 orta · terazi =================
a_,b_,c_=6,4,8   # ▲, ●, ■ (yalnız doğrulama)
def esit(sol,sag): return sol[0]*a_+sol[1]*b_+sol[2]*c_==sag[0]*a_+sag[1]*b_+sag[2]*c_
T1=((2,0,0),(0,3,0)); T2=((0,1,1),(2,0,0)); assert esit(*T1) and esit(*T2)
b=Fr(1); a=Fr(3,2)*b; c=2*a-b
sol=(2,0,2); v=(sol[0]*a+sol[2]*c)/b
assert v==7 and c==2
w1_a=Fr(2,3); w1_c=2*w1_a-1; d1=sol[0]*w1_a+sol[2]*w1_c
d2=sol[0]*a+sol[2]*(2*a+1); d3=sol[0]*a+sol[2]*(2*a); d4=sol[0]*a+1*c
e=[d1,d2,d3,d4]; assert e==[2,11,9,5] and len({v,*e})==5
def sem(kind,x,y,s=0.27):
    if kind=='u': return f'\\draw[thick] ({x-s:.2f},{y}) -- ({x+s:.2f},{y}) -- ({x:.2f},{y+1.6*s:.2f}) -- cycle;'
    if kind=='d': return f'\\draw[thick,fill=vurgu!25] ({x:.2f},{y+s:.2f}) circle ({s});'
    return f'\\draw[thick,fill=black!25] ({x-s:.2f},{y}) rectangle ({x+s:.2f},{y+2*s:.2f});'
def kefe(items,cx,y):
    o=[]; n=sum(k for _,k in items)
    xs=[cx+(i-(n-1)/2)*0.75 for i in range(n)]; i=0
    for kind,k in items:
        for _ in range(k): o.append(sem(kind,xs[i],y+0.03)); i+=1
    return o
def terazi(sol,sag,ox,soru=False):
    o=[f'\\draw[thick] ({ox},0) -- ({ox},1.7); \\draw[thick] ({ox-0.7},0) -- ({ox+0.7},0);',f'\\draw[line width=1.8pt] ({ox-2.3},1.7) -- ({ox+2.3},1.7);']
    for cx,it in ((ox-2.3,sol),(ox+2.3,sag)):
        o.append(f'\\draw[line width=1.8pt] ({cx-1.45},0.75) -- ({cx+1.45},0.75); \\draw ({cx},1.7) -- ({cx-1.45},0.75); \\draw ({cx},1.7) -- ({cx+1.45},0.75);'); o+=kefe(it,cx,0.75)
    if soru: o.append(f'\\node[font=\\large] at ({ox+2.3},1.1) {{?}};')
    return o
o=[]
o+=terazi([('u',2)],[('d',3)],0)
o+=[f'\\begin{{scope}}[yshift=-2.4cm]']+terazi([('d',1),('k',1)],[('u',2)],0)+['\\end{scope}']
o+=[f'\\begin{{scope}}[yshift=-4.8cm]']+terazi([('u',2),('k',2)],[],0,True)+['\\end{scope}']
o.append('\\node[anchor=west,font=\\small] at (3.4,-0.3) {$\\triangle$ : üçgen,};')
SK=fig('\n'.join(o[:-1]))
q('0009',tipId='rts-terazi',tip='Dengede teraziler',z='orta',alt='Terazi Denklemleri',kaz='Dengedeki terazilerden cisimlerin ağırlık oranlarını bulup üçüncü terazideki dengeyi kurar.',kalip='yeni nesil',
 kart='K-RTS-09 (terazi) · 2▲ = 3●; ● + ■ = 2▲; 2▲ + 2■',
 metin='Her üçgen birbirine, her daire birbirine ve her kare birbirine eşit ağırlıktadır. Şekildeki ilk iki terazi dengededir. Üçüncü terazinin sol kefesinde şekildeki cisimler bulunmaktadır ve terazi, sağ kefesine yalnız daireler konularak dengelenecektir.\nBuna göre, üçüncü terazinin dengelenmesi için sağ kefeye kaç daire konulmalıdır?',
 dogru=v,yan=[(e[0],'İlk terazide üçgen ile daireyi ters okuyup 3 üçgen = 2 daire almış; sonuç 2 çıkmıştır.','dikkat'),(e[1],'İkinci terazide daireyi yanlış kefeye yazıp kare = 2 üçgen + daire almış; sonuç 11 çıkmıştır.','dikkat'),(e[2],'İkinci terazide daireyi unutup kare = 2 üçgen almış; sonuç 9 çıkmıştır.','dikkat'),(e[3],'Üçüncü terazide yalnız bir kareyi hesaba katmış: 2 üçgen + 1 kare.','dikkat')],
 istenen='Dengelemek için gereken daire sayısı.',ip=['Önce iki dengeden üçgenin, dairenin ve karenin ağırlıklarını birbirine bağla; üçüncü terazideki her cismi aynı cins cinsinden yaz.'],bilgi=[TER],sekil=SK,
 ad=[A('Birinci terazi','Üçgen ile daireyi ilişkilendir.','2 üçgen = 3 daire → üçgen = 1,5 daire'),A('İkinci terazi','Kareyi üçgen ve daire cinsinden yaz.','kare = 2 · 1,5 − 1 = 2 daire'),A('Üçüncü terazinin sol kefesi','Her cisim daire cinsinden yazılır.','2 · 1,5 + 2 · 2'),A('Topla','Daire sayısı bulunur.','3 + 4 = 7')],
 puf='Bütün cisimleri tek cins cinsinden yaz; kefelerde cins başına tek ağırlık kalmalı.')

# ================= 10 orta · kutu–top =================
kt=[9,2,7,1,6]; ort=sum(kt)//len(kt); assert sum(kt)%len(kt)==0 and ort==5
def bfs(bas):
    hedef=tuple([ort]*len(bas)); bas=tuple(bas); gor={bas:0}; kuy=deque([bas])
    while kuy:
        s=kuy.popleft()
        if s==hedef: return gor[s]
        for i in range(len(s)-1):
            for a,b2 in ((i,i+1),(i+1,i)):
                if s[a]>0:
                    t=list(s); t[a]-=1; t[b2]+=1; t=tuple(t)
                    if t not in gor: gor[t]=gor[s]+1; kuy.append(t)
v=bfs(kt)
fark=[x-ort for x in kt]; pre=list(itertools.accumulate(fark))
assert v==sum(abs(x) for x in pre[:-1])==9
pos_=sum(x for x in fark if x>0)
# komşu şartını yok sayan, mesafe ağırlıklı açgözlü eşleştirme (en zengin→en yoksul)
fz=fark[:]; mal=0
while any(fz):
    i=max(range(5),key=lambda k:fz[k]); j=min(range(5),key=lambda k:fz[k]); m=min(fz[i],-fz[j]); mal+=m*abs(i-j); fz[i]-=m; fz[j]+=m
e=[max(fark),ort,pos_,sum(abs(x) for x in fark)]
assert e==[4,5,7,14] and len({v,*e})==5,e
o=[];s=1.9
for i,n in enumerate(kt):
    x=i*s
    o.append(f'\\draw[thick] ({x:.2f},0) -- ({x:.2f},-1.0) -- ({x+1.55:.2f},-1.0) -- ({x+1.55:.2f},0);')
    for k in range(n):
        r,cc=divmod(k,3); o.append(f'\\draw[fill=vurgu!25] ({x+0.33+cc*0.45:.2f},{-0.75+r*0.3:.2f}) circle (0.12);')
    o.append(f'\\node[below=2pt] at ({x+0.78:.2f},-1.0) {{{n} top}};')
SK=fig('\n'.join(o))
q('0010',tipId='rts-kutu',tip='Komşu kutular arasında aktarma',z='orta',alt='Kutu ve Top',kaz='Komşu kutular arasında top aktararak kutuları eşitlemek için gereken en az hamleyi bulur.',kalip='yeni nesil',
 kart='K-RTS-10 (kutu-top) · 9, 2, 7, 1, 6',
 metin='Yan yana dizilmiş 5 kutuda, şekilde görüldüğü kadar top vardır. Bir “hamle”, yan yana olan iki kutudan birinden bir top alıp diğerine koymaktır; hamle sırasında hiçbir kutudaki top sayısı sıfırın altına düşmez. Bütün kutulardaki top sayıları eşit olduğunda işlem tamamlanmış sayılır ve kutulara hamle dışında top eklenmez ya da çıkarılmaz.\nBuna göre, işlemi tamamlamak için en az kaç hamle gerekir?',
 dogru=v,yan=[(e[0],'En fazla toplu kutunun fazlasını (9 − 5) hamle sayısı sanmış.','dikkat'),(e[1],'Her kutuda kalması gereken top sayısını (ortalama) hamle sayısı sanmış.','dikkat'),(e[2],'Yalnız fazla topların toplamını (4 + 2 + 1) almış; topların uzaktaki kutulara taşınmasını hesaba katmamış.','dikkat'),(e[3],'Fazla ve eksik farkların hepsini toplamış: 4 + 3 + 2 + 4 + 1.','islem')],
 istenen='En az hamle sayısı.',ip=['Her kutunun ortalamadan farkını yaz; soldan sağa ilerleyerek her komşu çiftin arasından kaç topun geçmesi gerektiğine bak.'],bilgi=[KUT],sekil=SK,
 ad=[A('Ortalamayı bul','Toplam top 5 kutuya eşit dağılır.','25 ÷ 5 = 5 top'),A('Farkları yaz','Her kutunun ortalamadan farkı bulunur.','+4, −3, +2, −4, +1'),A('Komşu çiftlerden geçenler','Soldan sağa biriken farkın mutlak değeri, o iki kutu arasından geçen top sayısıdır.','4, 1, 3, 1'),A('Topla','Dört komşu çiftten geçen top sayıları toplanır.','4 + 1 + 3 + 1 = 9')],
 puf='Birinci ve ikinci kutu arasından geçecek top sayısı, birinci kutunun fazlasına eşittir.')

bitir(P,'rutinsek',UK)
