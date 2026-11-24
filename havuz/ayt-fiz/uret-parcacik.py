"""AYT Fizik · Büyük Patlama ve Parçacık Fiziği · 20 soru (kardeş yok, ipucu 1). Her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
H.KONU='Büyük Patlama ve Parçacık Fiziği'
P=Parti('parcacik','Büyük Patlama ve Parçacık Fiziği','afiz|Büyük Patlama ve Parçacık Fiziği',ders='AYT Fizik',idon='aytfiz')
KY='ÖSYM AYT 2022–2026 Fizik (Büyük Patlama ve Evrenin Oluşumu; yalnız mantık) · 345 AYT Fizik s.331–392 · Bilgi Sarmal AYT Fizik · MEB 12. sınıf fizik'
TIPLER={'pc-kuark':'Kuarklar, yük ve hadronlar','pc-sinif':'Standart model sınıflandırması','pc-kuvvet':'Temel kuvvetler ve aracı parçacıklar','pc-karsit':'Karşıt madde ve çift olayları',
 'pc-evren':'Evrenin evreleri ve soğuması','pc-kanit':'Büyük Patlama’nın gözlemsel kanıtları','pc-nukleo':'İlk çekirdek oluşumu','pc-tepkime':'Korunum yasalarıyla tepkime analizi'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AFPC-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),kart=f'K-AFPC-{kn:02d} ('+CARD[kn]+')',**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,box/.style={draw,rounded corners=2pt,thick,align=center,inner sep=4pt},\n wav/.style={decorate,decoration={snake,amplitude=1.3pt,segment length=5pt},thick}]\n'
TAIL='\n\\end{tikzpicture}'
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos):
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if t}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex: parts.append(f'{n}. yargıyı da doğru sanmış; gerçekte {why[nm.index(n)]}.')
        for n in ms: parts.append(f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
def ech(x):
    x=Fr(x)
    if x==0: return '0'
    s='+' if x>0 else '−'; n,d=abs(x.numerator),x.denominator
    return f'{s}e' if (n,d)==(1,1) else f'{s}{n if n!=1 else ""}e/{d}' if d!=1 else f'{s}{n}e'
UK,DK=Fr(2,3),Fr(-1,3)
# ---------- bilgi kutuları (örnekler soruların sayılarını kullanmaz)
KU=B('Kuarklar ve hadronlar','yukarı (u) kuarkın yükü +2e/3, aşağı (d) kuarkın yükü −e/3’tür; karşıt kuarklar aynı kütleli ve zıt yüklüdür. Baryonlar üç kuarktan, mezonlar bir kuark ile bir karşıt kuarktan oluşur; ikisi de hadrondur ve güçlü kuvvetten etkilenir. Leptonlar kuark içermez. Örnek: bir baryonun yükü, üç kuarkın yüklerinin cebirsel toplamıdır')
SN=B('Standart model sınıflandırması','temel parçacıklar fermiyonlar (madde parçacıkları: kuarklar ve leptonlar) ile bozonlar (kuvvet taşıyıcıları) olarak ayrılır. Leptonlar (elektron, müon, tau ve nötrinolar) güçlü kuvvet hissetmez; kuarklar hisseder. Örnek: nötrino yüksüz bir leptondur, elektriksel etkileşime girmez')
KV=B('Temel kuvvetler','güçlü kuvvet (gluon): kuarkları hadronda tutar, menzili çok kısadır; elektromanyetik kuvvet (foton): yüklü parçacıklar arasında, menzili sonsuzdur; zayıf kuvvet (W ve Z bozonları): beta bozunumu ve nötrino etkileşimleri, menzili çok kısadır; kütle çekimi: en zayıf kuvvet, menzili sonsuzdur. Örnek: göreli şiddet sıralaması güçlü > elektromanyetik > zayıf > kütle çekimidir')
KS=B('Karşıt madde','her parçacığın kütlesi aynı, yükü ve baryon/lepton sayısı zıt bir karşıt parçacığı vardır. Parçacık ile karşıtı karşılaşınca yok olur ve enerjiye dönüşür; yeterli enerjili foton da bir parçacık–karşıt parçacık çifti oluşturabilir. Örnek: durgun bir parçacık–karşıt parçacık çiftinin yok olmasında toplam enerji, iki parçacığın kütle enerjileri toplamıdır')
KO=B('Korunum yasaları','her tepkimede toplam elektriksel yük, toplam baryon sayısı ve toplam lepton sayısı korunur (parçacıklar için +1, karşıt parçacıklar için −1 alınır; foton ve kuvvet taşıyıcıları 0’dır). Örnek: yük ve baryon sayısı korunup lepton sayısı korunmayan bir tepkime gerçekleşmez')
EV=B('Evrenin evreleri','Büyük Patlama’dan sonra evren genişlerken soğur: kuark–gluon plazması → proton ve nötronlar → helyum çekirdekleri → (yaklaşık 380 000 yıl sonra) nötr atomlar ve ışığın serbest kalması → yıldız ve gökadalar. Genişleme sırasında ışınımın sıcaklığı evrenin ölçeğiyle ters orantılı azalır. Örnek: ölçek iki katına çıkarsa sıcaklık yarıya iner')
HB=B('Genişleme kanıtları','uzaktaki gökadaların ışığı kırmızıya kayar; kırmızıya kayma z = Δλ ÷ λ₀ ve düşük hızlarda v = z × c bağıntısı geçerlidir. Hubble yasası: v = H × d. Her gökada sabit hızla uzaklaşmışsa evrenin yaşı t = d ÷ v = 1 ÷ H alınır. Örnek: H küçülürse bulunan yaş büyür')
NK=B('İlk çekirdek oluşumu','Büyük Patlama’dan birkaç dakika sonra çekirdek oluşumunda kütlece yaklaşık %75 hidrojen ve %25 helyum oluştu. Bir çekirdeğin kütlesi nükleon sayısıyla orantılıdır: hidrojen çekirdeği 1, helyum-4 çekirdeği 4 birim. Örnek: sayı oranı kütle oranının kütle numarasına bölünmüş hâlidir')
# ===== 01 kolay · baryon yükü
card(1,'Baryonun yükünü kuarklardan bulma','Hadronun yükü, içerdiği kuarkların yüklerinin cebirsel toplamıdır; u kuarkı +2e/3, d kuarkı −e/3 yüklüdür.','Bir kuarkı saymamak ya da proton (uud) ile karıştırmak.','kolay','tablo',3,'pc-kuark','kuark yükleri tabloda; yapı verilir, yük istenir')
SK=tablo_svg(['Kuark','Elektriksel yük'],[['Yukarı (u)','+2e/3'],['Aşağı (d)','−e/3']])
tot=lambda *x:sum(x,Fr(0))
c=tot(UK,DK,DK); assert c==0
assert tot(DK,DK)==Fr(-2,3) and tot(UK,DK)==Fr(1,3) and UK==Fr(2,3) and tot(UK,UK,DK)==1
q('0001',tipId='pc-kuark',tip=TIPLER['pc-kuark'],z='kolay',alt='Kuarklar',kaz='Hadronların yükünü kuark yüklerinden hesaplar.',kalip='tablo',
 metin='Standart modelde yukarı (u) ve aşağı (d) kuarkların elektriksel yükleri tabloda verilmiştir (e: elektronun yükünün büyüklüğü). Yapısında yalnızca bir yukarı kuark ve iki aşağı kuark bulunan bir hadron inceleniyor.\nBuna göre bu hadronun elektriksel yükü kaçtır?',
 sekil=SK,dogru='0',yan=[('−2e/3','İki aşağı kuarkın yüklerini toplayıp yukarı kuarkı hesaba katmamış: −e/3 − e/3 = −2e/3.','dikkat'),('+e/3','İki aşağı kuarktan yalnız birini hesaba katmış: +2e/3 − e/3 = +e/3.','dikkat'),
  ('+2e/3','Yalnız yukarı kuarkın yükünü almış, aşağı kuarkları saymamış.','dikkat'),('+e','Yapıyı proton (u u d) ile karıştırıp +2e/3 + 2e/3 − e/3 = +e yazmış.','bilgi')],
 sira=['−2e/3','0','+e/3','+2e/3','+e'],istenen='Hadronun elektriksel yükü.',
 ip=['Her kuarkın yükünü ayrı ayrı yaz ve yapıda kaç tane bulunduğuna göre cebirsel olarak topla.'],bilgi=[KU],
 ad=[A('Kuark yüklerini oku','Tablodaki yükler kuark başına verilir.','u: +2e/3; d: −e/3'),
     A('Sayıları yerleştir','Yapıda bir u ve iki d vardır.','Q = (+2e/3) + 2 × (−e/3)'),
     A('Topla','Payları cebirsel olarak toplayıp sadeleştir.','Q = (2 − 2)e/3 = 0')],
 puf='Hadronun yükü = Σ(kuark yükleri); her kuarkı sayıdaki payıyla ayrı ayrı yazmak hata payını azaltır.')
# ===== 02 kolay · sınıflandırma şeması
card(2,'Parçacığı şemada yerleştirme','Foton kuvvet taşıyıcısıdır; müon leptondur (güçlü kuvvet hissetmez); aşağı kuark güçlü kuvvetten etkilenir.','Kuarkları da güçlü kuvvetten etkilenmeyen grupta saymak; fotonu madde parçacığı sanmak.','kolay','şekilli',3,'pc-sinif','sınıflandırma şemasına üç parçacık yerleştirme')
o=[ '\\node[box] (T) at (0,3.1) {Temel parçacıklar};',
 '\\node[box] (K) at (-2.2,1.5) {\\textbf{K}\\\\Madde parçacıkları};','\\node[box] (L) at (2.4,1.5) {\\textbf{L}\\\\Kuvvet taşıyıcıları};',
 '\\node[box] (M) at (-3.7,-.3) {\\textbf{M}\\\\Güçlü kuvvetten\\\\etkilenenler};','\\node[box] (N) at (-.6,-.3) {\\textbf{N}\\\\Güçlü kuvvetten\\\\etkilenmeyenler};',
 '\\draw[thick] (T.south) -- ++(0,-.3) -| (K.north);','\\draw[thick] (T.south) -- ++(0,-.3) -| (L.north);',
 '\\draw[thick] (K.south) -- ++(0,-.3) -| (M.north);','\\draw[thick] (K.south) -- ++(0,-.3) -| (N.north);']
SK=tikz(o)
G2={'foton':'L','müon':'N','aşağı kuark':'M'}
q('0002',tipId='pc-sinif',tip=TIPLER['pc-sinif'],z='kolay',alt='Standart Model',kaz='Parçacıkları standart model sınıflandırmasındaki yerlerine yerleştirir.',kalip='şekilli',
 metin='Standart modele göre temel parçacıkların sınıflandırılması şemada K, L, M ve N kutularıyla gösterilmiştir. Parçacıklar her zaman, kendisini kapsayan kutulardan en özel olanına yerleştirilecektir.\nBuna göre foton, müon ve aşağı kuark parçacıkları sırasıyla hangi kutulara yerleştirilir?',
 sekil=SK,dogru='L – N – M',yan=[('L – M – N','Müonu güçlü kuvvetten etkilenen, aşağı kuarkı etkilenmeyen gruba koymuş; leptonla kuarkın yerini karıştırmış.','bilgi'),
  ('K – N – M','Fotonu madde parçacığı saymış; oysa foton elektromanyetik kuvvetin taşıyıcısıdır.','bilgi'),('L – N – N','Aşağı kuarkı da güçlü kuvvetten etkilenmeyen gruba koymuş; oysa kuarklar güçlü kuvvet hisseder.','bilgi'),
  ('L – M – M','Müonu da güçlü kuvvetten etkilenen gruba koymuş; oysa müon bir leptondur ve güçlü kuvvet hissetmez.','bilgi')],
 sira=['K – N – M','L – M – M','L – M – N','L – N – M','L – N – N'],istenen='Parçacıkların yerleştirileceği kutular.',
 ip=['Önce her parçacığın madde parçacığı mı kuvvet taşıyıcısı mı olduğuna, sonra güçlü kuvvetten etkilenip etkilenmediğine karar ver.'],bilgi=[SN],
 ad=[A('Foton','Elektromanyetik kuvvetin aracı parçacığıdır.','foton → L'),A('Müon','Leptondur; güçlü kuvvet hissetmez.','müon → N'),A('Aşağı kuark','Kuarklar güçlü kuvvetle etkileşir.','aşağı kuark → M')],
 puf='Önce madde/kuvvet ayrımını yap; madde parçacıklarında kuark mı lepton mu diye güçlü kuvvete bak.')
# ===== 03 kolay · kuvvet–aracı
card(3,'Kuvvet ve aracı parçacık eşleştirmesi','Güçlü kuvvet gluonla, elektromanyetik kuvvet fotonla, zayıf kuvvet W ve Z bozonlarıyla taşınır.','Gluon ile fotonu karıştırmak; Higgs’i kuvvet taşıyıcısı saymak.','kolay','düz',2,'pc-kuvvet','kuvvet–aracı eşleştirme')
q('0003',tipId='pc-kuvvet',tip=TIPLER['pc-kuvvet'],z='kolay',alt='Temel Kuvvetler',kaz='Temel kuvvetleri aracı parçacıklarıyla eşleştirir.',kalip='düz',
 metin='Standart modelde temel kuvvetler, aracı parçacıkların kuvvetin etkidiği parçacıklar arasında değiş tokuş edilmesiyle açıklanır.\nBuna göre aşağıdaki kuvvet – aracı parçacık eşleştirmelerinden hangisi doğrudur?',
 sekil=None,dogru='Güçlü kuvvet – gluon',yan=[('Elektromanyetik kuvvet – gluon','Gluonu elektromanyetik kuvvetin taşıyıcısı sanmış; elektromanyetik kuvvet foton değiş tokuşuyla açıklanır.','bilgi'),
  ('Zayıf kuvvet – foton','Zayıf kuvveti fotonla ilişkilendirmiş; zayıf kuvvet W ve Z bozonlarıyla taşınır.','bilgi'),('Kütle çekim kuvveti – W bozonu','Kütle çekimini W bozonuyla eşleştirmiş; W bozonu zayıf kuvvetin aracısıdır.','bilgi'),
  ('Güçlü kuvvet – Higgs bozonu','Higgs bozonunu güçlü kuvvetin taşıyıcısı saymış; Higgs bozonu parçacıklara kütle kazandırma ile ilgilidir.','bilgi')],
 sira=['Güçlü kuvvet – gluon','Elektromanyetik kuvvet – gluon','Zayıf kuvvet – foton','Kütle çekim kuvveti – W bozonu','Güçlü kuvvet – Higgs bozonu'],istenen='Doğru kuvvet – aracı parçacık eşleştirmesi.',
 ip=['Kuarkları hadron içinde bir arada tutan kuvvetin hangi aracı parçacıkla taşındığını düşün.'],bilgi=[KV],
 ad=[A('Aracıları hatırla','Her kuvvetin ayrı bir aracı parçacığı vardır.','güçlü: gluon; elektromanyetik: foton; zayıf: W, Z'),A('Higgs bozonunu ayır','Higgs bozonu bir kuvvet taşıyıcısı değil, kütle kazandırma mekanizmasının parçacığıdır.','Higgs → kuvvet taşıyıcısı değil'),A('Seçenekleri ele','Yalnız bir eşleşme bu listeyle uyuşur.','Güçlü kuvvet – gluon')],
 puf='Gluon = güçlü, foton = elektromanyetik, W/Z = zayıf; Higgs kuvvet taşıyıcısı değil, kütle kazandıran alanın bozonudur.')
# ===== 04 orta · kartlar öncüllü
card(4,'Yük ve kuark sayısından sınıf belirleme','Üç kuarklı parçacık baryon, kuark–karşıt kuark çifti mezon, kuarksız yüklü parçacık lepton olabilir.','İki kuarklı parçacığı lepton saymak.','orta','öncüllü',3,'pc-kuark','yük ve kuark sayısı verilen üç parçacığın sınıfı')
def kart_ciz(x,adi,yuk,nk):
    s=[f'\\node[box,minimum width=2.7cm,minimum height=2.9cm] at ({x},0) {{}};',f'\\node at ({x},1.15) {{\\textbf{{{adi}}}}};']
    if nk==0: s.append(f'\\node[font=\\scriptsize] at ({x},.2) {{kuark yok}};')
    else:
        xs=[(-.6+1.2*i/(max(nk-1,1))) for i in range(nk)] if nk>1 else [0]
        for t in xs: s.append(f'\\filldraw[fill=vurgu!35,thick] ({x+t*(0.9 if nk==3 else .7)},.35) circle (.3);')
        s.append(f'\\node[font=\\scriptsize] at ({x},-.2) {{{nk} kuark/karşıt kuark}};')
    s.append(f'\\node at ({x},-.85) {{Yük: ${yuk}$}};'); return s
o=kart_ciz(0,'I','+e',3)+kart_ciz(3.2,'II','0',2)+kart_ciz(6.4,'III','-e',0)
SK=tikz(o)
q('0004',tipId='pc-kuark',tip=TIPLER['pc-kuark'],z='orta',alt='Hadron ve Lepton',kaz='Yük ve kuark içeriği verilen parçacıkları baryon, mezon ve lepton olarak sınıflandırır.',kalip='öncüllü',
 metin='Şekilde, üç farklı parçacığın elektriksel yükü ve yapısında bulunan kuark (ya da karşıt kuark) sayısı gösterilmiştir (e: elektronun yükünün büyüklüğü). Parçacıkların kararlı olup olmadığı bilinmemektedir.\nBuna göre,\nI. I numaralı parçacık bir baryon olabilir.\nII. II numaralı parçacık bir lepton olabilir.\nIII. III numaralı parçacık elektron olabilir.\nyargılarından hangileri kesinlikle doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Üç kuarklı, iki kuarklı ve kuarksız parçacıkların hangi sınıflara girdiğini ayrı ayrı düşün.'],bilgi=[KU,SN],
 ad=[A('I. yargı','Üç kuarktan oluşan parçacık baryondur.','3 kuark → baryon → I doğru'),A('II. yargı','Yapısında kuark bulunan parçacık hadrondur, lepton olamaz.','2 kuark → mezon (hadron) → II yanlış'),A('III. yargı','Yüklü ve kuarksız parçacık elektron olabilir.','yük −e, kuark yok → III doğru')],
 puf='Kuark içeren parçacık hadrondur (üç kuark: baryon, kuark–karşıt kuark: mezon); kuark içermeyen madde parçacığı leptondur.',
 **onc([True,False,True],['üç kuarklı parçacık baryon olabilir','kuark içeren parçacık hadrondur ve lepton olamaz','yük −e olan kuarksız parçacık elektron olabilir'],4))
# ===== 05 zor · nötron bozunumu
card(5,'Kuark düzeyinde nötron bozunumu','d → u dönüşümünde W bozonu −e yükü taşır; W bozonu bozunurken yük ve lepton sayısı toplamı korunur.','Lepton sayısını unutup nötrino ile karşıt nötrinoyu karıştırmak.','zor','şekilli',4,'pc-tepkime','nötron bozunumu diyagramında X ve Y')
PRT={'elektron':(-1,1),'pozitron':(1,-1),'elektron nötrinosu':(0,1),'karşıt elektron nötrinosu':(0,-1),'foton':(0,0)}
def tp(a,b): return (PRT[a][0]+PRT[b][0],PRT[a][1]+PRT[b][1])
assert tp('elektron','karşıt elektron nötrinosu')==(-1,0)   # W⁻ : yük −1, lepton sayısı 0
assert tp('pozitron','elektron nötrinosu')==(1,0) and tp('elektron','elektron nötrinosu')==(-1,2) and tp('elektron','foton')==(-1,1) and tp('elektron','pozitron')==(0,0) and tp('pozitron','karşıt elektron nötrinosu')==(1,-2)
o=['\\draw[thick,-{Stealth}] (0,2) -- (1.9,2); \\draw[thick] (1.9,2) -- (4,2) node[right] {u};','\\node[left] at (0,2) {u};',
 '\\draw[thick,-{Stealth}] (0,1) -- (1.9,1); \\draw[thick] (1.9,1) -- (4,1) node[right] {d};','\\node[left] at (0,1) {d};',
 '\\draw[thick,-{Stealth}] (0,0) -- (.9,0); \\draw[thick] (.9,0) -- (1.6,0) coordinate (V1); \\draw[thick,-{Stealth}] (1.6,0) -- (3.4,0); \\draw[thick] (3.4,0) -- (4,0) node[right] {u};','\\node[left] at (0,0) {d};',
 '\\draw[wav] (V1) -- (2.5,-1.1) coordinate (V2);','\\node[right,font=\\small] at (2.05,-.42) {W};',
 '\\draw[thick,-{Stealth}] (V2) -- (3.3,-.55); \\draw[thick] (3.3,-.55) -- (4,-.55) node[right] {X};','\\draw[thick,-{Stealth}] (V2) -- (3.3,-1.65); \\draw[thick] (3.3,-1.65) -- (4,-1.65) node[right] {Y};',
 '\\node[font=\\small] at (-1.1,1) {nötron};','\\node[font=\\small] at (5.2,1) {proton};',
 '\\draw[thin,gray] (4.55,2.3) -- (4.65,2.3) -- (4.65,-.3) -- (4.55,-.3);']
SK=tikz(o)
opt5=[('elektron','karşıt elektron nötrinosu'),('pozitron','elektron nötrinosu'),('elektron','elektron nötrinosu'),('elektron','foton'),('elektron','pozitron')]
fmt=lambda a:f'X: {a[0]}, Y: {a[1]}'
q('0005',tipId='pc-tepkime',tip=TIPLER['pc-tepkime'],z='zor',alt='Beta Bozunumu',kaz='Zayıf etkileşimde yük ve lepton sayısı korunumuyla ürün parçacıkları belirler.',kalip='şekilli',
 metin='Şekilde, bir nötronun kuark düzeyinde bozunması gösterilmiştir. Nötron içindeki aşağı kuarklardan biri yukarı kuarka dönüşürken W aracı bozonunu yayınlamakta, W bozonu da hemen X ve Y parçacıklarına bozunmaktadır. Bozunmada toplam yük ve toplam lepton sayısı korunur; kuarkların yükleri +2e/3 ve −e/3’tür.\nBuna göre X ve Y parçacıkları aşağıdakilerden hangisidir?',
 sekil=SK,dogru=fmt(opt5[0]),yan=[(fmt(opt5[1]),'W bozonunun yükünü +e almış; oysa d → u dönüşümünde yük −e/3 → +2e/3 olduğundan W bozonu −e yüklüdür.','bilgi'),
  (fmt(opt5[2]),'Yükü doğru bulmuş ama lepton sayısını korumamış; elektron ve nötrino birlikte +2 lepton sayısı getirir, W bozonunun lepton sayısı sıfırdır.','dikkat'),
  (fmt(opt5[3]),'Yükü elektronla sağlamış ama lepton sayısını unutmuş; elektronun +1 lepton sayısını dengeleyen bir karşıt lepton gerekir.','dikkat'),
  (fmt(opt5[4]),'Elektronun lepton sayısını karşıt lepton olan pozitronla dengelemiş; fakat bu çift yüksüzdür ve W bozonunun −e yükünü taşıyamaz.','bilgi')],
 sira=[fmt(x) for x in [opt5[3],opt5[1],opt5[2],opt5[4],opt5[0]]],istenen='X ve Y parçacıkları.',
 ip=['W bozonunun yükünü kuark dönüşümünden bul; sonra yük ve lepton sayısı toplamını ürün çiftine uygula.'],bilgi=[KO,KV],
 ad=[A('W bozonunun yükü','Kuark yükleri toplamı korunur.','−e/3 = +2e/3 + Q(W) → Q(W) = −e'),A('Lepton sayısı','W bozonunun lepton sayısı sıfırdır, ürünlerin toplamı da sıfır olmalıdır.','L(X) + L(Y) = 0'),
     A('X’i belirle','Yükü −e olan hafif lepton elektrondur (L = +1).','X: elektron'),A('Y’yi belirle','Yük toplamı −e kalması için Y yüksüz, lepton sayısı −1 olmalıdır.','Y: karşıt elektron nötrinosu')],
 puf='Zayıf bozunmada önce yük, sonra lepton sayısını denkleştir: elektronla birlikte her zaman karşıt nötrino çıkar.')
# ===== 06 orta · yok olma enerjisi
card(6,'Çift yok olmasında foton enerjisi','Durgun parçacık–karşıt parçacık çiftinin toplam kütle enerjisi, zıt yönde çıkan iki eşit fotona paylaşılır.','Toplam enerjiyi paylaştırmayı unutmak ya da tek parçacığın enerjisini almak.','orta','şekilli',3,'pc-karsit','durgun e⁻ e⁺ yok olması, foton enerjisi')
E1=Fr(51,100); Eg=(2*E1)/2; assert Eg==E1 and 2*E1==Fr(102,100)
o=['\\filldraw[fill=vurgu!30,thick] (-3.1,0) circle (.45) node {$e^-$};','\\filldraw[fill=vurgu!30,thick] (-2.2,0) circle (.45) node {$e^+$};',
 '\\node[font=\\scriptsize,align=center] at (-2.65,-1) {durgun\\\\$mc^2=0{,}51$ MeV\\\\(her biri)};','\\draw[thick,-{Stealth[length=2.4mm]}] (-1.3,0) -- (-.2,0);',
 '\\draw[wav] (0,0) -- (-1.2,0) ++(0,0);','\\draw[wav] (.4,0) -- (1.6,.9) node[right] {$\\gamma_1$};','\\draw[wav] (.4,0) -- (1.6,-.9) node[right] {$\\gamma_2$};']
o=[l for l in o if '(0,0) -- (-1.2,0)' not in l]
SK=tikz(o)
q('0006',tipId='pc-karsit',tip=TIPLER['pc-karsit'],z='orta',alt='Yok Olma',kaz='Parçacık–karşıt parçacık yok olmasında ortaya çıkan fotonların enerjisini kütle enerjisinden hesaplar.',kalip='şekilli',
 metin='Şekilde, birbirine çok yakın ve durgun bir elektron ile pozitronun yok olarak enerjiye dönüşmesi gösterilmiştir. Yok olma sonunda aynı büyüklükte enerjiye sahip iki foton (γ₁ ve γ₂) zıt yönlerde yayılmaktadır. Elektron ve pozitronun her birinin durgun kütle enerjisi şekilde verilmiştir.\nBuna göre her bir fotonun enerjisi kaç MeV’dir?',
 sekil=SK,dogru=Fr(51,100),yan=[(0,'Parçacıkların durgun olduğunu görüp fotonların enerjisiz olacağını sanmış; oysa kütle enerjisi fotonlara aktarılır.','bilgi'),(Fr(255,1000),'Bir parçacığın kütle enerjisini (0,51) iki fotona böldüğünde 0,255 bulmuş; diğer parçacığın enerjisini katmamış.','dikkat'),
  (Fr(102,100),'Toplam enerjiyi (0,51 + 0,51 = 1,02) iki fotona paylaştırmadan her fotonun enerjisi saymış.','dikkat'),(Fr(204,100),'Toplam enerjiyi bir kez daha ikiyle çarpmış: 1,02 × 2 = 2,04.','islem')],
 istenen='Her bir fotonun enerjisi (MeV).',
 ip=['Yok olmadan önceki toplam enerjiyi bul; iki fotonun enerjisi eşit olduğundan bu enerjiyi nasıl bölüştüklerini düşün.'],bilgi=[KS],
 ad=[A('Toplam enerji','Parçacıklar durgun olduğundan yalnız kütle enerjileri vardır.','E = 0,51 + 0,51 = 1,02 MeV'),A('Enerji korunumu','Yok olmadan önceki toplam enerji iki fotonun enerjileri toplamına eşittir.','Eγ₁ + Eγ₂ = 1,02 MeV'),A('Paylaştır','Fotonların enerjileri eşittir.','Eγ = 1,02 ÷ 2 = 0,51 MeV')],
 puf='Durgun çift yok olurken toplam enerji = 2mc²; her bir foton bunun yarısını, yani bir parçacığın mc² değerini taşır.')
assert Fr(255,1000)==E1/2
# ===== 07 orta · evren sıralama
card(7,'Evrenin evrelerinin sırası','Plazma → hadronlar → helyum çekirdekleri → nötr atomlar → yıldızlar sırası, sıcaklığın düşmesiyle belirlenir.','Atom oluşumunu çekirdek oluşumundan önce sanmak.','orta','şekilli',3,'pc-evren','beş olayın zaman sırası')
EV7={'K':'Proton ve nötronların birleşerek helyum çekirdeklerini oluşturması','L':'Kuarkların bir araya gelerek proton ve nötronları oluşturması','M':'Elektronların çekirdeklere bağlanarak nötr atomların oluşması','N':'Gaz bulutlarının çökmesiyle ilk yıldızların oluşması','P':'Evrenin kuark ve gluonlardan oluşan çok sıcak bir plazma hâlinde bulunması'}
o=[]; pos7={'K':(0,0),'L':(4.2,0),'M':(0,-1.9),'N':(4.2,-1.9),'P':(2.1,-3.8)}
import textwrap
for k_,(x,y) in pos7.items():
    t='\\\\'.join(textwrap.wrap(EV7[k_],28))
    o.append(f'\\node[box,minimum width=3.9cm,minimum height=1.45cm,font=\\footnotesize] at ({x},{y}) {{\\textbf{{{k_}}} \\ \\ {t}}};')
SK=tikz(o)
dz='P – L – K – M – N';
q('0007',tipId='pc-evren',tip=TIPLER['pc-evren'],z='orta',alt='Evrenin Zaman Çizelgesi',kaz='Büyük Patlama’dan sonraki evrenin evrelerini oluş sırasına dizer.',kalip='şekilli',
 metin='Büyük Patlama modeline göre evrenin ilk saniyelerinden ilk yıldızların oluşumuna kadar gerçekleşen beş olay şekilde K, L, M, N ve P harfleriyle gösterilmiştir. Kutuların şekildeki dizilişi zaman sırasını göstermemektedir.\nBuna göre bu olaylar zamanda ilkinden sonuncusuna doğru aşağıdakilerden hangisi gibi sıralanır?',
 sekil=SK,dogru=dz,yan=[('P – L – M – K – N','Nötr atomların oluşumunu helyum çekirdeklerinin oluşumundan önce koymuş; atom, çekirdek oluştuktan çok sonra, evren soğuyunca ortaya çıkar.','bilgi'),
  ('L – P – K – M – N','Proton ve nötronların oluşumunu kuark–gluon plazmasından önce koymuş; hadronlar plazma soğuyunca oluşur.','bilgi'),('P – L – K – N – M','Yıldızların oluşumunu nötr atomlardan önce koymuş; gaz bulutları atomlar oluştuktan sonra çöker.','bilgi'),
  ('K – P – L – M – N','Helyum çekirdeklerini ilk olay saymış; proton ve nötronlar olmadan çekirdek oluşamaz.','bilgi')],
 sira=['K – P – L – M – N','L – P – K – M – N','P – L – K – M – N','P – L – K – N – M','P – L – M – K – N'],istenen='Olayların zaman sırası.',
 ip=['Evren genişleyip soğudukça hangi yapıların kararlı kalabildiğini enerjiye göre sırala.'],bilgi=[EV],
 ad=[A('Plazma','Sıcaklık çok yüksekken kuark ve gluonlar serbesttir.','P ilk'),A('Hadronlar ve çekirdekler','Soğuyunca kuarklar proton–nötron, sonra çekirdek oluşturur.','L → K'),A('Atomlar ve yıldızlar','Ancak çok soğuyunca elektronlar bağlanır; gaz çöker.','M → N')],
 puf='Sıcaklık düştükçe önce kuarklar, sonra çekirdekler, sonra atomlar, en son yıldızlar bir araya gelir.')
# ===== 08 orta · kırmızıya kayma
card(8,'Kırmızıya kayma ve Hubble yasası','Dalga boyu artışı uzaklaşmayı gösterir; v = z × c ve v ∝ d ile hız oranı uzaklık oranına eşittir.','Dalga boyunun kısalmasını uzaklaşma sanmak; kaymayı yüzde olarak yanlış okumak.','zor','şekilli',3,'pc-kanit','üç gökadanın spektral çizgisi')
lab=600; gal={'A':612,'B':624,'C':648}
z={k_:Fr(v-lab,lab) for k_,v in gal.items()}; assert z['C']/z['A']==4 and z['B']==Fr(1,25)
x0=lambda l:(l-580)*.075
o=[]
rows=[('Laboratuvar',lab,0)]+[(f'{k_} gökadası',v,-1.25*(i+1)) for i,(k_,v) in enumerate(gal.items())]
for nm_,l,y in rows:
    o.append(f'\\draw[thick,fill=gray!12] ({x0(580):.2f},{y-.3}) rectangle ({x0(680):.2f},{y+.3});')
    o.append(f'\\draw[vurgu,very thick] ({x0(l):.2f},{y-.3}) -- ({x0(l):.2f},{y+.3});')
    o.append(f'\\node[font=\\footnotesize] at ({x0(l):.2f},{y+.58}) {{{l} nm}};'); o.append(f'\\node[left,font=\\footnotesize] at (-.15,{y}) {{{nm_}}};')
o.append(f'\\draw[thin,-{{Stealth}}] ({x0(580):.2f},-4.65) -- ({x0(680):.2f},-4.65) node[right,font=\\footnotesize] {{$\\lambda$}};')
SK=tikz(o)
truth8=[True,True,False]
assert 100*Fr(gal['B']-lab,lab)==4
q('0008',tipId='pc-kanit',tip=TIPLER['pc-kanit'],z='zor',alt='Kırmızıya Kayma',kaz='Gökada spektrumlarındaki kaymadan uzaklaşma hızını ve göreli uzaklığı yorumlar.',kalip='öncüllü',
 metin='Laboratuvarda dalga boyu 600 nm ölçülen bir spektral çizgi, A, B ve C gökadalarının spektrumlarında şekildeki dalga boylarında gözlenmiştir. Gökadaların hızları ışık hızından çok küçüktür ve Hubble yasası (hız uzaklıkla doğru orantılı) geçerlidir.\nBuna göre,\nI. A, B ve C gökadaları Dünya’dan uzaklaşmaktadır.\nII. C gökadası, A gökadasından 4 kat daha uzaktadır.\nIII. B gökadasının uzaklaşma hızı, ışık hızının %2’sidir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Her gökada için dalga boyundaki göreli değişimi bul; bu değişimin hız ve uzaklıkla ilişkisini düşün.'],bilgi=[HB],
 ad=[A('Kayma yönü','Gözlenen dalga boyları 600 nm’den büyüktür.','kırmızıya kayma → uzaklaşma → I doğru'),A('Uzaklık oranı','Hız kaymayla, uzaklık da hızla orantılıdır.','dC ÷ dA = 48 ÷ 12 = 4 → II doğru'),A('B’nin hızı','Hız, ışık hızının kayma oranı kadar kesridir.','Δλ ÷ λ₀ = 24 ÷ 600 = %4 → III yanlış')],
 puf='Δλ ÷ λ₀ oranı v ÷ c’ye eşittir; uzaklık oranı da hız oranı kadardır.',
 **onc(truth8,['dalga boyları artmıştır, yani gökadalar uzaklaşmaktadır','hız (dolayısıyla uzaklık) kayma miktarıyla orantılıdır, oran 48 ÷ 12 = 4’tür','B’nin kayma oranı 24 ÷ 600 = %4’tür'],3))
# ===== 09 orta · nükleosentez oranı
card(9,'Hidrojen/helyum çekirdek sayısı oranı','Kütle yüzdesini çekirdek kütlesine bölerek sayıyla orantılı değer bulunur.','Kütle oranını sayı oranı sanmak.','orta','grafik',3,'pc-nukleo','kütle yüzdelerinden sayı oranı')
mH,mHe=75,25; oran=Fr(mH,1)/Fr(mHe,4); assert oran==12
assert Fr(mH,mHe)==3 and Fr(mH,4)/Fr(mHe,1)==Fr(3,4) and Fr(mH,1)/Fr(mHe,2)==6 and Fr(mH,mHe)*4*4==48
o=['\\node[font=\\small] at (4,1.1) {Kütlece bolluk};',
 '\\draw[thick,fill=vurgu!18] (0,0) rectangle (6,.9); \\draw[thick,fill=vurgu!55] (6,0) rectangle (8,.9);','\\node at (3,.45) {Hidrojen: \\%75}; \\node at (7,.45) {Helyum: \\%25};']
for p_ in range(0,101,25): o.append(f'\\draw[thick] ({p_*.08},0) -- ({p_*.08},-.15) node[below,font=\\footnotesize] {{{p_}}};')
o.append('\\node[font=\\footnotesize] at (4,-.85) {kütle yüzdesi (\\%)};')
SK=tikz(o)
q('0009',tipId='pc-nukleo',tip=TIPLER['pc-nukleo'],z='orta',alt='Nükleosentez',kaz='Büyük Patlama çekirdek oluşumunda kütle yüzdelerinden çekirdek sayısı oranını hesaplar.',kalip='grafik',
 metin='Büyük Patlama’dan birkaç dakika sonra gerçekleşen çekirdek oluşumu sonunda, evrendeki maddenin kütlece bolluğu şekildeki gibi hidrojen ve helyum çekirdeklerinden oluşmaktadır. Bir hidrojen çekirdeğinin kütlesi 1 birim, bir helyum çekirdeğinin kütlesi 4 birim alınacaktır.\nBuna göre hidrojen çekirdeği sayısının helyum çekirdeği sayısına oranı kaçtır?',
 sekil=SK,dogru=12,yan=[(3,'Kütle oranını (75 ÷ 25) çekirdek sayısı oranı olarak yazmış.','bilgi'),(Fr(3,4),'Kütle yüzdelerini çekirdek kütlesiyle ters bölmüş: (75 ÷ 4) ÷ 25 = 0,75.','islem'),(6,'Helyum çekirdeğinin kütlesini 2 birim alarak 75 ÷ (25 ÷ 2) = 6 bulmuş.','islem'),(48,'Kütle oranını iki kez 4 ile çarpmış: 3 × 4 × 4 = 48.','islem')],
 istenen='N(H) ÷ N(He) oranı.',
 ip=['Bir elementin çekirdek sayısı, o elementin toplam kütlesinin tek çekirdeğin kütlesine bölünmesiyle bulunur.'],bilgi=[NK],
 ad=[A('Kütleleri oku','Yüzdeler 100 birimlik örnek için kütle gibi alınır.','H: 75 birim, He: 25 birim'),A('Sayıları bul','Sayı = toplam kütle ÷ çekirdek kütlesi.','N(H) = 75 ÷ 1 = 75; N(He) = 25 ÷ 4 = 6,25'),A('Oranla','Hidrojen sayısı helyum sayısına bölünür.','75 ÷ 6,25 = 12')],
 puf='Kütle yüzdesi sayı değildir; her elementin kütlesini çekirdek kütlesine bölüp sonra oranla.')
# ===== 10 orta · uuu
card(10,'Yüke göre kuark bileşimi','Üç kuarklı parçacığın yükünden kuark bileşimi bulunur; karşıt kuark yükleri zıttır.','Karşıt kuark yükünü işaretiyle karıştırmak.','orta','şekilli',3,'pc-kuark','yük verilir, kuark bileşimi istenir')
Q4={'u':UK,'d':DK,'ū':-UK,'d̄':-DK}
bil=lambda s:sum(Q4[k_] for k_ in s.split())
for s,v in {'u u u':2,'u u d':1,'d d d':-1,'ū ū ū':-2,'d̄ d̄ d̄':1}.items(): assert bil(s)==v,s
o=['\\filldraw[fill=vurgu!35,thick] (0,0) circle (.55) node {u};','\\node[align=center,font=\\small] at (0,-1.15) {yukarı kuark\\\\yük: $+2e/3$};',
 '\\filldraw[fill=vurgu!10,thick] (3.4,0) circle (.55) node {d};','\\node[align=center,font=\\small] at (3.4,-1.15) {aşağı kuark\\\\yük: $-e/3$};',
 '\\node[align=center,font=\\small] at (7.2,0) {Karşıt kuark: aynı kütle,\\\\zıt yük (örn. $\\bar{\\mathrm{u}}$: $-2e/3$)};']
SK=tikz(o)
q('0010',tipId='pc-kuark',tip=TIPLER['pc-kuark'],z='orta',alt='Baryon Yapısı',kaz='Yükü verilen üç kuarklı parçacığın kuark bileşimini belirler.',kalip='şekilli',
 metin='Şekilde bazı kuarkların yükleri ve karşıt kuarkın tanımı verilmiştir. Yapısı yalnızca bu kuarklardan ya da bunların karşıt kuarklarından oluşan, üç parçacıklı bir hadronun elektriksel yükü +2e’dir (e: elektronun yükünün büyüklüğü).\nBuna göre bu hadronun yapısında hangi kuarklar bulunur?',
 sekil=SK,dogru='u u u',yan=[('u u d','Protonun yapısını yazmış; bu bileşimin yükü +2e/3 + 2e/3 − e/3 = +e’dir.','bilgi'),('d d d','Yüklü olduğunu görüp aşağı kuarkları seçmiş; bu bileşimin yükü −e’dir.','dikkat'),
  ('ū ū ū','Karşıt yukarı kuarkın yük işaretini yanlış almış; bu bileşimin yükü −2e’dir.','dikkat'),('d̄ d̄ d̄','Karşıt aşağı kuarkı seçmiş; yükü +e/3 + e/3 + e/3 = +e olduğundan +2e’yi vermez.','islem')],
 sira=['u u u','u u d','d d d','ū ū ū','d̄ d̄ d̄'],istenen='Hadronun kuark bileşimi.',
 ip=['Her seçenekteki üç kuarkın yük toplamını yaz; karşıt kuarkın yükünün işaretine dikkat et.'],bilgi=[KU],
 ad=[A('Seçenek yüklerini bul','Her kuark için yük toplanır.','uuu: +2e; uud: +e; ddd: −e; ūūū: −2e; d̄d̄d̄: +e'),A('Karşılaştır','Yalnız bir bileşim +2e verir.','u u u'),A('Karşıt kuark kontrolü','Karşıt kuarklar zıt işaretli yük getirir.','ū ū ū: −2e olduğundan elenir')],
 puf='Yük +2e ise üçlü ancak üç yukarı kuarktır; karşıt kuark yüklerini işaretle birlikte hesapla.')
# ===== 11 orta · karşıt parçacık tablosu
card(11,'Parçacık–karşıt parçacık özellikleri','Karşıt parçacık aynı kütleli, zıt yüklü ve zıt baryon/lepton sayılıdır; nötr olması kendisiyle aynı olmasını gerektirmez.','Nötr parçacığın karşıtını kendisi sanmak.','orta','öncüllü',3,'pc-karsit','parçacık–karşıt parçacık çiftleri tablosu')
tb=[['Elektron','−e','0','+1'],['Pozitron','+e','0','−1'],['Proton','+e','+1','0'],['Antiproton','−e','−1','0'],['Nötron','0','+1','0'],['Antinötron','0','−1','0']]
SK=tablo_svg(['Parçacık','Elektriksel yük','Baryon sayısı','Lepton sayısı'],tb)
assert (-Fr(2,3)*2+Fr(1,3))==-1   # antiproton ū ū d̄ yükü
q('0011',tipId='pc-karsit',tip=TIPLER['pc-karsit'],z='orta',alt='Karşıt Parçacıklar',kaz='Parçacık ve karşıt parçacığın özelliklerini karşılaştırır.',kalip='öncüllü',
 metin='Tabloda, bazı parçacıklar ile karşıt parçacıklarının elektriksel yükü, baryon sayısı ve lepton sayısı verilmiştir (e: elektronun yükünün büyüklüğü).\nBuna göre,\nI. Antiprotonun yapısında iki yukarı kuark ve bir aşağı kuark bulunur.\nII. Elektron ile pozitronun kütleleri eşit, yükleri zıttır.\nIII. Antinötron, yüksüz olduğundan nötronla aynı parçacıktır.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Tablodaki işaretlerin parçacıktan karşıt parçacığa geçerken nasıl değiştiğine bak; kütle ve kuark yapısını karşıtlık ilişkisiyle düşün.'],bilgi=[KS,KU],
 ad=[A('I. yargı','Antiprotonun yükü −e olmalıdır; iki yukarı ve bir aşağı kuark +e verir.','antiproton: ū ū d̄ → −e → I yanlış'),A('II. yargı','Karşıt parçacığın kütlesi aynı, yükü zıttır.','m(e⁻) = m(e⁺); yükler −e ve +e → II doğru'),A('III. yargı','Nötr olsa da baryon sayısı zıttır.','+1 ≠ −1 → farklı parçacıklar → III yanlış')],
 puf='Karşıt parçacık: aynı kütle, zıt yük, zıt baryon/lepton sayısı; nötr parçacıkta baryon sayısı farkı yine ayırt eder.',
 **onc([False,True,False],['antiprotonun yapısında iki karşıt yukarı kuark ve bir karşıt aşağı kuark bulunur (yük −e)','karşıt parçacığın kütlesi eşit, yükü zıttır','nötronun baryon sayısı +1, antinötronunki −1’dir; ikisi farklı parçacıklardır'],0))
# ===== 12 orta · şiddet-menzil grafiği
card(12,'Kuvvetleri şiddet ve menzilden tanıma','Göreli şiddet sırası güçlü > elektromanyetik > zayıf > kütle çekimi; güçlü ve zayıf menzilli kısadır.','Gluon–foton eşleşmesini ters kurmak; zayıf kuvvetin menzilini sonsuz sanmak.','orta','grafik',3,'pc-kuvvet','dört kuvvetin log şiddet–menzil grafiği')
ls={'K':0,'L':-2,'M':-6,'N':-39}; mz={'K':'$10^{-15}$ m','L':'sonsuz','M':'$10^{-18}$ m','N':'sonsuz'}
o=['\\draw[thick,-{Stealth}] (0,0) -- (0,-4.5);','\\node[font=\\footnotesize,rotate=90] at (-1.25,-2) {$\\log_{10}$ (göreli şiddet)};','\\draw[thick] (-.05,0) -- (5.2,0);']
for t in (0,-10,-20,-30,-40): o.append(f'\\draw (0,{t*.1}) -- (-.12,{t*.1}) node[left,font=\\footnotesize] {{${t}$}};')
for i,(k_,v) in enumerate(ls.items()):
    x=.9+1.25*i; o.append(f'\\draw[very thick,vurgu] ({x},0) -- ({x},{v*.1}); \\filldraw[vurgu] ({x},{v*.1}) circle (.09);')
    o.append(f'\\node[font=\\small] at ({x},.85) {{\\textbf{{{k_}}}}}; \\node[font=\\scriptsize,align=center] at ({x},.35) {{{mz[k_]}}};')
o.append('\\node[font=\\scriptsize,anchor=east] at (-.35,.35) {menzil};')
SK=tikz(o)
q('0012',tipId='pc-kuvvet',tip=TIPLER['pc-kuvvet'],z='orta',alt='Kuvvetlerin Karşılaştırılması',kaz='Dört temel kuvveti göreli şiddet ve menzillerine göre ayırt eder.',kalip='grafik',
 metin='Şekilde, dört temel kuvvetin (K, L, M ve N) göreli şiddetlerinin 10 tabanındaki logaritması ve menzilleri gösterilmiştir. Kuvvetlerin hangisinin hangi temel kuvvet olduğu belirtilmemiştir.\nBuna göre,\nI. K kuvvetinin aracı parçacığı fotondur.\nII. M kuvvetinin menzili L kuvvetinin menzilinden büyüktür.\nIII. Gezegenlerin Güneş çevresindeki hareketinden sorumlu kuvvet N’dir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Şiddeti ve menzili sıralayarak her harfin hangi temel kuvvete karşılık geldiğini önce belirle.'],bilgi=[KV],
 ad=[A('Kuvvetleri tanı','En şiddetli ve kısa menzilli K güçlü kuvvettir; menzili sonsuz L elektromanyetik, kısa menzilli M zayıf, en zayıf N kütle çekimidir.','K: güçlü; L: elektromanyetik; M: zayıf; N: kütle çekimi'),
     A('I ve II','Güçlü kuvvetin aracısı gluondur; zayıf kuvvetin menzili kısadır.','K: gluon → I yanlış; M: 10⁻¹⁸ m < sonsuz → II yanlış'),A('III','Yıldız–gezegen sisteminde yüksüz cisimler arasında kütle çekimi etkilidir.','N → III doğru')],
 puf='Şiddet ve menzil birlikte kuvveti tanıtır: güçlü (en şiddetli, kısa), elektromanyetik (sonsuz), zayıf (kısa), kütle çekimi (en zayıf, sonsuz).',
 **onc([False,False,True],['güçlü kuvvetin aracı parçacığı gluondur, foton elektromanyetik kuvvetin taşıyıcısıdır','zayıf kuvvetin menzili kısadır, elektromanyetik kuvvetinki sonsuzdur','gezegenlerin hareketinden kütle çekim kuvveti sorumludur'],1))
# ===== 13 orta · parçacık–kuvvet tablosu
card(13,'Parçacıkların etkilendiği kuvvetler','Yüklü leptonlar elektromanyetik ve zayıf, nötrinolar yalnız zayıf; kuark içerenler güçlü kuvvetten de etkilenir.','Yüksüz hadronu güçlü kuvvetten etkilenmez sanmak.','orta','tablo',3,'pc-kuvvet','dört madde parçacığının etkileşimleri')
SK=tablo_svg(['Parçacık','Elektriksel yük','Yapısında kuark'],[['P₁','−e','Yok'],['P₂','0','Yok'],['P₃','+e','Var'],['P₄','0','Var']])
q('0013',tipId='pc-kuvvet',tip=TIPLER['pc-kuvvet'],z='orta',alt='Etkileşim Türleri',kaz='Madde parçacıklarının yük ve kuark içeriğine göre etkilendiği kuvvetleri belirler.',kalip='öncüllü',
 metin='Tabloda, madde parçacığı (fermiyon) olan P₁, P₂, P₃ ve P₄ parçacıklarının elektriksel yükü ve yapısında kuark bulunup bulunmadığı verilmiştir (e: elektronun yükünün büyüklüğü).\nBuna göre,\nI. P₁ elektromanyetik kuvvetten etkilenir, güçlü kuvvetten etkilenmez.\nII. P₂ elektromanyetik ve güçlü kuvvetten etkilenmez.\nIII. P₄ yüksüz olmasına rağmen güçlü kuvvetten etkilenir.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Yükü ve kuark içeriğini hangi kuvvetlerin ilgilendirdiğini ayrı ayrı düşün.'],bilgi=[KV,SN],
 ad=[A('P₁','Yüklü, kuarksız madde parçacığı leptondur.','elektromanyetik evet; güçlü hayır → I doğru'),A('P₂','Yüksüz leptondur (nötrino).','elektromanyetik ve güçlü yok → II doğru'),A('P₄','Kuark içeren hadrondur.','güçlü kuvvet etkisinde → III doğru')],
 puf='Güçlü kuvvet yükle değil, kuark içeriğiyle ilgilidir; elektromanyetik kuvvet yükle ilgilidir.',
 **onc([True,True,True],['yüklü bir leptondur: elektromanyetik kuvvetten etkilenir, güçlü kuvvetten etkilenmez','yüksüz bir leptondur: ne elektromanyetik ne güçlü kuvvetten etkilenir','kuark içerdiğinden yüksüz olsa da güçlü kuvvetten etkilenir'],4))
# ===== 14 orta · foton değişimi diyagramı
card(14,'Elektronlar arası etkileşimin aracısı','Aynı yüklü iki elektronun itmesi foton değişimiyle olur; foton kütlesiz, yüksüzdür, menzil sonsuzdur.','Aracı parçacığı yüklü ya da kısa menzilli sanmak.','orta','şekilli',3,'pc-kuvvet','iki elektron ve aracı parçacık diyagramı')
o=['\\draw[thick,-{Stealth}] (0,0) -- (1.5,1.2); \\draw[thick] (1.5,1.2) -- (2.4,1.9); \\draw[thick,-{Stealth}] (2.4,1.9) -- (3.5,1.9);','\\node[left] at (0,0) {$e^-$};',
 '\\draw[thick,-{Stealth}] (0,3.8) -- (1.5,2.8); \\draw[thick] (1.5,2.8) -- (2.4,2.1); \\draw[thick,-{Stealth}] (2.4,2.1) -- (3.5,2.1);','\\node[left] at (0,3.8) {$e^-$};','\\node[right] at (3.5,2) {};']
o=['\\draw[thick,-{Stealth}] (0,0) -- (1.2,.9); \\draw[thick] (1.2,.9) -- (1.8,1.4) coordinate (A1); \\draw[thick,-{Stealth}] (1.8,1.4) -- (3.1,.55) node[right] {$e^-$};','\\node[left] at (0,0) {$e^-$};',
 '\\draw[thick,-{Stealth}] (0,3.4) -- (1.2,2.5); \\draw[thick] (1.2,2.5) -- (1.8,2.1) coordinate (A2); \\draw[thick,-{Stealth}] (1.8,2.1) -- (3.1,2.95) node[right] {$e^-$};','\\node[left] at (0,3.4) {$e^-$};',
 '\\draw[wav] (A1) -- (A2);','\\node[right] at (1.9,1.75) {X};']
SK=tikz(o)
q('0014',tipId='pc-kuvvet',tip=TIPLER['pc-kuvvet'],z='orta',alt='Aracı Parçacıklar',kaz='Elektronlar arasındaki itme etkileşiminin aracı parçacığını ve özelliklerini belirler.',kalip='öncüllü',
 metin='Şekilde, birbirine yaklaşan iki elektronun elektriksel itme etkileşimi, X aracı parçacığının değiş tokuşuyla gösterilmiştir. Etkileşimden sonra elektronlar birbirinden uzaklaşmıştır.\nBuna göre,\nI. X parçacığının durgun kütlesi sıfırdır.\nII. X parçacığı elektriksel olarak yüklüdür.\nIII. Bu etkileşimin menzili sınırlıdır.\nyargılarından hangileri doğrudur?',
 sekil=SK,istenen='Doğru yargılar.',
 ip=['Elektriksel itmeyi taşıyan aracı parçacığın hangisi olduğunu, yükünü ve menzilini düşün.'],bilgi=[KV],
 ad=[A('X’i belirle','Elektriksel itme elektromanyetik etkileşimdir.','X: foton'),A('Kütle ve yük','Foton kütlesiz ve yüksüzdür.','m = 0 → I doğru; yük = 0 → II yanlış'),A('Menzil','Elektromanyetik kuvvetin menzili sonsuzdur.','III yanlış')],
 puf='Elektriksel etkileşimin aracısı fotondur: kütlesiz, yüksüz, sonsuz menzilli.',
 **onc([True,False,False],['aracı parçacık fotondur ve durgun kütlesi sıfırdır','foton yüksüzdür','elektromanyetik etkileşimin menzili sonsuzdur'],0))
# ===== 15 zor · çift oluşumu
card(15,'Çift oluşumunda kinetik enerji','Foton enerjisi önce iki parçacığın kütle enerjisine harcanır, kalan enerji kinetik enerji olarak paylaşılır.','Kütle enerjisini düşmeyi unutmak ya da tek parçacığınkini düşmek.','zor','şekilli',3,'pc-karsit','çift oluşumunda parçacık başına kinetik enerji')
Eph,m0=Fr(202,100),Fr(51,100); Ek=(Eph-2*m0)/2; assert Ek==Fr(1,2)
assert Eph/2==Fr(101,100) and Eph-2*m0==1 and Eph-m0==Fr(151,100) and Ek/2==Fr(1,4)
o=['\\foreach \\i in {1,...,3}{\\foreach \\j in {0,...,4}{\\node[gray,font=\\tiny] at (\\i*.95+.1,\\j*.95-1.9) {$\\times$};}}',
 '\\draw[thick,dashed] (-1.1,0) -- (0,0); \\node[above] at (-.7,.05) {$\\gamma$};','\\node[font=\\small,align=center] at (-1.2,.75) {$E=2{,}02$ MeV};',
 '\\draw[very thick,vurgu] (0,0) to[bend left=38] (3.6,2.2); \\node[right] at (3.6,2.2) {$e^+$};','\\draw[very thick,vurgu] (0,0) to[bend right=38] (3.6,-2.2); \\node[right] at (3.6,-2.2) {$e^-$};',
 '\\node[font=\\scriptsize,align=center] at (6.1,0) {her biri için\\\\$mc^2=0{,}51$ MeV\\\\$\\times$: sayfaya dik\\\\içeri manyetik alan};']
SK=tikz(o)
q('0015',tipId='pc-karsit',tip=TIPLER['pc-karsit'],z='zor',alt='Çift Oluşumu',kaz='Foton enerjisinden oluşan parçacık–karşıt parçacık çiftinin kinetik enerjisini hesaplar.',kalip='şekilli',
 metin='Şekilde, enerjisi 2,02 MeV olan bir fotonun ağır bir çekirdeğin yakınında bir elektron–pozitron çifti oluşturması ve çiftin manyetik alandaki izleri gösterilmiştir. Çekirdeğin aldığı enerji ihmal edilecektir ve elektron ile pozitron eşit büyüklükte kinetik enerjiyle ayrılmaktadır. Her birinin durgun kütle enerjisi şekilde verilmiştir.\nBuna göre elektronun kinetik enerjisi kaç MeV’dir?',
 sekil=SK,dogru=Fr(1,2),yan=[(Fr(1,4),'Kalan kinetik enerjiyi iki kez ikiye bölmüş: 1,00 ÷ 2 ÷ 2 = 0,25.','islem'),(1,'Kalan kinetik enerjiyi (2,02 − 1,02 = 1,00) iki parçacık arasında paylaştırmamış.','dikkat'),
  (Fr(101,100),'Foton enerjisini kütle enerjisi düşmeden ikiye bölmüş: 2,02 ÷ 2 = 1,01.','bilgi'),(Fr(151,100),'Yalnız bir parçacığın kütle enerjisini düşmüş: 2,02 − 0,51 = 1,51.','dikkat')],
 istenen='Elektronun kinetik enerjisi (MeV).',
 ip=['Foton enerjisinin hangi kısmının yeni parçacıkların varlığına harcandığını, geri kalanın nasıl dağıldığını düşün.'],bilgi=[KS],
 ad=[A('Kütle enerjisi','Çiftin oluşması için iki parçacığın kütle enerjisi gerekir.','2 × 0,51 = 1,02 MeV'),A('Kalan enerji','Foton enerjisinden kütle enerjisi çıkarılır.','2,02 − 1,02 = 1,00 MeV'),A('Paylaştır','İki parçacığın kinetik enerjileri eşittir.','Ek = 1,00 ÷ 2 = 0,50 MeV')],
 puf='Çift oluşumunda E(foton) = 2mc² + Ek(e⁻) + Ek(e⁺); önce kütle enerjisi ayrılır, kalan eşit pay edilir.')
# ===== 16 orta · soğuma ve ölçek
card(16,'Soğuma ile ölçek ilişkisi','Işınımın sıcaklığı ölçekle ters orantılıdır; sıcaklık oranı ölçek oranını verir.','Oranı ters almak.','orta','şekilli',3,'pc-evren','iki sıcaklıktan genişleme katsayısı')
T1,T2=3000,3; kat=Fr(T1,T2); assert kat==1000 and Fr(T2,T1)==Fr(1,1000) and T1-T2==2997
o=['\\draw[thick,-{Stealth}] (-.2,0) -- (9.6,0);']
for x,t1,t2 in [(0,'Çekirdeklerin oluşumu','$t\\approx3$ dk\\\\$T\\approx10^{9}$ K'),(4.2,'Atomların oluşumu','$t\\approx380\\,000$ yıl\\\\$T\\approx3000$ K'),(8.0,'Bugün','$t\\approx13{,}8$ milyar yıl\\\\$T\\approx3$ K')]:
    o.append(f'\\filldraw[vurgu] ({x},0) circle (.1);'); o.append(f'\\node[above,font=\\footnotesize,align=center] at ({x},.2) {{\\textbf{{{t1}}}}};'); o.append(f'\\node[below,font=\\footnotesize,align=center] at ({x},-.2) {{{t2}}};')
SK=tikz(o)
q('0016',tipId='pc-evren',tip=TIPLER['pc-evren'],z='orta',alt='Genişleme ve Soğuma',kaz='Evrenin genişlemesi sırasında ışınım sıcaklığı ile ölçek ilişkisini kullanır.',kalip='şekilli',
 metin='Evren genişlerken içindeki ışınımın sıcaklığı, evrenin ölçeği (uzaklıkların büyüklüğü) ile ters orantılı olarak azalır. Şekilde evrenin bazı dönemlerindeki yaşı ve ışınım sıcaklığı yaklaşık değerleriyle verilmiştir. Atomların oluştuğu dönemde iki gökada arasındaki uzaklık d₀’dır.\nBuna göre bu iki gökada arasındaki uzaklık bugün kaç d₀’dır?',
 sekil=SK,dogru=1000,yan=[(Fr(1,1000),'Sıcaklık oranını ters almış: 3 ÷ 3000 = 0,001.','islem'),(3,'Yalnız bugünkü sıcaklığı (3 K) uzaklık katı olarak almış.','dikkat'),(2997,'Sıcaklıkların farkını almış: 3000 − 3 = 2997.','islem'),(3000,'Yalnız atomların oluştuğu dönemdeki sıcaklığı (3000 K) uzaklık katı olarak almış.','dikkat')],
 istenen='Bugünkü uzaklığın d₀’a oranı.',
 ip=['Ters orantı kurulunca, sıcaklık oranının ölçek oranına nasıl karşılık geldiğini yaz.'],bilgi=[EV],
 ad=[A('Ters orantı','Sıcaklık ölçekle ters orantılıdır.','T × d = sabit'),A('Veriyi yerleştir','Atom dönemi ve bugünün değerleri kullanılır.','3000 × d₀ = 3 × d'),A('Çöz','Bugünkü uzaklık bulunur.','d = 1000 d₀')],
 puf='Ters orantılı büyüklüklerde çarpım sabittir: sıcaklık kaç kat düştüyse ölçek o kadar kat artmıştır.')
# ===== 17 zor · evrenin yaşı
card(17,'Hubble grafiğinden evrenin yaşı','Sabit hızla uzaklaşan gökadalar için t = d ÷ v = 1 ÷ H; birimleri km, s ve yıla çevirerek yaş bulunur.','Birim çevirme hataları.','zor','grafik',4,'pc-kanit','v–d grafiğinden yaş')
Hh=Fr(80); Mpc=3*10**19; yil=3*10**7
t=Fr(Mpc,1)/Hh/yil; assert t==Fr(125,10)*10**9  # 1,25e10 yıl
tg=t/10**9; assert tg==Fr(25,2)
assert tg*10==125 and tg/10==Fr(5,4) and tg*2==25 and tg/2==Fr(25,4)
SK=tikz_svg(r'''\begin{tikzpicture}\begin{axis}[width=7.6cm,height=5.6cm,xmin=0,xmax=200,ymin=0,ymax=16000,xtick={0,50,100,150,200},ytick={0,4000,8000,12000,16000},grid=both,minor tick num=0,xlabel={$d$ (Mpc)},ylabel={$v$ (km/s)},tick label style={font=\footnotesize},label style={font=\small},scaled ticks=false,/pgf/number format/.cd,1000 sep={}]
\addplot[thick,mark=none,vurgu!60,dashed] coordinates{(0,0)(200,16000)};
\addplot[only marks,mark=*,mark size=2.4pt,vurgu] coordinates{(50,4000)(100,8000)(150,12000)};
\end{axis}\end{tikzpicture}''')
q('0017',tipId='pc-kanit',tip=TIPLER['pc-kanit'],z='zor',alt='Evrenin Yaşı',kaz='Hubble grafiğinden evrenin yaşını yaklaşık olarak hesaplar.',kalip='grafik',
 metin='Şekilde, bazı gökadaların Dünya’ya uzaklıkları (d) ve Dünya’dan uzaklaşma hızları (v) gösterilmiştir. Evrendeki bütün gökadaların Büyük Patlama anından beri sabit hızla uzaklaştığı ve hızın uzaklıkla doğru orantılı olduğu varsayılacaktır (1 Mpc = 3 × 10¹⁹ km, 1 yıl = 3 × 10⁷ s).\nBuna göre evrenin yaşı yaklaşık kaç milyar yıldır?',
 sekil=SK,dogru=Fr(25,2),yan=[(Fr(5,4),'Yılı 3 × 10⁸ s almış; saniye cinsinden yaşı yıla çevirirken sonucu on kat küçültmüş.','islem'),(Fr(25,4),'Uzaklığı yarıya indirip t = d ÷ (2v) kullanmış.','islem'),(25,'Hızı yarıya indirip t = 2d ÷ v kullanmış (ortalama hız v ÷ 2 sanmış).','bilgi'),(125,'Yılı 3 × 10⁶ s almış; saniye cinsinden yaşı yıla çevirirken sonucu on kat büyütmüş.','islem')],
 istenen='Evrenin yaşı (milyar yıl).',
 ip=['Doğru orantının eğiminden hız–uzaklık oranını bul; sabit hızla gelen bir gökada için geçen süreyi bu oranla ilişkilendir.'],bilgi=[HB],
 ad=[A('Eğimi oku','Grafikten d = 100 Mpc için v okunur.','H = 8000 ÷ 100 = 80 km/s/Mpc'),A('Süreyi yaz','Sabit hızla uzaklaşan için t = d ÷ v = 1 ÷ H.','t = 3 × 10¹⁹ ÷ 80 s = 3,75 × 10¹⁷ s'),A('Yıla çevir','Saniyeyi yıla bölerek çevir.','t = 3,75 × 10¹⁷ ÷ (3 × 10⁷) = 1,25 × 10¹⁰ yıl'),A('Milyar yıla çevir','10⁹ yıl bir milyar yıldır.','t = 12,5 milyar yıl')],
 puf='Hubble sabitinin tersi (1 ÷ H) evrenin yaşı mertebesindedir; km, Mpc ve yıl birimlerini çevirmeyi unutma.')
# ===== 18 zor · tepkimeler
card(18,'Korunum yasalarına göre tepkime seçimi','Yük, baryon ve lepton sayısı korunan tepkime gerçekleşebilir; karşıt parçacık işareti ters alınır.','Karşıt parçacığın baryon sayısını +1 almak.','zor','öncüllü',4,'pc-tepkime','üç tepkimede korunum denetimi')
PP={'p':(1,1,0),'p̄':(-1,-1,0),'e⁻':(-1,0,1),'e⁺':(1,0,-1),'γ':(0,0,0)}
def topl(L): return tuple(sum(PP[x][i] for x in L) for i in range(3))
assert topl(['p'])!=topl(['e⁺','γ']) and topl(['e⁻','e⁺'])==topl(['γ','γ']) and topl(['p','p'])==topl(['p','p','p','p̄'])
SK=tablo_svg(['Tepkime','Denklem'],[['I','p → e⁺ + γ'],['II','e⁻ + e⁺ → γ + γ'],['III','p + p → p + p + p + p̄']])
q('0018',tipId='pc-tepkime',tip=TIPLER['pc-tepkime'],z='zor',alt='Korunum Yasaları',kaz='Tepkimelerde yük, baryon ve lepton sayısı korunumunu denetler.',kalip='öncüllü',
 metin='Tabloda üç tepkime verilmiştir (p: proton, p̄: karşıt proton, e⁻: elektron, e⁺: pozitron, γ: foton). Tepkimelerde enerji koşulunun sağlandığı kabul edilecektir.\nBuna göre bu tepkimelerden hangileri, toplam yük, toplam baryon sayısı ve toplam lepton sayısının korunumu bakımından gerçekleşebilir?',
 sekil=SK,istenen='Gerçekleşebilen tepkimeler.',
 ip=['Her tepkimenin iki yanı için üç niceliği ayrı ayrı topla; karşıt parçacıkların işaretini ters al.'],bilgi=[KO,KS],
 ad=[A('I. tepkime','Soldaki baryon sayısı +1’dir, sağdaki sıfırdır.','B: +1 → 0; yük +1 → +1; L: 0 → −1 → I gerçekleşmez'),A('II. tepkime','Elektron–pozitron çifti yok olur.','Q: 0 → 0; B: 0 → 0; L: +1 − 1 = 0 → II gerçekleşir'),A('III. tepkime','Üç proton ve bir karşıt proton oluşur.','Q: +2 → +3 − 1 = +2; B: +2 → +3 − 1 = +2; L: 0 → 0 → III gerçekleşir')],
 puf='Üç niceliği tepkimenin her iki yanında ayrı ayrı topla; karşıt parçacık için yükü, baryon ve lepton sayısını ters al.',
 **onc([False,True,True],['protonun baryon sayısı +1’dir; sağ tarafta baryon sayısı sıfırdır ve lepton sayısı da korunmaz','elektron–pozitron çiftinin yük, baryon ve lepton sayısı toplamı sıfırdır; iki fotonla uyumludur','iki proton, üç proton ve bir karşıt protona dönüşürken yük ve baryon sayısı +2 olarak korunur'],3))
# ===== 19 orta · X parçacığı
card(19,'Tepkimeden bilinmeyen parçacık','Yük, baryon ve lepton sayısı korunumu bilinmeyen ürünü adayları ayıklayarak belirler.','Yalnız yüke bakmak.','orta','tablo',3,'pc-tepkime','tabloda adaylar; bilinmeyen X')
PT={'Elektron (e⁻)':(-1,0,1),'Pozitron (e⁺)':(1,0,-1),'Karşıt elektron nötrinosu':(0,0,-1),'Pion (π⁻)':(-1,0,0),'Karşıt proton (p̄)':(-1,-1,0)}
nec=(-1,0,1); ok_=[k_ for k_,v in PT.items() if v==nec]; assert ok_==['Elektron (e⁻)']
assert [k_ for k_,v in PT.items() if v[0]==-1]==['Elektron (e⁻)','Pion (π⁻)','Karşıt proton (p̄)'] and PT['Pion (π⁻)'][1:]==(0,0) and PT['Karşıt proton (p̄)'][1]==-1
SK=tablo_svg(['Parçacık','Yük','Baryon sayısı','Lepton sayısı'],[[k_,'+e' if v[0]==1 else '−e' if v[0]==-1 else '0',('+' if v[1]>0 else '−' if v[1]<0 else '')+str(abs(v[1])),('+' if v[2]>0 else '−' if v[2]<0 else '')+str(abs(v[2]) )] for k_,v in PT.items()])
q('0019',tipId='pc-tepkime',tip=TIPLER['pc-tepkime'],z='orta',alt='Bilinmeyen Ürün',kaz='Korunum yasalarını kullanarak tepkimedeki bilinmeyen parçacığı bulur.',kalip='tablo',
 metin='Bir nötron ile bir elektron nötrinosunun çarpışmasıyla bir proton ve X parçacığı oluşmaktadır. Tabloda X için aday olan beş parçacığın yükü, baryon sayısı ve lepton sayısı verilmiştir. (Nötron: yük 0, baryon sayısı +1, lepton sayısı 0; proton: yük +e, baryon sayısı +1, lepton sayısı 0; elektron nötrinosu: yük 0, baryon sayısı 0, lepton sayısı +1.)\nBuna göre X parçacığı hangisidir?',
 sekil=SK,dogru='Elektron (e⁻)',yan=[('Pozitron (e⁺)','Yük korunumunu sağlamamış; pozitron +e yüklüdür, ürünlerin toplam yükü +2e olur.','bilgi'),('Karşıt elektron nötrinosu','Yük korunumunu sağlamamış; yüksüz parçacık eklenince ürünlerin toplam yükü +e kalır, oysa girenler yüksüzdür.','bilgi'),
  ('Pion (π⁻)','Yük ve baryon sayısına bakıp lepton sayısını denetlememiş; pionun lepton sayısı sıfırdır, girenlerin toplamı +1’dir.','dikkat'),('Karşıt proton (p̄)','Yeni oluşan parçacığın yükünü doğru bulup baryon sayısını denetlememiş; karşıt protonla sağ taraftaki baryon sayısı 1 − 1 = 0 olur, oysa soldaki +1’dir.','dikkat')],
 sira=['Pozitron (e⁺)','Elektron (e⁻)','Karşıt elektron nötrinosu','Pion (π⁻)','Karşıt proton (p̄)'],istenen='X parçacığı.',
 ip=['Girenlerin ve çıkanların yük, baryon sayısı ve lepton sayısı toplamını eşitleyerek X için gereken üç değeri bul.'],bilgi=[KO],
 ad=[A('Girenlerin toplamı','Nötron ve nötrinonun değerleri toplanır.','Q = 0; B = +1; L = +1'),A('X için gerekenler','Proton +e, +1, 0 getirir; X bunları tamamlar.','X: Q = −e; B = 0; L = +1'),A('Tabloda ara','Üç değeri birden sağlayan tek parçacık seçilir.','X: elektron')],
 puf='Bilinmeyen ürünü bulmak için sol toplamdan bilinen ürünleri çıkar; çıkan üçlüyü tabloda ara.')
# ===== 20 zor · sıcaklık ve çift oluşumu
card(20,'Sıcaklığa göre çift oluşum eşiği','Çift oluşumu için ortalama foton enerjisi iki parçacığın kütle enerjisi toplamına ulaşmalıdır.','Tek parçacığın kütle enerjisini eşik saymak.','zor','tablo',4,'pc-evren','sıcaklık–enerji tablosunda eşik karşılaştırması')
Tt=[(14,Fr(8600)),(13,Fr(860)),(12,Fr(86)),(11,Fr(86,10)),(10,Fr(86,100)),(9,Fr(86,1000))]
me,mp=Fr(51,100),Fr(938)
def sel(ee,pp): return tuple(e for e,E in Tt if E>=2*ee and E<2*pp) if pp else None
ans=tuple(e for e,E in Tt if E>=2*me and E<2*mp); assert ans==(13,12,11)
Sb=lambda s:'; '.join(f'10{chr(0x2070+0) if False else ""}'+'' for _ in [])
def fmt20(s): return ', '.join(f'10^{x} K'.replace('^1','¹').replace('^9','⁹') for x in s)
sup={9:'⁹',10:'¹⁰',11:'¹¹',12:'¹²',13:'¹³',14:'¹⁴'}
fs=lambda s:' ve '.join([', '.join(f'10{sup[x]} K' for x in s[:-1]),f'10{sup[s[-1]]} K']) if len(s)>1 else f'10{sup[s[0]]} K'
alt_e=tuple(e for e,E in Tt if E>=2*me)  # pp̄ koşulunu unutan
alt_c=tuple(e for e,E in Tt if E>=me and E<2*mp)
alt_p=tuple(e for e,E in Tt if E>=2*mp)
alt_n=tuple(e for e,E in Tt if E<2*me)
assert alt_e==(14,13,12,11) and alt_c==(13,12,11,10) and alt_p==(14,) and alt_n==(10,9)
SK=tablo_svg(['Sıcaklık (K)','Ortalama foton enerjisi (MeV)'],[[f'10{sup[e]}',str(E).replace('.',',') if E.denominator==1 else ('%g'%float(E)).replace('.',',')] for e,E in Tt])
q('0020',tipId='pc-evren',tip=TIPLER['pc-evren'],z='zor',alt='Evrenin İlk Anları',kaz='Evrenin sıcaklığına göre hangi parçacık çiftlerinin oluşabileceğini belirler.',kalip='tablo',
 metin='Büyük Patlama’dan sonra evren soğurken, ışınımdaki fotonların ortalama enerjisinin iki parçacığın durgun kütle enerjileri toplamına ulaşması hâlinde o parçacık–karşıt parçacık çifti oluşabilir. Tabloda evrenin bazı sıcaklıklarındaki ortalama foton enerjisi verilmiştir. Elektronun durgun kütle enerjisi 0,51 MeV, protonunki 938 MeV’dir.\nBuna göre evrenin hangi sıcaklıklarında elektron–pozitron çifti oluşabilirken proton–karşıt proton çifti oluşamaz?',
 sekil=SK,dogru=fs(ans),yan=[(fs(alt_e),'Proton–karşıt proton çifti için eşiği denetlememiş; 10¹⁴ K’de ortalama foton enerjisi 1876 MeV’ten büyüktür ve bu çift de oluşabilir.','dikkat'),(fs(alt_c),'Elektron–pozitron eşiği için yalnız bir elektronun kütle enerjisini (0,51 MeV) almış; çift için 1,02 MeV gerekir.','bilgi'),
  (fs(alt_p),'Proton–karşıt proton çiftinin oluşabildiği sıcaklığı seçmiş; sorulan, bu çiftin oluşamadığı sıcaklıklardır.','dikkat'),(fs(alt_n),'Foton enerjisi eşiğin altında kalan sıcaklıkları seçmiş; bu sıcaklıklarda elektron–pozitron çifti de oluşamaz.','bilgi')],
 sira=[fs(alt_e),fs(alt_c),fs(alt_p),fs(alt_n),fs(ans)],istenen='İstenen sıcaklıklar.',
 ip=['Her çift için eşik enerjisini iki parçacığın kütle enerjisi toplamı olarak yaz ve tablodaki değerlerle karşılaştır.'],bilgi=[KS,EV],
 ad=[A('Eşikler','Çift oluşumu için iki parçacığın kütle enerjisi gerekir.','e⁻e⁺: 2 × 0,51 = 1,02 MeV; pp̄: 2 × 938 = 1876 MeV'),A('Elektron çifti','Ortalama enerjisi 1,02 MeV veya fazlası olan sıcaklıklar.','10¹⁴, 10¹³, 10¹², 10¹¹ K'),A('Proton çifti oluşamayan','Ortalama enerjisi 1876 MeV’in altında olanlar.','10¹³ K ve altı'),A('Kesişim','Her iki koşulu sağlayan sıcaklıklar.','10¹³, 10¹² ve 10¹¹ K')],
 puf='Çift oluşumunda eşik 2mc²’dir; iki eşik arasında kalan sıcaklık aralığını tablodan işaretle.')
# ===== yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/parcacik'
P.yaz(os.path.join(GD,'parcacik-1.json'),os.path.join(SC,'bos-parcacik.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='afiz|Büyük Patlama ve Parçacık Fiziği'))['kartlar'].append(c['id'])
json.dump(dict(konu='Büyük Patlama ve Parçacık Fiziği',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2022–2026 Fizik (yalnız mantık), 345 AYT Fizik, Bilgi Sarmal AYT Fizik, MEB 12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afparcacik.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
