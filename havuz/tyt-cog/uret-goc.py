import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_b import *
Q=Konu('goc','Göç','cog|Göç',6)
Q.kart('K-CGGC-01','Göç türleri','Göçler ülke sınırına göre iç/dış sınıflanır; örnekte kişinin ülke içinde mi dışında mı yer değiştirdiğine bakılır.','Yurt dışı göçü iç göç saymak; mevsimlik göçü ülke dışı sanmak.','kolay','öncüllü',2,'cg-goc-tur','Göç türlerini ayırt etme')
Q.kart('K-CGGC-02','İtici ve çekici etkenler','Göç verilen yerdeki olumsuzluklar itici, göç alan yerdeki olanaklar çekici etkendir.','İtici ve çekici etkenleri karıştırmak.','orta','öncüllü',3,'cg-goc-neden','İtici ve çekici etkenler')
Q.kart('K-CGGC-03','Göçün sonuçları','Sürekli göç veren yerde genç nüfus azalır, arazi boş kalır; göç alan yerde konut, altyapı, işsizlik sorunları artar.','Göç alan yerin sorunlarını göç veren yere yazmak.','orta','düz',3,'cg-goc-sonuc','Göç veren bölgedeki sonuçlar')
Q.kart('K-CGGC-04','Net göç','Net göç = alınan göç − verilen göç; pozitifse göç kazancı, negatifse göç kaybı vardır.','En çok göç alanı net göçü en fazla sanmak.','orta','tablo',3,'cg-goc-net','Net göç sayısı')
Q.kart('K-CGGC-05','Göçü çok ölçütle sınıflandırma','Göç yer (iç/dış), isteğe bağlılık (gönüllü/zorunlu) ve süre (geçici/kalıcı) ölçütleriyle birlikte değerlendirilir.','Üç ölçütten birini atlamak.','zor','yeni nesil',4,'cg-goc-ciftsinif','Çok ölçütlü göç sınıflaması')
Q.kart('K-CGGC-06','Net göç ve nüfus değişimi','Yıl sonu nüfusu = başlangıç nüfusu + doğal artış + net göç.','Net göçü ya da doğal artışı atlamak; işareti karıştırmak.','zor','hikâyeli',4,'cg-goc-nufusdeg','Doğal artış ve net göçle nüfus değişimi')
# ---- 0001
st=[('Bir ailenin, çalışmak üzere köyünden aynı ülkedeki sanayi kentine yerleşmesi',True,'aile ülke sınırları içinde yer değiştirmiştir'),
    ('Bir mühendisin, iş sözleşmesiyle başka bir ülkeye yerleşmesi',False,'ülke sınırı aşılmıştır, bu dış göçtür'),
    ('Bir işçinin, hasat döneminde çalışmak için aynı ülkedeki başka bir ile gidip dönmesi',True,'yer değiştirme ülke içindedir')]
op,dg=oncul(st,['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III'],'C'); assert dg=={'I','III'}
Q.S('0001','K-CGGC-01','kolay','Verilen göç örneklerini ülke sınırına göre iç ve dış göç olarak ayırır.',
 metin_oncul('Aşağıda bazı göç örnekleri verilmiştir.',st,'Bu örneklerden hangileri iç göçe örnektir?'),op,'C',
 'İç göç sayılan örneklerin belirlenmesi.','Her örnekte kişinin ülke sınırını geçip geçmediğine bak.',
 [B('İç göç ve dış göç','İç göç: ülke sınırları içinde yapılan göç (köyden kente taşınma) · Dış göç: bir ülkeden başka bir ülkeye yapılan göç. Örnek: Konya’dan İzmir’e taşınmak iç göçtür.')],
 [A('Ölçütü hatırla','İç göçte ülke sınırı aşılmaz.','iç göç = aynı ülke'),
  A('Örnekleri sına','I ve III’te kişiler aynı ülkede kalır; II’de başka bir ülkeye gidilir.','I: iç · II: dış · III: iç'),
  A('Sonuç','İç göç örnekleri I ve III’tür.','I ve III')],
 'Göçün adını, ülke sınırını geçip geçmediğine bakarak koy.','yeni göç örnekleri')
