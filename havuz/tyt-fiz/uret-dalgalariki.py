"""TYT Fizik · Dalgalar (ikinci paket) · 20 soru, hafif mod (kardeş yok, ipucu 1). Şekiller TikZ; konum, açı ve genlik değerleri Python'da hesaplanır.
Her cevap, çeldirici değeri ve öncül Python'da assert edilir."""
import sys,os,math,json,itertools
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt,asin,acos,pi
from fractions import Fraction as Fr
H.KONU='Dalgalar'
P=Parti('dalgalariki','Dalgalar','fiz|Dalgalar',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · Fizikpedia (yalnız mantık) · MEB 10. sınıf fizik'
def kartla(id,alt,fikir,tuzak,z,adim,tipId,tip,kalip='şekilli'):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
STL='Stealth[length=1.9mm,width=1.7mm]'
def pt(p): return f'({p[0]:.3f},{p[1]:.3f})'
def seg(a,b,st='thick'): return f'\\draw[{st}] {pt(a)} -- {pt(b)};'
def ray(a,b,col='vurgu',w='thick',at=.55):
    ar='\\arrow{'+STL+'}'
    return '\\draw['+col+','+w+',postaction={decorate,decoration={markings,mark=at position '+str(at)+' with {'+ar+'}}}] '+pt(a)+' -- '+pt(b)+';'
def nd(p,txt,anc='',st=''):
    return f'\\node[{anc},inner sep=1.5pt{st}] at {pt(p)} {{{txt}}};'
def add(p,q_): return (p[0]+q_[0],p[1]+q_[1])
def mul(p,s): return (p[0]*s,p[1]*s)
def poly(pts,st='thick'): return f'\\draw[{st}] '+' -- '.join(pt(p) for p in pts)+';'
def dim(a,b,txt,pos='below',off=''):
    return f'\\draw[<->,thin] {pt(a)} -- {pt(b)}; \\node[{pos},inner sep=1pt,fill=white{off}] at {pt(((a[0]+b[0])/2,(a[1]+b[1])/2))} {{{txt}}};'
def bump(x,c,w,h):
    """cos² biçimli atma: merkez c, yarı genişlik w, yükseklik h"""
    return h*cos(pi*(x-c)/(2*w))**2 if abs(x-c)<w else 0.0
def wire(x0,x1,f,n=160,st='thick'):
    return poly([(x0+(x1-x0)*i/n,f(x0+(x1-x0)*i/n)) for i in range(n+1)],st)
ALL=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def kume(t):
    idx=[i for i in range(3) if t[i]]; r=['I','II','III']
    if len(idx)==1: return 'Yalnız '+r[idx[0]]
    if len(idx)==2: return ' ve '.join(r[i] for i in idx)
    return 'I, II ve III'
def onc_sira(dogru,harf):
    k=ALL.index(dogru); p=' ABCDE'.index(harf)-1
    for c in itertools.combinations(range(7),5):
        if k in c and c.index(k)==p: return [ALL[i] for i in c]
    raise AssertionError((dogru,harf))
def qo(no,ad,truth,harf,neden,**k):
    """öncüllü soru: truth=(I,II,III); neden[i]=(açıklama,tür) o yargıyı yanlış değerlendirme nedeni."""
    dg=kume(truth); sira=onc_sira(dg,harf); yan=[]
    for s in sira:
        if s==dg: continue
        cum={'Yalnız I':(1,0,0),'Yalnız II':(0,1,0),'Yalnız III':(0,0,1),'I ve II':(1,1,0),'I ve III':(1,0,1),'II ve III':(0,1,1),'I, II ve III':(1,1,1)}[s]
        fark=[i for i in range(3) if bool(cum[i])!=bool(truth[i])]; assert fark
        txt=' '.join(f"{['I','II','III'][i]}. yargıyı {'yanlış' if truth[i] else 'doğru'} sanmış: {neden[i][0]}" for i in fark)
        yan.append((s,txt,neden[fark[0]][1]))
    q(no,ad,dogru=dg,yan=yan,sira=sira,**k)
def yer(dogru,dig,harf):
    p=' ABCDE'.index(harf)-1; assert 0<=p<=4; return list(dig[0:p])+[dogru]+list(dig[p:])
def qt(no,ad,dogru,yan,harf,**k):
    """metin şıklı soru: doğru şık istenen harfe yerleşir (yan sırası korunur)."""
    sira=yer(dogru,[y[0] for y in yan],harf); q(no,ad,dogru=dogru,yan=yan,sira=sira,**k)
TIPK={}
def kt(*a,**k):
    kartla(*a,**k); TIPK[a[6]]='fiz|Dalgalar'
DAL=B('Dalga büyüklükleri','periyot ve frekans ters orantılıdır: T = 1 ÷ f. Dalga hızı v = λ × f’dir; bir dalga boyu (λ), aynı fazdaki iki ardışık nokta arasındaki uzaklıktır. Örnek: f = 2 Hz, λ = 7 m ise v = 14 m/s')

# ------------------------------------------------------------------ KARTLAR
kt('K-FZDL2-01','Dalga grafiği (y–x) okuma','Konum–yer değiştirme grafiğinde dalga boyu aynı fazdaki iki nokta arasından, genlik denge konumundan en uzak noktaya uzaklıktan okunur; fazlar tepe–çukur ilişkisiyle karşılaştırılır.','Genliği tepe–çukur arası sanmak; yarım dalga boyunu dalga boyu almak; tepe ile çukuru aynı fazda saymak.','kolay',3,'fz-dl2-grafik-yx','Dalga grafiğinden dalga boyu, genlik ve faz','grafik')
kt('K-FZDL2-02','Titreşim hareketi ve dalga sınıflaması','Titreşim doğrultusu yayılma doğrultusuna dikse enine, paralelse boyuna dalga; ortam isteyenler mekanik, boşlukta yayılanlar elektromanyetik dalgadır.','Ses dalgasını enine, ışığı mekanik sanmak.','kolay',3,'fz-dl2-sinif','Enine–boyuna ve mekanik–elektromanyetik dalga','öncüllü')
kt('K-FZDL2-03','Sarkaçta periyot, frekans ve yol','Yarım titreşim süresinden periyot; bir periyotta yol 4 × genliktir (genlik, uç noktalar arası uzaklığın yarısı).','Uç noktalar arasını genlik sanmak; yarım titreşimi periyot almak.','orta',4,'fz-dl2-titresim','Titreşim hareketi: periyot, genlik ve alınan yol','şekilli')
kt('K-FZDL2-04','İp dalgası ve dalga denklemi','Şekilden kaç dalga boyunun çizildiği sayılır, λ bulunur; frekans titreşim sayısından hesaplanır ve v = λ × f uygulanır.','Yarım dalgaları atlayıp sayım hatası; frekans yerine periyot kullanmak.','orta',4,'fz-dl2-ip-dalga','Dalga boyu sayımı ve dalga hızı','şekilli')
kt('K-FZDL2-05','İnce–kalın yay geçişi','Atma ince yaydan kalın yaya geçerken yansıyan atma ters döner, iletilen atma aynı yönlüdür; kalın yayda atmanın hızı azalır.','Yansıyanın da aynı yönlü olduğunu sanmak; kalın yayda hızın arttığını düşünmek.','orta',3,'fz-dl2-ince-kalin','Atmanın ince–kalın yay geçişinde yansıması ve iletilmesi','öncüllü')
kt('K-FZDL2-06','Sabit uçtan yansıyan atmanın konumu','Atma sabit uçtan ters dönerek (tepe çukura) aynı hızla yansır; konum, toplam yoldan duvara gidilen yol çıkarılarak bulunur.','Yansımada atmanın yönünü korumasını sanmak; toplam yolu duvara uzaklık gibi almak.','zor',4,'fz-dl2-sabit-uc','Sabit uçtan yansıyan atmanın konumu','şekilli')
kt('K-FZDL2-07','Sabit ve serbest uçtan yansıma','Sabit uçtan yansıyan atma ters döner, serbest uçtan yansıyan atma aynı yönlü kalır; iki durumda da hız değişmez.','Serbest uçta da ters dönmesini beklemek; yansımada hızın değiştiğini sanmak.','kolay',3,'fz-dl2-uc-yansima','Sabit ve serbest uçtan yansıma','öncüllü')
kt('K-FZDL2-08','Atmaların üst üste binmesi','Karşılaşan atmaların yer değiştirmeleri cebirsel toplanır; tepe artı, çukur eksi alınır; atmalar sonra yollarına bozulmadan devam eder.','Genlikleri mutlak değer olarak toplamak; işareti atlamak.','zor',4,'fz-dl2-superpozisyon','Atmaların süperpozisyonu (farklı genlik)','şekilli')
kt('K-FZDL2-09','Su dalgasının derin–sığ geçişinde kırılması','Geçişte frekans sabit kalır; sığ bölgede hız ve dalga boyu küçülür, dalga cepheleri arası daralır, yön normale yaklaşır.','Frekansın da değiştiğini sanmak; sığda dalga boyunun arttığını düşünmek.','orta',3,'fz-dl2-su-kirilma','Derin–sığ geçişte su dalgasının kırılması','öncüllü')
kt('K-FZDL2-10','Doğrusal su dalgasının düz engelden yansıması','Yansıma yasası: yansıma açısı gelme açısına eşittir; açılar normalle ölçülür.','Açıyı yüzeyle ölçüp normalle karıştırmak; dalganın geri döndüğünü (aynı doğru) sanmak.','kolay',3,'fz-dl2-su-dogrusal','Doğrusal dalganın yansıması','şekilli')
kt('K-FZDL2-11','Dairesel su dalgasının düz engelden yansıması','Yansıyan dairesel dalgalar, kaynağın engele göre ayna görüntüsü olan noktadan yayılıyormuş gibi davranır.','Yansıyanların engel üzerindeki bir noktadan ya da kaynaktan çıktığını sanmak.','orta',3,'fz-dl2-su-dairesel','Dairesel dalganın düz engelden yansıması','şekilli')
kt('K-FZDL2-12','Dalga leğeninde derinlik–hız–dalga boyu','Frekans sabitken v = λ × f; dalga boyu küçük olan bölgede hız küçük, bölge sığdır; hızlar dalga boylarıyla orantılıdır.','En büyük dalga boyunu en sığ bölge sanmak; frekansın bölgeye göre değiştiğini düşünmek.','orta',3,'fz-dl2-su-tablo','Derinlik, hız ve dalga boyu ilişkisi (tablo)','tablo')
kt('K-FZDL2-13','Ses: yükseklik, şiddet ve osiloskop','Frekans sesin yüksekliğini (ince–kalın), genlik şiddetini (güçlü–zayıf) belirler; osiloskopta sıklık frekansı, tepe yüksekliği genliği gösterir.','Genlik büyüklüğünü sesin incelik derecesi sanmak; şiddet ile yüksekliği karıştırmak.','orta',3,'fz-dl2-ses-osiloskop','Sesin yüksekliği ve şiddeti (osiloskop)','grafik')
kt('K-FZDL2-14','Yankı ve iki duvar arası uzaklık','Yankıda ses gidip dönerken yol iki katıdır; iki duvar arası, her duvara olan uzaklıkların toplamıdır.','Gidiş–dönüş süresini yarıya bölmeyi unutmak; süre farkını toplam almak.','orta',4,'fz-dl2-yanki','Yankı ve uzaklık','şekilli')
kt('K-FZDL2-15','Ses hızının ortama göre değişimi','Ses katıda en hızlı, gazda en yavaş yayılır; ortam değişince frekans sabit kalır, hız ve dalga boyu değişir.','Ortam değişince frekansın değiştiğini sanmak; süreyi hesaplarken hızı ters kullanmak.','orta',3,'fz-dl2-ses-hizi','Ortamlara göre ses hızı (tablo)','tablo')
kt('K-FZDL2-16','Rezonans','Doğal frekansı vurulan kaynakla aynı olan cisim, gelen ses dalgalarıyla titreşmeye başlar (rezonans); farklı frekanslıda etki görülmez.','Yakınlıkla titreşimin her cisimde olacağını sanmak; frekansın havada azaldığını düşünmek.','orta',3,'fz-dl2-rezonans','Rezonans (diyapazon)','şekilli')
kt('K-FZDL2-17','Ultrases ve sonar','Frekansı 20 000 Hz üzerindeki ses ultrasestir; sonarda yankı süresinin yarısı gidiş süresidir (derinlik = v · t ÷ 2).','Ortamı yanlış seçip havadaki hızı kullanmak; yankı süresini bölmeden almak.','kolay',3,'fz-dl2-ultrases','Ultrases ve sonar uygulaması','hikâyeli')
kt('K-FZDL2-18','Sismogram: P, S ve yüzey dalgaları','İlk kaydedilen P dalgası (boyuna, en hızlı), sonra S (enine); en büyük genlik yüzey dalgalarına aittir.','En büyük genlikli kaydı S saymak; P dalgasını enine sanmak.','orta',3,'fz-dl2-sismogram','Deprem dalgaları ve sismogram','grafik')
kt('K-FZDL2-19','P ve S varış farkından uzaklık','Aynı yolu P ve S dalgaları farklı sürelerde alır: d ÷ v_S − d ÷ v_P = Δt; saat farkı şekilden okunur.','Varış farkını P dalgasının yol süresi sanmak; hızları toplamak.','zor',4,'fz-dl2-ps-fark','Deprem merkezine uzaklık (P–S farkı)','grafik')
kt('K-FZDL2-20','Deprem şiddeti, büyüklüğü ve korunma','Büyüklük depremin enerjisini ölçer, tek değerdir; şiddet yere göre değişen hasar ölçüsüdür, merkez üssünden uzaklaştıkça genelde azalır; deprem anında çök–kapan–tutun uygulanır.','Büyüklüğün yere göre değiştiğini sanmak; şiddet ile büyüklüğü karıştırmak.','orta',3,'fz-dl2-siddet','Deprem büyüklüğü, şiddeti ve korunma','öncüllü')

# ================================================================== 01 · grafik y–x · kolay · öncüllü · A
lam=8; Ay=2; sx,sy=.5,.55
def W(x,y): return (x*sx,y*sy)
assert abs(Ay*sin(2*pi*2/lam)-2)<1e-9 and abs(Ay*sin(2*pi*6/lam)+2)<1e-9 and abs(Ay*sin(2*pi*8/lam))<1e-9
fo=[]
for xv in range(2,13,2): fo.append(f'\\draw[gray!50,dashed,thin] {pt(W(xv,-2.6))} -- {pt(W(xv,2.6))};')
for yv in (-2,2): fo.append(f'\\draw[gray!50,dashed,thin] {pt(W(0,yv))} -- {pt(W(12.4,yv))};')
fo.append(f'\\draw[->,thick] {pt(W(-.2,0))} -- {pt(W(13,0))};\\draw[->,thick] {pt(W(0,-3))} -- {pt(W(0,3.1))};')
fo.append(nd(W(13.1,0),'$x$ (cm)','right')); fo.append(nd(W(0,3.1),'$y$ (cm)','above'))
for xv in range(2,13,2): fo.append(nd(add(W(xv,0),(0,-.0)),f'${xv}$','below',',yshift=-1pt'))
fo.append(nd(W(0,2),'$2$','left')); fo.append(nd(W(0,-2),'$-2$','left'))
pts_=[(x*sx,Ay*sin(2*pi*x/lam)*sy) for x in [i*.1 for i in range(121)]]
fo.append(poly(pts_,'very thick,vurgu'))
fo.append(f'\\fill {pt(W(2,2))} circle (2pt);'+nd(W(2,2),'K','above')); fo.append(f'\\fill {pt(W(6,-2))} circle (2pt);'+nd(W(6,-2),'M','below'))
SK=tikz_svg(HEAD+'\n'.join(x for x in fo if x)+TAIL)
qo('0001',[A('Dalga boyunu oku','Bir dalga boyu, aynı fazdaki iki ardışık nokta arasıdır. Grafikte dalga x = 0’da denge konumundan yukarı doğru başlar ve x = 8 cm’de aynı noktaya aynı yönde döner.','λ = 8 cm → I. doğru'),
 A('Genliği belirle','Genlik, dalganın denge konumundan en uzak noktaya (tepe ya da çukur) uzaklığıdır. Tepe y = 2 cm’dedir; tepe ile çukur arası 4 cm’dir.','Genlik = 2 cm → II. yanlış'),
 A('K ile M’yi karşılaştır','K bir tepe, M bir çukurdur; tepe ile çukur zıt fazdadır. Aynı fazlı noktalar arası uzaklık λ = 8 cm’dir, K–M arası ise 4 cm’dir.','K ve M zıt fazlı → III. yanlış'),
 A('Sonuç','Yalnız I. yargı doğrudur.','Yalnız I')],
 truth=(True,False,False),harf='A',tipId='fz-dl2-grafik-yx',tip='Dalga grafiğinden dalga boyu, genlik ve faz',z='kolay',alt='Dalga Kavramları',kaz='Konum–yer değiştirme grafiğinden dalga boyunu, genliği ve fazı yorumlar.',
 kart='K-FZDL2-01 (y–x grafiği: λ, genlik, faz) · gergin ip, K tepe ve M çukur',kalip='grafik',
 metin='Bir öğrenci, gergin bir ip boyunca ilerleyen enine dalganın belirli bir andaki fotoğrafından yararlanarak konum–yer değiştirme (y–x) grafiğini şekildeki gibi çizmiştir. Grafikte x ekseni ip boyunca konumu, y ekseni ipin denge konumundan olan uzaklığını göstermektedir; iki eksen de cm cinsindendir. K ve M, ip üzerinde işaretlenmiş iki noktadır.\nBuna göre,\nI. Dalganın dalga boyu 8 cm’dir.\nII. Dalganın genliği 4 cm’dir.\nIII. K ve M noktaları aynı fazdadır.\nyargılarından hangileri doğrudur?',
 neden=[('dalga boyunu tepe ile çukur arası 4 cm okumuş; bir dalga boyu aynı fazlı iki nokta arasıdır.','dikkat'),('genliği tepe ile çukur arasındaki 4 cm sanmış; genlik denge konumundan en uzak noktaya olan uzaklıktır.','bilgi'),('tepe ile çukuru aynı fazda saymış; K ve M zıt fazdadır.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Aynı fazdaki iki noktayı ve dalganın denge konumundan en uzak noktasını grafikte ayrı ayrı bul.'],
 bilgi=[DAL],
 puf='Dalga boyu aynı fazlı iki nokta arasıdır, genlik denge konumundan tepeye (çukura) uzaklıktır; tepe ile çukur zıt fazdadır.',sekil=SK)

# ================================================================== 02 · enine–boyuna, mekanik–elektromanyetik · kolay · öncüllü · B
qo('0002',[A('Yayı ileri–geri hareket ettir','Yayın serbest ucu yay doğrultusunda ileri–geri oynatılınca titreşim yönü ile yayılma yönü aynı doğrultudadır; bu boyuna dalgadır.','dalga boyuna, enine değil → I. yanlış'),
 A('Dalganın türüne bak','Yay, yani maddesel bir ortam titreştiği için oluşan dalgalar mekanik dalgadır; elektromanyetik dalgalar maddesiz ortamda da yayılabilir.','mekanik dalga, elektromanyetik değil → II. yanlış'),
 A('Dik titreştirmeyi incele','Yayı doğrultusuna dik yönde titreştirince titreşim yönü yayılma yönüne diktir; bu enine dalgadır. Havadaki ses dalgası ise boyunadır.','enine dalga, ses boyuna → III. doğru'),A('Sonuç','Yalnız III. yargı doğrudur.','Yalnız III')],
 truth=(False,False,True),harf='B',tipId='fz-dl2-sinif',tip='Enine–boyuna ve mekanik–elektromanyetik dalga',z='kolay',alt='Dalga Türleri',kaz='Dalgaları titreşim yönüne ve yayılma ortamına göre sınıflandırır.',
 kart='K-FZDL2-02 (sarmal yay ile enine/boyuna dalga) · mekanik–elektromanyetik ayrımı',kalip='öncüllü',
 metin='Fizik laboratuvarında bir ucu masaya sabitlenmiş sarmal yayın serbest ucu önce yay doğrultusunda ileri–geri, ardından yay doğrultusuna dik yönde düzenli olarak hareket ettiriliyor. Her iki durumda da yay boyunca ilerleyen dalgalar gözleniyor. Öğrenciler bu dalgaları havadaki ses dalgası ve boşlukta da yayılabilen ışık dalgasıyla karşılaştırıyor.\nBuna göre,\nI. Yay doğrultusunda ileri–geri hareketle oluşan dalga enine dalgadır.\nII. Yayda oluşan dalgalar elektromanyetik dalgadır.\nIII. Yaya dik yönde titreştirmeyle oluşan dalga, ses dalgasından farklı olarak enine dalgadır.\nyargılarından hangileri doğrudur?',
 neden=[('titreşimin yayılma doğrultusunda olduğunu fark etmeyip dalgayı enine saymış; bu dalga boyunadır.','bilgi'),('yaydaki dalgaların da ışık gibi elektromanyetik olduğunu sanmış; yay dalgası maddesel ortamda ilerleyen mekanik dalgadır.','bilgi'),('ses dalgasını da enine sanmış; ses dalgası boyunadır.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her yargıda titreşim yönü ile yayılma yönü arasındaki ilişkiyi ve dalganın yayılmak için ortam isteyip istemediğini ayrı ayrı düşün.'],
 bilgi=[B('Dalga türleri','titreşim yönü yayılma yönüne diktir → enine dalga; aynı doğrultudaysa → boyuna dalga. Ortam gerektiren dalgalar mekanik (yay, su, ses), boşlukta da yayılanlar elektromanyetik dalgadır (ışık, radyo dalgaları). Örnek: su yüzeyindeki dalga mekanik ve enine, deprem P dalgası mekanik ve boyunadır')],
 puf='Titreşim yönü yayılmaya dikse enine, paralelse boyunadır; yay ve ses mekaniktir, ışık elektromanyetiktir.')

# ================================================================== 03 · sarkaç · orta · şekilli · C (sayısal)
th=radians(16); Ls=3.0; xk=Ls*sin(th); yk=Ls-Ls*cos(th)
KM=8; T_=Fr(4,5); t_=8; Aa=Fr(KM,2)
nT=Fr(t_)/T_; assert nT==10 and 4*Aa*nT==160
assert 10*Aa==40 and 10*KM==80 and 4*Aa*Fr(t_)/Fr(2,5)==320 and 4*KM*Fr(t_)/Fr(2,5)==640
fo=[]
fo.append(f'\\fill[gray!35] (-1.3,3) rectangle (1.3,3.2);\\draw[thick] (-1.3,3) -- (1.3,3);')
fo.append(f'\\draw[thick] (0,3) -- (0,0); \\draw[gray,dashed] (0,3) -- ({-xk:.3f},{yk:.3f}); \\draw[gray,dashed] (0,3) -- ({xk:.3f},{yk:.3f});')
fo.append(f'\\draw[gray,dashed] ({-xk:.3f},{yk:.3f}) arc[start angle={-90-degrees(th):.2f},end angle={-90+degrees(th):.2f},radius={Ls}];')
for x_,y_,n_,fl in ((-xk,yk,'K','white'),(0,0,'L','vurgu!35'),(xk,yk,'M','white')):
    fo.append(f'\\draw[thick,fill={fl}] ({x_:.3f},{y_-.17:.3f}) circle (.17);')
    fo.append(nd((x_,y_-.5),n_,'below'))
fo.append(dim((-xk,yk-1.05),(xk,yk-1.05),'8 cm','below'))
fo.append(f'\\draw[dotted] ({-xk:.3f},{yk-.35:.3f}) -- ({-xk:.3f},{yk-1.05:.3f}); \\draw[dotted] ({xk:.3f},{yk-.35:.3f}) -- ({xk:.3f},{yk-1.05:.3f});')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0003',[A('Yarım titreşimden periyoda geç','K’den M’ye gitmek yarım titreşimdir; tam titreşim K–L–M–L–K yolunun tamamıdır.','T = 2 × 0,4 = 0,8 s'),
 A('Titreşim sayısını bul','Verilen süreyi periyoda böl.','n = 8 ÷ 0,8 = 10 titreşim'),
 A('Bir titreşimdeki yolu hesapla','Genlik, uç noktalar arası uzaklığın yarısıdır: 4 cm. Bir tam titreşimde cisim 4 genlik yol alır.','4 × 4 = 16 cm'),
 A('Toplam yolu bul','Titreşim sayısı ile bir titreşimdeki yol çarpılır.','10 × 16 = 160 cm')],
 dogru=160,yan=[(40,'Bir titreşimde yalnız bir genlik (4 cm) yol aldığını düşünmüş: 10 × 4 = 40 cm.','bilgi'),(80,'K–M arasını (8 cm) bir titreşimdeki yol saymış: 10 × 8 = 80 cm.','dikkat'),
 (320,'K’den M’ye geçiş süresini (0,4 s) periyot sanmış: 20 titreşim × 16 = 320 cm.','dikkat'),(640,'Hem 0,4 s’yi periyot almış hem K–M arasını genlik sanmış: 20 × 4 × 8 = 640 cm.','bilgi')],
 tipId='fz-dl2-titresim',tip='Titreşim hareketi: periyot, genlik ve alınan yol',z='orta',alt='Dalga Kavramları',kaz='Titreşim hareketinde periyot, frekans ve genlikten alınan yolu hesaplar.',
 kart='K-FZDL2-03 (sarkaç: periyot, genlik, yol) · K–M = 8 cm, 0,4 s, 8 s',kalip='şekilli',
 metin='Şekildeki basit sarkacın cismi, sürtünmesiz ortamda L denge noktasının iki yanında K ve M uç noktaları arasında gidip gelmektedir. Cisim K noktasından serbest bırakıldıktan 0,4 s sonra M noktasına ilk kez ulaşmaktadır. K ile M arasındaki uzaklık 8 cm’dir ve sarkacın salınımı K–L–M–L–K yolunu izleyerek sürmektedir.\nBuna göre cismin 8 saniyede aldığı toplam yol kaç cm’dir?',
 istenen='Cismin 8 s’de aldığı toplam yol (cm).',
 ip=['Önce bir tam titreşimin kaç saniye sürdüğünü ve bir tam titreşimde cismin kaç genlik yol aldığını belirle.'],
 bilgi=[B('Titreşim hareketi','bir tam titreşim, cismin aynı noktadan aynı yönde yeniden geçtiği hareketin tamamıdır; süresine periyot (T) denir. Cisim bir periyotta 4 genlik yol alır. Örnek: uç noktaları arası 6 cm olan sarkacın genliği 3 cm, bir periyotta yolu 12 cm’dir')],
 puf='Bir periyotta alınan yol 4 genliktir; genlik, uç noktalar arası uzaklığın yarısıdır.',sekil=SK)

# ================================================================== 04 · ip dalgası · orta · şekilli · D (sayısal)
lam4=6; f4=Fr(12,4); v4=lam4*f4; assert v4==18 and Fr(15,Fr(5,2))==lam4
assert Fr(lam4)/f4==2 and 12*1==12 and Fr(15,3)*f4==15 and 15*f4==45
sc=.4; A4=.55
fo=[]
fo.append(f'\\draw[gray,dashed] (0,0) -- ({15*sc:.3f},0);')
fo.append(wire(0,15*sc,lambda x:A4*sin(2*pi*x/(lam4*sc)),n=200,st='very thick,vurgu'))
fo.append(f'\\draw[thick,fill=gray!25] (-.65,-.3) rectangle (-.05,.3);'+nd((-.35,0),'S')+f'\\draw[<->,thin] (-.35,.45) -- (-.35,.95);')
fo.append(f'\\fill ({15*sc:.3f},0) circle (2pt);'+nd((15*sc,0),'P','right'))
for k_ in range(0,6): fo.append(f'\\draw[gray,dotted] ({3*k_*sc:.3f},-.62) -- ({3*k_*sc:.3f},.62); \\fill ({3*k_*sc:.3f},0) circle (1.3pt);')
fo.append(dim((0,-1.05),(15*sc,-1.05),'15 m','below'))
fo.append(f'\\draw[dotted] (0,-.3) -- (0,-1.05); \\draw[dotted] ({15*sc:.3f},-.15) -- ({15*sc:.3f},-1.05);')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0004',[A('Dalga boyunu bul','S’den P’ye uzaklık yarım dalgalarla birlikte sayılır; şekilde 2,5 dalga vardır.','2,5 λ = 15 m → λ = 6 m'),
 A('Frekansı hesapla','Frekans, birim zamandaki titreşim sayısıdır.','f = 12 ÷ 4 = 3 Hz'),
 A('Dalga hızını yaz','Hız, dalga boyu ile frekansın çarpımıdır.','v = λ × f'),A('Sonuç','Değerler yerine konur.','v = 6 × 3 = 18 m/s')],
 dogru=18,yan=[(2,'Hızı dalga boyunun frekansa oranı olarak hesaplamış: 6 ÷ 3 = 2 m/s.','islem'),(12,'Kaynağın titreşim sayısını (12) hız sanmış.','dikkat'),(15,'Şekilde 3 dalga olduğunu düşünüp λ = 5 m almış: 5 × 3 = 15 m/s.','dikkat'),(45,'S–P uzaklığının tamamını (15 m) dalga boyu sanmış: 15 × 3 = 45 m/s.','dikkat')],
 tipId='fz-dl2-ip-dalga',tip='Dalga boyu sayımı ve dalga hızı',z='orta',alt='Dalga Kavramları',kaz='Şekildeki dalgadan dalga boyunu bulup frekansla birleştirerek dalga hızını hesaplar.',
 kart='K-FZDL2-04 (ip dalgası, 2,5 dalga) · S–P = 15 m, 12 titreşim / 4 s',kalip='şekilli',
 metin='Gergin bir ipin bir ucundaki S kaynağı, sabit frekansla yukarı–aşağı titreştirilerek ip boyunca enine dalgalar oluşturuyor. Şekilde, ipin S kaynağından P noktasına kadar olan kısmındaki dalga görünüşü, kaynak titreşmeye başladıktan bir süre sonra çizilmiştir. S kaynağı 4 saniyede 12 tam titreşim yapmaktadır.\nBuna göre ipte yayılan dalganın hızı kaç m/s’dir?',
 istenen='İpteki dalganın yayılma hızı (m/s).',
 ip=['Şekilde S ile P arasında kaç dalga boyu bulunduğunu, tepe ve çukurları sayarak belirle.'],
 bilgi=[DAL],
 puf='Şekilden dalga sayısını doğru oku (yarım dalgaları da say); önce λ, sonra f bulunur ve v = λ × f uygulanır.',sekil=SK)

