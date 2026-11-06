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
P=Parti('ekosistem','Ekosistem','bio|Ekosistem',ders='TYT Biyoloji',idon='tytbio')
PRE='BEK'
FAK=B('Biyotik ve abiyotik faktörler','Abiyotik: cansız etmenler (ışık, sıcaklık, su, rüzgâr, toprak yapısı, pH) · Biyotik: canlı etmenler (üretici, tüketici, ayrıştırıcı, parazit, rakip, av)')
ENE=B('Enerji aktarımı','Her basamakta enerjinin yaklaşık %10’u bir üst basamağa aktarılır, kalanı solunumla ısı olarak kaybolur · Örnek: üretici 1000 kJ → otçul 100 kJ → etçil 10 kJ')
AGI=B('Besin zinciri ve ağı','Besin zinciri: üretici → otçul → etçil … basamak basamak tek yol · Besin ağı: birbirine bağlı besin zincirlerinin tümüdür · Zincir üreticiyle başlar, hiçbir canlı tarafından yenmeyen canlıyla biter')
SIM=B('Canlılar arası ilişkiler','Mutualizm: iki tarafın da yararlandığı ilişki (liken, mikoriza, baklagil–Rhizobium) · Parazitizm: bir taraf yararlanır, konak zarar görür (kene, tenya) · Kommensalizm: bir taraf yararlanır, diğeri etkilenmez (ağaç üzerindeki orkide)')
AZO=B('Azot döngüsü','Azot bağlayıcı bakteriler: N2 → amonyak · Nitrifikasyon bakterileri: amonyak → nitrat · Denitrifikasyon bakterileri: nitrat → N2')
KAR=B('Karbon döngüsü','Fotosentez: atmosferdeki CO2 → organik madde · Solunum: organik madde → CO2 · Ayrışma: ölü canlıdaki organik madde ayrıştırıcılarla CO2’ye döner')
POP=B('Popülasyon büyüklüğü','Değişim = doğum + göçle giren − ölüm − göçle çıkan · Popülasyon yoğunluğu = birey sayısı ÷ yaşam alanı (örnek: 200 birey, 4 km² → 50 birey/km²)')
Q(P,PRE,'0001','ek-faktor','Biyotik ve abiyotik faktörler','kolay','Ekosistem bileşenleri','Abiyotik faktörleri biyotik faktörlerden ayırt eder.','öncüllü',2,
 'Verilen etmenlerden cansız (abiyotik) olanlar seçilir.','Canlı olmayan ama canlıdan türeyen etmeni biyotik sanmak.',[FAK],
 'Cansız etmen = abiyotik, canlı etmen = biyotik.',
 dict(m='I. Sıcaklık\nII. Ayrıştırıcı bakteri\nIII. Toprağın pH değeri\nYukarıdakilerden hangileri bir ekosistemin abiyotik faktörlerindendir?',i='Abiyotik faktörler.',ip=['Abiyotik ne demektir?','Bakteri canlı mıdır?','Sıcaklık ve pH canlı etmen midir?'],
  o=[('Yalnız I','Toprağın pH değerinin de abiyotik faktör olduğunu atlamak.','bilgi'),('Yalnız II','Ayrıştırıcıyı abiyotik sanmak.','bilgi'),('II ve III','Sıcaklığı atlayıp bakteriyi abiyotik saymak.','bilgi'),('I ve III',None,None),('I, II ve III','Ayrıştırıcı bakterinin canlı olduğunu unutmak.','bilgi')],
  ad=[A('Tanımı hatırla','Abiyotik faktörler cansız çevre etmenleridir.','abiyotik = cansız'),A('Ögeleri sını','Sıcaklık ve toprağın pH değeri cansızdır; ayrıştırıcı bakteri canlıdır.','I, III cansız · II canlı'),A('Sonuç','Abiyotik olanlar I ve III.','I ve III')]),
 dict(m='I. Işık şiddeti\nII. Parazit bakteri\nIII. Rüzgâr\nYukarıdakilerden hangileri bir ekosistemin biyotik faktörlerindendir?',
  o=[('Yalnız II',None,None),('Yalnız I','Işık şiddetini canlı etmen sanmak.','bilgi'),('I ve II','Işığı biyotik, bakteriyi doğru sayıp rüzgârı atlamak.','bilgi'),('II ve III','Rüzgârı biyotik sanmak.','bilgi'),('I, II ve III','Cansız etmenlerin hepsini biyotik saymak.','bilgi')],
  ad=[A('Tanımı hatırla','Biyotik faktörler canlı etmenlerdir.','biyotik = canlı'),A('Ögeleri sını','Işık şiddeti ve rüzgâr cansız etmenlerdir; parazit bakteri canlıdır.','I, III cansız · II canlı'),A('Sonuç','Biyotik olan yalnız II.','Yalnız II')]),
 'abiyotik faktörler','soru yönü (biyotik) ve ögeler değişti')