# ---- 0002
st=[('Köyde işlenebilir tarım arazisinin azalması',False,'bu, göç verilen yerdeki olumsuzluk, yani itici etkendir'),
    ('Kentte sanayi tesislerinin çok olması nedeniyle iş bulma olanağının yüksek olması',True,'hedef yerdeki iş olanağı çekici etkendir'),
    ('Kentte eğitim ve sağlık kurumlarının çeşitli olması',True,'hedef yerdeki hizmet çokluğu çekici etkendir'),
    ('Köyde doğal afet riskinin yüksek olması',False,'bu, çıkış yerindeki olumsuzluktur, itici etkendir')]
op,dg=oncul(st,['Yalnız II','I ve II','I ve IV','II ve IV','II ve III'],'E'); assert dg=={'II','III'}
Q.S('0002','K-CGGC-02','orta','Göçe neden olan etkenleri itici ve çekici olarak ayırt eder.',
 metin_oncul('Köyünü bırakıp kente yerleşen bir ailenin göç gerekçeleri şöyle sıralanmıştır:',st,'Bu gerekçelerden hangileri göç edilen kentin çekici (çeken) etkenlerindendir?'),op,'E',
 'Çekici etkenlerin belirlenmesi.','Gerekçenin köyün mü, kentin mi özelliği olduğuna bak.',
 [B('İtici ve çekici etkenler','İtici etken: insanı göç verilen (çıkış) yerden uzaklaştıran olumsuzluk (arazi azlığı, afet, işsizlik) · Çekici etken: göç alan (varış) yerin cazibesi (iş, eğitim, sağlık hizmeti)')],
 [A('Ayrımı yap','Köydeki olumsuzluklar iter, kentteki olanaklar çeker.','köy: itici · kent: çekici'),
  A('Gerekçeleri sına','I ve IV köyün olumsuzluğudur; II ve III kentin olanağıdır.','I: itici · II: çekici · III: çekici · IV: itici'),
  A('Sonuç','Çekici etkenler II ve III’tür.','II ve III')],
 'Gerekçenin kimin özelliği olduğuna bak: çıkış yerinin olumsuzluğu iter, varış yerinin olanağı çeker.','4 gerekçe, doğru kümesi hesaplandı')
# ---- 0003
Q.S('0003','K-CGGC-03','orta','Göç veren bölgelerde görülen sonuçları belirler.',
 'Genç ve çalışabilir nüfusun uzun yıllardır başka bölgelere göç ettiği bir dağ köyünde yaşayanlar azalmaktadır.\nBu köyde aşağıdakilerden hangisinin görülmesi beklenir?',
 [('Konut ihtiyacının ve konut fiyatlarının hızla artması',False,'Konut ihtiyacı göç alan yerde artar; bu köy nüfus kaybetmektedir.','bilgi'),('Tarım arazilerinin boş kalması ve yaşlı oranının artması',True,'',''),('İşsizlik ve altyapı sorunlarının hızla artması',False,'Bu sorunlar nüfusu hızla artan, göç alan yerlerde görülür.','bilgi'),('Yerleşme alanının kontrolsüz biçimde genişlemesi',False,'Köy nüfus kaybettiği için çarpık yerleşme değil, boşalma yaşar.','bilgi'),('Köydeki nüfus yoğunluğunun belirgin biçimde artması',False,'Göç verildiği için nüfus ve yoğunluk azalır.','dikkat')],'B',
 'Göç veren köydeki beklenen sonuç.','Göç eden kesimin genç olduğunu ve geride kalanların kimler olduğunu düşün.',
 [B('Göçün sonuçları','Göç veren yer: genç nüfus azalır, yaşlı oranı artar, tarım arazisi boş kalabilir. Göç alan yer: konut, altyapı ve işsizlik sorunları artar, yerleşme alanı genişler.')],
 [A('Soruyu yönlendir','Köy göç veren yerdir; nüfus ve genç iş gücü azalır.','göç veren: nüfus ↓'),
  A('Geride kalanları düşün','Çalışabilen gençler gidince tarlalara bakacak kişi azalır; yaşlılar kalır.','arazi boş · yaşlı oranı ↑'),
  A('Şıkları ele','Konut, altyapı ve işsizlik sorunları ile kontrolsüz yayılma göç alan yerin sorunudur.','B: doğru · A, C, D, E: yanlış')],
 'Sorunun göç alan mı, veren mi olduğunu belirle; sonuçlar ters yönde olur.','göç veren yer sonuçları')
