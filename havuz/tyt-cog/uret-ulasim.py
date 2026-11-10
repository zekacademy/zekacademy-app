import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_b import *
Q=Konu('ulasim','Uluslararası Ulaşım Hatları','cog|Uluslararası Ulaşım Hatları',4)
Q.kart('K-CGUL-01','Taşıma türleri','Deniz taşımacılığı büyük hacimli, ağır yükleri ucuza taşır; hava hızlıdır ama pahalıdır; kara kapıdan kapıya hizmet verir.','Taşıma türlerinin üstünlüklerini karıştırmak.','kolay','düz',2,'cg-ulasim-tur','Taşıma türlerinin özellikleri')
Q.kart('K-CGUL-02','Kanal ve boğazlar','Süveyş: Akdeniz–Kızıldeniz; Panama: Atlas–Pasifik; Cebelitarık: Akdeniz–Atlas; İstanbul: Karadeniz–Marmara; Çanakkale: Marmara–Ege.','Kanal ve boğazların bağladığı denizleri karıştırmak.','orta','öncüllü',3,'cg-ulasim-gecit','Kanal ve boğazların bağladığı denizler')
Q.kart('K-CGUL-03','Kanalın etkisi','Süveyş Kanalı Avrupa ile Hint Okyanusu çevresi arasındaki deniz yolunu Ümit Burnu’na göre kısaltır.','Kanalın bağladığı denizleri karıştırıp yanlış sonuç çıkarmak.','orta','düz',3,'cg-ulasim-kanal','Süveyş Kanalı’nın etkisi')
Q.kart('K-CGUL-04','Rota karşılaştırma','Mesafe farkı hıza bölünerek süre, süre farkı günlük tüketimle çarpılarak tasarruf bulunur.','Saat ile günü karıştırmak; tek rotanın değerini vermek.','zor','hikâyeli',4,'cg-ulasim-rota','Rota seçimi ve yakıt hesabı')
# ---- 0001
Q.S('0001','K-CGUL-01','kolay','Deniz taşımacılığının diğer taşıma türlerine göre üstünlüğünü belirler.',
 'Aşağıdakilerden hangisi deniz taşımacılığının diğer taşıma türlerine göre üstünlüklerinden biridir?',
 [('Ağır ve hacimli yüklerin birim maliyetinin düşük olması',True,'',''),('Yükün aktarma yapılmadan kapıdan kapıya taşınabilmesi',False,'Kapıdan kapıya taşıma karayolunun üstünlüğüdür; denizde liman gerekir.','bilgi'),('Taşıma süresinin diğer türlere göre en kısa olması',False,'En hızlı taşıma havayoludur; deniz yavaştır.','bilgi'),('Hava koşullarından hiç etkilenmeden sefer yapabilmesi',False,'Fırtına ve sis denizyolunu etkiler.','dikkat'),('Kıyısı olmayan bölgelere de doğrudan ulaşabilmesi',False,'Denizyolu ancak kıyılara ve limanlara ulaşır.','bilgi')],'A',
 'Deniz taşımacılığının üstünlüğü.','Gemilerin bir seferde ne kadar yük taşıdığını ve neden ucuz olduğunu düşün.',
 [B('Taşıma türleri','Denizyolu: büyük hacim, ağır yük, ucuz, yavaş · Havayolu: hızlı, pahalı · Karayolu: kapıdan kapıya, esnek · Demiryolu: ağır yük, orta hız, raylı')],
 [A('Özelliği hatırla','Gemiler bir seferde çok yük taşır, birim maliyet düşer.','deniz: çok yük, ucuz'),
  A('Şıkları sına','B karayolunu, C havayolunu anlatır; D ve E denizyoluna uymaz.','B: kara · C: hava · D, E: yanlış'),
  A('Sonuç','Düşük birim maliyet denizin üstünlüğüdür.','A')],
 'Ucuz ve büyük hacim: deniz; hızlı: hava; kapıdan kapıya: kara.','taşıma türlerinin özellikleri')
