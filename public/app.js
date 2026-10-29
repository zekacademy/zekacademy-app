/* Zekacademy koçluk uygulaması */
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js";
import { getAuth, initializeAuth, inMemoryPersistence, onAuthStateChanged, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, setPersistence, browserLocalPersistence, browserSessionPersistence, updatePassword, reauthenticateWithCredential, EmailAuthProvider } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-auth.js";
import { getFirestore, doc, setDoc, updateDoc, deleteDoc, deleteField, FieldPath, collection, onSnapshot } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js";
import { getMessaging, getToken, isSupported as messagingSupported } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-messaging.js";
import { getFunctions, httpsCallable } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-functions.js";
import { firebaseConfig, vapidKey } from "./firebase-config.js";
const fbApp = initializeApp(firebaseConfig);

/* ---------- Müfredat (Zekacademy şablonundan) ---------- */
const CUR = {"TYT": [{"k": "tr", "n": "Türkçe", "g": "Türkçe", "t": ["Sözcükte Anlam", "Söz Yorumu", "Deyimler ve Atasözleri", "Cümlede Anlam", "Ses Bilgisi", "Sözcükte Yapı/Ekler", "Sözcük Türleri", "Fiiller-Fiilimsiler-Ek Fiiller-Çatı", "Sözcük Grupları", "Cümlenin Ögeleri", "Cümle Türleri", "Anlatım Bozukluğu", "Yazım Kuralları", "Noktalama İşaretleri"]}, {"k": "mat", "n": "Matematik · İlk 12 Konu", "g": "Matematik", "t": ["Temel Kavramlar", "Rasyonel Sayılar", "Sayı Basamakları", "Bölme ve Bölünebilme", "Ebob – ekok", "Basit Eşitsizlikler", "Mutlak Değer", "Üslü Sayılar", "Köklü Sayılar", "Çarpanlara Ayırma", "Oran Orantı", "Denklem Çözme"]}, {"k": "prob", "n": "Matematik · Problemler", "g": "Matematik", "t": ["Sayı Problemleri", "Kesir Problemleri", "Yaş Problemleri", "Hareket Hız Problemleri", "İşçi Emek Problemleri", "Yüzde Problemleri", "Kar Zarar Problemleri", "Karışım Problemleri", "Grafik Problemleri", "Rutin Olmayan Problemleri"]}, {"k": "matd", "n": "Matematik · Diğer Konular", "g": "Matematik", "t": ["Kümeler-Kartezyen Çarpım", "Mantık", "Fonksiyonlar", "Polinomlar", "2.Dereceden Denklemler", "Permütasyon ve Kombinasyon", "Olasılık", "Veri – İstatistik"]}, {"k": "geo", "n": "Geometri", "g": "TYT/AYT", "t": ["Temel Kavramlar", "Doğruda Açılar", "Üçgende Açılar", "Özel Üçgenler", "Dik Üçgen", "İkizkenar Üçgen", "Eşkenar Üçgen", "Açıortay", "Kenarortay", "Eşlik ve Benzerlik", "Üçgende Alan", "Üçgende Benzerlik", "Açı Kenar Bağıntıları", "Çokgenler", "Özel Dörtgenler", "Dörtgenler", "Deltoid", "Paralelkenar", "Eşkenar Dörtgen", "Dikdörtgen", "Kare", "Yamuk", "Çemberde Açı", "Çemberde Uzun", "Dairede Çevre ve Alan", "Noktanın Analitiği", "Doğrunun Analitiği", "Dönüşüm Geometrisi", "Çemberin Analitiği", "Katı Cisimler", "Prizmalar", "Küp", "Silindir", "Piramit", "Koni", "Küre"]}, {"k": "tar", "n": "Tarih", "g": "Sosyal", "t": ["TYT Tarih", "Tarih ve Zaman", "İnsanlığın İlk Dönemleri", "Ortaçağ’da Dünya", "İlk ve Orta Çağlarda Türk Dünyası", "İslam Medeniyetinin Doğuşu", "İlk Türk İslam Devletleri", "Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi", "Beylikten Devlete Osmanlı Siyaseti(1300-1453)", "Dünya Gücü Osmanlı Devleti (1453-1600)", "Yeni Çağ Avrupa Tarihi", "Yakın Çağ Avrupa Tarihi", "Osmanlı Devletinde Arayış Yılları", "18. Yüzyılda Değişim ve Diplomasi", "En Uzun Yüzyıl", "Osmanlı Kültür ve Medeniyeti", "20. Yüzyılda Osmanlı Devleti", "I. Dünya Savaşı", "Mondros Ateşkesi, İşgaller ve Cemiyetler", "Kurtuluş Savaşına Hazırlık Dönemi", "I. TBMM Dönemi", "Kurtuluş Savaşı ve Antlaşmalar", "II. TBMM Dönemi ve Çok Partili Hayata Geçiş", "Türk İnkılabı", "Atatürk İlkeleri", "Atatürk Dönemi Türk Dış Politikası"]}, {"k": "cog", "n": "Coğrafya", "g": "Sosyal", "t": ["Doğa ve İnsan", "Dünya’nın Şekli ve Hareketleri", "Coğrafi Konum", "Harita Bilgisi", "Atmosfer ve Sıcaklık", "İklimler", "Basınç ve Rüzgarlar", "Nem, Yağış ve Buharlaşma", "İç Kuvvetler / Dış Kuvvetler", "Su – Toprak ve Bitkiler", "Nüfus", "Göç", "Yerleşme", "Türkiye’nin Yer Şekilleri", "Ekonomik Faaliyetler", "Bölgeler", "Uluslararası Ulaşım Hatları", "Çevre ve Toplum", "Doğal Afetler"]}, {"k": "fel", "n": "Felsefe", "g": "Sosyal", "t": ["Felsefenin Konusu", "Bilgi Felsefesi", "Varlık Felsefesi", "Ahlak Felsefesi", "Sanat Felsefesi", "Din Felsefesi", "Siyaset Felsefesi", "Bilim Felsefesi"]}, {"k": "fiz", "n": "Fizik", "g": "Fen", "t": ["Fizik Bilimine Giriş", "Madde ve Özellikleri", "Sıvıların Kaldırma Kuvveti", "Basınç", "Isı, Sıcaklık ve Genleşme", "Hareket ve Kuvvet", "Dinamik", "İş, Güç ve Enerji", "Elektrik", "Manyetizma", "Dalgalar", "Optik"]}, {"k": "kim", "n": "Kimya", "g": "Fen", "t": ["Kimya Bilimi", "Atom ve Yapısı", "Periyodik Sistem", "Kimyasal Türler Arası Etkileşimler", "Maddenin Halleri", "Kimyanın Temel Kanunları", "Kimyasal Hesaplamalar", "Karışımlar", "Asitler, Bazlar ve Tuzlar", "Endüstride ve Canlılarda Enerji", "Kimya Her Yerde"]}, {"k": "bio", "n": "Biyoloji", "g": "Fen", "t": ["Canlıların Ortak Özellikleri", "Canlıların Temel Bileşenleri", "Hücre ve Organeller – Madde Geçişleri", "Canlıların Sınıflandırılması", "Hücrede Bölünme – Üreme", "Kalıtım", "Ekosistem"]}], "AYT": [{"k": "amat", "n": "Matematik", "g": "SAY · EA", "t": ["Polinomlar", "Fonksiyonlar", "2.Dereceden Denklemler", "Permütasyon ve Kombinasyon", "Binom ve Olasılık", "İstatistik", "Karmaşık Sayılar", "Eşitsizlikler", "Parabol", "Trigonometri", "Logaritma", "Diziler", "Limit", "Türev", "İntegral"], "a": ["SAY", "EA"]}, {"k": "afiz", "n": "Fizik", "g": "SAY", "t": ["Vektörler", "Bağıl Hareket", "Newton’un Hareket Yasaları", "Bir Boyutta Sabit İvmeli Hareket", "Atışlar", "Enerji ve Hareket", "İtme ve Momentum", "Tork Denge", "Kütle ve Ağırlık Merkezi", "Basit Makineler", "Düzgün Çembersel Hareket", "Eylemsizlik ve Açısal Momentum", "Kütle Çekim Kuvveti", "Basit Harmonik Hareket", "Dalga Mekaniği", "Elektrik Alan ve Potansiyel", "Paralel Levhalar ve Sığa", "Manyetik Alan ve Manyetik Kuvvet", "İndüksiyon, Alternatif Akım ve Transformatörler", "Atom Modelleri", "Büyük Patlama ve Parçacık Fiziği", "Radyoaktivite", "Özel Görelilik", "Kara Cisim Işıması", "Fotoelektrik Olay ve Compton Olayı", "Modern Fiziğin Teknolojideki Uygulamaları"], "a": ["SAY"]}, {"k": "akim", "n": "Kimya", "g": "SAY", "t": ["Modern Atom Teorisi", "Gazlar", "Sıvı Çözeltiler", "Kimyasal Tepkimelerde Enerji", "Kimyasal Tepkimelerde Hız", "Kimyasal Tepkimelerde Denge", "Asit-Baz Dengesi", "Çözünürlük Dengesi", "Kimya ve Elektrik", "Organik Kimya", "Enerji Kaynakları ve Bilimsel Gelişmeler"], "a": ["SAY"]}, {"k": "abio", "n": "Biyoloji", "g": "SAY", "t": ["Sinir Sistemi", "Endokrin Sistem", "Duyu Organları", "Destek ve Hareket Sistemi", "Sindirim Sistemi", "Dolaşım ve Bağışıklık Sistemi", "Solunum Sistemi", "Boşaltım Sistemi", "Üreme Sistemi ve Embriyonik Gelişim", "Komünite ve Popülasyon Ekolojisi", "Genetik Şifre-Protein Sentezi", "Fotosentez – Kemosentez", "Hücresel Solunum", "Bitki Biyolojisi", "Canlılar ve Çevre"], "a": ["SAY"]}, {"k": "aede", "n": "Edebiyat", "g": "EA · SÖZ", "t": ["Güzel Sanatlar ve Edebiyat", "Metinlerin Sınıflandırılması", "Şiir Bilgisi", "Edebi Sanatlar", "Türk Edebiyatı Dönemleri", "İslamiyet Öncesi Türk Edebiyatı ve Geçiş Dönemi", "Halk Edebiyatı", "Divan Edebiyatı", "Tanzimat Edebiyatı", "Servet-i Fünun Edebiyatı", "Fecr-i Ati Edebiyatı", "Milli Edebiyat", "Cumhuriyet Dönemi Edebiyatı", "Edebiyat Akımları", "Dünya Edebiyatı"], "a": ["EA", "SÖZ"]}, {"k": "atar", "n": "Tarih", "g": "EA · SÖZ", "t": ["Tarih ve Zaman", "İnsanlığın İlk Dönemleri", "Ortaçağ’da Dünya", "İlk ve Orta Çağlarda Türk Dünyası", "İslam Medeniyetinin Doğuşu", "İlk Türk İslam Devletleri", "Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi", "Beylikten Devlete Osmanlı Siyaseti(1300-1453)", "Dünya Gücü Osmanlı Devleti (1453-1600)", "Yeni Çağ Avrupa Tarihi", "Yakın Çağ Avrupa Tarihi", "Osmanlı Devletinde Arayış Yılları", "18. Yüzyılda Değişim ve Diplomasi", "En Uzun Yüzyıl", "Osmanlı Kültür ve Medeniyeti", "20. Yüzyılda Osmanlı Devleti", "I. Dünya Savaşı", "Mondros Ateşkesi, İşgaller ve Cemiyetler", "Kurtuluş Savaşına Hazırlık Dönemi", "I. TBMM Dönemi", "Kurtuluş Savaşı ve Antlaşmalar", "II. TBMM Dönemi ve Çok Partili Hayata Geçiş", "Türk İnkılabı", "Atatürk İlkeleri", "Atatürk Dönemi Türk Dış Politikası", "Atatürk Sonrası Dış Politika ve Güncel Olaylar"], "a": ["EA", "SÖZ"]}, {"k": "acog", "n": "Coğrafya", "g": "EA · SÖZ", "t": ["Biyoçeşitlilik", "Enerji Akışı ve Madde Döngüleri", "Nüfus Politikaları", "Şehirlerin Fonksiyonları", "Türkiyede Yerleşmeler", "Ekonomik Faaliyetler", "Türkiyede Tarım", "Türkiyede Hayvancılık", "Türkiyede Madenler", "Türkiyede Enerji Kaynakları", "Türkiyede Sanayi", "Kültür Bölgeleri", "Küresel Ticaret", "Küresel ve Bölgesel Örgütler", "Çevre Sorunları ve Ekstrem Doğa Olayları", "Küresel İklim Değişikliği", "Kalkınma Projeleri", "Türkiyede Ulaşım", "Türkiyede Ticaret", "Türkiyede Turizm", "Jeopolitik Konum", "Ülkeler Arası Etkileşimler", "Çatışma Bölgeleri", "Çevre Sorunları"], "a": ["EA", "SÖZ"]}, {"k": "afel", "n": "Felsefe Grubu", "g": "SÖZ", "t": ["Felsefe", "Psikoloji", "Sosyoloji", "Mantık", "Din"], "a": ["SÖZ"]}]};
/* ---------- Sabitler ---------- */
/* ---------- Sabitler ---------- */
/* ---------- Sabitler ---------- */
/* ---------- Sabitler ---------- */
/* ---------- Sabitler ---------- */
/* ---------- Sabitler ---------- */
const ALANLAR = ["SAY","EA","SÖZ"];
const SINIFLAR = ["9. sınıf","10. sınıf","11. sınıf","12. sınıf","Mezun"];
const DERSLER = ["TYT Türkçe","Paragraf","TYT Matematik","Problemler","Geometri","TYT Fizik","TYT Kimya","TYT Biyoloji","TYT Tarih","TYT Coğrafya","TYT Felsefe","TYT Din","AYT Matematik","AYT Fizik","AYT Kimya","AYT Biyoloji","AYT Edebiyat","AYT Tarih","AYT Coğrafya","AYT Felsefe Grubu","TYT Deneme","AYT Deneme","Branş Denemesi","Konu Tekrarı","Diğer"];
const SURELER = [20,30,40,45,60,75,90,120,150,180];
const TYTF = [["turkce","Türkçe",40,"Tr"],["sosyal","Sosyal Bilimler",20,"Sos"],["mat","Temel Matematik",40,"Mat"],["fen","Fen Bilimleri",20,"Fen"]];
const AYTF = [["mat","Matematik",40,"Mat"],["fen","Fen Bilimleri",40,"Fen"],["sos1","Edebiyat-Sosyal 1",40,"TDE"],["sos2","Sosyal Bilimler 2",40,"Sos2"]];
const GUN = ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"];
const GUNK = ["Pzt","Sal","Çar","Per","Cum","Cmt","Paz"];
const MON = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"];
const DEF_SABAH = [
"Hayırlı sabahlar {Ad}, sabahın bereketini yakalamanı istiyorum. Bugün sağlam bir gün seni bekliyor.",
"Hayırlı sabahlar {Ad}, bugün senden sağlam bir kronometre bekliyorum.",
"Hayırlı sabahlar {Ad}, bugün ciddi anlamda sağlam bir çalışma bekliyorum.",
"Hayırlı sabahlar {Ad}, bugün programımızı eksiksiz tamamlamaya çalışalım.",
"Hayırlı sabahlar {Ad}, erken başlayan günün bereketi başka olur. Hadi ilk görevle açalım.",
"Hayırlı sabahlar {Ad}, bugün programdaki her satırı tek tek kapatalım inşallah.",
"Hayırlı sabahlar {Ad}, bugün odaklı ve verimli bir gün geçirmeni istiyorum.",
"Hayırlı sabahlar {Ad}, dünü geride bıraktık. Bugün yeni ve sağlam bir sayfa açıyoruz.",
"Hayırlı sabahlar {Ad}, bugün kronometreyi erkenden başlatmanı bekliyorum.",
"Hayırlı sabahlar {Ad}, hedefe bir gün daha yaklaşıyoruz. Bugünü boş geçirmeyelim.",
"Hayırlı sabahlar {Ad}, bugün paragrafla güne başlayalım, gerisi kendiliğinden gelir.",
"Hayırlı sabahlar {Ad}, bugün senden disiplinli bir çalışma bekliyorum. Sana güveniyorum.",
"Hayırlı sabahlar {Ad}, bugün emek verdiğin her saat haziranda karşılığını verecek inşallah.",
"Hayırlı sabahlar {Ad}, telefonu bir kenara koyup sağlam bir ilk oturumla başlayalım.",
"Hayırlı sabahlar {Ad}, bugün programı eksiksiz bitirip akşam rahat bir kafayla yatalım.",
"Hayırlı sabahlar {Ad}, bugün yanlışlarımızdan öğrenip netlerimizi büyüteceğiz.",
"Hayırlı sabahlar {Ad}, bugün sağlam bir tempo tutturmanı istiyorum. Hadi bakalım.",
"Hayırlı sabahlar {Ad}, sabahın ilk saatleri en verimli saatler. Onları iyi değerlendirelim.",
"Hayırlı sabahlar {Ad}, bugün hedef saatini doldurmanı bekliyorum.",
"Hayırlı sabahlar {Ad}, bugün de azimle çalışalım. Emeğimiz boşa gitmeyecek inşallah.",
"Hayırlı sabahlar {Ad}, bugün branş denemeni ciddiyetle çöz, analizini de ihmal etme.",
"Hayırlı sabahlar {Ad}, bugünün programı hazır. Sana düşen tek şey başlamak.",
"Hayırlı sabahlar {Ad}, bugün dünden daha iyi bir kronometre görmek istiyorum.",
"Hayırlı sabahlar {Ad}, bugün yavaş da olsa istikrarlı ilerleyelim. Asıl kazanç istikrarda.",
"Hayırlı sabahlar {Ad}, hayalindeki bölüm için bugün de sağlam bir adım atalım.",
"Hayırlı sabahlar {Ad}, bugün dikkatini dağıtacak her şeyi uzak tutup programa odaklanalım.",
"Hayırlı sabahlar {Ad}, bugün zorlandığın konunun üstüne gitmeni istiyorum. Üstesinden gelirsin.",
"Hayırlı sabahlar {Ad}, Allah kolaylık versin. Bugün de verimli bir gün olsun inşallah.",
"Hayırlı sabahlar {Ad}, bugün yapılacakları bitirip akşam kendinle gurur duyalım.",
"Hayırlı sabahlar {Ad}, yeni bir gün, yeni bir fırsat. Bugün de sağlam bir çalışma bekliyorum."];
const DEF_AKSAM_LIST = [
"Hayırlı akşamlar {Ad}, eğer kronometreyi ve programı hâlâ girmediysek mutlaka uygulamaya kaydedelim inşallah.",
"Hayırlı akşamlar {Ad}, bugün yoğun bir gündü. Ne kadar çalışırsak çalışalım, takip açısından kronometremizi ve yaptıklarımızı uygulamaya kaydedelim; sadece 1 dakika sürer.",
"Hayırlı akşamlar {Ad}, günü kapatmadan programdaki tamamladığın görevleri işaretleyelim.",
"Hayırlı akşamlar {Ad}, bugünkü çalışma süreni henüz göremiyorum. Yatmadan önce kronometreye kaydedelim.",
"Hayırlı akşamlar {Ad}, bugünün emeği kayıtlara geçsin. Programı ve süreyi girmeyi unutmayalım.",
"Hayırlı akşamlar {Ad}, az ya da çok fark etmez; bugün yaptıklarını mutlaka uygulamaya işleyelim.",
"Hayırlı akşamlar {Ad}, programda işaretlenmemiş görevlerin görünüyor. Bitirdiklerini işaretleyip günü kapatalım.",
"Hayırlı akşamlar {Ad}, kronometreyi kullanmadıysan sorun değil; bugünkü süreni elle ekleyelim, 1 dakikanı alır.",
"Hayırlı akşamlar {Ad}, takibimizi düzenli yapalım ki yarın programı daha doğru planlayalım. Bugünü kaydetmeyi unutma.",
"Hayırlı akşamlar {Ad}, bugünü kayda geçirip iyi bir uykuya dalalım. Yarın yeni bir gün inşallah."];
const dayNo = d => Math.floor(new Date(d+"T12:00:00").getTime()/864e5);
const strHash = x => [...String(x)].reduce((a,c)=>(a*31+c.charCodeAt(0))>>>0, 7);
const fillName = (m, s) => m.replace("{Ad}", firstName(s.name));
const DEF_AKSAM = {sure:[DEF_AKSAM_LIST[3],DEF_AKSAM_LIST[7]], gorev:[DEF_AKSAM_LIST[2],DEF_AKSAM_LIST[6]], ikisi:[0,1,4,5,8,9].map(i=>DEF_AKSAM_LIST[i])};
const hm = x => { const [h,m] = String(x||"0:0").split(":").map(Number); return (h||0)*60+(m||0); };
const nowMin = () => { const d = new Date(); return d.getHours()*60+d.getMinutes(); };
function morningMsg(s, id){ const c = cfg(); if(!c.sabahAcik || nowMin() < hm(c.sabahSaat)) return null; const L = c.sabah.filter(Boolean); if(!L.length) return null; return fillName(L[(dayNo(today()) + strHash(id)) % L.length], s); }
function eveningMsg(s){
  const c = cfg(); if(!c.aksamAcik || nowMin() < hm(c.aksamSaat)) return null;
  const tl = dayTasks(s, today()), missTasks = tl.some(x=>!x.done), missTime = minutes(s, today())===0;
  if(!missTasks && !missTime) return null;
  const pool = (missTasks && missTime ? c.aksam.ikisi : missTime ? c.aksam.sure : c.aksam.gorev).filter(Boolean);
  const any = pool.length ? pool : [...c.aksam.ikisi, ...c.aksam.sure, ...c.aksam.gorev].filter(Boolean); if(!any.length) return null;
  return {text: fillName(any[dayNo(today()) % any.length], s), missTasks, missTime};
}
const ADMIN_U = "zekacademy";

