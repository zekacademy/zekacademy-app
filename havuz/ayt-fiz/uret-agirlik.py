"""AYT Fizik · Kütle ve Ağırlık Merkezi · 20 soru (kardeş yok, ipucu 1). Şekiller ve cevaplar aynı veriden (Fraction) üretilir."""
import sys,os,json,math
HV='/home/claude/zekacademy-app/havuz'
sys.path.insert(0,HV); sys.path.insert(0,HV+'/tyt-fiz')
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from fractions import Fraction as Fr
import itertools,random
P=Parti('agirlik','Kütle ve Ağırlık Merkezi','afiz|Kütle ve Ağırlık Merkezi',ders='AYT Fizik',idon='aytfiz')
KONU='Kütle ve Ağırlık Merkezi'; H.KONU=KONU
TIPK={}
KAYNAK='ÖSYM AYT Fizik 2018–2025 (yalnız mantık) · 345 AYT Fizik Soru Bankası · Bilgi Sarmal AYT Fizik'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK); TIPK[tipId]=P.k
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def v(x): return fm(x)
# ---------- ağırlık merkezi hesapları ----------
def cm(cells):
    n=len(cells); return (Fr(sum(2*i+1 for i,j in cells),2*n),Fr(sum(2*j+1 for i,j in cells),2*n))
def rect(x0,y0,x1,y1): return {(i,j) for i in range(x0,x1) for j in range(y0,y1)}
def wcm(items):  # (kütle,(x,y))
    M=sum(m for m,_ in items); return (sum(m*p[0] for m,p in items)/M,sum(m*p[1] for m,p in items)/M)
def seglist(pts): return [(Fr(abs(b[0]-a[0])+abs(b[1]-a[1])),(Fr(a[0]+b[0],2),Fr(a[1]+b[1],2))) for a,b in zip(pts,pts[1:])]
# ---------- çizim ----------
def fx(x): return f'{float(x):.3f}'
def pt(x,y): return f'({fx(x)},{fx(y)})'
def marks_tikz(marks,u):
    o=[]
    for lab,x,y,d in marks:
        o.append(f'\\fill {pt(x*u,y*u)} circle (1.7pt);')
        o.append(f'\\node[{d},inner sep=1.5pt,font=\\small\\bfseries] at {pt(x*u,y*u)} {{{lab}}};')
    return o
def HS(k): return f'\\begin{{tikzpicture}}[scale={k},line cap=round,line join=round,font=\\small]\n'
def plate(cells,hatch=(),marks=(),u=.55,extra=(),labels=(),fills=None,k=1.5,pre=()):
    pre=list(pre)
    cells=set(cells); hatch=set(hatch); al=cells|hatch; o=list(pre)
    for (i,j) in cells:
        f=(fills or {}).get((i,j),'gray!22')
        o.append(f'\\fill[{f}] {pt(i*u,j*u)} rectangle {pt((i+1)*u,(j+1)*u)};')
    for (i,j) in hatch:
        o.append(f'\\fill[gray!60] {pt(i*u,j*u)} rectangle {pt((i+1)*u,(j+1)*u)}; \\draw[white,thin] {pt(i*u,j*u)} -- {pt((i+1)*u,(j+1)*u)};')
    ed=set(); th=set()
    for (i,j) in al:
        for e,(a,b),nb in [((i,j,'h'),((i,j),(i+1,j)),(i,j-1)),((i,j+1,'h'),((i,j+1),(i+1,j+1)),(i,j+1)),((i,j,'v'),((i,j),(i,j+1)),(i-1,j)),((i+1,j,'v'),((i+1,j),(i+1,j+1)),(i+1,j))]:
            ed.add((e,a,b))
            if nb not in al: th.add(e)
    for e,a,b in sorted(ed):
        w='thick' if e in th else 'very thin,gray!70'
        o.append(f'\\draw[{w}] {pt(a[0]*u,a[1]*u)} -- {pt(b[0]*u,b[1]*u)};')
    o+=list(extra)+marks_tikz(marks,u)+list(labels)
    return tikz_svg(HS(k)+'\n'.join(o)+TAIL)
def wirefig(paths,marks=(),W=8,Hh=7,u=.55,extra=(),k=1.4):
    o=[]
    for i in range(W+1): o.append(f'\\draw[very thin,gray!60,dashed] {pt(i*u,0)} -- {pt(i*u,Hh*u)};')
    for j in range(Hh+1): o.append(f'\\draw[very thin,gray!60,dashed] {pt(0,j*u)} -- {pt(W*u,j*u)};')
    for p in paths:
        o.append('\\draw[line width=1.6pt] '+' -- '.join(pt(a*u,b*u) for a,b in p)+';')
    o+=list(extra)+marks_tikz(marks,u)
    return tikz_svg(HS(k)+'\n'.join(o)+TAIL)
# öncüllü kurucu
SIRA7=[('Yalnız I',{0}),('Yalnız II',{1}),('Yalnız III',{2}),('I ve II',{0,1}),('I ve III',{0,2}),('II ve III',{1,2}),('I, II ve III',{0,1,2})]
def onc(truth,miss,wrong,drop):
    T={i for i,t in enumerate(truth) if t}
    names=[n for n,s in SIRA7]; sets=dict(SIRA7)
    dogru=[n for n,s in SIRA7 if s==T][0]
    others=[n for n in names if n!=dogru]
    keep=[n for k,n in enumerate(others) if k not in drop]; assert len(keep)==4
    sira=[n for n in names if n==dogru or n in keep]; assert len(sira)==5
    yan=[]
    for n in keep:
        S=sets[n]; txt=[]
        for i in sorted(S-T): txt.append(wrong[i])
        for i in sorted(T-S): txt.append(miss[i])
        yan.append((n,' '.join(txt),'bilgi'))
    return dogru,yan,sira
def tfs(t): return 'doğru' if t else 'yanlış'
def pts_choice(correct,wrongs,idx,letters='KLMNP'):
    """correct=(x,y,cel yok); wrongs=[(x,y,cel,tur)]; idx: doğru noktanın harf sırası. Dönen: harfli noktalar, dogru harf, yan, sira"""
    lst=list(wrongs); lst.insert(idx,None)
    pos={}; yan=[]; dog=None
    for k,L in enumerate(letters):
        if lst[k] is None: dog=L; pos[L]=correct[:2]
        else: pos[L]=lst[k][0]; yan.append((L,lst[k][1],lst[k][2]))
    assert len({p for p in pos.values()})==5
    return pos,dog,yan,list(letters)
def fmt_pt(p): return f'({v(p[0])}; {v(p[1])})'

# =========================================================================
# 01 · L biçimli levha · kolay
kartla('K-AFAG-01','Eş karelerden oluşan levhanın ağırlık merkezi','Levha özdeş karelere ayrılır; her karenin kütlesi eşit ve ağırlığı kendi merkezinde kabul edilir, parçaların ağırlık merkezleri koordinatlarının ortalaması alınarak levhanın ağırlık merkezi bulunur.','Ağırlık merkezini sınırlayıcı dikdörtgenin ortası sanmak; levhanın yalnız bir koluna bakmak; kareleri sayarken kütleleri unutmak.','kolay','şekilli',3,'ag-levha-merkez','Eş karelerden oluşan türdeş levhanın ağırlık merkezi')
S1=rect(0,0,4,1)|rect(0,0,1,3); c1=cm(S1); assert c1==(Fr(3,2),Fr(1)) and len(S1)==6
pos,dog,yan,sira=pts_choice((c1[0],c1[1]),[
 ((2,Fr(3,2)),'Levhanın tamamını kapsayan dikdörtgenin ortasını (2; 1,5) ağırlık merkezi sanmış; boş kısmı hesaba katmamış.','bilgi'),
 ((2,Fr(1,2)),'Yalnız yatay kolun ağırlık merkezini (2; 0,5) seçmiş; düşey kolu hesaba katmamış.','dikkat'),
 ((Fr(1,2),2),'Yalnız düşey kolun ağırlık merkezini (0,5; 2) seçmiş; yatay kolu hesaba katmamış.','dikkat'),
 ((1,1),'Levhanın iç köşe noktasını (1; 1) ağırlık merkezi sanmış; kare sayılarına ve kütle dağılımına bakmamış.','islem')],0)
mk1=[(L,pos[L][0],pos[L][1],{'K':'above right','L':'above right','M':'below right','N':'above right','P':'below left'}[L]) for L in 'KLMNP']
SK=plate(S1,marks=mk1,u=.62)
q('0001',tipId='ag-levha-merkez',tip='Eş karelerden oluşan türdeş levhanın ağırlık merkezi',z='kolay',alt='Levhanın Ağırlık Merkezi',kaz='Eş karelerden oluşan türdeş levhanın ağırlık merkezini parçaların ağırlık merkezlerinden bulur.',
 kart='K-AFAG-01 (L levha) · 6 eş kare',kalip='şekilli',
 metin='Şekilde, eş karelerden oluşan ince, türdeş ve L biçimli bir levha ile levha düzlemindeki K, L, M, N ve P noktaları gösterilmiştir. Noktalar kare kenarlarının köşelerinde ya da kenar orta noktalarındadır.\nBuna göre, levhanın ağırlık merkezi hangi noktadadır?',
 dogru=dog,yan=yan,sira=sira,istenen='Levhanın ağırlık merkezinin bulunduğu nokta.',
 ip=['Levhayı yatay ve düşey kollar olarak iki dikdörtgene ayırıp her birinin kütlesini kare sayısıyla orantılı al.'],
 bilgi=[B('Türdeş levhanın ağırlık merkezi','Eş karelerden oluşan türdeş levhada her karenin kütlesi eşittir ve ağırlığı karenin merkezinden etki eder. Levhanın ağırlık merkezinin koordinatı, karelerin merkez koordinatlarının ortalamasıdır. Örnek: iki bitişik karenin ağırlık merkezi ortak kenarın orta noktasındadır')],
 ad=[A('Koordinat sistemi seç','Sol alt köşeyi başlangıç, kare kenarını 1 birim al; her karenin merkezini yaz.','Yatay kol: 4 kare, düşey kol: ek 2 kare'),
     A('Kolları ayır','Yatay kol 4 kare ve ağırlık merkezi (2; 0,5); düşey kolun yukarıdaki kısmı 2 kare, merkezi (0,5; 2).','m₁ = 4, m₂ = 2'),
     A('Ağırlıklı ortalama al','Her koordinat kütleyle ağırlıklandırılır.','x = (4 × 2 + 2 × 0,5) ÷ 6 = 1,5 · y = (4 × 0,5 + 2 × 2) ÷ 6 = 1'),
     A('Noktayı bul','(1,5; 1) noktasını ızgarada işaretle.','Ağırlık merkezi: '+dog+' noktası')],
 puf='Biçimi dikdörtgenlere ayır, kare sayılarını kütle say ve koordinatların ağırlıklı ortalamasını al.',sekil=SK)

# 02 · kare levhadan köşe parçası kesilmiş · orta
kartla('K-AFAG-02','Parça çıkarılmış levhanın ağırlık merkezi','Parça çıkarılan levha, tam levhadan çıkarılan parçanın negatif kütleli eklenmesi gibidir: M·x_tam = m_kalan·x_kalan + m_çıkan·x_çıkan.','Ağırlık merkezini tam levhanın merkezinde bırakmak; çıkarılan parçanın merkezine göre simetrik bir nokta almak.','orta','şekilli',4,'ag-kesme-ekleme','Parça kesilip çıkarılan levhanın ağırlık merkezi')
S2=rect(0,0,6,6)-rect(0,0,3,3); c2=cm(S2); assert c2==(Fr(7,2),Fr(7,2)) and len(S2)==27
assert (36*Fr(3)-9*Fr(3,2))/27==Fr(7,2)
pos,dog,yan,sira=pts_choice(c2,[
 ((3,3),'Kesilmeden önceki kare levhanın merkezini (3; 3) seçmiş; çıkarılan parçanın etkisini hesaba katmamış.','dikkat'),
 ((Fr(9,2),Fr(9,2)),'Ağırlık merkezini, çıkarılan parçanın merkezine göre karşı tarafta eşit uzaklıkta (4,5; 4,5) almış; kütle oranını kullanmamış.','bilgi'),
 ((Fr(3,2),Fr(3,2)),'Çıkarılan parçanın ağırlık merkezini (1,5; 1,5) kalan levhanın ağırlık merkezi sanmış.','dikkat'),
 ((Fr(9,2),Fr(3,2)),'Yalnız sağ alttaki kolun ağırlık merkezini (4,5; 1,5) seçmiş.','dikkat')],2)
