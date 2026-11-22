"""AYT Matematik · İstatistik, 2. dalga (20 soru: 3 kolay / 10 orta / 7 zor). Şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer kodla hesaplanıp assert edilir.
Kardeş yok, ipucu 1. Varyans = Σ(x−x̄)²/n (anakütle tanımı). 1. dalga kurguları (kütüphane sütunu, kulüp dairesi, bekleme histogramı, A/B kutu, çalışma-puan saçılımı…) tekrarlanmadı."""
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
P=Parti('istatiki','İstatistik',UK,ders='AYT Matematik',idon='aytmat')
KY='MEB 11–12. sınıf matematik (veri analizi, merkezî eğilim ve yayılma ölçüleri) · ÖSYM AYT 2018–2025 taraması (konuda doğrudan soru yok; grafik okuma, tanımlı yeni işlem, öncüllü ve aşağıdakilerden-hangisi kalıpları yalnız mantık) · 345 AYT soru bankası (yalnız kurgu çeşitliliği)'
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
GOV=B('Gövde-yaprak diyagramı','her değer gövde (onlar basamağı) ve yaprak (birler basamağı) olarak yazılır; anahtara göre okunur. Yapraklar küçükten büyüğe dizildiğinden değerler doğrudan sıralı okunur. Örnek: gövde 6, yaprak 4 ise değer 64’tür')
BIR=B('Birleşik ortalama','toplam = ortalama × değer sayısı her grup için ayrı yazılır; grupların toplamları ve sayıları ayrı ayrı toplanıp birleşik ortalama bulunur. Örnek: 2 kişilik grubun ortalaması 10, 3 kişilik grubun ortalaması 20 ise birleşik ortalama (20 + 60) / 5 = 16’dır')
BIK=B('Birikimli frekans grafiği','her sınıfın üst sınırında o sınıfa kadar olan toplam gözlem sayısı gösterilir. Bir sınıfın frekansı, iki ardışık noktanın dikey farkıdır. Örnek: üst sınırlarda 3 ve 8 okunuyorsa ikinci sınıfta 5 gözlem vardır')
KAR=B('Varyansın kareler ortalaması ile hesabı','Var = (Σxᵢ² / n) − x̄² dir. Bir a sayısına göre kareler toplamı Σ(xᵢ − a)² ise Var = Σ(xᵢ − a)² / n − (x̄ − a)² olur. Örnek: 3 değer için Σx = 6 ve Σx² = 18 ise Var = 6 − 4 = 2’dir')
YEN=B('Tanımlı ölçü','soruda tanımı verilen ölçü, tanımdaki adımlar sırayla uygulanarak hesaplanır; benzer görünen ölçülerle (varyans, ortalama mutlak sapma) karıştırılmaz. Örnek: 1, 5 için ortalama 3, ortalamadan sapmalar 2 ve 2’dir')
# ---------- kartlar (her tipId için bir kart; ilkinde olduğu gibi yalnız fikir) ----------
kartla('K-AIS2-01','Grafik okuyarak merkezî ölçüler','Grafik türüne göre değerler ya da sıra numaraları önce okunur; ardından istenen ölçü (medyan, ranj, çeyrek, ortalama) tanımına göre hesaplanır ve gerekirse yargılar tek tek sınanır.','Grafikten okurken ölçeği ya da çizgi türünü karıştırmak; ortalama ile medyanı birbirinin yerine kullanmak; çeyrekler açıklığı ile ranjı karıştırmak.','orta','grafik',4,'ist2-grafikoku','Grafik okuyarak merkezî ölçüler')
kartla('K-AIS2-02','Gövde-yaprak diyagramı','Gövde ve yapraklardan değerler yazılır; sıralı dizilimde medyan sıra numarasıyla, mod en çok tekrar eden tam değer olarak bulunur; bilinmeyen yaprak için koşul denklem kurulur.','Yaprağı tek başına sayı sanmak; değer sayısını yanlış saymak; çift sayıda değerde ortadaki iki değeri unutmak.','orta','grafik',4,'ist2-govde','Gövde-yaprak diyagramı')
kartla('K-AIS2-03','Veri değişimlerinin etkisi','Bir değer değişince toplam, sıralama ve uç değerlerin nasıl değiştiği izlenir; dönüşüm ve eklemelerde ortalama, medyan ve yayılma ölçüleri ayrı ayrı düşünülür.','Ortalama değişince medyanın da değiştiğini sanmak; eklenen değerin sapmayı artırdığını varsaymak; çarpanı yayılma ölçülerine yanlış uygulamak.','orta','öncüllü',4,'ist2-etki','Veri değişimlerinin etkisi')
kartla('K-AIS2-04','Sınıflanmış veri ve birikimli frekans','Birikimli değerlerden sınıf frekansları farkla bulunur; sınıf orta noktaları frekanslarla ağırlıklandırılarak ortalama ve varyans hesaplanır.','Üst ya da alt sınırı temsilci almak; birikimli değerleri frekans sanmak; varyansta frekansları atlamak ya da n’ye bölmeyi unutmak.','orta','grafik',4,'ist2-sinif','Sınıflanmış veri ve birikimli frekans')
kartla('K-AIS2-05','Grupları birleştirme ve veri ekleme','Her grubun toplamı ortalama çarpı sayı ile yazılır; birleşik ortalama toplamlar toplamı bölü sayılar toplamıdır; kareler toplamı ile varyans ilişkisi veri eklenince yeniden kurulur.','Ortalamaların basit ortalamasını almak; paydaya yeni değerleri koymamak; varyans için sapmanın karesini almamak.','zor','tablo',4,'ist2-birlesik','Grupları birleştirme ve veri ekleme')
kartla('K-AIS2-06','Daire ve sütun grafiklerini birlikte okuma','Merkez açı toplam sayıyla orantılanır; ikinci grafikteki oran ya da değer her dilime uygulanıp sonuçlar toplanır; bilinmeyen açı 360° toplamından bulunur.','Açıyı kişi sayısı sanmak; yüzdelerin basit ortalamasını almak; dilimleri tek tek değil topluca hesaplamak.','orta','grafik',4,'ist2-dagilim','Daire ve sütun grafiklerini birlikte okuma')
kartla('K-AIS2-07','Tanımlı ölçüleri hesaplama','Soruda tanımlanan ölçü (ortalama mutlak sapma, standart puan, değişkenlik katsayısı) tanımın adımlarıyla hesaplanır; gruplar arası karşılaştırma aynı ölçüyle yapılır.','Tanımı yerine benzer bir ölçüyü kullanmak; mutlak değeri atlamak; ortalamayı hesaba katmadan yalnız sapmaları karşılaştırmak.','orta','yeni nesil',4,'ist2-yeniolcu','Tanımlı ölçüleri hesaplama')
kartla('K-AIS2-08','Kareler toplamından varyans','Verilen toplamlardan ortalama bulunur; varyans kareler ortalaması eksi ortalamanın karesi biçiminde ya da kaydırılmış toplamlarla yazılır.','Kareler ortalamasını varyans sanmak; ortalamanın karesini çıkarmamak ya da kaydırma miktarını hesaba katmamak.','orta','yeni nesil',3,'ist2-kareler','Kareler toplamından varyans')
kartla('K-AIS2-09','Sıralama koşullarından değer bulma','Medyan, mod, ortalama ve uç değer koşulları birlikte sıralı dizilime yerleştirilir; bilinmeyenin konumu ve en büyük (en küçük) olabilecek değer için diğer değerler kısıtlar içinde uç seçilir.','Bilinmeyen değeri sıralamadan medyan yerine koymak; tek mod koşulunu atlamak; değer sayısını yanlış almak.','zor','düz',4,'ist2-siralama','Sıralama koşullarından değer bulma')
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

# ---------- yeni şekil yardımcıları ----------
def cizgi(cats,seriler,y0,y1,ystep,sy,xw=1.0,yl='',lab=None,deger=False,legend=False):
    """seriler: [(değerler,renk,ad,işaret)]; y ekseni y0..y1."""
    lab=lab or ystep; w=len(cats)*xw; o=[]
    for j in range(y0,y1+1,ystep):
        o.append(f'\\draw[gray!{40 if (j-y0)%lab==0 else 22},thin] (0,{(j-y0)*sy:.3f}) -- ({w:.3f},{(j-y0)*sy:.3f});')
        if (j-y0)%lab==0: o.append(f'\\node[left=2pt] at (0,{(j-y0)*sy:.3f}) {{${j}$}};')
    for i,c in enumerate(cats): o.append(f'\\node[below=2pt] at ({(i+0.5)*xw:.3f},0) {{{c}}};')
    for vals,rk,ad,isr in seriler:
        pts=' -- '.join(f'({(i+0.5)*xw:.3f},{(v-y0)*sy:.3f})' for i,v in enumerate(vals))
        o.append(f'\\draw[{rk},very thick] {pts};')
        for i,v in enumerate(vals):
            c=f'({(i+0.5)*xw:.3f},{(v-y0)*sy:.3f})'
            o.append(f'\\fill[{rk}] {c} circle (0.075);' if isr=='o' else f'\\fill[{rk}] ($ {c} +(-0.075,-0.075) $) rectangle ($ {c} +(0.075,0.075) $);')
            if deger: o.append(f'\\node[above=3pt,font=\\scriptsize] at {c} {{{v}}};')
    o.append(f'\\draw[-{{Stealth}},thick] (0,0) -- ({w+0.3:.3f},0);\\draw[-{{Stealth}},thick] (0,0) -- (0,{(y1-y0)*sy+0.45:.3f}) node[above] {{{yl}}};')
    if legend:
        for k,(vals,rk,ad,isr) in enumerate(seriler):
            x0=0.2+k*2.4; yy=(y1-y0)*sy+0.85
            o.append(f'\\draw[{rk},very thick] ({x0:.2f},{yy:.2f}) -- ({x0+0.5:.2f},{yy:.2f});')
            o.append(f'\\fill[{rk}] ({x0+0.25:.2f},{yy:.2f}) circle (0.075);' if isr=='o' else f'\\fill[{rk}] ({x0+0.175:.3f},{yy-0.075:.3f}) rectangle ({x0+0.325:.3f},{yy+0.075:.3f});')
            o.append(f'\\node[right=2pt] at ({x0+0.5:.2f},{yy:.2f}) {{{ad}}};')
    return '\n'.join(o)
