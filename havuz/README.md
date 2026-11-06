# Soru Havuzu

Bu klasör uygulamaya henüz bağlı değil; yayına (Hosting) gitmez.

- `osym-harita.json` — ÖSYM TYT Matematik 2018–2026 haritası: konu/yıl dağılımı, kalıp, sayı büyüklüğü, adım sayısı ve zorluk istatistikleri. **Soru metni içermez.** Kaynak: MEB OGM "YKS Çıkmış Sorular TYT".
- `kartlar/<konu>.json` — ÖSYM + yayınlardan çıkarılan mantık kartları (fikir, tuzak, zorluk, kalıp; soru metni değil). Üretimde önce ilgili konunun kartları okunur.
- `kutuphane-dizini.json` — 6 yayının kitap × konu soru sayıları (otomatik, yaklaşık). Okunmuş metinler depoda değil, koçun klasöründe (`_kutuphane/`).
- `tyt-mat/<konu>.json` — üretilen özgün sorular (Soru Çözüm ekranı formatı).

Kurallar: `claude/soru-havuzu-plani.md` (proje notu). Bu dal main'e koçun onayı olmadan birleştirilmez.
