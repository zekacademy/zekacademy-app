"""Sayı Problemleri · iskelet havuz (8 ana + 8 kardeş). Her cevap ve ara sonuç kodla doğrulanır."""
import sys,os,json
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..'))
from ortak import *
TT=lambda **k:k
KONU='Sayı Problemleri'; UK='prob|Sayı Problemleri'
P=Parti('sayiprob',KONU,UK)

# ---------- kartlar ve tipler
KARTLAR=[
 dict(id='K-SP-01',konu=KONU,alt='İki tür nesne',fikir='Toplam adet ve toplam tutar (ya da toplam tekerlek, koltuk) verilir; “hepsi ucuz olandan olsaydı” düşüncesiyle fark, birim farka bölünür. Değişim sonrası yeni toplamdan değişen adet bulunur.',
      tuzak='İstenen türü karıştırma (diğer türün adedini işaretleme); değişimde birim farkı yerine yeni birimin değerine bölme.',zorluk='kolay-orta',kalip='hikâyeli',adim=3,tipId='sp-iki-urun',tip='İki tür nesneyle adet-tutar denklemi',
      kaynak='ÖSYM YKS çıkmış (kitap s257 #135, bina–kat değişimi) · Bilgi Sarmal ve 345 SB bilet/araç soruları'),
 dict(id='K-SP-02',konu=KONU,alt='Eşit aralıklı dizilim',fikir='Belirli uzunluktaki yola eşit aralıklarla fidan, direk ya da bank konur; açık yolda öğe = aralık + 1, kapalı yolda öğe = aralık.',
      tuzak='Aralık sayısını öğe sayısı sanma; yolun iki kenarı istenince ikiyle çarpmayı unutma; çemberde +1 ekleme.',zorluk='kolay',kalip='hikâyeli',adim=2,tipId='sp-dizilim',tip='Eşit aralıklı dizilim',
      kaynak='ÖSYM YKS çıkmış (kitap s90, ağaç dikme planı) · Bilgi Sarmal s123, s130, s201'),
 dict(id='K-SP-03',konu=KONU,alt='Eşit paylaşım',fikir='Bir tutar kişilere eşit paylaştırılacakken bazı kişiler ödeyemez ya da eksik öder; eksik kalan tutar ötekilere eşit bölünür ve kişi başı artış verilir.',
      tuzak='Eksik kalan tutarı yanlış sayma (yarı ödeyenleri hiç ödemedi sayma); planlanan payla gerçekleşen ödemeyi karıştırma.',zorluk='orta-zor',kalip='hikâyeli',adim=4,tipId='sp-paylasim',tip='Planlanan ve gerçekleşen eşit paylaşım',
      kaynak='ÖSYM YKS çıkmış (kitap s253 #120, ortak hediye) · Bilgi Sarmal s212 #9, s220 #7 · Mert s164 #4'),
 dict(id='K-SP-04',konu=KONU,alt='Kaplarla ölçme',fikir='Eşit miktardaki iki kap, iki farklı kap türünün farklı sayılarını doldurur; iki ifade eşitlenerek kaplar arasındaki oran bulunur.',
      tuzak='Oranı ters çevirme; yalnızca bir kap türünü çevirip diğerini eklemeyi unutma.',zorluk='orta',kalip='hikâyeli',adim=3,tipId='sp-kap',tip='Eşit miktarları kaplarla karşılaştırma',
      kaynak='ÖSYM YKS çıkmış (kitap s238 #67, şişe–bardak–fincan) · Bilgi Sarmal s124 #7, s146 #8'),
 dict(id='K-SP-05',konu=KONU,alt='Kampanya karşılaştırma',fikir='İki satıcının farklı kampanyaları verilir; istenen adedi en ucuza almak için kampanyalar ayrı ayrı ve birlikte denenir.',
      tuzak='“3 alana 1 hediye” ile “3’te 1 bedava”yı karıştırma; iki satıcıyı birlikte kullanmanın daha ucuz olabileceğini düşünmeme.',zorluk='orta-zor',kalip='hikâyeli',adim=4,tipId='sp-kampanya',tip='Kampanya ve alışveriş karşılaştırma',
      kaynak='ÖSYM YKS çıkmış (kitap s252, 50 TL üzeri indirim · s267 #170, iki kırtasiye kampanyası) · Bilgi Sarmal s227 #4, s244 #14'),
]
TIPLER=[dict(tipId=k['tipId'],ad=k['tip'],kartlar=[k['id']],uygulamaKonu=UK) for k in KARTLAR]
json.dump(dict(konu=KONU,surum=1,kartlar=KARTLAR,tipler=TIPLER),open(os.path.join(H,'..','kartlar','sayiprob.json'),'w'),ensure_ascii=False,indent=1)
T={k['tipId']:k['tip'] for k in KARTLAR}

HEPSI=B('“Hepsi aynı olsaydı” yöntemi','her şeyi ucuz türden say, gerçek toplamla aradaki fark, birim farka bölünür. Örnek: 10 tavuk-koyun, 28 ayak ⇒ hepsi tavuk 20 ayak, fark 8, 8 ÷ 2 = 4 koyun')
ARALIK=B('Aralık ve öğe sayısı','düz yolda iki uca da öğe konuyorsa öğe = aralık + 1; çember gibi kapalı yolda öğe = aralık. Örnek: 20 m yol, 5 m aralık ⇒ 4 aralık, 5 fidan')
PAY=B('Eşit paylaşım','kişi başı pay = toplam tutar ÷ kişi sayısı. Örnek: 1200 TL 4 kişiye ⇒ 300 TL')

