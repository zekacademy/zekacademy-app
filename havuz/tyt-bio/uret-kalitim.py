import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
from collections import Counter
def _num(t):
    try: return Fr(t.replace('−','-').replace(',','.').strip())
    except Exception: return None
def _opts(o):
    if all(_num(x[0]) is not None for x in o): o=sorted(o,key=lambda x:_num(x[0]))
    L='ABCDE'; assert len(o)==5
    sik=[L[i] for i,x in enumerate(o) if x[1] is None]; assert len(sik)==1,sik
    return [x[0] for x in o],sik[0],{L[i]:x[1] for i,x in enumerate(o) if x[1] is not None},{L[i]:x[2] for i,x in enumerate(o) if x[1] is not None}
KARTLAR=[]
def Q(P,pre,no,tipId,tip,zor,alt,kaz,kalip,adim,fikir,tuzak,bilgi,puf,a,k,ozet,degisti,kisa=None):
    kid=f'K-{pre}-{int(no):02d}'
    KARTLAR.append(dict(id=kid,konu=P.konu_adi,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak='ÖSYM 2018–2026 TYT Biyoloji dağılımı · MEB 9–10. sınıf biyoloji'))
    s,c,cel,tur=_opts(a['o'])
    P.R(no,tipId,tip,zor,alt,kaz,kalip,adim,f'{kid} ({ozet}) · {degisti}',a['m'],s,c,a['i'],a['ip'],bilgi,a['ad'],puf,cel,tur,kisa=kisa)
    s,c,cel,tur=_opts(k['o'])
    P.K(no,k['m'],s,c,k.get('i',a['i']),k.get('ip',a['ip']),k.get('bilgi',bilgi),k['ad'],k.get('puf',puf),cel,tur,kisa=kisa)
def bitir(P,onek,konu,uyg,n_ana):
    assert len(P.ANA)==n_ana==len(P.KAR),(len(P.ANA),len(P.KAR))
    tipler={}
    for k in KARTLAR: tipler.setdefault(k['tipId'],dict(tipId=k['tipId'],ad=k['tip'],kartlar=[],uygulamaKonu=uyg))['kartlar'].append(k['id'])
    json.dump(dict(konu=konu,surum=1,kartlar=KARTLAR,tipler=list(tipler.values())),open(os.path.join(H,'..','kartlar',onek+'.json'),'w'),ensure_ascii=False,indent=1)
    P.yaz(os.path.join(H,onek+'-1.json'),os.path.join(H,onek+'-1-kardes.json'))
    print('zorluk',Counter(q['zorluk'] for q in P.ANA),'tipler',len(tipler))
P=Parti('kalitim','Kalıtım','bio|Kalıtım',ders='TYT Biyoloji',idon='tytbio')
PRE='BKA'
def fs(x):
    x=Fr(x); return '0' if x==0 else (str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}')
def gam(g):
    return [''.join(x) for x in product(*[g[i:i+2] for i in range(0,len(g),2)])]
def cross(g1,g2):
    c=Counter()
    for a in gam(g1):
        for b in gam(g2):
            c[''.join(''.join(sorted(a[i]+b[i])) for i in range(len(a)))]+=1
    return c
def pr(c,f): return Fr(sum(v for g,v in c.items() if f(g)),sum(c.values()))
def abo(p1,p2):
    c=Counter()
    for a in p1:
        for b in p2:
            s={a,b}; c['AB' if s=={'A','B'} else 'A' if 'A' in s else 'B' if 'B' in s else 'O']+=1
    return c
