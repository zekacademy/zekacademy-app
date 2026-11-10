# Paragraf genişletme talimatı (TYT Türkçe · koç onayı 10 Kasım 2026)

Önce `havuz/URETIM.md` ve `havuz/URETIM-DERSLER.md` dosyalarını oku; burada yazmayan her kural oradan gelir. Bu dosya **paragraf genişletmesinin** farklarını anlatır. Hedef: toplam ~260 paragraf sorusu.

## Hafif mod (geçerli)
- Kardeş yok: `kardes` None; yalnız ana dosya `havuz/tyt-tr/<onek>-1.json` (kardeş çıktısı `/tmp/bos-<onek>.json`).
- `ipuclari` tam 1 ipucu (cevabı söylemez).
- Yardımcı: `havuz/tyt-tr/hafif_dilbilgisi.py` (`kur`, `soru`, `bitir`; her şıkka etiket verip tek doğru şıkkı assert eder). İstersen `havuz/tyt-tr/_hafif_<onek>.py` adıyla kendi kopyanı yaz; mevcut dosyaları değiştirme.
- Uygulama anahtarı her soruda `tr|Paragraf`. `Parti(..., ders='TYT Türkçe', idon='tyttr')`.

## Kaynaklar (tip ve zorluk için; METİN KOPYALANMAZ)
- ÖSYM: `/home/claude/kutup/dersler/osym_turkce.txt` (paragraf soruları; ÖSYM dili ve uzunluğu için 3–5 örneğe bak).
- Yayınlar (koçun satın aldığı kitaplar; yalnız mantık kartı çıkarılır): `/home/claude/kutup/turkce/parafiq.txt` (Paraf İQ), `/home/claude/kutup/turkce/sifirrisk.txt` (Sıfır Risk). Kendi tip başlığın için bu kitaplarda 3–5 örnek soruya bak: kök kalıbı, tuzak türü, zor sorunun neden zor olduğu. Kart `kaynak` alanına "ÖSYM 20xx · Paraf İQ · Sıfır Risk" gibi yaz.
- **Paragraf metinlerini sen yaz.** Kitaptan ya da ÖSYM'den cümle, kurgu, özgün benzetme, örnek kişi/eser alma. Gerçek yazar/sanatçıdan alıntı yok; gerçek kişi adı geçecekse yalnız tartışmasız tarihsel bilgiyle (genelde kaçın).

## Metin standardı (ÖSYM düzeyi)
- 60–140 kelime (zor sorularda 100–150). Akıcı, deneme/eleştiri/bilim yazısı dili; konu çeşitliliği: sanat, edebiyat, bilim, doğa, teknoloji, psikoloji, eğitim, şehir, müzik, spor, tarih (tartışmasız), dil. Siyasi/dini tartışma, güncel olay, marka yok.
- Kök ÖSYM kalıbında: "Bu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?", "Bu parçadan aşağıdakilerin hangisine ulaşılamaz?", "Bu parçada aşağıdakilerin hangisine değinilmemiştir?", "Bu parça aşağıdaki cümlelerden hangisiyle tamamlanabilir?", "Numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?", "Bu parça iki paragrafa ayrılmak istense ikinci paragraf hangi cümleyle başlar?", "Bu parçanın anlatımında aşağıdakilerden hangisi yoktur?" vb. Numaralı cümlelerde "(I) … (II) …" biçimi.
- Şıklar aynı uzunluk ve biçimde; doğru şık en uzun ya da en "güzel" şık olmamalı.

## Tek doğru şık (en önemli kural)
- Her şık için betikte bir etiket yaz: doğru şık için parçadaki dayanak cümlesi; yanlış şıklar için neden yanlış (parçada yok / parçayla çelişir / fazla genelleme / yan düşünce, ana değil / bilgi parçada var ama soru değinilmeyeni soruyor …). `soru()` tek doğru şıkkı assert eder.
- "Ulaşılamaz / değinilmemiştir" sorularında dört yanlış şıkkın her biri parçada açıkça karşılığı olan bir yargı olmalı; doğru şık parçada hiç geçmeyen ya da parçayla çelişen yargı. "Ulaşılabilir" sorularında yanlış şıklar parçanın söylemediği ama akla yatkın genellemeler.
- Ana düşünce sorularında yanlış şıklar: yardımcı düşünce, parçadaki örnek, fazla geniş yargı, parçayla ilgisiz ama konuya yakın yargı. Doğru şık parçanın tamamını kapsayan yargı.
- Sıralama/akış/bölme sorularında doğruluğu yapı ile göster (bağlaç, gönderim sözcüğü "bu, böyle, ayrıca, oysa", zaman akışı); `celdiriciler` her yanlış seçeneğin neden olmadığını söyler.
- Kendini kör çözücü yerine koy: başka bir şık da savunulabiliyorsa parçayı ya da şıkkı değiştir.

## Zorluk dağılımı
Her önekte yaklaşık %25 kolay, %50 orta, %25 zor. Zor soru: ince ayrım (yan düşünce ile ana düşünceyi ayırma, örtük çıkarım, iki şıkkın biri parçanın yalnız bir bölümünü kapsıyor), uzun metin, olumsuz kök. Kolay soru: kısa metin, belirgin ana düşünce cümlesi.

## Anlatım alanları
- `bilgi` 0–2 madde (ör. "Ana düşünce: yazarın parçanın tamamında okura vermek istediği temel mesaj; genellikle giriş ya da sonuç cümlesinde toplanır").
- `adimlar` 3–5 adım: parçayı oku → anahtar cümleyi/bağlacı bul → şıkları parçayla karşılaştır → sonuç. `islem` kısa ("A: yan düşünce · B: ana düşünce ✓").
- `puf` tek cümle, genellenebilir.

## Denetim
`python3 havuz/denetle.py havuz/tyt-tr/<onek>-1.json --benzerlik /home/claude/kutup/dersler/osym_turkce.txt /home/claude/kutup/turkce/yayin_parafiq.txt /home/claude/kutup/turkce/yayin_sifirrisk.txt` → **0 hata**. 0,15 üstü benzerlik uyarısını oku; kurgu yakınsa metni değiştir. Havuz içi tekrar uyarısında konu/kurgu değiştir.

## Dosyalar ve kural
- Yalnız kendi öneklerine yaz: `havuz/kartlar/<onek>.json`, `havuz/tyt-tr/uret-<onek>.py`, `havuz/tyt-tr/<onek>-1.json`, bitince `havuz/tyt-tr/<onek>-1.HAZIR`.
- Numara 0001'den başlar. Cevap harfleri öneğin içinde dengeli (her harf ±2).
- git commit/push yok, GitHub yok, artifact yok.
- Sonunda kısa rapor: sayı, zorluk, harf dağılımı, tip dağılımı, "emin olmadıklarım" (id + neden).
