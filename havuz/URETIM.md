# Soru üretim talimatı (paralel üreticiler için)

Sen Zekacademy soru havuzu için **özgün TYT soruları** üreten bir üreticisin. Bu dosya senin tek talimatındır; burada yazmayan bir şeyi tahmin etme, en yakın örneğe bak:
`havuz/tyt-mat/uret-sayi-kumeleri-parti5.py` (biçim, anlatım dili, çeldiriciler, kardeş, assert'ler). Bütün metinler **Türkçe**.

## Görevin
Sana verilen her konu için bir **iskelet havuz** üret:
1. **Kaynakları incele (en fazla ~10 dakika).**
   - Yayın soruları: `/home/claude/kutup/sorular.json` (liste; alanlar `kitap, sayfa, no, konu, metin`). Konu grubuna göre süz (ör. `konu=='Problemler'`), anahtar kelimeyle alt konuyu bul (ör. "yüzde", "%").
   - ÖSYM: `havuz/osym-harita.json` (konu başına yıllık soru sayısı, kalıp ve adım profili) ve `/home/claude/kutup/osym_metin.json` (sayfa metinleri; anahtar kelimeyle ara).
   - Amaç: o konuda ÖSYM'nin ve yayınların sorduğu **4–6 soru tipini** ve her tipin mantığını (fikir, tuzak, adım sayısı) çıkarmak. **Soru metni kopyalanmaz, saklanmaz.**
2. **Kart ve tip dosyası yaz:** `havuz/kartlar/<onek>.json`
   ```json
   {"konu":"Yüzde Problemleri","surum":1,
    "kartlar":[{"id":"K-YZ-01","konu":"Yüzde Problemleri","alt":"…","fikir":"…","tuzak":"…","zorluk":"orta","kalip":"hikâyeli","adim":3,"tipId":"yz-ardisik","tip":"Ardışık yüzde değişimi","kaynak":"ÖSYM 2019, 2023 · 345, 3D"}],
    "tipler":[{"tipId":"yz-ardisik","ad":"Ardışık yüzde değişimi","kartlar":["K-YZ-01"],"uygulamaKonu":"prob|Yüzde Problemleri"}]}
   ```
   Kart kimliği `K-<2–3 büyük harf>-NN`, tipId `<kısaltma>-<ad>` (küçük harf, tire). Her tipin `uygulamaKonu` değeri sana verilen uygulama anahtarıdır.
3. **Üretim betiği yaz ve çalıştır:** `havuz/tyt-mat/uret-<onek>.py` → `havuz/tyt-mat/<onek>-1.json` (ana) ve `havuz/tyt-mat/<onek>-1-kardes.json`.
   - `from ortak import *` (bkz. `havuz/ortak.py`; `Parti` sınıfı, `A()`, `B()`, `G` = `havuz/gorsel.py`).
   - **Konu başına 8 ana soru**: 2 kolay, 4 orta, 2 zor; tipler arasında dağıt (her tip en az 1). **Her ana sorunun bir kardeşi** (toplam 16).
   - Numara `0001`–`0008`, id otomatik: `tytmat-<onek>-0001`, kardeş `…0001k`.
4. **Denetle:** `python3 havuz/denetle.py havuz/tyt-mat/<onek>-1.json havuz/tyt-mat/<onek>-1-kardes.json --benzerlik /home/claude/kutup/osym_metin.json /home/claude/kutup/sorular.json` → **0 hata** olana kadar düzelt. (Kendi dosyalarını ver; başka üreticinin dosyalarına dokunma.)
5. **Bitirince kısa rapor ver:** dosya adları, tip listesi, zorluk ve harf dağılımı, emin olmadığın noktalar. **git commit/push yapma, artifact yayınlama.** Kör çözüm ve önizlemeyi koordinatör yapar.

## Doğruluk (en önemli kural)
- Her cevabı betikte **kodla yeniden hesapla ve `assert` et**. Sayma/rakam/olasılık/yerleştirme sorularında **tüm olasılıkları tara** (kaba kuvvet) ve tek doğru şık olduğunu kanıtla (diğer 4 şık yanlış olmalı).
- Anlatımdaki ve görseldeki her sayısal iddia doğru olmalı (ara sonuçları da assert et).
- İki farklı doğru çözüm iki farklı cevap veremez; metinde örtük varsayım bırakma ("aynı noktaya gelen iki işaret tek kesim sayılır", "bu sürede yakıt harcanmamıştır" gibi açıkça yaz).
- Sayılar temiz (tam sayı ya da sade kesir), ÖSYM büyüklüğünde; hesap makinesi gerektiren işlem yok.

## Soru metni (ÖSYM kitapçık dili)
- Veriler ayrı satırlarda (`\n`), kök "…olduğuna göre … kaçtır?" kalıbında, soru işaretiyle biter.
- Öncüllü sorularda "I. … II. … III. … ifadelerinden hangileri kesinlikle doğrudur?"; şıklar "Yalnız I", "I ve II" …
- Hikâye/öge/sayı: kaynaktaki sorudan **en az ikisi** farklı; sadece sayı değiştirmek kopyadır. Kaynağın cümle yapısını ve şık dizilimini kopyalama. Havuz içindeki diğer sorularla da kalıp cümle tekrarlama (denetleyici yakalar).
- İki anlamlı kelime kullanma ("tek" = yegâne/tek sayı, "kat" = bina katı/katı). Harfli sayılarda "A ve B birer rakam olmak üzere" yaz.
- Ürün ilkesi: hiçbir metinde "koçuna sor" vb. olmaz.

## Şıklar ve çeldiriciler
- 5 şık, hepsi aynı biçimde; sayısal şıklar **küçükten büyüğe sıralı** (ondalık virgülle: "74,25"; kesir "3/5"; negatif "−10" — eksi işareti U+2212).
- Her yanlış şık **gerçek bir öğrenci hatasından** türetilir. `cel`: o şıkkı seçen öğrencinin hatası (1–2 kısa cümle, en az 12 karakter). `tur`: aynı şıklar için `bilgi` (bilgi eksiği), `islem` (işlem hatası) ya da `dikkat` (soru kökünü/koşulu kaçırma).
- Doğru cevap harfleri konu içinde A–E'ye dengeli dağılsın (16 soruda her harf 2–5 kez).

## Çözüm anlatımı (öğrenci hiçbir şey bilmiyormuş gibi)
- `bilgi` ("Bilmen gereken", 0–3 madde): soruda geçen temel kavram, **örnekle** (ör. "%20 = 20/100 = 0,2 · 150’nin %20’si = 30"). Soruda "iki basamaklı AB" geçiyorsa `AB = 10 × A + B` maddesi zorunlu; "tek/çift sayı" geçiyorsa tek-çift kuralı; "asal" geçiyorsa asal tanımı; "!" geçiyorsa faktöriyel tanımı (denetleyici zorunlu kılar).
- `adimlar` 3–7 adım: `A(baslik, aciklama, islem, gorsel=None)`. Başlık ≤ 6 kelime, anlamlı (aynı kelimeyi tekrar etme); açıklama ≤ 3 kısa cümle ve **neden** söyler; `islem` eşitlikler.
- **`islem` içinde " · " satır ayıracıdır** (ekranda alt alta). **Çarpma için × kullan** ("a × b", "3 × 4"); metin ve açıklamada "·" serbest. Uzun ondalık listeleri "; " ile ayır.
- `puf`: tek cümlelik genelleştirilebilir ders. `kisa` (Sınavda hızlı yol): yalnızca gerçekten zaman kazandıran ikinci yol varsa (≥ 20 karakter), yoksa verme.
- `ipuclari`: tam 3 ipucu, kademeli; cevabı söylemez.
- Görsel: şekilli sorularda `sekil`, faydalıysa adım `gorsel` (SVG; `havuz/gorsel.py` yardımcılarını kullan ya da aynı stilde yeni yardımcı yaz: `currentColor`, vurgu `var(--acc,#16A34A)`, `viewBox`). Şekil, soruyu çözmek için gereken her bilgiyi göstermeli; metinle çelişmemeli.

## Kardeş soru
Aynı tip ve zorluk, **yeni kurgu ve yeni sayılar**; metni ve şık kümesi anasından farklı (öncüllü sorularda şık kombinasyonlarını da değiştir). Kendi doğrulaması (assert) ayrı yapılır.

## Alanlar (ortak.py doldurur; sen bunları verirsin)
`R(no, tipId, tip, zorluk, alt, kazanim, kalip, adim, kart, metin, siklar, sik, istenen, ipuclari, bilgi, adimlar, puf, cel, tur, kisa=None, sekil=None)`
- `kalip` ∈ düz | hikâyeli | öncüllü | tablo | grafik | şekilli | yeni nesil
- `adim` = ÖSYM ölçüsünde çözüm adım sayısı (1–7; kolay 2, orta 3, zor 4–5 civarı)
- `kart` = "K-YZ-01 (kart özeti) · ne değişti" (kaynak kartın kimliği ile başlar)
- `istenen` = "Ne isteniyor?" kutusu (tek cümle)

## Paralel çalışma kuralları
- Yalnızca kendi dosyalarına yaz: `havuz/kartlar/<onek>.json`, `havuz/tyt-mat/uret-<onek>.py`, `havuz/tyt-mat/<onek>-1.json`, `havuz/tyt-mat/<onek>-1-kardes.json`.
- `havuz/gorsel.py`, `havuz/ortak.py`, `havuz/denetle.py` ve başka üreticilerin dosyalarını **değiştirme**. Yeni bir çizim yardımcısı gerekirse üretim betiğinin içine yaz (aynı stil: `G._svg`, `G._t`, `G.ACC`).
- Konuları sırayla bitir; her konu denetimden 0 hatayla geçince bir sonrakine geç. Bir konu bitince `havuz/tyt-mat/<onek>-1.HAZIR` adlı boş bir dosya oluştur (koordinatör bunu görünce kör çözüme alır).
- Takıldığın bir soruyu zorlama: değiştir ya da yerine başka bir soru yaz. Kaliteden ödün verme; hız için soru sayısını değil, gereksiz uzunluğu azalt.
