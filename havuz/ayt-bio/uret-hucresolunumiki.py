"""AYT Biyoloji · Hücresel Solunum · 2. dalga · 10 soru. Şekiller TikZ/tablo; sayısal değerler modelden hesaplanıp assert edilir."""
import sys,os,math,json
BD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(BD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
from fractions import Fraction as Fr
from collections import Counter
KONU_AD='Hücresel Solunum'; KK='abio|Hücresel Solunum'
P=Parti('hucresolunumiki',KONU_AD,KK,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KY='ÖSYM 2018–2026 AYT Biyoloji dağılımı · MEB 12. sınıf biyoloji'
TIPAD={'hs-yer':'Hücresel solunumun gerçekleştiği yerler','hs-basamak':'Solunum basamakları ve ürünleri','hs-ets':'Elektron taşıma sistemi ve kemiozmoz','hs-ferm':'Fermantasyon','hs-atp':'ATP ve taşıyıcı hesapları','hs-deney':'Solunum deney düzenekleri','hs-grafik':'Solunum grafikleri','hs-karsilastir':'Solunum türlerinin karşılaştırılması'}
def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId):
    tip=TIPAD[tipId]; kart(f'K-ABHS2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY); return f'K-ABHS2-{no:02d}'

# ===================== MODEL =====================
GL=dict(harcanan=2,uretilen=4,net=2,NADH=2)              # 1 glikoz, glikoliz
PO=dict(NADH=2,CO2=2)                                      # piruvat -> asetil CoA (1 glikoz)
KG=dict(NADH=6,FADH2=2,ATP=2,CO2=4)                        # Krebs (1 glikoz = 2 tur)
ETS_N,ETS_F=3,2                                            # soruda verilen katsayilar
assert GL['uretilen']-GL['harcanan']==GL['net']
ETS_G=(GL['NADH']+PO['NADH']+KG['NADH'])*ETS_N+KG['FADH2']*ETS_F    # 1 glikozdan ETS ATP
NET_G=GL['net']+KG['ATP']+ETS_G                                       # 1 glikozdan net ATP
assert (ETS_G,NET_G)==(34,38) and PO['CO2']+KG['CO2']==6
FERM_ATP=2
ONC7=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def etiket(s,rom):
    s=sorted(s,key=rom.index)
    if len(s)==1: return 'Yalnız '+s[0]
    if len(s)==len(rom): return ', '.join(s[:-1])+' ve '+s[-1]
    return ' ve '.join(s)
def kume_of(lbl):
    if lbl.startswith('Yalnız '): return {lbl[7:]}
    return {x for x in lbl.replace(' ve ',', ').split(', ')}
def onc_sec(T,harf,rom=('I','II','III')):
    d=etiket(T,list(rom)); p=ONC7.index(d); i='ABCDE'.index(harf)
    assert p-i>=0 and len(ONC7[p+1:p+5-i])==4-i,(d,harf)
    return d,ONC7[p-i:p]+[d]+ONC7[p+1:p+5-i]
def onc_cel(T,sira,d,n,rom=('I','II','III'),olumsuz=False):
    U=set(rom); yan=[]
    for o in sira:
        if o==d: continue
        S=kume_of(o); ex=sorted(S-T,key=rom.index); ms=sorted(T-S,key=rom.index); pr=[]
        if olumsuz:
            for e in ex: pr.append(f'{e} öncülü kökteki koşulu sağlamadığı hâlde seçilmiş: {n[e]}')
            for e in ms: pr.append(f'{e} öncülü kökteki koşulu sağladığı hâlde dışarıda bırakılmış: {n[e]}')
        else:
            for e in ex: pr.append(f'{e} öncülü kökteki koşulu sağlamadığı hâlde seçilmiş: {n[e]}')
            for e in ms: pr.append(f'{e} öncülü kökteki koşulu sağladığı hâlde dışarıda bırakılmış: {n[e]}')
        tur='dikkat' if (olumsuz and S==U-T) else 'bilgi'
        txt=' '.join(x if x.endswith('.') else x+'.' for x in pr)
        if tur=='dikkat': txt='Kökteki olumsuzluğu gözden kaçırıp tersini seçmek. '+txt
        yan.append((o,txt,tur))
    return yan
def onc_adim(T,n,rom=('I','II','III')):
    return [A(f'{e}. öncülü değerlendir',n[e],f'{e}: '+('koşulu sağlar' if e in T else 'koşulu sağlamaz')) for e in rom]
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)); return sira
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKS='-{Stealth[length=2.2mm,width=1.8mm]}'
def q(no,ad,**k):
    k['tip']=TIPAD[k['tipId']]; mk(P,no,ad=ad,adim=len(ad),**k)
def sayisal(dogru,diger):
    vals=[dogru]+[v for v,_,_ in diger]; assert len(set(vals))==5
    return sorted(vals)
SIRA={}

# ===================== Q1 · hücre ve mitokondri şeması · kolay =====================
k1=kartla(1,'Glikoliz ve kemiozmozun yerleri','Hücresel solunumun basamakları sitoplazmada ya da mitokondrinin farklı bölümlerinde yürür; bir basamağın hangi bölgede olduğu o bölgedeki enzimlere ve zar yapılarına bağlıdır.','Kemiozmotik ATP sentezini matriksle ya da glikolizi mitokondriyle ilişkilendirmek; sorulan iki yerin sırasını karıştırmak.','kolay','şekilli',3,'hs-yer')
a_,b_=2.55,1.35
def yt(x): return b_*math.sqrt(1-(x/a_)**2)
def mito_yol():
    top=[-1.55,0.3,1.7]; bot=[-0.9,0.9]; hw=.14
    def seg(x0,x1,n=3): return [(x0+(x1-x0)*i/n,yt(x0+(x1-x0)*i/n)) for i in range(n+1)]
    cur=-2.5; path=[(-a_,0.0),(-2.5,yt(-2.5))]
    for f in top:
        for p in seg(cur,f-hw,3)[1:]: path.append(p)
        path+=[(f-hw,-.2),(f+hw,-.2),(f+hw,yt(f+hw))]; cur=f+hw
    for p in seg(cur,2.5,3)[1:]: path.append(p)
    path.append((a_,0.0)); path.append((2.5,-yt(2.5))); cur=2.5
    for f in sorted(bot,reverse=True):
        for p in seg(cur,f+hw,3)[1:]: path.append((p[0],-p[1]))
        path+=[(f+hw,.2),(f-hw,.2),(f-hw,-yt(f-hw))]; cur=f-hw
    for p in seg(cur,-2.5,3)[1:]: path.append((p[0],-p[1]))
    return path
MP=mito_yol()
def lab(t,tx,ty,ex,ey):
    return f'\\node[font=\\normalsize\\bfseries] at ({tx},{ty}) {{{t}}};\\draw[{OKS},line width=.8pt] ({tx+(ex-tx)*.14:.3f},{ty+(ey-ty)*.14:.3f})--({ex},{ey});'