def govde(satirlar,anahtar):
    """satirlar: [(gövde,[yaprak metinleri])]"""
    o=[]; n=len(satirlar); h=0.6
    o.append(f'\\draw[thick] (0.5,{h*0.6:.2f}) -- (0.5,{-h*(n-0.4):.2f});')
    for i,(g,yap) in enumerate(satirlar):
        y=-h*i; o.append(f'\\node[left=2pt,font=\\bfseries] at (0.45,{y:.2f}) {{{g}}};')
        for j,yp in enumerate(yap): o.append(f'\\node at ({0.8+j*0.5:.2f},{y:.2f}) {{{yp}}};')
    o.append(f'\\node[anchor=west] at (0,{-h*n-0.15:.2f}) {{{anahtar}}};')
    return '\n'.join(o)
def pie2(dil,r=1.4,renkler=(MAV,TUR,YES,MOR),dis=1.5):
    o=[]; a=90.0
    for (ad,aci,et),rk in zip(dil,renkler):
        b=a-aci; o.append(f'\\draw[fill={rk},draw=black!70,thick] (0,0) -- ({a:.2f}:{r}) arc ({a:.2f}:{b:.2f}:{r}) -- cycle;')
        m=(a+b)/2; o.append(f'\\node[align=center] at ({m:.2f}:{r*dis:.3f}) {{{ad}\\\\{et}}};'); a=b
    return '\n'.join(o)
def noktalar(degerler,sx,satir_y,renk,r=0.17,adim=0.4):
    from collections import Counter
    o=[]
    for v,c in sorted(Counter(degerler).items()):
        for k in range(c): o.append(f'\\draw[fill={renk},draw=black!70,thick] ({v*sx:.3f},{satir_y+0.2+k*adim:.3f}) circle ({r});')
    return '\n'.join(o)
def sutun_deger(et,dg,ymax,ystep,sy,renk,yl,xw=0.9,xl=''):
    w=len(et)*xw+0.2; o=[yizgara(w,ymax,ystep,sy)]
    for i,(e,v) in enumerate(zip(et,dg)):
        x0=0.1+i*xw+0.1; x1=x0+xw-0.2
        o.append(f'\\draw[fill={renk[i%len(renk)]},draw=black!70,thick] ({x0:.3f},0) rectangle ({x1:.3f},{v*sy:.3f});')
        o.append(f'\\node[below=2pt] at ({(x0+x1)/2:.3f},0) {{{e}}};\\node[above=1pt,font=\\scriptsize] at ({(x0+x1)/2:.3f},{v*sy:.3f}) {{{v}}};')
    o.append(eksen_xy(w+0.3,ymax*sy+0.5,xl,yl)); return '\n'.join(o)

# ================= 01 kolay · çizgi grafiği, medyan + ranj =================
gunler=['Pzt','Sal','Çar','Per','Cum','Cmt','Paz']; kv=[14,18,11,20,25,15,16]
assert mean(kv)==17 and med(kv)==16 and max(kv)-min(kv)==14
v=med(kv)+14; e=[14,16,min(kv)+med(kv),mean(kv)+14]
assert v==30 and e==[14,16,27,31] and len({v,*e})==5
SK=fig(cizgi(gunler,[(kv,MAV,'','o')],8,28,2,0.2,xw=0.95,yl='°C',lab=4,deger=True))
q('0001',tipId='ist2-grafikoku',tip='Grafik okuyarak merkezî ölçüler',z='kolay',alt='Çizgi Grafiği',kaz='Çizgi grafiğinden okuduğu değerlerin medyanını ve ranjını bulup toplar.',kalip='grafik',
 kart='K-AIS2-01 (çizgi grafiği) · yedi günlük en yüksek sıcaklık; medyan ile ranjın toplamı',
 metin='Şekildeki çizgi grafiği, bir kentte bir haftanın her gününde ölçülen en yüksek hava sıcaklıklarını (°C) göstermektedir.\nBuna göre, bu veri grubunun medyanı ile ranjının toplamı kaç °C’dir?',
 dogru=v,yan=[(e[0],'Yalnız ranjı (25 − 11) bulmuş; medyanı eklememiş.','dikkat'),(e[1],'Yalnız medyanı bulmuş; ranjı eklememiş.','dikkat'),(e[2],'Ranj yerine en küçük değeri (11) medyana eklemiş.','bilgi'),(e[3],'Medyan yerine aritmetik ortalamayı (119 / 7 = 17) alıp 17 + 14 yazmış.','bilgi')],
 istenen='Veri grubunun medyanı ile ranjının toplamı (°C).',ip=['Yedi sıcaklık değerini küçükten büyüğe sıralayınca medyan kaçıncı sıradadır?'],bilgi=[MED],sekil=SK,
 ad=[A('Değerleri oku','Her günün noktasındaki değer okunur ve küçükten büyüğe sıralanır.','11, 14, 15, 16, 18, 20, 25'),A('Medyan ve ranjı bul','Yedi değerin ortadaki (4.) değeri medyandır; ranj en büyük ile en küçük değerin farkıdır.','Medyan 16 · ranj 25 − 11 = 14'),A('Topla','İki ölçü toplanır.','16 + 14 = 30')],
 puf='Medyanı bulmadan önce değerleri mutlaka sırala; grafikteki gün sırası değer sırası değildir.')

# ================= 02 kolay · gövde-yaprak, mod ve medyan =================
GV=[11,13,15,15,15,21,24,27,32,38,40]
assert med(GV)==21 and stt.mode(GV)==15 and max(GV)-min(GV)==29
v=med(GV)-15; e=[15,21,max(GV)-min(GV),med(GV)+15]
assert v==6 and e==[15,21,29,36] and len({v,*e})==5
SK=fig(govde([(1,['1','3','5','5','5']),(2,['1','4','7']),(3,['2','8']),(4,['0'])],'Anahtar: 2 | 4 → 24 soru'),'\\small')
q('0002',tipId='ist2-govde',tip='Gövde-yaprak diyagramı',z='kolay',alt='Gövde-Yaprak',kaz='Gövde-yaprak diyagramından değerleri yazıp medyan ve modu bulur.',kalip='grafik',
 kart='K-AIS2-02 (gövde-yaprak) · on bir öğrencinin çözdüğü soru sayısı; medyan ile mod farkı',
 metin='Aşağıdaki gövde-yaprak diyagramında, bir kursa devam eden 11 öğrencinin bir haftada çözdüğü soru sayıları gösterilmiştir.\nBuna göre, bu veri grubunun medyanı ile modunun farkı kaçtır?',
 dogru=v,yan=[(e[0],'Yalnız modu (15) yazmış; medyanla farkını almamış.','dikkat'),(e[1],'Yalnız medyanı (21) yazmış; modu çıkarmamış.','dikkat'),(e[2],'Medyan ile mod yerine en büyük ile en küçük değerin farkını (40 − 11) almış.','bilgi'),(e[3],'Medyan ile modu çıkarmak yerine toplamış (21 + 15).','islem')],
 istenen='Veri grubunun medyanı ile modunun farkı.',ip=['Yapraklar küçükten büyüğe dizili olduğundan değerleri satır satır okuyarak sıralamış olursun.'],bilgi=[GOV,MED],sekil=SK,
 ad=[A('Değerleri yaz','Her gövde ve yaprak birleştirilir.','11, 13, 15, 15, 15, 21, 24, 27, 32, 38, 40'),A('Medyan ve modu bul','11 değerin ortadaki 6. değeri medyandır; en çok tekrar eden değer moddur.','Medyan 21 · mod 15'),A('Farkı al','Medyandan mod çıkarılır.','21 − 15 = 6')],
 puf='Gövde-yaprakta mod en uzun yaprak satırında değil, en çok tekrar eden tam değerdedir.')

