"""TYT Türkçe · Yazım Kuralları (dil bilgisi genişletmesi, ikinci yarı): 24 soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
KARTLAR={
 'K-DBYZB-01':dict(alt='Yardımcı Fiille Kurulan Birleşik Fiiller',fikir='Ses düşmesi ya da türemesi olan birleşik fiillerin bitişik (hissetmek, kaybolmak), olmayanların ayrı (yardım etmek) yazıldığını ayırmak.',tuzak='Her “etmek/olmak” birleşiğini ayrı ya da hepsini bitişik yazmak.',zorluk='orta',kalip='düz',adim=3,tipId='dyzb-yardimci',kaynak=KY),
 'K-DBYZB-02':dict(alt='Anlam Kayması ve Zarf-Fiille Kurulan Fiiller',fikir='Anlamı kaymış bitişik adları (hanımeli, aslanağzı) ve -a/-e/-ı/-i zarf-fiilli bileşik fiilleri (yapabilmek, düşüvermek) bitişik; -ıp/-arak gibi biçimleri ayrı yazmak.',tuzak='Zarf-fiilli bileşik fiilleri ayırmak, -ıp’lı yapıları bitiştirmek, anlamı kaymış adı ayrı yazmak.',zorluk='zor',kalip='düz',adim=3,tipId='dyzb-kayma',kaynak=KY),
 'K-DBYZB-03':dict(alt='Pekiştirme ve İkilemelerin Yazımı',fikir='Pekiştirmeli sözcükleri bitişik (masmavi), ikilemeleri ayrı yazmak; ikilemenin aralarına virgül ya da kısa çizgi koymamak.',tuzak='Pekiştirmeyi ayırmak, ikilemeyi bitiştirmek ya da araya işaret koymak.',zorluk='orta',kalip='düz',adim=3,tipId='dyzb-pekistirme',kaynak=KY),
 'K-DBYZB-04':dict(alt='Yazılışı Karıştırılan Sözcükler',fikir='Herkes, yalnız, yanlış, birkaç, hiçbir, herhangi, şoför, sürpriz, kirpik gibi sözcüklerin ve “her şey, her gün” gibi ayrı yazılanların doğru biçimini bilmek.',tuzak='Söyleyişe bakıp harf değiştirmek; bitişik sözcüğü ayırmak, ayrı olanı bitiştirmek.',zorluk='orta',kalip='düz',adim=3,tipId='dyzb-karisan',kaynak=KY),
 'K-DBYZB-05':dict(alt='“Bir” ile Kurulan Sözcükler ve “-ki” li Bağlaçlar',fikir='Birbiri, birdenbire, biraz bitişik; bir an, bir gün, bir daha, bir şey ayrı; sanki, çünkü, belki gibi kalıplaşmış bağlaçları bitişik yazmak.',tuzak='“Bir” sözcüğünü hep bitişik ya da hep ayrı sanmak; bağlaçtaki “ki”yi ayırmak.',zorluk='orta',kalip='düz',adim=3,tipId='dyzb-bir',kaynak=KY),
 'K-DBYZB-06':dict(alt='Karışık Yazım Parçası',fikir='Bir parçadaki numaralı yerlerde bitişik/ayrı yazım, pekiştirme, ikileme ve karışan sözcük kurallarını birlikte uygulamak.',tuzak='Bir kuralı iyi bilip öteki numaralı yerleri atlamak.',zorluk='zor',kalip='öncüllü',adim=4,tipId='dyzb-parca',kaynak=KY),
}
TIPLER={'dyzb-yardimci':'Yardımcı fiille birleşik fiiller','dyzb-kayma':'Anlam kayması ve zarf-fiille kurulan fiiller','dyzb-pekistirme':'Pekiştirme ve ikileme yazımı','dyzb-karisan':'Yazılışı karıştırılan sözcükler','dyzb-bir':'“Bir” ile kurulanlar ve “-ki” li bağlaçlar','dyzb-parca':'Karışık yazım parçası'}
Q=kur('dyazimb','Yazım Kuralları','tr|Yazım Kuralları',KARTLAR,TIPLER); Q.n=24

B_YF=B('Yardımcı fiille birleşikler','ses düşmesi/türemesi olanlar bitişik: hissetmek (his+etmek), kaybetmek, kaybolmak, kaydetmek · olmayanlar ayrı: yardım etmek, kabul etmek, teşekkür etmek')
B_KY=B('Anlam kayması ve zarf-fiil','anlamı kaymış ad: hanımeli, aslanağzı, karaciğer, kuşburnu (bitişik) · -a/-e/-ı/-i ile kurulan bileşik fiil bitişik: yapabilmek, düşüvermek, bakakalmak, uyuyakalmak · -ıp ile ayrı: koşup gelmek')
B_PK=B('Pekiştirme','pekiştirmeli sözcük tek sözcüktür, bitişik yazılır: masmavi, yemyeşil, kıpkırmızı, dopdolu, sımsıkı')
B_IK=B('İkileme','ikileme iki sözcüktür, ayrı yazılır; aralarına virgül ya da kısa çizgi konmaz: ağır ağır, ufak tefek, eğri büğrü, pırıl pırıl')
B_KR=B('Karıştırılan sözcükler','bitişik: herkes, yalnız, yanlış, birkaç, hiçbir, herhangi, bugün, şoför, sürpriz, kirpik, orijinal · ayrı: her şey, her gün, hiçbir şey')
B_BR=B('“Bir” ile kurulanlar','bitişik: birbiri, birdenbire, biraz, birazdan, birlikte, birkaç · ayrı: bir an, bir gün, bir daha, bir şey, bir de')
B_KI=B('“-ki” li bağlaçlar','sanki, belki, çünkü tek sözcüktür ve bitişik yazılır; “ki” ayrı yazılmaz (çün ki ✗) · “madem”, “oysa” da tek sözcüktür')

def bc(no,kart,zor,kaz,adim,kok,opts,harf,ask,ist,ip,bilgi,kural,kisa_kural,sonuc,puf):
    """Beş cümle. opts: (metin,etiket,cel,tur,kisa). ask: Y ya da D (aranan etiket)."""
    o4=[(m,e,c,t) for m,e,c,t,k in opts]
    isl=' · '.join(f"{'ABCDE'[i]}: {x[4]}" for i,x in enumerate(opts))
    ad=[AD('Kuralı hatırla',kural,kisa_kural),AD('Şıkları tek tek sına','Her cümledeki sınanan yazımı kurala göre denetle.',isl),AD('Sonucu seç',sonuc,f"cevap {harf}")]
    soru(Q,no,kart,zor,kaz,adim,kok,o4,harf,lambda e:e==ask,ist,ip,bilgi,ad,puf)
def parca(no,kart,zor,kaz,adim,pasaj,items,harf,ask,ist,ip,bilgi,kural,kisa_kural,sonuc,puf,kok=None):
    """Numaralı parça. items: 5 × (etiket,kisa,cel); cel her numara için ≥12 karakter."""
    R=['I','II','III','IV','V']
    if kok is None: kok='Bu parçada numaralanmış sözcük ya da sözcük öbeklerinden hangisinin yazımı yanlıştır?' if ask==Y else 'Bu parçada numaralanmış sözcük ya da sözcük öbeklerinden hangisinin yazımı doğrudur?'
    o4=[(R[i],e,c,'bilgi') for i,(e,k,c) in enumerate(items)]
    isl=' · '.join(f"{R[i]}: {x[1]}" for i,x in enumerate(items))
    ad=[AD('Kuralı hatırla',kural,kisa_kural),AD('Numaraları tek tek sına','Parçadaki her numaralı yeri ayrı ayrı denetle.',isl),AD('Sonucu seç',sonuc,f"cevap {R['ABCDE'.index(harf)]}")]
    soru(Q,no,kart,zor,kaz,adim,pasaj+'\n\n'+kok,o4,harf,lambda e:e==ask,ist,ip,bilgi,ad,puf,kalip='öncüllü')

# ---- 0001 kolay · C
bc('0001','K-DBYZB-01','kolay','Yardımcı fiille kurulan birleşik fiillerin bitişik/ayrı yazımını ayırt eder.',2,
 'Aşağıdaki cümlelerin hangisinde yardımcı fiille kurulan birleşik fiilin yazımı yanlıştır?',
 [('Yolcular kaybolan çantayı havaalanında aradı.',D,'“Kaybolmak” ses olayı (ünlü düşmesi) nedeniyle bitişik yazılır; doğrudur.','bilgi','kaybolan ✓'),
  ('Öğretmenimiz bize çok yardım etti.',D,'“Yardım etmek”te ses olayı yoktur, ayrı yazılır; doğrudur.','bilgi','yardım etti ✓'),
  ('Sınavdan sonra büyük bir rahatlık his ettim.',Y,'','','his ettim ✗'),
  ('Kardeşim ders notlarını defterine kaydetti.',D,'“Kaydetmek” ünlü düşmesiyle (kayıt → kayd-) bitişik yazılır; doğrudur.','bilgi','kaydetti ✓'),
  ('Çocuk annesine teşekkür etti ve odasına çıktı.',D,'“Teşekkür etmek” ses olayı olmadığı için ayrı yazılır; doğrudur.','dikkat','teşekkür etti ✓')],
 'C',Y,'Birleşik fiilin yazımı yanlış olan cümle.','Birleşik fiilin ilk sözcüğünde ses düşmesi ya da türemesi var mı diye bak.',[B_YF],
 'Yardımcı fiille kurulan birleşiklerde ses olayı varsa bitişik, yoksa ayrı yazılır.','ses olayı: bitişik · yok: ayrı',
 'C’de “his” sözcüğünde ses türemesi vardır, “hissetmek” bitişik yazılmalıdır; öteki dört cümlede yazım doğrudur.',
 '“His” sözcüğünün sonundaki ünlü ünsüzü ikizleştirir (his → hiss-etmek); ses olayı görürsen bitişik yaz.')

# ---- 0002 orta · A
bc('0002','K-DBYZB-01','orta','Ses olayına bakarak yardımcı fiilli birleşiklerin doğru yazımını seçer.',3,
 'Hangi cümledeki birleşik fiil kurala uygun yazılmıştır?',
 [('Annem bize sabretmenin önemini anlattı.',D,'','','sabretmek ✓'),
  ('Müdür öğrencilerin isteğini kabuletti.',Y,'“Kabul etmek”te ses olayı yoktur; ayrı yazılmalıdır: “kabul etti”.','bilgi','kabuletti ✗'),
  ('Küçük kardeşim ağlayarak yardımetmemi istedi.',Y,'“Yardım etmek” ayrı yazılır; “yardımetmemi” yanlıştır.','bilgi','yardımetmemi ✗'),
  ('Bakkal yeni gelen ürünü müşterilere tavsiyeetti.',Y,'“Tavsiye etmek”te ses olayı yoktur; ayrı yazılmalıdır.','bilgi','tavsiyeetti ✗'),
  ('Hasta doktorun uyarılarına dikkatetmedi.',Y,'“Dikkat etmek” ayrı yazılır; “dikkatetmedi” yanlıştır.','dikkat','dikkatetmedi ✗')],
 'A',D,'Yazım yanlışı bulunmayan cümle.','Her birleşik fiilde ses düşmesi/türemesi var mı diye bak.',[B_YF],
 'Ses olayı olmayan birleşik fiiller ayrı, olanlar bitişik yazılır.','sabır → sabretmek (ses düşmesi)',
 'B, C, D ve E’de ses olayı olmayan birleşik fiiller yanlışlıkla bitişik yazılmış; yalnız A’daki “sabretmek” bitişik yazılması gereken bir fiildir.',
 '“Hatasız olan” sorusunda yanlışı çok olan şıklardan değil, tek doğru kalandan git.')

# ---- 0003 orta · D (IV)
parca('0003','K-DBYZB-01','orta','Parçadaki birleşik fiillerin yazımını numaralı yerlerde denetler.',3,
 'Kış tatilinde dağ köyüne gittik. Sisin içinde yolu kaybetmemek (I) için yavaş ilerledik. Köye varınca soğuğu iliklerimize kadar hissettik (II). Köylüler bizi evlerine aldı, hepsi yardım etmeye (III) çalıştı. Ev sahibimize teşekkürettiğimizde (IV) gülümsedi. Dönerken bu güzel günler için içimizden şükrettik (V).',
 [(D,'kaybetmek ✓','“Kaybetmek” ses olayı (kayıp → kayb-) nedeniyle bitişik yazılır; doğrudur.'),
  (D,'hissetmek ✓','“Hissetmek” ses türemesiyle bitişik yazılır; doğrudur.'),
  (D,'yardım etmek ✓','“Yardım etmek” ayrı yazılır; doğrudur.'),
  (Y,'teşekkürettiğimizde ✗',''),
  (D,'şükretmek ✓','“Şükretmek” ünlü düşmesiyle bitişik yazılır; doğrudur.')],
 'D',Y,'Yazımı yanlış olan numaralı yer.','Her numaralı birleşik fiilde ses olayı var mı, yok mu?',[B_YF],
 'Ses olayı olan birleşik fiiller bitişik, olmayanlar ayrı yazılır.','ses olayı: bitişik · yok: ayrı',
 'IV’teki “teşekkür etmek” ses olayı taşımadığından ayrı yazılmalıdır; öteki numaralı yerler kurala uygundur.',
 'Ses olayı olmayan birleşik fiili bitişik yazmak sık yapılan bir hatadır.')

# ---- 0004 orta · B (II)
parca('0004','K-DBYZB-01','orta','Birleşik fiilleri bağlam içinde bitişik/ayrı yazım bakımından ayırt eder.',3,
 'Okul gezisinde kalabalığın içinde kaybolduğunu (I) fark eden Elif önce çok korktu. Ne yapacağını bilemediği için bir süre hiçbir şey his edemedi (II). Sonra sakinleşip öğretmeninin uyarılarını aklına getirdi. Yoldan geçen bir görevliden yardım etmesini (III) rica etti (IV). Kısa süre sonra arkadaşlarına kavuştu ve yaşadığı bu olayı defterine kaydetti (V).',
 [(D,'kaybolmak ✓','“Kaybolmak” bitişik yazılır; doğrudur.'),
  (Y,'his edemedi ✗',''),
  (D,'yardım etmek ✓','“Yardım etmek” ses olayı olmadığı için ayrı yazılır; doğrudur.'),
  (D,'rica etti ✓','“Rica etmek” ayrı yazılır; doğrudur.'),
  (D,'kaydetmek ✓','“Kaydetmek” ünlü düşmesiyle bitişik yazılır; doğrudur.')],
 'B',Y,'Yazımı yanlış olan numaralı yer.','Ses olayı olan birleşik fiil hangisinde ayrı yazılmış?',[B_YF],
 '“His” ile “etmek” birleşirken ses türemesi olur ve fiil bitişik yazılır.','his → hissetmek',
 'II’deki “hissedemedi” bitişik yazılmalıdır (his + etmek, ses türemesi); öteki yerler doğrudur.',
 '“Hissetmek, kaybolmak, kaydetmek” bitişik; “yardım etmek, rica etmek” ayrı.')

# ---- 0005 kolay · E
bc('0005','K-DBYZB-02','kolay','Anlamı kaymış bitişik adların yazımını bilir.',2,
 'Aşağıdaki cümlelerin hangisinde yazım yanlışı vardır?',
 [('Duvarın dibindeki hanımeli çok güzel kokuyor.',D,'Anlamı kaymış “hanımeli” bitişik yazılır; doğrudur.','bilgi','hanımeli ✓'),
  ('Annem kış için kuşburnu çayı hazırladı.',D,'“Kuşburnu” bitki adı olarak bitişik yazılır; doğrudur.','bilgi','kuşburnu ✓'),
  ('Annem salataya biraz karabiber ekledi.',D,'“Karabiber” baharat adı olarak bitişik yazılır; doğrudur.','bilgi','karabiber ✓'),
  ('Bahçedeki aslanağzı çiçekleri açmıştı.',D,'Çiçek adı olan “aslanağzı” bitişik yazılır; doğrudur.','dikkat','aslanağzı ✓'),
  ('Doktor, hastanın kara ciğerini muayene etti.',Y,'','','kara ciğer ✗')],
 'E',Y,'Yazımı yanlış olan cümle.','Bu adların hangisi anlamı kayarak tek sözcük olmuştur ama ayrı yazılmış?',[B_KY],
 'Anlamı kaymış birleşik adlar bitişik yazılır.','hanımeli · aslanağzı · karaciğer',
 'E’de organ adı olan “karaciğer” bitişik yazılmalıdır; öteki dört adın yazımı doğrudur.',
 'Bir organ, bitki ya da baharat adı olarak anlamı kaymışsa birleşik ad bitişik yazılır.')

# ---- 0006 orta · B
bc('0006','K-DBYZB-02','orta','-a/-e/-ı/-i zarf-fiiliyle kurulan bileşik fiillerin bitişik yazımını uygular.',3,
 'Aşağıdaki cümlelerin hangisinde, zarf-fiil ekiyle kurulan bir fiilin bitişik/ayrı yazımında yanlışlık yapılmıştır?',
 [('Kitabı okuyup masanın üstüne bıraktı.',D,'“-ıp” zarf-fiiliyle kurulan yapı ayrı yazılır; doğrudur.','bilgi','okuyup bıraktı ✓'),
  ('Uzun yolculuktan sonra koltukta uyuya kaldı.',Y,'','','uyuya kaldı ✗'),
  ('Çocuk kapının önünde bir süre bakakaldı.',D,'“-a” zarf-fiili + “kalmak” bitişik yazılır; doğrudur.','dikkat','bakakaldı ✓'),
  ('Kedi yüksek duvardan aşağıya düşüverdi.',D,'“-ı” zarf-fiili + “vermek” (tezlik) bitişik yazılır; doğrudur.','bilgi','düşüverdi ✓'),
  ('Kardeşim kapıdan koşup geldi.',D,'“-ıp” zarf-fiiliyle kurulan yapı ayrı yazılır; doğrudur.','dikkat','koşup geldi ✓')],
 'B',Y,'Yazımı yanlış olan cümle.','Hangi fiilde -a/-e/-ı/-i zarf-fiili ile “kalmak” bitişik olması gerekirken ayrı yazılmış?',[B_KY],
 '-a/-e/-ı/-i zarf-fiilli bileşik fiiller bitişik, -ıp’lı yapılar ayrı yazılır.','-ıp: ayrı · -a/-ı + kal/ver: bitişik',
 'B’deki “uyuyakalmak” bitişik yazılmalıdır; A ve E’deki -ıp’lı yapılar ayrı yazıldığı için doğrudur.',
 '“-ıp” ile kurulanları ayır, “-a/-ı + kalmak, vermek, bilmek” bitişik yaz.')

# ---- 0007 zor · D
bc('0007','K-DBYZB-02','orta','Zarf-fiille kurulan bileşik fiilleri hem bitişik hem ayrı yazılan biçimlerle ayırt eder.',4,
 'Bu cümlelerden hangisi yazım bakımından hatasızdır?',
 [('Çocuk uçan balona uzun uzun baka kaldı.',Y,'“Bakakalmak” bitişik yazılır; “baka kaldı” yanlıştır.','bilgi','baka kaldı ✗'),
  ('Kapıyı çalmadan içeri gire verdi.',Y,'“Girivermek” tezlik fiilidir ve bitişik yazılır.','bilgi','gire verdi ✗'),
  ('Bu soruyu sen tek başına yapa bilir misin?',Y,'“Yapabilmek” bitişik yazılır; “yapa bilir” yanlıştır.','dikkat','yapa bilir ✗'),
  ('Sabah hava açınca bavulunu hazırlayıverdi.',D,'','','hazırlayıverdi ✓'),
  ('Marketten ekmek alıpgeldi.',Y,'“-ıp” zarf-fiiliyle kurulan yapı ayrı yazılır: “alıp geldi”.','bilgi','alıpgeldi ✗')],
 'D',D,'Yazım yanlışı bulunmayan cümle.','Hangi şıkta -a/-ı’lı bileşik fiil bitişik, -ıp’lı yapı ayrı yazılmış?',[B_KY],
 '-a/-e/-ı/-i zarf-fiilli bileşik fiil bitişik; -ıp’lı yapı ayrı yazılır.','-a/-ı + ver/kal/bil: bitişik · -ıp: ayrı',
 'A, B, C’de bitişik olması gerekenler ayrı, E’de ayrı olması gerekenler bitişik yazılmış; yalnız D’deki “hazırlayıverdi” kurala uygundur.',
 'Bitişik/ayrı yanlışı iki yönde olabilir; her şıkta yönü ayrı ayrı sına.')

# ---- 0008 zor · A (I)
parca('0008','K-DBYZB-02','zor','Anlam kayması ve zarf-fiilli fiillerin yazımını parçada denetler.',4,
 'Büyükannemin bahçesinde hanım eli (I) kokusu her yaza renk katar. Geçen hafta oraya gittiğimde aslanağzı (II) çiçeklerinin arasında yürürken bir arı yanımdan geçti. Bir süre arının ardından bakakaldım (III). Sonra çimlerde uzanıp uyuyakalmışım (IV). Uyandığımda akşam olmuş, dedem de bahçeye çıkagelmişti (V).',
 [(Y,'hanım eli ✗',''),
  (D,'aslanağzı ✓','Çiçek adı olarak anlamı kayan “aslanağzı” bitişik yazılır; doğrudur.'),
  (D,'bakakaldım ✓','“-a” zarf-fiili + “kalmak” bitişik yazılır; doğrudur.'),
  (D,'uyuyakalmışım ✓','“-ı” zarf-fiili + “kalmak” bitişik yazılır; doğrudur.'),
  (D,'çıkagelmişti ✓','“-a” zarf-fiili + “gelmek” bitişik yazılır; doğrudur.')],
 'A',Y,'Yazımı yanlış olan numaralı yer.','Bitki adı olan sözcük ve zarf-fiilli fiiller hangi numarada bozulmuş?',[B_KY],
 'Anlamı kaymış adlar ve -a/-ı zarf-fiilli bileşik fiiller bitişik yazılır.','hanımeli · bakakalmak · çıkagelmek',
 'I’de bitki adı olan “hanımeli” ayrı yazılmış; öteki numaralı yerlerin yazımı doğrudur.',
 'Bitki adı olan “hanımeli” tek sözcüktür; “hanım eli” yazılışı yanlıştır.')

# ---- 0009 kolay · C
bc('0009','K-DBYZB-03','kolay','Pekiştirmeli sözcüklerin bitişik yazıldığını bilir.',2,
 'Aşağıdaki cümlelerin hangisinde pekiştirmeli sözcüğün yazımı yanlıştır?',
 [('Sabah yağan karla bahçe bembeyaz olmuştu.',D,'“Bembeyaz” pekiştirmeli sözcüktür, bitişik yazılır; doğrudur.','bilgi','bembeyaz ✓'),
  ('Yaz boyunca kıpkırmızı domatesler yetiştirdik.',D,'“Kıpkırmızı” bitişik yazılır; doğrudur.','bilgi','kıpkırmızı ✓'),
  ('Odanın duvarları yem yeşil boyanmıştı.',Y,'','','yem yeşil ✗'),
  ('Çocuk sımsıkı tuttuğu elini bir türlü açmadı.',D,'“Sımsıkı” bitişik yazılır; doğrudur.','dikkat','sımsıkı ✓'),
  ('Eve döndüğünde simsiyah bir kedi kapıda bekliyordu.',D,'“Simsiyah” bitişik yazılır; doğrudur.','dikkat','simsiyah ✓')],
 'C',Y,'Pekiştirmeli sözcüğün yazımı yanlış olan cümle.','Pekiştirmeli sözcük tek sözcük müdür, iki sözcük mü?',[B_PK],
 'Pekiştirmeli sözcükler bitişik yazılır.','masmavi · yemyeşil',
 'C’de “yemyeşil” iki sözcük gibi ayrı yazılmış; öteki dört sözcük bitişik yazıldığı için doğrudur.',
 'Pekiştirme tek sözcüktür; ayrı yazılan pekiştirme yanlıştır.')

# ---- 0010 orta · E
bc('0010','K-DBYZB-03','orta','İkilemelerin ayrı yazıldığını, araya işaret konmadığını bilir.',3,
 'İkilemelerin yazımı bakımından aşağıdaki cümlelerin hangisinde hata yapılmıştır?',
 [('Çocuklar bahçede ağır ağır yürüyen kaplumbağayı izledi.',D,'“Ağır ağır” ikilemedir, ayrı yazılmıştır; doğrudur.','bilgi','ağır ağır ✓'),
  ('Kitap mitap okumayı pek sevmez, hep top oynar.',D,'“Kitap mitap” ikilemesi ayrı yazılmıştır; doğrudur.','bilgi','kitap mitap ✓'),
  ('Sokakta ufak tefek bir kız ağlıyordu.',D,'“Ufak tefek” ikilemesi ayrı yazılmıştır; doğrudur.','dikkat','ufak tefek ✓'),
  ('Bulutlar yavaş yavaş dağılınca güneş çıktı.',D,'“Yavaş yavaş” ikilemesi ayrı yazılmıştır; doğrudur.','dikkat','yavaş yavaş ✓'),
  ('Misafirler eğri-büğrü yoldan geçerek köye ulaştı.',Y,'','','eğri-büğrü ✗')],
 'E',Y,'Yazımı yanlış olan cümle.','İkilemenin aralarına bir işaret konmuş mu, bitişik mi yazılmış?',[B_IK],
 'İkilemeler ayrı yazılır, araya işaret konmaz.','ağır ağır · eğri büğrü',
 'E’de ikilemenin sözcükleri kısa çizgiyle bağlanmış; “eğri büğrü” ayrı yazılmalıdır. Öteki dört cümle doğrudur.',
 'İkilemede ne virgül ne kısa çizgi ne bitişik yazım olur; yalnız bir boşluk vardır.')

# ---- 0011 orta · B (II)
parca('0011','K-DBYZB-03','orta','Pekiştirme ve ikilemelerin yazımını parçada denetler.',3,
 'Hafta sonu ailecek kıra çıktık. Gökyüzü masmavi (I) bir örtü gibiydi, çimenler ise yem yeşil (II) görünüyordu. Çocuklar bir süre koşuşturup tepeden aşağı yuvarlandı, sonra yorulunca yavaş yavaş (III) yürüdü. Annem sepetten ufak tefek (IV) yiyecekler çıkardı. Dönerken torbayı sımsıkı (V) bağladık.',
 [(D,'masmavi ✓','“Masmavi” pekiştirmedir, bitişik yazılır; doğrudur.'),
  (Y,'yem yeşil ✗',''),
  (D,'yavaş yavaş ✓','“Yavaş yavaş” ikilemedir, ayrı yazılır; doğrudur.'),
  (D,'ufak tefek ✓','“Ufak tefek” ikilemedir, ayrı yazılır; doğrudur.'),
  (D,'sımsıkı ✓','“Sımsıkı” pekiştirmedir, bitişik yazılır; doğrudur.')],
 'B',Y,'Yazımı yanlış olan numaralı yer.','Pekiştirmelerden biri ayrı, ikilemelerden biri bitişik yazılmış olabilir; hangisi?',[B_PK,B_IK],
 'Pekiştirme bitişik, ikileme ayrı yazılır.','masmavi: bitişik · ağır ağır: ayrı',
 'II’deki “yemyeşil” pekiştirmedir ve bitişik yazılmalıdır; ikilemeler doğru yazılmıştır.',
 'Önce her numaranın pekiştirme mi ikileme mi olduğuna karar ver, sonra yazımına bak.')

# ---- 0012 zor · C
bc('0012','K-DBYZB-03','zor','Aynı cümledeki pekiştirme ve ikilemenin yazımını birlikte denetler.',4,
 'Aşağıdaki cümlelerin hangisinde hem pekiştirmeli sözcük hem ikileme doğru yazılmıştır?',
 [('Çocuk yem yeşil çimlerde koşa koşa eve geldi.',Y,'Pekiştirme “yemyeşil” bitişik yazılmalıdır; ikileme doğrudur ama cümle ölçütü karşılamaz.','bilgi','yem yeşil ✗'),
  ('Bembeyaz kar altında yavaşyavaş ilerlediler.',Y,'Pekiştirme doğrudur ama ikileme “yavaş yavaş” ayrı yazılmalıdır.','bilgi','yavaşyavaş ✗'),
  ('Sapsarı yapraklar yere hışır hışır dökülüyordu.',D,'','','sapsarı ✓ · hışır hışır ✓'),
  ('Simsiyah bulutlar toplanınca çocuklar koşa-koşa eve gitti.',Y,'Pekiştirme doğrudur ama ikilemede kısa çizgi kullanılmaz: “koşa koşa”.','dikkat','koşa-koşa ✗'),
  ('Yolda sap sağlam bir kütük bulup ağır ağır taşıdık.',Y,'İkileme doğrudur ama pekiştirme “sapasağlam” bitişik yazılmalıdır.','dikkat','sap sağlam ✗')],
 'C',D,'Hem pekiştirmenin hem ikilemenin doğru yazıldığı cümle.','Her şıkta iki yazımı da ayrı ayrı sına; ikisi birden doğru olan hangisi?',[B_PK,B_IK],
 'Pekiştirme bitişik, ikileme ayrı yazılır; araya işaret konmaz.','masmavi · ağır ağır',
 'A ve E’de pekiştirme, B ve D’de ikileme yanlış yazılmış; yalnız C’de iki yazım da doğrudur.',
 'İki koşullu sorularda her koşulu ayrı ayrı işaretle; ikisi de ✓ olan cevaptır.')

# ---- 0013 kolay · A
bc('0013','K-DBYZB-04','kolay','Yazılışı karıştırılan sözcüklerden “şoför”ün doğru yazımını bilir.',2,
 'Aşağıdaki cümlelerin birinde bir sözcük, söyleyişe uyularak yanlış yazılmıştır. Bu cümle hangisidir?',
 [('Annemin arkadaşı kasabadan gelen şöförle konuştu.',Y,'','','şöför ✗'),
  ('Doğum günümde herkes bana güzel bir sürpriz yaptı.',D,'“Herkes” ve “sürpriz” doğru yazılmıştır.','bilgi','herkes · sürpriz ✓'),
  ('Kızın uzun kirpikleri yanaklarına gölge düşürüyordu.',D,'“Kirpik” doğru yazılmıştır.','bilgi','kirpik ✓'),
  ('Yarınki toplantıya herhangi bir belge getirmedim.',D,'“Herhangi” bitişik yazılmıştır; doğrudur.','dikkat','herhangi bir ✓'),
  ('Bu işte yalnız kalmak istemedi.',D,'“Yalnız” doğru yazılmıştır.','dikkat','yalnız ✓')],
 'A',Y,'Yazımı yanlış olan cümle.','Hangi sözcüğün harfleri söyleyişe bakılarak yanlış yazılmış?',[B_KR],
 'Karıştırılan sözcüklerin doğru yazımı ezberlenir.','şoför · sürpriz · kirpik · yalnız',
 'A’da “şöför” yazılmış; doğrusu “şoför”dür (ilk ünlü o). Öteki dört cümledeki sözcükler doğru yazılmıştır.',
 'Alıntı sözcüklerde söyleyişe değil, Türkçe yazım kılavuzundaki biçime güven.')

# ---- 0014 orta · D
bc('0014','K-DBYZB-04','orta','Karıştırılan sözcüklerde bitişik/ayrı ve harf yazımını ayırt eder.',3,
 'Verilen cümlelerin hangisinde karıştırılan sözcüklerin yazımı doğrudur?',
 [('Hiçbirşey söylemeden masadan kalktı.',Y,'“Hiçbir şey” ayrı yazılır; “hiçbirşey” yanlıştır.','bilgi','hiçbirşey ✗'),
  ('Kardeşim yanlız başına bahçede oyun oynamıştı.',Y,'Doğru yazım “yalnız”dır; “yanlız” yanlıştır.','bilgi','yanlız ✗'),
  ('Herkez bu konuda aynı şeyi düşünüyordu.',Y,'Doğru yazım “herkes”tir; “herkez” yanlıştır.','bilgi','herkez ✗'),
  ('Dolapta herhangi bir çorap bulamadım.',D,'','','herhangi bir ✓'),
  ('Bu sene hemen herşey çok pahalı oldu.',Y,'“Her şey” ayrı yazılır; “herşey” yanlıştır.','dikkat','herşey ✗')],
 'D',D,'Yazım yanlışı bulunmayan cümle.','Dört şıkta bir sözcük bitişik ya da harf bakımından yanlış yazılmış.',[B_KR],
 'Karıştırılan sözcüklerin bitişik/ayrı ve harf yazımı bilinmelidir.','herkes · yalnız · herhangi · her şey',
 'A, B, C, E’de “hiçbir şey, yalnız, herkes, her şey” yanlış yazılmış; yalnız D’deki “herhangi bir” doğrudur.',
 '“Herhangi” bitişik, “her şey” ayrı yazılır; bu ikisi en sık karışan çifttir.')

# ---- 0015 zor · B
bc('0015','K-DBYZB-04','kolay','Sık kullanılan ama karışan sözcüklerin hepsini birlikte denetler.',4,
 'Şıklardan hangisinde bir sözcüğün yazılışında hata görülür?',
 [('Pazartesi günü okul bahçesinde bir sergi açılacak.',D,'“Pazartesi” bitişik yazılır; doğrudur.','bilgi','pazartesi ✓'),
  ('Annem rahatsızlanınca hastahaneye gittik.',Y,'','','hastahane ✗'),
  ('Bugün yağmur yağacağı için şemsiyemi aldım.',D,'“Bugün” bitişik yazılır; doğrudur.','dikkat','bugün ✓'),
  ('Kuaförde bir saat sıra bekledim.',D,'“Kuaför” doğru yazılmıştır.','dikkat','kuaför ✓'),
  ('Tecrübeli bir mühendis projeyi inceledi.',D,'“Tecrübeli” ve “mühendis” doğru yazılmıştır.','bilgi','tecrübeli · mühendis ✓')],
 'B',Y,'Yazımı yanlış olan cümle.','Hangi sözcükte fazladan bir hece vardır?',[B_KR],
 'Karıştırılan sözcüklerin doğru biçimini bil.','hastane · pazartesi · bugün',
 'B’de “hastane” sözcüğü “hastahane” biçiminde yazılmış; öteki dört cümledeki sözcükler doğrudur.',
 'Çıkaramadığın sözcükte yazımı hecelere ayırarak sına.')

# ---- 0016 orta · E (V)
parca('0016','K-DBYZB-04','orta','Karıştırılan sözcüklerin yazımını numaralı yerlerde sınar.',3,
 'Doğum günümde herkes (I) bana sürpriz (II) yapmak için gizlice plan kurmuştu. Sabah okula giderken yalnız (III) kalmak istediğimi söyledim ve hiçbir (IV) şeyden şüphelenmedim. Akşam eve girince ışıklar yandı, bir kaç (V) arkadaşım pastayla karşıma çıktı.',
 [(D,'herkes ✓','“Herkes” doğru yazılmıştır.'),
  (D,'sürpriz ✓','“Sürpriz” doğru yazılmıştır.'),
  (D,'yalnız ✓','“Yalnız” doğru yazılmıştır.'),
  (D,'hiçbir ✓','“Hiçbir” bitişik yazılır; doğrudur.'),
  (Y,'bir kaç ✗','')],
 'E',Y,'Yazımı yanlış olan numaralı yer.','Bitişik yazılması gereken bir sözcük ayrı yazılmış.',[B_KR],
 '“Herkes, yalnız, hiçbir, birkaç” doğru ve bitişik yazılır.','herkes · yalnız · hiçbir · birkaç',
 'V’teki “birkaç” bitişik yazılmalıdır; öteki sözcükler doğru yazılmıştır.',
 '“Birkaç” ve “hiçbir” bitişik yazılan en sık sözcüklerdir.')

# ---- 0017 zor · C (III)
parca('0017','K-DBYZB-04','zor','Karışan sözcüklerin yazımını bağlam içinde denetler.',4,
 'Eski otobüs durağında bekleyen yaşlı adam bana yardım istedi. Şoför (I) yanlış (II) yöne saptığı için yolcular geç kalmıştı. Adam elindeki biletin orjinal (III) olduğunu söyledi. Yaşlı adamın kirpikleri (IV) gözyaşından ıslanmıştı. Ona bir bardak su verip hiçbir (V) şey sormadım.',
 [(D,'şoför ✓','“Şoför” doğru yazılmıştır.'),
  (D,'yanlış ✓','“Yanlış” doğru yazılmıştır.'),
  (Y,'orjinal ✗',''),
  (D,'kirpik ✓','“Kirpik” doğru yazılmıştır.'),
  (D,'hiçbir ✓','“Hiçbir” bitişik, “şey” ayrı yazılır; doğrudur.')],
 'C',Y,'Yazımı yanlış olan numaralı yer.','Yabancı kökenli bir sözcüğün yazımında söyleyişe uyulmuş.',[B_KR],
 'Alıntı sözcüklerde söyleyişe değil kılavuzdaki yazıma güven.','orijinal',
 'III’teki “orjinal” yanlıştır; doğrusu “orijinal”dir. Öteki numaralı yerlerin yazımı doğrudur.',
 '“Orijinal” sözcüğünde “i” düşmez; söyleyişe değil yazıma bak.')

# ---- 0018 kolay · A
bc('0018','K-DBYZB-05','kolay','“Bir” ile kurulan sözcüklerin bitişik/ayrı yazımını ayırt eder.',2,
 '“Bir” sözcüğüyle kurulan yapılardan biri aşağıdaki cümlelerin hangisinde yanlış yazılmıştır?',
 [('Bu işi birdaha yapmayacağıma söz verdim.',Y,'','','birdaha ✗'),
  ('Birbirimize hiç yalan söylemedik.',D,'“Birbirimize” bitişik yazılır; doğrudur.','bilgi','birbirimize ✓'),
  ('Oyun birdenbire durdu ve herkes sustu.',D,'“Birdenbire” bitişik yazılır; doğrudur.','bilgi','birdenbire ✓'),
  ('Çantasından biraz su içti.',D,'“Biraz” bitişik yazılır; doğrudur.','dikkat','biraz ✓'),
  ('Bir gün seni ziyarete geleceğim.',D,'“Bir gün” ayrı yazılır; doğrudur.','dikkat','bir gün ✓')],
 'A',Y,'Yazımı yanlış olan cümle.','“Bir daha” bir sözcük müdür, iki sözcük mü?',[B_BR],
 'Birbiri, birdenbire, biraz bitişik; bir daha, bir gün ayrı yazılır.','birbiri · biraz: bitişik · bir daha: ayrı',
 'A’daki “bir daha” ayrı yazılmalıdır; öteki dört cümledeki sözcükler doğrudur.',
 '“Bir daha, bir gün, bir an, bir şey” ayrı; “birbiri, biraz, birdenbire” bitişik.')

# ---- 0019 orta · D
bc('0019','K-DBYZB-05','orta','“-ki” ile kalıplaşmış bağlaçların bitişik yazımını bilir.',3,
 'Bağlaçların yazımı bakımından hangi cümlede hata yapılmıştır?',
 [('Sanki hiçbir şey olmamış gibi gülümsüyordu.',D,'“Sanki” bitişik yazılır; doğrudur.','bilgi','sanki ✓'),
  ('Belki yarın hava düzelir.',D,'“Belki” bitişik yazılır; doğrudur.','bilgi','belki ✓'),
  ('Madem gelecektin, bize haber verseydin.',D,'“Madem” tek sözcüktür ve doğru yazılmıştır.','dikkat','madem ✓'),
  ('Çün ki hava çok soğuktu, dışarı çıkmadık.',Y,'','','çün ki ✗'),
  ('Ders çalışmadı, oysa başarılı olmak istiyordu.',D,'“Oysa” tek sözcüktür ve doğru yazılmıştır.','dikkat','oysa ✓')],
 'D',Y,'Yazımı yanlış olan cümle.','Bağlacın sonundaki “ki” ayrı yazılmış mı?',[B_KI],
 'Sanki, belki, çünkü tek sözcüktür; “ki” ayrı yazılmaz.','sanki · çünkü · belki: bitişik',
 'D’deki “çünkü” bitişik yazılmalıdır; öteki bağlaçlar bitişik yazılmıştır.',
 '“-ki” ile kalıplaşan bağlaçlarda ayrı yazılan “ki” hatadır.')

# ---- 0020 orta · A (I)
parca('0020','K-DBYZB-05','orta','“Bir” ile kurulan sözcüklerin yazımını parçada denetler.',3,
 'İki kardeş bir birine (I) çok benzerdi. Sabah birlikte (II) uyanırlar, bir şey (III) yemeden önce bahçede oyun oynarlardı. Biraz (IV) sonra annelerinin sesini duyarlardı. Bir gün (V) beni de oyuna çağırdılar.',
 [(Y,'bir birine ✗',''),
  (D,'birlikte ✓','“Birlikte” bitişik yazılır; doğrudur.'),
  (D,'bir şey ✓','“Bir şey” ayrı yazılır; doğrudur.'),
  (D,'biraz ✓','“Biraz” bitişik yazılır; doğrudur.'),
  (D,'bir gün ✓','“Bir gün” ayrı yazılır; doğrudur.')],
 'A',Y,'Yazımı yanlış olan numaralı yer.','“Birbiri” bitişik bir sözcüktür; ekli hâlinde de bitişik kalır.',[B_BR],
 'Birbiri, birlikte, biraz bitişik; bir şey, bir gün ayrı yazılır.','birbirine: bitişik',
 'I’deki “birbirine” bitişik yazılmalıdır; öteki numaralı yerlerin yazımı doğrudur.',
 '“Birbiri” ek aldığında da bitişik yazılır (birbirine, birbirimize).')

# ---- 0021 zor · B
bc('0021','K-DBYZB-05','zor','“Bir” ile kurulan yapıları ve “-ki” li bağlaçları aynı cümlede birlikte denetler.',4,
 'Aşağıdaki cümlelerden hangisinde “bir” ile kurulan yapıların ve bağlaçların yazımı doğrudur?',
 [('Sanki rüyadaymış gibi birden bire sustu.',Y,'“Birdenbire” bitişik yazılır; “sanki” doğru olsa da “birden bire” yanlıştır.','bilgi','sanki ✓ · birden bire ✗'),
  ('Sanki biraz yorulmuş gibi bir an durdu.',D,'','','sanki ✓ · biraz ✓ · bir an ✓'),
  ('Çünkü kimse birşey sormadı, biz de sustuk.',Y,'“Bir şey” ayrı yazılır; “çünkü” doğru olsa da “birşey” yanlıştır.','bilgi','çünkü ✓ · birşey ✗'),
  ('Belki birkaç gün bekleriz, çünki yol kapalı.',Y,'“Çünkü” ünlü uyumuyla yazılır; “birkaç” doğru olsa da “çünki” yanlıştır.','dikkat','birkaç ✓ · çünki ✗'),
  ('Belki yorulmuştu ama hiç bir şikâyet etmedi.',Y,'“Hiçbir” bitişik yazılır; “belki” doğru olsa da “hiç bir” yanlıştır.','dikkat','belki ✓ · hiç bir ✗')],
 'B',D,'Yazım yanlışı bulunmayan cümle.','Her cümlede “bir” ile kurulan yapıyı da bağlacı da ayrı ayrı sına.',[B_BR,B_KI],
 '“Bir” ile kurulan sözcüklerle bağlaçlardaki bitişik/ayrı ayrımını uygula.','birdenbire · bir şey · çünkü · hiçbir',
 'A’da “birden bire”, C’de “birşey”, D’de “çünki”, E’de “hiç bir” yanlış yazılmıştır; yalnız B’de üç yapının üçü de doğrudur.',
 'Her şıkta iki yapı varsa ikisini de sına; biri bozuksa şık elenir.')

# ---- 0022 zor · C (III)
parca('0022','K-DBYZB-06','orta','Birden çok yazım kuralını aynı parçada numaralı yerlerde uygular.',4,
 'Yeni evimize taşındığımızda herkes (I) bize yardım etmek (II) istedi. Komşularla kısa sürede bir birimize (III) alıştık. Annem teşekkür edip (IV) çay ikram etti. Sohbet sırasında hiçbir (V) şeyin eksik olmadığını fark ettik.',
 [(D,'herkes ✓','“Herkes” doğru yazılmıştır.'),
  (D,'yardım etmek ✓','“Yardım etmek” ayrı yazılır; doğrudur.'),
  (Y,'bir birimize ✗',''),
  (D,'teşekkür edip ✓','“Teşekkür etmek” ses olayı olmadığı için ayrı yazılır; doğrudur.'),
  (D,'hiçbir ✓','“Hiçbir” bitişik yazılır; doğrudur.')],
 'C',Y,'Yazımı yanlış olan numaralı yer.','Birbirine bağlı sözcüklerden biri ayrı yazılmış.',[B_YF,B_BR],
 'Birleşik fiilde ses olayı, “bir” sözcüklerinde bitişik/ayrı ayrımı aranır.','birbirimize: bitişik',
 'III’teki “birbirimize” bitişik yazılmalıdır; öteki numaralı yerlerin yazımı doğrudur.',
 'Karışık parçada her numaraya kuralını ayrı ayrı sor.')

# ---- 0023 zor · E (V)
parca('0023','K-DBYZB-06','orta','Pekiştirme, ikileme ve bileşik fiil yazımlarını bir parçada birlikte sınar.',4,
 'Yağmur dinince sokaklar pırıl pırıl (I) oldu. Çocuklar sapsarı (II) yağmurluklarıyla dışarı fırladı. Çünkü (III) bir saattir hepsi evde oturuyordu. Kimi kıpır kıpır (IV) zıplıyor, kimi de su birikintisine baka kalıyordu (V).',
 [(D,'pırıl pırıl ✓','“Pırıl pırıl” ikilemedir, ayrı yazılır; doğrudur.'),
  (D,'sapsarı ✓','“Sapsarı” pekiştirmedir, bitişik yazılır; doğrudur.'),
  (D,'çünkü ✓','“Çünkü” bağlacı bitişik yazılır; doğrudur.'),
  (D,'kıpır kıpır ✓','“Kıpır kıpır” ikilemedir, ayrı yazılır; doğrudur.'),
  (Y,'baka kalıyordu ✗','')],
 'E',Y,'Yazımı yanlış olan numaralı yer.','İkileme, pekiştirme, bağlaç ve bileşik fiil var; hangisi bozuk?',[B_IK,B_KY,B_KI],
 'İkileme ayrı; pekiştirme, bağlaç ve -a/-ı zarf-fiilli bileşik fiil bitişik yazılır.','ikileme: ayrı · bakakalmak: bitişik',
 'V’teki “bakakalıyordu” bitişik yazılmalıdır; öteki numaralı yerlerin yazımı doğrudur.',
 'Farklı kuralları birlikte sınayan parçada her numaranın türünü önce belirle.')

# ---- 0024 orta · D (IV)
parca('0024','K-DBYZB-06','orta','Bitişik/ayrı yazım kurallarını bir parçada denetler.',3,
 'Sabah okula erken geldim, çünkü (I) sınavdan önce notlarımı gözden geçirmek istiyordum. Kantinde bir an (II) durup kahvaltı ettim (III). Sınıfa çıkınca bir kaç (IV) arkadaşım çoktan gelmişti. Birazdan sınıf dopdolu (V) olacaktı.',
 [(D,'çünkü ✓','“Çünkü” bitişik yazılır; doğrudur.'),
  (D,'bir an ✓','“Bir an” ayrı yazılır; doğrudur.'),
  (D,'kahvaltı ettim ✓','“Kahvaltı etmek” ses olayı olmadığı için ayrı yazılır; doğrudur.'),
  (Y,'bir kaç ✗',''),
  (D,'dopdolu ✓','“Dopdolu” pekiştirmedir, bitişik yazılır; doğrudur.')],
 'D',Y,'Yazımı yanlış olan numaralı yer.','Bitişik yazılması gereken belgisiz sıfatı ara.',[B_KR,B_BR],
 'Birkaç bitişik; çünkü, dopdolu bitişik; bir an, kahvaltı etmek ayrı yazılır.','birkaç: bitişik',
 'IV’teki “birkaç” bitişik yazılmalıdır; öteki numaralı yerlerin yazımı doğrudur.',
 '“Birkaç” bitişik, “bir an” ayrıdır.')
bitir(Q)
