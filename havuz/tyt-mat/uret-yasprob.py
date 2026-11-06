"""Yaş Problemleri · iskelet havuz (8 ana + 8 kardeş). Her cevap ve ara sonuç kodla doğrulanır."""
import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
TT=lambda **k:k
KONU='Yaş Problemleri'; UK='prob|Yaş Problemleri'
P=Parti('yasprob',KONU,UK)

KARTLAR=[
 dict(id='K-YAS-01',konu=KONU,alt='Kat ilişkisi',fikir='Bugünkü yaşlar arasında bir kat ilişkisi, geçmişte ya da gelecekte başka bir kat ilişkisi verilir; iki yaşa da aynı yıl eklenip çıkarılarak denklem kurulur.',
      tuzak='Yıl kaydırırken yalnızca bir kişinin yaşını değiştirmek; birden çok çocuğun toplamında yılı kişi sayısıyla çarpmayı unutmak; istenen kişiyi ya da yılı karıştırmak.',zorluk='kolay-orta',kalip='hikâyeli',adim=3,tipId='yas-kat',tip='Yaşlar arasında kat ilişkisi',
      kaynak='ÖSYM YKS çıkmış (kitap s167, günlük yazısı ve 3 katı yaş) · Bilgi Sarmal s232 #10 · 3D s157 #9'),
 dict(id='K-YAS-02',konu=KONU,alt='Sabit yaş farkı',fikir='“Ben senin yaşındayken…”, “sen benim yaşıma geldiğinde…” cümleleri yaş farkı kadar geri ya da ileri gitmektir; yaş farkı hiç değişmez.',
      tuzak='Yaş farkının zamanla arttığını sanmak; iki yaşın ortalamasını ya da farkını yaş sanmak; iki kişinin toplamını bir kez artırmak.',zorluk='orta-zor',kalip='hikâyeli',adim=4,tipId='yas-fark',tip='Sabit yaş farkı (“ben senin yaşındayken”)',
      kaynak='ÖSYM YKS çıkmış (kitap s179, anne–çocuk tablo konuşması) · Bilgi Sarmal s232 #14–16 · 345 Deneme s118 #18'),
 dict(id='K-YAS-03',konu=KONU,alt='Toplam yaşın değişimi',fikir='n kişilik bir grubun yaşları toplamı t yılda n × t değişir; geçmişe gidilirken o tarihte doğmamış kişiler ayrıca düşünülür.',
      tuzak='Toplamı yalnızca t kadar değiştirmek; doğmamış çocuğu negatif yaşla saymak.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='yas-toplam',tip='Yaşlar toplamının zamanla değişimi',
      kaynak='Bilgi Sarmal s232 #10, s233 #2 · ÖSYM YKS çıkmış (kitap s90 #110, arkadaşlar ve çocukları)'),
 dict(id='K-YAS-04',konu=KONU,alt='Yıl ve yaş',fikir='Takvim yılları, doğum ya da yapım yılları ile yaşlar birlikte verilir; yaş = yıl − doğum yılı ilişkisiyle bilinmeyen yıl bulunur.',
      tuzak='Yaşı farklı bir yıla göre hesaplamak; doğum yılı ile yaşı karıştırmak; iki farkı karıştırmak.',zorluk='orta-zor',kalip='hikâyeli',adim=4,tipId='yas-yil',tip='Takvim yılı ile yaş',
      kaynak='ÖSYM YKS çıkmış (kitap s118 #141, tarihi ağaç · s122 #143, vazo · s150 #174, restoran) · Bilgi Sarmal s234 #9–10'),
 dict(id='K-YAS-05',konu=KONU,alt='Yaş ortalaması',fikir='Bir grubun yaş ortalaması verilir; gruba katılan ya da ayrılan kişilerden sonra yeni ortalama verilip kişilerin yaşları istenir.',
      tuzak='Ortalamayı toplam sanmak; ortalamadaki değişimi doğrudan yaşa eklemek; yeni kişi sayısını yanlış almak.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='yas-ortalama',tip='Yaş ortalaması',
      kaynak='ÖSYM YKS çıkmış (kitap s90 #110 · s230 #259) · Bilgi Sarmal s190 #13, s200 #8 · 3D s156 #3'),
]
TIPLER=[dict(tipId=k['tipId'],ad=k['tip'],kartlar=[k['id']],uygulamaKonu=UK) for k in KARTLAR]
json.dump(dict(konu=KONU,surum=1,kartlar=KARTLAR,tipler=TIPLER),open(os.path.join(H,'..','kartlar','yasprob.json'),'w'),ensure_ascii=False,indent=1)
T={k['tipId']:k['tip'] for k in KARTLAR}

