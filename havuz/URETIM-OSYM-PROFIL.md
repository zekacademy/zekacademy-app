# ÖSYM profiline uyum (15 Kasım 2026 · koç isteği) — TÜM üreticiler için ek talimat

Önce dersin kendi talimatını oku (`URETIM.md`, `URETIM-DERSLER.md`, `URETIM-PARAGRAF.md`, `URETIM-DILBILGISI.md`). Bu dosya **ileri yönlü** bir ektir: bundan sonra üretilen her paket, `havuz/osym-profil.json` içindeki ders hedeflerine uyar. Eski sorular yeniden yazılmaz.

## Neden
2018–2026 ÖSYM TYT soruları ders ders tarandı (metin taraması; görsel oranları alt sınırdır). Havuzla karşılaştırınca en büyük açıklar:

| Ders | ÖSYM görsel | Havuz görsel (15 Kasım) | ÖSYM olumsuz kök | Havuz | ÖSYM kök (kelime) | Havuz |
|---|---|---|---|---|---|---|
| Matematik (temel) | ≥ %40 | %8 | — | — | ~54 | 33 |
| Fizik | ≥ %74 | %47 | %0 | %0 | ~94 | 33 |
| Kimya | ≥ %16 (tablolar sayılamadı) | %4 | %8 | %4 | ~48 | 33 |
| Biyoloji | ≥ %33 | %0 | %27 | %2 | ~34 | 30 |
| Tarih | ≥ %11 | %0 | %41 | %18 | ~72 | 32 |
| Coğrafya | ≥ %70 | %9 | %24 | %4 | ~40 | 32 |
| Türkçe | ≥ %18 | %0 | %29 | %20 | ~100 (parça dahil) | 37 |

Öncüllü oranı fizikte ÖSYM %40–60, havuz %19; diğer derslerde yakın. Sayısal şıklar havuzda hep küçükten büyüğe (doğru). Cevap harfleri her iki tarafta da kabaca dengeli.

## Kurallar (her paket için)
1. **Görsel oranı** ders hedefini karşılar (`gorsel_min`). Görsel = `sekil` alanı dolu: şekil, düzenek, grafik, tablo, harita, soy ağacı, devre, profil, klimograf. Metin içinde `|` ile tablo YASAK; tablo `tablo_svg` ile `sekil` alanına çizilir. Şekiller `havuz/cizim.py` (TikZ) ya da mevcut SVG yardımcılarıyla, değerler Python'da hesaplanarak çizilir (`claude/sekil-cizim-yontemi.md`).
2. **Şekil gerçekten gerekli olsun:** veri şeklin içinde, metin şekli tekrar etmez ("şekildeki gibi", "grafiğe göre"); şekil cevabı ele vermez; renk tek başına bilgi taşımaz.
3. **Kök uzunluğu ve bağlam:** ÖSYM kökleri havuzdan belirgin uzun (bağlam, deney, durum, kısa metin). Hedef aralık `kok_kelime_medyan`. Uzunluk süs için değil: gerçek bir durum/deney/metin kur, gereksiz cümle ekleme.
4. **Kök türü:** olumsuz kök (değildir, ulaşılamaz, söylenemez, beklenemez, gösterilemez…) ders hedefinde (`olumsuz_kok`). Olumsuz kökte olumsuz ek kalın değil ama açık yazılır; kök ile şıklar çift olumsuz oluşturmaz.
5. **Öncüllü oran** ders hedefinde (`oncullu`). Fizikte öncüllü + şekil birlikte sık (düzenek → I, II, III yargıları). Öncüllü şık sırası alışılmış (Yalnız I, Yalnız II, I ve II, I ve III, I, II ve III …); doğru küme sorudan soruya değişir.
6. **Şık dizilimi:** sayısal şıklar küçükten büyüğe; kesir/ondalık biçimi tutarlı; metin şıkları benzer uzunlukta (denetleyici "ele veren şık" HATA'sı); görsel şık (A–E'de beş küçük grafik) fizik/kimyada ara sıra kullanılabilir (ÖSYM fizikte ~%3).
7. **Cevap harfi** paket içinde her harf %15–25.
8. **Matematik kalıp dengesi:** hikâyeli %45–60, düz ≤ %25, yeni nesil (tanımlı kavram/işlem, okuma–yorum) ≥ %8, şekilli/grafik/tablo ≥ %35.
9. **Coğrafya:** gerçek harita verisi şimdilik indirilemiyor (ağ kapalı). Şematik/kurgusal harita (numaralı alanlar, eş yükselti, profil, klimograf, nüfus piramidi, grafik) kullan; gerçek ülke sınırı gerektiren soruyu ağ izni gelene kadar beklet.
10. **Biyoloji:** hücre/organel, deney düzeneği, grafik (enzim, fotosentez), soy ağacı, besin ağı, tablo; organ/doku çizimi (hazır görsel) ağ izni gelene kadar şematik çizilir.

## Kontrol
`python3 havuz/denetle.py <paket dosyaları> --profil` → pakette görsel, öncüllü, olumsuz kök, kök uzunluğu ve harf oranlarını ders hedefiyle karşılaştırır; hedef dışı her oran **uyarı** verir. Koordinatör uyarıları paket kapanmadan giderir ya da gerekçesini devir notuna yazar.