# ---- 0002
st=[('Süveyş Kanalı, Akdeniz ile Kızıldeniz’i birbirine bağlar.',True,'Süveyş Kanalı Akdeniz ile Kızıldeniz arasındadır'),
    ('Panama Kanalı, Atlas Okyanusu ile Hint Okyanusu’nu birbirine bağlar.',False,'Panama Kanalı Atlas ile Pasifik Okyanusu’nu bağlar'),
    ('Cebelitarık Boğazı, Akdeniz ile Atlas Okyanusu’nu birbirine bağlar.',True,'Cebelitarık Akdeniz ile Atlas’ı bağlar'),
    ('İstanbul Boğazı, Ege Denizi ile Marmara Denizi’ni birbirine bağlar.',False,'İstanbul Boğazı Karadeniz ile Marmara’yı bağlar')]
op,dg=oncul(st,['Yalnız I','Yalnız III','II ve IV','I ve III','I, II ve III'],'D'); assert dg=={'I','III'}
Q.S('0002','K-CGUL-02','orta','Önemli kanal ve boğazların bağladığı su alanlarını doğru eşleştirir.',
 metin_oncul('Kanal ve boğazlarla ilgili olarak',st,'ifadelerinden hangileri doğrudur?'),op,'D',
 'Doğru ifadelerin belirlenmesi.','Her kanal ya da boğazın hangi iki deniz ya da okyanusun arasında olduğunu hatırla.',
 [B('Kanal ve boğazlar','Süveyş Kanalı: Akdeniz – Kızıldeniz · Panama Kanalı: Atlas – Pasifik · Cebelitarık Boğazı: Akdeniz – Atlas · İstanbul Boğazı: Karadeniz – Marmara · Çanakkale Boğazı: Marmara – Ege')],
 [A('Bağlantıları hatırla','Her kanal ve boğazın bağladığı iki su alanını yaz.','Süveyş: Akdeniz–Kızıldeniz · Panama: Atlas–Pasifik'),
  A('Öncülleri sına','I ve III doğrudur; II’de Hint değil Pasifik, IV’te Ege değil Karadeniz olmalıdır.','I: doğru · II: yanlış · III: doğru · IV: yanlış'),
  A('Sonuç','Doğru ifadeler I ve III’tür.','I ve III')],
 'Kanalları bağladıkları iki su alanıyla birlikte ezberle.','kanal–boğaz eşleştirmesi')
# ---- 0003
Q.S('0003','K-CGUL-03','orta','Süveyş Kanalı’nın deniz yollarına etkisini belirler.',
 'Mısır’da açılan Süveyş Kanalı, Akdeniz ile Kızıldeniz’i birbirine bağlamaktadır.\nBu kanalın açılmasıyla aşağıdakilerden hangisi gerçekleşmiştir?',
 [('Karadeniz’e kıyısı olan ülkelerin okyanuslara çıkışı kolaylaşmıştır.',False,'Bu etki Boğazlar’a aittir; Süveyş Kanalı Karadeniz’i bağlamaz.','bilgi'),('Avrupa–Hint Okyanusu arasındaki deniz yolu Ümit Burnu’na göre kısalmıştır.',True,'',''),('Atlas ile Pasifik Okyanusu arasındaki gemi geçişi kolaylaşmıştır.',False,'Bu etki Panama Kanalı’na aittir.','bilgi'),('Avrupa ile Kuzey Amerika arasındaki deniz mesafesi kısalmıştır.',False,'Bu iki kıta arasındaki yol Süveyş’ten geçmez; Atlas Okyanusu üzerindedir.','dikkat'),('Hint Okyanusu çevresiyle yapılan deniz ticareti azalmıştır.',False,'Yol kısalınca bu bölgeyle ticaret azalmaz, kolaylaşır.','dikkat')],'B',
 'Süveyş Kanalı’nın etkisi.','Kanalın bağladığı iki denizi ve bunun hangi rotaları kısaltacağını düşün.',
 [B('Süveyş Kanalı','Akdeniz ile Kızıldeniz’i bağlar. Avrupa ile Hint Okyanusu çevresi arasındaki gemiler Afrika’yı dolaşıp Ümit Burnu’ndan geçmek yerine kanaldan geçer; yol kısalır.')],
 [A('Konumu belirle','Kanal, Akdeniz ile Kızıldeniz arasındadır.','Akdeniz — Kızıldeniz'),
  A('Rotayı yorumla','Avrupa’dan Hint Okyanusu’na gitmek için Afrika’yı dolaşmak gerekmez; mesafe kısalır.','Ümit Burnu rotası > Süveyş rotası'),
  A('Şıkları ele','Karadeniz çıkışı Boğazlar’a, Atlas–Pasifik geçişi Panama’ya aittir.','B: doğru · A, C: başka geçit')],
 'Kanalın bağladığı iki denizi yaz, hangi rotayı kısalttığını oradan çıkar.','Süveyş Kanalı etkisi')
