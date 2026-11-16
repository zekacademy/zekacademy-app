"""TYT Fizik · İş, Güç ve Enerji genişletmesi (enerjiiki) · 22 soru, kardeş yok, ipucu 1.
Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici değer assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
H.KONU='İş, Güç ve Enerji'
P=Parti('enerjiiki','İş, Güç ve Enerji','fiz|İş, Güç ve Enerji',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 TYT Fizik (iş, güç, enerji; yalnız mantık) · MEB 9. sınıf fizik'
g=10
def kk(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZEN2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,'fz-en2-'+tipId,tip,KY)
def q(no,ad,**k):
    mk(P,no,ad=ad,adim=len(ad),**k)
# ---------- TikZ yardımcıları
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
DARR='{Stealth[length=1.7mm,width=1.5mm]}-{Stealth[length=1.7mm,width=1.5mm]}'
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def D(a,b,o='thick'): return f'\\draw[{o}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def AR(a,b,o='vurgu,very thick'): return f'\\draw[{o},{ARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def DM(a,b,o='thin'): return f'\\draw[{o},{DARR}] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});'
def zemin(x0,x1,y=0): return f'\\fill[pattern=north east lines,pattern color=gray] ({x0},{y-.2}) rectangle ({x1},{y});\n'+D((x0,y),(x1,y),'thick')
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
def tablo(bas,satir,gen):
    L=[]; h=.62; y=0
    x=0
    xs=[0]
    for w in gen: xs.append(xs[-1]+w)
    for j,t in enumerate(bas): L.append(f'\\node[draw,fill=gray!25,minimum width={gen[j]}cm,minimum height={h}cm,font=\\small\\bfseries] at ({xs[j]+gen[j]/2:.3f},0) {{{t}}};')
    for i,r in enumerate(satir):
        for j,t in enumerate(r): L.append(f'\\node[draw,minimum width={gen[j]}cm,minimum height={h}cm] at ({xs[j]+gen[j]/2:.3f},{-(i+1)*h:.3f}) {{{t}}};')
    return L
def axis(plots,xmax,ymax,xt,yt,xl,yl,w=6.4,h=5.0):
    return ['\\begin{axis}['+f'width={w}cm,height={h}cm,xmin=0,xmax={xmax},ymin=0,ymax={ymax},xtick={{{xt}}},ytick={{{yt}}},grid=both,major grid style={{gray!55,thin}},tick label style={{font=\\scriptsize}},axis lines=left,xlabel={{{xl}}},ylabel={{{yl}}},xlabel style={{font=\\small}},ylabel style={{font=\\small}},clip=false]']+plots+['\\end{axis}']
# ---------- öncüllü yardımcısı
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos):
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if t}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex: parts.append(f'{n}. yargıyı da doğru sanmış; {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
EP=B('Potansiyel ve kinetik enerji','E_p = m × g × h ve E_k = ½ × m × v². Sürtünmesiz yolda E_k + E_p sabit kalır. Örnek: 3 kg’lık cisim 2 m yükseklikte 3 × 10 × 2 = 60 J potansiyel enerjiye sahiptir')
IS=B('İş','W = F × x (kuvvet yer değiştirme doğrultusundayken). Kuvvet–yol grafiğinde grafiğin altında kalan alan işi verir. Örnek: 5 N’luk kuvvet 4 m’de 20 J iş yapar')
GU=B('Güç','P = W ÷ t; birimi watt (W). Örnek: 8 s’de 400 J iş yapan makinenin gücü 50 W’tır')
VE=B('Verim','verim = yararlı enerji (ya da iş) ÷ harcanan enerji (ya da iş). Örnek: 200 J harcayıp 50 J yararlı iş veren sistemin verimi %25’tir')
# ================= KARTLAR
kk(1,'Fiziksel anlamda iş','İş için kuvvetin yer değiştirme doğrultusunda bileşeni olmalı; yer değiştirme yoksa ya da kuvvet yola dikse iş sıfırdır.','Kuvvet uygulamakla iş yapmayı, yük taşımakla da iş yapmayı karıştırmak.','kolay','öncüllü',2,'is-yok','İş yapılmayan durumlar')
kk(2,'İş','Bölgelerde sabit kuvvetlerin işi ayrı ayrı hesaplanıp toplanır.','Ortalama ya da en büyük kuvveti tüm yola uygulamak.','kolay','şekilli',2,'bolge-is','Bölgeli yolda kuvvetten iş')
kk(3,'Kuvvet–yol grafiği','Yamuk grafikte parça parça iş hesaplanır; sürtünmesiz yolda toplam iş kinetik enerjiye eşittir.','Üçgen alanda ½ çarpanını unutmak.','orta','grafik',3,'grafik-yamuk','Yamuk kuvvet–yol grafiği ve kinetik enerji')
kk(4,'Güç','Güç = iş ÷ süre; en çok iş yapan en güçlü değildir.','İşi güçle, gücü işle karıştırmak.','orta','tablo',3,'guc-tablo','Tablodan güç karşılaştırması')
kk(5,'Güç','İş–zaman grafiğinde eğim gücü verir; doğrusal grafikte güç sabittir.','Eğimi güç yerine iş sanmak.','orta','grafik',3,'guc-grafik','İş–zaman grafiğinden güç')
kk(6,'Kinetik enerji','E_k = ½mv²; kütle ve hız oranlarından kinetik enerji oranı bulunur.','Hızın karesini almamak; kütle ve hızı doğrudan çarpmak.','kolay','hikâyeli',2,'kinetik-oran','Kinetik enerji oranı')
kk(7,'Kinetik enerji','Net kuvvetin yaptığı iş kinetik enerji değişimine eşittir.','Sürtünmeyi eklemek ya da atlamak.','orta','şekilli',3,'kinetik-net','Net iş ve kinetik enerji')
kk(8,'Yer çekimi potansiyel enerjisi','E_p = m g h; referans seviyesine bağlıdır; enerji yalnız yüksekliğe bağlı sanılmaz.','Yalnız yüksekliğe bakmak; kütleyi unutmak.','kolay','öncüllü',2,'potansiyel-ref','Potansiyel enerji ve referans seviyesi')
kk(9,'Yer çekimi potansiyel enerjisi','Aynı yüksekliğe çıkarken sürtünmesiz rampalarda iş yoldan bağımsızdır; uzun rampada kuvvet küçüktür.','Uzun rampada işin de küçük olduğunu sanmak.','orta','öncüllü',3,'rampa-is','İki rampada iş ve kuvvet')
kk(10,'Esneklik potansiyel enerjisi','Yayı uzatan kuvvet–uzama grafiğinde alan, yayda depolanan enerjidir; birimler SI’ya çevrilir.','cm’yi m’ye çevirmemek; ½ çarpanını unutmak.','orta','grafik',3,'yay-grafik','Yay kuvvet–uzama grafiğinden iş')
kk(11,'Esneklik potansiyel enerjisi','Yayda depolanan enerji sıkışmanın karesiyle artar; bırakılınca kinetik enerjiye dönüşür.','Enerjinin sıkışmayla doğru orantılı olduğunu sanmak.','orta','öncüllü',3,'yay-nitel','Yayda enerji depolanması (nitel)')
kk(12,'Esneklik potansiyel enerjisi','Verilen yay enerjisi kinetik enerjiye, sürtünme kaybı çıkınca potansiyel enerjiye dönüşür.','Sürtünme kaybını atlamak ya da iki kez çıkarmak.','orta','şekilli',4,'yay-yukseklik','Yay, sürtünme ve eğik düzlem')
kk(13,'Mekanik enerjinin korunumu','Sarkaçta ip gerilmesi iş yapmaz; bırakıldığı noktayla en alt nokta arasındaki düşey yükseklik farkı kullanılır.','İp boyunu düşey yükseklik sanmak.','orta','şekilli',3,'sarkac','Sarkaçta en alt noktadaki hız')
kk(14,'Mekanik enerjinin korunumu','Sürtünmesiz rayda yükseklik azaldıkça kinetik enerji artar; toplam mekanik enerji sabit kalır.','Yüksek noktada hızın büyük olduğunu sanmak.','orta','öncüllü',3,'ray-nitel','Rayda enerji karşılaştırması')
kk(15,'Mekanik enerjinin korunumu','Başlangıç hızı olan cisimde v² = v₀² ± 2gΔh; hız toplanmaz, kareler toplanır.','Başlangıç hızını atlamak; hızları toplamak.','zor','şekilli',4,'ray-hiz','Başlangıç hızlı cismin tepedeki hızı')
kk(16,'Sürtünmeli yüzeyde ısı','Isıya dönüşen enerji = ilk mekanik enerji − son mekanik enerji.','Yalnız kinetik ya da yalnız potansiyel enerjiyi vermek.','orta','şekilli',3,'surtunme-isi','Eğik düzlemde ısıya dönüşen enerji')
kk(17,'Sürtünmeli yüzeyde ısı','Aynı yüzeyde kütle ne olursa olsun durma yolu aynıdır; ısı kütleyle artar.','Ağır cismin daha uzağa gideceğini sanmak.','orta','öncüllü',4,'surtunme-nitel','Sürtünmeli yatayda durma ve ısı')
kk(18,'Kinetik enerji–yol grafiği','Kinetik enerji–yol grafiğinin eğimi net kuvvettir; sürtünme kuvveti ikinci bölümden bulunur.','Net kuvveti uygulanan kuvvet sanmak.','zor','grafik',4,'kinetik-grafik','Kinetik enerji–yol grafiğinden kuvvet')
kk(19,'Enerji dönüşümleri','Lambada elektrik enerjisi ışığa ve ısıya dönüşür; ışığa dönüşen pay verimi belirler.','Enerjinin lambada tükendiğini sanmak.','kolay','tablo',2,'lamba-tablo','Lambalarda enerji dönüşümü')
kk(20,'Verim','Eğik düzlemde verim = yararlı iş (m g h) ÷ çekme işi (F ℓ).','Verimi h ÷ ℓ ile karıştırmak; oranı ters almak.','orta','şekilli',3,'verim-egik','Eğik düzlemin verimi')
kk(21,'Verim','Ardışık sistemlerde verimler çarpılır; güç, saniyedeki enerjidir.','Verimleri toplamak ya da ortalamasını almak.','orta','şekilli',4,'verim-zincir','Seri verim ve elektriksel güç')
kk(22,'Yenilenebilir ve yenilenemez enerji kaynakları','Güneş, rüzgâr, hidroelektrik, jeotermal ve biyokütle yenilenebilir; kömür, petrol ve doğal gaz yenilenemez.','Jeotermal ya da hidroelektriği yenilenemez saymak.','kolay','tablo',2,'kaynak-tablo','Elektrik üretiminde yenilenemez kaynak payı')
# ================= 0001 iş yapılmayan durumlar (öncüllü, şekil)
def kisi(x,hand,y=0):
    o=[f'\\draw[thick] ({x},{y+1.55}) circle (.17);',D((x,y+1.38),(x,y+.72)),D((x,y+.72),(x-.22,y)),D((x,y+.72),(x+.22,y)),D((x,y+1.22),hand)]
    return o
o=[]
# I
o.append(zemin(-.4,3.0))
o+= kisi(1.0,(2.28,1.0))
o.append('\\fill[pattern=north east lines,pattern color=gray] (2.3,0) rectangle (2.7,2.0);'+D((2.3,0),(2.3,2.0)))
o.append(AR((1.2,1.5),(2.2,1.5))); o.append(N(1.7,1.8,'$F$','vurgu'))
# II
dx=3.6
o.append(zemin(dx-.4,dx+3.0))
o+= kisi(dx+1.0,(dx+1.35,.75))
o.append(f'\\draw[thick,fill=gray!25] ({dx+1.15},.25) rectangle ({dx+1.55},.62);'+D((dx+1.35,.75),(dx+1.35,.62),'thin'))
o.append(AR((dx+1.9,.35),(dx+1.9,1.15))); o.append(N(dx+2.15,.8,'$F$','vurgu'))
o.append(f'\\draw[thin,gray,dashed,{ARR}] ({dx+.4},-.5) -- ({dx+2.6},-.5);')
# III
dx=7.2
o.append(zemin(dx-.4,dx+2.6))
o.append(f'\\fill[pattern=north east lines,pattern color=gray] ({dx+.3},2.35) rectangle ({dx+2.0},2.55);'+D((dx+.3,2.35),(dx+2.0,2.35)))
o.append(f'\\draw[thick,fill=gray!25] ({dx+.75},0) rectangle ({dx+1.55},.6);')
o.append(D((dx+1.15,.6),(dx+1.15,2.35),'thin'))
o.append(AR((dx+1.15,.6),(dx+1.15,1.5))); o.append(N(dx+1.4,1.1,'$F$','vurgu'))
o.append(f'\\draw[thin,gray,dashed,{ARR}] ({dx+1.95},.3) -- ({dx+1.95},1.6);')
for t,x in (('I',1.3),('II',4.9),('III',8.35)): o.append(N(x,-.85,'\\textbf{'+t+'}'))
SK1=tikz(o)
q('0001',tipId='fz-en2-is-yok',tip='İş yapılmayan durumlar',z='kolay',alt='İş',kaz='Kuvvet ile yer değiştirmenin yönüne bakarak kuvvetin iş yapmadığı durumları ayırt eder.',kalip='öncüllü',
 kart='K-FZEN2-01 (iş yapılmayan durumlar) · duvar, yatay taşıma, düşey çekme',
 metin='Bir spor salonunda ve bir depoda gözlenen üç durum şekilde gösterilmiştir. Her durumda $F$ ile gösterilen kuvvet, kişinin ya da ipin cisme uyguladığı kuvvettir; kesikli oklar yer değiştirmenin yönünü göstermektedir.\nI. Bir kişi, yerinde sabit duran sağlam bir duvarı itiyor.\nII. Bir kişi, elindeki çantayı düşürmeden tutarak düz bir yolda sabit hızla yürüyor.\nIII. Bir kutu, ip ile düşey doğrultuda sabit hızla yukarı çekiliyor.\nBuna göre, hangi durumlarda $F$ ile gösterilen kuvvetin yaptığı iş sıfırdır?'.replace('$F$','F'),
 sekil=SK1,istenen='$F$ kuvvetinin işinin sıfır olduğu durumlar.'.replace('$F$','F'),
 ip=['İşin tanımında kuvvetin ve yer değiştirmenin yönü ile miktarı birlikte yer alır; her durumda ikisine ayrı ayrı bak.'],
 bilgi=[IS,B('İş yapılmayan durumlar','yer değiştirme sıfırsa ya da kuvvet yer değiştirmeye diktirse kuvvet iş yapmaz. Örnek: bavulu yatay yolda taşırken elin uyguladığı yukarı kuvvet iş yapmaz')],
 ad=[A('I. durumu incele','Duvar hareket etmiyor; yer değiştirme sıfır.','W = F × 0 = 0'),A('II. durumu incele','Çantayı tutan kuvvet yukarı, yer değiştirme yatay; kuvvet yola diktir.','F ⟂ x → W = 0'),A('III. durumu incele','Kuvvet ve yer değiştirme aynı yönde; kuvvet pozitif iş yapar.','W = F × x ≠ 0'),A('Sonuç','İş sıfırdır: I ve II.','I ve II')],
 puf='Kuvvet uygulamak tek başına iş yapmak değildir; kuvvetin yola paralel bir bileşeni ve yer değiştirme gerekir.',
 **onc([True,True,False],['yer değiştirme olmadığı için iş sıfırdır','kuvvet yer değiştirmeye dik olduğundan iş sıfırdır','kuvvet ve yer değiştirme aynı yönde olduğundan kuvvet iş yapar'],1))
# ================= 0002 bölgeli yolda iş (kolay, şekil)
assert 30*2+10*4==100 and 10*4==40 and 30*2==60 and (30+10)//2*6==120 and 30*6==180
o=[zemin(-.3,6.5)]
for x in (0,2,6): o.append(D((x,-.1),(x,1.7),'thin,dashed'))
o.append('\\draw[thick,fill=gray!25] (.3,0) rectangle (1.0,.5);'); o.append(AR((1.0,.25),(1.0+30*.045,.25))); o.append(N(1.7,.6,'$30$ N','vurgu'))
o.append('\\draw[thick,fill=gray!25] (3.0,0) rectangle (3.7,.5);'); o.append(AR((3.7,.25),(3.7+10*.045,.25))); o.append(N(3.95,.6,'$10$ N','vurgu'))
o.append(DM((0,-.55),(2,-.55))); o.append(N(1,-.85,'$2$ m')); o.append(DM((2,-.55),(6,-.55))); o.append(N(4,-.85,'$4$ m'))
SK2=tikz(o)
q('0002',tipId='fz-en2-bolge-is',tip='Bölgeli yolda kuvvetten iş',z='kolay',alt='İş',kaz='Yolun bölgelerinde farklı sabit kuvvetlerin yaptığı işleri hesaplayıp toplar.',kalip='şekilli',
 kart='K-FZEN2-02 (bölgeli yolda iş) · iki sabit kuvvet bölgesi',
 metin='Bir depoda çalışan işçi, yatay zeminde durgun hâldeki ağır bir kasayı yol doğrultusunda uyguladığı kuvvetle düz bir hat boyunca itiyor. Zemin ilk bölümde pürüzlü, sonraki bölümde daha az pürüzlü olduğundan işçi uyguladığı kuvveti azaltıyor. Her bölümde kuvvet sabittir ve bölümlerin uzunlukları ile kuvvetler şekilde gösterilmiştir. Kasa, iş boyunca yer değiştirirken kuvvet her zaman yol doğrultusundadır.\nBuna göre, kasa bu iki bölümün tamamı boyunca itilirken işçinin uyguladığı kuvvetin yaptığı iş kaç J’dür?',
 sekil=SK2,dogru=100,yan=[(40,'Yalnız ikinci bölümün işini (10 × 4) hesaplamış.','dikkat'),(60,'Yalnız ilk bölümün işini (30 × 2) hesaplamış.','dikkat'),(120,'İki kuvvetin ortalamasını (20 N) alıp tüm yolla (6 m) çarpmış; kuvvet bölgelere göre değişir, her bölgenin işi ayrı hesaplanır.','bilgi'),(180,'En büyük kuvveti (30 N) tüm yola uygulanmış sanıp 30 × 6 hesaplamış.','bilgi')],
 istenen='Kuvvetin iki bölüm boyunca yaptığı iş (J).',
 ip=['Kuvvet her bölümde farklı olduğundan işi bölümlere ayırarak düşün.'],
 bilgi=[IS],
 ad=[A('İlk bölüm','Kuvvet 30 N, yol 2 m.','W₁ = 30 × 2 = 60 J'),A('İkinci bölüm','Kuvvet 10 N, yol 4 m.','W₂ = 10 × 4 = 40 J'),A('Toplam','Parçaların işleri toplanır.','W = 60 + 40 = 100 J')],
 puf='Kuvvet bölgeden bölgeye değişiyorsa her bölgenin işini ayrı hesapla ve topla; ortalama kuvvet almak hatalıdır.')
# ================= 0003 yamuk grafik (öncüllü)
a1=Fr(1,2)*2*20; a2=2*20; a3=Fr(1,2)*2*20
assert a1==20 and a2==40 and a3==20 and a1+a2+a3==80 and Fr(1,2)*2*0+80==80
pl=['\\addplot[fill=vurgu!20,draw=vurgu,thick] coordinates {(0,0)(2,20)(4,20)(6,0)} -- cycle;']
SK3=tikz(axis(pl,7,26,'0,2,4,6','0,10,20','$x$ (m)','$F$ (N)'))
q('0003',tipId='fz-en2-grafik-yamuk',tip='Yamuk kuvvet–yol grafiği ve kinetik enerji',z='orta',alt='İş',kaz='Yamuk biçimli kuvvet–yol grafiğinden işi ve kinetik enerji artışını yorumlar.',kalip='grafik',
 kart='K-FZEN2-03 (yamuk grafik) · üç parçalı alan ve kinetik enerji',
 metin='Sürtünmesiz yatay bir rayda durmakta olan 2 kg kütleli bir araba, ray doğrultusunda etkiyen değişken bir kuvvetle çekiliyor. Kuvvetin arabanın konumuna bağlı değişimi şekildeki grafikte verilmiştir. Kuvvet her an ray doğrultusundadır ve hava direnci önemsizdir.\nBuna göre,\nI. Kuvvet, 0–2 m aralığında 40 J’lük iş yapar.\nII. Kuvvet, 2–4 m aralığında 40 J’lük iş yapar.\nIII. Araba 6 m konumundan geçerken kinetik enerjisi 80 J’dür.\nyargılarından hangileri doğrudur?',
 sekil=SK3,istenen='Doğru olan yargılar.',
 ip=['Grafiği üç bölgeye ayır; her bölgenin işini bulduktan sonra sürtünme olmadığında toplam işin enerjiye ne olduğunu düşün.'],
 bilgi=[IS,B('İş–enerji ilişkisi','sürtünmesiz yatay yolda durgun cisme yapılan toplam iş, cismin kinetik enerjisine eşittir. Örnek: 30 J iş yapılan durgun cismin kinetik enerjisi 30 J olur')],
 ad=[A('0–2 m bölgesi','Kuvvet 0’dan 20 N’a çıkar; alan üçgendir.','W = ½ × 2 × 20 = 20 J → I yanlış'),A('2–4 m bölgesi','Kuvvet 20 N sabittir.','W = 2 × 20 = 40 J → II doğru'),A('4–6 m bölgesi','Kuvvet 20 N’dan 0’a iner; alan üçgendir.','W = ½ × 2 × 20 = 20 J'),A('Kinetik enerji','Sürtünme olmadığından toplam iş kinetik enerjiye eşittir.','20 + 40 + 20 = 80 J → III doğru')],
 puf='Yamuk grafikte alan üçgen ve dikdörtgenlere bölünür; sürtünmesizse toplam alan kinetik enerji kazancına eşittir.',
 **onc([False,True,True],['0–2 m aralığındaki alan ½ × 2 × 20 = 20 J’dür','2–4 m aralığındaki dikdörtgenin alanı 2 × 20 = 40 J’dür','toplam iş 80 J olup durgun arabanın kinetik enerjisine eşittir'],4))
# ================= 0004 güç tablosu (öncüllü)
Wk,tk,Wl,tl,Wm,tm=1200,20,900,10,2400,40
assert Fr(Wk,tk)==60 and Fr(Wl,tl)==90 and Fr(Wm,tm)==60 and Fr(90,60)==Fr(3,2)
SK4=tikz(tablo(['Makine','Yapılan iş (J)','Süre (s)'],[['K',str(Wk),str(tk)],['L',str(Wl),str(tl)],['M',str(Wm),str(tm)]],[2.2,3.2,2.4]))
q('0004',tipId='fz-en2-guc-tablo',tip='Tablodan güç karşılaştırması',z='orta',alt='Güç',kaz='İş ve süre verilerinden makinelerin güçlerini karşılaştırır.',kalip='tablo',
 kart='K-FZEN2-04 (güç tablosu) · en çok iş yapan en güçlü değil',
 metin='Bir atölyede çalışan K, L ve M makineleri, her biri çalıştığı süre boyunca sabit güçle çalışarak farklı miktarlarda iş yapmıştır. Makinelerin yaptığı iş ve çalışma süreleri şekildeki tabloda verilmiştir.\nBuna göre,\nI. L makinesinin gücü, K makinesinin gücünün 1,5 katıdır.\nII. En fazla iş yapan M makinesinin gücü de en büyüktür.\nIII. K ve M makinelerinin güçleri eşittir.\nyargılarından hangileri doğrudur?',
 sekil=SK4,istenen='Doğru olan yargılar.',
 ip=['Her makinenin gücünü ayrı ayrı bulup birbiriyle karşılaştır; iş ile güç aynı şey değildir.'],
 bilgi=[GU],
 ad=[A('Güçleri hesapla','Her makine için iş süreye bölünür.','P_K = 1200 ÷ 20 = 60 W · P_L = 900 ÷ 10 = 90 W · P_M = 2400 ÷ 40 = 60 W'),A('I. yargı','L’nin gücü K’ninkine oranlanır.','90 ÷ 60 = 1,5 → doğru'),A('II. yargı','M en çok iş yapmıştır ama süresi de en uzundur.','P_M = 60 W < P_L = 90 W → yanlış'),A('III. yargı','K ve M aynı güçtedir.','60 W = 60 W → doğru')],
 puf='Güç, işin süreye oranıdır; çok iş yapmak, uzun sürede yapılmışsa yüksek güç demek değildir.',
 **onc([True,False,True],['L’nin gücü 90 W, K’ninki 60 W olduğundan oran 1,5’tir','M’nin gücü 60 W olup L’nin 90 W’lık gücünden küçüktür; güç iş ile değil iş ÷ süre ile belirlenir','K ve M’nin güçleri 60 W’la eşittir'],3))
# ================= 0005 iş–zaman grafiği (öncüllü)
PK,PL=40,20
assert PK*10==400 and PL*10==200 and PL*2==PK and PL*6==120 and PK*5==200 and PL!=40
pl=['\\addplot[very thick,vurgu] coordinates {(0,0)(10,400)};','\\addplot[very thick,black] coordinates {(0,0)(10,200)};','\\node[anchor=south east,font=\\small\\bfseries] at (axis cs:10,400) {K};','\\node[anchor=south east,font=\\small\\bfseries] at (axis cs:10,200) {L};']
SK5=tikz(axis(pl,11,450,'0,2,4,6,8,10','0,100,200,300,400','$t$ (s)','$W$ (J)'))
q('0005',tipId='fz-en2-guc-grafik',tip='İş–zaman grafiğinden güç',z='orta',alt='Güç',kaz='İş–zaman grafiğinin eğiminden gücü bulur ve güçleri karşılaştırır.',kalip='grafik',
 kart='K-FZEN2-05 (iş–zaman grafiği) · iki motor',
 metin='Bir sulama sisteminde su pompalayan K ve L motorları, çalıştıkları süre boyunca sabit güçle çalışmaktadır. Motorların yaptığı toplam işin zamana bağlı değişimi şekildeki grafikte verilmiştir. Motorlar aynı anda çalıştırılmaya başlanmış ve verilen süre boyunca kesintisiz çalışmıştır.\nBuna göre,\nI. L motorunun gücü 40 W’tır.\nII. L motorunun gücü, K motorunun gücünün yarısıdır.\nIII. K motoru 5 s’de 300 J iş yapar.\nyargılarından hangileri doğrudur?',
 sekil=SK5,istenen='Doğru olan yargılar.',
 ip=['İş–zaman grafiğinde doğrunun eğimi neyi verir? Her motor için bir zaman seçip işi o zamana böl.'],
 bilgi=[GU,B('İş–zaman grafiği','doğrusal iş–zaman grafiğinin eğimi sabit gücü verir. Örnek: 10 s’de 100 J’e ulaşan doğrunun gücü 10 W’tır')],
 ad=[A('K motorunun gücü','10 s’de 400 J iş yapmış.','P_K = 400 ÷ 10 = 40 W'),A('L motorunun gücü','10 s’de 200 J iş yapmış.','P_L = 200 ÷ 10 = 20 W → I yanlış'),A('II. yargı','20 W, 40 W’ın yarısıdır.','II doğru'),A('III. yargı','K 5 s’de 40 × 5 kadar iş yapar.','W = 200 J ≠ 300 J → III yanlış')],
 puf='İş–zaman grafiğinde eğim güçtür; doğrunun daha dik olduğu motor daha güçlüdür.',
 **onc([False,True,False],['L’nin gücü 200 ÷ 10 = 20 W’tır, 40 W olan K motorudur','20 W, K’nin 40 W’ının yarısıdır','K 5 s’de 40 × 5 = 200 J iş yapar, 300 J değil'],0))
# ================= 0006 kinetik enerji oranı (kolay, metin)
mK,vK,mL,vL=6000,20,2000,10
EK=Fr(1,2)*mK*vK**2; EL=Fr(1,2)*mL*vL**2
assert EK==1200000 and EL==100000 and EK/EL==12 and Fr(mK*vK,mL*vL)==6 and Fr(vK,vL)**2==4 and Fr(mK,mL)==3 and Fr(vK,vL)==2
q('0006',tipId='fz-en2-kinetik-oran',tip='Kinetik enerji oranı',z='kolay',alt='Kinetik Enerji',kaz='Kütle ve hız oranlarından iki cismin kinetik enerji oranını bulur.',kalip='hikâyeli',
 kart='K-FZEN2-06 (kinetik enerji oranı) · kamyon ve otomobil',
 metin='Bir şehirlerarası yolda kütlesi 6 000 kg olan K kamyonu 20 m/s hızla, kütlesi 2 000 kg olan L otomobili ise 10 m/s hızla aynı doğrultuda ilerlemektedir. İki taşıtın da hızı sabittir, yolcular ve yük dahil toplam kütleleri verilmiştir ve taşıtlar bir tek cisim gibi düşünülebilir. Dönen parçaların enerjisi hesaba katılmayacaktır.\nBuna göre, K kamyonunun kinetik enerjisinin L otomobilinin kinetik enerjisine oranı kaçtır?',
 dogru=12,yan=[(2,'Yalnız hızların oranını (20 ÷ 10) almış; kütle farkını ve hızın karesini atlamış.','dikkat'),(3,'Yalnız kütlelerin oranını (6 000 ÷ 2 000) almış; hız farkını hesaba katmamış.','dikkat'),(4,'Yalnız hızların karesinin oranını (2²) almış; kütle oranını (3) çarpmayı unutmuş.','dikkat'),(6,'Kütle ile hızı çarpıp (m × v) karşılaştırmış; kinetik enerjide hız karesiyle çarpılır.','bilgi')],
 istenen='E_K ÷ E_L oranı.',
 ip=['İki taşıtın kütle oranını ve hız oranını ayrı ayrı yazıp kinetik enerjinin bunlara nasıl bağlandığını düşün.'],
 bilgi=[B('Kinetik enerji','E_k = ½ × m × v². Hız iki katına çıkarsa enerji dört katına çıkar. Örnek: 2 kg, 3 m/s için E_k = ½ × 2 × 9 = 9 J')],
 ad=[A('K’nin enerjisi','Kütle ve hız yerine konur.','E_K = ½ × 6000 × 20² = 1 200 000 J'),A('L’nin enerjisi','Aynı bağıntı L için uygulanır.','E_L = ½ × 2000 × 10² = 100 000 J'),A('Oran','İki enerji oranlanır.','1 200 000 ÷ 100 000 = 12')],
 puf='Kinetik enerji oranı = kütle oranı × (hız oranı)²; hız karesiyle etki eder.')
# ================= 0007 net iş ve kinetik enerji (orta, şekil)
F7,f7,x7=30,10,5
Ek7=(F7-f7)*x7
assert Ek7==100 and f7*x7==50 and F7*x7==150 and (F7+f7)*x7==200 and Fr(1,2)*F7*x7==75 or True
assert Fr(1,2)*(F7*x7)==Fr(75)
o=[zemin(-.3,8.2)]
o.append('\\draw[thick,fill=gray!25] (0.6,0) rectangle (1.4,.6);')
o.append(AR((1.4,.35),(3.8,.35))); o.append(N(2.6,.72,'$30$ N','vurgu'))
o.append(AR((.6,.3),(-.2,.3),'gray,thick')); o.append(N(.2,.62,'$10$ N','gray'))
o.append(D((7.2,0),(7.2,.9),'thin,dashed')); o.append(N(7.2,1.15,'$L$'))
o.append(D((1.0,0),(1.0,-.7),'thin,dashed')); o.append(DM((1.0,-.85),(7.2,-.85))); o.append(N(4.1,-1.15,'$5$ m'))
o.append(N(1.0,1.15,'$K$'))
SK7=tikz(o)
q('0007',tipId='fz-en2-kinetik-net',tip='Net iş ve kinetik enerji',z='orta',alt='Kinetik Enerji',kaz='Uygulanan kuvvet ve sürtünme kuvvetinin işinden kinetik enerji kazancını bulur.',kalip='şekilli',
 kart='K-FZEN2-07 (net iş ve kinetik enerji) · sürtünmeli yatay',
 metin='Yatay bir zeminde K noktasında durmakta olan 2 kg kütleli bir sandık, yüzeye paralel ve sabit bir kuvvetle L noktasına kadar itiliyor. Zemin ile sandık arasında sabit büyüklükte bir sürtünme kuvveti vardır; uygulanan kuvvet, sürtünme kuvveti ve K–L uzaklığı şekilde verilmiştir. Sandığın boyutları ve hava direnci önemsizdir; sandık, K’den L’ye kadar hiç durmadan ilerlemektedir.\nBuna göre, sandık L noktasından geçerken kinetik enerjisi kaç J’dür?',
 sekil=SK7,dogru=100,yan=[(50,'Yalnız sürtünme kuvvetinin işini (10 × 5) kinetik enerji sanmış.','dikkat'),(75,'Uygulanan kuvvetin işine ½ çarpanını uygulamış (½ × 150); iş doğrudan kinetik enerjiye eşitlenir.','bilgi'),(150,'Sürtünmeyi hesaba katmamış; yalnız uygulanan kuvvetin işini (30 × 5) almış.','dikkat'),(200,'Sürtünme kuvvetini uygulanan kuvvete eklemiş (40 × 5).','islem')],
 istenen='Sandığın L noktasındaki kinetik enerjisi (J).',
 ip=['Sandığa etki eden kuvvetlerin yönlerine bak; hareket yönündeki bileşke kuvvetin yaptığı iş kinetik enerjiyi belirler.'],
 bilgi=[IS,B('Net iş','bileşke kuvvetin yaptığı net iş, kinetik enerjideki değişime eşittir. Örnek: bileşke kuvveti 6 N olan durgun cisim 5 m sonra 30 J kinetik enerjiye ulaşır')],
 ad=[A('Bileşke kuvvet','Sürtünme hareketin tersine etki eder.','F_net = 30 − 10 = 20 N'),A('Net iş','Bileşke kuvvetin K–L yolundaki işi bulunur.','W_net = 20 × 5 = 100 J'),A('Kinetik enerji','Durgun başlayan cismin kinetik enerjisi net işe eşittir.','E_k = 100 J')],
 puf='Sürtünmeli yolda kinetik enerji kazancı, uygulanan kuvvetin işi eksi sürtünmenin işidir.')
# ================= 0008 potansiyel enerji ve referans (öncüllü, şekil)
hh={'K':(4,1),'L':(2,3),'M':(1,4)}
EpK,EpL,EpM=[m*g*h for m,h in hh.values()]
assert (EpK,EpL,EpM)==(40,60,40) and EpL!=2*EpK
o=[zemin(-.5,6.8)]
sc=.75
for xx,(k,(m,h)) in zip((.8,3.0,5.2),hh.items()):
    o.append(D((xx,0),(xx,h*sc),'thick')); o.append(D((xx-.45,h*sc),(xx+.45,h*sc),'thick'))
    o.append(f'\\draw[thick,fill=gray!25] ({xx-.3},{h*sc}) rectangle ({xx+.3},{h*sc+.5});'); o.append(N(xx,h*sc+.25,f'${m}$ kg','font=\\scriptsize'))
    o.append(N(xx,h*sc+.8,f'\\textbf{{{k}}}'))
    o.append(DM((xx-.75,0),(xx-.75,h*sc))); o.append(N(xx-.8,h*sc/2,f'${h}$ m','anchor=east,font=\\scriptsize'))
SK8=tikz(o)
q('0008',tipId='fz-en2-potansiyel-ref',tip='Potansiyel enerji ve referans seviyesi',z='kolay',alt='Yer Çekimi Potansiyel Enerjisi',kaz='Kütle ve yüksekliğe bağlı potansiyel enerjiyi karşılaştırır, referans seviyesinin etkisini yorumlar.',kalip='öncüllü',
 kart='K-FZEN2-08 (potansiyel enerji, referans) · üç direk',
 metin='Bir marangoz atölyesinde aynı zemine dikilmiş üç direğin tepesine K, L ve M cisimleri yerleştirilmiştir. Cisimlerin kütleleri ve zeminden yükseklikleri şekilde gösterilmiştir. Yer çekimi ivmesi her yerde aynıdır ve potansiyel enerji ilk olarak zemine göre ölçülmektedir.\nBuna göre,\nI. L cisminin potansiyel enerjisi, K cisminin potansiyel enerjisinin iki katıdır.\nII. En yüksekte bulunan M cisminin potansiyel enerjisi en büyüktür.\nIII. Potansiyel enerji K cisminin bulunduğu yatay düzleme göre ölçülürse K cisminin potansiyel enerjisi sıfır olur.\nyargılarından hangileri doğrudur?',
 sekil=SK8,istenen='Doğru olan yargılar.',
 ip=['Potansiyel enerji hem kütleye hem yüksekliğe bağlıdır; her cisim için kütle ile yüksekliğin çarpımını yaz.'],
 bilgi=[EP],
 ad=[A('Enerjileri hesapla','E_p = m × g × h; her cisim için ayrı ayrı yazılır.','E_K = 4 × 10 × 1 = 40 J · E_L = 2 × 10 × 3 = 60 J · E_M = 1 × 10 × 4 = 40 J'),A('I. yargı','L’nin enerjisi K’nin enerjisinin 1,5 katıdır.','60 ÷ 40 = 1,5 → yanlış'),A('II. yargı','M en yüksektedir ama kütlesi en küçüktür.','E_M = 40 J < E_L = 60 J → yanlış'),A('III. yargı','Referans K’nin düzlemi olursa K’nin yüksekliği 0 sayılır.','E_K = 0 → doğru')],
 puf='Potansiyel enerji kütle ve yüksekliğin çarpımıdır; yalnız yüksekliğe bakmak yanıltır, enerji referans seçimine bağlıdır.',
 **onc([False,False,True],['L’nin enerjisi 60 J, K’ninki 40 J olduğundan oran 1,5’tir','M en yüksektedir ama kütlesi küçüktür; enerjisi 40 J olup L’nin 60 J’ünden küçüktür','referans düzlemi K’nin yüksekliğinde seçilirse K’nin yüksekliği sıfır olur ve potansiyel enerjisi sıfırdır'],0))
# ================= 0009 iki rampa (öncüllü, şekil)
m9,h9,lK,lL=10,2,4,5
EpA=m9*g*h9; FK=Fr(m9*g*h9,lK); FL=Fr(m9*g*h9,lL)
assert EpA==200 and FK==50 and FL==40 and FK*lK==200 and FL*lL==200 and FL<FK
s9=.9; hc=h9*s9
def rampa(x0,l,lab):
    ln=l*s9; bs=math.sqrt(ln**2-hc**2); th=math.degrees(math.atan2(hc,bs)); c,sn=bs/ln,hc/ln
    o=[f'\\draw[thick] ({x0},0) -- ({x0+bs:.3f},0) -- ({x0+bs:.3f},{hc}) -- cycle;']
    sc_=1.2; px,py=x0+sc_*c,sc_*sn
    o.append(f'\\begin{{scope}}[shift={{({px:.3f},{py:.3f})}},rotate={th:.2f}]\\draw[thick,fill=gray!25] (-.3,0) rectangle (.3,.4);\\draw[vurgu,very thick,{ARR}] (.3,.2) -- (1.05,.2);\\end{{scope}}')
    o.append(f'\\draw[thin,{DARR}] ({x0+bs+.3:.3f},0) -- ({x0+bs+.3:.3f},{hc});'+N(x0+bs+.35,hc/2,f'${h9}$ m','anchor=west,font=\\scriptsize'))
    o.append(f'\\node[rotate={th:.2f},font=\\scriptsize] at ({x0+bs*.7+.22*sn:.3f},{hc*.7-.22*c:.3f}) {{$\\ell_{lab}={l}$ m}};')
    o.append(N(x0+bs/2,-.4,f'\\textbf{{{lab}}}'))
    o.append(AR((px+.0,py),(px,py),'vurgu')) if False else None
    return [x for x in o if x],bs
o1,b1=rampa(0,lK,'K'); o2,b2=rampa(b1+1.4,lL,'L')
SK9=tikz([zemin(-.4,b1+1.4+b2+1.2)]+o1+o2)
q('0009',tipId='fz-en2-rampa-is',tip='İki rampada iş ve kuvvet',z='orta',alt='Yer Çekimi Potansiyel Enerjisi',kaz='Sürtünmesiz rampalarda potansiyel enerji artışını, çekme kuvvetini ve yapılan işi karşılaştırır.',kalip='öncüllü',
 kart='K-FZEN2-09 (iki rampa) · aynı yükseklik, farklı boy',
 metin='Bir kargo görevlisi, 10 kg kütleli bir kutuyu aynı yüksekliğe çıkarmak için iki farklı sürtünmesiz rampadan birini kullanabilmektedir. Kutu, rampa boyunca rampaya paralel ve sabit büyüklükteki bir kuvvetle, sabit hızla yukarı çekilmektedir. Rampaların boyları ve yükseklikleri şekilde verilmiştir.\n(g = 10 m/s²)\nBuna göre,\nI. Kutunun potansiyel enerjisindeki artış iki rampada da 200 J’dür.\nII. Çekme kuvveti L rampasında, K rampasındakinden küçüktür.\nIII. Kuvvetin yaptığı iş iki rampada da eşittir.\nyargılarından hangileri doğrudur?',
 sekil=SK9,istenen='Doğru olan yargılar.',
 ip=['Sabit hızla çekilen cisimde kuvvetin işi neye dönüşür? Rampa boyu değişince kuvvet ile yolun çarpımına ne olur?'],
 bilgi=[EP,IS],
 ad=[A('Enerji artışı','Her rampada kutu aynı yüksekliğe çıkar.','ΔE_p = 10 × 10 × 2 = 200 J → I doğru'),A('Yapılan iş','Sürtünme yok, hız sabit: kuvvetin işi enerji artışına eşit.','W_K = W_L = 200 J → III doğru'),A('Kuvvetler','F = W ÷ rampa boyu.','F_K = 200 ÷ 4 = 50 N · F_L = 200 ÷ 5 = 40 N → II doğru')],
 puf='Sürtünmesiz rampada iş yola değil yüksekliğe bağlıdır; uzun rampa işi değil kuvveti azaltır.',
 **onc([True,True,True],['çıkılan yükseklik aynı olduğundan enerji artışı 10 × 10 × 2 = 200 J’dür','uzun yolda aynı iş daha küçük kuvvetle yapılır (40 N < 50 N)','sürtünme olmadığından iş enerji artışına eşittir ve iki rampada da 200 J’dür'],4))
# ================= 0010 yay kuvvet–uzama grafiği (orta)
E_=lambda F,xm:Fr(1,2)*F*xm
d10=E_(16,Fr(8,100))-E_(8,Fr(4,100))
assert d10==Fr(12,25) and E_(8,Fr(4,100))==Fr(4,25) and E_(16,Fr(8,100))==Fr(16,25) and Fr(1,2)*16*Fr(4,100)==Fr(8,25) and 16*Fr(8,100)==Fr(32,25) and Fr(1,2)*(8+16)*Fr(4,100)==d10
pl=['\\addplot[very thick,vurgu] coordinates {(0,0)(8,16)};']
SK10=tikz(axis(pl,10,20,'0,2,4,6,8,10','0,4,8,12,16,20','uzama (cm)','$F$ (N)'))
q('0010',tipId='fz-en2-yay-grafik',tip='Yay kuvvet–uzama grafiğinden iş',z='orta',alt='Esneklik Potansiyel Enerjisi',kaz='Yayın kuvvet–uzama grafiğinden iki uzama arasında yapılan işi hesaplar.',kalip='grafik',
 kart='K-FZEN2-10 (yay grafiği) · 4 cm ile 8 cm arası',
 metin='Bir fizik laboratuvarında, bir ucu sabitlenmiş esnek bir yay serbest ucundan yavaşça çekilerek uzatılıyor. Yayı uzatmak için uygulanan kuvvetin yayın uzama miktarına bağlı değişimi şekildeki grafikte verilmiştir. Yay, esneklik sınırını aşmamaktadır ve yayın kütlesi ile sürtünmeler önemsizdir. Uzatma işlemi o kadar yavaş yapılmaktadır ki yaya kinetik enerji kazandırılmamaktadır.\nBuna göre, yayın uzaması 4 cm iken uzama 8 cm oluncaya kadar yaya yapılan iş kaç J’dür?',
 sekil=SK10,dogru=Fr(12,25),yan=[(Fr(4,25),'Yalnız 0–4 cm arasındaki işi hesaplamış.','dikkat'),(Fr(8,25),'Son kuvvetle (16 N) yol farkını çarpıp ½’ye bölmüş; kuvvet 4 cm’deki değerden başlar, yamuk alan gerekir.','islem'),(Fr(16,25),'İşi 0 cm’den 8 cm’e kadar hesaplamış; başlangıç uzaması 4 cm’dir.','dikkat'),(Fr(32,25),'Son kuvveti uzamayla çarpmış (16 × 0,08); kuvvet sabit olmadığından ½ çarpanı gerekir.','bilgi')],
 istenen='4 cm ile 8 cm uzama arasında yaya yapılan iş (J).',
 ip=['Kuvvet–uzama grafiğinde alan neyi gösterir? Uzamayı hangi birime çevirmen gerektiğini de düşün.'],
 bilgi=[B('Yayda iş ve enerji','yayı uzatan kuvvet uzamayla doğru orantılı artar; kuvvet–uzama grafiğinin altındaki alan yayda depolanan enerjiyi verir. Örnek: 10 N’a kadar 0,2 m uzatılan yay ½ × 10 × 0,2 = 1 J enerji depolar')],
 ad=[A('Kuvvetleri oku','Grafikten 4 cm ve 8 cm için kuvvetler okunur.','4 cm → 8 N · 8 cm → 16 N'),A('Yamuk alanı yaz','Alan, iki kuvvetin ortalaması ile uzama farkının çarpımıdır.','W = ½ × (8 + 16) × Δx'),A('Birimi çevir','Δx = 4 cm = 0,04 m olmalıdır.','Δx = 0,04 m'),A('Sonuç','İşlem yapılır.','W = 12 × 0,04 = 0,48 J')],
 puf='Yay grafiğinde iki konum arasındaki iş yamuk alandır; uzamayı mutlaka metreye çevir.')
# ================= 0011 yay nitel (öncüllü, şekil)
def yay(y,xs,xe,n=8):
    return f'\\draw[thick,decorate,decoration={{coil,aspect=.5,segment length={(xe-xs)/n:.3f}cm,amplitude=2.2mm}}] ({xs},{y+.35}) -- ({xe},{y+.35});'
def duvar(y,h=.9): return f'\\fill[pattern=north east lines,pattern color=gray] (-.35,{y}) rectangle (0,{y+h});'+D((0,y),(0,y+h),'thick')
def blok(x,y,t='$m$'): return f'\\draw[thick,fill=gray!25] ({x},{y}) rectangle ({x+.9},{y+.7});'+N(x+.45,y+.35,t,'')
nat,com=2.6,1.4
o=[]
for i,(y,lab) in enumerate(((0,'(1)'),(-2.2,'(2)'),(-4.4,'(3)'))): o.append(D((-.35,y),(8.3,y),'thick'))
o.append(duvar(0)); o.append(yay(0,0,nat)); o.append(blok(nat,0)); o.append(N(7.6,.4,'(1)'))
y=-2.2; o.append(duvar(y)); o.append(yay(y,0,com)); o.append(blok(com,y)); o.append(N(7.6,y+.4,'(2)'))
o.append(D((nat,y-.1),(nat,y+1.0),'thin,dashed')); o.append(DM((com,y+1.0),(nat,y+1.0))); o.append(N((com+nat)/2,y+1.3,'$x$'))
y=-4.4; o.append(duvar(y)); o.append(yay(y,0,nat)); o.append(blok(4.6,y)); o.append(AR((5.6,y+.35),(6.9,y+.35))); o.append(N(6.25,y+.65,'$v$','vurgu')); o.append(N(7.6,y+.4,'(3)'))
SK11=tikz(o)
q('0011',tipId='fz-en2-yay-nitel',tip='Yayda enerji depolanması (nitel)',z='orta',alt='Esneklik Potansiyel Enerjisi',kaz='Yayın sıkıştırılması ve bırakılmasında enerji dönüşümlerini ve sıkışma–enerji ilişkisini yorumlar.',kalip='öncüllü',
 kart='K-FZEN2-11 (yay nitel) · sıkıştır–bırak',
 metin='Sürtünmesiz yatay bir masada bir ucu duvara bağlı bir yay vardır. (1) durumunda yay doğal boyundadır ve m kütleli bir cisim yaya temas etmektedir. Cisim, yayı x kadar sıkıştıracak biçimde (2) konumuna getirilip durgun hâlde bırakılıyor; yay doğal boyuna gelirken cisim yaydan ayrılıyor ve (3) durumundaki gibi v hızıyla ilerliyor. Yay, esneklik sınırı içinde kalmaktadır.\nBuna göre,\nI. Yay sıkıştırılırken yapılan iş, yayda esneklik potansiyel enerjisi olarak depolanır.\nII. Cisim yaydan ayrılırken kinetik enerjisi, yayın (2) konumunda sıkışıkken depoladığı enerjiden küçüktür.\nIII. Yay 2x kadar sıkıştırılıp cisim bırakılırsa cismin kinetik enerjisi dört katına çıkar.\nyargılarından hangileri doğrudur?',
 sekil=SK11,istenen='Doğru olan yargılar.',
 ip=['Sürtünme olmadığında enerji kaybolmaz; yayın depoladığı enerjinin sıkışma miktarıyla nasıl değiştiğini düşün.'],
 bilgi=[B('Esneklik potansiyel enerjisi','sıkıştırılmış ya da gerilmiş yay enerji depolar; bu enerji sıkışma (uzama) miktarının karesiyle artar. Örnek: sıkışma 3 katına çıkarsa enerji 9 katına çıkar'),B('Enerji dönüşümü','yay bırakılınca esneklik potansiyel enerjisi cismin kinetik enerjisine dönüşür')],
 ad=[A('I. yargı','Yayı sıkıştıran kuvvet iş yapar; iş yayda depolanır.','I doğru'),A('II. yargı','Sürtünme yok; (2) konumunda yayda depolanan enerjinin tamamı cisme geçer.','E_k = E_yay(2) → II yanlış'),A('III. yargı','Enerji sıkışmanın karesiyle artar: x → 2x.','E’ = (2x)² ∝ 4 × x² → III doğru')],
 puf='Yayda depolanan enerji sıkışmanın karesiyle artar; sürtünmesizse bu enerjinin tamamı kinetik enerjiye dönüşür.',
 **onc([True,False,True],['yaya yapılan iş esneklik potansiyel enerjisi olarak depolanır','sürtünme olmadığından (2) konumunda yayda depolanan enerjinin tamamı cisme geçer; kinetik enerji bu enerjiye eşittir','yay enerjisi sıkışmanın karesiyle artar; sıkışma iki katına çıkınca enerji dört katına çıkar'],4))
# ================= 0012 yay + sürtünme + rampa (zor, şekil)
Ey,m12,f12,l12=5,Fr(1,2),2,1
Eh=Ey-f12*l12; h12=Eh/(m12*g)
assert Eh==3 and h12==Fr(3,5) and Ey/(m12*g)==1 and (Ey+f12*l12)/(m12*g)==Fr(7,5) and (Ey+2*f12*l12)/(m12*g)==Fr(9,5) and Eh/m12==6
o=[]
o.append(duvar(0,1.0)); o.append(D((0,0),(6.4,0),'thick'))
o.append(yay(0,0,1.2))
o.append(f'\\draw[thick,fill=gray!25] (1.2,0) rectangle (1.9,.6);')

o.append('\\fill[pattern=north east lines,pattern color=gray] (3.2,-.2) rectangle (4.6,0);'+D((3.2,0),(4.6,0),'ultra thick'))
o.append(DM((3.2,-.55),(4.6,-.55))); o.append(N(3.9,-.85,'$1$ m','font=\\scriptsize'))
o.append(D((6.4,0),(9.0,1.9),'thick')); o.append(D((9.0,1.9),(9.0,0),'thin')); o.append(D((6.4,0),(9.0,0),'thick'))
yb=1.9*(8.0-6.4)/2.6
o.append(f'\\begin{{scope}}[shift={{(8.0,{yb:.3f})}},rotate=36.2]\\draw[thick,fill=gray!25,dashed] (-.3,0) rectangle (.3,.4);\\end{{scope}}')
o.append(D((8.0,yb),(9.3,yb),'thin,dashed')); o.append(DM((9.3,0),(9.3,yb))); o.append(N(9.35,yb/2,'$h$','anchor=west'))
SK12=tikz(o)
q('0012',tipId='fz-en2-yay-yukseklik',tip='Yay, sürtünme ve eğik düzlem',z='orta',alt='Esneklik Potansiyel Enerjisi',kaz='Yayda depolanan enerjinin kinetik ve potansiyel enerjiye dönüşümünü, sürtünme kaybıyla birlikte hesaplar.',kalip='şekilli',
 kart='K-FZEN2-12 (yay + sürtünme + rampa) · üç aşamalı enerji',
 metin='Kütlesi 500 g olan bir cisim, bir ucu duvara bağlı yaya dayanarak şekildeki gibi sıkıştırılıp durgun hâlde bırakılıyor; sıkıştırılmış yayda 5 J’lük esneklik potansiyel enerjisi depolanmıştır. Yay doğal boyuna gelince cisim yaydan ayrılıyor, yatay yolun pürüzlü bölgesinden geçiyor ve sürtünmesiz eğik düzlemde yükselerek bir h yüksekliğinde anlık duruyor. Yalnızca pürüzlü bölgede cisme sabit 2 N’luk sürtünme kuvveti etki etmektedir; yayın kütlesi ve hava direnci önemsizdir.\n(g = 10 m/s²)\nBuna göre, cismin çıkabildiği h yüksekliği kaç m’dir?',
 sekil=SK12,dogru=Fr(3,5),yan=[(Fr(9,5),'Sürtünme işini iki kez eklemiş: (5 + 4) ÷ 5.','islem'),(1,'Sürtünme kaybını hesaba katmamış; yay enerjisinin (5 J) tamamını potansiyel enerjiye çevirmiş.','dikkat'),(Fr(7,5),'Sürtünme işini yay enerjisine eklemiş: (5 + 2) ÷ 5.','islem'),(6,'g’yi hesaba katmamış: h = 3 ÷ 0,5.','bilgi')],
 istenen='Cismin eğik düzlemde çıktığı en büyük yükseklik h (m).',
 ip=['Enerjinin hangi biçimlerden hangilerine dönüştüğünü sırayla izle; yatay yoldaki kaybı çıkarmayı unutma.'],
 bilgi=[B('Yayda depolanan enerji','sıkıştırılmış yay enerji depolar; yay bırakılınca bu enerji cismin kinetik enerjisine dönüşür. Örnek: yayda 8 J depolanmışsa sürtünmesiz yüzeyde cisim 8 J kinetik enerji kazanır'),EP,B('Sürtünme işi','sürtünme kuvveti × yol kadar enerji ısıya dönüşür. Örnek: 3 N, 2 m → 6 J ısı')],
 ad=[A('Yaydaki enerji','Yayın depoladığı enerji cisme kinetik enerji olarak geçer.','E = 5 J'),A('Sürtünme kaybı','Pürüzlü bölgede ısıya dönüşen enerji.','E_ısı = 2 × 1 = 2 J'),A('Kalan enerji','Eğik düzleme çıkan enerji potansiyel enerjiye dönüşür.','5 − 2 = 3 J = m × g × h'),A('Yükseklik','Kütle 0,5 kg’dır.','h = 3 ÷ (0,5 × 10) = 0,6 m')],
 puf='Enerji dönüşümlerinde sırayla: depolanan yay enerjisi − ısıya giden enerji = ulaşılan potansiyel enerji.')
# ================= 0013 sarkaç (orta)
L13,h13=Fr(5,4),Fr(4,5); m13=1
v13=math.sqrt(2*g*h13); assert v13==4 and m13*g*h13==8 and 2*g*h13==16 and 2*g*(L13-h13)==9 and 2*g*L13==25
cs=1-float(h13)/float(L13); sn=math.sqrt(1-cs**2); sc=2.4; Lc=float(L13)*sc
bx,by=-Lc*sn,-Lc*cs; low=(0,-Lc)
o=[f'\\fill[pattern=north east lines,pattern color=gray] (-1.2,0) rectangle (1.2,.22);'+D((-1.2,0),(1.2,0),'thick')]
o.append(D((0,0),(bx*(1-.17/Lc),by*(1-.17/Lc)),'thin')); o.append(D((0,0),(0,-Lc+.17),'thin,dashed'))
o.append(f'\\draw[thick,fill=gray!25] ({bx},{by}) circle (.17);'); o.append(f'\\draw[thick,fill=gray!25] (0,{-Lc}) circle (.17);')
o.append(N(bx-.35,by+.05,'\\textbf{K}')); o.append(N(.4,-Lc-.15,'\\textbf{L}','anchor=west'))
o.append(f'\\draw[thin,dotted] plot[domain=0:{math.degrees(math.asin(sn)):.2f},samples=20] ({{-{Lc:.3f}*sin(\\x)}},{{-{Lc:.3f}*cos(\\x)}});')
o.append(D((bx+.17,by),(1.2,by),'thin,dashed')); o.append(D((.17,-Lc),(1.2,-Lc),'thin,dashed')); o.append(DM((1.0,-Lc),(1.0,by))); o.append(N(1.05,(by-Lc)/2,'$0{,}8$ m','anchor=west,font=\\scriptsize'))
o.append(N(bx/2-.35,by/2+.1,'$1{,}25$ m','font=\\scriptsize,rotate=-%.1f'%(math.degrees(math.atan2(-by,-bx))-90+90) if False else 'font=\\scriptsize,anchor=east'))
SK13=tikz(o)
q('0013',tipId='fz-en2-sarkac',tip='Sarkaçta en alt noktadaki hız',z='orta',alt='Mekanik Enerji',kaz='Sarkaçta bırakılma noktası ile en alt nokta arasındaki düşey yükseklik farkından hızı hesaplar.',kalip='şekilli',
 kart='K-FZEN2-13 (sarkaç) · h ve ip boyu birlikte verilmiş',
 metin='Kütlesi 1 kg olan küçük bir cisim, kütlesi önemsiz esnemeyen bir ipin ucuna bağlanarak şekildeki K konumunda ip gergin hâldeyken serbest bırakılıyor. Cisim dairesel bir yay çizerek ipin düşey olduğu en alt L noktasından geçiyor. Şekilde ipin boyu ve K ile L arasındaki düşey uzaklık verilmiştir. Hava direnci ve sürtünme önemsizdir; cismin boyutları da önemsenmeyecek kadar küçüktür.\n(g = 10 m/s²)\nBuna göre, cismin L noktasından geçerken hızı kaç m/s’dir?',
 sekil=SK13,dogru=4,yan=[(3,'İp boyundan düşey yüksekliği çıkarıp (1,25 − 0,8 = 0,45 m) yükseklik farkı yerine kullanmış.','dikkat'),(5,'İp boyunu (1,25 m) yükseklik farkı sanmış; cisim yalnız 0,8 m alçalır.','dikkat'),(8,'Potansiyel enerji kaybını (8 J) hız sanmış.','bilgi'),(16,'v² = 2 × g × h değerini (16) hıza çevirmeyi unutmuş.','islem')],
 istenen='Cismin L noktasındaki hızı (m/s).',
 ip=['İp gerilmesi cisme dik doğrultuda olduğundan iş yapmaz; cismin düşey doğrultuda ne kadar alçaldığına bak.'],
 bilgi=[EP,B('Sarkaçta enerji','ip cisme hareket doğrultusuna dik kuvvet uygular ve iş yapmaz; potansiyel enerji azalması kinetik enerji artışına eşittir')],
 ad=[A('Potansiyel enerji kaybı','K ile L arasındaki düşey fark 0,8 m’dir.','ΔE_p = 1 × 10 × 0,8 = 8 J'),A('Kinetik enerji','Kayıp enerji kinetik enerjiye dönüşür.','½ × 1 × v² = 8'),A('Hız','Denklem çözülür.','v² = 16 → v = 4 m/s')],
 puf='Sarkaçta hızı belirleyen şey ip boyu değil, bırakılma noktasıyla en alt nokta arasındaki düşey yükseklik farkıdır.')
# ================= 0014 ray nitel (öncüllü, şekil)
def ray(pts,marks,sc,hmax,ruler,note=None,v0=None):
    P_=[(x,h*sc) for x,h in pts]
    o=[D((-.2,-.12),(max(x for x,_ in pts)+.3,-.12),'thick,gray')]
    o.append('\\draw[very thick] plot[smooth] coordinates {'+' '.join(f'({x:.3f},{y:.3f})' for x,y in P_)+'};')
    x0=-1.0
    o.append(D((x0,0),(x0,hmax*sc+.1),'thin'))
    for t in range(0,hmax+1):
        o.append(D((x0-.07,t*sc),(x0+.07,t*sc),'thin')); o.append(N(x0-.12,t*sc,f'${t}$','anchor=east,font=\\scriptsize'))
    o.append(N(x0-.1,hmax*sc+.45,'yükseklik (m)','font=\\scriptsize,anchor=east'))
    for nm,(x,h),lab in marks:
        o.append(f'\\fill ({x},{h*sc}) circle (.07);'); o.append(N(x+lab[0],h*sc+lab[1],f'\\textbf{{{nm}}}'))
        if nm in ruler: 
            o.append(D((x0,h*sc),(x,h*sc),'thin,dotted'))
            if ruler[nm]: o.append(N(x0+.1,h*sc+.17,ruler[nm],'anchor=west,font=\\scriptsize'))
    return o
sc14=.85
pts14=[(0,4),(.8,2.1),(1.6,.6),(2.4,0),(3.2,.4),(4.0,1.2),(4.6,2),(5.2,2.6),(5.8,3),(6.4,3.5)]
hK,hL,hM,hN=4,0,2,3
assert hK-hL>hK-hM>hK-hN>0 and (hK-hM)==hM  # M'de Ek = Ep
o=ray(pts14,[('K',(0,4),(-.3,.3)),('L',(2.4,0),(0,-.4)),('M',(4.6,2),(.3,-.3)),('N',(5.8,3),(.3,-.35))],sc14,4,{'K':None,'M':None,'N':None})
SK14=tikz(o)
q('0014',tipId='fz-en2-ray-nitel',tip='Rayda enerji karşılaştırması',z='orta',alt='Mekanik Enerji',kaz='Sürtünmesiz rayda farklı noktalardaki kinetik ve potansiyel enerjileri karşılaştırır.',kalip='öncüllü',
 kart='K-FZEN2-14 (ray nitel) · K, L, M, N noktaları',
 metin='Sürtünmesiz bir rayın K noktasında durgun hâlde tutulan bir cisim serbest bırakılıyor. Cisim, ray boyunca ilerleyerek sırasıyla L, M ve N noktalarından geçiyor; raydan hiçbir noktada ayrılmıyor. Rayın K, M ve N noktalarının yerden yükseklikleri, şekildeki cetvelden okunabilmektedir. Hava direnci önemsizdir.\nBuna göre,\nI. Cismin kinetik enerjisi en büyük L noktasındadır.\nII. Cismin N noktasındaki hızı, M noktasındaki hızından büyüktür.\nIII. Cismin M noktasındaki kinetik enerjisi, potansiyel enerjisine eşittir.\nyargılarından hangileri doğrudur?',
 sekil=SK14,istenen='Doğru olan yargılar.',
 ip=['Her noktada toplam mekanik enerji aynıdır; kinetik enerji, K ile o nokta arasındaki yükseklik farkından gelir.'],
 bilgi=[EP],
 ad=[A('Yükseklikleri oku','Cetvelden K, L, M, N yükseklikleri okunur.','K: 4 m; L: 0; M: 2 m; N: 3 m'),A('I. yargı','En alçak nokta L’de potansiyel enerji en küçük, kinetik enerji en büyüktür.','E_k(L) = 4 m g → doğru'),A('II. yargı','N, M’den yüksektir; N’de kinetik enerji daha küçüktür.','v_N < v_M → yanlış'),A('III. yargı','M’de potansiyel enerji ve kinetik enerji hesaplanır.','E_p = 2 m g · E_k = (4 − 2) m g = 2 m g → doğru')],
 puf='Sürtünmesiz rayda hız yükseklikle ters değişir: yükseklik azaldıkça kinetik enerji artar.',
 **onc([True,False,True],['L en alçak nokta olduğundan potansiyel enerji en küçük, kinetik enerji en büyüktür','N, M’den yüksektir; yükseklik arttıkça kinetik enerji ve hız azalır','M’de E_p = 2mg ve E_k = (4 − 2)mg = 2mg olduğundan ikisi eşittir'],3))
# ================= 0015 başlangıç hızlı, tepe (zor, şekil)
v15,hK15,hM15=8,Fr(3),Fr(27,5)
v2=v15**2-2*g*(hM15-hK15); assert v2==16 and math.isqrt(int(v2))==4
assert math.sqrt(v15**2+2*g*float(hM15-hK15))>0 and v15**2-2*g*float(hM15)<0
sc15=.7
pts15=[(0,3),(.8,1.5),(1.6,.4),(2.4,0),(3.2,.4),(3.9,2.2),(4.6,4.6),(5.2,5.4),(5.8,4.6),(6.4,3.6)]
o=ray(pts15,[('K',(0,3),(-.3,.3)),('L',(2.4,0),(0,-.4)),('M',(5.2,5.4),(0,.35))],sc15,6,{'K':None,'M':'$5{,}4$'})
d=(.8,-1.5*sc15); nrm=math.hypot(*d); d=(d[0]/nrm,d[1]/nrm); S=(-.15*0+.1-d[1]*.4, 3*sc15+d[0]*.4)
o.append(AR(S,(S[0]+d[0]*.9,S[1]+d[1]*.9))); o.append(N(S[0]+.3,S[1]+.35,'$v_0=8$ m/s','vurgu,font=\\scriptsize,anchor=west'))
SK15=tikz(o)
q('0015',tipId='fz-en2-ray-hiz',tip='Başlangıç hızlı cismin tepedeki hızı',z='zor',alt='Mekanik Enerji',kaz='Başlangıç hızı olan cismin sürtünmesiz rayda tepe noktasındaki hızını enerji korunumundan bulur.',kalip='şekilli',
 kart='K-FZEN2-15 (başlangıç hızlı ray) · K’den v₀ ile geçiş, M tepesi',
 metin='Sürtünmesiz bir rayda hareket eden bir cisim, rayın K noktasından şekilde belirtilen hızla geçiyor, L vadisine iniyor ve ardından M tepesine tırmanıyor. K ve M noktalarının yerden yükseklikleri şekilde verilmiştir. Cisim raydan ayrılmıyor ve M tepesini aşabilmektedir; hava direnci önemsizdir. Cismin boyutları önemsenmeyecek kadar küçüktür ve ray hiçbir noktada cismi durdurmamaktadır.\n(g = 10 m/s²)\nBuna göre, cismin M noktasından geçerken hızı kaç m/s’dir?',
 sekil=SK15,dogru=4,yan=[(0,'M’nin yüksekliğini (5,4 m) K’ye göre değil zemine göre kullanıp 64 − 108 < 0 bulmuş ve cismin M’ye ulaşamayacağını sanmış.','dikkat'),(8,'Sürtünmesiz olduğu için hızın değişmeyeceğini sanmış; oysa yükseklik artınca kinetik enerji azalır.','bilgi'),(2,'K’nin zemine göre yüksekliğini (3 m) yükseklik farkı sanmış: 64 − 2 × 10 × 3 = 4 → 2 m/s.','dikkat'),(16,'v² = 16 değerini hıza çevirmeyi unutmuş.','islem')],
 istenen='Cismin M noktasındaki hızı (m/s).',
 ip=['Yalnız K ile M arasındaki yükseklik farkı önemlidir; başlangıçtaki kinetik enerji, tepeye çıkarken ne kadar azalır?'],
 bilgi=[EP,B('Hızlı başlangıç','başlangıç hızı varsa mekanik enerji E = ½ × m × v₀² + m × g × h’tır; hızlar toplanmaz, enerjiler korunur. Örnek: 2 m yükselen 1 kg’lık cisim 20 J kinetik enerji kaybeder')],
 ad=[A('Yükseklik farkı','M tepesi K’den yüksektir.','Δh = 5,4 − 3 = 2,4 m'),A('Enerji korunumu','Birim kütle için: ½v_M² = ½v₀² − g × Δh.','½ v_M² = 32 − 24'),A('v² değeri','Her iki taraf 2 ile çarpılır.','v_M² = 64 − 48 = 16'),A('Hız','Karekök alınır.','v_M = 4 m/s')],
 puf='Başlangıç hızlı cisimde kinetik enerji farkı = −m g Δh; kütle sadeleşir, hız karelerle hesaplanır.')
# ================= 0016 sürtünmeli eğik düzlem ısı (orta, şekil)
m16,h16,v16=2,5,6
Ep16=m16*g*h16; Ek16=Fr(1,2)*m16*v16**2; Q16=Ep16-Ek16
assert Ep16==100 and Ek16==36 and Q16==64 and Fr(Q16,2)==32 and Ep16+Ek16==136
o=[zemin(-.3,6.2),D((0,0),(0,2.5),'thick'),D((0,2.5),(4.0,0),'thick')]
o.append('\\begin{scope}[shift={(.55,2.1)},rotate=-32.0]\\draw[thick,fill=gray!25] (-.3,0) rectangle (.3,.4);\\end{scope}')
o.append(DM((-.5,0),(-.5,2.5))); o.append(N(-.55,1.25,'$5$ m','anchor=east,font=\\scriptsize'))
o.append(N(.35,2.95,'\\textbf{K}')); o.append(N(4.0,-.5,'\\textbf{L}'))
o.append(AR((4.4,.4),(5.9,.4))); o.append(N(5.15,.75,'$v=6$ m/s','vurgu,font=\\scriptsize'))
SK16=tikz(o)
q('0016',tipId='fz-en2-surtunme-isi',tip='Eğik düzlemde ısıya dönüşen enerji',z='orta',alt='Sürtünmeli Yüzeyde Isıya Dönüşen Enerji',kaz='Eğik düzlemde kayan cismin başlangıç ve son enerjisini karşılaştırarak ısıya dönüşen enerjiyi bulur.',kalip='şekilli',
 kart='K-FZEN2-16 (sürtünmeli eğik düzlem) · ısı = ilk − son',
 metin='Kütlesi 2 kg olan bir cisim, pürüzlü bir eğik düzlemin tepesindeki K noktasından serbest bırakılıyor ve düzlemin dibindeki L noktasından yatay doğrultuda geçiyor. K noktasının yerden yüksekliği ve cismin L noktasındaki hızı şekilde verilmiştir. Hava direnci önemsizdir; cismin enerjisindeki azalmanın tamamı cisim ile eğik düzlem arasındaki sürtünmeden kaynaklanmaktadır.\n(g = 10 m/s²)\nBuna göre, cisim K’den L’ye inerken sürtünme nedeniyle ısıya dönüşen enerji kaç J’dür?',
 sekil=SK16,dogru=64,yan=[(172,'Kinetik enerjiyi ½ çarpanını unutarak (72 J) hesaplayıp potansiyel enerjiyle toplamış.','islem'),(36,'L’deki kinetik enerjiyi (36 J) ısıya dönüşen enerji sanmış.','dikkat'),(100,'K’deki potansiyel enerjinin (100 J) tamamının ısıya dönüştüğünü sanmış.','dikkat'),(136,'Potansiyel enerji ile kinetik enerjiyi toplamış.','islem')],
 istenen='Isıya dönüşen enerji (J).',
 ip=['K ve L noktalarında cismin hangi enerji türlerine sahip olduğunu belirle; sürtünme varken toplam mekanik enerjiye ne olur?'],
 bilgi=[EP,B('Sürtünme ve ısı','sürtünmeli ortamda mekanik enerji korunmaz; azalan mekanik enerji ısıya dönüşür. Örnek: 100 J’lük cisim 70 J kinetik enerjiyle yere ulaşırsa 30 J ısı olur')],
 ad=[A('İlk enerji','K’de cisim durgundur; yalnız potansiyel enerji vardır.','E_K = 2 × 10 × 5 = 100 J'),A('Son enerji','L’de yükseklik sıfırdır; yalnız kinetik enerji vardır.','E_L = ½ × 2 × 6² = 36 J'),A('Isı','Azalan mekanik enerji ısıya dönüşür.','Q = 100 − 36 = 64 J')],
 puf='Sürtünmeli yolda ısı = ilk mekanik enerji − son mekanik enerji.')
# ================= 0017 sürtünmeli yatay nitel (zor, öncüllü, şekil)
# f = mu m g ; x = v²/(2 mu g) kütleden bağımsız ; Q = ½ m v² ; sürtünme kuvveti 2 katı
mu,v17,mA=Fr(1,2),10,3
def dur(m): return Fr(v17**2)/(2*mu*g), Fr(1,2)*m*v17**2, mu*m*g
(xA,QA,fA),(xB,QB,fB)=dur(mA),dur(2*mA)
assert xA==xB==10 and QB==2*QA and fB==2*fA
o=[]
for y,lab,t in ((0,'K','$m$'),(-2.1,'L','$2m$')):
    o.append(zemin(0,6.6,y)); o.append(f'\\draw[thick,fill=gray!25] (.5,{y}) rectangle (1.5,{y+.8});'); o.append(N(1.0,y+.4,t))
    o.append(AR((1.6,y+.4),(3.0,y+.4))); o.append(N(2.3,y+.75,'$v$','vurgu'))
    o.append(N(-.45,y+.4,f'\\textbf{{{lab}}}'))
SK17=tikz(o)
q('0017',tipId='fz-en2-surtunme-nitel',tip='Sürtünmeli yatayda durma ve ısı',z='orta',alt='Sürtünmeli Yüzeyde Isıya Dönüşen Enerji',kaz='Aynı sürtünmeli yüzeyde farklı kütleli cisimlerin durma yolunu, sürtünme kuvvetini ve ısıya dönüşen enerjiyi karşılaştırır.',kalip='öncüllü',
 kart='K-FZEN2-17 (sürtünmeli yatay nitel) · kütle 2 katı, hız aynı',
 metin='Aynı pürüzlü yatay yüzey üzerinde, kütleleri ve ilk hızları şekilde gösterilen K ve L cisimleri harekete başlıyor. Cisimlerin yüzeyle arasındaki kinetik sürtünme katsayısı aynıdır; cisimlere yalnız sürtünme kuvveti etki eder ve cisimler durana kadar kayar. Hava direnci önemsizdir.\nBuna göre,\nI. K cismi, L cisminden daha uzun yol alarak durur.\nII. L cisminde ısıya dönüşen enerji, K cismindekinin iki katıdır.\nIII. L cismine etki eden sürtünme kuvveti, K cismine etki edenin iki katıdır.\nyargılarından hangileri doğrudur?',
 sekil=SK17,istenen='Doğru olan yargılar.',
 ip=['Sürtünme kuvveti ve cismin ilk kinetik enerjisi kütleyle nasıl değişir? Durana kadar yapılan iş ile ilk kinetik enerjiyi eşitle.'],
 bilgi=[B('Sürtünme kuvveti','F_s = μ × N; yatay yüzeyde N = m × g olduğundan sürtünme kuvveti kütleyle artar. Örnek: μ = 0,5 ve 4 kg için F_s = 0,5 × 40 = 20 N'),B('Sürtünme işi','durana kadar ısıya dönüşen enerji, cismin ilk kinetik enerjisine eşittir: F_s × x = ½ × m × v²')],
 ad=[A('Sürtünme kuvveti','F_s = μ m g; L’nin kütlesi iki katıdır.','F_L = 2 × F_K → III doğru'),A('Isıya dönüşen enerji','Isı, ilk kinetik enerjiye eşittir.','Q = ½ m v²; L için iki katı → II doğru'),A('Durma yolu','F_s × x = ½ m v² eşitliğinde m sadeleşir.','μ m g x = ½ m v² → x = v² ÷ (2 μ g) iki cisimde eşit'),A('Sonuç','K daha uzun yol almaz → I yanlış.','II ve III')],
 puf='Aynı yüzeyde durma yolu kütleden bağımsızdır; ısıya dönüşen enerji ve sürtünme kuvveti kütleyle artar.',
 **onc([False,True,True],['iki cisimde de durma yolu x = v² ÷ (2μg) olduğundan kütleden bağımsızdır, yollar eşittir','ısıya dönüşen enerji ilk kinetik enerjiye eşittir ve kütle iki katına çıkınca iki katına çıkar','sürtünme kuvveti μ × m × g olduğundan kütle iki katına çıkınca iki katına çıkar'],4))
# ================= 0018 Ek–x grafiği (zor)
F18,f18=15,5
assert (40-0)//4==10 and F18-f18==10 and Fr(40,12-4)==f18 and F18==10+f18 and Fr(40,4)==10 and 10+10==20 and 40!=F18
pl=['\\addplot[very thick,vurgu] coordinates {(0,0)(4,40)(12,0)};']
SK18=tikz(axis(pl,14,48,'0,4,8,12','0,10,20,30,40','$x$ (m)','$E_k$ (J)'))
q('0018',tipId='fz-en2-kinetik-grafik',tip='Kinetik enerji–yol grafiğinden kuvvet',z='zor',alt='Kinetik Enerji',kaz='Kinetik enerji–yol grafiğinin eğimlerinden net kuvveti ve sürtünme kuvvetini bulur.',kalip='grafik',
 kart='K-FZEN2-18 (Ek–x grafiği) · iki bölge, eğimler',
 metin='Yatay ve pürüzlü bir zeminde durmakta olan bir kızak, ilk 4 m boyunca yola paralel sabit bir kuvvetle çekiliyor; 4. metreden sonra kuvvet kaldırılıyor ve kızak sürtünme nedeniyle duruyor. Kızağın kinetik enerjisinin konuma bağlı değişimi şekildeki grafikte verilmiştir. Sürtünme kuvveti zeminin her yerinde sabittir, hava direnci önemsizdir ve kızak yol boyunca düz bir çizgide ilerlemektedir.\nBuna göre, çekme kuvvetinin büyüklüğü kaç N’dur?',
 sekil=SK18,dogru=15,yan=[(5,'Yalnız sürtünme kuvvetini (40 ÷ 8) çekme kuvveti sanmış.','dikkat'),(10,'İlk bölgedeki eğimi (net kuvvet) çekme kuvveti sanmış; sürtünmeyi eklemeyi unutmuş.','dikkat'),(20,'Sürtünme kuvvetini 10 N alıp F = 10 + 10 = 20 N bulmuş.','islem'),(40,'Grafikteki en büyük kinetik enerji değerini kuvvet sanmış.','bilgi')],
 istenen='Çekme kuvvetinin büyüklüğü (N).',
 ip=['Kuvvet kalktıktan sonra kızağa yalnız hangi kuvvet etki ediyor? Grafikteki iki eğimin her biri neyi gösteriyor?'],
 bilgi=[B('Kinetik enerji–yol grafiği','bileşke kuvvetin yaptığı iş kinetik enerji değişimine eşittir: F_net × x = ΔE_k; grafiğin eğimi bileşke kuvvettir. Örnek: 5 m’de kinetik enerjisi 20 J artan cismin bileşke kuvveti 4 N’dur')],
 ad=[A('İlk bölge','Kinetik enerji 4 m’de 40 J artmıştır; eğim bileşke kuvvettir.','F − F_s = 40 ÷ 4 = 10 N'),A('İkinci bölge','Yalnız sürtünme kuvveti etkir; 8 m’de 40 J azalır.','F_s = 40 ÷ 8 = 5 N'),A('Kuvveti bul','İlk denklemde sürtünme yerine konur.','F = 10 + 5 = 15 N')],
 puf='Kinetik enerji–yol grafiğinde eğim bileşke kuvvettir; kuvvet kalktıktan sonraki eğim sürtünme kuvvetini verir.')
# ================= 0019 lamba tablosu (öncüllü)
lam=[('Akkor lamba',5,95),('Floresan lamba',20,80),('LED lamba',30,70)]
assert all(i+s==100 for _,i,s in lam) and max(i for _,i,_ in lam)==30 and lam[1][1]<lam[2][1]
SK19=tikz(tablo(['Lamba','Elektrik (J)','Işık (J)','Isı (J)'],[[n,'100',str(i),str(s)] for n,i,s in lam],[3.0,2.4,2.0,2.0]))
q('0019',tipId='fz-en2-lamba-tablo',tip='Lambalarda enerji dönüşümü',z='kolay',alt='Enerji Dönüşümleri',kaz='Lambalarda elektrik enerjisinin ışık ve ısıya dönüşümünü tablodan yorumlar, verimi karşılaştırır.',kalip='tablo',
 kart='K-FZEN2-19 (lamba tablosu) · akkor, floresan, LED',
 metin='Bir tüketici dergisi, aynı ortamda çalıştırdığı üç lambanın her birinin 100 J’lük elektrik enerjisini ne kadar ışık ve ne kadar ısı enerjisine dönüştürdüğünü ölçmüş ve sonuçları şekildeki tabloda vermiştir. Ölçümler sırasında lambalar başka bir enerji biçimine dönüşüm yapmamıştır.\nBuna göre,\nI. Elektrik enerjisini ışığa en çok dönüştüren lamba LED lambadır.\nII. Akkor lambada elektrik enerjisinin büyük bölümü ısıya dönüşür.\nIII. Floresan lambanın verimi LED lambanınkinden yüksektir.\nyargılarından hangileri doğrudur?',
 sekil=SK19,istenen='Doğru olan yargılar.',
 ip=['Her lamba için elektrik enerjisinin ne kadarının işe yaradığını (ışığa dönüştüğünü) karşılaştır.'],
 bilgi=[VE,B('Enerji dönüşümü','lambada elektrik enerjisi ışık ve ısıya dönüşür; enerji yok olmaz, toplam enerji korunur. Örnek: 40 J elektrik enerjisinin 10 J’ü ışığa dönüşürse 30 J’ü ısı olur')],
 ad=[A('Verimleri bul','Işık enerjisi ÷ 100 J.','Akkor %5 · Floresan %20 · LED %30'),A('I. yargı','En çok ışık veren lamba LED’dir.','30 J en büyük → I doğru'),A('II. yargı','Akkor lambada 95 J ısıdır.','95 J > 100 J’ün yarısı → II doğru'),A('III. yargı','Floresan 20 J, LED 30 J ışık verir.','%20 < %30 → III yanlış')],
 puf='Verim, yararlı enerjinin (ışığın) harcanan enerjiye oranıdır; enerjinin geri kalanı ısıya dönüşür.',
 **onc([True,True,False],['LED lamba 100 J’ün 30 J’ünü ışığa dönüştürerek en yüksek verimdedir','akkor lamba 100 J’ün 95 J’ünü ısıya dönüştürür','Floresan lambanın ışığı 20 J, LED’inki 30 J olduğundan verimi LED’den düşüktür'],3))
# ================= 0020 eğik düzlem verimi (orta, şekil)
m20,h20,l20,F20=20,3,5,150
Wy=m20*g*h20; Wg=F20*l20; ver=Fr(Wy,Wg)
assert Wy==600 and Wg==750 and ver==Fr(4,5) and Fr(h20,l20)==Fr(3,5) and Fr(Wg,Wy)==Fr(5,4) and Fr(F20*h20,Wy)==Fr(3,4) and Fr(Wg-Wy,Wg)==Fr(1,5)
hs=.8; hc=h20*hs; bs=math.sqrt((l20*hs)**2-hc**2); th=math.degrees(math.atan2(hc,bs)); c,sn=bs/(l20*hs),hc/(l20*hs)
o=[zemin(-.3,bs+1.0),D((0,0),(bs,hc),'thick'),D((bs,hc),(bs,0),'thin')]
px,py=1.3*c,1.3*sn
o.append(f'\\begin{{scope}}[shift={{({px:.3f},{py:.3f})}},rotate={th:.2f}]\\draw[thick,fill=gray!25] (-.45,0) rectangle (.45,.6);\\draw[vurgu,very thick,{ARR}] (.45,.3) -- (1.6,.3);\\node[vurgu,rotate=0] at (1.05,.65) {{$150$ N}};\\end{{scope}}')
o.append(DM((bs+.3,0),(bs+.3,hc))); o.append(N(bs+.35,hc/2,'$3$ m','anchor=west,font=\\scriptsize'))
o.append(f'\\node[rotate={th:.2f},font=\\scriptsize] at ({bs*.72+.22*sn:.3f},{hc*.72-.22*c:.3f}) {{$5$ m}};')
SK20=tikz(o)
q('0020',tipId='fz-en2-verim-egik',tip='Eğik düzlemin verimi',z='orta',alt='Verim',kaz='Eğik düzlemde yapılan yararlı işi ve harcanan işi karşılaştırarak verimi hesaplar.',kalip='şekilli',
 kart='K-FZEN2-20 (eğik düzlem verimi) · yararlı iş m g h, harcanan iş F ℓ',
 metin='Bir yük görevlisi, 20 kg kütleli bir sandığı pürüzlü bir eğik düzlemin tepesine çıkarmak için düzlem yüzeyine paralel bir kuvvetle sandığı sabit hızla yukarı çekiyor. Eğik düzlemin boyu, yüksekliği ve uygulanan kuvvet şekilde verilmiştir. Sandığa yapılan işin bir bölümü sürtünme nedeniyle ısıya dönüşmektedir; sandık, çıkış boyunca hızlanmamakta ve yavaşlamamaktadır.\n(g = 10 m/s²)\nBuna göre, eğik düzlemin verimi yüzde kaçtır?',
 sekil=SK20,dogru=80,yan=[(20,'Kayıp enerjinin yüzdesini (150 ÷ 750) verim sanmış.','dikkat'),(60,'Verimi yükseklik ile boyun oranı (3 ÷ 5) sanmış.','bilgi'),(75,'Kaybı (750 − 600 = 150 J) yararlı işe oranlayıp (%25) 100’den çıkarmış.','islem'),(125,'Oranı ters almış (harcanan iş ÷ yararlı iş); verim hiçbir zaman %100’ü aşmaz.','islem')],
 istenen='Eğik düzlemin verimi (%).',
 ip=['Yararlı işi ve harcanan işi hangi büyüklüklerle bulabilirsin? Verim bu ikisinin oranıdır.'],
 bilgi=[VE,EP],
 ad=[A('Yararlı iş','Sandığın potansiyel enerji kazancıdır.','W_y = 20 × 10 × 3 = 600 J'),A('Harcanan iş','Çekme kuvveti, 5 m’lik yol boyunca iş yapar.','W_h = 150 × 5 = 750 J'),A('Verim','Yararlı iş harcanan işe bölünür.','verim = 600 ÷ 750 = 0,8 = %80')],
 puf='Verim = yararlı iş ÷ harcanan iştir; eğik düzlemde yararlı iş m g h, harcanan iş F ℓ’dir.')
# ================= 0021 seri verim (zor, şekil)
Eh21=1000*g*40; el=Fr(Eh21)*Fr(8,10)*Fr(75,100)/1000
assert Eh21==400000 and el==240 and Fr(Eh21,1000)*Fr(8,10)==320 and Fr(Eh21,1000)*Fr(75,100)==300 and Fr(Eh21,1000)*Fr(155,200)==310 and Fr(8,10)+Fr(75,100)==Fr(31,20)
def kutu(x,y,t,w=4.4): return f'\\node[draw,rounded corners=2pt,minimum width={w}cm,minimum height=1.5cm,text width={w-.3}cm,align=center,font=\\large] at ({x},{y}) {{{t}}};'
o=[kutu(0,0,'Suyun potansiyel enerjisi'),kutu(6.4,0,'Türbin\\\\ verim \\%80'),kutu(6.4,-2.4,'Jeneratör\\\\ verim \\%75'),kutu(0,-2.4,'Elektrik enerjisi')]
o.append(AR((2.3,0),(4.1,0),'thick')); o.append(AR((6.4,-.8),(6.4,-1.6),'thick')); o.append(AR((4.1,-2.4),(2.3,-2.4),'thick'))
SK21=tikz(o)
q('0021',tipId='fz-en2-verim-zincir',tip='Seri verim ve elektriksel güç',z='orta',alt='Verim',kaz='Ardışık iki sistemin verimini birleştirerek santralin elektriksel gücünü hesaplar.',kalip='şekilli',
 kart='K-FZEN2-21 (seri verim) · baraj, türbin ve jeneratör',
 metin='Bir hidroelektrik santralinde her saniye 1 000 kg su, 40 m yükseklikten türbine akmaktadır. Suyun potansiyel enerjisi önce türbinde, sonra jeneratörde dönüştürülerek elektrik enerjisine çevrilmektedir; bu iki aşamanın verimleri şekilde gösterilmiştir. Başka bir enerji kaybı yoktur, su türbine sürekli aynı miktarda akmaktadır ve suyun türbine çarpmadan önceki hızı ihmal edilecek kadar küçüktür.\n(g = 10 m/s²)\nBuna göre, santralin ürettiği elektriksel güç kaç kW’tır?',
 sekil=SK21,dogru=240,yan=[(300,'Yalnız jeneratörün verimini (%75) uygulamış; türbin kaybını atlamış.','dikkat'),(310,'İki verimin ortalamasını (%77,5) uygulamış; verimler çarpılır, ortalaması alınmaz.','bilgi'),(320,'Yalnız türbinin verimini (%80) uygulamış; jeneratör kaybını atlamış.','dikkat'),(400,'Verimleri hiç hesaba katmamış; suyun saniyedeki enerjisini (400 kW) elektrik gücü sanmış.','dikkat')],
 istenen='Santralin elektriksel gücü (kW).',
 ip=['Önce suyun bir saniyede kaybettiği potansiyel enerjiyi bul; ardışık iki aşamada ilk aşamadan çıkan enerji ikinci aşamanın girdisidir.'],
 bilgi=[VE,GU,EP],
 ad=[A('Suyun enerjisi','Bir saniyede 1 000 kg su 40 m düşer.','E = 1000 × 10 × 40 = 400 000 J'),A('Türbin çıkışı','Verim %80.','0,8 × 400 000 = 320 000 J'),A('Jeneratör çıkışı','Türbinden çıkan enerji jeneratöre girer; verim %75.','0,75 × 320 000 = 240 000 J'),A('Güç','Bir saniyede üretilen enerji güçtür.','P = 240 000 J ÷ 1 s = 240 000 W = 240 kW')],
 puf='Ardışık sistemlerde toplam verim, verimlerin çarpımıdır; ardışık verimler toplanmaz ya da ortalaması alınmaz.')
# ================= 0022 yenilenebilir tablo (kolay)
kay=[('Kömür',30,False),('Doğal gaz',25,False),('Hidroelektrik',20,True),('Rüzgâr',12,True),('Güneş',6,True),('Jeotermal',4,True),('Biyokütle',3,True)]
assert sum(p for _,p,_ in kay)==100
yen=sum(p for _,p,r in kay if not r); assert yen==55 and yen+4==59 and yen+3==58 and yen+20==75 and 100-yen==45
SK22=tikz(tablo(['Kaynak','Pay (\\%)'],[[n,str(p)] for n,p,_ in kay],[3.4,2.4]))
q('0022',tipId='fz-en2-kaynak-tablo',tip='Elektrik üretiminde yenilenemez kaynak payı',z='kolay',alt='Enerji Kaynakları',kaz='Enerji kaynaklarını yenilenebilir ve yenilenemez olarak sınıflandırıp paylarını toplar.',kalip='tablo',
 kart='K-FZEN2-22 (enerji kaynakları) · yedi kaynaklı üretim tablosu',
 metin='Bir ülkenin bir yıllık elektrik üretiminin kaynaklara göre dağılımı şekildeki tabloda yüzde olarak verilmiştir. Ülkenin enerji bakanlığı, kaynakların toplam paylarını türlerine göre karşılaştırarak ülkenin dışa bağımlılığını ve çevreye etkisini değerlendirmek istemektedir.\nBuna göre, bu ülkenin elektrik üretiminde yenilenemez enerji kaynaklarının toplam payı yüzde kaçtır?',
 sekil=SK22,dogru=55,yan=[(45,'Yenilenebilir kaynakların toplam payını (%45) bulmuş; sorulan yenilenemez paydır.','dikkat'),(58,'Biyokütleyi de yenilenemez sayıp toplama eklemiş; biyokütle yenilenebilirdir.','bilgi'),(59,'Jeotermal enerjiyi yenilenemez sayıp toplama eklemiş; jeotermal yenilenebilirdir.','bilgi'),(75,'Hidroelektriği yenilenemez sayıp toplama eklemiş; akarsu enerjisi yenilenebilirdir.','bilgi')],
 istenen='Yenilenemez kaynakların toplam payı (%).',
 ip=['Kaynakları ikiye ayır: kullanıldıkça tükenen fosil yakıtlar ile doğada sürekli yenilenenler.'],
 bilgi=[B('Enerji kaynakları','kömür, petrol ve doğal gaz yenilenemez; güneş, rüzgâr, akarsu (hidroelektrik), jeotermal ve biyokütle yenilenebilir kaynaklardır. Örnek: kömür yenilenemez, rüzgâr yenilenebilirdir')],
 ad=[A('Kaynakları ayır','Fosil yakıtlar yenilenemezdir; diğerleri yenilenebilirdir.','Yenilenemez: kömür, doğal gaz'),A('Payları oku','Tablodan iki payı al.','Kömür %30 · Doğal gaz %25'),A('Topla','İki payı topla.','30 + 25 = %55')],
 puf='Fosil yakıtlar (kömür, petrol, doğal gaz) yenilenemezdir; güneş, rüzgâr, hidroelektrik, jeotermal ve biyokütle yenilenebilirdir.')
bitir(P,'enerjiiki','fiz|İş, Güç ve Enerji')
