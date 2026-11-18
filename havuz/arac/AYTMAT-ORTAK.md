# AYT Matematik — üretim kuralları (hafif mod)

TYT kurallarının hepsi geçerli: önce `arac/MAT-ORTAK.md` (sonundaki dersler dahil) ve `URETIM-SEKIL.md` oku. Şema ve çizim için örnek betik: `tyt-mat/uret-fonksekb.py` (yardımcılar `tyt-mat/_hafif_mat.py`, `cizim.py`). Aşağıdakiler AYT'ye özel farklar.

## Kimlik ve alanlar
- Klasör `ayt-mat/`. Betik `ayt-mat/uret-<onek>.py` → `ayt-mat/<onek>-1.json`, kartlar `kartlar/<onek>.json`.
- `id`: `aytmat-<onek>-00NN`. `ders`: `"AYT Matematik"`. `k`: `"amat|<konu adı>"`; konu adı uygulamadaki listeyle BİREBİR: Polinomlar · Fonksiyonlar · 2.Dereceden Denklemler · Permütasyon ve Kombinasyon · Binom ve Olasılık · İstatistik · Karmaşık Sayılar · Eşitsizlikler · Parabol · Trigonometri · Logaritma · Diziler · Limit · Türev · İntegral.
- Kart öneki `K-A<harfler>-NN`; grep ile boş olduğunu kontrol et.

## Kapsam ve düzey
- MEB 11–12. sınıf matematik (AYT). Konunun AYT'de gerçekten sorulan kazanımları; TYT düzeyinde kalan basit sorular en fazla 4 tane.
- Paket 20 soru: zorluk **4 kolay / 10 orta / 6 zor**. Zor = ÖSYM AYT'deki gibi iki kavramı birleştiren, çok adımlı; "zor" etiketini şişirme.
- Cevap harfleri A–E dörder. 6–10 tipId. Aynı şekil türü en çok 4.
- Şekil (koç isteği: görselleştirmekten ve renklendirmekten korkma): her pakette en az %50 şekilli; Parabol, Fonksiyonlar, Türev, İntegral, Trigonometri, Limit, Logaritma'da ≥%70 (grafik, birim çember, alan boyama, tablo, sayı doğrusu, ağaç/ızgara şeması). Renk kullan: eğriler/bölgeler için ayırt edici renkler (ör. mavi, turuncu, yeşil, mor), boyalı alanlar açık tonla; yazılar koyu ve okunaklı, renk tek başına bilgi taşımasın (etiket de olsun). Grafikte okunan her değer ızgara/etiketle net.
- Öncüllü (I, II, III) sorular %15–25.
- Her cevap ve çeldirici Python'da (gerekirse `sympy`/`fractions` ile) hesaplanıp `assert` edilir. Limit/türev/integral değerlerini sympy ile doğrula.
- Çeldirici = gerçek öğrenci hatası (işaret, zincir kuralı unutma, sınır değerini dahil etme, periyodu yanlış alma…); açıklama o değeri gerçekten üretmeli.
- Bilgi kartı/ipucu/püf anahtar fikri ya da cevabı vermez; kart örneği soruyla aynı kurgu olmaz. Adımlarda şık harfi yok. Metindeki bir sayı cevabı doğrudan vermez.
- Matematik yazımı: düz metin + Unicode (x², √, π, ∫, ≤, ·); LaTeX yok. Kesirler `a/b` ya da şekil içinde.

## Kaynak (yalnız mantık kartı, metin kopyalanmaz)
- ÖSYM AYT matematik çıkmış soruları (2018–2025): `/home/claude/kutup/ayt/osym_ayt_mat.txt` — ÖNCE BUNU İNCELE: konunun ÖSYM sorularını grep ile bul, en az 8–10 tanesini oku; soru kalıplarını, şekil türlerini, zorluk ve kök uzunluğunu not et; paketin kurgu dağılımını buna göre kur.
- Yayınlar: `/home/claude/kutup/ayt/yayin_bs_ayt_mat.txt` (Bilgi Sarmal denemeleri, metin) ve `/home/claude/kutup/ayt/yayin_acil_ayt_mat.txt` (Acil soru bankası, her 4. sayfanın yazı tanıma çıktısı; "=== a<sayfa>" başlıklı; yoksa birkaç dakika sonra yeniden bak). Konunun bölümünü tara, kurgu çeşitliliği için kullan.

## Bitiş
- `python3 denetle.py ayt-mat/<onek>-1.json --profil --benzerlik /home/claude/kutup/ayt/osym_ayt_mat.txt /home/claude/kutup/ayt/yayin_bs_ayt_mat.txt` → 0 HATA (profil uyarıları TYT'ye göredir, bilgi amaçlı).
- `python3 kalite.py ayt-mat/<onek> <onek>` → `/tmp/kor/aytmat-<onek>-00NN.png`; şekilli olanların HEPSİNE Read ile bak ve düzelt.
- Çalışma dosyaların yalnız kendi scratchpad alt klasöründe. hazirla.sh, git, GitHub'a dokunma.
- Rapor EN FAZLA 3 satır: dosya, zorluk/şekil dağılımı, varsa sorun.