def hucre_svg(n):
    b=['\\draw[line width=1.6pt,fill=vurgu,fill opacity=.07] (0,0) ellipse (5.3 and 3.3);',
       '\\draw[line width=1.6pt,fill=orange,fill opacity=.12] (0,0) ellipse (3 and 1.75);',
       '\\draw[line width=1.6pt,rounded corners=2.5pt,fill=orange,fill opacity=.18] '+' -- '.join('(%.3f,%.3f)'%p for p in MP)+' -- cycle;',
       '\\draw[line width=1pt] (-.3,-.62) circle (.2);']
    for (x,y) in [(-3.9,.8),(-3.6,-.2),(-3.2,.55),(-4.3,-.5),(3.8,-.9),(4.2,.2),(3.5,-1.8),(-3.3,-1.8)]: b.append(f'\\fill[blue!55!black] ({x},{y}) circle (.07);')
    th=math.radians(35); b.append(lab(n['arasi'],3.3,2.2,2.775*math.cos(th),1.55*math.sin(th)))
    th=math.radians(205); b.append(lab(n['ic'],-3.9,-2.1,2.55*math.cos(th),1.35*math.sin(th)))
    b.append(lab(n['matriks'],1.0,2.45,1.0,.55))
    b.append(lab(n['sit'],-4.5,1.9,-3.5,1.05))
    return tk('\n'.join(b),.8)
N1=dict(sit='I',arasi='II',ic='III',matriks='IV')
SK1=hucre_svg(N1)
D1='I ve III'; S1=['I ve III','I ve IV','III ve I','IV ve III','II ve III']
assert len(set(S1))==5
q('0001',tipId='hs-yer',z='kolay',alt='Solunumun gerçekleştiği yerler',kaz='Hücre ve mitokondri şemasında glikoliz ile kemiozmotik ATP sentezinin yerlerini belirler.',kalip='şekilli',
 kart=f'{k1} · hücre ve mitokondri şeması',
 metin='Şekilde ökaryot bir hücre ve içindeki mitokondri şematik olarak gösterilmiş; bazı bölgeler I, II, III ve IV ile numaralandırılmıştır. Glikozun yıkımının ilk basamağı ile elektron taşıma sistemine bağlı ATP sentezi hücrenin farklı bölgelerinde gerçekleşir.\nBuna göre, glikoliz ve kemiozmozla ATP sentezi sırasıyla numaralandırılmış bölgelerin hangilerinde gerçekleşir?',
 dogru=D1,sira=S1,
 yan=[('I ve IV','Kemiozmotik ATP sentezini matriksle ilişkilendirmek; ATP sentaz matrikste değil, iç zarda bulunur.','bilgi'),
      ('III ve I','Bölgeleri doğru bulup sırayı ters yazmak; glikoliz I numaralı, kemiozmozla ATP sentezi III numaralı bölgededir.','dikkat'),
      ('IV ve III','Glikolizi matriksle ilişkilendirmek; glikoliz mitokondride değil, sitoplazmada yürür.','bilgi'),
      ('II ve III','Glikolizi zarlar arası boşlukla ilişkilendirmek; bu boşlukta glikoliz tepkimeleri gerçekleşmez, yalnız H⁺ birikir.','bilgi')],
 istenen='Glikoliz ve kemiozmozla ATP sentezinin gerçekleştiği bölgelerin numaraları.',
 ip=['Mitokondrinin dışında kalan hücre bölgesini ve mitokondrinin zarla ayrılmış bölümlerini biçimlerinden tanı; her basamağın enzimlerinin çözünmüş mü yoksa zara gömülü mü olduğunu düşün.'],
 bilgi=[B('Hücresel solunumun yerleri','glikozun yıkımının ilk basamağı mitokondri dışında yürür · Mitokondri çift zarlıdır; iç zarın çevrelediği sıvı bölge matriks, iki zar arasındaki aralık zarlar arası boşluktur')],
 ad=[A('Bölgeleri tanı','Mitokondrinin dışındaki hücre sıvısı sitoplazmadır; iç zar kıvrımlı zardır; matriks iç zarın çevrelediği sıvıdır; iki zar arası boşluktur.','I: sitoplazma · II: zarlar arası boşluk · III: iç zar · IV: matriks'),
     A('Glikolizin yerini bul','Glikoliz enzimleri sitoplazmada çözünmüş hâldedir.','Glikoliz → I'),
     A('ATP sentezinin yerini bul','ATP sentaz enzimi iç zara gömülüdür; H⁺ akışı bu zarda gerçekleşir.','Kemiozmoz → III'),
     A('Sırayla yaz','Önce glikolizin, sonra kemiozmozun yeri yazılır.','I ve III')],
 puf='Basamağın enzimleri çözünmüş mü yoksa zara bağlı mı, buna göre bölgeyi seç.',sekil=SK1)
SIRA[1]=1

# ===================== Q2 · glikoliz şeması · kolay =====================
k2=kartla(2,'Glikolizde net ATP hesabı','Glikolizde bir glikoz için ATP hem harcanır hem üretilir; net kazanç üretilenden harcananın çıkarılmasıyla bulunur ve glikoz sayısıyla çarpılır.','Üretilen ATP’yi net sanmak; glikoz sayısıyla çarpmayı unutmak.','kolay','şekilli',3,'hs-atp')
ng=6; net2=ng*GL['net']; assert net2==12
SK2=tk(r'''\draw[line width=1.4pt,rounded corners=4pt,fill=vurgu,fill opacity=.12] (0,0) rectangle (4.2,.9); \node at (2.1,.45) {Glikoz (6 karbonlu)};
\draw[line width=1.4pt,rounded corners=4pt,fill=orange,fill opacity=.15] (0,-2.4) rectangle (4.2,-1.5); \node at (2.1,-1.95) {2 üç karbonlu madde};
\draw[line width=1.4pt,rounded corners=4pt,fill=blue,fill opacity=.10] (0,-4.8) rectangle (4.2,-3.9); \node at (2.1,-4.35) {2 pirüvik asit};
\draw[-{Stealth[length=2.4mm,width=2mm]},line width=1.4pt] (2.1,-.05)--(2.1,-1.45);
\draw[-{Stealth[length=2.4mm,width=2mm]},line width=1.4pt] (2.1,-2.45)--(2.1,-3.85);
\node[font=\normalsize\bfseries] at (1.5,-.75) {1};\node[font=\normalsize\bfseries] at (1.5,-3.15) {2};
\node[font=\normalsize,anchor=west] at (2.45,-.75) {2 ATP $\rightarrow$ 2 ADP};
\node[font=\normalsize,anchor=west,align=left] at (2.45,-3.15) {4 ADP $\rightarrow$ 4 ATP\\ 2 NAD$^+$ $\rightarrow$ 2 NADH};''',.85)
y2=[(GL['net'],'Tek glikozun net kazancını bulup glikoz sayısıyla çarpmayı unutmak.','islem'),
    (GL['uretilen'],'Tek glikozda üretilen ATP’yi net kazanç saymak ve glikoz sayısıyla çarpmamak.','islem'),
    (ng*GL['uretilen'],'Harcanan ATP’leri çıkarmayıp yalnız üretilen ATP’leri saymak.','islem'),
    (ng*(GL['uretilen']+GL['harcanan']),'Harcanan ve üretilen ATP’leri çıkarmak yerine toplamak.','islem')]
