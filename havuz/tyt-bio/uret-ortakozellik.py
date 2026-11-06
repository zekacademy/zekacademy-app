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
P=Parti('ortakozellik','Canlıların Ortak Özellikleri','bio|Canlıların Ortak Özellikleri',ders='TYT Biyoloji',idon='tytbio')
PRE='BOR'
OZ=B('Canlıların ortak özellikleri','Metabolizma (madde alışverişi) · Homeostasi (iç dengeyi koruma) · Uyarılara tepki verme · Üreme · Büyüme ve gelişme · Adaptasyon (çevreye uyum) · Hücresel organizasyon')
MET=B('Anabolizma ve katabolizma','Anabolizma: küçük moleküllerden büyük molekül sentezi, enerji harcar (fotosentez, protein sentezi, kemosentez) · Katabolizma: büyük molekülün parçalanması, enerji açığa çıkarır (hücresel solunum, hidroliz)')
UR=B('Bakteride üreme','Bakteriler ikiye bölünerek çoğalır: her bölünmede sayı iki katına çıkar · n bölünme sonunda sayı = başlangıç × 2 üzeri n')
Q(P,PRE,'0001','oz-eslestir','Özellik–örnek eşleştirmesi','kolay','Ortak özellikler','Günlük örneği canlıların ortak özelliğiyle eşleştirir.','düz',2,
 'Verilen örnek hangi ortak özelliğe girer.','Uyarılara tepkiyi büyüme-gelişmeyle karıştırmak.',[OZ],
 'Örneğe bak: tepki mi, denge mi, çoğalma mı, uyum mu?',
 dict(m='Dokunulduğunda yapraklarını kapatan bir mimoza bitkisi, canlıların aşağıdaki ortak özelliklerinden hangisini gösterir?',i='Örneğin gösterdiği ortak özellik.',ip=['Yaprakların kapanması bir dış etkiye karşı verilen nedir?','Bu olay çoğalma ile ilgili midir?','Dokunma bir uyarıdır; bitki ona ne yapıyor?'],
  o=[('Üreme','Yaprak kapanmasını çoğalma sanmak.','bilgi'),('Homeostasi','Olayı iç denge ile karıştırmak.','bilgi'),('Uyarılara tepki verme',None,None),('Büyüme ve gelişme','Yaprak hareketini büyüme sanmak.','bilgi'),('Metabolizma','Olayı madde alışverişi sanmak.','bilgi')],
  ad=[A('Olayı çöz','Dokunma bir dış etkidir, bitki yapraklarını kapatarak karşılık verir.','uyarı → tepki'),A('Özellikleri ele','Üreme, büyüme, metabolizma ve homeostasi bu olayı açıklamaz.','4 özellik elenir'),A('Sonuç','Örnek uyarılara tepki vermedir.','Uyarılara tepki verme')]),
 dict(m='Sıcak bir günde terleyerek vücut sıcaklığını yaklaşık 37 °C’de tutan bir insan, canlıların aşağıdaki ortak özelliklerinden hangisini gösterir?',
  o=[('Homeostasi',None,None),('Üreme','Terlemeyi çoğalma ile ilişkilendirmek.','bilgi'),('Adaptasyon','İç dengeyi uzun vadeli çevreye uyumla karıştırmak.','bilgi'),('Büyüme ve gelişme','Olayı büyümeyle karıştırmak.','bilgi'),('Uyarılara tepki verme','Sıcaklığı uyarı sanıp denge özelliğini atlamak.','dikkat')],
  ad=[A('Olayı çöz','Vücut sıcaklığı dış sıcaklıktan bağımsız olarak sabit tutuluyor.','sabit iç ortam'),A('Özelliği seç','İç ortamın dengede tutulmasına homeostasi denir.','homeostasi'),A('Sonuç','Örnek homeostasidir.','Homeostasi')]),
 'uyarılara tepki örneği','homeostasi örneği ve şıklar değişti')
