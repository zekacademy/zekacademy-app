// Firebase web yapılandırması (gizli değildir; güvenlik Firestore kurallarıyla sağlanır)
export const firebaseConfig = {
  apiKey: "AIzaSyBwy-Ow55ah1o_sY4xB-EFX7bv1jMvx7W8",
  authDomain: "zekacademy-59b2f.firebaseapp.com",
  projectId: "zekacademy-59b2f",
  storageBucket: "zekacademy-59b2f.firebasestorage.app",
  messagingSenderId: "600798206740",
  appId: "1:600798206740:web:c6b71bc108918de94f4001"
};
// Web Push sertifikasının herkese açık anahtarı (Firebase → Proje ayarları → Cloud Messaging → Web Push certificates).
// Boşken bildirim düğmeleri gizlenir.
export const vapidKey = "";