dom=lambda g,i: g[2*i].isupper() or g[2*i+1].isupper()
GEN=B('Gamet çeşidi','Her heterozigot gen çifti (Aa) 2 çeşit gamet verir, homozigot çift (AA, aa) 1 çeşit · Çeşit sayısı 2 üzeri heterozigot çift sayısıdır: AaBb → 2 × 2 = 4 çeşit')
BAS=B('Baskın ve çekinik','Baskın alel (A) heterozigotta da kendini gösterir; çekinik alel (a) yalnız homozigotta görünür · AA ve Aa baskın fenotip, aa çekinik fenotiptir')
CAP=B('Çaprazlama','Aa × Aa → AA : Aa : aa = 1 : 2 : 1 (fenotip 3 : 1) · Aa × aa → Aa : aa = 1 : 1 · Bağımsız iki özellikte olasılıklar çarpılır')
ABO=B('ABO kan grupları','A grubu: AA ya da AO · B grubu: BB ya da BO · AB grubu: AB · O grubu: OO · A ve B alelleri O’ya baskındır, birbirlerine eş baskındır')
RH=B('Rh faktörü','Rh+ baskın (R), Rh− çekiniktir (r) · Rh+ birey RR ya da Rr, Rh− birey rr’dir')
XB=B('Eşeye bağlı kalıtım','Renk körlüğü ve hemofili X kromozomundaki çekinik alellerle taşınır · Kadın XX, erkek XY · Erkek tek X taşıdığı için çekinik alel erkekte tek başına etkili olur')
CAP2=B('Koşullu olasılık','Soru “…olanlar arasından seçilen birey” diyorsa payda tüm yavrular değil, o koşulu sağlayan yavrulardır: olasılık = istenen sayı ÷ koşulu sağlayanların sayısı')
# 0001
assert len(set(gam('AaBbCC')))==4 and len(set(gam('AaBBCcDd')))==8
Q(P,PRE,'0001','kl-gamet','Gamet çeşidi sayısı','kolay','Gametler','Genotipten oluşabilecek gamet çeşidi sayısını bulur.','düz',2,
 'Heterozigot gen çifti sayısından gamet çeşidi bulunur.','Homozigot çifti de gamet çeşidi sayısına katmak.',[GEN],
 'Gamet çeşidi sayısı = 2 üzeri heterozigot gen çifti sayısı.',
 dict(m='Genler bağımsız ayrılır ve krossing-over olmaz.\nGenotipi AaBbCC olan bir bireyin oluşturabileceği farklı gamet çeşidi sayısı kaçtır?',i='Farklı gamet çeşidi sayısı.',ip=['Hangi gen çiftleri heterozigot?','Homozigot çift kaç çeşit alel verir?','Her heterozigot çift çeşit sayısını iki katına çıkarır.'],
  o=[('2','Yalnız bir heterozigot çifti saymak.','islem'),('4',None,None),('6','Gen çifti sayısını 2 ile çarpmak.','islem'),('8','Homozigot CC çiftini de iki çeşit saymak.','bilgi'),('12','Gen çifti sayısını 4 ile çarpmak.','islem')],
  ad=[A('Heterozigotları bul','Aa ve Bb heterozigot, CC homozigottur.','2 heterozigot çift'),A('Çeşitleri say','Aa 2, Bb 2, CC 1 çeşit alel verir.','2 × 2 × 1'),A('Gametleri yaz','ABC, AbC, aBC, abC.','4 çeşit'),A('Sonuç','Farklı gamet çeşidi 4’tür.','4')]),
 dict(m='Genler bağımsız ayrılır ve krossing-over olmaz.\nGenotipi AaBBCcDd olan bir bireyde oluşabilecek farklı gamet çeşidi sayısı kaçtır?',
  o=[('2','Yalnız bir heterozigot çifti saymak.','islem'),('4','İki heterozigot çifti saymak, üçüncüyü atlamak.','islem'),('6','Heterozigot çift sayısını 2 ile çarpmak.','islem'),('8',None,None),('16','Homozigot BB çiftini de iki çeşit saymak.','bilgi')],
  ad=[A('Heterozigotları bul','Aa, Cc ve Dd heterozigot; BB homozigottur.','3 heterozigot çift'),A('Çeşitleri say','Her heterozigot çift 2, homozigot çift 1 çeşit verir.','2 × 1 × 2 × 2'),A('Sonuç','Farklı gamet çeşidi 8’dir.','8')]),
 'AaBbCC gamet çeşidi','dört gen çifti, farklı genotip')

