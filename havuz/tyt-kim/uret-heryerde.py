import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
H.KONU='Kimya Her Yerde'
P=Parti('heryerde','Kimya Her Yerde','kim|Kimya Her Yerde',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (günlük hayat kimyasalları) · MEB 10. sınıf'
kart('K-KHY-01','Temizlik maddeleri','Çamaşır suyunun etkin maddesi sodyum hipoklorittir (NaOCl); ağartıcı ve mikrop öldürücüdür.','Çamaşır suyunu NaCl ya da NaOH ile karıştırmak.','kolay','düz',2,'kim-hy-camasir','Çamaşır suyu',KY)
kart('K-KHY-02','Sabun ve deterjan','Sabun yağın bazla tepkimesinden elde edilir; sert suda çözünmeyen tuz verip etkisini yitirir; deterjan sert suda da etkilidir.','Sabun ile deterjanın sert sudaki davranışını karıştırmak.','orta','öncüllü',3,'kim-hy-sabun','Sabun ve deterjan',KY)
kart('K-KHY-03','Günlük hayat kimyasalları','Yaygın kimyasalların bileşimi ile kullanım amacını eşleştirmek.','Kuvvetli ve aşındırıcı maddeyi ilaç sanmak.','orta','düz',3,'kim-hy-eslestirme','Kimyasal ve kullanım eşleştirme',KY)
kart('K-KHY-04','Günlük hayat kimyasalları','Çamaşır suyu bazik; tuz ruhu ile karıştırılmaz; sabunun polar ve apolar kısmı; antiasit bazik; katkı maddeleri yapay da olabilir.','Çamaşır suyunu asidik sanmak; katkı maddelerinin yalnız doğal olduğunu düşünmek.','orta','öncüllü',4,'kim-hy-guvenli','Evde kullanılan kimyasalların özellikleri',KY)
# 0001
s1=['HCl','Na₂CO₃','NaCl','NaOH','NaOCl']
mk(P,'0001',tipId='kim-hy-camasir',tip='Çamaşır suyu',z='kolay',alt='Temizlik Maddeleri',kaz='Çamaşır suyunun etkin maddesini bilir.',kalip='düz',adim=2,
 kart='K-KHY-01 (çamaşır suyu) · etkin madde formülü',
 metin='Evlerde ağartıcı ve mikrop öldürücü olarak kullanılan çamaşır suyunun etkin maddesi aşağıdakilerden hangisidir?',
 dogru=s1[4],sira=s1,
 yan=[(s1[0],'HCl’yi tuz ruhuyla karıştırıp çamaşır suyu sanmış; HCl asit olup farklı bir temizlik maddesidir.','bilgi'),(s1[1],'Na₂CO₃’ı (soda) çamaşır suyuna bağlamış; soda başka bir temizlik maddesidir.','bilgi'),(s1[2],'NaCl’yi (sofra tuzu) etkin madde sanmış; tuz ağartıcı değildir.','bilgi'),(s1[3],'NaOH’ı (kostik) çamaşır suyuyla karıştırmış; NaOH kuvvetli bir bazdır ama çamaşır suyunun etkin maddesi değildir.','bilgi')],
 istenen='Çamaşır suyunun etkin maddesi.',
 ip=['Çamaşır suyunun adı sodyum hipoklorit çözeltisidir; formülünde Na, O ve Cl bulunur.'],
 bilgi=[B('Çamaşır suyu','sodyum hipoklorit (NaOCl) çözeltisidir; ağartıcı ve mikrop öldürücüdür. Örnek: bazı yüzey temizleyicilerinde NaOCl bulunur')],
 ad=[A('Maddeyi hatırla','Çamaşır suyu, sodyum hipoklorit çözeltisidir.','çamaşır suyu = sodyum hipoklorit'),A('Elementleri eşle','Sodyum Na, klor Cl, hipoklorit ise ClO⁻ iyonudur.','Na + ClO → NaOCl'),A('Formülü seç','Seçeneklerde yalnız bu formül Na, O ve Cl birlikte içerir.','NaOCl')],
 puf='Çamaşır suyunun adı sodyum hipoklorittir; formülünde Na, O ve Cl bulunur.')
# 0002
s2=['I ve II','Yalnız I','Yalnız II','II ve III','I, II ve III']
mk(P,'0002',tipId='kim-hy-sabun',tip='Sabun ve deterjan',z='orta',alt='Sabun ve Deterjanlar',kaz='Sabun ve deterjanın elde edilişini ve sert sudaki davranışını karşılaştırır.',kalip='öncüllü',adim=3,
 kart='K-KHY-02 (sabun ve deterjan) · üç öncül, deterjan sert suda sabun gibi sanılır',
 metin='I. Sabun, yağların NaOH gibi bir bazla tepkimeye girmesiyle elde edilir.\nII. Sert suda sabunun temizleme etkisi azalır.\nIII. Deterjanlar sert suda, sabun gibi çözünmeyen tuz oluşturarak etkisini yitirir.\nSabun ve deterjanlarla ilgili yukarıdaki ifadelerden hangileri doğrudur?',
 dogru='I ve II',sira=s2,
 yan=[(s2[1],'II’yi yanlış sanmış; sabunun sert suda Ca²⁺ ve Mg²⁺ ile çözünmeyen tuz verdiğini bilmemiş.','bilgi'),(s2[2],'I’i yanlış sanmış; sabunun bazla yağın tepkimesinden elde edildiğini bilmemiş.','bilgi'),(s2[3],'I’i yanlış sanıp III’ü doğru bulmuş; deterjanın sert suda da etkili olduğunu bilmemiş.','bilgi'),(s2[4],'III’ü doğru saymış; sabun ile deterjanın sert sudaki farkını karıştırmış.','bilgi')],
 istenen='Doğru ifadelerin belirlenmesi.',
 ip=['Sert suda çözünmüş Ca²⁺ ve Mg²⁺ iyonları bulunur; sabun bu iyonlarla çözünmeyen tuz oluşturur, deterjan ise oluşturmaz.'],
 bilgi=[B('Sabun ve deterjan','sabun, yağların NaOH ya da KOH gibi bir bazla tepkimesinden elde edilir; sert suda köpürmez ve temizleme gücü azalır. Deterjan sert suda da etkilidir')],
 ad=[A('I’i incele','Sabun, yağın kuvvetli bazla tepkimesinden (sabunlaşma) elde edilir.','I: doğru'),A('II’yi incele','Sert suda Ca²⁺ ve Mg²⁺ sabunla çözünmeyen tuz oluşturur.','II: doğru'),A('III’ü incele','Deterjan sert suda çözünmeyen tuz oluşturmaz, temizlik etkisini sürdürür.','III: yanlış'),A('Sonuç','Doğru ifadeler I ve II’dir.','I ve II')],
 puf='Sert suda sabun etkisini yitirir; deterjan sert suda da temizler.')
# 0003
s3=['Sodyum hipoklorit (NaOCl): Ağartıcı ve mikrop öldürücü olarak kullanılır.','Hidroklorik asit çözeltisi (tuz ruhu): Yüzeylerdeki kireç lekelerini gidermede kullanılır.','Asetik asit çözeltisi (sirke): Turşu gibi gıdalarda koruyucu ve tat verici olarak kullanılır.','Sodyum hidrojenkarbonat (NaHCO₃): Mide asidini gidermek ve kabartma tozu olarak kullanılır.','Sodyum hidroksit (NaOH): Mide yanmasını gidermek için ilaç olarak içilir.']
s3=[s3[4],s3[0],s3[1],s3[2],s3[3]]
mk(P,'0003',tipId='kim-hy-eslestirme',tip='Kimyasal ve kullanım eşleştirme',z='orta',alt='Yaygın Günlük Hayat Kimyasalları',kaz='Yaygın günlük hayat kimyasallarını kullanım amaçlarıyla eşleştirir.',kalip='düz',adim=3,
 kart='K-KHY-03 (günlük kimyasallar) · kimyasal–kullanım eşleştirme, aşındırıcı baz ilaç sanılır',
 metin='Aşağıdaki günlük hayat kimyasalı ve kullanım amacı eşleştirmelerinden hangisi yanlıştır?',
 dogru=s3[0],sira=s3,
 yan=[(s3[1],'Doğru eşleştirmeyi yanlış sanmış; NaOCl çamaşır suyunun etkin maddesidir.','bilgi'),(s3[2],'Doğru eşleştirmeyi yanlış sanmış; asit kireci çözer.','bilgi'),(s3[3],'Doğru eşleştirmeyi yanlış sanmış; sirke gıdalarda koruyucu ve tat verici olarak kullanılır.','bilgi'),(s3[4],'Doğru eşleştirmeyi yanlış sanmış; NaHCO₃ bazik özellikte olup asidi giderir.','bilgi')],
 istenen='Yanlış eşleştirmenin bulunması.',
 ip=['Kuvvetli ve aşındırıcı bir maddenin vücuda alınan ilaç olarak kullanılıp kullanılamayacağını düşün.'],
 bilgi=[B('Günlük hayat kimyasalları','NaOCl: ağartıcı; HCl çözeltisi (tuz ruhu): kireç çözücü; asetik asit çözeltisi (sirke): gıdada; NaHCO₃: antiasit ve kabartma tozu; NaOH: kuvvetli, aşındırıcı bazdır')],
 ad=[A('Kimyasalları tanı','Her kimyasalın adını ve özelliğini hatırla.','NaOCl: ağartıcı · HCl: asit · sirke: zayıf asit · NaHCO₃: zayıf baz · NaOH: kuvvetli baz'),A('Şıkları ele','B, C, D ve E eşleştirmeleri doğrudur.','B: doğru · C: doğru · D: doğru · E: doğru'),A('Yanlışı bul','NaOH kuvvetli ve aşındırıcı olduğundan ilaç olarak içilmez; mide yanması için bazik ve zayıf olan NaHCO₃ kullanılır.','A: yanlış → cevap A')],
 puf='Kuvvetli asit ve bazlar aşındırıcıdır; ilaç ve gıda amaçlı kullanılmaz.')
# 0004
st={'I':True,'II':True,'III':False,'IV':False,'V':True}
s4=['I ve II','I, II ve V','I, III ve V','I, II ve IV','II, IV ve V']
dog=[k for k,v in st.items() if v]; assert dog==['I','II','V']
mk(P,'0004',tipId='kim-hy-guvenli',tip='Evde kullanılan kimyasalların özellikleri',z='orta',alt='Yaygın Günlük Hayat Kimyasalları',kaz='Günlük hayattaki temizlik, gıda ve ilaç kimyasallarının özelliklerini doğru-yanlış olarak değerlendirir.',kalip='öncüllü',adim=4,
 kart='K-KHY-04 (günlük kimyasallar) · beş ifade, üçü doğru',
 metin='I. Çamaşır suyu ile tuz ruhu karıştırılırsa zehirli klor gazı açığa çıkabileceğinden birlikte kullanılmaz.\nII. Sabun molekülünün apolar hidrokarbon zinciri yağ ile, iyonik başı su ile etkileşir.\nIII. Çamaşır suyu çözeltisi asidik özelliktedir.\nIV. Gıdalarda kullanılan katkı maddelerinin tamamı doğal kaynaklıdır.\nV. Mide asidini gidermek için kullanılan antiasit ilaçlar bazik özellik gösterir.\nGünlük hayatta kullanılan kimyasallarla ilgili yukarıdaki ifadelerden hangileri doğrudur?',
 dogru=s4[1],sira=s4,
 yan=[(s4[0],'V’i yanlış sanmış; antiasitlerin mide asidini nötrleştirmek için bazik olduğunu bilmemiş.','bilgi'),(s4[3],'IV’ü doğru sanmış; katkı maddelerinin bir kısmının yapay olarak üretildiğini bilmemiş.','bilgi'),(s4[2],'II’yi yanlış, III’ü doğru sanmış; çamaşır suyunun bazik, sabunun iki kısımlı olduğunu karıştırmış.','bilgi'),(s4[4],'I’i yanlış sanıp IV’ü doğru bulmuş; karıştırma tehlikesini ve katkı maddelerinin çeşitliliğini bilmemiş.','bilgi')],
 istenen='Doğru ifadelerin belirlenmesi.',
 ip=['Çamaşır suyunun asit mi baz mı olduğunu, antiasit ilaçların ise asidi gidermek için nasıl bir madde olması gerektiğini düşün.'],
 bilgi=[B('Günlük hayat kimyasalları','çamaşır suyu bazik özelliktedir ve asitli temizleyicilerle karıştırılmaz. Antiasitler mide asidini nötrleştiren bazik maddelerdir. Gıda katkı maddeleri doğal ya da yapay olabilir')],
 ad=[A('I ve II','Klor gazı tehlikesi nedeniyle çamaşır suyu asitlerle karıştırılmaz; sabunun iki ucu farklı özelliktedir.','I: doğru · II: doğru'),A('III ve IV','Çamaşır suyu bazik özelliktedir; katkı maddelerinin bir kısmı yapaydır.','III: yanlış · IV: yanlış'),A('V','Asidi gidermek için baz gerekir.','V: doğru'),A('Sonuç','Doğru olanlar I, II ve V’tir.','I, II ve V')],
 puf='Doğru-yanlış sorularında “tamamı”, “hepsi” gibi kesin ifadeler çoğunlukla yanlıştır.')
bitir(P,'heryerde','kim|Kimya Her Yerde')
