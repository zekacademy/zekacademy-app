# Zekacademy Koçluk Uygulaması

YKS koçluk uygulaması: öğrenci paneli (telefona kurulabilir web uygulaması) ve koç paneli.

## Yapı
- `public/` — uygulamanın kendisi (index.html, app.js, simgeler, manifest, service worker)
- `firestore.rules` — veritabanı güvenlik kuralları
- `tests/` — kuralların otomatik testleri (Firebase emülatöründe çalışır)
- `.github/workflows/deploy.yml` — her değişiklikte test + yayın

## Yayın
- Pull request açıldığında: testler çalışır, uygulama 14 günlük bir **deneme adresinde** yayınlanır.
- `main` dalına birleşince: uygulama ve güvenlik kuralları **canlıya** çıkar.
- Gerekli GitHub sırrı: `FIREBASE_SERVICE_ACCOUNT` (Firebase hizmet hesabı anahtarı).

## Hesaplar
- Koç: kullanıcı adı `zekacademy` (Firebase'de `zekacademy@app.zekacademy.com`).
- Öğrenci: kullanıcı adı `ad` → `ad@app.zekacademy.com`. Koçun açtığı hesaplarda ilk girişte şifre değişikliği zorunlu.

## Veri modeli (Firestore)
- `students/{uid}` — öğrenci kaydı (öğrenci kendisi + koç)
- `coachNotes/{uid}` — koçun özel notları (sadece koç)
- `settings/main` — mesajlar, süreler, konu listeleri (herkes okur, koç yazar)
- `notifs/{id}` — koça bildirimler (yeni kayıt)
