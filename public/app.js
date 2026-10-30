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
  chat:'<path d="M4 5h16v11H9l-5 4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
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
const LOGO = `<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="16" cy="67" r="6" fill="#fff"/><path d="M27 54 L43 35 L56 66 L76 41" fill="none" stroke="#fff" stroke-width="10.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M84.75 30.07 L84.59 47.88 L67.41 34.13 Z" fill="#fff" stroke="#fff" stroke-width="3" stroke-linejoin="round"/></svg>`;
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
if(!THEME.v){ THEME.mode = "light"; THEME.accent = "green"; THEME.v = 2; } /* yeni varsayılan: açık mod, yeşil */
THEME.mode = THEME.mode || "light"; THEME.accent = THEME.accent || "green";
function applyTheme(){
  const r = document.documentElement;
  r.classList.toggle("m-light", THEME.mode==="light"); r.classList.toggle("m-dark", THEME.mode==="dark");
  r.setAttribute("data-accent", THEME.accent);
  setBarColor();
  try{ localStorage.setItem("zk-theme", JSON.stringify(THEME)); }catch(e){}
}
/* Telefonun üst çubuğu: açık modda tema rengi, koyu modda koyu zemin */
function setBarColor(){ const dark = THEME.mode==="dark" || (THEME.mode==="system" && matchMedia("(prefers-color-scheme: dark)").matches);
  const c = dark ? "#0A0B0E" : ({green:"#1E9E4A", blue:"#2563EB", red:"#DC2F3C"}[THEME.accent] || "#1E9E4A");
  const m = document.querySelector('meta[name="theme-color"]'); if(m) m.setAttribute("content", c); }
try{ matchMedia("(prefers-color-scheme: dark)").addEventListener("change", setBarColor); }catch(e){}
applyTheme();

/* ---------- Durum ---------- */
const S = { students:new Map(), cnotes:new Map(), notifs:new Map(), gorus:new Map(), settings:{examDate:"2027-06-19", tahmini:false},
  ready:false, role:null, me:null, auth:"signup", authRole:"student",
  view:"home", cur:null, dtab:"ozet", week:monday(new Date()), day:today(), pmode:"gun", ex:"TYT", aytAll:false, q:"" };