# ================================================================== 05 · ince–kalın yay · orta · öncüllü · C
fo=[]
fo.append(f'\\draw[thin] (0,0) -- (3,0); \\draw[ultra thick] (3,0) -- (6.2,0); \\fill (3,0) circle (1.6pt);')
pb=[(x,bump(x,1.4,.9,.6)) for x in [.5+i*.045 for i in range(41)]]
fo.append(poly(pb,'thin,vurgu,line width=1.1pt'))
fo.append(f'\\draw[vurgu,thick,-{{{STL}}}] (1.05,.95) -- (1.85,.95);')
fo.append(nd((1.5,-.5),'K yayı (ince)')); fo.append(nd((4.6,-.5),'L yayı (kalın)'))
SK=tikz_svg(HEAD+'\n'.join(x for x in fo if x)+TAIL)
qo('0005',[A('Yansıyan atmayı incele','Atma, daha ağır (kalın) yayın başlangıcında sabit uca benzer bir engelle karşılaşır; yansıyan atma ters dönerek çukur olur.','yansıyan atma çukur → I. doğru'),
 A('İletilen atmayı incele','İletilen atma, gelen atmayla aynı yönlüdür (tepe olarak devam eder).','iletilen atma tepe → II. yanlış'),
 A('Hızı karşılaştır','Gerginlik eşit olduğundan kalın yayda dalga daha yavaş ilerler.','v_L < v_K → III. doğru'),A('Sonuç','I. ve III. yargılar doğrudur.','I ve III')],
 truth=(True,False,True),harf='C',tipId='fz-dl2-ince-kalin',tip='Atmanın ince–kalın yay geçişinde yansıması ve iletilmesi',z='orta',alt='Yay Dalgaları',kaz='Atmanın ince yaydan kalın yaya geçişinde yansıyan ve iletilen atmanın biçimini ve hızını yorumlar.',
 kart='K-FZDL2-05 (ince→kalın yay geçişi) · yansıyan ters, iletilen aynı yönlü',kalip='öncüllü',
 metin='Gerginlikleri eşit olan ince K yayı ile kalın L yayı, şekildeki gibi uç uca bağlanmıştır; yayların diğer uçları çok uzaktadır. K yayında, ek noktasına doğru ilerleyen tepe biçimli bir atma gönderiliyor. Atma ek noktasına ulaştığında bir kısmı L yayına geçerken bir kısmı K yayında geri dönmektedir.\nBuna göre,\nI. K yayında geri dönen atma çukur biçimindedir.\nII. L yayına geçen atma çukur biçimindedir.\nIII. Atmanın L yayındaki hızı, K yayındaki hızından küçüktür.\nyargılarından hangileri doğrudur?',
 neden=[('geri dönen atmanın da tepe kaldığını sanmış; kalın yaya doğru yansımada atma ters döner.','bilgi'),('iletilen atmanın da ters döndüğünü sanmış; iletilen atma gelen atmayla aynı yönlüdür.','bilgi'),('kalın yayda atmanın hızlandığını düşünmüş; kalın yayda hız azalır.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Atmanın hangi yaydan hangisine geçtiğine bak; yansıyan ve iletilen atmanın yönünü ve hızını ayrı ayrı değerlendir.'],
 bilgi=[B('Yayda atmanın hızı ve geçişi','yayda dalga hızı gerginlik arttıkça artar, yay kalınlaştıkça azalır. İnce yaydan kalın yaya geçerken yansıyan atma ters döner, iletilen atma aynı yönlü kalır. Örnek: kalın yaydan ince yaya geçişte ise yansıyan atma aynı yönlü olur')],
 puf='İnce yaydan kalın yaya geçen atmada yansıyan atma ters döner, iletilen atma aynı yönlüdür ve kalın yayda hız azalır.',sekil=SK)

# ================================================================== 06 · sabit uçtan yansıma, konum · zor · şekilli · A (metin şık)
v6=2; t6=7; x0_=4; xw=12; yol=v6*t6
assert yol==14 and yol>xw-x0_ and xw-(yol-(xw-x0_))==6 and yol-(xw-x0_)==6
assert t6-(xw-x0_)//v6==3 and yol-xw==2
sc=.5; fo=[]
fo.append(f'\\draw[thin] (0,0) -- ({xw*sc:.3f},0);')
pb=[(x*sc,bump(x,x0_,1.2,.7)) for x in [i*.05 for i in range(0,241)]]
fo.append(poly(pb,'thick,vurgu'))
fo.append(f'\\fill[gray!35] ({xw*sc:.3f},-.8) rectangle ({xw*sc+.25:.3f},.9);\\draw[thick] ({xw*sc:.3f},-.8) -- ({xw*sc:.3f},.9);')
fo.append(nd((xw*sc+.1,1.1),'sabit uç','above'))
fo.append(f'\\draw[vurgu,thick,-{{{STL}}}] ({x0_*sc-.3:.3f},1.0) -- ({x0_*sc+.35:.3f},1.0);')
fo.append(dim((x0_*sc,-.55),(xw*sc,-.55),'8 m','below'))
fo.append(f'\\draw[dotted] ({x0_*sc:.3f},-.05) -- ({x0_*sc:.3f},-.55);')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qt('0006',[A('Yolu hesapla','Atma sabit hızla ilerler; 7 s’de aldığı yol hız ile sürenin çarpımıdır.','x = v × t = 2 × 7 = 14 m'),
 A('Duvara varışı bul','Tepe noktası sabit uca 8 m uzaklıktadır; atma önce bu yolu alır.','8 m → 4 s sonra duvarda'),
 A('Yansıma sonrası yolu bul','Kalan yol, yansıyan atmanın geri yönde aldığı yoldur.','14 − 8 = 6 m'),
 A('Biçimini belirle','Sabit uçtan yansıyan atma ters döner; tepe çukura dönüşür.','sabit uçtan 6 m uzakta, çukur')],
 'Sabit uçtan 6 m uzaklıkta, çukur biçiminde',
 [('Sabit uçtan 6 m uzaklıkta, tepe biçiminde','Konumu doğru bulmuş ama atmanın sabit uçta ters döndüğünü unutmuş.','bilgi'),
  ('Sabit uçtan 3 m uzaklıkta, çukur biçiminde','Yansımadan sonra geçen süreyi (3 s) hızla çarpmadan uzaklık sanmış.','islem'),
  ('Sabit uçtan 2 m uzaklıkta, çukur biçiminde','Yansımadan sonraki 3 s’de 6 m gittiğini bulmuş ama bunu duvara uzaklık yerine duvara kalan 8 m’den çıkarmış: 8 − 6 = 2 m.','islem'),
  ('Sabit uçtan 2 m uzaklıkta, tepe biçiminde','8 − 6 = 2 m hatasını yapmış ve atmanın sabit uçta ters döndüğünü de unutmuş.','dikkat')],'A',
 z='zor',alt='Yay Dalgaları',kaz='Sabit uçtan yansıyan atmanın belli bir süre sonraki konumunu ve biçimini belirler.',
 kart='K-FZDL2-06 (sabit uç, konum ve biçim) · 8 m, 2 m/s, 7 s',kalip='şekilli',tipId='fz-dl2-sabit-uc',tip='Sabit uçtan yansıyan atmanın konumu',
 metin='Şekildeki gergin yayın sağ ucu duvara sabitlenmiştir. Yayda sağa doğru ilerleyen tepe biçimli bir atma, tepe noktası sabit uca 8 m uzaklıktayken gösterilmiştir. Atmanın yayılma hızı 2 m/s’dir ve atma yayda enerji kaybetmeden ilerlemektedir. Atmanın tepe noktası şekildeki konumdan geçtiği anda süre başlatılıyor.\nBuna göre süre başladıktan 7 s sonra atmanın tepe (çukur) noktası, sabit uca ne kadar uzaklıktadır ve atma nasıl bir biçimdedir?',
 istenen='7 s sonra atmanın uzaklığı ve biçimi.',
 ip=['Atmanın 7 s’de toplam kaç m yol aldığını bul; bu yolun ne kadarının sabit uca gelmek için, ne kadarının yansıdıktan sonra olduğunu ayır.'],
 bilgi=[B('Sabit uçtan yansıma','atma, sabit bir uca ulaşınca aynı hızla geri döner ama ters yöne çevrilir: tepe çukur, çukur tepe olur. Hızı ve genişliği değişmez. Örnek: sabit uca 3 m kala tepe biçimli bir atma, uca ulaşıp 2 m geri döndüğünde uçtan 2 m uzaklıkta çukur olarak ilerler')],
 puf='Yansımada atmanın hızı değişmez; sabit uçtan ters dönerek (tepe çukura) geri gelir, uzaklık = toplam yol − duvara kadar yol.',sekil=SK)

# ================================================================== 07 · sabit ve serbest uç · kolay · öncüllü · E (I ve III)
fo=[]
def panel(y0,etiket,serbest):
    o=[]
    o.append(f'\\draw[thin] (0,{y0}) -- (5,{y0});')
    pb_=[(x,y0+bump(x,2.2,.8,.6)) for x in [1.4+i*.04 for i in range(41)]]
    o.append(poly(pb_,'thick,vurgu'))
    o.append(f'\\draw[vurgu,thick,-{{{STL}}}] (1.8,{y0+.95}) -- (2.6,{y0+.95});')
    if not serbest:
        o.append(f'\\fill[gray!35] (5,{y0-.8}) rectangle (5.25,{y0+.8});\\draw[thick] (5,{y0-.8}) -- (5,{y0+.8});')
    else:
        o.append(f'\\draw[thick] (5,{y0-.8}) -- (5,{y0+.8});\\draw[thick,fill=white] (5,{y0}) circle (.1);')
    o.append(nd((-.4,y0),etiket,'left',',font=\\normalsize\\bfseries'))
    return o
fo+=panel(2.1,'K',False); fo+=panel(0,'L',True)
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0007',[A('K yayında yansımayı incele','K yayının ucu duvara sabitlenmiştir; sabit uçtan yansıyan atma ters döner, tepe çukur olur.','K’de yansıyan atma çukur → I. doğru'),
 A('L yayında yansımayı incele','L yayının ucu halka ile serbestçe hareket edebilir; serbest uçtan yansıyan atma ters dönmez, tepe olarak geri gelir.','L’de yansıyan atma tepe → II. yanlış'),
 A('Hızı karşılaştır','Yansıma aynı yayda ve aynı gerginlikte olduğundan atmanın hızı değişmez.','v yansıyan = v gelen → III. doğru'),A('Sonuç','I. ve III. yargılar doğrudur.','I ve III')],
 truth=(True,False,True),harf='E',tipId='fz-dl2-uc-yansima',tip='Sabit ve serbest uçtan yansıma',z='kolay',alt='Yay Dalgaları',kaz='Sabit ve serbest uçtan yansıyan atmanın biçimini ve hızını karşılaştırır.',
 kart='K-FZDL2-07 (sabit ve serbest uç) · iki özdeş yay, biri duvarda biri halkada',kalip='öncüllü',
 metin='Özdeş ve eşit gerginlikteki iki yaydan K’nin sağ ucu duvara sabitlenmiş, L’nin sağ ucu ise sürtünmesiz bir düşey çubuk üzerinde serbestçe kayabilen hafif bir halkaya bağlanmıştır. İki yayda da şekildeki gibi tepe biçimli birer atma sağ uca doğru gönderiliyor. Atmalar uçlara ulaştıktan sonra yansıyor.\nBuna göre,\nI. K yayında yansıyan atma çukur biçimindedir.\nII. L yayında yansıyan atma çukur biçimindedir.\nIII. İki yayda da yansıyan atmanın hızı, gelen atmanın hızına eşittir.\nyargılarından hangileri doğrudur?',
 neden=[('sabit uçtan yansıyan atmanın da aynı yönlü kalacağını sanmış; sabit uçta atma ters döner.','bilgi'),('serbest uçtan yansımada da atmanın ters döneceğini sanmış; serbest uçtan yansıyan atma aynı yönlü kalır.','bilgi'),('yansımada atmanın hız değiştirdiğini düşünmüş; aynı yayda hız sabit kalır.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Her yaydaki ucun hareket edip edemediğine bak ve yansıyan atmanın hangi yönde döneceğini buna göre düşün.'],
 bilgi=[B('Uç koşulları ve yansıma','sabit uçtan yansıyan atma ters döner (tepe çukur olur); serbest uçtan yansıyan atma aynı yönlü kalır (tepe tepe olarak döner). Her iki durumda da atmanın hızı, yayın gerginliği değişmediğinden aynıdır. Örnek: halkaya ulaşan çukur biçimli atma, çukur olarak geri döner')],
 puf='Sabit uç atmayı ters çevirir, serbest uç çevirmez; yansımada hız (aynı yayda) değişmez.',sekil=SK)