assert sayisal(net2,y2)==[2,4,12,24,36]
q('0002',tipId='hs-atp',z='kolay',alt='ATP hesapları',kaz='Glikoliz şemasından net ATP kazancını glikoz sayısıyla hesaplar.',kalip='şekilli',
 kart=f'{k2} · glikoliz şeması, 6 glikoz',
 metin='Şekilde bir glikozun glikolizde yıkılma basamakları şematik olarak gösterilmiştir. Oklar üzerinde bu basamaklarda harcanan ve oluşan maddeler yazılmıştır.\nBuna göre, 6 glikozun tamamı bu basamaklardan geçtiğinde hücrede net kaç ATP kazanılır?',
 dogru=net2,yan=y2,
 istenen='6 glikozun glikolizinde net ATP kazancı.',
 ip=['Şemada ATP’nin hangi okta harcandığını, hangi okta oluştuğunu bul; bir glikoz için net farkı yazdıktan sonra glikoz sayısına bak.'],
 bilgi=[B('Net ATP kazancı','bir basamaktaki net kazanç, oluşan ATP sayısından harcanan ATP sayısının çıkarılmasıyla bulunur · Hücredeki toplam kazanç, her glikozun net kazancının glikoz sayısıyla çarpımıdır')],
 ad=[A('Harcananı oku','Birinci okta ATP ADP’ye dönüşür, yani ATP harcanır.','1 glikoz: 2 ATP harcanır'),
     A('Oluşanı oku','İkinci okta ADP ATP’ye dönüşür, yani ATP oluşur.','1 glikoz: 4 ATP oluşur'),
     A('Bir glikozun neti','Oluşandan harcanan çıkarılır.','4 − 2 = 2 ATP'),
     A('Glikoz sayısıyla çarp','Her glikoz aynı basamaklardan geçer.','6 × 2 = 12 ATP')],
 puf='Önce tek glikoz için oluşan ve harcanan ATP’yi oku, sonra net farkı glikoz sayısıyla çarp.',sekil=SK2)
SIRA[2]=2

# ===================== Q3 · ETS inhibitörü tablosu · orta · öncüllü =====================
k3=kartla(3,'ETS’nin durmasının sonuçları','Elektron taşıma sistemi durduğunda taşıyıcıların yükseltgenmesi, H⁺ pompalanması ve ATP sentezi birbirine bağlı biçimde etkilenir.','NADH’ın ETS dışında da yükseltgenebileceğini düşünmek; H⁺ akışı ile ATP sentezi arasındaki bağı gözden kaçırmak.','orta','öncüllü',3,'hs-ets')
SK3=tablo_svg(['Ölçülen (birim)','Eklemeden önce','Eklemeden sonra'],[['Matriks NADH derişimi','20','55'],['Zarlar arası H⁺ derişimi','60','25'],['O₂ tüketim hızı','12','0']])
T3={'I','III'}
N3={'I':'Matriksteki NADH derişimi arttığına göre NADH’ın NAD⁺’ya yükseltgenmesi yavaşlamıştır; ETS elektronları O₂’ye aktaramaz hâle gelmiştir.',
    'II':'Zarlar arası boşlukta H⁺ derişimi azaldığına göre H⁺ pompalanması azalmıştır; bu durumda ATP sentaz aracılığıyla matrikse geçen H⁺ miktarı artmaz, azalır.',
    'III':'Zarlar arası boşlukta H⁺ birikimi azaldığından kemiozmotik ATP sentezi için gereken H⁺ gradyanı zayıflamış, ATP sentez hızı düşmüştür.'}
d3,s3=onc_sec(T3,'D')
q('0003',tipId='hs-ets',z='orta',alt='ETS ve kemiozmoz',kaz='ETS’nin durmasıyla taşıyıcı, H⁺ ve ATP sentezindeki değişimleri tablodan yorumlar.',kalip='öncüllü',
 kart=f'{k3} · ETS’yi durduran madde tablosu',
 metin='Pirüvik asit ve ADP bulunan, O₂’li ortamdaki bütün mitokondri süspansiyonuna, elektronların son elektron alıcısına aktarılmasını engelleyen bir madde eklenmiştir. Maddenin eklenmesinden önce ve sonra yapılan ölçümler tabloda verilmiştir.\nI. NADH’ın yükseltgenme hızı azalmıştır.\nII. ATP sentaz aracılığıyla matrikse geçen H⁺ miktarı artmıştır.\nIII. Kemiozmozla ATP sentez hızı azalmıştır.\nBuna göre, yukarıdaki öncüllerden hangileri söylenebilir?',
 dogru=d3,sira=s3,yan=onc_cel(T3,s3,d3,N3),
 istenen='Tablodan çıkarılabilecek yargılar.',
 ip=['Her ölçümün madde eklendikten sonra hangi yönde değiştiğini oku; sonra NADH, H⁺ ve ATP sentezi arasındaki bağı kurarak öncülleri tek tek sına.'],
 bilgi=[B('ETS ve H⁺ gradyanı','ETS’de elektronlar taşıyıcılardan geçerken H⁺ zarlar arası boşluğa pompalanır · Oluşan H⁺ gradyanı ATP sentaz aracılığıyla ATP sentezinde kullanılır')],
 ad=onc_adim(T3,N3)+[A('Sonuç','Tablodan çıkarılabilecek yargılar I ve III’tür.','Doğru: I ve III')],
 puf='Her ölçümün değişim yönünü yazıp öncülleri bu değişimlerle eşleştir.',sekil=SK3)
SIRA[3]=3