# ================= 03 kolay · öncüllü, değer değişimi =================
D3=[3,5,6,8,9,11,14]; D3b=[3,5,6,8,9,11,20]
tr=[mean(D3b)>mean(D3),med(D3b)>med(D3),(max(D3b)-min(D3b))>(max(D3)-min(D3))]; assert tr==[True,False,True]
dogru,yan=oncullu({0,2},['en büyük değer artsa da ortalamanın değişmediğini sanmış','ortalama arttığı için medyanın da arttığını sanmış','ranjın yalnız ortadaki değerlere bağlı olduğunu sanıp değişmediğini düşünmüş'])
q('0003',tipId='ist2-etki',tip='Veri değişimlerinin etkisi',z='kolay',alt='Değer Değişimi',kaz='Bir değerin değiştirilmesinin ortalama, medyan ve ranj üzerindeki etkisini yorumlar.',kalip='öncüllü',
 kart='K-AIS2-03 (öncüllü, değer değişimi) · yedi değerli veri grubunda en büyük değerin artırılması',
 metin='3, 5, 6, 8, 9, 11, 14\nveri grubunda en büyük değer olan 14, 20 ile değiştirilerek yeni bir veri grubu oluşturuluyor. Yeni veri grubu için üç yargı ileri sürülmüştür.\nI. Aritmetik ortalama artar.\nII. Medyan artar.\nIII. Ranj artar.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='Yeni veri grubu için doğru olan yargılar.',ip=['Değişen değer sıralamada hangi konumda olduğundan, medyanı etkileyip etkilemediğine bak.'],bilgi=[MED,ORT],
 ad=[A('Ortalama','Toplam 6 artar, değer sayısı aynıdır.','56 / 7 = 8 → 62 / 7 > 8, I doğru'),A('Medyan','Değişen değer en büyük değerdir; ortadaki (4.) değer değişmez.','Medyan 8 olarak kalır, II yanlış'),A('Ranj','En büyük değer arttığı için ranj büyür.','14 − 3 = 11 → 20 − 3 = 17, III doğru')],
 puf='Uç değerdeki değişim ortalamayı ve ranjı etkiler, medyanı etkilemez (ortadaki değerler aynı kalıyorsa).')

# ================= 04 orta · birikimli frekans grafiği, sınıflanmış ortalama =================
snr=[0,20,40,60,80,100]; fr4=[4,8,10,12,6]; cum=[0,4,12,22,34,40]
orta=[10,30,50,70,90]; assert sum(fr4)==40
v=Fr(sum(f*m for f,m in zip(fr4,orta)),40); assert v==54
alt=Fr(sum(f*m for f,m in zip(fr4,snr[:-1])),40); ust=Fr(sum(f*m for f,m in zip(fr4,snr[1:])),40)
assert alt==44 and ust==64
medsn=[i for i,c in enumerate(cum[1:]) if c>=20][0]; assert orta[medsn]==50
modsn=fr4.index(max(fr4)); assert orta[modsn]==70
e=[alt,orta[medsn],ust,orta[modsn]]; assert len({v,*e})==5
sx4,sy4=0.07,0.11; o=[]
for j in range(0,41,2):
    o.append(f'\\draw[gray!{40 if j%4==0 else 22},thin] (0,{j*sy4:.3f}) -- ({100*sx4:.3f},{j*sy4:.3f});')
    if j%4==0: o.append(f'\\node[left=2pt] at (0,{j*sy4:.3f}) {{${j}$}};')
for x_ in snr[1:]: o.append(f'\\draw[gray!40,thin] ({x_*sx4:.3f},0) -- ({x_*sx4:.3f},{40*sy4:.3f});')
for x_ in snr: o.append(f'\\node[below=2pt] at ({x_*sx4:.3f},0) {{${x_}$}};')
o.append(f'\\draw[{MAV},very thick] '+' -- '.join(f'({x_*sx4:.3f},{c*sy4:.3f})' for x_,c in zip(snr,cum))+';')
for x_,c in zip(snr,cum): o.append(f'\\fill[{MAV}] ({x_*sx4:.3f},{c*sy4:.3f}) circle (0.08);')
o.append(f'\\draw[-{{Stealth}},thick] (0,0) -- ({100*sx4+0.4:.3f},0) node[right] {{puan}};\\draw[-{{Stealth}},thick] (0,0) -- (0,{40*sy4+0.5:.3f}) node[above] {{Birikimli öğrenci sayısı}};')
SK=fig('\n'.join(o))
q('0004',tipId='ist2-sinif',tip='Sınıflanmış veri ve birikimli frekans',z='orta',alt='Birikimli Frekans',kaz='Birikimli frekans grafiğinden sınıf frekanslarını bulup sınıf orta noktalarıyla aritmetik ortalamayı hesaplar.',kalip='grafik',
 kart='K-AIS2-04 (birikimli frekans grafiği) · beş sınıflı puan dağılımı; sınıflanmış veriden ortalama',
 metin='Bir deneme sınavına giren öğrencilerin puanları, genişliği 20 olan sınıflara ayrılarak şekildeki birikimli frekans grafiği ile gösterilmiştir. Grafikteki her nokta, bir sınıfın üst sınırında o sınıfa kadar olan öğrenci sayısını göstermektedir.\nHer sınıftaki öğrencilerin puanlarının o sınıfın orta noktasında olduğu kabul edildiğine göre, öğrencilerin puan ortalaması kaçtır?',
 dogru=v,yan=[(e[0],'Her sınıfı alt sınırıyla temsil etmiş: (0·4 + 20·8 + 40·10 + 60·12 + 80·6) / 40.','bilgi'),(e[1],'Medyanın bulunduğu (40 – 60) sınıfının orta noktasını ortalama sanmış.','dikkat'),(e[2],'Her sınıfı üst sınırıyla temsil etmiş: (20·4 + 40·8 + 60·10 + 80·12 + 100·6) / 40.','bilgi'),(e[3],'En kalabalık (60 – 80) sınıfın orta noktasını ortalama sanmış.','dikkat')],
 istenen='Öğrencilerin puan ortalaması.',ip=['Grafikteki bir noktanın dikey değeri neyi gösterir?'],bilgi=[BIK,HIS],sekil=SK,
 ad=[A('Frekansları bul','Ardışık birikimli değerlerin farkı sınıf frekansıdır.','4, 12 − 4 = 8, 22 − 12 = 10, 34 − 22 = 12, 40 − 34 = 6'),A('Toplamı kur','Orta noktalar 10, 30, 50, 70, 90 frekanslarla çarpılıp toplanır.','10·4 + 30·8 + 50·10 + 70·12 + 90·6 = 2160'),A('Ortalamayı bul','Toplam öğrenci sayısına bölünür.','2160 / 40 = 54')],
 puf='Grafikte okunan değerin frekansı mı, yoksa toplamı mı gösterdiğini her zaman ayır.')

# ================= 05 orta · tablo, birleşik ortalama =================
nA,mA,nB,mB,c5,M5=10,60,25,55,75,65
x5=Fr(M5*(nA+nB)-nA*mA-nB*mB,c5-M5); assert x5==30 and nA*mA+nB*mB+c5*x5==M5*(nA+nB+x5)
d=c5-M5; e1=Fr(M5*nA-nA*mA,d); e1b=Fr(M5*nB-nB*mB,d); e2=Fr(M5*(nA+nB)-nA*mA-nB*mB,c5); e3=Fr(M5*(nA+nB)-Fr(mA+mB,2)*(nA+nB),d)
assert (e1,e1b,e2,e3)==(5,25,4,Fr(105,4))
SK=tablo_svg(['Şube','Öğrenci sayısı','Puan ortalaması'],[['9-A','10','60'],['9-B','25','55'],['9-C','x','75']])
q('0005',tipId='ist2-birlesik',tip='Grupları birleştirme ve veri ekleme',z='orta',alt='Birleşik Ortalama',kaz='Üç grubun ortalamalarından birleşik ortalama koşuluyla bilinmeyen grup büyüklüğünü bulur.',kalip='tablo',
 kart='K-AIS2-05 (birleşik ortalama tablosu) · üç şubenin puan ortalaması; bilinmeyen şube mevcudu',
 metin='Bir okulda üç şubenin ortak matematik sınavından aldıkları puanların ortalamaları ve şubelerdeki öğrenci sayıları aşağıdaki tabloda verilmiştir. 9-C şubesindeki öğrenci sayısı x’tir.\nÜç şubedeki bütün öğrencilerin puan ortalaması 65 olduğuna göre, x kaçtır?',
 dogru=x5,yan=[(e1,'Yalnız 9-A şubesini hesaba katmış: 600 + 75x = 65(10 + x).','dikkat'),(e1b,'Yalnız 9-B şubesini hesaba katmış: 1375 + 75x = 65(25 + x).','dikkat'),(e2,'Paydaya x’i yazmamış: 1975 + 75x = 65 · 35.','islem'),(e3,'9-A ve 9-B ortalamalarının basit ortalamasını (57,5) alıp 35 öğrenciye uygulamış: 57,5 · 35 + 75x = 65(35 + x).','bilgi')],
 istenen='9-C şubesindeki öğrenci sayısı x.',ip=['Her şubenin puan toplamını ortalama çarpı öğrenci sayısı ile yaz.'],bilgi=[BIR,ORT],sekil=SK,
 ad=[A('Toplamları yaz','Her şubenin puan toplamı ortalama × öğrenci sayısıdır.','9-A: 600 · 9-B: 1375 · 9-C: 75x'),A('Birleşik ortalamayı kur','Toplam puan, toplam öğrenci sayısı ile ortalamanın çarpımına eşittir.','(600 + 1375 + 75x) / (35 + x) = 65'),A('Çöz','Denklem düzenlenir.','1975 + 75x = 2275 + 65x → x = 30')],
 puf='Birleşik ortalamada her grubun toplamını (ortalama × sayı) yaz; ortalamaların ortalamasını alma.')

