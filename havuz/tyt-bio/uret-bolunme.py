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
P=Parti('bolunme','Hücrede Bölünme – Üreme','bio|Hücrede Bölünme – Üreme',ders='TYT Biyoloji',idon='tytbio')
PRE='BBO'
MM=B('Mitoz ve mayoz','Mitoz: vücut hücrelerinde, büyüme ve onarım için; 1 hücreden 2 hücre, kromozom sayısı değişmez (2n → 2n) · Mayoz: gamet oluşumu için; 1 hücreden 4 hücre, kromozom sayısı yarıya iner (2n → n), krossing-over olur')
KRO=B('Mayozda kromozom sayısı','Kromozom sayısı mayoz I sonunda yarıya iner (2n → n); mayoz II’de kardeş kromatitler ayrıldığı için kromozom sayısı n olarak kalır')
GAM=B('Gamet oluşumu','Bir sperm ana hücresi mayozla 4 sperm verir · Bir yumurta ana hücresi mayozla 1 yumurta ve 3 kutup hücresi verir; kutup hücreleri gamet olarak kullanılmaz')
EVR=B('Evrelerde olanlar','Profaz: kromozomlar belirginleşir · Metafaz: kromozomlar ekvatorda dizilir · Anafaz: mitozda ve mayoz II’de kardeş kromatitler, mayoz I’de homolog kromozomlar ayrılır · Telofaz: çekirdekler oluşur')
DNB=B('DNA miktarı','S evresinde DNA eşlenir ve miktarı iki katına çıkar · Mayoz I sonunda DNA miktarı yarıya, mayoz II sonunda bir daha yarıya iner · Örnek: G1’de 4 birim → S sonunda 8 → mayoz I sonunda 4 → mayoz II sonunda 2')
GCE=B('Gamet çeşidi','n çift kromozomlu bir bireyde (krossing-over yokken) 2 üzeri n çeşit gamet oluşur · Örnek: 2n = 4 → 2 çift → 2 × 2 = 4 çeşit · Sperm ve yumurta rastgele birleşir: toplam kombinasyon = gamet çeşidi × gamet çeşidi')
Q(P,PRE,'0001','bo-karsilastir','Mitoz ve mayoz karşılaştırması','kolay','Mitoz ve mayoz','Yalnız mitoza ya da yalnız mayoza özgü olayları ayırt eder.','öncüllü',2,
 'Mitoz ve mayozu ayıran özellikler seçilir.','İki bölünmede ortak olan olayları ayırıcı sanmak.',[MM],
 'Krossing-over ve kromozom sayısının yarıya inmesi yalnız mayozun işaretleridir.',
 dict(m='I. Krossing-over\nII. Kromozom sayısının yarıya inmesi\nIII. Bölünmeden önce DNA’nın eşlenmesi\nYukarıdaki olaylardan hangileri yalnız mayoz bölünmede görülür?',i='Yalnız mayozda görülen olaylar.',ip=['Hangi olaylar iki bölünmede de ortak?','DNA eşlenmesi hangi evrede olur ve bölünmeye özel midir?','Krossing-over kimlerde görülür?'],
  o=[('I ve II',None,None),('Yalnız I','Kromozom sayısının yarıya inmesinin mayoza özgü olduğunu atlamak.','bilgi'),('Yalnız II','Krossing-over’ın mayoza özgü olduğunu atlamak.','bilgi'),('I ve III','DNA eşlenmesini mayoza özgü sanmak.','bilgi'),('I, II ve III','DNA’nın mitozdan önce de eşlendiğini unutmak.','bilgi')],
  ad=[A('I. olay','Krossing-over mayoz I’in profazında homolog kromozomlar arasında olur.','I yalnız mayozda'),A('II. olay','Mitozda kromozom sayısı sabit kalır, mayozda yarıya iner.','II yalnız mayozda'),A('III. olay','DNA eşlenmesi interfazın S evresindedir ve iki bölünmeden önce de olur.','III ortak'),A('Sonuç','Yalnız mayozda görülenler I ve II.','I ve II')]),
 dict(m='I. Vücut hücrelerinde büyüme ve onarımı sağlama\nII. Bir hücreden dört hücre oluşturma\nIII. Diploit (2n) bir ana hücreden 2n kromozomlu yavru hücreler oluşması\nYukarıdakilerden hangileri yalnız mitoz bölünmede görülür?',
  o=[('Yalnız I','Diploit ana hücreden 2n kromozomlu yavru hücrelerin mitoza özgü olduğunu atlamak.','bilgi'),('Yalnız II','Dört hücre oluşumunun mayoza özgü olduğunu bilmemek.','bilgi'),('II ve III','Dört hücre oluşumunu mitoza ait sanmak.','bilgi'),('I ve III',None,None),('I, II ve III','Mayozdaki dört hücre oluşumunu mitoz sanmak.','bilgi')],
  ad=[A('I. olay','Büyüme ve onarım mitozla sağlanır.','I yalnız mitozda'),A('II. olay','Bir hücreden dört hücre mayozda oluşur.','II mayoza ait'),A('III. olay','Diploit ana hücreden 2n kromozomlu yavru hücreler yalnız mitozda oluşur; mayozda yavru hücreler n kromozomludur.','III yalnız mitozda'),A('Sonuç','Yalnız mitozda görülenler I ve III.','I ve III')]),
 'mayoza özgü olaylar','yalnız mitoz sorusu, olaylar yeniden yazıldı')