# ===================== Q4 · laktat dehidrojenaz inhibisyonu · orta · düz · olumsuz =====================
k4=kartla(4,'Fermantasyonda NAD⁺’nın yenilenmesi','Glikolizin sürmesi için NAD⁺ gerekir; oksijensiz ortamda NAD⁺, fermantasyon basamağında NADH’ın yükseltgenmesiyle yenilenir.','Fermantasyonun ATP üretmediğini sanmak; fermantasyon basamağı engellenince glikolizin etkilenmeyeceğini düşünmek.','orta','düz',4,'hs-ferm')
W4='Hücre, glikolizle ATP sentezini başlangıçtaki hızında sürdürür.'
q('0004',tipId='hs-ferm',z='orta',alt='Fermantasyon',kaz='Fermantasyon basamağı engellenen hücrede NAD⁺, NADH, pirüvat ve ATP sentezindeki değişimleri yorumlar.',kalip='düz',
 kart=f'{k4} · laktat basamağının engellenmesi',
 metin='Oksijensiz ortamdaki bir iskelet kası hücresinde pirüvik asidin laktik aside dönüştüğü basamağı katalizleyen enzim, bir kimyasal maddeyle etkisiz hâle getirilmiştir. Hücrede glikoz ve ADP yeterince bulunmakta, NAD⁺ yenilenmesi için başka bir yol bulunmamaktadır.\nBuna göre, bu hücreyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=W4,
 sira=yer('E',W4,['Laktik asit oluşumu durur.','NADH’ın NAD⁺’ya yükseltgenmesi engellenir.','Pirüvik asit derişimi, glikoliz sürdüğü sürece artar.','NAD⁺ miktarı azaldıkça glikolizin hızı düşer.']),
 yan=[('Laktik asit oluşumu durur.','Kökün yanlış ifadeyi istediğini gözden kaçırıp doğru bir ifadeyi seçmek; laktik aside dönüşüm basamağı engellendiğinden laktik asit oluşmaz.','dikkat'),
      ('NADH’ın NAD⁺’ya yükseltgenmesi engellenir.','Doğru bir ifadeyi yanlış sanmak; oksijensiz ortamda NADH yalnız laktik asit oluşumu sırasında yükseltgendiğinden bu basamak durunca NAD⁺ yenilenemez.','bilgi'),
      ('Pirüvik asit derişimi, glikoliz sürdüğü sürece artar.','Doğru bir ifadeyi yanlış sanmak; pirüvik asit laktik aside dönüşemediği için glikoliz sürdüğü sürece birikir.','bilgi'),
      ('NAD⁺ miktarı azaldıkça glikolizin hızı düşer.','Doğru bir ifadeyi yanlış sanmak; glikolizde NAD⁺ indirgendiğinden NAD⁺ tükendikçe glikoliz yavaşlar.','bilgi')],
 istenen='Hücreyle ilgili yanlış yargı.',
 ip=['Kök yanlış yargıyı istiyor; engellenen basamağın hangi maddeyi yenilediğini bul ve bunun glikolizle bağını izleyerek her yargıyı sına.'],
 bilgi=[B('Fermantasyonun işlevi','fermantasyon, glikolizde indirgenen NAD⁺’nın yeniden oluşmasını sağlar · NAD⁺ yenilenemezse glikolizin devam edebilmesi sınırlanır')],
 ad=[A('Kökü oku','Yanlış yargı isteniyor; doğru olanlar elenecek.','Aranan: yanlış yargı'),
     A('Engellenen basamağın etkisi','Pirüvat laktik aside dönüşemez; bu dönüşümde NADH yükseltgendiğinden NAD⁺ da yenilenemez.','Laktik asit yok · NAD⁺ yenilenmez'),
     A('Glikolize etkisi','Glikolizde NAD⁺ indirgenir; NAD⁺ azaldıkça glikoliz yavaşlar ve pirüvat birikir.','Glikoliz yavaşlar'),
     A('Sonuç','ATP’nin başlangıç hızında sürdürüldüğünü söyleyen yargı yanlıştır.','Yanlış: hız aynı kalır')],
 puf='Engellenen basamağın hangi taşıyıcıyı yenilediğini bulup bu taşıyıcıya bağımlı basamağı düşün.')
SIRA[4]=4

# ===================== Q5 · izole mitokondri deneyi · orta · tablo · olumsuz =====================
k5=kartla(5,'İzole mitokondri deneyi','Basamakların hücrede ve organelde hangi bölgede gerçekleştiği, ayrılmış organel ve özütlerle yapılan deneylerin sonuçlarından çıkarılır.','Her basamak için mitokondri ya da sitoplazma enzimlerinin birlikte gerektiğini düşünmek; sonuçları olmayan bir koşula bağlamak.','orta','tablo',4,'hs-deney')
SK5=tablo_svg(['Tüp','Karışım','O₂','Gözlem'],[['K','Mitokondri + glikoz','Var','O₂ tüketilmedi, CO₂ yok'],['L','Mitokondri + pirüvik asit','Var','O₂ tüketildi, CO₂ çıktı'],['M','Sitoplazma özütü + glikoz','Var','Pirüvik asit oluştu, O₂ tüketilmedi']])
W5='Pirüvik asidin O₂ ile yıkımı için sitoplazmadaki enzimler gereklidir.'
q('0005',tipId='hs-deney',z='orta',alt='Solunum deneyi',kaz='İzole mitokondri ve sitoplazma özütü deney sonuçlarından basamakların gerçekleştiği yerleri çıkarır.',kalip='tablo',
 kart=f'{k5} · K, L, M tüpleri',
 metin='Bir hücreden mitokondriler ve mitokondrisiz sitoplazma özütü ayrı ayrı elde edilmiştir. Üç tüpe aşağıdaki karışımlar konmuş, ortamda O₂ bulunurken ve sıcaklık sabitken gerçekleşen olaylar gözlenmiştir. Sonuçlar tabloda verilmiştir.\nBuna göre, aşağıdakilerden hangisi söylenemez?',
 dogru=W5,
 sira=yer('B',W5,['Glikoliz basamağı mitokondri olmadan gerçekleşebilir.','Glikoz mitokondride doğrudan yıkılamaz.','Pirüvik asit, mitokondride O₂ kullanılarak yıkılabilir.','Glikolizin ürünü olan pirüvik asit O₂ kullanılmadan oluşur.']),
 yan=[('Glikoliz basamağı mitokondri olmadan gerçekleşebilir.','Kökün olumsuz olduğunu gözden kaçırıp doğru bir yargıyı seçmek; M tüpünde mitokondri bulunmadığı hâlde pirüvik asit oluşmuştur.','dikkat'),
      ('Glikoz mitokondride doğrudan yıkılamaz.','Kökün olumsuz olduğunu gözden kaçırıp doğru bir yargıyı seçmek; K tüpünde mitokondri glikozu yıkamadığı için O₂ tüketilmemiştir.','dikkat'),
      ('Pirüvik asit, mitokondride O₂ kullanılarak yıkılabilir.','Doğru bir yargıyı söylenemez sanmak; L tüpünde yalnız mitokondri ve pirüvik asit bulunduğu hâlde O₂ tüketilmiş ve CO₂ çıkmıştır.','bilgi'),
      ('Glikolizin ürünü olan pirüvik asit O₂ kullanılmadan oluşur.','Doğru bir yargıyı söylenemez sanmak; M tüpünde O₂ varken tüketilmediği hâlde pirüvik asit oluşmuştur.','bilgi')],
 istenen='Tablodan söylenemeyecek yargı.',
 ip=['Her tüpte karışıma hangi kısmın konduğuna ve O₂’nin tüketilip tüketilmediğine bak; bir yargının tabloda hangi tüpten desteklendiğini ara.'],
 bilgi=[B('Organel ve özüt deneyleri','hücre bölümlerine ayrılarak her bölümde hangi tepkimelerin yürüdüğü ayrı ayrı incelenebilir · Bir olayın bir bölümde gerçekleşmesi, başka bölümdeki bir bileşene ihtiyaç duymadığını gösterir')],
 ad=[A('Kökü oku','Tablodan söylenemeyecek yargı isteniyor; desteklenenler elenecek.','Aranan: söylenemeyen yargı'),
     A('K ve M tüplerini yorumla','K’de mitokondri glikozu yıkamamış, M’de sitoplazma özütü glikozdan pirüvik asit üretmiştir.','Glikoliz: mitokondrisiz'),
     A('L tüpünü yorumla','Mitokondri pirüvik asidi yıkmış, O₂ harcamış ve CO₂ çıkarmıştır; başka karışım bileşeni yoktur.','Pirüvat yıkımı: yalnız mitokondri'),
     A('Sonuç','Pirüvik asit yıkımı için sitoplazma enzimleri gerektiğini söyleyen yargı tabloyla çelişir.','Söylenemez: sitoplazma şartı')],
 puf='Her yargının tabloda hangi tüple desteklendiğini eşle; hiçbir tüple desteklenmeyen ya da çelişen yargıyı seç.',sekil=SK5)