# ---- 0004
tab={'K':(50000,40000),'L':(20000,45000),'M':(18000,22000),'N':(42000,30000),'P':(31000,29000)}
net={k:a-v for k,(a,v) in tab.items()}; assert net=={'K':10000,'L':-25000,'M':-4000,'N':12000,'P':2000} and max(net,key=net.get)=='N'
assert max(tab,key=lambda k:tab[k][0])=='K' and max(tab,key=lambda k:tab[k][1])=='L'
Q.S('0004','K-CGGC-04','orta','Göç alan ve veren sayılarından net göçü hesaplayıp karşılaştırır.',
 'Beş ilin bir yıl içinde aldığı ve verdiği göç sayıları aşağıdaki tabloda gösterilmiştir. Veriler kurgusaldır.\nİl – Aldığı göç – Verdiği göç\nK – 50 000 – 40 000\nL – 20 000 – 45 000\nM – 18 000 – 22 000\nN – 42 000 – 30 000\nP – 31 000 – 29 000\nBu verilere göre hangi ilin göç kazancı (net göç artışı) en fazladır?',
 [('K',False,'En çok göç alan ili seçmiş; K’nin verdiği göç de fazla olduğundan net göç yalnız 10 000’dir.','dikkat'),('L',False,'En çok göç veren ili seçmiş; L’nin net göçü −25 000’dir, kayıp vardır.','dikkat'),('M',False,'M’nin net göçü −4 000’dir; verdiği göç aldığından fazladır.','islem'),('N',True,'',''),('P',False,'P’nin net göçü yalnız +2 000’dir.','islem')],'D',
 'Net göç değeri en büyük olan il.','Net göç, alınan ve verilen göçün farkıdır; yalnız aldığı göce bakmak yetmez.',
 [B('Net göç','Net göç = alınan göç − verilen göç. Pozitifse göç kazancı, negatifse göç kaybı vardır. Örnek: 500 kişi gelen, 300 kişi giden yerde net göç +200’dür.')],
 [A('Formülü yaz','Her il için alınan göçten verilen göçü çıkar.','net göç = alınan − verilen'),
  A('İllerin net göçü','Farkları hesapla.','K: 10 000 · L: −25 000 · M: −4 000 · N: 12 000 · P: 2 000'),
  A('Karşılaştır','En büyük pozitif değer aranır.','12 000 > 10 000 > 2 000 > −4 000 > −25 000 · en fazla: N')],
 'Net göç sorularında “gelen − giden” farkını her satır için ayrı hesapla.','kurgusal tablo',kalip='tablo')
# ---- 0005
Pp=[('Bir garson, turizm sezonunda çalışmak için aynı ülkedeki bir kıyı kentine gitmiş ve sezon sonunda evine dönmüştür.',('iç','gönüllü','geçici')),
    ('Bir öğrenci, bir yıllık değişim programı için başka bir ülkeye gitmiş ve program bitince dönmüştür.',('dış','gönüllü','geçici')),
    ('Taşkında köyü su altında kalan bir aile, su çekilene kadar ülkenin başka bir ilinde barındırılmış, sonra köyüne dönmüştür.',('iç','zorunlu','geçici')),
    ('Bir öğretmen, kendi isteğiyle aynı ülkedeki başka bir kente tayin isteyip oraya yerleşmiş ve geri dönmeyi düşünmemektedir.',('iç','gönüllü','kalıcı')),
    ('Savaştan kaçan bir aile, komşu bir ülkeye yerleşmiş ve geri dönmeyi planlamamaktadır.',('dış','zorunlu','kalıcı'))]
