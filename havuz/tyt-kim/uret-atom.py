import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
H.KONU='Atom ve Yapısı'
P=Parti('atom','Atom ve Yapısı','kim|Atom ve Yapısı',ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 (atomun yapısı, atom modelleri) · MEB 9. sınıf'
kart('K-KAT-01','Atomun yapısı','Atom numarası proton sayısını verir; nötr atomda elektron = proton, iyonda yüke göre değişir.','İyon yükünü ters işlemek; kütle numarasını proton sanmak.','kolay','düz',2,'kim-at-iyon','İyonda tanecik sayıları',KY)
kart('K-KAT-02','Atomun yapısı','İzotop: aynı proton; izobar: aynı kütle numarası; izoton: aynı nötron sayısı.','Üç kavramı birbirine karıştırmak; nötron sayısını hesaplamayı atlamak.','orta','öncüllü',3,'kim-at-izo','İzotop, izobar, izoton',KY)
kart('K-KAT-03','Atom modelleri','Dalton, Thomson, Rutherford ve Bohr modellerinin getirdiği temel yenilik.','Çekirdeğin keşfini Thomson’a, elektronun keşfini Rutherford’a yazmak.','orta','düz',3,'kim-at-model','Atom modelleri ve katkıları',KY)
kart('K-KAT-04','Atomun yapısı','İzoelektronik taneciklerde elektron sayısı eşit; proton sayısı yükten geriye doğru bulunur.','Elektron sayısını proton sayısı sanmak; iyon yükünü yanlış yönde eklemek.','zor','düz',4,'kim-at-izoelektronik','İzoelektronik iyonlar',KY)
# 0001
A_,n_,q=32,16,-2; Z=A_-n_; e=Z-q; assert Z==16 and e==18
mk(P,'0001',tipId='kim-at-iyon',tip='İyonda tanecik sayıları',z='kolay',alt='Atomun Yapısı',kaz='İyonun proton, nötron ve elektron sayısını yük ve kütle numarasından hesaplar.',kalip='düz',adim=2,
 kart='K-KAT-01 (atomun yapısı) · eksi yüklü iyonun elektron sayısı',
 metin='X²⁻ iyonunun kütle numarası 32, nötron sayısı 16’dır.\nBuna göre X²⁻ iyonunun elektron sayısı kaçtır?',
 dogru=18,yan=[(14,'İyonun eksi yükünü elektrondan çıkarmış; eksi yük elektron fazlalığıdır.','dikkat'),(16,'Elektron sayısını proton sayısına eşit almış; iyonda bu eşitlik bozulur.','bilgi'),(32,'Kütle numarasını elektron sayısı sanmış.','bilgi'),(34,'Kütle numarasına yükü ekleyip 32 + 2 işlemini yapmış.','islem')],
 istenen='X²⁻ iyonundaki elektron sayısı.',
 ip=['Önce proton sayısını kütle numarası ile nötron sayısından bul; sonra iyon yüküne bak.'],
 bilgi=[B('Atom ve iyon','kütle numarası = proton + nötron. Nötr atomda elektron = proton. 2− yüklü iyon, atoma göre 2 elektron fazla taşır. Örnek: O²⁻ iyonunda proton 8, elektron 10')],
 ad=[A('Proton sayısı','Kütle numarasından nötron sayısı çıkarılır.','p = 32 − 16 = 16'),A('Yükü yorumla','2− yük, atomun 2 elektron kazandığını gösterir.','nötr atomda e = 16 · iyonda 2 fazla'),A('Elektron sayısı','Nötr atomdaki elektron sayısına 2 eklenir.','e = 16 + 2 = 18')],
 puf='İyonda elektron sayısı = proton sayısı − yük (yük işaretiyle birlikte düşünülür).')
# 0002
at={'X':(18,40),'Y':(20,40),'Z':(20,42)}
nn={k:v[1]-v[0] for k,v in at.items()}
izobar=lambda a,b:at[a][1]==at[b][1] and at[a][0]!=at[b][0]
izoton=lambda a,b:nn[a]==nn[b] and at[a][0]!=at[b][0]
izotop=lambda a,b:at[a][0]==at[b][0] and at[a][1]!=at[b][1]
T1=izobar('X','Y'); T2=izotop('Y','Z'); T3=izoton('Y','Z'); assert (T1,T2,T3)==(True,True,False) and nn=={'X':22,'Y':20,'Z':22}
mk(P,'0002',tipId='kim-at-izo',tip='İzotop, izobar, izoton',z='orta',alt='Atomun Yapısı',kaz='İzotop, izobar ve izoton atomları atom numarası ve kütle numarasına göre ayırt eder.',kalip='öncüllü',adim=3,
 kart='K-KAT-02 (izotop-izobar-izoton) · üç atomlu tablo, Y–Z izoton sanılır',
 metin='Nötr X, Y ve Z atomlarının atom numaraları ve kütle numaraları tabloda verilmiştir.\nAtom: X · Atom numarası: 18 · Kütle numarası: 40\nAtom: Y · Atom numarası: 20 · Kütle numarası: 40\nAtom: Z · Atom numarası: 20 · Kütle numarası: 42\nI. X ile Y izobardır.\nII. Y ile Z izotoptur.\nIII. Y ile Z izotondur.\nBu atomlarla ilgili yukarıdaki ifadelerden hangileri doğrudur?',
 dogru='I ve II',sira=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],
 yan=[('Yalnız I','İzotop tanımını bilmemiş; atom numarası eşit olan Y ile Z’nin izotop olduğunu görmemiş.','bilgi'),('II ve III','I’i yanlış sanmış; kütle numarası eşit olan X ile Y’nin izobar olduğunu görmemiş. III’ü doğru sanmış; oysa Y’nin nötron sayısı 20, Z’nin 22’dir, izoton değildirler.','bilgi'),('I ve III','II’yi yanlış sanıp III’ü doğru bulmuş; Y ve Z’nin nötron sayılarını (20 ve 22) karşılaştırmamış.','islem'),('I, II ve III','III’ü doğru saymış; nötron sayılarını hesaplamadan izotonu izotopla karıştırmış.','islem')],
 istenen='Doğru ifadelerin belirlenmesi.',
 ip=['İzoton için kütle numarasından atom numarasını çıkararak her atomun nötron sayısını bul.'],
 bilgi=[B('İzotop–izobar–izoton','izotop: proton sayısı aynı, kütle numarası farklı; izobar: kütle numarası aynı, proton sayısı farklı; izoton: nötron sayısı aynı. Örnek: ¹²C ile ¹³C izotoptur')],
 ad=[A('Nötron sayıları','Nötron sayısı kütle numarasından atom numarası çıkarılarak bulunur.','X: 40 − 18 = 22 · Y: 40 − 20 = 20 · Z: 42 − 20 = 22'),A('Her ifadeyi sına','Kütle ve atom numaralarını karşılaştır.','I: X ve Y kütle numarası 40 → doğru · II: Y ve Z atom numarası 20 → doğru'),A('III’ü incele','Y ile Z’nin nötron sayıları farklıdır.','III: 20 ≠ 22 → yanlış'),A('Sonuç','Doğru olanlar I ve II’dir.','I ve II')],
 puf='Önce her atomun proton ve nötron sayısını yaz; izo-sözcüklerini bu iki sayıya göre karşılaştır.')
