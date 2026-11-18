# Konu Tekrarı Kartı — üretim kuralları

Öğrenci bir soruyu yanlış yapıp çözüme baktığında, sorunun kazanımına ait kart açılır. Her kazanım için BİR kart yazılır; aynı kazanımdaki bütün sorular bu kartı kullanır. Örnek tasarım: Zekacademy Konu Tekrarı sayfası (geometri açıortay, fizik yüzen cisim, biyoloji enzim ve kalıtım kartları).

## Girdi
`/tmp/kor/kart/parti/pNN.txt` — her `### <id> | <anahtar> | <kazanım adı> | <N soru>` bloğu bir kart. Altında o kazanımdaki soru tipleri, örnek kazanım cümleleri, havuz sorularının bilgi kartları, çeldiricilerden öğrenci hataları ve püf notu var. Bunlar HAM MALZEMEDİR: kuralı ve sık hatayı buradan derle, metni kopyalama.

## Çıktı
`havuz/tekrar/uret-pNN.py` betiği → `havuz/tekrar/kart-pNN.json` (liste). Her kart:
```json
{"id": "...", "k": "<anahtar>", "baslik": "<kısa başlık, en çok 6 kelime>",
 "olcer": "<Bu soru neyi ölçüyordu? tek cümle, en çok 25 kelime, 'Bu soru …' diye başlamaz>",
 "kural": "<temel kural, en çok 60 kelime; önemli 1-2 ifade **kalın**>",
 "formul": "<tek satır formül/özet ya da null>",
 "sekil": "<SVG metni ya da null>",
 "ornek": {"soru": "<mini soru>", "adimlar": ["…", "…"], "cevap": "<kısa cevap>"},
 "hata": "<sık yapılan hata + nasıl fark edilir, en çok 40 kelime>",
 "akilda": "<akılda kalacak tek cümle, en çok 8 kelime, tırnaksız>"}
```
- Mini örnek: 2–4 adım, çözümlü, şıksız. Sayılar ham malzemedeki örneklerden FARKLI olsun. Hesap varsa betikte Python ile hesaplanıp `assert` edilir.
- Şekil: yalnız gerçekten yardımcı olduğunda (geometri, grafik okuma, düzenek). Basit tut: `sys.path.insert(0,'/home/claude/zekacademy-app/havuz'); from cizim import tikz_svg`. SVG ≤ 25 KB, yazı ≥ 11 px. Şekilli kartları `rsvg-convert -w 360 x.svg -o /tmp/kor/kart/png/<id>.png` ile PNG'ye çevirip Read ile bak (yalnız şekilli olanlara). Şekilsiz kart da tamamen geçerlidir; şekli olan kart oranı geometride çoğunluk, diğerlerinde ~%30 yeterli.
- Dil: öğrenciye "sen" diye, sade, kısa cümleler. TYT (MEB 9–10) dışında bilgi yok.
- Kapsam dışı kazanım (ör. koligatif özellikler, Bayes): kart yazma, `{"id": "...", "kapsamDisi": true, "neden": "..."}` yaz.
- 1–2 soruluk ve aynı partideki başka bir kazanımla aynı kuralı kullanan kazanım: kart yazma, `{"id": "...", "birlesti": "<hedef id>"}` yaz.
- Betik sonunda: her kartta zorunlu alanlar dolu, kelime sınırları tutuyor, id'ler girdidekilerle birebir (eksik yok) diye `assert` et.

## Sınırlar
- Çalışma dosyaların yalnız kendi scratchpad alt klasöründe ya da `/tmp/kor/kart/pNN/` altında.
- hazirla.sh, git, GitHub'a dokunma.
- Rapor EN FAZLA 3 satır: kart sayısı, birleşen/kapsam dışı sayısı, varsa sorun.
