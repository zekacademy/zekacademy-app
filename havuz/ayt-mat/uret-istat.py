"""AYT Matematik · İstatistik (20 soru: 4 kolay / 10 orta / 6 zor). Şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer kodla hesaplanıp assert edilir.
Kardeş yok, ipucu 1. Varyans = Σ(x−x̄)²/n (anakütle tanımı; soruda açıkça verilir)."""
import sys,os,statistics as stt,math
AD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(AD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-mat')); sys.path.insert(0,HV)
import _hafif_mat as H
from _hafif_mat import *
from _hafif_mat import tablo_svg
from cizim import tikz_svg
import json
H.KONU='İstatistik'
UK='amat|İstatistik'
P=Parti('istat','İstatistik',UK,ders='AYT Matematik',idon='aytmat')
KY='ÖSYM AYT Matematik 2018–2025 taraması (konuda doğrudan soru az; grafik okuma ve ortalama kalıpları, yalnız mantık) · MEB 11–12. sınıf matematik (veri analizi, merkezî eğilim ve yayılma ölçüleri)'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\footnotesize'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
Fr_=Fr
def mean(x): return Fr(sum(x),len(x))
def var(x): m=mean(x); return sum((Fr(v)-m)**2 for v in x)/len(x)
def med(x):
    s=sorted(x); n=len(s); return Fr(s[n//2]) if n%2 else Fr(s[n//2-1]+s[n//2],2)
def quart(x):
    s=sorted(x); n=len(s); h=n//2; lo=s[:h]; hi=s[h+1:] if n%2 else s[h:]; return med(lo),med(s),med(hi)

# ---------- bilgi kutuları (yalnız tanım; örnekler soruların sayılarından farklı) ----------
ORT=B('Aritmetik ortalama','değerlerin toplamının değer sayısına bölümüdür. Toplam = ortalama × değer sayısı. Örnek: 4 değerin ortalaması 7 ise toplamları 28’dir')
AGR=B('Ağırlıklı ortalama','her değer kendi ağırlığıyla çarpılır, çarpımların toplamı ağırlıkların toplamına bölünür. Örnek: 2 ağırlıklı 10 ile 3 ağırlıklı 20 değerinin ağırlıklı ortalaması (2 × 10 + 3 × 20) / 5 = 16’dır')
MED=B('Medyan, mod, ranj','küçükten büyüğe sıralanan değerlerde ortadaki değer medyandır (değer sayısı çiftse ortadaki iki değerin ortalaması). Mod en çok tekrar eden değerdir. Ranj en büyük ile en küçük değerin farkıdır. Örnek: 1, 4, 4, 6 için medyan 4, mod 4, ranj 5’tir')
FRE=B('Frekans tablosu','her değerin kaç kez gözlendiğini gösterir; frekansların toplamı toplam gözlem sayısıdır. Ortalama için Σ(değer × frekans) toplamı gözlem sayısına bölünür. Örnek: 1 değeri 2 kez, 3 değeri 2 kez gözlenmişse toplam 1 × 2 + 3 × 2 = 8’dir')
DAI=B('Daire grafiği','tam daire 360° olup bir dilimin merkez açısı, o dilimin payıyla orantılıdır: dilimdeki kişi sayısı = (merkez açı / 360°) × toplam kişi sayısı. Örnek: 200 kişilik grupta 90° lik dilim 50 kişiyi gösterir')
HIS=B('Histogram','sınıf aralıklarına karşılık gelen sütunların yüksekliği o sınıftaki gözlem sayısıdır. Sınıflanmış veride her gözlemin sınıf orta noktasında olduğu varsayılır; orta nokta = (alt sınır + üst sınır) / 2. Örnek: 0 – 4 sınıfının orta noktası 2’dir')
VAR=B('Varyans ve standart sapma','varyans, değerlerin ortalamadan farklarının karelerinin ortalamasıdır: Var = Σ(xᵢ − x̄)² / n. Standart sapma varyansın kareköküdür. Örnek: 1, 3 için x̄ = 2, Var = (1 + 1) / 2 = 1’dir')
KUT=B('Kutu grafiği','en küçük değer, 1. çeyrek (Q1), medyan, 3. çeyrek (Q3) ve en büyük değer gösterilir. Çeyrekler açıklığı Q3 − Q1’dir; verilerin ortadaki yarısını kapsar. Değer sayısı tekse Q1 ve Q3 medyan hariç alt ve üst yarının medyanıdır. Örnek: 1, 3, 5, 7, 9 için Q1 = 2, medyan 5, Q3 = 8’dir')
DON=B('Doğrusal dönüşüm','her değer yᵢ = a·xᵢ + b ile değişirse ortalama ȳ = a·x̄ + b olur; standart sapma |a| katına, varyans a² katına çıkar, b sapmayı ve varyansı değiştirmez. Örnek: x̄ = 5, standart sapma 2 iken y = 3x + 1 için ȳ = 16, standart sapma 6’dır')
SAC=B('Saçılım diyagramı','iki değişkenin değer çiftlerini nokta olarak gösterir. Noktalar soldan sağa yükseliyorsa ilişki pozitif, alçalıyorsa negatiftir; noktalar bir doğru etrafında ne kadar toplanmışsa ilişki o kadar güçlüdür. Örnek: boy arttıkça ayakkabı numarası genelde artar')
EKL=B('Veri ekleme ve ortalama','toplam = ortalama × değer sayısı; yeni toplam eski toplam artı eklenen değerlerdir. Ortalamaya eşit bir değer eklenirse ortalama değişmez. Örnek: 5 değerin ortalaması 8 iken 8 eklenirse 6 değerin ortalaması yine 8’dir')

# ---------- kartlar (her tipId için bir kart) ----------
kartla('K-AIS-01','Ortalama ve veri ekleme','Ortalama ile değer sayısı toplamı verir; gruplar birleştirilirken toplamlar ayrı ayrı yazılıp birleşik ortalamada yerine konur.','Ortalamaların ortalamasını almak; toplam yerine ortalamayı çıkarmak; değer sayısını yanlış bölenle kullanmak.','orta','hikâyeli',3,'ist-ortalama','Ortalama ve veri ekleme')
kartla('K-AIS-02','Frekans tablosunda ortalama ve medyan','Tablodaki değerler frekanslarıyla ağırlıklandırılır; medyan için yığılmalı frekans izlenerek ortadaki sıra numaralarının hangi değere düştüğüne bakılır.','Frekansları değer sanmak; değerlerin sayısına bölmek; çift sayıda gözlemde tek bir sırayı almak.','orta','tablo',4,'ist-frekans','Frekans tablosunda ortalama ve medyan')
kartla('K-AIS-03','Medyan, mod ve ranj','Veri sıralanır; ortadaki sıra, en sık değer ve uç değerler okunur; bilinmeyen değer için sıradaki yeri belirlenir.','Veriyi sıralamadan ortadaki değeri almak; modu ortalamayla karıştırmak; bilinmeyenin her konumda aynı etkiyi yaptığını sanmak.','kolay','öncüllü',3,'ist-merkez','Medyan, mod ve ranj')
kartla('K-AIS-04','Daire grafiğinden sayı ve ortalama','Merkez açılar toplam sayıyla orantılanır; her dilimin kişi sayısı bulunduktan sonra ortalama ya da karşılaştırma yapılır.','Merkez açıyı kişi sayısı sanmak; yüzdeyle açıyı karıştırmak; dilim farkında açı farkını yanıt yapmak.','kolay','hikâyeli',3,'ist-daire','Daire grafiğinden sayı ve ortalama')
kartla('K-AIS-05','Histogramda sınıf orta noktaları','Her sınıf orta noktasıyla temsil edilir; orta noktalar frekanslarla çarpılıp toplanarak ortalama ve bilinmeyen sütun bulunur.','Sınıf sınırlarını orta nokta yerine kullanmak; frekansları hesaba katmamak; en kalabalık sınıfı ortalama sanmak.','orta','grafik',4,'ist-histogram','Histogramda sınıf orta noktaları')
kartla('K-AIS-06','Varyans ve standart sapma','Sapmaların kareleri toplanıp değer sayısına bölünür ya da karelerin ortalamasından ortalamanın karesi çıkarılır; veri eklenince toplam kareler değişimi izlenir.','Bölmeyi unutmak; ortalamanın karesini çıkarmamak; karesini almadan mutlak sapma kullanmak; gruplar arası farkı atlamak.','orta','grafik',4,'ist-sapma','Varyans ve standart sapma')
kartla('K-AIS-07','Doğrusal dönüşümün etkisi','Dönüşümün çarpanı ve ekleneni ayrı düşünülür: ortalama ikisinden, sapma yalnız çarpandan etkilenir; ters yönde çözerken işlemler tersine uygulanır.','Sapmaya ya da varyansa sabit eklemek; varyansa çarpanın kendisini uygulamak; ters çevirirken işaretini yanlış kullanmak.','zor','yeni nesil',4,'ist-donusum','Doğrusal dönüşümün etkisi')
kartla('K-AIS-08','Kutu grafiği ve çeyrekler','Kutu grafiğinden Q1, medyan ve Q3 okunur; değer sayısına göre sıra numaraları belirlenip bilinmeyen değerler konumlarından bulunur.','Çeyrekler açıklığı ile ranjı karıştırmak; çeyrek sırasını yanlış yerden saymak; dönüşümü çeyrekler açıklığına yanlış uygulamak.','orta','öncüllü',4,'ist-kutu','Kutu grafiği ve çeyrekler')
kartla('K-AIS-09','Saçılım diyagramında yorum','Noktaların toplu eğilimi, gruplar için ortalama ve eşik koşulları ayrı ayrı denetlenir.','Tek noktaya bakıp genel eğilimi yorumlamak; aynı x değerli noktaları tek sanmak; koşulun yönünü ters okumak.','orta','öncüllü',4,'ist-sacilim','Saçılım diyagramında yorum')

# ---------- şekil yardımcıları ----------
MAV='blue!55'; TUR='orange!80'; YES='teal!65'; MOR='violet!55'
def eksen_xy(x1,y1,xl='',yl=''):
    return (f'\\draw[-{{Stealth}},thick] (0,0) -- ({x1},0) node[right] {{{xl}}};\n\\draw[-{{Stealth}},thick] (0,0) -- (0,{y1}) node[above] {{{yl}}};')
def yizgara(w,ymax,ystep,sy,etiket=True):
    o=[]
    for j in range(ystep,ymax+1,ystep):
        o.append(f'\\draw[gray!40,thin] (0,{j*sy:.3f}) -- ({w},{j*sy:.3f});')
        if etiket: o.append(f'\\node[left=2pt] at (0,{j*sy:.3f}) {{${j}$}};')
    return '\n'.join(o)
def sutun_grafik(et,dg,ymax,ystep,sy,renk,yl,xw=0.85):
    w=len(et)*xw+0.2; o=[yizgara(w,ymax,ystep,sy)]
    for i,(e,v) in enumerate(zip(et,dg)):
        x0=0.1+i*xw+0.1; x1=x0+xw-0.2
        o.append(f'\\draw[fill={renk[i]},draw=black!70,thick] ({x0:.3f},0) rectangle ({x1:.3f},{v*sy:.3f});')
        o.append(f'\\node[below=2pt] at ({(x0+x1)/2:.3f},0) {{{e}}};')
    o.append(eksen_xy(w+0.3,ymax*sy+0.5,'',yl)); return '\n'.join(o)
def pie(dilimler,r=1.55,renkler=(MAV,TUR,YES,MOR),ek=''):
    o=[]; a=90.0
    for (ad,aci),rk in zip(dilimler,renkler):
        b=a-aci; o.append(f'\\draw[fill={rk},draw=black!70,thick] (0,0) -- ({a:.2f}:{r}) arc ({a:.2f}:{b:.2f}:{r}) -- cycle;')
        m=(a+b)/2; o.append(f'\\node[align=center,fill=white,fill opacity=0.8,text opacity=1,inner sep=1.5pt] at ({m:.2f}:{r*1.42:.3f}) {{{ad}\\\\${aci}^\\circ$}};')
        a=b
    return '\n'.join(o)+ek
def histogram(sinirlar,fr,ymax,ystep,sy,sx,renk,yl,bilinmeyen=None,ad_x='',notx=1):
    w=(len(sinirlar)-1)*sx; o=[yizgara(w,ymax,ystep,sy)]
    for i,f in enumerate(fr):
        x0=i*sx; x1=x0+sx
        if bilinmeyen==i:
            o.append(f'\\draw[dash pattern=on 3pt off 2pt,thick,fill=gray!15] ({x0:.3f},0) rectangle ({x1:.3f},{9*sy:.3f});\\node[font=\\large] at ({(x0+x1)/2:.3f},{4.5*sy:.3f}) {{$x$}};')
        else: o.append(f'\\draw[fill={renk[i%len(renk)]},draw=black!70,thick] ({x0:.3f},0) rectangle ({x1:.3f},{f*sy:.3f});')
    for i,s in enumerate(sinirlar): o.append(f'\\node[below=2pt] at ({i*sx:.3f},0) {{${s}$}};')
    o.append(eksen_xy(w+0.35,ymax*sy+0.5,ad_x,yl)); return '\n'.join(o)
def kutu(y,mn,q1,md,q3,mx,sx,renk,etiket=None,sayi=False,alt=False,yh=0.55):
    o=[f'\\draw[thick] ({mn*sx:.3f},{y}) -- ({q1*sx:.3f},{y});\\draw[thick] ({q3*sx:.3f},{y}) -- ({mx*sx:.3f},{y});',
       f'\\draw[thick] ({mn*sx:.3f},{y-yh/2}) -- ({mn*sx:.3f},{y+yh/2});\\draw[thick] ({mx*sx:.3f},{y-yh/2}) -- ({mx*sx:.3f},{y+yh/2});',
       f'\\draw[fill={renk},draw=black!75,thick] ({q1*sx:.3f},{y-yh}) rectangle ({q3*sx:.3f},{y+yh});',
       f'\\draw[very thick] ({md*sx:.3f},{y-yh}) -- ({md*sx:.3f},{y+yh});']
    if etiket: o.append(f'\\node[left=3pt,font=\\bfseries] at ({mn*sx-0.05:.3f},{y}) {{{etiket}}};')
    if sayi:
        for k,v in zip((mn,q1,md,q3,mx),(mn,q1,md,q3,mx)):
            o.append(f'\\node[{"below" if alt else "above"}=1pt,font=\\scriptsize] at ({v*sx:.3f},{y-yh if alt else y+yh}) {{{v}}};')
    return '\n'.join(o)
def xekseni(x0,x1,adim,sx,ymin,ad='',kucuk=None,hg=3.6):
    o=[f'\\draw[-{{Stealth}},thick] ({x0*sx-0.2:.3f},{ymin}) -- ({x1*sx+0.5:.3f},{ymin}) node[right] {{{ad}}};']
    for v in range(x0,x1+1,adim): o.append(f'\\draw ({v*sx:.3f},{ymin}) -- ({v*sx:.3f},{ymin-0.1}); \\node[below=1pt] at ({v*sx:.3f},{ymin-0.1}) {{${v}$}};')
    if kucuk:
        for v in range(x0,x1+1,kucuk): o.append(f'\\draw[gray!35,thin] ({v*sx:.3f},{ymin}) -- ({v*sx:.3f},{ymin+hg});')
    return '\n'.join(o)
def oncul_hata(dogru_set,cevap_kumesi,nedenler):
    """Öncüllü çeldirici açıklaması: hangi öncülü neden yanlış değerlendirdiği."""
    parca=[]
    for i,r in enumerate(('I','II','III')):
        if (i in cevap_kumesi) and (i not in dogru_set): parca.append(f'{r}. öncülü doğru sanmış ({nedenler[i]})')
        if (i in dogru_set) and (i not in cevap_kumesi): parca.append(f'{r}. öncülü yanlış sanmış ({nedenler[i]})')
    return '; '.join(parca)[0].upper()+'; '.join(parca)[1:]+'.'
SIRA=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']; KUME=[{0},{1},{0,1},{0,2},{0,1,2}]
def oncullu(dogru_set,nedenler):
    di=KUME.index(set(dogru_set)); yan=[(SIRA[i],oncul_hata(set(dogru_set),KUME[i],nedenler),'bilgi') for i in range(5) if i!=di]
    return SIRA[di],yan
HARF={}

# ================= 01 kolay · sütun grafiği, ortalama (hikâyeli) =================
gun=['Pzt','Sal','Çar','Per','Cum','Cmt']; kv=[6,16,4,14,10,18]
cikar=[0,1,2,4]; x=[kv[i] for i in cikar]
v=mean(x); assert v==9
e=[med(x),mean([kv[3],kv[5]]),sum(x),max(x)-min(x)]
assert e==[8,16,36,12] and len({v,*e})==5
sy=0.27
SK=fig(sutun_grafik(gun,kv,20,2,sy,[MAV,MAV,MAV,TUR,MAV,TUR],'Kitap sayısı'))
q('0001',tipId='ist-ortalama',tip='Ortalama ve veri ekleme',z='kolay',alt='Ortalama',kaz='Sütun grafiğinden değerleri okuyup seçilen günlerin aritmetik ortalamasını hesaplar.',kalip='hikâyeli',
 kart='K-AIS-01 (sütun grafiği) · altı günlük ödünç alma; iki gün dışarıda bırakılıp kalan dört günün ortalaması',
 metin='Bir ilçe halk kütüphanesi, bir haftanın altı çalışma gününde ödünç verdiği kitap sayısını şekildeki sütun grafiğiyle göstermiştir. Kütüphane yöneticisi, kampanya yapılan Perşembe ve Cumartesi günlerini hesaba katmadan kalan dört günün normal bir gün için ne kadar kitap verdiğini bilmek istiyor.\nBuna göre, Perşembe ve Cumartesi dışındaki dört günde günlük ortalama ödünç verilen kitap sayısı kaçtır?',
 dogru=v,yan=[(e[0],'Dört günün değerlerini küçükten büyüğe sıralayıp ortadaki iki değerin ortalamasını almış; ortalama yerine medyan bulmuş.','bilgi'),(e[1],'Dışarıda bırakılacak günleri seçmiş; Perşembe ve Cumartesi’nin ortalamasını hesaplamış.','dikkat'),(e[2],'Dört günün toplamını bulmuş, gün sayısına bölmeyi unutmuş.','islem'),(e[3],'Dört günün en büyük ve en küçük değerinin farkını (ranjı) bulmuş.','bilgi')],
 istenen='Perşembe ve Cumartesi dışındaki dört günde ödünç verilen günlük ortalama kitap sayısı.',ip=['Şekilde dışarıda tutulacak günlerin sütunları dışındakileri ızgaradan oku.'],bilgi=[ORT],sekil=SK,
 ad=[A('Dört günü oku','Pazartesi, Salı, Çarşamba ve Cuma sütunlarının yüksekliği ızgaradan okunur.','6, 16, 4, 10'),A('Toplamı bul','Okunan dört değer toplanır.','6 + 16 + 4 + 10 = 36'),A('Ortalamayı hesapla','Toplam gün sayısına bölünür.','36 / 4 = 9')],
 puf='Grafikten okuma yaparken önce hangi sütunların hesaba katılacağını işaretle.')

# ================= 02 kolay · öncüllü merkezî eğilim =================
D=[6,3,6,15,5,6,8]
assert mean(D)==7 and med(D)==6 and stt.mode(D)==6 and max(D)-min(D)==12
tr=[mean(D)>med(D),stt.mode(D)==med(D),max(D)-min(D)==10]; assert tr==[True,True,False]
dogru,yan=oncullu({0,1},['toplamı 49 yerine 42 bulup ortalamayı 6 sanmış','modu ortalamayla karıştırmış','en büyük değerden 5’i çıkarıp ranjı 10 bulmuş'])
q('0002',tipId='ist-merkez',tip='Medyan, mod ve ranj',z='kolay',alt='Merkezî Eğilim',kaz='Veri grubunun ortalama, medyan, mod ve ranjını bulup bunlar hakkındaki yargıları değerlendirir.',kalip='öncüllü',
 kart='K-AIS-03 (öncüllü merkezî eğilim) · yedi değerli veri; ortalama–medyan karşılaştırması, mod–medyan eşitliği, ranj',
 metin='Bir atletizm antrenörü, yedi sporcusunun bir günlük deneme koşusunda ölçülen sürelerini (saniye cinsinden) şu şekilde kaydetmiştir:\n6, 3, 6, 15, 5, 6, 8\nBu veri grubu için üç yargı ileri sürülmüştür.\nI. Aritmetik ortalama, medyandan büyüktür.\nII. Mod, medyana eşittir.\nIII. Ranj 10’dur.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='Verilen yargılardan doğru olanlar.',ip=['Önce değerleri küçükten büyüğe sırala; sonra her yargı için ilgili ölçüyü ayrı ayrı bul.'],bilgi=[MED],
 ad=[A('Sırala','Değerler küçükten büyüğe dizilir.','3, 5, 6, 6, 6, 8, 15'),A('Ölçüleri bul','Medyan ortadaki 4. değerdir; mod en çok tekrar eden değerdir; ortalama toplamın 7’ye bölümüdür.','Medyan 6 · mod 6 · ortalama 49 / 7 = 7 · ranj 15 − 3 = 12'),A('Yargıları değerlendir','I: 7 > 6 doğru · II: 6 = 6 doğru · III: ranj 12, 10 değil yanlış.','I ve II doğru')],
 puf='Ölçüleri ayrı ayrı hesaplamadan yargıyı sezgiyle değerlendirme.')

# ================= 03 kolay · tablo, ağırlıklı ortalama =================
d=[('Matematik',5,60),('Fizik',3,90),('Kimya',2,75)]
tw=sum(s for _,s,_ in d); v=Fr(sum(s*n for _,s,n in d),tw); assert v==72
e=[mean([n for *_,n in d]),Fr(sum(n for *_,n in d),tw),sum(s*n for _,s,n in d),Fr(sum(s*n for _,s,n in d),3)]
assert e==[75,Fr(45,2),720,240] and len({v,*e})==5
SK=tablo_svg(['Ders','Haftalık ders saati','Sınav notu'],[[a,str(s),str(n)] for a,s,n in d])
q('0003',tipId='ist-frekans',tip='Frekans tablosunda ortalama ve medyan',z='kolay',alt='Ağırlıklı Ortalama',kaz='Tabloda verilen değerlerin ağırlıklı ortalamasını hesaplar.',kalip='hikâyeli',
 kart='K-AIS-02 (ağırlıklı ortalama tablosu) · üç ders, haftalık ders saatleri ağırlık',
 metin='Bir özel lisenin burs sınavında adaylar, derslerin haftalık ders saatleriyle orantılı olacak biçimde ağırlıklı ortalamaya göre değerlendiriliyor. Bir adayın üç dersteki sınav notları ve o derslerin haftalık ders saatleri aşağıdaki tabloda verilmiştir.\nBuna göre, bu adayın ağırlıklı not ortalaması kaçtır?',
 dogru=v,yan=[(e[0],'Ders saatlerini hesaba katmamış, üç notun sade aritmetik ortalamasını almış.','bilgi'),(e[1],'Notları toplayıp toplam ders saatine bölmüş (225 / 10).','islem'),(e[2],'Not ile saatin çarpımlarını toplamış, toplam saate bölmeyi unutmuş.','islem'),(e[3],'Çarpımlar toplamını ders sayısına (3) bölmüş.','islem')],
 istenen='Adayın ağırlıklı not ortalaması.',ip=['Derslerin ortalamaya katkısı eşit mi, değil mi?'],bilgi=[AGR],sekil=SK,
 ad=[A('Çarpımları bul','Her sınav notu kendi haftalık ders saatiyle çarpılır.','5 × 60 + 3 × 90 + 2 × 75 = 300 + 270 + 150'),A('Çarpımları topla','Çarpımların toplamı bulunur.','720'),A('Saate böl','Toplam ders saati 5 + 3 + 2 = 10’dur; toplam bununla bölünür.','720 / 10 = 72')],
 puf='Ağırlıklı ortalamada bölen, ağırlıkların toplamıdır; değer sayısı değil.')

# ================= 04 kolay · daire grafiği =================
dl=[('Spor',144),('Müzik',96),('Satranç',72),('Resim',48)]; assert sum(a for _,a in dl)==360
N=480; kisi={n:Fr(a,360)*N for n,a in dl}; v=kisi['Spor']-kisi['Resim']; assert v==128
e=[dl[0][1]-dl[3][1],kisi['Spor'],kisi['Spor']+kisi['Resim'],kisi['Müzik']-kisi['Satranç']]
assert e==[96,192,256,32] and len({v,*e})==5
SK=fig(pie(dl))
q('0004',tipId='ist-daire',tip='Daire grafiğinden sayı ve ortalama',z='kolay',alt='Daire Grafiği',kaz='Daire grafiğindeki merkez açılardan kişi sayılarını bulup iki grubu karşılaştırır.',kalip='hikâyeli',
 kart='K-AIS-04 (daire grafiği) · 480 öğrencinin kulüp tercihi; iki dilimin kişi sayısı farkı',
 metin='480 öğrencinin okuduğu bir ortaokulda her öğrenci yalnızca bir kulübe kayıt yaptırmıştır. Kayıtların kulüplere göre dağılımı şekildeki daire grafiğinde merkez açıları ile gösterilmiştir.\nBuna göre, spor kulübüne kayıtlı öğrenci sayısı ile resim kulübüne kayıtlı öğrenci sayısı arasındaki fark kaçtır?',
 dogru=v,yan=[(e[0],'Merkez açılar arasındaki farkı (144° − 48°) doğrudan kişi sayısı sanmış.','bilgi'),(e[1],'Yalnız spor dilimini kişiye çevirmiş; resim dilimini çıkarmayı unutmuş.','dikkat'),(e[2],'İki dilimin kişi sayılarını çıkarmak yerine toplamış.','islem'),(e[3],'Farkı istenen iki dilim yerine müzik ve satranç dilimlerinin farkını almış.','dikkat')],
 istenen='Spor ve resim kulübüne kayıtlı öğrenci sayıları arasındaki fark.',ip=['Bir dilimin merkez açısı ile o dilimdeki kişi sayısı arasında nasıl bir ilişki var?'],bilgi=[DAI],sekil=SK,
 ad=[A('Açıları oku','Spor dilimi 144°, resim dilimi 48°dir.','144° ve 48°'),A('Kişi sayılarına çevir','Her açı 360°a bölünüp toplam öğrenci sayısıyla çarpılır.','144/360 × 480 = 192 · 48/360 × 480 = 64'),A('Farkı bul','İki kişi sayısı çıkarılır.','192 − 64 = 128')],
 puf='Açıyı önce kişi sayısına çevir, sonra farkı al.')

# ================= 05 orta · çıkarılan değerlerle varyans =================
n0,m0,v0=10,8,6; Sq=n0*(v0+m0**2); assert Sq==700
r=[12,4]; n1=n0-2; S1=n0*m0-sum(r); Q1_=Sq-sum(x*x for x in r); mn=Fr(S1,n1); assert mn==8
v=Fr(Q1_,n1)-mn**2; assert v==Fr(7,2)
e=[v0,Fr(Q1_,n1),Fr(28,10),28]; assert e==[6,Fr(135,2),Fr(14,5),28] and len({v,*e})==5
q('0005',tipId='ist-sapma',tip='Varyans ve standart sapma',z='orta',alt='Değer Çıkarılınca Varyans',kaz='Bir veri grubundan değerler çıkarıldığında ortalama ve varyanstaki değişimi hesaplar.',kalip='hikâyeli',
 kart='K-AIS-06 (değer çıkarma) · 10 değer, ortalama 8, varyans 6; 12 ve 4 çıkarılıyor',
 metin='Bir fabrikada 10 makinenin dakikada ürettiği parça sayılarının aritmetik ortalaması 8, varyansı 6 olarak hesaplanmıştır. Bakıma alınan iki makinenin üretimleri 12 ve 4 parçadır. Bu iki makine listeden çıkarıldığında kalan 8 makinenin üretimlerinin varyansı yeniden hesaplanacaktır.\nBuna göre, kalan 8 makinenin dakikada ürettiği parça sayılarının varyansı kaçtır?',
 dogru=v,yan=[(e[0],'Çıkarılan değerlerin ortalamaya eşit uzaklıkta olduğunu görüp varyansın hiç değişmediğini sanmış.','bilgi'),(e[1],'Kalan değerlerin kareler toplamını 8’e bölüp ortalamanın karesini çıkarmayı unutmuş.','bilgi'),(e[2],'Kalan sapma kareleri toplamını (28) yeni değer sayısı yerine eski değer sayısına (10) bölmüş.','islem'),(e[3],'Kalan sapma kareleri toplamını (28) değer sayısına bölmeyi unutmuş.','islem')],
 istenen='Kalan 8 makinenin üretimlerinin varyansı.',ip=['Varyansı ve ortalamayı kullanarak ilk gruptaki toplam bilgileri çıkar; çıkarılan değerlerin payını ayır.'],bilgi=[VAR,EKL],
 ad=[A('Eski toplamları bul','Toplam ve sapma kareleri toplamı, ortalama ve varyanstan bulunur.','Toplam 80 · sapma kareleri toplamı 10 × 6 = 60'),A('Çıkarılanların payı','12 ve 4 ortalama 8’den sırasıyla 4 birim uzaktır; kareleri çıkarılır.','Kalan ortalama (80 − 16) / 8 = 8 · 60 − 16 − 16 = 28'),A('Yeni varyans','Kalan sapma kareleri toplamı 8’e bölünür.','28 / 8 = 7/2 = 3,5')],
 puf='Değer çıkarırken önce ortalamanın değişip değişmediğini sapma kareleri toplamıyla birlikte düşün.')

# ================= 06 orta · frekans tablosu bilinmeyen + medyan =================
xs=[1,2,3,4]; fa,fb=3,6; fq=[4,fa,7,fb]; Nm=sum(fq); assert Nm==20
ort=Fr(sum(a*b for a,b in zip(xs,fq)),Nm); assert ort==Fr(11,4)
sol=[(a,b) for a in range(0,10) for b in range(0,10) if 4+a+7+b==20 and Fr(4+2*a+21+4*b,20)==ort]; assert sol==[(3,6)]
mdn=med([x for x,f in zip(xs,fq) for _ in range(f)]); assert mdn==3
v=(fb-fa)+mdn; assert v==6
e=[(fa-fb)+mdn,(fa+fb)+mdn,fb+mdn,fb-fa]; assert e==[0,12,9,3] and len({v,*e})==5
SK=tablo_svg(['Masadaki kişi sayısı','1','2','3','4'],[['Masa sayısı','4','a','7','b']])
q('0006',tipId='ist-frekans',tip='Frekans tablosunda ortalama ve medyan',z='orta',alt='Frekans Tablosu',kaz='Frekans tablosunda toplam ve ortalama bilgisinden iki bilinmeyen frekansı bulup medyanla birleştirir.',kalip='tablo',
 kart='K-AIS-02 (frekans tablosu, iki bilinmeyen) · 20 masa; ortalama 2,75; (b − a) + medyan',
 metin='Bir kafe, öğle saatinde dolu olan 20 masanın her birinde oturan kişi sayısını kaydetmiş ve kayıtları aşağıdaki frekans tablosuyla göstermiştir. Tabloda a ve b birer doğal sayıdır. Masaların her birinde oturan kişi sayısı ortalama 2,75 olarak hesaplanmıştır.\nBuna göre, b − a farkı ile masalardaki kişi sayılarının medyanının toplamı kaçtır?',
 dogru=v,yan=[(e[0],'a ve b’yi doğru bulmuş, farkı ters yönde (a − b) alıp medyanı eklemiş.','islem'),(e[1],'Yalnız a + b = 9 denklemini bulup fark yerine toplamı almış, medyanı eklemiş.','dikkat'),(e[2],'b değerini fark sanıp medyanı eklemiş.','dikkat'),(e[3],'b − a farkını bulup medyanı eklemeyi unutmuş.','dikkat')],
 istenen='b − a farkı ile kişi sayılarının medyanının toplamı.',ip=['Masa sayıları toplamı ve kişi sayıları toplamı için iki ayrı denklem yaz; medyanı bulmak için masaları kişi sayısına göre sıralı düşün.'],bilgi=[FRE,MED],sekil=SK,
 ad=[A('Masa toplamı','Frekansların toplamı 20’dir.','4 + a + 7 + b = 20 → a + b = 9'),A('Kişi toplamı','Ortalama × masa sayısı toplam kişi sayısını verir.','2,75 × 20 = 55 = 4 + 2a + 21 + 4b → 2a + 4b = 30'),A('Denklemleri çöz','İlk denklemden a = 9 − b yazılır.','18 − 2b + 4b = 30 → b = 6, a = 3'),A('Medyanı bul','Frekanslar 4, 3, 7, 6 olduğundan 10. ve 11. masa 3 kişilik gruptadır.','Medyan = 3'),A('Topla','Fark ile medyan toplanır.','(6 − 3) + 3 = 6')],
 puf='İki bilinmeyen için iki denklem kur; tablo tamamlanınca diğer ölçüleri tablodan oku.')

# ================= 07 orta · histogram ortalama =================
sn=[0,10,20,30,40,50]; fr=[4,8,10,12,6]; orta=[(a+b)//2 for a,b in zip(sn,sn[1:])]; Nn=sum(fr); assert Nn==40 and orta==[5,15,25,35,45]
v=Fr(sum(a*b for a,b in zip(orta,fr)),Nn); assert v==27
mod=orta[fr.index(max(fr))]
e=[Fr(sum(a*b for a,b in zip(sn[:-1],fr)),Nn),mean(orta),Fr(sum(a*b for a,b in zip(sn[1:],fr)),Nn),mod]
assert e==[22,25,32,35] and len({v,*e})==5
sy=0.28
SK=fig(histogram(sn,fr,14,2,sy,1.0,[MAV],'Kişi sayısı',ad_x='dk'))
q('0007',tipId='ist-histogram',tip='Histogramda sınıf orta noktaları',z='orta',alt='Histogram',kaz='Histogramda sınıf orta noktalarını kullanarak veri grubunun ortalamasını hesaplar.',kalip='grafik',
 kart='K-AIS-05 (histogram) · beş sınıflı bekleme süresi; sınıf orta noktalarına göre ortalama',
 metin='Bir diş kliniğinde randevusuz gelen hastaların bekleme süreleri (dakika) sınıflandırılmış ve şekildeki histogramla gösterilmiştir. Her sınıfa ait gözlemlerin, o sınıfın orta noktasındaki değere sahip olduğu kabul edilmektedir; alt sınır sınıfa dahil, üst sınır dahil değildir.\nBuna göre, hastaların ortalama bekleme süresi kaç dakikadır?',
 dogru=v,yan=[(e[0],'Orta nokta yerine her sınıfın alt sınırını frekansla çarpıp toplamış.','bilgi'),(e[1],'Frekansları hesaba katmayıp sınıf orta noktalarının sade ortalamasını almış.','bilgi'),(e[2],'Orta nokta yerine her sınıfın üst sınırını frekansla çarpıp toplamış.','bilgi'),(e[3],'En kalabalık sınıfın orta noktasını ortalama sanmış.','bilgi')],
 istenen='Hastaların ortalama bekleme süresi (dakika).',ip=['Her sınıfı tek bir değerle temsil edip bu değerin frekansını hesaba kat.'],bilgi=[HIS,ORT],sekil=SK,
 ad=[A('Sütunları oku','Sınıfların gözlem sayıları ızgaradan okunur.','4, 8, 10, 12, 6 (toplam 40)'),A('Orta noktaları yaz','Her sınıfın alt ve üst sınırının ortalaması alınır.','15, 25, 35, 45, 55'),A('Toplamı bul','Orta nokta × frekans çarpımları toplanır.','60 + 200 + 350 + 540 + 330 = 1080'),A('Ortalama','Toplam gözlem sayısına bölünür.','1080 / 40 = 27')],
 puf='Histogramda her sınıf bir değere indirilir: orta nokta × frekans.')

# ================= 08 orta · iki kutu grafiği, öncüllü =================
A_=(20,35,50,70,90); B_=(30,45,60,75,85)
caA=A_[3]-A_[1]; caB=B_[3]-B_[1]; rA=A_[4]-A_[0]; rB=B_[4]-B_[0]
tr=[caA<caB,A_[2]>B_[1],rB>rA]; assert tr==[False,True,False] and (caA,caB,rA,rB)==(35,30,70,55)
dogru,yan=oncullu({1},['A’nın ÇA’sı 35, B’ninki 30; 35 < 30 değildir','medyan 50, B’nin 1. çeyreği 45; 50 > 45 doğrudur','ranjlar A için 70, B için 55; B büyük değildir'])
# yanlış kümeler için nedenleri anlamlı yaz
def ned8(): return ['çeyrekler açıklığı yerine uç değerlere bakarak karar vermiş','medyanı yanlış okuyup 1. çeyrekle karşılaştırmamış','ranjı kutunun genişliği sanmış']
dogru,yan=oncullu({1},ned8())
SK=fig(xekseni(10,100,10,0.06,-1.0,'puan',kucuk=5,hg=3.2)+'\n'+kutu(1.6,*A_,0.06,MAV,'A',True)+'\n'+kutu(0.45,*B_,0.06,TUR,'B',True,alt=True),'\\footnotesize')
q('0008',tipId='ist-kutu',tip='Kutu grafiği ve çeyrekler',z='orta',alt='Kutu Grafikleri',kaz='İki kutu grafiğinden çeyrekler açıklığı, ranj ve medyanı okuyup yargıları değerlendirir.',kalip='öncüllü',
 kart='K-AIS-08 (iki kutu grafiği, öncüllü) · A ve B şubelerinin puanları; ÇA, ranj, medyan–Q1 karşılaştırması',
 metin='İki farklı dershanedeki A ve B şubelerinin aynı deneme sınavından aldıkları puanların dağılımı şekildeki kutu grafikleriyle gösterilmiştir. Her şubede kutunun sol ucu 1. çeyreği, sağ ucu 3. çeyreği, kutunun içindeki çizgi medyanı göstermektedir.\nBu grafikler için üç yargı ileri sürülmüştür.\nI. A şubesinin çeyrekler açıklığı, B şubesinin çeyrekler açıklığından küçüktür.\nII. A şubesinin medyanı, B şubesinin 1. çeyreğinden büyüktür.\nIII. B şubesinin ranjı, A şubesinin ranjından büyüktür.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='Verilen yargılardan doğru olanlar.',ip=['Her yargı için iki şubenin ilgili değerini (açıklık, medyan, ranj) grafikten ayrı ayrı oku.'],bilgi=[KUT],sekil=SK,
 ad=[A('A şubesini oku','Uç değerler, çeyrekler ve medyan grafikten okunur.','En küçük 20, Q1 35, medyan 50, Q3 70, en büyük 90'),A('B şubesini oku','Aynı değerler B için okunur.','En küçük 30, Q1 45, medyan 60, Q3 75, en büyük 85'),A('Ölçüleri hesapla','Çeyrekler açıklığı Q3 − Q1, ranj en büyük − en küçüktür.','A: 35 ve 70 · B: 30 ve 55'),A('Yargıları değerlendir','I: 35 < 30 yanlış · II: 50 > 45 doğru · III: 55 > 70 yanlış.','Yalnız II')],
 puf='Çeyrekler açıklığı kutunun genişliğidir, ranj ise bıyıkların toplam uzunluğu.')

# ================= 09 orta · medyan ile bilinmeyen =================
vals=[16,3,21,8,6]; sol=[x for x in range(-10,100) if med(vals+[x])==10]; assert sol==[12]
xx=sol[0]; allv=vals+[xx]; v=mean(allv); assert v==11
e=[mean(vals),mean(vals+[0]),med(allv),xx]; assert e==[Fr(54,5),9,10,12] and len({v,*e})==5
q('0009',tipId='ist-merkez',tip='Medyan, mod ve ranj',z='orta',alt='Medyan ve Bilinmeyen',kaz='Çift sayıda veride medyan koşulundan bilinmeyen değeri bulup ortalamayı hesaplar.',kalip='hikâyeli',
 kart='K-AIS-03 (medyandan bilinmeyen) · altı değer; medyan 10 verilip x ve ortalama',
 metin='Bir bisiklet sporcusu, hazırlık kampının altı gününde sırasıyla 16, 3, 21, 8, x ve 6 kilometre yol yapmıştır. Burada x bir tam sayıdır ve bu altı günlük yol uzunluklarının medyanı 10 kilometredir.\nBuna göre, sporcunun altı günde yaptığı yolun aritmetik ortalaması kaç kilometredir?',
 dogru=v,yan=[(e[0],'x’i hesaba katmadan yalnız bilinen beş değerin ortalamasını almış (54 / 5).','dikkat'),(e[1],'x yerine 0 koyup altı değerin ortalamasını almış.','dikkat'),(e[2],'Sorulan ortalama yerine verilen medyan değerini yazmış.','dikkat'),(e[3],'x’i bulduktan sonra ortalama yerine x’i yanıt yapmış.','dikkat')],
 istenen='Altı günlük yol uzunluklarının aritmetik ortalaması (km).',ip=['Altı değerde medyan hangi sıradaki değerlerle bulunur?'],bilgi=[MED,ORT],
 ad=[A('Bilinenleri sırala','Beş değer küçükten büyüğe dizilir.','3, 6, 8, 16, 21'),A('x’in yerini bul','Altı değerin medyanı 3. ve 4. değerin ortalamasıdır; 3. değer 8 ise 4. değer x olmalıdır.','(8 + x) / 2 = 10 → x = 12 (8 < 12 < 16 koşulu sağlanır)'),A('Toplamı bul','Altı değer toplanır.','3 + 6 + 8 + 16 + 21 + 12 = 66'),A('Ortalama','Toplam 6’ya bölünür.','66 / 6 = 11')],
 puf='Medyan koşulundan çıkan değer, varsayılan sıralamayla tutarlı mı diye mutlaka denetle.')

# ================= 10 orta · nokta diyagramı, varyans =================
dd=[2,2,2,6,6,6,8,8]; assert mean(dd)==5 and var(dd)==6
v=var(dd); e=[sum((a-5)**2 for a in dd),Fr(sum(abs(a-5) for a in dd),8),mean(dd),Fr(sum(a*a for a in dd),8)]
assert e==[48,Fr(9,4),5,31] and len({v,*e})==5
o=[]
for val,say in ((2,3),(6,3),(8,2)):
    for k in range(say): o.append(f'\\draw[fill={MAV},draw=black!70,thick] ({val*0.55:.3f},{0.2+k*0.42:.3f}) circle (0.18);')
SK=fig('\n'.join(o)+'\n'+xekseni(0,9,1,0.55,0,'gelme sayısı'))
q('0010',tipId='ist-sapma',tip='Varyans ve standart sapma',z='orta',alt='Varyans',kaz='Nokta diyagramından okunan veri grubunun varyansını tanımından hesaplar.',kalip='grafik',
 kart='K-AIS-06 (nokta diyagramı, varyans) · sekiz değer; ortalama 5, varyans 6',
 metin='Bir spor salonunda sekiz üyenin son bir ayda salona gelme sayıları şekildeki nokta diyagramında gösterilmiştir; her nokta bir üyeyi göstermektedir. Bu veri grubunun varyansı, değerlerin ortalamadan farklarının karelerinin toplamının değer sayısına bölünmesiyle hesaplanır.\nBuna göre, bu veri grubunun varyansı kaçtır?',
 dogru=v,yan=[(e[0],'Sapmaların karelerini toplamış, değer sayısına (8) bölmeyi unutmuş.','islem'),(e[1],'Sapmaların karesi yerine mutlak değerlerini alıp ortalamasını bulmuş.','bilgi'),(e[2],'Varyans yerine veri grubunun aritmetik ortalamasını yazmış.','dikkat'),(e[3],'Değerlerin karelerinin ortalamasını bulmuş, ortalamanın karesini çıkarmamış.','bilgi')],
 istenen='Veri grubunun varyansı.',ip=['Önce ortalamayı bul, sonra her değerin ortalamadan farkını yaz.'],bilgi=[VAR],sekil=SK,
 ad=[A('Değerleri oku','Noktalardan değerler okunur.','2, 2, 2, 6, 6, 6, 8, 8'),A('Ortalama','Değerlerin toplamı 8’e bölünür.','40 / 8 = 5'),A('Sapmaların kareleri','Her değerden 5 çıkarılıp karesi alınır.','3 × 9 + 3 × 1 + 2 × 9 = 27 + 3 + 18 = 48'),A('Varyans','Kareler toplamı 8’e bölünür.','48 / 8 = 6')],
 puf='Varyansı hesaplarken sapmaları önce karele, sonra topla, en son değer sayısına böl.')

# ================= 11 orta · yeni nesil varyans toplam formülü =================
nn,S,SQ=5,35,275; m=Fr(S,nn); v=Fr(SQ,nn)-m**2; assert v==6
e=[Fr(SQ,nn)-m,Fr(SQ,nn),m**2,SQ-m**2]; assert e==[48,55,49,226] and len({v,*e})==5
q('0011',tipId='ist-sapma',tip='Varyans ve standart sapma',z='orta',alt='Varyans İfadesi',kaz='Değerlerin toplamı ve kareleri toplamı verilen veri grubunun varyansını bulur.',kalip='yeni nesil',
 kart='K-AIS-06 (toplam ve kareler toplamı) · beş ölçüm; toplam 35, kareleri toplamı 275',
 metin='Bir laboratuvarda aynı numunenin sıcaklığı 5 kez ölçülmüş ve ölçüm sonuçları x₁, x₂, x₃, x₄, x₅ olarak kaydedilmiştir. Bu ölçümler için x₁ + x₂ + x₃ + x₄ + x₅ = 35 ve x₁² + x₂² + x₃² + x₄² + x₅² = 275 olduğu görülmüştür. Ölçüm sonuçlarının varyansı, sonuçların ortalamadan farklarının karelerinin ortalamasıdır.\nBuna göre, bu ölçüm sonuçlarının varyansı kaçtır?',
 dogru=v,yan=[(e[0],'Karelerin ortalamasından (55) ortalamanın karesi yerine ortalamayı (7) çıkarmış.','islem'),(e[1],'Karelerin ortalamasını (55) varyans sanmış.','bilgi'),(e[2],'Ortalamanın karesini (49) varyans sanmış.','bilgi'),(e[3],'Kareler toplamından ortalamanın karesini çıkarıp değer sayısına bölmeyi unutmuş.','islem')],
 istenen='Ölçüm sonuçlarının varyansı.',ip=['Ölçümler tek tek verilmediği için varyans ifadesini açıp verilen toplamlarla ilişkilendir.'],bilgi=[VAR],
 ad=[A('Ortalamayı bul','Toplam, ölçüm sayısına bölünür.','x̄ = 35 / 5 = 7'),A('Karelerin ortalaması','Kareler toplamı ölçüm sayısına bölünür.','275 / 5 = 55'),A('Varyansı yaz','Varyans = karelerin ortalaması − ortalamanın karesi.','55 − 7² = 55 − 49 = 6')],
 puf='Veriler tek tek verilmediğinde varyans ifadesini verilen toplamlara bağlayacak biçimde aç.')

# ================= 12 orta · kutu grafiği ve doğrusal dönüşüm =================
bx=(12,24,36,52,80); a_,b_=2,8
nm=a_*(bx[2]+b_); nca=a_*(bx[3]-bx[1]); v=nm+nca; assert (nm,nca,v)==(88,56,144)
e=[(a_*bx[2]+b_)+nca,nm+((bx[3]-bx[1])+b_),a_*bx[2]+nca,nm+(bx[3]-bx[1])]
assert e==[136,124,128,116] and len({v,*e})==5
SK=fig(kutu(0.5,*bx,0.07,MAV,None,True)+'\n'+xekseni(0,90,10,0.07,-0.2,'dk'))
q('0012',tipId='ist-kutu',tip='Kutu grafiği ve çeyrekler',z='orta',alt='Kutu Grafiği ve Dönüşüm',kaz='Kutu grafiğindeki medyan ve çeyrekler açıklığının doğrusal dönüşümden nasıl etkilendiğini bulur.',kalip='hikâyeli',
 kart='K-AIS-08 (kutu grafiği + dönüşüm) · medyan 36, Q1 24, Q3 52; yeni süre = 2(x + 8)',
 metin='Bir oyun uygulamasının 60 kullanıcısının günlük kullanım süreleri (dakika) şekildeki kutu grafiğiyle verilmiştir. Uygulamanın yazılımcısı, raporlama sistemindeki bir ayar nedeniyle her kullanıcının süresine önce 8 dakika eklenip çıkan sonucun 2 katını alarak yeni süreleri (x yerine 2(x + 8)) hesaplamıştır.\nBuna göre, yeni sürelerin medyanı ile çeyrekler açıklığının toplamı kaç dakikadır?',
 dogru=v,yan=[(e[0],'Dönüşümü sıra ters uygulayıp medyanı 2 × 36 + 8 olarak almış.','bilgi'),(e[1],'Çeyrekler açıklığına 8 ekleyip çarpanı uygulamamış (28 + 8).','bilgi'),(e[2],'Medyana 8 eklemeyi unutup yalnız 2 ile çarpmış (2 × 36).','bilgi'),(e[3],'Çeyrekler açıklığına çarpanı uygulamamış (28 dakikalık açıklığı değiştirmemiş).','bilgi')],
 istenen='Yeni sürelerin medyanı ile çeyrekler açıklığının toplamı.',ip=['Sabit eklemenin ve çarpanın medyan ile çeyrekler açıklığını ayrı ayrı nasıl değiştirdiğini düşün.'],bilgi=[KUT,DON],sekil=SK,
 ad=[A('Değerleri oku','Medyan ve çeyrekler grafikten okunur.','Q1 = 24, medyan = 36, Q3 = 52'),A('Yeni medyan','Medyan her işlemden aynı biçimde etkilenir.','2 × (36 + 8) = 88'),A('Yeni açıklık','Sabit ekleme farkı değiştirmez; yalnız çarpan etkiler.','2 × (52 − 24) = 56'),A('Topla','İki değer toplanır.','88 + 56 = 144')],
 puf='Dönüşümün her adımını konum ölçüsü ve yayılma ölçüsü için ayrı ayrı uygula.')

# ================= 13 orta · saçılım diyagramı, öncüllü =================
pts=[(1,35),(2,45),(2,50),(3,55),(4,60),(4,70),(5,75),(6,70)]
pos=sum((x-mean([p[0] for p in pts]))*(y-mean([p[1] for p in pts])) for x,y in pts)>0
m4=mean([y for x,y in pts if x==4]); allhi=all(x>=4 for x,y in pts if y>=60)
tr=[pos,m4==62,allhi]; assert tr==[True,False,True] and m4==65
ned=['çalışma süresi arttıkça puanın azaldığını sanmış','4 saat çalışanların puanlarından 70’i atlayıp ortalamayı hatalı bulmuş','60 puan ve üzerini alanlardan birinin 4 saatten az çalıştığını sanmış']
ned=['noktaların yükselen eğilimini görmemiş','3 saat çalışan öğrenciyi de katıp (55 + 60 + 70) / 3 ≈ 62 bulmuş','60 ve üzeri puan alan noktalardan birinin 4 saatin altında olduğunu sanmış']
dogru,yan=oncullu({0,2},ned)
o=[yizgara(7,80,10,0.07*1,False)] if False else []
sxs,sys_=0.62,0.058
g=[]
for j in range(30,81,5): g.append(f'\\draw[gray!{40 if j%10==0 else 22},thin] (0,{(j-30)*sys_:.3f}) -- ({7*sxs:.3f},{(j-30)*sys_:.3f});'+(f'\\node[left=2pt] at (0,{(j-30)*sys_:.3f}) {{${j}$}};' if j%10==0 else ''))
for i in range(1,8): g.append(f'\\draw[gray!40,thin] ({i*sxs:.3f},0) -- ({i*sxs:.3f},{50*sys_:.3f});\\node[below=2pt] at ({i*sxs:.3f},0) {{${i}$}};')
g.append(f'\\draw[-{{Stealth}},thick] (0,0) -- ({7.4*sxs:.3f},0) node[right] {{saat}}; \\draw[-{{Stealth}},thick] (0,0) -- (0,{52.5*sys_:.3f}) node[above] {{puan}};')
for x,y in pts: g.append(f'\\fill[{MAV},draw=black] ({x*sxs:.3f},{(y-30)*sys_:.3f}) circle (0.085);\\draw[black!70] ({x*sxs:.3f},{(y-30)*sys_:.3f}) circle (0.085);')
SK=fig('\n'.join(g))
q('0013',tipId='ist-sacilim',tip='Saçılım diyagramında yorum',z='orta',alt='Saçılım Diyagramı',kaz='Saçılım diyagramındaki noktalardan eğilim, grup ortalaması ve eşik koşullarını yorumlar.',kalip='öncüllü',
 kart='K-AIS-09 (saçılım diyagramı, öncüllü) · sekiz öğrenci; haftalık çalışma saati ve puan',
 metin='Bir dershanede sekiz öğrencinin haftalık çalışma süresi (saat) ile deneme sınavındaki puanı arasındaki ilişki şekildeki saçılım diyagramında gösterilmiştir; her nokta bir öğrenciyi göstermektedir.\nBu diyagram için üç yargı ileri sürülmüştür.\nI. Haftalık çalışma süresi arttıkça öğrencilerin puanları genel olarak artmaktadır.\nII. Haftada 4 saat çalışan öğrencilerin puan ortalaması 62’dir.\nIII. Puanı 60 ve üzeri olan her öğrenci haftada en az 4 saat çalışmaktadır.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='Verilen yargılardan doğru olanlar.',ip=['II. ve III. yargıları test etmek için ilgili noktaları ızgaradan tek tek oku.'],bilgi=[SAC,ORT],sekil=SK,
 ad=[A('Eğilimi yorumla','Noktalar soldan sağa yükseliyor; ilişki pozitiftir.','I doğru'),A('4 saat çalışanlar','Haftada 4 saat çalışan iki öğrencinin puanı okunur ve ortalaması alınır.','(60 + 70) / 2 = 65 → II yanlış'),A('Eşik koşulu','60 ve üzeri puanlı noktalar: (4, 60), (4, 70), (5, 75), (6, 70); hepsinin saati 4 veya daha fazladır.','III doğru'),A('Sonuç','Doğru olan yargılar belirlenir.','I ve III')],
 puf='Bir öncülü denetlerken önce ilgili noktaları grafikten tek tek yaz.')

# ================= 14 orta · frekans tablosu medyan, mod, ortalama =================
kv_=[0,1,2,3,4]; kf=[5,9,8,11,7]; Nn=sum(kf); assert Nn==40
exp=[x for x,f in zip(kv_,kf) for _ in range(f)]; assert med(exp)==2 and stt.mode(exp)==3 and mean(exp)==Fr(43,20)
v=med(exp)+stt.mode(exp)+mean(exp); assert v==Fr(143,20)
e=[2*mean(exp)+3,2+11+mean(exp),med(kf)+3+mean(exp),3+3+mean(exp)]; assert e==[Fr(73,10),Fr(303,20),Fr(263,20),Fr(163,20)] and len({v,*e})==5
SK=tablo_svg(['Kardeş sayısı']+[str(k) for k in kv_],[['Öğrenci sayısı']+[str(f) for f in kf]])
q('0014',tipId='ist-frekans',tip='Frekans tablosunda ortalama ve medyan',z='orta',alt='Frekans Tablosu Medyan',kaz='Frekans tablosunda medyan, mod ve ortalamayı bulup toplar.',kalip='tablo',
 kart='K-AIS-02 (frekans tablosu, medyan–mod–ortalama) · 40 öğrenci; kardeş sayısı 0–4',
 metin='Bir ortaokuldaki 40 öğrencinin kardeş sayıları sorulmuş ve cevaplar aşağıdaki frekans tablosunda gösterilmiştir. Kardeş sayıları küçükten büyüğe sıralandığında ortadaki değer medyan, en çok tekrar eden değer moddur.\nBuna göre, bu veri grubunun medyanı, modu ve aritmetik ortalamasının toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Medyan yerine de aritmetik ortalamayı (2,15) kullanıp ortalamayı iki kez saymış.','bilgi'),(e[1],'Mod olarak en büyük frekansı (11) almış.','bilgi'),(e[2],'Frekans değerlerini sıralayıp medyanını (8) almış.','bilgi'),(e[3],'Medyanı da mod ile aynı (3) sanmış.','islem')],
 istenen='Kardeş sayılarının medyanı, modu ve aritmetik ortalamasının toplamı.',ip=['Üç ölçüyü ayrı ayrı bul; frekanslar her birinde farklı biçimde kullanılır.'],bilgi=[MED,FRE],sekil=SK,
 ad=[A('Yığılmalı say','Frekanslar sırayla toplanır.','0: 5 · 1: 14 · 2: 22 · 3: 33 · 4: 40'),A('Medyan ve mod','40 değerde ortadaki 20. ve 21. değer 2’dir; en büyük frekans 3 değerindedir.','Medyan = 2 · mod = 3'),A('Ortalama','Değer × frekans toplamı 40’a bölünür.','(0 + 9 + 16 + 33 + 28) / 40 = 86 / 40 = 2,15'),A('Topla','Üç ölçü toplanır.','2 + 3 + 2,15 = 7,15')],
 puf='Mod frekansın kendisi değil, o frekansa sahip değerdir.')

# ================= 15 zor · histogram, bilinmeyen sütun =================
sn=[10,20,30,40,50,60]; fr=[4,12,8,None,12]; xv=4
fs=fr[:]; fs[3]=xv; orta=[15,25,35,45,55]
mm=Fr(sum(a*b for a,b in zip(orta,fs)),sum(fs)); assert mm==37 and sum(fs)==40
sol=[x for x in range(1,60) if Fr(sum(a*b for a,b in zip(orta,[4,12,8,x,12])),sum([4,12,8,x,12]))==37]; assert sol==[4]
v=xv+fr[4]; assert v==16
e=[8+12,4+12+8,4+12+8+4,sum(fs)]; assert e==[20,24,28,40] and len({v,*e})==5
sy=0.2
SK=fig(histogram(sn,[4,12,8,None,12],16,2,sy,1.0,[MAV],'Çalışan sayısı',bilinmeyen=3,ad_x='bin TL'))
q('0015',tipId='ist-histogram',tip='Histogramda sınıf orta noktaları',z='zor',alt='Histogram ve Ortalama',kaz='Histogramdaki bir sütunun yüksekliğini ortalama koşulundan bulup istenen gözlem sayısını hesaplar.',kalip='grafik',
 kart='K-AIS-05 (histogram, bilinmeyen sütun) · ortalama 37; x = 4; üst iki sınıfın toplamı',
 metin='Bir atölyedeki çalışanların aylık maaşları (bin TL) sınıflandırılarak şekildeki histogramla gösterilmiştir. x ile gösterilen sütun ölçekli çizilmemiştir ve x bir doğal sayıdır. Her sınıftaki maaşların, o sınıfın orta noktasında olduğu kabul edildiğinde çalışanların ortalama maaşı 37 bin TL olmaktadır.\nBuna göre, aylık maaşı 40 bin TL veya daha fazla olan çalışan sayısı kaçtır?',
 dogru=v,yan=[(e[0],'30–40 ve 50–60 sınıflarını (8 + 12) alıp 40–50 sınıfını katmamış.','dikkat'),(e[1],'40 bin TL’den az maaşlı çalışan sayısını (4 + 12 + 8) bulmuş.','dikkat'),(e[2],'50 bin TL’den az maaşlı çalışan sayısını (4 + 12 + 8 + 4) bulmuş.','dikkat'),(e[3],'Toplam çalışan sayısını sorulan değer sanmış.','dikkat')],
 istenen='Aylık maaşı en az 40 bin TL olan çalışan sayısı.',ip=['x’i bilinmeyen alıp ortalama koşulunu orta noktalar ve frekanslarla yaz.'],bilgi=[HIS,ORT],sekil=SK,
 ad=[A('Orta noktalar','Sınıf orta noktaları bulunur.','15, 25, 35, 45, 55'),A('Ortalama denklemi','Toplam = ortalama × çalışan sayısı.','(60 + 300 + 280 + 45x + 660) / (36 + x) = 37'),A('x’i çöz','Denklem düzenlenir.','1300 + 45x = 1332 + 37x → x = 4'),A('İstenen sayı','40 ve üzeri maaşlı çalışanlar son iki sütundadır.','x + 12 = 4 + 12 = 16')],
 puf='Bilinmeyen frekans içeren ortalama, toplam = ortalama × sayı denklemine dönüştürülür.')

# ================= 16 zor · iki grubun birleşik varyansı =================
g1=(12,19,12); g2=(8,24,2); N=g1[0]+g2[0]; M=Fr(g1[0]*g1[1]+g2[0]*g2[1],N); assert M==21
v=Fr(g1[0]*(g1[2]+(g1[1]-M)**2)+g2[0]*(g2[2]+(g2[1]-M)**2),N); assert v==14
w=Fr(g1[0]*g1[2]+g2[0]*g2[2],N); s=Fr(g1[2]+g2[2],2); b=v-w
e=[b,s,w,M]; assert e==[6,7,8,21] and len({v,*e})==5
SK=tablo_svg(['Grup','Kişi sayısı','Ortalama','Varyans'],[['A',str(g1[0]),str(g1[1]),str(g1[2])],['B',str(g2[0]),str(g2[1]),str(g2[2])]])
q('0016',tipId='ist-sapma',tip='Varyans ve standart sapma',z='zor',alt='Birleşik Varyans',kaz='İki grubun ortalama ve varyansından birleştirilmiş grubun varyansını hesaplar.',kalip='hikâyeli',
 kart='K-AIS-06 (iki grubun birleşimi) · gruplar 12 ve 8 kişi; ortalamalar 19 ve 24; varyanslar 12 ve 2',
 metin='Bir şirketin iki ayrı biriminde çalışan A ve B gruplarının günlük satış adetleri incelenmiştir. İki grubun kişi sayısı, satış adedi ortalaması ve varyansı aşağıdaki tabloda verilmiştir. Daha sonra iki grup birleştirilerek tek bir grup olarak değerlendirilmiştir.\nBuna göre, birleşik grubun satış adetlerinin varyansı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız grupların ortalamalarının birleşik ortalamadan sapmalarını hesaba katıp grup içi varyansı atlamış.','bilgi'),(e[1],'İki grubun varyanslarının sade ortalamasını almış.','bilgi'),(e[2],'Varyansları kişi sayılarıyla ağırlıklandırmış, grupların ortalamalarının birbirinden farkını hesaba katmamış.','bilgi'),(e[3],'Varyans yerine birleşik grubun ortalamasını yazmış.','dikkat')],
 istenen='Birleştirilmiş grubun varyansı.',ip=['Her grup için kareler toplamını Σx² = n(varyans + ortalama²) ilişkisinden yaz ve birleşik ortalamayı hesaba kat.'],bilgi=[VAR,ORT],sekil=SK,
 ad=[A('Birleşik ortalama','Toplamlar toplam kişiye bölünür.','(12 × 19 + 8 × 24) / 20 = 420 / 20 = 21'),A('Kareler toplamları','Her grup için Σx² = n(Var + ortalama²).','A: 12 × (12 + 361) = 4476 · B: 8 × (2 + 576) = 4624'),A('Birleşik kareler ortalaması','İki toplam toplanıp 20’ye bölünür.','(4476 + 4624) / 20 = 455'),A('Varyans','Karelerin ortalamasından ortalamanın karesi çıkarılır.','455 − 21² = 455 − 441 = 14')],
 puf='Gruplar birleşince varyans, grup içi dağılım artı ortalamalar arası dağılımdan oluşur.')