# 0002
for n in (6,10): assert n==2*n//2
Q(P,PRE,'0002','bo-kromozom','Mayozda kromozom sayısı','orta','Mayoz','Mayozun evrelerinde kromozom sayısını izler.','düz',3,
 'Diploit hücrede mayoz I ve II sonundaki kromozom sayıları sorulur.','Mayoz II’de de kromozom sayısının yarıya indiğini sanmak.',[KRO,MM],
 'Mayoz I sonunda n, mayoz II sonunda yine n.',
 dict(m='Kromozom sayısı 2n = 12 olan bir hücre mayoz bölünme geçiriyor.\nBu hücrenin mayoz I sonunda oluşan hücrelerinin her birinde ve mayoz II sonunda oluşan hücrelerinin her birinde bulunan kromozom sayıları sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',i='Mayoz I ve mayoz II sonundaki kromozom sayıları.',ip=['Mayoz I’de hangi kromozomlar ayrılır?','Mayoz I sonunda kromozom sayısı kaça iner?','Mayoz II’de kromozom sayısı değişir mi?'],
  o=[('12 – 12','Mayozda kromozom sayısının hiç azalmadığını sanmak.','bilgi'),('12 – 6','Kromozom sayısının mayoz II’de yarıya indiğini sanmak.','bilgi'),('6 – 3','Mayoz II’de de yarıya indiğini sanmak.','bilgi'),('6 – 6',None,None),('3 – 3','2n = 12’yi dörde bölmek.','islem')],
  ad=[A('Mayoz I','Homolog kromozomlar ayrılır, kromozom sayısı 12’den 6’ya iner.','2n = 12 → n = 6'),A('Mayoz II','Kardeş kromatitler ayrılır; hücre başına kromozom sayısı değişmez.','6 → 6'),A('Sonuç','Mayoz I sonunda ve mayoz II sonunda 6 kromozom bulunur.','6 – 6')]),
 dict(m='Kromozom sayısı 2n = 20 olan bir hücre mayoz bölünme geçiriyor.\nBu hücrenin mayoz I sonunda oluşan hücrelerinin her birinde ve mayoz II sonunda oluşan hücrelerinin her birinde bulunan kromozom sayıları sırasıyla kaçtır?',
  o=[('5 – 5','2n = 20’yi dörde bölmek.','islem'),('10 – 10',None,None),('10 – 5','Mayoz II’de de yarıya indiğini sanmak.','bilgi'),('20 – 10','Yarıya inmenin mayoz II’de olduğunu sanmak.','bilgi'),('20 – 20','Mayozda kromozom sayısının hiç azalmadığını sanmak.','bilgi')],
  ad=[A('Mayoz I','Homolog kromozomlar ayrılır, kromozom sayısı 20’den 10’a iner.','2n = 20 → n = 10'),A('Mayoz II','Kardeş kromatitler ayrılır; hücre başına kromozom sayısı değişmez.','10 → 10'),A('Sonuç','Mayoz I sonunda ve mayoz II sonunda 10 kromozom bulunur.','10 – 10')]),
 'mayoz I ve II kromozom sayısı','2n değeri değişti')
