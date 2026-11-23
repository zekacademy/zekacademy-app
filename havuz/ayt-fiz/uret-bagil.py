"""AYT Fizik · Bağıl Hareket (nehir/akıntı dahil) · 20 soru. Kardeş yok, ipucu 1.
Şekil verileri betikteki aynı sayılardan üretilir; her cevap ve çeldirici assert edilir."""
import sys,os,json
from fractions import Fraction as Fr
from math import sqrt
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
KONU_AD='Bağıl Hareket'; KEY='afiz|Bağıl Hareket'
P=Parti('bagil',KONU_AD,KEY,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Fizik bağıl hareket soruları (yalnız mantık) · 345 AYT Fizik s.22–27 · Bilgi Sarmal AYT denemeleri'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
def q(no,ad,**k):
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),**k)

# ---------- TikZ yardımcıları ----------
def tk(body,opt=''): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small'+opt+']\n'+body+'\n\\end{tikzpicture}')
AK='blue!65!black'
def V(p,q_,lab='',side='above',col='vurgu'):
    n=f' node[midway,{side}] {{{lab}}}' if lab else ''
    return '\\draw[%s,very thick,-{Stealth[length=2mm,width=1.8mm]}] (%.3f,%.3f) -- (%.3f,%.3f)%s;'%(col,p[0],p[1],q_[0],q_[1],n)
def car(x,y,lab,w=1.0):
    return ('\\draw[thick,fill=gray!25,rounded corners=2pt] (%.3f,%.3f) rectangle (%.3f,%.3f);\\node at (%.3f,%.3f) {%s};'%(x-w/2,y+.15,x+w/2,y+.6,x,y+.375,lab)+
            '\\draw[thick,fill=white] (%.3f,%.3f) circle (.13) (%.3f,%.3f) circle (.13);'%(x-w/3,y+.13,x+w/3,y+.13))
def road(x0,x1,y=0): return '\\draw[thick] (%.2f,%.2f) -- (%.2f,%.2f);'%(x0,y,x1,y)
def river_h(x0,x1,h): return '\\fill[blue!8] (%.2f,0) rectangle (%.2f,%.2f);\\draw[thick] (%.2f,0) -- (%.2f,0) (%.2f,%.2f) -- (%.2f,%.2f);'%(x0,x1,h,x0,x1,x0,h,x1,h)
def dim(p,q_,lab,side='left'): return '\\draw[<->,thin] (%.3f,%.3f) -- (%.3f,%.3f) node[midway,%s,fill=white,inner sep=1pt] {%s};'%(p[0],p[1],q_[0],q_[1],side,lab)
def f1(items): return '\n'.join(items)