# ================= 17 orta · sütun grafiği, veri ekleme (öncüllü) =================
vk=[1,2,4,7,10]; fk=[2,3,2,2,1]; dat=[x for x,f in zip(vk,fk) for _ in range(f)]; assert mean(dat)==4 and len(dat)==10
dat2=dat+[4]
assert med(dat)==3 and med(dat2)==4 and var(dat)==Fr(42,5) and var(dat2)==Fr(84,11)
tr=[med(dat2)>med(dat),var(dat2)>8,max(dat2)-min(dat2)>9]; assert tr==[True,False,False]
ned=['yeni değer ortalamaya eşit olduğu için medyanın da değişmeyeceğini sanmış','yeni varyansı eski varyans olan 8,4 sanmış (84 / 11 ≈ 7,6 olduğunu görmemiş)','yeni değerle ranjın arttığını sanmış (1 ile 10 arasındaki değer ranjı değiştirmez)']
dogru,yan=oncullu({0},ned)
sy=0.5; w=5*0.9+0.2; g=[yizgara(w,4,1,sy)]
for i,(x_,f) in enumerate(zip(vk,fk)):
    x0=0.1+i*0.9+0.1; x1=x0+0.7
    g.append(f'\\draw[fill={TUR},draw=black!70,thick] ({x0:.3f},0) rectangle ({x1:.3f},{f*sy:.3f});\\node[below=2pt] at ({(x0+x1)/2:.3f},0) {{${x_}$}};')