SIRA[5]=5

# ===================== Q6 · basamak tablosu · orta · öncüllü · olumsuz =====================
k6=kartla(6,'Basamakların özelliklerinden yer ve ürün çıkarma','Basamakların CO₂ çıkışı, NADH oluşumu, O₂ kullanımı ve ATP sentezi gibi özellikleri karşılaştırılarak hangi basamak olduğu ve nerede gerçekleştiği çıkarılır.','Krebs döngüsü ile pirüvatın asetil CoA’ya dönüşümünü karıştırmak; ETS’yi matrikse yerleştirmek.','orta','tablo',3,'hs-yer')
SK6=tablo_svg(['Basamak','CO₂ açığa çıkar','NADH oluşur','O₂ kullanılır','ATP sentezlenir'],[['K','+','+','−','+'],['L','−','−','+','+'],['M','−','+','−','+'],['N','+','+','−','−']])
T6={'I','II'}   # doğru olan öncüller; kök yanlışları ister -> Yalnız III
YANLIS6={'III'}
N6={'I':'M basamağı CO₂ çıkarmayan, NADH oluşturan ve ATP sentezleyen glikolizdir; glikoliz sitoplazmada gerçekleşir, öncül doğrudur.',
    'II':'N basamağı pirüvatın asetil CoA’ya dönüşümüdür; ürünü asetil CoA, K basamağı olan Krebs döngüsünde yıkılır, öncül doğrudur.',
    'III':'L basamağı O₂ kullanılan elektron taşıma sistemidir; ETS mitokondrinin matriksinde değil iç zarında gerçekleşir, öncül yanlıştır.'}
d6,s6=onc_sec(YANLIS6,'B')
q('0006',tipId='hs-yer',z='orta',alt='Solunumun gerçekleştiği yerler',kaz='Tablodaki özelliklerden basamakları belirleyip yerlerine ve ürünlerine ilişkin yanlış öncülü bulur.',kalip='tablo',
 kart=f'{k6} · K, L, M, N basamakları',
 metin='Oksijenli solunumun glikoliz, pirüvatın asetil CoA’ya dönüşümü, Krebs döngüsü ve elektron taşıma sistemi (ETS) basamaklarına K, L, M ve N adları verilmiştir; adlar bu sıraya göre verilmemiştir. Basamaklarda gerçekleşen bazı olaylar tabloda verilmiştir (+: gerçekleşir, −: gerçekleşmez).\nI. M basamağı sitoplazmada gerçekleşir.\nII. N basamağında oluşan ürün K basamağında yıkılır.\nIII. L basamağı mitokondrinin matriksinde gerçekleşir.\nBuna göre, yukarıdaki öncüllerden hangileri yanlıştır?',
 dogru=d6,sira=s6,yan=onc_cel(YANLIS6,s6,d6,N6,olumsuz=True),
 istenen='Tabloya göre yanlış olan öncüller.',
 ip=['Önce tablodaki işaretlerden her harfin hangi basamak olduğunu belirle; sonra her öncülde adı geçen basamağı yeri ve ürünüyle karşılaştır.'],
 bilgi=[B('Basamakların özellikleri','dört basamaktan yalnız biri O₂ kullanır · CO₂ çıkışı yalnız mitokondride yürüyen iki basamakta görülür · Basamakların bir kısmı sitoplazmada, bir kısmı mitokondrinin farklı bölümlerinde gerçekleşir')],
 ad=[A('Basamakları belirle','O₂ kullanan L ETS’dir; CO₂ çıkarıp ATP sentezlemeyen N pirüvatın dönüşümüdür; CO₂ çıkarıp ATP sentezleyen K Krebs’tir; CO₂ çıkarmayan M glikolizdir.','K: Krebs · L: ETS · M: glikoliz · N: pirüvat dönüşümü')]+onc_adim(set(),N6)[0:0]+[
     A('I. öncülü değerlendir',N6['I'],'I: doğru'),A('II. öncülü değerlendir',N6['II'],'II: doğru'),A('III. öncülü değerlendir',N6['III'],'III: yanlış'),
     A('Sonuç','Yanlış olan öncül yalnız III’tür.','Yalnız III')],
 puf='İşaretlerden basamakları tanıdıktan sonra her öncülü basamağın yerine göre sına.',sekil=SK6)
SIRA[6]=6