for u,z in ((20000,3),(50000,4)):
    e=u
    for _ in range(z): e//=10
assert 20000//1000==20 and 50000//10000==5
Q(P,PRE,'0002','ek-enerji','Besin zincirinde enerji aktarımı','orta','Enerji akışı','%10 kuralıyla basamaklar arası enerji miktarını hesaplar.','hikâyeli',3,
 'Her basamakta %10 aktarımla son basamaktaki enerji bulunur.','Basamak sayısını yanlış saymak.',[ENE,AGI],
 'Enerji her basamakta 10’a bölünür; basamak sayısını doğru say.',
 dict(m='Bir ekosistemde üreticilerde 20000 kJ enerji bulunmaktadır. Besin zinciri üretici → otçul → etçil → üst etçil şeklindedir ve her basamakta enerjinin %10’u bir sonraki basamağa aktarılmaktadır.\nBuna göre üst etçile aktarılan enerji kaç kJ’dür?',i='Üst etçile aktarılan enerji (kJ).',ip=['Üreticiden otçula aktarılan enerjiyi bul.','Her basamakta enerji kaç kat azalır?','Üretici ile üst etçil arasında kaç aktarım var?'],
  o=[('2','Dört basamağı beş aktarım sanmak.','dikkat'),('20',None,None),('200','Yalnız iki aktarım hesaplamak.','dikkat'),('2000','Yalnız otçula aktarılan enerjiyi hesaplamak.','dikkat'),('20000','Enerjinin aktarılırken azalmadığını sanmak.','bilgi')],
  ad=[A('Otçul','Üreticideki enerjinin %10’u otçula geçer.','20000 × 0,1 = 2000'),A('Etçil','Otçuldaki enerjinin %10’u etçile geçer.','2000 × 0,1 = 200'),A('Üst etçil','Etçildeki enerjinin %10’u üst etçile geçer.','200 × 0,1 = 20'),A('Sonuç','Üst etçile 20 kJ aktarılır.','20 kJ')]),
 dict(m='Bir ekosistemde üreticilerde 50000 kJ enerji bulunmaktadır. Besin zinciri üretici → böcek → kurbağa → yılan → şahin şeklindedir ve her basamakta enerjinin %10’u bir sonraki basamağa aktarılmaktadır.\nBuna göre şahine aktarılan enerji kaç kJ’dür?',
  o=[('5',None,None),('50','Üç aktarım hesaplayıp son basamağı atlamak.','dikkat'),('500','İki aktarım hesaplayıp durmak.','dikkat'),('5000','Yalnız böceğe aktarılan enerjiyi vermek.','dikkat'),('50000','Enerjinin aktarılırken azalmadığını sanmak.','bilgi')],
  ad=[A('Böcek','Üreticideki enerjinin %10’u böceğe geçer.','50000 × 0,1 = 5000'),A('Kurbağa ve yılan','Her basamakta enerji 10’a bölünür.','5000 → 500 → 50'),A('Şahin','Yılandaki enerjinin %10’u şahine geçer.','50 × 0,1 = 5'),A('Sonuç','Şahine 5 kJ aktarılır.','5 kJ')]),
 '%10 kuralı, 4 basamak','zincir, basamak sayısı ve sayılar değişti')
