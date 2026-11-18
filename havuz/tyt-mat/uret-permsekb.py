"""Permütasyon ve Kombinasyon · ŞEKİLLİ ek paket b (10 soru): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer kodla (kaba kuvvet/formül) assert edilir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians,comb,factorial as fa,prod
from itertools import product,permutations,combinations
H.KONU='Permütasyon ve Kombinasyon'
UK='matd|Permütasyon ve Kombinasyon'
P=Parti('permsekb','Permütasyon ve Kombinasyon',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu sayma soruları; yalnız mantık) · MEB 10. sınıf'
SP=[]
def spec(no,dogru,aday,**k): SP.append((no,dogru,aday,k))
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def olus(sp):
    """Her soruda doğru şıkkın sırası (A–E) kümesini hesaplar; harfleri 2'şer dağıtır; çeldirici listesini seçer."""
    import itertools
    fe=[]
    for no,d,ad,k in sp:
        assert len({d,*[a[0] for a in ad]})==len(ad)+1,no
        sm=sum(1 for a in ad if a[0]<d); lg=len(ad)-sm
        fe.append([r for r in range(5) if r<=sm and 4-r<=lg])
    sol=[None]
    def bt(i,cnt):
        if i==len(sp): sol[0]=list(cnt_l); return True
        for r in fe[i][i%len(fe[i]):]+fe[i][:i%len(fe[i])]:
            if cnt[r]<2:
                cnt[r]+=1; cnt_l.append(r)
                if bt(i+1,cnt): return True
                cnt[r]-=1; cnt_l.pop()
        return False
    cnt_l=[]; assert bt(0,[0]*5),fe
    return sol[0]

# ---------- bilgi kartları (örnekler soruların kurgusundan farklı) ----------
KOM=B('Kombinasyon','n elemanlı bir kümeden sırası önemsiz k eleman seçmenin yolu C(n, k) = n! / (k!(n − k)!) kadardır. Örnek: 6 renkli kalemden 2’sini seçmek C(6, 2) = 15 yoldur')
CAR=B('Çarpma ve toplama ilkesi','art arda ve birbirinden bağımsız adımların seçenek sayıları çarpılır; birbirinin yerine geçen ayrı durumların sayıları toplanır. Örnek: 3 gömlek ve 2 pantolonla 6 kıyafet; gömlek yerine ceket giyilecekse ayrı bir durum olarak toplanır')
KOS=B('Koşullu sayma','bir sayımda “şu özellikte olmayan”, “en az bir” gibi koşullar varsa tüm durumlar ile koşulu bozan durumlar ayrı sayılabilir. Örnek: 5 kişiden 2’si seçilirken belirli bir kişinin seçilmemesi, o kişiyi hariç tutup 4 kişiden seçmeye eşittir')
TEK=B('Tekrarlı permütasyon','n nesnenin n₁ tanesi birbirinin aynı, n₂ tanesi birbirinin aynı ise bunların sıralanış sayısı n! / (n₁! · n₂!)’dir. Örnek: ANA sözcüğündeki harflerin sıralanışı 3! / 2! = 3’tür')
SIF=B('Sayı yazarken basamak koşulları','baştaki basamak 0 olamaz, çift sayıda son basamak çifttir; kısıtlı basamaklar önce doldurulur. Örnek: 1, 2, 3 rakamlarıyla yazılabilen rakamları farklı üç basamaklı çift sayıların son basamağı 2’dir, 2 tane vardır')
NOK=B('Noktalardan şekil oluşturma','üçgenin köşeleri, bir doğru üzerinde bulunmayan üç noktadır; nokta seçimi sırasız olduğundan kombinasyonla sayılır. Örnek: hiçbir üçü doğrusal olmayan 5 noktadan 3 nokta seçmek C(5, 3) = 10 yoldur')
YOL=B('Yönlü yol sayısı','yönü olan bir şemada bir noktaya gelen yolların sayısı, o noktaya ok gönderen noktalara gelen yol sayılarının toplamıdır. Örnek: bir noktaya iki noktadan ok geliyor ve bunlara 4’er yol varsa orada 8 yol vardır')
ESL=B('Eşleştirme sayımı','bir kişi için yalnız belirli seçenekler uygunsa kişilerin seçenekleri birbirini etkiler; bir kişinin seçimi diğerlerinin seçenek kümesinden bir öğeyi çıkarır. Örnek: 3 kişi 3 koltuğa oturacaksa ilk kişinin seçimi kalan iki kişi için o koltuğu kullanılamaz yapar')
KUM=B('Gruplu seçim','her gruptan en az bir kişi koşulu, hangi gruptan kaç kişi alındığına göre durumlara ayrılarak sayılabilir; durumlar toplanır, her durumun içinde gruplar çarpılır. Örnek: iki gruptan toplam 3 kişi, her gruptan en az bir olacak biçimde seçilirken (1, 2) ve (2, 1) dağılımı ayrı durumlardır')
DIZ=B('Komşu olmayan seçim','iki öğenin komşu sayılması için yan yana (bir kenarı ortak) olması gerekir; komşu olmayan seçimler, öğelerin dizilişine göre sayılır. Örnek: 5 yan yana koltuktan komşu olmayan iki koltuk seçmek 6 yoldur')
SAY=B('Şekilde seçim sayma','çokgenlerde bir köşegen komşu olmayan iki köşeyi birleştirir; n köşeli çokgenin her köşesinden n − 3 köşegen çıkar. Örnek: 6 köşeli çokgenin her köşesinden 3 köşegen çıkar')