KAT=B('“Katı” denklemi','“A’nın yaşı B’nin yaşının 3 katı” ⇒ A = 3 × B. Yıl kaydırınca iki kişinin yaşına da aynı sayı eklenir ya da çıkarılır')
FARK=B('Yaş farkı değişmez','iki kişinin yaş farkı her zaman aynıdır. Örnek: anne 30, kızı 6 ise 10 yıl sonra 40 ve 16; fark yine 24')
TOP=B('Zamanla toplam yaş','n kişinin her biri t yıl büyürse yaşları toplamı n × t artar. Örnek: 3 kişi 5 yıl sonra toplam 15 yaş büyür')
ORT=B('Aritmetik ortalama','ortalama = yaşlar toplamı ÷ kişi sayısı ⇒ toplam = ortalama × kişi sayısı. Örnek: 4 kişinin ortalaması 20 ise toplam 80')
YIL=B('Yıl ve yaş','yaş = içinde bulunulan yıl − doğum (yapım) yılı. Örnek: 2010’da doğan biri 2026’da 16 yaşındadır')

# ===== 0001 kat KOLAY
c=[e for e in range(1,60) if 4*e+6==3*(e+6)]; assert c==[12] and 4*12==48 and 48-12==36 and 48+6==54
c2=[e for e in range(1,60) if 4*e==3*(e+6)]; assert c2==[18] and 4*18==72
P.R('0001','yas-kat',T['yas-kat'],'kolay','Gelecekte kat','Bugünkü ve gelecekteki kat ilişkilerinden yaşları bulur.','hikâyeli',2,
 'K-YAS-01 (bugün ve gelecekte kat ilişkisi) · yeni kurgu (anne–kız), gelecek 6 yıl',
 'Bugün Ece’nin annesinin yaşı, Ece’nin yaşının 4 katıdır.\n6 yıl sonra annesinin yaşı, Ece’nin o zamanki yaşının 3 katı olacaktır.\nBuna göre Ece’nin annesi bugün kaç yaşındadır?',
 ['12','36','48','54','72'],'C','Annenin bugünkü yaşı.',
 ['Ece’nin bugünkü yaşına e de; annenin yaşı ne olur?','6 yıl sonra ikisinin de yaşına 6 ekle.','Denklemi çöz; soru kimin yaşını soruyor?'],[KAT],
 [A('Bugünkü yaşlar','Ece e, annesi 4e yaşında.','Ece: e · anne: 4e'),
  A('6 yıl sonra','İkisi de 6 yaş büyür.','4e + 6 = 3 × (e + 6) = 3e + 18 ⇒ e = 12'),
  A('Annenin yaşı','Bugünkü yaş 4e.','4 × 12 = 48 · kontrol: 54 = 3 × 18 ✓')],
 'Yıl kaydırırken iki kişinin yaşına da aynı sayıyı ekle; sonra sorunun kimi sorduğunu kontrol et.',
 dict(A='12, Ece’nin bugünkü yaşı; soru annesini soruyor.',B='36, anne ile Ece arasındaki yaş farkı.',D='54, annenin 6 yıl sonraki yaşı.',E='72, annenin yaşına 6 eklemeyi unutmak (4e = 3 × (e + 6) ⇒ e = 18).'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='islem'))
c=[t for t in range(6,40) if 7*t-5==12*(t-5)]; assert c==[11] and 7*11==77 and 77-11==66 and 77-5==72
c2=[t for t in range(6,40) if 7*t==12*(t-5)]; assert c2==[12] and 7*12==84
P.K('0001','Bir dedenin bugünkü yaşı, torununun bugünkü yaşının 7 katıdır.\n5 yıl önce dedenin yaşı, torununun o zamanki yaşının 12 katıydı.\nBuna göre dede bugün kaç yaşındadır?',
 ['11','66','72','77','84'],'D','Dedenin bugünkü yaşı.',
 ['Torunun bugünkü yaşına t de; dede kaç yaşında?','5 yıl önce ikisinin de yaşından 5 çıkar.','Bulduğun t değerini dedenin yaşına çevir.'],[KAT],
 [A('Bugünkü yaşlar','Torun t, dede 7t.','torun: t · dede: 7t'),
  A('5 yıl önce','İkisinden de 5 çıkar.','7t − 5 = 12 × (t − 5) = 12t − 60 ⇒ 5t = 55 ⇒ t = 11'),
  A('Dedenin yaşı','Bugün 7t.','7 × 11 = 77 · kontrol: 72 = 12 × 6 ✓')],
 'Geçmişe gidince her iki yaştan da aynı yıl çıkarılır; denklem bunu iki tarafta da göstermeli.',
 dict(A='11, torunun bugünkü yaşı.',B='66, dede ile torun arasındaki yaş farkı.',C='72, dedenin 5 yıl önceki yaşı.',E='84, dedenin yaşından 5 çıkarmayı unutmak (7t = 12 × (t − 5) ⇒ t = 12).'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='islem'))

