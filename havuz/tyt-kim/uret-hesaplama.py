import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
H.KONU='Kimyasal Hesaplamalar'
P=Parti('hesaplama','Kimyasal Hesaplamalar','kim|Kimyasal Hesaplamalar',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (mol kavramı, tepkimelerde hesaplamalar) · MEB 10. sınıf'
kart('K-KHE-01','Mol kavramı','n = m ÷ MA; 1 mol = 6 × 10²³ tanecik; atom sayısı = molekül sayısı × molekül başına atom.','Molekül sayısı ile atom sayısını karıştırmak; mol kütlesini yanlış toplamak.','kolay','düz',2,'kim-hs-mol','Mol, tanecik ve atom sayısı',KY)
kart('K-KHE-02','Tepkimelerde hesaplama','Katsayılar mol oranını verir; gaz hacmi NK’da n × 22,4.','Katsayıyı kullanmamak; yanlış maddenin katsayısını almak.','orta','düz',3,'kim-hs-tepkime','Tepkimede mol ve hacim',KY)
kart('K-KHE-03','Mol kavramı','Aynı kaplardaki gazların mol sayısını karşılaştırıp molekül ve atom sayılarını yorumlamak.','Hacmi ile kütleyi birbirine karıştırmak; atom ve molekül sayısını eşitlemek.','orta','öncüllü',3,'kim-hs-karsilastir','Gazlarda molekül ve atom sayısı karşılaştırma',KY)
kart('K-KHE-04','Tepkimelerde hesaplama','Sınırlayıcı bileşen önce bulunur; artan madde miktarı tepkimeye girene göre hesaplanır.','Katsayı oranını 1:1 almak; artan maddeyi yanlış seçmek.','zor','düz',4,'kim-hs-sinirlayici','Sınırlayıcı bileşen ve artan madde',KY)
NA=6
MOL=B('Mol','n = kütle ÷ mol kütlesi; 1 mol = 6 × 10²³ tanecik. Örnek: 9 g H₂O (18 g/mol) = 0,5 mol = 3 × 10²³ molekül')
# 0001
n=Fr(36,18); assert n==2
tot=n*3; mol_=n*1; Hs=n*2; assert tot==6 and tot*NA==36 and mol_*NA==12 and Hs*NA==24 and (Fr(36,36)*3*NA)==18 and n*6*NA==72
ss=['1,2 × 10²⁴','1,8 × 10²⁴','2,4 × 10²⁴','3,6 × 10²⁴','7,2 × 10²⁴']
mk(P,'0001',tipId='kim-hs-mol',tip='Mol, tanecik ve atom sayısı',z='kolay',alt='Mol Kavramı',kaz='Kütleden mol sayısını, oradan toplam atom sayısını hesaplar.',kalip='düz',adim=2,
 kart='K-KHE-01 (mol kavramı) · su örneği, toplam atom sayısı',
 metin='H: 1 g/mol, O: 16 g/mol, Avogadro sayısı = 6 × 10²³ olduğuna göre 36 g H₂O sıvısındaki toplam atom sayısı kaçtır?',
 dogru=ss[3],sira=ss,
 yan=[(ss[0],'Yalnız molekül sayısını (2 mol) bulmuş; atom sayısına geçmemiş.','dikkat'),(ss[1],'H₂O’nun mol kütlesini 36 g/mol almış; mol sayısını 1 bulmuş.','islem'),(ss[2],'Yalnız H atomlarının sayısını (4 mol) bulmuş.','dikkat'),(ss[4],'Molekül başına atom sayısını 6 almış.','bilgi')],
 istenen='36 g H₂O’daki toplam atom sayısı.',
 ip=['Önce mol sayısını bul; sonra bir H₂O molekülünde kaç atom olduğuna bak.'],
 bilgi=[MOL],
 ad=[A('Mol kütlesi','H₂O molekülünde 2 H ve 1 O vardır.','M = 2 × 1 + 16 = 18 g/mol'),A('Mol sayısı','Kütle mol kütlesine bölünür.','n = 36 ÷ 18 = 2 mol'),A('Toplam atom','Bir H₂O molekülünde 2 H + 1 O = 3 atom vardır.','2 × 3 = 6 mol atom · 6 × 6 × 10²³ = 3,6 × 10²⁴')],
 puf='Atom sayısı = mol × molekül başına atom × Avogadro sayısı.')
# 0002
M=44; nC=Fr(88,10)/M; nO=5*nC; V=nO*Fr(224,10); assert nC==Fr(1,5) and nO==1 and V==Fr(224,10)
assert nC*Fr(224,10)==Fr(448,100) and 3*nC*Fr(224,10)==Fr(1344,100) and 4*nC*Fr(224,10)==Fr(1792,100) and 5*Fr(224,10)==112
mk(P,'0002',tipId='kim-hs-tepkime',tip='Tepkimede mol ve hacim',z='orta',alt='Kimyasal Tepkimelerde Hesaplamalar',kaz='Denkleştirilmiş tepkimenin katsayılarını kullanarak harcanan gazın NK’daki hacmini bulur.',kalip='düz',adim=3,
 kart='K-KHE-02 (tepkimede hesaplama) · propan yanması, O₂ hacmi',
 metin='C₃H₈ gazının yanma tepkimesi aşağıdaki gibidir.\nC₃H₈ + 5O₂ → 3CO₂ + 4H₂O\nC: 12 g/mol, H: 1 g/mol ve NK’da 1 mol gaz 22,4 L olduğuna göre 8,8 g C₃H₈ gazı yeterli miktarda O₂ ile tamamen yandığında harcanan O₂ gazı normal koşullarda (NK) kaç L hacim kaplar?',
 dogru=Fr(224,10),yan=[(Fr(448,100),'O₂ için katsayıyı kullanmamış; 0,2 mol O₂ almış.','bilgi'),(Fr(1344,100),'CO₂’nin katsayısını (3) kullanıp 0,6 mol almış.','dikkat'),(Fr(1792,100),'H₂O’nun katsayısını (4) kullanıp 0,8 mol almış.','dikkat'),(112,'Mol sayısını bulmadan doğrudan 5 mol O₂ almış.','islem')],
 istenen='Harcanan O₂’nin NK’daki hacmi (L).',
 ip=['C₃H₈’in mol sayısını bul; denklemdeki katsayı oranıyla O₂’nin mol sayısına geç.'],
 bilgi=[MOL,B('Gaz hacmi','Normal koşullarda (NK) 1 mol gaz 22,4 L hacim kaplar. Örnek: 0,5 mol gaz 11,2 L kaplar')],
 ad=[A('C₃H₈ mol sayısı','C₃H₈’in mol kütlesi 3 × 12 + 8 × 1 = 44 g/mol’dür.','n = 8,8 ÷ 44 = 0,2 mol'),A('O₂ mol sayısı','Katsayılar mol oranını verir: 1 mol C₃H₈ için 5 mol O₂.','n(O₂) = 5 × 0,2 = 1 mol'),A('Hacim','NK’da mol sayısı 22,4 ile çarpılır.','V = 1 × 22,4 = 22,4 L')],
 puf='Katsayı oranı mol oranıdır; önce mol, sonra gram ya da hacim hesaplanır.')
# 0003
n1=Fr(112,10)/Fr(224,10); n2=Fr(11,44); assert n1==Fr(1,2) and n2==Fr(1,4)
I=(n1==2*n2); II=(n2*3>n1*5); III=(n1*4==4*(n2*2)); assert (I,II,III)==(True,False,True)
s3=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III']
mk(P,'0003',tipId='kim-hs-karsilastir',tip='Gazlarda molekül ve atom sayısı karşılaştırma',z='orta',alt='Mol Kavramı',kaz='Farklı gazların mol sayılarını bularak molekül ve atom sayılarını karşılaştırır.',kalip='öncüllü',adim=3,
 kart='K-KHE-03 (mol karşılaştırma) · CH₄ hacmi ile CO₂ kütlesi',
 metin='Kap 1: NK’da 11,2 L CH₄ gazı\nKap 2: 11 g CO₂ gazı\nI. Kap 1’deki molekül sayısı, Kap 2’dekinin 2 katıdır.\nII. Kap 2’deki toplam atom sayısı, Kap 1’dekinden fazladır.\nIII. Kap 1’deki H atomu sayısı, Kap 2’deki O atomu sayısının 4 katıdır.\nC: 12 g/mol, O: 16 g/mol ve NK’da 1 mol gaz 22,4 L olduğuna göre yukarıdaki ifadelerden hangileri doğrudur?',
 dogru='I ve III',sira=s3,
 yan=[(s3[0],'III’ü yanlış sanmış; H atomu sayısını (2 mol) O atomu sayısıyla (0,5 mol) karşılaştırmamış.','islem'),(s3[1],'II’yi doğru sanıp I ile III’ü yanlış bulmuş; atom sayılarını mol sayısıyla molekül başına atomu çarparak bulmamış.','islem'),(s3[2],'I’i yanlış sanmış; mol sayılarının 0,5 ve 0,25 olduğunu bulmamış.','islem'),(s3[3],'II’yi doğru sanmış; CO₂’nin toplam atom sayısını (0,75 mol) Kap 1’le (2,5 mol) karşılaştırmamış.','dikkat')],
 istenen='Doğru ifadelerin belirlenmesi.',
 ip=['İki kaptaki gazın da mol sayısını ayrı ayrı bul; sonra her molekülde kaç atom olduğuna bak.'],
 bilgi=[MOL,B('Molekülde atom','CH₄ molekülünde 1 C ve 4 H (toplam 5 atom), CO₂ molekülünde 1 C ve 2 O (toplam 3 atom) vardır')],
 ad=[A('Mol sayıları','CH₄: hacimden, CO₂: kütleden mol hesaplanır (CO₂ = 44 g/mol).','CH₄: 11,2 ÷ 22,4 = 0,5 mol · CO₂: 11 ÷ 44 = 0,25 mol'),A('I ve II','Molekül sayısı mol ile doğru orantılıdır; atom sayısı molekül başına atomla çarpılır.','I: 0,5 = 2 × 0,25 → doğru · atom: 0,5 × 5 = 2,5 mol ve 0,25 × 3 = 0,75 mol → II yanlış'),A('III','Kap 1’de H atomu 4 × 0,5 = 2 mol, Kap 2’de O atomu 2 × 0,25 = 0,5 mol.','2 ÷ 0,5 = 4 → doğru'),A('Sonuç','Doğru olanlar I ve III.','I ve III')],
 puf='Önce her kabın mol sayısını bul; molekül sayısı mol ile, atom sayısı mol ve formül indisleriyle bulunur.')
# 0004
nMg=Fr(72,10)/24; nHCl=Fr(4,10); used=nHCl/2; left=nMg-used
assert nMg==Fr(3,10) and used==Fr(1,5) and left==Fr(1,10) and nHCl/2<nMg
assert left*24==Fr(24,10) and used*24==Fr(48,10) and Fr(1,10)*Fr(365,10)==Fr(365,100) and nMg*24==Fr(72,10) and nHCl*Fr(365,10)==Fr(146,10)
assert nMg<nHCl # 1:1 hatası: Mg sınırlayıcı sanılır, 0,1 mol HCl artar
mk(P,'0004',tipId='kim-hs-sinirlayici',tip='Sınırlayıcı bileşen ve artan madde',z='zor',alt='Kimyasal Tepkimelerde Hesaplamalar',kaz='Sınırlayıcı bileşeni belirleyip tepkime sonunda artan maddenin kütlesini bulur.',kalip='düz',adim=4,
 kart='K-KHE-04 (sınırlayıcı bileşen) · Mg ile HCl, artan madde kütlesi',
 metin='Mg + 2HCl → MgCl₂ + H₂\n7,2 g Mg katısı, 0,4 mol HCl içeren sulu çözeltiye atılıyor ve tepkime tamamlanıyor.\nH: 1 g/mol, Mg: 24 g/mol, Cl: 35,5 g/mol olduğuna göre tepkime sonunda artan maddenin kütlesi kaç gramdır?',
 dogru=Fr(24,10),yan=[(Fr(365,100),'Mg ile HCl’yi 1 : 1 oranında tepkimeye sokmuş; HCl’nin 0,1 mol arttığını sanmış.','bilgi'),(Fr(48,10),'Artan değil, tepkimeye giren Mg’nin kütlesini (0,2 mol) bulmuş.','dikkat'),(Fr(72,10),'Tepkimeyi dikkate almadan atılan Mg’nin tamamını artan kabul etmiş.','dikkat'),(Fr(146,10),'0,4 mol HCl’nin başlangıç kütlesini artan madde olarak yazmış.','dikkat')],
 istenen='Tepkime sonunda artan maddenin kütlesi (g).',
 ip=['Her iki maddenin mol sayısını bul; 2 : 1 mol oranıyla hangisinin yetmediğine bak.'],
 bilgi=[MOL,B('Sınırlayıcı bileşen','tepkimede önce biten maddedir; ürün miktarını o belirler. Örnek: 1 mol A ile 3 mol B, A + B → ürün tepkimesinde B 2 mol artar')],
 ad=[A('Mol sayıları','Mg’nin mol kütlesi 24 g/mol’dür.','n(Mg) = 7,2 ÷ 24 = 0,3 mol · n(HCl) = 0,4 mol'),A('Sınırlayıcı madde','1 mol Mg için 2 mol HCl gerekir; 0,3 mol Mg için 0,6 mol HCl gerekirdi ama 0,4 mol var.','HCl sınırlayıcı · Mg artan'),A('Tüketilen Mg','0,4 mol HCl, yarısı kadar Mg ile tepkimeye girer.','0,4 ÷ 2 = 0,2 mol Mg'),A('Artan Mg','Başlangıçtaki mol sayısından tüketilen çıkarılır ve kütleye çevrilir.','0,3 − 0,2 = 0,1 mol · 0,1 × 24 = 2,4 g')],
 puf='Sınırlayıcıyı bulmak için her maddenin mol sayısını katsayısına böl; en küçük değeri veren madde önce biter.')
bitir(P,'hesaplama','kim|Kimyasal Hesaplamalar')