dirs={'K':'below left','L':'above left','M':'above right','N':'below right','P':'above right'}
SK=plate(S2,hatch=rect(0,0,3,3),marks=[(L,pos[L][0],pos[L][1],{'K':'below right','L':'above right','M':'above left','N':'below right','P':'below right'}[L]) for L in 'KLMNP'],u=.5)
q('0002',tipId='ag-kesme-ekleme',tip='Parça kesilip çıkarılan levhanın ağırlık merkezi',z='orta',alt='Kesilen Levha',kaz='Parçası çıkarılmış türdeş levhanın ağırlık merkezini tam levha ve çıkarılan parçanın kütle–konum ilişkisinden bulur.',
 kart='K-AFAG-02 (6×6 levhadan 3×3 kesilmiş) · M·x = Σ m·x',kalip='şekilli',
 metin='Şekilde eş karelerden oluşan 6×6’lık türdeş bir kare levha görülmektedir. Levhanın sol alt köşesindeki, kenarı 3 kare olan taralı bölüm kesilip atılıyor. K, L, M, N ve P noktaları kare kenarlarının köşelerinde ya da orta noktalarındadır.\nBuna göre, kalan levhanın ağırlık merkezi hangi noktadadır?',
 dogru=dog,yan=yan,sira=sira,istenen='Kalan levhanın ağırlık merkezinin bulunduğu nokta.',
 ip=['Tam levha = kalan levha + çıkarılan parça yazıp ağırlık merkezi koordinatlarını kütlelerle ağırlıklandır.'],
 bilgi=[B('Parçalardan ağırlık merkezi','Bir cisim parçalara ayrılırsa ağırlık merkezinin koordinatı x = (m₁x₁ + m₂x₂ + …) ÷ (m₁ + m₂ + …) ile bulunur. Parça çıkarılmışsa tam cismi, kalan ve çıkarılan parçaların toplamı olarak yaz. Örnek: 4 kütleli levhadan 1 kütleli parça çıkarılırsa kalan 3 kütle denge koşulunu sağlamak zorundadır')],
 ad=[A('Kütleleri belirle','Kare sayıları kütle ile orantılıdır.','Tam levha: 36, çıkarılan: 9, kalan: 27'),
     A('Merkezleri yaz','Köşe (0; 0) alınırsa tam levhanın merkezi (3; 3), çıkarılan parçanın (1,5; 1,5).','—'),
     A('Denge denklemini kur','36 × 3 = 27 × x + 9 × 1,5','108 = 27x + 13,5 → x = 3,5 (y için aynı)'),
     A('Noktayı bul','Ağırlık merkezi köşegen üzerindedir.','(3,5; 3,5) → '+dog)],
 puf='Çıkarılan parçayı “negatif kütle” gibi düşün: tam levhanın momenti = kalanın momenti + çıkanın momenti.',sekil=SK)

# 03 · kavram öncüllü · kolay
kartla('K-AFAG-03','Kütle merkezi ve ağırlık merkezi kavramı','Homojen ve simetrik cismin kütle merkezi geometrik merkezdedir; düzgün çekim alanında ağırlık merkezi ile kütle merkezi çakışır; ağırlık merkezi cismin dışında olabilir.','Ağırlık merkezinin daima cismin içinde olduğunu sanmak; kütle merkezi ile ağırlık merkezini her koşulda farklı saymak.','kolay','öncüllü',3,'ag-kavram','Kütle merkezi ve ağırlık merkezi kavramları')
tr=[True,False,True]
dg,yn,sr=onc(tr,['Homojen kürenin kütle merkezinin geometrik merkezde olduğunu bilmemiş.','','Düzgün çekim alanında ağırlık merkezinin kütle merkeziyle çakıştığını bilmemiş.'],['','Halka gibi cisimlerin ağırlık merkezinin cismin dışında kalabileceğini düşünmemiş.',''],(0,1))
q('0003',tipId='ag-kavram',tip='Kütle merkezi ve ağırlık merkezi kavramları',z='kolay',alt='Kavramlar',kaz='Kütle merkezi ve ağırlık merkezi kavramlarını, simetrik ve homojen cisimler üzerinde yorumlar.',
 kart='K-AFAG-03 (kavram öncülleri) · küre, halka, düzgün çekim',kalip='öncüllü',
 metin='Öğretmen, kütle merkezi ve ağırlık merkezi kavramlarıyla ilgili şu üç ifadeyi tahtaya yazıyor:\nI. Homojen bir kürenin kütle merkezi, kürenin geometrik merkezindedir.\nII. Bir cismin ağırlık merkezi her zaman cismin madde bulunan bir noktasındadır.\nIII. Yerçekimi ivmesinin her noktada aynı olduğu bir bölgede cismin kütle merkezi ile ağırlık merkezi aynı noktadadır.\nBuna göre, bu ifadelerden hangileri doğrudur?',
 dogru=dg,yan=yn,sira=sr,istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['Halka biçimli bir cismin ağırlık merkezinin nerede olduğunu düşün.'],
 bilgi=[B('Kütle ve ağırlık merkezi','Kütle merkezi, cismin kütlesinin toplandığı kabul edilen noktadır; homojen ve simetrik cisimlerde geometrik merkezdir. Ağırlık merkezi, ağırlık kuvvetinin etki noktasıdır ve yerçekimi alanı düzgünse kütle merkeziyle çakışır. Örnek: halkanın merkezi halkada madde olmayan bir noktadır')],
 ad=[A('I. ifadeyi incele','Homojen küre her yönde simetriktir.','I: doğru (merkezde)'),
     A('II. ifadeyi incele','Halkanın ağırlık merkezi halka düzleminde, madde bulunmayan merkezdedir.','II: yanlış'),
     A('III. ifadeyi incele','Düzgün çekim alanında her parçaya etkiyen ağırlık orantılıdır; bileşke kütle merkezinden geçer.','III: doğru'),
     A('Sonuç','Doğru olanlar I ve III.','Cevap: '+dg)],
 puf='Ağırlık merkezi cismin dışında olabilir; düzgün çekim alanında kütle ve ağırlık merkezi aynıdır.',sekil=None)

# 04 · iki bantı kesilmiş levha · orta
S4=rect(0,0,6,4)-(rect(0,0,1,3)|rect(2,1,3,4)); c4=cm(S4); assert c4==(Fr(7,2),Fr(2)) and len(S4)==18
S4b=rect(0,0,6,4); assert cm(S4b)==(3,2)
pos,dog,yan,sira=pts_choice(c4,[
 ((3,2),'Kesilmeden önceki levhanın ağırlık merkezini (3; 2) seçmiş; kesilen parçaların etkisini hesaba katmamış.','dikkat'),
 ((Fr(5,2),2),'Ağırlık merkezinin kesilen parçaların bulunduğu sola doğru kayacağını sanmış; kayma yönünü ters almış.','bilgi'),
 ((Fr(9,2),2),'Kayma miktarını doğru yönde ama fazla (1,5 birim) bulmuş.','islem'),
 ((Fr(7,2),1),'Yatay koordinatı doğru bulmuş ancak düşey koordinatı, kesilen parçaların yüksekliklerine bakarak (1) kaydırmış.','dikkat')],3)
SK=plate(S4,hatch=(rect(0,0,1,3)|rect(2,1,3,4)),marks=[(L,pos[L][0],pos[L][1],{'K':'below left','L':'above left','M':'above right','N':'above right','P':'below right'}[L]) for L in 'KLMNP'],u=.55,k=2.0)
kartla('K-AFAG-04','Birden çok parça kesilmiş levha','Kesilen parçaların kütleleri ve merkezleri tek tek yazılıp tam levhanın momentinden çıkarılır; simetrik çıkarılan parçalar merkezi kaydırmaz.','Kesilen parçaları ayrı ayrı hesaplayıp yön karıştırmak; çıkarılan kütleyi toplam kütleden düşmeyi unutmak.','orta','şekilli',4,'ag-levha-merkez','Eş karelerden oluşan türdeş levhanın ağırlık merkezi')
q('0004',tipId='ag-levha-merkez',tip='Eş karelerden oluşan türdeş levhanın ağırlık merkezi',z='orta',alt='Kesilen Levha',kaz='İki ayrı parçası kesilmiş türdeş levhanın ağırlık merkezini koordinat hesabıyla bulur.',
 kart='K-AFAG-04 (6×4 levhadan iki şerit) · Σ m·x',kalip='şekilli',
 metin='Dikdörtgen biçimli, ince ve türdeş bir levha 6×4 eş kareye ayrılmıştır. Levhanın şekilde taralı gösterilen iki dikey şeridi makasla ayrılıp atılıyor; geriye tek parça bir levha kalıyor. Şekilde işaretli K, L, M, N ve P noktalarının hepsi kare köşelerinde ya da kenar orta noktalarındadır.\nGeriye kalan levhanın ağırlık merkezi bu noktalardan hangisine denk gelir?',
 dogru=dog,yan=yan,sira=sira,istenen='Kalan levhanın ağırlık merkezinin bulunduğu nokta.',
 ip=['Kesilen iki şeridin ortak ağırlık merkezini bul; kalan levhanın ağırlık merkezi bunun tam levhanın merkezine göre karşı tarafındadır.'],
 bilgi=[B('Kesilen parçalar','Tam levha: M, merkezi O. Çıkarılan parçaların toplam kütlesi m, ortak merkezi C ise kalan levhanın merkezi O’ya göre C’nin karşı tarafında, O’dan uzaklığı m·(OC) ÷ (M − m) olan noktadadır. Örnek: simetrik çıkarılan parçalar merkezi kaydırmaz')],
 ad=[A('Tam levha ve kesilenler','Tam levha 24 kare, merkezi (3; 2). Kesilen şeritler 3 + 3 = 6 kare.','Kalan: 18 kare'),
     A('Kesilenlerin ortak merkezi','Sol şerit merkezi (0,5; 1,5); sağdaki şerit (2,5; 2,5); kütleler eşit.','x_c = (0,5 + 2,5) ÷ 2 = 1,5 · y_c = (1,5 + 2,5) ÷ 2 = 2'),
     A('Denge denklemini kur','24 × 3 = 18 × x + 6 × 1,5','72 = 18x + 9 → x = 3,5'),
     A('Düşey koordinat','24 × 2 = 18 × y + 6 × 2 → y = 2','Nokta: (3,5; 2) → '+dog)],
 puf='Kesilen parçaların ortak merkezi tam levhanın merkezinin neresindeyse, kalan levhanın merkezi tam karşı yöne kayar.',sekil=SK)

# 05 · kesilecek parça çiftleri · öncüllü orta
kartla('K-AFAG-05','Ağırlık merkezinin yerinin değişmemesi','Parçalar kesilince ağırlık merkezi yerinde kalıyorsa kesilen parçaların ortak ağırlık merkezi levhanın merkezindedir.','Her parçayı ayrı ayrı simetrik aramak; yalnız bir koordinatı kontrol etmek.','orta','öncüllü',4,'ag-kesme-ekleme','Parça kesilip çıkarılan levhanın ağırlık merkezi')
Q5=rect(0,0,4,4); O5=(Fr(2),Fr(2))
def ctr(c): return (Fr(2*c[0]+1,2),Fr(2*c[1]+1,2))
Acut=[(0,3),(2,0)]
need=(8-sum(ctr(c)[0] for c in Acut),8-sum(ctr(c)[1] for c in Acut))
cand=[c for c in sorted(Q5) if c not in Acut]
good=[(a,b) for a,b in itertools.combinations(cand,2) if (ctr(a)[0]+ctr(b)[0],ctr(a)[1]+ctr(b)[1])==need]
assert good, need
pair_true=good[0]
# harf yerleşimi: I:(K,L) II:(M,N) III:(S,T)
random.seed(11)
rest=[c for c in cand if c not in pair_true]
def falsepair(used):
    while True:
        a,b=random.sample([c for c in rest if c not in used],2)
        if (ctr(a)[0]+ctr(b)[0],ctr(a)[1]+ctr(b)[1])!=need: return (a,b)
f1=falsepair(set()); f2=falsepair(set(f1))
truth5=[False,True,True]
pairs5=[f1,pair_true,f2] ;
pairs5=[f1,pair_true,None]
# III de doğru olsun: ikinci doğru çifti ara
good2=[(a,b) for a,b in good if not ({a,b}&set(pair_true)) and not ({a,b}&set(f1))]
assert good2, 'ikinci doğru çift yok'
pairs5[2]=good2[0]
for t,pr in zip(truth5,pairs5):
    s=(ctr(pr[0])[0]+ctr(pr[1])[0],ctr(pr[0])[1]+ctr(pr[1])[1]); assert (s==need)==t