g.append(eksen_xy(w+0.35,4.5*sy+0.4,'değer','frekans'))
SK=fig('\n'.join(g))
q('0017',tipId='ist-sapma',tip='Varyans ve standart sapma',z='orta',alt='Veri Ekleme ve Yayılma',kaz='Frekans grafiğiyle verilen bir gruba ortalamaya eşit değer eklendiğinde medyan, varyans ve ranjdaki değişimi yorumlar.',kalip='öncüllü',
 kart='K-AIS-06 (veri ekleme, öncüllü) · on gözlemli frekans grafiği; ortalamaya eşit değer eklenmesi',
 metin='Bir bilgisayar oyunundaki on oyuncunun bir turda topladığı yıldız sayıları şekildeki sütun grafiğinde (yatay eksende yıldız sayısı, dikey eksende oyuncu sayısı) verilmiştir. Bu on oyuncuya, yıldız sayısı bu grubun aritmetik ortalamasına eşit olan bir on birinci oyuncu daha katılmıştır.\nOn bir oyunculu yeni grup için üç yargı ileri sürülmüştür.\nI. Medyan artmıştır.\nII. Varyans 8’den büyüktür.\nIII. Ranj 9’dan büyüktür.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='Yeni grup için doğru olan yargılar.',ip=['Grafikten ortalamayı, ilk grubun medyanını ve kareler toplamını bul; yeni değerin etkisini ayrı ayrı incele.'],bilgi=[VAR,EKL,MED],sekil=SK,
 ad=[A('Veriyi oku','Sütunlardan değerler ve frekanslar okunur.','1 (2 kez), 2 (3 kez), 4 (2 kez), 7 (2 kez), 10 (1 kez)'),A('Ortalama ve medyan','Ortalama 4; yeni değer 4’tür. Medyan 5. ve 6. değerin ortalamasıdır.','Eski medyan (2 + 4) / 2 = 3 · yeni medyan 4 → I doğru'),A('Varyans','Yeni değerin sapması 0 olduğundan kareler toplamı (84) aynı kalır, bölen 11 olur.','84 / 11 ≈ 7,6 < 8 → II yanlış'),A('Ranj','En küçük 1, en büyük 10 kalır.','10 − 1 = 9, 9’dan büyük değil → III yanlış')],
 puf='Yargıları rastgele düşünme; her birini grafikten okuduğun veriyle hesapla.')

