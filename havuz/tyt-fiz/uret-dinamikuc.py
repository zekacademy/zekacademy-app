"""TYT Fizik · Dinamik (üçüncü/dördüncü genişletme) · 10 soru.
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
KONU='Dinamik'; H.KONU=KONU
P=Parti('dinamikuc','Dinamik','fiz|Dinamik',ders='TYT Fizik',idon='tytfiz')
KAYNAK='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9–10. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'
TAIL='\n\\end{tikzpicture}'
def tk(body): return tikz_svg(HEAD+body+TAIL)
def nn(no): return f'{int(no):02d}'
def kartk(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZDN3-{nn(no)}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)

# ---------- sayısal soru ----------
def N(no,tipId,tip,alt,z,kaz,fikir,tuzak,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,kalip=None,sira=None):
    kalip=kalip or ('şekilli' if sekil else 'düz')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZDN3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı',kisa=None,sira=sira)

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
       kalip=kalip,adim=len(ad),kart=f'K-FZDN3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı')

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
# =============== 01 · dik kuvvetlerin bileşkesi (üstten görünüm) · sayısal · kolay ===============
Fe,Fw,Fn,m1=9,5,3,Fr(5,2)
nx,ny=Fe-Fw,Fn; Fnet=math.hypot(nx,ny); assert Fnet==5.0
a1=Fr(5)/m1; assert a1==2
assert {Fr(3)/m1,Fr(4)/m1,Fr(Fe+Fw+Fn)/m1,Fr(Fe-Fw+Fn)/m1}=={Fr(6,5),Fr(8,5),Fr(34,5),Fr(7,2.5).limit_denominator(10) if False else Fr(14,5)}
sc_=.22
sk=('\\draw[thick,fill=gray!25] (-.55,-.55) rectangle (.55,.55); \\node at (0,0) {$2{,}5$ kg};\n'
    f'\\draw[vurgu,very thick,{ARR}] (.55,0) -- ({.55+Fe*sc_:.2f},0); \\node[vurgu,above] at ({.55+Fe*sc_/2:.2f},0) {{$9$ N}};\n'
    f'\\draw[vurgu,very thick,{ARR}] (-.55,0) -- ({-.55-Fw*sc_:.2f},0); \\node[vurgu,above] at ({-.55-Fw*sc_/2:.2f},0) {{$5$ N}};\n'
    f'\\draw[vurgu,very thick,{ARR}] (0,.55) -- (0,{.55+Fn*sc_:.2f}); \\node[vurgu,right] at (0,{.55+Fn*sc_/2:.2f}) {{$3$ N}};\n'
    '\\node[font=\\small] at (0,-1.1) {yukarıdan görünüm};')
N('0001','fz-dn3-net','Net kuvvet ve ivme','Newton’ın Hareket Yasaları','kolay',
 'Aynı düzlemde, birbirine dik doğrultulardaki kuvvetlerin bileşkesini bulur ve ivmeyi Newton’ın ikinci yasasıyla hesaplar.',
 'Zıt yönlü kuvvetler aynı doğrultuda çıkarılır; birbirine dik bileşenlerin bileşkesi Pisagor ile bulunur ve ivme bileşkenin kütleye oranıdır.',
 'Kuvvetlerin büyüklüklerini düz toplamak; dik kuvvetleri de cebirsel toplamak; yalnız bir doğrultuyu hesaba katmak.',
 'Şekilde, sürtünmesiz yatay bir masa üzerinde durmakta olan cisme masa düzleminde etkiyen üç kuvvet, yukarıdan görünüşle verilmiştir. Kuvvetlerin büyüklükleri ve cismin kütlesi şekildedir.\nBuna göre, cismin ivmesinin büyüklüğü kaç m/s²’dir?',
 2,[(Fr(6,5),'Yalnız 3 N’luk kuvveti dikkate almış: 3 ÷ 2,5 = 1,2 m/s².','dikkat'),(Fr(8,5),'Yalnız yatay doğrultudaki net kuvveti (9 − 5 = 4 N) almış: 4 ÷ 2,5 = 1,6 m/s².','dikkat'),
    (Fr(14,5),'Kuvvetleri cebirsel toplamış: (9 − 5 + 3) ÷ 2,5 = 2,8 m/s²; dik kuvvetler Pisagor ile birleşir.','bilgi'),(Fr(34,5),'Büyüklükleri düz toplamış: (9 + 5 + 3) ÷ 2,5 = 6,8 m/s².','bilgi')],
 'Cismin ivmesinin büyüklüğü (m/s²).',
 ['Kuvvetlerin doğrultularına bak: hangileri aynı doğrultuda, hangileri birbirine dik?'],
 [B('Bileşke kuvvet','aynı doğrultuda zıt yönlü kuvvetler çıkarılır; birbirine dik iki kuvvetin bileşkesi F = √(F₁² + F₂²) ile bulunur. Örnek: 6 N ve 8 N’luk dik kuvvetlerin bileşkesi 10 N’dur')],
 [A('Yatay doğrultuyu birleştir','Zıt yönlü kuvvetler çıkarılır.','F_x = 9 − 5 = 4 N'),
  A('Bileşkeyi bul','Yatay (4 N) ve düşey (3 N) kuvvetler birbirine diktir.','F = √(4² + 3²) = 5 N'),
  A('İvmeyi hesapla','a = F ÷ m.','a = 5 ÷ 2,5 = 2 m/s²')],
 'Dik kuvvetlerin bileşkesi için önce her doğrultuyu ayrı ayrı birleştir, sonra Pisagor kullan.',sekil=tk(sk))

# =============== 02 · sürtünme kuvveti–uygulanan kuvvet grafiği · öncüllü · orta ===============
m2=5; fk=15; fsmax=20
assert Fr(fk,m2*10)==Fr(3,10) and Fr(25-fk,m2)==2 and 15<fsmax
sk=GR('7.6cm','5.2cm',30,25,5,5,'$F$ (N)','sürtünme kuvveti (N)','\\addplot[thick,vurgu] coordinates {(0,0) (20,20)};','\\addplot[thick,vurgu,dashed] coordinates {(20,20) (20,15)};','\\addplot[thick,vurgu] coordinates {(20,15) (30,15)};')
O('0002','fz-dn3-surtunme','Sürtünme kuvveti','Sürtünme Kuvveti','orta',
 'Sürtünme kuvvetinin uygulanan kuvvetle değişimini gösteren grafikten statik ve kinetik sürtünmeyi, katsayıyı ve ivmeyi yorumlar.',
 'Cisim kıpırdamadan önce sürtünme uygulanan kuvvete eşittir; hareket başlayınca sabit kinetik sürtünme etkir ve ivme (F − f_k) ÷ m ile bulunur.',
 'Statik sürtünme kuvvetini hep sabit sanmak; grafikteki yüksek değeri kinetik sürtünme almak.',
 'Yatay bir zeminde durmakta olan 5 kg kütleli cisme, yatay doğrultuda büyüklüğü sıfırdan başlayarak yavaşça artan bir F kuvveti uygulanıyor. Cisim ile zemin arasındaki sürtünme kuvvetinin F’ye göre değişimi grafikte verilmiştir (g = 10 m/s²).',
 [('F = 15 N iken cisim ivmeli hareket eder.',False,'Grafikte F = 15 N’de sürtünme kuvveti de 15 N’dur; net kuvvet sıfırdır ve cisim durgun kalır.','Uygulanan kuvvet 15 N olduğunda sürtünme 15 N olsa da cismin harekete geçtiğini düşünmüş.'),
  ('Cisimle zemin arasındaki kinetik sürtünme katsayısı 0,3’tür.',True,'Hareket başladıktan sonra sürtünme 15 N’dur; f = μ·N ve N = 50 N olduğundan μ = 15 ÷ 50 = 0,3.','Grafikteki en büyük değer olan 20 N’u kinetik sürtünme alarak katsayıyı 0,4 bulmuş.'),
  ('F = 25 N iken cismin ivmesi 2 m/s²’dir.',True,'Cisim hareket hâlindedir; a = (25 − 15) ÷ 5 = 2 m/s².','25 N’dan sürtünmeyi 20 N çıkararak ivmeyi 1 m/s² bulmuş.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('Grafikte sürtünme önce F’yi izler (0–20 N), sonra sabit 15 N olur.','f_s,maks = 20 N · f_k = 15 N'),
 ['Cismin hangi F değerinde harekete geçtiğini grafikten bul; hareketten sonra sürtünme kuvvetinin değerini oku.'],
 [B('Statik ve kinetik sürtünme','cisim kıpırdamadan önce sürtünme uygulanan kuvvete eşittir ve belli bir en büyük değere ulaşır; hareket başladıktan sonra kinetik sürtünme sabittir: f = μ·N. Örnek: N = 40 N ve μ = 0,25 ise f = 10 N')],
 'Sürtünme grafiğinde önce statik bölgeyi, sonra kinetik sabit değeri oku; ivmede sabit olan kinetik sürtünmeyi kullan.',sekil=sk,kalip='grafik')

# =============== 03 · Atwood · sayısal · orta ===============
mA,mB=3,1; a3=Fr((mA-mB)*10,mA+mB); T3=mB*(10+a3)
assert (a3,T3)==(5,15) and T3==mA*(10-a3)
assert (mB*10,mA*10,a3)==(10,30,5)
sk=('\\draw[thick,fill=white] (0,0) circle (.35); \\fill (0,0) circle (1.5pt); \\draw[very thick] (0,.35) -- (0,.8); \\draw[thick] (-.55,.8) -- (.55,.8); \\foreach \\x in {-.5,-.3,...,.5} \\draw[thin] (\\x,.8) -- (\\x+.15,.95);\n'
    '\\draw[thick] (-.35,0) -- (-.35,-1.5); \\draw[thick] (.35,0) -- (.35,-2.3);\n'
    '\\draw[thick,fill=gray!40] (-.75,-2.1) rectangle (.05,-1.5); \\node at (-.35,-1.8) {$3$ kg};\n'
    '\\draw[thick,fill=gray!25] (-.02,-2.85) rectangle (.72,-2.3); \\node at (.35,-2.58) {\\small $1$ kg};')
N('0003','fz-dn3-makara','Makara ve dinamometre sistemleri','Newton’ın Hareket Yasaları','orta',
 'Sabit makaradan geçen iple bağlı iki asılı cismin ivmesini ve ip gerilmesini bulur.',
 'Cisimler aynı büyüklükte ivmeyle hareket eder; ağır cisim aşağı iner. Sistem için ΣF = (m₁ + m₂)·a, tek bir cisim için ip gerilmesi bulunur.',
 'Gerilmeyi hafif ya da ağır cismin ağırlığına eşit almak; ivmeyi gerilme sanmak.',
 'Şekildeki düzenekte kütleleri şekilde verilen cisimler, sürtünmesiz ve kütlesi önemsenmeyen bir makaradan geçen hafif, esnemeyen bir iple bağlanmıştır. Sistem serbest bırakılıyor (g = 10 m/s²).\nBuna göre, ipteki gerilme kuvveti kaç N’dur?',
 15,[(5,'İvmeyi (5 m/s²) gerilme olarak yazmış.','dikkat'),(10,'Gerilmeyi hafif cismin ağırlığına (1 × 10 = 10 N) eşit almış; cisim ivmeli hareket eder.','bilgi'),
     (20,'Net kuvveti (30 − 10 = 20 N) gerilme sanmış.','islem'),(30,'Gerilmeyi ağır cismin ağırlığına (3 × 10 = 30 N) eşit almış.','bilgi')],
 'İpteki gerilme kuvveti (N).',
 ['İpteki gerilme hangi niceliklerden etkilenir? Cisimlerin ivmeli hareket edip etmediğini düşün.'],
 [B('Newton’ın ikinci yasası','ΣF = m·a. İple bağlı cisimlerin ivmeleri büyüklükçe aynıdır. Örnek: 10 N’luk net kuvvet 2 kg’lık cisme 5 m/s² ivme verir')],
 [A('Ortak ivmeyi bul','Sistemi hareket ettiren net kuvvet ağırlıklar farkıdır.','30 − 10 = (3 + 1) × a → a = 5 m/s²'),
  A('Hafif cisme uygula','Hafif cisim yukarı ivmelenir: T − m₂·g = m₂·a.','T − 10 = 1 × 5'),
  A('Gerilmeyi bul','Hafif cismin hareket denklemindeki değerleri yerine koy.','T = 10 + 5 = 15 N')],
 'Asılı iki cisimde önce sistemin ivmesini bul; gerilme iki ağırlığın arasında bir değerdedir.',sekil=tk(sk))

# =============== 04 · sabit hızlı hareket, sürtünme (öncüllü) · orta ===============
m4=5; F4=20; f4=F4
a_30=Fr(30-f4,m4); a_off=Fr(-f4,m4)
assert f4==20 and a_30==2 and a_off==-4
sk=('\\fill[gray!30] (-.5,-.2) rectangle (5.2,0); \\draw (-.5,0) -- (5.2,0);\n'
    '\\draw[thick,fill=gray!25] (1.3,0) rectangle (2.7,.9); \\node at (2.0,.45) {$5$ kg};\n'
    f'\\draw[vurgu,very thick,{ARR}] (2.7,.45) -- (4.2,.45); \\node[vurgu,above] at (3.45,.48) {{$20$ N}};\n'
    f'\\draw[very thick,{ARR}] (1.3,1.25) -- (2.7,1.25); \\node[above] at (2.0,1.3) {{$v$ (sabit)}};')
O('0004','fz-dn3-net','Net kuvvet ve ivme','Sürtünme Kuvveti','orta',
 'Sabit hızlı harekette net kuvvetin sıfır olmasından sürtünmeyi bulur; kuvvet değişince ya da kaldırılınca ivmeyi yorumlar.',
 'Sabit hızda net kuvvet sıfırdır; kinetik sürtünme uygulanan kuvvete eşittir ve kuvvet değişse de sabit kalır. Net kuvvet farkı ivme verir.',
 'Sabit hızda kuvvetin ve sürtünmenin olmadığını sanmak; kuvvet kalkınca cismin hemen durduğunu düşünmek.',
 'Yatay ve sürtünmeli bir zeminde 5 kg kütleli cisim, şekildeki yatay kuvvetle çekilerek sabit hızla hareket etmektedir. Kinetik sürtünme kuvveti, hızdan bağımsızdır.',
 [('Cisme etkiyen sürtünme kuvveti 20 N’dur.',True,'Sabit hızda ivme sıfırdır; net kuvvet sıfır olduğundan sürtünme kuvveti çekme kuvvetine eşittir.','Sabit hızda sürtünme olmadığını düşünmüş.'),
  ('Çekme kuvveti 30 N yapılırsa cismin ivmesi 6 m/s² olur.',False,'Sürtünme 20 N kalır; net kuvvet 30 − 20 = 10 N olur ve a = 10 ÷ 5 = 2 m/s²’dir.','Sürtünmeyi hesaba katmadan 30 ÷ 5 = 6 bulmuş.'),
  ('Çekme kuvveti kaldırılırsa cisim hemen durur.',False,'Kuvvet kalkınca cisim hızıyla hareket eder; yalnız 20 N’luk sürtünme etkir ve cisim 4 m/s² ivmeyle yavaşlayarak durur.','Kuvvet kalkınca cismin anında duracağını sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('Sabit hız → net kuvvet 0.','F = f_k = 20 N'),
 ['Sabit hızlı harekette cisme etkiyen net kuvvetin değeri nedir? Bunu sürtünmeyle ilişkilendir.'],
 [B('Newton’ın birinci ve ikinci yasası','net kuvvet sıfırsa cisim sabit hızla (ya da durgun) kalır; net kuvvet varsa ΣF = m·a kadar ivme kazanır. Örnek: 12 N net kuvvet 4 kg’a 3 m/s² verir')],
 'Sabit hızda net kuvvet sıfırdır; kuvvet değişince net kuvvet farkı ivmeyi, sürtünme sabit kalır.',sekil=tk(sk))

# =============== 05 · yukarı eğik kuvvet ve sürtünme · sayısal · zor ===============
m5,F5,mu5=10,50,Fr(1,2); s37,c37=Fr(3,5),Fr(4,5)
N5=m5*10-F5*s37; f5=mu5*N5; a5=(F5*c37-f5)/m5
assert (N5,f5,a5)==(70,35,Fr(1,2))
d1=(F5*c37-mu5*m5*10)/m5; assert d1<0
assert (F5*c37)/m5==4 and F5-f5==15 and (F5*c37-mu5*(m5*10-F5*c37))/m5==1
th=math.radians(37)
sk=('\\fill[gray!30] (-.5,-.2) rectangle (5.2,0); \\draw (-.5,0) -- (5.2,0);\n'
    '\\draw[thick,fill=gray!25] (1.3,0) rectangle (2.7,.9); \\node at (2.0,.45) {$10$ kg};\n'
    f'\\draw[vurgu,very thick,{ARR}] (2.7,.45) -- ({2.7+1.5*math.cos(th):.3f},{.45+1.5*math.sin(th):.3f}); \\node[vurgu,above] at (3.45,1.25) {{$50$ N}};\n'
    f'\\draw[thin] (2.7,.45) -- (4.4,.45); \\draw[thin] (3.2,.45) arc[start angle=0,end angle=37,radius=.5]; \\node at (3.55,.62) {{\\scriptsize $37^\\circ$}};\n'
    '\\node[font=\\small] at (0.6,.45) {$\\mu=0{,}5$};')
N('0005','fz-dn3-surtunme','Sürtünme kuvveti','Sürtünme Kuvveti','zor',
 'Yatayla açı yapan çekme kuvvetinin bileşenlerini ve azalan normal kuvveti kullanarak sürtünmeli zeminde ivmeyi bulur.',
 'Yukarı eğik kuvvetin düşey bileşeni normal kuvveti azaltır; sürtünme f = μ·N yeni normal kuvvetle bulunur, yatay bileşen ile sürtünme farkı ivme verir.',
 'Normal kuvveti cismin ağırlığına eşit almak; kuvvetin tamamını yatay saymak; sürtünmeyi unutmak.',
 'Yatay bir zeminde duran 10 kg kütleli cisim, yatayla 37° açı yapan 50 N’luk kuvvetle şekildeki gibi çekilmektedir. Cisim ile zemin arasındaki kinetik sürtünme katsayısı şekilde verilmiştir (g = 10 m/s², sin37° = 0,6, cos37° = 0,8).\nBuna göre, cismin ivmesi kaç m/s²’dir?',
 Fr(1,2),[(0,'Normal kuvveti ağırlığa eşit alıp sürtünmeyi 50 N bulmuş; yatay bileşen (40 N) bunu yenemediğinden cismi durgun sanmış.','bilgi'),
    (1,'Normal kuvveti ağırlıktan yatay bileşeni çıkararak (100 − 40 = 60 N) bulmuş: f = 30 N, a = 1 m/s².','islem'),
    (Fr(3,2),'Yatay bileşen yerine 50 N’u alıp sürtünmeyi doğru (35 N) bulmuş: (50 − 35) ÷ 10 = 1,5 m/s².','dikkat'),(4,'Sürtünmeyi hiç hesaba katmamış: 40 ÷ 10 = 4 m/s².','dikkat')],
 'Cismin ivmesi (m/s²).',
 ['Çekme kuvvetini yatay ve düşey bileşenlerine ayır; düşey bileşenin normal kuvveti nasıl değiştirdiğini düşün.'],
 [B('Kuvvet bileşenleri','θ açısıyla etkiyen F kuvvetinin yatay bileşeni F·cosθ, düşey bileşeni F·sinθ’dır. Örnek: 10 N’luk kuvvet 37° açıyla etkirse bileşenler 8 N ve 6 N’dur'),
  B('Normal kuvvet ve sürtünme','dikey kuvvetlerin dengesinden normal kuvvet bulunur; kinetik sürtünme f = μ·N’dir')],
 [A('Bileşenleri bul','F_x = 50 × 0,8, F_y = 50 × 0,6.','F_x = 40 N · F_y = 30 N'),
  A('Normal kuvveti bul','Düşeyde denge: N + F_y = m·g.','N = 100 − 30 = 70 N'),
  A('Sürtünmeyi bul','f = μ·N.','f = 0,5 × 70 = 35 N'),
  A('İvmeyi hesapla','Yatayda ΣF = m·a.','40 − 35 = 10 × a → a = 0,5 m/s²')],
 'Yukarı eğik çekmede normal kuvvet ağırlıktan küçüktür; sürtünmeyi hesaplarken ağırlığı değil N’yi kullan.',sekil=tk(sk))

# =============== 06 · dinamometre, iki yanda asılı kütleler · sayısal · kolay ===============
mD=4; Dn=mD*10
assert Dn==40 and 2*Dn==80 and Dn//2==20
sk=('\\draw[thick,fill=gray!15] (-.9,-.25) rectangle (.9,.25); \\node at (0,0) {\\scriptsize dinamometre};\n'
    '\\draw[thick] (-.9,0) -- (-2.4,0); \\draw[thick] (.9,0) -- (2.4,0);\n'
    '\\foreach \\x in {-2.4,2.4} {\\draw[thick,fill=white] (\\x,-.0) circle (.28); \\draw[very thick] (\\x,.28) -- (\\x,.6); \\draw[thick] (\\x-.45,.6) -- (\\x+.45,.6);}\n'
    '\\draw[thick] (-2.68,0) -- (-2.68,-1.4); \\draw[thick] (2.68,0) -- (2.68,-1.4);\n'
    '\\draw[thick,fill=gray!40] (-3.08,-2.0) rectangle (-2.28,-1.4); \\node at (-2.68,-1.7) {$4$ kg}; \\draw[thick,fill=gray!40] (2.28,-2.0) rectangle (3.08,-1.4); \\node at (2.68,-1.7) {$4$ kg};')
N('0006','fz-dn3-makara','Makara ve dinamometre sistemleri','Newton’ın Hareket Yasaları','kolay',
 'İki ucundan eşit kuvvetle çekilen dinamometrenin, uygulanan kuvvetin tek bir değerini gösterdiğini bilir ve okumayı belirler.',
 'Durgun sistemde ip gerilmesi her iki yanda ağırlığa eşittir; dinamometre, kendisine uygulanan kuvvetlerden birinin büyüklüğünü gösterir, toplamını değil.',
 'Her iki yanın ağırlığını toplamak; zıt kuvvetlerin birbirini götürdüğünü düşünüp sıfır okumak.',
 'Şekilde kütleleri 4 kg olan iki cisim, sürtünmesiz ve kütlesi önemsenmeyen iki makaradan geçen hafif iplerle, kütlesi ihmal edilen bir dinamometrenin iki ucuna bağlanmıştır. Sistem durgun ve dengededir (g = 10 m/s²).\nBuna göre, dinamometre kaç N’u gösterir?',
 40,[(0,'Zıt yönlü iki kuvvetin birbirini götürdüğünü düşünüp dinamometrenin sıfır göstereceğini sanmış.','bilgi'),(4,'Kütle değerini (4 kg) kuvvet sanmış; ağırlığı bulmak için g ile çarpmayı unutmuş.','dikkat'),
     (20,'Ağırlığın (40 N) yarısını almış; iki ucu paylaştığını sanmış.','bilgi'),(80,'İki ağırlığı toplamış: 40 + 40 = 80 N.','islem')],
 'Dinamometrenin gösterdiği değer (N).',
 ['Dinamometreyi çeken kuvvetleri ayrı ayrı yaz.'],
 [B('Dinamometre','kendisine uygulanan kuvvetin büyüklüğünü ölçer; iki ucundan zıt yönde aynı büyüklükte kuvvet uygulanırsa bu büyüklüğü gösterir. Örnek: iki ucundan 6 N’la çekilen dinamometre 6 N gösterir')],
 [A('Ağırlığı bul','Cisimler durgun olduğundan ip gerilmesi ağırlığa eşittir.','T = 4 × 10 = 40 N'),
  A('Dinamometreye uygulanan kuvveti bul','Kütlesi ihmal edilen dinamometrenin her iki ucuna ip gerilmesi kadar kuvvet uygulanır.','Her uca 40 N'),
  A('Okumayı belirle','Dinamometre bir ucundaki kuvvetin büyüklüğünü gösterir.','Okuma = 40 N')],
 'Ölçü aletine etkiyen kuvvetleri ayrı ayrı belirleyip aletin neyi ölçtüğünü düşün.',sekil=tk(sk))

# =============== 07 · sürtünmenin bağlı olduğu etkenler · öncüllü · orta ===============
sk=('\\fill[gray!30] (-.5,-.2) rectangle (9.6,0); \\draw (-.5,0) -- (9.6,0);\n'
    '\\draw[thick,fill=gray!25] (0,0) rectangle (1.8,.9); \\node at (.9,.45) {$2$ kg}; \\node at (.9,-.55) {$K$};\n'
    '\\draw[thick,fill=gray!25] (3.4,0) rectangle (4.3,1.8); \\node at (3.85,.9) {$2$ kg}; \\node at (3.85,-.55) {$L$};\n'
    '\\draw[thick,fill=gray!25] (6.2,0) rectangle (8.0,.9); \\node at (7.1,.45) {$2$ kg}; \\draw[thick,fill=gray!50] (6.5,.9) rectangle (7.7,1.5); \\node at (7.1,1.2) {$2$ kg}; \\node at (7.1,-.55) {$M$};\n'
    +''.join(f'\\draw[vurgu,very thick,{ARR}] ({x2},{y2}) -- ({x2+ln},{y2});' for x2,y2,ln in ((1.8,.45,.8),(4.3,.9,.8),(8.0,.45,1.6))))
O('0007','fz-dn3-surtunme','Sürtünme kuvveti','Sürtünme Kuvveti','orta',
 'Kinetik sürtünme kuvvetinin yüzey alanına değil, normal kuvvete ve yüzey cinsine bağlı olduğunu yorumlar.',
 'Kinetik sürtünme f = μ·N ile bulunur; yüzey alanından ve hızdan bağımsızdır, normal kuvvet ve yüzeyin cinsine bağlıdır.',
 'Temas alanı büyüdükçe sürtünmenin arttığını sanmak; hız arttıkça sürtünmenin arttığını düşünmek.',
 'Aynı maddeden yapılmış, K ve L konumlarındaki 2 kg kütleli özdeş dikdörtgen bloklar farklı yüzleri üzerinde, M konumunda ise blok üstüne 2 kg’lık ek bir kütle konularak, aynı yatay zeminde şekildeki gibi sabit hızlarla çekilmektedir.',
 [('L konumundaki sürtünme kuvveti, K konumundakinden büyüktür.',False,'Kinetik sürtünme temas alanına bağlı değildir; iki durumda da normal kuvvet aynıdır, sürtünme kuvvetleri eşittir.','Temas alanı küçüldükçe sürtünmenin arttığını (ya da büyüdükçe arttığını) düşünmüş.'),
  ('M konumundaki sürtünme kuvveti, K konumundakinden büyüktür.',True,'M’de normal kuvvet iki katına çıkmıştır (4 kg’ın ağırlığı); f = μ·N olduğundan sürtünme de iki katıdır.','Üstüne konan kütlenin sürtünmeyi değiştirmeyeceğini düşünmüş.'),
  ('Bloğu daha büyük hızla çekmek, kinetik sürtünme kuvvetini artırır.',False,'Kinetik sürtünme kuvveti hızdan bağımsızdır; f = μ·N yalnız normal kuvvete ve yüzeye bağlıdır.','Hız arttıkça sürtünmenin arttığını sanmış.')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],
 ('K ve L’de normal kuvvet aynı; M’de ek kütle var.','N_K = N_L; N_M = 2·N_K'),
 ['Sürtünme kuvvetini belirleyen niceliklerin neler olduğunu düşün; her konumda bunların hangisinin değiştiğine bak.'],
 [B('Kinetik sürtünme','f = μ·N’dir; yalnız yüzeylerin cinsine ve normal kuvvete bağlıdır. Temas alanından ve hızdan bağımsızdır. Örnek: N = 20 N ve μ = 0,5 için f = 10 N')],
 'Kinetik sürtünmeyi artırmak için normal kuvveti ya da yüzeyin pürüzlülüğünü değiştir; alan ve hız etkili değildir.',sekil=tk(sk))

# =============== 08 · eğik düzlemde yukarı kuvvet ve sürtünme · sayısal · zor ===============
th8=math.radians(53); m8=5; F8=75; mu8=Fr(1,2); s53,c53=Fr(4,5),Fr(3,5)
g8=m8*10*s53; N8=m8*10*c53; f8=mu8*N8; a8=(F8-g8-f8)/m8
assert (g8,N8,f8,a8)==(40,30,15,4)
assert (F8-g8)/m8==7 and (F8-f8)/m8==12 and (F8-g8-mu8*m8*10)/m8==2 and F8/m8==15
Lk=3.2; Hk=Lk*math.sin(th8); Wk=Lk*math.cos(th8)
u8=(math.cos(th8),math.sin(th8)); n8=(-math.sin(th8),math.cos(th8)); bw,bh=1.2,.75
s0=1.5; c=[(s0*u8[0],s0*u8[1])]
pts=[(s0*u8[0]+dx*u8[0]*bw+dy*n8[0]*bh, s0*u8[1]+dx*u8[1]*bw+dy*n8[1]*bh) for dx,dy in ((0,0),(1,0),(1,1),(0,1))]
cen=((pts[0][0]+pts[2][0])/2,(pts[0][1]+pts[2][1])/2)
fa=(cen[0]+u8[0]*bw/2,cen[1]+u8[1]*bw/2); fb=(fa[0]+u8[0]*1.4,fa[1]+u8[1]*1.4)
sk=(f'\\fill[gray!30] (-.4,-.2) rectangle ({Wk+.6:.2f},0); \\draw (-.4,0) -- ({Wk+.6:.2f},0);\n'
    f'\\draw[thick] (0,0) -- ({Wk:.3f},{Hk:.3f}) -- ({Wk:.3f},0) -- cycle;\n'
    '\\draw[thick,fill=gray!25] '+' -- '.join(f'({x:.3f},{y:.3f})' for x,y in pts)+' -- cycle;\n'
    f'\\node[rotate=53] at ({cen[0]:.3f},{cen[1]:.3f}) {{$5$ kg}};\n'
    f'\\draw[vurgu,very thick,{ARR}] ({fa[0]:.3f},{fa[1]:.3f}) -- ({fb[0]:.3f},{fb[1]:.3f}); \\node[vurgu,right] at ({fb[0]:.3f},{fb[1]-.1:.3f}) {{$75$ N}};\n'
    '\\draw (.9,0) arc[start angle=0,end angle=53,radius=.9]; \\node at (1.25,.28) {\\scriptsize $53^\\circ$};\n'
    f'\\node[font=\\small] at ({Wk+1.0:.2f},.45) {{$\\mu=0{{,}}5$}};')
N('0008','fz-dn3-egik','Eğik düzlemde düzleme paralel kuvvetle yukarı çekilen cisim','Sürtünme Kuvveti','zor',
 'Eğik düzlemde ağırlığın düzleme paralel ve dik bileşenlerini kullanarak sürtünmeli yukarı harekette ivmeyi bulur.',
 'Normal kuvvet ağırlığın düzleme dik bileşenine, sürtünmeyi engelleyen bileşen ise ağırlığın düzleme paralel bileşenine eşittir; yukarı doğru net kuvvet ivmeyi verir.',
 'Ağırlığın bileşenlerini ters atamak; sürtünmeyi ya da paralel bileşeni unutmak; normal kuvveti mg almak.',
 'Şekildeki 53° eğimli eğik düzlemde 5 kg kütleli cisim, düzleme paralel ve yukarı yönlü 75 N’luk kuvvetle çekilmektedir. Cisim ile düzlem arasındaki kinetik sürtünme katsayısı şekilde verilmiştir (g = 10 m/s², sin53° = 0,8, cos53° = 0,6). Cisim yukarı doğru hareket etmektedir.\nBuna göre, cismin ivmesi kaç m/s²’dir?',
 4,[(2,'Normal kuvveti ağırlığa eşit almış: f = 0,5 × 50 = 25 N ve a = (75 − 40 − 25) ÷ 5 = 2 m/s².','bilgi'),
    (7,'Sürtünmeyi hesaba katmamış: (75 − 40) ÷ 5 = 7 m/s².','dikkat'),(12,'Ağırlığın düzleme paralel bileşenini unutmuş: (75 − 15) ÷ 5 = 12 m/s².','dikkat'),(15,'Yalnız çekme kuvvetini dikkate almış: 75 ÷ 5 = 15 m/s².','dikkat')],
 'Cismin ivmesi (m/s²).',
 ['Cismin ağırlığını düzleme paralel ve dik bileşenlerine ayır; hangisi normal kuvveti, hangisi harekete karşı kuvveti belirler?'],
 [B('Eğik düzlemde ağırlık','ağırlığın düzleme paralel bileşeni m·g·sinθ, dik bileşeni m·g·cosθ’dır. Örnek: 2 kg’lık cisim için 37° eğimli düzlemde bileşenler 12 N ve 16 N’dur')],
 [A('Ağırlığın bileşenleri','m·g = 50 N.','Paralel: 50 × 0,8 = 40 N · dik: 50 × 0,6 = 30 N'),
  A('Sürtünmeyi bul','N = 30 N; hareket yukarı olduğundan sürtünme aşağı yönlüdür.','f = 0,5 × 30 = 15 N'),
  A('Net kuvvet ve ivme','Yukarı yönlü kuvvet ile aşağı yönlü kuvvetlerin farkı.','75 − 40 − 15 = 5 × a → a = 4 m/s²')],
 'Eğik düzlemde önce bileşenleri ayır; normal kuvvet dik bileşene, sürtünme normal kuvvete bağlıdır.',sekil=tk(sk))

# =============== 09 · vinç, hız–zaman grafiği ve ip gerilmesi (öncüllü) · orta ===============
m9=20; ag=[Fr(4,2),Fr(0),Fr(-4,2)]
Tg=[m9*(10+a) for a in ag]; assert Tg==[240,200,160]
sk=GR('7.6cm','5.0cm',9,5,1,1,'$t$ (s)','$v$ (m/s)','\\addplot[thick,vurgu] coordinates {(0,0) (2,4) (6,4) (8,0)};')
O('0009','fz-dn3-vinc','Vinçle kaldırılan yükte hız–zaman grafiği ve ip gerilmesi','Newton’ın Hareket Yasaları','orta',
 'Hız–zaman grafiğinden her evredeki ivmeyi bulup ip gerilmesini ağırlıkla karşılaştırarak yorumlar.',
 'Düşey yukarı hareket eden yükte T − m·g = m·a; hızlanırken gerilme ağırlıktan büyük, sabit hızda eşit, yavaşlarken küçüktür.',
 'Sabit hızda gerilmenin ağırlıktan büyük olduğunu sanmak; yavaşlarken gerilmenin sıfıra gittiğini düşünmek.',
 'Bir vinç, 20 kg kütleli bir yükü, ideal bir halatla düşey doğrultuda yukarı çekmektedir. Yükün hız–zaman grafiği şekilde verilmiştir (g = 10 m/s²).',
 [('0–2 s aralığında halattaki gerilme 240 N’dur.',True,'Bu aralıkta ivme 4 ÷ 2 = 2 m/s² yukarıdır; T − 200 = 20 × 2 olduğundan T = 240 N.','Hızlanırken gerilmenin ağırlığa (200 N) eşit kalacağını düşünmüş.'),
  ('2–6 s aralığında halattaki gerilme 240 N’dur.',False,'Hız sabit olduğundan ivme sıfırdır; gerilme ağırlığa eşittir: T = 200 N.','Hızlanma evresindeki gerilmeyi (240 N) bütün hareket boyunca sürdürmüş.'),
  ('6–8 s aralığında halattaki gerilme, yükün ağırlığından küçüktür.',True,'Yavaşlarken ivme aşağı yönlüdür (−2 m/s²); T = 20 × (10 − 2) = 160 N, ağırlıktan küçüktür.','Yukarı hareket eden yükte gerilmenin her zaman ağırlıktan büyük olduğunu düşünmüş.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 ('Eğimden ivme: 0–2 s → +2; 2–6 s → 0; 6–8 s → −2 (m/s²).','a = Δv ÷ Δt'),
 ['Grafiğin her bölümünün eğiminden o evredeki ivmeyi bul; ardından yük için Newton’ın ikinci yasasını yaz.'],
 [B('Düşey harekette gerilme','yukarı yönlü ivme a ise T − m·g = m·a; yani T = m·(g + a). İvme aşağı yönlüyse a negatif alınır. Örnek: 3 kg yük 1 m/s² ile yukarı hızlanırsa T = 33 N')],
 'Yük yukarı hızlanırken T > mg, sabit hızda T = mg, yavaşlarken T < mg olur.',sekil=sk,kalip='grafik')

# =============== 10 · fren mesafesi · sayısal · kolay ===============
v10,mu10=20,Fr(1,2); a10=mu10*10; x10=Fr(v10*v10)/(2*a10)
assert (a10,x10)==(5,40) and Fr(v10*v10,2*10)==20 and Fr(v10,a10)==4 and Fr(v10*v10)/a10==80
sk=('\\fill[gray!30] (-.3,-.2) rectangle (7.2,0); \\draw (-.3,0) -- (7.2,0);\n'
    '\\draw[thick,rounded corners=3pt,fill=gray!25] (.5,.25) rectangle (2.3,.95); \\draw[thick,fill=white] (.9,.25) circle (.25); \\draw[thick,fill=white] (1.9,.25) circle (.25);\n'
    f'\\draw[vurgu,very thick,{ARR}] (2.3,.6) -- (3.5,.6); \\node[vurgu,above] at (2.9,.65) {{$20$ m/s}};\n'
    '\\node at (5.2,.5) {$\\mu=0{,}5$ (kuru yol)};')
N('0010','fz-dn3-surtunme','Sürtünme kuvveti','Sürtünme Kuvveti','kolay',
 'Sürtünme kuvvetinden yavaşlamayı bulur ve düzgün yavaşlayan harekette durma mesafesini hesaplar.',
 'Kayarak duran araçta yavaşlatan tek yatay kuvvet kinetik sürtünmedir; ivmenin büyüklüğü μ·g olur ve durma mesafesi v² ÷ 2a ile bulunur.',
 'Yavaşlamayı sürtünmeden hesaplamamak; mesafeyi hızla ya da süreyle karıştırmak.',
 'Şekildeki araç, yatay bir yolda şekilde verilen hızla giderken tekerlekleri kilitlenerek kaymaya başlıyor ve düzgün yavaşlayarak duruyor. Yol ile lastik arasındaki kinetik sürtünme katsayısı şekilde verilmiştir (g = 10 m/s²).\nBuna göre, araç kayma başladıktan sonra kaç m yol alarak durur?',
 40,[(4,'Durma süresini (v ÷ a = 4 s) mesafe olarak yazmış.','dikkat'),(5,'İvmenin büyüklüğünü (5 m/s²) mesafe sanmış.','dikkat'),
     (20,'Sürtünmeyi hesaba katmadan g ile (v² ÷ 2g = 20 m) işlem yapmış.','bilgi'),(80,'Mesafeyi v² ÷ a olarak (½ çarpanını unutarak) bulmuş: 400 ÷ 5 = 80 m.','islem')],
 'Aracın kayarak aldığı yol (m).',
 ['Aracı yavaşlatan kuvvetin ne olduğunu ve bu kuvvetin yaratacağı ivmeyi bul; sonra hız–yol ilişkisini kullan.'],
 [B('Düzgün yavaşlayan hareket','hızı v₀ olan cisim a büyüklüğünde ivmeyle yavaşlayarak durursa aldığı yol x = v₀² ÷ (2a)’dır. Örnek: 10 m/s hızla 2 m/s² ile yavaşlayan cisim 25 m yol alır')],
 [A('Yavaşlamayı bul','Yatay kuvvet yalnız sürtünmedir: m·a = μ·m·g.','a = 0,5 × 10 = 5 m/s²'),
  A('Hız–yol bağıntısını yaz','Durana kadar hız sıfıra iner.','0 = v² − 2·a·x'),
  A('Durma mesafesi','Değerleri yerine koy.','x = 400 ÷ 10 = 40 m')],
 'Kayarak duran araçta a = μ·g; mesafe v² ÷ 2a ile bulunur.',sekil=tk(sk))

bitir(P,'dinamikuc','fiz|Dinamik')
