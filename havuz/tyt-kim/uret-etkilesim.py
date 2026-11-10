import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim as H
from _hafif_kim import *
H.KONU='Kimyasal Türler Arası Etkileşimler'
P=Parti('etkilesim','Kimyasal Türler Arası Etkileşimler','kim|Kimyasal Türler Arası Etkileşimler',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (güçlü ve zayıf etkileşimler) · MEB 9. sınıf'
kart('K-ETKL-01','Bağ türü belirleme','Metal–ametal arasında iyonik, ametal–ametal arasında kovalent bağ oluşur.','Her bileşikte iyonik bağ aramak; kovalent bileşiği iyonik sanmak.','kolay','düz',2,'kim-et-bagturu','Bileşikte bağ türü',KY)
kart('K-ETKL-02','İyonik bileşik formülü','Metal elektron verir, ametal alır; verilen ve alınan elektron sayısı eşitlenerek formül yazılır.','Atom sayılarını 1:1 almak; çaprazlamayı ters yapmak.','orta','düz',3,'kim-et-formul','Atom numarasından bileşik formülü',KY)
kart('K-ETKL-03','Çoklu bağlar','Her atom oktetini (H için dueti) tamamlayacak kadar bağ yapar; O₂ çift, N₂ üçlü bağ içerir.','CO₂’deki çift bağları ya da C₂H₄’teki çift bağı atlamak.','orta','düz',3,'kim-et-coklu','Çoklu bağ içeren moleküller',KY)
kart('K-ETKL-04','Moleküller arası etkileşim türü','Hidrojen bağı için H, F–O–N atomlarından birine bağlı olmalıdır; apolarda London, polarda dipol–dipol baskındır.','HBr ya da HCl’de hidrojen bağı aramak.','orta','öncüllü',3,'kim-et-zayif','Baskın zayıf etkileşim',KY)
kart('K-ETKL-05','Halojenlerin hâl ve kaynama noktası','Apolar moleküllerde mol kütlesi arttıkça London kuvveti ve kaynama noktası artar; hâl, oda sıcaklığının erime–kaynama noktaları arasındaki yerinden bulunur.','Hâli yalnız kaynama noktasına bakıp belirlemek.','zor','tablo',4,'kim-et-halojen','Tablodan hâl ve kaynama noktası yorumu',KY)
kart('K-ETKL-06','Benzer benzeri çözer','Polar maddeler polar çözücüde, apolar maddeler apolar çözücüde çözünür; iyonik maddeler polar çözücüde çözünür.','Yağın suda, NaCl’nin CCl₄’te çözüneceğini sanmak.','zor','öncüllü',4,'kim-et-cozunme','Çözünme ve etkileşim',KY)
# ---- 0001
S=[('CO₂',False,'karbon ve oksijen ametaldir, aralarında kovalent bağ vardır'),
   ('NaCl',True,''),
   ('H₂O',False,'hidrojen ve oksijen ametaldir, aralarında kovalent bağ vardır'),
   ('CH₄',False,'karbon ve hidrojen ametaldir, aralarında kovalent bağ vardır'),
   ('NH₃',False,'azot ve hidrojen ametaldir, aralarında kovalent bağ vardır')]
r=tek(S,True)
mk(P,'0001',tipId='kim-et-bagturu',tip='Bileşikte bağ türü',z='kolay',alt='Güçlü Etkileşimler',kaz='Bileşiği oluşturan elementlerin türüne göre bağ türünü belirler.',kalip='düz',adim=2,
 kart='K-ETKL-01 (bağ türü) · NaCl, CO₂, H₂O, CH₄, NH₃',
 metin='Aşağıdaki bileşiklerden hangisinde atomlar arasında yalnız iyonik bağ bulunur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yalnız iyonik bağ içeren bileşik.',
 ip=['Bileşiği oluşturan elementlerin metal mi ametal mi olduğuna bak.'],
 bilgi=[B('İyonik ve kovalent bağ','Metal ile ametal arasında elektron aktarımıyla iyonik bağ oluşur (örnek: NaCl). Ametaller arasında elektronlar ortak kullanılır ve kovalent bağ oluşur (örnek: H₂O)')],
 ad=[A('Elementleri sınıflandır','Na metaldir; C, O, H, N, Cl ametaldir.','Na: metal · C, H, N, O, Cl: ametal'),A('Bağ türünü belirle','Metal–ametal iyonik, ametal–ametal kovalenttir.','NaCl: iyonik · CO₂, H₂O, CH₄, NH₃: kovalent'),A('Sonuç','Yalnız iyonik bağ içeren tek bileşik bulunur.','NaCl → B')],
 puf='Bileşikte metal varsa genellikle iyonik, yalnız ametal varsa kovalent bağ düşün.')
# ---- 0002
Zx,Zy=12,17; (px,vx),(py,vy)=yer(Zx),yer(Zy)
verir=vx; alir=8-vy; assert (verir,alir)==(2,1) and vx<=3 and vy>=5
S=[('XY₂, kovalent',False,'metal ile ametal arasında elektron aktarılır, bağ iyoniktir'),
   ('X₂Y, kovalent',False,'bağ iyoniktir ve indisler de ters yazılmıştır'),
   ('XY, iyonik',False,'X 2 elektron verir, Y 1 elektron alır; 1:1 birleşirse yük dengelenmez'),
   ('X₂Y, iyonik',False,'çaprazlama ters yapılmış; X için indis 1, Y için indis 2 olmalıdır'),
   ('XY₂, iyonik',True,'')]
r=tek(S,True)
mk(P,'0002',tipId='kim-et-formul',tip='Atom numarasından bileşik formülü',z='orta',alt='Güçlü Etkileşimler',kaz='Atom numaralarından elektron dizilimini bulup oluşan bileşiğin formülünü ve bağ türünü belirler.',kalip='düz',adim=3,
 kart='K-ETKL-02 (iyonik bileşik formülü) · atom numaraları 12 ve 17',
 metin='X ve Y elementlerinin atom numaraları sırasıyla 12 ve 17’dir.\nBuna göre X ile Y’nin oluşturduğu kararlı bileşiğin formülü ve bağ türü aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Bileşiğin formülü ve bağ türü.',
 ip=['Elektron dizilimlerinden son katmandaki elektron sayılarını bul; kim kaç elektron verir, kim kaç elektron alır?'],
 bilgi=[B('Elektron dizilimi','Elektronlar katmanlara 2, 8, 8 … sırasıyla yerleşir. Son katmandaki elektronlar değerlik elektronudur. Örnek: atom numarası 11 → 2, 8, 1'),B('Kararlı olma','Metal son katmandaki elektronları verir, ametal oktetini tamamlayacak kadar alır; verilen ve alınan elektron sayıları eşitlenir')],
 ad=[A('Elektron dizilimleri','Atom numaralarına göre katmanlar doldurulur.','X: 2, 8, 2 · Y: 2, 8, 7'),A('Verilen ve alınan elektron','X 2 elektron verir (metal), Y oktet için 1 elektron alır (ametal).','X: −2 e⁻ → X²⁺ · Y: +1 e⁻ → Y⁻'),A('Formül','1 X, 2 Y atomu 2 elektronu dengeler; bağ iyoniktir.','XY₂, iyonik')],
 puf='Verilen elektron sayısı alınan elektron sayısına eşitlenerek formül bulunur.')
# ---- 0003
Mol={'O₂':(['O','O'],[(0,1,2)]),'N₂':(['N','N'],[(0,1,3)]),'CO₂':(['O','C','O'],[(0,1,2),(1,2,2)]),'C₂H₄':(['C','C','H','H','H','H'],[(0,1,2),(0,2,1),(0,3,1),(1,4,1),(1,5,1)]),
     'H₂O':(['O','H','H'],[(0,1,1),(0,2,1)]),'NH₃':(['N','H','H','H'],[(0,1,1),(0,2,1),(0,3,1)])}
VAL={'H':1,'C':4,'N':5,'O':6}
for ad_,(at,bg) in Mol.items():
    top=[0]*len(at)
    for a,b,o in bg: top[a]+=o; top[b]+=o
    for i,s in enumerate(at): assert top[i]==(1 if s=='H' else 8-VAL[s]),(ad_,i)
cok=[a for a,(at,bg) in Mol.items() if any(o>1 for _,_,o in bg)]
assert len(cok)==4
mk(P,'0003',tipId='kim-et-coklu',tip='Çoklu bağ içeren moleküller',z='orta',alt='Güçlü Etkileşimler',kaz='Moleküllerin Lewis yapılarını çizerek çift ve üçlü bağ içerenleri belirler.',kalip='düz',adim=3,
 kart='K-ETKL-03 (çoklu bağlar) · O₂, N₂, CO₂, C₂H₄, H₂O, NH₃',
 metin='O₂, N₂, CO₂, C₂H₄, H₂O ve NH₃ moleküllerinin tamamında atomlar oktet (H için dubletle) kuralına uyacak biçimde bağlanmıştır.\nBuna göre bu moleküllerden kaç tanesi çift ya da üçlü bağ içerir?',
 dogru=4,yan=[(2,'Yalnız O₂ ve N₂’yi saymış; CO₂ ve C₂H₄’teki çift bağları atlamış.','bilgi'),(3,'C₂H₄’teki karbon–karbon çift bağını fark etmemiş.','dikkat'),(5,'H₂O ya da NH₃’ü de çoklu bağlı saymış; hidrojen yalnız tek bağ yapar.','bilgi'),(6,'Tüm molekülleri çoklu bağlı saymış.','bilgi')],
 istenen='Çift ya da üçlü bağ içeren molekül sayısı.',
 ip=['Her atomun oktetini tamamlamak için kaç bağ yapması gerektiğini düşün: O 2, N 3, C 4, H 1 bağ yapar.'],
 bilgi=[B('Bağ sayısı','Oktetini tamamlamak için ametal atomu 8 − (değerlik elektron sayısı) kadar bağ yapar: H 1, O 2, N 3, C 4 bağ. Örnek: H₂O’da O iki tek bağ yapar'),B('Çoklu bağ','İki atom arasında iki ortak elektron çifti çift bağ, üç çift üçlü bağdır. Örnek: O=O çift bağ, N≡N üçlü bağdır')],
 ad=[A('Bağ sayıları','Her atomun yapması gereken bağ sayısı bulunur.','H: 1 · O: 2 · N: 3 · C: 4'),A('Moleküller','O₂ ve CO₂’de O’lar, N₂’de N’ler, C₂H₄’te C’ler tek bağla doyamaz.','O=O; N≡N; O=C=O; H₂C=CH₂'),A('Tek bağlılar','H₂O ve NH₃’te O ve N, H’lerle tek bağ yaparak doyar.','H–O–H · NH₃: üç tek bağ'),A('Sayım','Çoklu bağlı olanlar sayılır.','O₂, N₂, CO₂, C₂H₄ → 4')],
 puf='Önce her atomun yapması gereken bağ sayısını yaz; tek bağla doymayan atom çiftleri çoklu bağ kurar.')
# ---- 0004
d={'I':(True,'N–H bağı içeren NH₃ moleküllerinde hidrojen bağı bulunur'),
   'II':(True,'CH₄ apolar bir molekül olduğu için baskın etkileşim London kuvvetleridir'),
   'III':(False,'HBr’de H, F–O–N atomlarından birine bağlı değildir; baskın etkileşim dipol–dipoldür')}
r=onc(d,[('I','II'),('I',),('II',),('III',),('I','III')])
mk(P,'0004',tipId='kim-et-zayif',tip='Baskın zayıf etkileşim',z='orta',alt='Zayıf Etkileşimler',kaz='Moleküller arasındaki baskın zayıf etkileşim türünü belirler.',kalip='öncüllü',adim=3,
 kart='K-ETKL-04 (zayıf etkileşimler) · NH₃, CH₄, HBr',
 metin='Sıvı hâlde bulunan aşağıdaki maddelerin molekülleri arasındaki baskın etkileşim türleri için şunlar söyleniyor.\nI. NH₃ – hidrojen bağı\nII. CH₄ – London kuvvetleri\nIII. HBr – hidrojen bağı\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru eşleştirilen etkileşim türleri.',
 ip=['Önce molekülün polar mı apolar mı olduğuna, sonra H’nin F, O ya da N’ye bağlı olup olmadığına bak.'],
 bilgi=[B('Zayıf etkileşimler','Apolar moleküller arasında London kuvvetleri vardır. Polar moleküller arasında dipol–dipol etkileşimi bulunur. H atomu F, O ya da N’ye bağlıysa moleküller arasında hidrojen bağı oluşur. Örnek: H₂O')],
 ad=[A('NH₃','Azota bağlı hidrojen vardır.','hidrojen bağı → I: doğru'),A('CH₄','Molekül apolardır.','London kuvvetleri → II: doğru'),A('HBr','H, brom atomuna bağlıdır; polar molekül.','dipol–dipol → III: yanlış'),A('Sonuç','Doğru olanlar toplanır.',etk(d)+' · Sonuç: I ve II')],
 puf='Hidrojen bağı yalnız H’nin F, O ya da N atomuna bağlı olduğu moleküllerde görülür.')
# ---- 0005
T={'F₂':(38,-220,-188),'Cl₂':(71,-101,-34),'Br₂':(160,-7,59),'I₂':(254,114,184)}
hal=lambda e,k:'katı' if 25<e else ('sıvı' if 25<k else 'gaz')
hl={a:hal(v[1],v[2]) for a,v in T.items()}
assert hl=={'F₂':'gaz','Cl₂':'gaz','Br₂':'sıvı','I₂':'katı'}
assert all(T[a][0]<T[b][0] and T[a][2]<T[b][2] for a,b in zip(list(T),list(T)[1:]))
d={'I':(True,'tablodaki dört maddede kaynama noktası mol kütlesiyle aynı sırada artar'),
   'II':(False,'25 °C kaynama noktalarının üstündedir; F₂ ve Cl₂ bu sıcaklıkta gaz hâldedir'),
   'III':(True,'25 °C’de Br₂ erime ve kaynama noktası arasında olduğu için sıvı, I₂ erime noktasının altında olduğu için katıdır')}
r=onc(d,[('I',),('II',),('III',),('I','III'),('II','III')])
mk(P,'0005',tipId='kim-et-halojen',tip='Tablodan hâl ve kaynama noktası yorumu',z='zor',alt='Zayıf Etkileşimler',kaz='Apolar moleküllerin mol kütlesi, erime ve kaynama noktası verilerinden hâl ve etkileşim yorumu yapar.',kalip='tablo',adim=4,
 kart='K-ETKL-05 (halojenler) · mol kütlesi, erime ve kaynama noktası tablosu',
 metin='Apolar moleküllerden oluşan F₂, Cl₂, Br₂ ve I₂ maddelerine ait bilgiler tabloda verilmiştir.\nMadde | Mol kütlesi (g/mol) | Erime noktası (°C) | Kaynama noktası (°C)\nF₂ | 38 | −220 | −188\nCl₂ | 71 | −101 | −34\nBr₂ | 160 | −7 | 59\nI₂ | 254 | 114 | 184\nBu maddelerle ilgili şunlar söyleniyor.\nI. Mol kütlesi arttıkça kaynama noktası artmaktadır.\nII. 25 °C’de F₂ ve Cl₂ sıvı hâldedir.\nIII. 25 °C’de Br₂ sıvı, I₂ katı hâldedir.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Tabloya göre doğru olan öncüller.',
 ip=['Bir maddenin hâli için 25 °C’nin erime ve kaynama noktalarına göre yerini bul: erime noktasının altında katı, kaynama noktasının üstünde gazdır.'],
 bilgi=[B('Apolar maddeler','Apolar moleküller arasında London kuvvetleri etkindir. Mol kütlesi büyüdükçe London kuvvetleri güçlenir ve kaynama noktası yükselir'),B('Hâl belirleme','Sıcaklık erime noktasının altındaysa madde katı, erime ile kaynama noktası arasındaysa sıvı, kaynama noktasının üstündeyse gazdır. Örnek: su 25 °C’de sıvıdır (0 < 25 < 100)')],
 ad=[A('I. öncül','Kaynama noktaları −188, −34, 59, 184 ve mol kütleleri 38, 71, 160, 254 aynı sırada artıyor.','I: doğru'),A('II. öncül','25 °C, F₂ ve Cl₂’nin kaynama noktasından yüksektir.','25 > −188 ve 25 > −34 → gaz → II: yanlış'),A('III. öncül','Br₂ için −7 < 25 < 59; I₂ için 25 < 114.','Br₂: sıvı · I₂: katı → III: doğru'),A('Sonuç','Doğru olanlar toplanır.','Sonuç: I ve III')],
 puf='Hâl sorularında sıcaklığı erime ve kaynama noktalarıyla karşılaştır: altı katı, arası sıvı, üstü gaz.')
# ---- 0006
d={'I':(False,'apolar yağ polar suda çözünmez; benzer benzeri çözer'),
   'II':(True,'apolar I₂ ile apolar CCl₄ arasındaki London kuvvetleri çözünmeyi sağlar'),
   'III':(False,'iyonik NaCl polar suda çözünür, apolar CCl₄’te çözünmez'),
   'IV':(True,'C₂H₅OH ile H₂O molekülleri arasında hidrojen bağı kurulur ve ikisi her oranda karışır')}
r=onc(d,[('I','II'),('II','IV'),('III','IV'),('I','III'),('II','III')])
mk(P,'0006',tipId='kim-et-cozunme',tip='Çözünme ve etkileşim',z='zor',alt='Zayıf Etkileşimler',kaz='Maddelerin polarlığına göre çözünme durumlarını yorumlar.',kalip='öncüllü',adim=4,
 kart='K-ETKL-06 (benzer benzeri çözer) · yağ–su, I₂–CCl₄, NaCl–CCl₄, etanol–su',
 metin='Aşağıdaki çözünme olayları için şunlar söyleniyor.\nI. Apolar olan yağ, polar olan suda çözünür.\nII. Apolar olan I₂ katısı, apolar olan CCl₄ sıvısında çözünür.\nIII. İyonik olan NaCl katısı, apolar olan CCl₄ sıvısında çözünür.\nIV. Polar olan C₂H₅OH (etanol) sıvısı, suda hidrojen bağları kurarak her oranda çözünür.\nBuna göre hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan öncüller.',
 ip=['Çözünmede “benzer benzeri çözer” ilkesini uygula: çözünen ve çözücünün polar, apolar ya da iyonik olduğuna bak.'],
 bilgi=[B('Benzer benzeri çözer','Polar maddeler ve iyonik bileşikler polar çözücülerde (örnek: su), apolar maddeler apolar çözücülerde (örnek: CCl₄) çözünür')],
 ad=[A('Maddeleri sınıflandır','Su ve etanol polar, yağ, I₂ ve CCl₄ apolar, NaCl iyoniktir.','polar: H₂O, C₂H₅OH · apolar: yağ, I₂, CCl₄ · iyonik: NaCl'),A('I ve III','Yağ–su ve NaCl–CCl₄ benzer değildir.','I: yanlış · III: yanlış'),A('II ve IV','I₂–CCl₄ apolar–apolar; etanol–su polar–polar ve hidrojen bağlıdır.','II: doğru · IV: doğru'),A('Sonuç','Doğru olanlar toplanır.','Sonuç: II ve IV')],
 puf='Çözünme sorusunda önce her maddeyi polar, apolar ya da iyonik olarak etiketle; benzerler birbirini çözer.')
bitir(P,'etkilesim','kim|Kimyasal Türler Arası Etkileşimler')