labs=['K','L','M','N','S','T']; lab_cell={}
flat=[c for pr in pairs5 for c in pr]; assert len(set(flat))==6 and not (set(flat)&set(Acut))
for l,c in zip(labs,flat): lab_cell[c]=l
labels=[f'\\node[font=\\small\\bfseries] at {pt(ctr(c)[0]*.6,ctr(c)[1]*.6)} {{{l}}};' for c,l in lab_cell.items()]
SK=plate(Q5,hatch=Acut,labels=labels,u=.6)
dg,yn,sr=onc(truth5,[f'{labs[2*i]} ve {labs[2*i+1]} merkez koordinatlarının toplamının (5; 4) olduğunu, yani dört karenin ortak merkezinin levhanın merkezine geldiğini görmemiş.' for i in range(3)],[f'{labs[2*i]} ve {labs[2*i+1]} eklenince dört karenin ortak merkezinin levhanın merkezinden farklı kaldığını (toplamın (5; 4) olmadığını) görmemiş.' for i in range(3)],(0,5))
exp5=[f'{labs[2*i]} ve {labs[2*i+1]} kesilirse dört parçanın koordinat toplamı '+('(8; 8) olur' if truth5[i] else 'farklı çıkar') for i in range(3)]
q('0005',tipId='ag-kesme-ekleme',tip='Parça kesilip çıkarılan levhanın ağırlık merkezi',z='orta',alt='Kesilen Levha',kaz='Levhanın ağırlık merkezinin yerinin değişmemesi için kesilmesi gereken parçaları belirler.',
 kart='K-AFAG-05 (4×4 levha, parça çiftleri) · ortak merkez = levha merkezi',kalip='öncüllü',
 metin=f'Şekilde 4×4’lük, eş karelerden oluşan türdeş bir levha görülmektedir. Levhadan taralı iki kare kesilip çıkarılmıştır. Her birinde taralı kareler ile birlikte toplam dört kare çıkarılan aşağıdaki üç ayrı işlem düşünülüyor.\nBuna göre,\nI. {labs[0]} ve {labs[1]},\nII. {labs[2]} ve {labs[3]},\nIII. {labs[4]} ve {labs[5]}\nkare çiftlerinden hangileri, taralı iki kareye ek olarak tek başına (yalnız o çift) kesilip çıkarılırsa levhanın ağırlık merkezinin yeri değişmez?',
 dogru=dg,yan=yn,sira=sr,istenen='Ağırlık merkezinin yerini değiştirmeyen kesme işlemleri.',
 ip=['Yerinin değişmemesi için çıkarılan dört karenin ortak ağırlık merkezinin levhanın merkezinde olması gerekir.'],
 bilgi=[B('Yerini koruma koşulu','Levhanın merkezi O ise, çıkarılan parçaların ortak ağırlık merkezi de O’da olmalıdır; çünkü kalan parçanın momenti ancak o zaman değişmez. Örnek: merkeze göre karşılıklı simetrik iki parça birlikte çıkarılabilir')],
 ad=[A('Koşulu yaz','Çıkarılan dört karenin merkez koordinatlarının ortalaması (2; 2) olmalıdır.','Toplam: (8; 8)'),
     A('Taralı karelerin toplamı','Taralı karelerin merkezleri (0,5; 3,5) ve (2,5; 0,5).','Toplam: (3; 4) → çiftin toplamı (5; 4) olmalı'),
     A('Çiftleri sına','Her çiftin merkez koordinatlarının toplamı hesaplanır.',' · '.join(exp5)),
     A('Sonuç','Koşulu sağlayan çiftler: '+', '.join(['I','II','III'][i] for i in range(3) if truth5[i])+'.','Cevap: '+dg)],
 puf='Ağırlık merkezi yerinde kalacaksa çıkan parçaların ortak merkezi levhanın merkezi olmalı; koordinat toplamlarını sına.',sekil=SK)

# 06 · asılı levha, ip noktaları · öncüllü orta
kartla('K-AFAG-06','Asılı levhanın dengesi','Levha asıldığında ağırlık merkezi askı noktasının hemen altına gelinceye kadar döner; askı noktası ağırlık merkezinin düşey doğrultusundaysa şekil dönmez.','Askı noktasının solunda ya da sağında kalan ağırlık merkezinin dönüş yönünü karıştırmak.','orta','öncüllü',4,'ag-asma','İple asılan levhanın dengesi')
S6=rect(0,0,5,4)-(rect(0,0,2,1)|rect(3,0,5,3)); c6=cm(S6); print('S6',len(S6),c6)
assert c6[0]==2
px={'K':1,'L':2,'M':4}
truth6=[px['K']<c6[0],px['L']==c6[0],px['M']<c6[0]]
assert truth6==[True,True,False]
mk6=[(l,x,4,'above') for l,x in px.items()]
SK=plate(S6,hatch=(rect(0,0,2,1)|rect(3,0,5,3)),marks=mk6,u=.62)
dg,yn,sr=onc(truth6,['K’den asılan levhanın ağırlık merkezi askı noktasının sağında kaldığından sağ tarafın aşağı döneceğini görememiş.','L’nin ağırlık merkezinin düşey doğrultusunda olduğunu fark edememiş.',''],['','','M’den asılırken sağ üst köşenin aşağı gideceğini sanmış; ağırlık merkezi M’nin solunda kaldığı için sol taraf aşağı iner.'],(4,5))
q('0006',tipId='ag-asma',tip='İple asılan levhanın dengesi',z='orta',alt='Asılı Levha',kaz='Levhanın ağırlık merkezini bularak farklı noktalardan asıldığında alacağı dengeyi yorumlar.',
 kart='K-AFAG-06 (5×4 levha, üst kenardan asma) · ağırlık merkezi düşeyi',kalip='öncüllü',
 metin='Şekilde eş karelerden oluşan türdeş bir levha görülmektedir; levhanın taralı kısımları kesilip atılmıştır. Kalan levha, üst kenar üzerindeki K, L ya da M noktalarından biri ile düşey bir ipe bağlanarak, düşey düzlemde serbestçe dönebilecek biçimde asılıyor.\nBuna göre, levha dengeye geldiğinde,\nI. K noktasından asılırsa levhanın sağ üst köşesi sol üst köşesinden daha aşağıdadır.\nII. L noktasından asılırsa levhanın üst kenarı yatay durur.\nIII. M noktasından asılırsa levhanın sağ üst köşesi sol üst köşesinden daha aşağıdadır.\nyargılarından hangileri doğrudur?',
 dogru=dg,yan=yn,sira=sr,istenen='Denge durumu için doğru olan yargılar.',
 ip=['Kalan levhanın ağırlık merkezinin yatay konumunu bul; denge, ağırlık merkezi askı noktasının hemen altına gelince oluşur.'],
 bilgi=[B('Asılı cismin dengesi','İple asılan cismin ağırlık merkezi, denge durumunda askı noktasının tam altındadır. Ağırlık merkezi askı noktasının sağındaysa ağırlığın torku cismi o yönde (sağ taraf aşağı) döndürür. Örnek: ucundan asılan çubuk düşey durur')],
 ad=[A('Kalan levhanın merkezi','Kalan 12 kare; kare merkezlerinin koordinat ortalaması alınır.','x_cm = '+v(c6[0])+' birim, y_cm = '+v(c6[1])+' birim'),
     A('K noktası (x = 1)','Ağırlık merkezi (x = 2) askı noktasının sağında kalır; levha sağ tarafı aşağı gelecek biçimde döner.','I: '+tfs(truth6[0])),
     A('L noktası (x = 2)','Askı noktası ağırlık merkezinin hemen üstündedir; levha dönmez.','II: '+tfs(truth6[1])),
     A('M noktası (x = 4)','Ağırlık merkezi askı noktasının solunda kalır; sol taraf aşağı iner.','III: '+tfs(truth6[2])),
     A('Sonuç','Doğru yargılar I ve II.','Cevap: '+dg)],
 puf='Asılı levhada ağırlık merkezi askı noktasının hangi yanındaysa levha o yanı aşağı olacak biçimde döner.',sekil=SK)

# 07 · katlama · orta
kartla('K-AFAG-07','Katlanan levhanın ağırlık merkezi','Katlanan bölüm, kütlesi korunarak aynalanır; üst üste gelen yerde kütle iki katına çıkar. Ağırlık merkezi, aynalanan parçanın yeni merkeziyle hesaplanır.','Katlamada kütle kaybolduğunu sanmak; parçanın yeni merkezini aynalamayı unutmak; üst üste gelen bölgeyi tek kat saymak.','orta','şekilli',4,'ag-katlama','Katlanan levhanın ağırlık merkezi')
W7,H7,K7=8,4,6
mult={}
for i in range(W7):
    for j in range(H7):
        ii=i if i<K7 else 2*K7-1-i; mult[(ii,j)]=mult.get((ii,j),0)+1
x7=Fr(sum(m*(2*i+1) for (i,j),m in mult.items()),2*W7*H7); assert x7==Fr(7,2)
assert (24*Fr(3)+8*Fr(5))/32==x7
fold=[f'\\draw[very thick,dashed,vurgu] {pt(K7*.55,-.35)} -- {pt(K7*.55,H7*.55+.35)};',
      f'\\draw[{ARR},thick] {pt(7.0*.55,H7*.55+.3)} .. controls {pt(6.7*.55,H7*.55+.9)} and {pt(5.3*.55,H7*.55+.9)} .. {pt(5.0*.55,H7*.55+.3)};']
SK=plate(rect(0,0,6,4),hatch=rect(6,0,8,4),extra=fold+[f'\\node[below] at {pt(6*.55,-.3)} {{katlama doğrusu}};'],u=.55)
q('0007',tipId='ag-katlama',tip='Katlanan levhanın ağırlık merkezi',z='orta',alt='Katlama',kaz='Katlanarak üst üste getirilen levhanın ağırlık merkezinin yerini kütle dağılımından bulur.',
 kart='K-AFAG-07 (8×4 levha, 2 sütun katlanıyor) · aynalama',kalip='şekilli',
 metin='Şekilde eş karelerden oluşan 8×4’lük ince ve türdeş bir levha görülmektedir. Levha, şekildeki kesikli doğru boyunca katlanarak taralı bölüm levhanın üzerine tamamen yapıştırılıyor.\n(Kare kenarı = 1 birim)\nBuna göre, katlama işleminden sonra levhanın ağırlık merkezinin levhanın sol kenarına olan uzaklığı kaç birimdir?',
 dogru=Fr(7,2),yan=[(3,'Üst üste gelen bölgeyi tek kat sayarak yalnız yeni şeklin (6×4) merkezini almış: 6 ÷ 2 = 3.','dikkat'),
  (4,'Katlamanın ağırlık merkezini değiştirmeyeceğini sanmış; ilk levhanın merkezini (8 ÷ 2 = 4) yazmış.','bilgi'),
  (Fr(9,2),'Kayma yönünü ters alarak ilk merkezin 0,5 birim sağına (4 + 0,5) yazmış.','islem'),
  (5,'Katlanan parçanın katlama sonrası merkezini (5) levhanın ağırlık merkezi sanmış.','dikkat')],
 istenen='Ağırlık merkezinin sol kenara uzaklığı (birim).',
 ip=['Katlanan 2×4’lük bölümün katlanmadan önceki ve sonraki merkezlerinin yatay konumunu karşılaştır.'],
 bilgi=[B('Katlama','Katlama kütleyi değiştirmez; yalnız parçanın konumunu aynalar. Yeni ağırlık merkezi, kütle × konum toplamının toplam kütleye bölünmesiyle bulunur. Örnek: 2 kütleli parça 4 birim ötelenirse sistemin merkezi 2 × 4 ÷ toplam kütle kadar kayar')],
 ad=[A('Kütleleri ayır','Katlanmayan kısım 6×4 = 24 kare, katlanan kısım 2×4 = 8 kare.','M = 32 kare'),
     A('Merkezleri yaz','Katlanmayan kısmın merkezi sol kenardan 3 birim. Katlanan kısmın merkezi önce 7 birimdeydi; katlama doğrusuna (6) göre aynalanınca 5 birim olur.','x₁ = 3, x₂ = 5'),
     A('Ortalama al','Yatay koordinat kütleyle ağırlıklandırılır.','x = (24 × 3 + 8 × 5) ÷ 32 = 112 ÷ 32 = 3,5'),
     A('Sonuç','Düşey konum değişmez.','Cevap: 3,5 birim')],
 puf='Katlamada kütle sabit kalır; yalnız katlanan parçanın merkezi katlama doğrusuna göre aynalanır.',sekil=SK)

