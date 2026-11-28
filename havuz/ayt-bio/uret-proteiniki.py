"""AYT Biyoloji · Genetik Şifre-Protein Sentezi · 2. dalga (10 soru). Kardeş yok, ipucu 1.
Kodon çevirisi, dizi, sayım ve öncül değerleri Python'da tek yerde tanımlanıp assert edilir."""
import sys,os,math,json,itertools
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_bio as H
from _hafif_bio import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
KONU='Genetik Şifre-Protein Sentezi'; UK='abio|Genetik Şifre-Protein Sentezi'
H.KONU=KONU
P=Parti('proteiniki',KONU,UK,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2025 Biyoloji (Genetik Şifre ve Protein Sentezi; yalnız mantık) · MEB 12. sınıf biyoloji'
TIP={'sifre':('pr2-sifre','Genetik şifre ve kodon çizelgesi'),'transl':('pr2-transl','RNA çeşitleri ve translasyon'),'kodlama':('pr2-kodlama','Kodon, antikodon ve iplik ilişkisi'),
     'mutasyon':('pr2-mutasyon','Mutasyon ve okuma çerçevesi'),'transk':('pr2-transk','Transkripsiyon ve translasyon ilişkisi')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kart(f'K-ABPR2-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KY)
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABPR2-{no[-2:]} ({ozet})',**k)
# ---------------- genetik şifre ----------------
BZ='UCAG'; AAS='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
KOD={a+b+c:AAS[i] for i,(a,b,c) in enumerate(itertools.product(BZ,BZ,BZ))}
AD={'F':'Phe','L':'Leu','S':'Ser','Y':'Tyr','C':'Cys','W':'Trp','P':'Pro','H':'His','Q':'Gln','R':'Arg','I':'Ile','M':'Met','T':'Thr','N':'Asn','K':'Lys','V':'Val','A':'Ala','D':'Asp','E':'Glu','G':'Gly'}
assert sum(1 for v in KOD.values() if v=='*')==3 and KOD['AUG']=='M'
def cevir(m,bas=0):
    """m dizisini bas'tan okur; ilk dur kodonunda durur. (aa listesi, dur görüldü mü)"""
    o=[]
    for i in range(bas,len(m)-2,3):
        a=KOD[m[i:i+3]]
        if a=='*': return o,True
        o.append(a)
    return o,False
def ad3(l): return ' – '.join(AD[a] for a in l)
def kalip_of(mrna): return ''.join({'U':'A','A':'T','G':'C','C':'G'}[c] for c in mrna)
def mrna_of(kalip): return ''.join({'A':'U','T':'A','G':'C','C':'G'}[c] for c in kalip)
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)) and len(set(sira))==5; return sira
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
NM=['I','II','III']
def onc(d,harf,neg=False,sab=None):
    """d={'I':(metin,doğru_mu,gerçek)}; neg: doğru olmayanlar istenir."""
    C={k for k in NM if d[k][1]!=neg}; assert C and len(C)<=3
    dogru=[s for s in SIR if SETS[s]==C][0]; i=SIR.index(dogru); p='ABCDE'.index(harf)
    cb=SIR[:i]; ca=SIR[i+1:]; assert p<=len(cb) and 4-p<=len(ca),(dogru,harf)
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-i))
    bef=sorted(sorted(cb,key=key)[:p],key=SIR.index); aft=sorted(sorted(ca,key=key)[:4-p],key=SIR.index)
    if sab is None:
        sab=(('{x}. yargıyı doğru sanmış; oysa yanlıştır: {n}.','{x}. yargının doğru olduğunu görememiş: {n}.') if not neg else
             ('{x}. yargıyı yanlış sanmış; oysa doğrudur: {n}.','{x}. yargıyı doğru sanmış; oysa yanlıştır: {n}.'))
    yan=[]
    for s in bef+aft:
        parts=[]
        for x in NM:
            if x in SETS[s]-C: parts.append(sab[0].format(x=x,n=d[x][2]))
            if x in C-SETS[s]: parts.append(sab[1].format(x=x,n=d[x][2]))
        assert parts; yan.append((s,' '.join(parts),'bilgi'))
    return dict(dogru=dogru,sira=bef+[dogru]+aft,yan=yan,C=C)
def oncmetin(giris,d,kok): return giris+'\n'+'\n'.join(f'{x}. {d[x][0]}' for x in NM)+'\n'+kok
def oncad(d,neg,etiket=('doğru','yanlış'),bas=None,son=None):
    a=list(bas or [])
    for x in NM: a.append(A(f'{x}. yargıyı incele',d[x][2][0].upper()+d[x][2][1:]+'.',etiket[0] if d[x][1] else etiket[1]))
    C=[x for x in NM if d[x][1]!=neg]
    a.append(A('Sonucu birleştir',son or 'İstenen yargılar bir arada yazılır.',' ve '.join(C) if len(C)<3 else 'I, II ve III'))
    return a
