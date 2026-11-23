"""AYT Fizik · İndüksiyon, Alternatif Akım ve Transformatörler · 20 soru. Kardeş yok, ipucu 1.
Şekil verileri betikteki aynı sayılardan üretilir; her cevap ve çeldirici assert edilir."""
import sys,os,json
from fractions import Fraction as Fr
from math import sqrt
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
KONU_AD='İndüksiyon, Alternatif Akım ve Transformatörler'; KEY='afiz|İndüksiyon, Alternatif Akım ve Transformatörler'
P=Parti('induksiyon',KONU_AD,KEY,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Fizik indüksiyon, alternatif akım ve transformatör soruları (yalnız mantık) · 345 AYT Fizik s.220–249 · Bilgi Sarmal AYT denemeleri'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
def q(no,ad,**k):
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),**k)

def tk(body,opt=''): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small'+opt+']\n'+body+'\n\\end{tikzpicture}')
AK='blue!65!black'
def f1(items): return '\n'.join(items)
def V(p,q_,lab='',side='above',col='vurgu'):
    n=f' node[midway,{side},fill=white,inner sep=1pt] {{{lab}}}' if lab else ''
    return '\\draw[%s,very thick,-{Stealth[length=2mm,width=1.8mm]}] (%.3f,%.3f) -- (%.3f,%.3f)%s;'%(col,p[0],p[1],q_[0],q_[1],n)
def dim(p,q_,lab,side='left'): return '\\draw[<->,thin] (%.3f,%.3f) -- (%.3f,%.3f) node[midway,%s,fill=white,inner sep=1pt] {%s};'%(p[0],p[1],q_[0],q_[1],side,lab)
def crosses(x0,y0,x1,y1,dx=.6,dy=.6):
    s=[];x=x0
    while x<=x1+1e-9:
        y=y0
        while y<=y1+1e-9: s.append('\\node[gray] at (%.2f,%.2f) {$\\times$};'%(x,y)); y+=dy
        x+=dx
    return ''.join(s)
def sin_graph(ylab,ymax_lab,T_lab,ymax=1.2):
    head='\\begin{axis}[width=7.6cm,height=4.6cm,axis lines=middle,clip mode=individual,xlabel={$t$ (s)},ylabel={%s},xmin=0,xmax=2.15,ymin=-%s,ymax=%s,xtick={0.5,1,1.5,2},xticklabels={,,,},ytick={-1,1},yticklabels={$-%s$,$%s$},grid=major,grid style={gray!30},tick label style={font=\\small},label style={font=\\small},xlabel style={at={(ticklabel* cs:1.0)},anchor=north west},ylabel style={at={(ticklabel* cs:1.0)},anchor=south west}]\n'%(ylab,ymax,ymax,ymax_lab,ymax_lab)
    pl='\\addplot[vurgu,very thick,domain=0:2,samples=90] {sin(360*x)};\n'
    nd=''.join('\\node[below,font=\\small] at (axis cs:%s,-%s) {$%s$};'%(xx,ymax,tt) for xx,tt in zip((0.5,1,1.5,2),T_lab.split(',,')))
    return tk(head+pl+nd+'\\end{axis}')

