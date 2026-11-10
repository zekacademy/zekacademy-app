"""TYT Türkçe · Paragraf (ana düşünce / konu / başlık / yazarın amacı): 50 ana soru (hafif mod). Metinler özgündür.
Her şıkka etiket verilir; tek doğru şık assert edilir. Parça 1: 0001–0025, parça 2: 0026–0050."""
import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Paraf İQ · Sıfır Risk'
KARTLAR={
 'K-PNA-01':dict(alt='Ana Düşünce',fikir='Giriş ya da sonuç cümlesinde belirgin olan temel mesajı, ayrıntı ve örnekten ayırıp parçanın tamamını kapsayan yargı olarak seçmek.',tuzak='Parçada geçen bir ayrıntıyı ana düşünce sanmak; “her, yalnızca, hiçbir” gibi sözcüklerle genellenmiş ya da parçaya ters yargıyı seçmek.',zorluk='kolay',kalip='düz',adim=2,tipId='pana-ana',kaynak=KY),
 'K-PNA-02':dict(alt='Ana Düşünce',fikir='Karşıtlık bağlacından (oysa, ama, ne var ki) sonra gelen asıl iddiayı, öncesindeki eleştirilen görüşten ve örneklerden ayırarak bulmak.',tuzak='Eleştirilen görüşü ya da destekleyici örneği ana düşünce saymak; parçanın yalnız bir bölümünü kapsayan yargıda durmak.',zorluk='orta',kalip='düz',adim=3,tipId='pana-ana',kaynak=KY),
 'K-PNA-03':dict(alt='Ana Düşünce',fikir='Parçada doğrudan söylenmeyen, iddia–gerekçe–örnek ilişkisinden çıkan sonuç yargısını bulmak; iki şıktan birinin parçanın yalnız bölümünü kapsadığını görmek.',tuzak='Parçanın bir bölümünü kapsayan şıkkı tümünü kapsıyor sanmak; “her zaman, tümüyle” ile aşırılaştırılmış yargıya kapılmak.',zorluk='zor',kalip='düz',adim=4,tipId='pana-ana',kaynak=KY),
 'K-PNA-04':dict(alt='Konu',fikir='Parçanın neyi, hangi yönden anlattığını bulup ne çok geniş ne çok dar olan, parçanın tamamını karşılayan adlandırmayı seçmek.',tuzak='Yan konuyu ya da bir örneği konu sanmak; konuya yakın ama parçada işlenmeyen ifadeyi seçmek; yargı cümlesiyle konuyu karıştırmak.',zorluk='orta',kalip='düz',adim=3,tipId='pana-konu',kaynak=KY),
 'K-PNA-05':dict(alt='Konu',fikir='Birden çok yönü olan parçada tüm yönleri bir arada karşılayan konu ifadesini, yalnız bir yönü anan şıklardan ayırmak.',tuzak='Parçanın bir bölümünü anlatan şıkkı konunun tamamı sanmak.',zorluk='zor',kalip='düz',adim=4,tipId='pana-konu',kaynak=KY),
 'K-PNA-06':dict(alt='Başlık',fikir='Parçanın konusunu ve vurgusunu kısa bir adla özetleyen başlığı seçmek; başlık parçayı ne daraltmalı ne taşmalı.',tuzak='Parçadaki bir örneği ya da ayrıntıyı başlık yapmak; çok geniş başlığı uygun sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='pana-baslik',kaynak=KY),
 'K-PNA-07':dict(alt='Yazarın Amacı',fikir='Yazarın parçayı hangi düşünceyi vurgulamak için yazdığını, parçadaki karşıtlık ve sonuç ifadelerinden çıkarmak.',tuzak='Parçada geçen bir bilgiyi yazarın amacı saymak; amacı aşırı genelleyen şıkka kapılmak.',zorluk='orta',kalip='düz',adim=3,tipId='pana-amac',kaynak=KY),
 'K-PNA-08':dict(alt='Yazarın Amacı',fikir='Yazarın eleştirdiği görüşü ve savunduğu görüşü ayırıp parçanın tamamında vurgulanan yargıyı, yarım doğru içeren şıklardan ayırmak.',tuzak='Parçadaki örnekten ya da yarım doğrudan amaç çıkarmak; yazarın eleştirdiği yargıyı yazarın görüşü sanmak.',zorluk='zor',kalip='düz',adim=4,tipId='pana-amac',kaynak=KY),
}
TIPLER={'pana-ana':'Ana düşünce / asıl anlatılmak istenen','pana-konu':'Konu','pana-baslik':'Başlık önerme','pana-amac':'Yazarın amacı / vurgulanan yargı'}
Q=kur('pana','Paragraf','tr|Paragraf',KARTLAR,TIPLER); Q.n=25
BI={
 'ana':[B('Ana düşünce','yazarın parçanın tamamında okura vermek istediği temel mesajdır; genellikle giriş ya da sonuç cümlesinde (“bu yüzden, oysa, sonuç olarak” gibi bağlaçlarla) toplanır. Örnek: “Düzenli çalışan başarır.”'),
        B('Ayrıntı ve ana düşünce','örnekler ve sayılan bilgiler ana düşünceyi destekler; parçanın yalnız bir bölümünü anlatan ya da “her, yalnızca, hiçbir” ile genelleyen şık ana düşünce olmaz')],
 'konu':[B('Konu','parçada “neyin” anlatıldığıdır ve genellikle bir ad ya da ad tamlamasıyla belirtilir. Örnek: “Mercan resiflerinin deniz yaşamındaki rolü”'),
         B('Konu ve ana düşünce','konu bir adlandırmadır, ana düşünce ise bir yargıdır; konu şıkları parçada işlenen tüm yönleri karşılamalı, ne çok geniş ne çok dar olmalıdır')],
 'baslik':[B('Başlık','parçanın konusunu ve vurgusunu kısa biçimde özetleyen addır. Örnek: Parça leyleklerin yolculuğunu anlatıyorsa “Leyleklerin Göç Yolculuğu” uygundur'),
           B('İyi başlık','parçanın tamamını kapsar; bir örneğe ya da ayrıntıya dayanan başlık dar, parçada işlenmeyeni çağrıştıran başlık yanlıştır')],
 'amac':[B('Yazarın amacı','yazarın parçada okura neyi göstermek, neyi savunmak ya da neyi eleştirmek istediğidir. Karşıtlık bağlaçları (oysa, ama) ve sonuç cümleleri amacı gösterir'),
         B('Vurgulanan yargı','yazar bir görüşü eleştirip bir görüşü öne çıkarıyorsa vurgulanan yargı, öne çıkarılandır; yazarın eleştirdiği ya da yalnız örnekle andığı yargı amaç değildir')],
}
KOK={'ana':['Bu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?','Bu parçanın ana düşüncesi aşağıdakilerden hangisidir?','Bu parçada vurgulanmak istenen temel düşünce aşağıdakilerden hangisidir?'],
     'konu':['Bu parçanın konusu aşağıdakilerden hangisidir?','Bu parçada üzerinde durulan konu aşağıdakilerden hangisidir?'],
     'baslik':['Bu parça için aşağıdakilerden hangisi başlık olarak getirilebilir?','Bu parçaya getirilebilecek en uygun başlık aşağıdakilerden hangisidir?'],
     'amac':['Yazar, bu parçada aşağıdakilerden hangisini vurgulamak istemiştir?','Bu parçada yazarın asıl amacı aşağıdakilerden hangisidir?']}
TIPID={'ana':'pana-ana','konu':'pana-konu','baslik':'pana-baslik','amac':'pana-amac'}
KAZ={'ana':'Paragrafın ana düşüncesini belirler.','konu':'Paragrafın konusunu belirler.','baslik':'Paragrafa uygun başlığı belirler.','amac':'Yazarın amacını ve parçanın vurguladığı yargıyı belirler.'}
KARTSEC={('ana','kolay'):'K-PNA-01',('ana','orta'):'K-PNA-02',('ana','zor'):'K-PNA-03',('konu','kolay'):'K-PNA-04',('konu','orta'):'K-PNA-04',('konu','zor'):'K-PNA-05',
         ('baslik','kolay'):'K-PNA-06',('baslik','orta'):'K-PNA-06',('baslik','zor'):'K-PNA-06',('amac','kolay'):'K-PNA-07',('amac','orta'):'K-PNA-07',('amac','zor'):'K-PNA-08'}
ETK={'D':'doğru ✓','yan':'yan düşünce','ters':'parçaya ters','genel':'fazla genel','yok':'parçada yok','dar':'yalnız bir bölüm'}
ADIM3={'ana':'Her şıkkı parçayla karşılaştır; yalnız tümünü kapsayan yargı ana düşüncedir.','konu':'Her şıkkın parçanın tamamını karşılayıp karşılamadığına bak; çok dar ya da parçada işlenmeyen ifadeleri ele.','baslik':'Başlığın parçanın tamamını kapsayıp kapsamadığına bak; örneğe dayanan ya da taşan başlıkları ele.','amac':'Yazarın eleştirdiği ve savunduğu yargıyı ayır; yalnız örnekten ya da yarım doğrudan çıkan şıkları ele.'}
PUF={'ana':['Ana düşünce parçanın tamamını kapsar; yalnız bir cümleyi karşılayan şık ayrıntıdır.','Bağlaçtan sonra gelen yargı çoğunlukla yazarın asıl söylemek istediğidir.','“Her, yalnızca, hiçbir” gibi sözcüklerle genelleyen şık çoğunlukla parçayı aşar.'],
     'konu':['Konu “ne” sorusuna, ana düşünce “ne diyor” sorusuna yanıt verir.','Konu şıkkı parçadaki tüm yönleri karşılamalı; örnekten doğan dar şıkka kapılma.'],
     'baslik':['İyi başlık parçanın tamamını kısa bir adla özetler; örneği değil konuyu adlandırır.'],
     'amac':['Yazarın amacını bulmak için hangi görüşü eleştirip hangisini öne çıkardığına bak.','Yazarın amacı çoğunlukla karşıtlık ya da sonuç ifadesiyle verilir.']}
ERR=[]; KEL={}; KONULAR=set(); SAY={'ana':0,'konu':0,'baslik':0,'amac':0}
def S(no,tur,zor,harf,konu,metin,dogru,yan,ozet,anahtar,ip):
    """tur: ana|konu|baslik|amac; yan: [(şık, etiket, çeldirici açıklaması, hata türü)] ×4 (A–E sırasıyla doğru şık atlanarak)"""
    assert konu not in KONULAR,konu; KONULAR.add(konu)
    kelime=len(metin.split()); KEL[no]=kelime
    if not 60<=kelime<=150 or (zor=='zor' and kelime<100) or (zor!='zor' and kelime>140): ERR.append((no,zor,'kelime',kelime))
    assert len(yan)==4 and all(y[1] in ETK and y[1]!='D' for y in yan)
    if len(dogru)>max(len(y[0]) for y in yan): ERR.append((no,'doğru şık en uzun',len(dogru),[len(y[0]) for y in yan]))
    kok=KOK[tur][SAY[tur]%len(KOK[tur])]; SAY[tur]+=1
    it=iter(yan); opts=[]
    for L in 'ABCDE':
        opts.append((dogru,'D','','') if L==harf else next(it))
    adimlar=[AD('Parçayı özetle',ozet[0],ozet[1]),AD('Anahtar ifadeyi bul',anahtar[0],anahtar[1]),
             AD('Şıkları parçayla karşılaştır',ADIM3[tur],' · '.join(f"{L}: {ETK[o[1]]}" for L,o in zip('ABCDE',opts))),
             AD('Sonucu yaz','Parçanın tamamını karşılayan tek şık doğru cevaptır.',f'cevap: {harf}')]
    n=int(no); puf=PUF[tur][n%len(PUF[tur])]
    soru(Q,no,KARTSEC[(tur,zor)],zor,KAZ[tur],KARTLAR[KARTSEC[(tur,zor)]]['adim'],metin+'\n'+kok,opts,harf,lambda e:e=='D',
         {'ana':'Parçanın asıl mesajı.','konu':'Parçada işlenen konu.','baslik':'Parçanın tamamını karşılayan başlık.','amac':'Yazarın vurgulamak istediği yargı.'}[tur],
         ip,BI[tur][:2] if zor=='zor' else BI[tur][:1],adimlar,puf)

# ===================== PARÇA 1 (0001–0025) =====================
S('0001','ana','kolay','C','yürüyüş',
 'Yürüyüş, yalnızca bacak kaslarını çalıştıran bir hareket değildir; aynı zamanda zihni de dinlendirir. Kalp daha güçlü atar, kaslar ısınır, ama asıl fark kafanın içinde başlar. Masa başında bir türlü çözemediğimiz bir sorunun, kısa bir yürüyüşten sonra birdenbire netleştiğini çoğumuz yaşamışızdır. Adımlar düzenli bir ritme oturdukça düşünceler de sıraya girer. Bu yüzden günde yarım saat yürümek, hem bedenin hem de zihnin ihtiyaç duyduğu bir bakımdır.',
 'Yürüyüş, bedene olduğu kadar zihne de iyi gelir.',
 [('Masa başında çalışan herkes sorunlarını yürüyerek çözmelidir.','genel','Parça yürüyüşün sorunu netleştirebildiğini söyler; “herkes yürüyerek çözmelidir” genellemesi yoktur.','bilgi'),
  ('Yürüyüşün hızı arttıkça düşünceler daha düzenli hâle gelir.','yok','Parçada yalnızca düzenli ritimden söz edilir; hız arttıkça düzenin arttığı söylenmez.','bilgi'),
  ('Kısa bir yürüyüş, çözülemeyen bir sorunu netleştirebilir.','yan','Parçada geçen bir örnek durumdur; parçanın tamamının vermek istediği sonuç değildir.','dikkat'),
  ('Yürüyüş, yalnızca kas gücünü artırmak için yapılan bir harekettir.','ters','İlk cümle tam tersini söyler: yürüyüş “yalnızca” kas çalıştırmaz, zihni de dinlendirir.','bilgi')],
 ('Yürüyüş hem bedeni hem zihni dinlendiriyor.','yürüyüş → beden + zihin'),('“Bu yüzden” ile başlayan son cümle sonucu verir: yürüyüş hem beden hem zihin bakımıdır.','sonuç: beden ve zihin bakımı'),
 'Son cümledeki “hem … hem de” ifadesi iki yönü birden anıyor.')

S('0002','ana','kolay','A','arılar',
 'Arılar çiçekten çiçeğe konarken yalnızca kendi besinlerini toplamış olmazlar; bu sırada ayaklarına yapışan polenleri bir sonraki çiçeğe de taşırlar. Böylece bitkilerin döllenmesi gerçekleşir ve meyveler oluşur. Bir arı kovanı günde binlerce çiçeği dolaşır ve bu yoğun emek, tarlalardan bahçelere kadar geniş bir alanı etkiler. Sofralarımıza gelen sebze ve meyvelerin büyük bölümü, bu küçük canlıların emeğine borçludur. Arıların azalması, bu nedenle yalnızca bal üretimini değil, besin zincirinin tamamını tehdit eder.',
 'Arılar, bitkileri döllemeleriyle insan beslenmesi için önemlidir.',
 [('Arılar, ayaklarına yapışan polenleri bir çiçekten başka bir çiçeğe taşır.','yan','Parçada geçen bir ayrıntıdır; parçanın asıl vermek istediği mesaj değildir.','dikkat'),
  ('Bal üretimi, arıların insanlara sağladığı tek yarardır.','ters','Parça arıların döllenmeye katkıyla bal dışında da büyük yarar sağladığını söyler.','bilgi'),
  ('Sebze ve meyve üretimi yalnızca arıların yaptığı tozlaşmaya bağlıdır.','genel','Parça “büyük bölümü” der; “yalnızca” aşırı genellemedir.','dikkat'),
  ('Arı sayısı azalırsa besin zincirinin tamamı kısa sürede çökecektir.','genel','Parça “tehdit eder” der; kesin ve hızlı bir çöküş iddiası parçada yoktur.','dikkat')],
 ('Arılar polen taşır, bitkiler döllenir, meyveler oluşur.','arı → döllenme → besin'),('“Bu nedenle” ile başlayan son cümle, arıların azalmasının besin zincirine etkisini söyler.','sonuç: arı = besin güvencesi'),
 'Parçanın başı ile sonu arasında nasıl bir neden–sonuç bağı var?')

S('0003','ana','orta','E','kent ağaçları',
 'Şehir planlamacıları uzun süre ağacı, yolun kenarına dikilen bir süs gibi gördü. Oysa sokaktaki ağaç, yazın asfaltın ısısını düşüren, havadaki tozu tutan ve gürültüyü azaltan bir altyapı unsurudur. Sıra sıra dizilmiş ağaçların oluşturduğu yeşil çatı, kış yağmurlarında suyun akışını yavaşlatarak yolların taşmasını da azaltır. Üstelik gölgesinde yürüyen insan daha az yorulur, daha uzun süre dışarıda kalır. Bir ağacın bakım masrafı ise çoğu zaman yaptığı bu işlerin parasal karşılığının çok altındadır. Yine de bütçe daraldığında ilk kısılan kalem çoğunlukla yeşil alanlar olur. Bu nedenle ağaçlandırma, estetik bir tercih olarak değil, kentin işleyişine hizmet eden bir yatırım olarak ele alınmalıdır.',
 'Kent ağacı süs değil, kente hizmet eden bir yatırımdır.',
 [('Ağaç bakımı, kentlerin en pahalı belediye hizmetlerinden biridir.','ters','Parça bakım masrafının ağacın sağladığı yararın çok altında kaldığını söyler.','bilgi'),
  ('Gölgede yürüyen insanlar, daha uzun süre dışarıda kalabilir.','yan','Parçada geçen bir ayrıntıdır; ana düşünceyi destekler ama onun yerine geçmez.','dikkat'),
  ('Şehir planlamacıları ağaca hiçbir zaman önem vermemiştir.','genel','Parça “uzun süre” süs saymaktan söz eder; “hiçbir zaman” aşırı bir genellemedir.','dikkat'),
  ('Ağaçlandırma, yalnızca yaz sıcaklığını düşürmek amacıyla yapılır.','dar','Sıcaklığı düşürmek ağacın yalnız bir yararıdır; toz tutma ve gürültüyü azaltma da sayılır.','bilgi')],
 ('Ağaç süs değil, sıcaklık, toz ve gürültüye karşı işlev görüyor.','ağaç → altyapı'),('“Oysa” karşıtlığı ve “Bu nedenle” sonucu, ağaca bakışın değişmesi gerektiğini söyler.','süs ✗ → yatırım ✓'),
 '“Oysa” ve “Bu nedenle” sözcükleri yazarın asıl yargısını işaret eder.')

S('0004','ana','orta','B','çeviri',
 'Bir metni başka bir dile çevirmek, sözcükleri tek tek karşılıklarıyla değiştirmekten ibaret görülür. Oysa her dilin kendine özgü bir düşünme ve duyma biçimi vardır. Bir dilde tek sözcükle anlatılan duygu, başka bir dilde ancak bir cümleyle karşılanabilir. Bir deyimi sözcük sözcük çevirdiğinizde ortaya ya gülünç ya da anlamsız bir cümle çıkar. İyi bir çevirmen bu yüzden sözcüğün sözlükteki karşılığından çok, onun metindeki yükünü taşımaya çalışır; çünkü çeviride en çok zorlanılan şey sözcükler değil, sözcüklerin arasında kalan tonlardır. Sözcüğe sadık kalan çeviri çoğu zaman anlama ihanet eder.',
 'İyi çeviri, sözcüğü değil anlamı ve duyguyu aktarır.',
 [('Her dilde duyguları anlatan sözcüklerin sayısı birbirine eşittir.','yok','Parça dillerin duygu sözcüklerinin sayısını karşılaştırmaz; dillerin farklı duyma biçimlerinden söz eder.','bilgi'),
  ('Çevirmenler çeviri yaparken sözlüklere başvurmaktan kaçınmalıdır.','genel','Parça sözlüğü yasaklamaz; yalnızca sözlük karşılığının tek başına yetmediğini söyler.','dikkat'),
  ('Her dil, kendi konuşurlarının düşünme biçimini yansıtır.','yan','Parçada geçer ama çeviriden söz eden asıl düşünceyi kapsamaz; gerekçedir.','dikkat'),
  ('Sözcüğe sadık kalan çeviri, her zaman anlama ihanet eder.','genel','Parça “çoğu zaman” der; “her zaman” aşırı bir genellemedir.','dikkat')],
 ('Çeviri sözcük değiştirme değil; her dilin duyma biçimi farklı, çevirmen anlamı taşır.','çeviri ≠ sözcük değişimi'),('“Oysa” ve “bu yüzden” sözcükleri, iyi çevirmenin sözcükten çok anlama yöneldiğini gösterir.','sözcük ✗ → anlam ✓'),
 'Dillerin farklı olması, parçada neyin gerekçesi olarak kullanılıyor?')

S('0005','ana','orta','D','müzik ve hafıza',
 'Bir şarkıyı yıllar sonra duyduğumuzda, o şarkının çaldığı döneme ait koku, mekân ve yüzler bir anda gözümüzün önüne gelir. Eski bir ezgi, unuttuğumuzu sandığımız bir yaz akşamını, o akşamın gürültüsünü bile geri getirir; bunun için hiçbir çaba harcamamız gerekmez. Müzik, sözcüklerden önce duyguya seslenir; duygu ise anıların depolandığı yere en kısa yoldan ulaşır. Bu yüzden müziğin hatırlatma gücü, çoğu zaman bir fotoğrafınkinden daha canlıdır. Sevdiklerini unutmaya başlayan yaşlılara eski şarkıların dinletildiği bakım evlerinde, silinmiş sanılan anıların geri geldiği görülür.',
 'Müzik, duygu yoluyla anıları canlandırma gücüne sahiptir.',
 [('Fotoğraflar, anıları hatırlamak için yetersiz bir araçtır.','genel','Parça müziğin hatırlatma gücünü “çoğu zaman daha canlı” bulur; fotoğrafı yetersiz saymaz.','dikkat'),
  ('Yaşlılar için müzik, hastalıkları iyileştiren tek yöntemdir.','genel','Parça yalnızca anıların geri geldiğini söyler; “tek yöntem” iddiası parçada yoktur.','bilgi'),
  ('Bir şarkı, çaldığı döneme ait kokuları hatırlatabilir.','yan','Parçada geçen bir örnektir; müziğin anıyı canlandırma gücünü gösterir, ama ana düşünce değildir.','dikkat'),
  ('Anılar, yalnızca sözcüklerle yeniden hatırlanabilir.','ters','Parça müziğin sözcüklerden önce duyguya seslendiğini ve anıları geri getirdiğini söyler.','bilgi')],
 ('Şarkı duyulunca dönem canlanıyor; müzik duygu yoluyla anıya ulaşıyor.','müzik → duygu → anı'),('“Müzik, sözcüklerden önce duyguya seslenir; duygu anılara en kısa yoldan ulaşır” cümlesi parçanın özüdür.','müzik → duygu → anı'),
 'Parçadaki örnekleri (şarkı, bakım evi) bir mesajın kanıtı olarak düşün.')

S('0006','ana','orta','A','çömlekçilik',
 'Çömlekçi çamuru çarka koyduğunda elinin biraz fazla baskı yapması, kabın bir anda yamulmasına yeter. Acemi çömlekçi bu yüzden çarkın hızı karşısında telaşlanır ve elini erken çeker. Ne kadar acele ederse etsin kil, kendi kuruma süresini bekler; çatlamaması için günlerce gölgede durması gerekir. Fırın da ısınmak için kendi zamanını ister. Usta bu yüzden işin hızlandırılamayan yönlerine karşı direnmez, onlara uyum sağlar. Yıllarını bu işe vermiş birinin sabrı, bir erdem olmaktan önce, malzemeyi tanımanın doğal sonucudur.',
 'El sanatlarındaki sabır, malzemeyi tanımanın sonucudur.',
 [('Çamura fazla baskı uygulayan çömlekçinin kabı kolayca yamulur.','yan','Parçada geçen bir örnektir; sabrın nedenini açıklayan ana düşünceyi kapsamaz.','dikkat'),
  ('Acele eden çömlekçilerin kapları fırında mutlaka çatlar.','genel','Parça kilin çatlamaması için beklemek gerektiğini söyler; “mutlaka çatlar” kesinliği parçada yoktur.','dikkat'),
  ('Fırının ısınması, çömlekçilikteki en uzun aşamadır.','yok','Parça fırının kendi zamanını istediğini söyler; aşamaların süresini karşılaştırmaz.','bilgi'),
  ('Sabır, el sanatlarında bir erdem sayıldığı için kazanılır.','ters','Parça sabrın “bir erdem olmaktan önce” malzemeyi tanımanın sonucu olduğunu söyler.','dikkat')],
 ('Çamur ve fırın acele kabul etmez; usta bunlara uyar.','malzeme → uyum → sabır'),('Son cümle sabrın kaynağını söyler: erdemden çok malzemeyi tanımak.','sabır ← malzemeyi tanımak'),
 'Parça sabrın nereden doğduğunu açıklıyor; son cümleye dikkat et.')

S('0007','ana','orta','C','hata yapma korkusu',
 'Bir öğrenci, yanlış cevap verdiğinde sınıfta alay konusu oluyorsa bir daha elini kaldırmaz. Daha sonra bildiği bir konuda bile susmayı seçer; çünkü susan çocuk kimsenin gözüne batmaz. Hata yapmanın bedeli ağır olan ortamlarda öğrenciler, öğrenmek yerine güvenli görünmeyi seçer. Öğretmenin tavrı da bu havayı belirler: yanlışı düzeltirken küçümseyen bir öğretmen, sınıfa farkında olmadan susmayı öğretmiş olur. Oysa öğrenme, tam da yanlışın fark edilip düzeltilmesiyle ilerler. Yanlışı utanılacak bir şey olmaktan çıkaran sınıflarda öğrenciler daha cesur sorular sorar ve daha kalıcı biçimde öğrenir.',
 'Hatanın olağan karşılandığı ortamlar, öğrenmeyi güçlendirir.',
 [('Öğretmenler yanlış yapan öğrencileri her zaman küçümser.','genel','Parça yalnızca küçümseyen bir öğretmenin etkisini anlatır; bütün öğretmenlerin küçümsediğini söylemez.','dikkat'),
  ('Öğrenciler güvenli görünmeyi, öğrenmekten daha önemli sayar.','ters','Parça bu davranışı hatanın bedelinin ağır olduğu ortama bağlar ve eleştirir; öğrencinin değer yargısını söylemez.','dikkat'),
  ('Alay edilmek, öğrencinin başarısını doğrudan düşürür.','yok','Parça alayın katılımı azalttığını söyler; başarıya doğrudan etkisinden söz etmez.','bilgi'),
  ('Cesur soru soran öğrenciler hiçbir zaman yanlış yapmaz.','ters','Parça yanlışın öğrenmenin parçası olduğunu söyler; bu şık parçaya terstir.','bilgi')],
 ('Alay edilen öğrenci susar; hata normal olunca öğrenci cesur ve kalıcı öğrenir.','hata korkusu → sessizlik'),('“Oysa” ile parça, öğrenmenin yanlışın düzeltilmesiyle ilerlediğini söyler; son cümle bunu ortama bağlar.','hata normal → öğrenme ↑'),
 '“Oysa” sonrasındaki yargıyı ve son cümledeki sonucu birlikte düşün.')

S('0008','ana','zor','E','ortalama',
 'Bir köydeki ortalama gelirin yüksek çıkması, köyde yaşayan herkesin rahat olduğunu göstermez; zira birkaç büyük kazanç, onlarca küçük geliri gölgede bırakabilir. Aynı ortalamaya sahip iki köyden birinde gelirler birbirine yakın, ötekinde uçurum gibi ayrışmış olabilir. Ortalama, veriyi tek sayıya indirdiği için pratiktir; ama pratik olması, doğru anlatması demek değildir. Haberlerde ve raporlarda gördüğümüz yüzdelerin, oranların ve ortalamaların çoğu bu yüzden sandığımızdan daha az şey söyler. Sayıların dilini bilmeyen okur, ortalamayı kesin bir hüküm sanır ve tablonun ardındaki dağılımı görmez. Rakamlar ne kadar temiz görünürse görünsün, onları üreten dağılım hâlâ yerinde durur. Bu yüzden bir istatistikle karşılaştığımızda önce “kaç?” değil, “nasıl dağılmış?” diye sormak gerekir.',
 'Özet istatistikler, dağılım sorgulanmazsa yanıltıcı olabilir.',
 [('Ortalama gelir, bir toplumun refahını ölçmede hiçbir zaman kullanılamaz.','genel','Parça ortalamanın tek başına yanıltabileceğini söyler; “hiçbir zaman kullanılamaz” demez.','dikkat'),
  ('Birkaç yüksek gelir, ortalamayı olduğundan yüksek gösterebilir.','yan','Parçada geçen bir açıklamadır; parçanın tamamını kapsayan sonuç değildir.','dikkat'),
  ('Sayılarla çalışan herkes, dağılıma bakmayı kendiliğinden bilir.','ters','Parça sayıların dilini bilmeyen okurun ortalamayı kesin hüküm sandığını söyler.','bilgi'),
  ('Pratik olan yöntemlerin sonuçları her zaman yanlıştır.','genel','Parça “pratik olması doğru anlatması demek değildir” der; her zaman yanlış demez.','dikkat')],
 ('Ortalama pratik ama yanıltıcı; asıl bakılacak şey dağılım.','ortalama ≠ dağılım'),('“Bu yüzden” ile başlayan son cümle çıkarımı verir: önce dağılımı sor.','sonuç: dağılımı sorgula'),
 'Örnekleri (köy geliri) ayır; yazar bunlardan hangi genel sonuca varıyor?')

S('0009','ana','zor','B','unutma',
 'Unutmayı çoğu zaman belleğin bir arızası sayarız. Oysa her gördüğünü, her duyduğunu eksiksiz saklayan bir zihin, anlamlı olanı anlamsızdan ayıramazdı; önemli bir yüz, binlerce önemsiz yüzün arasında kaybolurdu. Hafızası kusursuz olan biri arkadaşının yüzünü tanımakta bile zorlanırdı; çünkü o yüzün her günkü ışığı, her günkü ifadesi ayrı bir kayıt olarak dururdu ve hiçbiri ötekine benzetilemezdi. Bir odaya girdiğimizde gözümüze çarpan binlerce ayrıntının çoğunu birkaç saniye içinde bırakırız; bu bir kayıp değil, bir seçimdir. Zihnin bu eleme gücü, her gün sayısız küçük karar vermemizi sağlar. Elenen ayrıntılar sayesinde genel örüntüler belirginleşir, kavramlar oluşur, düşünmek mümkün olur. Bu açıdan bakıldığında bellek, ne kadar şey sakladığıyla değil, neyi bırakabildiğiyle değer kazanır.',
 'Unutma, belleğin arızası değil, düşünmeyi mümkün kılan özelliğidir.',
 [('İnsan zihni, gördüğü her şeyi eksiksiz saklayabilecek kapasitededir.','yok','Parça böyle bir zihnin olsaydı neler yaşanacağını varsayar; insan zihninin kapasitesinden söz etmez.','bilgi'),
  ('Önemli yüzleri hatırlamak, önemsiz yüzleri unutmaktan daha zordur.','yok','Parçada iki işlemin güçlük karşılaştırması yoktur.','bilgi'),
  ('Kavramlar, ancak ayrıntılar elendikten sonra oluşabilir.','dar','Parçada geçen bir gerekçedir; bellek–unutma ilişkisinin tamamını ve sonuç yargısını kapsamaz.','dikkat'),
  ('Bellek, ne kadar çok şey sakladığıyla değerlendirilmelidir.','ters','Son cümle tam tersini söyler: değer, neyi bırakabildiğinde yatar.','bilgi')],
 ('Eksiksiz saklayan zihin ayıramaz; unutma örüntü ve kavram sağlar.','unutma → kavram → düşünme'),('“Oysa” ile unutma arıza sayılmaktan çıkar; son cümle “neyi bırakabildiği”ni öne çıkarır.','arıza ✗ → işlev ✓'),
 'Son cümledeki “ne kadar … değil, neyi …” karşıtlığı yazarın görüşünü verir.')

S('0010','ana','zor','D','mesajlaşma hızı',
 'Eskiden bir mektubun cevabını haftalarca beklemek olağandı ve bu bekleyiş, yazılan her satırı daha özenli kılardı. Mektup yazan kişi, cümlesini bir kez gönderdikten sonra geri alamayacağını bilirdi; bu bilgi onu düşünmeye iterdi. Beklemek, bir zamanlar düşünmenin sessiz ortağıydı. Şimdi mesajın iletilme hızı saniyelere indi; ama cevap beklentisi de aynı oranda kısaldı. Karşımızdakinin hemen yanıt vermemesi, ilgisizlik diye yorumlanıyor. Cümleler kısalıyor, özenle seçilmiş sözcükler yerini hazır kalıplara bırakıyor. İnsanlar düşüncelerini toparlamadan, aklına ilk geleni yazıp gönderiyor; ekranda silinen cümle ise hiç yazılmamış sayılıyor. Hız, aramızdaki mesafeyi kısalttı kuşkusuz; fakat düşünmeye ayrılan aralığı da ortadan kaldırarak konuşmaları art arda gelen kısa mesajların kovalandığı dalgalı bir akışa dönüştürdü.',
 'Hızlanan iletişim, mesafeyi kısaltırken düşünme payını azaltmıştır.',
 [('Mektup yazmak, mesajlaşmaktan her bakımdan daha değerlidir.','genel','Parça mektubun bekleyişinin özenli yazdırdığını söyler; “her bakımdan daha değerli” demez.','dikkat'),
  ('Geç yanıt veren kişi, karşısındakine ilgisiz olduğunu göstermiş olur.','yok','Parça bu yorumun yapıldığını söyler; yorumun doğru olduğunu savunmaz.','dikkat'),
  ('Mesajların iletilme hızı, eskiye göre büyük ölçüde artmıştır.','yan','Parçada geçen bir tespittir; yazarın asıl vurgusu bu hızın bir bedeli olduğudur.','dikkat'),
  ('İnsanlar artık birbirlerine yazmaktan tümüyle kaçınmaktadır.','yok','Parçada böyle bir iddia yoktur; yazışmanın niteliğinden söz edilir.','bilgi')],
 ('Mektup bekleyişi özen katardı; hız mesafeyi kısalttı ama düşünme payını yok etti.','hız ↑ → düşünme payı ↓'),('“Kuşkusuz … fakat” kalıbı, hızın yararını kabul edip asıl vurguyu bedeline getirir.','kabul → fakat → bedel'),
 '“Fakat”tan sonraki yargı, yazarın asıl söylemek istediğidir.')

S('0011','ana','orta','E','fotoğraf ve anı',
 'Eskiden bir fotoğraf çektirmek bir olaydı; poz verilir, ışık beklenir, film sayılırdı. Aileler, filmin basılacağı günü haftalarca merakla beklerdi. Bugün ise günde yüzlerce kare çekebiliyoruz. Ne var ki çoğalan kareler, anıları da çoğaltmıyor. Çektiğimiz fotoğraflara çoğu kez bir daha bakmıyor, o anı yaşamak yerine kadraja sığdırmaya çalışıyoruz. Bir doğum günü pastasının mumlarını üflemekten çok, o anı kaydetmekle uğraşan kalabalıklar bunun örneğidir. Anıyı değerli kılan, kaç kare çekildiği değil, o anın ne kadar derinden yaşandığıdır.',
 'Anının değeri, belgelenmesine değil yaşanma derinliğine bağlıdır.',
 [('Fotoğraf çektirmek, eskiden olduğu gibi özenle ve seyrek yapılmalıdır.','yok','Parça eski çekim biçimini anlatır; bugünün de öyle yapılması gerektiğini önermez.','dikkat'),
  ('Film sayılarak çekilen fotoğraflar, daha kalıcı anılar bırakır.','ters','Parça kalıcılığı çekim sayısına değil yaşanmışlığın derinliğine bağlar.','bilgi'),
  ('Günümüzde fotoğraf çekmek, eskiye göre çok daha kolay hâle gelmiştir.','yan','Parçada geçen bir tespittir; parçanın vermek istediği sonuç değildir.','dikkat'),
  ('İnsanların çektikleri fotoğraflara bir daha bakmaması bir alışkanlıktır.','yan','Parçada geçen bir ayrıntıdır; sonuca götüren bir gözlemdir, ana düşünce değildir.','dikkat')],
 ('Eskiden az fotoğraf, şimdi çok; ama kare çoğalınca anı çoğalmıyor.','kare ↑ ≠ anı ↑'),('“Ne var ki” ile bir karşıtlık kurulur; son cümle anıyı değerli kılanı söyler.','değer = yaşanmışlık'),
 'Son cümledeki “… değil, …” yapısı vurgulanan yargıyı gösterir.')

S('0012','ana','orta','B','edebiyat eleştirisi',
 'İyi bir eleştirmen, eserin yanına oturup ona kendi zevklerini dayatmaz; önce eserin neyi amaçladığını anlamaya çalışır. Bir komediyi dramın ölçütleriyle yargılamak, balığı ağaca tırmanamadığı için suçlamaya benzer. Bir şiirde romanın akıcılığını, bir minyatürde yağlıboya tablonun derinliğini aramak da aynı yanılgıdır. Ölçüt, eserin kendi dünyasından çıkarıldığında eleştiri yalnızca eleştirmenin portresini çizer. Gerçek eleştiri, eseri yargılamadan önce onun hangi soruya cevap verdiğini sormakla başlar; ancak bu sorunun yanıtı alındıktan sonra eserin başarılı olup olmadığı tartışılabilir.',
 'Eleştiri, eserin kendi amacı ve ölçütleri esas alınarak yapılmalıdır.',
 [('Komedi türündeki eserler, dram türündeki eserlerden daha az değerlidir.','ters','Parça türlerin birbirinin ölçütleriyle yargılanmasını eleştirir; değer sıralaması yapmaz.','bilgi'),
  ('Eleştirmenler, eserleri çoğunlukla kendi zevklerine göre yargılar.','ters','Parça eleştirmenin zevkini dayatmaması gerektiğini söyler; bu bir tespit değil, eleştirilen davranıştır.','dikkat'),
  ('Eleştiri yazıları, yazarın kişiliğini yansıtan metinlerdir.','genel','Parça yalnızca ölçüt dışarıdan alınınca eleştirinin eleştirmeni yansıttığını söyler; genel bir kural koymaz.','dikkat'),
  ('Her eser, hangi soruya cevap verdiğini kendisi açıklar.','yok','Parçada eserin kendini açıkladığı söylenmez; eleştirmenin bunu sorması gerektiği söylenir.','bilgi')],
 ('İyi eleştirmen eserin amacını anlar; ölçütü dışarıdan getirmek eleştiriyi bozar.','ölçüt eserden gelir'),('Son cümle gerçek eleştirinin başlangıcını söyler: eserin cevap verdiği soruyu sormak.','sonuç: eserin amacını esas al'),
 'Parçadaki benzetme (balık, ağaç) bir yargıyı örnekliyor.')

S('0013','ana','orta','A','uyku ve öğrenme',
 'Sınav öncesi geceyi sabaha kadar ders çalışarak geçirmek, birçok öğrencinin başvurduğu bir yöntemdir. Gece boyunca ışığın altında kitap karıştıran öğrenci kendini hazır hisseder; ama sabah sınav kâğıdını gördüğünde bildiklerinin bulanıklaştığını fark eder. Oysa öğrenilen bilgiler, uyku sırasında beynin düzenleme sürecinden geçerek kalıcı belleğe yerleşir. Uykusuz geçen bir gecede bu süreç yarım kalır; bilgi, sabaha kadar tekrarlanmış olsa bile kısa süre içinde silinip gider. Bu, kişinin tembelliğiyle değil, belleğin işleyişiyle ilgilidir. Bu nedenle yeterince uyumuş bir öğrenci, aynı konuyu uykusuz tekrar eden bir arkadaşından çoğu zaman daha başarılıdır.',
 'Kalıcı öğrenme, yeterli uyku olmadan verimsiz kalır.',
 [('Sınav öncesinde ders çalışmak, yararsız bir uğraştır.','genel','Parça çalışmayı değil, uykusuz çalışmanın verimsizliğini eleştirir.','dikkat'),
  ('Beyin, uyku sırasında yalnızca dinlenmekle yetinir.','ters','Parça beynin uykuda bilgiyi düzenleyip kalıcı belleğe yerleştirdiğini söyler.','bilgi'),
  ('Bilgiler, sabaha kadar tekrarlandığında kalıcı hâle gelir.','ters','Parça tersini söyler: uykusuz tekrar edilen bilgi kısa sürede silinir.','bilgi'),
  ('Birçok öğrenci, sınav gecesini ders çalışarak geçirir.','yan','Parçanın başında verilen bir tespittir; asıl düşünceye zemin hazırlar.','dikkat')],
 ('Sabaha kadar çalışmak yaygın; oysa bilgi uykuda kalıcılaşıyor.','uykusuz çalışma ✗'),('“Oysa” cümlesi asıl iddiayı verir: bilgi uyku sırasında kalıcılaşır.','uyku → kalıcı bellek'),
 '“Oysa” ve “Bu nedenle” sözcükleri parçanın omurgasını gösterir.')

S('0014','konu','kolay','C','mercan resifleri',
 'Mercan resifleri, okyanus tabanının küçük bir bölümünü kaplasa da çok sayıda deniz canlısına yuva olur. Küçük balıklar kayalıkların arasına gizlenir, daha büyükler bu küçüklerle beslenmek için resife gelir. Resifin kendisi de yüzyıllar boyunca santim santim büyüyen, içinde sayısız canlıyı barındıran, renkli ve kıpır kıpır bir şehir gibidir. Resifler aynı zamanda dalgaların gücünü kıran doğal birer set görevi görür ve kıyıyı aşınmadan korur.',
 'Mercan resiflerinin doğaya sağladığı yararlar',
 [('Okyanusların kirlenmesinin canlılar üzerindeki etkisi','yok','Parçada kirlilikten ya da canlılara zararından hiç söz edilmez.','bilgi'),
  ('Küçük balıkların beslenme alışkanlıkları','dar','Parçada yalnızca küçük balıkların gizlendiği ve büyüklere yem olduğu söylenir; bu parçanın bir ayrıntısıdır.','dikkat'),
  ('Kıyıların aşınmasını önlemenin yolları','dar','Resiflerin kıyıyı koruması parçanın yalnız bir bölümüdür; “önlemenin yolları” işlenmemiştir.','dikkat'),
  ('Deniz canlılarının göç yolları','yok','Parçada göçten hiç söz edilmez.','bilgi')],
 ('Resif canlılara yuva olur, besin zincirini kurar, kıyıyı korur.','resif → yuva + koruma'),('Üç cümle resifin üç ayrı yararını sayar: yuva, besin, kıyı koruması.','yararlar: yuva, besin, koruma'),
 'Parçanın bütün cümlelerinde resif ne yapıyor?')

S('0015','konu','kolay','D','sokak oyunları',
 'Eskiden mahalle aralarında çocuklar akşama kadar saklambaç, ip atlama ve misket oynardı. Sokağın her köşesi bir oyun alanına dönüşür, farklı yaştaki çocuklar aynı oyunun içinde buluşurdu. Bu oyunların çoğu için pahalı bir araç gerekmezdi; bir tebeşir, bir ip ya da bir avuç taş yeterdi. Çocuklar kuralları kendileri koyar, anlaşmazlıkları yine kendileri çözerdi. Böylece oyun, yalnızca eğlence değil, bir toplumsal yaşam provası da olurdu.',
 'Sokak oyunlarının özellikleri ve önemi',
 [('Çocukların teknolojiyle kurduğu ilişki','yok','Parçada teknolojiden söz edilmez.','bilgi'),
  ('Mahalle kültürünün yok oluşu','yok','Parça mahalle oyunlarını anlatır; kültürün yok oluşu işlenmemiştir.','bilgi'),
  ('Oyuncak üretiminin ekonomik boyutu','yok','Parça oyunların pahalı araç gerektirmediğini söyler; üretim ve ekonomiden söz etmez.','dikkat'),
  ('Çocuklarda kural koyma becerisinin gelişimi','dar','Kural koyma parçanın yalnız bir ayrıntısıdır; oyunların özellikleri ve önemi daha geniştir.','dikkat')],
 ('Sokak oyunları ucuz, kuralları çocuklarca konan, öğretici oyunlardı.','sokak oyunu → özellik + önem'),('Parça önce oyunları sayar, sonra araç ve kural özelliklerini, en sonda önemini anlatır.','oyun → özellik → önem'),
 'Parça hem oyunların nasıl olduğunu hem ne işe yaradığını anlatıyor.')

S('0016','konu','orta','A','gizli su',
 'Bir pamuklu tişörtün üretimi için yüzlerce litre suyun harcandığını çok az kişi bilir. Tarladaki sulamadan boyahanedeki yıkamaya kadar her aşama su ister. Bir kilo buğday ya da bir fincan kahve için de benzer bir hesap yapılabilir; sofradaki her şey, bize gelene dek suyla yoğrulmuştur. Biz yalnızca musluktan akan suyu hesaba kattığımız için tüketimimizin gerçek boyutunu göremeyiz. Oysa aldığımız her ürünün gizli bir su payı vardır ve bu pay, evde kullandığımız suyun çok üzerine çıkabilir.',
 'Ürünlerde harcanan gizli su miktarı',
 [('Pamuk tarımında kullanılan sulama yöntemleri','dar','Pamuk tarlası yalnızca bir örnek aşamadır; yöntemlerden söz edilmez.','dikkat'),
  ('Musluk suyunun tasarruflu kullanılma yolları','yok','Parça musluk suyunu bir karşılaştırma ölçüsü olarak anar; tasarruf yollarını işlemez.','dikkat'),
  ('Boyahanelerin çevreye verdiği zararlar','yok','Parça boyahaneyi su harcanan bir aşama olarak anar; çevre zararından söz etmez.','dikkat'),
  ('Tekstil sektörünün ekonomik büyüklüğü','yok','Parçada sektörün ekonomik boyutuna dair bir bilgi yoktur.','bilgi')],
 ('Ürünlerin üretiminde, bilmediğimiz kadar çok su harcanıyor.','tişört → gizli su'),('“Gizli bir su payı” ifadesi parçanın merkezidir; tişört ise örnektir.','konu: gizli su payı'),
 'Tişört bir örnek mi, konunun kendisi mi?')

S('0017','konu','orta','E','dublaj ve altyazı',
 'Bir filmi dublajlı izlemek ile altyazılı izlemek, aynı hikâyeyi iki farklı deneyime dönüştürür. Dublajda gözümüz görüntüye tam olarak odaklanabilir; ama oyuncunun sesindeki titreşim, aksan ve duraksamalar yerini başka bir sese bırakır. Altyazıda ise özgün sesi duyarız, buna karşılık gözümüzün bir kısmı satırların peşinden koşar. Hangisinin daha iyi olduğu, çoğu zaman filmin türüne ve izleyicinin alışkanlığına göre değişir. İki yöntemin her biri bir şeyi kazandırırken başka bir şeyi geri alır.',
 'Dublaj ve altyazının kazandırdıkları ve kaybettirdikleri',
 [('Yabancı dil öğreniminde filmlerin ve dizilerin yeri','yok','Parçada dil öğrenimi hiç geçmez.','bilgi'),
  ('Yabancı filmlerin ülkemizdeki izlenme oranları ve eğilimleri','yok','Parçada izlenme oranlarına dair bir veri ya da söz yoktur.','bilgi'),
  ('Altyazılı film izlemenin görme sağlığı üzerindeki etkisi','dar','Gözün satırları izlemesi, altyazıya ilişkin yalnız bir ayrıntıdır.','dikkat'),
  ('Dublajda oyuncunun özgün sesinin tamamen kaybolması','dar','Yalnızca dublajın bir kaybıdır; altyazıyı ve kazanımları kapsamaz.','dikkat')],
 ('Dublaj görüntüyü rahatlatır, sesi değiştirir; altyazı sesi korur, gözü yorar.','dublaj ↔ altyazı'),('İlk ve son cümle iki yöntemi yan yana koyar: her biri kazandırır, her biri geri alır.','karşılaştırma: kazanç ve kayıp'),
 'Parça iki yöntemi karşılaştırıyor; şık ikisini birden kapsamalı.')

S('0018','konu','zor','C','orman ağı',
 'Ormanın altında, ağaçların kökleriyle iç içe geçmiş ince mantar telleri bir ağ oluşturur. Bu ağ sayesinde bir ağaç, topraktan topladığı mineralleri komşusuyla paylaşabilir; karşılığında ağaçtan şeker alan mantar da beslenir. Araştırmacılar, zayıf düşen bir ağaca yakındaki daha güçlü ağaçlardan bu ağ yoluyla besin aktarıldığını gözlemlemiştir. Yer üstünden hiç görünmeyen bu alışveriş, ağaçların yalnızca birbirine rakip olduğu varsayımını sarsmıştır. Bilim insanları bu yapıya kimi zaman ormanın gizli ağı adını verir. Ağın ne kadar geniş olduğu hâlâ tam bilinmese de ormanın görünmeyen bir paylaşım düzeni taşıdığı artık kabul edilmektedir. Bu durum, ormanı tek tek ağaçların toplamı olarak değil, birbirine bağlı bir topluluk olarak düşünmeyi gerektirir.',
 'Ormanı topluluk yapan ağaç–mantar ilişkisi',
 [('Mantarların ağaç köklerinden beslenme biçimleri','dar','Mantarın ağaçtan şeker alması parçanın yalnız bir yönüdür; karşılıklı alışveriş ve topluluk fikri dışarıda kalır.','dikkat'),
  ('Zayıf ağaçların güçlü ağaçlardan yardım alması','dar','Parçadaki gözlemin yalnız bir bölümüdür; mantar ağı ve topluluk anlayışı kapsanmaz.','dikkat'),
  ('Orman toprağının mineral bakımından zenginliği','yok','Parça mineralleri paylaşım bağlamında anar; toprağın zenginliği konu edilmez.','bilgi'),
  ('Ormanların tek tek ağaçlardan oluşan bir yapı olması','ters','Parça ormanı “tek tek ağaçların toplamı olarak değil” düşünmeyi önerir.','bilgi')],
 ('Mantar ağı ağaçları birbirine bağlıyor; orman bir topluluk olarak düşünülmeli.','ağaç + mantar → topluluk'),('Son cümle, ağ ilişkisinin orman anlayışına yansımasını verir; yani konu tek bir ayrıntı değil ilişkinin bütünüdür.','konu: ağ ilişkisi + topluluk'),
 'Şıklardan hangisi hem mantarı hem ağacı hem de topluluk fikrini içeriyor?')

S('0019','baslik','kolay','B','leylek göçü',
 'Leylekler, sonbahar geldiğinde binlerce kilometre uzaktaki sıcak bölgelere doğru yola çıkar. Yolculuk haftalar sürer ve kimi zaman iki üç kıtayı aşar. Yön bulmak için güneşin konumundan ve yeryüzü şekillerinden yararlanırlar. Sürüler hâlinde, çoğunlukla gündüz uçarlar; geceleri tarlalara ve sulak alanlara konup dinlenirler. Bu uzun yol, her yıl yinelenir. Yolculuk boyunca yorulduklarında yükselen sıcak hava akımlarına kanatlarını açıp kendilerini bırakır, böylece enerji harcamadan yükselirler.',
 'Leyleklerin Uzun Göç Yolculuğu',
 [('Kuşların Yuva Yapma Alışkanlıkları','yok','Parçada yuvadan hiç söz edilmez.','bilgi'),
  ('Sıcak Hava Akımlarının Oluşumu','dar','Sıcak hava akımları yalnızca yolculukta kullanılan bir yöntemdir; oluşumu anlatılmaz.','dikkat'),
  ('Güneşin Canlılar Üzerindeki Etkisi','genel','Güneş yalnız yön bulmada anılır; başlık parçayı aşar ve çok geniştir.','dikkat'),
  ('Kış Aylarında Kuşların Beslenmesi','yok','Parçada beslenmeden söz edilmez.','bilgi')],
 ('Leylekler göç eder, yön bulur, sıcak hava akımlarını kullanır.','konu: göç yolculuğu'),('Parçadaki bütün cümleler leyleğin yolculuğuyla ilgilidir; yön bulma ve enerji tasarrufu yolculuğun ayrıntılarıdır.','başlık: yolculuk'),
 'Başlık yolculuğu mu, yalnız bir ayrıntıyı mı adlandırıyor?')

S('0020','baslik','orta','D','onarım anlayışı',
 'Kırılan bir fincanı atmak yerine çatlakları altın tozuyla onaran bir gelenek, kusuru gizlemek yerine onu parlatıp nesnenin tarihine dönüştürür. Bir çatlak, burada utanılacak bir iz değil, nesnenin yaşadığı bir olayın kanıtıdır. Onarılan fincan, yeni bir fincandan daha çok dikkat çeker; bakan kişi çatlakların izini izleyerek nesnenin geçmişini okur. Böyle bir bakışta eskimek değer kaybı sayılmaz; yeni izler nesneyi biricik kılar. Bugün her şeyin kolayca yenisiyle değiştirildiği bir dünyada bu bakış, nesneyle kurduğumuz bağı yeniden düşündürüyor.',
 'Kusuru Değerli Kılan Onarım Anlayışı',
 [('Fincan Üretiminde Kullanılan Malzemeler','yok','Parça üretimi değil, kırılan fincanın onarımını anlatır.','bilgi'),
  ('Eskiyi Atıp Yeniyi Almanın Yararları','ters','Parça bu davranışı sorgular; yararlarını anlatmaz.','bilgi'),
  ('Altının Sanatta Kullanımı','dar','Altın tozu yalnızca onarımda kullanılan bir araçtır; konu onarım anlayışıdır.','dikkat'),
  ('Nesnelerin Zamanla Eskimesi','genel','Çok geniş bir başlıktır; parçadaki onarım ve kusuru değerli görme anlayışını yansıtmaz.','dikkat')],
 ('Kırık fincan altınla onarılıyor; çatlak değer kazanıyor.','onarım → kusur = tarih'),('Parçanın merkezinde kusuru gizlememek ve onu değerli saymak vardır.','başlık: onarım + değer'),
 'Başlıkta hem onarım hem kusura bakış yer almalı.')

S('0021','amac','kolay','C','gök gözlemi',
 'Gökyüzüne bakmak için teleskop ya da gözlemevi gerekmez; açık bir gecede şehrin ışıklarından biraz uzaklaşmak yeterlidir. Gökyüzüne ilk baktığınızda yalnızca birkaç yıldız görürsünüz; gözler karanlığa alıştıkça sayı hızla artar. Çıplak gözle bile Ay’ın kraterleri, parlak gezegenler ve yıldız kümeleri seçilebilir. Bunun için özel bir bilgi de gerekmez. Önemli olan, merakla başını kaldırmak ve beklemeyi bilmektir. Gökyüzü, ona vakit ayıranlara her zaman bir şey gösterir.',
 'Gök gözlemi için araçtan çok merak ve sabır gerektiğini',
 [('Gözlemevlerinin gökbilim eğitimi için vazgeçilmez olduğunu','ters','Parça teleskop ya da gözlemevinin gerekmediğini söyler.','bilgi'),
  ('Şehir ışıklarının gök gözlemini tümüyle olanaksız kıldığını','ters','Parça ışıklardan biraz uzaklaşmanın yeterli olduğunu söyler.','bilgi'),
  ('Gezegenlerin çıplak gözle her zaman seçilebileceğini','genel','Parça “parlak gezegenler” der; “her zaman” genellemesi parçada yoktur.','dikkat'),
  ('Ay’ın kraterlerinin yıldız kümelerinden kolay görüldüğünü','yok','Parça ikisinin görünme kolaylığını karşılaştırmaz.','bilgi')],
 ('Gök gözlemi için araç gerekmez; merak ve bekleme yeter.','araç ✗ → merak + sabır ✓'),('“Önemli olan” ifadesi yazarın vurguladığı yargıyı verir: merak ve beklemek.','vurgu: merak + sabır'),
 '“Önemli olan” sözcükleri yazarın asıl vurgusunu gösterir.')

S('0022','amac','orta','E','başarının ölçüsü',
 'Bir yarışta herkes birinci olmak ister; ama yarış bittiğinde birinci yalnızca bir kişidir. Geri kalanların yıllarca süren emeği sıralamada bir numaraya dönüşür ve unutulur. Oysa antrenmanda her sabah kalkmayı başaran, sakatlıktan sonra yeniden koşmaya dönen, bir öncekinden daha iyi derece yapan herkes kendi yolunda kazanmıştır. Maratonun son kilometrelerinde bile bırakmayan, bitiş çizgisine son sırada giren bir koşucu, alkışı en çok hak edenlerden biri olabilir; çünkü onun asıl rakibi çoğu zaman diğer koşucular değil, kendi yorgunluğudur. Başarıyı yalnızca podyumda ölçmek, çabanın büyük bölümünü görünmez kılar.',
 'Başarının yalnızca sonuçla değil süreçle de ölçülmesi gerektiğini',
 [('Yarışlarda birinciliğin sporcular için gereksiz olduğunu','ters','Parça birinciliğin istendiğini kabul eder; amacı birinciliği gereksiz saymak değildir.','bilgi'),
  ('Antrenman düzeninin yarış başarısını belirleyen tek etken olduğunu','genel','Parça antrenmanı bir çaba örneği olarak anar; “tek etken” iddiası yoktur.','dikkat'),
  ('Sakatlanan sporcuların yarışlardan çekilmesi gerektiğini','yok','Parça sakatlıktan sonra dönenleri över; çekilmeyi önermez.','bilgi'),
  ('Geride kalan sporcuların unutulmasının doğal olduğunu','ters','Parça bu unutulmayı eleştirir; doğal saymaz.','bilgi')],
 ('Birinci tek kişi; yazar sıralamanın dışında kalan emeği görünür kılmak istiyor.','sonuç + süreç'),('“Oysa” ile yazar kazanmayı sonuçtan çıkarıp sürece taşır; son cümle bunu bağlar.','amaç: süreci de say'),
 'Yazarın eleştirdiği ölçü ile savunduğu ölçüyü ayır.')

S('0023','amac','orta','B','müzede bakmak',
 'Müzelerde insanlar çoğu zaman eserin önünde birkaç saniye durur, etiketi okur ve geçer. Kalabalık salonlarda gezen kişi her tabloyla kısacık bir tanışıklık kurar ve çıkışta hangi eseri gördüğünü hatırlamakta zorlanır. Oysa bir eser, ancak ona vakit tanıyan kişiye kendini açar. Aynı tabloya on dakika bakan biri ilk bakışta fark etmediği bir ayrıntıyı, bir ışık oyununu ya da sanatçının çekingen bir fırça darbesini bulabilir. Müzede çok şey görmek ile görmeyi öğrenmek aynı şey değildir.',
 'Eseri anlamanın, çok görmekten çok dikkatle bakmaya bağlı olduğunu',
 [('Müzelerdeki etiket yazılarının daha ayrıntılı hazırlanması gerektiğini','yok','Parça etiketten yalnızca ziyaretçinin hızlı davranışı bağlamında söz eder; etiketi eleştirmez.','dikkat'),
  ('Sanatçıların fırça darbelerini bilinçli biçimde gizlediğini','ters','Parça çekingen fırça darbesini bakan kişinin fark edebileceği bir ayrıntı olarak anar; sanatçının gizlediğini söylemez.','bilgi'),
  ('Müze ziyaretçisi sayısının sanat anlayışının düzeyini yansıttığını','yok','Parçada ziyaretçi sayısına ilişkin bir değerlendirme yoktur.','bilgi'),
  ('Tabloya uzun süre bakıldıkça eserin değerinin arttığını','genel','Parça eserin değerinin değil, fark edilen ayrıntıların arttığını söyler.','dikkat')],
 ('Ziyaretçiler hızlı geçiyor; yazar eseri anlamanın uzun bakmayla olduğunu söylüyor.','hızlı bakış ✗ → dikkatli bakış ✓'),('Son cümle çok görmek ile görmeyi öğrenmek arasındaki farkı vurgular.','çok görmek ≠ görmeyi öğrenmek'),
 'Son cümledeki karşıtlık yazarın amacını açık ediyor.')

S('0024','amac','zor','A','dil ve düşünce',
 'Bir dilde bir şeyi adlandıracak sözcük yoksa o şeyi düşünmek de zorlaşır; ama bu, düşüncenin yalnızca dil tarafından belirlendiği anlamına gelmez. Bir müzisyen, bir ezginin adını bilmese de onu çalabilir; bir çocuk, “özgürlük” sözcüğünü öğrenmeden önce de engellendiğinde itiraz eder. Gündelik dilde bile bunu görürüz: aradığımız sözcüğü bulamadığımızda elimizle bir şey gösterir, sonra o şeyi tarif etmeye başlarız. Düşünce önce bulanık bir sezgi olarak belirir, dile geldikçe netleşir; ama dile getirilemeyen her sezgi yok olmuş sayılmaz. Dil, düşünceyi taşıyan bir araç olduğu kadar onu keskinleştiren bir bileydir de. Düşünce ile dil arasındaki bağı tek yönlü bir ilişki gibi sunanlar, olgunun karmaşıklığını sadeleştirmiş olurlar.',
 'Dil ile düşünce arasındaki ilişkinin tek yönlü olmadığını',
 [('Adlandırılamayan şeylerin hiçbir biçimde düşünülemeyeceğini','genel','Parça adlandırılamayan şeyi düşünmenin “zorlaştığını” söyler; imkânsız demez ve bu görüşü sınırlar.','dikkat'),
  ('Çocukların sözcükleri öğrenmeden önce de tepki verebildiğini','dar','Parçadaki çocuk örneğidir; ana vurgu ilişkinin iki yönlülüğüdür.','dikkat'),
  ('Müzisyenlerin dil kullanmadan düşünebildiğini','dar','Müzisyen örneği yalnız adını bilmeden çalabilmeyi gösterir; parçanın tamamını kapsamaz.','dikkat'),
  ('Dilin düşünceyi yalnızca taşıyan bir araçtan ibaret olduğunu','dar','Parça dilin düşünceyi keskinleştirdiğini de söyler; şık yalnız yarısını kapsar.','dikkat')],
 ('Dil düşünceyi etkiler ama belirlemez; düşünce de dili etkiler.','dil ⇄ düşünce'),('Son cümle, ilişkiyi tek yönlü sunanları eleştirir; asıl yargı iki yönlülüktür.','amaç: iki yönlü ilişki'),
 'Son cümlede yazarın eleştirdiği görüş hangisi?')

S('0025','amac','zor','D','dijital saklama',
 'Eski bir mektubu kâğıttan okumak yıllar sonra bile mümkündür; oysa on beş yıl önce bir disketle kaydettiğimiz dosyayı bugün açabilmek için çoğumuzun elinde okuyucu bile yoktur. Veriyi büyük miktarlarda ve ucuza saklayabilmek, onu uzun süre koruyabilmek anlamına gelmiyor. Biçimler değişiyor, cihazlar eskiyor, eski kayıtların anahtarı kayboluyor. Bu yüzden arşivlerin asıl işi artık raflara belge dizmek değil, eski biçimdeki kayıtları yenilerine düzenli olarak aktarmaktır. Aktarma yapılmazsa bugün sıradan görünen bir dosya, birkaç on yıl sonra çözülemeyen bir şifreye dönüşebilir. Üstelik saklamanın ucuzlaması, bakımın önemini unutturan bir rahatlık doğuruyor. Bellek, yalnızca depolama kapasitesiyle değil, saklananın yarın okunabilir kalmasını sağlayan bakımla ayakta durur.',
 'Verinin kalıcılığının bakıma bağlı olduğunu',
 [('Kâğıt belgelerin dijital kayıtlardan daha ucuza saklandığını','ters','Parça ucuz ve büyük miktarda saklamanın dijital veri için mümkün olduğunu söyler.','bilgi'),
  ('Disketlerin yeniden üretilmesi gerektiğini','yok','Disket yalnızca bir örnektir; yeniden üretim önerisi parçada yoktur.','bilgi'),
  ('Eski cihazların toplanıp sergilenmesi gerektiğini','yok','Parçada sergileme önerisi yoktur.','bilgi'),
  ('Dijital depolamanın artık gereksiz hâle geldiğini','ters','Parça depolamanın yetmediğini söyler; gereksiz saymaz.','dikkat')],
 ('Dijital veri ucuz saklanır ama okunabilir kalması bakım ister.','saklamak ≠ korumak'),('Son cümle “yalnızca … değil, … bakımla” diyerek yazarın vurguladığı yargıyı verir.','vurgu: bakım + okunabilirlik'),
 'Yazarın depolama kapasitesi hakkındaki yargısına dikkat et.')

print('UYARI',ERR)
assert not ERR
assert len(Q.P.ANA)==Q.n,len(Q.P.ANA)
bitir(Q)
