# Düzeltme turu talimatı
Kör çözüm sonucu ve içerik doğrulayıcı raporu sana bildirilecek. Rapordaki her SORUN satırını üretim betiğinde düzelt (somut öneriyi uygula ya da daha iyisini yaz):
- metin belirsizliği / çelişki, gerçek dışı kurgu ve sayılar;
- çeldirici: değeri gerçekten üreten gerçekçi hata; yapay olanı değiştir;
- ipucu anahtar fikri söylemesin (yönlendirsin);
- zorluk etiketleri (şişkin olanı düşür; önekte yaklaşık %20–25 "zor" kalsın — gerekirse TYT kapsamında gerçekten zorlaştır);
- kalıp/tipId etiketleri, ilgisiz bilgi kartı, adimSayisi = adım sayısı, dosya içi tekrar eden kurgu.
Harf dengesi ±2; assert'ler korunmalı/güncellenmeli. Betiği çalıştır; `denetle.py` (--benzerlik ile ve mevcut dosyalarla birlikte) 0 HATA. Kısa rapor ver: neler değişti, çözemediğin madde.