# 08 · L-tel öncüllü · orta
kartla('K-AFAG-08','Bükülmüş telin ağırlık merkezi','Türdeş telde kütle uzunluğuyla orantılıdır; her doğrusal parçanın ağırlık merkezi orta noktasındadır, tel ağırlık merkezi parçaların uzunlukla ağırlıklı ortalamasıdır.','Telin ağırlık merkezini tel üzerinde aramak; parçaları eşit kütleli saymak; levha gibi alan hesabı yapmak.','orta','öncüllü',4,'ag-tel','Bükülmüş türdeş telin ağırlık merkezi')
seg8=seglist([(0,3),(0,0),(6,0)]); c8=wcm(seg8); assert c8==(2,Fr(1,2))
tr8=[False,c8[0]==4*c8[1],(3-c8[0])==1 and seg8[0][0]*2==seg8[1][0]]
assert tr8==[False,True,True]
SK=wirefig([[(0,3),(0,0),(6,0)]],W=7,Hh=4,u=.65,extra=[f'\\node[left] at {pt(0,1.5*.65)} {{$3$ birim}}; \\node[below] at {pt(3*.65,0)} {{$6$ birim}};'])
dg,yn,sr=onc(tr8,['','II. yargıdaki 2 = 4 × 0,5 oranını fark edememiş; koordinatları bulsa da yargıyı yanlış saymış.','III. yargıda 3 − 2 = 1 birimlik uzaklığı kontrol etmemiş.'],['Ağırlık merkezinin tel üzerinde bulunduğunu sanmış; ağırlık merkezi telin içinde kalan boşluk bölgesindedir.','Ağırlık merkezinin koordinatlarını (2; 0,5) bulduğunda 2 = 4 × 0,5 olduğunu fark etmemiş.','Parçaların kütle oranını (1 : 2) ve AM’nin yatay kolun orta noktasına uzaklığını (1 birim) yanlış bulmuş.'],(1,5))
q('0008',tipId='ag-tel',tip='Bükülmüş türdeş telin ağırlık merkezi',z='orta',alt='Tel',kaz='Dik açıyla bükülmüş türdeş telin ağırlık merkezinin yerini uzunluk ağırlıklı ortalamadan bulur.',
 kart='K-AFAG-08 (L biçimli tel, 6 + 3 birim) · uzunlukla ağırlıklı ortalama',kalip='öncüllü',
 metin='Düzgün ve türdeş ince bir tel, şekildeki gibi dik açıyla bükülerek bir köşesinden birleşen 6 birim ve 3 birim uzunluğunda iki kol oluşturulmuştur. Koordinat sisteminin başlangıcı olarak köşe noktası alınıyor; yatay kol x ekseni, düşey kol y ekseni boyunca uzanıyor.\nBuna göre,\nI. Telin ağırlık merkezi tel üzerindedir.\nII. Ağırlık merkezinin düşey (y) eksenine uzaklığı, yatay (x) eksenine uzaklığının 4 katıdır.\nIII. Ağırlık merkezi, yatay kolun orta noktasının 1 birim solundadır.\nyargılarından hangileri doğrudur?',
 dogru=dg,yan=yn,sira=sr,istenen='Doğru olan yargılar.',
 ip=['Her kolun kütlesini uzunluğuyla, ağırlık merkezini orta noktasıyla temsil et.'],
 bilgi=[B('Telin ağırlık merkezi','Türdeş telde kütle, uzunlukla orantılıdır; düz bir parçanın ağırlık merkezi orta noktasıdır. Birden çok parçalı telin merkezi x = Σ(ℓ·x) ÷ Σℓ ile bulunur. Örnek: 4 ve 2 birimlik kollar için kütle oranı 2 : 1’dir')],
 ad=[A('Parçaları yaz','Yatay kol ℓ = 6, orta noktası (3; 0); düşey kol ℓ = 3, orta noktası (0; 1,5).','m₁ : m₂ = 2 : 1'),
     A('Koordinatları bul','Uzunlukla ağırlıklı ortalama.','x = (6 × 3 + 3 × 0) ÷ 9 = 2 · y = (6 × 0 + 3 × 1,5) ÷ 9 = 0,5'),
     A('I. yargı','AM (2; 0,5) noktasında tel yok.','I: '+tfs(tr8[0])),
     A('II ve III','x = 2 = 4 × 0,5; yatay kolun orta noktası x = 3, 3 − 2 = 1.','II: '+tfs(tr8[1])+' · III: '+tfs(tr8[2])),
     A('Sonuç','Doğru yargılar II ve III.','Cevap: '+dg)],
 puf='Tel hesabında kütle yerine uzunluk kullan; ağırlık merkezi tel üzerinde olmak zorunda değildir.',sekil=SK)

# 09 · dik üçgen tel · orta
kartla('K-AFAG-09','Üçgen biçimli telin ağırlık merkezi','Tel çerçevede kenarlar kütle taşır; her kenarın ağırlık merkezi orta noktasıdır ve uzunluğuyla ağırlıklı ortalama alınır (levhadaki 1/3 kuralı geçerli değildir).','Üçgen tel için levhanın ağırlık merkezi kuralını (1/3) kullanmak.','orta','şekilli',4,'ag-tel','Bükülmüş türdeş telin ağırlık merkezi')
seg9=[(Fr(4),(Fr(2),Fr(0))),(Fr(3),(Fr(0),Fr(3,2))),(Fr(5),(Fr(2),Fr(3,2)))]; c9=wcm(seg9); assert c9==(Fr(3,2),Fr(1)) and sum(s[0] for s in seg9)==12
pos,dog,yan,sira=pts_choice(c9,[
 ((1,Fr(3,2)),'Yatay koordinatı iki dik kenarın orta noktalarının ortalamasından (0 + 2) ÷ 2 = 1, düşey koordinatı sol kenarın orta noktasından (1,5) almış; kenar uzunluklarını ve hipotenüsü hesaba katmamış.','bilgi'),
 ((2,Fr(3,2)),'Hipotenüsün orta noktasını (2; 1,5) ağırlık merkezi seçmiş.','dikkat'),
 ((1,Fr(1,2)),'Yalnız alt ve sol kenarları hesaba katıp hipotenüsü atlamış: x = (4 × 2 + 3 × 0) ÷ 7 ≈ 1,1, y = (3 × 1,5) ÷ 7 ≈ 0,6; ızgarada en yakın (1; 0,5) noktasını seçmiş.','islem'),
 ((2,1),'Yatay koordinatı alt kenarın orta noktasından (2) alıp düşey koordinatı doğru bulmuş.','dikkat')],4)
# (1,1/2) düzelt: gerçek hata metni uyumlu olsun
SK=wirefig([[(0,0),(4,0),(0,3),(0,0)]],marks=[(L,pos[L][0],pos[L][1],{'K':'above left','L':'above right','M':'below left','N':'right','P':'below'}[L]) for L in 'KLMNP'],W=5,Hh=4,u=.8,k=1.5)
q('0009',tipId='ag-tel',tip='Bükülmüş türdeş telin ağırlık merkezi',z='orta',alt='Tel',kaz='Üçgen biçiminde bükülmüş türdeş telin ağırlık merkezini kenar uzunluklarına göre bulur.',
 kart='K-AFAG-09 (3-4-5 üçgen tel) · uzunlukla ağırlıklı ortalama',kalip='şekilli',
 metin='Düzgün ve türdeş ince bir tel, kenar uzunlukları 3, 4 ve 5 birim olan dik üçgen biçiminde bükülmüş ve uçları kaynaklanmıştır. Tel, ızgaralı kâğıt üzerine şekildeki gibi konulmuştur. K, L, M, N ve P noktaları ızgara çizgilerinin kesişim noktalarında, kare merkezlerinde ya da kare kenarlarının orta noktalarındadır.\nBuna göre, telin ağırlık merkezi hangi noktadadır?',
 dogru=dog,yan=yan,sira=sira,istenen='Telin ağırlık merkezinin bulunduğu nokta.',
 ip=['Üç kenarın kütlelerini uzunluklarıyla, merkezlerini orta noktalarıyla temsil et.'],
 bilgi=[B('Tel ve levha farkı','Üçgen levhanın ağırlık merkezi köşe koordinatlarının ortalamasıdır; üçgen telde ise kütle kenarlardadır ve her kenar uzunluğuyla ağırlıklandırılır. Örnek: iki kenarlı telde ağırlık merkezi kenarların orta noktalarını bağlayan doğru üzerinde kenar uzunluklarının oranının tersine bölünür')],
 ad=[A('Kenarları yaz','Dik köşe başlangıç: alt kenar 4 birim (orta nokta (2; 0)), sol kenar 3 birim (0; 1,5), hipotenüs 5 birim (2; 1,5).','Toplam uzunluk = 12'),
     A('x koordinatı','x = (4 × 2 + 3 × 0 + 5 × 2) ÷ 12','x = 18 ÷ 12 = 1,5'),
     A('y koordinatı','y = (4 × 0 + 3 × 1,5 + 5 × 1,5) ÷ 12','y = 12 ÷ 12 = 1'),
     A('Noktayı bul','(1,5; 1) noktası ızgarada işaretlenir.','Cevap: '+dog)],
 puf='Tel çerçevede her kenar uzunluğu kadar kütle taşır; kenarların orta noktalarının uzunlukla ağırlıklı ortalamasını al.',sekil=SK)

# 10 · masa kenarında L levha + cisim · zor
kartla('K-AFAG-10','Masa kenarında dengede levha','Devrilmeden kalması için levha ile üzerindeki cismin ortak ağırlık merkezinin düşeyi destek yüzeyi içinde kalmalıdır; sınır durumda ortak merkez masa kenarının tam üstündedir.','Cismin kütlesini hesaba katmamak; levhanın geometrik merkezini ağırlık merkezi sanmak; taşma miktarını ağırlık merkezinden değil levhanın ucundan ölçmeyi karıştırmak.','zor','şekilli',5,'ag-levha-merkez','Eş karelerden oluşan türdeş levhanın ağırlık merkezi')
S10=rect(0,0,4,1)|rect(0,0,1,3); c10=cm(S10); assert c10[0]==Fr(3,2) and len(S10)==6
xcm10=(6*c10[0]+6*Fr(7,2))/12; assert xcm10==Fr(5,2)
tas=4-xcm10; assert tas==Fr(3,2)
assert 4-Fr(7,2)==Fr(1,2) and Fr(7,2)-xcm10==1 and 4-c10[0]==Fr(5,2) and 4-Fr(2)==2
ed=3*.7
pre10=[f'\\fill[gray!12] {pt(-.6,-.9)} rectangle {pt(ed,2.3)};']
ex=[f'\\draw[very thick,vurgu,dashed] {pt(ed,-1.0)} -- {pt(ed,2.5)}; \\node[above,font=\\footnotesize] at {pt(ed,2.5)} {{masa kenarı}};',
    f'\\node[font=\\footnotesize] at {pt(.25,-.6)} {{masa (üstten görünüş)}};',
    f'\\draw[thick,fill=gray!55] {pt(3.5*.7-.2,.35-.2)} rectangle {pt(3.5*.7+.2,.35+.2)}; \\node[above,font=\\footnotesize,inner sep=2pt] at {pt(3.5*.7,.7)} {{$6$ kg}};']
