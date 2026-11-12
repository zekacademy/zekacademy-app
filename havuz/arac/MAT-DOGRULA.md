# TYT Matematik içerik doğrulayıcı talimatı
Sana verilen JSON dosyasındaki soruları denetle (alanlar: metin, siklar, cevap, `celdiriciler`, `adimlar`, `bilgi`, `ipuclari`, `puf`, `zorluk`, `kalip`, `tipId`). DOSYAYI DEĞİŞTİRME. Hafif moddayız: ipucu sayısının 1 olması SORUN DEĞİL, yazma.
Her soru için:
1. Metin tek anlamlı mı; koşullar eksiksiz mi ("sabit hızla", "eşit kapasiteli", "pozitif tam sayı", 0 dahil mi, aralık uçları, başka ekleme/çıkarma yok). Cevap doğru mu — Python ile (Fraction/tarama) yeniden hesapla; başka şık da koşulu sağlıyor mu.
2. Adımlar/bilgi/puf içinde hesap ya da kavram hatası.
3. Her çeldirici açıklaması o şıkkın DEĞERİNİ gerçekten üreten, gerçekçi bir öğrenci hatasını mı anlatıyor (hesapla). Yapay ya da tutarsız olanlar için somut yeni değer + açıklama öner.
4. İpucu cevabı ya da anahtar fikri söylüyor mu.
5. Zorluk etiketi ÖSYM TYT'ye göre gerçekçi mi (tek adım = kolay; "zor" = 4+ adım/iki koşul).
6. Kapsam TYT (MEB 9–10) içinde mi.
7. Kurgu gerçekçi mi (sayılar, birimler, yaşlar, fiyatlar), Türkçe doğal mı, ÖSYM üslubu.
8. Kalıp etiketi doğru mu; öncüllü şık dizilimi alışılmış mı.
9. Dosya içinde aynı kurgu / aynı çözüm kalıbı tekrar ediyor mu.
Çıktı: belirtilen dosyaya her soru tek satır: `id | TAMAM` ya da `id | SORUN | alan | ne | somut düzeltme`. Doğrulama betiklerini /tmp/kor/dogr/ altına yaz. Bitince SORUN sayısını ve en ciddi 5 sorunu kısaca raporla.