# ===== 0002 toplam KOLAY
assert 104-4*6==80 and 104-6==98 and 104-12==92 and 104-18==86 and 104+24==128 and 7>=6
P.R('0002','yas-toplam',T['yas-toplam'],'kolay','Geçmişte toplam yaş','Bir grubun yaşları toplamının geçmişteki değerini kişi sayısıyla yılı çarparak bulur.','hikâyeli',2,
 'K-YAS-03 (toplam yaşın değişimi) · yeni kurgu (dört kişilik aile), geçmişe gidiş',
 'Anne, baba ve iki çocuktan oluşan dört kişilik bir ailenin bugünkü yaşları toplamı 104’tür.\nAilenin en küçük üyesi 7 yaşındadır.\nBuna göre 6 yıl önce bu ailedeki dört kişinin yaşları toplamı kaçtı?',
 ['80','86','92','98','128'],'A','6 yıl önceki toplam yaş.',
 ['6 yıl önce her bir aile üyesi kaç yaş küçüktü?','Ailede kaç kişi var?','En küçük üye 6 yıl önce doğmuş muydu?'],[TOP],
 [A('Herkes doğmuş mu?','En küçük üye 7 yaşında; 6 yıl önce o da doğmuştu.','4 kişi de sayılır'),
  A('Toplam azalma','4 kişinin her biri 6 yaş küçüktü.','4 × 6 = 24'),
  A('Sonuç','Bugünkü toplamdan çıkar.','104 − 24 = 80')],
 't yıl geçmişe gidince toplam yaş, kişi sayısı × t kadar azalır.',
 dict(B='86, yalnızca 3 kişinin yaşından 6 çıkarmak.',C='92, yalnızca 2 kişinin yaşından 6 çıkarmak.',D='98, toplamdan yalnızca 6 çıkarmak; her kişi ayrı ayrı 6 yaş küçüktü.',E='128, 6 yıl önce yerine 6 yıl sonrayı hesaplamak.'),
 TT(B='islem',C='islem',D='bilgi',E='dikkat'))
assert 96-4*5-3==73 and 96-25==71 and 96-20==76 and 96-5==91 and 96+25==121
P.K('0002','Anne, baba ve üç çocuktan oluşan bir ailenin bugünkü yaşları toplamı 96’dır.\nAilenin en küçük çocuğu 3 yaşında, diğer iki çocuğu ise 5 yaşından büyüktür.\nBuna göre 5 yıl önce, o tarihte doğmuş olan aile üyelerinin yaşları toplamı kaçtı?',
 ['71','73','76','91','121'],'B','5 yıl önce doğmuş olanların yaşları toplamı.',
 ['5 yıl önce ailenin hangi üyesi henüz doğmamıştı?','Doğmuş olan her üye 5 yaş küçüktü.','Doğmamış çocuğun bugünkü yaşını toplamdan nasıl çıkarırsın?'],[TOP],
 [A('Doğmamış üye','En küçük çocuk 3 yaşında; 5 yıl önce yoktu. Onun yaşı toplamdan tamamen çıkar.','96 − 3 = 93 (4 kişi)'),
  A('Doğmuş olanlar','Kalan 4 kişi 5’er yaş küçüktü.','4 × 5 = 20'),
  A('Sonuç','Dört kişinin 5 yıl önceki toplamı.','93 − 20 = 73')],
 'Geçmişe giderken o tarihte doğmamış olanları ayrıca düşün; onlar −2, −3 gibi yaşla sayılmaz.',
 dict(A='71, en küçük çocuğu da 5 yaş küçültmek (96 − 25); o 5 yıl önce doğmamıştı.',C='76, en küçük çocuğun yaşını toplamdan çıkarmayı unutmak (96 − 20).',D='91, toplamdan yalnızca 5 çıkarmak.',E='121, 5 yıl sonrayı hesaplamak.'),
 TT(A='dikkat',C='islem',D='bilgi',E='dikkat'))

# ===== 0003 fark ORTA
c=[(m,e) for m in range(1,90) for e in range(1,m) if m+(m-e)==46 and e-(m-e)==10]; assert c==[(34,22)] and (46+10)//2==28 and 46-10==36
P.R('0003','yas-fark',T['yas-fark'],'orta','İki konuşma cümlesi','“Senin yaşındayken” ve “benim yaşıma geldiğinde” cümlelerini yaş farkı kadar geri ve ileri gitmek olarak yorumlar.','hikâyeli',3,
 'K-YAS-02 (sabit yaş farkı) · yeni kurgu (kardeşler), geçmiş ve gelecek birlikte',
 'Murat, kız kardeşi Elif’e şunları söylemiştir:\n• “Sen benim bugünkü yaşıma geldiğinde ben 46 yaşında olacağım.”\n• “Ben senin bugünkü yaşındayken sen 10 yaşındaydın.”\nBuna göre Murat bugün kaç yaşındadır?',
 ['12','22','28','34','36'],'D','Murat’ın bugünkü yaşı.',
 ['Yaş farkına d de. Elif, Murat’ın yaşına kaç yıl sonra gelir?','Murat, Elif’in bugünkü yaşında kaç yıl önceydi?','46 ile 10 arasında kaç tane d var?'],[FARK],
 [A('Farkı adlandır','Murat m, Elif e yaşında; fark d = m − e.','m = e + d'),
  A('İki zamanı yaz','d yıl sonra Murat 46, d yıl önce Elif 10.','m + d = 46 · e − d = 10'),
  A('Farkı bul','46’dan 10’a: m + d − (e − d) = (m − e) + 2d = 3d.','46 − 10 = 36 = 3d ⇒ d = 12'),
  A('Murat','m + d = 46.','m = 46 − 12 = 34 (Elif 22)')],
 '“Senin yaşındayken” = yaş farkı kadar geri, “benim yaşıma geldiğinde” = yaş farkı kadar ileri gitmektir.',
 dict(A='12, iki kardeş arasındaki yaş farkı.',B='22, Elif’in bugünkü yaşı.',C='28, iki kardeşin bugünkü yaşlarının ortalaması ((46 + 10) ÷ 2).',E='36, 46 ile 10’un farkı; bu fark yaş farkının 3 katıdır.'),
 TT(A='dikkat',B='dikkat',C='islem',E='bilgi'))
