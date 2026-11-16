# TYT Biyoloji genişletme · üretici ortak talimatı (hafif mod, 17 Kasım 2026)
Depo: /home/claude/zekacademy-app/havuz (git commit/push YOK, GitHub YOK, artifact YOK).
Önce sırayla oku: `URETIM.md` (kardeş kuralları HARİÇ), `URETIM-DERSLER.md`, `URETIM-OSYM-PROFIL.md`, `URETIM-SEKIL.md`, `arac/MAT-ORTAK.md` (genel kurallar ve sondaki şekil dersleri), `arac/KIM-ORTAK.md` İÇİNDEKİ "İlk kimya dalgasından dersler" ve `arac/FIZ-ORTAK.md` İÇİNDEKİ "İlk dalgadan dersler" bölümleri (biyolojide de aynen geçerli), `tyt-bio/_hafif_bio.py` (kart(), mk(), bitir(), fm(), tikz_svg, tablo_svg), `cizim.py`, ÖRNEK betikler `tyt-bio/uret-biopilot.py` (hücre, ozmoz, soy ağacı, besin ağı, bölünme evreleri, enzim grafiği çizimleri) ve `tyt-kim/uret-asitbaziki.py` (mk/bitir düzeni; `from _hafif_bio import *`), konunun mevcut `tyt-bio/uret-<konu>.py` betiği + `<konu>-1.json`, `<konu>-1-kardes.json` ve `biopilot-1.json` soruları (kurgu tekrarlama).
## ÖSYM biyoloji profili (zorunlu; `denetle.py --profil` ölçer)
- **Görsel ≥ %45** (koç isteği: şekli artır; ÖSYM ≥%33). Doğal görseller: hücre ve organel şemaları (biçimle ayırt edilen yapılar; renk cevabı vermesin), madde geçişi düzenekleri (U borusu/osmometre, hücre hacmi–zaman grafiği), enzim/sıcaklık/pH grafikleri, deney düzeneği ve sonuç tablosu, soy ağacı, çaprazlama (Punnett) tablosu, kromozom/hücre evreleri çizimi, DNA–kromozom miktarı grafikleri, besin zinciri/ağı, besin piramidi, madde döngüleri (karbon, azot, su — şematik), popülasyon grafiği, sınıflandırma tablosu/dallanma şeması, canlı özellikleri tablosu.
- **Öncüllü ~%35–45**; **olumsuz kök ~%20–30** (değildir, yanlıştır, söylenemez, beklenmez, gözlenmez…; çift olumsuz yok); **kök medyanı 35–60 kelime**.
- Harfler dengeli; öncüllü şık sırası alışılmış.
## Doğruluk
- TYT = MEB 9. ve 10. sınıf biyolojisi (2024 programı dahil yaygın içerik). Kapsam DIŞI (AYT/11–12): sinir, sindirim, dolaşım sistemleri ayrıntısı, hormonlar, fotosentez/solunum tepkime basamakları (ışık-karanlık evre ayrıntısı, Krebs), protein sentezi aşamaları (transkripsiyon/translasyon ayrıntısı), bitki biyolojisi ayrıntısı, genetik mühendisliği ayrıntısı. TYT'de fotosentez ve solunum yalnız genel denklem/ATP/enerji dönüşümü düzeyinde; DNA yapısı ve replikasyon temel düzeyde.
- Bilgi yalnız MEB lise kitabında yer alan, tartışmasız gerçekler; tarih/isim/örnek iki kez kontrol. Tartışmalı sınıflandırma (ör. protista ayrıntıları) varsa soruyu kurma.
- Sayısal sorular (kalıtım olasılıkları, gamet çeşidi, DNA nükleotit sayıları, kromozom/DNA miktarları, besin piramidinde enerji aktarımı %10, popülasyon büyüme) Python'da (Fraction / tarama) hesaplanıp her cevap ve çeldirici DEĞERİ assert edilir. Kalıtımda olasılıklar Punnett/tarama ile.
- Öncüllü/nitel sorularda her öncülün doğru/yanlış değeri betikte TEK yerde tanımlanır; anahtar, adımlar ve çeldirici açıklamaları oradan üretilir. Adımlarda şık harfi yazma. "Kesinlikle" köklerinde "olabilir/kesin" ayrımı ve tüm olasılıklar betikte taranır.
- Çeldirici = gerçek kavram yanılgısı (ör. "bitkiler solunum yapmaz", "mitoz yalnız eşeysiz üremede", "baskın gen her zaman sık görülür", "virüsler canlıdır", "enzim tepkimede harcanır").
- Deney sorularında bağımlı/bağımsız/kontrol değişkeni ve kontrol grubu doğru kurulsun.
## Kaynak (yalnız mantık kartı; metin/sayı/şekil kopyalama YOK)
- ÖSYM: `/home/claude/kutup/dersler/osym_biyoloji.txt` (ilk sayfalarda konu dağılım tablosu).
- Yayın: `/home/claude/kutup/biyoloji/yayin_palme.txt` (Palme TYT Biyoloji, yazı tanıma ile çıkarıldı; hatalı karakterler olabilir; sayfalar `\f` ile). Dosya henüz yoksa ÖSYM ve MEB bilgisiyle başla, birkaç dakika sonra tekrar bak.
## Dosyalar
`tyt-bio/uret-<onek>.py` → `tyt-bio/<onek>-1.json`, kartlar `kartlar/<onek>.json` (kart kimliği öneki görevde; çakışma için `grep -h '"id"' kartlar/*.json`). Konu adı ve uygulama anahtarı mevcut `<konu>-1.json` ile AYNEN. Zorluk ≈ %25 kolay, %50 orta, %20–25 zor. Tip sayısı 5–8. Kardeş yok, ipucu 1.
## Denetim
`python3 denetle.py tyt-bio/<onek>-1.json --profil --benzerlik /home/claude/kutup/dersler/osym_biyoloji.txt` (+ yayın dosyası varsa ekle) → 0 HATA (0,15 üstü benzerlik uyarısında kurguyu değiştir); mevcut aynı konu dosyalarıyla birlikte de 0 HATA. PNG: `python3 kalite.py tyt-bio/<onek> <onek>` → `/tmp/kor/tytbio-<onek>-00NN.png`; HER PNG'yi Read ile aç (okunaklılık ≥ 11 px, biyolojik doğruluk: organel biçimleri, kromozom sayıları, evre sırası, soy ağacı sembolleri — kare erkek, daire dişi, dolu = özelliği gösteren; grafik biçimi; metinle tutarlılık; cevabı ele vermeme), gerekeni düzelt. SVG ≤ 40 KB. hazirla.sh ÇALIŞTIRMA.
Rapor KISA (en çok 10 satır): soru sayısı, zorluk, harf, görsel/öncüllü/olumsuz kök oranı, emin olmadıkların.
## Düzeltme turu notu (17 Kasım)
- Biyolojide olumsuz kök hedefi ÖSYM'ye göre ~%20–30'dur; doğrulayıcının "%10" önerisini UYGULAMA (olumsuz kökleri azaltma).
- Bilgi kartı (`bilgi`) yalnız genel kavramı anlatır; sorudaki canlı, sayı, öncül ya da sonucu içeremez. İpucu yalnız yön verir ("neye bak?"), sonucu söylemez. Bu en sık bulgu oldu.
- Aynı şekil türü pakette en çok 3; fazlası metne/başka görsele çevrilir. Yazılar ≥ 11 px.
