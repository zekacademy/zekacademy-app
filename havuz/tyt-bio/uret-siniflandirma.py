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
P=Parti('siniflandirma','Canlıların Sınıflandırılması','bio|Canlıların Sınıflandırılması',ders='TYT Biyoloji',idon='tytbio')
PRE='BSI'
BAS=B('Sınıflandırma basamakları','Küçükten büyüğe: tür → cins → familya → takım → sınıf → şube → âlem · Tür basamağında benzerlik en fazla, âlemde en azdır')
IKI=B('İkili adlandırma','Her canlının adı cins + tür adından oluşur (Linne). Örnek: Felis catus (ev kedisi): Felis cins, catus tür adıdır · Cins adı büyük harfle başlar, tür adı küçük harfle yazılır')
ALM=B('Beş âlem','Bakteriler: prokaryot · Protista: ökaryot, çoğu tek hücreli · Mantarlar: ökaryot, heterotrof, hücre duvarı kitin · Bitkiler: ökaryot, ototrof, hücre duvarı selüloz · Hayvanlar: ökaryot, heterotrof, hücre duvarı yok')
DIK=B('Dikotomik anahtar','Her basamakta iki seçenek (a ve b) vardır; canlının özelliğine uyan seçeneğin yönlendirdiği basamağa geçilir ve bir gruba ulaşılır')
Q(P,PRE,'0001','bs-basamak','Sınıflandırma basamakları','kolay','Taksonomik basamaklar','Sınıflandırma basamaklarını küçükten büyüğe sıralar.','düz',2,
 'Basamakların sırası ve aralarındaki konum sorulur.','Takım ile sınıfın yerini karıştırmak.',[BAS],
 'Tür en küçük, âlem en büyük basamaktır; aradakileri sırayla say.',
 dict(m='Canlıların sınıflandırılmasında kullanılan basamakların küçükten büyüğe doğru sıralanışı aşağıdakilerden hangisinde doğru verilmiştir?',i='Doğru basamak sırası.',ip=['En küçük basamak hangisi, en büyük hangisi?','Tür’den sonra hangi basamak gelir?','Sınıf ile şube arasında hangisi büyüktür?'],
  o=[('Tür – Familya – Cins – Takım – Sınıf – Şube – Âlem','Cins ile familyanın yerini değiştirmek.','bilgi'),('Tür – Cins – Takım – Familya – Sınıf – Şube – Âlem','Familya ile takımın yerini değiştirmek.','bilgi'),('Tür – Cins – Familya – Takım – Şube – Sınıf – Âlem','Sınıf ile şubenin yerini değiştirmek.','bilgi'),('Cins – Tür – Familya – Takım – Sınıf – Şube – Âlem','Tür ile cinsin yerini değiştirmek.','bilgi'),('Tür – Cins – Familya – Takım – Sınıf – Şube – Âlem',None,None)],
  ad=[A('Uçları belirle','Tür en küçük, âlem en büyük basamaktır.','tür … âlem'),A('Aradakileri sırala','Tür, cins, familya, takım, sınıf, şube sırasıyla büyür.','cins < familya < takım < sınıf < şube'),A('Sonuç','Doğru sıralama beşinci şıktadır.','Tür – Cins – Familya – Takım – Sınıf – Şube – Âlem')]),
 dict(m='Sınıflandırma basamakları içinde aşağıdakilerden hangisi familya ile sınıf arasında yer alır?',
  o=[('Cins','Cinsin familyadan küçük olduğunu bilmemek.','bilgi'),('Tür','Türün en küçük basamak olduğunu bilmemek.','bilgi'),('Şube','Şubenin sınıftan büyük olduğunu bilmemek.','bilgi'),('Âlem','Âlemin en büyük basamak olduğunu bilmemek.','bilgi'),('Takım',None,None)],
  i='Familya ile sınıf arasındaki basamak.',
  ad=[A('Sırayı yaz','Tür, cins, familya, takım, sınıf, şube, âlem.','küçükten büyüğe'),A('Aralığa bak','Familyadan sonra takım, ondan sonra sınıf gelir.','familya < takım < sınıf'),A('Sonuç','Arada yalnız takım bulunur.','Takım')]),
 'basamak sırası','sıralama yerine aralıktaki basamak')
