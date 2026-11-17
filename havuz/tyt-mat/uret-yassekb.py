"""Yaş Problemleri · ŞEKİLLİ ek paket b (10 soru): şekil/tablo çözüm verisini taşır; her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians
H.KONU='Yaş Problemleri'
UK='prob|Yaş Problemleri'
P=Parti('yassekb','Yaş Problemleri',UK)
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu yaş soruları; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

FRK=B('Yaş farkı','iki kişinin yaş farkı hiçbir zaman değişmez; her ikisi de aynı süre sonra aynı miktar büyür. Örnek: bugün 30 ve 10 yaşında olanlar, 5 yıl sonra 35 ve 15 yaşında olur; fark 20 olarak kalır')
KUT=B('Kutu modeli','yaşlar eş kutularla gösterildiğinde her kutu aynı yaşa karşılık gelir; toplam ya da fark, kutu sayısına bölünerek bir kutunun değeri bulunur. Örnek: 4 kutu 20 yaşı gösteriyorsa bir kutu 5 yaştır')
SIM=B('Yıllar sonra toplam','n kişinin yaşları toplamı, her yıl n artar; hedef toplama ulaşmak için gereken yıl, eksik toplamın kişi sayısına bölümüdür. Örnek: iki kişinin toplamı 10 iken 30 olması 20 ÷ 2 = 10 yıl sonradır')
ORT=B('Yaş ortalaması','ortalama, tüm yaşların toplamının kişi sayısına bölümüdür; gruplarda her yaş, kişi sayısıyla çarpılıp toplanır. Örnek: 2 kişi 10, 3 kişi 20 yaşındaysa ortalama (20 + 60) ÷ 5 = 16’dır')
YIL=B('Doğum yılı ve yaş','bir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki farktır; yıllar sonra ya da önce yaşlar o kadar artar ya da azalır. Örnek: 1990’da doğan kişi 2010’da 20 yaşındadır')
IFD=B('Konuşmalardan yaş bulma','her ifade bir yaş ilişkisi verir; ilişkiler ortak bir bilinmeyen cinsinden yazılıp bilinen toplam kullanılarak çözülür. Örnek: “Ben senden 5 yaş büyüğüm; yaşlarımız toplamı 25” → senin yaşın 10’dur')

kartla('K-YAB-01','Yaş–yıl çizgi grafiği','Yaş farkı grafikteki iki noktadan bulunur; oran koşulundan küçüğün yaşı hesaplanır.','Grafikteki değeri cevap sanmak; farkı yaş sanmak.','orta','grafik',3,'yab-grafik','Grafik okuma ve yaş')
kartla('K-YAB-02','Eş kutulu çubuk modeli','Kutu sayılarından toplamın kaç kutu olduğu, bir kutunun yaşı ve istenen fark bulunur.','Kutu sayısını yaş sanmak; toplamı bölmeyi unutmak.','kolay','hikâyeli',3,'yab-model','Kutu modeli')
kartla('K-YAB-03','Mumlu pasta simgeleri','Mum sayıları yaşları verir; hedef toplamla farkı kişi sayısına bölünür.','Eksik toplamı yıl sanmak; kişi sayısına bölmemek.','kolay','hikâyeli',3,'yab-simge','Simge grafiği ve toplam yaş')
kartla('K-YAB-04','Daire grafiğinde yaş ortalaması','Dilim yüzdelerinden kişi sayıları, oradan toplam yaş bulunur; yeni üyelerle ortalama yeniden hesaplanır.','Yüzdeleri yaş sanmak; yeni üyeleri sayıya katmamak.','orta','grafik',4,'yab-grafik','Grafik okuma ve yaş')
kartla('K-YAB-05','Yaşam çubukları','Doğum yıllarından yaşlar bulunur; geçmişte aynı süre çıkarılarak oran koşulundan süre çözülür.','Her kişiden farklı süre çıkarmak; yıl sayısını iki kez saymamak.','zor','hikâyeli',4,'yab-yil','Doğum yılı ve yaş')
kartla('K-YAB-06','Konuşma balonları','Üç ifade ortak bir bilinmeyen cinsinden yazılır; toplam koşulundan çocuğun yaşı, sonra babanın yaşı bulunur.','Doğum anındaki yaşı bugünkü yaş sanmak; anneyi babadan büyük almak.','orta','hikâyeli',4,'yab-ifade','Konuşmalardan yaş bulma')
kartla('K-YAB-07','Önce ve sonra kutu modeli','İki zamanın kutu oranları ve yıl farkı birlikte yazılır; çocuğun yaşı bulunup anneye geçilir.','Oranı iki zamana aynı almak; yıl farkını unutmak.','orta','yeni nesil',3,'yab-model','Kutu modeli')
kartla('K-YAB-08','Nokta grafiği ve ortalama','Her yaşın nokta sayısı kişi sayısıdır; yaşlar bu sayılarla çarpılıp toplanır ve toplam kişiye bölünür.','Yaş değerlerinin ortalamasını almak; en sık yaşı ortalama sanmak.','kolay','grafik',3,'yab-grafik','Grafik okuma ve yaş')
kartla('K-YAB-09','Takım ortalamaları tablosu','Her takımın toplam yaşı bulunur; hepsi toplanıp toplam oyuncuya bölünür.','Ortalamaların ortalamasını almak; tek takıma bakmak.','orta','tablo',3,'yab-tablo','Yaş ortalaması tablosu')
kartla('K-YAB-10','Doğum yılı çizgisi','Bugünün yılı bilinmeyen olarak alınıp yaşlar yıl cinsinden yazılır; verilen oran denklemi çözülür.','Yılı yaş sanmak; doğum yıllarını karıştırmak.','zor','hikâyeli',4,'yab-yil','Doğum yılı ve yaş')

# ===== 01 orta · çizgi grafiği =====
a0,a1,k0,k1=45,55,5,15; fark=a0-k0; assert a1-k1==fark==40
v=Fr(fark,2); assert v==20 and 3*v-v==fark
e=[k0,fark,a1,3*v]
assert e==[5,40,55,60] and len({v,*e})==5
sx,sy=0.28,0.052; o=[f'\\draw[-{{Stealth}}] (0,0) -- (3.4,0) node[right] {{yıl}}; \\draw[-{{Stealth}}] (0,0) -- (0,3.3) node[above] {{yaş}};']
for t in (2015,2025): o.append(f'\\draw ({(t-2013)*sx:.2f},-0.06) -- ({(t-2013)*sx:.2f},0.06); \\node[below=2pt] at ({(t-2013)*sx:.2f},0) {{{t}}};')
for t in (10,20,30,40,50,60): o.append(f'\\draw[gray!50,dashed] (0,{t*sy:.2f}) -- (3.2,{t*sy:.2f}); \\draw (-0.06,{t*sy:.2f}) -- (0.06,{t*sy:.2f}); \\node[left=2pt] at (0,{t*sy:.2f}) {{{t}}};')
for (y0,y1,nm) in ((a0,a1,'Anne'),(k0,k1,'Kız')):
    o.append(f'\\draw[thick,vurgu!80!black] ({2*sx:.2f},{y0*sy:.2f}) -- ({12*sx:.2f},{y1*sy:.2f}); \\fill[vurgu!80!black] ({2*sx:.2f},{y0*sy:.2f}) circle (0.06); \\fill[vurgu!80!black] ({12*sx:.2f},{y1*sy:.2f}) circle (0.06); \\node[right=3pt] at ({12*sx:.2f},{y1*sy:.2f}) {{{nm}}};')
SK=fig('\n'.join(o))
q('0001',tipId='yab-grafik',tip='Grafik okuma ve yaş',z='orta',alt='Yaş–Yıl Grafiği',kaz='Grafikteki iki noktadan yaş farkını bulup bir oran koşulunda küçüğün yaşını hesaplar.',kalip='grafik',
 kart='K-YAB-01 · anne 45→55, kız 5→15; anne=3×kız',
 metin='Şekildeki grafikte, bir annenin ve kızının yaşları 2015 ve 2025 yıllarında verilmiştir; iki kişinin yaşı da yıllar içinde her yıl 1 artmaktadır. Anne ile kız, ileride bir yıl, fotoğraf stüdyosunda aile fotoğrafı çektireceklerdir. Fotoğraf çekimi, annenin yaşının kızının yaşının tam 3 katı olduğu yıl yapılacaktır.\nBuna göre, fotoğraf çekildiği yılda kız kaç yaşındadır?',
 dogru=20,yan=[(5,'2015’teki kız yaşını yazmış.','dikkat'),(40,'Yaş farkını (40) kızın yaşı sanmış.','dikkat'),(55,'2025’teki anne yaşını (55) kızın yaşı sanmış.','dikkat'),(60,'Annenin o yıldaki yaşını (60) kızın yaşı sanmış.','dikkat')],
 istenen='Fotoğraf çekildiği yılda kızın yaşı.',ip=['Grafikteki iki noktadan her iki kişinin yaşı arasındaki ilişkinin zamanla değişip değişmediğine bak.'],bilgi=[FRK],sekil=SK,
 ad=[A('Yaş farkı','2015’te anne 45, kız 5.','45 − 5 = 40 (hep sabit)'),A('Oran koşulu','Anne yaşı kızın 3 katı ise fark kızın yaşının 2 katıdır.','3k − k = 40'),A('Kızın yaşı','k bulunur.','k = 20')],
 puf='Yaşlar arasındaki fark yıllar geçse de aynıdır.')

# ===== 02 kolay · eş kutulu çubuk =====
kut=[('Ece',2),('Can',3),('Deniz',5)]; top=60; kb=Fr(top,sum(n for _,n in kut)); v=(5-2)*kb
e=[3,kb,2*kb,5*kb]
assert kb==6 and v==18 and e==[3,6,12,30] and len({v,*e})==5
u=0.8; o=[]
for i,(nm,n) in enumerate(kut):
    y=-i*0.85; o.append(f'\\node[left] at (-0.1,{y}) {{{nm}}};')
    for j in range(n): o.append(f'\\filldraw[fill=vurgu!{25 if j%2==0 else 40},draw=vurgu!80!black] ({j*u},{y-0.3}) rectangle ({(j+1)*u},{y+0.3});')
SK=fig('\n'.join(o))
q('0002',tipId='yab-model',tip='Kutu modeli',z='kolay',alt='Eş Kutulu Çubuk',kaz='Eş kutularla verilen üç yaşın toplamından bir kutunun değerini bulup en büyük ile en küçük yaşın farkını hesaplar.',kalip='hikâyeli',
 kart='K-YAB-02 · 2, 3, 5 kutu; toplam 60',
 metin='Üç kardeşin bugünkü yaşları, eş kutulardan oluşan çubuklarla şekilde gösterilmiştir; her kutu aynı sayıda yaşı temsil etmektedir. Üç kardeşin yaşları toplamı 60’tır. Aile, en büyük kardeşle en küçük kardeş arasındaki yaş farkına göre bir yıllık harçlık düzenlemesi yapacaktır.\nBuna göre, en büyük kardeşle en küçük kardeşin yaşları arasındaki fark kaçtır?',
 dogru=v,yan=[(3,'Kutu sayıları farkını (3) yaş farkı sanmış.','dikkat'),(kb,'Bir kutunun değerini (6) fark sanmış.','dikkat'),(2*kb,'En küçük kardeşin yaşını (12) fark sanmış.','dikkat'),(5*kb,'En büyük kardeşin yaşını (30) fark sanmış.','dikkat')],
 istenen='En büyük ile en küçük kardeşin yaş farkı.',ip=['Çubuklardaki toplam kutu sayısını bul; toplam yaşın bir kutuya düşen payını hesapla.'],bilgi=[KUT],sekil=SK,
 ad=[A('Toplam kutu','2 + 3 + 5 kutu.','10 kutu'),A('Bir kutu','Toplam yaş kutu sayısına bölünür.','60 ÷ 10 = 6'),A('Fark','Kutu farkı bir kutuyla çarpılır.','(5 − 2) × 6 = 18')],
 puf='Önce bir kutunun kaç yaşı gösterdiğini bul.')

# ===== 03 kolay · mum simgeleri =====
mum=[('Ali',8),('Ece',11),('Cem',5)]; tp=sum(n for _,n in mum); hedef=60; v=Fr(hedef-tp,3)
e=[Fr(hedef-tp,2),Fr(hedef,3),tp,hedef-tp]
assert tp==24 and v==12 and e==[18,20,24,36] and len({v,*e})==5
o=[]
for i,(nm,n) in enumerate(mum):
    x0=i*3.7
    o.append(f'\\filldraw[fill=vurgu!15,draw=black,thick] ({x0},0) rectangle ({x0+3.2},0.7); \\node[below=2pt] at ({x0+1.6},0) {{{nm}}};')
    for j in range(n):
        cx=x0+0.2+(j%11)*0.28
        cy=0.7+(j//11)*0.0
        o.append(f'\\draw[line width=2pt,vurgu!60!black] ({cx:.2f},{cy}) -- ({cx:.2f},{cy+0.5}); \\fill[orange!80!yellow] ({cx:.2f},{cy+0.62}) circle (0.06);')
SK=fig('\n'.join(o))
q('0003',tipId='yab-simge',tip='Simge grafiği ve toplam yaş',z='kolay',alt='Mumlu Pasta',kaz='Pastalardaki mum sayılarından yaşlar toplamını bulup hedef toplama kaç yıl sonra ulaşılacağını hesaplar.',kalip='hikâyeli',
 kart='K-YAB-03 · 8, 11, 5 mum; hedef toplam 60',
 metin='Üç kardeş Ali, Ece ve Cem, doğum günlerini aynı gün kutlamaktadır. Her kardeşin pastasına yaşı kadar mum konulmuş ve pastalar şekilde gösterilmiştir; başka mum yoktur. Kardeşler, yaşları toplamının ilk kez 60 olacağı doğum gününde büyük bir parti yapmayı planlamaktadır.\nBuna göre, bu parti bu doğum gününden kaç yıl sonra yapılacaktır?',
 dogru=v,yan=[(e[0],'Kişi sayısı yerine 2’ye bölmüş: 36 ÷ 2.','dikkat'),(e[1],'60’ı kişi sayısına bölüp yıl sanmış.','dikkat'),(e[2],'Bugünkü toplam yaşı (24) yıl sanmış.','dikkat'),(e[3],'Eksik toplamı (36) kişi sayısına bölmeden yıl sanmış.','dikkat')],
 istenen='Partiye kalan yıl.',ip=['Mumlardan şimdiki toplam yaşı bul; her yıl bu toplamın kaç arttığını düşün.'],bilgi=[SIM],sekil=SK,
 ad=[A('Bugünkü toplam','Mum sayıları toplanır.','8 + 11 + 5 = 24'),A('Eksik toplam','Hedefe kalan.','60 − 24 = 36'),A('Yıl','Her yıl toplam 3 artar.','36 ÷ 3 = 12')],
 puf='Her yıl üç kişi birden bir yaş büyür.')

# ===== 04 orta · daire grafiği =====
yg=[(10,20),(12,50),(15,30)]; n=40; toplam=sum(Fr(n*p,100)*a for a,p in yg); ort=Fr(toplam,n); yeni=10; v=(toplam+yeni*15)/(n+yeni)
e=[12,ort,(ort+15)/2,15]
assert toplam==500 and ort==Fr(25,2) and v==13 and e==[12,Fr(25,2),Fr(55,4),15] and len({v,*e})==5
def pasta(dilim,r=1.5,tonlar=(20,40,60)):
    o=[]; ang=90
    for i,(nm,pc,lab) in enumerate(dilim):
        a1,a2=ang,ang-3.6*pc; mid=radians((a1+a2)/2)
        o.append(f'\\draw[thick,fill=vurgu!{tonlar[i%3]}] (0,0) -- ({r*cos(radians(a1)):.3f},{r*sin(radians(a1)):.3f}) arc[start angle={a1},end angle={a2},radius={r}] -- cycle;')
        ax='west' if cos(mid)>0.1 else 'east' if cos(mid)<-0.1 else 'center'
        o.append(f'\\node[anchor={ax},align=center] at ({(r+0.15)*cos(mid):.3f},{(r+0.3)*sin(mid):.3f}) {{{nm}\\\\{lab}}};'); ang=a2
    return o
SK=fig('\n'.join(pasta([('10 yaş',20,'\\%20'),('12 yaş',50,'\\%50'),('15 yaş',30,'\\%30')])))
q('0004',tipId='yab-grafik',tip='Grafik okuma ve yaş',z='orta',alt='Daire Grafiği',kaz='Daire grafiğindeki yaş dağılımından ortalamayı bulup yeni üyeler katılınca ortalamayı yeniden hesaplar.',kalip='grafik',
 kart='K-YAB-04 · 40 üye; %20·10, %50·12, %30·15; +10 üye 15 yaş',
 metin='Bir bilim kulübündeki 40 üyenin yaşlarına göre dağılımı şekildeki daire grafikte yüzde olarak verilmiştir; her üye yalnız bir yaş grubundadır. Kulübe 15 yaşında 10 yeni üye katılmış ve başka bir değişiklik olmamıştır. Kulüp başkanı, yeni üyelerle birlikte kulübün yaş ortalamasını açıklayacaktır.\nBuna göre, kulübün yeni yaş ortalaması kaçtır?',
 dogru=v,yan=[(e[0],'En çok üyesi olan yaşı (12) ortalama sanmış.','dikkat'),(e[1],'Yeni üyeleri hesaba katmamış; eski ortalamayı yazmış.','dikkat'),(e[2],'Eski ortalama ile yeni üyelerin yaşının ortalamasını almış: (12,5 + 15) ÷ 2.','dikkat'),(e[3],'Yeni üyelerin yaşını (15) ortalama sanmış.','dikkat')],
 istenen='Yeni yaş ortalaması.',ip=['Dilim yüzdelerinden her yaş grubundaki üye sayısını ve toplam yaşı bul; yeni üyelerin toplam yaşını ekle.'],bilgi=[ORT],sekil=SK,
 ad=[A('Üye sayıları','Her dilim 40 kişinin yüzdesi.','8 üye 10 yaş, 20 üye 12 yaş, 12 üye 15 yaş'),A('Eski toplam yaş','Yaş × kişi sayısı toplanır.','80 + 240 + 180 = 500'),A('Yeni toplam','10 üye × 15 yaş eklenir.','500 + 150 = 650'),A('Ortalama','Yeni toplam, 50 kişiye bölünür.','650 ÷ 50 = 13')],
 puf='Ortalama için toplam yaşı ve kişi sayısını ayrı bul.')

# ===== 05 zor · yaşam çubukları =====
dog={'Anne':1978,'Baba':1979,'Ali':2004,'Ece':2013}; bg=2026
Pt=(bg-dog['Anne'])+(bg-dog['Baba']); Kt=(bg-dog['Ali'])+(bg-dog['Ece'])
tt=lambda k: Fr(k*Kt-Pt,2*(k-1))
v=tt(5); e=[tt(3),tt(4),tt(6),2*v]
assert Pt==95 and Kt==35 and v==10 and e==[Fr(5,2),Fr(15,2),Fr(23,2),20] and len({v,*e})==5
assert (Pt-2*v)==5*(Kt-2*v)
sx=0.105; o=[]
for i,(nm,b) in enumerate(dog.items()):
    y=-i*0.8; x0=(b-1975)*sx
    o.append(f'\\node[left] at (-0.1,{y}) {{{nm}}}; \\filldraw[fill=vurgu!30,draw=vurgu!80!black] ({x0:.2f},{y-0.28}) rectangle ({(bg-1975)*sx:.2f},{y+0.28}); \\node[anchor=west] at ({x0+0.05:.2f},{y}) {{{b}}};')
yb=-3*0.8-0.55
o.append(f'\\draw[-{{Stealth}}] (0,{yb}) -- ({(2030-1975)*sx:.2f},{yb});')
for t in (1975,1985,1995,2005,2015,2025): o.append(f'\\draw ({(t-1975)*sx:.2f},{yb-0.07}) -- ({(t-1975)*sx:.2f},{yb+0.07}); \\node[below=2pt] at ({(t-1975)*sx:.2f},{yb}) {{{t}}};')
o.append(f'\\draw[dashed] ({(bg-1975)*sx:.2f},{yb}) -- ({(bg-1975)*sx:.2f},0.45); \\node[above=1pt] at ({(bg-1975)*sx:.2f},0.45) {{bugün: {bg}}};')
SK=fig('\n'.join(o))
q('0005',tipId='yab-yil',tip='Doğum yılı ve yaş',z='zor',alt='Yaşam Çubukları',kaz='Doğum yıllarından yaşları bulup geçmişteki bir oran koşulundan yılı çözer.',kalip='hikâyeli',
 kart='K-YAB-05 · 1978, 1979, 2004, 2013; bugün 2026; oran 5',
 metin='Bir ailede anne ile babanın ve iki çocuğun doğum yılları, şekildeki çubukların başlangıcında yazılıdır; çubukların sağ ucu bugünün yılını gösterir. Aile albümünü hazırlayan çocuklar, geçmişte bir yılın yaşlarını merak etmektedir: anne ile babanın yaşları toplamının, iki çocuğun yaşları toplamının tam 5 katı olduğu yıl.\nBuna göre, o yıl bugünden kaç yıl öncedir?',
 dogru=v,yan=[(e[0],'Oranı 3 almış (3 katı).','dikkat'),(e[1],'Oranı 4 almış (4 katı).','dikkat'),(e[2],'Oranı 6 almış (6 katı).','dikkat'),(e[3],'Toplam azalışı (2t = 20) yıl sanmış.','dikkat')],
 istenen='Kaç yıl önce (yıl).',ip=['Bugünkü yaşları doğum yıllarından bul; aynı t yıl önce her iki toplamın kaç azaldığını yaz.'],bilgi=[YIL],sekil=SK,
 ad=[A('Bugünkü toplamlar','Doğum yıllarından yaşlar.','Ebeveynler: 48 + 47 = 95; çocuklar: 22 + 13 = 35'),A('t yıl önce','Her toplam 2t azalır.','95 − 2t = 5 · (35 − 2t)'),A('Denklem','Parantez açılır.','95 − 2t = 175 − 10t'),A('t','Bilinmeyen çözülür.','8t = 80, t = 10')],
 puf='Her iki toplam da 2t azalır.')

# ===== 06 orta · konuşma balonları =====
bab_ece=26; anne_fark=3; tp=63
ece=Fr(tp-(bab_ece-anne_fark),2); v=ece+bab_ece
e=[ece,bab_ece,ece+bab_ece-anne_fark,tp+bab_ece]
assert ece==20 and v==46 and e==[20,26,43,89] and len({v,*e})==5
o=[]
bl=['Ben doğduğumda babam 26 yaşındaydı.','Annem babamdan 3 yaş küçüktür.','Annemle benim yaşlarımızın toplamı bugün 63’tür.']
for i,t in enumerate(bl):
    y=-i*1.15
    o.append(f'\\node[draw,thick,rounded corners=8pt,fill=vurgu!10,text width=6.2cm,align=center,inner sep=6pt] at (0,{y}) {{{t}}};')
SK=fig('\n'.join(o))
q('0006',tipId='yab-ifade',tip='Konuşmalardan yaş bulma',z='orta',alt='Konuşma Balonları',kaz='Üç yaş ifadesini ortak bir bilinmeyen cinsinden yazıp toplam koşulundan babanın bugünkü yaşını bulur.',kalip='hikâyeli',
 kart='K-YAB-06 · 26, −3, toplam 63',
 metin='Ece, ailesinin yaşlarıyla ilgili bir okul ödevi hazırlarken şekildeki üç cümleyi yazmıştır; üç cümle de bugünün durumunu anlatmaktadır ve Ece’nin ailesi yalnızca anne, baba ve Ece’den oluşmaktadır. Ödevin sonunda, öğretmeni babanın bugünkü yaşını sormuştur.\nBuna göre, Ece’nin babası bugün kaç yaşındadır?',
 dogru=v,yan=[(e[0],'Ece’nin yaşını (20) babanın yaşı sanmış.','dikkat'),(e[1],'Ece doğduğunda babanın yaşını (26) bugünkü yaşı sanmış.','dikkat'),(e[2],'Annenin yaşını (43) babanın yaşı sanmış.','dikkat'),(e[3],'Toplam 63 ile 26’yı toplamış: 63 + 26.','dikkat')],
 istenen='Babanın bugünkü yaşı.',ip=['Ece’nin bugünkü yaşına göre babanın ve annenin yaşını yaz; toplam cümlesini kullan.'],bilgi=[IFD],sekil=SK,
 ad=[A('Baba ve anne','Ece e yaşında olsun.','Baba: e + 26; anne: e + 23'),A('Toplam','Anne ile Ece’nin toplamı 63.','(e + 23) + e = 63'),A('Ece','Denklem çözülür.','e = 20'),A('Baba','e + 26.','20 + 26 = 46')],
 puf='Önce Ece’nin yaşını bul.')

# ===== 07 orta · önce–sonra kutu modeli =====
ec=4; an=5*ec; assert (ec+4)*3==an+4
v=an; e=[ec,ec+4,3*ec,an-ec]
assert v==20 and e==[4,8,12,16] and len({v,*e})==5
w=0.5; o=[]
def grup(y,lab,u,e_,a_):
    s=[f'\\node[left] at (-0.1,{y}) {{Ece}}; \\node[left] at (-0.1,{y-0.85}) {{Anne}};']
    s.append(f'\\filldraw[fill=vurgu!40,draw=vurgu!80!black] (0,{y-0.28}) rectangle ({u},{y+0.28});')
    for j in range(a_): s.append(f'\\filldraw[fill=vurgu!{20 if j%2==0 else 30},draw=vurgu!80!black] ({j*u},{y-0.85-0.28}) rectangle ({(j+1)*u},{y-0.85+0.28});')
    return s
ud,us=0.35*2,0.35*4
o+=['\\node[anchor=west] at (0,0.75) {\\textbf{Bugün}};']+grup(0,'Bugün',1.0,1,5)
o+=['\\node[anchor=west] at (0,-1.75) {\\textbf{4 yıl sonra}};']+grup(-2.5,'4 yıl sonra',1.9,1,3)
SK=fig('\n'.join(o))
q('0007',tipId='yab-model',tip='Kutu modeli',z='orta',alt='Önce–Sonra Kutu Modeli',kaz='İki zamandaki kutu oranları ve yıl farkından çocuğun yaşını, sonra annenin yaşını bulur.',kalip='yeni nesil',
 kart='K-YAB-07 · bugün 1:5, 4 yıl sonra 1:3',
 metin='Bir anne ve kızının yaşları iki ayrı zamanda eş kutularla şekilde gösterilmiştir: üstte bugünkü, altta 4 yıl sonraki durum. Her zamanda kutular birbirinin aynıdır; üstteki ve alttaki kutuların gösterdiği yaşlar ise birbirinden farklıdır.\nBuna göre, annenin bugünkü yaşı kaçtır?',
 dogru=v,yan=[(e[0],'Kızın bugünkü yaşını (4) annenin yaşı sanmış.','dikkat'),(e[1],'4 yıl sonraki kız yaşını (8) annenin bugünkü yaşı sanmış.','dikkat'),(e[2],'Annenin yaşını bugünkü kızın yaşının 3 katı (12) almış.','dikkat'),(e[3],'Yaş farkını (16) annenin yaşı sanmış.','dikkat')],
 istenen='Annenin bugünkü yaşı.',ip=['Her iki zamandaki kutu değerlerini ayrı ayrı yaz ve iki kişinin 4 yıl içindeki değişimini karşılaştır.'],bilgi=[KUT],sekil=SK,
 ad=[A('Bugün ve 4 yıl sonra','Kız x; anne 5x. 4 yıl sonra kız x + 4, anne 5x + 4 = 3(x + 4).','5x + 4 = 3x + 12'),A('Kızın yaşı','x bulunur.','2x = 8, x = 4'),A('Annenin yaşı','5x.','5 × 4 = 20')],
 puf='Kızın yaşına x diyerek başla.')

# ===== 08 kolay · nokta grafiği =====
nk={10:3,11:2,12:2,13:1,14:2}; N=sum(nk.values()); S=sum(a*c for a,c in nk.items()); v=Fr(S,N)
e=[sum(nk)/5,max(nk),Fr(S,5),S]
assert N==10 and S==117 and v==Fr(117,10) and e==[12,14,Fr(117,5),117] and len({v,*e})==5
o=['\\draw[-{Stealth}] (0,0) -- (6.3,0) node[right] {yaş};']
for a in range(10,15): o.append(f'\\draw ({(a-9.5)*1.1:.2f},-0.07) -- ({(a-9.5)*1.1:.2f},0.07); \\node[below=2pt] at ({(a-9.5)*1.1:.2f},0) {{{a}}};')
for a,c in nk.items():
    for j in range(c): o.append(f'\\filldraw[fill=vurgu!50,draw=vurgu!80!black] ({(a-9.5)*1.1:.2f},{0.3+j*0.4:.2f}) circle (0.15);')
SK=fig('\n'.join(o))
q('0008',tipId='yab-grafik',tip='Grafik okuma ve yaş',z='kolay',alt='Nokta Grafiği',kaz='Nokta grafiğindeki her yaşın kişi sayısını kullanarak yaş ortalamasını hesaplar.',kalip='grafik',
 kart='K-YAB-08 · 3,2,2,1,2 kişi; ort. 11,7',
 metin='Bir yaz kampındaki çocukların yaşları, şekildeki nokta grafiğinde gösterilmiştir; her nokta bir çocuğu temsil eder ve kamptaki her çocuk grafikte bir kez gösterilmiştir. Kamp yönetimi, etkinlikleri yaş düzeyine uygun hazırlamak için çocukların yaş ortalamasını öğrenmek istemektedir.\nBuna göre, kamptaki çocukların yaş ortalaması kaçtır?',
 dogru=v,yan=[(e[0],'Grafikteki yaş değerlerinin (10, 11, 12, 13, 14) ortalamasını almış.','dikkat'),(e[1],'En büyük yaşı ortalama sanmış.','dikkat'),(e[2],'Toplam yaşı çocuk sayısına değil, yaş türü sayısına (5) bölmüş.','dikkat'),(e[3],'Toplam yaşı (117) ortalama sanmış.','dikkat')],
 istenen='Çocukların yaş ortalaması.',ip=['Her yaştaki nokta sayısını say; her yaşı kendi sayısıyla çarpıp toplamlarını bul.'],bilgi=[ORT],sekil=SK,
 ad=[A('Çocuk sayısı','Noktalar sayılır.','3 + 2 + 2 + 1 + 2 = 10'),A('Toplam yaş','Her yaş, nokta sayısıyla çarpılır.','30 + 22 + 24 + 13 + 28 = 117'),A('Ortalama','Toplam yaş ÷ çocuk sayısı.','117 ÷ 10 = 11,7')],
 puf='Her noktanın bir çocuk olduğunu unutma.')

# ===== 09 orta · tablo =====
tk=[('A takımı',8,30),('B takımı',12,25),('C takımı',5,32)]; Nt=sum(n for _,n,_ in tk); St=sum(n*a for _,n,a in tk); v=Fr(St,Nt)
e=[25,Fr(sum(a for *_,a in tk),3),30,32]
assert Nt==25 and St==700 and v==28 and e==[25,29,30,32] and len({v,*e})==5
SK=tablo_svg(['Takım','Oyuncu sayısı','Yaş ortalaması'],[[n,str(k),str(a)] for n,k,a in tk])
q('0009',tipId='yab-tablo',tip='Yaş ortalaması tablosu',z='orta',alt='Takım Ortalamaları',kaz='Takımların oyuncu sayısı ve ortalamalarından üç takımın birleşik yaş ortalamasını bulur.',kalip='tablo',
 kart='K-YAB-09 · 8·30, 12·25, 5·32',
 metin='Bir şirketler arası turnuvaya katılan üç takımın oyuncu sayıları ve yaş ortalamaları aşağıdaki tabloda verilmiştir. Hiçbir oyuncu iki takımda oynamamaktadır. Turnuva komitesi, bütün oyuncuların ortak yaş ortalamasını turnuva kitapçığına yazacaktır.\nBuna göre, üç takımın oyuncularının birlikte yaş ortalaması kaçtır?',
 dogru=v,yan=[(e[0],'En kalabalık takımın ortalamasını (25) tüm ortalama sanmış.','dikkat'),(e[1],'Üç ortalamanın aritmetik ortalamasını almış: (30 + 25 + 32) ÷ 3.','dikkat'),(e[2],'A takımının ortalamasını (30) tüm ortalama sanmış.','dikkat'),(e[3],'C takımının ortalamasını (32) tüm ortalama sanmış.','dikkat')],
 istenen='Tüm oyuncuların yaş ortalaması.',ip=['Her takımın oyuncularının yaşları toplamını, ortalama × oyuncu sayısı ile bul.'],bilgi=[ORT],sekil=SK,
 ad=[A('Takım toplamları','Ortalama × oyuncu sayısı.','8·30 = 240; 12·25 = 300; 5·32 = 160'),A('Genel toplam','Üç toplam toplanır.','240 + 300 + 160 = 700'),A('Ortalama','Toplam yaş ÷ 25 oyuncu.','700 ÷ 25 = 28')],
 puf='Ortalamalardan toplam yaşa geç.')

# ===== 10 zor · doğum yılı çizgisi, bugün verili =====
dd,aa,kk,bg=1958,1990,2016,2026
xs=[x for x in range(1,60) if (bg-dd)+x==3*((bg-kk)+x)]
assert xs==[19]; x=xs[0]
v=(bg-dd)+x
e=[bg-dd,(bg-kk)+x,x,(bg-aa)+x]
assert v==87 and e==[68,29,19,55] and len({v,*e})==5
o=[f'\\draw[-{{Stealth}}] (0,0) -- (8.4,0);']
sc=7.6/70
for yv in (1960,1980,2000,2020): o.append(f'\\draw ({(yv-1955)*sc:.2f},-0.07) -- ({(yv-1955)*sc:.2f},0.07); \\node[below=2pt] at ({(yv-1955)*sc:.2f},0) {{{yv}}};')
for nm,yv,hh in (('Dede',dd,0.6),('Anne',aa,1.2),('Kız',kk,0.6)):
    xx=(yv-1955)*sc; o.append(f'\\fill[vurgu!70!black] ({xx:.2f},0) circle (0.1); \\draw[dotted] ({xx:.2f},0) -- ({xx:.2f},{hh}); \\node[above,align=center] at ({xx:.2f},{hh}) {{{nm}\\\\doğum: {yv}}};')
xb=(bg-1955)*sc; o.append(f'\\draw[thick,red!70!black] ({xb:.2f},-0.5) -- ({xb:.2f},1.5); \\node[above,align=center,red!70!black] at ({xb:.2f},1.5) {{bugün\\\\{bg}}};')
SK=fig('\n'.join(o))
q('0010',tipId='yab-yil',tip='Doğum yılı ve yaş',z='zor',alt='Doğum Yılı Çizgisi',kaz='Doğum yıllarından bugünkü yaşları bulup ileride bir oran koşulunun gerçekleşeceği yılı çözer ve dedenin yaşını hesaplar.',kalip='hikâyeli',
 kart='K-YAB-10 · 1958, 1990, 2016; bugün 2026; dede = 3 × kız; sorulan dede yaşı',
 metin='Bir ailedeki dede, anne ve kızın doğum yılları ile bugünün yılı şekildeki zaman çizgisinde gösterilmiştir. Aile, ileride bir yıl, dedenin yaşının kızın yaşının tam 3 katı olacağını fark etmiş ve o yıl büyük bir aile yemeği yapmaya karar vermiştir. Bir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki fark olarak alınır.\nBuna göre, aile yemeği yapıldığı yılda dede kaç yaşındadır?',
 dogru=v,yan=[(e[0],'Dedenin bugünkü yaşını (68) yazmış.','dikkat'),(e[1],'Kızın yemekteki yaşını (29) dedenin yaşı sanmış.','dikkat'),(e[2],'Kaç yıl sonra olduğunu (19) dedenin yaşı sanmış.','dikkat'),(e[3],'Annenin yemekteki yaşını (55) dedenin yaşı sanmış.','dikkat')],
 istenen='Yemek yılında dedenin yaşı.',ip=['Bugünkü yaşlardan başlayıp x yıl sonra dede ve kızın yaşlarını yaz; verilen oranı denklem yap.'],bilgi=[YIL],sekil=SK,
 ad=[A('Bugünkü yaşlar','Bugün 2026.','Dede 68, anne 36, kız 10'),A('x yıl sonra','Dede = 3 × kız.','68 + x = 3(10 + x)'),A('x','Denklem çözülür.','2x = 38, x = 19'),A('Dedenin yaşı','Bugünkü yaşa x eklenir.','68 + 19 = 87')],
 puf='Yaşlar her yıl birlikte artar.')

bitir(P,'yassekb',UK)