# 0002
c=cross('Mm','Mm'); assert pr(c,lambda g:dom(g,0))==Fr(3,4); c2=cross('Kk','kk'); assert pr(c2,lambda g:g=='kk')==Fr(1,2)
Q(P,PRE,'0002','kl-monohibrit','Tek karakter çaprazlaması','kolay','Monohibrit çaprazlama','Tek özellik çaprazlamasında olasılığı hesaplar.','hikâyeli',2,
 'Tek gen çifti çaprazlaması; yavruda çekinik fenotip olasılığı sorulur.','Fenotip olasılığını genotip olasılığıyla karıştırmak.',[BAS,CAP],
 'Çaprazlamada önce ebeveyn gametlerini yaz, sonra kareyi doldur.',
 dict(m='Bezelyede mor çiçek rengi (M), beyaz çiçek rengi (m) üzerine baskındır. Heterozigot mor çiçekli iki bezelye çaprazlanıyor.\nBu çaprazlamadan elde edilen bir bezelyenin mor çiçekli olma olasılığı kaçtır?',i='Yavrunun mor çiçekli olma olasılığı.',ip=['İki ebeveynin genotipini yaz.','Her ebeveynden hangi gametler gelir?','Mor çiçek hangi genotiplerde görünür?'],
  o=[('0','Heterozigot ebeveynlerden mor yavru çıkmayacağını sanmak.','bilgi'),('1/4','Beyaz çiçekli olma olasılığını (mm) vermek.','dikkat'),('1/2','Yalnız heterozigot yavruların mor olduğunu sanmak.','bilgi'),('3/4',None,None),('1','Tüm yavruların mor olacağını sanmak.','bilgi')],
  ad=[A('Genotipleri yaz','Heterozigot mor çiçekli bezelye Mm genotipindedir.','Mm × Mm'),A('Gametler','Her ebeveyn M ve m gameti verir.','M ve m olmak üzere iki çeşit'),A('Yavru genotipleri','Kareyi doldurunca MM, Mm, Mm, mm çıkar.','1 MM : 2 Mm : 1 mm'),A('Sonuç','MM ve Mm mor çiçeklidir; mm beyazdır.','3/4')]),
 dict(m='Tavşanlarda kahverengi tüy rengi (K), krem tüy rengi (k) üzerine baskındır. Heterozigot kahverengi bir dişi tavşan, krem tüylü bir erkek tavşanla çiftleştiriliyor.\nBu çiftleşmeden doğan bir yavrunun krem tüylü olma olasılığı kaçtır?',
  o=[('1/8','Gamet sayısını yanlış sayıp olasılığı küçültmek.','islem'),('1/4','İki heterozigot çaprazlaması gibi düşünmek.','dikkat'),('1/2',None,None),('3/4','Baskın fenotip olasılığı kullanmak.','dikkat'),('1','Tüm yavruların krem olacağını sanmak.','bilgi')],
  ad=[A('Genotipleri yaz','Heterozigot dişi Kk, krem erkek kk genotipindedir.','Kk × kk'),A('Gametler','Dişi K ve k, erkek yalnız k verir.','dişi: K ve k, erkek: k'),A('Yavru genotipleri','Kk ve kk eşit olasılıkla oluşur.','1 Kk : 1 kk'),A('Sonuç','Krem yalnız kk genotipinde görünür.','1/2')]),
 'Mm × Mm çekinik olasılığı','tür, özellik ve çaprazlama (Kk × kk)')

# 0003
c=abo(['A','O'],['B','O']); assert Fr(c['AB'],4)==Fr(1,4); c=abo(['A','O'],['B','O']); assert Fr(c['A']+c['B'],4)==Fr(1,2)
Q(P,PRE,'0003','kl-abo','ABO kan grubu çaprazlaması','orta','Kan grupları','Çocuğun kan grubundan ebeveyn genotiplerini bulup sonraki çocuğun olasılığını hesaplar.','hikâyeli',3,
 'İlk çocuğun kan grubu ebeveynin heterozigot olduğunu gösterir; sonraki çocuk olasılığı bulunur.','Önceki çocuğun sonraki çocuğun olasılığını etkilediğini sanmak.',[ABO,CAP],
 'O grubu çocuk, her ebeveynden bir O aleli aldığını gösterir.',
 dict(m='A kan grubundan bir anne ile B kan grubundan bir babanın ilk çocuğu O kan grubundadır.\nBu çiftin ikinci çocuğunun AB kan grubunda olma olasılığı kaçtır?',i='İkinci çocuğun AB grubunda olma olasılığı.',ip=['O grubu çocuk hangi alelleri almıştır?','Anne ve babanın genotipleri ne olmalı?','Her çocuk için olasılık bağımsızdır.'],
  o=[('0','İlk çocuğun O olması nedeniyle AB’nin olamayacağını sanmak.','dikkat'),('1/16','Dört birleşmeyi 16 sanıp olasılığı küçültmek.','islem'),('1/8','Gamet olasılıklarını çarpıp bir kez daha bölmek.','islem'),('1/4',None,None),('1/2','A ve B alellerinden her birinin gelme olasılığını toplamak.','islem')],
  ad=[A('Genotipleri bul','İlk çocuk OO; her ebeveyn bir O vermiştir. Anne AO, baba BO olmalı.','AO × BO'),A('Yavru olasılıkları','Gametler A, O ve B, O; dört birleşme eşit olasılıklıdır.','AB, AO, BO, OO'),A('Sonuç','AB yalnız bir kutuda çıkar; her çocuk için olasılık aynıdır.','1/4')]),
 dict(m='A kan grubundan bir baba ile B kan grubundan bir annenin ilk çocuğu O kan grubundadır.\nBu çiftin ikinci çocuğunun A ya da B kan grubunda olma olasılığı kaçtır?',
  o=[('0','İlk çocuğun O olması nedeniyle A ve B’nin çıkamayacağını sanmak.','dikkat'),('1/8','Gamet olasılıklarını çarpıp bir kez daha bölmek.','islem'),('1/4','Yalnız tek bir grubun olasılığını vermek.','dikkat'),('3/8','Olasılıkları yanlış toplamak.','islem'),('1/2',None,None)],
  ad=[A('Genotipleri bul','İlk çocuk OO; her ebeveyn bir O vermiştir. Baba AO, anne BO olmalı.','AO × BO'),A('Yavru olasılıkları','Dört birleşme eşit olasılıklıdır.','AB, AO, BO, OO'),A('Sonuç','A grubu (AO) ve B grubu (BO) birer kutuda çıkar: 1/4 + 1/4.','1/2')]),
 'A ve B ebeveyn, O çocuk','istenen grup (AB yerine A ya da B)')