c=[(a,k) for a in range(1,99) for k in range(1,a) if k+(a-k)==a and a-k>0 and k-(a-k)==4 and a+(a-k)==76]; assert c==[(52,28)] and 52-28==24 and 72//2==36 and 80//2==40
P.K('0003','Bir anne, kızına şunları söylemiştir:\n• “Ben senin bugünkü yaşındayken sen 4 yaşındaydın.”\n• “Sen benim bugünkü yaşıma geldiğinde ben 76 yaşında olacağım.”\nBuna göre anne, kızını kaç yaşında doğurmuştur?',
 ['24','28','36','40','52'],'A','Annenin kızını doğurduğu yaş (yaş farkı).',
 ['Anne ile kızı arasındaki yaş farkına d de.','Bir cümle d yıl geriye, diğeri d yıl ileriye gidiyor.','4 ile 76 arasında kaç tane d var?'],[FARK],
 [A('Farkı adlandır','Anne a, kızı k; fark d = a − k. Annenin kızını doğurduğu yaş d’dir.','a = k + d'),
  A('İki zamanı yaz','d yıl önce kız 4, d yıl sonra anne 76.','k − d = 4 · a + d = 76'),
  A('Farkı bul','76 − 4 = (a − k) + 2d = 3d.','72 = 3d ⇒ d = 24'),
  A('Kontrol','Kız 28, anne 52.','28 − 24 = 4 ✓ · 52 + 24 = 76 ✓')],
 'İki konuşma cümlesi arasındaki zaman farkı üç yaş farkı eder; bu ilişki soruyu tek adımda çözer.',
 dict(B='28, kızın bugünkü yaşı.',C='36, 72’yi 2’ye bölmek; aradaki fark 3 yaş farkıdır.',D='40, 4 ile 76’nın ortalaması; bu, iki yaşın ortalamasıdır.',E='52, annenin bugünkü yaşı.'),
 TT(B='dikkat',C='islem',D='islem',E='dikkat'))

# ===== 0004 yıl ORTA
c=[(s,4*s) for s in range(11,80) if 4*s-10==9*(s-10)]; assert c==[(16,64)] and 2026-64==1962 and 2016-54==1962 and 2026-16==2010
assert 2016-64==1952 and 2026-54==1972 and 2010-64==1946
P.R('0004','yas-yil',T['yas-yil'],'orta','Eşyanın yapım yılı','İki farklı yıldaki kat ilişkisinden bir eşyanın yaşını ve yapıldığı yılı bulur.','hikâyeli',4,
 'K-YAS-04 (takvim yılı ile yaş) · yeni kurgu (duvar saati), iki yılda kat ilişkisi',
 'Selin, 2026 yılında dedesinden kalan bir duvar saatinin yapım yılını merak etmiş ve şunları hesaplamıştır:\n• 2026 yılında saatin yaşı, Selin’in yaşının 4 katıdır.\n• 2016 yılında saatin yaşı, Selin’in o yılki yaşının 9 katıydı.\nBuna göre bu duvar saati hangi yılda yapılmıştır?',
 ['1946','1952','1962','1972','2010'],'C','Saatin yapıldığı yıl.',
 ['2026’da Selin’in yaşına s de; saatin yaşı kaçtır?','2016, 2026’dan kaç yıl önce? İki yaştan da o kadar çıkar.','Saatin 2026’daki yaşını 2026’dan çıkar.'],[YIL,KAT],
 [A('2026’daki yaşlar','Selin s, saat 4s yaşında.','Selin: s · saat: 4s'),
  A('2016’ya git','10 yıl önce; ikisinden de 10 çıkar.','4s − 10 = 9 × (s − 10) = 9s − 90 ⇒ 5s = 80 ⇒ s = 16'),
  A('Saatin yaşı','2026’da 4s.','4 × 16 = 64'),
  A('Yapım yılı','Yıl − yaş.','2026 − 64 = 1962 · kontrol: 2016’da 54 = 9 × 6 ✓')],
 'Yapım ya da doğum yılını bulurken yaşı hangi yıla göre bulduysan o yıldan çıkar.',
 dict(A='1946, saatin yaşını (64) Selin’in doğum yılından (2010) çıkarmak.',B='1952, 2026’daki yaşı (64) 2016’dan çıkarmak; yaş ile yıl uyuşmuyor.',D='1972, 2016’daki yaşı (54) 2026’dan çıkarmak.',E='2010, Selin’in doğum yılı; soru saatin yapım yılını soruyor.'),
 TT(A='islem',B='dikkat',D='dikkat',E='dikkat'))