Q(P,PRE,'0002','oz-metabolizma','Anabolizma ve katabolizma','orta','Metabolizma','Tepkimeleri anabolik ve katabolik olarak sınıflandırır.','öncüllü',3,
 'Üç tepkimenin anabolik ya da katabolik olduğu sınanır.','Fotosentez ile solunumu birbirine karıştırmak.',[MET],
 'Birleştirme (sentez) = anabolizma; parçalama = katabolizma.',
 dict(m='Metabolizmayla ilgili,\nI. Fotosentez bir anabolik tepkimedir.\nII. Hücresel solunum bir katabolik tepkimedir.\nIII. Protein sentezi bir katabolik tepkimedir.\nifadelerinden hangileri doğrudur?',i='Doğru olan ifadeler.',ip=['Anabolik tepkime küçük molekülleri ne yapar?','Solunumda glikoza ne olur?','Protein sentezinde amino asitler ne yapar?'],
  o=[('Yalnız I','Hücresel solunumun katabolik olduğunu atlamak.','bilgi'),('Yalnız III','Protein sentezini katabolik sanmak.','bilgi'),('II ve III','Fotosentezi atlayıp protein sentezini katabolik saymak.','bilgi'),('I, II ve III','Protein sentezinin anabolik olduğunu unutmak.','bilgi'),('I ve II',None,None)],
  ad=[A('I. ifade','Fotosentezde CO2 ve sudan glikoz yapılır: sentez, anabolik.','I doğru'),A('II. ifade','Solunumda glikoz parçalanıp enerji açığa çıkar: katabolik.','II doğru'),A('III. ifade','Protein sentezinde amino asitler birleşir: anabolik.','III yanlış'),A('Sonuç','Doğru olanlar I ve II.','I ve II')]),
 dict(m='Metabolizmayla ilgili,\nI. Hidroliz bir anabolik tepkimedir.\nII. Protein sentezi bir anabolik tepkimedir.\nIII. Kemosentez bir anabolik tepkimedir.\nifadelerinden hangileri doğrudur?',
  o=[('I ve II','Hidrolizi anabolik sanmak.','bilgi'),('II ve III',None,None),('Yalnız II','Kemosentezin de organik madde sentezi olduğunu atlamak.','bilgi'),('I ve III','Protein sentezini atlayıp hidrolizi anabolik saymak.','bilgi'),('I, II ve III','Hidrolizin parçalama olduğunu unutmak.','bilgi')],
  ad=[A('I. ifade','Hidroliz suyla parçalamadır: katabolik.','I yanlış'),A('II. ifade','Protein sentezi amino asitleri birleştirir: anabolik.','II doğru'),A('III. ifade','Kemosentez inorganik maddelerden organik madde yapar: anabolik.','III doğru'),A('Sonuç','Doğru olanlar II ve III.','II ve III')]),
 'fotosentez/solunum/protein','hidroliz, protein sentezi ve kemosentez')
Q(P,PRE,'0003','oz-durum','Durum–özellik eşleştirmesi','orta','Ortak özellikler','Üç ayrı örneği ortak özelliklerle eşleştirir.','tablo',3,
 'Üç örnek ve üç özellik birlikte eşleştirilir.','Adaptasyon ile homeostasiyi karıştırmak.',[OZ],
 'Kısa sürede iç denge → homeostasi; kalıtsal uyum → adaptasyon.',
 dict(m='Üç örnek aşağıda verilmiştir:\nX: Çöl bitkisinin yapraklarının su kaybını azaltmak için dikene dönüşmüş olması\nY: Kandaki glikoz düzeyinin yaklaşık sabit tutulması\nZ: Bir tohumun çimlenip fidana dönüşmesi\nBuna göre X, Y ve Z örnekleri canlıların hangi ortak özelliklerine örnektir?',i='X, Y ve Z’nin ait olduğu özellikler.',ip=['Çevreye uzun süreli uyum hangi özelliktir?','Kan glikozunun sabit kalması neyi gösterir?','Tohumdan fidana dönüşme neyle ilgilidir?'],
  o=[('X: Homeostasi, Y: Adaptasyon, Z: Büyüme ve gelişme','X ile Y’yi karıştırmak.','bilgi'),('X: Adaptasyon, Y: Homeostasi, Z: Büyüme ve gelişme',None,None),('X: Adaptasyon, Y: Büyüme ve gelişme, Z: Homeostasi','Y ile Z’yi karıştırmak.','bilgi'),('X: Uyarılara tepki, Y: Homeostasi, Z: Üreme','X’i uyarı, Z’yi çoğalma sanmak.','bilgi'),('X: Büyüme ve gelişme, Y: Adaptasyon, Z: Homeostasi','Üçünü de karıştırmak.','bilgi')],
  ad=[A('X','Dikene dönüşmüş yapraklar çevreye uyumdur.','X: adaptasyon'),A('Y','Kan glikozunun dengede tutulması iç ortamın korunmasıdır.','Y: homeostasi'),A('Z','Çimlenme ve fidan oluşumu büyüme ve gelişmedir.','Z: büyüme ve gelişme'),A('Sonuç','Doğru sıra ikinci şıktadır.','X, Y, Z')]),
 dict(m='Üç örnek aşağıda verilmiştir:\nK: Devenin hörgücünde yağ depolaması\nL: Bakterinin ikiye bölünmesi\nM: Tavşanın tehlike anında kaçması\nBuna göre K, L ve M örnekleri canlıların hangi ortak özelliklerine örnektir?',
  o=[('K: Adaptasyon, L: Üreme, M: Uyarılara tepki verme',None,None),('K: Homeostasi, L: Üreme, M: Adaptasyon','K ile M’yi karıştırmak.','bilgi'),('K: Adaptasyon, L: Büyüme ve gelişme, M: Homeostasi','Bölünmeyi büyüme sanmak.','bilgi'),('K: Uyarılara tepki, L: Üreme, M: Adaptasyon','K ile M’yi ters yazmak.','bilgi'),('K: Metabolizma, L: Homeostasi, M: Uyarılara tepki','L’yi iç denge sanmak.','bilgi')],
  ad=[A('K','Hörgüçte yağ depolama çölde yaşamaya uyumdur.','K: adaptasyon'),A('L','İkiye bölünerek sayı artar.','L: üreme'),A('M','Tehlike bir uyarıdır, tavşan kaçarak tepki verir.','M: uyarılara tepki'),A('Sonuç','Doğru sıra birinci şıktadır.','K, L, M')]),
 'çöl bitkisi/glikoz/çimlenme','deve/bakteri/tavşan')