Q(P,PRE,'0002','bs-ikili-ad','İkili adlandırma','orta','İkili adlandırma','Verilen bilimsel adlardan cins ve tür ilişkisini yorumlar.','öncüllü',3,
 'Bilimsel adlardan aynı cins ve aynı tür ilişkisi çıkarılır.','Cins adını paylaşan canlıları aynı tür sanmak.',[IKI,BAS],
 'İlk sözcük cinsi, ikinci sözcük türü gösterir: cins aynıysa tür farklı olabilir.',
 dict(m='Dört canlının bilimsel adları aşağıda verilmiştir:\nFelis catus (ev kedisi)\nFelis silvestris (yaban kedisi)\nCanis lupus (kurt)\nCanis aureus (çakal)\nBu canlılarla ilgili,\nI. Felis catus ile Felis silvestris aynı cinstedir.\nII. Canis lupus ile Felis catus aynı cinstedir.\nIII. Dördü de birbirinden farklı türlerdir.\nifadelerinden hangileri doğrudur?',i='Doğru olan ifadeler.',ip=['Bilimsel adın ilk sözcüğü neyi gösterir?','Aynı cinsteki iki canlı aynı tür olabilir mi?','Dört adın ikinci sözcüklerini karşılaştır.'],
  o=[('Yalnız I','Dört canlının farklı tür olduğunu görmemek.','dikkat'),('Yalnız III','Aynı cinsteki canlıları fark etmemek.','dikkat'),('I ve III',None,None),('I ve II','Farklı cinsteki canlıları aynı cins sanmak.','bilgi'),('II ve III','Cins adlarını yanlış okumak.','dikkat')],
  ad=[A('Adı çöz','İlk sözcük cins, ikinci sözcük tür adıdır.','Felis | Canis'),A('I. ifade','Felis catus ve Felis silvestris’in ilk sözcüğü aynı: aynı cinstedirler.','I doğru'),A('II. ifade','Canis lupus’un cinsi Canis, Felis catus’un cinsi Felis’tir.','II yanlış'),A('III. ifade','Dört adın ikinci sözcükleri (tür adları) farklıdır.','III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 dict(m='Dört bitkinin bilimsel adları aşağıda verilmiştir:\nQuercus robur (saplı meşe)\nQuercus cerris (saçlı meşe)\nPinus nigra (karaçam)\nPinus sylvestris (sarıçam)\nBu bitkilerle ilgili,\nI. Quercus robur ile Quercus cerris aynı cinsteki iki farklı türdür.\nII. Pinus nigra ile Pinus sylvestris aynı türdür.\nIII. Quercus robur ile Pinus nigra aynı cinstedir.\nifadelerinden hangileri doğrudur?',
  o=[('Yalnız I',None,None),('Yalnız II','Aynı cinsteki iki bitkiyi aynı tür sanmak.','bilgi'),('Yalnız III','Cins adlarının farklı olduğunu görmemek.','dikkat'),('I ve II','Pinus’un iki türünü aynı tür saymak.','bilgi'),('II ve III','Hem tür hem cins ilişkisini yanlış okumak.','bilgi')],
  ad=[A('Adı çöz','İlk sözcük cins, ikinci sözcük tür adıdır.','Quercus | Pinus'),A('I. ifade','İki meşenin cinsi Quercus, tür adları farklıdır: robur ve cerris.','I doğru'),A('II. ifade','Pinus nigra ile Pinus sylvestris’in tür adları farklıdır.','II yanlış'),A('III. ifade','Quercus ve Pinus farklı cinslerdir.','III yanlış'),A('Sonuç','Yalnız I doğrudur.','Yalnız I')]),
 'Felis ve Canis adları','bitki adları, ifadeler değişti')
TB1='Üç âleme ait canlı grubunun özellikleri tabloda verilmiştir.\n\nGrup | Hücre tipi | Beslenme | Hücre duvarı\nX | Prokaryot | Ototrof ya da heterotrof | Bulunur\nY | Ökaryot | Heterotrof | Kitin yapılı\nZ | Ökaryot | Ototrof | Selüloz yapılı\n\nBuna göre X, Y ve Z gruplarının âlemleri aşağıdakilerden hangisinde doğru verilmiştir?'
TB2='Üç âleme ait canlı grubunun özellikleri tabloda verilmiştir.\n\nGrup | Hücre tipi | Beslenme | Hücre duvarı\nK | Ökaryot | Heterotrof | Bulunmaz\nL | Prokaryot | Ototrof ya da heterotrof | Bulunur\nM | Ökaryot | Heterotrof | Kitin yapılı\n\nBuna göre K, L ve M gruplarının âlemleri aşağıdakilerden hangisinde doğru verilmiştir?'
Q(P,PRE,'0003','bs-alem-tablo','Âlemlerin özellikleri','orta','Âlemler','Hücre tipi, beslenme ve hücre duvarı özelliklerinden âlemi belirler.','tablo',3,
 'Tablodaki üç özellikten âlem belirlenir.','Bitki ile mantarın hücre duvarı yapısını karıştırmak.',[ALM],
 'Hücre tipi, beslenme ve hücre duvarının yapısı âlemi ayırır.',
 dict(m=TB1,i='X, Y ve Z’nin âlemleri.',ip=['Prokaryot olan grup hangisi?','Hücre duvarı kitin olan ökaryotlar hangi âlemdedir?','Selülozlu duvarı ve ototrof beslenmesi olan grup hangisi?'],
  o=[('X: Bakteriler, Y: Bitkiler, Z: Mantarlar','Kitin ve selüloz duvarı karıştırmak.','bilgi'),('X: Bakteriler, Y: Mantarlar, Z: Bitkiler',None,None),('X: Protista, Y: Mantarlar, Z: Bitkiler','Prokaryot grubu Protista sanmak.','bilgi'),('X: Mantarlar, Y: Bakteriler, Z: Bitkiler','Hücre tipini hiç kullanmamak.','dikkat'),('X: Bakteriler, Y: Hayvanlar, Z: Bitkiler','Hayvanlarda hücre duvarı bulunmadığını atlamak.','bilgi')],
  ad=[A('X’i belirle','Prokaryot tek ökaryot olmayan âlem bakterilerdir.','X: bakteriler'),A('Y’yi belirle','Ökaryot, heterotrof, kitin duvarlı: mantarlar.','Y: mantarlar'),A('Z’yi belirle','Ökaryot, ototrof, selüloz duvarlı: bitkiler.','Z: bitkiler'),A('Sonuç','X bakteri, Y mantar, Z bitkidir.','X, Y, Z')]),
 dict(m=TB2,i='K, L ve M’nin âlemleri.',
  o=[('K: Hayvanlar, L: Mantarlar, M: Bakteriler','Kitinli duvarı bakterilere atfetmek.','bilgi'),('K: Protista, L: Bakteriler, M: Hayvanlar','Duvarı olmayan grubu protista sanmak ve hayvanı M’ye yazmak.','dikkat'),('K: Hayvanlar, L: Bakteriler, M: Mantarlar',None,None),('K: Mantarlar, L: Bakteriler, M: Hayvanlar','Hücre duvarı olmayan hayvanı mantar sanmak.','bilgi'),('K: Bitkiler, L: Bakteriler, M: Mantarlar','Heterotrof, duvarsız grubu bitki sanmak.','bilgi')],
  ad=[A('L’yi belirle','Prokaryot yalnız bakteriler âlemindedir.','L: bakteriler'),A('K’yi belirle','Ökaryot, heterotrof, hücre duvarı yok: hayvanlar.','K: hayvanlar'),A('M’yi belirle','Ökaryot, heterotrof, kitin duvarlı: mantarlar.','M: mantarlar'),A('Sonuç','K hayvan, L bakteri, M mantardır.','K, L, M')]),
 'âlem özellikleri tablosu','farklı gruplar ve harfler')
Q(P,PRE,'0004','bs-dikotom','Dikotomik anahtar','orta','Dikotomik anahtar','Dikotomik anahtarı izleyerek canlıların hangi gruba ait olduğunu belirler.','tablo',3,
 'Anahtarın seçeneklerini izleyerek canlı grubu bulunur.','Anahtardaki yönlendirmeyi yanlış izlemek.',[DIK,ALM],
 'Anahtarda her basamakta özelliğe uyan seçeneği seç ve gösterilen yere git.',
 dict(m='Beş âleme ait canlıları ayırt etmek için hazırlanan dikotomik anahtar aşağıda verilmiştir:\n1a. Çekirdek zarı yoktur → Bakteriler\n1b. Çekirdek zarı vardır → 2’ye git\n2a. Fotosentez yapar → 3’e git\n2b. Fotosentez yapmaz → 4’e git\n3a. Tek hücrelidir → Protista\n3b. Çok hücrelidir → Bitkiler\n4a. Hücre duvarı vardır → Mantarlar\n4b. Hücre duvarı yoktur → Hayvanlar\nÖzellikleri şöyle olan K, L ve M canlıları için;\nK: Çekirdek zarı vardır, fotosentez yapar, tek hücrelidir.\nL: Çekirdek zarı yoktur.\nM: Çekirdek zarı vardır, fotosentez yapmaz, hücre duvarı yoktur.\nbu anahtara göre K, L ve M hangi gruplara aittir?',i='K, L ve M’nin grupları.',ip=['L için 1. basamakta hangi seçenek uyar?','K için 2a ve 3a seçeneklerini izle.','M için 2b ve 4b seçeneklerini izle.'],
  o=[('K: Bitkiler, L: Bakteriler, M: Hayvanlar','K’yi çok hücreli bitki sanmak.','dikkat'),('K: Protista, L: Bakteriler, M: Mantarlar','M’nin hücre duvarı olmadığını görmemek.','dikkat'),('K: Protista, L: Bakteriler, M: Hayvanlar',None,None),('K: Protista, L: Hayvanlar, M: Bakteriler','L ile M’nin çekirdek zarı bilgisini karıştırmak.','dikkat'),('K: Bakteriler, L: Protista, M: Hayvanlar','K’nin çekirdek zarlı olduğunu görmemek.','dikkat')],
  ad=[A('L’yi bul','L’de çekirdek zarı yok; 1a seçeneği uyar.','L: Bakteriler'),A('K’yi bul','Çekirdek zarı var (1b), fotosentez yapıyor (2a), tek hücreli (3a).','K: Protista'),A('M’yi bul','Çekirdek zarı var (1b), fotosentez yok (2b), duvar yok (4b).','M: Hayvanlar'),A('Sonuç','K Protista, L Bakteriler, M Hayvanlardır.','K, L, M')]),
 dict(m='Dört canlı grubunu ayırt etmek için hazırlanan dikotomik anahtar aşağıda verilmiştir:\n1a. Hücre duvarı yoktur → 2’ye git\n1b. Hücre duvarı vardır → 3’e git\n2a. Çok hücrelidir, heterotrof beslenir → Hayvanlar\n2b. Çok hücreli değildir → Protista\n3a. Çekirdek zarı yoktur → Bakteriler\n3b. Çekirdek zarı vardır, duvarı kitin yapılıdır → Mantarlar\nÖzellikleri şöyle olan X, Y ve Z canlıları için;\nX: Hücre duvarı vardır, çekirdek zarı vardır, duvarı kitin yapılıdır.\nY: Hücre duvarı yoktur, çok hücrelidir, heterotrof beslenir.\nZ: Hücre duvarı vardır, çekirdek zarı yoktur.\nbu anahtara göre X, Y ve Z hangi gruplara aittir?',
  o=[('X: Bakteriler, Y: Hayvanlar, Z: Mantarlar','Çekirdek zarı bilgisini yanlış yönlendirmek.','dikkat'),('X: Mantarlar, Y: Hayvanlar, Z: Bakteriler',None,None),('X: Mantarlar, Y: Protista, Z: Bakteriler','Y’nin çok hücreli olduğunu görmemek.','dikkat'),('X: Protista, Y: Hayvanlar, Z: Bakteriler','X’in hücre duvarını görmemek.','dikkat'),('X: Mantarlar, Y: Bakteriler, Z: Hayvanlar','Y ve Z’nin yönlendirmelerini karıştırmak.','dikkat')],
  ad=[A('X’i bul','Hücre duvarı var (1b), çekirdek zarı ve kitin duvar var (3b).','X: Mantarlar'),A('Y’yi bul','Hücre duvarı yok (1a), çok hücreli ve heterotrof (2a).','Y: Hayvanlar'),A('Z’yi bul','Hücre duvarı var (1b), çekirdek zarı yok (3a).','Z: Bakteriler'),A('Sonuç','X Mantarlar, Y Hayvanlar, Z Bakteriler.','X, Y, Z')]),
 'beş âlem anahtarı','anahtar yapısı ve canlılar değişti')
# 0005
def say(l):
    return len({(g,t) for g,t,f in l}),len({g for g,t,f in l}),len({f for g,t,f in l})
l1=[('Panthera','leo','Felidae'),('Panthera','tigris','Felidae'),('Felis','catus','Felidae'),('Canis','lupus','Canidae'),('Canis','aureus','Canidae'),('Panthera','leo','Felidae'),('Canis','lupus','Canidae')]
assert say(l1)==(5,3,2)
l2=[('Quercus','robur','Fagaceae'),('Quercus','cerris','Fagaceae'),('Pinus','nigra','Pinaceae'),('Pinus','sylvestris','Pinaceae'),('Quercus','robur','Fagaceae'),('Fagus','orientalis','Fagaceae'),('Abies','nordmanniana','Pinaceae'),('Pinus','nigra','Pinaceae')]
assert say(l2)==(6,4,2)
Q(P,PRE,'0005','bs-takson-say','Tür, cins ve familya sayısı','zor','Basamaklara göre sayma','Birey listesinden farklı tür, cins ve familya sayısını bulur.','tablo',4,
 'Tekrar eden bireyler çıkarılarak tür, cins ve familya sayıları ayrı ayrı sayılır.','Birey sayısını tür sayısı sanmak.',[IKI,BAS],
 'Tür = ikili adın tamamı; cins = ilk sözcük; aynı ad tekrar ederse yeni tür sayma.',
 dict(m='Bir araştırmada yedi canlı birey incelenmiş ve bilimsel adları ile familyaları aşağıdaki tabloda verilmiştir.\n\nBirey | Bilimsel ad | Familya\n1 | Panthera leo | Felidae\n2 | Panthera tigris | Felidae\n3 | Felis catus | Felidae\n4 | Canis lupus | Canidae\n5 | Canis aureus | Canidae\n6 | Panthera leo | Felidae\n7 | Canis lupus | Canidae\n\nBuna göre bu bireyler sırasıyla kaç farklı türe, kaç farklı cinse ve kaç farklı familyaya aittir?',i='Farklı tür, cins ve familya sayıları.',ip=['Aynı bilimsel adı taşıyan bireyler aynı türdür.','Cins, bilimsel adın ilk sözcüğüdür.','Familya sütunundaki farklı adları say.'],
  o=[('5 – 3 – 2',None,None),('5 – 2 – 2','Cins sayısını familya sayısına eşitlemek.','dikkat'),('7 – 3 – 2','Birey sayısını tür sayısı sanmak.','dikkat'),('7 – 5 – 2','Her bireyi ayrı tür ve her adı cins saymak.','dikkat'),('5 – 5 – 3','Her türü ayrı cins saymak ve familyayı yanlış saymak.','dikkat')],
  ad=[A('Türleri say','Aynı bilimsel adlar tek tür sayılır: leo, tigris, catus, lupus, aureus.','Panthera leo, P. tigris, Felis catus, Canis lupus, C. aureus = 5'),A('Cinsleri say','İlk sözcükler: Panthera, Felis, Canis.','3 cins'),A('Familyaları say','Felidae ve Canidae.','2 familya'),A('Sonuç','Sırasıyla tür, cins, familya.','5 – 3 – 2')]),
 dict(m='Bir ormanda sekiz ağaç incelenmiş ve bilimsel adları ile familyaları aşağıdaki tabloda verilmiştir.\n\nAğaç | Bilimsel ad | Familya\n1 | Quercus robur | Fagaceae\n2 | Quercus cerris | Fagaceae\n3 | Pinus nigra | Pinaceae\n4 | Pinus sylvestris | Pinaceae\n5 | Quercus robur | Fagaceae\n6 | Fagus orientalis | Fagaceae\n7 | Abies nordmanniana | Pinaceae\n8 | Pinus nigra | Pinaceae\n\nBuna göre bu ağaçlar sırasıyla kaç farklı türe, kaç farklı cinse ve kaç farklı familyaya aittir?',
  o=[('6 – 2 – 2','Cins sayısını familya sayısına eşitlemek.','dikkat'),('6 – 4 – 3','Familya sayısını yanlış saymak.','dikkat'),('8 – 4 – 2','Birey sayısını tür sayısı sanmak.','dikkat'),('6 – 4 – 2',None,None),('8 – 6 – 2','Her bireyi ayrı tür ve her adı cins saymak.','dikkat')],
  ad=[A('Türleri say','Aynı bilimsel adlar tek tür sayılır: robur, cerris, nigra, sylvestris, orientalis, nordmanniana.','6 tür'),A('Cinsleri say','İlk sözcükler: Quercus, Pinus, Fagus, Abies.','4 cins'),A('Familyaları say','Fagaceae ve Pinaceae.','2 familya'),A('Sonuç','Sırasıyla tür, cins, familya.','6 – 4 – 2')]),
 'tür/cins/familya tablosu','canlılar ve tablodaki tekrarlar değişti')
Q(P,PRE,'0006','bs-alem-yorum','Âlemler arası karşılaştırma','zor','Âlemler','Birden fazla âlemin ortak ve ayırıcı özelliklerini değerlendirir.','öncüllü',4,
 'Birden fazla âlemin özellikleri karşılaştırılarak doğru yargılar seçilir.','Bitki ve mantarın hücre duvarı farkını karıştırmak.',[ALM],
 'Âlem özelliklerini hücre tipi, beslenme ve hücre duvarı üç başlığında karşılaştır.',
 dict(m='Âlemlerle ilgili,\nI. Mantarlar ve hayvanlar heterotrof beslenir.\nII. Bakterilerin ve protistaların hepsinde çekirdek zarı bulunur.\nIII. Bitkilerin ve mantarların hücrelerinde hücre duvarı bulunur.\nifadelerinden hangileri doğrudur?',i='Doğru olan ifadeler.',ip=['Bakteriler prokaryot mu, ökaryot mu?','Hayvan hücresinde hücre duvarı var mı?','Mantarlar kendi besinini üretir mi?'],
  o=[('Yalnız I','Hücre duvarının hem bitki hem mantarda bulunduğunu atlamak.','bilgi'),('Yalnız III','Mantar ve hayvanların heterotrof olduğunu atlamak.','bilgi'),('I ve II','Bakterilerin çekirdek zarına sahip olduğunu sanmak.','bilgi'),('I ve III',None,None),('I, II ve III','Prokaryot bakterilerde çekirdek zarı olduğunu sanmak.','bilgi')],
  ad=[A('I. ifade','Mantarlar ve hayvanlar hazır organik madde ile beslenen heterotroflardır.','I doğru'),A('II. ifade','Bakteriler prokaryottur; çekirdek zarı yoktur.','II yanlış'),A('III. ifade','Bitkilerde selüloz, mantarlarda kitin yapılı hücre duvarı bulunur.','III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 dict(m='Âlemlerle ilgili,\nI. Bitkilerin hepsi ökaryot hücrelidir.\nII. Hayvan hücrelerinde hücre duvarı bulunur.\nIII. Bakterilerin hepsi heterotrof beslenir.\nifadelerinden hangileri doğrudur?',
  o=[('I ve II','Hayvan hücresinde hücre duvarı olmadığını bilmemek.','bilgi'),('Yalnız I',None,None),('Yalnız II','Bitkilerin ökaryot olduğunu atlamak.','bilgi'),('II ve III','Hayvan hücre duvarı ve bakteri beslenmesini yanlış bilmek.','bilgi'),('I ve III','Bazı bakterilerin ototrof olduğunu unutmak.','bilgi')],
  ad=[A('I. ifade','Bitkiler ökaryot hücrelidir.','I doğru'),A('II. ifade','Hayvan hücrelerinde hücre duvarı yoktur.','II yanlış'),A('III. ifade','Bazı bakteriler fotosentez ya da kemosentezle ototrof beslenir.','III yanlış'),A('Sonuç','Yalnız I doğrudur.','Yalnız I')]),
 'üç âlem karşılaştırması','farklı âlemler ve ifadeler')
bitir(P,'siniflandirma','Canlıların Sınıflandırılması','bio|Canlıların Sınıflandırılması',6)