def yollar(g,bas):
    son=[]
    def git(d,yol):
        if d not in g: son.append(yol); return
        for h in g[d]: git(h,yol+[h])
    git(bas,[bas]); return son
g1={'ot':['çekirge','tavşan'],'çekirge':['kurbağa','kuş'],'kurbağa':['yılan'],'yılan':['kartal'],'kuş':['kartal'],'tavşan':['tilki','kartal']}
assert len(yollar(g1,'ot'))==4
g2={'alg':['pire','larva'],'pire':['kbalık'],'larva':['kbalık','kurbağa'],'kbalık':['bbalık','balıkçıl'],'kurbağa':['balıkçıl']}
assert len(yollar(g2,'alg'))==5
Q(P,PRE,'0003','ek-besin-agi','Besin ağında zincir sayısı','orta','Besin ağı','Besin ağındaki farklı besin zincirlerini sayar.','düz',3,
 'Okla verilen besin ağındaki üreticiden son tüketiciye yol sayısı bulunur.','Kısa yolları ya da ortak halkaları atlamak.',[AGI],
 'Zincirleri üreticiden başlayıp en sona kadar tek tek yaz.',
 dict(m='Bir çayır ekosisteminde canlılar arasındaki beslenme ilişkileri aşağıda (A → B: B, A’yı yer) verilmiştir:\not → çekirge\not → tavşan\nçekirge → kurbağa\nçekirge → kuş\nkurbağa → yılan\nyılan → kartal\nkuş → kartal\ntavşan → tilki\ntavşan → kartal\nBuna göre bu besin ağında üreticiden başlayıp son tüketiciyle biten kaç farklı besin zinciri vardır?',i='Farklı besin zinciri sayısı.',ip=['Zincir hangi canlıyla başlar?','Kimleri kimse yemiyor? Zincir orada biter.','Her dalı ayrı bir zincir olarak yaz.'],
  o=[('2','Yalnızca iki ana dalı saymak.','dikkat'),('3','Tavşanın kartala giden yolunu atlamak.','dikkat'),('4',None,None),('5','Bir zinciri iki kez saymak.','dikkat'),('9','Ok sayısını zincir sayısı sanmak.','dikkat')],
  ad=[A('Başlangıç','Zincirler üretici otla başlar.','ot'),A('Çekirge dalı','Ot → çekirge → kurbağa → yılan → kartal ve ot → çekirge → kuş → kartal.','2 zincir'),A('Tavşan dalı','Ot → tavşan → tilki ve ot → tavşan → kartal.','2 zincir'),A('Sonuç','Toplam zincir sayısı.','2 + 2 = 4')]),
 dict(m='Bir göl ekosisteminde canlılar arasındaki beslenme ilişkileri aşağıda (A → B: B, A’yı yer) verilmiştir:\nalg → su piresi\nalg → sivrisinek larvası\nsu piresi → küçük balık\nlarva → küçük balık\nlarva → kurbağa\nküçük balık → büyük balık\nküçük balık → balıkçıl\nkurbağa → balıkçıl\nBuna göre bu besin ağında üreticiden başlayıp son tüketiciyle biten kaç farklı besin zinciri vardır?',
  o=[('3','Küçük balıktan sonraki iki dalı tek saymak.','dikkat'),('4','Kurbağa dalını atlamak.','dikkat'),('5',None,None),('6','Bir zinciri iki kez saymak.','dikkat'),('8','Ok sayısını zincir sayısı sanmak.','dikkat')],
  ad=[A('Başlangıç','Zincirler üretici algle başlar.','alg'),A('Su piresi dalı','Alg → pire → küçük balık → büyük balık ve alg → pire → küçük balık → balıkçıl.','2 zincir'),A('Larva dalı','Larva küçük balık üzerinden iki, kurbağa üzerinden bir zincir verir.','3 zincir'),A('Sonuç','Toplam zincir sayısı.','2 + 3 = 5')]),
 'çayır besin ağı','göl besin ağı, farklı halkalar')