assert 3*2**6==192 and 5*2**6==320
Q(P,PRE,'0004','oz-bakteri','Bakterilerde çoğalma hesabı','zor','Üreme','Bölünme süresi ve toplam süreden bakteri sayısını hesaplar.','yeni nesil',4,
 'Başlangıç sayısı ve bölünme süresinden toplam bakteri sayısı bulunur.','Bölünme sayısını yanlış bulmak ya da başlangıç sayısını çarpmamak.',[UR],
 'Önce toplam bölünme sayısını bul; sayı her bölünmede iki katına çıkar.',
 dict(m='Uygun koşullarda her 30 dakikada bir ikiye bölünen bir bakteri türünden başlangıçta 3 hücre vardır. Hiçbir bakteri ölmemektedir.\nBuna göre 3 saat sonunda toplam bakteri sayısı kaç olur?',i='3 saat sonundaki bakteri sayısı.',ip=['3 saatte kaç kez bölünme olur?','Her bölünme sayıyı kaç katına çıkarır?','Başlangıçtaki 3 hücreyi unutma.'],
  o=[('18','Bölünme sayısıyla başlangıcı çarpmak.','islem'),('64','Başlangıç sayısını hesaba katmamak.','dikkat'),('96','Bir bölünme eksik saymak.','islem'),('192',None,None),('384','Bir bölünme fazla saymak.','islem')],
  ad=[A('Bölünme sayısı','3 saat = 180 dakika; 180 ÷ 30 = 6 bölünme.','6 bölünme'),A('Katlanma','Her bölünmede sayı iki katına çıkar.','2 üzeri 6 = 64'),A('Başlangıç sayısı','Başlangıçtaki 3 hücrenin her biri 64 hücre verir.','3 × 64'),A('Sonuç','Toplam bakteri sayısı.','192')]),
 dict(m='Uygun koşullarda her 20 dakikada bir ikiye bölünen bir bakteri türünden başlangıçta 5 hücre vardır. Hiçbir bakteri ölmemektedir.\nBuna göre 2 saat sonunda toplam bakteri sayısı kaç olur?',
  o=[('30','Bölünme sayısıyla başlangıcı çarpmak.','islem'),('160','Bir bölünme eksik saymak.','islem'),('320',None,None),('640','Bir bölünme fazla saymak.','islem'),('1280','İki bölünme fazla saymak.','islem')],
  ad=[A('Bölünme sayısı','2 saat = 120 dakika; 120 ÷ 20 = 6 bölünme.','6 bölünme'),A('Katlanma','Her bölünmede sayı iki katına çıkar.','2 üzeri 6 = 64'),A('Başlangıç sayısı','Başlangıçtaki 5 hücrenin her biri 64 hücre verir.','5 × 64'),A('Sonuç','Toplam bakteri sayısı.','320')]),
 'bakteri bölünmesi','süre ve sayılar değişti')
bitir(P,'ortakozellik','Canlıların Ortak Özellikleri','bio|Canlıların Ortak Özellikleri',4)