# ---------- betik içi gerekçe/öncül yardımcısı ----------
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
        cel=' '.join(stm[i][3] for i in d)
        yan.append((a,cel,'bilgi'))
    metin=giris+'\nBuna göre,\n'+'\n'.join(f'{ROM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+kok
    ad=[A(f'{ROM[i]}. yargıyı incele',s[2],f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış')) for i,s in enumerate(stm)]
    ad.append(A('Sonucu yaz','Doğru olan yargıları birleştir.',' · '.join(f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış') for i,s in enumerate(stm))+' → '+COMB[ci][0]))
    q(no,ad,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kart=kart,kalip=kalip,metin=metin,dogru=COMB[ci][0],yan=yan,sira=[a for a,b in win],
      istenen=istenen,ip=ip,bilgi=bilgi,puf=puf,sekil=sekil)

# ================= KARTLAR =================
kartla('K-AFBH-01','Zıt/aynı yönlü araçların bağıl hızı','Yön seçilip hızlar işaretlenir; v_AB = v_A − v_B. Zıt yönde büyüklükler toplanır, aynı yönde çıkarılır; yetişme için kapanma hızı kullanılır.','Bağıl hızı yalnız bir cismin yere göre hızı sanmak; zıt yönde çıkarmak.','orta','şekilli',3,'bh-dogrusal','Aynı doğrultuda bağıl hız ve yetişme')
kartla('K-AFBH-02','Akıntıda gidiş–dönüş ve su çerçevesi','Yere göre hız = suya göre hız ± akıntı; gidiş ve dönüş süreleri ayrı hesaplanır. Su çerçevesinde cisimler akıntı yokmuş gibi davranır.','Dönüş süresini gidiş süresine eşit almak; akıntıyı yok saymak.','orta','şekilli',4,'bh-akinti-yol','Akıntılı nehirde doğrusal gidiş–dönüş')
kartla('K-AFBH-03','Nehirde karşıya geçiş','Hız bileşenleri bağımsızdır: karşıya geçiş süresi yalnız kıyıya dik bileşenle bulunur, sürüklenme akıntı × süredir; dik geçişte suya göre hızın akıntıya zıt bileşeni akıntıyı dengeler.','Yere göre hız büyüklüğüyle genişliği bölmek; akıntının süreyi değiştirdiğini sanmak.','orta','şekilli',4,'bh-karsiya-gecis','Nehirde karşıya geçiş: süre ve sürüklenme')
kartla('K-AFBH-04','Vektörel bağıl hız: uçak–rüzgâr, yağmur–araç','Birbirine dik hızlar Pisagor ile bileşke; hedef doğrultusu istenen yönde kalması için bileşenlerden biri sıfırlanır.','Dik hızları cebirsel toplamak.','orta','şekilli',3,'bh-vektor','Dik hızların bileşkesi ve bağıl hız')
kartla('K-AFBH-05','Izgarada iki yüzücünün karşılaşması','Yere göre hızlar (suya göre ± akıntı) bulunur; kapanma hızıyla süre ve konum bölmeden okunur.','Akıntıyı yalnız bir yüzücüye eklemek.','orta','şekilli',4,'bh-izgara','Izgara üzerinde karşılaşma noktası')
kartla('K-AFBH-06','x–t grafiğinden bağıl hız','Eğimler hız verir; bağıl hız eğimlerin vektörel farkıdır.','Eğimi ilk/son konumdan okumak; zıt işaretleri çıkarmak.','orta','grafik',3,'bh-xt','x–t grafiğinden bağıl hız')
kartla('K-AFBH-07','v–t grafiğinden bağıl hız ve uzaklık','Bağıl hız v_L − v_K; bağıl hız–zaman alanı aralarındaki uzaklık değişimini verir, bağıl hız sıfırken uzaklık ekstremum olur.','Hızlar eşitlenince araçlar yan yana sanmak.','zor','grafik',4,'bh-vt','v–t grafiğinden bağıl hız ve uzaklık')
kartla('K-AFBH-08','Referans sistemi ve hız zinciri','v_AC = v_AB + v_BC; gözlemci değişince hız değişir ama cismin kendi yürüme hızı sistemden bağımsızdır.','Bağıl hızı mutlak sanmak; zinciri ters yönde kurmak.','zor','öncüllü',4,'bh-referans','Referans sistemleri ve bağıl hız zinciri')

# ============== SORULAR ==============
# ---- 01 kolay · zıt yönlü araçlar (F1) ----
vK,vL=20,15; rel=vK+vL; assert rel==35 and vK-vL==5 and Fr(vK+vL,2)==Fr(35,2)
sc=.1
SK=tk(f1([road(-.3,8.3),car(1.2,0,'K'),car(6.8,0,'L'),V((1.7,1.0),(1.7+vK*sc,1.0),f'{vK} m/s'),V((6.3,1.0),(6.3-vL*sc,1.0),f'{vL} m/s'),
  '\\node at (-.1,-.45) {Batı}; \\node at (8.1,-.45) {Doğu};']))
q('0001',[A('Yönü seç','Doğuyu pozitif al; K doğuya, L batıya gider.','v_K = +20 m/s · v_L = −15 m/s'),
  A('Bağıl hızı yaz','L’nin K’ye göre hızı, L’nin hızından K’nin hızı çıkarılarak bulunur.','v_LK = v_L − v_K = −15 − 20 = −35 m/s'),
  A('Büyüklüğü al','Eksi işaret yalnızca yönü (batı) gösterir.','|v_LK| = 35 m/s')],
 tipId='bh-dogrusal',tip='Aynı doğrultuda bağıl hız ve yetişme',z='kolay',alt='Bağıl Hız',kaz='Aynı doğrultuda zıt yönlü iki aracın birbirine göre hız büyüklüğünü bulur.',
 kart='K-AFBH-01 (zıt yönlü araçlar) · yere göre hızlar şekilde',kalip='şekilli',
 metin='Doğu–batı doğrultusunda uzanan düz bir yolda K ve L araçları birbirine doğru sabit hızlarla gitmektedir. Araçların yere göre hızları şekilde gösterilmiştir.\nBuna göre, L aracındaki sürücünün K aracına göre hızının büyüklüğü kaç m/s’dir?',
 dogru=rel,yan=[(vK-vL,'Araçlar zıt yönlü olduğu hâlde hızları çıkarmış: 20 − 15 = 5.','dikkat'),(vL,'Yalnız L’nin yere göre hızını almış; gözlemci K’nin hareketini hesaba katmamış.','bilgi'),
  (Fr(35,2),'İki hızın ortalamasını almış: (20 + 15) ÷ 2 = 17,5.','bilgi'),(vK,'K’nin yere göre hızını bağıl hız sanmış; L’nin hareketini hesaba katmamış.','bilgi')],
 istenen='L’nin K’ye göre hız büyüklüğü (m/s).',ip=['Gözlemciyi K’nin içine yerleştir: K duruyormuş gibi görünürse L’nin hızı nasıl değişir?'],
 bilgi=[B('Bağıl hız','A’nın B’ye göre hızı v_AB = v_A − v_B (vektörel). Aynı doğrultuda zıt yönlerde büyüklükler toplanır. Örnek: doğuya 10 m/s ve batıya 4 m/s giden iki cismin bağıl hız büyüklüğü 14 m/s’dir')],
 puf='Zıt yönlü hareketlerde bağıl hız büyüklüğü hızların toplamıdır, aynı yönlüde farkıdır.',sekil=SK)

# ---- 02 kolay · akıntı yönünde gidiş (F3) ----
uA,vS,dAB=3,5,240; t2=Fr(dAB,uA+vS); assert t2==30 and Fr(dAB,vS)==48 and Fr(dAB,(uA+vS)//2)==60 and Fr(dAB,uA)==80 and Fr(dAB,vS-uA)==120
h=3.0; s=.25
SK=tk(f1([river_h(-.3,7.3,h),'\\fill (.8,.8) circle (2pt) (6.2,.8) circle (2pt);\\node[below=1pt] at (.8,.8) {A};\\node[below=1pt] at (6.2,.8) {B};',
  V((.8,1.3),(.8+vS*s,1.3),f'{vS} m/s (suya göre)'),V((3.4,2.3),(3.4+uA*s,2.3),f'akıntı {uA} m/s',col=AK),dim((.8,-.35),(6.2,-.35),f'{dAB} m','below')]))
q('0002',[A('Yere göre hızı bul','Motor akıntıyla aynı yönde gittiğinden hızlar toplanır.','v = 5 + 3 = 8 m/s'),A('Yolu belirle','A’dan B’ye uzaklık şekilde verilmiştir.','x = 240 m'),A('Süreyi hesapla','Yol sabit hızla alınır, t = yol ÷ hız.','t = 240 ÷ 8 = 30 s')],
 tipId='bh-akinti-yol',tip='Akıntılı nehirde doğrusal gidiş–dönüş',z='kolay',alt='Nehir Problemleri',kaz='Akıntı yönünde giden motorun yere göre hızını ve yolculuk süresini bulur.',
 kart='K-AFBH-02 (akıntı yönünde gidiş) · tek yönlü yolculuk',kalip='şekilli',
 metin='Kıyıları paralel, düz bir nehirde akıntı hızı sabittir. A noktasındaki bir motor, suya göre sabit hızla, akıntı yönünde bulunan B noktasına gitmektedir. Hızlar ve A–B uzaklığı şekilde verilmiştir.\nBuna göre, motor A’dan B’ye kaç saniyede ulaşır?',
 dogru=30,yan=[(48,'Akıntıyı yok saymış: 240 ÷ 5 = 48 s.','dikkat'),(60,'Hızların ortalamasını almış: (5 + 3) ÷ 2 = 4 m/s, 240 ÷ 4 = 60 s.','bilgi'),(80,'Yalnız akıntı hızını kullanmış: 240 ÷ 3 = 80 s.','dikkat'),(120,'Akıntıyı ters yönlü sanıp hızları çıkarmış: 240 ÷ (5 − 3) = 120 s.','dikkat')],
 istenen='Motorun A’dan B’ye gidiş süresi (s).',ip=['Motor akıntıyla birlikte mi, akıntıya karşı mı gidiyor? Yere göre hızını buna göre belirle.'],
 bilgi=[B('Akıntıda yere göre hız','v_yer = v_suya göre + v_akıntı (vektörel). Akıntı yönünde hızlar toplanır, akıntıya karşı çıkarılır. Örnek: suya göre 7 m/s ve akıntı 2 m/s ise akıntıya karşı yere göre hız 5 m/s’dir')],
 puf='Akıntı yönünde yere göre hız suya göre hıza akıntı eklenerek bulunur.',sekil=SK)

# ---- 03 kolay · referans sistemi öncüllü ----
onc('0003','A','Sabit hızla düz raylarda ilerleyen bir trenin koridorunda bir yolcu, trenin hareket yönünde sabit hızla yürümektedir. Yolcuyu hem trende oturan arkadaşı hem de istasyonda duran bir görevli izlemektedir.',
 [('Yolcunun yere göre hızının büyüklüğü, trene göre hızının büyüklüğünden büyüktür.',True,'Yolcu ile tren aynı yönde olduğundan yere göre hız = trenin hızı + yolcunun trene göre hızıdır; büyüktür.','I numaralı yargıda yere göre hızı trene göre hızla karıştırmış.'),
  ('Yolcu yürüme hızını değiştirmezse, trenin yere göre hızı artınca yolcunun trene göre hızı da artar.',False,'Yolcunun trene göre hızı yürüyüşüne bağlıdır; trenin hızından bağımsızdır.','II numaralı yargıda trene göre hızı, trenin yere göre hızına bağlı sanmış.'),
  ('Yolcunun oturan arkadaşına göre hızının büyüklüğü, görevliye göre hızının büyüklüğüne eşittir.',False,'Arkadaşı trende durmaktadır; yolcunun ona göre hızı yürüme hızıdır. Görevliye göre hız ise trenin hızı kadar büyüktür.','III numaralı yargıda hızın gözlemciden bağımsız olduğunu düşünmüş.')],
 ['Her yargıda hangi gözlemciye göre hızdan söz edildiğine dikkat et.'],
 [B('Referans sistemi','Hız, gözlemciye göre tanımlanır. Aynı cismin hızı farklı gözlemciler için farklı olabilir. Örnek: yürüyen merdivende yürüyen kişi, merdivene göre yavaş, yere göre hızlı görünür')],
 'Önce “kime göre” sorusunu yanıtla; hızlar gözlemciye göre değişir.','Doğru olan yargılar.','bh-referans','Referans sistemleri ve bağıl hız zinciri','kolay','Referans Sistemi','Gözlemciye göre hızın değiştiğini ve bağıl hızın sistemden bağımsız bileşenlerini ayırt eder.','K-AFBH-08 (tren ve yolcu) · nitel öncüllü','öncüllü')

# ---- 04 orta · dik geçişte sürüklenme (F2) ----
W4,u4,v4=160,3,4; t4=Fr(W4,v4); dr4=u4*t4; assert t4==40 and dr4==120 and W4*Fr(u4,5)==96 and sqrt(u4**2+v4**2)*t4==200 and W4+dr4==280
sc=.4; bw=W4/40
SK=tk(f1(['\\fill[blue!8] (-.3,0) rectangle (5.6,%.2f);\\draw[thick] (-.3,0) -- (5.6,0) (-.3,%.2f) -- (5.6,%.2f);'%(bw,bw,bw),
  '\\fill (1,0) circle (2pt);\\node[below=1pt] at (1,0) {O};\\fill (1,%.2f) circle (2pt);\\node[above=1pt] at (1,%.2f) {P};'%(bw,bw),
  '\\draw[dashed,thin] (1,0) -- (1,%.2f);'%bw,dim((.45,0),(.45,bw),f'{W4} m','left'),
  V((1,0),(1,v4*sc),f'{v4} m/s (suya göre)','right'),V((2.6,2.9),(2.6+u4*sc,2.9),f'akıntı {u4} m/s',col=AK)]))
q('0004',[A('Süreyi bul','Karşıya geçiş süresi yalnız kıyıya dik bileşenle belirlenir; akıntı bu bileşeni değiştirmez.','t = 160 ÷ 4 = 40 s'),
  A('Sürüklenmeyi hesapla','Kıyıya paralel yönde kayık yalnızca akıntıyla ilerler.','x = 3 × 40 = 120 m'),A('Sonucu yaz','Varış noktası P’den akıntı yönünde 120 m ötededir.','Uzaklık = 120 m')],
 tipId='bh-karsiya-gecis',tip='Nehirde karşıya geçiş: süre ve sürüklenme',z='orta',alt='Nehir Problemleri',kaz='Kıyıya dik yönde yüzen kayığın karşıya geçiş süresini ve sürüklenmesini ayrı bileşenlerle bulur.',
 kart='K-AFBH-03 (dik geçiş) · sürüklenme',kalip='şekilli',
 metin='Kıyıları paralel olan düz bir nehirde akıntı hızı kıyıya paralel ve sabittir. Bir kayıkçı, O noktasından kıyıya dik doğrultuda ve suya göre sabit büyüklükteki hızla kürek çekerek karşı kıyıya geçiyor. Genişlik ve hızlar şekilde verilmiştir; P noktası O’nun tam karşısındadır.\nBuna göre, kayık karşı kıyıya P noktasından kaç m uzakta ulaşır?',
 dogru=dr4,yan=[(96,'Hız büyüklüklerini oranlayıp genişliğe uygulamış: 160 × 3/5 = 96 m.','bilgi'),(160,'Sürüklenmeyi nehrin genişliğine eşit almış.','bilgi'),(200,'Yere göre hızı (5 m/s) süreyle çarpmış; bu kayığın izlediği yolun uzunluğudur.','dikkat'),(280,'Genişlik ile sürüklenmeyi toplamış: 160 + 120.','dikkat')],
 istenen='Varış noktasının P’ye uzaklığı (m).',ip=['Kıyıya dik ve kıyıya paralel hareketleri ayrı ayrı düşün; karşıya geçiş süresini hangi bileşen belirler?'],
 bilgi=[B('Hareketlerin bağımsızlığı','Birbirine dik iki hız bileşeni ayrı ayrı incelenir; süre ortaktır. Örnek: 50 m genişlikte 5 m/s dik hızla geçiş 10 s sürer, bu sürede 2 m/s’lik akıntı 20 m sürükler')],
 puf='Karşıya geçiş süresi yalnızca kıyıya dik bileşenle bulunur; sürüklenme akıntı × süredir.',sekil=SK)

# ---- 05 orta · gidiş–dönüş (F3) ----
u5,v5,d5=2,6,240; tg=Fr(d5,v5+u5); td=Fr(d5,v5-u5); tt=tg+td; assert (tg,td,tt)==(30,60,90) and Fr(2*d5,v5)==80 and 2*td==120
SK=tk(f1([river_h(-.3,7.3,h),'\\fill (.8,.8) circle (2pt) (6.2,.8) circle (2pt);\\node[below=1pt] at (.8,.8) {A};\\node[below=1pt] at (6.2,.8) {B};',
  V((.8,1.3),(.8+v5*.25,1.3),f'{v5} m/s (suya göre)'),V((3.9,2.3),(3.9+u5*.25,2.3),f'akıntı {u5} m/s',col=AK),dim((.8,-.35),(6.2,-.35),f'{d5} m','below')]))
q('0005',[A('Gidiş süresi','Akıntı yönünde yere göre hız suya göre hız ile akıntının toplamıdır.','v₁ = 6 + 2 = 8 m/s · t₁ = 240 ÷ 8 = 30 s'),
  A('Dönüş süresi','Dönüşte akıntıya karşı gidildiğinden hızlar çıkarılır.','v₂ = 6 − 2 = 4 m/s · t₂ = 240 ÷ 4 = 60 s'),A('Toplamı bul','Gidiş ve dönüş süreleri toplanır.','t = 30 + 60 = 90 s')],
 tipId='bh-akinti-yol',tip='Akıntılı nehirde doğrusal gidiş–dönüş',z='orta',alt='Nehir Problemleri',kaz='Akıntı yönünde ve akıntıya karşı hareketin sürelerini ayrı hesaplayarak toplam süreyi bulur.',
 kart='K-AFBH-02 (gidiş–dönüş) · dönüşte akıntıya karşı',kalip='şekilli',
 metin='Akıntı hızının kıyıya paralel ve sabit olduğu düz bir nehirde bir motor, A noktasından hareket ederek akıntı yönündeki B noktasına gidiyor ve oradan geri dönerek A noktasına ulaşıyor. Motor gidişte de dönüşte de suya göre aynı büyüklükteki hızla ilerlemektedir; B’deki dönüş süresi önemsizdir. Hızlar ve A–B uzaklığı şekilde verilmiştir.\nBuna göre, motorun A–B–A yolculuğu toplam kaç saniye sürer?',
 dogru=90,yan=[(30,'Yalnız gidiş süresini hesaplamış (240 ÷ 8 = 30 s), dönüşü unutmuş.','dikkat'),(60,'Yalnız dönüş süresini bulmuş (240 ÷ 4 = 60 s).','dikkat'),(80,'Akıntının gidiş ve dönüşte birbirini götürdüğünü sanmış: 2 × 240 ÷ 6 = 80 s.','bilgi'),(120,'İki yolda da akıntıya karşı gidildiğini varsaymış: 2 × 60 = 120 s.','dikkat')],
 istenen='A–B–A yolculuğunun toplam süresi (s).',ip=['Gidiş ve dönüşte yere göre hızlar aynı mı? Her yol için süreyi ayrı bul.'],
 bilgi=[B('Akıntı ve süre','Akıntı gidiş süresini kısaltırken dönüş süresini daha çok uzatır; gidiş–dönüş toplamı akıntısız sudakinden büyüktür. Örnek: suya göre 5 m/s, akıntı 1 m/s, 120 m için akıntısız toplam 48 s, akıntılı 20 + 30 = 50 s')],
 puf='Akıntılı suda gidiş–dönüş toplam süresi, akıntısız sudakinden her zaman uzundur.',sekil=SK)

# ---- 06 orta · ızgara karşılaşma (F6) ----
n6=10; vA,vB=3,2; kA=vA+1; kB=-(vB-1); assert (kA,kB)==(4,-1)
t6=Fr(n6,kA-kB); x6=kA*t6; assert t6==2 and x6==8 and Fr(n6*vA,vA+vB)==6 and Fr(n6*(vA-1),(vA-1)+(vB+1))==4 and n6-x6==2
lbl={2:'M',4:'N',5:'P',6:'R',8:'S'}; u=.65
g=['\\fill[gray!12] (0,0) rectangle (%.2f,%.2f);'%(n6*u,4*u),'\\draw[gray!70,dashed] '+' '.join('(%.2f,0)--(%.2f,%.2f)'%(i*u,i*u,4*u) for i in range(n6+1))+';','\\draw[thick] (0,0)--(%.2f,0) (0,%.2f)--(%.2f,%.2f);'%(n6*u,4*u,n6*u,4*u)]
g.append('\\fill (0,%.2f) circle (2.4pt) (%.2f,%.2f) circle (2.4pt);\\node[left=2pt] at (0,%.2f) {A};\\node[right=2pt] at (%.2f,%.2f) {B};'%(2*u,n6*u,2*u,2*u,n6*u,2*u))
for k_,l_ in lbl.items(): g.append('\\fill (%.2f,%.2f) circle (2.2pt);\\node[below=2pt] at (%.2f,%.2f) {%s};'%(k_*u,2*u,k_*u,2*u,l_))
g.append(V((0,3.1*u),(vA*u,3.1*u),'$3v$','above'));g.append(V((n6*u,3.1*u),((n6-vB)*u,3.1*u),'$2v$','above'));g.append(V((3.5*u,.9*u),(4.5*u,.9*u),'akıntı $v$','below',AK))
SK=tk(f1(g))
q('0006',[A('Yere göre hızları bul','Akıntı sağa doğru; A’nın suya göre hızı sağa, B’ninki sola.','v_A = 3v + v = 4v (sağa) · v_B = −2v + v = −v (sola)'),
  A('Konumları yaz','Bölme sayısı birim, v = 1 bölme/s alınır; A’dan başlayıp sağa gidilir.','x_A = 4t · x_B = 10 − t'),A('Karşılaşma anı','Konumlar eşitlenir.','4t = 10 − t → t = 2 s'),A('Noktayı oku','A’dan 8 bölme ötedeki nokta işaretlidir.','x = 4 × 2 = 8 bölme → S')],
 tipId='bh-izgara',tip='Izgara üzerinde karşılaşma noktası',z='orta',alt='Nehir Problemleri',kaz='Akıntıyı hesaba katarak iki yüzücünün yere göre hızlarını ve karşılaşma noktasını bulur.',
 kart='K-AFBH-05 (ızgara) · 3v ve 2v, akıntı v',kalip='şekilli',
 metin='Üstten görünüşü şekildeki gibi olan, kıyıları paralel bir nehirde akıntı hızının büyüklüğü v’dir ve akıntı A’dan B’ye doğrudur. A ve B noktalarındaki iki yüzücü aynı anda, kıyıya paralel olan aynı doğru boyunca, birbirine doğru yüzmeye başlıyor. Yüzücülerin suya göre hız vektörleri şekilde gösterilmiştir. Bölmeler eşit aralıklıdır.\nBuna göre, yüzücüler hangi noktada karşılaşır?',
 dogru='S',yan=[('R','Akıntıyı hiç hesaba katmamış: 10 × 3/(3 + 2) = 6 bölme → R.','dikkat'),('N','Akıntıyı ters yönlü almış: hızlar 2v ve 3v çıkıyor, 10 × 2/5 = 4 bölme → N.','bilgi'),('M','Konumu B’den ölçmüş: 10 − 8 = 2 bölme → M.','dikkat'),('P','İki yüzücü de eşit hızlı sanıp ortada (5. bölme) karşılaşacaklarını düşünmüş.','bilgi')],
 sira=['M','N','P','R','S'],istenen='Karşılaşma noktası.',ip=['Akıntı iki yüzücünün de hızını aynı yönde etkiler; yere göre hızları ayrı ayrı yaz.'],
 bilgi=[B('Yere göre hızlar','Akıntıya sahip ortamda her hareketlinin yere göre hızı suya göre hızıyla akıntının vektörel toplamıdır. Örnek: akıntı sağa 1 m/s iken suya göre sola 3 m/s giden yüzücünün yere göre hızı 2 m/s sola olur')],
 puf='Önce yere göre hızları yaz, sonra konum denklemlerini eşitle.',sekil=SK)

# ---- 07 orta · drone + rüzgâr (F7) ----
vd,vw,T7=12,5,10; vg=int(sqrt(vd**2+vw**2)); assert vg==13 and vg*T7==130 and (vd+vw)*T7==170 and (vd-vw)*T7==70 and vd*T7==120 and vw*T7==50
sc=.2
SK=tk(f1(['\\fill (0,0) circle (2.4pt);\\node[above left] at (0,0) {drone};',V((0,0),(vd*sc,0),f'{vd} m/s (havaya göre)','below'),V((0,0),(0,vw*sc),f'{vw} m/s (rüzgâr)','right',AK),
  '\\draw[->,thick] (4.6,-.2) -- (4.6,.7) node[above] {Kuzey}; \\draw[->,thick] (4.6,-.2) -- (5.5,-.2) node[right] {Doğu};']))
q('0007',[A('Hızları belirle','Drone havaya göre doğuya, hava ise yere göre kuzeye hareket eder; iki hız birbirine diktir.','v₁ = 12 m/s (doğu) · v₂ = 5 m/s (kuzey)'),A('Yere göre hızı bul','Dik bileşenlerin bileşkesi Pisagor ile bulunur.','v = √(12² + 5²) = 13 m/s'),A('Yer değiştirmeyi hesapla','Hız sabit olduğundan yer değiştirme hız × süredir.','x = 13 × 10 = 130 m')],
 tipId='bh-vektor',tip='Dik hızların bileşkesi ve bağıl hız',z='orta',alt='Bağıl Hız',kaz='Birbirine dik hız vektörlerini bileşke hız olarak toplar ve yer değiştirmeyi bulur.',
 kart='K-AFBH-04 (drone + rüzgâr) · dik vektörler',kalip='şekilli',
 metin='Bir drone, havaya göre doğuya doğru sabit hızla uçmaktadır. Aynı anda rüzgâr, yere göre kuzeye doğru sabit hızla esmektedir. Drone’un havaya göre hızı ve rüzgârın hızı şekilde verilmiştir.\nBuna göre, drone 10 s boyunca bu hareketini sürdürürse yere göre yer değiştirmesinin büyüklüğü kaç m olur?',
 dogru=130,yan=[(50,'Yalnız rüzgârın etkisiyle olan yer değiştirmeyi bulmuş: 5 × 10 = 50 m.','dikkat'),(70,'Dik hızlara zıt yönlüymüş gibi davranıp çıkarmış: (12 − 5) × 10 = 70 m.','bilgi'),(120,'Rüzgârı hesaba katmamış: 12 × 10 = 120 m.','dikkat'),(170,'Dik hızları cebirsel toplamış: (12 + 5) × 10 = 170 m.','bilgi')],
 istenen='Yere göre yer değiştirmenin büyüklüğü (m).',ip=['İki hızın doğrultuları arasındaki açıya bakarak bileşke hızı nasıl bulacağını düşün.'],
 bilgi=[B('Dik vektörlerin bileşkesi','Birbirine dik a ve b vektörlerinin bileşkesinin büyüklüğü √(a² + b²)’dir. Örnek: 3 m/s ve 4 m/s’lik dik hızların bileşkesi 5 m/s’dir')],
 puf='Dik hızları toplarken Pisagor, aynı doğrultuda cebirsel toplama kullan.',sekil=SK)

# ---- 08 orta · yağmur–araç öncüllü (F9) ----
vc,vr=12,9; vrel=int(sqrt(vc**2+vr**2)); assert vrel==15
SK=tk(f1([road(-.3,5.2),car(.9,0,'Araç',1.6),V((.9,1.25),(.9+vc*.1,1.25),f'{vc} m/s','above'),
  ''.join(V((x_,2.9),(x_,2.0),'','above',AK) for x_ in (3.4,4.0,4.6))+'\\node[right] at (4.7,2.45) {9 m/s (damla)};']))
onc('0008','C','Rüzgârsız bir havada yağmur damlaları yere göre düşey doğrultuda ve sabit hızla düşmektedir. Düz bir yolda sabit hızla giden araçtaki bir yolcu camdan damlaları izlemektedir. Aracın ve damlaların yere göre hızları şekilde verilmiştir.',
 [('Damlaların araca göre hızının büyüklüğü 15 m/s’dir.',True,'Araca göre hız, yere göre düşey 9 m/s ile aracın 12 m/s’lik hızının vektörel farkıdır; dik bileşenlerden √(9² + 12²) = 15 m/s.','I numaralı yargıda dik hızları cebirsel işlemle birleştirip büyüklüğü farklı bulmuş.'),
  ('Araç hızını artırırsa damlaların araca göre hızının büyüklüğü artar.',True,'Araca göre hızın yatay bileşeni büyür; düşey bileşen aynı kalır, bileşke büyür.','II numaralı yargıda damlaların hızının araç hızından bağımsız olduğunu düşünmüş.'),
  ('Yolcuya göre damlalar düşey doğrultuda iner.',False,'Araca göre hızın yatay bileşeni aracın hızının tersi yönündedir; damlalar geriye doğru eğik görünür.','III numaralı yargıda yolcunun da damlaları yere göre gibi düşey göreceğini sanmış.')],
 ['Her yargıda damlaların hangi gözlemciye göre hareket ettiğini belirle ve araca göre hız vektörünü çiz.'],
 [B('Vektörel bağıl hız','A’nın B’ye göre hızı v_AB = v_A − v_B’dir. Bileşenleri dik olan hızlarda büyüklük Pisagor ile bulunur. Örnek: yere göre düşey 6 m/s düşen cisim, yatay 8 m/s giden araca göre 10 m/s hızla görünür')],
 'Gözlemci hareketliyse onun hızını ters yönde ekleyerek bağıl hızı bul.','Doğru olan yargılar.','bh-vektor','Dik hızların bileşkesi ve bağıl hız','orta','Bağıl Hız','Hareketli bir gözlemciye göre düşen damlaların hız vektörünü bulur ve yorumlar.','K-AFBH-04 (yağmur–araç) · öncüllü','şekilli',sekil=SK)

# ---- 09 orta · x–t grafiği (F4) ----
def axis_xt(lines,xmax,ymax,xs,ys,ylab,xlab='$t$ (s)',extra='',w=7.0,h_=5.6):
    s_=f'\\begin{{axis}}[width={w}cm,height={h_}cm,axis lines=left,xlabel={{{xlab}}},ylabel={{{ylab}}},xmin=0,xmax={xmax},ymin=0,ymax={ymax},xtick={{{xs}}},ytick={{{ys}}},grid=major,grid style={{gray!30}},tick label style={{font=\\small}},label style={{font=\\small}}]\n'
    for st,pts,lab,at in lines:
        s_+='\\addplot[%s,very thick] coordinates {%s};\n'%(st,' '.join('(%s,%s)'%p for p in pts))
        s_+='\\node[font=\\small\\bfseries,fill=white,inner sep=1pt] at (axis cs:%s,%s) {%s};\n'%(at[0],at[1],lab)
    return tk(s_+extra+'\\end{axis}')
xK,xL=Fr(80,8),Fr(60-20,8); assert xK==10 and xL==5 and xK+xL==15 and Fr(60,8)==Fr(15,2) and xK-xL==5
SK=axis_xt([('vurgu',[(0,0),(8,80)],'K',(7.2,66)),('blue!65!black,dashed',[(0,60),(8,20)],'L',(7.3,31))],8,100,'0,1,...,8','0,20,...,100','$x$ (m)')
q('0009',[A('K’nin hızı','Doğrunun eğimi hızı verir.','v_K = 80 ÷ 8 = +10 m/s'),A('L’nin hızı','L’nin konumu azalıyor; eğim negatiftir.','v_L = (20 − 60) ÷ 8 = −5 m/s'),A('Bağıl hız','Hızlar zıt işaretli olduğundan büyüklükler toplanır.','|v_K − v_L| = |10 − (−5)| = 15 m/s')],
 tipId='bh-xt',tip='x–t grafiğinden bağıl hız',z='orta',alt='Bağıl Hız',kaz='Konum–zaman grafiğinden hızları okuyup iki cismin birbirine göre hızını bulur.',
 kart='K-AFBH-06 (x–t, iki doğru) · zıt işaretli eğimler',kalip='grafik',
 metin='Doğrusal bir yolda sabit hızlarla hareket eden K ve L araçlarının, aynı başlangıç noktasına göre konum–zaman grafikleri şekilde verilmiştir.\nBuna göre, K aracındaki bir yolcunun L aracına göre hızının büyüklüğü kaç m/s’dir?',
 dogru=15,yan=[(5,'Hızların zıt yönlü olduğunu görmeden çıkarmış: 10 − 5 = 5.','dikkat'),(Fr(15,2),'L’nin eğimi yerine ilk konumunu süreye bölmüş: 60 ÷ 8 = 7,5.','bilgi'),(10,'Yalnız K’nin hızını bulmuş: 80 ÷ 8 = 10.','dikkat'),(20,'Son konumlardan, hız değil konum farkı (80 − 60) okumuş.','bilgi')],
 istenen='K’nin L’ye göre hızının büyüklüğü (m/s).',ip=['Grafikteki her doğrunun eğimini işaretiyle yaz; bağıl hız eğimlerin farkıdır.'],
 bilgi=[B('x–t grafiğinde hız','Doğrunun eğimi hızı verir: v = Δx ÷ Δt; azalan doğru negatif hızdır. Örnek: 2 s’de 6 m artan konum 3 m/s’lik hızdır')],
 puf='x–t grafiğinde bağıl hız, iki doğrunun eğimlerinin vektörel farkıdır.',sekil=SK)

# ---- 10 orta · v–t bağıl hız (F5) ----
vKt=20; aL=2; vL6=aL*6; rel6=vKt-vL6; assert rel6==8 and vL6==12 and vKt+vL6==32
SK=axis_xt([('vurgu',[(0,20),(10,20)],'K',(8.8,21.5)),('blue!65!black,dashed',[(0,0),(10,20)],'L',(8.8,15))],10,24,'0,2,...,10','0,4,...,24','$v$ (m/s)')
q('0010',[A('L’nin hızı','L’nin hızı 0’dan 10 s’de 20 m/s’ye lineer artar; ivme 2 m/s²’dir.','v_L(6) = 2 × 6 = 12 m/s'),A('K’nin hızı','K sabit hızlıdır.','v_K = 20 m/s'),A('Bağıl hız','Aynı yönde hareket ettiklerinden hızlar çıkarılır.','|v_L − v_K| = |12 − 20| = 8 m/s')],
 tipId='bh-vt',tip='v–t grafiğinden bağıl hız ve uzaklık',z='orta',alt='Bağıl Hız',kaz='Hız–zaman grafiğinden belirli anda iki aracın bağıl hızını bulur.',
 kart='K-AFBH-07 (v–t, bağıl hız) · belirli anda okuma',kalip='grafik',
 metin='Doğrusal bir yolda aynı yönde hareket eden K ve L araçlarının yere göre hız–zaman grafikleri şekildeki gibidir.\nBuna göre, 6. saniyede K aracındaki sürücünün L aracına göre hızının büyüklüğü kaç m/s’dir?',
 dogru=8,yan=[(2,'L’nin hızı yerine grafiğin eğimini (ivmeyi) hız sanmış: 2 m/s.','bilgi'),(12,'Yalnız L’nin 6. s’deki yere göre hızını okumuş.','dikkat'),(20,'Yalnız K’nin yere göre hızını bağıl hız sanmış.','bilgi'),(32,'Aynı yönlü hareketi zıt yönlü sanıp hızları toplamış: 20 + 12.','dikkat')],
 istenen='K’nin L’ye göre hızının büyüklüğü (m/s).',ip=['İstenen anda iki aracın yere göre hızlarını grafikten oku; hareketleri aynı yönlü.'],
 bilgi=[B('v–t grafiğinde bağıl hız','Aynı anda iki grafikten okunan hızların farkı bağıl hızı verir. Örnek: bir anda 15 m/s ve 9 m/s hızla aynı yönde giden iki aracın bağıl hızı 6 m/s’dir')],
 puf='Bağıl hız için iki grafiği aynı t anında oku ve aynı yönlü hareketlerde çıkar.',sekil=SK)

# ---- 11 orta · yetişme (F1) ----
gap,vk,vl=120,30,20; ty=Fr(gap,vk-vl); xk=vk*ty; assert ty==12 and xk==360 and vl*ty==240 and Fr(gap,vk+vl)*vk==72 and Fr(gap,vk)*vk==gap and Fr(gap,vl)*vk==180
sc=.07
SK=tk(f1([road(-.3,7.6),car(.6,0,'K'),car(4.6,0,'L'),V((1.1,1.0),(1.1+vk*sc,1.0),f'{vk} m/s'),V((5.1,1.0),(5.1+vl*sc,1.0),f'{vl} m/s'),dim((1.1,-.35),(4.1,-.35),f'{gap} m','below'),
  '\\node at (-.1,-.9) {Batı}; \\node at (7.4,-.9) {Doğu};']))
q('0011',[A('Kapanma hızı','K’ye göre L’nin hızı aynı yönde olduğundan hızlar çıkarılır.','v_bağıl = 30 − 20 = 10 m/s'),A('Yetişme süresi','Aradaki mesafe kapanma hızıyla kapanır.','t = 120 ÷ 10 = 12 s'),A('K’nin yolu','K’nin yere göre aldığı yol hesaplanır.','x = 30 × 12 = 360 m')],
 tipId='bh-dogrusal',tip='Aynı doğrultuda bağıl hız ve yetişme',z='orta',alt='Bağıl Hız',kaz='Aynı yönde giden iki aracın yetişme süresini bağıl hızla bulup yere göre yolu hesaplar.',
 kart='K-AFBH-01 (yetişme) · K’nin yolu isteniyor',kalip='şekilli',
 metin='Doğu yönünde uzanan düz bir yolda K aracı, önünde aynı yönde giden L aracına doğru sabit hızla gitmektedir. Araçların yere göre hızları ve aralarındaki uzaklık şekilde verilmiştir. K aracı L aracına yetişinceye kadar iki araç da hızlarını değiştirmiyor.\nBuna göre, K aracı L aracına yetişinceye kadar yere göre kaç m yol alır?',
 dogru=360,yan=[(72,'Yetişmeyi zıt yönlü sanıp hızları toplamış: t = 120 ÷ 50 = 2,4 s, yol = 30 × 2,4 = 72 m.','bilgi'),(120,'L’yi duruyor sanmış: t = 120 ÷ 30 = 4 s, yol = 30 × 4 = 120 m.','bilgi'),(180,'K’yi duruyor sanmış: t = 120 ÷ 20 = 6 s, yol = 30 × 6 = 180 m.','bilgi'),(240,'L’nin yetişme süresinde aldığı yolu (20 × 12) bulmuş.','dikkat')],
 istenen='K’nin yetişene kadar yere göre aldığı yol (m).',ip=['K’nin L’ye göre hızını bul; aradaki mesafe bu hızla kapanır.'],
 bilgi=[B('Yetişme problemi','Aynı yönde giden iki araçta kapanma hızı hız farkıdır; süre = mesafe ÷ hız farkı. Örnek: 40 m geride, hızı 5 m/s fazla olan araç 8 s’de yetişir')],
 puf='Yetişme süresi için mesafeyi hız farkına böl; yolu yere göre hızla bul.',sekil=SK)

# ---- 12 orta · tahta parçası öncüllü ----
onc('0012','A','Akıntı hızı doğu yönünde ve 2 m/s olan düz bir nehirde bir motor, suya göre batı yönünde 5 m/s’lik hızla gitmektedir. Aynı anda nehirde akıntıyla birlikte sürüklenen bir tahta parçası vardır.',
 [('Motorun yere göre hızı batı yönünde 7 m/s’dir.',False,'Akıntı motorun hızına zıt yöndedir; yere göre hız 5 − 2 = 3 m/s batıya doğrudur.','I numaralı yargıda akıntıyı hıza ekleyip toplamış.'),
  ('Tahta parçasının motora göre hızı doğu yönünde 5 m/s’dir.',True,'Tahta suyla birlikte olduğundan suya göre durur; motora göre hızı, motorun suya göre hızının tersidir: doğuya 5 m/s.','II numaralı yargıda tahtanın yere göre hızını (2 m/s) motora göre hız sanmış.'),
  ('Motorun tahta parçasına göre hızının büyüklüğü 3 m/s’dir.',False,'Tahta su çerçevesindedir; motorun ona göre hızı suya göre hızıdır: 5 m/s.','III numaralı yargıda motorun yere göre hızını tahtaya göre hız sanmış.')],
 ['Tahta parçasının suya göre hızı kaçtır?'],
 [B('Su çerçevesi','Akıntıyla birlikte sürüklenen cisim suya göre durgundur; sudaki hareketliler bu cisme göre suya göre hızlarıyla hareket eder. Örnek: akıntıda yüzen şamandıraya göre, suya göre 3 m/s giden kayığın hızı 3 m/s’dir')],
 'Akıntıyla sürüklenen bir cisme göre hızlar, akıntı yokmuş gibi hesaplanır.','Doğru olan yargılar.','bh-akinti-yol','Akıntılı nehirde doğrusal gidiş–dönüş','orta','Nehir Problemleri','Su çerçevesinde bağıl hızı yorumlar.','K-AFBH-02 (su çerçevesi) · öncüllü','öncüllü')

# ---- 13 orta · dik geçiş (vektör üçgeni, F2) ----
u13,v13,W13=3,5,120; vy=int(sqrt(v13**2-u13**2)); t13=Fr(W13,vy); assert vy==4 and t13==30 and Fr(W13,v13)==24 and Fr(W13,v13+u13)==15 and Fr(W13,v13-u13)==60 and Fr(W13,u13)==40
bw=W13/30; sc=.4
SK=tk(f1(['\\fill[blue!8] (-1.8,0) rectangle (3.4,%.2f);\\draw[thick] (-1.8,0) -- (3.4,0) (-1.8,%.2f) -- (3.4,%.2f);'%(bw,bw,bw),'\\fill (1.5,0) circle (2pt);\\node[below=1pt] at (1.5,0) {O};',
  '\\draw[dashed,thin] (1.5,0) -- (1.5,%.2f);'%bw,dim((1.9,0),(1.9,bw),f'{W13} m','right'),
  V((1.5,0),(1.5-u13*sc,vy*sc),f'{v13} m/s (suya göre)','left'),V((2.5,3.0),(2.5+u13*sc,3.0),f'akıntı {u13} m/s','above',AK)]))
q('0013',[A('Dik geçiş koşulu','Yere göre hızın kıyıya paralel bileşeni sıfır olmalıdır; suya göre hızın bileşeni akıntıyı dengeler.','v_paralel = 3 m/s (akıntıya zıt, suya göre bileşen)'),
  A('Dik bileşeni bul','Suya göre hız 5 m/s olduğundan dik bileşen Pisagor ile bulunur.','v_dik = √(5² − 3²) = 4 m/s'),A('Süreyi hesapla','Karşıya geçiş süresi dik bileşenle belirlenir.','t = 120 ÷ 4 = 30 s')],
 tipId='bh-karsiya-gecis',tip='Nehirde karşıya geçiş: süre ve sürüklenme',z='orta',alt='Nehir Problemleri',kaz='Kıyıya dik yönde karşıya geçmek için gereken bileşenleri bulup süreyi hesaplar.',
 kart='K-AFBH-03 (en kısa yol, dik geçiş) · vektör üçgeni',kalip='şekilli',
 metin='Genişliği, akıntı hızı ve kayığın suya göre hız büyüklüğü şekilde verilen düz kıyılı bir nehirde bir kayıkçı, O noktasından yola çıkıp kıyıya dik doğrultuda ilerleyerek tam karşıdaki noktaya ulaşmak istiyor. Bunun için kayığı akıntıya karşı yönde eğik tutuyor; kayığın suya göre hızı sabittir.\nBuna göre, kayık karşı kıyıya kaç saniyede ulaşır?',
 dogru=30,yan=[(15,'Hızları toplayıp (5 + 3 = 8 m/s) 120 ÷ 8 = 15 s bulmuş.','bilgi'),(24,'Suya göre hızın tamamını karşıya geçişe katmış: 120 ÷ 5 = 24 s.','bilgi'),(40,'Akıntı hızıyla bölmüş: 120 ÷ 3 = 40 s.','dikkat'),(60,'Hızları çıkarmış: 120 ÷ (5 − 3) = 60 s.','islem')],
 istenen='Karşı kıyıya ulaşma süresi (s).',ip=['Yere göre hızın kıyıya paralel bileşeninin sıfır olması için suya göre hızın dik bileşenini üçgenden bul.'],
 bilgi=[B('Dik geçiş','Kıyıya dik gitmek için suya göre hızın akıntıya zıt bileşeni akıntı hızına eşit olmalıdır; dik bileşen √(v² − u²) olur. Örnek: v = 13, u = 5 için dik bileşen 12 m/s’dir')],
 puf='Dik geçişte karşıya geçiş süresi, genişliğin √(v² − u²)’ye bölünmesidir.',sekil=SK)

# ---- 14 zor · v–t, en büyük uzaklık (F5) ----
vk14=15; vl0,aL14=5,2; ts=Fr(vk14-vl0,aL14); gap14=lambda t: vk14*t-(vl0*t+aL14*t*t/2); assert ts==5 and gap14(5)==25 and gap14(10)==0 and max(gap14(Fr(i,2)) for i in range(0,21))==25 and vl0*5+25==50 and vk14*5==75 and vk14*10==150
SK=axis_xt([('vurgu',[(0,15),(10,15)],'K',(8.8,17)),('blue!65!black,dashed',[(0,5),(10,25)],'L',(8.8,22))],10,30,'0,2,...,10','0,5,...,30','$v$ (m/s)')
q('0014',[A('Bağıl hızı yaz','L’nin hızı v_L = 5 + 2t, K’nin hızı 15 m/s’dir.','v_LK = 5 + 2t − 15 = 2t − 10'),A('Uzaklığın ekstremumu','Bağıl hız sıfır olduğunda araçlar arası uzaklık en büyük (ya da en küçük) olur.','2t − 10 = 0 → t = 5 s'),
  A('Konumları bul','Başlangıçta aynı noktadalar; 5 s’de alınan yollar.','x_K = 15 × 5 = 75 m · x_L = 5 × 5 + ½ × 2 × 25 = 50 m'),A('Uzaklığı yaz','K, L’nin önündedir.','75 − 50 = 25 m'),A('Kontrol et','10. s’de her iki araç 150 m yol almıştır; yan yana gelir, 5. s’deki 25 m en büyük değerdir.','x_K(10) = x_L(10) = 150 m')],
 tipId='bh-vt',tip='v–t grafiğinden bağıl hız ve uzaklık',z='zor',alt='Bağıl Hız',kaz='Hız–zaman grafiğinden bağıl hızı ve bağıl hız sıfırken araçlar arası en büyük uzaklığı bulur.',
 kart='K-AFBH-07 (v–t, en büyük uzaklık) · iki araç, aynı başlangıç',kalip='grafik',
 metin='Doğrusal bir yolda aynı yönde hareket eden K ve L araçları, t = 0 anında yoldaki aynı noktadan geçmektedir. Araçların yere göre hız–zaman grafikleri şekilde verilmiştir.\nBuna göre, 0–10 s aralığında K ile L araçları arasındaki uzaklığın alabileceği en büyük değer kaç m’dir?',
 dogru=25,yan=[(10,'İlk andaki hız farkını (15 − 5) uzaklık sanmış.','bilgi'),(50,'5. s’de yalnız L’nin aldığı yolu (50 m) bulmuş.','dikkat'),(75,'5. s’de yalnız K’nin aldığı yolu (75 m) bulmuş.','dikkat'),(150,'K’nin 10 s’de aldığı yolu (alan) uzaklık sanmış; araçlar 10. s’de yan yana gelir.','bilgi')],
 istenen='Araçlar arası uzaklığın en büyük değeri (m).',ip=['Araçlar arası uzaklık, bağıl hızın işareti değiştiği anda en büyük ya da en küçük olur; bu anı bul.'],
 bilgi=[B('Bağıl hız ve uzaklık','İki araç arasındaki uzaklık, bağıl hız–zaman grafiğinin altındaki işaretli alanla değişir. Bağıl hızın sıfır olduğu anda uzaklık ekstremum değeri alır. Örnek: bağıl hızı 6 s boyunca 0’dan 12 m/s’ye düzgün artan araçlar arası uzaklık 36 m değişir')],
 puf='Araçlar arası uzaklık, hızlar eşitlendiği anda ekstremum değerdedir; yan yana gelme anı değildir.',sekil=SK)

# ---- 15 orta · uçak–rüzgâr (F7 harita) ----
vp,wd,D15=100,60,480; vn=int(sqrt(vp**2-wd**2)); assert vn==80 and Fr(D15,vn)==6 and Fr(D15,vp)==Fr(24,5) and Fr(D15,vp+wd)==3 and Fr(D15,wd)==8 and Fr(D15,vp-wd)==12
sc=.02
SK=tk(f1(['\\fill (2.6,0) circle (2pt);\\node[below] at (2.6,0) {K};\\fill (2.6,%.2f) circle (2pt);\\node[above] at (2.6,%.2f) {L};'%(D15*.01,D15*.01),'\\draw[dashed,thin] (2.6,0) -- (2.6,%.2f);'%(D15*.01),dim((4.4,0),(4.4,D15*.01),f'{D15} km','right'),
  V((2.6,0),(2.6-wd*sc,vn*sc),f'{vp} km/h (havaya göre)','left'),V((2.6,3.5),(2.6+wd*sc,3.5),f'rüzgâr {wd} km/h','above',AK).replace('inner sep=1pt','inner sep=1pt').replace('node[midway,above]','node[midway,above,fill=white,inner sep=1pt]'),
  '\\draw[->,thick] (7.0,.1) -- (7.0,1.0) node[above] {Kuzey};']))
q('0015',[A('Yönelmeyi belirle','Uçak L’ye (kuzeye) gitmek için burnunu rüzgârın doğuya sürüklemesini dengeleyecek biçimde batıya çevirir.','Doğu bileşeni: v·sinθ = 60 → sinθ = 0,6'),A('Kuzey bileşeni','Yere göre hız, havaya göre hızın kuzey bileşenidir.','v_kuzey = √(100² − 60²) = 80 km/h'),A('Süreyi bul','Yere göre hız kuzeyde 80 km/h’tir.','t = 480 ÷ 80 = 6 saat')],
 tipId='bh-vektor',tip='Dik hızların bileşkesi ve bağıl hız',z='orta',alt='Bağıl Hız',kaz='Rüzgârın etkisini dengelemek için gereken bileşenleri bulup yere göre hızla süreyi hesaplar.',
 kart='K-AFBH-04 (uçak–rüzgâr, hedef yönünde) · yönelme',kalip='şekilli',
 metin='Bir pilot, K şehrinden tam kuzeyindeki L şehrine uçmak istiyor. Rüzgâr batıdan doğuya doğru sabit hızla esmektedir. Pilot rüzgârı dengelemek için uçağın burnunu uygun yöne çeviriyor ve uçak, havaya göre sabit büyüklükte hızla, K’den L’ye doğrudan kuzey doğrultusunda ilerliyor. Hızlar ve şehirler arası uzaklık şekilde verilmiştir.\nBuna göre, uçak L şehrine kaç saatte ulaşır?',
 dogru=6,yan=[(3,'Hızları toplayıp (100 + 60 = 160 km/h) 480 ÷ 160 = 3 saat bulmuş.','bilgi'),(Fr(24,5),'Havaya göre hızı yere göre hız almış: 480 ÷ 100 = 4,8 saat.','dikkat'),(8,'Rüzgâr hızını yere göre hız almış: 480 ÷ 60 = 8 saat.','dikkat'),(12,'Hızları çıkarmış: 480 ÷ (100 − 60) = 12 saat.','islem')],
 istenen='Uçağın L’ye ulaşma süresi (saat).',ip=['Yere göre hızın doğrultusu nedir?'],
 bilgi=[B('Rüzgârlı havada yön tutma','Hedefe doğrudan gitmek için havaya göre hızın rüzgâra zıt bileşeni rüzgâr hızına eşit olmalıdır; kalan bileşen yere göre hızdır. Örnek: 13 m/s ve rüzgâr 5 m/s için yere göre hız 12 m/s’dir')],
 puf='Hedefe doğrudan gitmek için bileşenlerden biri sıfırlanır; kalan bileşen yere göre hızı verir.',sekil=SK)

# ---- 16 zor · x–t, üç araç öncüllü (F4) ----
vK16,vL16,vM16=8,-4,2; xL0=48; xM0=16
assert vK16-vL16==12 and xL0//(vK16-vL16)==4 and abs(vM16-vL16)==6 and abs(vK16-vM16)==6==abs(vL16-vM16) and vK16*4==xL0+vL16*4 and xM0+vM16*6==28
SK=axis_xt([('vurgu',[(0,0),(6,48)],'K',(5.6,40)),('blue!65!black,dashed',[(0,48),(6,24)],'L',(4.8,33)),('black,densely dotted',[(0,16),(6,28)],'M',(.7,22))],6,56,'0,1,...,6','0,8,...,56','$x$ (m)')
onc('0016','D','Doğrusal bir yolda sabit hızlarla hareket eden K, L ve M araçlarının, aynı başlangıç noktasına göre konum–zaman grafikleri şekilde verilmiştir.',
 [('M’nin L’ye göre hızının büyüklüğü 4 m/s’dir.',False,'Eğimler: v_L = −4 m/s, v_M = +2 m/s; zıt yönlü olduklarından bağıl hız 2 + 4 = 6 m/s’dir.','I numaralı yargıda L’nin kendi hızını (4 m/s) M’nin L’ye göre hızı sanmış.'),
  ('K ile L, 4. s’de yan yana gelir.',True,'Konumlar eşitlenir: 8t = 48 − 4t → t = 4 s (grafikte doğruların kesişim noktası).','II numaralı yargıda kesişimin 4. s’de olduğunu görmemiş.'),
  ('K’nin M’ye göre hızı ile L’nin M’ye göre hızının büyüklükleri eşittir.',True,'K’nin M’ye göre hızı 8 − 2 = +6 m/s, L’nin M’ye göre hızı −4 − 2 = −6 m/s; büyüklükleri 6 m/s ile eşittir.','III numaralı yargıda M’nin hareketini hesaba katmadan yere göre hızlara (8 ve 4 m/s) bakmış.')],
 ['Önce her doğrunun eğimini işaretiyle yaz, sonra her yargıdaki gözlemciyi belirle.'],
 [B('Konum–zaman grafiğinde bağıl hız','Eğim hızı verir. A’nın B’ye göre hızı v_A − v_B’dir. Örnek: eğimleri +5 ve −2 olan doğruların bağıl hızı 7 m/s’dir')],
 'Önce eğimleri işaretiyle yaz; bağıl hızlarda işaret önemlidir.','Doğru olan yargılar.','bh-xt','x–t grafiğinden bağıl hız','zor','Bağıl Hız','Konum–zaman grafiğinden hızları okuyarak bağıl hız ve karşılaşma yargılarını değerlendirir.','K-AFBH-06 (üç araçlı x–t) · öncüllü','grafik',sekil=SK)

# ---- 17 zor · şapka problemi ----
u17,v17,t_l=2,6,30; away=v17*t_l; back_t=Fr(away,v17); tot=t_l+back_t; hat=u17*tot
assert (away,back_t,tot,hat)==(180,30,60,120) and u17*t_l==60 and (v17+u17)*back_t==240 and v17*tot==360
q('0017',[A('Su çerçevesine geç','Akıntıyla sürüklenen şapka suya göre duruyor; akıntıyı yok sayıp yalnız suya göre hareketlere bak.','Şapka: suya göre 0 · kayık: suya göre 6 m/s'),
  A('Uzaklaşma','30 s boyunca kayık suya göre şapkadan uzaklaşır.','d = 6 × 30 = 180 m'),A('Dönüş süresi','Dönüşte suya göre hız yine 6 m/s’dir.','t = 180 ÷ 6 = 30 s'),
  A('Şapkanın toplam sürüklenmesi','Şapka düştüğü andan yakalanana kadar 60 s boyunca akıntıyla gider.','x = 2 × (30 + 30) = 120 m')],
 tipId='bh-akinti-yol',tip='Akıntılı nehirde doğrusal gidiş–dönüş',z='zor',alt='Nehir Problemleri',kaz='Su çerçevesine geçerek akıntıyla sürüklenen cisme göre gidiş–dönüş süresini ve yere göre uzaklığı bulur.',
 kart='K-AFBH-02 (su çerçevesinde gidiş–dönüş) · akıntıyla sürüklenen cisim',kalip='hikâyeli',
 metin='Akıntı hızı kıyıya paralel ve sabit 2 m/s olan düz bir nehirde, bir kayık suya göre sabit 6 m/s hızla akıntıya karşı ilerlemektedir. Kayıktaki Elif’in şapkası K noktasında suya düşüyor ve akıntıyla birlikte sürükleniyor. Elif, 30 s sonra şapkanın düştüğünü fark ediyor; kayığı hemen çevirip suya göre aynı büyüklükteki hızla akıntı yönünde giderek şapkayı yakalıyor. Dönüş manevrasının süresi önemsizdir.\nBuna göre, şapka yakalandığında K noktasından kaç m uzaktadır?',
 dogru=120,yan=[(60,'Şapkanın yalnız ilk 30 s’deki sürüklenmesini bulmuş: 2 × 30 = 60 m.','dikkat'),(180,'Suya göre uzaklığı (6 × 30) şapkanın yer değiştirmesi sanmış.','bilgi'),(240,'Kayığın dönüşte yere göre aldığı yolu (8 × 30) şapkanın yolu sanmış.','dikkat'),(360,'Kayığın suya göre toplam yolunu (6 × 60) bulmuş.','bilgi')],
 istenen='Şapkanın yakalandığı noktanın K’ye uzaklığı (m).',ip=['Şapkanın suya göre hızı nedir?'],
 bilgi=[B('Su çerçevesi','Akıntıyla sürüklenen bir cisme göre hareketler akıntı yokmuş gibi incelenir; gidiş ve dönüş süreleri eşit olur. Örnek: suya göre 4 m/s’lik kayık 10 s uzaklaşırsa aynı hızla 10 s’de geri döner')],
 puf='Akıntıyla sürüklenen cisme göre gidiş ve dönüş süreleri eşittir; akıntı süreyi değil yer değiştirmeyi belirler.')

# ---- 18 zor · tablo + zincir öncüllü ----
vB,vAB_=8,-3; vAy=vB+vAB_; vKA,vLA,vMA=10,-6,4; assert vAy==5 and vAy+vKA==15 and vAy+vLA==-1 and vAy+vMA-vB==1
rows=[('K','10','doğu'),('L','6','batı'),('M','4','doğu')]
tb=['\\node[font=\\small\\bfseries] at (3.2,3.35) {Ayşe’ye göre hızlar};','\\draw[thick] (0,0) rectangle (6.4,3.0); \\draw (0,2.25)--(6.4,2.25) (0,1.5)--(6.4,1.5) (0,.75)--(6.4,.75) (1.4,0)--(1.4,3.0) (4.2,0)--(4.2,3.0);',
  '\\node at (.7,2.62) {\\bfseries Araç};\\node at (2.8,2.62) {\\bfseries Hız (m/s)};\\node at (5.3,2.62) {\\bfseries Yön};']
for i,(a,b,c) in enumerate(rows): y_=1.87-i*.75; tb.append('\\node at (.7,%.2f) {%s};\\node at (2.8,%.2f) {%s};\\node at (5.3,%.2f) {%s};'%(y_,a,y_,b,y_,c))
SK=tk(f1(tb))
onc('0018','E','Doğu–batı doğrultusunda uzanan düz bir yolda K, L ve M araçları sabit hızlarla gitmektedir. Ayşe, Berk’e göre batı yönünde 3 m/s hızla yürümektedir. Berk yere göre doğu yönünde 8 m/s hızla gitmektedir. K, L ve M araçlarının Ayşe’ye göre hızları tabloda verilmiştir.',
 [('K’nin yere göre hızı doğu yönünde 15 m/s’dir.',True,'Ayşe’nin yere göre hızı 8 − 3 = 5 m/s doğuya; K’nin yere göre hızı 5 + 10 = 15 m/s doğuya.','I numaralı yargıda Ayşe’nin yere göre hızını bulmadan hız zincirini kurmuş.'),
  ('L’nin yere göre hızı doğu yönünde 1 m/s’dir.',False,'Ayşe’nin yere göre hızı +5 m/s; L, Ayşe’ye göre batıya 6 m/s: 5 − 6 = −1 m/s, yani batıya 1 m/s.','II numaralı yargıda eksi işareti (yönü) gözden kaçırmış.'),
  ('M’nin Berk’e göre hızı doğu yönünde 1 m/s’dir.',True,'M’nin yere göre hızı 5 + 4 = 9 m/s; Berk’e göre 9 − 8 = 1 m/s doğuya.','III numaralı yargıda M’nin Ayşe’ye göre hızını Berk’e göre hız sanmış.')],
 ['Önce Ayşe’nin yere göre hızını bul; sonra her yargıda gözlemciyi belirle.'],
 [B('Hız zinciri','v_AC = v_AB + v_BC: A’nın C’ye göre hızı, A’nın B’ye göre ve B’nin C’ye göre hızlarının vektörel toplamıdır. Örnek: yürüyen merdivende merdivene göre 1 m/s, merdivenin yere göre hızı 2 m/s ise yere göre hız 3 m/s olur')],
 'Hız zincirinde ara gözlemciyi yere bağlayarak adım adım ilerle.','Doğru olan yargılar.','bh-referans','Referans sistemleri ve bağıl hız zinciri','zor','Referans Sistemi','Birden çok gözlemci arasında hız zincirini kurarak bağıl hızları bulur.','K-AFBH-08 (tablo + zincir) · öncüllü','tablo',sekil=SK)

# ---- 19 zor · iki kayık dik geçiş öncüllü ----
W19,uu,vX,vY=80,1,4,2; tX,tY=Fr(W19,vX),Fr(W19,vY); assert (tX,tY)==(20,40) and sqrt(vX**2+uu**2)!=5 and uu*tX==20 and uu*tY==40
onc('0019','A','Kıyıları paralel, genişliği 80 m olan düz bir nehirde akıntı hızı kıyıya paralel ve 1 m/s’dir. X ve Y kayıkları aynı kıyıdaki aynı noktadan aynı anda, kıyıya dik doğrultuda ve suya göre sırasıyla 4 m/s ile 2 m/s’lik sabit hızlarla karşı kıyıya yönelmiştir.',
 [('X’in Y’ye göre hızının büyüklüğü 3 m/s’dir.',False,'Akıntı iki kayığa da aynı etkiyi yapar ve bağıl hızda birbirini götürür; fark yalnız suya göre hızlardan gelir: 4 − 2 = 2 m/s.','I numaralı yargıda akıntıyı bağıl hıza da katmış (4 − 2 + 1).'),
  ('X karşı kıyıya ulaştığı anda Y, X’in 20 m gerisindedir.',False,'X 80 ÷ 4 = 20 s’de karşıya varır; Y bu sürede dik yönde 2 × 20 = 40 m gitmiştir, X’ten 40 m gerisindedir.','II numaralı yargıda Y’nin 20 s’de gittiği yolu hesaplamadan hız farkını (2 m/s) kullanmış.'),
  ('X karşı kıyıya ulaştığı anda X ile Y arasındaki uzaklık 40 m’dir.',True,'İki kayık da 20 s’de akıntıyla aynı 1 × 20 = 20 m sürüklenmiştir; kıyıya paralel fark sıfır, dik fark 80 − 40 = 40 m’dir.','III numaralı yargıda iki kayığın sürüklenme farkı olduğunu sanmış.')],
 ['Karşıya geçiş süresi yalnız kıyıya dik hıza bağlıdır; iki kayığın konumlarını aynı anda karşılaştır.'],
 [B('Dik hareketlerin bağımsızlığı','Kıyıya dik ve paralel bileşenler birbirini etkilemez; geçiş süresi genişlik ÷ dik hızdır, sürüklenme akıntı × süredir. Örnek: 60 m, dik hız 3 m/s, akıntı 2 m/s için süre 20 s, sürüklenme 40 m')],
 'Akıntı aynı ortamdaki tüm cisimlere aynı etkiyi yapar; aralarındaki bağıl hareketi değiştirmez.','Doğru olan yargılar.','bh-karsiya-gecis','Nehirde karşıya geçiş: süre ve sürüklenme','zor','Nehir Problemleri','İki kayığın karşıya geçiş anındaki bağıl konum ve hızlarını yargılarla karşılaştırır.','K-AFBH-03 (iki kayık, öncüllü) · bağıl konum','öncüllü')

# ---- 20 zor · kıyıdaki araç + karşıya geçen motor ----
W20,uu20,vm20,va20=160,3,4,6; t20=Fr(W20,vm20); mx=uu20*t20; ax=va20*t20; dist=sqrt((ax-mx)**2+W20**2)
assert t20==40 and mx==120 and ax==240 and dist==200 and ax-mx==120 and ax==240 and (ax-mx)+W20==280 and sqrt(vm20**2+(va20-uu20)**2)*t20==200
q('0020',[A('Süreyi bul','Karşıya geçiş süresi yalnız kıyıya dik bileşenle belirlenir.','t = 160 ÷ 4 = 40 s'),
  A('Konumları bul','Araç kıyı boyunca 6 m/s, motor akıntıyla 3 m/s sürüklenir (kıyıya paralel yönde).','x_araç = 6 × 40 = 240 m · x_motor = 3 × 40 = 120 m'),
  A('Konum farkı','Kıyıya paralel fark 240 − 120 = 120 m; dik fark nehir genişliğidir.','Δx = 120 m · Δy = 160 m'),
  A('Uzaklığı yaz','İki fark birbirine dik olduğundan Pisagor kullanılır.','d = √(120² + 160²) = 200 m'),
  A('Kontrol et','Motorun araca göre hızı: paralel −3, dik 4 → 5 m/s; 5 × 40 = 200 m.','200 m')],
 tipId='bh-karsiya-gecis',tip='Nehirde karşıya geçiş: süre ve sürüklenme',z='zor',alt='Nehir Problemleri',kaz='Karşıya geçen motorun ve kıyıdaki aracın konumlarını bağıl hareketle birleştirip aralarındaki uzaklığı bulur.',
 kart='K-AFBH-03 (kıyıdaki araç + karşıya geçen motor) · bağıl konum',kalip='hikâyeli',
 metin='Kıyıları paralel, genişliği 160 m olan düz bir nehirde akıntı hızı kıyıya paralel, doğu yönünde ve 3 m/s’dir. Bir motor, kıyıdaki O noktasından kıyıya dik doğrultuda ve suya göre sabit 4 m/s hızla karşı kıyıya geçiyor. Aynı anda O noktasından geçen bir araç, motor yola çıkarken aynı kıyıda doğu yönünde yere göre sabit 6 m/s hızla gitmeye başlıyor.\nBuna göre, motor karşı kıyıya ulaştığı anda motor ile araç arasındaki uzaklık kaç m’dir?',
 dogru=200,yan=[(120,'Yalnız kıyıya paralel konum farkını (240 − 120) bulmuş; nehrin genişliğini katmamış.','dikkat'),(160,'Yalnız nehrin genişliğini uzaklık almış; paralel konum farkını unutmuş.','dikkat'),(240,'Aracın karşıya geçiş süresince aldığı yolu (6 × 40) uzaklık sanmış.','bilgi'),(280,'Paralel ve dik farkları cebirsel toplamış: 120 + 160.','islem')],
 istenen='Motor ile araç arasındaki uzaklık (m).',ip=['Her iki cismin t anındaki konumunu O’ya göre iki doğrultuda ayrı ayrı yaz.'],
 bilgi=[B('Bağıl konum','Birbirine dik doğrultulardaki konum farkları ayrı ayrı bulunur, aradaki uzaklık Pisagor ile hesaplanır. Örnek: dik farkları 9 m ve 12 m olan iki cisim arasındaki uzaklık 15 m’dir')],
 puf='Bağıl konumu iki dik doğrultuda ayrı bul, sonra Pisagor ile birleştir.')

# ---------- yaz ----------
for x in P.ANA: x['kardes']=None
P.yaz(os.path.join(GD,'bagil-1.json'),os.path.join(os.environ.get('SCRATCH','/tmp'),'bos-bagil.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik, MEB 11. sınıf bağıl hareket.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','afbagil.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
