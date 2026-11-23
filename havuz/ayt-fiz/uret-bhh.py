"""AYT Fizik · Basit Harmonik Hareket · 20 soruluk paket (3 kolay / 11 orta / 6 zor). Kardeş yok, ipucu 1.
Şekil verileri ve her cevap/çeldirici değeri Python'da (Fraction) hesaplanıp assert edilir; TikZ gövdeleri aynı verilerden üretilir. π = 3 alınan sorularda metinde belirtilir."""
import sys,os,json,math
ADIR=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(ADIR,'..')
sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,HV)
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from fractions import Fraction as Fr
H.KONU='Basit Harmonik Hareket'
UK='afiz|Basit Harmonik Hareket'
P=Parti('bhh','Basit Harmonik Hareket',UK,ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM 2018–2026 AYT Fizik (Basit Harmonik Hareket: yay–kütle, basit sarkaç, periyot, grafik yorumu; yalnız mantık) · 345 AYT Fizik · Bilgi Sarmal AYT Fizik denemeleri · MEB 11. sınıf'
g=10
_A0=A
def A(b,a,i,g=None): return _A0(b,a,i.replace(' · ',' × '),g)
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def rsq(x):
    x=Fr(x); n=math.isqrt(x.numerator); d=math.isqrt(x.denominator); assert n*n==x.numerator and d*d==x.denominator,x
    return Fr(n,d)
def Tyay(m,k): return 6*rsq(Fr(m)/Fr(k))      # π = 3
def Tsar(l,gg=g): return 6*rsq(Fr(l)/Fr(gg))
def sec(dogru,cands,hedef):
    r='ABCDE'.index(hedef); vs=[c[0] for c in cands]; assert dogru not in vs and len(set(vs))==len(vs),(dogru,vs)
    sm=sorted([c for c in cands if c[0]<dogru],key=lambda c:c[0]); lg=sorted([c for c in cands if c[0]>dogru],key=lambda c:c[0])
    assert len(sm)>=r and len(lg)>=4-r,(dogru,hedef,vs)
    return (sm[len(sm)-r:] if r else [])+lg[:4-r]
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def fig(body): return tikz_svg(HEAD+body+TAIL)
def zem(x0,x1,y=0): return f'\\fill[gray!30] ({x0},{y-.2}) rectangle ({x1},{y}); \\draw[thick] ({x0},{y}) -- ({x1},{y});'
def blok(cx,w,h,lab,y=0,fill='gray!25'):
    return f'\\draw[thick,fill={fill}] ({cx-w/2:.3f},{y}) rectangle ({cx+w/2:.3f},{y+h}); \\node at ({cx:.3f},{y+h/2:.3f}) {{{lab}}};'
def vk(x1,y1,x2,y2,lab='',pos='above',col='vurgu'):
    s=f'\\draw[{col},very thick,{ARR}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'
    if lab: s+=f' \\node[{col}!70!black,{pos},inner sep=2pt] at ({(x1+x2)/2:.3f},{(y1+y2)/2:.3f}) {{{lab}}};'
    return s
COIL='decorate,decoration={coil,aspect=.4,segment length=2.2mm,amplitude=1.7mm},thick'
def yay(x0,y0,x1,y1): return f'\\draw[{COIL}] ({x0:.3f},{y0:.3f}) -- ({x1:.3f},{y1:.3f});'
def duvar(x,y0,y1): return f'\\fill[gray!35] ({x-.25},{y0}) rectangle ({x},{y1}); \\draw[very thick] ({x},{y0}) -- ({x},{y1});'
def tavan(x0,x1,y=0): return f'\\fill[gray!35] ({x0},{y}) rectangle ({x1},{y+.22}); \\draw[very thick] ({x0},{y}) -- ({x1},{y});'
def axis_opts(xl,yl,xmin,xmax,ymin,ymax,xt,yt,w='7cm',h='5cm'):
    return (f'\\begin{{axis}}[width={w},height={h},xmin={xmin},xmax={xmax},ymin={ymin},ymax={ymax},xtick={{{xt}}},ytick={{{yt}}},grid=both,major grid style={{gray!55,thin}},'
            f'tick label style={{font=\\scriptsize}},/pgf/number format/use comma,axis lines=middle,xlabel={{{xl}}},ylabel={{{yl}}},xlabel style={{font=\\small,at={{(ticklabel* cs:1)}},anchor=west}},ylabel style={{font=\\small,at={{(ticklabel* cs:1)}},anchor=south}}]')
def egri(f,t0,t1,adim):
    n=int((t1-t0)/adim); pts=[(t0+i*adim,f(t0+i*adim)) for i in range(n+1)]
    return ' '.join(f'({a:.3f},{b:.3f})' for a,b in pts)
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS=[{'I'},{'II'},{'III'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}]
ROM=['I','II','III']
def adi(S): return SIR[SETS.index(set(S))]
def onc(truth,why,pos):
    """Her öncülün değeri truth'ta TEK yerde; açıklamalar buradan üretilir. pos: doğru şıkkın konumu (0–4)."""
    dS={r for r in ROM if truth[r]}; i=SETS.index(dS)
    onceki=[j for j in range(7) if j<i]; sonra=[j for j in range(7) if j>i]
    assert len(onceki)>=pos and len(sonra)>=4-pos,(adi(dS),pos)
    sec_=(onceki[len(onceki)-pos:] if pos else [])+sonra[:4-pos]
    sira=[SIR[j] for j in sorted(sec_+[i])]; assert sira.index(adi(dS))==pos
    yan=[]
    for j in sec_:
        S=SETS[j]; parca=[]
        for r in ROM:
            if (r in S)!=truth[r]:
                parca.append(f'{r} yargısını {"doğru" if r in S else "yanlış"} kabul etmiş; oysa {why[r]}.')
        assert parca
        yan.append((SIR[j],' '.join(parca),'bilgi'))
    return adi(dS),yan,sira
def onc_adim(truth,why):
    return [A(f'{r} numaralı yargıyı incele',why[r][0].upper()+why[r][1:]+'.',f'{r} {"doğru" if truth[r] else "yanlış"}') for r in ROM]+[A('Sonucu yaz','Doğru olan yargıları birleştir.',adi({r for r in ROM if truth[r]}))]
def dist(v,e): assert len({v,*[x[0] for x in e]})==len(e)+1,(v,e)

# ---------- bilgi kutuları (örnekler soruların sayılarından farklı) ----------
BY=B('Yay–kütle sistemi','Periyot T = 2π√(m ÷ k), frekans f = 1 ÷ T’dir; periyot genliğe bağlı değildir. Aynı sistem düşey de kurulsa, eğik düzlemde de kurulsa (sürtünmesiz) periyot değişmez, yalnız denge konumu kayar. Örnek: m = 1 kg, k = 100 N/m için T = 2π√(1 ÷ 100) = 0,2π s’dir')
BS=B('Basit sarkaç','Küçük açılı salınımda T = 2π√(ℓ ÷ g)’dir; periyot ip uzunluğuna ve yer çekimi ivmesine bağlıdır, kütleye ve genliğe bağlı değildir. Örnek: ℓ = 2,5 m için T = 2π√(2,5 ÷ 10) = π s’dir (g = 10 m/s²)')
BX=B('Uzanım, hız ve ivme','Uzanım x denge konumundan uzaklıktır. Geri çağırıcı kuvvet F = −k·x, ivme a = −ω²·x (ω = 2π ÷ T) olur; uzanım büyüdükçe ivme ve net kuvvet büyür, sürat azalır. Uç noktada hız sıfır, ivme en büyük; denge noktasında ivme sıfır, sürat en büyüktür. Örnek: x = 3 cm’de a = 12 cm/s² ise x = 6 cm’de a = 24 cm/s²’dir')
BE=B('Enerji ve en büyük sürat','Toplam enerji sabittir: E = ½kA² = Ek + Ep, Ep ∝ x². Uç noktada tüm enerji potansiyel, denge noktasında tüm enerji kinetiktir. Hız v = ω√(A² − x²), en büyük sürat v_maks = A·ω’dır. Örnek: ω = 5 rad/s, A = 8 cm için v_maks = 40 cm/s ve x = 4 cm’de v = 5·√(64 − 16) cm/s’dir')
BG=B('Grafik yorumu','x–t grafiğinin eğimi hızı, v–t grafiğinin eğimi ivmeyi verir; a = −ω²·x olduğundan a–t grafiği x–t grafiğinin ters işaretlisidir. Grafik tekrar etmeye başladığı süre periyottur; en büyük değer genliktir. Örnek: x–t grafiği t = 0’da +A’dan başlayıp t = 5 s’de yeniden +A’ya ilk kez dönüyorsa T = 5 s’dir')
BYB=B('Yayların bağlanması','Paralel bağlı özdeş yaylarda eşdeğer sabit toplanır (k_eş = k₁ + k₂), seri bağlı yaylarda 1 ÷ k_eş = 1 ÷ k₁ + 1 ÷ k₂’dir. Daha büyük k, daha küçük periyot demektir. Örnek: k ve 3k’lık iki yay paralel bağlanırsa k_eş = 4k olur')
BO=B('İvmeli ortamda sarkaç','İvmeli bir ortamda (asansör, roket) sarkaç, g yerine g_etkin ile salınır: yukarı ivmede g_etkin = g + a, aşağı ivmede g_etkin = g − a. Her sistemin periyot bağıntısı ayrı yazılır. Örnek: a = 10 m/s² yukarı yönlüyse g_etkin = 20 m/s²’dir')
BPI=B('π = 3 alınması','Soruda belirtildiğinde π = 3 alınır; 2π = 6 olur. Örnek: T = 2π√(m ÷ k) ifadesinde m ÷ k = 1 ÷ 25 ise T = 6 · 0,2 = 1,2 s’dir')
BKM=B('Üst üste kütleler ve sürtünme','Üstteki cisim, alttaki cisimle birlikte aynı ivmeyle titreşir; ona ivmeyi statik sürtünme kuvveti kazandırır. Kaymama koşulu: ω²·A ≤ μ·g. Örnek: ω² = 50 s⁻² ve μ·g = 4 m/s² ise A en çok 0,08 m olabilir')
BMK=B('Titreşimde momentum ve kütle ekleme','Yatay titreşen sisteme dik doğrultuda yapışan cisim, yatay momentumu korunur; kütle artınca hız azalır. Yeni genlik A′ = v′ ÷ ω′ ile (denge noktasında v′ en büyük hızdır) bulunur. Örnek: 2 kg’lık cisim 6 m/s ile geçerken 1 kg’lık hamur yapışırsa v′ = 4 m/s olur')

# ---------- kartlar ----------
kartla('K-AFBHH-01','Yay–kütle periyodu ve salınım sayısı','T = 2π√(m ÷ k) ile bir salınımın süresi bulunur; n salınım süresi n·T’dir.','2π ya da karekökü unutmak; yarım periyodu periyot saymak.','kolay','şekilli',3,'bh-yay','Yay–kütle sistemi')
kartla('K-AFBHH-02','Basit sarkaç periyodu','Küçük açılı salınımda T = 2π√(ℓ ÷ g) uygulanır.','ℓ ÷ g yerine ℓ·g yazmak; yarım periyodu periyot saymak.','kolay','şekilli',3,'bh-sarkac','Basit sarkaç')
kartla('K-AFBHH-03','Sarkaçta nitel yargılar','Denge noktasında sürat en büyük; periyot kütleye bağlı değil, gidiş süresi yarım periyot.','Periyodu kütleye bağlı sanmak; yarım periyot ile periyodu karıştırmak.','kolay','öncüllü',3,'bh-nitel','Uzanım, hız ve ivme ilişkileri')
kartla('K-AFBHH-04','x–t grafiğinden yargı','x–t grafiğinden periyot, denge anları ve alınan yol okunur.','Periyodu yarım çevrim süresi sanmak; uç noktayı denge sanmak.','orta','öncüllü',4,'bh-grafik','Grafik yorumu')
kartla('K-AFBHH-05','T²–m grafiğinden yay sabiti','T² = (4π²÷k)·m olduğundan T²–m doğrusunun eğimi 4π²÷k’dir.','Eğimi k sanmak; 4π² katsayısını yanlış yazmak.','orta','grafik',4,'bh-grafik','Grafik yorumu')
kartla('K-AFBHH-06','Denge uzamasından periyot','Düşey yayda m·g = k·x₀ olduğundan T = 2π√(x₀ ÷ g); kütle gerekmez.','Birimi (cm) çevirmemek; yay sabitini bilinmeyen sanıp çözümsüz bırakmak.','orta','şekilli',4,'bh-yay','Yay–kütle sistemi')
kartla('K-AFBHH-07','İvmeli asansörde sarkaç ve yay','İvmeli ortamda sarkacın g_etkin’i değişir; yay–kütle periyodu ve kütle etkisi sorgulanır.','Yayın periyodunu da değişir sanmak; kütlenin etkisini aramak.','orta','öncüllü',4,'bh-ortam','İvmeli ortamda titreşim')
kartla('K-AFBHH-08','Uzanım ve hızdan periyot','v = ω√(A² − x²) bağıntısından ω, sonra T = 2π ÷ ω bulunur.','ω = v ÷ x yazmak; cm ile m’yi karıştırmak.','orta','şekilli',5,'bh-enerji','Enerji ve en büyük sürat')
kartla('K-AFBHH-09','v–t grafiğinden yargı','v–t grafiğinde hızın sıfır olduğu anlar uç, en büyük olduğu anlar denge konumudur.','Hız sıfır olan anı denge sanmak; eğim ile değeri karıştırmak.','orta','öncüllü',4,'bh-grafik','Grafik yorumu')
kartla('K-AFBHH-10','a–t grafiğinden yargı','a–t grafiğinden uç/denge anları ve hızın yönü okunur.','İvme sıfır olan anı uç sanmak; hızın yönünü ivmeyle aynı sanmak.','orta','öncüllü',4,'bh-grafik','Grafik yorumu')
kartla('K-AFBHH-11','Sarkaçta ip ve yer çekimi değişimi','T ∝ √(ℓ ÷ g) oranları birlikte uygulanır.','Karekökü almamak; yalnız bir değişimi hesaba katmak.','orta','şekilli',3,'bh-sarkac','Basit sarkaç')
kartla('K-AFBHH-12','Çivili sarkaç','Çivi nedeniyle iki yarım salınım farklı uzunluklarla yapılır; periyot iki yarım periyodun toplamıdır.','Tüm salınımı tek uzunlukla hesaplamak; iki periyodu toplamak.','zor','şekilli',5,'bh-sarkac','Basit sarkaç')
kartla('K-AFBHH-13','Üst üste kütlelerde kaymama','Üstteki cismin ivmesini statik sürtünme sağlar: ω²A ≤ μg, ω² = k ÷ toplam kütle.','Yalnız bir kütleyi kullanmak; μ ya da g’yi unutmak.','zor','şekilli',5,'bh-kayma','Üst üste kütleler')
kartla('K-AFBHH-14','x–t grafiğinden ortalama sürat','Yol ile yer değiştirmeyi ayırmak: grafikten konumlar okunup alınan yol bulunur.','Ortalama hız ile ortalama sürati karıştırmak; yolu eksik saymak.','orta','grafik',5,'bh-grafik','Grafik yorumu')
kartla('K-AFBHH-15','Eşit aralıklı noktalarda ivme ve enerji','Uzanım oranlarından ivme, uzanımın karesinden potansiyel enerji oranı bulunur.','Ep’yi x ile orantılı sanmak; uçtan denge noktasına giderken sürati azalır saymak.','orta','öncüllü',4,'bh-nitel','Uzanım, hız ve ivme ilişkileri')
kartla('K-AFBHH-16','F–x grafiğinden en büyük sürat','Grafik eğiminden k, ardından ω ve v_maks = Aω bulunur.','Birimleri (cm) çevirmemek; ω yerine k÷m yazmak.','zor','grafik',5,'bh-enerji','Enerji ve en büyük sürat')
kartla('K-AFBHH-17','Frekansı artıran işlemler','f = (1÷2π)√(k÷m); genlik frekansı etkilemez, paralel yay k’yi artırır.','Genliği frekansı artırır sanmak; kütle artışını frekansı artırır saymak.','orta','öncüllü',4,'bh-yay','Yay–kütle sistemi')
kartla('K-AFBHH-18','Seri ve paralel yaylarda periyot oranı','Seri k÷2, paralel 2k eşdeğer sabit verir; periyot oranı karekökle bulunur.','Karekökü almamak; oranı ters yazmak.','orta','şekilli',4,'bh-yay','Yay–kütle sistemi')
kartla('K-AFBHH-19','İvmeli ortamda ve değişen uzunlukta sarkaç','g_etkin = g + a ve ip uzunluğu oranı T ∝ √(ℓ ÷ g_etkin) ile birlikte uygulanır.','Ortamın ivmesini ya da ip uzunluğu değişimini hesaba katmamak; karekökü unutmak.','zor','şekilli',4,'bh-ortam','İvmeli ortamda titreşim')
kartla('K-AFBHH-20','Titreşim sırasında kütle ekleme','Yatay momentum korunur, ω değişir; yeni genlik A′ = v′ ÷ ω′.','Genliği değişmez sanmak; eski ω’yı kullanmak.','zor','şekilli',5,'bh-kutle','Kütle ekleme ve momentum')

TIPAD={'bh-yay':'Yay–kütle sistemi','bh-sarkac':'Basit sarkaç','bh-nitel':'Uzanım, hız ve ivme ilişkileri','bh-grafik':'Grafik yorumu','bh-enerji':'Enerji ve en büyük sürat','bh-ortam':'İvmeli ortamda titreşim','bh-kayma':'Üst üste kütleler','bh-kutle':'Kütle ekleme ve momentum'}
def S(no): return dict(kalip=None)  # yer tutucu
def NUM(no,tipId,z,alt,kaz,kart,kalip,metin,dogru,e,hedef,istenen,ip,bilgi,sekil,ad,puf):
    dist(dogru,e)
    q(no,tipId=tipId,tip=TIPAD[tipId],z=z,alt=alt,kaz=kaz,kart=kart,kalip=kalip,metin=metin,dogru=dogru,yan=sec(dogru,e,hedef),istenen=istenen,ip=ip,bilgi=bilgi,sekil=sekil,ad=ad,puf=puf)
def ONC(no,tipId,z,alt,kaz,kart,metin,truth,why,pos,istenen,ip,bilgi,sekil,puf,kalip='öncüllü'):
    d,yan,sira=onc(truth,why,pos)
    q(no,tipId=tipId,tip=TIPAD[tipId],z=z,alt=alt,kaz=kaz,kart=kart,kalip=kalip,metin=metin,dogru=d,yan=yan,sira=sira,istenen=istenen,ip=ip,bilgi=bilgi,sekil=sekil,ad=onc_adim(truth,why),puf=puf)

# ---- ortak çizim parçaları ----
def sarkac(Lu,aci,etiket,ox=0,oy=0,genis=1.7):
    """Tavandan sarkan sarkaç; etiket: [(ad,açı°,dolu)]"""
    s=tavan(ox-genis,ox+genis,oy)+f'\\draw[dashed,gray] ({ox},{oy}) -- ({ox},{oy-Lu});\n'
    for ad_,a,dolu in etiket:
        x=ox+Lu*math.sin(math.radians(a)); y=oy-Lu*math.cos(math.radians(a))
        s+=f'\\draw[thick] ({ox},{oy}) -- ({x:.3f},{y:.3f});\n\\draw[thick,fill=gray!{50 if dolu else 15}] ({x:.3f},{y:.3f}) circle (.17);\n'
        pos='left' if a<0 else ('right' if a>0 else 'below')
        s+=f'\\node[{pos},inner sep=9pt] at ({x:.3f},{y-(.15 if a==0 else 0):.3f}) {{{ad_}}};\n'
    return s

# ================= 01 kolay · yay–kütle, 10 salınım =================
m1,k1=Fr(1,2),200
T1=Tyay(m1,k1); S10=10*T1
assert T1==Fr(3,10) and S10==3
e1=[(Fr(1,2),'Periyodu 2π çarpanı olmadan T = √(m ÷ k) = 0,05 s bulmuş; 10 salınım 0,5 s eder.','islem'),
    (Fr(3,20),'Karekök almadan T = 2π · (m ÷ k) = 6 ÷ 400 = 0,015 s bulmuş; 10 salınım 0,15 s eder.','islem'),
    (Fr(3,2),'10 salınımın süresi yerine yarım periyodu 10 ile çarpmış: 10 · 0,15 = 1,5 s.','dikkat'),
    (Fr(6),'Gidiş ve dönüşü ayrı birer salınım sayıp 20 salınımın süresini hesaplamış: 20 · 0,3 = 6 s.','dikkat')]
body=zem(-.3,7)+duvar(0,0,1.4)+'\n'+yay(0,.45,2.9,.45)+'\n'+blok(3.45,1.1,.9,'0,5 kg')+'\n\\node[above] at (1.4,.75) {$k=200$ N/m};\n'
SK=fig(body)
NUM('0001','bh-yay','kolay','Yay–kütle Sistemi','Yay–kütle sisteminin periyodunu hesaplayıp belirli sayıda salınım için geçen süreyi bulur.','K-AFBHH-01 (yay–kütle periyodu) · m = 0,5 kg, k = 200 N/m, 10 salınım','şekilli',
 'Sürtünmesiz yatay düzlemde, esneklik sabiti 200 N/m olan yayın ucuna bağlı 0,5 kg kütleli cisim şekildeki gibi basit harmonik hareket yapmaktadır.\n(π = 3 alınız.)\nBuna göre, cismin 10 tam salınımı kaç saniyede tamamlanır?',
 S10,e1,'D','Cismin 10 tam salınım süresi (s).',['Önce bir tam salınımın süresini veren bağıntıyı yaz.'],[BY,BPI],SK,
 [A('Periyodu yaz','Yay–kütle sisteminde periyot T = 2π√(m ÷ k)’dir.','T = 6 · √(0,5 ÷ 200)'),
  A('Hesapla','Karekökün içi 1 ÷ 400’tür.','T = 6 · (1 ÷ 20) = 0,3 s'),
  A('10 salınımın süresini bul','Süre = salınım sayısı · periyot.','10 · 0,3 = 3 s')],
 'Salınım sayısı n ise süre n·T’dir; T = 2π√(m ÷ k).')

# ================= 02 kolay · basit sarkaç periyodu =================
l2=Fr(9,10); T2=Tsar(l2); assert T2==Fr(9,5)
e2=[(Fr(3,10),'2π çarpanını unutup T = √(ℓ ÷ g) = √(0,09) = 0,3 s bulmuş.','islem'),
    (Fr(27,50),'Karekök almadan T = 2π · (ℓ ÷ g) = 6 · 0,09 = 0,54 s bulmuş.','islem'),
    (Fr(3,5),'2π yerine 2 yazmış: T = 2 · √(ℓ ÷ g) = 2 · 0,3 = 0,6 s.','islem'),
    (Fr(9,10),'Periyot yerine K’den N’ye gidiş süresini, yani yarım periyodu (0,9 s) yazmış.','dikkat')]
SK=fig(sarkac(3.4,16,[('K',-16,False),('M',0,True),('N',16,False)])+'\\draw[<->,thin] (-2.3,0) -- (-2.3,-3.4); \\node[left] at (-2.3,-1.7) {$\\ell=0{,}9$ m};')
NUM('0002','bh-sarkac','kolay','Basit Sarkaç','İp uzunluğu verilen basit sarkacın periyodunu hesaplar.','K-AFBHH-02 (basit sarkaç) · ℓ = 0,9 m','şekilli',
 'Şekildeki basit sarkaç, ağırlığı ihmal edilebilen 0,9 m uzunluğundaki ipe bağlı noktasal bir cisimden oluşmaktadır. Sarkaç, hava direncinin ihmal edildiği ortamda K ile N noktaları arasında küçük açılı salınım yapmaktadır; M, denge konumudur.\n(g = 10 m/s², π = 3 alınız.)\nBuna göre, sarkacın periyodu kaç saniyedir?',
 T2,e2,'E','Sarkacın periyodu (s).',['Periyodu hangi niceliklerin belirlediğini düşün.'],[BS,BPI],SK,
 [A('Bağıntıyı yaz','Küçük açılı salınımda T = 2π√(ℓ ÷ g).','T = 6 · √(0,9 ÷ 10)'),
  A('Karekökü bul','0,9 ÷ 10 = 0,09.','√0,09 = 0,3'),
  A('Periyodu hesapla','Çarpımı yap.','T = 6 · 0,3 = 1,8 s')],
 'Basit sarkaçta T = 2π√(ℓ ÷ g); kütle ve genlik hesaba girmez.')

# ================= 03 kolay · sarkaç nitel (öncüllü) =================
tr3={'I':True,'II':False,'III':False}
why3={'I':'sarkaç denge konumundan geçerken potansiyel enerjisi en küçük, kinetik enerjisi en büyüktür; dolayısıyla sürati en büyüktür',
      'II':'K’den N’ye ilk gidiş süresi yarım periyottur; periyot, cismin K’ye geri dönmesine kadar geçen süredir',
      'III':'T = 2π√(ℓ ÷ g) bağıntısında kütle yoktur; kütle artırılırsa periyot değişmez'}
SK=fig(sarkac(3.0,18,[('K',-18,False),('M',0,True),('N',18,False)]))
ONC('0003','bh-nitel','kolay','Sarkaçta Titreşim','Basit sarkaçta hız, süre ve periyodun bağlı olduğu niceliklerle ilgili yargıları değerlendirir.','K-AFBHH-03 (sarkaçta nitel yargılar)',
 'Şekildeki basit sarkaç, sürtünmelerin ihmal edildiği ortamda K ve N noktaları arasında küçük açılı basit harmonik hareket yapmaktadır; M noktası denge konumudur.\nBuna göre,\nI. Sarkaç, sürati en büyük olan noktada M’den geçmektedir.\nII. Sarkacın K’den N’ye ilk gidiş süresi periyoduna eşittir.\nIII. Sarkacın kütlesi artırılırsa periyodu da artar.\nyargılarından hangileri doğrudur?',
 tr3,why3,0,'Doğru olan yargılar.',['Her yargıyı periyodun ve enerjinin tanımıyla ayrı ayrı sına.'],[BS,BX],SK,
 'Basit sarkaçta sürat denge noktasında en büyüktür; periyot kütleye ve genliğe bağlı değildir.')

# ================= 04 orta · x–t grafiği (öncüllü) =================
A4=12; f4=lambda t:A4*math.cos(math.pi*t/4)
tr4={'I':False,'II':False,'III':True}
why4={'I':'konum, t = 0’daki değerine ilk kez t = 8 s’de döndüğünden periyot 8 s’dir',
      'II':'t = 4 s’de konum −12 cm’dir; cisim bu anda denge konumunda değil, uç konumdadır',
      'III':'cisim t = 0’da x = 12 cm’den başlayıp t = 2 s’de x = 0’a gelir; yani genlik kadar, 12 cm yol alır'}
assert round(f4(2),9)==0 and round(f4(4),9)==-12 and round(f4(8),9)==12
gr=axis_opts('$t$ (s)','$x$ (cm)',0,9,-14,14,'0,1,2,3,4,5,6,7,8','-12,-6,0,6,12')+'\n\\addplot[thick,vurgu,smooth] coordinates {'+egri(f4,0,8,.5)+'};\n\\end{axis}'
SK=fig(gr)
ONC('0004','bh-grafik','orta','Konum–zaman Grafiği','Basit harmonik hareket yapan cismin konum–zaman grafiğinden periyot, konum ve alınan yol hakkında yargı verir.','K-AFBHH-04 (x–t yargıları) · A = 12 cm, T = 8 s',
 'Basit harmonik hareket yapan bir cismin konum–zaman grafiği şekilde verilmiştir.\nBuna göre, cismin hareketi ile ilgili,\nI. Periyodu 4 s’dir.\nII. t = 4 s anında denge konumundadır.\nIII. t = 0 ile t = 2 s arasında 12 cm yol almıştır.\nyargılarından hangileri doğrudur?',
 tr4,why4,0,'Doğru olan yargılar.',['Grafiğin ilk kez tekrar ettiği anı ve her anda konumu oku.'],[BG,BX],SK,
 'x–t grafiğinde grafiğin kendini tekrar ettiği ilk süre periyottur; denge konumu x = 0’dır.',kalip='grafik')

# ================= 05 orta · T²–m grafiği, yay sabiti =================
m5,T25=3,Fr(108,100); k5=Fr(36)*m5/T25
assert k5==100
e5=[(Fr(324,25),'Oranı ters yazmış: k = 4π² · T² ÷ m = 36 · 1,08 ÷ 3 = 12,96 N/m.','islem'),
    (25,'T = π√(m ÷ k) yazıp 2 çarpanını unutmuş: k = π² · m ÷ T² = 9 · 3 ÷ 1,08 = 25 N/m.','islem'),
    (50,'T² = 2π² · m ÷ k diye yazmış: k = 18 · 3 ÷ 1,08 = 50 N/m.','islem'),
    (200,'T² = 8π² · m ÷ k diye yazmış: k = 72 · 3 ÷ 1,08 = 200 N/m.','islem'),
    (400,'T = 4π√(m ÷ k) yazmış: k = 16π² · m ÷ T² = 144 · 3 ÷ 1,08 = 400 N/m.','islem')]
assert [Fr(36)*Fr(2)**0*0+c[0] for c in e5]==[Fr(324,25),25,50,200,400]
assert Fr(9)*3/T25==25 and Fr(18)*3/T25==50 and Fr(72)*3/T25==200 and Fr(144)*3/T25==400 and Fr(36)*T25/3==Fr(324,25)
gr=axis_opts('$m$ (kg)','$T^2$ (s$^2$)',0,5,0,1.8,'0,1,2,3,4,5','0,0.36,0.72,1.08,1.44,1.8',w='6.4cm')+'\n\\addplot[thick,vurgu] coordinates {(0,0) (5,1.8)};\n\\addplot[only marks,mark=*,mark size=2pt,vurgu] coordinates {(3,1.08)};\n\\end{axis}'
SK=fig(gr)
NUM('0005','bh-grafik','orta','Periyot–kütle Grafiği','Periyodun karesi–kütle grafiğinin eğiminden yayın esneklik sabitini bulur.','K-AFBHH-05 (T²–m) · k = 100 N/m, π = 3','grafik',
 'Bir öğrenci, aynı yayın ucuna kütleleri farklı cisimler bağlayıp her biri için basit harmonik hareketin periyodunu ölçüyor ve periyodun karesinin (T²) kütleye (m) göre değişimini şekildeki grafikle gösteriyor. Grafik, orijinden geçen bir doğrudur.\n(Sürtünmeler ihmal edilmektedir, π = 3 alınız.)\nBuna göre, yayın esneklik sabiti kaç N/m’dir?',
 k5,e5,'D','Yayın esneklik sabiti (N/m).',['T² ile m arasındaki bağıntıyı yazıp grafikteki işaretli noktayı kullan.'],[BY,BG],SK,
 [A('Bağıntıyı yaz','T = 2π√(m ÷ k) ifadesinin karesi alınır.','T² = (4π² ÷ k) · m'),
  A('Noktayı oku','Doğru üzerindeki işaretli nokta: m = 3 kg için T² = 1,08 s².','1,08 = (36 ÷ k) · 3'),
  A('k’yi çöz','Denklemi k için yaz (π = 3 için 4π² = 36).','k = 108 ÷ 1,08'),
  A('Sonucu hesapla','Bölme işlemini yap.','k = 100 N/m')],
 'T²–m doğrusunun eğimi 4π² ÷ k’dir; k = 4π² ÷ eğim.')

# ================= 06 orta · denge uzamasından periyot =================
x6=Fr(1,10); T6=6*rsq(x6/g); assert T6==Fr(3,5)
e6=[(Fr(1,5),'2π yerine 2 yazmış: T = 2 · √(x₀ ÷ g) = 2 · 0,1 = 0,2 s.','islem'),
    (Fr(3,10),'2π çarpanını π diye almış: T = 3 · √(0,1 ÷ 10) = 0,3 s.','islem'),
    (Fr(6,5),'Bir tam salınım yerine iki salınımın süresini (2T) yazmış.','dikkat'),
    (6,'Uzamayı metreye çevirmeden 10 yazmış: T = 6 · √(10 ÷ 10) = 6 s.','dikkat')]
body=tavan(-.9,2.6)+f'\\draw[{COIL}] (-.2,0) -- (-.2,-1.5); \\draw[dashed,gray] (-.8,-1.5) -- (.5,-1.5); \\node[below,font=\\footnotesize] at (-.2,-1.6) {{boşta}};\n'
body+=f'\\draw[{COIL}] (1.4,0) -- (1.4,-3.0); \\draw[thick,fill=gray!25] (.95,-3.7) rectangle (1.85,-3.0); \\node at (1.4,-3.35) {{$m$}}; \\node[below,font=\\footnotesize] at (1.4,-3.75) {{denge}};\n'
body+='\\draw[dashed,gray] (.9,-1.5) -- (2.1,-1.5); \\draw[dashed,gray] (.95,-3.0) -- (2.1,-3.0); \\draw[<->,thin] (2.0,-1.5) -- (2.0,-3.0); \\node[right] at (2.05,-2.25) {$10$ cm};\n'
SK=fig(body)
NUM('0006','bh-yay','orta','Düşey Yay Sarkacı','Düşey yayın denge konumundaki uzamasından basit harmonik hareketin periyodunu bulur.','K-AFBHH-06 (denge uzaması) · x₀ = 10 cm, π = 3','şekilli',
 'Tavana asılı, esneklik sabiti bilinmeyen bir yayın ucuna kütlesi bilinmeyen bir cisim bağlandığında yay şekildeki gibi 10 cm uzayarak dengede kalıyor. Cisim, denge konumundan aşağı doğru az miktarda çekilip serbest bırakılınca düşey doğrultuda basit harmonik hareket yapıyor.\n(Sürtünmeler ihmal edilmektedir, g = 10 m/s², π = 3 alınız.)\nBuna göre, hareketin periyodu kaç saniyedir?',
 T6,e6,'C','Hareketin periyodu (s).',['Periyodu veren bağıntıdaki niceliklerin verilenlerle nasıl ilişkilendirilebileceğini düşün.'],[BY,BPI],SK,
 [A('Denge koşulunu yaz','Denge konumunda yay kuvveti ağırlığa eşittir.','k · x₀ = m · g → m ÷ k = x₀ ÷ g'),
  A('Oranı hesapla','x₀ = 0,1 m alınır.','m ÷ k = 0,1 ÷ 10 = 0,01 s²'),
  A('Periyodu yaz','T = 2π√(m ÷ k).','T = 6 · √0,01'),
  A('Sonucu bul','Karekökü al.','T = 6 · 0,1 = 0,6 s')],
 'Düşey yayda m ÷ k = x₀ ÷ g olduğundan T = 2π√(x₀ ÷ g); kütle ve k ayrı ayrı gerekmez.')

# ================= 07 orta · ivmeli asansör (öncüllü) =================
tr7={'I':False,'II':True,'III':True}
why7={'I':'asansör aşağı yönlü ivmeyle hızlanırken sarkaç için g_etkin = g − a = 7,5 m/s² olur ve T = 2π√(ℓ ÷ g_etkin) arttığından periyot azalmaz, artar',
      'II':'yay–kütle sisteminde T = 2π√(m ÷ k) bağıntısında g yoktur; periyot değişmez',
      'III':'sarkacın periyodu kütleye bağlı değildir; kütle artırılırsa periyot yine değişmez'}
body='\\draw[thick] (0,0) rectangle (5.2,4.2);\n'+tavan(.3,4.9,4.2).replace('4.2)','4.2)')+'\n'
body+=f'\\draw[thick] (1.4,4.2) -- ({1.4+2.2*math.sin(math.radians(14)):.3f},{4.2-2.2*math.cos(math.radians(14)):.3f}); \\draw[thick,fill=gray!50] ({1.4+2.2*math.sin(math.radians(14)):.3f},{4.2-2.2*math.cos(math.radians(14)):.3f}) circle (.18);\n'
body+=f'\\draw[{COIL}] (3.8,4.2) -- (3.8,2.5); \\draw[thick,fill=gray!25] (3.4,2.5) rectangle (4.2,1.8);\n'
body+=vk(5.8,3.4,5.8,2.0,'','right')+'\\node[right,vurgu!70!black] at (5.85,2.7) {$\\vec a$};\\node[right,font=\\footnotesize] at (5.85,2.2) {2,5 m/s²};\n'
SK=fig(body)
ONC('0007','bh-ortam','orta','İvmeli Ortamda Titreşim','İvmeli asansörde basit sarkaç ve yay–kütle sisteminin periyotlarını karşılaştırır.','K-AFBHH-07 (ivmeli asansör)',
 'Şekildeki asansörün içinde, tavana bir basit sarkaç ile bir düşey yay–kütle sistemi asılmıştır. Asansör aşağı yönlü 2,5 m/s² ivmeyle hızlanırken sarkaç küçük açılı, yay–kütle sistemi ise düşey doğrultuda basit harmonik hareket yapmaktadır. (g = 10 m/s², sürtünmeler önemsizdir.)\nAsansör durağan iken yapılan harekete göre,\nI. Sarkacın periyodu azalır.\nII. Yay–kütle sisteminin periyodu değişmez.\nIII. Sarkacın kütlesi artırılırsa periyodu değişmez.\nyargılarından hangileri doğrudur?',
 tr7,why7,3,'Doğru olan yargılar.',['Her sistemin periyodunu belirleyen nicelikleri ayrı ayrı yaz.'],[BO,BY],SK,
 'İvmeli ortamda periyodu belirleyen nicelikler her sistem için ayrı ayrı değerlendirilir.')

# ================= 08 zor · uzanım ve hızdan periyot =================
A8,x8,v8=10,6,16
w8=rsq(Fr(v8**2,A8**2-x8**2)); T8=6/w8
assert w8==2 and T8==3
e8=[(Fr(3,2),'A − x = 4 cm alıp ω = v ÷ 4 = 4 rad/s ve T = 6 ÷ 4 = 1,5 s bulmuş.','islem'),
    (2,'Hesapladığı ω değerini (2 rad/s) periyot olarak yazmış.','dikkat'),
    (Fr(9,4),'ω = v ÷ x = 16 ÷ 6 alıp T = 6 ÷ ω = 2,25 s bulmuş; v = ω·x bağıntısı yalnız denge noktası için geçerlidir.','bilgi'),
    (Fr(15,4),'ω = v ÷ A = 1,6 rad/s alıp T = 6 ÷ 1,6 = 3,75 s bulmuş.','bilgi'),
    (6,'A + x = 16 cm alıp ω = 1 rad/s ve T = 6 s bulmuş.','islem')]
assert Fr(6)/Fr(v8,A8-x8)==Fr(3,2) and Fr(6)*6/v8==Fr(9,4) and 6/Fr(v8,A8)==Fr(15,4) and 6/Fr(v8,A8+x8)==6
u=.26
body=zem(-4.5,5.5)+duvar(-4.2,0,1.5)+'\n'+yay(-4.2,.5,x8*u-.45,.5)+'\n'+blok(x8*u,.9,.9,'m')+'\n'
for xx,lab in [(0,'O'),(-A8*u,'K'),(A8*u,'L')]:
    body+=f'\\draw[thick] ({xx},-.2) -- ({xx},.15); \\node[below] at ({xx},-.2) {{{lab}}};\n'
body+=vk(x8*u+.6,.45,x8*u+1.7,.45,'16 cm/s','above')+'\n'
body+=f'\\draw[<->,thin] (0,-1.0) -- ({x8*u},-1.0); \\node[below] at ({x8*u/2},-1.0) {{6 cm}}; \\draw[<->,thin] (0,-1.7) -- ({A8*u},-1.7); \\node[below] at ({A8*u/2},-1.7) {{10 cm}};\n'
SK=fig(body)
NUM('0008','bh-enerji','orta','Uzanım ve Hız','Uzanım ve hız verilen basit harmonik hareketin açısal frekansını ve periyodunu bulur.','K-AFBHH-08 (v = ω√(A²−x²)) · A = 10 cm, x = 6 cm, v = 16 cm/s','şekilli',
 'Sürtünmesiz yatay düzlemde yayın ucuna bağlı m kütleli cisim, K ve L noktaları arasında denge konumu O olan basit harmonik hareket yapmaktadır. O’ya uzaklığı 10 cm olan K ve L, hareketin uç noktalarıdır. Cisim, O’nun sağında 6 cm uzaklıktan sağa doğru 16 cm/s süratle geçmektedir.\n(π = 3 alınız.)\nBuna göre, hareketin periyodu kaç saniyedir?',
 T8,e8,'D','Hareketin periyodu (s).',['Hızı, genlik ve uzanım cinsinden veren bağıntıyı yaz.'],[BE,BPI],SK,
 [A('Bağıntıyı yaz','Basit harmonik harekette v = ω√(A² − x²).','16 = ω · √(10² − 6²)'),
  A('ω’yı bul','Karekökün içi 64’tür.','16 = ω · 8 → ω = 2 rad/s'),
  A('Periyoda geç','T = 2π ÷ ω, π = 3.','T = 6 ÷ 2'),
  A('Sonucu yaz','Bölme işlemini yap.','T = 3 s')],
 'v = ω√(A² − x²); ω bulunduktan sonra T = 2π ÷ ω.')

# ================= 09 orta · v–t grafiği (öncüllü) =================
f9=lambda t:-6*math.sin(math.pi*t/2)
tr9={'I':True,'II':True,'III':False}
why9={'I':'hız–zaman grafiği t = 0’da 0 iken t = 4 s’de yeniden 0 ve aynı yönde artmaya başlıyor; hareket 4 s’de kendini tekrar eder',
      'II':'t = 2 s’de hız sıfırdır; hızın sıfır olduğu anlarda cisim uç konumdadır',
      'III':'t = 0’dan t = 1 s’ye hızın büyüklüğü 0’dan 6 m/s’ye artar; yani sürat azalmaz, artar'}
gr=axis_opts('$t$ (s)','$v$ (m/s)',0,4.6,-7,7,'0,1,2,3,4','-6,-3,0,3,6')+'\n\\addplot[thick,vurgu,smooth] coordinates {'+egri(f9,0,4,.25)+'};\n\\end{axis}'
SK=fig(gr)
ONC('0009','bh-grafik','orta','Hız–zaman Grafiği','Basit harmonik hareketin hız–zaman grafiğinden periyot, uç konum ve sürat değişimi hakkında yargı verir.','K-AFBHH-09 (v–t yargıları) · T = 4 s, v_maks = 6 m/s',
 'Sürtünmesiz yatay düzlemde yayın ucuna bağlı bir blok, denge konumu çevresinde titreşmektedir. Bloğun yatay doğrultudaki hızının zamanla değişimi şekildeki grafikte verilmiştir.\nBuna göre,\nI. hareket 4 s sürede kendini tekrar eder.\nII. blok, t = 2 s anında yayın en çok uzanmış ya da sıkışmış olduğu konumdadır.\nIII. blok, ilk 1 s içinde yavaşlamaktadır.\nyargılarından hangileri doğrudur?',
 tr9,why9,1,'Doğru olan yargılar.',['Hızın sıfır ve en büyük olduğu anların cisim için ne anlama geldiğini düşün.'],[BG,BX],SK,
 'v–t grafiğinde hızın sıfır olduğu anlar uç konumları, hız büyüklüğünün en büyük olduğu anlar denge konumunu gösterir.',kalip='grafik')

# ================= 10 orta · a–t grafiği (öncüllü) =================
f10=lambda t:8*math.cos(math.pi*t/3)
tr10={'I':True,'II':True,'III':True}
why10={'I':'t = 0’da ivme en büyük değerindedir; a = −ω²x olduğundan cisim bu anda uç konumdadır',
       'II':'ivme t = 1,5 s’de pozitiften negatife, t = 4,5 s’de negatiften pozitife geçtiği için cisim denge konumundan bu anlarda zıt yönlerde geçer; hızlar zıt yönlüdür',
       'III':'t = 3 s’de ivme t = 0’daki değerin tersidir; yani cisim t = 0’daki uç konumun karşısındaki uçtadır'}
gr=axis_opts('$t$ (s)','$a$ (m/s$^2$)',0,6.8,-10,10,'0,1.5,3,4.5,6','-8,-4,0,4,8')+'\n\\addplot[thick,vurgu,smooth] coordinates {'+egri(f10,0,6,.25)+'};\n\\end{axis}'
SK=fig(gr)
ONC('0010','bh-grafik','orta','İvme–zaman Grafiği','İvme–zaman grafiğinden cismin uç ve denge konumlarını ve hız yönlerini yorumlar.','K-AFBHH-10 (a–t yargıları) · T = 6 s',
 'Doğrusal bir yörüngede basit harmonik hareket yapan bir cismin ivme–zaman grafiği şekilde verilmiştir.\nBuna göre, cismin hareketi ile ilgili,\nI. t = 0 anında uç konumdadır.\nII. t = 1,5 s ve t = 4,5 s anlarında hızları zıt yönlüdür.\nIII. t = 3 s anında, t = 0 anındaki uç konumun karşısındaki uç konumdadır.\nyargılarından hangileri doğrudur?',
 tr10,why10,4,'Doğru olan yargılar.',['a = −ω²x bağıntısıyla ivmenin işaretinden konumu çıkar.'],[BG,BX],SK,
 'a–t grafiği x–t grafiğinin −ω² katıdır: ivme sıfırken cisim denge konumundan, ivme en büyükken uç konumdadır.',kalip='grafik')

# ================= 11 orta · ip ve yer çekimi değişimi =================
T11=Fr(3,5); T11n=T11*rsq(Fr(4)/Fr(1,4)); assert T11n==Fr(12,5)
e11=[(Fr(3,20),'Oranları ters yazmış: T = 0,6 ÷ 4 = 0,15 s.','islem'),
     (Fr(3,5),'Periyodun değişmediğini düşünmüş.','bilgi'),
     (Fr(6,5),'İki değişimden yalnızca birini (ip uzunluğunun 4 katına çıkmasını) hesaba katmış: T = 0,6 · 2 = 1,2 s.','dikkat'),
     (Fr(24,5),'Bir değişimde karekök alıp diğerinde almamış: T = 0,6 · 2 · 4 = 4,8 s.','islem'),
     (Fr(48,5),'İki değişimde de karekök almamış: T = 0,6 · 4 · 4 = 9,6 s.','islem')]
assert T11*2*4==Fr(24,5) and T11*16==Fr(48,5)
NUM('0011','bh-sarkac','orta','Basit Sarkaç','İp uzunluğu ve yer çekimi ivmesi değişen sarkacın yeni periyodunu oran yoluyla bulur.','K-AFBHH-11 (ℓ ve g oranları) · T = 0,6 s, 4ℓ ve g/4','şekilli',
 'Yer yüzünde periyodu 0,6 s olan bir basit sarkaç, küçük açılı salınım yapmaktadır. Bu sarkacın ipi aynı malzemeden 4 katı uzunluğunda bir ip ile değiştirilip sarkaç, yer çekimi ivmesi yer yüzündekinin dörtte biri olan bir gezegene götürülüyor ve burada da küçük açılı salınım yapması sağlanıyor.\nBuna göre, sarkacın bu gezegendeki periyodu kaç saniyedir?',
 T11n,e11,'C','Sarkacın gezegendeki periyodu (s).',['Periyodun ℓ ve g ile nasıl orantılı olduğunu yaz; iki değişimi birlikte uygula.'],[BS],None,
 [A('Oranı yaz','T ∝ √(ℓ ÷ g).','T′ ÷ T = √(ℓ′ ÷ ℓ) · √(g ÷ g′)'),
  A('Değerleri yerine koy','ℓ′ = 4ℓ ve g′ = g ÷ 4.','T′ ÷ T = √4 · √4 = 4'),
  A('Yeni periyodu bul','Oranı T ile çarp.','T′ = 4 · 0,6 = 2,4 s')],
 'T ∝ √(ℓ ÷ g); iki değişim varsa oranlar karekök içinde birlikte çarpılır.')
P.ANA[-1]['kalip']='hikâyeli'

# ================= 12 zor · çivili sarkaç =================
l12,d12=Fr(9,10),Fr(1,2); lk=l12-d12
T12=3*rsq(l12/g)+3*rsq(lk/g); assert lk==Fr(2,5) and T12==Fr(3,2)
e12=[(Fr(6,5),'Tüm salınımı çivinin altında kalan 0,4 m’lik ipin periyoduyla hesaplamış: T = 6 · 0,2 = 1,2 s.','dikkat'),
     (Fr(3,4),'İki yarım salınımın süresini toplamak yerine ortalamasını almış: (0,9 + 0,6) ÷ 2 = 0,75 s.','islem'),
     (Fr(9,10),'Yalnızca uzun ipin yarım periyodunu (0,9 s) yazmış.','dikkat'),
     (Fr(3,5),'Yalnızca kısa ipin yarım periyodunu (0,6 s) yazmış.','dikkat')]
R=4.5; Rk=2.0; aK=10; aN=math.degrees(math.acos(1-(R*(1-math.cos(math.radians(aK))))/Rk))
Kx=-R*math.sin(math.radians(aK)); Ky=-R*math.cos(math.radians(aK)); Nx=Rk*math.sin(math.radians(aN)); Ny=-2.5-Rk*math.cos(math.radians(aN))
assert abs(Ky-Ny)<1e-9 and 4.5/5==0.9 and 2.5/5==0.5
body=tavan(-1.3,1.3,0)+f'\\draw[dashed,gray] (0,0) -- (0,-{R});\n'
body+=f'\\draw[thick] (0,0) -- ({Kx:.3f},{Ky:.3f}); \\draw[thick,fill=gray!50] ({Kx:.3f},{Ky:.3f}) circle (.17);\n'
body+=f'\\draw[thick] (0,-2.5) -- ({Nx:.3f},{Ny:.3f}); \\draw[thick,dashed,fill=gray!12] ({Nx:.3f},{Ny:.3f}) circle (.17);\n'
body+='\\fill (0,-2.5) circle (.1); \\node[right,inner sep=5pt] at (0,-2.5) {Ç};\n'
body+=f'\\draw[<->,thin] (-2.2,0) -- (-2.2,-{R}); \\node[left] at (-2.2,-{R/2}) {{0,9 m}}; \\draw[<->,thin] (.9,0) -- (.9,-2.5); \\node[right] at (.9,-1.25) {{0,5 m}};\n'
SK=fig(body)
NUM('0012','bh-sarkac','zor','Basit Sarkaç','Çivi nedeniyle uzunluğu değişen sarkacın periyodunu iki yarım salınımın toplamı olarak bulur.','K-AFBHH-12 (çivili sarkaç) · ℓ = 0,9 m, çivi 0,5 m altta','şekilli',
 'Şekilde, tavandaki bir noktadan 0,9 m uzunluğundaki ince bir ip ile asılı noktasal cisim, ipin tavana bağlandığı noktanın 0,5 m altındaki Ç çivisine takılacak biçimde küçük açılı salınım yapmaktadır. Cisim sol uçtan serbest bırakıldığında ip, denge konumunda çiviye takılıp sağ tarafta kalan kısmıyla salınıma devam etmektedir; iki uç, denge konumundan aynı yükseklikte kabul edilir.\n(g = 10 m/s², π = 3 alınız; hava direnci ve sürtünmeler önemsizdir.)\nBuna göre, cismin tam bir salınımının (başladığı uca dönüşünün) süresi kaç saniyedir?',
 T12,e12,'E','Cismin tam bir salınım süresi (s).',['Salınımın iki yarısında ipin etkin uzunluğunun ne olduğunu belirle.'],[BS,BPI],SK,
 [A('Sol yarı salınımı bul','Sol tarafta uzunluk 0,9 m’dir; yarım salınım T₁ ÷ 2 sürer.','T₁ ÷ 2 = 3 · √(0,9 ÷ 10) = 3 · 0,3 = 0,9 s'),
  A('Çivi altındaki uzunluğu bul','Sağ tarafta ip çiviye takılır.','ℓ₂ = 0,9 − 0,5 = 0,4 m'),
  A('Sağ yarı salınımı bul','Yarım salınım T₂ ÷ 2 sürer.','T₂ ÷ 2 = 3 · √(0,4 ÷ 10) = 3 · 0,2 = 0,6 s'),
  A('Toplamı yaz','Tam salınım iki yarım salınımın toplamıdır.','T = 0,9 + 0,6 = 1,5 s')],
 'Çivili sarkaçta tam salınım süresi, iki ayrı uzunluğun yarım periyotlarının toplamıdır.')

# ================= 13 zor · üst üste kütleler =================
M13,m13,k13,mu13=3,1,400,Fr(1,2)
w2=Fr(k13,M13+m13); Amax=mu13*g/w2*100
assert w2==100 and Amax==5
e13=[(Fr(1,2),'Ivmeyi μ·g yerine μ olarak yazıp g’yi unutmuş: A = 0,5 ÷ 100 = 0,005 m = 0,5 cm.','islem'),
     (Fr(5,4),'ω² = k ÷ m = 400 almış (yalnız üstteki kütle): A = 5 ÷ 400 = 1,25 cm.','dikkat'),
     (Fr(5,2),'Toplam kütle yerine kütle farkını (3 − 1 = 2 kg) kullanmış: ω² = 200, A = 5 ÷ 200 = 2,5 cm.','dikkat'),
     (Fr(15,4),'ω² = k ÷ M = 400 ÷ 3 almış (yalnız alttaki kütle): A = 5 × 3 ÷ 400 m = 3,75 cm.','dikkat'),
     (10,'Statik sürtünme katsayısını hesaba katmamış: A = g ÷ ω² = 10 ÷ 100 = 0,1 m = 10 cm.','islem')]
assert mu13*g*(M13+m13)/k13*100==5 and Fr(5)/k13*100*0+mu13*g*m13/Fr(k13)*100==Fr(5,4) and mu13*g*(M13-m13)/Fr(k13)*100==Fr(5,2) and mu13*g*M13/Fr(k13)*100==Fr(15,4) and mu13/w2*100==Fr(1,2) and Fr(g)/w2*100==10
body=zem(-.3,6.8)+duvar(0,0,1.8)+'\n'+yay(0,.5,2.9,.5)+'\n\\node[above] at (1.45,.8) {$k=400$ N/m};\n'+blok(3.6,1.4,1.0,'3 kg')+'\n'+blok(3.6,.8,.7,'1 kg',y=1.0)+'\n'
body+='\\node[right,align=left] at (4.5,1.2) {iki blok arasında\\\\$\\mu_s=0{,}5$};\n\\node[below] at (3.3,-.25) {zemin sürtünmesiz};\n'
SK=fig(body)
NUM('0013','bh-kayma','zor','Üst Üste Kütleler','Üst üste duran iki kütlenin birlikte titreşebileceği en büyük genliği, statik sürtünme koşulundan bulur.','K-AFBHH-13 (kaymama koşulu) · 3 kg + 1 kg, k = 400, μs = 0,5','şekilli',
 'Sürtünmesiz yatay düzlemde, esneklik sabiti 400 N/m olan yayın ucuna bağlı 3 kg kütleli bloğun üzerine 1 kg kütleli ikinci blok konulmuştur. Bloklar arasındaki statik sürtünme katsayısı 0,5’tir. Sistem, yayın denge konumu çevresinde yatay doğrultuda basit harmonik hareket yapmaktadır.\n(g = 10 m/s²)\nÜstteki blok alttakine göre kaymadığına göre, hareketin genliği en çok kaç cm olabilir?',
 Amax,e13,'E','Kaymadan titreşimin en büyük genliği (cm).',['Blokların birlikte hareket edebilmesi için gereken koşulu yaz.'],[BKM,BY],SK,
 [A('Ortak açısal frekansı bul','İki blok birlikte titreşir; toplam kütle 4 kg.','ω² = k ÷ (M + m) = 400 ÷ 4 = 100 s⁻²'),
  A('Üstteki bloğun en büyük ivmesi','İvmeyi statik sürtünme kuvveti kazandırır; kayma sınırında f = μ·m·g.','a_maks = μ·g = 0,5 · 10 = 5 m/s²'),
  A('Uç noktadaki ivmeyi eşitle','Titreşimde en büyük ivme uç noktadadır: a_maks = ω²·A.','ω²·A = 5 → A = 5 ÷ 100 = 0,05 m'),
  A('Birimi çevir','Metreyi santimetreye çevir.','A = 5 cm')],
 'Kaymama koşulu: ω²·A ≤ μ·g; ω² toplam kütleyle bulunur.')

# ================= 14 zor · x–t, ortalama sürat =================
A14=12; f14=lambda t:A14*math.sin(math.pi*t/4)
yol14=3*A14; sur14=Fr(yol14,6); hiz14=Fr(A14,6)
assert round(f14(2),9)==12 and round(f14(4),9)==0 and round(f14(6),9)==-12 and sur14==6 and hiz14==2
e14=[(hiz14,'Yer değiştirmeyi (12 cm) süreye bölüp ortalama hızın büyüklüğünü (2 cm/s) bulmuş; ortalama sürat için alınan yol kullanılmalıdır.','dikkat'),
     (4,'İlk 4 s’deki yolu (24 cm) 6 s’ye bölmüş: 24 ÷ 6 = 4 cm/s.','islem'),
     (9,'En büyük süratı (A·ω = 12 · 0,75 = 9 cm/s, π = 3) ortalama sürat saymış.','bilgi'),
     (12,'Genliğin sayısal değerini (12) ortalama sürat sanmış.','bilgi')]
gr=axis_opts('$t$ (s)','$x$ (cm)',0,9,-14,14,'0,1,2,3,4,5,6,7,8','-12,-6,0,6,12')+'\n\\addplot[thick,vurgu,smooth] coordinates {'+egri(f14,0,8,.5)+'};\n\\end{axis}'
SK=fig(gr)
NUM('0014','bh-grafik','orta','Konum–zaman Grafiği','Konum–zaman grafiğinden cismin aldığı yolu ve yer değiştirmesini ayırarak ortalama süratini bulur.','K-AFBHH-14 (ortalama sürat) · A = 12 cm, T = 8 s','grafik',
 'Doğrusal bir yörüngede basit harmonik hareket yapan bir cismin konum–zaman grafiği şekilde verilmiştir.\nBuna göre, cismin t = 0 ile t = 6 s arasındaki ortalama süratinin büyüklüğü kaç cm/s’dir?',
 sur14,e14,'C','Cismin 0–6 s aralığındaki ortalama sürati (cm/s).',['Cismin hangi konumlardan sırayla geçtiğini yaz; alınan yol ile yer değiştirmeyi ayır.'],[BG,BE],SK,
 [A('Konumları oku','Grafikten t = 0, 2, 4, 6 s anlarındaki konumlar okunur.','0 → +12 → 0 → −12 cm'),
  A('Alınan yolu bul','Her bir aralık bir genlik kadar yoldur.','Yol = 12 + 12 + 12 = 36 cm'),
  A('Ortalama sürati yaz','Ortalama sürat = toplam yol ÷ süre.','36 ÷ 6 = 6 cm/s')],
 'Ortalama sürat yola, ortalama hız yer değiştirmeye bağlıdır; salınımda ikisi farklıdır.')

# ================= 15 orta · eşit aralıklı noktalar (öncüllü) =================
tr15={'I':True,'II':False,'III':True}
why15={'I':'F = −kx olduğundan ivme uzanımla orantılıdır; L’nin uzanımı K’ninkinin yarısı olduğundan ivmesi de yarısıdır',
       'II':'potansiyel enerji uzanımın karesiyle orantılıdır; L’de Ep = E ÷ 4, Ek = 3E ÷ 4 olur ve Ek, Ep’ye eşit değildir',
       'III':'cisim O’dan N’ye giderken yay kuvveti hareketine zıt yönlüdür; hız büyüklüğü azalır'}
u=.9
# blok K'de olacak biçimde yeniden kur
body=zem(-3.0,3.6)+duvar(-3.9,0,1.5)+'\n'+yay(-3.9,.5,-2*u-.45,.5)+blok(-2*u,.9,.9,'m')+'\n'
for xx,lab in [(-2*u,'K'),(-u,'L'),(0,'O'),(u,'M'),(2*u,'N')]:
    body+=f'\\draw[dashed,gray] ({xx},0) -- ({xx},1.5); \\fill ({xx},0) circle (.05); \\node[below] at ({xx},-.2) {{{lab}}};\n'
body=body.replace(zem(-3.0,3.6),zem(-4.1,3.2))
SK=fig(body)
ONC('0015','bh-nitel','orta','Uzanım, Hız ve İvme','Eşit aralıklı noktalardan geçen titreşimde ivme, enerji ve hızın değişimini uzanımla ilişkilendirir.','K-AFBHH-15 (ivme ve enerji oranları)',
 'Sürtünmesiz yatay düzlemde yayın ucuna bağlı m kütleli cisim, denge konumu O olan basit harmonik hareket yapmaktadır. Şekilde K, L, O, M ve N noktaları eşit aralıklıdır; cisim K noktasından serbest bırakılmıştır.\nBuna göre, cisim için,\nI. L’den geçerken ivmesinin büyüklüğü, K’dekinin yarısıdır.\nII. L’den geçerken kinetik enerjisi, potansiyel enerjisine eşittir.\nIII. O’dan N’ye giderken sürati azalır.\nyargılarından hangileri doğrudur?',
 tr15,why15,2,'Doğru olan yargılar.',['İvmenin ve potansiyel enerjinin uzanımla nasıl orantılı olduğunu yaz.'],[BX,BE],SK,
 'İvme, enerji ve sürat uzanıma bağlı olarak değişir; bu ilişkileri hatırla.')

# ================= 16 zor · F–x grafiği, v_maks =================
F16,x16=10,Fr(20,100); k16=Fr(F16)/x16; m16=2; A16=Fr(20,100)
w16=rsq(k16/m16); v16=A16*w16
assert k16==50 and w16==5 and v16==1
e16=[(2,'ω = √(k · m) = 10 rad/s alıp v = 0,2 · 10 = 2 m/s bulmuş.','islem'),
     (5,'ω yerine k ÷ m = 25 alıp v = 0,2 · 25 = 5 m/s bulmuş.','islem'),
     (10,'Eğimi 0,5 N/cm ve genliği 20 cm bırakıp ω = √(0,5 ÷ 2) = 0,5 rad/s, v = 20 · 0,5 = 10 bulmuş.','dikkat'),
     (100,'Genliği metreye çevirmeden (20 cm) v = 20 · 5 = 100 bulmuş.','dikkat')]
assert Fr(1,5)*10==2 and Fr(1,5)*25==5 and 20*rsq(Fr(1,2)/2)==10 and 20*5==100
gr=axis_opts('$x$ (cm)','$F$ (N)',0,24,0,12,'0,4,8,12,16,20,24','0,2,4,6,8,10,12',w='6.6cm')+'\n\\addplot[thick,vurgu] coordinates {(0,0) (20,10)};\n\\addplot[only marks,mark=*,mark size=2pt,vurgu] coordinates {(20,10)};\n\\end{axis}'
SK=fig(gr)
NUM('0016','bh-enerji','zor','Yay Kuvveti ve Sürat','Yayın kuvvet–uzama grafiğinden esneklik sabitini, buradan titreşimin en büyük süratini bulur.','K-AFBHH-16 (F–x ve v_maks) · k = 50 N/m, m = 2 kg, A = 20 cm','grafik',
 'Bir yayı uzatmak için gereken F kuvvetinin yayın uzamasına (x) göre değişimi şekildeki doğrusal grafikle verilmiştir. Bu yayın ucuna 2 kg kütleli bir cisim bağlanıp sürtünmesiz yatay düzlemde, denge konumundan 20 cm uzağa çekilerek serbest bırakılıyor ve cisim basit harmonik hareket yapıyor.\nBuna göre, cismin hareketi boyunca ulaştığı en büyük sürat kaç m/s’dir?',
 v16,e16,'A','Cismin en büyük sürati (m/s).',['Grafikten yayın sabitini bul; ardından açısal frekansı ve genliği kullan.'],[BY,BE],SK,
 [A('Esneklik sabitini bul','Hooke yasası: F = k·x; grafikteki bir nokta kullanılır (20 cm = 0,2 m için 10 N).','k = 10 ÷ 0,2 = 50 N/m'),
  A('Açısal frekansı bul','ω = √(k ÷ m).','ω = √(50 ÷ 2) = 5 rad/s'),
  A('Genliği yaz','Cisim 20 cm’den bırakıldığı için genlik bu uzaklıktır.','A = 0,2 m'),
  A('En büyük sürati hesapla','Denge noktasında v_maks = A·ω.','v_maks = 0,2 · 5 = 1 m/s')],
 'v_maks = A·ω ve ω = √(k ÷ m); k, F–x grafiğinin eğimidir.')

# ================= 17 orta · frekansı artıran işlemler (öncüllü) =================
tr17={'I':False,'II':True,'III':False}
why17={'I':'periyot ve frekans genliğe bağlı değildir; genliği artırmak frekansı değiştirmez',
       'II':'özdeş bir yayı paralel bağlamak eşdeğer yay sabitini artırır ve f = (1 ÷ 2π)√(k ÷ m) bağıntısına göre frekansı artırır',
       'III':'kütleyi artırmak periyodu büyütür, frekansı azaltır'}
u=.28
body=zem(-.3,7.4)+duvar(0,0,1.5)+'\n'+yay(0,.5,2.7,.5)+blok(3.25,1.1,.9,'$m$')+'\n\\node[above] at (1.35,.8) {$k$};\n'
body+='\\draw[dashed,gray] (3.25,-.1) -- (3.25,1.5); \\node[below] at (3.25,-.2) {O};\n'
body+='\\draw[dashed,gray] (2.2,-.1) -- (2.2,1.5); \\node[below] at (2.2,-.2) {A}; \\draw[dashed,gray] (4.3,-.1) -- (4.3,1.5); \\node[below] at (4.3,-.2) {B};\n'
SK=fig(body)
ONC('0017','bh-yay','orta','Yay–kütle Sistemi','Yay–kütle sisteminin frekansını artırmak için tek başına yeterli olan işlemleri belirler.','K-AFBHH-17 (frekansı artıran işlemler)',
 'Sürtünmesiz yatay düzlemde, yayın ucuna bağlı m kütleli cisim A ile B noktaları arasında basit harmonik hareket yapmaktadır; O, denge konumudur.\n(Diğer koşullar aynı kalmaktadır.)\nBuna göre, hareketin frekansını artırmak için,\nI. cismi A noktasından daha uzak bir noktaya çekip bırakmak,\nII. yaya aynı özellikte bir yay daha paralel bağlamak,\nIII. cismin kütlesini artırmak\nişlemlerinden hangileri tek başına yapılabilir?',
 tr17,why17,1,'Frekansı artıran işlemler.',['Frekansı belirleyen niceliklerin hangileri olduğunu yaz.'],[BY,BYB],SK,
 'Frekansı yay sabiti ve kütle belirler; hangi işlemin bunlardan birini değiştirdiğine bak.')

# ================= 18 orta · seri ve paralel =================
Tr18=rsq(Fr(1,2)/Fr(2))   # T_II/T_I = sqrt(k_seri/k_paralel)
assert Tr18==Fr(1,2)
e18=[(1,'Seri ve paralel bağlı sistemlerin eşdeğer yay sabitlerini eşit sanmış.','bilgi'),
     (2,'Oranı ters yazmış: T_I ÷ T_II = 2 olur, istenen ise T_II ÷ T_I’dir.','dikkat'),
     (4,'Karekök almadan eşdeğer sabitlerin oranını (k_II ÷ k_I = 4) yazmış.','islem'),
     (16,'Eşdeğer sabitlerin oranının (4) karesini almış.','islem')]
body=zem(-.3,6.4,y=3.6)+duvar(0,3.6,5.2)+'\n'+yay(0,4.1,1.7,4.1)+yay(1.7,4.1,3.4,4.1)+blok(3.95,1.1,.9,'$m$',y=3.6)+'\n\\node[above] at (.85,4.4) {$k$}; \\node[above] at (2.55,4.4) {$k$}; \\node[right] at (4.7,4.1) {Şekil I};\n'
body+=zem(-.3,6.4,y=0)+duvar(0,0,1.8)+'\n'
body+=yay(0,.3,3.4,.3)+yay(0,.95,3.4,.95)+blok(3.95,1.1,1.25,'$m$',y=0)+'\n\\node[above] at (1.7,1.25) {$k$}; \\node[below] at (1.7,-.0) {}; \\node[right] at (4.7,.45) {Şekil II};\n'
SK=fig(body)
NUM('0018','bh-yay','orta','Yay–kütle Sistemi','Seri ve paralel bağlı özdeş yaylarla kurulan sistemlerin periyotlarını oranlar.','K-AFBHH-18 (seri / paralel) · k_seri = k÷2, k_paralel = 2k','şekilli',
 'Sürtünmesiz yatay düzlemde, esneklik sabiti k olan özdeş yaylar ve özdeş m kütleli cisimlerle iki düzenek kuruluyor: Şekil I’de iki yay seri, Şekil II’de iki yay paralel bağlanarak cisme bağlanmıştır. Cisimler denge konumlarından eşit miktarda çekilip bırakıldığında basit harmonik hareket yapmaktadır. Şekil I ve Şekil II’deki sistemlerin periyotları sırasıyla T_I ve T_II’dir.\nBuna göre, T_II ÷ T_I oranı kaçtır?',
 Tr18,e18,'A','T_II ÷ T_I oranı.',['Her düzenek için eşdeğer yay sabitini bul; periyodun k ile nasıl değiştiğini yaz.'],[BYB,BY],SK,
 [A('Eşdeğer sabitleri bul','Seri bağlamada k_eş = k ÷ 2, paralel bağlamada k_eş = 2k.','k_I = k ÷ 2, k_II = 2k'),
  A('Periyot oranını yaz','T ∝ 1 ÷ √k; kütleler eşittir.','T_II ÷ T_I = √(k_I ÷ k_II)'),
  A('Hesapla','Oranı yerine koy.','√((k ÷ 2) ÷ (2k)) = √(1 ÷ 4) = 1 ÷ 2')],
 'T ∝ 1 ÷ √k; paralelde k toplanır, seride 1 ÷ k_eş = 1 ÷ k₁ + 1 ÷ k₂.')

# ================= 19 zor · ivmeli roket =================
T19=Fr(6,5); g19=g+30; T19n=T19*rsq(Fr(9)*g/g19); assert T19n==Fr(9,5)
e19=[(Fr(3,5),'Yalnızca roketin ivmesini hesaba katıp ip uzunluğunun değiştiğini unutmuş: T = 1,2 ÷ 2 = 0,6 s.','dikkat'),
     (Fr(27,10),'İki oranı da karekök almadan uygulamış: T = 1,2 × 9 ÷ 4 = 2,7 s.','islem'),
     (Fr(18,5),'Roketin ivmesini hesaba katmayıp yalnız ip uzunluğunu uygulamış: T = 1,2 × 3 = 3,6 s.','dikkat'),
     (Fr(36,5),'Etkin yer çekimini ters yazmış: T = 1,2 × √(9 × 4) = 7,2 s.','dikkat')]
assert T19*3==Fr(18,5) and T19*Fr(9,4)==Fr(27,10) and T19*6==Fr(36,5)
body='\\draw[thick] (0,0) rectangle (4.0,4.4);\n'+tavan(.3,3.7,4.4)+'\n'
a_=14; bx=2.0+2.6*math.sin(math.radians(a_)); by=4.4-2.6*math.cos(math.radians(a_))
body+=f'\\draw[dashed,gray] (2.0,4.4) -- (2.0,{4.4-2.6}); \\draw[thick] (2.0,4.4) -- ({bx:.3f},{by:.3f}); \\draw[thick,fill=gray!50] ({bx:.3f},{by:.3f}) circle (.18);\n'
body+=vk(4.7,1.2,4.7,3.2,'','right')+'\\node[right,vurgu!70!black] at (4.75,2.5) {$\\vec a$}; \\node[right,font=\\footnotesize] at (4.75,1.8) {30 m/s²};\n'
SK=fig(body)
NUM('0019','bh-ortam','zor','İvmeli Ortamda Sarkaç','Yukarı ivmeli kabinde etkin yer çekimi ivmesini bulup sarkacın periyodunu hesaplar.','K-AFBHH-19 (g_etkin = g + a ve ℓ değişimi) · T = 1,2 s, a = 30 m/s², 9ℓ','şekilli',
 'Yer yüzünde periyodu 1,2 s olan bir basit sarkacın ipi, aynı malzemeden 9 katı uzunluğunda bir ip ile değiştirilip sarkaç şekildeki roketin kabininde tavana asılmıştır. Roket yer yüzünden fırlatıldıktan sonra düşey doğrultuda yukarı yönlü, sabit 30 m/s² ivmeyle hızlanırken sarkaç kabin içinde küçük açılı salınım yapmaktadır.\n(g = 10 m/s²; hava direnci ve sürtünmeler önemsizdir.)\nBuna göre, sarkacın bu andaki periyodu kaç saniyedir?',
 T19n,e19,'B','Sarkacın periyodu (s).',['Kabinde sarkaca etki eden etkin yer çekimi ivmesinin ne olduğunu düşün.'],[BO,BS],SK,
 [A('Etkin ivmeyi bul','Yukarı ivmeli kabinde g_etkin = g + a.','g_etkin = 10 + 30 = 40 m/s²'),
  A('Oranı yaz','T ∝ √(ℓ ÷ g_etkin); ip uzunluğu 9 katına çıkmıştır.','T′ ÷ T = √(9 × 10 ÷ 40) = 3 ÷ 2'),
  A('Yeni periyodu bul','Oranı T ile çarp.','T′ = 1,2 × 3 ÷ 2 = 1,8 s')],
 'İvmeli kabinde g yerine g_etkin alınır; yukarı ivmede g_etkin = g + a.')

# ================= 20 zor · kütle ekleme =================
m20,v20,M20,k20=1,4,3,400
w20=rsq(Fr(k20,m20)); A20=Fr(v20)/w20; vy=Fr(m20*v20,m20+M20); wy=rsq(Fr(k20,m20+M20)); Ay=vy/wy*100
assert w20==20 and A20==Fr(1,5) and vy==1 and wy==10 and Ay==10
e20=[(5,'Çarpışmadan sonra hızı 1 m/s bulup açısal frekansı eski değerle (20 rad/s) almış: A′ = 1 ÷ 20 m = 5 cm.','dikkat'),
     (20,'Genliğin değişmediğini düşünmüş: A = 4 ÷ 20 m = 20 cm.','bilgi'),
     (30,'Kütle oranını ters yazmış: v′ = 4 · 3 ÷ 4 = 3 m/s ve A′ = 3 ÷ 10 m = 30 cm.','islem'),
     (40,'Hızı eski değerinde (4 m/s) bırakıp yalnız yeni ω’yı kullanmış: A′ = 4 ÷ 10 m = 40 cm.','dikkat')]
u=.28
body=zem(-.3,7.2)+duvar(0,0,1.5)+'\n'+yay(0,.45,2.0,.45)+blok(2.55,1.1,.9,'1 kg')+'\n\\node[above] at (1.0,.75) {$k=400$ N/m};\n'
body+='\\draw[dashed,gray] (2.55,-.1) -- (2.55,3.6); \\node[below] at (2.55,-.2) {O};\n'
body+=vk(3.2,.45,4.6,.45,'4 m/s','above')+'\n'
body+='\\draw[thick,fill=gray!55] (2.55,3.0) circle (.4); \\node at (2.55,3.0) {3 kg}; '+vk(2.55,2.5,2.55,1.15,'','right','blue')+'\n'
SK=fig(body)
NUM('0020','bh-kutle','zor','Kütle Ekleme ve Momentum','Denge noktasından geçen titreşimli cisme kütle yapıştığında yeni genliği momentum korunumu ve yeni ω ile bulur.','K-AFBHH-20 (kütle ekleme) · 1 kg, 4 m/s, +3 kg, k = 400 N/m','şekilli',
 'Sürtünmesiz yatay düzlemde, esneklik sabiti 400 N/m olan yayın ucuna bağlı 1 kg kütleli cisim basit harmonik hareket yapmaktadır. Cisim, denge konumu O’dan 4 m/s süratle geçtiği anda, düşey doğrultuda yukarıdan serbestçe düşen 3 kg kütleli yapışkan bir hamur parçası cisme yapışıyor ve birlikte titreşmeye devam ediyorlar.\n(Hamurun yatay hızı sıfırdır; yapışma çok kısa sürede gerçekleşir.)\nBuna göre, yapışmadan sonraki titreşimin genliği kaç cm’dir?',
 Ay,e20,'B','Yapışmadan sonraki genlik (cm).',['Yapışma anında sistemde hangi nicelik değişmez, ω neye bağlıdır?'],[BMK,BE],SK,
 [A('Yapışma anını yaz','Yatay momentum korunur.','1 · 4 = (1 + 3) · v′ → v′ = 1 m/s'),
  A('Yeni açısal frekansı bul','ω′ = √(k ÷ (m + M)).','ω′ = √(400 ÷ 4) = 10 rad/s'),
  A('Genliği hesapla','Cisim denge noktasındadır; bu hız en büyük sürattir: v′ = A′·ω′.','A′ = 1 ÷ 10 = 0,1 m'),
  A('Birimi çevir','Metreyi santimetreye çevir.','A′ = 10 cm')],
 'Denge noktasındaki hız en büyük süratir: A′ = v′ ÷ ω′; yapışmada hız ve ω birlikte değişir.')

# ---------- bitir ----------
for q_ in P.ANA: q_['kardes']=None
SCR='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bhh/bos.json'
P.yaz(os.path.join(ADIR,'bhh-1.json'),SCR)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Fizik çıkmış soruları ve yayın soru bankaları (yalnız mantık), MEB 11. sınıf fizik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afbhh.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
