# TYT Geometri içerik doğrulayıcı + şekil eleştirmeni talimatı
Önce `arac/MAT-DOGRULA.md` (genel maddeler ve "Şekilli sorular için ek") ve `arac/GEO-ORTAK.md` dosyalarını oku. Geometri için ekler:
1. Her soruyu şekil + metinle bağımsız çöz (Python ile koordinat/uzunluk/açı hesabı). Verilenler cevabı TEK belirliyor mu; eksik koşul (paralellik, diklik, eşlik, merkez) metinde ya da şekilde işaretli mi; gereksiz/çelişkili veri var mı.
2. Şekil: etiketler doğru yerde ve okunaklı (≥ 11 px), dik açı/çentik/paralel işaretleri doğru; ölçekli çizimde bilinmeyen gözle okunuyorsa ve "ölçekli değildir" notu yoksa SORUN; 3B'de gizli kenarlar kesikli, oranlar doğru.
3. Kapsam: TYT dışı (kosinüs teoremi ağır hesap, trigonometrik formüller, vektör, konik) varsa SORUN.
4. Çeldirici açıklaması o değeri üreten gerçek hata mı (Python ile hesapla); ipucu/bilgi kartı anahtar fikri ya da sonucu söylüyor mu; zorluk etiketi gerçekçi mi; adımlarda şık harfi var mı.
5. Dosya içi ve dosyalar arası tekrar eden kurgu.
Çıktı: istenen dosyaya her soru tek satır ("<id> | TAMAM" ya da "<id> | SORUN: … | ÖNERİ: …"). Dosyaları DEĞİŞTİRME. Rapor KISA (en çok 12 satır): SORUN sayısı, cevap hatası var mı, en ciddi 5 madde.