c=[(o,4*o) for o in range(1,80) if 4*o+10==3*(o+10)]; assert c==[(20,80)] and 2025-80==1945 and 2025-20==2005 and 2035-80==1955 and 2025-60==1965 and 2005-80==1925
P.K('0004','Bir köy okulunun bahçesinde, okul açılmadan önce dikilmiş bir çınar ağacı vardır.\n2025 yılında çınarın yaşı okulun yaşının 4 katıdır. 2035 yılında ise çınarın yaşı okulun yaşının 3 katı olacaktır.\nBuna göre çınar ağacı hangi yılda dikilmiştir?',
 ['1925','1945','1955','1965','2005'],'B','Çınarın dikildiği yıl.',
 ['2025’te okulun yaşına o de; çınarın yaşı kaçtır?','2035’e gidince iki yaşa da kaç eklenir?','Çınarın 2025’teki yaşını 2025’ten çıkar.'],[YIL,KAT],
 [A('2025’teki yaşlar','Okul o, çınar 4o yaşında.','okul: o · çınar: 4o'),
  A('2035’e git','10 yıl sonra; ikisine de 10 ekle.','4o + 10 = 3 × (o + 10) = 3o + 30 ⇒ o = 20'),
  A('Çınarın yaşı','2025’te 4o.','4 × 20 = 80'),
  A('Dikildiği yıl','Yıl − yaş.','2025 − 80 = 1945 · kontrol: 2035’te 90 = 3 × 30 ✓')],
 'Yaşı bulduğun yıl ile çıkarma yaptığın yıl aynı olmalı.',
 dict(A='1925, çınarın yaşını (80) okulun açıldığı yıldan (2005) çıkarmak.',C='1955, 2025’teki yaşı (80) 2035’ten çıkarmak.',D='1965, çınar ile okul arasındaki yaş farkını (60) çınarın yaşı sanmak.',E='2005, okulun açıldığı yıl.'),
 TT(A='islem',C='dikkat',D='dikkat',E='dikkat'))

# ===== 0005 ortalama ORTA
yeni=10*28-8*30; assert yeni==40; c=[(x,x-6) for x in range(1,60) if x+(x-6)==yeni]; assert c==[(23,17)] and 40//2==20
c2=[x for x in range(1,60) if x+(x-6)==56]; assert c2==[31]
P.R('0005','yas-ortalama',T['yas-ortalama'],'orta','Gruba katılanlar','Ortalamadan toplamlara geçip gruba katılanların yaşlarını bulur.','hikâyeli',3,
 'K-YAS-05 (yaş ortalaması) · yeni kurgu (koro), iki kişi katılıyor, yaş farkı verildi',
 'Bir korodaki 8 kişinin yaş ortalaması 30’dur.\nKoroya 2 yeni üye katıldıktan sonra korodaki tüm üyelerin yaş ortalaması 28 olmuştur.\nYeni üyelerden biri diğerinden 6 yaş büyük olduğuna göre büyük olan üye kaç yaşındadır?',
 ['17','20','23','31','40'],'C','Yeni üyelerden büyük olanın yaşı.',
 ['8 kişinin yaşları toplamı kaç?','10 kişinin yaşları toplamı kaç?','İki toplamın farkı yeni üyelerin yaşları toplamıdır.'],[ORT],
 [A('İlk toplam','Ortalama × kişi sayısı.','8 × 30 = 240'),
  A('Yeni toplam','Katılımdan sonra 10 kişi.','10 × 28 = 280'),
  A('Yeni üyeler','Farkları 6 olan iki yaşın toplamı 40.','280 − 240 = 40 · x + (x − 6) = 40 ⇒ x = 23')],
 'Ortalama sorularında önce toplamlara geç; toplamlar arasındaki fark katılan ya da ayrılanların toplamıdır.',
 dict(A='17, küçük olan yeni üyenin yaşı.',B='20, iki yeni üyenin yaş ortalaması.',D='31, yeni üyelerin yaş ortalamasını 28 sanmak (toplam 56).',E='40, iki yeni üyenin yaşları toplamı.'),
 TT(A='dikkat',B='dikkat',D='bilgi',E='dikkat'))
