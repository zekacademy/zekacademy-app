"""AYT Fizik · Newton’un Hareket Yasaları · 20 soru. Şekil değerleri ve her cevap/çeldirici Python'da hesaplanıp assert edilir."""
import sys,os,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from math import sin,cos,tan,radians,degrees,atan2,sqrt
KONU='Newton’un Hareket Yasaları'
P=Parti('newton',KONU,'afiz|'+KONU,ders='AYT Fizik',idon='aytfiz')
P.konu_adi=KONU; H.KONU=KONU
g=10
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
NK=[0]
TIPAD={'nw-temas':'Temas kuvveti','nw-surtunme':'Sürtünme kuvveti','nw-makara':'Makara–ip sistemleri','nw-yigin':'Üst üste cisimlerde sürtünme','nw-grafik':'Grafik yorumu ve dinamik','nw-asansor':'İvmeli düşey hareket','nw-egik':'Eğik düzlemde hareket','nw-kavram':'Kavramsal yargılar ve etki–tepki'}
def Q(tipId,tip,z,alt,fikir,tuzak,kalip,metin,istenen,ip,bilgi,ad,puf,sekil=None,dogru=None,yan=None,sira=None,kaz=None):
    tip=TIPAD[tipId]; NK[0]+=1; n=NK[0]; no=f'{n:04d}'; kid=f'K-AFNW-{n:02d}'
    kart(kid,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,'ÖSYM AYT 2018–2025 Newton soruları (yalnız mantık) · 345 AYT Fizik · MEB 11. sınıf')
    mk(P,no,ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz or alt+' konusunda hesap ve yorum yapar.',kart=f'{kid} ({alt}) · özgün kurgu',kalip=kalip,
       metin=metin,dogru=dogru,yan=yan,istenen=istenen,ip=[ip],bilgi=bilgi,puf=puf,sekil=sekil,sira=sira)
import re as _re
def _hat(m):
    x1,y1,x2,y2=[float(v) for v in m.groups()]; d=y2-y1 if y2>y1 else y1-y2; lo,hi=min(y1,y2),max(y1,y2); out=[]; x=x1+d
    while x<=x2+1e-9: out.append(f'\\draw[gray,thin] ({x:.2f},{hi:.2f}) -- ({x-d:.2f},{lo:.2f});'); x+=.25
    return ' '.join(out)
def sade(t): return _re.sub(r'\\fill\[pattern=north east lines,pattern color=gray\] \(([-\d.]+),([-\d.]+)\) rectangle \(([-\d.]+),([-\d.]+)\);',_hat,t)
def tk(*lines): return tikz_svg(sade(HEAD+'\n'.join(lines)+TAIL))
def blk(x,y,w,h,txt,fill='gray!25'): return f'\\draw[thick,fill={fill}] ({x:.3f},{y:.3f}) rectangle ({x+w:.3f},{y+h:.3f}); \\node at ({x+w/2:.3f},{y+h/2:.3f}) {{{txt}}};'
def arr(x1,y1,x2,y2,lab='',pos='above',col='vurgu'):
    n=f' node[{pos},{col},midway] {{{lab}}}' if lab else ''
    return f'\\draw[{col},very thick,{ARR}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f}){n};'
