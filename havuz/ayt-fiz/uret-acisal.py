"""AYT Fizik · Eylemsizlik ve Açısal Momentum · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ; koordinatlar ve her sayı Python'da hesaplanıp assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
KONUAD='Eylemsizlik ve Açısal Momentum'
P=Parti('acisal',KONUAD,'afiz|'+KONUAD,ders='AYT Fizik',idon='aytfiz')
H.KONU=KONUAD
ALT='Eylemsizlik ve Açısal Momentum'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,'ÖSYM AYT 2018–2026 Fizik (yalnız mantık) · 345 AYT Fizik Soru Bankası · MEB 12. sınıf fizik')
def q(no,**k):
    assert len(k['ip'])==1
    mk(P,no,adim=len(k['ad']),ad=k.pop('ad'),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
DARR='{Stealth[length=1.8mm,width=1.6mm]}-{Stealth[length=1.8mm,width=1.6mm]}'
def fig(*parts): return tikz_svg(HEAD+'\n'.join(parts)+TAIL)
def onc(truth,reasons,sira):
    def kume(l): return set(('I','II','III')) if l=='I, II ve III' else set(x for x in l.replace('Yalnız ','').replace(' ve ',' ').split())
    gercek={k for k,v in truth.items() if v}
    dog=[l for l in sira if kume(l)==gercek]; assert len(dog)==1,(sira,gercek)
    yan=[]
    for l in sira:
        if l==dog[0]: continue
        k=kume(l); c=[]
        for x in ('I','II','III'):
            if x in k and x not in gercek: c.append(f'{x}. öncülü doğru saymış, oysa yanlıştır: {reasons[x]}')
            if x in gercek and x not in k: c.append(f'{x}. öncülünü yanlış saymış, oysa doğrudur: {reasons[x]}')
        yan.append((l,' '.join(c),'bilgi'))
    ad=[A(f'{x}. öncülü incele',reasons[x],f'{x}: '+('doğru' if truth[x] else 'yanlış')) for x in ('I','II','III')]
    ad.append(A('Sonuca var','Doğru öncülleri birleştir.','Doğru: '+', '.join(x for x in ('I','II','III') if truth[x])))
    return dog[0],yan,ad
S5=['Yalnız I','Yalnız II','I ve II','I ve III','II ve III']
S5b=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
B_I=B('Eylemsizlik momenti','noktasal kütlelerden oluşan sistemde I = Σ m·r² (r: kütlenin dönme eksenine dik uzaklığı) bağıntısıyla bulunur; kütleye, kütlenin dağılımına ve dönme eksenine bağlıdır, açısal hıza bağlı değildir. Örnek: 4 kg’lık bir cisim eksenden 0,5 m uzaktaysa I = 4 · 0,5² = 1 kg·m²’dir')
B_E=B('Dönme kinetik enerjisi','E = ½·I·ω² bağıntısıyla bulunur (I: eylemsizlik momenti, ω: açısal hız). Örnek: I = 6 kg·m² olan bir cisim ω = 3 rad/s ile dönerken E = ½ · 6 · 3² = 27 J’dür')
B_L=B('Açısal momentum','dönen cisimde L = I·ω, noktasal cisimde L = m·v·r (v: hızın r’ye dik bileşeni) bağıntısıyla bulunur. Dışarıdan net tork etki etmiyorsa açısal momentum korunur: I₁ω₁ = I₂ω₂. Örnek: I = 5 kg·m² ve ω = 2 rad/s ise L = 10 kg·m²/s’dir')
B_Y=B('Kaymadan yuvarlanma','kaymadan yuvarlanan cisimde v = ω·R’dir ve toplam kinetik enerji E = ½·m·v² + ½·I·ω² olur; sürtünme iş yapmaz. Örnek: m = 2 kg, v = 3 m/s ve I = ½·m·R² olan cisim için E = 9 + 4,5 = 13,5 J’dür')
B_T=B('Tork ve açısal ivme','τ = F·d ve τ = I·α bağıntıları geçerlidir; net tork, açısal momentumun değişim hızıdır (τ = ΔL/Δt). Örnek: I = 4 kg·m² olan cisme τ = 6 N·m’lik net tork etki ederse α = 1,5 rad/s² olur')
B_KOR=B('Korunum koşulu','dönme eksenine göre net dış tork sıfırsa açısal momentum korunur; iç kuvvetler (ip, sürtünme, çarpışma kuvvetleri) toplam açısal momentumu değiştirmez, ancak mekanik enerjiyi değiştirebilir. Örnek: buz üstünde dönen bir kişi kollarını kapatınca açısal momentumu aynı kalır')
# ================= KARTLAR =================
kartla('K-AFACISAL-01','Eylemsizlik momenti (nokta kütleler, kavram)','I = Σ m·r² ile hesaplanır; kütle ve eksene uzaklığın karesi belirleyicidir, açısal hıza bağlı değildir.','r’yi kare almamak; uzaklığı yanlış eksenden ölçmek; I’yı açısal hıza bağlı sanmak.','kolay','şekilli',3,'acisal-eylemsizlik','Eylemsizlik momentinin hesaplanması ve bağlı olduğu nicelikler')
kartla('K-AFACISAL-02','Dönme kinetik enerjisi','E = ½·I·ω²; grafikten okunan L ve I ile E = L²/(2I) de kullanılır.','Kareyi unutmak; ½ katsayısını atlamak; L’yi ω sanmak.','kolay','şekilli',3,'acisal-donme-ke','Dönme kinetik enerjisi')
kartla('K-AFACISAL-03','Açısal momentumun korunumu (platform, kişi, böcek)','Net dış tork yokken I₁ω₁ = I₂ω₂; I değişince ω değişir, enerji ise korunmaz.','Enerjinin korunduğunu sanmak; yalnız yarıçap oranını kullanmak; platformun I’sını atlamak.','orta','şekilli',4,'acisal-koruma','Dönen sistemde eylemsizlik momenti değişimi ve açısal momentumun korunumu')
kartla('K-AFACISAL-04','Yapışma / esnek olmayan çarpışmada açısal momentum','Ortak eksende birleşen cisimlerde L korunur; mekanik enerjinin bir kısmı ısıya dönüşür.','Enerjinin korunduğunu sanmak; yapışan cismin I’sını son duruma katmamak.','zor','şekilli',4,'acisal-yapisma','Birleşen dönen cisimlerde açısal hız ve enerji kaybı')
kartla('K-AFACISAL-05','İp çekilen cisim, çembersel hareket ve açısal momentum','Merkezden geçen kuvvet tork yapmaz; m·v·r sabit kalır, kinetik enerjideki artış çekilen iş kadardır.','v·r yerine v sabit saymak; v’yi r² ile ters orantılı almak; işi ΔE yerine E sanmak.','orta','şekilli',4,'acisal-ip-cember','Merkezi kuvvet altında hareket ve açısal momentum')
kartla('K-AFACISAL-06','Yuvarlanma enerjisi ve karşılaştırma','Kaymadan yuvarlanmada enerji öteleme ve dönmeye paylaşılır; I/(mR²) oranı büyük olan cisim daha yavaş iner.','Yuvarlanan cismi kayan cisim gibi çözmek; I = mR² varsaymak; enerji paylarını karıştırmak.','orta','öncüllü',4,'acisal-yuvarlanma','Kaymadan yuvarlanan cisimlerde enerji ve hız')
kartla('K-AFACISAL-07','Tork, açısal ivme ve makara-ip sistemi','τ = I·α ve enerji korunumu birlikte kullanılır; ip kaymadan makarayı döndürür (v = ωR).','Makaranın kinetik enerjisini atlamak; v ile ω’yı eşit almak; I = ½MR² yerine MR² kullanmak.','orta','şekilli',4,'acisal-tork-makara','Torkla açısal ivme ve makaralı sistemde enerji')
g=10
# ================= 01 · kolay · I = Σ m r² =================
u=1.5; m1,r1,m2,r2=2,1,3,2
I1=m1*r1**2+m2*r2**2; assert I1==14
d_a=m1*r1+m2*r2; d_b=m1*r1**2; d_c=m1*r2**2+m2*r1**2; d_d=m2*r2**2
assert (d_a,d_b,d_c,d_d)==(8,2,11,12) and len({I1,d_a,d_b,d_c,d_d})==5
sk=fig(f'\\draw[thick] ({-r1*u:.2f},0) -- ({r2*u:.2f},0);',
 f'\\fill[gray!55] ({-r1*u:.2f},0) circle (.2); \\fill[gray!55] ({r2*u:.2f},0) circle (.2);',
 f'\\draw ({-r1*u:.2f},0) circle (.2); \\draw ({r2*u:.2f},0) circle (.2);',
 f'\\node[above=4pt] at ({-r1*u:.2f},0) {{$2$ kg}}; \\node[above=4pt] at ({r2*u:.2f},0) {{$3$ kg}};',
 '\\draw[thick,fill=white] (0,0) circle (.13); \\fill (0,0) circle (1.3pt); \\node[above=4pt] at (0,0) {O};',
 f'\\draw[{DARR}] ({-r1*u:.2f},-.6) -- (0,-.6) node[midway,below] {{$1$ m}};',
 f'\\draw[{DARR}] (0,-.6) -- ({r2*u:.2f},-.6) node[midway,below] {{$2$ m}};',
 f'\\draw[dashed,gray] ({-r1*u:.2f},-.15) -- ({-r1*u:.2f},-.7); \\draw[dashed,gray] (0,-.15) -- (0,-.7); \\draw[dashed,gray] ({r2*u:.2f},-.15) -- ({r2*u:.2f},-.7);')
q('0001',tipId='acisal-eylemsizlik',tip='Eylemsizlik momentinin hesaplanması ve bağlı olduğu nicelikler',z='kolay',alt=ALT,kaz='Noktasal kütlelerden oluşan sistemin eylemsizlik momentini I = Σ m·r² ile hesaplar.',
 kart='K-AFACISAL-01 (I = Σmr²) · 2 kg ve 3 kg, 1 m ve 2 m',kalip='şekilli',
 metin='Kütlesi önemsiz bir çubuğun iki noktasına, boyutları önemsiz iki cisim şekildeki gibi bağlanmıştır. Sistem, çubuğun O noktasından geçen ve çubuğa dik olan sabit bir eksen etrafında dönebilmektedir.\nBuna göre, sistemin O noktasından geçen eksene göre eylemsizlik momenti kaç kg·m²’dir?',
 dogru=I1,yan=[(d_a,'Uzaklıkların karesini almamış: I = 2 · 1 + 3 · 2 = 8 kg·m².','dikkat'),(d_b,'Yalnız 2 kg’lık cismin katkısını almış: I = 2 · 1² = 2 kg·m².','bilgi'),(d_c,'Uzaklıkları iki cisme ters yazmış: I = 2 · 2² + 3 · 1² = 11 kg·m².','islem'),(d_d,'Yalnız 3 kg’lık cismin katkısını almış: I = 3 · 2² = 12 kg·m².','dikkat')],
 istenen='Sistemin O eksenine göre eylemsizlik momenti (kg·m²).',ip=['Her cismin dönme eksenine olan dik uzaklığını belirleyip katkıları ayrı ayrı bulmayı dene.'],
 bilgi=[B_I],
 ad=[A('Uzaklıkları oku','Şekilde 2 kg’lık cisim eksene 1 m, 3 kg’lık cisim 2 m uzaktadır.','r₁ = 1 m, r₂ = 2 m'),A('Her cisim için m·r² yaz','Eylemsizlik momenti nokta kütlelerde Σ m·r²’dir.','I₁ = 2 · 1² = 2, I₂ = 3 · 2² = 12'),A('Topla','Katkılar toplanır.','I = 2 + 12 = 14 kg·m²')],
 puf='Eylemsizlik momentinde uzaklığın karesi alınır; eksene uzak kütle çok daha fazla katkı yapar.',sekil=sk)
# ================= 02 · kolay · öncüllü kavram =================
tr={'I':True,'II':False,'III':False}
rs={'I':'Eylemsizlik momenti I = Σ m·r² olduğundan cismin kütlesine bağlıdır.','II':'Eylemsizlik momenti cismin o anki açısal hızına bağlı değildir; ω değişse de I değişmez.','III':'Dönme kinetik enerjisi ½·I·ω² ile I’dan hesaplanan bir sonuçtur; enerji değişse de I kendiliğinden değişmez.'}
d,y,ad=onc(tr,rs,S5)
q('0002',tipId='acisal-eylemsizlik',tip='Eylemsizlik momentinin hesaplanması ve bağlı olduğu nicelikler',z='kolay',alt=ALT,kaz='Eylemsizlik momentinin bağlı olduğu ve olmadığı nicelikleri ayırt eder.',
 kart='K-AFACISAL-01 (I kavramı) · öncüllü',kalip='öncüllü',
 metin='Sabit bir eksen etrafında dönebilen katı bir cismin bu eksene göre eylemsizlik momenti I ile gösteriliyor.\nBuna göre, I niceliği;\nI. cismin kütlesine,\nII. cismin açısal hızına,\nIII. cismin dönme kinetik enerjisine\nniceliklerinden hangilerine bağlıdır?',
 dogru=d,yan=y,sira=S5,istenen='I’nın bağlı olduğu nicelikler.',ip=['Eylemsizlik momentini veren bağıntıda hangi niceliklerin yer aldığına bak.'],
 bilgi=[B_I],ad=ad,puf='Eylemsizlik momentinin hangi büyüklüklerle tanımlandığını hatırla.')
# ================= 03 · kolay · E = ½ I ω² =================
Id=Fr(2,5); w3=10; E3=Id*w3**2/2; assert E3==20
dd=[Id*w3,Id*w3**2,Id*w3/2,(Id*w3)**2/2]; assert dd==[4,40,2,8] and len({E3,*dd})==5
sk=fig('\\draw[thick,fill=gray!18] (0,0) circle (1.35); \\draw[thin,gray] (0,0) circle (.9);',
 '\\fill (0,0) circle (1.6pt);',
 '\\draw[vurgu,very thick,-{Stealth[length=2.2mm,width=2mm]}] (1.75,-.75) arc[start angle=-23,end angle=45,radius=1.9];',
 '\\node[vurgu] at (2.95,.45) {$\\omega=10$ rad/s};',
 '\\node at (0,.3) {Disk}; \\node at (0,-1.75) {$I=0{,}4$ kg$\\cdot$m$^2$};')
q('0003',tipId='acisal-donme-ke',tip='Dönme kinetik enerjisi',z='kolay',alt=ALT,kaz='Eylemsizlik momenti ve açısal hızı verilen cismin dönme kinetik enerjisini hesaplar.',
 kart='K-AFACISAL-02 (E = ½Iω²) · I = 0,4 kg·m², ω = 10 rad/s',kalip='şekilli',
 metin='Merkezinden geçen sabit bir eksen etrafında dönen disk şekilde gösterilmiştir. Diskin bu eksene göre eylemsizlik momenti ve açısal hızı şekilde verilmiştir.\nBuna göre, diskin dönme kinetik enerjisi kaç J’dür?',
 dogru=20,yan=[(2,'Enerjiyi E = ½·I·ω olarak almış (ω’nın karesini almamış): ½ · 0,4 · 10 = 2 J.','dikkat'),(4,'Enerji yerine açısal momentumu (I·ω = 0,4 · 10) hesaplamış.','bilgi'),(8,'Açısal momentumun karesinin yarısını almış: ½ · (0,4 · 10)² = 8 J.','islem'),(40,'½ katsayısını atlamış: I·ω² = 0,4 · 100 = 40 J.','dikkat')],
 istenen='Diskin dönme kinetik enerjisi (J).',ip=['Dönme kinetik enerjisini veren bağıntıda açısal hızın nasıl yer aldığına dikkat et.'],
 bilgi=[B_E],
 ad=[A('Bağıntıyı yaz','Dönme kinetik enerjisi eylemsizlik momenti ve açısal hızın karesine bağlıdır.','E = ½·I·ω²'),A('Değerleri yerine koy','Şekildeki değerleri kullan.','E = ½ · 0,4 · 10²'),A('Hesapla','Çarpımı yap.','E = 20 J')],
 puf='Dönme kinetik enerjisi, öteleme kinetik enerjisinin dönmedeki karşılığıdır: m yerine I, v yerine ω gelir.',sekil=sk)
# ================= 04 · orta · platform, cisimler yaklaşır =================
Ip0=2; mm=1; ra,rb=2,1; w0=2
Ia=Ip0+2*mm*ra**2; Ib=Ip0+2*mm*rb**2; w4=Fr(Ia*w0,Ib); assert (Ia,Ib,w4)==(10,4,5)
x1=w0*ra/rb; x2=w0*Fr(Ib,Ia); x3='√10'
assert (x1,x2)==(4,Fr(4,5)) and w0*w0*Ia==Ib*10 and len({w4,w0,x1,x2})==4  # E korunur: ½·10·4 = ½·4·ω² → ω² = 10
def turn(cx,r,tit,rl,u=.8):
    s=[f'\\fill[gray!35] ({cx-2.1:.2f},-.12) rectangle ({cx+2.1:.2f},.04); \\draw[thick] ({cx-2.1:.2f},-.12) rectangle ({cx+2.1:.2f},.04);',
       f'\\draw[thick] ({cx:.2f},-.12) -- ({cx:.2f},-.6); \\draw[thick] ({cx-.5:.2f},-.6) -- ({cx+.5:.2f},-.6);',
       f'\\draw[dashed,gray] ({cx:.2f},.04) -- ({cx:.2f},.95);']
    for sg in (-1,1):
        x=cx+sg*r*u
        s.append(f'\\draw[thick,fill=gray!60] ({x-.17:.2f},.04) rectangle ({x+.17:.2f},.38);')
    s.append(f'\\draw[{DARR}] ({cx:.2f},.95) -- ({cx+r*u:.2f},.95) node[midway,above] {{{rl}}};')
    s.append(f'\\draw[dashed,gray] ({cx+r*u:.2f},.4) -- ({cx+r*u:.2f},1.0);')
    s.append(f'\\draw[vurgu,thick,-{{Stealth[length=2mm,width=1.8mm]}}] ({cx-.7:.2f},1.75) to[bend left=40] ({cx+.7:.2f},1.75);')
    s.append(f'\\node[vurgu] at ({cx:.2f},2.2) {{$\\omega$}}; \\node at ({cx:.2f},-1.0) {{{tit}}};')
    return s
sk=fig(*turn(0,ra,'I. durum','$r_1=2$ m'),*turn(5.2,rb,'II. durum','$r_2=1$ m'))
q('0004',tipId='acisal-koruma',tip='Dönen sistemde eylemsizlik momenti değişimi ve açısal momentumun korunumu',z='orta',alt=ALT,kaz='Platform üzerindeki cisimlerin eksene yaklaşmasında eylemsizlik momenti değişimini ve açısal momentumun korunumunu birlikte kullanır.',
 kart='K-AFACISAL-03 (platform) · I₀ = 2 kg·m², 1 kg’lık iki cisim, 2 m → 1 m',kalip='şekilli',
 metin='Düşey eksen etrafında sürtünmesiz dönebilen platformun eksene göre eylemsizlik momenti 2 kg·m²’dir. Platformun üzerinde, eksenin iki yanında ve eksene eşit uzaklıkta bulunan 1 kg kütleli iki cisim şekil I’deki konumdayken sistem 2 rad/s’lik açısal hızla dönmektedir. Cisimler, platform dönerken eksene doğru kaydırılarak şekil II’deki konuma getiriliyor.\nBuna göre, sistemin II. durumdaki açısal hızı kaç rad/s’dir?',
 dogru='5',yan=[('2','Açısal hızın değişmediğini sanmış; oysa eylemsizlik momenti azaldığı için açısal hız artar.','bilgi'),('4','Açısal hızı yarıçapla ters orantılı almış: 2 · (2 ÷ 1) = 4 rad/s.','dikkat'),('0,8','Eylemsizlik momentleri oranını ters yazmış: 2 · (4 ÷ 10) = 0,8 rad/s.','dikkat'),('√10','Dönme kinetik enerjisinin korunduğunu sanmış: ½ · 10 · 2² = ½ · 4 · ω² → ω = √10 rad/s.','islem')],
 sira=['0,8','2','√10','4','5'],
 istenen='II. durumdaki açısal hız (rad/s).',ip=['Platform ve cisimlerden oluşan sistemin eylemsizlik momentini iki durum için ayrı ayrı bulup hangi niceliğin korunduğunu düşün.'],
 bilgi=[B_I,B_L],
 ad=[A('I. durumdaki I','Platform ve iki cismin katkıları toplanır.','I₁ = 2 + 2 · 1 · 2² = 10 kg·m²'),A('II. durumdaki I','Cisimler eksene 1 m yaklaşmıştır.','I₂ = 2 + 2 · 1 · 1² = 4 kg·m²'),A('Korunumu yaz','Net dış tork olmadığından açısal momentum korunur.','I₁ω₁ = I₂ω₂ → 10 · 2 = 4 · ω₂'),A('Çöz','Eşitliği ω₂ için çöz.','ω₂ = 5 rad/s')],
 puf='Sistemin eylemsizlik momenti azalırsa korunan açısal momentum nedeniyle açısal hız artar.',sekil=sk)
# ================= 05 · orta · zıt yönlü dönen iki disk, ortak ω =================
IA,wA,IB,wB=2,6,1,9
Lt=IA*wA-IB*wB; wf=Fr(Lt,IA+IB); assert (Lt,wf)==(3,1)
c1=Fr(IA*wA+IB*wB,IA+IB); c2=Fr(wA+wB,2); c3=Lt; c4=wA+wB
assert (c1,c2,c3,c4)==(7,Fr(15,2),3,15) and len({wf,c1,c2,c3,c4})==5
sk=fig('\\draw[thick] (0,-.3) -- (0,3.1);',
 '\\fill[gray!45] (-1.3,.2) rectangle (1.3,.5); \\draw[thick] (-1.3,.2) rectangle (1.3,.5);',
 '\\node at (-1.75,.35) {A};',
 '\\draw[vurgu,thick,-{Stealth[length=2mm,width=1.8mm]}] (-.8,.85) to[bend left=40] (.8,.85); \\node[vurgu] at (1.9,1.0) {$\\omega_A=6$ rad/s};',
 '\\node[right] at (1.45,.35) {$I_A=2$ kg$\\cdot$m$^2$};',
 '\\draw[thick,dashed,fill=gray!15] (-.8,2.0) rectangle (.8,2.3);',
 '\\node at (-1.25,2.15) {B}; \\node[right] at (1.0,2.15) {$I_B=1$ kg$\\cdot$m$^2$};',
 '\\draw[vurgu,thick,-{Stealth[length=2mm,width=1.8mm]}] (.8,2.65) to[bend right=40] (-.8,2.65); \\node[vurgu] at (1.9,2.75) {$\\omega_B=9$ rad/s};',
 '\\draw[thick,-{Stealth[length=2mm,width=1.8mm]}] (-1.9,1.9) -- (-1.9,.7);')
q('0005',tipId='acisal-yapisma',tip='Birleşen dönen cisimlerde açısal hız ve enerji kaybı',z='orta',alt=ALT,kaz='Zıt yönlerde dönen iki diskin birleşmesinde açısal momentumun vektörel korunumundan ortak açısal hızı bulur.',
 kart='K-AFACISAL-04 (zıt yönlü diskler) · I_A = 2, ω_A = 6, I_B = 1, ω_B = 9',kalip='şekilli',
 metin='Sürtünmesiz düşey bir eksen etrafında dönen A diskinin üstünde, aynı eksen etrafında A’ya göre zıt yönde dönen B diski şekildeki gibi bulunmaktadır. B diski serbest bırakılıyor; iki disk birbirine temas edip kısa sürede yapışarak ortak açısal hızla dönmeye başlıyor.\nBuna göre, birleşik sistemin açısal hızının büyüklüğü kaç rad/s’dir?',
 dogru=wf,yan=[(c1,'İki diskin aynı yönde döndüğünü sanmış: (2 · 6 + 1 · 9) ÷ 3 = 7 rad/s.','bilgi'),(Fr(15,2),'Açısal hızların aritmetik ortalamasını almış: (6 + 9) ÷ 2 = 7,5 rad/s.','dikkat'),(3,'Toplam açısal momentumu (3 kg·m²/s) toplam eylemsizlik momentine bölmeden açısal hız sanmış.','dikkat'),(15,'Açısal hızları toplamış: 6 + 9 = 15 rad/s.','islem')],
 istenen='Birleşik sistemin açısal hızının büyüklüğü (rad/s).',ip=['Dönme yönlerini işaretle göstererek sistemin toplam açısal momentumunu yaz.'],
 bilgi=[B_L,B_KOR],
 ad=[A('A’nın açısal momentumu','A’nın dönme yönünü pozitif al.','L_A = 2 · 6 = +12 kg·m²/s'),A('B’nin açısal momentumu','B zıt yönde döndüğünden işareti negatiftir.','L_B = −(1 · 9) = −9 kg·m²/s'),A('Toplam L','Net dış tork olmadığından toplam açısal momentum korunur.','L = 12 − 9 = 3 kg·m²/s'),A('Ortak açısal hız','Birleşik sistemin eylemsizlik momenti I_A + I_B’dir.','ω = 3 ÷ (2 + 1) = 1 rad/s')],
 puf='Açısal momentum vektörel bir niceliktir; zıt yönlü dönmelerde büyüklükler değil işaretli değerler toplanır.',sekil=sk)
# ================= 06 · orta · öncüllü, kollar açılıyor =================
def man(cx,out,tit):
    s=[f'\\fill[gray!40] ({cx-.8:.2f},-.12) rectangle ({cx+.8:.2f},0); \\draw[thick] ({cx-.8:.2f},-.12) rectangle ({cx+.8:.2f},0);',
       f'\\draw[thick] ({cx:.2f},-.12) -- ({cx:.2f},-.5); \\draw[thick] ({cx-.4:.2f},-.5) -- ({cx+.4:.2f},-.5);',
       f'\\draw[very thick] ({cx:.2f},0) -- ({cx:.2f},1.25); \\draw[thick,fill=white] ({cx:.2f},1.5) circle (.2);']
    for sg in (-1,1):
        ex=cx+sg*(1.15 if out else .38); ey=1.0 if out else .62
        s.append(f'\\draw[very thick] ({cx:.2f},1.05) -- ({ex:.2f},{ey:.2f}); \\draw[thick,fill=gray!65] ({ex:.2f},{ey:.2f}) circle (.14);')
    s.append(f'\\draw[vurgu,thick,-{{Stealth[length=2mm,width=1.8mm]}}] ({cx-.55:.2f},2.1) to[bend left=40] ({cx+.55:.2f},2.1);')
    s.append(f'\\node at ({cx:.2f},-.9) {{{tit}}};')
    return s
sk=fig(*man(0,False,'I. durum'),*man(3.8,True,'II. durum'))
tr={'I':True,'II':False,'III':True}
rs={'I':'Net dış tork sıfır olduğundan sistemin açısal momentumu korunur.','II':'Eylemsizlik momenti arttığı için L = I·ω sabit kalırken açısal hız azalır.','III':'E = L² ÷ (2I) olduğundan L sabitken I arttıkça dönme kinetik enerjisi azalır.'}
d,y,ad=onc(tr,rs,S5)
q('0006',tipId='acisal-koruma',tip='Dönen sistemde eylemsizlik momenti değişimi ve açısal momentumun korunumu',z='orta',alt=ALT,kaz='Dönen sistemde kütlelerin eksenden uzaklaşmasının açısal momentum, açısal hız ve dönme kinetik enerjisine etkisini yorumlar.',
 kart='K-AFACISAL-03 (kollar açılıyor) · öncüllü',kalip='öncüllü',
 metin='Sürtünmesiz biçimde dönebilen bir sandalyede oturan bir kişi, ellerinde birer ağırlık tutarak I. durumdaki gibi dönmektedir. Kişi, dönmeye devam ederken kollarını açarak II. durumdaki konuma getiriyor.\nBuna göre, I. durumdan II. duruma geçerken kişi, sandalye ve ağırlıklardan oluşan sistem için;\nI. Dönme eksenine göre açısal momentum değişmez.\nII. Açısal hız artar.\nIII. Dönme kinetik enerjisi azalır.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5,istenen='Doğru olan yargılar.',ip=['Kollar açılırken eylemsizlik momentinin nasıl değiştiğini ve sisteme dışarıdan tork gelip gelmediğini incele.'],
 bilgi=[B_L,B_E],ad=ad,puf='Kollar açılırken eylemsizlik momentinin nasıl değiştiğine ve dışarıdan tork olup olmadığına bak.',sekil=sk)
# ================= 07 · orta · ip çekilen cisim, iş =================
mb,rA,vA,rB=2,1,4,Fr(1,2)
vB=Fr(mb*vA*rA,mb*rB); W7=Fr(mb*vB**2,2)-Fr(mb*vA**2,2); assert vB==8 and W7==48
e1=Fr(mb*vA**2,2); e2=Fr(mb*vB**2,2); e3=e1+e2; e4=mb*(vB**2-vA**2)
assert (e1,e2,e3,e4)==(16,64,80,96) and len({W7,e1,e2,e3,e4})==5
sk=fig('\\draw[dashed,gray] (0,0) circle (2.0); \\draw[dashed,gray] (0,0) circle (1.0);',
 '\\draw[thick] (0,0) -- (0,2.0);',
 '\\draw[thick,fill=white] (0,0) circle (.09); \\node[below left=2pt] at (0,0) {O (delik)};',
 '\\draw[thick,fill=gray!60] (0,2.0) circle (.2);',
 '\\draw[vurgu,very thick,-{Stealth[length=2.2mm,width=2mm]}] (-.3,2.0) -- (-1.6,2.0); \\node[vurgu,above] at (-1.2,2.2) {$v_1=4$ m/s};',
 '\\node[right] at (.08,1.4) {$r_1=1$ m};',
 '\\draw[thin] (0,0) -- (.707,-.707); \\node[right] at (.75,-.75) {$r_2=0{,}5$ m};')
q('0007',tipId='acisal-ip-cember',tip='Merkezi kuvvet altında hareket ve açısal momentum',z='orta',alt=ALT,kaz='İpin ucundaki cismin yarıçapı değişirken açısal momentumun korunumunu ve yapılan işin kinetik enerji değişimine eşitliğini kullanır.',
 kart='K-AFACISAL-05 (ip çekme) · m = 2 kg, 1 m → 0,5 m',kalip='şekilli',
 metin='Sürtünmesiz yatay bir masanın üzerinde, 2 kg kütleli boyutları önemsiz bir cisim hafif bir ipin ucuna bağlanmıştır. İpin diğer ucu masadaki O deliğinden geçirilmiştir. Cisim, O noktası merkezli çember üzerinde şekildeki gibi dönerken ip, delikten aşağıya doğru yavaşça çekilerek yörünge yarıçapı 1 m’den 0,5 m’ye düşürülüyor.\nBuna göre, ipi çeken kuvvetin yaptığı iş kaç J’dür?',
 dogru=48,yan=[(16,'Yalnız cismin ilk kinetik enerjisini (½ · 2 · 4²) iş olarak almış.','dikkat'),(64,'Yalnız cismin son kinetik enerjisini (½ · 2 · 8²) iş olarak almış.','dikkat'),(80,'İlk ve son kinetik enerjileri toplamış: 16 + 64 = 80 J.','bilgi'),(96,'Kinetik enerji farkında ½ katsayısını unutmuş: 2 · (8² − 4²) = 96 J.','islem')],
 istenen='İpi çeken kuvvetin yaptığı iş (J).',ip=['İp kuvvetinin O noktasına göre torkunu düşünüp cismin son hızını bulmak için hangi niceliğin sabit kaldığını belirle.'],
 bilgi=[B_L,B('İş–enerji ilişkisi','cisme etki eden net kuvvetin yaptığı iş, kinetik enerji değişimine eşittir (W = ΔE_k). Örnek: kütlesi 3 kg olan bir cismin hızı 2 m/s’den 4 m/s’ye çıkarsa W = ½ · 3 · (16 − 4) = 18 J’dür')],
 ad=[A('Korunan niceliği belirle','İp kuvveti O’dan geçtiği için tork sıfırdır; m·v·r sabittir.','v₁ · r₁ = v₂ · r₂ → 4 · 1 = v₂ · 0,5'),A('Son hızı bul','Eşitliği çöz.','v₂ = 8 m/s'),A('Kinetik enerjileri hesapla','Başlangıç ve sondaki enerjiler.','E₁ = ½ · 2 · 4² = 16 J, E₂ = ½ · 2 · 8² = 64 J'),A('İşi bul','Yapılan iş enerji artışına eşittir.','W = 64 − 16 = 48 J')],
 puf='İp kuvvetinin O noktasına göre torkunun ne olduğunu düşün.',sekil=sk)
# ================= 08 · orta · eğik düzlem, yuvarlanan silindir, h =================
v8=4
h8=Fr(3*v8**2,4*g); assert h8==Fr(6,5)
y1=Fr(v8**2,2*g); y2=Fr(v8**2,g); y3=Fr(v8**2,4*g); y4=Fr(5*v8**2,4*g)
assert (y1,y2,y3,y4)==(Fr(4,5),Fr(8,5),Fr(2,5),2) and len({h8,y1,y2,y3,y4})==5
dxn,dyn=4.5,-2.0; Ln=(dxn**2+dyn**2)**.5; dx,dy=dxn/Ln,dyn/Ln; nx,ny=-dy,dx; rr=.3; sc=.55
cxy=(dx*sc+nx*rr,2.0+dy*sc+ny*rr)
sk=fig('\\fill[gray!35] (-.5,-.2) rectangle (6.3,0); \\draw[thick] (-.5,0) -- (6.3,0);',
 '\\draw[thick] (0,0) -- (0,2.0) -- (4.5,0) -- cycle;',
 f'\\draw[thick,fill=gray!30] ({cxy[0]:.3f},{cxy[1]:.3f}) circle ({rr}); \\draw[thick] ({cxy[0]:.3f},{cxy[1]:.3f}) -- ({cxy[0]+rr*.7:.3f},{cxy[1]+rr*.7:.3f}); \\fill ({cxy[0]:.3f},{cxy[1]:.3f}) circle (1.2pt);',
 f'\\draw[{DARR}] (-.4,0) -- (-.4,2.0) node[midway,left] {{$h$}};',
 '\\draw[dashed,gray] (-.4,2.0) -- (0,2.0);',
 '\\draw[vurgu,very thick,-{Stealth[length=2.2mm,width=2mm]}] (4.7,.9) -- (5.9,.9); \\node[vurgu,above] at (5.3,1.0) {$v=4$ m/s}; \\node[below] at (5.3,.85) {\\scriptsize tabanda};')
q('0008',tipId='acisal-yuvarlanma',tip='Kaymadan yuvarlanan cisimlerde enerji ve hız',z='orta',alt=ALT,kaz='Kaymadan yuvarlanan dolu silindirde enerjinin öteleme ve dönmeye paylaşımını kullanarak bırakıldığı yüksekliği bulur.',
 kart='K-AFACISAL-06 (yuvarlanma enerjisi) · I = ½mR², v = 4 m/s',kalip='şekilli',
 metin='Kütlesi m, yarıçapı R olan dolu bir silindir, şekildeki eğik düzlemin üst ucundan durgun hâlde serbest bırakılıyor ve kaymadan yuvarlanarak ilerliyor. Silindirin eksenine göre eylemsizlik momenti I = ½·m·R²’dir. Silindirin eğik düzlemin tabanındaki kütle merkezi hızı şekilde verilmiştir. Hava direnci önemsizdir; g = 10 m/s²’dir.\nBuna göre, silindirin bırakıldığı h yüksekliği kaç m’dir?',
 dogru=h8,yan=[(y1,'Silindiri kayan bir cisim gibi ele almış: m·g·h = ½·m·v² → h = 16 ÷ 20 = 0,8 m.','dikkat'),(y2,'Silindirin eylemsizlik momentini I = m·R² almış: m·g·h = m·v² → h = 16 ÷ 10 = 1,6 m.','bilgi'),(y3,'Yalnız dönme kinetik enerjisini (¼·m·v²) alıp ağırlığın yaptığı işe eşitlemiş: h = 16 ÷ 40 = 0,4 m.','dikkat'),(y4,'Öteleme enerjisini ½·m·v² yerine m·v² yazmış: m·g·h = m·v² + ¼·m·v² → h = 2 m.','islem')],
 istenen='Silindirin bırakıldığı yükseklik h (m).',ip=['Kaymadan yuvarlanan cismin tabandaki toplam kinetik enerjisinin hangi iki biçimden oluştuğunu düşün.'],
 bilgi=[B_Y,B('Enerji korunumu','sürtünme kuvveti kaymadan yuvarlanmada iş yapmadığından mekanik enerji korunur: m·g·h = toplam kinetik enerji. Örnek: g = 10 m/s² için 2 kg’lık bir cisim 5 m yükseklikten kayarak inerse tabandaki kinetik enerjisi 100 J’dür')],
 ad=[A('ω ile v ilişkisini kur','Kaymadan yuvarlanmada ω = v ÷ R’dir.','½·I·ω² = ½ · ½·m·R² · (v²/R²) = ¼·m·v²'),A('Toplam kinetik enerji','Öteleme ve dönme enerjileri toplanır.','E = ½·m·v² + ¼·m·v² = ¾·m·v²'),A('Enerji korunumu','Ağırlığın yaptığı iş toplam kinetik enerjiye eşittir.','m·g·h = ¾·m·v²'),A('h’yi bul','Değerleri yerine koy.','h = 3 · 16 ÷ (4 · 10) = 1,2 m')],
 puf='Yuvarlanan cismin enerjisi iki yere gider; bu yüzden aynı yükseklikten kayan cisme göre tabandaki kütle merkezi hızı daha küçüktür.',sekil=sk)
# ================= 09 · orta · öncüllü, K L M yuvarlanma =================
KK,KL,KM=Fr(2,5),Fr(1,2),Fr(1)
vv={n:Fr(2,1)/(1+k) for n,k in (('K',KK),('L',KL),('M',KM))}   # v² / (g h)
rot={n:k/(1+k) for n,k in (('K',KK),('L',KL),('M',KM))}        # E_rot / (m g h)
assert max(vv,key=vv.get)=='K' and max(rot,key=rot.get)=='M' and rot['M']==Fr(1,2)
tr={'I':False,'II':True,'III':True}
rs={'I':'Hız karesi v² = 2gh ÷ (1 + I/(mR²)) olduğundan I/(mR²) en küçük olan K (dolu küre) en hızlıdır; L en hızlı değildir.','II':'Dönme enerjisi payı I/(mR²) ÷ (1 + I/(mR²)) olup halka M için ½ ile en büyüktür.','III':'Üç cisim de aynı yükseklikten ve enerji kaybı olmadan indiğinden tabandaki toplam kinetik enerjileri eşit ve m·g·h’tır.'}
d,y,ad=onc(tr,rs,S5)
def slope3(ax,lab,kind):
    w,hh=2.0,1.3; o=[]
    o.append(f'\\draw[thick] ({ax:.2f},0) -- ({ax:.2f},{hh}) -- ({ax+w:.2f},0) -- cycle;')
    Ln=(w**2+hh**2)**.5; dx,dy=w/Ln,-hh/Ln; nx,ny=-dy,dx; rr=.22; sc=.35
    cx0=ax+dx*sc+nx*rr; cy0=hh+dy*sc+ny*rr
    if kind=='K': o.append(f'\\draw[thick,fill=gray!55] ({cx0:.3f},{cy0:.3f}) circle ({rr});')
    if kind=='L': o.append(f'\\draw[thick,fill=gray!25] ({cx0:.3f},{cy0:.3f}) circle ({rr}); \\draw[thin] ({cx0:.3f},{cy0:.3f}) circle ({rr*.45});')
    if kind=='M': o.append(f'\\draw[thick,fill=white] ({cx0:.3f},{cy0:.3f}) circle ({rr}); \\draw[thick] ({cx0:.3f},{cy0:.3f}) circle ({rr*.7});')
    o.append(f'\\draw[{DARR}] ({ax-.3:.2f},0) -- ({ax-.3:.2f},{hh}) node[midway,left] {{$h$}};')
    o.append(f'\\node[below] at ({ax+w/2:.2f},-.12) {{{lab}}};')
    return o
sk=fig('\\fill[gray!35] (-.6,-.2) rectangle (8.4,0); \\draw[thick] (-.6,0) -- (8.4,0);',*slope3(0,'K','K'),*slope3(3.0,'L','L'),*slope3(6.0,'M','M'))
q('0009',tipId='acisal-yuvarlanma',tip='Kaymadan yuvarlanan cisimlerde enerji ve hız',z='orta',alt=ALT,kaz='Kaymadan yuvarlanan farklı cisimlerin hız ve enerji paylarını eylemsizlik momentleri üzerinden karşılaştırır.',
 kart='K-AFACISAL-06 (K, L, M karşılaştırma) · öncüllü',kalip='öncüllü',
 metin='Kütleleri ve yarıçapları eşit olan; dolu küre (K), dolu silindir (L) ve ince halka (M), özdeş eğik düzlemlerin aynı h yüksekliğindeki ucundan durgun hâlde serbest bırakılıyor. Üç cisim de kaymadan yuvarlanarak tabana ulaşıyor. Eylemsizlik momentleri sırasıyla I_K = 2/5·m·R², I_L = ½·m·R² ve I_M = m·R²’dir.\nBuna göre;\nI. Tabana en büyük hızla ulaşan L’dir.\nII. Tabana vardıklarında dönme kinetik enerjisi en büyük olan M’dir.\nIII. Tabana vardıklarında üçünün toplam kinetik enerjileri eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5,istenen='Doğru olan yargılar.',ip=['Her cismin kaymadan yuvarlanırken kinetik enerjisini nasıl paylaştırdığını I/(mR²) oranı üzerinden karşılaştır.'],
 bilgi=[B_Y],ad=ad,puf='I/(mR²) oranı büyüdükçe enerjinin öteleme ve dönmeye paylaşımının nasıl değiştiğini düşün.',sekil=sk)
# ================= 10 · orta · öncüllü, çembersel hareket L =================
tr={'I':True,'II':True,'III':True}
rs={'I':'Düzgün çembersel harekette v ve r sabit olduğundan L = m·v·r’nin büyüklüğü sabittir.','II':'L = r × p vektörel çarpımı r ve v’nin oluşturduğu düzleme (çember düzlemine) diktir.','III':'v sabit tutulup r iki katına çıkarılırsa L = m·v·r iki katına çıkar.'}
d,y,ad=onc(tr,rs,S5b)
q('0010',tipId='acisal-ip-cember',tip='Merkezi kuvvet altında hareket ve açısal momentum',z='orta',alt=ALT,kaz='Çembersel hareket yapan cismin açısal momentumunun büyüklüğünü, yönünü ve bağlı olduğu niceliklerini yorumlar.',
 kart='K-AFACISAL-05 (çembersel hareket) · öncüllü',kalip='öncüllü',
 metin='Sürtünmesiz yatay bir düzlemde, hafif bir ipin ucuna bağlı m kütleli bir cisim, ipin diğer ucundaki sabit O noktası etrafında v büyüklüğündeki sabit hızla düzgün çembersel hareket yapmaktadır. Yörünge yarıçapı r’dir.\nBuna göre, cismin O noktasına göre açısal momentumu için;\nI. Büyüklüğü zamanla değişmez.\nII. Yönü, yörünge düzlemine diktir.\nIII. Hız büyüklüğü v sabit kalacak biçimde yarıçap 2r yapılırsa büyüklüğü iki katına çıkar.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5b,istenen='Doğru olan yargılar.',ip=['Noktasal cismin açısal momentumunu veren bağıntıyı yazıp her büyüklüğün bu bağıntıda nasıl yer aldığına bak.'],
 bilgi=[B_L],ad=ad,puf='Vektörel çarpımın yönünün nasıl bulunduğunu hatırla.')
# ================= 11 · orta · grafik L–t =================
I11=3; L6=6
w11=Fr(L6,I11); E11=Fr(L6**2,2*I11); assert (w11,E11)==(2,6)
g1=Fr(I11*w11,2); g2=Fr(L6**2,I11); g3=Fr(L6**2,2); g4=Fr(12**2,2*I11)
assert (g1,g2,g3,g4)==(3,12,18,24) and len({E11,g1,g2,g3,g4})==5
sk=fig('\\begin{axis}[width=6.8cm,height=5.2cm,xmin=0,xmax=8,ymin=0,ymax=15,xtick distance=1,ytick={0,3,6,9,12,15},grid=both,major grid style={gray!55,thin},tick label style={font=\\small},axis lines=left,xlabel={$t$ (s)},ylabel={$L$ (kg$\\cdot$m$^2$/s)},xlabel style={font=\\small},ylabel style={font=\\small}]',
 '\\addplot[thick,vurgu] coordinates {(0,0) (2,12) (5,12) (7,0)};','\\end{axis}')
q('0011',tipId='acisal-donme-ke',tip='Dönme kinetik enerjisi',z='orta',alt=ALT,kaz='Açısal momentum–zaman grafiğinden okunan L değeri ve eylemsizlik momentiyle dönme kinetik enerjisini hesaplar.',
 kart='K-AFACISAL-02 (E = L²/2I, grafik) · I = 3 kg·m², t = 6 s',kalip='grafik',
 metin='Sabit bir eksen etrafında dönen, eylemsizlik momenti 3 kg·m² olan ve değişmeyen bir cismin eksene göre açısal momentumunun zamana göre değişimi şekildeki grafikte verilmiştir.\nBuna göre, cismin t = 6 s anındaki dönme kinetik enerjisi kaç J’dür?',
 dogru=6,yan=[(3,'Enerjiyi E = ½·I·ω olarak almış (ω’nın karesini atlamış): ½ · 3 · 2 = 3 J.','dikkat'),(12,'½ katsayısını unutmuş: E = L² ÷ I = 36 ÷ 3 = 12 J.','dikkat'),(18,'Eylemsizlik momentini hesaba katmamış: E = ½ · L² = ½ · 6² = 18 J.','bilgi'),(24,'Grafikteki en büyük değeri (L = 12) okumuş: E = 12² ÷ (2 · 3) = 24 J.','islem')],
 istenen='t = 6 s anındaki dönme kinetik enerjisi (J).',ip=['Önce grafikten istenen andaki açısal momentum değerini oku; sonra bu değerden açısal hıza geç.'],
 bilgi=[B_L,B_E],
 ad=[A('L değerini oku','t = 6 s, grafikte azalan doğru parçasının üzerindedir; 5 s ile 7 s arasında L, 12’den 0’a düzgün biçimde iner.','L(6) = 6 kg·m²/s'),A('Açısal hızı bul','L = I·ω bağıntısını kullan.','ω = 6 ÷ 3 = 2 rad/s'),A('Enerjiyi hesapla','Dönme kinetik enerjisi bağıntısını uygula.','E = ½ · 3 · 2² = 6 J')],
 puf='Önce grafikten istenen andaki değeri oku.',sekil=sk)
# ================= 12 · orta · öncüllü, yuvarlanan küre =================
k_=Fr(2,5); Et=Fr(1,2); Er=Fr(1,2)*k_*2   # E_öt = ½mv², E_dön = ½·(k m R²)(v/R)² = ½ k m v²  (k = 2/5 → 1/5 m v²)
Er=Fr(1,2)*k_
assert Er==Fr(1,5) and Er/(Et+Er)==Fr(2,7) and Et/Er==Fr(5,2)
tr={'I':True,'II':False,'III':True}
rs={'I':'Dolu küre için E_dön = ½·(2/5·m·R²)·(v/R)² = (1/5)·m·v² ve E_öt = ½·m·v² olduğundan dönme enerjisi toplamın 2/7’sidir.','II':'E_öt ÷ E_dön = (1/2) ÷ (1/5) = 5/2 olduğundan iki enerji eşit değildir; öteleme enerjisi daha büyüktür.','III':'Kaymadan yuvarlanmada temas noktasının hızı v − ω·R = 0’dır; yani alt nokta zemine göre anlık olarak durgundur.'}
d,y,ad=onc(tr,rs,S5)
q('0012',tipId='acisal-yuvarlanma',tip='Kaymadan yuvarlanan cisimlerde enerji ve hız',z='orta',alt=ALT,kaz='Kaymadan yuvarlanan dolu kürede öteleme ve dönme enerjilerinin oranını ve temas noktasının hızını yorumlar.',
 kart='K-AFACISAL-06 (yuvarlanan küre) · öncüllü',kalip='öncüllü',
 metin='Kütlesi m, yarıçapı R olan dolu bir küre (I = 2/5·m·R²), yatay zeminde kütle merkezi hızı v olacak biçimde kaymadan yuvarlanmaktadır.\nBuna göre;\nI. Dönme kinetik enerjisi, toplam kinetik enerjinin 2/7’si kadardır.\nII. Öteleme kinetik enerjisi, dönme kinetik enerjisine eşittir.\nIII. Küre üzerinde o anda zemine temas eden noktanın, zemine göre hızı sıfırdır.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5,istenen='Doğru olan yargılar.',ip=['Kaymadan yuvarlanma koşulunu yazıp iki kinetik enerjiyi m ve v cinsinden ifade et.'],
 bilgi=[B_Y],ad=ad,puf='Kaymadan yuvarlanma koşulunu v ve ω ile yaz.')
# ================= 13 · orta · tork, açısal ivme =================
I13,R13,F13,t13=2,Fr(1,2),8,3
tau=F13*R13; al=Fr(tau,I13); w13=al*t13; assert (tau,al,w13)==(4,2,6)
z1=Fr(F13,I13)*t13; z2=F13*t13; z3=al*t13**2; z4=Fr(al*t13**2,2)
assert (z1,z2,z3,z4)==(12,24,18,9) and len({w13,z1,z2,z3,z4})==5
sk=fig('\\draw[thick,fill=gray!15] (0,0) circle (1.5);','\\fill (0,0) circle (1.6pt); \\node[below left=1pt] at (0,0) {O};',
 '\\node at (-.1,-.85) {$I=2$ kg$\\cdot$m$^2$};',
 '\\draw[thin] (0,0) -- (1.5,0); \\node[above] at (.75,0) {$R=0{,}5$ m};',
 '\\draw[vurgu,very thick,-{Stealth[length=2.2mm,width=2mm]}] (1.5,0) -- (1.5,1.5); \\node[vurgu,right] at (1.55,.9) {$F=8$ N};')
q('0013',tipId='acisal-tork-makara',tip='Torkla açısal ivme ve makaralı sistemde enerji',z='orta',alt=ALT,kaz='Teğetsel kuvvetin torkundan açısal ivmeyi ve verilen süre sonundaki açısal hızı bulur.',
 kart='K-AFACISAL-07 (τ = Iα) · I = 2, R = 0,5, F = 8, t = 3 s',kalip='şekilli',
 metin='Merkezinden geçen düşey bir eksen etrafında sürtünmesiz dönebilen ve başlangıçta durgun olan disk şekilde gösterilmiştir. Diskin kenarına, yarıçapa dik ve diskin düzleminde olan sabit büyüklükte bir F kuvveti 3 s boyunca uygulanıyor.\nBuna göre, kuvvet kalktığı anda diskin açısal hızı kaç rad/s’dir?',
 dogru=6,yan=[(z4,'Açısal hız yerine 3 s sonundaki dönme açısını (½·α·t² = ½ · 2 · 3² = 9 rad) bulmuş.','bilgi'),(18,'Açısal hızı ω = α·t² olarak almış: 2 · 3² = 18 rad/s.','dikkat'),(12,'Torku, kuvvet kolunu hesaba katmadan τ = F = 8 N·m almış: α = 4 rad/s² ve ω = 12 rad/s bulmuş.','islem'),(24,'Açısal hızı F · t = 24 olarak almış; eylemsizlik momentini ve yarıçapı hesaba katmamış.','dikkat')],
 istenen='Kuvvet kalktığı andaki açısal hız (rad/s).',ip=['Kuvvetin dönme eksenine göre torkunu bulup açısal ivmeye geç.'],
 bilgi=[B_T],
 ad=[A('Torku bul','Kuvvet yarıçapa diktir; kuvvet kolu R’dir.','τ = F·R = 8 · 0,5 = 4 N·m'),A('Açısal ivmeyi bul','τ = I·α bağıntısını kullan.','α = 4 ÷ 2 = 2 rad/s²'),A('Açısal hızı bul','Başlangıçta durgun olan disk düzgün hızlanır.','ω = α·t = 2 · 3 = 6 rad/s')],
 puf='Tork kuvvet ile kuvvet kolunun çarpımıdır; sabit torkta açısal ivme sabit olduğundan ω = α·t yazılır.',sekil=sk)
# ================= 14 · orta · öncüllü, eliptik yörünge =================
rA_,rB_=1,3
assert Fr(rB_,rA_)==3 and Fr(rB_,rA_)**2==9
tr={'I':False,'II':True,'III':False}
rs={'I':'m·v·r sabit olduğundan A’da hız B’dekinin 3 katıdır; yani A’daki hız B’dekinden küçük değildir.','II':'Hızlar oranı 3 olduğundan kinetik enerjiler oranı 3² = 9’dur.','III':'Merkezi kuvvet tork yapmadığı için açısal momentum korunur; A ve B’deki açısal momentumlar eşittir.'}
d,y,ad=onc(tr,rs,S5)
a_,b_,c_=3.2,2.77,1.6
sk=fig(f'\\draw[thick] (0,0) ellipse ({a_} and {b_});',
 f'\\fill[gray!60] ({c_},0) circle (.22); \\draw[thick] ({c_},0) circle (.22); \\node[above=5pt] at ({c_},0) {{M}};',
 f'\\fill ({a_},0) circle (2pt); \\node[right=3pt] at ({a_},0) {{A}};',
 f'\\fill ({-a_},0) circle (2pt); \\node[left=3pt] at ({-a_},0) {{B}};',
 f'\\draw[{DARR}] ({c_},-.55) -- ({a_},-.55) node[midway,below] {{$d$}};',
 f'\\draw[{DARR}] ({-a_},-1.3) -- ({c_},-1.3) node[midway,below] {{$3d$}};',
 f'\\draw[dashed,gray] ({a_},-.1) -- ({a_},-.6); \\draw[dashed,gray] ({c_},-.3) -- ({c_},-1.35); \\draw[dashed,gray] ({-a_},-.1) -- ({-a_},-1.35);')
q('0014',tipId='acisal-ip-cember',tip='Merkezi kuvvet altında hareket ve açısal momentum',z='orta',alt=ALT,kaz='Merkezi kuvvet etkisindeki eliptik yörüngede açısal momentumun korunumundan hız ve enerji oranlarını yorumlar.',
 kart='K-AFACISAL-05 (eliptik yörünge) · d ve 3d, öncüllü',kalip='öncüllü',
 metin='Kütlesi m olan bir uydu, M gök cisminin çekim kuvvetinin etkisiyle şekildeki eliptik yörüngede dolanmaktadır. M, elipsin odaklarından birindedir. Uydunun yörüngedeki A ve B noktalarında M’ye olan uzaklıkları sırasıyla d ve 3d’dir. Açısal momentum M’ye göre alınacak; diğer cisimlerin etkisi önemsizdir.\nBuna göre, uydu için;\nI. A noktasındaki hızının büyüklüğü, B noktasındakinden küçüktür.\nII. A noktasındaki kinetik enerjisi, B noktasındakinin 9 katıdır.\nIII. A noktasındaki açısal momentumunun büyüklüğü, B noktasındakinin 3 katıdır.\nyargılarından hangileri doğrudur?',
 dogru=d,yan=y,sira=S5,istenen='Doğru olan yargılar.',ip=['Çekim kuvvetinin M’ye göre torkunu düşünüp A ve B’de m·v·r çarpımını karşılaştır.'],
 bilgi=[B_L,B_E],ad=ad,puf='Çekim kuvvetinin M’ye göre torkunun ne olduğunu düşün.',sekil=sk)
# ================= 15 · zor · makara + ip + cisim, h =================
M15,R15,m15,v15=4,Fr(1,2),1,4
I15=Fr(M15*R15**2,2); w15=v15/R15; Er15=I15*w15**2/2; Et15=Fr(m15*v15**2,2); h15=(Er15+Et15)/(m15*g)
assert (I15,w15,Er15,Et15,h15)==(Fr(1,2),8,16,8,Fr(12,5))
j1=Et15/(m15*g); j2=Er15/(m15*g)
j3=(I15*v15**2/2+Et15)/(m15*g)
j4=(Fr(M15*R15**2)*w15**2/2+Et15)/(m15*g)
assert (j1,j2,j3,j4)==(Fr(4,5),Fr(8,5),Fr(6,5),4) and len({h15,j1,j2,j3,j4})==5
sk=fig('\\fill[gray!35] (-1.0,3.3) rectangle (1.2,3.5); \\draw[thick] (-1.0,3.3) -- (1.2,3.3);',
 '\\draw[thick] (0,3.3) -- (0,2.7);',
 '\\draw[thick,fill=gray!25] (0,2.1) circle (.6); \\fill (0,2.1) circle (1.5pt);',
 '\\draw[thin] (0,2.1) -- (-.6,2.1); \\node[above] at (-.3,2.1) {\\scriptsize $R$}; \\node at (0,1.75) {\\scriptsize $M$};',
 '\\node[left=2pt] at (-.7,2.5) {\\scriptsize $R=0{,}5$ m}; \\node[left=2pt] at (-.7,1.7) {\\scriptsize $M=4$ kg};',
 '\\draw[thick] (.6,2.1) -- (.6,1.0);',
 '\\draw[thick,fill=gray!55] (.3,.45) rectangle (.9,1.0); \\node at (.6,.725) {\\scriptsize $m$};',
 '\\node[right=2pt] at (.95,.725) {\\scriptsize $m=1$ kg};',
 '\\draw[dashed] (.3,-1.55) rectangle (.9,-1.0);',
 '\\draw[{Stealth[length=1.8mm,width=1.6mm]}-{Stealth[length=1.8mm,width=1.6mm]}] (2.3,.45) -- (2.3,-1.55) node[midway,right] {$h$};',
 '\\draw[dashed,gray] (.95,.45) -- (2.35,.45); \\draw[dashed,gray] (.95,-1.55) -- (2.35,-1.55);',
 '\\draw[vurgu,very thick,-{Stealth[length=2.2mm,width=2mm]}] (-.35,-1.0) -- (-.35,-1.8); \\node[vurgu,left] at (-.4,-1.4) {$v$};')
q('0015',tipId='acisal-tork-makara',tip='Torkla açısal ivme ve makaralı sistemde enerji',z='zor',alt=ALT,kaz='Makaraya sarılı ipin ucundaki cismin inmesinde cismin ve makaranın kinetik enerjilerini birlikte kullanarak yüksekliği bulur.',
 kart='K-AFACISAL-07 (makara + cisim) · M = 4 kg, R = 0,5 m, m = 1 kg, v = 4 m/s',kalip='şekilli',
 metin='Yatay ve sürtünmesiz sabit bir eksen etrafında dönebilen, düzgün ve türdeş disk biçimli makaranın (I = ½·M·R²) üzerinden hafif ve esnemeyen bir ip geçirilmiştir. İpin ucundaki cisim durgun hâlden serbest bırakılıyor; ip makara üzerinde kaymamaktadır. Makaranın ve cismin bilgileri şekilde verilmiştir. Hava direnci önemsizdir; g = 10 m/s²’dir.\nBuna göre, cismin hızı 4 m/s olduğunda cismin inmiş olduğu h yüksekliği kaç m’dir?',
 dogru=h15,yan=[(j1,'Makaranın dönme enerjisini hesaba katmadan m·g·h = ½·m·v² yazmış: h = 8 ÷ 10 = 0,8 m.','dikkat'),(j2,'Cismin öteleme enerjisini atlayıp yalnız makaranın dönme enerjisini (16 J) almış: h = 16 ÷ 10 = 1,6 m.','dikkat'),(j3,'Makaranın açısal hızını ω = v almış (R’ye bölmemiş): ½ · 0,5 · 4² = 4 J, h = (8 + 4) ÷ 10 = 1,2 m.','islem'),(j4,'Makaranın eylemsizlik momentini ½·M·R² yerine M·R² almış: dönme enerjisi 32 J, h = (8 + 32) ÷ 10 = 4 m.','bilgi')],
 istenen='Cismin inme yüksekliği h (m).',ip=['İp kaymadığına göre cismin hızı ile makaranın açısal hızı arasındaki bağıntıyı kurup sistemin toplam kinetik enerjisini yaz.'],
 bilgi=[B_E,B_Y],
 ad=[A('ω’yı bul','İp kaymadığından cismin hızı makara kenarının çizgisel hızına eşittir.','ω = v ÷ R = 4 ÷ 0,5 = 8 rad/s'),A('Makaranın I’sı','Düzgün disk için ½·M·R² kullan.','I = ½ · 4 · 0,5² = 0,5 kg·m²'),A('Kinetik enerjileri hesapla','Cismin öteleme, makaranın dönme enerjisi.','E_cisim = ½ · 1 · 16 = 8 J, E_makara = ½ · 0,5 · 64 = 16 J'),A('Enerji korunumu','Ağırlığın yaptığı iş toplam kinetik enerjiye eşittir.','m·g·h = 24 → 10 · h = 24'),A('h’yi bul','Eşitliği çöz.','h = 2,4 m')],
 puf='Makaralı sistemde cismin ağırlığı yalnız cismi değil makarayı da döndürür; enerjiyi iki parçaya bölmeyi unutma.',sekil=sk)
# ================= 16 · zor · çubuğa yapışan hamur =================
M16,m16,r16,v16=1,1,1,6
L16=m16*v16*r16; I16=(2*M16+m16)*r16**2; w16=Fr(L16,I16); Ei16=Fr(m16*v16**2,2); Ef16=Fr(I16*w16**2,2); loss16=Ei16-Ef16
assert (L16,I16,w16,Ei16,Ef16,loss16)==(6,3,2,18,6,12)
w_alt=Fr(L16,2*M16*r16**2); k1=Ei16-Fr(2*M16*r16**2*w_alt**2,2); k2=m16*v16**2
assert (w_alt,k1,k2)==(3,9,36) and len({loss16,Ef16,Ei16,k1,k2})==5
sk=fig('\\draw[very thick] (-1.6,0) -- (1.6,0);',
 '\\fill[gray!60] (-1.6,0) circle (.2); \\draw (-1.6,0) circle (.2); \\fill[gray!60] (1.6,0) circle (.2); \\draw (1.6,0) circle (.2);',
 '\\node[above=4pt] at (-1.6,0) {$1$ kg}; \\node[above=4pt] at (1.6,0) {$1$ kg};',
 '\\draw[thick,fill=white] (0,0) circle (.12); \\fill (0,0) circle (1.2pt); \\node[above=4pt] at (0,0) {O};',
 '\\draw[{Stealth[length=1.8mm,width=1.6mm]}-{Stealth[length=1.8mm,width=1.6mm]}] (-1.6,-.5) -- (1.6,-.5) node[midway,below] {$2$ m};',
 '\\draw[thick,fill=gray!20] (1.6,-2.2) circle (.2); \\node[right=3pt] at (1.8,-2.2) {$1$ kg};',
 '\\draw[vurgu,very thick,-{Stealth[length=2.2mm,width=2mm]}] (1.6,-1.95) -- (1.6,-1.15); \\node[vurgu,left=2pt] at (1.5,-1.55) {$v=6$ m/s};')
q('0016',tipId='acisal-yapisma',tip='Birleşen dönen cisimlerde açısal hız ve enerji kaybı',z='zor',alt=ALT,kaz='Çubuğun ucuna yapışan cismin çarpışmasında açısal momentumun korunumunu ve mekanik enerji kaybını birlikte kullanır.',
 kart='K-AFACISAL-04 (çubuğa çarpan hamur) · 1 kg, 6 m/s, çubuk 2 m',kalip='şekilli',
 metin='Yatay, sürtünmesiz bir masanın üzerinde, kütlesi önemsiz 2 m uzunluğundaki bir çubuğun uçlarına 1 kg kütleli iki cisim bağlanmıştır. Çubuk, orta noktasından (O) geçen düşey ve sabit bir eksen etrafında serbestçe dönebilmektedir. Çubuk durgunken, çubuğa dik doğrultuda şekildeki gibi gelen 1 kg kütleli bir hamur parçası çubuğun bir ucundaki cisme çarpıp ona yapışıyor. Tüm cisimlerin boyutları önemsizdir.\nBuna göre, çarpışma sırasında mekanik enerjideki azalma kaç J’dür?',
 dogru=12,yan=[(6,'Birleşik sistemin son dönme enerjisini (½ · 3 · 2²) enerjideki azalma sanmış.','dikkat'),(9,'Hamur parçasının eylemsizlik momentini katmadan I = 2 kg·m² almış: ω = 3 rad/s, son enerji 9 J, azalma 18 − 9 = 9 J.','islem'),(18,'Hamur parçasının ilk kinetik enerjisinin (½ · 1 · 6²) tamamının kaybolduğunu sanmış.','bilgi'),(36,'İlk enerjiyi ½ katsayısı olmadan (m·v² = 36 J) almış ve son enerjiyi çıkarmamış.','dikkat')],
 istenen='Mekanik enerjideki azalma (J).',ip=['Çarpışma sırasında O eksenine göre hangi niceliğin korunduğunu belirleyip birleşik sistemin eylemsizlik momentini yaz.'],
 bilgi=[B_L,B_I,B_KOR],
 ad=[A('Çarpışmadan önceki L','Hamur parçası O’ya dik uzaklığı 1 m olan bir doğru boyunca gelir.','L = m·v·r = 1 · 6 · 1 = 6 kg·m²/s'),A('Birleşik sistemin I’sı','İki uçtaki cisim ve yapışan hamur parçası eksenden 1 m uzaktadır.','I = (1 + 1 + 1) · 1² = 3 kg·m²'),A('Ortak açısal hız','L korunur.','ω = 6 ÷ 3 = 2 rad/s'),A('Enerjileri karşılaştır','İlk enerji hamur parçasındadır, son enerji dönmededir.','E₁ = ½ · 1 · 6² = 18 J, E₂ = ½ · 3 · 2² = 6 J'),A('Azalmayı bul','Fark, ısı ve ses enerjisine dönüşür.','ΔE = 18 − 6 = 12 J')],
 puf='Çarpışmada eksene göre açısal momentum korunur ama tamamen esnek olmayan çarpışmada mekanik enerji korunmaz.',sekil=sk)
# ================= 17 · zor · grafik ω–t, yapışma =================
IA17,w1_,w2_=3,10,6
IB17=Fr(IA17*(w1_-w2_),w2_); Ei17=Fr(IA17*w1_**2,2); Ef17=Fr((IA17+IB17)*w2_**2,2); Q17=Ei17-Ef17
assert (IB17,Ei17,Ef17,Q17)==(2,150,90,60)
n1=Ei17; n2=Fr(IA17*(w1_**2-w2_**2),2); n3=Fr(IB17*w1_**2,2)
assert (n1,n2,n3)==(150,96,100) and len({Q17,Ef17,n1,n2,n3})==5
sk=fig('\\begin{axis}[width=6.8cm,height=5.2cm,xmin=0,xmax=6,ymin=0,ymax=12,xtick distance=1,ytick distance=2,grid=both,major grid style={gray!55,thin},tick label style={font=\\small},axis lines=left,xlabel={$t$ (s)},ylabel={$\\omega$ (rad/s)},xlabel style={font=\\small},ylabel style={font=\\small}]',
 '\\addplot[thick,vurgu] coordinates {(0,10) (2,10)}; \\addplot[thick,vurgu] coordinates {(2,6) (6,6)}; \\addplot[thick,vurgu,dashed] coordinates {(2,10) (2,6)};','\\end{axis}')
q('0017',tipId='acisal-yapisma',tip='Birleşen dönen cisimlerde açısal hız ve enerji kaybı',z='zor',alt=ALT,kaz='Açısal hız–zaman grafiğinden birleşen diskin eylemsizlik momentini bulup ısıya dönüşen enerjiyi hesaplar.',
 kart='K-AFACISAL-04 (ω–t grafiği, yapışma) · I_A = 3 kg·m², 10 → 6 rad/s',kalip='grafik',
 metin='Düşey bir eksen etrafında sürtünmesiz dönen, eylemsizlik momenti 3 kg·m² olan A diskinin üzerine, t = 2 s anında aynı eksenle çakışık ve durgun hâlde bulunan B diski bırakılıyor. İki disk kısa sürede birbirine yapışıp birlikte dönüyor. Sistemin açısal hızının zamana göre değişimi şekildeki grafikte verilmiştir.\nBuna göre, birleşme sırasında ısıya dönüşen enerji kaç J’dür?',
 dogru=60,yan=[(150,'Başlangıçtaki dönme enerjisinin (½ · 3 · 10²) tamamının ısıya dönüştüğünü sanmış.','dikkat'),(90,'Birleşik sistemin son dönme enerjisini (½ · 5 · 6²) ısıya dönüşen enerji sanmış.','bilgi'),(96,'Son durumda yalnız A diskinin döndüğünü varsayıp ½ · 3 · (10² − 6²) = 96 J bulmuş.','islem'),(100,'B diskinin ilk açısal hızla dönmesi durumundaki enerjisini (½ · 2 · 10²) ısı saymış.','dikkat')],
 istenen='Birleşme sırasında ısıya dönüşen enerji (J).',ip=['Grafikteki iki açısal hız değerinden yararlanarak B diskinin eylemsizlik momentini ayrı bir adımda bul.'],
 bilgi=[B_L,B_E,B_KOR],
 ad=[A('Grafiği oku','Birleşmeden önce ω = 10 rad/s, sonra ω = 6 rad/s’dir.','ω₁ = 10, ω₂ = 6 rad/s'),A('B’nin I’sını bul','Birleşme sırasında açısal momentum korunur.','3 · 10 = (3 + I_B) · 6 → I_B = 2 kg·m²'),A('Enerjileri hesapla','Başlangıçta yalnız A döner; sonra A ve B birlikte döner.','E₁ = ½ · 3 · 10² = 150 J, E₂ = ½ · 5 · 6² = 90 J'),A('Isıya dönüşeni bul','Enerjideki azalma ısıya dönüşür.','Q = 150 − 90 = 60 J')],
 puf='Grafikteki iki değeri ayrı ayrı yorumla.',sekil=sk)
# ================= 18 · zor · halka üzerinde böcek =================
M18,R18,mb18,w18=3,2,1,3
Ir=M18*R18**2; Ia18=Ir+mb18*R18**2; Ib18=Ir; Lc=Ia18*w18; wb18=Fr(Lc,Ib18)
Eic=Fr(Ia18*w18**2,2); Efc=Fr(Ib18*wb18**2,2); dE=Efc-Eic
assert (Ir,Ia18,wb18,Eic,Efc,dE)==(12,16,4,72,96,24)
assert len({dE,0,Eic,Efc,Eic+Efc})==5
sk=fig('\\draw[thick,fill=gray!25] (0,0) circle (2.0); \\draw[thick,fill=white] (0,0) circle (1.8);',
 '\\draw[very thick] (-1.8,0) -- (1.8,0); \\fill (0,0) circle (1.6pt); \\node[below=3pt] at (0,0) {O};',
 '\\fill[gray!80] (1.9,0) circle (.14); \\draw[thick] (1.9,0) circle (.14);',
 '\\draw[dashed,vurgu,very thick,-{Stealth[length=2.2mm,width=2mm]}] (1.7,0) -- (.3,0);',
 '\\node[above] at (1.0,.05) {\\scriptsize yürüyüş yönü};',
 '\\draw[thin] (0,0) -- (-1.414,-1.414); \\node[right] at (-.85,-1.2) {\\scriptsize $R=2$ m};',
 '\\node at (.8,-.6) {\\scriptsize $M=3$ kg};',
 '\\draw[vurgu,thick,-{Stealth[length=2mm,width=1.8mm]}] (-1.0,2.35) to[bend left=40] (1.0,2.35); \\node[vurgu,above] at (0,2.65) {$\\omega=3$ rad/s};',
 '\\node[right] at (2.15,0) {böcek, $1$ kg};')
q('0018',tipId='acisal-koruma',tip='Dönen sistemde eylemsizlik momenti değişimi ve açısal momentumun korunumu',z='zor',alt=ALT,kaz='Dönen halka üzerinde yürüyen cisim için açısal momentumun korunumunu ve dönme kinetik enerjisindeki artışı birlikte kullanır.',
 kart='K-AFACISAL-03 (halka ve böcek) · M = 3 kg, R = 2 m, m = 1 kg, ω = 3 rad/s',kalip='şekilli',
 metin='Yatay düzlemde, merkezinden geçen düşey eksen etrafında sürtünmesiz dönebilen ince bir halkanın (I = M·R²) kenarında bir böcek durmaktadır. Halkanın bir çapı boyunca kütlesi önemsiz, ince bir çubuk bağlanmıştır; böcek bu çubuğun ucundadır. Sistem, şekildeki gibi sabit açısal hızla dönerken böcek, çubuk üzerinde yürüyerek halkanın merkezine geliyor. Böceğin boyutları önemsizdir.\nBuna göre, böcek merkeze ulaştığında sistemin dönme kinetik enerjisi kaç J artmıştır?',
 dogru=24,yan=[(0,'Dönme kinetik enerjisinin korunduğunu sanmış; oysa korunan nicelik açısal momentumdur.','bilgi'),(72,'Başlangıçtaki dönme kinetik enerjisini (½ · 16 · 3²) artış sanmış.','dikkat'),(96,'Son dönme kinetik enerjisini (½ · 12 · 4²) artış sanmış.','dikkat'),(168,'İlk ve son dönme enerjilerini toplamış: 72 + 96 = 168 J.','islem')],
 istenen='Dönme kinetik enerjisindeki artış (J).',ip=['Böceğin merkezde olduğu duruma göre sistemin son eylemsizlik momentini yazıp önce son açısal hızı bul.'],
 bilgi=[B_I,B_L,B_E],
 ad=[A('İlk ve son I','Halka M·R², böcek kenarda m·R² katkı yapar; merkezde katkısı sıfırdır.','I₁ = 3·2² + 1·2² = 16 kg·m², I₂ = 12 kg·m²'),A('Son açısal hız','Açısal momentum korunur.','16 · 3 = 12 · ω₂ → ω₂ = 4 rad/s'),A('Enerjileri hesapla','Her durumda E = ½·I·ω².','E₁ = ½ · 16 · 9 = 72 J, E₂ = ½ · 12 · 16 = 96 J'),A('Artışı bul','Son ve ilk enerji farkı.','ΔE = 96 − 72 = 24 J')],
 puf='Açısal momentum sabit kalırken eylemsizlik momenti azalırsa dönme enerjisi artar; fazlalığı böceğin yaptığı iş karşılar.',sekil=sk)
# ================= 19 · zor · halka ve silindir, dönme enerjisi oranı =================
mK,mL=3,4
ErK=mK*Fr(1,2); ErL=mL*Fr(1,3)
assert ErK/ErL==Fr(9,8)
sira19=['3/4','8/9','9/8','3/2','2']
assert [Fr(3,4),Fr(8,9),Fr(9,8),Fr(3,2),Fr(2)]==sorted([Fr(3,4),Fr(8,9),Fr(9,8),Fr(3,2),Fr(2)])
assert Fr(mK,mL)==Fr(3,4) and ErL/ErK==Fr(8,9) and Fr(1,2)/Fr(1,3)==Fr(3,2) and Fr(1)/Fr(1,2)==2
sk=fig('\\fill[gray!35] (-.6,-.2) rectangle (6.0,0); \\draw[thick] (-.6,0) -- (6.0,0);',*slope3(0,'K (halka, $3$ kg)','M'),*slope3(3.2,'L (silindir, $4$ kg)','L'))
q('0019',tipId='acisal-yuvarlanma',tip='Kaymadan yuvarlanan cisimlerde enerji ve hız',z='zor',alt=ALT,kaz='Farklı kütleli, kaymadan yuvarlanan cisimlerin tabandaki dönme kinetik enerjilerinin oranını enerji payları ve kütleler üzerinden bulur.',
 kart='K-AFACISAL-06 (halka–silindir enerji oranı) · 3 kg ve 4 kg',kalip='şekilli',
 metin='Yarıçapları eşit olan, kütlesi 3 kg olan ince bir halka (K) ile kütlesi 4 kg olan dolu bir silindir (L), özdeş eğik düzlemlerin aynı h yüksekliğindeki ucundan durgun hâlde serbest bırakılıyor. Her iki cisim de kaymadan yuvarlanarak tabana ulaşıyor. Eylemsizlik momentleri I_K = m_K·R² ve I_L = ½·m_L·R²’dir.\nBuna göre, tabana ulaştıklarında K’nin dönme kinetik enerjisinin L’ninkine oranı kaçtır?',
 dogru='9/8',yan=[('3/4','Dönme enerjisi paylarını (½ ve ⅓) hesaba katmadan yalnız kütlelerin oranını almış: 3 ÷ 4.','dikkat'),('8/9','Oranı ters çevirmiş: E_L ÷ E_K = (4 · ⅓) ÷ (3 · ½) = 8/9.','islem'),('3/2','Kütleleri eşit sanıp yalnız dönme payları oranını almış: ½ ÷ ⅓ = 3/2.','bilgi'),('2','Yalnız I ÷ (m·R²) katsayılarının oranını almış: 1 ÷ ½ = 2.','dikkat')],
 sira=sira19,istenen='E_dön(K) ÷ E_dön(L) oranı.',ip=['Her cisim için dönme enerjisinin toplam enerjiden payını eylemsizlik momentinin m·R²’ye oranından bul.'],
 bilgi=[B_Y,B_I],
 ad=[A('Dönme enerjisi payını bul','Toplam enerji m·g·h; dönme payı k ÷ (1 + k), k = I ÷ (m·R²).','Halka: k = 1 → ½·m·g·h; silindir: k = ½ → ⅓·m·g·h'),A('K için dönme enerjisi','Kütle 3 kg.','E_K = 3 · ½ · g·h = 1,5·g·h'),A('L için dönme enerjisi','Kütle 4 kg.','E_L = 4 · ⅓ · g·h = (4/3)·g·h'),A('Oranı bul','Birini diğerine böl.','E_K ÷ E_L = 1,5 ÷ (4/3) = 9/8')],
 puf='Kütleler farklı olduğu için yalnız dönme paylarını değil, toplam enerji m·g·h’yi de hesaba kat.',sekil=sk)
# ================= 20 · zor · grafik I–r², platform, enerji artışı =================
I0,mg=1,1
Ir1=I0+2*mg*2**2; Ir2=I0+2*mg*1**2; w1=2; w2=Fr(Ir1*w1,Ir2)
E1_=Fr(Ir1*w1**2,2); E2_=Fr(Ir2*w2**2,2); dE20=E2_-E1_
assert (Ir1,Ir2,w2,E1_,E2_,dE20)==(9,3,6,18,54,36) and len({dE20,0,E1_,E2_,E1_+E2_})==5
sk=fig('\\begin{axis}[width=6.8cm,height=5.2cm,xmin=0,xmax=5,ymin=0,ymax=12,xtick distance=1,ytick distance=2,grid=both,major grid style={gray!55,thin},tick label style={font=\\small},axis lines=left,xlabel={$r^2$ (m$^2$)},ylabel={$I$ (kg$\\cdot$m$^2$)},xlabel style={font=\\small},ylabel style={font=\\small}]',
 '\\addplot[thick,vurgu] coordinates {(0,1) (5,11)};','\\end{axis}')
q('0020',tipId='acisal-koruma',tip='Dönen sistemde eylemsizlik momenti değişimi ve açısal momentumun korunumu',z='zor',alt=ALT,kaz='Eylemsizlik momenti–r² grafiğinden iki durumdaki I değerlerini okuyup açısal momentumun korunumuyla son açısal hızı ve dönme kinetik enerjisindeki artışı bulur.',
 kart='K-AFACISAL-03 (I–r² grafiği, enerji) · r = 2 m → 1 m, ω = 2 rad/s',kalip='grafik',
 metin='Düşey eksen etrafında sürtünmesiz dönebilen bir platformun üzerinde, eksenin iki yanında eşit uzaklıkta özdeş iki cisim bulunmaktadır. Cisimlerin eksene olan uzaklığı r olmak üzere sistemin eksene göre eylemsizlik momentinin r² ile değişimi şekildeki grafikte verilmiştir. Cisimler eksenden 2 m uzaktayken sistem 2 rad/s’lik açısal hızla dönmektedir. Dönme sürerken cisimler, eksene 1 m uzaklığa getiriliyor.\nBuna göre, bu işlem sırasında sistemin dönme kinetik enerjisi kaç J artmıştır?',
 dogru=36,yan=[(0,'Dönme kinetik enerjisinin korunduğunu sanmış; oysa korunan nicelik açısal momentumdur.','bilgi'),(18,'Yalnız ilk dönme kinetik enerjisini (½ · 9 · 2²) artış sanmış.','dikkat'),(54,'Yalnız son dönme kinetik enerjisini (½ · 3 · 6²) artış sanmış.','dikkat'),(72,'İlk ve son enerjileri toplamış: 18 + 54 = 72 J.','islem')],
 istenen='Dönme kinetik enerjisindeki artış (J).',ip=['Önce grafikten iki durumdaki eylemsizlik momentini oku.'],
 bilgi=[B_I,B_L,B_E],
 ad=[A('I değerlerini oku','r = 2 m için r² = 4 m², r = 1 m için r² = 1 m²’dir.','I₁ = 9 kg·m², I₂ = 3 kg·m²'),A('Son açısal hızı bul','Net dış tork sıfırdır; açısal momentum korunur.','9 · 2 = 3 · ω₂ → ω₂ = 6 rad/s'),A('Enerjileri hesapla','Her durumda E = ½·I·ω².','E₁ = ½ · 9 · 2² = 18 J, E₂ = ½ · 3 · 6² = 54 J'),A('Artışı bul','Son ve ilk enerji farkı.','ΔE = 54 − 18 = 36 J')],
 puf='Grafikte doğrunun her noktası, o r² değerindeki eylemsizlik momentini verir.',sekil=sk)
# ================= yaz =================
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(GD,'acisal-1.json'),'/tmp/bos-acisal.json')
tipler={}
for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|'+KONUAD))['kartlar'].append(c['id'])
json.dump(dict(konu=KONUAD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik (yalnız mantık), MEB 12. sınıf fizik müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afacisal.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'kart',len(KARTLAR))
