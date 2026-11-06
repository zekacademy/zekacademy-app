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
P=Parti('hucre','Hücre ve Organeller – Madde Geçişleri','bio|Hücre ve Organeller – Madde Geçişleri',ders='TYT Biyoloji',idon='tytbio')
PRE='BHU'
ORG=B('Organeller ve görevleri','Ribozom: protein sentezi · Lizozom: hücre içi sindirim · Mitokondri: hücresel solunumla ATP üretimi · Golgi cisimciği: madde paketleme ve salgılama · Kloroplast: fotosentez')
PRO=B('Prokaryot ve ökaryot','Prokaryotta (bakteri) çekirdek zarı ve zarlı organeller yoktur; DNA sitoplazmadadır, tek organel ribozomdur. Ökaryotta (bitki, hayvan, mantar) çekirdek ve zarlı organeller bulunur')
GEC=B('Madde geçiş türleri','Basit difüzyon: çok → az, protein yok, ATP yok · Kolaylaştırılmış difüzyon: çok → az, taşıyıcı protein var, ATP yok · Aktif taşıma: az → çok, taşıyıcı protein var, ATP harcanır')
OZM=B('Ozmoz','Suyun yarı geçirgen zardan, su oranı çok olan (seyrek) ortamdan az olan (derişik) ortama geçmesidir · Saf su = su oranı en yüksek ortam')
BIT=B('Bitki hücresi ve su','Derişik ortamda hücre su kaybeder, hücre zarı duvardan ayrılır (plazmoliz) · Seyrek ortamda su alır, turgor basıncı artar; hücre duvarı hücrenin patlamasını önler')
SAL=B('Salgı proteini yolu','Ribozomda sentezlenir, endoplazmik retikuluma geçer, Golgi cisimciğinde paketlenir, keseciklerle hücre zarına taşınıp dışarı verilir')
IKZ=B('Çift zarlı organeller','Mitokondri ve kloroplast çift zarlıdır; her ikisinde kendine ait DNA ve ribozom bulunur · Fotosentez yalnız kloroplastta, hücresel solunum mitokondride yapılır')
HUC=B('Hücre türü ve organel','Bir organelin bol olması hücrenin işine işaret eder: çok enerji harcayan hücrede mitokondri, salgı yapan hücrede granüllü ER ve Golgi, bakteri yutan hücrede lizozom, ışıkla beslenen hücrede kloroplast bol bulunur')