SK=plate(S10,u=.7,extra=ex,k=1.4,pre=pre10)
q('0010',tipId='ag-levha-merkez',tip='Eş karelerden oluşan türdeş levhanın ağırlık merkezi',z='zor',alt='Denge',kaz='Masa kenarındaki levha ve üzerindeki cismin ortak ağırlık merkezinden devrilmeden kalabilme koşulunu belirler.',
 kart='K-AFAG-10 (L levha + 6 kg cisim, masa kenarı) · ortak ağırlık merkezi sınırı',kalip='şekilli',
 metin='Şekilde yatay bir masanın üzerinde duran, eş karelerden oluşan 6 kg kütleli türdeş L biçimli bir levha yukarıdan görülmektedir. Levhanın sağ kolunun ucundaki karenin merkezine, kütlesi 6 kg olan küçük bir cisim konmuştur. Levha, sağ kolu masanın kenarından dışarı taşacak biçimde ileri doğru itilerek masanın kenarına yaklaştırılıyor ve levha devrilmeden dengede kalabiliyor. Karelerin kenarı 1 birimdir.\nBuna göre, levhanın sağ ucunun masa kenarından dışarı taşabileceği en büyük uzunluk kaç birimdir?',
 dogru=Fr(3,2),yan=[(Fr(1,2),'Taşmayı cismin konumuna göre almış: 4 − 3,5 = 0,5 birim.','dikkat'),
  (1,'Cisimle ortak ağırlık merkezi arasındaki uzaklığı (3,5 − 2,5) taşma sanmış.','islem'),
  (2,'Levhanın geometrik merkezini (2) ağırlık merkezi alıp cismi katmamış: 4 − 2 = 2 birim.','bilgi'),
  (Fr(5,2),'Cismin kütlesini hesaba katmamış; yalnız levhanın ağırlık merkezini (1,5) kullanmış: 4 − 1,5 = 2,5 birim.','dikkat')],
 istenen='Sağ ucun masa kenarından en fazla taşabileceği uzunluk (birim).',
 ip=['Devrilmenin sınırında levha ile cismin ortak ağırlık merkezinin nerede olması gerektiğini düşün.'],
 bilgi=[B('Devrilmeden dengede kalma','Bir cisim, ağırlık merkezinin düşeyi destek yüzeyinin içinde kaldığı sürece dengededir. Levha ve cisimden oluşan sistemin ortak ağırlık merkezi x = (m₁x₁ + m₂x₂) ÷ (m₁ + m₂) ile bulunur. Örnek: 2 kg ve 4 kg kütleler 0 ve 6 birimde ise ortak merkez 4 birimdedir')],
 ad=[A('Levhanın merkezi','Sol kenardan ölçülür: yatay kol 4 kare, düşey kolun ek 2 karesi sol sütunda.','x₁ = (4 × 2 + 2 × 0,5) ÷ 6 = 1,5 birim'),
     A('Ortak ağırlık merkezi','Levha 6 kg (x = 1,5), cisim 6 kg (x = 3,5).','x = (6 × 1,5 + 6 × 3,5) ÷ 12 = 2,5 birim'),
     A('Sınır koşulu','Devrilmenin sınırında ortak ağırlık merkezi masa kenarının hizasındadır.','Masa kenarı sol uçtan 2,5 birimde'),
     A('Taşma miktarı','Levhanın sağ ucu sol uçtan 4 birimdedir.','4 − 2,5 = 1,5 birim')],
 puf='Devrilme sınırında ortak ağırlık merkezi tam destek kenarının üstündedir; önce ortak merkezi bul.',sekil=SK)

# 11 · iki farklı özkütleli levha · orta
kartla('K-AFAG-11','Farklı özkütleli bölgelerden oluşan levha','Kütle, alan ve özkütlenin çarpımıdır; ağırlık merkezi kütlelerle ağırlıklandırılır ve daha özkütleli bölgeye doğru kayar.','Geometrik merkezi ağırlık merkezi sanmak; kütle oranını alan oranıyla karıştırmak.','orta','şekilli',3,'ag-levha-merkez','Eş karelerden oluşan türdeş levhanın ağırlık merkezi')
cellsL=rect(0,0,3,2); cellsR=rect(3,0,6,2)
mL,mR=len(cellsL)*2,len(cellsR)*1; xL,xR=Fr(3,2),Fr(9,2)
x11=(mL*xL+mR*xR)/(mL+mR); assert x11==Fr(5,2)
assert (mR*xL+mL*xR)/(mL+mR)==Fr(7,2)
fills={c:'vurgu!35' for c in cellsL}; fills.update({c:'gray!15' for c in cellsR})
SK=plate(cellsL|cellsR,fills=fills,u=.7,labels=[f'\\node[font=\\small] at {pt(1.5*.7,1*.7)} {{$2d$}}; \\node[font=\\small] at {pt(4.5*.7,1*.7)} {{$d$}};'])
q('0011',tipId='ag-levha-merkez',tip='Eş karelerden oluşan türdeş levhanın ağırlık merkezi',z='orta',alt='Bileşik Levha',kaz='Farklı özkütleli iki bölgeden oluşan levhanın ağırlık merkezini kütleleri kullanarak bulur.',
 kart='K-AFAG-11 (özkütle 2d ve d) · kütle ağırlıklı ortalama',kalip='şekilli',
 metin='Şekilde, aynı kalınlıktaki iki türdeş levhanın uç uca birleştirilmesiyle oluşturulmuş 6×2’lik bir levha görülmektedir. Sol bölümün özkütlesi 2d, sağ bölümün özkütlesi d’dir. Her bölüm 3×2’lik karelerden oluşur.\n(Kare kenarı = 1 birim)\nBuna göre, levhanın ağırlık merkezinin levhanın sol kenarına uzaklığı kaç birimdir?',
 dogru=Fr(5,2),yan=[(Fr(3,2),'Yalnız sol (daha özkütleli) bölümün merkezini (1,5) ağırlık merkezi sanmış.','dikkat'),
  (3,'Levhanın geometrik merkezini (3) almış; özkütle farkını hesaba katmamış.','bilgi'),
  (Fr(7,2),'Kütleleri ters yazmış: sol bölüme d, sağ bölüme 2d özkütle vermiş.','islem'),
  (Fr(9,2),'Yalnız sağ bölümün merkezini (4,5) ağırlık merkezi sanmış.','dikkat')],
 istenen='Ağırlık merkezinin sol kenara uzaklığı (birim).',
 ip=['Bölümlerin kütle oranını özkütle × alan ile bul.'],
 bilgi=[B('Bileşik cisim','Kütle m = özkütle × hacim (levhada alan); ağırlık merkezi x = Σ(m·x) ÷ Σm. Özkütlesi büyük bölge ağırlık merkezini kendine çeker. Örnek: 3 kg ve 1 kg kütleli parçaların merkezleri 4 birim uzaktaysa ağırlık merkezi ağır parçadan 1 birim uzaktadır')],
 ad=[A('Kütle oranını bul','Alanlar eşit (6 kare), özkütle oranı 2 : 1.','m_sol = 12k, m_sağ = 6k'),
     A('Merkezleri yaz','Sol bölüm merkezi 1,5; sağ bölüm merkezi 4,5.','—'),
     A('Ortalama al','x = (12 × 1,5 + 6 × 4,5) ÷ 18','x = 45 ÷ 18 = 2,5 birim')],
 puf='Özkütleler farklıysa kütle = özkütle × alan; ağırlık merkezi ağır bölgeye daha yakın çıkar.',sekil=SK)

# 12 · dairesel levha · zor
kartla('K-AFAG-12','Dairesel levhadan parça kesip yapıştırma','Dairesel levhada kütle alanla (yarıçapın karesi) orantılıdır; kesilen ve yapıştırılan parçaların momentleri toplanır.','Kütleyi yarıçapla orantılı almak; kesme ve yapıştırmayı tek adımda yazmak.','zor','şekilli',5,'ag-kesme-ekleme','Parça kesilip çıkarılan levhanın ağırlık merkezi')
R,r=12,6
mbig=R*R; msm=r*r; assert mbig==4*msm
x_after_cut=Fr(-(msm*(-r)),mbig-msm)   # kalan: M x = m_k*x_k + m_c*x_c → 4m·0 = 3m x + m(-r) → x=r/3
assert x_after_cut==2
x_new=((mbig-msm)*x_after_cut+msm*(-3*r))/mbig; assert x_new==Fr(-3)
assert abs(x_new)==Fr(R,4)
O=(3,0)
sc=.28; cx=3.3*1;
tk=[f'\\fill[gray!22] (0,0) circle ({R*sc});',f'\\draw[thick] (0,0) circle ({R*sc});',
    f'\\fill[gray!60] ({-r*sc},0) circle ({r*sc});',f'\\draw[thick] ({-r*sc},0) circle ({r*sc});',
    f'\\draw[thick,dashed] ({-3*r*sc},0) circle ({r*sc});',
    f'\\fill (0,0) circle (1.6pt); \\node[above right,inner sep=1pt] at (0,0) {{O}};',
    f'\\draw[{ARR},thick,vurgu] ({-r*sc},{(r+1.1)*sc}) .. controls ({-r*sc},{(r+4.5)*sc}) and ({-3*r*sc},{(r+4.5)*sc}) .. ({-3*r*sc},{(r+1.0)*sc});',
    f'\\draw[<->,thin] (0,{-(R+1.2)*sc}) -- ({R*sc},{-(R+1.2)*sc}); \\node[below] at ({R*sc/2},{-(R+1.2)*sc}) {{$12$ cm}};',
    f'\\draw[<->,thin] ({-2*r*sc},{-(r+1.2)*sc}) -- (0,{-(r+1.2)*sc}); \\node[below] at ({-r*sc},{-(r+1.2)*sc}) {{$12$ cm}};',
    f'\\draw[thin] (0,0) -- ({R*sc},0); \\node[above] at ({R*sc/2},0) {{$12$ cm}};']
# sadeleştir: yalnız R ve r bilgisini ver
tk=tk[:7]+[f'\\draw[thin] (0,0) -- ({R*sc},0); \\node[above,inner sep=1pt] at ({R*sc/2},0) {{$12$ cm}};',
           f'\\draw[thin] ({-r*sc},0) -- ({-r*sc},{r*sc}); \\node[right,inner sep=1pt] at ({-r*sc},{r*sc/2}) {{$6$ cm}};',
           f'\\node[below,align=center] at ({-3*r*sc},{-(r+.4)*sc}) {{yapıştırılacak\\\\yer}};']
SK=tikz_svg(HEAD+'\n'.join(tk)+TAIL)
q('0012',tipId='ag-kesme-ekleme',tip='Parça kesilip çıkarılan levhanın ağırlık merkezi',z='zor',alt='Dairesel Levha',kaz='Dairesel levhadan kesilip başka yere yapıştırılan parçanın ağırlık merkezini nasıl kaydırdığını hesaplar.',
 kart='K-AFAG-12 (R = 2r disk, kesip dışa yapıştırma) · kütle ∝ alan',kalip='şekilli',
 metin='Yarıçapı 12 cm olan ince, türdeş dairesel bir levhanın merkezi O noktasıdır. Levhanın sol kenarına içten teğet olan, yarıçapı 6 cm’lik taralı dairesel parça kesilip çıkarılıyor ve levhanın sol kenarına bu kez dıştan teğet olacak biçimde (şekilde kesikli çizgiyle gösterilen yere) yapıştırılıyor.\nBuna göre, son durumda levhanın ağırlık merkezi O noktasından kaç cm uzaklıktadır?',
 dogru=3,yan=[(2,'Yalnız parçanın kesilmesinden sonraki kayma miktarını (r ÷ 3 = 2 cm) bulmuş; yapıştırma işlemini hesaba katmamış.','dikkat'),
  (4,'Kesilen parçanın kütlesini levhanın üçte biri kabul ederek (yanlış kütle oranıyla) kaymayı 4 cm bulmuş.','bilgi'),
  (6,'Kütleyi alanla değil yarıçapla orantılı alıp (2m ve m) 6 cm bulmuş.','bilgi'),
  (9,'Yapıştırılan parçanın merkezinin O’ya uzaklığının (18 cm) yarısını almış.','islem')],
 istenen='Son durumda ağırlık merkezinin O’ya uzaklığı (cm).',
 ip=['Önce kesilen parçanın kütlesini büyük levhanın kütlesiyle alan oranından karşılaştır; sonra parçayı yeni yerine koyduğunda momentleri topla.'],
 bilgi=[B('Alan–kütle ilişkisi','Türdeş ince levhada kütle alanla orantılıdır. Dairede alan yarıçapın karesiyle artar: yarıçap 2 katına çıkarsa kütle 4 katı olur. Örnek: 2r yarıçaplı levhadan r yarıçaplı parça çıkarılırsa kalan kütle toplamın 3 ÷ 4’üdür')],
 ad=[A('Kütle oranını yaz','Alan ∝ yarıçapın karesi.','Büyük levha 4m, küçük parça m, kalan 3m'),
     A('Kesilince ağırlık merkezi','O’yu başlangıç, sol yönü negatif al; küçük parçanın merkezi −6 cm.','4m × 0 = 3m × x + m × (−6) → x = +2 cm'),
     A('Parça yeni yerine konunca','Küçük parçanın yeni merkezi sol kenarın 6 cm dışında: x = −12 − 6 = −18 cm.','4m × X = 3m × 2 + m × (−18)'),
     A('Hesapla','4X = 6 − 18','X = −3 cm'),
     A('Sonuç','Ağırlık merkezi O’nun 3 cm soludadır.','Uzaklık: 3 cm')],
 puf='Kesme ve yapıştırmada her adımda toplam moment korunur; dairede kütle oranı alan (yarıçapın karesi) oranıdır.',sekil=SK)