# ===================== Q7 · ETS ATP'sinden Krebs CO2 · orta · sayısal =====================
k7=kartla(7,'ETS’deki ATP’den glikoz ve CO₂ sayısı','ETS’de elde edilen toplam ATP, bir glikozdan ETS’ye ulaşan NADH ve FADH₂ sayısıyla bölünerek yıkılan glikoz sayısı bulunur; sonra istenen basamağın ürünü hesaplanır.','Glikolizdeki ve pirüvat dönüşümündeki NADH’ı ya da FADH₂’yi unutmak; tüm CO₂’yi Krebs’ten saymak.','orta','düz',4,'hs-atp')
ETS_T=510; g7=Fr(ETS_T,ETS_G); assert g7==15
c7=KG['CO2']*g7; assert c7==60
y7=[(g7,'Bulunan glikoz sayısını Krebs döngüsünde çıkan CO₂ sayısı sanmak.','dikkat'),
    (KG['CO2']//2*g7,'Krebs’te glikoz başına yalnız 2 CO₂ (tek tur) çıktığını varsaymak.','islem'),
    (KG['CO2']*Fr(ETS_T,(GL['NADH']+PO['NADH']+KG['NADH'])*ETS_N),'FADH₂’nin ETS’deki katkısını hesaba katmayıp glikoz sayısını fazla bulmak.','islem'),
    ((PO['CO2']+KG['CO2'])*g7,'Pirüvatın asetil CoA’ya dönüşümünde çıkan CO₂’yi de Krebs döngüsüne eklemek.','islem')]
assert sayisal(c7,y7)==[15,30,60,68,90],sayisal(c7,y7)
q('0007',tipId='hs-atp',z='orta',alt='ATP ve taşıyıcı hesapları',kaz='ETS’de elde edilen toplam ATP’den yıkılan glikoz sayısını ve Krebs döngüsünde çıkan CO₂ miktarını hesaplar.',kalip='düz',
 kart=f'{k7} · ETS ATP’sinden Krebs CO₂’sine',
 metin='Oksijenli solunum yapan bir hücre kültüründe glikozun tamamı CO₂ ve H₂O’ya yıkılmıştır. ETS’de 1 NADH’ın yükseltgenmesiyle 3 ATP, 1 FADH₂’nin yükseltgenmesiyle 2 ATP sentezlendiği ve glikolizde oluşan NADH’ın da ETS’de yükseltgendiği kabul edilecektir. Kültürde ETS’de toplam 510 ATP sentezlenmiştir.\nBuna göre, aynı sürede Krebs döngüsünde açığa çıkan CO₂ molekülü sayısı kaçtır?',
 dogru=int(c7),yan=[(int(v),t,tu) for v,t,tu in y7],
 istenen='Krebs döngüsünde açığa çıkan CO₂ sayısı.',
 ip=['Bir glikozun ETS’ye kaç NADH ve kaç FADH₂ verdiğini üç basamaktan topla; ETS’deki ATP’yi bu değerle ilişkilendirip glikoz sayısına ulaş.'],
 bilgi=[B('Taşıyıcıların kaynakları','bir glikozdan oluşan NADH ve FADH₂’nin kaynakları glikoliz, pirüvatın asetil CoA’ya dönüşümü ve Krebs döngüsüdür · Krebs döngüsü bir glikoz için iki kez işler')],
 ad=[A('NADH sayısı','Bir glikozdan glikolizde 2, pirüvat dönüşümünde 2, Krebs’te 6 NADH oluşur.','2 + 2 + 6 = 10 NADH'),
     A('FADH₂ sayısı','Bir glikoz için Krebs’in iki turunda 2 FADH₂ oluşur.','2 FADH₂'),
     A('Bir glikozun ETS ATP’si','NADH başına 3, FADH₂ başına 2 ATP.','10 × 3 + 2 × 2 = 34 ATP'),
     A('Glikoz sayısı','Toplam ETS ATP’si bir glikozun değerine bölünür.','510 ÷ 34 = 15 glikoz'),
     A('Krebs CO₂’si','Bir glikozun iki Krebs turunda 4 CO₂ çıkar.','15 × 4 = 60 CO₂')],
 puf='Önce bir glikozun ETS’ye ulaştırdığı ATP’yi bul, sonra glikoz sayısından istenen basamağın ürününe geç.')
SIRA[7]=7

# ===================== Q8 · maya O2/CO2 grafiği · zor · sayısal =====================
k8=kartla(8,'Gaz grafiğinden toplam ATP hesabı','Tüketilen O₂ oksijenli solunumla yıkılan glikozu, toplam CO₂’den oksijenli solunum payı çıkarıldığında kalan CO₂ fermantasyonla yıkılan glikozu verir.','Toplam CO₂’nin tamamını tek yola bağlamak; iki yolun ATP verimini karıştırmak.','zor','grafik',5,'hs-grafik')
O2_0=24; CO2_T=48; t_o=6
g_oks=Fr(O2_0,6); co2_oks=g_oks*6; co2_f=CO2_T-co2_oks; g_f=Fr(co2_f,2)
assert (g_oks,co2_oks,co2_f,g_f)==(4,24,24,12)
atp8=g_oks*NET_G+g_f*FERM_ATP; assert atp8==176
y8=[(int(g_f*FERM_ATP),'Oksijenli solunumu hesaba katmayıp yalnız fermantasyonun ATP’sini bulmak.','islem'),
    (int(g_oks*(NET_G-2*GL['NADH']*ETS_N)+g_f*FERM_ATP),'Glikolizde ve pirüvat dönüşümünde oluşan NADH’ın ETS’deki ATP’sini hesaba katmamak.','islem'),
    (int(g_oks*NET_G),'Fermantasyonla yıkılan glikozun ATP’sini toplama eklememek.','islem'),
    (int(g_oks*(NET_G-GL['net']-KG['ATP'])+g_f*FERM_ATP),'Substrat düzeyinde kazanılan ATP’yi oksijenli solunumun toplamına eklememek.','islem')]
assert [v for v,_,_ in y8]==[24,128,152,160]
gr8=r'''\draw[-{Stealth[length=2.2mm,width=1.8mm]},line width=1pt] (0,0)--(6.4,0);\draw[-{Stealth[length=2.2mm,width=1.8mm]},line width=1pt] (0,0)--(0,3.6);
\foreach \x/\t in {0/0,1.2/2,2.4/4,3.6/6,4.8/8,6/10} {\draw (\x,0)--(\x,-.09) node[below,font=\footnotesize] {\t};}
\foreach \y/\t in {0/0,1.5/24,3/48} {\draw (0,\y)--(-.09,\y) node[left,font=\footnotesize] {\t};}
\node at (3.1,-.85) {Zaman (dk)};\node[rotate=90] at (-1.0,1.8) {Molekül sayısı};
\draw[line width=1.8pt] (0,1.5)--(3.6,0)--(6,0);
\draw[line width=1.8pt,dash pattern=on 5pt off 3pt,color=vurgu!70!black] (0,0)--(3.6,1.5)--(6,3);
\node[font=\small\bfseries,anchor=west] at (.15,1.75) {O$_2$};\node[font=\small\bfseries,color=vurgu!60!black,anchor=south] at (4.3,2.2) {CO$_2$};'''
SK8=tk(gr8,.85)
q('0008',tipId='hs-grafik',z='zor',alt='ATP hesapları',kaz='O₂ ve CO₂ grafiğinden iki yolla yıkılan glikozları bulup toplam net ATP’yi hesaplar.',kalip='grafik',
 kart=f'{k8} · kapalı kapta maya, O₂ ve CO₂',
 metin='Glikozlu besiyeri içeren kapalı bir kapta maya hücreleri bulunmakta ve kaptaki O₂ ile CO₂ moleküllerinin sayısı zamanla ölçülmektedir. Sonuçlar grafikte verilmiştir. Maya hücreleri ATP’yi yalnız oksijenli solunumla ve etil alkol fermantasyonuyla üretmekte, glikozun tamamını yıkmakta; ortamda başka CO₂ kaynağı ya da CO₂ tüketimi bulunmamaktadır. ETS’de 1 NADH’ın yükseltgenmesiyle 3 ATP, 1 FADH₂’nin yükseltgenmesiyle 2 ATP sentezlendiği ve glikolizde oluşan NADH’ın da ETS’de yükseltgendiği kabul edilecektir.\nBuna göre, 10. dakikaya kadar maya hücrelerinin oksijenli solunum ve etil alkol fermantasyonuyla kazandığı toplam net ATP sayısı kaçtır?',
 dogru=int(atp8),yan=y8,
 istenen='10. dakikaya kadar oksijenli solunum ve fermantasyonla kazanılan toplam net ATP sayısı.',
 ip=['O₂ yalnız bir yolda tüketilir; bu yolun CO₂’sini ayırarak kalan CO₂’nin hangi yola ait olduğunu bul ve iki yolun glikoz başına ATP’sini ayrı hesapla.'],
 bilgi=[B('Gaz alışverişi ve glikoz','oksijenli solunumda tüketilen O₂ ile çıkan CO₂ sayıları eşittir · Etil alkol fermantasyonunda ise O₂ tüketilmez ve glikoz başına CO₂ çıkar')],
 ad=[A('Oksijenli solunumu bul','Tüketilen O₂ oksijenli solunumdandır; 1 glikoz 6 O₂ tüketir.','24 ÷ 6 = 4 glikoz'),
     A('Fermantasyonun CO₂’sini bul','Oksijenli solunumda 6 CO₂ çıkar; toplam CO₂’den bu miktar çıkarılır.','48 − 4 × 6 = 24 CO₂'),
     A('Fermantasyonla yıkılan glikoz','Alkol fermantasyonunda 1 glikozdan 2 CO₂ çıkar.','24 ÷ 2 = 12 glikoz'),
     A('ATP’leri hesapla','Oksijenli solunumda glikoz başına 2 + 2 + 34 = 38, fermantasyonda 2 net ATP kazanılır.','4 × 38 + 12 × 2'),
     A('Sonuç','Toplam net ATP 176’dır.','152 + 24 = 176')],
 puf='Önce O₂’den oksijenli solunumu, sonra kalan CO₂’den fermantasyonu hesapla.',sekil=SK8)
SIRA[8]=8

# ===================== Q9 · bitki gaz alışverişi · zor · sayısal =====================
k9=kartla(9,'Işıkta solunum ve net CO₂ alışverişi','Işık varken de solunum sürer; net CO₂ alışverişi fotosentezle alınan ve solunumla verilen CO₂’nin farkıdır. Solunum hızı, ışık şiddeti sıfırken ölçülen CO₂ salınımından okunur.','Işık varken solunumun durduğunu sanmak; net CO₂ alımını solunuma ait saymak.','zor','grafik',4,'hs-grafik')
S9=12; N9=24
g9=Fr(S9,6); NN=GL['NADH']+PO['NADH']+KG['NADH']; atp9=g9*NN; assert atp9==20
y9=[(int(Fr(S9,KG['CO2'])*NN),'Solunum CO₂’sini yalnız Krebs döngüsündeki CO₂ (glikoz başına 4) kabul edip glikoz sayısını fazla bulmak.','islem'),
    (int(Fr(N9,6)*NN),'Net CO₂ alımını solunumla yıkılan glikoz hesabında kullanmak.','islem'),
    (int(Fr(N9+S9,6)*NN),'Fotosentezle alınan toplam CO₂’yi solunumla yıkılan glikoz hesabında kullanmak.','islem'),
    (S9*NN,'Solunumla verilen CO₂ sayısını yıkılan glikoz sayısı sanmak.','dikkat')]
assert sayisal(int(atp9),y9)==[20,30,40,60,120]
gr9=r'''\draw[-{Stealth[length=2.2mm,width=1.8mm]},line width=1pt] (0,0)--(6.6,0);\draw[-{Stealth[length=2.2mm,width=1.8mm]},line width=1pt] (0,-1.9)--(0,3.9);
\draw (0,-1.5)--(-.09,-1.5) node[left,font=\footnotesize] {$-12$};\draw (0,0)--(-.09,0) node[left,font=\footnotesize] {0};\draw (0,3)--(-.09,3) node[left,font=\footnotesize] {24};
\draw (5.4,0)--(5.4,-.09) ;\node[font=\small\bfseries,below] at (5.4,-.08) {K};
\node[font=\small,text width=3cm,align=center] at (3,-2.55) {Işık şiddeti};\node[font=\small,rotate=90,text width=5cm,align=center] at (-1.1,1.0) {CO$_2$ alışverişi (molekül/dk)};
\draw[line width=1.9pt,color=vurgu!70!black] (0,-1.5)--(1.8,0)--(4.8,3)--(6.3,3);
\draw[dashed,line width=.6pt] (5.4,0)--(5.4,3);\draw[dashed,line width=.6pt] (0,3)--(5.4,3);
\node[font=\footnotesize,text width=2cm,align=left] at (7.6,1.2) {$+$: alınan\\$-$: verilen};'''
SK9=tk(gr9,.8)
q('0009',tipId='hs-grafik',z='zor',alt='Taşıyıcı hesapları',kaz='Işık şiddetine bağlı net CO₂ alışverişi grafiğinden solunum hızını okuyup ETS’de yükseltgenen NADH sayısını hesaplar.',kalip='grafik',
 kart=f'{k9} · bitkide net CO₂ alışverişi',
 metin='Bir bitkinin yaprak hücrelerinde, farklı ışık şiddetlerinde dakikada gerçekleşen net CO₂ alışverişi grafikte gösterilmiştir. Bitki hücrelerinde oksijenli solunum hızı ışık şiddetinden bağımsız ve sabittir; solunum yalnız glikozla yapılmaktadır. Glikolizde, pirüvatın asetil CoA’ya dönüşümünde ve Krebs döngüsünde oluşan tüm NADH’ın ETS’de yükseltgendiği kabul edilecektir.\nBuna göre, ışık şiddeti K olduğunda bu hücrelerde dakikada ETS’de yükseltgenen toplam NADH sayısı kaçtır?',
 dogru=int(atp9),yan=y9,
 istenen='K ışık şiddetinde dakikada ETS’de yükseltgenen toplam NADH sayısı.',
 ip=['Solunum hızının ışıktan bağımsız olduğunu kullan; solunuma ait CO₂ salınımını ışığın hiç olmadığı durumdan oku ve glikoz sayısına çevir.'],
 bilgi=[B('Net CO₂ alışverişi','ışık varken hem fotosentez hem solunum sürer; grafikteki değer bu iki olayın farkını gösterir · Işık yokken fotosentez olmaz, yalnız solunumun CO₂ salınımı ölçülür')],
 ad=[A('Solunum hızını oku','Işık şiddeti sıfırken yalnız solunum sürer; hücreler dakikada CO₂ verir.','12 CO₂/dk'),
     A('Glikoza çevir','Oksijenli solunumda 1 glikozdan 6 CO₂ çıkar; hız sabit olduğundan K’de de aynıdır.','12 ÷ 6 = 2 glikoz/dk'),
     A('Glikoz başına NADH','Glikolizde 2, pirüvat dönüşümünde 2, Krebs döngüsünde 6 NADH oluşur.','2 + 2 + 6 = 10 NADH'),
     A('Sonuç','Yıkılan glikoz sayısı ile glikoz başına NADH sayısı çarpılır.','2 × 10 = 20')],
 puf='Işıktan bağımsız olan olayın değerini ışığın bulunmadığı koşuldan oku.',sekil=SK9)
SIRA[9]=9

# ===================== Q10 · alyuvar-kas grafiği · zor · öncüllü =====================
k10=kartla(10,'Mitokondrisiz hücrede O₂ etkisi','Mitokondrisi olmayan hücrelerde ATP yalnız glikolizle kazanıldığından O₂ derişimi fermantasyon hızını etkilemez; mitokondrili hücrelerde O₂ arttıkça oksijenli solunumun payı artar.','O₂ derişimini her hücre için fermantasyonu azaltan etken saymak; ATP verimini glikoz yıkım hızıyla karıştırmak.','zor','grafik',4,'hs-ferm')
gr10=r'''\draw[-{Stealth[length=2.2mm,width=1.8mm]},line width=1pt] (0,0)--(6.4,0);\draw[-{Stealth[length=2.2mm,width=1.8mm]},line width=1pt] (0,0)--(0,3.6);
\foreach \x/\t in {0/0,1.2/2,2.4/4,3.6/6,4.8/8,6/10} {\draw (\x,0)--(\x,-.09) node[below,font=\footnotesize] {\t};}
\foreach \y/\t in {0/0,1.5/4,3/8} {\draw (0,\y)--(-.09,\y) node[left,font=\footnotesize] {\t};}
\node at (3.1,-.85) {Ortamdaki O$_2$ derişimi (birim)};\node[rotate=90,text width=5.2cm,align=center] at (-1.0,1.7) {Laktik asit oluşum hızı (birim)};
\draw[line width=1.9pt] (0,3)--(6,3);
\draw[line width=1.9pt,dash pattern=on 5pt off 3pt,color=vurgu!70!black] (0,3)--(1.2,2.55)--(2.4,1.7)--(3.6,.95)--(4.8,.4)--(6,.15);
\node[font=\small\bfseries,anchor=south] at (5.2,3.05) {K};\node[font=\small\bfseries,color=vurgu!60!black,anchor=south west] at (4.6,.5) {L};'''
SK10=tk(gr10,.85)
T10={'II','III'}
N10={'I':'K kültüründe laktik asit oluşum hızı O₂ derişiminden etkilenmediğine göre K, mitokondrisi olmayan olgun alyuvarlardan oluşur; iskelet kası hücreleri L kültürüne uygundur.',
     'II':'L kültüründe laktik asit oluşumu O₂ arttıkça azaldığına ve glikoz yıkım hızı sabit olduğuna göre glikozun giderek daha büyük kısmı oksijenli solunumla yıkılır; bu nedenle glikoz başına net ATP artar.',
     'III':'K kültüründeki hücreler mitokondrisiz olduğundan glikozu yalnız glikoliz ve fermantasyonla yıkar; ATP yalnız glikolizde substrat düzeyinde fosforilasyonla sentezlenir.'}
d10,s10=onc_sec(T10,'D')
q('0010',tipId='hs-ferm',z='zor',alt='Fermantasyon',kaz='Farklı O₂ derişimlerinde iki kültürün laktik asit oluşum hızından hücre türlerini ve ATP üretim yollarını çıkarır.',kalip='grafik',
 kart=f'{k10} · K ve L kültürleri',
 metin='Glikozun bol bulunduğu bir ortamda, aynı sayıda olgun alyuvardan oluşan bir kültür ile aynı sayıda iskelet kası hücresinden oluşan bir kültürün laktik asit oluşum hızı, ortamdaki O₂ derişimine bağlı olarak ölçülmüş ve grafikte K ve L ile gösterilmiştir. Her iki kültürde de hücrelerin glikoz yıkım hızı O₂ derişiminden etkilenmemektedir.\nI. K kültürü iskelet kası hücrelerinden oluşmaktadır.\nII. L kültüründe glikoz başına kazanılan net ATP, O₂ derişimi arttıkça artmaktadır.\nIII. K kültüründe ATP yalnız substrat düzeyinde fosforilasyonla sentezlenmektedir.\nBuna göre, yukarıdaki öncüllerden hangileri doğrudur?',
 dogru=d10,sira=s10,yan=onc_cel(T10,s10,d10,N10),
 istenen='Grafikten çıkarılabilecek doğru öncüller.',
 ip=['Her eğrinin O₂ derişimiyle nasıl değiştiğine bak; hangi hücre türünde O₂’nin ATP üretim yolunu değiştirebileceğini mitokondri varlığıyla ilişkilendir.'],
 bilgi=[B('Olgun alyuvarın enerji metabolizması','olgun alyuvarda çekirdek ve mitokondri bulunmaz · İskelet kası hücresi ise mitokondri taşır ve oksijen yeterliyken oksijenli solunum yapabilir')],
 ad=[A('Eğrileri yorumla','K sabittir; L ise O₂ arttıkça düşer, yani L’de O₂ ile birlikte başka bir yıkım yolu devreye girer.','K: etkilenmez · L: azalır')]+onc_adim(T10,N10)+[A('Sonuç','Doğru öncüller II ve III’tür.','II ve III')],
 puf='Hangi hücrenin O₂’ye tepki verdiğini, hangisinin vermediğini mitokondri varlığıyla eşleştir.',sekil=SK10)
SIRA[10]=10

# ===================== YAZ =====================
yeni={f'{k:04d}':f'{SIRA[k]:04d}' for k in SIRA}
for qq in P.ANA:
    eski=qq['id'].rsplit('-',1)[1]; qq['id']=f"aytbio-hucresolunumiki-{yeni[eski]}"; qq['kardes']=None
P.ANA.sort(key=lambda x:x['id'])
for c in H.KARTLAR: c['kaynak']=KY
cnt=Counter(qq['zorluk'] for qq in P.ANA); print(cnt)
assert cnt==Counter(kolay=2,orta=5,zor=3),cnt
P.yaz(os.path.join(BD,'hucresolunumiki-1.json'),'/tmp/bos-hucresolunumiki.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Biyoloji dağılımı (yalnız mantık), MEB 12. sınıf biyoloji müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abhucresolunumiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