# ---- 0004
d1,d2,v,gun,yk=14400,9600,20,24,30
s1,s2=Fr(d1,v),Fr(d2,v); assert s1==720 and s2==480 and (s1-s2)==240 and (s1-s2)/gun==10 and (s1-s2)/gun*yk==300
assert s2/gun*yk==600 and s1/gun*yk==900
Q.S('0004','K-CGUL-04','zor','İki deniz rotasının mesafe farkından süre ve yakıt tasarrufunu hesaplar.',
 'Bir yük gemisi, iki liman arasında Ümit Burnu rotasını izlediğinde 14 400 km, Süveyş Kanalı rotasını izlediğinde 9 600 km yol yapmaktadır. Gemi her iki rotada da saatte ortalama 20 km hızla gitmekte ve günde 30 ton yakıt tüketmektedir. Gemi gece gündüz hiç durmadan yol almaktadır. Veriler kurgusaldır.\nBuna göre gemi Süveyş Kanalı rotasını kullanırsa toplam kaç ton yakıt tasarrufu sağlar?',
 [('10',False,'Süre farkını (10 gün) yakıt miktarı sanmış; günlük tüketimle çarpmamış.','dikkat'),('240',False,'Süre farkını saat olarak (240) bulup yakıt sanmış; güne çevirmemiş.','islem'),('300',True,'',''),('600',False,'Yalnız kanal rotasının toplam yakıtını (20 gün × 30) bulmuş.','dikkat'),('900',False,'Yalnız uzun rotanın toplam yakıtını (30 gün × 30) bulmuş.','dikkat')],'C',
 'Süveyş rotasının sağladığı yakıt tasarrufu (ton).','Önce iki rotanın süre farkını bul, sonra bu farkı güne çevirip günlük yakıtla çarp.',
 [B('Hız–yol–süre','Süre = yol ÷ hız. Yakıt = gün sayısı × günlük tüketim. Örnek: 100 km yolu saatte 20 km ile giden gemi 5 saat yol alır; günde 24 saat olduğundan 48 saat 2 gün eder.')],
 [A('Mesafe farkı','Uzun rotadan kısa rotayı çıkar.','14 400 − 9 600 = 4 800 km'),
  A('Süre farkı','Mesafe farkını hıza böl, günlere çevir.','4 800 ÷ 20 = 240 saat · 240 ÷ 24 = 10 gün'),
  A('Yakıt tasarrufu','Gün farkını günlük tüketimle çarp.','10 × 30 = 300 ton'),
  A('Şıkları ele','600 ve 900 tek rotanın toplam yakıtıdır; 10 ve 240 yakıt değildir.','C: 300')],
 'Tasarrufu iki rotanın farkından bul; tek rotanın toplamı sorulanı vermez.','kurgusal rota ve hız; kodla doğrulandı')
Q.bitir()
