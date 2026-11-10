"""TYT Türkçe · Paragraf genişletme (pyarb): 30 ana soru, hafif mod (kardeş yok). Metinler özgündür; her şık etiketle denetlenir."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_pyarb import *
import re

KARTLAR={
 'K-PAB-01':dict(alt='Ulaşılamaz',fikir='Dört şıkkın her biri parçada açıkça karşılığı olan bir yargıdır; parçada hiç geçmeyen ya da parçayla çelişen yargıyı bulmak.',tuzak='Konuya yakın görünen şıkkı doğru sanmak; “ulaşılamaz” kökünü “ulaşılır” diye okumak; parçanın bir cümlesini abartan şıkta duraksamak.',zorluk='orta',kalip='düz',adim=3,tipId='pab-ulasilamaz',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (paragrafta anlam: ulaşılamaz)'),
 'K-PAB-02':dict(alt='Değinilmemiştir',fikir='Parçada işlenen dört noktayı tek tek bulup hiç işlenmeyen noktayı seçmek; parçaya ters olmak şart değil, yalnızca parçada yer almamak yeterlidir.',tuzak='Parçanın konusuna uygun düştüğü için değinilmemiş bir yargıyı “değinilmiş” saymak; ters bir yargıyla değinilmeyen yargıyı karıştırmak.',zorluk='orta',kalip='düz',adim=3,tipId='pab-degenilmemis',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (paragrafta anlam: değinilmemiştir)'),
 'K-PAB-03':dict(alt='Öncüllü Ulaşılabilir Yargılar',fikir='Her öncül ayrı ayrı parçayla sınanır: parçadan çıkarılabilen yargıya ulaşılır; parçada olmayan, abartılan ya da parçayla çelişen yargıya ulaşılamaz. Sonra doğru öncüllerin birleşimi şıklarda aranır.',tuzak='Öncüllerden birini ezbere doğru saymak; akla yatkın ama parçada olmayan yargıyı doğru kabul etmek; şıktaki birleşimi eksik okumak.',zorluk='zor',kalip='öncüllü',adim=4,tipId='pab-oncullu',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (paragrafta anlam: yargılardan hangilerine ulaşılabilir)'),
 'K-PAB-04':dict(alt='Söylenebilir',fikir='Parçadan doğrudan çıkarılabilen tek yargıyı bulmak; yanlış şıklar parçaya terstir, parçada yoktur ya da parçayı abartır.',tuzak='Parçada olmayan ama doğru bilinen bir yargıyı seçmek; “her, hiç, yalnızca” gibi sözcüklerle abartılmış şıkka kanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='pab-soylenebilir',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (paragrafta anlam: söylenebilir)'),
}
TIPLER={'pab-ulasilamaz':'Parçadan ulaşılamayan yargı','pab-degenilmemis':'Parçada değinilmeyen nokta','pab-oncullu':'Öncüllü yargılardan hangilerine ulaşılabilir','pab-soylenebilir':'Parçadan söylenebilecek yargı'}
Q=kur('pyarb','Paragraf','tr|Paragraf',KARTLAR,TIPLER,30)

BILGI={
 'pab-ulasilamaz':[B('Olumsuz soru kökü','“ulaşılamaz” sorusunda dört şık parçadan çıkarılabilir, doğru şık çıkarılamayandır. Örnek: parça “su yaşam kaynağıdır” diyorsa “suyun yaşamla ilgisi yoktur” ulaşılamaz'),B('Çıkarılamayan yargı','parçada hiç geçmeyen ya da parçayla çelişen yargıya ulaşılamaz. Örnek: parça yalnızca kitaptan söz ediyorsa “gazeteler yararsızdır” parçadan çıkarılamaz')],
 'pab-degenilmemis':[B('Değinme','bir yargıya değinilmiş sayılması için parçada açıkça ya da kesin biçimde işlenmesi gerekir. Örnek: parça yalnızca bir kentin sokaklarını anlatıyorsa kentin nüfusuna değinilmemiştir'),B('Olumsuz soru kökü','“değinilmemiştir” sorusunda dört şık parçada yer alır; doğru şık parçada hiç işlenmeyen şıktır')],
 'pab-oncullu':[B('Ulaşılabilir yargı','parçadan makul bir çıkarımla varılabilen yargıdır; parçada olmayan, abartılan ya da parçaya ters yargıya ulaşılamaz. Örnek: parça “spor yararlıdır” diyorsa “her spor herkese yararlıdır” abartıdır'),B('Öncüllü soru','her öncül ayrı sınanır, sonra doğru öncüllerin birleşimi şıklarda aranır. Örnek: I ve III doğruysa yanıt “I ve III”tür')],
 'pab-soylenebilir':[B('Söylenebilir yargı','parçadan doğrudan çıkarılabilen yargıdır; parçaya ters, parçada olmayan ya da parçayı abartan yargı söylenemez. Örnek: parça “bazı kuşlar göç eder” diyorsa “bütün kuşlar göç eder” söylenemez')],
}
PUFLAR={
 'pab-ulasilamaz':['Olumsuz köklerde önce dört “var” şıkkını parçada işaretle, geriye kalan şık doğrudur.','Parçada izi olmayan ya da parçayı tersine çeviren şık, “ulaşılamaz” sorusunun yanıtıdır.','Konuya uygun görünmesi bir yargının parçadan çıkarılabildiği anlamına gelmez; dayanak cümlesini göstermeden şık seçme.'],
 'pab-degenilmemis':['“Değinilmemiştir” sorusunda parçaya ters olmak şart değil, parçada işlenmemiş olmak yeterlidir.','Her şık için parçadaki dayanak cümleyi bul; dayanağı bulunamayan şık yanıttır.'],
 'pab-oncullu':['Öncülleri tek tek sına: parçada olmayan ya da abartılan öncül “ulaşılamaz”dır.','Önce öncüllere karar ver, şıklara sonra bak; şık, kararını doğrulayan birleşimdir.'],
 'pab-soylenebilir':['“Söylenebilir” sorusunda parçanın söylediğinin dışına çıkan şıkkı ele.','Abartı sözcükleri (hiç, her, yalnızca) taşıyan şıklar çoğunlukla parçadan taşar.'],
}
KOK={'pab-ulasilamaz':'Bu parçadan aşağıdakilerden hangisine ulaşılamaz?','pab-degenilmemis':'Bu parçada aşağıdakilerden hangisine değinilmemiştir?','pab-oncullu':'Bu parçadan hareketle aşağıdaki yargılardan hangilerine ulaşılabilir?','pab-soylenebilir':'Bu parçadan aşağıdakilerden hangisi söylenebilir?'}
ISTENEN={'pab-ulasilamaz':'Parçadan çıkarılamayan yargı.','pab-degenilmemis':'Parçada işlenmeyen nokta.','pab-oncullu':'Parçadan çıkarılabilen öncüllerin birleşimi.','pab-soylenebilir':'Parçadan çıkarılabilen yargı.'}
KART={'pab-ulasilamaz':'K-PAB-01','pab-degenilmemis':'K-PAB-02','pab-oncullu':'K-PAB-03','pab-soylenebilir':'K-PAB-04'}
sayac={}
def kelime(m): return len(re.findall(r'\w+',m))
def adimlar(tip,ozet,harf,dayanak,durum):
    """durum: A–E için 'var'/'yok'/... kısa etiketler (doğru şık dahil)."""
    isl=' · '.join(f'{l}: {durum[l]}' for l in 'ABCDE')
    kokac={'pab-ulasilamaz':('Kökü doğru oku','Kök olumsuz: parçadan çıkarılamayanı arıyoruz. Dört şık parçada dayanak bulacak.','aranan: dayanağı olmayan şık'),
           'pab-degenilmemis':('Kökü doğru oku','Kök “değinilmemiştir” diyor: parçada işlenmeyen noktayı arıyoruz. Dört şık parçada yer alacak.','aranan: parçada işlenmeyen şık'),
           'pab-soylenebilir':('Kökü doğru oku','Kök, parçadan çıkarılabilen yargıyı soruyor. Doğru şık parçanın söylediğinin dışına çıkmaz.','aranan: parçayla örtüşen şık')}[tip]
    return [A(*kokac),A('Dayanağı parçada bul',ozet,'dayanak: '+dayanak),A('Şıkları tek tek ele','Her şıkkı parçadaki cümleyle karşılaştır; dayanağı olan ya da olmayanı ayır.',isl),A('Sonucu ver',f'{harf} şıkkı kökün aradığı şıktır; diğerlerinin parçada dayanağı vardır.' if tip!='pab-soylenebilir' else f'{harf} şıkkı parçayla örtüşen tek şıktır; diğerleri parçaya terstir ya da parçada yoktur.',f'doğru: {harf}')]
def S(no,tip,zor,harf,metin,dogru,dayanak,yan,ip,ozet,kaz,puf=None):
    """yan: 4 adet (şık, cel) ya da (şık, cel, tur). Doğru şık harf konumuna yerleşir; yanlışlar verilen sırayla kalan harflere."""
    tur0='dikkat' if tip in('pab-ulasilamaz','pab-degenilmemis') else 'bilgi'
    kelimeler=kelime(metin); aralik={'kolay':(40,110),'orta':(60,140),'zor':(100,150)}[zor]
    print(no,zor,kelimeler)
    assert len(yan)==4 and len(dogru)<=max(len(y[0]) for y in yan)+4,(no,'doğru şık çok uzun')
    sayac[tip]=sayac.get(tip,0)
    opts=[];it=iter(yan);durum={}
    for l in 'ABCDE':
        if l==harf: opts.append((dogru,'+'+dayanak,None,None)); durum[l]='yok ✓' if tip!='pab-soylenebilir' else 'doğru ✓'
        else:
            y=next(it); opts.append((y[0],'-'+y[1],y[1],y[2] if len(y)>2 else tur0)); durum[l]='var' if tip in('pab-ulasilamaz','pab-degenilmemis') else 'yanlış'
    puf=puf or PUFLAR[tip][len(sayac)%len(PUFLAR[tip]) if False else sum(1 for q in Q.P.ANA if q['tipId']==tip)%len(PUFLAR[tip])]
    soru(Q,no,KART[tip],zor,kaz,{'kolay':2,'orta':3,'zor':4}[zor],'düz',metin+'\n'+KOK[tip],opts,harf,lambda e:e[0]=='+',ISTENEN[tip],ip,BILGI[tip],adimlar(tip,ozet,harf,dayanak,durum),puf)

ROMS=['I','II','III']
KOMB=[(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)]
def kad(c): return {(0,):'Yalnız I',(1,):'Yalnız II',(2,):'Yalnız III',(0,1):'I ve II',(0,2):'I ve III',(1,2):'II ve III',(0,1,2):'I, II ve III'}[c]
def O(no,zor,harf,metin,onc,ip,ozet,kaz,puf=None):
    """onc: 3 adet (yargı, doğru_mu, not). Şık dizilimi: doğru birleşim harf konumuna gelecek biçimde 5 birleşim seçilir."""
    tip='pab-oncullu'; T=tuple(i for i in range(3) if onc[i][1]); assert T and T in KOMB
    r=KOMB.index(T); hedef='ABCDE'.index(harf); digerler=[k for k in KOMB if k!=T]
    from itertools import combinations
    sec=None
    for c in combinations(range(6),4):
        l=[digerler[i] for i in c]; onceki=sum(1 for k in l if KOMB.index(k)<r)
        if onceki==hedef: sec=l; break
    assert sec,(no,'harf uygun değil')
    liste=sorted(sec+[T],key=KOMB.index); assert 'ABCDE'[liste.index(T)]==harf
    opts=[]
    for k in liste:
        if k==T:
            gerek='; '.join(f'{ROMS[i]}. yargı: {onc[i][2]}' for i in T); opts.append((kad(k),'+'+gerek,None,None))
        else:
            parca=[]
            for i in sorted(set(k)-set(T)): parca.append(f'{ROMS[i]}. yargıya ulaşılamaz ({onc[i][2]})')
            for i in sorted(set(T)-set(k)): parca.append(f'{ROMS[i]}. yargıya ulaşılabilir ({onc[i][2]}), şıkta eksik kalmış')
            tur='bilgi' if set(k)-set(T) else 'dikkat'
            opts.append((kad(k),'-'+'; '.join(parca),'; '.join(parca)+'.',tur))
    metin=metin+'\n'+'\n'.join(f'{ROMS[i]}. {onc[i][0]}' for i in range(3))+'\n'+KOK[tip]
    kl=kelime(metin.split('\nI. ')[0]); print(no,zor,kl)
    durum=' · '.join(f'{ROMS[i]}: '+('ulaşılabilir' if onc[i][1] else 'ulaşılamaz') for i in range(3))
    st=[A('Öncülleri ayrı ayrı oku','Her yargı bağımsız bir iddiadır; birini doğru bulmak ötekileri doğru yapmaz. Hepsini parçayla sınayacağız.','sınanacak: I · II · III' if False else 'sınanacak: üç yargı'),
        A('Dayanak ara',ozet,'dayanak: '+'; '.join(f'{ROMS[i]} {"var" if onc[i][1] else "yok"}' for i in range(3))),
        A('Karar ver',' '.join(f'{ROMS[i]}. yargı: {onc[i][2]}.' for i in range(3)),durum),
        A('Şıkta birleşimi bul',f'Doğru öncüllerin birleşimi “{kad(T)}” olduğundan yanıt {harf} şıkkıdır.',f'doğru: {harf}')]
    soru(Q,no,KART[tip],zor,kaz,{'kolay':2,'orta':3,'zor':4}[zor],'öncüllü',metin,opts,harf,lambda e:e[0]=='+',ISTENEN[tip],ip,BILGI[tip],st,puf or PUFLAR[tip][int(no)%2])

V='dikkat'
# ===================== ULAŞILAMAZ =====================
S('0001','pab-ulasilamaz','kolay','A',
 'Mahalle bakkalı yalnızca alışveriş yapılan bir dükkân değildir. Bakkal, sokaktan geçen herkesi tanır; kimin evde hasta olduğunu, kimin sınava hazırlandığını bilir. Çocuklar harçlıklarıyla ilk alışverişlerini orada yapar, yaşlılar da evden çıkmadan siparişlerini telefonla iletir. Veresiye defteri, parayla ölçülemeyen bir güven ilişkisinin kaydıdır. Büyük marketlerin yaygınlaşmasıyla bu ilişki zayıflamış, alışveriş hızlanmış ama sohbet azalmıştır. Bu yüzden mahalleliler, bakkalın kapanmasına bir dükkânın kapanmasından fazlası olarak bakar.',
 'Bakkallar fiyat bakımından marketlere üstündür.','Parçada bakkal–market karşılaştırması ilişki ve sohbet üzerinden yapılır; fiyattan hiç söz edilmez.',
 [('Bakkallar, çevresindeki insanlar hakkında bilgi sahibidir.','Parçada karşılığı var: bakkal “kimin evde hasta olduğunu” bilir.'),
  ('Veresiye defteri, bakkalla müşteri arasındaki güveni yansıtır.','Parçada karşılığı var: defter “güven ilişkisinin kaydıdır”.'),
  ('Marketlerin yaygınlaşması alışverişi hızlandırmıştır.','Parçada karşılığı var: son cümlede “alışveriş hızlanmış” denir.'),
  ('Bakkalın kurduğu ilişkiler alışverişten daha geniş anlam taşır.','Parçada karşılığı var: ilk cümle bakkalın “yalnızca alışveriş yapılan” yer olmadığını söyler.')],
 'Şıkların hangisi parçada hiç geçmeyen bir konuyu getiriyor?','Bakkal ve market karşılaştırması parçada yalnızca ilişki ve sohbet üzerinden yapılır; fiyat konusu hiç açılmaz. Diğer dört şık parçadaki birer cümleyle eşleşir.','Parçada bulunmayan yargıyı belirler.')
S('0002','pab-ulasilamaz','kolay','B',
 'Bir romanı ikinci kez okuyan kişi, ilk okumada gözünden kaçan ayrıntıları fark eder. Ne var ki bu, kitabın değiştiği anlamına gelmez; değişen, okurun kendisidir. Çocukken sevilen bir kitabın yetişkinlikte bambaşka bir tat vermesi bundandır. Aradan geçen yıllar okura yeni yaşantılar kazandırmıştır ve metin bu birikimle başka bir ışıkta görünür. Bu nedenle iyi bir roman, bir kez okunup rafa kaldırılan bir şey değil, okurla birlikte yaşlanan bir yol arkadaşıdır.',
 'Bir romanın metni her okuyuşta kendiliğinden değişir.','Parça “kitabın değiştiği anlamına gelmez; değişen okurun kendisidir” der; şık parçayla çelişir.',
 [('İlk okumada fark edilmeyen ayrıntılar sonra görünür olabilir.','Parçada karşılığı var: ikinci okuyan kişi “gözünden kaçan ayrıntıları fark eder”.'),
  ('Okurun yaşantıları, metnin algılanışını etkileyebilir.','Parçada karşılığı var: metin “bu birikimle başka bir ışıkta görünür”.'),
  ('Geçen yıllar okura yeni yaşantılar kazandırmıştır.','Parçada karşılığı var: “aradan geçen yıllar okura yeni yaşantılar kazandırmıştır”.'),
  ('İyi bir roman, tekrar okunmaya değer bir eserdir.','Parçada karşılığı var: iyi roman “rafa kaldırılan” değil, okurla yaşlanan bir yol arkadaşıdır.')],
 '“Ne var ki” sonrasında parça neyin değiştiğini söylüyor?','Parça değişenin kitap değil okur olduğunu söyler; “metin kendiliğinden değişir” yargısı bununla çelişir. Diğer dört şık parçada açıkça yer alır.','Parçayla çelişen yargıyı belirler.')
S('0003','pab-ulasilamaz','orta','C',
 'Gönüllülük, çoğu zaman karşılıksız emek olarak tanımlanır; oysa gönüllü çalışanlar karşılıklarını başka biçimlerde alır: yeni arkadaşlıklar, kazanılan beceriler, kendini işe yarar hissetmenin verdiği doyum. Hiçbir karşılık beklemediğini söyleyen gönüllü bile, çoğu zaman emeğinin bir işe yaradığını görmekten memnun olur. Bu durum gönüllülüğün değerini azaltmaz, tersine onu sürdürülebilir kılar. Yalnızca verenin yorulduğu bir ilişki uzun ömürlü olmaz; iki tarafın da bir şey kazandığı bir ilişki ise kendi kendini besler.',
 'Gönüllünün karşılık görmesi, gönüllülüğün değerini azaltır.','Parça karşılık görmenin gönüllülüğün değerini “azaltmadığını” söyler; şık parçayla çelişir.',
 [('Gönüllüler maddi olmayan kazançlar elde edebilir.','Parçada karşılığı var: arkadaşlık, beceri ve doyum sayılır.'),
  ('Karşılıklı kazanç, gönüllülüğün sürmesine katkı sağlar.','Parçada karşılığı var: karşılıklı ilişki “kendi kendini besler”, değeri “sürdürülebilir” kılar.'),
  ('Gönüllülük sırasında yeni beceriler edinilebilir.','Parçada karşılığı var: “kazanılan beceriler” karşılıklar arasında sayılır.'),
  ('Gönüllülük, çoğu kez karşılıksız emek diye anlaşılır.','Parçada karşılığı var: ilk cümle bunu bir tespit olarak verir.')],
 'Parça karşılık görmenin gönüllülüğe etkisi için ne diyor?','Parça, karşılık görmenin gönüllülüğü azaltmadığını, sürdürülebilir kıldığını söyler. “Değerini azaltır” şıkkı bu cümleyle çelişir.','Parçayla çelişen yargıyı belirler.')
S('0004','pab-ulasilamaz','orta','D',
 'Ezbere dayalı öğrenme kısa vadede iyi sonuç verir; sınavdan önce toplanan bilgi sınavdan sonra hızla silinir. Anlayarak öğrenilen konu ise başka konulara bağlanır ve zamanla kendi kendine genişler. Nitekim bir kez anlaşılan bir konu aylar sonra bile kısa bir hatırlatmayla yerine oturur. Bu, ezberin tümüyle gereksiz olduğu anlamına gelmez: çarpım tablosu ya da bir dildeki temel sözcükler ezberlenmeden ilerlemek zordur. Sorun, ezberin bir araç olmaktan çıkıp tek yöntem hâline gelmesindedir.',
 'Ezber, öğrenme sürecinden tümüyle çıkarılmalıdır.','Parça ezberin “tümüyle gereksiz olduğu anlamına gelmediğini” söyler; şık parçayla çelişir.',
 [('Ezberlenen bilgi çoğu zaman kalıcı olmaz.','Parçada karşılığı var: bilgi sınavdan sonra “hızla silinir”.'),
  ('Anlayarak öğrenme, bilgilerin birbirine bağlanmasını sağlar.','Parçada karşılığı var: anlayarak öğrenilen konu “başka konulara bağlanır”.'),
  ('Kimi konularda ezber, öğrenmenin gerekli parçasıdır.','Parçada karşılığı var: çarpım tablosu ve temel sözcükler örnek verilir.'),
  ('Ezber, tek yöntem olduğunda sorun yaratır.','Parçada karşılığı var: son cümle sorunu “tek yöntem hâline gelmesinde” görür.')],
 'Parça ezberin tümüyle gereksiz olduğunu söylüyor mu?','Parça ezberin sınırlarını çizer ama tümüyle gereksiz saymaz. “Tümüyle çıkarılmalıdır” yargısı parçayla çelişir.','Aşırı genellemeyi ve çelişen yargıyı ayırt eder.')
S('0005','pab-ulasilamaz','orta','E',
 'Bir müzede en kalabalık yer, çoğu kez en ünlü eserin önüdür; oysa ziyaretçilerin eserin karşısında durduğu süre birkaç saniyeyi bulmaz. Çoğu insan eseri görmekten çok, onunla birlikte görüntülenmeyi önemser. Kimi ziyaretçi, yanındaki arkadaşıyla sohbet ederken eserin etiketini bile okumadan yoluna devam eder. Oysa bir esere uzun uzun bakmak, ilk bakışta fark edilmeyen ayrıntıları ortaya çıkarır. Bu yüzden bazı müzeler, kalabalığı dağıtan sessiz bakış köşeleri düzenlemektedir.',
 'Müzelerde fotoğraf çekmek yasaklanmalıdır.','Parça müzelerdeki bir uygulamayı anlatır; fotoğraf yasağı önerisi parçada yoktur.',
 [('Ünlü eserlerin önü genellikle kalabalıktır.','Parçada karşılığı var: en kalabalık yer “en ünlü eserin önüdür”.'),
  ('Çok sayıda ziyaretçi eserin karşısında kısa süre durur.','Parçada karşılığı var: süre “birkaç saniyeyi bulmaz”.'),
  ('Uzun bakış eserin gözden kaçan yönlerini ortaya çıkarır.','Parçada karşılığı var: üçüncü cümle bunu söyler.'),
  ('Bazı müzeler izleyiciye yönelik sessiz alanlar kurar.','Parçada karşılığı var: son cümledeki “sessiz bakış köşeleri”.')],
 'Parçada bir yasaktan ya da öneriden söz ediliyor mu?','Parça yasaklayıcı bir öneri getirmez, müzelerin sessiz köşeler kurduğunu aktarır. Fotoğraf yasağı parçada hiç geçmez.','Parçada geçmeyen öneriyi belirler.')
S('0006','pab-ulasilamaz','orta','A',
 'Kentlerde yeşil alanlar çoğu zaman “boş arsa” gözüyle görülür ve imara açılacak ilk yerler olur. Bir sokağın ya da mahallenin yeşili, çoğu zaman yıllar içinde büyüyen ağaçlarla oluşur ve kesildiğinde kolay yerine konmaz. Oysa parklar yalnızca nefes alınan yerler değildir; yaz sıcağında çevresini birkaç derece serinletir, yağmur sularının toprağa karışmasını sağlar ve komşuların birbirini tanıdığı ortak bir buluşma noktası oluşturur. Bu yararlar sayılarla gösterilemediği için karar verilirken kolayca gözden çıkarılır.',
 'Yeşil alanların bakımı kent bütçesine ağır yük getirir.','Parçada yeşil alanların maliyetinden hiç söz edilmez; şık parçada yer almaz.',
 [('Yeşil alanlar, kentin sıcaklığını düşürebilir.','Parçada karşılığı var: park çevresini “birkaç derece serinletir”.'),
  ('Yeşil alanların toplumsal bir işlevi de vardır.','Parçada karşılığı var: parklar “ortak bir buluşma noktası” oluşturur.'),
  ('Yeşil alanlar imara açılacak ilk yerler sayılabilir.','Parçada karşılığı var: ilk cümlede böyle denir.'),
  ('Yeşil alanların yararı rakamla gösterilemediği için ihmal edilir.','Parçada karşılığı var: son cümle bunu söyler.')],
 'Parça yeşil alanların maliyetinden söz ediyor mu?','Parça yeşil alanların yararlarını sayar, bakım giderlerine hiç değinmez. Bu yüzden bakım yükü yargısına ulaşılamaz.','Parçada olmayan yargıyı belirler.')
S('0007','pab-ulasilamaz','orta','B',
 'Çeviri, bir metni sözcük sözcük başka bir dile aktarmak değildir; çünkü her dilin kendine özgü bir ses düzeni, deyim dağarcığı ve düşünme alışkanlığı vardır. İyi bir çevirmen yalnızca iki dili değil, iki kültürü de bilir. Bir deyimi harfi harfine çevirmek, çoğu zaman anlamı ortadan kaldırır. Örneğin bir dilde yağmurun yağışını anlatan bir deyim, başka bir dilde bambaşka bir görüntüyle karşılanabilir. Bu yüzden çevirmen, yazarın söylediğini değil, söylemek istediğini okura ulaştırmaya çalışır.',
 'Çevirmen, metni okura uyarlamak için kısaltmak zorundadır.','Parçada çevirmenin metni kısaltması gerektiğinden söz edilmez; şık parçada yer almaz.',
 [('Her dilin kendine özgü bir deyim dağarcığı vardır.','Parçada karşılığı var: ilk cümlede “deyim dağarcığı” geçer.'),
  ('İyi çeviri için iki kültürü tanımak gerekir.','Parçada karşılığı var: iyi çevirmen “iki kültürü de bilir”.'),
  ('Sözcüğü sözcüğüne çeviri anlam kaybına yol açabilir.','Parçada karşılığı var: harfi harfine çeviri “anlamı ortadan kaldırır”.'),
  ('Çevirmen, yazarın amaçladığı anlamı aktarmayı hedefler.','Parçada karşılığı var: çevirmen “söylemek istediğini” ulaştırmaya çalışır.')],
 'Parçada çevirmene yüklenen görevler neler?','Parça çevirmenin iki kültürü bilmesini ve yazarın amacını aktarmasını anlatır. Metni kısaltma zorunluluğu parçada geçmez.','Parçada olmayan yargıyı belirler.')
S('0008','pab-ulasilamaz','orta','C',
 'Apartman yaşamında insanlar yan yana yaşadığı hâlde çoğu zaman birbirine yabancıdır. Asansörde yapılan kısa selamlaşma, tanışıklığın en ileri biçimi sayılır. Merdivende karşılaşıp başını eğerek geçen komşular bunun en bilinen örneğidir. Oysa bir su kesintisi, bir bayram ya da bir yönetim toplantısı bu mesafeyi bir anda kısaltabilir; ortak bir derdi olan insanlar birbirinin kapısını çalmakta zorlanmaz. Demek ki yabancılığı yaratan, duvarların inceliği değil, ortak bir konunun eksikliğidir.',
 'Komşular arasındaki yabancılığın nedeni binanın yapısıdır.','Parça yabancılığın nedenini “duvarların inceliğinde değil” ortak konu eksikliğinde görür; şık parçayla çelişir.',
 [('Apartmanda komşuluk ilişkileri çoğu zaman yüzeyseldir.','Parçada karşılığı var: selamlaşma “tanışıklığın en ileri biçimi” sayılır.'),
  ('Ortak sorunlar komşuları birbirine yaklaştırabilir.','Parçada karşılığı var: ortak derdi olanlar “kapıyı çalmakta zorlanmaz”.'),
  ('Bayram gibi günler komşuluğu canlandırabilir.','Parçada karşılığı var: bayram mesafeyi kısaltan durumlar arasında sayılır.'),
  ('Yabancılığın asıl kaynağı ortak bir konunun eksikliğidir.','Parçada karşılığı var: son cümle bunu açıkça söyler.')],
 'Son cümlede yabancılığın nedeni olarak ne reddediliyor?','Parça yabancılığın nedenini duvarlarda değil, ortak konu eksikliğinde bulur. Binanın yapısına bağlayan şık parçayla çelişir.','Parçanın reddettiği nedeni içeren şıkkı bulur.')
S('0009','pab-ulasilamaz','zor','D',
 'Bir eserin klasik sayılması için yalnızca eski olması yetmez; eski olup unutulan pek çok eser vardır. Klasik, her çağın okuru tarafından yeniden okunabilen ve her okumada yeni bir şey söyleyen eserdir. Bu yüzden klasikler, yazıldıkları dönemin ruhunu taşımalarına rağmen o dönemle sınırlı kalmaz. Bir tragedya, yazıldığı yüzyılın töresini yansıtır; ama bugünkü okur, o töreyi bilmese bile eserin acısını anlar. Ancak bu nitelik, eserin bir kez kazanıp sonsuza dek koruduğu bir ayrıcalık da değildir: Her kuşak, ona yeniden ilgi gösterdiği ölçüde onu klasik tutar. Bu bakımdan klasikliği bir ödül değil, sürekli yenilenen bir ilişki saymak gerekir. Başka bir deyişle klasikliği eserin kendisi kadar, onu okuyanlar da belirler.',
 'Eser klasik olduktan sonra bu niteliği kalıcı biçimde korur.','Parça klasikliğin “sonsuza dek korunan bir ayrıcalık” olmadığını söyler; şık parçayla çelişir.',
 [('Eskilik, bir eserin klasik sayılması için tek başına yetmez.','Parçada karşılığı var: ilk cümlede böyle denir.'),
  ('Klasik eserler, yazıldığı dönemin özelliklerini taşıyabilir.','Parçada karşılığı var: klasikler “dönemin ruhunu taşır”.'),
  ('Klasikliğin sürmesi, okurların eserle ilişkisine bağlıdır.','Parçada karşılığı var: her kuşak ilgi gösterdiği ölçüde eseri “klasik tutar”.'),
  ('Klasik bir eser her okumada yeni bir şey söyler.','Parçada karşılığı var: ikinci cümlede böyle tanımlanır.')],
 '“Ancak” bağlacından sonra parça klasikliği nasıl niteliyor?','“Ancak” sonrası parça klasikliğin kalıcı bir ayrıcalık olmadığını, kuşakların ilgisine bağlı olduğunu söyler. “Kalıcı biçimde korur” yargısı bununla çelişir.','Bağlaç sonrası gelen asıl yargıya dikkat ettirir.')
S('0010','pab-ulasilamaz','zor','E',
 'Çocukların açıkça soru sorma sıklığı, okul çağına geldiklerinde belirgin biçimde azalır. Bunun nedeni merakın körelmesi sanılır; oysa araştırmalar, çocukların sormaktan vazgeçmediğini, yalnızca sorularını artık yüksek sesle sormadıklarını gösterir. Bu düşüş, çoğu zaman okulla birlikte başlayan yeni bir kuralla ilişkilendirilir: söz almadan konuşulmaz ve her soru ders akışına uygun olmak zorundadır. Evde bütün gün “neden” diye soran çocuk, sınıfta parmak kaldırmadan önce arkadaşlarının ona nasıl bakacağını uzun uzun hesaplar. Sınıfta yanlış soru sormanın küçük düşürücü olabileceğini öğrenen çocuk, sorusunu kendine saklar. Dolayısıyla merak ölmez, yer değiştirir; öğretmenin işi de merakı yeniden yaratmak değil, ona güvenli bir ortam hazırlamaktır. Bu yüzden öğretmenler, sessiz bir sınıfı ilgili bir sınıf sanma yanılgısına düşebilir.',
 'Öğretmen, çocuğun merakını yeniden uyandırmakla yükümlüdür.','Parça öğretmenin işinin merakı “yeniden yaratmak değil”, güvenli ortam hazırlamak olduğunu söyler; şık parçayla çelişir.',
 [('Okul çağında çocukların açıkça soru sorması azalır.','Parçada karşılığı var: ilk cümle sıklığın “belirgin biçimde azaldığını” söyler.'),
  ('Soru sormaktan çekinme, çevreden gelen tepkiyle ilişkilidir.','Parçada karşılığı var: yanlış soru sormanın “küçük düşürücü” olabileceği öğrenilir.'),
  ('Çocuk, dile getirmediği sorulara ilişkin merakı sürdürebilir.','Parçada karşılığı var: çocuk sorusunu “kendine saklar”, merak yer değiştirir.'),
  ('Öğretmenin işi, soru sormayı güvenli kılacak ortamı hazırlamaktır.','Parçada karşılığı var: son cümlede böyle denir.')],
 'Parça öğretmenin işini ne olarak, neyin karşıtı olarak tanımlıyor?','Parça merakın ölmediğini söylediği için öğretmenin görevini merakı yeniden yaratmak olarak görmez. Bu görevi ona yükleyen şık parçayla çelişir.','“değil” ile reddedilen yargıyı seçenekte yakalar.')
# ===================== DEĞİNİLMEMİŞTİR =====================
S('0011','pab-degenilmemis','kolay','A',
 'Sokak müzisyenleri kentin en eski seslerinden biridir. Köprü başında çalan keman, meydandaki gitar, tramvay durağındaki akordeon; her biri yoldan geçenin gününe küçük bir ritim ekler. Müzisyen için de sokak bir sahnedir ve seyirci, davetsiz ama hiç beklemeden gelen bir kalabalıktır. Bazen tek bir şarkı, aceleyle yürüyen birini birkaç dakikalığına durdurur. Kimi akşamlar, kalabalığın arasından bir türkü yükselir ve bütün bir sokak onunla birlikte yavaşlar.',
 'Sokak müzisyenlerinin gelirine ilişkin bilgi verilmiştir.','Parçada müzisyenlerin kazancından hiç söz edilmez.',
 [('Sokak müzisyenlerinin çaldığı çalgılardan örnek verilmiştir.','Parçada karşılığı var: keman, gitar ve akordeon sayılır.'),
  ('Sokağın müzisyen için bir sahne işlevi gördüğü söylenmiştir.','Parçada karşılığı var: “sokak bir sahnedir”.'),
  ('Müziğin yoldan geçenleri etkileyebildiğine yer verilmiştir.','Parçada karşılığı var: bir şarkı “aceleyle yürüyen birini durdurur”.'),
  ('Sokak müzisyenliğinin kentte eski bir geçmişi olduğu belirtilmiştir.','Parçada karşılığı var: sokak müzisyenleri “kentin en eski seslerinden biridir”.')],
 'Hangi konu parçada hiç geçmiyor?','Parça çalgıları, sahneyi, dinleyiciyi ve geçmişi işler; gelir konusu hiç açılmaz. Diğer dört şık parçada yer alır.','Parçada işlenmeyen noktayı belirler.')
S('0012','pab-degenilmemis','kolay','B',
 'Bisiklet, kent trafiğinde hem hızlı hem sessiz bir ulaşım aracıdır. Kısa mesafelerde otomobilden daha çabuk varılabilir, park yeri aramak gerekmez ve havaya duman karışmaz. Üstelik bisiklet, trafik sıkışıklığında kendine yer bulabilen az sayıdaki araçtan biridir. Sabah işe giderken sıraya girmiş araçların yanından geçmek, birçok kullanıcı için küçük bir keyiftir. Ancak bisiklet kullanıcılarının güvenle yol alabilmesi için ayrılmış yollara gerek vardır; aksi hâlde bisiklet, çoğu insan için çekici bir seçenek olmaktan çıkar.',
 'Bisiklet kullanımının sağlığa yararlı olduğu vurgulanmıştır.','Parçada bisikletin sağlığa etkisinden söz edilmez.',
 [('Bisikletin kısa mesafede hız üstünlüğü sağladığı belirtilmiştir.','Parçada karşılığı var: kısa mesafelerde “otomobilden daha çabuk” varılır.'),
  ('Bisikletin havayı kirletmediği ifade edilmiştir.','Parçada karşılığı var: “havaya duman karışmaz”.'),
  ('Bisiklet yollarının gerekliliği üzerinde durulmuştur.','Parçada karşılığı var: “ayrılmış yollara gerek vardır”.'),
  ('Bisikletle park sorunu yaşanmadığına değinilmiştir.','Parçada karşılığı var: “park yeri aramak gerekmez”.')],
 'Bisikletin hangi yararı parçada sayılmıyor?','Parça hızı, temiz havayı, park kolaylığını ve yol gereksinimini işler. Sağlık konusu hiç geçmez.','Parçada işlenmeyen noktayı belirler.')
S('0013','pab-degenilmemis','orta','C',
 'Şiirde ses, anlam kadar önemlidir. Kimi şair, sözcükleri anlamlarına göre değil çıkardıkları sese göre seçer; aynı ünlünün tekrarı bir hüzün, kısa ve sert ünsüzlerin ardı ardına gelişi bir gerginlik duygusu uyandırır. Bu tür şiirler çevrilmeye direnir, çünkü bir dilin sesi başka bir dile taşınamaz. Bu yüzden bazı şairler yazdıklarını bitirmeden önce defalarca yüksek sesle okuyup kulaklarına güvenir. Okur ise bu şiirleri sessizce okumaktansa yüksek sesle okuyarak daha iyi kavrar.',
 'Şairlerin kişisel duygularını öne çıkardığı söylenmiştir.','Parçada şairin kendi duygularını anlatmasından söz edilmez; duygu yalnızca okurda uyanan etki olarak geçer.',
 [('Şiirde sesin anlam kadar belirleyici olduğu savunulmuştur.','Parçada karşılığı var: ilk cümle böyle der.'),
  ('Seslerin okurda duygu uyandırabileceğine örnek verilmiştir.','Parçada karşılığı var: ünlü tekrarı hüzün, sert ünsüzler gerginlik uyandırır.'),
  ('Ses ağırlıklı şiirlerin çevrilmesinin güç olduğu belirtilmiştir.','Parçada karşılığı var: bu şiirler “çevrilmeye direnir”.'),
  ('Yüksek sesle okumanın kavramayı kolaylaştırdığı söylenmiştir.','Parçada karşılığı var: okur şiirleri yüksek sesle okuyarak “daha iyi kavrar”.')],
 'Şairin neye göre sözcük seçtiği parçada nasıl anlatılıyor?','Parça şairin sözcüğü sesine göre seçtiğini söyler, kişisel duygularından söz etmez. Diğer dört şık parçada işlenir.','Konuya yakın ama işlenmemiş noktayı ayırır.')
S('0014','pab-degenilmemis','orta','D',
 'Geri dönüşüm alışkanlığı bireysel bir erdem gibi sunulsa da asıl belirleyici olan, kentin altyapısıdır. Mahallesinde ayrı toplama kutuları bulunan kişi, atıklarını ayırmayı kısa sürede alışkanlık hâline getirir; kutuyu on dakika uzakta bulan kişi ise en iyi niyetle bile vazgeçer. Alışkanlık, çoğu zaman bir kez kurulduktan sonra kendini sürdürür. Bu nedenle çevre bilinci aşılamaya çalışmak kadar, doğru davranışı kolaylaştıracak düzenlemeler yapmak da gereklidir.',
 'Geri dönüşümün ekonomiye katkısından söz edilmiştir.','Parçada geri dönüşümün ekonomik sonuçlarına hiç değinilmez.',
 [('Davranışların oluşmasında altyapının etkili olduğu belirtilmiştir.','Parçada karşılığı var: asıl belirleyici “kentin altyapısıdır”.'),
  ('Toplama kutusunun uzaklığıyla ilgili bir vazgeçme örneği verilmiştir.','Parçada karşılığı var: kutuyu “on dakika uzakta bulan kişi” vazgeçer.'),
  ('Çevre bilinci aşılamanın tek başına yetmeyebileceği anlatılmıştır.','Parçada karşılığı var: düzenleme yapmak da “gereklidir”.'),
  ('Geri dönüşümün bireysel bir erdem gibi sunulduğuna değinilmiştir.','Parçada karşılığı var: ilk cümle böyle der.')],
 'Parçada geri dönüşümün hangi yönü hiç işlenmiyor?','Parça altyapıyı, kutu uzaklığını, bilinç ve düzenlemeyi ve erdem anlayışını işler. Ekonomik katkı parçada geçmez.','Parçada işlenmeyen noktayı belirler.')
S('0015','pab-degenilmemis','orta','E',
 'Çoğu öğrenci, hoca ne söylediyse not defterine geçirmenin en güvenli yol olduğuna inanır. Derste not tutan öğrenci, dinlediği her şeyi yazmaya çalıştığında genellikle anlamayı kaçırır; elinin hızına yetişmek için kulağı gevşer. Daha iyi bir yol, öğretmenin söylediklerini kendi cümleleriyle kısaltarak yazmaktır. Böylece öğrenci hem anlamak hem de seçmek zorunda kalır. Not tutma, bu yüzden bir yazı yarışı değil, düşünerek yapılan bir ayıklama işidir. Ders sonrasında bu notlara bir kez daha göz atmak, bilginin kalıcı olmasını da kolaylaştırır.',
 'Not tutmanın derse katılımı artırdığı ifade edilmiştir.','Parçada not tutmanın derse katılıma etkisinden söz edilmez.',
 [('Her şeyi yazmaya çalışmanın dinlemeyi zayıflattığı söylenmiştir.','Parçada karşılığı var: öğrencinin “kulağı gevşer”.'),
  ('Notların kendi cümleleriyle kısaltılarak yazılması önerilmiştir.','Parçada karşılığı var: ikinci cümle bunu önerir.'),
  ('Not alırken ayıklama yapmak gerektiğine dikkat çekilmiştir.','Parçada karşılığı var: öğrenci “hem anlamak hem de seçmek zorunda kalır”.'),
  ('Notlara ders sonrasında dönmenin yararı belirtilmiştir.','Parçada karşılığı var: son cümle bilginin kalıcılığına değinir.')],
 'Parçada not tutmanın hangi sonucu hiç anılmıyor?','Parça dinlemeyi, kısaltmayı, seçmeyi ve tekrarı işler. Derse katılım konusu geçmez.','Parçada işlenmeyen noktayı belirler.')
S('0016','pab-degenilmemis','orta','C',
 'Eski kent dokularındaki dar sokaklar, ilk bakışta modern ulaşımın düşmanı gibi görünür. Oysa bu sokaklar araçları yavaşlatır, yürümeyi ve sohbet etmeyi özendirir; çocuklar sokakta oynayabilir. Böyle bir sokakta komşular pencereden seslenerek bile selamlaşabilir. Genişletilen her yol ise bir süre sonra daha fazla araç çeker ve yaya, kendi mahallesinde konuk gibi kalır. Kimi kent planlamacıları, genişliği bir kazanç saymanın aldatıcı olduğunu söyler. Kimi kentler bu yüzden en dar sokaklarını koruma altına almaktadır.',
 'Dar sokakların acil durumlarda sorun yarattığı söylenmiştir.','Parçada dar sokakların acil durumlardaki sakıncalarına hiç değinilmez.',
 [('Dar sokakların araç hızını düşürdüğü ifade edilmiştir.','Parçada karşılığı var: sokaklar “araçları yavaşlatır”.'),
  ('Dar sokakların çocuklara oyun alanı olabildiği belirtilmiştir.','Parçada karşılığı var: “çocuklar sokakta oynayabilir”.'),
  ('Yolların genişletilmesinin araç sayısını artırabileceği söylenmiştir.','Parçada karşılığı var: genişletilen yol “daha fazla araç çeker”.'),
  ('Dar sokaklara ilk bakışta olumsuz yaklaşıldığına değinilmiştir.','Parçada karşılığı var: ilk cümle sokakların “düşman gibi göründüğünü” söyler.')],
 'Dar sokaklarla ilgili hangi sakınca parçada yok?','Parça dar sokakların yararlarını sayar ve sakıncalarından yalnızca ilk bakıştaki izlenim olarak söz eder. Acil durum konusu hiç geçmez.','Parçada işlenmeyen noktayı belirler.')
S('0017','pab-degenilmemis','zor','D',
 'Fotoğrafın icadı başlangıçta resmin sonu olarak görülmüştü; gerçeği olduğu gibi kaydedebilen bir makine varken ressamın elinin ne anlamı kalırdı? Beklenen olmadı. Nitekim ilk fotoğrafçılar bile çoğu zaman ressamların bıraktığı kompozisyon kurallarıyla çalışıyordu. Ressamlar, kameranın yapabildiğini yapmaktan vazgeçtiler ve kameranın yapamadığına, yani görünenin ardındaki duyguya yöneldiler. Müzelerde asılan tabloların önünde insanlar, bir resmin ne kadar uzun sürede yapıldığını değil, ne söylediğini sormaya başladı. Öte yandan fotoğrafın kendisi de zamanla bir sanat dalı olarak kabul gördü; çünkü hangi anın, hangi açıdan, hangi ışıkta tutulacağına karar veren kişi, makineden çok bir göz ve bir tercihti. Böylece iki sanat birbirinin yerine geçmedi, birbirini yeniden tanımladı.',
 'Fotoğraftan sonra resim satışlarının düştüğüne yer verilmiştir.','Parçada resim satışlarından ya da piyasadan hiç söz edilmez; tehdit algısı yalnızca bir beklenti olarak geçer.',
 [('Fotoğrafın icadının resim için bir tehdit sayıldığı belirtilmiştir.','Parçada karşılığı var: icat “resmin sonu olarak görülmüştü”.'),
  ('Ressamların kameranın yapamadığı alana yöneldiği anlatılmıştır.','Parçada karşılığı var: ressamlar “görünenin ardındaki duyguya yöneldi”.'),
  ('Fotoğraf çekerken yapılan tercihlerin sanatsal değer taşıdığına işaret edilmiştir.','Parçada karşılığı var: anı, açıyı ve ışığı seçen kişinin “bir göz ve bir tercih” olduğu söylenir.'),
  ('Fotoğraf ile resmin birbirini yeniden tanımladığı söylenmiştir.','Parçada karşılığı var: son cümle bunu söyler.')],
 'Parçada resmin uğradığı olumsuz sonuç neyle anlatılıyor?','Parça resmin tehdit sanıldığını ama beklenenin olmadığını anlatır; satışların düşmesi konusu geçmez. Diğer dört şık parçadaki cümlelerle eşleşir.','Tehdit algısı ile somut bir sonucu karıştırmamayı sağlar.')
S('0018','pab-degenilmemis','zor','B',
 'Övgü, doğru verildiğinde güçlü bir motivasyon aracıdır; ancak yanlış verildiğinde tersine çalışır. Çocuğa “Çok zekisin” demek, başarıyı doğuştan gelen bir niteliğe bağlar ve çocuk, zor bir işle karşılaştığında bu imajı kaybetme korkusuyla denemekten kaçınabilir. Nitekim kendisine hep başarılı olduğu söylenen çocuk, ilk kez zorlandığında bunu bir yetersizlik belirtisi sayabilir. “Çok çalıştın, bu iş sana yaradı” demek ise çabayı öne çıkarır ve çocuğu yeniden denemeye iter. Çabası görülen çocuk ise zorluğu geçici ve aşılabilir bir durum olarak karşılar. Yani övgünün etkisi, övülenin kim olduğuna değil, neyin övüldüğüne bağlıdır. Bu ayrım, övgüyü azaltmayı değil, daha özenli seçmeyi gerektirir. Çünkü çocuk, kendisine söylenen sözden kendine dair bir hüküm çıkarır.',
 'Övgünün yetişkinler üzerinde de etkili olduğuna değinilmiştir.','Parça yalnızca çocuğa yönelik övgüyü işler; yetişkinlerden söz etmez.',
 [('Övgünün hem yararlı hem zararlı olabildiği ifade edilmiştir.','Parçada karşılığı var: övgü doğru verilirse motivasyon, yanlış verilirse tersine işler.'),
  ('Başarıyı doğuştan bir niteliğe bağlamanın riskine işaret edilmiştir.','Parçada karşılığı var: çocuk “imajı kaybetme korkusuyla” denemekten kaçınabilir.'),
  ('Çabanın övülmesinin yeniden denemeyi desteklediği vurgulanmıştır.','Parçada karşılığı var: çabayı öne çıkarmak “yeniden denemeye iter”.'),
  ('Övgünün etkisinin neyin övüldüğüne göre değiştiği belirtilmiştir.','Parçada karşılığı var: dördüncü cümle bunu söyler.')],
 'Parçadaki örnekler kimi hedef alıyor?','Parça övgünün etkisini çocuk örneği üzerinden anlatır; yetişkinlere hiç geçmez. Diğer dört şık parçada yer alır.','Parçanın kapsamını aşan noktayı ayırır.')
# ===================== ÖNCÜLLÜ =====================
O('0019','kolay','C',
 'Yaşlıların teknolojiyi öğrenemediği düşüncesi yaygındır; oysa onları teknolojiden uzak tutan şey çoğu zaman yeteneksizlik değil, acele eden öğreticilerdir. Bir telefonun ayarını ilk kez gösteren torununun hızına yetişemeyen yaşlı kişi, kendini beceriksiz sanır ve denemeyi bırakır. Oysa kendi hızında ilerlemesine izin verilen yaşlılar, uygulamaları çoğu zaman şaşırtıcı bir çabuklukla öğrenir. Sabırla, adım adım gösterildiğinde aynı kişi, bir mesajı birkaç gün içinde rahatça gönderir.',
 [('Yaşlıların teknolojiden uzak kalmasında öğretim biçimi etkili olabilir.',True,'öğreticilerin acelesi engel olarak gösterilir'),
  ('Yaşlılar teknolojiyi öğrenmek için hiçbir yardıma gereksinim duymaz.',False,'parça sabırlı gösterimin işe yaradığını söyler, yardımı gereksiz saymaz'),
  ('Sabırlı bir öğretim, yaşlının teknolojiyi kullanmasını kolaylaştırır.',True,'adım adım gösterilince mesaj rahatça gönderilir')],
 'Her öncülü parçadaki cümleyle karşılaştır.','Parça yaşlıların teknolojiden kopmasını öğretim biçimine bağlar; I ve III bu çerçevede çıkarılır. II parçadaki sabırlı gösterim vurgusuyla çelişir.','Öncüllerin her birini ayrı sınar.')
O('0020','orta','A',
 'Bir çalgıyı öğrenmek, parmaklara olduğu kadar kulağa da ders verir. Çalgı çalan çocuk, sesler arasındaki küçük farkları ayırt etmeyi öğrenir; bu beceri başka alanlara da sızar ve örneğin yabancı dildeki ses ayrımlarını kavramayı kolaylaştırır. Piyano başında geçen ilk aylarda en çok yorulan şey, çoğu zaman parmaklar değil kulaktır. Ne var ki bu kazanç düzenli çalışmayı gerektirir; haftada bir kez elini çalgıya süren çocuğun kulağı fazla gelişmez.',
 [('Çalgı çalmak, çocukların bütün derslerdeki başarısını artırır.',False,'parça yalnızca ses ayrımı becerisinden ve bir örnek olarak yabancı dilden söz eder'),
  ('Çalgı eğitimiyle gelişen kulak becerisi, müzik dışı alanlarda da işe yarayabilir.',True,'beceri “başka alanlara da sızar”'),
  ('Çalgı çalmaya başlamak için en uygun dönem çocukluktur.',False,'parçada uygun yaş dönemine ilişkin bir yargı yoktur')],
 'Öncülleri parçada geçen ifadelerle eşle; abartıyı ayıkla.','Parça kulak gelişiminin başka alanlara yansıyabildiğini söyler; yalnızca II çıkarılır. I abartıdır, III parçada geçmez.','Abartılan ve olmayan yargıyı ayıklar.')
O('0021','orta','D',
 'Tarihî binaları müzeye çevirmek, onları korumanın en yaygın yolu sayılır. Oysa kapısı yalnızca ziyaret saatlerinde açılan bir bina, zamanla kentin gündelik yaşamından kopar. Aynı yapı bir kütüphane, bir kafe ya da bir atölye olarak kullanıldığında ise insanlar ona sürekli uğrar ve onun bakımına da gönüllü sahip çıkar. Elbette her yapı yeni bir işleve uygun değildir; taşıyıcı sistemi bozulacak bir binada bu denenmemelidir.',
 [('Müzeye dönüştürme, bir yapının kentle bağını zayıflatabilir.',True,'ziyaret saatleri dışında kapalı bina gündelik yaşamdan kopar'),
  ('Tarihî yapıya yeni işlev seçilirken yapının durumu gözetilmelidir.',True,'taşıyıcı sistemi bozulacak binada yeni işlev denenmemelidir'),
  ('Müzeye çevirme, tarihî yapıyı korumanın en etkisiz yoludur.',False,'parça müzeyi “en yaygın” yol sayar, etkisiz olduğunu söylemez')],
 'Her yargının parçada hangi cümleye dayandığını ara.','Parça müze dönüşümünün kentle bağı zayıflatabildiğini ve yapının durumuna bakılması gerektiğini söyler; I ve II çıkarılır. “En etkisiz yol” parçada yoktur.','Yaygın olmak ile etkisiz olmak arasındaki farkı ayırt eder.')
O('0022','orta','E',
 'Mektup yazmak, düşünceyi yavaşlatan bir iştir. Yazan kişi, cümleyi gönderdikten sonra geri alamayacağını bilir ve sözünü tartarak seçer. Kâğıda dökülen bir öfke, bir gece beklese çoğu zaman yumuşar. Anlık mesajlaşmada ise düşünce, ağızdan çıktığı hızla ekrana düşer; bu hız samimiyet kazandırır ama özen kaybettirir. Bu iki yazışma biçimi birbirinin yerini almaz, farklı ihtiyaçlara hizmet eder; hızlı bir haber için mesaj, uzun bir hesaplaşma için mektup uygundur.',
 [('Mektup, anlık mesajlaşmanın yerini almıştır.',False,'parça iki biçimin birbirinin yerini almadığını söyler'),
  ('Anlık mesajlaşmanın hızı, yazışmaya samimiyet katabilir.',True,'“bu hız samimiyet kazandırır”'),
  ('Uzun bir hesaplaşma için mektup uygun görülebilir.',True,'son cümlede uzun hesaplaşma için mektup önerilir')],
 'Parçada her iki yazışma biçimine verilen değeri ayır.','Parça mesajın hızına samimiyet, mektubun uzun hesaplaşmalara uygunluk payı verir; II ve III çıkarılır. I parçaya terstir.','Parçaya ters yargıyı ayıklar.')
O('0023','zor','E',
 'Bir hikâyeyi anlatan kişi, hikâyenin yalnızca aktarıcısı değildir; neyi anlatacağına, neyi atlayacağına ve hangi sırayla söyleyeceğine o karar verir. Bu yetki, anlatıcıya görünmez bir güç verir: Bir kişiyi sevimli ya da sevimsiz kılmak, çoğu zaman yalnızca onu hangi sahnede gösterdiğine bağlıdır. Aynı olay, iki farklı anlatıcının ağzından iki ayrı hikâye olur. Tarih kitaplarında bile aynı savaşı iki farklı ülkenin farklı anlatması, bu durumun sık anılan bir örneğidir. Bu yüzden okur, anlatılanı gerçeğin kendisi sanmamalı, anlatıcının seçtiği bir gerçek olarak okumalıdır. Okurun işi, bu seçimlerin ardındaki sesi duymaktır. Ne var ki bu durum, hikâyenin değerini azaltmaz: Anlatıcının seçimleri, hikâyeyi yaşatan asıl dokudur.',
 [('Anlatıcı, olayların hangi sırayla verileceğini belirleyebilir.',True,'sırayı “o karar verir”'),
  ('Aynı olay, farklı anlatıcıların elinde farklı hikâyelere dönüşebilir.',True,'aynı olay “iki ayrı hikâye olur”'),
  ('Anlatıcının seçimleri, bir hikâyenin değerini belirleyen önemli bir öğedir.',True,'seçimler hikâyeyi yaşatan “asıl doku” sayılır')],
 'Her yargı parçada başka sözcüklerle söylenmiş olabilir; dayanak ara.','Üç yargı da parçadaki cümlelerin başka sözcüklerle ifadesidir: seçim yetkisi, aynı olayın farklı hikâyeleri ve seçimlerin hikâyedeki önemi.','Aynı düşüncenin başka sözcüklerle ifadesini tanır.')
O('0024','zor','A',
 'Sınav kaygısı çoğu zaman olumsuz bir duygu olarak görülür; oysa belli bir düzeyin altındaki kaygı kişiyi hazırlıksız bırakır. Kaygının dozu bir kez ayarlandığında, sınav günü heyecanı bile işe yarar hâle gelir; titreyen eller soruyu okumaya engel olmaz. Hiç heyecan duymayan öğrenci çalışmayı gereksiz bulabilir. Sorun, kaygının varlığı değil, kişinin çalışmasını engelleyecek kadar büyümesidir. Bu noktada işe yarayan şey kaygıyı yok etmeye çalışmak değil, ona bir yön vermektir: Kaygıyı konu listesine, günlük çalışma planına dönüştüren öğrenci onu bir yakıt olarak kullanır. Öğretmenlerin ve ailelerin “Sakın heyecanlanma” demesi çoğu zaman kaygıyı azaltmaz, çünkü öğrenci bu kez kaygılı olduğu için de kaygılanır. Kısacası kaygı, doğru kanala akıtıldığında düşman değil müttefiktir.',
 [('Kaygının hiç bulunmaması, hazırlıksızlığa yol açabilir.',True,'hiç heyecan duymayan öğrenci çalışmayı gereksiz bulabilir'),
  ('Sınav kaygısını gidermenin en etkili yolu sınavdan önce dinlenmektir.',False,'parça kaygıyı gidermeyi değil yönlendirmeyi önerir; dinlenmeden söz etmez'),
  ('Aşırı kaygı yaşayan öğrenci çalışma planı yapamaz.',False,'parça aşırı kaygının çalışmayı engelleyebileceğini söyler; plan yapılamayacağını söylemez')],
 'Parçanın kaygıya yönelik yaklaşımını belirle, sonra öncülleri sına.','Parça hiç kaygı duymamanın da sorun olduğunu söyler; yalnız I çıkarılır. II parçada yoktur, III parçadaki “engelleyebilir” ifadesini abartır.','Abartıyı ve parçada olmayan öneriyi ayıklar.')
O('0025','zor','B',
 'Kent bahçeleri, boş kalmış arsaların sebze yetiştirilen küçük tarlalara dönüştürülmesiyle ortaya çıkar. Bu bahçelerde çoğu zaman bir kişinin parseli, öteki kişinin sulama saatini belirler; alet çantası ortak, su borusu ortak, takvim ortaktır. İlk bakışta bu uygulamanın amacı gıda üretimi sanılır; ancak bahçelerde yetişen sebzenin kente sağladığı katkı sınırlıdır. Hasat edilen sebze market fiyatından çok daha pahalıya mal olsa da kimse bundan yakınmaz. Asıl işlev, birbirini tanımayan insanların aynı toprağı paylaşırken kurduğu ilişkidir. Bahçe yönetiminde ortaya çıkan küçük anlaşmazlıklar bile komşuluğun öğrenildiği bir ortam sağlar. Kış gelip bahçe boşaldığında bile komşular birbirinin ismini bilir ve sokakta selamlaşır. Bahçeye ilk kez gelen biri, tohum ekmeyi komşusundan öğrenir.',
 [('Kent bahçeleri, kentin gıda gereksinimini büyük ölçüde karşılar.',False,'parça sebzenin kente katkısını “sınırlı” bulur'),
  ('Kent bahçeleri yalnızca kentte yaşayan emeklilere yöneliktir.',False,'parçada bahçeleri kullananların yaşına ilişkin bir yargı yoktur'),
  ('Kent bahçeleri, insanlar arasındaki ilişkileri güçlendirebilir.',True,'asıl işlev tanımayan insanların kurduğu ilişkidir')],
 'Parçanın “asıl işlev” dediği şeyi bul, öncülleri onunla karşılaştır.','Parça bahçelerin asıl işlevini insan ilişkilerinde görür; yalnız III çıkarılır. I parçaya terstir, II parçada geçmez.','Parçaya ters ve parçada olmayan yargıyı ayıklar.')
# ===================== SÖYLENEBİLİR =====================
S('0026','pab-soylenebilir','kolay','E',
 'Kütüphaneler yalnızca kitap ödünç alınan yerler değildir. Sessiz çalışma masaları, çocuk okuma saatleri, yaşlılar için düzenlenen söyleşiler ve internet erişimi sayesinde her yaştan insan için bir buluşma noktası hâline gelmiştir. Birçok kütüphane artık akşam saatlerine kadar açık kalmakta ve ücretsiz kurslara da ev sahipliği yapmaktadır. Sabahın erken saatlerinde bile okuma salonunda yer bulmak güçtür. Bu çeşitlilik, kütüphanelerin dijital çağda bile ziyaretçi kaybetmemesine yardım eder.',
 'Kütüphaneler farklı yaş gruplarına yönelik hizmetler sunar.','Parça çocuk saatlerini, yaşlı söyleşilerini ve her yaştan insanın buluşma noktası olmasını anlatır.',
 [('Kütüphaneler dijital çağda önemini tümüyle yitirmiştir.','Parça kütüphanelerin dijital çağda bile ziyaretçi kaybetmemesine yardım edildiğini söyler; şık parçaya terstir.'),
  ('Kitap ödünç vermek, kütüphanelerin tek işlevidir.','Parça ilk cümlede kütüphanelerin yalnızca ödünç kitap yeri olmadığını söyler; şık parçaya terstir.'),
  ('Kütüphanelere en çok ilgiyi çocuklar göstermektedir.','Parçada hangi yaş grubunun daha çok geldiğine dair karşılaştırma yoktur.'),
  ('Yaşlıların kütüphane etkinliklerine katılımı azalmaktadır.','Parçada katılımın azaldığına ilişkin bir bilgi yoktur; yaşlılar için söyleşi düzenlendiği söylenir.')],
 'Parçadaki sayılan hizmetlere bak: hangi yaş gruplarına yöneliyor?','Parça çocuklara, yaşlılara ve her yaştan insana yönelik hizmetleri sayar. Yanlış şıklar parçaya terstir ya da parçada olmayan karşılaştırmalar getirir.','Parçanın doğrudan söylediğini seçer.')
S('0027','pab-soylenebilir','kolay','A',
 'Çocuklar aynı masalı defalarca dinlemek ister ve anlatıcı bir yerde sapıtsa hemen uyarır. Gece uyumadan önce istenen masal çoğu zaman bir gün öncekiyle aynıdır. Yetişkinler bunu sıkıcı bulabilir; oysa çocuk için tekrar bir sıkıntı değil güvencedir. Ne olacağını bilmek, korkutucu bölümleri bile katlanılır kılar ve çocuğun dünyayı öngörebildiği bir yer olarak görmesine yardım eder. Ebeveynler kimi zaman sıkılır, ama çocuk bu tekrar sayesinde rahatlayıp uykuya dalar.',
 'Çocuğa tanıdık olan, güven duygusu verir.','Parça tekrarın çocuk için “güvence” olduğunu, ne olacağını bilmenin korkuyu katlanılır kıldığını söyler.',
 [('Çocuklar yeni masallara karşı ilgisizdir.','Parça çocukların tanıdık masalı sevdiğini söyler; yeni masallara ilgisiz olduklarını söylemez.'),
  ('Korkutucu bölümler masallardan çıkarılmalıdır.','Parça korkutucu bölümlerin tanıdık olunca katlanılır hâle geldiğini söyler; çıkarılmasını önermez.'),
  ('Çocuklar yetişkinlerden daha iyi masal anlatır.','Parçada çocukların masal anlatma becerisine ilişkin bir yargı yoktur.'),
  ('Tekrarlanan masallar çocuğun hayal gücünü zayıflatır.','Parça tekrarı sıkıntı değil güvence sayar; hayal gücüne etkisinden söz etmez.')],
 'Parça çocuk için tekrarı ne olarak niteliyor?','Parça tekrarı güvence olarak niteler; doğru şık bunu genelleyerek söyler. Diğer şıklar parçada olmayan ya da parçaya ters yargılardır.','Parçanın doğrudan söylediğini seçer.')
S('0028','pab-soylenebilir','orta','D',
 'Büyük kentlerde gece gökyüzüne bakan biri, çoğu zaman birkaç yıldızdan fazlasını göremez. Bunun nedeni hava kirliliğinden çok, kentin aydınlatma düzenidir: yukarı doğru saçılan ışık, gökyüzünü soluk bir parlaklıkla örter. Yıldız görememek insanlar için yalnızca bir estetik kayıp değildir; geceleri yön bulmak için gökyüzüne bakan göçmen kuşların da yolunu şaşırmasına yol açar. Armatürlerin ışığı aşağı yönlendirecek biçimde tasarlanması, sorunu büyük ölçüde hafifletir.',
 'Kent ışığı, insanların yanı sıra kuşları da olumsuz etkiler.','Parça yıldız görememenin “yalnızca estetik kayıp” olmadığını, göçmen kuşların yolunu şaşırttığını söyler.',
 [('Kentlerde yıldızların az görünmesinin asıl nedeni hava kirliliğidir.','Parça nedenin “hava kirliliğinden çok aydınlatma düzeni” olduğunu söyler; şık parçaya terstir.'),
  ('Göçmen kuşlar yön bulmak için yalnızca yıldızlara başvurur.','Parça kuşların gökyüzüne baktığını söyler; “yalnızca yıldız” abartısı parçada yoktur.'),
  ('Armatür tasarımı değişse bile sorun azalmaz.','Parça tasarımın sorunu “büyük ölçüde hafiflettiğini” söyler; şık parçaya terstir.'),
  ('Yıldız görememek yalnızca estetik bir sorun sayılmalıdır.','Parça tam tersini söyler: sorun yalnızca estetik değildir.')],
 'Parçada yıldız görememenin sonuçları neler?','Parça yıldız görememenin kuşları da etkilediğini söyler; doğru şık bunu ifade eder. Diğerleri parçaya ters ya da parçayı abartan yargılardır.','Abartılan ve ters yargıyı ayırır.')
S('0029','pab-soylenebilir','orta','B',
 'Usta–çırak ilişkisinde bilgi, kitaptan değil el hareketinden öğrenilir. Çırak, ustasının bir işi nasıl yaptığını izler, yanlış yaptığında düzeltilir ve yıllar içinde ustanın bakışını da edinir. Fırının ya da tamirhanenin kapısından giren çırak, ilk günlerde çoğu zaman yalnızca süpürür ve izler. Bu öğrenme biçimi bir ders programına sığmaz, çünkü neyin ne zaman öğretileceği önceden belirlenmemiştir. Bunun bedeli yavaşlıktır; karşılığında ise okulda kolay aktarılamayan bir “iş sezgisi” kazanılır.',
 'Okulda aktarılması güç bir sezgi, bu yöntemle kazanılır.','Parça son cümlede “okulda kolay aktarılamayan bir iş sezgisi” kazanıldığını söyler.',
 [('Usta–çırak yöntemi okul eğitiminden daha verimlidir.','Parça iki yöntemi verimlilik bakımından karşılaştırmaz; yalnızca usta–çırak yönteminin bedelinin yavaşlık olduğunu söyler.'),
  ('Çırak ustasının yöntemini sorgulamadan benimsemek zorundadır.','Parçada çırağın sorgulama hakkına ilişkin bir yargı yoktur.'),
  ('Usta–çırak ilişkisinde öğrenme süresi kısadır.','Parça bu yöntemin bedelinin “yavaşlık” olduğunu söyler; şık parçaya terstir.'),
  ('Bu yöntemde öğretilecekler önceden bir programla belirlenir.','Parça neyin ne zaman öğretileceğinin önceden belirlenmediğini söyler; şık parçaya terstir.')],
 'Parçada usta–çırak yönteminin bedeli ve kazancı nedir?','Parça bedeli yavaşlık, kazancı okulda aktarılamayan iş sezgisi olarak gösterir. Yanlış şıklar parçaya terstir ya da parçada olmayan karşılaştırmalar getirir.','Parçanın doğrudan söylediğini seçer.')
S('0030','pab-soylenebilir','orta','C',
 'Tiyatroyu sinemadan ayıran şey, oyuncu ile seyircinin aynı odada, aynı anda soluk almasıdır. Sinemada film önceden çekilmiştir ve her gösterimde aynıdır; tiyatroda ise oyuncunun yorgunluğu, salonun sessizliği ya da bir öksürük bile o akşamın oyununu değiştirebilir. Bu nedenle aynı oyun iki akşam arka arkaya izlense de iki ayrı deneyim olur. Kimi oyuncular, perde açılmadan önce kulise sızan seyirci uğultusundan o akşamın nasıl geçeceğini sezdiğini söyler.',
 'Aynı tiyatro oyunu farklı akşamlarda birebir aynı olmayabilir.','Parça aynı oyunun iki akşamda “iki ayrı deneyim” olduğunu söyler.',
 [('Sinema, seyirciyle kurduğu bağ bakımından tiyatrodan daha zayıftır.','Parça iki sanatı farklı gösterir ama birini bağ bakımından üstün ya da zayıf saymaz.'),
  ('Tiyatroda oyuncunun hataları seyirci tarafından bağışlanmaz.','Parçada seyircinin oyuncu hatalarına tepkisine ilişkin bir yargı yoktur.'),
  ('Seyircinin tepkisi oyunun metnini değiştirir.','Parça oyunun akışının o akşama göre değişebileceğini söyler; metnin değiştiğini söylemez.'),
  ('Tiyatro, sinemadan daha eski bir sanat dalıdır.','Parçada iki sanatın tarihine ilişkin bir yargı yoktur.')],
 'Parça iki akşam izlenen aynı oyun için ne diyor?','Parça aynı oyunun iki akşamda iki ayrı deneyim olduğunu söyler; bu, oyunun birebir aynı olmayabileceği anlamına gelir. Diğer şıklar parçada olmayan karşılaştırmalar ya da abartılardır.','Parçanın doğrudan söylediğini seçer.')

Q.P.ANA.sort(key=lambda q:q['id'])
# kitap benzeri kalıp ve çeşitlilik denetimi
from collections import Counter
bitir(Q)
print('tip',dict(Counter(q['tip'] for q in Q.P.ANA)))