# ---------- kartlar ----------
kartla('K-PSB-01','Çokgende köşegen','Köşe çiftlerinden komşu olanlar ayrılır; belirli bir köşeden çıkan köşegenler ayrıca çıkarılır.','Kenarları da köşegen saymak; belirli köşeden çıkan sayıyı yanlış bulmak.','kolay','şekilli',3,'psb-geosay','Şekilde sayma (çokgen, ızgara, nokta ağı)')
kartla('K-PSB-02','Ağaç şeması','Şemadan ilk seçimin her dalındaki ikinci seçim sayısı okunur; yollar toplanır, sonraki seçimle çarpılır.','Her dalın sayısını aynı sanıp çarpmak; son seçimi atlamak.','kolay','şekilli',3,'psb-yol','Yollar ve dallanma şeması')
kartla('K-PSB-03','Izgarada dikdörtgen','Dikdörtgenin dört kenarı ızgara çizgilerinden seçilir; işaretli kareyi örtme koşulu çizgi seçeneklerini sınırlar.','Kareleri çizgi sanmak; yalnız bir doğrultuyu saymak.','orta','şekilli',4,'psb-geosay','Şekilde sayma (çokgen, ızgara, nokta ağı)')
kartla('K-PSB-04','Dilimlerden komşusuz seçim','Eksik dilimlerin oluşturduğu ayrı yaylar bulunur; her yayda ve yaylar arasında komşu olmayan seçimler sayılır.','Yenmiş dilimleri hâlâ orada sanmak; pizzayı bütün çember sanmak.','orta','şekilli',4,'psb-desen','Komşuluk koşullu desen ve seçim')
kartla('K-PSB-05','Lamba panosu','Arızalı lambalar çıkarılır; komşu olmayan lamba üçlüleri sistemli sayılır.','Arızalı lambaları saymak; komşuluğu yalnız yatay sanmak.','orta','şekilli',4,'psb-desen','Komşuluk koşullu desen ve seçim')
kartla('K-PSB-06','Rakam kartlarıyla sayı yazma','Tekrarlı kartlar ayırt edilemez; baştaki rakam 0 olamaz, son rakam çift olmalıdır.','Aynı kartları farklı sanmak; baştaki 0’ı unutmak.','orta','şekilli',4,'psb-sayi','Kartlarla sayı yazma')
kartla('K-PSB-07','Nokta ağında üçgen','Tüm üçlülerden aynı doğru üzerindeki üçlüler (yatay, dikey, çapraz) çıkarılır.','Çapraz doğruları unutmak.','zor','şekilli',5,'psb-geosay','Şekilde sayma (çokgen, ızgara, nokta ağı)')
kartla('K-PSB-08','Tablodan görev dağılımı','Kişilerin uygun görevleri tablodan okunur; en kısıtlı kişiden başlayarak dağılımlar sayılır.','Her kişinin seçeneklerini çarpmak; görevlerin tek kişiye gidebileceğini sanmak.','zor','tablo',5,'psb-esles','Kısıtlı eşleştirme')
kartla('K-PSB-09','Tablodan kurul seçimi','Tablodaki gruplardan ilk koşulu sağlayan seçimler sayılır; ikinci koşulu bozanlar çıkarılır.','Her sınıftan bir kişi seçip kalanı serbest bırakarak aynı kurulu birden çok kez saymak.','zor','tablo',5,'psb-secme','Gruplu kurul seçimi')
kartla('K-PSB-10','Yönlü yol şeması','Her noktaya gelen yol sayısı, ok gönderen noktaların toplamıdır; koşullu durumlar ayrı hesaplanır.','Yönü yok sayıp geri gitmek; koşulu yalnız birine uygulamak.','zor','şekilli',5,'psb-yol','Yollar ve dallanma şeması')

# ================= 01 kolay · köşegen =================
n=7
vert=list(range(n)); adjf=lambda a,b:(a-b)%n in (1,n-1)
v=sum(1 for a,b in combinations(vert,2) if not adjf(a,b) and 0 not in (a,b)); assert v==comb(n,2)-n-(n-3)==10
kos=sum(1 for a,b in combinations(vert,2) if not adjf(a,b)); assert kos==14
c=[(kos,'A direğine bağlanmama koşulunu atlamış: bütün köşegenleri saymış.','dikkat'),
   (comb(n-1,2),'A dışındaki 6 direk arasındaki bütün çiftleri saymış; kenarları da kablo sanmış: C(6, 2).','bilgi'),
   (kos-(n-2),'A’dan çıkan köşegen sayısını n − 2 = 5 sanıp çıkarmış: 14 − 5.','islem'),
   (kos-(n-1),'A’dan çıkan köşegen sayısını 6 sanıp çıkarmış (komşu iki direği de saymış): 14 − 6.','islem'),
   (comb(n,2),'Çit olan kenarları da kablo sanmış: C(7, 2).','dikkat'),
   (n-3,'Yalnız A’dan çıkacak köşegenleri sayıp cevap sanmış.','dikkat')]
o=[]; pts=[]
for i in range(n):
    a=radians(90-360*i/n); pts.append((2.0*cos(a),2.0*sin(a)))
