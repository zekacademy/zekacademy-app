"""Mantık (hafif mod): 25 ana soru, kardeş yok, ipucu 1. Her cevap ve çeldirici doğruluk tablosu taramasıyla (itertools.product) doğrulanır."""
import sys,os,itertools,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
H.KONU='Mantık'
UK='matd|Mantık'
P=Parti('mantik','Mantık',UK)

# ---------- mantık yardımcıları: ifade ayrıştırıcı (′ ∧ ∨ ⇒ ⇔ ≡), tablo taraması ----------
def parse(s):
    t=[c for c in s if c!=' ']; pos=[0]
    def peek(): return t[pos[0]] if pos[0]<len(t) else None
    def nxt(): pos[0]+=1; return t[pos[0]-1]
    def iff():
        a=imp()
        while peek() in ('⇔','≡'):
            nxt(); b=imp(); a=(lambda a,b:lambda e:a(e)==b(e))(a,b)
        return a
    def imp():
        a=orr()
        if peek()=='⇒':
            nxt(); b=imp(); return (lambda a,b:lambda e:(not a(e)) or b(e))(a,b)
        return a
    def orr():
        a=andd()
        while peek()=='∨':
            nxt(); b=andd(); a=(lambda a,b:lambda e:a(e) or b(e))(a,b)
        return a
    def andd():
        a=un()
        while peek()=='∧':
            nxt(); b=un(); a=(lambda a,b:lambda e:a(e) and b(e))(a,b)
        return a
    def un():
        a=atom()
        while peek()=='′':
            nxt(); a=(lambda a:lambda e:not a(e))(a)
        return a
    def atom():
        c=nxt()
        if c=='(':
            a=iff(); assert nxt()==')'; return a
        if c in '01': return lambda e,c=c:c=='1'
        return lambda e,c=c:e[c]
    f=iff(); assert pos[0]==len(t),s; return f
def V(_e,**env): return int(parse(_e)(env))
def modeller(s,vs):
    f=parse(s); return [m for m in itertools.product([0,1],repeat=len(vs)) if f(dict(zip(vs,map(bool,m))))]
def esdeger(a,b,vs): return modeller(a,vs)==modeller(b,vs)
def kesin(prem,concl,vs):
    """premler (liste) doğruyken concl her modelde doğru mu?"""
    pf=[parse(x) for x in prem]; cf=parse(concl); ok=False; hep=True
    for m in itertools.product([0,1],repeat=len(vs)):
        e=dict(zip(vs,map(bool,m)))
        if all(f(e) for f in pf):
            ok=True
            if not cf(e): hep=False
    assert ok,'öncüller çelişkili'
    return hep
def yer(dog,yal,hedef):
    s=list(yal); s.insert('ABCDE'.index(hedef),dog); return s
TIP={'mnt-temel':'Önerme, değil, ve/veya ve doğruluk değeri','mnt-kosullu':'Koşullu ve iki yönlü koşullu önerme','mnt-bulma':'Bileşik önermenin doğruluk değerinden p, q, r bulma',
     'mnt-denk':'Denk önermeler, De Morgan ve totoloji','mnt-nicelik':'Niceleyiciler ve olumsuzu','mnt-cikarim':'Hikâyeli çıkarım (kesinlikle doğru olan)','mnt-acik':'Açık önerme, doğruluk kümesi ve tablo'}
def Q(no,tipId,z,alt,kaz,kalip,kart,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sira=None,sekil=None,kisa=None):
    assert 3<=len(ad)<=7
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,sira=sira,ip=[ip],bilgi=bilgi,puf=puf,kisa=kisa,tipId=tipId,tip=TIP[tipId],z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=kart)

# ---------- bilgi kutuları ----------
ONER=B('Önerme','Doğru ya da yanlış hükmü verilebilen cümleye önerme denir; doğruysa doğruluk değeri 1, yanlışsa 0’dır. Soru, emir, ünlem, öznel yargı ve x’e bağlı ifade önerme değildir. Örnek: “5 asaldır” (1) ve “4 tektir” (0) önermedir; “Kaç yaşındasın?” önerme değildir')
DEGIL=B('Değil (olumsuz)','p′, p’nin değilidir ve p’nin doğruluk değerini tersine çevirir. Örnek: p = 1 ise p′ = 0; (p′)′ ≡ p')
VEVEYA=B('Ve, veya','p ∧ q yalnız ikisi de 1 iken 1’dir; p ∨ q yalnız ikisi de 0 iken 0’dır. Örnek: 1 ∧ 0 = 0 ve 1 ∨ 0 = 1')
KOS=B('Koşullu önerme','p ⇒ q yalnız p = 1 ve q = 0 iken 0’dır; diğer üç durumda 1’dir. Örnek: 0 ⇒ 1 = 1, 1 ⇒ 0 = 0. Ayrıca p ⇒ q ≡ p′ ∨ q ve (p ⇒ q)′ ≡ p ∧ q′')
IKI=B('İki yönlü koşullu','p ⇔ q, p ile q aynı değeri aldığında 1, farklı değer aldığında 0’dır. Örnek: 0 ⇔ 0 = 1 ve 1 ⇔ 0 = 0')
DEM=B('De Morgan kuralları','(p ∧ q)′ ≡ p′ ∨ q′ ve (p ∨ q)′ ≡ p′ ∧ q′; değil alınırken bağlaç değişir. Örnek: “Ne çay ne kahve içti” = “çay içmedi ve kahve içmedi”')
DENK=B('Koşulluya denk ifadeler','p ⇒ q ≡ q′ ⇒ p′ (karşıt tersi) ≡ p′ ∨ q. Karşıtı (q ⇒ p) ve tersi (p′ ⇒ q′) p ⇒ q ile denk değildir. Örnek: “Yağmur yağarsa ıslanırım” ≡ “Islanmadıysam yağmur yağmamıştır”')
TOT=B('Totoloji ve çelişki','Bütün durumlarda 1 olan önermeye totoloji, bütün durumlarda 0 olan önermeye çelişki denir. Örnek: p ∨ p′ totoloji, p ∧ p′ çelişkidir')
NIC=B('Niceleyiciler','∀ “her”, ∃ “bazı” (en az bir) demektir. (∀x, P(x))′ ≡ ∃x, P(x)′ ve (∃x, P(x))′ ≡ ∀x, P(x)′. Örnek: “Her kuş uçar”ın olumsuzu “Uçmayan en az bir kuş vardır”dır')
TC=B('Tek ve çift sayı','2’ye tam bölünen sayı çifttir, bölünmeyen sayı tektir. Örnek: 6 ve 12 çift, 7 ve 9 tektir')
ACIK=B('Açık önerme ve doğruluk kümesi','x’e değer verilince doğru ya da yanlış olan ifadeye açık önerme, onu doğru yapan x değerlerinin kümesine doğruluk kümesi denir. Örnek: x ∈ {1, 2, 3, 4} için “x çift” ifadesinin doğruluk kümesi {2, 4}')
CIK=B('Koşullu önermeden çıkarım','p ⇒ q ve p doğruysa q doğrudur; p ⇒ q ve q′ doğruysa p′ doğrudur. q doğruysa p hakkında, p′ doğruysa q hakkında kesin bir şey söylenemez. Örnek: “Kar yağarsa okul tatil olur” ve “okul tatil değil” ise kar yağmamıştır')

KY='ÖSYM 2021–2026 TYT Matematik (Mantık, her yıl 1 soru) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf Mantık'
kart('K-MNT-01','Önerme, değil, ve/veya','Önerme olup olmadığını ayırt eder; p, q, r değerleri verilen bileşik önermenin değerini ve tablosunu bulur.','Soru/emir/öznel yargıyı önerme saymak; değil işaretini atlamak; 1 ⇒ 0’ı 1 sanmak.','kolay','düz',2,'mnt-temel','Önerme, değil, ve/veya ve doğruluk değeri',KY)
kart('K-MNT-02','Koşullu ve iki yönlü koşullu','p ⇒ q ve p ⇔ q yorumlanır; karşıt, ters, karşıt tersi ve p ∨ q′ biçimindeki denklikler ayrılır; günlük “ise/ancak ve ancak” cümleleri çözülür.','Karşıt ya da tersi karşıt tersi ile karıştırmak; p ⇒ q yanlışken hangi değerlerin kesin olduğunu atlamak.','orta','hikâyeli',3,'mnt-kosullu','Koşullu ve iki yönlü koşullu önerme',KY)
kart('K-MNT-03','Doğruluk değerinden p, q, r bulma','Bileşik önermenin doğru/yanlış olduğu bilgisinden önermelerin değerleri geriye doğru çözülür; modeller taranır, olabilecek durum seçilir.','Değilleri her önermeye ayrı dağıtmak; tek model olmayan durumda “olabilir” ile “kesin” ayrımını kaçırmak.','zor','hikâyeli',4,'mnt-bulma','Bileşik önermenin doğruluk değerinden p, q, r bulma',KY)
kart('K-MNT-04','De Morgan, denklik, totoloji','Değilin dağılması, denk ifade seçme, totoloji; günlük cümlenin olumsuzu.','De Morgan’da bağlacı değiştirmemek; koşullunun olumsuzunu yine koşullu yazmak.','orta','düz',3,'mnt-denk','Denk önermeler, De Morgan ve totoloji',KY)
kart('K-MNT-05','Niceleyiciler ve olumsuzu','∀ ile ∃ yer değiştirir, özellik değillenir; iç içe ve bileşik niceleyicili önermelerin olumsuzu.','∀’yı ∃ yapıp özelliği değillemeyi unutmak; ≥ ın değilini ≤ yazmak.','orta','düz',3,'mnt-nicelik','Niceleyiciler ve olumsuzu',KY)
kart('K-MNT-06','Hikâyeli çıkarım','Günlük cümlelerle verilen koşullu önermelerden “kesinlikle doğru” olanlar (karşıt tersi zinciri) bulunur.','Ters ve karşıt hatası; ara halkada durmak; “kesin” yerine “olabilir” seçmek.','zor','öncüllü',4,'mnt-cikarim','Hikâyeli çıkarım (kesinlikle doğru olan)',KY)
kart('K-MNT-07','Açık önerme, doğruluk kümesi, tablo','Açık önermelerin bileşiklerinin doğruluk kümesi ve tablodaki satırlara bileşik önerme uygulanır; model sayma.','⇒ yerine ∧/∨ kullanmak; tabloda satırı atlamak; model sayarken ∨’da çift sayım.','orta','tablo',4,'mnt-acik','Açık önerme, doğruluk kümesi ve tablo',KY)

L5=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']

