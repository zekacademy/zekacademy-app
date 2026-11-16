# Matematik genişletme · üretici ortak talimatı (hafif mod)
Depo: /home/claude/zekacademy-app (git commit/push YOK, GitHub YOK, artifact YOK).
Önce oku: havuz/URETIM.md (kardeş kuralları HARİÇ), havuz/tyt-mat/_hafif_mat.py (kart(), mk(), bitir()), ÖRNEK betikler havuz/tyt-mat/uret-bolme.py ve uret-oraniki.py (aynı biçim: assert'ler, anlatım dili).
Kurallar:
- Kardeş YOK, ipucu tam 1 (yönlendirir, cevabı ve anahtar fikri söylemez).
- **ŞEKİL:** önce `havuz/URETIM-SEKIL.md` dosyasını oku ve uygula. Paketteki şekilli + grafik + tablo sorularının payı o dosyadaki hedef orana ulaşmalı (matematikte en az %25–30). Çizim `havuz/cizim.py` → `tikz_svg`, tablo `tablo_svg`; her şeklin PNG'sine Read ile bakmak zorunlu.
- Her doğru cevap Python'da (Fraction / tarama) hesaplanıp assert edilir; her çeldirici DEĞERİ de açıklamasındaki hatadan hesaplanıp assert edilir. Çeldirici = gerçek öğrenci hatası (yapay "±1", "yarısı" yok).
- Konu adı ve uygulama anahtarı mevcut dosyadakiyle AYNEN. Mevcut soruları oku, kurgu ve sayı yapısını TEKRARLAMA; kendi dosyanda da aynı kurguyu iki kez kullanma (otobüs, ikramiye, havuz… her biri bir kez).
- Soru metni tek anlamlı: koşullar eksiksiz ("sabit hızla", "eşit kapasiteli", "pozitif tam sayı", "0 dahil doğal sayı", aralık uçları, "başka ekleme yapılmamıştır"). Gerçekçi kurgu ve sayılar; Türkçesi doğal; ÖSYM üslubu ("Buna göre, … kaçtır?").
- Zorluk ÖSYM TYT düzeyi; "zor" gerçekten 4+ adım / iki koşullu, etiketi şişirme; tek adımlı soru "kolay".
- TYT DIŞI YOK: ikinci dereceye indirgeme gerektiren üslü denklem, iç içe kök açma, geometrik ortalama, üçlü içerme-dışarma, logaritma, türev, x⁴+1/x⁴ türü, ikinci derece denklem formülü (basit çarpanlara ayırma olabilir).
- Kalıp etiketi doğru: 'hikâyeli' (günlük bağlam), 'yeni nesil' (yalnız tanımlı kavram/işlem/kural), 'öncüllü' (I-II-III; şık sırası: Yalnız I, Yalnız II, I ve II, I ve III, I, II ve III ya da benzeri alışılmış sıra; doğru kümeler sorudan soruya değişsin), 'düz', 'tablo'.
- Cevap harfleri dengeli (her harf ±2). Sayısal şıklar küçükten büyüğe (yardımcı sıralar).
- Kaynak (yalnız mantık kartı; metin/sayı kopyalama yok): /home/claude/kutup/sorular.json (liste: kitap,sayfa,no,konu,metin; konu grubu + anahtar kelimeyle süz), havuz/osym-harita.json (konu profili, mantik_aileleri), /home/claude/kutup/osym_metin.json.
- Denetim: `python3 havuz/denetle.py havuz/tyt-mat/<onek>-1.json --benzerlik /home/claude/kutup/osym_metin.json /home/claude/kutup/sorular.json` → 0 HATA (0,15 üstü benzerlik uyarısında kurguyu değiştir); ayrıca mevcut dosyalarla birlikte çalıştırıp havuz içi tekrar HATA'sı olmadığını gör.
- Bitince kısa rapor: sayı, zorluk, harf dağılımı, kartlar, "emin olmadıklarım".
- EK (12 Kasım): ipucu anahtar fikri söylemesin; `adimSayisi` = adım listesinin uzunluğu; sayılar/fiyatlar/hızlar gerçekçi; derişimlerde "kütlece/hacimce" açık. Çeldirici açıklaması o değeri TEK tutarlı hata zinciriyle üretsin (öncüllülerde: hangi öncül neden doğru/yanlış sanıldı). Metin içinde boru (|) işaretli tablo YASAK: tablo gerekiyorsa `from _hafif_mat import tablo_svg` → `sekil=tablo_svg(['Başlık1','Başlık2'],[['a','b'],...])`, metinde "aşağıdaki tabloda" de, kalıp 'tablo'.

## Şekilli ek paketleri için dersler (15 Kasım, sek1 turundan)
- Şekil VERİ taşır: şekilde verilen sayı metinde tekrar edilmez; şekil çıkarılınca soru çözülemiyor olmalı. Süs şekil yasak.
- Şekil ölçekli çizilince cevabı gözle ele veriyorsa (sayı doğrusunda nokta yeri, ibre) şematik çiz ya da soruyu değiştir.
- Yazılar 500 px genişlikte en az 11–12 px; küçük nesneler (kap, nokta, diş) iri çizilir; okunacak uçlar kılavuz çizgiyle bir bölme çizgisine oturur. Dosya 40 KB'ı geçmesin (tarama deseni yerine düz dolgu).
- Nesne ne ise şekilde/lejantta yazsın ("● : 1 kalem"); metindeki sözcük ile şekildeki nesne aynı olsun.
- "bilgi" örneği sorunun kendi sayılarıyla yazılmaz (cevap zincirini sızdırır).
- Çeldiriciler metindeki bir koşulla hesapsız elenmesin (ör. kapasiteyi aşan değer).
- Aynı pakette aynı şekil türü en çok 2 kez; aynı kurgu 1 kez.
- Kurgu kendi içinde tutarlı: kapasite aşılmaz, sıra belirsiz kalmaz.
- (16 Kasım) Şekilli problem sorularında da kalıp etiketi doğru: günlük bağlamlı soru 'hikâyeli' (şekli olsa da; şekil `sekil` alanında zaten sayılır), tanımlı işlem/kural 'yeni nesil', grafik okuma 'grafik', tablo 'tablo'. Kök medyanı 40–65 kelime: gerçek bir durum anlat, süs cümlesi yok.