/* ---------- İkonlar ---------- */
const IC = {
  phone:'<path fill-rule="evenodd" d="M8 2h8a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2zm0 2.5v13h8v-13zm3 15h2v1.5h-2z"/><path d="M11 6.5h2v4h2l-3 3.5-3-3.5h2z"/>',
 home:'<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 cal:'<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/>',
 chart:'<path d="M5 20V11M12 20V4M19 20v-6"/>',
 book:'<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21a2 2 0 0 1 2-2h13"/>',
 more:'<circle cx="5" cy="12" r="1.3" fill="currentColor"/><circle cx="12" cy="12" r="1.3" fill="currentColor"/><circle cx="19" cy="12" r="1.3" fill="currentColor"/>',
 bell:'<path d="M6 9a6 6 0 1 1 12 0c0 6 2.5 7.5 2.5 7.5h-17S6 15 6 9z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
 clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 check:'<path d="M5 12.5 10 17 19 7"/>',
 flame:'<path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 0 1-10 0c0-2 1-3.5 2-4.5 0 2 1 3 2 3 0-3-1-5 1-8.5z"/>',
 target:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 plus:'<path d="M12 5v14M5 12h14"/>',
 chev:'<path d="m9 6 6 6-6 6"/>',
 back:'<path d="m15 6-6 6 6 6"/>',
 play:'<path d="M8 5.5v13l11-6.5z" fill="currentColor"/>',
 stop:'<rect x="6" y="6" width="12" height="12" rx="2" fill="currentColor"/>',
 moon:'<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
 sun:'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 logout:'<path d="M15 4h3a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-3M10 16l-4-4 4-4M6 12h10"/>',
 users:'<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
 search:'<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 x:'<path d="M6 6l12 12M18 6 6 18"/>',
 edit:'<path d="M4 20h4L19 9l-4-4L4 16z"/>',
 trash:'<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/>',
 copy:'<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
 timer:'<circle cx="12" cy="13" r="8"/><path d="M12 9v4M9 2h6"/>',
 list:'<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/>',
 note:'<path d="M5 4h14v12l-4 4H5z"/><path d="M15 20v-4h4"/>',
 palette:'<circle cx="12" cy="12" r="9"/><circle cx="8" cy="10" r="1.3"/><circle cx="12" cy="7.5" r="1.3"/><circle cx="16" cy="10" r="1.3"/>',
 eye:'<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 alert:'<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17h.01"/>',
 user:'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 grad:'<path d="M2 9 12 4l10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
 trend:'<path d="m3 17 6-6 4 4 8-8"/><path d="M15 7h6v6"/>'
};
const icon = (n, c="") => `<svg class="i ${c}" viewBox="0 0 24 24" aria-hidden="true">${IC[n]||""}</svg>`;

/* ---------- Yardımcılar ---------- */
const $ = s => document.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const uid = () => Math.random().toString(36).slice(2,10) + Date.now().toString(36).slice(-4);
const num = v => { if(v===""||v==null) return null; const n = parseFloat(String(v).replace(",", ".")); return isFinite(n) ? n : null; };
const fmt = n => n == null ? "—" : (Math.round(n*100)/100).toLocaleString("tr-TR");
const iso = d => { const x = new Date(d); x.setMinutes(x.getMinutes()-x.getTimezoneOffset()); return x.toISOString().slice(0,10); };
const today = () => iso(new Date());
const monday = d => { const x = new Date(typeof d==="string"? d+"T12:00:00" : d); x.setHours(12,0,0,0); const w = (x.getDay()+6)%7; x.setDate(x.getDate()-w); return iso(x); };
const addDays = (s,n) => { const x = new Date(s+"T12:00:00"); x.setDate(x.getDate()+n); return iso(x); };
const dIdx = s => (new Date(s+"T12:00:00").getDay()+6)%7;
const dNum = s => new Date(s+"T12:00:00").getDate();
const trDate = s => { if(!s) return "—"; const d = new Date(s+"T12:00:00"); return d.getDate()+" "+MON[d.getMonth()]+" "+d.getFullYear(); };
const shortDate = s => { const d = new Date(s+"T12:00:00"); return d.getDate()+" "+MON[d.getMonth()].slice(0,3); };
const longToday = () => { const t = today(); return dNum(t)+" "+MON[new Date().getMonth()]+", "+GUN[dIdx(t)]; };
const initials = n => (n||"?").split(/\s+/).filter(Boolean).slice(0,2).map(w=>w[0].toLocaleUpperCase("tr")).join("");
const tkey = (sk, name) => sk + "|" + name;
const normU = u => String(u||"").trim().toLocaleLowerCase("tr").replace(/ı/g,"i").replace(/ş/g,"s").replace(/ğ/g,"g").replace(/ü/g,"u").replace(/ö/g,"o").replace(/ç/g,"c");
const normName = n => normU(n).replace(/\s+/g," ");
const fmtMin = m => { m = Math.round(m||0); if(m<60) return m+"dk"; const h=Math.floor(m/60), r=m%60; return h+"s"+(r?" "+r+"dk":""); };
const addMin = (hhmm, m) => { if(!hhmm) return ""; const [h,mi] = hhmm.split(":").map(Number); const t = h*60+mi+(+m||0); return String(Math.floor(t/60)%24).padStart(2,"0")+":"+String(t%60).padStart(2,"0"); };
const firstName = n => (n||"").split(" ")[0];
const nowISO = () => new Date().toISOString();
const ago = isoStr => { if(!isoStr) return ""; const m = Math.round((Date.now()-new Date(isoStr))/60000); if(m<1) return "şimdi"; if(m<60) return m+" dk önce"; const h=Math.round(m/60); if(h<24) return h+" sa önce"; const d=Math.round(h/24); return d+" gün önce"; };
function sha256(str){
  const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const b=[...unescape(encodeURIComponent(str))].map(c=>c.charCodeAt(0));
  const l=b.length*8; b.push(0x80); while(b.length%64!==56) b.push(0);
  for(let i=7;i>=0;i--) b.push(Math.floor(l/Math.pow(2,i*8))&255);
  let H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const r=(x,n)=>(x>>>n)|(x<<(32-n));
  for(let o=0;o<b.length;o+=64){
    const w=new Array(64);
    for(let i=0;i<16;i++) w[i]=(b[o+4*i]<<24)|(b[o+4*i+1]<<16)|(b[o+4*i+2]<<8)|b[o+4*i+3];
    for(let i=16;i<64;i++){ const s0=r(w[i-15],7)^r(w[i-15],18)^(w[i-15]>>>3), s1=r(w[i-2],17)^r(w[i-2],19)^(w[i-2]>>>10); w[i]=(w[i-16]+s0+w[i-7]+s1)|0; }
    let [a,bb,c,d,e,f,g,h]=H;
    for(let i=0;i<64;i++){ const S1=r(e,6)^r(e,11)^r(e,25), ch=(e&f)^(~e&g), t1=(h+S1+ch+K[i]+w[i])|0, S0=r(a,2)^r(a,13)^r(a,22), mj=(a&bb)^(a&c)^(bb&c), t2=(S0+mj)|0; h=g; g=f; f=e; e=(d+t1)|0; d=c; c=bb; bb=a; a=(t1+t2)|0; }
    H=[H[0]+a,H[1]+bb,H[2]+c,H[3]+d,H[4]+e,H[5]+f,H[6]+g,H[7]+h].map(x=>x|0);
  }
  return H.map(x=>(x>>>0).toString(16).padStart(8,"0")).join("");
}

/* ---------- Tema ---------- */
const THEME = (()=>{ try{ return JSON.parse(localStorage.getItem("zk-theme")||"{}"); }catch(e){ return {}; } })();
THEME.mode = THEME.mode || "system"; THEME.accent = THEME.accent || "blue";
function applyTheme(){
  const r = document.documentElement;
  r.classList.toggle("m-light", THEME.mode==="light"); r.classList.toggle("m-dark", THEME.mode==="dark");
  if(THEME.accent==="blue") r.removeAttribute("data-accent"); else r.setAttribute("data-accent", THEME.accent);
  try{ localStorage.setItem("zk-theme", JSON.stringify(THEME)); }catch(e){}
}
applyTheme();

/* ---------- Durum ---------- */
const S = { students:new Map(), cnotes:new Map(), notifs:new Map(), settings:{examDate:"2027-06-19", tahmini:true},
  ready:false, role:null, me:null, auth:"signup", authRole:"student",
  view:"home", cur:null, dtab:"ozet", week:monday(new Date()), day:today(), pmode:"gun", ex:"TYT", aytAll:false, q:"" };
const A = () => S.role === "admin";
function cfg(){ const x = S.settings; return {
  kurum: x.kurum || "zekacademy",
  sabahAcik: x.sabahAcik !== false, sabahSaat: x.sabahSaat || "08:30", sabah: x.sabah || DEF_SABAH,
  aksamAcik: x.aksamAcik !== false, aksamSaat: x.aksamSaat || "22:00", aksam: x.aksam || DEF_AKSAM,
  sureler: x.sureler || DEF_SURELER, quick: x.quick || DEF_QUICK, hedefDers: x.hedefDers || DEF_HEDEF_DERS }; }
const CURX = () => S.settings.cur || CUR;
const st = () => S.students.get(A() ? S.cur : S.me);
const sid = () => A() ? S.cur : S.me;
function blank(f){
  return { name:f.name, alan:f.alan, sinif:f.sinif, okul:f.sinif==="Mezun"?"":(f.okul||""), createdAt:today(), kullanici:f.kullanici||"",
    baslangic:{tarih:today(), tyt:f.tyt??null, ayt:f.ayt??null, tytYok:!!f.tytYok, aytYok:!!f.aytYok}, hedef:{tarih:"", tyt:null, ayt:null},
    topics:{}, weeks:{}, denemeler:[], gunluk:{}, timer:null, koctanNot:null, notSeen:"", lastSeen:"" };
}

/* ---------- Depolama ve giriş (Firebase) ---------- */
const auth = getAuth(fbApp), fdb = getFirestore(fbApp);
const COACH_EMAIL = "zekacademy@app.zekacademy.com";
const EMAIL_DOMAIN = "app.zekacademy.com";
const emailOf = u => `${u}@${EMAIL_DOMAIN}`;
const dirty = new Set(), timers = {}; let chain = Promise.resolve(); let unsubs = [];
const MAPS = { students:()=>S.students, notifs:()=>S.notifs, coachNotes:()=>S.cnotes };
/* Sunucudaki son hâl (base) ile yereldeki farkı alan alan yazar; böylece koç ve öğrenci aynı anda farklı yerleri değiştirince birbirinin değişikliğini silmez. */
const BASE = new Map();
const isObj = x => x && typeof x === "object" && !Array.isArray(x);
function diffPaths(a, b, path=[], out=[], depth=0){
  if(depth < 4 && isObj(a) && isObj(b)){
    for(const k of new Set([...Object.keys(a), ...Object.keys(b)])){
      if(!(k in b)) out.push([[...path,k], deleteField()]);
      else if(!(k in a)) out.push([[...path,k], b[k]]);
      else diffPaths(a[k], b[k], [...path,k], out, depth+1);
    }
  } else if(JSON.stringify(a) !== JSON.stringify(b)) out.push([path, b === undefined ? deleteField() : b]);
  return out;
}
async function writeDoc(coll, id, data){
  const ref = doc(fdb, coll, id), key = coll+"/"+id, base = BASE.get(key);
  if(!data){ await deleteDoc(ref); BASE.delete(key); return; }
  const clean = JSON.parse(JSON.stringify(data));
  if(!base){ await setDoc(ref, clean); BASE.set(key, clean); return; }
  const changes = diffPaths(base, clean); if(!changes.length) return;
  const args = []; changes.forEach(([segs, v])=>{ args.push(new FieldPath(...segs), v); });
  await updateDoc(ref, ...args); BASE.set(key, clean);
}
function persistDoc(coll, id, delay=500){
  if(!id) return;
  const key = coll+"/"+id; dirty.add(key);
  clearTimeout(timers[key]);
  timers[key] = setTimeout(()=>{
    const data = MAPS[coll]().get(id);
    chain = chain.then(()=> writeDoc(coll, id, data))
      .then(()=>{ dirty.delete(key); })
      .catch(e=>{ dirty.delete(key); console.error(e); toast(e && e.code==="permission-denied" ? "Bu değişikliği kaydetme yetkin yok" : "Kaydedilemedi, internet bağlantını kontrol et"); });
  }, delay);
}
const save = () => persistDoc("students", sid());
let setTimer = null, setDirty = false;
function saveSettings(delay=0){ setDirty = true; clearTimeout(setTimer); setTimer = setTimeout(()=>{ chain = chain.then(()=>setDoc(doc(fdb,"settings","main"), JSON.parse(JSON.stringify(S.settings)))).then(()=>{ setDirty=false; }).catch(()=>{ setDirty=false; toast("Ayarlar kaydedilemedi"); }); }, delay); }
function notify(type, data){ const id = uid(); S.notifs.set(id, {type, at:nowISO(), read:false, ...data}); persistDoc("notifs", id, 0); }

const loaded = {};
function applySnap(coll, snap){
  const m = MAPS[coll](), seen = new Set();
  snap.docs.forEach(d=>{ seen.add(d.id); if(!dirty.has(coll+"/"+d.id)){ const v = JSON.parse(JSON.stringify(d.data())); m.set(d.id, v); BASE.set(coll+"/"+d.id, JSON.parse(JSON.stringify(v))); } });
  [...m.keys()].forEach(k=>{ if(!seen.has(k) && !dirty.has(coll+"/"+k)) m.delete(k); });
}
function watchColl(coll, need){
  unsubs.push(onSnapshot(collection(fdb, coll), snap=>{ applySnap(coll, snap); loaded[coll]=true; checkReady(need); render(true); },
    e=>{ console.error(coll, e); loaded[coll]=true; checkReady(need); render(); }));
}
function watchSettings(need){
  unsubs.push(onSnapshot(doc(fdb,"settings","main"), s=>{ if(s.exists() && !setDirty){ S.settings = {...S.settings, ...JSON.parse(JSON.stringify(s.data()))}; } loaded.settings=true; checkReady(need); render(true); },
    e=>{ console.error("settings", e); loaded.settings=true; checkReady(need); render(); }));
}
function checkReady(need){ if(!S.ready && need.every(k=>loaded[k])){ S.ready = true; if(S.role==="student") startStudent(S.me); openDeepLink(); render(); pushSupported().then(()=>{ refreshPush(); render(); }); } }
function openDeepLink(){ const v = new URLSearchParams(location.search).get("ac"); if(!v) return; if(v==="program"){ S.view="program"; S.pmode="gun"; S.day=today(); if(st()) S.week=curStart(st()); } else if(v==="bildirim") S.view="bildirim"; history.replaceState(null, "", "/"); }
function stopWatching(){ unsubs.forEach(u=>{ try{ u(); }catch(e){} }); unsubs = []; BASE.clear(); for(const k in loaded) delete loaded[k]; S.students.clear(); S.notifs.clear(); S.cnotes.clear(); S.ready = false; }

let authResolved = false;
function init(){
  onAuthStateChanged(auth, user=>{
    authResolved = true; stopWatching();
    if(!user){ S.role=null; S.me=null; render(); return; }
    if(user.email === COACH_EMAIL){
      S.role = "admin"; S.me = null; S.view = "ozet";
      const need = ["students","notifs","coachNotes","settings"]; need.slice(0,3).forEach(c=>watchColl(c, need)); watchSettings(need);
    } else {
      S.role = "student"; S.me = user.uid; S.view = "home";
      const need = ["students","settings"];
      unsubs.push(onSnapshot(doc(fdb,"students",user.uid), s=>{ if(!dirty.has("students/"+user.uid)){ if(s.exists()){ const v = JSON.parse(JSON.stringify(s.data())); S.students.set(user.uid, v); BASE.set("students/"+user.uid, JSON.parse(JSON.stringify(v))); } else S.students.delete(user.uid); } loaded.students=true; checkReady(need); render(true); },
        e=>{ console.error(e); loaded.students=true; checkReady(need); render(); }));
      watchSettings(need);
    }
    render();
  });
}
function startStudent(id){
  S.me=id; S.view="home"; S.day=today(); S.week=S.students.get(id) ? curStart(S.students.get(id)) : monday(new Date());
  const s = S.students.get(id); if(s && s.lastSeen!==today()){ s.lastSeen = today(); persistDoc("students", id); }
}
/* Koçun başka bir öğrenciye hesap açabilmesi için ikinci bir Firebase örneği (koçun oturumu etkilenmez) */
let secAuth = null;
function secondaryAuth(){ if(!secAuth){ const app2 = initializeApp(firebaseConfig, "ikincil"); secAuth = initializeAuth(app2, {persistence: inMemoryPersistence}); } return secAuth; }
async function createStudentAccount(u, p){
  const a = secondaryAuth(); const cred = await createUserWithEmailAndPassword(a, emailOf(u), p); const id = cred.user.uid; await signOut(a); return id;
}
const authMsg = e => ({ "auth/email-already-in-use":"Bu kullanıcı adı alınmış, başka bir tane dene.", "auth/invalid-credential":"Kullanıcı adı veya şifre hatalı.", "auth/wrong-password":"Kullanıcı adı veya şifre hatalı.", "auth/user-not-found":"Kullanıcı adı veya şifre hatalı.", "auth/too-many-requests":"Çok fazla deneme yapıldı. Birkaç dakika sonra tekrar dene.", "auth/network-request-failed":"İnternet bağlantısı yok gibi görünüyor.", "auth/weak-password":"Şifre en az 6 karakter olmalı.", "auth/requires-recent-login":"Güvenlik için çıkış yapıp tekrar girmen gerekiyor." }[e && e.code] || ("Bir sorun oldu: " + (e && (e.code || e.message) || e)));

/* ---------- Telefon bildirimleri ---------- */
const fns = getFunctions(fbApp, "europe-west3");
const callFn = (name, data) => httpsCallable(fns, name)(data).then(r => r.data);
const isIOS = () => /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
const isStandalone = () => window.matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
let pushOk = null;
async function pushSupported(){ if(pushOk !== null) return pushOk; try{ pushOk = !!vapidKey && "Notification" in window && "serviceWorker" in navigator && await messagingSupported(); }catch(e){ pushOk = false; } return pushOk; }
/* Bildirim kartının durumu: "hazir" (açık), "ac" (izin istenebilir), "ios" (önce ana ekrana eklenmeli), "red" (reddedilmiş), null (desteklenmiyor) */
function pushState(){
  if(!vapidKey) return null;
  if(isIOS() && !isStandalone()) return "ios";
  if(!("Notification" in window) || pushOk === false) return null;
  if(Notification.permission === "denied") return "red";
  if(Notification.permission === "granted") return "hazir";
  return "ac";
}
async function enablePush(){
  if(!(await pushSupported())){ toast("Bu tarayıcı bildirimleri desteklemiyor"); return; }
  const perm = await Notification.requestPermission();
  if(perm !== "granted"){ toast("Bildirim izni verilmedi"); render(); return; }
  try{
    const reg = await navigator.serviceWorker.register("/sw.js");
    const token = await getToken(getMessaging(fbApp), { vapidKey, serviceWorkerRegistration: reg });
    if(!token) throw new Error("token yok");
    if(A()){ await setDoc(doc(fdb, "coachDevices", token.slice(-40).replace(/[^A-Za-z0-9_-]/g,"_")), { token, at: nowISO(), ua: navigator.userAgent.slice(0,120) }); }
    else { const s = st(); s.bildirim = s.bildirim || {}; s.bildirim.tokens = {...(s.bildirim.tokens||{}), [token]: nowISO()}; s.bildirim.izin = "granted"; save(); }
    try{ localStorage.setItem("zk-push", token); }catch(e){}
    toast("Bildirimler açıldı"); render();
  }catch(e){ console.error(e); toast("Bildirimler açılamadı, biraz sonra tekrar dene"); }
}
/* İzin daha önce verildiyse cihaz anahtarını sessizce tazele */
async function refreshPush(){
  try{ if(!(await pushSupported()) || Notification.permission !== "granted") return;
    const reg = await navigator.serviceWorker.register("/sw.js");
    const token = await getToken(getMessaging(fbApp), { vapidKey, serviceWorkerRegistration: reg }); if(!token) return;
    if(A()) await setDoc(doc(fdb, "coachDevices", token.slice(-40).replace(/[^A-Za-z0-9_-]/g,"_")), { token, at: nowISO(), ua: navigator.userAgent.slice(0,120) });
    else { const s = st(); if(s && !(s.bildirim && s.bildirim.tokens && s.bildirim.tokens[token])){ s.bildirim = s.bildirim || {}; s.bildirim.tokens = {...(s.bildirim.tokens||{}), [token]: nowISO()}; s.bildirim.izin = "granted"; save(); } }
  }catch(e){ console.warn("push yenileme", e); }
}
function pushCard(){
  const k = pushState(); if(!k || k === "hazir") return "";
  if(k === "ios") return `<div class="card" style="background:var(--acs);border:0"><h3>${icon("bell","sm")} Bildirimleri almak için</h3><p class="muted small" style="margin:6px 0 0">iPhone’da önce uygulamayı ana ekrana ekle: Safari’de alttaki <b>Paylaş</b> simgesine dokun → <b>Ana Ekrana Ekle</b>. Sonra uygulamayı ana ekrandaki simgeden aç.</p></div>`;
  if(k === "red") return `<div class="card"><h3>${icon("bell","sm")} Bildirimler kapalı</h3><p class="muted small" style="margin:6px 0 0">Bildirim izni reddedilmiş. Açmak için telefonun ayarlarından bu uygulamanın bildirim iznini aç.</p></div>`;
  return `<div class="card" style="background:var(--acs);border:0"><div class="sech"><h3>${icon("bell","sm")} Bildirimleri aç</h3></div><p class="muted small" style="margin:6px 0 10px">${A()?"Yeni öğrenci kaydolduğunda bu cihaza bildirim gelsin.":"Koçunun sabah mesajları ve akşam hatırlatmaları telefonuna gelsin."}</p><button class="btn sm pri" data-act="pushon">Bildirimlere izin ver</button></div>`;
}

