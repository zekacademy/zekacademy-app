# AYT Fizik — üretim kuralları (hafif mod)

TYT fizik kurallarının hepsi geçerli: önce `arac/FIZ-ORTAK.md`'yi oku (oradaki okuma listesi, ÖSYM fizik profili, doğruluk kuralları ve "İlk dalgadan dersler" dahil; yalnız TYT kapsam/kaynak/dosya satırları aşağıdakilerle değişir). Örnek betik ve yardımcılar: `tyt-fiz/_hafif.py`, `tyt-fiz/uret-fizpilot.py`, `cizim.py` (TikZ: circuitikz, pgfplots). AYT'ye özel farklar:

## Kimlik ve alanlar
- Klasör `ayt-fiz/` (yoksa oluştur). Betik `ayt-fiz/uret-<onek>.py` → `ayt-fiz/<onek>-1.json`, kartlar `kartlar/af<onek>.json` (TYT kart dosyalarıyla çakışmasın diye `af` ön eki).
- `id`: `aytfiz-<onek>-00NN`. `ders`: `"AYT Fizik"`. `k`: `"afiz|<konu adı>"`; konu adı uygulamadaki listeyle BİREBİR (prompttaki ad).
- Kart öneki `K-AF<HARFLER>-NN`; `grep -h '"id"' kartlar/*.json` ile boş olduğunu kontrol et.

## Kapsam ve düzey
- MEB 11–12. sınıf fizik (AYT). Konunun ÖSYM AYT'de gerçekten sorulan kazanımları; TYT düzeyinde kalan basit sorular en fazla 3.
- Paket 20 soru: zorluk **3 kolay / 11 orta / 6 zor**. Zor = ÖSYM AYT gibi iki kavramı birleştiren, çok adımlı; etiketi şişirme.
- Cevap harfleri A–E dörder. 6–10 tipId. Öncüllü %30–50 (ÖSYM AYT fizikte TYT'den biraz az).
- **Şekil ≥ %70**, renkli ve ÖSYM sadeliğinde: düzenek, kuvvet/hız vektörleri, grafik (x–t, v–t, a–t, F–x, E–t…), devre, alan çizgileri, dalga leğeni, enerji seviyeleri. Okların boyu büyüklükle orantılı, ızgara/etiketle okunan her değer net. Renk tek başına bilgi taşımasın (etiket de olsun). Yazı ≥ 11 px.
- ÖSYM dili: bilgi önce, soru en sonda ("Buna göre, … kaçtır?"); gereksiz hikâye yok; sayılar temiz, sonuç sade; sayısal şıklar küçükten büyüğe. g = 10 m/s², sin37 = 0,6 gibi değerler metinde verilir. Sürtünme/hava direnci/ideal makara koşulları açık.
- Her cevap ve çeldirici Python'da (Fraction/sympy) hesaplanıp `assert` edilir; vektör ve grafik sorularında şekildeki ızgaradan okunan değerler de betikte aynı veriden üretilir.
- Modern fizik konularında hesap kadar kavram/öncül soruları da ÖSYM'deki gibi olsun; bilimsel doğruluk tartışmasız.

## Kaynak (yalnız mantık kartı, metin/sayı/şekil kopyalanmaz)
- ÖSYM AYT sayısal çıkmışlar (2018–2025): `/home/claude/kutup/ayt/osym_ayt_sayisal.txt` — ÖNCE BUNU İNCELE: "FİZİK" bölümlerinden konunun sorularını bul, en az 8 tanesini oku; kalıpları, şekil türlerini, zorluğu not et; paketin kurgu dağılımını buna göre kur.
- 345 AYT Fizik Soru Bankası, her 3. sayfanın yazı tanıma çıktısı: `/home/claude/kutup/ayt/yayin_345_ayt_fiz.txt` ("=== s<sayfa>"); sayfa resimleri `/home/claude/kutup/ayt/jfiz/f345_<sayfa>-<3 hane>.jpg` (`ls` ile bul). Yaklaşık sayfalar: Vektör 7–20, Bağıl 22–27, Newton 28–50, İvmeli/Atış 52–96, Enerji 97–117, Momentum 118–144, Tork/Denge/Ağırlık M./Basit Mak. 145–190, Elektrik alan–Sığa 190–240, Manyetizma–İndüksiyon 220–249, Çembersel/Kütle Çekim/BHH 250–300, Dalga 301–330, Modern fizik 331–392. Konunun 2–3 sayfa RESMİNE Read ile bak (şekil ve kurgu stili).
- Bilgi Sarmal AYT Fizik Denemeleri (metin): `/home/claude/kutup/ayt/yayin_bs_ayt_fiz.txt` — konunu anahtar sözcükle ara; en zor kurguları seç.

## Bitiş
- `python3 denetle.py ayt-fiz/<onek>-1.json --benzerlik /home/claude/kutup/ayt/osym_ayt_sayisal.txt /home/claude/kutup/ayt/yayin_bs_ayt_fiz.txt` → 0 HATA (benzerlik 0,15 üstü uyarıda kurguyu değiştir).
- `python3 kalite.py ayt-fiz/<onek> <onek>` → `/tmp/kor/aytfiz-<onek>-00NN.png`; şekilli olanların HEPSİNE Read ile bak ve düzelt (ok yönleri, açı, devre bağlantısı, okunan değerler, cevabı ele vermeme).
- Çalışma dosyaların yalnız kendi scratchpad alt klasöründe. hazirla.sh, git, GitHub'a dokunma.
- Rapor EN FAZLA 3 satır: dosya, zorluk/şekil/öncüllü dağılımı, varsa sorun.
