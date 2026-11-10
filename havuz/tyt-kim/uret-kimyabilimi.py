import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
H.KONU='Kimya Bilimi'
P=Parti('kimyabilimi','Kimya Bilimi','kim|Kimya Bilimi',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (kimya disiplinleri, sembolik dil, iş güvenliği) · MEB 9. sınıf'
kart('K-KBL-01','Kimya disiplinleri','Analitik kimya madde miktarı/türü analizi; organik kimya karbon bileşikleri; biyokimya canlıdaki olaylar.','Maddenin türüne bakıp disiplini seçmek; çalışmanın amacını gözden kaçırmak.','kolay','düz',2,'kim-kb-disiplin','Kimya disiplinleri',KY)
kart('K-KBL-02','Kimyanın sembolik dili','Katsayı tüm formül birimini, alt indis yalnız önündeki atomu (ya da parantezi) çoğaltır.','Katsayıyı atlamak; parantez dışı indisi iç atomlara uygulamamak.','orta','düz',3,'kim-kb-formul','Formülde atom sayısı',KY)
kart('K-KBL-03','Kimyanın sembolik dili','Tepkime denkleminde atom türü ve sayısı iki yanda eşitlenir; katsayılar bulunur.','Hidrojen ve oksijeni sayarken indisleri unutmak.','orta','düz',3,'kim-kb-denkles','Denklem denkleştirme',KY)
kart('K-KBL-04','İş sağlığı ve güvenliği','Laboratuvarda doğru davranışlar: asit suya eklenir, kokular yelpazelenerek, zehirli gazlarla çeker ocak.','Kokuyu doğrudan koklamak; artan kimyasalı şişeye geri boşaltmak.','orta','öncüllü',4,'kim-kb-guvenlik','Laboratuvar güvenliği',KY)
# 0001
s1=['Endüstriyel kimya','Biyokimya','Fizikokimya','Organik kimya','Analitik kimya']
mk(P,'0001',tipId='kim-kb-disiplin',tip='Kimya disiplinleri',z='kolay',alt='Kimya Disiplinleri',kaz='Bir çalışmanın hangi kimya disiplinine ait olduğunu belirler.',kalip='düz',adim=2,
 kart='K-KBL-01 (kimya disiplinleri) · su numunesinde kurşun miktarı',
 metin='Bir kimyager, bir göl suyundan aldığı numunede çözünmüş kurşun iyonlarının miktarını belirlemek için bir ölçüm yöntemi uygulamaktadır. Kimyagerin amacı, numunede hangi maddenin ne kadar bulunduğunu saptamaktır.\nBu çalışma, kimyanın aşağıdaki disiplinlerinden hangisinin alanına girer?',
 dogru=s1[4],sira=s1,
 yan=[(s1[0],'Çalışmayı üretim ve endüstriyel uygulama sanmış; burada amaç numunedeki madde miktarını belirlemektir.','dikkat'),(s1[1],'Canlıyla ilgisi olmayan bir su numunesini biyokimya sanmış.','bilgi'),(s1[2],'Enerji ve hız gibi fiziksel ilkeleri inceleyen disiplini seçmiş.','bilgi'),(s1[3],'Organik kimyayı karbon bileşikleriyle ilişkilendirmeyi bilmemiş; burada karbon bileşiği incelenmiyor.','bilgi')],
 istenen='Çalışmanın ait olduğu kimya disiplini.',
 ip=['Kimyagerin amacı bir maddenin ne olduğunu ya da ne kadar olduğunu bulmak mı, yoksa yeni madde üretmek mi?'],
 bilgi=[B('Analitik kimya','maddelerin türünü (nitel) ve miktarını (nicel) belirleyen kimya dalıdır. Örnek: sütteki kalsiyum miktarının bulunması')],
 ad=[A('Amacı belirle','Çalışmada kurşun iyonlarının miktarı ölçülüyor; yeni madde elde edilmiyor.','amaç: miktar belirleme'),A('Disiplinleri ele','Organik kimya karbon bileşiklerini, biyokimya canlıdaki olayları, fizikokimya enerji ve hız gibi ilkeleri, endüstriyel kimya üretim süreçlerini inceler.','Bu çalışma onların konusu değil'),A('Disiplini seç','Madde miktarı ve türü tayini analitik kimyanın konusudur.','Analitik kimya')],
 puf='Disiplini maddenin kendisine değil, çalışmanın amacına bakarak seç.')
# 0002
k=3; al,s_,o=2,3,12
tot=k*(al+s_+o); assert tot==51 and (al+s_+o)==17 and k*(2+1+4)==21 and k*(2+3+4)==27 and tot+3==54
mk(P,'0002',tipId='kim-kb-formul',tip='Formülde atom sayısı',z='orta',alt='Kimyanın Sembolik Dili',kaz='Katsayı ve parantez dışı indisleri kullanarak formülde toplam atom sayısını bulur.',kalip='düz',adim=3,
 kart='K-KBL-02 (sembolik dil) · 3Al₂(SO₄)₃ ifadesinde toplam atom',
 metin='3Al₂(SO₄)₃ ifadesinde toplam kaç atom vardır?',
 dogru=51,yan=[(17,'Başındaki katsayıyı (3) hesaba katmamış.','dikkat'),(21,'Parantez dışındaki indisi (3) S ve O atomlarına uygulamamış.','bilgi'),(27,'Parantez dışındaki indisi yalnız S’ye uygulamış, O’nun 4 olduğunu değiştirmemiş.','bilgi'),(54,'Katsayıyı (3) toplam atom sayısına eklemiş.','islem')],
 istenen='3Al₂(SO₄)₃ içindeki toplam atom sayısı.',
 ip=['Önce bir Al₂(SO₄)₃ biriminde atom türlerini say; parantez dışındaki indis parantezin içindeki her atomu çarpar.'],
 bilgi=[B('Formülde sayma','katsayı bütün formül birimini çoğaltır, alt indis önündeki atomu ya da parantezi çoğaltır. Örnek: 2Ca(OH)₂ içinde 2 Ca, 4 O, 4 H vardır')],
 ad=[A('Parantezi aç','(SO₄)₃ içinde 3 S ve 3 × 4 = 12 O vardır.','S: 3 · O: 12'),A('Tek birimdeki atomlar','Al₂ ile birlikte tüm atomlar toplanır.','2 + 3 + 12 = 17 atom'),A('Katsayıyı uygula','3 formül birimi vardır.','3 × 17 = 51')],
 puf='Önce parantezi aç, sonra katsayıyla çarp.')
# 0003
import itertools
sol=[(a,b,c,d) for a,b,c,d in itertools.product(range(1,13),repeat=4) if 3*a==c and 8*a==2*d and 2*b==2*c+d]
sol=[x for x in sol if x[0]==1]; assert sol==[(1,5,3,4)] and sum(sol[0])==13
assert 1+5+3+4==13 and 5+4==9 and 5+3+4==12 and 1+7+3+4==15 and 1+9+3+4==17
mk(P,'0003',tipId='kim-kb-denkles',tip='Denklem denkleştirme',z='orta',alt='Kimyanın Sembolik Dili',kaz='Kimyasal denklemi denkleştirip katsayılar toplamını bulur.',kalip='düz',adim=3,
 kart='K-KBL-03 (denkleştirme) · propanın yanma denklemi, katsayılar toplamı',
 metin='C₃H₈ + O₂ → CO₂ + H₂O\nDenkleşmemiş tepkimesi verilen bu yanma tepkimesi en küçük tam sayılarla denkleştirildiğinde katsayıların toplamı kaç olur?',
 dogru=13,yan=[(9,'Yalnız O₂ ile H₂O’nun katsayılarını (5 + 4) toplamış.','dikkat'),(12,'Katsayısı 1 olan C₃H₈’i toplamaya katmamış.','dikkat'),(15,'O atomlarını sayarken O₂ katsayısını 7 bulmuş.','islem'),(17,'O atomlarını sayarken O₂ katsayısını 9 bulmuş.','islem')],
 istenen='Denkleştirilmiş denklemdeki katsayıların toplamı.',
 ip=['Önce C ve H atomlarını eşitle; oksijen atomlarını en son say.'],
 bilgi=[B('Denkleştirme','tepkimenin iki yanında her atomdan eşit sayıda bulunmalıdır; yalnız katsayılar değiştirilir, indisler değişmez. Örnek: 2H₂ + O₂ → 2H₂O')],
 ad=[A('C ve H’yi eşitle','1 C₃H₈ için 3 CO₂ ve 4 H₂O gerekir.','C: 3 → 3CO₂ · H: 8 → 4H₂O'),A('Oksijeni say','Ürün tarafında O atomu sayısı bulunur.','3 × 2 + 4 × 1 = 10 O → 5O₂'),A('Katsayıları topla','Denklem 1, 5, 3, 4 katsayılarıyla denkleşir.','C₃H₈ + 5O₂ → 3CO₂ + 4H₂O · 1 + 5 + 3 + 4 = 13')],
 puf='Denkleştirmede en çok geçen ve yalnız tek maddede bulunan atomlardan başla, O₂ gibi serbest elementi sona bırak.')
# 0004
st={'I':True,'II':False,'III':True,'IV':False,'V':True}
s4=['I ve III','I, III ve V','I, II ve V','I, III ve IV','II, IV ve V']
dog=[k for k,v in st.items() if v]; assert dog==['I','III','V']
mk(P,'0004',tipId='kim-kb-guvenlik',tip='Laboratuvar güvenliği',z='orta',alt='Kimya Uygulamalarında İş Sağlığı ve Güvenliği',kaz='Kimya laboratuvarında güvenli ve güvensiz davranışları ayırt eder.',kalip='öncüllü',adim=4,
 kart='K-KBL-04 (iş güvenliği) · beş davranış, üçü doğru',
 metin='I. Seyreltik asit çözeltisi hazırlarken asit, karıştırılarak suya azar azar eklenir.\nII. Bir kimyasalın kokusunu belirlemek için kap buruna yaklaştırılıp derin nefes alınır.\nIII. Yanıcı simgesi taşıyan kimyasallar açık alevden uzak tutulur.\nIV. Deney sonunda artan kimyasallar, tekrar kullanılmak üzere stok şişesine geri boşaltılır.\nV. Uçucu ve zehirli gaz çıkaran deneyler çeker ocak altında yapılır.\nBir kimya laboratuvarındaki davranışlarla ilgili yukarıdaki ifadelerden hangileri doğrudur?',
 dogru=s4[1],sira=s4,
 yan=[(s4[0],'V’i yanlış sanmış; zehirli gazların çeker ocakta çalışılarak uzaklaştırıldığını bilmemiş.','bilgi'),(s4[2],'II’yi doğru sanmış; kokunun elle yelpazelenerek ve çok az alınarak anlaşılması gerektiğini bilmemiş.','bilgi'),(s4[3],'IV’ü doğru sanmış; artan kimyasalın şişeyi kirleteceğini düşünmemiş.','bilgi'),(s4[4],'I ve III’ü yanlış sanıp II ve IV’ü doğru bulmuş; güvenlik kurallarını ters yorumlamış.','bilgi')],
 istenen='Doğru ifadelerin belirlenmesi.',
 ip=['Her ifadeyi güvenlik kuralına göre ayrı ayrı değerlendir; kimyasalı kaba geri boşaltmak ve doğrudan koklamak güvenli değildir.'],
 bilgi=[B('Laboratuvar güvenliği','asit suya azar azar eklenir; kokular elle yelpazelenerek anlaşılır; artan kimyasal stok şişesine geri konmaz; zehirli gazlarda çeker ocak kullanılır. Örnek: derişik asit seyreltilirken asit suya eklenir')],
 ad=[A('I ve II','Asit seyreltilirken asit suya azar azar eklenir; kokular doğrudan koklanmaz.','I: doğru · II: yanlış'),A('III ve IV','Yanıcı maddeler alevden uzak tutulur; artan kimyasal stok şişesini kirletir.','III: doğru · IV: yanlış'),A('V','Zehirli gazlar çeker ocakta çalışılarak uzaklaştırılır.','V: doğru'),A('Sonuç','Doğru olanlar I, III ve V’tir.','I, III ve V')],
 puf='Güvenlik sorularında kimyasalla doğrudan temas ve kirletme içeren davranışlar yanlıştır.')
bitir(P,'kimyabilimi','kim|Kimya Bilimi')