# ===== 0001 iki ürün KOLAY
c=[(t,30-t) for t in range(31) if 240*t+180*(30-t)==6120]; assert c==[(12,18)] and 30*240-6120==1080 and 1080//60==18
assert 1080/180==6 and (6120-30*180)/30==24
P.R('0001','sp-iki-urun',T['sp-iki-urun'],'kolay','İki tür bilet','İki tür nesnenin toplam adedi ve toplam tutarından bir türün adedini bulur.','hikâyeli',2,
 'K-SP-01 (iki tür nesne, toplam adet ve tutar) · yeni kurgu (sinema bileti), istenen ucuz türün adedi',
 'Bir sinemada tam bilet 240 TL, öğrenci bileti 180 TL’dir.\n30 kişilik bir arkadaş grubu, her kişiye bir bilet alarak bu sinemaya toplam 6120 TL ödemiştir.\nBuna göre gruptaki kişilerden kaçı öğrenci bileti almıştır?',
 ['6','12','15','18','24'],'D','Öğrenci bileti alan kişi sayısı.',
 ['Herkes tam bilet alsaydı kaç TL ödenirdi?','Bu tutar ile gerçekte ödenen arasındaki fark nereden geliyor?','Her öğrenci bileti, tam bilete göre kaç TL daha ucuz?'],[HEPSI],
 [A('Hepsi tam bilet','30 kişinin hepsi tam bilet alsaydı ödenecek tutarı bul.','30 × 240 = 7200 TL'),
  A('Farkı bul','Ödenen daha az; fark öğrenci biletlerinden geliyor.','7200 − 6120 = 1080 TL'),
  A('Öğrenci bileti sayısı','Her öğrenci bileti 240 − 180 = 60 TL ucuz.','1080 ÷ 60 = 18 · kontrol: 12 × 240 + 18 × 180 = 6120 ✓')],
 'İki türlü nesnede “hepsi bir türden olsaydı” de; fark ÷ birim fark diğer türün adedini verir.',
 dict(A='6, farkı (1080) öğrenci bileti fiyatına bölmek; fiyat farkına (60) bölünmeli.',B='12, tam bilet alanların sayısı; soru öğrenci biletini soruyor.',C='15, grubun yarısının öğrenci olduğunu varsaymak; ödenen tutar kullanılmamış.',E='24, hepsi öğrenci bileti sayıp fazlalığı (720) kişi sayısına (30) bölmek.'),
 TT(A='islem',B='dikkat',C='dikkat',E='bilgi'))
c=[(s,24-s) for s in range(25) if 15*s+25*(24-s)==460]; assert c==[(14,10)] and 460-24*15==100 and 100//10==10 and 100//5==20
P.K('0001','Bir fırında simidin tanesi 15 TL, poğaçanın tanesi 25 TL’dir.\nBir okul kantini bu fırından simit ve poğaça olmak üzere toplam 24 parça alıp 460 TL ödemiştir.\nBuna göre kantin kaç poğaça almıştır?',
 ['10','12','14','18','20'],'A','Alınan poğaça sayısı.',
 ['24 parçanın hepsi simit olsaydı kaç TL ödenirdi?','Gerçek tutarla aradaki fark nereden geliyor?','Her poğaça simitten kaç TL pahalı?'],[HEPSI],
 [A('Hepsi simit','24 parçanın hepsi simit olsaydı.','24 × 15 = 360 TL'),
  A('Farkı bul','Fazladan ödenen para poğaçalardan geliyor.','460 − 360 = 100 TL'),
  A('Poğaça sayısı','Her poğaça 25 − 15 = 10 TL fazla.','100 ÷ 10 = 10 · kontrol: 14 × 15 + 10 × 25 = 460 ✓')],
 'Fark tutarı, iki fiyat arasındaki farka bölünür; sonra hangi türün sorulduğuna bak.',
 dict(B='12, iki türden eşit sayıda alındığını varsaymak; toplam tutar kullanılmamış.',C='14, simit sayısı; soru poğaçayı soruyor.',D='18, toplamı (460) poğaça fiyatına bölüp yuvarlamak; iki tür birlikte alınmış.',E='20, fiyat farkını 5 TL almak; 25 − 15 = 10.'),
 TT(B='dikkat',C='dikkat',D='bilgi',E='islem'))

# ===== 0002 dizilim KOLAY
ara=180//12; assert ara==15 and 180%12==0; bir=ara+1; assert 2*bir==32 and 2*ara==30 and 2*(bir+1)==34
P.R('0002','sp-dizilim',T['sp-dizilim'],'kolay','Düz yolda dizilim','Düz bir yolun iki kenarına eşit aralıklarla konan nesnelerin sayısını aralık sayısından bulur.','hikâyeli',2,
 'K-SP-02 (açık yolda öğe = aralık + 1) · yeni kurgu (aydınlatma direği), yolun iki kenarı',
 'Bir parktaki 180 metrelik düz bir yürüyüş yolunun iki kenarına da aydınlatma direkleri dikilecektir.\nHer kenarda direkler 12 metre aralıklarla dikilecek; yolun başına ve sonuna da birer direk gelecektir.\nBuna göre toplam kaç direk dikilecektir?',
 ['15','16','30','32','34'],'D','İki kenardaki toplam direk sayısı.',
 ['Bir kenarda kaç tane 12 metrelik aralık var?','Başta ve sonda direk varsa direk sayısı aralık sayısından kaç fazla?','İki kenarı unutma.'],[ARALIK],
 [A('Aralık sayısı','Bir kenar 180 m; her aralık 12 m.','180 ÷ 12 = 15 aralık'),
  A('Bir kenardaki direk','Yolun iki ucunda da direk var: direk = aralık + 1.','15 + 1 = 16 direk'),
  A('İki kenar','Aynı dizilim karşı kenarda da yapılıyor.','2 × 16 = 32 direk')],
 'Düz yolda iki uçta da öğe varsa öğe sayısı aralık sayısından 1 fazladır; kenar sayısıyla sonra çarp.',
 dict(A='15, bir kenardaki aralık sayısı; direk sayısı değil.',B='16, yalnızca bir kenar; yolun iki kenarına da direk dikiliyor.',C='30, iki kenardaki aralık sayısı; her kenarda direk aralıktan 1 fazla.',E='34, her kenara 2 fazla direk saymak (17 + 17); bir kenarda 16 direk var.'),
 TT(A='bilgi',B='dikkat',C='bilgi',E='islem'))