# ================= 18 orta · daire grafiği + varyans =================
dg=[(40,60),(60,90),(70,120),(80,90)]; per=15; nn=24; cnt=[a//per for _,a in dg]; assert cnt==[4,6,8,6] and sum(cnt)==nn and sum(a for _,a in dg)==360
dd=[p for (p,_),c in zip(dg,cnt) for _ in range(c)]; mu=mean(dd); assert mu==65
v=var(dd); assert v==175
e=[sum((p-mu)**2 for p in dd),Fr(sum(p*p for p in dd),nn),Fr(sum(p*p for p in dd),nn)-mu,Fr(sum((p-mu)**2 for p,_ in dg),4)]
assert e==[4200,4400,4335,225] and len({v,*e})==5
SK=fig(pie([(f'{p} puan',a) for p,a in dg]))
q('0018',tipId='ist-daire',tip='Daire grafiğinden sayı ve ortalama',z='orta',alt='Daire Grafiği ve Varyans',kaz='Merkez açılardan kişi sayılarını bulup puanların varyansını hesaplar.',kalip='hikâyeli',
 kart='K-AIS-04 (daire grafiği + varyans) · 24 öğrenci; 40, 60, 70, 80 puan dilimleri',
 metin='24 öğrencinin katıldığı bir kodlama yarışmasında her öğrenci 40, 60, 70 ya da 80 puandan yalnızca birini almıştır. Puanların öğrenciler arasındaki dağılımı şekildeki daire grafiğinde merkez açılarla gösterilmiştir. Puanların varyansı, puanların ortalamadan farklarının karelerinin ortalamasıdır.\nBuna göre, bu 24 öğrencinin puanlarının varyansı kaçtır?',
 dogru=v,yan=[(e[0],'Sapmaların karelerinin toplamını bulup öğrenci sayısına (24) bölmeyi unutmuş.','islem'),(e[1],'Puanların karelerinin ortalamasını bulup ortalamanın karesini çıkarmamış.','bilgi'),(e[2],'Karelerin ortalamasından ortalamanın karesi yerine ortalamayı (65) çıkarmış.','islem'),(e[3],'Dört puan değerini frekanslarını hesaba katmadan eşit ağırlıkla ele almış.','bilgi')],
 istenen='24 öğrencinin puanlarının varyansı.',ip=['Önce her merkez açının kaç öğrenciyi gösterdiğini bul; 24 öğrenci 360° ye bölünür.'],bilgi=[DAI,VAR],sekil=SK,
 ad=[A('Açıdan kişiye','Tam daire 24 öğrenciyi gösterir; 1 öğrenci 360° / 24 = 15° tutar.','60° → 4 · 90° → 6 · 120° → 8 · 90° → 6'),A('Ortalamayı bul','Her puan, öğrenci sayısıyla çarpılıp toplanır.','(160 + 360 + 560 + 480) / 24 = 1560 / 24 = 65'),A('Sapma kareleri','Her puanın ortalamadan farkının karesi, öğrenci sayısıyla çarpılıp toplanır.','4 × 625 + 6 × 25 + 8 × 25 + 6 × 225 = 4200'),A('Varyans','Toplam 24’e bölünür.','4200 / 24 = 175')],
 puf='Daire grafiğinde açılar oran verir; önce kişi sayısına çevir, sonra yayılma ölçüsünü kur.')

# ================= 19 zor · kutu grafiği, bilinmeyen iki değer =================
bk=(9,15,21,28,40); known=[9,12,18,20,22,25,28,31,40]
sol=[(a,b) for a in range(1,61) for b in range(a,61) if (lambda d:(d[2],d[5],d[8])==(bk[1],bk[2],bk[3]) and d[0]==bk[0] and d[10]==bk[4])(sorted(known+[a,b]))]
assert sol==[(15,21)]; a,b=sol[0]; v=a+b; assert v==36
e=[bk[1],bk[2],bk[4]-bk[0],bk[3]]; assert e==[15,21,31,28] and len({v,*e})==5
SK=fig(kutu(0.5,*bk,0.14,TUR,None,True)+'\n'+xekseni(0,45,5,0.14,-0.2,'TL',kucuk=None),'\\footnotesize')
q('0019',tipId='ist-kutu',tip='Kutu grafiği ve çeyrekler',z='zor',alt='Kutu Grafiği ve Bilinmeyenler',kaz='Kutu grafiğindeki çeyrek ve medyan değerlerinden sıralı veride iki bilinmeyeni bulur.',kalip='hikâyeli',
 kart='K-AIS-08 (kutu grafiği, iki bilinmeyen) · on bir değer; Q1 = 15, medyan = 21, Q3 = 28',
 metin='Bir kantinde bir ay boyunca rastgele seçilen 11 satış fişindeki tutarlar (TL) şu şekilde kaydedilmiştir:\n25, 9, 40, 18, a, 31, 22, 12, b, 20, 28\nBurada a ve b tam sayılardır. Bu 11 tutarın kutu grafiği şekilde verilmiştir; değer sayısı tek olduğundan 1. çeyrek, medyanın altındaki 5 değerin medyanı; 3. çeyrek, medyanın üstündeki 5 değerin medyanıdır.\nBuna göre, a + b toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız a değerini (1. çeyrek) bulup b’yi katmamış.','dikkat'),(e[1],'Yalnız b değerini (medyan) bulup a’yı katmamış.','dikkat'),(e[2],'a + b yerine en büyük ile en küçük değerin farkını (ranjı) yazmış.','dikkat'),(e[3],'a + b yerine 3. çeyrek değerini yazmış.','dikkat')],
 istenen='a ve b tam sayılarının toplamı.',ip=['11 değerde çeyrekler ve medyan kaçıncı sıradadır?'],bilgi=[KUT],sekil=SK,
 ad=[A('Grafikten oku','Q1, medyan ve Q3 grafikten okunur; sıralı 11 değerdeki konumları belirlenir.','Q1 = 15, medyan = 21, Q3 = 28'),A('Bilinenleri sırala','Verilen 9 sayı dizilir.','9, 12, 18, 20, 22, 25, 28, 31, 40'),A('Medyanı kur','Bu dizide 21 yoktur; 6. değer 21 olabilmesi için bilinmeyenlerden biri 21 olmalıdır.','b = 21 (a ya da b)'),A('Q1’i kur','3. değerin 15 olması için diğer bilinmeyen 12 ile 18 arasında 15 olmalıdır.','a = 15 → sıralı: 9, 12, 15, 18, 20, 21, 22, 25, 28, 31, 40'),A('Topla','İki bilinmeyen toplanır.','15 + 21 = 36')],
 puf='Çeyrek ve medyanı değer değil sıra numarası olarak düşünüp bilinmeyenin yerini belirle.')