# ---------- 01 kolay · önerme tanıma ----------
assert 2 in [2,3,5,7] and 2%2==0   # "Her asal sayı tektir" yanlış (2 asal ve çift)
Q('0001','mnt-temel','kolay','Önerme ve Doğruluk Değeri','Önerme olan ve olmayan cümleleri ayırt edip doğruluk değeri 0 olan önermeyi bulur.','düz',
 'K-MNT-01 (önerme tanıma) · yanlış değerli önerme',
 'Aşağıdakilerden hangisi doğruluk değeri 0 olan bir önermedir?',
 'Her asal sayı tek sayıdır.',
 [('Bir haftada yedi gün vardır.','Önerme olduğunu görmüş ama değerinin 1 olduğunu fark etmeyip soru kökündeki “0” koşulunu atlamış.','dikkat'),
  ('x + 3 = 7','x’e bağlı açık ifadeyi yanlış önerme sanmış; x = 4 için doğru olduğundan değeri belli değildir.','bilgi'),
  ('Yarınki sınavın saati kaçta?','Soru cümlesini yanlış bir önerme saymış; soru cümlelerine doğru/yanlış hükmü verilmez.','bilgi'),
  ('Matematik en güzel derstir.','Kişiden kişiye değişen yargıyı yanlış bir önerme saymış; öznel yargı önerme değildir.','bilgi')],
 'Doğruluk değeri 0 olan önerme.',
 'Şıkları tek tek incele; hangilerine doğru ya da yanlış hükmü verilebildiğine, sonra bunların değerlerine bak.',
 [ONER],
 [A('Önermeleri ayır','C, x’e bağlı bir açık ifadedir; D bir soru cümlesidir; E öznel bir yargıdır.','Önerme olanlar: A ve B'),
  A('Değerlerine bak','Haftada 7 gün vardır; ama 2 asaldır ve çifttir.','A = 1 · B = 0 (2 asal ve çift)'),
  A('Cevabı seç','Doğruluk değeri 0 olan önerme B’dir.','B: Her asal sayı tek sayıdır.')],
 'Önce önerme olup olmadığına, sonra doğruluk değerine bak; soru, emir ve öznel yargı önerme değildir.',
 sira=yer('Her asal sayı tek sayıdır.',['Bir haftada yedi gün vardır.','x + 3 = 7','Yarınki sınavın saati kaçta?','Matematik en güzel derstir.'],'B'))

# ---------- 02 kolay · değer hesabı ----------
env2=dict(p=int(12%4==0),q=int(math.isqrt(16)==8),r=int(2**3<3**2)); assert env2==dict(p=1,q=0,r=1)
S2=dict(A='(p ∧ q) ∨ r′',B='p ⇒ (q ∨ r′)',C='(p ∨ q)′ ∧ r',D='(p ⇒ q) ∧ r',E='(p ⇒ q)′ ∧ r')
v2={k:V(x,**{a:bool(b) for a,b in env2.items()}) for k,x in S2.items()}; assert v2==dict(A=0,B=0,C=0,D=0,E=1)
e=lambda s_,**k:V(s_,**k)
assert V('(p ∧ q) ∨ r',p=1,q=0,r=1)==1 and V('p ⇒ (q ∨ r)',p=1,q=0,r=1)==1 and V('(p ∨ q) ∧ r',p=1,q=0,r=1)==1
Q('0002','mnt-temel','kolay','Bileşik Önermeler','p, q, r önermelerinin doğruluk değerlerini bulup bileşik önermenin değerini hesaplar.','düz',
 'K-MNT-01 (doğruluk değeri) · koşullu ve değilli bileşik önerme',
 'p : 12 sayısı 4’e tam bölünür.\nq : √16 = 8\nr : 2³ < 3²\nBuna göre, aşağıdaki bileşik önermelerden hangisinin doğruluk değeri 1’dir?',
 S2['E'],
 [(S2['A'],'r′ yerine r’yi almış: (p ∧ q) ∨ r = 0 ∨ 1 = 1 bulmuş.','dikkat'),
  (S2['B'],'r′ değerini 1 sanmış (r = 1 iken değilini almamış): q ∨ 1 = 1 ve p ⇒ 1 = 1 bulmuş.','dikkat'),
  (S2['C'],'Parantezin değilini unutmuş: p ∨ q = 1 alıp 1 ∧ r = 1 bulmuş.','dikkat'),
  (S2['D'],'1 ⇒ 0 değerini 1 sanmış (yalnız 0 ⇒ 1’i yanlış saymış): 1 ∧ 1 = 1 bulmuş.','bilgi')],
 'Doğruluk değeri 1 olan bileşik önerme.',
 'Önce üç önermenin doğru mu yanlış mı olduğunu belirle; sonra şıkları içten dışa doğru değerlendir.',
 [KOS,DEGIL],
 [A('p, q, r değerleri','12 = 4 × 3 olduğundan p doğru; √16 = 4 olduğundan q yanlış; 8 < 9 olduğundan r doğru.','p = 1 · q = 0 · r = 1'),
  A('E’yi hesapla','p ⇒ q = 1 ⇒ 0 = 0; değili 1; r ile ve bağlacı.','(p ⇒ q)′ ∧ r = 1 ∧ 1 = 1'),
  A('Diğerlerini ele','Dört şıkkın değeri de 0 çıkar.','A = 0 · B = 0 · C = 0 · D = 0')],
 'Bileşik önermeyi önce parçaların 1/0 değerlerine çevirip içten dışa değerlendir.',
 sira=yer(S2['E'],[S2['A'],S2['B'],S2['C'],S2['D']],'E'))

# ---------- 03 kolay · hikâyeli ne … ne de ----------
O3=dict(A=('p ∧ q','Bugün hava hem yağmurlu hem soğuktur.'),B=('p','Bugün hava yağmurludur.'),C=('q′','Bugün hava soğuk değildir.'),D=('p ∨ q','Bugün hava yağmurlu veya soğuktur (en az biri doğrudur).'),E=('p′','Bugün hava yağmurlu değildir.'))
pr3=['(p′ ∧ q′)′']
ks=[k for k,(f,_) in O3.items() if kesin(pr3,f,['p','q'])]; assert ks==['D']
Q('0003','mnt-temel','kolay','Bileşik Önermeler','“Ne … ne de” önermesinin yanlış olmasından kesin sonucu çıkarır.','hikâyeli',
 'K-MNT-01 (ve/veya, değil) · “ne yağmurlu ne soğuk” yanlış',
 'Bir hava durumu programında\np : Bugün hava yağmurludur.\nq : Bugün hava soğuktur.\nönermeleri veriliyor.\n“Bugün hava ne yağmurlu ne de soğuktur.” önermesinin yanlış olduğu bilindiğine göre, aşağıdakilerden hangisi kesinlikle doğrudur?',
 O3['D'][1],
 [(O3['A'][1],'“Ne … ne de” yanlışsa ikisinin de doğru olması gerektiğini sanmış; yalnız biri doğruyken de “veya” doğrudur, (1, 0) ve (0, 1) durumlarını unutmuş.','bilgi'),
  (O3['B'][1],'Yağmurlu olmasının kesin olduğunu sanmış; hava yalnız soğuk da olabilir.','dikkat'),
  (O3['C'][1],'p′ ∧ q′ yanlışsa p′ yanlış, q′ doğru sanmış; oysa hangisinin yanlış olduğu belli değildir: (0, 1) için q′ = 0.','bilgi'),
  (O3['E'][1],'p′ ∧ q′ yanlışsa p′ doğru sanmış; hava yağmurlu olup soğuk olmayabilir.','bilgi')],
 'Kesinlikle doğru olan ifade.',
 'Verilen cümleyi p′ ve q′ ile sembolle yaz; “yanlış” bilgisini bu ifadenin değerine yaz.',
 [DEM,VEVEYA],
 [A('Cümleyi yaz','“Ne yağmurlu ne soğuk” = yağmurlu değil ve soğuk değil.','p′ ∧ q′ yanlış'),
  A('Değilini al','Yanlış önermenin değili doğrudur; De Morgan uygula.','(p′ ∧ q′)′ ≡ p ∨ q doğru'),
  A('Şıkları sına','p ∨ q (kapsayıcı veya) doğruysa (1, 1), (1, 0), (0, 1) modellerinden biri vardır.','Her modelde doğru olan yalnız p ∨ q')],
 '“Ne … ne de” cümlesi yanlışsa, iki durumdan en az biri gerçekleşmiştir (p ∨ q).',
 sira=yer(O3['D'][1],[O3['A'][1],O3['B'][1],O3['C'][1],O3['E'][1]],'A'))

# ---------- 04 kolay · tablo ----------
def tb(s_): return [V(s_,p=a,q=b) for a,b in [(1,1),(1,0),(0,1),(0,0)]]
assert tb('p′ ⇔ q')==[0,1,1,0]
O4={'0, 1, 1, 0':'p′ ⇔ q','1, 0, 0, 1':'p ⇔ q','1, 0, 1, 1':'p′ ∨ q','0, 0, 1, 0':'p′ ∧ q','1, 1, 1, 0':'p′ ⇒ q'}
for k,f in O4.items(): assert ', '.join(map(str,tb(f)))==k
assert len(set(O4))==5
tab4=tablo_svg(['p','q','p′ ⇔ q'],[['1','1','a'],['1','0','b'],['0','1','c'],['0','0','d']])
Q('0004','mnt-temel','kolay','Bileşik Önermeler','İki yönlü koşullu önermenin doğruluk tablosunu değilli bir terimle oluşturur.','tablo',
 'K-MNT-01 (doğruluk tablosu) · p′ ⇔ q',
 'Aşağıdaki tabloda p′ ⇔ q bileşik önermesinin doğruluk değerleri a, b, c ve d ile gösterilmiştir.\nBuna göre, a, b, c, d sırasıyla aşağıdakilerden hangisidir?',
 '0, 1, 1, 0',
 [('1, 0, 0, 1','p′ yerine p’yi kullanıp p ⇔ q’nun tablosunu yazmış.','dikkat'),
  ('1, 0, 1, 1','⇔ bağlacını “veya” gibi okuyup p′ ∨ q’nun tablosunu yazmış.','bilgi'),
  ('0, 0, 1, 0','⇔ bağlacını “ve” gibi okuyup p′ ∧ q’nun tablosunu yazmış.','bilgi'),
  ('1, 1, 1, 0','⇔ bağlacını ⇒ gibi okuyup p′ ⇒ q’nun tablosunu yazmış.','bilgi')],
 'a, b, c, d değerlerinin sırası.',
 'Her satır için önce p′ değerini yaz, sonra p′ ile q’nun aynı olup olmadığına bak.',
 [IKI,DEGIL],
 [A('p′ değerleri','p′, p’nin tersidir.','p = 1, 1, 0, 0 → p′ = 0, 0, 1, 1'),
  A('Satırları karşılaştır','⇔, iki tarafın değeri aynıysa 1 verir.','(0, 1) → 0 · (0, 0) → 1 · (1, 1) → 1 · (1, 0) → 0'),
  A('Sırala','a, b, c, d değerlerini yaz.','a = 0 · b = 1 · c = 1 · d = 0')],
 'Tablo sorularında değilli sütunu önce ayrıca yaz; sonra bağlacı satır satır uygula.',
 sira=yer('0, 1, 1, 0',['1, 0, 0, 1','1, 0, 1, 1','0, 0, 1, 0','1, 1, 1, 0'],'A'),sekil=tab4)

