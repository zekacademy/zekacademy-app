"""TYT Fizik · Sıvıların Kaldırma Kuvveti (üçüncü/dördüncü genişletme) · 10 soru.
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
KONU='Sıvıların Kaldırma Kuvveti'; H.KONU=KONU
P=Parti('kaldirmauc','Sıvıların Kaldırma Kuvveti','fiz|Sıvıların Kaldırma Kuvveti',ders='TYT Fizik',idon='tytfiz')
KAYNAK='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9–10. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'
TAIL='\n\\end{tikzpicture}'
def tk(body): return tikz_svg(HEAD+body+TAIL)
def nn(no): return f'{int(no):02d}'
def kartk(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZKL3-{nn(no)}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)

# ---------- sayısal soru ----------
def N(no,tipId,tip,alt,z,kaz,fikir,tuzak,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,kalip=None,sira=None):
    kalip=kalip or ('şekilli' if sekil else 'düz')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZKL3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı',kisa=None,sira=sira)

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
       kalip=kalip,adim=len(ad),kart=f'K-FZKL3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı')

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
SU='fill=blue!12'
# =============== 01 · yüzen silindir, özkütle · kolay ===============
H1,B1,ds=10,4,1000
r1=ds*Fr(B1,H1); assert r1==400 and ds*Fr(H1-B1,H1)==600 and ds+r1==1400 and ds*Fr(H1,B1)==2500 and ds*B1==4000
sk=('\\fill[blue!12] (0,0) rectangle (3,1.4); \\draw[thick] (0,2.6) -- (0,0) -- (3,0) -- (3,2.6); \\draw[blue!60] (0,1.4) -- (3,1.4);\n'
    '\\draw[thick,fill=gray!30] (1,.4) rectangle (2,2.9);\n'
    '\\draw[<->,thin] (3.45,.4) -- (3.45,2.9); \\node[right,font=\\small] at (3.45,1.65) {$10$ cm}; \\draw[thin,gray] (2,.4) -- (3.45,.4); \\draw[thin,gray] (2,2.9) -- (3.45,2.9);\n'
    '\\draw[<->,thin] (-.45,.4) -- (-.45,1.4); \\node[left,font=\\small] at (-.45,.9) {$4$ cm}; \\draw[thin,gray] (-.45,.4) -- (1,.4); \\draw[thin,gray] (-.45,1.4) -- (0,1.4);\n'
    '\\node[font=\\small] at (.5,.9) {su};')
N('0001','fz-kl3-yuzme','Yüzen cismin batan hacmi ve özkütle','Yüzme ve Batma','kolay',
 'Yüzen düzgün silindirin batan yüksekliğinden özkütlesini bulur.',
 'Yüzen cisimde kaldırma kuvveti ağırlığa eşittir; düzgün cisimde batan hacim oranı, cismin özkütlesinin sıvı özkütlesine oranına eşittir.',
 'Dışarıda kalan oranı batan oran sanmak; oranı ters çevirmek; yükseklik değerini özkütle sanmak.',
 'Düzgün silindir biçimli bir cisim, özkütlesi 1000 kg/m³ olan suda şekildeki gibi dik olarak yüzmektedir.\nBuna göre, cismin özkütlesi kaç kg/m³’tür?',
 400,[(600,'Sudan dışarıda kalan oranı (6/10) batan oran sanmış.','dikkat'),(1400,'Özkütleleri toplamış: 1000 + 400.','bilgi'),(2500,'Oranı ters yazmış: 1000 × 10 ÷ 4.','islem'),(4000,'Batan yüksekliği (4) doğrudan 1000 ile çarpmış.','dikkat')],
 'Cismin özkütlesi (kg/m³).',
 ['Yüzen cisimde ağırlık ile kaldırma kuvveti arasındaki ilişkiyi yaz; düzgün cisimde hacim oranı yükseklik oranına eşittir.'],
 [B('Yüzme koşulu','yüzen cisimde ağırlık kaldırma kuvvetine eşittir: d_cisim · V = d_sıvı · V_batan. Örnek: yarısı batan cismin özkütlesi sıvının yarısıdır')],
 [A('Dengeyi yaz','Ağırlık kaldırma kuvvetine eşit.','d_c × V × g = d_su × V_batan × g'),
  A('Hacim oranını yükseklikten al','Düzgün silindirde V_batan ÷ V = 4 ÷ 10.','d_c = 1000 × 4 ÷ 10'),
  A('Sonucu bul','İşlemi tamamla.','d_c = 400 kg/m³')],
 'Düzgün cisimde batan yükseklik oranı, batan hacim oranına eşittir.',sekil=tk(sk))

# =============== 02 · ölçü silindiri, kaldırma kuvveti · kolay ===============
V0,V1=200,260; Vc=V1-V0; Fk=Fr(Vc,1000)*10
assert (Vc,Fk)==(60,Fr(3,5)) and (Fr(V0,1000),Fr(V1,1000),Fr(V0,1000)*10,Fr(V1,1000)*10)==(Fr(1,5),Fr(13,50),2,Fr(13,5))
def olcu(ox,lv,cis):
    s=f'\\fill[blue!12] ({ox},0) rectangle ({ox+1.2},{lv});\n\\draw[thick] ({ox},3.4) -- ({ox},0) -- ({ox+1.2},0) -- ({ox+1.2},3.4);\n'
    for t in range(0,6): s+=f'\\draw[thin] ({ox},{t*.6:.2f}) -- ({ox+.18},{t*.6:.2f});\n'
    s+=f'\\draw[blue!60] ({ox},{lv}) -- ({ox+1.2},{lv});\n'
    if cis: s+=f'\\draw[thick,fill=gray!45] ({ox+.35},.05) rectangle ({ox+.85},.55);\n'
    return s
sk=(olcu(0,1.2,False)+olcu(3,1.56,True)+
    '\\node[left,font=\\small] at (-.1,1.2) {$200$ mL}; \\node[right,font=\\small] at (4.3,1.56) {$260$ mL};\n'
    '\\node[font=\\small] at (.6,-.4) {(a)}; \\node[font=\\small] at (3.6,-.4) {(b)};')
N('0002','fz-kl3-hacim','Taşan hacimden kaldırma kuvveti','Kaldırma Kuvveti','kolay',
 'Sıvı seviyesindeki artıştan cismin hacmini bulup tam batık cisme etkiyen kaldırma kuvvetini hesaplar.',
 'Tamamen batan cisim, hacmi kadar sıvıyı yer değiştirir; kaldırma kuvveti bu sıvının ağırlığına eşittir.',
 'Su hacmini doğrudan kaldırma kuvveti sanmak; g ile çarpmayı veya birim çevirmeyi unutmak.',
 'Şekil (a)’da ölçü silindirinde su vardır. Şekil (b)’de küçük bir cisim, silindire bırakılıp tamamen batırılmıştır. Suyun özkütlesi 1 g/cm³’tür (1 mL = 1 cm³; g = 10 m/s²).\nBuna göre, cisme etkiyen kaldırma kuvveti kaç N’dur?',
 Fr(3,5),[(Fr(1,5),'İlk su hacminin kütlesini (0,2 kg) g ile çarpmadan almış.','dikkat'),(Fr(13,50),'Son okumanın kütlesini (0,26 kg) g ile çarpmadan almış.','dikkat'),(2,'İlk su hacminin ağırlığını (200 g → 2 N) kaldırma kuvveti sanmış.','bilgi'),(Fr(13,5),'Son okumadaki toplam su hacminin ağırlığını (2,6 N) almış.','bilgi')],
 'Cisme etkiyen kaldırma kuvveti (N).',
 ['Cismin hacmini iki okuma arasındaki farktan bul; bu hacimdeki suyun ağırlığı ne kadardır?'],
 [B('Taşan sıvı','tamamen batan cismin hacmi, sıvı seviyesindeki artışa eşittir ve kaldırma kuvveti bu hacimdeki sıvının ağırlığıdır. Örnek: 100 cm³ hacimli cisim suda 1 N kaldırma kuvveti görür')],
 [A('Hacmi bul','İki okumanın farkı cismin hacmidir.','V = 260 − 200 = 60 cm³'),
  A('Sıvının kütlesi','Hacmi özkütleyle çarp.','m = 1 × 60 = 60 g = 0,06 kg'),
  A('Ağırlığı bul','Kaldırma kuvveti yer değiştiren suyun ağırlığıdır.','F = 0,06 × 10 = 0,6 N')],
 'Seviye farkı hacmi verir; kaldırma kuvveti için hacmi kütleye, kütleyi de ağırlığa çevir.',sekil=tk(sk))

# =============== 03 · dinamometre–derinlik grafiği · öncüllü · orta ===============
W3,Fb,A3,hb=10,6,50,8
Fk3=W3-Fb; V3=A3*hb; assert Fk3==4 and Fr(Fk3,10)*1000==V3==400 and Fr(W3,10)/(Fr(V3,10**6))==2500
assert (Fr(W3,10)/Fr(600,10**6)).limit_denominator(10)==Fr(5000,3) and W3-Fk3*Fr(4,hb)==8 and (W3-Fk3*Fr(4,hb))==8 and Fk3*Fr(4,hb)==2
sk=GR('7.6cm','5.2cm',12,12,2,2,'$h$ (cm)','dinamometre (N)','\\addplot[thick,vurgu] coordinates {(0,10) (8,6) (12,6)};')
O('0003','fz-kl3-grafik','Grafikten kaldırma kuvveti ve yüzme–batma yorumu','Kaldırma Kuvveti','orta',
 'Dinamometre–derinlik grafiğinden kaldırma kuvvetini, hacmi ve özkütleyi yorumlar; tam batıktan sonra okumanın sabit kaldığını bilir.',
 'Batan hacim arttıkça kaldırma kuvveti artar ve dinamometre okuması azalır; cisim tamamen batınca kaldırma kuvveti ve okuma sabit kalır.',
 'Tam battıktan sonra da okumanın azalacağını sanmak; kaldırma kuvvetini dinamometre okumasıyla karıştırmak.',
 'Taban alanı 50 cm² olan düzgün bir cisim, dinamometreye asılı hâlde, alt yüzeyi su yüzeyine değecek biçimde tutuluyor ve düşey doğrultuda yavaşça suya daldırılıyor. Dinamometre okumasının, cismin alt yüzeyinin su yüzeyinden olan derinliğine (h) göre değişimi grafikte verilmiştir. Su kabı yeterince derindir (g = 10 m/s², d_su = 1 g/cm³).',
 [('Cismin özkütlesi 2500 kg/m³’tür.',True,'Tam batınca kaldırma kuvveti 10 − 6 = 4 N, hacim 400 cm³’tür; m = 1 kg olduğundan d = 1 ÷ 0,0004 = 2500 kg/m³.','Okumayı (6 N) kaldırma kuvveti sanıp hacmi 600 cm³ almış; özkütleyi yaklaşık 1667 kg/m³ bulmuş.'),
  ('h = 4 cm iken cisme etkiyen kaldırma kuvveti 4 N’dur.',False,'Okuma 4 cm’de 8 N’dur; kaldırma kuvveti 10 − 8 = 2 N’dur.','Tam batıkken oluşan 4 N’luk kaldırma kuvvetini 4 cm’de de geçerli saymış.'),
  ('h = 10 cm iken dinamometre 6 N’u gösterir.',True,'Cisim h = 8 cm’de tamamen batmıştır; daha derinde kaldırma kuvveti değişmez, okuma 6 N kalır.','Batma derinliği arttıkça okumanın azalmaya devam edeceğini (≈ 5 N) düşünmüş.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 ('Okuma 10 N’dan 6 N’a iniyor; 8 cm’den sonra sabit.','F_k = ağırlık − okuma'),
 ['Dinamometre okumasının değişmeyi bıraktığı yer cisme ne olduğunu gösterir? Kaldırma kuvvetini okumayla ağırlık arasındaki ilişkiden bul.'],
 [B('Dinamometreyle kaldırma kuvveti','okuma = ağırlık − kaldırma kuvveti; tamamen batan cisimde kaldırma kuvveti derinlikle değişmez. Örnek: havada 8 N, suda 5 N okunan cisme 3 N kaldırma kuvveti etkir')],
 'Grafikte kırılma noktası cismin tamamen battığı yerdir; bu noktadan sonra okuma da kaldırma kuvveti de sabittir.',sekil=sk,kalip='grafik')

# =============== 04 · kütle–hacim grafiği, eşit kütleli cisimler · orta ===============
rK,rL=2,Fr(1,2)
m4=Fr(8)  # ortak kütle g
FK=Fr(m4)/rK; FL=m4; oran=FK/FL
assert oran==Fr(1,2) and rK/rL==4 and rL/rK==Fr(1,4)
sk=GR('7.6cm','5.2cm',12,24,2,4,'$V$ (cm$^3$)','$m$ (g)','\\addplot[thick,vurgu] coordinates {(0,0) (12,24)}; \\node[vurgu,below right,font=\\small] at (axis cs:9.3,19.5) {K};','\\addplot[thick,dashed] coordinates {(0,0) (12,6)}; \\node[below,font=\\small] at (axis cs:11,5) {L};')
N('0004','fz-kl3-grafik','Grafikten kaldırma kuvveti ve yüzme–batma yorumu','Yüzme ve Batma','orta',
 'Kütle–hacim grafiğinden özkütleleri bulup suda yüzen ve batan eşit kütleli cisimlerin kaldırma kuvvetlerini karşılaştırır.',
 'Suda batan cismin kaldırma kuvveti hacmine, yüzen cismin kaldırma kuvveti ağırlığına eşittir; eşit kütlede özkütlesi küçük olanın hacmi büyüktür.',
 'Her iki cismin de kaldırma kuvvetini ağırlığa eşitlemek; kaldırma kuvvetini özkütle oranına eşitlemek.',
 'Homojen K ve L cisimlerinin kütle–hacim grafikleri şekildeki gibidir. Eşit kütleli K ve L cisimleri, özkütlesi 1 g/cm³ olan su dolu bir kaba ayrı ayrı bırakılıyor ve dengeye geliyor.\nBuna göre, K’ye etkiyen kaldırma kuvvetinin L’ye etkiyen kaldırma kuvvetine oranı kaçtır?',
 Fr(1,2),[(Fr(1,4),'Özkütle oranının tersini (0,5 ÷ 2) kaldırma oranı sanmış.','dikkat'),(1,'İki cismin de aynı kütleli olduğundan kaldırma kuvvetlerinin eşit olduğunu düşünmüş; K’nin battığını hesaba katmamış.','bilgi'),(2,'Oranı ters yazmış: L ÷ K.','dikkat'),(4,'Özkütle oranını (2 ÷ 0,5) kaldırma kuvvetleri oranı sanmış.','dikkat')],
 'K’ye ve L’ye etkiyen kaldırma kuvvetlerinin oranı.',
 ['Grafikten her cismin hacim başına kütlesini karşılaştır.'],
 [B('Yüzme ve batma','özkütlesi sudan büyük cisim batar ve hacmi kadar su yer değiştirir; küçük cisim yüzer ve kaldırma kuvveti ağırlığına eşit olur. Örnek: 40 g’lık, özkütlesi 0,5 g/cm³ olan cismin kaldırma kuvveti 0,4 N’dur')],
 [A('Özkütleleri bul','Grafiğin eğimi özkütledir.','d_K = 24 ÷ 12 = 2 g/cm³; d_L = 6 ÷ 12 = 0,5 g/cm³'),
  A('Yüzme–batma durumunu belirle','K batar, L yüzer.','K: F = d_su·V_K·g; L: F = m·g'),
  A('Kaldırma kuvvetlerini kıyasla','K’nin hacmi m ÷ 2’dir.','F_K ÷ F_L = (m ÷ 2) ÷ m = 1 ÷ 2')],
 'Önce özkütlelere bak: batan cisimde kaldırma kuvveti hacimden, yüzende ağırlıktan bulunur.',sekil=sk,kalip='grafik')

# =============== 05 · içi boş küre · orta ===============
Vd,md=100,80
su=Vd*1-md
assert su==20 and md==80 and Fr(md,10)==8 and su+Vd==120
sk=('\\fill[blue!12] (-2,-1.7) rectangle (4.2,.47); \\draw[thick] (-2,1.5) -- (-2,-1.7) -- (4.2,-1.7) -- (4.2,1.5); \\draw[blue!60] (-2,.47) -- (4.2,.47);\n'
    '\\draw[thick,fill=gray!50] (0,0) circle (1.1); \\draw[thick,fill=white] (0,0) circle (1.04); \\node[font=\\small] at (0,0) {boş};\n'
    '\\node[right,font=\\small,align=left] at (1.3,1.0) {dış hacim $100$ cm$^3$\\\\kütle $80$ g};')
N('0005','fz-kl3-yuzme','Yüzen cismin batan hacmi ve özkütle','Yüzme ve Batma','orta',
 'İçi boş kürenin yüzme koşulundan, askıda kalması için boşluğa doldurulacak su kütlesini hesaplar.',
 'Cisim ancak toplam kütlesi, kendi hacmi kadar suyun kütlesine eşit olduğunda suyun içinde askıda kalır.',
 'Boşluk hacmini doldurulacak su kütlesi sanmak; küre kütlesini hacimle karıştırmak.',
 'Metalden yapılmış, içi boş ve kapalı bir kürenin dış hacmi ve toplam kütlesi şekilde verilmiştir. Küre suyun (1 g/cm³) yüzeyinde yüzmektedir. Kürenin içindeki boşluğa bir delikten su doldurulup delik kapatılıyor ve küre, tamamen suyun içinde askıda kalıyor.\nBuna göre, boşluğa kaç g su doldurulmuştur?',
 20,[(8,'Kütleyi g = 10’a bölerek 80 ÷ 10 işlemini doldurulan su sanmış.','dikkat'),(80,'Kürenin kendi kütlesini (80 g) doldurulan su sanmış.','dikkat'),(100,'Askıda kalma için gereken toplam kütleyi (100 g) doldurulan su saymış.','bilgi'),(120,'Eksik kütle (20 g) ile toplam kütleyi (100 g) toplamış.','islem')],
 'Boşluğa doldurulan suyun kütlesi (g).',
 ['Küre askıdayken toplam kütlesi ile yer değiştirdiği suyun kütlesi arasındaki ilişkiyi yaz.'],
 [B('Askıda kalma','cisim sıvının içinde askıdaysa toplam kütlesi, hacmi kadar sıvının kütlesine eşittir. Örnek: hacmi 50 cm³ olan cisim suda askıdaysa kütlesi 50 g’dır')],
 [A('Askıda kalma koşulu','Toplam kütle = dış hacim × özkütle (su).','m_toplam = 100 × 1 = 100 g'),
  A('Küre ve su kütlesi','Toplam kütle küre ile suyun toplamıdır.','80 + m_su = 100'),
  A('Su kütlesini bul','Denklemi çöz.','m_su = 20 g')],
 'Askıda kalan cismin ortalama özkütlesi sıvınınkine eşittir; eksik kütleyi suyla tamamla.',sekil=tk(sk))

# =============== 06 · tablo, alkolde yüzme–batma · öncüllü · orta ===============
dalk=Fr(4,5); T6={'K':(60,100),'L':(80,100),'M':(100,100)}
FkK=Fr(T6['K'][0],1000)*10; FkL=dalk*T6['L'][1]*Fr(10,1000); FkM=dalk*T6['M'][1]*Fr(10,1000)
assert (FkK,FkL,FkM)==(Fr(3,5),Fr(4,5),Fr(4,5)) and Fr(T6['M'][0],1000)*10-FkM==Fr(1,5) and FkK!=FkL
sk=tablo_svg(['Cisim','Kütle (g)','Hacim (cm³)'],[[k,str(a),str(b)] for k,(a,b) in T6.items()])
O('0006','fz-kl3-yuzbat','Alkolde yüzme–batma ve kaldırma kuvvetlerinin karşılaştırılması','Yüzme ve Batma','orta',
 'Tablodaki kütle ve hacimlerden cisimlerin özkütlesini bulup alkolde yüzme–batma durumunu ve kaldırma kuvvetlerini karşılaştırır.',
 'Özkütlesi sıvıdan küçük cisim yüzer, eşit olan askıda kalır, büyük olan batar; yüzen ve askıdaki cismin kaldırma kuvveti ağırlığına, batan cismin kaldırma kuvveti hacmine bağlıdır.',
 'Askıda kalan ve yüzen cisimlerin kaldırma kuvvetini aynı sanmak; batan cisme etkiyen kaldırma kuvvetini ağırlığına eşitlemek.',
 'Özkütlesi 0,8 g/cm³ olan alkol dolu bir kaba, kütle ve hacimleri tabloda verilen K, L ve M cisimleri ayrı ayrı bırakılıyor; K yüzüyor, L sıvının içinde askıda kalıyor, M ise kabın tabanına batıyor (g = 10 m/s²).',
 [ ('L ile M’ye etkiyen kaldırma kuvvetleri eşittir.',True,'Hacimleri eşit ve ikisi de sıvının içindedir: F = 0,8 × 100 × 10⁻³ = 0,8 N.','Kaldırma kuvvetini ağırlıkla karıştırıp M’ninkini 1 N sanmış.'),
  ('M cismi kabın tabanına 0,2 N’luk kuvvetle bastırır.',True,'M’nin ağırlığı 1 N, kaldırma kuvveti 0,8 N’dur; taban tepkisi 1 − 0,8 = 0,2 N’dur.','Batan cismin tabana ağırlığı kadar (1 N) bastırdığını düşünmüş.'),
  ('K ile L’ye etkiyen kaldırma kuvvetleri eşittir.',False,'K yüzer: F = ağırlığı = 0,6 N; L askıdadır: F = ağırlığı = 0,8 N. Kaldırma kuvvetleri eşit değildir.','Yüzen ve askıda kalan cisimlerin ikisinde de kaldırma kuvveti ağırlığa eşit olduğundan, ağırlıkları farklı olsa da değerlerin aynı olacağını düşünmüş.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],
 ('Özkütleler: K 0,6; L 0,8; M 1,0 g/cm³; alkol 0,8 g/cm³.','d = m ÷ V'),
 ['Önce her cismin özkütlesini bul; yüzme, askıda kalma ve batma durumlarında kaldırma kuvvetinin nasıl bulunduğunu düşün.'],
 [B('Kaldırma kuvveti','yüzen ve askıda kalan cisimde kaldırma kuvveti ağırlığa eşittir; batan cisimde ise F = d_sıvı · V · g’dir. Örnek: 50 cm³’lük cisim suda tamamen batıksa 0,5 N’luk kaldırma kuvveti görür')],
 'Özkütleyi sıvıyla karşılaştır; batan cisimde kaldırma kuvvetini hacimden, yüzende ağırlıktan hesapla.',sekil=sk,kalip='tablo')

# =============== 07 · ahşap + metal, iki düzenek · zor ===============
mw,Vw,mm,Vm7=500,1000,300,100
a_bat=Fr(mw+mm,1); b_bat=(mw+mm)-Vm7
assert (a_bat,b_bat)==(800,700) and Fr(b_bat,Vw)*100==70 and Fr(a_bat,Vw)*100==80 and Fr(Vw-a_bat,Vw)*100==20 and Fr(Vw-b_bat,Vw)*100==30 and Fr(mw,Vw)*100==50
def kapp(ox,lv):
    return f'\\fill[blue!12] ({ox},0) rectangle ({ox+3},{lv}); \\draw[thick] ({ox},2.9) -- ({ox},0) -- ({ox+3},0) -- ({ox+3},2.9); \\draw[blue!60] ({ox},{lv}) -- ({ox+3},{lv});\n'
sk=(kapp(0,1.89)+'\\draw[thick,fill=brown!25] (.75,.85) rectangle (2.25,2.15);\\node at (1.5,1.5) {ahşap}; \\draw[thick,fill=gray!60] (1.05,2.15) rectangle (1.95,2.55); \\node[font=\\scriptsize] at (1.5,2.35) {metal};\n'
    +kapp(4.5,1.96)+'\\draw[thick,fill=brown!25] (5.25,1.05) rectangle (6.75,2.35); \\node at (6,1.7) {ahşap}; \\draw[thick] (6,1.05) -- (6,.65); \\draw[thick,fill=gray!60] (5.7,.25) rectangle (6.3,.65); \\node[font=\\scriptsize] at (6,.45) {metal};\n'
    '\\node[font=\\small] at (1.5,-.4) {I}; \\node[font=\\small] at (6,-.4) {II};')
N('0007','fz-kl3-yuzme','Yüzen cismin batan hacmi ve özkütle','Yüzme ve Batma','orta',
 'Metal yükün ahşap blokla üstte taşınması ve altından asılması durumlarında batan hacmi iki ayrı denge koşuluyla bulur.',
 'Yüzen bütün sistemde toplam ağırlık, toplam kaldırma kuvvetine eşittir; metal suyun içindeyse kendi hacmi kadar da kaldırma kuvveti sağlar.',
 'İkinci durumda metalin kaldırma kuvvetini unutmak; iki durumdaki batan oranları karıştırmak.',
 'Hacmi 1000 cm³, kütlesi 500 g olan ahşap bir blokla, hacmi 100 cm³, kütlesi 300 g olan bir metal parça, suda (1 g/cm³) şekildeki iki düzenekte dengededir: I’de metal bloğun üstündedir, II’de metal ince bir iple bloğun altına asılıdır ve tamamen suyun içindedir. İpin kütlesi ve hacmi ihmal edilmektedir.\nBuna göre, II numaralı düzenekte ahşap bloğun hacminin yüzde kaçı su içindedir?',
 70,[(20,'I düzeneğinde dışarıda kalan oranı (200 cm³) II’de dışarıda kalan sanmış.','dikkat'),(30,'II düzeneğinde dışarıda kalan oranı batan oran sanmış.','dikkat'),(50,'Metalin ağırlığını hesaba katmayıp yalnız ahşabın yüzme koşulunu yazmış.','dikkat'),(80,'I düzeneğindeki batan oranı (800 cm³) II için de almış.','bilgi')],
 'II düzeneğinde ahşabın su içindeki kısmının yüzdesi.',
 ['II düzeneğinde sisteme etkiyen toplam kaldırma kuvvetinin hangi parçalardan geldiğini yaz.'],
 [B('Bağlı cisimler','birlikte yüzen cisim sisteminde toplam ağırlık = toplam kaldırma kuvvetidir; sıvıya batan her parça kendi hacmi kadar kaldırma kuvveti verir. Örnek: 30 g’lık sistem 30 cm³ suyu yer değiştirir')],
 [A('Toplam ağırlığı yaz','Ahşap ve metalin kütleleri toplanır.','m_toplam = 500 + 300 = 800 g'),
  A('Kaldırma kuvvetini yaz','Metal tamamen batık, ahşap V_x kadar batık.','(V_x + 100) × 1 = 800'),
  A('Oranı bul','V_x = 700 cm³ ve blok 1000 cm³’tür.','700 ÷ 1000 = %70')],
 'Metal suyun içindeyse kendi kaldırma kuvvetini sağlar; ağırlık toplamından bu hacmi çıkar.',sekil=tk(sk))

# =============== 08 · bardaktan alınan taş · öncüllü · zor ===============
def kap8(ox,lv,tas_bardak,dep=.35):
    s=f'\\fill[blue!12] ({ox},0) rectangle ({ox+3.2},{lv}); \\draw[thick] ({ox},2.8) -- ({ox},0) -- ({ox+3.2},0) -- ({ox+3.2},2.8); \\draw[blue!60] ({ox},{lv}) -- ({ox+3.2},{lv});\n'
    top=lv+.8-dep; bot=lv-dep
    s+=f'\\draw[thick,fill=white] ({ox+.8},{top}) -- ({ox+.95},{bot}) -- ({ox+2.25},{bot}) -- ({ox+2.4},{top});\n'
    if tas_bardak: s+=f'\\draw[thick,fill=gray!55] ({ox+1.6},{bot+.2}) circle (.2);\n'
    else: s+=f'\\draw[thick,fill=gray!55] ({ox+2.7},.2) circle (.2);\n'
    return s
sk=kap8(0,1.7,True)+kap8(4.4,1.55,False,.15)+'\\node[font=\\small] at (1.6,-.4) {I}; \\node[font=\\small] at (6,-.4) {II};'
O('0008','fz-kl3-kap','Kapta kaldırma kuvveti, seviye ve basınç değişimi','Yüzme ve Batma','zor',
 'Yüzen kaptaki taşın suya bırakılmasıyla kaldırma kuvveti, su seviyesi ve sıvı basıncındaki değişimi yorumlar.',
 'Yüzen cisim ağırlığı kadar, batan cisim ise kendi hacmi kadar sıvı yer değiştirir; seviye ve basınç yer değiştiren toplam hacme bağlıdır.',
 'Taşın bardağın içinde veya suda olmasının su seviyesini etkilemediğini sanmak; bardağa etkiyen kaldırma kuvvetinin sabit kaldığını düşünmek.',
 'Su dolu geniş bir kapta, içinde taş bulunan küçük bir bardak şekil I’deki gibi yüzmektedir. Taş bardaktan alınıp doğrudan kabın suyuna bırakılıyor; taş dibe batıyor ve bardak yüzmeye devam ediyor (şekil II). Su kaptan taşmamaktadır.',
 [('Kaptaki su seviyesi alçalır.',True,'Taş bardaktayken ağırlığına eşit su kütlesini, yani kendi hacminden daha büyük bir hacmi yer değiştiriyordu; dipte yalnız kendi hacmi kadar yer değiştirir. Seviye alçalır.','Taşın bardakta ya da suda olmasının hacim yer değiştirmesi bakımından farkı olmadığını düşünüp seviyenin sabit kaldığını sanmış.'),
  ('Kabın tabanındaki sıvı basıncı değişmez.',False,'Seviye alçaldığı için taban basıncı (d·g·h) azalır.','Toplam su miktarının aynı kaldığını görüp basıncın da aynı kalacağını düşünmüş.'),
  ('Bardağa etkiyen kaldırma kuvveti değişmez.',False,'Bardak taşsız kalınca ağırlığı azalır; yüzen cismin kaldırma kuvveti ağırlığına eşit olduğundan azalır.','Yüzen bardağın kaldırma kuvvetinin daima aynı kalacağını düşünmüş.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],
 ('I’de taş bardaktadır; II’de taş dipte, bardak yine yüzmektedir.','Yüzen cisimde F_k = ağırlık'),
 ['Taşın bardakta ve dipte yer değiştirdiği su hacimlerini karşılaştır; bardağın kaldırma kuvveti neye eşit?'],
 [B('Yer değiştirme','yüzen cisim ağırlığı kadar, batan cisim ise kendi hacmi kadar sıvı yer değiştirir. Örnek: 30 g’lık taş yüzen bir kapta suyun 30 cm³’ünü, dipte ise taşın kendi hacmini yer değiştirir')],
 'Yüzenin yer değiştirdiği hacim ağırlığa, batanın yer değiştirdiği hacim kendi hacmine bağlıdır.',sekil=tk(sk))

# =============== 09 · tabana yayla bağlı cisim, sıvı değişimi · zor ===============
V9,d9,k9,dY=500,Fr(3,5),100,Fr(6,5)
mg9=d9*V9*Fr(10,1000); Fs=Fr(V9,1000)*10; Fy=dY*V9*Fr(10,1000)
x1=(Fs-mg9)/k9*100; x2=(Fy-mg9)/k9*100
assert (mg9,Fs,Fy,x1,x2)==(3,5,6,2,3)
assert (Fr(6,5)*x1,((Fy-2)/k9)*100,Fy/k9*100,x1)==(Fr(12,5),4,6,2)
sk=('\\fill[blue!12] (0,0) rectangle (4,3.2); \\draw[thick] (0,3.6) -- (0,0) -- (4,0) -- (4,3.6); \\draw[blue!60] (0,3.2) -- (4,3.2);\n'
    '\\draw[thick] (1.6,0) -- (1.6,.25) -- (1.8,.35) -- (1.4,.55) -- (1.8,.75) -- (1.4,.95) -- (1.6,1.0) -- (1.6,1.4);\n'
    '\\draw[thick,fill=gray!30] (1.1,1.4) rectangle (2.1,2.4);\n'
    '\\draw[thin,dashed] (1.0,1.0) -- (2.7,1.0); \\draw[thin,dashed] (2.1,1.4) -- (2.7,1.4);\n'
    '\\draw[<->,thick] (2.55,1.0) -- (2.55,1.4); \\node[right,font=\\small,align=left] at (2.65,1.2) {uzama\\\\$2$ cm}; \\node[font=\\small] at (2,3.7) {su};')
N('0009','fz-kl3-yay','Yayla tabana bağlı cismin kaldırma kuvveti ve yay uzaması','Kaldırma Kuvveti','zor',
 'Yayla tabana bağlı tam batık cisimde sıvı değişince kaldırma kuvvetindeki artışı ve yay uzamasını Hooke ve denge yasasıyla hesaplar.',
 'Dengede yay kuvveti, kaldırma kuvveti ile ağırlığın farkına eşittir; sıvı özkütlesi artınca yalnız kaldırma kuvveti değişir, yay uzaması bu farkla orantılıdır.',
 'Yay uzamasını yalnız kaldırma kuvvetiyle orantılı sanmak; ağırlığı hesaba katmamak; sıvı değişimini yok saymak.',
 'Hacmi 500 cm³, özkütlesi 0,6 g/cm³ olan bir cisim, kabın tabanına bağlı hafif bir yayla suyun (1 g/cm³) içinde tamamen batık ve dengede tutulmaktadır; yayın uzaması şekilde verilmiştir. Daha sonra su boşaltılıp kap özkütlesi 1,2 g/cm³ olan bir sıvıyla dolduruluyor ve cisim yine tamamen batık hâlde yayla dengede kalıyor (g = 10 m/s²).\nBuna göre, yeni durumda yayın uzaması kaç cm olur?',
 3,[(2,'Sıvı değişse de yay uzamasının aynı kalacağını düşünmüş.','dikkat'),(Fr(12,5),'Yay uzamasını kaldırma kuvvetiyle orantılı alıp 2 × 1,2 = 2,4 cm bulmuş.','islem'),(4,'Ağırlığı 2 N alarak (6 − 2) ÷ 100 = 4 cm bulmuş.','dikkat'),(6,'Kaldırma kuvvetini (6 N) doğrudan yay kuvveti sanmış.','dikkat')],
 'Yeni durumdaki yay uzaması (cm).',
 ['Dengede yay kuvvetini kaldırma kuvveti ve ağırlıkla ilişkilendir; önce suyun içindeki durumdan yay sabitini bul.'],
 [B('Yay ve kaldırma kuvveti','tabana bağlı, tamamen batık cisimde dengede F_yay = F_k − G olur ve F_yay = k·x’tir. Örnek: kaldırma kuvveti 5 N, ağırlık 4 N ise yay 1 N’luk kuvvet uygular')],
 [A('Su içindeki durum','F_k = 1 × 500 × 10⁻³ × 10, G = 0,6 × 500 × 10⁻³ × 10.','F_k = 5 N; G = 3 N; yay kuvveti 2 N'),
  A('Yay sabitini bul','2 cm = 0,02 m uzamada 2 N var.','k = 2 ÷ 0,02 = 100 N/m'),
  A('Yeni sıvıda','F_k = 1,2 × 500 × 10⁻³ × 10 = 6 N; yay kuvveti = 6 − 3.','x = 3 ÷ 100 = 0,03 m = 3 cm')],
 'Yay kuvveti kaldırma kuvvetiyle ağırlığın farkıdır; farkları oranlayarak yay sabitini bilmeden de çözebilirsin.',sekil=tk(sk))

# =============== 10 · yer çekimi farklı gezegende yüzen blok · öncüllü · zor ===============
def kap10(ox,et):
    return (f'\\fill[blue!12] ({ox},0) rectangle ({ox+3},1.8); \\draw[thick] ({ox},2.8) -- ({ox},0) -- ({ox+3},0) -- ({ox+3},2.8); \\draw[blue!60] ({ox},1.8) -- ({ox+3},1.8);\n'
            f'\\draw[thick,fill=brown!25] ({ox+.9},1.1) rectangle ({ox+2.1},2.3);\n\\node[font=\\small] at ({ox+1.5},-.4) {{{et}}};\n')
sk=kap10(0,'Dünya ($g$)')+kap10(4.4,'Gezegen ($g/2$)')
O('0010','fz-kl3-kap','Kapta kaldırma kuvveti, seviye ve basınç değişimi','Kaldırma Kuvveti','zor',
 'Yer çekimi ivmesinin yarıya indiği ortamda yüzen cismin batan hacmini, kaldırma kuvvetini ve taban basıncını yorumlar.',
 'Bir büyüklüğün formülünde g varsa, g değişince o büyüklük de değişir; g sadeleşen oranlar ise aynı kalır.',
 'Kaldırma kuvvetinin yer çekiminden bağımsız olduğunu sanmak; batan hacmin g ile değiştiğini düşünmek; basınçta g’yi unutmak.',
 'Su dolu bir kapta şekildeki gibi yüzen homojen bir ahşap blok, kapla birlikte, yüzeyindeki yer çekimi ivmesi Dünya’dakinin yarısı olan bir gezegene götürülüyor. Kaptaki su miktarı ve sıcaklığı değişmiyor; blok yine yüzüyor.',
 [('Bloğun suya batan hacmi artar.',False,'Yüzme koşulu d_blok·V·g = d_su·V_batan·g’dir; g sadeleştiği için batan hacim değişmez.','Yer çekimi azalınca suyun bloğu daha az ittiğini düşünüp bloğun daha çok batacağını sanmış.'),
  ('Bloğa etkiyen kaldırma kuvveti azalır.',True,'Yüzen blokta kaldırma kuvveti ağırlığa eşittir; ağırlık m·g olduğundan g yarıya inince kaldırma kuvveti de yarıya iner.','Kaldırma kuvvetinin yer çekiminden bağımsız olduğunu düşünmüş.'),
  ('Kabın tabanındaki sıvı basıncı azalır.',True,'Sıvı derinliği aynı kalsa da P = d·g·h ifadesinde g yarıya iner; basınç azalır.','Su derinliği aynı kaldığı için basıncın da aynı kalacağını sanmış.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],
 ('Dünya: g; gezegen: g/2. Su miktarı ve yüzme durumu aynı.','d_blok·V·g = d_su·V_batan·g'),
 ['Yüzme koşulunu yaz; g hangi formüllerde geçiyor?'],
 [B('Ortamın etkisi','kaldırma kuvveti d_sıvı·V_batan·g, sıvı basıncı d·g·h’tır; yer çekimi ivmesi değişince ikisi de aynı oranda değişir, ama yüzen cismin batan hacmi değişmez. Örnek: g yarıya inerse 20 N’luk kaldırma kuvveti 10 N olur')],
 'Yüzme koşulunda g sadeleşir; g içeren büyüklükler g ile birlikte değişir.',sekil=tk(sk))

bitir(P,'kaldirmauc','fiz|Sıvıların Kaldırma Kuvveti')