# ================================================================== 08 · süperpozisyon · zor · şekilli · A (metin şık)
cT,cC=3,9; hT,hC=3,-2; vv=1; assert (cC-cT)/(2*vv)==3
def tri(x,c,h): return h*max(0,1-abs(x-c))
def top(x,t): return tri(x,cT+vv*t,hT)+tri(x,cC-vv*t,hC)
assert top(6,3)==hT+hC==1 and top(6,0)==0 and abs(hT)+abs(hC)==5
sq=.45; fo=[]
for xv in range(0,13): fo.append(f'\\draw[gray!45,thin] ({xv*sq:.3f},{-3.5*sq:.3f}) -- ({xv*sq:.3f},{3.5*sq:.3f});')
for yv in range(-3,4): fo.append(f'\\draw[gray!45,thin] (0,{yv*sq:.3f}) -- ({12*sq:.3f},{yv*sq:.3f});')
fo.append(f'\\draw[thick] (0,0) -- ({12*sq:.3f},0);')
fo.append(poly([(0,0),(2*sq,0),(3*sq,3*sq),(4*sq,0),(8*sq,0),(9*sq,-2*sq),(10*sq,0),(12*sq,0)],'very thick,vurgu'))
fo.append(f'\\draw[thick,-{{{STL}}}] ({2.2*sq:.3f},{3.45*sq:.3f}) -- ({3.9*sq:.3f},{3.45*sq:.3f});')
fo.append(f'\\draw[thick,-{{{STL}}}] ({9.9*sq:.3f},{-2.9*sq:.3f}) -- ({8.2*sq:.3f},{-2.9*sq:.3f});')
fo.append(nd((-.1,3*sq),'$3$','left')); fo.append(nd((-.1,-2*sq),'$-2$','left')); fo.append(nd((-.1,0),'$0$','left'))
for xv in (0,3,6,9,12): fo.append(nd((xv*sq,-3.5*sq),f'${xv}$','below'))
fo.append(nd((12*sq+.55,-3.5*sq),'$x$ (m)','below right')); fo.append(nd((-.1,3.5*sq+.05),'$y$ (cm)','above left'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qt('0008',[A('Atmaların hareketini incele','Atmalar zıt yönde 1 m/s hızla ilerler; merkezleri x = 3 m ve x = 9 m’dedir.','başlangıç mesafesi = 6 m'),
 A('Üst üste binme anını bul','Göreli hız 2 m/s olduğundan merkezler 6 m’yi birlikte kapatır.','t = 6 ÷ (1 + 1) = 3 s'),
 A('Yer değiştirmeleri topla','Tepe (+3 cm) ile çukur (−2 cm) cebirsel toplanır.','y = +3 + (−2) = +1 cm'),
 A('Sonucu yorumla','Toplam pozitif olduğundan o anda orta noktada 1 cm yüksekliğinde bir tepe görülür.','3 s sonra, 1 cm’lik tepe')],
 '3 s sonra, orta noktada 1 cm yüksekliğinde tepe',
 [('3 s sonra, orta noktada 5 cm yüksekliğinde tepe','Atmaların yüksekliklerini mutlak değer olarak toplamış (3 + 2).','islem'),
  ('3 s sonra, orta noktada 1 cm derinliğinde çukur','Farkı doğru almış ama büyük genlikli atmanın tepe olduğunu atlayıp çukur demiş.','dikkat'),
  ('6 s sonra, orta noktada 1 cm yüksekliğinde tepe','Atmalardan yalnızca birinin 1 m/s ile 6 m gittiğini düşünüp göreli hızı hesaba katmamış.','dikkat'),
  ('3 s sonra, orta noktada yay tamamen doğrusal','Atmaların genliklerini eşit sanmış; tepe 3 cm, çukur 2 cm olduğundan yay düz kalmaz.','bilgi')],'A',
 z='zor',alt='Yay Dalgaları',kaz='Zıt yönde ilerleyen farklı genlikli atmaların üst üste geldiği anı ve bileşke yer değiştirmeyi bulur.',
 kart='K-FZDL2-08 (süperpozisyon, farklı genlik) · tepe 3 cm, çukur 2 cm',kalip='şekilli',tipId='fz-dl2-superpozisyon',tip='Atmaların süperpozisyonu (farklı genlik)',
 metin='Şekilde, gergin bir yay üzerinde birbirine doğru ilerleyen üçgen biçimli iki atma, başlangıç anında gösterilmiştir. Atmaların her biri 1 m/s hızla ilerlemektedir; yatay eksendeki bir kare 1 m, düşey eksendeki bir kare 1 cm’dir. Yay ideal olup atmalar karşılaşma sırasında ve sonrasında şekillerini korumaktadır.\nBuna göre atmaların merkezleri yayın orta noktasında üst üste geldiği anda, yayın orta noktasında ne zaman ve nasıl bir görüntü oluşur?',
 istenen='Merkezlerin üst üste geldiği an ve oluşan görüntü.',
 ip=['Atmaların merkezlerinin birbirine yaklaşma hızını ve karşılaşan atmaların yer değiştirmelerinin nasıl birleştiğini düşün.'],
 bilgi=[B('Atmaların üst üste binmesi','karşılaşan atmaların yer değiştirmeleri işaretiyle birlikte toplanır (tepe +, çukur −); atmalar geçtikten sonra eski biçimleriyle yollarına devam eder. Örnek: +4 cm’lik tepe ile −1 cm’lik çukur üst üste gelince o noktada +3 cm’lik tepe oluşur')],
 puf='Üst üste binmede yer değiştirmeler işaretiyle toplanır; zıt yönlü atmaların karşılaşma süresi = aradaki uzaklık ÷ hızlar toplamı.',sekil=SK)

# ================================================================== 09 · derin–sığ kırılma · orta · öncüllü · B
lam1,lam2=1.0,.6; th1=radians(45); kx=sin(th1)/lam1; ky1=cos(th1)/lam1; ky2=sqrt(1/lam2**2-kx**2)
assert abs(sqrt(kx**2+ky1**2)-1/lam1)<1e-9 and abs(sqrt(kx**2+ky2**2)-1/lam2)<1e-9 and ky2/ky1>1
assert lam2<lam1
X0,X1=0.0,6.5; Y1=2.4; Y2=-2.4
def clip_front(n,ky,ylo,yhi):
    """kx·x − ky·y = n doğrusunun [X0,X1]×[ylo,yhi] içindeki parçası"""
    xs=lambda y:(n+ky*y)/kx
    ya=(kx*X0-n)/ky; yb=(kx*X1-n)/ky
    lo=max(ylo,min(ya,yb)); hi=min(yhi,max(ya,yb))
    if hi-lo<1e-6: return None
    return (xs(lo),lo),(xs(hi),hi)
fo=[]
fo.append(f'\\draw[thick,dashed] ({X0},0) -- ({X1},0);')
for n in range(-6,9):
    s_=clip_front(n,ky1,0,Y1)
    if s_: fo.append(seg(s_[0],s_[1],'vurgu,thick'))
    s_=clip_front(n,ky2,Y2,0)
    if s_: fo.append(seg(s_[0],s_[1],'vurgu,thick'))
fo.append(nd((X1+.15,Y1-.5),'K','right',',font=\\normalsize\\bfseries')); fo.append(nd((X1+.15,Y2+.5),'L','right',',font=\\normalsize\\bfseries'))
fo.append(f'\\draw[thick,-{{{STL}}}] (0.9,{Y1+.3}) -- ({0.9+.9*sin(th1):.3f},{Y1+.3-.9*cos(th1):.3f});')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0009',[A('Frekansı karşılaştır','Dalga bir bölgeden diğerine geçerken frekansı kaynak belirler; frekans değişmez.','f_K = f_L → I. doğru'),
 A('Dalga boyunu şekilden oku','Ardışık cepheler arası uzaklık dalga boyudur; L bölgesinde cepheler birbirine daha yakındır, yani λ_L < λ_K.','λ_L < λ_K → III. yanlış'),
 A('Derinliği yorumla','Frekans sabit olduğundan hız dalga boyuyla orantılıdır: v = λ × f. L’de hız küçüktür; hızı küçük olan bölge daha sığdır.','v_L < v_K → L daha sığ → II. doğru'),
 A('Sonuç','I. ve II. yargılar doğrudur.','I ve II')],
 truth=(True,True,False),harf='B',tipId='fz-dl2-su-kirilma',tip='Derin–sığ geçişte su dalgasının kırılması',z='orta',alt='Su Dalgaları',kaz='Su dalgasının derinliği farklı iki bölge arasındaki geçişini frekans, hız ve dalga boyu açısından yorumlar.',
 kart='K-FZDL2-09 (derin–sığ geçişte kırılma) · cepheler şekilde, derinlik bilgisi şekilden',kalip='öncüllü',
 metin='Dalga leğeninde derinlikleri farklı K ve L bölgeleri, şekilde kesikli çizgiyle gösterilen sınırla ayrılmıştır. Üreteç, sabit frekansla K bölgesine düzlem su dalgaları gönderiyor ve dalgalar sınırı eğik olarak geçerek L bölgesine ilerliyor. Şekilde dalga tepelerini temsil eden dalga cepheleri aynı andaki konumlarıyla çizilmiştir. Bölgelerden hangisinin daha sığ olduğu şekilden çıkarılacaktır.\nBuna göre,\nI. Dalgaların frekansı K ve L bölgelerinde aynıdır.\nII. L bölgesi, K bölgesinden daha sığdır.\nIII. Dalgaların dalga boyu L bölgesinde, K bölgesindekinden büyüktür.\nyargılarından hangileri doğrudur?',
 neden=[('geçişte frekansın da değiştiğini sanmış; frekansı kaynak belirler ve sabit kalır.','bilgi'),('dalga boyu küçük olan bölgeyi derin sanmış; küçük dalga boyu, küçük hız yani sığ bölge demektir.','bilgi'),('sığ bölgede dalga boyunun arttığını düşünmüş; sığ bölgede dalga boyu azalır.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Dalga cepheleri arasındaki uzaklığı iki bölgede karşılaştır ve geçişte hangi büyüklüğün sabit kaldığını düşün.'],
 bilgi=[B('Derin–sığ geçişi','su dalgası derin bölgeden sığ bölgeye geçerken frekansı değişmez; hızı ve dalga boyu azalır (v = λ × f). Sığ bölgede dalga cepheleri birbirine yaklaşır ve ilerleme yönü, sınıra dik doğrultuya (normale) yaklaşacak biçimde kırılır. Örnek: dalga cepheleri arası daralan bölge daha sığdır')],
 puf='Dalga boyu küçük olan bölgede hız küçüktür ve bölge daha sığdır; geçişte yalnız frekans sabit kalır.',sekil=SK)

# ================================================================== 10 · doğrusal dalga yansıması · kolay · şekilli · C
thi=radians(35)
def dirv(a): return (sin(radians(a)),cos(radians(a)))
angl={'K':-58,'L':55,'M':35,'N':78,'P':15}
assert angl['M']==35 and len(set(angl.values()))==5
fo=[]
fo.append(f'\\fill[gray!35] (-3.2,-.3) rectangle (3.2,0);\\draw[thick] (-3.2,0) -- (3.2,0);')
fo.append(f'\\draw[dashed,gray] (0,0) -- (0,3.3);'+nd((0,3.3),'normal','above',',gray')+f'\\draw (0,1.3) arc[start angle=90,end angle=125,radius=1.3];'+nd((-.45,1.75),'$35^\\circ$'))
src=(-3.0*sin(thi),3.0*cos(thi)); fo.append(ray(src,(0,0),'vurgu','very thick',.7))
fo.append(nd((0,0),'O','below',',yshift=-4pt'))
for d_ in (1.2,2.0,2.8):
    c=(-d_*sin(thi),d_*cos(thi)); tgt=(cos(thi),sin(thi)); fo.append(seg(add(c,mul(tgt,-.75)),add(c,mul(tgt,.75)),'gray!70,thick'))
for k_,a_ in angl.items():
    e=mul(dirv(a_),2.7); fo.append(f'\\draw[thick,-{{{STL}}}] (0,0) -- {pt(e)};')
    fo.append(nd(mul(dirv(a_),3.0),f'\\textbf{{{k_}}}'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qt('0010',[A('Gelme açısını bul','Gelme açısı, gelen dalganın yönü ile yüzeye çizilen normal arasındaki açıdır; şekilde 35°’dir.','i = 35°'),
 A('Yansıma yasasını uygula','Yansıma açısı gelme açısına eşittir ve yansıyan dalga normalin öbür yanındadır.','r = i = 35°'),
 A('Oku seç','Normalin gelen dalgaya göre karşı yanında, normalle 35° yapan ok bulunur.','M ok yönü')],
 'M',[('K','Yansıyan dalganın gelen dalgayla aynı yanda, normale daha yatık gideceğini sanmış; yansımada dalga normalin öbür yanına geçer.','bilgi'),
  ('L','Açıyı normale göre değil yüzeye göre almış; yüzeyle 35° yapan (normalle 55°) oku seçmiş.','dikkat'),
  ('N','Yansıyan dalganın yüzeye yakın, yatık bir doğrultuda gideceğini sanmış.','bilgi'),('P','Yansıma açısını gelme açısından küçük sanmış.','bilgi')],'C',
 tipId='fz-dl2-su-dogrusal',tip='Doğrusal dalganın yansıması',z='kolay',alt='Su Dalgaları',kaz='Doğrusal su dalgasının düz engelden yansımasında yönü yansıma yasasıyla belirler.',
 kart='K-FZDL2-10 (doğrusal dalga yansıması) · beş seçenek ok, 35°',kalip='şekilli',
 metin='Dalga leğeninde, düz ve katı bir engele doğru ilerleyen doğrusal su dalgalarının yönü ve birkaç dalga cephesi şekilde gösterilmiştir. Engelin yüzeyine O noktasında normal çizilmiştir. Engele çarpan dalgaların yansıdıktan sonra ilerleyebileceği yönleri gösteren K, L, M, N ve P okları O noktasından çizilmiştir. Yansıma sırasında dalga boyu değişmemektedir.\nBuna göre yansıyan dalgaların ilerleme yönünü hangi ok gösterir?',
 istenen='Yansıyan dalganın yönünü gösteren ok.',
 ip=['Gelen dalganın normalle yaptığı açıyı bul ve yansımada bu açının nasıl değiştiğini düşün.'],
 bilgi=[B('Dalgaların yansıması','düz bir engelden yansımada yansıma açısı, gelme açısına eşittir; açılar yüzeye değil normale göre ölçülür ve gelen ile yansıyan dalga normalin zıt yanlarındadır. Dalga boyu, hız ve frekans değişmez. Örnek: normalle 50° yapan dalga, normalin öbür yanında 50° ile yansır')],
 puf='Yansımada açılar normale göre ölçülür; yansıma açısı = gelme açısı ve yansıyan dalga normalin öbür yanındadır.',sekil=SK)

# ================================================================== 11 · dairesel dalga yansıması · orta · şekilli · D
dS=1.5; Rr=[.8,2.0,3.0]
fo=[]
fo.append(f'\\fill[gray!35] (-3.4,-.25) rectangle (3.4,0);\\draw[thick] (-3.4,0) -- (3.4,0);')
fo.append(f'\\fill (0,{dS}) circle (2pt);'+nd((0,dS),'S','above',',yshift=1pt')+dim((-.6,0),(-.6,dS),'$d$','left'))
for R in Rr:
    if R<dS: fo.append(f'\\draw[vurgu,thick] (0,{dS}) circle ({R});')
    else:
        a0=degrees(asin(dS/R)); fo.append(f'\\draw[vurgu,thick] ({R*cos(radians(-a0)):.3f},{dS+R*sin(radians(-a0)):.3f}) arc[start angle={-a0:.2f},end angle={180+a0:.2f},radius={R}];')
        fo.append(f'\\draw[vurgu,thick,dashed] ({R*cos(radians(a0)):.3f},{-dS+R*sin(radians(a0)):.3f}) arc[start angle={a0:.2f},end angle={180-a0:.2f},radius={R}];')
cand={'K':-.0,'L':-dS/3,'M':-2*dS/3,'N':-dS,'P':-1.5*dS}
assert cand['N']==-dS and len(set(cand.values()))==5
for k_,y_ in cand.items():
    fo.append(f'\\fill (0,{y_}) circle (1.8pt);'+nd((.12,y_-.02),f'\\textbf{{{k_}}}','right'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qt('0011',[A('Yansıma yasasını hatırla','Yansıyan dalgalar, engele göre kaynağın ayna görüntüsü olan noktadan yayılıyormuş gibi davranır.','görüntü noktası S′'),
 A('Görüntü konumunu bul','S, engelin d kadar üstündedir; ayna görüntüsü engelin d kadar altında, S ile aynı düşey doğru üzerindedir.','S′: engelden d aşağıda'),
 A('Noktayı seç','Şekilde engelden d kadar aşağıda bulunan nokta N’dir.','N')],
 'N',[('K','Yansıyan dalgaların engel yüzeyindeki bir noktadan yayıldığını sanmış.','bilgi'),('L','Görüntü uzaklığını kaynağın uzaklığının üçte biri (d ÷ 3) sanmış.','bilgi'),('M','Görüntü uzaklığını kaynağın uzaklığının üçte ikisi (2d ÷ 3) almış.','dikkat'),('P','Görüntünün kaynaktan daha uzakta (1,5d) olduğunu düşünmüş.','bilgi')],'D',
 tipId='fz-dl2-su-dairesel',tip='Dairesel dalganın düz engelden yansıması',z='orta',alt='Su Dalgaları',kaz='Dairesel su dalgasının düz engelden yansımasında yansıyan dalgaların hangi noktadan yayılıyormuş gibi davrandığını belirler.',
 kart='K-FZDL2-11 (dairesel dalga yansıması) · kaynak engelden d, aday noktalar',kalip='şekilli',
 metin='Dalga leğeninde S noktasındaki küçük bir titreştirici, düz ve katı bir engelin önünde dairesel su dalgaları oluşturuyor. Dalga cephelerinden bazıları, engele çarpmadan önceki hâlleriyle (düz çizgi) ve yansıdıktan sonraki hâlleriyle (kesikli çizgi) şekilde gösterilmiştir. S ile engel arasındaki uzaklık d’dir; engelin arkasındaki noktalar, S’den geçen düşey doğru üzerinde işaretlenmiştir.\nBuna göre yansıyan dalgalar, işaretli noktalardan hangisinden yayılıyormuş gibi davranır?',
 istenen='Yansıyan dalgaların sanki çıktığı nokta.',
 ip=['Yansıyan dalga cephelerinin merkezini bulmak için kesikli yayların hangi noktaya ait çember parçaları olduğunu düşün.'],
 bilgi=[B('Dairesel dalganın yansıması','düz engelden yansıyan dairesel dalgalar, kaynağın engele göre simetriği (ayna görüntüsü) olan noktadan yayılıyormuş gibi ilerler; bu nokta kaynakla aynı uzaklıktadır ve engelin diğer yanındadır. Örnek: engelden 2 m önceki kaynağın görüntüsü engelden 2 m ötededir')],
 puf='Yansıyan dairesel dalgalar, kaynağın engele göre ayna görüntüsünden yayılıyormuş gibidir.',sekil=SK)

# ================================================================== 12 · tablo · derinlik–hız–dalga boyu · orta · öncüllü · E (II ve III)
lamK,lamL,lamM=4,6,3; f12=5
vK,vL,vM=lamK*f12,lamL*f12,lamM*f12; assert (vK,vL,vM)==(20,30,15)
assert vM<vK<vL and Fr(vL,vK)==Fr(3,2)
SK=tablo_svg(['Bölge','Dalga boyu (cm)'],[['K',str(lamK)],['L',str(lamL)],['M',str(lamM)]])
qo('0012',[A('Hızları hesapla','Frekans sabittir (5 Hz); her bölgede v = λ × f yazılır.','v_K = 4 × 5 = 20 · v_L = 6 × 5 = 30 · v_M = 3 × 5 = 15 cm/s'),
 A('En büyük hızı bul','Hızı en büyük olan bölge, dalga boyu en büyük olan L’dir; M’de hız en küçüktür.','en hızlı L → I. yanlış'),
 A('Derinliği yorumla','Hız küçüldükçe bölge sığlaşır; hızı en küçük olan M en sığ bölgedir.','M en sığ → II. doğru'),
 A('Oranı kontrol et','L ile K’nin hız oranı dalga boylarının oranına eşittir.','30 ÷ 20 = 1,5 → III. doğru')],
 truth=(False,True,True),harf='E',tipId='fz-dl2-su-tablo',tip='Derinlik, hız ve dalga boyu ilişkisi (tablo)',z='orta',alt='Su Dalgaları',kaz='Dalga leğeninde farklı derinlikli bölgelerdeki dalga boylarından hız ve derinlik karşılaştırması yapar.',
 kart='K-FZDL2-12 (derinlik–hız–dalga boyu tablosu) · üç bölge, f = 5 Hz',kalip='tablo',
 metin='Dalga leğeninde derinlikleri birbirinden farklı K, L ve M bölgeleri vardır. Kaynak, her bölgede ayrı ayrı olmak üzere 5 Hz’lik sabit frekansla dalga üretmiştir. Üç bölgede ölçülen dalga boyları aşağıdaki tabloda verilmiştir.\nBuna göre,\nI. Dalga hızı en büyük olan bölge M’dir.\nII. En sığ bölge M’dir.\nIII. L bölgesindeki dalga hızı, K bölgesindekinin 1,5 katıdır.\nyargılarından hangileri doğrudur?',
 neden=[('dalga boyu en küçük olanın hızının en büyük olacağını sanmış; hız dalga boyuyla doğru orantılıdır.','bilgi'),('en büyük dalga boyunu en sığ bölge sanmış; sığ bölgede dalga boyu ve hız küçüktür.','bilgi'),('hız oranını bulamamış; hızlar dalga boylarıyla orantılı olduğundan oran 6 ÷ 4 = 1,5’tir.','islem')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Frekans aynı olduğuna göre hızların dalga boylarıyla nasıl değiştiğini ve hızın derinlikle ilişkisini düşün.'],
 bilgi=[DAL,B('Derinlik ve hız','su dalgasının hızı, suyun derinliği arttıkça artar. Sabit frekansta dalga boyu da hızla doğru orantılı değişir. Örnek: daha derin bölgede dalga boyu daha büyüktür')],
 puf='Frekans aynıysa dalga boyu hızla orantılıdır; dalga boyu küçük olan bölge daha sığdır.',sekil=SK)

# ================================================================== 13 · osiloskop · orta · grafik/öncüllü · A (Yalnız I)
sq=.4; fo=[]
def osk(y0,amp,per,et):
    o=[]
    o.append(f'\\draw[thick] (0,{y0-2.5*sq:.3f}) rectangle ({8*sq:.3f},{y0+2.5*sq:.3f});')
    for i in range(1,8): o.append(f'\\draw[gray!45,thin] ({i*sq:.3f},{y0-2.5*sq:.3f}) -- ({i*sq:.3f},{y0+2.5*sq:.3f});')
    for j in range(-2,3): o.append(f'\\draw[gray!45,thin] (0,{y0+j*sq:.3f}) -- ({8*sq:.3f},{y0+j*sq:.3f});')
    o.append(poly([(t*sq,y0+amp*sq*sin(2*pi*t/per)) for t in [i*.05 for i in range(161)]],'very thick,vurgu'))
    o.append(nd((-.1,y0),et,'left',',font=\\normalsize\\bfseries'))
    return o
perK,perL,perM=4,2,4; ampK,ampL,ampM=1,1,2
assert 8/perL>8/perK and perM==perK and ampM>ampK
for y0,a_,p_,e_ in ((4.9,ampK,perK,'K'),(2.45,ampL,perL,'L'),(0,ampM,perM,'M')): fo+=osk(y0,a_,p_,e_)
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0013',[A('K ile L’yi karşılaştır','Aynı sürede L’nin ekranında K’dekinden daha çok tam dalga vardır; frekansı büyüktür. Genlikleri eşittir. Frekansı büyük ses daha incedir.','f_L > f_K → L daha ince → I. doğru'),
 A('K ile M’yi karşılaştır','M’nin ekranında K ile aynı sayıda tam dalga vardır; frekansları eşittir. Yükseklikleri (incelik–kalınlık) aynıdır.','f_M = f_K → II. yanlış'),
 A('Şiddeti yorumla','Şiddeti genlik belirler; M’nin genliği K’nin iki katıdır, yani M’nin sesi daha şiddetlidir.','A_M > A_K → III. yanlış'),A('Sonuç','Yalnız I. yargı doğrudur.','Yalnız I')],
 truth=(True,False,False),harf='A',tipId='fz-dl2-ses-osiloskop',tip='Sesin yüksekliği ve şiddeti (osiloskop)',z='orta',alt='Ses Dalgaları',kaz='Osiloskop görüntüsünden sesin frekansını ve genliğini karşılaştırarak yükseklik ve şiddeti yorumlar.',
 kart='K-FZDL2-13 (osiloskop, yükseklik–şiddet) · K, L, M',kalip='grafik',
 metin='Bir mikrofona bağlı osiloskopta, K, L ve M ses kaynaklarının oluşturduğu ses dalgaları aynı zaman ve aynı gerilim ayarlarıyla sırayla gözlenmiş ve ekran görüntüleri şekildeki gibi elde edilmiştir. Ekrandaki kareler her üç görüntüde de aynı boyuttadır ve sesler aynı ortamda yayılmaktadır.\nBuna göre,\nI. L sesi, K sesinden daha incedir.\nII. M sesi, K sesinden daha incedir.\nIII. M sesinin şiddeti, K sesinin şiddetinden küçüktür.\nyargılarından hangileri doğrudur?',
 neden=[('sıklığı daha büyük olan dalgayı daha kalın ses saymış; frekans arttıkça ses incelir.','bilgi'),('genliği büyük olan sesi daha ince sanmış; incelik frekansa, şiddet genliğe bağlıdır.','bilgi'),('genliği büyük olan sesin şiddetinin daha küçük olduğunu düşünmüş; şiddet genlikle birlikte artar.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Ekranda aynı sürede kaç tam dalga oluştuğuna ve dalgaların yüksekliğine ayrı ayrı bakarak hangisinin frekansı, hangisinin genliği temsil ettiğini düşün.'],
 bilgi=[B('Sesin özellikleri','sesin yüksekliği (ince–kalın) frekansa bağlıdır; frekans büyük olan ses incedir. Sesin şiddeti (güçlü–zayıf) genliğe bağlıdır; genlik büyük olan ses daha şiddetlidir. Osiloskopta aynı sürede sığan dalga sayısı frekansı, dalga yüksekliği genliği gösterir')],
 puf='Frekans (aynı sürede sığan dalga sayısı) sesin inceliğini, genlik şiddetini belirler.',sekil=SK)

# ================================================================== 14 · yankı, iki duvar · zor · şekilli · C (sayısal)
v14=340; t1,t2=2,5; d1=Fr(v14*t1,2); d2=Fr(v14*t2,2); dT=d1+d2
assert (d1,d2,dT)==(340,850,1190) and v14*(t2-t1)//2==510 and v14*t1==680 and v14*t2==1700 and v14*(t1+t2)==2380
fo=[]
fo.append('\\draw[thick] (-.4,0) -- (7.4,0);')
for x_,n_ in ((0,'K'),(7,'L')):
    s_=1 if x_==0 else -1
    fo.append(f'\\fill[gray!35] ({x_ if s_>0 else x_-.35},0) rectangle ({x_+.35 if s_>0 else x_},2.2);\\draw[thick] ({x_},0) -- ({x_},2.2);')
    fo.append(nd((x_+(.1 if s_>0 else -.1),2.2),n_,'above',',font=\\normalsize\\bfseries'))
xo=2.0
fo.append(f'\\draw[thick] ({xo},.1) -- ({xo},.65);\\draw[thick,fill=white] ({xo},.8) circle (.15);')
fo.append(nd((xo,0),'O','below'))
fo.append(f'\\draw[dotted] ({xo},.95) -- ({xo},1.5);'+f'\\draw[vurgu,thick,<->] ({xo},1.5) -- (.08,1.5);'+nd((1.05,1.5),'yankı 2 s sonra','above',',font=\\footnotesize'))
fo.append(f'\\draw[vurgu,thick,<->] ({xo},1.05) -- (6.92,1.05);'+nd((4.5,1.05),'yankı 5 s sonra','above',',font=\\footnotesize'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0014',[A('Gidiş–dönüş yolu düşün','Yankıda ses, kayalığa gidip geri döner; toplam yol kayalığa olan uzaklığın iki katıdır.','x = 2 × d'),
 A('K kayalığına uzaklık','2 s’lik sürede ses 340 m/s hızla yol alır, bu yolun yarısı K’ye olan uzaklıktır.','d₁ = 340 × 2 ÷ 2 = 340 m'),
 A('L kayalığına uzaklık','5 s’lik süre için aynı işlem yapılır.','d₂ = 340 × 5 ÷ 2 = 850 m'),
 A('İki kayalık arası','Kişi iki kayalığın arasında olduğundan uzaklıklar toplanır.','d₁ + d₂ = 340 + 850 = 1190 m')],
 dogru=1190,yan=[(510,'Yankı süreleri farkını (3 s) alıp ses hızıyla çarparak yarıya bölmüş: 340 × 3 ÷ 2.','dikkat'),(680,'Yalnız yakın kayalığa gidiş–dönüş yolunu (340 × 2) hesaplamış.','dikkat'),
 (1700,'Uzak kayalığın yankı süresini hızla çarpmış (340 × 5); yarıya bölmeyi unutmuş.','islem'),(2380,'İki yankı süresini toplayıp hızla çarpmış (340 × 7); gidiş–dönüşü hesaba katmamış.','islem')],
 tipId='fz-dl2-yanki',tip='Yankı ve uzaklık',z='orta',alt='Ses Dalgaları',kaz='İki kayalıktan gelen yankı sürelerinden kayalıklar arasındaki uzaklığı hesaplar.',
 kart='K-FZDL2-14 (iki duvardan yankı) · 2 s ve 5 s, v = 340 m/s',kalip='şekilli',
 metin='Dik yamaçlı bir vadide, K ve L kayalıkları arasında, bu kayalıkları birleştiren doğru üzerinde duran bir kişi, bir el çırpma sesi çıkarıyor. Kişi sesin K ve L kayalıklarından yansıyan yankılarını, ses çıktıktan sonra şekilde gösterilen sürelerde duyuyor. Sesin havadaki hızı 340 m/s’dir ve kayalıklar arasındaki hava sakindir.\nBuna göre K ve L kayalıkları arasındaki uzaklık kaç metredir?',
 istenen='K ile L kayalıkları arasındaki uzaklık (m).',
 ip=['Her yankının, sesin kayalığa gidip geri dönmesiyle oluştuğunu ve kişinin iki kayalığın arasında bulunduğunu düşünerek uzaklıkları ayrı ayrı bul.'],
 bilgi=[B('Yankı','ses bir engele çarpıp yansıyarak geri döndüğünde yankı duyulur. Yankı süresinde ses, engele gidip geri gelir; yani yol = hız × süre ve engele uzaklık bu yolun yarısıdır. Örnek: hızı 300 m/s olan bir ses 1 s sonra yankı veriyorsa engel 150 m uzaktadır')],
 puf='Yankıda gidilen yol uzaklığın iki katıdır: d = v · t ÷ 2; iki yankıda uzaklıklar ayrı bulunup toplanır.',sekil=SK)

# ================================================================== 15 · ses hızı tablosu · orta · öncüllü · B (I ve II)
SK=tablo_svg(['Ortam','Ses hızı (m/s)'],[['Hava','340'],['Su','1500'],['Çelik','5000']])
assert 3000/1500==2 and 5000/340>1500/340
qo('0015',[A('Dalga boyunu karşılaştır','Frekans aynıysa λ = v ÷ f olduğundan dalga boyu hızla orantılıdır; ses hızı en büyük çelikte, dolayısıyla dalga boyu da en büyük çelikte olur.','v_çelik en büyük → λ_çelik en büyük → I. doğru'),
 A('Ortam değişimini incele','Ses bir ortamdan diğerine geçerken frekansı kaynak belirlediği için frekans değişmez; hız ve dalga boyu değişir.','f sabit → II. doğru'),
 A('Süreyi hesapla','Suda 3000 m yol için süre, yolun hıza bölümüdür.','t = 3000 ÷ 1500 = 2 s (1 s değil) → III. yanlış'),A('Sonuç','I. ve II. yargılar doğrudur.','I ve II')],
 truth=(True,True,False),harf='B',tipId='fz-dl2-ses-hizi',tip='Ortamlara göre ses hızı (tablo)',z='orta',alt='Ses Dalgaları',kaz='Ses dalgasının farklı ortamlardaki hız, dalga boyu ve frekans değişimini yorumlar.',
 kart='K-FZDL2-15 (ses hızı tablosu) · hava, su, çelik',kalip='tablo',
 metin='Bir fizik öğretmeni, sesin ortamlara göre yayılma hızlarını gösteren aşağıdaki tabloyu öğrencilere veriyor. Aynı ses kaynağından çıkan sabit frekanslı ses dalgasının önce havada, sonra suda, daha sonra çelik bir levhada yayıldığı düşünülmektedir. Ortamlar arasında yansıma ve enerji kaybı ihmal edilmektedir.\nBuna göre,\nI. Dalga boyu en büyük olduğu ortam çeliktir.\nII. Ses dalgası havadan suya geçerken frekansı değişmez.\nIII. Ses dalgası suda 3000 m’lik yolu 1 s’de alır.\nyargılarından hangileri doğrudur?',
 neden=[('dalga boyunun hızla ilgisini kurmamış; frekans sabitken dalga boyu hızla orantılıdır.','bilgi'),('ortam değişince frekansın da değiştiğini sanmış; frekansı kaynak belirler.','bilgi'),('yolu süreyle hızı bölerek ya da 1500 m’yi 1 s sanarak süreyi hatalı bulmuş; 3000 m için 2 s gerekir.','islem')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Frekans sabitken hızın dalga boyunu nasıl etkilediğini ve ortam değişince hangi büyüklüğün korunduğunu düşün.'],
 bilgi=[B('Ses hızı','ses katılarda en hızlı, gazlarda en yavaş yayılır. Ortam değişince frekans sabit kalır, hız ve dalga boyu değişir (λ = v ÷ f). Alınan yol = hız × süredir. Örnek: 2000 m/s hızla giden ses 4 s’de 8000 m yol alır')],
 puf='Ortam değişince frekans sabit kalır; dalga boyu hızla orantılı değişir ve hız katıda en büyüktür.',sekil=SK)

# ================================================================== 16 · rezonans · orta · şekilli/öncüllü · B (Yalnız III)
fo=[]
def fork(x,n_,hz):
    o=[]
    o.append(f'\\draw[thick,fill=gray!15] ({x-.45},0) rectangle ({x+.45},.3);')
    o.append(f'\\draw[thick] ({x},.3) -- ({x},.62);')
    o.append(f'\\draw[thick] ({x-.18},.8) -- ({x-.18},2.0);\\draw[thick] ({x+.18},.8) -- ({x+.18},2.0);')
    o.append(f'\\draw[thick] ({x-.18},.8) arc[start angle=180,end angle=360,radius=.18];')
    o.append(nd((x,2.0),n_,'above',',font=\\normalsize\\bfseries')); o.append(nd((x,0),f'{hz} Hz','below',',yshift=-3pt'))
    return o
fK,fL,fM=440,440,512; assert fK==fL!=fM
fo.append('\\draw[thick] (-.9,0) -- (5.3,0);')
for x_,n_,h_ in ((0,'K',fK),(1.6,'L',fL),(4.4,'M',fM)): fo+=fork(x_,n_,h_)
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0016',[A('Rezonans koşulunu hatırla','Titreşen bir kaynağın sesi, doğal frekansı kendi frekansına eşit olan cismi titreştirir; buna rezonans denir.','f_kaynak = f_doğal → rezonans'),
 A('L ve M’yi incele','L’nin doğal frekansı K ile aynı (440 Hz); L titreşmeye başlar → III. doğru. M’nin doğal frekansı farklı (512 Hz), M titreşmez → I. yanlış.','L titreşir, M titreşmez'),
 A('Frekansı kontrol et','Ses havada ilerlerken frekansı değişmez; frekansı kaynak belirler.','f sabit → II. yanlış'),A('Sonuç','Yalnız III. yargı doğrudur.','Yalnız III')],
 truth=(False,False,True),harf='B',tipId='fz-dl2-rezonans',tip='Rezonans (diyapazon)',z='orta',alt='Ses Dalgaları',kaz='Doğal frekansları verilen diyapazonlarda rezonansın hangisinde oluşacağını belirler.',
 kart='K-FZDL2-16 (rezonans, diyapazon) · 440 Hz çifti ve 512 Hz',kalip='şekilli',
 metin='Sessiz bir laboratuvarda aynı masanın üzerine K, L ve M diyapazonları yerleştirilmiştir. Şekilde diyapazonların altlarında doğal frekansları yazılıdır. K diyapazonuna lastik bir tokmakla vurulup titreşmesi sağlanıyor ve hemen ardından diğer diyapazonlar gözleniyor. Ortam yalnızca havadır ve diyapazonlar arasında başka bir bağlantı yoktur.\nBuna göre,\nI. M diyapazonu belirgin biçimde titreşmeye başlar.\nII. K diyapazonunun sesinin frekansı, L’ye ulaşırken azalır.\nIII. L diyapazonu titreşmeye başlar.\nyargılarından hangileri doğrudur?',
 neden=[('yakın olmayan ama farklı frekanslı M’nin de titreşeceğini sanmış; rezonans için doğal frekans eşit olmalıdır.','bilgi'),('sesin havada ilerlerken frekansının azaldığını düşünmüş; frekans değişmez.','bilgi'),('aynı frekanslı L’nin titreşmeyeceğini sanmış; doğal frekansı eşit olan cisim rezonansa girer.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Vurulan diyapazonun frekansını diğerlerinin doğal frekanslarıyla karşılaştır.'],
 bilgi=[B('Rezonans','bir kaynağın ses dalgaları, doğal frekansı kaynağın frekansına eşit olan cismi de titreştirir; buna rezonans denir. Doğal frekansı farklı olan cisimler belirgin biçimde titreşmez. Örnek: 300 Hz’lik bir diyapazonun sesiyle yalnız 300 Hz’lik diyapazon titreşir')],
 puf='Rezonans için gelen sesin frekansı cismin doğal frekansına eşit olmalıdır; frekans havada değişmez.',sekil=SK)

# ================================================================== 17 · ultrases, sonar · kolay · hikâyeli · E (sayısal)
va,vs,t17=340,1500,Fr(3,5)
D17=Fr(vs)*t17/2; assert D17==450 and Fr(va)*t17/2==Fr(102) and Fr(va)*t17==Fr(204) and Fr(vs)*t17/4==Fr(225) and Fr(va)*t17/4==Fr(51)
q('0017',[A('Ultrasesi tanı','Frekansı 20 000 Hz’in üzerindeki sese ultrases denir; sonar cihazı 40 000 Hz’lik ultrases kullanır. Sesin hızı ortama göre seçilir: denizde 1500 m/s.','v = 1500 m/s'),
 A('Gidiş–dönüş yolunu bul','0,6 s boyunca ses dibe gidip geri döner.','x = v × t = 1500 × 0,6 = 900 m'),
 A('Derinliğe geç','Yol, derinliğin iki katıdır.','h = 900 ÷ 2 = 450 m')],
 dogru=450,yan=[(51,'Havadaki hızı (340 m/s) kullanmış ve yarıya bölme işlemini iki kez uygulamış.','islem'),(102,'Suda değil havadaki hızı (340 m/s) alıp yolu ikiye bölmüş.','dikkat'),(204,'Havadaki hızı almış ve gidiş–dönüş yolunu ikiye bölmeyi unutmuş.','dikkat'),(225,'Gidiş–dönüş yolunu iki kez ikiye bölmüş.','islem')],
 tipId='fz-dl2-ultrases',tip='Ultrases ve sonar uygulaması',z='kolay',alt='Ses Dalgaları',kaz='Ultrasesin sonar uygulamasında yankı süresinden derinlik hesaplar.',
 kart='K-FZDL2-17 (ultrases, sonar) · 40 kHz, 0,6 s, suda 1500 m/s',kalip='hikâyeli',
 metin='Bir balıkçı teknesindeki sonar cihazı, deniz tabanına doğru frekansı 40 000 Hz olan ultrases dalgaları gönderiyor ve dipten yansıyıp gelen sesi algılıyor. Cihaz, ses gönderildikten 0,6 s sonra yankıyı kaydediyor. Sesin havadaki hızı 340 m/s, deniz suyundaki hızı ise 1500 m/s’dir. Deniz tabanı düzdür ve teknenin hareketi ihmal edilmektedir.\nBuna göre bu noktada deniz kaç metre derinliktedir?',
 istenen='Deniz tabanının derinliği (m).',
 ip=['Sesin hangi ortamda yayıldığına ve yankı süresi boyunca toplam kaç metre yol aldığına dikkat et.'],
 bilgi=[B('Ultrases ve sonar','frekansı 20 000 Hz’in üzerindeki seslere ultrases denir; insan kulağı duyamaz. Sonar ve ultrasonografide ultrases yansıması kullanılır. Yankıda yol, uzaklığın iki katıdır: uzaklık = v · t ÷ 2. Örnek: hızı 200 m/s olan bir ses 1 s sonra yankı veriyorsa engel 100 m uzaktadır')],
 puf='Sonarda ses yolu iki katıdır; derinlik = ortamdaki ses hızı × yankı süresi ÷ 2.')

# ================================================================== 18 · sismogram · orta · grafik/öncüllü · D (I ve II)
def sism(t,arr):
    y=.04*sin(2*pi*3.1*t)*(.6+.4*sin(2*pi*.37*t))
    for (s0,a0,f0,tau) in arr:
        if t>=s0: y+=a0*(1-math.exp(-(t-s0)*6))*math.exp(-(t-s0)/tau)*sin(2*pi*f0*(t-s0))
    return y
arr18=[(1.6,.22,2.8,6),(4.2,.5,1.7,6),(6.4,1.05,1.0,3.2)]
fo=[]
fo.append(f'\\draw[->,thick] (-.1,0) -- (6.9,0);\\draw[->,thick] (0,-1.5) -- (0,1.6);')
fo.append(nd((6.9,0),'$t$','right'));
pts_=[(t*.55,sism(t,arr18)*1.0) for t in [i*.03 for i in range(401)]]
fo.append(poly(pts_,'thick,vurgu'))
for k_,(s0,_,_,_) in enumerate(arr18,1):
    fo.append(f'\\draw[dashed,gray] ({s0*.55:.3f},-1.3) -- ({s0*.55:.3f},1.45);'+f'\\node[circle,draw,inner sep=1.2pt] at ({s0*.55:.3f},1.7) {{{k_}}};')
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0018',[A('İlk gelen dalgayı belirle','İstasyona ilk ulaşan 1 numaralı dalga, en hızlı olan P dalgasıdır; P dalgası boyunadır.','1: P dalgası (boyuna) → I. doğru'),
 A('Hızları karşılaştır','Varış sırası hız sırasını verir; 2 numaralı dalga (S dalgası) P’den sonra geldiğine göre daha yavaştır.','v_2 < v_1 → II. doğru'),
 A('Genliği incele','Kayıtta en büyük genlik, en son gelen 3 numaralı dalgaya, yani yüzey dalgasına aittir; 2 numaralı dalganın genliği daha küçüktür.','en büyük genlik: 3 → III. yanlış'),A('Sonuç','I. ve II. yargılar doğrudur.','I ve II')],
 truth=(True,True,False),harf='D',tipId='fz-dl2-sismogram',tip='Deprem dalgaları ve sismogram',z='orta',alt='Deprem Dalgaları',kaz='Sismogram kaydından P, S ve yüzey dalgalarının varış sırasını, hızını ve genliğini yorumlar.',
 kart='K-FZDL2-18 (sismogram: P, S, yüzey) · 1, 2, 3 numaralı varışlar',kalip='grafik',
 metin='Bir sismograf istasyonu, aynı depremde oluşan P, S ve yüzey dalgalarını şekildeki gibi kaydetmiştir. Kayıtta dalgaların istasyona ulaştığı anlar 1, 2 ve 3 ile işaretlenmiştir. Dalgaların hangisinin hangi tür olduğu, kayıttaki sıra ve genlik özelliklerinden çıkarılacaktır. Üç dalga da deprem merkezinden aynı anda yola çıkmıştır.\nBuna göre,\nI. 1 ile gösterilen dalga boyuna dalgadır.\nII. 2 ile gösterilen dalganın hızı, 1 ile gösterilen dalganın hızından küçüktür.\nIII. Kayıttaki en büyük genlik 2 ile gösterilen dalgaya aittir.\nyargılarından hangileri doğrudur?',
 neden=[('P dalgasını enine sanmış; P dalgası boyuna, S dalgası enine dalgadır.','bilgi'),('ilk gelen dalganın daha yavaş olduğunu düşünmüş; aynı yolu önce alan dalga daha hızlıdır.','bilgi'),('S dalgasının en büyük genlikli kayıt olduğunu sanmış; en büyük genlik yüzey dalgalarına aittir.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Dalgalar aynı anda yola çıktığına göre varış sırasının hızlarla nasıl ilişkili olduğunu ve genliği en büyük kaydın hangisi olduğunu kayıttan oku.'],
 bilgi=[B('Deprem dalgaları','P dalgası (boyuna) en hızlıdır ve ilk gelir; S dalgası (enine) ikinci gelir; yüzey dalgaları en yavaştır, en son gelir ve en büyük hasarı yapar. Aynı noktadan aynı anda çıkan dalgalardan hızlı olan önce ulaşır. Örnek: 5 km/s ile giden dalga, 3 km/s ile gidenden önce varır')],
 puf='Aynı anda çıkan dalgalardan hızlı olan önce gelir: P, sonra S, en sonda yüzey dalgaları gelir ve en büyük genlik yüzey dalgalarındadır.',sekil=SK)

# ================================================================== 19 · P–S farkı · zor · grafik · D (sayısal)
vP,vS,dt19=6,4,20
d19=Fr(dt19)/(Fr(1,vS)-Fr(1,vP)); assert d19==240 and d19/vS-d19/vP==dt19
assert dt19*vS==80 and dt19*vP==120 and dt19*(vP+vS)==200 and dt19*vP*vS==480
tP,tS=20,40; assert tS-tP==dt19
def sism2(t):
    y=.04*sin(2*pi*3.1*t)*(.6+.4*sin(2*pi*.37*t))
    for (s0,a0,f0,tau) in ((tP/10,.3,2.6,5),(tS/10,.65,1.6,5)):
        if t>=s0: y+=a0*(1-math.exp(-(t-s0)*6))*math.exp(-(t-s0)/tau)*sin(2*pi*f0*(t-s0))
    return y
fo=[]
fo.append("\\draw[->,thick] (-.1,-1.3) -- (6.7,-1.3);\\draw[->,thick] (0,-1.3) -- (0,1.5);")
fo.append(poly([(t*1.0,sism2(t)) for t in [i*.03 for i in range(201)]],'thick,vurgu'))
for k_ in range(0,7):
    fo.append(f'\\draw[thick] ({k_},-1.37) -- ({k_},-1.23);'+nd((k_,-1.37),f'{k_*10}','below',',font=\\footnotesize'))
fo.append(nd((6.7,-1.3),'$t$ (s)','right'))
for s0,n_ in ((tP/10,'P'),(tS/10,'S')):
    fo.append(f'\\draw[dashed,gray] ({s0},-1.3) -- ({s0},1.2);'+nd((s0,1.2),f'\\textbf{{{n_}}}','above'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
q('0019',[A('Varış farkını oku','Şekilde P dalgası 20. s’de, S dalgası 40. s’de kaydedilmiştir; aradaki fark verilir.','Δt = 40 − 20 = 20 s'),
 A('Süreleri yaz','Aynı d yolunu P dalgası d ÷ 6, S dalgası d ÷ 4 sürede alır; fark kayıttaki 20 s’dir.','d ÷ 4 − d ÷ 6 = 20'),
 A('Denklemi çöz','Paydaları eşitleyip d’yi bul.','3d ÷ 12 − 2d ÷ 12 = 20 → d ÷ 12 = 20'),
 A('Sonuç','Uzaklık km cinsinden bulunur.','d = 240 km')],
 dogru=240,yan=[(80,'Varış farkını S dalgasının hızıyla çarpmış: 20 × 4.','dikkat'),(120,'Varış farkını P dalgasının hızıyla çarpmış: 20 × 6.','dikkat'),(200,'Varış farkını iki hızın toplamıyla çarpmış: 20 × (6 + 4).','islem'),(480,'Varış farkını iki hızın çarpımıyla çarpmış: 20 × 6 × 4.','islem')],
 tipId='fz-dl2-ps-fark',tip='Deprem merkezine uzaklık (P–S farkı)',z='zor',alt='Deprem Dalgaları',kaz='P ve S dalgalarının istasyona varış zamanı farkından deprem merkezine olan uzaklığı hesaplar.',
 kart='K-FZDL2-19 (P ve S varış farkı) · 6 ve 4 km/s, fark 20 s',kalip='grafik',
 metin='Bir deprem sırasında oluşan P ve S dalgaları, deprem merkezinden aynı anda yola çıkarak aynı yol boyunca sabit hızlarla ilerlemiştir. P dalgasının hızı 6 km/s, S dalgasının hızı 4 km/s’dir. Şekilde, merkezden uzaktaki bir istasyonun sismografının kaydı ve P ile S dalgalarının istasyona ulaştığı anlar gösterilmiştir. Zaman ekseni, kaydın başlangıcından itibaren geçen süreyi saniye cinsinden vermektedir.\nBuna göre istasyonun deprem merkezine uzaklığı kaç km’dir?',
 istenen='İstasyonun deprem merkezine uzaklığı (km).',
 ip=['Kayıttan okunan varış farkının, iki dalganın aynı yolu farklı hızlarla almasından kaynaklandığını düşün.'],
 bilgi=[B('Hız, yol ve süre','sabit hızlı harekette süre = yol ÷ hız’dır. İki dalga aynı yolu farklı hızlarla alırsa süreleri farklı olur; yavaş olanın süresi uzun olur. Örnek: 10 km’lik yolu 5 km/s ile giden dalga 2 s, 2 km/s ile giden 5 s’de alır')],
 puf='Aynı yol için varış farkı: d ÷ v_S − d ÷ v_P = Δt; fark hızlardan biriyle çarpılarak bulunmaz.',sekil=SK)

# ================================================================== 20 · deprem şiddeti, büyüklüğü, korunma · orta · öncüllü · E (I, II ve III)
fo=[]
for r_ in (1.0,2.0,3.0): fo.append(f'\\draw[thick,gray] (0,0) circle ({r_});')
fo.append('\\fill (0,0) circle (2.2pt);')
fo.append(nd((0,0),'E','left'))
pos={'K':(.5,60),'L':(1.5,150),'M':(2.5,320)}
for n_,(r_,a_) in pos.items():
    p=(r_*cos(radians(a_)),r_*sin(radians(a_))); fo.append(f'\\fill {pt(p)} circle (2pt);'+nd(p,f'\\textbf{{{n_}}}','above right'))
for r_,s_,a_ in ((.72,'8',320),(1.5,'6',280),(2.5,'4',30)):
    p=(r_*cos(radians(a_)),r_*sin(radians(a_))); fo.append(nd(p,f'\\textbf{{{s_}}}','',',fill=white,draw,circle,inner sep=1.5pt'))
SK=tikz_svg(HEAD+'\n'.join(fo)+TAIL)
qo('0020',[A('Şiddeti karşılaştır','Şiddet, deprem yerlerde bıraktığı etkiyi gösterir ve merkez üssünden uzaklaştıkça azalır. K, 8 şiddetli bölgede; L, 6 şiddetli bölgededir.','şiddet K = 8 > L = 6 → I. doğru'),
 A('Büyüklüğü değerlendir','Büyüklük depremin açığa çıkardığı enerjiyle ilgilidir ve tek bir değerdir; yere göre değişmez.','büyüklük K, L, M için aynı → II. doğru'),
 A('Korunmayı değerlendir','Deprem anında bina içinde asansör kullanılmaz; çök–kapan–tutun hareketi yapılır.','çök–kapan–tutun → III. doğru'),A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],
 truth=(True,True,True),harf='E',tipId='fz-dl2-siddet',tip='Deprem büyüklüğü, şiddeti ve korunma',z='orta',alt='Deprem Dalgaları',kaz='Deprem büyüklüğü ile şiddetini ayırt eder ve deprem anında korunma davranışını belirler.',
 kart='K-FZDL2-20 (büyüklük–şiddet, korunma) · eş şiddet bölgeleri, K, L, M',kalip='öncüllü',
 metin='Bir depremin merkez üssü E noktasıdır. Şekilde, deprem sonrası hasar gözlemlerine göre belirlenen eş şiddet bölgeleri çemberlerle ayrılmış ve bölgelerin içindeki sayılar o bölgedeki deprem şiddetini göstermektedir. K, L ve M, deprem bölgesindeki üç yerleşim yeridir.\nBuna göre,\nI. Depremin şiddeti K’de L’dekinden büyüktür.\nII. Depremin büyüklüğü K, L ve M’de aynı değerdedir.\nIII. L’deki bir apartmanda bulunan kişi, deprem sırasında asansöre binmek yerine çök–kapan–tutun hareketini yapmalıdır.\nyargılarından hangileri doğrudur?',
 neden=[('şiddetin merkez üssünden uzaklaştıkça arttığını düşünmüş; şiddet merkez üssünde en büyüktür.','bilgi'),('büyüklüğün yere göre değiştiğini sanmış; büyüklük depremin kendisine ait tek değerdir, şiddet yere göre değişir.','bilgi'),('deprem anında asansörle hızlıca binadan çıkmanın doğru olduğunu düşünmüş; asansör kullanılmaz.','bilgi')],
 istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Şekildeki sayıların neyi gösterdiğini düşün.'],
 bilgi=[B('Büyüklük ve şiddet','büyüklük, depremde açığa çıkan enerjiyi gösterir ve her deprem için tek bir değerdir (sismograf kayıtlarından hesaplanır). Şiddet, depremin bir yerde yarattığı etkidir; merkez üssünde en büyüktür ve uzaklaştıkça azalır. Deprem anında çök–kapan–tutun yapılır, asansör kullanılmaz. Örnek: büyüklüğü 7 olan bir depremin şiddeti merkez üssünde 10, uzak bir kentte 6 olabilir')],
 puf='Büyüklük depremin tek değeri, şiddet yere göre değişen etkisidir; merkez üssünde şiddet en büyüktür.',sekil=SK)

# =============================== YAZ
assert len(P.ANA)==20
from collections import Counter
print('zorluk',Counter(x['zorluk'] for x in P.ANA),'harf',sorted(Counter(x['cevap']['sik'] for x in P.ANA).items()),'görsel',sum(1 for x in P.ANA if x['sekil']),'öncüllü',sum(1 for x in P.ANA if 'yargılarından hangileri' in x['metin']))
bitir(P,'dalgalariki','fiz|Dalgalar')
