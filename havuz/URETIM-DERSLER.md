# Ek talimat: Matematik dışındaki TYT dersleri ve Geometri

Önce `havuz/URETIM.md` dosyasını oku; oradaki her kural geçerlidir. Bu dosya yalnızca **farkları** anlatır.

## Kaynaklar
- ÖSYM 2018–2026 soruları ders ders: `/home/claude/kutup/dersler/osym_<ders>.txt` (turkce, tarih, cografya, felsefe, fizik, kimya, biyoloji; sayfalar `=== PDF sayfa N ===` ile ayrılmış). Her dersin ilk sayfalarında **"Konulara göre soru dağılım tablosu"** var: konu başına yıllık soru sayısı. Bunu ÖSYM haritası olarak kullan (hangi alt konular sık çıkıyor). Geometri soruları `/home/claude/kutup/osym_metin.json` içinde (matematik bölümü), harita `havuz/osym-harita.json` (bölüm "Geometri").
- Bu derslerde yayın kütüphanesi yok: tipleri ve kartları ÖSYM sorularından ve MEB müfredatı bilginden çıkar.
- Benzerlik denetimi: `--benzerlik /home/claude/kutup/dersler/osym_<ders>.txt` (geometride `/home/claude/kutup/osym_metin.json`).

## Dosya ve kimlikler
| Ders | klasör | `Parti(..., ders=, idon=)` | uygulama anahtarı öneki |
|---|---|---|---|
| Türkçe | `havuz/tyt-tr/` | `ders='TYT Türkçe', idon='tyttr'` | `tr|` |
| Tarih | `havuz/tyt-tar/` | `ders='TYT Tarih', idon='tyttar'` | `tar|` |
| Coğrafya | `havuz/tyt-cog/` | `ders='TYT Coğrafya', idon='tytcog'` | `cog|` |
| Felsefe | `havuz/tyt-fel/` | `ders='TYT Felsefe', idon='tytfel'` | `fel|` |
| Fizik | `havuz/tyt-fiz/` | `ders='TYT Fizik', idon='tytfiz'` | `fiz|` |
| Kimya | `havuz/tyt-kim/` | `ders='TYT Kimya', idon='tytkim'` | `kim|` |
| Biyoloji | `havuz/tyt-bio/` | `ders='TYT Biyoloji', idon='tytbio'` | `bio|` |
| Geometri | `havuz/tyt-geo/` | `ders='TYT Geometri', idon='tytgeo'` | `geo|` |

Dosya adları: `havuz/<klasör>/uret-<onek>.py`, `<onek>-1.json`, `<onek>-1-kardes.json`, `<onek>-1.HAZIR`; kartlar `havuz/kartlar/<onek>.json` (kart kimliği `K-<2–4 harf>-NN`). Uygulama anahtarları `havuz/uygulama-konulari.json` içindekilerle **birebir** aynı olmalı.

## Doğruluk (sözel ve fen)
- **Fizik, kimya, geometri:** sayısal her şeyi kodla hesapla ve assert et (birimler dahil). Geometride şekil koordinatlarını hesaplayarak çiz; şekil ölçekli olmasa da verilen her uzunluk/açı etiketi doğru ve çözüm için yeterli olmalı. Gereksiz ya da çelişkili veri koyma.
- **Türkçe, tarih, coğrafya, felsefe, biyoloji:** kodla doğrulanamayan bilgide yalnızca **MEB lise ders kitaplarında yer alan, tartışmasız** bilgileri kullan. Tarih/yer/isim/kavramı iki kez kontrol et; emin olmadığın bir bilgiyi soruya koyma. Güncel olaylar, tartışmalı yorumlar, siyasi görüş yok.
- Her yanlış şıkkın neden yanlış olduğu `cel` alanında açıkça yazılsın (bilgiye dayanarak). "Kesinlikle doğru/yanlış" köklerinde tek doğru şık olduğundan emin ol; iki savunulabilir cevap varsa soruyu değiştir.
- Türkçe (paragraf, cümlede anlam, dil bilgisi): metinleri **sen yaz** (özgün, 60–140 kelime); kitap/yazar alıntısı yok. Dil bilgisi sorularında her şıkkı kurala göre çözümle ve açıklamada göster (ör. "koşmak: fiil kökü koş- + -mak mastar eki").

## Anlatım
- "Bilmen gereken" (`bilgi`): sorunun dayandığı kural/kavram, kısa ve örnekli (ör. "Ünsüz benzeşmesi: sert ünsüzle biten sözcüğe c, d, g ile başlayan ek gelince ç, t, k olur · kitapçı, sepetçi").
- Adımlar matematik dışı derslerde de 3–7 adım: veriyi oku → ilgili bilgiyi hatırla → şıkları tek tek ele → sonuç. `islem` alanına kısa sonuç yaz (ör. "A: yanlış (Malazgirt 1071) · B: doğru").
- Sözel derslerde `kisa` (hızlı yol) çoğu zaman yoktur; zorlama.

## Kapsam
Konu başına 8 ana + 8 kardeş (2 kolay, 4 orta, 2 zor). Uygulama konusu çok dar ise (ör. "Kimya Her Yerde") 6 ana + 6 kardeş yeterli.