# 0004
def xk(m,f):
    c=Counter()
    for a in m:
        for b in f: c[(a,b)]+=1
    return c
c=xk(['XD','Xd'],['XD','Y']); assert Fr(c[('Xd','Y')],4)==Fr(1,4) and Fr(c[('Xd','Y')],c[('XD','Y')]+c[('Xd','Y')])==Fr(1,2)
c=xk(['XH','Xh'],['Xh','Y']); kiz=[k for k in c if k[1]!='Y']; assert Fr(sum(c[k] for k in kiz if k[0]=='Xh'),sum(c[k] for k in kiz))==Fr(1,2)
Q(P,PRE,'0004','kl-eseye-bagli','Eşeye bağlı kalıtım','orta','Eşeye bağlı kalıtım','Eşeye bağlı çekinik özellikte çocuğun cinsiyet ve fenotip olasılığını hesaplar.','hikâyeli',3,
 'X’e bağlı çekinik özellikte cinsiyet ve hastalık birlikte sorulur.','“Erkek ve hasta” olasılığı ile “erkek olduğu bilinen çocuk hasta” olasılığını karıştırmak.',[XB,CAP],
 'Eşeye bağlı sorularda cinsiyeti de olasılığa kat: koşul yoksa hepsi çarpılır.',
 dict(m='Renk körlüğü, X kromozomu üzerindeki çekinik bir alelle (Xd) belirlenir. Renk körlüğü bakımından taşıyıcı olan bir anne ile renk körü olmayan bir babanın çocukları olacaktır.\nBu çiftin doğacak çocuğunun renk körü bir erkek olma olasılığı kaçtır?',i='Çocuğun renk körü erkek olma olasılığı.',ip=['Anne XDXd, baba XDY genotipindedir; gametleri yaz.','Dört birleşmenin her birini yaz.','Soruda cinsiyet önceden verilmiş mi?'],
  o=[('1/4',None,None),('3/8','Olasılıkları toplamak.','islem'),('1/2','Çocuğun erkek olduğunu önceden bilinen koşul saymak.','dikkat'),('3/4','Renk körü olmayan çocukların olasılığını vermek.','dikkat'),('1','Tüm çocukların renk körü olacağını sanmak.','bilgi')],
  ad=[A('Genotipleri yaz','Taşıyıcı anne XDXd, sağlam baba XDY.','XDXd × XDY'),A('Birleşmeler','Dört eşit olasılıklı birleşme oluşur.','XDXD, XDXd, XDY, XdY'),A('Renk körü erkek','Renk körü erkek yalnız XdY genotipindedir.','4 birleşmeden 1’i'),A('Sonuç','Koşul yok; olasılık dört birleşmeden birine eşittir.','1/4')]),
 dict(m='Hemofili, X kromozomu üzerindeki çekinik bir alelle (Xh) belirlenir. Hemofili bakımından taşıyıcı bir anne ile hemofili hastası bir babanın çocukları olacaktır.\nBu çiftin doğacak kız çocuğunun hemofili hastası olma olasılığı kaçtır?',
  o=[('0','Anne taşıyıcı olduğundan kızların hasta olamayacağını sanmak.','bilgi'),('1/8','Gamet sayısını yanlış sayıp olasılığı küçültmek.','islem'),('1/4','Kız olma olasılığını ayrıca çarpmak; kız olduğu zaten verilmiş.','dikkat'),('3/8','Olasılıkları toplamak.','islem'),('1/2',None,None)],
  ad=[A('Genotipleri yaz','Taşıyıcı anne XHXh, hasta baba XhY.','XHXh × XhY'),A('Kız yavrular','Kız çocuk babadan Xh alır, anneden XH ya da Xh alır.','XHXh veya XhXh'),A('Hasta olan kızlar','Anneden Xh alan kız XhXh olur ve hastadır; iki seçenek eşit olasılıklıdır.','2 kız genotipinden 1’i'),A('Sonuç','Kız olduğu verildiği için yalnız kız yavrulara bakılır.','1/2')]),
 'X’e bağlı çekinik, taşıyıcı anne','hastalık, cinsiyet koşulu (kız olduğu bilinen)')