Q(P,PRE,'0004','ek-iliski','Canlılar arası ilişkiler','orta','Simbiyotik ilişkiler','Canlılar arasındaki ilişki türlerini ayırt eder.','öncüllü',3,
 'Örnek ilişkinin türü (mutualizm, parazitizm, kommensalizm) doğru verilmiş mi sınanır.','Tenya gibi parazitleri kommensalizm sanmak.',[SIM],
 'Kim yararlanıyor, kim zarar görüyor diye sor.',
 dict(m='Canlılar arasındaki ilişkiler ve türleri ile ilgili,\nI. Baklagil kökü ile Rhizobium bakterisi: Mutualizm\nII. İnsan bağırsağındaki tenya: Kommensalizm\nIII. Mantar ile bitki kökü (mikoriza): Mutualizm\neşleştirmelerinden hangileri doğrudur?',i='Doğru eşleştirmeler.',ip=['Her iki taraf yararlanıyorsa ilişki nedir?','Tenya konağa zarar verir mi?','Konak zarar görüyorsa ilişki hangisidir?'],
  o=[('Yalnız I','Mikorizayı mutualizm olarak bilmemek.','bilgi'),('Yalnız III','Baklagil–Rhizobium ilişkisini mutualizm olarak bilmemek.','bilgi'),('I ve II','Tenyanın konağa zarar verdiğini atlamak.','bilgi'),('II ve III','Baklagil–Rhizobium eşleşmesini atlamak, tenyayı yanlış saymak.','bilgi'),('I ve III',None,None)],
  ad=[A('I. eşleştirme','Rhizobium baklagilden besin alır, baklagile azotlu bileşik sağlar: iki taraf da yararlanır.','Mutualizm doğru'),A('II. eşleştirme','Tenya konaktan beslenir, konağa zarar verir: parazitizm.','Kommensalizm yanlış'),A('III. eşleştirme','Mantar ile bitki kökü karşılıklı yarar sağlar.','Mutualizm doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 dict(m='Canlılar arasındaki ilişkiler ve türleri ile ilgili,\nI. Liken (alg ile mantar): Mutualizm\nII. Köpek üzerindeki kene: Parazitizm\nIII. Ağaç gövdesinde yaşayan orkide: Parazitizm\neşleştirmelerinden hangileri doğrudur?',
  o=[('Yalnız I','Kenenin parazit olduğunu atlamak.','bilgi'),('I ve II',None,None),('Yalnız II','Likenin mutualizm olduğunu atlamak.','bilgi'),('I ve III','Orkideyi parazit saymak; ağaca zarar vermez.','bilgi'),('I, II ve III','Orkideyi parazit saymak; ağaç etkilenmez.','bilgi')],
  ad=[A('I. eşleştirme','Alg besin üretir, mantar nem ve koruma sağlar: iki taraf da yararlanır.','Mutualizm doğru'),A('II. eşleştirme','Kene köpeğin kanını emer ve konağa zarar verir.','Parazitizm doğru'),A('III. eşleştirme','Orkide ağaçtan yararlanır, ağaç etkilenmez: kommensalizm.','Parazitizm yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 'mutualizm/parazitizm eşleştirmesi','farklı örnekler ve ilişkiler')
Q(P,PRE,'0005','ek-dongu','Madde döngüleri','zor','Azot ve karbon döngüsü','Madde döngülerindeki basamakları ilgili süreç ya da canlıyla eşleştirir.','düz',4,
 'Döngüdeki X, Y, Z basamaklarını doğru süreç/canlı ile eşleştirir.','Nitrifikasyon ile denitrifikasyonu karıştırmak.',[AZO],
 'Azot döngüsünün sırası: bağlama → nitrifikasyon → denitrifikasyon.',
 dict(m='Azot döngüsünün basamakları şöyledir:\nAtmosferdeki N2 —(X)→ Amonyak —(Y)→ Nitrat —(Z)→ Atmosferdeki N2\nBuna göre X, Y ve Z basamaklarını gerçekleştiren canlılar aşağıdakilerden hangisinde doğru verilmiştir?',i='X, Y ve Z’yi gerçekleştiren canlılar.',ip=['N2’yi amonyağa çeviren bakteriler hangileri?','Amonyağı nitrata çevirmeye ne denir?','Nitratı tekrar N2’ye çeviren bakterilere ne denir?'],
  o=[('X: Denitrifikasyon bakterileri, Y: Nitrifikasyon bakterileri, Z: Azot bağlayıcı bakteriler','Üç basamağı ters yazmak.','bilgi'),('X: Azot bağlayıcı bakteriler, Y: Denitrifikasyon bakterileri, Z: Nitrifikasyon bakterileri','Y ile Z’yi karıştırmak.','bilgi'),('X: Nitrifikasyon bakterileri, Y: Azot bağlayıcı bakteriler, Z: Denitrifikasyon bakterileri','X ile Y’yi karıştırmak.','bilgi'),('X: Azot bağlayıcı bakteriler, Y: Nitrifikasyon bakterileri, Z: Denitrifikasyon bakterileri',None,None),('X: Nitrifikasyon bakterileri, Y: Denitrifikasyon bakterileri, Z: Azot bağlayıcı bakteriler','Üç basamağı karıştırmak.','bilgi')],
  ad=[A('X’i bul','Atmosferdeki N2’yi amonyağa çevirenler azot bağlayıcı bakterilerdir.','X: azot bağlayıcılar'),A('Y’yi bul','Amonyak nitrata nitrifikasyon bakterileriyle dönüşür.','Y: nitrifikasyon'),A('Z’yi bul','Nitrat tekrar N2 gazına denitrifikasyon bakterileriyle döner.','Z: denitrifikasyon'),A('Sonuç','Doğru sıra dördüncü şıktadır.','X, Y, Z')]),
 dict(m='Karbon döngüsünün basamakları şöyledir:\nAtmosferdeki CO2 —(X)→ Organik madde —(Y)→ Atmosferdeki CO2\nÖlü canlıdaki organik madde —(Z)→ Atmosferdeki CO2\nBuna göre X, Y ve Z süreçleri aşağıdakilerden hangisinde doğru verilmiştir?',
  o=[('X: Solunum, Y: Fotosentez, Z: Ayrışma','X ile Y’yi ters yazmak.','bilgi'),('X: Fotosentez, Y: Ayrışma, Z: Solunum','Y ile Z’yi karıştırmak.','bilgi'),('X: Ayrışma, Y: Solunum, Z: Fotosentez','Z’yi fotosentez sanmak.','bilgi'),('X: Solunum, Y: Ayrışma, Z: Fotosentez','Üç basamağı karıştırmak.','bilgi'),('X: Fotosentez, Y: Solunum, Z: Ayrışma',None,None)],
  ad=[A('X’i bul','CO2’nin organik maddeye geçişi fotosentezdir.','X: fotosentez'),A('Y’yi bul','Canlıların organik maddeyi solunumla yakması CO2 verir.','Y: solunum'),A('Z’yi bul','Ölü canlıların ayrıştırıcılarla ayrışması CO2’yi atmosfere döndürür.','Z: ayrışma'),A('Sonuç','X fotosentez, Y solunum, Z ayrışmadır.','X, Y, Z')]),
 'azot döngüsü basamakları','karbon döngüsüne geçildi')
a=400+80-60+30-20; assert a==430 and a/5==86
b=600+120-90+40-45; assert b==625 and b/5==125
Q(P,PRE,'0006','ek-populasyon','Popülasyon büyüklüğü ve yoğunluğu','zor','Popülasyon','Doğum, ölüm ve göçlerden yıl sonu popülasyon yoğunluğunu hesaplar.','yeni nesil',5,
 'Doğum, ölüm, giriş ve çıkış verilerinden popülasyon büyüklüğü ve yoğunluğu bulunur.','Göçle giren ya da çıkanları hesaba katmamak.',[POP],
 'Önce yeni birey sayısını bul, sonra alana böl.',
 dict(m='5 km² büyüklüğündeki bir alanda yaşayan bir popülasyonda yıl başında 400 birey vardır. Bir yıl içinde 80 birey doğmuş, 60 birey ölmüş, dışarıdan 30 birey gelmiş ve 20 birey başka bir alana göç etmiştir.\nBuna göre yıl sonunda bu popülasyonun yoğunluğu kaç birey/km²’dir?',i='Yıl sonu popülasyon yoğunluğu (birey/km²).',ip=['Yıl sonu birey sayısını bul.','Doğum ve göçle gelenler artırır, ölenler ve göç edenler azaltır.','Yoğunluk = birey sayısı ÷ alan.'],
  o=[('70','Doğumları hesaba katmamak.','dikkat'),('80','Yıl başındaki sayıyı alana bölmek.','dikkat'),('86',None,None),('90','Göç edenleri çıkarmayı unutmak.','dikkat'),('98','Ölenleri çıkarmayı unutmak.','dikkat')],
  ad=[A('Artanlar','Doğumlar ve dışarıdan gelenler sayıyı artırır.','+ 80 + 30'),A('Azalanlar','Ölenler ve göç edenler sayıyı azaltır.','− 60 − 20'),A('Yıl sonu sayı','Başlangıçtaki sayıya değişimi uygula.','400 + 80 − 60 + 30 − 20 = 430'),A('Yoğunluk','Birey sayısı alana bölünür.','430 ÷ 5 = 86'),A('Sonuç','Yoğunluk 86 birey/km²’dir.','86')]),
 dict(m='5 km² büyüklüğündeki bir alanda yaşayan bir popülasyonda yıl başında 600 birey vardır. Bir yıl içinde 120 birey doğmuş, 90 birey ölmüş, dışarıdan 40 birey gelmiş ve 45 birey başka bir alana göç etmiştir.\nBuna göre yıl sonunda bu popülasyonun yoğunluğu kaç birey/km²’dir?',
  o=[('117','Dışarıdan gelenleri hesaba katmamak.','dikkat'),('125',None,None),('134','Göç edenleri çıkarmayı unutmak.','dikkat'),('143','Ölenleri çıkarmayı unutmak.','dikkat'),('152','Ölenleri ve göç edenleri çıkarmayı unutmak.','dikkat')],
  ad=[A('Artanlar','Doğumlar ve dışarıdan gelenler sayıyı artırır.','+ 120 + 40'),A('Azalanlar','Ölenler ve göç edenler sayıyı azaltır.','− 90 − 45'),A('Yıl sonu sayı','Başlangıçtaki sayıya değişimi uygula.','600 + 120 − 90 + 40 − 45 = 625'),A('Yoğunluk','Birey sayısı alana bölünür.','625 ÷ 5 = 125'),A('Sonuç','Yoğunluk 125 birey/km²’dir.','125')]),
 'doğum, ölüm, göç ve alan','sayılar ve hata kaynakları değişti')
bitir(P,'ekosistem','Ekosistem','bio|Ekosistem',6)