# ---------- 05 kolay · karşıt tersi (hikâyeli) ----------
O5={'A':('q′ ⇒ p′','Okullar tatil edilmediyse kar yağmamıştır.'),'B':('q ⇒ p','Okullar tatil edildiyse kar yağmıştır.'),'C':('p′ ⇒ q′','Kar yağmazsa okullar tatil edilmez.'),'D':('p ∧ q′','Kar yağmış ve okullar tatil edilmemiştir.'),'E':('p ⇔ q','Kar yağarsa ve ancak o zaman okullar tatil edilir.')}
dk=[k for k,(f,_) in O5.items() if esdeger(f,'p ⇒ q',['p','q'])]; assert dk==['A']
Q('0005','mnt-kosullu','kolay','Koşullu Önerme','Günlük bir koşullu cümlenin karşıt tersini (denk ifadesini) bulur.','hikâyeli',
 'K-MNT-02 (karşıt tersi) · kar ve okul tatili',
 '“Kar yağarsa okullar tatil edilir.” önermesine denk olan önerme aşağıdakilerden hangisidir?',
 O5['A'][1],
 [(O5['B'][1],'Koşullunun karşıtını (q ⇒ p) karşıt tersi sanmış.','bilgi'),
  (O5['C'][1],'Koşullunun tersini (p′ ⇒ q′) karşıt tersi sanmış.','bilgi'),
  (O5['D'][1],'Koşullunun olumsuzu olan p ∧ q′ ile kendisini karıştırmış.','bilgi'),
  (O5['E'][1],'“ise” ile “ancak ve ancak” bağlacını aynı sanmış.','bilgi')],
 'Verilen önermeye denk olan önerme.',
 'Cümleyi p ve q ile sembole çevirip sırasıyla her şıkkın hangi sembolle yazıldığına bak.',
 [DENK],
 [A('Sembolle yaz','p : Kar yağar. q : Okullar tatil edilir.','Verilen: p ⇒ q'),
  A('Karşıt tersini kur','Önce yer değiştir, sonra ikisini de değille.','q′ ⇒ p′'),
  A('Şıkla eşle','“Tatil edilmediyse kar yağmamıştır.”','q′ ⇒ p′ ≡ p ⇒ q')],
 'p ⇒ q ile denk olan koşullu yalnız karşıt tersidir: q′ ⇒ p′.',
 sira=yer(O5['A'][1],[O5['B'][1],O5['C'][1],O5['D'][1],O5['E'][1]],'A'))

# ---------- 06 orta · sepet ----------
F6='(p ∨ q)′ ∧ r'; m6=modeller(F6,['p','q','r']); assert m6==[(0,0,1)]
O6={'Yalnızca elma vardır.':(1,0,0),'Elma, armut ve kiraz vardır.':(1,1,1),'Yalnızca armut ve kiraz vardır.':(0,1,1),'Sepet boştur.':(0,0,0),'Yalnızca kiraz vardır.':(0,0,1)}
assert [k for k,v in O6.items() if v in m6]==['Yalnızca kiraz vardır.']
c6=lambda f:[k for k,v in O6.items() if V(f,p=v[0],q=v[1],r=v[2]) and v!=(0,0,1)]
assert c6('(p ∨ q) ∧ r′')==['Yalnızca elma vardır.']          # A: değilleri ayrı uygulamış
assert 'Elma, armut ve kiraz vardır.' in c6('(p ∨ q) ∧ r')      # B: değili hiç almamış
assert c6('(p′ ∨ q′) ∧ r')==['Yalnızca armut ve kiraz vardır.'] # C: bağlacı değiştirmemiş
assert c6('(p ∨ q)′')==['Sepet boştur.']                        # D: r denetlenmemiş
Q('0006','mnt-bulma','orta','Doğruluk Değerinden Önerme Bulma','Bileşik önermenin doğru olmasından p, q, r değerlerini bulup günlük durumu belirler.','hikâyeli',
 'K-MNT-03 (p, q, r bulma) · sepetteki meyveler',
 'Bir manav, sepetine koyduğu meyveler için\np : Sepette elma vardır.\nq : Sepette armut vardır.\nr : Sepette kiraz vardır.\nönermelerini yazıyor. Sepette bu üç meyveden başka meyve olmadığı ve (p ∨ q)′ ∧ r önermesinin doğru olduğu bilindiğine göre, sepettekiler aşağıdakilerden hangisi olabilir?',
 'Yalnızca kiraz vardır.',
 [('Yalnızca elma vardır.','Değilleri her önermeye ayrı uygulayıp (p ∨ q) ∧ r′ gibi okumuş; bu ifade elma için 1 olur.','bilgi'),
  ('Elma, armut ve kiraz vardır.','(p ∨ q)′ ifadesinin değilini hiç almamış: (p ∨ q) ∧ r = 1 bulmuş.','dikkat'),
  ('Yalnızca armut ve kiraz vardır.','De Morgan’da bağlacı değiştirmeyip (p ∨ q)′ yerine p′ ∨ q′ almış; armut ve kiraz için bu değer 1 çıkar.','bilgi'),
  ('Sepet boştur.','(p ∨ q)′ = 1 bulmuş ama r = 1 koşulunu denetlememiş.','dikkat')],
 'Sepette bulunan meyveler.',
 'Doğru olan bir “ve” önermesinde iki tarafın aldığı değere bak; sonra değilli parçanın içini çöz.',
 [VEVEYA,DEM],
 [A('Ve bağlacını aç','Bir “∧” önermesi, ancak iki tarafı da doğruysa doğrudur.','(p ∨ q)′ = 1 ve r = 1'),
  A('Değili çöz','(p ∨ q)′ = 1 ise p ∨ q = 0; “veya” yalnız ikisi de 0 iken 0’dır.','p = 0 · q = 0'),
  A('Meyveleri yaz','Elma yok, armut yok, kiraz var; başka meyve de yok.','Yalnızca kiraz vardır.')],
 'Doğru bir “ve” bileşiğinde her bileşen 1’dir; “veya”nın yanlışlığı iki tarafın da 0 olması demektir.',
 sira=yer('Yalnızca kiraz vardır.',['Yalnızca elma vardır.','Elma, armut ve kiraz vardır.','Yalnızca armut ve kiraz vardır.','Sepet boştur.'],'E'))

# ---------- 07 orta · p, q, r bulma (sembolik) ----------
F7='(p ∨ q′) ∧ (q ⇒ r)′'; m7=modeller(F7,['p','q','r']); assert m7==[(1,1,0)]
O7={'0, 1, 0':(0,1,0),'1, 0, 0':(1,0,0),'1, 1, 0':(1,1,0),'1, 1, 1':(1,1,1),'0, 0, 1':(0,0,1)}
ok_=lambda f,v:V(f,p=v[0],q=v[1],r=v[2])
assert [k for k,v in O7.items() if v in m7]==['1, 1, 0']
assert ok_('(p′ ∨ q′) ∧ (q ⇒ r)′',O7['0, 1, 0']) and ok_('(p ∨ q′) ∧ (q′ ⇒ r′)',O7['1, 0, 0']) and ok_('(p ∨ q′) ∧ (q ⇒ r)',O7['1, 1, 1']) and ok_('(p ∨ q′) ∧ (q ⇒ r′)',O7['0, 0, 1'])
Q('0007','mnt-bulma','orta','Doğruluk Değerinden Önerme Bulma','Değilli “veya” ve değilli koşullu önermenin doğru olmasından p, q, r değerlerini bulur.','düz',
 'K-MNT-03 (p, q, r bulma) · değilli veya ve değilli koşullu',
 'p, q ve r önermeleri için\n(p ∨ q′) ∧ (q ⇒ r)′\nönermesi doğrudur.\nBuna göre, (p, q, r) doğruluk değeri üçlüsü aşağıdakilerden hangisidir?',
 '1, 1, 0',
 [('0, 1, 0','p ∨ q′ ifadesini p′ ∨ q′ gibi okumuş; (0, 1) için bu okuma 1 verir.','dikkat'),
  ('1, 0, 0','Değili parantez içine dağıtıp (q ⇒ r)′ yerine q′ ⇒ r′ yazmış; (q, r) = (0, 0) için bu 1 olur.','bilgi'),
  ('1, 1, 1','(q ⇒ r)′ ifadesinin değilini hiç almamış; q ⇒ r = 1 ⇒ 1 = 1 bulmuş.','dikkat'),
  ('0, 0, 1','(q ⇒ r)′ ifadesini q ⇒ r′ gibi okumuş; (q, r) = (0, 1) için bu 1 olur.','bilgi')],
 'p, q, r değerleri.',
 'Önce “ve” bileşiğinin iki yanını ayrı ayrı 1 yap; önce yalnız bir değer veren tarafı çöz.',
 [KOS,VEVEYA,DEGIL],
 [A('Ve bağlacını aç','Her iki taraf da doğru olmalı.','p ∨ q′ = 1 ve (q ⇒ r)′ = 1'),
  A('Koşulluyu çöz','(q ⇒ r)′ = 1 ise q ⇒ r yanlıştır; bu yalnız q = 1, r = 0 iken olur.','q = 1 · r = 0'),
  A('Veya’yı çöz','q = 1 iken q′ = 0; p ∨ 0 doğruysa p = 1.','p = 1'),
  A('Cevap','Değerleri sırala.','p = 1 · q = 1 · r = 0')],
 'Yanlış bir koşullunun olumsuzu tek bir değer çifti verir; önce onu çöz.',
 sira=yer('1, 1, 0',['0, 1, 0','1, 0, 0','1, 1, 1','0, 0, 1'],'B'))

