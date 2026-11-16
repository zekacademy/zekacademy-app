"""TYT Fizik · Dinamik ikinci paket (20 soru, kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from math import sin,cos,radians,exp
H.KONU='Dinamik'
P=Parti('dinamikiki','Dinamik','fiz|Dinamik',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9. sınıf fizik'
TIP={'ey':('fz-dn2-eylemsizlik','Eylemsizlik ve Newton’ın birinci yasası'),
     'gr':('fz-dn2-grafik','Net kuvvet–ivme ve hız–zaman grafikleri'),
     'ic':('fz-dn2-iki-cisim','Birbirine değen iki cismin hareketi'),
     'et':('fz-dn2-etki-tepki','Etki–tepki kuvvetleri'),
     'su':('fz-dn2-surtunme','Sürtünmeli ve sürtünmesiz yatay düzlem'),
     'ip':('fz-dn2-ip','İple bağlı cisimlerde gerilme'),
     'li':('fz-dn2-limit-hiz','Serbest düşme ve limit hız'),
     'ag':('fz-dn2-agirlik-kutle','Ağırlık ve kütle farkı'),
     'as':('fz-dn2-asansor','Asansörde tartı')}
def K(n,t,alt,fikir,tuzak,z,kalip,adim):
    tid,tad=TIP[t]; kart(f'K-FZDN2-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tid,tad,KY)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def fok(p,q,et,pos='above'):
    m=((p[0]+q[0])/2,(p[1]+q[1])/2)
    return f'\\draw[vurgu,very thick,{ARR}] ({p[0]:.2f},{p[1]:.2f}) -- ({q[0]:.2f},{q[1]:.2f}); \\node[vurgu,{pos}] at ({m[0]:.2f},{m[1]:.2f}) {{{et}}};'
def blok(x,y,w,h,et,fill='gray!25'):
    return f'\\draw[thick,fill={fill}] ({x:.2f},{y:.2f}) rectangle ({x+w:.2f},{y+h:.2f}); \\node at ({x+w/2:.2f},{y+h/2:.2f}) {{{et}}};'
def zemin(x0,x1,y=0,sw=False):
    return f'\\fill[gray!30] ({x0},{y-.2}) rectangle ({x1},{y}); \\draw ({x0},{y}) -- ({x1},{y});'
def sk(*l,sc=1.35): return tikz_svg(HEAD.replace('[','[scale=%s,'%sc,1)+'\n'.join(l)+TAIL)
ROM={1:'I',2:'II',3:'III'}
def lab(s):
    s=sorted(s); return 'Yalnız '+ROM[s[0]] if len(s)==1 else (ROM[s[0]]+' ve '+ROM[s[1]] if len(s)==2 else 'I, II ve III')
def parse(l):
    return {n for n,r in ROM.items() if r in l.replace('Yalnız','').replace(',',' ').replace('ve',' ').split()}
def onc(no,truth,sira,ney,kok,**k):
    """ney: {n:(doğru_gerekçe, yanlış_gerekçe)}; öncül cümleleri kok içinde yazılır."""
    for l in sira: assert lab(parse(l))==l,l
    assert lab(truth) in sira and len(set(sira))==5
    yan=[]
    for l in sira:
        if l==lab(truth): continue
        S=parse(l); p=[]
        for n in sorted(S-truth): p.append(f'{ROM[n]}. yargıyı doğru sanmış: {ney[n][1]}')
        for n in sorted(truth-S): p.append(f'{ROM[n]}. yargıyı yanlış sanmış: {ney[n][0]}')
        yan.append((l,' '.join(p),'bilgi'))
    ad=k.pop('ad_on',[])+[A(f'{ROM[n]}. yargıyı sına',ney[n][0] if n in truth else ney[n][1],'doğru' if n in truth else 'yanlış') for n in (1,2,3)]
    ad.append(A('Sonucu yaz','Doğru olan yargıları birleştir.','Doğru olanlar: '+lab(truth)))
    assert 3<=len(ad)<=7
    q(no,ad=ad,metin=kok,dogru=lab(truth),yan=yan,sira=sira,kalip=k.pop('kalip','öncüllü'),**k)
def q(no,**k):
    assert len(k['ip'])==1
    ad=k.pop('ad'); mk(P,no,ad=ad,adim=len(ad),**k)
S1=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
GRAF=('\\begin{axis}[width=%s,height=%s,xmin=0,xmax=%s,ymin=0,ymax=%s,xtick distance=%s,ytick distance=%s,grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={%s},ylabel={%s},xlabel style={font=\\small},ylabel style={font=\\small}]')
def graf(w,h,xm,ym,dx,dy,xl,yl,*govde): return sk(GRAF%(w,h,xm,ym,dx,dy,xl,yl),*govde,'\\end{axis}',sc=1)

# ================= 01 · eylemsizlik, sarkaç · orta · öncüllü =================
K(1,'ey','Newton’ın Hareket Yasaları','Araçta asılı cismin sapma yönü aracın ivme yönünü gösterir (eylemsizlik); ivme ile hız yönünden hızın artıp azaldığı çıkarılır.','Cismin savrulduğu yönü hareket yönü sanmak; sapmayı kuvvet “iter” diye yorumlamak.','orta','öncüllü',3)
ang=22; L1=1.5; px=2.1; py=2.3; bx=px+L1*sin(radians(ang)); by=py-L1*cos(radians(ang))
assert bx>px and by>0.45
SK1=sk('\\draw (-.4,.05) -- (4.6,.05);','\\draw[thick,rounded corners=4pt] (0,.35) rectangle (4.2,2.3);','\\draw[thick,fill=white] (.9,.35) circle (.3); \\draw[thick,fill=white] (3.3,.35) circle (.3);',
 f'\\draw[dashed,gray] ({px},{py}) -- ({px},{py-L1:.2f});',f'\\draw[thick] ({px},{py}) -- ({bx:.3f},{by:.3f});',f'\\draw[thick,fill=gray!50] ({bx:.3f},{by:.3f}) circle (.15);',f'\\fill ({px},{py}) circle (1.5pt);')
onc('0001',{1,2},['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 {1:('İvme sola doğrudur; sağa giden araçta ivme hıza zıt olduğundan hız azalır.','Sarkacın sağa sapması aracın sağa doğru hızlandığını göstermez; ivme tersi yöndedir.'),
  2:('İvme sola doğru, hız da sola doğruysa ikisi aynı yönlüdür; hız artar.','Sola giden araçta ivmenin sola olması hızı azaltır sanmış; aynı yönlü ivme hızı artırır.'),
  3:('Sabit hızda ivme sıfırdır; sarkaç düşey asılı kalır. İp eğik olduğundan araç ivmelidir.','Sabit hızda ivme sıfırdır ve ip düşey kalır; ip eğik olduğundan minibüs ivmelidir.')},
 'Düz ve yatay bir yolda giden bir minibüsün tavanına hafif bir iple küçük bir top asılmıştır. İpin kütlesi ve hava direnci önemsenmeyecek kadar küçüktür. Şekildeki an, top minibüse göre durgun ve ip düşeyle sabit bir açı yapacak biçimdedir. Minibüsün hareket yönü bilinmemektedir.\nBuna göre,\nI. Minibüs sağa doğru gidiyorsa hızı azalmaktadır.\nII. Minibüs sola doğru gidiyorsa hızı artmaktadır.\nIII. Minibüs sabit hızla hareket etmektedir.\nyargılarından hangileri doğrudur?',
 tipId=TIP['ey'][0],tip=TIP['ey'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Eylemsizlik yoluyla araçtaki sarkacın sapmasından ivme yönünü ve hızın artıp azaldığını yorumlar.',
 kart='K-FZDN2-01 (araçta sarkaç, eylemsizlik) · öncüllü',istenen='Doğru olan yargılar.',ip=['Topun minibüse göre durgun olması ne anlama gelir; minibüsün ivmesi var mıdır?'],
 bilgi=[B('Eylemsizlik','cisimler hareket durumlarındaki değişime direnir. Araç hızlanırken içindeki asılı cisim geride kalır, yavaşlarken ileri savrulur. Örnek: otobüs ani kalkarken yolcular geriye doğru eğilir'),B('İvme ve hız yönü','hız ile ivme aynı yönlüyse hız artar, zıt yönlüyse azalır')],
 puf='Asılı cisim aracın ivmesinin tersi yönünde sapar; hız–ivme yönlerini karşılaştırarak artış ya da azalışa karar ver.',sekil=SK1,kalip='öncüllü')

# ================= 02 · eylemsizlik günlük örnekler · orta · öncüllü (şekilsiz) =================
K(2,'ey','Newton’ın Hareket Yasaları','Eylemsizlik kütleyle artar; her cismin eylemsizliği vardır; örtü çekme, kafa vurma gibi örnekler birinci yasa ile açıklanır.','Hareketsiz cismin eylemsizliği yoktur sanmak; eylemsizliği hızla karıştırmak.','orta','öncüllü',3)
onc('0002',{1,3},['Yalnız I','Yalnız II','Yalnız III','I ve III','I, II ve III'],
 {1:('Eylemsizliğin ölçüsü kütledir; kütlesi büyük cismin hareket durumunu değiştirmek zordur.','Büyük kütleli cismin eylemsizliğinin daha küçük olduğunu sanmış.'),
  2:('Duran cisim de hareket durumunu korur (durma hâlini sürdürür); eylemsizlik her cisimde vardır.','Eylemsizlik her cismin özelliğidir; durgun cisim de durma hâlini korur.'),
  3:('Örtü hızla çekilince etkiyen kuvvet bardağa çok kısa süre uygulanır; bardak durma hâlini korur ve yerinde kalır.','Örtü çok hızlı çekilirse bardağa kısa süre kuvvet uygulanır; bardak durma hâlini korur ve yerinde kalır.')},
 'Bir öğrenci, düz masa üzerine serilmiş kaygan bir örtünün üzerine içi dolu bir bardak koyuyor. Örtüyü masa kenarından yatay doğrultuda çok hızlı çekince bardağın yerinde kaldığını gözlüyor. Öğrenci bunu Newton’ın birinci yasası ile açıklamaya çalışıyor ve eylemsizlik hakkında şu yargıları ileri sürüyor:\nI. Kütlesi büyük olan cismin eylemsizliği daha fazladır.\nII. Durmakta olan cisimlerin eylemsizliği yoktur.\nIII. Bardağın yerinde kalması, bardağın durma hâlini korumasındandır.\nBuna göre öğrencinin yargılarından hangileri doğrudur?',
 tipId=TIP['ey'][0],tip=TIP['ey'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Eylemsizlik kavramını kütle ve günlük örnekler üzerinden değerlendirir.',
 kart='K-FZDN2-02 (eylemsizlik, günlük örnek) · öncüllü',istenen='Doğru olan yargılar.',ip=['Eylemsizliğin neye bağlı olduğunu ve durgun cisimlerde de geçerli olup olmadığını düşün.'],
 bilgi=[B('Newton’ın birinci yasası','net kuvvet etki etmeyen cisim durgunsa durgun, hareketliyse sabit hızla hareketine devam eder. Bu eğilime eylemsizlik denir; ölçüsü kütledir. Örnek: ani frende yolcunun öne savrulması')],
 puf='Eylemsizlik her cisimde vardır ve kütleyle artar; ani kuvvetlerde cisim eski hâlini korumaya çalışır.')

# ================= 03 · a–F grafiği · kolay =================
K(3,'gr','Newton’ın Hareket Yasaları','Net kuvvet–ivme grafiğinin eğimi 1/m’dir; doğru orantı olduğundan başka bir ivmedeki kuvvet eğimden bulunur.','Eğim yerine ordinatı kütle ya da kuvveti ivme gibi alıp bölmek.','kolay','grafik',2)
m3=2; assert Fr(8,4)==m3 and Fr(7)*m3==14 and Fr(7,2)==3.5 and 7+2==9 and 7*4==28
SK3=graf('8.2cm','5.6cm',9,5,2,1,'$F_{net}$ (N)','$a$ (m/s$^2$)','\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {(0,0) (8,4)};')
q('0003',tipId=TIP['gr'][0],tip=TIP['gr'][1],z='kolay',alt='Newton’ın Hareket Yasaları',kaz='Net kuvvet–ivme grafiğinden kütleyi dolaylı bularak farklı bir ivme için gereken kuvveti hesaplar.',
 kart='K-FZDN2-03 (a–F grafiği, kütle) · kolay',kalip='grafik',
 metin='Bir öğrenci, sürtünmesiz yatay bir yüzeyde durmakta olan bir cisme, her denemede büyüklüğü farklı olan yatay kuvvetler uygulanıyor. Cismin kazandığı ivmeler ölçülerek elde edilen net kuvvet–ivme grafiği şekildeki gibi çiziliyor.\nAynı cisme 7 m/s² ivme kazandırmak için uygulanması gereken yatay kuvvet kaç N olmalıdır?',
 sekil=SK3,dogru=14,yan=[(3.5,'Kuvveti bulmak için ivmeyi kütleye bölmüş (7 ÷ 2).','islem'),(7,'Kuvvetle ivmeyi eşit almış; kütleyi hesaba katmamış.','bilgi'),(9,'İvmeye kütleyi toplayarak eklemiş (7 + 2).','islem'),(28,'Grafikteki 4 m/s² değerini kütle sanıp 7 ile çarpmış.','dikkat')],
 istenen='7 m/s² ivme için gereken kuvvet (N).',ip=['Grafikteki bir noktadan cismin kütlesini bul, sonra istenen ivmeye uygula.'],
 bilgi=[B('Newton’ın ikinci yasası','F = m × a; net kuvvet–ivme grafiği orijinden geçen doğrudur ve eğimi 1/m’dir. Örnek: 3 kg’lık cisimde 6 N kuvvet 2 m/s² ivme verir')],
 ad=[A('Grafikten okuma','Doğru üzerindeki bir noktanın kuvvet ve ivmesini oku.','F = 8 N için a = 4 m/s²'),A('Kütleyi bul','Kütle kuvvetin ivmeye oranıdır.','m = 8 ÷ 4 = 2 kg'),A('Kuvveti hesapla','İstenen ivmeyi yasada yerine koy.','F = 2 × 7 = 14 N')],
 puf='Doğrusal a–F grafiğinden kütleyi bir noktadan bul: m = F ÷ a.')

# ================= 04 · iki doğrulu a–F grafiği · orta · öncüllü =================
K(4,'gr','Newton’ın Hareket Yasaları','İki cismin a–F doğruları karşılaştırılır: eğim büyükse kütle küçüktür; aynı kuvvette ivme kütleyle ters orantılıdır.','Eğimi büyük doğruyu büyük kütleli sanmak.','orta','öncüllü',3)
mX,mY=2,4; assert Fr(12,mX)==6 and Fr(12,mY)==3 and Fr(8,mY)==2 and Fr(8,mX)==4 and Fr(8,mX)==2*Fr(8,mY)
SK4=graf('8.4cm','5.8cm',13,7,2,1,'$F_{net}$ (N)','$a$ (m/s$^2$)','\\addplot[thick,vurgu] coordinates {(0,0) (12,6)}; \\node[vurgu,above left] at (axis cs:12,6) {X};','\\addplot[thick] coordinates {(0,0) (12,3)}; \\node[above] at (axis cs:12,3) {Y};')
onc('0004',{2,3},['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 {1:('Aynı kuvvette X’in ivmesi büyük olduğundan X’in kütlesi küçüktür.','Eğim 1/m’dir; X’in eğimi büyük olduğundan X’in kütlesi küçüktür.'),
  2:('Grafikte 8 N için Y’nin ivmesi 2 m/s² okunur.','Y’nin ivmesini 8 N için yanlış okumuş; grafikte 2 m/s²’dir.'),
  3:('Aynı kuvvette ivmeler kütle ile ters orantılıdır; X’in ivmesi Y’ninkinin 2 katıdır (4 ve 2 m/s²).','Aynı kuvvette X’in ivmesinin Y’ninkinden 2 kat büyük olduğunu fark etmemiş.')},
 'Bir fizik laboratuvarında öğrenciler, sürtünmesiz yatay bir düzlemde durmakta olan X ve Y cisimlerine ayrı ayrı yatay kuvvetler uyguluyor ve kazandıkları ivmeleri ölçüyor. Ölçümlerden elde edilen net kuvvet–ivme grafikleri şekildeki gibidir.\nBuna göre,\nI. X’in kütlesi Y’nin kütlesinden büyüktür.\nII. 8 N’luk net kuvvet uygulanan Y’nin ivmesi 2 m/s²’dir.\nIII. Aynı net kuvvet uygulandığında X’in ivmesi Y’ninkinin 2 katıdır.\nyargılarından hangileri doğrudur?',
 tipId=TIP['gr'][0],tip=TIP['gr'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='İki cismin net kuvvet–ivme grafiklerini karşılaştırarak kütle ve ivme ilişkisini yorumlar.',
 kart='K-FZDN2-04 (iki cisimli a–F grafiği) · öncüllü',istenen='Doğru olan yargılar.',ip=['Her doğrunun eğimi 1/m’dir; aynı kuvvete karşılık gelen ivmeleri grafikte yan yana oku.'],
 bilgi=[B('İvme–kütle ilişkisi','aynı net kuvvet altında ivme kütleyle ters orantılıdır (a = F ÷ m). Örnek: kütlesi yarı olan cismin ivmesi 2 kat olur')],
 puf='a–F grafiğinde eğimi büyük doğru kütlesi küçük olan cisme aittir.',sekil=SK4)

# ================= 05 · temas kuvveti · kolay =================
K(5,'ic','Newton’ın Hareket Yasaları','Birlikte hareket eden değen cisimlerde ortak ivme bulunur; öndeki cisme uygulanan temas kuvveti onun kütlesi × ivmedir.','Uygulanan kuvveti temas kuvveti sanmak; iki cisme ayrı ayrı F uygulamak.','kolay','şekilli',3)
mA,mB,F5=2,4,30; a5=Fr(F5,mA+mB); N5=mB*a5
assert a5==5 and N5==20 and F5-mA*a5==N5 and mA*a5==10 and F5//2==15
SK5=sk(zemin(-.3,7.2,0),blok(1.4,0,1.1,.9,'$2$ kg'),blok(2.5,0,1.4,1.1,'$4$ kg'),fok((-.2,.45),(1.4,.45),'$F=30$ N'))
q('0005',tipId=TIP['ic'][0],tip=TIP['ic'][1],z='kolay',alt='Newton’ın Hareket Yasaları',kaz='Birbirine değen iki cismin ortak ivmesinden aralarındaki temas kuvvetini bulur.',
 kart='K-FZDN2-05 (değen iki cisim, temas kuvveti) · kolay',kalip='şekilli',
 metin='Bir laboratuvarda, sürtünmesiz yatay bir masada kütleleri 2 kg ve 4 kg olan iki cisim şekildeki gibi birbirine değecek biçimde durmaktadır. Soldaki cisme yatay doğrultuda, büyüklüğü şekilde verilen kuvvet uygulanınca iki cisim birbirinden ayrılmadan hareket ediyor.\nBuna göre 2 kg’lık cismin 4 kg’lık cisme uyguladığı kuvvet kaç N’dur?',
 sekil=SK5,dogru=20,yan=[(5,'Ortak ivmeyi (5 m/s²) kuvvet sanmış.','dikkat'),(10,'Temas kuvvetini soldaki cismin kütlesi ile ivmesinin çarpımı (2 × 5) olarak almış.','dikkat'),(15,'Uygulanan kuvveti iki cisme eşit paylaştırmış (30 ÷ 2).','bilgi'),(30,'Uygulanan kuvvetin 4 kg’lık cisme olduğu gibi iletildiğini sanmış.','bilgi')],
 istenen='İki cisim arasındaki temas kuvveti (N).',ip=['Önce iki cismin birlikte kazandığı ivmeyi bul; sonra hangi cismi hangi kuvvetin hızlandırdığına bak.'],
 bilgi=[B('Birlikte hareket','birbirine değen ya da bağlı cisimler aynı ivmeyle hareket eder: a = F ÷ (toplam kütle). Örnek: 5 kg ve 1 kg’a 12 N uygulanırsa a = 2 m/s²')],
 ad=[A('Ortak ivme','Her iki cisim birlikte hareket eder; toplam kütle 6 kg’dır.','a = 30 ÷ 6 = 5 m/s²'),A('Öndeki cisme bak','4 kg’lık cismi hızlandıran tek yatay kuvvet temas kuvvetidir.','N = m × a'),A('Hesapla','Değerleri yerine koy.','N = 4 × 5 = 20 N')],
 puf='Değen cisimlerde önce ortak ivmeyi bul, temas kuvvetini öndeki cismin m × a değerinden hesapla.')

# ================= 06 · üç cisim, sürtünmeli, ip gerilmesi · zor =================
K(6,'ip','Sürtünme Kuvveti','Sürtünmeli zeminde üç cisimde ortak ivme Fnet = F − Σf ile bulunur; ip gerilmesi, ipin gerisindeki ya da önündeki cisimlerden biri için sürtünme de yazılarak hesaplanır.','Sürtünmeyi atlamak; gerilmeyi yanlış tarafın kütlesiyle hesaplamak.','zor','şekilli',5)
m1,m2,m3,F6,mu,g=1,2,3,42,Fr(1,10),10; f1,f2,f3=mu*m1*g,mu*m2*g,mu*m3*g
a6=Fr(F6-f1-f2-f3,m1+m2+m3); T1=f1+m1*a6; T2=F6-f3-m3*a6
assert (f1,f2,f3)==(1,2,3) and a6==6 and T1==7 and T2==21 and T2-f1-f2==(m1+m2)*a6 and (m1+m2)*a6==18 and (m2+m3)*a6==30 and F6-f3==39
SK6=sk(zemin(-.3,9.0,0),blok(.5,0,.9,.8,'$1$ kg'),blok(2.4,0,1.1,.9,'$2$ kg'),blok(4.5,0,1.3,1.0,'$3$ kg'),
 '\\draw[thick] (1.4,.4) -- (2.4,.4); \\node[above] at (1.9,.4) {$T_1$};','\\draw[thick] (3.5,.4) -- (4.5,.4); \\node[above] at (4.0,.4) {$T_2$};',fok((5.8,.5),(7.7,.5),'$F=42$ N'),sc=1.2)
q('0006',tipId=TIP['ip'][0],tip=TIP['ip'][1],z='zor',alt='Sürtünme Kuvveti',kaz='Sürtünmeli zeminde üç cisimli sistemde ortak ivmeyi ve ip gerilmesini hesaplar.',
 kart='K-FZDN2-06 (üç cisim, iki ip, sürtünmeli) · zor',kalip='şekilli',
 metin='Bir fizik deneyinde, kütleleri 1 kg, 2 kg ve 3 kg olan cisimler şekildeki gibi hafif ve esnemez iki iple birbirine bağlanmıştır. Cisimlerle yatay yüzey arasındaki kinetik sürtünme katsayısı her cisim için 0,1’dir (g = 10 m/s²). En sağdaki cisme yatay doğrultuda şekilde verilen kuvvet uygulanıyor ve cisimler iplerin gergin kaldığı biçimde birlikte hareket ediyor.\nBuna göre 2 kg ile 3 kg’lık cisimleri bağlayan ipteki gerilme kuvveti T₂ kaç N’dur?',
 sekil=SK6,dogru=21,yan=[(7,'1 kg’lık cismi çeken ipin gerilmesini (T₁ = 7 N) bulmuş; sorulan T₂’dir.','dikkat'),(18,'Sürtünmeyi hesaba katmadan T₂ = (1 + 2) × 6 yazmış; ip, geride kalan cisimlerin sürtünmesini de yenmelidir.','dikkat'),(30,'T₂’yi ipin önündeki cisimlerin (2 kg ve 3 kg) kütlesiyle hesaplamış.','bilgi'),(39,'3 kg’lık cisim için F − f yazıp kütle × ivme terimini eklememiş (42 − 3).','islem')],
 istenen='İp gerilmesi T₂ (N).',ip=['Önce bütün sistemin ivmesini bul; sonra T₂ ipinin hangi cisimlere etki ettiğine bak.'],
 bilgi=[B('Sürtünme kuvveti','kinetik sürtünme f = μ × m × g (yatay yüzeyde). Örnek: μ = 0,2, m = 5 kg, g = 10 m/s² için f = 10 N'),B('İp gerilmesi','ip, kendisinden geride ya da önde kalan cisimlerden birine uygulanan kuvvettir; o cisim için net kuvvet = kütle × ivme yazılır')],
 ad=[A('Sürtünme kuvvetleri','Her cisim için f = μ × m × g.','f₁ = 1 N, f₂ = 2 N, f₃ = 3 N'),A('Ortak ivme','Net kuvvet dış kuvvet eksi toplam sürtünmedir; toplam kütle 6 kg.','a = (42 − 6) ÷ 6 = 6 m/s²'),A('3 kg’lık cisme uygula','Cisme F ileri, T₂ ve f₃ geri etki eder.','F − T₂ − f₃ = m₃ × a'),A('Gerilmeyi bul','Değerleri yerine koy.','42 − T₂ − 3 = 18 → T₂ = 21 N'),A('Kontrol et','1 kg ve 2 kg’lık cisimler için T₂ ileri, sürtünmeler geri etki eder.','T₂ − 3 = 3 × 6 → T₂ = 21 N')],
 puf='Sürtünmeli sistemde önce ortak ivmeyi bul; gerilmeyi tek bir cisim ya da cisim grubu için sürtünmeyi de yazarak hesapla.')

# ================= 07 · v–t grafiği · orta · öncüllü =================
K(7,'gr','Newton’ın Hareket Yasaları','Hız–zaman grafiğinin eğimi ivmeyi verir; net kuvvet yönü ivme yönündedir; sabit hızda net kuvvet sıfırdır.','Sabit hızlı harekette net kuvvet olduğunu sanmak; yavaşlarken net kuvveti hareket yönünde almak.','orta','öncüllü',3)
m7=2; a1=Fr(6,2); assert a1==3 and m7*a1==6 and Fr(6-6,2)==0 and Fr(0-6,6-4)==-3
SK7=graf('8.4cm','5.4cm',7,7,1,1,'$t$ (s)','$v$ (m/s)','\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {(0,0) (2,6) (4,6) (6,0)};')
onc('0007',{1},S1,
 {1:('0–2 s aralığında ivme 6 ÷ 2 = 3 m/s²’dir; F = 2 × 3 = 6 N, hareket yönündedir.','0–2 s aralığında net kuvvetin 6 N olmadığını sanmış; ivme 3 m/s², kuvvet 2 × 3 = 6 N’dur.'),
  2:('2–4 s aralığında hız sabit olduğundan ivme ve net kuvvet sıfırdır.','Sabit hızda ivme sıfırdır; dolayısıyla net kuvvet de sıfırdır.'),
  3:('4–6 s aralığında hız azalır; ivme hareket yönüne zıt olduğundan net kuvvet de zıt yöndedir.','Hızın azaldığı aralıkta net kuvveti hareket yönünde almış; yavaşlayan cisimde net kuvvet harekete zıttır.')},
 'Yatay bir yolda doğrusal hareket eden 2 kg kütleli bir cismin hız–zaman grafiği şekildeki gibidir. Cisim yolda hız değiştirmektedir.\nBuna göre,\nI. 0–2 s aralığında cisme etki eden net kuvvet 6 N’dur.\nII. 2–4 s aralığında cisme hareket yönünde bir net kuvvet etki eder.\nIII. 4–6 s aralığında cisme etki eden net kuvvet hareket yönündedir.\nyargılarından hangileri doğrudur?',
 tipId=TIP['gr'][0],tip=TIP['gr'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Hız–zaman grafiğinin eğiminden ivmeyi ve net kuvveti yorumlar.',
 kart='K-FZDN2-07 (v–t grafiğinden net kuvvet) · öncüllü',istenen='Doğru olan yargılar.',ip=['Her aralıkta grafiğin eğimine, yani ivmenin işaretine ve büyüklüğüne bak.'],
 bilgi=[B('v–t grafiğinde ivme','eğim ivmeyi verir; ivme yönü net kuvvet yönüdür. Örnek: 4 s’de 8 m/s artan hızın ivmesi 2 m/s²’dir')],
 puf='v–t grafiğinde eğim ivme demektir; yatay doğru net kuvvetin sıfır olduğunu gösterir.',sekil=SK7)

# ================= 08 · etki–tepki · orta · öncüllü =================
K(8,'et','Newton’ın Hareket Yasaları','Etki–tepki kuvvetleri farklı cisimlere etkir; ağırlık ile tepki aynı cisme etkir, çift değildir.','Ağırlık ile masanın tepkisini etki–tepki çifti sanmak.','orta','öncüllü',3)
SK8=sk(zemin(-.5,4.5,0),'\\draw[thick,fill=gray!15] (-.5,-1.3) rectangle (4.5,0);','\\draw[thick,fill=gray!30] (1,0) rectangle (3,1.6);',
 f'\\draw[vurgu,very thick,{ARR}] (1.4,0) -- (1.4,.8); \\node[vurgu,left] at (1.4,.4) {{$N$}};',
 f'\\draw[vurgu,very thick,{ARR}] (2.6,.8) -- (2.6,0); \\node[vurgu,right] at (2.6,.4) {{$W$}};',
 f'\\draw[vurgu,very thick,{ARR}] (2.0,0) -- (2.0,-.8); \\node[vurgu,right] at (2.0,-.4) {{$F$}};',sc=1.6)
onc('0008',{2,3},['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],
 {1:('W ile N aynı cisme (kitaba) etki eder; etki–tepki kuvvetleri farklı cisimlere etkir, dolayısıyla çift değildir.','W ile N aynı cisme (kitaba) etki eder; etki–tepki kuvvetleri ise farklı cisimlere etki eder, bu yüzden çift değildir.'),
  2:('N masanın kitaba, F kitabın masaya uyguladığı kuvvettir; karşılıklı etkileşim olduğundan etki–tepki çiftidir.','N ile F’nin etki–tepki çifti olduğunu görmemiş; karşılıklı etkileşimde iki kuvvet çiftlenir.'),
  3:('Kitap durgun olduğundan net kuvvet sıfırdır; W = N.','Kitap durgunken W ve N’nin eşit olmadığını sanmış; net kuvvet sıfırsa kuvvetler dengelenir.')},
 'Yatay bir masanın üzerinde durgun hâlde bulunan bir kitaba ve masaya etki eden kuvvetler şekildeki gibi gösterilmiştir. Kitap masa yüzeyine tamamen oturmuştur. W, Dünya’nın kitaba uyguladığı çekim kuvveti; N, masanın kitaba uyguladığı kuvvet; F ise kitabın masaya uyguladığı kuvvettir.\nBuna göre,\nI. W ile N etki–tepki kuvvetleridir.\nII. N ile F etki–tepki kuvvetleridir.\nIII. W ile N’nin büyüklükleri eşittir.\nyargılarından hangileri doğrudur?',
 tipId=TIP['et'][0],tip=TIP['et'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Etki–tepki kuvvetlerini farklı cisimlere uygulanmalarına göre ayırt eder.',
 kart='K-FZDN2-08 (masadaki kitap, etki–tepki) · öncüllü',istenen='Doğru olan yargılar.',ip=['Etki–tepki çiftlerinin hangi cisimlere etki ettiğine bak.'],
 bilgi=[B('Etki–tepki yasası','A cismi B’ye kuvvet uygularsa B de A’ya büyüklükçe eşit, yönce zıt bir kuvvet uygular; bu kuvvetler farklı cisimlere etki ettiğinden birbirini dengelemez. Örnek: ayağın yere basma kuvveti ile yerin ayağı itme kuvveti')],
 puf='Etki–tepki kuvvetleri farklı cisimlere etkir; bir cisme etki eden iki kuvvet çift olamaz.',sekil=SK8)

# ================= 09 · patenciler · kolay =================
K(9,'et','Newton’ın Hareket Yasaları','İtişen iki cismin birbirine uyguladığı kuvvetler eşittir; ivmeler kütleyle ters orantılıdır.','Eşit kuvvet olduğundan hareket olmadığını ya da ivmelerin eşit olduğunu sanmak.','kolay','şekilli',2)
mP,mQ,Fp=60,40,120; assert Fr(Fp,mP)==2 and Fr(Fp,mQ)==3 and Fr(Fp,mP+mQ)==Fr(6,5) and Fr(Fp,mP-mQ)==6
SK9=sk(zemin(-.5,7.0,0),blok(.8,0,1.5,1.5,'$P$ $60$ kg'),blok(2.3,0,1.4,1.2,'$Q$ $40$ kg'),
 fok((.8,.75),(-.3,.75),'$F$'),fok((3.7,.6),(4.8,.6),'$F$'))
q('0009',tipId=TIP['et'][0],tip=TIP['et'][1],z='kolay',alt='Newton’ın Hareket Yasaları',kaz='Etki–tepki kuvvetlerinin eşitliğinden iki cismin ivmelerini hesaplar.',
 kart='K-FZDN2-09 (itişen patenciler) · kolay',kalip='şekilli',
 metin='Bir buz pateni gösterisinde, sürtünmesiz sayılabilecek buz pistinde kütleleri 60 kg ve 40 kg olan P ve Q patencileri şekildeki gibi birbirine değerek durmaktadır. Patenciler birbirini iterek zıt yönlerde harekete başlıyor. İtme süresince her bir patencinin diğerine uyguladığı kuvvetin büyüklüğü 120 N’dur.\nBuna göre bu sürede P patencisinin ivmesinin büyüklüğü kaç m/s²’dir?',
 sekil=SK9,dogru=2,yan=[(0,'Kuvvetler eşit ve zıt olduğundan birbirini dengelediğini, patencilerin hareket etmeyeceğini sanmış.','bilgi'),(1.2,'İki patenciyi tek cisim sayıp toplam kütleye bölmüş (120 ÷ 100).','bilgi'),(3,'Q patencisinin ivmesini (120 ÷ 40) bulmuş; P’nin kütlesi 60 kg’dır.','dikkat'),(6,'Kuvveti kütleler farkına bölmüş (120 ÷ 20).','islem')],
 istenen='P patencisinin ivmesi (m/s²).',ip=['P patencisine etki eden tek yatay kuvvetin hangisi olduğunu bul.'],
 bilgi=[B('Etki–tepki ve ivme','etki–tepki kuvvetleri eşit büyüklüktedir ama farklı cisimlere etki ettiğinden dengelenmez; her cisim kendi kütlesine göre ivmelenir. Örnek: 30 N kuvvet 5 kg’lık cisme 6 m/s² verir')],
 ad=[A('P’ye etki eden kuvvet','Q’nun P’ye uyguladığı kuvvet P’yi hızlandırır.','F = 120 N'),A('Yasayı uygula','P için net kuvvet 120 N’dur.','a = F ÷ m'),A('İvmeyi bul','P’nin kütlesi 60 kg’dır.','a = 120 ÷ 60 = 2 m/s²')],
 puf='Etki–tepki kuvvetleri eşit olsa da ivmeler eşit değildir; her cisim için F = m × a’yı ayrı yaz.')

# ================= 10 · sürtünmeli a–F grafiği · orta =================
K(10,'gr','Sürtünme Kuvveti','Sürtünmeli düzlemde a–F doğrusu F eksenini sürtünme kuvvetinde keser; eğim 1/m’dir.','Kütleyi F ÷ a ile bulup sürtünmeyi katmamak; eğimi kütle sanmak.','orta','grafik',3)
f10=6; assert Fr(14-6,4)==2 and Fr(14,4)==3.5 and Fr(4,8)==Fr(1,2) and Fr(6,4)==1.5
SK10=graf('8.4cm','5.6cm',16,5,2,1,'$F$ (N)','$a$ (m/s$^2$)','\\addplot[thick,vurgu,mark=*,mark size=1.5pt] coordinates {(0,0) (6,0) (14,4)};')
q('0010',tipId=TIP['gr'][0],tip=TIP['gr'][1],z='orta',alt='Sürtünme Kuvveti',kaz='Sürtünmeli düzlemdeki cismin ivme–kuvvet grafiğinden kütleyi bulur.',
 kart='K-FZDN2-10 (sürtünmeli a–F grafiği) · orta',kalip='grafik',
 metin='Bir öğrenci, yatay bir zeminde durgun hâldeki bir cisme dinamometre yardımıyla yatay doğrultuda büyüklüğü giderek artan bir F kuvveti uyguluyor. Cisim yalnızca F belli bir değeri aştığında harekete geçiyor; hareket başladıktan sonra zeminin uyguladığı kinetik sürtünme kuvveti sabit kalıyor. Cismin ivmesi ölçülerek elde edilen ivme–kuvvet grafiği şekildeki gibidir.\nBuna göre cismin kütlesi kaç kg’dır?',
 sekil=SK10,dogru=2,yan=[(0.5,'Grafiğin eğimini (a ÷ ΔF = 1/2) kütle sanmış; kütle eğimin tersidir.','bilgi'),(1.5,'Sürtünme kuvvetini ivmeye bölmüş (6 ÷ 4).','dikkat'),(3.5,'Sürtünmeyi hesaba katmadan F ÷ a (14 ÷ 4) almış.','dikkat'),(4,'Grafikteki ivme değerini kütle olarak yazmış.','dikkat')],
 istenen='Cismin kütlesi (kg).',ip=['Cisim hareket ederken kuvvetteki artışın ivmede ne kadar artışa yol açtığını düşün.'],
 bilgi=[B('Sürtünmeli harekette net kuvvet','Fnet = F − f. Hareket varken a = (F − f) ÷ m; a–F doğrusunun eğimi 1/m’dir. Örnek: 12 N’da a = 1, 20 N’da a = 3 olan cisim için ΔF ÷ Δa = 4 kg')],
 ad=[A('Hareket başlangıcı','Grafik, F = 6 N’dan sonra yükselir; sürtünme bu değere eşittir.','f = 6 N'),A('İki nokta seç','Hareketli bölgeden (6,0) ve (14,4) noktalarını al.','ΔF = 8 N, Δa = 4 m/s²'),A('Kütleyi bul','Net kuvvet değişimi kütle çarpı ivme değişimidir.','m = 8 ÷ 4 = 2 kg')],
 puf='Sürtünmeli a–F grafiğinde kütleyi doğrunun iki noktasındaki farklardan bul: m = ΔF ÷ Δa.')

# ================= 11 · üç bölgeli yol · zor · öncüllü =================
K(11,'su','Sürtünme Kuvveti','Her bölgede net kuvvet ayrı bulunur: sürtünmesizde a = F/m, sürtünmelide a = (F − f)/m; sürtünme F’ye eşit olunca hız sabit kalır.','Sürtünmeli bölgede cismin durduğunu sanmak; sürtünme kuvvetini uygulanan kuvvetten çıkarmayı unutmak.','zor','öncüllü',5)
m11,F11,fLM,fMN=5,30,10,30; aKL=Fr(F11,m11); aLM=Fr(F11-fLM,m11); aMN=Fr(F11-fMN,m11)
assert aKL==6 and aLM==4 and aMN==0
SK11=sk(zemin(-.3,8.8,0),'\\fill[gray!55] (2.8,-.2) rectangle (5.6,0); \\fill[gray!85] (5.6,-.2) rectangle (8.4,0);',blok(.3,0,1.0,.9,'$5$ kg'),fok((1.3,.45),(2.5,.45),'$F=30$ N'),
 '\\draw[dashed,gray] (2.8,-.2) -- (2.8,1.5); \\draw[dashed,gray] (5.6,-.2) -- (5.6,1.5);','\\node[below] at (0,-.2) {K}; \\node[below] at (2.8,-.2) {L}; \\node[below] at (5.6,-.2) {M}; \\node[below] at (8.4,-.2) {N};','\\node at (7.0,1.2) {$f=30$ N}; \\node at (4.2,1.2) {$f=10$ N};','\\node at (1.4,1.2) {sürtünmesiz};',sc=1.25)
onc('0011',{2,3},['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III'],
 {1:('L–M arasında net kuvvet 30 − 10 = 20 N’dur; ivme 20 ÷ 5 = 4 m/s²’dir, 6 m/s² değildir (6 m/s², sürtünmesiz K–L bölümündeki ivmedir).',
     'L–M arasında net kuvvet 30 − 10 = 20 N’dur; ivme 20 ÷ 5 = 4 m/s²’dir, 6 m/s² değildir (6 m/s², sürtünmesiz K–L bölümündeki ivmedir).'),
  2:('M–N arasında sürtünme kuvveti 30 N, F’ye eşittir; net kuvvet sıfır olduğundan hız değişmez.','M–N arasında net kuvvet sıfırdır; hız değişmez.'),
  3:('L–M arasında net kuvvet hareket yönünde (20 N) olduğundan cismin hızı artmaya devam eder.','L–M arasında net kuvvet hareket yönündedir; hız artar.')},
 'Yatay bir yolun K–L bölümü sürtünmesizdir; L–M ve M–N bölümlerinde ise cisme etki eden sürtünme kuvvetleri şekilde verilmiştir. K noktasında durmakta olan cisme, hareket boyunca sabit büyüklükte ve yatay F kuvveti uygulanıyor. Cismin kütlesi ve F kuvveti de şekilde gösterilmiştir. Cisim yoldan hiç ayrılmadan N noktasına kadar ilerliyor.\nBuna göre,\nI. Cismin L–M arasındaki ivmesi 6 m/s²’dir.\nII. Cismin hızı M–N arasında sabit kalır.\nIII. Cismin hızı L–M arasında artmaya devam eder.\nyargılarından hangileri doğrudur?',
 tipId=TIP['su'][0],tip=TIP['su'][1],z='zor',alt='Sürtünme Kuvveti',kaz='Sürtünmesiz ve farklı sürtünmeli bölgelerde net kuvvetten ivmeyi hesaplayıp hız değişimini yorumlar.',
 kart='K-FZDN2-11 (üç bölgeli yol) · öncüllü',istenen='Doğru olan yargılar.',ip=['Her bölge için net kuvveti ayrı bul; hız değişimi ivmenin işaretine bağlıdır.'],
 ad_on=[A('K–L bölümü','Sürtünme yoktur, net kuvvet F’dir.','a = 30 ÷ 5 = 6 m/s²')],
 bilgi=[B('Sürtünme ve net kuvvet','sürtünme kuvveti harekete zıttır: Fnet = F − f. Net kuvvet hareket yönündeyse hız artar, sıfırsa hız sabit kalır, zıt yöndeyse azalır. Örnek: 12 N çeken ve 4 N sürtünme olan 2 kg’lık cismin ivmesi 4 m/s²’dir')],
 puf='Her bölgede net kuvveti ayrı hesapla; net kuvvet sıfırsa cisim durmaz, o anki hızıyla sabit gider.',sekil=SK11)

# ================= 12 · sürtünmeli iple bağlı iki cisim · zor =================
K(12,'ip','Sürtünme Kuvveti','Sürtünmeli zeminde ortak ivme Fnet = F − f₁ − f₂ ile bulunur; ip gerilmesi önde kalan değil, arkada kalan cisim için T − f₁ = m₁a yazılarak bulunur.','Sürtünmeyi atlayarak T = m·a demek; ipin iki cisme eşit paylaştığını sanmak.','zor','şekilli',5)
m1,m2,f1,f2,F12=2,3,4,6,30; a12=Fr(F12-f1-f2,m1+m2); T12=f1+m1*a12
assert a12==4 and T12==12 and m1*a12==8 and F12//2==15 and F12-m2*a12==18 and F12-f1-f2==20 and F12-m2*a12-f2==T12
SK12=sk(zemin(-.3,9.0,0),blok(.5,0,1.0,.9,'$2$ kg'),blok(3.0,0,1.3,1.0,'$3$ kg'),'\\draw[thick] (1.5,.4) -- (3.0,.4); \\node[above] at (2.25,.4) {ip};',
 fok((4.3,.5),(6.3,.5),'$F=30$ N'),'\\draw[vurgu,very thick,'+ARR+'] (1.2,-.5) -- (.2,-.5); \\node[vurgu,below] at (.7,-.5) {$f_1=4$ N};','\\draw[vurgu,very thick,'+ARR+'] (4.0,-.5) -- (3.0,-.5); \\node[vurgu,below] at (3.5,-.5) {$f_2=6$ N};')
q('0012',tipId=TIP['ip'][0],tip=TIP['ip'][1],z='zor',alt='Sürtünme Kuvveti',kaz='Sürtünmeli zeminde iple bağlı iki cisimden oluşan sistemde ip gerilmesini bulur.',
 kart='K-FZDN2-12 (sürtünmeli zeminde iple bağlı iki cisim) · zor',kalip='şekilli',
 metin='Bir depoda işçi, yatay bir zeminde kütleleri 2 kg ve 3 kg olan iki kutuyu hafif ve esnemez bir iple bağlamıştır. Sağdaki kutuya şekilde verilen yatay kuvvet uygulanıyor ve kutular ip gergin kalacak biçimde ilerliyor. Hareket sırasında zeminin cisimlere uyguladığı kinetik sürtünme kuvvetleri şekilde gösterilmiştir.\nBuna göre ipteki gerilme kuvveti kaç N’dur?',
 sekil=SK12,dogru=12,yan=[(8,'Soldaki cismin sürtünmesini unutmuş: T = m × a = 2 × 4 = 8 N.','dikkat'),(15,'Uygulanan kuvvetin iki cisme eşit paylaşıldığını sanmış (30 ÷ 2).','bilgi'),(18,'Sağdaki cisim için F − m × a almış ve onun sürtünmesini (6 N) çıkarmamış.','dikkat'),(20,'Net kuvveti (30 − 4 − 6) ipteki gerilme sanmış.','bilgi')],
 istenen='İpteki gerilme kuvveti (N).',ip=['Önce tüm sistemi tek cisim say; sonra ipin hangi cismi hızlandırdığına bak.'],
 bilgi=[B('Sürtünmeli sistem','sistemin net kuvveti, dış kuvvetlerin farkıdır: Fnet = F − f₁ − f₂; ortak ivme a = Fnet ÷ (toplam kütle). Tek bir cisim için sürtünme ve gerilme ayrı yazılır. Örnek: 10 kg’a 50 N, toplam sürtünme 20 N ise a = 3 m/s²')],
 ad=[A('Net kuvvet','Sürtünme kuvvetleri harekete zıttır.','Fnet = 30 − 4 − 6 = 20 N'),A('Ortak ivme','Toplam kütle 5 kg’dır.','a = 20 ÷ 5 = 4 m/s²'),A('Soldaki cisme uygula','2 kg’lık cismi ip çeker, sürtünme geri çeker.','T − f₁ = m₁ × a'),A('Gerilmeyi bul','Değerleri yerine koy.','T − 4 = 2 × 4 → T = 12 N'),A('Kontrol et','3 kg’lık cisim için aynı gerilmeyi doğrula.','30 − T − 6 = 3 × 4 → T = 12 N')],
 puf='Sürtünmeli sistemde önce ortak ivmeyi bul; gerilmeyi tek cisim için sürtünmeyi de yazarak hesapla.')

# ================= 13 · asılı iki cisim · kolay =================
K(13,'ip','Newton’ın Hareket Yasaları','Durgun asılı cisimlerde üstteki ip, altındaki bütün cisimlerin ağırlığını taşır.','Üstteki ipin yalnız bir cismin ağırlığını taşıdığını sanmak.','kolay','şekilli',2)
mu_,ma_=3,2; g=10; T13=(mu_+ma_)*g; assert T13==50 and ma_*g==20 and mu_*g==30 and mu_*ma_*g==60 and mu_+ma_==5
SK13=sk('\\fill[gray!30] (-1,3.8) rectangle (1.6,4.0); \\draw (-1,3.8) -- (1.6,3.8);','\\draw[thick] (.3,3.8) -- (.3,2.5); \\node[right] at (.3,3.2) {$T_1$};',blok(-.3,1.6,1.2,.9,'$3$ kg'),'\\draw[thick] (.3,1.6) -- (.3,.7); \\node[right] at (.3,1.15) {$T_2$};',blok(-.3,-.2,1.2,.9,'$2$ kg'))
q('0013',tipId=TIP['ip'][0],tip=TIP['ip'][1],z='kolay',alt='Newton’ın Hareket Yasaları',kaz='Durgun asılı iki cismi taşıyan üstteki ipin gerilmesini bulur.',
 kart='K-FZDN2-13 (asılı iki cisim) · kolay',kalip='şekilli',
 metin='Bir müze salonunda tavana asılan hafif bir ipin ucuna 3 kg kütleli bir cisim bağlanmış; bu cismin altına da başka bir hafif ip ile 2 kg kütleli ikinci bir cisim asılmıştır. Düzenek şekildeki gibi durgun hâldedir (g = 10 m/s²).\nBuna göre tavana bağlı üstteki ipte oluşan T₁ gerilme kuvveti kaç N’dur?',
 sekil=SK13,dogru=50,yan=[(5,'Toplam kütleyi (5 kg) gerilme olarak yazmış; g ile çarpmamış.','islem'),(20,'Alttaki ipin gerilmesini (T₂ = 20 N) bulmuş; sorulan üstteki ip.','dikkat'),(30,'Üstteki ipin yalnızca üstteki cismi taşıdığını sanmış.','bilgi'),(60,'İki kütleyi ve g’yi birbiriyle çarpmış (3 × 2 × 10).','islem')],
 istenen='Üstteki ipteki gerilme T₁ (N).',ip=['Üstteki ip hangi cisimlerin ağırlığını dengeliyor?'],
 bilgi=[B('Denge ve gerilme','durgun cisimde net kuvvet sıfırdır: yukarı gerilme, aşağı ağırlık. Ağırlık W = m × g. Örnek: 4 kg’lık durgun cismi tutan ipte g = 10 m/s² için gerilme 40 N’dur')],
 ad=[A('Asılı kütle','Üstteki ip iki cismi birlikte taşır.','m = 3 + 2 = 5 kg'),A('Denge koşulu','Cisimler durgun olduğundan gerilme toplam ağırlığa eşittir.','T₁ = m × g'),A('Gerilmeyi bul','Değerleri yerine koy.','T₁ = 5 × 10 = 50 N')],
 puf='Durgun asılı sistemde ip, altında kalan bütün cisimlerin ağırlığını taşır.')

# ================= 14 · limit hız grafiği · orta · öncüllü =================
K(14,'li','Newton’ın Hareket Yasaları','Hava direnci hızla artar; v–t eğrisinin eğimi (ivme) giderek azalır ve limit hızda net kuvvet sıfır olur.','Limit hızda cismin durduğunu ya da hava direncinin ağırlıktan büyük olduğunu sanmak.','orta','öncüllü',3)
vl,tau=40,4; v4=vl*(1-exp(-4/tau)); v0=0; v16=vl*(1-exp(-16/tau)); v20=vl*(1-exp(-20/tau))
assert (v4-v0)/4>(v20-v16)/4 and v20<vl and vl-v20<0.8 and abs(vl/tau-10)<1e-9
SK14=graf('8.6cm','5.6cm',21,46,4,10,'$t$ (s)','$v$ (m/s)','\\addplot[gray,dashed] coordinates {(0,40) (21,40)};','\\addplot[thick,vurgu,domain=0:20,samples=60] {40*(1-exp(-x/4))};')
onc('0014',{1,2},['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 {1:('0–4 s aralığında hız çok artar, 16–20 s aralığında az artar; eğim (ivme) küçülmüştür.','0–4 s ile 16–20 s aralıklarındaki ivmeleri yanlış karşılaştırmış; eğri başta daha diktir, ivme başta büyüktür.'),
  2:('Hız 40 m/s’ye yaklaşırken ivme sıfıra, dolayısıyla net kuvvet sıfıra yaklaşır.','Limit hıza yaklaşırken net kuvvetin sıfıra gittiğini görmemiş.'),
  3:('Hava direnci hızla artar; limit hıza yaklaşırken azalmaz, ağırlığa eşit olmaya doğru artar.','Hava direnci hızla artar; limit hıza yaklaşırken azalmaz, ağırlığa eşitlenene kadar artar.')},
 'Yüksek bir irtifada havada asılı duran bir helikopterden büyük bir yük bırakılıyor ve yük hava direncinin etkisinde dikey olarak düşüyor. Yükün hız–zaman grafiği şekildeki gibi elde ediliyor.\nBuna göre,\nI. 0–4 s aralığındaki ivmenin büyüklüğü 16–20 s aralığındakinden büyüktür.\nII. Yükün hızı 40 m/s’ye yaklaşırken yüke etki eden net kuvvet sıfıra yaklaşır.\nIII. Yükün hızı 40 m/s’ye yaklaşırken hava direnci kuvveti azalır.\nyargılarından hangileri doğrudur?',
 tipId=TIP['li'][0],tip=TIP['li'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Hava direncinde düşen cismin hız–zaman grafiğini yorumlayarak limit hızı açıklar.',
 kart='K-FZDN2-14 (helikopterden bırakılan yük, limit hız grafiği) · öncüllü',istenen='Doğru olan yargılar.',ip=['Eğrinin eğimini erken ve geç aralıklarda karşılaştır; limit hızda eğimin ne olduğunu düşün.'],
 bilgi=[B('Limit hız','düşen cisme aşağı ağırlık, yukarı hava direnci etki eder. Hız arttıkça direnç artar; direnç ağırlığa eşit olunca net kuvvet sıfır olur ve cisim sabit hızla (limit hız) düşer')],
 puf='Hava direncinde düşen cismin ivmesi azalarak sıfıra gider; limit hızda direnç ağırlığa eşittir.',sekil=SK14)

# ================= 15 · serbest düşme · kolay · öncüllü (şekilsiz) =================
K(15,'li','Newton’ın Hareket Yasaları','Havasız ortamda tüm cisimler aynı ivmeyle düşer; havada fark hava direncinden doğar.','Ağır cismin daha hızlı düştüğünü sanmak.','kolay','öncüllü',3)
onc('0015',{1},S1,
 {1:('Havası boşaltılmış ortamda yalnız ağırlık etki eder; ivme g’dir ve cisimlerin kütlesinden bağımsızdır, ikisi aynı anda düşer.','Havasız ortamda metal paranın daha önce düşeceğini sanmış; kütleye bakılmaksızın ivme g’dir.'),
  2:('Serbest düşmede ivme g’dir ve kütleye bağlı değildir; “ağır cisim büyük ivmeyle düşer” yanlış bir kavramdır.','Serbest düşmede ivme g’dir ve kütleden bağımsızdır.'),
  3:('Hava direnci düşen cisme ağırlığın tersi yönde (yukarı) etki eder.','Hava direnci harekete zıt yönde, yani düşen cisimde yukarı yönde etki eder.')},
 'Bir fizik öğretmeni, içindeki hava boşaltılmış uzun bir cam tüpün üst ucundan bir tüyü ve bir metal parayı aynı anda serbest bırakıyor. Daha sonra aynı deneyi havası boşaltılmamış tüple tekrarlıyor ve tüyün metal paradan daha geç tüpün dibine ulaştığını gözlüyor. Öğrenciler, deneyi serbest düşme ve hava direnci açısından yorumluyor.\nBuna göre,\nI. Havası boşaltılmış tüpte tüy ile metal para aynı anda tüpün dibine ulaşır.\nII. Serbest düşmede ağır cisimlerin ivmesi hafif cisimlerinkinden büyüktür.\nIII. Hava direnci, düşen cisme ağırlıkla aynı yönde etki eder.\nyargılarından hangileri doğrudur?',
 tipId=TIP['li'][0],tip=TIP['li'][1],z='kolay',alt='Newton’ın Hareket Yasaları',kaz='Serbest düşme ve hava direncini nitel olarak ayırt eder.',
 kart='K-FZDN2-15 (havasız tüpte düşme) · öncüllü',istenen='Doğru olan yargılar.',ip=['Havasız ortamda düşen cisme etki eden kuvvetin ne olduğunu ve ivmenin neye bağlı olduğunu düşün.'],
 bilgi=[B('Serbest düşme','yalnızca ağırlığın etkisindeki harekettir; ivme tüm cisimler için aynı (g) ve kütleden bağımsızdır. Hava direnci hareketin tersi yönde etki eder ve cisimlerin farklı düşmesine neden olur')],
 puf='Havasız ortamda her cisim aynı ivmeyle düşer; farkı yaratan hava direncidir.')

# ================= 16 · paraşüt açılırken ivme · zor =================
K(16,'li','Newton’ın Hareket Yasaları','Sabit hızda direnç ağırlığa eşittir; paraşüt açılınca direnç artar, net kuvvet yukarı olur ve ivme (F_hava − mg) ÷ m ile bulunur.','Ağırlığı çıkarmamak ya da eklemek; sabit hızda direncin sıfır olduğunu düşünmek.','zor','şekilli',4)
m16,g=80,10; W16=m16*g; Fd0=W16; Fd1=Fr(5,2)*Fd0; a16=(Fd1-W16)/m16
assert Fd0==800 and Fd1==2000 and a16==15 and Fd1/m16==25 and (Fd1+W16)/m16==35 and g==10
SK16=sk('\\draw[thick] (-1.2,2.3) arc[start angle=180,end angle=0,radius=1.2]; \\draw[thick] (-1.2,2.3) -- (1.2,2.3);','\\draw[thick] (-1.2,2.3) -- (0,1.0); \\draw[thick] (1.2,2.3) -- (0,1.0); \\draw[thick] (0,2.3) -- (0,1.0);',
 '\\draw[thick,fill=white] (0,.8) circle (.2); \\draw[thick] (0,.6) -- (0,-.2); \\draw[thick] (-.35,.3) -- (0,.45) -- (.35,.3); \\draw[thick] (-.3,-.9) -- (0,-.2) -- (.3,-.9);',
 '\\node[right] at (.5,.2) {$80$ kg};',sc=1.3)
q('0016',tipId=TIP['li'][0],tip=TIP['li'][1],z='zor',alt='Newton’ın Hareket Yasaları',kaz='Sabit hızlı düşüşteki hava direncinden yola çıkarak paraşüt açıldığı andaki ivmeyi bulur.',
 kart='K-FZDN2-16 (paraşüt açılırken ivme) · zor',kalip='şekilli',
 metin='Uçaktan atlayan bir paraşütçü, paraşütünü açmadan önce bir süre sonra sabit hızla düşmektedir. Paraşütçünün kütlesi şekilde verilmiştir. Paraşütünü açtığı anda hava direnci kuvveti, paraşüt açılmadan önceki sabit hızla düşerkenki değerinin 2,5 katına çıkmaktadır. Rüzgâr ihmal edilmektedir (g = 10 m/s²).\nBuna göre paraşüt açıldığı an paraşütçünün ivmesinin büyüklüğü kaç m/s²’dir?',
 sekil=SK16,dogru=15,yan=[(0,'Hava direnci ile ağırlığın hâlâ dengede olduğunu, hızın sabit kalacağını düşünmüş.','bilgi'),(10,'Paraşütçüyü serbest düşüyormuş gibi alıp ivmeyi g almış.','bilgi'),(25,'Ağırlığı çıkarmadan yeni hava direncini (2000 N) kütleye bölmüş.','dikkat'),(35,'Ağırlığı hava direncine eklemiş: (2000 + 800) ÷ 80.','islem')],
 istenen='Paraşüt açıldığı andaki ivmenin büyüklüğü (m/s²).',ip=['Paraşütçünün sabit hızla düştüğü durumda hava direnci ile ağırlık arasındaki ilişkiyi düşün.'],
 bilgi=[B('Hava direncinde net kuvvet','düşen cisimde ağırlık aşağı, hava direnci yukarı etki eder; sabit hızda ikisi eşittir. Direnç ağırlıktan büyükse net kuvvet yukarıdır, a = (Fhava − W) ÷ m ve cismin hızı azalır. Örnek: 50 kg’lık cismin W = 500 N, direnç 600 N ise a = 2 m/s²')],
 ad=[A('Ağırlığı bul','Ağırlık kütle ile g’nin çarpımıdır.','W = 80 × 10 = 800 N'),A('Sabit hızdaki direnç','Sabit hızda net kuvvet sıfırdır; direnç ağırlığa eşittir.','F₁ = 800 N'),A('Açılma anındaki direnç','Direnç 2,5 katına çıkar; net kuvvet yukarı yönlüdür.','F₂ = 2,5 × 800 = 2000 N ; Fnet = 2000 − 800 = 1200 N'),A('İvmeyi bul','Net kuvveti kütleye böl.','a = 1200 ÷ 80 = 15 m/s²')],
 puf='Sabit hızda hava direnci ağırlığa eşittir; direnç değişince ivmeyi net kuvvetten bul.')

# ================= 17 · ağırlık–kütle, tablo · orta · öncüllü =================
K(17,'ag','Newton’ın Hareket Yasaları','Kütle her yerde aynıdır; ağırlık W = m·g gezegenin g değerine bağlıdır.','Kütlenin de gezegene göre değiştiğini sanmak; ağırlık oranlarını ters almak.','orta','öncüllü',3)
gD,gX,gY=10,5,20; mm=30; assert mm*gX==150 and mm*gY==600 and mm*gD==300 and Fr(mm*gY,mm*gX)==4 and mm*gX!=300
SK17=tablo_svg(['Gök cismi','Yerçekimi ivmesi (m/s²)'],[['Dünya',gD],['X gezegeni',gX],['Y gezegeni',gY]])
onc('0017',{1},S1,
 {1:('Kütle cismin değişmeyen özelliğidir; her gök cisminde 30 kg’dır.','Kütlenin g’ye göre değiştiğini sanmış; kütle her yerde aynıdır.'),
  2:('X’te ağırlık 30 × 5 = 150 N’dur; 300 N Dünya’daki ağırlıktır.','X’te W = 30 × 5 = 150 N’dur; Dünya’da ise 30 × 10 = 300 N’dur.'),
  3:('Y’de 600 N, X’te 150 N olduğundan Y’deki ağırlık X’tekinin 4 katıdır, 2 katı değil.','Ağırlık g ile orantılıdır; Y’deki ağırlık X’tekinin 20 ÷ 5 = 4 katıdır, 2 katı değildir.')},
 'Aşağıdaki tabloda Dünya ile X ve Y gezegenlerinin yüzeyindeki yerçekimi ivmeleri verilmiştir. Kütlesi Dünya’da 30 kg olarak ölçülen bir cisim, uzay aracıyla bu üç gök cismine sırayla götürülüyor ve her birinin yüzeyinde dinamometreyle tartılıyor.\nBuna göre,\nI. Cismin kütlesi X gezegeninde 30 kg’dır.\nII. Cismin X gezegenindeki ağırlığı 300 N’dur.\nIII. Cismin Y gezegenindeki ağırlığı X gezegenindekinin 2 katıdır.\nyargılarından hangileri doğrudur?',
 tipId=TIP['ag'][0],tip=TIP['ag'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Kütle ve ağırlığın farklı gök cisimlerinde nasıl değiştiğini ayırt eder.',
 kart='K-FZDN2-17 (farklı gezegenlerde ağırlık) · öncüllü',istenen='Doğru olan yargılar.',kalip='tablo',ip=['Kütle ile ağırlığın hangisinin gezegene bağlı olduğunu düşün; ağırlığı W = m × g ile her gezegen için hesapla.'],
 bilgi=[B('Kütle ve ağırlık','kütle madde miktarıdır ve her yerde aynıdır (kg). Ağırlık yerçekimi kuvvetidir: W = m × g (N) ve g’ye bağlıdır. Örnek: 3 kg’lık cisim g = 6 m/s² olan yerde 18 N çeker')],
 puf='Kütle yer değiştirmez; ağırlık g ile orantılı olarak değişir.',sekil=SK17)

# ================= 18 · terazi ve dinamometre · zor =================
K(18,'ag','Newton’ın Hareket Yasaları','Eşit kollu terazi kütleyi, dinamometre ağırlığı ölçer; gezegen değişince kütle sabit kalır, dinamometre değeri m·g ile değişir.','Terazi ve dinamometre ölçümlerini karıştırmak; kütleyi g ile çarpmak yerine bölmek.','orta','şekilli',4)
mb,gE,gP=2,10,4; W_E=mb*gE; W_P=mb*gP; assert W_E==20 and W_P==8 and Fr(W_E,gP)==5 and W_E*gP==80 and mb==2
SK18=sk('\\draw[thick] (-2.4,1.8) -- (2.4,1.8); \\draw[thick] (0,1.8) -- (-.4,.2) -- (.4,.2) -- cycle; \\fill (0,1.8) circle (1.5pt);',
 '\\draw[thick] (-2,1.8) -- (-2.6,.6) -- (-1.4,.6) -- cycle; \\draw[thick] (2,1.8) -- (1.4,.6) -- (2.6,.6) -- cycle;',
 blok(-2.25,.6,.5,.5,'X'),'\\draw[thick,fill=gray!25] (1.7,.6) rectangle (2.3,1.1); \\node at (2.0,.85) {\\scriptsize $2$ kg};',
 '\\draw[thick] (4.3,.4) rectangle (4.9,1.9); \\draw[thick] (4.6,1.9) -- (4.6,2.3); \\draw[thick] (4.6,.4) -- (4.6,-.1);',
 '\\foreach \\y in {.7,.95,1.2,1.45} {\\draw (4.3,\\y) -- (4.5,\\y);}', blok(4.3,-.7,.6,.6,'X'),
 '\\node at (0,-.4) {eşit kollu terazi}; \\node at (4.6,-1.2) {dinamometre};')
q('0018',tipId=TIP['ag'][0],tip=TIP['ag'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Eşit kollu terazi (kütle) ve dinamometre (ağırlık) ölçümlerini farklı gezegenlerde ayırt eder.',
 kart='K-FZDN2-18 (terazi–dinamometre, gezegen değişimi) · zor',kalip='şekilli',
 metin='Bir öğrenci Dünya’da (g = 10 m/s²) X cismini eşit kollu terazide şekildeki gibi dengeliyor ve aynı cismi dinamometreye asıyor. Sonra aletleri ve X cismini yerçekimi ivmesi 4 m/s² olan başka bir gezegene götürüp aynı ölçümleri yapıyor.\nBuna göre X cismi bu gezegende dinamometreyi kaç N gösterir?',
 sekil=SK18,dogru=8,yan=[(2,'Kütle değerini (2 kg) dinamometre okuması sanmış.','bilgi'),(5,'Dünya’daki ağırlığı yerçekimi ivmesine bölmüş (20 ÷ 4).','islem'),(20,'Ağırlığın gezegenden bağımsız olduğunu, Dünya’daki değerin aynen okunacağını sanmış.','bilgi'),(80,'Dünya’daki ağırlığı yeni g ile çarpmış (20 × 4).','islem')],
 istenen='Dinamometrenin bu gezegendeki değeri (N).',ip=['Eşit kollu terazinin neyi ölçtüğünü ve bu niceliğin gezegen değişince değişip değişmediğini düşün.'],
 bilgi=[B('Terazi ve dinamometre','eşit kollu terazi kütleleri karşılaştırır; sonuç g’den bağımsızdır. Dinamometre ağırlığı (kuvveti) ölçer: W = m × g. Örnek: 3 kg’lık cisim g = 10 m/s²’de 30 N, g = 2 m/s²’de 6 N gösterir')],
 ad=[A('Kütleyi bul','Terazi dengesi kütlelerin eşit olduğunu gösterir; kütle gezegende değişmez.','m = 2 kg'),A('Yeni g’yi al','Yeni gezegende yerçekimi ivmesi 4 m/s²’dir.','g = 4 m/s²'),A('Ağırlığı hesapla','Dinamometre ağırlığı gösterir.','W = 2 × 4 = 8 N'),A('Kontrol et','Dünya’da 20 N olan değer, g oranı kadar küçülür.','20 × 4 ÷ 10 = 8 N')],
 puf='Gezegen değişince kütle sabit kalır; dinamometre değeri m × g ile yeniden hesaplanır.')

# ================= 19 · asansörde tartı · orta · öncüllü =================
K(19,'as','Newton’ın Hareket Yasaları','Tartı, kişiye uyguladığı tepki kuvvetini gösterir: ivme yukarıysa ağırlıktan büyük, aşağıysa küçüktür; sabit hızda ağırlığa eşittir.','Hızın yönüne bakıp ivme yönünü karıştırmak; sabit hızlı harekette değişim beklemek.','orta','öncüllü',3)
SK19=sk('\\draw[thick] (0,0) rectangle (2.4,3.2); \\draw[thick] (1.2,3.2) -- (1.2,4.0);',
 '\\draw[thick,fill=gray!25] (.5,0) rectangle (1.9,.28);','\\draw[thick,fill=white] (1.2,2.55) circle (.22); \\draw[thick] (1.2,2.33) -- (1.2,1.3); \\draw[thick] (.75,1.95) -- (1.2,2.1) -- (1.65,1.95); \\draw[thick] (.95,.28) -- (1.2,1.3) -- (1.45,.28);',
 '\\node[right,align=left] at (2.8,.15) {durgun asansörde\\\\tartı: $600$ N};')
onc('0019',{1},S1,
 {1:('Yukarı doğru hızlanan asansörde ivme yukarıdır; N − mg = ma olduğundan N > mg, tartı 600 N’dan büyük okur.','Yukarı hızlanırken tartının ağırlıktan küçük okuyacağını sanmış; ivme yukarıysa tepki ağırlıktan büyüktür.'),
  2:('Aşağı doğru hızlanırken ivme aşağıdır; mg − N = ma olduğundan N < mg, tartı 600 N’dan küçük okur.','Aşağı doğru hızlanırken ivme aşağıdır; mg − N = ma olduğundan N < mg ve tartı küçük okur.'),
  3:('Sabit hızla çıkarken ivme sıfırdır; N = mg, tartı 600 N okur. Hız yukarı olması tartıyı büyütmez.','Sabit hızda ivme sıfırdır; N = mg olduğundan tartı değeri değişmez.')},
 'Bir kişi, tartının üzerinde durarak asansörle seyahat ediyor. Asansör durgunken tartının gösterdiği değer şekilde verilmiştir. Kişi, asansör hareket ederken tartının okumasını farklı anlarda izliyor ve aşağıdaki yargıları öne sürüyor (g = 10 m/s²).\nI. Asansör yukarı doğru hızlanırken tartı 600 N’dan büyük değer okur.\nII. Asansör aşağı doğru hızlanırken tartı 600 N’dan büyük değer okur.\nIII. Asansör yukarı doğru sabit hızla çıkarken tartı 600 N’dan büyük değer okur.\nBuna göre hangi yargılar doğrudur?',
 tipId=TIP['as'][0],tip=TIP['as'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Asansörün ivme yönüne göre tartı okumasının ağırlıktan büyük, küçük ya da eşit olduğunu belirler.',
 kart='K-FZDN2-19 (asansörde tartı, nitel) · öncüllü',istenen='Doğru olan yargılar.',ip=['Tartı kişiye uyguladığı tepki kuvvetini gösterir; her durumda ivmenin yönünü belirle ve kuvvetleri karşılaştır.'],
 bilgi=[B('Asansörde tepki','tartı N’yi (kişiye uyguladığı kuvveti) gösterir. İvme yukarıysa N > mg, aşağıysa N < mg, ivme sıfırsa N = mg. Örnek: aşağı doğru hızlanan asansörde kişi kendini hafif hisseder')],
 puf='Tartının okuması ivme yönüne bağlıdır: yukarı ivme büyütür, aşağı ivme küçültür, sabit hız değiştirmez.',sekil=SK19)

# ================= 20 · asansörde tartı tablosu · orta · öncüllü =================
K(20,'as','Newton’ın Hareket Yasaları','Tartı okumasından net kuvvet ve ivme yönü çıkarılır; ağırlığa eşit okuma ivmenin sıfır olduğunu gösterir, durgunluğu değil.','Ağırlığa eşit okumayı asansörün durduğu anlamında yorumlamak.','orta','öncüllü',3)
m20=60; assert (720-m20*g)==120 and (m20*g-480)==120 and 720>600>480 and Fr(120,m20)==2
SK20=tablo_svg(['Zaman aralığı','Tartının okuması (N)'],[['0 – 2 s',720],['2 – 6 s',600],['6 – 8 s',480]])
onc('0020',{1,2,3},S1,
 {1:('720 N > 600 N olduğundan net kuvvet yukarıdır; ivme yukarı yönlüdür.','0–2 s aralığında ivmeyi yukarı yönlü görmemiş; tartı ağırlıktan büyükse ivme yukarıdır.'),
  2:('Tartı 600 N = mg okuduğundan net kuvvet sıfırdır.','2–6 s aralığında net kuvvetin sıfır olmadığını sanmış; okuma ağırlığa eşit olduğundan net kuvvet sıfırdır.'),
  3:('480 N < 600 N olduğundan net kuvvet aşağıdadır; ivme aşağı yönlüdür.','6–8 s aralığında ivmenin aşağı yönlü olduğunu görmemiş; tartı ağırlıktan küçükse ivme aşağıdır.')},
 'Kütlesi 60 kg olan bir kişi, düşey doğrultuda hareket eden bir asansörün tabanındaki tartının üzerinde durmaktadır. Tartının farklı zaman aralıklarında gösterdiği değerler aşağıdaki tabloda verilmiştir (g = 10 m/s²).\nBuna göre,\nI. 0–2 s aralığında asansörün ivmesi yukarı yönlüdür.\nII. 2–6 s aralığında kişiye etki eden net kuvvet sıfırdır.\nIII. 6–8 s aralığında asansörün ivmesi aşağı yönlüdür.\nyargılarından hangileri kesinlikle doğrudur?',
 tipId=TIP['as'][0],tip=TIP['as'][1],z='orta',alt='Newton’ın Hareket Yasaları',kaz='Tartı okumalarından asansörün ivme yönünü ve net kuvveti yorumlar.',
 kart='K-FZDN2-20 (asansörde tartı tablosu) · öncüllü',istenen='Kesinlikle doğru olan yargılar.',kalip='tablo',ip=['Her aralıkta tartının gösterdiği değeri kişinin ağırlığı ile karşılaştır.'],
 bilgi=[B('Net kuvvet ve ivme yönü','kişiye tartının tepkisi yukarı, ağırlık aşağı etki eder. Tepki ağırlıktan büyükse net kuvvet ve ivme yukarı, küçükse aşağı yönlüdür; eşitse ivme sıfırdır. Örnek: 50 kg’lık kişide 450 N okuma ivmenin aşağı yönlü olduğunu gösterir')],
 puf='Tartı ağırlıktan büyükse ivme yukarı, küçükse aşağı, eşitse sıfırdır; hız yönü bu sonuca karışmaz.',sekil=SK20)

H.bitir(P,'dinamikiki','fiz|Dinamik')