ROM=['I','II','III']
COMB=[('Yalnız I',{0}),('Yalnız II',{1}),('Yalnız III',{2}),('I ve II',{0,1}),('I ve III',{0,2}),('II ve III',{1,2}),('I, II ve III',{0,1,2})]
def onc(no,hedef,giris,stm,ip,bilgi,puf,istenen,tipId,tip,z,alt,kaz,kart,kalip,sekil=None,kok='yargılarından hangileri doğrudur?'):
    """stm: [(metin, doğru_mu, gerekçe, tuzak)]. Doğrulukların tek kaynağı burası."""
    T={i for i,s in enumerate(stm) if s[1]}
    idx=[i for i,(a,b) in enumerate(COMB) if b==T]; assert len(idx)==1; ci=idx[0]; p='ABCDE'.index(hedef)
    assert p<=ci and 4-p<=6-ci,(no,ci,p)
    win=COMB[ci-p:ci-p+5]; assert len(win)==5 and win[p][1]==T
    yan=[]
    for a,b in win:
        if b==T: continue
        d=sorted(b^T)
        yan.append((a,' '.join(stm[i][3] for i in d),'bilgi'))
    metin=giris+'\nBuna göre,\n'+'\n'.join(f'{ROM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+kok
    ad=[A(f'{ROM[i]}. yargıyı incele',s[2],f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış')) for i,s in enumerate(stm)]
    ad.append(A('Sonucu yaz','Doğru olan yargıları birleştir.',' · '.join(f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış') for i,s in enumerate(stm))+' → '+COMB[ci][0]))
    q(no,ad,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kart=kart,kalip=kalip,metin=metin,dogru=COMB[ci][0],yan=yan,sira=[a for a,b in win],
      istenen=istenen,ip=ip,bilgi=bilgi,puf=puf,sekil=sekil)

# ================= KARTLAR =================
kartla('K-AFIND-01','Manyetik akı ve açı','Φ = B·A·cosθ; θ yüzey normali ile alan arasındaki açıdır, alan çizgisi ile düzlem arasındaki açı verilmişse sinüs kullanılır.','Düzlemle yapılan açıyı normalle yapılmış gibi almak; açıyı hiç hesaba katmamak.','kolay','şekilli',3,'ind-aki','Manyetik akı hesabı ve açı')
kartla('K-AFIND-02','Lenz yasası: mıknatıs ve bobin','İndüklenen akım, kendisini doğuran akı değişimine karşı koyar; akı artarken zıt, azalırken aynı yönlü alan oluşur. Akı değişmiyorsa emk yoktur, değişim hızı arttıkça emk büyür.','Bobinin mıknatısı çekeceğini sanmak; sabit akıda da akım beklemek.','orta','şekilli',4,'ind-lenz','Lenz yasası ve indüksiyon akımının yönü')
kartla('K-AFIND-03','Faraday yasası: Φ–t ve B–t grafikleri','ε = −N·ΔΦ/Δt; grafikte eğim emk’yı verir. B–t grafiğinde ε = A·ΔB/Δt, dirençteki ısı Q = ε²·t/R.','Sarım sayısını ya da süreyi katmamak; eğim yerine değer okumak; yükü ısı sanmak.','orta','grafik',4,'ind-faraday','Faraday yasası ve grafik yorumu')
kartla('K-AFIND-04','Hareketli iletken ve raylar','ε = B·ℓ·v; i = ε/R; sabit hız için F = B·i·ℓ = B²ℓ²v/R. Sınır hızda uygulanan kuvvetin gücü dirençteki ısıl güce eşittir. Çerçeve alana girerken ve çıkarken akım vardır, tamamen içindeyken yoktur.','ℓ ya da B’yi karesiz almak; akımı kuvvet sanmak; alan içindeki çerçevede de akım beklemek.','orta','şekilli',4,'ind-hareketli','Hareketli iletken, emk ve manyetik kuvvet')
kartla('K-AFIND-05','Öz-indüksiyon','ε = L·Δi/Δt; i–t grafiğinde emk eğimle orantılıdır. Akım değişmeyince emk sıfırdır; bobinde depolanan enerji E = ½·L·i²’dir.','Emk’yı L ile çarpmadan eğim sanmak; ortalama değişim hızını kullanmak; enerjide ½ ve kareyi unutmak.','orta','grafik',4,'ind-oz','Öz-indüksiyon emk’sı ve RL devresi')
kartla('K-AFIND-06','Alternatif akım: etkin değer ve üretim','V_etkin = V_maks/√2, i_etkin = i_maks/√2; ısı ve güç etkin değerlerle bulunur. Döner çerçevede akı en büyükken emk sıfır, düzlem alana paralelken emk en büyüktür.','Maksimum değerle ısı hesaplamak; grafikten tepeden tepeye değeri okumak; akı ile emk’nın aynı anda en büyük olduğunu sanmak.','orta','grafik',3,'ac-etkin','Alternatif akımın etkin değeri ve üretimi')
kartla('K-AFIND-07','RLC devresi: reaktans, empedans, rezonans','X_L = ωL, X_C = 1/(ωC), Z = √(R² + (X_L − X_C)²). Rezonansta X_L = X_C, Z = R, akım en büyüktür; bobin ve sığaç gerilimleri kaynak gerilimini aşabilir.','Direnç ve reaktansları cebirsel toplamak; rezonansta bobin gerilimini kaynak gerilimine eşit sanmak.','zor','şekilli',4,'ac-rlc','RLC devresi: reaktans, empedans ve rezonans')
kartla('K-AFIND-08','Transformatör ve enerji iletimi','V_p/V_s = N_p/N_s; ideal trafoda P_p = P_s, akımlar sarım sayılarıyla ters orantılıdır; verim = P_s/P_p. İletimde gerilim yükseltilince hat akımı ve I²R kaybı azalır.','Akımı da gerilim gibi dönüştürmek; verimi unutmak; kaybı P = V²/R ya da gerilimle hesaplamak.','orta','şekilli',4,'tr-trafo','Transformatör ve enerji iletimi')

# ============== SORULAR ==============
# ---- 01 kolay · akı ve açı ----
B1,A1=Fr(4,10),Fr(1,10); phi1=B1*A1*Fr(1,2); assert phi1==Fr(2,100) and B1*A1==Fr(4,100) and B1*A1*Fr(1,4)==Fr(1,100)
import math
c30=math.cos(math.radians(30)); assert abs(0.04*c30-0.02*sqrt(3))<1e-12
th=30; c=math.cos(math.radians(th)); s=math.sin(math.radians(th))
def Bl(x0): return '\\draw[AKX,very thick,-{Stealth[length=2mm,width=1.8mm]}] (%.3f,%.3f) -- (%.3f,%.3f);'%(x0-1.3*c,-1.3*s,x0+1.3*c,1.3*s)
SK=tk('\\colorlet{AKX}{blue!65!black}\n'+f1([Bl(x0) for x0 in (.6,1.6,2.6,3.6)])+'\\draw[very thick] (0,0) -- (4.3,0);\\node[right] at (4.4,-.3) {Çerçeve};\\node[right] at (4.4,-.75) {$A=0{,}1\\ \\mathrm{m^2}$};'
  '\\draw[thick] (4.05,0) arc (0:30:.45);\\node[right] at (4.3,.16) {$30^\\circ$};\\node[AKX,fill=white,inner sep=1pt,text=blue!65!black] at (0.1,1.25) {$B=0{,}4$ T};')
q('0001',[A('Açıyı normale çevir','Akı formülündeki açı yüzey normali ile alan arasındadır; düzlemle 30° ise normalle 60° yapar.','θ = 90° − 30° = 60°'),
  A('Akı formülünü yaz','Alan çizgilerine dik bileşen akıyı oluşturur.','Φ = B × A × cos60° = B × A × sin30°'),
  A('Değerleri yerleştir','sin30° = 0,5 alınır.','Φ = 0,4 × 0,1 × 0,5 = 0,02 Wb')],
 tipId='ind-aki',tip='Manyetik akı hesabı ve açı',z='kolay',alt='Manyetik Akı',kaz='Alan çizgisi ile düzlem arasındaki açı verildiğinde manyetik akıyı hesaplar.',
 kart='K-AFIND-01 (düzlem–alan açısı) · yan görünüşlü çerçeve',kalip='şekilli',
 metin='Yan görünüşü şekilde verilen düz bir iletken çerçeve, düzgün bir manyetik alan içindedir. Çerçevenin alanı ve manyetik alan şiddeti şekilde gösterilmiştir.\n(sin 30° = 0,5 ; cos 30° = √3/2 alınız.)\nBuna göre, çerçeveden geçen manyetik akı kaç Wb’dir?',
 dogru='0,02',yan=[('0,01','Sinüsü iki kez çarpmış: 0,4 × 0,1 × 0,5 × 0,5 = 0,01.','islem'),('0,02√3','Açıyı normalle yapılmış gibi alıp cos30° kullanmış: 0,4 × 0,1 × √3/2 = 0,02√3.','bilgi'),('0,04','Açıyı hiç hesaba katmamış: Φ = B × A = 0,04.','dikkat'),('0,4','Manyetik alan şiddetini (0,4) akı sanmış.','bilgi')],
 sira=['0,01','0,02','0,02√3','0,04','0,4'],
 istenen='Çerçeveden geçen manyetik akı (Wb).',ip=['Akıyı oluşturan, alanın yüzeye dik bileşenidir; verilen açının hangi iki doğru arasında olduğuna dikkat et.'],
 bilgi=[B('Manyetik akı','Φ = B·A·cosθ, θ alan ile yüzey normali arasındaki açıdır. Alan düzlemle α açısı yapıyorsa Φ = B·A·sinα. Örnek: alan düzleme paralel ise akı sıfırdır')],
 puf='Akıyı, alanın yüzeye dik bileşeni belirler.',sekil=SK)

# ---- 02 kolay · Lenz öncüllü ----
magnet=('\\draw[thick,fill=blue!15] (0,0) rectangle (1.2,.8);\\draw[thick,fill=red!20] (1.2,0) rectangle (2.4,.8);\\node at (.6,.4) {S};\\node at (1.8,.4) {N};'
  +V((.3,1.2),(1.5,1.2),'$v$','above'))
coil=''.join('\\draw[thick] (%.2f,.4) ellipse (.16 and .55);'%x for x in (4.0,4.3,4.6,4.9,5.2))
SK=tk(f1([magnet,coil,'\\draw[thick] (4.0,-.15) -- (4.0,-1.2) -- (4.3,-1.2);\\draw[thick] (4.6,-1.2) -- (5.2,-1.2) -- (5.2,-.15);\\draw[thick,fill=white] (4.45,-1.2) circle (.17);\\node at (4.45,-1.2) {\\scriptsize G};']))
onc('0002','E','Bir mıknatıs, ucu galvanometreye bağlı bir bobine şekildeki gibi sabit hızla yaklaştırılmaktadır.',
 [('Bobinin mıknatısa bakan ucu, N kutbu gibi davranır.',True,'Bobinden geçen akı artar; Lenz yasasına göre bobin bu artışa karşı çıkacak alan oluşturur ve mıknatısa bakan ucu N kutbu gibi davranarak onu iter.','I numaralı yargıda bobinin mıknatısı çekeceğini düşünmüş.'),
  ('Mıknatıs bobinin önünde hareketsiz tutulursa galvanometreden akım geçmeye devam eder.',False,'Mıknatıs durunca bobinden geçen akı değişmez; emk oluşmaz ve akım sıfırlanır.','II numaralı yargıda güçlü bir alanın tek başına akım oluşturduğunu düşünmüş.'),
  ('Mıknatıs aynı yönde daha hızlı yaklaştırılırsa galvanometreden geçen akımın en büyük değeri artar.',True,'Akı daha çabuk değişir; ε = N·ΔΦ/Δt büyür ve akım artar.','III numaralı yargıda hızın emk’yı etkilemediğini düşünmüş.')],
 ['Her yargıda bobinden geçen akının değişip değişmediğine bak.'],
 [B('Lenz yasası','İndüksiyon akımı, kendisini oluşturan akı değişimine karşı koyacak yöndedir. Akı artıyorsa zıt yönlü, azalıyorsa aynı yönlü alan oluşur. Örnek: bir halkaya yaklaşan N kutbu itilir, uzaklaşan N kutbu çekilir')],
 'İndüksiyon emk’sı akının değerine değil, değişim hızına bağlıdır.','Doğru olan yargılar.','ind-lenz','Lenz yasası ve indüksiyon akımının yönü','kolay','Lenz Yasası','Mıknatıs ve bobin düzeneğinde indüksiyon akımının yönü ve büyüklüğüyle ilgili yargıları değerlendirir.','K-AFIND-02 (mıknatıs–bobin) · nitel öncüllü','şekilli',sekil=SK)

# ---- 03 kolay · etkin değer ----
Vm3=Fr(100); R3=25; Ve3=Vm3; i3=Fr(Ve3,R3); assert i3==4 and Fr(Ve3,2)/R3==2 and Fr(2*Ve3,R3)==8
SK=sin_graph('$V$ (volt)','100\\sqrt{2}','0{,}005,,0{,}01,,0{,}015,,0{,}02')
q('0003',[A('Maksimum gerilimi oku','Grafikte tepe noktası maksimum gerilimi verir.','V_maks = 100√2 V'),
  A('Etkin değere geç','Etkin değer maksimum değerin √2’ye bölünmesiyle bulunur.','V_etkin = 100√2 ÷ √2 = 100 V'),
  A('Akımı hesapla','Saf dirençte etkin değerler arasında Ohm yasası geçerlidir.','i_etkin = 100 ÷ 25 = 4 A')],
 tipId='ac-etkin',tip='Alternatif akımın etkin değeri ve üretimi',z='kolay',alt='Alternatif Akım',kaz='Gerilim–zaman grafiğinden etkin değeri bulup dirençteki etkin akımı hesaplar.',
 kart='K-AFIND-06 (gerilim grafiği, saf direnç) · etkin akım',kalip='grafik',
 metin='Bir alternatif akım kaynağının uçları arasındaki gerilimin zamanla değişimi şekilde verilmiştir. Kaynak, direnci 25 Ω olan saf bir dirence bağlanmıştır.\nBuna göre, dirençten geçen akımın etkin değeri kaç A’dır?',
 dogru='4',yan=[('2','Etkin gerilimi 2’ye bölüp dirence bölmüş: (100 ÷ 2) ÷ 25 = 2.','islem'),('4√2','Maksimum gerilimi dirence bölerek maksimum akımı bulmuş: 100√2 ÷ 25 = 4√2.','bilgi'),('8','Etkin gerilimin iki katını dirence bölmüş: 200 ÷ 25 = 8.','islem'),('8√2','Grafikte tepeden tepeye gerilimi alıp dirence bölmüş: 200√2 ÷ 25 = 8√2.','dikkat')],
 sira=['2','4','4√2','8','8√2'],
 istenen='Dirençten geçen akımın etkin değeri (A).',ip=['Ampermetrelerin ve Ohm yasasının kullandığı değer, grafikteki tepe değeri değil etkin değerdir.'],
 bilgi=[B('Etkin değer','V_etkin = V_maks/√2 ve i_etkin = i_maks/√2’dir. Etkin değer, aynı dirençte aynı ısıyı açığa çıkaran doğru akım değeridir. Örnek: tepe değeri 10√2 V olan gerilimin etkin değeri 10 V’tur')],
 puf='Alternatif akımda Ohm yasası etkin değerlerle (ya da maksimum değerlerle) kendi içinde kullanılır, karıştırılmaz.',sekil=SK)

# ---- 04 orta · Φ–t grafiği ----
N4=100; Phi4=[(0,0),(2,Fr(8,100)),(4,Fr(8,100)),(6,Fr(-4,100))]
e4=Fr(N4)*abs(Phi4[3][1]-Phi4[2][1])/(6-4); assert e4==6 and Fr(abs(Phi4[3][1]-Phi4[2][1]),2)==Fr(6,100) and N4*Fr(4,100)/2==2 and N4*Fr(8,100)/2==4 and N4*Fr(12,100)==12
SK=tk('\\begin{axis}[width=7.4cm,height=5.0cm,axis lines=middle,xticklabel pos=lower,xlabel={$t$ (s)},ylabel={$\\Phi$ (Wb)},xmin=0,xmax=6.6,ymin=-0.07,ymax=0.1,xtick={1,2,3,4,5,6},ytick={-0.04,0.04,0.08},yticklabels={$-0{,}04$,$0{,}04$,$0{,}08$},grid=major,grid style={gray!30},tick label style={font=\\small},label style={font=\\small},xlabel style={at={(ticklabel* cs:1.0)},anchor=north west},ylabel style={at={(ticklabel* cs:1.0)},anchor=south west}]\n\\addplot[vurgu,very thick] coordinates {(0,0) (2,0.08) (4,0.08) (6,-0.04)};\n\\end{axis}')
q('0004',[A('Akı değişimini bul','4. ve 6. saniyedeki akı değerleri arasındaki fark alınır; işaret değişimi farkı büyütür.','ΔΦ = −0,04 − 0,08 = −0,12 Wb'),
  A('Zaman aralığını yaz','Aralık 4 s ile 6 s arasıdır.','Δt = 6 − 4 = 2 s'),A('Faraday yasasını uygula','Emk büyüklüğü sarım sayısı × akı değişim hızıdır.','ε = N × |ΔΦ| ÷ Δt = 100 × 0,12 ÷ 2 = 6 V')],
 tipId='ind-faraday',tip='Faraday yasası ve grafik yorumu',z='orta',alt='Faraday Yasası',kaz='Akı–zaman grafiğinden belirli aralıktaki indüksiyon emk’sını hesaplar.',
 kart='K-AFIND-03 (Φ–t, işaret değiştiren aralık) · sarım sayısı 100',kalip='grafik',
 metin='Sarım sayısı 100 olan bir bobinin içinden geçen manyetik akının zamanla değişimi şekildeki grafikte verilmiştir.\nBuna göre, bobinde 4–6 s aralığında oluşan indüksiyon emk’sının büyüklüğü kaç V’tur?',
 dogru=6,yan=[(Fr(6,100),'Sarım sayısını katmamış: 0,12 ÷ 2 = 0,06.','dikkat'),(2,'Akı değişimini yalnız son değerle (0,04 Wb) hesaplamış: 100 × 0,04 ÷ 2 = 2.','dikkat'),(4,'Aralığı yanlış okuyup 0–2 s’yi almış: 100 × 0,08 ÷ 2 = 4.','dikkat'),(12,'Süreye bölmeyi unutmuş: 100 × 0,12 = 12.','islem')],
 istenen='4–6 s aralığındaki emk’nın büyüklüğü (V).',ip=['Emk, akının değişimine bağlıdır; sorulan aralığın başındaki ve sonundaki akı değerlerini oku.'],
 bilgi=[B('Faraday yasası','ε = −N·ΔΦ/Δt; emk, akı–zaman grafiğinin eğimiyle sarım sayısının çarpımıdır. Örnek: 5 sarımlı bobinde akı 2 s’de 0,6 Wb artarsa emk büyüklüğü 5 × 0,6 ÷ 2 = 1,5 V’tur')],
 puf='Φ–t grafiğinde eğim ne kadar dikse emk o kadar büyüktür; sabit akıda emk sıfırdır.',sekil=SK)

# ---- 05 orta · raylar üzerinde çubuk, kuvvet ----
B5,l5,v5,R5=Fr(1,2),Fr(2,5),5,2
e5=B5*l5*v5; i5=e5/R5; F5=B5*i5*l5; assert (e5,i5,F5)==(1,Fr(1,2),Fr(1,10)) and B5**2*l5**2*v5==Fr(1,5) and B5**2*l5*v5/R5==Fr(1,4)
SK=tk(f1(['\\draw[thick] (0,1.8) -- (5.2,1.8);\\draw[thick] (0,0) -- (5.2,0);\\draw[thick] (0,1.8) to[R=$2\\,\\Omega$] (0,0);','\\draw[very thick] (3.0,-.2) -- (3.0,2.0);',crosses(1.0,.4,2.6,1.4,.8,.5)+crosses(3.6,.4,4.8,1.4,.6,.5),
  '\\node[gray] at (2.6,-.6) {$B=0{,}5$ T (sayfadan içe)};',dim((5.5,0),(5.5,1.8),'$\\ell=0{,}4$ m','right'),V((3.0,2.25),(4.2,2.25),'$v=5$ m/s','above')]))
q('0005',[A('Emk’yı bul','Hareketli iletkende emk, B ℓ v ile bulunur.','ε = 0,5 × 0,4 × 5 = 1 V'),A('Akımı bul','Devre kapalıdır; Ohm yasası uygulanır.','i = ε ÷ R = 1 ÷ 2 = 0,5 A'),
  A('Manyetik kuvveti hesapla','Akım taşıyan çubuğa alan kuvvet uygular; sabit hız için çekme kuvveti buna eşit ve zıt olur.','F = B × i × ℓ = 0,5 × 0,5 × 0,4 = 0,1 N')],
 tipId='ind-hareketli',tip='Hareketli iletken, emk ve manyetik kuvvet',z='orta',alt='Hareketli İletken',kaz='Raylar üzerindeki çubuğun emk’sını, akımını ve sabit hız için gereken kuvveti hesaplar.',
 kart='K-AFIND-04 (ray ve çubuk) · sabit hız için kuvvet',kalip='şekilli',
 metin='Sürtünmesiz, yatay ve paralel iletken raylar üzerinde, raylara dik duran bir iletken çubuk dışarıdan çekilerek sabit hızla hareket ettirilmektedir. Raylar düzlemine dik, içeri yönlü düzgün bir manyetik alan vardır. Çubuğun ve rayların direnci önemsizdir; şekildeki değerler verilmiştir.\nBuna göre, çubuğu sabit hızla çekmek için uygulanması gereken kuvvetin büyüklüğü kaç N’dir?',
 dogru=F5,yan=[(Fr(1,5),'B²ℓ²v ifadesini bulup dirence bölmeyi unutmuş: 0,25 × 0,16 × 5 = 0,2.','islem'),(Fr(1,4),'ℓ’yi karesiz almış: B²ℓv ÷ R = 0,25 × 0,4 × 5 ÷ 2 = 0,25.','islem'),(Fr(1,2),'Devre akımını (0,5 A) kuvvet sanmış.','bilgi'),(1,'İndüksiyon emk’sını (1 V) kuvvet sanmış.','bilgi')],
 istenen='Sabit hız için uygulanan kuvvet (N).',ip=['Çubuğu sabit hızda tutan kuvvet, çubuğa etki eden manyetik kuvvetle dengelenir; önce devre akımını bul.'],
 bilgi=[B('Hareketli iletkende emk','Alana dik hareket eden ℓ uzunluklu iletkende ε = B·ℓ·v oluşur; akım taşıyan iletkene etki eden kuvvet F = B·i·ℓ’dir. Örnek: 1 T, 0,5 m ve 2 m/s için emk 1 V’tur')],
 puf='Sabit hızda çekme kuvveti, manyetik kuvvetle dengelenir.',sekil=SK)

# ---- 06 orta · döner çerçeve (jeneratör) öncüllü ----
SK=tk(f1(['\\draw[thick,fill=red!20] (-3.0,-1.2) rectangle (-2.2,1.2);\\node at (-2.6,0) {N};\\draw[thick,fill=blue!15] (2.2,-1.2) rectangle (3.0,1.2);\\node at (2.6,0) {S};']
  +[V((-2.0,y),(2.0,y),'' ,col=AK) for y in (-.9,-.45,.45,.9)]
  +['\\draw[very thick] (-.75,-.75) -- (.75,.75);\\fill (0,0) circle (2.2pt);\\node[below] at (0,-1.3) {Çerçeve (yan görünüş)};','\\draw[->,thick] (.9,-.3) arc (-20:40:1.0);','\\node[blue!65!black,fill=white,inner sep=1pt] at (0,1.45) {$\\vec B$};']))
onc('0006','B','Düzgün bir manyetik alan içinde, alan çizgilerine dik bir eksen etrafında sabit açısal hızla döndürülen tek sarımlı bir iletken çerçevenin yan görünüşü şekilde verilmiştir. Çerçevenin uçları bir alternatif akım devresine bağlanmıştır.',
 [('Çerçevenin düzlemi alan çizgilerine dik iken çerçeveden geçen manyetik akı en büyük değerdedir.',True,'Düzlem alana dik iken normal ile alan çakışır, cosθ = 1 olur ve akı maksimumdur.','I numaralı yargıda akının, düzlem alana paralelken en büyük olduğunu düşünmüş.'),
  ('Çerçevenin düzlemi alan çizgilerine paralel iken çerçevede oluşan indüksiyon emk’sı en büyük değerdedir.',True,'Düzlem alana paralelken akı sıfırdır ama akının değişim hızı en büyüktür; emk maksimumdur.','II numaralı yargıda akı sıfır olduğu için emk’nın da sıfır olduğunu düşünmüş.'),
  ('Çerçeve bir tam dönüş yaptığında çerçevedeki akımın yönü bir kez değişir.',False,'Akım yönü her yarım dönüşte değişir; bir tam dönüşte iki kez değişir.','III numaralı yargıda akımın yönünün tam dönüşte yalnız bir kez değiştiğini düşünmüş.')],
 ['Önce akının, sonra akının değişim hızının hangi konumlarda en büyük olduğunu ayrı ayrı düşün.'],
 [B('Alternatif akım üretimi','Alan içinde dönen çerçevede Φ = Φ_maks·cosωt ve ε = −dΦ/dt = ε_maks·sinωt olur. Akı en büyükken emk sıfır, emk en büyükken akı sıfırdır. Örnek: ωt = 60° anında akı Φ_maks’ın yarısıdır')],
 'Φ = Φ_maks·cosωt’dir; emk, akının zamana göre değişim hızıdır.','Doğru olan yargılar.','ac-etkin','Alternatif akımın etkin değeri ve üretimi','orta','Alternatif Akım','Döner çerçevede akı ve emk’nın konumla değişimini yorumlar.','K-AFIND-06 (döner çerçeve) · akı–emk ilişkisi','şekilli',sekil=SK)

# ---- 07 orta · i–t grafiği, öz-indüksiyon ----
L7=Fr(1,2); seg=[((0,0),(2,2)),((2,2),(3,8)),((3,8),(5,8))]
sl=[Fr(b[1]-a[1],b[0]-a[0]) for a,b in seg]; assert sl==[1,6,0]; e7=L7*max(sl); assert e7==3 and L7*1==Fr(1,2) and L7*Fr(8,5)==Fr(4,5) and L7*2==1
SK=tk('\\begin{axis}[width=7.2cm,height=5.0cm,axis lines=middle,xticklabel pos=lower,xlabel={$t$ (s)},ylabel={$i$ (A)},xmin=0,xmax=5.6,ymin=0,ymax=9.5,xtick={1,2,3,4,5},ytick={2,4,6,8},grid=major,grid style={gray!30},tick label style={font=\\small},label style={font=\\small},xlabel style={at={(ticklabel* cs:1.0)},anchor=north west},ylabel style={at={(ticklabel* cs:1.0)},anchor=south west}]\n\\addplot[vurgu,very thick] coordinates {(0,0) (2,2) (3,8) (5,8)};\n\\end{axis}')
q('0007',[A('Aralıkları ayır','Grafik üç doğru parçasından oluşur; her aralıkta akımın değişim hızı sabittir.','0–2 s: Δi/Δt = 1 A/s · 2–3 s: 6 A/s · 3–5 s: 0'),
  A('En büyük değişim hızını seç','Öz-indüksiyon emk’sı akımın değişim hızıyla orantılıdır.','(Δi/Δt)_maks = 6 A/s (2–3 s)'),A('Emk’yı hesapla','ε = L × Δi/Δt formülü kullanılır.','ε = 0,5 × 6 = 3 V')],
 tipId='ind-oz',tip='Öz-indüksiyon emk’sı ve RL devresi',z='orta',alt='Öz-indüksiyon',kaz='Akım–zaman grafiğinden öz-indüksiyon emk’sının en büyük değerini bulur.',
 kart='K-AFIND-05 (i–t, parçalı) · en büyük emk',kalip='grafik',
 metin='Öz-indüksiyon katsayısı 0,5 H olan ideal bir bobinden geçen akımın zamanla değişimi şekildeki grafikte verilmiştir.\nBuna göre, bobinde oluşan öz-indüksiyon emk’sının büyüklüğünün en büyük değeri kaç V’tur?',
 dogru=3,yan=[(Fr(1,2),'İlk aralığın eğimini almış: 0,5 × 1 = 0,5.','dikkat'),(Fr(4,5),'Tüm süredeki ortalama değişim hızını kullanmış: 0,5 × 8 ÷ 5 = 0,8.','bilgi'),(1,'Akım değişimini L ile çarpıp süreye bölmemiş (ilk aralıkta 0,5 × 2 = 1).','islem'),(6,'Akımın değişim hızını (6 A/s) emk sanmış; L ile çarpmamış.','islem')],
 istenen='Öz-indüksiyon emk’sının en büyük değeri (V).',ip=['Emk akımın kendisine değil, zamana göre değişim hızına bağlıdır; hangi aralıkta en dik?'],
 bilgi=[B('Öz-indüksiyon emk’sı','ε = −L·Δi/Δt; i–t grafiğinde eğim değişim hızını verir. Akım sabitken emk sıfırdır. Örnek: 2 H’lik bobinde akım 1 s’de 3 A artarsa emk büyüklüğü 6 V’tur')],
 puf='i–t grafiğinde emk, eğim × L’dir; yatay kısımda sıfırdır.',sekil=SK)

# ---- 08 orta · RLC empedansı ----
w8,L8,C8,R8=100,Fr(6,10),Fr(5,10000),30; XL8=w8*L8; XC8=1/(w8*C8); Z8=sqrt(R8**2+(XL8-XC8)**2)
assert XL8==60 and XC8==20 and Z8==50 and R8+(XL8-XC8)==70 and XL8-XC8==40
SK=tk('\\draw (0,0) to[sV,l_={$\\omega=100$ rad/s}] (0,2.4);\\draw (0,2.4) to[R=$30\\,\\Omega$] (2.5,2.4) to[cute inductor=$0{,}6$ H] (5,2.4) to[C=$500\\,\\mu$F] (5,0) -- (0,0);')
q('0008',[A('Bobinin reaktansı','İndüktif reaktans açısal frekansla orantılıdır.','X_L = ωL = 100 × 0,6 = 60 Ω'),A('Sığacın reaktansı','Kapasitif reaktans ω ve C ile ters orantılıdır.','X_C = 1 ÷ (ωC) = 1 ÷ (100 × 5 × 10⁻⁴) = 20 Ω'),
  A('Empedansı yaz','Direnç ile reaktans farkı birbirine diktir; Pisagor kullanılır.','Z = √(R² + (X_L − X_C)²) = √(30² + 40²) = 50 Ω')],
 tipId='ac-rlc',tip='RLC devresi: reaktans, empedans ve rezonans',z='orta',alt='RLC Devresi',kaz='Seri RLC devresinde reaktansları ve empedansı hesaplar.',
 kart='K-AFIND-07 (seri RLC, empedans) · ω verilmiş',kalip='şekilli',
 metin='Şekildeki seri devrede direnç, ideal bobin ve sığaç, açısal frekansı 100 rad/s olan alternatif gerilim kaynağına bağlanmıştır. Elemanların değerleri şekilde verilmiştir.\nBuna göre, devrenin empedansı kaç Ω’dur?',
 dogru=50,yan=[(20,'Yalnız sığacın kapasitif reaktansını (20 Ω) empedans sanmış.','bilgi'),(30,'Yalnız direnci empedans almış.','bilgi'),(40,'Reaktansların farkını (60 − 20) empedans sanmış, direnci katmamış.','dikkat'),(70,'Direnç ile reaktans farkını cebirsel toplamış: 30 + 40.','islem')],
 istenen='Devrenin empedansı (Ω).',ip=['Önce bobinin ve sığacın alternatif akıma gösterdiği dirençleri ayrı ayrı bul.'],
 bilgi=[B('Reaktans ve empedans','X_L = ωL, X_C = 1/(ωC), Z = √(R² + (X_L − X_C)²). Örnek: R = 3 Ω ve X_L − X_C = 4 Ω ise Z = 5 Ω’dur')],
 puf='Direnç, bobin ve sığaç alternatif akıma farklı fazlarda karşı koyar.',sekil=SK)

# ---- 09 orta · i–f rezonans öncüllü ----
SK=tk('\\begin{axis}[width=7.2cm,height=4.8cm,axis lines=left,xlabel={$f$},ylabel={$i_{etkin}$},xmin=0,xmax=8,ymin=0,ymax=1.15,xtick={2,4,6},xticklabels={$f_1$,$f_0$,$f_2$},ytick=\\empty,grid=none,tick label style={font=\\small},label style={font=\\small}]\n\\addplot[vurgu,very thick,domain=0.05:8,samples=140] {1/sqrt(1+(0.9*(x/4-4/x))^2)};\n\\draw[dashed,gray] (axis cs:2,0) -- (axis cs:2,0.55);\\draw[dashed,gray] (axis cs:4,0) -- (axis cs:4,1);\\draw[dashed,gray] (axis cs:6,0) -- (axis cs:6,0.63);\n\\end{axis}')
y1=1/sqrt(1+(0.9*(2/4-4/2))**2); y2=1/sqrt(1+(0.9*(6/4-4/6))**2); assert y1<1 and y2<1
onc('0009','A','Direnci, ideal bobini ve sığacı seri bağlı olan bir devre, frekansı değiştirilebilen sabit etkin gerilimli bir alternatif gerilim kaynağına bağlanmıştır. Devreden geçen etkin akımın frekansla değişimi şekildeki grafikte verilmiştir.',
 [('f₁ frekansında devrenin empedansı, direncine eşittir.',False,'Etkin akım en büyük değerinin altındadır; akımın en büyük olduğu f₀’da Z = R olur, f₁’de Z > R’dir.','I numaralı yargıda f₁’de devrenin yalnız dirençten oluşmuş gibi davrandığını düşünmüş.'),
  ('f₂ frekansında devre indüktif karakterlidir.',True,'Rezonans frekansının üstünde X_L > X_C olur; devre bobin gibi davranır.','II numaralı yargıda rezonanstan sonra sığacın baskın olduğunu düşünmüş.'),
  ('f₀ frekansında bobin uçları arasındaki etkin gerilim, sığaç uçları arasındakinden büyüktür.',False,'Rezonansta X_L = X_C ve akım ortaktır; iki gerilim eşittir.','III numaralı yargıda rezonansta bobin geriliminin daha büyük olduğunu düşünmüş.')],
 ['Akımın en büyük olduğu frekansta devrenin nasıl davrandığını belirle, sonra frekansın iki yanındaki durumları karşılaştır.'],
 [B('Rezonans','Seri RLC devresinde f₀ = 1/(2π√(LC)) frekansında X_L = X_C olur ve akım en büyüktür. Bobin ve sığaç frekansa zıt biçimde bağlıdır: X_L = 2πfL, X_C = 1/(2πfC)')],
 'Rezonansta X_L = X_C’dir.','Doğru olan yargılar.','ac-rlc','RLC devresi: reaktans, empedans ve rezonans','orta','Rezonans','Akım–frekans grafiğinden rezonans öncesi ve sonrasındaki devre davranışını yorumlar.','K-AFIND-07 (i–f grafiği) · rezonans öncüllü','grafik',sekil=SK)

# ---- 10 orta · verimli transformatör ----
r10=5; Vp10,ip10,eta=100,2,Fr(8,10); Pp=Vp10*ip10; Ps=eta*Pp; Vs=r10*Vp10; is10=Ps/Vs
assert (Pp,Ps,Vs,is10)==(200,160,500,Fr(32,100)) and Fr(ip10,r10)==Fr(4,10) and Ps/Vp10==Fr(8,5) and ip10*r10==10
q('0010',[A('Primer gücü bul','Güç, etkin gerilim ile etkin akımın çarpımıdır.','P_p = 100 × 2 = 200 W'),A('Sekonder gücü bul','Verim, sekonder gücün primer güce oranıdır.','P_s = 0,8 × 200 = 160 W'),
  A('Sekonder gerilimi bul','Gerilim sarım sayılarıyla doğru orantılıdır.','V_s = 5 × 100 = 500 V'),A('Sekonder akımı hesapla','Sekonder güç, sekonder gerilim ve akımın çarpımıdır.','i_s = 160 ÷ 500 = 0,32 A')],
 tipId='tr-trafo',tip='Transformatör ve enerji iletimi',z='orta',alt='Transformatör',kaz='Verimi bilinen bir transformatörde sekonder akımı güç ve gerilim ilişkisiyle bulur.',
 kart='K-AFIND-08 (verimli trafo) · sekonder akım',kalip='düz',
 metin='Sekonder sarım sayısının primer sarım sayısına oranı 5 olan bir transformatörün primer devresine etkin değeri 100 V olan alternatif gerilim uygulanmıştır. Bu durumda primer devreden etkin değeri 2 A olan akım geçmektedir. Transformatörün verimi % 80’dir ve sekonder devre yüklüdür.\nBuna göre, sekonder devreden geçen akımın etkin değeri kaç A’dır?',
 dogru=Fr(32,100),yan=[(Fr(4,10),'Verimi hesaba katmamış (ideal kabul etmiş): 2 ÷ 5 = 0,4.','dikkat'),(Fr(8,5),'Sekonder gerilimi 100 V sanarak P_s ÷ V_p = 160 ÷ 100 = 1,6 bulmuş.','bilgi'),(2,'Verimi ve sarım oranını hesaba katmayıp primer akımını (2 A) sekonder akım sanmış.','bilgi'),(10,'Akımı da gerilim gibi 5 katına çıkarmış: 2 × 5 = 10.','bilgi')],
 istenen='Sekonder akımın etkin değeri (A).',ip=['Önce transformatöre giren ve çıkan güçleri karşılaştır.'],
 bilgi=[B('Transformatör','V_p/V_s = N_p/N_s. Verim = P_s/P_p. İdeal trafoda P_p = P_s olduğundan akımlar sarım sayılarıyla ters orantılıdır. Örnek: ideal bir trafoda sarım oranı 4 ise sekonder akım primerin dörtte biridir')],
 puf='Transformatör gerilimi değiştirir, gücü değil; kayıplar verimle hesaba katılır.')

# ---- 11 orta · trafo tablosu öncüllü ----
rows=[('K',100,400),('L',400,100),('M',200,200)]
tb=['\\node[font=\\small\\bfseries] at (3.2,3.35) {Sarım sayıları};','\\draw[thick] (0,0) rectangle (6.4,3.0); \\draw (0,2.25)--(6.4,2.25) (0,1.5)--(6.4,1.5) (0,.75)--(6.4,.75) (1.6,0)--(1.6,3.0) (4.0,0)--(4.0,3.0);',
  '\\node at (.8,2.62) {\\bfseries Trafo};\\node at (2.8,2.62) {\\bfseries Primer};\\node at (5.2,2.62) {\\bfseries Sekonder};']
for i,(a,b_,c_) in enumerate(rows): y_=1.87-i*.75; tb.append('\\node at (.8,%.2f) {%s};\\node at (2.8,%.2f) {%d};\\node at (5.2,%.2f) {%d};'%(y_,a,y_,b_,y_,c_))
SK=tk(f1(tb))
assert rows[0][2]>rows[0][1] and Fr(rows[1][1],rows[1][2])==4 and rows[2][1]==rows[2][2]
onc('0011','E','K, L ve M ideal transformatörlerinin primer devrelerine eşit etkin gerilimli alternatif gerilimler uygulanmıştır. Transformatörlerin sekonder devreleri yüklüdür ve sarım sayıları tabloda verilmiştir.',
 [('K transformatörü gerilim alçaltıcıdır.',False,'K’de sekonder sarım sayısı primerinkinden büyüktür; gerilim yükselir.','I numaralı yargıda sarım sayısı fazla olan tarafı “alçaltıcı” sanmış.'),
  ('L transformatöründe sekonder akımın etkin değeri, primer akımın etkin değerinin 4 katıdır.',True,'İdeal trafoda akımlar sarım sayılarıyla ters orantılıdır: i_s/i_p = N_p/N_s = 400/100 = 4.','II numaralı yargıda akımın da gerilim gibi sarım oranıyla düz orantılı değiştiğini düşünmüş.'),
  ('M transformatöründe primer ve sekonder devrelerin akımlarının etkin değerleri eşittir.',True,'Sarım sayıları eşit olduğundan gerilimler ve ideal trafoda güçler eşittir; akımlar da eşit olur.','III numaralı yargıda iki taraf arasında akım farkı olacağını düşünmüş.')],
 ['Her trafo için sarım sayılarının oranına bakıp gerilimin ve ideal trafoda akımın nasıl değiştiğini yaz.'],
 [B('Trafoda sarım ve akım','İdeal trafoda V_p/V_s = N_p/N_s ve i_p/i_s = N_s/N_p’dir. Sekonder sarım fazla ise gerilim yükselir, akım azalır. Örnek: sarım oranı N_s/N_p = 3 ise sekonder gerilim üç kat olur')],
 'İdeal trafoda güç korunur.','Doğru olan yargılar.','tr-trafo','Transformatör ve enerji iletimi','orta','Transformatör','Farklı sarım oranlı transformatörlerde gerilim ve akım ilişkilerini değerlendirir.','K-AFIND-08 (tablo, üç trafo) · öncüllü','tablo',sekil=SK)

# ---- 12 orta · ısıdan maksimum akımı bulma ----
R12,t12,Q12=10,5,200; P12=Fr(Q12,t12); ie2=P12/R12; ie=int(sqrt(ie2)); assert ie*ie==ie2 and ie==2; imax12=ie*sqrt(2)
assert P12==40 and abs(imax12-2*sqrt(2))<1e-12 and Fr(ie,2)==1 and abs(ie/sqrt(2)-sqrt(2))<1e-12 and ie**2==4
q('0012',[A('Gücü bul','Isıl güç, enerjinin süreye oranıdır.','P = 200 ÷ 5 = 40 W'),A('Etkin akımı bul','Alternatif akımda güç etkin akımın karesi ile direncin çarpımıdır.','i_etkin² = 40 ÷ 10 = 4 → i_etkin = 2 A'),A('Maksimum akıma geç','Maksimum değer etkin değerin √2 katıdır.','i_maks = 2 × √2 = 2√2 A')],
 tipId='ac-etkin',tip='Alternatif akımın etkin değeri ve üretimi',z='orta',alt='Alternatif Akım',kaz='Dirençte açığa çıkan ısıdan etkin akımı, ondan da maksimum akımı bulur.',
 kart='K-AFIND-06 (ısıdan geri hesap) · maksimum akım',kalip='düz',
 metin='Direnci 10 Ω olan saf bir dirençten sinüs biçimli bir alternatif akım geçirildiğinde, dirençte 5 s’de 200 J ısı enerjisi açığa çıkmaktadır.\nBuna göre, bu alternatif akımın maksimum değeri kaç A’dır?',
 dogru='2√2',yan=[('1','Etkin akımı 2’ye bölmüş: 2 ÷ 2 = 1.','islem'),('√2','Etkin akımı bir kez daha √2’ye bölmüş: 2 ÷ √2 = √2.','islem'),('2','Etkin akımı maksimum akım sanmış.','bilgi'),('4','Etkin akımın karesini (i² = 4) akım olarak almış.','islem')],
 sira=['1','√2','2','2√2','4'],
 istenen='Akımın maksimum değeri (A).',ip=['Isıdan önce ortalama gücü, ondan da dirençte aynı ısıyı veren doğru akım değerini bul.'],
 bilgi=[B('Etkin ve maksimum değer','Dirençte açığa çıkan ısı etkin akımla bulunur: Q = i_etkin²·R·t. Maksimum değer etkin değerin √2 katıdır: i_maks = √2·i_etkin. Örnek: etkin akımı 3 A olan akımın maksimum değeri 3√2 A’dir')],
 puf='Isı etkin değerle bulunur; maksimum değer ancak √2 ile çarpılarak elde edilir.')

# ---- 13 orta · iletim hattı öncüllü ----
P13,V13,Rh=22000,2200,4; ih=Fr(P13,V13); loss=ih**2*Rh
assert ih==10 and loss==400 and Fr(P13,220)==100 and ih*Rh==40 and (ih*Rh)**2==1600 and (Fr(P13,220))**2*Rh==40000
onc('0013','A','Bir santralde üretilen 22 kW’lık güç, toplam direnci 4 Ω olan bir iletim hattıyla taşınacaktır. Santral çıkışındaki 220 V’luk etkin gerilim ideal bir T₁ transformatörüyle 2200 V’a yükseltilerek hatta verilmekte, hattın sonunda ideal bir T₂ transformatörü gerilimi yeniden 220 V’a indirmektedir. Hatta iletilen güç 22 kW alınacak ve güç katsayısı 1 kabul edilecektir.',
 [('Hat üzerinden geçen akımın etkin değeri 10 A’dir.',True,'Hatta gerilim 2200 V ve güç 22 kW olduğundan i = P/V = 22000 ÷ 2200 = 10 A.','I numaralı yargıda hat akımını 220 V ile bulup 100 A sanmış.'),
  ('Hatta ısı olarak harcanan güç 40 W’tır.',False,'Kayıp güç P = i²R = 10² × 4 = 400 W’tır; 40 değeri iR gerilim düşmesidir (V).','II numaralı yargıda gerilim düşmesini (iR = 40 V) kayıp güç sanmış.'),
  ('T₂ transformatörünün sekonder sarım sayısı, primer sarım sayısından büyüktür.',False,'T₂ gerilimi 2200 V’tan 220 V’a düşürür; alçaltıcıdır ve sekonder sarım sayısı küçüktür.','III numaralı yargıda iki trafonun da gerilim yükselttiğini düşünmüş.')],
 ['Hat akımını belirlerken hattın hangi gerilimde çalıştığına dikkat et.'],
 [B('İletim hattında kayıp','Hat direnci R_h ve hat akımı i ise kaybolan güç P_k = i²·R_h’dir. Aynı güç daha yüksek gerilimle iletilirse akım azalır, kayıp kareyle küçülür. Örnek: akım yarıya inerse kayıp dörtte birine düşer')],
 'Enerji iletiminde gerilim yükseltilir; akım azalır, kayıp I²R ile küçülür.','Doğru olan yargılar.','tr-trafo','Transformatör ve enerji iletimi','orta','Enerji İletimi','Enerji iletim hattında akım, kayıp güç ve trafo türünü değerlendirir.','K-AFIND-08 (iletim hattı) · öncüllü','öncüllü')

# ---- 14 orta · çerçeve alandan geçerken öncüllü ----
fx0=0.2
SK=tk(f1(['\\draw[thick,fill=blue!6] (2.6,-.3) rectangle (6.8,1.9);',crosses(3.0,.1,6.4,1.5,.7,.5),'\\node[gray] at (4.7,2.25) {$B$ (sayfadan içe)};',
  '\\draw[very thick,fill=white,fill opacity=.0] (.2,.1) rectangle (1.6,1.5);','\\node at (.9,.8) {Çerçeve};',V((1.8,.8),(2.5,.8),'$v$','above'),
  dim((2.6,-.55),(6.8,-.55),'bölge genişliği','below')]))
onc('0014','E','Kenar uzunluğu ℓ olan kare biçimli iletken bir çerçeve, düzlemi manyetik alana dik olacak biçimde şekildeki gibi sabit hızla, genişliği 3ℓ olan düzgün manyetik alan bölgesine doğru ilerlemekte ve bölgeden geçmektedir.',
 [('Çerçeve alana girerken çerçevede saat yönünün tersine akım oluşur.',True,'Alan sayfadan içeri doğrudur ve akı artar; Lenz yasasına göre dışarı yönlü alan oluşturacak biçimde saat yönünün tersine akım doğar.','I numaralı yargıda akı artarken akımın akıyla aynı yönlü alan yaptığını düşünmüş.'),
  ('Çerçeve tamamen alan içinde ilerlerken çerçevede akım oluşmaz.',True,'Çerçeve tamamen içeride iken akı sabittir; ΔΦ = 0 olduğundan emk ve akım sıfırdır.','II numaralı yargıda alan içindeki çerçevede de akım oluştuğunu düşünmüş.'),
  ('Çerçeve alandan çıkarken çerçeveye etki eden bileşke manyetik kuvvet, hareket yönüne zıttır.',True,'Lenz yasası gereği indüksiyon akımı hareketi engelleyecek yöndedir; kuvvet harekete zıttır.','III numaralı yargıda çıkarken kuvvetin hareketi desteklediğini düşünmüş.')],
 ['Çerçevenin alana girdiği, tamamen içinde olduğu ve çıktığı üç evrede akının nasıl değiştiğini ayrı ayrı yaz.'],
 [B('Alan sınırından geçen çerçeve','İndüksiyon emk’sı akının değişim hızına bağlıdır ve indüksiyon akımı, kendisini doğuran değişime karşı koyacak yöndedir. Örnek: akı artarken indüksiyon alanı zıt yönlüdür')],
 'Üç evrede akıyı ayrı ayrı yaz.','Doğru olan yargılar.','ind-lenz','Lenz yasası ve indüksiyon akımının yönü','orta','Lenz Yasası','Alan bölgesinden geçen çerçevede akım yönü ve kuvvet yargılarını değerlendirir.','K-AFIND-02 (alan bölgesinden geçen çerçeve) · öncüllü','şekilli',sekil=SK)

# ---- 15 zor · B–t grafiği (iki eğim), ısı ----
A15,R15=Fr(1,2),Fr(1,10); segs=[(2,Fr(4,10)),(2,Fr(16,10)-Fr(4,10))]
sl15=[Fr(b,d) for d,b in segs]; assert sl15==[Fr(2,10),Fr(6,10)]
e1,e2=A15*sl15[0],A15*sl15[1]; Q1=e1**2/R15*2; Q2=e2**2/R15*2; Q15=Q1+Q2
assert (e1,e2)==(Fr(1,10),Fr(3,10)) and (Q1,Q2,Q15)==(Fr(1,5),Fr(9,5),2) and Fr(16,10)/4==Fr(4,10) and (A15*Fr(4,10))**2/R15*4==Fr(8,5)
assert (sl15[1]**2/R15*2)==Fr(36,5) and (sl15[0]**2/R15*2+sl15[1]**2/R15*2)==8
SK=tk(f1(['\\draw[thick] (0,0) rectangle (2.2,2.2);',crosses(.45,.45,1.8,1.8,.65,.65),'\\node[gray] at (1.1,2.55) {$B$ (sayfadan içe)};',
  '\\begin{axis}[at={(4.3cm,0cm)},anchor=south west,width=6.0cm,height=4.4cm,axis lines=middle,xticklabel pos=lower,xlabel={$t$ (s)},ylabel={$B$ (T)},xmin=0,xmax=5,ymin=0,ymax=2,xtick={1,2,3,4},ytick={0.4,0.8,1.2,1.6},yticklabels={$0{,}4$,$0{,}8$,$1{,}2$,$1{,}6$},grid=major,grid style={gray!30},tick label style={font=\\small},label style={font=\\small},xlabel style={at={(ticklabel* cs:1.0)},anchor=north west},ylabel style={at={(ticklabel* cs:1.0)},anchor=south west}]\n\\addplot[vurgu,very thick] coordinates {(0,0) (2,0.4) (4,1.6)};\n\\end{axis}']))
q('0015',[A('Eğimleri bul','Grafik iki doğru parçasıdır; her aralıkta B’nin değişim hızı sabittir.','0–2 s: 0,4 ÷ 2 = 0,2 T/s · 2–4 s: 1,2 ÷ 2 = 0,6 T/s'),A('Emkleri hesapla','Alan sabit olduğundan ε = A × ΔB/Δt.','ε₁ = 0,5 × 0,2 = 0,1 V · ε₂ = 0,5 × 0,6 = 0,3 V'),
  A('Aralıklardaki ısıları bul','Her aralıkta emk sabittir; Q = ε² t ÷ R.','Q₁ = 0,1² × 2 ÷ 0,1 = 0,2 J · Q₂ = 0,3² × 2 ÷ 0,1 = 1,8 J'),A('Toplamı yaz','Isılar toplanır.','Q = 0,2 + 1,8 = 2 J')],
 tipId='ind-faraday',tip='Faraday yasası ve grafik yorumu',z='zor',alt='Faraday Yasası',kaz='Parçalı B–t grafiğinden her aralığın emk’sını bulup dirençteki toplam ısıyı hesaplar.',
 kart='K-AFIND-03 (B–t grafiği, iki eğim, ısı) · iki kavram',kalip='grafik',
 metin='Düzlemi manyetik alana dik olan, alanı 0,5 m² ve direnci 0,1 Ω olan tek sarımlı bir iletken çerçeve, şiddeti zamanla değişen düzgün bir manyetik alan içindedir. Manyetik alan şiddetinin zamanla değişimi şekildeki grafikte verilmiştir; çerçevenin alanı değişmemektedir.\nBuna göre, çerçevede 0–4 s aralığında açığa çıkan toplam ısı enerjisi kaç J’dür?',
 dogru=2,yan=[(Fr(8,5),'Tüm süredeki ortalama eğimi (0,4 T/s) kullanmış: 0,2² × 4 ÷ 0,1 = 1,6.','bilgi'),(Fr(9,5),'Yalnız ikinci aralığın ısısını bulmuş: 0,3² × 2 ÷ 0,1 = 1,8.','dikkat'),(Fr(36,5),'Alanı katmadan yalnız ikinci aralığı almış: 0,6² × 2 ÷ 0,1 = 7,2.','dikkat'),(8,'Alanı katmadan iki aralığın ısısını toplamış: 0,8 + 7,2 = 8.','dikkat')],
 istenen='0–4 s aralığında açığa çıkan toplam ısı (J).',ip=['Alan sabit, alan şiddeti değişiyor; grafiğin her parçası için ayrı hesap gerekir.'],
 bilgi=[B('Alan şiddeti değişen çerçeve','Alan sabitse ε = A·ΔB/Δt olur; dirençteki ısı Q = ε²·t/R’dir. Örnek: alanı 2 m² olan çerçevede B 1 s’de 3 T artıyorsa emk 6 V’tur')],
 puf='Emk, akı değişim hızıdır; eğim değişince emk de değişir.',sekil=SK)

# ---- 16 zor · makaralı çubuk, sınır hız ----
m16,B16,l16,R16,g=Fr(2,10),2,Fr(1,2),2,10
v16=m16*g*R16/(B16**2*l16**2); e16=B16*l16*v16; i16=e16/R16; P16=i16**2*R16
assert v16==4 and e16==4 and i16==2 and P16==8 and P16==m16*g*v16 and m16*g*R16/(B16**2*l16)*m16*g==4 and m16*g*R16/(B16*l16**2)*m16*g==16 and e16**2*R16==32
SK=tk(f1(['\\draw[thick] (0,1.8) -- (5.0,1.8);\\draw[thick] (0,0) -- (5.0,0);\\draw[thick] (0,1.8) to[R=$2\\,\\Omega$] (0,0);','\\draw[very thick] (2.2,-.2) -- (2.2,2.0);',
  crosses(1.0,.4,1.8,1.4,.4,.5)+crosses(2.8,.4,4.4,1.4,.6,.5),'\\node[gray] at (2.6,2.4) {$B=2$ T (sayfadan içe)};',dim((-.9,0),(-.9,1.8),'$\\ell=0{,}5$ m','left'),
  '\\draw[thick] (2.2,.9) -- (5.5,.9);','\\draw[thick,fill=white] (5.5,.55) circle (.35);','\\draw[thick] (5.85,.55) -- (5.85,-.9);','\\draw[thick,fill=gray!30] (5.55,-1.5) rectangle (6.15,-.9);\\node[right] at (6.3,-1.2) {$m=0{,}2$ kg};']))
q('0016',[A('Sınır hız koşulu','Sabit hızda ip gerilmesi (mg) manyetik kuvvete eşittir; manyetik kuvvet B²ℓ²v/R’dir.','mg = B²ℓ²v ÷ R'),A('Sınır hızı bul','Denklem v için çözülür.','v = mgR ÷ (B²ℓ²) = 2 × 2 ÷ (4 × 0,25) = 4 m/s'),
  A('Emk ve akım','Çubukta oluşan emk ve devre akımı hesaplanır.','ε = Bℓv = 2 × 0,5 × 4 = 4 V · akım: i = 4 ÷ 2 = 2 A'),A('Gücü hesapla','Dirençte ısıl güç i²R’dir.','P = 2² × 2 = 8 W'),A('Kontrol et','Isıl güç, asılı cismin potansiyel enerji kaybının gücüne eşittir.','P = mg × v = 2 × 4 = 8 W')],
 tipId='ind-hareketli',tip='Hareketli iletken, emk ve manyetik kuvvet',z='zor',alt='Hareketli İletken',kaz='Makara ile çekilen çubuğun sınır hızını bulup dirençteki ısıl gücü hesaplar.',
 kart='K-AFIND-04 (makaralı çubuk, sınır hız) · güç',kalip='şekilli',
 metin='Sürtünmesiz, yatay ve paralel iletken raylar üzerindeki iletken çubuk, şekildeki gibi ideal makaradan geçen hafif bir iple kütlesi 0,2 kg olan cisme bağlanmıştır. Raylar düzlemine dik, içeri yönlü düzgün manyetik alan vardır. Cisim serbest bırakılıyor ve bir süre sonra çubuk sabit hızla hareket ediyor. Çubuğun ve rayların direnci ile hava direnci önemsizdir (g = 10 m/s²).\nBuna göre, çubuk sabit hızla giderken dirençte açığa çıkan ısıl güç kaç W’tır?',
 dogru=8,yan=[(2,'Devre akımını (2 A) güç sanmış.','bilgi'),(4,'Sınır hızı bulurken ℓ’yi karesiz almış: v = 2 m/s, P = mg × v = 4 W.','islem'),(16,'Sınır hızı bulurken B’yi karesiz almış: v = 8 m/s, P = mg × v = 16 W.','islem'),(32,'Emk’yı akım gibi kullanmış: 4² × 2 = 32 W.','bilgi')],
 istenen='Dirençte açığa çıkan ısıl güç (W).',ip=['Sabit hızda çubuğa etki eden net kuvvet sıfırdır; ipteki kuvvet hangi kuvvetle dengelenir?'],
 bilgi=[B('Sınır hız ve güç','Sabit hızda net kuvvet sıfırdır; çubuğa etki eden manyetik kuvvet F = B·i·ℓ’dir. Örnek: 2 T, 3 A ve 0,5 m için manyetik kuvvet 3 N’dur')],
 puf='Sabit hızda net kuvvet sıfırdır.',sekil=SK)

# ---- 17 orta · bobinde depolanan enerji ----
L17,i17=Fr(250,1000),8; E17=Fr(1,2)*L17*i17**2
assert E17==8 and Fr(1,2)*L17*i17==1 and L17*i17==2 and L17*i17**2==16 and Fr(1,2)*i17**2==32
q('0017',[A('Birimi çevir','Öz-indüksiyon katsayısı henry cinsinden alınır.','L = 250 mH = 0,25 H'),A('Depolanan enerjiyi bul','Bobinde manyetik alan enerjisi ½ L i² ile bulunur.','E = ½ × 0,25 × 8² = 8 J'),A('Isıya çevir','Enerji tamamen dirençte ısıya dönüşür.','Q = E = 8 J')],
 tipId='ind-oz',tip='Öz-indüksiyon emk’sı ve RL devresi',z='orta',alt='Bobinde Enerji',kaz='Bobinde depolanan manyetik enerjiyi hesaplayıp ısıya dönüşen enerjiyle ilişkilendirir.',
 kart='K-AFIND-05 (bobin enerjisi) · mH–H dönüşümü',kalip='düz',
 metin='Öz-indüksiyon katsayısı 250 mH olan ideal bir bobinden 8 A’lik sabit akım geçmektedir. Bobin bir anda üretecinden ayrılıp bir dirence bağlanıyor ve bobinde depolanmış enerjinin tamamı dirençte ısıya dönüşüyor.\nBuna göre, dirençte açığa çıkan ısı kaç J’dür?',
 dogru=8,yan=[(1,'Karesini almadan ½ × 0,25 × 8 = 1 bulmuş.','islem'),(2,'Akıyı (L × i = 2) enerji sanmış.','bilgi'),(16,'½ katsayısını unutmuş: 0,25 × 8² = 16.','bilgi'),(32,'L’yi hesaba katmamış: ½ × 8² = 32.','dikkat')],
 istenen='Dirençte açığa çıkan ısı (J).',ip=['Bobin, akım geçerken manyetik alanında enerji depolar; öz-indüksiyon katsayısının birimine dikkat et.'],
 bilgi=[B('Bobinde enerji','Akım taşıyan bobinin manyetik alanında depolanan enerji E = ½·L·i²’dir. Örnek: 2 H’lik bobinden 3 A geçerken depolanan enerji 9 J’dür')],
 puf='Depolanan enerji akımın karesiyle artar.')

# ---- 18 zor · trafo + R–X_L, öncüllü ----
Vp18,r18,R18,X18=200,10,3,4; Vs18=Fr(Vp18,r18); Z18=Fr(int(sqrt(R18**2+X18**2))); is18=Vs18/Z18; ip18=is18/r18
assert Z18==5 and is18==4 and ip18==Fr(2,5) and R18+X18==7 and Vs18/X18==5 and is18*r18==40
SK=tk(f1(['\\draw[very thick] (1.0,0) rectangle (3.4,2.4);\\draw[very thick,fill=white] (1.7,.6) rectangle (2.7,1.8);',
  ''.join('\\draw[thick,fill=white] (1.35,%.2f) ellipse (.45 and .13);'%y for y in (.75,1.05,1.35,1.65)),''.join('\\draw[thick,fill=white] (3.05,%.2f) ellipse (.45 and .13);'%y for y in (.75,1.05,1.35,1.65)),
  '\\draw[thick] (.9,1.65) -- (0,1.65);\\draw (0,1.65) to[sV,l_=$200$ V] (0,.75);\\draw[thick] (0,.75) -- (.9,.75);',
  '\\draw[thick] (3.5,1.65) -- (3.9,1.65);\\draw (3.9,1.65) to[R=$3\\,\\Omega$] (5.3,1.65);\\draw (5.3,1.65) to[cute inductor={$X_L=4\\,\\Omega$}] (6.9,1.65);\\draw[thick] (6.9,1.65) -- (6.9,.75) -- (3.5,.75);',
  '\\node at (1.35,-.35) {$N_p=1000$};\\node at (3.05,-.35) {$N_s=100$};']))
onc('0018','C','Şekildeki ideal transformatörün primer devresine etkin değeri 200 V olan alternatif gerilim uygulanmıştır. Sekonder devrede, direnci 3 Ω olan direnç ile indüktif reaktansı 4 Ω olan ideal bir bobin seri bağlıdır.',
 [('Sekonder devrenin empedansı 7 Ω’dur.',False,'Direnç ile reaktans birbirine diktir: Z = √(3² + 4²) = 5 Ω.','I numaralı yargıda direnç ile reaktansı cebirsel toplamış: 3 + 4 = 7 Ω.'),
  ('Sekonder devreden geçen akımın etkin değeri 5 A’dir.',False,'V_s = 200 × 100/1000 = 20 V; i_s = 20 ÷ 5 = 4 A.','II numaralı yargıda yalnız bobinin reaktansını kullanmış: 20 ÷ 4 = 5 A.'),
  ('Primer devreden geçen akımın etkin değeri 0,4 A’dir.',True,'İdeal trafoda i_p = i_s × N_s/N_p = 4 × 100/1000 = 0,4 A.','III numaralı yargıda akımın da gerilim gibi sarım oranıyla düz orantılı değiştiğini düşünmüş.')],
 ['Sekonder gerilimi bulduktan sonra sekonder devreyi tek başına çöz.'],
 [B('Trafolu RL devresi','Sekonder gerilim V_s = V_p·N_s/N_p, sekonder akım i_s = V_s/Z’dir; ideal trafoda i_p = i_s·N_s/N_p olur. Örnek: R = 6 Ω ve X_L = 8 Ω seri ise Z = 10 Ω’dur')],
 'İdeal trafoda güç korunur.','Doğru olan yargılar.','tr-trafo','Transformatör ve enerji iletimi','zor','Transformatör','Transformatörün sekonder devresindeki R–X_L yükünü çözüp primer akımını bulur.','K-AFIND-08 (trafo + R–X_L) · öncüllü','şekilli',sekil=SK)

# ---- 19 zor · rezonanstan sonra frekans iki katına çıkarılırsa ----
R19,L19,C19,Ve19=80,Fr(4,10),Fr(25,100000),100; w0=1/sqrt(L19*C19); assert abs(w0-100)<1e-9
w1=2*100; XL19=w1*L19; XC19=1/(w1*C19); Z19=Fr(int(sqrt(R19**2+(XL19-XC19)**2))); i19=Ve19/Z19; VL19=i19*XL19
assert XL19==80 and XC19==20 and Z19==100 and i19==1 and VL19==80 and i19*XC19==20 and i19*40==40 and Fr(Ve19,R19)*40==50 and i19*(XL19-XC19)==60
q('0019',[A('Yeni reaktansları bul','Frekans iki katına çıkınca bobinin reaktansı iki katına çıkar, sığacınki yarıya iner. Rezonans açısal frekansı ω₀ = 1/√(LC) = 100 rad/s’dir.','ω = 200 rad/s · X_L = 200 × 0,4 = 80 Ω · X_C = 1 ÷ (200 × 2,5 × 10⁻⁴) = 20 Ω'),
  A('Empedansı bul','Direnç ile reaktans farkı birleşir.','Z = √(80² + (80 − 20)²) = 100 Ω'),A('Akımı bul','Ohm yasası etkin değerlerle uygulanır.','i = 100 ÷ 100 = 1 A'),A('Bobin gerilimini yaz','Bobin gerilimi akım × reaktanstır.','V_L = 1 × 80 = 80 V')],
 tipId='ac-rlc',tip='RLC devresi: reaktans, empedans ve rezonans',z='zor',alt='Rezonans',kaz='Rezonanstan sonra frekansı değiştirilen seri RLC devresinde bobin gerilimini bulur.',
 kart='K-AFIND-07 (rezonanstan sonra frekans 2 katı) · bobin gerilimi',kalip='düz',
 metin='Seri bağlı 80 Ω’luk bir direnç, 0,4 H’lik ideal bir bobin ve 250 μF’lık ideal bir sığaçtan oluşan devre, etkin gerilimi 100 V olan ve frekansı değiştirilebilen bir alternatif gerilim kaynağına bağlanmıştır. Kaynağın frekansı önce devre rezonansa girecek biçimde ayarlanmış, sonra bu değerin iki katına çıkarılmıştır.\nBuna göre, frekans iki katına çıkarıldıktan sonra bobinin uçları arasındaki etkin gerilim kaç V’tur?',
 dogru=80,yan=[(20,'Sığacın uçları arasındaki gerilimi (1 × 20) bobin gerilimi sanmış.','bilgi'),(40,'Bobinin reaktansını rezonanstaki değerinde (40 Ω) bırakmış: 1 × 40 = 40.','dikkat'),(50,'Rezonanstaki akımı (100 ÷ 80 = 1,25 A) yeni durumda da kullanmış: 1,25 × 40 = 50.','dikkat'),(60,'Reaktansların farkıyla akımı çarpmış: 1 × (80 − 20) = 60.','bilgi')],
 istenen='Bobin uçları arasındaki etkin gerilim (V).',ip=['Frekans değişince hem bobinin hem sığacın reaktansı değişir; akımı da yeniden bulmalısın.'],
 bilgi=[B('Frekansla reaktans','X_L = ωL frekansla artar, X_C = 1/(ωC) frekansla azalır; Z = √(R² + (X_L − X_C)²). Örnek: ω iki katına çıkınca X_L iki katına çıkar, X_C yarıya iner')],
 puf='Rezonansta Z = R’dir.')

# ---- 20 zor · çerçevenin alandan geçişi, toplam ısı ----
a20,B20,v20,R20,W20=Fr(2,10),Fr(1,2),2,Fr(4,10),Fr(5,10)
e20=B20*a20*v20; i20=e20/R20; tg=a20/v20; Q20=2*i20**2*R20*tg
assert e20==Fr(1,5) and i20==Fr(1,2) and tg==Fr(1,10) and Q20==Fr(2,100) and i20**2*R20*tg==Fr(1,100) and i20**2*R20*(W20+a20)/v20==Fr(35,1000) and i20**2*R20==Fr(1,10) and W20>a20
SK=tk(f1(['\\draw[thick,fill=blue!6] (3.6,-.2) rectangle (6.6,2.1);',crosses(4.0,.2,6.2,1.7,.55,.5),'\\node[gray] at (5.1,2.45) {$B=0{,}5$ T (sayfadan içe)};',
  '\\draw[very thick] (.4,.3) rectangle (1.6,1.5);',V((1.9,.9),(3.4,.9),'$v=2$ m/s','above'),dim((3.6,-.55),(6.6,-.55),'$0{,}5$ m','below'),dim((.4,1.8),(1.6,1.8),'$0{,}2$ m','above')]))
q('0020',[A('Emk’yı bul','Alana giren (ya da çıkan) kenar ε = B a v emk’sı oluşturur.','ε = 0,5 × 0,2 × 2 = 0,2 V'),A('Akımı bul','Akım Ohm yasasıyla bulunur.','i = 0,2 ÷ 0,4 = 0,5 A'),
  A('Akım süresini bul','Girerken 0,2 m, çıkarken 0,2 m yol alınır; arada (bölge çerçeveden geniş) akım yoktur.','t_giriş = t_çıkış = 0,2 ÷ 2 = 0,1 s'),A('Isıyı hesapla','Girişte ve çıkışta aynı güç, aynı sürede açığa çıkar.','Q = 2 × (0,5² × 0,4) × 0,1 = 0,02 J')],
 tipId='ind-hareketli',tip='Hareketli iletken, emk ve manyetik kuvvet',z='zor',alt='Hareketli İletken',kaz='Alan bölgesinden geçen çerçevede emk, akım ve akımın aktığı süreyi birleştirip ısıyı hesaplar.',
 kart='K-AFIND-04 (çerçevenin alandan geçişi) · toplam ısı',kalip='şekilli',
 metin='Kenar uzunluğu 0,2 m ve direnci 0,4 Ω olan kare biçimli iletken bir çerçeve, düzlemi manyetik alana dik olacak biçimde, genişliği şekilde verilen düzgün manyetik alan bölgesine sabit hızla girip bölgeyi tamamen geçmektedir.\nBuna göre, çerçevenin bölgeye girmeye başlamasından bölgeyi tamamen terk etmesine kadar geçen sürede çerçevede açığa çıkan toplam ısı kaç J’dür?',
 dogru=Fr(2,100),yan=[(Fr(1,100),'Yalnız girişteki ısıyı bulmuş: 0,25 × 0,4 × 0,1 = 0,01.','dikkat'),(Fr(35,1000),'Çerçeve bölgeyi geçerken akımın hep aktığını düşünmüş: 0,1 W × (0,5 + 0,2) ÷ 2 s = 0,035.','bilgi'),(Fr(1,10),'Isıl gücü (0,1 W) enerji sanmış.','bilgi'),(Fr(1,5),'Emk değerini (0,2 V) ısı sanmış.','bilgi')],
 istenen='Çerçevede açığa çıkan toplam ısı (J).',ip=['Çerçevede akımın yalnız akı değiştiği sürelerde aktığını göz önünde bulundur; bu süreler kaç saniyedir?'],
 bilgi=[B('Alan bölgesinden geçiş','Çerçeve girerken ve çıkarken, alana dik kenar başına ε = B·a·v emk’sı oluşur; tamamen içerideyken emk sıfırdır. Örnek: eni 0,3 m olan dikdörtgen çerçeve 3 m/s ile giriyorsa giriş 0,1 s sürer')],
 puf='Akı ne zaman değişiyor?',sekil=SK)

# ---------- yaz ----------
for x in P.ANA: x['kardes']=None
SC=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/ind')
os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'induksiyon-1.json'),os.path.join(SC,'bos-induksiyon.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik, MEB 12. sınıf indüksiyon, alternatif akım ve transformatörler.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','afinduksiyon.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