# 13 · noktasal kütleler · kolay
kartla('K-AFAG-13','Noktasal kütle sisteminin kütle merkezi','Kütle merkezi x = Σ m·x ÷ Σ m ile bulunur; ağır cisme daha yakındır.','Basit ortalama almak; toplam kütleye bölmeyi unutmak.','kolay','şekilli',3,'ag-noktasal','Noktasal kütle sisteminin kütle merkezi')
ms=[(1,0),(2,3),(3,6)]; x13=Fr(sum(m*x for m,x in ms),6); assert x13==4
assert sum(m*x for m,x in ms)==24
nl=[f'\\draw[{ARR}] (-.4,0) -- (6.0,0);']
u13=.9
nl=[f'\\draw[{ARR},thick] (-.5,0) -- ({6.6*u13+.5},0);']
for m,x in ms:
    nl.append(f'\\draw[thick,fill=gray!30] {pt(x*u13-.4,.05)} rectangle {pt(x*u13+.4,.65)}; \\node at {pt(x*u13,.35)} {{\\footnotesize ${m}$ kg}};')
for t in range(0,7):
    nl.append(f'\\draw {pt(t*u13,-.08)} -- {pt(t*u13,.08)}; \\node[below,inner sep=2pt] at {pt(t*u13,-.08)} {{\\footnotesize ${t}$}};')
nl.append(f'\\node[right] at {pt(6.6*u13+.55,0)} {{$x$ (m)}};')
SK=tikz_svg(HS(1.2)+'\n'.join(nl)+TAIL)
q('0013',tipId='ag-noktasal',tip='Noktasal kütle sisteminin kütle merkezi',z='kolay',alt='Kütle Merkezi',kaz='Doğru üzerinde bulunan noktasal kütlelerden oluşan sistemin kütle merkezinin konumunu hesaplar.',
 kart='K-AFAG-13 (1-2-3 kg, 0-3-6 m) · Σmx ÷ Σm',kalip='şekilli',
 metin='Sürtünmesiz yatay bir doğru üzerinde, kütleleri 1 kg, 2 kg ve 3 kg olan üç küçük cisim x ekseni üzerinde şekildeki konumlarda durmaktadır.\nBuna göre, bu cisimlerden oluşan sistemin kütle merkezi x ekseninde kaç m’dedir?',
 dogru=4,yan=[(Fr(9,2),'Yalnız en büyük iki kütlenin konumlarının ortalamasını almış: (3 + 6) ÷ 2 = 4,5 m.','dikkat'),
  (24,'Momentler toplamını (1 × 0 + 2 × 3 + 3 × 6 = 24) toplam kütleye bölmeden doğrudan kütle merkezi sanmış.','islem'),
  (8,'Momentler toplamını (24) cisim sayısına (3) bölmüş.','islem'),
  (12,'Momentler toplamını (24) 2’ye bölmüş; toplam kütleyi (6 kg) kullanmamış.','islem')],
 istenen='Kütle merkezinin konumu (m).',
 ip=['Her kütleyi konumuyla çarpıp topla; sonra toplam kütleye böl.'],
 bilgi=[B('Kütle merkezi','Noktasal kütlelerin kütle merkezi x_cm = (m₁x₁ + m₂x₂ + …) ÷ (m₁ + m₂ + …) ile bulunur. Örnek: 1 kg ve 3 kg kütleler 0 ve 4 m’de ise x_cm = (0 + 12) ÷ 4 = 3 m')],
 ad=[A('Momentleri yaz','Her kütlenin konumla çarpımı.','1 × 0 + 2 × 3 + 3 × 6 = 24'),
     A('Toplam kütle','1 + 2 + 3 = 6 kg','—'),
     A('Böl','x_cm = 24 ÷ 6','x_cm = 4 m')],
 puf='Kütle merkezi, kütle ağırlıklı ortalamadır; ağır cisme yaklaşır.',sekil=SK)

# 14 · ip kopması, kütle merkezi ivmesi · zor öncüllü
kartla('K-AFAG-14','Dış kuvvet ve kütle merkezinin ivmesi','Sistemin kütle merkezi yalnız dış kuvvetin bileşkesiyle ivmelenir: F_net = M·a_cm; iç kuvvetler (ip gerilmesi) kütle merkezinin ivmesini değiştirmez.','Kopan ipin kütle merkezinin ivmesini değiştirdiğini sanmak; ip koptuktan sonra L’ye kuvvet uygulanmaya devam ettiğini düşünmek.','zor','öncüllü',5,'ag-merkez-hareket','Kütle merkezinin hareketi')
mK,mL,F14=2,4,12
a_before=Fr(F14,mK+mL); assert a_before==2
aK_after=Fr(F14,mK); aL_after=0; assert aK_after==6
acm_after=(mK*aK_after+mL*aL_after)/(mK+mL); assert acm_after==2
tr14=[acm_after==2,aK_after==6,aL_after==2]; assert tr14==[True,True,False]
dg,yn,sr=onc(tr14,['İp koptuğunda kütle merkezinin ivmesini F ÷ (m_K + m_L) = 2 m/s² olarak bulamamış.','İp koptuktan sonra K’ye yalnız 12 N’un etki ettiğini (a = 12 ÷ 2 = 6 m/s²) görememiş.',''],['','','İp koptuktan sonra L’nin de 2 m/s² ivmelendiğini sanmış; L’ye artık bileşke kuvvet etki etmez, ivmesi sıfırdır.'],(1,5))
car=lambda x,lab,w: f'\\draw[thick,fill=gray!25] {pt(x,.25)} rectangle {pt(x+w,.95)}; \\node at {pt(x+w/2,.6)} {{{lab}}}; \\draw[thick,fill=white] {pt(x+.2,.25)} circle (.17) {pt(x+w-.2,.25)} circle (.17);'
cl=[f'\\draw[thick] (-.4,.08) -- (6.4,.08);',car(0.2,'L: $4$ kg',1.7),car(3.4,'K: $2$ kg',1.3),
    f'\\draw[thick] (1.9,.7) -- (3.4,.7); \\node[above,font=\\footnotesize] at (2.65,.7) {{ip}};',
    f'\\draw[vurgu,very thick,{ARR}] (4.7,.6) -- (6.3,.6); \\node[vurgu,above] at (5.4,.7) {{$F=12$ N}};']
SK=tikz_svg(HS(1.2)+'\n'.join(cl)+TAIL)
q('0014',tipId='ag-merkez-hareket',tip='Kütle merkezinin hareketi',z='zor',alt='Kütle Merkezi Hareketi',kaz='Dış kuvvet etkisindeki sistemin kütle merkezinin ivmesini, iç kuvvetlerin etkisiz olduğunu kullanarak yorumlar.',
 kart='K-AFAG-14 (2 kg + 4 kg, ip kopuyor, F = 12 N) · a_cm = F ÷ M',kalip='öncüllü',
 metin='Sürtünmesiz yatay zeminde durmakta olan kütleleri 4 kg olan L ve 2 kg olan K arabaları, hafif ve esnemez bir iple birbirine bağlanmıştır. K arabasına, şekildeki gibi yatay ve sabit büyüklükte 12 N’luk F kuvveti uygulanıyor; sistem hareket ederken bir süre sonra ip kopuyor. İp koptuktan sonra F kuvveti aynı büyüklükte K’ye etki etmeye devam ediyor.\nBuna göre, ip koptuktan sonra,\nI. L ve K arabalarından oluşan sistemin kütle merkezinin ivmesi 2 m/s²’dir.\nII. K’nin ivmesi 6 m/s²’dir.\nIII. L’nin ivmesi 2 m/s²’dir.\nyargılarından hangileri doğrudur?',
 dogru=dg,yan=yn,sira=sr,istenen='İp koptuktan sonra doğru olan yargılar.',
 ip=['Kütle merkezinin ivmesini yalnızca dış kuvvet belirler; ip koptuktan sonra her arabaya etki eden kuvveti ayrı ayrı yaz.'],
 bilgi=[B('Kütle merkezinin ivmesi','Sistem üzerindeki dış kuvvetlerin bileşkesi F_net = (m₁ + m₂ + …)·a_cm ile kütle merkezinin ivmesini verir; ip gerilmesi gibi iç kuvvetler bu ivmeyi etkilemez. Örnek: 6 kg’lık sisteme 12 N dış kuvvet uygulanırsa kütle merkezi 2 m/s² ile hızlanır')],
 ad=[A('Kütle merkezinin ivmesi','Dış kuvvet yalnız F; iç kuvvetler ivmeyi değiştirmez.','a_cm = 12 ÷ (2 + 4) = 2 m/s² → I: doğru'),
     A('K’nin ivmesi','İp koptuktan sonra K’ye yalnız F etki eder.','a_K = 12 ÷ 2 = 6 m/s² → II: doğru'),
     A('L’nin ivmesi','L’ye etki eden yatay kuvvet kalmaz (sürtünme yok).','a_L = 0 → III: yanlış'),
     A('Kontrol et','Kütle merkezinin ivmesini parçalardan hesapla.','(2 × 6 + 4 × 0) ÷ 6 = 2 m/s² ✓'),
     A('Sonuç','Doğru yargılar I ve II.','Cevap: '+dg)],
 puf='Kütle merkezinin ivmesi yalnız dış kuvvete bağlıdır; ip kopsa bile F ÷ M değişmez.',sekil=SK)

# 15 · buzda iki kişi · orta öncüllü
kartla('K-AFAG-15','Dış kuvvet yokken kütle merkezi sabittir','Dış kuvvetin bileşkesi sıfırsa sistemin kütle merkezi durgunsa durgun kalır; iç kuvvetlerle çekilen cisimler kütle merkezinde buluşur, daha hafif olan daha çok yol alır.','Eşit yol aldıklarını sanmak; kütle merkezinin ağır cisimle birlikte hareket ettiğini düşünmek.','orta','öncüllü',4,'ag-merkez-hareket','Kütle merkezinin hareketi')
m60,m40,D=60,40,10
xc=Fr(m60*0+m40*D,m60+m40); assert xc==4
tr15=[True,xc==4,False]; assert Fr(D)-xc==6 and tr15==[True,True,False]
dg,yn,sr=onc(tr15,['Dış kuvvet olmadığı için kütle merkezinin durgun kaldığını fark edememiş.','Buluşma noktasının kütle merkezi olduğunu ve 60 kg’lık kişinin 4 m yol aldığını bulamamış.',''],['','','Karşılıklı çekme kuvvetleri eşit olduğundan ivmelerin de eşit olduğunu sanmış; ivme kütleyle ters orantılıdır.'],(4,5))
pl=[f'\\draw[thick] (-.3,0) -- (7.8,0);']
for x,m,lab in [(0.0,60,'$60$ kg'),(7.0,40,'$40$ kg')]:
    pl.append(f'\\draw[thick,fill=gray!30] {pt(x,0)} rectangle {pt(x+1.0,.7)}; \\node at {pt(x+.5,.35)} {{\\footnotesize {lab}}};')
