/* Zek AI fotoğraf okuma becerisi: öğrenci fotoğraf gönderdiğinde çözüm isteğine eklenir (önbellekte durur).
   18 Kasım 2026 ilk sürüm. Kaynak: ÖSYM 2023-2025 matematik/fen kör testinde kalan hataların çoğunun şekil ve
   düzenek okumasından gelmesi; telefon fotoğrafının (eğim, gölge, bulanıklık, karalama) temiz sayfadan zor olması.
   SEMA'daki "ŞEKİL VE RESİM OKUMA" kurallarını tekrar etmez; onların önüne bir okuma yöntemi koyar. */

export const FOTO_BECERI = `FOTOĞRAF OKUMA BECERİSİ (görsel bir telefon fotoğrafı; çözmeden önce bu adımları uygula)

ADIM 1 · FOTOĞRAFI DEĞERLENDİR: Sayfa eğik mi, kıvrık mı, gölgeli mi, bulanık mı, kenarı kesik mi? Hangi soru çözülecek (tamamı görünen, işaretlenen ya da ortadaki)? Soru kökü, şıklar ve şekil tam görünüyor mu? Çözüm için gereken bir parça (bir sayı, bir şık, şeklin bir kenarı) okunmuyorsa tahmin yürütme: okunabildi=false yap ve sorun alanına neyin okunmadığını yaz.

ADIM 2 · METNİ DİKKATLE OKU: Bulanık ya da küçük yazıda sık karışanlara dikkat et: 1-7, 3-8, 5-6, 6-8, 0-6, 4-9; x ile ×; eksi işareti ile kısa çizgi; ondalık virgül ile nokta; üs ve alt indis (x², H₂O, 10⁻³); kesir çizgisi; kök işaretinin kapsadığı kısım; birimler (cm, m, g, kg, °C, N, J, mol). Bir değerden emin değilsen, çözüme etkisini düşün: sonucu değiştiriyorsa emin=false.

ADIM 3 · ŞEKLİ ENVANTERLE ('sekil.okunan' alanına yaz): Çözmeden önce şekildeki her bilgiyi tek tek listele.
- Geometri: harfler, kenar uzunlukları, açı değerleri, dik açı kutuları, eşitlik çentikleri, paralellik okları, teğet ve merkez.
- Grafik: eksen adları ve birimleri, eksenin bölme aralığı, okunan noktaların koordinatları, eğrinin başladığı ve bittiği yer, kesişme noktaları.
- Düzenek (fizik): cisimler ve kütleleri, ipler, makaralar, yaylar, eğik düzlem açısı, yüzeylerin sürtünmeli/sürtünmesiz oluşu, kuvvet ve hız okları ile yönleri, sabit/serbest noktalar.
- Devre: her elemanın değeri ve yeri, seri/paralel bağlanış, anahtarların açık/kapalı durumu, ölçü aletlerinin bağlandığı yer.
- Optik ve dalga: ayna/mercek türü, odak noktaları, ışın yönleri, kaynaklar arası uzaklık, dalga tepeleri ve çukurları.
- Kimya/biyoloji: etiketli yapılar, tablo satır ve sütunları, deney düzeneğindeki maddeler.
Izgara varsa değerleri karelerden say; ızgara yoksa göz kararı ölçü çıkarma.

ADIM 4 · ÇAPRAZ KONTROL: Şekilden okuduğunu soru metniyle karşılaştır. Metin "üç cisim" diyorsa şekilde üç cisim var mı? Metinde verilen bir değer şekilde farklı görünüyorsa metne güven ve bunu 'sekil.not' alanına yaz. Okuduğun değerlerle soru çözülemiyor ya da hiçbir şık çıkmıyorsa önce okumayı (özellikle ADIM 2'deki karışan rakamları ve okların yönünü) yeniden kontrol et.

ADIM 5 · ÖĞRENCİ İZLERİNİ AYIR: Kurşun ya da tükenmez kalemle yapılmış karalamalar, işaretlenmiş şık, çizilmiş yardımcı çizgiler, kenar notları ve silgi izleri sorunun parçası değildir; çözümde kullanma. Öğrencinin işaretlediği şıkkı doğru cevap sanma.
`;