# ---------- 08 orta · p ⇒ q yanlış ----------
S8=['p′ ∧ q′','p′ ∧ q','p ⇔ q','p′ ∨ q','p ∧ q′']
assert modeller('p ⇒ q',['p','q'])==[(0,0),(0,1),(1,1)]
v8=[(x,V(x,p=1,q=0)) for x in S8]; assert [x for x,v in v8 if v]==['p ∧ q′']
assert kesin(['(p ⇒ q)′'],'p ∧ q′',['p','q'])
Q('0008','mnt-kosullu','orta','Koşullu Önerme','Koşullu önermenin yanlış olmasından p ve q’nun değerlerini bulup kesin doğru olan bileşik önermeyi seçer.','düz',
 'K-MNT-02 (p ⇒ q yanlış) · kesin doğru olan bileşik önerme',
 'p ⇒ q önermesi yanlış olduğuna göre, aşağıdaki önermelerden hangisinin doğruluk değeri kesinlikle 1’dir?',
 'p ∧ q′',
 [('p′ ∧ q′','p ⇒ q yanlışken p = 0 ve q = 0 sanmış; bu değerlerde p′ ∧ q′ = 1 olur.','bilgi'),
  ('p′ ∧ q','p ⇒ q yanlışken p = 0, q = 1 almış; bu değerlerde p′ ∧ q = 1 olur.','bilgi'),
  ('p ⇔ q','Yanlış koşulludan p ve q’nun eşit değerli olduğunu sanmış; oysa p = 1, q = 0’dır.','bilgi'),
  ('p′ ∨ q','p′ ∨ q ≡ p ⇒ q olduğunu görmemiş; bu önerme de yanlıştır.','bilgi')],
 'Kesinlikle doğru olan bileşik önerme.',
 'Koşullu önerme ancak bir tek durumda yanlıştır; o durumda p ile q’nun aldığı değerleri bul.',
 [KOS],
 [A('p ile q’yu bul','p ⇒ q yalnız p = 1, q = 0 iken yanlıştır.','p = 1 · q = 0'),
  A('Şıkları hesapla','p′ = 0, q′ = 1 değerlerini yerine koy.','p′ ∧ q′ = 0 · p′ ∧ q = 0 · p ⇔ q = 0 · p′ ∨ q = 0'),
  A('Doğru olanı seç','Geriye kalan şık 1 olur.','p ∧ q′ = 1 ∧ 1 = 1')],
 'p ⇒ q yanlışsa p = 1 ve q = 0’dır; p ∧ q′ onun olumsuzudur.',
 sira=yer('p ∧ q′',['p′ ∧ q′','p′ ∧ q','p ⇔ q','p′ ∨ q'],'A'))

# ---------- 09 orta · öncüllü denk ----------
I9=['q′ ⇒ p′','(p ∧ q′)′','p′ ⇒ q′']; assert [esdeger(x,'p ⇒ q',['p','q']) for x in I9]==[True,True,False]
Q('0009','mnt-kosullu','orta','Koşullu Önerme','Koşullu önermeye denk olan ifadeleri karşıt tersi ve De Morgan ile belirler.','öncüllü',
 'K-MNT-02 (denk önermeler) · karşıt tersi ve olumsuzun olumsuzu',
 'I. q′ ⇒ p′\nII. (p ∧ q′)′\nIII. p′ ⇒ q′\nYukarıdaki önermelerden hangileri p ⇒ q önermesine denktir?',
 'I ve II',
 [('Yalnız I','II’yi açamamış: (p ∧ q′)′ ≡ p′ ∨ q ≡ p ⇒ q olduğunu görememiş.','bilgi'),
  ('Yalnız II','q′ ⇒ p′ ifadesini q ⇒ p gibi okuyup I’i denk saymamış.','bilgi'),
  ('I ve III','Tersi (p′ ⇒ q′) denk saymış; II’yi De Morgan ile açamamış.','bilgi'),
  ('I, II ve III','Tersini (p′ ⇒ q′) karşıt tersi ile karıştırıp III’ü de denk saymış.','bilgi')],
 'p ⇒ q önermesine denk olan öncüller.',
 'Öncülleri sırayla p ⇒ q ile tablo ya da bilinen denkliklerle karşılaştır; olumsuz önermeyi açmayı unutma.',
 [DENK,DEM],
 [A('Bilinen denkler','p ⇒ q ≡ q′ ⇒ p′ ≡ p′ ∨ q','I doğrudan karşıt tersidir'),
  A('II’yi aç','De Morgan: (p ∧ q′)′ ≡ p′ ∨ (q′)′.','(p ∧ q′)′ ≡ p′ ∨ q ≡ p ⇒ q'),
  A('III’ü sına','p′ ⇒ q′ tersidir; p = 0, q = 1 için p′ ⇒ q′ = 1 ⇒ 0 = 0, p ⇒ q = 1.','III denk değil'),
  A('Sonuç','I ve II denk, III denk değil.','I ve II')],
 'Koşulluya yalnız karşıt tersi (q′ ⇒ p′) ve p′ ∨ q ile (p ∧ q′)′ denktir; karşıt ve ters değildir.',
 sira=L5)

# ---------- 10 orta · ⇔ ve ⇒ çıkarım (hikâyeli) ----------
# p: finale kaldı, q: ödül aldı, r: davetiye aldı; Selin ödül aldı: q=1
O10={'A':('p ∧ r′','Selin finale kalmış, ama tören davetiyesi almamıştır.'),'B':('p ∧ r','Selin finale kalmış ve tören davetiyesi almıştır.'),'C':('p′ ∧ r','Selin finale kalmamış, ama tören davetiyesi almıştır.'),'D':('p′ ∧ r′','Selin finale kalmamış ve tören davetiyesi almamıştır.'),'E':('(p ∧ r)′','Selin finale kalmamış veya tören davetiyesi almamıştır.')}
ks=[k for k,(f,_) in O10.items() if kesin(['p ⇔ q','q ⇒ r','q'],f,['p','q','r'])]; assert ks==['B']
assert kesin(['p′ ⇔ q','q ⇒ r','q'],'p′ ∧ r',['p','q','r'])  # C: ⇔ ters okunmuş
Q('0010','mnt-kosullu','orta','Koşullu Önerme','İki yönlü koşullu ve koşullu önermelerden birlikte kesin sonuç çıkarır.','hikâyeli',
 'K-MNT-02 (⇔ ve ⇒) · yarışma finali ve davetiye',
 'Bir bilgi yarışmasının kuralları şöyledir:\n• Bir yarışmacı ancak ve ancak finale kalırsa ödül alır.\n• Ödül alan her yarışmacıya tören davetiyesi verilir.\nBu yarışmada ödül alan Selin için aşağıdakilerden hangisi kesinlikle doğrudur?',
 O10['B'][1],
 [(O10['A'][1],'İkinci kuralı (ödül ⇒ davetiye) kullanmayıp davetiye almadığını sanmış.','dikkat'),
  (O10['C'][1],'“Ancak ve ancak” kuralını ters okuyup ödül alanın finale kalmadığını düşünmüş; davetiyeyi doğru bulmuş.','bilgi'),
  (O10['D'][1],'Hem “ancak ve ancak” kuralını ters okumuş hem de davetiyeyi ödülle ilişkilendirmemiş.','bilgi'),
  (O10['E'][1],'Doğru sonuç olan “finale kaldı ve davetiye aldı” ifadesinin değilini alıp seçmiş.','dikkat')],
 'Selin için kesinlikle doğru olan ifade.',
 'Ödül almayı q diye adlandır; iki kuralın q’ya hangi sonuçları verdiğini ayrı ayrı yaz.',
 [IKI,KOS,CIK],
 [A('Önermeleri adlandır','p : Finale kaldı. q : Ödül aldı. r : Davetiye aldı.','Kurallar: p ⇔ q ve q ⇒ r'),
  A('İki yönlü kuralı kullan','q = 1 ise p ile q aynı değerde olmalıdır.','p = 1'),
  A('Koşullu kuralı kullan','q = 1 ve q ⇒ r doğru olduğundan r doğrudur.','r = 1'),
  A('Şıkla eşle','Selin finale kalmış ve davetiye almıştır.','p ∧ r = 1')],
 '“Ancak ve ancak” iki yönde de çıkarım verir; koşullu ise yalnız “ise” yönünde.',
 sira=yer(O10['B'][1],[O10['A'][1],O10['C'][1],O10['D'][1],O10['E'][1]],'E'))

# ---------- 11 orta · Ece (hikâyeli) ----------
pr11=['(p ∧ q) ⇒ r','r′']
O11={'A':('p′ ∧ q′','Ece sınavı geçmemiş ve ödevi teslim etmemiştir.'),'B':('p′','Ece sınavı geçmemiştir.'),'C':('q′','Ece ödevi teslim etmemiştir.'),'D':('p ⇒ q′','Ece sınavı geçmişse ödevi teslim etmemiştir.'),'E':('p′ ⇒ q','Ece sınavı geçmemişse ödevi teslim etmiştir.')}
ks=[k for k,(f,_) in O11.items() if kesin(pr11,f,['p','q','r'])]; assert ks==['D']
Q('0011','mnt-kosullu','orta','Koşullu Önerme','“Ve” koşullu bir cümlenin sonucunun gerçekleşmemesinden kesin çıkarımı yapar.','hikâyeli',
 'K-MNT-02 (koşulda ∧) · sınav, ödev ve tatil',
 'Ece, “Sınavı geçersem ve ödevimi teslim edersem tatile çıkacağım.” demiştir. Ece’nin tatile çıkmadığı bilindiğine göre, aşağıdakilerden hangisi kesinlikle doğrudur?',
 O11['D'][1],
 [(O11['A'][1],'Koşulun (p ∧ q) yanlış olması için her iki parçanın da yanlış olması gerektiğini sanmış.','bilgi'),
  (O11['B'][1],'Koşul yanlışken ilk parçayı kesin yanlış saymış; ödev de teslim edilmemiş olabilir.','bilgi'),
  (O11['C'][1],'Koşul yanlışken ikinci parçayı kesin yanlış saymış; sınav geçilmemiş olabilir.','bilgi'),
  (O11['E'][1],'(p′ ∨ q′) bilgisini p′ ⇒ q diye yazmış; oysa p′ ⇒ q ≡ p ∨ q’dur ve kesin değildir.','bilgi')],
 'Kesinlikle doğru olan ifade.',
 'Tatile çıkılmadığı bilgisi hangi koşulun gerçekleşmediğini söyler; bu koşulun olumsuzunu yaz.',
 [CIK,DEM],
 [A('Sembolle yaz','p : Sınavı geçti. q : Ödevi teslim etti. r : Tatile çıktı.','(p ∧ q) ⇒ r ve r′'),
  A('Karşıt tersi','r′ doğruysa koşul gerçekleşmemiştir.','(p ∧ q)′ doğru'),
  A('De Morgan','Değili aç.','p′ ∨ q′ ≡ p ⇒ q′'),
  A('Şıkla eşle','“Sınavı geçmişse ödevi teslim etmemiştir.”','B')],
 '“A ve B ise C” ve C gerçekleşmediyse A ve B’den en az biri gerçekleşmemiştir; hangisinin olduğu belli değildir.',
 sira=yer(O11['D'][1],[O11['A'][1],O11['B'][1],O11['C'][1],O11['E'][1]],'B'))

