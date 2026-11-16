# TYT Kimya içerik doğrulayıcı + şekil eleştirmeni talimatı
Önce `arac/MAT-DOGRULA.md` dosyasını oku (genel maddeler ve "Şekilli sorular için ek" aynen geçerli). Kimya için ekler:
1. **Kimya doğruluğu:** her cevabı bağımsız olarak yeniden çöz (sayısal ise Python). Öncüllü sorularda HER öncülü ayrı ayrı değerlendir; "kesin/olabilir" ayrımı, eksik koşul (sıcaklık, basınç, saflık, "oda koşulları", tam verim) yüzünden ikinci savunulabilir cevap var mı.
2. **Kapsam:** TYT = MEB 9–10. AYT konusu (orbital/kuantum sayıları, s-p-d dizilimi, hibritleşme, VSEPR, gaz yasası hesabı, denge, hız, log ile pH, elektrokimya, molalite) varsa SORUN.
3. **Şekil:** kimyasal olarak doğru mu (formül ve yükler, tanecik sayıları ve türleri, Lewis yapısında elektron sayısı, periyodik tablo konumları, grafik biçimi, düzenek parçaları); metindeki harf/etiket şekilde var mı; veri şekilde olup metinde tekrar mı; şekil cevabı ele veriyor mu.
4. Çeldirici açıklamaları gerçek kavram yanılgısına dayanıyor mu; sayısal çeldirici değeri açıklamadaki hatadan çıkıyor mu.
5. Gerçekçilik (atom kütleleri, erime/kaynama noktaları, çözünürlükler, pH değerleri), birimler, atom kütleleri metinde mi.
6. Zorluk etiketi, kalıp etiketi, ipucu (anahtar fikri söylemesin), bilgi kartı sorunun kendi sayılarını kullanmasın.
Çıktı: istenen dosyaya her soru tek satır ("<id> | TAMAM" ya da "<id> | SORUN: … | ÖNERİ: …"). Dosyaları DEĞİŞTİRME. Rapor KISA (en çok 15 satır): SORUN sayısı, cevap hatası var mı, en ciddi 5 madde.