o.append('\\draw[thick,fill=vurgu!10] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+' -- cycle;')
for i,(x,y) in enumerate(pts):
    a=radians(90-360*i/n); o.append(f'\\fill ({x:.3f},{y:.3f}) circle (0.08); \\node[font=\\normalsize\\bfseries] at ({2.5*cos(a):.3f},{2.5*sin(a):.3f}) {{{"ABCDEFG"[i]}}};')
SK=fig('\n'.join(o))
spec('0001',v,c,tipId='psb-geosay',tip='Şekilde sayma (çokgen, ızgara, nokta ağı)',z='kolay',alt='Çokgende Köşegen',kaz='Çokgenin köşe çiftlerinden komşu olmayanları ve belirli bir köşeden çıkanları ayırarak köşegen sayısını bulur.',kalip='hikâyeli',
 kart='K-PSB-01 (çokgen) · 7 köşe, A köşesinden çıkmayan köşegenler',
 metin='Bir bahçenin köşelerine, şekildeki gibi birer sulama direği dikilmiştir. Bahçenin kenarları boyunca direkler zaten çitle bağlıdır. Komşu olmayan her direk çifti arasına birer kablo çekilecektir; ancak A ile gösterilen direk arızalı olduğundan o direğe hiçbir kablo bağlanmayacaktır.\nBuna göre kaç tane kablo çekilir?',
 istenen='Çekilecek kablo sayısı.',ip=['Çitle zaten bağlı olan direk çiftleri hangileri?'],bilgi=[SAY],sekil=SK,
 ad=[A('Direk sayısı','Şekildeki çokgenin köşeleri sayılır.','7 direk'),A('Bütün kablolar','Komşu olmayan direk çiftleri, yani köşegenler sayılır.','C(7, 2) − 7 = 14'),A('A’ya bağlananlar','A’dan kendisi ve iki komşusu dışındaki 4 direğe kablo gidecekti.','7 − 3 = 4'),A('Çıkar','A’ya bağlanacak kablolar çekilmeyecektir.','14 − 4 = 10')],
 puf='Sayım bitince küçük bir durumla (ör. dörtgen) aynı yolu deneyip sonucu kontrol et.')

# ================= 02 kolay · ağaç şeması =================
dal=[3,2,4]; cay=2; v=sum(dal)*cay; assert v==18
yollar=[(a,b) for a,nb in enumerate(dal) for b in range(nb)]; assert len(yollar)*cay==v
c=[(sum(dal),'Çay seçimini atlamış: yalnız ana yemek–eşlikçi ikililerini saymış.','dikkat'),
   (len(dal)*max(dal)*cay,'Her ana yemekte en çok eşlikçi sayısı kadar dal olduğunu sanıp çarpmış: 3 × 4 × 2.','bilgi'),
   (prod(dal)*cay,'Dalları ayrı durumlar yerine art arda seçim sanıp çarpmış: 3 × 2 × 4 × 2.','bilgi'),
   (len(dal)+sum(dal)+cay,'Bütün sayıları toplamış: 3 + 9 + 2.','dikkat'),
   (len(dal)*sum(dal)*cay,'Ana yemek sayısını ikinci kez çarpmış: 3 × 9 × 2.','dikkat'),
   (sum(dal)*cay*cay,'Çay seçimini iki kez çarpmış: 9 × 2 × 2.','dikkat'),
   (len(dal)*min(dal)*cay,'Her ana yemekte en az eşlikçi sayısı kadar dal olduğunu sanıp çarpmış: 3 × 2 × 2.','bilgi'),
   (len(dal)*min(dal),'Her ana yemekte en az eşlikçi sayısı kadar dal sanmış ve çay seçimini atlamış: 3 × 2.','dikkat')]
o=['\\node[font=\\small\\bfseries] at (3.0,2.9) {Ana yemek}; \\node[font=\\small\\bfseries] at (6.6,2.9) {Eşlikçi};']
y=2.3; gy=[]; ly=[]
for nb in dal:
    ys=[y-0.55*i for i in range(nb)]; ly.append(ys); gy.append(sum(ys)/nb); y=ys[-1]-0.55-0.25
mid=(gy[0]+gy[-1])/2
o.append(f'\\node[draw,thick,circle,fill=white,inner sep=2pt] (R) at (0,{mid:.3f}) {{Seçim}};')
for i,(nm,ys) in enumerate(zip(['Omlet','Menemen','Kavurma'],ly)):
    o.append(f'\\node[draw,thick,fill=vurgu!12,minimum width=1.9cm,minimum height=0.55cm] (M{i}) at (3.0,{gy[i]:.3f}) {{{nm}}};')
    o.append(f'\\draw[thick] (R) -- (M{i});')
    for j,yy in enumerate(ys):
        o.append(f'\\node[draw,thick,circle,fill=white,minimum size=0.35cm,inner sep=0pt] (L{i}{j}) at (6.6,{yy:.3f}) {{}}; \\draw[thick] (M{i}) -- (L{i}{j});')
SK=fig('\n'.join(o))
spec('0002',v,c,tipId='psb-yol',tip='Yollar ve dallanma şeması',z='kolay',alt='Ağaç Şeması',kaz='Ağaç şemasında her dalın seçenek sayısını okuyup toplama ve çarpma ilkesini birlikte uygular.',kalip='hikâyeli',
 kart='K-PSB-02 (ağaç şeması) · dallar 3, 2, 4; çay 2',
 metin='Bir kafe, kahvaltı setini şekildeki şemaya göre hazırlıyor: önce bir ana yemek, sonra o ana yemekle birlikte sunulan eşlikçilerden biri seçiliyor; şemadaki her yol, seçilebilen bir ana yemek–eşlikçi ikilisidir. Seçilen her ikiliye ayrıca iki çeşit çaydan biri eklenecektir.\nBuna göre bu kafede kaç farklı kahvaltı seti hazırlanabilir?',
 istenen='Hazırlanabilecek farklı kahvaltı seti sayısı.',ip=['Şemadaki her yolun sonunda, çay için kaç seçenek açılıyor?'],bilgi=[CAR],sekil=SK,
 ad=[A('Dalları oku','Şemada her ana yemeğin altındaki eşlikçi sayısı okunur.','3, 2 ve 4 eşlikçi'),A('İkilileri say','Ana yemekler birbirinin yerine geçtiğinden eşlikçi sayıları toplanır.','3 + 2 + 4 = 9 ikili'),A('Çayı ekle','Her ikili için çay seçimi bağımsızdır.','9 × 2 = 18 set')],
 puf='Şemadaki bütün seçim aşamalarını çarpmadan önce tek tek listele.')

# ================= 03 orta · ızgarada dikdörtgen =================
C_,R_=5,4; ci,rj=2,3
def sayd(cl,rw):
    s=0
    for l,r in combinations(range(C_+1),2):
        for b,t in combinations(range(R_+1),2):
            if l<=ci-1 and r>=ci and b<=rj-1 and t>=rj: s+=1
    return s
v=sayd(C_,R_); assert v==ci*(C_-ci+1)*rj*(R_-rj+1)==48
tum=comb(C_+1,2)*comb(R_+1,2); assert tum==150
c=[(tum,'İşaretli kareyi örtme koşulunu atlamış: bütün dikdörtgenleri saymış: C(6, 2) × C(5, 2).','dikkat'),
   (ci*(C_-ci)*rj*(R_-rj),'Sağ ve üst kenar seçeneklerini birer eksik almış (4 yerine 3, 2 yerine 1): 2 × 3 × 3 × 1.','islem'),
   (ci*(C_-ci+1),'Yalnız sol ve sağ kenar seçimini saymış, alt ve üst kenarı atlamış: 2 × 4.','dikkat'),
   (ci*(C_-ci+1)*rj,'Üst kenar için seçenek saymamış: 2 × 4 × 3.','dikkat'),
   (ci*(C_-ci+1)*(R_-rj+1),'Alt kenar için seçenek saymamış: 2 × 4 × 2.','dikkat')]
u=1.0; o=[]
o.append(f'\\fill[vurgu!40] ({(ci-1)*u},{(rj-1)*u}) rectangle ({ci*u},{rj*u});')
for i in range(C_+1): o.append(f'\\draw[thick] ({i*u},0) -- ({i*u},{R_*u});')
for j in range(R_+1): o.append(f'\\draw[thick] (0,{j*u}) -- ({C_*u},{j*u});')
o.append(f'\\draw[thick,fill=vurgu!40] (0.0,-0.75) rectangle (0.4,-0.35); \\node[right] at (0.5,-0.55) {{: gider kapağı}};')
SK=fig('\n'.join(o))
spec('0003',v,c,tipId='psb-geosay',tip='Şekilde sayma (çokgen, ızgara, nokta ağı)',z='orta',alt='Izgarada Dikdörtgen',kaz='Izgara çizgilerinden dikdörtgenin kenarlarını seçerek işaretli kareyi örten dikdörtgenleri sayar.',kalip='hikâyeli',
 kart='K-PSB-03 (ızgara dikdörtgen) · 5 × 4 ızgara, işaretli kare',
 metin='Şekildeki zemin, birim karelerden oluşan dikdörtgen biçimli bir seramik alandır. Zemine, kenarları şekildeki çizgiler üzerinde olan dikdörtgen biçimli bir halı serilecektir. Zemindeki taralı kare bir gider kapağıdır ve halı bu kareyi tamamen örtmelidir.\nBuna göre kaç farklı dikdörtgen halı serilebilir?',
 istenen='Serilebilecek farklı halı sayısı.',ip=['Halının kenarları için ayrı ayrı kaç çizgi seçilebileceğini düşünmeden önce, gider kapağını kapsama koşulunun neyi sınırladığını düşün.'],bilgi=[CAR],sekil=SK,
 ad=[A('Çizgileri say','Dikdörtgeni iki dikey ve iki yatay çizgi belirler; gider kapağı sol–sağ çizgiler arasında kalmalıdır.','Sol çizgi 2 seçenek, sağ çizgi 4 seçenek'),A('Sütun seçimi','Sol ve sağ kenar seçimleri bağımsızdır.','2 × 4 = 8'),A('Satır seçimi','Alt çizgi gider kapağının altında 3 seçenek, üst çizgi üstünde 2 seçenek.','3 × 2 = 6'),A('Çarp','Sütun ve satır seçimleri bağımsızdır.','8 × 6 = 48')],
 puf='Yöntemini 2 × 2’lik küçük bir ızgarada elle sayarak sına.')

# ================= 04 orta · pizza dilimleri =================
N=10; mis={3,7}; pre=[i for i in range(N) if i not in mis]
adjp=lambda a,b:(a-b)%N in (1,N-1)
v=sum(1 for t in combinations(pre,3) if not any(adjp(a,b) for a,b in combinations(t,2))); assert v==24
cem=lambda m:sum(1 for t in combinations(range(m),3) if not any((a-b)%m in (1,m-1) for a,b in combinations(t,2)))
dog=lambda m:sum(1 for t in combinations(range(m),3) if not any(abs(a-b)==1 for a,b in combinations(t,2)))
c=[(comb(len(pre),3),'Komşuluk koşulunu atlamış: kalan 8 dilimden herhangi 3’ünü seçmiş: C(8, 3).','dikkat'),
   (cem(N),'Yenmiş dilimlerin yerini hâlâ dolu sanmış: 10 dilimlik tam çemberde sayım.','bilgi'),
   (cem(len(pre)),'Kalan 8 dilimi yan yana kapanmış tek bir çember sanmış (boşlukları yok saymış).','bilgi'),
   (dog(len(pre)),'Kalan 8 dilimi tek bir sıra sanıp uçları komşu saymamış.','bilgi'),
   (comb(len(pre),3)-comb(len(pre),2),'Komşu dilim çiftlerinin sayısını C(8, 2) sanıp tüm seçimlerden çıkarmış: 56 − 28.','islem')]
o=['\\def\\r{2.2}']
for i in range(N):
    a1=90-36*i; a2=a1-36
    if i in mis: o.append(f'\\draw[thick,dashed] (0,0) -- ({a1}:\\r) arc ({a1}:{a2}:\\r) -- cycle;')
    else: o.append(f'\\draw[thick,fill=vurgu!15] (0,0) -- ({a1}:\\r) arc ({a1}:{a2}:\\r) -- cycle;')
o.append('\\draw[thick,dashed] (-2.0,-2.75) -- (-1.55,-2.75) -- (-1.55,-2.4) -- (-2.0,-2.4) -- cycle; \\node[right] at (-1.45,-2.57) {: yenmiş dilimin yeri};')
SK=fig('\n'.join(o))
spec('0004',v,c,tipId='psb-desen',tip='Komşuluk koşullu desen ve seçim',z='orta',alt='Dilim Seçimi',kaz='Eksik dilimlerin oluşturduğu ayrı yaylarda komşu olmayan dilim üçlülerini sayar.',kalip='hikâyeli',
 kart='K-PSB-04 (pizza dilimleri) · 10 dilim, 2 yenmiş, 3 komşusuz dilim',
 metin='Eş dilimlere ayrılmış bir pizzanın bazı dilimleri yenmiş; yenmiş dilimlerin yerleri şekilde kesikli çizgilerle gösterilmiştir. Üç arkadaş kalan dilimlerden birer dilim alacak; alınan hiçbir iki dilim kenar paylaşmayacaktır.\nBuna göre bu üç dilim kaç farklı biçimde seçilebilir?',
 istenen='Üç dilimin farklı seçim sayısı.',ip=['Hangi dilim çiftleri birbirine komşudur? Şekildeki kesikli yerlere dikkat et.'],bilgi=[DIZ],sekil=SK,
 ad=[A('Grupları belirle','Boş yerler dilimleri ayırır; kalan dilimler 3’lük bir yay ve 5’lik bir yay olur, hiçbirinin uçları birbirine komşu değildir.','3 + 5 = 8 dilim'),A('Dilimleri paylaştır','Üç dilimin 3’lük yaydan 0, 1 ya da 2; 5’lik yaydan kalanı alacağı durumlar ayrı ayrı sayılır.','durumlar: (0, 3), (1, 2), (2, 1)'),A('Yaylarda say','3’lük yayda komşusuz 1 dilim için 3, 2 dilim için 1 (uçlar) seçim; 5’lik yayda komşusuz 3 dilim için 1, 2 dilim için 6, 1 dilim için 5 seçim.','(0, 3): 1 × 1 = 1 · (1, 2): 3 × 6 = 18 · (2, 1): 1 × 5 = 5'),A('Topla','Durumlar birbirinin yerine geçtiğinden toplanır.','1 + 18 + 5 = 24')],
 puf='Kalan dilimler tek çember mi, ayrı yaylar mı oluşturuyor? Şekilden kontrol et.')

# ================= 05 orta · lamba panosu =================
Rr,Cc=3,4; brk={(0,1),(1,2)}
cells=[(r,c) for r in range(Rr) for c in range(Cc) if (r,c) not in brk]
def ok(t,diag=False,horiz=False):
    for a_,b_ in combinations(t,2):
        dr,dc=abs(a_[0]-b_[0]),abs(a_[1]-b_[1])
        if horiz:
            if dr==0 and dc==1: return False
        elif dr+dc==1 or (diag and dr==1 and dc==1): return False
    return True
v=sum(1 for t in combinations(cells,3) if ok(t)); assert v==52
nb=lambda a_,b_:abs(a_[0]-b_[0])+abs(a_[1]-b_[1])==1
EC=sum(1 for a_,b_ in combinations(cells,2) if nb(a_,b_)); P2=sum(comb(sum(1 for b_ in cells if nb(a_,b_)),2) for a_ in cells); BAD=EC*(len(cells)-2)-P2
assert comb(len(cells),3)-BAD==v and (EC-sum(1 for a_,b_ in combinations(cells,2) if nb(a_,b_) and a_[0]==b_[0]))==sum(1 for a_,b_ in combinations(cells,2) if nb(a_,b_) and a_[1]==b_[1]),'v'
print('lamba',EC,P2,BAD,sum(1 for a_,b_ in combinations(cells,2) if nb(a_,b_) and a_[0]==b_[0]))
tumc=[(r,c) for r in range(Rr) for c in range(Cc)]
c=[(comb(len(cells),3),'Komşuluk koşulunu atlamış: 10 sağlam lambadan herhangi 3’ünü seçmiş: C(10, 3).','dikkat'),
   (sum(1 for t in combinations(tumc,3) if ok(t)),'Arızalı lambaları da sağlam sanmış: 12 lambanın hepsinden komşusuz seçmiş.','dikkat'),
   (sum(1 for t in combinations(cells,3) if ok(t,horiz=True)),'Komşuluğu yalnız yatay sanmış, dikey komşuluğu hesaba katmamış.','bilgi'),
   (comb(len(cells),3)-EC*(len(cells)-2),'Her komşu çifte kalan 8 lambadan birini ekleyip 120 − 10 × 8 yapmış; iki komşu çifti olan üçlülerin iki kez çıkarıldığını düzeltmemiş.','islem')]
o=[]
for r in range(Rr):
    for c_ in range(Cc):
        x,y=c_*1.0,-r*1.0
        if (r,c_) in brk: o.append(f'\\node[circle,draw,thick,fill=gray!45,minimum size=0.7cm,inner sep=0pt,font=\\large\\bfseries] at ({x},{y}) {{$\\times$}};')
        else: o.append(f'\\node[circle,draw,thick,fill=vurgu!12,minimum size=0.7cm] at ({x},{y}) {{}};')
o.append('\\node[circle,draw,thick,fill=gray!45,minimum size=0.45cm,inner sep=0pt,font=\\small\\bfseries] at (0,-3.0) {$\\times$}; \\node[right] at (0.35,-3.0) {: arızalı lamba};')
SK=fig('\n'.join(o))
spec('0005',v,c,tipId='psb-desen',tip='Komşuluk koşullu desen ve seçim',z='orta',alt='Lamba Panosu',kaz='Arızalı lambaları dışarıda bırakıp yatay ya da dikey komşu olmayan lamba üçlülerini sayar.',kalip='hikâyeli',
 kart='K-PSB-05 (lamba panosu) · 3 × 4 pano, 2 arızalı, 3 lamba komşusuz',
 metin='Bir vitrin panosunda lambalar şekildeki gibi sıralanmıştır; × işaretli lambalar arızalıdır ve yakılamaz. Gösterişli bir desen için sağlam lambalardan tam üçü yakılacaktır. Desen yalnız şu kurala uymalıdır: yakılan hiçbir iki lamba, bir kenarını paylaşan (yatay ya da dikey) komşu olmamalıdır; köşegen komşuluk sakıncalı sayılmaz.\nBuna göre kaç farklı desen oluşturulabilir?',
 istenen='Farklı desen sayısı.',ip=['Bir lamba yakıldığında, bundan sonra yakılamayacak olan sağlam lambalar hangileridir? Şekilde köşelerin, kenarların ve ortanın komşu sayısını karşılaştır.'],bilgi=[KOS],sekil=SK,
 ad=[A('Sağlam lambalar','Arızalı iki lamba çıkarılınca desen için kullanılabilecek lambalar belirlenir.','12 − 2 = 10 sağlam lamba'),A('Tüm seçimler','Sağlam lambalardan herhangi üçü seçilirse.','C(10, 3) = 120'),A('Komşu çiftler','Sağlam lambalar arasında bir kenarı ortak olan çiftler sayılır (yatay 5, dikey 5).',f'{EC} çift'),A('Koşulu bozan üçlüler','Her komşu çifte kalan 8 lambadan biri eklenir; ortak lambası olan iki komşu çifti içeren üçlüler iki kez sayıldığından bu zincirlerin sayısı kadar düzeltilir.',f'{EC} × 8 − {P2} = {BAD}'),A('Çıkar','Komşu çifti içermeyen üçlüler kalır.','120 − '+str(BAD)+' = 52')],
 puf='Yöntemini 2 × 2’lik küçük bir panoda elle sayarak sına.')

# ================= 06 orta · rakam kartları =================
kart_=(0,1,2,2,3)
S={p for p in permutations(kart_) if p[0]!=0 and p[-1]%2==0}; v=len(S); assert v==30
c=[(len(set(permutations(kart_))),'Başta 0 olamayacağını ve sayının çift olması koşulunu atlamış: aynı kartları ayırt etmeden bütün dizilişler, 5!/2!.','dikkat'),
   (fa(5),'Aynı rakamlı kartları farklı sanmış ve koşulları atlamış: 5!.','bilgi'),
   (4*fa(4),'Baştaki 0’ı dışlamış, kartları farklı sanmış ve çift koşulunu atlamış: 4 × 4!.','bilgi'),
   (len({p for p in permutations(kart_) if p[-1]%2==0}),'Çift koşulunu uygulamış ama baştaki 0’ı unutmuş.','dikkat'),
   (len({p for p in permutations(kart_) if p[0]!=0}),'Baştaki 0’ı dışlamış ama çift koşulunu atlamış.','dikkat'),
   (len({p for p in permutations(kart_) if p[0]!=0 and p[-1]==2}),'Yalnız son basamağın 2 olduğu durumu saymış, 0 olan durumu unutmuş.','dikkat'),
   (len({p for p in permutations(kart_) if p[-1]==0}),'Yalnız son basamağın 0 olduğu durumu saymış, 2 olan durumu unutmuş.','dikkat')]
assert [x[0] for x in c]==[60,120,96,36,48,18,12],[x[0] for x in c]
o=[]
for i,d in enumerate([2,0,3,2,1]):
    o.append(f'\\node[draw,thick,rounded corners=3pt,minimum width=1.1cm,minimum height=1.6cm,font=\\Huge\\bfseries,fill=vurgu!10] at ({i*1.4},0) {{{d}}};')
SK=fig('\n'.join(o))
spec('0006',v,c,tipId='psb-sayi',tip='Kartlarla sayı yazma',z='orta',alt='Rakam Kartları',kaz='Aynı rakamlı kartların ayırt edilemediği durumda baştaki rakam ve çift sayı koşullarıyla yazılabilecek sayıları sayar.',kalip='yeni nesil',
 kart='K-PSB-06 (rakam kartları) · kartlar 0, 1, 2, 2, 3',
 metin='Şekildeki kartların her birinde bir rakam yazılıdır; aynı rakamı taşıyan kartlar birbirinden ayırt edilemez. Bu kartların hepsi yan yana dizilerek beş basamaklı bir doğal sayı yazılıyor; kartlar ters çevrilmiyor ve kartlardaki rakamlar değiştirilmiyor.\nBuna göre bu kartlarla yazılabilen çift doğal sayıların sayısı kaçtır?',
 istenen='Yazılabilecek çift doğal sayıların sayısı.',ip=['Son basamağa hangi kartlar gelebilir, ve her durumda baştaki kart için seçenekler nasıl değişir?'],bilgi=[SIF,TEK],sekil=SK,
 ad=[A('Kartları oku','Şekildeki kartlardaki rakamlar belirlenir.','0, 1, 2, 2, 3'),A('Son basamak 0','0 son basamağa konursa kalan 1, 2, 2, 3 kartı serbest dizilir (2 aynı).','4! / 2! = 12'),A('Son basamak 2','2 son basamağa konursa kalan 0, 1, 2, 3 kartı dizilir; 0 başa gelemez.','4! − 3! = 18'),A('Topla','İki durum birbirinin yerine geçer.','12 + 18 = 30')],
 puf='Bulduğun sayıyı yazmadan önce her koşulu bir kez daha oku ve hangisini uyguladığını işaretle.')

# ================= 07 zor · nokta ağında üçgen =================
Rw,Cl=3,4
nok=[(x,y) for x in range(Cl) for y in range(Rw)]
def kol(a,b,c_): return (b[0]-a[0])*(c_[1]-a[1])-(b[1]-a[1])*(c_[0]-a[0])==0
tuc=[t for t in combinations(nok,3) if not kol(*t)]; v=len(tuc); assert v==200
sat=Rw*comb(Cl,3); sut=Cl*comb(Rw,3); cap=sum(1 for t in combinations(nok,3) if kol(*t))-sat-sut
assert (sat,sut,cap)==(12,4,4)
c=[(comb(12,3),'Aynı doğru üzerindeki üçlüleri hiç çıkarmamış: C(12, 3).','dikkat'),
   (comb(12,3)-sat-sut,'Çapraz doğrular üzerindeki üçlüleri çıkarmamış: 220 − 12 − 4.','dikkat'),
   (comb(12,3)-sat,'Yalnız yatay doğruları çıkarmış: 220 − 12.','dikkat'),
   (comb(12,2),'Üçgeni iki nokta seçerek saymış: C(12, 2).','bilgi')]
o=[]
for (x,y) in nok: o.append(f'\\fill ({x*1.2},{y*1.2}) circle (0.1);')
SK=fig('\n'.join(o))
spec('0007',v,c,tipId='psb-geosay',tip='Şekilde sayma (çokgen, ızgara, nokta ağı)',z='zor',alt='Nokta Ağında Üçgen',kaz='Nokta ağındaki üçlülerden aynı doğru üzerindeki yatay, dikey ve çapraz üçlüleri çıkararak üçgen sayısını bulur.',kalip='yeni nesil',
 kart='K-PSB-07 (nokta ağı) · 3 × 4 nokta',
 metin='Şekildeki noktalar, her satırda ve her sütunda eşit aralıklarla yerleştirilmiştir. Köşeleri bu noktalardan üçü olacak biçimde üçgenler çizilecek; ancak aynı doğru üzerinde bulunan üç nokta üçgen oluşturamaz.\nBuna göre köşeleri bu noktalar olan kaç farklı üçgen çizilebilir?',
 istenen='Çizilebilecek farklı üçgen sayısı.',ip=['Hangi doğrultularda üç nokta aynı doğru üzerinde olabilir? Noktalar arasındaki yatay ve dikey uzaklıkların oranına dikkat et.'],bilgi=[NOK],sekil=SK,
 ad=[A('Noktaları say','Şekilde 3 satır ve 4 sütun nokta vardır.','3 × 4 = 12 nokta'),A('Tüm üçlüler','Noktalardan herhangi üçü seçilirse.','C(12, 3) = 220'),A('Yatay ve dikey','Her satırdan 4 noktadan 3’ü seçilir; her sütundaki 3 nokta tek üçlüdür.','3 × C(4, 3) + 4 × 1 = 12 + 4 = 16'),A('Çapraz','Üç satırı birer noktayla birleştiren eğik üçlüler: sağa-yukarı 2, sağa-aşağı 2.','2 + 2 = 4'),A('Çıkar','Doğrusal üçlüler üçgen vermez.','220 − 16 − 4 = 200')],
 puf='Yöntemini 2 × 2 noktalı küçük bir ağda elle sayarak sına.')

# ================= 08 zor · tabloda görev dağılımı =================
M=[[1,1,1,1],[1,1,1,0],[0,1,0,1],[1,1,1,1]]
v=sum(1 for s in permutations(range(4)) if all(M[i][s[i]] for i in range(4))); assert v==10
rs=[sum(r) for r in M]; cs=[sum(M[i][j] for i in range(4)) for j in range(4)]
pc=[sum(1 for s in permutations(range(4)) if all(M[i][s[i]] for i in range(4)) and s[2]==j) for j in (1,3)]; assert sum(pc)==10
c=[(prod(rs),'Her kişinin uygun görev sayısını çarpmış, görevlerin tek kişiye verileceğini unutmuş: 4 × 3 × 2 × 4.','bilgi'),
   (fa(4),'Tablodaki kısıtları atlamış: 4!.','dikkat'),
   (sum(rs),'Tablodaki “Evet” sayısını sayıp dağılım sanmış.','dikkat'),
   (prod(cs),'Görevlerin uygun kişi sayılarını çarpmış: 3 × 4 × 3 × 3.','bilgi'),
   (pc[0],'En kısıtlı kişinin (Cem) yalnız Boya seçeneğini hesaba katmış.','dikkat'),(pc[1],'En kısıtlı kişinin (Cem) yalnız Paketleme seçeneğini hesaba katmış.','dikkat'),
   (fa(3)*min(rs),'Kısıtlı kişinin iki seçeneğiyle kalan üç kişinin 3! sıralamasını çarpmış: 2 × 3!.','bilgi')]
assert pc==[4,6] and len({x[0] for x in c}|{v})==8
SK=tablo_svg(['Kişi','Montaj','Boya','Test','Paketleme'],[[n_]+['Evet' if x else 'Hayır' for x in r] for n_,r in zip(['Ali','Banu','Cem','Derya'],M)])
spec('0008',v,c,tipId='psb-esles',tip='Kısıtlı eşleştirme',z='zor',alt='Tablodan Görev Dağılımı',kaz='Tabloda her kişinin yapabildiği görevleri okuyup en kısıtlı kişiden başlayarak görev dağılımlarını sayar.',kalip='tablo',
 kart='K-PSB-08 (tablo, eşleştirme) · 4 kişi, 4 görev, 3 kısıt',
 metin='Bir atölyede Ali, Banu, Cem ve Derya’ya dört ayrı görev verilecektir. Her kişi tam bir görevi yapacak, her görev tam bir kişi tarafından yapılacaktır. Kişilerin hangi görevleri yapabildiği aşağıdaki tabloda “Evet” ile, yapamadığı görevler “Hayır” ile gösterilmiştir; bir kişiye yalnız yapabildiği bir görev verilebilir.\nBuna göre görevler kişilere kaç farklı biçimde dağıtılabilir?',
 istenen='Görevlerin kişilere farklı dağıtım sayısı.',ip=['Tabloda her satırda ve her sütunda kaç “Evet” olduğuna bak; bir görev bir kişiye verilince diğer kişilerin seçenekleri nasıl değişir?'],bilgi=[ESL],sekil=SK,
 ad=[A('Tabloyu oku','Cem yalnız Boya ve Paketleme görevlerini yapabiliyor; diğerleri daha çok görevde çalışabiliyor.','Cem: 2 seçenek'),A('Cem Boya yaparsa','Banu yalnız Montaj ya da Test yapabilir (Boya alındı); Ali ile Derya kalan görevlerden birini alır. Banu Montaj alırsa kalan Test ve Paketleme Ali ile Derya arasında 2 biçimde dağıtılır; Banu Test alırsa Montaj ve Paketleme 2 biçimde dağıtılır.','2 + 2 = 4'),A('Cem Paketleme yaparsa','Banu Montaj, Boya ya da Test yapabilir; Ali ile Derya kalan iki görevi alır.','3 × 2 = 6'),A('Topla','İki durum birbirinin yerine geçer.','4 + 6 = 10')] ,
 puf='Sonucu, kısıtsız durumun sayısıyla karşılaştırarak makul olup olmadığını kontrol et.')

# ================= 09 zor · tabloda kurul seçimi =================
TT={'9. sınıf':(2,2),'10. sınıf':(3,2),'11. sınıf':(1,3)}
people=[(s,g,i) for s,(k,e) in TT.items() for g,n_ in (('k',k),('e',e)) for i in range(n_)]; n9=len(people)
def kc(cm,cls=True,gen=True):
    if cls and len({p[0] for p in cm})<3: return False
    if gen and {p[1] for p in cm}!={'k','e'}: return False
    return True
v=sum(1 for cm in combinations(people,4) if kc(cm)); assert v==367 and n9==13
sinif=sum(1 for cm in combinations(people,4) if kc(cm,gen=False)); assert sinif==400
tk=sum(1 for cm in combinations(people,4) if kc(cm,gen=False) and {p[1] for p in cm}=={'k'}); te=sum(1 for cm in combinations(people,4) if kc(cm,gen=False) and {p[1] for p in cm}=={'e'}); assert (tk,te)==(9,24) and sinif-tk-te==v
szs=[sum(x) for x in TT.values()]
c=[(sinif,'Kurulda en az bir kız ve bir erkek bulunma koşulunu atlamış: her sınıftan en az bir kişi koşulunu sağlayan 400 seçimi yazmış.','dikkat'),
   (sinif-te,'Yalnız erkeklerden oluşan kurulları çıkarmış, yalnız kızlardan oluşanları unutmuş: 400 − 24.','dikkat'),
   (sinif-tk,'Yalnız kızlardan oluşan kurulları çıkarmış, yalnız erkeklerden oluşanları unutmuş: 400 − 9.','dikkat'),
   (comb(n9,4),'Sınıf koşulunu atlayıp 13 öğrenciden herhangi 4’ünü seçmiş: C(13, 4).','dikkat')]
SK=tablo_svg(['Sınıf','Kız öğrenci','Erkek öğrenci'],[[s,str(k),str(e)] for s,(k,e) in TT.items()])
spec('0009',v,c,tipId='psb-secme',tip='Gruplu kurul seçimi',z='zor',alt='Tablodan Kurul Seçimi',kaz='Tabloda verilen sınıf ve cinsiyet gruplarından iki koşulu birlikte sağlayan kurul seçimlerini sayar.',kalip='tablo',
 kart='K-PSB-09 (tablo, kurul seçimi) · 9. sınıf 2K 2E, 10. sınıf 3K 2E, 11. sınıf 1K 3E',
 metin='Bir okulda 9., 10. ve 11. sınıf öğrencilerinden oluşan 4 kişilik bir öğrenci kurulu kurulacaktır. Kurulda her sınıftan en az bir öğrenci bulunacak ve kurulun hepsi aynı cinsiyetten olmayacaktır. Her sınıftaki kız ve erkek öğrenci sayıları aşağıdaki tabloda verilmiştir; kurulda görev ayrımı yapılmayacaktır.\nBuna göre bu kurul kaç farklı biçimde oluşturulabilir?',
 istenen='Oluşturulabilecek farklı kurul sayısı.',ip=['İki koşuldan birini önce uygulayıp ikincisini bu sayıma göre ele almak mümkün mü?'],bilgi=[KUM],sekil=SK,
 ad=[A('Öğrenci sayısı','Tablodaki tüm öğrenciler toplanır.','4 + 5 + 4 = 13 öğrenci'),A('Sınıf koşulu','4 kişilik kurulda bir sınıftan 2, diğerlerinden 1 kişi bulunur; hangi sınıftan 2 kişi seçildiğine göre durumlar toplanır.','C(4, 2) × 5 × 4 + 4 × C(5, 2) × 4 + 4 × 5 × C(4, 2) = 120 + 160 + 120 = 400'),A('Yalnız kızlar','6 kız öğrenciden her sınıftan en az bir kişi olan 4 kişilik kurullar: (2, 3, 1) kız sayılarıyla.','C(2, 2) × 3 × 1 + 2 × C(3, 2) × 1 = 3 + 6 = 9'),A('Yalnız erkekler','7 erkek öğrenciden (2, 2, 3) erkek sayılarıyla her sınıftan en az bir kişi olan kurullar.','C(2, 2) × 2 × 3 + 2 × C(2, 2) × 3 + 2 × 2 × C(3, 2) = 6 + 6 + 12 = 24'),A('Çıkar','Tek cinsiyetten oluşan kurullar koşulu bozar.','400 − 9 − 24 = 367')],
 puf='Koşullu seçimde bulduğun sayının, koşulsuz seçim sayısından küçük olması gerektiğini kontrol et.')

# ================= 10 zor · yönlü yol şeması =================
E_={'A':'BCD','B':'EF','C':'EFG','D':'FG','E':'HI','F':'HIJ','G':'IJ','H':'K','I':'K','J':'K'}
def yollar_(s,t,p=('A',)):
    if s==t: yield p; return
    for nx in E_.get(s,''): yield from yollar_(nx,t,p+(nx,))
PY=list(yollar_('A','K')); assert len(PY)==17
v=sum(1 for p in PY if 'F' in p and 'C' not in p); assert v==6
fs=sum(1 for p in PY if 'F' in p); cs_=sum(1 for p in PY if 'C' not in p); fc=sum(1 for p in PY if 'F' in p and 'C' in p)
assert (fs,cs_,fc)==(9,10,3)
c=[(len(PY),'F ve C koşullarını atlamış: bütün yolları saymış.','dikkat'),
   (fs,'C’den geçmeme koşulunu atlamış: F’den geçen bütün yolları saymış.','dikkat'),
   (cs_,'F’den geçme koşulunu atlamış: C’den geçmeyen bütün yolları saymış.','dikkat'),
   (fc,'Koşulu ters okumuş: hem F’den hem C’den geçen yolları saymış.','bilgi'),
   (sum(1 for p in PY if 'F' not in p and 'C' not in p),'Her iki noktadan da geçmeyen yolları saymış.','bilgi'),
   (len(PY)-fs,'F’den geçmeyen yolları saymış.','dikkat'),
   (2,'Yalnız A’dan F’ye (C’siz) giden yolları saymış.','dikkat')]
print([x[0] for x in c],v); assert len({x[0] for x in c}|{v})==len(c)+1
pos={'A':(0,0),'B':(2.0,1.9),'C':(2.0,0),'D':(2.0,-1.9),'E':(4.1,1.9),'F':(4.1,0),'G':(4.1,-1.9),'H':(6.2,1.9),'I':(6.2,0),'J':(6.2,-1.9),'K':(8.3,0)}
o=[]
for k_,(x,y) in pos.items(): o.append(f'\\node[circle,draw,thick,fill=white,minimum size=0.75cm,inner sep=0pt,font=\\normalsize\\bfseries] ({k_}) at ({x},{y}) {{{k_}}};')
for a_,bs in E_.items():
    for b_ in bs: o.append(f'\\draw[thick,-{{Stealth[length=2.2mm]}}] ({a_}) -- ({b_});')
SK=fig('\n'.join(o))
spec('0010',v,c,tipId='psb-yol',tip='Yollar ve dallanma şeması',z='orta',alt='Yönlü Yol Şeması',kaz='Yönlü yol şemasında her noktaya gelen yol sayılarını toplayarak bir noktadan geçen, diğerinden geçmeyen yolları sayar.',kalip='yeni nesil',
 kart='K-PSB-10 (yönlü şema) · 11 nokta, A’dan K’ye 17 yol; F’den geçip C’den geçmeyen',
 metin='Şekildeki oklar, bir oyun alanındaki geçitlerin tek yönlü geçilebilen yönlerini göstermektedir. Bir oyuncu A noktasından başlayıp oklara uyarak K noktasına ulaşıyor; oyuncu bir geçitten geri dönemiyor. Oyuncu, yolculuğunda F noktasından geçmek zorundadır, ancak C noktasına hiç uğrayamaz.\nBuna göre oyuncu A’dan K’ye kaç farklı yolla gidebilir?',
 istenen='Koşula uyan farklı yol sayısı.',ip=['C noktası yasak olduğuna göre şemada hangi oklar artık kullanılamaz?'],bilgi=[YOL],sekil=SK,
 ad=[A('C’yi dışarıda bırak','C’den çıkan ve C’ye giden oklar kullanılamaz; A’dan yalnız B ve D’ye gidilebilir.','A → B, A → D'),A('A’dan F’ye','F’ye gelen oklar B, C ve D’den gelir; C yasak olduğundan B ve D üzerinden.','2 yol'),A('F’den K’ye','F’den H, I ve J’ye ok gider; bunların her biri K’ye tek yolla ulaşır.','3 yol'),A('Çarp','A’dan F’ye giden her yol, F’den K’ye giden her yolla birleşebilir.','2 × 3 = 6')],
 puf='Sonucu, koşulsuz toplam yol sayısıyla karşılaştırarak kontrol et.')

# ---------- üret ----------
HR=olus(SP)
for (no,d,ad_,k),r in zip(SP,HR):
    sm=[a for a in ad_ if a[0]<d]; lg=[a for a in ad_ if a[0]>d]
    yan=sm[:r]+lg[:4-r]; assert len(yan)==4
    mk(P,no,dogru=d,yan=yan,adim=len(k['ad']),**k)
bitir(P,'permsekb',UK)