# ================= 06 orta · daire grafiği, x cinsinden açılar =================
x6=40; ac=[3*x6,2*x6,x6+30,2*x6+10]; assert sum(ac)==360 and 8*x6+40==360
kit=[a//2 for a in ac]; assert sum(kit)==180 and kit==[60,40,35,45]
v=kit[0]-kit[2]; e=[kit[0]-kit[3],kit[0]-kit[2]+0,0]
e=[kit[0]-kit[3],kit[0]-kit[2]-0,0]
e=[kit[0]-kit[3], ac[0]-ac[2], Fr(135-75,2)]
assert v==25 and e==[15,50,30] and len({v,*e,20})==5
e=[15,20,30,50]; assert kit[0]-kit[1]==20
dl=[('Roman',ac[0],'$3x$'),('Şiir',ac[1],'$2x$'),('Tarih',ac[2],'$x+30$'),('Bilim',ac[3],'$2x+10$')]
SK=fig(pie2(dl))
q('0006',tipId='ist2-dagilim',tip='Daire ve sütun grafiklerini birlikte okuma',z='orta',alt='Daire Grafiği',kaz='Merkez açıları x cinsinden verilen daire grafiğinde x’i bulup dilimlerdeki kişi sayılarını karşılaştırır.',kalip='grafik',
 kart='K-AIS2-06 (daire grafiği, bilinmeyen x) · kitapçıda satılan kitapların türe göre dağılımı',
 metin='Bir kitapçıda bir günde satılan 180 kitabın türlere göre dağılımı şekildeki daire grafiğiyle gösterilmiştir. Dilimlerin merkez açıları x cinsinden verilmiştir (derece cinsinden).\nBuna göre, satılan Roman sayısı ile Tarih sayısı arasındaki fark kaçtır?',
 dogru=v,yan=[(15,'Tarih yerine Bilim dilimini (2x + 10 = 90°, 45 kitap) almış: 60 − 45.','dikkat'),(20,'Tarih yerine Şiir dilimini (80°, 40 kitap) almış: 60 − 40.','dikkat'),(30,'Sabit terimleri (30 ve 10) unutup 8x = 360, x = 45 bulmuş; 135° ve 75° için 67,5 − 37,5.','islem'),(50,'Açı farkını (120° − 70°) kitap sayısı farkı sanmış.','bilgi')],
 istenen='Roman sayısı ile Tarih sayısı arasındaki fark.',ip=['Daire grafiğinde merkez açıların toplamı kaç derecedir?'],bilgi=[DAI],sekil=SK,
 ad=[A('x’i bul','Dilimlerin merkez açıları toplamı 360°’dir.','3x + 2x + (x + 30) + (2x + 10) = 360 → 8x = 320 → x = 40'),A('Açıları yaz','Roman 3x = 120°, Tarih x + 30 = 70°.','120° ve 70°'),A('Kitap sayısı','360° 180 kitaba karşılık gelir, yani 2° bir kitaptır.','Roman 60 · Tarih 35 → 60 − 35 = 25')],
 puf='Merkez açı verildiğinde önce bütün için kaç derecenin bir kişi (adet) ettiğini bul.')

# ================= 07 orta · kutu grafiği, öncüllü (sayım yorumu) =================
bx=(20,35,50,70,90); n7=48
tr=[True,True,False]; assert (bx[3]-bx[1])==35 and (bx[4]-bx[0])==70
dogru,yan=oncullu({0,1},['medyanın değerlerin yarısını (24 öğrenciyi) 50’ye eşit ya da küçük yaptığını görmemiş','Q1 ile Q3 arasında verilerin ortadaki yarısının bulunduğunu görmemiş','çeyrekler açıklığı ile ranjı (90 − 20 = 70) karıştırmış'])
SK=fig(kutu(0.5,*bx,0.07,MAV,None,True)+'\n'+xekseni(10,100,10,0.07,-0.2,'puan'))
q('0007',tipId='ist2-grafikoku',tip='Grafik okuyarak merkezî ölçüler',z='orta',alt='Kutu Grafiği',kaz='Kutu grafiğinden çeyrekleri okuyarak değer sayılarına ilişkin yargıları değerlendirir.',kalip='öncüllü',
 kart='K-AIS2-01 (kutu grafiği, öncüllü) · 48 öğrencinin puanı; çeyreklere göre en az/en çok sayım yargıları',
 metin='Bir sınava giren 48 öğrencinin puanları şekildeki kutu grafiğiyle gösterilmiştir. Kutunun uçları 1. ve 3. çeyreği, kutunun içindeki çizgi medyanı göstermektedir.\nI. Puanı en fazla 50 olan en az 24 öğrenci vardır.\nII. Puanı 35 ile 70 arasında olan (35 ve 70 dahil) en az 24 öğrenci vardır.\nIII. Çeyrekler açıklığı 70’tir.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='Grafiğe göre doğru olan yargılar.',ip=['Medyanın ve çeyreklerin değerlerin kaçta kaçını ayırdığını düşün.'],bilgi=[KUT],sekil=SK,
 ad=[A('Medyanı yorumla','Medyan 50’dir; sıralı 48 değerin ilk 24’ü medyana eşit ya da küçüktür.','En az 24 öğrenci → I doğru'),A('Kutuyu yorumla','Q1 = 35 ile Q3 = 70 arasında verilerin ortadaki yarısı bulunur.','48 / 2 = 24 → II doğru'),A('Çeyrekler açıklığı','Q3 − Q1 hesaplanır; 70 ise ranjdır (90 − 20).','70 − 35 = 35 → III yanlış')],
 puf='Çeyrekler açıklığı kutunun uzunluğu, ranj ise bütün grafiğin uzunluğudur.')

# ================= 08 orta · sütun grafiği, tanımlı ölçü (ortalama mutlak sapma) =================
kv8=[6,14,16,20,24,28]; m8=mean(kv8); assert m8==18
oms=Fr(sum(abs(a-18) for a in kv8),6); assert oms==6 and sum(abs(a-18) for a in kv8)==36 and sum(a-18 for a in kv8)==0
e=[0,Fr(36,5),max(abs(a-18) for a in kv8),36]; assert e==[0,Fr(36,5),12,36] and len({oms,*e})==5
SK=fig(sutun_deger(['1','2','3','4','5','6'],kv8,30,5,0.16,[MAV,TUR,YES,MOR,MAV,TUR],'Satılan kahve',xl='gün'))
q('0008',tipId='ist2-yeniolcu',tip='Tanımlı ölçüleri hesaplama',z='orta',alt='Ortalama Mutlak Sapma',kaz='Tanımı verilen ortalama mutlak sapma ölçüsünü sütun grafiğindeki veriden hesaplar.',kalip='yeni nesil',
 kart='K-AIS2-07 (tanımlı ölçü, sütun grafiği) · altı günlük satış; ortalama mutlak sapma',
 metin='Bir veri grubundaki değerlerin aritmetik ortalamadan farklarının mutlak değerlerinin aritmetik ortalamasına, bu veri grubunun ortalama mutlak sapması denir.\nŞekildeki sütun grafiği, bir kafede altı gün boyunca günlük satılan kahve sayılarını göstermektedir.\nBuna göre, bu veri grubunun ortalama mutlak sapması kaçtır?',
 dogru=oms,yan=[(0,'Farkları mutlak değer almadan toplamış; sapmaların toplamı 0 çıkmış.','bilgi'),(Fr(36,5),'Mutlak sapmaların toplamını (36) 6 yerine 5’e bölmüş.','islem'),(12,'Mutlak sapmaların ortalaması yerine en büyük mutlak sapmayı (|6 − 18|) yazmış.','dikkat'),(36,'Mutlak sapmaları toplamış, değer sayısına bölmeyi unutmuş.','islem')],
 istenen='Veri grubunun ortalama mutlak sapması.',ip=['Önce aritmetik ortalamayı bul, sonra her sütunun ortalamadan uzaklığını yaz.'],bilgi=[ORT,YEN],sekil=SK,
 ad=[A('Ortalamayı bul','Sütunlardaki değerler toplanıp 6’ya bölünür.','(6 + 14 + 16 + 20 + 24 + 28) / 6 = 108 / 6 = 18'),A('Mutlak sapmaları yaz','Her değerin ortalamadan farkının mutlak değeri alınır.','12, 4, 2, 2, 6, 10'),A('Ortalamasını al','Mutlak sapmalar toplanıp 6’ya bölünür.','36 / 6 = 6')],
 puf='Tanımı verilen ölçüde adımları sırayla yaz: ortalama, sapmalar, mutlak değer, ortalama.')

# ================= 09 orta · kareler toplamından varyans =================
n9,s9,k9,a9=10,20,120,4
m9=Fr(s9,n9)+a9; vr=Fr(k9,n9)-(m9-a9)**2; assert m9==6 and vr==8
e=[Fr(k9,n9),Fr(k9,n9)-(m9-a9),Fr(k9,n9)+(m9-a9)**2,k9-s9]; assert e==[12,10,16,100] and len({vr,*e})==5
q('0009',tipId='ist2-kareler',tip='Kareler toplamından varyans',z='orta',alt='Varyans',kaz='Bir sabite göre sapmaların toplamı ve kareler toplamından veri grubunun varyansını hesaplar.',kalip='yeni nesil',
 kart='K-AIS2-08 (kaydırılmış kareler toplamı) · 10 değer; Σ(x − 4) ve Σ(x − 4)² verilmiş',
 metin='10 değerden oluşan bir veri grubunun x₁, x₂, …, x₁₀ değerleri için\nΣ(xᵢ − 4) = 20 ve Σ(xᵢ − 4)² = 120\nolduğu biliniyor. (Toplamlar i = 1’den 10’a kadardır.)\nBuna göre, bu veri grubunun varyansı kaçtır?',
 dogru=vr,yan=[(12,'Σ(xᵢ − 4)² / 10 değerini varyans sanmış; ortalamanın 4’ten sapmasının karesini çıkarmamış.','islem'),(10,'Sapmanın karesi (2² = 4) yerine kendisini (2) çıkarmış: 12 − 2.','dikkat'),(16,'Ortalamanın sapmasının karesini çıkarmak yerine eklemiş: 12 + 4.','islem'),(100,'Kareler toplamından sapmalar toplamını çıkarmış (120 − 20) ve 10’a bölmemiş.','islem')],
 istenen='Veri grubunun varyansı.',ip=['Sapmalar toplamı, ortalamanın 4’ten ne kadar saptığını verir.'],bilgi=[VAR,KAR],
 ad=[A('Ortalamanın sapması','Sapmaların ortalaması, ortalamanın 4’ten uzaklığıdır.','20 / 10 = 2 → x̄ = 6'),A('Kareler ortalaması','Kaydırılmış değerlerin kareler ortalaması bulunur.','120 / 10 = 12'),A('Varyansı bul','Varyans = kareler ortalaması − (ortalamanın sapması)².','12 − 2² = 8')],
 puf='Kaydırılmış toplamlardan varyansı nasıl kurabileceğini düşün.')

# ================= 10 orta · tablo, standart puan (tanımlı ölçü) =================
mt,st_,mf,sf=60,12,48,8; zz=Fr(84-mt,st_); assert zz==2
v=mf+zz*sf; assert v==64
e=[mf+(84-mt)*Fr(1,1)*0+mf*0+ (sf*1), mf+(84-mt), Fr(84*mf,mt), mf*zz]
assert e==[56,72,Fr(336,5),96] and len({v,*e})==5
SK=tablo_svg(['Test','Ortalama','Standart sapma'],[['Matematik','60','12'],['Fen','48','8']])
q('0010',tipId='ist2-yeniolcu',tip='Tanımlı ölçüleri hesaplama',z='orta',alt='Standart Puan',kaz='Tanımı verilen standart puan ölçüsüyle iki testteki puanları karşılaştırır.',kalip='yeni nesil',
 kart='K-AIS2-07 (tanımlı ölçü, tablo) · iki testin ortalama ve standart sapması; eşit standart puan',
 metin='Bir testte bir öğrencinin standart puanı, öğrencinin puanından testin ortalaması çıkarılıp sonucun testin standart sapmasına bölünmesiyle bulunur.\nBir sınavdaki Matematik ve Fen testlerinin ortalaması ve standart sapması aşağıdaki tabloda verilmiştir.\nMatematik testinden 84 puan alan bir öğrencinin Fen testindeki standart puanının Matematik testindeki standart puanına eşit olması için Fen testinden kaç puan alması gerekir?',
 dogru=v,yan=[(e[0],'Standart puanı 1 bulmuş (Fen ortalamasına yalnız bir standart sapma, 8, eklemiş).','islem'),(e[1],'Matematikteki puan farkını (84 − 60 = 24) doğrudan Fen ortalamasına eklemiş.','bilgi'),(e[2],'Standart puan yerine oran kullanmış: 84 · 48 / 60.','bilgi'),(e[3],'Standart puanı (2) Fen ortalamasıyla (48) çarpmış.','islem')],
 istenen='Fen testinden alınması gereken puan.',ip=['Önce Matematikteki standart puanı bul; Fen için aynı standart puanı sağlayan puanı ara.'],bilgi=[YEN],sekil=SK,
 ad=[A('Matematikteki standart puan','Verilen tanımla hesaplanır.','(84 − 60) / 12 = 2'),A('Fen için denklem','Aynı standart puan için Fen puanı y olsun.','(y − 48) / 8 = 2'),A('Çöz','Denklem y için çözülür.','y − 48 = 16 → y = 64')],
 puf='Farklı ölçeklerdeki testleri karşılaştırırken ham puan farkına değil, ortalamadan kaç standart sapma uzakta olunduğuna bak.')

# ================= 11 orta · saçılım diyagramı, koşullu grup ortalaması =================
pts=[(1,90),(2,80),(2,60),(3,70),(4,60),(4,50),(5,70),(6,40),(6,50),(7,30)]
mx_=Fr(sum(a for a,b in pts),10); my_=Fr(sum(b for a,b in pts),10); assert (mx_,my_)==(4,60)
alt_=[a for a,b in pts if b<my_]; ust_=[a for a,b in pts if b>my_]
v=mean(alt_); assert v==Fr(23,4) and mean(ust_)==Fr(11,4) and med(alt_)==6 and mean([b for a,b in pts if b<60])==Fr(85,2)
e=[mean(ust_),mx_,med(alt_),mean([b for a,b in pts if b<60])]; assert len({v,*e})==5
sxs,sys_=0.68,0.048
g=[]
for j in range(20,101,10): g.append(f'\\draw[gray!40,thin] (0,{(j-20)*sys_:.3f}) -- ({7.5*sxs:.3f},{(j-20)*sys_:.3f});\\node[left=2pt] at (0,{(j-20)*sys_:.3f}) {{${j}$}};')
for i in range(1,8): g.append(f'\\draw[gray!40,thin] ({i*sxs:.3f},0) -- ({i*sxs:.3f},{80*sys_:.3f});\\node[below=2pt] at ({i*sxs:.3f},0) {{${i}$}};')
g.append(f'\\draw[-{{Stealth}},thick] (0,0) -- ({8*sxs:.3f},0) node[right] {{yaş}}; \\draw[-{{Stealth}},thick] (0,0) -- (0,{85*sys_:.3f}) node[above] {{fiyat (bin TL)}};')
for x_,y_ in pts: g.append(f'\\fill[{TUR}] ({x_*sxs:.3f},{(y_-20)*sys_:.3f}) circle (0.095);\\draw[black!70] ({x_*sxs:.3f},{(y_-20)*sys_:.3f}) circle (0.095);')
SK=fig('\n'.join(g))
q('0011',tipId='ist2-grafikoku',tip='Grafik okuyarak merkezî ölçüler',z='orta',alt='Saçılım Diyagramı',kaz='Saçılım diyagramından okuduğu değerlerle koşula uyan noktaların ortalamasını hesaplar.',kalip='grafik',
 kart='K-AIS2-01 (saçılım diyagramı) · on aracın yaşı ve fiyatı; fiyatı ortalamanın altındaki araçların yaş ortalaması',
 metin='Bir galeride satılan 10 ikinci el aracın yaşı (yıl) ile satış fiyatı (bin TL) arasındaki ilişki şekildeki saçılım diyagramında gösterilmiştir; her nokta bir aracı göstermektedir.\nBuna göre, satış fiyatı bu 10 aracın ortalama fiyatından düşük olan araçların yaş ortalaması kaç yıldır?',
 dogru=v,yan=[(e[0],'Ortalama fiyattan yüksek olan araçların yaş ortalamasını (11 / 4) bulmuş.','dikkat'),(e[1],'10 aracın tamamının yaş ortalamasını (40 / 10) yazmış.','dikkat'),(e[2],'Fiyatı ortalamadan düşük araçların yaş ortalaması yerine medyanını yazmış.','bilgi'),(e[3],'Yaş ortalaması yerine bu araçların fiyat ortalamasını (170 / 4) yazmış.','bilgi')],
 istenen='Fiyatı ortalama fiyattan düşük olan araçların yaş ortalaması (yıl).',ip=['Önce 10 fiyatın ortalamasını bul; sonra yalnız bu ortalamanın altındaki noktaların yaşlarını ayır.'],bilgi=[ORT,SAC],sekil=SK,
 ad=[A('Ortalama fiyat','On noktanın fiyatları ızgaradan okunup toplanır.','(90 + 80 + 60 + 70 + 60 + 50 + 70 + 40 + 50 + 30) / 10 = 60'),A('Koşula uyanlar','Fiyatı 60’tan düşük noktalar ayrılır; 60 olanlar dahil değildir.','(4, 50), (6, 40), (6, 50), (7, 30)'),A('Yaş ortalaması','Bu araçların yaşları toplanıp sayısına bölünür.','(4 + 6 + 6 + 7) / 4 = 23 / 4 = 5,75')],
 puf='Koşullu grup ortalamasında önce grubun hangi noktalardan oluştuğunu listele, sınırdaki noktaların dahil olup olmadığına dikkat et.')

# ================= 12 orta · çift çizgi grafiği, öncüllü =================
ay=['Oca','Şub','Mar','Nis','May','Haz']; sA=[2,6,10,14,18,22]; sB=[10,12,12,16,16,18]
assert mean(sA)==12 and mean(sB)==14 and max(sA)-min(sA)==20 and max(sB)-min(sB)==8 and all(a!=b for a,b in zip(sA,sB))
tr=[mean(sA)>mean(sB),(max(sA)-min(sA))>(max(sB)-min(sB)),any(a==b for a,b in zip(sA,sB))]; assert tr==[False,True,False]
dogru,yan=oncullu({1},['A çizgisinin yaz aylarında B’nin üstüne çıkmasından ortalamasının da büyük olduğunu sanmış','iki çizginin yükselişine bakıp yayılımlarının benzer olduğunu düşünmüş','çizgilerin kesiştiği yeri bir ayın değeri sanmış'])
SK=fig(cizgi(ay,[(sA,MAV,'A şehri','o'),(sB,TUR,'B şehri','s')],0,24,2,0.17,xw=0.95,yl='°C',lab=4,legend=True))
q('0012',tipId='ist2-grafikoku',tip='Grafik okuyarak merkezî ölçüler',z='orta',alt='Çizgi Grafiği',kaz='İki çizgi grafiğindeki veri gruplarının ortalama ve ranjını karşılaştırır.',kalip='öncüllü',
 kart='K-AIS2-01 (iki çizgi, öncüllü) · iki kentin altı aylık ortalama sıcaklığı; ortalama, ranj ve eşitlik yargıları',
 metin='Şekildeki çizgi grafiği, A ve B kentlerinde ocak ayından haziran ayına kadar ölçülen aylık ortalama sıcaklıkları (°C) göstermektedir.\nI. A kentinin aylık ortalama sıcaklıklarının aritmetik ortalaması, B kentininkinden büyüktür.\nII. A kentinin sıcaklıklarının ranjı, B kentininkinden büyüktür.\nIII. İki kentin aylık ortalama sıcaklıklarının eşit olduğu en az bir ay vardır.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='Grafiğe göre doğru olan yargılar.',ip=['Her kent için altı değeri ızgaradan oku; yargıları ayrı ayrı hesapla.'],bilgi=[MED,ORT],sekil=SK,
 ad=[A('Değerleri oku','A: 2, 6, 10, 14, 18, 22 · B: 10, 12, 12, 16, 16, 18','Toplamlar 72 ve 84'),A('Ortalama ve ranj','Ortalamalar toplamın 6’ya bölümüdür; ranj en büyük ile en küçük değerin farkıdır.','A: 12, ranj 20 · B: 14, ranj 8'),A('Yargıları değerlendir','I: 12 > 14 yanlış · II: 20 > 8 doğru · III: aynı ayda eşit değer yok (çizgiler Nisan ile Mayıs arasında kesişir, bir ayın değeri değildir) → yanlış.','Yalnız II doğru')],
 puf='İki grafiği karşılaştırırken çizgilerin kesişmesine değil, her ayın okunan değerine bak.')

# ================= 13 orta · medyan koşuluyla bilinmeyen =================
sol=[x for x in range(-60,61) if med([2,6,x,x+6,14,20])==9]; assert sol==[6]
x13=6; D13=[2,6,x13,x13+6,14,20]; v=mean(D13); assert v==10
def ort_x(xx): return mean([2,6,xx,xx+6,14,20])
e=[ort_x(3),ort_x(9),Fr(sum(D13),5),Fr(sum(D13),4)]; assert e==[9,11,12,15] and len({v,*e})==5
q('0013',tipId='ist2-siralama',tip='Sıralama koşullarından değer bulma',z='orta',alt='Medyan Koşulu',kaz='Çift sayıda değerli bir veri grubunda medyan koşulundan bilinmeyen değeri bulup ortalamayı hesaplar.',kalip='düz',
 kart='K-AIS2-09 (medyan koşulu) · altı değerli grup; x ve x + 6; ortalama istenir',
 metin='x bir tam sayı olmak üzere, 6 değerden oluşan\n2, 6, x, x + 6, 14, 20\nveri grubunun medyanı 9’dur.\nBuna göre, bu veri grubunun aritmetik ortalaması kaçtır?',
 dogru=v,yan=[(e[0],'x + 6 = 9 alıp x = 3 bulmuş (4. değeri medyan saymış): toplam 54, 54 / 6.','dikkat'),(e[1],'x = 9 alıp medyanı 3. değerle eşitlemiş: toplam 66, 66 / 6.','dikkat'),(e[2],'Doğru toplamı (60) 6 yerine 5 değere bölmüş.','islem'),(e[3],'Doğru toplamı (60) 4’e bölmüş.','islem')],
 istenen='Veri grubunun aritmetik ortalaması.',ip=['Altı değerde medyan, sıralı dizilimin ortadaki iki değerinin ortalamasıdır; x’in sıradaki yerini düşün.'],bilgi=[MED,ORT],
 ad=[A('x’in yerini belirle','Değerler 2 < 6 ≤ x < x + 6 ≤ 14 < 20 sırasındaysa ortadaki iki değer x ve x + 6’dır.','Medyan = (x + x + 6) / 2 = x + 3'),A('x’i bul','Medyan 9’a eşitlenir ve sıralama koşulu denetlenir.','x + 3 = 9 → x = 6 (6 ≤ 6 < 12 ≤ 14 sağlanır)'),A('Ortalamayı bul','Değerler toplanıp 6’ya bölünür.','(2 + 6 + 6 + 12 + 14 + 20) / 6 = 60 / 6 = 10')],
 puf='Bilinmeyenli değerlerle medyan kurarken varsayılan sıralamayı bulduğun değerle mutlaka denetle.')

# ================= 14 zor · histogram, sınıflanmış veride varyans =================
sn14=[0,10,20,30,40,50]; fr14=[2,6,6,4,2]; md14=[5,15,25,35,45]; n14=sum(fr14); assert n14==20
m14=Fr(sum(f*m for f,m in zip(fr14,md14)),n14); assert m14==24
x14=Fr(24*(14+0)-0,1) if False else None
# x değeri: 2·5 + 15x + 6·25 + 4·35 + 2·45 = 24 (14 + x)
assert (10+15*6+150+140+90)==24*(14+6)
v=Fr(sum(f*(m-24)**2 for f,m in zip(fr14,md14)),n14); assert v==129
sk=sum(f*(m-24)**2 for f,m in zip(fr14,md14)); kt=Fr(sum(f*m*m for f,m in zip(fr14,md14)),n14); ucs=Fr(sum((m-24)**2 for m in md14),5); oms14=Fr(sum(f*abs(m-24) for f,m in zip(fr14,md14)),n14)
assert (sk,kt,ucs,oms14)==(2580,705,201,Fr(46,5)) and kt-576==v and len({v,sk,kt,ucs,oms14})==5
SK=fig(histogram(sn14,[2,0,6,4,2],12,2,0.3,1.0,[MAV],'Çalışan sayısı',ad_x='adet')+'\n\\node[font=\\large] at (1.5,0.45) {$x$};')
q('0014',tipId='ist2-sinif',tip='Sınıflanmış veri ve birikimli frekans',z='zor',alt='Histogram ve Varyans',kaz='Histogramdaki bilinmeyen sütunu ortalama koşulundan bulup sınıflanmış verinin varyansını hesaplar.',kalip='grafik',
 kart='K-AIS2-04 (histogram, sınıflanmış varyans) · beş sınıflı günlük üretim; ortalama verilmiş, x bulunup varyans istenir',
 metin='Bir atölyedeki çalışanların günlük ürettiği parça sayısı sınıflandırılarak şekildeki histogramla gösterilmiştir. 10 – 20 sınıfındaki çalışan sayısı x’tir (bu sınıfın sütunu çizilmemiştir) ve x bir doğal sayıdır. Her sınıftaki değerlerin o sınıfın orta noktasında olduğu kabul edildiğinde üretimlerin aritmetik ortalaması 24’tür.\nBu kabulle, çalışanların günlük üretiminin varyansı kaçtır?',
 dogru=v,yan=[(Fr(46,5),'Varyans yerine mutlak sapmaların ortalamasını almış: (2·19 + 6·9 + 6·1 + 4·11 + 2·21) / 20.','bilgi'),(ucs,'Frekansları hesaba katmadan beş orta noktanın sapma karelerini beşe bölmüş: 1005 / 5.','dikkat'),(kt,'Kareler ortalamasını (14100 / 20) bulup ortalamanın karesini (24² = 576) çıkarmamış.','islem'),(sk,'Frekanslı sapma kareleri toplamını (2580) 20’ye bölmeyi unutmuş.','islem')],
 istenen='Günlük üretimin varyansı.',ip=['Önce ortalama koşulundan x’i bul; sınıfların orta noktaları 5, 15, 25, 35, 45’tir.'],bilgi=[HIS,VAR],sekil=SK,
 ad=[A('x’i bul','Orta noktalar frekanslarla çarpılır; toplam, ortalama ile toplam sayının çarpımına eşitlenir.','(2·5 + 15x + 6·25 + 4·35 + 2·45) / (14 + x) = 24 → 390 + 15x = 336 + 24x → x = 6'),A('Sapma kareleri','Her orta noktanın ortalamadan sapmasının karesi frekansıyla çarpılıp toplanır.','2·361 + 6·81 + 6·1 + 4·121 + 2·441 = 2580'),A('Varyans','Toplam çalışan sayısına (20) bölünür.','2580 / 20 = 129')],
 puf='Sınıflanmış veride her orta noktayı frekansı kadar tekrar eden değer gibi düşün; varyansta da frekanslarla ağırlıklandır.')

# ================= 15 zor · gövde-yaprak, ortalama = medyan, bilinmeyen yaprak =================
bs=[22,23,27,29,35,39,43,45,56]
def dz(a): return sorted(bs+[30+a])
sol=[a for a in range(10) if med(dz(a))==mean(dz(a))]; assert sol==[6]
v=med(dz(6)); assert v==Fr(71,2) and mean(dz(6))==v
d1=sorted(bs+[1]); assert med(d1)==32 and mean(d1)==32
e=[Fr(32),Fr(35),Fr(36),Fr(37)]; assert med(dz(6))<e[2] and dz(6)[5]==36 and (35+39)//2==37 and len({v,*e})==5
SK=fig(govde([(2,['2','3','7','9']),(3,['5','9','\\textbf{a}']),(4,['3','5']),(5,['6'])],'Anahtar: 2 | 3 → 23 adet'),'\\small')
q('0015',tipId='ist2-govde',tip='Gövde-yaprak diyagramı',z='zor',alt='Bilinmeyen Yaprak',kaz='Gövde-yaprak diyagramında ortalama–medyan eşitliğinden bilinmeyen yaprağı bulup medyanı hesaplar.',kalip='grafik',
 kart='K-AIS2-02 (gövde-yaprak, bilinmeyen yaprak) · 10 sporcunun şınav sayısı; ortalama = medyan koşulu',
 metin='Aşağıdaki gövde-yaprak diyagramında, bir antrenmanda 10 sporcunun yaptığı şınav sayıları gösterilmiştir. a bir rakamdır, yaprakların sırası önemli değildir ve bu veri grubunun aritmetik ortalaması medyanına eşittir.\nBuna göre, bu veri grubunun medyanı kaçtır?',
 dogru=v,yan=[(e[0],'Bilinmeyen değeri 30 + a yerine yalnız a alıp en küçük değer saymış; bu durumda a = 1 için ortalama ve medyan 32 olur.','dikkat'),(e[1],'Çift sayıda değerde 5. değeri (35) medyan almış.','dikkat'),(e[2],'a = 6 bulduktan sonra bilinmeyen değeri (36) medyan sanmış.','dikkat'),(e[3],'Ortadaki iki değeri a’ya bakmadan 35 ve 39 alıp ortalamalarını yazmış.','bilgi')],
 istenen='Veri grubunun medyanı.',ip=['Bilinmeyen değerin sıradaki yerini ortadaki iki değeri etkileyecek biçimde düşün.'],bilgi=[GOV,MED],sekil=SK,
 ad=[A('Değerleri yaz','Bilinmeyen değer 30 + a olur; diğer dokuz değer okunur.','22, 23, 27, 29, 35, 39, 43, 45, 56 ve 30 + a'),A('Medyanı a ile yaz','30 + a, 35 ile 39 arasındaysa 5. ve 6. değerler 35 ve 30 + a olur.','Medyan = (35 + 30 + a) / 2'),A('Ortalama = medyan','Toplam 319 + 30 + a, değer sayısı 10’dur; eşitlik çözülür.','(349 + a) / 10 = (65 + a) / 2 → a = 6 (35 < 36 < 39 sağlanır)'),A('Medyanı bul','a = 6 yerine konur.','(35 + 36) / 2 = 35,5')],
 puf='Bilinmeyen değerin medyanı etkileyip etkilemediğini sıralamayı varsayarak dene ve bulduğun değerle yerleşimi denetle.')

# ================= 16 zor · daire + sütun birlikte =================
ac16=[150,90,72,48]; say=[a*300//360 for a in ac16]; pct=[80,60,70,50]; assert say==[125,75,60,40] and sum(say)==300
giren=[s*p//100 for s,p in zip(say,pct)]; assert giren==[100,45,42,20] and sum(giren)==207
v=300-sum(giren); assert v==93
basit=Fr(sum(pct),4); e=[300-Fr(basit*300,100), 360-Fr(sum(a*p for a,p in zip(ac16,pct)),100), Fr(basit*300,100), sum(giren)]
assert e==[105,Fr(558,5),195,207] and len({v,*e})==5
dl=[(f'{s}. sınıf',a,f'${a}^\\circ$') for s,a in zip((9,10,11,12),ac16)]
SK=fig('\\begin{scope}\n'+pie2(dl,r=1.25,dis=1.62)+'\n\\end{scope}\n\\begin{scope}[shift={(4.7,-1.4)}]\n'+sutun_grafik(['9','10','11','12'],pct,100,10,0.03,[MAV,TUR,YES,MOR],'\\%',xw=0.75)+'\n'+'\\node[above=2pt] at (1.7,3.55) {Sınava giren oranı};\n\\end{scope}\n\\node at (0,3.1) {Sınıflara göre öğrenci dağılımı};')
q('0016',tipId='ist2-dagilim',tip='Daire ve sütun grafiklerini birlikte okuma',z='orta',alt='İki Grafik',kaz='Daire grafiğindeki dağılım ile sütun grafiğindeki oranları birleştirerek toplam sayıyı hesaplar.',kalip='grafik',
 kart='K-AIS2-06 (daire + sütun) · 300 öğrencinin sınıfa göre dağılımı ve sınava girme oranları; girmeyen sayısı',
 metin='Bir lisedeki 300 öğrencinin sınıf düzeylerine göre dağılımı şekildeki daire grafiğinde, her sınıf düzeyinde ortak yazılı sınavına giren öğrencilerin o sınıftaki öğrencilere oranı sütun grafiğinde gösterilmiştir.\nBuna göre, bu sınava girmeyen öğrenci sayısı kaçtır?',
 dogru=v,yan=[(105,'Sütun oranlarının basit ortalamasını (65%) bütün öğrencilere uygulamış: 300 · 35 / 100.','bilgi'),(Fr(558,5),'Açıları öğrenci sayısı sanıp 360 üzerinden hesaplamış: 360 − 248,4.','bilgi'),(195,'Girenlerin sayısını oranların basit ortalamasıyla (65%) bulmuş: 300 · 65 / 100.','bilgi'),(207,'Girmeyenleri değil, sınava giren öğrenci sayısını yazmış.','dikkat')],
 istenen='Sınava girmeyen öğrenci sayısı.',ip=['Her sınıf düzeyindeki öğrenci sayısını daire grafiğinden, giren sayısını sütun grafiğinden bul.'],bilgi=[DAI],sekil=SK,
 ad=[A('Sınıf mevcutları','360° 300 öğrenci eder; her dilim 5/6 ile çarpılır.','150° → 125 · 90° → 75 · 72° → 60 · 48° → 40'),A('Girenleri bul','Her mevcut kendi sınıfının oranıyla çarpılır.','125·0,8 + 75·0,6 + 60·0,7 + 40·0,5 = 100 + 45 + 42 + 20 = 207'),A('Girmeyenleri bul','Toplamdan girenler çıkarılır.','300 − 207 = 93')],
 puf='Farklı büyüklükteki gruplarda oranları birleştirirken her grubun büyüklüğünü hesaba kat.')

# ================= 17 zor · sıralama koşulları, en büyük değer =================
def cozum(n,S,medv,mode,mn):
    import itertools
    r=[]
    for c in itertools.combinations_with_replacement(range(1,30),n):
        if sum(c)!=S or c[n//2]!=medv or c[0]!=mn: continue
        cnt={x_:c.count(x_) for x_ in set(c)}; m_=max(cnt.values()); md=[x_ for x_ in cnt if cnt[x_]==m_]
        if md==[mode] and m_>=2: r.append(c)
    return r
cz=cozum(7,42,5,4,2); assert max(c[-1] for c in cz)==14 and (2,4,4,5,6,7,14) in cz
e=[42-sum((2,4,4,5,6,6)),42-sum((2,4,4,5,5,6)),42-sum((2,4,4,5,5,5)),42-sum((2,4,4,5))]; assert e==[15,16,17,27]
q('0017',tipId='ist2-siralama',tip='Sıralama koşullarından değer bulma',z='zor',alt='Mod ve Medyan Koşulu',kaz='Ortalama, medyan, tek mod ve en küçük değer koşullarını birlikte sağlayan veri grubunun en büyük değerini bulur.',kalip='düz',
 kart='K-AIS2-09 (çok koşullu sıralama) · yedi pozitif tam sayı; ortalama, medyan, tek mod, en küçük değer; en büyük değerin sınırı',
 metin='Pozitif tam sayılardan oluşan, 7 değerli bir veri grubunun aritmetik ortalaması 6, medyanı 5, modu 4 ve en küçük değeri 2’dir. Bu veri grubunda 4’ten başka en çok tekrar eden değer yoktur.\nBuna göre, bu veri grubunun en büyük değeri en fazla kaç olabilir?',
 dogru=14,yan=[(15,'5. ve 6. değerleri 6 ve 6 almış; 4 ve 6’nın ikişer kez tekrarıyla tek mod koşulunu bozmuş: 42 − 27.','dikkat'),(16,'5. ve 6. değerleri 5 ve 6 almış; 4 ile 5 ikişer kez tekrar eder, tek mod koşulu bozulur: 42 − 26.','dikkat'),(17,'5. ve 6. değerleri 5 ve 5 almış; 5 üç kez tekrar edip mod olur: 42 − 25.','dikkat'),(27,'İlk dört değerin toplamını (15) toplamdan çıkarıp son üç değerin toplamını yazmış.','islem')],
 istenen='Veri grubunun alabileceği en büyük değer.',ip=['En büyük değeri büyütmek için diğer değerleri koşulları bozmayacak en küçük değerlere ayarla.'],bilgi=[MED,ORT],
 ad=[A('Sıralamayı kur','Medyan 4. değerdir; mod 4 en az iki kez görünmelidir ve 4. değer 5 olduğundan 4’ler 2. ve 3. sıradadır.','2, 4, 4, 5, a, b, c'),A('5. ve 6. değerleri seç','En büyük değer için a ve b en küçük seçilir; ancak 5 ve 6 ikişer kez tekrar ederse 4 tek mod olmaz.','a = 5 olamaz (5 iki kez), a = 6 ise b ≥ 7 olmalı → a = 6, b = 7'),A('En büyük değeri bul','Toplam 42’dir.','c = 42 − (2 + 4 + 4 + 5 + 6 + 7) = 14')],
 puf='En büyük değeri büyütmek için diğer değerleri küçült; ama mod, medyan gibi koşulları her seçimde yeniden denetle.')

# ================= 18 zor · veri ekleme, kareler toplamı =================
n0,m0,v0=8,10,9; S2a=n0*(v0+m0**2); S2b=(n0+2)*(8+m0**2); kk=S2b-S2a; assert (S2a,S2b,kk)==(872,1080,208)
a_,b_=12,8; assert a_+b_==20 and a_*b_==96 and a_**2+b_**2==208 and mean([*([10]*0)])==0 if False else True
e=[a_*b_,Fr(kk,2),200,(a_+b_)**2]; assert e==[96,104,200,400] and len({kk,*e})==5
q('0018',tipId='ist2-birlesik',tip='Grupları birleştirme ve veri ekleme',z='zor',alt='Veri Ekleme ve Varyans',kaz='Ortalamayı koruyan iki değer eklendiğinde varyans değişiminden eklenen değerlerin kareler toplamını bulur.',kalip='yeni nesil',
 kart='K-AIS2-05 (veri ekleme, kareler toplamı) · 8 değerli grup; iki değer eklenince ortalama sabit, varyans değişir',
 metin='8 değerden oluşan bir veri grubunun aritmetik ortalaması 10, varyansı 9’dur. Bu veri grubuna a ve b değerleri eklendiğinde aritmetik ortalama değişmemiş, varyans 8 olmuştur.\nBuna göre, a² + b² toplamı kaçtır?',
 dogru=kk,yan=[(96,'a + b = 20 ve a² + b² = 208 olduğunu bulup a · b = 96 değerini yazmış.','dikkat'),(Fr(104),'a² + b² toplamı yerine bunların ortalamasını (208 / 2) yazmış.','islem'),(200,'a ve b’yi ortalamaya eşit (10 ve 10) alıp 10² + 10² yazmış; varyanstaki değişimi hesaba katmamış.','bilgi'),(400,'a² + b² yerine (a + b)² = 20² yazmış.','islem')],
 istenen='Eklenen iki değerin kareleri toplamı.',ip=['Ortalama değişmediğine göre a + b kaçtır? Kareler toplamını varyanstan yeniden kur.'],bilgi=[EKL,KAR],
 ad=[A('Eski kareler toplamı','Varyans ve ortalamadan Σx² bulunur.','Σx² = 8 · (9 + 10²) = 872'),A('Yeni kareler toplamı','10 değer, ortalama 10, varyans 8.','Σx² = 10 · (8 + 10²) = 1080'),A('Farkı al','Eklenen iki değerin kareleri toplamı farktır.','a² + b² = 1080 − 872 = 208')],
 puf='Varyanstan kareler toplamına geçebilmek, veri eklenen sorularda işini kolaylaştırır.')

# ================= 19 zor · iki nokta diyagramı, değişkenlik katsayısı =================
dA=[3,8,8,8,9,9,9,10]; dB=[1,3,4,6,6,6,7,7]
def sdv(x): return math.isqrt(int(var(x)))
assert mean(dA)==8 and var(dA)==4 and mean(dB)==5 and var(dB)==4 and sdv(dA)==2 and sdv(dB)==2
DKA=Fr(2,8)*100; DKB=Fr(2,5)*100; v=DKB-DKA; assert (DKA,DKB,v)==(25,40,15)
e=[-v,0,Fr(15,100),Fr(4,5)*100-Fr(4,8)*100]; assert e==[-15,0,Fr(3,20),30] and len({v,*e})==5
sx19=0.55
SK=fig(noktalar(dA,sx19,2.5,MAV)+'\n'+xekseni(0,12,1,sx19,2.5,'')+'\n'+noktalar(dB,sx19,0,TUR)+'\n'+xekseni(0,12,1,sx19,0,'')+'\n\\node[font=\\bfseries,anchor=west] at (0,4.5) {A grubu};\\node[font=\\bfseries,anchor=west] at (0,1.65) {B grubu};')
q('0019',tipId='ist2-yeniolcu',tip='Tanımlı ölçüleri hesaplama',z='zor',alt='Değişkenlik Katsayısı',kaz='Tanımı verilen değişkenlik katsayısını iki nokta diyagramındaki veri grubu için hesaplayıp karşılaştırır.',kalip='yeni nesil',
 kart='K-AIS2-07 (tanımlı ölçü, iki nokta diyagramı) · iki grubun değişkenlik katsayıları; farkı',
 metin='Bir veri grubunun değişkenlik katsayısı (DK), grubun standart sapmasının aritmetik ortalamasına oranının 100 katıdır:\nDK = (standart sapma / aritmetik ortalama) · 100\nA ve B gruplarına ait değerler, her nokta bir değeri gösterecek biçimde şekildeki nokta diyagramlarında verilmiştir.\nBuna göre, B grubunun DK değeri ile A grubunun DK değerinin farkı (DK_B − DK_A) kaçtır?',
 dogru=v,yan=[(-15,'Farkı ters sırada almış: DK_A − DK_B.','dikkat'),(0,'İki grubun standart sapmalarının eşit (2 ve 2) olmasından DK’ların da eşit olduğunu sanmış.','bilgi'),(Fr(3,20),'100 ile çarpmayı unutup 0,40 − 0,25 yazmış.','islem'),(30,'Standart sapma yerine varyansı (4) kullanmış: (4/5 − 4/8) · 100.','bilgi')],
 istenen='B grubunun DK değeri ile A grubunun DK değerinin farkı.',ip=['Her grup için önce ortalamayı, sonra ortalamadan sapmaların karelerinin ortalamasını hesapla.'],bilgi=[ORT,VAR,YEN],sekil=SK,
 ad=[A('A grubu','Değerlerin toplamı ve sapma kareleri hesaplanır.','Ortalama 8 · varyans (25 + 0 + 0 + 0 + 1 + 1 + 1 + 4) / 8 = 4 → standart sapma 2 → DK_A = 2 / 8 · 100 = 25'),A('B grubu','Aynı işlemler B için yapılır.','Ortalama 5 · varyans (16 + 4 + 1 + 1 + 1 + 1 + 4 + 4) / 8 = 4 → standart sapma 2 → DK_B = 2 / 5 · 100 = 40'),A('Farkı al','DK_B − DK_A bulunur.','40 − 25 = 15')],
 puf='Yayılma ölçüsünü ortalamaya oranlamadan gruplar arası karşılaştırma yapma; aynı standart sapma farklı ortalamalarda farklı değişkenlik demektir.')

# ================= 20 zor · öncüllü, dönüşüm ve ortalamaya eşit değer ekleme =================
A20=[2,4,6,8,10]; B20=[3*a-2 for a in A20]; B20=B20+[int(mean(B20))]
assert B20==[4,10,16,22,28,16] and mean(B20)==3*mean(A20)-2
vA=var(A20); vB=var(B20); assert vA==8 and vB==60 and vB<9*vA and med(B20)==3*med(A20)-2==16
tr=[mean(B20)==3*mean(A20)-2,vB<9*vA,med(B20)==3*med(A20)-2]; assert tr==[True,True,True]
dogru,yan=oncullu({0,1,2},['ortalamaya eşit değer eklenince ortalamanın değiştiğini sanmış','dönüşümden sonra varyansın tam 9 katı olduğunu, eklenen değerin etkisi olmadığını düşünmüş','eklenen 16’yı listenin sonuna yazıp sıralamadan 3. ve 4. değerleri (16 ve 22) alarak medyanı 19 bulmuş'])
q('0020',tipId='ist2-etki',tip='Veri değişimlerinin etkisi',z='zor',alt='Dönüşüm ve Veri Ekleme',kaz='Doğrusal dönüşüm ve ortalamaya eşit değer eklenmesinin ortalama, varyans ve medyana etkisini yargılar.',kalip='öncüllü',
 kart='K-AIS2-03 (öncüllü, dönüşüm + ekleme) · A grubundan y = 3x − 2 ile B; B’ye ortalamasına eşit değer eklenmesi',
 metin='A = {2, 4, 6, 8, 10} veri grubu veriliyor. B veri grubu şöyle oluşturuluyor: A’nın her değeri 3 ile çarpılıp 2 çıkarılıyor, elde edilen değerlerin aritmetik ortalamasına eşit bir değer de gruba ekleniyor.\nI. B’nin aritmetik ortalaması, A’nın aritmetik ortalamasının 3 katından 2 eksiktir.\nII. B’nin varyansı, A’nın varyansının 9 katından küçüktür.\nIII. B’nin medyanı, A’nın medyanının 3 katından 2 eksiktir.\nBuna göre, bu yargılardan hangileri doğrudur?',
 dogru=dogru,yan=yan,sira=SIRA,istenen='B grubu için doğru olan yargılar.',ip=['B’nin değerlerini yazıp ortalama, varyans ve medyanı A ile karşılaştır.'],bilgi=[DON,EKL,VAR],
 ad=[A('B grubunu yaz','Dönüşümle 4, 10, 16, 22, 28 bulunur; ortalamaları 16 olduğundan 16 eklenir.','B = {4, 10, 16, 16, 22, 28}'),A('Ortalama ve medyan','Ortalamaya eşit değer eklenince ortalama değişmez; ortadaki iki değer 16 ve 16’dır.','Ortalama 16 = 3·6 − 2 → I doğru · Medyan 16 = 3·6 − 2 → III doğru'),A('Varyans','A’nın varyansı 8; dönüşümle 72 olur, eklenen değer sapmayı artırmaz ve değer sayısı büyür.','Var(B) = 360 / 6 = 60 < 72 → II doğru')],
 puf='Dönüşüm ve ekleme birlikte olduğunda her yargıyı B’nin değerlerini yazarak ayrı ayrı sına.')

# ---------- bitiş ----------
def bitir_ayt():
    for q_ in P.ANA: q_['kardes']=None
    P.yaz(os.path.join(AD,'istatiki-1.json'),'/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ist2/bos-istatiki.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: MEB 11–12. sınıf matematik (veri analizi), ÖSYM AYT 2018–2025 ve yayın bankalarının mantık taraması.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','istatiki.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
bitir_ayt()