/* ---------- Hesaplar ---------- */
const netOf = v => v==null ? null : typeof v==="number" ? v : typeof v==="object" ? ((num(v.d)||0)-(num(v.y)||0)/4) : num(v);
const tytTotal = d => TYTF.reduce((a,[k])=>a+(netOf(d[k])||0),0);
const aytTotal = d => AYTF.reduce((a,[k])=>a+(netOf(d[k])||0),0);
const totalOf = d => d.tur==="TYT" ? tytTotal(d) : aytTotal(d);
const exams = (s, tur) => (s.denemeler||[]).filter(d=>d.tur===tur).sort((a,b)=>a.tarih<b.tarih?-1:a.tarih>b.tarih?1:0);
function topicScore(t){ if(!t) return 0; return ((t.r>0?1:0)+(t.s1?1:0)+(t.s2?1:0))/3; }
function subjPct(s, sub){ let sum=0; sub.t.forEach(n=>sum+=topicScore(s.topics[tkey(sub.k,n)])); return sub.t.length? sum/sub.t.length : 0; }
function aytSubjects(s, all){ return CURX().AYT.filter(x=> all || !ALANLAR.includes(s.alan) ? true : x.a.includes(s.alan)); }
function examPct(s, ex){ const list = ex==="TYT"? CURX().TYT : aytSubjects(s,false); let sum=0,c=0; list.forEach(sub=>sub.t.forEach(n=>{sum+=topicScore(s.topics[tkey(sub.k,n)]);c++;})); return c? sum/c : 0; }
/* Program dönemleri: hafta başı = son "yeni görüşme" günü. Görüşme yoksa Pazartesi. */
const dDiff = (a,b) => Math.round((new Date(b+"T12:00:00")-new Date(a+"T12:00:00"))/864e5);
const anchors = s => (s.donem||[]).slice().sort();
function pStart(s, d){ const an = anchors(s).filter(a=>a<=d); if(!an.length) return monday(d); const a = an[an.length-1]; return addDays(a, Math.floor(dDiff(a,d)/7)*7); }
function pLen(s, st){ const nx = anchors(s).find(a=>a>st); return nx ? Math.min(7, dDiff(st,nx)) : 7; }
const pDays = (s, st) => [...Array(pLen(s,st))].map((_,i)=>addDays(st,i));
const pIdx = (s, d) => dDiff(pStart(s,d), d);
const pEnd = (s, st) => addDays(st, pLen(s,st)-1);
const pPrev = (s, st) => pStart(s, addDays(st,-1));
const pNext = (s, st) => addDays(st, pLen(s,st));
const curStart = s => pStart(s, today());
const dayTasks = (s, date) => ((s.weeks||{})[pStart(s,date)]||{})[pIdx(s,date)] || [];
function setDayTasks(s, date, list){ const w = pStart(s,date); s.weeks = s.weeks||{}; s.weeks[w] = s.weeks[w]||{}; s.weeks[w][pIdx(s,date)] = list; }
function timerMin(s){ return s.timer && s.timer.start ? (Date.now()-s.timer.start)/60000 : 0; }
function minutes(s, date, live=true){ let m = (s.gunluk||{})[date]||0; if(live && s.timer && s.timer.start && iso(new Date(s.timer.start))===date) m += timerMin(s); return m; }
function weekStats(s, w){ let all=0,done=0,min=0; for(const d of pDays(s,w)){ const l=dayTasks(s,d); all+=l.length; done+=l.filter(t=>t.done).length; min+=minutes(s,d); } return {all,done,min,pct: all? done/all : null}; }
function active(s, d){ return minutes(s,d,false)>0 || dayTasks(s,d).some(t=>t.done) || (s.timer && iso(new Date(s.timer.start))===d); }
function streak(s){ let c=0, d=today(); if(!active(s,d)) d=addDays(d,-1); while(active(s,d) && c<400){ c++; d=addDays(d,-1); } return c; }
function lastActivity(s){
  let best = s.lastSeen || "";
  Object.entries(s.gunluk||{}).forEach(([d,m])=>{ if(m>0 && d>best) best=d; });
  Object.values(s.weeks||{}).forEach(w=>Object.values(w).forEach(l=>(l||[]).forEach(t=>{ if(t.doneAt && t.doneAt>best) best=t.doneAt; })));
  return best;
}
function coachMetrics(s){
  const w = weekStats(s, curStart(s));
  const t = exams(s,"TYT"), last = t[t.length-1], prev = t[t.length-2];
  const lt = last ? tytTotal(last) : null, dlt = last && prev ? tytTotal(last)-tytTotal(prev) : null;
  const la = lastActivity(s); const idle = la ? Math.round((new Date(today()+"T12:00:00")-new Date(la+"T12:00:00"))/864e5) : null;
  const flags = [];
  if(w.pct!=null && w.pct<0.5 && pIdx(s,today())>=2) flags.push(["bad","Program uyumu düşük"]);
  if(idle==null) flags.push(["warn","Henüz hareket yok"]); else if(idle>=3) flags.push(["bad",idle+" gündür hareket yok"]);
  if(dlt!=null && dlt<0) flags.push(["warn","Son TYT’de düşüş"]);
  if(w.all===0) flags.push(["warn","Bu hafta programı yok"]);
  const score = flags.reduce((a,f)=>a+(f[0]==="bad"?2:1),0);
  return {w, lt, dlt, idle, flags, score, streak:streak(s)};
}
const accountOf = id => { const x = S.students.get(id); return x && x.kullanici ? {u:x.kullanici} : null; };
const examDays = () => Math.max(0, Math.ceil((new Date(S.settings.examDate+"T10:00:00") - new Date())/864e5));

/* ---------- Ortak parçalar ---------- */
function ring(p, label){
  const r=32, c=2*Math.PI*r;
  return `<div class="ring"><svg viewBox="0 0 76 76"><circle cx="38" cy="38" r="${r}" fill="none" stroke="currentColor" stroke-opacity=".25" stroke-width="7"/><circle cx="38" cy="38" r="${r}" fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round" stroke-dasharray="${c}" stroke-dashoffset="${c*(1-(p||0))}"/></svg><b>${label}</b></div>`;
}
const tile = (cls, ic, val, lbl, id="") => `<div class="tile ${cls}"><div class="ic">${icon(ic,"sm")}</div><b class="num" ${id?`id="${id}"`:""}>${val}</b><span>${lbl}</span></div>`;
function topbar(title, right="", left=""){
  return `<header class="top ${A()?"wide":""}"><div class="topin">${left}${title}<span class="spacer"></span>${right}</div></header>`;
}
function bellBtn(count){ return `<button class="iconbtn" data-act="${A()?"go":"bell"}" data-v="bildirim" aria-label="Bildirimler">${icon("bell")}${count?`<span class="dot">${count}</span>`:""}</button>`; }

/* ---------- Ana render ---------- */
let lastRenderKey = "";
function render(fromSnap){
  const root = $("#root");
  if(!S.role){
    if(!authResolved){ root.innerHTML = `<div class="auth"><div class="apanel" style="align-items:center;padding-top:30vh"><div class="lm" style="width:56px;height:56px;font-size:28px">Z</div><p class="muted">Panelin açılıyor…</p></div></div>`; return; }
    if(fromSnap && $("#root .auth form") && root.contains(document.activeElement)){ const b = $("#root .auth form .btn.pri"); if(b && b.disabled){ b.disabled=false; b.textContent=b.dataset.label; } return; }
    renderAuth(); return;
  }
  if(!S.ready){ root.innerHTML = `<div class="auth"><div class="apanel" style="align-items:center;padding-top:30vh"><div class="lm" style="width:56px;height:56px;font-size:28px">Z</div><p class="muted">Panelin açılıyor…</p></div></div>`; return; }
  if(S.role==="student" && !S.students.has(S.me)){ root.innerHTML = `<div class="auth"><div class="apanel" style="padding-top:20vh"><h2>Kaydın bulunamadı</h2><p class="muted">Hesabına ait öğrenci kaydı silinmiş olabilir. Koçunla iletişime geç.</p><button class="btn" data-act="logout">Çıkış yap</button></div></div>`; return; }
  if(S.role==="student" && st().ilkSifre){ renderFirstPassword(); return; }
  if(fromSnap && document.activeElement && root.contains(document.activeElement) && document.activeElement.matches("input[type=text],input[type=number],textarea,select")) return;
  const y = window.scrollY;
  root.innerHTML = A() ? coachShell() : studentShell();
  window.scrollTo(0, y);
}
function navHTML(items){
  return `<nav class="nav" aria-label="Menü"><div class="navin">${items.map(([v,ic,l,fab,cnt])=>`<button class="nb ${fab?"fab":""}" data-act="go" data-v="${v}" aria-current="${S.view===v||(v==="program"&&S.view==="program")?"page":"false"}">${fab?`<span class="bub">${icon(ic)}</span>`:icon(ic)}<span class="l">${l}</span>${cnt?`<span class="cnt">${cnt}</span>`:""}</button>`).join("")}</div></nav>`;
}