# 0003
sira3=['Dalton: Atomu, içi dolu ve bölünemeyen bir küre olarak tanımlamıştır.','Thomson: Atomun artı yüklü bir kütle içine gömülü elektronlardan oluştuğunu öne sürmüştür.','Thomson: Atomun merkezinde artı yüklü bir çekirdek bulunduğunu göstermiştir.','Rutherford: Atomun artı yükünün ve kütlesinin büyük bölümünün küçük bir çekirdekte toplandığını bulmuştur.','Bohr: Elektronların çekirdek çevresinde belirli enerjili katmanlarda bulunduğunu öne sürmüştür.']
sira3=[sira3[0],sira3[1],sira3[3],sira3[4],sira3[2]]
mk(P,'0003',tipId='kim-at-model',tip='Atom modelleri ve katkıları',z='orta',alt='Atom Modelleri',kaz='Atom modellerini ve bilim insanlarının getirdiği temel yenilikleri eşleştirir.',kalip='düz',adim=3,
 kart='K-KAT-03 (atom modelleri) · yanlış eşleştirme: çekirdek Thomson’a yazılmış',
 metin='Aşağıdaki bilim insanı ve atom modeline getirdiği yenilik eşleştirmelerinden hangisi yanlıştır?',
 dogru=sira3[4],sira=sira3,
 yan=[(sira3[0],'Doğru eşleştirmeyi yanlış sanmış; Dalton atomu bölünemeyen küre kabul eder.','bilgi'),(sira3[1],'Doğru eşleştirmeyi yanlış sanmış; elektronlu “üzümlü kek” modeli Thomson’a aittir.','bilgi'),(sira3[2],'Doğru eşleştirmeyi yanlış sanmış; çekirdeğin varlığı Rutherford’un saçılma deneyiyle bulunmuştur.','bilgi'),(sira3[3],'Doğru eşleştirmeyi yanlış sanmış; enerji katmanları fikri Bohr modelindedir.','bilgi')],
 istenen='Yanlış eşleştirmenin bulunması.',
 ip=['Çekirdeğin keşfini hangi bilim insanının yaptığını düşün; Thomson’ın modelinde atomun içi nasıl düzenlenmişti?'],
 bilgi=[B('Atom modelleri','Dalton: bölünemeyen küre. Thomson: elektronun keşfi, artı yüklü kütle içinde elektronlar. Rutherford: çekirdek. Bohr: belirli enerjili katmanlar')],
 ad=[A('Modelleri sırala','Dalton → Thomson → Rutherford → Bohr sırasıyla her modelin yeniliğini hatırla.','Dalton: bölünemez · Thomson: elektron · Rutherford: çekirdek · Bohr: katman'),A('Seçenekleri ele','Dalton, Rutherford ve Bohr eşleştirmeleri doğrudur; Thomson’ın elektronlu modeli de doğrudur.','Dalton ✓ · Thomson (elektron) ✓ · Rutherford ✓ · Bohr ✓'),A('Yanlışı bul','Çekirdeği Rutherford bulmuştur, Thomson modelinde çekirdek yoktur.','Thomson: çekirdek → yanlış')],
 puf='Çekirdek Rutherford, elektron Thomson, katmanlar Bohr ile eşleşir.')