def zem(x1,x2,y=0): return f'\\fill[pattern=north east lines,pattern color=gray] ({x1},{y-.22}) rectangle ({x2},{y}); \\draw ({x1},{y}) -- ({x2},{y});'
def pul(x,y,r=.22): return f'\\draw[thick,fill=white] ({x:.3f},{y:.3f}) circle ({r}); \\fill ({x:.3f},{y:.3f}) circle (1.2pt);'
def ln(*pts,st='thick'): return f'\\draw[{st}] '+' -- '.join(f'({a:.3f},{b:.3f})' for a,b in pts)+';'
RM=['I','II','III']
OS=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
OSET={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(truth,neden,secenek):
    """truth: 3 bool; neden: her öncül için doğru açıklama; secenek: 5 şık (OS sırasında). Döndürür dogru, yan, sira."""
    T={i for i in range(3) if truth[i]}; dog=[s for s in secenek if OSET[s]==T]; assert len(dog)==1 and len(secenek)==5
    assert [OS.index(s) for s in secenek]==sorted(OS.index(s) for s in secenek)
    yan=[]
    for s in secenek:
        if s==dog[0]: continue
        d=OSET[s]^T
        t=' '.join((f'{RM[i]}. öncülü yanlış saymış; oysa {neden[i]}.' if i in T else f'{RM[i]}. öncülü doğru saymış; oysa {neden[i]}.') for i in sorted(d))
        yan.append((s,t,'bilgi'))
    return dog[0],yan,list(secenek)
def oadim(truth,neden):
    a=[A(f'{RM[i]}. öncülü incele',neden[i][0].upper()+neden[i][1:]+'.',f'{RM[i]}: '+('doğru' if truth[i] else 'yanlış')) for i in range(3)]
    return a

# ===== 01 · temas kuvveti · kolay =====
mK,mL,F=2,3,20; a=F/(mK+mL); N=mL*a
assert a==4 and N==12 and mK*a==8 and F/2==10
S=tk(zem(-1.8,4.6),blk(0,0,1.2,.9,'K\\,(2 kg)'),blk(1.2,0,1.5,.9,'L\\,(3 kg)'),arr(-1.7,.45,-.05,.45,'$F=20$ N','above'))
Q('nw-temas','Yan yana cisimlerde temas kuvveti','kolay','Temas Kuvveti','Sistemin ortak ivmesi bulunur; arkadaki cismin ivmesini sağlayan net kuvvet, öndeki cismin ona uyguladığı kuvvettir.','F kuvvetini temas kuvveti sanmak; temas kuvvetini ivmesi bilinen cismin kütlesiyle değil yanlış kütleyle çarpmak.','şekilli',
 'Sürtünmesiz yatay düzlemde yan yana duran K ve L cisimlerine, şekilde verilen yatay F kuvveti K cismine uygulanarak ikisi birlikte hareket ettiriliyor. Cisimlerin kütleleri ve kuvvetin büyüklüğü şekilde gösterilmiştir.\nBuna göre, K cisminin L cismine uyguladığı temas kuvvetinin büyüklüğü kaç N’dur?',
 'K’nin L’ye uyguladığı temas kuvvetinin büyüklüğü (N).','Önce iki cismi tek bir sistem gibi düşünüp ortak ivmeyi bul; sonra yalnız L’ye bak.',
 [B('Newton’un ikinci yasası','ΣF = m·a. Birlikte hareket eden cisimlerin ivmesi aynıdır. Örnek: 10 N’luk kuvvet 5 kg’lık cisme 2 m/s² ivme verir'),B('Etki–tepki','K, L’ye kaç N kuvvet uygularsa L de K’ya aynı büyüklükte, zıt yönlü kuvvet uygular')],
 [A('Ortak ivmeyi bul','Sistemin toplam kütlesine dış kuvvet etki eder.','a = 20 ÷ (2 + 3) = 4 m/s²'),A('L’ye uygula','L’yi hızlandıran tek yatay kuvvet K’nin temas kuvvetidir.','N = m_L · a = 3 · 4'),A('Sonuç','Temas kuvvetinin büyüklüğü hesaplanır.','N = 12 N')],
 'Öndeki cismi hızlandıran kuvvet, onun kütlesi × ortak ivmedir.',sekil=S,
 dogru=12,yan=[(8,'K’nin kütlesini kullanmış: 2 · 4 = 8 N; temas kuvveti L’nin ivmesini sağlar.','dikkat'),(20,'F kuvvetinin tamamının L’ye iletildiğini sanmış; F iki cismi birlikte hızlandırır.','bilgi'),(10,'F kuvvetini iki cisim arasında eşit paylaştırmış (20 ÷ 2).','bilgi'),(4,'Ortak ivmeyi (4 m/s²) temas kuvveti sanmış; kütle ile çarpmayı unutmuş.','islem')])

# ===== 02 · statik sürtünme · kolay · öncüllü =====
m2,us,uk,F2=5,0.5,0.4,15; fmax=us*m2*g; assert fmax==25 and F2<fmax and uk*m2*g==20 and 20<fmax
S=tk(zem(-.6,4.4),blk(0,0,1.6,1.0,'5 kg'),arr(1.65,.5,3.3,.5,'$F=15$ N','above'),'\\node at (.8,-.6) {$\\mu_s=0{,}5\\quad \\mu_k=0{,}4$};')
tr=[True,False,True]; nd=['durgun cisimde statik sürtünme, uygulanan kuvvete eşittir (15 N)','durgun cisimde sürtünme μk·N değil, uygulanan kuvvete eşittir','statik sürtünmenin üst sınırı μs·N = 25 N olduğundan 20 N’luk kuvvette de cisim durur']
d,y,sr=onc(tr,nd,['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])
Q('nw-surtunme','Statik ve kinetik sürtünme','kolay','Sürtünme Kuvveti','Durgun cisimde sürtünme uygulanan kuvvete eşittir ve μs·N sınırını aşamaz; kinetik sürtünme yalnız hareket hâlinde geçerlidir.','Her durumda f = μ·N yazmak; μk’yı durgun cisme uygulamak.','öncüllü',
 'Yatay zemin üzerinde duran cisme, şekilde verilen 15 N’luk yatay kuvvet uygulanıyor ve cisim hareket etmiyor. Cisim ile zemin arasındaki statik ve kinetik sürtünme katsayıları şekilde verilmiştir.\n(g = 10 m/s²)\nBuna göre,\nI. Zeminin cisme uyguladığı sürtünme kuvveti 15 N’dur.\nII. Zeminin cisme uyguladığı sürtünme kuvveti 20 N’dur.\nIII. Kuvvet 20 N yapılırsa cisim yine hareket etmez.\nyargılarından hangileri doğrudur?',
 'Doğru olan öncüllerin belirlenmesi.','Cisim durgunsa net kuvvetin ne olduğunu düşün; statik sürtünmenin üst sınırını hesapla.',
 [B('Statik sürtünme','Cisim durgun kaldığı sürece f_s = uygulanan kuvvet; üst sınır f_max = μs·N. Örnek: 40 N ağırlık, μs = 0,5 → en çok 20 N'),B('Kinetik sürtünme','Yalnız kayarken f_k = μk·N')],
 oadim(tr,nd)+[A('Sonuç','I ve III doğru.','I ve III')],'Durgun cisimde sürtünme uygulanan kuvvete eşit; kayma başlamadan sınırı μs·N ile karşılaştır.',sekil=S,dogru=d,yan=y,sira=sr)

# ===== 03 · kinetik sürtünmeli ivme · kolay =====
m3,F3,u3=5,30,0.4; f3=u3*m3*g; a3=(F3-f3)/m3; assert f3==20 and a3==2 and F3/m3==6 and (F3+f3)/m3==10 and (F3-u3*m3)/m3==5.6 and (F3-u3*F3)/m3==3.6
S=tk(zem(-.6,4.6),blk(0,0,1.6,1.0,'5 kg'),arr(1.65,.5,3.3,.5,'$F=30$ N','above'),'\\node at (.8,-.6) {$\\mu_k=0{,}4$};')
Q('nw-surtunme','Kinetik sürtünmeli yatay hareket','kolay','Sürtünme Kuvveti','Net kuvvet = uygulanan kuvvet − kinetik sürtünme; ivme = net kuvvet ÷ kütle.','Sürtünmeyi hesaba katmamak; sürtünmeyi eklemek; N yerine kütleyi kullanmak.','şekilli',
 'Yatay ve pürüzlü zemin üzerindeki cisme şekildeki gibi yatay F kuvveti uygulandığında cisim sağa doğru hareket ediyor. Cismin kütlesi, kuvvet ve kinetik sürtünme katsayısı şekilde verilmiştir.\n(g = 10 m/s²)\nBuna göre, cismin ivmesinin büyüklüğü kaç m/s²’dir?',
 'Cismin ivmesi (m/s²).','Önce kinetik sürtünme kuvvetini bul; net kuvveti ondan sonra yaz.',
 [B('Kinetik sürtünme','f = μk·N; yatay zeminde N = m·g. Örnek: 2 kg, μk = 0,5 → f = 10 N'),B('Net kuvvet','ΣF = m·a. Örnek: 12 N net kuvvet, 3 kg → 4 m/s²')],
 [A('Sürtünmeyi bul','Yatay zeminde normal kuvvet ağırlığa eşittir.','N = 50 N → f = 0,4 · 50 = 20 N'),A('Net kuvvet','Sürtünme hareketin tersine.','ΣF = 30 − 20 = 10 N'),A('İvme','ΣF = m·a.','a = 10 ÷ 5 = 2 m/s²')],
 'Sürtünmeli harekette önce f = μ·N, sonra ΣF = m·a.',sekil=S,
 dogru=2,yan=[(6,'Sürtünmeyi yok saymış: 30 ÷ 5 = 6 m/s².','dikkat'),(10,'Sürtünmeyi kuvvete eklemiş: (30 + 20) ÷ 5 = 10 m/s².','islem'),(5.6,'Normal kuvvet yerine kütleyi kullanmış: f = 0,4 · 5 = 2 N, a = 28 ÷ 5.','bilgi'),(3.6,'Normal kuvvet yerine uygulanan kuvveti kullanmış: f = 0,4 · 30 = 12 N, a = 18 ÷ 5 = 3,6 m/s².','bilgi')])

# ===== 04 · Atwood, tavan kuvveti · orta =====
a1_,a2_=2,3; a4=(a2_-a1_)*g/(a1_+a2_); T4=a1_*(g+a4); assert a4==2 and T4==24 and a2_*(g-a4)==T4
C4=2*T4; assert C4==48 and (a1_+a2_)*g==50 and a2_*g==30 and T4==24
S=tk(ln((.3,3.4),(2.7,3.4),st='thick'),'\\fill[pattern=north east lines,pattern color=gray] (.3,3.4) rectangle (2.7,3.65);',ln((1.5,3.4),(1.5,3.0)),pul(1.5,2.5,.5),
 ln((1,2.5),(1,1.5)),ln((2,2.5),(2,1.9)),blk(.55,.7,.9,.8,'3 kg'),blk(1.55,1.1,.9,.8,'2 kg'))
Q('nw-makara','Atwood düzeneği ve makara askısı','orta','Makara–İp Sistemleri','Atwood düzeneğinde ortak ivme ve ip gerilmesi bulunur; makara için kuvvet dengesi yazılır.','Tavan kuvvetini cisimlerin ağırlıkları toplamına (durgun sistem) eşitlemek; T yerine 2T almamak.','şekilli',
 'Şekildeki düzenekte kütleleri 3 kg ve 2 kg olan cisimler, hafif ve sürtünmesiz bir makaradan geçen esnemez bir iple birbirine bağlanmıştır. Makara, hafif bir iple tavana asılıdır. Cisimler serbest bırakılıp hareket ederken tavana bağlı ipteki gerilme kuvveti ölçülüyor.\n(g = 10 m/s²)\nBuna göre, tavana bağlı ipteki gerilme kuvvetinin büyüklüğü kaç N’dur?',
 'Tavana bağlı ipteki gerilme kuvveti (N).','Makarayı tutan ipteki kuvveti hangi kuvvetlerin dengelediğini düşün; önce cisimlerin ortak ivmesini bul.',
 [B('Atwood düzeneği','ortak ivme a = (m₂ − m₁)g ÷ (m₁ + m₂); T = m₁(g + a). Örnek: 1 kg ve 3 kg → a = 5 m/s²'),B('Hafif makara','Kütlesiz makarada ΣF = 0: tutan kuvvet = 2T')],
 [A('İvmeyi bul','Ağır cisim aşağı, hafif cisim yukarı ivmelenir.','a = (30 − 20) ÷ 5 = 2 m/s²'),A('İp gerilmesini bul','Hafif cisim için T − m₁g = m₁a.','T = 2 · (10 + 2) = 24 N'),A('Makarayı dengele','Makara hafif; iki ip kolu aşağı çeker, tavan ipi yukarı.','T_tavan = 2T = 48 N')],
 'Hafif makarayı tutan kuvvet 2T’dir; ivmeli harekette cisim ağırlıklarının toplamı değil.',sekil=S,
 dogru=48,yan=[(24,'Yalnız bir ipin gerilmesini (T = 24 N) bulup makaradaki iki ip kolunu hesaba katmamış.','dikkat'),(20,'Hafif cismin ağırlığını (20 N) tavan ipindeki gerilme sanmış.','bilgi'),(30,'Ağır cismin ağırlığını (30 N) tavan ipindeki gerilme sanmış.','bilgi'),(40,'Hafif cismin ağırlığını gerilme sanıp (T = m₁g = 20 N) iki katını (40 N) almış; ivmeyi hesaba katmamış.','islem')])

# ===== 05 · masa + asılı cisim, kütle bulma · orta =====
mt=3; a5=4; m5=Fr(mt*a5,g-a5); assert m5==2 and m5*g-mt*a5==m5*a5 and Fr(mt*a5,g)==Fr(6,5) and mt+m5==5
def masa(mm,lab_t,lab_h,extra=''):
    return tk(zem(-.2,4.2,1.0),blk(.3,1.0,1.1,.8,lab_t),ln((1.4,1.4),(3.6,1.4)),ln((3.6,1.0),(3.6,.9),st='thin'),'\\draw[thick] (3.5,1.0) -- (3.5,.9);',
      pul(3.6,1.4,.2),ln((3.8,1.4),(3.8,.75)),blk(3.35,-.05,.9,.8,lab_h),extra)
S=tk('\\fill[pattern=north east lines,pattern color=gray] (-.2,.78) rectangle (3.4,1.0);',ln((-.2,1.0),(3.4,1.0)),blk(.3,1.0,1.1,.8,'3 kg'),ln((1.4,1.5),(3.4,1.5)),
  pul(3.4,1.3,.2),ln((3.6,1.3),(3.6,.75)),blk(3.15,-.05,.9,.8,'$m$'))
Q('nw-makara','Masa üstündeki ve asılı cisim: kütle bulma','orta','Makara–İp Sistemleri','Sürtünmesiz masada ip hem asılı cismi geriyor hem masadaki cismi çekiyor; verilen ivmeyle masadaki cisimden T bulunur, asılı cisimden kütle çıkarılır.','Gerilmeyi asılı cismin ağırlığına eşitlemek; ip gerilimini iki kez saymak; toplam kütleyi karıştırmak.','şekilli',
 'Şekildeki sürtünmesiz sistemde yatay masa üzerindeki 3 kg kütleli cisim, hafif ve sürtünmesiz bir makaradan geçen esnemez bir iple kütlesi m olan asılı cisme bağlanmıştır. Sistem serbest bırakıldığında cisimlerin ivmesinin büyüklüğü 4 m/s² olarak ölçülüyor.\n(g = 10 m/s²)\nBuna göre, asılı cismin kütlesi m kaç kg’dır?',
 'Asılı cismin kütlesi m (kg).','Önce masadaki cisim için ipin gerilmesini ivmeden bul.',
 [B('Newton’un ikinci yasası','Her cisim için ayrı ayrı ΣF = m·a yazılır; ip esnemezse ivmeler aynıdır. Örnek: 2 kg, 6 N net kuvvet → 3 m/s²')],
 [A('Gerilmeyi bul','Masadaki cismi hızlandıran tek yatay kuvvet ip gerilmesidir.','T = 3 · 4 = 12 N'),A('Asılı cisme uygula','Aşağı ağırlık, yukarı gerilme; net kuvvet aşağı.','m·10 − 12 = m · 4'),A('Çöz','Bilinmeyen m’yi yalnız bırak.','6m = 12 → m = 2 kg')],
 'Her cisim için ayrı denklem yaz; ip gerilmesi ikisini bağlar.',sekil=S,
 dogru=2,yan=[(1.2,'Asılı cisim için T = m·g yazmış (hareketi yok saymış): 12 = 10m.','bilgi'),(3,'Asılı cismi masadaki cisimle aynı kütleli sanmış.','dikkat'),(4,'İvmenin sayısal değerini (4) kütle sanmış.','dikkat'),(5,'Cisimlerin toplam kütlesini (3 + 2 = 5 kg) asılı cismin kütlesi olarak vermiş.','islem')])

# ===== 06 · sürtünmeli masa + asılı · orta =====
m61,u6,m62=2,0.5,4; f6=u6*m61*g; a6=(m62*g-f6)/(m61+m62); T6=m62*(g-a6); assert f6==10 and a6==5 and T6==20==f6+m61*a6
assert m62*g==40 and m62*g-f6==30
S=tk('\\fill[pattern=north east lines,pattern color=gray] (-.2,.78) rectangle (3.4,1.0);',ln((-.2,1.0),(3.4,1.0)),blk(.3,1.0,1.1,.8,'2 kg'),ln((1.4,1.5),(3.4,1.5)),
  pul(3.4,1.3,.2),ln((3.6,1.3),(3.6,.75)),blk(3.15,-.05,.9,.8,'4 kg'),'\\node at (.85,-.25) {$\\mu_k=0{,}5$};')
Q('nw-makara','Sürtünmeli masa ve asılı cisim','orta','Makara–İp Sistemleri','Masa ile cisim arasındaki kinetik sürtünme hareketi engeller; ortak ivme bulunduktan sonra gerilme tek cisimden hesaplanır.','Sürtünmeyi unutmak; gerilmeyi asılı cismin ağırlığına eşitlemek.','şekilli',
 'Şekildeki sistemde masa üzerindeki 2 kg kütleli cisim ile masa arasındaki kinetik sürtünme katsayısı 0,5’tir. Cisim, hafif ve sürtünmesiz bir makaradan geçen esnemez bir iple 4 kg kütleli asılı cisme bağlanmıştır. Sistem serbest bırakılıyor.\n(g = 10 m/s²)\nBuna göre, cisimler hareket ederken ipteki gerilme kuvveti kaç N’dur?',
 'Hareket sırasında ipteki gerilme (N).','Önce kinetik sürtünme kuvvetini bul ve ortak ivmeyi tüm sistem için yaz.',
 [B('Kinetik sürtünme','Yatay yüzeyde f = μk·m·g. Örnek: 3 kg, μk = 0,2 → 6 N'),B('Sistem denklemi','Hareket yönündeki kuvvetler toplamı = toplam kütle × ivme')],
 [A('Sürtünmeyi bul','Masadaki cisme etki eder.','f = 0,5 · 2 · 10 = 10 N'),A('Ortak ivmeyi bul','Sistemi asılı cismin ağırlığı hareket ettirir.','40 − 10 = (2 + 4)·a → a = 5 m/s²'),A('Gerilmeyi bul','Masadaki cisim: T − f = m·a.','T = 10 + 2 · 5 = 20 N'),A('Kontrol','Asılı cisim: 40 − T = 4 · 5.','T = 20 N')],
 'İvmeli harekette ip gerilmesi asılı cismin ağırlığına eşit değildir.',sekil=S,
 dogru=20,yan=[(5,'İvmenin değerini (5 m/s²) gerilme sanmış.','dikkat'),(10,'Sürtünme kuvvetini (10 N) gerilme olarak vermiş.','dikkat'),(30,'Asılı cismin ağırlığından sürtünmeyi çıkarmış (net kuvvet, 30 N); gerilme farklıdır.','bilgi'),(40,'Gerilmeyi asılı cismin ağırlığına eşit almış; ivmeli harekette T < m₂g.','bilgi')])

# ===== 07 · üst üste cisimler, kayma sınırı · orta =====
mA,mB,u7=2,3,0.4; a7=u7*g; F7=(mA+mB)*a7; assert a7==4 and F7==20 and u7*mA*g==8 and mB*a7==12
S=tk(zem(-.6,4.6),blk(0,0,2.0,.8,'B\\,(3 kg)'),blk(.4,.8,1.2,.7,'A\\,(2 kg)'),arr(2.05,.4,3.7,.4,'$F$','above'),'\\node[right] at (2.15,1.15) {$\\mu=0{,}4$ (A–B)};','\\node[below] at (1.0,-.25) {zemin sürtünmesiz};')
Q('nw-yigin','Üst üste cisimlerde kayma sınırı','orta','Sürtünme Kuvveti','Üstteki cisme etki eden yatay kuvvet ve sınır durumu incelenir; ardından sistem bir bütün olarak çözülür.','Sürtünme kuvvetini F’ye eşitlemek; yalnız B’nin kütlesini kullanmak.','şekilli',
 'Sürtünmesiz yatay zeminde duran B cisminin üzerinde, A cismi şekildeki gibi bulunmaktadır. A ile B arasındaki sürtünme katsayısı şekilde verilmiştir. B cismine yatay F kuvveti uygulanıyor ve A cismi B’nin üzerinde kaymadan hareket ediyor. (Sınır durumunda statik ve kinetik sürtünme katsayıları eşit alınacaktır.)\n(g = 10 m/s²)\nBuna göre, A’nın B üzerinde kaymaması için F kuvveti en fazla kaç N olabilir?',
 'F’nin alabileceği en büyük değer (N).','A’ya yatay doğrultuda etki eden kuvvetin hangisi olduğunu belirle.',
 [B('Statik sürtünme','Kaymama sınırında f = μ·N. Örnek: 2 kg, μ = 0,5 → 10 N')],
 [A('A için ivmenin sınırı','A’yı yalnız sürtünme hızlandırır.','μ·m_A·g = m_A·a → a = 4 m/s²'),A('Sistemi bütün al','Kaymadan hareket için ivme ortak.','F = (2 + 3) · 4'),A('Sonuç','En büyük kuvvet.','F = 20 N')],
 'Kaymama sınırında üstteki cismin ivmesi μ·g’dir; F bu ivmeyle toplam kütleyi çeker.',sekil=S,
 dogru=20,yan=[(4,'En büyük ivmeyi (4 m/s²) kuvvet sanmış.','dikkat'),(8,'Sürtünme kuvvetini (8 N) F değeri olarak vermiş.','bilgi'),(12,'Yalnız B’nin kütlesini kullanmış: 3 · 4 = 12 N.','dikkat'),(50,'Toplam ağırlığı (50 N) kuvvet sanmış.','dikkat')])

# ===== 08 · v–t grafiği, kütle · zor =====
m8=2; F8=12; a8a=Fr(8,4); a8b=Fr(8,2); f8=m8*a8b; assert F8-f8==m8*a8a and F8/(a8a+a8b)==m8==2 and f8/(m8*g)==Fr(2,5)
assert F8/a8a==6 and F8/a8b==3 and Fr(F8,8)==Fr(3,2)
G8=['\\begin{axis}[width=6.4cm,height=5cm,xmin=0,xmax=7,ymin=0,ymax=10,xtick={0,1,2,3,4,5,6,7},ytick={0,2,4,6,8,10},grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$t$ (s)},ylabel={$v$ (m/s)}]',
 '\\addplot[vurgu,very thick] coordinates {(0,0)(4,8)(6,0)};','\\end{axis}']
S=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(G8)+TAIL)
Q('nw-grafik','Hız–zaman grafiğinden kütle ve sürtünme','zor','Hız–Zaman Grafiği ve Dinamik','İvmeler grafiğin eğiminden okunur; kuvvet uygulanırken F − f = m·a₁, kuvvet kalkınca yalnız sürtünme: f = m·a₂; iki denklemden kütle bulunur.','Yavaşlama evresinde de F’nin etkidiğini sanmak; sürtünmeyi unutup F = m·a₁ yazmak.','grafik',
 'Yatay ve pürüzlü bir zeminde durgun hâldeki bir cisme t = 0 anında yatay ve 12 N büyüklüğünde sabit bir kuvvet uygulanıyor; kuvvet t = 4 s anında ortadan kaldırılıyor. Cismin hız–zaman grafiği şekilde verilmiştir. Kinetik sürtünme kuvveti hareket boyunca sabittir.\nBuna göre, cismin kütlesi kaç kg’dır?',
 'Cismin kütlesi (kg).','İki evrenin ivmelerini grafiğin eğiminden bul; her evre için ayrı denklem yaz.',
 [B('v–t grafiği','Eğim ivmeyi verir: a = Δv ÷ Δt. Örnek: 3 s’de 6 m/s artış → 2 m/s²'),B('Kuvvet kalkınca','Yalnız sürtünme yavaşlatır: f = m·a')],
 [A('Hızlanma evresi','0–4 s: a₁ = 8 ÷ 4.','a₁ = 2 m/s² → 12 − f = 2m'),A('Yavaşlama evresi','4–6 s: yalnız sürtünme.','a₂ = 8 ÷ 2 = 4 m/s² → f = 4m'),A('İki denklemi birleştir','f’yi yerine yaz.','12 − 4m = 2m → m = 2 kg')],
 'Kuvvet kalkınca yavaşlatan tek kuvvet sürtünmedir; iki evre iki denklem verir.',sekil=S,
 dogru=2,yan=[(6,'Sürtünmeyi yok sayıp yalnız hızlanma evresini almış: 12 ÷ 2 = 6 kg.','dikkat'),(3,'Yalnız yavaşlama ivmesiyle F’yi kullanmış: 12 ÷ 4 = 3 kg; yavaşlarken F etkimez.','bilgi'),(1.5,'İvme yerine en büyük hızı (8 m/s) kullanmış: 12 ÷ 8.','bilgi'),(8,'En büyük hız değerini kütle sanmış.','dikkat')])

# ===== 09 · F–a grafiği · orta · öncüllü =====
pts9=[(10,0),(20,2),(30,4),(40,6),(50,8)]; sl=Fr(pts9[1][1]-pts9[0][1],pts9[1][0]-pts9[0][0]); m9=1/sl; f9=pts9[0][0]
assert m9==5 and f9==10 and all(Fr(b)==sl*(a_-10) for a_,b in pts9) and (45-f9)/m9==7
G9=['\\begin{axis}[width=6.4cm,height=5cm,xmin=0,xmax=50,ymin=0,ymax=8,xtick={0,5,10,15,20,25,30,35,40,45,50},ytick={0,1,2,3,4,5,6,7,8},grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$F$ (N)},ylabel={$a$ (m/s²)}]',
 '\\addplot[vurgu,very thick] coordinates {(10,0)(50,8)};','\\end{axis}']
S=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(G9)+TAIL)
tr=[False,True,True]; nd=['grafiğin eğimi 1 ÷ m = 0,2 m/s²·N⁻¹ olduğundan kütle 5 kg’dır','a = 0 olan noktadaki F değeri sürtünmeye eşittir: 10 N','F = 45 N için a = (45 − 10) ÷ 5 = 7 m/s²’dir']
d,y,sr=onc(tr,nd,['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'])
Q('nw-grafik','İvme–kuvvet grafiği yorumu','orta','F–a Grafiği ve Sürtünme','Sürtünmeli yatay harekette a = (F − f) ÷ m; F–a grafiğinin eğimi 1/m, a = 0 noktasındaki F ise sürtünme kuvvetidir.','Grafiğin eğimini kütle sanmak; F eksenini kestiği değeri yok saymak; grafiğin başlangıçtan geçtiğini varsaymak.','öncüllü',
 'Yatay ve pürüzlü bir zemin üzerinde hareket eden bir cisme uygulanan yatay F kuvveti değiştirilerek cismin ivmesi ölçülüyor ve şekildeki F–a grafiği çiziliyor. Hareket boyunca kinetik sürtünme kuvveti sabittir.\nBuna göre,\nI. Cismin kütlesi 4 kg’dır.\nII. Cisme etki eden kinetik sürtünme kuvveti 10 N’dur.\nIII. F = 45 N iken cismin ivmesi 7 m/s²’dir.\nyargılarından hangileri doğrudur?',
 'Doğru olan öncüllerin belirlenmesi.','a = (F − f) ÷ m bağıntısını grafikteki doğruyla karşılaştır.',
 [B('Grafik okuma','a = F/m − f/m doğrusunda eğim 1/m, F eksenini kestiği nokta f’dir. Örnek: 0,5 eğimli doğru → 2 kg')],
 oadim(tr,nd)+[A('Sonuç','II ve III doğru.','II ve III')],'F–a doğrusunda a = 0 olduğu F değeri sürtünmeye eşittir.',sekil=S,dogru=d,yan=y,sira=sr)

# ===== 10 · asansör, dinamometre · orta · öncüllü =====
m10,R10=3,24; a10=(R10-m10*g)/m10; assert a10==-2 and m10*a10==-6
tr=[True,True,True]; nd=['dinamometre ağırlıktan az (24 N < 30 N) gösterdiğinden ivme aşağı yönlüdür; hız aşağı yönlü ise asansör hızlanır','ivme aşağı yönlü iken hız yukarı yönlü olabilir; bu durumda asansör yavaşlar','net kuvvet = 30 − 24 = 6 N ve aşağı yönlüdür']
d,y,sr=onc(tr,nd,['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'])
S=tk('\\draw[thick] (0,0) rectangle (2.6,3.6);',ln((1.3,3.6),(1.3,3.15)),'\\draw[thick,decorate,decoration={zigzag,segment length=5pt,amplitude=2.5pt}] (1.3,3.15) -- (1.3,2.15);',
 blk(.85,1.2,.9,.9,'3 kg'),'\\draw[thick] (1.3,2.15) -- (1.3,2.1);','\\node[draw,fill=white,inner sep=2pt] at (2.05,2.65) {24 N};')
Q('nw-asansor','Asansörde dinamometre okuması','orta','İvmeli Düzeneklerde Kuvvet','Dinamometre cismin ağırlığı ile ivmeye bağlı gerilmeyi gösterir; okuma ağırlıktan azsa ivme aşağı yönlüdür, hız yönü ayrı bir bilgidir.','İvme yönü ile hız yönünü karıştırmak; dinamometre okumasını ağırlık sanmak.','öncüllü',
 'Bir asansörün tavanına bağlı dinamometreye 3 kg kütleli bir cisim asılmıştır. Asansör hareket ederken cisim asansöre göre durgun kalmakta ve dinamometre şekildeki değeri göstermektedir.\n(g = 10 m/s²)\nBuna göre,\nI. Asansör aşağı yönde hızlanıyor olabilir.\nII. Asansör yukarı yönde yavaşlıyor olabilir.\nIII. Cisme etki eden net kuvvet 6 N’dur ve aşağı yönlüdür.\nyargılarından hangileri doğrudur?',
 'Doğru olan öncüllerin belirlenmesi.','Ağırlığı hesapla ve dinamometre okumasıyla karşılaştırarak ivmenin yönünü bul.',
 [B('İvmeli asansör','Gerilme T = m(g + a) (a yukarı pozitif). T < mg ise ivme aşağı yönlüdür. Örnek: 2 kg, T = 24 N → a = 2 m/s² aşağı')],
 oadim(tr,nd)+[A('Sonuç','Üçü de doğru.','I, II ve III')],'İvme aşağı yönlü ise asansör ya aşağı hızlanıyor ya da yukarı yavaşlıyordur.',sekil=S,dogru=d,yan=y,sira=sr)

# ===== 11 · eğik düzlem sürtünmeli · orta · öncüllü =====
def egik(Lb,Ht,s,bw,bh,lab,extra=''):
    hyp=(Lb*Lb+Ht*Ht)**.5; u=(Lb/hyp,Ht/hyp); n=(-u[1],u[0])
    c=[(s*u[0]+x*u[0]+y*n[0], s*u[1]+x*u[1]+y*n[1]) for x,y in [(-bw/2,0),(bw/2,0),(bw/2,bh),(-bw/2,bh)]]
    top=(s*u[0]+n[0]*bh/2, s*u[1]+n[1]*bh/2); import math
    ang=math.degrees(math.atan2(Ht,Lb))
    o=[f'\\draw[thick] (0,0) -- ({Lb},{Ht}) -- ({Lb},0) -- cycle;',zem(-.5,Lb+.5),
       '\\draw[thick,fill=gray!25] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in c)+' -- cycle;',
       f'\\node[rotate={ang:.2f}] at ({top[0]:.3f},{top[1]:.3f}) {{{lab}}};',
       f'\\draw (.9,0) arc[start angle=0,end angle={ang:.2f},radius=.9]; \\node at (1.3,.28) {{$37^\\circ$}};',extra]
    return o,u,n,c
m11,u11=5,0.5; N11=m11*g*0.8; f11=u11*N11; a11=(m11*g*0.6-f11)/m11
assert N11==40 and f11==20 and a11==2 and tan(radians(37))>u11 and m11*g*0.6==30
o,u,n,c=egik(4,3,2.2,1.0,.7,'5 kg','\\node at (3.0,.35) {$\\mu_k=0{,}5$};')
S=tk(*o)
tr=[True,False,False]; nd=['tan37° = 0,75 > μ = 0,5 olduğundan (30 N > en çok 20 N) cisim aşağı kayar','sürtünme kuvveti μ·m·g·cos37° = 0,5 · 40 = 20 N’dur, 30 N değil','ivme (30 − 20) ÷ 5 = 2 m/s²’dir, 3 m/s² değil']
d,y,sr=onc(tr,nd,['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])
Q('nw-egik','Sürtünmeli eğik düzlemde kayma','orta','Eğik Düzlemde Hareket','Ağırlığın düzleme paralel bileşeni m·g·sinθ ile en büyük sürtünme μ·m·g·cosθ karşılaştırılır; kayarsa a = g(sinθ − μ cosθ).','Sürtünmeyi m·g ile hesaplamak (cosθ’yı unutmak); kayma koşulunu denetlemeden hareket varsaymak.','öncüllü',
 'Şekildeki 37° eğimli eğik düzlemin yüzeyi pürüzlüdür; kinetik sürtünme katsayısı şekilde verilmiştir. Üzerindeki 5 kg kütleli cisim serbest bırakılıyor.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8; statik ve kinetik sürtünme katsayıları eşit alınacaktır.)\nBuna göre,\nI. Cisim eğik düzlemde aşağı doğru kayar.\nII. Cisme etki eden sürtünme kuvveti 30 N’dur.\nIII. Cismin ivmesi 3 m/s²’dir.\nyargılarından hangileri doğrudur?',
 'Doğru olan öncüllerin belirlenmesi.','Önce cismi kaydırmaya çalışan kuvveti, sonra sürtünmenin alabileceği en büyük değeri hesapla.',
 [B('Eğik düzlem','Paralel bileşen m·g·sinθ, dik bileşen m·g·cosθ; f = μ·m·g·cosθ. Örnek: 2 kg, 37°: 12 N ve 16 N')],
 oadim(tr,nd)+[A('Sonuç','Yalnız I doğru.','Yalnız I')],'Eğik düzlemde N = m·g·cosθ; kayma için m·g·sinθ > μ·N olmalı.',sekil=S,dogru=d,yan=y,sira=sr)

# ===== 12 · fren yapan otobüste sarkaç · orta · öncüllü =====
th12=37; T_over=1/0.8; a12=g*0.75; assert a12==7.5 and T_over==1.25 and g*0.6==6
tr=[True,True,False]; nd=['topun ivmesi otobüsünkiyle aynıdır ve geriye yönlüdür; net kuvvet ivme yönündedir','düşey dengeden T·cos37° = m·g ve T = 1,25·m·g > m·g','ivme g·tan37° = 7,5 m/s²’dir; 6 m/s² (g·sin37°) alınamaz']
d,y,sr=onc(tr,nd,['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])
S=tk(ln((0,0),(5,0),(5,2.0),(0,2.0),(0,0)),'\\draw[thick,fill=white] (1,0) circle (.35); \\draw[thick,fill=white] (4,0) circle (.35);',
 ln((2.5,2.0),(2.5+1.2*.6,2.0-1.2*.8),st='thick'),'\\draw[thick,fill=gray!40] (3.22,1.04) circle (.17);','\\draw[dashed,thin] (2.5,2.0) -- (2.5,.6);',
 '\\draw (2.5,1.55) arc[start angle=-90,end angle=-53,radius=.45]; \\node at (2.15,1.3) {$37^\\circ$};',zem(-.8,5.8,-.35),arr(5.3,2.35,6.5,2.35,'$v$','above','black'))
Q('nw-kavram','Sarkaç ile ivmeli aracın ivmesi','orta','İvmeli Referans Sistemleri','Sarkaç aracın ivmesiyle aynı ivmeyle hareket eder; gerilmenin düşey bileşeni ağırlığı dengeler, yatay bileşeni net kuvveti oluşturur: a = g·tanθ.','g·sinθ ile g·tanθ’yı karıştırmak; net kuvvetin yönünü hareket yönü sanmak.','öncüllü',
 'Yatay yolda sağa doğru giden bir otobüs sabit ivmeyle frenlemektedir. Otobüsün tavanına iple asılı küçük bir top, ip düşeyle şekildeki açıyı yapacak biçimde otobüse göre durgun kalmaktadır. Hız vektörü şekilde gösterilmiştir.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8, tan 37° = 0,75)\nBuna göre, yere göre durgun bir gözlemciye göre,\nI. Topa etki eden net kuvvet, otobüsün hareket yönünün tersinedir.\nII. İpteki gerilme kuvveti topun ağırlığından büyüktür.\nIII. Otobüsün ivmesinin büyüklüğü 6 m/s²’dir.\nyargılarından hangileri doğrudur?',
 'Doğru olan öncüllerin belirlenmesi.','Topa etki eden iki kuvveti (ağırlık ve gerilme) çiz; net kuvvetin yatay olması gerektiğini kullan.',
 [B('Sarkaç ve ivme','T·cosθ = m·g, T·sinθ = m·a → a = g·tanθ. Örnek: θ = 45° ise a = g')],
 oadim(tr,nd)+[A('Sonuç','I ve II doğru.','I ve II')],'Sarkacın düşeyle yaptığı açı ivmeyi verir: a = g·tanθ.',sekil=S,dogru=d,yan=y,sira=sr)

# ===== 13 · üç cisim, iki ip · orta =====
m1_,m2_,m3_=2,3,5; a13=Fr(m3_*g,m1_+m2_+m3_); T1=m1_*a13; T2=m3_*(g-a13)
assert a13==5 and T1==10 and T2==25 and T2==T1+m2_*a13 and Fr(T2,T1)==Fr(5,2)
assert Fr(m3_*g,T1)==5 and Fr(T2,(m1_+m2_)*a13)==1 and Fr(T1,T2)==Fr(2,5) and Fr(T2-T1,T1)==Fr(3,2)
S=tk('\\fill[pattern=north east lines,pattern color=gray] (-.2,.78) rectangle (4.4,1.0);',ln((-.2,1.0),(4.4,1.0)),blk(.2,1.0,1.0,.8,'2 kg'),blk(2.2,1.0,1.2,.8,'3 kg'),
 ln((1.2,1.4),(2.2,1.4)),ln((3.4,1.4),(4.4,1.4)),'\\node[above] at (1.7,1.4) {$T_1$};','\\node[above] at (3.9,1.4) {$T_2$};',pul(4.4,1.2,.2),ln((4.6,1.2),(4.6,.75)),blk(4.15,-.05,.9,.8,'5 kg'))
Q('nw-makara','Üç cisimli ip sistemi','orta','Makara–İp Sistemleri','Üç cisimli sistemde ortak ivme toplam kütleden bulunur; her ipteki gerilme ipin arkasında kalan cisimlerden değil, ipin çektiği cisimlerden hesaplanır.','Her ipteki gerilmeyi eşit sanmak; asılı cismin ağırlığını T₂ almak; ip gerilmesine yanlış cisim grubunu uygulamak.','şekilli',
 'Şekildeki sürtünmesiz sistemde yatay masa üzerindeki 2 kg ve 3 kg kütleli cisimler birbirine, 3 kg’lık cisim de hafif ve sürtünmesiz bir makaradan geçen iple asılı 5 kg’lık cisme bağlanmıştır. İplerdeki gerilme kuvvetleri şekilde T₁ ve T₂ ile gösterilmiştir. Sistem serbest bırakılıyor.\n(g = 10 m/s²)\nBuna göre, T₂ ÷ T₁ oranı kaçtır?',
 'T₂ ÷ T₁ oranı.','Ortak ivmeyi bulduktan sonra T₁’i yalnız 2 kg’lık cisim, T₂’yi asılı cisim için yaz.',
 [B('İp gerilmesi','İpin ucundaki cisim grubunu hareket ettiren kuvvet gerilmedir. Örnek: 3 kg 2 m/s² ile hareket ederse onu çeken ip 6 N’dur')],
 [A('Ortak ivme','Sistemi asılı cismin ağırlığı hareket ettirir.','50 = (2 + 3 + 5)·a → a = 5 m/s²'),A('T₁’i bul','2 kg’lık cismi yalnız T₁ çeker.','T₁ = 2 · 5 = 10 N'),A('T₂’yi bul','Asılı cisim: m·g − T₂ = m·a.','T₂ = 50 − 25 = 25 N'),A('Oranla','İki gerilmeyi böl.','25 ÷ 10 = 2,5')],
 'Her ip, arkasında kalan cisimlerin toplam kütlesi × ivme kadar çeker.',sekil=S,
 dogru=Fr(5,2),yan=[(5,'T₂’yi asılı cismin ağırlığı (50 N) almış: 50 ÷ 10 = 5.','bilgi'),(1,'T₁’i iki masa cisminin birlikte ivmelendirdiğini (25 N) sanıp iki gerilmeyi eşit bulmuş.','dikkat'),(Fr(2,5),'Oranı ters yazmış: T₁ ÷ T₂.','dikkat'),(Fr(3,2),'T₂ yerine iki gerilme arasındaki farkı (15 N) kullanmış.','islem')])

# ===== 14 · hareketli makara · zor =====
M1,M2=2,2; a2=Fr(M2*g,M2+4*M1); a1=2*a2; Tm=M1*a1
assert a2==2 and a1==4 and Tm==8 and M2*g-2*Tm==M2*a2
assert Fr(M2*g,M2+M1)==5 and M2*(g-a2)==16 and a1==4
S=tk('\\fill[pattern=north east lines,pattern color=gray] (-.2,1.38) rectangle (3.4,1.6);',ln((-.2,1.6),(3.4,1.6)),blk(.3,1.6,1.1,.7,'$m_1$'),
 ln((1.4,1.95),(3.4,1.95)),pul(3.4,1.75,.2),ln((3.6,1.75),(3.6,.55)),pul(3.9,.55,.3),'\\draw[thick] (3.6,.55) arc[start angle=180,end angle=360,radius=.3];',ln((4.2,.55),(4.2,2.85)),
 '\\fill[pattern=north east lines,pattern color=gray] (3.7,2.85) rectangle (4.7,3.1); \\draw (3.7,2.85) -- (4.7,2.85);',ln((3.9,.25),(3.9,-.05)),blk(3.45,-.85,.9,.8,'$m_2$'))
Q('nw-makara','Hareketli makaralı düzenek','zor','Makara–İp Sistemleri','Hareketli makarada ipin boyu sabit olduğundan masadaki cismin ivmesi makaranın ivmesinin iki katıdır; hafif makarada 2T = m₂g − m₂a₂ yazılır.','Her iki cismin ivmesini eşit sanmak; hafif hareketli makaraya T yerine 2T uygulamamak.','şekilli',
 'Şekildeki sürtünmesiz düzenekte kütlesi m₁ = 2 kg olan cisim yatay masadadır; ucu tavana bağlı esnemez ip, hafif hareketli makaradan geçip masanın kenarındaki sabit ve sürtünmesiz makaradan m₁’e uzanmaktadır. Hareketli makaraya m₂ = 2 kg kütleli cisim asılmıştır. Sistem serbest bırakılıyor.\n(g = 10 m/s², iplerin ve makaraların kütlesi önemsizdir.)\nBuna göre, ipteki gerilme kuvveti kaç N’dur?',
 'Ipteki gerilme kuvveti (N).','İpin toplam boyu sabit olduğuna göre m₁ ile m₂’nin hareket miktarlarını ilişkilendir.',
 [B('Hareketli makara','Makara x kadar inerse ipin makaradan geçen kısmı 2x kadar uzar; bu nedenle masadaki cisim 2x gider ve a₁ = 2a₂. Hafif makarada ΣF = 0: tutan toplam kuvvet 2T.')],
 [A('İvme bağıntısı','İp boyu sabit.','a₁ = 2·a₂'),A('m₁ için','Masadaki cismi yalnız T çeker.','T = 2·a₁ = 4·a₂'),A('m₂ için','Hareketli makarayı iki ip kolu çeker.','m₂g − 2T = m₂a₂ → 20 − 8a₂ = 2a₂'),A('Çöz','a₂ bulunur, sonra T.','a₂ = 2 m/s² → T = 8 N')],
 'Hareketli makarada ivmeler farklıdır (a₁ = 2a₂) ve makarayı 2T tutar.',sekil=S,
 dogru=Tm,yan=[(5,'İvmeleri eşit alıp a = 20 ÷ (2 + 2) = 5 m/s² bulmuş ve ivmeyi gerilme sanmış.','dikkat'),(4,'Masadaki cismin ivmesini (a₁ = 4 m/s²) gerilme sanmış.','dikkat'),(20,'Gerilmeyi asılı cismin ağırlığına eşitlemiş.','bilgi'),(16,'Asılı cisim için m₂g − T = m₂a₂ yazmış (2T yerine T): T = 2 · (10 − 2) = 16 N.','islem')])

# ===== 15 · iki katmanlı sürtünme · zor =====
mA5,mB5,u1,u2,F15=2,4,0.4,0.1,42
a_birlikte=Fr(F15-u2*(mA5+mB5)*g).limit_denominator(100)/(mA5+mB5); aA=u1*g; assert a_birlikte==6>aA==4          # A kayar
aB=Fr(F15-u1*mA5*g-u2*(mA5+mB5)*g).limit_denominator(100)/mB5; assert aB==7
assert Fr(F15-u1*mA5*g-u2*mB5*g).limit_denominator(100)/mB5==Fr(15,2) and Fr(F15-u2*(mA5+mB5)*g).limit_denominator(100)/mB5==9 and Fr(F15,mB5)==Fr(21,2)
S=tk(zem(-.6,5.4),blk(0,0,2.4,.8,'B\\,(4 kg)'),blk(.5,.8,1.3,.7,'A\\,(2 kg)'),arr(2.45,.4,4.3,.4,'$F=42$ N','above'),
 '\\node[right] at (2.55,1.15) {$\\mu_{AB}=0{,}4$};','\\node[below] at (1.2,-.25) {$\\mu_{B-zemin}=0{,}1$};')
Q('nw-yigin','Çift yüzeyli sürtünme ve kayma','zor','Sürtünme Kuvveti','Cisimlerin hareket biçimi önce sorgulanır; ardından her cisim için ayrı ayrı hareket denklemi yazılır.','Cisimleri bir bütün sanmak; zemin sürtünmesini yalnız B’nin ağırlığıyla hesaplamak; A–B sürtünmesini B’ye eklemeyi unutmak.','şekilli',
 'Yatay zeminde duran B cisminin üzerine A cismi şekildeki gibi konmuştur. A ile B arasındaki ve B ile zemin arasındaki kinetik sürtünme katsayıları şekilde verilmiştir (statik sürtünme katsayıları kinetik olanlara eşit alınacaktır). B cismine yatay ve 42 N büyüklüğünde F kuvveti uygulanıyor.\n(g = 10 m/s²)\nBuna göre, B cisminin ivmesinin büyüklüğü kaç m/s²’dir?',
 'B cisminin ivmesi (m/s²).','Önce A cismine etki eden yatay kuvveti düşün.',
 [B('Kayma koşulu','Birlikte hareketteki ivme, üstteki cismin alabileceği en büyük ivmeyi (μ·g) aşıyorsa cisimler kayar. Örnek: μ = 0,3 → en çok 3 m/s²'),B('Zemin sürtünmesi','B’ye zemin, B + A’nın toplam ağırlığı üzerinden sürtünme uygular: f = μ·(m_A + m_B)·g')],
 [A('Birlikte hareketi denetle','Zemin sürtünmesi: 0,1 · 6 · 10 = 6 N.','a = (42 − 6) ÷ 6 = 6 m/s²'),A('A’nın sınırı','A’yı yalnız sürtünme hızlandırır.','a_A,en çok = 0,4 · 10 = 4 m/s² < 6 → A kayar'),A('B’ye etki eden kuvvetler','A’nın B’ye tepkisi (8 N) ve zemin sürtünmesi geriye.','F − 8 − 6 = 42 − 14 = 28 N'),A('B’nin ivmesi','ΣF = m_B · a_B.','a_B = 28 ÷ 4 = 7 m/s²')],
 'Kayma varsa A’nın ivmesi μ·g’de kalır; B için tüm sürtünmeleri ayrı yaz.',sekil=S,
 dogru=7,yan=[(6,'Cisimlerin birlikte hareket ettiğini varsaymış: a = 36 ÷ 6; A için gereken ivme sınırı aşılıyor.','dikkat'),(7.5,'Zemin sürtünmesini yalnız B’nin ağırlığıyla (4 N) bulmuş: (42 − 8 − 4) ÷ 4.','bilgi'),(9,'A ile B arasındaki sürtünmeyi unutmuş: (42 − 6) ÷ 4.','dikkat'),(10.5,'Tüm sürtünmeleri yok sayıp F ÷ m_B hesaplamış.','dikkat')])

# ===== 16 · çatı tipi iki eğik düzlem · zor =====
import math
m1c,m2c=6,8; s1,c1_=0.6,0.8; s2,c2_=0.8,0.6
ac=(Fr(m2c*g*4,5)-Fr(m1c*g*3,5))/(m1c+m2c); Tc=m1c*(ac+Fr(g*3,5))
assert ac==2 and Tc==48 and m2c*(Fr(g*4,5)-ac)==Tc and m1c*g*Fr(3,5)==36 and m2c*g*Fr(4,5)==64 and m1c*(g+ac)==72 and m1c*(Fr(g*3,5)-ac)==24 and 64-36==28
d=.275; r=.2; dl=d-r
# sol yüzey: n1.p = 0 ; n1=(-.6,.8) ; sağ yüzey: n2.p = 5 ; n2=(.8,.6)
n1=(-.6,.8); n2=(.8,.6); ap=(4,3); u1v=(.8,.6); u2v=(.6,-.8)
det=n1[0]*n2[1]-n1[1]*n2[0]; rhs1=dl; rhs2=5+dl
cx=(rhs1*n2[1]-n1[1]*rhs2)/det; cy=(n1[0]*rhs2-rhs1*n2[0])/det
p1=(cx+r*n1[0],cy+r*n1[1]); p2=(cx+r*n2[0],cy+r*n2[1])
bw,bh=.9,.55; sA=1.7; tB=1.2
def bc(origin,u,n,s0,s1_): return [(origin[0]+s*u[0]+h*n[0],origin[1]+s*u[1]+h*n[1]) for s,h in [(s0,0),(s1_,0),(s1_,bh),(s0,bh)]]
cA=bc((0,0),u1v,n1,sA-bw/2,sA+bw/2); cB=bc(ap,u2v,n2,tB-bw/2,tB+bw/2)
rA=(sA+bw/2)*u1v[0]+d*n1[0],(sA+bw/2)*u1v[1]+d*n1[1]; rB=(ap[0]+(tB-bw/2)*u2v[0]+d*n2[0],ap[1]+(tB-bw/2)*u2v[1]+d*n2[1])
tA=(sA*u1v[0]+n1[0]*bh/2,sA*u1v[1]+n1[1]*bh/2); tBp=(ap[0]+tB*u2v[0]+n2[0]*bh/2,ap[1]+tB*u2v[1]+n2[1]*bh/2)
S=tk(f'\\draw[thick] (0,0) -- (4,3) -- (6.25,0) -- cycle;',zem(-.5,6.75),
 '\\draw[thick,fill=gray!25] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in cA)+' -- cycle;',
 '\\draw[thick,fill=gray!25] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in cB)+' -- cycle;',
 f'\\node[rotate=36.87] at ({tA[0]:.3f},{tA[1]:.3f}) {{\\footnotesize 6 kg}};',f'\\node[rotate=-53.13] at ({tBp[0]:.3f},{tBp[1]:.3f}) {{\\footnotesize 8 kg}};',
 f'\\draw[thick,fill=white] ({cx:.3f},{cy:.3f}) circle ({r});',
 f'\\draw[thick] ({rA[0]:.3f},{rA[1]:.3f}) -- ({p1[0]:.3f},{p1[1]:.3f}) arc[start angle=126.87,end angle=36.87,radius={r}] -- ({rB[0]:.3f},{rB[1]:.3f});',
 '\\draw (.9,0) arc[start angle=0,end angle=36.87,radius=.9]; \\node at (1.3,.27) {$37^\\circ$};',
 '\\draw (5.65,0) arc[start angle=180,end angle=126.87,radius=.6]; \\node at (5.35,.35) {$53^\\circ$};')
Q('nw-egik','İki eğik düzlemde ip ile bağlı cisimler','zor','Eğik Düzlemde Hareket','Her cisim kendi eğik düzleminde ipe paralel bileşenle hareket eder; ortak ivme, iki paralel bileşenin farkının toplam kütleye bölünmesiyle bulunur.','Bileşenleri sin yerine cos ile almak; gerilmeyi bir cismin paralel bileşenine eşitlemek (durgun sanmak).','şekilli',
 'Şekildeki sürtünmesiz ve çatı biçimli düzeneğin iki yüzeyi 37° ve 53° eğimlidir. Kütleleri 6 kg ve 8 kg olan iki cisim, hafif ve sürtünmesiz makaradan geçen esnemez bir iple bağlanmış ve serbest bırakılmıştır.\n(g = 10 m/s², sin 37° = 0,6, sin 53° = 0,8)\nBuna göre, cisimler hareket ederken ipteki gerilme kuvveti kaç N’dur?',
 'İpteki gerilme kuvveti (N).','Her cismin eğik düzleme paralel ağırlık bileşenini hesapla; hangi yöne hareket edeceklerine karar ver.',
 [B('Eğik düzlemde bileşen','Paralel bileşen m·g·sinθ. Örnek: 2 kg, 37° için 12 N')],
 [A('Paralel bileşenler','Her cisim için m·g·sinθ.','37° tarafı: 6·10·0,6 = 36 N · 53° tarafı: 8·10·0,8 = 64 N'),A('Ortak ivme','Büyük bileşen yönünde hareket.','64 − 36 = (6 + 8)·a → a = 2 m/s²'),A('Gerilme','37° tarafındaki cisim yukarı doğru ivmelenir: T − 36 = 6·2.','T = 48 N'),A('Kontrol','53° tarafı: 64 − T = 8·2.','T = 48 N')],
 'Önce hareket yönünü paralel bileşenlerle belirle; ivmeyi toplam kütleyle, gerilmeyi tek cisimle bul.',sekil=S,
 dogru=48,yan=[(36,'Gerilmeyi hafif taraftaki paralel bileşene (36 N) eşitlemiş; sistem ivmeli olduğu için T > 36 N.','bilgi'),(28,'Net kuvveti (64 − 36 = 28 N) gerilme sanmış.','dikkat'),(24,'Hafif taraftaki cisim için T = m(g·sin37° − a) yazmış (işaret hatası): 6 · (6 − 2) = 24 N.','islem'),(72,'Gerilmeyi m·(g + a) almış; bu bağıntı düşey harekete aittir.','islem')])

# ===== 17 · F–t grafiği, konum · zor =====
m17=4; seg=[(2,8),(2,-12),(2,4)]; v=0; x=0; vs=[0]; xs=[0]
for dt,Fk in seg:
    ak=Fr(Fk,m17); x+=v*dt+ak*dt*dt/2; v+=ak*dt; vs.append(v); xs.append(x)
assert vs==[0,4,-2,0] and xs==[0,4,6,4]
xm=0;vm=0
for dt,Fk in seg: ak=Fr(abs(Fk),m17); xm+=vm*dt+ak*dt*dt/2; vm+=ak*dt
assert xm==40
G17=['\\begin{axis}[width=6.4cm,height=5cm,xmin=0,xmax=6,ymin=-12,ymax=12,xtick={0,1,2,3,4,5,6},ytick={-12,-8,-4,0,4,8,12},grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={$t$ (s)},ylabel={$F$ (N)}]',
 '\\addplot[black,thin] coordinates {(0,0)(6,0)};','\\addplot[vurgu,very thick] coordinates {(0,8)(2,8)(2,-12)(4,-12)(4,4)(6,4)};','\\end{axis}']
S=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(G17)+TAIL)
Q('nw-grafik','Kuvvet–zaman grafiğinden konum','zor','F–t Grafiği ve Hareket','Her aralıkta ivme a = F ÷ m sabittir; hız ve konum aralık aralık hesaplanır, kuvvetin işareti ivmenin yönünü belirler.','Negatif kuvveti büyüklük olarak almak; hız sıfırlanınca cismin başlangıca döndüğünü sanmak; grafiğin altındaki alanı doğrudan konum sanmak.','grafik',
 'Sürtünmesiz yatay düzlemde durgun hâldeki 4 kg kütleli bir cisme doğrusal yol boyunca etki eden yatay kuvvetin zamanla değişimi şekildeki grafikte verilmiştir. Pozitif yön, cismin ilk hareket yönüdür.\nBuna göre, cismin t = 6 s anında başlangıç konumuna göre konumu kaç m’dir?',
 'Cismin t = 6 s anındaki konumu (m).','Her 2 s’lik aralık için ivmeyi ve aralık sonundaki hızı sırayla hesapla; ardından konum değişimlerini topla.',
 [B('Düzgün ivmeli hareket','Δx = v₀·t + ½·a·t²; v = v₀ + a·t. Örnek: v₀ = 2 m/s, a = 1 m/s², t = 2 s → Δx = 6 m')],
 [A('0–2 s','a = 8 ÷ 4 = 2 m/s².','v = 4 m/s · Δx = ½·2·2² = 4 m'),A('2–4 s','a = −12 ÷ 4 = −3 m/s².','v = 4 − 6 = −2 m/s · Δx = 4·2 − ½·3·4 = 2 m'),A('4–6 s','a = 4 ÷ 4 = 1 m/s².','v = −2 + 2 = 0 · Δx = −2·2 + ½·1·4 = −2 m'),A('Konum','Yer değiştirmeleri topla.','x = 4 + 2 − 2 = 4 m')],
 'Kuvvet işaret değiştirince ivme ve hız yönü de değişir; her aralığı ayrı hesapla.',sekil=S,
 dogru=4,yan=[(0,'Son hızın sıfır olmasından cismin başlangıçta durduğunu (konum 0) sanmış.','bilgi'),(2,'Yalnız ikinci aralığın yer değiştirmesini (2 m) vermiş.','dikkat'),(6,'t = 4 s anındaki konumu (6 m) vermiş; son aralığı hesaba katmamış.','dikkat'),(40,'Negatif kuvveti pozitif almış: tüm aralıklarda hızlanma sanıp 4 + 14 + 22 = 40 m bulmuş.','islem')])

# ===== 18 · eğik düzlemde çekme, kuvvet kalkınca · zor =====
m18,u18,F18,t18=5,0.5,60,2; a_up=Fr(F18-m18*g*3//5-0,1) ; a_up=(Fr(F18)-30-Fr(1,2)*40)/m18; v18=a_up*t18; a_dn=(30+20)/Fr(m18); dist=v18**2/(2*a_dn)
assert a_up==2 and v18==4 and a_dn==10 and dist==Fr(4,5) and Fr(v18,a_dn)==Fr(2,5) and v18**2/(2*Fr(20,5))==2 and v18**2/(2*a_up*Fr(1,1))/1==4 and v18**2/(2*10)*2==Fr(8,5)
v_nf=Fr(F18-30,m18)*t18; assert v_nf==12 and v_nf**2/(2*a_dn)==Fr(36,5)
o,u,n,c=egik(4,3,2.2,1.0,.7,'5 kg')
bs=((c[1][0]+c[2][0])/2,(c[1][1]+c[2][1])/2); be=(bs[0]+1.0*u[0],bs[1]+1.0*u[1])
S=tk(*o,arr(bs[0],bs[1],be[0],be[1],'','above'),f'\\node[vurgu,above left] at ({be[0]:.3f},{be[1]:.3f}) {{$F=60$ N}};','\\node at (3.05,.35) {$\\mu_k=0{,}5$};')
Q('nw-egik','Çekilen cismin kuvvet kalktıktan sonraki hareketi','zor','Eğik Düzlemde Hareket','Kuvvet varken ve kalktıktan sonra net kuvvet farklıdır; yukarı hareket eden cismi paralel bileşen ve sürtünme birlikte yavaşlatır.','Kuvvet kalktıktan sonra sürtünme yönünü değiştirmemek; yavaşlamada yalnız bir kuvveti hesaba katmak; yolu v²/a ile bulup 2 çarpanını unutmak.','şekilli',
 'Şekildeki 37° eğimli ve pürüzlü eğik düzlemin yüzeyi boyunca yukarı doğru uygulanan 60 N’luk kuvvetle, düzlemde durgun hâldeki 5 kg kütleli cisim hareket ettiriliyor. Kuvvet t = 2 s anında kaldırılıyor ve cisim bir süre daha yukarı doğru gidiyor. Kinetik sürtünme katsayısı şekilde verilmiştir.\n(g = 10 m/s², sin 37° = 0,6, cos 37° = 0,8)\nBuna göre, kuvvet kaldırıldıktan sonra cismin durana kadar eğik düzlemde aldığı yol kaç m’dir?',
 'Kuvvet kalktıktan sonra durana kadar alınan yol (m).','İki evre için net kuvvetleri ayrı ayrı yaz; birinci evrenin sonundaki hızı ikinciye başlangıç hızı olarak kullan.',
 [B('Eğik düzlemde kuvvetler','Yukarı hareketteki cisme paralel bileşen (m·g·sinθ) ve sürtünme (μ·m·g·cosθ) aşağı yönde etkir. Örnek: 2 kg, 37°, μ = 0,5 → 12 N ve 8 N'),B('Yol','v² = v₀² − 2·a·x; durana kadar yol x = v₀² ÷ 2a')],
 [A('Kuvvetli evre','Yukarı: F; aşağı: paralel bileşen ve sürtünme.','60 − 30 − 20 = 5·a₁ → a₁ = 2 m/s²'),A('Evre sonu hızı','2 s boyunca.','v = 2 · 2 = 4 m/s'),A('Kuvvet kalkınca','Cisim yukarı gidiyor; iki kuvvet de aşağı yönlü.','30 + 20 = 5·a₂ → a₂ = 10 m/s² (yavaşlama)'),A('Durma yolu','v² = 2·a₂·x.','16 = 2 · 10 · x → x = 0,8 m')],
 'Yukarı giden cismi hem paralel bileşen hem sürtünme yavaşlatır; kuvvet kalkınca yalnız bu ikisi kalır.',sekil=S,
 dogru=Fr(4,5),yan=[(7.2,'Birinci evrede sürtünmeyi unutmuş: a₁ = (60 − 30) ÷ 5 = 6, v = 12 m/s, x = 144 ÷ 20 = 7,2 m.','dikkat'),(1.6,'Yolu v²/a = 16 ÷ 10 olarak bulmuş (½ çarpanını unutmuş).','islem'),(2,'Yavaşlamada yalnız sürtünmeyi (20 N → 4 m/s²) hesaba katmış: 16 ÷ 8.','bilgi'),(4,'Sürtünmeyi yanlış yönde alıp yavaşlamayı (30 − 20) ÷ 5 = 2 m/s² bulmuş: 16 ÷ 4.','bilgi')])

# ===== 19 · iki ipli düşey sistem, ip dayanımı · orta =====
mU,mL2,TU,TL=6,4,150,52
aU=Fr(TU,mU+mL2)-g; aL=Fr(TL,mL2)-g; amax=min(aU,aL)
assert aU==5 and aL==3 and amax==3 and Fr(TU,mU+mL2)==15 and Fr(TL,mL2)==13 and TL<mL2*(g+aU)
Q('nw-asansor','İki ipli düşey sistemde dayanım sınırı','orta','İvmeli Düzeneklerde Kuvvet','Her ipin taşıdığı kütle grubu için T = m(g + a) yazılır; ipler farklı sınırlara sahipse ivmeyi en kısıtlayıcı ip belirler.','Ağırlığı hesaba katmadan T = m·a yazmak; yalnız bir ipi denetlemek.','düz',
 'Bir vinç, kütleleri 6 kg ve 4 kg olan iki yükü düşey doğrultuda yukarı çekmektedir: vincin ipi 6 kg’lık yüke, 6 kg’lık yük de 4 kg’lık yüke ikinci bir iple bağlanmıştır. Vinç tarafındaki ip en fazla 150 N, iki yükü bağlayan ip ise en fazla 52 N’luk gerilme kuvvetine dayanabilmektedir. İplerin kütlesi önemsizdir.\n(g = 10 m/s²)\nBuna göre, ipler kopmadan yüklerin ulaşabileceği en büyük ivmenin büyüklüğü kaç m/s²’dir?',
 'Yüklerin alabileceği en büyük ivme (m/s²).','Her ipin hangi kütleleri taşıdığını belirle ve iplerin her biri için ayrı bir sınır ivmesi bul.',
 [B('Düşey ivmeli hareket','Yukarı ivmede T − m·g = m·a. Örnek: 2 kg, a = 3 m/s² → T = 26 N')],
 [A('Üst ip','Üst ip iki yükü (10 kg) taşır.','150 = 10·(10 + a) → a ≤ 5 m/s²'),A('Alt ip','Alt ip yalnız 4 kg’lık yükü taşır.','52 = 4·(10 + a) → a ≤ 3 m/s²'),A('Sınırlayıcı ip','İki koşul birlikte sağlanmalı.','a_en çok = 3 m/s²')],
 'Birden çok ipte en küçük sınır ivmesi geçerlidir; her ip, altında kalan kütleleri taşır.',
 dogru=3,yan=[(5,'Yalnız vinç tarafındaki ipi denetlemiş; alt ip 5 m/s² ivmede 4·15 = 60 N > 52 N ile kopar.','dikkat'),(10,'g’yi (10 m/s²) ivme sanmış.','dikkat'),(13,'Alt ip için ağırlığı hesaba katmadan a = T ÷ m = 52 ÷ 4 yazmış.','bilgi'),(15,'Üst ip için ağırlığı hesaba katmadan a = 150 ÷ 10 yazmış.','bilgi')])

# ===== 20 · etki–tepki · orta · öncüllü =====
mA20,mB20=60,40; assert Fr(mB20,mA20)==Fr(2,3)
tr=[False,True,False]; nd=['etki–tepki çiftinin kuvvetleri her zaman eşit büyüklüktedir','F = m·a’da kuvvet eşit olduğundan kütlesi küçük olanın ivmesi büyüktür (40 kg → B)','a_A ÷ a_B = m_B ÷ m_A = 40 ÷ 60 = 2/3’tür; A’nın ivmesi B’ninkinin 3/2 katı değildir']
d,y,sr=onc(tr,nd,['Yalnız I','Yalnız II','Yalnız III','I ve III','I, II ve III'])
Q('nw-kavram','Etki–tepki ve ivmelerin oranı','kolay','Etki–Tepki Yasası','Etki–tepki kuvvetleri eşit büyüklükte ve zıt yönlüdür; aynı büyüklükteki kuvvet kütlesi küçük cisme daha büyük ivme kazandırır.','Güçlü iteni daha büyük kuvvet uygulamış sanmak; kuvvet eşit diye ivmeleri de eşit sanmak.','öncüllü',
 'Sürtünmesiz buz pistinde durgun hâldeki kütlesi 60 kg olan A ile kütlesi 40 kg olan B, ellerini birbirine dayayıp A’nın B’yi itmesiyle birbirinden uzaklaşmaktadır. İtme sırasında iki kişi arasındaki temas sürmektedir.\nBuna göre, itme sürerken,\nI. A’nın B’ye uyguladığı kuvvet, B’nin A’ya uyguladığı kuvvetten büyüktür.\nII. B’nin ivmesinin büyüklüğü A’nınkinden büyüktür.\nIII. A’nın ivmesinin büyüklüğü, B’nin ivmesinin büyüklüğünün 3/2 katıdır.\nyargılarından hangileri doğrudur?',
 'Doğru olan öncüllerin belirlenmesi.','İki kişinin birbirine uyguladığı kuvvetleri karşılaştır, sonra ivmeleri F = m·a ile yaz.',
 [B('Etki–tepki yasası','Bir cisim ötekine kuvvet uygularsa diğeri de ona eşit büyüklükte, zıt yönlü kuvvet uygular. Örnek: 30 N itme → 30 N tepki')],
 oadim(tr,nd)+[A('Sonuç','Yalnız II doğru.','Yalnız II')],'Etki–tepki kuvvetleri eşittir; ivmeler kütleyle ters orantılıdır.',
 dogru=d,yan=y,sira=sr)

# ===== yaz =====
def bitir_afiz():
    for qq in P.ANA: qq['kardes']=None
    P.yaz(os.path.join(GD,'newton-1.json'),'/tmp/bos-newton.json')
    tipler={}
    for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|'+KONU))['kartlar'].append(c['id'])
    json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 fizik soruları (yalnız mantık), MEB 11. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar','afnewton.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler),'sorular',len(P.ANA))
bitir_afiz()