ay=6*35-5*32; assert ay==50 and 32+6*3==50 and 35+5*3==50 and 35+3==38 and 32+5*3==47
P.K('0005','Bir ofiste çalışan 6 kişinin yaş ortalaması 35’tir.\nBu çalışanlardan biri emekli olup ofisten ayrıldığında kalan çalışanların yaş ortalaması 32 olmuştur.\nBuna göre emekli olan çalışan kaç yaşındadır?',
 ['32','35','38','47','50'],'E','Ofisten ayrılan çalışanın yaşı.',
 ['6 kişinin yaşları toplamı kaç?','Ayrılıştan sonra kaç kişi kaldı ve toplamları kaç?','İki toplamın farkını bul.'],[ORT],
 [A('İlk toplam','6 çalışan.','6 × 35 = 210'),
  A('Kalanların toplamı','5 çalışan kaldı.','5 × 32 = 160'),
  A('Ayrılan çalışan','Toplamların farkı.','210 − 160 = 50')],
 'Ortalamadaki düşüşü doğrudan yaşa ekleme; toplamlar üzerinden git.',
 dict(A='32, kalan çalışanların yaş ortalaması.',B='35, ilk yaş ortalaması; ayrılanın yaşı değil.',C='38, ortalamadaki 3 yaşlık düşüşü 35’e eklemek; düşüş 5 kişiye yayılmıştı.',D='47, 32’ye 5 × 3 eklemek; 32’ye 6 × 3 ya da 35’e 5 × 3 eklenmeliydi.'),
 TT(A='dikkat',B='bilgi',C='islem',D='islem'))

# ===== 0006 kat (çok çocuk) ORTA
c=[s for s in range(1,100) if 3*s+6==2*(s+12)]; assert c==[18] and 3*18==54 and 54-18==36 and 54+6==60 and 18+12==30
P.R('0006','yas-kat',T['yas-kat'],'orta','Çocukların toplam yaşı','Bir kişinin yaşı ile birden çok kişinin yaşları toplamı arasındaki kat ilişkisini, toplamın kişi sayısı kadar arttığını gözeterek kurar.','hikâyeli',3,
 'K-YAS-01 (kat ilişkisi) · bir kişi ile iki kişinin toplamı, gelecek 6 yıl',
 'Bir babanın bugünkü yaşı, iki çocuğunun bugünkü yaşları toplamının 3 katıdır.\n6 yıl sonra babanın yaşı, iki çocuğunun o zamanki yaşları toplamının 2 katı olacaktır.\nBuna göre baba bugün kaç yaşındadır?',
 ['18','30','36','54','60'],'D','Babanın bugünkü yaşı.',
 ['Çocukların bugünkü yaşları toplamına s de.','6 yıl sonra iki çocuğun yaşları toplamı kaç artar?','Denklemi kur ve babanın yaşını bul.'],[KAT,TOP],
 [A('Bugün','Çocukların toplamı s, baba 3s.','baba: 3s'),
  A('6 yıl sonra','Baba 6 yaş büyür; iki çocuğun toplamı 2 × 6 = 12 artar.','3s + 6 = 2 × (s + 12)'),
  A('Çöz','3s + 6 = 2s + 24.','s = 18 ⇒ baba 3 × 18 = 54 · kontrol: 60 = 2 × 30 ✓')],
 'Bir toplamın içinde kaç kişi varsa, yıl kaydırınca toplam o kadar kez değişir.',
 dict(A='18, çocukların bugünkü yaşları toplamı.',B='30, çocukların 6 yıl sonraki yaşları toplamı.',C='36, baba ile çocukların yaşları toplamı arasındaki fark.',E='60, babanın 6 yıl sonraki yaşı.'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='dikkat'))
