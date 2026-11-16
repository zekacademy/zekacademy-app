# TYT Fizik genişletme · üretici ortak talimatı (hafif mod, 16 Kasım 2026)
Depo: /home/claude/zekacademy-app/havuz (git commit/push YOK, GitHub YOK, artifact YOK).
Önce sırayla oku: `URETIM.md` (kardeş kuralları HARİÇ), `URETIM-DERSLER.md`, `URETIM-OSYM-PROFIL.md`, `URETIM-SEKIL.md`, `arac/MAT-ORTAK.md` (genel kurallar ve sondaki şekil dersleri fizikte de geçerli), `tyt-fiz/_hafif.py` (kart(), mk(), bitir(), fm()), `cizim.py` (tikz_svg), ÖRNEK betik `tyt-fiz/uret-fizpilot.py` (TikZ ile düzenek, devre, optik, grafik) ve konunun mevcut `tyt-fiz/uret-<konu>.py` betiği.
## ÖSYM fizik profili (zorunlu hedefler; `denetle.py --profil` ölçer)
- **Görsel ≥ %74:** sorularının en az dörtte üçü `sekil` taşır (düzenek, devre, ışın çizimi, grafik, tablo). Şekil veri taşır; metin şekli tekrar etmez. Devre `circuitikz` (tikzpicture içinde), grafik `pgfplots`.
- **Öncüllü %40–60:** "Buna göre, I. … II. … III. … yargılarından hangileri doğrudur?" Şıklar: Yalnız I / Yalnız II / I ve II / I ve III (ya da II ve III) / I, II ve III; doğru küme sorudan soruya değişir.
- **Kök uzunluğu:** medyan 60–100 kelime; gerçek bir deney/düzenek/günlük durum anlat (süs cümlesi yok).
- Olumsuz kök neredeyse yok. Sayısal şıklar küçükten büyüğe. Harfler dengeli.
## Doğruluk
- TYT = MEB 9–10. sınıf fiziği. Kapsam DIŞI (AYT): atışlar, çembersel hareket, tork-denge hesapları, momentum, basit harmonik hareket, elektriksel alan/potansiyel hesabı, manyetik kuvvet formülleri, indüksiyon, modern fizik, mercek/ayna formülüyle hesap (TYT'de çizim ve nitel özellik), Snell yasasıyla sinüslü hesap.
- Her sayısal cevap ve her çeldirici DEĞERİ Python'da (Fraction) hesaplanıp assert edilir; birimler tutarlı (g = 10 m/s² metinde yazılır). Nitel/öncüllü sorularda her öncülün doğruluğu betikte yorum + mümkünse hesapla gerekçelendirilir; iki savunulabilir cevap bırakma. Sürtünme, hava direnci, ısı alışverişi, ideal tel/makara, özdeş lamba/direnç gibi koşullar metinde açık.
- Çeldirici = gerçek kavram yanılgısı (ör. "ağır cisim daha hızlı düşer", "akım lambada harcanır", "basınç = kuvvet", "ısı = sıcaklık").
- Fiziksel gerçekçilik: özkütleler, özısılar, dirençler, hızlar gerçek dünyaya uygun.
## Kaynak (yalnız mantık kartı; metin/sayı/şekil kopyalama YOK)
- ÖSYM: `/home/claude/kutup/dersler/osym_fizik.txt` (ilk sayfalarda konu dağılım tablosu).
- Yayın: `/home/claude/kutup/fizik/yayin_fizikpedia.txt` (sayfalar `\f` ile ayrılır; konunu anahtar sözcükle ara, soru tiplerinin MANTIĞINI çıkar).
## Dosyalar
`tyt-fiz/uret-<onek>.py` → `tyt-fiz/<onek>-1.json`, kartlar `kartlar/<onek>.json` (kart kimlikleri mevcutlarla çakışmasın: önce `grep -h '"id"' kartlar/*.json` ile bak). Konu adı ve uygulama anahtarı mevcut dosyadakiyle AYNEN. Mevcut soruları (`<konu>-1.json`, `-kardes`, `fizpilot-1.json`) oku; kurgu tekrarlama.
Zorluk ≈ %25 kolay, %50 orta, %25 zor. Kardeş yok, ipucu 1.
## Denetim
`python3 denetle.py tyt-fiz/<onek>-1.json --profil --benzerlik /home/claude/kutup/dersler/osym_fizik.txt /home/claude/kutup/fizik/yayin_fizikpedia.txt` → 0 HATA (benzerlik uyarısı 0,15 üstüyse kurguyu değiştir); mevcut aynı konu dosyalarıyla birlikte de 0 HATA. PNG: `DERS=tyt-fiz bash arac/hazirla.sh gecici_<onek> <onek>` → `/tmp/kor/tytfiz-<onek>-00NN.png`; HER PNG'yi Read ile aç (okunaklılık, metinle tutarlılık, fiziksel doğruluk: ok yönleri, ışın açıları, devre bağlantıları, cevabı ele vermeme), gerekeni düzelt.
Rapor KISA (en çok 12 satır): soru sayısı, zorluk, harf, görsel/öncüllü oranı, emin olmadıkların.
## İlk dalgadan dersler (16 Kasım; doğrulayıcı bulguları)
- Öncüllü soruda adım açıklaması doğru kavramı anlatır; çeldirici dilini ("…sanmış") adımlara kopyalama. Her öncülün doğru/yanlış değeri betikte TEK yerde tanımlanır; adımlar, çeldirici açıklamaları ve anahtar oradan üretilir (bir soruda adım "II yanlış" derken açıklaması doğru diyordu → anahtar hatası).
- "Kesinlikle doğru" köklerinde bütün olası durumları betikte tara; ikinci savunulabilir cevap kalmasın. Şekilde çizili nesne ile metindeki "diğer/en çok kaç" ifadesi sayım belirsizliği yaratmasın.
- Metin cevabı ele vermesin ("hızı sabitleniyor", "üç yolu da hedefler" gibi cümleler öncülü söyler).
- Kuvvet/hız oklarının boyu büyüklükle orantılı; eşit kuvvetler eşit boyda; oklar cisme değer. Dengedeki cisimde zıt oklar eşit.
- Kurgu fiziksel olarak mümkün olsun (yaylı araba sabit ivmeyle gitmez; çatıdan düşen cisim limit hıza ulaşmaz → helikopter/paraşüt).
- Öncüllü şık sırası hep alışılmış: Yalnız I, Yalnız II, (Yalnız III), I ve II, I ve III, II ve III, I, II ve III içinden beşi bu sırayla. Harf dengesi için sırayı bozma; doğru kümeyi değiştir.
- Bilgi kartı örneği sorunun sayılarını/cevabını ya da komşu sorunun cevabını tekrar etmez.
- "zor" yalnız gerçekten çok adımlı/iki koşullu soruda; paket başına en çok %20–25.
- Kalıp etiketi: şekli grafik olan 'grafik', tablo olan 'tablo'. Aynı şekil türü (ör. F–x grafiği) pakette en çok 2 kez.
- SVG ≤ 40 KB (130–170 KB çıkanlar oldu: desen/çok küçük parçalı çizimden kaçın, gereksiz düğüm metni azalt). Şekil tuvali içeriğe sıkı otursun (sağ yarısı boş PNG olmasın).
- Sayısal yay enerjisi (½kx²) hesabı isteme; gerekirse enerjiyi doğrudan ver.