ara=96//6; assert ara==16 and 96%6==0
P.K('0002','Çevresi 96 metre olan çember biçimindeki bir süs havuzunun kenarına oturma bankları konacaktır.\nBanklar havuzun kenarı boyunca 6 metre aralıklarla yerleştirilecek ve ardışık her iki bankın arası eşit olacaktır.\nBuna göre havuzun çevresine kaç bank konur?',
 ['8','15','16','17','32'],'C','Havuzun çevresindeki bank sayısı.',
 ['Çevrede kaç tane 6 metrelik aralık var?','Çember kapalı bir yoldur: ilk bank ile son bank yan yana gelir.','Kapalı yolda öğe sayısı ile aralık sayısı arasındaki ilişkiyi düşün.'],[ARALIK],
 [A('Aralık sayısı','Çevre 96 m, her aralık 6 m.','96 ÷ 6 = 16 aralık'),
  A('Kapalı yol','Çemberde son aralık ilk banka döner; başlangıç ve bitiş aynı banktır.','bank = aralık'),
  A('Sonuç','Aralık sayısı kadar bank vardır.','16 bank')],
 'Kapalı yolda (çember, kare çevre) öğe sayısı aralık sayısına eşittir; +1 yalnızca açık yolda eklenir.',
 dict(A='8, aralığı 12 m almak; aralık 6 m.',B='15, aralık sayısından 1 çıkarmak; çemberde öğe = aralık.',D='17, düz yoldaki gibi 1 eklemek; çemberde başlangıç ve bitiş aynı bank.',E='32, sayıyı iki kenar varmış gibi ikiyle çarpmak; havuzun tek bir çevresi var.'),
 TT(A='islem',B='bilgi',D='bilgi',E='dikkat'))