c=[s for s in range(15,100) if 2*s-5==7*(s-15)]; assert c==[20] and 2*20==40 and 40-5==35 and 40+5==45 and 20-15==5
P.K('0006','Bir annenin bugünkü yaşı, üç çocuğunun bugünkü yaşları toplamının 2 katıdır.\nEn küçük çocuk 6 yaşındadır. 5 yıl önce annenin yaşı, üç çocuğunun o zamanki yaşları toplamının 7 katıydı.\nBuna göre annenin 5 yıl sonraki yaşı kaç olacaktır?',
 ['5','20','35','40','45'],'E','Annenin 5 yıl sonraki yaşı.',
 ['Çocukların bugünkü toplam yaşına s de; anne kaç yaşında?','5 yıl önce üç çocuğun toplamı kaç azalır? Hepsi doğmuş muydu?','Annenin bugünkü yaşını bulduktan sonra istenen zamana git.'],[KAT,TOP],
 [A('Bugün','Çocukların toplamı s, anne 2s.','anne: 2s'),
  A('5 yıl önce','En küçük çocuk 6 yaşında; üçü de doğmuştu. Toplam 3 × 5 = 15 azalır.','2s − 5 = 7 × (s − 15)'),
  A('Çöz','2s − 5 = 7s − 105.','5s = 100 ⇒ s = 20 ⇒ anne 40'),
  A('5 yıl sonra','İstenen zaman.','40 + 5 = 45 · kontrol: 35 = 7 × 5 ✓')],
 'Geçmişe giderken çocukların o tarihte doğmuş olup olmadığını kontrol et; sonra istenen yıla git.',
 dict(A='5, çocukların 5 yıl önceki yaşları toplamı.',B='20, çocukların bugünkü yaşları toplamı.',C='35, annenin 5 yıl önceki yaşı.',D='40, annenin bugünkü yaşı; soru 5 yıl sonrasını soruyor.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='dikkat'))

# ===== 0007 fark ZOR
c=[(a,y) for a in range(1,99) for y in range(1,a) if a+y==56 and y-(a-y)==4]; assert c==[(36,20)]
a,y=36,20; d=a-y; assert d==16 and (a+d)+(y+d)==88 and 56+16==72 and 2*52==104 and a+d==52
P.R('0007','yas-fark',T['yas-fark'],'zor','Toplam ve yaş farkı','Yaşlar toplamı ile “senin yaşındayken” bilgisinden yaşları bulur; ileri bir zamandaki toplamı yaş farkı kadar ilerleyerek hesaplar.','hikâyeli',4,
 'K-YAS-02 (sabit yaş farkı) · toplam yaş verildi, istenen gelecekteki toplam',
 'Ayşe ile annesinin bugünkü yaşları toplamı 56’dır.\nAnnesi, Ayşe’nin bugünkü yaşındayken Ayşe 4 yaşındaydı.\nBuna göre Ayşe, annesinin bugünkü yaşına geldiğinde ikisinin yaşları toplamı kaç olur?',
 ['36','52','72','88','104'],'D','Ayşe annesinin bugünkü yaşına geldiğindeki yaşlar toplamı.',
 ['Yaş farkına d de; annesi Ayşe’nin yaşındayken kaç yıl önceydi?','O zaman Ayşe 4 yaşındaydı: Ayşe’nin yaşı d cinsinden ne olur?','Ayşe annesinin yaşına d yıl sonra gelir; o zaman ikisi de d yaş büyümüştür.'],[FARK,TOP],
 [A('Yaşları d ile yaz','d yıl önce Ayşe 4 yaşındaydı.','Ayşe: d + 4 · anne: 2d + 4'),
  A('Toplamı kullan','İki yaşın toplamı 56.','3d + 8 = 56 ⇒ d = 16'),
  A('Bugünkü yaşlar','Ayşe 20, annesi 36.','20 + 36 = 56 ✓'),
  A('Gelecek','Ayşe 36’ya 16 yıl sonra gelir; iki kişi 16’şar yaş büyür.','56 + 2 × 16 = 88 (36 ve 52)')],
 'İki kişinin toplam yaşı t yılda 2t artar; “benim yaşıma geldiğinde” t’nin yaş farkı olduğunu gösterir.',
 dict(A='36, annenin bugünkü yaşı; Ayşe’nin o zamanki yaşı.',B='52, annenin o zamanki yaşı; soru toplamı soruyor.',C='72, toplama 16’yı yalnızca bir kez eklemek; iki kişi de 16 yaş büyür.',E='104, annenin o zamanki yaşını iki kez almak; Ayşe o zaman 36 yaşında olur.'),
 TT(A='dikkat',B='dikkat',C='islem',E='islem'))
c=[(a,y) for a in range(1,99) for y in range(1,a) if a+y==64 and y-(a-y)==2]; assert c==[(42,22)]
a,y=42,22; d=a-y; assert d==20 and a+d==62 and a+2*d==82 and 2*a==84
P.K('0007','Bir baba ile oğlunun bugünkü yaşları toplamı 64’tür.\nBaba, oğlunun bugünkü yaşındayken oğlu 2 yaşındaydı.\nBuna göre oğul, babasının bugünkü yaşına geldiğinde babası kaç yaşında olur?',
 ['42','62','64','82','84'],'B','Oğul babasının bugünkü yaşına geldiğinde babanın yaşı.',
 ['Yaş farkına d de; oğlun bugünkü yaşını d ile yaz.','Babanın yaşını da d ile yaz ve toplamı kullan.','Oğul babasının yaşına kaç yıl sonra gelir?'],[FARK],
 [A('Yaşları d ile yaz','d yıl önce oğul 2 yaşındaydı.','oğul: d + 2 · baba: 2d + 2'),
  A('Toplamı kullan','Toplam 64.','3d + 4 = 64 ⇒ d = 20'),
  A('Bugünkü yaşlar','Oğul 22, baba 42.','22 + 42 = 64 ✓'),
  A('Gelecek','Oğul 42 olana kadar 20 yıl geçer; baba da 20 yaş büyür.','42 + 20 = 62')],
 'Yaş farkı değişmez: oğul babasının yaşına geldiğinde baba, kendi yaşına yaş farkını ekler.',
 dict(A='42, babanın bugünkü yaşı.',C='64, bugünkü yaşlar toplamı; soru gelecekteki bir yaşı soruyor.',D='82, yaş farkını iki kez eklemek (42 + 2 × 20).',E='84, babanın yaşını iki katına çıkarmak; yaş farkı sabittir, yaşlar katlanmaz.'),
 TT(A='dikkat',C='dikkat',D='islem',E='bilgi'))

# ===== 0008 yıl ZOR
c=[k for k in range(1,60) if 3*k-k==58-26]; assert c==[16]
k=16; b=48; dd=k+58; assert dd==74 and dd-b==26 and 2026-dd==1952 and 2026-58==1968 and 2026-b==1978 and 2026-k==2010
k2=[k for k in range(1,60) if 3*k-k==26]; assert k2==[13] and 2026-(13+58)==1955
P.R('0008','yas-yil',T['yas-yil'],'zor','Doğum yılları ve farklar','Doğumlardaki yaşlardan yaş farklarını çıkarır, kat ilişkisiyle yaşları bulup doğum yılını hesaplar.','hikâyeli',5,
 'K-YAS-04 (takvim yılı ile yaş) · üç kuşak, iki yaş farkı ve kat ilişkisi, istenen doğum yılı',
 'Kerem, 2026 yılında dedesiyle sohbet etmektedir. Dedesi Kerem’e şunları söylemiştir:\n• “Sen doğduğunda ben 58 yaşındaydım.”\n• “Baban doğduğunda ise ben 26 yaşındaydım.”\nBugün Kerem’in babasının yaşı, Kerem’in yaşının 3 katı olduğuna göre dede hangi yılda doğmuştur?',
 ['1952','1955','1968','1978','2010'],'A','Dedenin doğum yılı.',
 ['Dede ile Kerem, dede ile baba arasındaki yaş farkları nedir?','Bu iki farktan baba ile Kerem arasındaki yaş farkını bul.','Kerem’in yaşını bul, dedenin yaşına geç ve 2026’dan çıkar.'],[YIL,FARK],
 [A('Yaş farkları','Doğumdaki yaş, yaş farkıdır.','dede − Kerem = 58 · dede − baba = 26'),
  A('Baba − Kerem','İki farkın farkı.','58 − 26 = 32'),
  A('Kerem’in yaşı','Baba 3k, Kerem k; fark 2k.','2k = 32 ⇒ k = 16 · baba 48'),
  A('Dedenin yaşı','Kerem’den 58 büyük.','16 + 58 = 74'),
  A('Doğum yılı','Yıl − yaş.','2026 − 74 = 1952')],
 'Birinin doğduğu andaki yaş, iki kişi arasındaki yaş farkıdır; farkların farkı da üçüncü bir farktır.',
 dict(B='1955, baba ile Kerem arasındaki farkı 26 almak (k = 13, dede 71).',C='1968, 58’i dedenin bugünkü yaşı sanmak.',D='1978, Kerem’in babasının doğum yılı.',E='2010, Kerem’in doğum yılı.'),
 TT(B='dikkat',C='bilgi',D='dikkat',E='dikkat'))
c=[a for a in range(34,99) if a+(a-27)+(a-33)==81]; assert c==[47]
a=47; kb,kk=a-27,a-33; assert (kb,kk)==(20,14) and 27-kk==13 and 81+3*13==120 and 81+13==94 and 81+26==107 and a+13==60 and 81+3*(33-kk)==138
P.K('0008','Bir anne, 2025 yılında iki kızıyla ilgili şunları söylemiştir:\n• “Büyük kızım doğduğunda 27, küçük kızım doğduğunda 33 yaşındaydım.”\n• “Bugün üçümüzün yaşları toplamı 81’dir.”\nBuna göre küçük kız, annesinin büyük kızını doğurduğu yaşa geldiğinde bu üç kişinin yaşları toplamı kaç olur?',
 ['60','94','107','120','138'],'D','Küçük kız 27 yaşına geldiğinde üç kişinin yaşları toplamı.',
 ['Annenin yaşına a de; kızların yaşlarını a ile yaz.','Toplamdan a’yı bul; küçük kız kaç yaşında?','Küçük kızın 27 yaşına gelmesi kaç yıl sürer? O sürede üç kişinin toplamı kaç artar?'],[FARK,TOP],
 [A('Yaşları yaz','Doğumdaki yaşlar yaş farklarıdır.','anne a · büyük kız a − 27 · küçük kız a − 33'),
  A('Toplamı kullan','Üç yaşın toplamı 81.','3a − 60 = 81 ⇒ a = 47'),
  A('Kızların yaşları','Büyük kız 20, küçük kız 14.','47 + 20 + 14 = 81 ✓'),
  A('Geçecek süre','Küçük kız 27 yaşına 13 yıl sonra gelir.','27 − 14 = 13 yıl'),
  A('Yeni toplam','Üç kişi 13’er yaş büyür.','81 + 3 × 13 = 120')],
 'Gelecekteki toplamı bulurken geçecek yılı kişi sayısıyla çarpıp bugünkü toplama ekle.',
 dict(A='60, annenin o zamanki yaşı; soru üç kişinin toplamını soruyor.',B='94, toplama 13’ü yalnızca bir kez eklemek.',C='107, 13 yılı yalnızca iki kişiye eklemek.',E='138, küçük kızın 33 yaşına gelmesini hesaplamak; istenen yaş 27.'),
 TT(A='dikkat',B='islem',C='islem',E='dikkat'))

P.yaz(os.path.join(H,'yasprob-1.json'),os.path.join(H,'yasprob-1-kardes.json'))
