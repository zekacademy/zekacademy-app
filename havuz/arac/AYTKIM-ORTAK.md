# AYT Kimya — üretim kuralları (hafif mod)

TYT kimya kurallarının hepsi geçerli: önce `arac/KIM-ORTAK.md`'yi oku (okuma listesi, ÖSYM kimya profili, doğruluk kuralları, sondaki dersler dahil; yalnız TYT kapsam/kaynak/dosya satırları aşağıdakilerle değişir). Yardımcılar: `tyt-kim/_hafif_kim2.py`, `cizim.py` (TikZ, mhchem, pgfplots). AYT farkları:

## Kimlik
- Klasör `ayt-kim/`. Betik `ayt-kim/uret-<onek>.py` → `ayt-kim/<onek>-1.json`, kartlar `kartlar/ak<onek>.json`. Gerekirse `sys.path`'e `tyt-kim` ekle.
- `id`: `aytkim-<onek>-00NN`. `ders`: `"AYT Kimya"`. `k`: `"akim|<konu adı>"` — prompttaki ad BİREBİR. Kart öneki `K-AK<HARFLER>-NN` (grep ile boş olduğunu kontrol et).

## Kapsam ve düzey
- MEB 11–12. sınıf kimya (AYT). TYT düzeyinde basit soru en fazla 3. Zorluk **3 kolay / 11 orta / 6 zor** (zor = iki kavramı birleştiren çok adımlı ÖSYM AYT sorusu).
- Harfler A–E dörder; 6–10 tipId; öncüllü %30–45; olumsuz kök ~%10.
- **Şekil ≥ %60**, renkli, ÖSYM sadeliğinde: tablo, grafik (P–V, P–T, enerji diyagramı, derişim–zaman, hız–zaman, titrasyon eğrisi, çözünürlük), kap/piston/manometre düzeneği, pil/elektroliz düzeneği, tanecik modeli, orbital diyagramı, iskelet/yapı formülü (organik), periyodik tablo kesiti. Yazı ≥ 11 px; renk tek başına bilgi taşımasın.
- Sabitler ve atom kütleleri metinde verilir (R = 0,082 L·atm/mol·K ya da 22,4 L/mol NŞA vb.). Logaritma gereken pH sorularında değerler tam çıkacak şekilde seç.
- Her sayısal cevap ve çeldirici Python'da (Fraction) hesaplanıp `assert` edilir. Organik yapılarda adlandırma IUPAC'a uygun, izomer sayıları kaba kuvvetle doğrulanır. Kimyasal gerçekler tartışmasız ders kitabı bilgisi.
- ÖSYM dili: bilgi önce, soru en sonda; gereksiz hikâye yok; sayısal şıklar küçükten büyüğe.

## Kaynak (yalnız mantık kartı)
- ÖSYM AYT sayısal çıkmışlar: `/home/claude/kutup/ayt/osym_ayt_sayisal.txt` — "KİMYA" bölümlerinden konunun sorularını bul, en az 6–8 tanesini oku; kalıp, şekil, zorluk dağılımını buna göre kur (dosyanın sonundaki konu dağılım tablosu yol gösterir).
- Yayın kaynağı şu an yok (koçun bilgisayarı bağlı değil); kurgu çeşitliliği için MEB 11–12 kazanımlarını ve ÖSYM kalıplarını kullan.

## Bitiş
- `python3 denetle.py ayt-kim/<onek>-1.json --benzerlik /home/claude/kutup/ayt/osym_ayt_sayisal.txt` → 0 HATA.
- `python3 kalite.py ayt-kim/<onek> <onek>` → `/tmp/kor/aytkim-<onek>-00NN.png`; şekilli olanların HEPSİNE Read ile bak ve düzelt.
- hazirla.sh, git, GitHub'a dokunma; çalışma dosyaların scratchpad'de. Rapor EN FAZLA 3 satır.

## AYT Fizik dalgasından dersler (baştan uygula)
- Şekildeki ok boyu/oranı cevabı doğrudan vermesin: istenen büyüklüğün okunu ya eşit/nötr çiz ya da değeri etiketle ver; açı yayı ile çizilen açı uyumlu olsun.
- İpucu/püf/bilgi kartı sorunun ara sonucunu, öncül hükmünü ya da anahtar fikri söylemesin; kart örneği sorunun sayılarını kullanmasın.
- Her çeldirici açıklaması tam cümle (".." ile bitmez) ve o DEĞERİ gerçekten üretir; betikte hesapla assert et.
- "Zor" yalnız gerçek çok adımlı/iki kavramlı sorular; tek adımlı üç yargı "orta"dır. Aynı kalıbı ve aynı sayıları paket içinde tekrarlama.
- Öncüllü kökte "Buna göre," kalıbı; kişi/cisim durumları (oturan/yürüyen, sabit/hareketli) açık.

## 2. dalga (ek 10'luk paketler) — yukarıdakilere EK kurallar
- Önek `<eski önek>iki`, dosya `<ders klasörü>/<onek>-1.json`, kart dosyası `kartlar/<ak|ab><onek>.json`, kart öneki eski öneke `2` ekle (ör. `K-AKGAZ2-NN`); grep ile boş olduğunu kontrol et.
- Paket **10 soru**: zorluk **2 kolay / 5 orta / 3 zor**; harfler A–E ikişer; 4–6 tipId; şekil ≥ %60.
- ÖNCE konunun 1. dalga dosyasını (`<onek>-1.json`) oku: aynı kurguyu, sayıları, tipId'yi TEKRARLAMA; 1. dalgada eksik kalan ÖSYM kalıplarını kapat.
- Yayın kaynakları (yazı tanıma; kurgu için oku, metin kopyalama): Kimya `/home/claude/kutup/ayt/yayin_345_ayt_kim.txt`, `yayin_345zor_ayt_kim.txt`; Biyoloji `/home/claude/kutup/ayt/yayin_345_ayt_bio.txt`, `yayin_drbio_ayt_bio.txt` ("=== s<sayfa>" başlıklı). Sayfa resimleri `/home/claude/kutup/ayt/jkim/`, `/home/claude/kutup/ayt/jbio/` — konunun 2 sayfa resmine Read ile bak.
- 1. dalga doğrulamasında en sık bulunan hatalar (baştan kaçın): ipucu/püf/bilgi kartı/kart doğru şıkkı, öncül hükmünü ya da sorunun sayısını söylüyor; "zor" etiketi tek adımlı sorulara verilmiş; çeldirici açıklaması değeri üretmiyor ya da yarım cümle; şekil cevabı veriyor; ikinci savunulabilir öncül ("kesin/olabilir" belirsizliği); MEB 11–12 dışı içerik.
