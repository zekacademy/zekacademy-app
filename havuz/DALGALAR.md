# Paralel üretim dalgaları (iskelet)

Koordinatör notu: üreticiler **Sonnet** ile çalışır (`model: sonnet`), kör çözüm Sonnet ile 40–50 soruluk paketlerle yapılır. Konu başına ana soru sayısı ÖSYM ağırlığına göre (`havuz/osym-harita.json`, `havuz/osym-harita-dersler.json`); her ana sorunun bir kardeşi var. Zorluk dağılımı: 4 soruda 1 kolay–2 orta–1 zor; 6'da 1–3–2; 8'de 2–4–2; 12'de 3–6–3.

## 1. dalga — TYT Matematik (Opus; başladı)
A uslu, koklu, carpanlar, denklem · B bolunebilme, ebobekok, esitsizlik, mutlak · C sayiprob, kesirprob, yasprob, oranoranti · D hareketprob, isciprob, karisimprob, rutinprob · E yuzdeprob, karzararprob, grafikprob · F kumeler, fonksiyon, permkomb, olasilik (her biri 8 ana).

## 2. dalga — diğer TYT dersleri ve geometri (Sonnet)
| Üretici | Ders / klasör | Konular (uygulama anahtarı → önek → ana soru) |
|---|---|---|
| T1 | Türkçe `tyt-tr` | tr|Paragraf → paragraf → 12 · tr|Cümlede Anlam → cumleanlam → 8 · tr|Sözcükte Anlam → sozcukanlam → 8 · tr|Söz Yorumu → sozyorumu → 4 · tr|Deyimler ve Atasözleri → deyimler → 4 |
| T2 | Türkçe `tyt-tr` | tr|Yazım Kuralları → yazim → 6 · tr|Noktalama İşaretleri → noktalama → 6 · tr|Cümlenin Ögeleri → ogeler → 6 · tr|Ses Bilgisi → sesbilgisi → 4 · tr|Sözcükte Yapı/Ekler → yapiekler → 4 · tr|Sözcük Türleri → sozcukturleri → 4 · tr|Fiiller-Fiilimsiler-Ek Fiiller-Çatı → fiiller → 4 · tr|Cümle Türleri → cumleturleri → 4 · tr|Anlatım Bozukluğu → anlatimboz → 4 |
| P1 | Fizik `tyt-fiz` | fiz|Elektrik → elektrik → 8 · fiz|Optik → optik → 8 · fiz|Sıvıların Kaldırma Kuvveti → kaldirma → 6 · fiz|Dalgalar → dalgalar → 6 · fiz|Madde ve Özellikleri → madde → 6 · fiz|Isı, Sıcaklık ve Genleşme → isi → 6 · fiz|Hareket ve Kuvvet → hareketkuvvet → 6 · fiz|Dinamik → dinamik → 4 · fiz|Basınç → basinc → 4 · fiz|İş, Güç ve Enerji → enerji → 4 · fiz|Manyetizma → manyetizma → 4 · fiz|Fizik Bilimine Giriş → fizikgiris → 4 |
| K1 | Kimya `tyt-kim` | kim|Karışımlar → karisimlar → 6 · kim|Asitler, Bazlar ve Tuzlar → asitbaz → 6 · kim|Kimyasal Türler Arası Etkileşimler → etkilesim → 6 · kim|Maddenin Halleri → haller → 6 · kim|Periyodik Sistem → periyodik → 6 · kim|Atom ve Yapısı → atom → 4 · kim|Kimyasal Hesaplamalar → hesaplama → 4 · kim|Kimyanın Temel Kanunları → kanunlar → 4 · kim|Kimya Bilimi → kimyabilimi → 4 · kim|Kimya Her Yerde → heryerde → 4 |
| B1 | Biyoloji `tyt-bio` | bio|Hücre ve Organeller – Madde Geçişleri → hucre → 8 · bio|Kalıtım → kalitim → 8 · bio|Canlıların Temel Bileşenleri → bilesenler → 6 · bio|Hücrede Bölünme – Üreme → bolunme → 6 · bio|Canlıların Sınıflandırılması → siniflandirma → 6 · bio|Ekosistem → ekosistem → 6 · bio|Canlıların Ortak Özellikleri → ortakozellik → 4 |
| H1 | Tarih `tyt-tar` | ÖSYM ağırlığına göre: Kurtuluş Savaşına Hazırlık Dönemi, Kurtuluş Savaşı ve Antlaşmalar, İlk ve Orta Çağlarda Türk Dünyası, İlk Türk İslam Devletleri → 6'şar; kalan 22 tar| konusu → 4'er (önekler konu adından, yalnız küçük İngilizce harf) |
| C1 | Coğrafya `tyt-cog` + Felsefe `tyt-fel` | cog: İklimler, Nüfus, Göç, Doğal Afetler, Bölgeler → 6'şar; kalan 14 cog| konusu → 4'er · fel: 8 konunun her biri → 6 |
| G1 | Geometri `tyt-geo` (1) | Doğruda Açılar, Üçgende Açılar, Dik Üçgen, İkizkenar Üçgen, Eşkenar Üçgen, Açıortay, Kenarortay, Eşlik ve Benzerlik, Üçgende Benzerlik, Üçgende Alan, Açı Kenar Bağıntıları → 4'er (Üçgende Açılar, Dik Üçgen, Üçgende Benzerlik 6) |
| G2 | Geometri `tyt-geo` (2) | Çokgenler, Dörtgenler, Özel Dörtgenler, Yamuk, Paralelkenar, Eşkenar Dörtgen, Deltoid, Dikdörtgen, Kare, Çemberde Açı, Çemberde Uzun, Dairede Çevre ve Alan → 4'er (Özel Dörtgenler 6) |
| G3 | Geometri `tyt-geo` (3) | Katı Cisimler, Prizmalar, Küp, Silindir, Piramit, Koni, Küre, Noktanın Analitiği, Doğrunun Analitiği, Çemberin Analitiği, Dönüşüm Geometrisi → 4'er (Katı Cisimler 6) |

## Üretici istemi (şablon)
"Zekacademy soru havuzu için <ders> sorusu üreteceksin. Depo /home/claude/zekacademy-app (commit/push YAPMA). Önce `havuz/URETIM.md`, sonra `havuz/URETIM-DERSLER.md` dosyasını oku ve uygula. Kaynak taramasını kısa tut: alt konu ağırlıkları için `havuz/osym-harita-dersler.json` yeter; `/home/claude/kutup/dersler/osym_<ders>.txt` içinde her alt konu için yalnızca 1–2 örnek soruya bak (soru metni kopyalanmaz). Kardeş soruda `bilgi`, `puf` ve `ipuclari` ana sorudan büyük ölçüde aynen alınabilir; metin, sayılar/örnekler, adımlar ve çeldiriciler yeni olmalı. Konuların: <liste>. Her konu bitince `<onek>-1.HAZIR`. Sonunda çok kısa rapor."
