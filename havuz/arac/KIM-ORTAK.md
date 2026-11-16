# TYT Kimya genişletme · üretici ortak talimatı (hafif mod, 17 Kasım 2026)
Depo: /home/claude/zekacademy-app/havuz (git commit/push YOK, GitHub YOK, artifact YOK).
Önce sırayla oku: `URETIM.md` (kardeş kuralları HARİÇ), `URETIM-DERSLER.md`, `URETIM-OSYM-PROFIL.md`, `URETIM-SEKIL.md`, `arac/MAT-ORTAK.md` (genel kurallar ve sondaki şekil dersleri), `arac/FIZ-ORTAK.md` İÇİNDEKİ "İlk dalgadan dersler" bölümü (kimyada da aynen geçerli), `tyt-kim/_hafif_kim2.py` (kart(), mk(), bitir(), fm(), tikz_svg, tablo_svg), `cizim.py`, ÖRNEK betikler `tyt-fiz/uret-fizpilot.py` ve `tyt-fiz/uret-isiiki.py` (aynı mk/bitir düzeni; `from _hafif import *` yerine `from _hafif_kim2 import *`) ve konunun mevcut `tyt-kim/uret-<konu>.py` betiği + `<konu>-1.json` soruları (kurgu tekrarlama).
## ÖSYM kimya profili (zorunlu; `denetle.py --profil` ölçer)
- **Görsel ≥ %40** (koç isteği: şekli artır; ÖSYM ≥%16 ama tablolar sayılamadı). Kimyada doğal görseller: tablo (madde–özellik, deney sonuçları, kütle/mol verileri, periyodik tablo kesiti), tanecik modeli (kapta atom/molekül çizimi; karışım/saf madde, hâl, çözelti), grafik (ısıtma–soğutma, çözünürlük–sıcaklık, kütle–kütle, pH ölçeği, iyonlaşma enerjisi), deney düzeneği (ayırma: damıtma, süzme, ayırma hunisi; iletkenlik deneyi; çözünme), Lewis/nokta yapısı (TikZ ile elle), periyodik tablo kesiti (gruplar/periyotlar, harfli elementler), Bohr modeli/katman diyagramı, uyarı işaretleri (şematik).
- **Öncüllü ~%35–45**; **olumsuz kök ~%10** (yanlıştır, değildir, söylenemez…; çift olumsuz yok); **kök medyanı 45–70 kelime** (gerçek deney/gözlem/günlük durum).
- Sayısal şıklar küçükten büyüğe; öncüllü şık sırası alışılmış; harfler dengeli.
## Doğruluk
- TYT = MEB 9–10. sınıf kimyası. Kapsam DIŞI (AYT): orbital/kuantum sayıları, elektron dizilimi s-p-d (TYT'de yalnız katman/Bohr modeli ve basit katman dağılımı), hibritleşme, molekül geometrisi VSEPR, gaz yasaları hesabı (PV=nRT), kimyasal denge, tepkime hızı, Kc, pH hesabı (log), elektrokimya, organik adlandırma ayrıntısı, derişimde molalite.
- Her sayısal cevap ve her çeldirici DEĞERİ Python'da (Fraction) hesaplanıp assert edilir; atom kütleleri metinde verilir (H=1, C=12, N=14, O=16, Na=23, Mg=24, Al=27, S=32, Cl=35,5 vb. gerçek yuvarlanmış değerler). Mol, Avogadro (N_A metinde: 6,02·10²³ ya da sadeleştirilmiş "N_A"), kütlenin korunumu, sabit oranlar, katlı oranlar, tepkime denkleştirme, sınırlayıcı bileşen, verim, % derişim, ppm hesapları.
- Öncüllü/nitel sorularda her öncülün doğru/yanlış değeri betikte TEK yerde tanımlanır; anahtar, adımlar ve çeldirici açıklamaları oradan üretilir. Kimyasal gerçekler yalnız MEB 9–10 kitabındaki tartışmasız bilgiler (iyonik/kovalent, polar/apolar, hidrojen bağı, fiziksel/kimyasal değişim, karışım ayırma, asit–baz–tuz özellikleri, günlük kimya). Kimyasal formüller doğru (mhchem: `\ce{H2SO4}` TikZ içinde; düz metinde Unicode alt simge: H₂SO₄).
- Çeldirici = gerçek kavram yanılgısı (ör. "erime kimyasal değişimdir", "her iyonik bileşik suda çözünür", "kovalent bağ yalnız ametaller arasında olur" gibi ince durumlar, "atom numarası kütle numarasıdır", katsayıyı alt simgeyle karıştırma).
- Güvenlik: tehlikeli madde üretimi/karışımı tarifi yok; güvenlik işaretleri ve laboratuvar kuralları sorulabilir.
## Kaynak (yalnız mantık kartı; metin/sayı/şekil kopyalama YOK)
- ÖSYM: `/home/claude/kutup/dersler/osym_kimya.txt` (ilk sayfalarda konu dağılım tablosu).
- Yayın: `/home/claude/kutup/kimya/yayin_miray.txt`, `/home/claude/kutup/kimya/yayin_orbital.txt` (sayfalar `\f` ile; konunu anahtar sözcükle ara, soru tiplerinin MANTIĞINI çıkar).
## Dosyalar
`tyt-kim/uret-<onek>.py` → `tyt-kim/<onek>-1.json`, kartlar `kartlar/<onek>.json` (kart kimliği öneki görevde verilir; çakışma için `grep -h '"id"' kartlar/*.json`). Konu adı ve uygulama anahtarı mevcut `<konu>-1.json` ile AYNEN (ilk sorunun `konu` ve `k`/`uygulamaKonu` alanına bak). Zorluk ≈ %25 kolay, %50 orta, %20–25 zor. Kardeş yok, ipucu 1.
## Denetim
`python3 denetle.py tyt-kim/<onek>-1.json --profil --benzerlik /home/claude/kutup/dersler/osym_kimya.txt /home/claude/kutup/kimya/yayin_miray.txt /home/claude/kutup/kimya/yayin_orbital.txt` → 0 HATA (0,15 üstü benzerlik uyarısında kurguyu değiştir); mevcut aynı konu dosyasıyla birlikte de 0 HATA. PNG: `python3 kalite.py tyt-kim/<onek> <onek>` → `/tmp/kor/tytkim-<onek>-00NN.png`; HER PNG'yi Read ile aç (okunaklılık, kimyasal doğruluk: formül, yük, tanecik sayısı, grafik eğimi; metinle tutarlılık; cevabı ele vermeme), gerekeni düzelt.
Rapor KISA (en çok 12 satır): soru sayısı, zorluk, harf, görsel/öncüllü/olumsuz kök oranı, emin olmadıkların.
## İlk kimya dalgasından dersler (17 Kasım; doğrulayıcı bulguları)
- Şık harfine bağlı adım metni YAZMA ("E yanlış" gibi): mk() şıkları sıraladığı için harf kayar → adımlar cevapla çelişti (3 soruda). Adımlarda şık içeriğini ya da öncül numarasını an.
- Bilgi kartı (`bilgi`) ve ipucu cevabı/anahtar fikri vermesin; kart örneği sorudaki madde/sayılarla aynı olmasın (en sık bulgu).
- Tip sayısı: pakette 5–8 tipId (her soruya ayrı tip açma); benzer sorular aynı tipte.
- Zorluk: tek bilgi/tek okuma = kolay; "zor" yalnız çok adımlı/iki koşullu; pakette %20–25.
- Aynı şekil türü (ör. periyodik tablo kesiti, kaynama grafiği) en çok 3 kez; aynı kurgu bir kez. Şekildeki tüm yazılar ≥ 11 px (grup başlıkları dahil); okunacak değerler eksen çentiğine/kılavuza otursun.
- Fiziksel/kimyasal gerçekçilik: ısıtma grafiğinde eğimler öz ısıyla, platolar erime/buharlaşma ısısıyla orantılı; elementler gerçek (soy gaza iyon yükü verme).
- Konu dışına taşma: başka TYT konusunun hesabı (ör. etkileşim konusunda mol hesabı) o konunun paketine girmez. İdeal/gerçek gaz sapması, bağ enerjisiyle net tepkime ısısı hesabı TYT dışı.
- Olumsuz kökte ("yanlıştır") çeldirici açıklamalarının yönü ters dönmesin: o şıkkı seçen öğrencinin hatası yazılır.