# 0005
c=cross('Aa','Aa'); assert pr(c,lambda g:g=='aa')==Fr(1,4)
Q(P,PRE,'0005','kl-soyagaci','Aile öyküsünden kalıtım yorumu','orta','Soyağacı yorumu','Aile öyküsünden baskın ya da çekinik kalıtımı ve genotipleri çıkarır.','öncüllü',3,
 'Ebeveynde olmayan özelliğin çocukta görünmesinden çekinik kalıtım çıkarılır.','Taşıyıcı ebeveynin olasılığını 1/2 sanmak.',[BAS,CAP],
 'Ebeveynde olmayan özellik çocukta ortaya çıkıyorsa özellik çekiniktir ve ebeveynler heterozigottur.',
 dict(m='Sağlıklı bir anne ile sağlıklı bir babanın ilk çocuğu bir hastalık bakımından hastadır. Hastalığın otozomal kromozomlarda tek gen çiftiyle belirlendiği bilinmektedir.\nBuna göre,\nI. Hastalık çekinik alelle belirlenir.\nII. Anne ve baba bu gen bakımından heterozigottur.\nIII. Çiftin sonraki çocuğunun hasta olma olasılığı 1/2’dir.\nifadelerinden hangileri doğrudur?',i='Doğru olan ifadeler.',ip=['Sağlıklı ebeveynden hasta çocuk doğması neyi gösterir?','Hasta çocuğun aleli hangi ebeveynden gelmiştir?','Heterozigot × heterozigotta çekinik olasılığı kaçtır?'],
  o=[('Yalnız I','Ebeveynlerin heterozigot olduğunu fark etmemek.','bilgi'),('Yalnız II','Hastalığın çekinik olduğunu çıkaramamak.','bilgi'),('I ve II',None,None),('I ve III','Heterozigot × heterozigotta çekinik olasılığını 1/2 sanmak.','bilgi'),('I, II ve III','III’ü doğru saymak; olasılık 1/4’tür.','islem')],
  ad=[A('I. ifade','Sağlıklı ebeveynden hasta çocuk doğması, hastalık aleline sahip olduklarını ama göstermediklerini gösterir.','I doğru: çekinik'),A('II. ifade','Hasta çocuk aa; her ebeveyn bir a vermiş ama sağlıklı olduğu için Aa olmalı.','II doğru'),A('III. ifade','Aa × Aa çaprazlamasında aa olasılığı 1/4’tür.','III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 dict(m='Hasta bir anne ile hasta bir babanın ilk çocuğu sağlıklıdır. Hastalığın otozomal kromozomlarda tek gen çiftiyle belirlendiği bilinmektedir.\nBuna göre,\nI. Hastalık baskın alelle belirlenir.\nII. Anne ve baba bu gen bakımından heterozigottur.\nIII. Sağlıklı çocuğun genotipi homozigot çekiniktir.\nifadelerinden hangileri doğrudur?',
  o=[('Yalnız I','Ebeveynlerin heterozigot olduğunu ve çocuğun aa olduğunu çıkaramamak.','bilgi'),('I ve II','Sağlıklı çocuğun homozigot çekinik olduğunu atlamak.','dikkat'),('I ve III','Ebeveynlerin heterozigot olduğunu atlamak.','bilgi'),('II ve III','Hastalığın baskın alelle belirlendiğini çıkaramamak.','bilgi'),('I, II ve III',None,None)],
  ad=[A('I. ifade','Hasta ebeveynden sağlıklı çocuk doğması, hastalığın baskın alelle belirlendiğini gösterir.','I doğru'),A('II. ifade','Sağlıklı çocuk aa; her ebeveyn bir a vermiş. Hasta oldukları için Aa olmalı.','II doğru'),A('III. ifade','Sağlıklı fenotip çekinik fenotiptir; genotip aa’dır.','III doğru'),A('Sonuç','Üç ifade de doğrudur.','I, II ve III')]),
 'sağlıklı ebeveyn, hasta çocuk','hasta ebeveyn, sağlıklı çocuk (baskın)')

# 0006
for g in ('SS','Ss'):
    c=cross(g,'ss'); 
assert pr(cross('Ss','ss'),lambda g:g=='ss')==Fr(1,2) and pr(cross('SS','ss'),lambda g:g=='ss')==0
Q(P,PRE,'0006','kl-test','Test çaprazlaması','orta','Test çaprazlaması','Yavru oranlarından ebeveynin genotipini belirler.','hikâyeli',3,
 'Çekinik bireyle çaprazlamada yavru oranı baskın ebeveynin genotipini gösterir.','Beyaz yavru çıkmasının nedenini baskın ebeveyne bağlayamamak.',[BAS,CAP,GEN],
 'Baskın fenotipli bireyi çekinikle çaprazla: yavruların yarısı çekinikse birey heterozigottur.',
 dict(m='Tavşanlarda siyah tüy rengi (S), beyaz tüy rengi (s) üzerine baskındır. Siyah tüylü bir dişi tavşan, beyaz tüylü bir erkek tavşanla çiftleştirildiğinde doğan 8 yavrunun 4’ü siyah, 4’ü beyaz tüylü oluyor.\nBuna göre dişi tavşanın genotipi ve oluşturduğu gamet çeşidi sayısı aşağıdakilerden hangisinde doğru verilmiştir?',i='Dişinin genotipi ve gamet çeşidi sayısı.',ip=['Beyaz erkek hangi genotipte?','Beyaz yavru çıkması dişi hakkında ne söyler?','Heterozigot birey kaç çeşit gamet verir?'],
  o=[('Ss – 2',None,None),('SS – 1','Beyaz yavrunun çıkamayacağını görmemek.','bilgi'),('SS – 2','Genotipi ve gamet sayısını birlikte yanlış bulmak.','bilgi'),('Ss – 1','Genotipi bulup heterozigotun gamet çeşidini 1 saymak.','bilgi'),('ss – 1','Siyah tüylü dişinin çekinik olduğunu sanmak.','dikkat')],
  ad=[A('Erkeğin genotipi','Beyaz tüylü erkek çekiniktir; genotipi ss ve yalnız s gameti verir.','erkek: ss'),A('Beyaz yavrunun anlamı','Beyaz yavru ss’tir; bir s’yi dişi de vermiştir.','dişide s var'),A('Dişinin genotipi','Dişi siyah tüylü olduğuna göre baskın S de vardır.','dişi: Ss'),A('Gametler','Ss genotipli birey S ve s olmak üzere iki çeşit gamet verir.','2 çeşit')]),
 dict(m='Drosophila (sirke sineği) türünde uzun kanat (K), kısa kanat (k) üzerine baskındır. Uzun kanatlı bir erkek sinek, kısa kanatlı bir dişi sinekle çiftleştirilince doğan 6 yavrunun 3’ü uzun, 3’ü kısa kanatlı oluyor.\nBuna göre erkek sineğin genotipi ve yavrulardan kaçının heterozigot olduğu aşağıdakilerden hangisinde doğru verilmiştir?',
  o=[('KK – 3','Yavruların yarısının kısa kanatlı olamayacağını görmemek.','bilgi'),('Kk – 3',None,None),('KK – 6','Erkeğin homozigot olduğunu sanmak.','bilgi'),('Kk – 0','Heterozigot yavru olmadığını sanmak.','bilgi'),('Kk – 6','Bütün yavruların heterozigot olduğunu sanmak.','dikkat')],
  ad=[A('Dişinin genotipi','Kısa kanatlı dişi çekiniktir; genotipi kk ve yalnız k gameti verir.','dişi: kk'),A('Erkeğin genotipi','Kısa kanatlı yavru kk’dir; bir k’yi erkek vermiştir. Erkek uzun kanatlı olduğundan Kk’dir.','erkek: Kk'),A('Yavruların genotipi','Kk × kk çaprazlamasında yavruların yarısı Kk, yarısı kk olur.','3 Kk · 3 kk'),A('Sonuç','Heterozigot (uzun kanatlı) yavru sayısı 3’tür.','Kk – 3')]),
 'test çaprazlaması (siyah/beyaz tavşan)','tür, özellik ve sorulan değer (heterozigot yavru sayısı)')

# 0007
c=cross('AaBb','AaBb'); a=sum(v for g,v in c.items() if dom(g,0) and dom(g,1)); b=c['AaBb']; assert (a,b)==(9,4) and Fr(b,a)==Fr(4,9)
c=cross('MmNn','MmNn'); a=sum(v for g,v in c.items() if dom(g,0) and not dom(g,1)); b=c['MmNn'.replace('Nn','nn')]; assert (a,b)==(3,2) and Fr(b,a)==Fr(2,3)
Q(P,PRE,'0007','kl-dihibrit','İki karakter çaprazlaması','zor','Dihibrit çaprazlama','İki karakterli çaprazlamada koşullu olasılığı hesaplar.','düz',5,
 'Dihibrit çaprazlamada belirli fenotipli bireyler arasından seçilen bireyin genotip olasılığı bulunur.','Paydayı 16 almak (koşulu paydaya katmamak).',[CAP,CAP2],
 'Koşullu olasılıkta payda “koşulu sağlayan yavru sayısı”dır, 16 değil.',
 dict(m='A ve B genleri bağımsız ayrılan, birer baskın (A, B) ve çekinik (a, b) alele sahip iki gen çiftidir. AaBb genotipli iki birey çaprazlanıyor.\nElde edilen yavrulardan her iki özellik bakımından baskın fenotipli olanlar arasından rastgele seçilen bir bireyin AaBb genotipli olma olasılığı kaçtır?',i='Seçilen bireyin AaBb olma olasılığı.',ip=['16 yavrunun kaçı iki özellikte de baskın fenotiplidir?','Bu bireylerin kaçı AaBb genotipindedir?','Payda tüm yavrular değil, koşulu sağlayanlardır.'],
  o=[('1/4','Paydayı 16 alıp koşulu paydaya katmamak.','dikkat'),('1/3','Genotip sayısını yanlış sayıp 3’e bölmek.','islem'),('4/9',None,None),('1/2','Heterozigot olma olasılığını gamet seçimine indirgemek.','islem'),('9/16','Baskın fenotip olasılığını sorulan olasılık sanmak.','dikkat')],
  ad=[A('Gametler','Her birey AB, Ab, aB, ab gameti verir; 16 eşit olasılıklı birleşme oluşur.','4 × 4 = 16'),A('Koşulu sağlayanlar','İki özellikte de baskın fenotip: A_B_ genotipleri (AABB, AABb, AaBB, AaBb).','1 + 2 + 2 + 4 = 9'),A('İstenen genotip','Bu 9 yavrudan AaBb olanlar 4 tanedir.','4'),A('Sonuç','İstenen sayı ÷ koşulu sağlayanlar.','4/9')]),
 dict(m='M ve N genleri bağımsız ayrılan, birer baskın (M, N) ve çekinik (m, n) alele sahip iki gen çiftidir. MmNn genotipli iki birey çaprazlanıyor.\nElde edilen yavrulardan M özelliği bakımından baskın, N özelliği bakımından çekinik fenotipli olanlar arasından rastgele seçilen bir bireyin Mmnn genotipli olma olasılığı kaçtır?',
  o=[('3/16','Paydayı 16 alıp koşulu paydaya katmamak.','dikkat'),('1/4','Tek bir gen çiftinin olasılığını vermek.','dikkat'),('1/3','Genotip sayısını yanlış sayıp 3’e bölmek.','islem'),('1/2','Heterozigot olma olasılığını tek gen çiftinden almak.','islem'),('2/3',None,None)],
  ad=[A('Gametler','Her birey MN, Mn, mN, mn gameti verir; 16 eşit olasılıklı birleşme oluşur.','4 × 4 = 16'),A('Koşulu sağlayanlar','M baskın, N çekinik fenotip: M_nn genotipleri (MMnn, Mmnn).','1 + 2 = 3'),A('İstenen genotip','Bu 3 yavrudan Mmnn olanlar 2 tanedir.','2'),A('Sonuç','İstenen sayı ÷ koşulu sağlayanlar.','2/3')]),
 'AaBb × AaBb koşullu genotip','farklı fenotip koşulu, farklı genler')

# 0008
def abrh(m,f,ab,rh,ra,fa):
    pass
cm=abo(['A','O'],['B','O']); 
rr=Counter(''.join(sorted(a+b)) for a in 'Rr' for b in 'rr'); assert Fr(cm['AB'],4)*Fr(rr['Rr'],4)==Fr(1,8)
cm=abo(['B','O'],['A','O']); rr=Counter(''.join(sorted(a+b)) for a in 'Rr' for b in 'Rr'); assert Fr(cm['B'],4)*Fr(rr['rr'],4)==Fr(1,16)
Q(P,PRE,'0008','kl-abo-rh','ABO ve Rh birlikte','zor','Kan grubu ve Rh','ABO ve Rh özelliklerini birlikte değerlendirerek olasılık hesaplar.','hikâyeli',5,
 'İlk çocuktan iki özellikte ebeveyn genotipleri çıkarılır; olasılıklar çarpılır.','Rh genotipini ebeveynlerden çıkaramamak ya da olasılıkları toplamak.',[ABO,RH,CAP],
 'Bağımsız ayrılan özellikler için olasılıklar çarpılır.',
 dict(m='A kan grubundan Rh+ bir anne ile B kan grubundan Rh− bir babanın ilk çocuğu O kan grubundan ve Rh−’dir. ABO ve Rh özellikleri bağımsız kalıtılmaktadır.\nBu çiftin ikinci çocuğunun AB kan grubundan ve Rh+ olma olasılığı kaçtır?',i='İkinci çocuğun AB Rh+ olma olasılığı.',ip=['İlk çocuğun OO ve rr olması ebeveynlerin genotipi hakkında ne söyler?','ABO için olasılığı ve Rh için olasılığı ayrı hesapla.','Bağımsız iki olasılık birbiriyle çarpılır.'],
  o=[('1/16','Olasılıklardan birini 1/4 yerine 1/2 alıp yanlış çarpmak.','islem'),('1/8',None,None),('1/4','Yalnız AB olma olasılığını vermek.','dikkat'),('3/8','Olasılıkları çarpmak yerine toplamak.','islem'),('1/2','Yalnız Rh+ olma olasılığını vermek.','dikkat')],
  ad=[A('ABO genotipleri','İlk çocuk OO olduğuna göre anne AO, baba BO’dur.','AO × BO'),A('Rh genotipleri','Rh− çocuk rr’dir; baba rr olduğundan anne Rr olmalıdır.','Rr × rr'),A('Ayrı olasılıklar','AO × BO’da AB olasılığı 1/4; Rr × rr’de Rh+ (Rr) olasılığı 1/2.','1/4 ve 1/2'),A('Sonuç','Bağımsız özellikler olduğundan olasılıklar çarpılır.','1/4 × 1/2 = 1/8')]),
 dict(m='B kan grubundan Rh+ bir anne ile A kan grubundan Rh+ bir babanın ilk çocuğu O kan grubundan ve Rh−’dir. ABO ve Rh özellikleri bağımsız kalıtılmaktadır.\nBu çiftin ikinci çocuğunun B kan grubundan ve Rh− olma olasılığı kaçtır?',
  o=[('1/16',None,None),('1/8','Yalnız iki olasılıktan birini 1/2 alıp yanlış çarpmak.','islem'),('3/16','Rh− yerine Rh+ olasılığını (3/4) kullanmak.','dikkat'),('1/4','Yalnız tek bir özelliğin olasılığını vermek.','dikkat'),('3/8','Olasılıkları çarpmak yerine toplamak.','islem')],
  ad=[A('ABO genotipleri','İlk çocuk OO olduğuna göre anne BO, baba AO’dur.','BO × AO'),A('Rh genotipleri','Rh− çocuk rr’dir; iki ebeveyn Rh+ olduğundan ikisi de Rr olmalıdır.','Rr × Rr'),A('Ayrı olasılıklar','BO × AO’da B (BO) olasılığı 1/4; Rr × Rr’de rr olasılığı 1/4.','1/4 ve 1/4'),A('Sonuç','Bağımsız özellikler olduğundan olasılıklar çarpılır.','1/4 × 1/4 = 1/16')]),
 'AO × BO ve Rr × rr','ebeveyn grupları, Rh genotipleri ve istenen birleşim')
bitir(P,'kalitim','Kalıtım','bio|Kalıtım',8)
