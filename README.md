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

## Video Kütüphanesi
- Uygulama: Ders → Video Kütüphanesi (Ders → Hoca → TYT / AYT / Maarif). Konu ilerlemesi'nde ▶ öğrencinin hocasının videosunu açar. Koç, Öğrenciyi düzenle → "Ders videoları · hocası"ndan ders ders hoca seçer.
- Veri `public/video/<ders>.json` dosyalarında; ders açılınca yüklenir.
- Listeleri yenilemek: GitHub → Actions → "Video Kütüphanesi listeleri" (sır: `YOUTUBE_API_KEY`). Hocalar `data/video-kaynak.json`'da; sonuç raporu `data/video-rapor.md`.
- Yerel derleme (API'siz): `node tools/youtube-listeler.mjs`