# ---------- 12 orta · De Morgan sadeleştirme ----------
F12='(p′ ∨ q′)′ ∧ (q ∨ r)'
O12={'A':'p ∧ q','B':'q ∨ (p ∧ r)','C':'p′ ∧ q′ ∧ r','D':'p ∧ (q ∨ r)','E':'p ∧ q ∧ r'}
vs3=['p','q','r']
assert [k for k,f in O12.items() if esdeger(F12,f,vs3)]==['A']
assert esdeger('(p ∨ q) ∧ (q ∨ r)',O12['B'],vs3) and esdeger('p′ ∧ q′ ∧ (q ∨ r)',O12['C'],vs3) and esdeger('p ∧ q ∧ (q ∧ r)',O12['E'],vs3) and esdeger('p ∧ (q ∨ r)',O12['D'],vs3)
assert esdeger('p ∧ q ∧ (q ∨ r)','p ∧ q',vs3) and not esdeger('p ∧ q ∧ (q ∨ r)','p ∧ (q ∨ r)',vs3)
Q('0012','mnt-denk','orta','De Morgan ve Denklik','De Morgan kuralını uygulayıp bileşik önermeyi en sade denk biçime getirir.','düz',
 'K-MNT-04 (De Morgan, sadeleştirme) · değilli bileşiğin sadeleşmesi',
 '(p′ ∨ q′)′ ∧ (q ∨ r)\nönermesine denk olan en sade önerme aşağıdakilerden hangisidir?',
 O12['A'],
 [(O12['B'],'De Morgan’da bağlacı değiştirmeyip (p′ ∨ q′)′ yerine p ∨ q yazmış; (p ∨ q) ∧ (q ∨ r) ≡ q ∨ (p ∧ r) bulmuş.','bilgi'),
  (O12['C'],'Dıştaki değili dağıtırken içteki değilleri koruyup yalnız bağlacı değiştirmiş: p′ ∧ q′; p′ ∧ q′ ∧ (q ∨ r) ≡ p′ ∧ q′ ∧ r bulmuş.','bilgi'),
  (O12['D'],'p ∧ q ∧ (q ∨ r) içinde q ∧ (q ∨ r) yerine q ∨ r yazmış (yutma kuralını karıştırmış).','islem'),
  (O12['E'],'q ∨ r ifadesini q ∧ r gibi okumuş.','dikkat')],
 'Verilen önermeye denk olan en sade önerme.',
 'Önce soldaki değilli parantezi aç; sonra ortaya çıkan ifadeyi (q ∨ r) ile birlikte sadeleştir.',
 [DEM,VEVEYA],
 [A('De Morgan','(p′ ∨ q′)′ ≡ (p′)′ ∧ (q′)′.','(p′ ∨ q′)′ ≡ p ∧ q'),
  A('İfadeyi yaz','Sonucu (q ∨ r) ile birleştir.','p ∧ q ∧ (q ∨ r)'),
  A('Yut','q doğruysa q ∨ r zaten doğrudur.','q ∧ (q ∨ r) ≡ q'),
  A('Sonuç','Geriye p ∧ q kalır.','p ∧ q')],
 'Değilli parantezi önce De Morgan ile aç; ∧ içinde q ve q ∨ r birlikteyse q yeterlidir.',
 sira=yer(O12['A'],[O12['B'],O12['C'],O12['D'],O12['E']],'A'))

# ---------- 13 orta · piknik olumsuzu (hikâyeli) ----------
O13={'A':('p ∧ q ∧ r′','Hava güneşli, gün hafta sonu olduğu hâlde Dilek piknik yapmaz.'),
     'B':('(p′ ∨ q′) ⇒ r′','Hava güneşli değilse veya gün hafta sonu değilse Dilek piknik yapmaz.'),
     'C':('(p′ ∧ q′) ⇒ r','Hava güneşli değilse ve gün hafta sonu değilse Dilek piknik yapar.'),
     'D':('(p ∧ q) ⇒ r′','Hava güneşli ve gün hafta sonu ise Dilek piknik yapmaz.'),
     'E':('(p ∨ q) ∧ r′','Hava güneşli veya gün hafta sonu olduğu hâlde Dilek piknik yapmaz.')}
S13='((p ∧ q) ⇒ r)′'
assert [k for k,(f,_) in O13.items() if esdeger(f,S13,vs3)]==['A']
Q('0013','mnt-denk','orta','De Morgan ve Denklik','Günlük bir koşullu cümlenin olumsuzunu (p ∧ q ∧ r′) bulur.','hikâyeli',
 'K-MNT-04 (koşulluyu olumsuzlama) · güneşli hafta sonu pikniği',
 '“Hava güneşliyse ve gün hafta sonuysa Dilek piknik yapar.” önermesinin olumsuzu aşağıdakilerden hangisidir?',
 O13['A'][1],
 [(O13['B'][1],'Koşulun parçalarını değilleyip bağlacı değiştirmiş, sonucu da değillemiş; ama koşullu yine koşullu olarak kalmış.','bilgi'),
  (O13['C'][1],'Yalnız koşuldaki önermeleri değilleyip sonucu aynen bırakmış.','bilgi'),
  (O13['D'][1],'Yalnız sonucu değillemiş; koşullunun olumsuzunun yine koşullu olamayacağını görmemiş.','bilgi'),
  (O13['E'][1],'Koşuldaki “ve” bağlacını “veya”ya çevirmiş, ⇒ yerine ∧ yazmış.','bilgi')],
 'Verilen önermenin olumsuzu.',
 'Önce cümleyi p, q, r ile sembole çevir; koşullu önermenin hangi durumda yanlış olduğunu düşün.',
 [KOS,DEM],
 [A('Sembolle yaz','p : Hava güneşli. q : Gün hafta sonu. r : Dilek piknik yapar.','(p ∧ q) ⇒ r'),
  A('Koşulluyu değille','(a ⇒ b)′ ≡ a ∧ b′.','((p ∧ q) ⇒ r)′ ≡ (p ∧ q) ∧ r′'),
  A('Cümleye çevir','Güneşli, hafta sonu ve piknik yapılmıyor.','p ∧ q ∧ r′')],
 'Koşullunun olumsuzu koşullu değildir: (a ⇒ b)′ ≡ a ∧ b′.',
 sira=yer(O13['A'][1],[O13['B'][1],O13['C'][1],O13['D'][1],O13['E'][1]],'B'))

# ---------- 14 orta · öncüllü totoloji ----------
I14=['(p ⇒ q) ∨ (q ⇒ p)','(p ∨ q) ⇒ p','(p ∧ q) ⇒ (p ∨ q)']
def tot(f): return len(modeller(f,['p','q']))==4
assert [tot(x) for x in I14]==[True,False,True]
L14=['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III']
Q('0014','mnt-denk','orta','De Morgan ve Denklik','Verilen bileşik önermelerden hangilerinin totoloji olduğunu tablo ile belirler.','öncüllü',
 'K-MNT-04 (totoloji) · koşullu bileşikler',
 'I. (p ⇒ q) ∨ (q ⇒ p)\nII. (p ∨ q) ⇒ p\nIII. (p ∧ q) ⇒ (p ∨ q)\nYukarıdaki önermelerden hangileri totolojidir?',
 'I ve III',
 [('Yalnız I','III’ün her durumda doğru olduğunu görmeyip sınamamış.','dikkat'),
  ('Yalnız III','I’de p = 1, q = 0 satırında p ⇒ q = 0 görüp “veya” ile bağlı q ⇒ p = 1’i hesaba katmamış; I’i totoloji saymamış.','bilgi'),
  ('I ve II','II’yi p = 0, q = 1 satırında sınamamış; orada (0 ∨ 1) ⇒ 0 yanlıştır.','dikkat'),
  ('I, II ve III','II’yi yalnız p = 1 satırlarına bakarak totoloji sanmış.','dikkat')],
 'Totoloji olan öncüller.',
 'Her öncül için dört (p, q) satırını da dene; bir satırda bile 0 çıkıyorsa totoloji değildir.',
 [TOT,KOS],
 [A('I’i sına','Her satırda p ⇒ q ya da q ⇒ p’den en az biri doğrudur.','Satırlar: 1 · 1 · 1 · 1 → totoloji'),
  A('II’yi sına','p = 0, q = 1 için (0 ∨ 1) ⇒ 0 = 1 ⇒ 0 = 0.','II totoloji değil'),
  A('III’ü sına','p ∧ q doğruysa p ∨ q de doğrudur; koşul 1 iken sonuç hep 1.','Satırlar: 1 · 1 · 1 · 1 → totoloji'),
  A('Sonuç','I ve III totolojidir.','I ve III')],
 'Totoloji kanıtı için bütün satırlar taranır; çürütmek için tek bir 0 satırı yeter.',
 sira=L14)

# ---------- 15 orta · niceleyici olumsuzu ----------
xs=[-1,-0.5,0,0.5,1,2]
Pf=lambda x:x*x>=x           # p(x): x² ≥ x
O15={'A':('E',lambda x:x*x<x,'(∃x ∈ ℝ) x² < x'),'B':('E',lambda x:x*x<=x,'(∃x ∈ ℝ) x² ≤ x'),'C':('A',lambda x:x*x<x,'(∀x ∈ ℝ) x² < x'),'D':('A',lambda x:x*x<=x,'(∀x ∈ ℝ) x² ≤ x'),'E':('E',lambda x:x*x>x,'(∃x ∈ ℝ) x² > x')}
dz=[k for k,(qn,f,_) in O15.items() if qn=='E' and all(f(x)==(not Pf(x)) for x in xs)]; assert dz==['A']
# soyut doğrulama: (∀x P)′ ≡ ∃x P′ (3 elemanlı alan, tüm P)
assert all((not all(P_))==any(not v for v in P_) for P_ in itertools.product([0,1],repeat=3))
assert not Pf(0.5) and Pf(0) and not (0*0<0)    # B: x=0 için doğru; ¬p(x) ile aynı kümeyi vermez
Q('0015','mnt-nicelik','orta','Niceleyiciler','“Her” niceleyicili önermenin olumsuzunu (∃ ve değillenmiş özellik) yazar.','düz',
 'K-MNT-05 (∀ olumsuzu) · x² ≥ x',
 '(∀x ∈ ℝ) x² ≥ x\nönermesinin olumsuzu aşağıdakilerden hangisidir?',
 O15['A'][2],
 [(O15['B'][2],'∀ yerine ∃ yazmış ama ≥’nin değilini ≤ almış; doğrusu <’dir.','bilgi'),
  (O15['C'][2],'Özelliği doğru değillemiş (<) ama ∀ niceleyicisini ∃ yapmayı unutmuş.','bilgi'),
  (O15['D'][2],'Niceleyiciyi değiştirmemiş, özelliği de ≤ olarak değillemiş.','bilgi'),
  (O15['E'][2],'Niceleyiciyi ∃ yapmış ama özelliği değillemeden ≥ yerine > yazmış.','bilgi')],
 'Verilen önermenin olumsuzu.',
 '“Her” sözcüğünün olumsuzunu ve ≥ ifadesinin tam tersini ayrı ayrı yaz.',
 [NIC],
 [A('Niceleyiciyi değiştir','“Her” değillenince “bazı” olur.','∀ → ∃'),
  A('Özelliği değille','x² ≥ x’in değili x² < x’tir (≤ değil).','x² ≥ x → x² < x'),
  A('Birleştir','Hepsini yaz.','(∃x ∈ ℝ) x² < x')],
 '(∀x, P)′ ≡ ∃x, P′; ≥’nin değili <’dir.',
 sira=yer(O15['A'][2],[O15['B'][2],O15['C'][2],O15['D'][2],O15['E'][2]],'C'))

