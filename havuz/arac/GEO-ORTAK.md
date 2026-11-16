# TYT Geometri · üretici ortak talimatı (hafif mod, 17 Kasım 2026)
Depo: /home/claude/zekacademy-app/havuz (git commit/push YOK, GitHub YOK, artifact YOK).
Önce sırayla oku: `URETIM.md` (kardeş kuralları HARİÇ), `URETIM-DERSLER.md`, `URETIM-OSYM-PROFIL.md`, `URETIM-SEKIL.md`, `arac/MAT-ORTAK.md` (genel kurallar + sondaki şekil dersleri), `arac/KIM-ORTAK.md` sonundaki "İlk kimya dalgasından dersler" (bilgi kartı/ipucu sızıntısı, adımda şık harfi yok, tip 5–8, şekil türü tekrarı), ÖRNEK betik `tyt-geo/uret-geopilot.py` (çizim yardımcıları F sınıfı: poly, vl, sl, arc, dik, tick, par; koordinatlar hesaplanır, TikZ aynı değerlerden; her cevap koordinat hesabıyla assert). Bu yardımcıları kendi betiğine kopyala (ortak modül yazma).
## ÖSYM geometri profili
- **Görsel ≥ %90** (neredeyse her soru şekilli); kök medyanı ~50–60 kelime; günlük bağlamlı (bahçe, kâğıt katlama, raf, kutu, rampa, saat, harita) sorular ~%30, kalanı saf şekil. Öncüllü az (~%5). Sayısal şıklar küçükten büyüğe; harfler dengeli.
- Şekil ÖLÇEKLİ ya da "şekil ölçekli değildir" notlu; ölçekli çizim cevabı gözle vermesin (bilinmeyen açı/uzunluk ölçekli ise not ekle ya da hafif bozuk çiz ve not düş). Verilen her uzunluk/açı etiketi doğru ve çözüm için yeterli; gereksiz/çelişkili veri yok. Etiketler ≥ 11 px, birbirine ve çizgilere değmez; dik açı işareti, eş kenar çentikleri, paralel okları doğru yerde.
- 3B cisimlerde eğik görünüm; ön yüz gerçek oran, derinlik yarı kısaltılmış; gizli kenarlar kesikli (hesapla belirle); açınım çizimleri hesaplı.
## Doğruluk ve kapsam
- TYT = MEB 9–10 geometri + TYT'de çıkan analitik/katı cisim temel düzeyi. Kapsam DIŞI: trigonometrik toplam/fark formülleri, kosinüs teoremi ile karmaşık hesap (yalnız özel üçgenler ve basit sinüs alan formülü olabilir), vektörler, çemberin analitiğinde genel denklem dönüşümleri ileri düzey, konikler.
- Her doğru cevap ve her çeldirici DEĞERİ Python'da (Fraction/sympy yok → math + Fraction; kök içeren değerler için a√b biçimini tam sayı çiftiyle temsil et) hesaplanıp assert edilir. Şekil koordinatları cevabı doğrular (koordinattan ölçülen açı/uzunluk = cevap, ölçekli çizimlerde).
- Çeldirici = gerçek öğrenci hatası (yanlış benzerlik oranı, alan yerine çevre, yarıçap–çap karışıklığı, dış açı–iç açı, π'yi 3 almamak gibi; π kullanımı metinde açık).
- Kökte "şekil ölçekli değildir", "|AB| = 6 cm", "m(ABC) = 40°" ÖSYM yazımı. Uzunluk gösterimi |AB|; açı m(ABC).
## Kaynak (yalnız mantık kartı; metin/sayı/şekil kopyalama YOK)
- ÖSYM: `/home/claude/kutup/osym_metin.json` (geometri soruları matematik bölümünde), `havuz/osym-harita.json` (bölüm "Geometri"). Yayın: `/home/claude/kutup/geometri/yayin_orijinal.txt` (Orijinal TYT–AYT Geometri; sayfalar `\f` ile; şekiller metinde yok, yalnız soru metni) ve yazı tanımayla çıkarılan `/home/claude/kutup/geometri/yayin_kenankara.txt` (henüz yoksa birkaç dakika sonra bak; hatalı karakter olabilir). İkisi de TYT ve AYT içerir; yalnız TYT düzeyini al.
## Dosyalar
Her konu için ayrı önek: `tyt-geo/uret-<onek>.py` → `tyt-geo/<onek>-1.json`, kartlar `kartlar/<onek>.json`. `Parti('<onek>','<Konu adı>','geo|<Konu adı>',ders='TYT Geometri',idon='tytgeo')` (konu adı uygulama anahtarındaki adla AYNEN). Kart kimliği öneki görevde. Zorluk ≈ %25 kolay, %50 orta, %25 zor. Kardeş yok, ipucu 1.
## Denetim
`python3 denetle.py tyt-geo/<onek>-1.json --profil --benzerlik /home/claude/kutup/osym_metin.json /home/claude/kutup/geometri/yayin_orijinal.txt` → 0 HATA; tüm `tyt-geo/*-1.json` ile birlikte 0 HATA. PNG: `python3 kalite.py tyt-geo/<onek> <onek>` → `/tmp/kor/tytgeo-<onek>-00NN.png`; HER PNG'yi Read ile aç ve düzelt. hazirla.sh ÇALIŞTIRMA. SVG ≤ 40 KB.
Rapor KISA (en çok 8 satır).
## Düzeltme turu dersleri (17 Kasım gece; doğrulayıcı bulguları)
- Ölçekli çizilmiş ve bilinmeyeni gözle okunabilen HER soruya kökte "Şekil ölçekli değildir." notu ekle (en sık bulgu).
- Uzunluk etiketleri hangi parçaya ait olduğu belli olacak biçimde: ölçü oku/kavsi ya da parça ortasına yakın; "10" BG mi BC mi tartışılmasın. Metindeki veri (köşegen vb.) şekilde de görünsün ya da yalnız metinde olsun, ikisi çelişmesin.
- Şekil çözümün kanıtlanacak adımını vermesin (ör. kanıtlanacak dik açıyı işaretleme).
- Bilgi kartı/ipucu/puf sonucu ya da formülün sorudaki özel hâlini vermesin.
- Aynı kurgu/sayı üçlüsü (5-12-13, 8-6-10) dosyalar arasında tekrar etmesin; yalnız TYT kapsamı (eğik kesilmiş silindir, "vektör" yok).
- Şık sırası sayısal değere göre (π ve kök içerenlerde gerçek değere göre); harf dengesi.