pl.append('\\draw[thick] (1.0,.35) -- (7.0,.35);')
pl.append('\\draw[<->,thin] (0.5,-.35) -- (7.5,-.35); \\node[below] at (4.0,-.35) {$10$ m};')
SK=tikz_svg(HS(1.2)+'\n'.join(pl)+TAIL)
q('0015',tipId='ag-merkez-hareket',tip='Kütle merkezinin hareketi',z='orta',alt='Kütle Merkezi Hareketi',kaz='Sürtünmesiz zeminde iç kuvvetle birbirini çeken cisimlerin kütle merkezinin sabit kaldığını kullanır.',
 kart='K-AFAG-15 (60 kg + 40 kg, buz, 10 m) · kütle merkezi sabit',kalip='öncüllü',
 metin='Sürtünmesiz buz üzerinde birbirinden 10 m uzaklıkta durgun duran 60 kg ve 40 kg kütleli iki kişi, aralarındaki hafif ve esnemez bir ipi çekerek birbirine yaklaşıyor. Kişiler küçük cisimler gibi düşünülecektir.\nBuna göre,\nI. Sistemin kütle merkezi hareket etmez.\nII. 60 kg kütleli kişi, ilk konumundan 4 m uzakta 40 kg kütleli kişiyle karşılaşır.\nIII. Kişilerin ivmelerinin büyüklükleri birbirine eşittir.\nyargılarından hangileri doğrudur?',
 dogru=dg,yan=yn,sira=sr,istenen='Doğru olan yargılar.',
 ip=['Dış kuvvet var mı? Yoksa kütle merkezinin konumu ilk andaki konumunda kalır; buluşma noktasını da kütle merkezi belirler.'],
 bilgi=[B('Kütle merkezinin korunumu','Sisteme yatay dış kuvvet etki etmiyorsa ve sistem durgunsa kütle merkezi yerinden oynamaz. İç kuvvetler eşit büyüklükte olduğundan ivmeler kütleyle ters orantılıdır. Örnek: 1 kg ve 3 kg kütleler 8 m ara ile buluşursa 1 kg’lık 6 m, 3 kg’lık 2 m yol alır')],
 ad=[A('I. yargı','Yatay dış kuvvet yok (zemin sürtünmesiz); kütle merkezi durgun kalır.','I: doğru'),
     A('Kütle merkezini bul','60 kg’lık kişiden başlayarak ölç.','x_cm = (60 × 0 + 40 × 10) ÷ 100 = 4 m'),
     A('II. yargı','İki kişi kütle merkezinde buluşur; 60 kg’lık kişi 4 m yol alır.','II: doğru'),
     A('III. yargı','Çekme kuvvetleri eşit, kütleler farklıdır: a = F ÷ m.','a₁ : a₂ = 40 : 60 → III: yanlış'),
     A('Sonuç','Doğru yargılar I ve II.','Cevap: '+dg)],
 puf='Dış kuvvet yoksa kütle merkezi sabittir; birbirini çeken cisimler kütle merkezinde buluşur.',sekil=SK)

# 16 · çubuk + cisim · öncüllü orta
kartla('K-AFAG-16','Homojen çubuk ve noktasal kütle','Homojen çubuk kütlesini orta noktasında toplar; eklenen cisimle birlikte kütle merkezi kütlelerin ağırlıklı ortalamasıdır.','Çubuğun ağırlığını yok saymak; ağırlık merkezini çubuğun orta noktası sanmak.','orta','öncüllü',4,'ag-noktasal','Noktasal kütle sisteminin kütle merkezi')
mrod,Lr,mb=6,8,2
xrod=Fr(Lr,2); xcm16=(mrod*xrod+mb*Lr)/(mrod+mb); assert xcm16==5
xcm_wo=xrod; tr16=[xcm16>xrod,abs(Lr-xcm16)<abs(xrod-xcm16),xcm16-xrod==1]
assert tr16==[True,False,True]
dg,yn,sr=onc(tr16,['Cisimden dolayı kütle merkezinin çubuğun orta noktasından sağa kaydığını görememiş.','',' Cisim kaldırılınca merkezin 1 birim sola kayacağını bulamamış.'.strip()],['','Kütle merkezinin cisme, çubuğun orta noktasına olduğundan daha yakın olduğunu sanmış; oysa 5 m’deki merkez orta noktaya 1 m, cisme 3 m uzaktadır.',''],(4,5))
rod=['\\draw[thick,fill=gray!25] (0,.25) rectangle (6.4,.55);','\\draw[thick,fill=gray!50] (6.2,.55) rectangle (6.6,.95); \\node[right] at (6.65,.75) {$2$ kg};',
     '\\fill (0,.4) circle (1.2pt);']
rod+=[f'\\draw[thin] ({t*.8},.25) -- ({t*.8},.1); \\node[below,inner sep=1pt,font=\\scriptsize] at ({t*.8},.1) {{${t}$}};' for t in range(0,9)]
rod+=['\\draw[<->,thin] (0,1.2) -- (6.4,1.2); \\node[above] at (3.2,1.2) {$8$ m};','\\node at (3.2,.4) {\\footnotesize $6$ kg};']
SK=tikz_svg(HS(1.2)+'\n'.join(rod)+TAIL)
q('0016',tipId='ag-noktasal',tip='Noktasal kütle sisteminin kütle merkezi',z='orta',alt='Kütle Merkezi',kaz='Homojen çubuk ve üzerine konan cismin oluşturduğu sistemin kütle merkezini yorumlar.',
 kart='K-AFAG-16 (6 kg çubuk, 8 m, ucunda 2 kg) · Σmx ÷ Σm',kalip='öncüllü',
 metin='Kütlesi 6 kg ve uzunluğu 8 m olan homojen bir çubuğun sağ ucuna şekildeki gibi küçük, 2 kg kütleli bir cisim yapıştırılmıştır. Çubuğun sol ucu başlangıç noktası olarak alınıyor.\nBuna göre,\nI. Çubuk–cisim sisteminin kütle merkezi, çubuğun orta noktasının sağındadır.\nII. Sistemin kütle merkezi, cisme çubuğun orta noktasına olduğundan daha yakındır.\nIII. Cisim sistemden çıkarılırsa kalan çubuğun kütle merkezi, sistemin ilk kütle merkezinin 1 m solunda olur.\nyargılarından hangileri doğrudur?',
 dogru=dg,yan=yn,sira=sr,istenen='Doğru olan yargılar.',
 ip=['Çubuğu, tüm kütlesi orta noktasında toplanmış bir cisim gibi düşün.'],
 bilgi=[B('Homojen çubuk','Homojen çubuğun kütle merkezi orta noktasıdır. Sistemin merkezi x = (m₁x₁ + m₂x₂) ÷ (m₁ + m₂) ile bulunur. Örnek: 2 kg’lık çubuk (orta noktası 1 m) ucuna 2 kg cisim eklenirse merkez 1,5 m olur')],
 ad=[A('Konumları yaz','Çubuk 6 kg orta noktasında (4 m), cisim 2 kg 8 m’de.','—'),
     A('Kütle merkezini bul','x = (6 × 4 + 2 × 8) ÷ 8','x = 40 ÷ 8 = 5 m'),
     A('Yargıları sına','I: 5 m > 4 m doğru. II: cisme uzaklık 3 m, orta noktaya 1 m → yanlış. III: çubuğun tek başına merkezi 4 m, sistemin merkezi 5 m; 5 − 4 = 1 m sol → doğru.','I: doğru · II: yanlış · III: doğru'),
     A('Sonuç','Doğru yargılar I ve III.','Cevap: '+dg)],
 puf='Homojen çubuğu orta noktasındaki tek kütle olarak yaz; merkez ağır tarafa yakın çıkar.',sekil=SK)

# 17 · kesip yapıştırma yükseklik · zor
kartla('K-AFAG-17','Kesilip yeniden yapıştırılan parça','Toplam kütle korunur; parçanın kaydırılmasıyla ağırlık merkezi, kütle oranı × kayma miktarı kadar aynı yönde yer değiştirir.','Kütle merkezinin değişmediğini sanmak; kaymayı toplam kütle yerine parça kütlesine bölmek.','orta','şekilli',5,'ag-kesme-ekleme','Parça kesilip çıkarılan levhanın ağırlık merkezi')
S17=rect(0,0,6,4); piece=rect(0,0,3,2); new=rect(0,4,3,6)
new_cells=(S17-piece)|new; y17=cm(new_cells)[1]; assert y17==3 and cm(S17)[1]==2
assert Fr(len(piece)*4,24)==1
fo=[f'\\draw[thick,dashed,vurgu] {pt(0,4*.55)} rectangle {pt(3*.55,6*.55)};',
    f'\\draw[{ARR},thick,vurgu] {pt(1.5*.55,2*.55)} -- {pt(1.5*.55,4*.55+.45)};',
    f'\\node[right,font=\\footnotesize] at {pt(3*.55+.05,5*.55)} {{yapıştırılacak yer}};',
    f'\\draw[<->,thin] {pt(-.25,0)} -- {pt(-.25,4*.55)}; \\node[left,inner sep=1pt] at {pt(-.25,2*.55)} {{$4$ birim}};']
SK=plate(S17,hatch=piece,extra=fo,u=.55)
q('0017',tipId='ag-kesme-ekleme',tip='Parça kesilip çıkarılan levhanın ağırlık merkezi',z='orta',alt='Kesme ve Yapıştırma',kaz='Bir levhadan kesilen parçanın başka yere yapıştırılmasıyla ağırlık merkezinin yer değiştirmesini hesaplar.',
 kart='K-AFAG-17 (6×4 levha, 3×2 parça yukarı taşınıyor) · Δy = m·d ÷ M',kalip='şekilli',
 metin='Şekilde eş karelerden oluşan 6×4’lük türdeş bir levha görülmektedir. Levhanın sol alt köşesindeki 3×2’lik taralı parça kesilip çıkarılıyor ve levhanın üst kenarına, şekilde kesikli çizgilerle gösterilen yere (aynı sütunlar, üstte) yapıştırılıyor.\n(Kare kenarı = 1 birim)\nBuna göre, son durumda levhanın ağırlık merkezi alt kenardan kaç birim yukarıdadır?',
 dogru=3,yan=[(2,'Parçanın yerinin değişmesinin ağırlık merkezini etkilemediğini sanmış; ilk yüksekliği (2) yazmış.','bilgi'),
  (Fr(5,2),'Parçanın yer değiştirmesini 2 birim (yalnız parça yüksekliği) alarak 2 + 6 × 2 ÷ 24 = 2,5 bulmuş.','islem'),
  (Fr(7,2),'İlk merkez (2) ile parçanın yeni merkezinin (5) ortalamasını almış: (2 + 5) ÷ 2.','bilgi'),
  (4,'Parçanın yer değiştirme miktarını (4 birim) ağırlık merkezinin kayması sanıp ilk yüksekliğe eklememiş; doğrudan 4 yazmış.','dikkat')],
 istenen='Ağırlık merkezinin alt kenardan yüksekliği (birim).',
 ip=['Parça taşındığında kütle toplamının değişmediğini, yalnız konumunun değiştiğini kullanarak ağırlık merkezinin nasıl kaydığını düşün.'],
 bilgi=[B('Parça taşıma','Toplam kütlesi M olan cismin m kütleli parçası d kadar kaydırılırsa ağırlık merkezi aynı yönde Δ = m·d ÷ M kadar yer değiştirir. Örnek: 4 kütleli levhanın 1 kütleli parçası 2 birim kaydırılırsa merkez 0,5 birim kayar')],
 ad=[A('Kütleleri yaz','Tüm levha 24 kare, taşınan parça 6 kare.','m ÷ M = 1 ÷ 4'),
     A('Parçanın kayma miktarı','Parça 4 birim yukarı taşınıyor (2 yükseklikli bölgeden 4 yukarı).','d = 4 birim'),
     A('Ağırlık merkezinin kayması','Δy = m·d ÷ M','Δy = 6 × 4 ÷ 24 = 1 birim'),
     A('Yeni yükseklik','İlk yükseklik 2 birimdi.','y = 2 + 1 = 3 birim')],
 puf='Kütlesi m olan parça d kadar taşınırsa ağırlık merkezi m·d ÷ M kadar kayar; hesabı tek satırda yap.',sekil=SK)

# 18 · asılı dikdörtgen levha · orta
kartla('K-AFAG-18','Köşesinden asılan dikdörtgen levha','Askı noktasından ağırlık merkezine çizilen doğru denge durumunda düşeydir; levhanın kenarının düşeyle yaptığı açı köşegen–kenar açısıdır.','Düşeyin levhanın kenarıyla çakıştığını sanmak; kısa ve uzun kenarı karıştırmak.','orta','şekilli',4,'ag-asma','İple asılan levhanın dengesi')
a18,b18=8,6; diag=5
ux,uy=-.6,-.8; vx,vy=.8,-.6
cx18=(a18*ux+b18*vx)/2; cy18=(a18*uy+b18*vy)/2; assert abs(cx18)<1e-12 and abs(cy18+5)<1e-12
u18=.42
P0=(0,0)
Cs=[P0,(a18*ux,a18*uy),(a18*ux+b18*vx,a18*uy+b18*vy),(b18*vx,b18*vy)]
o=[f'\\draw[thick,fill=gray!22] '+' -- '.join(pt(x*u18,y*u18) for x,y in Cs)+' -- cycle;']
for k in range(1,a18):
    o.append(f'\\draw[very thin,dashed,gray] {pt((k*ux)*u18,(k*uy)*u18)} -- {pt((k*ux+b18*vx)*u18,(k*uy+b18*vy)*u18)};')