# 0003
assert 100*4==400 and 100*1==100 and 50*4+50*1==250
Q(P,PRE,'0003','bo-gamet-sayisi','Gamet sayısı hesabı','orta','Gamet oluşumu','Ana hücre sayısından oluşan gamet sayısını hesaplar.','hikâyeli',3,
 'Sperm ve yumurta ana hücrelerinden mayozla oluşan gamet sayıları bulunur.','Yumurta ana hücresinden 4 yumurta oluştuğunu sanmak.',[GAM],
 'Sperm ana hücresi → 4 sperm; yumurta ana hücresi → 1 yumurta.',
 dict(m='Bir hayvanda 100 sperm ana hücresi ve 100 yumurta ana hücresi mayoz bölünme geçiriyor.\nBu bölünmeler sonunda oluşan olgun sperm ve olgun yumurta sayıları sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',i='Oluşan sperm ve yumurta sayıları.',ip=['Bir sperm ana hücresinden kaç sperm oluşur?','Bir yumurta ana hücresinden kaç yumurta oluşur?','Kutup hücreleri gamet olarak sayılır mı?'],
  o=[('100 – 100','Sperm ana hücresinden de bir sperm oluştuğunu sanmak.','bilgi'),('100 – 400','Sperm ve yumurta sayılarını ters yazmak.','dikkat'),('400 – 100',None,None),('400 – 400','Yumurta ana hücresinden de dört yumurta oluştuğunu sanmak.','bilgi'),('200 – 100','Mayozda iki hücre oluştuğunu sanmak.','bilgi')],
  ad=[A('Sperm','Her sperm ana hücresi mayozla 4 sperm oluşturur.','100 × 4 = 400'),A('Yumurta','Her yumurta ana hücresi 1 yumurta ve 3 kutup hücresi oluşturur; kutup hücreleri gamet olmaz.','100 × 1 = 100'),A('Sonuç','400 sperm ve 100 yumurta oluşur.','400 – 100')]),
 dict(m='Bir hayvanda 50 sperm ana hücresi ve 50 yumurta ana hücresi mayoz bölünme geçiriyor.\nBu bölünmeler sonunda oluşan olgun sperm ve olgun yumurta sayılarının toplamı kaçtır?',
  o=[('100','Her ana hücreden bir gamet oluştuğunu sanmak.','bilgi'),('150','Sperm ana hücresinden 2 sperm oluştuğunu sanmak.','bilgi'),('200','Yumurtaları saymayı unutmak.','dikkat'),('250',None,None),('400','Her ana hücreden 4 gamet oluştuğunu sanmak.','bilgi')],
  ad=[A('Sperm','Her sperm ana hücresi 4 sperm oluşturur.','50 × 4 = 200'),A('Yumurta','Her yumurta ana hücresi yalnız 1 yumurta verir.','50 × 1 = 50'),A('Sonuç','Toplam gamet sayısı sperm ve yumurta toplamıdır.','200 + 50 = 250')]),
 'sperm/yumurta sayısı','sayılar ve istenen (toplam) değişti')