# ================= 20 zor · yeni nesil çift dönüşüm =================
mz,sz=-30,18; my=Fr(mz-10,-2); sdy=Fr(sz,2); mxx=(my+4)/3; sdx=sdy/3; vx=sdx**2
assert (my,sdy,mxx,sdx,vx)==(20,9,8,3,9) and mxx+vx==17
v=mxx+vx
e=[mxx,mxx+sdx,sdx+sdy,mxx+Fr(sz,3)]
assert e==[8,11,12,14] and len({v,*e})==5
q('0020',tipId='ist-donusum',tip='Doğrusal dönüşümün etkisi',z='orta',alt='Çift Dönüşüm',kaz='Ardışık iki doğrusal dönüşümden sonraki ortalama ve standart sapmadan ilk veri grubunun ortalama ve varyansını bulur.',kalip='yeni nesil',
 kart='K-AIS-07 (ardışık dönüşüm) · y = 3x − 4, z = −2y + 10; z için ortalama −30, standart sapma 18',
 metin='Bir veri grubunun x değerleri önce y = 3x − 4 kuralıyla y değerlerine, sonra z = −2y + 10 kuralıyla z değerlerine dönüştürülmüştür. Elde edilen z değerlerinin aritmetik ortalaması −30, standart sapması 18 olduğuna göre, ilk veri grubunun (x değerlerinin) aritmetik ortalaması ile varyansının toplamı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız ilk grubun ortalamasını (8) bulup varyansı eklememiş.','dikkat'),(e[1],'Varyans yerine standart sapmayı (3) ekleyerek 8 + 3 yazmış.','dikkat'),(e[2],'x ve y gruplarının standart sapmalarını (3 + 9) toplamış.','dikkat'),(e[3],'z’nin standart sapmasını yalnız 3’e bölüp (6) ortalamaya eklemiş; −2 çarpanını hesaba katmamış.','islem')],
 istenen='x değerlerinin aritmetik ortalaması ile varyansının toplamı.',ip=['Dönüşümleri tersten, sondan başa doğru çöz; sapma için katsayının mutlak değerini kullan.'],bilgi=[DON,VAR],
 ad=[A('z’den y’ye','z = −2y + 10 olduğundan y ortalaması ve sapması geri bulunur.','ȳ = (−30 − 10) / (−2) = 20 · sapma = 18 / 2 = 9'),A('y’den x’e','y = 3x − 4 olduğundan aynı işlem tekrarlanır.','x̄ = (20 + 4) / 3 = 8 · sapma = 9 / 3 = 3'),A('Varyansı bul','Varyans standart sapmanın karesidir.','3² = 9'),A('Toplam','Ortalama ile varyans toplanır.','8 + 9 = 17')],
 puf='Doğrusal dönüşümleri geri alırken ortalamada ekleneni çıkar, sapmada yalnız çarpanın mutlak değerine böl.')

# ---------- bitiş ----------
def bitir_ayt():
    for q_ in P.ANA: q_['kardes']=None
    P.yaz(os.path.join(AD,'istat-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-istat.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: MEB 11–12. sınıf matematik (veri analizi), ÖSYM AYT 2018–2025 ve yayın bankalarının mantık taraması.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','istat.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ayt()