def tek(items,hedef,harf,yon=('Bu ifadeyi doğru sanmış; oysa yanlıştır: ','Bu ifadeyi yanlış sanmış; oysa doğrudur: ')):
    h=[s for s in items if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    dg=h[0]; dig=[s for s in items if s[1]!=hedef]; assert len(dig)==4
    sira=dig[:]; sira.insert('ABCDE'.index(harf),dg)
    yan=[(m,(yon[0] if hedef else yon[1])+n+'.','bilgi') for m,b,n in dig]
    return dict(dogru=dg[0],yan=yan,sira=[s[0] for s in sira]),dg[2]
# ---------------- şekil yardımcıları ----------------
PR="$'$"
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
OKU='-{Stealth[length=2.3mm,width=1.9mm]}'
def cod_svg():
    W=480; x0=58; cw=105; ch=62; y0=42; b=[]
    b.append(G._t(x0+2*cw,14,'2. nükleotit',size=12,bold=True))
    b.append(f'<text transform="translate(14,{y0+2*ch}) rotate(-90)" text-anchor="middle" font-size="12" style="fill:currentColor;stroke:none;font-weight:700">1. nükleotit</text>')
    for j,s in enumerate(BZ):
        b.append(f'<rect x="{x0+j*cw+1}" y="22" width="{cw-2}" height="18" style="fill:{G.ACC};fill-opacity:.18;stroke:none"/>'); b.append(G._t(x0+j*cw+cw/2,35,s,size=12,bold=True))
        b.append(f'<rect x="{x0-22}" y="{y0+j*ch+1}" width="20" height="{ch-2}" style="fill:{G.ACC};fill-opacity:.18;stroke:none"/>'); b.append(G._t(x0-12,y0+j*ch+ch/2+4,s,size=12,bold=True))
    for i,a in enumerate(BZ):
        for j,c in enumerate(BZ):
            for k,e in enumerate(BZ):
                cod=a+c+e; aa=KOD[cod]; nm='Dur' if aa=='*' else AD[aa]
                b.append(G._t(x0+j*cw+14,y0+i*ch+14+k*14,f'{cod}  {nm}',anchor='start',size=11.5,bold=(aa=='*')))
    for i in range(5): b.append(f'<line x1="{x0}" y1="{y0+i*ch}" x2="{x0+4*cw}" y2="{y0+i*ch}" stroke-width="1.2"/>')
    for j in range(5): b.append(f'<line x1="{x0+j*cw}" y1="{y0}" x2="{x0+j*cw}" y2="{y0+4*ch}" stroke-width="1.2"/>')
    return G._svg(W,y0+4*ch+4,''.join(b))
COD=cod_svg()
# ---------------- bilgi kutuları (örnekler soru sayılarını kullanmaz) ----------------
BKOD=B('Kodon ve başlangıç','Translasyon, mRNA’da 5’ ucundan başlayarak rastlanan ilk AUG kodonunda başlar; kodonlar üçer nükleotitlik gruplar hâlinde, örtüşmeden okunur. AUG aynı zamanda metiyonin kodonudur. UAA, UAG ve UGA amino asit şifrelemez ve okumayı sonlandırır.')
BRNA=B('Protein sentezinde RNA çeşitleri','mRNA genin kalıp ipliğinden kopyalanır ve kodon dizisini taşır. tRNA bir ucunda amino asit taşır, antikodonuyla mRNA kodonuna eşleşir. rRNA, ribozomun protein ile birlikte oluşturduğu yapısal bileşenidir. Üçü de DNA’dan transkripsiyonla sentezlenir.')
BDEN=B('Deney verisini yorumlama','Bir bileşen yokken olay gerçekleşmiyorsa o bileşen olay için gereklidir. Bir yargıya ulaşılabilmesi için yargının doğrudan verilerden çıkarılabilmesi gerekir; yalnız verilen veriden doğrudan çıkarılabilen yargılara ulaşılabilir.')
BGRAF=B('Grafik okuma','Sabit hızla ilerleyen bir olayda grafik doğrusal artar; eğimin aynı olması hızın aynı olduğunu, doğruların birbirinden yatay uzaklığı ise olayların başlama zamanı farkını gösterir.')
BTRNA=B('Kodon–antikodon eşleşmesi','tRNA’nın antikodonu, bağlandığı kodona tümleyendir ve karşılıklı iki ucu zıt yönlüdür; mRNA 5’→3’ yönündeyse antikodon 3’→5’ yönünde yazıldığında kodonla aynı sırada karşı karşıya gelir. Dur kodonlarına karşılık gelen tRNA yoktur. Aynı kodon tekrarlanırsa aynı tRNA çeşidi yeniden kullanılabilir.')
BMUT=B('Mutasyon ve polipeptit','Nükleotit değişimi aynı amino asidi şifreleyen bir kodon oluşturursa polipeptit değişmez; bir nükleotitin eklenmesi ya da çıkması çıkış noktasından sonraki kodonları değiştirir. Kodonun dur kodonuna dönüşmesi polipeptiti kısaltır.')
BIPL=B('Çift zincirli DNA’da kalıp iplik','RNA polimeraz kalıp ipliği 3’→5’ yönünde okur ve RNA’yı 5’→3’ yönünde uzatır. Çift zincirli DNA’nın iki ipliği zıt yönlüdür; bu yüzden aynı bölgede ters yönlerde ilerleyen iki transkripsiyon, iki ayrı ipliği kalıp olarak kullanır.')
BKUL=B('Başlangıç kodonu ve okuma','Ribozom, mRNA’da ilk AUG kodonunu bulduğunda translasyonu başlatır ve üçlü gruplar hâlinde okur. İlk AUG kodonu bozulursa okuma sonraki AUG kodonundan başlar; çerçeve, bu yeni başlangıç noktasına göre belirlenir.')
BSAY=B('Kodon çeşidi ve amino asit çeşidi','n çeşit nükleotitten üçlü kodon sayısı n×n×n’dür. Genetik şifre dejeneredir: farklı kodonlar aynı amino asidi şifreleyebilir; bu yüzden amino asit çeşidi, amino asit şifreleyen kodon sayısından küçük ya da ona eşittir.')
BTR=B('Transkripsiyon ve translasyon','Transkripsiyon DNA’dan RNA sentezidir; translasyon mRNA’dan polipeptit sentezidir. Bakterilerde mRNA ürünü çekirdek zarı olmadan ribozomla buluşur. Transkripsiyon engellenirse yeni RNA oluşmaz; translasyon engellenirse yeni RNA oluşur ama yeni polipeptit oluşmaz.')

# ===== 01 · kolay · kodon çizelgesi · AUG ve okuma çerçevesi
M1='GAAUGUUCGCAUAAGGC'; i0=M1.index('AUG'); assert i0==2
o1,s1=cevir(M1,i0); assert ''.join(o1)=='MFA' and s1
f0,_=cevir(M1,0); assert ''.join(f0)=='ECSHK'
f1,_=cevir(M1,1); assert ''.join(f1)=='NVRIR'
ge,_=cevir(M1,i0+3); assert ''.join(ge)=='FA'
th=''.join(o1)+'G'; assert KOD[M1[14:17]]=='G'
D1=[(ad3(f0),'Okumaya mRNA’nın ilk nükleotidinden başlamış; oysa translasyon ilk AUG kodonundan başlar ve öncesindeki nükleotitler okunmaz.','dikkat'),
    (ad3(ge),'Başlangıç kodonunu amino asit saymamış; oysa AUG metiyonin şifreler ve polipeptitin ilk amino asidi olur.','bilgi'),
    (ad3(o1)+' – Gly','UAA dur kodonunda okumayı sürdürüp sonraki GGC kodonunu da amino asit olarak yazmış; oysa dur kodonu translasyonu sonlandırır.','dikkat'),
    (ad3(f1),'Okumayı 2. nükleotitten başlatmış; oysa çerçeve ilk AUG kodonunun ilk nükleotidinden itibaren belirlenir.','dikkat')]
Q('0001','sifre','kolay','şekilli','Kodon çizelgesi ile polipeptit dizilimi','Genetik şifre çizelgesini kullanarak mRNA’dan polipeptit dizilimini belirler.','Okuma ilk AUG kodonunda başlar, üçer üçer ilerler ve ilk dur kodonunda biter.','Okumaya mRNA’nın ilk nükleotidinden başlamak; dur kodonundan sonrasını da okumak.','AUG’den dur kodonuna okuma',
 [A('Başlangıcı bul','Translasyon mRNA’da 5’ ucundan başlayarak ilk AUG kodonunda başlar; dizide bu kodonun yeri aranır.','AUG, 3. nükleotitle başlar'),
  A('Üçer üçer oku','AUG’den itibaren dizi örtüşmeden üçlü gruplar hâlinde bölünür ve her kodon çizelgeden okunur.','AUG · UUC · GCA · UAA · GGC'),
  A('Dur kodonunda bitir','UAA dur kodonu olduğundan okuma burada sonlanır; sonraki nükleotitler okunmaz.','Dur kodonu: UAA'),
  A('Dizilimi yaz','Dur kodonundan önceki kodonların amino asitleri sırayla yazılır.','Met – Phe – Ala')],
 metin='Şekilde genetik şifre çizelgesi verilmiştir. Ökaryotik bir hücrede ribozoma bağlanan mRNA’nın nükleotit dizisi 5’–GAAUGUUCGCAUAAGGC–3’ şeklindedir. Translasyon, mRNA’da 5’ ucundan başlayarak rastlanan ilk AUG kodonunda başlamakta ve ilk dur kodonunda sonlanmaktadır.\nBuna göre, sentezlenen polipeptitin amino asit dizilimi aşağıdakilerden hangisidir?',
 sekil=COD,dogru=ad3(o1),yan=D1,sira=yer('C',ad3(o1),[x[0] for x in D1]),
 istenen='Polipeptitin amino asit dizilimi',ip=['Önce başlangıç kodonunun dizide nerede olduğuna bak; okumayı oradan başlat.'],bilgi=[BKOD],puf='Başlangıç AUG, bitiş dur kodonu; arası üçer üçer okunur.')

# ===== 02 · kolay · düz · RNA çeşitleri (yanlış)
it2=[('mRNA, genin kalıp ipliğinden sentezlenir ve kodon dizisini ribozoma taşır.',True,'mRNA kalıp ipliğe tümleyen sentezlenir ve genetik bilgiyi ribozoma taşır'),
     ('tRNA, antikodonuyla mRNA’daki kodona bağlanır ve ribozoma amino asit getirir.',True,'tRNA bir amino asit taşır ve antikodonuyla kodona eşleşir'),
     ('rRNA, ribozomun yapısına proteinlerle birlikte katılır.',True,'ribozom rRNA ve proteinlerden oluşur'),
     ('Üç çeşit RNA da DNA üzerindeki genlerden transkripsiyonla sentezlenir.',True,'mRNA, tRNA ve rRNA genlerden transkripsiyonla oluşur'),
     ('rRNA, mRNA kodonlarıyla eşleşen antikodonlar taşıyarak amino asitleri ribozoma taşır.',False,'antikodon taşıyan ve amino asit getiren RNA tRNA’dır; rRNA ribozomun yapısal bileşenidir')]
r2,g2=tek(it2,False,'A')
Q('0002','transl','kolay','düz','RNA çeşitleri','Protein sentezindeki RNA çeşitlerinin görevlerini ayırt eder.','Antikodon ve amino asit taşıma tRNA’nın görevidir; rRNA ribozomun yapısal bileşenidir.','tRNA ve rRNA görevlerini karıştırmak.','RNA çeşitlerinin görevleri',
 [A('RNA çeşitlerini hatırla','mRNA kodonları taşır, tRNA amino asit getirir, rRNA ribozomun yapısına katılır.','mRNA · tRNA · rRNA'),
  A('İfadeleri görevleriyle karşılaştır','Her ifadedeki görev, ilgili RNA çeşidinin gerçek görevi ile karşılaştırılır.','Görev eşleştirme'),
  A('Yanlış görevi bul','Antikodon taşıyıp amino asit getirme görevi rRNA’ya verilmiştir; bu görev tRNA’ya aittir.','Yanlış: rRNA antikodon taşır')],
 metin='Protein sentezinde mRNA, tRNA ve rRNA olmak üzere üç çeşit RNA görev alır.\nBu RNA çeşitleriyle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r2['dogru'],yan=r2['yan'],sira=r2['sira'],istenen='RNA çeşitleriyle ilgili yanlış ifade',ip=['Antikodon taşıyan ve amino asit getiren RNA çeşidini düşün.'],bilgi=[BRNA],puf='Antikodon ve amino asit: tRNA; ribozomun yapısı: rRNA.')

# ===== 03 · orta · tablo · hücre dışı sistem (ulaşılamaz)
TUP=[('1','Var','Var','Var','Var','Var'),('2','Yok','Var','Var','Var','Yok'),('3','Var','Yok','Var','Var','Yok'),('4','Var','Var','Yok','Var','Yok'),('5','Var','Var','Var','Yok','Yok')]
assert all(t[5]=='Var' for t in TUP if all(x=='Var' for x in t[1:5])) and sum(1 for t in TUP if t[5]=='Var')==1
for t in TUP[1:]: assert t[1:5].count('Yok')==1 and t[5]=='Yok'
d3={'I':('Polipeptit sentezi için ribozom, mRNA, tRNA ve amino asidin dördü de gereklidir.',True,'her bileşen tek tek çıkarıldığında polipeptit sentezlenmemiştir; bu, dört bileşenin de gerekli olduğunu gösterir'),
    'II':('Ribozom bulunmayan ortamda mRNA ve tRNA, polipeptit sentezini tek başına sağlayabilir.',False,'ribozomun bulunmadığı 2. tüpte mRNA, tRNA ve amino asit bulunduğu hâlde polipeptit sentezlenmemiştir; veri bu yargıyla çelişir'),
    'III':('Polipeptit sentezi için DNA da gereklidir.',False,'DNA hiçbir tüpe eklenmediği hâlde 1. tüpte polipeptit sentezlenmiştir; veri bu yargıyla çelişir')}
sab3=('{x}. yargıya ulaşılabileceğini görememiş: {n}.','{x}. yargıya ulaşılamayacağını görememiş: {n}.')
r3=onc(d3,'E',neg=True,sab=sab3); assert r3['dogru']=='II ve III'
Q('0003','transl','orta','tablo','Hücre dışı protein sentezi deneyi','Hücre dışı sistem deneyinden hangi sonuçlara ulaşılabileceğini ayırt eder.','Bir bileşen yokken sentez olmuyorsa bileşen gereklidir; verilerle çelişen yargıya ulaşılamaz.','Verideki karşılaştırmayı yargının hükmüyle eşleştirmemek.','bileşen eksikliği ve sonuç yorumu',
 oncad(d3,True,('ulaşılabilir','ulaşılamaz'),son='Deney sonuçlarından çıkarılamayan yargılar bir arada yazılır.'),
 metin=oncmetin('Bir araştırmacı, hücre özütü içermeyen bir düzenekte 5 tüp hazırlıyor. Her tüpe ATP ve gerekli enzimler eklenmiş, tüplerin hiçbirine DNA konmamıştır. Tüplere eklenen bileşenler ve polipeptit sentezlenip sentezlenmediği tabloda verilmiştir.',d3,'Buna göre, yalnız bu tablodaki verilerden doğrudan çıkarılabilenler dikkate alındığında yukarıdaki yargılardan hangilerine ulaşılamaz?'),
 sekil=tablo_svg(['Tüp','Ribozom','mRNA','tRNA','Amino asit','Polipeptit sentezi'],[list(t) for t in TUP]),dogru=r3['dogru'],yan=r3['yan'],sira=r3['sira'],
 istenen='Deney sonuçlarından çıkarılamayan yargılar',ip=['Her yargı için tabloda bunu gösteren bir karşılaştırma var mı diye bak.'],bilgi=[BDEN],puf='Her yargıyı tablodaki bir karşılaştırmayla doğrula ya da çürüt.')

# ===== 04 · orta · grafik · üç ribozom, zaman–uzunluk
HIZ=2; UZ=60; BAS={1:0,2:10,3:20}; BIT={k:v+UZ//HIZ for k,v in BAS.items()}
def aa_at(k,t): return max(0,min(UZ,(t-BAS[k])*HIZ)) if t>=BAS[k] else None
assert all(BAS[k]<=25<BIT[k] for k in BAS)           # I: 25. s'de üçü de etkin
assert aa_at(2,35)==50 and BAS[2]<=35<BIT[2]          # II
assert all(aa_at(k,BIT[k])==UZ for k in BAS)          # III: hepsi aynı uzunlukta
d4={'I':('25. saniyede mRNA üzerinde üç ribozom da translasyon yapmaktadır.',True,'1. ribozom 30. saniyeye, 2. ribozom 40. saniyeye, 3. ribozom 50. saniyeye kadar sentez yaptığından 25. saniyede üçü de etkindir'),
    'II':('35. saniyede 2. ribozomun sentezlediği polipeptit zincirinde 50 amino asit bulunur.',True,'2. ribozom 10. saniyede başlamış ve saniyede 2 amino asit eklediğinden 35. saniyede 50 amino asitlik zincire ulaşmıştır'),
    'III':('3. ribozom, 1. ribozomdan daha hızlı ilerlemektedir.',False,'üç doğru da paraleldir; eğimler eşit olduğundan ribozomların ilerleme hızı aynıdır, yalnız başlama zamanları farklıdır')}
r4=onc(d4,'D'); assert r4['dogru']=='I ve II'
def f4():
    b=[r'\begin{axis}[width=8.2cm,height=5.4cm,xmin=0,xmax=56,ymin=0,ymax=70,xtick={0,10,20,30,40,50},ytick={0,20,40,60},axis lines=left,xlabel={Zaman (saniye)},ylabel={Polipeptitteki amino asit sayısı},tick label style={font=\footnotesize},label style={font=\small},every axis plot/.append style={line width=1.6pt},grid=both,grid style={black!12}]']
    sty={1:'black',2:'vurgu',3:'black!60,dashed'}
    for k in (1,2,3): b.append(rf'\addplot[{sty[k]}] coordinates {{({BAS[k]},0)({BIT[k]},{UZ})}};')
    for k in (1,2,3): b.append(rf'\node[font=\small\bfseries,anchor=west] at (axis cs:{BIT[k]+.8},{UZ}) {{{k}}};')
    b.append(r'\end{axis}'); return tk('\n'.join(b),.95)
Q('0004','transl','orta','grafik','Polizomda ribozomların ilerlemesi','Grafikten ribozomların başlama zamanı ve polipeptit uzunluğunu yorumlar.','Aynı hızla ilerleyen ribozomların doğruları paraleldir; eğimler hızı, yatay uzaklık başlama farkını gösterir.','Geç başlayan ribozomun daha yavaş ya da daha kısa polipeptit yaptığını sanmak.','grafikte ribozom ilerlemesi',
 oncad(d4,False,son='Doğru yargılar bir arada yazılır.',bas=[A('Grafiği oku','Her ribozomun başlama anı ve dur kodonuna ulaştığı an doğruların başlangıç ve bitiş noktalarından okunur.','1. ribozom 0 – 30 s · 2. ribozom 10 – 40 s · 3. ribozom 20 – 50 s')]),
 metin=oncmetin('Şekilde, bir mRNA üzerinde translasyon yapan üç ribozomun (1, 2 ve 3) sentezlediği polipeptit zincirlerindeki amino asit sayısının zamanla değişimi gösterilmiştir. Ribozomların üçü de mRNA’nın başlangıç kodonundan başlayıp dur kodonuna kadar aynı sabit hızla ilerlemekte; dur kodonuna ulaşan ribozom polipeptiti tamamlayıp mRNA’dan ayrılmaktadır.',d4,'Buna göre, yukarıdaki yargılardan hangileri doğrudur?'),
 sekil=f4(),dogru=r4['dogru'],yan=r4['yan'],sira=r4['sira'],istenen='Grafikle uyumlu doğru yargılar',ip=['Her doğrunun hangi saniyede başlayıp hangi saniyede bittiğini ayrı ayrı oku.'],bilgi=[BGRAF],puf='Paralel doğrular: aynı hız, farklı başlangıç zamanı.')

# ===== 05 · orta · tablo · tRNA çeşitleri
M5='AUGUUCGCCUUCGAAUAG'; k5=[M5[i:i+3] for i in range(0,18,3)]; assert KOD[k5[-1]]=='*' and all(KOD[k]!='*' for k in k5[:-1])
ANT={'I':'GGA','II':'AAG','III':'UAC','IV':'CUU','V':'UCG','VI':'CGG'}
anti=lambda k:''.join({'A':'U','U':'A','G':'C','C':'G'}[c] for c in k)
kul=set(anti(k) for k in k5[:-1]); assert kul<=set(ANT.values()) and len(kul)==4 and len(ANT)==6
CES=len(kul); PB=len(k5[:-1])-1; assert CES+PB==8
VAL5=dict(dogru=8,yan=[(7,'Başlangıç kodonuna bağlanan tRNA’yı saymayıp tRNA çeşidini 3 bulmuş; bu durumda 3 + 4 = 7 olur.','dikkat'),
  (9,'Tekrarlanan UUC kodonu için iki ayrı tRNA çeşidi sayarak tRNA çeşidini 5 bulmuş; bu durumda 5 + 4 = 9 olur.','dikkat'),
  (10,'Tablodaki 6 tRNA çeşidinin hepsinin kullanıldığını sanmış; bu durumda 6 + 4 = 10 olur.','bilgi'),
  (11,'tRNA çeşidini 6 alıp peptit bağı sayısı yerine amino asit sayısını (5) eklemiş; bu durumda 6 + 5 = 11 olur.','dikkat')])
assert {8,7,9,10,11}=={VAL5['dogru']}|{y[0] for y in VAL5['yan']} and 5+4==9 and 6+4==10 and 6+5==11 and 3+4==7
Q('0005','kodlama','orta','tablo','tRNA çeşidi ve peptit bağı sayısı','Kodon–antikodon eşleşmesinden kullanılan tRNA çeşidini ve peptit bağı sayısını bulur.','Her kodon antikodonu tümleyen tRNA çeşidiyle eşleşir; tekrarlanan kodon aynı tRNA çeşidini kullanır, dur kodonuna tRNA bağlanmaz.','Tekrarlanan kodonu ayrı çeşit saymak; dur kodonu için tRNA aramak.','tRNA çeşidi + peptit bağı',
 [A('Kodonlara ayır','mRNA bölümü başlangıç kodonundan itibaren üçlülere ayrılır; son üçlü dur kodonudur.','AUG · UUC · GCC · UUC · GAA · UAG'),
  A('Amino asit kodonlarını belirle','Dur kodonuna tRNA bağlanmadığından beş kodon amino asit şifreler; tekrarlanan kodonlar aynı tRNA çeşidini kullanır.','4 farklı kodon · 5 amino asit'),
  A('tRNA çeşidini ve bağı say','Her farklı kodon için antikodonu tümleyen bir tRNA çeşidi gerekir; n amino asitli zincirde n − 1 peptit bağı bulunur.','4 tRNA çeşidi · 4 peptit bağı'),
  A('Toplamı bul','tRNA çeşidi sayısı ile peptit bağı sayısı toplanır.','4 + 4')],
 metin='Tabloda, bir bakteri hücresindeki altı tRNA çeşidinin antikodonları 3’→5’ yönünde verilmiştir. Bu hücrede mRNA’nın 5’–AUGUUCGCCUUCGAAUAG–3’ bölümü başlangıç kodonundan başlayarak dur kodonuna kadar eksiksiz translasyona uğramaktadır. Her tRNA çeşidi yalnız kendi antikodonuna tümleyen kodona bağlanmakta ve bir tRNA çeşidi yeniden kullanılabilmektedir.\nBuna göre, bu translasyonda kullanılan tRNA çeşidi sayısı ile sentezlenen polipeptitteki peptit bağı sayısının toplamı kaçtır?',
 sekil=tablo_svg(['tRNA','Antikodon (3’→5’)'],[[k,v] for k,v in ANT.items()]),dogru=VAL5['dogru'],yan=VAL5['yan'],
 istenen='tRNA çeşidi sayısı ile peptit bağı sayısının toplamı',ip=['mRNA’yı kodonlara ayır, her kodonu tabloyla eşleştir.'],bilgi=[BTRNA],puf='Farklı kodon sayısı tRNA çeşidini, amino asit sayısı eksi bir peptit bağını verir.')

# ===== 06 · orta · düz · mutasyon yargıları (yanlış)
M6='AUGGAACUGAAAGGCUACUGA'; K6=[M6[i:i+3] for i in range(0,21,3)]
def aa6(m): o,s=cevir(m); return o,s
base,_=aa6(M6); assert ''.join(base)=='MELKGY'
m1=M6[:11]+'G'+M6[12:]; assert K6[3]=='AAA' and m1[9:12]=='AAG' and aa6(m1)[0]==base
m2=M6[:3]+M6[4:]; assert aa6(m2)[0]==['M','N'] and len(aa6(m2)[0])==2
m3=M6[:17]+'U'+M6[18:]; assert M6[15:18]=='UAC' and m3[15:18]=='UAU' and len(aa6(m3)[0])==6
d6={'I':('4. kodonun 3. nükleotidi A yerine G olursa polipeptitin amino asit dizilimi değişmez.',True,'AAA ve AAG kodonlarının ikisi de lizin şifrelediğinden dizilim değişmez'),
    'II':('2. kodonun 1. nükleotidi olan G yok olursa polipeptit 2 amino asitten oluşur.',True,'G yok olunca okuma çerçevesi kayar, AUG AAC UGA şeklinde okunur ve dur kodonu erkenden gelir; polipeptit Met ve Asn’den oluşur'),
    'III':('6. kodonun 3. nükleotidi C yerine U olursa polipeptit 5 amino asitten oluşur.',False,'UAC yerine UAU oluşur; ikisi de tirozin şifrelediğinden polipeptit yine 6 amino asitten oluşur')}
r6=onc(d6,'B',neg=True); assert r6['dogru']=='Yalnız III'
Q('0006','mutasyon','orta','düz','Mutasyonların polipeptite etkisi','Nükleotit değişimi ve çıkmasının polipeptite etkisini kodonlar üzerinden değerlendirir.','Aynı amino asidi şifreleyen kodona dönüşüm polipeptiti değiştirmez; bir nükleotitin çıkması okuma çerçevesini kaydırır.','Her nükleotit değişiminin amino asit dizilimini değiştirdiğini düşünmek.','sessiz mutasyon ve çerçeve kayması',
 oncad(d6,True,son='Yanlış yargılar bir arada yazılır.',bas=[A('mRNA’yı kodonlara ayır','Verilen bölüm üçlülere ayrılır ve kodon–amino asit ilişkileriyle polipeptit belirlenir.','AUG · GAA · CUG · AAA · GGC · UAC · UGA')]),
 metin=oncmetin('Bir bakteriye ait mRNA’nın başlangıç kodonuyla başlayan bölümü 5’–AUGGAACUGAAAGGCUACUGA–3’ dizisindedir ve translasyon bu bölümdeki dur kodonunda sonlanmaktadır. Kodon–amino asit ilişkileri şöyledir: AUG: Met, GAA: Glu, AAC: Asn, CUG: Leu, AAA ve AAG: Lys, GGC: Gly, UAC ve UAU: Tyr, UGA: dur.\nBu mRNA’da ayrı ayrı gerçekleşen mutasyonlarla ilgili aşağıdaki yargılar öne sürülüyor.',d6,'Buna göre, bu yargılardan hangileri yanlıştır?'),
 dogru=r6['dogru'],yan=r6['yan'],sira=r6['sira'],istenen='Yanlış olan yargılar',ip=['Her mutasyondan sonra mRNA’yı yeniden üçer üçer okuyup amino asitleri karşılaştır.'],bilgi=[BMUT],puf='Önce mutant mRNA’yı yaz, sonra üçlülere ayırıp oku.')

# ===== 07 · zor · kodon çizelgesi · yapay mRNA, kodon çeşitleri
S7='ACU'; ks=[''.join(p) for p in itertools.product(S7,repeat=3)]
n7=len(ks); st7=sum(1 for k in ks if KOD[k]=='*'); aa7={KOD[k] for k in ks if KOD[k]!='*'}; n_aa7=len([k for k in ks if KOD[k]!='*'])
assert (n7,st7,len(aa7),n_aa7)==(27,1,11,26) and [k for k in ks if KOD[k]=='*']==['UAA']
dg7='27 – 1 – 11'
D7=[('27 – 3 – 11','Dur kodonu sayısını çizelgedeki gibi 3 almış; oysa UAG ve UGA kodonları guanin içerdiğinden bu mRNA’larda bulunamaz.','dikkat'),
    ('27 – 1 – 26','Her amino asit şifreleyen kodonu ayrı bir amino asit çeşidi saymış; oysa farklı kodonlar aynı amino asidi şifreleyebilir.','dikkat'),
    ('26 – 1 – 11','Kodon çeşidinden dur kodonunu düşmüş; oysa dur kodonu da bir kodon çeşididir ve toplam 27 kodon vardır.','bilgi'),
    ('27 – 1 – 12','Dur kodonunu da amino asit çeşidi gibi saymış; oysa dur kodonu amino asit şifrelemez.','dikkat')]
assert 11+1==12 and len({dg7}|{x[0] for x in D7})==5
Q('0007','sifre','zor','şekilli','Sınırlı nükleotitle kodon çeşitleri','Kodon sayısını kombinasyonla bulup çizelgeden dur kodonu ve amino asit çeşidini belirler.','Üç nükleotit çeşidinden 27 kodon oluşur; dur kodonları ve aynı amino asidi şifreleyen kodonlar çizelgeden ayrı ayrı sayılır.','Üç dur kodonunun da bulunacağını varsaymak; kodon sayısını amino asit çeşidi saymak.','kodon kombinasyonu ve dejenerelik',
 [A('Kodon çeşidini hesapla','Üç çeşit nükleotitle her kodon konumu üç farklı nükleotitle doldurulabilir.','3 × 3 × 3 = 27'),
  A('Dur kodonlarını ayıkla','Üç dur kodonundan yalnız guanin içermeyenler bu mRNA’larda bulunabilir.','Yalnız UAA bulunabilir'),
  A('Amino asitleri çizelgeden ayır','Kalan 26 kodonun şifrelediği amino asitler çizelgeden okunur ve tekrar edenler bir kez sayılır.','11 farklı amino asit'),
  A('Sonuçları sırala','Kodon çeşidi, dur kodonu sayısı ve amino asit çeşidi sırayla yazılır.','27 – 1 – 11')],
 metin='Şekilde genetik şifre çizelgesi verilmiştir. Bir araştırmacı, hücre dışı protein sentezi düzeneğinde yalnız adenin, sitozin ve urasil nükleotitlerinden oluşan yapay mRNA’lar kullanıyor; bu üç nükleotit mRNA’larda her sırada bulunabilmektedir.\nBuna göre, bu mRNA’larda bulunabilecek kodon çeşidi, dur kodonu çeşidi ve şifrelenen amino asit çeşidi sayıları sırasıyla aşağıdakilerden hangisidir?',
 sekil=COD,dogru=dg7,yan=D7,sira=yer('E',dg7,[x[0] for x in D7]),istenen='Kodon, dur kodonu ve amino asit çeşidi sayıları',ip=['Önce üç nükleotitle kaç kodon yazılabildiğini bul; sonra yazılabilecek kodonların hangi nükleotitleri içerdiğine bak.'],bilgi=[BSAY],puf='Kodon sayısı n³; amino asit çeşidi çizelgeden tekrarsız sayılır.')

# ===== 08 · orta · tablo · bakteri kültürleri, engelleyici maddeler
T8=[('1','Yok','Var','Var'),('2','X','Yok','Yok'),('3','Y','Var','Yok')]
dg8='X: transkripsiyon – Y: translasyon'
D8=[('X: translasyon – Y: transkripsiyon','Maddelerin etkilerini ters yazmış; oysa X varlığında yeni RNA oluşmadığından X, Y varlığında yeni RNA oluşup polipeptit oluşmadığından Y etkilidir.','dikkat'),
    ('X: replikasyon – Y: translasyon','X için replikasyonu seçmiş; oysa replikasyon engellense de RNA sentezi sürebilir, 2. kültürde RNA hiç oluşmadığından X transkripsiyonu engeller.','bilgi'),
    ('X: transkripsiyon – Y: replikasyon','Y için replikasyonu seçmiş; oysa 3. kültürde RNA oluşurken polipeptit oluşmadığından Y translasyonu engeller.','bilgi'),
    ('X: translasyon – Y: replikasyon','X’in RNA oluşumunu değil polipeptiti engellediğini sanıp translasyonu seçmiş; Y’de polipeptit oluşmadığı için sorunu çoğalmaya (replikasyon) bağlamış; oysa X RNA sentezini (transkripsiyon), Y RNA okunmasını (translasyon) engeller.','bilgi')]
assert len({dg8}|{x[0] for x in D8})==5 and T8[1][2:]==('Yok','Yok') and T8[2][2:]==('Var','Yok')
Q('0008','transk','orta','tablo','Engelleyici maddelerin etkisi','Kültür verilerinden maddelerin hangi evreyi engellediğini çıkarır.','Yeni RNA oluşmuyorsa transkripsiyon, RNA oluşup polipeptit oluşmuyorsa translasyon engellenmiştir.','Polipeptit oluşmamasını her zaman translasyon engeli saymak.','transkripsiyon ve translasyon engeli',
 [A('Kontrolü incele','Madde eklenmeyen kültürde hem yeni RNA hem yeni polipeptit oluşur; engellenen olay bu duruma göre anlaşılır.','1. kültür: RNA var, polipeptit var'),
  A('X’in etkisine bak','X varken yeni RNA oluşmamıştır; mRNA olmayınca polipeptit sentezi de gerçekleşmemiştir.','RNA yok: transkripsiyon engellenmiş'),
  A('Y’nin etkisine bak','Y varken yeni RNA oluşmuş fakat polipeptit oluşmamıştır; sorun RNA’nın okunmasındadır.','RNA var, polipeptit yok: translasyon engellenmiş'),
  A('Sonucu yaz','Maddelerin engellediği olaylar sırasıyla yazılır.','X: transkripsiyon · Y: translasyon')],
 metin='Bir araştırmacı, aynı türden üç bakteri kültürünü farklı koşullarda bir süre bekletiyor. 2. ve 3. kültürlere sırasıyla X ve Y maddeleri ekleniyor; her madde yalnız bir olayı engellemektedir. Süre sonunda kültürlerde yeni RNA ve yeni polipeptit oluşup oluşmadığı tabloda verilmiştir.\nBuna göre, X ve Y maddelerinin engellediği olaylar aşağıdakilerden hangisinde doğru verilmiştir?',
 sekil=tablo_svg(['Kültür','Eklenen madde','Yeni RNA','Yeni polipeptit'],[list(t) for t in T8]),dogru=dg8,yan=D8,sira=yer('A',dg8,[x[0] for x in D8]),istenen='X ve Y maddelerinin engellediği olaylar',ip=['Her kültürde RNA oluşumu ile polipeptit oluşumunu ayrı ayrı karşılaştır.'],bilgi=[BTR],puf='RNA yoksa transkripsiyon; RNA var ama polipeptit yoksa translasyon engellenmiştir.')

# ===== 09 · zor · şekilli · çift iplikli DNA'da ters yönlü iki gen
TOP='ATGCTTCAGGCGCTAAAGTGGTTTTGACAT'; assert len(TOP)==30
BOT=''.join({'A':'T','T':'A','G':'C','C':'G'}[c] for c in TOP)       # alt ipliğin sol→sağ okunuşu (3'→5')
mX=TOP.replace('T','U')                                              # alt iplik kalıp, soldan sağa transkripsiyon
mY=mrna_of(TOP)[::-1]                                                # üst iplik kalıp, sağdan sola transkripsiyon
assert mY==''.join({'A':'U','T':'A','G':'C','C':'G'}[c] for c in reversed(TOP))
aX,sX=cevir(mX); aY,sY=cevir(mY); assert sX and sY and (len(aX),len(aY))==(8,5) and aX[0]=='M' and aY[0]=='M'
assert mX[:3]=='AUG' and mY[:3]=='AUG'
swX=len(aY); swY=len(aX)           # roller ters alınırsa
nX,pY=len(aX),len(aY)-1
dg9=f'{nX} – {pY}'; assert dg9=='8 – 4'
# kalıp ipliği yönsüz kopyalayan hata: Y için revers almadan tümleyen
yy=mrna_of(TOP); ayy,_=cevir(yy); 
D9=[(f'{swX} – {swY-1}','Kalıp iplikleri ters almış: X’i üst iplikten, Y’yi alt iplikten okumuş; oysa soldan sağa ilerleyen transkripsiyon alt ipliği, sağdan sola ilerleyen üst ipliği kalıp alır.','dikkat'),
    (f'{nX} – {len(aY)}','Y polipeptidinin amino asit sayısını vermiş; oysa istenen peptit bağı sayısıdır ve bu, amino asit sayısından bir eksiktir.','dikkat'),
    (f'{nX+1} – {pY}','X’te dur kodonunu da amino asit saymış; oysa dur kodonu amino asit şifrelemez.','dikkat'),
    (f'{nX-1} – {pY}','X için de peptit bağı sayısını vermiş; oysa X’ten istenen amino asit sayısıdır.','dikkat')]
assert len({dg9}|{x[0] for x in D9})==5 and (swX,swY-1)==(5,7)
def f9():
    dx,gap=0.34,0.22; xs=[i*dx+(i//3)*gap for i in range(30)]; b=[]
    for x,ct,cb in zip(xs,TOP,BOT):
        b.append(N(x,1.0,ct,'font=\\large\\ttfamily\\bfseries')); b.append(N(x,0.0,cb,'font=\\large\\ttfamily\\bfseries'))
        b.append(f'\\draw[line width=.5pt,black!55] ({x:.3f},0.28)--({x:.3f},0.72);')
    b.append(N(-.55,1.0,f'5{PR}')); b.append(N(xs[-1]+.55,1.0,f'3{PR}')); b.append(N(-.55,0.0,f'3{PR}')); b.append(N(xs[-1]+.55,0.0,f'5{PR}'))
    b.append(f'\\draw[{OKU},line width=1.5pt,color=vurgu] ({xs[0]},-0.75)--({xs[-1]},-0.75);'); b.append(N((xs[0]+xs[-1])/2,-1.15,'X geninin transkripsiyonu','font=\\normalsize'))
    b.append(f'\\draw[{OKU},line width=1.5pt,color=vurgu] ({xs[-1]},1.75)--({xs[0]},1.75);'); b.append(N((xs[0]+xs[-1])/2,2.15,'Y geninin transkripsiyonu','font=\\normalsize'))
    return tk('\n'.join(b),.9)
Q('0009','kodlama','zor','şekilli','Aynı bölgede ters yönlü iki gen','Çift zincirli DNA’da zıt yönlerde ilerleyen iki transkripsiyonun kalıp ipliğini ve ürünlerini belirler.','Soldan sağa ilerleyen transkripsiyon 3’ ucu solda olan ipliği, sağdan sola ilerleyen ise diğer ipliği kalıp alır.','İki mRNA’yı da aynı iplikten ve aynı yönde okumak.','iki gende kalıp iplik ve polipeptit uzunluğu',
 [A('Kalıp iplikleri belirle','RNA polimeraz kalıbı 3’→5’ yönünde okur; soldan sağa ilerleyen X için 3’ ucu solda olan alt iplik, sağdan sola ilerleyen Y için üst iplik kalıptır.','X: alt iplik · Y: üst iplik'),
  A('mRNA’ları yaz','X’in mRNA’sı alt ipliğe tümleyen olduğundan üst iplikle aynı diziyi (T yerine U) taşır; Y’nin mRNA’sı üst ipliğin ters yönde tümleyenidir.','X: AUG CUU CAG GCG … · Y: AUG UCA AAA CCA …'),
  A('Dur kodonlarını bul','Her mRNA başlangıç kodonundan okunur ve ilk dur kodonunda sonlanır.','X: 9. kodon UGA · Y: 6. kodon UAG'),
  A('İstenenleri hesapla','X’te dur kodonundan önceki kodon sayısı amino asit sayısıdır; Y’de bu sayıdan bir eksik peptit bağı sayısını verir.','8 amino asit · 4 peptit bağı')],
 metin='Şekilde, bir bakteri DNA’sında üçlü gruplar hâlinde verilen 30 baz çiftlik bölge gösterilmiştir. Bu bölgenin sol ucundan başlayan X geni ile sağ ucundan başlayan Y geni, oklarla belirtilen yönlerde ve ayrı ipliklerden transkripsiyonla mRNA’ya kopyalanmaktadır. Her iki mRNA’nın da ilk kodonu başlangıç kodonudur ve translasyon ilk dur kodonunda sonlanmaktadır.\nBuna göre, X geninden sentezlenen polipeptitteki amino asit sayısı ile Y geninden sentezlenen polipeptitteki peptit bağı sayısı sırasıyla aşağıdakilerden hangisidir?',
 sekil=f9(),dogru=dg9,yan=D9,sira=yer('C',dg9,[x[0] for x in D9]),istenen='X’teki amino asit sayısı ve Y’deki peptit bağı sayısı',ip=['Önce her transkripsiyon yönü için hangi ipliğin 3’ ucunun RNA polimerazın geldiği tarafta olduğuna bak.'],bilgi=[BIPL],puf='Her gende mRNA’yı önce kalıp ipliğe göre yaz, sonra kodonlara ayır.')

# ===== 10 · zor · şekilli dizi · ilk AUG mutasyonu ve çerçeve
M10='GCAUGCAUGAAUUAGCUUGACC'; K10=kalip_of(M10); assert K10=='CGTACGTACTTAATCGAACTGG' and mrna_of(K10)==M10
n10,_=cevir(M10,M10.index('AUG')); assert ''.join(n10)=='MHELA'
t=K10.index('TAC'); assert t==2
K10m=K10[:t]+'C'+K10[t+1:]; M10m=mrna_of(K10m); assert M10m[:5]=='GCGUG' and M10m.index('AUG')==6
mu,smu=cevir(M10m,M10m.index('AUG')); assert ''.join(mu)=='MN' and smu
dg10=ad3(mu); assert KOD['GUG']=='V' and KOD['AAU']=='N' and KOD['UAG']=='*'
D10=[('Val – His – Glu – Leu – Ala','Translasyonun, değişen GUG kodonuyla başladığını sanmış; oysa bu soruda translasyon yalnız AUG kodonundan başlar; okuma sonraki AUG kodonundan başlar.','dikkat'),
     ('Met – His – Glu – Leu – Ala','Mutasyonun polipeptiti etkilemediğini sanmış; oysa ilk AUG kodonu bozulduğundan okuma başka bir AUG kodonundan başlar.','bilgi'),
     ('His – Glu – Leu – Ala','Okumayı bozulan AUG’den sonraki kodondan sürdürmüş; oysa ribozom, ilk bozulmamış AUG kodonunu arar.','dikkat'),
     ('Asn','Başlangıç kodonunu amino asit saymamış; oysa ikinci AUG kodonu da metiyonin şifreler ve ilk amino asit olur.','dikkat')]
assert len({dg10}|{x[0] for x in D10})==5 and ad3(n10)=='Met – His – Glu – Leu – Ala'
def f10():
    dx=0.34; b=[]
    for i,ch in enumerate(K10): b.append(N(i*dx,0,ch,'font=\\large\\ttfamily\\bfseries'))
    b.append(N(-.55,0,f'3{PR}')); b.append(N((len(K10)-1)*dx+.55,0,f'5{PR}')); b.append(N(-.55,.62,'Kalıp iplik','anchor=west,font=\\normalsize\\bfseries'))
    return tk('\n'.join(b))
Q('0010','mutasyon','zor','şekilli','Başlangıç kodonunun bozulması','Başlangıç kodonunu bozan mutasyonun okuma çerçevesine ve polipeptit dizilimine etkisini değerlendirir.','İlk AUG bozulursa okuma sonraki AUG’den, onun belirlediği çerçeveyle başlar.','Okumanın bozulan kodondan ya da aynı çerçeveden sürdüğünü sanmak.','başlangıç kodonu mutasyonu',
 [A('mRNA’yı yaz','Kalıp iplikteki her nükleotitin tümleyeni alınarak mRNA oluşturulur.','GCAUGCAUGAAUUAGCUUGACC'),
  A('Mutasyonu uygula','Kalıptaki T nükleotidinin C ile değişmesi, mRNA’da bu kodonun ilk nükleotidinin A yerine G olmasına yol açar.','İlk AUG → GUG'),
  A('Yeni başlangıcı bul','Bu soruda translasyon yalnız AUG kodonundan başlar; ribozom mRNA’da ilk bulduğu bozulmamış AUG’den başlar ve çerçeve bu noktadan belirlenir.','AUG · AAU · UAG'),
  A('Dizilimi yaz','Dur kodonuna kadar okunan kodonların amino asitleri sırayla yazılır.','Met – Asn')],
 metin='Şekilde, bir bakteri geninin kalıp ipliğinin 3’→5’ yönündeki 22 nükleotitlik bölümü verilmiştir. Bu bölümün tamamından mRNA sentezlenmekte ve ribozom, mRNA’da rastladığı ilk AUG kodonundan translasyonu başlatıp ilk dur kodonunda sonlandırmaktadır. Bu bölümdeki ilk AUG kodonunu şifreleyen TAC üçlüsünün T nükleotidi, mutasyonla C ile yer değiştiriyor.\nKodon–amino asit ilişkileri: AUG: Met, CAU: His, GAA: Glu, UUA: Leu, GCU: Ala, AAU: Asn, GUG: Val; UGA ve UAG: dur.\nBuna göre, mutasyondan sonra oluşan polipeptitin amino asit dizilimi aşağıdakilerden hangisidir?',
 sekil=f10(),dogru=dg10,yan=D10,sira=yer('D',dg10,[x[0] for x in D10]),istenen='Mutant polipeptitin amino asit dizilimi',ip=['Mutasyondan sonra mRNA’yı yeniden yaz ve ribozomun başlayabileceği AUG kodonunu ara.'],bilgi=[BKUL],puf='Önce mutant mRNA’yı yaz, ilk AUG’yi bul, çerçeveyi oradan kur.')

# ---------------- çıktı ----------------
for q in P.ANA: q['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-proteiniki.json'
P.yaz(os.path.join(GD,'proteiniki-1.json'),SC)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Biyoloji (yalnız mantık), MEB 12. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abproteiniki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
