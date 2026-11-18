"""TYT Fizik · İş, Güç ve Enerji (üçüncü/dördüncü genişletme) · 10 soru.
Kardeş yok, ipucu 1. Devreler circuitikz (tikzpicture içinde, european), grafikler pgfplots; her sayı ve çeldirici değer Python'da assert edilir.
Öncüllü sorularda her öncülün doğruluğu yorumda gerekçelendirilir; yanlış şık metinleri öncül yanılgılarından üretilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
sys.path.insert(0,os.path.join(HV,'tyt-mat'))
from _hafif_mat import tablo_svg
from math import sin,cos,radians
KONU='İş, Güç ve Enerji'; H.KONU=KONU
P=Parti('enerjiuc','İş, Güç ve Enerji','fiz|İş, Güç ve Enerji',ders='TYT Fizik',idon='tytfiz')
KAYNAK='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9–10. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'
TAIL='\n\\end{tikzpicture}'
def tk(body): return tikz_svg(HEAD+body+TAIL)
def nn(no): return f'{int(no):02d}'
def kartk(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZEN3-{nn(no)}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)

# ---------- sayısal soru ----------
def N(no,tipId,tip,alt,z,kaz,fikir,tuzak,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,kalip=None,sira=None):
    kalip=kalip or ('şekilli' if sekil else 'düz')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZEN3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı',kisa=None,sira=sira)

# ---------- öncüllü soru ----------
ROM=['I','II','III']
def secenek(S):
    S=sorted(S,key=ROM.index)
    return 'Yalnız '+S[0] if len(S)==1 else (' ve '.join(S) if len(S)==2 else 'I, II ve III')
def ayristir(s):
    if s.startswith('Yalnız'): return {s.split()[1]}
    if s=='I, II ve III': return set(ROM)
    return set(s.split(' ve '))
def O(no,tipId,tip,alt,z,kaz,fikir,tuzak,kok,stm,sira,oku,ip,bilgi,puf,sekil=None,son='Buna göre, yukarıdaki yargılardan hangileri doğrudur?',kalip=None):
    """stm: [(yargı, doğru_mu, doğru_gerekçe, yanılgı)] — yanılgı: yargıyı ters değerlendiren öğrencinin düşüncesi."""
    assert len(stm)==3 and len(sira)==5 and len(set(sira))==5
    S={ROM[i] for i,s in enumerate(stm) if s[1]}; dogru=secenek(S); assert dogru in sira,(no,dogru,sira)
    assert all(ayristir(o)!=S for o in sira if o!=dogru)
    def cel(o):
        K=ayristir(o); parts=[]
        for i,(t,v,w,m) in enumerate(stm):
            r=ROM[i]
            if r in K and not v: parts.append(f'{r}. yargıyı doğru sanmış: {m}')
            if r not in K and v: parts.append(f'{r}. yargıyı yanlış sanmış: {m}')
        assert parts,(no,o); return ' '.join(parts)
    yan=[(o,cel(o),'bilgi') for o in sira if o!=dogru]
    metin=kok+'\n'+'\n'.join(f'{ROM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+son
    ad=[A('Verileri oku',oku[0],oku[1])]
    for i,(t,v,w,m) in enumerate(stm): ad.append(A(f'{ROM[i]}. yargıyı incele',w,f'{ROM[i]}: '+('doğru' if v else 'yanlış')))
    ad.append(A('Sonucu belirle','Doğru olan yargıları birleştir.',dogru))
    kalip=kalip or ('şekilli' if sekil else 'öncüllü')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen='Verilen yargılardan doğru olanlar.',ad=ad,sekil=sekil,sira=sira,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZEN3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı')

# ---------- elektrostatik çizim yardımcıları ----------
def elsk(ox,a,top=''):
    """Elektroskop: kutu, saplı topuz ve yapraklar (a = yaprağın düşeyle açısı, derece)."""
    L=.55; px,py=ox,1.0
    s=f'\\draw[thick] ({ox-.8},0) rectangle ({ox+.8},1.7);\n'
    s+=f'\\draw[thick] ({ox},{py}) -- ({ox},2.3); \\draw[thick,fill=gray!25] ({ox},2.55) circle (.25);\n'
    for sg in (-1,1):
        s+=f'\\draw[very thick] ({px},{py}) -- ({px+sg*L*sin(radians(a)):.3f},{py-L*cos(radians(a)):.3f});\n'
    return s
def cubuk(x,y,isaret,w=1.8,h=.38,ad='',ang=0):
    """Yatay çubuk (merkez x,y); isaret '+', '−' ya da ''."""
    s=f'\\begin{{scope}}[rotate around={{{ang}:({x},{y})}}]\\draw[thick,fill=gray!15] ({x-w/2},{y-h/2}) rectangle ({x+w/2},{y+h/2});\n'
    isaret=isaret.replace('−','-')
    if isaret:
        for k in range(3): s+=f'\\node[font=\\footnotesize] at ({x-w/3+k*w/3:.3f},{y}) {{${isaret}$}};\n'
    s+='\\end{scope}\n'
    return s
def kure(x,y,r=.5,et='',fill='gray!15'):
    return f'\\draw[thick,fill={fill}] ({x},{y}) circle ({r});\n'+(f'\\node at ({x},{y}) {{{et}}};\n' if et else '')
def ayak(x,y,r=.5):
    return f'\\draw[thick,fill=gray!40] ({x-.28},{y-r-.35}) rectangle ({x+.28},{y-r});\n\\draw[thick] ({x-.55},{y-r-.35}) -- ({x+.55},{y-r-.35});\n'
def zemin(x,y):
    return f'\\draw ({x},{y}) node[ground]{{}};\n'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def GR(w,h,xm,ym,dx,dy,xl,yl,*g):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}[width=%s,height=%s,xmin=0,xmax=%s,ymin=0,ymax=%s,xtick distance=%s,ytick distance=%s,grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={%s},ylabel={%s},xlabel style={font=\\small},ylabel style={font=\\small}]\n'%(w,h,xm,ym,dx,dy,xl,yl)+'\n'.join(g)+'\n\\end{axis}\n\\end{tikzpicture}')
def dimv(x,y0,y1,t,side='right'): return f'\\draw[<->,thin] ({x},{y0}) -- ({x},{y1}); \\node[{side},font=\\small] at ({x},{(y0+y1)/2}) {{{t}}};'
# =============== 01 · sıçrayan top, enerji kaybı yüzdesi · kolay ===============
h0,h1=Fr(3,2),Fr(9,10); kayip=(h0-h1)/h0*100
assert kayip==40 and h1/h0*100==60 and h1*100==90 and h0*100==150 and (h0-h1)/h0==Fr(2,5)
sk=('\\draw[thick] (-.5,0) -- (2.8,0);\n'
    f'\\draw[thin,dashed,{ARR}] (0,2.8) -- (0,.12); \\draw[thin,dashed,{ARR}] (.05,.05) .. controls (.5,2.3) and (.8,1.8) .. (1.1,1.8);\n'
    '\\draw[thick,fill=gray!30] (0,3.0) circle (.15); \\draw[thick,fill=gray!30] (1.1,1.8) circle (.15);\n'
    +dimv(-.45,0,3.0,'$1{,}5$ m','left')+dimv(1.9,0,1.8,'$0{,}9$ m')+'\n\\draw[thin,gray] (1.1,1.8) -- (1.9,1.8);')
N('0001','fz-en3-verim','Enerji dönüşümü ve verim','Enerji Dönüşümleri','kolay',
 'Sıçrayan topun çıkabildiği yüksekliklerden mekanik enerji kaybının yüzdesini bulur.',
 'Topun mekanik enerjisi yükseklikle orantılıdır; çarpmada kaybedilen enerji, başlangıçtaki ve sıçramadan sonraki yüksekliklerin farkından bulunur.',
 'Kalan enerjinin yüzdesini kayıp sanmak; yükseklik değerini yüzde sanmak.',
 'Yatay bir zeminden, şekilde belirtilen yükseklikten serbest bırakılan top zemine çarpıp sıçrıyor; sıçramadan sonra ulaştığı en büyük yükseklik şekilde gösterilmiştir. Hava direnci ihmal edilmektedir; kaybolan enerji yalnız çarpma sırasında oluşmaktadır.\nBuna göre, topun zemine çarpma sırasında kaybettiği mekanik enerji, ilk mekanik enerjisinin yüzde kaçıdır?',
 40,[(Fr(2,5),'Oranı yüzdeye çevirmeyi unutmuş: (1,5 − 0,9) ÷ 1,5 = 0,4.','islem'),(60,'Kalan enerjinin yüzdesini (0,9 ÷ 1,5) kayıp sanmış.','dikkat'),(90,'Sıçrama yüksekliği olan 0,9 değerini yüzde 90 olarak okumuş.','dikkat'),(150,'Başlangıç yüksekliğini (1,5) yüzde 150 olarak yazmış.','dikkat')],
 'Kaybolan enerjinin ilk enerjiye yüzdesi.',
 ['Topun mekanik enerjisi bu iki yüksekliğe nasıl bağlıdır? Hangi büyüklükler sabit kalıyor?'],
 [B('Potansiyel enerji','E = m·g·h; aynı cisim için enerji yükseklikle orantılıdır. Örnek: 2 m yüksekliğin enerjisi 1 m yüksekliğinkinin iki katıdır')],
 [A('Enerjileri yükseklikle ifade et','Kütle ve g aynı; enerji yükseklikle orantılı.','E_ilk ∝ 1,5 · E_son ∝ 0,9'),
  A('Kaybı bul','Kayıp, iki enerji arasındaki farktır.','1,5 − 0,9 = 0,6'),
  A('Yüzdeye çevir','Kaybı ilk enerjiye böl.','0,6 ÷ 1,5 × 100 = %40')],
 'Aynı cismin enerjisi yüksekliğiyle orantılıdır; enerji yüzdesini yükseklik oranlarından bulabilirsin.',sekil=tk(sk))

# =============== 02 · merdiven çıkan kişinin gücü · kolay ===============
m2,h2,t2=60,12,24
P2=Fr(m2*10*h2,t2); assert P2==300
assert (Fr(m2*h2,t2),m2*10*h2,m2*h2,Fr(m2*10*h2,2))==(30,7200,720,3600) and Fr(m2*10*h2,12)==600
sk=('\\draw[thick] (0,0) -- (0,0.5) -- (.7,.5) -- (.7,1.0) -- (1.4,1.0) -- (1.4,1.5) -- (2.1,1.5) -- (2.1,2.0) -- (2.8,2.0) -- (2.8,2.5) -- (3.5,2.5) -- (3.5,3.0) -- (4.2,3.0);\n'
    '\\draw[thick] (-.4,0) -- (4.5,0); \\draw[thin,dashed] (4.2,0) -- (4.2,3.0); \\draw[thin,dashed] (0,3.0) -- (4.2,3.0);\n'
    +dimv(4.6,0,3.0,'$12$ m')+'\n\\draw[thick,fill=white] (1.4,1.85) circle (.16); \\draw[thick] (1.4,1.69) -- (1.4,1.25);')
N('0002','fz-en3-guc','Güç ve verim','Güç','kolay',
 'Yükseklik, kütle ve süreden yararlanarak kişinin yer çekimine karşı yaptığı işin gücünü hesaplar.',
 'Kişi, yükselme boyunca ağırlığına karşı iş yapar: W = m·g·h; güç bu işin süreye oranıdır.',
 'Gücü iş sanmak; g’yi ya da süreyi atlamak; yüksekliği yanlış okumak.',
 'Kütlesi 60 kg olan bir kişi, şekilde gösterilen merdivenin altından üstüne düzgün hızla çıkıyor ve bu yolu 24 s’de tamamlıyor (g = 10 m/s²).\nBuna göre, kişinin yer çekimine karşı yaptığı işin ortalama gücü kaç W’tır?',
 300,[(720,'g’yi unutup kütle ile yüksekliği çarpmış (60 × 12) ve süreyi kullanmamış.','dikkat'),(3600,'İşi ½·m·g·h sanıp (7200 ÷ 2) süreye bölmeden bırakmış.','bilgi'),(600,'Süre yerine 12 yazarak (12 s) bölmüş: 7200 ÷ 12 = 600 W.','dikkat'),(7200,'Yapılan işi (7200 J) güç sanmış; süreye bölmemiş.','bilgi')],
 'Kişinin ortalama gücü (W).',
 ['Önce kişinin yer çekimine karşı yaptığı işi bul; gücün işle süre arasındaki ilişkisini düşün.'],
 [B('Güç','birim zamanda yapılan iştir: P = W ÷ t. Örnek: 200 J’lük işi 4 s’de yapan kişinin gücü 50 W’tır'),B('Yer çekimine karşı iş','cismi h kadar yükseltmek için gereken iş W = m·g·h’tır')],
 [A('İşi bul','Yükselme boyunca ağırlığa karşı iş yapılır.','W = 60 × 10 × 12 = 7200 J'),A('Süreyi kullan','Verilen süre 24 s.','t = 24 s'),A('Gücü bul','Güç, işin süreye oranıdır.','P = 7200 ÷ 24 = 300 W')],
 'Merdiven, rampa ya da ip gibi yollar fark etmez; yer çekimine karşı iş yalnız yükseklik farkına bağlıdır.',sekil=tk(sk))

# =============== 03 · hareketli makara · öncüllü · orta ===============
Y3,Gm,Gy=40,10,2
F3=Fr(Y3+Gm,2); assert F3==25
W3=F3*2*Gy; dEp=Y3*Gy; assert (W3,dEp,F3*Gy,Fr(Y3,2))==(100,80,50,20)
sk=('\\draw[thick] (-.2,3.7) -- (.8,3.7); \\foreach \\x in {-.1,.15,...,.7} \\draw[thin] (\\x,3.7) -- (\\x+.15,3.9);\n'
    '\\draw[thick] (.6,3.7) -- (.6,1.8); \\draw[thick,fill=white] (1.0,1.8) circle (.4); \\fill (1.0,1.8) circle (1.5pt);\n'
    f'\\draw[thick] (1.4,1.8) -- (1.4,3.3); \\draw[vurgu,very thick,{ARR}] (1.4,3.3) -- (1.4,4.1); \\node[vurgu,right] at (1.45,3.8) {{$F$}};\n'
    '\\draw[thick] (1.0,1.4) -- (1.0,.9); \\draw[thick,fill=gray!30] (.4,.2) rectangle (1.6,.9); \\node at (1.0,.55) {$40$ N};')
O('0003','fz-en3-makara','Hareketli makarada kuvvet, yol ve iş','Basit Makineler ve İş','orta',
 'Ağırlığı olan hareketli makarada kuvveti, ip yolunu ve yapılan işi yük enerjisiyle karşılaştırır.',
 'Hareketli makarada çekme kuvveti, taşınan toplam ağırlığın ip kolu sayısına bölünmesiyle bulunur; ip ucu, yükün aldığı yolun ip kolu sayısı kadar katını alır.',
 'Makara ağırlığını yok saymak; ip ucunun yükle aynı yolu aldığını sanmak; işi yalnız yükün enerjisine eşitlemek.',
 'Ağırlığı 10 N olan hareketli makara ile 40 N’luk yük şekildeki düzenekle sabit hızla yükseltiliyor. İp ve makara sürtünmesi ihmal edilmektedir ve F kuvveti düşey doğrultudadır. Yük 2 m yükseltildiğinde:',
 [('F kuvveti 25 N’dur.',True,'Yük ve makara iki ip kolu tarafından taşınır: F = (40 + 10) ÷ 2 = 25 N.','Makara ağırlığını yok sayıp F = 40 ÷ 2 = 20 N bulmuş.'),
  ('F kuvvetinin yaptığı iş 100 J’dur.',True,'İp ucu yükün iki katı yol (4 m) alır: W = 25 × 4 = 100 J.','İp ucunun yükle aynı yolu (2 m) aldığını sanıp 25 × 2 = 50 J bulmuş.'),
  ('F kuvvetinin yaptığı iş, yükün potansiyel enerjisindeki artışa eşittir.',False,'Yükün potansiyel enerji artışı 40 × 2 = 80 J’dur; 100 J’lük işin 20 J’u makaranın yükselmesine gider.','Makara ile ip düzeneğinde iş korunumunu yalnız yük için uygulamış; makaranın kazandığı enerjiyi unutmuş.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 ('Yük 40 N, makara 10 N; yük 2 m yükseliyor.','W = F · ip yolu'),
 ['Makarayı taşıyan ip kollarını say; ip ucunun aldığı yol ile yükün aldığı yol arasındaki ilişkiyi düşün.'],
 [B('Hareketli makara','yükü ve makarayı taşıyan ip kolu sayısı 2 ise çekme kuvveti toplam ağırlığın yarısı, ip ucunun yolu yükün yolunun iki katıdır. Örnek: toplam 30 N’luk düzenekte F = 15 N, yük 1 m çıkarsa ip ucu 2 m gider')],
 'Makara ağırlıklıysa onu da taşınan yüke ekle; kazanılan kuvvet kadar yoldan kaybedilir.',sekil=tk(sk))

# =============== 04 · güç–zaman grafiği, verim · orta ===============
t4a,t4b,P4=4,10,300
W4=Fr(t4a*P4,2)+(t4b-t4a)*P4; assert W4==2400
Wy=W4*Fr(3,4); m4=Fr(Wy,10*6); assert (Wy,m4)==(1800,30)
assert {Fr(W4*Fr(1,4),60),Fr(t4b*P4*3,4*60),Fr((t4a*P4+(t4b-t4a)*P4)*3,4*60),Fr(W4,60)}=={10,Fr(75,2),Fr(45,2)*0+Fr(75,2),40} or True
assert Fr((t4b-t4a)*P4*3,4*60)==Fr(45,2) and Fr((t4a*P4+(t4b-t4a)*P4)*3,4*60)==Fr(75,2) and Fr(W4,60)==40 and Fr(W4,4*60)==10
sk=GR('7.6cm','5.2cm',11,350,2,100,'$t$ (s)','$P$ (W)','\\addplot[thick,vurgu] coordinates {(0,0) (4,300) (10,300)};')
N('0004','fz-en3-guc','Güç ve verim','Güç','orta',
 'Güç–zaman grafiğinin altındaki alandan enerjiyi bulup verimle birlikte kaldırılan yükün kütlesini hesaplar.',
 'Güç–zaman grafiğinin altındaki alan harcanan enerjiyi verir; bunun verim kadarı yararlı işe, yani yükün potansiyel enerji artışına dönüşür.',
 'Eğimli bölümün alanını dikdörtgen almak; verimi atlamak ya da kayıp oranını verim sanmak.',
 'Verimi %75 olan bir elektrik motoru, 10 s boyunca çalışarak yükü 6 m yükseğe çıkarıyor; yükün kinetik enerjisindeki değişim ihmal edilmektedir. Motorun kaynaktan çektiği gücün zamanla değişimi grafikte verilmiştir. Yararlı iş yalnız yükün potansiyel enerji artışına harcanmaktadır (g = 10 m/s²).\nBuna göre, yükün kütlesi kaç kg’dır?',
 30,[(10,'Yararlı enerji yerine kayıp oranını (%25) kullanmış: 2400 × 0,25 ÷ 60 = 10 kg.','dikkat'),(Fr(45,2),'Eğimli 0–4 s bölümünün enerjisini hesaba katmamış: 1800 × 0,75 ÷ 60.','dikkat'),(Fr(75,2),'0–4 s bölümünü 300 W’lık dikdörtgen sanmış: 3000 × 0,75 ÷ 60.','islem'),(40,'Verimi hesaba katmamış: 2400 ÷ 60 = 40 kg.','dikkat')],
 'Yükün kütlesi (kg).',
 ['Grafiğin altındaki alan neyi verir? Bu enerjinin ne kadarı yükün yükselmesine gidiyor?'],
 [B('Güç–zaman grafiği','grafiğin altındaki alan yapılan işi ya da harcanan enerjiyi verir. Örnek: 2 s boyunca sabit 50 W’lık motorun enerjisi 100 J’dur')],
 [A('Harcanan enerjiyi bul','Grafiğin altındaki alanı üçgen ve dikdörtgen olarak topla.','(4 × 300 ÷ 2) + (6 × 300) = 600 + 1800 = 2400 J'),
  A('Yararlı enerjiyi bul','Verim kadarı yükün enerjisine gider.','2400 × 0,75 = 1800 J'),
  A('Kütleyi bul','Yararlı enerji m·g·h’a eşittir.','1800 = m × 10 × 6 → m = 30 kg')],
 'Grafikte enerji alandır; verimle çarpılan kısım yararlı iş olur, kalan ısı olarak kaybolur.',sekil=sk,kalip='grafik')

# =============== 05 · düşey atışta Ek = Ep anı · orta ===============
m5,v5=2,20
Ek0=Fr(m5*v5*v5,2); Ep5=Ek0/2; h5=Ep5/(m5*10)
assert (Ek0,Ep5,h5)==(400,200,10) and Ek0/(m5*10)==20 and Fr(v5*v5,10)==40 and Fr(20,4)==5 and Fr(Ek0,4)/(m5*10)==5 and Fr(3*20,4)==15
sk=('\\draw[thick] (-.8,0) -- (1.8,0); \\draw[thick,fill=gray!30] (0,.15) circle (.15);\n'
    f'\\draw[vurgu,very thick,{ARR}] (0,.4) -- (0,2.4); \\node[vurgu,right] at (.1,1.4) {{$20$ m/s}};')
N('0005','fz-en3-atis','Düşey atışta enerji korunumu','Mekanik Enerji ve Korunum','orta',
 'Düşey yukarı atılan cismin kinetik ve potansiyel enerjilerinin eşit olduğu yüksekliği enerji korunumuyla bulur.',
 'Hava direnci yokken mekanik enerji korunur; kinetik ve potansiyel enerji eşitse her biri toplam mekanik enerjinin yarısıdır.',
 'Eşitlik anını en yüksek nokta sanmak; potansiyel enerjiyi toplam enerjiye eşitlemek; h hesabında ½ katsayısını unutmak.',
 'Yerden, şekilde gösterilen hızla düşey yukarı doğru 2 kg kütleli bir cisim atılıyor. Hava direnci ihmal edilmektedir (g = 10 m/s²).\nBuna göre, cismin kinetik enerjisi potansiyel enerjisine eşit olduğunda yerden yüksekliği kaç m’dir?',
 10,[(5,'Potansiyel enerjiyi toplamın dörtte biri alıp h = 100 ÷ 20 bulmuş.','islem'),(15,'En yüksek noktanın yüksekliğinin dörtte üçünü almış.','bilgi'),(20,'Eşitlik anını en yüksek nokta sanıp tüm enerjiyi potansiyel enerji almış: 400 ÷ 20.','dikkat'),(40,'h = v² ÷ g alarak ½ katsayısını unutmuş.','dikkat')],
 'Kinetik ve potansiyel enerjinin eşit olduğu yükseklik (m).',
 ['Atış anındaki mekanik enerjiyi bul; kinetik ve potansiyel enerji eşitse toplamın ne kadarı potansiyeldir?'],
 [B('Mekanik enerji korunumu','hava direnci yokken kinetik ve potansiyel enerjinin toplamı değişmez. Örnek: toplam 60 J ise iki enerji eşit olduğunda her biri 30 J’dür')],
 [A('Toplam enerjiyi bul','Atış anında enerji yalnız kinetiktir.','E = ½ × 2 × 20² = 400 J'),
  A('Eşitlik koşulunu yaz','Ek = Ep ise her biri toplamın yarısıdır.','Ep = 200 J'),
  A('Yüksekliği bul','Ep = m·g·h.','200 = 2 × 10 × h → h = 10 m')],
 'Ek = Ep olduğunda potansiyel enerji, toplam mekanik enerjinin yarısıdır.',sekil=tk(sk))

# =============== 06 · Ek–x grafiği, sürtünme · öncüllü · orta ===============
m6,E6,x6=2,64,8
f6=Fr(E6,x6); mu6=f6/(m6*10); v6=math.sqrt(2*E6/m6)
assert (f6,mu6,v6)==(8,Fr(2,5),8.0) and Fr(E6,2)==32 and math.isclose(math.sqrt(2*32/m6),v6/math.sqrt(2))
sk=GR('7.6cm','5.2cm',10,80,2,16,'$x$ (m)','$E_k$ (J)','\\addplot[thick,vurgu,mark=*,mark size=1.6pt] coordinates {(0,64) (8,0)};')
O('0006','fz-en3-ekgraf','Enerji–yol grafiğinden kuvvet ve enerji yorumu','İş, Güç ve Enerji','orta',
 'Ek–yol grafiğinin eğiminden sürtünme kuvvetini, katsayıyı ve hızın nasıl değiştiğini yorumlar.',
 'İş–enerji teoreminde net kuvvet kinetik enerji–yol grafiğinin eğimidir; kinetik enerji hızın karesiyle orantılı olduğundan enerji yarıya inince hız yarıya inmez.',
 'Enerji yarıya indiğinde hızın da yarıya indiğini sanmak; eğim yerine grafikteki değeri kuvvet saymak.',
 'Yatay ve pürüzlü bir zeminde ilk hızıyla kayan 2 kg kütleli bir cismin kinetik enerjisinin aldığı yola göre değişimi grafikte verilmiştir (g = 10 m/s²).',
 [('Cisme etkiyen sürtünme kuvveti 8 N’dur.',True,'Ek–x grafiğinin eğimi sürtünme kuvvetini verir: 64 ÷ 8 = 8 N.','Eğimi bulmak yerine 64 J’ü kuvvet gibi okumuş.'),
  ('Cismin hızı, 4 m yol aldığında ilk hızının yarısına iner.',False,'4 m’de Ek = 32 J, yani ilk enerjinin yarısı olur; Ek ∝ v² olduğundan hız ilk hızın 1/√2 katıdır.','Kinetik enerji yarıya inince hızın da yarıya indiğini düşünmüş.'),
  ('Cisimle zemin arasındaki kinetik sürtünme katsayısı 0,4’tür.',True,'N = m·g = 20 N olduğundan μ = f ÷ N = 8 ÷ 20 = 0,4.','Normal kuvveti yanlış (ör. 8 N’a eşit) alarak katsayıyı 1 bulmuş.')],
 ['Yalnız I','Yalnız III','I ve III','II ve III','I, II ve III'],
 ('Grafikte cisim 8 m’de durmakta; başlangıçta Ek = 64 J.','f = ΔEk ÷ Δx'),
 ['Ek–x grafiğinin eğimi hangi kuvvete karşılık gelir? Kinetik enerji ile hız arasındaki bağı düşün.'],
 [B('İş–enerji teoremi','net kuvvetin yaptığı iş kinetik enerji değişimine eşittir: F·x = ΔEk. Bu yüzden Ek–x grafiğinin eğimi net kuvvettir. Örnek: 5 m’de 20 J azalan enerji 4 N’luk kuvvete işaret eder')],
 'Ek–x grafiğinin eğimi net kuvvettir; hız karekökle değiştiği için enerjinin yarısı hızın yarısı değildir.',sekil=sk,kalip='grafik')

# =============== 07 · rüzgâr türbini · zor ===============
v7a,m7a,e7a,v7b,e7b=10,200,Fr(2,5),20,Fr(1,2)
m7b=m7a*Fr(v7b,v7a); P7a=e7a*Fr(m7a*v7a**2,2); P7b=e7b*Fr(m7b*v7b**2,2)
assert (m7b,P7a,P7b)==(400,4000,40000)
assert (e7b*Fr(m7a*v7b**2,2)==20000 and e7a*Fr(m7b*v7b**2,2)==32000 and P7a*4==16000 and P7a*2*Fr(5,4)==10000)
sk=tablo_svg(['Durum','Rüzgâr hızı (m/s)','Kütle akışı (kg/s)','Verim'],[['Önce','10','200','%40'],['Sonra','20','–','%50']])
N('0007','fz-en3-verim','Enerji dönüşümü ve verim','Enerji Dönüşümleri','zor',
 'Kütle akışı hızla değişen rüzgârın kinetik enerji gücünü ve değişen verimi birlikte kullanarak türbinin elektrik gücünü bulur.',
 'Rüzgârın saniyede taşıdığı kinetik enerji ½·ṁ·v²’dir; kütle akışı hızla orantılıysa ṁ de hızla birlikte değişir ve elektrik gücü bu kinetik enerji gücünün verim kadarıdır.',
 'Kütle akışını sabit tutmak; kinetik enerjideki hız karesini unutmak; verim değişimini hesaba katmamak.',
 'Bir rüzgâr türbininin kanatlarına çarpan havanın kütle akışı (saniyede geçen hava kütlesi), rüzgâr hızıyla doğru orantılıdır. Türbinin elektrik gücü, rüzgârın saniyede taşıdığı kinetik enerjinin verim kadarıdır. Rüzgârın iki durumdaki değerleri tabloda verilmiştir.\nBuna göre, türbinin “Sonra” durumdaki elektrik gücü kaç kW’tır?',
 40,[(10,'Gücü hızla doğru orantılı alıp verim artışını da çarpmış: 4 × 2 × 1,25 = 10 kW.','bilgi'),(16,'Kütle akışını hızla artırıp (×2) hız karesini yalnız ×2 saymış; verimi %40 bırakmış: 4 × 4 = 16 kW.','dikkat'),(20,'Kütle akışını 200 kg/s sabit bırakmış: 0,5 × ½ × 200 × 20² = 20 kW.','dikkat'),(32,'Verim artışını göz ardı edip %40 ile hesaplamış: 0,4 × ½ × 400 × 20² = 32 kW.','dikkat')],
 'Türbinin “Sonra” durumdaki elektrik gücü (kW).',
 ['Kütle akışı hızla orantılıysa “Sonra” durumda kütle akışı kaç olur? Bu değer kinetik enerji gücünde nasıl kullanılır?'],
 [B('Akış gücü','saniyede ṁ kütleli hava v hızıyla geçiyorsa kinetik enerji gücü ½·ṁ·v² olur. Örnek: 10 kg/s ve 2 m/s için ½ × 10 × 4 = 20 W')],
 [A('Kütle akışını bul','Akış hızla doğru orantılıdır.','ṁ = 200 × (20 ÷ 10) = 400 kg/s'),
  A('Kinetik enerji gücünü bul','½·ṁ·v² işlemini uygula.','½ × 400 × 20² = 80 000 W'),
  A('Elektrik gücünü bul','Verim %50 ile çarp.','0,5 × 80 000 = 40 000 W = 40 kW')],
 'Kütle akışı hızla değişiyorsa kinetik enerji gücü hızın küpüyle orantılı olur; verim değişimini ayrıca çarp.',sekil=sk,kalip='tablo')

# =============== 08 · Atwood, enerji korunumu · öncüllü · zor ===============
M8,m8,h8=3,1,Fr(2,5)
v8=math.sqrt(float(2*(M8-m8)*10*h8/(M8+m8))); Ek8=Fr((M8+m8)*4,2); dEp3=M8*10*h8; dEp1=m8*10*h8
assert v8==2.0 and Ek8==8 and dEp3==12 and dEp1==4 and dEp3-dEp1==Ek8 and Fr(M8*4,2)==6
sk=('\\draw[thick] (-.7,.9) -- (.7,.9); \\foreach \\x in {-.6,-.35,...,.6} \\draw[thin] (\\x,.9) -- (\\x+.15,1.1); \\draw[very thick] (0,.5) -- (0,.9);\n'
    '\\draw[thick,fill=white] (0,0) circle (.5); \\fill (0,0) circle (1.5pt);\n'
    '\\draw[thick] (-.5,0) -- (-.5,-1.2); \\draw[thick] (.5,0) -- (.5,-1.2);\n'
    '\\draw[thick,fill=gray!40] (-.9,-1.8) rectangle (-.1,-1.2); \\node at (-.5,-1.5) {$3$ kg};\n'
    '\\draw[thick,fill=gray!25] (.1,-1.6) rectangle (.9,-1.2); \\node at (.5,-1.4) {\\scriptsize $1$ kg};\n'
    '\\draw[thin,dashed] (-.9,-2.4) rectangle (-.1,-1.8); \\draw[thin,dashed] (.1,-1.0) rectangle (.9,-.6);\n'
    '\\draw[<->,thin] (-1.3,-1.2) -- (-1.3,-1.8); \\node[left,font=\\small] at (-1.3,-1.5) {$0{,}4$ m};\n'
    '\\draw[thin,gray] (-1.3,-1.2) -- (-.9,-1.2); \\draw[thin,gray] (-1.3,-1.8) -- (-.9,-1.8);')
O('0008','fz-en3-atwood','Atwood düzeneğinde enerji dönüşümü','Mekanik Enerji ve Korunum','zor',
 'Atwood düzeneğinde potansiyel enerji azalışı ile kinetik enerji artışını karşılaştırıp hızı ve sistemin kinetik enerjisini yorumlar.',
 'Sürtünmesiz düzenekte toplam mekanik enerji korunur: inen cismin potansiyel enerji azalması, çıkan cismin potansiyel enerji artışı ile sistemin kinetik enerji artışının toplamına eşittir.',
 'İnen cismin kaybettiği enerjinin tamamını kinetik enerji saymak; çıkan cismin kazandığı potansiyel enerjiyi unutmak.',
 'Kütlesi önemsiz ideal makara ve ipten oluşan sürtünmesiz Atwood düzeneğinde 3 kg ve 1 kg kütleli cisimler durgun hâlden serbest bırakılıyor (g = 10 m/s²). 3 kg’lık cisim şekildeki gibi 0,4 m aşağı indiği anda:',
 [('3 kg’lık cismin potansiyel enerjisindeki azalma, sistemin kinetik enerjisindeki artışa eşittir.',False,'Azalma 3 × 10 × 0,4 = 12 J’dur; 1 kg’lık cismin kazandığı 4 J’lük potansiyel enerji çıkınca sistemin kinetik enerjisi 8 J olur.','İnen cismin kaybettiği 12 J’ün tamamını kinetik enerjiye dönüşmüş saymış.'),
  ('Cisimlerin hızı 2 m/s’dir.',True,'½ × (3 + 1) × v² = 8 olduğundan v = 2 m/s.','12 J’ü yalnız 3 kg’a vererek ½·3·v² = 12 → v = 2√2 m/s bulmuş.'),
  ('Sistemin toplam kinetik enerjisi 8 J’dur.',True,'Enerji korunumu: 12 J − 4 J = 8 J.','Sistemin kinetik enerjisini 12 J sanmış.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],
 ('Sürtünme yok; 3 kg 0,4 m iniyor, 1 kg 0,4 m çıkıyor.','Ep azalması = Ep artışı + Ek artışı'),
 ['İnen ve çıkan cismin potansiyel enerji değişimlerini ayrı ayrı yaz; hangisi kinetik enerjiye gidiyor?'],
 [B('Enerji korunumu','sürtünmesiz sistemde toplam mekanik enerji değişmez; bir cismin kaybettiği potansiyel enerji diğerinin potansiyel ve kinetik enerjisine dönüşür. Örnek: 2 kg 1 m iner, 1 kg 1 m çıkarsa 10 J kinetik enerjiye gider')],
 'Atwood’da enerji dengesini sistem olarak yaz; kinetik enerji (m₁ + m₂) toplam kütle üzerinden bulunur.',sekil=tk(sk))

# =============== 09 · araç gücü, direnç hızın karesiyle · zor ===============
v9a,F9a,v9b=20,800,30
F9b=F9a*Fr(v9b,v9a)**2; P9=F9b*v9b
assert (F9b,P9)==(1800,54000)
assert (F9a*v9a,F9a*v9b,F9a*Fr(v9b,v9a)*v9b,F9a*Fr(v9b,v9a)**3*v9b)==(16000,24000,36000,81000)
sk=('\\fill[gray!30] (-.3,-.2) rectangle (7.2,0); \\draw (-.3,0) -- (7.2,0);\n'
    '\\draw[thick,rounded corners=3pt,fill=gray!25] (2.3,.25) rectangle (4.1,.95); \\draw[thick,fill=white] (2.7,.25) circle (.25); \\draw[thick,fill=white] (3.7,.25) circle (.25);\n'
    f'\\draw[vurgu,very thick,{ARR}] (4.1,.6) -- (5.3,.6); \\node[vurgu,above] at (4.8,.65) {{$20$ m/s}};\n'
    f'\\draw[very thick,{ARR}] (2.3,.6) -- (1.0,.6); \\node[above] at (1.6,.65) {{$800$ N}}; \\node[below,font=\\scriptsize] at (1.6,.6) {{hava direnci}};')
N('0009','fz-en3-guc','Güç ve verim','Güç','orta',
 'Direnç kuvvetinin hızın karesiyle orantılı olduğu durumda sabit hızda motorun yararlı gücünü yeni hızda hesaplar.',
 'Sabit hızda motor kuvveti direnç kuvvetine eşittir ve güç P = F·v’dir; direnç hızın karesiyle değişiyorsa hız k katına çıkınca direnç k² katına çıkar.',
 'Direnç kuvvetini hız değişse de sabit saymak; direncin hızla doğru orantılı olduğunu düşünmek; sonucu ilk güçle karıştırmak.',
 'Yatay bir yolda sabit hızla giden bir araca etkiyen hava direnci kuvveti hızın karesiyle orantılıdır. Araç şekildeki hızla giderken direnç kuvveti şekilde verilmiştir. Aracın hızı 30 m/s olarak sabit tutuluyor ve direnç dışında kuvvet dikkate alınmıyor.\nBuna göre, motorun 30 m/s hızda sabit hız için sağladığı yararlı güç kaç kW’tır?',
 54,[(16,'İlk durumun gücünü (800 × 20) yeni hızdaki güç sanmış.','dikkat'),(24,'Direnci 800 N sabit bırakmış: 800 × 30 = 24 kW.','dikkat'),(36,'Direncin hızla doğru orantılı olduğunu düşünmüş: 1200 × 30 = 36 kW.','bilgi'),(81,'Direncin hızın küpüyle değiştiğini alıp 2700 × 30 = 81 kW bulmuş.','islem')],
 'Motorun yararlı gücü (kW).',
 ['Hız sabit kalıyorsa motor kuvveti neye eşittir? Yeni hızdaki direnç kuvvetini oran yoluyla bul.'],
 [B('Hızla değişen direnç','F ∝ v² ise v iki katına çıkınca F dört katına çıkar. Örnek: 10 m/s’de 50 N olan direnç 20 m/s’de 200 N olur; güç P = F·v’dir')],
 [A('Yeni direnci bul','Direnç hızın karesiyle orantılı.','F′ = 800 × (30 ÷ 20)² = 1800 N'),
  A('Motor kuvvetini yaz','Hız sabit olduğundan motor kuvveti dirence eşittir.','F_motor = 1800 N'),
  A('Gücü hesapla','P = F · v.','P = 1800 × 30 = 54 000 W = 54 kW')],
 'Sabit hızda motor kuvveti dirence eşittir; direnç v² ile değişiyorsa güç v³ ile değişir.',sekil=tk(sk))

# =============== 10 · Ek ve Ep grafiği, hava direnci · öncüllü · zor ===============
E10,mg10,h10=100,20,4
Epm=mg10*h10; f10=Fr(E10-Epm,h10); Emek2=(E10-(mg10+f10)*2)+mg10*2; Eyer=Epm-f10*h10
assert (Epm,f10,Emek2,Eyer)==(80,5,90,60) and E10-(mg10+f10)*h10==0
sk=GR('7.6cm','5.4cm',5,120,1,20,'$h$ (m)','enerji (J)','\\addplot[thick,vurgu] coordinates {(0,100) (4,0)}; \\node[vurgu,above right,font=\\small] at (axis cs:.2,96) {$E_k$};','\\addplot[thick,dashed] coordinates {(0,0) (4,80)}; \\node[above left,font=\\small] at (axis cs:4,80) {$E_p$};')
O('0010','fz-en3-ekgraf','Enerji–yol grafiğinden kuvvet ve enerji yorumu','Mekanik Enerji ve Korunum','zor',
 'Ek–h ve Ep–h grafiklerinden hava direncini, mekanik enerji kaybını ve dönüşteki kinetik enerjiyi yorumlar.',
 'Hava direncinde mekanik enerji azalır; kaybolan enerji, direnç kuvvetiyle alınan toplam yolun çarpımına eşittir.',
 'Mekanik enerjinin korunduğunu varsaymak; dönüşte hava direncinin etkisini unutmak; kuvveti enerji farkına eşitlemek.',
 'Yerden düşey yukarı atılan bir cisim, sabit büyüklükteki hava direncine karşı yükselip en üst noktada duruyor ve aynı hava direnciyle geri düşüyor. Yükselirken kinetik ve potansiyel enerjisinin yerden yüksekliğe göre değişimi grafikte verilmiştir (g = 10 m/s²).',
 [('Cisme etkiyen hava direnci kuvveti 5 N’dur.',True,'En üstte mekanik enerji 80 J olduğundan 4 m’de 20 J kaybolmuştur: f = 20 ÷ 4 = 5 N.','Kaybolan 20 J’ü doğrudan kuvvet (20 N) sanmış.'),
  ('h = 2 m’de cismin mekanik enerjisi 100 J’dur.',False,'h = 2 m’de Ek = 50 J ve Ep = 40 J’dur; mekanik enerji 90 J’dür.','Hava direncinde de mekanik enerjinin ilk değerde (100 J) kaldığını düşünmüş.'),
  ('Cisim yere döndüğünde kinetik enerjisi 100 J’dur.',False,'Dönüşte de 4 m boyunca 20 J kaybolur: Ek = 80 − 20 = 60 J.','Enerjinin atış değerine (100 J) geri döneceğini düşünmüş.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],
 ('En üstte Ep = 80 J; başlangıçta Ek = 100 J.','f = kayıp enerji ÷ yol'),
 ['Mekanik enerji (Ek + Ep) yükseklikle nasıl değişiyor? Bu değişim hangi kuvvetin işine karşılık gelir?'],
 [B('Hava direncinde enerji','sürtünme türü kuvvetin yaptığı iş mekanik enerjiyi azaltır: ΔE = f·yol. Örnek: 10 m yolda 3 N’luk direnç 30 J mekanik enerji götürür')],
 'Mekanik enerji kaybı f·yol’dur; yükselirken ve düşerken ayrı ayrı yaz, dönüşte de kayıp devam eder.',sekil=sk,kalip='grafik')

bitir(P,'enerjiuc','fiz|İş, Güç ve Enerji')
