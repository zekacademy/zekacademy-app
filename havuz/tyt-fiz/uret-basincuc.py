"""TYT Fizik · Basınç (üçüncü/dördüncü genişletme) · 10 soru.
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
KONU='Basınç'; H.KONU=KONU
P=Parti('basincuc','Basınç','fiz|Basınç',ders='TYT Fizik',idon='tytfiz')
KAYNAK='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9–10. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,circuitikz/bipoles/length=1.1cm]\n'
TAIL='\n\\end{tikzpicture}'
def tk(body): return tikz_svg(HEAD+body+TAIL)
def nn(no): return f'{int(no):02d}'
def kartk(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZBS3-{nn(no)}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)

# ---------- sayısal soru ----------
def N(no,tipId,tip,alt,z,kaz,fikir,tuzak,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil=None,kalip=None,sira=None):
    kalip=kalip or ('şekilli' if sekil else 'düz')
    kartk(no,alt,fikir,tuzak,z,kalip,len(ad),tipId,tip)
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,ip=ip,bilgi=bilgi,puf=puf,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,
       kalip=kalip,adim=len(ad),kart=f'K-FZBS3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı',kisa=None,sira=sira)

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
       kalip=kalip,adim=len(ad),kart=f'K-FZBS3-{nn(no)} ({alt}) · yeni kurgu, ÖSYM mantığı')

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
# =============== 01 · çivi: aynı kuvvet, farklı alan · sayısal · kolay ===============
Ab,Au=Fr(2),Fr(1,20)
oran=Ab/Au; assert oran==40 and Fr(1)!=oran
assert Au/Ab==Fr(1,40) and Fr(2,Fr(1,2))==4 and oran*10==400
sk=('\\draw[thick,fill=gray!25] (1.4,-.45) rectangle (1.8,.45); \\draw[thick] (1.8,0) -- (4.1,0);\n'
    '\\draw[thick,fill=gray!25] (4.1,-.06) -- (4.5,0) -- (4.1,.06) -- cycle;\n'
    '\\draw[very thick] (4.5,-1.1) -- (4.5,1.1); \\foreach \\y in {-1.0,-.7,...,1.0} \\draw[thin] (4.5,\\y) -- (4.8,\\y+.3);\n'
    '\\draw[vurgu,very thick,-{Stealth[length=2mm,width=1.8mm]}] (-.3,0) -- (1.35,0); \\node[vurgu,above] at (.55,.05) {$F$};\n'
    '\\node[above] at (1.6,.55) {baş: $2$ cm$^2$}; \\node[below] at (3.0,-.55) {uç: $0{,}05$ cm$^2$}; \\draw[thin] (3.5,-.6) -- (4.35,-.05);\n'
    '\\node at (5.4,1.3) {tahta};')
N('0001','fz-bs3-kati','Katı basıncı','Katı Basıncı','kolay',
 'Aynı büyüklükte kuvvetin iki farklı yüzeye uyguladığı basıncı alanlarla ters orantılı olarak karşılaştırır.',
 'Çivi dengede olduğundan baştaki ve uçtaki kuvvet aynıdır; basınç P = F ÷ A olduğundan basınçlar temas alanlarıyla ters orantılıdır.',
 'Kuvvet aynı olduğu için basıncın da aynı olduğunu sanmak; alan oranını ters kurmak.',
 'Şekildeki çivi, başına parmakla uygulanan F kuvvetiyle tahtaya bastırılmaktadır. Çivi dengededir ve ağırlığı önemsenmeyecek kadar küçüktür. Çivinin baş ve uç yüzeylerinin alanları şekilde verilmiştir.\nBuna göre, çivinin ucunun tahtaya uyguladığı basınç, başının parmağa uyguladığı basıncın kaç katıdır?',
 40,[(1,'Çivinin iki ucundaki kuvvet aynı olduğu için basınçların da aynı olduğunu düşünmüş.','bilgi'),
     (Fr(1,40),'Alan oranını ters kurmuş: P_uç ÷ P_baş yerine 0,05 ÷ 2 almış.','islem'),
     (4,'Uç alanını 0,5 cm² okumuş: 2 ÷ 0,5 = 4.','dikkat'),(400,'Alanları oranlarken ondalık kaydırma hatası yapmış: 2 ÷ 0,005 = 400.','islem')],
 'Uç basıncının baş basıncına oranı.',
 ['Çivinin iki ucunda hangi nicelik ortaktır, hangisi farklıdır? Basıncı bu niceliklerle yaz.'],
 [B('Katı basıncı','birim yüzeye dik etkiyen kuvvettir: P = F ÷ A. Örnek: 12 N’luk kuvvet 3 cm²’ye etkirse basınç 4 N/cm² olur')],
 [A('Kuvvetleri karşılaştır','Çivi dengede olduğundan baştaki ve uçtaki kuvvet aynıdır.','F_baş = F_uç = F'),
  A('Basınçları yaz','Basınç kuvvetin alana oranıdır.','P_baş = F ÷ 2 · P_uç = F ÷ 0,05'),
  A('Oranla','İki ifadeyi birbirine böl.','P_uç ÷ P_baş = 2 ÷ 0,05 = 40')],
 'Aynı kuvvet küçük alana etkirse basınç alan oranı kadar büyür.',sekil=tk(sk))

# =============== 02 · tablo: ağırlık ve alan · öncüllü · kolay ===============
T2={'K':(60,20),'L':(60,40),'M':(90,30),'N':(100,20)}
PB={k:Fr(a,b) for k,(a,b) in T2.items()}; assert PB=={'K':3,'L':Fr(3,2),'M':3,'N':5}
assert PB['K']==PB['M'] and PB['L']!=max(PB.values()) and PB['N']==max(PB.values())
sk=tablo_svg(['Cisim','Ağırlık (N)','Temas alanı (cm²)'],[[k,str(a),str(b)] for k,(a,b) in T2.items()])
O('0002','fz-bs3-kati','Katı basıncı','Katı Basıncı','kolay',
 'Tabloda verilen ağırlık ve temas alanından cisimlerin yatay zemine uyguladığı basınçları hesaplayıp karşılaştırır.',
 'Yatay zemindeki cismin basıncı ağırlığının temas alanına oranıdır; her cisim için ayrı hesaplanır ve karşılaştırılır.',
 'Ağırlığı en büyük cismin basıncının da en büyük olduğunu sanmak; yalnız alana bakmak.',
 'K, L, M ve N cisimleri yatay bir zemine tamamen yaslanarak durmaktadır. Cisimlerin ağırlıkları ve zeminle temas alanları tabloda verilmiştir.',
 [('K ve M cisimlerinin zemine uyguladığı basınçlar eşittir.',True,'P = G ÷ A: K için 60 ÷ 20 = 3 N/cm², M için 90 ÷ 30 = 3 N/cm²; basınçlar eşittir.','Ağırlığı farklı olan cisimlerin basıncının da farklı olacağını düşünmüş.'),
  ('L cisminin zemine uyguladığı basınç en büyüktür.',False,'L için 60 ÷ 40 = 1,5 N/cm²; bu değer dört cismin en küçüğüdür.','Alanı en büyük cismin (L, 40 cm²) basıncının da en büyük olduğunu sanmış.'),
  ('N cisminin zemine uyguladığı basınç en büyüktür.',True,'N için 100 ÷ 20 = 5 N/cm²; diğerlerinden büyüktür.','N’nin basıncını, alanı aynı olan K’ninkiyle (3 N/cm²) aynı sanmış; ağırlık farkını hesaba katmamış.')],
 ['Yalnız I','Yalnız III','I ve III','II ve III','I, II ve III'],
 ('Her cisim için P = G ÷ A hesapla.','K: 3 · L: 1,5 · M: 3 · N: 5 (N/cm²)'),
 ['Her cismin basıncını ayrı ayrı hesapla; yalnız ağırlığa ya da yalnız alana bakma.'],
 [B('Katı basıncı','yatay zemindeki cismin basıncı ağırlığının temas alanına oranıdır: P = G ÷ A. Örnek: 50 N ağırlık 10 cm²’ye yaslanırsa basınç 5 N/cm² olur')],
 'Basınç hem kuvvete hem alana bağlıdır; karşılaştırırken her cismin G ÷ A değerini ayrı hesapla.',sekil=sk,kalip='tablo')

# =============== 03 · ağzına kadar dolu kapta batan cisim · öncüllü · orta ===============
m3,V3=2700,1000; dz=Fr(27,10)                                  # cisim: 2,7 kg, 1000 cm³ → özkütle 2,7 g/cm³
assert Fr(m3,V3)==dz and dz>1
tasan=V3*1                                                     # g su
assert tasan<m3                                                # taşan su ağırlığı < cisim ağırlığı → III yanlış
assert m3-tasan>0                                              # kap+su ağırlığı artar → II doğru; su seviyesi aynı → I doğru
sk=('\\draw[thick] (0,2.6) -- (0,0) -- (2.6,0) -- (2.6,2.6); \\fill[vurgu!15] (.03,.03) rectangle (2.57,2.5);\n'
    '\\draw[thick,fill=gray!40] (.8,.03) rectangle (1.7,.73);\n'
    '\\draw[thick] (2.6,2.5) -- (3.0,2.5) -- (3.0,2.35); \\draw[thick] (3.0,.15) -- (3.0,.15);\n'
    '\\draw[thick] (3.3,1.3) -- (3.4,.8) -- (4.4,.8) -- (4.5,1.3); \\fill[vurgu!15] (3.42,.82) rectangle (4.38,1.05);\n'
    '\\draw[->,thin] (3.0,2.3) -- (3.7,1.2);\n'
    '\\node at (1.25,.38) {cisim}; \\node[font=\\small] at (4.2,1.75) {taşan su};\n'
    '\\draw[thick] (-.4,0) -- (3.2,0);')
O('0003','fz-bs3-sivi-kap','Kaplarda sıvı basıncı','Sıvı Basıncı','orta',
 'Ağzına kadar sıvı dolu kaba batan bir cisim bırakıldığında taban basıncının, zemine yapılan basıncın ve taşan sıvının değişimini yorumlar.',
 'Sıvı yüksekliği değişmediğinden taban basıncı aynı kalır; batan cismin ağırlığı taşan sıvının ağırlığından büyük olduğundan kabın toplam ağırlığı ve zemine uyguladığı basınç artar.',
 'Cismin eklenmesiyle sıvı basıncının arttığını sanmak; taşan sıvının ağırlığını cismin ağırlığına eşit saymak.',
 'Yatay zeminde duran, kesiti her yerde aynı olan bir kap, şekildeki taşma ağzına kadar su ile doludur. Kaba, özkütlesi suyun özkütlesinin 2,7 katı olan ve tamamen suya batan bir cisim hafifçe bırakılıyor; cisim kabın tabanına oturuyor ve taşan su yandaki kapta toplanıyor. Kabın zemine temas alanı değişmemektedir.',
 [('Kabın tabanındaki sıvı basıncı, cisim bırakılmadan önceki değerine eşit kalır.',True,'Taşan suyla birlikte sıvı yüksekliği taşma ağzı seviyesinde aynı kalır; P = d·g·h değişmez.','Cisim eklenince su seviyesinin ve tabandaki basıncın arttığını düşünmüş.'),
  ('Kabın yatay zemine uyguladığı basınç artar.',True,'Cisim batarken ağırlığı, taşan suyun ağırlığından büyüktür; kap + su + cismin toplam ağırlığı artar, alan aynı olduğundan basınç artar.','Taşan su kadar ağırlığın çıkmasıyla toplam ağırlığın değişmediğini sanmış.'),
  ('Taşan suyun ağırlığı, cismin ağırlığına eşittir.',False,'Taşan suyun ağırlığı cismin hacmi kadar suyun ağırlığıdır; cismin özkütlesi suyunkinden büyük olduğundan cismin ağırlığından küçüktür.','Cismin ağırlığı kadar suyun taştığını düşünmüş.')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 ('Kap ağzına kadar dolu; cisim batıyor; taşan su hacmi = cismin hacmi.','V_taşan = V_cisim'),
 ['Su seviyesi cisim konulunca değişiyor mu? Taşan suyun hacmi ile cismin hacmi arasındaki ilişkiyi düşün.'],
 [B('Sıvı basıncı','sıvı basıncı P = d·g·h ile bulunur; yalnız sıvının özkütlesine ve derinliğe bağlıdır'),
  B('Taşırma','tamamen batan cisim kendi hacmi kadar sıvıyı yerinden taşırır')],
 'Taban basıncı ile zemine yapılan basıncın bağlı olduğu nicelikler farklıdır; her birini ayrı değerlendir.',sekil=tk(sk))

# =============== 04 · pistonlu kapta tabandaki basınç · sayısal · zor ===============
m4,A4,h4=20,Fr(1,100),Fr(1,2); dsu=1000; g=10
Ppis=Fr(m4*g)/A4; Psiv=dsu*g*h4; Pt=Ppis+Psiv
assert (Ppis,Psiv,Pt)==(20000,5000,25000)
assert Pt/1000==25 and Psiv/1000==5 and Ppis/1000==20 and m4*g==200 and 200+5==205
sk=('\\draw[thick] (0,3.3) -- (0,0) -- (2.2,0) -- (2.2,3.3); \\fill[vurgu!15] (.03,.03) rectangle (2.17,2.2);\n'
    '\\draw[thick,fill=gray!30] (.04,2.2) rectangle (2.16,2.35); \\draw[thick,fill=gray!50] (.55,2.35) rectangle (1.65,3.05); \\node at (1.1,2.7) {$20$ kg};\n'
    '\\draw[<->,thin] (2.55,0) -- (2.55,2.2); \\node[right] at (2.6,1.1) {$h=50$ cm};\n'
    '\\draw[<->,thin] (.04,.4) -- (2.16,.4); \\node[above,font=\\small] at (1.1,.4) {$A=100$ cm$^2$};\n'
    '\\draw[thick] (-.3,0) -- (2.5,0);')
N('0004','fz-bs3-sivi-kap','Kaplarda sıvı basıncı','Pascal Prensibi','orta',
 'Piston üzerindeki yükün sıvıya ilettiği basıncı ile sıvının ağırlığından doğan basıncı toplayarak tabandaki toplam basıncı hesaplar.',
 'Pistonun sıvıya uyguladığı basınç yük ağırlığının piston alanına oranıdır; sıvı bunu her yöne iletir. Tabandaki basınç bu değer ile sıvı sütununun basıncının toplamıdır.',
 'Yalnız sıvı sütununun ya da yalnız pistonun basıncını almak; birimleri karıştırarak N ile kPa’ı toplamak.',
 'Şekildeki silindirik kapta su, sürtünmesiz ve ağırlığı önemsenmeyecek kadar küçük bir pistonla kapatılmıştır. Pistonun üzerine şekildeki cisim konulmuştur. Su yoğunluğu 1000 kg/m³, g = 10 m/s² alınacak ve açık hava basıncı hesaba katılmayacaktır.\nBuna göre, kabın tabanındaki sıvı basıncı kaç kPa’dır?',
 25,[(5,'Yalnız su sütununun basıncını (1000 × 10 × 0,5 = 5000 Pa) bulmuş; pistondaki yükün basıncını hesaba katmamış.','dikkat'),
     (20,'Yalnız pistonun ilettiği basıncı (200 ÷ 0,01 = 20 000 Pa) bulmuş; su sütununu unutmuş.','dikkat'),
     (200,'Yükün ağırlığını (200 N) basınç değeri sanmış.','bilgi'),(205,'Yükün ağırlığı olan 200 N ile su sütununun 5 kPa’lık basıncını toplamış; birimleri karıştırmış.','islem')],
 'Tabandaki sıvı basıncı (kPa).',
 ['Basınç iki kaynaktan gelir: biri piston üzerindeki yük, diğeri suyun kendi ağırlığı. Her birini ayrı hesaplayıp aynı birimde topla.'],
 [B('Pascal prensibi','kapalı kaptaki sıvıya uygulanan basınç, sıvının her noktasına aynen iletilir. Örnek: 30 kPa’lık basınçla sıkıştırılan sıvının her noktasında bu 30 kPa ayrıca bulunur'),
  B('Sıvı basıncı','h derinlikteki basınç P = d·g·h’tır')],
 [A('Pistonun basıncını bul','Yükün ağırlığı pistona dik etkir; 100 cm² = 0,01 m².','P₁ = 20 × 10 ÷ 0,01 = 20 000 Pa'),
  A('Sıvı sütununun basıncını bul','h = 50 cm = 0,5 m.','P₂ = 1000 × 10 × 0,5 = 5 000 Pa'),
  A('Topla','Tabanda iki basınç birlikte bulunur.','P = 20 000 + 5 000 = 25 000 Pa = 25 kPa')],
 'Pistonla kapatılmış sıvıda tabandaki basınç = piston basıncı + sıvı sütununun basıncı.',sekil=tk(sk))

# =============== 05 · havuz tabanında kapak · sayısal · orta ===============
h5,A5=4,Fr(1,4); P5=1000*10*h5; F5=P5*A5
assert (P5,F5)==(40000,10000)
assert (P5*Fr(5,2), P5, P5/A5, (100000+P5)*A5)==(100000,40000,160000,35000)
sk=('\\draw[thick] (0,3.2) -- (0,0) -- (4.4,0) -- (4.4,3.2); \\fill[vurgu!15] (.03,.03) rectangle (4.37,2.6);\n'
    '\\draw[thick,fill=gray!60] (1.9,0) rectangle (2.5,.12); \\node[font=\\small] at (2.2,.45) {kapak}; \\node[font=\\small] at (2.2,.85) {$0{,}25$ m$^2$};\n'
    '\\draw[<->,thin] (-.45,0) -- (-.45,2.6); \\node[left] at (-.5,1.3) {$4$ m};\n'
    '\\draw[thin] (0,2.6) -- (-.2,2.6); \\draw[thin] (0,3.2) -- (0,3.2);\n'
    '\\draw[thick] (-.3,0) -- (4.7,0);')
N('0005','fz-bs3-sivi-kap','Kaplarda sıvı basıncı','Sıvı Basıncı','orta',
 'Derinlikteki sıvı basıncını bulup kapağın alanıyla çarparak sıvının uyguladığı basınç kuvvetini hesaplar.',
 'Havuz tabanındaki sıvı basıncı P = d·g·h ile bulunur; yatay yüzeye etkiyen kuvvet basıncın yüzey alanıyla çarpımıdır (F = P·A).',
 'Basıncı kuvvet sanmak; alana bölmek; açık hava basıncını da katmak.',
 'Şekildeki havuz ağzına kadar suyla dolu değildir; su derinliği şekilde gösterilmiştir. Havuzun yatay tabanındaki kapağın alanı şekilde verilmiştir. Su yoğunluğu 1000 kg/m³, g = 10 m/s² alınacak; yalnızca suyun kapağa uyguladığı kuvvet istenmektedir, açık hava basıncı hesaba katılmayacaktır.\nBuna göre, suyun kapağa uyguladığı kuvvet kaç N’dur?',
 10000,[(100000,'Kapak alanını 2,5 m² okumuş: 40 000 × 2,5 = 100 000 N.','dikkat'),
        (35000,'Açık hava basıncını (100 000 Pa) da ekleyerek (100 000 + 40 000) × 0,25 = 35 000 N bulmuş.','dikkat'),
        (40000,'Basıncı kuvvet sanmış: 40 000 N; alanla çarpmayı unutmuş.','bilgi'),(160000,'Basıncı alana bölmüş: 40 000 ÷ 0,25 = 160 000.','islem')],
 'Suyun kapağa uyguladığı kuvvet (N).',
 ['Önce kapağın bulunduğu derinlikteki basıncı bul; basınç ile kuvvet arasındaki bağıntıyı yaz.'],
 [B('Basınç kuvveti','yüzeye dik ve düzgün etkiyen basınç P, A alanlı yüzeye F = P·A kuvveti uygular. Örnek: 500 Pa’lık basınç 2 m²’lik yüzeye 1000 N kuvvet uygular')],
 [A('Basıncı bul','Kapak taban seviyesinde, derinlik 4 m.','P = 1000 × 10 × 4 = 40 000 Pa'),
  A('Alanı belirle','Kapak yatay tabanda olduğundan basınç kapak boyunca aynıdır; alan 0,25 m².','A = 0,25 m²'),
  A('Kuvvete çevir','F = P × A.','F = 40 000 × 0,25 = 10 000 N')],
 'Sıvının yatay yüzeye uyguladığı kuvvet: F = d·g·h·A.',sekil=tk(sk))

# =============== 06 · cıva tıkaçlı tüpte gaz basıncı · sayısal · orta ===============
P0=76; hc=14; Pg=P0+hc
assert Pg==90 and P0-hc==62 and P0+2*hc==104
sk=('\\draw[thick] (0,0) -- (0,3.6); \\draw[thick] (.6,0) -- (.6,3.6); \\draw[thick] (0,0) arc[start angle=180,end angle=360,radius=.3];\n'
    '\\fill[gray!55] (.02,1.5) rectangle (.58,2.5); \\node[font=\\small] at (.3,2.0) {cıva};\n'
    '\\draw[<->,thin] (1.0,1.5) -- (1.0,2.5); \\node[right] at (1.05,2.0) {$14$ cm};\n'
    '\\node[font=\\small] at (.3,.8) {gaz}; \\node[font=\\small] at (.3,3.9) {açık uç};')
N('0006','fz-bs3-gaz','Hapsolmuş gazın basıncı','Gaz Basıncı','orta',
 'Dikey tüpte cıva tıkacın altındaki gazın basıncını, açık hava basıncı ve cıva sütunu basıncını toplayarak bulur.',
 'Cıva tıkaç dengede olduğundan altındaki gazın basıncı, tıkacın üstündeki açık hava basıncı ile cıva sütununun basıncının toplamına eşittir.',
 'Gaz basıncını yalnız cıva sütunu ya da yalnız açık hava basıncı sanmak; cıva basıncını çıkarmak.',
 'Bir ucu kapalı, düşey bir cam tüpün kapalı ucuna şekildeki gibi gaz hapsedilmiştir; gazın üstünde şekilde boyu verilen cıva tıkaç bulunmakta, tüpün üst ucu açıktır. Sistem dengededir ve açık hava basıncı 76 cmHg’dir.\nBuna göre, tüpteki gazın basıncı kaç cmHg’dir?',
 90,[(14,'Gazın basıncını yalnız cıva sütununun yüksekliğine (14 cmHg) eşit almış; açık hava basıncını eklememiş.','dikkat'),
     (62,'Cıva sütununu açık hava basıncından çıkarmış: 76 − 14 = 62 cmHg; bu durum tüp ağzı aşağıdayken geçerlidir.','bilgi'),
     (76,'Gaz basıncını açık hava basıncına eşit almış; cıva sütununun ağırlığını unutmuş.','bilgi'),(104,'Cıva yüksekliğini iki kez eklemiş: 76 + 14 + 14 = 104 cmHg.','islem')],
 'Tüpteki gazın basıncı (cmHg).',
 ['Cıva tıkacın dengesini düşün: tıkacı aşağı iten ve yukarı iten basınçları yaz.'],
 [B('Cıvalı basınç','cıva sütunu basıncı, yüksekliğiyle (cmHg) ifade edilebilir. Örnek: 10 cm’lik cıva sütunu 10 cmHg’lik basınç oluşturur'),
  B('Denge','bir sıvı tıkaç dengedeyse tıkacın iki yüzündeki toplam basınçlar eşittir')],
 [A('Tıkacın dengesi','Tıkacı yukarıdan açık hava ve cıvanın ağırlığı iter; aşağıdan gaz basıncı destekler.','P_gaz = P₀ + h'),
  A('Değerleri oku','Açık hava basıncı 76 cmHg, cıva sütununun yüksekliği 14 cm.','P₀ = 76 cmHg · h = 14 cm'),
  A('Yerine koy','Basınçları topla.','P_gaz = 76 + 14 = 90 cmHg')],
 'Cıva tıkacın hangi yüzüne hangi basıncın etki ettiğini listele ve dengeyi yaz.',sekil=tk(sk))

# =============== 07 · pistonlu silindirde gaz basıncı · sayısal · orta ===============
m7,A7,Po=12,Fr(1,500),100000
Pgz=Po+Fr(m7*10)/A7
assert Pgz==160000 and Fr(m7*10)/A7==60000
sk=('\\draw[thick] (0,0) -- (0,2.6) ; \\draw[thick] (2.2,0) -- (2.2,2.6); \\draw[thick] (0,0) -- (2.2,0);\n'
    '\\fill[gray!15] (.03,.03) rectangle (2.17,1.4); \\node at (1.1,1.0) {gaz};\n'
    '\\draw[thick,fill=gray!40] (.03,1.4) rectangle (2.17,1.55); \\draw[thick,fill=gray!55] (.6,1.55) rectangle (1.6,2.2); \\node at (1.1,1.9) {$12$ kg};\n'
    '\\draw[<->,thin] (.03,.25) -- (2.17,.25); \\node[above,font=\\small] at (1.1,.2) {$A=20$ cm$^2$};')
N('0007','fz-bs3-gaz','Hapsolmuş gazın basıncı','Gaz Basıncı','orta',
 'Üzerinde ağırlık bulunan serbest pistonun altındaki gazın basıncını açık hava basıncı ve piston basıncını toplayarak bulur.',
 'Piston dengede olduğundan gaz basıncı, dış basınç ile pistonun üstündeki cismin ağırlığından doğan basıncın toplamına eşittir.',
 'Yalnız açık hava ya da yalnız cismin basıncını almak; basıncı çıkarmak; kuvvetle basıncı karıştırmak.',
 'Şekildeki düşey silindirde sürtünmesiz ve ağırlığı önemsenmeyecek bir piston, gazı kapatmaktadır; pistonun üstünde şekildeki cisim durmaktadır. Sistem dengededir. Açık hava basıncı 100 kPa, g = 10 m/s²’dir.\nBuna göre, silindirdeki gazın basıncı kaç kPa’dır?',
 160,[(40,'Cismin basıncını açık hava basıncından çıkarmış: 100 − 60 = 40 kPa.','islem'),(60,'Yalnız cismin pistona uyguladığı basıncı (120 ÷ 0,002 = 60 kPa) bulmuş; açık hava basıncını eklememiş.','dikkat'),
      (100,'Gaz basıncını açık hava basıncına eşit almış; cismin ağırlığını hesaba katmamış.','dikkat'),(120,'Cismin ağırlığını (120 N) kPa cinsinden basınç sanmış.','bilgi')],
 'Gazın basıncı (kPa).',
 ['Pistonun dengesini yaz: piston üzerine hangi kaynaklardan aşağı doğru basınç geliyor, aşağıdan gaz ne yapıyor?'],
 [B('Basınç–kuvvet','P = F ÷ A; 1 cm² = 10⁻⁴ m². Örnek: 50 N kuvvet 25 cm²’ye etkirse 20 000 Pa basınç oluşturur')],
 [A('Cismin basıncını bul','Ağırlık 12 × 10 = 120 N; alan 20 cm² = 0,002 m².','P₁ = 120 ÷ 0,002 = 60 000 Pa'),
  A('Dengeyi yaz','Piston dengede: gaz basıncı yukarı, açık hava ve cisim basıncı aşağı.','P_gaz = 100 000 + 60 000'),
  A('Sonuç','Basınçlar toplanır.','P_gaz = 160 000 Pa = 160 kPa')],
 'Piston dengedeyse alt ve üst yüzüne etkiyen basınçlar eşittir.',sekil=tk(sk))

# =============== 08 · kapaklı şişe, açık hava basıncı · öncüllü · orta ===============
# Kapak kapalı, delik alt kısımda; denge: P_gaz + d g h = P0 → P_gaz < P0. Kapak açılırsa üst yüzeye P0 iner → delikte iç basınç P0 + d g h > P0 → akar.
P0b=100000; dgh=1000*10*0.2; Pgaz=P0b-dgh
assert Pgaz<P0b and Pgaz+dgh==P0b and P0b+dgh>P0b
sk=('\\draw[thick] (.8,3.6) -- (.8,3.1) -- (0,2.4) -- (0,0) -- (2.6,0) -- (2.6,2.4) -- (1.8,3.1) -- (1.8,3.6);\n'
    '\\fill[vurgu!15] (.03,.03) rectangle (2.57,2.0); \\draw[thick,fill=gray!40] (.7,3.6) rectangle (1.9,3.8); \\node[font=\\small] at (1.3,4.1) {kapak};\n'
    '\\fill[white] (-.05,.22) rectangle (.05,.34); \\draw[thick] (0,.22) -- (0,.34); \\draw[thin,->] (-.7,.28) -- (-.1,.28); \\node[font=\\small] at (-1.15,.28) {delik};\n'
    '\\node[font=\\small] at (1.3,2.75) {gaz}; \\draw[thick] (-.4,0) -- (3.0,0);')
O('0008','fz-bs3-acik-hava','Açık hava basıncı','Açık Hava Basıncı','orta',
 'Üst kısmı kapalı ve alt kısmında küçük delik bulunan su dolu şişede açık hava basıncı, gaz basıncı ve sıvı basıncı ilişkisini yorumlar.',
 'Kapak kapalıyken şişedeki gaz, delik seviyesinde dışarıdaki açık hava basıncını dengeleyecek kadar seyrelmiştir; kapak açılınca üst yüzeye açık hava basıncı iner ve delikteki iç basınç dış basıncı aşar.',
 'Gaz basıncının açık hava basıncına eşit ya da büyük olduğunu sanmak; suyun akmamasını havasız kalmaya bağlamak.',
 'Alt kısmına şekildeki gibi küçük bir delik açılmış plastik bir şişe, deliği parmakla kapatılarak suyla doldurulmuş ve ağzı kapakla kapatılmıştır. Üstte bir miktar gaz kalmıştır. Parmak çekildiğinde delikten su akmamakta, şişe dengede kalmaktadır. Sıcaklık sabittir ve açık hava basıncı P₀’dır.',
 [('Kapak kapalıyken şişenin içindeki gazın basıncı P₀’dan büyüktür.',False,'Delik seviyesinde denge için P_gaz + d·g·h = P₀ olmalıdır; bu durumda P_gaz, P₀’dan d·g·h kadar küçüktür.','Gazın basıncının dışarıdan büyük olduğunu, bu yüzden suyu içeri ittiğini sanmış.'),
  ('Kapak açılırsa delikten su akmaya başlar.',True,'Kapak açılınca üst yüzeye açık hava basıncı P₀ iner; delik seviyesindeki iç basınç P₀ + d·g·h olur ve dış basınçtan büyüktür; su dışarı akar.','Kapak açıldığında da suyun akmayacağını düşünmüş.'),
  ('Kapak kapalıyken delik seviyesinde sıvının içindeki basınç, dışarıdaki basınca (P₀) eşittir.',True,'Su akmadığına göre delik seviyesinde iç ve dış basınçlar eşittir.','Su akmıyorsa bile iç basıncın dış basınçtan farklı olması gerektiğini sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 ('Kapak kapalıyken denge var; kapak açılınca üst yüzeye P₀ etkir.','Denge: delikte P_iç = P_dış'),
 ['Suyun akmaması delikte iç ve dış basınçlar hakkında ne söyler? Kapak açılınca üst yüzeydeki basınç nasıl değişir?'],
 [B('Açık hava basıncı','atmosfer, her yüzeye basınç uygular; akışkanlar basıncı yüksek yerden düşük yere doğru akar. Örnek: iki ucu açık borunun içindeki cıva, iki yüzeydeki basınç eşitse dengede kalır')],
 'Su, basıncı yüksek yerden düşük yere akar; delik seviyesindeki iç ve dış basıncı karşılaştır.',sekil=tk(sk))

# =============== 09 · P–h grafiği, iki katmanlı sıvı · sayısal · zor ===============
dX=Fr(1600,10*Fr(20,100)); dY=Fr(3600,10*Fr(30,100))
assert dX==800 and dY==1200 and dY/dX==Fr(3,2)
assert Fr(5200,10*Fr(50,100))!=1000
sk=tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}[width=7.6cm,height=5.4cm,xmin=0,xmax=60,ymin=0,ymax=6,xtick={0,20,50},ytick={0,1.6,5.2},yticklabel style={/pgf/number format/fixed,/pgf/number format/precision=1,/pgf/number format/use comma},grid=both,major grid style={gray!55,thin},tick label style={font=\\scriptsize},axis lines=left,xlabel={derinlik (cm)},ylabel={sıvı basıncı (kPa)},xlabel style={font=\\small},ylabel style={font=\\small}]\n\\addplot[thick,vurgu,mark=*,mark size=1.6pt] coordinates {(0,0) (20,1.6) (50,5.2)};\n\\end{axis}\n\\end{tikzpicture}')
O('0009','fz-bs3-sivi-grafik','Basınç–derinlik grafiğinden katmanların özkütleleri','Sıvı Basıncı','zor',
 'Karışmayan iki sıvının basınç–derinlik grafiğindeki eğimlerinden özkütleleri hesaplar ve karşılaştırır.',
 'Sıvı basıncı derinlikle doğrusal artar ve eğim d·g’ye eşittir; katman değişince eğim değişir. Her katmanın basınç artışı o katmanın kalınlığına bölünerek özkütle bulunur.',
 'Toplam basınçları ya da toplam derinlikleri oranlamak; basınç artışı yerine toplam basınç kullanmak.',
 'Birbirine karışmayan X ve Y sıvıları, yatay tabanlı bir kapta üst üste durmaktadır; üstteki X sıvısı, altta Y sıvısı yer almaktadır. Sıvı yüzeyinden itibaren derinliğe bağlı sıvı basıncı (açık hava basıncı hariç) grafikte verilmiştir; grafikteki kırılma noktası iki sıvının sınırına karşılık gelmektedir (g = 10 m/s²).',
 [('X sıvısının özkütlesi 800 kg/m³’tür.',True,'X katmanında basınç 20 cm = 0,2 m’de 1600 Pa artmıştır; d = 1600 ÷ (10 × 0,2) = 800 kg/m³.','Eğimi 1,6 kPa ÷ 20 cm = 0,08 bulup birim çevirmeyi unutarak X’in özkütlesini 80 kg/m³ sanmış.'),
  ('Y sıvısının özkütlesi X sıvısının özkütlesinin 1,5 katıdır.',True,'Y katmanında basınç artışı 3600 Pa, kalınlık 0,3 m: d = 3600 ÷ (10 × 0,3) = 1200 kg/m³; oran 1200 ÷ 800 = 1,5.','Toplam basınçları ya da toplam derinlikleri oranlamış.'),
  ('Y sıvısının özkütlesi 1000 kg/m³’tür.',False,'Y’nin özkütlesi 1200 kg/m³’tür; 5,2 kPa’ın 50 cm’ye oranından elde edilen değer katmanlı sıvıda özkütle değildir.','Toplam basıncı toplam derinliğe bölüp özkütleyi 1040 ya da yaklaşık 1000 sanmış.')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 ('Grafikte X: 0–20 cm, 1,6 kPa; Y: 20–50 cm, 1,6 → 5,2 kPa.','Δh_X = 0,2 m · Δh_Y = 0,3 m'),
 ['Her sıvı katmanı için ayrı bir eğim bul: basınç artışını o katmanın kalınlığına böl.'],
 [B('Sıvı basıncı','P = d·g·h; sabit özkütleli sıvıda basınç derinlikle doğru orantılıdır, eğim d·g’dir. Örnek: eğimi iki katına çıkan sıvının özkütlesi iki katıdır')],
 'Basınç–derinlik grafiğinde eğim d·g’dir; farklı sıvıların eğimlerini karşılaştır.',sekil=sk,kalip='grafik')

# =============== 10 · vantuz · sayısal · kolay ===============
A10=Fr(20,10000); F10=100000*A10
assert F10==200 and 100000*Fr(20,1)==2000000 and 100000*Fr(2,10)==20000
sk=('\\draw[very thick] (0,-1.2) -- (0,1.5); \\foreach \\y in {-1.1,-.8,...,1.4} \\draw[thin] (0,\\y) -- (-.3,\\y-.3);\n'
    '\\draw[thick,fill=gray!30] (0,-.7) .. controls (1.5,-.7) and (1.5,.7) .. (0,.7) -- cycle;\n'
    '\\draw[thick] (1.0,0) -- (2.0,0); \\draw[thick,fill=gray!25] (2.0,-.12) rectangle (2.25,.12);\n'
    '\\node[font=\\small,align=center] at (2.2,1.5) {vantuz, taban\\\\alanı $20$ cm$^2$}; \\draw[thin] (1.7,1.1) -- (.9,.35);\n'
    '\\draw[vurgu,very thick,-{Stealth[length=2mm,width=1.8mm]}] (2.3,0) -- (3.3,0); \\node[vurgu,above] at (2.9,.05) {$F$};')
N('0010','fz-bs3-acik-hava','Açık hava basıncı','Açık Hava Basıncı','kolay',
 'Açık hava basıncının yüzeye uyguladığı kuvveti P·A ile hesaplar.',
 'İçindeki hava tamamen boşaltılmış vantuzu, dışarıdaki açık hava basıncı duvara bastırır; vantuzu koparmak için bu basınç kuvvetine eşit kuvvet gerekir.',
 'Basıncı kuvvet sanmak; cm² ile m² dönüşümünde hata yapmak.',
 'İçindeki hava tamamen boşaltılmış bir vantuz, şekildeki gibi düzgün bir duvara yapışmıştır. Vantuzun duvara temas eden yüzeyinin alanı şekilde verilmiştir. Açık hava basıncı 10⁵ Pa’dır ve vantuzun ağırlığı önemsenmemektedir.\nBuna göre, vantuzu duvardan ayırmak için duvara dik uygulanması gereken en küçük F kuvveti kaç N’dur?',
 200,[(400,'Duvara etkiyen basıncı iki kez saymış: 2 × 10⁵ × 0,002 = 400 N.','bilgi'),(2000,'20 cm²’yi 0,02 m² almış: 10⁵ × 0,02 = 2000 N.','islem'),
      (20000,'20 cm²’yi 0,2 m² almış: 10⁵ × 0,2 = 20 000 N.','islem'),(2000000,'Alanı birim çevirmeden (20) basınçla çarpmış: 10⁵ × 20.','dikkat')],
 'Vantuzu ayırmak için gereken en küçük kuvvet (N).',
 ['Vantuzun içinde hava yoksa duvara bastıran basıncı yalnız dışarıdaki hava oluşturur; bunu alanla ilişkilendir.'],
 [B('Açık hava basıncı','atmosfer yüzeylere dik basınç uygular; F = P·A. Birim: 1 cm² = 0,0001 m². Örnek: 5 cm²’lik yüzeye 10⁵ Pa basınç 50 N kuvvet uygular')],
 [A('Alanı çevir','20 cm² = 20 × 10⁻⁴ m².','A = 0,002 m²'),
  A('Basınç kuvvetini yaz','Dışarıdan etkiyen kuvvet P₀·A.','F = P₀ × A'),
  A('Kuvveti hesapla','Değerleri yerine koy.','F = 10⁵ × 0,002 = 200 N')],
 'Hangi basıncın hangi yüzeye etkidiğini belirle; birim çevirmeyi unutma.',sekil=tk(sk))

bitir(P,'basincuc','fiz|Basınç')