const A = () => S.role === "admin";
function cfg(){ const x = S.settings; return {
  kurum: x.kurum || "Zekacademy",
  odemeAcik: x.odemeAcik !== false, odemeSaat: x.odemeSaat || "18:00", odemeMesaj: x.odemeMesaj || DEF_ODEME_MESAJ, gorusmeHatirlat: x.gorusmeHatirlat !== false,
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
const MAPS = { students:()=>S.students, notifs:()=>S.notifs, coachNotes:()=>S.cnotes, gorusmeler:()=>S.gorus };
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
  unsubs.push(onSnapshot(doc(fdb,"settings","main"), s=>{ if(s.exists() && !setDirty){ S.settings = {...S.settings, ...JSON.parse(JSON.stringify(s.data()))}; } if(A() && S.settings.tahmini && S.settings.examDate==="2027-06-19"){ S.settings.tahmini=false; saveSettings(); } /* 19 Haziran 2027 kesinleşti */ loaded.settings=true; checkReady(need); render(true); },
    e=>{ console.error("settings", e); loaded.settings=true; checkReady(need); render(); }));
}
function checkReady(need){ if(!S.ready && need.every(k=>loaded[k])){ S.ready = true; if(S.role==="student") startStudent(S.me); openDeepLink(); render(); pushSupported().then(()=>{ refreshPush(); render(); }); } }
function openDeepLink(){ const v = new URLSearchParams(location.search).get("ac"); if(!v) return; if(v==="program"){ S.view="program"; S.pmode="gun"; S.day=today(); if(st()) S.week=curStart(st()); } else if(v==="bildirim") S.view="bildirim"; history.replaceState(null, "", "/"); }
function stopWatching(){ unsubs.forEach(u=>{ try{ u(); }catch(e){} }); unsubs = []; BASE.clear(); for(const k in loaded) delete loaded[k]; S.students.clear(); S.notifs.clear(); S.cnotes.clear(); S.gorus.clear(); S.ready = false; }

let authResolved = false;
function init(){
  onAuthStateChanged(auth, user=>{
    authResolved = true; stopWatching();
    if(!user){ S.role=null; S.me=null; render(); return; }
    if(user.email === COACH_EMAIL){
      S.role = "admin"; S.me = null; S.view = "ozet";
      const need = ["students","notifs","coachNotes","gorusmeler","settings"]; need.slice(0,4).forEach(c=>watchColl(c, need)); watchSettings(need);
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
    if(!authResolved){ root.innerHTML = `<div class="auth"><div class="apanel" style="align-items:center;padding-top:30vh"><div class="lm" style="width:56px;height:56px;border-radius:16px">${LOGO}</div><p class="muted">Panelin açılıyor…</p></div></div>`; return; }
    if(fromSnap && $("#root .auth form") && root.contains(document.activeElement)){ const b = $("#root .auth form .btn.pri"); if(b && b.disabled){ b.disabled=false; b.textContent=b.dataset.label; } return; }
    renderAuth(); return;
  }
  if(!S.ready){ root.innerHTML = `<div class="auth"><div class="apanel" style="align-items:center;padding-top:30vh"><div class="lm" style="width:56px;height:56px;border-radius:16px">${LOGO}</div><p class="muted">Panelin açılıyor…</p></div></div>`; return; }
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
  return `${topbar(`<div class="logo"><span class="lm">${LOGO}</span>${esc(cfg().kurum)}</div>`, bellBtn(nots.length))}
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
      <button type="button" class="kpick" id="hk-${esc(d)}" data-act="sheet" data-v="konu" data-ders="${esc(d)}">${h[d]?.konu?esc(h[d].konu):`<span class="faint">Konu seç</span>`}<span class="kpi">${icon("search","xs")}</span></button>
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
/* ---------- Türkiye Yüzyılı Maarif Modeli konu havuzu (9, 10, 11. sınıf öğrencileri) ----------
   Kaynak: MEB öğretim programları (tymm.meb.gov.tr), tema ve içerik çerçeveleri. 1. Aşama: 9-10. sınıf, 2. Aşama: 11. sınıf (12. sınıf programı 2027-28'de eklenecek). */
const MAARIF = [{"d":"Matematik","dk":"mat","s":9,"t":[["Sayılar",["Üslü ve Köklü Gösterimlerle İşlemler","Gerçek Sayı Aralıkları ve Küme Sembolleri","Sayı Kümeleri ve İşlem Özellikleri","İşlem Özelliklerini Cebirsel İfade Etme"]],["Nicelikler ve Değişimler",["Doğrusal Fonksiyonlar ve Nitel Özellikleri","Mutlak Değer Fonksiyonu ve Nitel Özellikleri","Doğrusal Denklem ve Eşitsizlik Problemleri"]],["Geometrik Şekiller",["Üçgende Açı ve Kenar Özellikleri","Üçgen Oluşturabilme Koşulları"]],["Eşlik ve Benzerlik",["Geometrik Dönüşümler","Eşlik ve Benzerlik Koşulları","Benzer Üçgenler Oluşturma","Tales, Öklid ve Pisagor Teoremleri","Eşlik ve Benzerlik Problemleri"]],["Algoritma ve Bilişim",["Algoritma Temelli Problemler","Mantık Bağlaçları ve Niceleyiciler","Bağlaç ve Niceleyicilerin Algoritmik Problemlerde Kullanımı"]],["İstatistiksel Araştırma Süreci",["Tek Nicel Değişkenli Veri Dağılımları","Hazır Veri Dağılımlarını İnceleme"]],["Veriden Olasılığa",["Deneysel Olasılık","Teorik Olasılık"]]]},{"d":"Matematik","dk":"mat","s":10,"t":[["Geometrik Şekiller",["Dik Üçgende Trigonometrik Oranlar ve Özdeşlikler","Üçgende Yardımcı Elemanlar","Üçgenin Alanı","Sinüs ve Kosinüs Teoremleri"]],["İstatistiksel Araştırma Süreci",["İki Kategorik Değişkenli Veriler","Hazır İki Kategorik Değişkenli Verileri İnceleme"]],["Sayılar",["Asal Çarpanlar ve Bölenler","EBOB ve EKOK","Bölünebilme"]],["Nicelikler ve Değişimler",["Fonksiyon Olma Şartları","Karesel Fonksiyon","Karekök Fonksiyonu","Rasyonel Fonksiyon","Ters Fonksiyonlar","Fonksiyonlarla Denklem ve Eşitsizlik Problemleri"]],["Sayma, Algoritma ve Bilişim",["Sayma Stratejileri","Cebirsel ve Fonksiyonel İşlemlerin Algoritmik Yapısı"]],["Analitik İnceleme",["Noktanın Analitik İncelenmesi","Doğrunun Analitik İncelenmesi"]],["Veriden Olasılığa",["Koşullu Olasılık","Bayes Teoremi"]]]},{"d":"Matematik","dk":"mat","s":11,"t":[["İstatistiksel Araştırma Süreci",["İki Nicel Değişkenli Veriler","Hazır İki Nicel Değişkenli Verileri İnceleme"]],["Geometrik Şekiller",["Dörtgenlerin Özellikleri","Özel Dörtgenler Arasındaki İlişkiler","Çokgenlerin Sınıflandırılması","Dışbükey Çokgenlerin Özellikleri","Çokgen Problemleri"]],["Nicelikler ve Değişimler · Trigonometri",["Trigonometrik Fonksiyonlar ve Nitel Özellikleri","Trigonometrik Denklem Problemleri"]],["Nicelikler ve Değişimler · Üstel ve Logaritma",["Üstel Fonksiyonlar","Üstel Fonksiyonların Tersi","Logaritmik Fonksiyonlar","Üstel ve Logaritmik Denklem/Eşitsizlik Problemleri"]],["Nicelikler ve Değişimler · Fonksiyonlarda İşlemler",["Fonksiyonların Bileşkesi","Fonksiyonlarda Dört İşlem"]]]},{"d":"Fizik","dk":"fiz","s":9,"t":[["Fizik Bilimi ve Kariyer Keşfi",["Fizik Bilimi","Fizik Biliminin Alt Dalları","Fizik Bilimine Yön Verenler","Fizik ile İlgili Kariyer Keşfi"]],["Kuvvet ve Hareket",["Temel ve Türetilmiş Nicelikler","Skaler ve Vektörel Nicelikler","Vektörler","Doğadaki Temel Kuvvetler","Hareket ve Hareket Türleri"]],["Akışkanlar",["Basınç","Sıvılarda Basınç","Açık Hava Basıncı","Kaldırma Kuvveti","Bernoulli İlkesi"]],["Enerji",["İç Enerji, Isı ve Sıcaklık","Öz Isı ve Isı Sığası","Hâl Değişimi","Isıl Denge","Isı Aktarım Yolları","Isı İletim Hızı"]]]},{"d":"Fizik","dk":"fiz","s":10,"t":[["Kuvvet ve Hareket",["Sabit Hızlı Hareket","Bir Boyutta Sabit İvmeli Hareket"]],["Enerji",["İş, Enerji ve Güç","Enerji Biçimleri","Mekanik Enerji","Enerji Kaynakları"]],["Elektrik",["Basit Elektrik Devreleri","Elektrik Akımı","Ohm Yasası","Dirençlerin Bağlanması","Üreteçlerin Bağlanması","Elektrik Güvenliği ve Topraklama"]],["Dalgalar",["Periyodik Hareketler","Dalgaların Temel Kavramları","Dalgaların Sınıflandırılması","Yayılma Süratini Etkileyen Etmenler","Su Dalgalarında Yansıma ve Kırılma","Rezonans ve Deprem"]]]},{"d":"Fizik","dk":"fiz","s":11,"t":[["Kuvvet ve Hareket",["Serbest Düşme","İki Boyutta Sabit İvmeli Hareket","Newton Hareket Yasaları","Sürtünme Kuvveti","Limit Hız","Çembersel Hareket"]],["Elektrik ve Manyetizma",["Elektriksel Kuvvet ve Elektriksel Alan","Manyetik Alan ve Manyetik Kuvvet","İndüksiyon Akımı","Transformatörler"]],["Optik",["Işık Şiddeti, Işık Akısı ve Aydınlanma","Düzlem Aynalar","Küresel Aynalar","Kırılma","Görünür Derinlik","Fiber Optik","Prizmalar","Mercekler"]]]},{"d":"Kimya","dk":"kim","s":9,"t":[["Etkileşim",["Günlük Hayatta Kimya ve Güvenlik","Kimyanın Alt Disiplinleri ve Kariyer","Atom Teorileri ve Atomun Yapısı","Atom Orbitalleri ve Elektron Dizilimi","Periyodik Tabloda Yer Bulma","Periyodik Özellikler"]],["Çeşitlilik",["Metalik Bağ","İyonik Bağ","Kovalent Bağ ve Lewis Yapısı","Molekül Polarlığı","Bileşiklerin Adlandırılması","Moleküller Arası Etkileşimler","Katılar (Amorf ve Kristal)","Sıvılar ve Özellikleri"]],["Sürdürülebilirlik",["Metal Nanoparçacıklar","Metal, Alaşım ve Nanoparçacıkların Çevresel Etkileri","Yeşil Kimyanın Atık Önleme İlkesi"]]]},{"d":"Kimya","dk":"kim","s":10,"t":[["Etkileşim",["Kimyasal Değişimin Göstergeleri","Kimyasal Tepkime Türleri","Mol Kavramı","Tepkime Denklemlerini Denkleştirme","Kimyasal (Stokiyometrik) Hesaplamalar","Gazlar ve Kinetik Moleküler Teori","Gaz Yasaları ve İdeal Gaz","Graham Difüzyon ve Efüzyon Yasası"]],["Çeşitlilik",["Çözünme Süreci ve Çözünebilirlik","Çözünürlük ve Etki Eden Faktörler","Çözeltilerin Sınıflandırılması","Derişim Birimleri (Molarite, ppm)","Koligatif Özellikler"]],["Sürdürülebilirlik",["Makro ve Mikro Ölçekli Deneyler","Atmosferdeki Tepkimeler ve Küresel Sorunlar"]]]},{"d":"Kimya","dk":"kim","s":11,"t":[["Etkileşim",["Tepkimelerde Enerji Değişimi","Bağ Enerjileriyle Tepkime Entalpisi","Oluşum Entalpileriyle Tepkime Entalpisi","Tepkimelerin Gerçekleşme Şartları","Ortalama Tepkime Hızı","Tepkime Hızına Etki Eden Faktörler","Hız Denklemi"]],["Çeşitlilik",["Tersinir Tepkimeler ve Denge","Denge Sabiti ve Tepkime Oranı","Dengeyi Etkileyen Faktörler","Suyun Otoiyonizasyonu ve Asit-Baz Teorileri","Asit-Baz Kuvveti ve pH","Nötralleşme ve Titrasyon","Molar Çözünürlük ve Kçç","Çözünürlüğe Etki Eden Faktörler"]],["Sürdürülebilirlik",["Fermantasyonla Yeşil Hidrojen","Nanoteknolojik Ürünler: Fayda ve Zarar","Mikroplastik ve Nanoplastikler"]]]},{"d":"Biyoloji","dk":"bio","s":9,"t":[["Yaşam",["Biyolojinin Önemi ve Gelişimi","Bilimin Doğası ve Bilimsel Araştırma","Bilim Etiği","Canlıların Ortak Özellikleri","İnorganik Moleküller (Su, Mineraller)","Karbohidratlar","Lipitler","Proteinler ve Enzimler","Nükleik Asitler","Vitaminler"]],["Organizasyon",["Prokaryot ve Ökaryot Hücre","Hücre Zarı ve Sitoplazma","Organeller ve Çekirdek","Hücre Zarından Madde Geçişleri","Sınıflandırma ve İkili Adlandırma","Bakteriler ve Arkeler","Ökaryotlar (Protist, Bitki, Mantar, Hayvan)","Biyoçeşitlilik"]]]},{"d":"Biyoloji","dk":"bio","s":10,"t":[["Enerji",["ATP ve Enerji Aktarımı","Fotosentez","Fotosentez Hızını Etkileyen Faktörler","Kemosentez","Hücre İçi ve Hücre Dışı Sindirim","İnsanda Sindirim, Emilim ve Taşınma","Hücresel Solunum","Besinlerin Solunuma Katılması","Fermantasyon","Enerji-Metabolizma İlişkisi"]],["Ekoloji",["Ekosistemin Bileşenleri","Tür İçi ve Türler Arası Etkileşimler","Süksesyon","Popülasyon Dinamikleri","Madde ve Enerji Akışı","Biyolojik Birikim","Madde Döngüleri","Ekolojik Sürdürülebilirlik"]]]},{"d":"Biyoloji","dk":"bio","s":11,"t":[["Tepki",["Canlılarda Uyaranlara Tepki","Bitkilerde Hormonlar ve Tepki","Nöronların Yapısı ve Sinyal İletimi","Sinaps","Duyu Organları","İnsan Sinir Sistemi ve Refleksler","Kemik, Eklem ve Kaslar","Kasılma Mekanizması","Bağışıklık ve Alerji"]],["Homeostazi",["Homeostazi ve Geri Bildirim","Sinir ve Endokrin Sistem ile Homeostazi","Dolaşım Sistemi ve Homeostazi","Solunum Sistemi ve Homeostazi","Boşaltım Sistemi ve Homeostazi","Sistemlerin Eş Güdümü","Homeostazi Bozuklukları"]]]},{"d":"Türk Dili ve Edebiyatı","dk":"tde","s":9,"t":[["Sözün İnceliği",["Şiir","Deneme","Betimleme Paragrafı","Mülakat","Ses Bilgisi"]],["Anlam Arayışı",["Hikâye","Anı (Hatıra)","İstiklal Marşı","Şiir Yazma"]],["Anlamın Yapı Taşları",["Hikâye: Olay Örgüsü, Anlatıcı, Bakış Açısı","Gezi Yazısı","Belgesel","Şekil Bilgisi","Söz Varlığı"]],["Dilin Zenginliği",["Roman","Tiyatro","Eleştiri","Otobiyografi","Sosyal Medya Dili","Ekler","Yazım ve Noktalama"]]]},{"d":"Türk Dili ve Edebiyatı","dk":"tde","s":10,"t":[["Sözün Ezgisi",["Koşuk","Türkü ve Koşma","Ninni ve Masal","İsim ve Sıfat","İsim ve Sıfat Tamlamaları"]],["Kelimelerin Ritmi",["Gazel ve Kaside","Saf Şiir","Söyleşi","Bilgilendirici Metin","Zamir","Edat, Bağlaç ve Ünlem"]],["Dünden Bugüne",["Destan","Halk Hikâyesi","Mesnevi","Fabl","Zarf"]],["Nesillerin Mirası",["Dede Korkut Hikâyeleri","Tanzimat Dönemi Şiiri","Servetifünun Romanı","Fecriati Şiiri","Millî Edebiyat Hikâyesi","Fiiller"]]]},{"d":"Türk Dili ve Edebiyatı","dk":"tde","s":11,"t":[["Bir Diyeceğim Var!",["Karagöz","Mektup","Dilekçe","E-posta","Fiilimsiler"]],["Kültür Yolculuğu",["Türk Dünyası Edebiyatı","Orhun Abideleri","Dîvânu Lugâti't-Türk ve Kutadgu Bilig","Âşık Tarzı Halk Şiiri","Fiilde Kip ve Çatı"]],["Yaşamın İzinde",["Roman","Biyografi","Tezkire","Radyo Tiyatrosu","Cümlenin Ögeleri"]],["Hayatın Aynası",["Tiyatro","Küçürek Hikâye","Belgesel","Afiş","Cümle Türleri"]]]},{"d":"Tarih","dk":"tar","s":9,"t":[["Geçmişin İnşa Sürecinde Tarih",["Tarih Öğrenmenin Faydaları","Tarihin Doğası","Tarihsel Bilginin Üretim Süreci","Tarih Araştırmasında Dijitalleşme"]],["Eski Çağ Medeniyetleri",["Tarım Devrimi, Yerleşme ve Ekonomi","Eski Çağda Yönetim ve Ordu","Eski Çağda Hukuk","Eski Çağda İnanç, Bilim ve Sanat","Türklerde Konargöçer Yaşam"]],["Orta Çağ Medeniyetleri",["Orta Çağda Kitlesel Göçler","Başlıca Devletlerin Yönetim ve Ordu Yapıları","Orta Çağda Ticaret Yolları","Medeniyet Havzalarında Bilim, Kültür ve Sanat"]]]},{"d":"Tarih","dk":"tar","s":10,"t":[["Türkistan'dan Türkiye'ye (1040-1299)",["Önemli Askerî Mücadeleler","Devlet ve Ordu Teşkilatında Değişim","Sosyal Yaşam ve Ekonomik Faaliyetler","Türk-İslam Medeniyetinde Bilim, Kültür ve Sanat"]],["Beylikten Devlete Osmanlı (1299-1453)",["Kuruluşa Dair Farklı Görüşler","Anadolu ve Rumeli'deki Mücadeleler","Devletleşme: Ordu, Hukuk ve Toprak Sistemi","Fethedilen Topraklarda İzlenen Politikalar","İlim ve İrfan Geleneği"]],["Cihan Devleti Osmanlı (1453-1683)",["Siyasi ve Askerî Mücadeleler","Yönetim ve Ordu Yapısındaki Değişim","Avrupa'nın Sömürgeci Politikaları","Önemli İsyanlar: Neden ve Sonuçları","Bilim, Kültür, Eğitim ve Sanat"]]]},{"d":"Tarih","dk":"tar","s":11,"t":[["Değişen Dünyada Osmanlı (1683-1789)",["Siyasi ve Askerî Mücadeleler","Lale Devri","1755 Lizbon ve 1766 İstanbul Depremleri","Sanayi Devrimi ve Etkileri"]],["Dönüşüm Sürecinde Osmanlı (1789-1908)",["Fransız İhtilali ve Etkileri","Siyasi, Askerî ve İdari Gelişmeler","Bilim, Sanat ve Teknoloji","Sanayileşme Çabaları"]],["Savaşlar Sarmalında Osmanlı (1908-1918)",["Siyasi ve Askerî Gelişmeler","Kitlesel Göç ve Salgınlar","Osmanlı'nın İnsanlık Tarihine Katkıları"]]]},{"d":"Coğrafya","dk":"cog","s":9,"t":[["Coğrafyanın Doğası",["Coğrafyanın Konusu ve Bölümleri","Niçin Coğrafya Öğrenmeliyiz?","Coğrafya Biliminin Gelişimi"]],["Mekânsal Bilgi Teknolojileri",["Haritalar","Türkiye'nin Coğrafi Konumu","Mekânsal Bilgi Teknolojilerinin Bileşenleri"]],["Doğal Sistemler ve Süreçler",["Hava Olayları","İklim Sisteminin Bileşenleri","İklim Türleri","İklim Sistemindeki Değişiklikler"]],["Beşerî Sistemler ve Süreçler",["Nüfusun Tarihsel Değişimi","Nüfusun Dağılışı ve Hareketleri","Demografik Dönüşüm ve Nüfus Piramitleri","Nüfus Politikaları"]],["Ekonomik Faaliyetler ve Etkileri",["Ekonomik Faaliyetleri Etkileyen Coğrafi Faktörler"]],["Afetler ve Sürdürülebilir Çevre",["Tehlike, Risk ve Afet","Afet Türleri","Bütüncül Afet Yönetimi"]],["Bölgeler, Ülkeler ve Küresel Bağlantılar",["Bölge ve Bölge Sınırı"]]]},{"d":"Coğrafya","dk":"cog","s":10,"t":[["Coğrafyanın Doğası",["Coğrafi Bakış"]],["Mekânsal Bilgi Teknolojileri",["CBS ve Uzaktan Algılama","Mekânsal Verilerin Haritalara Aktarılması"]],["Doğal Sistemler ve Süreçler",["Tektonik Süreçler","Aşınma ve Çözünme Süreçleri","Aşınım-Birikim ve Yeryüzü Şekilleri","Yeryüzü Şekilleri ve Beşerî Faaliyetler"]],["Beşerî Sistemler ve Süreçler",["Yerleşmelerin Kuruluşu ve Gelişimi","Yerleşmelerin Fonksiyonları"]],["Ekonomik Faaliyetler ve Etkileri",["Ekonomik Faaliyetlerin Özellikleri","Ekonomik Sektörler ve Gelişmişlik","Türkiye Ekonomisinin Sektörel Dağılımı"]],["Afetler ve Sürdürülebilir Çevre",["Afetlerle Mücadelede İyi Örnekler","Afetlere Dirençli Yaşam Alanları","Afetlerden Korunma ve Afet Bilinci"]],["Bölgeler, Ülkeler ve Küresel Bağlantılar",["Türk Kültürünün Mekânsal Özellikleri"]]]},{"d":"Coğrafya","dk":"cog","s":11,"t":[["Coğrafyanın Doğası",["Mekânsal Sorunlar ve Coğrafya"]],["Mekânsal Bilgi Teknolojileri",["Web Tabanlı CBS Uygulamaları"]],["Doğal Sistemler ve Süreçler",["Su Kaynakları","Türkiye'deki Su Kaynakları"]],["Beşerî Sistemler ve Süreçler",["Yerleşmelerin Mekânsal Organizasyonu","Yerleşmelerin Etki Alanları"]],["Ekonomik Faaliyetler ve Etkileri",["Tarım ve Gıda Güvencesi","Tarımda Sürdürülebilirlik","Stratejik ve Kritik Madenler","Enerji Kaynakları","Sanayileşmenin Mekânsal Etkileri"]],["Afetler ve Sürdürülebilir Çevre",["Gezegen Sınırı","Küresel İklim Değişikliği","Türkiye'de Suyun Sürdürülebilir Kullanımı"]],["Bölgeler, Ülkeler ve Küresel Bağlantılar",["Türkiye'nin Kültürel Hinterlandı","Tarımsal Üretim: Örnek Ülke","Sanayileşme: Örnek Ülkeler","Madencilik: Örnek Ülke","Enerji Kaynakları: Örnek Ülkeler"]]]},{"d":"Felsefe","dk":"fel","s":10,"t":[["Felsefe Üniteleri",["Felsefenin Doğası","Felsefe, Mantık ve Argümantasyon","Varlık Felsefesi","Bilgi Felsefesi","Ahlak Felsefesi","Estetik ve Sanat Felsefesi","Siyaset Felsefesi","Din Felsefesi","Bilim Felsefesi"]]]},{"d":"Felsefe","dk":"fel","s":11,"t":[["Felsefe Üniteleri",["Çevre Sorunları ve Felsefe","Teknoloji ve Hayat","Akıl ve İnanç","Edebiyat ve Felsefe","Hayatın Anlamı","Hukuk ve Felsefe"]]]}];
const MAARIF_SINIF = ["9. sınıf","10. sınıf","11. sınıf"];
const isMaarif = s => !!s && MAARIF_SINIF.includes(s.sinif);
const MAARIF_ALAN = {mat:["SAY","EA"], fiz:["SAY"], kim:["SAY"], bio:["SAY"], tde:["EA","SÖZ"], tar:["EA","SÖZ"], cog:["EA","SÖZ"], fel:["SÖZ"]};
const MAARIF_GRUP = {mat:["mat",0], fiz:["fen",0], kim:["fen",1], bio:["fen",2], tde:["tr",0], tar:["sos",0], cog:["sos",1], fel:["sos",2]};
const MAARIF_SUBS = MAARIF.flatMap(x=>x.t.map(([n,t],i)=>({k:`m${x.s}${x.dk}${i+1}`, n, ders:x.d, dk:x.dk, sinif:x.s, asama:x.s<=10?1:2, ex:`${x.s}. sınıf`, g:`${x.s}. sınıf · ${i+1}. tema`, t, a:MAARIF_ALAN[x.dk]})));
function maarifList(s, asama, all){ return MAARIF_SUBS.filter(x=>x.asama===asama && (asama===1 || all || !ALANLAR.includes(s.alan) || x.a.includes(s.alan))); }
const asamaSeg = () => `<div class="seg">${[[1,"1. Aşama"],[2,"2. Aşama"]].map(([k,l])=>`<button data-act="mx" data-v="${k}" aria-pressed="${(S.mx||1)===k}">${l}</button>`).join("")}</div>`;
function pKonularMaarif(s){
  const mx = S.mx || 1, list = maarifList(s, mx, S.aytAll), CLS = subColors(list);
  let sum = 0, c = 0; list.forEach(sub=>sub.t.forEach(n=>{ sum += topicScore(s.topics[tkey(sub.k,n)]); c++; })); const pct = c ? sum/c : 0;
  const dersler = [...new Set(list.map(x=>x.ders))];
  const head = A() ? "" : topbar(`<h1 class="ttl">Konu Takibi</h1>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    ${asamaSeg()}
    <div class="card"><div class="sech"><h3>${mx}. Aşama ilerlemesi${mx===2?` · ${esc(s.alan)}`:""}</h3><b class="num">%${Math.round(pct*100)}</b></div><div class="bar" style="margin-top:10px"><i style="width:${pct*100}%"></i></div>
      <p class="muted small" style="margin:10px 0 0">Maarif Modeli konuları, temalara göre. ${mx===1?"9. ve 10. sınıf temaları.":"11. sınıf temaları."} Her konuda: tekrar sayısı, 1. ve 2. soru bankası. Üçü tamamlanan konu yeşil olur.</p>
      ${mx===2?`<div class="pills" style="margin-top:10px"><button class="tog" data-act="aytall" aria-pressed="${S.aytAll}">${S.aytAll?"Tüm dersler gösteriliyor":"Tüm dersleri göster"}</button></div>`:""}</div>
    ${dersler.map(d=>{ const subs = list.map((x,i)=>[x,i]).filter(([x])=>x.ders===d); let ds=0, dc=0; subs.forEach(([x])=>x.t.forEach(n=>{ ds+=topicScore(s.topics[tkey(x.k,n)]); dc++; }));
      const dp = dc ? ds/dc : 0, kon = subs.reduce((a,[x])=>a+x.t.length,0);
      return `<details class="mders" data-ders="${esc(d)}" style="${CLS[subs[0][1]].split('style="')[1]||""}" ${S.mOpen && S.mOpen[d]?"open":""}><summary><span><b>${esc(d)}</b><span class="faint small">${subs.length} tema · ${kon} konu</span></span><div class="bar"><i style="width:${dp*100}%;${dp>=1?"background:var(--good)":""}"></i></div><span class="pct num">%${Math.round(dp*100)}</span></summary>
      <div class="mtemalar">${subs.map(([sub,si])=>{ const p = subjPct(s,sub);
        return `<details class="${CLS[si]}"><summary><span><span class="sn">${esc(sub.n)}</span><span class="sg">${esc(sub.ex)}</span></span><div class="bar"><i style="width:${p*100}%;${p>=1?"background:var(--good)":""}"></i></div><span class="pct num">%${Math.round(p*100)}</span></summary>${konuSatirlari(s, sub)}</details>`; }).join("")}</div></details>`; }).join("")}
  </div>`;
}

/* ---------- Ders renkleri (Konular / Çetele) ---------- */
const DERS_GRUP = {tr:"tr",aede:"tr",mat:"mat",prob:"mat",matd:"mat",geo:"mat",amat:"mat",fiz:"fen",kim:"fen",bio:"fen",afiz:"fen",akim:"fen",abio:"fen",tar:"sos",cog:"sos",fel:"sos",atar:"sos",acog:"sos",afel:"sos"};
function subGrp(sub){ if(sub.dk && MAARIF_GRUP[sub.dk]) return MAARIF_GRUP[sub.dk][0]; if(DERS_GRUP[sub.k]) return DERS_GRUP[sub.k]; const n = trLow(sub.n);
  return /mat|geo|problem/.test(n) ? "mat" : /fiz|kim|biy|fen/.test(n) ? "fen" : /türk|edeb|dil/.test(n) ? "tr" : "sos"; }
/* Aynı gruptaki dersler aynı rengin farklı tonlarında */
function subColors(list){ const seen = {}; return list.map(sub=>{ const g = subGrp(sub), i = sub.dk && MAARIF_GRUP[sub.dk] ? MAARIF_GRUP[sub.dk][1] : (seen[g] = (seen[g]==null ? 0 : seen[g]+1));
  return `subj cl" style="--sc:color-mix(in srgb, var(--c-${g}) ${100-(i%4)*13}%, var(--fg))`; }); }
const trLow = x => String(x||"").toLocaleLowerCase("tr");

function konuSatirlari(s, sub){ return sub.t.map(n=>{ const k=tkey(sub.k,n), t=s.topics[k]||{}, full=topicScore(t)>=1;
        return `<div class="trow ${full?"full":""}"><div class="tn">${full?icon("check","xs"):""}${esc(n)}</div>
          <div class="tctl"><span class="stepper lbl">Tekrar<button data-act="rep" data-k="${esc(k)}" data-d="-1" aria-label="Azalt">−</button><span class="num">${t.r||0}</span><button data-act="rep" data-k="${esc(k)}" data-d="1" aria-label="Artır">+</button></span>
          <button class="tog" data-act="sb" data-f="s1" data-k="${esc(k)}" aria-pressed="${!!t.s1}">${t.s1?icon("check","xs"):""}${esc(((s.sbAd||{})[sub.k]||[])[0]||"Soru B. 1")}</button>
          <button class="tog" data-act="sb" data-f="s2" data-k="${esc(k)}" aria-pressed="${!!t.s2}">${t.s2?icon("check","xs"):""}${esc(((s.sbAd||{})[sub.k]||[])[1]||"Soru B. 2")}</button></div>
          <input class="tnote" type="text" id="n-${esc(k)}" data-act="tnote" data-k="${esc(k)}" value="${esc(t.n||"")}" placeholder="Not ekle (ör. formülleri tekrar et)"></div>`; }).join(""); }
function pKonular(s){
  if(isMaarif(s)) return pKonularMaarif(s);
  const ex = S.ex, list = ex==="TYT" ? CURX().TYT : aytSubjects(s, S.aytAll), pct = examPct(s, ex);
  const head = A() ? "" : topbar(`<h1 class="ttl">Konu Takibi</h1>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    <div class="seg"><button data-act="ex" data-v="TYT" aria-pressed="${ex==="TYT"}">TYT</button><button data-act="ex" data-v="AYT" aria-pressed="${ex==="AYT"}">AYT</button></div>
    <div class="card"><div class="sech"><h3>${ex} ilerlemesi${ex==="AYT"?` · ${esc(s.alan)}`:""}</h3><b class="num">%${Math.round(pct*100)}</b></div><div class="bar" style="margin-top:10px"><i style="width:${pct*100}%"></i></div>
      <p class="muted small" style="margin:10px 0 0">Her konuda: tekrar sayısı, 1. ve 2. soru bankası. Üçü tamamlanan konu yeşil olur.</p>
      ${ex==="AYT"?`<div class="pills" style="margin-top:10px"><button class="tog" data-act="aytall" aria-pressed="${S.aytAll}">${S.aytAll?"Tüm AYT dersleri gösteriliyor":"Tüm AYT derslerini göster"}</button></div>`:""}</div>
    ${(cls=>list.map((sub,si)=>{ const p = subjPct(s,sub);
      return `<details class="${cls[si]}"><summary><span><span class="sn">${esc(sub.n)}</span><span class="sg">${esc(sub.g)}</span></span><div class="bar"><i style="width:${p*100}%;${p>=1?"background:var(--good)":""}"></i></div><span class="pct num">%${Math.round(p*100)}</span></summary>
      ${konuSatirlari(s, sub)}
      </details>`; }).join(""))(subColors(list))}
  </div>`;
}
function pCetele(s){
  const MX = isMaarif(s), ex = MX ? `${S.mx||1}. Aşama` : S.ex, list = MX ? maarifList(s, S.mx||1, S.aytAll) : ex==="TYT" ? CURX().TYT : aytSubjects(s, S.aytAll);
  const CLS = subColors(list); let max = 1, total = 0; list.forEach(sub=>sub.t.forEach(n=>{ const y=(s.topics[tkey(sub.k,n)]||{}).y||0; max=Math.max(max,y); total+=y; }));
  const head = A() ? "" : topbar(`<h1 class="ttl">Yanlış Çetelesi</h1>`, "", `<button class="iconbtn" data-act="go" data-v="daha" aria-label="Geri">${icon("back")}</button>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    ${MX ? asamaSeg() : `<div class="seg"><button data-act="ex" data-v="TYT" aria-pressed="${ex==="TYT"}">TYT</button><button data-act="ex" data-v="AYT" aria-pressed="${ex==="AYT"}">AYT</button></div>`}
    <div class="card"><div class="sech"><h3>${ex} toplam yanlış</h3><b class="num" style="color:var(--bad);font-size:22px">${total}</b></div><p class="muted small" style="margin:6px 0 0">Deneme ve testlerden sonra yanlış yaptığın konuları burada işaretle. En çok yanlış yapılan konular koçunun özetinde görünür.</p></div>
    ${list.map((sub,si)=>{ const tot = sub.t.reduce((a,n)=>a+((s.topics[tkey(sub.k,n)]||{}).y||0),0);
      return `<details class="${CLS[si]}" ${tot?"open":""}><summary><span><span class="sn">${esc(MX ? sub.ders+" · "+sub.n : sub.n)}</span><span class="sg">${esc(MX ? sub.ex : ex)}</span></span><span></span><span class="pct num" style="color:${tot?"var(--bad)":"var(--faint)"}">${tot}</span></summary>
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

/* Formdaki serbest alan yazısını SAY/EA/SÖZ'e çevir */
function alanTahmin(t){ const n = trLow(t); return /say/.test(n) ? "SAY" : /eşit|esit|\bea\b/.test(n) ? "EA" : /söz|soz/.test(n) ? "SÖZ" : ""; }
/* Ayarlar → Google Form bağlantısı: Apps Script kodunu hazırla */
let FORMKOD = null;
async function formKod(yenile){
  const out = $("#formKodOut"); if(out) out.innerHTML = `<p class="muted small">Hazırlanıyor…</p>`;
  try{ FORMKOD = await callFn("formAnahtari", {yenile:!!yenile}); }
  catch(e){ if(out) out.innerHTML = `<p class="err">Kod alınamadı: ${esc(e.message||e)}</p>`; return; }
  if(out) out.innerHTML = formKodHTML();
  if(yenile) toast("Yeni anahtar oluşturuldu. Formdaki kodu da güncellemelisin.");
}
function formKodHTML(){ if(!FORMKOD) return "";
  const kod = `// Zekacademy · Google Form → uygulama bildirimi
const ADRES = "${FORMKOD.url}";
const ANAHTAR = "${FORMKOD.anahtar}";

// Form gönderilince otomatik çalışır
function gonder(e) {
  yolla(e.response, false);
}

function yolla(r, sessiz) {
  var cevaplar = r.getItemResponses().map(function (x) {
    var v = x.getResponse();
    return { s: x.getItem().getTitle(), c: Array.isArray(v) ? v.join(", ") : String(v) };
  });
  var cevap = UrlFetchApp.fetch(ADRES, {
    method: "post", contentType: "application/json", muteHttpExceptions: true,
    payload: JSON.stringify({ anahtar: ANAHTAR, cevaplar: cevaplar, eposta: r.getRespondentEmail(),
      zaman: r.getTimestamp().toISOString(), yanitId: r.getId(), sessiz: sessiz })
  });
  return cevap.getResponseCode() + " " + cevap.getContentText();
}

// 1) Önce bunu bir kez çalıştır: form gönderilince gonder() otomatik çalışsın
function kur() {
  ScriptApp.getProjectTriggers().forEach(function (t) { ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger("gonder").forForm(FormApp.getActiveForm()).onFormSubmit().create();
}

// 2) Formdaki son 13 başvuruyu uygulamaya aktarır (bildirim göndermeden).
//    İki kez çalıştırılsa da aynı başvuru tekrar eklenmez. Sayıyı değiştirebilirsin.
function sonBasvurulariAktar() {
  var KAC = 13;
  var hepsi = FormApp.getActiveForm().getResponses();
  hepsi.slice(-KAC).forEach(function (r) {
    Logger.log(r.getTimestamp() + " → " + yolla(r, true));
    Utilities.sleep(300);
  });
}

// 3) Denemek için: uygulamaya örnek bir başvuru gönderir
function deneme() {
  var r = UrlFetchApp.fetch(ADRES, {
    method: "post", contentType: "application/json", muteHttpExceptions: true,
    payload: JSON.stringify({ anahtar: ANAHTAR, deneme: true, cevaplar: [
      { s: "İsim Soyisim", c: "Deneme Başvuru" }, { s: "Telefon Numaranız", c: "0555 000 00 00" },
      { s: "Sınava hangi alandan gireceksiniz?", c: "Sayısal" }, { s: "Öncelikle hangi hizmete başvurduğumuzu netleştirelim", c: "Birebir Koçluk" } ] })
  });
  Logger.log(r.getResponseCode() + " " + r.getContentText());
}`;
  return `<ol class="small" style="margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px">
      <li>Google Form'u bilgisayarda düzenleme modunda aç → sağ üstteki <b>⋮</b> → <b>Apps Script</b> (Komut dosyası düzenleyici).</li>
      <li>Açılan sayfadaki her şeyi sil, aşağıdaki kodu yapıştır, <b>Kaydet</b>'e bas.</li>
      <li>Üstteki işlev listesinden <b>kur</b>'u seç → <b>Çalıştır</b>. Google izin isteyecek: hesabını seç → <b>Gelişmiş</b> → <b>Git (güvenli değil)</b> → <b>İzin ver</b>. Bu senin kendi kodun olduğu için çıkan bir uyarı.</li>
      <li>Denemek için <b>deneme</b>'yi seç → <b>Çalıştır</b>. Birkaç saniye içinde Bildirimler'de yeşil "Yeni başvuru" görünür.</li>
      <li>İstersen <b>sonBasvurulariAktar</b>'ı seç → <b>Çalıştır</b>: formdaki son 13 başvuru, bildirim göndermeden Başvurular'a eklenir.</li></ol>
    <pre class="kod" id="formKodPre">${esc(kod)}</pre>
    <div class="pills"><button class="btn sm pri" data-act="kopyala" data-hedef="formKodPre">${icon("copy","xs")} Kodu kopyala</button><button class="btn sm" data-act="formkod" data-v2="yenile">Anahtarı yenile</button></div>
    <p class="faint small" style="margin:0">Kodun içindeki anahtar gizlidir; kimseyle paylaşma. Paylaşırsan “Anahtarı yenile” de ve yeni kodu forma yapıştır.</p>`; }

/* ---------- Başvuru süreci (Google Form → WhatsApp adımları) ---------- */
const DEF_BMESAJ = {
  onay: "🎯 *Koçluk Başvurun Onaylandı, {Ad}!*\nSeninle derece odaklı, planlı bir yolculuğa başlıyoruz.🚀 ✨\n\nHaftalık çalışma programların *YKS Türkiye 8. si Zekeriya Ürünlü tarafından hazırlanacak.*\nSüreç boyunca tüm sorularını yanıtlayacak, her adımda yanında olacağım. 💬\n\n📌 *Süreçte neler var?*\n✅ Haftalık bire bir online görüşme 📅\n✅ Sınırsız WhatsApp desteği (soru, motivasyon, planlama, rehberlik) 📲 💡\n✅ Profesyonel Excel tabanlı online takip sistemi (her gün) 📊 🖥️\n✅ Türkiye 8. si, 26.sı, 67. si, 95. si ve 101. si olmuş Türkiye YKS derece rekortmeninin özel çalışma stratejileri 🎓 🔥\n✅ Tamamen kişiye özel planlama ve destek 📝 🎯\n\n*Koçluk süreci, ödemenin ardından resmen başlayacaktır.* 💳 ⏳\nÖdeme tamamlandıktan sonra ilk görüşme ve süreç takvimi seninle paylaşılacak. 📅 ✉️\n\nHedef net, yol planlı.\nHazırsan birlikte başlıyoruz! 💪 🚀",
  kontenjan: "📌 Kontenjan oldukça sınırlı olduğu için *gün içerisinde dönüş yapmanı* bekliyorum.  Hızlı olan kazanır. ⏳",
  iban: "TR40 0015 7000 0000 0158 6692 82",
  alici: "İNCİ AKDAĞ ÜRÜNLÜ",
  odemeNot: "*Not:* Ödemeyi yaptıktan sonra sürecimiz başlayacak inşallah🌹💐\n*Önemli:* Ödemelerin karışmaması için dekont iletmeniz rica olunur🌹💐",
};
const bmesaj = () => ({...DEF_BMESAJ, ...(S.settings.bmesaj||{})});
const BDURUM = [["yeni","Yeni"],["mesaj","Mesaj gönderildi"],["evet","Evet dedi"],["odeme","Ödeme bilgisi gitti"],["ogrenci","Öğrenci oldu"],["hayir","Vazgeçti"]];
const bdLabel = k => (BDURUM.find(x=>x[0]===k)||BDURUM[0])[1];
const ilkAd = n => { const a = String(n||"").trim().split(/\s+/)[0] || ""; return a ? a.charAt(0).toLocaleUpperCase("tr") + a.slice(1).toLocaleLowerCase("tr") : ""; };
const adSoyad = n => String(n||"").trim().split(/\s+/).filter(Boolean).map(w=>w.charAt(0).toLocaleUpperCase("tr")+w.slice(1).toLocaleLowerCase("tr")).join(" ");
function waNo(t){ let d = String(t||"").replace(/\D/g,""); if(d.startsWith("0")) d = "9"+d; else if(d.length===10 && d.startsWith("5")) d = "90"+d; return d; }
const waLink = (tel, text) => `https://wa.me/${waNo(tel)}?text=${encodeURIComponent(text)}`;
const doldur = (t, n) => String(t).replace(/\{Ad\}/g, ilkAd(n.name)).replace(/\{AdSoyad\}/g, adSoyad(n.name));
function bSet(id, fn){ const n = S.notifs.get(id); if(!n) return; fn(n); n.adim = {...(n.adim||{})}; S.notifs.set(id, n); persistDoc("notifs", id, 200); }
/* Fotoğraf: settings/foto (Ayarlar'dan yüklenir) */
let FOTO = undefined;
function fotoYukle(){ if(FOTO !== undefined) return Promise.resolve(FOTO);
  return new Promise(res=>{ const u = onSnapshot(doc(fdb,"settings","foto"), sn=>{ FOTO = sn.exists() ? (sn.data().data || null) : null; try{ u(); }catch(_){} res(FOTO); }, ()=>{ FOTO = null; res(null); }); }); }
async function fotoKaydet(file){
  const img = await new Promise((res,rej)=>{ const i = new Image(); i.onload=()=>res(i); i.onerror=rej; i.src = URL.createObjectURL(file); });
  const max = 1080, k = Math.min(1, max/Math.max(img.width, img.height)), c = document.createElement("canvas");
  c.width = Math.round(img.width*k); c.height = Math.round(img.height*k); c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
  let q = .85, data = c.toDataURL("image/jpeg", q); while(data.length > 700000 && q > .4){ q -= .1; data = c.toDataURL("image/jpeg", q); }
  await setDoc(doc(fdb,"settings","foto"), {data, at:nowISO()}); FOTO = data; }
async function fotoDosya(){ const d = await fotoYukle(); if(!d) return null; const b = await (await fetch(d)).blob(); return new File([b], "zekacademy.jpg", {type:"image/jpeg"}); }
function rehberKart(n){ const ad = `${adSoyad(n.name)} Koçluk`, tel = "+"+waNo(n.tel);
  const v = ["BEGIN:VCARD","VERSION:3.0",`N:Koçluk;${adSoyad(n.name)};;;`,`FN:${ad}`,`TEL;TYPE=CELL:${tel}`, n.eposta?`EMAIL:${n.eposta}`:"", "NOTE:Zekacademy başvurusu","END:VCARD"].filter(Boolean).join("\r\n");
  return new File([v], `${ad}.vcf`, {type:"text/vcard"}); }
async function rehbereKaydet(id){ const n = S.notifs.get(id); if(!n) return; const f = rehberKart(n);
  try{ if(navigator.canShare && navigator.canShare({files:[f]}) && /android|iphone|ipad/i.test(navigator.userAgent)){ await navigator.share({files:[f], title:f.name}); } else throw 0; }
  catch(e){ if(e && e.name==="AbortError") return; const a = document.createElement("a"); a.href = URL.createObjectURL(f); a.download = f.name; document.body.appendChild(a); a.click(); a.remove(); }
  bSet(id, x=>{ x.adim = {...(x.adim||{}), rehber:nowISO()}; }); render(); toast("Kişi kartı açıldı: “Kaydet”e dokun"); }
async function onayGonder(id){ const n = S.notifs.get(id); if(!n) return; const text = doldur(bmesaj().onay, n);
  try{ await navigator.clipboard.writeText(text); }catch(_){}
  const f = await fotoDosya().catch(()=>null);
  const mobil = /android|iphone|ipad/i.test(navigator.userAgent);
  if(f && mobil && navigator.canShare && navigator.canShare({files:[f], text})){
    try{ await navigator.share({files:[f], text}); }catch(e){ if(e && e.name==="AbortError") return; }
  } else {
    let panoda = false;
    if(f && window.ClipboardItem && navigator.clipboard && navigator.clipboard.write){ try{ /* bilgisayarda: fotoğrafı panoya al, WhatsApp'ta yapıştır */
      const bmp = await createImageBitmap(f), c = document.createElement("canvas"); c.width = bmp.width; c.height = bmp.height; c.getContext("2d").drawImage(bmp,0,0);
      const png = await new Promise(r=>c.toBlob(r,"image/png")); await navigator.clipboard.write([new ClipboardItem({"image/png": png})]); panoda = true; }catch(_){} }
    window.open(waLink(n.tel, text), "_blank");
    toast(!f ? "Fotoğraf yüklenmemiş; sadece mesaj açıldı (Ayarlar → Başvuru mesajları)" : panoda ? "Mesaj hazır. Fotoğraf panoda: WhatsApp'ta önce Ctrl+V ile yapıştır" : "Mesaj açıldı; fotoğrafı ayrıca eklemelisin"); }
  bSet(id, x=>{ x.adim = {...(x.adim||{}), onay:nowISO()}; if(!x.durum || x.durum==="yeni") x.durum = "mesaj"; }); render(); }
function metinGonder(id, ne){ const n = S.notifs.get(id); if(!n) return; const m = bmesaj();
  const text = ne==="kontenjan" ? doldur(m.kontenjan, n) : ne==="iban" ? m.iban : doldur(`${m.iban}\n${m.alici}\n\n${m.odemeNot}`, n);
  window.open(waLink(n.tel, text), "_blank");
  bSet(id, x=>{ x.adim = {...(x.adim||{}), [ne==="iban"?"odeme":ne]:nowISO()}; if(ne!=="kontenjan" && ["yeni","mesaj","evet"].includes(x.durum||"yeni")) x.durum = "odeme"; else if(ne==="kontenjan" && (!x.durum || x.durum==="yeni")) x.durum = "mesaj"; }); render(); }
function cBasvuru(){
  const all = [...S.notifs.entries()].filter(([,n])=>n.type==="basvuru").sort((a,b)=>a[1].at<b[1].at?1:-1);
  const tab = S.btab || "aktif", grp = {aktif:x=>!["ogrenci","hayir"].includes(x.durum||"yeni"), ogrenci:x=>x.durum==="ogrenci", hayir:x=>x.durum==="hayir"};
  const list = all.filter(([,n])=>grp[tab](n)), cnt = k => all.filter(([,n])=>grp[k](n)).length;
  const step = (done, no, title, body, btns) => `<div class="bstep ${done?"done":""}"><span class="bno">${done?icon("check","xs"):no}</span><div style="min-width:0;flex:1"><b>${title}</b>${body?`<div class="small muted">${body}</div>`:""}<div class="pills" style="margin-top:6px">${btns}</div></div></div>`;
  const card = ([id,n]) => { const a = n.adim||{}, d = n.durum||"yeni", tel = n.tel;
    return `<div class="bcard b-${d}"><div class="bhead"><span class="av">${esc(initials(n.name||"?"))}</span><div style="min-width:0;flex:1"><b>${esc(adSoyad(n.name)||"İsimsiz")}</b>${n.deneme?` <span class="pill">deneme</span>`:""}<div class="small muted">${esc([n.hizmet, n.alan, tel].filter(Boolean).join(" · "))} · ${ago(n.at)}</div></div><span class="bdur">${bdLabel(d)}</span></div>
      ${d==="ogrenci"||d==="hayir" ? "" : `<div class="bsteps">
        ${step(a.rehber, 1, "Rehbere kaydet", `“${esc(adSoyad(n.name))} Koçluk” olarak`, `<button class="btn sm" data-act="brehber" data-id="${id}" ${tel?"":"disabled"}>${icon("user","xs")} Kişi kartını aç</button>`)}
        ${step(a.onay, 2, "Onay mesajı", "Fotoğraf + “Koçluk Başvurun Onaylandı” mesajı", `<button class="btn sm ${a.onay?"":"pri"}" data-act="bonay" data-id="${id}" ${tel?"":"disabled"}>WhatsApp'ta gönder</button>`)}
        ${step(a.kontenjan, 3, "Kontenjan mesajı", "", `<button class="btn sm ${a.onay&&!a.kontenjan?"pri":""}" data-act="bmetin" data-v="kontenjan" data-id="${id}" ${tel?"":"disabled"}>WhatsApp'ta gönder</button>`)}
        ${step(d==="evet"||d==="odeme", 4, "Anket", "Anketi WhatsApp'tan sen ekle, cevabı burada işaretle", `<button class="btn sm ${d==="evet"||d==="odeme"?"pri":""}" data-act="bdurum" data-v="evet" data-id="${id}">Evet dedi</button><button class="btn sm" data-act="bdurum" data-v="hayir" data-id="${id}">Hayır dedi</button>`)}
        ${step(a.odeme, 5, "Ödeme bilgisi", "IBAN, alıcı adı ve dekont notu", `<button class="btn sm ${d==="evet"?"pri":""}" data-act="bmetin" data-v="odeme" data-id="${id}" ${tel?"":"disabled"}>WhatsApp'ta gönder</button><button class="btn sm" data-act="bmetin" data-v="iban" data-id="${id}" ${tel?"":"disabled"}>Sadece IBAN</button>`)}
        ${step(false, 6, "Ödeme geldi", "Öğrenci hesabını aç; ödeme takibi bugünden başlar", `<button class="btn sm ${d==="odeme"?"pri":""}" data-act="sheet" data-v="ogrenci" data-bid="${id}" data-name="${esc(adSoyad(n.name))}" data-alan="${esc(n.alan||"")}">${icon("plus","xs")} Öğrenci hesabı aç</button><button class="btn sm" data-act="sheet" data-v="gplan" data-bid="${id}" data-ad="${esc(adSoyad(n.name))}">${icon("clock","xs")} İlk görüşmeyi planla</button>`)}
      </div>`}
      <details class="bmore"><summary>Form cevapları ve diğer</summary>${(n.cevaplar||[]).length?`<dl>${n.cevaplar.map(x=>`<dt>${esc(x.s)}</dt><dd>${esc(x.c||"—")}</dd>`).join("")}</dl>`:""}
        <div class="pills" style="margin-top:8px">${d==="hayir"||d==="ogrenci"?`<button class="btn sm" data-act="bdurum" data-v="yeni" data-id="${id}">Aktife geri al</button>`:`<button class="btn sm" data-act="bdurum" data-v="hayir" data-id="${id}">Vazgeçti</button>`}<button class="btn sm danger" data-act="nsil" data-id="${id}">Başvuruyu sil</button></div></details></div>`; };
  return `${topbar(`<h1 class="ttl">Başvurular</h1>`, `<button class="iconbtn" data-act="sheet" data-v="bdeneme" aria-label="Deneme başvurusu">${icon("plus")}</button>`, `<button class="iconbtn" data-act="go" data-v="daha" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page wide">
    ${(b=>b.length?`<p class="muted small" style="margin:0">Bu ay ${b.filter(n=>String(n.at).slice(0,7)===today().slice(0,7)).length} başvuru · toplam ${b.length} başvurudan ${b.filter(n=>n.durum==="ogrenci").length} öğrenci (%${Math.round(b.filter(n=>n.durum==="ogrenci").length/b.length*100)})</p>`:"")([...S.notifs.values()].filter(n=>n.type==="basvuru" && !n.deneme))}
    <div class="seg">${[["aktif","Süreçte"],["ogrenci","Öğrenci oldu"],["hayir","Vazgeçti"]].map(([k,l])=>`<button data-act="btab" data-v="${k}" aria-pressed="${tab===k}">${l} <span class="num faint">${cnt(k)}</span></button>`).join("")}</div>
    ${list.length ? list.map(card).join("") : `<div class="card"><div class="empty">${tab==="aktif"?"Süreçte başvuru yok. Google Form doldurulunca burada görünür. Sağ üstteki + ile kendine deneme başvurusu oluşturabilirsin.":"Burada henüz kimse yok."}</div></div>`}
    <p class="faint small" style="text-align:center">Mesajları Ayarlar → Başvuru mesajları'ndan değiştirebilirsin. {Ad} yazan yere öğrencinin adı gelir.</p>
  </div>`;
}

/* ---------- Görüşme planlayıcı (koça özel; gorusmeler/{id} + coachNotes/{uid}.duzen) ---------- */
const SURE_SEANS = 15, SURE_ILK = 30;
const hmTo = t => { const [h,m] = String(t||"0:0").split(":").map(Number); return h*60+(m||0); };
const toHm = m => String(Math.floor(m/60)).padStart(2,"0")+":"+String(m%60).padStart(2,"0");
const duzenOf = id => (S.cnotes.get(id)||{}).duzen || null;
/* Seans günü: elle seçildiyse o gün, yoksa öğrencinin program döngüsünün başladığı gün (Yeni görüşme ile kayarsa seans da kayar) */
const isWA = x => !!x && x.paket==="whatsapp";
function seansGunu(sid, d){ const z = duzenOf(sid), x = S.students.get(sid);
  if(isWA(x)){ if(z && z.gun!=null && z.gun!=="") return z.gun===dIdx(d); return pStart(x, d)===d; } /* WhatsApp paketi: döngü gününde haftalık rapor, saat yok */
  if(!z || !z.saat) return false; if(z.gun!=null && z.gun!=="") return z.gun===dIdx(d);
  return !!x && pStart(x, d)===d; }
function sanalKayit(sid, d){ const x = S.students.get(sid), z = duzenOf(sid) || {};
  return isWA(x) ? {sid, ad:x?.name||"", tarih:d, hafta:monday(d), saat:null, sure:0, tur:"rapor", durum:"planli", kaynak:"duzen"}
    : {sid, ad:x?.name||"", tarih:d, hafta:monday(d), saat:z.saat, sure:z.sure||SURE_SEANS, tur:"seans", durum:"planli", kaynak:"duzen"}; }
const saatSira = g => g.saat ? hmTo(g.saat) : 99999;
function otoGun(sid){ const x = S.students.get(sid); return x ? dIdx(curStart(x)) : 0; }
/* Bir günün görüşmeleri: kayıtlı olanlar + haftalık düzenden gelenler (o hafta için ayrıca kaydı yoksa) */
function gunGorusme(d){
  const real = [...S.gorus.entries()].filter(([,g])=>g.tarih===d).map(([id,g])=>({...g, id}));
  const w = monday(d), virt = [];
  S.students.forEach((x,sid)=>{ const z = duzenOf(sid); if(!seansGunu(sid, d) || (z && z.bas && d < z.bas)) return;
    if([...S.gorus.values()].some(g=>g.sid===sid && g.kaynak==="duzen" && (g.hafta || monday(g.tarih))===w)) return;
    virt.push({id:"v:"+sid+":"+d, sanal:true, ...sanalKayit(sid, d)}); });
  const all = [...real, ...virt].sort((a,b)=>saatSira(a)-saatSira(b) || (a.ad||"").localeCompare(b.ad||"","tr"));
  const akt = all.filter(g=>g.durum!=="iptal" && g.tur!=="rapor");
  akt.forEach(g=>{ const a = hmTo(g.saat), b = a+(g.sure||15); g.cakisma = akt.some(h=>h!==g && hmTo(h.saat) < b && hmTo(h.saat)+(h.sure||15) > a); });
  return all; }
function gorusAd(g){ return g.sid && S.students.has(g.sid) ? S.students.get(g.sid).name : (g.ad || "İsimsiz"); }
/* Sanal (düzenden gelen) görüşmeyi gerçek kayda çevirir */
function gorusGercek(id){ if(!id.startsWith("v:")) return id; const [,sid,d] = id.split(":"); const z = duzenOf(sid) || {};
  const var_ = [...S.gorus.entries()].find(([,g])=>g.sid===sid && g.kaynak==="duzen" && (g.hafta || monday(g.tarih))===monday(d)); if(var_) return var_[0];
  const nid = uid(); S.gorus.set(nid, sanalKayit(sid, d)); persistDoc("gorusmeler", nid, 0); return nid; }
function gorusSet(id, fn){ const rid = gorusGercek(id); const g = {...S.gorus.get(rid)}; fn(g); S.gorus.set(rid, g); persistDoc("gorusmeler", rid, 200); return rid; }
function cGorusme(){
  const t = today(), d = S.gday || t, w = monday(d), days = [0,1,2,3,4,5,6].map(i=>addDays(w,i));
  const tum = gunGorusme(d), list = tum.filter(g=>g.tur!=="rapor"), rap = tum.filter(g=>g.tur==="rapor"), akt = list.filter(g=>g.durum!=="iptal"), top = akt.reduce((a,g)=>a+(g.sure||15),0);
  const duzensiz = sortedStudents().filter(([id,x])=>!isWA(x) && !duzenOf(id)?.saat).length;
  const rows = []; let son = null;
  list.forEach(g=>{ const a = hmTo(g.saat); if(son!=null && g.durum!=="iptal" && a - son >= 15) rows.push(`<div class="gbos">Boş · ${toHm(son)} – ${g.saat} <span>${a-son} dk</span></div>`);
    if(g.durum!=="iptal") son = Math.max(son??0, a+(g.sure||15));
    const ilk = g.tur==="ilk", dur = g.durum;
    rows.push(`<div class="grow g-${dur} ${g.cakisma?"g-cak":""} ${ilk?"g-ilk":""}"><div class="gsaat"><b class="num">${g.saat}</b><span class="num">${toHm(a+(g.sure||15))}</span></div>
      <div style="min-width:0;flex:1;cursor:pointer" data-act="gmod" data-v="${g.id}" role="button" tabindex="0"><b>${esc(gorusAd(g))}</b><div class="gmeta"><span class="gtag">${ilk?"İlk görüşme":"Seans"} · ${g.sure||15} dk</span>${g.sanal||g.kaynak==="duzen"?`<span class="faint">her hafta</span>`:""}${g.cakisma?`<span class="gwarn">Çakışıyor</span>`:""}${dur==="yapildi"?`<span class="gok">Yapıldı</span>`:dur==="gelmedi"?`<span class="gwarn">Gelmedi</span>`:dur==="iptal"?`<span class="faint">İptal</span>`:""}</div>${g.not?`<div class="small muted" style="margin-top:4px">${esc(g.not)}</div>`:""}</div>
      <div class="gact"><button class="iconbtn sm ${dur==="yapildi"?"on":""}" data-act="gdurum" data-id="${g.id}" data-v="${dur==="yapildi"?"planli":"yapildi"}" aria-label="Yapıldı">${icon("check","sm")}</button><button class="iconbtn sm" data-act="sheet" data-v="gplan" data-id="${g.id}" aria-label="Düzenle">${icon("edit","sm")}</button></div></div>`); });
  return `${topbar(`<h1 class="ttl">Görüşmeler</h1>`, `<button class="iconbtn" data-act="sheet" data-v="gplan" data-d="${d}" aria-label="Görüşme ekle">${icon("plus")}</button>`)}
  <div class="page wide">
    <div class="wknav"><button class="iconbtn" data-act="gwk" data-d="-7" aria-label="Önceki hafta">${icon("back","sm")}</button><b>${shortDate(w)} – ${shortDate(addDays(w,6))}${w===monday(t)?` <span class="pill ac">Bu hafta</span>`:""}</b><button class="iconbtn" data-act="gwk" data-d="7" aria-label="Sonraki hafta">${icon("chev","sm")}</button></div>
    <div class="gdays">${days.map(x=>{ const l = gunGorusme(x).filter(g=>g.durum!=="iptal"), c = l.some(g=>g.cakisma);
      return `<button class="gday ${x===t?"today":""}" data-act="gday" data-v="${x}" aria-pressed="${x===d}"><span>${GUNK[dIdx(x)]}</span><b class="num">${dNum(x)}</b><em class="num">${l.length||""}</em>${c?`<i></i>`:""}</button>`; }).join("")}</div>
    <div class="card"><div class="sech"><h3>${GUN[dIdx(d)]}, ${trDate(d)}</h3><span class="faint small">${akt.length?`${akt.length} görüşme · ${fmtMin(top)}${akt.length?` · ${akt[0].saat}–${toHm(Math.max(...akt.map(g=>hmTo(g.saat)+(g.sure||15))))}`:""}`:"Görüşme yok"}</span></div>
      <div class="glist">${rows.join("") || `<div class="empty">Bu gün için görüşme yok. Sağ üstteki + ile ekleyebilir ya da öğrencilere haftalık düzen verebilirsin.</div>`}</div></div>
    ${rap.length?`<div class="card"><div class="sech"><h3>${icon("chat","sm")} Haftalık raporlar · WhatsApp</h3><span class="faint small">${rap.filter(g=>g.durum==="yapildi").length}/${rap.length} geldi</span></div>
      <div class="glist">${rap.map(g=>`<div class="grow g-${g.durum} rap"><div style="min-width:0;flex:1;cursor:pointer" data-act="gmod" data-v="${g.id}" role="button" tabindex="0"><b>${esc(gorusAd(g))}</b><div class="gmeta"><span class="gtag">Rapor günü</span>${g.durum==="yapildi"?`<span class="gok">Rapor geldi</span>`:g.durum==="gelmedi"?`<span class="gwarn">Gelmedi</span>`:`<span class="faint">Bekleniyor</span>`}</div>${g.not?`<div class="small muted" style="margin-top:4px">${esc(g.not)}</div>`:""}</div>
        <div class="gact"><button class="iconbtn sm ${g.durum==="yapildi"?"on":""}" data-act="gdurum" data-id="${g.id}" data-v="${g.durum==="yapildi"?"planli":"yapildi"}" aria-label="Rapor geldi">${icon("check","sm")}</button>${waBtn(g.sid,true).replace("WhatsApp","")}</div></div>`).join("")}</div></div>`:""}
    <div class="card"><div class="sech"><h3>Haftalık düzen</h3><button class="btn sm ${duzensiz?"pri":""}" data-act="sheet" data-v="duzen">Düzenle</button></div>
      <p class="muted small" style="margin:6px 0 0">Seans günü öğrencinin program döngüsünden otomatik gelir (son görüşme günü); sen sadece saati girersin. ${duzensiz?`<b>${duzensiz} öğrencinin saati girilmedi.</b>`:"Tüm öğrencilerin saati girildi."}</p></div>
    <p class="faint small" style="text-align:center">Seans ${SURE_SEANS} dk, ilk görüşme ${SURE_ILK} dk. Bu sayfayı sadece sen görürsün.</p>
  </div>`;
}

/* ---------- Öğrenciye WhatsApp ---------- */
const DEF_WMESAJ = ["Selam {Ad}, nasıl gidiyor hayat, nasılsın? 😊", "{Ad}, bugünkü görüşmemiz saat {Saat}'te. Görüşürüz! 👋", "{Ad}, yarınki görüşmemiz saat {Saat}'te. Görüşmeden önce programını işaretlemeyi unutma 📝", "{Ad}, bu haftanın programını uygulamada işaretlemeyi unutma 📝", "{Ad}, haftalık raporunu bekliyorum 📋 Gönderince yeni haftanın programını hazırlıyorum.", "Tebrikler {Ad}! Bu hafta harika gidiyorsun, aynen devam 👏"];
const wmesajlar = () => (S.settings.wmesaj && S.settings.wmesaj.length) ? S.settings.wmesaj : DEF_WMESAJ;
/* Öğrencinin bugünden itibaren ilk planlı görüşmesi (14 gün içinde) */
function sonrakiGorusme(sid){ const t = today(); for(let i=0;i<14;i++){ const d = addDays(t,i); const g = gunGorusme(d).find(x=>x.sid===sid && x.tur!=="rapor" && x.durum==="planli" && (i>0 || hmTo(x.saat)+(x.sure||15) > nowMin())); if(g) return g; } return null; }
function waDoldur(t, sid){ const x = S.students.get(sid), g = sonrakiGorusme(sid);
  return String(t).replace(/\{Ad\}/g, ilkAd(x?.name)).replace(/\{AdSoyad\}/g, adSoyad(x?.name)).replace(/\{Saat\}/g, g ? g.saat : "__:__").replace(/\{Gün\}/g, g ? GUN[dIdx(g.tarih)] : ""); }
const waBtn = (sid, sm) => `<button class="btn ${sm?"sm":""} wa" data-act="sheet" data-v="wa" data-sid="${sid}">${icon("chat","xs")} WhatsApp</button>`;

function waAc(sid, text){ const x = S.students.get(sid), inp = $("#wa-tel"), tel = (inp && inp.value.trim()) || x?.tel || "";
  if(waNo(tel).length < 11){ sheetErr("Önce öğrencinin telefonunu yaz."); if(inp) inp.focus(); return; }
  if(x && tel !== x.tel){ x.tel = tel; persistDoc("students", sid, 0); }
  window.open(waLink(tel, text), "_blank"); }
/* ---------- Yedek ---------- */
let YEDEK = undefined;
function yedekBilgi(){ if(YEDEK !== undefined) return Promise.resolve(YEDEK);
  return new Promise(res=>{ const u = onSnapshot(doc(fdb,"settings","yedek"), sn=>{ YEDEK = sn.exists() ? sn.data() : null; try{ u(); }catch(_){} res(YEDEK); }, ()=>{ YEDEK = null; res(null); }); }); }
function yedekIndir(){
  const m = x => Object.fromEntries([...x.entries()]);
  const veri = { tarih:nowISO(), students:m(S.students), coachNotes:m(S.cnotes), notifs:m(S.notifs), gorusmeler:m(S.gorus), settings:{main:S.settings} };
  const f = new File([JSON.stringify(veri, null, 1)], `zekacademy-yedek-${today()}.json`, {type:"application/json"});
  const a = document.createElement("a"); a.href = URL.createObjectURL(f); a.download = f.name; document.body.appendChild(a); a.click(); a.remove();
  toast(`Yedek indirildi · ${S.students.size} öğrenci`); }
/* ---------- Günün özeti (sadece uygulama içinde) ---------- */
function gununOzeti(){
  const t = today(), dun = addDays(t,-1), items = [];
  const gt = gunGorusme(t).filter(g=>g.durum!=="iptal"), gl = gt.filter(g=>g.tur!=="rapor"), rp = gt.filter(g=>g.tur==="rapor"), sira = gl.find(g=>g.durum==="planli" && hmTo(g.saat)+(g.sure||15) > nowMin());
  items.push({ic:"clock", k:gl.length?"":"bos", t: gl.length ? `<b>${gl.length} görüşme</b>${sira?` · sıradaki ${sira.saat} ${esc(gorusAd(sira))}`:" · hepsi bitti"}` : "Bugün görüşme yok", act:`data-act="gday" data-v="${t}"`});
  if(rp.length) items.push({ic:"chat", k:"", t:(n=>`<b>${rp.length}</b> haftalık rapor günü · ${n===rp.length?"hepsi geldi":n?`${n} geldi, ${rp.length-n} bekleniyor`:"bekleniyor"}`)(rp.filter(g=>g.durum==="yapildi").length), act:`data-act="gday" data-v="${t}"`});
  let bugun = 0, gecik = 0; S.students.forEach((_,id)=>{ const d = odemeDurum(id); if(d.d===t && d.k==="turuncu") bugun++; if(d.k==="kirmizi"||d.k==="pembe") gecik++; });
  if(bugun || gecik) items.push({ic:"cal", k:gecik?"kotu":"", t:[bugun?`<b>${bugun}</b> ödeme günü bugün`:"", gecik?`<b>${gecik}</b> geciken ödeme`:""].filter(Boolean).join(" · "), act:`data-act="go" data-v="odeme"`});
  const yb = [...S.notifs.values()].filter(n=>n.type==="basvuru" && (n.durum||"yeni")==="yeni").length;
  if(yb) items.push({ic:"user", k:"iyi", t:`<b>${yb}</b> yeni başvuru bekliyor`, act:`data-act="go" data-v="basvuru"`});
  const isaret = [], sure = [];
  S.students.forEach((x,id)=>{ const l = dayTasks(x,dun); if(l.length && !l.some(z=>z.done)) isaret.push(x.name); if(l.length && !minutes(x,dun)) sure.push(x.name); });
  if(isaret.length) items.push({ic:"check", k:"uyari", t:`Dün görevlerini işaretlemeyen <b>${isaret.length}</b>: ${esc(isaret.slice(0,4).map(ilkAd).join(", "))}${isaret.length>4?"…":""}`, act:`data-act="go" data-v="ogrenciler"`});
  if(sure.length) items.push({ic:"timer", k:"uyari", t:`Dün çalışma süresi girmeyen <b>${sure.length}</b>: ${esc(sure.slice(0,4).map(ilkAd).join(", "))}${sure.length>4?"…":""}`, act:`data-act="go" data-v="ogrenciler"`});
  return `<div class="card gozet"><div class="sech"><h3>${icon("sun","sm")} Günün özeti</h3><span class="faint small">${longToday()}</span></div>
    <div class="gozl">${items.map(x=>`<button class="gozi ${x.k}" ${x.act}><span class="gzi">${icon(x.ic,"sm")}</span><span class="gzt">${x.t}</span>${icon("chev","sm")}</button>`).join("")}</div></div>`;
}

/* ---------- Görüşme modu: görüşmeye dokununca öğrencinin tek sayfalık özeti ---------- */
function cGmod(){
  const g = S.gsel && (S.gsel.startsWith("v:") ? gunGorusme(S.gsel.split(":")[2]).find(x=>x.id===S.gsel) : (S.gorus.get(S.gsel) ? {...S.gorus.get(S.gsel), id:S.gsel} : null));
  if(!g){ S.view = "gorusme"; return cGorusme(); }
  const sid = g.sid, s = sid && S.students.get(sid), back = `<button class="iconbtn" data-act="go" data-v="gorusme" aria-label="Geri">${icon("back")}</button>`;
  const R = g.tur==="rapor";
  const ust = `<div class="card gmhead"><div><div class="gmsaat num">${R?"Haftalık rapor":`${g.saat} – ${toHm(hmTo(g.saat)+(g.sure||15))}`}</div><div class="small muted">${GUN[dIdx(g.tarih)]}, ${trDate(g.tarih)} · ${R?"WhatsApp koçluğu":`${g.tur==="ilk"?"İlk görüşme":"Seans"} · ${g.sure||15} dk`}${g.durum==="yapildi"?` · <b style="color:var(--good)">${R?"Rapor geldi":"Yapıldı"}</b>`:g.durum==="gelmedi"?` · <b style="color:var(--bad)">Gelmedi</b>`:""}</div></div>
      <div class="pills">${s?waBtn(sid,true):""}<button class="btn sm" data-act="sheet" data-v="gplan" data-id="${g.id}">${icon("edit","xs")} Düzenle</button></div></div>`;
  if(!s) return `${topbar(`<h1 class="ttl">${esc(gorusAd(g))}</h1>`, "", back)}<div class="page wide">${ust}
    <div class="card"><p class="muted" style="margin:0">Bu kişi henüz öğrenci değil (ilk görüşme). Görüşmeden sonra Başvurular'dan öğrenci hesabını açabilirsin.</p>
    <div class="pills" style="margin-top:10px"><button class="btn sm pri" data-act="gdurum" data-id="${g.id}" data-v="yapildi">${icon("check","xs")} Yapıldı</button><button class="btn sm" data-act="gdurum" data-id="${g.id}" data-v="gelmedi">Gelmedi</button>${g.bid?`<button class="btn sm" data-act="go" data-v="basvuru">Başvuruya git</button>`:""}</div></div></div>`;
  const yeniHafta = pStart(s, g.tarih)===g.tarih, w = yeniHafta ? pStart(s, addDays(g.tarih,-1)) : pStart(s, g.tarih);
  const ws = weekStats(s, w), gl = weekGoals(s, w), days = pDays(s, w), mins = days.map(d=>minutes(s,d)), mx = Math.max(60, ...mins), m = coachMetrics(s);
  const den = [...exams(s,"TYT").map(d=>["TYT",d,tytTotal(d)]), ...exams(s,"AYT").map(d=>["AYT",d,aytTotal(d)])].sort((a,b)=>a[1].tarih<b[1].tarih?1:-1).slice(0,4);
  return `${topbar(`<div style="min-width:0;flex:1"><h1 class="ttl" style="font-size:20px">${esc(s.name)}</h1><div class="faint small">${esc(s.alan)} · ${esc(s.sinif)}</div></div>`, `<button class="iconbtn" data-act="open" data-id="${sid}" aria-label="Öğrenci sayfası">${icon("user")}</button>`, back)}
  <div class="page wide">${ust}
    ${m.flags.length?`<div class="pills">${m.flags.map(f=>`<span class="pill ${f[0]}">${esc(f[1])}</span>`).join("")}</div>`:""}
    <div class="kpis">
      ${tile("t-g","target",ws.pct==null?"—":"%"+Math.round(ws.pct*100),`Görev uyumu · ${ws.done}/${ws.all}`)}
      ${tile("t-a","clock",fmtMin(ws.min),"Toplam çalışma")}
      ${tile("t-w","trend",fmt(m.lt),m.dlt!=null?`Son TYT · ${m.dlt>=0?"+":""}${fmt(m.dlt)}`:"Son TYT")}
      ${tile("t-r","flame",m.streak+" gün","Seri")}
    </div>
    <div class="card"><div class="sech"><h3>${yeniHafta?"Geçen hafta":"Bu hafta"} · ${shortDate(w)} – ${shortDate(addDays(w, days.length-1))}</h3></div>
      <div class="bars7">${days.map((d,i)=>`<div class="b7 ${d===today()?"today":""}"><em class="num">${mins[i]?fmtMin(mins[i]):""}</em><i style="height:${mins[i]/mx*100}%"></i><span>${GUNK[dIdx(d)]}</span></div>`).join("")}</div></div>
    <div class="card"><div class="sech"><h3>Hedef konular</h3><span class="faint small">${gl.list.length?`${gl.done}/${gl.list.length} bitti`:"Hedef girilmemiş"}</span></div>
      ${gl.list.length?`<div style="margin-top:6px">${gl.list.map(d=>`<div class="row"><span class="ri" style="${gl.h[d].done?"background:var(--goods);color:var(--good)":""}">${icon(gl.h[d].done?"check":"target","sm")}</span><div style="min-width:0"><div class="rt">${esc(d)}</div><div class="rs">${esc(gl.h[d].konu)}</div></div></div>`).join("")}</div>`:""}</div>
    ${den.length?`<div class="card"><h3>Son denemeler</h3><div style="margin-top:4px">${den.map(([t,d,n])=>`<div class="row"><span class="ri">${icon("chart","sm")}</span><div style="min-width:0"><div class="rt">${t} · ${esc(d.yayin||"Deneme")}</div><div class="rs">${trDate(d.tarih)}</div></div><b class="rx num">${fmt(n)}</b></div>`).join("")}</div></div>`:""}
    <label class="f">${R?"Rapor notu":"Görüşme notu"}<input type="text" id="gm-not" data-gnot="${g.id}" value="${esc(g.not||"")}" placeholder="ör. problemlere ağırlık ver"></label>
    <div class="gmacts"><button class="btn pri" data-act="gbitir" data-id="${g.id}" data-sid="${sid}" data-d="${g.tarih}">${icon("check","sm")} ${R?"Rapor geldi":"Yapıldı"} · yeni haftayı başlat</button>
      <button class="btn" data-act="gdurum" data-id="${g.id}" data-v="yapildi">${R?"Sadece rapor geldi":"Sadece yapıldı"}</button><button class="btn" data-act="gdurum" data-id="${g.id}" data-v="gelmedi">${R?"Rapor gelmedi":"Gelmedi"}</button></div>
  </div>`;
}

/* ---------- Gelir paneli (koça özel; taslak ödeme verileri varsayılan olarak hariç) ---------- */
const AYK = ["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"];
function gelirVeri(taslak){
  const t = today(), ay = t.slice(0,7), aylar = []; for(let i=5;i>=0;i--){ const x = addMonthsISO(ay+"-15", -i).slice(0,7); aylar.push(x); }
  const tah = Object.fromEntries(aylar.map(a=>[a,0])); let buAyVade = 0, buAyOdenen = 0, geciken = 0, gecikenN = 0, gelecek30 = 0, aktif = 0, tutarlar = [];
  S.students.forEach((x,id)=>{ const o = odemeOf(id); if(!o || !o.bas || (o.taslak && !taslak)) return; aktif++; const tu = num(o.tutar)||0; if(tu) tutarlar.push(tu);
    Object.values(o.odenen||{}).forEach(p=>{ const m = String(p.t||"").slice(0,7); if(m in tah) tah[m] += num(p.tutar) ?? tu; });
    vadeler(o).forEach(d=>{ const paid = (o.odenen||{})[d];
      if(d.slice(0,7)===ay){ buAyVade += tu; if(paid) buAyOdenen += tu; }
      if(!paid && d < t){ geciken += tu; gecikenN++; }
      if(!paid && d >= t && d <= addDays(t,30)) gelecek30 += tu; }); });
  return {aylar, tah, buAyVade, buAyOdenen, geciken, gecikenN, gelecek30, aktif, ort: tutarlar.length ? tutarlar.reduce((a,b)=>a+b,0)/tutarlar.length : 0}; }
function gelirOzet(){
  const taslakVar = [...S.students.keys()].some(id=>odemeOf(id)?.taslak), g = gelirVeri(!!S.gelirTaslak), mx = Math.max(1, ...g.aylar.map(a=>g.tah[a])), cur = g.aylar[g.aylar.length-1];
  const bas = [...S.notifs.values()].filter(n=>n.type==="basvuru" && !n.deneme), ay = today().slice(0,7);
  const ayB = bas.filter(n=>String(n.at).slice(0,7)===ay), ogr = bas.filter(n=>n.durum==="ogrenci");
  const pct = g.buAyVade ? Math.round(g.buAyOdenen/g.buAyVade*100) : 0;
  return `
    ${taslakVar?`<div class="seg"><button data-act="gtaslak" data-v="0" aria-pressed="${!S.gelirTaslak}">Gerçek veriler</button><button data-act="gtaslak" data-v="1" aria-pressed="${!!S.gelirTaslak}">Taslaklar dahil</button></div>`:""}
    <div class="kpis">
      ${tile("t-g","check",fmtTL(g.tah[cur])||"0 ₺","Bu ay tahsil edilen")}
      ${tile("t-a","cal",fmtTL(g.buAyVade-g.buAyOdenen)||"0 ₺",`Bu ay bekleyen · %${pct} tahsil`)}
      ${tile("t-r","alert",fmtTL(g.geciken)||"0 ₺",`Geciken · ${g.gecikenN} ödeme`)}
      ${tile("t-w","users",g.aktif,`Aktif öğrenci · ort. ${fmtTL(Math.round(g.ort))||"—"}`)}
    </div>
    <div class="card"><div class="sech"><h3>Aylık tahsilat</h3><span class="faint small">Son 6 ay · ödenme tarihine göre</span></div>
      <div class="mbars" role="img" aria-label="Son 6 ayın tahsilatı">${g.aylar.map(a=>{ const v = g.tah[a], h = v/mx*100, [y,m] = a.split("-");
        return `<button class="mbar ${a===cur?"cur":""}" data-tip="${AYK[+m-1]} ${y}: ${fmtTL(v)||"0 ₺"}" aria-label="${AYK[+m-1]} ${y}: ${fmtTL(v)||"0 ₺"}"><em class="num">${a===cur||v===mx&&v>0?(fmtTL(v)||""):""}</em><i style="height:${Math.max(v?3:0,h)}%"></i><span>${AYK[+m-1]}</span></button>`; }).join("")}</div>
      <p class="faint small" style="margin:8px 0 0">Bir sütuna dokununca tutarı görürsün.</p>
      <table class="sr-only"><caption>Aylık tahsilat</caption>${g.aylar.map(a=>`<tr><th>${a}</th><td>${g.tah[a]}</td></tr>`).join("")}</table></div>
    <div class="card"><div class="sech"><h3>Önümüzdeki 30 gün</h3><b class="num">${fmtTL(g.gelecek30)||"0 ₺"}</b></div><p class="muted small" style="margin:6px 0 0">Vadesi önümüzdeki 30 gün içinde gelecek ödemelerin toplamı.</p></div>
    <p class="faint small" style="text-align:center">${S.gelirTaslak?"Taslak ödeme verileri dahil edildi.":"Taslak ödeme verileri hariç."} Tutarı girilmemiş ödeme planları 0 ₺ sayılır. </p>`;
}

/* ---------- Ödeme takibi (sadece koç; coachNotes/{uid}.odeme) ---------- */
const DEF_ODEME_MESAJ = "Merhaba, bu mesaj aylık döngümüzü hatırlatma mesajıdır. Ödememizi yaptıysak bu mesajı dikkate almayalım, dekontu Zekeriya hocaya iletmen yeterli. Eğer önemli veya acil bir durum varsa Zekeriya hocaya rahatça söyleyebilirsin.";
const PERIYOT = {ay:"Aylık", hafta4:"4 haftada bir"};
const gunFark = (a,b) => Math.round((new Date(a+"T12:00:00") - new Date(b+"T12:00:00"))/864e5); /* a - b gün */
function addMonthsISO(d, n){ const [y,m,g] = d.split("-").map(Number); const t = new Date(y, m-1+n, 1, 12); const last = new Date(t.getFullYear(), t.getMonth()+1, 0).getDate(); t.setDate(Math.min(g,last)); return iso(t); }
const odemeOf = id => (S.cnotes.get(id)||{}).odeme || null;
/* Başlangıçtan itibaren ödeme günleri (bugünden ~2 ay sonrasına kadar) */
function vadeler(o){ if(!o || !o.bas) return []; const out = [], lim = addDays(today(), 62);
  for(let i=0; i<240; i++){ const d = o.periyot==="hafta4" ? addDays(o.bas, 28*i) : addMonthsISO(o.bas, i); if(d > lim) break; out.push(d); } return out; }
/* Durum: kirmizi (5 günden fazla gecikti), pembe (gecikti), turuncu (0–3 gün kaldı), tamam, yok */
function odemeDurum(id){ const o = odemeOf(id); if(!o || !o.bas) return {k:"yok", t:"Ödeme planı yok"};
  const paid = o.odenen||{}, t = today(), un = vadeler(o).filter(d=>!paid[d]);
  const late = un.filter(d=>d < t), next = un.find(d=>d >= t);
  if(late.length){ const g = gunFark(t, late[0]); return {k: g>5 ? "kirmizi" : "pembe", d:late[0], g, n:late.length, t:`${g} gün gecikti${late.length>1?` · ${late.length} ödeme bekliyor`:""}`}; }
  if(next){ const g = gunFark(next, t); if(g<=3) return {k:"turuncu", d:next, g, t: g===0 ? "Ödeme günü bugün" : `${g} gün kaldı`}; return {k:"tamam", d:next, g, t:`Sonraki ödeme ${trDate(next)}`}; }
  return {k:"tamam", t:"Güncel"}; }
const ODEME_SIRA = {kirmizi:0, pembe:1, turuncu:2, yok:3, tamam:4};
const ODEME_ETIKET = {kirmizi:"5 günü geçti", pembe:"Gecikti", turuncu:"Yaklaşıyor", tamam:"Güncel", yok:"Plan yok"};
const fmtTL = v => v==null || v==="" ? "" : Number(v).toLocaleString("tr-TR")+" ₺";
function odemeSay(){ const c = {kirmizi:0, pembe:0, turuncu:0, yok:0, tamam:0}; S.students.forEach((_,id)=>c[odemeDurum(id).k]++); return c; }
function setDuzen(id, z){ const cn = {...(S.cnotes.get(id)||{})}; cn.duzen = z; S.cnotes.set(id, cn); persistDoc("coachNotes", id, 300); }
function setOdeme(id, fn){ const cn = {...(S.cnotes.get(id)||{})}; cn.odeme = {...(cn.odeme||{})}; fn(cn.odeme); if(!cn.odeme.bas) delete cn.odeme; S.cnotes.set(id, cn); persistDoc("coachNotes", id, 300); }
function cOdeme(){
  const c = odemeSay(), rows = sortedStudents().map(([id,x])=>({id,x,d:odemeDurum(id),o:odemeOf(id)})).sort((a,b)=>ODEME_SIRA[a.d.k]-ODEME_SIRA[b.d.k] || (a.d.d||"9").localeCompare(b.d.d||"9") || a.x.name.localeCompare(b.x.name,"tr"));
  const taslakVar = rows.some(r=>r.o && r.o.taslak), planYok = c.yok;
  const chip = (k,l) => `<div class="ochip o-${k}"><b class="num">${c[k]}</b><span>${l}</span></div>`;
  return `${topbar(`<h1 class="ttl">Ödemeler</h1>`, "", `<button class="iconbtn" data-act="go" data-v="daha" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page wide">
    ${gelirOzet()}
    <h3 style="margin:6px 0 0">Öğrenci ödemeleri</h3>
    <div class="ochips">${chip("kirmizi","5 günü geçen")}${chip("pembe","Geciken")}${chip("turuncu","3 gün içinde")}${chip("tamam","Güncel")}</div>
    ${taslakVar||planYok?`<div class="card" style="box-shadow:none;border-style:dashed">${taslakVar?`<p class="small" style="margin:0 0 10px"><b>Taslak veriler gösteriliyor.</b> Başlangıç tarihleri örnek olarak oluşturuldu; gerçek tarihleri girince taslak etiketi kalkar.</p>`:""}
      <div class="pills">${planYok?`<button class="btn sm" data-act="otaslak">${icon("plus","xs")} ${planYok} öğrenciye taslak tarih ver</button>`:""}${taslakVar?`<button class="btn sm danger" data-act="otaslaksil">Taslakları sil</button>`:""}</div></div>`:""}
    <div class="olist">${rows.map(({id,x,d,o})=>`<div class="orow o-${d.k}"><button class="ohead" data-act="sheet" data-v="odeme" data-id="${id}"><span class="av">${esc(initials(x.name))}</span><div style="min-width:0;flex:1"><b>${esc(x.name)}</b>${o&&o.taslak?` <span class="pill">taslak</span>`:""}
        <div class="osub">${o&&o.bas?`${PERIYOT[o.periyot||"ay"]}${o.tutar?" · "+fmtTL(o.tutar):""} · Başlangıç ${shortDate(o.bas)}`:"Başlangıç tarihi girilmedi"}</div></div>
        <div class="ostat"><span class="otag">${ODEME_ETIKET[d.k]}</span><span class="small">${esc(d.t)}</span></div></button>
        ${d.k==="kirmizi"||d.k==="pembe"||d.k==="turuncu"?`<button class="btn sm ${d.k==="turuncu"?"":"pri"} opay" data-act="odendi" data-id="${id}" data-d="${d.d}">${icon("check","xs")} ${shortDate(d.d)} ödendi</button>`:""}</div>`).join("") || `<div class="card"><div class="empty">Henüz öğrenci yok.</div></div>`}</div>
    <p class="faint small" style="text-align:center">${cfg().odemeAcik?`Ödemesi yapılmamış öğrenciye ödeme gününde ve 5 gün sonra saat ${esc(cfg().odemeSaat)}'de hatırlatma bildirimi gider (taslaklara gitmez). `:""}Pembe: ödeme günü geçti · Kırmızı: 5 günden fazla gecikti · Turuncu: 3 gün ya da daha az kaldı. Bu sayfayı sadece sen görürsün.</p>
  </div>`;
}
/* Taslak: mevcut öğrencilere farklı durumlar gösterecek örnek başlangıç tarihleri */
function odemeTaslak(){ const fark = [-9,-3,2,0,12,-6,5,1,20,-2], t = today(); let i = 0;
  sortedStudents().forEach(([id])=>{ if(odemeOf(id)) return; const f = fark[i++ % fark.length], cur = addDays(t, f);
    const bas = addMonthsISO(cur, -(1 + i%3)); const o = {bas, tutar:1000, periyot:"ay", taslak:true, odenen:{}};
    vadeler(o).forEach(d=>{ if(d < cur) o.odenen[d] = {t:d, tutar:1000}; });
    setOdeme(id, x=>Object.assign(x,o)); });
  toast("Taslak ödeme tarihleri oluşturuldu"); }

/* ---------- Koç ---------- */
function coachShell(){
  const unread = [...S.notifs.values()].filter(n=>!n.read).length;
  const pages = {ozet:cOzet, ogrenciler:cList, detay:cDetail, program:cProgram, bildirim:cBell, daha:cMore, ayarlar:cSettings, odeme:cOdeme, basvuru:cBasvuru, gorusme:cGorusme, gelir:cOdeme, gmod:cGmod};
  return `<div class="shell">${(pages[S.view]||cOzet)()}</div>` + navHTML([["ozet","home","Özet"],["ogrenciler","users","Öğrenciler"],["program","cal","Haftalık Program",true],["gorusme","clock","Görüşmeler",false,gunGorusme(today()).filter(g=>g.durum==="planli").length],["daha","more","Daha Fazla",false,unread]]);
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
  return `${topbar(`<div class="logo"><span class="lm">${LOGO}</span>Koç Paneli</div>`, bellBtn(unread))}
  <div class="page wide">
    <div class="hello"><p class="small" style="margin:0">${longToday()}</p><h1>Günaydın hocam</h1><p>Öğrencilerinin bu haftaki durumu. Bu sayfayı sadece sen görürsün.</p></div>
    <div class="kpis">
      ${tile("t-a","users",n,"Öğrenci")}
      ${tile("t-g","target",avgP==null?"—":"%"+Math.round(avgP*100),"Ortalama program uyumu")}
      ${tile("t-w","clock",fmtMin(avgMin),"Öğrenci başı haftalık çalışma")}
      ${tile("t-r","alert",att.length,"İlgilenmen gereken")}
    </div>
    ${gununOzeti()}
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
  return `${topbar(`<div style="min-width:0;flex:1"><h1 class="ttl" style="font-size:20px">${esc(s.name)}</h1><div class="faint small">${esc(s.alan)} · ${esc(s.sinif)}${isWA(s)?" · WhatsApp koçluğu":""}${s.okul?" · "+esc(s.okul):""}${acc?" · @"+esc(acc.u):" · hesap yok"}</div></div>`, `<button class="iconbtn" data-act="sheet" data-v="wa" data-sid="${S.cur}" aria-label="WhatsApp mesajı">${icon("chat")}</button><button class="iconbtn" data-act="sheet" data-v="ogrenci" data-id="${S.cur}" aria-label="Öğrenciyi düzenle">${icon("edit")}</button>`, `<button class="iconbtn" data-act="go" data-v="ozet" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page wide"><div class="tabs">${tabs.map(([k,n])=>`<button data-act="dtab" data-v="${k}" aria-pressed="${S.dtab===k}">${n}</button>`).join("")}</div>${body()}</div>`;
}
function cSummary(s){
  const m = coachMetrics(s), la = exams(s,"AYT").pop();
  const weak = [];
  (isMaarif(s) ? [...maarifList(s,1), ...maarifList(s,2,false)].map(x=>[x.ex, {...x, n:x.ders+" · "+x.n}]) : [...CURX().TYT.map(x=>["TYT",x]), ...aytSubjects(s,false).map(x=>["AYT",x])]).forEach(([ex,sub])=>sub.t.forEach(n=>{const y=(s.topics[tkey(sub.k,n)]||{}).y||0; if(y>0) weak.push({ex,sub:sub.n,n,y});}));
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
  const bas = list.filter(([,n])=>n.type==="basvuru"), diger = list.filter(([,n])=>n.type!=="basvuru");
  const telL = t => String(t||"").replace(/[^\d+]/g,""), wa = t => { let d = telL(t).replace(/^\+/,""); if(d.startsWith("0")) d = "9"+d; else if(d.length===10) d = "90"+d; return d; };
  const basCard = ([id,n]) => `<div class="nbas"><div class="nbh"><span class="nbi">${icon("user","sm")}</span><div style="min-width:0;flex:1"><div class="nbt">Yeni başvuru · Google Form${!n.read?` <span class="pill good">Yeni</span>`:""}${n.deneme?` <span class="pill">deneme</span>`:""}</div><div class="small muted">${ago(n.at)}</div></div></div>
      <dl><dt>Ad soyad</dt><dd>${esc(n.name||"—")}</dd>${n.hizmet?`<dt>Hizmet</dt><dd>${esc(n.hizmet)}</dd>`:""}${n.alan?`<dt>Alan</dt><dd>${esc(n.alan)}</dd>`:""}${n.tel?`<dt>Telefon</dt><dd>${esc(n.tel)}</dd>`:""}${n.eposta?`<dt>E-posta</dt><dd>${esc(n.eposta)}</dd>`:""}</dl>
      ${(n.cevaplar||[]).length?`<details><summary>Tüm cevaplar (${n.cevaplar.length})</summary><dl style="margin-top:8px">${n.cevaplar.map(x=>`<dt>${esc(x.s)}</dt><dd>${esc(x.c||"—")}</dd>`).join("")}</dl></details>`:""}
      <div class="pills">${n.tel?`<a class="btn sm" href="tel:${esc(telL(n.tel))}">Ara</a><a class="btn sm" href="https://wa.me/${esc(wa(n.tel))}" target="_blank" rel="noopener">WhatsApp</a>`:""}<button class="btn sm pri" data-act="go" data-v="basvuru">Süreci yönet · ${esc(bdLabel(n.durum||"yeni"))}</button></div></div>`;
  return `${topbar(`<h1 class="ttl">Bildirimler</h1>`)}
  <div class="page wide">${bas.length?`<h3 style="margin:0">Google Form başvuruları</h3>${bas.map(basCard).join("")}`:""}<div class="card">${diger.length? diger.map(([id,n])=>`<button class="row" data-act="${n.sid&&S.students.has(n.sid)?"open":""}" data-id="${n.sid||""}"><span class="ri" style="${!n.read?"background:var(--acs);color:var(--ac)":""}">${icon(n.type==="kayit"?"user":"alert","sm")}</span><div style="min-width:0"><div class="rt">${label[n.type]||"Bildirim"}${!n.read?` <span class="pill ac">Yeni</span>`:""}</div><div class="rs">${esc(n.name||"")}${n.type==="kayit"?` · ${esc(n.alan||"")} · ${esc(n.sinif||"")}`:" yeni şifre oluşturdu"}</div></div><span class="rx small">${ago(n.at)}</span></button>`).join("") : `<div class="empty">${bas.length?"Başka bildirim yok.":"Henüz bildirim yok. Bir öğrenci kaydolduğunda ya da Google Form doldurulduğunda burada görünür."}</div>`}</div>
  <p class="faint small" style="text-align:center">Bildirimleri açtıysan bunlar telefonuna da gelir.</p></div>`;
}
function cMore(){
  return `${topbar(`<h1 class="ttl">Daha Fazla</h1>`)}
  <div class="page wide"><h3 class="msec">İşim</h3><div class="card">
    ${(b=>`<button class="row" data-act="go" data-v="basvuru"><span class="ri" style="background:#1E9E4A;color:#fff">${icon("user","sm")}</span><div><div class="rt">Başvurular</div><div class="rs">${b?`${b} başvuru süreçte`:"Süreçte başvuru yok"}</div></div><span class="rx">${icon("chev","sm")}</span></button>`)([...S.notifs.values()].filter(n=>n.type==="basvuru" && !["ogrenci","hayir"].includes(n.durum||"yeni")).length)}
    ${(c=>`<button class="row" data-act="go" data-v="odeme"><span class="ri" style="background:${c.kirmizi+c.pembe?"var(--bads);color:var(--bad)":"var(--goods);color:var(--good)"}">${icon("cal","sm")}</span><div><div class="rt">Ödemeler ve gelir</div><div class="rs">${c.kirmizi+c.pembe?`${c.kirmizi+c.pembe} geciken`:"Geciken yok"}${c.turuncu?` · ${c.turuncu} yaklaşan`:""}${c.yok?` · ${c.yok} plansız`:""}</div></div><span class="rx">${icon("chev","sm")}</span></button>`)(odemeSay())}
    ${(u=>`<button class="row" data-act="go" data-v="bildirim"><span class="ri" style="${u?"background:var(--acs);color:var(--ac)":""}">${icon("bell","sm")}</span><div><div class="rt">Bildirimler${u?` <span class="pill ac">${u} yeni</span>`:""}</div><div class="rs">Yeni kayıtlar ve başvurular</div></div><span class="rx">${icon("chev","sm")}</span></button>`)([...S.notifs.values()].filter(x=>!x.read).length)}
  </div><h3 class="msec">Uygulama</h3><div class="card">
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
  if(YEDEK===undefined) yedekBilgi().then(()=>{ if(S.view==="ayarlar") keepSettingsOpen(); });
  if(FOTO===undefined) fotoYukle().then(()=>{ if(S.view==="ayarlar") keepSettingsOpen(); });
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
    ${sec("Ödeme hatırlatması",`${c.odemeAcik?"Ödeme günü ve 5 gün sonra "+c.odemeSaat:"kapalı"}`,`
      <div class="two"><label class="inline"><input type="checkbox" id="st-oa" data-setb="odemeAcik" ${c.odemeAcik?"checked":""}>Öğrenciye ödeme hatırlatması gönder</label>
      <label class="f">Gönderim saati<input type="time" id="st-os" data-set="odemeSaat" value="${esc(c.odemeSaat)}"></label></div>
      <label class="f">Mesaj<textarea id="st-om" data-set="odemeMesaj" rows="4">${esc(c.odemeMesaj)}</textarea></label>
      <p class="faint small" style="margin:0">Ödeme gününde ve 5 gün sonra bir kez daha gider. Ödemesi “ödendi” işaretlenen öğrenciye gitmez. Taslak ödeme verileri için hiç gönderilmez.</p>`, "odemeMesaj,odemeSaat,odemeAcik")}
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
    ${sec("Yedekleme","Verilerinin kopyası",`<p class="muted small" style="margin:0">Her pazar gecesi tüm veriler (öğrenciler, programlar, ödemeler, görüşmeler, başvurular) otomatik olarak yedeklenir ve son 12 hafta saklanır. ${YEDEK?`Son otomatik yedek: <b style="color:var(--fg)">${trDate(YEDEK.son)}</b> · ${YEDEK.ogrenci} öğrenci.`:YEDEK===null?"<b>Henüz otomatik yedek alınmadı.</b>":""}</p>
      <div class="pills"><button class="btn sm pri" data-act="yedekindir">${icon("copy","xs")} Yedeği şimdi indir</button></div>
      <p class="faint small" style="margin:0">İndirilen dosyayı bilgisayarında ya da Drive'ında sakla. Bir şey ters giderse bu dosyadan geri yükleriz.</p>`)}
    ${sec("Görüşme hatırlatması","Öğrenciye 1 saat önce bildirim",`<label class="inline"><input type="checkbox" id="st-gh" data-setb="gorusmeHatirlat" ${cfg().gorusmeHatirlat?"checked":""}>Görüşmeden 1 saat önce öğrenciye “Görüşmen 1 saat sonra” bildirimi gönder</label>
      <p class="faint small" style="margin:0">Görüşmeler sayfasındaki planlı görüşmeler için, bildirimi açık öğrencilere gider. İptal edilen ya da yapıldı işaretlenen görüşmeye gitmez.</p>`)}
    ${sec("Öğrenci mesajları (WhatsApp)","Öğrenci sayfasındaki hazır mesajlar",`<div class="f">Her satır bir mesaj <span class="faint" style="font-weight:500">· {Ad}: öğrencinin adı, {Saat} ve {Gün}: sonraki görüşmesi</span>${ta("st-wm","wmesaj",wmesajlar(),6)}</div>`, "wmesaj")}
    ${(m=>sec("Başvuru mesajları","WhatsApp'ta gönderilecek hazır mesajlar ve fotoğraf",`
      <div class="f">Onay mesajıyla gönderilecek fotoğraf<div class="pills" style="align-items:center"><span id="fotoDurum" class="small muted">${FOTO?"Fotoğraf yüklü ✓":FOTO===null?"Henüz fotoğraf yok":"Kontrol ediliyor…"}</span><label class="btn sm">${icon("plus","xs")} Fotoğraf seç<input type="file" accept="image/*" id="fotoSec" hidden></label></div>${FOTO?`<img src="${FOTO}" alt="" style="max-width:180px;border-radius:12px;margin-top:6px">`:""}</div>
      <label class="f">Onay mesajı <span class="faint" style="font-weight:500">· {Ad} yerine öğrencinin adı gelir</span><textarea data-setb2="onay" rows="10">${esc(m.onay)}</textarea></label>
      <label class="f">Kontenjan mesajı<textarea data-setb2="kontenjan" rows="3">${esc(m.kontenjan)}</textarea></label>
      <div class="two"><label class="f">IBAN<input type="text" data-setb2="iban" value="${esc(m.iban)}"></label><label class="f">Alıcı adı<input type="text" data-setb2="alici" value="${esc(m.alici)}"></label></div>
      <label class="f">Ödeme notu<textarea data-setb2="odemeNot" rows="3">${esc(m.odemeNot)}</textarea></label>
      <p class="faint small" style="margin:0">WhatsApp'ta *yıldız arası* kalın görünür.</p>`, "bmesaj"))(bmesaj())}
    ${sec("Google Form bağlantısı","Form doldurulunca sana yeşil bildirim gelsin",`<p class="muted small" style="margin:0">Başvuru formun her doldurulduğunda Bildirimler'e yeşil bir “Yeni başvuru” düşer ve telefonuna bildirim gelir. Kurulum bir kere yapılır.</p>
      <div id="formKodOut">${FORMKOD?formKodHTML():`<div class="pills"><button class="btn sm pri" data-act="formkod">Bağlantı kodunu hazırla</button></div>`}</div>`)}
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
  if(t.dataset.setb2!=null){ S.settings.bmesaj = {...(S.settings.bmesaj||{}), [t.dataset.setb2]: t.value}; saveSettings(700); return true; }
  if(t.id==="fotoSec"){ if(isChange && t.files && t.files[0]){ const st = $("#fotoDurum"); if(st) st.textContent = "Yükleniyor…"; fotoKaydet(t.files[0]).then(()=>{ keepSettingsOpen(); toast("Fotoğraf kaydedildi"); }).catch(e=>{ if(st) st.textContent = "Yüklenemedi: "+(e.message||e); }); } return true; }
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
    <div class="logo"><span class="lm">${LOGO}</span>Zekacademy</div>${roleSeg}<div id="instWrap">${installCard()}</div>
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
    <div class="logo"><span class="lm">${LOGO}</span>Zekacademy</div>
    <h2>Şifreni mi unuttun?</h2>
    <p class="sub">Koçuna yaz, sana yeni bir giriş versin. Programın, denemelerin ve tüm bilgilerin olduğu gibi kalır.</p>
    <div class="card"><b>Koçuna ne yazmalısın?</b><p class="muted small" style="margin:6px 0 0">“Hocam şifremi unuttum, kullanıcı adım: …” yazman yeterli.</p></div>
    <p class="swap"><button type="button" class="link" data-act="amode" data-v="login">Girişe dön</button></p></div>`;
  else { const adm = mode==="admin"; f = `<form class="apanel" id="fLogin" novalidate>
    <div class="logo"><span class="lm">${LOGO}</span>Zekacademy</div>${roleSeg}<div id="instWrap">${installCard()}</div>
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
    <div class="logo"><span class="lm">${LOGO}</span>${esc(cfg().kurum)}</div>
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
/* ---------- Haftalık hedef: konu arama ve öneri ---------- */
function maarifDersSubs(s, d){ const nd = trLow(d), al = MAARIF_SUBS.filter(x=>x.asama===1 || !ALANLAR.includes(s.alan) || x.a.includes(s.alan));
  let m = /türkçe|edebiyat|türk dili/.test(nd) ? al.filter(x=>x.dk==="tde")
    : /geometri/.test(nd) ? al.filter(x=>x.dk==="mat" && /geometri|eşlik|analitik/i.test(x.n))
    : al.filter(x=>trLow(x.ders).startsWith(nd) || nd.startsWith(trLow(x.ders)));
  if(!m.length) m = al; return m.map(x=>({...x, ex:x.ex})); }
function dersSubs(s, d){ if(isMaarif(s)) return maarifDersSubs(s, d); const nd = trLow(d), all = [...CURX().TYT.map(x=>({...x, ex:"TYT"})), ...CURX().AYT.map(x=>({...x, ex:"AYT"}))];
  const base = x => trLow(x.n.split(" · ")[0]);
  let m = all.filter(x=> base(x).startsWith(nd) || nd.startsWith(base(x)) || (nd.startsWith("din") && x.k==="afel"));
  if(!m.length) return all;
  const al = s.alan, rel = m.filter(x=> x.ex==="TYT" || !x.a || !ALANLAR.includes(al) || x.a.includes(al));
  return rel.length ? rel : m; }
const splitKonu = v => String(v||"").split(/\s*,\s*/).map(x=>x.trim()).filter(Boolean);
function konuOneri(s, d, subs){
  const ordered = subs.flatMap(sub=>sub.t.map(n=>({n, k:tkey(sub.k,n)})));
  const weeks = Object.keys(s.plan||{}).filter(w=> w < S.week && (s.plan[w].hedef||{})[d] && s.plan[w].hedef[d].konu).sort();
  const used = new Set(weeks.flatMap(w=>splitKonu(s.plan[w].hedef[d].konu)));
  const done = n => ordered.some(o=>o.n===n && topicScore((s.topics||{})[o.k])>=1);
  const out = [];
  if(weeks.length){ const last = s.plan[weeks[weeks.length-1]].hedef[d], lt = splitKonu(last.konu);
    if(!last.done) lt.filter(n=>!done(n)).forEach(n=> out.push({n, why:"Geçen hafta bitmedi, devam"}));
    const idx = Math.max(-1, ...lt.map(n=>ordered.findIndex(o=>o.n===n)));
    const nx = ordered.slice(idx+1).find(o=> !used.has(o.n) && !done(o.n)); if(nx) out.push({n:nx.n, why: last.done ? "Geçen hafta bitti, sıradaki konu" : "Sıradaki konu"}); }
  else { const nx = ordered.find(o=>!done(o.n)); if(nx) out.push({n:nx.n, why:"Bitirilmemiş ilk konu"}); }
  return out.slice(0,3); }
let KSEL = [];
function kselNote(){ const e = $("#ksel"); if(e) e.innerHTML = KSEL.length ? `Seçilen: <b>${esc(KSEL.join(", "))}</b>` : `<span class="faint">Henüz konu seçilmedi</span>`; }

function closeSheet(){ $("#layer").innerHTML=""; }
document.addEventListener("toggle", e=>{ const d = e.target; if(d && d.classList && d.classList.contains("mders")){ S.mOpen = S.mOpen||{}; S.mOpen[d.dataset.ders] = d.open; } }, true);
document.addEventListener("keydown", e=>{ if(e.key==="Escape" && $("#layer").innerHTML) closeSheet(); });
const sheetErr = t => { const e=$("#serr"); if(e) e.textContent=t; };

function openSheet(kind, el){
  const s = st();
  if(kind==="konu"){ const d = el.dataset.ders, w = S.week, p = plan(s,w), cur = ((p.hedef||{})[d]||{}).konu || "";
    const subs = dersSubs(s,d), allT = new Set(subs.flatMap(x=>x.t)); KSEL = splitKonu(cur);
    const free = KSEL.filter(x=>!allT.has(x)); KSEL = KSEL.filter(x=>allT.has(x));
    const one = konuOneri(s,d,subs);
    const tbtn = (sub,n) => { const full = topicScore((s.topics||{})[tkey(sub.k,n)])>=1;
      return `<button type="button" class="kt" data-act="kt" data-v="${esc(n)}" data-q="${esc(trLow(n+" "+sub.n))}" aria-pressed="${KSEL.includes(n)}">${icon("check","xs")}<span>${esc(n)}</span>${full?`<small>bitti</small>`:""}</button>`; };
    return sheet(`<h3>${esc(d)} · bitirilecek konu</h3>
      <input type="search" id="kq" placeholder="Konu ara (ör. basınç, türev)" autocomplete="off" aria-label="Konu ara">
      ${one.length?`<div class="koneri"><div class="gh">Öneri</div>${one.map(o=>`<button type="button" class="kt sug" data-act="kt" data-v="${esc(o.n)}" data-q="${esc(trLow(o.n))}" aria-pressed="${KSEL.includes(o.n)}">${icon("check","xs")}<span>${esc(o.n)}<small class="kwhy">${esc(o.why)}</small></span></button>`).join("")}</div>`:""}
      <div class="klist">${subs.map((sub,si)=>`<div class="kgrp" data-grp><div class="gh">${sub.ex} · ${esc(sub.n)}</div>${sub.t.map(n=>tbtn(sub,n)).join("")}</div>`).join("")}<p class="faint small" id="knone" hidden>Bu aramayla eşleşen konu yok. Aşağıya elle yazabilirsin.</p></div>
      <p class="small" id="ksel" style="margin:0"></p>
      <label class="f">Listede yoksa elle yaz<input type="text" name="serbest" id="kfree" value="${esc(free.join(", "))}" placeholder="ör. Karma test"></label>
      <div class="acts"><button type="button" class="btn" data-act="kclear">Temizle</button><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ const v = [...KSEL, ...splitKonu(fd.get("serbest"))].filter((x,i,a)=>a.indexOf(x)===i).join(", ");
      mutate(st=>{ const pp = ensurePlan(st,w); if(v) pp.hedef[d] = {konu:v, done: !!(pp.hedef[d] && pp.hedef[d].done && pp.hedef[d].konu===v)}; else delete pp.hedef[d]; });
      closeSheet(); render(); }), kselNote(); }
  if(kind==="odeme"){ const id = el.dataset.id, x = S.students.get(id), o = odemeOf(id) || {}, paid = o.odenen||{}, t = today();
    const vl = vadeler(o).slice().reverse();
    return sheet(`<h3>${esc(x?.name||"")} · ödeme</h3>
      <div class="two"><label class="f">Başlangıç tarihi<input type="date" name="bas" id="od-bas" value="${esc(o.bas||"")}"></label><label class="f">Tutar (₺)<input type="number" inputmode="numeric" min="0" step="50" name="tutar" id="od-tutar" value="${o.tutar??""}" placeholder="ör. 1000"></label></div>
      <label class="f">Ödeme sıklığı<select name="periyot" id="od-per">${Object.entries(PERIYOT).map(([k,l])=>`<option value="${k}" ${(o.periyot||"ay")===k?"selected":""}>${l}</option>`).join("")}</select></label>
      ${o.taslak?`<p class="small" style="margin:0;color:var(--warn)"><b>Taslak:</b> Bu tarih örnek olarak oluşturuldu. Kaydedince gerçek kabul edilir.</p>`:""}
      ${vl.length?`<div class="f">Ödemeler <span class="faint" style="font-weight:500">· dokunarak ödendi / ödenmedi yap</span><div class="vlist">${vl.map(d=>{ const p = paid[d], late = !p && d < t, g = late ? gunFark(t,d) : 0, k = p ? "ok" : late ? (g>5?"kirmizi":"pembe") : (gunFark(d,t)<=3?"turuncu":"bek");
        return `<button type="button" class="vrow v-${k}" data-act="vtog" data-id="${id}" data-d="${d}"><span>${trDate(d)}</span><span class="small">${p?`Ödendi${p.t&&p.t!==d?" · "+shortDate(p.t):""}`:late?`${g} gün gecikti`:d===t?"Bugün":`${gunFark(d,t)} gün kaldı`}</span></button>`; }).join("")}</div></div>`:""}
      <div class="err" id="serr"></div>
      <div class="acts">${o.bas?`<button type="button" class="btn danger" data-act="osil" data-id="${id}" style="margin-right:auto">Planı sil</button>`:""}<button type="button" class="btn" data-close>Kapat</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ const bas = fd.get("bas"); if(!bas) return sheetErr("Başlangıç tarihini seç.");
      setOdeme(id, z=>{ const degisti = z.bas !== bas || (z.periyot||"ay") !== fd.get("periyot"); z.bas = bas; z.tutar = num(fd.get("tutar")); z.periyot = fd.get("periyot"); delete z.taslak; if(degisti && z.odenen){ const v = new Set(vadeler(z)); Object.keys(z.odenen).forEach(d=>{ if(!v.has(d)) delete z.odenen[d]; }); } });
      closeSheet(); render(); toast("Ödeme planı kaydedildi"); }); }
  if(kind==="bdeneme") return sheet(`<h3>Deneme başvurusu</h3>
      <p class="muted small" style="margin:-6px 0 0">Süreci kendi üzerinde denemek için. Kendi telefon numaranı yazarsan WhatsApp mesajları sana (“Kendime mesaj”) gider.</p>
      <label class="f">Ad soyad<input type="text" name="ad" id="bd-ad" value="Deneme Öğrenci"></label>
      <label class="f">Telefon<input type="tel" name="tel" id="bd-tel" placeholder="05xx xxx xx xx"></label>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Oluştur</button></div>`,
    fd=>{ const ad = String(fd.get("ad")).trim(), tel = String(fd.get("tel")).trim(); if(!ad || waNo(tel).length<11) return sheetErr("Ad ve geçerli bir telefon gir.");
      const id = uid(); S.notifs.set(id, {type:"basvuru", at:nowISO(), read:true, deneme:true, name:ad, tel, alan:"Sayısal", hizmet:"Birebir Koçluk - 1000₺ / Ay", cevaplar:[{s:"İsim Soyisim", c:ad},{s:"Telefon Numaranız", c:tel}]});
      persistDoc("notifs", id, 0); closeSheet(); S.btab="aktif"; render(); toast("Deneme başvurusu oluşturuldu"); });
  if(kind==="gplan"){ const gid = el.dataset.id, g0 = gid ? (gid.startsWith("v:") ? gunGorusme(gid.split(":")[2]).find(x=>x.id===gid) : {...S.gorus.get(gid), id:gid}) : null;
    const bid = el.dataset.bid || g0?.bid || "", d0 = g0?.tarih || el.dataset.d || S.gday || today();
    const dl = gunGorusme(d0).filter(x=>x.durum!=="iptal"), sonra = dl.length ? toHm(Math.max(...dl.map(x=>hmTo(x.saat)+(x.sure||15)))) : "18:00";
    const kisi = g0 ? (g0.sid || "") : bid ? "" : "", ilk = g0 ? g0.tur==="ilk" : !!bid;
    return sheet(`<h3>${g0?"Görüşmeyi düzenle":"Görüşme ekle"}</h3>
      <label class="f">Kiminle<select name="kim" id="go-kim">${bid||(g0&&!g0.sid)?"":""}<option value="">Yeni öğrenci (ilk görüşme)</option>${sortedStudents().map(([id,x])=>`<option value="${id}" ${kisi===id?"selected":""}>${esc(x.name)}</option>`).join("")}</select></label>
      <label class="f" id="go-adw" ${kisi?"hidden":""}>Ad soyad<input type="text" name="ad" id="go-ad" value="${esc(g0&&!g0.sid?g0.ad:(el.dataset.ad||""))}" placeholder="ör. Ahmet Yılmaz"></label>
      <div class="two"><label class="f">Tarih<input type="date" name="tarih" id="go-tarih" value="${d0}"></label><label class="f">Saat<input type="time" name="saat" id="go-saat" step="300" value="${esc(g0?.saat||sonra)}"></label></div>
      <div class="two"><label class="f">Süre<select name="sure" id="go-sure">${[15,30,45,60].map(m=>`<option value="${m}" ${(g0?.sure||(ilk||!kisi?SURE_ILK:SURE_SEANS))===m?"selected":""}>${m} dk</option>`).join("")}</select></label>
        <label class="f">Tür<select name="tur" id="go-tur"><option value="seans" ${!ilk&&kisi?"selected":""}>Seans</option><option value="ilk" ${ilk||!kisi?"selected":""}>İlk görüşme</option></select></label></div>
      ${g0&&(g0.sanal||g0.kaynak==="duzen")?`<div class="f" id="go-tekw">Değişiklik<div class="seg"><label class="segr"><input type="radio" name="kapsam" value="hafta" checked><span>Sadece bu hafta</span></label><label class="segr"><input type="radio" name="kapsam" value="hep"><span>Bundan sonra hep</span></label></div></div>`
        : !g0 ? `<label class="inline" id="go-tekw" ${kisi?"":"hidden"}><input type="checkbox" name="tekrar" id="go-tekrar">Her hafta bu gün ve saatte (haftalık düzen)</label>` : ""}
      <label class="f">Not<input type="text" name="not" id="go-not" value="${esc(g0?.not||"")}" placeholder="ör. deneme analizi yapılacak"></label>
      ${g0?`<div class="f">Durum<div class="seg">${[["planli","Planlı"],["yapildi","Yapıldı"],["gelmedi","Gelmedi"],["iptal","İptal"]].map(([k,l])=>`<label class="segr"><input type="radio" name="durum" value="${k}" ${g0.durum===k?"checked":""}><span>${l}</span></label>`).join("")}</div></div>`:""}
      <div class="err" id="serr"></div>
      <div class="acts">${g0&&!g0.sanal?`<button type="button" class="btn danger" data-act="gsil" data-id="${gid}" style="margin-right:auto">Sil</button>`:""}<button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ const kim = fd.get("kim"), ad = String(fd.get("ad")||"").trim(), tarih = fd.get("tarih"), saat = fd.get("saat"), sure = +fd.get("sure"), tur = fd.get("tur"), not = String(fd.get("not")||"").trim();
      if(!kim && !ad) return sheetErr("Kiminle görüşeceğini seç ya da adını yaz."); if(!tarih || !saat) return sheetErr("Tarih ve saati seç.");
      if(!g0 && kim && fd.get("tekrar")){ setDuzen(kim, {gun:dIdx(tarih), saat, sure, bas:monday(tarih)}); if(not){ gorusSet("v:"+kim+":"+tarih, g=>{ g.not = not; }); } }
      else if(g0 && fd.get("kapsam")==="hep" && kim){ const eski = duzenOf(kim)||{}, gunDegisti = dIdx(tarih)!==dIdx(g0.tarih);
        setDuzen(kim, {...eski, saat, sure, gun: gunDegisti ? dIdx(tarih) : (eski.gun ?? null), bas: eski.bas || monday(g0.tarih)});
        if(!g0.sanal) gorusSet(gid, g=>{ Object.assign(g, {tarih, saat, sure, not, durum:fd.get("durum")||g.durum||"planli"}); });
        else if(not || (fd.get("durum")||"planli")!=="planli" || gunDegisti) gorusSet(gid, g=>{ Object.assign(g, {tarih, saat, sure, not, durum:fd.get("durum")||"planli"}); }); }
      else if(g0){ gorusSet(gid, g=>{ Object.assign(g, {sid:kim||null, ad:kim?S.students.get(kim)?.name:ad, tarih, saat, sure, tur, not, durum:fd.get("durum")||g.durum||"planli"}); if(bid) g.bid = bid; }); }
      else { const nid = uid(); S.gorus.set(nid, {sid:kim||null, ad:kim?S.students.get(kim)?.name:ad, tarih, saat, sure, tur, not, durum:"planli", ...(bid?{bid}:{})}); persistDoc("gorusmeler", nid, 0); }
      S.gday = tarih; closeSheet(); if(S.view!=="basvuru") S.view = "gorusme"; render(); toast("Görüşme kaydedildi"); }); }
  if(kind==="duzen"){ const gunOpt = (v, oto) => `<option value="">Otomatik · ${GUN[oto]}</option>${GUN.map((g,i)=>`<option value="${i}" ${v===i?"selected":""}>${g}</option>`).join("")}`;
    return sheet(`<h3>Haftalık düzen</h3><p class="muted small" style="margin:-6px 0 0">Gün, öğrencinin program döngüsünden (son görüşme günü) otomatik gelir; “Yeni görüşme” ile döngü kayarsa seans da kayar. Sen sadece saati gir. Saati boş bırakılan öğrenci takvime gelmez. Bir öğrencinin günü sabit başka bir güne geçtiyse günü elle seç.</p>
      <div class="dzlist">${sortedStudents().map(([id,x])=>{ const z = duzenOf(id)||{}; return `<div class="dzrow"><b>${esc(x.name)}</b><select name="g_${id}" aria-label="${esc(x.name)} günü">${gunOpt(z.gun??null, otoGun(id))}</select>${isWA(x)?`<span class="dzwa">${icon("chat","xs")} Rapor</span>`:`<input type="time" step="300" name="s_${id}" value="${esc(z.saat||"")}" aria-label="${esc(x.name)} saati">`}</div>`; }).join("") || `<div class="empty">Henüz öğrenci yok.</div>`}</div>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ let n = 0; const w = monday(today());
      for(const [id,x] of sortedStudents()){ const g = fd.get("g_"+id), sa = fd.get("s_"+id), z = duzenOf(id), gun = g==="" || g==null ? null : +g;
        if(isWA(x)){ if((z?.gun??null)!==gun){ setDuzen(id, gun==null ? null : {gun, bas:z?.bas||w}); n++; } continue; }
        if(!sa){ if(z){ setDuzen(id, null); n++; } continue; }
        if(!z || (z.gun??null)!==gun || z.saat!==sa){ setDuzen(id, {gun, saat:sa, sure:z?.sure||SURE_SEANS, bas:z?.bas||w}); n++; } }
      closeSheet(); render(); toast(n?`${n} öğrencinin düzeni güncellendi`:"Değişiklik yok"); }); }
  if(kind==="wa"){ const sid = el.dataset.sid, x = S.students.get(sid); if(!x) return;
    const g = sonrakiGorusme(sid);
    return sheet(`<h3>${esc(x.name)} · WhatsApp</h3>
      <label class="f">Telefon<input type="tel" name="tel" id="wa-tel" value="${esc(x.tel||"")}" placeholder="05xx xxx xx xx"></label>
      ${g?`<p class="small muted" style="margin:-4px 0 0">Sonraki görüşme: <b style="color:var(--fg)">${GUN[dIdx(g.tarih)]} ${g.saat}</b></p>`:""}
      <div class="f">Hazır mesajlar<div class="walist">${wmesajlar().map((m,i)=>`<button type="button" class="wam" data-act="wagonder" data-i="${i}" data-sid="${sid}">${esc(waDoldur(m, sid))}</button>`).join("")}</div></div>
      <label class="f">Ya da kendin yaz<textarea name="serbest" id="wa-serbest" rows="2" placeholder="Mesajın…"></textarea></label>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Kapat</button><button class="btn pri">Yazdığımı gönder</button></div>`,
    fd=>{ const t = String(fd.get("serbest")||"").trim(); if(!t) return sheetErr("Bir mesaj yaz ya da hazır mesajlardan birine dokun."); waAc(sid, t); }); }
  if(kind==="tema") return sheet(`<h3>Görünüm</h3>
    <div class="f">Mod<div class="seg">${[["system","Otomatik"],["light","Açık"],["dark","Koyu"]].map(([k,l])=>`<button type="button" data-act="mode" data-v="${k}" aria-pressed="${THEME.mode===k}">${l}</button>`).join("")}</div></div>
    <div class="f">Tema rengi<div class="swatch">${[["green","#1E9E4A","Yeşil"],["blue","#2563EB","Mavi"],["red","#DC2F3C","Kırmızı"]].map(([k,c,l])=>`<button type="button" class="sw" style="background:${c}" data-act="accent" data-v="${k}" aria-pressed="${THEME.accent===k}" aria-label="${l}">${THEME.accent===k?icon("check","sm"):""}</button>`).join("")}</div></div>
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
  if(kind==="gorusme"){ const t = (el && el.dataset && el.dataset.d) || today();
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
      <label class="f">Ad soyad<input type="text" name="name" id="m-name" value="${esc(x?.name||el.dataset.name||"")}"></label>
      <div class="two"><label class="f">Sınıf<select name="sinif" id="m-sinif">${SINIFLAR.map(a=>`<option ${sinif===a?"selected":""}>${a}</option>`).join("")}</select></label>
      <label class="f">Alan<select name="alan" id="m-alan">${(pa=>ALANLAR.map(a=>`<option ${(x?x.alan===a:pa===a)?"selected":""}>${a}</option>`).join(""))(alanTahmin(el.dataset.alan))}</select></label></div>
      <label class="f" id="m-okulWrap" ${sinif==="Mezun"?"hidden":""}>Okul<input type="text" name="okul" id="m-okul" value="${esc(x?.okul||"")}"></label>
      <label class="f">Koçluk paketi<select name="paket" id="m-paket"><option value="birebir" ${(x?x.paket!=="whatsapp":!/whatsapp/i.test((el.dataset.bid&&S.notifs.get(el.dataset.bid)?.hizmet)||""))?"selected":""}>Birebir görüşme (haftalık seans)</option><option value="whatsapp" ${(x?x.paket==="whatsapp":/whatsapp/i.test((el.dataset.bid&&S.notifs.get(el.dataset.bid)?.hizmet)||""))?"selected":""}>WhatsApp koçluğu (haftalık rapor)</option></select></label>
      <label class="f">Telefon (WhatsApp)<input type="tel" name="tel" id="m-tel" value="${esc(x?.tel||(el.dataset.bid&&S.notifs.get(el.dataset.bid)?.tel)||"")}" placeholder="05xx xxx xx xx"></label>
      ${acc?`<div class="card" style="box-shadow:none"><span class="muted small">Öğrenci hesabı: <b style="color:var(--fg)">@${esc(acc.u)}</b>${x.ilkSifre?" · henüz ilk şifresini değiştirmedi":""}. </span>
        <div class="two" style="margin-top:10px"><label class="f">Yeni şifre<input type="text" id="m-np" autocomplete="off" value="123456"></label><div class="f" style="justify-content:flex-end"><button type="button" class="btn" id="m-reset">Şifreyi sıfırla</button></div></div>
        <span class="faint small">Öğrenci bir sonraki girişinde bu şifreyle girer ve kendi şifresini belirler.</span><div class="err" id="m-rerr"></div></div>`
        :`<div class="card" style="box-shadow:none;display:flex;flex-direction:column;gap:10px"><span class="muted small">${x?"Bu öğrencinin hesabı yok. Hesap açmak için “Yeni öğrenci” ile ekleyip bu kayıtla birleştirebilirsin.":"Öğrenci bu bilgilerle kendi paneline girer. İlk girişte şifresini değiştirmesi istenir."}</span>
        ${x?"":`<div class="two"><label class="f">Kullanıcı adı<input type="text" name="u" id="m-u" autocapitalize="none" autocomplete="off" placeholder="ör. ahmetguner" value="${esc(el.dataset.name?normU(el.dataset.name).replace(/[^a-z0-9]/g,"").slice(0,20):"")}"></label><label class="f">İlk şifre<input type="text" name="p" id="m-p" autocomplete="off" value="123456"></label></div>`}</div>`}
      ${x?`<label class="f">Başka bir kayıtla birleştir<select name="merge" id="m-merge"><option value="">—</option>${sortedStudents().filter(([k])=>k!==id).map(([k,y])=>`<option value="${k}">${esc(y.name)} · ${esc(y.sinif)}${y.kullanici?" · @"+esc(y.kullanici):""}</option>`).join("")}</select><span class="faint small" style="font-weight:500">Seçtiğin eski kaydın tüm verisi bu kayda taşınır ve eski kayıt silinir.</span></label>`:""}
      <div class="err" id="serr"></div>
      <div class="acts">${x?`<button type="button" class="btn danger" id="m-del" style="margin-right:auto">Öğrenciyi sil</button>`:""}<button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri" data-label="${x?"Kaydet":"Ekle"}">${x?"Kaydet":"Ekle"}</button></div>`,
    async (fd, form)=>{ const name = String(fd.get("name")).trim(); if(!name) return sheetErr("Ad soyad gerekli.");
      const sn = fd.get("sinif"), okul = sn==="Mezun"?"":String(fd.get("okul")||"").trim();
      const tel = String(fd.get("tel")||"").trim(), paket = fd.get("paket")==="whatsapp" ? "whatsapp" : "birebir";
      if(x){ Object.assign(x,{name,alan:fd.get("alan"),sinif:sn,okul,tel,paket});
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
        S.students.set(nid, {...blank({name,alan:fd.get("alan"),sinif:sn,okul,kullanici:u}), ilkSifre:true, paket, ...(tel?{tel}:{})}); persistDoc("students", nid, 0);
        const bid = el.dataset.bid;
        if(bid && S.notifs.has(bid)){ const bn = S.notifs.get(bid); bSet(bid, z=>{ z.durum="ogrenci"; z.sid=nid; });
          const tl = num(String(bn.hizmet||"").replace(/\./g,"").match(/(\d{3,6})\s*₺/)?.[1]); const t0 = today();
          setOdeme(nid, z=>Object.assign(z, {bas:t0, tutar:tl, periyot:"ay", odenen:{[t0]:{t:t0, tutar:tl}}})); }
        S.cur=nid; S.view="detay"; S.dtab="ozet"; closeSheet(); render(); toast(`Hesap açıldı · @${u} · ilk şifre ${p}${bid?" · ödeme takibi bugünden başladı":""}`); }
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
    case "mx": S.mx = +v; render(); break;
    case "odendi": { const id=b.dataset.id, d=b.dataset.d; setOdeme(id, o=>{ o.odenen = {...(o.odenen||{})}; o.odenen[d] = {t:today(), tutar:o.tutar??null}; }); render(); toast(`${S.students.get(id)?.name||""}: ${trDate(d)} ödemesi işlendi`); break; }
    case "vtog": { const id=b.dataset.id, d=b.dataset.d; setOdeme(id, o=>{ o.odenen = {...(o.odenen||{})}; if(o.odenen[d]) delete o.odenen[d]; else o.odenen[d] = {t:today(), tutar:o.tutar??null}; }); openSheet("odeme", b); render(); break; }
    case "osil": { const id=b.dataset.id; const cn = {...(S.cnotes.get(id)||{})}; cn.odeme = null; S.cnotes.set(id, cn); persistDoc("coachNotes", id, 0); closeSheet(); render(); toast("Ödeme planı silindi"); break; }
    case "otaslak": odemeTaslak(); render(); break;
    case "gday": S.gday = v; S.view = "gorusme"; render(); break;
    case "gmod": S.gsel = v; S.view = "gmod"; render(); window.scrollTo(0,0); break;
    case "gbitir": { const rid = gorusSet(b.dataset.id, g=>{ g.durum = "yapildi"; }); S.gsel = rid; S.cur = b.dataset.sid; render(); const bb = document.createElement("button"); bb.dataset.d = b.dataset.d; openSheet("gorusme", bb); break; }
    case "yedekindir": yedekIndir(); break;
    case "wagonder": waAc(b.dataset.sid, waDoldur(wmesajlar()[+b.dataset.i], b.dataset.sid)); break;
    case "gwk": S.gday = addDays(monday(S.gday||today()), +b.dataset.d); render(); break;
    case "gdurum": gorusSet(b.dataset.id, g=>{ g.durum = v; }); render(); break;
    case "gsil": { const id=b.dataset.id; S.gorus.delete(id); persistDoc("gorusmeler", id, 0); closeSheet(); render(); toast("Görüşme silindi"); break; }
    case "gtaslak": S.gelirTaslak = v==="1"; render(); break;
    case "brehber": rehbereKaydet(b.dataset.id); break;
    case "bonay": onayGonder(b.dataset.id); break;
    case "bmetin": metinGonder(b.dataset.id, v); break;
    case "bdurum": bSet(b.dataset.id, x=>{ x.durum = v; }); render(); toast(v==="evet"?"Evet dedi: sıradaki adım ödeme bilgisi":v==="hayir"?"Vazgeçenlere taşındı":"Aktife alındı"); break;
    case "btab": S.btab = v; render(); break;
    case "nsil": { const id=b.dataset.id; S.notifs.delete(id); deleteDoc(doc(fdb,"notifs",id)).catch(()=>toast("Silinemedi")); render(); break; }
    case "formkod": formKod(b.dataset.v2==="yenile"); break;
    case "kopyala": { const el=document.getElementById(b.dataset.hedef); if(el){ (navigator.clipboard?navigator.clipboard.writeText(el.textContent):Promise.reject()).then(()=>toast("Kopyalandı")).catch(()=>{ const r=document.createRange(); r.selectNodeContents(el); const sel=getSelection(); sel.removeAllRanges(); sel.addRange(r); toast("Seçildi, kopyala de"); }); } break; }
    case "otaslaksil": S.students.forEach((_,id)=>{ const o = odemeOf(id); if(o && o.taslak){ const cn = {...(S.cnotes.get(id)||{})}; cn.odeme = null; S.cnotes.set(id, cn); persistDoc("coachNotes", id, 0); } }); render(); toast("Taslak ödeme verileri silindi"); break;
    case "kt": { const n=v, on=!KSEL.includes(n); KSEL = on ? [...KSEL, n] : KSEL.filter(x=>x!==n); document.querySelectorAll("#layer .kt").forEach(x=>{ if(x.dataset.v===n) x.setAttribute("aria-pressed", on); }); kselNote(); break; }
    case "kclear": KSEL=[]; document.querySelectorAll("#layer .kt").forEach(x=>x.setAttribute("aria-pressed","false")); { const f=$("#kfree"); if(f) f.value=""; } kselNote(); break;
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
  if(t.id==="go-kim"){ const yeni = !t.value; const aw=$("#go-adw"), tw=$("#go-tekw"); if(aw) aw.hidden = !yeni; if(tw) tw.hidden = yeni; $("#go-sure").value = String(yeni?SURE_ILK:SURE_SEANS); $("#go-tur").value = yeni?"ilk":"seans"; return; }
  if(t.id==="go-tur"){ $("#go-sure").value = String(t.value==="ilk"?SURE_ILK:SURE_SEANS); return; }
  if(t.name==="sinif"){ const w = t.closest("form")?.querySelector("#okulWrap,#m-okulWrap"); if(w) w.hidden = t.value==="Mezun"; }
  else if(t.dataset.net){ const i=document.getElementById(t.dataset.net); i.disabled=t.checked; if(t.checked) i.value=""; }
  else if(t.dataset.act==="pick"){ S.cur=t.value; S.week=curStart(st()); S.day=today(); render(); }
  else if(t.dataset.quick!=null && t.value){ const d=t.dataset.quick, ta=document.getElementById("pl-"+pIdx(st(),d)); if(ta){ ta.value = (ta.value.trim()? ta.value.replace(/\s+$/,"")+"\n" : "") + t.value; ta.dispatchEvent(new Event("input",{bubbles:true})); } t.value=""; }
  else if(t.dataset.plan || t.dataset.hd==="konu"){ setTimeout(()=>{ if(!document.activeElement || !document.activeElement.matches("textarea,input[type=text],input[type=number]")) render(); }, 0); }
  else if(t.dataset.f && t.type==="date"){ setField(t.dataset.f, t.value); }
});
document.addEventListener("keydown", e=>{ if(e.key==="Enter" && e.target.id==="kq"){ e.preventDefault(); const b=[...document.querySelectorAll("#layer .klist .kt")].find(x=>!x.hidden && !x.closest("[hidden]")); if(b) b.click(); } });
document.addEventListener("input", e=>{
  const t = e.target;
  if(A() && t.closest && t.closest("#settingsPage")){ onSetting(t,false); return; }
  if(t.dataset.gnot){ const id = gorusSet(t.dataset.gnot, g=>{ g.not = t.value; }); if(id!==t.dataset.gnot){ t.dataset.gnot = id; S.gsel = id; } return; }
  if(t.id==="kq"){ const q = trLow(t.value).trim(); let any=false;
    document.querySelectorAll("#layer .klist .kgrp").forEach(g=>{ let n=0; g.querySelectorAll(".kt").forEach(b=>{ const ok = !q || b.dataset.q.includes(q); b.hidden=!ok; if(ok) n++; }); g.hidden = !n; if(n) any=true; });
    const ko=$("#layer .koneri"); if(ko) ko.hidden = !!q; const kn=$("#knone"); if(kn) kn.hidden = any; return; }
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