# ---------- 16 orta · tek niceleyicili günlük cümlenin olumsuzu ----------
pk=list(itertools.product([0,1],repeat=3))   # her öğrenci için: sınava girdi mi
S16=lambda g:all(g)
O16={'A':('Bu kursta hiçbir öğrenci sınava girmemiştir.',lambda g:all(not v for v in g)),
     'B':('Bu kursta sınava giren en az bir öğrenci vardır.',lambda g:any(g)),
     'C':('Bu kursta sınava girmeyen en az bir öğrenci vardır.',lambda g:any(not v for v in g)),
     'D':('Bu kursta hem sınava giren hem de girmeyen öğrenci vardır.',lambda g:any(g) and any(not v for v in g)),
     'E':('Bu kursta sınava girmeyen öğrenci yoktur.',lambda g:not any(not v for v in g))}
dz=[k for k,(_,f) in O16.items() if all(f(g)==(not S16(g)) for g in pk)]; assert dz==['C']
assert all(O16['E'][1](g)==S16(g) for g in pk)
Q('0016','mnt-nicelik','orta','Niceleyiciler','“Her” niceleyicili günlük cümlenin olumsuzunu seçer.','hikâyeli',
 'K-MNT-05 (∀ olumsuzu, günlük dil) · kursta sınav',
 '“Bu kursta her öğrenci sınava girmiştir.” önermesinin olumsuzu aşağıdakilerden hangisidir?',
 O16['C'][0],
 [(O16['A'][0],'“Her öğrenci girmiştir”in olumsuzunu “hiçbiri girmemiştir” sanmış; “her”i koruyup yalnız özelliği değillemiş.','bilgi'),
  (O16['B'][0],'“Her”i “en az bir”e çevirmiş ama “girmiştir” özelliğini değillememiş.','bilgi'),
  (O16['D'][0],'Girmeyen öğrenci olduğunu bulmuş, yanına “giren de vardır” koşulunu da eklemiş; bu koşul olumsuzun gereği değildir.','dikkat'),
  (O16['E'][0],'Olumsuzu almak yerine aynı şeyi söyleyen bir ifade yazmış: girmeyen öğrencinin olmaması, her öğrencinin girmesidir.','dikkat')],
 'Verilen önermenin olumsuzu.',
 'Cümlenin yanlış olması için kursta ne olması gerektiğini, “her” sözcüğünün karşıtını düşünerek yaz.',
 [NIC],
 [A('Niceleyiciyi değiştir','“Her öğrenci” yerine “en az bir öğrenci” gelir.','∀ → ∃'),
  A('Özelliği değille','“Girmiştir” yerine “girmemiştir” yazılır.','P(x) → P(x)′'),
  A('Cümle kur','Sınava girmeyen en az bir öğrenci vardır.','(∃x) P(x)′')],
 '“Her … dir”in olumsuzu “… olmayan en az bir … vardır”dır.',
 sira=yer(O16['C'][0],[O16['A'][0],O16['B'][0],O16['D'][0],O16['E'][0]],'C'))

# ---------- 17 orta · doğruluk kümesi ----------
A17=range(1,9); p17=lambda x:x%2==0; q17=lambda x:x>5
ts=lambda f:[x for x in A17 if f(x)]
assert ts(lambda x:(not p17(x)) or q17(x))==[1,3,5,6,7,8]
assert len(ts(lambda x:p17(x) and q17(x)))==2 and len(ts(lambda x:not p17(x)))==4 and len(ts(lambda x:p17(x) or q17(x)))==5 and len(ts(lambda x:(not q17(x)) or p17(x)))==7
Q('0017','mnt-acik','orta','Açık Önerme','Koşullu bir açık önermenin doğruluk kümesinin eleman sayısını bulur.','düz',
 'K-MNT-07 (doğruluk kümesi) · p(x) ⇒ q(x)',
 'A = {1, 2, 3, 4, 5, 6, 7, 8} kümesinde tanımlı\np(x) : x çift sayıdır.\nq(x) : x > 5\naçık önermeleri veriliyor.\nBuna göre, p(x) ⇒ q(x) önermesinin doğruluk kümesi kaç elemanlıdır?',
 6,
 [(2,'⇒ yerine ∧ kullanmış: x çift ve 5’ten büyük olan {6, 8} kümesini bulmuş.','bilgi'),
  (4,'p(x)’in değilinin (tek sayılar) doğruluk kümesini bulmuş; q(x)’in doğru olduğu çift sayıları katmamış.','dikkat'),
  (5,'⇒ yerine ∨ kullanmış: {2, 4, 6, 7, 8} kümesini saymış.','bilgi'),
  (7,'Koşullunun yönünü ters okuyup q(x) ⇒ p(x)’in doğruluk kümesini bulmuş.','bilgi')],
 'p(x) ⇒ q(x)’in doğruluk kümesinin eleman sayısı.',
 'Her x için önce p(x) ve q(x)’in değerine bak; koşullu hangi x değerlerinde yanlıştır, onları ele.',
 [ACIK,KOS,TC],
 [A('Yanlış olduğu değerler','p ⇒ q yalnız p doğru, q yanlış iken yanlıştır.','x çift ve x ≤ 5: {2, 4}'),
  A('Diğerleri doğru','Bütün A’dan bu iki değeri çıkar.','{1, 3, 5, 6, 7, 8}'),
  A('Say','Doğruluk kümesinin eleman sayısı.','8 − 2 = 6')],
 'Koşullunun doğruluk kümesi, yanlış yapan değerlerin tümleyenidir.',
 )

# ---------- 18 orta · “veya” koşullu kural (öncüllü, hikâyeli) ----------
pr18=['(a ∨ e) ⇒ k','k′']; vs18=['a','e','k']
I18=['a','e′','a′ ∧ e′']
r18=[kesin(pr18,f,vs18) for f in I18]; assert r18==[False,True,True]
assert kesin(pr18,'a′',vs18) and not kesin(pr18,'a',vs18)
L18=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
Q('0018','mnt-cikarim','orta','Çıkarım','“Veya” koşullu bir kuralın sonucundan hangi ifadelerin kesin olduğunu belirler.','öncüllü',
 'K-MNT-06 (hikâyeli çıkarım) · asansör, elektrik ve jeneratör',
 'Bir sitenin yönetimi şu kuralı koymuştur: “Asansör bozulursa veya elektrik kesilirse jeneratör çalıştırılır.” Bir gün jeneratörün çalıştırılmadığı biliniyor.\nBuna göre,\nI. Asansör bozulmuştur.\nII. Elektrik kesilmemiştir.\nIII. Asansör bozulmamıştır ve elektrik kesilmemiştir.\nifadelerinden hangileri kesinlikle doğrudur?',
 'II ve III',
 [('Yalnız I','Jeneratör çalışmadığı için asansörün bozulduğunu sanmış; sonucu koşul yerine koymuş.','bilgi'),
  ('Yalnız II','Elektrik kesilmediğini bulmuş ama “veya” koşulunun asansörü de kapsadığını görüp III’ü sınamamış.','dikkat'),
  ('I ve II','(a ∨ e)′ ≡ a ∧ e′ yazmış: De Morgan’da yalnız bir terimi değillemiş.','bilgi'),
  ('I, II ve III','I’deki “bozulmuştur” ifadesini “bozulmamıştır” gibi okuyup üçünü de kesin saymış.','dikkat')],
 'Kesinlikle doğru olan ifadeler.',
 'Kuralın sonucu gerçekleşmediğinde, kuralın koşulundaki iki durumdan her biri için ne söylenebileceğini ayrı ayrı sına.',
 [CIK,DEM],
 [A('Önermeleri yaz','a : Asansör bozuldu. e : Elektrik kesildi. k : Jeneratör çalıştırıldı.','(a ∨ e) ⇒ k ve k′'),
  A('Karşıt tersi','k′ doğruysa koşul gerçekleşmemiştir.','(a ∨ e)′ doğru'),
  A('De Morgan','Değili aç.','a′ ∧ e′ doğru'),
  A('Öncülleri sına','Asansör bozulmamış ve elektrik kesilmemiştir; I yanlış, II ve III doğrudur.','II ve III')],
 '“A veya B” koşulu gerçekleşmeden sonuç yoksa, hem A hem B gerçekleşmemiştir.',
 sira=L18)

# ---------- 19 zor · doğruluk kümesi toplamı ----------
A19=range(1,13); p19=lambda x:x%3==0; q19=lambda x:x<=5; r19=lambda x:x%2==1
f19=lambda x:(not (p19(x) or q19(x))) or r19(x)
yl=[x for x in A19 if not f19(x)]; assert yl==[2,4,6,12] and sum(yl)==24
assert sum(x for x in A19 if f19(x))==78-24==54
assert sum(x for x in A19 if q19(x) and not r19(x))==6 and sum(x for x in A19 if p19(x) and not r19(x))==18 and sum(x for x in A19 if p19(x) or q19(x))==42
Q('0019','mnt-acik','zor','Açık Önerme','Üç açık önermeden kurulan koşullu önermeyi yanlış yapan değerleri bulup toplar.','düz',
 'K-MNT-07 (açık önerme, doğruluk kümesi) · yanlış yapan değerlerin toplamı',
 'A = {1, 2, 3, …, 12} kümesinde tanımlı\np(x) : x, 3’ün katıdır.\nq(x) : x ≤ 5\nr(x) : x tek sayıdır.\naçık önermeleri veriliyor.\nBuna göre, (p(x) ∨ q(x)) ⇒ r(x) önermesini yanlış yapan x değerlerinin toplamı kaçtır?',
 24,
 [(6,'Yanlış yapan çiftlerden yalnız q(x)’i sağlayan {2, 4} değerlerini toplamış; 3’ün katı olan çiftleri unutmuş.','dikkat'),
  (18,'Yalnız p(x)’i sağlayan çiftleri ({6, 12}) toplamış; x ≤ 5 olan çiftleri unutmuş.','dikkat'),
  (42,'Yanlış yapan değerler yerine koşulun “∨” kısmını sağlayan tüm x değerlerini toplamış.','bilgi'),
  (54,'Önermeyi yanlış yapanlar yerine doğru yapan x değerlerini toplamış (78 − 24).','dikkat')],
 'Önermeyi yanlış yapan x değerlerinin toplamı.',
 'Koşullu önermenin yanlış olduğu durumu yaz; sonra bu durumun x için ne demek olduğunu 1’den 12’ye kadar sayılarda ara.',
 [ACIK,KOS,TC],
 [A('Yanlış olma şartı','a ⇒ b yalnız a doğru, b yanlış iken yanlıştır.','(p ∨ q) doğru ve r yanlış'),
  A('r yanlış','r(x) yanlışsa x çift sayıdır.','x ∈ {2, 4, 6, 8, 10, 12}'),
  A('p ∨ q doğru','Çiftlerden 3’ün katı olan ya da 5’e kadar olanlar.','2, 4 (≤ 5) · 6, 12 (3’ün katı)'),
  A('Topla','Yanlış yapan değerler {2, 4, 6, 12}.','2 + 4 + 6 + 12 = 24')],
 'Koşullunun yanlış olduğu durumu (a doğru, b yanlış) bulup sayılarda ara; doğru yapanları toplamak tuzaktır.',
 )