Q(P,PRE,'0001','hc-organel-gorev','Organel–görev eşleştirme','kolay','Organeller ve görevleri','Temel organellerin görevlerini eşleştirir.','öncüllü',2,
 'Organel adı ile görevi verilir; doğru eşleşmeler seçilir.','Golgi cisimciğini enerji üretimiyle karıştırmak.',[ORG],
 'Organelin adını görevine bağlayan tek cümle ezberi: ribozom–protein, mitokondri–enerji, lizozom–sindirim, Golgi–paketleme.',
 dict(m='Bazı organeller ve görevleri aşağıda eşleştirilmiştir.\nI. Ribozom: Protein sentezi\nII. Lizozom: Hücre içi sindirim\nIII. Golgi cisimciği: ATP üretimi\nBu eşleştirmelerden hangileri doğrudur?',
  i='Doğru eşleştirilmiş organel–görev çiftleri.',ip=['Her organeli görevine tek tek bağla.','ATP üretimi hangi organele aittir?','Golgi cisimciği madde üretmez, ne yapar?'],
  o=[('Yalnız I','Lizozomun hücre içi sindirim görevini bilmemek.','bilgi'),('Yalnız II','Ribozomun protein sentezi yaptığını bilmemek.','bilgi'),('I ve II',None,None),('II ve III','Golgi cisimciğini enerji üreten organel sanmak, ribozomu atlamak.','bilgi'),('I, II ve III','Golgi cisimciği ile mitokondriyi karıştırıp III’ü de doğru saymak.','bilgi')],
  ad=[A('Eşleşmeleri oku','Her satırda bir organel ve bir görev var.','I, II, III ayrı ayrı sınanır'),A('I. ve II. satır','Ribozom amino asitleri birleştirip protein yapar. Lizozom sindirim enzimleriyle hücre içi sindirim yapar.','I doğru · II doğru'),A('III. satır','ATP’yi mitokondri üretir. Golgi cisimciği ise maddeleri paketler ve salgılar.','III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 dict(m='I. Çekirdek: Kalıtım materyalini barındırma\nII. Kloroplast: Hücresel solunumla ATP üretme\nIII. Golgi cisimciği: Maddeleri paketleyip salgılama\nYukarıdaki organel–görev eşleştirmelerinden hangileri doğrudur?',
  o=[('I ve III',None,None),('Yalnız II','Çekirdeğin yönetim ve kalıtım materyalini barındırma görevini atlamak.','bilgi'),('Yalnız III','Çekirdek eşleşmesini görmeden yalnız Golgi’yi seçmek.','dikkat'),('I ve II','Kloroplastın görevini hücresel solunum sanıp III’ü atlamak.','bilgi'),('I, II ve III','Kloroplastı mitokondriyle karıştırıp II’yi doğru saymak.','bilgi')],
  ad=[A('Satırları ayır','Üç eşleştirmeyi ayrı ayrı değerlendir.','I, II, III'),A('I. ve III. satır','DNA çekirdekte bulunur. Golgi cisimciği keseciklerle maddeleri paketler ve salgılar.','I doğru · III doğru'),A('II. satır','Kloroplast fotosentez yapar; hücresel solunum mitokondridedir.','II yanlış'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 'çekirdek–kalıtım, kloroplast–fotosentez','görev eşleştirme kurgusu değişti')

Q(P,PRE,'0002','hc-prokaryot','Prokaryot ve ökaryot hücre','kolay','Hücre tipleri','Prokaryot hücrede bulunan ve bulunmayan yapıları ayırt eder.','düz',2,
 'Bakteri hücresinde bulunabilecek tek yapı ya da bulunmayan yapı sorulur.','Bakteride de mitokondri ve endoplazmik retikulum olduğunu sanmak.',[PRO],
 'Prokaryotta zarlı organel yok; tek organel ribozomdur.',
 dict(m='Bir bakteri hücresinde aşağıdaki yapılardan hangisi bulunur?',i='Bakteri hücresinde bulunan yapı.',ip=['Bakteri prokaryottur; çekirdek zarı var mı?','Zarlı organeller bakteride bulunur mu?','Prokaryotta bulunan tek organeli hatırla.'],
  o=[('Mitokondri','Bakteriyi ökaryot gibi düşünüp zarlı organel aramak.','bilgi'),('Golgi cisimciği','Zarlı organelin prokaryotta bulunmadığını bilmemek.','bilgi'),('Lizozom','Zarlı organelin prokaryotta bulunmadığını bilmemek.','bilgi'),('Endoplazmik retikulum','Zarlı organelin prokaryotta bulunmadığını bilmemek.','bilgi'),('Ribozom',None,None)],
  ad=[A('Hücre tipini belirle','Bakteri prokaryot bir hücredir.','prokaryot'),A('Özelliği hatırla','Prokaryotta çekirdek zarı ve zarlı organel yoktur; protein sentezi için ribozom bulunur.','tek organel: ribozom'),A('Şıkları ele','Mitokondri, Golgi, lizozom ve endoplazmik retikulum zarlı organeldir.','hepsi elenir'),A('Sonuç','Bakteride bulunan yapı ribozomdur.','Ribozom')]),
 dict(m='Aşağıdakilerden hangisi bir bakteri hücresinde bulunmaz?',i='Bakteri hücresinde bulunmayan yapı.',ip=['Bakteri prokaryottur; çekirdek zarı var mı?','Zarlı organeller bakteride bulunur mu?','Prokaryotta bulunan tek organeli hatırla.'],
  o=[('Ribozom','Ribozomun prokaryotta da bulunduğunu bilmemek.','bilgi'),('Hücre zarı','Her canlı hücrede hücre zarı bulunduğunu unutmak.','bilgi'),('Sitoplazma','Bakteride sitoplazma olmadığını sanmak.','bilgi'),('Çekirdek zarı',None,None),('DNA','Bakteride DNA’nın bulunduğunu unutmak; bakteri DNA’sı sitoplazmadadır.','bilgi')],
  ad=[A('Hücre tipini belirle','Bakteri prokaryot bir hücredir.','prokaryot'),A('Ortak yapıları ayır','Her hücrede hücre zarı, sitoplazma, DNA ve ribozom bulunur.','ribozom, zar, sitoplazma, DNA vardır'),A('Eksik olanı bul','Çekirdek zarı yalnız ökaryotta bulunur.','çekirdek zarı yok'),A('Sonuç','Bakteride bulunmayan yapı çekirdek zarıdır.','Çekirdek zarı')]),
 'bakteride bulunan yapı','soru yönü "bulunmaz" oldu')

TAB1='Üç farklı madde (X, Y, Z) hücre zarından geçerken yapılan gözlemler tabloda verilmiştir.\n\nMadde | Geçiş yönü | Taşıyıcı protein | ATP harcanması\nX | Çok derişimliden az derişimliye | Yok | Yok\nY | Çok derişimliden az derişimliye | Var | Yok\nZ | Az derişimliden çok derişimliye | Var | Var\n\nBuna göre X, Y ve Z maddelerinin geçiş türleri aşağıdakilerden hangisinde doğru verilmiştir?'
TAB2='Dört farklı madde (K, L, M) hücre zarından geçerken yapılan gözlemler tabloda verilmiştir.\n\nMadde | Geçiş yönü | Taşıyıcı protein | ATP harcanması\nK | Az derişimliden çok derişimliye | Var | Var\nL | Çok derişimliden az derişimliye | Yok | Yok\nM | Çok derişimliden az derişimliye | Var | Yok\n\nBuna göre K, L ve M maddelerinin geçiş türleri aşağıdakilerden hangisinde doğru verilmiştir?'.replace('Dört','Üç')
Q(P,PRE,'0003','hc-gecis-turu','Madde geçiş türleri','orta','Madde geçişleri','Geçiş yönü, taşıyıcı protein ve ATP verilerinden madde geçiş türünü belirler.','tablo',3,
 'Tablodaki üç özellikten geçiş türü çıkarılır.','Taşıyıcı proteini olan her geçişi aktif taşıma sanmak.',[GEC],
 'ATP harcanıyorsa aktif taşıma; ATP yok ama taşıyıcı varsa kolaylaştırılmış difüzyon.',
 dict(m=TAB1,i='X, Y ve Z’nin geçiş türleri.',ip=['Önce ATP harcanan maddeyi bul.','ATP’si olmayan iki maddeden hangisinde taşıyıcı protein var?','Taşıyıcısız ve ATP’siz geçiş hangi türdür?'],
  o=[('X: Basit difüzyon, Y: Aktif taşıma, Z: Kolaylaştırılmış difüzyon','Taşıyıcı proteini olan Y’yi aktif taşıma, ATP harcayan Z’yi kolaylaştırılmış sanmak.','bilgi'),('X: Basit difüzyon, Y: Kolaylaştırılmış difüzyon, Z: Aktif taşıma',None,None),('X: Kolaylaştırılmış difüzyon, Y: Basit difüzyon, Z: Aktif taşıma','Taşıyıcısı olmayan X ile taşıyıcısı olan Y’nin türlerini birbirine karıştırmak.','dikkat'),('X: Aktif taşıma, Y: Kolaylaştırılmış difüzyon, Z: Basit difüzyon','Geçiş yönü ve ATP verisini hiç kullanmamak.','dikkat'),('X: Basit difüzyon, Y: Basit difüzyon, Z: Aktif taşıma','Taşıyıcı proteinin varlığını göz ardı etmek.','dikkat')],
  ad=[A('Z’yi belirle','Az derişimliden çok derişimliye geçiş ve ATP harcanması aktif taşımanın özelliğidir.','Z: aktif taşıma'),A('X ve Y’yi ayır','İkisi de çoktan aza geçer ve ATP harcamaz. Fark taşıyıcı proteindedir.','X: protein yok · Y: protein var'),A('Türleri adlandır','Taşıyıcısız geçiş basit difüzyon, taşıyıcılı geçiş kolaylaştırılmış difüzyondur.','X: basit · Y: kolaylaştırılmış'),A('Sonuç','Doğru sıralama X basit, Y kolaylaştırılmış difüzyon, Z aktif taşımadır.','X, Y, Z')]),
 dict(m=TAB2,i='K, L ve M’nin geçiş türleri.',
  o=[('K: Aktif taşıma, L: Kolaylaştırılmış difüzyon, M: Basit difüzyon','L ile M’nin taşıyıcı protein durumunu karıştırmak.','dikkat'),('K: Aktif taşıma, L: Basit difüzyon, M: Kolaylaştırılmış difüzyon',None,None),('K: Kolaylaştırılmış difüzyon, L: Basit difüzyon, M: Aktif taşıma','Taşıyıcı proteini olan her geçişin ATP harcadığını sanmak.','bilgi'),('K: Basit difüzyon, L: Aktif taşıma, M: Kolaylaştırılmış difüzyon','Geçiş yönünü hiç dikkate almamak.','dikkat'),('K: Aktif taşıma, L: Basit difüzyon, M: Basit difüzyon','M’deki taşıyıcı proteini görmezden gelmek.','dikkat')],
  ad=[A('K’yi belirle','Az derişimliden çok derişimliye giden ve ATP harcayan geçiş aktif taşımadır.','K: aktif taşıma'),A('L ve M’yi ayır','Her ikisi çoktan aza geçer, ATP harcamaz. Taşıyıcı proteinle ayrılırlar.','L: protein yok · M: protein var'),A('Türleri adlandır','Taşıyıcısız geçiş basit difüzyon, taşıyıcılı geçiş kolaylaştırılmış difüzyondur.','L: basit · M: kolaylaştırılmış'),A('Sonuç','K aktif taşıma, L basit difüzyon, M kolaylaştırılmış difüzyondur.','K, L, M')]),
 'geçiş yönü + taşıyıcı + ATP tablosu','farklı harfler ve sıra')

Q(P,PRE,'0004','hc-ozmoz','Ozmoz ve bitki hücresi','orta','Ozmoz','Bitki hücresinin farklı derişimdeki ortamlarda davranışını yorumlar.','öncüllü',3,
 'Hücre çözeltisi ile ortamın derişimi karşılaştırılır; suyun yönü ve hücrenin durumu yorumlanır.','Bitki hücresinin saf suda da patlayacağını sanmak.',[OZM,BIT],
 'Su her zaman seyrek ortamdan derişik ortama geçer; bitki hücresi duvarı sayesinde patlamaz.',
 dict(m='Hücre özsuyunun derişimi %2 olan bir bitki hücresi %10’luk şeker çözeltisine konuluyor. Çözeltideki şekerin hücreye girmediği kabul edilecektir.\nBu hücreyle ilgili,\nI. Su hücreden dışarı çıkar.\nII. Hücre zarı hücre duvarından ayrılır.\nIII. Turgor basıncı artar.\nyargılarından hangileri doğrudur?',
  i='Doğru olan yargılar.',ip=['Hangi ortam daha derişik: hücre özsuyu mu, dış çözelti mi?','Su hangi yöne geçer?','Su kaybeden hücrenin turgor basıncı artar mı, azalır mı?'],
  o=[('Yalnız I','Su çıkışını görüp zarın duvardan ayrılmasını (plazmoliz) atlamak.','bilgi'),('Yalnız II','Suyun hücreden çıktığını görmeden sonucu yazmak.','dikkat'),('I ve II',None,None),('I ve III','Su kaybeden hücrenin turgor basıncının arttığını sanmak.','bilgi'),('II ve III','Turgor basıncının artmasını doğru sanıp su çıkışını atlamak.','bilgi')],
  ad=[A('Derişimleri karşılaştır','Dış çözelti %10, hücre özsuyu %2. Dış ortam daha derişiktir.','%10 > %2'),A('Suyun yönü','Su, seyrek ortamdan derişik ortama geçer; yani hücreden dışarı çıkar.','I doğru'),A('Hücrenin durumu','Su kaybeden hücrenin zarı duvardan ayrılır (plazmoliz) ve turgor basıncı azalır.','II doğru · III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 dict(m='Bir bitki hücresi saf suya konuluyor.\nBu hücreyle ilgili,\nI. Su hücre içine girer.\nII. Hücre zarı patlayana kadar su girişi sürer.\nIII. Turgor basıncı artar.\nyargılarından hangileri doğrudur?',
  o=[('I ve III',None,None),('Yalnız I','Turgor basıncının arttığını bilmemek.','bilgi'),('Yalnız III','Su girişini atlamak; turgor basıncı su girişinin sonucudur.','dikkat'),('I ve II','Bitki hücresinin hücre duvarı olduğunu unutup hayvan hücresi gibi patlayacağını sanmak.','bilgi'),('II ve III','Su girişini atlayıp patlama yargısını doğru saymak.','bilgi')],
  ad=[A('Ortamı karşılaştır','Saf su, hücre özsuyundan daha seyrektir; su oranı en yüksek ortamdır.','saf su < özsu'),A('Suyun yönü','Su, seyrek ortamdan derişik ortama, yani hücre içine geçer.','I doğru'),A('Hücre duvarının etkisi','Su alan hücrede turgor basıncı artar; hücre duvarı hücrenin patlamasını engeller.','III doğru · II yanlış'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 'bitki hücresi hipertonik ortamda','ortam saf su oldu, öncüller değişti')

Q(P,PRE,'0005','hc-protein-yolu','Salgı proteininin yolu','orta','Organellerin birlikte çalışması','Hücre dışına salgılanan proteinin organeller arasındaki yolunu sıralar.','düz',3,
 'Bir proteinin ribozomdan hücre zarına uzanan yolu sıralanır.','Golgi cisimciğini endoplazmik retikulumdan önce koymak.',[SAL,ORG],
 'Salgı proteini yolu: ribozom → endoplazmik retikulum → Golgi → kesecik → hücre zarı.',
 dict(m='Pankreas hücrelerinde sentezlenip hücre dışına salgılanan bir sindirim enzimi (protein), aşağıdaki yapılardan hangisinde belirtilen sırayla ilerler?',i='Proteinin izlediği doğru sıra.',ip=['Protein nerede sentezlenir?','Sentezlenen protein önce hangi zar sistemine girer?','Paketleme hangi organelin görevidir?'],
  o=[('Golgi cisimciği → Ribozom → Endoplazmik retikulum → Hücre zarı','Proteinin sentezinden önce paketlendiğini sanmak.','bilgi'),('Ribozom → Golgi cisimciği → Endoplazmik retikulum → Hücre zarı','Endoplazmik retikulum ile Golgi sırasını ters yazmak.','bilgi'),('Ribozom → Endoplazmik retikulum → Golgi cisimciği → Hücre zarı',None,None),('Endoplazmik retikulum → Ribozom → Golgi cisimciği → Hücre zarı','Ribozomun sentezi yaptığını, ER’nin sonra geldiğini unutmak.','bilgi'),('Ribozom → Lizozom → Golgi cisimciği → Hücre zarı','Lizozomu salgı yoluna katmak; lizozom sindirim yapar.','bilgi')],
  ad=[A('Başlangıç','Proteinler ribozomda sentezlenir.','ilk: ribozom'),A('Taşınma','Protein endoplazmik retikuluma geçer, buradan Golgi cisimciğine kesecikle gider.','ER → Golgi'),A('Paketleme ve salgı','Golgi cisimciği proteini paketler; kesecik hücre zarıyla birleşip proteini dışarı verir.','Golgi → zar'),A('Sonuç','Doğru sıra ribozom, endoplazmik retikulum, Golgi, hücre zarıdır.','Ribozom → ER → Golgi → zar')]),
 dict(m='Bir tükürük bezi hücresinde üretilen ve hücre dışına verilen amilaz enzimi için organellerin görev sırası aşağıdakilerden hangisidir?',
  o=[('Ribozom → Lizozom → Golgi cisimciği → Hücre zarı','Lizozomu salgı yolunun bir basamağı sanmak.','bilgi'),('Ribozom → Golgi cisimciği → Endoplazmik retikulum → Hücre zarı','ER ile Golgi’nin sırasını karıştırmak.','bilgi'),('Golgi cisimciği → Endoplazmik retikulum → Ribozom → Hücre zarı','Yolu sondan başa yazmak.','dikkat'),('Endoplazmik retikulum → Ribozom → Golgi cisimciği → Hücre zarı','Sentezin ribozomda başladığını unutmak.','bilgi'),('Ribozom → Endoplazmik retikulum → Golgi cisimciği → Hücre zarı',None,None)],
  ad=[A('Başlangıç','Enzimler protein yapılıdır ve ribozomda sentezlenir.','ilk: ribozom'),A('Taşınma','Sentezlenen enzim endoplazmik retikulumdan geçer ve Golgi cisimciğine ulaşır.','ER → Golgi'),A('Salgı','Golgi, enzimi paketleyip kesecikle hücre zarına gönderir; enzim dışarı verilir.','Golgi → zar'),A('Sonuç','Sıra ribozom, ER, Golgi, hücre zarıdır.','Ribozom → ER → Golgi → zar')]),
 'pankreas enzimi','hücre ve enzim değişti, şıklar baştan yazıldı')

Q(P,PRE,'0006','hc-organel-karsilastir','Mitokondri ve kloroplast karşılaştırması','orta','Organellerin yapısı','Mitokondri ve kloroplastın ortak ve ayırıcı özelliklerini değerlendirir.','öncüllü',3,
 'İki organelin ortak özelliklerinden doğru olanlar seçilir.','Fotosentezi her iki organele atfetmek.',[IKZ],
 'Mitokondri ve kloroplast: çift zar, kendi DNA’sı ve ribozomu ortak; fotosentez yalnız kloroplastta.',
 dict(m='Mitokondri ve kloroplast ile ilgili,\nI. Her ikisi de çift zarlı organeldir.\nII. Her ikisinde de fotosentez gerçekleşir.\nIII. Her ikisinde de ribozom bulunur.\nifadelerinden hangileri doğrudur?',i='Doğru ifadeler.',ip=['Her iki organelin zar sayısını hatırla.','Fotosentez hangi organelde yapılır?','Kendi DNA’sı olan organellerde protein sentezi için ne bulunur?'],
  o=[('Yalnız I','Organellerin ribozom içerdiğini bilmemek.','bilgi'),('Yalnız III','Her iki organelin de çift zarlı olduğunu bilmemek.','bilgi'),('I ve II','Fotosentezi mitokondriye de yazmak.','bilgi'),('I ve III',None,None),('II ve III','Zar sayısını atlayıp fotosentezi ortak saymak.','bilgi')],
  ad=[A('Zarlar','Mitokondri ve kloroplastın ikisi de çift zarlıdır.','I doğru'),A('Fotosentez','Fotosentez yalnızca kloroplastta yapılır; mitokondri hücresel solunum yapar.','II yanlış'),A('Ribozom','İkisi de kendine ait DNA ve ribozom taşır, kendi proteinlerinin bir kısmını yapabilir.','III doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')]),
 dict(m='Mitokondri ve kloroplast ile ilgili,\nI. Hayvan hücrelerinin hepsinde ikisi de bulunur.\nII. Her ikisinde de kendine ait ribozom bulunur.\nIII. Her ikisi de çift zarlıdır.\nifadelerinden hangileri doğrudur?',
  o=[('II ve III',None,None),('Yalnız II','Çift zarlı olma özelliğini atlamak.','bilgi'),('I ve II','Hayvan hücresinde kloroplast olmadığını unutmak.','bilgi'),('I ve III','Hayvan hücresindeki kloroplast yargısını doğru sanıp ribozomu atlamak.','bilgi'),('I, II ve III','Kloroplastın hayvan hücresinde bulunduğunu sanmak.','bilgi')],
  ad=[A('Bulunduğu hücre','Kloroplast bitki ve alg hücrelerindedir; hayvan hücresinde bulunmaz.','I yanlış'),A('Ribozom','Her iki organelin matriksinde kendi ribozomları vardır.','II doğru'),A('Zarlar','Her ikisi de dış ve iç olmak üzere iki zarla çevrilidir.','III doğru'),A('Sonuç','Doğru olanlar II ve III.','II ve III')]),
 'çift zar, ortak özellik','ifadeler ve kombinasyonlar değişti')

Q(P,PRE,'0007','hc-ozmoz-hesap','Ozmozda su geçişi hesabı','zor','Ozmoz','Yarı geçirgen zarla ayrılmış iki çözeltide derişimler eşitlenene kadar geçen su miktarını hesaplar.','yeni nesil',5,
 'Yalnız suyu geçiren zarla ayrılmış iki çözeltinin son derişimi ve hacimleri bulunur.','Son hacmi, geçen su miktarı sanmak.',[OZM,B('Yüzde derişim','100 mL’de %3 = 3 g madde · Madde miktarı değişmezse son derişim = toplam madde ÷ toplam hacim')],
 'Madde miktarı sabit, toplam hacim sabit: son derişim = toplam madde ÷ toplam hacim; geçen su = hacim farkı.',
 dict(m='U şeklindeki bir kabın ortasına yalnızca suyu geçiren yarı geçirgen bir zar konulmuştur. Sol kola %3’lük 100 mL, sağ kola %9’luk 100 mL şeker çözeltisi konuluyor. Şeker zardan geçemez; su hareketi iki koldaki derişimler eşitlenene kadar sürmektedir ve basıncın etkisi yok sayılacaktır.\nBuna göre bu süreçte sol koldan sağ kola geçen su miktarı kaç mL’dir?',
  i='Sol koldan sağ kola geçen su miktarı (mL).',ip=['Her koldaki şeker miktarını gram olarak bul.','Derişimler eşitlendiğinde toplam şeker kaç mL çözeltide bulunur?','Soldaki yeni hacmi bul; ilk hacimden farkı alırsan geçen suyu bulursun.'],
  o=[('25','Geçen su miktarını son hacim farkının yarısı sanmak.','islem'),('50',None,None),('75','Sağ koldaki son hacmin (150 mL) yarısını geçen su sanmak.','islem'),('100','Sol koldaki bütün suyun geçtiğini sanmak.','dikkat'),('150','Sağdaki son hacmi, geçen su miktarı sanmak.','dikkat')],
  ad=[A('Şeker miktarları','100 mL’de %3 için 3 g, 100 mL’de %9 için 9 g şeker vardır.','sol: 3 g · sağ: 9 g'),A('Son derişim','Toplam şeker 12 g, toplam hacim 200 mL; derişim eşitlenince her kolda aynı olur.','12 ÷ 200 = 0,06 (%6)'),A('Sol kolun son hacmi','Sol kolda 3 g şeker %6 derişimde kalmalı.','3 ÷ 0,06 = 50 mL'),A('Geçen su','Sol kol 100 mL’den 50 mL’ye inmiştir; su sağa geçmiştir.','100 − 50 = 50 mL'),A('Kontrol','Sağ kol 150 mL olur; 9 ÷ 150 = 0,06, aynı derişim.','150 mL ✓')]),
 dict(m='Yalnızca suyu geçiren yarı geçirgen bir zarla ikiye ayrılmış bir kabın sol bölmesine %5’lik 60 mL, sağ bölmesine %15’lik 60 mL tuz çözeltisi konuluyor. Tuz zardan geçemez; su hareketi iki bölmedeki derişimler eşitlenene kadar sürmektedir ve basıncın etkisi yok sayılacaktır.\nBuna göre sol bölmeden sağ bölmeye geçen su miktarı kaç mL’dir?',
  o=[('10','Geçen suyu son hacimle karıştırıp hacim farkını yanlış almak.','islem'),('15','Geçen suyu son hacim farkının yarısı sanmak.','islem'),('30',None,None),('60','Sol bölmedeki bütün suyun geçtiğini sanmak.','dikkat'),('90','Sağdaki son hacmi, geçen su miktarı sanmak.','dikkat')],
  ad=[A('Tuz miktarları','60 mL’de %5 için 3 g, 60 mL’de %15 için 9 g tuz vardır.','sol: 3 g · sağ: 9 g'),A('Son derişim','Toplam tuz 12 g, toplam hacim 120 mL.','12 ÷ 120 = 0,1 (%10)'),A('Sol bölmenin son hacmi','3 g tuz %10 derişimde 30 mL çözeltide bulunur.','3 ÷ 0,1 = 30 mL'),A('Geçen su','Sol bölme 60 mL’den 30 mL’ye inmiştir.','60 − 30 = 30 mL')]),
 'yarı geçirgen zarla ayrılmış iki çözelti','sayılar, madde ve kap değişti')
v1=(3*100/100,9*100/100); tot=sum(v1)/(100+100); assert tot==0.06 and 3/tot==50 and 100-50==50
tot2=(3+9)/120; assert tot2==0.1 and 3/tot2==30 and 60-30==30

TAB3='Üç farklı hücrede bulunan organellerin göreli miktarları tabloda verilmiştir (+++: çok, +: az).\n\nHücre | Mitokondri | Granüllü ER | Golgi | Lizozom\nX | +++ | + | + | +\nY | + | +++ | +++ | +\nZ | + | + | + | +++\n\nBu hücreler; iskelet kası hücresi, sindirim enzimi salgılayan bez hücresi ve bakteri yutan akyuvar hücresi olduğuna göre X, Y ve Z hangi hücrelerdir?'
TAB4='Üç farklı hücrede bulunan organellerin göreli miktarları tabloda verilmiştir (+++: çok, +: az).\n\nHücre | Mitokondri | Kloroplast | Granüllü ER | Golgi\nK | + | +++ | + | +\nL | +++ | – | + | +\nM | + | – | +++ | +++\n\nBu hücreler; sperm hücresi, yaprağın ışık alan fotosentez hücresi ve protein salgılayan bez hücresi olduğuna göre K, L ve M hangi hücrelerdir?'
Q(P,PRE,'0008','hc-hucre-organel','Hücre türü ve organel miktarı','zor','Organeller ve hücre işlevi','Organel miktarlarından hücrenin işlevini ve türünü çıkarır.','tablo',4,
 'Organel yoğunluğundan hücrenin ne iş yaptığı çıkarılır.','Bol organelin işlevini yanlış hücreye bağlamak.',[ORG,HUC],
 'Bol bulunan organel, hücrenin asıl işini gösterir.',
 dict(m=TAB3,i='X, Y ve Z hücrelerinin türleri.',ip=['Çok enerji harcayan hücrede hangi organel bol olur?','Protein salgılayan hücrede hangi iki organel bol bulunur?','Bakteri yutan hücre, yutulanı hangi organelle sindirir?'],
  o=[('X: Kas, Y: Akyuvar, Z: Bez','Granüllü ER ve Golgi’nin salgı işine ait olduğunu bilmemek.','bilgi'),('X: Bez, Y: Kas, Z: Akyuvar','Mitokondrinin enerji harcayan kas hücresinde bol olduğunu atlamak.','bilgi'),('X: Akyuvar, Y: Bez, Z: Kas','Lizozomu enerji organeliyle karıştırmak.','bilgi'),('X: Kas, Y: Bez, Z: Akyuvar',None,None),('X: Bez, Y: Akyuvar, Z: Kas','Üç organel görevinin hiçbirini hücre türüne bağlamamak.','dikkat')],
  ad=[A('X’i belirle','Çok mitokondri, çok enerji demektir; kas hücresi sürekli kasılır.','X: kas'),A('Y’yi belirle','Granüllü ER ve Golgi bol: protein sentezleyip paketleyip salgılayan hücre.','Y: bez hücresi'),A('Z’yi belirle','Lizozom bol: yuttuğu bakterileri sindiren hücre.','Z: akyuvar'),A('Sonuç','X kas, Y bez, Z akyuvardır.','X, Y, Z')]),
 dict(m=TAB4,i='K, L ve M hücrelerinin türleri.',
  o=[('K: Sperm, L: Bez, M: Fotosentez hücresi','Kloroplastın yalnız fotosentez hücresinde bol olduğunu atlamak.','bilgi'),('K: Fotosentez hücresi, L: Bez, M: Sperm','Mitokondrinin sperm gibi hareketli hücrede bol olduğunu bilmemek.','bilgi'),('K: Bez, L: Sperm, M: Fotosentez hücresi','Kloroplast bol olan hücreyi ışıkla beslenen hücre olarak görmemek.','dikkat'),('K: Sperm, L: Fotosentez hücresi, M: Bez','Kloroplast bol hücreyi spermle karıştırmak.','bilgi'),('K: Fotosentez hücresi, L: Sperm, M: Bez',None,None)],
  ad=[A('K’yi belirle','Kloroplast yalnız K’de bol: ışıkla besin üreten hücre.','K: fotosentez hücresi'),A('L’yi belirle','Çok mitokondri: hareket için çok ATP gereken sperm hücresi.','L: sperm'),A('M’yi belirle','Granüllü ER ve Golgi bol: protein salgılayan bez hücresi.','M: bez hücresi'),A('Sonuç','K fotosentez hücresi, L sperm, M bez hücresidir.','K, L, M')]),
 'organel yoğunluğu tablosu','farklı hücre türleri ve organeller')
bitir(P,'hucre','Hücre ve Organeller – Madde Geçişleri','bio|Hücre ve Organeller – Madde Geçişleri',8)