hedef=('iç','gönüllü','geçici'); assert [p[1]==hedef for p in Pp]==[True,False,False,False,False]
def fark(t): return [x for x,y in zip(('ülke sınırı','isteğe bağlılık','süre'),t) if False]
isim=['Kişi'] 
CLM={1:'L ülke dışına gittiği için dış göçtür; aranan iç göç koşulunu sağlamaz.',2:'M afet yüzünden gittiği için göçü zorunludur; aranan gönüllü göç koşulunu sağlamaz.',3:'N geri dönmeyi düşünmediği için göçü kalıcıdır; aranan geçici göç koşulunu sağlamaz.',4:'P ülke dışına gitmiş (dış göç), savaş yüzünden zorunlu ve kalıcı yerleşmiştir; üç koşulun hiçbirini sağlamaz.'}
for i in range(1,5): assert Pp[i][1]!=hedef
op=[(f'{"KLMNP"[i]}',i==0,CLM[i] if i else '','bilgi' if i else '') for i in range(5)]
ls='\n'.join(f'{"KLMNP"[i]}: {Pp[i][0]}' for i in range(5))
Q.S('0005','K-CGGC-05','zor','Göç örneklerini yer, istek ve süre ölçütlerine göre birlikte sınıflandırır.',
 'Aşağıda beş kişinin göç öyküsü verilmiştir.\n'+ls+'\nBu öykülerden hangisi aynı anda hem iç göç hem gönüllü göç hem de geçici göçe örnektir?',op,'A',
 'Üç ölçütü birlikte sağlayan göç.','Her öyküyü üç soruyla sına: ülke içinde mi, kendi isteğiyle mi, geri dönüş var mı?',
 [B('Göç ölçütleri','Yer: iç / dış göç · İstek: gönüllü (kendi isteği) / zorunlu (afet, savaş) · Süre: geçici (mevsimlik, dönmek üzere) / kalıcı (yerleşmek üzere). Örnek: hasat için gidip dönen işçi iç, gönüllü, geçici göç yapmıştır.')],
 [A('Ölçütleri yaz','Aranan göç: iç + gönüllü + geçici.','iç · gönüllü · geçici'),
  A('K, L ve M’yi sına','K üç ölçütü sağlar. L başka ülkeye gittiği için dış; M ise afet yüzünden gittiği için zorunludur.','K: iç, gönüllü, geçici · L: dış · M: zorunlu'),
  A('N ve P’yi sına','N geri dönmeyi düşünmediği için kalıcıdır; P hem dış hem zorunlu hem kalıcıdır.','N: kalıcı · P: dış, zorunlu, kalıcı'),
  A('Sonuç','Yalnız K’nin öyküsü üç ölçütün hepsini sağlar.','K')],
 'Çok ölçütlü sorularda her seçeneği ölçütlerin hepsiyle tek tek sına.','5 öykü, ölçütler kodla karşılaştırıldı',kalip='yeni nesil')
# ---- 0006
n0=400000; al,ve=14000,22000; dgm,olm=18,8
da=Fr(n0*(dgm-olm),1000); ng=al-ve
assert da==4000 and ng==-8000 and n0+da+ng==396000
assert n0+ng*2+da==388000 and n0+da==404000 and n0+da+ng*-1==412000 and n0+ng==392000
Q.S('0006','K-CGGC-06','zor','Doğal artış ve net göçü birlikte kullanarak yıl sonu nüfusunu bulur.',
 'Nüfusu 400 000 olan bir ilde bir yıl boyunca binde 18 doğum ve binde 8 ölüm gerçekleşmiş, ile başka yerlerden 14 000 kişi gelerek yerleşmiş, ilden ise 22 000 kişi başka yerlere göç etmiştir. Başka bir nüfus hareketi olmamıştır.\nBuna göre ilin yıl sonundaki nüfusu kaç kişidir?',
 [('388 000',False,'Net göçü (−8 000) iki kez çıkarmış.','islem'),('392 000',False,'Doğal artışı (+4 000) katmamış; yalnız net göçü çıkarmış.','dikkat'),('396 000',True,'',''),('404 000',False,'Göçü hiç hesaba katmamış; yalnız doğal artışı eklemiş.','dikkat'),('412 000',False,'Net göç kaybını nüfusa eklemiş; işareti ters almış.','islem')],'C',
 'İlin yıl sonu nüfusu.','Nüfusun değişimi iki kaynaktan gelir: doğum–ölüm farkı ve göç alma–verme farkı.',
 [B('Nüfus değişimi','Yıl sonu nüfusu = başlangıç nüfusu + doğal artış + net göç. Doğal artış = nüfus × (doğum − ölüm) ÷ 1000; net göç = alınan − verilen. Örnek: 1000 nüfuslu yerde artış 10‰, net göç −2 ise 1000 + 10 − 2 = 1008 olur.')],
 [A('Doğal artış','Binde 18 − binde 8 = binde 10 artış.','400 000 × 10 ÷ 1000 = 4 000'),
  A('Net göç','Alınan göçten verilen göçü çıkar.','14 000 − 22 000 = −8 000'),
  A('Yıl sonu nüfusu','Başlangıç nüfusuna ikisini de ekle.','400 000 + 4 000 − 8 000 = 396 000')],
 'Nüfus değişimini iki parçaya ayır: doğal artış ve net göç; ikisini de başlangıca ekle.','doğal artış + net göç, kodla doğrulandı')
Q.bitir()
