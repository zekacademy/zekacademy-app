"""TYT Türkçe · Cümle Türleri: 4 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (cümle türleri) ve MEB Türk Dili ve Edebiyatı müfredatı'
KARTLAR={
 'K-CT-01':dict(alt='Yapısına Göre Cümleler',fikir='Cümlenin basit, birleşik, sıralı ya da bağlı olduğunu yargı ve yüklem sayısına göre belirlemek.',tuzak='Fiilimsi içeren cümleyi basit sanmak; virgüllü cümleyi hep sıralı saymak.',zorluk='kolay',kalip='düz',adim=2,tipId='cum-yapi',kaynak=KY),
 'K-CT-02':dict(alt='Yüklemin Türüne Göre Cümleler',fikir='Yüklemi isim soylu sözcük olan cümleyi (isim cümlesi), fiil olan cümleden ayırmak.',tuzak='Yüklemdeki ek fiili görmemek.',zorluk='orta',kalip='düz',adim=3,tipId='cum-yuklem',kaynak=KY),
 'K-CT-03':dict(alt='Anlamına Göre Cümleler',fikir='Yüklemin olumlu ya da olumsuz olduğuna göre cümlenin anlamını belirlemek.',tuzak='Fiilimsideki olumsuzluğu yüklemin olumsuzluğu sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='cum-anlam',kaynak=KY),
 'K-CT-04':dict(alt='Yapı ve Yüklemin Yeri',fikir='Cümlenin hem yapısını hem yüklemin yerini birlikte değerlendirmek.',tuzak='Devrik cümleyi yalnız yapıdan ayırmaya çalışmak.',zorluk='zor',kalip='düz',adim=4,tipId='cum-yer',kaynak=KY),
}
TIPLER={'cum-yapi':'Yapısına göre cümleler','cum-yuklem':'Yüklemin türüne göre cümleler','cum-anlam':'Anlamına göre cümleler','cum-yer':'Yapı ve yüklemin yeri'}
Q=kur('cumleturleri','Cümle Türleri','tr|Cümle Türleri',KARTLAR,TIPLER); Q.n=4
B_YP=B('Yapısına göre cümleler','basit: tek yargı, tek yüklem (Çocuk top oynadı) · birleşik: fiilimsi ya da yan cümle içerir (Yağmur durunca çıktık) · sıralı: bağımsız birden çok yargı (Ali gitti, Ayşe döndü)')
B_YK=B('Yüklemin türüne göre','fiil cümlesi: yüklem fiildir (Annem geldi) · isim cümlesi: yüklem isim soyludur, ek fiil alır (Mahalle sakindir)')
B_AN=B('Olumlu / olumsuz cümle','cümlenin türü yüklemine göre belirlenir. Fiilimsideki olumsuzluk cümleyi olumsuz yapmaz: “Çalışmadan girdi” olumludur, yüklem girdi olumludur')
B_YR=B('Yüklemin yeri','kurallı cümle: yüklem sonda (Eve döndük) · devrik cümle: yüklem sonda değil (Döndük eve)')

# 0001 yapı · kolay · C
soru(Q,'0001','K-CT-01','kolay','Cümleyi yapısına göre basit, birleşik ve sıralı olarak ayırt eder.',2,
 'Aşağıdaki cümlelerin hangisi yapısı bakımından basit cümledir?',
 [('Yağmur durunca yola çıktık.','birleşik','“Durunca” zarf-fiil içerir; ikinci bir yargı bulunduğu için birleşik cümledir.','bilgi'),
  ('Ali okula gitti, Ayşe eve döndü.','sıralı','İki bağımsız yargı vardır; sıralı cümledir.','bilgi'),
  ('Çocuk bahçede top oynadı.','basit','',''),
  ('Sınavı kazanan öğrenci ödül aldı.','birleşik','“Kazanan” sıfat-fiildir; fiilimsi içerdiği için birleşik cümledir.','dikkat'),
  ('Hava güzel olduğu için pikniğe gittik.','birleşik','“Olduğu için” yan yargı oluşturur; birleşik cümledir.','bilgi')],
 'C',lambda t:t=='basit','Yapısı bakımından basit olan cümle.',
 'Cümlede yüklem dışında fiilimsi ya da ikinci bir yargı var mı?',[B_YP],
 [AD('Basit cümleyi hatırla','Basit cümlede tek yargı ve tek yüklem vardır; fiilimsi içermez.','basit: tek yargı'),AD('Şıkları çözümle','A durunca, D kazanan, E olduğu için: fiilimsi ya da yan yargı var. B’de iki bağımsız yargı var.','A, D, E: birleşik · B: sıralı'),AD('Basit olanı seç','C’de yalnız “oynadı” yüklemi var; fiilimsi yok.','C: basit')],
 'Yüklem dışında fiilimsi ya da yan yargı görürsen cümle basit değildir.')

# 0002 yüklem türü · orta · A
soru(Q,'0002','K-CT-02','orta','Yüklemi isim soylu olan cümleyi (isim cümlesini) belirler.',3,
 'Aşağıdaki cümlelerden hangisi yüklemin türüne göre isim cümlesidir?',
 [('Bu mahalle çok sakindir.','isim','',''),
  ('Çocuklar parkta oynuyor.','fiil','“Oynuyor” fiildir; yüklem fiil olduğu için fiil cümlesidir.','bilgi'),
  ('Misafirler akşam geldi.','fiil','“Geldi” fiildir; fiil cümlesidir.','bilgi'),
  ('Yarın erken kalkacağız.','fiil','“Kalkacağız” fiildir; fiil cümlesidir.','dikkat'),
  ('Annem pencereyi açtı.','fiil','“Açtı” fiildir; fiil cümlesidir.','dikkat')],
 'A',lambda t:t=='isim','İsim cümlesi olan seçenek.',
 'Yüklemin kökü fiil mi, yoksa isim soylu bir sözcük mü?',[B_YK],
 [AD('Ölçütü hatırla','Yüklemi fiil olan cümle fiil cümlesi, isim soylu sözcük olan cümle isim cümlesidir.','yüklem fiil → fiil cümlesi'),AD('Yükleme bak','oynuyor, geldi, kalkacağız, açtı: dört yüklem de fiildir.','B, C, D, E: fiil cümlesi'),AD('İsim cümlesini seç','“Sakindir” sıfat kökü + -dir ek fiil: yüklem isim soyludur.','A: isim cümlesi')],
 'Önce cümlenin yüklemini bul, sonra kökünün fiil mi isim mi olduğuna bak.')

# 0003 anlam · orta · E
soru(Q,'0003','K-CT-03','orta','Yüklemi olumsuz olan cümleyi belirler.',3,
 'Aşağıdaki cümlelerden hangisinin yüklemi olumsuzdur?',
 [('Ders çalışmadan sınava girdi.','olumlu','Yüklem “girdi”dir ve olumludur; “çalışmadan” zarf-fiildir, cümleyi olumsuz yapmaz.','dikkat'),
  ('Gelmeyen arkadaşlarımızı bekledik.','olumlu','Yüklem “bekledik”tir ve olumludur; “gelmeyen” sıfat-fiildir.','dikkat'),
  ('Okumak için kitap aldı.','olumlu','Yüklem “aldı”dır ve olumludur; olumsuzluk eki yoktur.','bilgi'),
  ('Yağmur dinmeden yola çıktık.','olumlu','Yüklem “çıktık”tır ve olumludur; “dinmeden” zarf-fiildir.','dikkat'),
  ('Bu akşam hiç kimseyi görmedim.','olumsuz','','')],
 'E',lambda t:t=='olumsuz','Yüklemi olumsuz olan cümle.',
 'Olumsuzluk ekini (-ma/-me) yüklemde mi, yoksa fiilimside mi bulduğuna bak.',[B_AN],
 [AD('Yüklemi bul','Her cümlede yüklem sondaki fiildir: girdi, bekledik, aldı, çıktık, görmedim.','5 yüklem'),AD('Olumsuzluk eki ara','“Çalışmadan”, “gelmeyen”, “dinmeden” fiilimsilerdir; yüklem değildir. Yüklemler olumludur.','A, B, C, D: olumlu'),AD('Olumsuz yüklemi seç','“Görmedim”: gör- + -me (olumsuzluk) + -di + -m. Yüklem olumsuzdur.','E: olumsuz')],
 'Cümlenin olumlu ya da olumsuz oluşunu yalnız yükleme bakarak belirle.')

# 0004 yapı ve yer · zor · B
soru(Q,'0004','K-CT-04','zor','Cümlenin yapısını ve yüklemin yerini birlikte değerlendirir.',4,
 'Aşağıdaki cümlelerin hangisi yapısı bakımından birleşik, yüklemin yeri bakımından devrik cümledir?',
 [('Yağmur başlayınca eve döndük.',('birleşik','kurallı'),'Birleşik cümledir ama yüklem sonda; kurallıdır, devrik değildir.','dikkat'),
  ('Eve döndük akşam olunca.',('birleşik','devrik'),'',''),
  ('Hava soğuk, yollar buzluydu.',('sıralı','kurallı'),'İki bağımsız yargı: sıralı. Yüklem sonda: kurallı. Birleşik de devrik de değildir.','bilgi'),
  ('Çocuk sessizce odasına çekildi.',('basit','kurallı'),'Basit ve kurallı bir cümledir.','bilgi'),
  ('Gittiler sabah erkenden.',('basit','devrik'),'Yüklem sonda değil: devrik. Ama fiilimsi ya da yan yargı yok, cümle basittir.','dikkat')],
 'B',lambda t:t==('birleşik','devrik'),'Birleşik ve devrik olan cümle.',
 'Önce her cümlenin yüklemini bul ve sonda olup olmadığına bak; sonra yapıyı belirle.',[B_YP,B_YR],
 [AD('İki ölçütü yaz','Aranan cümle hem birleşik (fiilimsi ya da yan yargı var) hem devrik (yüklem sonda değil) olmalı.','birleşik + devrik'),AD('Her şıkkı çöz','A birleşik ama kurallı. C sıralı. D basit ve kurallı. E devrik ama basit.','A, C, D, E: koşul tamam değil'),AD('Doğrula','“Döndük” yüklemdir, sonda değil (devrik). “Olunca” zarf-fiil içerir (birleşik).','B: birleşik + devrik')],
 'İki ölçütlü sorularda şıkları iki sütunda (yapı, yer) etiketleyip ikisini birden sağlayanı seç.')
bitir(Q)