# 0004
Ax,nx=27,14; Zx=Ax-nx; ex=Zx-3; Zy=ex-(-2)*-1; 
Zy=ex-2; Ay=17; ny=Ay-Zy; assert Zx==13 and ex==10 and Zy==8 and ny==9 and nx+ny==23
assert (nx+(Ay-ex))==21 and (nx+(Ay-(ex+2)))==19 and nx+Ay==31 and nx+(Ay-(Zx+3-2))==17
mk(P,'0004',tipId='kim-at-izoelektronik',tip='İzoelektronik iyonlar',z='zor',alt='Atomun Yapısı',kaz='Elektron sayıları eşit iyonlardan yola çıkarak atomların nötron sayılarını bulur.',kalip='düz',adim=4,
 kart='K-KAT-04 (izoelektronik) · X³⁺ ile Y²⁻ elektron sayısı eşit',
 metin='X³⁺ ve Y²⁻ iyonlarının elektron sayıları birbirine eşittir. X atomunun kütle numarası 27, nötron sayısı 14; Y atomunun kütle numarası 17’dir.\nBuna göre X ve Y atomlarının nötron sayıları toplamı kaçtır?',
 dogru=23,yan=[(17,'X³⁺ iyonunun elektron sayısını 16 bulmuş (yükü eklemiş), böylece Y’nin proton sayısı yanlış çıkmış.','dikkat'),(19,'Y²⁻ iyonunun elektron sayısına yükü ekleyerek Y’nin proton sayısını 12 bulmuş.','dikkat'),(21,'Y²⁻ iyonunun elektron sayısını (10) Y’nin proton sayısı sanmış.','bilgi'),(31,'Y’nin kütle numarasını (17) nötron sayısı olarak toplamış.','islem')],
 istenen='X ve Y atomlarının nötron sayıları toplamı.',
 ip=['X’in proton sayısından X³⁺’ın elektron sayısına, oradan Y’nin proton sayısına git.'],
 bilgi=[B('İyonda elektron','artı yüklü iyonda elektron = proton − yük; eksi yüklü iyonda elektron = proton + yük. Örnek: Mg²⁺ (p = 12) 10 elektron taşır')],
 ad=[A('X’in proton sayısı','Kütle numarasından nötron sayısı çıkarılır.','pₓ = 27 − 14 = 13'),A('Elektron sayısı','X³⁺ üç elektron vermiştir; Y²⁻ ile elektron sayısı eşittir.','e = 13 − 3 = 10'),A('Y’nin proton sayısı','Y²⁻ iyonu 2 elektron almıştır.','p_Y = 10 − 2 = 8 · n_Y = 17 − 8 = 9'),A('Toplam','İki atomun nötron sayıları toplanır.','14 + 9 = 23')],
 puf='Elektron sayısı eşit iyon çiftlerinde her iyonun elektronunu yazıp protonlara geri dön.')
bitir(P,'atom','kim|Atom ve Yapısı')