for k in range(1,b18):
    o.append(f'\\draw[very thin,dashed,gray] {pt((k*vx)*u18,(k*vy)*u18)} -- {pt((k*vx+a18*ux)*u18,(k*vy+a18*uy)*u18)};')
o.append(f'\\draw[thick] {pt(0,0)} -- {pt(0,1.0)}; \\draw[thick] (-.7,1.0) -- (.7,1.0);')
o.append(f'\\fill {pt(0,0)} circle (1.8pt); \\node[right,inner sep=3pt] at {pt(0,.5)} {{ip}};')
mid_long=((a18*ux/2),(a18*uy/2)); mid_short=((b18*vx/2),(b18*vy/2))
o.append(f'\\node[font=\\footnotesize,left,inner sep=3pt] at {pt(mid_long[0]*u18,mid_long[1]*u18)} {{$8$ birim}};')
o.append(f'\\node[font=\\footnotesize,right,inner sep=3pt] at {pt(mid_short[0]*u18,mid_short[1]*u18)} {{$6$ birim}};')
SK=tikz_svg(HS(1.25)+'\n'.join(o)+TAIL)
q('0018',tipId='ag-asma',tip='İple asılan levhanın dengesi',z='orta',alt='Asılı Levha',kaz='Köşesinden iple asılan dikdörtgen levhanın denge durumunda kenarlarının düşeyle yaptığı açıyı bulur.',
 kart='K-AFAG-18 (6×8 dikdörtgen levha, köşeden asılı) · tan θ = 3 ÷ 4',kalip='şekilli',
 metin='Kenar uzunlukları 8 birim ve 6 birim olan türdeş, ince dikdörtgen bir levha, bir köşesinden düşey bir ipe bağlanarak düşey düzlemde serbestçe dönebilecek biçimde asılmıştır. Levha şekildeki gibi dengededir; ızgara çizgileri 1 birim aralıklıdır.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre, levhanın 8 birimlik kenarı, düşeyle kaç derecelik açı yapar?',
 dogru=37,yan=[(30,'Açıyı bilinen özel açılardan biri (30°) sanmış; dik üçgenin kenar oranını (3, 4, 5) kullanmamış.','bilgi'),
  (45,'Ağırlık merkezinin köşegen üzerinde olduğunu, levhanın düşeyle 45° yaptığını sanmış.','bilgi'),
  (53,'8 birimlik kenar yerine 6 birimlik kenarın düşeyle yaptığı açıyı bulmuş.','dikkat'),
  (60,'Köşegenin kenarlarla yaptığı açıyı özel açı (60°) sanmış.','bilgi')],
 istenen='8 birimlik kenarın düşeyle yaptığı açı (derece).',
 ip=['Denge durumunda ipin doğrultusu levhanın ağırlık merkezinden geçer; ağırlık merkezi dikdörtgenin köşegenlerinin kesişimindedir.'],
 bilgi=[B('Asılı cismin dengesi','Asılan cismin ağırlık merkezi askı noktasının hemen altında, aynı düşey doğru üzerindedir. Dikdörtgen levhanın ağırlık merkezi köşegenlerin kesim noktasıdır. Örnek: 3–4–5 üçgeninde 3 birimlik kenarın karşısındaki açı 37°’dir')],
 ad=[A('Ağırlık merkezi','Dikdörtgenin merkezi, asıldığı köşeden köşegenin yarısı kadar uzaktadır.','Köşegen = √(8² + 6²) = 10 → 5 birim'),
     A('İp doğrultusu','İp, askı köşesi ile ağırlık merkezinden geçer; yani düşey doğru köşegenin üzerindedir.','Düşey doğru = köşegen'),
     A('Dik üçgen kur','Yarım köşegen 5, yarı kenarlar 4 ve 3.','cos θ = 4 ÷ 5 = 0,8'),
     A('Açıyı bul','8 birimlik kenar ile köşegen arasındaki açı θ.','θ = 37°')],
 puf='Asılı levhada köşegenin yarısı düşeydir; kenarın düşeyle açısı köşegenle kenar arasındaki açıdır.',sekil=SK)

# 19 · kesilmiş levha, asma noktası · zor
kartla('K-AFAG-19','Kesilmiş levhanın asma noktası','Levhanın üst kenarının yatay kalması için askı noktası, ağırlık merkezinin düşeyi üzerinde olmalıdır; kesilen parçalar bu düşeyi değiştirir.','Kesilmeden önceki levhanın merkezine göre asmak; kesilen parçanın merkezine göre simetriği almak.','zor','şekilli',5,'ag-asma','İple asılan levhanın dengesi')
S19=rect(0,0,6,4)-(rect(0,0,2,3)|rect(2,0,4,3)); c19=cm(S19); assert c19==(4,Fr(5,2)) and len(S19)==12
pxs={'K':1,'L':2,'M':3,'N':4,'P':5}
mk19=[(L,x,4,'above') for L,x in pxs.items()]
SK=plate(S19,hatch=(rect(0,0,2,3)|rect(2,0,4,3)),marks=mk19,u=.55,extra=[f'\\draw[thin,gray] {pt(2*.55,0)} -- {pt(2*.55,3*.55)};'])
q('0019',tipId='ag-asma',tip='İple asılan levhanın dengesi',z='zor',alt='Asılı Levha',kaz='Kesilmiş levhanın ağırlık merkezini bulup üst kenarı yatay tutacak askı noktasını belirler.',
 kart='K-AFAG-19 (6×4 levhadan iki 2×3 parça kesilmiş) · üst kenardan askı',kalip='şekilli',
 metin='Şekilde eş karelerden oluşan 6×4’lük türdeş bir levha görülmektedir. Levhadan taralı iki parça (her biri 2×3’lük) kesilip atılıyor. Kalan levha, üst kenarındaki K, L, M, N ve P noktalarından birinden düşey bir iple bağlanıp düşey düzlemde serbestçe dönebilecek biçimde asılacaktır.\nBuna göre, levhanın üst kenarının dengede yatay kalması için ip hangi noktaya bağlanmalıdır?',
 dogru='N',yan=[('K','Yalnız üst şeridin sol sütununun merkezini (x = 1) ağırlık merkezinin yatay konumu sanmış.','dikkat'),
  ('L','Kesilen parçaların sol parçasının sağ kenarını (x = 2) seçmiş; kalan levhanın merkezini hesaplamamış.','dikkat'),
  ('M','Kesilmeden önceki levhanın ağırlık merkezinin düşeyini (x = 3) seçmiş.','bilgi'),
  ('P','Sağdaki dikdörtgen kolun merkezini (x = 5) ağırlık merkezinin yatay konumu sanmış.','bilgi')],sira=['K','L','M','N','P'],
 istenen='İpin bağlanacağı nokta.',
 ip=['Kalan levhanın ağırlık merkezinin yatay konumunu bul; ip bu düşey doğrultuda olmalıdır.'],
 bilgi=[B('Asma noktası','Levha, ağırlık merkezinin düşeyinden asılırsa dönmez ve şekli dengede bozulmadan durur. Kalan levhanın merkezi, tam levhadan kesilen parçaların momentleri çıkarılarak bulunur. Örnek: 2 kütleli parçaya x = 1 ve 4 kütleli parçaya x = 4 verilirse bileşke x = 3 konumundadır')],
 ad=[A('Kütleleri yaz','Tam levha 24 kare, kesilen 12 kare, kalan 12 kare.','Kalan: üst şerit (6 kare) + sağ kol (6 kare)'),
     A('Merkezleri yaz','Üst satırın merkezi x = 3; sağ kolun (alt üç satır) merkezi x = 5.','Üst şerit: 6 kare, x = 3 · sağ kol (alt üç satır): 6 kare, x = 5'),
     A('Ağırlıklı ortalama','x = (6 × 3 + 6 × 5) ÷ 12','x = 48 ÷ 12 = 4'),
     A('Noktayı bul','Üst kenarda x = 4 noktası.','Cevap: N')],
 puf='Kalan levhanın merkezinin yatay konumunu bul; asma noktası tam onun üstündeki üst kenar noktasıdır.',sekil=SK)

# 20 · Z biçimli tel · zor
kartla('K-AFAG-20','Üç parçalı katlanmış tel','Bir telin ağırlık merkezi, dik katlanan parçaların orta noktalarının uzunlukla ağırlıklı ortalamasıdır; sonuç genelde tel üzerinde değildir.','Parçaların orta noktalarını yanlış yazmak; kenarları eşit kütleli saymak.','zor','şekilli',5,'ag-tel','Bükülmüş türdeş telin ağırlık merkezi')
pts20=[(0,0),(4,0),(4,6),(6,6)]; seg20=seglist(pts20); c20=wcm(seg20); assert c20==(Fr(7,2),Fr(5,2)) and sum(s[0] for s in seg20)==12
pos,dog,yan,sira=pts_choice(c20,[
 ((3,3),'Telin sınırlayıcı dikdörtgeninin ortasını (3; 3) seçmiş.','bilgi'),
 ((4,3),'Ortadaki parçanın merkezini (4; 3) ağırlık merkezi sanmış.','dikkat'),
 ((Fr(5,2),Fr(5,2)),'Yatay koordinatı tersine (6 − 3,5) alarak 2,5 bulmuş.','islem'),
 ((Fr(7,2),Fr(7,2)),'Düşey koordinat için kısa yatay parçanın uzunluğunu yanlış (4 yerine 2 ve 4) kullanmış: y = 3,5.','islem')],0)
SK=wirefig([pts20],marks=[(L,pos[L][0],pos[L][1],{'K':'below left','L':'above left','M':'right','N':'left','P':'above left'}[L]) for L in 'KLMNP'],W=7,Hh=7,u=.6,k=1.3)
q('0020',tipId='ag-tel',tip='Bükülmüş türdeş telin ağırlık merkezi',z='zor',alt='Tel',kaz='Üç parçalı biçimde bükülmüş türdeş telin ağırlık merkezini uzunluklarla ağırlıklı ortalamadan bulur.',
 kart='K-AFAG-20 (4 + 6 + 2 birimlik Z tel) · Σℓx ÷ Σℓ',kalip='şekilli',
 metin='Uzunluğu 12 birim olan türdeş ve ince bir tel, bir ucundan 4 birim uzaklıkta ve 10 birim uzaklıkta dik açıyla katlanarak şekildeki gibi üç doğrusal parçalı bir biçime getirilmiştir. Tel ızgara üzerinde duruyor; K, L, M, N ve P noktaları ızgara çizgilerinin kesişim noktalarında, kare merkezlerinde ya da kare kenarlarının orta noktalarındadır.\nBuna göre, telin ağırlık merkezi hangi noktadadır?',
 dogru=dog,yan=yan,sira=sira,istenen='Telin ağırlık merkezinin bulunduğu nokta.',
 ip=['Üç parçayı uzunlukları kadar kütle olarak düşün ve her parçanın orta noktasının koordinatını yaz.'],
 bilgi=[B('Parçalı tel','Tel parçalara ayrılır; her parçanın kütlesi uzunluğu, merkezi orta noktasıdır. x_cm = Σℓx ÷ Σℓ, y_cm = Σℓy ÷ Σℓ. Örnek: 3 ve 1 birimlik parçaların orta noktaları x = 1 ve x = 5’te ise merkez (3 × 1 + 1 × 5) ÷ 4 = 2’dedir')],
 ad=[A('Parçaları yaz','Alt kol: 4 birim, merkezi (2; 0). Dik kol: 6 birim, merkezi (4; 3). Üst kol: 2 birim, merkezi (5; 6).','Σℓ = 12'),
     A('x koordinatı','x = (4 × 2 + 6 × 4 + 2 × 5) ÷ 12','x = 42 ÷ 12 = 3,5'),
     A('y koordinatı','y = (4 × 0 + 6 × 3 + 2 × 6) ÷ 12','y = 30 ÷ 12 = 2,5'),
     A('Noktayı bul','(3,5; 2,5) noktasını ızgarada işaretle.','Cevap: '+dog)],
 puf='Tel soruları ağırlıklı ortalamadır: her parçanın uzunluğu kütle, orta noktası konumdur.',sekil=SK)

# ----------------- yaz -----------------
for qq in P.ANA: qq['kardes']=None
os.makedirs(HV+'/ayt-fiz',exist_ok=True)
P.yaz(HV+'/ayt-fiz/agirlik-1.json','/dev/null')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Fizik 2018–2025, 345 AYT Fizik, Bilgi Sarmal AYT Fizik (yalnız mantık), MEB 11–12. sınıf fizik.',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(HV+'/kartlar/afagirlik.json','w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
