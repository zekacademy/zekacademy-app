"""TYT Biyoloji · Kalıtım · 3. paket (kalitimuc): 10 soru, kardeş yok, ipucu 1.
Soyağacı genotipleri (tara), kan grubu, dihibrit ve eşeye bağlı olasılıklar Python'da taranır; her şık ve çeldirici değeri assert edilir.
Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır; anahtar, adım ve çeldirici açıklamaları oradan üretilir."""
import sys,os,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_bio as H
from _hafif_bio3 import *
KONU_='Kalıtım'; UK='bio|Kalıtım'; H.KONU=KONU_
P=Parti('kalitimuc',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji (yalnız mantık) · MEB 10. sınıf Kalıtım'
TIP={'abo':('by-kl3-abo','Kan grupları ve ABO kalıtımı'),'soy':('by-kl3-soyagaci','Soyağacından kalıtım biçimi ve genotip'),
     'soyo':('by-kl3-soyagaci-olasilik','Soyağacında olasılık hesabı'),'dihib':('by-kl3-dihibrit','Dihibrit çaprazlama ve olasılık'),
     'capraz':('by-kl3-capraz-tablo','Çaprazlama sonuç tablosundan genotip çıkarma'),'ese':('by-kl3-eseye','Eşeye bağlı kalıtım')}
def kartla(n,tip,alt,fikir,tuzak,z,kalip,adim):
    kart(f'K-BYKL3-{n}',alt,fikir,tuzak,z,kalip,adim,TIP[tip][0],TIP[tip][1],KY)
def q(no,tip,ad,ne,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[tip][0],tip=TIP[tip][1],kart=f"K-BYKL3-{no[-2:]} ({TIP[tip][1].lower()}) · {ne}",**k)
H_=lambda *a:None
def F(a,b=1): return Fr(a,b)
def fr(x): x=Fr(x); return f'{x.numerator}/{x.denominator}' if x.denominator!=1 else str(x.numerator)

# ============ 0001 · ABO · kolay · öncüllü · tablo ============
kartla('01','abo','ABO – çocuklardan ebeveyn genotipi','Çocukların kan grubu kümesinden (A, B, AB, O hepsi) ebeveynlerin taşıdığı alel kümesi çıkarılır: AB çocuk için bir ebeveynde A, diğerinde B; O çocuk için ikisinde de O aleli gerekir.','AB çocuğu olan ailede ebeveynlerden birinin AB olması gerektiğini sanmak; ebeveynleri homozigot varsaymak.','kolay','öncüllü',4)
GEN=['AA','AO','BB','BO','AB','OO']
def grup(g): return 'AB' if set(g)=={'A','B'} else ('A' if 'A' in g else ('B' if 'B' in g else 'O'))
def yavru(a,b): return {grup(x+y) for x in a for y in b}
gecerli=[(a,b) for a,b in itertools.combinations_with_replacement(GEN,2) if yavru(a,b)>={'A','B','AB','O'}]
assert gecerli==[('AO','BO')]
oran={g:Fr(sum(grup(x+y)==g for x in 'AO' for y in 'BO'),4) for g in ['A','B','AB','O']}; assert oran['AB']==F(1,4)
d1={'I':(True,'AB çocuk için bir ebeveynde A, diğerinde B aleli; O çocuk için de ikisinde O aleli gerekir. Bu yalnız AO × BO çiftinde olur, yani biri A diğeri B grubundadır.'),
    'II':(True,'O kan grubundaki çocuk her ebeveynden bir O aleli almıştır; ebeveynler A ve B grubu olduklarından AO ve BO, yani heterozigottur.'),
    'III':(False,'AO × BO çaprazında A, B, AB ve O çocukların her biri 1/4 olasılıklıdır; AB olasılığı 1/2 değil 1/4’tür.')}
r=onc(d1,True,'D')
q('0001','abo',[adim_onc(d1,'I'),adim_onc(d1,'II'),adim_onc(d1,'III'),sonuc(r,True)],'dört çocuğun kan grupları tablosu',z='kolay',alt='Kan Grupları',
 kaz='Çocukların kan grupları tablosundan ebeveyn genotiplerini belirler ve sonraki çocuk için olasılık yorumlar.',kalip='öncüllü',
 metin='Bir ailenin dört çocuğunun cinsiyeti ve ABO kan grupları aşağıdaki tabloda verilmiştir. Ebeveynlerin kan grupları bilinmemektedir; ABO kan grubu tek gen yerindeki üç alelle (A, B, O) belirlenir ve mutasyon gerçekleşmemiştir.\nBuna göre,\nI. Ebeveynlerden biri A, diğeri B kan grubundandır.\nII. Ebeveynlerin ikisi de heterozigot genotiptedir.\nIII. Çiftin beşinci çocuğunun AB kan grubundan olma olasılığı 1/2’dir.\nyargılarından hangileri doğrudur?',
 sekil=tablo_svg(['Çocuk','Cinsiyet','Kan grubu'],[['1. çocuk','Kız','A'],['2. çocuk','Erkek','B'],['3. çocuk','Kız','AB'],['4. çocuk','Erkek','O']]),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',
 ip=['AB ve O kan grubundaki çocukların her birinin ebeveynlerinden hangi alelleri almış olması gerektiğini düşün.'],
 bilgi=[B('ABO alelleri','A ve B aleli O aleline baskındır, A ile B birbirine eş baskındır · A grubu AA ya da AO, B grubu BB ya da BO, AB grubu AB, O grubu OO genotiplidir · Her çocuk ebeveynlerinden birer alel alır')],
 puf='AB ve O çocuk aynı ailedeyse ebeveynler AO ve BO’dur; çocuğun kan grubundaki her alel ebeveynlerden birinden gelmelidir.')

# ============ 0002 · AD soyağacı · kolay · olumsuz ============
kartla('02','soy','Soyağacı – otozomal baskın','Hasta ebeveynlerin sağlıklı çocuğu otozomal çekinik ve eşeye bağlı kalıtımları dışlar; baskın kalıtımda sağlıklı bireyler çekinik homozigottur, hasta bireylerin genotipi çocuk ve ebeveynlerinden çıkarılır.','Hasta bireylerin hepsini homozigot saymak; çocuğu sağlıklı olan hasta ebeveynin heterozigot olacağını gözden kaçırmak.','kolay','şekilli',4)
K2={'I-1':('E',1,None,None),'I-2':('K',1,None,None),'II-1':('K',0,'I-2','I-1'),'II-2':('K',1,'I-2','I-1'),'II-3':('E',1,'I-2','I-1'),'II-4':('K',0,None,None),
    'III-1':('E',1,'II-4','II-3'),'III-2':('K',0,'II-4','II-3'),'III-3':('E',0,'II-4','II-3')}
gecer={m:bool(tara(K2,m)) for m in ('AR','AD','XR','XD')}; assert gecer=={'AR':False,'AD':True,'XR':False,'XD':False}
W2=tara(K2,'AD')
kes2=lambda f:all(f(w) for w in W2); yok2=lambda f:not any(f(w) for w in W2)
Y_={'I-1':(.85,4.4),'I-2':(2.55,4.4),'II-1':(0,2.4),'II-2':(1.7,2.4),'II-3':(3.4,2.4),'II-4':(5.1,2.4),'III-1':(3.15,.4),'III-2':(4.25,.4),'III-3':(5.35,.4)}
SK2=tk(pedciz(K2,Y_,[('I-1','I-2',['II-1','II-2','II-3'],3.4),('II-3','II-4',['III-1','III-2','III-3'],1.4)]),1.0)
assert kes2(lambda w:w['I-1']==1 and w['I-2']==1) and kes2(lambda w:w['III-1']==1) and kes2(lambda w:w['III-2']==0 and w['III-3']==0)
assert kes2(lambda w:w['II-1']==w['II-4']==0) and yok2(lambda w:w['II-3']==2)
S0='II-3 bireyi homozigot baskın genotiptedir.'
S1='Hastalık otozomal baskın alelle belirlenir.'; S2='I-1 ve I-2 bireylerinin ikisi de heterozigot genotiptedir.'
S3='III-1 bireyi heterozigot genotiptedir.'; S4='II-1 ve II-4 bireyleri aynı genotiptedir.'
q('0002','soy',[A('Kalıtım biçimini bul','Hasta I-1 ile I-2’nin sağlıklı kızı II-1 var; bu, hastalığın çekinik olmadığını ve hasta babanın kızı sağlıklı olduğu için eşeye bağlı olmadığını gösterir.','Otozomal baskın'),
   A('Sağlıklı bireylerin genotipini yaz','Baskın kalıtımda sağlıklı bireyler çekinik homozigottur.','II-1, II-4, III-2, III-3 = aa'),
   A('Hasta bireyleri çöz','Hasta I-1, I-2 ve II-3 sağlıklı çocuk verdiği için Aa’dır; Aa × aa çaprazının hasta çocuğu III-1 de Aa’dır.','I-1, I-2, II-3, III-1 = Aa'),
   A('Yargıları karşılaştır','II-3 heterozigot olduğundan “homozigot baskın” demek yanlıştır; diğer ifadeler bu genotiplerle uyuşur.','Yanlış ifade: II-3 homozigot baskındır')],
 'üç kuşak, hasta ebeveynlerin sağlıklı çocuğu',z='kolay',alt='Soyağacı',kaz='Soyağacından kalıtım biçimini belirler ve bireylerin genotipini yorumlar.',kalip='şekilli',
 metin='Şekilde, tek bir gen çiftiyle belirlenen ve otozomal ya da eşeye bağlı kalıtıma sahip olabilen bir hastalığın üç kuşaklık soyağacı verilmiştir. Dolu semboller hastalığı gösteren, boş semboller göstermeyen bireyleri; kareler erkekleri, daireler kadınları simgelemektedir. Bireyler kuşak ve soldan sağa sıra numarasıyla anılır (II-2, ikinci kuşaktaki ikinci bireydir). Mutasyon gerçekleşmemiştir.\nBuna göre, aşağıdakilerden hangisi yanlıştır?',
 sekil=SK2,dogru=S0,sira=yer('A',S0,[S1,S2,S3,S4]),
 yan=[(S1,'Hasta ebeveynlerin (I-1, I-2) sağlıklı kızı vardır; bu yalnız baskın kalıtımda olur. İfade doğrudur, “hasta çocuğu yok = çekinik” gibi düşünülerek yanlış sanılmış.','bilgi'),
      (S2,'Sağlıklı kızları II-1 (aa) olduğuna göre iki ebeveyn de a aleli taşır; hasta oldukları için Aa’dır. İfade doğrudur.','dikkat'),
      (S3,'III-1’in annesi II-4 aa’dır; hasta olduğuna göre baskın aleli babadan almıştır ve Aa’dır. İfade doğrudur; “hasta = homozigot” sanılmış.','bilgi'),
      (S4,'II-1 ve II-4 sağlıklıdır; baskın kalıtımda ikisi de aa’dır. İfade doğrudur.','dikkat')],
 istenen='Soyağacına göre yanlış olan ifade.',
 ip=['Önce hasta ve sağlıklı ebeveynlerin çocuklarına bakarak kalıtım biçimini belirle, sonra her ifadeyi bu biçime göre sına.'],
 bilgi=[B('Soyağacında kalıtım biçimi','Sağlıklı ebeveynlerin hasta çocuğu varsa hastalık çekiniktir · Hasta ebeveynlerin sağlıklı çocuğu varsa hastalık baskındır ve ebeveynler heterozigottur · Eşeye bağlı çekinikte hasta kızın babası da hastadır'),
        B('Genotip yazımı','Çekinik özelliği gösteren birey aa, baskın özelliği gösteren birey AA ya da Aa’dır · Baskın özellikte sağlıklı bireyin aa olduğu kesindir')],
 puf='Hasta ebeveynlerden sağlıklı çocuk doğuyorsa hastalık baskındır ve iki ebeveyn de heterozigottur.')

# ============ 0003 · AR soyağacı · orta · öncüllü ============
kartla('03','soy','Soyağacı – kesin ve belirsiz genotipler','Otozomal çekinik soyağacında genotipi kesinleşenler (hasta, hasta çocuğu olan sağlıklı) ile belirsiz kalanlar (yalnız sağlıklı çocuğu olan ya da sağlıklı kardeşi hastaya sahip bireyler) ayrılır; “kesin” için tüm olası genotipler taranır.','Sağlıklı bireyi homozigot baskın sanmak; “taşıyıcı olabilir” ile “taşıyıcıdır” ayrımını yapmamak.','orta','öncüllü',4)
K3={'I-1':('E',0,None,None),'I-2':('K',0,None,None),'II-1':('E',0,'I-2','I-1'),'II-2':('K',1,'I-2','I-1'),'II-3':('E',0,'I-2','I-1'),'II-4':('K',0,None,None),
    'III-1':('K',0,'II-4','II-3'),'III-2':('E',1,'II-4','II-3')}
assert [m for m in ('AR','AD','XR','XD') if tara(K3,m)]==['AR','XR'] or tara(K3,'AR')
W3=tara(K3,'AR'); kes=lambda w3,a:{w[a] for w in w3}
assert kes(W3,'I-1')=={1} and kes(W3,'I-2')=={1} and kes(W3,'II-3')=={1} and kes(W3,'II-4')=={1}
assert kes(W3,'II-1')=={0,1} and kes(W3,'III-1')=={0,1} and kes(W3,'II-2')=={2} and kes(W3,'III-2')=={2}
Y3={'I-1':(.85,4.4),'I-2':(2.55,4.4),'II-1':(0,2.4),'II-2':(1.7,2.4),'II-3':(3.4,2.4),'II-4':(5.1,2.4),'III-1':(3.4,.4),'III-2':(5.1,.4)}
SK3=tk(pedciz(K3,Y3,[('I-1','I-2',['II-1','II-2','II-3'],3.4),('II-3','II-4',['III-1','III-2'],1.4)]),1.0)
d3={'I':(True,'II-3 ile II-4’ün hasta çocuğu III-2 vardır; hastanın iki aleli de çekiniktir ve her biri bir ebeveynden gelir. Sağlıklı oldukları için ikisi de Aa’dır.'),
    'II':(False,'II-1’in ebeveynleri Aa × Aa’dır; II-1 sağlıklıdır ve AA (1/3) ya da Aa (2/3) olabilir. Heterozigot olduğu kesin değildir.'),
    'III':(True,'Hasta kızları II-2 olduğundan I-1 ve I-2’nin ikisi de çekinik alel taşır; sağlıklı oldukları için ikisi de Aa’dır, aynı genotiptedirler.')}
assert d3['I'][0]==all(w['II-3']==1 and w['II-4']==1 for w in W3) and d3['II'][0]==all(w['II-1']==1 for w in W3) and d3['III'][0]==all(w['I-1']==w['I-2'] for w in W3)
r=onc(d3,True,'D')
q('0003','soy',[A('Kesin genotipleri yaz','Hasta çocuğu olan sağlıklı ebeveynler heterozigottur: I-1, I-2, II-3 ve II-4 için Aa.','I-1 = I-2 = II-3 = II-4 = Aa'),
    A('Belirsiz bireyleri ayır','Ebeveynleri taşıyıcı olan sağlıklı II-1 ve III-1, AA ya da Aa olabilir.','II-1 ve III-1: AA veya Aa'),
    adim_onc(d3,'I'),adim_onc(d3,'II'),adim_onc(d3,'III'),sonuc(r,True)],
 'iki sağlıklı ebeveynin hasta çocuğu, genotip taraması',z='orta',alt='Soyağacı',kaz='Otozomal çekinik soyağacında genotipi kesin olan bireyleri belirler.',kalip='öncüllü',
 metin='Şekilde, otozomal çekinik tek bir gen çiftiyle belirlenen bir hastalığın üç kuşaklık soyağacı verilmiştir. Dolu semboller hasta, boş semboller sağlıklı bireyleri; kareler erkekleri, daireler kadınları göstermektedir. Bireyler kuşak ve soldan sağa sıra numarasıyla anılır; II-4 ailenin dışından evlenmiştir.\nBuna göre,\nI. II-3 ve II-4 bireylerinin ikisi de heterozigot genotiptedir.\nII. II-1 bireyi heterozigot genotiptedir.\nIII. I-1 ve I-2 bireyleri aynı genotiptedir.\nyargılarından hangileri kesinlikle doğrudur?',
 sekil=SK3,dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Soyağacına göre kesinlikle doğru olan yargılar.',
 ip=['Hangi bireylerin genotipinin ebeveyn ya da çocuklarından mutlaka çıkarılabildiğini, hangilerinin iki olasılık taşıdığını ayır.'],
 bilgi=[B('Genotip belirleme','Hasta birey aa’dır · Sağlıklı ebeveynlerin hasta çocuğu varsa ebeveynlerin ikisi de Aa’dır · Aa × Aa çaprazındaki sağlıklı çocuk AA ya da Aa olabilir, hangisi olduğu başka bilgi yoksa kesin değildir')],
 puf='Kesinlik yalnız hasta çocuğu olan ebeveynlerde vardır; yalnız sağlıklı çocuğu ya da sağlıklı ebeveyni olan bireylerde “AA veya Aa” belirsizliği kalır.')

# ============ 0004 · XR soyağacı olasılık · zor ============
kartla('04','soyo','Eşeye bağlı soyağacında olasılık','Sağlıklı annenin hasta oğlu varsa anne taşıyıcıdır; taşıyıcı annenin sağlıklı kızı 1/2 olasılıkla taşıyıcıdır. Hasta çocuk olasılığı taşıyıcılık olasılığı, çocuğun cinsiyeti ve aldığı X kromozomu olasılıklarının çarpımıdır.','Kızı kesin taşıyıcı saymak; taşıyıcılık olasılığını iki kez ya da hiç çarpmamak; otozomal çekinik gibi 2/3 almak.','zor','şekilli',5)
K4={'I-1':('E',0,None,None),'I-2':('K',0,None,None),'II-1':('E',0,None,None),'II-2':('K',0,'I-2','I-1'),'II-3':('E',1,'I-2','I-1'),'II-4':('E',0,'I-2','I-1'),
    'III-1':('E',1,'II-2','II-1'),'III-2':('K',0,'II-2','II-1')}
W4=tara(K4,'XR'); assert W4 and {w['I-2'] for w in W4}=={1} and {w['II-2'] for w in W4}=={1} and {w['III-2'] for w in W4}=={0,1}
Y4={'I-1':(2.55,4.4),'I-2':(4.25,4.4),'II-1':(0,2.4),'II-2':(1.7,2.4),'II-3':(3.4,2.4),'II-4':(5.1,2.4),'III-1':(0,.4),'III-2':(1.7,.4)}
SK4=tk(pedciz(K4,Y4,[('I-1','I-2',['II-2','II-3','II-4'],3.4),('II-1','II-2',['III-1','III-2'],1.4)]),1.0)
# III-2 taşıyıcı olasılığı ve ilk çocuğun hasta olma olasılığı: gametleri say
anne={'XR':Fr(1,2),'Xr':Fr(1,2)}   # III-2: babadan XR, anneden (II-2 taşıyıcı) XR ya da Xr
p_tas=anne['Xr']; assert p_tas==F(1,2)
hasta=Fr(0)
for g,pg in anne.items():            # III-2 genotipi (XR,g)
    for gam,pm in (('XR',Fr(1,2)),(g,Fr(1,2))):    # III-2'nin gameti
        for cins,pc in (('K',Fr(1,2)),('E',Fr(1,2))):
            if cins=='E' and gam=='Xr': hasta+=pg*pm*pc
assert hasta==F(1,8)
assert F(1,2)*F(1,2)*F(1,2)*F(1,2)==F(1,16) and F(2,3)*F(1,4)==F(1,6) and F(1,4)==F(1,4)
dg,yn,sr=kesirler(F(1,8),[(F(1,16),'III-2’nin taşıyıcı olma olasılığını (1/2) iki kez hesaba katmış: 1/2 × 1/2 × 1/2 × 1/2.','dikkat'),
  (F(1,6),'Hastalığı otozomal çekinik sanıp sağlıklı III-2’nin taşıyıcı olma olasılığını 2/3 almış: 2/3 × 1/4.','bilgi'),
  (F(1,4),'III-2’yi kesin taşıyıcı saymış: taşıyıcı annenin hasta çocuk olasılığı 1/4, ama III-2’nin taşıyıcılığı yalnızca 1/2 olasılıklıdır.','dikkat'),
  (F(1,2),'Cinsiyet olasılığını hesaba katmamış; taşıyıcı annenin her çocuğunun yarısının hasta olacağını sanmış.','bilgi')])
q('0004','soyo',[A('Kalıtım biçimini kullan','Hastalık X’e bağlı çekiniktir; erkekte tek çekinik alel hastalık yapar, kızın hasta olması için iki çekinik alel gerekir.','Erkek: XrY hasta · Kız: XrXr hasta'),
   A('II-2’nin genotipini bul','II-2 sağlıklı olduğu halde hasta oğlu III-1’i vardır; oğlu Xr’yi yalnız annesinden alabilir.','II-2 = XRXr (kesin taşıyıcı)'),
   A('III-2’nin taşıyıcılığını hesapla','III-2, babası II-1’den XR alır; annesinden XR ya da Xr alması eşit olasılıklıdır.','P(taşıyıcı) = 1/2'),
   A('Çocuğun hasta olma olasılığı','Taşıyıcı anne ile sağlıklı babanın hasta çocuğu yalnız erkek (1/2) ve Xr almış (1/2) olabilir.','1/2 × 1/2 = 1/4'),
   A('Olasılıkları çarp','Önce III-2’nin taşıyıcı olması gerekir.','1/2 × 1/4 = 1/8')],
 'X’e bağlı çekinik, III-2 taşıyıcılık olasılığı',z='zor',alt='Soyağacı',kaz='Eşeye bağlı soyağacında taşıyıcılık olasılığını bulup çocuğun hasta olma olasılığını hesaplar.',kalip='şekilli',
 metin='Şekilde, X kromozomu üzerindeki çekinik bir alelle belirlenen ve Y kromozomunda karşılığı bulunmayan bir hastalığın üç kuşaklık soyağacı verilmiştir. Dolu semboller hasta, boş semboller sağlıklı bireyleri; kareler erkekleri, daireler kadınları göstermektedir. Bireyler kuşak ve soldan sağa sıra numarasıyla anılır; II-1 ailenin dışından evlenmiştir. Mutasyon gerçekleşmemiştir.\nIII-2 bireyi, ailesinde bu hastalık öyküsü bulunmayan sağlıklı bir erkekle evleniyor.\nBuna göre, bu çiftin ilk çocuğunun hasta olma olasılığı kaçtır?',
 sekil=SK4,dogru=dg,yan=yn,sira=sr,istenen='Çiftin ilk çocuğunun hasta olma olasılığı.',
 ip=['III-2’nin taşıyıcı olma olasılığını ayrı hesapla; sonra taşıyıcı bir annenin ve sağlıklı bir babanın çocuğunda hastalığın görülme olasılığını bul.'],
 bilgi=[B('Eşeye bağlı çekinik kalıtım','Erkeğin tek X’i vardır, çekinik alel taşıyorsa hastadır · Taşıyıcı anne (XRXr) ile sağlıklı baba (XRY) çaprazında yalnız erkek çocuklar hasta olabilir · Birbirini izleyen bağımsız olayların olasılıkları çarpılır')],
 puf='Önce “anne taşıyıcı mı, olasılığı nedir?” sorusunu çöz, sonra taşıyıcı anne için çocuk olasılığını (1/4) bununla çarp.')

# ============ 0005 · dihibrit olumsuz · orta ============
kartla('05','dihib','Dihibrit çaprazda görülmeyen genotip/fenotip','Her gen çifti ayrı çaprazlanır; ebeveynlerden biri bir gen yeri bakımından homozigot baskınsa çekinik fenotip hiç görülmez. Görülemeyen sınıf tüm gamet birleşimleri taranarak bulunur.','Dihibriti 9:3:3:1 sanmak; homozigot baskın ebeveynin çekinik alel aktaramayacağını unutmak.','orta','hikâyeli',4)
def gam(g): return [x+y for x in g[0] for y in g[1]]
def capraz(p1,p2):
    c={}
    for a in gam(p1):
        for b in gam(p2):
            g=''.join(sorted(a[0]+b[0],key=lambda x:x.isupper() is False))+''.join(sorted(a[1]+b[1],key=lambda x:x.isupper() is False))
            c[g]=c.get(g,0)+1
    return c
# ebeveyn: KKBb (kırmızı, yüksek) × kkBb (sarı, yüksek): genotip çiftleri (K,B) için
def zig(p): return (p[0:2],p[2:4])
c5=capraz(zig('KKBb'),zig('kkBb')); assert sum(c5.values())==16
G5=set(c5); fen=lambda g:('kırmızı' if 'K' in g[:2] else 'sarı','yüksek' if 'B' in g[2:] else 'bodur')
F5={fen(g) for g in G5}; assert F5=={('kırmızı','yüksek'),('kırmızı','bodur')}
assert 'KkBb' in G5 and 'Kkbb' in G5 and 'KkBB' in G5 and 'kkBb' not in G5 and 'KKBb' not in G5
S5=['Meyvesi sarı ve boyu yüksek olan bir domates bitkisi','Meyvesi kırmızı ve boyu yüksek olan bir domates bitkisi','Meyvesi kırmızı ve boyu bodur olan bir domates bitkisi','KkBb genotipli bir domates bitkisi','Kkbb genotipli bir domates bitkisi']
q('0005','dihib',[A('Gametleri yaz','KKBb bireyi KB ve Kb, kkBb bireyi kB ve kb gameti oluşturur.','KKBb: KB, Kb · kkBb: kB, kb'),
   A('Her gen çiftini ayrı çaprazla','K geni için KK × kk, B geni için Bb × Bb çaprazlanır.','Meyve rengi: tamamı Kk · Boy: 1 BB : 2 Bb : 1 bb'),
   A('Oluşan genotipleri birleştir','Yavruların hepsi Kk’dır; boy bakımından BB, Bb ya da bb olabilir.','KkBB, KkBb, Kkbb'),
   A('Fenotipleri değerlendir','Tüm yavrular kırmızı meyvelidir; sarı meyveli (kk) yavru oluşmaz.','Sarı meyveli bitki gözlenmez')],
 'AABb tipi homozigot ebeveyn, görülmeyen fenotip',z='orta',alt='Dihibrit Çaprazlama',kaz='Dihibrit çaprazlamada oluşabilecek ve oluşamayacak genotip ve fenotipleri belirler.',kalip='hikâyeli',
 metin='Domateslerde kırmızı meyve (K), sarı meyve (k) üzerine; yüksek boy (B), bodur boy (b) üzerine tam baskındır ve iki gen çifti farklı kromozomlardadır. Bir araştırmacı, kırmızı meyveli ve boyu heterozigot yüksek (KKBb) bir bitkiyi, sarı meyveli ve boyu heterozigot yüksek (kkBb) bir bitkiyle çaprazlıyor. Krossing-over ve mutasyon gerçekleşmemiştir.\nBuna göre, bu çaprazlamadan elde edilen yavru bitkiler arasında aşağıdakilerden hangisi bulunmaz?',
 dogru=S5[0],sira=yer('E',S5[0],[S5[1],S5[2],S5[3],S5[4]]),
 yan=[(S5[1],'KkB_ genotipli yavrular vardır: Bb × Bb çaprazında yüksek boylu yavrular 3/4 oranındadır ve hepsi Kk olduğundan kırmızıdır. Bu fenotip gözlenir.','dikkat'),
      (S5[2],'Bb × Bb çaprazında bb (1/4) oluşur ve yavrular Kk’dır; kırmızı ve bodur yavrular gözlenir.','bilgi'),
      (S5[3],'Yavrular Kk’dır ve Bb × Bb çaprazında Bb (1/2) oluşur; KkBb genotipi gözlenir.','bilgi'),
      (S5[4],'Kk’ye bb (1/4) eşlik edebilir; Kkbb genotipi oluşur.','bilgi')],
 istenen='Yavrular arasında gözlenmeyen sınıf.',
 ip=['Her gen çiftini ayrı ayrı çaprazla ve oluşabilecek yavru genotiplerini yaz.'],
 bilgi=[B('Dihibrit çaprazlama','Bağımsız ayrılan gen çiftleri ayrı ayrı çaprazlanıp sonuçlar çarpılır · Heterozigot × heterozigot (Aa × Aa) çaprazında çekinik fenotip 1/4 oranındadır')],
 puf='Gen çiftlerini ayrı ele alıp olası gamet birleşimlerini yazarak hangi sınıfların oluştuğunu tara.')

# ============ 0006 · eşeye bağlı + otozomal · zor ============
kartla('06','dihib','Eşeye bağlı ve otozomal gen birlikte','Eşeye bağlı gen (göz rengi) ve otozomal gen (kanat) ayrı hesaplanıp çarpılır; belirli cinsiyet seçildiğinde o cinsiyet içindeki oran alınır.','Cinsiyet koşulunu bir kez daha çarpmak; göz rengini de otozomal sanmak; erkek yavruyu seçtikten sonra tüm yavrular üzerinden hesap yapmak.','zor','hikâyeli',5)
def sinek(anne,baba):   # anne: (X alleli çifti, kanat çifti) ; sonuç: {(cins,göz,kanat):olasılık}
    out={}
    for xa in anne[0]:
        for xb in baba[0]:
            for va in anne[1]:
                for vb in baba[1]:
                    cins='K' if xb!='Y' else 'E'
                    goz='kırmızı' if ('W' in (xa,xb)) else 'beyaz'
                    kan='uzun' if ('V' in (va,vb)) else 'kısa'
                    k=(cins,goz,kan); out[k]=out.get(k,0)+Fr(1,16)
    return out
S6=sinek((('W','w'),('V','v')),(('W','Y'),('V','v')))
assert sum(S6.values())==1
erkek=sum(v for k,v in S6.items() if k[0]=='E'); assert erkek==F(1,2)
p6=sum(v for k,v in S6.items() if k==('E','beyaz','uzun'))/erkek; assert p6==F(3,8)
assert sum(v for k,v in S6.items() if k==('E','beyaz','uzun'))==F(3,16) and F(1,2)*F(1,2)==F(1,4) and F(3,4)*F(3,4)==F(9,16)
dg,yn,sr=kesirler(p6,[(F(3,16),'Zaten erkek yavru seçildiği halde erkek olma olasılığını (1/2) bir kez daha çarpmış: 1/2 × 3/8.','dikkat'),
  (F(1,4),'Kanat bakımından uzun kanat olasılığını 1/2 almış (Vv × vv çaprazı gibi düşünmüş); oysa Vv × Vv çaprazında 3/4’tür: 1/2 × 1/2.','bilgi'),
  (F(1,2),'Kanat özelliğini hiç hesaba katmamış; yalnızca erkeklerin beyaz gözlü olma olasılığını (1/2) vermiş.','dikkat'),
  (F(9,16),'Göz rengini de otozomal sanıp iki özelliği de baskın hesaplamış: 3/4 × 3/4. Oysa istenen beyaz gözlüdür ve göz rengi X’e bağlıdır.','bilgi')])
q('0006','dihib',[A('Gametleri yaz','Dişi XWXw Vv; erkek XWY Vv. Göz rengi için X’ler, kanat için V alelleri ayrılır.','Dişi: XW/Xw ve V/v · Erkek: XW/Y ve V/v'),
   A('Göz rengini erkekler için hesapla','Erkek yavru Y’yi babadan, X’i annesinden alır; Xw alma olasılığı 1/2’dir.','Erkeklerde beyaz göz: 1/2'),
   A('Kanat için hesapla','Vv × Vv çaprazında uzun kanat (VV, Vv) olasılığı 3/4’tür.','Uzun kanat: 3/4'),
   A('Olasılıkları çarp','Gen yerleri bağımsız olduğundan oranlar çarpılır; erkek seçildiği için cinsiyet olasılığı katılmaz.','1/2 × 3/4 = 3/8')],
 'meyve sineği, X’e bağlı göz rengi + otozomal kanat',z='zor',alt='Eşeye Bağlı ve Bağımsız Kalıtım',kaz='Eşeye bağlı ve otozomal gen çiftini birlikte içeren çaprazlamada koşullu olasılık hesaplar.',kalip='hikâyeli',
 metin='Meyve sineklerinde kırmızı göz (W), beyaz göz (w) üzerine baskındır ve göz rengi geni X kromozomundadır; Y’de karşılığı yoktur. Uzun kanat (V), kısa kanat (v) üzerine baskındır ve kanat geni otozomaldir; iki gen yeri bağımsız ayrılır. Göz rengi bakımından taşıyıcı, kanat bakımından heterozigot bir dişi sinek ile kırmızı gözlü, heterozigot uzun kanatlı bir erkek sinek çiftleştiriliyor.\nBuna göre, bu çiftleşmeden doğan yavrular arasından rastgele seçilen bir erkek sineğin beyaz gözlü ve uzun kanatlı olma olasılığı kaçtır?',
 dogru=dg,yan=yn,sira=sr,istenen='Seçilen erkek yavrunun beyaz gözlü ve uzun kanatlı olma olasılığı.',
 ip=['Göz rengi ve kanat özelliğini ayrı gen yerleri olarak ele al; “erkek yavru seçildi” bilgisinin hangi olasılığı değiştirdiğini düşün.'],
 bilgi=[B('Bağımsız özelliklerde olasılık','Farklı kromozomlardaki gen çiftleri bağımsız ayrılır; olasılıklar çarpılır · Eşeye bağlı genlerde erkek X’ini yalnız annesinden alır, Y’yi babadan')],
 puf='Gen çiftlerini ayrı hesapla ve çarp; cinsiyet zaten verilmişse cinsiyet olasılığını bir daha katma.')

# ============ 0007 · ABO + Rh olumsuz · orta ============
kartla('07','abo','ABO ve Rh birlikte – oluşamayacak çocuk','AB anne ile O baba çiftinin çocukları yalnız A ya da B olabilir; Rh özelliği bağımsız kalıtılır. İlk çocuğun Rh− olması Rh+ babanın heterozigot olduğunu gösterir.','AB × O çiftinden AB ya da O çocuk bekleme; Rh+ babayı homozigot varsayma.','orta','hikâyeli',4)
kombin={(a,rh) for a in yavru('AB','OO') for rh in ('+','−')}
assert kombin=={('A','+'),('A','−'),('B','+'),('B','−')}   # baba Rr (ilk çocuk Rh−); anne rr
R7=[f'{a} kan grubundan, Rh{rh}' for a,rh in [('AB','+'),('A','+'),('A','−'),('B','+'),('B','−')]]
assert ('AB','+') not in kombin
q('0007','abo',[A('Ebeveynlerin genotipini yaz','Anne AB ve Rh−’dir (rr). Baba O (OO) ve Rh+’dır; ilk çocuk Rh− olduğundan baba heterozigottur (Rr).','Anne: ABrr · Baba: OORr'),
   A('ABO kan grubunu bul','Anne A ya da B aleli, baba yalnız O aleli aktarır.','Çocuk: AO (A) ya da BO (B)'),
   A('Rh’yi bul','Anne yalnız r, baba R ya da r aktarır; çocuk Rh+ ya da Rh− olabilir.','Rh+ veya Rh−'),
   A('Oluşamayacak sınıfı seç','ABO ve Rh bağımsızdır; çocuk AB ya da O olamaz.','AB grubundan çocuk gözlenmez')],
 'AB Rh− anne × O Rh+ baba, ilk çocuk Rh−',z='orta',alt='Kan Grupları',kaz='ABO ve Rh kan gruplarını birlikte değerlendirerek oluşabilecek ve oluşamayacak çocuk özelliklerini belirler.',kalip='hikâyeli',
 metin='Bir çiftin annesi AB kan grubundan ve Rh−, babası O kan grubundan ve Rh+’dır. Çiftin ilk çocuğu Rh− doğmuştur. ABO ve Rh kan grubu özellikleri bağımsız kalıtılmaktadır ve ailede mutasyon gerçekleşmemiştir.\nBuna göre, bu çiftin ikinci çocuğunun kan grubu özellikleri bakımından aşağıdakilerden hangisi olamaz?',
 dogru=R7[0],sira=yer('A',R7[0],R7[1:]),
 yan=[(R7[1],'Anne AB, baba O olduğundan A grubu (AO) oluşabilir; baba Rr olduğu için Rh+ (Rr) da oluşur. Bu kombinasyon beklenir.','dikkat'),
      (R7[2],'AO genotipi ve Rh− (rr) birlikte oluşabilir; baba Rr’dir ve r aleli aktarabilir.','bilgi'),
      (R7[3],'BO genotipi ve Rh+ (Rr) birlikte oluşabilir; kan grubu ve Rh bağımsız kalıtılır.','bilgi'),
      (R7[4],'BO genotipi ve Rh− (rr) birlikte oluşabilir; ikisi de annenin ve babanın verebileceği alellerdendir.','bilgi')],
 istenen='İkinci çocukta beklenmeyen kan grubu özelliği.',
 ip=['Babanın hangi ABO alelini aktarabileceğine bak; AB grubu için çocukta hangi iki alelin birleşmesi gerektiğini düşün.'],
 bilgi=[B('ABO ve Rh','ABO ve Rh farklı gen yerlerindedir, birbirinden bağımsız kalıtılır · Rh+ baskın (R), Rh− çekinik (rr)’dir · AB grubu çocuk için bir ebeveynden A, diğerinden B aleli gelmelidir')],
 puf='AB çocuk için ebeveynlerden birinde A, diğerinde B aleli gerekir; ebeveynlerden biri O (OO) ise çocuk AB ya da O olamaz (diğeri AB ise).')

# ============ 0008 · X'e bağlı tablo · orta · öncüllü ============
kartla('08','ese','Üç ailede X’e bağlı çekinik – kesin genotip','Hasta oğlu olan sağlıklı anne kesin taşıyıcıdır; hasta anne tüm oğullarına çekinik alel aktarır ve kızlarını taşıyıcı yapar; yalnız sağlıklı çocuğu olan annenin genotipi belirsizdir.','Sağlıklı anneyi homozigot baskın sanmak; hasta annenin kızlarını hasta saymak.','orta','tablo',4)
def aile(anne_aff,baba_aff,cocuklar):    # çocuk: (cins,hasta)
    out=[]
    for ga in ([2] if anne_aff else [0,1]):
        for gb in ([1] if baba_aff else [0]):
            ok=True
            for cins,h in cocuklar:
                olas={x for x in allel(ga)} if cins=='E' else {x+gb for x in allel(ga)}
                durum={(x==1) for x in olas} if cins=='E' else {(x==2) for x in olas}
                if bool(h) not in durum: ok=False
            if ok: out.append((ga,gb))
    return out
A1=aile(0,0,[('E',1),('K',0)]); A2=aile(1,0,[('K',0),('E',1)]); A3=aile(0,1,[('K',0),('E',0)])
assert A1==[(1,0)] and A2==[(2,0)] and A3==[(0,1),(1,1)]
d8={'I':(True,'1. ailede sağlıklı anne hasta bir oğul doğurmuştur; oğul Xd’yi yalnız annesinden alabileceği için anne XDXd taşıyıcıdır.'),
    'II':(False,'3. ailede baba hastadır ve çocuklar sağlıklıdır; anne XDXD ya da XDXd olabilir. Annenin taşıyıcı olmadığı ya da olduğu kesin değildir.'),
    'III':(False,'2. ailede anne hastadır (XdXd), baba sağlıklıdır; oğulların hepsi hastadır ancak kızların hepsi taşıyıcıdır, hasta değildir. “Kızlar hastadır” ifadesi yanlıştır.')}
# I: 1. aile annesi taşıyıcı kesin ; II: 3. ailede anne taşıyıcı değildir (kesin değil) ; III: 2. ailede kızların hepsi hasta (yanlış)
assert all(g==1 for g,_ in A1) and any(g==0 for g,_ in A3) and any(g==1 for g,_ in A3)
d8['II']=(False,'3. ailede baba hastadır ve çocukların hepsi sağlıklıdır; anne XDXD ya da XDXd olabilir. Annenin taşıyıcı olmadığı kesin değildir.')
d8['III']=(True,'2. ailede anne hastadır (XdXd) ve baba sağlıklıdır; kızlar babadan XD, anneden Xd alır. Kız çocuğu taşıyıcıdır, oğul hastadır.')
r=onc(d8,True,'C')
q('0008','ese',[A('Anne ve baba genotiplerini tara','Her ailede çocukların durumuna uyan tüm ebeveyn genotipleri taranır.','1. aile: anne XDXd · 2. aile: anne XdXd · 3. aile: anne XDXD veya XDXd'),
   adim_onc(d8,'I'),adim_onc(d8,'II'),adim_onc(d8,'III'),sonuc(r,True)],
 'üç aile tablosu, X’e bağlı çekinik hastalık',z='orta',alt='Eşeye Bağlı Kalıtım',kaz='Üç ailenin verisinden X’e bağlı çekinik kalıtımda kesin genotipleri belirler.',kalip='tablo',
 metin='Bir hastalığın X kromozomu üzerindeki çekinik bir alelle belirlendiği, Y kromozomunda bu gen yerinin bulunmadığı bilinmektedir. Üç ailenin her birinin ebeveyn, bir oğul ve bir kız çocuğunun durumu aşağıdaki tabloda verilmiştir. Ailelerde mutasyon gerçekleşmemiştir.\nBuna göre,\nI. 1. ailenin annesi taşıyıcıdır.\nII. 3. ailenin annesi homozigot baskındır.\nIII. 2. ailenin kız çocuğu hasta olmayıp taşıyıcıdır.\nyargılarından hangileri kesinlikle doğrudur?',
 sekil=tablo_dar(['Aile','Anne','Baba','Oğul','Kız'],[['1','Sağlıklı','Sağlıklı','Hasta','Sağlıklı'],['2','Hasta','Sağlıklı','Hasta','Sağlıklı'],['3','Sağlıklı','Hasta','Sağlıklı','Sağlıklı']]),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Kesinlikle doğru olan yargılar.',
 ip=['Her ailede çocukların durumundan, ebeveynlerin taşıyabileceği X alellerini ayrı ayrı belirle; birden çok olasılık kalan aileyi ayır.'],
 bilgi=[B('X’e bağlı çekinik kalıtım','Erkek çocuk X’ini yalnız annesinden alır · Hasta annenin (XdXd) oğulları hastadır, kızları sağlıklı baba ile taşıyıcıdır · Sağlıklı annenin hasta oğlu varsa anne taşıyıcıdır')],
 puf='Hasta oğlu ya da hasta kızı olan sağlıklı annenin genotipi kesindir (taşıyıcı); yalnız sağlıklı çocukları olan annede AA/Aa belirsizliği kalır.')

# ============ 0009 · test çaprazı tablosu · orta · öncüllü ============
kartla('09','capraz','Çaprazlama sonuç tablosu – 1:1:1:1','Yavru fenotip oranı 1:1:1:1 ise ebeveyn çifti yalnız AaBb × aabb değil, Aabb × aaBb de olabilir; “kesin” yargılar tüm ebeveyn genotip çiftleri taranarak bulunur.','1:1:1:1 görüp “ebeveynlerden biri çift çekiniktir” demek; iki seçeneği taramamak.','orta','tablo',4)
GEN9=['AA','Aa','aa']
def dag(p1,p2):
    out={}
    for pa in itertools.product(GEN9,GEN9):
        pass
    return out
def fenop(a1,b1,a2,b2):
    f={}
    for x in a1:
        for y in a2:
            for u in b1:
                for v in b2:
                    k=('A' if 'A' in (x,y) else 'a','B' if 'B' in (u,v) else 'b'); f[k]=f.get(k,0)+Fr(1,16)
    return f
PAIRS=[]
for p1 in itertools.product(['AA','Aa','aa'],['BB','Bb','bb']):
    for p2 in itertools.product(['AA','Aa','aa'],['BB','Bb','bb']):
        f=fenop(p1[0],p1[1],p2[0],p2[1])
        if len(f)==4 and set(f.values())=={Fr(1,4)}: PAIRS.append((p1,p2))
ayri={frozenset([p1,p2]) for p1,p2 in PAIRS}
assert ayri=={frozenset([('Aa','Bb'),('aa','bb')]),frozenset([('Aa','bb'),('aa','Bb')])}
def pr(f): return any(True for _ in [0])
# yargı doğrulama (tüm geçerli çiftlerde)
def tumu(fn): return all(fn(p1,p2) for p1,p2 in PAIRS)
assert not tumu(lambda p1,p2:p1==('aa','bb') or p2==('aa','bb'))                       # I yanlış (kesin değil)
assert tumu(lambda p1,p2:(p1[0]=='Aa')!=(p2[0]=='Aa') and (p1[0]=='aa' or p2[0]=='aa'))  # A geni: Aa × aa → yarısı baskın
assert tumu(lambda p1,p2:not(p1==('Aa','Bb') and p2==('Aa','Bb')))                      # III: ikisi birden AaBb olamaz
d9={'I':(False,'1:1:1:1 oranı AaBb × aabb çaprazından gelebilir; ancak Aabb × aaBb çaprazı da aynı oranı verir. Bu durumda ebeveynlerin hiçbiri çift çekinik değildir; yargı kesin değildir.'),
    'II':(True,'Her iki çaprazda da bir gen çifti Aa × aa, diğeri Bb × bb ya da bb × Bb biçimindedir; her özellikte yavruların yarısı baskın, yarısı çekinik fenotiplidir.'),
    'III':(False,'AaBb × AaBb çaprazı 9:3:3:1 oranı verir; yavruların 1:1:1:1 dağılması iki ebeveynin ikisinin birden AaBb olduğunu göstermez.')}
r=onc(d9,True,'B')
q('0009','capraz',[A('Fenotip oranını yaz','Dört fenotip sınıfında yavru sayıları eşittir.','1 : 1 : 1 : 1'),
   A('Ebeveyn çiftlerini tara','Bu oran AaBb × aabb ya da Aabb × aaBb çaprazından gelir.','İki olası çift'),
   adim_onc(d9,'I'),adim_onc(d9,'II'),adim_onc(d9,'III'),sonuc(r,True)],
 'hamster, fenotip sayıları tablosu',z='orta',alt='Çaprazlama Sonuçları',kaz='Yavru fenotip sayılarından ebeveyn genotipleri hakkında kesin çıkarımları belirler.',kalip='tablo',
 metin='Hamsterlerde sarı tüy (A), kahverengi tüy (a) üzerine; kısa tüy (B), uzun tüy (b) üzerine tam baskındır ve genler farklı kromozomlardadır. İki ebeveynin çaprazlanmasından elde edilen 160 yavrunun fenotip sayıları aşağıdaki tabloda verilmiştir. Ebeveyn genotipleri bilinmemektedir; mutasyon gerçekleşmemiştir.\nBuna göre,\nI. Ebeveynlerden biri her iki özellik bakımından çekinik homozigottur.\nII. Yavruların yarısı sarı tüylüdür.\nIII. Ebeveynlerin ikisi de her iki gen çifti bakımından heterozigottur.\nyargılarından hangileri kesinlikle doğrudur?',
 sekil=tablo_svg(['Tüy rengi','Tüy uzunluğu','Yavru sayısı'],[['Sarı','Kısa','40'],['Sarı','Uzun','40'],['Kahverengi','Kısa','40'],['Kahverengi','Uzun','40']]),
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Kesinlikle doğru olan yargılar.',
 ip=['Tablodaki sayıların oranını yaz ve bu oranı veren bütün ebeveyn genotip çiftlerini ayrı ayrı bul.'],
 bilgi=[B('Fenotip oranı ve genotip','Fenotip oranları ebeveyn gametlerinin birleşimlerinden bulunur · Örnek: AaBb × AaBb çaprazı 9:3:3:1 oranını verir · Aynı oranı veren birden çok ebeveyn genotip çifti bulunabilir')],
 puf='Oranı verebilen tüm ebeveyn çiftlerini yaz; yalnızca hepsinde geçerli olan yargı “kesin”dir.')

# ============ 0010 · eşeye bağlı olasılık · kolay ============
kartla('10','ese','Normal görüşlü çiftin renk körü oğlu','Sağlıklı annenin hasta oğlu varsa anne taşıyıcıdır; baba sağlıklı olduğundan XDY’dir. Taşıyıcı anne × sağlıklı baba çaprazında her çocuk için olasılıklar bağımsızdır; cinsiyet ve aleller ayrı çarpılır.','Önceki çocuğun durumunu sonraki çocuğu etkiler sanmak; “taşıyıcı kız” olasılığında cinsiyeti hesaba katmamak.','kolay','hikâyeli',3)
oll=Fr(0)
for ca,pa in (('XD',Fr(1,2)),('Xd',Fr(1,2))):
    for cb,pb in (('XD',Fr(1,2)),('Y',Fr(1,2))):
        if cb=='XD' and ca!=cb: oll+=pa*pb       # kız, taşıyıcı
assert oll==F(1,4) and F(1,2)*F(1,2)*F(1,2)==F(1,8)
dg,yn,sr=kesirler(oll,[(F(0),'Kızların renk körlüğü geninin hiç taşınmayacağını sanmış; oysa kızlar annelerinden Xd alabilir ve taşıyıcı olur.','bilgi'),
  (F(1,8),'Cinsiyet olasılığı ile aleli alma olasılığını yetmezmiş gibi bir kez daha (1/2) çarpmış: 1/2 × 1/2 × 1/2.','dikkat'),
  (F(1,2),'Cinsiyeti hesaba katmamış; kız çocukların yarısının taşıyıcı olduğunu bulup bunu tüm çocuklara uygulamış.','dikkat'),
  (F(3,4),'Sağlıklı görünen çocukların olasılığını (3/4) vermiş; taşıyıcı olma ile sağlıklı olmayı karıştırmış.','bilgi')])
q('0010','ese',[A('Ebeveyn genotiplerini yaz','Oğlu renk körü olan sağlıklı annenin Xd’yi taşıdığı kesindir; baba sağlıklı olduğundan XDY’dir.','Anne: XDXd · Baba: XDY'),
   A('Kız ve taşıyıcı olma olasılığını bul','Kız olması 1/2; annenin Xd aktarması 1/2.','1/2 × 1/2'),
   A('Sonucu yaz','Önceki çocuğun durumu sonraki çocuğu etkilemez.','1/4')],
 'renk körü oğlu olan normal görüşlü çift',z='kolay',alt='Eşeye Bağlı Kalıtım',kaz='Eşeye bağlı kalıtımda çocuğun taşıyıcı kız olma olasılığını hesaplar.',kalip='hikâyeli',
 metin='Renk körlüğü X kromozomu üzerindeki çekinik bir alelle (Xd) belirlenir ve Y kromozomunda karşılığı yoktur. Normal görüşlü bir anne ile normal görüşlü bir babanın ilk çocukları renk körü bir erkektir. Aile ikinci bir çocuk sahibi olmayı planlamaktadır. Ailede mutasyon gerçekleşmemiştir.\nBuna göre, ikinci çocuklarının renk körlüğü bakımından taşıyıcı bir kız olma olasılığı kaçtır?',
 dogru=dg,yan=yn,sira=sr,istenen='İkinci çocuğun taşıyıcı kız olma olasılığı.',
 ip=['Önce ilk çocuğun durumundan ebeveyn genotiplerine ulaş.'],
 bilgi=[B('Taşıyıcı birey','Taşıyıcı kız, çekinik aleli taşıyan ama hastalığı göstermeyen kızdır (XDXd) · Olasılıklar her doğumda aynıdır')],
 puf='Önce annenin genotipini çocuğun fenotipinden bul; sonra cinsiyet ve alel olasılıklarını ayrı ayrı çarp.')

bitir(P,'kalitimuc',UK)
