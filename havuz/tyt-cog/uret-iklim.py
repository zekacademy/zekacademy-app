"""TYT Coğrafya · İklimler: 6 ana soru (hafif mod). Metinler, sayılar ve şekiller özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_a import *
KY='ÖSYM 2018–2026 (iklim grafikleri, iklim tipleri) · MEB 9–10. sınıf coğrafya'
KARTLAR={
 'K-IKL-01':dict(alt='İklim tipini özelliklerinden bulma',fikir='Sıcaklık, yağış miktarı ve yağışın yıl içi dağılışı birlikte okunup iklim tipi belirlenir.',tuzak='Yıl boyu sıcak olan her bölgeyi savan sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='cg-iklim-ozellik',kaynak=KY),
 'K-IKL-02':dict(alt='Türkiye iklim grafiği',fikir='Aylık sıcaklık-yağış grafiğinden yağış rejimi ve sıcaklık farkı okunarak il merkezi belirlenir.',tuzak='Yalnız sıcaklığa bakıp yağış rejimini yok saymak.',zorluk='orta',kalip='grafik',adim=3,tipId='cg-iklim-grafik',kaynak=KY),
 'K-IKL-03':dict(alt='Muson iklimi',fikir='Mevsimlik rüzgârlar yazın denizden karaya, kışın karadan denize eser; yağış yazın yoğunlaşır.',tuzak='Muson yağışını yıl geneline dağıtmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='cg-iklim-muson',kaynak=KY),
 'K-IKL-04':dict(alt='Kıta ve deniz etkisi',fikir='Aynı enlem ve yükseltide denize yakın yerin yıllık sıcaklık farkı azdır, iç kesimin fazladır.',tuzak='Yazın aynı sıcaklığı görüp iki yerin aynı iklimde olduğunu sanmak.',zorluk='orta',kalip='tablo',adim=3,tipId='cg-iklim-kita',kaynak=KY),
 'K-IKL-05':dict(alt='Yarım küre ve iklim tipi',fikir='En sıcak ayın ocak olması ve yağışın haziran-ağustos aylarında toplanması Güney Yarım Küre kışını gösterir.',tuzak='Mevsimleri Kuzey Yarım Küre'+'’ye göre okumak.',zorluk='zor',kalip='grafik',adim=4,tipId='cg-iklim-yarimkure',kaynak=KY),
 'K-IKL-06':dict(alt='Dört istasyonun iklimi',fikir='Ocak-temmuz sıcaklık ve yağış değerlerinden dört istasyon farklı iklimlerle eşleştirilir.',tuzak='Yalnız sıcaklığa bakmak; yağış rejimini ihmal etmek.',zorluk='zor',kalip='tablo',adim=5,tipId='cg-iklim-dortlu',kaynak=KY),
}
TIPLER={'cg-iklim-ozellik':'İklim tipini özelliklerinden bulma','cg-iklim-grafik':'Türkiye iklim grafiği yorumu','cg-iklim-muson':'Muson iklimi özellikleri','cg-iklim-kita':'Kıta ve deniz etkisi karşılaştırması','cg-iklim-yarimkure':'Yarım küre ve iklim tipi (grafik)','cg-iklim-dortlu':'İstasyon–iklim eşleştirme (tablo)'}
Q=Konu('iklim','İklimler','cog|İklimler',6,KARTLAR,TIPLER,{'kolay':1,'orta':3,'zor':2})
B_GRF=B('Sıcaklık–yağış grafiği','çizgi: aylık sıcaklık (sol eksen, °C) · sütun: aylık yağış (sağ eksen, mm) · yıllık sıcaklık farkı = en sıcak ay − en soğuk ay (ör. 25 − 5 = 20 °C)')

# 0001 kolay · B
Q.soru('0001','K-IKL-01','kolay','Sıcaklık ve yağış özelliklerinden iklim tipini belirler.',2,'düz',
 'Yıllık ortalama sıcaklığı yüksek, yıllık sıcaklık farkı çok az olan, hemen her ay yağış alan ve yağışları çoğunlukla öğleden sonra sağanak biçiminde düşen bir bölgede aşağıdaki iklim tiplerinden hangisi görülür?',
 [('Savan iklimi','savan','Savan ikliminde yağışsız, kurak bir mevsim vardır. Burada her ay yağış alındığı için savan değildir.','bilgi'),
  ('Ekvatoral iklim','ekv','',''),
  ('Muson iklimi','muson','Muson ikliminde yağış yazın toplanır, kış kurak geçer; yağış yıla dengeli dağılmaz.','bilgi'),
  ('Akdeniz iklimi','akd','Akdeniz ikliminde yaz kurak, kış yağışlıdır ve yıllık sıcaklık farkı fazladır.','bilgi'),
  ('Çöl iklimi','col','Çöl ikliminde yağış çok azdır; sürekli yağış alan bir bölge çöl olamaz.','dikkat')],
 'B',lambda t:t=='ekv','Verilen özelliklere sahip iklim tipi.',
 'Yağışın yıl içindeki dağılışına bak: kurak bir mevsim var mı?',
 [B('Ekvatoral iklim','Ekvator çevresinde görülür · yıl boyu sıcak ve yağışlıdır · yıllık sıcaklık farkı çok azdır · yağışlar konveksiyonel (sağanak) biçimdedir · bitki örtüsü yağmur ormanıdır')],
 [A('Özellikleri ayır','Dört veri var: yüksek sıcaklık, çok az sıcaklık farkı, her ay yağış ve öğleden sonra sağanak.','sıcak + farksız + her ay yağışlı'),
  A('İklimleri sına','Savanda kurak mevsim, Akdeniz ve muson ikliminde yağışsız yaz ya da kış vardır. Çölde yağış zaten azdır.','savan, akdeniz, muson, çöl: uymuyor'),
  A('Sonucu bul','Yıl boyu sıcak ve yağışlı olan iklim ekvatoral iklimdir.','ekvatoral iklim')],
 'Kurak mevsim yoksa ve her ay yağış varsa önce ekvatoral iklimi düşün.')

# 0002 orta · D  (Karadeniz grafiği)
T2=[7,7,9,13,17,21,23,23,20,16,12,9]; P2=[200,170,150,120,100,130,110,140,210,300,280,240]
assert max(T2)-min(T2)==16 and min(P2)>=100 and sum(P2)==2150
def sinif_tr(il): return {'Antalya':'akdeniz','Konya':'step','Şanlıurfa':'güneydoğu','Rize':'karadeniz','Erzurum':'sert'}[il]
Q.soru('0002','K-IKL-02','orta','Aylık sıcaklık–yağış grafiğinden Türkiye’deki il merkezini belirler.',3,'grafik',
 'Türkiye’deki bir il merkezinin aylık sıcaklık ve yağış değerleri grafikte gösterilmiştir.\nGrafikteki verilere göre bu il merkezi aşağıdakilerden hangisi olabilir?',
 [('Antalya','akdeniz','Antalya’da yaz ayları kurak geçer; grafikte haziran-ağustos arası 100 mm’nin üzerinde yağış var.','bilgi'),
  ('Konya','step','Konya’da yıllık yağış yaklaşık 300–400 mm’dir; grafikteki yıllık toplam 2150 mm’dir.','bilgi'),
  ('Şanlıurfa','güneydoğu','Şanlıurfa’da yaz sıcaklığı 30 °C’yi aşar ve yaz kuraktır; grafikte temmuz 23 °C’dir ve yağışlıdır.','bilgi'),
  ('Rize','karadeniz','',''),
  ('Erzurum','sert','Erzurum’da kış çok soğuktur (ocak ayı sıfırın çok altındadır); grafikte ocak 7 °C’dir.','dikkat')],
 'D',lambda t:t=='karadeniz','Grafikteki il merkezi.',
 'Yağışsız ya da az yağışlı bir ay var mı? Yıllık sıcaklık farkı büyük mü?',
 [B_GRF,B('Karadeniz kıyısı iklimi','her mevsim yağışlı, yağış çok bol · deniz etkisiyle yıllık sıcaklık farkı az · Rize, Trabzon, Giresun')],
 [A('Grafiği oku','Sıcaklık ocakta 7, temmuzda 23 °C. Her ay en az 100 mm yağış düşüyor.','fark: 23 − 7 = 16 °C · en az yağış: 100 mm'),
  A('Yıllık toplamı bul','Aylık yağışlar toplanır; çok bol bir yağış söz konusu.','200 + 170 + … + 240 = 2150 mm'),
  A('İlleri ele','Antalya yazın kurak, Konya ve Şanlıurfa az yağışlı, Erzurum kışın çok soğuktur. Hiçbiri grafikle uyuşmaz.','Antalya, Konya, Şanlıurfa, Erzurum: yanlış'),
  A('Sonucu bul','Yıl boyu bol yağış ve az sıcaklık farkı Karadeniz kıyısını gösterir.','Rize')],
 'Yağışsız ay yoksa ve yıllık yağış çok yüksekse Karadeniz kıyısını düşün.',sekil=klimograf(T2,P2,30,10,300,100))

# 0003 orta · A (muson öncüllü)
Q.oncul('0003','K-IKL-03','orta','Muson ikliminin özelliklerini ayırt eder.',3,
 'Güney ve Güneydoğu Asya’nın önemli bölümünde muson ikliminin etkisi görülür.',
 [('Yağışlar yılın bütün aylarına dengeli biçimde dağılır.',False,'Muson ikliminde yağış yaz aylarında yoğunlaşır, kışlar kuraktır.'),
  ('Yazın denizden karaya esen nemli rüzgârlar bol yağış getirir.',True,'Yazın ısınan karaya doğru deniz üzerindeki nemli hava gelir ve yağış bırakır.'),
  ('Kışın rüzgârlar karadan denize doğru eserek kuru bir mevsim oluşturur.',True,'Kışın rüzgâr karadan denize eser; kuru hava kış mevsimini kurak geçirir.')],
 'Yukarıdaki ifadelerden hangileri muson iklimi için doğrudur?',
 ['II ve III','Yalnız I','Yalnız II','I ve III','I, II ve III'],'A',True,'Muson ikliminin doğru özellikleri.',
 'Muson, mevsimlere göre yönü değişen rüzgârlarla ilgilidir; yazın ve kışın rüzgâr yönünü düşün.',
 [B('Muson iklimi','rüzgârlar mevsimlik yön değiştirir · yaz: denizden karaya, nemli, bol yağış · kış: karadan denize, kuru · Hindistan, Bangladeş, Güneydoğu Asya')],
 [A('Rüzgâr yönünü hatırla','Yazın kara daha çok ısınır, alçak basınç oluşur ve rüzgâr denizden karaya eser.','yaz: deniz → kara · kış: kara → deniz'),
  A('Yağışı yorumla','Denizden gelen nemli hava yazın yağış bırakır, kış kuraktır. Yağış yıla eşit dağılmaz.','I: yanlış · II: doğru · III: doğru'),
  A('Sonuç','Doğru ifadeler II ve III.','II ve III')],
 'Muson denince “yaz yağışlı, kış kurak ve rüzgâr yönü mevsimlik” üçlüsünü hatırla.')

# 0004 orta · E (kıta-deniz)
D4={'K':(9,25),'L':(-6,25)}
fk=D4['K'][1]-D4['K'][0]; fl=D4['L'][1]-D4['L'][0]; assert (fk,fl)==(16,31)
Q.soru('0004','K-IKL-04','orta','Aynı enlemdeki iki yerin sıcaklık farkından kıta ve deniz etkisini yorumlar.',3,'tablo',
 'K ve L şehirleri aynı enlemde ve deniz seviyesindedir. Şehirlerin ocak ve temmuz ayı ortalama sıcaklıkları aşağıda verilmiştir.\nK şehri: Ocak 9 °C, Temmuz 25 °C\nL şehri: Ocak −6 °C, Temmuz 25 °C\nBu verilere göre aşağıdakilerden hangisi söylenebilir?',
 [('L’de en sıcak ay ile en soğuk ay arasındaki fark, K’dekinden azdır.',D4['L'][1]-D4['L'][0]<fk,'L’de fark 31 °C, K’de 16 °C’dir; ifade tersine kurulmuştur.','islem'),
  ('K’nin iç kesimde, L’nin kıyıda yer aldığı söylenebilir.',False,'Yıllık sıcaklık farkı az olan K deniz etkisindedir; farkı çok olan L iç kesimdedir.','bilgi'),
  ('Temmuz ayında K şehri, L şehrinden daha sıcaktır.',D4['K'][1]>D4['L'][1],'Temmuzda iki şehrin sıcaklığı da 25 °C’dir; biri diğerinden sıcak değildir.','dikkat'),
  ('Ocak ayında L şehri, K şehrinden daha sıcaktır.',D4['L'][0]>D4['K'][0],'Ocakta L −6 °C, K 9 °C’dir; kış sıcaklığı K’de daha yüksektir.','dikkat'),
  ('K şehrinde yıllık sıcaklık farkı L şehrine göre azdır; bu durum deniz etkisiyle açıklanabilir.',fk<fl,'','')],
 'E',lambda t:t is True,'Verilere göre söylenebilecek yargı.',
 'Her şehrin en sıcak ayı ile en soğuk ayı arasındaki farkı hesapla.',
 [B('Yıllık sıcaklık farkı','en sıcak ay ortalaması − en soğuk ay ortalaması (ör. 24 − 4 = 20 °C)'),B('Deniz ve kara','deniz geç ısınır, geç soğur: kıyıda kış ılık, yaz serin, fark az · iç kesimde kış soğuk, yaz sıcak, fark çok')],
 [A('Farkları hesapla','Aynı enlemde ve yükseltide olduğundan fark yalnız deniz-kara etkisinden gelir.','Fark (K şehri): 25 − 9 = 16 °C · Fark (L şehri): 25 − (−6) = 31 °C'),
  A('Yorumla','Deniz etkisi sıcaklık farkını azaltır. K’nin farkı küçük, L’nin farkı büyüktür.','K: kıyı · L: iç kesim'),
  A('Şıkları sına','A, B, C ve D verilerle çelişir; yalnız E verilere uyar.','A, B, C, D: yanlış · E: doğru')],
 'Yıllık sıcaklık farkı küçükse deniz etkisini, büyükse kıta etkisini düşün.')

# 0005 zor · C
T5=[21,21,20,17,14,12,11,12,13,16,18,20]; P5=[15,15,20,45,80,95,90,85,45,30,20,15]
assert T5.index(max(T5)) in (0,1) and T5.index(min(T5))==6 and sum(P5[11:12]+P5[0:2])<=45 and min(P5[4:8])>=80
def yarim(T): return 'Güney' if T.index(max(T)) in (11,0,1) else 'Kuzey'
assert yarim(T5)=='Güney'
Q.soru('0005','K-IKL-05','zor','Aylık sıcaklık-yağış grafiğinden iklim tipini ve yarım küreyi birlikte belirler.',4,'grafik',
 'Bir istasyonda ölçülen aylık ortalama değerler grafikte gösterilmiştir.\nBu istasyonun iklim tipi ile bulunduğu yarım küre, aşağıdakilerden hangisinde birlikte doğru verilmiştir?',
 [('Akdeniz iklimi – Kuzey Yarım Küre',('akd','Kuzey'),'Yağış düzeni Akdeniz iklimine benzer ama en sıcak ay ocaktır; bu, istasyonun Güney Yarım Küre’de olduğunu gösterir.','dikkat'),
  ('Okyanusal iklim – Güney Yarım Küre',('okyanusal','Güney'),'Okyanusal iklimde yağış yıl boyu dengelidir. Grafikte yaz ayları (aralık–şubat) 20 mm’nin altında kurak geçer.','bilgi'),
  ('Akdeniz iklimi – Güney Yarım Küre',('akd','Güney'),'',''),
  ('Savan iklimi – Güney Yarım Küre',('savan','Güney'),'Savanda yağış sıcak mevsimde düşer. Grafikte yağış, sıcaklığın en düşük olduğu haziran-ağustos aylarında toplanmıştır.','bilgi'),
  ('Muson iklimi – Kuzey Yarım Küre',('muson','Kuzey'),'Muson ikliminde yağış yazın yoğunlaşır; burada yağışlar sıcaklığın düşük olduğu aylarda toplanmıştır.','bilgi')],
 'C',lambda t:t==('akd','Güney'),'Grafikteki istasyonun iklim tipi ve yarım küresi.',
 'En sıcak ay hangisi? Bu, hangi yarım kürede olduğunu söyler.',
 [B_GRF,B('Mevsimlerin zıtlığı','Kuzey Yarım Küre’de yaz haziran–ağustos, Güney Yarım Küre’de yaz aralık–şubattır · Akdeniz iklimi: yaz sıcak ve kurak, kış ılık ve yağışlı')],
 [A('En sıcak ayı bul','Sıcaklık çizgisi ocak-şubatta tepe yapıyor (21 °C), temmuzda en düşük (11 °C).','en sıcak: ocak · en soğuk: temmuz'),
  A('Yarım küreyi belirle','Ocak en sıcak ay ise yaz aralık–şubattır. Bu mevsim düzeni Güney Yarım Küre’ye aittir.','yaz: ocak çevresi → Güney Yarım Küre'),
  A('Yağış düzenini oku','Yaz (aralık–şubat) kurak, kış (mayıs–ağustos) yağışlıdır; yıllık fark azdır.','yaz: 15–20 mm · kış: 80–95 mm'),
  A('İklimi seç','Kurak yaz, yağışlı kış: Akdeniz iklimi. Yarım küre güney olduğundan sonuç budur.','Akdeniz iklimi – Güney Yarım Küre')],
 'Önce en sıcak ayın hangi yarım kürede yaz olduğunu belirle, sonra yağışı mevsime göre oku.',sekil=klimograf(T5,P5,30,10,100,25))

# 0006 zor · B (dört istasyon)
ST={'K':(-24,16,20,80),'L':(26,26,250,180),'M':(10,27,120,4),'N':(14,36,5,3)}
def sinif(tj,tt,pj,pt):
    if pj<15 and pt<15: return 'Çöl iklimi'
    if pj>100 and pt>100 and abs(tt-tj)<3: return 'Ekvatoral iklim'
    if pt<10 and pj>50 and tj>0: return 'Akdeniz iklimi'
    if tj<-10: return 'Karasal iklim'
    raise AssertionError
dog=tuple(sinif(*ST[k]) for k in 'KLMN'); assert dog==('Karasal iklim','Ekvatoral iklim','Akdeniz iklimi','Çöl iklimi')
OZ={'K':'Ocak −24 °C ile çok soğuk, temmuz 16 °C; yağış az: karasal iklim.','L':'Ocak ve temmuz sıcaklığı 26 °C (fark yok), her iki ay da bol yağış: ekvatoral iklim.','M':'Temmuzda yağış 4 mm (yaz kurak), ocakta 120 mm (kış yağışlı): Akdeniz iklimi.','N':'Her iki ayda da yağış 5 mm’nin altında ve yaz çok sıcak: çöl iklimi.'}
S,E,Ak,C=dog
perms=[(S,E,Ak,C),(Ak,E,S,C),(S,C,Ak,E),(S,E,C,Ak),(E,S,Ak,C)]
optm=[]
for p in perms:
    cel=''
    if p!=dog:
        yanlis=[k for k,a,b in zip('KLMN',p,dog) if a!=b]
        cel=' '.join(f'{k} istasyonu {p["KLMN".index(k)].replace(" iklimi","").replace(" iklim","")} sayılmış; oysa {OZ[k][0].lower()+OZ[k][1:]}' for k in yanlis)
    optm.append((' · '.join(f'{k}: {v}' for k,v in zip('KLMN',p)),p,cel,'bilgi'))
# doğru şık B olsun: sırayı ayarla
optm=[optm[1],optm[0],optm[2],optm[3],optm[4]]
Q.soru('0006','K-IKL-06','zor','Dört istasyonun ocak-temmuz sıcaklık ve yağış verilerinden iklim tiplerini eşleştirir.',5,'tablo',
 'Aşağıdaki tabloda dört istasyonun ocak ve temmuz ayı ortalama sıcaklık ve yağış değerleri verilmiştir.\nİstasyon | Ocak (°C) | Temmuz (°C) | Ocak (mm) | Temmuz (mm)\n'+'\n'.join(f'{k} | {v[0].__str__().replace("-","−")} | {v[1]} | {v[2]} | {v[3]}' for k,v in ST.items())+'\nBu istasyonların iklim tipleri sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
 optm,'B',lambda t:t==dog,'K, L, M ve N istasyonlarının iklim tipleri.',
 'Önce yağışı hiç olmayan ve sıcaklığı hiç değişmeyen istasyonları ayır.',
 [B('İklim ipuçları','ekvatoral: her ay sıcak ve yağışlı · Akdeniz: yaz kurak, kış yağışlı · karasal: kış çok soğuk, yaz serin, yağış az · çöl: yıl boyu çok az yağış')],
 [A('Yağışı çok az olanı ayır','N istasyonunda iki ayda da yağış 5 mm’nin altında; yaz çok sıcak.','N: 5 ve 3 mm → çöl iklimi'),
  A('Sıcaklık farkı olmayanı bul','L’de ocak ve temmuz 26 °C, iki ay da bol yağışlı.','L: ekvatoral iklim'),
  A('Yaz kuraklığını ara','M’de temmuz yağışı 4 mm, ocak yağışı 120 mm; kış ılık (10 °C).','M: Akdeniz iklimi'),
  A('Kalanı çöz','K’de ocak −24 °C: kış çok soğuk, yağış az.','K: karasal iklim'),
  A('Şıkla karşılaştır','Sıra K, L, M, N için karasal, ekvatoral, Akdeniz, çöl olmalı.','Karasal, Ekvatoral, Akdeniz, Çöl')],
 'Tablodaki en belirgin (en uç) değerden başla ve elemeyle ilerle.')
Q.bitir()