# ---------- 20 zor · model sayma ----------
F20='(p ⇒ q) ∧ (r ⇒ s) ∧ (p ∨ r)'; vs4=['p','q','r','s']
n20=len(modeller(F20,vs4)); assert n20==5
cnt=lambda f:len(modeller(f,vs4))
assert cnt('(p ⇔ q) ∧ (r ⇔ s) ∧ (p ∨ r)')==3
assert cnt('(p ⇒ q) ∧ (r ⇒ s)')==9
assert cnt('(p ⇒ q) ∧ (r ⇒ s) ∧ ((p ∧ r′) ∨ (p′ ∧ r))')==4
c_p=len([m for m in itertools.product([0,1],repeat=4) if V('(p ⇒ q) ∧ (r ⇒ s) ∧ p',p=m[0],q=m[1],r=m[2],s=m[3])]); c_r=len([m for m in itertools.product([0,1],repeat=4) if V('(p ⇒ q) ∧ (r ⇒ s) ∧ r',p=m[0],q=m[1],r=m[2],s=m[3])])
assert (c_p,c_r)==(3,3)
Q('0020','mnt-bulma','zor','Doğruluk Değerinden Önerme Bulma','Bileşik önermeyi doğru yapan (p, q, r, s) doğruluk değeri dörtlülerinin sayısını tarama mantığıyla bulur.','düz',
 'K-MNT-03 (model sayma) · iki koşullu ve bir “veya”',
 'p, q, r ve s birer önermedir.\n(p ⇒ q) ∧ (r ⇒ s) ∧ (p ∨ r)\nbileşik önermesinin doğru olması için p, q, r ve s önermelerinin doğruluk değerleri kaç farklı şekilde seçilebilir?',
 5,
 [(3,'⇒ bağlaçlarını ⇔ gibi okumuş: (p, q) ve (r, s) eşit değerli, p ∨ r şartıyla 2 × 2 − 1 = 3 bulmuş.','bilgi'),
  (4,'p ∨ r şartını “ya p ya da r (yalnız biri)” okuyup ikisi birden doğru olan durumu saymamış.','bilgi'),
  (6,'p ∨ r için p doğru olan 3 durumu ve r doğru olan 3 durumu toplamış; ikisinin birden doğru olduğu durumu iki kez saymış.','islem'),
  (9,'p ∨ r şartını hiç uygulamamış; yalnız iki koşullu önermeyi 3 × 3 olarak saymış.','dikkat')],
 'Doğruluk değerlerinin farklı seçim sayısı.',
 'Önce (p, q) ve (r, s) ikilileri için koşullunun doğru olduğu durumları say; sonra “veya” koşulunu kaldır.',
 [KOS,VEVEYA],
 [A('(p, q) seçenekleri','p ⇒ q yalnız (1, 0) iken yanlıştır.','(0, 0); (0, 1); (1, 1): 3 durum'),
  A('(r, s) seçenekleri','r ⇒ s için de aynı.','(0, 0); (0, 1); (1, 1): 3 durum'),
  A('Birleştir','Üç ve üç durum birlikte seçilir.','3 × 3 = 9'),
  A('p ∨ r şartı','p = 0 ve r = 0 olan durumlar çıkarılır: (p, q) ∈ {(0, 0), (0, 1)} ve (r, s) ∈ {(0, 0), (0, 1)}.','9 − 2 × 2 = 5')],
 '“Veya”nın yanlış olduğu (ikisi de 0) durumları toplamdan çıkar; çift sayım yapma.',
 )

# ---------- 21 zor · dört önerme, tek model (hikâyeli) ----------
F21='(p ⇒ q)′ ∧ (r ⇒ p′) ∧ (s ∨ r)'; m21=modeller(F21,['p','q','r','s']); assert m21==[(1,0,0,1)]
O21={'Yalnızca balıkçıda yemek yemiştir.':(0,0,0,1),'Yalnızca bisiklet kiralamış ve sahilde yürümüştür.':(1,1,0,0),'Yalnızca bisiklet kiralamış ve balıkçıda yemek yemiştir.':(1,0,0,1),'Yalnızca sahilde yürümüş ve balıkçıda yemek yemiştir.':(0,1,0,1),'Yalnızca bisiklet kiralamış, müzeyi gezmiş ve balıkçıda yemek yemiştir.':(1,0,1,1)}
k21=list(O21); assert [k for k,v in O21.items() if v in m21]==[k21[2]]
g=lambda f,k:V(f,p=O21[k][0],q=O21[k][1],r=O21[k][2],s=O21[k][3])
assert g('(p ⇒ q)′ ∧ (r ⇒ p′)',k21[1])==0
assert g('(p ⇒ q) ∧ (r ⇒ p′) ∧ (s ∨ r)',k21[2])==0 and g('(p ⇒ q) ∧ (r ⇒ p′) ∧ (s ∨ r)',k21[0])==1 and g('(p′ ∧ q) ∧ (r ⇒ p′) ∧ (s ∨ r)',k21[3])==1 and g('(p ⇒ q)′ ∧ (r ⇒ p) ∧ (s ∨ r)',k21[4])==1
Q('0021','mnt-bulma','zor','Doğruluk Değerinden Önerme Bulma','Üç parçalı bileşik önermenin doğruluğundan dört önermenin değerlerini zincirleme bulur.','hikâyeli',
 'K-MNT-03 (p, q, r, s bulma) · hafta sonu gezisi',
 'Deniz’in hafta sonu gezisi için\np : Bisiklet kiraladı.\nq : Sahilde yürüyüş yaptı.\nr : Müzeyi gezdi.\ns : Akşam yemeğini balıkçıda yedi.\nönermeleri veriliyor. (p ⇒ q)′ ∧ (r ⇒ p′) ∧ (s ∨ r) önermesinin doğru olduğu bilindiğine göre, Deniz bu gezide aşağıdakilerden hangisini yapmıştır?',
 k21[2],
 [(k21[0],'(p ⇒ q)′ doğruluğundan p = 0 sonucunu çıkarmış; oysa koşullunun yanlış olması p = 1, q = 0 demektir.','bilgi'),
  (k21[1],'p ⇒ q yanlışken q = 1 almış ve s ∨ r şartını denetlememiş.','dikkat'),
  (k21[3],'p ⇒ q yanlışken p = 0, q = 1 almış; böylece r ⇒ p′ ve s ∨ r şartlarını sağlamış sanmış.','bilgi'),
  (k21[4],'r ⇒ p′ koşulunu r ⇒ p gibi okumuş; r = 1 ve p = 1 alınca “doğru” sanmış.','bilgi')],
 'Deniz’in gezide yaptığı etkinlikler.',
 'Üç parçalı “ve” bileşiğinin doğru olması için üç parçanın da 1 olması gerektiğini kullan; en kesin bilgi veren parçadan başla.',
 [VEVEYA,KOS],
 [A('Parçaları ayır','“Ve” bileşiği doğruysa üçü de doğrudur.','(p ⇒ q)′ = 1 · r ⇒ p′ = 1 · s ∨ r = 1'),
  A('Birinci parça','(p ⇒ q)′ = 1 ise p ⇒ q yanlıştır.','p = 1 · q = 0'),
  A('İkinci parça','p = 1 iken p′ = 0; r ⇒ 0 doğruysa r = 0 olmalıdır.','r = 0'),
  A('Üçüncü parça','r = 0 iken s ∨ r doğruysa s = 1.','s = 1'),
  A('Cevap','Bisiklet kiralamış, balıkçıda yemiş; yürüyüş ve müze yok.','p = 1 · q = 0 · r = 0 · s = 1')],
 'Koşullunun yanlışlığı kesin değer verir (1, 0); sonra diğer parçaları bu değerlerle sırayla çöz.',
 sira=yer(k21[2],[k21[0],k21[1],k21[3],k21[4]],'D'))

# ---------- 22 zor · Murat zinciri (öncüllü) ----------
pr22=['a ⇒ b','b ⇒ c','d ⇒ b′','d']; vs22=['a','b','c','d']
I22=['c′','a′','b′']
assert [kesin(pr22,f,vs22) for f in I22]==[False,True,True]
L22=['Yalnız II','Yalnız III','I ve III','II ve III','I, II ve III']
Q('0022','mnt-cikarim','orta','Çıkarım','Koşullu önermelerden oluşan zincirde karşıt tersi kullanıp kesin sonuçları bulur; ters hatasını eler.','öncüllü',
 'K-MNT-06 (hikâyeli çıkarım) · yağmur, maç ve ödev zinciri',
 'Murat’ın bir günü için şu bilgiler veriliyor:\n• Yağmur yağarsa maç ertelenir.\n• Maç ertelenirse Murat ödevini yapar.\n• Murat sinemaya giderse maç ertelenmemiştir.\nMurat’ın o gün sinemaya gittiği bilindiğine göre,\nI. Murat ödevini yapmamıştır.\nII. Yağmur yağmamıştır.\nIII. Maç ertelenmemiştir.\nifadelerinden hangileri kesinlikle doğrudur?',
 'II ve III',
 [('Yalnız II','Yağmurun yağmadığını görmüş ama maçın ertelenmediği ara sonucunu kesin saymamış.','dikkat'),
  ('Yalnız III','Zinciri bir adım yürütüp durmuş; maç ertelenmediyse yağmurun da yağmadığını (karşıt tersi) görmemiş.','dikkat'),
  ('I ve III','Maç ertelenmediği için ödevin yapılmadığını sanmış (b ⇒ c’nin tersini kullanmış); yağmura kadar zinciri sürdürmemiş.','bilgi'),
  ('I, II ve III','Maç ertelenmedi diye ödev yapılmadı sanmış (ters hatası); doğru sonuçları da bulduğu için üçünü seçmiş.','bilgi')],
 'Kesinlikle doğru olan ifadeler.',
 'Murat’ın sinemaya gittiği bilgisinden başla; her koşullunun karşıt tersini hangi yönde işletebildiğini ayrı ayrı sına.',
 [CIK,KOS],
 [A('Önermeleri yaz','a : Yağmur yağdı. b : Maç ertelendi. c : Murat ödevini yaptı. d : Murat sinemaya gitti.','a ⇒ b; b ⇒ c; d ⇒ b′; d = 1'),
  A('Maçı bul','d doğru ve d ⇒ b′ doğru olduğundan b′ doğrudur.','Maç ertelenmemiştir (III)'),
  A('Yağmuru bul','a ⇒ b’nin karşıt tersi: b′ ⇒ a′.','Yağmur yağmamıştır (II)'),
  A('Ödevi sına','b = 0 iken b ⇒ c hakkında bilgi vermez; ödev yapılmış da yapılmamış da olabilir.','I kesin değildir'),
  A('Sonuç','II ve III kesinlikle doğrudur.','II ve III')],
 'Koşullunun “ise” kısmı gerçekleşmediyse sonuç hakkında bilgi yoktur; kesin olan karşıt tersi yönüdür.',
 sira=L22)