# ===== 0003 paylaşım ORTA
c=[n for n in range(3,60) if 4800%n==0 and 4800%(n-2)==0 and 4800//(n-2)-4800//n==200]; assert c==[8] and 4800//8==600 and 4800//6==800
assert 4800//200==24 and 4800//(2*200)==12 and 4800//(6*200)==4
P.R('0003','sp-paylasim',T['sp-paylasim'],'orta','Kişi sayısı değişince pay','Kişi sayısı azalınca kişi başı payın artışından başlangıçtaki kişi sayısını bulur.','hikâyeli',3,
 'K-SP-03 (planlanan–gerçekleşen paylaşım) · yeni kurgu (kamp alanı kirası), bazı kişiler katılmıyor',
 'Bir arkadaş grubu, 4800 TL tutan kamp alanı kirasını eşit olarak ödemeyi planlamıştır.\nGruptan 2 kişi son anda kampa katılamamış ve kiranın tamamını kampa katılanlar eşit olarak ödemiştir.\nBöylece kampa katılanların her biri planlanandan 200 TL fazla ödemiştir.\nBuna göre bu grupta başlangıçta kaç kişi vardır?',
 ['4','6','8','12','24'],'C','Gruptaki başlangıç kişi sayısı.',
 ['Başlangıçtaki kişi sayısına n de; planlanan pay ve gerçekleşen pay nedir?','İki pay arasındaki fark 200 TL.','4800’ü tam bölen ve aralarında 2 fark olan iki kişi sayısını dene.'],[PAY],
 [A('Payları yaz','n kişi planlanmış, n − 2 kişi ödemiş.','planlanan 4800 ÷ n · gerçekleşen 4800 ÷ (n − 2)'),
  A('Farkı kur','Gerçekleşen pay 200 TL fazla.','4800 ÷ (n − 2) − 4800 ÷ n = 200'),
  A('Dene ve bul','n = 8 için 4800 ÷ 6 = 800 ve 4800 ÷ 8 = 600.','800 − 600 = 200 ✓ ⇒ n = 8'),
  A('Kontrol','Katılmayan 2 kişinin payı (1200 TL), ödeyen 6 kişiye 200’er TL bindi.','2 × 600 = 6 × 200 = 1200 ✓')],
 'Eksilen kişilerin payı, kalanlara eşit dağılır: eksilenlerin toplam payı = kalan kişi × kişi başı artış.',
 dict(A='4, eksik kalan 1200 TL’yi kişi başı pay sanıp 4800 ÷ 1200 yapmak.',B='6, kampa katılan kişi sayısı; soru başlangıçtaki sayıyı soruyor.',D='12, 200 TL’yi iki kişinin payıyla çarpıp (400) 4800’ü buna bölmek.',E='24, toplamı (4800) kişi başı artışa (200) bölmek; artış pay değildir.'),
 TT(A='islem',B='dikkat',D='islem',E='bilgi'))
c=[n for n in range(1,60) if 9000%n==0 and 9000%(n+3)==0 and 9000//n-9000//(n+3)==250]; assert c==[9] and 9000//9==1000 and 9000//12==750
P.K('0003','Bir müzik topluluğu, bir festivale gitmek için 9000 TL’ye bir minibüs kiralamış ve kirayı eşit olarak ödemeyi planlamıştır.\nYola çıkmadan önce topluluğa 3 kişi daha katılmış ve kira tüm kişiler arasında eşit olarak paylaştırılmıştır.\nBöylece kişi başına düşen tutar planlanandan 250 TL azalmıştır.\nBuna göre başlangıçta kişi başına ödenmesi planlanan tutar kaç TL’dir?',
 ['250','600','750','900','1000'],'E','Başlangıçta planlanan kişi başı pay.',
 ['Başlangıçtaki kişi sayısına n de; iki payı n cinsinden yaz.','Payların farkı 250 TL.','9000’i tam bölen ve aralarında 3 fark olan kişi sayılarını dene.'],[PAY],
 [A('Payları yaz','n kişi planlanmış, sonra n + 3 kişi olmuş.','planlanan 9000 ÷ n · gerçekleşen 9000 ÷ (n + 3)'),
  A('Farkı kur','Pay 250 TL azalmış.','9000 ÷ n − 9000 ÷ (n + 3) = 250'),
  A('Dene ve bul','n = 9 için 9000 ÷ 9 = 1000, 9000 ÷ 12 = 750.','1000 − 750 = 250 ✓ ⇒ n = 9'),
  A('Planlanan pay','Soru başlangıçta planlanan payı soruyor.','9000 ÷ 9 = 1000 TL')],
 'Paylaşım sorularında önce kişi sayısını bul, sonra sorunun planlanan mı gerçekleşen mi payı istediğine bak.',
 dict(A='250, paydaki azalma miktarı; planlanan pay değil.',B='600, kişi sayısını 15 alıp 9000 ÷ 15 yapmak; katılan 3 kişiyi iki kez eklemek.',C='750, son durumdaki kişi başı tutar; soru planlananı soruyor.',D='900, n = 10 alıp 9000 ÷ 10 yapmak; 9000 ÷ 13 tam çıkmaz, denemeyi kontrol etmemişsin.'),
 TT(A='dikkat',B='dikkat',C='dikkat',D='islem'))

# ===== 0004 kaplar ORTA
s,k=Fr(2),Fr(1)  # şişe = 2 kavanoz
assert 4*s+3*k==2*s+7*k and 4*s+3*k==11 and 4*Fr(1,2)+3==5 and 4*s==8
c=[(a,b) for a in range(1,20) for b in range(1,20) if 4*a+3*b==2*a+7*b and a==2*b]; assert c
P.R('0004','sp-kap',T['sp-kap'],'orta','Kaplarla ölçme','Eşit miktarların iki farklı kap kombinasyonuyla dolduğu bilgisinden kaplar arasındaki oranı bulup istenen kap sayısını hesaplar.','hikâyeli',3,
 'K-SP-04 (eşit miktar, iki kap türü) · yeni kurgu (zeytinyağı tenekesi, şişe ve kavanoz), istenen yalnız tek tür kapla doldurma',
 'Her birinde eşit miktarda zeytinyağı bulunan iki tenekeden birincisindeki yağın tamamı özdeş 4 şişeyi ve özdeş 3 kavanozu, ikincisindeki yağın tamamı ise bu şişelerden 2’sini ve bu kavanozlardan 7’sini tamamen doldurmaktadır.\nBuna göre bir tenekedeki yağın tamamı bu kavanozlardan kaç tanesini doldurur?',
 ['2','5','7','8','11'],'E','Bir teneke yağın doldurduğu kavanoz sayısı.',
 ['Bir şişeye ş, bir kavanoza k de; iki tenekeyi eşitle.','Eşitlikten bir şişenin kaç kavanoz ettiğini bul.','Birinci tenekedeki şişeleri kavanoza çevirip kavanozlarla topla.'],[],
 [A('Eşitliği kur','İki tenekede eşit yağ var.','4ş + 3k = 2ş + 7k'),
  A('Şişe kaç kavanoz?','Ortak terimleri sadeleştir.','2ş = 4k ⇒ ş = 2k'),
  A('Tenekeyi çevir','Birinci tenekede 4 şişe ve 3 kavanoz var.','4 × 2k + 3k = 11k ⇒ 11 kavanoz · kontrol: 2 × 2k + 7k = 11k ✓')],
 'Eşit miktarlar iki farklı biçimde verilmişse eşitleyip bir kabı diğeri cinsinden yaz; sonra tek birime çevir.',
 dict(A='2, bir şişenin kaç kavanoz ettiği; soru bir tenekenin tamamını soruyor.',B='5, oranı ters almak (ş = k/2 ⇒ 4 × 1/2 + 3 = 5); şişe kavanozdan büyük.',C='7, ikinci tenekedeki kavanoz sayısı; şişeleri çevirmeyi unutmak.',D='8, yalnızca 4 şişeyi kavanoza çevirmek; 3 kavanoz eklenmedi.'),
 TT(A='dikkat',B='islem',C='dikkat',D='dikkat'))
b,s=Fr(1),Fr(2)  # sürahi = 2 bardak
assert 6*b+1*s==2*b+3*s and (6*b+s)/s==4 and (6*b+s)==8 and 6+1==7
P.K('0004','Eşit miktarda süt bulunan iki bidondan birincisindeki sütün tamamı özdeş 6 bardağı ve özdeş 1 sürahiyi, ikincisindeki sütün tamamı da bu bardaklardan 2’sini ve bu sürahilerden 3’ünü tamamen doldurmaktadır.\nBir bidondaki sütün tamamı yalnızca bu sürahilere boşaltılırsa kaç sürahi tamamen dolar?',
 ['2','4','7','8','16'],'B','Bir bidon sütün doldurduğu sürahi sayısı.',
 ['Bir bardağa b, bir sürahiye s de; iki bidonu eşitle.','Bir sürahi kaç bardak eder?','Birinci bidonu yalnızca sürahi cinsinden yaz.'],[],
 [A('Eşitliği kur','İki bidonda eşit süt var.','6b + s = 2b + 3s'),
  A('Sürahi kaç bardak?','Sadeleştir.','4b = 2s ⇒ s = 2b'),
  A('Bardak cinsinden','Bidon = 6b + 2b.','8 bardak'),
  A('Sürahiye çevir','Her sürahi 2 bardak.','8 ÷ 2 = 4 sürahi')],
 'Eşitlikten bulduğun oranı her iki yönde de kontrol et: büyük kap küçük kabın katıdır.',
 dict(A='2, bir sürahinin kaç bardak ettiği; soru bidonun sürahi sayısını soruyor.',C='7, birinci bidondaki kap sayılarını (6 + 1) toplamak; kaplar eşit büyüklükte değil.',D='8, bidonun bardak cinsinden değeri; soru sürahi sayısını soruyor.',E='16, iki bidonun toplamını bardak cinsinden almak; soru bir bidonu soruyor.'),
 TT(A='dikkat',C='bilgi',D='dikkat',E='dikkat'))

# ===== 0005 kampanya ORTA
def hediyeli(paid,g):  # her g alana 1 hediye
    return paid+paid//g
fiy=90
# A: 3 alana 1 hediye ; B: tanesi 70 TL ; tam 12 defter (fazlası olabilir ama gereksiz)
best=min(fiy*pa+70*b for pa in range(20) for b in range(20) if hediyeli(pa,3)+b>=12)
assert best==810 and 9*90==810 and 12*70==840 and 12*90==1080 and 8*90==720 and 6*90+4*70==820 and hediyeli(9,3)==12
P.R('0005','sp-kampanya',T['sp-kampanya'],'orta','İki kampanya','İki farklı kampanyada aynı adet ürünün tutarını hesaplayıp en düşük ödemeyi bulur.','hikâyeli',3,
 'K-SP-05 (iki satıcı, farklı kampanya) · yeni kurgu (defter), kampanyalar hediye ve tane indirimi',
 'Bir defterin satış fiyatı K ve L kırtasiyelerinde 90 TL’dir. Bu kırtasiyelerdeki kampanyalar aşağıdaki gibidir:\n• K kırtasiyesinde her 3 defter alana 1 defter hediye verilmektedir.\n• L kırtasiyesinde her defter 70 TL’ye satılmaktadır.\n12 deftere ihtiyacı olan Ayşe, defterleri bu kırtasiyelerden birinden ya da ikisinden alacaktır.\nBuna göre Ayşe en az kaç TL ödeyerek 12 defter edinir?',
 ['720','810','820','840','1080'],'B','12 defter için ödenecek en az tutar.',
 ['K’de her 4 defterin kaçı için para ödenir?','12 defteri yalnız K’den ve yalnız L’den almanın tutarını ayrı ayrı bul.','İki kırtasiyeyi birlikte kullanmak daha ucuz olur mu, dene.'],[],
 [A('K kırtasiyesi','3 defter ödeyen 4 defter alır. 12 defter = 3 grup.','3 × 3 = 9 defter öde · 9 × 90 = 810 TL'),
  A('L kırtasiyesi','Her defter 70 TL.','12 × 70 = 840 TL'),
  A('Karma deneme','K’den 8 defter (6 öde), L’den 4 defter.','6 × 90 + 4 × 70 = 820 TL'),
  A('En azı seç','K’de defter başı maliyet 810 ÷ 12 = 67,5 TL; L’de 70 TL. K’den almak en ucuzudur.','en az 810 TL')],
 'Kampanyaları karşılaştırırken tane başına düşen maliyeti hesapla; karma seçenekleri de dene.',
 dict(A='720, “3 alana 1 hediye”yi “her 3 defterden 1’i bedava” sanmak (8 defter öde); doğrusu her 4 defterden 1’i bedava.',C='820, iki kırtasiyeyi karıştırmanın daha ucuz olduğunu sanmak; K’de defter başı maliyet daha düşük.',D='840, yalnız L kırtasiyesinin tutarı; K daha ucuz.',E='1080, kampanyasız fiyat (12 × 90).'),
 TT(A='dikkat',C='islem',D='islem',E='bilgi'))
best=min(120*pa+(240+100*max(0,b-2) if b>=2 else 120*b) for pa in range(20) for b in range(20) if pa+pa//4+b>=12)
assert best==1200 and 10*120==1200 and 240+10*100==1240 and 12*120==1440 and 9*120==1080 and 8*120==960 and (hediyeli(8,4)+2==12)
P.K('0005','Bir kahvenin fiyatı M ve N kafelerinde 120 TL’dir. Bu kafelerin kampanyaları şöyledir:\n• M kafede her 4 kahve alana 1 kahve ikram edilmektedir.\n• N kafede ilk 2 kahve 120 TL’den, sonraki her kahve 100 TL’den satılmaktadır.\nBir ofis çalışanı, toplantı için 12 kahve almak istemektedir.\nKahveleri bu kafelerin birinden ya da ikisinden alabildiğine göre ödeyeceği en az tutar kaç TL’dir?',
 ['960','1080','1200','1240','1440'],'C','12 kahve için ödenecek en az tutar.',
 ['M’de kaç kahve için para ödenirse 12 kahveye ulaşılır?','N’de 12 kahvenin tutarını hesapla.','Her iki kafeyi birlikte kullanmayı da dene.'],[],
 [A('M kafe','4 kahve ödeyen 5 kahve alır. 10 kahve için 8 ödenir, kalan 2 kahve ikramsız.','8 + 2 = 10 kahve öde · 10 × 120 = 1200 TL'),
  A('N kafe','İlk 2 kahve 120 TL, sonraki 10 kahve 100 TL.','2 × 120 + 10 × 100 = 1240 TL'),
  A('Karma deneme','M’den 10 kahve (8 öde), N’den 2 kahve.','8 × 120 + 2 × 120 = 1200 TL'),
  A('En az tutar','Hiçbir seçenek 1200 TL’nin altına inmiyor.','en az 1200 TL')],
 'Hediye kampanyasında grup dışında kalan ürünler tam fiyattır; grupları ve kalanı ayrı hesapla.',
 dict(A='960, M’de 8 kahve ödeyip 10 kahve almak; 12 kahve gerekiyordu.',B='1080, “her 4 kahveden 1’i ikram” sanıp 9 kahve ödemek; ikram 4 kahve alana veriliyor.',D='1240, yalnız N kafenin tutarı.',E='1440, kampanyasız fiyat (12 × 120).'),
 TT(A='dikkat',B='dikkat',D='islem',E='bilgi'))

# ===== 0006 iki ürün (değişim) ORTA
c=[m for m in range(21) if 5*(20-m)+16*m==166]; assert c==[6]
d=(199-166); assert d%11==0 and d//11==3; oto=14-3; assert oto==11 and 6+3==9 and 14+3==17
P.R('0006','sp-iki-urun',T['sp-iki-urun'],'orta','Araç değişimi','Toplam adet ve toplam kapasiteden türlerin sayısını, değişim sonrası kapasite artışından değişen araç sayısını bulur.','hikâyeli',4,
 'K-SP-01 (iki tür nesne) · değişim eklendi (kapasite artışı), yeni kurgu (tur şirketi araçları)',
 'Bir tur şirketinin 20 aracı vardır ve bu araçların her biri ya 5 kişilik otomobil ya da 16 kişilik minibüstür. Araçların toplam yolcu kapasitesi 166 kişidir.\nŞirket, otomobillerinden bazılarını satıp her birinin yerine birer minibüs almış ve toplam kapasite 199 kişiye çıkmıştır.\nBuna göre şirketin son durumda kaç otomobili vardır?',
 ['3','9','11','14','17'],'C','Son durumdaki otomobil sayısı.',
 ['20 aracın hepsi otomobil olsaydı kapasite kaç olurdu?','Bir otomobil yerine minibüs gelince kapasite kaç kişi artar?','Kapasitedeki son artışı bu farka böl.'],[HEPSI],
 [A('Hepsi otomobil','20 otomobil 100 kişi taşır; fazlalık minibüslerden gelir.','166 − 20 × 5 = 66'),
  A('Minibüs sayısı','Her minibüs otomobilden 16 − 5 = 11 kişi fazla taşır.','66 ÷ 11 = 6 minibüs · 14 otomobil'),
  A('Değişen araç','Kapasite artışı yine 11’in katıdır.','199 − 166 = 33 · 33 ÷ 11 = 3 araç'),
  A('Son durum','3 otomobil yerine minibüs geldi.','14 − 3 = 11 otomobil')],
 'Bir nesneyi diğer türle değiştirince toplam, birim fark kadar değişir; artışı birim farka böl.',
 dict(A='3, değiştirilen araç sayısı; soru kalan otomobilleri soruyor.',B='9, son durumdaki minibüs sayısı.',D='14, başlangıçtaki otomobil sayısı; değişim hesaba katılmamış.',E='17, değiştirilen araçları otomobile eklemek; otomobiller satıldı.'),
 TT(A='dikkat',B='dikkat',D='dikkat',E='islem'))
c=[f for f in range(26) if 2*(25-f)+4*f==76]; assert c==[13]; iki=12
d=92-76; assert d%4==0 and d//4==4; assert iki-4==8 and iki+4==16 and 8+13==21
P.K('0006','Bir kafedeki 25 masanın her biri 2 kişilik ya da 4 kişiliktir ve masalarda toplam 76 sandalye vardır.\nKafe sahibi 2 kişilik masaların bazılarını kaldırıp her birinin yerine 6 kişilik birer masa koymuş ve sandalye sayısı 92’ye çıkmıştır.\nHer masanın sandalye sayısı kişi sayısı kadar olduğuna göre son durumda kafede kaç tane 2 kişilik masa vardır?',
 ['8','12','13','16','21'],'A','Son durumdaki 2 kişilik masa sayısı.',
 ['Masaların hepsi 2 kişilik olsaydı kaç sandalye olurdu?','2 kişilik bir masanın yerine 6 kişilik masa gelince sandalye kaç artar?','Önce başlangıçtaki 2 kişilik masa sayısını bul.'],[HEPSI],
 [A('Hepsi 2 kişilik','25 masa 50 sandalye eder; fazlası 4 kişilik masalardan.','76 − 50 = 26 · 26 ÷ 2 = 13 dört kişilik'),
  A('2 kişilik masalar','Kalan masalar 2 kişilik.','25 − 13 = 12'),
  A('Değişen masa','Her değişim 6 − 2 = 4 sandalye ekler.','92 − 76 = 16 · 16 ÷ 4 = 4 masa'),
  A('Son durum','4 tane 2 kişilik masa kaldırıldı.','12 − 4 = 8')],
 'Değişimde birim fark, eski ve yeni nesnenin farkıdır (6 − 2), yeni nesnenin kendisi (6) değildir.',
 dict(B='12, başlangıçtaki 2 kişilik masa sayısı.',C='13, 4 kişilik masa sayısı; soru 2 kişilik masaları soruyor.',D='16, değişen masaları 2 kişiliklere eklemek; o masalar kaldırıldı.',E='21, son durumda 2 ve 4 kişilik masaların toplamı.'),
 TT(B='dikkat',C='dikkat',D='islem',E='dikkat'))

# ===== 0007 paylaşım ZOR
p=Fr(5*280,Fr(2)+Fr(3,2)); assert p==400 and 10*p==4000; od=p+280; assert od==680
assert 0*2+3*(p/2)+5*od==10*p
p2=Fr(1400,5); assert p2+280==560; p3=Fr(1400,2); assert p3+280==980
P.R('0007','sp-paylasim',T['sp-paylasim'],'zor','Eksik ödeme','Bazı kişilerin hiç ödemediği, bazılarının yarı ödediği paylaşımda eksik tutarı kişi başı artışla eşitleyip gerçekleşen ödemeyi bulur.','hikâyeli',5,
 'K-SP-03 (planlanan–gerçekleşen paylaşım) · iki farklı eksik ödeme (hiç ve yarı), istenen gerçekleşen pay',
 '10 kişilik bir ekip, emekli olan bir çalışma arkadaşına alınacak hediyenin tutarını eşit olarak paylaşmayı planlamıştır.\nEkipten 2 kişi hiç para verememiş, 3 kişi ise kendi payının yalnızca yarısını verebilmiştir.\nEksik kalan tutarı ekipteki diğer 5 kişi eşit olarak tamamlamış ve bu 5 kişinin her biri planlanandan 280 TL fazla ödemiştir.\nBuna göre bu 5 kişiden her biri kaç TL ödemiştir?',
 ['280','400','560','680','980'],'D','Eksiği tamamlayan kişilerden her birinin ödediği tutar.',
 ['Planlanan kişi başı paya p de. Hiç vermeyen 2 kişi kaç p eksik bıraktı?','Yarısını veren 3 kişinin eksiği ne kadar?','Toplam eksik, 5 kişinin fazladan ödediği tutara eşittir.'],[PAY],
 [A('Payı adlandır','Planlanan kişi başı pay p olsun.','hediye = 10p'),
  A('Eksiği hesapla','2 kişi p’nin tamamını, 3 kişi p’nin yarısını eksik bıraktı.','2p + 3 × p/2 = 3,5p'),
  A('Eşitle','Eksik, 5 kişinin fazladan ödediği paradır.','3,5p = 5 × 280 = 1400 ⇒ p = 400 TL'),
  A('Ödenen tutar','Her biri payına 280 TL ekledi.','400 + 280 = 680 TL'),
  A('Kontrol','Toplanan para hediye tutarına eşit olmalı.','3 × 200 + 5 × 680 = 4000 = 10 × 400 ✓')],
 'Eksik ödeme sorularında herkesin eksiğini payın kesri olarak yaz; toplam eksik = tamamlayan kişi × artış.',
 dict(A='280, kişi başı fazladan ödenen tutar; ödenen tutarın tamamı değil.',B='400, planlanan kişi başı pay; bu kişiler buna 280 TL ekledi.',C='560, yarısını verenleri hiç vermedi saymak (5p = 1400 ⇒ p = 280).',E='980, yarısını veren 3 kişinin eksiğini unutmak (2p = 1400 ⇒ p = 700).'),
 TT(A='dikkat',B='dikkat',C='dikkat',E='dikkat'))
p=Fr(6*150,Fr(1)+2*Fr(1,2)); assert p==450 and 9*p==4050 and p+150==600 and 6*600+2*225==4050
assert Fr(900,3)*9==2700 and 6*600==3600 and 9*600==5400 and 900*9==8100
P.K('0007','9 kişilik bir aile, bir restoranda yedikleri yemeğin hesabını eşit olarak ödemeyi planlamıştır.\nAiledeki çocuklardan biri hiç ödeme yapmamış, iki genç ise kendi paylarının yarısını ödemiştir.\nKalan tutarı diğer 6 kişi eşit olarak paylaşmış ve bu 6 kişinin her biri planlanandan 150 TL fazla ödemiştir.\nBuna göre yemeğin hesabı kaç TL’dir?',
 ['2700','3600','4050','5400','8100'],'C','Yemek hesabının tamamı.',
 ['Planlanan kişi başı paya p de; kim ne kadar eksik bıraktı?','Yarısını ödeyen iki kişinin toplam eksiği kaç p eder?','Toplam eksik = 6 × 150.'],[PAY],
 [A('Payı adlandır','Planlanan kişi başı pay p.','hesap = 9p'),
  A('Eksiği hesapla','1 kişi p, 2 kişi yarım p eksik bıraktı.','p + 2 × p/2 = 2p'),
  A('Eşitle','Eksik, 6 kişinin fazladan ödediği para.','2p = 6 × 150 = 900 ⇒ p = 450 TL'),
  A('Hesabın tamamı','Planlanan pay × kişi sayısı.','9 × 450 = 4050 TL'),
  A('Kontrol','Ödenenleri topla.','2 × 225 + 6 × 600 = 4050 ✓')],
 'Hesabın tamamı, planlanan pay ile toplam kişi sayısının çarpımıdır; ödeme yapmayanlar da sayılır.',
 dict(A='2700, yarısını ödeyenleri hiç ödemedi saymak (3p = 900 ⇒ p = 300).',B='3600, yalnızca 6 kişinin ödediği tutarı toplamak; yarım ödemeler eksik.',D='5400, 6 kişinin ödediği 600 TL’yi 9 kişiyle çarpmak.',E='8100, yarısını ödeyen iki kişinin eksiğini unutmak (p = 900).'),
 TT(A='dikkat',B='islem',D='islem',E='dikkat'))

# ===== 0008 kampanya ZOR (karma alım en ucuz)
fA=lambda n:120*(n//2)*Fr(3,2)+120*(n%2)
sec=[(fA(a)+120*pb,a,pb) for a in range(15) for pb in range(15) if a+hediyeli(pb,2)>=8]
best=min(sec)[0]; assert best==660 and min(c for c,a,pb in sec if pb==0)==720 and min(c for c,a,pb in sec if a==0)==720
assert [x for x in sec if x[0]==660]==[(660,2,4)] and 8*120==960 and 5*120==600 and 7*120+60==900
P.R('0008','sp-kampanya',T['sp-kampanya'],'zor','Karma alım','İki farklı kampanyayı birlikte kullanarak istenen adedin en düşük maliyetini bulur.','hikâyeli',5,
 'K-SP-05 (iki satıcı, farklı kampanya) · iki satıcıyı birlikte kullanmak en ucuz, yeni kurgu (damacana su)',
 'Bir ofis için en az 8 damacana su alınacaktır. Bir damacana suyun fiyatı R ve S marketlerinde 120 TL’dir.\n• R marketinde alınan her 2 damacanadan biri yarı fiyatına satılmaktadır.\n• S marketinde her 2 damacana alana 1 damacana hediye edilmektedir.\nSular bu marketlerin birinden ya da ikisinden alınabildiğine göre en az kaç TL ödenir?',
 ['600','660','720','900','960'],'B','En az 8 damacana için ödenecek en düşük tutar.',
 ['Her markette damacana başına düşen maliyeti hesapla.','S’de kaç damacana ödenirse 8’e en yakın sayıda damacana alınır; eksik kalanı nereden alırsın?','Yalnız R, yalnız S ve ikisini birlikte kullanan seçenekleri karşılaştır.'],[],
 [A('Tane başı maliyet','R’de 2 damacana 180 TL; S’de 3 damacana 240 TL.','R: 90 TL · S: 80 TL'),
  A('Tek marketten','R’den 8 damacana 4 × 180. S’de 8’e ulaşmak için 6 damacana ödenip 9 alınır.','R: 720 TL · S: 6 × 120 = 720 TL'),
  A('Karma alım','S’de 4 damacana öde, 6 al; eksik 2 damacanayı R’den al.','4 × 120 + 180 = 660 TL'),
  A('Diğer karmalar','S’de 2 öde 3 al, R’den 5 al: 240 + 2 × 180 + 120 = 720.','660 en az'),
  A('Sonuç','En ucuz yol karma alım.','660 TL')],
 'Kampanyaların “tam grup” avantajı vardır: ucuz markette tam grupları al, artakalanı diğer markette tamamla.',
 dict(A='600, S’de 5 damacana ödeyip 8 damacana alınacağını sanmak; 5 ödeyene yalnızca 2 hediye verilir.',C='720, yalnızca tek marketten almak; iki market birlikte daha ucuz.',D='900, R’deki indirimi yalnızca bir kez uygulamak (7 × 120 + 60).',E='960, kampanyasız fiyat (8 × 120).'),
 TT(A='islem',C='dikkat',D='dikkat',E='bilgi'))
fB=lambda n:160*(n//2)*Fr(3,2)+160*(n%2)
sec=[(160*pa+fB(b),pa,b) for pa in range(15) for b in range(15) if hediyeli(pa,2)+b>=11]
best=min(sec)[0]; assert best==1200 and min(c for c,pa,b in sec if b==0)==1280 and min(c for c,pa,b in sec if pa==0)==1360
assert [x[1:] for x in sec if x[0]==1200]==[(6,2)] and 11*160==1760 and 7*160==1120
P.K('0008','Bir resim kursu için en az 11 kutu boya kalemi alınacaktır. Bir kutunun fiyatı T ve U kırtasiyelerinde 160 TL’dir.\n• T kırtasiyesinde her 2 kutu alana 1 kutu hediye verilmektedir.\n• U kırtasiyesinde alınan her 2 kutudan biri yarı fiyatına satılmaktadır.\nKutular bu kırtasiyelerin birinden ya da ikisinden alınabildiğine göre en az kaç TL ödenir?',
 ['1120','1200','1280','1360','1760'],'B','En az 11 kutu için en düşük ödeme.',
 ['Her kırtasiyede kutu başına düşen maliyeti bul.','Ucuz olan kırtasiyede tam gruplarla 11’e en yakın sayıyı al.','Eksik kalan kutuları diğer kırtasiyeden tamamlamayı dene.'],[],
 [A('Tane başı maliyet','T’de 3 kutu 320 TL; U’da 2 kutu 240 TL.','T: yaklaşık 106,7 TL · U: 120 TL'),
  A('Tek kırtasiye','T’de 8 kutu öde, 12 al. U’da 11 kutu: 5 çift + 1 kutu.','T: 1280 TL · U: 5 × 240 + 160 = 1360 TL'),
  A('Karma alım','T’de 6 öde, 9 al; kalan 2 kutuyu U’dan al.','6 × 160 + 240 = 1200 TL'),
  A('Sonuç','Diğer karmalar bundan pahalı.','en az 1200 TL')],
 'Karma alımda ucuz yerdeki tam grupları kullan, artanı ikinci en ucuz yoldan tamamla.',
 dict(A='1120, T’de 7 kutu ödeyip 11 kutu alınacağını sanmak; 7 ödeyene 3 hediye verilir (10 kutu).',C='1280, yalnız T kırtasiyesinden almak; karma alım daha ucuz.',D='1360, yalnız U kırtasiyesinden almak.',E='1760, kampanyasız fiyat (11 × 160).'),
 TT(A='islem',C='dikkat',D='dikkat',E='bilgi'))

P.yaz(os.path.join(H,'sayiprob-1.json'),os.path.join(H,'sayiprob-1-kardes.json'))
