"""Kesir Problemleri · ŞEKİLLİ paket (8 soru): şekil çözüm verisini taşır; sayılar Fraction ile hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians
H.KONU='Kesir Problemleri'
P=Parti('kesirsek','Kesir Problemleri','prob|Kesir Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli kesir problemleri; yalnız mantık) · MEB 6–8. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

KP=B('Kesrin değeri','bir bölmenin değeri, o bölmelerin toplam değerinin bölme sayısına bölünmesiyle bulunur; bütün, bölme sayısıyla çarpılarak bulunur. Örnek: 5 eş bölmenin 2’si 30 ise bir bölme 15, bütün 75’tir')
KB=B('Bütünün kesri','bütün 1’e eşittir; verilen kesirler toplanıp 1’den çıkarılınca kalan kesir bulunur. Örnek: 1/2 ve 1/4 kullanıldıysa kalan 1 − 3/4 = 1/4’tür')
KY2=B('Kesirle çarpma','bir niceliğin a/b’si, niceliği b’ye bölüp a ile çarpmaktır. Örnek: 40’ın 3/8’i 40 ÷ 8 × 3 = 15’tir')

# ---------- kartlar ----------
kartla('K-KSS-01','Bölmeli sütlük ve seviye','Doluluk bölme sayısından okunur; bilinen su miktarından bir bölmenin değeri, sonra boş bölmelerin hacmi bulunur.','Bölme değerini bidonun tamamına eşitlemek; boş bölme sayısını yanlış saymak.','kolay','şekilli',3,'ksp-bidon','Bölmeli bidon ve seviye')
kartla('K-KSS-02','Bölünmüş bahçe modeli','Karelerin sayısı şekilden sayılır; bilinen alandan bir karenin alanı, sonra istenen bölgenin karesi bulunur.','Ekili alanı boş alan sanmak; kareleri yanlış saymak.','kolay','şekilli',4,'ksp-bahce','Bölünmüş bahçe modeli')
kartla('K-KSS-03','Pasta dilimleri','Dilim sayıları şekilden okunur; bilinen kütleden bir dilimin kütlesi, sonra yenmeyen dilimlerin kütlesi bulunur.','Yenen ile yenmeyeni karıştırmak; dilim sayısını yanlış okumak.','orta','hikâyeli',4,'ksp-pasta','Pasta dilimleri')
kartla('K-KSS-04','Harcama şeridi','Şeritteki kesirler toplanıp 1’den çıkarılarak eksik kesir bulunur; bilinen tutardan bütün, sonra istenen kesirler hesaplanır.','Eksik kesri yanlış bulmak; kesirleri paydaları eşitlemeden toplamak.','orta','grafik',5,'ksp-serit','Harcama şeridi')
kartla('K-KSS-05','Yol haritası','Bilinen bölümün kesri 1’den diğer kesirlerin toplamı çıkarılarak bulunur; yolun tamamı, sonra istenen iki bölümün toplamı hesaplanır.','Kesirleri yola değil birbirine uygulamak; eksik kesri yanlış bulmak.','orta','hikâyeli',5,'ksp-yol','Yol haritası')
kartla('K-KSS-06','İki bidon ve aktarma','Bölme sayılarından su miktarları bulunur; ikinci bidonu doldurmak için gereken su ilk bidondan çıkarılır.','Boşluk yerine dolu miktarı aktarmak; kapasiteyi su sanmak.','orta','şekilli',4,'ksp-bidon','Bölmeli bidon ve seviye')
kartla('K-KSS-07','Kitap sayfa çubuğu ve ayraçlar','İki ayraç arasındaki bölme sayısından bir bölmenin sayfası bulunur; ardından kitabın kalan kısmı ve kesri hesaplanır.','Ayraç sayısını bölme sayısı sanmak; kalan kısmı yanlış ayraçtan başlatmak.','zor','şekilli',5,'ksp-kitap','Kitap sayfa çubuğu')
kartla('K-KSS-08','İki uçtan kesirli yol','Yolun iki ucundan verilen kesirler çıkarılınca ortada kalan kesir bulunur; bu kesrin km’si yoldan, sonra istenen uzunluk hesaplanır.','İki kesri aynı uçtan saymak; ortadaki bölümü çıkarmayı unutmak.','orta','hikâyeli',5,'ksp-yol','Yol haritası')

# ================= 1 kolay · bölmeli bidon =================
n_,d_=8,3; su=15; bol=Fr(su,d_); kap=bol*n_; assert bol==5 and kap==40; dg=kap-su; assert dg==25
e=[bol,(n_-d_-1)*bol,kap,su+kap]; assert e==[5,20,40,55] and len({dg,*e})==5
def bidon(cx,n,lvl,w=1.5,dh=0.5,etiket=''):
    H_=n*dh; o=[f'\\fill[fill=vurgu!15] ({cx-w/2},0) rectangle ({cx+w/2},{lvl*dh});',f'\\draw[thick] ({cx-w/2-0.1},{H_}) -- ({cx-w/2},{H_}) -- ({cx-w/2},0) -- ({cx+w/2},0) -- ({cx+w/2},{H_}) -- ({cx+w/2+0.1},{H_});']
    o.append(f'\\draw[line width=1.3pt] ({cx-w/2},{lvl*dh}) -- ({cx+w/2},{lvl*dh});')
    for i in range(1,n): o.append(f'\\draw[thin] ({cx+w/2-0.55},{i*dh}) -- ({cx+w/2},{i*dh});')
    o.append(f'\\draw[thin,dashed] ({cx-w/2},{H_}) -- ({cx+w/2},{H_});')
    if etiket: o.append(f'\\node at ({cx},-0.4) {{\\footnotesize {etiket}}};')
    return '\n'.join(o)
SK=fig(bidon(0,n_,d_,w=1.8,dh=0.4,etiket='Sütlük'))
q('0001',tipId='ksp-bidon',tip='Bölmeli bidon ve seviye',z='kolay',alt='Bölmeli Sütlük',kaz='Seviyeden bölme değerini bulup kabın boş kısmını hesaplar.',kalip='şekilli',
 kart='K-KSS-01 (sütlük) · 3/8 dolu = 15 L → 25 L eksik',
 metin='Bir çiftçi, süt topladığı eş bölmeli sütlüğün şekildeki seviyeye kadar dolu olduğunu görmüş ve içinde 15 litre süt olduğunu ölçmüştür. Sütlüğü ağzına kadar doldurup peynir yapımı için süt tesisine götürecektir.\nBuna göre, sütlüğü ağzına kadar doldurmak için kaç litre süt daha eklenmelidir?',
 dogru=dg,yan=[(e[0],'Bir bölmenin değerini (5 L) bulup bırakmış.','dikkat'),(e[1],'Boş bölme sayısını 4 saymış (üst kenarı çentik sanıp bir bölmeyi atlamış): 4 × 5.','dikkat'),(e[2],'Sütlüğün kapasitesini (40 L) eklenecek süt sanmış.','dikkat'),(e[3],'Kapasiteyi mevcut süte eklemiş: 15 + 40.','dikkat')],
 istenen='Eklenecek süt (L).',ip=['Sütün kaç bölmeyi doldurduğunu say; bir bölmenin kaç litre olduğunu bul.'],bilgi=[KP],sekil=SK,
 ad=[A('Dolu bölme','Süt 3 bölmeyi doldurmuştur.','3 bölme = 15 L'),A('Bir bölme','Bölme değeri.','15 ÷ 3 = 5 L'),A('Boş bölme','Toplam 8 bölme vardır.','8 − 3 = 5 bölme'),A('Eklenecek süt','Boş bölmelerin hacmi.','5 × 5 = 25 L')],
 puf='Önce bir bölmenin değerini bul, sonra boş bölmelerle çarp.')

# ================= 2 kolay · bahçe ızgara modeli =================
R_,C_=4,6; dom={(r,c) for r in range(R_) for c in (0,1)}; bib={(r,c) for r in range(3) for c in (2,3)}
assert len(dom)==8 and len(bib)==6 and not dom&bib
dalan=32; kare=Fr(dalan,len(dom)); assert kare==4; bos=R_*C_-len(dom)-len(bib); assert bos==10; dg=bos*kare; assert dg==40
e=[len(bib)*kare,(len(dom)+len(bib))*kare,(R_*C_-len(dom))*kare,R_*C_*kare]; assert e==[24,56,64,96] and len({dg,*e})==5
o=[]
for r in range(R_):
    for c in range(C_):
        t='D' if (r,c) in dom else 'B' if (r,c) in bib else ''
        f='vurgu!30' if t=='D' else 'vurgu!12' if t=='B' else 'white'
        o.append(f'\\draw[thick,fill={f}] ({c*0.9},{-r*0.9}) rectangle ({c*0.9+0.9},{-r*0.9-0.9});'+(f'\\node at ({c*0.9+0.45},{-r*0.9-0.45}) {{\\textbf{{{t}}}}};' if t else ''))
o.append(f'\\node at ({C_*0.45},-{R_*0.9+0.4}) {{\\footnotesize Bahçenin planı}};')
SK=fig('\n'.join(o))
q('0002',tipId='ksp-bahce',tip='Bölünmüş bahçe modeli',z='kolay',alt='Bölünmüş Bahçe',kaz='Izgaradan kare sayılarını bulup boş alanı hesaplar.',kalip='şekilli',
 kart='K-KSS-02 (bahçe ızgarası) · 8 kare = 32 m² → 10 boş kare',
 metin='Dikdörtgen biçimli bir bahçe, şekildeki gibi eş karelere ayrılmıştır. D ile gösterilen karelere domates, B ile gösterilen karelere biber dikilmiş; diğer kareler ise boş bırakılmıştır. Domates dikilen bölümün alanı 32 m²’dir.\nBuna göre, bahçenin boş bırakılan bölümü kaç m²’dir?',
 dogru=dg,yan=[(e[0],'Boş alan yerine biber alanını (6 kare) bulmuş.','dikkat'),(e[1],'Ekili alanı (14 kare) boş alan sanmış.','dikkat'),(e[2],'Biber karelerini çıkarmayı unutmuş: (24 − 8) × 4.','dikkat'),(e[3],'Bütün bahçenin alanını (24 kare) vermiş.','dikkat')],
 istenen='Boş bölümün alanı (m²).',ip=['Domates karelerini sayıp bir karenin alanını bul.'],bilgi=[KP],sekil=SK,
 ad=[A('Domates karesi','D ile gösterilen 8 kare vardır.','8 kare = 32 m²'),A('Bir kare','Alan kare sayısına bölünür.','32 ÷ 8 = 4 m²'),A('Boş kare','Toplam 24 kare; 8 domates, 6 biber.','24 − 8 − 6 = 10'),A('Boş alan','Boş kare sayısı × bir karenin alanı.','10 × 4 = 40 m²')],
 puf='Toplam kareden domates ve biber karelerini çıkar.')

# ================= 3 orta · pasta dilimleri =================
nd,ay,bo=12,3,4; ayg=270; dil=Fr(ayg,ay); assert dil==90; top=dil*nd; kal=nd-ay-bo; dg=kal*dil; assert dg==450 and top==1080
e=[bo*dil,(ay+bo)*dil,(nd-ay)*dil,top]; assert e==[360,630,810,1080] and len({dg,*e})==5
def pasta(r=1.5):
    o=[]
    for i in range(nd):
        a1=90-i*360/nd; a2=a1-360/nd; t='A' if i<ay else 'B' if i<ay+bo else ''
        f='vurgu!30' if t=='A' else 'vurgu!12' if t=='B' else 'white'
        o.append(f'\\draw[thick,fill={f}] (0,0) -- ({r*cos(radians(a1)):.3f},{r*sin(radians(a1)):.3f}) arc[start angle={a1:.2f},end angle={a2:.2f},radius={r}] -- cycle;')
        if t: am=radians((a1+a2)/2); o.append(f'\\node at ({0.95*r*cos(am)*0.78:.3f},{0.95*r*sin(am)*0.78:.3f}) {{\\textbf{{{t}}}}};')
    return '\n'.join(o)
SK=fig(pasta())
q('0003',tipId='ksp-pasta',tip='Pasta dilimleri',z='orta',alt='Pasta Dilimleri',kaz='Dilim sayılarından yenmeyen kısmın kütlesini bulur.',kalip='hikâyeli',
 kart='K-KSS-03 (pasta) · 12 dilim, 3 dilim = 270 g → 5 dilim 450 g',
 metin='Bir doğum günü pastası, şekildeki gibi eş dilimlere bölünmüştür. A ile gösterilen dilimleri Ayşe, B ile gösterilen dilimleri Bora yemiş; boş gösterilen dilimler ise henüz yenmemiştir. Ayşe’nin yediği pasta 270 gramdır.\nBuna göre, pastanın yenmeyen kısmı kaç gramdır?',
 dogru=dg,yan=[(e[0],'Yenmeyen yerine Bora’nın yediği 4 dilimi (4 × 90) bulmuş.','dikkat'),(e[1],'Yenen kısmı (7 dilim) yenmeyen sanmış: 7 × 90.','dikkat'),(e[2],'Yalnız Ayşe’nin yediğini çıkarmış: (12 − 3) × 90.','dikkat'),(e[3],'Pastanın tamamını (12 × 90) vermiş.','dikkat')],
 istenen='Yenmeyen kısmın kütlesi (g).',ip=['Ayşe’nin yediği dilim sayısından bir dilimin kütlesini bul.'],bilgi=[KP],sekil=SK,
 ad=[A('Ayşe’nin dilimleri','A ile 3 dilim gösterilmiştir.','3 dilim = 270 g'),A('Bir dilim','Kütle dilim sayısına bölünür.','270 ÷ 3 = 90 g'),A('Yenmeyen dilim','12 dilimden 3 + 4 dilim yenmiştir.','12 − 7 = 5 dilim'),A('Yenmeyen kütle','Dilim sayısı × bir dilimin kütlesi.','5 × 90 = 450 g')],
 puf='Önce bir dilimin kütlesini bul, sonra yenmeyen dilimleri say.')

# ================= 4 orta · harcama şeridi =================
ye,ul,ki=Fr(2,5),Fr(1,6),Fr(1,10); eg=1-ye-ul-ki; assert eg==Fr(1,3); egt=700; top=egt/eg; assert top==2100
dg=top*(ye+ki); assert dg==1050
e=[top*(ye+Fr(1,5)),(ye+ki)*(egt/Fr(1,4)),top*(1-ul),top]; assert e==[1260,1400,1750,2100] and len({dg,*e})==5
W=9.0; segs=[('Yemek',ye,'2/5'),('Ulaşım',ul,'1/6'),('Kitap',ki,'1/10'),('Eğlence',eg,'')]; x=0; o=[]
for ad,f,t in segs:
    w=float(f)*W; fl='vurgu!%d'%{'Yemek':30,'Ulaşım':18,'Kitap':8,'Eğlence':0}[ad]
    o.append(f'\\draw[thick,fill={fl if fl!="vurgu!0" else "white"}] ({x:.3f},0) rectangle ({x+w:.3f},0.9);\\node at ({x+w/2:.3f},0.45) {{\\footnotesize {ad}}};')
    if t: o.append(f'\\node at ({x+w/2:.3f},-0.3) {{\\footnotesize ${t.replace("/","/")}$}};')
    x+=w
o.append('\\node at (4.5,1.35) {\\footnotesize Aylık harçlığın harcama dağılımı (şerit tamamı: aylık harçlık)};')
SK=fig('\n'.join(o))
q('0004',tipId='ksp-serit',tip='Harcama şeridi',z='orta',alt='Harcama Şeridi',kaz='Şeritteki kesirlerden eksik kesri ve bütünü bulup istenen toplamı hesaplar.',kalip='grafik',
 kart='K-KSS-04 (harcama şeridi) · 2/5, 1/6, 1/10, eğlence 700 TL → yemek + kitap',
 metin='Bir lise öğrencisi, aylık harçlığını şekildeki şeritte gösterildiği gibi dört bölüme ayırarak harcamıştır. Şeritteki bölümlerin uzunlukları harcanan paranın harçlığa oranıyla orantılıdır. Eğlenceye ayırdığı bölümün tutarı 700 TL’dir.\nBuna göre, öğrencinin yemek ve kitaba ayırdığı toplam tutar kaç TL’dir?',
 dogru=dg,yan=[(e[0],'Kitabın kesrini 1/10 yerine 1/5 okumuş: 2100 × 3/5.','dikkat'),(e[1],'Eğlence bölümünü harçlığın 1/4’ü sanmış (harçlık 2800 TL): 2800 × 1/2.','dikkat'),(e[2],'Ulaşım dışındaki üç bölümü (yemek, kitap, eğlence: 5/6) toplamış: 2100 × 5/6.','dikkat'),(e[3],'Harçlığın tamamını (2100 TL) vermiş.','dikkat')],
 istenen='Yemek ve kitaba ayrılan toplam tutar (TL).',ip=['Önce eğlence bölümünün harçlığın kaçta kaçı olduğunu, diğer üç kesri toplayarak bul.'],bilgi=[KB,KY2],sekil=SK,
 ad=[A('Üç kesrin toplamı','Paydalar 30’da eşitlenir.','12/30 + 5/30 + 3/30 = 20/30 = 2/3'),A('Eğlence kesri','Bütünden çıkarılır.','1 − 2/3 = 1/3'),A('Aylık harçlık','1/3’ü 700 TL.','700 × 3 = 2100 TL'),A('Yemek + kitap kesri','2/5 + 1/10.','4/10 + 1/10 = 1/2'),A('Tutar','Harçlığın yarısı.','2100 × 1/2 = 1050 TL')],
 puf='Şeritte eksik bölümün kesri 1’den diğerleri çıkarılarak bulunur.')

# ================= 5 orta · yol haritası =================
ab,bc=Fr(2,9),Fr(1,3); cd_km=80; cd=1-ab-bc; assert cd==Fr(4,9); yol=cd_km/cd; assert yol==180; dg=(ab+bc)*yol; assert dg==100
e=[ab*yol,Fr(2+1,9+3)*yol,bc*yol,cd_km]; assert e==[40,45,60,80] and len({dg,*e})==5
W=9.0; xA,xB,xC,xD=0,float(ab)*W,float(ab+bc)*W,W
o=[f'\\draw[line width=1.6pt] ({xA},0) -- ({xD},0);']
for nm,x in zip('ABCD',(xA,xB,xC,xD)): o.append(f'\\fill ({x:.3f},0) circle (0.1);\\node[below=3pt] at ({x:.3f},0) {{\\textbf{{{nm}}}}};')
o.append(f'\\node[above] at ({(xA+xB)/2:.3f},0.15) {{\\footnotesize yolun $\\frac{{2}}{{9}}$’u}};\\node[above] at ({(xB+xC)/2:.3f},0.15) {{\\footnotesize yolun $\\frac{{1}}{{3}}$’ü}};\\node[above] at ({(xC+xD)/2:.3f},0.15) {{\\footnotesize {cd_km} km}};')
SK=fig('\n'.join(o))
q('0005',tipId='ksp-yol',tip='Yol haritası',z='orta',alt='Yol Haritası',kaz='Kesirli yol bölümlerinden yolun tamamını ve istenen iki bölümün toplamını bulur.',kalip='hikâyeli',
 kart='K-KSS-05 (yol) · 2/9 + 1/3 + 80 km → AC',
 metin='Bir bisiklet turu, A noktasından başlayıp B ve C noktalarından geçerek D noktasında sona ermektedir. Yolun bölümleri şekilde verilmiştir; AB ve BC bölümlerinin uzunlukları, turun tamamının uzunluğuna oranıyla gösterilmiştir ve bütün noktalar tek bir doğru üzerindedir.\nBuna göre, A ile C arasındaki yol kaç kilometredir?',
 dogru=dg,yan=[(e[0],'Yalnız AB bölümünü (2/9) bulmuş.','dikkat'),(e[1],'2/9 + 1/3’ü payları ve paydaları ayrı toplayarak 3/12 bulmuş: 180 × 1/4.','dikkat'),(e[2],'Yalnız BC bölümünü (1/3) bulmuş.','dikkat'),(e[3],'AC yerine şekilde verilen CD uzunluğunu (80 km) vermiş.','dikkat')],
 istenen='AC yolunun uzunluğu (km).',ip=['CD bölümünün yolun kaçta kaçı olduğunu, diğer iki kesri 1’den çıkararak bul.'],bilgi=[KB],sekil=SK,
 ad=[A('CD’nin kesri','Bütünden AB ve BC çıkarılır.','1 − 2/9 − 3/9 = 4/9'),A('Yolun tamamı','4/9’u 80 km.','80 ÷ 4 × 9 = 180 km'),A('AC’nin kesri','AB + BC.','2/9 + 3/9 = 5/9'),A('AC','Yolun 5/9’u.','180 × 5/9 = 100 km')],
 puf='Kesirlerin hepsi tüm yola uygulanır; bilinmeyen bölüm 1’den çıkarılarak bulunur.')

# ================= 6 orta · iki bidon ve aktarma =================
nA,dA,KA=6,5,24; nB,dB,KB_=5,2,15; sA=Fr(KA,nA)*dA; sB=Fr(KB_,nB)*dB; assert (sA,sB)==(20,6); akt=KB_-sB; assert akt==9<=sA; dg=sA-akt; assert dg==11
e=[sA-sB,sA-KB_,akt,KA-sA]; assert e==[14,5,9,4] and len({dg,*e})==5
SK=fig(bidon(0,nA,dA,w=1.6,dh=0.45,etiket='A (24 L)')+'\n'+bidon(3.4,nB,dB,w=1.6,dh=0.54,etiket='B (15 L)'))
q('0006',tipId='ksp-bidon',tip='Bölmeli bidon ve seviye',z='orta',alt='İki Bidon ve Aktarma',kaz='Seviyeleri litreye çevirip aktarılan su miktarını hesaplar.',kalip='şekilli',
 kart='K-KSS-06 (iki bidon) · A 5/6 · 24 L, B 2/5 · 15 L → A’da kalan 11 L',
 metin='Kapasiteleri şekilde verilen A ve B bidonlarının doluluk seviyeleri gösterilmiştir. Bir çiftçi, A bidonundaki sudan B bidonuna, B bidonu tamamen dolana kadar su aktarmıştır. Aktarma sırasında hiç su dökülmemiş ve taşma olmamıştır.\nBuna göre, bu işlemden sonra A bidonunda kaç litre su kalır?',
 dogru=dg,yan=[(e[0],'B’deki su kadar (6 L) aktarmış: 20 − 6.','dikkat'),(e[1],'B’nin kapasitesi (15 L) kadar aktarmış: 20 − 15.','dikkat'),(e[2],'Aktarılan suyu (9 L) A’da kalan sanmış.','dikkat'),(e[3],'A’nın boş kısmını (24 − 20) kalan sanmış.','dikkat')],
 istenen='A bidonunda kalan su (L).',ip=['İki bidondaki su miktarlarını litre olarak bul; B’nin dolması için ne kadar su gerektiğini hesapla.'],bilgi=[KP],sekil=SK,
 ad=[A('A’daki su','6 bölmenin 5’i dolu; bölme 4 L.','5 × 4 = 20 L'),A('B’deki su','5 bölmenin 2’si dolu; bölme 3 L.','2 × 3 = 6 L'),A('Aktarılan','B’yi doldurmak için gereken su.','15 − 6 = 9 L'),A('A’da kalan','A’dan aktarılan su çıkarılır.','20 − 9 = 11 L')],
 puf='Boş kalan kısım aktarılır, B’nin dolu kısmı değil.')

# ================= 7 zor · kitap sayfa çubuğu =================
Nb=12; pa,pb=5,9; ara=84; bol=Fr(ara,pb-pa); assert bol==21; top=bol*Nb; kalan=(Nb-pb)*bol; okur=kalan*Fr(2,3); dg=kalan-okur; assert (top,kalan,okur,dg)==(252,63,42,21)
bol2=Fr(ara,3); e=[kalan,okur,(Nb-pb)*bol2*Fr(1,3),(Nb-pa)*bol*Fr(1,3)]; assert e==[63,42,28,49] and len({dg,*e})==5
W=9.0; u=W/Nb; o=[f'\\draw[thick,fill=vurgu!8] (0,0) rectangle ({W},0.8);']
for i in range(1,Nb): o.append(f'\\draw[thin] ({i*u:.3f},0) -- ({i*u:.3f},0.8);')
for nm,p in (('A',pa),('B',pb)): o.append(f'\\draw[line width=2pt,color=vurgu] ({p*u:.3f},-0.15) -- ({p*u:.3f},0.95);\\node[above] at ({p*u:.3f},0.95) {{\\textbf{{{nm}}}}};')
o.append(f'\\node[below] at (0,-0.15) {{\\footnotesize 1. sayfa}};\\node[below] at ({W},-0.15) {{\\footnotesize son sayfa}};')
SK=fig('\n'.join(o))
q('0007',tipId='ksp-kitap',tip='Kitap sayfa çubuğu',z='zor',alt='Kitap Sayfa Çubuğu',kaz='Ayraçlar arasındaki sayfadan bölme değerini bulup kalan sayfanın kesrini hesaplar.',kalip='şekilli',
 kart='K-KSS-07 (sayfa çubuğu) · 4 bölme = 84, kalan 3 bölmenin 2/3’ü okunur',
 metin='Ece, okuduğu romanın sayfalarını temsil eden eş bölmeli çubuk üzerinde okuma ilerlemesini iki ayraçla göstermiştir. A ayracı ilk okuma gününün, B ayracı ikinci okuma gününün sonundaki yeri belirtmektedir. A ile B arasında 84 sayfa bulunmaktadır. Ece üçüncü gün, B ayracından sonra kalan sayfaların 2/3’ünü okumuştur.\nBuna göre, Ece’nin okumadığı kaç sayfa kalmıştır?',
 dogru=dg,yan=[(e[0],'Üçüncü gün okuduklarını hesaba katmamış: B’den sonra kalan 63 sayfa.','dikkat'),(e[1],'Kalan sayfa yerine üçüncü gün okuduğu sayfayı (42) bulmuş.','dikkat'),(e[2],'Bir bölmeyi 84 ÷ 3 = 28 almış (iki ayraç arasını 3 bölme sanmış): 3 × 28 × 1/3.','dikkat'),(e[3],'Kalan sayfayı A ayracından başlatmış: 7 × 21 × 1/3.','dikkat')],
 istenen='Okunmayan sayfa sayısı.',ip=['A ile B arasındaki bölme sayısını say; bir bölmenin kaç sayfa olduğunu bul.'],bilgi=[KP,KY2],sekil=SK,
 ad=[A('Bölme sayısı','A 5., B 9. çizgidedir.','9 − 5 = 4 bölme'),A('Bir bölme','84 sayfa 4 bölmedir.','84 ÷ 4 = 21 sayfa'),A('B’den sonra','Toplam 12 bölme vardır.','12 − 9 = 3 bölme = 63 sayfa'),A('Üçüncü gün','Kalanın 2/3’ü okunur.','63 × 2/3 = 42 sayfa'),A('Okunmayan','Kalandan okunan çıkarılır.','63 − 42 = 21 sayfa')],
 puf='Kalan sayfanın 2/3’ü okunduğuna göre geriye 1/3’ü kalır.')

# ================= 8 zor · iki uçtan kesirli yol =================
ac,db=Fr(2,5),Fr(1,4); cd=1-ac-db; assert cd==Fr(7,20); cdkm=42; yol=cdkm/cd; assert yol==120; dg=(1-db)*yol; assert dg==90
e=[ac*yol,(ac+db)*yol,yol,dg+cdkm]; assert e==[48,78,120,132] and len({dg,*e})==5
W=9.0; xs={'A':0,'C':float(ac)*W,'D':float(1-db)*W,'B':W}
o=[f'\\draw[line width=1.6pt] (0,0) -- ({W},0);']
for nm,x in xs.items(): o.append(f'\\fill ({x:.3f},0) circle (0.1);\\node[above=3pt] at ({x:.3f},0) {{\\textbf{{{nm}}}}};')
o.append(f'\\draw[thick] (0,-0.3) -- (0,-0.4) -- ({xs["C"]:.3f},-0.4) -- ({xs["C"]:.3f},-0.3);\\node at ({xs["C"]/2:.3f},-0.75) {{\\footnotesize yolun $\\frac{{2}}{{5}}$’i}};')
o.append(f'\\draw[thick] ({xs["D"]:.3f},-0.3) -- ({xs["D"]:.3f},-0.4) -- ({W},-0.4) -- ({W},-0.3);\\node at ({(xs["D"]+W)/2:.3f},-0.75) {{\\footnotesize yolun $\\frac{{1}}{{4}}$’ü}};')
o.append(f'\\draw[thick] ({xs["C"]:.3f},-0.3) -- ({xs["C"]:.3f},-0.4) -- ({xs["D"]:.3f},-0.4) -- ({xs["D"]:.3f},-0.3);'.replace('-0.4','-1.25').replace('-0.3','-1.15')+f'\\node at ({(xs["C"]+xs["D"])/2:.3f},-1.6) {{\\footnotesize {cdkm} km}};')
SK=fig('\n'.join(o))
q('0008',tipId='ksp-yol',tip='Yol haritası',z='orta',alt='İki Uçtan Kesirli Yol',kaz='Yolun iki ucundan verilen kesirlerle ortadaki bölümü bulup uzunlukları hesaplar.',kalip='hikâyeli',
 kart='K-KSS-08 (iki uç) · AC = 2/5, DB = 1/4, CD = 42 km → AD',
 metin='A ve B şehirleri arasındaki düz bir karayolu üzerinde C ve D mola noktaları vardır. Yolun A ucundan C noktasına kadar olan bölümü ile D noktasından B ucuna kadar olan bölümü, A ile B arasındaki yolun kesirleriyle şekilde gösterilmiştir. C ile D arasındaki uzaklık da şekilde verilmiştir.\nBuna göre, A ile D arasındaki yol kaç kilometredir?',
 dogru=dg,yan=[(e[0],'AD yerine AC’yi (2/5 × 120) bulmuş.','dikkat'),(e[1],'CD’yi çıkarıp AC + DB’yi (78 km) vermiş.','dikkat'),(e[2],'Yolun tamamını (120 km) vermiş.','dikkat'),(e[3],'AD’ye CD’yi bir kez daha eklemiş: 90 + 42.','dikkat')],
 istenen='AD yolunun uzunluğu (km).',ip=['CD bölümünün yolun kaçta kaçı olduğunu bulmak için iki uçtaki kesirleri 1’den çıkar.'],bilgi=[KB],sekil=SK,
 ad=[A('Uçlardaki kesirler','AC ve DB.','2/5 + 1/4 = 13/20'),A('CD’nin kesri','Bütünden çıkarılır.','1 − 13/20 = 7/20'),A('Yolun tamamı','7/20’si 42 km.','42 ÷ 7 × 20 = 120 km'),A('DB','Yolun 1/4’ü.','120 ÷ 4 = 30 km'),A('AD','Yoldan DB çıkarılır.','120 − 30 = 90 km')],
 puf='AD = yolun tamamı − DB; DB doğrudan 1/4’ten bulunur.')

bitir(P,'kesirsek','prob|Kesir Problemleri')
