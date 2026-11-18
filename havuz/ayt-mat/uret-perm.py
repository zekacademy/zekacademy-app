"""AYT Matematik · Permütasyon ve Kombinasyon · 20 soruluk paket (4 kolay / 10 orta / 6 zor).
Her doğru ve çeldirici değer kaba kuvvetle ya da formülle hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import comb,perm,factorial as F
from itertools import permutations,combinations,product
H.KONU='Permütasyon ve Kombinasyon'
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
UK='amat|Permütasyon ve Kombinasyon'
P=Parti('perm','Permütasyon ve Kombinasyon',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM 2018–2025 AYT Matematik (Permütasyon-Kombinasyon: oturma düzeni, seçim, sıralama koşulları; yalnız mantık) · yayın soru bankaları · MEB 11. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def dist(v,e): assert len({v,*e})==len(e)+1,(v,e)

# ---------- bilgi kutuları (yalnız tanım/gösterim; örnekler soruların sayılarından farklı) ----------
SAY=B('Toplama ve çarpma kuralı','art arda yapılan bağımsız seçimlerin sayıları çarpılır; aynı anda gerçekleşemeyen ayrı durumların sayıları toplanır. Örnek: 2 gömlek ve 5 pantolondan bir takım 2 × 5 = 10 farklı biçimde seçilir; bir yolcu ya trenle (4 sefer) ya otobüsle (3 sefer) gidiyorsa 4 + 3 = 7 seçeneği vardır')
PER=B('Permütasyon','n farklı elemandan seçilen r tanesinin sıralı dizilişi P(n, r) = n!/(n − r)! tanedir; sıra önemlidir. Örnek: 6 farklı kitaptan 2’si bir rafa sıralı konacaksa P(6, 2) = 6 × 5 = 30')
KOM=B('Kombinasyon','n farklı elemandan sıra gözetmeden seçilen r tanenin sayısı C(n, r) = n!/(r! (n − r)!) tanedir; C(n, r) = C(n, n − r). Örnek: 6 kişiden 2 kişilik ekip C(6, 2) = 15')
TOP=B('Tümleyen sayma','“en az …” ya da “hiçbiri …” koşullarında tüm durumların sayısından istenmeyen durumların sayısı çıkarılarak da sayılabilir. Örnek: 5 kişiden 2’si seçilirken belirli bir kişinin bulunmadığı seçimler C(5, 2) − C(4, 1) = 6 tanedir')
DAI=B('Dairesel dizilim','n farklı elemanın bir çember (yuvarlak masa) etrafındaki dizilişlerinde, dönmeyle birbirine dönüşen dizilişler aynı sayılır ve sayıları (n − 1)! olur. Örnek: 4 kişi yuvarlak masaya (4 − 1)! = 6 farklı biçimde oturur')
TEK=B('Tekrarlı permütasyon','n elemandan n₁ tanesi birbirinin aynı, n₂ tanesi birbirinin aynı … ise bütün dizilişlerin sayısı n!/(n₁! · n₂! …) olur. Örnek: “ANANAS” harfleriyle yazılabilecek 6 harfli dizilişler 6!/(3! · 2!) = 60 tanedir')
IZG=B('Izgarada en kısa yol','yalnız sağa ve yukarı gidilen yollarda dikey ve yatay adımların dizilişi sayılır. a adım sağa, b adım yukarı gidilecekse en kısa yol sayısı C(a + b, a) tanedir. Örnek: 2 sağa, 2 yukarı adım için C(4, 2) = 6 yol vardır; bir noktadan geçen yolların sayısı iki parçanın çarpımıdır')
BLK=B('Bloklaştırma','yan yana bulunması istenen elemanlar tek bir blok sayılır; önce bloklar kendi aralarında, sonra her blok içinde sıralanır. Örnek: A ve B yan yana olacak biçimde 4 kişi, bloğu bir kişi sayarak 3! × 2! = 12 farklı sıralanır')
PAS=B('Faktöriyel ve gösterimler','n! = n (n − 1) … 2 · 1 (faktöriyel); P(n, r) = n!/(n − r)! ve C(n, r) = n!/(r! (n − r)!) biçiminde tanımlanır. Örnek: 5! = 120, P(5, 2) = 20, C(5, 2) = 10')
GRP=B('Gruplara ayırma','gruplar adlandırılmamışsa ve aynı büyüklükte k grup varsa, sırayla seçilerek bulunan sayı k!’e bölünür. Örnek: 4 kişi 2’şerli iki gruba C(4, 2)/2! = 3 farklı biçimde ayrılır')
GEO=B('Köşelerden şekil sayma','n noktadan üçgen kurmak için doğrusal olmayan üç nokta seçilir; aynı doğru üzerindeki üç nokta üçgen oluşturmaz. Örnek: biri aynı doğru üzerinde 4 nokta ile 2 ek nokta için C(6, 3) − C(4, 3) = 16 üçgen çizilir')
BOY=B('Bölge boyama','komşu bölgeler (ortak bir sınır çizgisi olan bölgeler) farklı renkte boyanır; yalnız bir noktada buluşan bölgeler komşu sayılmaz. Örnek: yan yana duran 3 bölgeyi, 3 renkle komşuları farklı olacak biçimde boyayan kişi 3 × 2 × 2 = 12 farklı boyama yapar')
SAYI=B('Rakamlardan sayı yazma','n basamaklı bir sayıda en soldaki rakam sıfır olamaz; rakamları farklı olması isteniyorsa her basamak seçildikçe seçenek sayısı bir azalır. Koşullu basamak (örneğin birler basamağı) önce doldurulur. Örnek: 1, 2, 3 rakamlarıyla rakamları farklı 2 basamaklı 3 × 2 = 6 sayı yazılır')

# ---------- kartlar ----------
kartla('K-APER-01','Toplama ve çarpma kuralı (şema, tablo, ağaç)','Şemadan ya da tablodan her aşamadaki seçenek sayıları okunur; art arda aşamalar çarpılır, birbirinin yerine geçen durumlar toplanır, koşullu dallar ayrı ele alınır.','Çarpılacak yerde toplamak (ya da tersi); bir dalda kaç seçenek olduğunu bütün dallar için aynı sanmak; koşulu sağlamayan dalları saymak.','kolay','hikâyeli',3,'pr-sayma','Toplama ve çarpma kuralı')
kartla('K-APER-02','Sıralı seçim ve sıralama koşulları','Her konum için kalan seçenek sayısı bulunur; kısıtlı konum önce doldurulur; yan yana koşulu blokla, ayrı koşulu tümleyenle çözülür.','Sıranın önemli olup olmadığını karıştırmak; blok içi sıralamayı unutmak; kısıtlı konumu sona bırakıp seçenek sayısını yanlış bulmak.','orta','hikâyeli',4,'pr-permutasyon','Permütasyon ve sıralama koşulları')
kartla('K-APER-03','Izgarada en kısa yol','Yolun yatay ve dikey adımlarının dizilişi sayılır; ara noktadan geçen yollar parçaların çarpımıdır; kapalı yollar tümleyenle ya da tek tek hesapla ayrılır.','Adım sayısını düğüm sayısıyla karıştırmak; çarpma yerine toplamak; çakışan yolları iki kez çıkarmak.','orta','hikâyeli',4,'pr-izgara','Izgarada en kısa yol')
kartla('K-APER-04','Dairesel ve sabit sandalyeli oturma düzeni','Sandalyeler numaralıysa sıralama, numarasız yuvarlak masada dönüşler aynı sayılır; ilişkili iki kişi için konum ilişkisi sayılır ya da tümleyen alınır.','Dönmeyle eşit dizilişleri ayrı saymak; “yan yana” ve “karşılıklı” durumlarından birini unutmak; iki kişinin kendi aralarındaki yer değişimini atlamak.','orta','hikâyeli',4,'pr-dairesel','Dairesel ve sabit sandalyeli oturma')
kartla('K-APER-05','Tekrarlı dizilişler ve bloklaştırma','Aynı harf/nesne tekrarı faktöriyellerle bölünür; birlikte olması istenenler blok, ayrı olması istenenler araya yerleştirme ile sayılır.','Tekrarı bölmeyi unutmak; araya yerleştirmede uçları saymamak; blokları kendi içinde sıralamamak.','orta','düz',4,'pr-siralama','Tekrarlı dizilişler ve bloklaştırma')
kartla('K-APER-06','Permütasyon-kombinasyon özdeşlikleri','Her yargı tanım ya da Pascal özdeşliğiyle sayısal olarak sınanır; küçük bir örnekle yanlış yargı çürütülür.','P(n, r) ile C(n, r) arasındaki r! çarpanını karıştırmak; faktöriyel sadeleştirmede kalan çarpanları atlamak; Pascal özdeşliğinin alt indislerini kaydırmak.','orta','öncüllü',3,'pr-ozdeslik','Permütasyon-kombinasyon özdeşlikleri')
kartla('K-APER-07','Rakamlardan sayı yazma','Koşullu basamak önce doldurulur; baştaki sıfır yasağı ayrı durum olarak ele alınır; her yargı için sayma ayrı yapılır.','Baştaki sıfırı ayrı düşünmemek; koşullu basamağı sona bırakıp seçenek sayısını yanlış bulmak; durumları iki kez saymak.','orta','öncüllü',4,'pr-sayiyaz','Rakamlardan sayı yazma')
kartla('K-APER-08','Geometrik nesnelerle sayma','Noktalar, köşeler ya da doğrular arasından seçim yapılır; aynı doğru üzerindeki ya da kenar oluşturan seçimler tümleyenle ayrılır.','Doğrusal noktalardan üçgen sanmak; iki koşulu çıkarırken ortak durumu iki kez çıkarmak; seçim yerine sıralama yapmak.','zor','yeni nesil',4,'pr-geometri','Geometrik nesnelerle sayma')
kartla('K-APER-09','Bölge boyama','Bölgeler komşuluk grafiğine göre sırayla boyanır; en çok komşusu olan bölge önce renklendirilir; çakışma yaratacak komşu çiftleri ayrı durum olarak sayılır.','Komşu olmayan bölgeleri komşu sanmak; döngü kapanışındaki ek koşulu unutmak; kullanılan renk sayısını yanlış belirlemek.','orta','yeni nesil',4,'pr-boyama','Bölge boyama')
kartla('K-APER-10','Seçim, gruplama ve en az/en çok koşulları','Koşullar bölünüp durumlara ayrılır ya da tümleyenle sayılır; seçimler kombinasyonla, adlandırılmamış gruplar eşit gruplara bölme düzeltmesiyle sayılır.','Sıra gözetmek; ortak durumu iki kez saymak; adlandırılmamış gruplarda grup sayısının faktöriyeline bölmeyi unutmak.','zor','hikâyeli',5,'pr-secim','Seçim, gruplama ve koşullu sayma')

# ---------- şekil yardımcıları ----------
def grid(W,Hh,kapali=(),pts=None,sc=0.8,etk=True):
    kap={frozenset(e) for e in kapali}; o=[]
    for x in range(W+1):
        for y in range(Hh+1):
            for dx,dy in ((1,0),(0,1)):
                x2,y2=x+dx,y+dy
                if x2>W or y2>Hh: continue
                if frozenset([(x,y),(x2,y2)]) in kap:
                    o.append(f'\\draw[red!70!black,dash pattern=on 2pt off 3pt,line width=1pt] ({x*sc},{y*sc}) -- ({x2*sc},{y2*sc});')
                    o.append(f'\\node[red!70!black,font=\\large\\bfseries,fill=white,inner sep=0.5pt] at ({(x+x2)/2*sc},{(y+y2)/2*sc}) {{$\\times$}};')
                else: o.append(f'\\draw[blue!55!black,line width=1.6pt] ({x*sc},{y*sc}) -- ({x2*sc},{y2*sc});')
    for x in range(W+1):
        for y in range(Hh+1): o.append(f'\\fill[gray!70] ({x*sc},{y*sc}) circle (0.06);')
    if etk:
        o.append(f'\\fill[green!50!black] (0,0) circle (0.14); \\node[below left,font=\\normalsize\\bfseries] at (0,0) {{A}};')
        o.append(f'\\fill[green!50!black] ({W*sc},{Hh*sc}) circle (0.14); \\node[above right,font=\\normalsize\\bfseries] at ({W*sc},{Hh*sc}) {{B}};')
    for n,((x,y),c) in (pts or {}).items():
        o.append(f'\\fill[{c}] ({x*sc},{y*sc}) circle (0.15); \\node[above left,font=\\normalsize\\bfseries,text={c}] at ({x*sc},{y*sc}) {{{n}}};')
    return '\n'.join(o)
def yollar(W,Hh,kapali=(),zorunlu=None,yasak=None):
    """Sağa/yukarı en kısa yolları tek tek sayar; zorunlu: geçilmesi gereken düğüm; yasak: geçilmeyecek düğümler."""
    kap={frozenset(e) for e in kapali}; yasak=set(yasak or [])
    def git(x,y,gec,zor_ok):
        if (x,y) in yasak: return 0
        if (x,y)==zorunlu: zor_ok=True
        if (x,y)==(W,Hh): return 1 if (zorunlu is None or zor_ok) else 0
        t=0
        for dx,dy in ((1,0),(0,1)):
            x2,y2=x+dx,y+dy
            if x2<=W and y2<=Hh and frozenset([(x,y),(x2,y2)]) not in kap: t+=git(x2,y2,gec,zor_ok)
        return t
    return git(0,0,None,False)
def masa(n,r=1.15,numara=False,rad=1.75):
    import math
    o=[f'\\draw[thick,fill=orange!22] (0,0) circle ({r});\\node[font=\\small\\bfseries] at (0,0) {{MASA}};']
    for i in range(n):
        a=math.pi/2-2*math.pi*i/n; x,y=rad*math.cos(a),rad*math.sin(a)
        o.append(f'\\draw[thick,fill=blue!18,rounded corners=2pt] ({x-0.27:.3f},{y-0.27:.3f}) rectangle ({x+0.27:.3f},{y+0.27:.3f});')
        if numara: o.append(f'\\node[font=\\footnotesize\\bfseries] at ({x:.3f},{y:.3f}) {{{i+1}}};')
    return '\n'.join(o)

# ================= 01 kolay · yol ağı (çarpma-toplama) =================
yl={('A','B'):3,('B','D'):2,('A','C'):2,('C','D'):4}
v=yl[('A','B')]*yl[('B','D')]+yl[('A','C')]*yl[('C','D')]; assert v==14
# kaba kuvvet: her yol bir (kenar, seçilen yol no) dizisi
ks=sum(1 for a in range(3) for b in range(2))+sum(1 for a in range(2) for b in range(4)); assert ks==v
e=[sum(yl.values()),yl[('A','B')]*yl[('C','D')]+yl[('A','C')]*yl[('B','D')],(yl[('A','B')]+yl[('A','C')])*(yl[('B','D')]+yl[('C','D')]),yl[('A','B')]*yl[('B','D')]*yl[('A','C')]*yl[('C','D')]]
assert e==[11,16,30,48]; dist(v,e)
o=[f'\\node[circle,draw,thick,fill=yellow!30,minimum size=0.75cm,font=\\bfseries] ({n}) at {p} {{{n}}};' for n,p in (('A','(0,0)'),('B','(2.8,1.5)'),('C','(2.8,-1.5)'),('D','(5.6,0)'))]+[
   '\\draw[-{Stealth},line width=1.8pt,blue!70!black] (A) -- node[midway,above left=1pt,fill=white,inner sep=2pt,font=\\small\\bfseries] {3 yol} (B);',
   '\\draw[-{Stealth},line width=1.8pt,blue!70!black] (B) -- node[midway,above right=1pt,fill=white,inner sep=2pt,font=\\small\\bfseries] {2 yol} (D);',
   '\\draw[-{Stealth},line width=1.8pt,orange!85!black] (A) -- node[midway,below left=1pt,fill=white,inner sep=2pt,font=\\small\\bfseries] {2 yol} (C);',
   '\\draw[-{Stealth},line width=1.8pt,orange!85!black] (C) -- node[midway,below right=1pt,fill=white,inner sep=2pt,font=\\small\\bfseries] {4 yol} (D);']
SK=fig('\n'.join(o))
q('0001',tipId='pr-sayma',tip='Toplama ve çarpma kuralı',z='kolay',alt='Sayma Kuralları',kaz='Şemadaki yol sayılarına çarpma ve toplama kurallarını birlikte uygulayarak toplam seçenek sayısını bulur.',kalip='hikâyeli',
 kart='K-APER-01 (yol şeması) · tek yönlü ağda iki ayrı güzergâh; her ayakta birden çok yol',
 metin='Bir kargo firmasının dağıtım ağında A, B, C ve D adlı dört merkez bulunmaktadır. Şekilde merkezler arasındaki tek yönlü karayolu bağlantıları ve her bağlantıdaki ayrı yol sayısı gösterilmiştir. Bir kurye, A merkezinden D merkezine yalnızca oklar yönünde ilerleyerek gidecektir.\nBuna göre kurye, A’dan D’ye kaç farklı yolla gidebilir?',
 dogru=v,yan=[(e[0],'Hangi güzergâhın seçildiğini ve aşamaların birbirini izlediğini düşünmeden bütün yol sayılarını toplamış: 3 + 2 + 2 + 4.','bilgi'),(e[1],'A→B yollarını C→D yollarıyla, A→C yollarını B→D yollarıyla çapraz eşleştirmiş: 3 × 4 + 2 × 2.','dikkat'),(e[2],'Önce A’dan çıkan yolları (3 + 2), sonra D’ye giren yolları (2 + 4) toplayıp çarpmış; B ve C üzerinden geçen güzergâhları ayırmamış.','bilgi'),(e[3],'Güzergâhları birbirinin seçeneği saymak yerine bütün yolları art arda kullanılacak sanıp hepsini çarpmış: 3 × 2 × 2 × 4.','bilgi')],
 istenen='A’dan D’ye oklar yönünde gidişlerin sayısı.',ip=['Kurye A’dan D’ye giderken kaç farklı güzergâh izleyebilir? Her güzergâhta kaç aşama var?'],bilgi=[SAY],sekil=SK,
 ad=[A('Güzergâhları ayır','A’dan D’ye gidiş ya B merkezi ya da C merkezi üzerinden olur; ikisi aynı anda seçilemez.','Güzergâh 1: A → B → D · Güzergâh 2: A → C → D'),A('Her güzergâhı say','Bir güzergâhta ardışık aşamalarda yol sayıları çarpılır.','3 × 2 = 6 · 2 × 4 = 8'),A('Toplam','Ayrı güzergâhlar toplanır.','6 + 8 = 14')],
 puf='Ağ sorularında önce birbirinin yerine geçen güzergâhları ayır, sonra her güzergâhın içinde çarp.')

# ================= 02 kolay · sıralı seçim =================
v=perm(7,3); assert v==210==sum(1 for _ in permutations(range(7),3))
e=[comb(7,3),7*6,7**3,F(7)//F(3)]; assert e==[35,42,343,840]; dist(v,e)
q('0002',tipId='pr-permutasyon',tip='Permütasyon ve sıralama koşulları',z='kolay',alt='Permütasyon',kaz='Farklı görevlerin dağıtıldığı sıralı seçimlerde permütasyon sayısını hesaplar.',kalip='hikâyeli',
 kart='K-APER-02 (sıralı seçim) · 7 kişiden üç ayrı görev; bir kişi en çok bir görevde',
 metin='Bir okul robotik kulübünün yedi üyesi arasından bir başkan, bir başkan yardımcısı ve bir sayman seçilecektir. Bir üye bu görevlerden en fazla birini üstlenebilir ve her görev için tek kişi seçilecektir.\nBuna göre bu seçim kaç farklı biçimde yapılabilir?',
 dogru=v,yan=[(e[0],'Görevlerin ayrı olduğunu görmeden yalnız üç kişilik grup seçmiş: C(7, 3) = 35.','bilgi'),(e[1],'Yalnız iki görevi doldurmuş: 7 × 6 = 42; sayman görevini unutmuş.','dikkat'),(e[2],'Bir üyenin birden çok görev alabileceğini sanıp 7 × 7 × 7 yazmış.','dikkat'),(e[3],'P(7, 3) için 7!/3! hesaplamış; paydada (7 − 3)! = 4! yerine 3! almış.','islem')],
 istenen='Üç ayrı görev için yapılabilecek seçimlerin sayısı.',ip=['Başkan seçildikten sonra başkan yardımcısı için kaç aday kalır?'],bilgi=[PER],
 ad=[A('Başkanı seç','Yedi üyeden biri başkan olabilir.','7 seçenek'),A('Diğer görevleri seç','Seçilen kişi başka görev alamaz.','Yardımcı: 6 · Sayman: 5'),A('Çarp','Ardışık seçimler çarpılır.','7 × 6 × 5 = 210')],
 puf='Görevler birbirinden farklıysa kişilerin seçilme sırası sonucu değiştirir.')

# ================= 03 kolay · ızgara en kısa yol =================
v=yollar(4,3); assert v==comb(7,3)==35
e=[comb(8,3),comb(8,4),F(4)*F(3),perm(7,3)]; assert e==[56,70,144,210]; dist(v,e)
SK=fig(grid(4,3))
q('0003',tipId='pr-izgara',tip='Izgarada en kısa yol',z='kolay',alt='Izgarada Yol Sayma',kaz='Dikdörtgen ızgarada yalnız sağa ve yukarı giderek en kısa yol sayısını kombinasyonla hesaplar.',kalip='hikâyeli',
 kart='K-APER-03 (tam ızgara) · 4 sağ, 3 yukarı adım',
 metin='Bir mahallenin sokakları şekildeki gibi birbirine dik ve eşit aralıklı doğrulardan oluşmaktadır. Postacı Ece, A noktasındaki postaneden çıkıp B noktasındaki apartmana, her adımda yalnızca sağa ya da yukarıya doğru sokak boyunca ilerleyerek gidecektir.\nBuna göre Ece, A’dan B’ye kaç farklı yolla gidebilir?',
 dogru=v,yan=[(e[0],'Çizgi sayısını adım sayısı sanıp 5 dikey ve 4 yatay çizgiye göre 5 sağa 3 yukarı adım almış: C(8, 3) = 56.','dikkat'),(e[1],'Izgarada 4 sağ ve 4 yukarı adım olduğunu sanıp C(8, 4) hesaplamış; adım sayısını kesişim sayısıyla karıştırmış.','dikkat'),(e[2],'Adımların her dizilişini farklı sanıp aynı yönlü adımları da birbirinden ayırmış: 4! × 3!.','bilgi'),(e[3],'Yedi adımın yalnızca üç tanesini sıralı seçmiş: P(7, 3) = 7 × 6 × 5; sırayı gereksiz saymış.','islem')],
 istenen='A’dan B’ye en kısa yol sayısı.',ip=['Her yolda toplam kaç adım atılır ve bu adımlar kaç türlü olabilir?'],bilgi=[IZG],sekil=SK,
 ad=[A('Adımları say','Şekilden A’dan B’ye 4 adım sağa ve 3 adım yukarı gidilir.','Toplam 4 + 3 = 7 adım'),A('Diziliş say','7 adımın hangi 3’ünün “yukarı” olduğu seçilir; geri kalanlar “sağa” olur.','C(7, 3)'),A('Hesapla','Kombinasyon açılır.','7 × 6 × 5 / (3 × 2 × 1) = 35')],
 puf='Izgara yolunu adım dizisine çevir; hangi adımların “yukarı” olacağını seçmek yeter.')

# ================= 04 kolay · tablo, farklı bölümlerden seçim =================
ogr={'Matematik':5,'Fizik':4,'Kimya':3}
kisi=[(b,i) for b,n in ogr.items() for i in range(n)]
v=sum(1 for a,b in combinations(kisi,2) if a[0]!=b[0]); assert v==5*4+5*3+4*3==47
e=[comb(12,2),5*4*3,perm(12,2),2*v]; assert e==[66,60,132,94]; dist(v,e)
SK=tablo_svg(['Bölüm','Öğretmen sayısı'],[[b,str(n)] for b,n in ogr.items()])
q('0004',tipId='pr-sayma',tip='Toplama ve çarpma kuralı',z='kolay',alt='Seçme Kuralları',kaz='Tablodaki verilerle farklı gruplardan seçim sayısını toplama ve çarpma kuralıyla bulur.',kalip='tablo',
 kart='K-APER-01 (tablo) · üç bölümden farklı bölümlerde iki kişilik seçim',
 metin='Bir okulun Matematik, Fizik ve Kimya bölümlerindeki öğretmen sayıları aşağıdaki tabloda verilmiştir. Okul müdürlüğü, iki öğretmenden oluşan bir sınav komisyonu kuracak; komisyondaki iki öğretmenin farklı bölümlerden olmasını istemektedir.\nBuna göre bu komisyon kaç farklı biçimde kurulabilir?',
 dogru=v,yan=[(e[0],'Bölüm koşulunu gözetmeden 12 öğretmenden herhangi ikisini seçmiş: C(12, 2).','dikkat'),(e[1],'Üç bölümden birer kişi seçecekmiş gibi bütün sayıları çarpmış: 5 × 4 × 3.','dikkat'),(e[2],'Bölüm koşulunu gözetmeden iki öğretmeni sıralı seçmiş: 12 × 11.','bilgi'),(e[3],'Seçilen iki kişinin sırasını da ayırt edip her komisyonu iki kez saymış: 2 × 47.','islem')],
 istenen='Farklı bölümlerden iki öğretmenlik komisyonların sayısı.',ip=['Komisyondaki iki öğretmenin bölümlerini seçmenin kaç farklı yolu var?'],bilgi=[SAY],sekil=SK,
 ad=[A('Bölüm çiftlerini yaz','İki öğretmen farklı bölümlerden gelir; bölüm çifti üç farklı biçimde olur.','Mat–Fiz · Mat–Kim · Fiz–Kim'),A('Her çift için say','Her çiftte öğretmen sayıları çarpılır.','5 × 4 = 20 · 5 × 3 = 15 · 4 × 3 = 12'),A('Topla','Çiftler birbirinin yerine geçen durumlardır, toplanır.','20 + 15 + 12 = 47')],
 puf='“Farklı gruptan” koşulu varsa önce grup çiftlerini yaz, her çift için çarp, sonra topla.')

# ================= 05 orta · yuvarlak masa, iki kişi yan yana değil =================
t5=sum(1 for p in permutations(range(1,7)) if (p.index(1)+1) not in (1,6)); assert t5==480
v=480; assert v==F(6)-2*F(5)
e=[2*F(5),4*F(4),F(6)-F(5),F(6)]; assert e==[240,96,600,720]; dist(v,e)
SK=fig(masa(7))
q('0005',tipId='pr-dairesel',tip='Dairesel ve sabit sandalyeli oturma',z='orta',alt='Dairesel Dizilim',kaz='Yuvarlak masa etrafında iki kişinin yan yana oturmaması koşulunu tümleyen sayma ile çözer.',kalip='hikâyeli',
 kart='K-APER-04 (yuvarlak masa) · 7 kişi, iki kişi yan yana olmayacak; dönmeler aynı',
 metin='Yedi arkadaş, şekilde görülen yuvarlak masanın etrafındaki yedi koltuğa oturacaktır. Koltuklar numaralı değildir; masa döndürüldüğünde birbirine dönüşen oturma düzenleri aynı kabul edilmektedir. Aralarında küs olan Ali ile Berk’in yan yana oturmak istememesi dışında bir koşul yoktur.\nBuna göre bu yedi arkadaş kaç farklı biçimde oturabilir?',
 dogru=v,yan=[(e[0],'Yan yana oturma durumlarını saymış: Ali ile Berk bir blok olursa 2 × 5! = 240; “olmayan”ı değil “olan”ı bulmuş.','dikkat'),(e[1],'Ali’yi sabitleyip Berk için 4 uygun koltuk bulmuş; kalan beş kişinin yerleşimi için 5! yerine 4! almış: 4 × 4!.','islem'),(e[2],'Yan yana olan durumları 5! saymış, ikisinin kendi aralarındaki yer değişimini (×2) unutmuş: 6! − 5!.','islem'),(e[3],'Koşulu hiç uygulamadan 7 kişinin dairesel dizilişini yazmış: (7 − 1)!.','dikkat')],
 istenen='Ali ile Berk’in yan yana oturmadığı oturma düzenlerinin sayısı.',ip=['Ali ile Berk’in yan yana oturduğu düzenler kaç tane?'],bilgi=[DAI,BLK],sekil=SK,
 ad=[A('Tüm düzenleri say','Yedi kişi yuvarlak masada, dönmeler aynı sayıldığı için (7 − 1)! farklı biçimde oturur.','6! = 720'),A('Yan yana olanları say','Ali ile Berk blok sayılır: 6 birim dairesel dizilir, blok içi 2 yoldur.','(6 − 1)! × 2! = 240'),A('Çıkar','İstenmeyen düzenler tüm düzenlerden çıkarılır.','720 − 240 = 480')],
 puf='Koşullu sayma sorularında hangi durumların sayılmasının daha kolay olduğuna önce karar ver.')

# ================= 06 orta · tekrarlı, A'lar ayrı =================
sozc=set(permutations('SAKARYA')); assert len(sozc)==840==F(7)//F(3)
v=sum(1 for w in sozc if 'AA' not in ''.join(w)); assert v==240==F(4)*comb(5,3)
assert sum(1 for w in sozc if 'AAA' in ''.join(w))==120
e=[F(4)*comb(4,3),120,840-120,F(4)]; assert e==[96,120,720,24]; dist(v,e)
q('0006',tipId='pr-siralama',tip='Tekrarlı dizilişler ve bloklaştırma',z='orta',alt='Tekrarlı Permütasyon',kaz='Tekrarlı harflerle yazılan dizilişlerde aynı harflerin ayrı yerleştirilmesini araya yerleştirme ile sayar.',kalip='düz',
 kart='K-APER-05 (tekrarlı harf, ayrı yerleştirme) · 7 harfli sözcük, üç özdeş harf birbirinden ayrı',
 metin='SAKARYA sözcüğündeki harflerin tamamı kullanılarak, anlamlı ya da anlamsız 7 harfli sözcükler yazılıyor. Bu sözcüklerin hiçbirinde iki A harfi yan yana bulunmuyor.\nBuna göre bu koşulu sağlayan kaç farklı sözcük yazılabilir?',
 dogru=v,yan=[(e[0],'A’lar için boşlukları sayarken iki uç boşluğu saymayıp 4 boşluk almış: 4! × C(4, 3) = 96.','dikkat'),(e[1],'Üç A’yı yan yana tek blok yapmış: 5! = 120; “ayrı” koşulunu yan yana koşuluyla karıştırmış.','bilgi'),(e[2],'Yalnız üç A’nın hepsinin bir arada olduğu durumları çıkarmış: 840 − 120; iki A’nın yan yana olduğu durumları atlamış.','dikkat'),(e[3],'Yalnız S, K, R, Y harflerinin dizilişini sayıp A’ların yerleşimini unutmuş: 4!.','dikkat')],
 istenen='A harflerinin hiçbirinin yan yana gelmediği sözcüklerin sayısı.',ip=['Üç A’nın hiçbiri yan yana olmayacaksa diğer harfler onlara nasıl bir yerleşim sağlar?'],bilgi=[TEK],
 ad=[A('A olmayanları yerleştir','S, K, R, Y harflerinin hepsi farklıdır.','4! = 24'),A('Boşlukları say','4 harf, iki uç dahil 5 boşluk oluşturur; her boşluğa en çok bir A konur.','5 boşluk'),A('A’ları yerleştir','Üç özdeş A için 5 boşluktan 3’ü seçilir; A’lar özdeş olduğundan sıra önemsizdir.','C(5, 3) = 10'),A('Çarp','Harf dizilişleri ve boşluk seçimi çarpılır.','24 × 10 = 240')],
 puf='“Hiçbiri yan yana değil” koşulunda önce diğer nesneleri diz, sonra araya (uçlar dahil) yerleştir.')

# ================= 07 orta · öncüllü özdeşlikler =================
I_=comb(12,5)+comb(12,6)==comb(13,6); II_=perm(7,3)==3*comb(7,3)
III_=all(F(n+2)//F(n)==n*n+3*n+2 for n in range(1,12))
assert (I_,II_,III_)==(True,False,True)
assert [F(n+2)//F(n)==n+2 for n in (3,4)]==[False,False]
sira=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
q('0007',tipId='pr-ozdeslik',tip='Permütasyon-kombinasyon özdeşlikleri',z='orta',alt='Özdeşlikler',kaz='Permütasyon, kombinasyon ve faktöriyel ifadelerinin eşitliklerini tanım ve Pascal özdeşliğiyle sınar.',kalip='öncüllü',
 kart='K-APER-06 (özdeşlik sınama) · Pascal toplamı, P–C ilişkisi, faktöriyel sadeleştirme',
 metin='n pozitif tam sayı olmak üzere,\nI. C(12, 5) + C(12, 6) = C(13, 6)\nII. P(7, 3) = 3 · C(7, 3)\nIII. (n + 2)!/n! = n² + 3n + 2\neşitliklerinden hangileri doğrudur?',
 dogru='I ve III',sira=sira,yan=[('Yalnız I','III’ü sınarken (n + 2)!/n! ifadesini n + 2 biçiminde sadeleştirmiş; (n + 2)(n + 1) çarpımını görememiş.','islem'),('Yalnız III','Pascal özdeşliğinde alt indisi kaydırıp C(12, 5) + C(12, 6) = C(13, 5) bulmuş; I’i yanlış saymış.','bilgi'),('I ve II','P(7, 3) = 3 · C(7, 3) yazıp II’yi doğru bulmuş; III’te (n + 2)!/n!’i n + 2’ye sadeleştirip III’ü yanlış bulmuş.','bilgi'),('I, II ve III','P(n, r) = r · C(n, r) sanıp II’yi doğru kabul etmiş; çarpan r! olmalıdır.','bilgi')],
 istenen='Doğru olan eşitliklerin hangileri olduğu.',ip=['Her eşitliği küçük sayılarla deneyerek sına.'],bilgi=[PAS],
 ad=[A('I’i sına','Pascal özdeşliği iki komşu terimi toplar.','C(12, 5) + C(12, 6) = C(13, 6) → doğru'),A('II’yi sına','P(7, 3) = 3! · C(7, 3) olmalıdır.','210 ≠ 3 × 35 = 105 → yanlış'),A('III’ü sına','(n + 2)!/n! = (n + 2)(n + 1).','n² + 3n + 2 → doğru'),A('Sonuç','Doğru olanlar I ve III’tür.','I ve III')],
 puf='Bir özdeşlikten şüphe ediyorsan küçük bir sayıyla deneyip hemen sına.')

# ================= 08 orta · ağaç şeması, ayranlı olmayan menü =================
T={'Köfte':{'Pilav':['Ayran','Su'],'Makarna':['Ayran','Su']},'Tavuk':{'Pilav':['Ayran','Su'],'Salata':['Ayran','Su'],'Makarna':['Ayran','Su']},'Balık':{'Salata':['Ayran','Su','Limonata']}}
menu=[(y,g,i) for y,d in T.items() for g,l in d.items() for i in l]
assert len(menu)==13; v=sum(1 for m in menu if m[2]!='Ayran'); assert v==7
npair=sum(len(d) for d in T.values()); assert npair==6
e=[len(menu),len(menu)-1,5*1+3,len(menu)-3]; assert e==[13,12,8,10]; dist(v,e)
col={'Köfte':'blue!70!black','Tavuk':'orange!85!black','Balık':'green!45!black'}
row=0; o=[]; yy={}
for y,d in T.items():
    gys=[]
    for g,l in d.items():
        iys=[]
        for i in l:
            Y=-row*0.46; iys.append(Y); row+=1
        gys.append((g,l,iys,sum(iys)/len(iys)))
    yy[y]=(gys,sum(g[3] for g in gys)/len(gys))
rootY=sum(v_[1] for v_ in yy.values())/len(yy)
o.append(f'\\node[font=\\small\\bfseries,fill=yellow!30,draw,rounded corners=2pt,inner sep=3pt] (r) at (0,{rootY:.2f}) {{Menü}};')
for y,(gys,ym) in yy.items():
    c=col[y]
    o.append(f'\\node[font=\\footnotesize\\bfseries,text={c}] (y{y}) at (1.7,{ym:.2f}) {{{y}}}; \\draw[{c},thick] (r) -- (y{y}.west);')
    for g,l,iys,gm in gys:
        o.append(f'\\node[font=\\footnotesize,text={c}] (g{y}{g}) at (4.0,{gm:.2f}) {{{g}}}; \\draw[{c},thick] (y{y}.east) -- (g{y}{g}.west);')
        for i,Y in zip(l,iys):
            o.append(f'\\node[font=\\footnotesize,anchor=west] (i{y}{g}{i}) at (5.7,{Y:.2f}) {{{i}}}; \\draw[{c},thick] (g{y}{g}.east) -- (i{y}{g}{i}.west);')
SK=fig('\n'.join(o))
q('0008',tipId='pr-sayma',tip='Toplama ve çarpma kuralı',z='orta',alt='Ağaç Şeması',kaz='Ağaç şemasında koşullu dallanmaları sayarak belirli bir koşulu sağlayan seçenek sayısını bulur.',kalip='hikâyeli',
 kart='K-APER-01 (ağaç şeması) · üç aşamalı menü; dallar eşit değil; bir içeceğin olmadığı menüler',
 metin='Bir lokantada menü; önce ana yemek, sonra garnitür, en sonunda içecek seçilerek oluşturuluyor. Her ana yemekle sunulan garnitürler ve her garnitürle sunulan içecekler şekildeki ağaç şemasında verilmiştir. Eda, ayranı hiç sevmemektedir.\nBuna göre Eda, içeceği ayran olmayan kaç farklı menü seçebilir?',
 dogru=v,yan=[(e[0],'İçecek koşulunu uygulamadan şemadaki bütün yolları saymış.','dikkat'),(e[1],'Ayranlı menü olarak yalnız Balık dalındaki tek menüyü sayıp diğer ayranlı yolları atlamış: 13 − 1.','dikkat'),(e[2],'Balık dalında üç içeceğin hepsini saymış; diğer çiftlerde yalnız Su’yu almış: 5 × 1 + 3.','dikkat'),(e[3],'Ayranlı menüleri 3 sanıp (ana yemek sayısı kadar) toplamdan çıkarmış: 13 − 3.','islem')],
 istenen='İçeceği ayran olmayan menü sayısı.',ip=['Şemada ayranın bulunduğu dalları ayrı ayrı say; hangi çiftlerde ayran dışında kaç içecek var?'],bilgi=[SAY,TOP],sekil=SK,
 ad=[A('Tüm menüleri say','Her yol bir menüdür; yollar son aşamadaki içecek sayısı kadardır.','5 çiftte 2 içecek, 1 çiftte 3 içecek: 5 × 2 + 3 = 13'),A('Ayranlı menüleri say','Her ana yemek–garnitür çiftinin altında bir ayran bulunur.','6 çift → 6 ayranlı menü'),A('Çıkar','Tüm menülerden ayranlı olanlar çıkarılır.','13 − 6 = 7'),A('Kontrol et','Ayransız menüler 6 Su’lu menü ile Balık–Salata dalındaki Limonata’lı menüden oluşur.','6 + 1 = 7')],
 puf='Şemada koşulu sağlayan yolları tek tek saymak yerine tüm yollardan koşulu bozanları çıkarmak çoğu zaman daha güvenlidir.')

# ================= 09 orta · öncüllü, rakamlardan sayı =================
S9=[a*1000+b*100+c*10+d for a,b,c,d in permutations(range(6),4) if a!=0]
n_top=len(S9); n_cift=sum(1 for x in S9 if x%2==0); n_bes=sum(1 for x in S9 if x%5==0)
assert (n_top,n_cift,n_bes)==(300,156,108)
assert n_top//2==150 and n_top//5==60 and 6*5*4*3==360 and 5*4*3==60
sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
q('0009',tipId='pr-sayiyaz',tip='Rakamlardan sayı yazma',z='orta',alt='Sayı Yazma',kaz='Verilen rakamlarla rakamları farklı dört basamaklı sayılarla ilgili üç sayma iddiasını baştaki sıfır ve koşullu basamak durumlarını ayırarak sınar.',kalip='öncüllü',
 kart='K-APER-07 (rakamlı sayma yargıları) · rakamları farklı 4 basamaklı sayı; toplam, çift, 5’e bölünen',
 metin='0, 1, 2, 3, 4 ve 5 rakamlarıyla, rakamları birbirinden farklı dört basamaklı doğal sayılar yazılıyor.\nBu sayılarla ilgili,\nI. Toplam 300 tanedir.\nII. Çift olanların sayısı 156’dır.\nIII. 5 ile tam bölünenlerin sayısı 108’dir.\nyargılarından hangileri doğrudur?',
 dogru='I, II ve III',sira=sira,yan=[('Yalnız I','Çift sayıları toplamın yarısı, 5’e bölünenleri toplamın beşte biri sanmış: 300/2 = 150 ve 300/5 = 60; II ve III’ü yanlış bulmuş.','bilgi'),('I ve II','5 ile bölünenleri yalnız sonu 0 olan sayılar sanıp 5 × 4 × 3 = 60 bulmuş; III’ü yanlış bulmuş. I ve II’yi doğru sınamış.','bilgi'),('I ve III','Çift sayıların sayısını toplamın yarısı sanıp 300/2 = 150 bulmuş; II’yi yanlış bulmuş. I ve III’ü doğru sınamış.','bilgi'),('II ve III','Binler basamağında 0’ı da kullanıp 6 × 5 × 4 × 3 = 360 bulmuş; I’i yanlış bulmuş. II ve III’ü doğru sınamış.','dikkat')],
 istenen='Doğru olan yargıların hangileri olduğu.',ip=['Birler basamağı koşullu olduğundan onu önce doldur; binler basamağındaki 0 yasağına dikkat et.'],bilgi=[SAYI],
 ad=[A('I’i say','Binler basamağı 0 olamaz; sonra yüzler, onlar ve birler kalan rakamlardan seçilir.','5 × 5 × 4 × 3 = 300 → doğru'),A('II’yi say','Birler basamağı 0 ise 5 × 4 × 3 = 60 sayı vardır. Birler basamağı 2 ya da 4 ise binler basamağı 0 ve birler basamağındaki rakam dışında 4 rakamdan, yüzler ve onlar basamakları kalanlardan seçilir.','60 + 2 × (4 × 4 × 3) = 156 → doğru'),A('III’ü say','Sonu 0 olanlar 5 × 4 × 3 = 60; sonu 5 olanlarda binler basamağı 0 olamayacağından 4 × 4 × 3 = 48 sayı vardır.','60 + 48 = 108 → doğru'),A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],
 puf='Sayı sayarken baştaki sıfırı ayrı bir durum olarak düşün; koşullu basamağı önce doldur.')

# ================= 10 orta · nokta kümesi, üçgen sayısı =================
from fractions import Fraction as Fr
D=[(Fr(i),Fr(0)) for i in range(5)]; Ot=[(Fr(-1),Fr(2)),(Fr(1),Fr(2)),(Fr(3),Fr(2))]
NK=D+Ot
def dogrusal(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])==0
dg=[t for t in combinations(NK,3) if dogrusal(*t)]; assert len(dg)==comb(5,3)+1 and all(all(p in D for p in t) or all(p in Ot for p in t) for t in dg)
v=sum(1 for t in combinations(NK,3) if not dogrusal(*t)); assert v==45==comb(8,3)-comb(5,3)-1
e=[comb(8,3)-comb(5,3),comb(8,3)-1,comb(8,3),8*7*6]; assert e==[46,55,56,336]; dist(v,e)
o=['\\draw[thick,blue!60!black] (-1.4,0) -- (4.6,0); \\node[right,font=\\normalsize\\bfseries] at (4.6,0) {$d$};','\\draw[thick,orange!80!black] (-1.4,2) -- (3.6,2); \\node[right,font=\\normalsize\\bfseries] at (3.6,2) {$e$};']
for x,y in D: o.append(f'\\fill[blue!70!black] ({float(x)},{float(y)}) circle (0.1);')
for x,y in Ot: o.append(f'\\fill[orange!90!black] ({float(x)},{float(y)}) circle (0.1);')
SK=fig('\n'.join(o))
q('0010',tipId='pr-geometri',tip='Geometrik nesnelerle sayma',z='orta',alt='Noktalardan Üçgen',kaz='Düzlemde verilen noktalardan, iki ayrı doğru üzerindeki doğrusal üçlüleri ayırarak çizilebilecek üçgen sayısını hesaplar.',kalip='şekilli',
 kart='K-APER-08 (nokta kümesi) · iki doğru üzerinde çok nokta; üçgen sayısı',
 metin='Düzlemde, şekilde işaretlenmiş 8 nokta verilmiştir. Bu noktalardan d doğrusu üzerinde bulunanlar ile e doğrusu üzerinde bulunanlar dışında hiçbir üç nokta aynı doğru üzerinde değildir.\nBuna göre köşeleri bu noktalardan seçilen kaç farklı üçgen çizilebilir?',
 dogru=v,yan=[(e[0],'Yalnız d üzerindeki doğrusal üçlüleri çıkarmış; e üzerindeki üçlüyü unutmuş: 56 − 10 = 46.','dikkat'),(e[1],'Yalnız e üzerindeki üçlüyü çıkarmış; d üzerindeki 10 üçlüyü unutmuş: 56 − 1 = 55.','dikkat'),(e[2],'Doğrusal üç nokta seçimlerini de üçgen sayıp koşulu uygulamamış: C(8, 3).','dikkat'),(e[3],'Köşelerin sırasını da ayırt edip 8 × 7 × 6 hesaplamış.','bilgi')],
 istenen='Çizilebilen üçgenlerin sayısı.',ip=['Seçilen üç noktanın üçgen oluşturamadığı durumlar şekilde nerelerde görülüyor?'],bilgi=[GEO],sekil=SK,
 ad=[A('Tüm üçlüleri say','8 noktadan seçilen her üç nokta bir üçlüdür.','C(8, 3) = 56'),A('Üçgen olmayanları say','d üzerindeki 5 noktadan ve e üzerindeki 3 noktadan seçilen üçlüler doğrusaldır.','C(5, 3) = 10 · C(3, 3) = 1'),A('Çıkar','Doğrusal üçlüler üçgen oluşturmaz.','56 − 10 − 1 = 45')],
 puf='Geometrik sayma sorularında önce tüm seçimleri say, sonra şekil oluşturmayanları ayır.')

# ================= 11 orta · bölge boyama =================
kom={('M','K'),('M','L'),('M','N'),('M','P'),('K','L'),('L','N'),('N','P'),('P','K')}
bol=['M','K','L','N','P']
def boya(k): return sum(1 for c in product(range(k),repeat=5) if all(c[bol.index(a)]!=c[bol.index(b)] for a,b in kom))
v=boya(4); assert v==72==4*18
e=[18,4*(3-1)**4,4*3*2*2*2,4*3**4]; assert e==[18,64,96,324]; dist(v,e)
o=['\\draw[thick,fill=gray!12] (0,0) rectangle (4,4);','\\draw[thick,fill=gray!12] (1.3,1.3) rectangle (2.7,2.7);']
for a,b in (((0,0),(1.3,1.3)),((4,0),(2.7,1.3)),((4,4),(2.7,2.7)),((0,4),(1.3,2.7))): o.append(f'\\draw[thick] {a} -- {b};')
for n,(x,y) in {'K':(2,3.4),'L':(3.4,2),'N':(2,0.6),'P':(0.6,2),'M':(2,2)}.items(): o.append(f'\\node[font=\\large\\bfseries] at ({x},{y}) {{{n}}};')
o.append('\\draw[blue!60!black,line width=2.2pt] (0,0) rectangle (4,4);')
SK=fig('\n'.join(o))
q('0011',tipId='pr-boyama',tip='Bölge boyama',z='orta',alt='Bölge Boyama',kaz='Komşuluk kuralına göre bölgeleri sırayla boyayarak renk seçimlerinin sayısını bulur.',kalip='yeni nesil',
 kart='K-APER-09 (merkez bölge ve çevresi) · merkez herkesle komşu, çevre bölgeler halka',
 metin='Şekildeki K, L, M, N ve P bölgelerinin her biri, 4 farklı renkten biriyle boyanacaktır. Ortak bir sınır çizgisi bulunan bölgeler komşudur ve komşu bölgeler aynı renkle boyanamaz. Yalnız bir noktada buluşan bölgeler komşu sayılmaz. Her bölge tek renkle boyanacak, her rengin kullanılması zorunlu değildir.\nBuna göre bu boyama kaç farklı biçimde yapılabilir?',
 dogru=v,yan=[(e[0],'Ortadaki bölgenin rengini seçmeyi unutup yalnız çevre halkasını boyamış: (3 − 1)⁴ + (3 − 1) = 18.','dikkat'),(e[1],'Çevredeki dört bölgeyi 3 renkle halka olarak boyarken kapanış düzeltmesini unutmuş: 4 × (3 − 1)⁴ = 64.','islem'),(e[2],'Çevre bölgeleri sırayla boyayıp dördüncü bölgeyi birinci bölgeyle de komşu olduğunu görmeden 2 seçenekle bırakmış: 4 × 3 × 2 × 2 × 2.','dikkat'),(e[3],'Çevre bölgelerin yalnız merkezle komşu olduğunu, birbirleriyle komşu olmadığını sanmış: 4 × 3 × 3 × 3 × 3.','bilgi')],
 istenen='Bölgeleri boyamanın farklı yollarının sayısı.',ip=['En çok komşusu olan bölgeden başlayıp kalan renklerle çevre bölgeleri boyamayı dene.'],bilgi=[BOY],sekil=SK,
 ad=[A('Komşulukları yaz','M, K, L, N ve P’nin hepsiyle komşudur; K–L, L–N, N–P, P–K komşudur; K–N ve L–P komşu değildir.','M merkez; K, L, N, P halka'),A('Merkezi boya','M’ye 4 renkten biri verilir; çevre bölgeler için 3 renk kalır.','4 seçenek'),A('Halkayı boya','K ve N aynı renkteyse L ve P’nin her biri 2 renkten birini alır; K ve N farklıysa L ve P’nin her biri 1 renk alır.','K = N: 3 × 2 × 2 = 12 · K ≠ N: 3 × 2 × 1 × 1 = 6 → 18'),A('Çarp','Merkez ve halkanın boyamaları çarpılır.','4 × 18 = 72')],
 puf='Bölge boyamada komşuluk çizelgesini çıkar ve en çok komşusu olan bölgeyi önce boya.')

# ================= 12 orta · Venn, komite =================
ses=[('s',i) for i in range(4)]; bil=[('b',i) for i in range(5)]; ik=[('i',i) for i in range(3)]
kul=ses+bil+ik; sat=set(ses+ik); bs=set(bil+ik)
v=sum(1 for c in combinations(kul,3) if any(x in sat for x in c) and any(x in bs for x in c)); assert v==206==comb(12,3)-comb(5,3)-comb(4,3)
e=[comb(12,3)-comb(5,3),comb(12,3)-comb(4,3),comb(12,3),7*8*10]; assert e==[210,216,220,560]; dist(v,e)
o=['\\fill[blue!45,opacity=.45] (0,0) circle (1.35);','\\fill[orange!55,opacity=.45] (1.7,0) circle (1.35);','\\draw[thick,blue!60!black] (0,0) circle (1.35);','\\draw[thick,orange!80!black] (1.7,0) circle (1.35);',
   '\\draw[thick] (-1.9,-1.9) rectangle (3.6,2.2);','\\node[anchor=south west,font=\\small] at (-1.85,-1.85) {Kulüp üyeleri};',
   '\\node[font=\\small\\bfseries,blue!50!black] at (-0.4,1.7) {Satranç}; \\node[font=\\small\\bfseries,orange!60!black] at (2.1,1.7) {Bilgisayar};',
   '\\node[font=\\Large\\bfseries] at (-0.55,0) {4}; \\node[font=\\Large\\bfseries] at (0.85,0) {3}; \\node[font=\\Large\\bfseries] at (2.25,0) {5};']
SK=fig('\n'.join(o))
q('0012',tipId='pr-secim',tip='Seçim, gruplama ve koşullu sayma',z='orta',alt='Koşullu Seçim',kaz='Venn şemasındaki gruplardan üç kişilik komiteyi, iki koşulun birlikte sağlanması istendiğinde tümleyen sayma ile bulur.',kalip='hikâyeli',
 kart='K-APER-10 (Venn şemalı komite) · iki özelliğin ikisi de komitede bulunsun',
 metin='Bir okuldaki kulübün 12 üyesinin her biri satranç oynamakta, bilgisayar bilmekte ya da ikisini birden yapmaktadır; şekildeki Venn şemasında her bölgedeki üye sayısı verilmiştir. Kulüp, üç üyeden oluşan bir turnuva komitesi kuracak; komitede satranç oynayan en az bir üye ve bilgisayar bilen en az bir üye bulunmasını istemektedir.\nBuna göre bu komite kaç farklı biçimde kurulabilir?',
 dogru=v,yan=[(e[0],'Satranç oynayan üyesi olmayan komiteleri (C(5, 3) = 10) çıkarmış; bilgisayar bilen üyesi olmayanları çıkarmayı unutmuş: 220 − 10 = 210.','dikkat'),(e[1],'Bilgisayar bilen üyesi olmayan komiteleri (C(4, 3) = 4) çıkarmış; satranç oynayan üyesi olmayanları çıkarmayı unutmuş: 220 − 4 = 216.','dikkat'),(e[2],'İki koşulu hiç uygulamadan 12 üyeden herhangi üçünü seçmiş: C(12, 3).','dikkat'),(e[3],'Önce bir satranççı (7), bir bilgisayarcı (8), sonra kalan 10 üyeden birini seçmiş; ortak seçimleri birçok kez saymış: 7 × 8 × 10.','bilgi')],
 istenen='İki koşulu birlikte sağlayan komite sayısı.',ip=['Koşulu bozan komitelerin hangi gruplardan oluşabileceğini düşün.'],bilgi=[KOM,TOP],sekil=SK,
 ad=[A('Tüm komiteleri say','12 üyeden herhangi üçü seçilir.','C(12, 3) = 220'),A('Satranççısız komiteleri say','Satranç oynayan üye olmaması için üç üyenin hepsi yalnız bilgisayar bilenlerden olmalıdır.','C(5, 3) = 10'),A('Bilgisayarcısız komiteleri say','Bilgisayar bilen üye olmaması için üç üyenin hepsi yalnız satranç oynayanlardan olmalıdır.','C(4, 3) = 4'),A('Çıkar','İki istenmeyen durum aynı anda gerçekleşemez, ayrıca çıkarılır.','220 − 10 − 4 = 206')],
 puf='“En az bir …, en az bir …” koşulunda her koşulu bozan durumları ayrı say; aynı anda bozulamıyorsa ayrı ayrı çıkar.')

# ================= 13 orta · öncüllü, ızgara, noktalardan geçen yollar =================
Pn=(2,2); Qn=(1,3)
tum=yollar(4,4); gP=yollar(4,4,zorunlu=Pn); gQ=yollar(4,4,zorunlu=Qn)
assert (tum,gP,gQ)==(70,36,16)
assert yollar(4,4,yasak=[Pn,Qn])==70-36-16==18
assert 6+6==12 and 4+4==8 and 70-12-8==50 and 70-36==34
sira=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
SK=fig(grid(4,4,pts={'P':(Pn,'orange!90!black'),'Q':(Qn,'violet')},sc=0.75))
q('0013',tipId='pr-izgara',tip='Izgarada en kısa yol',z='orta',alt='Izgara ve Ara Noktalar',kaz='Izgarada ara noktalardan geçen ve geçmeyen en kısa yolların sayısıyla ilgili yargıları sınar.',kalip='öncüllü',
 kart='K-APER-03 (ara noktalı ızgara) · iki ara nokta; geçen, geçmeyen yol yargıları',
 metin='Şekildeki sokak ağında A noktasından B noktasına, yalnızca sağa ya da yukarıya giderek en kısa yollarla ulaşılacaktır.\nBu en kısa yollarla ilgili,\nI. P noktasından geçenlerin sayısı 12’dir.\nII. Q noktasından geçenlerin sayısı 16’dır.\nIII. Ne P’den ne de Q’dan geçmeyenlerin sayısı 34’tür.\nyargılarından hangileri doğrudur?',
 dogru='Yalnız II',sira=sira,yan=[('Yalnız I','Parçaları çarpmak yerine toplamış: P için 6 + 6 = 12, Q için 4 + 4 = 8; III’te 70 − 12 − 8 = 50 bulup III’ü de yanlış saymış. Yalnız I’i doğru bulmuş.','bilgi'),('I ve II','P noktasında parçaları çarpmak yerine toplamış: 6 + 6 = 12; I’i doğru bulmuş. II ve III’ü doğru değerlendirmiş.','islem'),('II ve III','Ne P’den ne de Q’dan geçmeyenleri bulurken yalnız P’den geçenleri çıkarmış: 70 − 36 = 34; III’ü doğru bulmuş.','dikkat'),('I, II ve III','Hem P’de çarpma yerine toplama (6 + 6 = 12) hem de III’te yalnız P’den geçenleri çıkarma (70 − 36 = 34) hatası yapmış.','bilgi')],
 istenen='Doğru olan yargıların hangileri olduğu.',ip=['Bir noktadan geçen yolların sayısı iki parçanın sayısıyla nasıl bulunur?'],bilgi=[IZG],sekil=SK,
 ad=[A('Tüm yolları say','A’dan B’ye 4 sağa, 4 yukarı adım vardır.','C(8, 4) = 70'),A('P’den geçenleri say','A’dan P’ye 2 sağa 2 yukarı, P’den B’ye de 2 sağa 2 yukarı gidilir; parçalar çarpılır.','C(4, 2) × C(4, 2) = 36 ≠ 12 → I yanlış'),A('Q’dan geçenleri say','A’dan Q’ya 1 sağa 3 yukarı, Q’dan B’ye 3 sağa 1 yukarı gidilir.','C(4, 1) × C(4, 1) = 16 → II doğru'),A('Geçmeyenleri say','P ve Q’dan aynı anda geçilemez (Q, P’nin sol üstündedir); iki sayı ayrı çıkarılır.','70 − 36 − 16 = 18 ≠ 34 → III yanlış')],
 puf='Bir noktadan geçen yolları parçalara bölüp çarp; hem “geçen” hem “geçmeyen” yargılarında aynı sayılardan yararlan.')

# ================= 14 orta · bloklaştırma, ders kitapları =================
gr=[0]*4+[1]*3+[2]*2
sayac=0
for p in permutations(range(9)):
    L_=[gr[i] for i in p]
    if sum(1 for a_,b_ in zip(L_,L_[1:]) if a_!=b_)==2 and L_[0]!=2: sayac+=1
v=4*F(4)*F(3)*F(2); assert sayac==v==1152
e=[288,576,864,1728]; assert 4*3*2*1*3*2*1*2*1==288 and 2*288==576 and 3*288==864 and 6*288==1728; dist(v,e)
o=[]; cols={'Matematik':('blue!55',4),'Fizik':('orange!70',3),'Kimya':('green!55',2)}
for k,(ad_,(c,n)) in enumerate(cols.items()):
    x=k*2.5
    for i in range(n): o.append(f'\\draw[thick,fill={c}] ({x},{i*0.3}) rectangle ({x+1.7},{i*0.3+0.26});')
    o.append(f'\\node[font=\\small\\bfseries] at ({x+0.85},-0.35) {{{ad_}}};')
SK=fig('\n'.join(o))
q('0014',tipId='pr-siralama',tip='Tekrarlı dizilişler ve bloklaştırma',z='orta',alt='Bloklaştırma',kaz='Aynı derse ait kitapların yan yana bulunması koşulunda önce blokları, sonra blok içlerini sıralar.',kalip='hikâyeli',
 kart='K-APER-05 (bloklu dizilim) · üç gruptan 9 farklı kitap; gruplar kendi içinde bitişik',
 metin='Bir öğrenci, şekilde yığınlar hâlinde gösterilen 9 kitabı (kitapların hepsi birbirinden farklıdır) bir rafa soldan sağa dizecektir. Aynı derse ait kitapların raf üzerinde yan yana bulunmasını ve Kimya kitaplarının rafın en solunda yer almamasını istemektedir.\nBuna göre bu kitaplar rafa kaç farklı biçimde dizilebilir?',
 dogru=v,yan=[(e[0],'Blokların kendi aralarındaki sıralamasını hiç saymamış; yalnız blok içlerini saymış: 4! × 3! × 2!.','dikkat'),(e[1],'Kimya bloğunun yerini (2 seçenek) unutup diğer iki bloğu 2! ile sıralamış: 2 × 4! × 3! × 2! = 576.','dikkat'),(e[2],'Blokların sırası için 3! yerine 3 almış: 3 × 4! × 3! × 2! = 864.','islem'),(e[3],'Kimya bloğunun en solda olmaması koşulunu uygulamamış: 3! × 4! × 3! × 2! = 1728.','dikkat')],
 istenen='Koşulları sağlayan dizilişlerin sayısı.',ip=['Aynı derse ait kitapların konumu hakkında ne söyleyebilirsin?'],bilgi=[BLK],sekil=SK,
 ad=[A('Blok sırasını say','Matematik, Fizik ve Kimya blokları sıralanır; Kimya bloğu en solda olamaz, ortada ya da sağda olabilir.','Kimya: 2 yer · diğer iki blok: 2! → 2 × 2 = 4'),A('Blok içlerini say','Her blok içinde kitaplar farklıdır ve kendi aralarında sıralanır.','4! = 24 · 3! = 6 · 2! = 2'),A('Çarp','Blokların sıralaması ve blok içi sıralamalar çarpılır.','4 × 24 × 6 × 2 = 1152')],
 puf='Bitişik olması istenenleri blok yap; sayıyı hem bloklar arasında hem blok içinde say.')

OTU=B('Numaralı koltuklarda oturma','koltuklar numaralıysa dönmeyle elde edilen düzenler de ayrı sayılır; n kişi n numaralı koltuğa n! biçimde oturur. Bir çemberde “yan yana” komşu numaraları, “karşılıklı” n/2 numara farkını anlatır. Örnek: 6 koltukta 2 numaralı koltuğun komşuları 1 ve 3, karşısındaki 5’tir')

# ================= 15 zor · sabit sandalyeli masa, iki koşul =================
def say15(ab_adj=True,ab_opp=True,cd=True,cd_yon=False):
    t=0
    for p in permutations(range(8)):          # p[kisi] = koltuk; 0 Ali, 1 Berk, 2 Cem, 3 Duru
        d=lambda a,b:(p[a]-p[b])%8
        if ab_adj and d(0,1) in (1,7): continue
        if ab_opp and d(0,1)==4: continue
        if cd:
            if d(2,3) not in (1,7): continue
            if cd_yon and d(2,3)!=1: continue
        t+=1
    return t
v=say15(); e=[say15(True,False),say15(cd_yon=True),say15(False,False),say15(True,True,False)]
assert v==16*16*24==6144 and e==[16*20*24,8*16*24,16*30*24,8*4*F(6)] and e==[7680,3072,11520,23040]; dist(v,e)
SK=fig(masa(8,numara=True,r=1.2,rad=1.85))
q('0015',tipId='pr-dairesel',tip='Dairesel ve sabit sandalyeli oturma',z='zor',alt='Sabit Koltuklarda Oturma',kaz='Numaralı koltuklarda iki ayrı koşulu (yan yana olmama ve karşılıklı olmama; bitişik oturma) birlikte uygulayarak oturma düzenlerini sayar.',kalip='hikâyeli',
 kart='K-APER-04 (numaralı masa) · bir çift bitişik, bir çift ne bitişik ne karşılıklı',
 metin='Sekiz arkadaş, şekilde görülen, 1’den 8’e numaralanmış koltukları olan yuvarlak bir masaya oturacaktır; 1 ile 8 numaralı koltuklar da komşudur. Ali ile Berk ne komşu koltuklara ne de karşılıklı koltuklara oturmak istemektedir. Cem ile Duru ise komşu koltuklara oturmak istemektedir.\nBuna göre bu sekiz arkadaş koltuklara kaç farklı biçimde oturabilir?',
 dogru=v,yan=[(e[0],'Ali ile Berk için yalnız komşu koltukları yasaklamış, karşılıklı koltukları atlamıştır: 5 yasak çift yerine 7 yasak çift gerekirken sayı 16 × 20 × 24 olmuş.','dikkat'),(e[1],'Cem ile Duru’nun komşu koltuklarda iki farklı sırayla oturabileceğini unutmuş; yalnız bir yönü saymış: 8 × 16 × 24.','islem'),(e[2],'Ali–Berk koşulunu uygulamayıp yalnız Cem–Duru koşulunu saymış: 16 × 30 × 24.','dikkat'),(e[3],'Cem–Duru koşulunu uygulamayıp yalnız Ali–Berk koşulunu saymış: 8 × 4 × 6!.','dikkat')],
 istenen='İki koşulu birlikte sağlayan oturma düzenlerinin sayısı.',ip=['Önce bir koşullu çifti yerleştir; ikinci çift için kalan koltukların hangi çiftleri yasaklı?'],bilgi=[OTU,TOP],sekil=SK,
 ad=[A('Cem ile Duru’yu yerleştir','8 komşu koltuk çifti vardır; Cem ile Duru her çiftte iki farklı sırayla oturabilir.','8 × 2 = 16'),A('Ali ile Berk için çiftleri say','Kalan 6 koltukta Ali ve Berk 6 × 5 = 30 sıralı biçimde oturur. Bu koltuklarda komşu 5, karşılıklı 2 çift vardır; her çift iki sırayla oturur.','30 − 7 × 2 = 16'),A('Kalanları yerleştir','Diğer dört arkadaş kalan 4 koltuğa oturur.','4! = 24'),A('Çarp','Üç aşama çarpılır.','16 × 16 × 24 = 6144')],
 puf='İki koşullu çiftlerde önce kısıtı daha güçlü olan çifti yerleştir; sonra kalan koltuklardaki yasakları say.')

# ================= 16 zor · kapalı yollu ızgara =================
e1=((0,1),(1,1)); e2=((2,2),(2,3))
tum=yollar(4,5); a1=yollar(4,5,kapali=[e1]); a2=yollar(4,5,kapali=[e2]); v=yollar(4,5,kapali=[e1,e2])
assert (tum,a1,a2,v)==(126,91,90,67)
g1=1*comb(7,3); g2=comb(4,2)*comb(4,2); gb=1*2*6; assert (g1,g2,gb)==(35,36,12) and tum-g1-g2+gb==v and tum-g1-g2==55 and g1+g2-gb==59
e=[g1,g2,tum-g1-g2,g1+g2-gb]; assert e==[35,36,55,59]; dist(v,e)
SK=fig(grid(4,5,kapali=[e1,e2],sc=0.8))
q('0016',tipId='pr-izgara',tip='Izgarada en kısa yol',z='zor',alt='Kapalı Yollu Izgara',kaz='İki kapalı sokak bulunan ızgarada, kapalı yolları kullanan yolları ortak durum düzeltmesiyle çıkararak en kısa yol sayısını bulur.',kalip='hikâyeli',
 kart='K-APER-03 (kapalı sokaklı ızgara) · iki kapalı sokağı ortak kullanan yollar',
 metin='Bir sitenin sokakları şekildeki gibi birbirine dik ve eşit aralıklıdır. Yol çalışması nedeniyle × işaretli iki sokak parçası trafiğe kapatılmıştır. Bir servis aracı, A noktasından B noktasına yalnızca sağa ya da yukarıya doğru, kapalı parçalara hiç girmeden ilerleyecektir.\nBuna göre servis aracı A’dan B’ye en kısa yoldan kaç farklı biçimde gidebilir?',
 dogru=v,yan=[(e[0],'İstenen yerine yalnız alttaki kapalı parçayı kullanan yolları saymış: 1 × 35 = 35.','dikkat'),(e[1],'İstenen yerine yalnız üstteki kapalı parçayı kullanan yolları saymış: 6 × 6 = 36.','dikkat'),(e[2],'Kapalı parçaları kullanan yolları 35 ve 36 diye ayrı ayrı çıkarmış; iki parçayı birlikte kullanan 12 yolu iki kez çıkarmış: 126 − 35 − 36.','dikkat'),(e[3],'Çıkarılacak yolların sayısını (35 + 36 − 12 = 59) bulmuş ama bunu tüm yollardan çıkarmayı unutmuş.','dikkat')],
 istenen='Kapalı parçalara girmeden A’dan B’ye en kısa yolların sayısı.',ip=['Kapalı parçalar yolların sayısını nasıl azaltır?'],bilgi=[IZG,TOP],sekil=SK,
 ad=[A('Tüm yolları say','4 sağa, 5 yukarı adım vardır.','C(9, 4) = 126'),A('Soldaki kapalı parçayı say','Parçaya kadar 1 yol, parçadan sonra B’ye 3 sağa 4 yukarı adım vardır.','1 × C(7, 3) = 35'),A('Üstteki kapalı parçayı say','Parçaya kadar 2 sağa 2 yukarı, parçadan sonra B’ye 2 sağa 2 yukarı adım vardır.','C(4, 2) × C(4, 2) = 36'),A('Ortak yolları bul','İki parçayı birlikte kullanan yollar önce soldaki parçaya, sonra 2 yolla üstteki parçaya ulaşır, ardından 6 yolla B’ye gider.','1 × 2 × 6 = 12'),A('Çıkar','Ortak durumlar bir kez çıkarılır.','126 − (35 + 36 − 12) = 67')],
 puf='İki “yasak” durumu çıkarırken ikisinin ortak durumlarını iki kez çıkarmadığından emin ol.')

# ================= 17 zor · adsız gruplara ayırma =================
ogr=list(range(9)); AA,BB,CC=0,1,2
def bolum(l):
    if not l: yield []; return
    a=l[0]
    for r in combinations(l[1:],2):
        g=frozenset((a,)+r); kal=[x for x in l if x not in g]
        for b in bolum(kal): yield [g]+b
B_=[frozenset(map(frozenset,b)) for b in bolum(ogr)]; assert len(set(B_))==280
v=sum(1 for b in set(B_) if any(AA in g and BB in g and CC not in g for g in b)); assert v==60==6*comb(6,3)//2
e=[7*comb(6,3)//2,6*comb(6,3),280,F(9)//(F(3)**3)]; assert e==[70,120,280,1680]; dist(v,e)
q('0017',tipId='pr-secim',tip='Seçim, gruplama ve koşullu sayma',z='orta',alt='Gruplara Ayırma',kaz='Adlandırılmamış eşit gruplara ayırmada iki öğrencinin aynı grupta, üçüncünün farklı grupta olması koşulunu sayar.',kalip='hikâyeli',
 kart='K-APER-10 (adsız eşit gruplar) · iki kişi birlikte, bir kişi ayrı',
 metin='Bir okulun doğa kulübündeki dokuz öğrenci, üçerli üç gruba ayrılarak kamp çalışmasına gidecektir. Gruplar adlandırılmamıştır; yani grupların kendi aralarındaki sırası ve adı önemli değildir. Ada ile Barış’ın aynı grupta olması, Ceren’in ise onlarla aynı grupta olmaması istenmektedir.\nBuna göre bu öğrenciler kaç farklı biçimde gruplandırılabilir?',
 dogru=v,yan=[(e[0],'Ada ile Barış’ın grubunun üçüncü üyesini Ceren dahil 7 öğrenci arasından seçmiş; Ceren’in ayrı olması koşulunu uygulamamış: 7 × 10 = 70.','dikkat'),(e[1],'Kalan altı öğrenciyi iki adsız gruba ayırırken eşit iki grubun yer değiştirmesini ayrı saymış: 6 × 20 = 120.','bilgi'),(e[2],'Hiçbir koşul uygulamadan dokuz öğrenciyi adsız üç gruba ayıran toplam sayıyı yazmış: 9!/(3!)⁴ = 280.','dikkat'),(e[3],'Gruplar adlandırılmamışken gruplara ad verilmiş gibi saymış: 9!/(3!)³ = 1680.','bilgi')],
 istenen='Koşulları sağlayan gruplandırmaların sayısı.',ip=['Ada ile Barış’ın grubunu belirleyen şey nedir? Geri kalan altı öğrenci iki adsız gruba nasıl ayrılır?'],bilgi=[GRP],
 ad=[A('Ada ile Barış’ın grubunu kur','Üçüncü üye Ceren olamaz; Ada, Barış ve Ceren dışındaki 6 öğrenciden biri seçilir.','6 seçenek'),A('Kalan 6 öğrenciyi ayır','Kalan altı öğrenci, adsız iki gruba üçerli ayrılır; seçilen üçlü ile kalan üçlü aynı bölünmeyi verir.','C(6, 3)/2! = 10'),A('Çarp','İki aşama çarpılır.','6 × 10 = 60')],
 puf='Adsız grupları sayarken, aynı büyüklükteki gruplar için yer değiştirme sayısına bölmeyi unutma.')

# ================= 18 zor · düzgün dokuzgen, kenarsız üçgen =================
import math
def kenarli(a,b): return (a-b)%9 in (1,8)
v=sum(1 for t in combinations(range(9),3) if not any(kenarli(a,b) for a,b in combinations(t,2))); assert v==30==9*5*4//6
c84=comb(9,3); e=[c84-9*7,c84-9,c84,30*6]; assert e==[21,75,84,180]; dist(v,e)
o=[]; 
for i in range(9):
    a=math.pi/2+2*math.pi*i/9; o.append((1.9*math.cos(a),1.9*math.sin(a),a))
pl=' -- '.join(f'({x:.3f},{y:.3f})' for x,y,_ in o)
body=f'\\draw[thick,fill=green!18] {pl} -- cycle;\n'
for i,(x,y,a) in enumerate(o):
    body+=f'\\fill[blue!60!black] ({x:.3f},{y:.3f}) circle (0.09); \\node[font=\\small\\bfseries] at ({2.28*math.cos(a):.3f},{2.28*math.sin(a):.3f}) {{{i+1}}};\n'
SK=fig(body)
q('0018',tipId='pr-geometri',tip='Geometrik nesnelerle sayma',z='zor',alt='Çokgenin Köşelerinden Üçgen',kaz='Düzgün çokgenin köşelerinden, hiçbir kenarı çokgenin kenarı olmayan üçgenlerin sayısını iki kenarlı üçgenleri ayırarak bulur.',kalip='yeni nesil',
 kart='K-APER-08 (çokgen köşeleri) · çokgenin kenarı olmayan üçgen; ortak durum düzeltmesi',
 metin='Şekildeki düzgün çokgenin köşeleri 1’den 9’a numaralanmıştır. Köşeleri bu çokgenin köşelerinden seçilen bir üçgenin hiçbir kenarı, çokgenin bir kenarı ile çakışmıyorsa bu üçgene “iç üçgen” denir.\nBuna göre kaç farklı iç üçgen çizilebilir?',
 dogru=v,yan=[(e[0],'Her kenar için o kenarı içeren 7 üçgeni çıkarmış: 84 − 9 × 7; iki kenarı çokgenin kenarı olan 9 üçgeni iki kez çıkarmış.','dikkat'),(e[1],'Çokgenin kenarlarını içeren üçgenleri kenar sayısı kadar, 9 tane saymış: 84 − 9.','dikkat'),(e[2],'Koşulu uygulamadan bütün üçgenleri saymış: C(9, 3).','dikkat'),(e[3],'Üç köşeyi sıralı seçmiş: 30 × 3! = 180.','islem')],
 istenen='İç üçgenlerin sayısı.',ip=['Çokgenin kenarını içeren üçgenleri sayarken her üçgenin kaç kez sayıldığına dikkat et.'],bilgi=[GEO,TOP],sekil=SK,
 ad=[A('Tüm üçgenleri say','Köşelerden herhangi üçü bir üçgen oluşturur.','C(9, 3) = 84'),A('Bir kenarı içerenleri say','Her kenar için üçüncü köşe kalan 7 köşeden seçilir.','9 × 7 = 63'),A('Ortak sayımı düzelt','İki kenarı çokgenin kenarı olan üçgenler (ardışık üç köşe) 63’te iki kez sayılmıştır; bunlar 9 tanedir.','En az bir kenarı çakışan: 63 − 9 = 54'),A('Çıkar','Tüm üçgenlerden kenarı çakışanlar çıkarılır.','84 − 54 = 30')],
 puf='Çıkarma yaparken iki koşulun birlikte sağlandığı durumları iki kez çıkarmadığından emin ol.')

# ================= 19 zor · öncüllü, komite =================
K9=[('K',i) for i in range(5)]; E9=[('E',i) for i in range(4)]; ZE=('K',0); AL=('E',0)
kur=list(combinations(K9+E9,4))
n1=sum(1 for c in kur if sum(1 for x in c if x[0]=='E')>=2); n2=sum(1 for c in kur if ZE in c and AL in c); n3=sum(1 for c in kur if sum(1 for x in c if x[0]=='K')>sum(1 for x in c if x[0]=='E'))
assert (n1,n2,n3)==(81,21,45)
assert comb(4,2)*comb(5,2)+comb(4,3)*5==80 and comb(5,3)*4==40 and perm(7,2)==42
sira=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III']
q('0019',tipId='pr-secim',tip='Seçim, gruplama ve koşullu sayma',z='zor',alt='Kurul Seçimi',kaz='Dört kişilik kurul seçiminde en az, birlikte bulunma ve çoğunluk koşullarını içeren üç sayma yargısını durumlara ayırarak sınar.',kalip='öncüllü',
 kart='K-APER-10 (kurul yargıları) · en az iki erkek, belirli iki kişi birlikte, kadın çoğunluğu',
 metin='Beş kadın ve dört erkek üyesi bulunan bir derneğin yönetim kurulu, bu dokuz üyeden seçilen dört kişiden oluşacaktır. Kadın üyelerden biri Zeynep, erkek üyelerden biri Ali’dir.\nBu kurul seçimiyle ilgili,\nI. Kurulda en az iki erkek bulunan seçimlerin sayısı 80’dir.\nII. Zeynep ile Ali’nin ikisinin de bulunduğu seçimlerin sayısı 21’dir.\nIII. Kurulda kadın sayısının erkek sayısından fazla olduğu seçimlerin sayısı 45’tir.\nyargılarından hangileri doğrudur?',
 dogru='II ve III',sira=sira,yan=[('Yalnız II','III’ü sayarken yalnız üç kadın–bir erkek durumunu (10 × 4 = 40) sayıp dört kadınlı kurulları (5) atlamış; III’ü yanlış bulmuş.','dikkat'),('Yalnız III','II’yi sayarken Zeynep ve Ali dışındaki iki üyeyi sıralı seçmiş: P(7, 2) = 42; II’yi yanlış bulmuş.','islem'),('I ve II','Son durumu atlama hatası yapmış: I’de dört erkekli kurulu atlayıp 80 bulmuş ve I’i doğru kabul etmiş; III’te dört kadınlı kurulu atlayıp 40 bulmuş ve III’ü yanlış kabul etmiş.','dikkat'),('I, II ve III','I’de dört erkekli kurulu (1 seçim) atlayıp 60 + 20 = 80 bulmuş ve I’i doğru kabul etmiş.','dikkat')],
 istenen='Doğru olan yargıların hangileri olduğu.',ip=['Her yargıyı ayrı hesapla; “en az” ve “fazla” koşullarında hangi kadın–erkek dağılımları mümkün, listele.'],bilgi=[KOM,TOP],
 ad=[A('I’i say','İki, üç ya da dört erkekli kurullar ayrı ayrı sayılır.','C(4,2)·C(5,2) + C(4,3)·C(5,1) + C(4,4) = 60 + 20 + 1 = 81 ≠ 80 → yanlış'),A('II’yi say','İkisi kurulda olduğundan kalan iki üye diğer yedi kişiden seçilir.','C(7, 2) = 21 → doğru'),A('III’ü say','Kadın çoğunluğu için 3 kadın + 1 erkek ya da 4 kadın gerekir.','C(5,3)·C(4,1) + C(5,4) = 40 + 5 = 45 → doğru'),A('Sonuç','II ve III doğrudur.','II ve III')],
 puf='“En az” ve “fazla” koşullarında olası bütün dağılımları (uç durumlar dahil) listele; sonra her birini sayıp topla.')

# ================= 20 zor · numaralı koltuk sırası, bozuk koltuklar =================
boz={3,7}; uy=[i for i in range(1,12) if i not in boz]
ks=[c for c in combinations(uy,4) if all(b-a>1 for a,b in zip(c,c[1:]))]
s=len(ks); v=s*F(4); assert (s,v)==(29,696)
assert 1*1*3+2*3*3+2*1*4==29
col6=comb(6,4)
e=[s,col6*24,comb(8,4)*24,comb(9,4)*24]; assert e==[29,360,1680,3024]; dist(v,e)
o=[]
for i in range(1,12):
    x=(i-1)*0.72
    if i in boz: o.append(f'\\draw[thick,fill=gray!45] ({x},0) rectangle ({x+0.62},0.62); \\node[font=\\Large\\bfseries,red!70!black] at ({x+0.31},0.31) {{$\\times$}}; \\node[font=\\small] at ({x+0.31},-0.32) {{{i}}};')
    else: o.append(f'\\draw[thick,fill=blue!16] ({x},0) rectangle ({x+0.62},0.62); \\node[font=\\small\\bfseries] at ({x+0.31},0.31) {{{i}}};')
SK=fig('\n'.join(o))
q('0020',tipId='pr-permutasyon',tip='Permütasyon ve sıralama koşulları',z='zor',alt='Koltuk Sırası',kaz='Bozuk koltukların bulunduğu numaralı bir sırada, bitişik oturmama koşuluyla dört kişinin yerleşimini blok blok sayar.',kalip='hikâyeli',
 kart='K-APER-02 (koltuk sırası) · bozuk koltuklar sırayı bloklara böler; bitişik oturmama',
 metin='Bir sinema salonunun arka sırasında, 1’den 11’e kadar numaralanmış koltuklar yan yana sıralanmıştır; şekilde × işaretli koltuklar bozuktur ve kullanılamamaktadır. Dört arkadaş (hepsi birbirinden farklı), kullanılabilir koltuklara birer kişi oturacak biçimde yerleşecektir. Numaraları ardışık olan iki koltuk bitişik sayılır ve arkadaşlardan hiçbir ikisi bitişik koltuklara oturmayacaktır.\nBuna göre bu dört arkadaş kaç farklı biçimde yerleşebilir?',
 dogru=v,yan=[(e[0],'Hangi koltukların seçildiğini bulup arkadaşların birbirinden farklı olduğunu unutmuş; 4! ile çarpmamış.','dikkat'),(e[1],'Bozuk koltukları sıradan çıkarıp kalan 9 koltuğu ardışık sanmış: C(6, 4) × 4! = 360.','bilgi'),(e[2],'Bozuk koltukları hiç dikkate almamış, 11 koltukta bitişik olmayan seçim yapmış: C(8, 4) × 4! = 1680.','dikkat'),(e[3],'Bitişik oturmama koşulunu atlayıp 9 kullanılabilir koltuktan 4’ünü seçmiş: C(9, 4) × 4! = 3024.','dikkat')],
 istenen='Dört arkadaşın koşulları sağlayan yerleşim sayısı.',ip=['Bozuk koltuklar, kullanılabilir koltukları hangi ardışık gruplara ayırıyor?'],bilgi=[KOM,PER],sekil=SK,
 ad=[A('Blokları belirle','Bitişiklik yalnızca ardışık kullanılabilir koltuklar arasında geçerlidir; üç ardışık blok oluşur.','{1, 2} · {4, 5, 6} · {8, 9, 10, 11}'),A('Blok sınırlarını yaz','Birinci blokta en çok 1, ikincide en çok 2, üçüncüde en çok 2 kişi bitişik olmadan oturabilir; 4 kişi için olası dağılımlar bulunur.','(0, 2, 2); (1, 1, 2); (1, 2, 1)'),A('Her dağılımı say','Bloklardaki bitişik olmayan seçimler: 2 koltukta 1 kişi: 2 yol; 3 koltukta 1 kişi: 3, 2 kişi: 1 yol; 4 koltukta 1 kişi: 4, 2 kişi: 3 yol.','1 × 1 × 3 = 3 · 2 × 3 × 3 = 18 · 2 × 1 × 4 = 8'),A('Koltuk kümelerini topla','Dağılımlar birbirinin yerine geçen durumlardır.','3 + 18 + 8 = 29'),A('Kişileri yerleştir','Seçilen 4 koltuğa dört farklı arkadaş oturur.','29 × 4! = 696')],
 puf='Sıradaki engeller (bozuk koltuk gibi) bitişiklik koşulunu bloklara böler; her bloğu ayrı say, sonra birleştir.')

# ---------- bitir: ayt-mat/perm-1.json ve kartlar/perm.json ----------
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(HD,'perm-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-perm.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2025 AYT Matematik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','perm.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
