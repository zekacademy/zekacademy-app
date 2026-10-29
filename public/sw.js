/* Zekacademy service worker: uygulamayı kurulabilir yapar, sayfaları ağdan alır (her zaman güncel), ağ yoksa son kopyayı gösterir. */
const CACHE = "zk-v3";
const SHELL = ["/", "/index.html", "/app.js", "/firebase-config.js", "/manifest.webmanifest", "/icons/icon-192.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); return r; }).catch(() => caches.match(e.request).then(m => m || caches.match("/index.html"))));
});

/* Telefon bildirimleri (Firebase Cloud Messaging, veri mesajı) */
self.addEventListener("push", e => {
  let p = {}; try { p = e.data ? e.data.json() : {}; } catch (_) { p = { data: { body: e.data && e.data.text() } }; }
  const d = p.data || p.notification || p;
  const title = d.title || "Zekacademy";
  e.waitUntil(self.registration.showNotification(title, {
    body: d.body || "", icon: "/icons/icon-192.png", badge: "/icons/icon-192.png",
    data: { link: d.link || "/" }, tag: d.tag || undefined
  }));
});
self.addEventListener("notificationclick", e => {
  e.notification.close();
  const link = (e.notification.data && e.notification.data.link) || "/";
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then(list => {
    for (const c of list) { if ("focus" in c) { c.navigate(link).catch(() => {}); return c.focus(); } }
    return self.clients.openWindow(link);
  }));
});