/* ---------- Öğrenci ---------- */
function studentNotices(s){
  const out = [];
  if(s.koctanNot && s.koctanNot.text && (s.koctanNot.date||"") > (s.notSeen||"")) out.push(["note","Koçundan yeni not", s.koctanNot.text.slice(0,90)]);
  if(s.programYeni && s.programYeni > (s.programSeen||"")) out.push(["cal","Yeni haftalık programın hazır", `Koçun ${GUN[dIdx(curStart(s))]} gününden başlayan yeni programını hazırladı.`]);
  const ev = eveningMsg(s); if(ev) out.push(["moon","Akşam hatırlatması", ev.text]);
  const mm = morningMsg(s, S.me); if(mm) out.push(["sun","Günün mesajı", mm]);
  return out;
}
function studentShell(){
  const s = st(); if(!s) return "";
  const pages = {home:sHome, program:()=>pProgram(s,false), analiz:()=>pAnaliz(s), konular:()=>pKonular(s), daha:sMore, cetele:()=>pCetele(s), kronometre:()=>pCalisma(s), bildirim:sBell};
  const nots = studentNotices(s).length;
  return `<div class="shell">${(pages[S.view]||sHome)(s)}</div>` + navHTML([["home","home","Ana Sayfa"],["analiz","chart","Analiz"],["program","cal","Haftalık Program",true],["konular","book","Konular"],["daha","more","Daha Fazla", false, 0]]);
}
function sHome(s){
  const t = today(), tl = dayTasks(s,t), done = tl.filter(x=>x.done).length;
  const w = weekStats(s, curStart(s));
  const lt = exams(s,"TYT").pop();
  const h = new Date().getHours();
  const nots = studentNotices(s);
  const msg = !tl.length ? "Bugün için görev yok, kronometreyle çalışmanı kaydedebilirsin." : done===tl.length ? "Bugünün tüm görevleri tamam. Harikasın!" : done ? `${done} görevi tamamladın, devam!` : "Hadi ilk görevle başlayalım.";
  const ev = eveningMsg(s), mm = ev ? null : morningMsg(s, S.me);
  return `${topbar(`<div class="logo"><span class="lm">${esc(cfg().kurum.slice(0,1).toLocaleUpperCase("tr"))}</span>${esc(cfg().kurum)}</div>`, bellBtn(nots.length))}
  <div class="page">
    <div class="hellorow"><div class="hello"><p class="small" style="margin:0 0 2px">${longToday()}</p><h1>Merhaba, ${esc(firstName(s.name))} 👋</h1><p>Hedefine bir adım daha yaklaşıyorsun.</p></div>
      <div class="cd">${icon("cal","sm")}<div><b class="num">${examDays()} gün</b><small>YKS’ye kaldı</small></div></div></div>
    ${pushCard()}
    ${ev?`<div class="card evening"><div class="sech"><h3>${icon("moon","sm")} Koçundan akşam hatırlatması</h3></div><p style="margin:8px 0 12px;font-weight:600">${esc(ev.text)}</p><div class="pills">${ev.missTasks?`<button class="btn sm pri" data-act="go" data-v="program">${icon("check","xs")} Görevleri işaretle</button>`:""}${ev.missTime?`<button class="btn sm ${ev.missTasks?"":"pri"}" data-act="go" data-v="kronometre">${icon("timer","xs")} Süremi gir</button>`:""}</div></div>`:""}
    ${mm?`<div class="card morning"><div class="sech"><h3>${icon("sun","sm")} Günün mesajı</h3><span class="faint small">Koçundan</span></div><p style="margin:8px 0 0;font-weight:600;font-size:16px;line-height:1.5">${esc(mm)}</p></div>`:""}
    <div class="tiles">
      ${tile("t-g","clock",fmtMin(minutes(s,t)),dayTarget(s,t)?`Bugün çalışma · hedef ${fmtH(dayTarget(s,t))}`:"Bugün çalışma","liveMin")}
      ${tile("t-a","check",`${done}/${tl.length}`,"Görev tamamlandı")}
      ${tile("t-w","target",w.pct==null?"—":"%"+Math.round(w.pct*100),"Haftalık program uyumu")}
      ${tile("t-r","flame",streak(s)+" gün","Çalışma serisi")}
    </div>
    <button class="hero" data-act="go" data-v="program" style="text-align:left;width:100%">${ring(tl.length?done/tl.length:0, `${done}/${tl.length}`)}<div><h3>Bugünkü Program</h3><p>${msg}</p></div><span class="go">${icon("chev")}</span></button>
    <div class="card"><div class="sech"><h3>Bugünün Görevleri</h3><button class="link" data-act="go" data-v="program">Tümünü gör</button></div>
      <div class="tasks" style="margin-top:6px">${tl.length? tl.map(x=>taskRow(x,t,{canTick:true})).join("") : `<div class="empty">Koçun bugüne görev eklemedi.</div>`}</div></div>
    ${goalsCard(s, curStart(s), {compact:true})}
    <div class="tiles" style="grid-template-columns:repeat(2,minmax(0,1fr))">
      ${tile("t-a","trend", lt?fmt(tytTotal(lt)):"—", lt?`Son TYT neti · ${shortDate(lt.tarih)}`:"Henüz TYT denemesi yok")}
      ${tile("t-g","clock", fmtMin(w.min), "Bu hafta toplam çalışma")}
    </div>
    ${s.koctanNot&&s.koctanNot.text?`<div class="card note"><span class="av">${icon("grad","sm")}</span><div style="min-width:0"><div class="sech"><b>Koçundan not</b><span class="faint small">${s.koctanNot.date?shortDate(s.koctanNot.date.slice(0,10)):""}</span></div><p style="margin:4px 0 0;white-space:pre-wrap">${esc(s.koctanNot.text)}</p></div></div>`:""}
    <div><div class="sec" style="margin-bottom:10px">Hızlı Erişim</div><div class="qa">
      <button class="qb" data-act="go" data-v="kronometre"><span class="ic">${icon("timer")}</span>Kronometre</button>
      <button class="qb" data-act="sheet" data-v="deneme"><span class="ic">${icon("chart")}</span>Deneme ekle</button>
      <button class="qb" data-act="go" data-v="cetele"><span class="ic">${icon("list")}</span>Çetele</button>
      <button class="qb" data-act="go" data-v="konular"><span class="ic">${icon("book")}</span>Konular</button>
    </div></div>
  </div>`;
}
function sBell(s){
  const n = studentNotices(s);
  if(s.koctanNot && s.koctanNot.date && s.koctanNot.date > (s.notSeen||"")){ s.notSeen = s.koctanNot.date; save(); }
  return `${topbar(`<h1 class="ttl">Bildirimler</h1>`, "", `<button class="iconbtn" data-act="go" data-v="home" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page"><div class="card">${n.length? n.map(([ic,t,d])=>`<div class="row"><span class="ri">${icon(ic,"sm")}</span><div style="min-width:0"><div class="rt">${esc(t)}</div><div class="rs">${esc(d)}</div></div></div>`).join("") : `<div class="empty">Şimdilik yeni bir şey yok.</div>`}</div>
  <p class="faint small" style="text-align:center">Gerçek uygulamada bu hatırlatmalar telefonuna bildirim olarak da gelecek.</p></div>`;
}
function sMore(s){
  return `${topbar(`<h1 class="ttl">Daha Fazla</h1>`)}
  <div class="page">
    <div class="card note"><span class="av">${esc(initials(s.name))}</span><div><b>${esc(s.name)}</b><div class="muted small">${esc(s.alan)} · ${esc(s.sinif)}${s.okul?" · "+esc(s.okul):""}</div><div class="faint small">@${esc(s.kullanici||"")}</div></div></div>
    <div class="card">
      <button class="row" data-act="go" data-v="kronometre"><span class="ri">${icon("timer","sm")}</span><div><div class="rt">Kronometre ve çalışma süresi</div><div class="rs">Bugün ${fmtMin(minutes(s,today()))}</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="go" data-v="cetele"><span class="ri">${icon("list","sm")}</span><div><div class="rt">Yanlış çetelesi</div><div class="rs">Konu konu yanlışlarını işaretle</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="go" data-v="bildirim"><span class="ri">${icon("bell","sm")}</span><div><div class="rt">Bildirimler</div><div class="rs">Hatırlatmalar ve koçundan notlar</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="sheet" data-v="tema"><span class="ri">${icon("palette","sm")}</span><div><div class="rt">Görünüm</div><div class="rs">Açık / koyu mod ve tema rengi</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="logout"><span class="ri">${icon("logout","sm")}</span><div><div class="rt">Çıkış yap</div><div class="rs">“Beni hatırla” bu cihazda sıfırlanır</div></div></button>
    </div>
    <p class="proto">Zekacademy</p>
  </div>`;
}

/* ---------- Paylaşılan sayfalar ---------- */
/* ---------- Program: haftalık hedefler + günlük plan ---------- */
const DEF_HEDEF_DERS = ["Matematik","Geometri","Fizik","Kimya","Biyoloji","Türkçe","Tarih","Coğrafya","Felsefe","Edebiyat","Din Kültürü"];
const DEF_QUICK = ["Problem 20 soru","Paragraf 20 soru","TYT Matematik Branş x1","Türkçe Branş x1","Fen Branş x1","Sos Branş x1","AYT Matematik Branş x1","AYT Fen Branş x1","AYT Genel Deneme + Analiz","AYT Matematik Çalışması (2,5 saat)","AYT Fizik Çalışması (2 saat)","AYT Kimya Çalışması (2 saat)","AYT Biyoloji Çalışması (2 saat)","TYT Geometri Çalışması (2 saat)","TYT Genel Deneme + Analiz","AYT Fen O Hafta Tekrar (2 saat)"];
const taskText = t => t.d ? [t.d, t.t, t.soru ? t.soru+" soru" : ""].filter(Boolean).join(" · ") : (t.t||"");
/* Koçun ortalama süreleri: satırda süre yazmıyorsa kullanılır. Kelimeler satırda geçmeli (kısaltma olabilir: "mat" → "Matematik"); xN ile çarpılır. */
const DEF_SURELER = [{k:"ayt genel deneme",dk:210},{k:"genel deneme",dk:180},{k:"ayt fen branş",dk:90},{k:"ayt mat branş",dk:120},{k:"mat branş",dk:60},{k:"türkçe branş",dk:60},{k:"fen branş",dk:30},{k:"sos branş",dk:30}];
const trWords = x => String(x||"").toLocaleLowerCase("tr").split(/[^a-zçğıöşü0-9]+/).filter(Boolean);
function ruleFor(text){
  const toks = trWords(text);
  return cfg().sureler.filter(r=>r.k && r.dk).map(r=>({r, w:trWords(r.k)})).filter(x=>x.w.length && x.w.every(w=>toks.some(t=>t.startsWith(w)))).sort((a,b)=>b.w.length-a.w.length)[0]?.r || null;
}
function parseHours(text){
  const t = String(text||"");
  let h = 0; const m1 = t.match(/(\d+(?:[.,]\d+)?)\s*(saat|sa)\b/i); if(m1) h += parseFloat(m1[1].replace(",","."));
  const m2 = t.match(/(\d+)\s*(dk|dakika)\b/i); if(m2) h += (+m2[1])/60;
  if(h) return h;
  const rule = ruleFor(t); if(!rule) return 0;
  const low = t.toLocaleLowerCase("tr"), x = low.match(/\bx\s*(\d+)\b/) || low.match(/\b(\d+)\s*x\b/);
  return (+rule.dk/60) * (x ? Math.max(1, +x[1]) : 1);
}
const plan = (s,w) => ((s.plan||{})[w]) || {};
function ensurePlan(s,w){ s.plan = s.plan||{}; s.plan[w] = s.plan[w]||{}; const p = s.plan[w]; p.saat = p.saat||{}; p.hedef = p.hedef||{}; return p; }
const autoHours = (s,d) => dayTasks(s,d).reduce((a,t)=>a+parseHours(taskText(t)),0);
function dayTarget(s,d){ const v = (plan(s,pStart(s,d)).saat||{})[pIdx(s,d)]; return v!=null && v!=="" ? +v : autoHours(s,d); }
const fmtH = h => h ? (Math.round(h*10)/10).toLocaleString("tr-TR")+" saat" : "—";
function weekGoals(s,w){ const h = plan(s,w).hedef||{}; const list = cfg().hedefDers.filter(d=>h[d] && h[d].konu); return {list, h, done:list.filter(d=>h[d].done).length}; }
const kitap = (s,d) => (s.kitaplar||{})[d] || "";
function linesToTasks(old, text){
  const pool = old.slice();
  return text.split("\n").map(x=>x.trim()).filter(Boolean).map(line=>{
    const i = pool.findIndex(o=>taskText(o)===line);
    if(i>=0){ const o = pool.splice(i,1)[0]; return {id:o.id, t:line, done:!!o.done, doneAt:o.doneAt||null}; }
    return {id:uid(), t:line, done:false, doneAt:null};
  });
}

function taskRow(t, date, opts){
  const h = parseHours(taskText(t));
  return `<div class="task ${t.done?"done":""}">
    <button class="tick" data-act="tick" data-date="${date}" data-id="${t.id}" aria-pressed="${!!t.done}" aria-label="${t.done?"Tamamlandı":"Tamamla"}">${icon("check","sm")}</button>
    <div style="min-width:0"><div class="tt" style="font-weight:600">${esc(taskText(t))}</div></div>
    ${h?`<span class="pill">${icon("clock","xs")}${fmtH(h)}</span>`:"<span></span>"}
  </div>`;
}
function goalsCard(s, w, opts={}){
  const {list, h, done} = weekGoals(s,w);
  if(!list.length) return opts.compact ? "" : `<div class="card"><h3>Bu haftanın hedefleri</h3><div class="empty">Koçun bu hafta için hedef konu girmedi.</div></div>`;
  return `<div class="card"><div class="sech"><h3>${opts.title||"Bu haftanın hedefleri"}</h3><span class="small ${done===list.length?"up":"muted"}" style="font-weight:700">${done}/${list.length} konu</span></div>
    <div class="tasks" style="margin-top:4px">${list.map(d=>`<div class="task ${h[d].done?"done":""}"><button class="tick" data-act="gtick" data-w="${w}" data-ders="${esc(d)}" aria-pressed="${!!h[d].done}" aria-label="${esc(d)} hedefi">${icon("check","sm")}</button>
      <div style="min-width:0"><div class="ts" style="font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--ac);text-decoration:none">${esc(d)}</div><div class="tt" style="font-weight:600">${esc(h[d].konu)}</div>${kitap(s,d)?`<div class="tm"><span>${icon("book","xs")}${esc(kitap(s,d))}</span></div>`:""}</div><span></span></div>`).join("")}</div></div>`;
}
function dayFooter(s, d){
  const tg = dayTarget(s,d), m = minutes(s,d), p = tg ? Math.min(1, m/60/tg) : 0;
  return `<div style="margin-top:12px;padding-top:12px;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:8px">
    <div class="sech small"><span class="muted" style="display:flex;gap:6px;align-items:center">${icon("clock","xs")} Çalışma süresi</span><span><b class="num">${fmtMin(m)}</b> <span class="faint">/ ${fmtH(tg)}</span></span></div>
    ${tg?`<div class="bar"><i style="width:${p*100}%;background:${p>=1?"var(--good)":"var(--ac)"}"></i></div>`:""}</div>`;
}

function pProgram(s, edit){ return edit ? planEditor(s) : studentProgram(s); }

function weekNav(s){ const w = S.week, an = (s.donem||[]).includes(w);
  return `<div class="wknav"><button class="iconbtn" data-act="wk" data-d="-1" aria-label="Önceki hafta">${icon("back","sm")}</button><b>${shortDate(w)} – ${shortDate(pEnd(s,w))}${w===curStart(s)?` <span class="pill ac">Bu hafta</span>`:""}${an?`<div class="faint small" style="font-weight:600">Görüşme: ${GUN[dIdx(w)]} ${shortDate(w)}</div>`:""}</b><button class="iconbtn" data-act="wk" data-d="1" aria-label="Sonraki hafta">${icon("chev","sm")}</button></div>`; }

function studentProgram(s){
  const w = S.week, t = today(), ws = weekStats(s,w), g = weekGoals(s,w);
  const PD = pDays(s,w); let tgW = 0; PD.forEach(d=>tgW += dayTarget(s, d));
  const strip = `<div class="strip">${PD.map(d=>{ const x=GUNK[dIdx(d)], l=dayTasks(s,d), all=l.length&&l.every(y=>y.done);
    return `<button class="dbtn ${d===t?"today":""}" data-act="day" data-v="${d}" aria-pressed="${S.pmode==="gun"&&S.day===d}">${x}<b class="num">${dNum(d)}</b>${l.length?`<i class="${all?"":"p"}"></i>`:""}</button>`; }).join("")}</div>`;
  const hero = `<div class="hero goal" style="display:flex"><div class="goalrow"><span class="ic2">${icon("target")}</span><div style="flex:1"><h3>Haftalık durum</h3><p>${ws.all?`${ws.done}/${ws.all} görev`:"Görev yok"}${g.list.length?` · ${g.done}/${g.list.length} hedef konu`:""} · ${fmtMin(ws.min)}${tgW?` / ${fmtH(tgW)}`:""}</p></div><b class="num" style="font-size:20px">%${ws.pct==null?0:Math.round(ws.pct*100)}</b></div><div class="bar"><i style="width:${(ws.pct||0)*100}%"></i></div></div>`;
  let body;
  if(S.pmode==="gun"){
    const d = S.day && PD.includes(S.day) ? S.day : (PD.includes(t) ? t : w);
    const l = dayTasks(s,d), dn = l.filter(x=>x.done).length;
    body = `<div class="card"><div class="sech"><h3>${GUN[dIdx(d)]}, ${shortDate(d)}</h3><span class="small ${dn===l.length&&l.length?"up":"muted"}" style="font-weight:700">${l.length?`${dn}/${l.length}`:""}</span></div>
      <div class="tasks" style="margin-top:4px">${l.length? l.map(x=>taskRow(x,d,{})).join("") : `<div class="empty">Bu gün için görev yok.</div>`}</div>${dayFooter(s,d)}
      ${d===t?`<button class="btn full" style="margin-top:12px" data-act="go" data-v="kronometre">${icon("timer","sm")} Kronometreyi aç</button>`:""}</div>
      ${goalsCard(s,w)}`;
  } else {
    let rows = "";
    for(const d of PD){ const l=dayTasks(s,d), dn=l.filter(x=>x.done).length, m=minutes(s,d), tg=dayTarget(s,d);
      rows += `<tr class="${d===t?"today":""}"><td>${GUNK[dIdx(d)]} <span class="faint">${dNum(d)}</span></td><td class="r num">${l.length?`${dn}/${l.length}`:"—"}</td><td class="r num faint">${tg?fmtH(tg).replace(" saat","s"):"—"}</td><td class="r num" style="${tg&&m/60>=tg?"color:var(--good)":""}">${m?fmtMin(m):"—"}</td></tr>`; }
    body = `${goalsCard(s,w)}<div class="card"><h3>Günlük tablo</h3><div class="wrapx"><table class="wtable" style="margin-top:8px"><thead><tr><th>Gün</th><th class="r">Görev</th><th class="r">Hedef</th><th class="r">Yapılan</th></tr></thead><tbody>${rows}</tbody>
      <tfoot><tr><td>Toplam</td><td class="r num">${ws.done}/${ws.all}</td><td class="r num faint">${tgW?fmtH(tgW).replace(" saat","s"):"—"}</td><td class="r num">${fmtMin(ws.min)}</td></tr></tfoot></table></div></div>`;
  }
  return `${topbar(`<h1 class="ttl">Programım</h1>`, `<button class="iconbtn" data-act="wk" data-d="0" aria-label="Bu haftaya dön">${icon("cal")}</button>`)}
  <div class="page">
    <div class="seg"><button data-act="pmode" data-v="gun" aria-pressed="${S.pmode==="gun"}">Günlük</button><button data-act="pmode" data-v="hafta" aria-pressed="${S.pmode==="hafta"}">Haftalık</button></div>
    ${weekNav(s)}${S.pmode==="gun"?strip:""}${hero}${body}
    <p class="faint small" style="text-align:center">Programını koçun hazırlıyor. Bitirdiğin satırı ve hedef konuyu işaretle; koçun anında görür.</p>
  </div>`;
}

function planEditor(s){
  const w = S.week, p = plan(s,w), h = p.hedef||{}, ws = weekStats(s,w), g = weekGoals(s,w);
  const quick = [...new Set([...cfg().quick, ...Object.values(s.weeks||{}).flatMap(x=>Object.values(x).flatMap(l=>(l||[]).map(taskText)))])].slice(0,40);
  const goals = `<div class="card"><div class="sech"><h3>Haftalık hedefler</h3><span class="faint small">${g.list.length?`Öğrenci ${g.done}/${g.list.length} işaretledi`:"Boş bırakılan ders öğrenciye görünmez"}</span></div>
    <div class="goalgrid" style="margin-top:10px"><div class="gh">Ders</div><div class="gh">Bitirilecek konu</div><div class="gh">Takip edilen kitaplar</div>
    ${cfg().hedefDers.map(d=>`<div class="gd">${h[d]&&h[d].konu?`<button class="tick sm" data-act="gtick" data-w="${w}" data-ders="${esc(d)}" aria-pressed="${!!h[d].done}" aria-label="${esc(d)} tamamlandı">${icon("check","xs")}</button>`:`<span class="tick sm ghost"></span>`}${esc(d)}</div>
      <input type="text" id="hk-${esc(d)}" data-hd="konu" data-ders="${esc(d)}" value="${esc(h[d]?.konu||"")}" placeholder="—">
      <input type="text" id="hb-${esc(d)}" data-hd="kitap" data-ders="${esc(d)}" value="${esc(kitap(s,d))}" placeholder="—">`).join("")}</div>
    <p class="faint small" style="margin:10px 0 0">Kitaplar haftadan haftaya otomatik taşınır; sadece değiştiğinde güncellemen yeterli.</p></div>`;
  const days = pDays(s,w).map((d,i)=>{ const g = GUN[dIdx(d)], l = dayTasks(s,d), dn = l.filter(x=>x.done).length, auto = autoHours(s,d), sv = (p.saat||{})[i];
    return `<div class="dcard ${d===today()?"today":""}"><div class="dch"><b>${g}</b><span class="faint small">${shortDate(d)}</span></div>
      <textarea id="pl-${i}" data-plan="${d}" rows="8" placeholder="Her satıra bir görev&#10;Problem 20 soru&#10;AYT Matematik Çalışması (2,5 saat)&#10;Fen Branş x1">${esc(l.map(taskText).join("\n"))}</textarea>
      <div class="dcf"><label class="hrs">Çalışma süresi<input type="number" min="0" max="16" step="0.5" id="ps-${i}" data-hs="${i}" value="${sv!=null&&sv!==""?sv:""}" placeholder="${auto?String(Math.round(auto*10)/10).replace(".",","):"0"}"> saat</label>
        <select class="qsel" data-quick="${d}" aria-label="${g} için hızlı ekle"><option value="">+ Hızlı ekle</option>${quick.map(q=>`<option>${esc(q)}</option>`).join("")}</select></div>
      <div class="dcs"><span>${l.length?`Öğrenci <b class="num">${dn}/${l.length}</b> işaretledi`:"Henüz görev yok"} · <b class="num">${fmtMin(minutes(s,d))}</b> çalıştı</span><button class="link small" data-act="sheet" data-v="copyday" data-date="${d}">${icon("copy","xs")} Kopyala</button></div></div>`; }).join("");
  return `<div style="display:flex;flex-direction:column;gap:14px">
    ${weekNav(s)}
    <div class="pills"><button class="btn sm pri" data-act="sheet" data-v="gorusme">${icon("plus","xs")} Yeni görüşme</button><button class="btn sm" data-act="copyweek">${icon("copy","xs")} Geçen haftayı bu haftaya kopyala</button><span class="faint small" style="align-self:center">Küçük değişiklikleri doğrudan yaz; otomatik kaydedilir.</span></div>
    ${goals}
    <div class="sech"><h3 class="sec">Günlük plan</h3><span class="faint small">${ws.all?`${ws.done}/${ws.all} görev tamamlandı`:""}</span></div>
    <details class="card" style="padding:12px 16px"><summary class="small" style="cursor:pointer;font-weight:700;color:var(--muted)">Süre yazmayan satırlar için ortalama süreler</summary>
      <div class="pills" style="margin-top:10px">${cfg().sureler.filter(r=>r.k&&r.dk).map(r=>`<span class="pill">${esc(r.k)} · <b>${fmtMin(r.dk)}</b></span>`).join("")}<button class="link small" data-act="go" data-v="ayarlar">Ayarlardan düzenle</button></div>
      <p class="faint small" style="margin:8px 0 0">Satırda “(2 saat)” gibi süre yazarsan o geçerli olur. “x2” yazarsan süre ikiyle çarpılır. Günün çalışma süresi kutusunu boş bırakırsan bu toplam kullanılır.</p></details>
    <div class="daygrid">${days}</div>
  </div>`;
}

function netChart(s, tur){
  const list = exams(s,tur).slice(-8); const max = tur==="TYT"?120:160; const hedef = num(s.hedef[tur.toLowerCase()]);
  if(!list.length) return `<div class="empty">Deneme eklendikçe net grafiğin burada oluşur.</div>`;
  const W=600,H=220,pl=10,pr=10,pt=26,pb=28;
  const vals = list.map(totalOf); if(hedef!=null) vals.push(hedef);
  let hi = Math.min(max, Math.ceil((Math.max(...vals)+8)/10)*10), lo = Math.max(0, Math.floor((Math.min(...vals)-10)/10)*10); if(hi-lo<20) hi=lo+20;
  const x = i => list.length===1 ? W/2 : pl+20 + i*(W-pl-pr-40)/(list.length-1);
  const y = v => pt + (1-(v-lo)/(hi-lo))*(H-pt-pb);
  const pts = list.map((d,i)=>[x(i), y(totalOf(d)), totalOf(d), d]);
  let g = `<defs><linearGradient id="ag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--ac)" stop-opacity=".28"/><stop offset="1" stop-color="var(--ac)" stop-opacity="0"/></linearGradient></defs>`;
  for(let k=0;k<4;k++){ const v = lo+(hi-lo)*k/3; g+=`<line x1="${pl}" x2="${W-pr}" y1="${y(v)}" y2="${y(v)}" stroke="var(--line)" stroke-dasharray="3 5"/>`; }
  if(hedef!=null){ g+=`<line x1="${pl}" x2="${W-pr}" y1="${y(hedef)}" y2="${y(hedef)}" stroke="var(--good)" stroke-width="1.5" stroke-dasharray="6 5"/><text x="${W-pr}" y="${y(hedef)-6}" text-anchor="end" font-size="12" font-weight="700" fill="var(--good)">Hedef ${fmt(hedef)}</text>`; }
  if(pts.length>1) g += `<path d="M${pts[0][0]},${H-pb} ${pts.map(p=>`L${p[0]},${p[1]}`).join(" ")} L${pts[pts.length-1][0]},${H-pb}Z" fill="url(#ag)"/><polyline points="${pts.map(p=>p[0]+","+p[1]).join(" ")}" fill="none" stroke="var(--ac)" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>`;
  pts.forEach((p,i)=>{ const last=i===pts.length-1; g+=`<circle cx="${p[0]}" cy="${p[1]}" r="${last?6:4.5}" fill="${last?"var(--ac)":"var(--surface)"}" stroke="var(--ac)" stroke-width="2.5"/><text x="${p[0]}" y="${p[1]-11}" text-anchor="middle" font-size="12.5" font-weight="${last?800:600}" fill="var(--fg)">${fmt(p[2])}</text><text x="${p[0]}" y="${H-8}" text-anchor="middle" font-size="11" fill="var(--faint)">${shortDate(p[3].tarih)}</text>`; });
  return `<div class="chart"><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${tur} net grafiği">${g}</svg></div>`;
}
function pAnaliz(s){
  const tur = S.ex, F = tur==="TYT"?TYTF:AYTF, list = exams(s,tur), last = list[list.length-1], prev = list[list.length-2];
  const tot = last ? totalOf(last) : null, dl = last&&prev ? tot-totalOf(prev) : null;
  const hedef = num(s.hedef[tur.toLowerCase()]), bas = num(s.baslangic[tur.toLowerCase()]);
  const head = A() ? "" : topbar(`<h1 class="ttl">Deneme Analizi</h1>`, `<button class="iconbtn" data-act="sheet" data-v="deneme" aria-label="Deneme ekle">${icon("plus")}</button>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    <div class="seg"><button data-act="ex" data-v="TYT" aria-pressed="${tur==="TYT"}">TYT</button><button data-act="ex" data-v="AYT" aria-pressed="${tur==="AYT"}">AYT</button></div>
    <div class="card">
      ${last?`<div class="muted small" style="font-weight:700">Son ${tur} denemen · ${esc(last.yayin||"")} · ${trDate(last.tarih)}</div>
      <div class="bignet" style="margin-top:6px"><div><b class="num">${fmt(tot)}</b><div class="muted">net</div></div>${dl!=null?`<div class="chipd ${dl>0?"up":dl<0?"down":"eq"}"><span class="num">${dl>0?"↑ +":dl<0?"↓ ":""}${fmt(dl)}</span><small>Önceki denemeye göre</small></div>`:""}</div>`
      :`<div class="empty">Henüz ${tur} denemesi yok.</div>`}
      <div style="margin-top:12px">${netChart(s,tur)}</div>
      ${hedef!=null&&tot!=null?`<div class="small muted" style="margin-top:6px">Hedefine <b class="num" style="color:var(--fg)">${fmt(Math.max(0,hedef-tot))}</b> net kaldı${bas!=null?` · Başlangıçtan bu yana <b class="num ${tot-bas>=0?"up":"down"}">${tot-bas>=0?"+":""}${fmt(tot-bas)}</b>`:""}</div>`:""}
      <button class="btn pri full" style="margin-top:14px" data-act="sheet" data-v="deneme">${icon("plus","sm")} ${tur} denemesi ekle</button>
    </div>
    ${last?`<div class="card"><div class="sech"><h3>Ders bazlı analiz</h3><span class="faint small">Son deneme</span></div><div style="margin-top:6px">${F.map(([k,n,mx,ab])=>{ const v = netOf(last[k]); const o = last[k] && typeof last[k]==="object" ? last[k] : null; const pv = prev ? netOf(prev[k]) : null;
      return `<div class="drow"><span class="ic">${ab}</span><div style="min-width:0"><div class="n">${n}${o?` <span class="faint" style="font-weight:600">· ${o.d||0}D ${o.y||0}Y</span>`:""}</div><div class="bar"><i style="width:${Math.max(0,(v||0)/mx*100)}%"></i></div></div><div class="v num">${fmt(v)}<small> / ${mx}</small>${pv!=null&&v!=null&&v!==pv?`<div class="small ${v>pv?"up":"down"}" style="text-align:right;font-weight:700">${v>pv?"+":""}${fmt(v-pv)}</div>`:""}</div></div>`; }).join("")}</div></div>`:""}
    ${list.length?`<div class="card"><h3>Tüm ${tur} denemeleri</h3><div class="dlist" style="margin-top:6px">${list.slice().reverse().map((d,i,arr)=>{ const t=totalOf(d), p=arr[i+1]?totalOf(arr[i+1]):null;
      return `<div class="it"><div style="min-width:0"><b>${esc(d.yayin||"Deneme")}</b><div class="muted small">${trDate(d.tarih)}</div></div><div class="tot num">${fmt(t)}${p!=null?` <span class="small ${t>=p?"up":"down"}">${t>=p?"+":""}${fmt(t-p)}</span>`:""}</div><button class="mini" data-act="ddel" data-id="${d.id}" aria-label="Denemeyi sil">${icon("trash","xs")}</button>
        <div class="det">${F.map(([k,n,mx,ab])=>{ const o=d[k]; return `<span>${ab}: <b class="num">${fmt(netOf(o))}</b>${o&&typeof o==="object"?` (${o.d||0}/${o.y||0})`:""}</span>`; }).join("")}</div></div>`; }).join("")}</div></div>`:""}
  </div>`;
}
function pKonular(s){
  const ex = S.ex, list = ex==="TYT" ? CURX().TYT : aytSubjects(s, S.aytAll), pct = examPct(s, ex);
  const head = A() ? "" : topbar(`<h1 class="ttl">Konu Takibi</h1>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    <div class="seg"><button data-act="ex" data-v="TYT" aria-pressed="${ex==="TYT"}">TYT</button><button data-act="ex" data-v="AYT" aria-pressed="${ex==="AYT"}">AYT</button></div>
    <div class="card"><div class="sech"><h3>${ex} ilerlemesi${ex==="AYT"?` · ${esc(s.alan)}`:""}</h3><b class="num">%${Math.round(pct*100)}</b></div><div class="bar" style="margin-top:10px"><i style="width:${pct*100}%"></i></div>
      <p class="muted small" style="margin:10px 0 0">Her konuda: tekrar sayısı, 1. ve 2. soru bankası. Üçü tamamlanan konu yeşil olur.</p>
      ${ex==="AYT"?`<div class="pills" style="margin-top:10px"><button class="tog" data-act="aytall" aria-pressed="${S.aytAll}">${S.aytAll?"Tüm AYT dersleri gösteriliyor":"Tüm AYT derslerini göster"}</button></div>`:""}</div>
    ${list.map(sub=>{ const p = subjPct(s,sub);
      return `<details class="subj"><summary><span><span class="sn">${esc(sub.n)}</span><span class="sg">${esc(sub.g)}</span></span><div class="bar"><i style="width:${p*100}%;${p>=1?"background:var(--good)":""}"></i></div><span class="pct num">%${Math.round(p*100)}</span></summary>
      ${sub.t.map(n=>{ const k=tkey(sub.k,n), t=s.topics[k]||{}, full=topicScore(t)>=1;
        return `<div class="trow ${full?"full":""}"><div class="tn">${full?icon("check","xs"):""}${esc(n)}</div>
          <div class="tctl"><span class="stepper lbl">Tekrar<button data-act="rep" data-k="${esc(k)}" data-d="-1" aria-label="Azalt">−</button><span class="num">${t.r||0}</span><button data-act="rep" data-k="${esc(k)}" data-d="1" aria-label="Artır">+</button></span>
          <button class="tog" data-act="sb" data-f="s1" data-k="${esc(k)}" aria-pressed="${!!t.s1}">${t.s1?icon("check","xs"):""}${esc(((s.sbAd||{})[sub.k]||[])[0]||"Soru B. 1")}</button>
          <button class="tog" data-act="sb" data-f="s2" data-k="${esc(k)}" aria-pressed="${!!t.s2}">${t.s2?icon("check","xs"):""}${esc(((s.sbAd||{})[sub.k]||[])[1]||"Soru B. 2")}</button></div>
          <input class="tnote" type="text" id="n-${esc(k)}" data-act="tnote" data-k="${esc(k)}" value="${esc(t.n||"")}" placeholder="Not ekle (ör. formülleri tekrar et)"></div>`; }).join("")}
      </details>`; }).join("")}
  </div>`;
}
function pCetele(s){
  const ex = S.ex, list = ex==="TYT" ? CURX().TYT : aytSubjects(s, S.aytAll);
  let max = 1, total = 0; list.forEach(sub=>sub.t.forEach(n=>{ const y=(s.topics[tkey(sub.k,n)]||{}).y||0; max=Math.max(max,y); total+=y; }));
  const head = A() ? "" : topbar(`<h1 class="ttl">Yanlış Çetelesi</h1>`, "", `<button class="iconbtn" data-act="go" data-v="daha" aria-label="Geri">${icon("back")}</button>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    <div class="seg"><button data-act="ex" data-v="TYT" aria-pressed="${ex==="TYT"}">TYT</button><button data-act="ex" data-v="AYT" aria-pressed="${ex==="AYT"}">AYT</button></div>
    <div class="card"><div class="sech"><h3>${ex} toplam yanlış</h3><b class="num" style="color:var(--bad);font-size:22px">${total}</b></div><p class="muted small" style="margin:6px 0 0">Deneme ve testlerden sonra yanlış yaptığın konuları burada işaretle. En çok yanlış yapılan konular koçunun özetinde görünür.</p></div>
    ${list.map(sub=>{ const tot = sub.t.reduce((a,n)=>a+((s.topics[tkey(sub.k,n)]||{}).y||0),0);
      return `<details class="subj" ${tot?"open":""}><summary><span><span class="sn">${esc(sub.n)}</span><span class="sg">${ex}</span></span><span></span><span class="pct num" style="color:${tot?"var(--bad)":"var(--faint)"}">${tot}</span></summary>
      ${sub.t.map(n=>{ const k=tkey(sub.k,n), y=(s.topics[k]||{}).y||0;
        return `<div class="trow" style="flex-direction:row;align-items:center;gap:12px"><div style="flex:1;min-width:0"><div class="tn">${esc(n)}</div>${y?`<div class="wbar" style="width:${y/max*100}%"></div>`:""}</div><span class="stepper"><button data-act="yan" data-k="${esc(k)}" data-d="-1" aria-label="Azalt">−</button><span class="num cnt ${y>=5?"hot":""}">${y}</span><button data-act="yan" data-k="${esc(k)}" data-d="1" aria-label="Artır">+</button></span></div>`; }).join("")}
      </details>`; }).join("")}
  </div>`;
}
function pCalisma(s){
  const t = today(), run = !!(s.timer && s.timer.start), w = curStart(s);
  const days = pDays(s,w); const mins = days.map(d=>minutes(s,d)); const mx = Math.max(60,...mins);
  const head = A() ? "" : topbar(`<h1 class="ttl">Kronometre</h1>`, "", `<button class="iconbtn" data-act="go" data-v="home" aria-label="Geri">${icon("back")}</button>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    ${A()?"":`<div class="card timer"><div class="tface ${run?"run":""}"><b class="num" id="tval">${clock(run?timerMin(s)*60:0)}</b><small>${run?"çalışıyorsun":"hazır"}</small></div>
      <div class="tbtns">${run?`<button class="bigbtn stop" data-act="tstop">${icon("stop","sm")} Bitir ve kaydet</button>`:`<button class="bigbtn" data-act="tstart">${icon("play","sm")} Çalışmaya başla</button>`}</div>
      <div class="muted small">Bugün toplam: <b class="num" style="color:var(--fg)" id="ttoday">${fmtMin(minutes(s,t))}</b></div></div>`}
    <div class="card"><div class="sech"><h3>Bu hafta çalışma</h3><b class="num">${fmtMin(mins.reduce((a,b)=>a+b,0))}</b></div>
      <div class="bars7">${days.map((d,i)=>`<button class="b7 ${d===t?"today":""}" data-act="sheet" data-v="sure" data-date="${d}" aria-label="${GUN[dIdx(d)]} süresini düzenle"><em class="num">${mins[i]?fmtMin(mins[i]):""}</em><i style="height:${mins[i]/mx*100}%"></i><span>${GUNK[dIdx(d)]}</span></button>`).join("")}</div>
      <p class="faint small" style="margin:10px 0 0">Bir güne dokunarak süreyi elle düzeltebilirsin.</p>
      <button class="btn full" style="margin-top:10px" data-act="sheet" data-v="sure" data-date="${t}">${icon("plus","sm")} Elle süre ekle</button></div>
  </div>`;
}
const clock = sec => { sec=Math.floor(sec); const h=Math.floor(sec/3600), m=Math.floor(sec%3600/60), s=sec%60; return (h?h+":":"")+String(m).padStart(2,"0")+":"+String(s).padStart(2,"0"); };

/* ---------- Koç ---------- */
function coachShell(){
  const unread = [...S.notifs.values()].filter(n=>!n.read).length;
  const pages = {ozet:cOzet, ogrenciler:cList, detay:cDetail, program:cProgram, bildirim:cBell, daha:cMore, ayarlar:cSettings};
  return `<div class="shell">${(pages[S.view]||cOzet)()}</div>` + navHTML([["ozet","home","Özet"],["ogrenciler","users","Öğrenciler"],["program","cal","Haftalık Program",true],["bildirim","bell","Bildirimler",false,unread],["daha","more","Daha Fazla"]]);
}
const sortedStudents = () => [...S.students.entries()].sort((a,b)=>a[1].name.localeCompare(b[1].name,"tr"));
function cOzet(){
  const all = sortedStudents().map(([id,s])=>({id,s,m:coachMetrics(s)}));
  const n = all.length, unread = [...S.notifs.values()].filter(x=>!x.read).length;
  const withP = all.filter(x=>x.m.w.pct!=null), avgP = withP.length ? withP.reduce((a,x)=>a+x.m.w.pct,0)/withP.length : null;
  const avgMin = n ? all.reduce((a,x)=>a+x.m.w.min,0)/n : 0;
  const att = all.filter(x=>x.m.score>0).sort((a,b)=>b.m.score-a.m.score);
  const q = normName(S.q);
  const rows = all.filter(x=>!q || normName(x.s.name).includes(q)).sort((a,b)=>b.m.score-a.m.score || a.s.name.localeCompare(b.s.name,"tr"));
  return `${topbar(`<div class="logo"><span class="lm">Z</span>Koç Paneli</div>`, bellBtn(unread))}
  <div class="page wide">
    <div class="hello"><p class="small" style="margin:0">${longToday()}</p><h1>Günaydın hocam</h1><p>Öğrencilerinin bu haftaki durumu. Bu sayfayı sadece sen görürsün.</p></div>
    <div class="kpis">
      ${tile("t-a","users",n,"Öğrenci")}
      ${tile("t-g","target",avgP==null?"—":"%"+Math.round(avgP*100),"Ortalama program uyumu")}
      ${tile("t-w","clock",fmtMin(avgMin),"Öğrenci başı haftalık çalışma")}
      ${tile("t-r","alert",att.length,"İlgilenmen gereken")}
    </div>
    ${att.length?`<div class="card"><div class="sech"><h3>Dikkat gerektirenler</h3></div><div style="margin-top:4px">${att.slice(0,6).map(x=>`<button class="srow" data-act="open" data-id="${x.id}"><span class="av">${esc(initials(x.s.name))}</span><div style="min-width:0"><b>${esc(x.s.name)}</b><div class="pills" style="margin-top:4px">${x.m.flags.map(f=>`<span class="pill ${f[0]}">${esc(f[1])}</span>`).join("")}</div></div><span class="rx faint">${icon("chev","sm")}</span></button>`).join("")}</div></div>`:""}
    <div class="card"><div class="sech"><h3>Tüm öğrenciler</h3><button class="btn sm pri" data-act="sheet" data-v="ogrenci">${icon("plus","xs")} Ekle</button></div>
      <div class="search" style="margin-top:12px">${icon("search","sm")}<input type="text" id="q" data-act="q" value="${esc(S.q)}" placeholder="Öğrenci ara"></div>
      <div style="margin-top:6px">${rows.length? rows.map(x=>studentRow(x)).join("") : `<div class="empty">${n?"Aramaya uyan öğrenci yok.":"Henüz öğrenci yok. Kayıt linkini öğrencilerine gönderebilir ya da buradan ekleyebilirsin."}</div>`}</div></div>
  </div>`;
}
function studentRow({id,s,m}){
  return `<button class="srow" data-act="open" data-id="${id}"><span class="av">${esc(initials(s.name))}</span><div style="min-width:0"><b>${esc(s.name)}</b> <span class="faint small">${esc(s.alan)} · ${esc(s.sinif)}</span>
    <div class="smet"><span>Uyum <b class="num">${m.w.pct==null?"—":"%"+Math.round(m.w.pct*100)}</b></span><span>Çalışma <b class="num">${fmtMin(m.w.min)}</b></span><span>Son TYT <b class="num">${fmt(m.lt)}</b>${m.dlt!=null?` <span class="${m.dlt>=0?"up":"down"}">${m.dlt>=0?"+":""}${fmt(m.dlt)}</span>`:""}</span><span>Seri <b class="num">${m.streak}</b></span></div></div>
    <span class="rx">${Object.keys(s.bildirim?.tokens||{}).length?`<span title="Bildirimleri açık" style="color:var(--good)">${icon("bell","xs")}</span>`:`<span title="Bildirimleri kapalı" style="opacity:.35">${icon("bell","xs")}</span>`}${m.flags.some(f=>f[0]==="bad")?`<span class="pill bad">!</span>`:""}${icon("chev","sm")}</span></button>`;
}
function cList(){
  const q = normName(S.q);
  const all = sortedStudents().map(([id,s])=>({id,s,m:coachMetrics(s)})).filter(x=>!q || normName(x.s.name).includes(q));
  return `${topbar(`<h1 class="ttl">Öğrenciler <span class="faint" style="font-weight:600">${S.students.size}</span></h1>`, `<button class="iconbtn" data-act="sheet" data-v="ogrenci" aria-label="Öğrenci ekle">${icon("plus")}</button>`)}
  <div class="page wide">
    <div class="search">${icon("search","sm")}<input type="text" id="q" data-act="q" value="${esc(S.q)}" placeholder="Öğrenci ara"></div>
    <div class="card">${all.length? all.map(studentRow).join("") : `<div class="empty">Öğrenci bulunamadı.</div>`}</div>
    <div class="card"><h3>Kayıt linki</h3><p class="muted small" style="margin:6px 0 0">Öğrencilerin bu uygulamanın linkinden “Kayıt ol” ile kendileri kaydolur. Her yeni kayıt Bildirimler’e düşer. Link: <b>${esc(location.origin)}</b></p></div>
  </div>`;
}
function cDetail(){
  const s = st(); if(!s){ S.view="ogrenciler"; return cList(); }
  const tabs = [["ozet","Özet"],["program","Program"],["analiz","Analiz"],["konular","Konular"],["cetele","Çetele"],["calisma","Çalışma"]];
  const acc = accountOf(S.cur);
  const body = {ozet:()=>cSummary(s), program:()=>pProgram(s,true), analiz:()=>pAnaliz(s), konular:()=>pKonular(s), cetele:()=>pCetele(s), calisma:()=>pCalisma(s)}[S.dtab] || (()=>cSummary(s));
  return `${topbar(`<div style="min-width:0;flex:1"><h1 class="ttl" style="font-size:20px">${esc(s.name)}</h1><div class="faint small">${esc(s.alan)} · ${esc(s.sinif)}${s.okul?" · "+esc(s.okul):""}${acc?" · @"+esc(acc.u):" · hesap yok"}</div></div>`, `<button class="iconbtn" data-act="sheet" data-v="ogrenci" data-id="${S.cur}" aria-label="Öğrenciyi düzenle">${icon("edit")}</button>`, `<button class="iconbtn" data-act="go" data-v="ozet" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page wide"><div class="tabs">${tabs.map(([k,n])=>`<button data-act="dtab" data-v="${k}" aria-pressed="${S.dtab===k}">${n}</button>`).join("")}</div>${body()}</div>`;
}
function cSummary(s){
  const m = coachMetrics(s), la = exams(s,"AYT").pop();
  const weak = [];
  [...CURX().TYT.map(x=>["TYT",x]), ...aytSubjects(s,false).map(x=>["AYT",x])].forEach(([ex,sub])=>sub.t.forEach(n=>{const y=(s.topics[tkey(sub.k,n)]||{}).y||0; if(y>0) weak.push({ex,sub:sub.n,n,y});}));
  weak.sort((a,b)=>b.y-a.y);
  const lt = exams(s,"TYT").pop();
  const stage = (t,key,o,editable) => `<div class="stg ${key==="cur"?"cur":""}"><div class="t">${t}</div>${editable?`
    <label>Tarih<input type="date" id="${key}-tarih" data-f="${key}.tarih" value="${esc(o.tarih||"")}"></label>
    <label>TYT<input type="text" inputmode="decimal" id="${key}-tyt" data-f="${key}.tyt" value="${o.tyt??""}" placeholder="${o.tytYok?"girmedi":"net"}"></label>
    <label>AYT<input type="text" inputmode="decimal" id="${key}-ayt" data-f="${key}.ayt" value="${o.ayt??""}" placeholder="${o.aytYok?"girmedi":"net"}"></label>`
    :`<div class="small muted">${o.tarih?trDate(o.tarih):"Deneme yok"}</div><div>TYT <span class="v num">${fmt(o.tyt)}</span></div><div>AYT <span class="v num">${fmt(o.ayt)}</span></div>`}</div>`;
  const curD = [lt?.tarih, la?.tarih].filter(Boolean).sort().pop();
  return `<div class="card" style="background:var(--acs);border-color:transparent"><div class="sech"><h3>${icon("eye","sm")} Koç özeti</h3><span class="pill ac">Sadece sen görürsün</span></div>
      <div class="pills" style="margin-top:10px">${(g=>g.list.length?`<span class="pill ac">Hedef konular ${g.done}/${g.list.length}</span>`:"")(weekGoals(s,curStart(s)))}${m.flags.length? m.flags.map(f=>`<span class="pill ${f[0]}">${esc(f[1])}</span>`).join("") : `<span class="pill good">Her şey yolunda görünüyor</span>`}</div></div>
    <div class="kpis">
      ${tile("t-g","target",m.w.pct==null?"—":"%"+Math.round(m.w.pct*100),`Bu hafta uyum · ${m.w.done}/${m.w.all}`)}
      ${tile("t-a","clock",fmtMin(m.w.min),"Bu hafta çalışma")}
      ${tile("t-w","trend",fmt(m.lt),m.dlt!=null?`Son TYT · ${m.dlt>=0?"+":""}${fmt(m.dlt)}`:"Son TYT")}
      ${tile("t-r","flame",m.streak+" gün",m.idle==null?"Henüz hareket yok":m.idle===0?"Bugün aktif":`Son hareket ${m.idle} gün önce`)}
    </div>
    <div class="card"><h3>Net yolculuğu</h3><div class="stage3" style="margin-top:10px">${stage("Başlangıç","baslangic",s.baslangic,true)}${stage("Güncel","cur",{tarih:curD,tyt:lt?tytTotal(lt):null,ayt:la?aytTotal(la):null},false)}${stage("Hedef","hedef",s.hedef,true)}</div></div>
    <div class="card"><h3>En çok yanlış yapılan konular</h3>${weak.length?`<div style="margin-top:4px">${weak.slice(0,6).map(x=>`<div class="row"><div style="min-width:0"><div class="rt">${esc(x.n)}</div><div class="rs">${x.ex} ${esc(x.sub)}</div></div><span class="rx num" style="color:var(--bad);font-weight:800">${x.y}</span></div>`).join("")}</div>`:`<div class="empty">Çeteleye henüz giriş yok.</div>`}</div>
    <div class="card"><div class="sech"><h3>Öğrenciye not</h3>${s.koctanNot?.date?`<span class="faint small">Gönderildi ${ago(s.koctanNot.date)}</span>`:""}</div><p class="muted small" style="margin:4px 0 8px">Öğrencinin ana sayfasında “Koçundan not” olarak görünür.</p>
      <textarea id="kn" placeholder="Bugün özellikle problemlere yoğunlaş…">${esc(s.koctanNot?.text||"")}</textarea><div class="pills" style="margin-top:8px"><button class="btn sm pri" data-act="sendnote">Notu gönder</button>${s.koctanNot?.text?`<button class="btn sm danger" data-act="clearnote">Notu kaldır</button>`:""}</div></div>
    <div class="card"><h3>Özel notların <span class="faint small" style="font-weight:600">· öğrenci görmez</span></h3><textarea id="coachnote" data-cnote="1" style="margin-top:8px" placeholder="Görüşme notları, veli görüşmesi, motivasyon durumu…">${esc(S.cnotes.get(S.cur)?.not||"")}</textarea></div>`;
}
function cProgram(){
  const ids = sortedStudents();
  if(!S.cur || !S.students.has(S.cur)) S.cur = ids[0]?.[0] || null;
  const s = st();
  return `${topbar(`<h1 class="ttl">Haftalık Program</h1>`)}
  <div class="page wide">
    ${ids.length?`<label class="f">Öğrenci<select id="pickStu" data-act="pick">${ids.map(([id,x])=>`<option value="${id}" ${id===S.cur?"selected":""}>${esc(x.name)} · ${esc(x.alan)}</option>`).join("")}</select></label>`:""}
    ${s? pProgram(s,true) : `<div class="card"><div class="empty">Program yazmak için önce bir öğrenci ekle.</div></div>`}
  </div>`;
}
function cBell(){
  const list = [...S.notifs.entries()].sort((a,b)=>a[1].at<b[1].at?1:-1);
  const unreadIds = list.filter(([,n])=>!n.read).map(([id])=>id);
  if(unreadIds.length) setTimeout(()=>{ unreadIds.forEach(id=>{ const n=S.notifs.get(id); if(n){ n.read=true; persistDoc("notifs",id,1500); } }); }, 0);
  const label = {kayit:"Yeni öğrenci kaydı", sifre:"Şifre yenilendi"};
  return `${topbar(`<h1 class="ttl">Bildirimler</h1>`)}
  <div class="page wide"><div class="card">${list.length? list.map(([id,n])=>`<button class="row" data-act="${n.sid&&S.students.has(n.sid)?"open":""}" data-id="${n.sid||""}"><span class="ri" style="${!n.read?"background:var(--acs);color:var(--ac)":""}">${icon(n.type==="kayit"?"user":"alert","sm")}</span><div style="min-width:0"><div class="rt">${label[n.type]||"Bildirim"}${!n.read?` <span class="pill ac">Yeni</span>`:""}</div><div class="rs">${esc(n.name||"")}${n.type==="kayit"?` · ${esc(n.alan||"")} · ${esc(n.sinif||"")}`:" yeni şifre oluşturdu"}</div></div><span class="rx small">${ago(n.at)}</span></button>`).join("") : `<div class="empty">Henüz bildirim yok. Bir öğrenci kaydolduğunda burada görünür.</div>`}</div>
  <p class="faint small" style="text-align:center">Gerçek uygulamada bu bildirimler telefonuna da gelecek.</p></div>`;
}
function cMore(){
  return `${topbar(`<h1 class="ttl">Daha Fazla</h1>`)}
  <div class="page wide"><div class="card">
    ${pushCard()}
    <button class="row" data-act="go" data-v="ayarlar"><span class="ri" style="background:var(--acs);color:var(--ac)">${icon("edit","sm")}</span><div><div class="rt">Ayarlar</div><div class="rs">Mesajlar, süreler, hızlı ekle, konu listeleri, şifre</div></div><span class="rx">${icon("chev","sm")}</span></button>
    <button class="row" data-act="sheet" data-v="tema"><span class="ri">${icon("palette","sm")}</span><div><div class="rt">Görünüm</div><div class="rs">Açık / koyu mod ve tema rengi</div></div><span class="rx">${icon("chev","sm")}</span></button>
    <button class="row" data-act="sheet" data-v="sinav"><span class="ri">${icon("cal","sm")}</span><div><div class="rt">YKS tarihi</div><div class="rs">${trDate(S.settings.examDate)}${S.settings.tahmini?" (tahmini)":""} · ${examDays()} gün</div></div><span class="rx">${icon("chev","sm")}</span></button>
    <button class="row" data-act="logout"><span class="ri">${icon("logout","sm")}</span><div><div class="rt">Çıkış yap</div></div></button>
  </div><p class="proto">Zekacademy Koç Paneli</p></div>`;
}

/* ---------- Ayarlar (koç) ---------- */
const clone = x => JSON.parse(JSON.stringify(x));
function cSettings(){
  const c = cfg(), cur = CURX(), ex = S.setEx || "TYT", sample = {name:"Ayşe Yılmaz"};
  const ta = (id, key, list, rows, ph) => `<textarea id="${id}" data-setlist="${key}" rows="${rows}" placeholder="${ph||""}">${esc(list.join("\n"))}</textarea>`;
  const sec = (title, desc, body, reset, open) => `<details class="card setsec" ${open?"open":""}><summary><span><b>${title}</b><span class="muted small">${desc}</span></span>${icon("chev","sm")}</summary><div class="setbody">${body}${reset?`<div class="pills"><button class="btn sm" data-act="sreset" data-v="${reset}">Varsayılana dön</button></div>`:""}</div></details>`;
  const morningPrev = c.sabah.filter(Boolean).length ? fillName(c.sabah.filter(Boolean)[dayNo(today()) % c.sabah.filter(Boolean).length], sample) : "—";
  return `${topbar(`<h1 class="ttl">Ayarlar</h1>`, "", `<button class="iconbtn" data-act="go" data-v="daha" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page wide" id="settingsPage">
    <p class="muted small" style="margin:0">Burada yaptığın değişiklikler otomatik kaydedilir ve tüm öğrencilerin uygulamasına anında yansır.</p>
    ${sec("Genel","Kurum adı, YKS tarihi, görünüm",`
      <div class="two"><label class="f">Kurum adı<input type="text" id="st-kurum" data-set="kurum" value="${esc(c.kurum)}"></label>
      <label class="f">YKS tarihi<input type="date" id="st-exam" data-set="examDate" value="${esc(S.settings.examDate)}"></label></div>
      <label class="inline"><input type="checkbox" id="st-tah" data-setb="tahmini" ${S.settings.tahmini?"checked":""}>Tarih henüz kesin değil (tahmini yazsın)</label>
      <div class="pills"><button class="btn sm" data-act="sheet" data-v="tema">${icon("palette","xs")} Açık / koyu mod ve tema rengi</button></div>`, "", true)}
    ${sec("Sabah motivasyon mesajları",`${c.sabah.filter(Boolean).length} mesaj · ${c.sabahAcik?c.sabahSaat+"’den itibaren":"kapalı"}`,`
      <div class="two"><label class="inline"><input type="checkbox" id="st-sa" data-setb="sabahAcik" ${c.sabahAcik?"checked":""}>Sabah mesajı gönder</label>
      <label class="f">Gönderim saati<input type="time" id="st-sas" data-set="sabahSaat" value="${esc(c.sabahSaat)}"></label></div>
      <div class="f">Mesajlar <span class="faint" style="font-weight:500">· her satır bir mesaj, {Ad} yazan yere öğrencinin adı gelir; sırayla döner</span>${ta("st-sabah","sabah",c.sabah,10)}</div>
      <div class="prev"><span class="faint small">Örnek: bugün Ayşe’ye giden mesaj</span><div>${esc(morningPrev)}</div></div>`, "sabah,sabahSaat,sabahAcik")}
    ${sec("Akşam hatırlatmaları",`${c.aksamAcik?c.aksamSaat+"’den itibaren, sadece eksiği olana":"kapalı"}`,`
      <div class="two"><label class="inline"><input type="checkbox" id="st-aa" data-setb="aksamAcik" ${c.aksamAcik?"checked":""}>Akşam hatırlatması gönder</label>
      <label class="f">Gönderim saati<input type="time" id="st-aas" data-set="aksamSaat" value="${esc(c.aksamSaat)}"></label></div>
      <div class="f">Sadece çalışma süresi girilmemişse${ta("st-ak1","aksam.sure",c.aksam.sure,3)}</div>
      <div class="f">Sadece görevler işaretlenmemişse${ta("st-ak2","aksam.gorev",c.aksam.gorev,3)}</div>
      <div class="f">İkisi de eksikse${ta("st-ak3","aksam.ikisi",c.aksam.ikisi,6)}</div>
      <p class="faint small" style="margin:0">İkisini de tamamlayan öğrenciye akşam mesajı gitmez.</p>`, "aksam,aksamSaat,aksamAcik")}
    ${sec("Ortalama süreler","Süre yazmayan satırların günlük toplama katılması",`
      <p class="muted small" style="margin:0">Satırda bu kelimelerin hepsi geçiyorsa süre otomatik hesaplanır. Kısaltma yazabilirsin: “mat” hem Mat hem Matematik’i tutar. Daha çok kelimeli kural önce uygulanır, “x2” süreyi ikiyle çarpar.</p>
      <div class="sgrid"><span class="gh">Satırda geçen kelimeler</span><span class="gh">Süre (dk)</span><span></span>
      ${c.sureler.map((r,i)=>`<input type="text" id="sr-k-${i}" data-sure="${i}" data-sf="k" value="${esc(r.k)}" placeholder="ör. geo branş"><input type="number" min="0" step="5" id="sr-d-${i}" data-sure="${i}" data-sf="dk" value="${r.dk??""}"><button class="mini" data-act="sdel" data-i="${i}" aria-label="Kuralı sil">${icon("trash","xs")}</button>`).join("")}</div>
      <div class="pills"><button class="btn sm" data-act="sadd">${icon("plus","xs")} Kural ekle</button></div>
      <label class="f">Dene: bir satır yaz<input type="text" id="sr-test" data-act="stest" placeholder="ör. AYT Fen Branş x2"></label><div class="small" id="sr-out" style="font-weight:700"></div>`, "sureler")}
    ${sec("Hızlı ekle listesi",`${c.quick.length} satır`,`<div class="f">Program yazarken “+ Hızlı ekle” menüsünde çıkan satırlar <span class="faint" style="font-weight:500">· her satır bir seçenek</span>${ta("st-quick","quick",c.quick,8)}</div>`, "quick")}
    ${sec("Haftalık hedef dersleri",`${c.hedefDers.length} ders`,`<div class="f">“Bitirilecek konu / Takip edilen kitaplar” tablosundaki dersler <span class="faint" style="font-weight:500">· her satır bir ders</span>${ta("st-hd","hedefDers",c.hedefDers,6)}</div>`, "hedefDers")}
    ${sec("Konu listeleri",`TYT ${cur.TYT.length} ders · AYT ${cur.AYT.length} ders`,`
      <p class="muted small" style="margin:0">Konu eklemek ve sıralamak güvenlidir. Bir konunun <b>adını değiştirirsen</b> o konuya daha önce girilmiş tekrar, soru bankası ve yanlış bilgileri görünmez olur.</p>
      <div class="seg"><button data-act="setex" data-v="TYT" aria-pressed="${ex==="TYT"}">TYT</button><button data-act="setex" data-v="AYT" aria-pressed="${ex==="AYT"}">AYT</button></div>
      ${cur[ex].map((sub,i)=>`<details class="subj"><summary><span><span class="sn">${esc(sub.n)}</span><span class="sg">${sub.t.length} konu</span></span><span></span><span class="pct">${icon("chev","xs")}</span></summary>
        <div class="trow">
          <div class="two"><label class="f">Ders adı<input type="text" id="cu-n-${ex}-${i}" data-cur="${ex}|${i}|n" value="${esc(sub.n)}"></label><label class="f">Etiket<input type="text" id="cu-g-${ex}-${i}" data-cur="${ex}|${i}|g" value="${esc(sub.g||"")}"></label></div>
          ${ex==="AYT"?`<div class="f">Hangi alanlarda görünsün<div class="chs">${ALANLAR.map(a=>`<label><input type="checkbox" id="cu-a-${i}-${a}" data-cura="${i}|${a}" ${(sub.a||[]).includes(a)?"checked":""}><span>${a}</span></label>`).join("")}</div></div>`:""}
          <div class="f">Konular <span class="faint" style="font-weight:500">· her satır bir konu</span><textarea id="cu-t-${ex}-${i}" data-curt="${ex}|${i}" rows="${Math.min(14,sub.t.length+1)}">${esc(sub.t.join("\n"))}</textarea></div>
          <div class="pills"><button class="btn sm danger" data-act="cdel" data-v="${ex}|${i}">${icon("trash","xs")} Bu dersi sil</button></div></div></details>`).join("")}
      <div class="pills"><button class="btn sm" data-act="cadd" data-v="${ex}">${icon("plus","xs")} ${ex} dersi ekle</button></div>`, "cur")}
    ${sec("Veri içe aktar","Drive’dan dönüştürülmüş öğrenci dosyası (.json)",`
      <p class="muted small" style="margin:0">Claude’un hazırladığı içe aktarma dosyasını seç. Her öğrenci için hesap açılır (ilk şifre dosyada yazan, genelde 123456) ve tüm verisi aktarılır. Kullanıcı adı zaten varsa o öğrenci atlanır.</p>
      <label class="f">Dosya<input type="file" id="imp-file" accept=".json,application/json"></label>
      <div class="pills"><button class="btn sm pri" data-act="import">Aktarmayı başlat</button></div>
      <div class="small" id="imp-out" style="white-space:pre-wrap;font-weight:600">${esc(S.impLog||"")}</div>`, "")}
    ${sec("Koç şifresi","Koç girişinde kullandığın şifre",`
      <div class="three"><label class="f">Mevcut şifre<input type="password" id="pw-0" autocomplete="current-password"></label><label class="f">Yeni şifre<input type="password" id="pw-1" autocomplete="new-password"></label><label class="f">Yeni şifre tekrar<input type="password" id="pw-2" autocomplete="new-password"></label></div>
      <div class="err" id="pwerr"></div><div class="pills"><button class="btn sm pri" data-act="pwd">Şifreyi değiştir</button></div>`, "")}
  </div>`;
}
function setPath(path, val){ const ks = path.split("."); let o = S.settings; for(let i=0;i<ks.length-1;i++){ o[ks[i]] = o[ks[i]] ? o[ks[i]] : clone(cfg()[ks[i]]); o = o[ks[i]]; } o[ks[ks.length-1]] = val; }
function onSetting(t, isChange){
  if(t.dataset.set!=null){ S.settings[t.dataset.set] = t.value; saveSettings(600); if(t.dataset.set==="kurum"||t.dataset.set==="examDate") renderSideOnly(); return true; }
  if(t.dataset.setb!=null && isChange){ S.settings[t.dataset.setb] = t.checked; saveSettings(); return true; }
  if(t.dataset.setlist!=null){ setPath(t.dataset.setlist, t.value.split("\n").map(x=>x.trim()).filter(Boolean)); saveSettings(800); return true; }
  if(t.dataset.sure!=null){ if(!S.settings.sureler) S.settings.sureler = clone(cfg().sureler); const r = S.settings.sureler[+t.dataset.sure]; if(r){ r[t.dataset.sf] = t.dataset.sf==="dk" ? num(t.value) : t.value; saveSettings(700); } return true; }
  if(t.dataset.act==="stest"){ const h = parseHours(t.value), r = ruleFor(t.value); $("#sr-out").textContent = t.value ? (h ? `${fmtMin(h*60)}${r && !/(saat|sa|dk|dakika)\b/i.test(t.value) ? ` · “${r.k}” kuralı` : " · satırdaki süre"}` : "Bu satır için kural yok; süre hesaba katılmaz.") : ""; return true; }
  const ensureCur = () => { if(!S.settings.cur) S.settings.cur = clone(CUR); return S.settings.cur; };
  if(t.dataset.cur!=null){ const [ex,i,f] = t.dataset.cur.split("|"); ensureCur()[ex][+i][f] = t.value; saveSettings(800); return true; }
  if(t.dataset.curt!=null){ const [ex,i] = t.dataset.curt.split("|"); ensureCur()[ex][+i].t = [...new Set(t.value.split("\n").map(x=>x.trim()).filter(Boolean))]; saveSettings(800); return true; }
  if(t.dataset.cura!=null && isChange){ const [i,a] = t.dataset.cura.split("|"); const sub = ensureCur().AYT[+i]; sub.a = sub.a||[]; sub.a = t.checked ? [...new Set([...sub.a,a])] : sub.a.filter(x=>x!==a); saveSettings(); return true; }
  return false;
}
function renderSideOnly(){}
async function runImport(b){
  const f = $("#imp-file")?.files?.[0], log = t => { S.impLog += t + "\n"; const o = $("#imp-out"); if(o) o.textContent = S.impLog; };
  S.impLog = "";
  if(!f) return log("Önce dosyayı seç.");
  let data; try{ data = JSON.parse(await f.text()); }catch(e){ return log("Dosya okunamadı: geçerli bir içe aktarma dosyası değil."); }
  const list = data.ogrenciler || []; if(!list.length) return log("Dosyada öğrenci yok.");
  b.disabled = true; let ok = 0, skip = 0;
  for(const o of list){
    const u = normU(o.kullanici), name = o.kayit?.name || u;
    if(!/^[a-z0-9._-]{3,20}$/.test(u)){ log(`✗ ${name}: kullanıcı adı geçersiz (${o.kullanici})`); skip++; continue; }
    if([...S.students.values()].some(x=>x.kullanici===u)){ log(`– ${name}: @${u} zaten var, atlandı`); skip++; continue; }
    try{
      const id = await createStudentAccount(u, o.sifre || "123456");
      const rec = {...o.kayit, kullanici:u, ilkSifre:true}; delete rec.not; delete rec.ornek; delete rec.aktarim;
      S.students.set(id, rec); await writeDoc("students", id, rec);
      if(o.kocNotu){ S.cnotes.set(id, {not:o.kocNotu}); await writeDoc("coachNotes", id, S.cnotes.get(id)); }
      log(`✓ ${name} → @${u}`); ok++;
    }catch(e){ log(`✗ ${name}: ${authMsg(e)}`); skip++; }
  }
  log(`\nBitti: ${ok} öğrenci aktarıldı${skip?`, ${skip} atlandı`:""}.`); b.disabled = false; keepSettingsOpen();
}
function onSettingClick(a, b){
  const v = b.dataset.v;
  if(a==="setex"){ S.setEx = v; render(); return true; }
  if(a==="sadd"){ if(!S.settings.sureler) S.settings.sureler = clone(cfg().sureler); S.settings.sureler.push({k:"",dk:30}); saveSettings(); keepSettingsOpen(); setTimeout(()=>{ const x=document.getElementById("sr-k-"+(S.settings.sureler.length-1)); if(x) x.focus(); },0); return true; }
  if(a==="sdel"){ if(!S.settings.sureler) S.settings.sureler = clone(cfg().sureler); S.settings.sureler.splice(+b.dataset.i,1); saveSettings(); keepSettingsOpen(); return true; }
  if(a==="cadd"){ if(!S.settings.cur) S.settings.cur = clone(CUR); const L = S.settings.cur[v]; L.push({k:(v==="TYT"?"x":"ax")+uid().slice(0,5), n:"Yeni ders", g:v, t:[], ...(v==="AYT"?{a:["SAY","EA","SÖZ"]}:{})}); saveSettings(); keepSettingsOpen(L.length-1); return true; }
  if(a==="cdel"){ if(!b.dataset.armed){ b.dataset.armed="1"; b.textContent="Silmek için tekrar dokun"; return true; } const [ex,i] = v.split("|"); if(!S.settings.cur) S.settings.cur = clone(CUR); S.settings.cur[ex].splice(+i,1); saveSettings(); keepSettingsOpen(); toast("Ders silindi"); return true; }
  if(a==="sreset"){ if(!b.dataset.armed){ b.dataset.armed="1"; b.textContent="Emin misin? Tekrar dokun"; setTimeout(()=>{ if(b.isConnected){ delete b.dataset.armed; b.textContent="Varsayılana dön"; } },3000); return true; } v.split(",").forEach(k=>delete S.settings[k]); saveSettings(); keepSettingsOpen(); toast("Varsayılana döndürüldü"); return true; }
  if(a==="import"){ runImport(b); return true; }
  if(a==="pwd"){ const p0=$("#pw-0").value, p1=$("#pw-1").value, p2=$("#pw-2").value, err=t=>{ $("#pwerr").textContent=t; };
    if(p1.length<6) return err("Yeni şifre en az 6 karakter olmalı."), true;
    if(p1!==p2) return err("Yeni şifreler aynı değil."), true;
    b.disabled = true;
    reauthenticateWithCredential(auth.currentUser, EmailAuthProvider.credential(COACH_EMAIL, p0.trim()))
      .then(()=>updatePassword(auth.currentUser, p1.trim()))
      .then(()=>{ ["pw-0","pw-1","pw-2"].forEach(id=>$("#"+id).value=""); err(""); toast("Koç şifresi değiştirildi"); })
      .catch(e=>err(e && (e.code==="auth/invalid-credential"||e.code==="auth/wrong-password") ? "Mevcut şifre hatalı." : authMsg(e)))
      .finally(()=>{ b.disabled = false; });
    return true; }
  return false;
}
function keepSettingsOpen(openSubj){
  const open = [...document.querySelectorAll("details.setsec")].map(d=>d.open), sub = [...document.querySelectorAll("details.setsec details.subj")].map(d=>d.open);
  render();
  document.querySelectorAll("details.setsec").forEach((d,i)=>{ if(open[i]) d.open=true; });
  const ss = document.querySelectorAll("details.setsec details.subj"); ss.forEach((d,i)=>{ if(sub[i]) d.open=true; }); if(openSubj!=null && ss[openSubj]) ss[openSubj].open = true;
}

/* ---------- Uygulamayı yükle (giriş ekranı) ---------- */
let installEvt = null;
const isAndroid = () => /android/i.test(navigator.userAgent);
window.addEventListener("beforeinstallprompt", e => { e.preventDefault(); installEvt = e; refreshInstall(); });
window.addEventListener("appinstalled", () => { installEvt = null; refreshInstall(); toast("Uygulama yüklendi! Artık ana ekrandaki Zekacademy simgesinden açabilirsin."); });
function installCard(){
  if(isStandalone()) return "";
  const head = t => `<div class="inst-h"><span class="inst-i">${icon("phone","sm")}</span><div><b>Uygulamayı telefonuna yükle</b><span>${t}</span></div></div>`;
  if(installEvt) return `<div class="instcard">${head("Tek dokunuşla kur; bildirimler gelsin, tam ekran açılsın.")}<button type="button" class="btn pri full" data-act="install">Uygulamayı yükle</button></div>`;
  if(isIOS()) return `<div class="instcard">${head("Bildirimlerin gelmesi için iPhone'da bu adım şart.")}<ol class="inst-s"><li><b>Safari</b> ile aç (başka tarayıcıdaysan adresi Safari'ye yapıştır).</li><li>Alttaki <b>Paylaş</b> düğmesine dokun (yukarı oklu kare).</li><li><b>Ana Ekrana Ekle</b> → <b>Ekle</b>.</li><li>Uygulamayı ana ekrandaki <b>Zekacademy</b> simgesinden aç.</li></ol></div>`;
  if(isAndroid()) return `<div class="instcard">${head("Bildirimler gelsin, tam ekran açılsın.")}<ol class="inst-s"><li><b>Chrome</b>'da sağ üstteki <b>⋮</b> menüsüne dokun.</li><li><b>Uygulamayı yükle</b> (ya da <b>Ana ekrana ekle</b>) seçeneğine dokun.</li><li>Uygulamayı ana ekrandaki <b>Zekacademy</b> simgesinden aç.</li></ol></div>`;
  return "";
}
function refreshInstall(){ const el = document.getElementById("instWrap"); if(el) el.innerHTML = installCard(); }
async function doInstall(){
  if(!installEvt) return refreshInstall();
  const e = installEvt; installEvt = null;
  try{ await e.prompt(); await e.userChoice; }catch(_){}
  refreshInstall();
}

/* ---------- Giriş ---------- */
function renderAuth(){
  const r = S.authRole, mode = r==="admin" ? "admin" : S.auth, rd = true;
  const roleSeg = `<div class="seg"><button type="button" data-act="arole" data-v="student" aria-pressed="${r==="student"}">Öğrenci</button><button type="button" data-act="arole" data-v="admin" aria-pressed="${r==="admin"}">Koç girişi</button></div>`;
  const keep = id => `<label class="inline"><input type="checkbox" id="${id}" name="keep" checked>Beni hatırla</label>`;
  const submit = l => `<button class="btn pri full" style="padding:14px" data-label="${l}" ${rd?"":"disabled"}>${rd?l:"Yükleniyor…"}</button>`;
  let f = "";
  if(mode==="signup") f = `<form class="apanel" id="fSignup" novalidate>
    <div class="logo"><span class="lm">Z</span>zekacademy</div>${roleSeg}<div id="instWrap">${installCard()}</div>
    <div class="ahero"><b>YKS yolculuğun tek uygulamada</b><span>Koçunun hazırladığı programı takip et, çalışmanı ve denemelerini kaydet.</span></div>
    <h2>Kayıt ol</h2><p class="sub">Bilgilerini bir kez gir, sonrasında panelin doğrudan açılsın.</p>
    <label class="f">Ad soyad<input type="text" id="r-name" name="name" autocomplete="name"></label>
    <div class="f">Sınıf<div class="chs">${SINIFLAR.map((x,i)=>`<label><input type="radio" name="sinif" id="r-s${i}" value="${x}" ${i===3?"checked":""}><span>${x.replace(". sınıf","")}</span></label>`).join("")}</div></div>
    <label class="f" id="okulWrap">Okul<input type="text" id="r-okul" name="okul" placeholder="Okulunun adı"></label>
    <div class="f">Alan<div class="chs">${ALANLAR.map((x,i)=>`<label><input type="radio" name="alan" id="r-a${i}" value="${x}" ${i===0?"checked":""}><span>${x}</span></label>`).join("")}</div></div>
    <div class="two">
      <div class="f"><label for="r-tyt">İlk TYT netin</label><input type="text" inputmode="decimal" id="r-tyt" name="tyt" placeholder="ör. 62,5"><label class="inline"><input type="checkbox" id="r-tytYok" name="tytYok" data-net="r-tyt">Girmedim</label></div>
      <div class="f"><label for="r-ayt">İlk AYT netin</label><input type="text" inputmode="decimal" id="r-ayt" name="ayt" placeholder="ör. 28"><label class="inline"><input type="checkbox" id="r-aytYok" name="aytYok" data-net="r-ayt">Girmedim</label></div>
    </div>
    <label class="f">Kullanıcı adı<input type="text" id="r-u" name="u" autocomplete="username" autocapitalize="none" autocorrect="off" spellcheck="false" placeholder="küçük harf, rakam, . _ -"></label>
    <div class="two"><label class="f">Şifre<input type="password" id="r-p" name="p" autocomplete="new-password" placeholder="en az 6 karakter"></label><label class="f">Şifre tekrar<input type="password" id="r-p2" name="p2" autocomplete="new-password"></label></div>
    ${keep("r-keep")}<div class="err" id="aerr"></div>${submit("Kaydol ve panele geç")}
    <p class="swap">Zaten hesabın var mı? <button type="button" class="link" data-act="amode" data-v="login">Giriş yap</button></p></form>`;
  else if(mode==="forgot") f = `<div class="apanel">
    <div class="logo"><span class="lm">Z</span>zekacademy</div>
    <h2>Şifreni mi unuttun?</h2>
    <p class="sub">Koçuna yaz, sana yeni bir giriş versin. Programın, denemelerin ve tüm bilgilerin olduğu gibi kalır.</p>
    <div class="card"><b>Koçuna ne yazmalısın?</b><p class="muted small" style="margin:6px 0 0">“Hocam şifremi unuttum, kullanıcı adım: …” yazman yeterli.</p></div>
    <p class="swap"><button type="button" class="link" data-act="amode" data-v="login">Girişe dön</button></p></div>`;
  else { const adm = mode==="admin"; f = `<form class="apanel" id="fLogin" novalidate>
    <div class="logo"><span class="lm">Z</span>zekacademy</div>${roleSeg}<div id="instWrap">${installCard()}</div>
    <h2>${adm?"Koç girişi":"Giriş yap"}</h2><p class="sub">${adm?"Tüm öğrencilerini görmek ve yönetmek için.":"Kayıt olurken oluşturduğun bilgilerle gir."}</p>
    <label class="f">Kullanıcı adı<input type="text" id="l-u" name="u" autocomplete="username" autocapitalize="none" autocorrect="off" spellcheck="false"></label>
    <label class="f">Şifre<input type="password" id="l-p" name="p" autocomplete="current-password"></label>
    ${keep("l-keep")}<div class="err" id="aerr"></div>${submit("Giriş yap")}
    ${adm?"":`<p class="swap"><button type="button" class="link" data-act="amode" data-v="forgot">Şifremi unuttum</button></p><p class="swap">Hesabın yok mu? <button type="button" class="link" data-act="amode" data-v="signup">Kayıt ol</button></p>`}</form>`; }
  $("#root").innerHTML = `<div class="auth">${f}</div>`;
}
function authErr(t){ const e=$("#aerr"); if(e) e.textContent=t; }
async function doSignup(f){
  const fd = new FormData(f);
  const name = String(fd.get("name")).trim().replace(/\s+/g," "), sinif = fd.get("sinif"), alan = fd.get("alan"), okul = String(fd.get("okul")||"").trim();
  const tytYok = !!fd.get("tytYok"), aytYok = !!fd.get("aytYok");
  const tyt = tytYok ? null : num(fd.get("tyt")), ayt = aytYok ? null : num(fd.get("ayt"));
  const u = normU(fd.get("u")), p = String(fd.get("p")), p2 = String(fd.get("p2"));
  if(name.split(" ").length < 2) return authErr("Adını ve soyadını yaz.");
  if(sinif!=="Mezun" && !okul) return authErr("Okulunu yaz.");
  if(!tytYok && tyt==null) return authErr("İlk TYT netini yaz ya da “Girmedim”i işaretle.");
  if(tyt!=null && (tyt<0||tyt>120)) return authErr("TYT neti 0 ile 120 arasında olmalı.");
  if(!aytYok && ayt==null) return authErr("İlk AYT netini yaz ya da “Girmedim”i işaretle.");
  if(ayt!=null && (ayt<0||ayt>160)) return authErr("AYT neti 0 ile 160 arasında olmalı.");
  if(!/^[a-z0-9._-]{3,20}$/.test(u)) return authErr("Kullanıcı adı 3–20 karakter olmalı; harf, rakam, nokta, alt çizgi ve tire kullanabilirsin.");
  if(u===ADMIN_U) return authErr("Bu kullanıcı adı alınmış, başka bir tane dene.");
  if(p.length<6) return authErr("Şifre en az 6 karakter olmalı.");
  if(p!==p2) return authErr("Şifreler aynı değil.");
  busy(f, true);
  try{
    await setPersistence(auth, fd.get("keep") ? browserLocalPersistence : browserSessionPersistence);
    const cred = await createUserWithEmailAndPassword(auth, emailOf(u), p);
    const id = cred.user.uid;
    S.students.set(id, blank({name,sinif,alan,okul,tyt,ayt,tytYok,aytYok,kullanici:u}));
    await writeDoc("students", id, S.students.get(id));
    await setDoc(doc(fdb,"notifs",uid()), {type:"kayit", at:nowISO(), read:false, sid:id, name, alan, sinif});
    toast("Kaydın tamamlandı, hoş geldin!");
  }catch(e){ busy(f, false); authErr(authMsg(e)); }
}
async function doLogin(f){
  const fd = new FormData(f), u = normU(fd.get("u")), p = String(fd.get("p")), keep = !!fd.get("keep");
  if(!u || !p) return authErr("Kullanıcı adı ve şifreni yaz.");
  if(S.authRole==="admin" && u!==ADMIN_U) return authErr("Kullanıcı adı veya şifre hatalı.");
  if(S.authRole!=="admin" && u===ADMIN_U) return authErr("Koç girişi için üstteki “Koç girişi” sekmesini kullan.");
  busy(f, true);
  try{
    await setPersistence(auth, keep ? browserLocalPersistence : browserSessionPersistence);
    await signInWithEmailAndPassword(auth, emailOf(u), S.authRole==="admin" ? p.trim() : p);
  }catch(e){ busy(f, false); authErr(authMsg(e)); }
}
function busy(f, on){ const b = f.querySelector(".btn.pri"); if(b){ b.disabled = on; b.textContent = on ? "Lütfen bekle…" : (b.dataset.label||b.textContent); } }
function renderFirstPassword(){
  const s = st();
  $("#root").innerHTML = `<div class="auth"><form class="apanel" id="fFirst" novalidate>
    <div class="logo"><span class="lm">Z</span>${esc(cfg().kurum)}</div>
    <h2>Hoş geldin, ${esc(firstName(s.name))}</h2>
    <p class="sub">Güvenliğin için koçunun verdiği ilk şifreyi kendi şifrenle değiştir. Sonraki girişlerinde bu şifreyi kullanacaksın.</p>
    <div class="faint small">Kullanıcı adın: <b style="color:var(--fg)">${esc(s.kullanici||"")}</b></div>
    <div class="two"><label class="f">Yeni şifre<input type="password" id="fp-1" name="p" autocomplete="new-password" placeholder="en az 6 karakter"></label><label class="f">Yeni şifre tekrar<input type="password" id="fp-2" name="p2" autocomplete="new-password"></label></div>
    <div class="err" id="aerr"></div><button class="btn pri full" style="padding:14px" data-label="Şifremi kaydet ve devam et">Şifremi kaydet ve devam et</button>
    <p class="swap"><button type="button" class="link" data-act="logout">Çıkış yap</button></p></form></div>`;
}
async function doFirstPassword(f){
  const fd = new FormData(f), p = String(fd.get("p")), p2 = String(fd.get("p2"));
  if(p.length<6) return authErr("Şifre en az 6 karakter olmalı.");
  if(p==="123456") return authErr("Koçunun verdiği ilk şifreden farklı bir şifre seç.");
  if(p!==p2) return authErr("Şifreler aynı değil.");
  busy(f, true);
  try{ await updatePassword(auth.currentUser, p); const s = st(); s.ilkSifre = false; await writeDoc("students", S.me, s); render(); toast("Şifren kaydedildi"); }
  catch(e){ busy(f, false); authErr(authMsg(e)); }
}
function logout(){ closeSheet(); S.authRole="student"; S.auth="login"; signOut(auth); window.scrollTo(0,0); }

/* ---------- Sayfa altı pencereleri ---------- */
function sheet(html, onSubmit){
  $("#layer").innerHTML = `<div class="ov"><form class="sheet" id="sheetForm" novalidate>${html}</form></div>`;
  const ov = $("#layer .ov"), form = ov.querySelector("form");
  ov.addEventListener("click", e=>{ if(e.target===ov || e.target.closest("[data-close]")) closeSheet(); });
  form.addEventListener("submit", e=>{ e.preventDefault(); e.stopPropagation(); onSubmit && onSubmit(new FormData(form), form); });
  const first = form.querySelector("input[type=text],input[type=number],select"); if(first && window.innerWidth>700) first.focus();
}
function closeSheet(){ $("#layer").innerHTML=""; }
document.addEventListener("keydown", e=>{ if(e.key==="Escape" && $("#layer").innerHTML) closeSheet(); });
const sheetErr = t => { const e=$("#serr"); if(e) e.textContent=t; };

function openSheet(kind, el){
  const s = st();
  if(kind==="tema") return sheet(`<h3>Görünüm</h3>
    <div class="f">Mod<div class="seg">${[["system","Otomatik"],["light","Açık"],["dark","Koyu"]].map(([k,l])=>`<button type="button" data-act="mode" data-v="${k}" aria-pressed="${THEME.mode===k}">${l}</button>`).join("")}</div></div>
    <div class="f">Tema rengi<div class="swatch">${[["blue","#2563EB","Mavi"],["green","#0E9F55","Yeşil"],["red","#DC2F3C","Kırmızı"]].map(([k,c,l])=>`<button type="button" class="sw" style="background:${c}" data-act="accent" data-v="${k}" aria-pressed="${THEME.accent===k}" aria-label="${l}">${THEME.accent===k?icon("check","sm"):""}</button>`).join("")}</div></div>
    <div class="acts"><button type="button" class="btn" data-close>Kapat</button></div>`);
  if(kind==="sinav") return sheet(`<h3>YKS tarihi</h3>
    <label class="f">Sınav tarihi<input type="date" name="d" id="m-exam" value="${S.settings.examDate}"></label>
    <label class="inline"><input type="checkbox" name="t" id="m-tah" ${S.settings.tahmini?"checked":""}>ÖSYM henüz açıklamadı (tahmini)</label>
    <div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ Object.assign(S.settings,{examDate:fd.get("d")||S.settings.examDate, tahmini:!!fd.get("t")}); saveSettings(); closeSheet(); render(); });
  if(kind==="sure"){ const d = el.dataset.date, cur = Math.round((s.gunluk||{})[d]||0);
    return sheet(`<h3>Çalışma süresi · ${GUN[dIdx(d)]}, ${shortDate(d)}</h3>
      <p class="muted small" style="margin:-6px 0 0">Bu günün toplam çalışma süresini yaz. Kronometreyle kaydedilen süre de buna dahildir.</p>
      <div class="two"><label class="f">Saat<input type="number" min="0" max="16" name="h" id="su-h" value="${Math.floor(cur/60)}"></label><label class="f">Dakika<input type="number" min="0" max="59" step="5" name="m" id="su-m" value="${cur%60}"></label></div>
      <div class="pills">${[30,60,90,120].map(x=>`<button type="button" class="btn sm" data-act="addq" data-v="${x}">+${fmtMin(x)}</button>`).join("")}</div>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ const v = (num(fd.get("h"))||0)*60 + (num(fd.get("m"))||0); if(v<0||v>16*60) return sheetErr("0 ile 16 saat arasında bir süre gir."); s.gunluk = s.gunluk||{}; if(v) s.gunluk[d]=v; else delete s.gunluk[d]; save(); closeSheet(); render(); toast("Çalışma süresi kaydedildi"); }); }
  if(kind==="deneme"){ const tur = S.ex, F = tur==="TYT"?TYTF:AYTF;
    return sheet(`<h3>${tur} denemesi ekle</h3>
      <div class="seg">${["TYT","AYT"].map(t=>`<button type="button" data-act="dtur" data-v="${t}" aria-pressed="${tur===t}">${t}</button>`).join("")}</div>
      <div class="two"><label class="f">Yayın<input type="text" name="yayin" id="dn-yayin" placeholder="ör. 345, Limit"></label><label class="f">Tarih<input type="date" name="tarih" id="dn-tarih" value="${today()}"></label></div>
      <div class="dyrow dyhead"><span>Ders</span><span style="text-align:center">Doğru</span><span style="text-align:center">Yanlış</span><span style="text-align:right">Net</span></div>
      ${F.map(([k,n,mx])=>`<div class="dyrow" data-mx="${mx}"><span class="nm">${n}<small>${mx} soru</small></span><input type="number" inputmode="numeric" min="0" max="${mx}" name="${k}_d" id="dn-${k}-d" data-dy="${k}" aria-label="${n} doğru"><input type="number" inputmode="numeric" min="0" max="${mx}" name="${k}_y" id="dn-${k}-y" data-dy="${k}" aria-label="${n} yanlış"><span class="net num" id="net-${k}">—</span></div>`).join("")}
      <div class="sech" style="border-top:1px solid var(--line);padding-top:12px"><b>Toplam net</b><b class="num" style="font-size:22px;color:var(--ac)" id="net-tot">0</b></div>
      <p class="faint small" style="margin:0">Net = Doğru − Yanlış ÷ 4. Boş bırakılan sorular hesaba girmez. Denemeden sonra yanlış konularını Çetele’de işaretlemeyi unutma.</p>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ const d = {id:uid(), tur, yayin:String(fd.get("yayin")).trim(), tarih:fd.get("tarih")||today()}; let any=false;
      for(const [k,n,mx] of F){ const D=num(fd.get(k+"_d"))||0, Y=num(fd.get(k+"_y"))||0; if(D<0||Y<0||D+Y>mx) return sheetErr(`${n}: doğru + yanlış en fazla ${mx} olabilir.`); if(D||Y) any=true; d[k]={d:D,y:Y}; }
      if(!any) return sheetErr("En az bir derste doğru veya yanlış sayısı gir.");
      s.denemeler = s.denemeler||[]; s.denemeler.push(d); save(); closeSheet(); render(); toast(`${tur} denemesi kaydedildi · ${fmt(totalOf(d))} net`); }); }
  if(kind==="gorusme"){ const t = today();
    return sheet(`<h3>Yeni görüşme</h3><p class="muted small" style="margin:-6px 0 0">Seçtiğin gün bu öğrencinin yeni hafta başı olur; program o günden itibaren 7 gün sürer. Hafta ortasındaki küçük değişiklikler için buna gerek yok, programın üstünde düzeltmen yeterli.</p>
      <label class="f">Görüşme / hafta başı günü<input type="date" name="d" id="gr-d" value="${t}"></label>
      <label class="inline"><input type="checkbox" name="kopya" id="gr-k" checked>Geçen haftanın programını aktar</label>
      <p class="faint small" style="margin:-4px 0 0">Satırlar aynı güne gelir (Çarşamba → Çarşamba). Günlük çalışma süreleri ve hedef konular da aktarılır; işaretler sıfırlanır, bugün işaretlenenler korunur.</p>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Yeni haftayı başlat</button></div>`,
    fd=>{ const d = fd.get("d"); if(!d) return sheetErr("Bir gün seç.");
      if((s.donem||[]).includes(d)) return sheetErr("Bu gün zaten bir hafta başı.");
      const oldStart = pStart(s,d), oldDays = [...Array(7)].map((_,i)=>addDays(oldStart,i)), oldW = (s.weeks||{})[oldStart]||{}, oldP = plan(s,oldStart);
      s.donem = [...(s.donem||[]), d].sort();
      const np = ensurePlan(s,d); let c = 0;
      if(fd.get("kopya")){
        pDays(s,d).forEach((x,i)=>{ const j = oldDays.findIndex(o=>dIdx(o)===dIdx(x)); if(j<0) return;
          const srcDate = oldDays[j], src = oldW[j]||[];
          const keepDone = srcDate===x;
          setDayTasks(s,x, src.map(t=>({id: keepDone? t.id : uid(), t:taskText(t), done: keepDone && !!t.done, doneAt: keepDone ? (t.doneAt||null) : null})));
          c += src.length;
          const sv = (oldP.saat||{})[j]; if(sv!=null && sv!=="") np.saat[i] = sv; });
        Object.entries(oldP.hedef||{}).forEach(([k,v])=>{ if(v && v.konu) np.hedef[k] = {konu:v.konu, done:false}; });
      }
      s.programYeni = nowISO();
      S.week = d; S.day = d; save(); closeSheet(); render(); toast(fd.get("kopya") ? `Yeni hafta ${GUN[dIdx(d)]} başladı · ${c} görev aktarıldı` : `Yeni hafta ${GUN[dIdx(d)]} başladı`); }); }
  if(kind==="copyday"){ const d = el.dataset.date, w = pStart(s,d);
    return sheet(`<h3>${GUN[dIdx(d)]} planını kopyala</h3><p class="muted small" style="margin:-6px 0 0">Seçtiğin günlerin planı bu günün planıyla değiştirilir. Çalışma süresi hedefi de kopyalanır.</p>
      <div class="chs">${pDays(s,w).map((x,i)=>x===d?"":`<label><input type="checkbox" name="days" id="cp-${i}" value="${x}"><span>${GUNK[dIdx(x)]} ${dNum(x)}</span></label>`).join("")}</div>
      <div class="pills"><button type="button" class="btn sm" data-act="cpsel" data-v="hafta">Hafta içi</button><button type="button" class="btn sm" data-act="cpsel" data-v="hepsi">Tümü</button></div>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kopyala</button></div>`,
    fd=>{ const days = fd.getAll("days"); if(!days.length) return sheetErr("En az bir gün seç.");
      const src = dayTasks(s,d), p = ensurePlan(s,w), sv = p.saat[pIdx(s,d)];
      days.forEach(x=>{ setDayTasks(s,x, src.map(t=>({id:uid(), t:taskText(t), done:false, doneAt:null}))); if(sv!=null && sv!=="") p.saat[pIdx(s,x)] = sv; else delete p.saat[pIdx(s,x)]; });
      save(); closeSheet(); render(); toast(`${days.length} güne kopyalandı`); }); }
  if(kind==="ogrenci"){ const id = el.dataset.id, x = id ? S.students.get(id) : null, acc = id ? accountOf(id) : null, sinif = x?.sinif || "12. sınıf";
    return sheet(`<h3>${x?"Öğrenciyi düzenle":"Yeni öğrenci"}</h3>
      <label class="f">Ad soyad<input type="text" name="name" id="m-name" value="${esc(x?.name||"")}"></label>
      <div class="two"><label class="f">Sınıf<select name="sinif" id="m-sinif">${SINIFLAR.map(a=>`<option ${sinif===a?"selected":""}>${a}</option>`).join("")}</select></label>
      <label class="f">Alan<select name="alan" id="m-alan">${ALANLAR.map(a=>`<option ${x?.alan===a?"selected":""}>${a}</option>`).join("")}</select></label></div>
      <label class="f" id="m-okulWrap" ${sinif==="Mezun"?"hidden":""}>Okul<input type="text" name="okul" id="m-okul" value="${esc(x?.okul||"")}"></label>
      ${acc?`<div class="card" style="box-shadow:none"><span class="muted small">Öğrenci hesabı: <b style="color:var(--fg)">@${esc(acc.u)}</b>${x.ilkSifre?" · henüz ilk şifresini değiştirmedi":""}. </span>
        <div class="two" style="margin-top:10px"><label class="f">Yeni şifre<input type="text" id="m-np" autocomplete="off" value="123456"></label><div class="f" style="justify-content:flex-end"><button type="button" class="btn" id="m-reset">Şifreyi sıfırla</button></div></div>
        <span class="faint small">Öğrenci bir sonraki girişinde bu şifreyle girer ve kendi şifresini belirler.</span><div class="err" id="m-rerr"></div></div>`
        :`<div class="card" style="box-shadow:none;display:flex;flex-direction:column;gap:10px"><span class="muted small">${x?"Bu öğrencinin hesabı yok. Hesap açmak için “Yeni öğrenci” ile ekleyip bu kayıtla birleştirebilirsin.":"Öğrenci bu bilgilerle kendi paneline girer. İlk girişte şifresini değiştirmesi istenir."}</span>
        ${x?"":`<div class="two"><label class="f">Kullanıcı adı<input type="text" name="u" id="m-u" autocapitalize="none" autocomplete="off" placeholder="ör. ahmetguner"></label><label class="f">İlk şifre<input type="text" name="p" id="m-p" autocomplete="off" value="123456"></label></div>`}</div>`}
      ${x?`<label class="f">Başka bir kayıtla birleştir<select name="merge" id="m-merge"><option value="">—</option>${sortedStudents().filter(([k])=>k!==id).map(([k,y])=>`<option value="${k}">${esc(y.name)} · ${esc(y.sinif)}${y.kullanici?" · @"+esc(y.kullanici):""}</option>`).join("")}</select><span class="faint small" style="font-weight:500">Seçtiğin eski kaydın tüm verisi bu kayda taşınır ve eski kayıt silinir.</span></label>`:""}
      <div class="err" id="serr"></div>
      <div class="acts">${x?`<button type="button" class="btn danger" id="m-del" style="margin-right:auto">Öğrenciyi sil</button>`:""}<button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri" data-label="${x?"Kaydet":"Ekle"}">${x?"Kaydet":"Ekle"}</button></div>`,
    async (fd, form)=>{ const name = String(fd.get("name")).trim(); if(!name) return sheetErr("Ad soyad gerekli.");
      const sn = fd.get("sinif"), okul = sn==="Mezun"?"":String(fd.get("okul")||"").trim();
      if(x){ Object.assign(x,{name,alan:fd.get("alan"),sinif:sn,okul});
        const mg = fd.get("merge");
        if(mg && S.students.has(mg)){ const o = S.students.get(mg);
          x.topics = {...o.topics, ...x.topics}; x.denemeler = [...(o.denemeler||[]), ...(x.denemeler||[])];
          const own = {...(x.gunluk||{})}; x.gunluk = {...(o.gunluk||{})}; Object.entries(own).forEach(([d,m])=>x.gunluk[d]=(x.gunluk[d]||0)+m);
          x.weeks = {...(o.weeks||{}), ...(x.weeks||{})}; x.plan = {...(o.plan||{}), ...(x.plan||{})}; x.kitaplar = {...(o.kitaplar||{}), ...(x.kitaplar||{})}; x.sbAd = {...(o.sbAd||{}), ...(x.sbAd||{})};
          x.donem = [...new Set([...(o.donem||[]), ...(x.donem||[])])].sort();
          x.baslangic = o.baslangic; x.hedef = o.hedef; x.koctanNot = x.koctanNot || o.koctanNot;
          const on = S.cnotes.get(mg)?.not, xn = S.cnotes.get(id)?.not; if(on || xn){ S.cnotes.set(id, {not:[on, xn].filter(Boolean).join("\n")}); persistDoc("coachNotes", id, 0); }
          S.students.delete(mg); persistDoc("students", mg, 0); S.cnotes.delete(mg); persistDoc("coachNotes", mg, 0);
          toast("Kayıtlar birleştirildi"); }
        persistDoc("students", id); closeSheet(); render(); return; }
      const u = normU(fd.get("u")), p = String(fd.get("p")||"");
      if(!u) return sheetErr("Kullanıcı adı gerekli.");
      if(!/^[a-z0-9._-]{3,20}$/.test(u) || u===ADMIN_U) return sheetErr("Kullanıcı adı 3–20 karakter; harf, rakam, . _ - olabilir.");
      if(p.length<6) return sheetErr("Şifre en az 6 karakter olmalı.");
      const btn = form.querySelector(".btn.pri"); btn.disabled = true; btn.textContent = "Hesap açılıyor…";
      try{ const nid = await createStudentAccount(u, p);
        S.students.set(nid, {...blank({name,alan:fd.get("alan"),sinif:sn,okul,kullanici:u}), ilkSifre:true}); persistDoc("students", nid, 0);
        S.cur=nid; S.view="detay"; S.dtab="ozet"; closeSheet(); render(); toast(`Hesap açıldı · @${u} · ilk şifre ${p}`); }
      catch(e){ btn.disabled=false; btn.textContent="Ekle"; sheetErr(authMsg(e)); }
    });
  }
}
function wireSheetExtras(){
  const del = document.getElementById("m-del");
  if(del) del.addEventListener("click", ()=>{
    if(!del.dataset.armed){ del.dataset.armed="1"; del.textContent="Tüm verisi silinsin mi? Onayla"; return; }
    const id = S.cur; del.disabled = true; del.textContent = "Siliniyor…";
    callFn("ogrenciSil", {uid:id}).then(()=>{ S.students.delete(id); S.cnotes.delete(id); S.cur=null; S.view="ogrenciler"; closeSheet(); render(); toast("Öğrenci ve giriş hesabı silindi"); })
      .catch(e=>{ console.warn(e); S.students.delete(id); persistDoc("students", id, 0); S.cnotes.delete(id); persistDoc("coachNotes", id, 0); S.cur=null; S.view="ogrenciler"; closeSheet(); render(); toast("Öğrenci kaydı silindi (giriş hesabı silinemedi)"); });
  });
  const rs = document.getElementById("m-reset");
  if(rs) rs.addEventListener("click", ()=>{
    const p = $("#m-np").value.trim(), err = t => { $("#m-rerr").textContent = t; };
    if(p.length < 6) return err("Şifre en az 6 karakter olmalı.");
    rs.disabled = true; rs.textContent = "Sıfırlanıyor…"; err("");
    callFn("sifreSifirla", {uid:S.cur, sifre:p}).then(()=>{ toast(`Şifre sıfırlandı · yeni şifre ${p}`); rs.textContent = "Sıfırlandı ✓"; })
      .catch(e=>{ rs.disabled = false; rs.textContent = "Şifreyi sıfırla"; err(e && e.message ? e.message : "Sıfırlanamadı, tekrar dene."); });
  });
}
function updateNets(){
  let tot=0; document.querySelectorAll("#sheetForm .dyrow[data-mx]").forEach(r=>{ const [d,y]=r.querySelectorAll("input"); const D=num(d.value)||0, Y=num(y.value)||0, mx=+r.dataset.mx; const n = D-Y/4; const out=r.querySelector(".net"); if(d.value===""&&y.value===""){ out.textContent="—"; } else { out.textContent = fmt(n); out.style.color = D+Y>mx ? "var(--bad)" : ""; tot+=n; } });
  const t=$("#net-tot"); if(t) t.textContent = fmt(tot);
}

/* ---------- Etkileşim ---------- */
function mutate(fn){ const s = st(); if(!s) return; fn(s); save(); }
const topic = (s,k) => s.topics[k] || (s.topics[k] = {});
function toast(t){ document.querySelectorAll(".toast").forEach(x=>x.remove()); const el=document.createElement("div"); el.className="toast"; el.textContent=t; document.body.appendChild(el); setTimeout(()=>el.remove(),2200); }

document.addEventListener("click", e=>{
  const b = e.target.closest("[data-act]"); if(!b || b.tagName==="SELECT" || b.tagName==="INPUT") return;
  const a = b.dataset.act, v = b.dataset.v;
  if(A() && b.closest("#settingsPage") && onSettingClick(a, b)) return;
  switch(a){
    case "arole": S.authRole=v; if(v==="student" && S.auth==="admin") S.auth="login"; renderAuth(); break;
    case "amode": S.auth=v; renderAuth(); window.scrollTo(0,0); break;
    case "install": doInstall(); break;
    case "logout": logout(); break;
    case "pushon": enablePush(); break;
    case "go": S.view=v; if(v==="program"){ S.pmode="gun"; S.day=today(); S.week= st() ? curStart(st()) : monday(new Date()); if(!A() && st()){ const x=st(); if(x.programYeni && x.programYeni>(x.programSeen||"")){ x.programSeen=x.programYeni; save(); } } } closeSheet(); render(); window.scrollTo(0,0); break;
    case "bell": S.view="bildirim"; render(); window.scrollTo(0,0); break;
    case "open": if(!b.dataset.id) break; S.cur=b.dataset.id; S.week=curStart(st()); S.view="detay"; S.dtab="ozet"; render(); window.scrollTo(0,0); break;
    case "dtab": S.dtab=v; if(v==="program"){ S.pmode="gun"; S.day=today(); S.week=curStart(st()); } render(); break;
    case "pmode": S.pmode=v; render(); break;
    case "day": S.day=v; S.pmode="gun"; render(); break;
    case "wk": { const d=+b.dataset.d, x=st(); S.week = d<0 ? pPrev(x,S.week) : d>0 ? pNext(x,S.week) : curStart(x); S.day = d ? S.week : today(); render(); break; }
    case "ex": S.ex=v; render(); break;
    case "aytall": S.aytAll=!S.aytAll; render(); break;
    case "tick": { const d=b.dataset.date, id=b.dataset.id; mutate(s=>{ const it=dayTasks(s,d).find(x=>x.id===id); if(it){ it.done=!it.done; it.doneAt = it.done ? today() : null; if(it.done && !A()){ const l=dayTasks(s,d); if(l.every(x=>x.done)) setTimeout(()=>toast("Bugünün tüm görevleri tamam! 🎉"),50); } } }); render(); break; }
    case "copyweek": { if(!A()) break; mutate(s=>{ const pw=pPrev(s,S.week), pp=plan(s,pw), np=ensurePlan(s,S.week), oldDays=pDays(s,pw); let c=0;
      pDays(s,S.week).forEach((cd,i)=>{ const pd = oldDays.find(o=>dIdx(o)===dIdx(cd)); if(!pd) return; const src=dayTasks(s,pd); c+=src.length; setDayTasks(s,cd, src.map(t=>({id:uid(), t:taskText(t), done:false, doneAt:null}))); const sv=(pp.saat||{})[pIdx(s,pd)]; if(sv!=null&&sv!=="") np.saat[i]=sv; });
      np.hedef = {}; Object.entries(pp.hedef||{}).forEach(([d,v])=>{ if(v&&v.konu) np.hedef[d]={konu:v.konu, done:false}; });
      toast(c?`Geçen haftanın planı kopyalandı (${c} görev)`:"Geçen hafta için plan yok"); }); render(); break; }
    case "gtick": { const w=b.dataset.w, d=b.dataset.ders; mutate(s=>{ const p=ensurePlan(s,w); if(p.hedef[d]) p.hedef[d].done=!p.hedef[d].done; }); render(); break; }
    case "cpsel": { document.querySelectorAll('#sheetForm input[name=days]').forEach(c=>{ const di=dIdx(c.value); c.checked = v==="hepsi" ? true : di<5; }); break; }
    case "rep": case "yan": { const f = a==="rep"?"r":"y"; mutate(s=>{ const t=topic(s,b.dataset.k); t[f]=Math.max(0,(t[f]||0)+(+b.dataset.d)); }); keepOpen(()=>render()); break; }
    case "sb": mutate(s=>{ const t=topic(s,b.dataset.k); t[b.dataset.f]=!t[b.dataset.f]; }); keepOpen(()=>render()); break;
    case "ddel": { if(!b.dataset.armed){ b.dataset.armed="1"; b.style.color="var(--bad)"; b.style.borderColor="var(--bad)"; toast("Silmek için tekrar dokun"); setTimeout(()=>{ if(b.isConnected){ delete b.dataset.armed; b.style.color=""; b.style.borderColor=""; } },2500); break; }
      mutate(s=>{ s.denemeler=s.denemeler.filter(d=>d.id!==b.dataset.id); }); render(); toast("Deneme silindi"); break; }
    case "tstart": mutate(s=>{ s.timer={start:Date.now()}; }); render(); break;
    case "tstop": { let added=0; mutate(s=>{ if(!s.timer) return; const d=iso(new Date(s.timer.start)); added=Math.round(timerMin(s)); s.gunluk=s.gunluk||{}; if(added>0) s.gunluk[d]=(s.gunluk[d]||0)+added; s.timer=null; }); render(); toast(added>0?`+${fmtMin(added)} kaydedildi`:"1 dakikadan kısa süre kaydedilmedi"); break; }
    case "sheet": openSheet(v, b); wireSheetExtras(); break;
    case "dtur": { S.ex=v; openSheet("deneme", b); break; }
    case "mode": THEME.mode=v; applyTheme(); openSheet("tema"); render(); break;
    case "accent": THEME.accent=v; applyTheme(); openSheet("tema"); render(); break;
    case "addq": { const h=$("#su-h"), m=$("#su-m"); const t=(num(h.value)||0)*60+(num(m.value)||0)+(+v); h.value=Math.floor(t/60); m.value=t%60; break; }
    case "sendnote": { const t=$("#kn").value.trim(); if(!t){ toast("Önce notu yaz"); break; } mutate(s=>{ s.koctanNot={text:t, date:nowISO()}; }); render(); toast("Not öğrencinin ana sayfasına gönderildi"); break; }
    case "clearnote": mutate(s=>{ s.koctanNot=null; }); render(); toast("Not kaldırıldı"); break;
  }
});
function keepOpen(fn){ const open = [...document.querySelectorAll("details.subj")].map((d,i)=>d.open?i:-1).filter(i=>i>=0); fn(); const ds=document.querySelectorAll("details.subj"); open.forEach(i=>{ if(ds[i]) ds[i].open=true; }); }
document.addEventListener("change", e=>{
  const t = e.target;
  if(A() && t.closest && t.closest("#settingsPage")){ if(onSetting(t,true) && (t.dataset.curt!=null || t.dataset.cur!=null)) keepSettingsOpen(); return; }
  if(t.name==="sinif"){ const w = t.closest("form")?.querySelector("#okulWrap,#m-okulWrap"); if(w) w.hidden = t.value==="Mezun"; }
  else if(t.dataset.net){ const i=document.getElementById(t.dataset.net); i.disabled=t.checked; if(t.checked) i.value=""; }
  else if(t.dataset.act==="pick"){ S.cur=t.value; S.week=curStart(st()); S.day=today(); render(); }
  else if(t.dataset.quick!=null && t.value){ const d=t.dataset.quick, ta=document.getElementById("pl-"+pIdx(st(),d)); if(ta){ ta.value = (ta.value.trim()? ta.value.replace(/\s+$/,"")+"\n" : "") + t.value; ta.dispatchEvent(new Event("input",{bubbles:true})); } t.value=""; }
  else if(t.dataset.plan || t.dataset.hd==="konu"){ setTimeout(()=>{ if(!document.activeElement || !document.activeElement.matches("textarea,input[type=text],input[type=number]")) render(); }, 0); }
  else if(t.dataset.f && t.type==="date"){ setField(t.dataset.f, t.value); }
});
document.addEventListener("input", e=>{
  const t = e.target;
  if(A() && t.closest && t.closest("#settingsPage")){ onSetting(t,false); return; }
  if(t.dataset.dy) updateNets();
  else if(t.dataset.act==="q"){ S.q=t.value; const pos=t.selectionStart; render(); const n=$("#q"); if(n){ n.focus(); try{ n.setSelectionRange(pos,pos); }catch(_){} } }
  else if(t.dataset.act==="tnote"){ mutate(s=>{ topic(s,t.dataset.k).n=t.value; }); }
  else if(t.dataset.plan && A()){ const d=t.dataset.plan; mutate(s=>setDayTasks(s,d,linesToTasks(dayTasks(s,d), t.value))); const ph=document.getElementById("ps-"+pIdx(st(),d)); if(ph){ const a=autoHours(st(),d); ph.placeholder = a?String(Math.round(a*10)/10).replace(".",","):"0"; } }
  else if(t.dataset.hs!=null && t.dataset.hs!=="" && A()){ const i=t.dataset.hs; mutate(s=>{ const p=ensurePlan(s,S.week); const v=num(t.value); if(v==null) delete p.saat[i]; else p.saat[i]=Math.max(0,Math.min(16,v)); }); }
  else if(t.dataset.hd && A()){ const d=t.dataset.ders, v=t.value; mutate(s=>{ if(t.dataset.hd==="kitap"){ s.kitaplar=s.kitaplar||{}; if(v.trim()) s.kitaplar[d]=v; else delete s.kitaplar[d]; } else { const p=ensurePlan(s,S.week); if(v.trim()) p.hedef[d]={konu:v, done:!!(p.hedef[d]&&p.hedef[d].done)}; else delete p.hedef[d]; } }); }
  else if(t.dataset.cnote && A()){ S.cnotes.set(S.cur, {...(S.cnotes.get(S.cur)||{}), not:t.value}); persistDoc("coachNotes", S.cur, 800); }
  else if(t.dataset.f && t.type!=="date"){ setField(t.dataset.f, t.value); }
});
function setField(path, v){ if(!A()) return; mutate(s=>{ const [a,b]=path.split("."); if(b){ s[a]=s[a]||{}; s[a][b] = b==="tarih" ? v : num(v); } else s[a]=v; }); }
document.addEventListener("submit", e=>{
  const f = e.target; if(f.id==="sheetForm") return; e.preventDefault();
  authErr("");
  try{ if(f.id==="fSignup") doSignup(f); else if(f.id==="fLogin") doLogin(f); else if(f.id==="fFirst") doFirstPassword(f); }
  catch(err){ authErr("Bir sorun oldu: "+(err && err.message || err)); }
});

/* Kronometre ve canlı süre */
setInterval(()=>{
  if(!S.role || A()) return; const s = st(); if(!s || !s.timer) return;
  const tv=$("#tval"); if(tv) tv.textContent = clock(timerMin(s)*60);
  const tt=$("#ttoday"); if(tt) tt.textContent = fmtMin(minutes(s,today()));
  const lm=$("#liveMin"); if(lm) lm.textContent = fmtMin(minutes(s,today()));
}, 1000);

render();
init();