# ---------- 23 zor · basketbol (öncüllü) ----------
pr23=['a ∨ b','a ⇒ c','b ⇒ d′','c′']; vs23=['a','b','c','d']
I23=['a′','b','d′']
assert [kesin(pr23,f,vs23) for f in I23]==[True,True,True]
Q('0023','mnt-cikarim','zor','Çıkarım','“Veya” ve iki koşullu önermeyi birlikte kullanarak üç kesin sonuca ulaşır.','öncüllü',
 'K-MNT-06 (hikâyeli çıkarım) · antrenörün kadro kuralları',
 'Bir basketbol antrenörü maç kadrosu için şunları söylüyor:\n• Ali ile Burak’tan en az biri oynayacak.\n• Ali oynarsa Can da oynayacak.\n• Burak oynarsa Deniz oynamayacak.\nCan’ın oynamadığı bilindiğine göre,\nI. Ali oynamamıştır.\nII. Burak oynamıştır.\nIII. Deniz oynamamıştır.\nifadelerinden hangileri kesinlikle doğrudur?',
 'I, II ve III',
 [('Yalnız I','Ali’nin oynamadığını bulup durmuş; “en az biri” koşulundan Burak’ın oynadığını çıkarmamış.','dikkat'),
  ('I ve II','Burak oynarsa Deniz oynamaz koşulunu son adımda kullanmayı unutmuş.','dikkat'),
  ('I ve III','“Ali oynamadı” sonucundan Deniz’e atlamış; Burak’ın oynadığı ara halkasını görmemiş.','dikkat'),
  ('II ve III','Ali’nin oynamamasını (karşıt tersi) bulamayıp Burak’ı doğrudan “Can oynamadı” bilgisinden çıkarmış.','bilgi')],
 'Kesinlikle doğru olan ifadeler.',
 'Can’ın oynamaması hangi koşulun sonucunu ortadan kaldırır? Çıkardığın her sonucu sıradaki koşulda kullan.',
 [CIK,VEVEYA],
 [A('Önermeleri yaz','a, b, c, d: Ali, Burak, Can, Deniz oynadı.','a ∨ b; a ⇒ c; b ⇒ d′; c′'),
  A('Ali’yi bul','c′ ve a ⇒ c: karşıt tersiyle a′.','Ali oynamamıştır (I)'),
  A('Burak’ı bul','a ∨ b doğru, a yanlış ise b doğrudur.','Burak oynamıştır (II)'),
  A('Deniz’i bul','b doğru ve b ⇒ d′ doğru olduğundan d′ doğrudur.','Deniz oynamamıştır (III)')],
 'Kesin bilgiyle başlayıp her çıkarımı bir sonraki koşulda kullan; zincirin her halkası kesindir.',
 sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'])

# ---------- 24 zor · bileşik niceleyicili önermenin olumsuzu ----------
# S = (∀x P(x)) ∧ (∃x Q(x)); P: x² ≥ 0, Q: x + 1 = 0. Soyut alan 3 elemanlı, tüm P, Q dağılımları taranır.
dom=list(itertools.product([0,1],repeat=3))
S24=lambda Pp,Qq:all(Pp) and any(Qq)
O24={'A':('(∃x ∈ ℝ) x² < 0  ∨  (∀x ∈ ℝ) x + 1 ≠ 0',lambda Pp,Qq:any(not v for v in Pp) or all(not v for v in Qq)),
     'B':('(∃x ∈ ℝ) x² < 0  ∧  (∀x ∈ ℝ) x + 1 ≠ 0',lambda Pp,Qq:any(not v for v in Pp) and all(not v for v in Qq)),
     'C':('(∀x ∈ ℝ) x² < 0  ∨  (∃x ∈ ℝ) x + 1 ≠ 0',lambda Pp,Qq:all(not v for v in Pp) or any(not v for v in Qq)),
     'D':('(∃x ∈ ℝ) x² ≤ 0  ∨  (∀x ∈ ℝ) x + 1 ≠ 0',None),
     'E':('(∃x ∈ ℝ) x² < 0  ∨  (∃x ∈ ℝ) x + 1 ≠ 0',lambda Pp,Qq:any(not v for v in Pp) or any(not v for v in Qq))}
eq24=[k for k,(_,f) in O24.items() if f and all(f(Pp,Qq)==(not S24(Pp,Qq)) for Pp in dom for Qq in dom)]; assert eq24==['A']
assert (0*0>=0) and (0*0<=0) and not (0*0<0)   # D: x² ≤ 0, x² ≥ 0’ın değili (x² < 0) değildir (x = 0)
sh=lambda k:O24[k][0]
Q('0024','mnt-nicelik','zor','Niceleyiciler','“Ve” ile bağlı ∀ ve ∃ niceleyicili bileşik önermenin olumsuzunu bulur.','düz',
 'K-MNT-05 (bileşik niceleyici olumsuzu) · ∀ ∧ ∃',
 '[(∀x ∈ ℝ) x² ≥ 0]  ∧  [(∃x ∈ ℝ) x + 1 = 0]\nönermesinin olumsuzu aşağıdakilerden hangisidir?',
 sh('A'),
 [(sh('B'),'Bağlacı değiştirmemiş: “ve”nin olumsuzunu yine “ve” yazmış; niceleyicileri ve özellikleri doğru değillemiş.','bilgi'),
  (sh('C'),'Bağlacı değiştirmiş ama niceleyicileri değiştirmemiş: ∀ ve ∃’yı yerinde bırakıp yalnız özellikleri değillemiş.','bilgi'),
  (sh('D'),'x² ≥ 0 özelliğinin değilini x² ≤ 0 almış; x = 0 için x² ≥ 0 ve x² ≤ 0 ikisi de doğrudur.','bilgi'),
  (sh('E'),'İkinci niceleyiciyi ∃ olarak bırakmış; ∃x, Q’nun değili ∀x, Q′ olmalıdır.','bilgi')],
 'Verilen önermenin olumsuzu.',
 'Önce “ve” ile bağlı iki parçanın her birini ayrı ayrı değille; sonra bağlacı düşün.',
 [NIC,DEM],
 [A('Bağlaç','(a ∧ b)′ ≡ a′ ∨ b′.','Olumsuz “veya” ile bağlanır'),
  A('Birinci parça','(∀x, x² ≥ 0)′ ≡ ∃x, x² < 0.','(∃x ∈ ℝ) x² < 0'),
  A('İkinci parça','(∃x, x + 1 = 0)′ ≡ ∀x, x + 1 ≠ 0.','(∀x ∈ ℝ) x + 1 ≠ 0'),
  A('Birleştir','İki olumsuzu “veya” ile bağla.',sh('A').replace('  ',' '))],
 'Bileşik niceleyicili önermede önce bağlacı De Morgan ile değiştir, sonra her parçada ∀ ↔ ∃ yapıp özelliği değille.',
 sira=yer(sh('A'),[sh('B'),sh('C'),sh('D'),sh('E')],'D'))

# ---------- 25 zor · tablo ----------
T25=[('Akasya',1,1,0),('Bozkır',1,0,0),('Çınar',0,0,0),('Doğan',0,1,1),('Erguvan',1,1,1),('Fidan',0,1,0)]
F25='(p ⇒ q) ∧ (q ⇒ r′)'
set25=lambda f:[n for n,a,b,c in T25 if V(f,p=a,q=b,r=c)]
assert set25(F25)==['Akasya','Çınar','Fidan']
assert set25('(p ⇒ q) ∧ (q ⇒ r)')==['Çınar','Doğan','Erguvan']
assert set25('(p ⇔ q) ∧ (q ⇒ r′)')==['Akasya','Çınar']
assert set25('(p ⇒ q) ∧ (r′ ⇒ q)')==['Akasya','Doğan','Erguvan','Fidan']
assert set25('q ⇒ r′')==['Akasya','Bozkır','Çınar','Fidan']
nm=lambda l:', '.join(l)
tab25=tablo_svg(['Takım','p','q','r'],[[n,str(a),str(b),str(c)] for n,a,b,c in T25])
Q('0025','mnt-acik','orta','Açık Önerme','Tabloda verilen doğruluk değerlerine iki koşullu bileşik önermeyi satır satır uygulayıp doğru olanları belirler.','tablo',
 'K-MNT-07 (tablodan değer bulma) · takımların durumları',
 'Bir lig maçı öncesinde takımlar için\np : Takım ev sahibidir.\nq : Takım önceki maçını kazanmıştır.\nr : Takımın sakat oyuncusu vardır.\nönermeleri yazılıyor. Aşağıdaki tabloda her takım için bu önermelerin doğruluk değerleri verilmiştir.\nBuna göre, (p ⇒ q) ∧ (q ⇒ r′) önermesi hangi takımlar için doğrudur?',
 nm(set25(F25)),
 [(nm(set25('(p ⇒ q) ∧ (q ⇒ r)')),'r′ yerine r’yi almış: (p ⇒ q) ∧ (q ⇒ r) önermesini hesaplamış.','dikkat'),
  (nm(set25('(p ⇔ q) ∧ (q ⇒ r′)')),'p ⇒ q koşullusunu p ⇔ q gibi okumuş; p = 0, q = 1 satırlarını yanlış saymış.','bilgi'),
  (nm(set25('(p ⇒ q) ∧ (r′ ⇒ q)')),'İkinci koşulluyu karşıt tersi yerine ters yönlü (r′ ⇒ q) yazmış.','bilgi'),
  (nm(set25('q ⇒ r′')),'İlk koşullu p ⇒ q’yu hesaba katmamış; yalnız q ⇒ r′’ya bakmış.','dikkat')],
 'Önermenin doğru olduğu takımlar.',
 'Her takımın satırı için önce iki koşullunun değerini ayrı ayrı bul; sonra “ve” ile birleştir.',
 [KOS,VEVEYA],
 [A('Satır satır p ⇒ q','p = 1, q = 0 olan takım yanlış verir.','Bozkır’da 1 ⇒ 0 = 0; diğerlerinde 1'),
  A('Satır satır q ⇒ r′','q = 1 ve r = 1 olan takım yanlış verir.','Doğan (1, 1) ve Erguvan (1, 1) yanlış'),
  A('İkisini birleştir','İki koşullu da doğruysa bileşik doğrudur.','Akasya, Çınar, Fidan')],
 'Tabloda her satıra bileşiğin parçalarını ayrı ayrı uygula; koşullu yalnız (1, 0) satırında yanlıştır.',
 sira=yer(nm(set25(F25)),[nm(set25('(p ⇒ q) ∧ (q ⇒ r)')),nm(set25('(p ⇔ q) ∧ (q ⇒ r′)')),nm(set25('(p ⇒ q) ∧ (r′ ⇒ q)')),nm(set25('q ⇒ r′'))],'E'),sekil=tab25)

bitir(P,'mantik',UK)