# 0004
Q(P,PRE,'0004','bo-evre','Bölünme evrelerinde olanlar','orta','Evreler','Mitoz ve mayoz evrelerindeki olayları değerlendirir.','öncüllü',3,
 'Evre–olay eşleştirmesinden doğru olanlar seçilir.','Anafazda ayrılan yapıları (kromatit/homolog) karıştırmak.',[EVR],
 'Anafaz: mitoz ve mayoz II’de kromatitler, mayoz I’de homologlar ayrılır.',
 dict(m='Mitoz bölünmenin evreleriyle ilgili,\nI. Profazda kromozomlar belirginleşir.\nII. Metafazda kromozomlar ekvator düzleminde dizilir.\nIII. Telofazda kardeş kromatitler birbirinden ayrılır.\nifadelerinden hangileri doğrudur?',i='Doğru olan ifadeler.',ip=['Kardeş kromatitler hangi evrede ayrılır?','Ekvatorda dizilme hangi evrede olur?','Telofazda hangi olaylar gerçekleşir?'],
  o=[('I ve II',None,None),('Yalnız I','Metafazda kromozomların ekvatorda dizildiğini atlamak.','bilgi'),('Yalnız III','Kromatitlerin telofazda ayrıldığını sanmak.','bilgi'),('I ve III','Kromatit ayrılmasını telofaza yazmak.','bilgi'),('I, II ve III','Anafaz ile telofazı karıştırmak.','bilgi')],
  ad=[A('I. ifade','Profazda kromozomlar kısalıp kalınlaşarak belirginleşir.','I doğru'),A('II. ifade','Metafazda kromozomlar ekvator düzleminde dizilir.','II doğru'),A('III. ifade','Kardeş kromatitler anafazda ayrılır; telofazda çekirdekler oluşur.','III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 dict(m='Mayoz bölünmeyle ilgili,\nI. Mayoz I’in anafazında homolog kromozomlar birbirinden ayrılır.\nII. Mayoz II’nin anafazında homolog kromozomlar birbirinden ayrılır.\nIII. Krossing-over mayoz I’in profazında gerçekleşir.\nifadelerinden hangileri doğrudur?',
  o=[('Yalnız I','Krossing-over’ın mayoz I profazında olduğunu atlamak.','bilgi'),('Yalnız III','Homolog kromozomların mayoz I’de ayrıldığını atlamak.','bilgi'),('I ve II','Mayoz II’de de homolog kromozomların ayrıldığını sanmak.','bilgi'),('II ve III','Mayoz I ve II’deki ayrılan yapıları karıştırmak.','bilgi'),('I ve III',None,None)],
  ad=[A('I. ifade','Mayoz I’de homolog kromozomlar ayrılır, kromozom sayısı yarıya iner.','I doğru'),A('II. ifade','Mayoz II’de kardeş kromatitler ayrılır, homologlar değil.','II yanlış'),A('III. ifade','Krossing-over mayoz I profazında homologlar arasında olur.','III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 'mitoz evre olayları','mayoz evrelerine geçildi')
# 0005
g1=6; s=2*g1; m1=s//2; m2=m1//2; assert (s,m1,m2)==(12,6,3)
g1=10; s=2*g1; m1=s//2; m2=m1//2; assert (s,m1,m2)==(20,10,5)
Q(P,PRE,'0005','bo-dna-miktari','Bölünmede DNA miktarı','zor','DNA miktarı','Hücre döngüsü ve mayozda DNA miktarının değişimini izler.','yeni nesil',4,
 'G1’deki DNA miktarından S evresi ve mayoz sonundaki DNA miktarları bulunur.','S evresinde artan DNA miktarını hesaba katmamak.',[DNB],
 'S’de iki katına çıkar, mayoz I’de ve mayoz II’de ikişer kez yarıya iner.',
 dict(m='Mayoz bölünme geçirecek bir hücrenin G1 evresindeki DNA miktarı 6 birimdir.\nBu hücreden mayoz I sonunda oluşan bir hücredeki DNA miktarı ile mayoz II sonunda oluşan bir hücredeki DNA miktarı sırasıyla kaç birimdir?',i='Mayoz I ve mayoz II sonundaki hücre başına DNA miktarı.',ip=['S evresinde DNA miktarına ne olur?','Mayoz I sonunda DNA miktarı kaça iner?','Mayoz II sonunda bir kez daha yarıya iner.'],
  o=[('3 – 3','G1’deki DNA miktarını S’de iki katına çıkarmayı unutmak.','bilgi'),('6 – 3',None,None),('6 – 6','Mayoz II’de DNA miktarının yarıya indiğini atlamak.','bilgi'),('12 – 3','Mayoz I’de DNA miktarının yarıya indiğini atlamak.','bilgi'),('12 – 6','Mayoz I’de yarıya inmeyi unutmak.','bilgi')],
  ad=[A('S evresi','DNA eşlenir, miktarı iki katına çıkar.','6 → 12'),A('Mayoz I','Homolog kromozomlar ayrılır, hücre başına DNA yarıya iner.','12 → 6'),A('Mayoz II','Kardeş kromatitler ayrılır, hücre başına DNA bir daha yarıya iner.','6 → 3'),A('Sonuç','Mayoz I sonunda 6, mayoz II sonunda 3 birim.','6 – 3')]),
 dict(m='Mayoz bölünme geçirecek bir hücrenin G1 evresindeki DNA miktarı 10 birimdir.\nBu hücrenin S evresi sonundaki DNA miktarı ile mayoz II sonunda oluşan bir hücredeki DNA miktarı sırasıyla kaç birimdir?',
  o=[('10 – 5','S evresinde DNA’nın iki katına çıktığını unutmak.','bilgi'),('10 – 10','S evresini ve mayozdaki yarılanmaları hesaba katmamak.','bilgi'),('20 – 5',None,None),('20 – 10','Mayoz II’de DNA’nın yarıya indiğini atlamak.','bilgi'),('40 – 10','S evresinde DNA’yı dört katına çıkarmak.','islem')],
  ad=[A('S evresi','DNA eşlenir, miktarı iki katına çıkar.','10 → 20'),A('Mayoz I','Hücre başına DNA yarıya iner.','20 → 10'),A('Mayoz II','Hücre başına DNA bir daha yarıya iner.','10 → 5'),A('Sonuç','S sonunda 20, mayoz II sonunda 5 birim.','20 – 5')]),
 'G1 DNA miktarı, S ve mayoz','sayılar ve sorulan evreler değişti')
# 0006
assert 2**3==8 and 8*8==64 and 2**2==4 and 4*4==16
Q(P,PRE,'0006','bo-gamet-cesidi','Gamet çeşidi ve zigot kombinasyonu','zor','Gamet çeşitliliği','Kromozom sayısından gamet çeşidini ve zigot kombinasyonu sayısını hesaplar.','yeni nesil',4,
 'Kromozom çifti sayısından gamet çeşidi, iki bireyin gametlerinden zigot kombinasyonu bulunur.','Zigot kombinasyonu için gamet çeşitlerini toplamak.',[GCE],
 'Zigot kombinasyonu = anne gamet çeşidi × baba gamet çeşidi.',
 dict(m='2n = 6 kromozomlu iki bireyin her kromozom çiftinde üyeler birbirinden farklıdır ve krossing-over görülmemektedir. Bu iki birey çiftleşiyor.\nBuna göre bu çiftleşmeden oluşabilecek farklı kromozom kombinasyonlu zigot sayısı en fazla kaçtır?',i='En fazla farklı zigot kombinasyonu sayısı.',ip=['2n = 6 kaç kromozom çiftidir?','Bir birey kaç çeşit gamet oluşturur?','Sperm ve yumurta birleşirken gamet çeşitleri çarpılır.'],
  o=[('8','Yalnız tek bireyin gamet çeşidini vermek.','dikkat'),('16','İki bireyin gamet çeşitlerini toplamak.','islem'),('36','Kromozom sayısının karesini almak.','islem'),('48','Gamet çeşidini kromozom sayısıyla çarpmak.','islem'),('64',None,None)],
  ad=[A('Kromozom çifti','2n = 6 olduğuna göre 3 homolog çift vardır.','3 çift'),A('Gamet çeşidi','Her çift 2 seçenek sunar; krossing-over yoktur.','2 × 2 × 2 = 8'),A('Zigot kombinasyonu','Her sperm çeşidi her yumurta çeşidiyle birleşebilir.','8 × 8'),A('Sonuç','En fazla 64 farklı zigot kombinasyonu.','64')]),
 dict(m='2n = 4 kromozomlu iki bireyin her kromozom çiftinde üyeler birbirinden farklıdır ve krossing-over görülmemektedir. Bu iki birey çiftleşiyor.\nBuna göre bu çiftleşmeden oluşabilecek farklı kromozom kombinasyonlu zigot sayısı en fazla kaçtır?',
  o=[('4','Yalnız tek bireyin gamet çeşidini vermek.','dikkat'),('8','İki bireyin gamet çeşitlerini toplamak.','islem'),('12','Gamet çeşidini kromozom sayısının üç katıyla çarpmak.','islem'),('16',None,None),('24','Kromozomları sıralayarak yanlış hesap yapmak.','islem')],
  ad=[A('Kromozom çifti','2n = 4 olduğuna göre 2 homolog çift vardır.','2 çift'),A('Gamet çeşidi','Her çift 2 seçenek sunar; krossing-over yoktur.','2 × 2 = 4'),A('Zigot kombinasyonu','Her sperm çeşidi her yumurta çeşidiyle birleşebilir.','4 × 4'),A('Sonuç','En fazla 16 farklı zigot kombinasyonu.','16')]),
 '2n = 6, gamet çeşidi ve kombinasyon','2n değeri değişti')
bitir(P,'bolunme','Hücrede Bölünme – Üreme','bio|Hücrede Bölünme – Üreme',6)
