/* Zekacademy koçluk uygulaması */
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js";
import { getAuth, initializeAuth, inMemoryPersistence, onAuthStateChanged, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, setPersistence, browserLocalPersistence, browserSessionPersistence, updatePassword, reauthenticateWithCredential, EmailAuthProvider } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-auth.js";
import { getFirestore, doc, setDoc, updateDoc, deleteDoc, deleteField, FieldPath, collection, onSnapshot, query, where, getDoc } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js";
import { getMessaging, getToken, isSupported as messagingSupported } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-messaging.js";
import { getFunctions, httpsCallable } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-functions.js";
import { firebaseConfig, vapidKey } from "./firebase-config.js";
const fbApp = initializeApp(firebaseConfig);

/* ---------- Müfredat (Zekacademy şablonundan) ---------- */
const CUR = {"TYT": [{"k": "tr", "n": "Türkçe", "g": "Türkçe", "t": ["Sözcükte Anlam", "Söz Yorumu", "Deyimler ve Atasözleri", "Cümlede Anlam", "Ses Bilgisi", "Sözcükte Yapı/Ekler", "Sözcük Türleri", "Fiiller-Fiilimsiler-Ek Fiiller-Çatı", "Sözcük Grupları", "Cümlenin Ögeleri", "Cümle Türleri", "Anlatım Bozukluğu", "Yazım Kuralları", "Noktalama İşaretleri"]}, {"k": "mat", "n": "Matematik · İlk 12 Konu", "g": "Matematik", "t": ["Temel Kavramlar", "Rasyonel Sayılar", "Sayı Basamakları", "Bölme ve Bölünebilme", "Ebob – ekok", "Basit Eşitsizlikler", "Mutlak Değer", "Üslü Sayılar", "Köklü Sayılar", "Çarpanlara Ayırma", "Oran Orantı", "Denklem Çözme"]}, {"k": "prob", "n": "Matematik · Problemler", "g": "Matematik", "t": ["Sayı Problemleri", "Kesir Problemleri", "Yaş Problemleri", "Hareket Hız Problemleri", "İşçi Emek Problemleri", "Yüzde Problemleri", "Kar Zarar Problemleri", "Karışım Problemleri", "Grafik Problemleri", "Rutin Olmayan Problemleri"]}, {"k": "matd", "n": "Matematik · Diğer Konular", "g": "Matematik", "t": ["Kümeler-Kartezyen Çarpım", "Mantık", "Fonksiyonlar", "Polinomlar", "2.Dereceden Denklemler", "Permütasyon ve Kombinasyon", "Olasılık", "Veri – İstatistik"]}, {"k": "geo", "n": "Geometri", "g": "TYT/AYT", "t": ["Temel Kavramlar", "Doğruda Açılar", "Üçgende Açılar", "Özel Üçgenler", "Dik Üçgen", "İkizkenar Üçgen", "Eşkenar Üçgen", "Açıortay", "Kenarortay", "Eşlik ve Benzerlik", "Üçgende Alan", "Üçgende Benzerlik", "Açı Kenar Bağıntıları", "Çokgenler", "Özel Dörtgenler", "Dörtgenler", "Deltoid", "Paralelkenar", "Eşkenar Dörtgen", "Dikdörtgen", "Kare", "Yamuk", "Çemberde Açı", "Çemberde Uzun", "Dairede Çevre ve Alan", "Noktanın Analitiği", "Doğrunun Analitiği", "Dönüşüm Geometrisi", "Çemberin Analitiği", "Katı Cisimler", "Prizmalar", "Küp", "Silindir", "Piramit", "Koni", "Küre"]}, {"k": "tar", "n": "Tarih", "g": "Sosyal", "t": ["TYT Tarih", "Tarih ve Zaman", "İnsanlığın İlk Dönemleri", "Ortaçağ’da Dünya", "İlk ve Orta Çağlarda Türk Dünyası", "İslam Medeniyetinin Doğuşu", "İlk Türk İslam Devletleri", "Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi", "Beylikten Devlete Osmanlı Siyaseti(1300-1453)", "Dünya Gücü Osmanlı Devleti (1453-1600)", "Yeni Çağ Avrupa Tarihi", "Yakın Çağ Avrupa Tarihi", "Osmanlı Devletinde Arayış Yılları", "18. Yüzyılda Değişim ve Diplomasi", "En Uzun Yüzyıl", "Osmanlı Kültür ve Medeniyeti", "20. Yüzyılda Osmanlı Devleti", "I. Dünya Savaşı", "Mondros Ateşkesi, İşgaller ve Cemiyetler", "Kurtuluş Savaşına Hazırlık Dönemi", "I. TBMM Dönemi", "Kurtuluş Savaşı ve Antlaşmalar", "II. TBMM Dönemi ve Çok Partili Hayata Geçiş", "Türk İnkılabı", "Atatürk İlkeleri", "Atatürk Dönemi Türk Dış Politikası"]}, {"k": "cog", "n": "Coğrafya", "g": "Sosyal", "t": ["Doğa ve İnsan", "Dünya’nın Şekli ve Hareketleri", "Coğrafi Konum", "Harita Bilgisi", "Atmosfer ve Sıcaklık", "İklimler", "Basınç ve Rüzgarlar", "Nem, Yağış ve Buharlaşma", "İç Kuvvetler / Dış Kuvvetler", "Su – Toprak ve Bitkiler", "Nüfus", "Göç", "Yerleşme", "Türkiye’nin Yer Şekilleri", "Ekonomik Faaliyetler", "Bölgeler", "Uluslararası Ulaşım Hatları", "Çevre ve Toplum", "Doğal Afetler"]}, {"k": "fel", "n": "Felsefe", "g": "Sosyal", "t": ["Felsefenin Konusu", "Bilgi Felsefesi", "Varlık Felsefesi", "Ahlak Felsefesi", "Sanat Felsefesi", "Din Felsefesi", "Siyaset Felsefesi", "Bilim Felsefesi"]}, {"k": "fiz", "n": "Fizik", "g": "Fen", "t": ["Fizik Bilimine Giriş", "Madde ve Özellikleri", "Sıvıların Kaldırma Kuvveti", "Basınç", "Isı, Sıcaklık ve Genleşme", "Hareket ve Kuvvet", "Dinamik", "İş, Güç ve Enerji", "Elektrik", "Manyetizma", "Dalgalar", "Optik"]}, {"k": "kim", "n": "Kimya", "g": "Fen", "t": ["Kimya Bilimi", "Atom ve Yapısı", "Periyodik Sistem", "Kimyasal Türler Arası Etkileşimler", "Maddenin Halleri", "Kimyanın Temel Kanunları", "Kimyasal Hesaplamalar", "Karışımlar", "Asitler, Bazlar ve Tuzlar", "Endüstride ve Canlılarda Enerji", "Kimya Her Yerde"]}, {"k": "bio", "n": "Biyoloji", "g": "Fen", "t": ["Canlıların Ortak Özellikleri", "Canlıların Temel Bileşenleri", "Hücre ve Organeller – Madde Geçişleri", "Canlıların Sınıflandırılması", "Hücrede Bölünme – Üreme", "Kalıtım", "Ekosistem"]}], "AYT": [{"k": "amat", "n": "Matematik", "g": "SAY · EA", "t": ["Polinomlar", "Fonksiyonlar", "2.Dereceden Denklemler", "Permütasyon ve Kombinasyon", "Binom ve Olasılık", "İstatistik", "Karmaşık Sayılar", "Eşitsizlikler", "Parabol", "Trigonometri", "Logaritma", "Diziler", "Limit", "Türev", "İntegral"], "a": ["SAY", "EA"]}, {"k": "afiz", "n": "Fizik", "g": "SAY", "t": ["Vektörler", "Bağıl Hareket", "Newton’un Hareket Yasaları", "Bir Boyutta Sabit İvmeli Hareket", "Atışlar", "Enerji ve Hareket", "İtme ve Momentum", "Tork Denge", "Kütle ve Ağırlık Merkezi", "Basit Makineler", "Düzgün Çembersel Hareket", "Eylemsizlik ve Açısal Momentum", "Kütle Çekim Kuvveti", "Basit Harmonik Hareket", "Dalga Mekaniği", "Elektrik Alan ve Potansiyel", "Paralel Levhalar ve Sığa", "Manyetik Alan ve Manyetik Kuvvet", "İndüksiyon, Alternatif Akım ve Transformatörler", "Atom Modelleri", "Büyük Patlama ve Parçacık Fiziği", "Radyoaktivite", "Özel Görelilik", "Kara Cisim Işıması", "Fotoelektrik Olay ve Compton Olayı", "Modern Fiziğin Teknolojideki Uygulamaları"], "a": ["SAY"]}, {"k": "akim", "n": "Kimya", "g": "SAY", "t": ["Modern Atom Teorisi", "Gazlar", "Sıvı Çözeltiler", "Kimyasal Tepkimelerde Enerji", "Kimyasal Tepkimelerde Hız", "Kimyasal Tepkimelerde Denge", "Asit-Baz Dengesi", "Çözünürlük Dengesi", "Kimya ve Elektrik", "Organik Kimyaya Giriş", "Hidrokarbonlar (Alkan, Alken, Alkin)", "Aromatik Bileşikler", "Alkoller ve Eterler", "Karbonil Bileşikleri (Aldehit ve Keton)", "Karboksilik Asitler ve Esterler", "Organik Tepkimeler ve İzomeri", "Enerji Kaynakları ve Bilimsel Gelişmeler"], "a": ["SAY"]}, {"k": "abio", "n": "Biyoloji", "g": "SAY", "t": ["Sinir Sistemi", "Endokrin Sistem", "Duyu Organları", "Destek ve Hareket Sistemi", "Sindirim Sistemi", "Dolaşım ve Bağışıklık Sistemi", "Solunum Sistemi", "Boşaltım Sistemi", "Üreme Sistemi ve Embriyonik Gelişim", "Komünite ve Popülasyon Ekolojisi", "Genetik Şifre-Protein Sentezi", "Fotosentez – Kemosentez", "Hücresel Solunum", "Bitki Biyolojisi", "Canlılar ve Çevre"], "a": ["SAY"]}, {"k": "aede", "n": "Edebiyat", "g": "EA · SÖZ", "t": ["Güzel Sanatlar ve Edebiyat", "Metinlerin Sınıflandırılması", "Şiir Bilgisi", "Edebi Sanatlar", "Türk Edebiyatı Dönemleri", "İslamiyet Öncesi Türk Edebiyatı ve Geçiş Dönemi", "Halk Edebiyatı", "Divan Edebiyatı", "Tanzimat Edebiyatı", "Servet-i Fünun Edebiyatı", "Fecr-i Ati Edebiyatı", "Milli Edebiyat", "Cumhuriyet Dönemi Edebiyatı", "Edebiyat Akımları", "Dünya Edebiyatı"], "a": ["EA", "SÖZ"]}, {"k": "atar", "n": "Tarih", "g": "EA · SÖZ", "t": ["Tarih ve Zaman", "İnsanlığın İlk Dönemleri", "Ortaçağ’da Dünya", "İlk ve Orta Çağlarda Türk Dünyası", "İslam Medeniyetinin Doğuşu", "İlk Türk İslam Devletleri", "Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi", "Beylikten Devlete Osmanlı Siyaseti(1300-1453)", "Dünya Gücü Osmanlı Devleti (1453-1600)", "Yeni Çağ Avrupa Tarihi", "Yakın Çağ Avrupa Tarihi", "Osmanlı Devletinde Arayış Yılları", "18. Yüzyılda Değişim ve Diplomasi", "En Uzun Yüzyıl", "Osmanlı Kültür ve Medeniyeti", "20. Yüzyılda Osmanlı Devleti", "I. Dünya Savaşı", "Mondros Ateşkesi, İşgaller ve Cemiyetler", "Kurtuluş Savaşına Hazırlık Dönemi", "I. TBMM Dönemi", "Kurtuluş Savaşı ve Antlaşmalar", "II. TBMM Dönemi ve Çok Partili Hayata Geçiş", "Türk İnkılabı", "Atatürk İlkeleri", "Atatürk Dönemi Türk Dış Politikası", "Atatürk Sonrası Dış Politika ve Güncel Olaylar"], "a": ["EA", "SÖZ"]}, {"k": "acog", "n": "Coğrafya", "g": "EA · SÖZ", "t": ["Biyoçeşitlilik", "Enerji Akışı ve Madde Döngüleri", "Nüfus Politikaları", "Şehirlerin Fonksiyonları", "Türkiyede Yerleşmeler", "Ekonomik Faaliyetler", "Türkiyede Tarım", "Türkiyede Hayvancılık", "Türkiyede Madenler", "Türkiyede Enerji Kaynakları", "Türkiyede Sanayi", "Kültür Bölgeleri", "Küresel Ticaret", "Küresel ve Bölgesel Örgütler", "Çevre Sorunları ve Ekstrem Doğa Olayları", "Küresel İklim Değişikliği", "Kalkınma Projeleri", "Türkiyede Ulaşım", "Türkiyede Ticaret", "Türkiyede Turizm", "Jeopolitik Konum", "Ülkeler Arası Etkileşimler", "Çatışma Bölgeleri", "Çevre Sorunları"], "a": ["EA", "SÖZ"]}, {"k": "afel", "n": "Felsefe Grubu", "g": "SÖZ", "t": ["Felsefe", "Psikoloji", "Sosyoloji", "Mantık", "Din"], "a": ["SÖZ"]}]};
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
  kamera:'<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
  kitapcik:'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/>',
  video:'<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9.5v5l4.5-2.5z"/>',
  defter:'<path d="M6 3h11a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6z"/><path d="M6 3v18M10 8h5"/>',
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
  const m = document.querySelector('meta[name="theme-color"]'); if(m) m.setAttribute("content", c);
  /* Android alt gezinme çubuğu: sayfanın renk şemasına ve kök zemine bakar */
  const cs = document.querySelector('meta[name="color-scheme"]'); if(cs) cs.setAttribute("content", dark ? "dark" : "light");
  document.documentElement.style.background = dark ? "#0A0B0E" : ""; }
try{ matchMedia("(prefers-color-scheme: dark)").addEventListener("change", setBarColor); }catch(e){}
/* ---------- Ses efektleri (Web Audio ile üretilir, dosya yok; Görünüm'den kapatılabilir) ---------- */
const SES = { acik: (()=>{ try{ return localStorage.getItem("zk-ses")!=="0"; }catch(e){ return true; } })(), ctx:null };
function sesCtx(){ try{ if(!SES.ctx){ const C = window.AudioContext || window.webkitAudioContext; if(!C) return null; SES.ctx = new C(); } if(SES.ctx.state==="suspended") SES.ctx.resume(); return SES.ctx; }catch(e){ return null; } }
function sesNota(c, f, t0, sure, vol, tip, f2){ const o = c.createOscillator(), g = c.createGain(); o.type = tip || "sine"; o.frequency.setValueAtTime(f, t0); if(f2) o.frequency.exponentialRampToValueAtTime(f2, t0+sure);
  g.gain.setValueAtTime(0.0001, t0); g.gain.exponentialRampToValueAtTime(vol, t0+0.008); g.gain.exponentialRampToValueAtTime(0.0001, t0+sure); o.connect(g).connect(c.destination); o.start(t0); o.stop(t0+sure+0.03); }
function sesCal(tur){ if(!SES.acik) return; const c = sesCtx(); if(!c) return; const t = c.currentTime + 0.005;
  try{ if(tur==="tik") sesNota(c, 480, t, 0.035, 0.018, "sine", 360);
    else if(tur==="basari"){ sesNota(c, 659, t, 0.12, 0.045, "triangle"); sesNota(c, 880, t+0.09, 0.16, 0.045, "triangle"); sesNota(c, 1175, t+0.18, 0.24, 0.035, "triangle"); } }catch(e){} }
/* Ses ve dalga sadece gerçek düğmelerde; satırlar, kartlar ve listeler sessiz ve sabit */
const DUGME = ".btn, .iconbtn, .nb, .tog, .chip, .seg button, .szkeys button, label.btn, .temabtn, .og4 button, .kis button, .oyd, .bksik button, .kasik button, .vdc button";
const DALGA = ".btn, .tog, .chip, .seg button, label.btn, .og4 button, .kis button, .bksik button, .vdc button";
document.addEventListener("pointerdown", e=>{ const b = e.target.closest && e.target.closest(DUGME); if(!b || b.disabled || b.matches('[data-act="tick"]')) return; sesCal("tik");
  const d = e.target.closest(DALGA); if(!d || matchMedia("(prefers-reduced-motion: reduce)").matches) return; const r = d.getBoundingClientRect(), z = Math.max(r.width, r.height);
  const sp = document.createElement("span"); sp.className = "dalga"; sp.style.cssText = `width:${z}px;height:${z}px;left:${e.clientX - r.left - z/2}px;top:${e.clientY - r.top - z/2}px`; d.appendChild(sp); setTimeout(()=>sp.remove(), 520); }, {passive:true});
/* Ana sayfadaki küçük açık/koyu geçiş butonu */
const koyuMu = () => THEME.mode==="dark" || (THEME.mode==="system" && matchMedia("(prefers-color-scheme: dark)").matches);
const temaBtn = () => { const k = koyuMu(); return `<button class="temabtn" data-act="temagec" aria-label="${k?"Açık moda geç":"Koyu moda geç"}" title="${k?"Açık mod":"Koyu mod"}">${icon(k?"sun":"moon","xs")}</button>`; };
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
  kaynak: x.kaynak || DEF_KAYNAK,
  paketler: Array.isArray(x.paketler) && x.paketler.length ? x.paketler : DEF_PAKET,
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
  unsubs.push(onSnapshot(doc(fdb,"settings","main"), s=>{ S.setYuklu = true; if(s.exists() && !setDirty){ S.settings = {...S.settings, ...JSON.parse(JSON.stringify(s.data()))}; } if(A() && S.settings.tahmini && S.settings.examDate==="2027-06-19"){ S.settings.tahmini=false; saveSettings(); } /* 19 Haziran 2027 kesinleşti */ loaded.settings=true; checkReady(need); render(true); },
    e=>{ console.error("settings", e); loaded.settings=true; checkReady(need); render(); }));
}
/* Bir kerelik düzeltme: Drive aktarımında kitap sütununa karışan saat çizelgesi satırlarını temizle */
const ORGANIK = ["Organik Kimyaya Giriş", "Hidrokarbonlar (Alkan, Alken, Alkin)", "Aromatik Bileşikler", "Alkoller ve Eterler", "Karbonil Bileşikleri (Aldehit ve Keton)", "Karboksilik Asitler ve Esterler", "Organik Tepkimeler ve İzomeri"];
function organikBol(){ if(!A() || !S.setYuklu || S.settings.duzeltme?.organik) return; let n = 0;
  const ak = S.settings.cur?.AYT?.find(x=>x.k==="akim"); if(ak && ak.t.includes("Organik Kimya")){ const k = ak.t.indexOf("Organik Kimya"); ak.t.splice(k, 1, ...ORGANIK); }
  S.students.forEach((x,id)=>{ const o = (x.topics||{})["akim|Organik Kimya"]; if(!o) return; ORGANIK.forEach(t=>{ const kk = "akim|"+t; if(!x.topics[kk]) x.topics[kk] = {...o}; }); delete x.topics["akim|Organik Kimya"]; n++; persistDoc("students", id, 0); });
  S.settings.duzeltme = {...(S.settings.duzeltme||{}), organik: nowISO()}; saveSettings(); if(n) console.log("organik bölündü:", n); }
function kitapAyir(){ if(!A() || !S.setYuklu || S.settings.duzeltme?.kitapAyir) return; let n = 0;
  S.students.forEach((x,id)=>{ const K = x.kitaplar; if(!K) return; let deg = false;
    Object.keys(K).forEach(d=>{ if(d.includes("|") || !ikiSinavli(x,d) || K[d+"|AYT"]) return; const p = String(K[d]).split(/\s+·\s+/); if(p.length < 2) return; K[d] = p[0]; K[d+"|AYT"] = p.slice(1).join(" + "); deg = true; });
    if(deg){ n++; persistDoc("students", id, 0); } });
  S.settings.duzeltme = {...(S.settings.duzeltme||{}), kitapAyir: nowISO()}; saveSettings(); if(n) console.log("kitap TYT/AYT ayrıldı:", n); }
function kitapCizelgeTemizle(){ if(!A() || !S.setYuklu || S.settings.duzeltme?.kitapCizelge) return; const saat = /\d{1,2}[.:]\d{2}\s*-\s*\d{1,2}[.:]\d{2}|^ara\b/i; let n = 0;
  S.students.forEach((x,id)=>{ const K = x.kitaplar; if(!K) return; let deg = false;
    Object.keys(K).forEach(d=>{ const parca = String(K[d]).split(/\s+·\s+/), kal = parca.filter(p=>!saat.test(p.trim())); if(kal.length !== parca.length){ deg = true; if(kal.length) K[d] = kal.join(" · "); else delete K[d]; } });
    if(deg){ n++; persistDoc("students", id, 0); } });
  S.settings.duzeltme = {...(S.settings.duzeltme||{}), kitapCizelge: nowISO()}; saveSettings(); if(n) console.log("kitap çizelge temizliği:", n); }
function checkReady(need){ if(!S.ready && need.every(k=>loaded[k])){ S.ready = true; geriKoruma(); if(S.role==="admin") setTimeout(()=>{ kitapCizelgeTemizle(); organikBol(); setTimeout(kitapAyir, 800); }, 1500); if(S.role==="student") startStudent(S.me); openDeepLink(); render(); pushSupported().then(()=>{ refreshPush(); render(); }); } }
function openDeepLink(){ const v = new URLSearchParams(location.search).get("ac"); if(!v) return; if(v==="program"){ S.view="program"; S.pmode="gun"; S.day=today(); if(st()) S.week=curStart(st()); } else if(v==="bildirim") S.view="bildirim"; else if(v==="socoz"){ S.view="socoz"; setTimeout(szKullanimYukle, 1500); } else if(v==="ayarlar" && A()) S.view="ayarlar"; history.replaceState(null, "", "/"); }
function stopWatching(){ unsubs.forEach(u=>{ try{ u(); }catch(e){} }); unsubs = []; for(const k in SQK) delete SQK[k]; S.sorular = new Map(); BASE.clear(); for(const k in loaded) delete loaded[k]; S.students.clear(); S.notifs.clear(); S.cnotes.clear(); S.gorus.clear(); S.ready = false; }

let authResolved = false;
function init(){
  onAuthStateChanged(auth, user=>{
    authResolved = true; stopWatching();
    if(!user){ S.role=null; S.me=null; render(); return; }
    if(user.email === COACH_EMAIL){
      S.role = "admin"; S.me = null; S.view = "ozet";
      const need = ["students","notifs","coachNotes","gorusmeler","settings"]; need.slice(0,4).forEach(c=>watchColl(c, need)); watchSettings(need); watchSorular(query(collection(fdb,"sorular"), where("durum","==","bekliyor"))); unsubs.push(onSnapshot(doc(fdb,"koc","form"), d=>{ S.formDurum = d.exists() ? d.data() : null; render(true); }, e=>console.warn("form durumu", e)));
    } else {
      S.role = "student"; S.me = user.uid; S.view = "home";
      const need = ["students","settings"];
      unsubs.push(onSnapshot(doc(fdb,"students",user.uid), s=>{ if(!dirty.has("students/"+user.uid)){ if(s.exists()){ const v = JSON.parse(JSON.stringify(s.data())); S.students.set(user.uid, v); BASE.set("students/"+user.uid, JSON.parse(JSON.stringify(v))); } else S.students.delete(user.uid); } loaded.students=true; checkReady(need); render(true); },
        e=>{ console.error(e); loaded.students=true; checkReady(need); render(); }));
      watchSettings(need); watchSorular(query(collection(fdb,"sorular"), where("sid","==",user.uid)));
    }
    render();
  });
}
/* Takıldığım sorular: sorular/{id} (bilgi + küçük resim), soruFoto/{id} (büyük resim, açınca yüklenir) */
S.sorular = new Map(); const SQK = {};
/* Birden çok dinleyici (koç: bekleyenler + açtığı öğrencinin tüm soruları); sonuçlar birleştirilir */
function watchSorular(q, key="ana"){ if(SQK[key]) return; SQK[key] = {m:new Map()};
  const un = onSnapshot(q, snap=>{ SQK[key].m = new Map(snap.docs.map(d=>[d.id, d.data()])); S.sorular = new Map(Object.values(SQK).flatMap(x=>[...x.m])); render(true); }, e=>console.error("sorular", e));
  SQK[key].un = un; unsubs.push(un); }
function sorularOgrenci(sid_){ if(A()) watchSorular(query(collection(fdb,"sorular"), where("sid","==",sid_)), "o:"+sid_); }
const soruList = sid_ => [...S.sorular.entries()].filter(([,q])=>q.sid===sid_).sort((a,b)=>(b[1].at||"").localeCompare(a[1].at||""));
async function resimKucult(file, max, limit){ const img = await new Promise((res,rej)=>{ const i = new Image(); i.onload=()=>res(i); i.onerror=rej; i.src = URL.createObjectURL(file); });
  const k = Math.min(1, max/Math.max(img.width, img.height)), c = document.createElement("canvas"); c.width = Math.round(img.width*k); c.height = Math.round(img.height*k);
  const g = c.getContext("2d"); g.fillStyle = "#fff"; g.fillRect(0,0,c.width,c.height); g.drawImage(img, 0, 0, c.width, c.height);
  let q = .85, data = c.toDataURL("image/jpeg", q); while(data.length > limit && q > .45){ q -= .1; data = c.toDataURL("image/jpeg", q); }
  /* hâlâ büyükse (çok detaylı fotoğraf) boyutu da küçült; öğrenciye uyarı göstermeden sığdır */
  let w = c.width, h = c.height; while(data.length > limit && w > 480){ w = Math.round(w*.85); h = Math.round(h*.85); const c2 = document.createElement("canvas"); c2.width = w; c2.height = h; const g2 = c2.getContext("2d"); g2.fillStyle = "#fff"; g2.fillRect(0,0,w,h); g2.drawImage(c, 0, 0, w, h); data = c2.toDataURL("image/jpeg", .6); }
  return data; }
function startStudent(id){
  S.me=id; S.view="home"; S.day=today(); S.week=S.students.get(id) ? curStart(S.students.get(id)) : monday(new Date());
  girisKaydet();
}
/* Öğrencinin girişini kaydeder: son giriş saati + son 30 günün giriş günleri (15 dakikada en fazla bir yazma) */
function girisKaydet(){ if(S.role!=="student" || !S.me) return; const s = S.students.get(S.me); if(!s) return;
  const t = today(), son = Date.parse(s.sonGiris||"") || 0; if(s.lastSeen===t && Date.now()-son < 15*60e3) return;
  const gg = {...(s.girisGun||{})}; gg[t] = (gg[t]||0) + 1; const sinir = addDays(t,-30); Object.keys(gg).forEach(d=>{ if(d < sinir) delete gg[d]; });
  s.sonGiris = nowISO(); s.lastSeen = t; s.girisGun = gg; persistDoc("students", S.me); }
document.addEventListener("visibilitychange", ()=>{ if(document.visibilityState==="visible") girisKaydet(); });
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
  if(Notification.permission === "granted") return pushKayitli() ? "hazir" : "ac"; /* izin var ama cihaz bağlanmamışsa yine göster */
  return "ac";
}
const pushKayitli = () => { try{ return !!localStorage.getItem("zk-push"); }catch(e){ return true; } };
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
    let yeni = false; try{ yeni = localStorage.getItem("zk-push") !== token; localStorage.setItem("zk-push", token); }catch(e){}
    if(A()) await setDoc(doc(fdb, "coachDevices", token.slice(-40).replace(/[^A-Za-z0-9_-]/g,"_")), { token, at: nowISO(), ua: navigator.userAgent.slice(0,120) });
    else { const s = st(); if(s && !(s.bildirim && s.bildirim.tokens && s.bildirim.tokens[token])){ s.bildirim = s.bildirim || {}; s.bildirim.tokens = {...(s.bildirim.tokens||{}), [token]: nowISO()}; s.bildirim.izin = "granted"; save(); } }
    if(yeni) render(true);
  }catch(e){ console.warn("push yenileme", e); }
}
function pushCard(){
  const k = pushState(); if(!k || k === "hazir") return "";
  if(k === "ios") return `<div class="card" style="background:var(--acs);border:0"><h3>${icon("bell","sm")} Bildirimleri almak için</h3><p class="muted small" style="margin:6px 0 0">iPhone’da önce uygulamayı ana ekrana ekle: Safari’de alttaki <b>Paylaş</b> simgesine dokun → <b>Ana Ekrana Ekle</b>. Sonra uygulamayı ana ekrandaki simgeden aç.</p></div>`;
  if(k === "red") return `<div class="card"><h3>${icon("bell","sm")} Bildirimler kapalı</h3><p class="muted small" style="margin:6px 0 0">Bildirim izni reddedilmiş. Açmak için telefonun ayarlarından bu uygulamanın bildirim iznini aç.</p></div>`;
  return `<div class="card pushbar"><span class="pbi">${icon("bell","sm")}</span><div style="min-width:0;flex:1"><b>Bildirimler kapalı</b><div class="small muted">${A()?"Yeni başvuru ve ödeme bildirimleri bu cihaza gelsin.":"Koçunun mesajları ve hatırlatmalar telefonuna gelsin."}</div></div><button class="btn sm pri" data-act="pushon">Aç</button></div>`;
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
/* ---------- Giriş takibi (koç) ---------- */
function girisGunleri(s){ const g = new Set(Object.keys(s.girisGun||{})); if(s.lastSeen) g.add(s.lastSeen);
  Object.entries(s.gunluk||{}).forEach(([d,m])=>{ if(m>0) g.add(d); }); return g; }
function girisDurum(s){ const son = s.sonGiris || "", gun = s.lastSeen || ([...girisGunleri(s)].sort().pop() || "");
  if(!son && !gun) return {k:"hic", gun:null, yazi:"Hiç girmedi"};
  const g = son ? iso(new Date(son)) : gun, fark = Math.round((new Date(today()+"T12:00:00")-new Date(g+"T12:00:00"))/864e5);
  const saat = son && iso(new Date(son))===g ? " "+new Date(son).toLocaleTimeString("tr-TR",{hour:"2-digit",minute:"2-digit"}) : "";
  const yazi = fark<=0 ? "Bugün"+saat : fark===1 ? "Dün"+saat : `${fark} gün önce`;
  return {k: fark<=1 ? "iyi" : fark<3 ? "orta" : "kotu", gun:fark, yazi}; }
function girisHatirlat(x, d){ const ad = ilkAd(x.name);
  return d.k==="hic" ? girisMesaj(x) : `Merhaba ${ad} 👋 ${d.gun} gündür Zekacademy uygulamasına girmediğini gördüm. Bugünkü görevlerine bir göz atıp çalıştıklarını işaretler misin? Bir sorun varsa yaz, birlikte çözelim 💪`; }
function cGiris(){ const t = today(), gunler = [...Array(14)].map((_,i)=>addDays(t, i-13));
  const L = sortedStudents().map(([id,x])=>({id, x, d:girisDurum(x)}));
  const sira = {hic:0, kotu:1, orta:2, iyi:3}; L.sort((a,b)=> sira[a.d.k]-sira[b.d.k] || (b.d.gun??0)-(a.d.gun??0) || a.x.name.localeCompare(b.x.name,"tr"));
  const bugun = L.filter(r=>r.d.gun===0).length, kotu = L.filter(r=>r.d.k==="kotu").length, hic = L.filter(r=>r.d.k==="hic").length;
  const satir = ({id,x,d}) => { const G = girisGunleri(x), uyar = d.k==="kotu" || d.k==="hic";
    return `<div class="gtrow"><button class="gtad" data-act="open" data-id="${id}"><b>${esc(x.name)}</b><span class="small muted">@${esc(x.kullanici||"—")}${x.ilkSifre?" · ilk şifre değişmedi":""}</span></button>
      <div class="gtsag"><span class="gtdur ${d.k}">${d.yazi}</span><div class="gtserit" aria-label="Son 14 gün">${gunler.map(g=>`<i class="${G.has(g)?"on":""} ${g===t?"bug":""}" title="${trDate(g)}${G.has(g)?" · girdi":""}"></i>`).join("")}</div></div>
      ${uyar && x.tel ? `<a class="btn sm" href="${esc(waLink(x.tel, girisHatirlat(x,d)))}" target="_blank" rel="noopener" title="WhatsApp'tan hatırlat">${icon("chat","xs")}</a>` : `<span class="gtbos"></span>`}</div>`; };
  return `${topbar(`<h1 class="ttl">Giriş takibi</h1>`, "", `<button class="iconbtn" data-act="go" data-v="daha" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page wide">
    <div class="kpis kp3">${tile("t-g","users",`${bugun}/${L.length}`,"Bugün giren")}${tile("t-r","flame",kotu,"3+ gündür girmeyen")}${tile("t-w","eye",hic,"Hiç girmeyen")}</div>
    <div class="card" style="padding:0">${L.length ? L.map(satir).join("") : `<div class="empty">Henüz öğrenci yok.</div>`}</div>
    <p class="faint small" style="text-align:center">Şeritte son 14 gün var; dolu kutular öğrencinin uygulamayı açtığı günler. Saat bilgisi bu güncellemeden sonraki girişlerde görünür.</p>
  </div>`; }
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
const tile = (cls, ic, val, lbl, id="", act="") => act ? `<button class="tile ${cls} tbtn" ${act}><div class="ic">${icon(ic,"sm")}</div><b class="num" ${id?`id="${id}"`:""}>${val}</b><span>${lbl}</span></button>`
  : `<div class="tile ${cls}"><div class="ic">${icon(ic,"sm")}</div><b class="num" ${id?`id="${id}"`:""}>${val}</b><span>${lbl}</span></div>`;
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
    renderAuth(); if(window.acilisBitir) window.acilisBitir(); return;
  }
  if(!S.ready){ root.innerHTML = `<div class="auth"><div class="apanel" style="align-items:center;padding-top:30vh"><div class="lm" style="width:56px;height:56px;border-radius:16px">${LOGO}</div><p class="muted">Panelin açılıyor…</p></div></div>`; return; }
  if(S.role==="student" && !S.students.has(S.me)){ root.innerHTML = `<div class="auth"><div class="apanel" style="padding-top:20vh"><h2>Kaydın bulunamadı</h2><p class="muted">Hesabına ait öğrenci kaydı silinmiş olabilir. Koçunla iletişime geç.</p><button class="btn" data-act="logout">Çıkış yap</button></div></div>`; return; }
  if(S.role==="student" && st().ilkSifre){ renderFirstPassword(); return; }
  if(fromSnap && document.activeElement && root.contains(document.activeElement) && document.activeElement.matches("input[type=text],input[type=number],textarea,select")) return;
  const y = window.scrollY, acik = new Set([...root.querySelectorAll("details[data-key][open]")].map(d=>d.dataset.key));
  root.innerHTML = A() ? coachShell() : studentShell();
  if(window.acilisBitir) window.acilisBitir();
  tlBoyut(root);
  if(acik.size) root.querySelectorAll("details[data-key]").forEach(d=>{ if(acik.has(d.dataset.key)) d.open = true; }); /* açık bölümler dokununca kapanmasın */
  const sayfa = [S.role, S.view, S.dtab, S.cur, S.gday, S.pmode, S.ex, S.mx, S.btab].join("|"); /* sayfa değişince hafif geçiş */
  if(!fromSnap && sayfa !== S._sayfa){ const sh = root.querySelector(".shell"); if(sh && S._sayfa) sh.classList.add("pgin"); }
  S._sayfa = sayfa;
  window.scrollTo(0, y);
}
function navHTML(items){
  const nb = ([v,ic,l,fab,cnt]) => `<button class="nb ${fab?"fab":""}" data-act="go" data-v="${v}" aria-current="${(S.view===v || (v==="ogren" && !A() && ["konular","cetele","sorular","socoz","banka","videolar"].includes(S.view)))?"page":"false"}" ${fab?`aria-label="${l}"`:""}>${fab?`<span class="bub">${icon(ic)}</span>`:icon(ic)}<span class="l">${l}</span>${cnt?`<span class="cnt">${cnt}</span>`:""}</button>`;
  return `<nav class="nav" aria-label="Menü"><div class="navin"><div class="navpill">${items.filter(x=>!x[3]).map(nb).join("")}</div>${items.filter(x=>x[3]).map(nb).join("")}</div></nav>`;
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
/* ---------- İlk açılışta uygulama tanıtımı (öğrenci) ---------- */
const TUR = [
  {nav:null, ic:"grad", b:"Hoş geldin {Ad}! 👋", t:"Bu uygulama koçunla senin ortak defterin. Programın, hedeflerin, denemelerin ve çalışma sürelerin burada. Koçun yaptığın her şeyi anında görür. Hadi 1 dakikada tanıyalım."},
  {nav:"home", ic:"home", b:"Bugünün görevleri", t:"Ana sayfada bugün yapacakların sıralı. Derse başlarken görevin yanındaki ▶ ile sayacı başlat, ara verirken “Durdur”a bas; süren kaydedilir. Görevi bitirince yuvarlağa dokun, yeşil olsun.", ornek:"gorev"},
  {nav:"home", ic:"target", b:"Görevin altındaki küçük yazı", t:"Her dersin altında o hafta bitireceğin konu 🎯, takip edeceğin kitap 📖 ve hoca 👥 yazar. Paragraf ve problemde “Günlük rutin” yazar.", ornek:"hedef"},
  {nav:"program", ic:"cal", b:"Haftalık Program", t:"Ortadaki yeşil düğme. Üstteki günlere dokunarak başka günlere geç; “Haftalık”ta bütün haftayı ve hedeflerini görürsün. Hedef konuyu bitirince onu da işaretle."},
  {nav:"daha", ic:"timer", b:"Çalışma süresi", t:"Daha Fazla → Kronometre. Derse başlarken başlat, bitince durdur. Unutursan süreyi elle de yazabilirsin. Örneğin: bugün 5 saat 30 dakika.", ornek:"sure"},
  {nav:"analiz", ic:"chart", b:"Denemeler ve analiz", t:"Her denemeden sonra netlerini gir; altta yanlış yaptığın konuları da seç, çeteleye kendiliğinden eklenir. Üstteki takvim simgesinde yaklaşan Türkiye geneli denemeler var."},
  {nav:"ogren", ic:"book", b:"Öğrenme Merkezi", t:"Öğren sekmesinde soru çözme, ders videoları, kartlar ve araçların bir arada. Konu Takibi’nde bir konuyu tekrar ettikçe tekrar sayısını artır, 1. ve 2. soru bankasını bitirince işaretle. Üçü tamamlanan konu yeşil olur.", ornek:"konu"},
  {nav:"ogren", ic:"list", b:"Yanlış çetelesi", t:"Öğren → Yanlış Çetelesi. Soru çözerken yanlış yaptığın konuya +1 ekle. Örneğin Basınç’tan 3 yanlış → +3. Yanlışı çok olan konular programına tekrar olarak gelir."},
  {nav:"ogren", ic:"note", b:"Hata Defteri", t:"Öğren → Hata Defteri. Çözemediğin sorunun fotoğrafını çek, dersini seç. Soru Çözüm’le adım adım çöz, anladığında “çözüldü” yap."},
  {nav:"daha", ic:"bell", b:"Bildirimler ve koçundan notlar", t:"Sabah motivasyon mesajı, akşam eksik hatırlatması ve görüşme hatırlatması gelir. Telefon izin isterse “İzin ver”e bas. Koçunun notları da burada."},
  {nav:null, ic:"check", b:"Hazırsın! 🎯", t:"Her gün görevlerini işaretle, süreni gir, haftada bir denemeni ekle. Bu tanıtımı Daha Fazla → “Uygulamayı tanı”dan istediğin zaman tekrar açabilirsin."} ];
/* Mevcut öğrencilere bir kerelik "Yenilikler" tanıtımı (sürüm değişince yeniden çıkar) */
const YENILIK_SURUM = "2026-11-01";
const YENILIK = [
  {nav:null, ic:"flame", b:"Uygulamada yenilikler var! 🎉", t:"{Ad}, senin için birkaç yeni özellik ekledik. 30 saniyede göstereyim."},
  {nav:"home", ic:"timer", b:"Görev sayacı", t:"Derse başlarken görevin yanındaki ▶’ye bas, sayaç başlasın. Ara verirken “Durdur”a bas; süren kendiliğinden kaydedilir. Görevi bitirince yuvarlağa dokun. Hangi derse ne kadar çalıştığını Kronometre’de görürsün.", ornek:"sayac"},
  {nav:"home", ic:"target", b:"TYT mi AYT mi, hemen gör", t:"Görevin altındaki konu ve kitap artık görevin sınavına göre: AYT Matematik görevinde sadece AYT konuları ve kitapları yazar.", ornek:"hedef2"},
  {nav:"analiz", ic:"chart", b:"Denemede yanlış konular", t:"Deneme eklerken altta yanlış yaptığın konuları seç; çeteleye kendiliğinden eklenir, ayrıca uğraşmazsın.", ornek:"yanlis"},
  {nav:"home", ic:"cal", b:"Deneme takvimi", t:"Yaklaşan Türkiye geneli denemeler ve yazılıların ana sayfanda. Tüm takvim Analiz’deki takvim simgesinde."},
  {nav:"ogren", ic:"note", b:"Hata Defteri", t:"Öğren → Hata Defteri. “Kamerayı aç” ile çözemediğin soruyu çek, dersini seç. Soru Çözüm’le adım adım çözebilirsin."},
  {nav:null, ic:"check", b:"Hepsi bu kadar 👍", t:"Kolay gelsin! Tanıtımları Daha Fazla → “Uygulamayı tanı”dan tekrar açabilirsin."} ];
const turListe = () => S.turListe==="yeni" ? YENILIK : TUR;
function turOrnek(k){
  if(k==="sayac") return `<div class="tasks turex"><div class="task"><span class="tick">${icon("check","sm")}</span><div><div class="tt" style="font-weight:600">TYT Kimya Çalışması (1,5 saat)</div></div><div class="tright"><span class="pill">${icon("clock","xs")}1,5 saat</span><span class="tplay">${icon("play","xs")}</span></div></div><div class="task running"><span class="tick">${icon("check","sm")}</span><div><div class="tt" style="font-weight:600">AYT Fizik Çalışması (2 saat)</div><div class="trun"><span class="tlive num">24:10</span><span class="btn sm">${icon("stop","xs")} Durdur</span></div></div><span></span></div></div>`;
  if(k==="hedef2") return `<div class="tasks turex"><div class="task"><span class="tick">${icon("check","sm")}</span><div><div class="tt" style="font-weight:600">AYT Matematik Çalışması (2 saat)</div><div class="thd"><span>${icon("target","xs")}Türev</span><span>${icon("book","xs")}Apotemi + Bilgi Sarmal</span><span>${icon("users","xs")}Mert Hoca</span></div></div><span></span></div></div>`;
  if(k==="yanlis") return `<div class="turex" style="padding:8px 10px"><div class="dykr on"><span>Basınç</span><span class="mini">−</span><b class="num">2</b><span class="mini">+</span></div><div class="dykr"><span>Paragrafta Anlam</span><span class="mini">−</span><b class="num">0</b><span class="mini">+</span></div></div>`;
  if(k==="gorev") return `<div class="tasks turex"><div class="task done"><span class="tick" aria-pressed="true">${icon("check","sm")}</span><div><div class="tt" style="font-weight:600">Paragraf 20 soru</div></div><span></span></div><div class="task"><span class="tick">${icon("check","sm")}</span><div><div class="tt" style="font-weight:600">TYT Matematik Çalışması (2,5 saat)</div></div><span class="pill">${icon("clock","xs")}2,5 saat</span></div></div>`;
  if(k==="hedef") return `<div class="tasks turex"><div class="task"><span class="tick">${icon("check","sm")}</span><div><div class="tt" style="font-weight:600">AYT Fizik Konu Soru Çalışması (2 saat)</div><div class="thd"><span>${icon("target","xs")}Basit Harmonik Hareket</span><span>${icon("book","xs")}345 + Bilgi Sarmal</span><span>${icon("users","xs")}Özcan Aykın</span></div></div><span></span></div></div>`;
  if(k==="sure") return `<div class="turex turbig"><b class="num">5 sa 30 dk</b><span class="muted small">bugün çalıştın · hedef 7,5 saat</span></div>`;
  if(k==="konu") return `<div class="turex turkonu"><span>Basınç</span><span class="pill">2 tekrar</span><span class="pill ac">SB1 ✓</span><span class="pill ac">SB2 ✓</span></div>`;
  return ""; }
function turHTML(s){ const L = turListe(), i = S.tur, a = L[i]; if(!a) return "";
  return `<div class="turov" role="dialog" aria-modal="true" aria-label="Uygulama tanıtımı"><div class="turkart">
    <div class="turust"><span class="turic">${icon(a.ic)}</span><span class="faint small">${i+1} / ${L.length}</span><button class="link small" data-act="turbitir">Atla</button></div>
    <h2>${esc(a.b.replaceAll("{Ad}", ilkAd(s.name)))}</h2><p>${esc(a.t.replaceAll("{Ad}", ilkAd(s.name)))}</p>${a.ornek?turOrnek(a.ornek):""}
    <div class="turnok">${L.map((_,k)=>`<i class="${k===i?"on":""}"></i>`).join("")}</div>
    <div class="acts">${i?`<button class="btn" data-act="tur" data-v="${i-1}">Geri</button>`:""}<button class="btn pri" data-act="${i===L.length-1?"turbitir":"tur"}" data-v="${i+1}">${i===L.length-1?(S.turListe==="yeni"?"Tamam":"Başlayalım"):"İleri"}</button></div></div></div>`; }
function studentShell(){
  const s = st(); if(!s) return "";
  if(S.tur==null && !s.tanitim && !S.turKapandi){ S.turListe = "tur"; S.tur = 0; }
  else if(S.tur==null && s.tanitim && s.yenilik!==YENILIK_SURUM && !S.turKapandi){ S.turListe = "yeni"; S.tur = 0; }
  const pages = {home:sHome, ogren:()=>pOgren(s), videolar:()=>pVideolar(s), banka:()=>pBanka(s), socoz:pSoruCoz, program:()=>pProgram(s,false), analiz:()=>pAnaliz(s), konular:()=>pKonular(s), daha:sMore, cetele:()=>pCetele(s), kronometre:()=>pCalisma(s), bildirim:sBell, sorular:()=>pSorular(s, S.me)};
  const nots = studentNotices(s).length;
  return `<div class="shell">${(pages[S.view]||sHome)(s)}</div>` + navHTML([["home","home","Ana Sayfa"],["analiz","chart","Analiz"],["program","cal","Haftalık Program",true],["ogren","book","Öğren"],["daha","more","Daha Fazla", false, 0]]).replace(/(data-v="([a-z]+)")/g, (m, a, v)=> S.tur!=null && turListe()[S.tur]?.nav===v ? a+' data-tur="1"' : a) + (S.tur!=null ? turHTML(s) : "");
}
/* ---------- Deneme takvimi (Ayarlar'dan düzenlenir) + öğrencinin yazılıları ---------- */
const DEF_TAKVIM = [{"bas":"2026-09-18","bit":"2026-09-19","yayin":"ÖZDEBİR","ad":"TYT İlk Prova"},{"bas":"2026-10-02","bit":"2026-10-05","yayin":"4K Yayınları","ad":"TYT Türkiye Geneli 1"},{"bas":"2026-10-16","bit":"2026-10-19","yayin":"ÖZDEBİR","ad":"YKS Türkiye Geneli 1"},{"bas":"2026-10-23","bit":"2026-10-26","yayin":"3D Yayınları","ad":"TYT Türkiye Geneli 1"},{"bas":"2026-11-09","bit":"2026-11-15","yayin":"MEBİ","ad":"YKS Denemesi 3"},{"bas":"2026-12-04","bit":"2026-12-07","yayin":"ÖZDEBİR","ad":"YKS Türkiye Geneli 2"},{"bas":"2026-12-10","bit":"2026-12-13","yayin":"Supara","ad":"TYT-AYT Türkiye Geneli 1"},{"bas":"2026-12-11","bit":"2026-12-14","yayin":"4K Yayınları","ad":"TYT Türkiye Geneli 2"},{"bas":"2026-12-14","bit":"2026-12-20","yayin":"MEBİ","ad":"YKS Denemesi 4"},{"bas":"2026-12-25","bit":"2026-12-28","yayin":"3D Yayınları","ad":"TYT Türkiye Geneli 2"},{"bas":"2027-01-08","bit":"2027-01-11","yayin":"ÖZDEBİR","ad":"YKS Türkiye Geneli 3"},{"bas":"2027-01-08","bit":"2027-01-11","yayin":"4K Yayınları","ad":"Maarif TYT"},{"bas":"2027-01-11","bit":"2027-01-17","yayin":"MEBİ","ad":"YKS Denemesi 5"},{"bas":"2027-02-15","bit":"2027-02-21","yayin":"MEBİ","ad":"YKS Denemesi 6"},{"bas":"2027-02-19","bit":"2027-02-22","yayin":"Hız ve Renk","ad":"TYT-AYT Türkiye Geneli 1"},{"bas":"2027-02-26","bit":"2027-03-01","yayin":"ÖZDEBİR","ad":"YKS Türkiye Geneli 4"},{"bas":"2027-03-15","bit":"2027-03-21","yayin":"MEBİ","ad":"YKS Denemesi 7"},{"bas":"2027-03-26","bit":"2027-03-29","yayin":"3D Yayınları","ad":"TYT-AYT Türkiye Geneli 3"},{"bas":"2027-04-02","bit":"2027-04-05","yayin":"ÖZDEBİR","ad":"YKS Türkiye Geneli 5"},{"bas":"2027-04-09","bit":"2027-04-12","yayin":"4K Yayınları","ad":"TYT-AYT Türkiye Geneli 3"},{"bas":"2027-04-12","bit":"2027-04-18","yayin":"MEBİ","ad":"YKS Denemesi 8"},{"bas":"2027-04-16","bit":"2027-04-19","yayin":"Hız ve Renk","ad":"TYT-AYT Türkiye Geneli 2"},{"bas":"2027-05-07","bit":"2027-05-10","yayin":"ÖZDEBİR","ad":"YKS Türkiye Geneli 6"},{"bas":"2027-05-10","bit":"2027-05-16","yayin":"MEBİ","ad":"YKS Denemesi 9"},{"bas":"2027-05-17","bit":"2027-05-23","yayin":"MEBİ","ad":"YKS Denemesi 10"},{"bas":"2027-05-28","bit":"2027-05-31","yayin":"3D Yayınları","ad":"TYT-AYT Türkiye Geneli 4"},{"bas":"2027-05-31","bit":"2027-06-06","yayin":"MEBİ","ad":"YKS Denemesi 11"},{"bas":"2027-06-04","bit":"2027-06-07","yayin":"ÖZDEBİR","ad":"YKS Türkiye Geneli 7"},{"bas":"2027-06-07","bit":"2027-06-10","yayin":"4K Yayınları","ad":"TYT-AYT Türkiye Geneli 4"},{"bas":"2027-06-07","bit":"2027-06-13","yayin":"MEBİ","ad":"YKS Denemesi 12"},{"bas":"2027-06-08","bit":"2027-06-11","yayin":"Supara","ad":"TYT-AYT Türkiye Geneli 2"}];
const takvim = () => (Array.isArray(S.settings.takvim) ? S.settings.takvim : DEF_TAKVIM).filter(x=>x && x.bas).slice().sort((a,b)=>a.bas.localeCompare(b.bas));
function yaklasan(s, gun){ const t = today(), son = addDays(t, gun); const L = takvim().filter(x=>(x.bit||x.bas) >= t && x.bas <= son).map(x=>({...x, tip:"deneme"}));
  Object.values(s.plan||{}).forEach(p=>(p.yazilar||[]).forEach(y=>{ if(y.tarih && y.tarih >= t && y.tarih <= son) L.push({bas:y.tarih, bit:y.tarih, yayin:"Yazılı", ad:y.ders, tip:"yazili"}); }));
  return L.sort((a,b)=>a.bas.localeCompare(b.bas)); }
const tarihAralik = x => x.bit && x.bit!==x.bas ? `${shortDate(x.bas)} – ${shortDate(x.bit)}` : shortDate(x.bas);
function takvimSatir(x){ const t = today(), aktif = x.bas <= t && (x.bit||x.bas) >= t, kalan = gunFark(x.bas, t);
  return `<div class="tkr ${x.tip==="yazili"?"yz":""} ${aktif?"akt":""}"><span class="tkd"><b class="num">${new Date(x.bas+"T12:00:00").getDate()}</b><small>${AYK[new Date(x.bas+"T12:00:00").getMonth()]}</small></span>
    <div style="min-width:0;flex:1"><b>${x.tip==="yazili"?"📝 "+esc(x.ad)+" yazılısı":esc(x.yayin)+" · "+esc(x.ad)}</b><div class="small muted">${tarihAralik(x)}${aktif?` · <b style="color:var(--ac)">bu günlerde</b>`:kalan>0?` · ${kalan} gün kaldı`:""}</div></div></div>`; }
function takvimKart(s, gun, baslik){ const L = yaklasan(s, gun); if(!L.length) return "";
  return `<div class="card"><div class="sech"><h3>${baslik||"Yaklaşan denemeler"}</h3><button class="link" data-act="sheet" data-v="takvim">Tüm takvim</button></div><div class="tkl">${L.slice(0,4).map(takvimSatir).join("")}</div></div>`; }
function sHome(s){
  const t = today(), tl = dayTasks(s,t), done = tl.filter(x=>x.done).length;
  const w = weekStats(s, curStart(s));
  const lt = exams(s,"TYT").pop();
  const h = new Date().getHours();
  const nots = studentNotices(s);
  const msg = !tl.length ? "Bugün için görev yok, kronometreyle çalışmanı kaydedebilirsin." : done===tl.length ? "Bugünün tüm görevleri tamam. Harikasın!" : done ? `${done} görevi tamamladın, devam!` : "Hadi ilk görevle başlayalım.";
  const ev = eveningMsg(s), mm = ev ? null : morningMsg(s, S.me);
  const PD = pDays(s, curStart(s)), tyt = exams(s,"TYT").slice(-5), tmx = Math.max(60, ...tyt.map(tytTotal));
  return `<header class="hhead"><div class="hhin">
      <div class="hrow"><span class="hav">${esc(initials(s.name))}</span><div class="hname"><span>Merhaba <b>${esc(firstName(s.name))}</b></span><small>${longToday()}</small></div><span class="spacer"></span>
        <span class="hchip" title="Çalışma serisi">${icon("flame","xs")}<b class="num">${streak(s)}</b></span>${temaBtn()}${bellBtn(nots.length)}</div>
      <div class="wstrip">${PD.map(d=>{ const l = dayTasks(s,d), dn = l.filter(x=>x.done).length;
        return `<button class="dbtn ${d===t?"today":""}" data-act="hgun" data-v="${d}" style="--p:${l.length?Math.round(dn/l.length*100):0}">${GUNK[dIdx(d)]}<b class="num">${dNum(d)}</b>${l.length?`<i class="${dn===l.length?"":"p"}"></i>`:""}</button>`; }).join("")}</div>
    </div></header>
  <div class="page">
    ${pushCard()}
    ${yaziliKart(s, curStart(s), false)}
    ${ev?`<div class="card evening"><div class="sech"><h3>${icon("moon","sm")} Koçundan akşam hatırlatması</h3></div><p style="margin:8px 0 12px;font-weight:600">${esc(ev.text)}</p><div class="pills">${ev.missTasks?`<button class="btn sm pri" data-act="go" data-v="program">${icon("check","xs")} Görevleri işaretle</button>`:""}${ev.missTime?`<button class="btn sm ${ev.missTasks?"":"pri"}" data-act="go" data-v="kronometre">${icon("timer","xs")} Süremi gir</button>`:""}</div></div>`:""}
    ${mm?`<div class="card morning"><div class="sech"><h3>${icon("sun","sm")} Günün mesajı</h3><span class="faint small">Koçundan</span></div><p style="margin:8px 0 0;font-weight:600;font-size:16px;line-height:1.5">${esc(mm)}</p></div>`:""}
    ${aiAcik(S.me) ? `<button class="szhome" data-act="go" data-v="socoz"><span class="szhi">${icon("search")}</span><span><b>Soru Çözüm</b><small>Takıldığın soruyu fotoğrafla, adım adım birlikte çözelim</small></span>${s.aiBonus && s.aiBonus.at > (s.aiBonusGoruldu||"") ? `<span class="szyeni">🎉 Bonus</span>` : icon("chev","sm")}</button>` : ""}
    <div class="duo">
      <div class="dcard2"><button class="dch" data-act="go" data-v="program"><b>Bugünkü Program</b>${icon("chev","sm")}</button><p>${msg}</p>
        <div class="dil">${ring(tl.length?done/tl.length:0, `${done}/${tl.length}`)}</div>
        <button class="btn pri full" data-act="go" data-v="program">${done && done===tl.length ? "Programa bak" : "Göreve başla"}</button></div>
      <div class="dcard2"><button class="dch" data-act="go" data-v="analiz"><b>Denemelerim</b>${icon("chev","sm")}</button><p>${lt?`Son TYT <b class="num">${fmt(tytTotal(lt))}</b> net`:"İlk denemeni ekle, gelişimini birlikte izleyelim."}</p>
        <div class="dil"><div class="mbars">${tyt.length ? tyt.map((d,i)=>`<i style="height:${Math.max(12,tytTotal(d)/tmx*100)}%" class="${i===tyt.length-1?"son":""}"><em class="num">${fmt(tytTotal(d))}</em></i>`).join("") : `<span class="mbos">${icon("chart")}</span>`}</div></div>
        <button class="btn pri full" data-act="sheet" data-v="deneme">Deneme ekle</button></div>
    </div>
    <div class="sec">Araçlar</div>
    <div class="arac">
      <button data-act="go" data-v="kronometre"><span>${icon("timer")}</span>Kronometre</button>
      <button data-act="go" data-v="sorular"><span>${icon("search")}</span>Sorularım</button>
      <button data-act="go" data-v="cetele"><span>${icon("list")}</span>Çetele</button>
      <button data-act="go" data-v="konular"><span>${icon("book")}</span>Konular</button>
    </div>
    ${bugunDersKart(s)}
    <div class="card" id="gorevler"><div class="sech"><h3>Bugünün Görevleri</h3><button class="link" data-act="go" data-v="program">Tümünü gör</button></div>
      <div class="tasks" style="margin-top:6px">${tl.length? tl.map(x=>taskRow(x,t,{canTick:true, s})).join("") : `<div class="empty">Koçun bugüne görev eklemedi.</div>`}</div></div>
    <div class="tiles">
      ${tile("t-g","clock",fmtMin(minutes(s,t)),dayTarget(s,t)?`Bugün çalışma · hedef ${fmtH(dayTarget(s,t))}`:"Bugün çalışma","liveMin",`data-act="git" data-v="kronometre" data-hedef="calisma"`)}
      ${tile("t-a","check",`${done}/${tl.length}`,"Görev tamamlandı","",`data-act="kaydir" data-hedef="gorevler"`)}
      ${tile("t-w","target",w.pct==null?"—":"%"+Math.round(w.pct*100),"Haftalık program uyumu","",`data-act="git" data-v="program" data-mod="hafta"`)}
      ${tile("t-r","clock",fmtMin(w.min),"Bu hafta toplam çalışma")}
    </div>
    ${goalsCard(s, curStart(s), {compact:true})}
    ${takvimKart(s, 45)}
    ${s.koctanNot&&s.koctanNot.text?`<div class="card note"><span class="av">${icon("grad","sm")}</span><div style="min-width:0"><div class="sech"><b>Koçundan not</b><span class="faint small">${s.koctanNot.date?shortDate(s.koctanNot.date.slice(0,10)):""}</span></div><p style="margin:4px 0 0;white-space:pre-wrap">${esc(s.koctanNot.text)}</p></div></div>`:""}
  </div>`;
}
function sBell(s){
  const n = studentNotices(s);
  if(s.koctanNot && s.koctanNot.date && s.koctanNot.date > (s.notSeen||"")){ s.notSeen = s.koctanNot.date; save(); }
  return `${topbar(`<h1 class="ttl">Bildirimler</h1>`, "", `<button class="iconbtn" data-act="go" data-v="home" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page"><div class="card">${n.length? n.map(([ic,t,d])=>`<div class="row"><span class="ri">${icon(ic,"sm")}</span><div style="min-width:0"><div class="rt">${esc(t)}</div><div class="rs">${esc(d)}</div></div></div>`).join("") : `<div class="empty">Şimdilik yeni bir şey yok.</div>`}</div>
  <p class="faint small" style="text-align:center">Bildirimleri açtıysan hatırlatmalar telefonuna da gelir.</p></div>`;
}
/* ---------- Takıldığım sorular (öğrencinin havuzu; koç da görür) ---------- */
function soruKart(id, q){ return `<button class="sqk ${q.durum==="cozuldu"?"ok":""}" data-act="sheet" data-v="soru" data-id="${id}">${q.thumb?`<img src="${q.thumb}" alt="">`:`<span class="sqph">${icon("note")}</span>`}
  <span class="sqm"><b data-c="${dersKodu(q.ders||"")}">${esc(q.ders||"Soru")}</b>${q.konu?`<span>${esc(q.konu)}</span>`:""}<small>${shortDate((q.at||"").slice(0,10))}${q.durum==="cozuldu"?" · ✓ çözüldü":""}${q.kocNot?" · 💬":""}</small></span></button>`; }
function pSorular(s, sid_){ const L = soruList(sid_), f = S.sqf || "bekliyor", G = L.filter(([,q])=> f==="tum" || (f==="cozuldu" ? q.durum==="cozuldu" : q.durum!=="cozuldu"));
  const bek = L.filter(([,q])=>q.durum!=="cozuldu").length;
  const head = A() ? "" : topbar(`<h1 class="ttl">Hata Defteri</h1>`, `<button class="iconbtn" data-act="sheet" data-v="soruekle" aria-label="Soru ekle">${icon("plus")}</button>`, `<button class="iconbtn" data-act="go" data-v="ogren" aria-label="Geri">${icon("back")}</button>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    ${A()?"":`<div class="card note"><span class="av">❓</span><div><b>Çözemediğin soruyu biriktir</b><div class="muted small">Fotoğrafını çek, dersini seç. Soru Çözüm’le adım adım çöz, anladığında “çözüldü” yap. Testlerde yanlış yaptığın sorular da Öğrenme Merkezi’nde tekrar karşına çıkar.</div></div></div>
    <button class="btn full" data-act="go" data-v="socoz">📷 Soru Çözüm’le çöz</button>
    <button class="btn pri full" data-act="sheet" data-v="soruekle">${icon("plus","sm")} Soru ekle</button>
    ${(L=>L.length?`<div class="card"><div class="sech"><h3>Test ve soru bankası yanlışları</h3><span class="faint small">${L.length}</span></div>${L.map(h=>{ const c = DERS_ICERIK[h.k], x = h.bid ? BANKA.find(b=>b.id===h.bid) : c && c.test[h.i]; return x ? `<button class="row" ${h.bid?`data-bk="tek" data-id="${h.bid}"`:`data-ders="${esc(h.k)}" data-sekme="test"`}><span class="ri">❗</span><div style="min-width:0"><div class="rt">${esc(x.q)}</div><div class="rs">${h.tur&&NT[h.tur]?NT[h.tur][0]+" "+NT[h.tur][1]+" · ":""}${esc(konuAdi(h.k))} · ${h.sonraki<=today()?"tekrar zamanı geldi":h.sonraki===gunSonra(1)?"yarın tekrar karşına çıkacak":"tekrar: "+esc(h.sonraki.split("-").reverse().join("."))}</div></div><span class="rx">${icon("chev","sm")}</span></button>` : ""; }).join("")}</div>`:"")((og().hata||[]).filter(h=>!h.tamam))}`}
    <div class="seg"><button data-act="sqf" data-v="bekliyor" aria-pressed="${f==="bekliyor"}">Bekleyen ${bek}</button><button data-act="sqf" data-v="cozuldu" aria-pressed="${f==="cozuldu"}">Çözülen ${L.length-bek}</button><button data-act="sqf" data-v="tum" aria-pressed="${f==="tum"}">Tümü</button></div>
    ${G.length ? `<div class="sqgrid">${G.map(([id,q])=>soruKart(id,q)).join("")}</div>` : `<div class="empty">${L.length ? "Bu filtrede soru yok." : (A() ? "Öğrenci henüz soru eklemedi." : "Henüz soru eklemedin. Takıldığın ilk soruyu ekle.")}</div>`}
  </div>`; }
function sMore(s){
  return `${topbar(`<h1 class="ttl">Daha Fazla</h1>`)}
  <div class="page">
    <div class="card note"><span class="av">${esc(initials(s.name))}</span><div><b>${esc(s.name)}</b><div class="muted small">${esc(s.alan)} · ${esc(s.sinif)}${s.okul?" · "+esc(s.okul):""}</div><div class="faint small">@${esc(s.kullanici||"")}</div></div></div>
    <div class="card">
      <button class="row" data-act="go" data-v="kronometre"><span class="ri">${icon("timer","sm")}</span><div><div class="rt">Kronometre ve çalışma süresi</div><div class="rs">Bugün ${fmtMin(minutes(s,today()))}</div></div><span class="rx">${icon("chev","sm")}</span></button>
      ${aiAcik(S.me) ? `<button class="row" data-act="go" data-v="socoz"><span class="ri" style="background:var(--acs);color:var(--ac)">${icon("search","sm")}</span><div><div class="rt">Soru Çözüm</div><div class="rs">Fotoğrafla, yapay zekâ adım adım çözsün</div></div><span class="rx">${icon("chev","sm")}</span></button>` : ""}
      <button class="row" data-act="go" data-v="sorular"><span class="ri">${icon("note","sm")}</span><div><div class="rt">Hata Defteri</div><div class="rs">${(n=>n?`${n} soru bekliyor`:"Çözemediğin soruların fotoğrafını biriktir")(soruList(S.me).filter(([,q])=>q.durum!=="cozuldu").length)}</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="go" data-v="cetele"><span class="ri">${icon("list","sm")}</span><div><div class="rt">Yanlış çetelesi</div><div class="rs">Konu konu yanlışlarını işaretle</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="go" data-v="bildirim"><span class="ri">${icon("bell","sm")}</span><div><div class="rt">Bildirimler</div><div class="rs">Hatırlatmalar ve koçundan notlar</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="tur" data-v="0" data-l="tur"><span class="ri">${icon("grad","sm")}</span><div><div class="rt">Uygulamayı tanı</div><div class="rs">Kısa tanıtımı tekrar izle</div></div><span class="rx">${icon("chev","sm")}</span></button>
      <button class="row" data-act="tur" data-v="0" data-l="yeni"><span class="ri">${icon("flame","sm")}</span><div><div class="rt">Yenilikler</div><div class="rs">Son eklenen özellikler</div></div><span class="rx">${icon("chev","sm")}</span></button>
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
const hoca = (s,d) => (s.hocalar||{})[d] || "";
/* TYT ve AYT kitapları ayrı tutulan dersler (öğrencinin alanına göre); AYT kitabı "Ders|AYT" anahtarında */
const AYT_DERS = {SAY:["Matematik","Fizik","Kimya","Biyoloji"], EA:["Matematik","Tarih","Coğrafya"], "SÖZ":["Tarih","Coğrafya","Felsefe","Din Kültürü"]};
const ikiSinavli = (s, d) => !!s && !isMaarif(s) && (AYT_DERS[s.alan]||[]).includes(d);
const kitapK = (s, d, ex) => (s.kitaplar||{})[ex==="AYT" ? d+"|AYT" : d] || "";
/* Takip edilen kitap ve hocalar (ayarlardan düzenlenir). "# Başlık" satırları grup başlığıdır. */
/* Koçun kendi listesi + piyasada öne çıkan kaynaklar (TYT/AYT ayrı); "M:" ile başlayanlar Maarif (9–11. sınıf) listeleri */
const DEF_KAYNAK = {"Matematik":{"kitap":["# Sıfırdan başlayan","345 Start","Antremanlarla Matematik","Acil Matematiğin İlacı","Mikroorijinal","# Orta","345","Bilgi Sarmal","3D","Orijinal","Acil","# Üst düzey","Ergi","Apotemi","Barış","# Öne çıkanlar · TYT","Acil Matematik","345","Bilgi Sarmal","3D","Orijinal","Karekök","Apotemi","Endemik","Hız ve Renk","Yarı Çap","# Öne çıkanlar · AYT","Acil","Orijinal","Bilgi Sarmal","3D","Limit","Karekök","Apotemi","Endemik","345","Birey B"],"hoca":["# Senin listen","Mert Hoca","Bıyıklı Matematik","Rehber Matematik","Şenol Hoca","Eyüp B","SML Matematik","Yaşar Hoca","Mathman","# Öne çıkanlar · TYT","Şenol Hoca","Rehber Matematik","Mert Hoca","Eyüp B","Bıyıklı Matematik","Hocalara Geldik","Matematik Kafası","Ceyhun Hoca","Sıfırdan Sonsuza Matematik","Tonguç Akademi","# Öne çıkanlar · AYT","Mert Hoca","Şenol Hoca","Rehber Matematik","Eyüp B","Matematik Kafası","Selim Yavuz","Mete Ekol Hoca","Hocalara Geldik","Atlas Akademi","Şifreli Matematik"]},"M:Matematik":{"kitap":["# Maarif · öne çıkanlar","Acil","Orijinal (Mikro MÖF)","Palme","Paraf","Çap / Yarıçap","Bilgi Sarmal","Hız ve Renk","Karekök","Limit","Full Matematik"],"hoca":["# Maarif · öne çıkanlar","Şenol Hoca","Rehber Matematik","Mert Hoca","Eyüp B","Bıyıklı Matematik","Matematik Kafası","Sıfırdan Sonsuza Matematik","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Geometri":{"kitap":["# Sıfırdan başlayan","Geometrinin İlacı","Mikroorijinal","# Orta","345","Bilgi Sarmal","3D","Orijinal","Acil","# Öne çıkanlar · TYT ve AYT","Acil Geometri","345","Bilgi Sarmal","3D","Orijinal","Karekök","Apotemi","Endemik","Kenan Kara Geometri","Hız ve Renk"],"hoca":["# Senin listen","Mert Hoca","Bıyıklı Matematik","Rehber Matematik","Şenol Hoca","Eyüp B","SML Matematik","Yaşar Hoca","Mathman","# Öne çıkanlar · TYT ve AYT","Kenan Kara","Şenol Hoca","Rehber Matematik","Eyüp B","Mert Hoca","Bıyıklı Matematik","Hocalara Geldik","Mete Ekol Hoca","Atlas Akademi","Farklı Ders"]},"M:Geometri":{"kitap":["# Maarif · öne çıkanlar","Acil","Orijinal","Palme","Çap / Yarıçap","Bilgi Sarmal","Hız ve Renk","Karekök","Limit","Aydın","Paraf"],"hoca":["# Maarif · öne çıkanlar","Kenan Kara","Şenol Hoca","Rehber Matematik","Eyüp B","Bıyıklı Matematik","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Fizik":{"kitap":["# Senin listen","345","Bilgi Sarmal","3D","# Öne çıkanlar · TYT","345","Bilgi Sarmal","3D","Palme","Hız ve Renk","Esen","Aydın","Nihat Bilgin","Limit","Orijinal","# Öne çıkanlar · AYT","345","Bilgi Sarmal","3D","Palme","Esen","Aydın","Nihat Bilgin","Kafadengi","Limit","Acil"],"hoca":["# Senin listen","Özcan Aykın","Altuğ Güneş","VIP Fizik","Umut Öncül","# Öne çıkanlar · TYT","Özcan Aykın","Umut Öncül","Altuğ Güneş","VIP Fizik","Fizikle Barış (Barış Akıncıoğlu)","Ertan Sinan Şahin","Hocalara Geldik","Kolay Fizik","Papatya Hoca","Tonguç Akademi","# Öne çıkanlar · AYT","Özcan Aykın","Umut Öncül","Altuğ Güneş","VIP Fizik","Fizikle Barış (Barış Akıncıoğlu)","Ertan Sinan Şahin","Hocalara Geldik","Fizik Okulu","Kolay Fizik","Yener Hoca (Öğreten Olsa)"]},"M:Fizik":{"kitap":["# Maarif · öne çıkanlar","Orijinal","Aydın","Palme","Paraf","Çap","ENS","Bilgi Sarmal","Hız ve Renk","Limit","Karekök"],"hoca":["# Maarif · öne çıkanlar","Umut Öncül","Özcan Aykın","Fizikle Barış (Barış Akıncıoğlu)","Kolay Fizik","Papatya Hoca","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Kimya":{"kitap":["# Senin listen","Orbital","345","Bilgi Sarmal","3D","# Öne çıkanlar · TYT","Orbital","345","Bilgi Sarmal","3D","Palme","Hız ve Renk","Aydın","Miray","Limit","Ferrum","# Öne çıkanlar · AYT","Orbital","345","Bilgi Sarmal","3D","Palme","Ferrum","Miray","Aydın","Kafadengi","Esen"],"hoca":["# Senin listen","Görkem Şahin","Ferrum","Kimya Dersleri","# Öne çıkanlar · TYT ve AYT","Görkem Şahin","Kimya Adası","Kimya Özel","Hocalara Geldik","Ferrum","Kimya Dersleri","Bizim Hocalar Kimya","Atlas Akademi","Tonguç Akademi","Kampüs"]},"M:Kimya":{"kitap":["# Maarif · öne çıkanlar","Orijinal","Aydın","Palme","Paraf","Çap","ENS","Bilgi Sarmal","Hız ve Renk","Limit","Orbital"],"hoca":["# Maarif · öne çıkanlar","Görkem Şahin","Kimya Adası","Kimya Özel","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Biyoloji":{"kitap":["# Senin listen","Biyotik","345","Bilgi Sarmal","3D","# Öne çıkanlar · TYT","Biyotik","345","Bilgi Sarmal","3D","Palme","Hız ve Renk","Limit","Aydın","Esen","Orijinal","# Öne çıkanlar · AYT","Biyotik","345","Bilgi Sarmal","3D","Palme","Limit","Esen","Aydın","Kafadengi","Hız ve Renk"],"hoca":["# Senin listen","Betül Biyoloji","Biosem","Dr. Biyoloji","# Öne çıkanlar · TYT ve AYT","Dr. Biyoloji","Selin Hoca","Betül Biyoloji","Biosem","OnBilim Biyoloji","FUNDAmentals Biyoloji","Hocalara Geldik","Benim Hocam Biyoloji","Bekir Avşar","Barış Hoca Biyoloji"]},"M:Biyoloji":{"kitap":["# Maarif · öne çıkanlar","Biyotik","Orijinal","Aydın","Palme","Paraf","Çap","ENS","Bilgi Sarmal","Hız ve Renk","Limit"],"hoca":["# Maarif · öne çıkanlar","Dr. Biyoloji","Selin Hoca","OnBilim Biyoloji","Biosem","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Türkçe":{"kitap":["# Senin listen","345 1 Haftada Dil Bilgisi","Bilgi Sarmal","Limit","3D","# Öne çıkanlar · TYT","345","Bilgi Sarmal","3D","Limit","Palme","Hız ve Renk","Apotemi","ENS","Tümler","Paragrafik"],"hoca":["# Senin listen","Rüştü Hoca","Aker Hoca","Deniz Hoca","Emek Taştan","# Öne çıkanlar · TYT","Rüştü Hoca","Önder Hoca","Fulya Hoca","Harun Ardıç","Aker Hoca","Deniz Hoca","Emek Taştan","Benim Hocam Türkçe","Hocalara Geldik","Tonguç Akademi"]},"M:Türkçe":{"kitap":["# Maarif · öne çıkanlar","Limit","Bilgi Sarmal","Palme","Çap","ENS","Paraf","Hız ve Renk","Aydın","Tümler","Yediiklim"],"hoca":["# Maarif · öne çıkanlar","Rüştü Hoca","Önder Hoca","Fulya Hoca","Harun Ardıç","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Edebiyat":{"kitap":["# Senin listen","Limit","Bilgi Sarmal","# Öne çıkanlar · AYT","Limit","Bilgi Sarmal","345","3D","Palme","Hız ve Renk","Benim Hocam","Kültür","FDD","Yediiklim"],"hoca":["# Senin listen","Rüştü Hoca","Aker Hoca","Deniz Hoca","Emek Taştan","# Öne çıkanlar · AYT","Rüştü Hoca","Önder Hoca","Fulya Hoca","Harun Ardıç","Benim Hocam Edebiyat","Hocalara Geldik","Tonguç Akademi","Aker Hoca","Deniz Hoca","Emek Taştan"]},"M:Edebiyat":{"kitap":["# Maarif · öne çıkanlar","Limit","Bilgi Sarmal","Palme","Çap","ENS","Paraf","Hız ve Renk","Aydın","Tümler","Yediiklim"],"hoca":["# Maarif · öne çıkanlar","Rüştü Hoca","Önder Hoca","Fulya Hoca","Harun Ardıç","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Tarih":{"kitap":["# Senin listen","Zeduva","Limit","Bilgi Sarmal","# Öne çıkanlar · TYT ve AYT","Zeduva","Limit","Bilgi Sarmal","345","3D","Yediiklim","Kültür","Benim Hocam","Hız ve Renk","Palme"],"hoca":["# Senin listen","Tarihin Kodları","Soner Ardıç","# Öne çıkanlar · TYT ve AYT","Tarihin Kodları","Soner Ardıç","KR Akademi (Burak Ünsur)","Sadettin Akyayla","Selami Yalçın","Hocalara Geldik","Atlas Akademi","Online Derslerim","Tonguç Akademi","Kampüs"]},"M:Tarih":{"kitap":["# Maarif · öne çıkanlar","Limit","Bilgi Sarmal","Zeduva","Palme","Çap","ENS","Paraf","Hız ve Renk","Yediiklim","Aydın"],"hoca":["# Maarif · öne çıkanlar","Tarihin Kodları","KR Akademi (Burak Ünsur)","Sadettin Akyayla","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Coğrafya":{"kitap":["# Senin listen","Zeduva","Limit","Bilgi Sarmal","Haritalar Kitabı (Coğrafyanın Kodları)","# Öne çıkanlar · TYT ve AYT","Zeduva","Limit","Bilgi Sarmal","345","3D","Yediiklim","Benim Hocam","Haritalar Kitabı (Coğrafyanın Kodları)","Hız ve Renk","Palme"],"hoca":["# Senin listen","Coğrafyanın Kodları","# Öne çıkanlar · TYT ve AYT","Coğrafyanın Kodları","Bayram Meral","Yavuz Tuna","Sosyal Hocam","Coğrafya Cepte","Hocalara Geldik","Atlas Akademi","Tonguç Akademi","Kampüs","Limit Yayınları"]},"M:Coğrafya":{"kitap":["# Maarif · öne çıkanlar","Limit","Bilgi Sarmal","Zeduva","Palme","Çap","ENS","Paraf","Hız ve Renk","Yediiklim","Aydın"],"hoca":["# Maarif · öne çıkanlar","Coğrafyanın Kodları","Bayram Meral","Yavuz Tuna","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Felsefe":{"kitap":["# Senin listen","Bilgi Sarmal","Limit","# Öne çıkanlar · TYT ve AYT","Bilgi Sarmal","Limit","345","3D","Palme","Yediiklim","Benim Hocam","Hız ve Renk","Kültür","Zeduva"],"hoca":["# Senin listen","Felsefe Atölyesi","# Öne çıkanlar · TYT ve AYT","Felsefe Atölyesi","Can Köni","Sosyal Hocam","Kampüs","Sevgi Bilgin (Bi Ders Anlatımı)","Hocalara Geldik","Tonguç Akademi","Benim Hocam"]},"M:Felsefe":{"kitap":["# Maarif · öne çıkanlar","Limit","Bilgi Sarmal","Palme","Çap","Paraf","Hız ve Renk","Yediiklim"],"hoca":["# Maarif · öne çıkanlar","Felsefe Atölyesi","Can Köni","Sosyal Hocam","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"Din Kültürü":{"kitap":["# Öne çıkanlar · TYT ve AYT","Bilgi Sarmal","Limit","345","3D","Yediiklim","Palme"],"hoca":["# Öne çıkanlar · TYT ve AYT","Hocalara Geldik","Tonguç Akademi","Benim Hocam"]},"M:Din Kültürü":{"kitap":["# Maarif · öne çıkanlar","Limit","Bilgi Sarmal","Palme","Çap","Yediiklim"],"hoca":["# Maarif · öne çıkanlar","Hocalara Geldik","Tonguç Akademi","Kampüs"]},"_brans":{"kitap":["345 Branş Deneme","Bilgi Sarmal Branş Deneme","3D Branş Deneme","Orijinal Branş Deneme"]}}
;
const kaynakListe = (d, k, mx) => { const K = S.settings.kaynak || DEF_KAYNAK, al = key => (K[key]||DEF_KAYNAK[key]||{})[k];
  if(mx){ const m = al("M:"+d); if(m && m.length) return m; } return al(d) || []; };
const kaynakBol = v => [...new Set(String(v||"").split(/\s+[+·]\s+/).map(x=>x.trim()).filter(Boolean))];
let KYS = [], DYK = {};
function linesToTasks(old, text){
  const pool = old.slice();
  return text.split("\n").map(x=>x.trim()).filter(Boolean).map(line=>{
    const i = pool.findIndex(o=>taskText(o)===line);
    if(i>=0){ const o = pool.splice(i,1)[0]; return {id:o.id, t:line, done:!!o.done, doneAt:o.doneAt||null, ...(o.dk?{dk:o.dk}:{})}; }
    return {id:uid(), t:line, done:false, doneAt:null};
  });
}

/* Görevin dersine ait bu haftaki hedef konu, kitap ve hoca (öğrenci ekranında görevin altında küçük yazı) */
function gorevHedef(s, date, text){ if(!s) return ""; const lt = trLow(text);
  if(/problem/.test(lt)){ /* Matematik hedefinde Problemler bölümünden seçilen (ya da adında "problem" geçen) konular problem görevinin altında görünür */
    const pt = new Set(((CURX().TYT||[]).find(x=>x.k==="prob")||{}).t||[]), mk = splitKonu((((plan(s, pStart(s,date)).hedef)||{})["Matematik"]||{}).konu);
    const pr = mk.filter(x=>pt.has(x) || /problem/i.test(x));
    return `<div class="thd">${pr.length?`<span>${icon("target","xs")}${esc(pr.join(", "))}</span>`:""}<span>${icon("flame","xs")}Günlük rutin</span></div>`; }
  if(/paragraf/.test(lt)) return `<div class="thd"><span>${icon("flame","xs")}Günlük rutin</span></div>`; const kod = dersKodu(text); if(!kod || kod==="den" || kod==="oku") return "";
  const d = cfg().hedefDers.find(x=>dersKodu(x)===kod); if(!d) return "";
  const hd = ((plan(s, pStart(s,date)).hedef)||{})[d] || {}, hc = hoca(s,d), sx0 = /\bAYT\b/i.test(text) ? "AYT" : /\bTYT\b/i.test(text) ? "TYT" : "";
  const kt = ikiSinavli(s,d) ? (sx0 ? kitapK(s,d,sx0) : [kitapK(s,d,"TYT") && (kitapK(s,d,"AYT") ? "TYT: " : "")+kitapK(s,d,"TYT"), kitapK(s,d,"AYT") && "AYT: "+kitapK(s,d,"AYT")].filter(Boolean).join(" · ")) : kitap(s,d);
  let konu = hd.konu || ""; const sx = /\bAYT\b/i.test(text) ? "AYT" : /\bTYT\b/i.test(text) ? "TYT" : "";
  if(sx && konu){ konu = splitKonu(konu).filter(n=>{ const e = konuEx(s,d,n); return !e || e==="ORT" || e===sx; }).join(", "); } /* AYT görevinde sadece AYT konuları, TYT'de TYT */
  if(d==="Matematik" && konu){ const pt = new Set(((CURX().TYT||[]).find(x=>x.k==="prob")||{}).t||[]), kalan = splitKonu(konu).filter(x=>!pt.has(x) && !/problem/i.test(x)); if(kalan.length) konu = kalan.join(", "); } /* problem konuları problem görevinde */
  const par = [konu ? `<span>${icon("target","xs")}${esc(konu)}</span>` : "", kt ? `<span>${icon("book","xs")}${esc(kt)}</span>` : "", hc ? `<span>${icon("users","xs")}${esc(hc)}</span>` : ""].filter(Boolean);
  return par.length ? `<div class="thd">${par.join("")}</div>` : ""; }
function taskRow(t, date, opts={}){
  const h = parseHours(taskText(t)), s = opts.s, ogr = s && !A(), run = !!(s && s.timer && s.timer.task && s.timer.task.id===t.id);
  const sayac = run ? `<div class="trun"><span class="tlive num" data-tlive>${clock(timerMin(s)*60)}</span><button class="btn sm" data-act="tgbitir" data-v="ara">${icon("stop","xs")} Durdur</button></div>` : "";
  const sag = `<div class="tright">${h?`<span class="pill">${icon("clock","xs")}${fmtH(h)}</span>`:""}${ogr && !t.done && !run && date<=today() ? `<button class="tplay" data-act="tgbasla" data-date="${date}" data-id="${t.id}" aria-label="Bu görev için sayacı başlat" title="Sayacı başlat">${icon("play","xs")}</button>`:""}</div>`;
  return `<div class="task ${t.done?"done":""} ${run?"running":""}">
    <button class="tick" data-act="tick" data-date="${date}" data-id="${t.id}" aria-pressed="${!!t.done}" aria-label="${t.done?"Tamamlandı":"Tamamla"}">${icon("check","sm")}</button>
    <div style="min-width:0"><div class="tt" style="font-weight:600">${esc(taskText(t))}</div>${gorevHedef(s, date, taskText(t))}${t.dk?`<div class="thd"><span>${icon("timer","xs")}${fmtMin(t.dk)} çalıştın</span></div>`:""}${sayac}</div>
    ${sag}
  </div>`;
}
/* Görev sayacı: başlat / bitir (bitirdim = görevi de tamamla) */
function sayacDurdur(bitti){ let added = 0, ad = ""; mutate(s=>{ if(!s.timer) return; const d = iso(new Date(s.timer.start)); added = Math.round(timerMin(s)); s.gunluk = s.gunluk||{}; if(added>0) s.gunluk[d] = (s.gunluk[d]||0)+added;
    const tk = s.timer.task; if(tk){ const it = dayTasks(s, tk.date).find(x=>x.id===tk.id); if(it){ ad = taskText(it); if(added>0) it.dk = (it.dk||0)+added; if(bitti){ it.done = true; it.doneAt = today(); } } } s.timer = null; });
  return {added, ad}; }
function goalsCard(s, w, opts={}){
  const {list, h, done} = weekGoals(s,w);
  if(!list.length) return opts.compact ? "" : `<div class="card"><h3>Bu haftanın hedefleri</h3><div class="empty">Koçun bu hafta için hedef konu girmedi.</div></div>`;
  return `<div class="card"><div class="sech"><h3>${opts.title||"Bu haftanın hedefleri"}</h3><span class="small ${done===list.length?"up":"muted"}" style="font-weight:700">${done}/${list.length} konu</span></div>
    <div class="tasks" style="margin-top:4px">${list.map(d=>`<div class="task ${h[d].done?"done":""}"><button class="tick" data-act="gtick" data-w="${w}" data-ders="${esc(d)}" aria-pressed="${!!h[d].done}" aria-label="${esc(d)} hedefi">${icon("check","sm")}</button>
      <div style="min-width:0"><div class="ts" style="font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--ac);text-decoration:none">${esc(d)}</div><div class="tt" style="font-weight:600">${esc(h[d].konu)}</div>${kitap(s,d)||kitapK(s,d,"AYT")||hoca(s,d)?`<div class="tm">${ikiSinavli(s,d) ? [["TYT",kitapK(s,d,"TYT")],["AYT",kitapK(s,d,"AYT")]].filter(x=>x[1]).map(([e,v])=>`<span>${icon("book","xs")}<b class="exs ex-${e}">${e}</b> ${esc(v)}</span>`).join("") : (kitap(s,d)?`<span>${icon("book","xs")}${esc(kitap(s,d))}</span>`:"")}${hoca(s,d)?`<span>${icon("users","xs")}${esc(hoca(s,d))}</span>`:""}</div>`:""}</div><span></span></div>`).join("")}</div></div>`;
}
function dayFooter(s, d){
  const tg = dayTarget(s,d), m = minutes(s,d), p = tg ? Math.min(1, m/60/tg) : 0;
  return `<div style="margin-top:12px;padding-top:12px;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:8px">
    <div class="sech small"><span class="muted" style="display:flex;gap:6px;align-items:center">${icon("clock","xs")} Çalışma süresi</span><span><b class="num">${fmtMin(m)}</b> <span class="faint">/ ${fmtH(tg)}</span></span></div>
    ${tg?`<div class="bar"><i style="width:${p*100}%;background:${p>=1?"var(--good)":"var(--ac)"}"></i></div>`:""}</div>`;
}

/* ---------- Yazılı haftası (plan[w].yazili + plan[w].yazilar [{ders, tarih}]) ---------- */
function yaziliKart(s, w, edit){ const p = plan(s,w); if(!p.yazili) return "";
  const t = today(), l = (p.yazilar||[]).map((y,i)=>({...y, i})).sort((a,b)=>(a.tarih||"").localeCompare(b.tarih||""));
  const kalan = d => { if(!d) return ""; const g = Math.round((new Date(d+"T12:00:00")-new Date(t+"T12:00:00"))/864e5); return g===0?"bugün":g===1?"yarın":g>0?`${g} gün kaldı`:"geçti"; };
  return `<div class="card yzk"><div class="sech"><h3>📝 Yazılı haftası</h3>${edit?`<button class="btn sm" data-act="yazili" data-w="${w}">Kaldır</button>`:`<span class="faint small">${l.length} yazılı</span>`}</div>
    ${l.length?`<div class="yzl">${l.map(y=>`<div class="yzr ${y.tarih===t?"bugun":y.tarih&&y.tarih<t?"gecti":""}"><b>${esc(y.ders)}</b><span class="small muted">${y.tarih?`${GUN[dIdx(y.tarih)]} ${shortDate(y.tarih)} · ${kalan(y.tarih)}`:"tarih yok"}</span>${edit?`<button class="iconbtn sm" data-act="yzsil" data-w="${w}" data-i="${y.i}" aria-label="Sil">${icon("x","sm")}</button>`:""}</div>`).join("")}</div>`:`<p class="muted small" style="margin:6px 0 0">${edit?"Yazılıları aşağıdan ekle; öğrenci ders ve tarihleri programında görür.":"Koçun bu haftayı yazılı haftası olarak işaretledi."}</p>`}
    ${edit?`<div class="yzadd"><input type="text" id="yz-ders" placeholder="Ders (ör. Matematik)" list="yz-dersler"><datalist id="yz-dersler">${["Matematik","Fizik","Kimya","Biyoloji","Türk Dili ve Edebiyatı","Tarih","Coğrafya","Felsefe","Din Kültürü","İngilizce","Arapça","Geometri"].map(x=>`<option value="${x}">`).join("")}</datalist><input type="date" id="yz-tarih" value="${(l.length && l[l.length-1].tarih) || (today() >= w ? today() : w)}"><button class="btn sm pri" data-act="yzekle" data-w="${w}">${icon("plus","xs")} Ekle</button></div>`:""}</div>`; }
const yaziliGun = (s, d) => ((plan(s, pStart(s,d)).yazili && plan(s, pStart(s,d)).yazilar) || []).filter(y=>y.tarih===d).map(y=>y.ders);

function pProgram(s, edit){ return edit ? planEditor(s) : studentProgram(s); }

function weekNav(s){ const w = S.week, an = (s.donem||[]).includes(w);
  return `<div class="wknav"><button class="iconbtn" data-act="wk" data-d="-1" aria-label="Önceki hafta">${icon("back","sm")}</button><b>${shortDate(w)} – ${shortDate(pEnd(s,w))}${w===curStart(s)?` <span class="pill ac">Bu hafta</span>`:""}${an?`<div class="faint small" style="font-weight:600">Görüşme: ${GUN[dIdx(w)]} ${shortDate(w)}</div>`:""}</b><button class="iconbtn" data-act="wk" data-d="1" aria-label="Sonraki hafta">${icon("chev","sm")}</button></div>`; }

function studentProgram(s){
  const w = S.week, t = today(), ws = weekStats(s,w), g = weekGoals(s,w);
  const PD = pDays(s,w); let tgW = 0; PD.forEach(d=>tgW += dayTarget(s, d));
  const strip = `<div class="strip">${PD.map(d=>{ const x=GUNK[dIdx(d)], l=dayTasks(s,d), all=l.length&&l.every(y=>y.done);
    return `<button class="dbtn ${d===t?"today":""}" data-act="day" data-v="${d}" aria-pressed="${S.pmode==="gun"&&S.day===d}" style="--p:${l.length?Math.round(l.filter(y=>y.done).length/l.length*100):0}">${x}<b class="num">${dNum(d)}</b>${l.length?`<i class="${all?"":"p"}"></i>`:""}</button>`; }).join("")}</div>`;
  const hero = `<div class="hero goal" style="display:flex"><div class="goalrow"><span class="ic2">${icon("target")}</span><div style="flex:1"><h3>Haftalık durum</h3><p>${ws.all?`${ws.done}/${ws.all} görev`:"Görev yok"}${g.list.length?` · ${g.done}/${g.list.length} hedef konu`:""} · ${fmtMin(ws.min)}${tgW?` / ${fmtH(tgW)}`:""}</p></div><b class="num" style="font-size:20px">%${ws.pct==null?0:Math.round(ws.pct*100)}</b></div><div class="bar"><i style="width:${(ws.pct||0)*100}%"></i></div></div>`;
  let body;
  if(S.pmode==="gun"){
    const d = S.day && PD.includes(S.day) ? S.day : (PD.includes(t) ? t : w);
    const l = dayTasks(s,d), dn = l.filter(x=>x.done).length;
    body = `<div class="card"><div class="sech"><h3>${GUN[dIdx(d)]}, ${shortDate(d)}${yaziliGun(s,d).map(x=>` <span class="pill warn">${esc(x)} yazılısı</span>`).join("")}</h3><span class="small ${dn===l.length&&l.length?"up":"muted"}" style="font-weight:700">${l.length?`${dn}/${l.length}`:""}</span></div>
      <div class="tasks" style="margin-top:4px">${l.length? l.map(x=>taskRow(x,d,{s})).join("") : `<div class="empty">Bu gün için görev yok.</div>`}</div>${dayFooter(s,d)}
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
    ${weekNav(s)}${yaziliKart(s, w, false)}${S.pmode==="gun"?strip:""}${hero}${body}
    <p class="faint small" style="text-align:center">Programını koçun hazırlıyor. Bitirdiğin satırı ve hedef konuyu işaretle; koçun anında görür.</p>
  </div>`;
}

function planEditor(s){
  const w = S.week, p = plan(s,w), h = p.hedef||{}, ws = weekStats(s,w), g = weekGoals(s,w);
  const goals = `<div class="card"><div class="sech"><h3>Haftalık hedefler</h3><span class="faint small">${g.list.length?`Öğrenci ${g.done}/${g.list.length} işaretledi`:"Boş bırakılan ders öğrenciye görünmez"}</span></div>
    <div class="glist">${cfg().hedefDers.map(d=>hedefSatir(s, w, h, d)).join("")}</div>
    <p class="faint small" style="margin:10px 0 0">Kitap ve hocalar haftadan haftaya otomatik taşınır; sadece değiştiğinde güncellemen yeterli. Listeleri Ayarlar → Kitaplar ve hocalar’dan düzenleyebilirsin.</p></div>`;
  const days = pDays(s,w).map((d,i)=>{ const g = GUN[dIdx(d)], l = dayTasks(s,d), dn = l.filter(x=>x.done).length, auto = autoHours(s,d), sv = (p.saat||{})[i];
    return `<div class="dcard ${d===today()?"today":""}"><div class="dch"><b>${g}</b>${yaziliGun(s,d).map(x=>`<span class="pill warn">${esc(x)} yazılısı</span>`).join("")}<span class="faint small">${shortDate(d)}</span></div>
      <div class="tl" id="tl-${i}" data-i="${i}">${l.map(x=>tlSatir(taskText(x), x.done)).join("")}${tlSatir("", false, true)}</div>
      <div class="pbar" ${(S.pano||[]).length?"":"hidden"}><button type="button" class="btn sm" data-act="tyapistir" data-date="${d}">📋 Yapıştır <b>${(S.pano||[]).length>1?(S.pano.length+" görev"):esc((S.pano||[])[0]||"")}</b></button><button type="button" class="tx" data-act="ptemizle" aria-label="Panoyu temizle" title="Panoyu temizle">×</button></div>
      <textarea id="pl-${i}" data-plan="${d}" hidden>${esc(l.map(taskText).join("\n"))}</textarea>
      <div class="dcf"><label class="hrs">Çalışma süresi<input type="number" min="0" max="16" step="0.5" id="ps-${i}" data-hs="${i}" value="${sv!=null&&sv!==""?sv:""}" placeholder="${auto?String(Math.round(auto*10)/10).replace(".",","):"0"}"> saat</label>
        <div class="dcbtn"><button type="button" class="btn sm pri qbtn" data-act="sheet" data-v="blok" data-date="${d}" aria-label="${g} için blok ekle">${icon("plus","xs")} Blok</button><button type="button" class="btn sm qbtn" data-act="sheet" data-v="hizli" data-date="${d}" aria-label="${g} için hızlı ekle">${icon("search","xs")} Hızlı ekle</button></div></div>
      <div class="dcs"><span>${l.length?`Öğrenci <b class="num">${dn}/${l.length}</b> işaretledi`:"Henüz görev yok"} · <b class="num">${fmtMin(minutes(s,d))}</b> çalıştı</span><button class="link small" data-act="sheet" data-v="copyday" data-date="${d}">${icon("copy","xs")} Kopyala</button></div></div>`; }).join("");
  return `<div style="display:flex;flex-direction:column;gap:14px">
    ${weekNav(s)}
    <div class="pills"><button class="iconbtn sm" data-act="geri" title="Geri al (⌘Z)" aria-label="Geri al" ${(HIST[sid()]||{u:[]}).u.length?"":"disabled"}>↶</button><button class="iconbtn sm" data-act="ileri" title="İleri al (⇧⌘Z)" aria-label="İleri al" ${(HIST[sid()]||{r:[]}).r.length?"":"disabled"}>↷</button><button class="btn sm pri" data-act="sheet" data-v="gorusme">${icon("plus","xs")} Yeni görüşme</button>${plan(s,S.week).yazili?"":`<button class="btn sm" data-act="yazili" data-w="${S.week}">📝 Yazılı haftası yap</button>`}<button class="btn sm" data-act="copyweek">${icon("copy","xs")} Geçen haftayı bu haftaya kopyala</button><span class="faint small" style="align-self:center">Küçük değişiklikleri doğrudan yaz; otomatik kaydedilir.</span></div>
    ${yaziliKart(s, S.week, true)}
    ${(()=>{ const cz = cetele10(s); return cz.length ? `<div class="card czk"><div class="sech"><h3>🔁 Çetelede ${CETELE_ESIK}+ yanlış</h3><span class="faint small">${cz.length} konu</span></div>
      <div class="pills" style="margin-top:8px">${cz.slice(0,12).map(c=>`<span class="pill warn">${esc(c.n)} · <b class="num">${c.y}</b></span>`).join("")}${cz.length>12?`<span class="pill">+${cz.length-12}</span>`:""}</div>
      <p class="faint small" style="margin:8px 0 0">Bu konular günlerdeki “Hızlı ekle” penceresinde en üstte tekrar önerisi olarak çıkar.</p></div>` : ""; })()}
    ${goals}
    <div class="sech"><h3 class="sec">Günlük plan</h3><span class="faint small">${ws.all?`${ws.done}/${ws.all} görev tamamlandı`:""}</span></div>
    <details class="card" style="padding:12px 16px"><summary class="small" style="cursor:pointer;font-weight:700;color:var(--muted)">Süre yazmayan satırlar için ortalama süreler</summary>
      <div class="pills" style="margin-top:10px">${cfg().sureler.filter(r=>r.k&&r.dk).map(r=>`<span class="pill">${esc(r.k)} · <b>${fmtMin(r.dk)}</b></span>`).join("")}<button class="link small" data-act="go" data-v="ayarlar">Ayarlardan düzenle</button></div>
      <p class="faint small" style="margin:8px 0 0">Satırda “(2 saat)” gibi süre yazarsan o geçerli olur. “x2” yazarsan süre ikiyle çarpılır. Günün çalışma süresi kutusunu boş bırakırsan bu toplam kullanılır.</p></details>
    <div class="daygrid">${days}</div>
  </div>`;
}

function netChart(s, tur){
  const list = exams(s,tur).slice(-6); const max = tur==="TYT"?120:160; const hedef = num(s.hedef[tur.toLowerCase()]);
  if(!list.length) return `<div class="empty">Deneme eklendikçe net grafiğin burada oluşur.</div>`;
  const W=360,H=210,pl=26,pr=4,pt=16,pb=26, n=list.length;
  const vals = list.map(totalOf); if(hedef!=null) vals.push(hedef);
  const hi = Math.min(max, Math.max(20, Math.ceil((Math.max(...vals)+5)/20)*20));
  const y = v => pt + (1-Math.max(0,v)/hi)*(H-pt-pb);
  const slot = (W-pl-pr)/Math.max(n,4), bw = Math.min(42, slot*.66), x0 = pl + (W-pl-pr - slot*n)/2;
  let g = `<defs><linearGradient id="bg1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--ac2)"/><stop offset="1" stop-color="var(--ac)"/></linearGradient></defs>`;
  for(let k=0;k<=4;k++){ const v = hi*k/4; g+=`<line x1="${pl}" x2="${W-pr}" y1="${y(v)}" y2="${y(v)}" stroke="var(--line)" stroke-dasharray="3 6"/><text x="${pl-8}" y="${y(v)+4}" text-anchor="end" font-size="10" fill="var(--faint)">${Math.round(v)}</text>`; }
  list.forEach((d,i)=>{ const v = totalOf(d), cx = x0 + slot*i + slot/2, top = y(v), son = i===n-1, h = H-pb-top;
    g += `<rect x="${cx-bw/2}" y="${top}" width="${bw}" height="${Math.max(h,0)}" rx="${Math.min(14,bw/2.6)}" fill="${son?"url(#bg1)":"var(--ac)"}" fill-opacity="${son?1:.78}"/>`;
    g += h>24 ? `<text x="${cx}" y="${top+17}" text-anchor="middle" font-size="11.5" font-weight="800" fill="#fff">${fmt(v)}</text>` : `<text x="${cx}" y="${top-6}" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--fg)">${fmt(v)}</text>`;
    g += `<text x="${cx}" y="${H-8}" text-anchor="middle" font-size="10" fill="var(--faint)">${shortDate(d.tarih)}</text>`; });
  if(hedef!=null){ g+=`<line x1="${pl}" x2="${W-pr}" y1="${y(hedef)}" y2="${y(hedef)}" stroke="var(--warn)" stroke-width="1.6" stroke-dasharray="6 5"/><text x="${W-pr}" y="${y(hedef)-5}" text-anchor="end" font-size="10.5" font-weight="700" fill="var(--warn)">Hedef ${fmt(hedef)}</text>`; }
  return `<div class="chart"><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${tur} net grafiği">${g}</svg></div>`;
}
function pAnaliz(s){
  const tur = S.ex, F = tur==="TYT"?TYTF:AYTF, list = exams(s,tur), last = list[list.length-1], prev = list[list.length-2];
  const tot = last ? totalOf(last) : null, dl = last&&prev ? tot-totalOf(prev) : null;
  const hedef = num(s.hedef[tur.toLowerCase()]), bas = num(s.baslangic[tur.toLowerCase()]);
  const head = A() ? "" : topbar(`<h1 class="ttl">Deneme Analizi</h1>`, `<button class="iconbtn" data-act="sheet" data-v="takvim" aria-label="Deneme takvimi">${icon("cal")}</button><button class="iconbtn" data-act="sheet" data-v="deneme" aria-label="Deneme ekle">${icon("plus")}</button>`);
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
  const head = A() ? "" : topbar(`<h1 class="ttl">Konu Takibi</h1>`, "", `<button class="iconbtn" data-act="go" data-v="ogren" aria-label="Geri">${icon("back")}</button>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    ${asamaSeg()}
    <div class="card"><div class="sech"><h3>${mx}. Aşama ilerlemesi${mx===2?` · ${esc(s.alan)}`:""}</h3><b class="num">%${Math.round(pct*100)}</b></div><div class="bar" style="margin-top:10px"><i style="width:${pct*100}%"></i></div>
      <p class="muted small" style="margin:10px 0 0">Maarif Modeli konuları, temalara göre. ${mx===1?"9. ve 10. sınıf temaları.":"11. sınıf temaları."} Her konuda: tekrar sayısı, 1. ve 2. soru bankası. Üçü tamamlanan konu yeşil olur.</p>
      ${mx===2?`<div class="pills" style="margin-top:10px"><button class="tog" data-act="aytall" aria-pressed="${S.aytAll}">${S.aytAll?"Tüm dersler gösteriliyor":"Tüm dersleri göster"}</button></div>`:""}</div>
    ${dersler.map(d=>{ const subs = list.map((x,i)=>[x,i]).filter(([x])=>x.ders===d); let ds=0, dc=0; subs.forEach(([x])=>x.t.forEach(n=>{ ds+=topicScore(s.topics[tkey(x.k,n)]); dc++; }));
      const dp = dc ? ds/dc : 0, kon = subs.reduce((a,[x])=>a+x.t.length,0);
      return `<details class="mders" data-ders="${esc(d)}" data-key="m:${esc(d)}" style="${CLS[subs[0][1]].split('style="')[1]||""}" ${S.mOpen && S.mOpen[d]?"open":""}><summary><span><b>${esc(d)}</b><span class="faint small">${subs.length} tema · ${kon} konu</span></span><div class="bar"><i style="width:${dp*100}%;${dp>=1?"background:var(--good)":""}"></i></div><span class="pct num">%${Math.round(dp*100)}</span></summary>
      <div class="mtemalar">${subs.map(([sub,si])=>{ const p = subjPct(s,sub);
        return `<details class="${CLS[si]}" data-key="k:${esc(sub.k)}"><summary><span><span class="sn">${esc(sub.n)}</span><span class="sg">${esc(sub.ex)}</span></span><div class="bar"><i style="width:${p*100}%;${p>=1?"background:var(--good)":""}"></i></div><span class="pct num">%${Math.round(p*100)}</span></summary>${konuSatirlari(s, sub)}</details>`; }).join("")}</div></details>`; }).join("")}
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
        return `<div class="trow ${full?"full":""}"><div class="tn">${full?icon("check","xs"):""}${esc(n)}${icerik(k)?`<button type="button" class="kavbtn ${t.v?"on":""}" data-ders="${esc(k)}" aria-label="${esc(n)} konu anlatımı">▶<span>${t.v?"İzlendi":"Konu anlatımı"}</span></button>`:""}</div>
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
      return `<details class="${cls[si]}" data-key="k:${esc(sub.k)}"><summary><span><span class="sn">${esc(sub.n)}</span><span class="sg">${esc(sub.g)}</span></span><div class="bar"><i style="width:${p*100}%;${p>=1?"background:var(--good)":""}"></i></div><span class="pct num">%${Math.round(p*100)}</span></summary>
      ${konuSatirlari(s, sub)}
      </details>`; }).join(""))(subColors(list))}
  </div>`;
}
function pCetele(s){
  const MX = isMaarif(s), ex = MX ? `${S.mx||1}. Aşama` : S.ex, list = MX ? maarifList(s, S.mx||1, S.aytAll) : ex==="TYT" ? CURX().TYT : aytSubjects(s, S.aytAll);
  const CLS = subColors(list); let max = 1, total = 0; list.forEach(sub=>sub.t.forEach(n=>{ const y=(s.topics[tkey(sub.k,n)]||{}).y||0; max=Math.max(max,y); total+=y; }));
  const head = A() ? "" : topbar(`<h1 class="ttl">Yanlış Çetelesi</h1>`, "", `<button class="iconbtn" data-act="go" data-v="ogren" aria-label="Geri">${icon("back")}</button>`);
  return `${head}<div class="page ${A()?"wide":""}" style="${A()?"padding:0;max-width:none":""}">
    ${MX ? asamaSeg() : `<div class="seg"><button data-act="ex" data-v="TYT" aria-pressed="${ex==="TYT"}">TYT</button><button data-act="ex" data-v="AYT" aria-pressed="${ex==="AYT"}">AYT</button></div>`}
    <div class="card"><div class="sech"><h3>${ex} toplam yanlış</h3><b class="num" style="color:var(--bad);font-size:22px">${total}</b></div><p class="muted small" style="margin:6px 0 0">Deneme ve testlerden sonra yanlış yaptığın konuları burada işaretle. En çok yanlış yapılan konular koçunun özetinde görünür.</p></div>
    ${list.map((sub,si)=>{ const tot = sub.t.reduce((a,n)=>a+((s.topics[tkey(sub.k,n)]||{}).y||0),0);
      return `<details class="${CLS[si]}" data-key="c:${esc(sub.k)}" ${tot?"open":""}><summary><span><span class="sn">${esc(MX ? sub.ders+" · "+sub.n : sub.n)}</span><span class="sg">${esc(MX ? sub.ex : ex)}</span></span><span></span><span class="pct num" style="color:${tot?"var(--bad)":"var(--faint)"}">${tot}</span></summary>
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
      ${run && s.timer.task ? (()=>{ const it = dayTasks(s, s.timer.task.date).find(x=>x.id===s.timer.task.id); return it ? `<div class="tgorev">${icon("target","xs")} ${esc(taskText(it))}</div>` : ""; })() : ""}
      <div class="tbtns">${run ? (s.timer.task ? `<button class="bigbtn stop" data-act="tgbitir" data-v="ara">${icon("stop","sm")} Durdur ve kaydet</button>` : `<button class="bigbtn stop" data-act="tstop">${icon("stop","sm")} Bitir ve kaydet</button>`) : `<button class="bigbtn" data-act="tstart">${icon("play","sm")} Çalışmaya başla</button>`}</div>
      ${run?"":`<p class="faint small" style="margin:0;text-align:center">İpucu: Ana sayfada bir görevin yanındaki ▶ ile o görev için sayaç başlatırsan süre derse göre de kaydedilir.</p>`}
      <div class="muted small">Bugün toplam: <b class="num" style="color:var(--fg)" id="ttoday">${fmtMin(minutes(s,t))}</b></div></div>`}
    <div class="card" id="calisma"><div class="sech"><h3>Bu hafta çalışma</h3><b class="num">${fmtMin(mins.reduce((a,b)=>a+b,0))}</b></div>
      <div class="bars7">${days.map((d,i)=>`<button class="b7 ${d===t?"today":""}" data-act="sheet" data-v="sure" data-date="${d}" aria-label="${GUN[dIdx(d)]} süresini düzenle"><em class="num">${mins[i]?fmtMin(mins[i]):""}</em><i style="height:${mins[i]/mx*100}%"></i><span>${GUNK[dIdx(d)]}</span></button>`).join("")}</div>
      <p class="faint small" style="margin:10px 0 0">Bir güne dokunarak süreyi elle düzeltebilirsin.</p>
      <button class="btn full" style="margin-top:10px" data-act="sheet" data-v="sure" data-date="${t}">${icon("plus","sm")} Elle süre ekle</button></div>
    ${dersDagilimKart(s, w)}
  </div>`;
}
/* Bu hafta derslere göre süre (görev sayacıyla kaydedilenler) */
const DERS_AD = {mat:"Matematik", geo:"Geometri", fiz:"Fizik", kim:"Kimya", bio:"Biyoloji", tr:"Türkçe", ede:"Edebiyat", tar:"Tarih", cog:"Coğrafya", fel:"Felsefe", din:"Din Kültürü", den:"Deneme", oku:"Kitap okuma", "":"Diğer"};
function dersDagilim(s, w){ const m = {}; pDays(s,w).forEach(d=>dayTasks(s,d).forEach(t=>{ if(t.dk){ const k = /paragraf/i.test(taskText(t)) ? "tr" : dersKodu(taskText(t)); m[k] = (m[k]||0)+t.dk; } })); return Object.entries(m).sort((a,b)=>b[1]-a[1]); }
function dersDagilimKart(s, w){ const L = dersDagilim(s, w), top = L.reduce((a,[,v])=>a+v,0), tum = pDays(s,w).reduce((a,d)=>a+minutes(s,d,false),0);
  if(!L.length) return `<div class="card"><div class="sech"><h3>Derslere göre süre</h3></div><p class="muted small" style="margin:6px 0 0">${A()?"Öğrenci görev sayacını (▶) kullandıkça bu hafta hangi derse ne kadar çalıştığı burada görünür.":"Bir görevin yanındaki ▶ ile sayacı başlatırsan hangi derse ne kadar çalıştığın burada görünür."}</p></div>`;
  const mx = L[0][1];
  return `<div class="card"><div class="sech"><h3>Derslere göre süre</h3><span class="faint small">bu hafta · ${fmtMin(top)}${tum>top?` / ${fmtMin(tum)}`:""}</span></div>
    <div class="ddl">${L.map(([k,v])=>`<div class="ddr" data-c="${k}"><span class="ddn">${DERS_AD[k]||k}</span><span class="ddb"><i style="width:${Math.max(4, v/mx*100)}%"></i></span><b class="num">${fmtMin(v)}</b></div>`).join("")}</div>
    ${tum>top?`<p class="faint small" style="margin:8px 0 0">${fmtMin(tum-top)} görev sayacı dışında kaydedildi (kronometre ya da elle).</p>`:""}</div>`; }
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
/* Form bağlantısı sağlığı (koc/form: sonNabiz, sonBasvuru, tetikleyici) */
function formSaglik(){ const f = S.formDurum; if(!f || !f.sonNabiz) return {k:"yok"}; const saat = (Date.now() - Date.parse(f.sonNabiz))/36e5;
  if(f.tetikleyici === false) return {k:"kotu", saat, neden:"tetikleyici yok"};
  if(f.kontrol === false) return {k:"kotu", saat, neden:"yedek kontrol yok"}; return {k: saat > 36 ? "kotu" : "iyi", saat}; }
const saatYazi = h => h < 1 ? "1 saatten kısa süre önce" : h < 48 ? `${Math.floor(h)} saat önce` : `${Math.floor(h/24)} gün önce`;
function formDurumYazi(){ const d = formSaglik(); return d.k==="iyi" ? `Çalışıyor ✓ · son sinyal ${saatYazi(d.saat)}` : d.k==="kotu" ? `⚠️ Sorun var · ${d.neden || "son sinyal "+saatYazi(d.saat)}` : "Sinyal yok · kodu güncelle"; }
function formDurumKart(){ const d = formSaglik(), f = S.formDurum || {};
  if(d.k==="iyi") return `<div class="fdurum iyi">${icon("check","xs")} Bağlantı çalışıyor · son sinyal ${saatYazi(d.saat)}${f.sonBasvuru?` · son başvuru ${saatYazi((Date.now()-Date.parse(f.sonBasvuru))/36e5)}`:""}</div>`;
  if(d.k==="kotu") return `<div class="fdurum kotu">⚠️ ${d.neden==="tetikleyici yok" ? "Formdaki otomatik gönderme tetikleyicisi kapalı." : d.neden==="yedek kontrol yok" ? "Formdaki 10 dakikalık yedek kontrol kapalı." : `Formdan ${d.saat<48?Math.floor(d.saat)+" saattir":Math.floor(d.saat/24)+" gündür"} sinyal gelmedi.`} Apps Script'te <b>kur</b>'u yeniden çalıştır; kaçan başvurular için <b>sonBasvurulariAktar</b>.</div>`;
  return `<div class="fdurum">Formdaki kod henüz sinyal yollamıyor. Aşağıdan yeni kodu hazırlayıp forma yapıştır ve <b>kur</b>'u çalıştır.</div>`; }
function formKodHTML(){ if(!FORMKOD) return "";
  const kod = `// Zekacademy · Google Form → uygulama bildirimi
const ADRES = "${FORMKOD.url}";
const ANAHTAR = "${FORMKOD.anahtar}";

// Form gönderilince otomatik çalışır
function gonder(e) {
  yolla(e.response, false);
}

// Google bazen form tetikleyicisini atlar. Bu 10 dakikada bir kaçan başvuru var mı bakar
// ve varsa gönderir. Zaten ulaşmış olanlar sunucuda tekrar eklenmez, bildirim de tekrar gitmez.
function kontrol() {
  var p = PropertiesService.getScriptProperties();
  var son = Number(p.getProperty("sonKontrol")) || (Date.now() - 2 * 3600 * 1000);
  var simdi = Date.now();
  FormApp.getActiveForm().getResponses(new Date(son - 30 * 60 * 1000)).forEach(function (r) {
    Logger.log(r.getTimestamp() + " → " + yolla(r, false));
  });
  p.setProperty("sonKontrol", String(simdi));
  if (simdi - (Number(p.getProperty("sonNabiz")) || 0) > 6 * 3600 * 1000) { nabiz(); p.setProperty("sonNabiz", String(simdi)); }
}

// Uygulamaya "bağlantı çalışıyor" sinyali yollar (gelmezse koça uyarı gider)
function nabiz() {
  var adlar = ScriptApp.getProjectTriggers().map(function (t) { return t.getHandlerFunction(); });
  var r = UrlFetchApp.fetch(ADRES, { method: "post", contentType: "application/json", muteHttpExceptions: true,
    payload: JSON.stringify({ nabizAnahtar: ANAHTAR, nabiz: true,
      tetikleyici: adlar.indexOf("gonder") >= 0, kontrol: adlar.indexOf("kontrol") >= 0 }) });
  Logger.log("Sinyal: " + r.getResponseCode() + " " + r.getContentText());
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

// 1) Önce bunu bir kez çalıştır: form gönderilince gonder() çalışsın, kontrol() 10 dakikada bir yedek baksın
function kur() {
  var tut = ["gonder", "nabiz", "kontrol"];
  ScriptApp.getProjectTriggers().forEach(function (t) { if (tut.indexOf(t.getHandlerFunction()) >= 0) ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger("gonder").forForm(FormApp.getActiveForm()).onFormSubmit().create();
  ScriptApp.newTrigger("kontrol").timeBased().everyMinutes(10).create();
  PropertiesService.getScriptProperties().setProperty("sonKontrol", String(Date.now() - 3 * 24 * 3600 * 1000)); // ilk kontrolde son 3 günde kaçanlar bildirilir
  nabiz();
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
      <li>Üstteki işlev listesinden <b>kur</b>'u seç → <b>Çalıştır</b>. (Kodu her güncellediğinde <b>kur</b>'u yeniden çalıştır.) Google izin isteyecek: hesabını seç → <b>Gelişmiş</b> → <b>Git (güvenli değil)</b> → <b>İzin ver</b>. Bu senin kendi kodun olduğu için çıkan bir uyarı.</li>
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
/* Öğrenciye giriş bilgileri mesajı */
function girisMesaj(x){ const ad = ilkAd(x.name), u = x.kullanici || "";
  return x.ilkSifre
    ? `Merhaba ${ad} 👋\nZekacademy koçluk uygulaman hazır!\n\n📲 Link: https://app.zekacademy.com\n👤 Kullanıcı adın: ${u}\n🔑 İlk şifren: 123456\n\nİlk girişte kendi şifreni belirleyeceksin. Uygulamayı telefonunun ana ekranına eklemeyi unutma; kurulum rehberini de gönderiyorum. Takıldığın yerde bana yaz.`
    : `Merhaba ${ad} 👋\nZekacademy uygulamasına giriş bilgilerin:\n\n📲 Link: https://app.zekacademy.com\n👤 Kullanıcı adın: ${u}\n🔑 Şifren: kendi belirlediğin şifre\n\nŞifreni unuttuysan bana yaz, sıfırlayayım.`; }
function girisSatir(id, x){ const cn = S.cnotes.get(id)||{}, g = cn.girisGonderildi;
  return `<div class="grrow"><div style="min-width:0;flex:1"><b>${esc(x.name)}</b><div class="small muted">@${esc(x.kullanici||"—")} · ${x.ilkSifre?`<span style="color:var(--warn);font-weight:700">ilk şifre 123456</span>`:`<span style="color:var(--good);font-weight:700">kendi şifresini belirledi</span>`}${g?` · <span class="faint">gönderildi ${shortDate(g.slice(0,10))}</span>`:""}</div></div>
    ${x.tel?`<a class="btn sm ${g?"":"pri"}" href="${esc(waLink(x.tel, girisMesaj(x)))}" target="_blank" rel="noopener" data-act="girisgonder" data-id="${id}">${icon("chat","xs")} WhatsApp</a>`:`<span class="faint small">telefon yok</span>`}</div>`; }
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
      ${d==="ogrenci" && n.sid && S.students.has(n.sid) ? `<div class="pills" style="margin-top:8px"><button class="btn sm" data-act="open" data-id="${n.sid}">${icon("user","xs")} Öğrenci sayfası</button><button class="btn sm ${gorusmesiVar(n.sid)?"":"pri"}" data-act="sheet" data-v="gplan" data-sid="${n.sid}">${icon("clock","xs")} ${gorusmesiVar(n.sid)?"Görüşme planla":"İlk görüşmeyi planla"}</button></div>` : ""}
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
/* Koçluk paketleri (ayarlardan düzenlenir). tur: "seans" = haftalık birebir görüşme, "whatsapp" = ilk görüşme + haftalık rapor */
const DEF_PAKET = [{k:"super", n:"Süper Koçluk", tur:"seans", fiyat:6000}, {k:"whatsapp", n:"WhatsApp Koçluğu", tur:"whatsapp", fiyat:null}];
function paketOf(x){ const L = cfg().paketler; if(!x) return L[0];
  return L.find(p=>p.k===x.paket) || (x.paket==="whatsapp" ? L.find(p=>p.tur==="whatsapp") : L.find(p=>p.tur!=="whatsapp")) || L[0]; }
const isWA = x => !!x && paketOf(x)?.tur==="whatsapp";
/* Ödeme tutarına göre paket önerisi: fiyatı tutan paket; yoksa en ucuz seans paketinin altındaysa WhatsApp paketi */
function paketTahmin(id){ const L = cfg().paketler, tu = num(odemeOf(id)?.tutar); if(tu==null) return null;
  const tam = L.find(p=>num(p.fiyat)===tu); if(tam) return tam;
  const sMin = Math.min(...L.filter(p=>p.tur!=="whatsapp" && num(p.fiyat)!=null).map(p=>num(p.fiyat)));
  return tu < sMin ? L.find(p=>p.tur==="whatsapp") : L.find(p=>p.tur!=="whatsapp"); }
function paketOzet(){ const L = cfg().paketler, m = new Map(L.map(p=>[p.k, {p, n:0, tl:0}]));
  S.students.forEach((x,id)=>{ const r = m.get(paketOf(x).k); if(!r) return; r.n++; const o = odemeOf(id); r.tl += num(o?.tutar) ?? num(r.p.fiyat) ?? 0; });
  return [...m.values()]; }
function seansGunu(sid, d){ const z = duzenOf(sid), x = S.students.get(sid);
  if(isWA(x)){ if(z && z.gun!=null && z.gun!=="") return z.gun===dIdx(d); return pStart(x, d)===d; } /* WhatsApp paketi: döngü gününde haftalık rapor, saat yok */
  if(!z) return false; const gunVar = z.gun!=null && z.gun!=="";
  if(!z.saat) return gunVar && z.gun===dIdx(d); /* saati henüz girilmemiş: günü belli, listede "saat yok" olarak görünür */
  if(gunVar) return z.gun===dIdx(d);
  return !!x && pStart(x, d)===d; }
function sanalKayit(sid, d){ const x = S.students.get(sid), z = duzenOf(sid) || {};
  return isWA(x) ? {sid, ad:x?.name||"", tarih:d, hafta:monday(d), saat:null, sure:0, tur:"rapor", durum:"planli", kaynak:"duzen"}
    : {sid, ad:x?.name||"", tarih:d, hafta:monday(d), saat:z.saat||null, sure:z.sure||SURE_SEANS, tur:"seans", durum:"planli", kaynak:"duzen"}; }
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
  const akt = all.filter(g=>g.durum!=="iptal" && g.tur!=="rapor" && g.saat);
  akt.forEach(g=>{ const a = hmTo(g.saat), b = a+(g.sure||15); g.cakisma = akt.some(h=>h!==g && hmTo(h.saat) < b && hmTo(h.saat)+(h.sure||15) > a); });
  return all; }
/* Öğrencinin sıradaki görüşmesi (4 hafta içinde, haftalık düzenden gelenler dahil) */
function siradakiGorusme(sid){ const t = today(); for(let i=0;i<28;i++){ const g = gunGorusme(addDays(t,i)).find(x=>x.sid===sid && x.durum==="planli" && x.tur!=="rapor"); if(g) return g; } return null; }
const gorusmesiVar = sid => [...S.gorus.values()].some(g=>g.sid===sid) || !!duzenOf(sid)?.saat;
function gorusmeKart(sid){ const x = S.students.get(sid); if(!x) return ""; const g = siradakiGorusme(sid), z = duzenOf(sid), ilk = !gorusmesiVar(sid) && !g;
  const duz = z && z.saat && z.gun!=null && z.gun!=="" ? `Her hafta ${GUN[z.gun]} ${z.saat}` : "";
  const ust = g ? `<b>${g.tur==="ilk"?"İlk görüşme":"Sıradaki görüşme"}:</b> ${GUN[dIdx(g.tarih)]}, ${trDate(g.tarih)}${g.saat?` · ${g.saat}`:` · <span style="color:var(--bad)">saat yok</span>`}`
    : ilk ? `<b>İlk görüşme henüz planlanmadı.</b>` : `<span class="muted">Önümüzdeki 4 haftada planlı görüşme yok.</span>`;
  return `<div class="card gkart"><div class="sech"><h3>${icon("clock","sm")} Görüşme</h3>${duz?`<span class="pill">${esc(duz)}</span>`:""}</div>
    <p class="small" style="margin:6px 0 10px">${ust}</p>
    <div class="pills">${g?`<button class="btn sm" data-act="gmod" data-v="${g.id}">Görüşmeyi aç</button>`:""}<button class="btn sm ${g?"":"pri"}" data-act="sheet" data-v="gplan" data-sid="${sid}">${icon("plus","xs")} ${ilk?"İlk görüşmeyi planla":"Görüşme planla"}</button></div></div>`; }
function gorusAd(g){ return g.sid && S.students.has(g.sid) ? S.students.get(g.sid).name : (g.ad || "İsimsiz"); }
/* Sanal (düzenden gelen) görüşmeyi gerçek kayda çevirir */
function gorusGercek(id){ if(!id.startsWith("v:")) return id; const [,sid,d] = id.split(":"); const z = duzenOf(sid) || {};
  const var_ = [...S.gorus.entries()].find(([,g])=>g.sid===sid && g.kaynak==="duzen" && (g.hafta || monday(g.tarih))===monday(d)); if(var_) return var_[0];
  const nid = uid(); S.gorus.set(nid, sanalKayit(sid, d)); persistDoc("gorusmeler", nid, 0); return nid; }
function gorusSet(id, fn){ const rid = gorusGercek(id); const g = {...S.gorus.get(rid)}; fn(g); S.gorus.set(rid, g); persistDoc("gorusmeler", rid, 200); return rid; }
function cGorusme(){
  const t = today(), d = S.gday || t, w = monday(d), days = [0,1,2,3,4,5,6].map(i=>addDays(w,i));
  const tum = gunGorusme(d), list = tum.filter(g=>g.tur!=="rapor"), rap = tum.filter(g=>g.tur==="rapor"), akt = list.filter(g=>g.durum!=="iptal" && g.saat), top = akt.reduce((a,g)=>a+(g.sure||15),0);
  const duzensiz = sortedStudents().filter(([id,x])=>!isWA(x) && !duzenOf(id)?.saat).length;
  const rows = []; let son = null;
  list.forEach(g=>{ const a = hmTo(g.saat); if(g.saat && son!=null && g.durum!=="iptal" && a - son >= 15) rows.push(`<div class="gbos">Boş · ${toHm(son)} – ${g.saat} <span>${a-son} dk</span></div>`);
    if(g.saat && g.durum!=="iptal") son = Math.max(son??0, a+(g.sure||15));
    const ilk = g.tur==="ilk", dur = g.durum;
    rows.push(`<div class="grow g-${dur} ${g.cakisma?"g-cak":""} ${ilk?"g-ilk":""}"><div class="gsaat">${g.saat?`<b class="num">${g.saat}</b><span class="num">${toHm(a+(g.sure||15))}</span>`:`<b>—</b><span>saat yok</span>`}</div>
      <div style="min-width:0;flex:1;cursor:pointer" data-act="gmod" data-v="${g.id}" role="button" tabindex="0"><b>${esc(gorusAd(g))}</b><div class="gmeta"><span class="gtag">${ilk?"İlk görüşme":"Seans"} · ${g.sure||15} dk</span>${g.sanal||g.kaynak==="duzen"?`<span class="faint">her hafta</span>`:""}${!g.saat?`<span class="gwarn">Saati gir</span>`:""}${g.cakisma?`<span class="gwarn">Çakışıyor</span>`:""}${dur==="yapildi"?`<span class="gok">Yapıldı</span>`:dur==="gelmedi"?`<span class="gwarn">Gelmedi</span>`:dur==="iptal"?`<span class="faint">İptal</span>`:""}</div>${g.not?`<div class="small muted" style="margin-top:4px">${esc(g.not)}</div>`:""}</div>
      <div class="gact"><button class="iconbtn sm ${dur==="yapildi"?"on":""}" data-act="gdurum" data-id="${g.id}" data-v="${dur==="yapildi"?"planli":"yapildi"}" aria-label="Yapıldı">${icon("check","sm")}</button><button class="iconbtn sm" data-act="sheet" data-v="gplan" data-id="${g.id}" aria-label="Düzenle">${icon("edit","sm")}</button></div></div>`); });
  return `${topbar(`<h1 class="ttl">Görüşmeler</h1>`, `<button class="iconbtn" data-act="sheet" data-v="gplan" data-d="${d}" aria-label="Görüşme ekle">${icon("plus")}</button>`)}
  <div class="page wide">
    <div class="wknav"><button class="iconbtn" data-act="gwk" data-d="-7" aria-label="Önceki hafta">${icon("back","sm")}</button><b>${shortDate(w)} – ${shortDate(addDays(w,6))}${w===monday(t)?` <span class="pill ac">Bu hafta</span>`:""}</b><button class="iconbtn" data-act="gwk" data-d="7" aria-label="Sonraki hafta">${icon("chev","sm")}</button></div>
    <div class="gdays">${days.map(x=>{ const l = gunGorusme(x).filter(g=>g.durum!=="iptal"), c = l.some(g=>g.cakisma);
      return `<button class="gday ${x===t?"today":""}" data-act="gday" data-v="${x}" aria-pressed="${x===d}"><span>${GUNK[dIdx(x)]}</span><b class="num">${dNum(x)}</b><em class="num">${l.length||""}</em>${c?`<i></i>`:""}</button>`; }).join("")}</div>
    <div class="card"><div class="sech"><h3>${GUN[dIdx(d)]}, ${trDate(d)}</h3><span class="faint small">${akt.length?`${akt.length} görüşme · ${fmtMin(top)}${akt.length?` · ${akt[0].saat}–${toHm(Math.max(...akt.map(g=>hmTo(g.saat)+(g.sure||15))))}`:""}`:""}${list.some(g=>g.durum!=="iptal" && !g.saat)?`${akt.length?" · ":""}${list.filter(g=>g.durum!=="iptal" && !g.saat).length} kişinin saati yok`:akt.length?"":"Görüşme yok"}</span></div>
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
  return String(t).replace(/\{Ad\}/g, ilkAd(x?.name)).replace(/\{AdSoyad\}/g, adSoyad(x?.name)).replace(/\{Saat\}/g, g && g.saat ? g.saat : "__:__").replace(/\{Gün\}/g, g ? GUN[dIdx(g.tarih)] : ""); }
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
  const gt = gunGorusme(t).filter(g=>g.durum!=="iptal"), gl = gt.filter(g=>g.tur!=="rapor"), rp = gt.filter(g=>g.tur==="rapor"), sira = gl.find(g=>g.durum==="planli" && g.saat && hmTo(g.saat)+(g.sure||15) > nowMin()) || gl.find(g=>g.durum==="planli" && !g.saat);
  items.push({ic:"clock", k:gl.length?"":"bos", t: gl.length ? `<b>${gl.length} görüşme</b>${sira?` · sıradaki ${sira.saat||"(saat yok)"} ${esc(gorusAd(sira))}`:" · hepsi bitti"}` : "Bugün görüşme yok", act:`data-act="gday" data-v="${t}"`});
  if(rp.length) items.push({ic:"chat", k:"", t:(n=>`<b>${rp.length}</b> haftalık rapor günü · ${n===rp.length?"hepsi geldi":n?`${n} geldi, ${rp.length-n} bekleniyor`:"bekleniyor"}`)(rp.filter(g=>g.durum==="yapildi").length), act:`data-act="gday" data-v="${t}"`});
  let bugun = 0, gecik = 0; S.students.forEach((_,id)=>{ const d = odemeDurum(id); if(d.d===t && d.k==="turuncu") bugun++; if(d.k==="kirmizi"||d.k==="pembe") gecik++; });
  if(bugun || gecik) items.push({ic:"cal", k:gecik?"kotu":"", t:[bugun?`<b>${bugun}</b> ödeme günü bugün`:"", gecik?`<b>${gecik}</b> geciken ödeme`:""].filter(Boolean).join(" · "), act:`data-act="go" data-v="odeme"`});
  if(formSaglik().k==="kotu") items.push({ic:"alert", k:"kotu", t:`<b>Google Form bağlantısı</b> durmuş olabilir · ${esc(formDurumYazi().replace("⚠️ Sorun var · ",""))}`, act:`data-act="go" data-v="ayarlar"`});
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
  const ust = `<div class="card gmhead"><div><div class="gmsaat num">${R?"Haftalık rapor":g.saat?`${g.saat} – ${toHm(hmTo(g.saat)+(g.sure||15))}`:"Saat belirlenmedi"}</div><div class="small muted">${GUN[dIdx(g.tarih)]}, ${trDate(g.tarih)} · ${R?"WhatsApp koçluğu":`${g.tur==="ilk"?"İlk görüşme":"Seans"} · ${g.sure||15} dk`}${g.durum==="yapildi"?` · <b style="color:var(--good)">${R?"Rapor geldi":"Yapıldı"}</b>`:g.durum==="gelmedi"?` · <b style="color:var(--bad)">Gelmedi</b>`:""}</div></div>
      <div class="pills">${s?waBtn(sid,true):""}<button class="btn sm" data-act="sheet" data-v="gplan" data-id="${g.id}">${icon("edit","xs")} Düzenle</button></div></div>`;
  if(!s) return `${topbar(`<h1 class="ttl">${esc(gorusAd(g))}</h1>`, "", back)}<div class="page wide">${ust}
    <div class="card"><p class="muted" style="margin:0">Bu kişi henüz öğrenci değil (ilk görüşme). Görüşmeden sonra Başvurular'dan öğrenci hesabını açabilirsin.</p>
    <div class="pills" style="margin-top:10px"><button class="btn sm pri" data-act="gdurum" data-id="${g.id}" data-v="yapildi">${icon("check","xs")} Yapıldı</button><button class="btn sm" data-act="gdurum" data-id="${g.id}" data-v="gelmedi">Gelmedi</button>${g.bid?`<button class="btn sm" data-act="go" data-v="basvuru">Başvuruya git</button>`:""}</div></div></div>`;
  const yeniHafta = pStart(s, g.tarih)===g.tarih, w = yeniHafta ? pStart(s, addDays(g.tarih,-1)) : pStart(s, g.tarih);
  const ws = weekStats(s, w), gl = weekGoals(s, w), days = pDays(s, w), mins = days.map(d=>minutes(s,d)), mx = Math.max(60, ...mins), m = coachMetrics(s);
  const den = [...exams(s,"TYT").map(d=>["TYT",d,tytTotal(d)]), ...exams(s,"AYT").map(d=>["AYT",d,aytTotal(d)])].sort((a,b)=>a[1].tarih<b[1].tarih?1:-1).slice(0,4);
  return `${topbar(`<div class="tttl"><h1 class="ttl" style="font-size:20px">${esc(s.name)}</h1><div class="faint small">${esc(s.alan)} · ${esc(s.sinif)}</div></div>`, `<button class="iconbtn" data-act="open" data-id="${sid}" aria-label="Öğrenci sayfası">${icon("user")}</button>`, back)}
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
        <div class="osub">${esc(paketOf(x).n)} · ${o&&o.bas?`${PERIYOT[o.periyot||"ay"]}${o.tutar?" · "+fmtTL(o.tutar):""} · Başlangıç ${shortDate(o.bas)}`:"Başlangıç tarihi girilmedi"}</div></div>
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
  const pages = {socoz:pSoruCoz, aipanel:cAiPanel, ozet:cOzet, ogrenciler:cList, detay:cDetail, program:cProgram, bildirim:cBell, daha:cMore, ayarlar:cSettings, odeme:cOdeme, basvuru:cBasvuru, giris:cGiris, gorusme:cGorusme, gelir:cOdeme, gmod:cGmod};
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
  return `${topbar(`<div class="logo"><span class="lm">${LOGO}</span>Koç Paneli</div>`, temaBtn()+bellBtn(unread))}
  <div class="page wide">
    <div class="hello"><p class="small" style="margin:0">${longToday()}</p><h1>Günaydın hocam</h1><p>Öğrencilerinin bu haftaki durumu. Bu sayfayı sadece sen görürsün.</p></div>
    ${pushCard()}
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
    <div class="pills"><button class="btn sm" data-act="sheet" data-v="girisler">🔑 Giriş bilgilerini WhatsApp’tan gönder</button></div>
    <div class="card">${all.length? all.map(studentRow).join("") : `<div class="empty">Öğrenci bulunamadı.</div>`}</div>
    <div class="card"><h3>Kayıt linki</h3><p class="muted small" style="margin:6px 0 0">Öğrencilerin bu uygulamanın linkinden “Kayıt ol” ile kendileri kaydolur. Her yeni kayıt Bildirimler’e düşer. Link: <b>${esc(location.origin)}</b></p></div>
  </div>`;
}
function cDetail(){
  const s = st(); if(!s){ S.view="ogrenciler"; return cList(); }
  const sqb = soruList(S.cur).filter(([,q])=>q.durum!=="cozuldu").length;
  const tabs = [["ozet","Özet"],["program","Program"],["analiz","Analiz"],["konular","Konular"],["cetele","Çetele"],["calisma","Çalışma"],["sorular",`Sorular${sqb?` <span class="tcnt">${sqb}</span>`:""}`]];
  const acc = accountOf(S.cur);
  const body = {ozet:()=>cSummary(s), program:()=>pProgram(s,true), analiz:()=>pAnaliz(s), konular:()=>pKonular(s), cetele:()=>pCetele(s), calisma:()=>pCalisma(s), sorular:()=>{ sorularOgrenci(S.cur); return pSorular(s, S.cur); }}[S.dtab] || (()=>cSummary(s));
  return `${topbar(`<div class="tttl"><h1 class="ttl" style="font-size:20px">${esc(s.name)}</h1><div class="faint small">${esc(s.alan)} · ${esc(s.sinif)}${isWA(s)?" · WhatsApp koçluğu":""}${s.okul?" · "+esc(s.okul):""}${acc?" · @"+esc(acc.u):" · hesap yok"}${(d=>` · <span class="gtdur ${d.k}" style="font-size:11px;padding:1px 6px">${d.k==="hic"?"hiç girmedi":"son giriş "+d.yazi.charAt(0).toLocaleLowerCase("tr")+d.yazi.slice(1)}</span>`)(girisDurum(s))}</div></div>`, `<button class="iconbtn" data-act="sheet" data-v="wa" data-sid="${S.cur}" aria-label="WhatsApp mesajı">${icon("chat")}</button><button class="iconbtn" data-act="sheet" data-v="ogrenci" data-id="${S.cur}" aria-label="Öğrenciyi düzenle">${icon("edit")}</button>`, `<button class="iconbtn" data-act="go" data-v="ozet" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page wide"><div class="tabs">${tabs.map(([k,n])=>`<button data-act="dtab" data-v="${k}" aria-pressed="${S.dtab===k}">${n}</button>`).join("")}</div>${body()}</div>`;
}
/* ---------- Günlük görev listesi: her görev ayrı satır (metin kutusu gibi yazılır, Enter yeni satır) ---------- */
const DERS_ANAHTAR = [["mat",/matemat|problem|\bmat\b|türev|integral|limit\b|logaritma|polinom/],["geo",/geometri|\bgeo\b/],["fiz",/fizik/],["kim",/kimya/],["bio",/biyoloji|\bbiyo/],["tr",/türkçe|paragraf|dil bilgisi|dilbilgisi/],["ede",/edebiyat/],["tar",/tarih|inkılap/],["cog",/coğrafya/],["fel",/felsefe|psikoloji|sosyoloji|mantık/],["din",/din kültürü|\bdin\b/],["den",/deneme/],["oku",/kitap okuma|okuma/]];
const dersKodu = t => { const l = trLow(t); return (DERS_ANAHTAR.find(([,r])=>r.test(l))||[""])[0]; };
/* Haftalık hedef satırı: ders rengi, konu, kitap ve hoca çipleri */
function kaynakCipleri(s, d, k, ex=""){ const L = kaynakBol(k==="kitap" ? kitapK(s,d,ex) : hoca(s,d));
  return `<div class="gk gk-${k} ${ex?"ex-"+ex:""}" data-ex="${ex}"><span class="gkl">${icon(k==="kitap"?"book":"users","xs")}${k==="kitap"?(ex?ex:"Kitap"):"Hoca"}</span><div class="gchips">${L.map(x=>`<span class="kc">${esc(x)}<button type="button" data-act="kcsil" data-k="${k}" data-ex="${ex}" data-ders="${esc(d)}" data-v="${esc(x)}" aria-label="${esc(x)} kaldır">×</button></span>`).join("")}<button type="button" class="kadd" data-act="sheet" data-v="kaynak" data-k="${k}" data-ex="${ex}" data-ders="${esc(d)}" aria-label="${esc(d)} ${ex} ${k} ekle">${icon("plus","xs")}${L.length?"":(k==="kitap"?(ex?ex+" kitabı ekle":"Kitap ekle"):"Hoca ekle")}</button></div></div>`; }
function hedefSatir(s, w, h, d){ const hd = h[d]||{};
  return `<div class="gc ${hd.konu?"":"bos"}" data-c="${dersKodu(d)}"><div class="gch">${hd.konu?`<button class="tick sm" data-act="gtick" data-w="${w}" data-ders="${esc(d)}" aria-pressed="${!!hd.done}" aria-label="${esc(d)} tamamlandı">${icon("check","xs")}</button>`:`<span class="tick sm ghost"></span>`}<b>${esc(d)}</b></div>
    <button type="button" class="kpick" id="hk-${esc(d)}" data-act="sheet" data-v="konu" data-ders="${esc(d)}">${hd.konu?`<span class="kchs">${konuCipleri(s,d,hd.konu)}</span>`:`<span class="faint">Bitirilecek konu seç</span>`}<span class="kpi">${icon("search","xs")}</span></button>
    <div class="gkyn">${ikiSinavli(s,d) ? kaynakCipleri(s,d,"kitap","TYT")+kaynakCipleri(s,d,"kitap","AYT") : kaynakCipleri(s,d,"kitap")}${kaynakCipleri(s,d,"hoca")}</div></div>`; }
function kysNot(kaydet){ const e = $("#kysel"); if(e) e.textContent = KYS.length ? `Seçili: ${KYS.join(" + ")}` : "Seçim yok";
  if(!kaydet || !S.kyn) return; const {d, k, ex} = S.kyn, v = KYS.join(" + "), alan = k==="kitap" ? "kitaplar" : "hocalar", key = k==="kitap" && ex==="AYT" ? d+"|AYT" : d;
  mutate(x=>{ x[alan] = x[alan]||{}; if(v) x[alan][key] = v; else delete x[alan][key]; });
  const g = [...document.querySelectorAll(`#root .gk-${k} .kadd`)].find(x=>x.dataset.ders===d && (x.dataset.ex||"")===(ex||""))?.closest(".gk"); if(g) g.outerHTML = kaynakCipleri(st(), d, k, ex||""); }
function tlSure(t){ if(/\d\s*(saat|sa|dk|dakika)\b/i.test(t)) return ""; const h = parseHours(t); return h ? "≈ "+fmtMin(h*60) : ""; } /* satırda süre yazıyorsa tekrar gösterme */
const TL_BTN = `<span class="tacts"><button type="button" class="tx tc" data-act="tkopya" aria-label="Görevi kopyala" title="Kopyala">${'<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>'}</button><button type="button" class="tx" data-act="tdel" aria-label="Görevi sil">×</button></span>`;
function tlSatir(t, done, bos){ return `<div class="tr ${done?"ok":""} ${bos?"yeni":""}" data-c="${bos?"":dersKodu(t)}">${bos?"":`<span class="tgrip" data-grip title="Sürükleyip taşı" aria-label="Görevi taşı"><svg viewBox="0 0 10 16" width="8" height="14" fill="currentColor"><circle cx="2.5" cy="3" r="1.4"/><circle cx="7.5" cy="3" r="1.4"/><circle cx="2.5" cy="8" r="1.4"/><circle cx="7.5" cy="8" r="1.4"/><circle cx="2.5" cy="13" r="1.4"/><circle cx="7.5" cy="13" r="1.4"/></svg></span>`}<span class="tdot">${done?icon("check","xs"):""}</span><div class="tmain"><div class="tghost" aria-hidden="true"></div><textarea rows="1" class="tin" data-tl="1" placeholder="${bos?"+ Görev yaz":""}" aria-label="Görev">${esc(t)}</textarea><span class="tdur">${esc(tlSure(t))}</span></div>${bos?"":TL_BTN}</div>`; }
const TL_GRIP = `<span class="tgrip" data-grip title="Sürükleyip taşı" aria-label="Görevi taşı"><svg viewBox="0 0 10 16" width="8" height="14" fill="currentColor"><circle cx="2.5" cy="3" r="1.4"/><circle cx="7.5" cy="3" r="1.4"/><circle cx="2.5" cy="8" r="1.4"/><circle cx="7.5" cy="8" r="1.4"/><circle cx="2.5" cy="13" r="1.4"/><circle cx="7.5" cy="13" r="1.4"/></svg></span>`;
/* Sürükle-bırak: görevi aynı gün içinde ya da başka güne taşı (fare ve dokunmatik) */
let SUR = null, UZUN = null;
function surBasla(e){ const {row} = SUR, r = row.getBoundingClientRect(); SUR.basla = true; SUR.dx = e.clientX - r.left; SUR.dy = e.clientY - r.top;
  const ph = document.createElement("div"); ph.className = "tph"; ph.style.height = r.height+"px"; row.after(ph); SUR.ph = ph;
  row.classList.add("surukle"); Object.assign(row.style, {width:r.width+"px", left:r.left+"px", top:r.top+"px"}); document.body.classList.add("suruk"); }
document.addEventListener("pointerdown", e=>{ if(e.button>0) return; const g = e.target.closest && e.target.closest("[data-grip]");
  if(g){ const row = g.closest(".tr"); if(!row) return; e.preventDefault(); SUR = {row, src:row.closest(".tl"), x0:e.clientX, y0:e.clientY, basla:false, id:e.pointerId}; try{ g.setPointerCapture(e.pointerId); }catch(_){} return; }
  /* Uzun basma: görevin herhangi bir yerine ~0,4 sn basılı tut → taşı */
  const row = e.target.closest && e.target.closest(".tl .tr:not(.yeni)"); if(!row || e.target.closest("[data-act]")) return;
  clearTimeout(UZUN?.t); UZUN = {row, x0:e.clientX, y0:e.clientY, x:e.clientX, y:e.clientY, id:e.pointerId};
  UZUN.t = setTimeout(()=>{ const u = UZUN; UZUN = null; if(!u || !u.row.isConnected) return; if(document.activeElement && document.activeElement.blur) document.activeElement.blur(); try{ getSelection().removeAllRanges(); }catch(_){}
    SUR = {row:u.row, src:u.row.closest(".tl"), x0:u.x, y0:u.y, basla:false, id:u.id, uzun:true}; surBasla({clientX:u.x, clientY:u.y}); u.row.style.left = (u.x - SUR.dx)+"px"; u.row.style.top = (u.y - SUR.dy)+"px"; try{ navigator.vibrate && navigator.vibrate(18); }catch(_){} }, 420); });
document.addEventListener("pointermove", e=>{ if(UZUN && e.pointerId===UZUN.id){ UZUN.x = e.clientX; UZUN.y = e.clientY; if(Math.hypot(e.clientX-UZUN.x0, e.clientY-UZUN.y0) > 8){ clearTimeout(UZUN.t); UZUN = null; } } }, true);
document.addEventListener("touchmove", e=>{ if(SUR && SUR.basla) e.preventDefault(); }, {passive:false}); /* taşırken sayfa kaymasın */
document.addEventListener("contextmenu", e=>{ if(SUR || (UZUN && e.target.closest && e.target.closest(".tl"))) e.preventDefault(); });
document.addEventListener("pointermove", e=>{ if(!SUR || e.pointerId!==SUR.id) return; const {row} = SUR;
  if(!SUR.basla){ if(Math.hypot(e.clientX-SUR.x0, e.clientY-SUR.y0) < 5) return; surBasla(e); }
  row.style.left = (e.clientX - SUR.dx)+"px"; row.style.top = (e.clientY - SUR.dy)+"px";
  if(e.clientY < 70) window.scrollBy(0, -12); else if(e.clientY > innerHeight - 90) window.scrollBy(0, 12);
  row.style.visibility = "hidden"; const alt = document.elementFromPoint(e.clientX, e.clientY); row.style.visibility = "";
  const box = alt && alt.closest(".tl"); if(!box) return;
  const satirlar = [...box.querySelectorAll(".tr:not(.surukle):not(.yeni)")]; const once = satirlar.find(x=>{ const r = x.getBoundingClientRect(); return e.clientY < r.top + r.height/2; });
  if(once) once.before(SUR.ph); else { const y = box.querySelector(".tr.yeni"); if(y) y.before(SUR.ph); else box.appendChild(SUR.ph); } });
function surBitir(e){ if(UZUN && e && e.pointerId===UZUN.id){ clearTimeout(UZUN.t); UZUN = null; } if(!SUR || (e && e.pointerId!==SUR.id)) return; const {row, src, ph, basla} = SUR; SUR = null; document.body.classList.remove("suruk"); if(!basla) return;
  row.classList.remove("surukle"); row.removeAttribute("style"); const hedef = ph.closest(".tl"); ph.replaceWith(row); tlBoyut(row);
  tlSync(src); if(hedef && hedef!==src){ tlSync(hedef); const g = document.querySelector(`.dcard #tl-${hedef.dataset.i}`)?.closest(".dcard")?.querySelector(".dch b")?.textContent; toast(`${g||"Diğer güne"} taşındı`); } }
document.addEventListener("pointerup", surBitir); document.addEventListener("pointercancel", surBitir);
function panoGuncelle(){ const n = (S.pano||[]).length; document.querySelectorAll(".pbar").forEach(x=>{ x.hidden = !n; const b = x.querySelector("[data-act=tyapistir]"); if(b) b.innerHTML = `📋 Yapıştır <b>${n>1?n+" görev":esc(S.pano[0]||"")}</b>`; }); }
function tlBoyut(kok){ (kok||document).querySelectorAll(".tin").forEach(x=>{ x.style.height = "auto"; x.style.height = x.scrollHeight+"px"; }); }
function tlSync(box){ const ta = document.getElementById("pl-"+box.dataset.i); if(!ta) return;
  const v = [...box.querySelectorAll(".tin")].map(x=>x.value.replace(/\s+/g," ").trim()).filter(Boolean).join("\n");
  if(ta.value !== v){ ta.value = v; ta.dispatchEvent(new Event("input",{bubbles:true})); }
  const son = box.lastElementChild; if(!son || !son.classList.contains("yeni") || son.querySelector(".tin").value.trim()){ if(son && son.classList.contains("yeni")){ son.classList.remove("yeni"); son.insertAdjacentHTML("beforeend", TL_BTN); son.insertAdjacentHTML("afterbegin", TL_GRIP); son.querySelector(".tin").placeholder = ""; } box.insertAdjacentHTML("beforeend", tlSatir("", false, true)); } }
function tlSatirGuncelle(tin){ const r = tin.closest(".tr"); if(!r) return; tin.style.height = "auto"; tin.style.height = tin.scrollHeight+"px"; if(!r.classList.contains("yeni")) r.dataset.c = dersKodu(tin.value); r.querySelector(".tdur").textContent = tlSure(tin.value); }
/* Blok / hızlı ekle: güne satır ekle */
function gunEkle(d, t){ const i = pIdx(st(), d), box = document.getElementById("tl-"+i);
  if(box){ const yeni = box.querySelector(".tr.yeni"); yeni.insertAdjacentHTML("beforebegin", tlSatir(t, false)); tlBoyut(box); tlSync(box); return; }
  const ta = document.getElementById("pl-"+i); if(ta){ ta.value = (ta.value.trim()? ta.value.replace(/\s+$/,"")+"\n" : "") + t; ta.dispatchEvent(new Event("input",{bubbles:true})); } }
/* Yazarken otomatik tamamlama: "AYT Fiz" → "AYT Fizik Çalışması (1,5 saat)" (Enter veya Tab ile kabul) */
let ONERI = null, ONERI_ZAMAN = 0;
function oneriListesi(){ if(ONERI && Date.now()-ONERI_ZAMAN < 20000) return ONERI; const m = new Map(), ekle = (t, w) => { t = String(t||"").replace(/\s+/g," ").trim(); if(t.length > 2) m.set(t, (m.get(t)||0) + w); };
  const s = st(); if(s) Object.values(s.weeks||{}).forEach(x=>Object.values(x).forEach(l=>(l||[]).forEach(k=>ekle(taskText(k), 5))));
  cfg().quick.forEach(t=>ekle(t, 2)); S.students.forEach((x,id)=>{ if(id===sid()) return; Object.values(x.weeks||{}).forEach(w=>Object.values(w).forEach(l=>(l||[]).forEach(k=>ekle(taskText(k), 1)))); });
  ONERI = [...m.entries()].sort((a,b)=>b[1]-a[1] || a[0].length-b[0].length).map(([t])=>t); ONERI_ZAMAN = Date.now(); return ONERI; }
function oneriGoster(t){ const g = t.parentElement && t.parentElement.querySelector(".tghost"); if(!g) return; const v = t.value;
  const temizle = () => { g.innerHTML = ""; delete t.dataset.oneri; };
  if(document.activeElement!==t || v.trim().length < 2 || t.selectionStart !== v.length || /\n/.test(v)) return temizle();
  const lv = trLow(v), bul = oneriListesi().find(x=>x.length > v.length && trLow(x).startsWith(lv)); if(!bul) return temizle();
  t.dataset.oneri = bul; g.innerHTML = `<span class="tgt">${esc(v)}</span><span class="tgr">${esc(bul.slice(v.length))}</span><span class="tgk">↵</span>`; }
function oneriKabul(t){ if(!t.dataset.oneri) return false; t.value = t.dataset.oneri; delete t.dataset.oneri; const g = t.parentElement.querySelector(".tghost"); if(g) g.innerHTML = ""; tlSatirGuncelle(t); t.setSelectionRange(t.value.length, t.value.length); return true; }
document.addEventListener("focusout", e=>{ if(e.target.classList && e.target.classList.contains("tin")){ const g = e.target.parentElement.querySelector(".tghost"); if(g) g.innerHTML = ""; delete e.target.dataset.oneri; } });
document.addEventListener("keydown", e=>{ const t = e.target; if(!t.classList || !t.classList.contains("tin")) return; const r = t.closest(".tr"), box = t.closest(".tl");
  if((e.key==="Tab" || e.key==="ArrowRight") && t.dataset.oneri && t.selectionStart===t.value.length){ e.preventDefault(); oneriKabul(t); const bx = t.closest(".tl"); clearTimeout(t._z); t._z = setTimeout(()=>tlSync(bx), 200); return; }
  if(e.key==="Escape" && t.dataset.oneri){ e.preventDefault(); const g = t.parentElement.querySelector(".tghost"); if(g) g.innerHTML = ""; delete t.dataset.oneri; return; }
  if(e.key==="Enter" && !e.shiftKey){ e.preventDefault(); oneriKabul(t); if(!t.value.trim() && r.classList.contains("yeni")) return;
    if(r.classList.contains("yeni")){ tlSync(box); box.lastElementChild.querySelector(".tin").focus(); return; }
    const pos = t.selectionStart, sag = t.value.slice(pos); t.value = t.value.slice(0,pos).trim(); tlSatirGuncelle(t);
    r.insertAdjacentHTML("afterend", tlSatir(sag.trim(), false)); const n = r.nextElementSibling.querySelector(".tin"); tlSatirGuncelle(n); n.focus(); n.setSelectionRange(0,0); tlSync(box); return; }
  if(e.key==="Backspace" && t.selectionStart===0 && t.selectionEnd===0 && !r.classList.contains("yeni")){ const onc = r.previousElementSibling; if(!onc && t.value) return; e.preventDefault();
    if(onc){ const pt = onc.querySelector(".tin"), L = pt.value.length; pt.value = pt.value + (t.value ? (pt.value?" ":"") + t.value : ""); r.remove(); tlSatirGuncelle(pt); pt.focus(); pt.setSelectionRange(L,L); }
    else { r.remove(); box.querySelector(".tin")?.focus(); } tlSync(box); return; }
  if(e.key==="ArrowUp" && t.selectionStart===0){ const p = r.previousElementSibling?.querySelector(".tin"); if(p){ e.preventDefault(); p.focus(); } }
  if(e.key==="ArrowDown" && t.selectionEnd===t.value.length){ const n = r.nextElementSibling?.querySelector(".tin"); if(n){ e.preventDefault(); n.focus(); } } });
document.addEventListener("paste", e=>{ const t = e.target; if(!t.classList || !t.classList.contains("tin")) return; const txt = (e.clipboardData||window.clipboardData)?.getData("text")||""; if(!/\n/.test(txt)) return;
  e.preventDefault(); const r = t.closest(".tr"), box = t.closest(".tl"), L = txt.split(/\r?\n/).map(x=>x.trim()).filter(Boolean); if(!L.length) return;
  const pos = t.selectionStart, bas = t.value.slice(0,pos), son = t.value.slice(t.selectionEnd); t.value = (bas + L[0]).trim(); tlSatirGuncelle(t);
  let cur = r; L.slice(1).forEach((x,k)=>{ cur.insertAdjacentHTML("afterend", tlSatir(k===L.length-2 ? (x+" "+son).trim() : x, false)); cur = cur.nextElementSibling; });
  if(r.classList.contains("yeni") && L.length>1){ r.classList.remove("yeni"); r.insertAdjacentHTML("beforeend", TL_BTN); r.insertAdjacentHTML("afterbegin", TL_GRIP); }
  tlBoyut(box); tlSync(box); });
/* ---------- Blok ekle: ders → tür → (konu) → süre seçerek görev satırı oluşturma ---------- */
const BLK_TUR = [["konusoru","Konu Soru","Konu Soru Çalışması"],["tekrar","Tekrar","Tekrar"],["brans","Branş","Branş Denemesi"],["deneme","Genel Deneme","Genel Deneme"],["sb","Soru bankası","Soru Bankası"],["rutin","Günlük rutin",""]];
const BLK_ETIKET = {};
const BLK_RUTIN = ["Paragraf","Problem"], BLK_ADET = [10,20,30,40];
const turBasili = (b, k) => b.tur===k;
const BLK_SURE = [0.5,1,1.5,2,2.5,3,3.5];
const sureYaz = h => h < 1 ? `${Math.round(h*60)} dk` : `${String(Math.round(h*100)/100).replace(".",",")} saat`;
function sureOku(v){ const t = String(v||"").toLowerCase().replace(",","."), n = parseFloat(t); if(!(n>0)) return null; return /dk|dak/.test(t) || n > 12 ? n/60 : n; }
function blkSatir(b){ if(b.tur==="rutin") return b.rutin ? `${b.rutin} ${b.adet||20} soru` : "";
  const etk = BLK_ETIKET[b.tur] || (BLK_TUR.find(x=>x[0]===b.tur)||[])[2]; if(!etk) return "";
  const ex = b.ex ? b.ex+" " : "";
  let t = b.tur==="deneme" ? `${ex}Genel Deneme` : b.ders ? `${ex}${b.ders} ${etk}` : "";
  if(!t) return ""; if(b.konu.length && b.tur!=="deneme") t += ` – ${b.konu.join(" + ")}`;
  if(b.sure) t += ` (${sureYaz(b.sure)})`; return t; }
function blkDersler(s){ const L = cfg().hedefDers, al = s.alan, oncelik = {SAY:["Matematik","Geometri","Fizik","Kimya","Biyoloji","Türkçe"], EA:["Matematik","Geometri","Edebiyat","Tarih","Coğrafya","Türkçe"], "SÖZ":["Edebiyat","Tarih","Coğrafya","Felsefe","Türkçe","Din Kültürü"]}[al] || [];
  return [...oncelik.filter(x=>L.includes(x)), ...L.filter(x=>!oncelik.includes(x))]; }
function blkKonular(s, b){ if(!b.ders || b.tur==="deneme") return []; return dersSubs(s, b.ders).filter(x=>!b.ex || !x.ex || x.ex===b.ex || /^\d/.test(x.ex)); }
function blkKonuHTML(s, b){ const subs = blkKonular(s, b); if(!subs.length) return `<p class="faint small" style="margin:0">${b.tur==="deneme"?"Genel denemede konu seçilmez.":"Önce ders seç."}</p>`;
  return subs.map(sub=>`<div class="kgrp ex-${subEx(sub)||"x"}" data-grp><div class="gh">${esc(sub.ex||"")} · ${esc(sub.n)}</div>${sub.t.map(n=>`<button type="button" class="kt ${topicScore((s.topics||{})[tkey(sub.k,n)])>=1?"bitti":""}" data-act="bkk" data-v="${esc(n)}" data-q="${esc(trLow(n+" "+sub.n))}" aria-pressed="${b.konu.includes(n)}">${icon("check","xs")}<span>${esc(n)}</span></button>`).join("")}</div>`).join(""); }
function blkGuncelle(){ const s = st(), b = S.blk; if(!b) return;
  document.querySelectorAll("#layer [data-act=bkd]").forEach(x=>x.setAttribute("aria-pressed", x.dataset.v===b.ders));
  document.querySelectorAll("#layer [data-act=bke]").forEach(x=>x.setAttribute("aria-pressed", x.dataset.v===(b.ex||"")));
  document.querySelectorAll("#layer [data-act=bkt]").forEach(x=>x.setAttribute("aria-pressed", turBasili(b, x.dataset.v)));
  document.querySelectorAll("#layer [data-act=bkr]").forEach(x=>x.setAttribute("aria-pressed", x.dataset.v===b.rutin));
  document.querySelectorAll("#layer [data-act=bka]").forEach(x=>x.setAttribute("aria-pressed", +x.dataset.v===(b.adet||20)));
  const fm = $("#sheetForm"); if(fm) fm.dataset.bk = b.tur==="rutin" ? "rutin" : b.tur==="deneme" ? "deneme" : "";
  document.querySelectorAll("#layer [data-act=bks]").forEach(x=>x.setAttribute("aria-pressed", +x.dataset.v===b.sure && !b.elle));
  const out = blkSatir(b), pv = $("#bk-prev"), ek = $("#bk-ekle"); if(pv) pv.innerHTML = out ? esc(out) : `<span class="faint">${b.tur==="rutin"?"Paragraf ya da Problem seç":"Ders ve tür seç"}</span>`; if(ek) ek.disabled = !out;
  const ks = $("#bk-ksay"); if(ks) ks.textContent = b.konu.length ? `${b.konu.length} konu seçili` : "isteğe bağlı"; }
/* Çetelede 10 ve üzeri yanlışa ulaşan konular (program yazarken tekrar önerisi) */
const CETELE_ESIK = 10;
function cetele10(s){ const out = [];
  (isMaarif(s) ? [...maarifList(s,1), ...maarifList(s,2,false)].map(x=>[x.ex, x, x.ders]) : [...CURX().TYT.map(x=>["TYT",x,x.n]), ...aytSubjects(s,false).map(x=>["AYT",x,x.n])])
    .forEach(([ex,sub,ders])=>sub.t.forEach(n=>{ const y = ((s.topics||{})[tkey(sub.k,n)]||{}).y||0; if(y>=CETELE_ESIK) out.push({ex, ders:String(ders).split(" · ")[0], n, y}); }));
  return out.sort((a,b)=>b.y-a.y); }
const ceteleSatir = c => `${c.n} konu tekrarı (${/^\d/.test(c.ex)?"":c.ex+" "}${c.ders})`.replace("( ","(");
/* Konunun sınavı: TYT / AYT / ORT (geometri gibi ortak) */
const subEx = sub => sub.k==="geo" || /TYT\/AYT/.test(sub.g||"") ? "ORT" : (sub.ex==="TYT"||sub.ex==="AYT" ? sub.ex : "");
function konuEx(s, d, n){ const ex = new Set(dersSubs(s, d).filter(x=>x.t.includes(n)).map(subEx)); return ex.size===1 ? [...ex][0] : (ex.size ? "ORT" : ""); }
function konuCipleri(s, d, konu){ return splitKonu(konu).map(n=>{ const e = konuEx(s,d,n); return `<span class="kch ex-${e||"x"}">${e && e!=="ORT"?`<i>${e}</i>`:""}${esc(n)}</span>`; }).join(""); }
/* Net yolculuğu: başlangıç neti ve son 5 deneme ortalaması */
function netYolculugu(s){ const b = s.baslangic||{};
  const ort = tur => { const L = exams(s,tur).slice(-5); return L.length ? {v: L.reduce((a,d)=>a+totalOf(d),0)/L.length, n: L.length} : null; };
  const sat = (tur, k) => { const o = ort(tur), bv = num(b[k]), fark = o && bv!=null ? o.v - bv : null;
    return `<div class="nyr"><span class="nyt">${tur}</span>
      <label class="nyb"><small>Başlangıç</small><input type="text" inputmode="decimal" id="baslangic-${k}" data-f="baslangic.${k}" value="${b[k]??""}" placeholder="${b[k+"Yok"]?"girmedi":"net"}"></label>
      <span class="nyok">→</span>
      <div class="nyg"><small>Son ${o?o.n:5} deneme ort.</small><b class="num">${o?fmt(Math.round(o.v*100)/100):"—"}</b>${fark!=null?`<span class="${fark>=0?"up":"down"} small" style="font-weight:800">${fark>=0?"+":""}${fmt(Math.round(fark*100)/100)}</span>`:""}</div></div>`; };
  return `<div class="card"><h3>Net yolculuğu</h3><div class="nyl">${sat("TYT","tyt")}${s.alan==="DİL"?"":sat("AYT","ayt")}</div></div>`; }
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
  return `${gorusmeKart(S.cur)}<div class="card" style="background:var(--acs);border-color:transparent"><div class="sech"><h3>${icon("eye","sm")} Koç özeti</h3><span class="pill ac">Sadece sen görürsün</span></div>
      <div class="pills" style="margin-top:10px">${(g=>g.list.length?`<span class="pill ac">Hedef konular ${g.done}/${g.list.length}</span>`:"")(weekGoals(s,curStart(s)))}${m.flags.length? m.flags.map(f=>`<span class="pill ${f[0]}">${esc(f[1])}</span>`).join("") : `<span class="pill good">Her şey yolunda görünüyor</span>`}</div></div>
    <div class="kpis">
      ${tile("t-g","target",m.w.pct==null?"—":"%"+Math.round(m.w.pct*100),`Bu hafta uyum · ${m.w.done}/${m.w.all}`)}
      ${tile("t-a","clock",fmtMin(m.w.min),"Bu hafta çalışma")}
      ${tile("t-w","trend",fmt(m.lt),m.dlt!=null?`Son TYT · ${m.dlt>=0?"+":""}${fmt(m.dlt)}`:"Son TYT")}
      ${tile("t-r","flame",m.streak+" gün",m.idle==null?"Henüz hareket yok":m.idle===0?"Bugün aktif":`Son hareket ${m.idle} gün önce`)}
    </div>
    ${netYolculugu(s)}
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
  const bas = list.filter(([,n])=>n.type==="basvuru" && !n.zilGizli), diger = list.filter(([,n])=>n.type!=="basvuru");
  const telL = t => String(t||"").replace(/[^\d+]/g,""), wa = t => { let d = telL(t).replace(/^\+/,""); if(d.startsWith("0")) d = "9"+d; else if(d.length===10) d = "90"+d; return d; };
  const basCard = ([id,n]) => `<div class="nbas"><div class="nbh"><span class="nbi">${icon("user","sm")}</span><div style="min-width:0;flex:1"><div class="nbt">Yeni başvuru · Google Form${!n.read?` <span class="pill good">Yeni</span>`:""}${n.deneme?` <span class="pill">deneme</span>`:""}</div><div class="small muted">${ago(n.at)}</div></div></div>
      <dl><dt>Ad soyad</dt><dd>${esc(n.name||"—")}</dd>${n.hizmet?`<dt>Hizmet</dt><dd>${esc(n.hizmet)}</dd>`:""}${n.alan?`<dt>Alan</dt><dd>${esc(n.alan)}</dd>`:""}${n.tel?`<dt>Telefon</dt><dd>${esc(n.tel)}</dd>`:""}${n.eposta?`<dt>E-posta</dt><dd>${esc(n.eposta)}</dd>`:""}</dl>
      ${(n.cevaplar||[]).length?`<details><summary>Tüm cevaplar (${n.cevaplar.length})</summary><dl style="margin-top:8px">${n.cevaplar.map(x=>`<dt>${esc(x.s)}</dt><dd>${esc(x.c||"—")}</dd>`).join("")}</dl></details>`:""}
      <div class="pills">${n.tel?`<a class="btn sm" href="tel:${esc(telL(n.tel))}">Ara</a><a class="btn sm" href="https://wa.me/${esc(wa(n.tel))}" target="_blank" rel="noopener">WhatsApp</a>`:""}<button class="btn sm pri" data-act="go" data-v="basvuru">Süreci yönet · ${esc(bdLabel(n.durum||"yeni"))}</button><button class="btn sm" data-act="ngizle" data-id="${id}" title="Başvurular'da kalır">Bildirimden kaldır</button></div></div>`;
  return `${topbar(`<h1 class="ttl">Bildirimler</h1>`, bas.length||diger.length?`<button class="btn sm" data-act="ntemizle">${icon("trash","xs")} Tümünü temizle</button>`:"")}
  <div class="page wide">${bas.length?`<h3 style="margin:0">Google Form başvuruları</h3>${bas.map(basCard).join("")}`:""}<div class="card">${diger.length? diger.map(([id,n])=>`<div class="row nrow"><button class="nrowb" data-act="${n.sid&&S.students.has(n.sid)?"open":""}" data-id="${n.sid||""}"><span class="ri" style="${!n.read?"background:var(--acs);color:var(--ac)":""}">${icon(n.type==="kayit"?"user":"alert","sm")}</span><div style="min-width:0"><div class="rt">${label[n.type]||"Bildirim"}${!n.read?` <span class="pill ac">Yeni</span>`:""}</div><div class="rs">${esc(n.name||"")}${n.type==="kayit"?` · ${esc(n.alan||"")} · ${esc(n.sinif||"")}`:" yeni şifre oluşturdu"}</div></div><span class="rx small">${ago(n.at)}</span></button><button class="iconbtn sm nx" data-act="nsil" data-id="${id}" aria-label="Bildirimi sil">${icon("x","sm")}</button></div>`).join("") : `<div class="empty">${bas.length?"Başka bildirim yok.":"Henüz bildirim yok. Bir öğrenci kaydolduğunda ya da Google Form doldurulduğunda burada görünür."}</div>`}</div>
  <p class="faint small" style="text-align:center">Bildirimleri açtıysan bunlar telefonuna da gelir.</p></div>`;
}
function cMore(){
  return `${topbar(`<h1 class="ttl">Daha Fazla</h1>`)}
  <div class="page wide"><h3 class="msec">İşim</h3><div class="card">
    ${(b=>`<button class="row" data-act="go" data-v="basvuru"><span class="ri" style="background:#1E9E4A;color:#fff">${icon("user","sm")}</span><div><div class="rt">Başvurular</div><div class="rs">${b?`${b} başvuru süreçte`:"Süreçte başvuru yok"}</div></div><span class="rx">${icon("chev","sm")}</span></button>`)([...S.notifs.values()].filter(n=>n.type==="basvuru" && !["ogrenci","hayir"].includes(n.durum||"yeni")).length)}
    ${(k=>`<button class="row" data-act="go" data-v="giris"><span class="ri" style="${k?"background:var(--bads);color:var(--bad)":"background:var(--acs);color:var(--ac)"}">${icon("eye","sm")}</span><div><div class="rt">Giriş takibi</div><div class="rs">${k?`${k} öğrenci 3+ gündür girmedi`:"Öğrenciler uygulamaya düzenli giriyor"}</div></div><span class="rx">${icon("chev","sm")}</span></button>`)([...S.students.values()].filter(x=>["kotu","hic"].includes(girisDurum(x).k)).length)}
    ${(c=>`<button class="row" data-act="go" data-v="odeme"><span class="ri" style="background:${c.kirmizi+c.pembe?"var(--bads);color:var(--bad)":"var(--goods);color:var(--good)"}">${icon("cal","sm")}</span><div><div class="rt">Ödemeler ve gelir</div><div class="rs">${c.kirmizi+c.pembe?`${c.kirmizi+c.pembe} geciken`:"Geciken yok"}${c.turuncu?` · ${c.turuncu} yaklaşan`:""}${c.yok?` · ${c.yok} plansız`:""}</div></div><span class="rx">${icon("chev","sm")}</span></button>`)(odemeSay())}
    ${(u=>`<button class="row" data-act="go" data-v="bildirim"><span class="ri" style="${u?"background:var(--acs);color:var(--ac)":""}">${icon("bell","sm")}</span><div><div class="rt">Bildirimler${u?` <span class="pill ac">${u} yeni</span>`:""}</div><div class="rs">Yeni kayıtlar ve başvurular</div></div><span class="rx">${icon("chev","sm")}</span></button>`)([...S.notifs.values()].filter(x=>!x.read).length)}
  </div><h3 class="msec">Uygulama</h3><div class="card">
    <button class="row" data-act="go" data-v="ayarlar"><span class="ri" style="background:var(--acs);color:var(--ac)">${icon("edit","sm")}</span><div><div class="rt">Ayarlar</div><div class="rs">Mesajlar, süreler, hızlı ekle, konu listeleri, şifre</div></div><span class="rx">${icon("chev","sm")}</span></button>
    <button class="row" data-act="sheet" data-v="tema"><span class="ri">${icon("palette","sm")}</span><div><div class="rt">Görünüm</div><div class="rs">Açık / koyu mod ve tema rengi</div></div><span class="rx">${icon("chev","sm")}</span></button>
    <button class="row" data-act="sheet" data-v="sinav"><span class="ri">${icon("cal","sm")}</span><div><div class="rt">YKS tarihi</div><div class="rs">${trDate(S.settings.examDate)}${S.settings.tahmini?" (tahmini)":""} · ${examDays()} gün</div></div><span class="rx">${icon("chev","sm")}</span></button>
    <button class="row" data-act="logout"><span class="ri">${icon("logout","sm")}</span><div><div class="rt">Çıkış yap</div></div></button>
  </div><p class="proto">Zekacademy Koç Paneli</p></div>`;
}

/* ---------- Soru Çözüm (yapay zekâ; sunucuda Claude: önce kolay model, gerekirse güçlü model) ---------- */
const aiC = () => ({ acik:"kapali", pilot:[], aylikHak:120, tavan:50, uyari:40, takipGunluk:15, bonusAcik:true, bonusUyum:70, ...(S.settings.ai||{}) });
const aiAcik = sid => { const c = aiC(); return c.acik==="herkes" || (c.acik==="pilot" && (c.pilot||[]).includes(sid)); };
const aiAy = () => today().slice(0,7);
const callAi = (name, data) => httpsCallable(fns, name, { timeout: 200000 })(data).then(r => r.data);
const SZ_BOS = () => ({ foto:null, onizleme:"", key:"", mod:"coz", metin:"", data:null, shown:0, hints:0, busy:"", aciklama:{}, sohbet:[], benzer:null, benzerSec:"", hata:"", id:"", hak:0, model:"" });
let SZ = SZ_BOS(); SZ.kalan = null; SZ.toplam = null;
function szKullanimYukle(){ if(A() || !S.me) return; getDoc(doc(fdb, "aiKullanim", aiAy()+"_"+S.me)).then(d=>{ const k = d.exists() ? d.data() : {}, c = aiC();
  SZ.toplam = c.aylikHak + (k.bonus||0) + (k.ekHak||0); SZ.kalan = Math.max(0, SZ.toplam - (k.kullanilan||0)); if(S.view==="socoz") render(true); }).catch(()=>{}); }
function szHata(e){ const m = String((e && e.message) || "");
  if(/hak/.test(m) && !/takip/.test(m)) return "Bu ayın soru hakkın bitti. Koçun ek hak verebilir; ayın başında hakların yenilenir.";
  if(/takip/.test(m)) return "Bugünkü “anlamadım / benzer soru” hakkın doldu. Yarın yenilenir.";
  if(/butce/.test(m)) return "Bu ayın Soru Çözüm bütçesi doldu. Ayın başında yeniden açılacak.";
  if(/kapali/.test(m)) return "Soru Çözüm şu an senin için kapalı.";
  if(/anahtar-yok/.test(m)) return "Soru Çözüm henüz kurulmadı. Koçuna haber ver.";
  if(/resim-buyuk/.test(m)) return "Fotoğraf çok büyük. Sadece soruyu içine alacak şekilde tekrar çek.";
  if(/deadline|timeout/i.test(m)) return "Çözüm çok uzun sürdü. Bir kez daha dene.";
  return "Şu an çözemedim, bağlantıda bir sorun var. Biraz sonra tekrar dene. (Hakkın düşmedi.)"; }
const szInline = s => esc(String(s==null?"":s)).replace(/\*\*(.+?)\*\*/g,"<strong>$1</strong>");
function szMd(src){ const out = []; let list = null; const close = () => { if(list){ out.push(`</${list}>`); list = null; } };
  String(src||"").split("\n").forEach(raw=>{ const l = raw.trimEnd(); let m; if(!l.trim()){ close(); return; }
    if((m = l.match(/^#{1,6}\s+(.*)$/))){ close(); out.push(`<p><strong>${szInline(m[1])}</strong></p>`); return; }
    if((m = l.match(/^\s*\d+[.)]\s+(.*)$/))){ if(list!=="ol"){ close(); out.push("<ol>"); list = "ol"; } out.push(`<li>${szInline(m[1])}</li>`); return; }
    if((m = l.match(/^\s*[-*•]\s+(.*)$/))){ if(list!=="ul"){ close(); out.push("<ul>"); list = "ul"; } out.push(`<li>${szInline(m[1])}</li>`); return; }
    close(); out.push(`<p>${szInline(l)}</p>`); }); close(); return out.join(""); }
function szBaglam(){ const d = SZ.data || {}; return JSON.stringify({ soru:d.soru, siklar:d.siklar, ders:d.ders, konu:d.konu, adimlar:d.adimlar, cevap:d.cevap }); }
function szYukleniyor(){ return `<div class="szload"><div class="szph on"><i></i>Soruyu okuyorum</div><div class="szph"><i></i>Çözüyorum</div><div class="szph"><i></i>Her adımı kontrol ediyorum</div><p class="small muted" style="margin:4px 0 0">Zor sorularda bir dakika kadar sürebilir.</p></div>`; }
let szAsama = null;
function szAsamaBaslat(){ clearInterval(szAsama); let i = 0; szAsama = setInterval(()=>{ const ph = document.querySelectorAll(".szph"); if(!ph.length || i >= ph.length-1){ return; } ph[i].className = "szph ok"; i++; ph[i].className = "szph on"; }, 8000); }
function szCozum(){ const d = SZ.data; if(!d) return "";
  if(d.okunabildi===false) return `<div class="szalert warn"><b>Soruyu tam okuyamadım.</b><br>${szInline(d.sorun || "Fotoğraf bulanık ya da soru kesik olabilir.")}<br>Daha net, düz ve tek soruyu gösteren bir fotoğrafla tekrar dene. <b>Hakkın düşmedi.</b></div>`;
  let h = `<div class="szq"><div class="sztags">${d.ders?`<span class="sztag">${esc(d.ders)}</span>`:""}${d.konu?`<span class="sztag k">${esc(d.konu)}</span>`:""}</div><p class="szqt">${szInline(d.soru||"")}</p>${d.siklar && typeof d.siklar==="object" ? `<div class="szqo">${Object.keys(d.siklar).map(k=>`<span><b>${esc(k)})</b> ${esc(d.siklar[k])}</span>`).join("")}</div>` : ""}</div>`;
  if(d.anahtar==="uyumsuz" || d.emin===false) h += `<div class="szalert warn">⚠️ <b>Bu soruda emin olamadım.</b> ${d.anahtar==="uyumsuz" ? "Bulduğum cevap girdiğin cevap anahtarıyla uyuşmuyor; anahtarda baskı hatası da olabilir. " : ""}Kitabın çözümüne de bir göz at.</div>`;
  else if(d.anahtar==="uyumlu") h += `<div class="szalert ok">✓ Cevap anahtarıyla kontrol edildi, uyuşuyor.</div>`;
  if(d.istenen) h += `<div class="szgoal"><span>🎯</span><div><small>Ne isteniyor?</small><p>${szInline(d.istenen)}</p></div></div>`;
  const H = (d.ipuclari||[]).filter(Boolean);
  if(SZ.mod==="ipucu" && !SZ.shown){ const n = Math.max(1, SZ.hints||1);
    h += H.slice(0, n).map((x,i)=>`<div class="szhint"><span>${i+1}</span><p>${szInline(x)}</p></div>`).join("");
    return h + `<div class="szlock"><span>Önce kendin dene 💪 Takılırsan:</span><div class="pills" style="justify-content:center">${n < H.length ? `<button class="btn sm" data-act="szipucu">💡 Bir ipucu daha</button>` : ""}<button class="btn sm pri" data-act="szcozumac">Çözümü göster</button></div></div>`; }
  const bl = (d.bilgi||[]).filter(x=>x && x.ifade);
  if(bl.length) h += bl.map(x=>`<div class="szfact"><small>📌 ${esc(x.ad||"Kullanacağımız bilgi")}</small><div class="szf">${esc(x.ifade)}</div></div>`).join("");
  const A2 = d.adimlar || [], n = Math.min(SZ.shown, A2.length);
  h += `<div class="szsteps">${A2.slice(0, n).map((a,i)=>`<div class="szstep"><span class="szn">${i+1}</span><div class="szsb"><h4>${szInline(a.baslik||("Adım "+(i+1)))}</h4>${a.aciklama?`<p>${szInline(a.aciklama)}</p>`:""}${a.islem?`<div class="szf">${esc(a.islem)}</div>`:""}
    <button class="link small" data-act="szadim" data-v="${i}" ${SZ.busy?"disabled":""}>🤔 ${SZ.aciklama[i] ? "Hâlâ anlamadım" : "Bu adımı anlamadım"}</button>${SZ.aciklama[i]!=null ? `<div class="szex">${SZ.aciklama[i]==="…" ? `<span class="szdots"><i></i><i></i><i></i></span> Daha basit anlatıyorum…` : szMd(SZ.aciklama[i])}</div>` : ""}</div></div>`).join("")}</div>`;
  if(n < A2.length) return h + `<div class="pills"><button class="btn pri" data-act="szsonraki">${n===0?"1. adımı göster":"Sonraki adım →"}</button><button class="btn" data-act="szhepsi">Hepsini göster</button></div>`;
  if(d.cevap) h += `<div class="szans"><span class="szbig">${esc(d.cevap.sik||"✓")}</span><div><small>Cevap</small><b>${d.cevap.sik?esc(d.cevap.sik)+" şıkkı":""}${d.cevap.deger?" · "+esc(d.cevap.deger):""}</b></div></div>`;
  if(d.puf) h += `<div class="sztip"><span>💡</span><div><small>Püf noktası</small><p>${szInline(d.puf)}</p></div></div>`;
  if(SZ.model!=="zor" && !A()) h += `<p class="small muted" style="margin:0;text-align:center">Çözüm yanlış görünüyorsa <button class="link small" data-act="szyanlis" ${SZ.busy?"disabled":""}>daha güçlü modelle tekrar çözdür</button> (2 hak).</p>`;
  return h; }
function szBenzer(){ const q = SZ.benzer; if(!q) return ""; const dogru = String(q.dogru||"").trim().toUpperCase().charAt(0), sec = SZ.benzerSec;
  return `<div class="szquiz"><h3>🔁 Şimdi sıra sende</h3><p class="szqt" style="color:var(--fg)">${szInline(q.soru)}</p><div class="szopts">${Object.keys(q.siklar||{}).map(k=>`<button class="szopt ${sec ? (k===dogru?"dogru":k===sec?"yanlis":"") : ""}" data-act="szsec" data-v="${esc(k)}" ${sec?"disabled":""}><span>${esc(k)}</span>${esc(q.siklar[k])}</button>`).join("")}</div>
    ${sec ? (sec===dogru ? `<div class="szalert ok"><b>Harika, doğru! 🎉</b> Bu konuyu kaptın.</div>` : `<div class="szalert bad">Bu sefer olmadı, sorun değil. Doğru cevap <b>${esc(dogru)}</b>.</div>`) + (Array.isArray(q.cozum) && q.cozum.length ? `<div class="szex"><b>Kısa çözüm</b><ol>${q.cozum.map(x=>`<li>${szInline(x)}</li>`).join("")}</ol></div>` : "") : ""}</div>`; }
function pSoruCoz(){
  const s = !A() && st(), c = aiC(), yuk = SZ.busy==="coz";
  const head = topbar(`<h1 class="ttl">Soru Çözüm</h1>`, "", `<button class="iconbtn" data-act="go" data-v="${A()?"ayarlar":"home"}" aria-label="Geri">${icon("back")}</button>`);
  const hakSerit = SZ.kalan!=null ? `<div class="szhak"><span>Bu ay soru hakkın</span><b class="num">${SZ.kalan}</b><span>/ ${SZ.toplam}</span><i style="--w:${SZ.toplam ? Math.round(SZ.kalan/SZ.toplam*100) : 0}%"></i></div>` : A() ? `<div class="szhak"><span>Koç denemesi · hak düşmez</span></div>` : "";
  const bonus = s && s.aiBonus && s.aiBonus.at && s.aiBonus.at > (s.aiBonusGoruldu||"") ? `<div class="szbonus"><span>🎉</span><p>${esc(s.aiBonus.mesaj)}</p><button class="iconbtn sm" data-act="szbonuskapat" aria-label="Kapat">${icon("x","sm")}</button></div>` : "";
  const form = SZ.data || yuk ? "" : `${hakSerit}<div class="card szform">
      <label class="szdrop" for="szFoto">${SZ.onizleme ? `<img src="${SZ.onizleme}" alt="Seçilen soru"><span><b>Fotoğraf hazır</b><small>Değiştirmek için dokun</small></span>` : `<span class="szdic">${icon("note")}</span><span><b>Sorunun fotoğrafını ekle</b><small>Tek soru, net ve düz olsun</small></span>`}<input type="file" accept="image/*" id="szFoto" hidden></label>
      <div class="sqbtns"><label class="btn pri sm">📷 Kamerayı aç<input type="file" accept="image/*" capture="environment" id="szKamera" hidden></label><label class="btn sm">🖼️ Galeriden seç<input type="file" accept="image/*" id="szGaleri" hidden></label></div>
      <label class="f">Ya da soruyu yaz / not ekle<textarea id="szMetin" rows="2" placeholder="İsteğe bağlı · ör. 12. soru, 18 buldum ama şıklarda yok">${esc(SZ.metin)}</textarea></label>
      <div class="f">Cevap anahtarı (biliyorsan)<div class="szkeys">${["A","B","C","D","E"].map(k=>`<button data-act="szkey" data-v="${k}" aria-pressed="${SZ.key===k}">${k}</button>`).join("")}</div></div>
      <div class="seg">${[["coz","Adım adım çöz"],["ipucu","Önce ipucu"]].map(([k,l])=>`<button data-act="szmod" data-v="${k}" aria-pressed="${SZ.mod===k}">${l}</button>`).join("")}</div>
      ${SZ.hata ? `<div class="err" style="display:block">${esc(SZ.hata)}</div>` : ""}
      <button class="btn pri full" data-act="szgonder" ${SZ.kalan===0?"disabled":""}>${SZ.mod==="coz" ? "Soruyu çöz" : "İpucu ver"}</button>
      <p class="faint small" style="margin:0;text-align:center">Kolay sorular 1 hak, zor sorular 3 hak. Okunamayan fotoğraf hak düşürmez.</p></div>`;
  const devam = SZ.data && SZ.data.okunabildi!==false && (SZ.shown >= (SZ.data.adimlar||[]).length || SZ.mod==="ipucu") ? `<div class="card szdevam">
      <div class="pills">${[["benzer","🔁 Benzer soru ver"],["basit","🤔 Baştan, daha basit anlat"],["hizli","⚡ Sınavda en hızlı yol ne?"]].map(([k,l])=>`<button class="btn sm" data-act="szchip" data-v="${k}" ${SZ.busy?"disabled":""}>${l}</button>`).join("")}</div>
      <div class="szask"><textarea id="szSor" rows="1" placeholder="Aklına takılanı sor…"></textarea><button class="btn pri" data-act="szsor" ${SZ.busy?"disabled":""}>Sor</button></div></div>` : "";
  const sohbet = SZ.sohbet.map(m=>`<div class="szmsg ${m.r}">${m.t==="…" ? `<span class="szdots"><i></i><i></i><i></i></span> Düşünüyor…` : m.r==="me" ? szInline(m.t) : szMd(m.t)}</div>`).join("");
  const alt = SZ.data || yuk ? `<div class="pills" style="justify-content:space-between"><button class="btn" data-act="szyeni" ${SZ.busy?"disabled":""}>+ Yeni soru</button>${SZ.hak ? `<span class="faint small" style="align-self:center">${SZ.hak} hak kullanıldı</span>` : ""}</div>` : "";
  const modSec = s && !SZ.data && !yuk ? `<div class="seg szmodsec"><button aria-pressed="true">📷 Fotoğrafla çöz</button><button data-act="go" data-v="banka" aria-pressed="false">🧩 Soru Bankası</button></div>` : "";
  return `${head}<div class="page sz">${modSec}${SZ.data || yuk ? "" : bonus}${form}${yuk ? szYukleniyor() : ""}${SZ.hata && SZ.data ? `<div class="err" style="display:block">${esc(SZ.hata)}</div>` : ""}<div class="szsol">${szCozum()}</div>${szBenzer()}${sohbet ? `<div class="szchat">${sohbet}</div>` : ""}${devam}${alt}
    ${!SZ.data && !yuk ? `<p class="faint small" style="text-align:center;margin:0">Yapay zekâ hata yapabilir. Cevap anahtarını girersen çözümü ona göre kontrol eder.</p>` : ""}</div>`;
}
async function szFotoSec(file){ if(!file) return; SZ.hata = ""; SZ.foto = file; try{ SZ.onizleme = await resimKucult(file, 360, 60000); }catch(e){ SZ.foto = null; SZ.hata = "Bu fotoğraf açılamadı. Başka bir fotoğraf dene."; } render(); }
async function szGonder(tekrar){
  if(SZ.busy) return; const metin = SZ.metin.trim();
  if(!tekrar && !SZ.foto && !metin){ SZ.hata = "Önce sorunun fotoğrafını ekle ya da soruyu yaz."; render(); return; }
  SZ.hata = ""; SZ.busy = "coz"; if(!tekrar){ SZ.data = null; SZ.shown = 0; SZ.hints = 0; SZ.aciklama = {}; SZ.sohbet = []; SZ.benzer = null; SZ.benzerSec = ""; }
  const eski = tekrar && SZ.data ? szBaglam() : ""; SZ.data = null; render(); window.scrollTo(0,0); szAsamaBaslat();
  try{
    const [resim, kucuk] = SZ.foto ? await Promise.all([resimKucult(SZ.foto, 1568, 700000), resimKucult(SZ.foto, 240, 40000)]) : [null, null];
    const r = await callAi("soruCoz", { resim, kucuk, metin, anahtar: SZ.key, tekrar: eski || undefined });
    SZ.data = r.cozum; SZ.id = r.id; SZ.model = r.model; SZ.hak = (tekrar ? SZ.hak : 0) + (r.hak||0);
    if(r.kalan!=null && !A()){ SZ.kalan = r.kalan; SZ.toplam = r.toplam; }
    SZ.shown = SZ.mod==="coz" ? 1 : 0; SZ.hints = 1;
  }catch(e){ console.warn("soruCoz", e); SZ.hata = szHata(e); }
  finally{ clearInterval(szAsama); SZ.busy = ""; render(); window.scrollTo(0,0); }
}
async function szTakip(tur, gorunen, metin, adim){
  if(SZ.busy || !SZ.data) return; SZ.busy = tur; SZ.hata = "";
  if(tur==="adim") SZ.aciklama[adim] = "…"; else if(tur==="benzer"){ SZ.benzer = null; SZ.benzerSec = ""; SZ.sohbet.push({r:"ai", t:"…"}); } else { SZ.sohbet.push({r:"me", t:gorunen}, {r:"ai", t:"…"}); }
  render(); const yer = tur==="adim" ? null : document.querySelector(".szmsg:last-child"); if(yer) yer.scrollIntoView({behavior:"smooth", block:"center"});
  try{
    const r = await callAi("soruTakip", { tur, baglam: szBaglam(), metin, adim: adim!=null ? adim+1 : undefined });
    if(tur==="adim") SZ.aciklama[adim] = r.metin || "";
    else if(tur==="benzer"){ SZ.sohbet.pop(); SZ.benzer = r.benzer; }
    else SZ.sohbet[SZ.sohbet.length-1] = {r:"ai", t:r.metin || ""};
  }catch(e){ console.warn("soruTakip", e); const m = szHata(e);
    if(tur==="adim") SZ.aciklama[adim] = m; else SZ.sohbet[SZ.sohbet.length-1] = {r:"ai", t:"⚠️ "+m}; }
  finally{ SZ.busy = ""; render(); if(tur==="benzer"){ const q = document.querySelector(".szquiz"); if(q) q.scrollIntoView({behavior:"smooth", block:"start"}); } }
}
function szAct(a, b, v){
  switch(a){
    case "szkey": SZ.key = SZ.key===v ? "" : v; render(); return true;
    case "szmod": SZ.mod = v; render(); return true;
    case "szgonder": szGonder(false); return true;
    case "szyanlis": szGonder(true); return true;
    case "szsonraki": SZ.shown++; render(); { const l = document.querySelectorAll(".szstep"); if(l.length) l[l.length-1].scrollIntoView({behavior:"smooth", block:"center"}); } return true;
    case "szhepsi": SZ.shown = (SZ.data.adimlar||[]).length; render(); return true;
    case "szipucu": SZ.hints = (SZ.hints||1)+1; render(); return true;
    case "szcozumac": SZ.mod = "coz"; SZ.shown = 1; render(); return true;
    case "szadim": szTakip("adim", "", "", +v); return true;
    case "szchip": if(v==="benzer") szTakip("benzer"); else if(v==="basit") szTakip("sohbet", "Baştan, daha basit anlatır mısın?", "Bu soruyu hiç bilmeyen birine anlatır gibi baştan, çok basit anlat. Günlük hayattan küçük bir benzetme kullanabilirsin."); else szTakip("sohbet", "Sınavda en hızlı yol ne?", "Bu soruyu sınavda en hızlı nasıl çözerim? Kısa yol, eleme ya da pratik bir yöntem varsa göster; en fazla 4 madde."); return true;
    case "szsor": { const t = $("#szSor"), q = t && t.value.trim(); if(q) szTakip("sohbet", q, q); return true; }
    case "szsec": SZ.benzerSec = v; render(); return true;
    case "szyeni": { const k = SZ.kalan, tp = SZ.toplam, m = SZ.mod; SZ = SZ_BOS(); SZ.kalan = k; SZ.toplam = tp; SZ.mod = m; render(); window.scrollTo(0,0); return true; }
    case "szbonuskapat": { const s = st(); if(s && s.aiBonus){ s.aiBonusGoruldu = s.aiBonus.at; save(); } render(); return true; }
  }
  return false;
}

/* ---------- Soru Çözüm: koç ayarları ve harcama paneli ---------- */
function aiSet(k, v){ S.settings.ai = { ...(S.settings.ai||{}), [k]: v }; saveSettings(600); }
function aiAyarHTML(){ const c = aiC();
  return `<div class="f">Durum<div class="seg">${[["kapali","Kapalı"],["pilot","Sadece seçtiklerim"],["herkes","Tüm öğrenciler"]].map(([k,l])=>`<label class="segr"><input type="radio" name="aiacik" data-aiacik="1" value="${k}" ${c.acik===k?"checked":""}><span>${l}</span></label>`).join("")}</div></div>
    ${c.acik==="pilot" ? `<div class="f">Deneme öğrencileri<div class="aipil">${sortedStudents().map(([id,x])=>`<label class="inline"><input type="checkbox" data-aipilot="${id}" ${(c.pilot||[]).includes(id)?"checked":""}>${esc(x.name)}</label>`).join("")}</div></div>` : ""}
    <div class="two"><label class="f">Öğrenci başı aylık soru hakkı<input type="number" min="0" step="10" data-ainum="aylikHak" value="${c.aylikHak}"></label>
      <label class="f">Aylık bütçe tavanı ($)<input type="number" min="1" step="5" data-ainum="tavan" value="${c.tavan}"></label></div>
    <div class="two"><label class="f">Uyarı tutarı ($)<input type="number" min="1" step="5" data-ainum="uyari" value="${c.uyari}"></label>
      <label class="f">Günlük “anlamadım / benzer soru” sınırı<input type="number" min="0" step="1" data-ainum="takipGunluk" value="${c.takipGunluk}"></label></div>
    <label class="inline"><input type="checkbox" data-aibool="bonusAcik" ${c.bonusAcik?"checked":""}>Bütçe artarsa her pazartesi çalışkan öğrencilere bonus soru hakkı dağıt</label>
    <label class="f">Bonus için en az haftalık program uyumu (%)<input type="number" min="0" max="100" step="5" data-ainum="bonusUyum" value="${c.bonusUyum}"></label>
    <p class="faint small" style="margin:0">Kolay sorular 1 hak (hızlı model), zor ya da cevap anahtarıyla uyuşmayan sorular 3 hak (güçlü model). Bütçe tavana gelince sistem kendiliğinden durur. Kurulum için Anthropic API anahtarının GitHub'a eklenmiş olması gerekir.</p>
    <div class="pills"><button class="btn sm pri" data-act="go" data-v="aipanel">${icon("chart","xs")} Kullanım ve harcama</button><button class="btn sm" data-act="go" data-v="socoz">${icon("search","xs")} Kendin dene</button></div>`; }
const AIP = { ay:"", kul:[], sorular:[], yuk:false, hata:"" };
function aipYukle(){ const ay = aiAy(); AIP.ay = ay; AIP.yuk = true; AIP.hata = ""; let n = 0; const bitti = () => { if(++n===2){ AIP.yuk = false; if(S.view==="aipanel") render(true); } };
  const u1 = onSnapshot(query(collection(fdb, "aiKullanim"), where("ay","==",ay)), q=>{ AIP.kul = q.docs.map(d=>({id:d.id, ...d.data()})); try{ u1(); }catch(e){} bitti(); }, e=>{ AIP.hata = "Veriler okunamadı."; bitti(); });
  const u2 = onSnapshot(query(collection(fdb, "aiSorular"), where("ay","==",ay)), q=>{ AIP.sorular = q.docs.map(d=>({id:d.id, ...d.data()})).sort((a,b)=>a.at<b.at?1:-1).slice(0,40); try{ u2(); }catch(e){} bitti(); }, e=>{ bitti(); }); }
function cAiPanel(){
  if(AIP.ay !== aiAy() && !AIP.yuk) aipYukle();
  const c = aiC(), g = AIP.kul.find(k=>k.id.endsWith("_genel")) || {}, harc = g.dolar || 0, t = today(), gun = +t.slice(8,10), gs = new Date(+t.slice(0,4), +t.slice(5,7), 0).getDate();
  const tahmin = harc / Math.max(1, gun) * gs, zorOran = g.soru ? Math.round((g.zor||0)/g.soru*100) : 0;
  const days = [...Array(gs)].map((_,i)=>`${t.slice(0,8)}${String(i+1).padStart(2,"0")}`), gv = days.map(d=>(g.gun||{})[d]||0), mx = Math.max(0.01,...gv);
  const ogr = sortedStudents().map(([id,x])=>{ const k = AIP.kul.find(z=>z.id===`${AIP.ay}_${id}`) || {}; const top = c.aylikHak+(k.bonus||0)+(k.ekHak||0); return {id, x, k, top}; })
    .filter(o=>aiAcik(o.id) || o.k.soru).sort((a,b)=>(b.k.kullanilan||0)-(a.k.kullanilan||0));
  const back = `<button class="iconbtn" data-act="go" data-v="ayarlar" aria-label="Geri">${icon("back")}</button>`;
  return `${topbar(`<h1 class="ttl">AI harcama</h1>`, `<button class="iconbtn" data-act="aipyenile" aria-label="Yenile">${icon("trend")}</button>`, back)}
  <div class="page wide">
    ${AIP.hata ? `<div class="err" style="display:block">${esc(AIP.hata)}</div>` : ""}
    <div class="kpis">${tile(harc >= c.uyari ? "t-r" : "t-g","chart",`${harc.toFixed(2)} $`,`Bu ay harcanan · tavan ${c.tavan} $`)}${tile(tahmin > c.tavan ? "t-r" : "t-a","trend",`${tahmin.toFixed(2)} $`,"Bu hızla ay sonu tahmini")}${tile("t-w","search",String(g.soru||0),`Çözülen soru · %${zorOran} güçlü model`)}${tile("t-g","flame",String((g.bonusGecmis||[]).reduce((a,b)=>a+(b.hak||0),0)),"Dağıtılan bonus hak")}</div>
    <div class="card"><div class="sech"><h3>Günlük harcama</h3><span class="faint small">${shortDate(days[0])} – ${shortDate(days[gs-1])}</span></div><div class="aip-bar" style="margin-top:10px">${gv.map((v,i)=>`<i style="height:${v/mx*100}%;${days[i]===t?"opacity:1;background:var(--ac2)":""}" title="${shortDate(days[i])}: ${v.toFixed(3)} $"></i>`).join("")}</div></div>
    <div class="card"><div class="sech"><h3>Öğrenciler</h3><span class="faint small">${c.acik==="kapali" ? "Soru Çözüm kapalı" : c.acik==="pilot" ? "Sadece seçilen öğrenciler" : "Tüm öğrenciler"}</span></div>
      ${ogr.length ? `<div style="overflow-x:auto"><table class="aip-tbl"><thead><tr><th>Öğrenci</th><th class="num">Hak</th><th class="num">Soru</th><th class="num">Güçlü</th><th class="num">$</th><th></th></tr></thead><tbody>${ogr.map(o=>`<tr><td>${esc(o.x.name)}${o.k.bonus?` <span class="pill ac">+${o.k.bonus} bonus</span>`:""}</td><td class="num">${o.k.kullanilan||0}/${o.top}</td><td class="num">${o.k.soru||0}</td><td class="num">${o.k.zor||0}</td><td class="num">${(o.k.dolar||0).toFixed(2)}</td><td><button class="btn sm" data-act="aiekhak" data-id="${o.id}">+10 hak</button></td></tr>`).join("")}</tbody></table></div>` : `<div class="empty">${AIP.yuk ? "Yükleniyor…" : "Henüz kullanan yok. Ayarlar'dan Soru Çözüm'ü açabilirsin."}</div>`}</div>
    <div class="card"><div class="sech"><h3>Son sorular</h3><span class="faint small">${AIP.sorular.length} soru</span></div>
      ${AIP.sorular.length ? AIP.sorular.map(q=>`<div class="aip-q">${q.kucuk?`<img src="${q.kucuk}" alt="">`:`<span class="ri">${icon("note","sm")}</span>`}<div style="min-width:0;flex:1"><b class="small">${esc(S.students.get(q.sid)?.name || "Koç denemesi")}</b> <span class="faint small">· ${ago(q.at)}</span><div class="small muted">${esc([q.ders, q.konu].filter(Boolean).join(" · ") || "—")}</div></div><span class="pill ${q.model==="zor"?"":"ac"}">${q.model==="zor"?"Güçlü":"Hızlı"}</span>${q.anahtar==="uyumsuz"||q.emin===false?`<span class="pill" style="background:var(--warns);color:var(--warn)">emin değil</span>`:""}</div>`).join("") : `<div class="empty">Bu ay henüz soru yok.</div>`}</div>
  </div>`; }
async function aiEkHak(sid){ const id = `${aiAy()}_${sid}`, k = AIP.kul.find(z=>z.id===id) || {}, ek = (k.ekHak||0) + 10;
  try{ await setDoc(doc(fdb, "aiKullanim", id), { sid, ay: aiAy(), ekHak: ek }, { merge: true }); const i = AIP.kul.findIndex(z=>z.id===id); if(i>=0) AIP.kul[i] = {...AIP.kul[i], ekHak: ek}; else AIP.kul.push({id, sid, ay:aiAy(), ekHak: ek}); toast(`${S.students.get(sid)?.name || "Öğrenci"} · +10 soru hakkı verildi`); render(); }
  catch(e){ toast("Hak eklenemedi"); } }

/* ---------- Ayarlar (koç) ---------- */
const clone = x => JSON.parse(JSON.stringify(x));
function cSettings(){
  if(YEDEK===undefined) yedekBilgi().then(()=>{ if(S.view==="ayarlar") keepSettingsOpen(); });
  if(FOTO===undefined) fotoYukle().then(()=>{ if(S.view==="ayarlar") keepSettingsOpen(); });
  const c = cfg(), cur = CURX(), ex = S.setEx || "TYT", sample = {name:"Ayşe Yılmaz"};
  const ta = (id, key, list, rows, ph) => `<textarea id="${id}" data-setlist="${key}" rows="${rows}" placeholder="${ph||""}">${esc(list.join("\n"))}</textarea>`;
  const sec = (title, desc, body, reset, open) => `<details class="card setsec" data-key="set-${esc(String(title).replace(/\s+/g,"-"))}" ${open?"open":""}><summary><span><b>${title}</b><span class="muted small">${desc}</span></span>${icon("chev","sm")}</summary><div class="setbody">${body}${reset?`<div class="pills"><button class="btn sm" data-act="sreset" data-v="${reset}">Varsayılana dön</button></div>`:""}</div></details>`;
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
    ${(()=>{ const oz = paketOzet(), topN = oz.reduce((a,r)=>a+r.n,0), topTL = oz.reduce((a,r)=>a+r.tl,0), keys = new Set(c.paketler.map(p=>p.k));
      const atanmamis = [...S.students.values()].filter(x=>!keys.has(x.paket)).length;
      return sec("Koçluk paketleri", `${c.paketler.length} paket · ${topN} öğrenci · aylık ${fmtTL(topTL)||"0 ₺"}`, `
      <div class="pkgrid">${oz.map((r,i)=>`<div class="pkrow">
        <div class="pkhead"><input type="text" id="pk-n-${i}" data-pk="${i}|n" value="${esc(r.p.n)}" aria-label="Paket adı"><button class="mini" data-act="pkdel" data-i="${i}" aria-label="Paketi sil">${icon("trash","xs")}</button></div>
        <div class="two"><label class="f">Tür<select id="pk-t-${i}" data-pk="${i}|tur"><option value="seans" ${r.p.tur!=="whatsapp"?"selected":""}>Birebir seans</option><option value="whatsapp" ${r.p.tur==="whatsapp"?"selected":""}>WhatsApp · rapor</option></select></label>
        <label class="f">Aylık ücret (₺)<input type="number" min="0" step="50" id="pk-f-${i}" data-pk="${i}|fiyat" value="${r.p.fiyat??""}" placeholder="değişken"></label></div>
        <div class="pkstat"><b class="num">${r.n}</b> öğrenci · aylık <b class="num">${fmtTL(r.tl)||"0 ₺"}</b></div></div>`).join("")}</div>
      <div class="pktop">Toplam: <b class="num">${topN}</b> öğrenci · aylık <b class="num">${fmtTL(topTL)||"0 ₺"}</b></div>
      <p class="faint small" style="margin:0">Aylık toplam, öğrencilerin ödeme planındaki tutarlardan hesaplanır; planı olmayan öğrenci için paketin ücreti alınır. WhatsApp türündeki paketlerde ilk görüşmeden sonra her hafta görüşme yerine haftalık rapor günü olur.</p>
      <div class="pills"><button class="btn sm" data-act="pkadd">${icon("plus","xs")} Paket ekle</button>${atanmamis?`<button class="btn sm pri" data-act="pkata">${atanmamis} öğrenciyi ödeme tutarına göre pakete ata</button>`:""}</div>
      <div class="small" id="pk-out" style="font-weight:600">${esc(S.pkMsg||"")}</div>`, "paketler"); })()}
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
    ${sec("Soru Çözüm (yapay zekâ)", (c=>c.acik==="kapali" ? "Kapalı" : c.acik==="pilot" ? `Deneme · ${(c.pilot||[]).length} öğrenci` : `Açık · aylık ${c.aylikHak} hak · tavan ${c.tavan} $`)(aiC()), aiAyarHTML())}
    ${sec("Bildirimler (koç)", `Bu cihaz: ${typeof Notification==="undefined" ? "desteklemiyor" : Notification.permission==="granted" ? "açık" : Notification.permission==="denied" ? "kapalı" : "izin verilmedi"}`, `
      <p class="muted small" style="margin:0">Yeni kayıt ve başvuru bildirimleri, bildirim izni verdiğin cihazlara gelir. Gelmiyorsa önce bu cihazda bildirimleri yenile, sonra test gönder.</p>
      <div class="pills"><button class="btn sm" data-act="pushyenile">${icon("bell","xs")} Bu cihazda bildirimleri aç / yenile</button><button class="btn sm pri" data-act="bildirimtest">Test bildirimi gönder</button></div>
      <div id="bt-out" class="small"></div>`, "")}
    ${sec("Deneme takvimi", `${takvim().filter(x=>(x.bit||x.bas)>=today()).length} yaklaşan deneme`, `
      <p class="muted small" style="margin:0">Öğrencilerin ana sayfasında önümüzdeki 45 günün denemeleri görünür; yazılı tarihleri her öğrencinin yazılı haftasından otomatik eklenir. Yeni açıklanan denemeyi buraya eklemen yeterli.</p>
      <div class="tkgrid"><span class="gh">Başlangıç</span><span class="gh">Bitiş</span><span class="gh">Yayın</span><span class="gh">Deneme</span><span></span>
      ${takvim().map((x,i)=>`<input type="date" data-tk="${i}|bas" value="${esc(x.bas)}" aria-label="Başlangıç"><input type="date" data-tk="${i}|bit" value="${esc(x.bit||"")}" aria-label="Bitiş"><input type="text" data-tk="${i}|yayin" value="${esc(x.yayin||"")}" aria-label="Yayın"><input type="text" data-tk="${i}|ad" value="${esc(x.ad||"")}" aria-label="Deneme adı"><button class="mini" data-act="tkdel" data-i="${i}" aria-label="Sil">${icon("trash","xs")}</button>`).join("")}</div>
      <div class="pills"><button class="btn sm" data-act="tkadd">${icon("plus","xs")} Deneme ekle</button></div>`, "takvim")}
    ${sec("Kitaplar ve hocalar", `YKS ve Maarif ayrı · ${Object.keys(c.kaynak).filter(k=>k!=="_brans" && !k.startsWith("M:")).length} ders`, `
      <p class="muted small" style="margin:0">Haftalık hedeflerde kitap ve hoca seçerken çıkan listeler. Her satır bir seçenek; “# Başlık” yazan satır grup başlığı olur (ör. # Sıfırdan başlayan).</p>
      ${[...Object.keys(c.kaynak).filter(k=>k!=="_brans" && !k.startsWith("M:")), "_brans", ...Object.keys(c.kaynak).filter(k=>k.startsWith("M:"))].map(d=>`<details class="subj"><summary><span><span class="sn">${d==="_brans"?"Branş denemeleri (YKS, her derste çıkar)":d.startsWith("M:")?"Maarif (9–11. sınıf) · "+esc(d.slice(2)):esc(d)}</span><span class="sg">${(c.kaynak[d]?.kitap||[]).filter(x=>!/^#/.test(x)).length} kitap${d==="_brans"?"":` · ${(c.kaynak[d]?.hoca||[]).length} hoca`}</span></span><span></span><span class="pct">${icon("chev","xs")}</span></summary>
        <div class="two" style="padding:8px 0"><div class="f">Kitaplar${ta("ky-"+d+"-k","kaynak."+d+".kitap",c.kaynak[d]?.kitap||[],7)}</div>${d==="_brans"?"":`<div class="f">Hocalar${ta("ky-"+d+"-h","kaynak."+d+".hoca",c.kaynak[d]?.hoca||[],7)}</div>`}</div></details>`).join("")}`, "kaynak")}
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
    ${sec("Google Form bağlantısı", formDurumYazi(), `<p class="muted small" style="margin:0">Başvuru formun her doldurulduğunda Bildirimler'e yeşil bir “Yeni başvuru” düşer ve telefonuna bildirim gelir. Formdaki kod günde iki kez “çalışıyorum” sinyali yollar; 36 saat sinyal gelmezse sana uyarı gider.</p>
      ${formDurumKart()}
      <div id="formKodOut">${FORMKOD?formKodHTML():`<div class="pills"><button class="btn sm pri" data-act="formkod">Bağlantı kodunu hazırla</button></div>`}</div>`)}
    ${sec("Öğrencileri temizle","Örnek / eski öğrenci kayıtlarını toplu sil",`<p class="muted small" style="margin:0">Seçtiğin öğrencilerin tüm verisi ve giriş hesabı kalıcı olarak silinir (kullanıcı adları yeniden kullanılabilir). Başvurular etkilenmez. Silmeden önce Yedekleme'den yedek indirmen önerilir.</p>
      <div class="tmzl">${sortedStudents().map(([id,x])=>`<label class="inline"><input type="checkbox" class="tmz" value="${id}">${esc(x.name)} <span class="faint small">${x.kullanici?"@"+esc(x.kullanici):""}</span></label>`).join("") || `<span class="faint small">Öğrenci yok.</span>`}</div>
      <div class="pills"><button class="btn sm" data-act="tmzhepsi">Hepsini seç</button><button class="btn sm danger" data-act="tmzsil">Seçilenleri sil</button></div>
      <div class="small" id="tmz-out" style="white-space:pre-wrap;font-weight:600"></div>`, "")}
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
  if(t.dataset.ainum!=null){ const v = Math.max(0, Number(t.value)||0); aiSet(t.dataset.ainum, v); return true; }
  if(t.dataset.aibool!=null && isChange){ aiSet(t.dataset.aibool, t.checked); return true; }
  if(t.dataset.aiacik!=null && isChange){ aiSet("acik", t.value); keepSettingsOpen(); return true; }
  if(t.dataset.aipilot!=null && isChange){ const L = new Set(aiC().pilot||[]); if(t.checked) L.add(t.dataset.aipilot); else L.delete(t.dataset.aipilot); aiSet("pilot", [...L]); return true; }
  if(t.dataset.setb2!=null){ S.settings.bmesaj = {...(S.settings.bmesaj||{}), [t.dataset.setb2]: t.value}; saveSettings(700); return true; }
  if(t.id==="fotoSec"){ if(isChange && t.files && t.files[0]){ const st = $("#fotoDurum"); if(st) st.textContent = "Yükleniyor…"; fotoKaydet(t.files[0]).then(()=>{ keepSettingsOpen(); toast("Fotoğraf kaydedildi"); }).catch(e=>{ if(st) st.textContent = "Yüklenemedi: "+(e.message||e); }); } return true; }
  if(t.dataset.set!=null){ S.settings[t.dataset.set] = t.value; saveSettings(600); if(t.dataset.set==="kurum"||t.dataset.set==="examDate") renderSideOnly(); return true; }
  if(t.dataset.setb!=null && isChange){ S.settings[t.dataset.setb] = t.checked; saveSettings(); return true; }
  if(t.dataset.setlist!=null){ setPath(t.dataset.setlist, t.value.split("\n").map(x=>x.trim()).filter(Boolean)); saveSettings(800); return true; }
  if(t.dataset.tk!=null){ if(!S.settings.takvim) S.settings.takvim = clone(takvim()); const [i,f] = t.dataset.tk.split("|"), r = S.settings.takvim[+i]; if(r){ r[f] = t.value; saveSettings(700); } return true; }
  if(t.dataset.pk!=null){ if(!S.settings.paketler) S.settings.paketler = clone(cfg().paketler); const [i,f] = t.dataset.pk.split("|"), r = S.settings.paketler[+i];
    if(r){ r[f] = f==="fiyat" ? num(t.value) : t.value; saveSettings(700); if(isChange && f!=="n") keepSettingsOpen(); } return true; }
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
    const var_ = [...S.students.entries()].find(([,x])=>x.kullanici===u);
    if(var_){ /* zaten var: ilerlemesine dokunma; sadece eksik koç bilgilerini (ödeme planı, görüşme günü) ve telefonu tamamla */
      const [vid, vx] = var_, eski = S.cnotes.get(vid) || {}, cn = {...eski}, eklenen = [];
      if(o.koc?.odeme && !eski.odeme?.bas){ cn.odeme = o.koc.odeme; eklenen.push("ödeme planı"); }
      if(o.koc?.duzen && (eski.duzen?.gun==null || eski.duzen?.gun==="")){ cn.duzen = {...o.koc.duzen, ...(eski.duzen?.saat?{saat:eski.duzen.saat}:{})}; eklenen.push("görüşme günü"); }
      if(o.kocNotu && !eski.not){ cn.not = o.kocNotu; }
      try{
        if(eklenen.length || cn.not !== eski.not){ S.cnotes.set(vid, cn); await writeDoc("coachNotes", vid, cn); }
        if(o.kayit?.paket && !cfg().paketler.some(p=>p.k===vx.paket)){ vx.paket = o.kayit.paket; await writeDoc("students", vid, vx); eklenen.push("paket"); }
        if(o.kayit?.tel && vx.tel !== o.kayit.tel){ vx.tel = o.kayit.tel; await writeDoc("students", vid, vx); eklenen.push("telefon"); }
        log(eklenen.length ? `↻ ${name}: @${u} zaten vardı; ${eklenen.join(", ")} eklendi` : `– ${name}: @${u} zaten var, değişiklik yok`); skip++;
      }catch(e){ log(`✗ ${name}: ${e.message||e}`); skip++; }
      continue; }
    try{
      const id = await createStudentAccount(u, o.sifre || "123456");
      const rec = {...o.kayit, kullanici:u, ilkSifre:true}; delete rec.not; delete rec.ornek; delete rec.aktarim;
      S.students.set(id, rec); await writeDoc("students", id, rec);
      const cn = {...(o.koc||{}), ...(o.kocNotu ? {not:o.kocNotu} : {})}; /* koc: ödeme planı, haftalık görüşme günü vb. (sadece koç görür) */
      if(Object.keys(cn).length){ S.cnotes.set(id, cn); await writeDoc("coachNotes", id, cn); }
      log(`✓ ${name} → @${u}`); ok++;
    }catch(e){ log(`✗ ${name}: ${authMsg(e)}`); skip++; }
  }
  log(`\nBitti: ${ok} öğrenci aktarıldı${skip?`, ${skip} zaten vardı`:""}.`); b.disabled = false; keepSettingsOpen();
}
async function topluSil(b){ const ids = [...document.querySelectorAll(".tmz:checked")].map(x=>x.value), out = $("#tmz-out"), log = t => { if(out) out.textContent += t + "\n"; };
  if(!ids.length){ toast("Önce öğrenci seç"); return; }
  if(!b.dataset.armed){ b.dataset.armed = "1"; b.textContent = `${ids.length} öğrenci silinsin mi? Tekrar dokun`; setTimeout(()=>{ if(b.isConnected){ delete b.dataset.armed; b.textContent = "Seçilenleri sil"; } }, 4000); return; }
  b.disabled = true; if(out) out.textContent = "";
  for(const id of ids){ const n = S.students.get(id)?.name || id;
    try{ await callFn("ogrenciSil", {uid:id}); S.students.delete(id); S.cnotes.delete(id); log(`✓ ${n} silindi`); }
    catch(e){ log(`✗ ${n}: ${e.message||e}`); } }
  log("Bitti."); b.disabled = false; toast(`${ids.length} öğrenci için silme tamamlandı`); setTimeout(keepSettingsOpen, 1500); }
function onSettingClick(a, b){
  const v = b.dataset.v;
  if(a==="tmzhepsi"){ document.querySelectorAll(".tmz").forEach(x=>x.checked = true); return true; }
  if(a==="tmzsil"){ topluSil(b); return true; }
  if(a==="pushyenile"){ (async()=>{ try{ localStorage.removeItem("zk-push"); }catch(_){} await enablePush(); keepSettingsOpen(); })(); return true; }
  if(a==="bildirimtest"){ const o = $("#bt-out"); if(o) o.innerHTML = `<p class="muted">Gönderiliyor…</p>`; b.disabled = true;
    callFn("bildirimTest", {}).then(r=>{ b.disabled = false; const o2 = $("#bt-out"); if(!o2) return;
      const cihaz = ua => /iphone|ipad/i.test(ua) ? "iPhone" : /android/i.test(ua) ? "Android" : /mac/i.test(ua) ? "Mac" : /windows/i.test(ua) ? "Windows" : "Cihaz";
      const tr = h => ({"messaging/registration-token-not-registered":"cihaz kaydı geçersiz (silindi)","messaging/invalid-registration-token":"geçersiz cihaz kaydı","messaging/third-party-auth-error":"Apple/Google reddetti","messaging/internal-error":"geçici hata"}[h]||h);
      o2.innerHTML = `<div class="card" style="box-shadow:none;border:1px solid var(--line);padding:10px 12px;margin-top:6px">
        <b>${r.cihazlar.length ? `${r.gonderildi}/${r.cihazlar.length} cihaza gönderildi` : "Kayıtlı cihaz yok"}</b>${r.hatalar.length?` · <span style="color:var(--bad)">${esc([...new Set(r.hatalar.map(tr))].join(", "))}</span>`:""}
        <div class="muted" style="margin-top:4px">${r.cihazlar.map(c=>`${cihaz(c.ua)} · son yenileme ${c.at?shortDate(c.at.slice(0,10)):"-"}${c.silindi?" · <b style=\"color:var(--bad)\">silindi</b>":""}`).join("<br>") || "Bu cihazda “Bildirimleri aç / yenile”ye bas."}</div>
        ${r.gecmis.length?`<div style="margin-top:8px"><b>Son bildirim denemeleri</b><div class="muted">${r.gecmis.map(g=>`${new Date(g.at).toLocaleString("tr-TR",{day:"numeric",month:"short",hour:"2-digit",minute:"2-digit"})} · ${esc(g.tur)} · ${g.gonderildi}/${g.cihaz} cihaz${g.hatalar&&g.hatalar.length?` · ${esc([...new Set(g.hatalar.map(tr))].join(", "))}`:""}`).join("<br>")}</div></div>`:""}</div>`;
      toast(r.gonderildi ? "Test gönderildi; telefonuna gelmeli" : "Gönderilecek cihaz yok");
      if(r.gonderildi && r.mid){ o2.insertAdjacentHTML("beforeend", `<div class="fdurum" id="bt-ulas" style="margin-top:6px">Cihazlardan “ulaştı” onayı bekleniyor…</div>`); const t0 = Date.now(), bekle = r.cihazlar.map(c=>cihaz(c.ua));
        const yokla = async () => { let al = []; try{ const d = await getDoc(doc(fdb,"koc","bildirim")); al = ((d.exists() && d.data().alindi) || []).filter(x=>x.mid===r.mid).map(x=>x.cihaz); }catch(_){}
          const u = $("#bt-ulas"); if(!u) return; const kalan = [...bekle]; al.forEach(c=>{ const i = kalan.indexOf(c); if(i>=0) kalan.splice(i,1); });
          const bitti = !kalan.length || Date.now()-t0 > 25000;
          u.className = "fdurum " + (bitti ? (kalan.length ? "kotu" : "iyi") : "");
          u.innerHTML = (al.length ? `Ulaştı: ${al.map(c=>`<b>${c}</b> ✓`).join(", ")}` : "") + (kalan.length ? `${al.length?"<br>":""}${bitti ? "Ulaşmadı" : "Bekleniyor"}: ${kalan.map(c=>`<b>${c}</b>`).join(", ")}${bitti ? " · bu cihazda tarayıcı/uygulama bildirim ayarını ya da pil tasarrufunu kontrol et" : "…"}` : "");
          if(!bitti) setTimeout(yokla, 2500); };
        setTimeout(yokla, 2500); } })
    .catch(e=>{ b.disabled = false; const o2 = $("#bt-out"); if(o2) o2.innerHTML = `<p class="err">Test gönderilemedi: ${esc(e.message||e)}</p>`; }); return true; }
  if(a==="tkadd"){ S.settings.takvim = [{bas:today(), bit:"", yayin:"", ad:""}, ...clone(takvim())]; saveSettings(); keepSettingsOpen(); return true; }
  if(a==="tkdel"){ const L = clone(takvim()); L.splice(+b.dataset.i,1); S.settings.takvim = L; saveSettings(); keepSettingsOpen(); return true; }
  if(a==="pkadd"){ if(!S.settings.paketler) S.settings.paketler = clone(cfg().paketler); S.settings.paketler.push({k:"p"+uid().slice(0,6), n:"Yeni paket", tur:"seans", fiyat:null}); saveSettings(); keepSettingsOpen(); setTimeout(()=>{ const x=document.getElementById("pk-n-"+(S.settings.paketler.length-1)); if(x){ x.focus(); x.select(); } },0); return true; }
  if(a==="pkdel"){ const L = cfg().paketler, p = L[+b.dataset.i]; if(!p) return true; if(L.length<2){ toast("En az bir paket kalmalı"); return true; }
    const n = [...S.students.values()].filter(x=>paketOf(x).k===p.k).length; if(n){ toast(`Bu pakette ${n} öğrenci var; önce onları başka pakete al`); return true; }
    if(!b.dataset.armed){ b.dataset.armed="1"; b.classList.add("danger"); toast("Silmek için tekrar dokun"); return true; }
    S.settings.paketler = clone(L).filter((_,i)=>i!==+b.dataset.i); saveSettings(); keepSettingsOpen(); toast("Paket silindi"); return true; }
  if(a==="pkata"){ const keys = new Set(cfg().paketler.map(p=>p.k)); let n = 0, yok = [];
    S.students.forEach((x,id)=>{ if(keys.has(x.paket)) return; const t = paketTahmin(id); if(!t){ yok.push(x.name); return; } x.paket = t.k; persistDoc("students", id, 0); n++; });
    S.pkMsg = `${n} öğrenci pakete atandı.${yok.length?` Ödeme planı olmadığı için atanamayan: ${yok.join(", ")} (öğrenci düzenle ekranından seç).`:""}`; keepSettingsOpen(); toast(`${n} öğrenci pakete atandı`); return true; }
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
/* Samsung Internet vb. tarayıcılar uygulamayı kendileri paketliyor; Play Protect bunu "güvenli olmayan uygulama" diye engelliyor → Chrome'a yönlendir */
const androidBaskaTarayici = () => isAndroid() && /SamsungBrowser|MiuiBrowser|HuaweiBrowser|YaBrowser|OPR\/|HeyTapBrowser|VivoBrowser|UCBrowser/i.test(navigator.userAgent);
const chromeIntent = () => `intent://${location.host}${location.pathname}${location.search}#Intent;scheme=https;package=com.android.chrome;end`;
function installCard(){
  if(isStandalone()) return "";
  const head = t => `<div class="inst-h"><span class="inst-i">${icon("phone","sm")}</span><div><b>Uygulamayı telefonuna yükle</b><span>${t}</span></div></div>`;
  if(androidBaskaTarayici()) return `<div class="instcard">${head("Bu tarayıcıdan yüklersen telefon “güvenli olmayan uygulama” uyarısı verir. Chrome'dan yükle, uyarı çıkmaz.")}<a class="btn pri full" href="${chromeIntent()}">Chrome'da aç</a><button type="button" class="btn full" data-act="adresKopya" style="margin-top:8px">Adresi kopyala</button><p class="inst-not">Chrome açılınca giriş ekranındaki <b>Uygulamayı yükle</b> düğmesine dokun.</p></div>`;
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
/* Konuları ayır; adında virgül geçen konuları ("İş, Güç ve Enerji" gibi) bölme */
let KONU_ADLARI = null, KONU_KAYNAK = null;
function konuAdlari(){ const kaynak = S.settings.cur || CUR; if(KONU_ADLARI && KONU_KAYNAK===kaynak) return KONU_ADLARI; KONU_KAYNAK = kaynak;
  KONU_ADLARI = new Set([...(kaynak.TYT||[]), ...(kaynak.AYT||[]), ...MAARIF_SUBS].flatMap(x=>x.t||[]).filter(n=>n.includes(","))); return KONU_ADLARI; }
const splitKonu = v => { const p = String(v||"").split(/\s*,\s*/).map(x=>x.trim()).filter(Boolean), A_ = konuAdlari(), out = [];
  for(let i=0;i<p.length;i++){ let al = p[i], j = i; for(let k=Math.min(p.length-1, i+3); k>i; k--){ const aday = p.slice(i,k+1).join(", "); if(A_.has(aday)){ al = aday; j = k; break; } } out.push(al); i = j; }
  return out; };
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
/* ---------- Geri tuşu: önce pencereyi kapat, sonra ana sayfaya dön; ana sayfada iki kez basınca çık ---------- */
let geriSon = 0, geriKurulu = false;
function geriKoruma(){ try{ if(!geriKurulu){ history.replaceState({zk:"kok"}, ""); geriKurulu = true; } if(!(history.state && history.state.zk==="koruma")) history.pushState({zk:"koruma"}, ""); }catch(_){} }
window.addEventListener("popstate", ()=>{
  if(!S.role || !S.ready) return;
  const ana = A() ? "ozet" : "home";
  if($("#layer") && $("#layer").innerHTML.trim()){ closeSheet(); geriKoruma(); return; }
  if($("#dersk")){ dersKapat(); geriKoruma(); return; }
  if(S.view !== ana){ S.view = ana; S.q = ""; render(); window.scrollTo(0,0); geriKoruma(); return; }
  if(Date.now() - geriSon < 2000){ history.back(); return; }
  geriSon = Date.now(); toast("Çıkmak için tekrar geri bas"); geriKoruma();
});
document.addEventListener("toggle", e=>{ const d = e.target; if(d && d.classList && d.classList.contains("mders")){ S.mOpen = S.mOpen||{}; S.mOpen[d.dataset.ders] = d.open; } }, true);
document.addEventListener("keydown", e=>{ if(e.key==="Escape" && $("#layer").innerHTML) closeSheet(); });
const sheetErr = t => { const e=$("#serr"); if(e) e.textContent=t; };

/* ---------- Öğrenme Merkezi (PROTOTİP) ----------
   Video + notlar + özet + test + kartlar + anlamadım. Prototipte öğrenme verisi (ilerleme, notlar, kartlar, test yanlışları)
   bu cihazın hafızasında tutulur; gerçek sürümde öğrencinin kaydına yazılacak. */
/* Konu → video eşleştirmesi (data/video-eslestirme.json'dan üretildi; koçun hoca listesi, en güncel TYT serileri) */
const VIDEO = {"mat|Temel Kavramlar":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["8F-ojRKYTVU","Temel Kavramlar (tek video) Konu Anlatımı","k"]]},"mat|Sayı Basamakları":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["J8vCbkVlx-E","Sayı Basamakları Konu Anlatımı","k"]]},"mat|Rasyonel Sayılar":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Kn35GRczqOM","Rasyonel Sayılar Konu Anlatımı","k"]]},"mat|Bölme ve Bölünebilme":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["fmafVaxx_80","Bölme Bölünebilme Konu Anlatımı","k"]]},"mat|Ebob – ekok":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["KsY4JA_GBt4","Ebob Ekok Konu Anlatımı","k"]]},"mat|Basit Eşitsizlikler":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["2xNWVjgnHNU","Basit Eşitsizlikler Konu Anlatımı","k"]]},"mat|Mutlak Değer":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["IYrBQO9iUug","Mutlak Değer Konu Anlatımı","k"]]},"mat|Üslü Sayılar":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Bqtj4NRkZCo","Üslü Sayılar Konu Anlatımı","k"]]},"mat|Köklü Sayılar":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["3v2bLUpZ7rg","Köklü Sayılar Konu Anlatımı","k"]]},"mat|Çarpanlara Ayırma":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["rR82dLW8qK8","Çarpanlara Ayırma Konu Anlatımı","k"]]},"mat|Oran Orantı":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["VJW58GixYkM","Oran Orantı Konu Anlatımı","k"]]},"mat|Denklem Çözme":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["sEX8jTjVs_M","I ve II Bilinmeyenli Denklemler Konu Anlatımı","k"]]},"prob|Sayı Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|Kesir Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|Yaş Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|Hareket Hız Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|İşçi Emek Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|Yüzde Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|Kar Zarar Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|Karışım Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["Luys_WYJBsU","Problemler Part-1","k"],["WBZRkMVfveQ","Problemler Part-2","k"]]},"prob|Grafik Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["-P3XxaYHfAo","Grafik ve Veri Analizi","k"]]},"prob|Rutin Olmayan Problemleri":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["VWKV-aIClxk","Mantık Analizi","k"]]},"matd|Kümeler-Kartezyen Çarpım":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["mngMZfQVtmA","Kümeler","k"]]},"matd|Fonksiyonlar":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["rUsrVJbScOs","Fonksiyonlar","k"]]},"matd|Permütasyon ve Kombinasyon":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["JHMENIAC_X8","Permütasyon-1","k"],["vXczsrqu9RE","Permütasyon-2","k"],["CxxjhL3zDso","Kombinasyon-1","k"],["oSLCHj5WBn0","Kombinasyon-2","k"],["0z4T6paM5mg","Binom Açılımı-1","k"],["MuZqJKKQc1I","Binom Açılımı-2","k"],["6ezp7N3pUuA","Bölüm Bitirme Testi","s"],["2mhOHyA6L6o","Efişinado Testi","s"]]},"matd|Olasılık":{"h":"Mert Hoca","l":"TYT Matematik Konu Anlatımı 2027 (Tek Videolar)","p":[["wWLodePjvUA","Olasılık-1","k"],["krk0QsWTz40","Olasılık-2","k"],["w6DRg0TBMjk","Bölüm Bitirme Testi","s"],["C_dSLGhzCxo","Efişinado Testi","s"]]},"geo|Doğruda Açılar":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["MFy3DTnf3Zk","Doğruda Açılar 1","k"],["CYgjYxPCyMU","Doğruda Açılar 2","k"]]},"geo|Üçgende Açılar":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["IYU9eFFZf3k","Üçgende Açılar 1","k"],["D5kJMYUTMKI","Üçgende Açılar 2","k"],["is1r0z8GERs","Üçgende Açılar 3","k"],["8mvbCB6p2Cs","Üçgende Açılar 4","k"]]},"geo|Dik Üçgen":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["0Ie1k3knFUo","Dik Üçgen 1","k"],["_2_0NBKVh0Q","Dik Üçgen 2","k"],["SaujJsMorE4","Dik Üçgen 3","k"],["V_uulYI-5jg","Dik Üçgen 4","k"]]},"geo|İkizkenar Üçgen":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["YyisvG8RHOs","İkizkenar Üçgen 1","k"],["lMbQ2KYg-pY","İkizkenar Üçgen 2","k"]]},"geo|Eşkenar Üçgen":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["f4X7lIh0HHE","Eşkenar Üçgen 1","k"],["f6BLdYEXHbU","Eşkenar Üçgen 2","k"]]},"geo|Açıortay":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["3z7U3FMFAkI","Açıortay 1","k"],["ZIgadTHg9Po","Açıortay 2","k"],["pDFEfbfRGc0","Açıortay 3","k"]]},"geo|Kenarortay":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["yGcWu6QSBDM","Kenarortay 1","k"]]},"geo|Eşlik ve Benzerlik":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["0UD2tbQMOhE","Eşlik ve Benzerlik 1","k"],["TblbOFciF8A","Eşlik ve Benzerlik 2","k"],["p0TC--1YlZw","Eşlik ve Benzerlik 3","k"],["329nuGp0MQ0","Eşlik ve Benzerlik 4","k"]]},"geo|Üçgende Benzerlik":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["TblbOFciF8A","Üçgende Benzerlik 1","k"],["p0TC--1YlZw","Üçgende Benzerlik 2","k"],["329nuGp0MQ0","Üçgende Benzerlik 3","k"]]},"geo|Üçgende Alan":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["5iTvWZgLHmY","Üçgende Alan 1","k"],["D_OtwwYn3B4","Üçgende Alan 2","k"],["08I7f2iTBX0","Üçgende Alan 3","k"],["zuKTTqeoRWE","Üçgende Alan 4","k"]]},"geo|Çokgenler":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["rFBQVoBC-8Y","Çokgenler 1","k"],["fp7PD3Y_w0E","Çokgenler 2","k"]]},"geo|Dörtgenler":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["XgWNXN6-2Yc","Dörtgenler 1","k"],["e0in1nP5F4Y","Dörtgenler 2","k"]]},"geo|Yamuk":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["eVcPaSVkB48","Yamuk 1","k"],["E3oFohM8Njw","Yamuk 2","k"],["7elKvY7eEno","Yamuk 3","k"],["AYJS8CZrugU","Yamuk 4","k"]]},"geo|Paralelkenar":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["U3hV4C9E49M","Paralelkenar 1","k"],["eGSF2IDUjBU","Paralelkenar 2","k"],["LU_0LI2QR8A","Paralelkenar 3","k"],["FDEWcmnwO1M","Paralelkenar 4","k"]]},"geo|Eşkenar Dörtgen":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["HXZrjOjQCWQ","Eşkenar Dörtgen 1","k"],["ec-cRwyDdKA","Eşkenar Dörtgen 2","k"]]},"geo|Deltoid":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["NG_iMM2fItc","Deltoid 1","k"],["yTnsTVV9qtE","Deltoid 2","k"]]},"geo|Dikdörtgen":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["CJyp2jcBYV8","Dikdörtgen 1","k"],["OeP4VDwGbHk","Dikdörtgen 2","k"],["BrdHag76cGs","Dikdörtgen 3","k"],["VNrBvQCRK60","Dikdörtgen 4","k"]]},"geo|Kare":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["5_NuouyN6uE","Kare 1","k"],["fYAPYGDWopc","Kare 2","k"],["e00t0gjiKXQ","Kare 3","k"],["r0Im_kS8q-M","Kare 4","k"]]},"geo|Çemberde Açı":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["xqkW5PJIXMM","Çemberde Açı 1","k"],["YRUxcAODUHk","Çemberde Açı 2","k"],["Is7G8bPj2vM","Çemberde Açı 3","k"],["UjfXlGG1S9U","Çemberde Açı 4","k"]]},"geo|Çemberde Uzun":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["LBDtzd5_ihQ","Çemberde Uzun 1","k"],["6xGVpA4CUOw","Çemberde Uzun 2","k"],["KA5OMy5Jzrw","Çemberde Uzun 3","k"],["nXmh62LkFyo","Çemberde Uzun 4","k"]]},"geo|Dairede Çevre ve Alan":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["4Gu6vkai0R8","Dairede Çevre ve Alan 1","k"],["U0IEYS8Z9GY","Dairede Çevre ve Alan 2","k"],["tsUCDsIqfsE","Dairede Çevre ve Alan 3","k"],["1IXnfTu-8RY","Dairede Çevre ve Alan 4","k"]]},"geo|Prizmalar":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["i99dlWUm4U4","Prizmalar 1","k"],["tJ8K6Wz91V8","Prizmalar 2","k"]]},"geo|Silindir":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["NptKniWEKIk","Silindir 1","k"],["kBRocecFtH0","Silindir 2","k"]]},"geo|Piramit":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["loXoB4x7cjU","Piramit 1","k"],["EpWJnpYHXPQ","Piramit 2","k"]]},"geo|Koni":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["l-Z8vjL93L8","Koni 1","k"],["GcKRxvK_1yA","Koni 2","k"]]},"geo|Küre":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["ysgwiPxNOZk","Küre 1","k"],["4BhqTowgJxI","Küre 2","k"]]},"geo|Noktanın Analitiği":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["NJa5wdv20_k","Noktanın Analitiği 1","k"],["RzP6ROtBX20","Noktanın Analitiği 2","k"],["dO_rAqLwGLI","Noktanın Analitiği 3","k"],["UwR2j2xmTOo","Noktanın Analitiği 4","k"]]},"geo|Doğrunun Analitiği":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["fCqXEvvB79o","Doğrunun Analitiği 1","k"],["FY2G2Q0DfqQ","Doğrunun Analitiği 2","k"],["752hjLDvn8Q","Doğrunun Analitiği 3","k"],["LVQF75Jgz80","Doğrunun Analitiği 4","k"],["aQ1IeXOT1io","Doğrunun Analitiği 5","k"],["t2Al-QXu09w","Doğrunun Analitiği 6","k"],["1MOYiXURWTU","Doğrunun Analitiği 7","k"],["tFGYDOi599Q","Doğrunun Analitiği 8","k"],["EqzlUK1a7kk","Doğrunun Analitiği 9","k"],["6kjsjkfUboM","Doğrunun Analitiği 10","k"]]},"geo|Dönüşüm Geometrisi":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["FxEa4BhsDs4","Dönüşüm Geometrisi 1","k"],["mbR-nHmEEjo","Dönüşüm Geometrisi 2","k"],["QSe_ONLcIVQ","Dönüşüm Geometrisi 3","k"],["9ecN3lflVuE","Dönüşüm Geometrisi 4","k"],["dCfQekQOy80","Dönüşüm Geometrisi 5","k"],["AcjlQ_SBvW8","Dönüşüm Geometrisi 6","k"]]},"geo|Çemberin Analitiği":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["HfXJj6HJVJ4","Çemberin Analitiği 1","k"],["EHr7TEGuyC8","Çemberin Analitiği 2","k"],["RRF6p-nKCsM","Çemberin Analitiği 3","k"],["nmduSQhi3gA","Çemberin Analitiği 4","k"],["kFgj1DL9iIM","Çemberin Analitiği 5","k"],["MvBDJ_g100U","Çemberin Analitiği 6","k"]]},"geo|Açı Kenar Bağıntıları":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["pnuij2wmug4","Açı-Kenar Bağıntıları 1","k"],["Ik1vJS9h1vE","Açı-Kenar Bağıntıları 2","k"],["LiurZe73l-0","Üçgenler Bölüm Bitirme Testi 1","s"],["CK2f8rLEsTI","Üçgenler Bölüm Bitirme Testi 2","s"],["9sjMuUEA6No","Üçgenler Efişinado Testi 1","s"],["RD25-YnoI48","Üçgenler Efişinado Testi 2","s"]]},"geo|Özel Dörtgenler":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["XgWNXN6-2Yc","Dörtgenler 1","k"],["di4yA2tEvsw","Dörtgenler-Çokgenler Bölüm Bitirme Testi 1","s"],["TrnGLGDgdKU","Bölüm Bitirme Testi 2","s"],["5wmwSGl4ItU","Efişinado Testi 1","s"],["L5L8qgHY1PI","Efişinado Testi 2","s"]]},"geo|Katı Cisimler":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["i99dlWUm4U4","Prizmalar 1","k"],["OiVHA9uHjz8","Katı Cisimler Bölüm Bitirme Testi 1","s"],["oC_15SImxhw","Bölüm Bitirme Testi 2","s"],["gSWjx2-W2hg","Efişinado Testi 1","s"],["SsOYc3VwEQs","Efişinado Testi 2","s"]]},"geo|Küp":{"h":"Mert Hoca","l":"TYT-AYT Geometri Konu Anlatımı 2027 (60 Günde Geometri)","p":[["i99dlWUm4U4","Prizmalar 1 (küp dahil)","k"],["tJ8K6Wz91V8","Prizmalar 2","k"]]},"kim|Kimya Bilimi":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["ayDKtjR1Rm8","Kimya Dersine Giriş","k"],["duCUXCZQTQM","Simyadan Kimyaya","k"],["LLKF93vAs54","Kimyanın ve Kimyacıların Çalışması","k"],["tlTI8XiBxIw","Kimyanın Sembolik Dili","k"],["WWX-j2zEkTw","İş Sağlığı ve Güvenliği","k"]]},"kim|Atom ve Yapısı":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["jHs5nsAPTzA","Atom Modelleri","k"],["L3zFmvfH5l8","Atomun Yapısı","k"]]},"kim|Periyodik Sistem":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["xTDnVqsYBdQ","Periyodik Sistem","k"],["K0tJ3dlga9k","Elementlerin Sınıflandırılması","k"],["am3PMzxw97k","Periyodik Özellikler 1","k"],["v6HArH6Kd9E","Periyodik Özellikler 2","k"]]},"kim|Kimyasal Türler Arası Etkileşimler":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["rELNDPv4NlM","Kimyasal Türler Arası Etkileşimler","k"],["-rgN0nRTmxE","İyonik Bağ 1","k"],["jouoHKYFiEU","İyonik Bağ 2","k"],["m1Xp593lDCY","Kovalent Bağların Oluşumu","k"],["WlnowYuxJLE","Kovalent Bileşiklerin Adlandırılması","k"],["3qR_YCjUcHU","Zayıf Etkileşimler","k"],["G1ZADh2g--c","Fiziksel ve Kimyasal Değişimler","k"]]},"kim|Maddenin Halleri":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["VZoaFp4YAj4","Maddenin Halleri","k"],["lbCW7oezwhM","Katılar","k"],["hbfiyn-p92w","Sıvılar","k"],["vlx-BvDazm0","Gazlar","k"]]},"kim|Kimyanın Temel Kanunları":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["ArtApyDmbGw","Kütlenin Korunumu Kanunu","k"],["2WeEzROKVZE","Sabit Oranlar Kanunu","k"],["MU_vSjlXaAQ","Katlı Oranlar Kanunu","k"]]},"kim|Kimyasal Hesaplamalar":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["uCU_aTloakI","Mol Kavramı 1","k"],["Bs4QSOGqPNQ","Mol Kavramı 2","k"],["Fguaqi-AAKY","Mol Kavramı Soru Çözümü","s"],["TSEVOp0g0sQ","Kimyasal Tepkime Türleri","k"],["PxTdS5y2Al0","Kimyasal Hesaplamalar 1","k"],["FHfOyLJa0NI","Kimyasal Hesaplamalar 2","k"],["6quyj6fMaT8","Kimyasal Hesaplamalar 3","k"],["41G2hE1x9CU","Kimyasal Hesaplamalar Soru Çözümü","s"]]},"kim|Karışımlar":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["DbqfWCZ5ZHs","Karışımların Sınıflandırılması 1","k"],["_hjCuvmVx-k","Karışımların Sınıflandırılması 2","k"],["3_bnEfIO0oY","Çözünme Süreci","k"],["cclZfTbzZ18","Çözeltilerde Derişim","k"],["F4V31H_Jhdk","Koligatif Özellikler","k"],["CeEgV5BHLus","Ayırma ve Saflaştırma Teknikleri","k"]]},"kim|Asitler, Bazlar ve Tuzlar":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["aAgU4gcJEPg","Asitler ve Bazlar","k"],["_qumqYa03dY","Asit-Baz Tepkimeleri 1","k"],["Nxk2TBgmnGA","Asit-Baz Tepkimeleri 2","k"],["gjyrRYzsiiY","Hayatımızdaki Asitler, Bazlar ve Tuzlar","k"]]},"kim|Kimya Her Yerde":{"h":"Görkem Şahin","l":"2027 / TYT Kimya Video Ders Notları - Konu Anlatım Videoları (Benim Hocam)","p":[["oVSQDxD2khw","Kimya Her Yerde","k"],["p6o2TZe7lgE","Doğa ve Kimya","k"]]},"bio|Canlıların Ortak Özellikleri":{"h":"Betül Biyoloji","l":"2027 TYT Biyoloji Kampı (Günde 2 video, 2 haftada bitir)","p":[["wecoNsYW9gE","Canlıların Ortak Özellikleri","k"],["Kr32jD4Zvow","Bilimsel Yöntem Basamakları","k"]]},"bio|Canlıların Temel Bileşenleri":{"h":"Betül Biyoloji","l":"2027 TYT Biyoloji Kampı (Günde 2 video, 2 haftada bitir)","p":[["UoymYSQQdRM","İnorganik ve Organik Bileşikler","k"],["8Ht9-uObX4c","Karbohidratlar","k"],["AvRMrGjiDXE","Yağlar ve Proteinler","k"],["eWqCd-OMOVc","Enzimler","k"],["gzD8e6ocbGg","Vitaminler, Hormonlar, ATP","k"],["GqOcRwco1YQ","Nükleik Asitler, DNA, RNA","k"]]},"bio|Hücre ve Organeller – Madde Geçişleri":{"h":"Betül Biyoloji","l":"2027 TYT Biyoloji Kampı (Günde 2 video, 2 haftada bitir)","p":[["x1iRW6H4qFQ","Hücre","k"],["C0YllZtb6QI","Zarsız ve Tek Zarlı Organeller","k"],["k3S8u4sbaCo","Çift Zarlı Organeller","k"],["TlPdLWHoIXQ","Hücre Zarı, Hücre Duvarı","k"],["AZrTZfMmMKQ","Madde Geçişleri 1","k"],["l2_X8dPyTF4","Madde Geçişleri 2","k"]]},"bio|Canlıların Sınıflandırılması":{"h":"Betül Biyoloji","l":"2027 TYT Biyoloji Kampı (Günde 2 video, 2 haftada bitir)","p":[["gbESnGsY5_8","Çeşitlilik ve Sınıflandırma","k"],["fwfYAaQxfuE","Bakteriler ve Arkeler","k"],["tinDNgq2_RY","Protista, Bitkiler ve Mantarlar","k"],["2jLNlxU2M38","Hayvanlar Alemi ve Virüsler","k"]]},"bio|Hücrede Bölünme – Üreme":{"h":"Betül Biyoloji","l":"2027 TYT Biyoloji Kampı (Günde 2 video, 2 haftada bitir)","p":[["qtjAG8FIQ9Y","Hücre Bölünmeleri, Mitoz","k"],["jsnEKVwsH5Q","Eşeysiz Üreme","k"],["52AVCgjN6tM","Mayoz Bölünme, Eşeyli Üreme","k"]]},"bio|Kalıtım":{"h":"Betül Biyoloji","l":"2027 TYT Biyoloji Kampı (Günde 2 video, 2 haftada bitir)","p":[["x72DiT88gR4","Kalıtım 1 · Kavramlar, Gamet","k"],["ETAqRdS8LlU","Kalıtım 2 · Monohibrit, Dihibrit","k"],["PKYEwTvYwzQ","Kalıtım 3 · Soyağaçları, Kan Grupları","k"],["mvEBQX5Sdj0","Kalıtım 4 · Eşeye Bağlı Kalıtım","k"]]},"bio|Ekosistem":{"h":"Betül Biyoloji","l":"2027 TYT Biyoloji Kampı (Günde 2 video, 2 haftada bitir)","p":[["ylraslS39LY","Ekosistem Ekolojisi 1","k"],["5RRRpQnNl1g","Ekosistem Ekolojisi 2 · Madde ve Enerji Akışı","k"],["rY_k7QpCTic","Ekosistem Ekolojisi 3 · Çevre Sorunları","k"]]},"tr|Sözcükte Anlam":{"h":"Rüştü Hoca","l":"49 Günde TYT Türkçe Kampı (2026 Tayfa)","p":[["04toVLmAjBk","Sözcükte Anlam 1","k"],["4E4j-aEPPeg","Sözcükte Anlam 2","k"],["b42fQ4fYNHY","Sözcükte Anlam 3","k"],["GvSuD20mBlc","Sözcükte Anlam 4","k"],["N60maMRfhUI","Sözcükte Anlam 5","k"]]},"tr|Söz Yorumu":{"h":"Rüştü Hoca","l":"49 Günde TYT Türkçe Kampı (2026 Tayfa)","p":[["04toVLmAjBk","Sözcükte Anlam 1","k"],["4E4j-aEPPeg","Sözcükte Anlam 2","k"],["b42fQ4fYNHY","Sözcükte Anlam 3","k"],["GvSuD20mBlc","Sözcükte Anlam 4","k"],["N60maMRfhUI","Sözcükte Anlam 5","k"]]},"tr|Deyimler ve Atasözleri":{"h":"Rüştü Hoca","l":"49 Günde TYT Türkçe Kampı (2026 Tayfa)","p":[["04toVLmAjBk","Sözcükte Anlam 1","k"],["4E4j-aEPPeg","Sözcükte Anlam 2","k"],["b42fQ4fYNHY","Sözcükte Anlam 3","k"],["GvSuD20mBlc","Sözcükte Anlam 4","k"],["N60maMRfhUI","Sözcükte Anlam 5","k"]]},"tr|Cümlede Anlam":{"h":"Rüştü Hoca","l":"49 Günde TYT Türkçe Kampı (2026 Tayfa)","p":[["ADw1AqrMnR4","Cümlede Anlam 1","k"],["gPLUCkSmeDI","Cümlede Anlam 2","k"],["bmaqAXMn3pE","Cümlede Anlam 3","k"],["Yu0LbUkoZ04","Cümlede Anlam 4","k"],["3XD3HsSfvlA","Cümlede Anlam 5","k"],["G1ho1KSR4IY","Cümlede Anlam 6","k"],["8Akzdp-21pE","Cümlede Anlam 7","k"]]},"tr|Ses Bilgisi":{"h":"Rüştü Hoca","l":"Dil Bilgisinin Ritmi Kampı 2027","p":[["zRGGapulh30","Ses Bilgisi","k"]]},"tr|Sözcükte Yapı/Ekler":{"h":"Rüştü Hoca","l":"Dil Bilgisinin Ritmi Kampı 2027","p":[["iDFILOYlus8","Sözcükte Yapı 1","k"],["giY3F_oSI3k","Sözcükte Yapı 2","k"]]},"tr|Sözcük Türleri":{"h":"Rüştü Hoca","l":"Dil Bilgisinin Ritmi Kampı 2027","p":[["MJR0GAvY9wY","İsim - Sıfat","k"],["t9PXUsvpSQ0","Zamir - Zarf","k"],["dlRU9PQkwNs","Edat, Bağlaç, Ünlem, Eylem","k"],["cR1gPgPfdIk","Cümle Çeşitleri ve Sözcük Türleri Soru Çözümü","s"]]},"tr|Fiiller-Fiilimsiler-Ek Fiiller-Çatı":{"h":"Rüştü Hoca","l":"49 Günde TYT Türkçe Kampı (2026 Tayfa)","p":[["OwhjLT1PozI","Fiiller","k"],["pJrx6yIP51w","Eylemsi 1","k"],["dKPtZX9iQwY","Eylemsi 2","k"]]},"tr|Cümlenin Ögeleri":{"h":"Rüştü Hoca","l":"Dil Bilgisinin Ritmi Kampı 2027","p":[["ze257o4HpCE","Cümlenin Ögeleri","k"]]},"tr|Cümle Türleri":{"h":"Rüştü Hoca","l":"49 Günde TYT Türkçe Kampı (2026 Tayfa)","p":[["MOZ6j3kQDtA","Cümle Çeşitleri","k"]]},"tr|Anlatım Bozukluğu":{"h":"Rüştü Hoca","l":"Dil Bilgisinin Ritmi Kampı 2027","p":[["XcsUpEr0M1Q","Anlatım Bozukluğu","k"]]},"tr|Yazım Kuralları":{"h":"Rüştü Hoca","l":"Dil Bilgisinin Ritmi Kampı 2027","p":[["Rgn1jyLv-fg","Yazım Kuralları 1","k"],["4KLzFOuf884","Yazım Kuralları 2","k"]]},"tr|Noktalama İşaretleri":{"h":"Rüştü Hoca","l":"Dil Bilgisinin Ritmi Kampı 2027","p":[["OBRoj3NfvTo","Noktalama İşaretleri 1","k"],["gcfWjDnBQ84","Noktalama İşaretleri 2","k"]]},"tr|Paragraf":{"h":"Rüştü Hoca","l":"Paragrafın Ritmi Kampı 2027","p":[["MzbKo_zoaS4","1. Gün · Genel Taktikler","k"],["YbKBWaMhcdg","2. Gün","k"],["iOWbrw2tpFY","3. Gün","k"],["niGOSBj-Cbo","4. Gün","k"],["V2QUqKFlQSk","5. Gün","k"],["ApbCkLDw2hU","6. Gün","k"],["l_GK7b6buNY","7. Gün","k"],["dDdpan4RhhU","9. Gün","k"],["Bzv9-UIIpvA","10. Gün","k"],["umdFcyvC3Bs","11. Gün","k"],["LDSVAvrY15o","12. Gün · 5 Büyük Hata","k"],["4Qhw3t0csBg","13. Gün · Odak Çalışmaları","k"],["RKsZkPqRUyE","14. Gün · Odak Çalışmaları 2","k"],["1xP0ybY5p2E","15. Gün","k"],["Hr6oJGsH0NE","16. Gün · Paragraf Sözlüğü","k"],["H7LQy1Rqm7w","17. Gün","k"],["RPOHXE3DjTM","18. Gün","k"],["_ULBzRzUNGQ","19. Gün","k"],["1TE_TX3YtP8","20. Gün","k"],["v4w1g2PdyzA","21. Gün · Son","k"]]},"tar|TYT Tarih":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["jhWpC9WB5-M","Ders 0 · Tek videoda tüm üniteler","k"]]},"tar|Tarih ve Zaman":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["ChgR5JAg2Q4","Tarih ve Zaman","k"]]},"tar|İnsanlığın İlk Dönemleri":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["87b2HgNM6kE","İnsanlığın İlk Dönemleri","k"]]},"tar|Ortaçağ’da Dünya":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["FPj8nWsE3pg","Ortaçağ’da Dünya","k"]]},"tar|İlk ve Orta Çağlarda Türk Dünyası":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["ZEzpPdYVbKA","İlk ve Orta Çağlarda Türk Dünyası","k"]]},"tar|İslam Medeniyetinin Doğuşu":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["HBW6U7C63es","İslam Medeniyetinin Doğuşu","k"]]},"tar|İlk Türk İslam Devletleri":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["iGdsg6IeiDs","İlk Türk İslam Devletleri","k"]]},"tar|Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["3UW78WR8MUc","Yerleşme ve Devletleşme Sürecinde Selçuklu Türkiyesi","k"]]},"tar|Beylikten Devlete Osmanlı Siyaseti(1300-1453)":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["k-89z_wSA8Y","Beylikten Devlete Osmanlı Siyaseti(1300-1453)","k"]]},"tar|Dünya Gücü Osmanlı Devleti (1453-1600)":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["ubYoI00u3XM","Dünya Gücü Osmanlı Devleti (1453-1600)","k"]]},"tar|Yeni Çağ Avrupa Tarihi":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["9sIfS63rOL8","Yeni Çağ Avrupa Tarihi","k"]]},"tar|Yakın Çağ Avrupa Tarihi":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["i-Fd9Ldt7D0","Yakın Çağ Avrupa Tarihi","k"]]},"tar|Osmanlı Devletinde Arayış Yılları":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["QpVLskV0bMs","Osmanlı Devletinde Arayış Yılları","k"]]},"tar|18. Yüzyılda Değişim ve Diplomasi":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["3qJq9DSjgew","18. Yüzyılda Değişim ve Diplomasi","k"]]},"tar|En Uzun Yüzyıl":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["Rt5FIM02A5U","En Uzun Yüzyıl","k"]]},"tar|Osmanlı Kültür ve Medeniyeti":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["q1i4Bfdz96Y","Osmanlı Kültür ve Medeniyeti","k"]]},"tar|20. Yüzyılda Osmanlı Devleti":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["YhX80CmrdBM","20. Yüzyılda Osmanlı Devleti","k"]]},"tar|I. TBMM Dönemi":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["iRIEtMDcbYY","I. TBMM Dönemi","k"]]},"tar|II. TBMM Dönemi ve Çok Partili Hayata Geçiş":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["EMJklRnnObQ","II. TBMM Dönemi ve Çok Partili Hayata Geçiş","k"]]},"tar|Türk İnkılabı":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["VTerCzUfROI","Türk İnkılabı","k"]]},"tar|Atatürk İlkeleri":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["zeZTHGVHeM0","Atatürk İlkeleri","k"]]},"tar|Atatürk Dönemi Türk Dış Politikası":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["X3O90FDuGqY","Atatürk Dönemi Türk Dış Politikası","k"]]},"tar|I. Dünya Savaşı":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["YhX80CmrdBM","XX. Yüzyıl Başlarında Osmanlı Devleti","k"]]},"tar|Mondros Ateşkesi, İşgaller ve Cemiyetler":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["njRpa0jP9oM","Mondros Ateşkes Antlaşması ve Cemiyetler","k"],["tJTfgRi2SNo","Millî Mücadele Hazırlık Dönemi ve İşgaller","k"]]},"tar|Kurtuluş Savaşına Hazırlık Dönemi":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["tJTfgRi2SNo","Millî Mücadele Hazırlık Dönemi ve İşgaller","k"]]},"tar|Kurtuluş Savaşı ve Antlaşmalar":{"h":"Tarihin Kodları","l":"TYT Tarih · Kodlarla Konu Anlatımı 2027 (Sadettin Akyayla)","p":[["IzgAk6HxabM","Millî Mücadele Muharebeler Dönemi","k"],["swcUCWSk2jM","Mudanya Ateşkesi ve Lozan","k"]]},"cog|Doğa ve İnsan":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["TLVVxhghVd8","Coğrafyanın Bölümleri","k"],["Zx6bArZ49Gg","Coğrafyanın Bölümleri Soru Çözümü","s"],["k7Akbo06kIw","Coğrafyanın Tarihi Gelişimi","k"],["BDTd3m9KY4E","Tarihi Gelişim Soru Çözümü","s"]]},"cog|Dünya’nın Şekli ve Hareketleri":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["Sw3mhjAh6JU","Dünya'nın Şekli ve Hareketleri","k"],["PAMkcASzhfY","Soru Çözümü","s"]]},"cog|Coğrafi Konum":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["zHWck6jNyuo","Coğrafi Konum","k"],["wpAkuhAXT-4","Soru Çözümü","s"]]},"cog|Harita Bilgisi":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["IChJgQdiYJ0","Harita Bilgisi","k"],["6LG3DYgiVJw","Soru Çözümü","s"]]},"cog|Atmosfer ve Sıcaklık":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["JrRJFujEIJw","Atmosferin Katmanları","k"],["LMWkh7rf9QY","Atmosfer Soru Çözümü","s"],["JcKNDqwt-Vc","Sıcaklık","k"],["ckdvJ5g2nnw","Sıcaklık Soru Çözümü","s"]]},"cog|İklimler":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["IwtpdG4u96c","Büyük İklim Tipleri","k"],["oIs4EubPRjs","İklim Tipleri Soru Çözümü","s"],["9ra55hD5WA4","Türkiye İklimi","k"],["ywb5BmVQIpY","Türkiye İklimi Soru Çözümü","s"]]},"cog|Basınç ve Rüzgarlar":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["pOtroRS61nU","Basınç ve Rüzgarlar","k"],["zUu2eLxYyGk","Soru Çözümü","s"]]},"cog|Nem, Yağış ve Buharlaşma":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["srSMADVxKps","Nem ve Yağış","k"],["Y2HMa_KRQXg","Soru Çözümü","s"]]},"cog|İç Kuvvetler / Dış Kuvvetler":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["Dx5bq_L9UYQ","Dünyanın Tektonik Oluşumu","k"],["E7Rs_Jl5grs","Tektonik Oluşum Soru Çözümü","s"],["b-ezTmctZak","İç Kuvvetler","k"],["kmgo1byysio","İç Kuvvetler Soru Çözümü","s"],["KnsjldoMwnU","Kayaçlar","k"],["HJFwn43dx6g","Kayaçlar Soru Çözümü","s"],["cv7V9BfOtr4","Türkiye'de İç Kuvvetler","k"],["ht3Pyze8SW4","Türkiye'de İç Kuvvetler Soru Çözümü","s"],["E3Oluksc-uo","Dış Kuvvetler · Akarsular","k"],["CKHFCHec1Wk","Karstik Şekiller","k"],["VpO-OSf8hfU","Rüzgar ve Buzul","k"],["wrpp0gU5o5o","Dalga ve Akıntılar, Kıyı Tipleri","k"],["4viJ7ANXylk","Türkiye'de Dış Kuvvetler","k"]]},"cog|Su – Toprak ve Bitkiler":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["_oPDRQcj9TU","Dünya'da Sular","k"],["Um_6dyI7yaQ","Türkiye'de Sular","k"],["bw3uotgwtM8","Dünya'da Topraklar","k"],["P93G0P0xbgg","Türkiye'de Topraklar","k"],["5Ta4wvgpNE8","Dünya'da Bitkiler","k"],["KVZS7h0CHBc","Türkiye'de Bitkiler","k"]]},"cog|Nüfus":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["jf_8fVa0CRQ","Nüfusun Önemi ve Özellikleri","k"],["JbU5gnJw5U8","Dünya'da Nüfusun Dağılışı","k"],["U22oGb3dJL8","Nüfus Piramitleri","k"],["myXhBHoMvjw","Türkiye'de Nüfus","k"],["hOm8kalqImA","Türkiye'de Nüfus Soru Çözümü","s"]]},"cog|Göç":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["BHolf82LVxc","Dünya ve Türkiye'de Göçler","k"],["kSMrXNjRCDg","Soru Çözümü","s"]]},"cog|Yerleşme":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["o0tT35Vd8Zo","Dünya'da Yerleşmeler","k"],["ojhybvYpBhY","Türkiye'de Yerleşmeler","k"]]},"cog|Türkiye’nin Yer Şekilleri":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["t0_oJ7FshqI","Türkiye'nin Yer Şekilleri","k"],["kkAM9bnL5gk","Soru Çözümü","s"]]},"cog|Ekonomik Faaliyetler":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["j6CVJ7C5Ywk","Ekonomik Faaliyetler","k"]]},"cog|Bölgeler":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["4Zk6KrzT33U","Bölge ve Bölge Türleri","k"]]},"cog|Uluslararası Ulaşım Hatları":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["ZMbmy-GekAM","Ulaşım","k"]]},"cog|Çevre ve Toplum":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["yPwfZyXlOy0","Çevre ve Toplum","k"]]},"cog|Doğal Afetler":{"h":"Coğrafyanın Kodları","l":"39 Günde TYT Coğrafya Ayrıntılı Kampı 2027","p":[["UGsM0-wcvLU","Afetler","k"],["bG9OPsE4nqU","Afetler Soru Çözümü","s"]]},"fel|Felsefenin Konusu":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["jzsL2q8qVak","Felsefeyi Tanıma ve Felsefe ile Düşünme","k"]]},"fel|Varlık Felsefesi":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["hh2xzwJUJU8","Varlık ve Bilgi Felsefesi","k"]]},"fel|Bilgi Felsefesi":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["hh2xzwJUJU8","Varlık ve Bilgi Felsefesi","k"]]},"fel|Bilim Felsefesi":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["DGbgFNRNxz4","Bilim ve Ahlak Felsefesi","k"]]},"fel|Ahlak Felsefesi":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["DGbgFNRNxz4","Bilim ve Ahlak Felsefesi","k"]]},"fel|Din Felsefesi":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["mepU1SduBxI","Din, Siyaset ve Sanat Felsefesi","k"]]},"fel|Siyaset Felsefesi":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["mepU1SduBxI","Din, Siyaset ve Sanat Felsefesi","k"]]},"fel|Sanat Felsefesi":{"h":"Felsefe Atölyesi","l":"7 Günde TYT Felsefe Kampı 2027","p":[["mepU1SduBxI","Din, Siyaset ve Sanat Felsefesi","k"]]},"fiz|Fizik Bilimine Giriş":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["1Hg2eF907YA","Fizik Bilimine Giriş 1 · Fiziğin Alt Dalları","k",28],["7aVrdQ7uSQ4","Fizik Bilimine Giriş 2 · Fiziksel Büyüklükler","k",28],["PyTaVJVi21c","Fizik Bilimine Giriş Soru Çözümü","s",28]]},"fiz|Madde ve Özellikleri":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["Mhgsu-3ZLNA","Kütle ve Hacim","k",30],["tv64WNuMGn8","Özkütle","k",25],["OSpkdUAQ41o","Karışımların Özkütlesi","k",22],["H0HZrc9-I04","Soru Çözümü 1","s",27],["UrMwq39KF2c","Dayanıklılık","k",24],["Wh0MdHIOWHM","Adezyon ve Kohezyon","k",33],["dhSEXueJg40","Soru Çözümü 2","s",32]]},"fiz|Hareket ve Kuvvet":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["Qp211SqOGJ4","Hareket 1 · Temel Kavramlar","k",37],["C2lKjxiLnkE","Hareket 2 · Düzgün Doğrusal Hareket","k",32],["Cl43P5zbPeo","Hareket 3 · İvme","k",30],["w8PKMoRcjI4","Hareket Soru Çözümü 1","s",27],["EDbz2IbEc44","Hareket Soru Çözümü 2","s",20],["VwxSW7Rmr2U","Kuvvet 1 · Temel Kuvvetler ve Bileşke","k",24]]},"fiz|Dinamik":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["8pWbsm5Fz9U","Kuvvet 2 · Newton'ın Hareket Yasaları","k",37],["DjqPL2eMzVM","Kuvvet 3 · Newton'ın Hareket Yasaları","k",26],["-t8AXflQcVU","Kuvvet 4 · Sürtünme Kuvveti","k",30],["1NGTT1X4lnA","Kuvvet Soru Çözümü 1","s",22],["BhN4puabxW8","Kuvvet Soru Çözümü 2","s",26]]},"fiz|İş, Güç ve Enerji":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["D07mKe56Eis","İş Kavramı","k",29],["WXs6nUyVJ28","Mekanik Enerji","k",31],["Bidoa76lgEk","Enerjinin Korunumu ve Güç","k",32],["gK_GV4z-OjU","Verim ve Enerji Kaynakları","k",23],["0vA8I1D3yq0","Soru Çözümü 1","s",24],["LOpwAg5w_d8","Soru Çözümü 2","s",21]]},"fiz|Isı, Sıcaklık ve Genleşme":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["kGrdvkxHxjA","İç Enerji, Sıcaklık, Isı","k",31],["7HIjhLRs-Dc","Sıcaklık Ölçekleri","k",15],["VhqHkBN6xMQ","Öz Isı ve Isı Sığası","k",29],["3pRu3T0Q03U","Hal Değişimi","k",41],["2-aHeYUXvCI","Isıl Denge","k",32],["CRg4b_g1IXc","Enerji İletim Yolları ve Hızı","k",32],["XRHERBB3kI0","Isı ve Sıcaklık Soru Çözümü 1","s",25],["L3W9YVviHrU","Isı ve Sıcaklık Soru Çözümü 2","s",23],["brzhvf6-L_I","Genleşme 1","k",23],["iOkBQ3GBVk8","Genleşme 2","k",22],["YJJfmAinEhI","Genleşme Soru Çözümü","s",31]]},"fiz|Elektrik":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["jLdxW888qsg","Elektrostatik 1 · Elektrik Yükleri","k",20],["xieg5ohrPGs","Elektrostatik 2 · Elektriklenme Çeşitleri","k",37],["NqzDtAGqbQY","Elektrostatik 3 · Elektroskop","k",28],["AL7H47SY968","Elektrostatik 4 · İletken ve Yalıtkanlar","k",29],["qb2_VWVm_oQ","Elektrostatik 5 · Coulomb Kuvveti","k",19],["u2Y616NLBBs","Elektrostatik 6 · Elektrik Alan","k",23],["6jbPjwbPXls","Elektrostatik Soru Çözümü 1","s",27],["VKrJ1GJX0zE","Elektrostatik Soru Çözümü 2","s",23],["eFizWwjLopQ","Elektrik Akımı ve Potansiyel Fark","k",38],["Tap34nISlqg","Direnç","k",25],["uq9Q7seOe28","Ohm Yasası","k",42],["urZkI2qOtYo","Dirençlerin Bağlanması","k",38],["MjctdUFHILE","Üreteçlerin Bağlanması","k",29],["9CbekU-8WwQ","Elektrik Devreleri Soru Çözümü 1","s",19],["RwsGiXMimEw","Elektrik Devreleri Soru Çözümü 2","s",18],["zN7DKUvyqzA","Elektriksel Güç ve Lambalar","k",38],["Y8cJuEqETI0","Elektriksel Güç Soru Çözümü 1","s",24],["cbqBhmByflM","Elektriksel Güç Soru Çözümü 2","s",18]]},"fiz|Manyetizma":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["p6zLfL59v8Y","Mıknatıs ve Manyetik Alan","k",34],["57NKxjQkOoU","Akım ve Manyetik Alan","k",35],["WT5V4wGrSBM","Elektromıknatıs","k",22],["aMpvY7w8rK4","Dünya'nın Manyetik Alanı","k",14],["9k17_RBIXeg","Soru Çözümü 1","s",31],["OOZ-NFlWebY","Soru Çözümü 2","s",21]]},"fiz|Basınç":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["DnQNBoR_Dsw","Katı Basıncı","k",29],["5Hr5osikAlk","Katı Basıncı Soru Çözümü","s",20],["dkwbOGhBedc","Sıvı Basıncı 1","k",26],["8XFD833ngJc","Sıvı Basıncı 2","k",23],["jOKADXphfC8","Sıvı Basıncı 3","k",29],["bYnkDV0LJ5o","Açık Hava Basıncı","k",32],["8EvdMuWG6kU","Kapalı Kaplarda Gaz Basıncı","k",29],["pduzOUiY1uM","Basınç Ölçen Aletler","k",27],["1Q3CtzfV1lQ","Akışkanların Basıncı","k",26],["PQM2gVZrgS4","Durgun Sıvı ve Akışkan Basıncı Soru Çözümü 1","s",26],["2Y3BQddhguA","Durgun Sıvı ve Akışkan Basıncı Soru Çözümü 2","s",16],["PmJmQpttSnY","Gaz Basıncı Soru Çözümü 1","s",22],["iUDFx-qjjeM","Gaz Basıncı Soru Çözümü 2","s",23]]},"fiz|Sıvıların Kaldırma Kuvveti":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["XQHH2VV1Bbk","Kaldırma Kuvveti 1","k",34],["IX2LZ_CYJQI","Kaldırma Kuvveti 2","k",34],["EkNxYWi-uKM","Soru Çözümü 1","s",31],["-uyoBz_bC4I","Soru Çözümü 2","s",28]]},"fiz|Optik":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["1O3Q5X8mleQ","Işık Şiddeti ve Işık Akısı","k",24],["T9g5QdOr8Mo","Aydınlanma Şiddeti","k",24],["ceSzQEruRxQ","Aydınlanma Soru Çözümü","s",24],["dd-BhlkKSuU","Gölge 1","k",26],["9hgQWVXqn6s","Gölge 2","k",30],["0XJt3FaWS5M","Gölge Soru Çözümü","s",21],["ixgV1NTdISQ","Yansıma ve Yansıma Kanunları","k",34],["6Ol1f4UKsnM","Düzlem Ayna 1","k",36],["Niuye4Sxiio","Görüş Alanı · Düzlem Ayna 2","k",22],["PuGnerpUo14","Düzlem Ayna Soru Çözümü","s",27],["9Qv8MXWL4yc","Çukur Aynada Özel Işınlar","k",31],["jczDv1QHAic","Tümsek Aynada Özel Işınlar","k",14],["JK8l1zMiw0g","Çukur Aynada Görüntü","k",39],["W8H3bTK4JxE","Tümsek Aynada Görüntü","k",19],["Xn-W093iEGA","Küresel Aynalar Soru Çözümü","s",26],["HBGioahDgyA","Kırılma İndisi, Snell Yasası","k",33],["ffttO_LOmR8","Sınır Açısı ve Tam Yansıma","k",39],["DfDdkMfeUIo","Küresel Yüzeylerden Geçiş ve Görünür Uzaklık","k",25],["LrekDijm8Qc","Işığın Kırılması Soru Çözümü","s",33],["7UGITYRh8ds","Mercekler ve Odak Uzaklığı","k",33],["APT59L7PrxQ","Merceklerde Özel Işınlar","k",23],["Kb1V3qLPO8U","Merceklerde Görüntü","k",40],["EkaOHdAYKzI","Mercekler Soru Çözümü","s",31],["gSmX1oqE7sg","Prizmalar","k",33],["gFXIw6RN7cg","Renkler","k",40],["S6wH6_nZoEs","Prizma ve Renkler Soru Çözümü","s",24]]},"fiz|Dalgalar":{"h":"Özcan Aykın","l":"2027 - 55 Günde TYT Fizik Kampı","p":[["p13oQVkAzR0","Dalgalar 1 · Temel Kavramlar","k",34],["1QpDnuEAm2s","Dalgalar 2 · Sınıflandırma","k",28],["bRbvtVB4ZDc","Yay Dalgaları 1","k",38],["IvCvvEQeGrg","Yay Dalgaları 2","k",38],["sPS084MAn88","Yay Dalgaları 3","k",32],["o4QOA4JWjqo","Yay Dalgaları Soru Çözümü","s",27],["W2kxJOz57Bc","Su Dalgası 1","k",21],["HXTKAnIUe1c","Su Dalgası 2","k",31],["rvcpdc5-v9w","Su Dalgası 3","k",16],["85SvEQsvJgM","Su Dalgası 4","k",40],["KAmjPBtPfMk","Su Dalgaları Soru Çözümü","s",37],["CJh-XzyR6Dg","Ses ve Deprem Dalgaları","k",44],["VMGG-hcx5JM","Ses ve Deprem Dalgaları Soru Çözümü","s",22]]}};
const DERS_ICERIK = {
  "mat|Temel Kavramlar": { vid:"8F-ojRKYTVU", baslik:"Temel Kavramlar Konu Anlatımı · 70 Günde TYT Matematik",
    ozet:["**Rakam** sayıları yazmak için kullanılan 10 semboldür: 0, 1, 2, … 9. Sayılar rakamlardan oluşur.",
      "**Tek / çift:** tek + tek = çift, tek · tek = tek. Çarpanlardan biri çiftse sonuç çifttir.",
      "**0** çift sayıdır; ne pozitif ne negatiftir.",
      "**Ardışık sayılar:** n tane ardışık sayının toplamı = ortadaki sayı × n."],
    formul:[{ad:"1'den n'ye toplam", ifade:"n · (n + 1) ÷ 2"},{ad:"Terim sayısı", ifade:"(son − ilk) ÷ artış + 1"}],
    kart:[["0 tek mi çift mi?","Çift. Ama ne pozitif ne negatif."],["tek · tek = ?","tek (bir çarpan çiftse sonuç çift)"],["1'den n'ye kadar sayıların toplamı?","n · (n + 1) ÷ 2"],["Ardışık 5 sayının toplamı 60 ise ortadaki sayı?","60 ÷ 5 = 12"],["Terim sayısı formülü?","(son − ilk) ÷ artış + 1"]],
    test:[{q:"a, b ve c birbirinden farklı rakamlardır. Buna göre a + b + c toplamının alabileceği en büyük değer kaçtır?", s:{A:"21",B:"22",C:"23",D:"24",E:"27"}, d:"D", c:"Farklı rakamlar demek: en büyük üç rakamı seç → **9 + 8 + 7 = 24**. 27 için üçünün de 9 olması gerekirdi."},
      {q:"x ve y tam sayılardır. x + y = 7 olduğuna göre x · y çarpımı aşağıdakilerden hangisi olamaz?", s:{A:"−8",B:"0",C:"10",D:"11",E:"12"}, d:"D", c:"Toplamı 7 olan çiftler: (−1)·8 = **−8**, 0·7 = **0**, 2·5 = **10**, 3·4 = **12**. 11 = 1·11 ya da (−1)·(−11); bunların toplamı 7 değil."},
      {q:"Ardışık üç çift sayının toplamı 66 ise en büyüğü kaçtır?", s:{A:"20",B:"22",C:"24",D:"26",E:"28"}, d:"C", c:"Ortadaki = 66 ÷ 3 = **22**. Çift sayılar 2'şer artar: 20, 22, **24**. Dikkat: 22 ortadaki sayı."}] },
  "mat|Rasyonel Sayılar": { vid:"Kn35GRczqOM", baslik:"Rasyonel Sayılar Konu Anlatımı · 70 Günde TYT Matematik",
    ozet:["Toplama ve çıkarmada önce **paydalar eşitlenir**.","Bölmede ikinci kesir **ters çevrilip çarpılır**.","Sıralarken ondalığa çevir ya da payları / paydaları eşitle.","**İşlem önceliği:** parantez → çarpma ve bölme → toplama ve çıkarma."],
    formul:[{ad:"Bölme", ifade:"a/b ÷ c/d = a/b × d/c"},{ad:"Devirli sayı", ifade:"0,3̄ = 3/9 = 1/3"}],
    kart:[["a/b ÷ c/d = ?","a/b × d/c"],["Payları eşit iki kesirden hangisi büyük?","Paydası küçük olan"],["0,3̄ kaça eşittir?","3/9 = 1/3"],["1/2 + 1/3 = ?","5/6"],["İşlem önceliği?","Parantez → çarpma/bölme → toplama/çıkarma"]],
    test:[{q:"(1/2 + 1/3) ÷ 5/6 işleminin sonucu kaçtır?", s:{A:"5/6",B:"1",C:"6/5",D:"5/3",E:"2"}, d:"B", c:"Parantez: 1/2 + 1/3 = **5/6**. Sonra 5/6 ÷ 5/6 = **1**."},
      {q:"0,2 + 0,3 · 0,4 işleminin sonucu kaçtır?", s:{A:"0,12",B:"0,2",C:"0,32",D:"0,5",E:"0,9"}, d:"C", c:"Önce çarpma: 0,3 · 0,4 = **0,12**. Sonra 0,2 + 0,12 = **0,32**. Soldan sağa yapan 0,2 bulur."},
      {q:"a = 3/4, b = 2/3 ve c = 5/6 olduğuna göre aşağıdaki sıralamalardan hangisi doğrudur?", s:{A:"a < b < c",B:"b < a < c",C:"b < c < a",D:"c < a < b",E:"a < c < b"}, d:"B", c:"Paydaları 12 yap: a = **9/12**, b = **8/12**, c = **10/12**. Yani b < a < c."}] },
  "mat|Basit Eşitsizlikler": { vid:"2xNWVjgnHNU", baslik:"Basit Eşitsizlikler Konu Anlatımı · 70 Günde TYT Matematik",
    ozet:["İki tarafa aynı sayı eklenir ya da çıkarılırsa **yön değişmez**.","**Negatif** bir sayıyla çarpınca ya da bölünce **yön değişir**.","a < x < b aralığındaki tam sayı sayısı = **b − a − 1**.","0 < x < 1 ise **x² < x** olur."],
    formul:[{ad:"Negatife bölme", ifade:"−3x > 12 ⇒ x < −4"},{ad:"Tam sayı adedi", ifade:"a < x < b ⇒ b − a − 1 tane"}],
    kart:[["−2x < 6 ⇒ ?","x > −3 (negatife bölünce yön değişir)"],["−2 < x < 3 aralığında kaç tam sayı var?","3 − (−2) − 1 = 4"],["0 < x < 1 ise x² mi büyük x mi?","x büyük (x² < x)"],["x² < 0 olabilir mi?","Hayır, her zaman x² ≥ 0"],["a ≤ x ≤ b aralığında kaç tam sayı var?","b − a + 1"]],
    test:[{q:"−2 < x < 3 eşitsizliğini sağlayan kaç farklı x tam sayısı vardır?", s:{A:"2",B:"3",C:"4",D:"5",E:"6"}, d:"C", c:"Uçlar dahil değil: −1, 0, 1, 2 → **4** tane. Uçları dahil eden 6 bulur."},
      {q:"3x + 2 ≤ 20 eşitsizliğini sağlayan en büyük x tam sayısı kaçtır?", s:{A:"5",B:"6",C:"7",D:"8",E:"18"}, d:"B", c:"3x ≤ 18 ⇒ x ≤ **6**. Eşitlik dahil olduğu için en büyük değer 6."},
      {q:"−3x > 12 eşitsizliğinin çözüm kümesi aşağıdakilerden hangisidir?", s:{A:"x < −4",B:"x > −4",C:"x < 4",D:"x > 4",E:"x > −36"}, d:"A", c:"İki tarafı **−3'e** böl: negatife bölünce yön değişir ⇒ **x < −4**."}] },
  "mat|Mutlak Değer": { vid:"IYrBQO9iUug", baslik:"Mutlak Değer Konu Anlatımı · 70 Günde TYT Matematik",
    ozet:["|x|, sayı doğrusunda x'in 0'a **uzaklığıdır**; hiçbir zaman negatif olmaz.","|x| = a (a > 0) ise **x = a veya x = −a**.","|x| < a ise **−a < x < a**; |x| > a ise x > a veya x < −a.","|a − b|, a ile b arasındaki **uzaklıktır**."],
    formul:[{ad:"Denklem", ifade:"|x − 2| = 5 ⇒ x = 7 veya x = −3"},{ad:"Eşitsizlik", ifade:"|x − c| < r ⇒ c − r < x < c + r"}],
    kart:[["|−7| = ?","7"],["|x| = 4 ⇒ ?","x = 4 veya x = −4"],["|x − 1| < 3 ⇒ ?","−2 < x < 4"],["|a − b| ne anlama gelir?","a ile b arasındaki uzaklık"],["|x| = −2 denkleminin çözümü?","Yok; mutlak değer negatif olamaz"]],
    test:[{q:"|−5| − |3 − 7| işleminin sonucu kaçtır?", s:{A:"−1",B:"1",C:"2",D:"9",E:"12"}, d:"B", c:"|−5| = **5**, |3 − 7| = |−4| = **4**. 5 − 4 = **1**."},
      {q:"|x − 2| = 5 denklemini sağlayan x değerlerinin toplamı kaçtır?", s:{A:"4",B:"5",C:"7",D:"10",E:"14"}, d:"A", c:"x − 2 = 5 ⇒ **7**; x − 2 = −5 ⇒ **−3**. Toplam 7 + (−3) = **4**."},
      {q:"|x − 1| < 3 eşitsizliğini sağlayan kaç farklı x tam sayısı vardır?", s:{A:"3",B:"4",C:"5",D:"6",E:"7"}, d:"C", c:"−3 < x − 1 < 3 ⇒ −2 < x < 4: −1, 0, 1, 2, 3 → **5** tane."}] }
};
Object.assign(DERS_ICERIK, {
  "fiz|Fizik Bilimine Giriş": { vid:"1Hg2eF907YA", kanal:"Özcan Aykın", baslik:"55 Günde TYT Fizik Kampı · 1. Gün · Fizik Bilimine Giriş",
    parca:[["1Hg2eF907YA","Fiziğin Alt Dalları","konu",28],["7aVrdQ7uSQ4","Fiziksel Büyüklükler","konu",28],["PyTaVJVi21c","Soru Çözümü","soru",28]],
    ozet:["Fizik; **madde ve enerjiyi**, ikisi arasındaki etkileşimi inceler.","**Temel büyüklükler** (7 tane): uzunluk, kütle, zaman, sıcaklık, elektrik akımı, madde miktarı, ışık şiddeti. Diğerleri **türetilmiş** büyüklüktür.","**Skaler** büyüklükte sayı ve birim yeter (kütle, zaman, enerji). **Vektörel** büyüklükte yön de gerekir (kuvvet, hız, ivme).","Alt dallar: mekanik, termodinamik, elektromanyetizma, optik, atom ve nükleer fizik, katıhal fiziği."],
    formul:[{ad:"Temel SI birimleri", ifade:"m · kg · s · K · A · mol · cd"},{ad:"Türetilmiş örnek", ifade:"hız = yol ÷ zaman → m/s"}],
    kart:[["Kütle skaler mi vektörel mi?","Skaler"],["Ağırlık skaler mi vektörel mi?","Vektörel (aşağı yönlü bir kuvvet)"],["Sıcaklığın SI birimi?","Kelvin (K)"],["Kuvvet temel mi türetilmiş mi?","Türetilmiş (newton = kg·m/s²)"],["Elektrik akımının SI birimi?","Amper (A)"]],
    test:[{q:"Aşağıdakilerden hangisi temel büyüklüktür?", s:{A:"Kuvvet",B:"Hız",C:"Enerji",D:"Elektrik akımı",E:"Basınç"}, d:"D", c:"7 temel büyüklükten biri **elektrik akımıdır** (amper). Kuvvet, hız, enerji ve basınç temel büyüklüklerden türetilir."},
      {q:"Aşağıdakilerden hangisi vektörel bir büyüklüktür?", s:{A:"İvme",B:"Kütle",C:"Zaman",D:"Sıcaklık",E:"Enerji"}, d:"A", c:"**İvmenin** yönü vardır, bu yüzden vektöreldir. Kütle, zaman, sıcaklık ve enerji skalerdir."},
      {q:"Buzdolabının soğutma sisteminin çalışma ilkesi fiziğin en çok hangi alt dalının konusudur?", s:{A:"Mekanik",B:"Optik",C:"Termodinamik",D:"Atom fiziği",E:"Nükleer fizik"}, d:"C", c:"Isı aktarımı ve sıcaklık değişimi **termodinamiğin** konusudur."}] },
  "kim|Kimya Bilimi": { vid:"WsP2LkGg5q4", kanal:"Mihriban Hoca İle Kimya", baslik:"Kimya Bilimi · 30 Günde TYT Kimya Kampı",
    ozet:["**Simya** deneme-yanılmaya dayanır, sistematik bilgi birikimi yoktur. **Kimya** bilimsel yöntemle çalışır.","**Robert Boyle** ile kimya bir bilim olmaya başladı; **Lavoisier** kütlenin korunumunu gösterdi.","**Element** tek tür atomdan oluşur (Fe, O₂). **Bileşik** farklı atomların belirli oranda birleşmesidir (H₂O).","Alt dallar: analitik, organik, anorganik, fizikokimya, biyokimya, polimer, endüstriyel kimya."],
    formul:[{ad:"Sembol kuralı", ifade:"İlk harf büyük, ikincisi küçük"},{ad:"Dikkat", ifade:"Co = kobalt · CO = karbon monoksit"}],
    kart:[["Kimyayı bilim yapan ilk bilim insanı?","Robert Boyle"],["O₂ element mi bileşik mi?","Element (tek tür atom)"],["H₂O element mi bileşik mi?","Bileşik (H ve O)"],["Co ile CO arasındaki fark?","Co kobalt elementi; CO karbon monoksit bileşiği"],["Maddenin bileşimini ve miktarını belirleyen alt dal?","Analitik kimya"]],
    test:[{q:"Aşağıdakilerden hangisi bileşiktir?", s:{A:"NaCl",B:"N₂",C:"Fe",D:"O₃",E:"He"}, d:"A", c:"**NaCl** iki farklı elementten (Na ve Cl) oluşur. N₂, Fe, O₃ ve He tek tür atomdan oluştuğu için elementtir."},
      {q:"Aşağıdakilerden hangisi simyanın özelliklerinden biri değildir?", s:{A:"Deneme-yanılmaya dayanması",B:"Değersiz metalleri altına çevirmeye çalışması",C:"Bilimsel yöntem kullanması",D:"Sistematik bilgi birikiminin olmaması",E:"Bazı laboratuvar araçları geliştirmesi"}, d:"C", c:"Simya **bilimsel yöntem kullanmaz**; bilimsel yöntem kimyanın özelliğidir."},
      {q:"Karbonun sembolü C, kobaltın sembolü Co'dur. Buna göre CO ifadesi neyi gösterir?", s:{A:"Kobalt elementini",B:"Karbon monoksit bileşiğini",C:"Karbon elementini",D:"Oksijen elementini",E:"Kobalt oksit bileşiğini"}, d:"B", c:"İki büyük harf iki ayrı element demek: **C** (karbon) ve **O** (oksijen) → karbon monoksit."}] },
  "bio|Canlıların Ortak Özellikleri": { vid:"1_LWUCjbYx0", kanal:"Senin Biyolojin", baslik:"Canlıların Ortak Özellikleri 1 · TYT Biyoloji Kampı",
    ozet:["Bütün canlılar **hücreden** oluşur; hücre canlının en küçük yapı ve görev birimidir.","**Metabolizma** = yapım (**anabolizma**) + yıkım (**katabolizma**).","Canlılar solunum yapar, **ATP** üretir, uyarılara tepki verir, ürer, büyür ve gelişir.","Canlılar **homeostazi** ile iç dengelerini korur, çevrelerine **adaptasyon** gösterir."],
    formul:[{ad:"Metabolizma", ifade:"anabolizma + katabolizma"},{ad:"Ortak enerji molekülü", ifade:"ATP"}],
    kart:[["Canlının en küçük yapı ve görev birimi?","Hücre"],["Anabolizma ne demek?","Yapım: küçük moleküllerden büyük molekül"],["Katabolizma ne demek?","Yıkım: büyük moleküllerin parçalanması"],["Homeostazi nedir?","İç ortamın dengede tutulması"],["Tüm canlıların ortak enerji molekülü?","ATP"]],
    test:[{q:"Aşağıdakilerden hangisi tüm canlılar için ortak bir özellik değildir?", s:{A:"Hücreden oluşma",B:"ATP üretme",C:"Fotosentez yapma",D:"Uyarılara tepki verme",E:"Metabolizma faaliyeti gösterme"}, d:"C", c:"**Fotosentezi** sadece bitkiler, algler ve bazı bakteriler yapar. Diğerleri bütün canlılarda ortaktır."},
      {q:"Proteinlerin amino asitlere parçalanması aşağıdakilerden hangisine örnektir?", s:{A:"Katabolizma",B:"Anabolizma",C:"Homeostazi",D:"Adaptasyon",E:"Üreme"}, d:"A", c:"Büyük molekülün küçük parçalara ayrılması bir **yıkım** olayıdır, yani katabolizma."},
      {q:"Sıcak bir günde terleyerek vücut sıcaklığının sabit tutulması hangi özelliğe örnektir?", s:{A:"Büyüme",B:"Homeostazi",C:"Üreme",D:"Anabolizma",E:"Adaptasyon"}, d:"B", c:"İç ortamın (vücut sıcaklığının) dengede tutulması **homeostazidir**."}] },
  "tr|Sözcükte Anlam": { vid:"XVDocbEn6T8", kanal:"Sözel Hocam", baslik:"Sözcükte Anlam 1 · TYT Türkçe",
    ozet:["**Gerçek anlam:** sözcüğün akla gelen ilk anlamı (\"elini kesti\").","**Mecaz anlam:** gerçek anlamından uzaklaşmış anlam (\"sert bakış\", \"sıcak davranış\").","**Terim anlam:** bir bilim, sanat ya da meslek dalına özgü anlam (\"açı\", \"kesir\").","**Eş anlamlı** (siyah–kara), **zıt anlamlı** (uzun–kısa), **sesteş** (yüz: sayı / yüz: surat)."],
    formul:[{ad:"Somut", ifade:"Beş duyudan biriyle algılanır: taş, ses"},{ad:"Soyut", ifade:"Duyularla algılanamaz: sevgi, umut"}],
    kart:[["\"Sert konuştu\" sözünde \"sert\" hangi anlamda?","Mecaz anlam"],["\"Kara\" ile \"siyah\" arasındaki ilişki?","Eş anlamlı"],["\"Sevgi\" somut mu soyut mu?","Soyut"],["\"Yüz\" (sayı) ve \"yüz\" (surat) ilişkisi?","Sesteş (eş sesli)"],["Terim anlam nedir?","Bir bilim ya da meslek dalına özgü anlam"]],
    test:[{q:"Aşağıdaki cümlelerin hangisinde \"sıcak\" sözcüğü mecaz anlamda kullanılmıştır?", s:{A:"Sıcak çorbayı yavaşça içti.",B:"Bize çok sıcak davrandılar.",C:"Odadaki sıcak hava bunalttı.",D:"Sıcak sudan elini hemen çekti.",E:"Fırından sıcak ekmek aldık."}, d:"B", c:"\"Sıcak davranmak\" **içten, samimi** davranmak demektir; sıcaklıkla ilgisi yoktur. Diğerlerinde gerçek anlam var."},
      {q:"Aşağıdaki sözcüklerden hangisi soyut anlamlıdır?", s:{A:"Özlem",B:"Rüzgâr",C:"Koku",D:"Duman",E:"Gölge"}, d:"A", c:"**Özlem** duyularla algılanamaz. Rüzgâr hissedilir, koku koklanır, duman ve gölge görülür."},
      {q:"Aşağıdaki sözcük çiftlerinden hangisi zıt anlamlıdır?", s:{A:"Cevap – yanıt",B:"Yaşlı – ihtiyar",C:"Cesur – korkak",D:"Okul – mektep",E:"Kırmızı – al"}, d:"C", c:"**Cesur – korkak** zıt anlamlıdır. Diğer çiftler eş anlamlıdır."}] },
  "tar|Tarih ve Zaman": { vid:"n8TRsD_kWl4", kanal:"Tarihane", baslik:"Tarih ve Zaman · Tarih Bilimine Giriş · TYT Tarih",
    ozet:["Tarih; geçmişteki olayları **yer ve zaman** belirterek, **neden-sonuç** ilişkisi içinde, belgelere dayanarak inceler.","Tarihte **deney ve gözlem yapılamaz**; olaylar bir daha aynı koşullarla yaşanmaz.","**Kaynaklar:** yazılı (kitabe, ferman, kronik) ve yazısız (çanak çömlek, silah, fosil).","**Takvimler:** Hicri (Ay yılı, 622 Hicret), Miladi (Güneş yılı), Celali (Melikşah dönemi, Güneş yılı)."],
    formul:[{ad:"Yüzyıl bulma", ifade:"1453 → 14,53 → 15. yüzyıl"},{ad:"Yıl uzunluğu", ifade:"Güneş yılı ≈ 365 gün · Ay yılı ≈ 354 gün"}],
    kart:[["1453 hangi yüzyıldadır?","15. yüzyıl"],["Hicri takvimin başlangıcı?","622, Hicret"],["Celali takvimi hangi hükümdar döneminde hazırlandı?","Melikşah (Büyük Selçuklu)"],["Tarihte neden deney yapılamaz?","Olaylar bir daha aynı koşullarla yaşanmaz"],["Kitabe yazılı mı yazısız kaynak mı?","Yazılı kaynak"]],
    test:[{q:"1071 yılı hangi yüzyılın hangi çeyreğindedir?", s:{A:"10. yüzyılın son çeyreği",B:"11. yüzyılın ilk çeyreği",C:"11. yüzyılın üçüncü çeyreği",D:"11. yüzyılın son çeyreği",E:"12. yüzyılın ilk çeyreği"}, d:"C", c:"1071 → **11. yüzyıl** (1001–1100). Çeyrekler: 1001–1025, 1026–1050, **1051–1075**, 1076–1100 → üçüncü çeyrek."},
      {q:"Aşağıdakilerden hangisi yazısız bir tarih kaynağıdır?", s:{A:"Çanak çömlek",B:"Kitabe",C:"Ferman",D:"Kronik",E:"Antlaşma metni"}, d:"A", c:"**Çanak çömlek** üzerinde yazı yoktur; diğerlerinin hepsi yazılı belgedir."},
      {q:"Ay yılını esas alan takvim aşağıdakilerden hangisidir?", s:{A:"Celali",B:"Miladi",C:"Rumi",D:"On İki Hayvanlı Türk Takvimi",E:"Hicri"}, d:"E", c:"**Hicri** takvim Ay yılına göredir (yaklaşık 354 gün). Diğerleri Güneş yılını esas alır."}] }
});
["mat|Temel Kavramlar","mat|Rasyonel Sayılar","mat|Basit Eşitsizlikler","mat|Mutlak Değer"].forEach(k=>{ DERS_ICERIK[k].kanal = "Mert Hoca"; });
/* Video bölümleri: videoların YouTube açıklamasındaki zaman damgalarından */
const BOLUM = {};
/* Bir konunun ders ekranı içeriği: özet/test/kart varsa DERS_ICERIK'ten, videolar her zaman VIDEO'dan */
function icerik(k){ const v = VIDEO[k], c = DERS_ICERIK[k]; if(!v && !c) return null;
  const P = v ? v.p.map(x=>[x[0], x[1], x[2]==="s"?"soru":"konu", x[3]]) : (c.parca || [[c.vid, c.baslik, "konu"]]);
  return {...(c||{ozet:[], formul:[], kart:[], test:[]}), vid:P[0][0], parca:P.length>1?P:null, kanal: v ? v.h : c.kanal, baslik: v ? v.l : c.baslik, tamIcerik: !!c}; } /* bölümler videoların açıklamasındaki zaman damgalarından eklenecek */
const OG_SIRALAR = [["mat","Matematik · İlk 12 Konu","Matematik"],["prob","Matematik · Problemler","Matematik"],["matd","Matematik · Diğer Konular","Matematik"],["geo","Geometri","Geometri"],["tr","Türkçe","Türkçe"],["fiz","Fizik","Fizik"],["kim","Kimya","Kimya"],["bio","Biyoloji","Biyoloji"],["tar","Tarih","Tarih"],["cog","Coğrafya","Coğrafya"],["fel","Felsefe","Felsefe"]];
/* Demo: öğrenci biraz ilerlemiş görünsün (sadece demo modunda, bir kez) */
function demoOgrenTohum(){ let demo = false; try{ demo = localStorage.getItem("zk-demo")==="1"; }catch(e){} if(!demo || !S.me) return;
  if(!og().tohum2){ ogYaz(o=>{ o.tohum2 = 1; }); setTimeout(()=>{ mutate(x=>{ x.hocalar = {...(x.hocalar||{}), "Matematik":"Mert Hoca", "Geometri":"Mert Hoca", "Fizik":"Özcan Aykın", "Kimya":"Görkem Şahin", "Biyoloji":"Betül Biyoloji", "Türkçe":"Rüştü Hoca", "Tarih":"Tarihin Kodları", "Coğrafya":"Coğrafyanın Kodları"}; }); render(); }, 0); }
  if(!og().tohum3){ ogYaz(o=>{ o.tohum3 = 1; o.testSonuc = {...(o.testSonuc||{}), "mat|Temel Kavramlar":{d:3,n:3,at:Date.now()-2*864e5}, "mat|Rasyonel Sayılar":{d:2,n:3,at:Date.now()-864e5}}; o.izlenen = {...(o.izlenen||{}), "fiz|Fizik Bilimine Giriş":[0,1]}; if(o.kartlar && o.kartlar["mat|Temel Kavramlar"]) Object.values(o.kartlar["mat|Temel Kavramlar"]).forEach(x=>{ x.kutu = Math.max(x.kutu, 2); }); }); }
  if(og().tohum) return;
  const t0 = today(), now = Date.now();
  ogYaz(o=>{ o.tohum = 1;
    o.ilerleme = {"mat|Basit Eşitsizlikler":{t:1394, d:3480, at:now-3600e3}, "mat|Temel Kavramlar":{t:4100, d:4100, at:now-2*864e5}, "fiz|Fizik Bilimine Giriş":{t:2950, d:2950, at:now-3*864e5}};
    o.izleme = {[t0]:1500};
    o.kartlar = {"mat|Temel Kavramlar":{0:{kutu:1,sonraki:t0},1:{kutu:0,sonraki:t0},2:{kutu:2,sonraki:gunSonra(5)},3:{kutu:1,sonraki:t0},4:{kutu:3,sonraki:gunSonra(20)}},
      "mat|Rasyonel Sayılar":{0:{kutu:2,sonraki:gunSonra(4)},1:{kutu:0,sonraki:t0},2:{kutu:1,sonraki:t0},3:{kutu:2,sonraki:gunSonra(6)},4:{kutu:1,sonraki:gunSonra(1)}},
      "fiz|Fizik Bilimine Giriş":{0:{kutu:1,sonraki:t0},1:{kutu:0,sonraki:t0},2:{kutu:2,sonraki:gunSonra(3)},3:{kutu:1,sonraki:t0},4:{kutu:2,sonraki:gunSonra(7)}}};
    o.hata = [{k:"mat|Rasyonel Sayılar", i:1, at:now-864e5, sonraki:t0}, {k:"tar|Tarih ve Zaman", i:0, at:now-864e5, sonraki:t0}, {k:"mat|Temel Kavramlar", i:1, at:now-2*864e5, sonraki:gunSonra(3)}];
    o.testSonuc = {"mat|Temel Kavramlar":{d:3,n:3,at:now-2*864e5}, "mat|Rasyonel Sayılar":{d:2,n:3,at:now-864e5}};
    o.izlenen = {"fiz|Fizik Bilimine Giriş":[0,1]};
    o.notlar = {"mat|Temel Kavramlar":[{t:312, m:"0 çift sayı ama pozitif değil!", at:now-2*864e5},{t:1260, m:"Ardışık sayılarda toplam = ortanca × adet", at:now-2*864e5}],
      "fiz|Fizik Bilimine Giriş":[{t:540, m:"Ağırlık vektörel, kütle skaler", at:now-3*864e5}]};
  });
  setTimeout(()=>{ mutate(x=>{ ["mat|Temel Kavramlar","mat|Rasyonel Sayılar","fiz|Fizik Bilimine Giriş","tar|Tarih ve Zaman"].forEach(k=>{ topic(x,k).v = true; }); topic(x,"fiz|Basınç").y = 12; }); render(); }, 0); }
const kalin = x => esc(x).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>");
const dkSn = t => { t = Math.max(0, Math.floor(t||0)); const h = Math.floor(t/3600), m = Math.floor(t%3600/60), sn = t%60; return (h? h+":"+String(m).padStart(2,"0") : m) + ":" + String(sn).padStart(2,"0"); };
const OGK = () => "zk-ogren-" + (S.me||"x");
function og(){ try{ return JSON.parse(localStorage.getItem(OGK())||"{}"); }catch(e){ return {}; } }
function ogYaz(fn){ const o = og(); fn(o); try{ localStorage.setItem(OGK(), JSON.stringify(o)); }catch(e){} return o; }
const gunSonra = n => { const d = new Date(today()+"T12:00:00"); d.setDate(d.getDate()+n); return d.toISOString().slice(0,10); };
const KUTU = [1,3,7,30];
const konuAdi = k => k.split("|").slice(1).join("|");
const thumb = id => `https://i.ytimg.com/vi/${id}/mqdefault.jpg`;
/* Bu haftanın koç hedeflerinden konu anahtarları */
function haftaKonulari(s){ const h = ((s.plan||{})[curStart(s)]||{}).hedef||{}, out = [];
  Object.entries(h).forEach(([d, x])=> splitKonu(x.konu).forEach(n=>{ const sub = dersSubs(s, d).find(sb=>sb.t.includes(n)); if(sub) out.push({k:tkey(sub.k,n), d, n}); })); return out; }
function vidKart(k, s, genis){ const c = icerik(k), t = (s.topics||{})[k]||{}, p = (og().ilerleme||{})[k], pct = p&&p.d ? Math.min(100, p.t/p.d*100) : 0;
  return `<button type="button" class="vk ${c?"":"yok"} ${genis?"genis":""}" ${c?`data-ders="${esc(k)}"`:"disabled"}>
    <span class="vkr">${c?`<img src="${thumb(c.vid)}" alt="" loading="lazy">`:`<i>🎬</i>`}${t.v?`<em class="vkok">✓ İzlendi</em>`:""}${c?`<span class="vkp">▶</span>`:""}${pct?`<span class="vkbar"><i style="width:${pct}%"></i></span>`:""}</span>
    <span class="vkm"><span class="vkt">${esc(konuAdi(k))}</span><span class="vks">${c?(p&&p.t>20&&pct<97?`${dkSn(p.t)}'de kaldın`:esc(c.kanal)+(((og().sure||{})[k]||(p&&p.d))?` · ${Math.round(((og().sure||{})[k]||p.d)/60)} dk`:"")+(c.parca?` · ${c.parca.length} video`:"")+(BOLUM[k]?` · ${BOLUM[k].length} bölüm`:"")):"Video yakında"}</span></span></button>`; }
function tekrarListesi(s){ const o = og(), L = [], bugun = today();
  Object.entries(DERS_ICERIK).forEach(([k,c])=>{ const ks = (o.kartlar||{})[k]||{}, t = (s.topics||{})[k]||{};
    const due = c.kart.filter((_,i)=>{ const x = ks[i]; return x ? x.sonraki<=bugun : t.v; }).length; if(due) L.push({tip:"kart", k, n:due}); });
  (o.hata||[]).filter(h=>h.sonraki<=bugun && !h.tamam).forEach(h=>L.push({tip:"hata", k:h.k, i:h.i, bid:h.bid}));
  cetele10(s).slice(0,3).forEach(c=>L.push({tip:"cetele", ad:c.n||c.ad||"", y:c.y}));
  return L; }
/* ---------- Konu durumu: video + test + kart → ⚪ başlanmadı · 🟡 devam · 🟢 tamam ---------- */
function konuDurum(k, s){ const c = icerik(k); if(!c) return null; const o = og(), t = (s.topics||{})[k]||{}, P = c.parca || [[c.vid]];
  const iz = t.v ? P.length : Math.min(P.length, ((o.izlenen||{})[k]||[]).length + ((((o.ilerleme||{})[k]||{}).t||0) > 60 ? 0 : 0));
  const kys = (o.kartlar||{})[k]||{}, kOgr = Object.values(kys).filter(x=>x.kutu>=2).length, kTop = c.kart.length;
  const ts = (o.testSonuc||{})[k], tTop = c.test.length;
  const vPct = P.length ? iz/P.length : 0, tPct = tTop ? (ts ? ts.d/ts.n : 0) : null, kPct = null; /* kartlar ilerlemeye sayılmaz (koçun kararı) */
  const parcalar = [vPct, tPct, kPct].filter(x=>x!=null), ort = parcalar.reduce((a,b)=>a+b,0)/parcalar.length;
  const durum = ort>=0.8 && vPct===1 ? "tamam" : ort>0 || (((o.ilerleme||{})[k]||{}).t||0)>30 ? "devam" : "yok";
  return {iz, vTop:P.length, vPct, ts, tTop, kOgr, kTop, pct:Math.round(ort*100), durum, c}; }
const DURUM_AD = {yok:"Başlanmadı", devam:"Devam ediyor", tamam:"Tamam"};
/* Sıradaki tek adım: önce yarım video, sonra testi çözülmemiş izlenmiş konu, sonra kart, sonra yeni konu */
function siradakiAdim(s){ const hk = haftaKonulari(s).map(x=>x.k).filter(k=>icerik(k)); for(const k of hk){ const d = konuDurum(k,s); if(d.durum==="tamam") continue;
    if(d.vPct<1) return {k, sekme:"ozet", ikon:"▶️", baslik:`${konuAdi(k)}: videoyu ${d.iz?"bitir":"izle"}`, alt:`${d.c.kanal} · ${d.vTop>1?`${d.iz}/${d.vTop} video`:"konu anlatımı"}`};
    if(d.tTop && !d.ts) return {k, sekme:"test", ikon:"🧩", baslik:`${konuAdi(k)}: testi çöz`, alt:`${d.tTop} soru · konuyu anladın mı görelim`};
    if(d.kTop && d.kOgr<d.kTop) return {k, sekme:"kart", ikon:"🃏", baslik:`${konuAdi(k)}: kartları tekrar et`, alt:`${d.kOgr}/${d.kTop} kart öğrenildi`}; }
  return null; }
function durumCip(d){ return `<span class="kdc ${d.durum}">${d.durum==="tamam"?"🟢":d.durum==="devam"?"🟡":"⚪"} ${DURUM_AD[d.durum]}</span>`; }
const dersAdi = sk => ({mat:"Matematik", prob:"Problemler", matd:"Matematik", geo:"Geometri", tr:"Türkçe", fiz:"Fizik", kim:"Kimya", bio:"Biyoloji", tar:"Tarih", cog:"Coğrafya", fel:"Felsefe"})[sk]||sk;
function devamSatiri(s){ const o = og(), devam = Object.entries(o.ilerleme||{}).filter(([k,p])=>icerik(k) && p.t>20 && (!p.d || p.t < p.d-30)).sort((a,b)=>b[1].at-a[1].at)[0]; if(!devam) return "";
  const [k,p] = devam, c = icerik(k), pct = p.d ? Math.min(100, p.t/p.d*100) : 0;
  return `<button class="card dvs" data-ders="${esc(k)}"><span class="vkr"><img src="${thumb(c.vid)}" alt="" loading="lazy"><span class="vkp">▶</span>${pct?`<span class="vkbar"><i style="width:${pct}%"></i></span>`:""}</span><span class="dvm"><small>Kaldığın yerden devam et</small><b>${esc(konuAdi(k))}</b><span class="faint small">${esc(c.kanal)} · ${dkSn(p.t)}'te kaldın</span></span></button>`; }
function tekrarKarti(s, kisa){ const tk = tekrarListesi(s); if(!tk.length) return kisa ? "" : `<div class="card ogt"><div class="sech"><h3>🔁 Bugün tekrar et</h3></div><p class="muted small" style="margin:6px 0 0">Bugün tekrar edecek bir şey yok 🎉</p></div>`;
  const kart = tk.filter(x=>x.tip==="kart"), hata = tk.filter(x=>x.tip==="hata"), cet = tk.filter(x=>x.tip==="cetele"), kartSay = kart.reduce((a,x)=>a+x.n,0);
  return `<div class="card ogt"><div class="sech"><h3>🔁 Bugün tekrar et</h3><span class="faint small">${tk.length} iş</span></div><div class="tklist">
    ${kartSay?`<button class="row" data-ders="${esc(kart[0].k)}" data-sekme="kart"><span class="ri">🃏</span><div><div class="rt">${kartSay} kart tekrar zamanında</div><div class="rs">${kart.map(x=>esc(konuAdi(x.k))).join(", ")}</div></div><span class="rx">${icon("chev","sm")}</span></button>`:""}
    ${hata.length?`<button class="row" ${hata[0].bid?`data-bk="tek" data-id="${hata[0].bid}"`:`data-ders="${esc(hata[0].k)}" data-sekme="test"`}><span class="ri">❗</span><div><div class="rt">${hata.length} yanlışını tekrar çöz</div><div class="rs">${hata.map(x=>esc(konuAdi(x.k))).join(", ")}</div></div><span class="rx">${icon("chev","sm")}</span></button>`:""}
    ${cet.map(x=>`<button class="row" data-act="go" data-v="cetele"><span class="ri">📌</span><div><div class="rt">${esc(x.ad)} konusunu tekrar et</div><div class="rs">Çetelede ${x.y} yanlış</div></div><span class="rx">${icon("chev","sm")}</span></button>`).join("")}</div></div>`; }
function araclar(s){ const o = og(), notSay = Object.values(o.notlar||{}).reduce((a,x)=>a+x.length,0), hataSay = (o.hata||[]).filter(h=>!h.tamam).length + soruList(S.me).filter(([,q])=>q.durum!=="cozuldu").length;
  return `<div class="ogar"><div class="sech" style="margin:6px 4px 10px"><h3>Araçlarım</h3></div><div class="ogarac">
      <button data-act="go" data-v="konular"><span>${icon("book")}</span><b>Konu Takibi</b><small>%${Math.round(examPct(s,"TYT")*100)} TYT</small></button>
      <button data-act="go" data-v="cetele"><span>${icon("list")}</span><b>Yanlış Çetelesi</b><small>Konu konu yanlışların</small></button>
      <button data-act="go" data-v="sorular"><span>${icon("defter")}</span><b>Hata Defteri</b><small>${hataSay?hataSay+" soru bekliyor":"Çözemediğin sorular"}</small></button>
      <button data-ogr="notlar"><span>${icon("note")}</span><b>Notlarım</b><small>${notSay?notSay+" not":"Videodan not al"}</small></button></div></div>`; }
const ogDort = () => `<div class="og4">
    <button data-act="go" data-v="socoz" class="og4a"><span>📷</span><b>Soru Çöz</b></button>
    <button data-act="go" data-v="videolar" class="og4b"><span>▶️</span><b>Ders Videoları</b></button>
    <button data-act="go" data-v="banka" class="og4c"><span>🧩</span><b>Soru Bankası</b></button>
    <button data-ogr="kartlar" class="og4d"><span>🃏</span><b>Kartlar</b></button></div>`;
/* ---- Öğrenme Merkezi (koçun kararı): bugünün görevleri + koçun bu haftaki konuları; tekrar önerisi yok, sadece yanlışları çöz ---- */
const GOREV_DERS = [[/paragraf/,"Türkçe","tr|Paragraf"],[/problem/,"Matematik"],[/geometri/,"Geometri"],[/matematik/,"Matematik"],[/fizik/,"Fizik"],[/kimya/,"Kimya"],[/biyoloji/,"Biyoloji"],[/türkçe|dil bilgisi|edebiyat/,"Türkçe"],[/tarih/,"Tarih"],[/coğrafya/,"Coğrafya"],[/felsefe/,"Felsefe"]];
function gorevDers(t){ const n = trLow(t); if(/deneme|analiz/.test(n) && !/branş/.test(n)) return null; const m = GOREV_DERS.find(([r])=>r.test(n)); return m ? {ders:m[1], sabit:m[2]||null, prob:/problem/.test(n)} : null; }
function dersKonulari(s, ders){ const h = (((s.plan||{})[curStart(s)]||{}).hedef||{})[ders]; if(!h || !h.konu) return [];
  return splitKonu(h.konu).map(n=>{ const sub = dersSubs(s, ders).find(sb=>sb.t.includes(n)); return sub ? tkey(sub.k, n) : null; }).filter(Boolean); }
function konuIslem(k, kisa){ const c = icerik(k), banka = BANKA.some(x=>x.k===k);
  return `<span class="kis">${c?`<button class="kdin" data-ders="${esc(k)}">${icon("play","xs")}${kisa?"Dinle":"Konu dinle"}</button>`:`<span class="yok">${icon("play","xs")}Video yok</span>`}${banka?`<button class="kcoz" data-bk="konu" data-k="${esc(k)}">${icon("kitapcik","xs")}${kisa?"Çöz":"Soru çöz"}</button>`:`<button class="kcoz" data-act="go" data-v="socoz">${icon("kamera","xs")}${kisa?"Çöz":"Soru çöz"}</button>`}</span>`; }
function konuSatiri(k, s){ const d = konuDurum(k, s);
  return `<div class="ks ${d?d.durum:"yok"}"><div class="ksb"><span class="ksad">${esc(konuAdi(k))}</span><span class="faint small">${esc(dersAdi(k.split("|")[0]))}${d?" · "+esc(d.c.kanal):""}${d&&d.durum!=="yok"?` · ${d.durum==="tamam"?"🟢 Tamam":"🟡 Devam ediyor"}`:""}</span></div>${konuIslem(k)}</div>`; }
const DERS_KIS = {mat:"Mat", prob:"Prb", matd:"Mat", geo:"Geo", tr:"Tür", fiz:"Fiz", kim:"Kim", bio:"Bio", tar:"Tar", cog:"Coğ", fel:"Fel"};
const dersRozet = on => `<span class="drz g-${grpOf(on)}">${DERS_KIS[on]||"Ders"}</span>`;
const DERS_ON = {Matematik:"mat", Geometri:"geo", Türkçe:"tr", Fizik:"fiz", Kimya:"kim", Biyoloji:"bio", Tarih:"tar", Coğrafya:"cog", Felsefe:"fel"};
const grpOf = on => DERS_GRUP[on] || "sos";
const kucukKapak = k => { const c = icerik(k); return c ? `<span class="kk2" style="background-image:url(${thumb(c.vid)})"></span>` : `<span class="kk2 bos">${icon("video","sm")}</span>`; };
function bugunGorevler(s){ const L = dayTasks(s, today()).map(g=>({g, d:gorevDers(g.t)})).filter(x=>x.d);
  if(!L.length) return `<div class="card"><div class="sech"><h3>${icon("check","sm")} Bugün ne yapayım?</h3></div><p class="muted small" style="margin:6px 0 0">Bugünkü programında ders görevi yok. Haftalık konularından dilediğine çalışabilirsin.</p></div>`;
  return `<div class="card"><div class="sech"><h3>${icon("check","sm")} Bugün ne yapayım?</h3><span class="faint small">bugünkü programından</span></div><div class="bglist">${L.map(({g,d})=>{ const ks = d.sabit ? [d.sabit] : dersKonulari(s, d.ders).filter(k=>!d.prob || k.startsWith("prob|") || true);
      const on = d.sabit ? "tr" : (d.prob ? "prob" : DERS_ON[d.ders]||"mat");
      return `<div class="bgg g-${grpOf(on)} ${g.done?"bitti":""}"><div class="bggh">${dersRozet(on)}<div class="bggm"><b>${esc(g.t)}</b><span class="bggd">${g.done?"✓ Tamamlandı":esc(d.ders)}</span></div></div>
        ${ks.length ? ks.map(k=>`<div class="bggk">${kucukKapak(k)}<span class="bggkn">${esc(konuAdi(k))}</span>${konuIslem(k, true)}</div>`).join("") : `<div class="bggk"><span class="faint small">Bu ders için haftalık konu yazılmamış.</span><span class="kis"><button class="kdin" data-act="go" data-v="videolar">${icon("video","xs")}Videolar</button><button class="kcoz" data-act="go" data-v="socoz">${icon("kamera","xs")}Soru çöz</button></span></div>`}</div>`; }).join("")}</div></div>`; }
function yanlislarKarti(s){ const o = og(), H = (o.hata||[]).filter(h=>!h.tamam), bek = soruList(S.me).filter(([,q])=>q.durum!=="cozuldu").length; if(!H.length && !bek) return "";
  const bugun = H.filter(h=>h.sonraki<=today());
  return `<div class="card"><div class="sech"><h3>${icon("alert","sm")} Yanlışlarını çöz</h3><span class="faint small">${H.length+bek} soru</span></div><div class="tklist">
    ${H.slice(0,3).map(h=>{ const x = h.bid ? BANKA.find(b=>b.id===h.bid) : (icerik(h.k)||{test:[]}).test[h.i]; return x ? `<button class="row" ${h.bid?`data-bk="tek" data-id="${h.bid}"`:`data-ders="${esc(h.k)}" data-sekme="test"`}><span class="ri kotu">${icon("alert","sm")}</span><div style="min-width:0"><div class="rt">${esc(konuAdi(h.k))}</div><div class="rs">${esc(x.q.replace(/\n/g," ").slice(0,70))}…</div></div><span class="rx">${icon("chev","sm")}</span></button>` : ""; }).join("")}
    ${bek?`<button class="row" data-act="go" data-v="sorular"><span class="ri">${icon("defter","sm")}</span><div><div class="rt">Hata Defteri'nde ${bek} soru bekliyor</div><div class="rs">Soru Çözüm'le adım adım çöz</div></div><span class="rx">${icon("chev","sm")}</span></button>`:""}</div>${bugun.length?`<p class="faint small" style="margin:8px 0 0">${bugun.length} tanesinin tekrar günü bugün.</p>`:""}</div>`; }
function ogHero(s){ const L = dayTasks(s, today()).filter(g=>gorevDers(g.t)), bitti = L.filter(g=>g.done).length, pct = L.length ? bitti/L.length : 0, o = og();
  const dk = Math.round(((o.izleme||{})[today()]||0)/60), yan = (o.hata||[]).filter(h=>!h.tamam).length, R = 26, C = 2*Math.PI*R;
  return `<div class="oghero"><div class="ohm"><small>${["Pazar","Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi"][new Date().getDay()]} · bugün</small><b>${L.length ? (bitti===L.length ? "Bugünkü dersler tamam 🎉" : `${L.length - bitti} ders görevin var`) : "Bugün serbest çalışma"}</b>
      <span class="ohc"><span>${icon("play","xs")}${dk} dk izledin</span>${yan?`<span>${icon("alert","xs")}${yan} yanlış bekliyor</span>`:""}</span></div>
    <svg class="ohr" viewBox="0 0 64 64" aria-label="Bugünkü ders görevleri ${bitti}/${L.length}"><circle cx="32" cy="32" r="${R}" fill="none" stroke="rgba(255,255,255,.25)" stroke-width="7"/><circle cx="32" cy="32" r="${R}" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-dasharray="${C}" stroke-dashoffset="${C*(1-pct)}" transform="rotate(-90 32 32)"/><text x="32" y="37" text-anchor="middle" fill="#fff" font-size="15" font-weight="800">${bitti}/${L.length}</text></svg></div>`; }
function ogDortKutu(s){ const o = og(), hataSay = (o.hata||[]).filter(h=>!h.tamam).length + soruList(S.me).filter(([,q])=>q.durum!=="cozuldu").length;
  const vSay = Object.keys(VIDEO).length, bkKonu = new Set(BANKA.map(x=>x.k)).size, hak = SZ.kalan!=null ? `${SZ.kalan} soru hakkın var` : "Fotoğrafını çek, adım adım öğren";
  const k = (cls, v, ic, ad, alt) => `<button data-act="go" data-v="${v}" class="${cls}"><span>${icon(ic)}</span><div><b>${ad}</b><small>${alt}</small></div>${icon("chev","sm")}</button>`;
  return `<div class="og4">${k("og4a","socoz","kamera","Soru Çöz",hak)}${k("og4b","videolar","video","Ders Videoları",`${vSay} konu · 9 ders`)}${k("og4c","banka","kitapcik","Soru Bankası",`${BANKA.length} soru · ${bkKonu} konu`)}${k("og4d","sorular","defter","Hata Defteri",hataSay?`${hataSay} soru bekliyor`:"Çözemediğin sorular")}</div>`; }
function pOgren(s){ demoOgrenTohum(); const hk = haftaKonulari(s).map(x=>x.k);
  return `${topbar(`<h1 class="ttl">Öğrenme Merkezi</h1>`)}
  <div class="page ogpage ogv3">
    ${ogHero(s)}
    ${ogDortKutu(s)}
    ${bugunGorevler(s)}
    ${devamSatiri(s)}
    ${yanlislarKarti(s)}
    ${hk.length?`<div class="sech" style="margin:4px 4px -4px"><h3>${icon("target","sm")} Bu haftaki konuların</h3><span class="faint small">koçunun programından</span></div><div class="hkrow">${hk.map(k=>{ const on = k.split("|")[0], c = icerik(k), d = konuDurum(k,s);
      return `<div class="hk g-${grpOf(on)}"><button class="hkk" ${c?`data-ders="${esc(k)}"`:"disabled"} style="${c?`background-image:url(${thumb(c.vid)})`:""}"><span class="hkd">${esc(dersAdi(on))}</span>${d&&d.durum!=="yok"?`<span class="hks ${d.durum}">${d.durum==="tamam"?"Tamam":"Devam ediyor"}</span>`:""}${c?`<span class="vkp">▶</span>`:""}</button>
        <div class="hkm"><b>${esc(konuAdi(k))}</b><span class="faint small">${c?esc(c.kanal):"Video yakında"}</span></div>${konuIslem(k)}</div>`; }).join("")}</div>`:""}
    ${araclar(s)}
  </div>`; }
/* ---- Ders Videoları sayfası ---- */
function pVideolar(s){ const sec = S.vders || "mat", grup = sec==="mat" ? ["mat","prob","matd"] : [sec];
  const L = CURX().TYT.filter(x=>grup.includes(x.k)).flatMap(sub=>[...sub.t, ...(sub.k==="tr"?["Paragraf"]:[])].map(n=>tkey(sub.k,n))).filter(k=>VIDEO[k]);
  const h = L.length ? VIDEO[L[0]].h : "", o = og();
  return `${topbar(`<h1 class="ttl">Ders Videoları</h1>`, "", `<button class="iconbtn" data-act="go" data-v="ogren" aria-label="Geri">${icon("back")}</button>`)}
  <div class="page ogpage">
    <div class="vdc">${[["mat","Matematik"],["geo","Geometri"],["tr","Türkçe"],["fiz","Fizik"],["kim","Kimya"],["bio","Biyoloji"],["tar","Tarih"],["cog","Coğrafya"],["fel","Felsefe"]].map(([k,ad])=>`<button data-vd="${k}" aria-pressed="${sec===k}">${ad}</button>`).join("")}</div>
    ${devamSatiri(s)}
    <div class="card"><div class="sech"><h3>${esc(({mat:"Matematik",geo:"Geometri",tr:"Türkçe",fiz:"Fizik",kim:"Kimya",bio:"Biyoloji",tar:"Tarih",cog:"Coğrafya",fel:"Felsefe"})[sec])}</h3><span class="faint small">Hocan: ${esc((hoca(s, dersAdi(sec))||h).split("+")[0].trim())} · ${L.length} konu</span></div>
      <div class="vlist">${L.map((k,i)=>{ const v = VIDEO[k], d = konuDurum(k,s), p = (o.ilerleme||{})[k], pct = d.vPct===1 ? 100 : p&&p.d ? Math.min(100,p.t/p.d*100) : 0;
        return `<button class="vls" data-ders="${esc(k)}"><span class="vkr"><img src="${thumb(v.p[0][0])}" alt="" loading="lazy">${pct?`<span class="vkbar"><i style="width:${pct}%"></i></span>`:""}</span><span class="vlm"><b>${i+1}. ${esc(konuAdi(k))}</b><span class="faint small">${v.p.length>1?v.p.length+" video":"1 video"}${v.p.some(x=>x[2]==="s")?" · soru çözümü var":""}</span>${durumCip(d)}</span></button>`; }).join("")}</div></div>
  </div>`; }
document.addEventListener("click", e=>{ const b = e.target.closest && e.target.closest("[data-vd]"); if(!b) return; S.vders = b.dataset.vd; render(); });

/* Kartlarım / Notlarım listeleri (alttan pencere) */
document.addEventListener("click", e=>{ const b = e.target.closest && e.target.closest("[data-ogr]"); if(!b) return; const v = b.dataset.ogr, o = og();
  if(v==="videolar"){ const el = $("#og-videolar"); if(el) el.scrollIntoView({behavior:"smooth", block:"start"}); return; }
  if(v==="kartlar") return sheet(`<h3>Kartlarım</h3><p class="muted small" style="margin:0">Her konu bir deste. Bildiğin kart 1, 3, 7, 30 gün sonra tekrar gelir.</p>
    ${Object.entries(DERS_ICERIK).map(([k,c])=>{ const ks = (o.kartlar||{})[k]||{}, ogr = Object.values(ks).filter(x=>x.kutu>=3).length;
      return `<button type="button" class="row" data-ders="${esc(k)}" data-sekme="kart"><span class="ri">🃏</span><div><div class="rt">${esc(konuAdi(k))}</div><div class="rs">${c.kart.length} kart · ${ogr} tanesini öğrendin</div></div><span class="rx">${icon("chev","sm")}</span></button>`; }).join("")}
    <div class="acts"><button type="button" class="btn" data-close>Kapat</button></div>`);
  if(v==="notlar"){ const L = Object.entries(o.notlar||{}).flatMap(([k,a])=>a.map(n=>({...n,k}))).sort((a,b)=>b.at-a.at);
    return sheet(`<h3>Notlarım</h3><p class="muted small" style="margin:0">Videolardan aldığın notlar. Nota dokun, video o saniyeden açılsın.</p>
      ${L.length?L.map(n=>`<button type="button" class="row" data-ders="${esc(n.k)}" data-sn="${n.t}"><span class="ri ognt">${dkSn(n.t)}</span><div><div class="rt">${esc(n.m)}</div><div class="rs">${esc(konuAdi(n.k))}</div></div></button>`).join(""):`<div class="empty">Henüz not yok. Video izlerken "Not al"a bas.</div>`}
      <div class="acts"><button type="button" class="btn" data-close>Kapat</button></div>`); }
});
/* ---------- Soru Bankası (PROTOTİP): konu seç, kitapçık gibi çöz, kontrol et ---------- */
const BANKA = [
  {id:"tk1", k:"mat|Temel Kavramlar", z:"orta", q:"a ve b birer pozitif tam sayıdır.\na · b = 24\nolduğuna göre a + b toplamının alabileceği en küçük değer kaçtır?", s:{A:"9",B:"10",C:"11",D:"14",E:"25"}, d:"B",
    ad:[["Çarpanları listele","Çarpımı 24 olan pozitif tam sayı çiftlerini yaz.","1·24, 2·12, 3·8, 4·6"],["Toplamları bul","Her çiftin toplamını hesapla.","25, 14, 11, **10**"],["En küçüğü seç","Sayılar birbirine ne kadar yakınsa toplam o kadar küçük olur.","4 + 6 = 10"]], puf:"Çarpımı sabit iki sayının toplamı, sayılar birbirine en yakın olduğunda en küçüktür."},
  {id:"tk2", k:"mat|Temel Kavramlar", z:"kolay", q:"Ardışık beş tek sayının toplamı 105'tir.\nBuna göre bu sayıların en büyüğü kaçtır?", s:{A:"19",B:"21",C:"23",D:"25",E:"27"}, d:"D",
    ad:[["Ortadaki sayıyı bul","Ardışık sayılarda toplam = ortadaki × adet.","105 ÷ 5 = **21**"],["Sayıları yaz","Tek sayılar 2'şer artar.","17, 19, 21, 23, 25"],["En büyüğü seç","Ortadakinden iki adım ileri git.","21 + 4 = **25**"]], puf:"21'i işaretleme: o ortadaki sayı, soru en büyüğü soruyor."},
  {id:"tk3", k:"mat|Temel Kavramlar", z:"orta", q:"x, y ve z birbirinden farklı rakamlardır.\nBuna göre 2x + y − z ifadesinin alabileceği en büyük değer kaçtır?", s:{A:"22",B:"23",C:"24",D:"26",E:"27"}, d:"D",
    ad:[["Katsayısı büyük olana en büyük rakam","x iki kez sayılıyor, ona 9 ver.","x = **9**"],["Sıradaki büyük rakam y'ye","Farklı olmaları gerektiği için y = 8.","y = **8**"],["Çıkarılan en küçük olsun","z = 0 seçilirse hiçbir şey kaybedilmez.","2·9 + 8 − 0 = **26**"]], puf:"27 bulduysan y'ye de 9 vermişsin; rakamlar farklı olmalı."},
  {id:"tk4", k:"mat|Temel Kavramlar", z:"orta", q:"a ve b tam sayılardır.\na + b toplamı tek sayı olduğuna göre aşağıdakilerden hangisi kesinlikle çift sayıdır?", s:{A:"a · b",B:"a + 2b",C:"2a + b",D:"a² + b",E:"a"}, d:"A",
    ad:[["Toplam tekse","İki sayının toplamı tekse biri tek, diğeri çifttir.","tek + çift = tek"],["Çarpıma bak","Çarpanlardan biri çift olduğu için çarpım her zaman çifttir.","a · b = **çift**"],["Diğerlerini ele","a + 2b ve a, a'ya; 2a + b, b'ye bağlıdır. a² + b ise a + b gibi tektir.","Kesin olan: a · b"]], puf:"\"Kesinlikle\" sorularında her iki durumu da dene: a tek–b çift ve a çift–b tek."},
  {id:"md1", k:"mat|Mutlak Değer", z:"orta", q:"x < 0 < y olmak üzere\n|x − y| + |x| − |y|\nifadesinin eşiti aşağıdakilerden hangisidir?", s:{A:"0",B:"2x",C:"−2x",D:"2y",E:"−2y"}, d:"C",
    ad:[["İçlerin işaretini bul","x negatif, y pozitif; x − y negatiftir.","x − y < 0"],["Mutlak değerleri aç","Negatif olanın işaretini değiştirerek çıkar.","|x − y| = y − x, |x| = −x, |y| = y"],["Topla","Benzer terimleri sadeleştir.","(y − x) + (−x) − y = **−2x**"]], puf:"Bir örnekle kontrol et: x = −1, y = 2 → 3 + 1 − 2 = 2 = −2x ✓"},
  {id:"md2", k:"mat|Mutlak Değer", z:"kolay", q:"|2x − 4| = 6\ndenklemini sağlayan x değerlerinin çarpımı kaçtır?", s:{A:"−10",B:"−5",C:"−1",D:"5",E:"10"}, d:"B",
    ad:[["İki durum yaz","İçerisi 6 ya da −6 olabilir.","2x − 4 = 6 veya 2x − 4 = −6"],["Çöz","Her denklemi ayrı çöz.","x = **5** veya x = **−1**"],["Çarp","İki kökü çarp.","5 · (−1) = **−5**"]], puf:"Mutlak değerli denklemde negatif durumu unutma; tek kök bulan 5 işaretler."},
  {id:"md3", k:"mat|Mutlak Değer", z:"orta", q:"|x + 2| ≤ 5\neşitsizliğini sağlayan kaç farklı x tam sayısı vardır?", s:{A:"7",B:"8",C:"9",D:"10",E:"11"}, d:"E",
    ad:[["Aralığa çevir","|A| ≤ 5 ise −5 ≤ A ≤ 5.","−5 ≤ x + 2 ≤ 5"],["2 çıkar","Üç tarafa birden uygula.","−7 ≤ x ≤ 3"],["Say","Uçlar dahil: son − ilk + 1.","3 − (−7) + 1 = **11**"]], puf:"≤ işareti uçları dahil eder; 9 bulduysan uçları saymamışsın."},
  {id:"be1", k:"mat|Basit Eşitsizlikler", z:"zor", q:"−3 < x < 2 ve 1 < y < 4\nolduğuna göre x · y çarpımının alabileceği kaç farklı tam sayı değeri vardır?", s:{A:"15",B:"17",C:"19",D:"20",E:"21"}, d:"C",
    ad:[["En küçük çarpım","Negatif en büyük x ile en büyük y'yi düşün.","x → −3, y → 4 ⇒ xy → **−12**"],["En büyük çarpım","Pozitif en büyük x ile en büyük y.","x → 2, y → 4 ⇒ xy → **8**"],["Aralığı say","Uçlar dahil değil: −12 < xy < 8.","−11'den 7'ye: **19** tane"]], puf:"Çarpımda uç değerleri tek tek çarpıp en küçük ve en büyüğü seç; sadece uçları çarpmak yetmez, işaretlere dikkat."},
  {id:"be2", k:"mat|Basit Eşitsizlikler", z:"orta", q:"a < b < 0\nolduğuna göre aşağıdakilerden hangisi kesinlikle doğrudur?", s:{A:"a² < b²",B:"a · b < 0",C:"1/a < 1/b",D:"a − b > 0",E:"b² < a²"}, d:"E",
    ad:[["Örnek seç","Koşula uyan sayılar al.","a = −3, b = −1"],["Şıkları dene","a² = 9, b² = 1; ab = 3; 1/a = −1/3, 1/b = −1; a − b = −2.","Sadece b² < a² sağlanıyor"],["Genelle","Negatiflerde mutlak değeri büyük olanın karesi büyüktür.","|a| > |b| ⇒ **a² > b²**"]], puf:"Negatif sayılarda sıralama terslenir: −3 < −1 ama (−3)² > (−1)²."},
  {id:"be3", k:"mat|Basit Eşitsizlikler", z:"kolay", q:"2 ≤ x ≤ 6\nolduğuna göre 3 − 2x ifadesinin alabileceği en küçük değer kaçtır?", s:{A:"−9",B:"−5",C:"−1",D:"1",E:"3"}, d:"A",
    ad:[["−2 ile çarp","Negatifle çarpınca yön değişir.","−12 ≤ −2x ≤ −4"],["3 ekle","Üç tarafa da ekle.","−9 ≤ 3 − 2x ≤ −1"],["En küçüğü oku","Sol uç en küçük değerdir.","**−9**"]], puf:"−1 en büyük değerdir; soru en küçüğü soruyor."}
];
/* Neden yanlış? Havuzdaki her çeldirici belirli bir hatadan türetildiği için seçilen şık hatanın türünü ve sebebini söyler. */
const NT = {bilgi:["📘","Bilgi eksiği"], islem:["🧮","İşlem hatası"], dikkat:["👀","Dikkatsizlik"], sure:["⏱️","Süre yetmedi"]};
const NEDEN = {
  tk1:{A:["bilgi","a + b ≥ 2√24 ≈ 9,8 sonucunu aşağı yuvarladın; ama a ve b tam sayı olmalı, 9 elde edilemez."],C:["dikkat","3 · 8'de durdun; birbirine daha yakın 4 · 6 çifti daha küçük toplam verir."],D:["dikkat","2 · 12'yi aldın; çarpan çiftlerini sonuna kadar listelemedin."],E:["dikkat","1 · 24 en büyük toplamı verir; soru en küçüğü soruyor."]},
  tk2:{A:["islem","Ortadaki 21'den geriye gittin; en büyük sayı ileride."],B:["dikkat","21 ortadaki sayı; soru en büyüğü soruyor."],C:["islem","Ortadakinden bir adım ileri gittin; beş sayıda en büyük, ortadakinden iki adım (+4) ileridedir."],E:["islem","Üç adım ileri gittin; ortadakinden sonra sadece iki sayı var."]},
  tk3:{A:["bilgi","Çıkarılan z için 0'ı seçmedin; 0 da bir rakamdır ve çıkarılan en küçük olmalı."],B:["bilgi","Çıkarılan z için 0'ı seçmedin; 0 da bir rakamdır ve çıkarılan en küçük olmalı."],C:["dikkat","9 + 8 + 7 gibi topladın; x'in katsayısı 2, z ise çıkarılıyor."],E:["dikkat","y'ye de 9 verdin; rakamların birbirinden farklı olması gerekiyordu."]},
  tk4:{B:["bilgi","a + 2b'nin tek mi çift mi olduğu a'ya bağlı; a'nın durumu bilinmiyor."],C:["bilgi","2a + b'nin tek mi çift mi olduğu b'ye bağlı; b'nin durumu bilinmiyor."],D:["bilgi","a² ile a aynı teklikte olduğu için a² + b de a + b gibi tektir."],E:["dikkat","a tek de olabilir çift de; \"kesinlikle\" sorularında iki durumu da dene."]},
  md1:{A:["islem","|x − y|'yi x − y diye açtın; içi negatif olduğu için y − x olur."],B:["bilgi","|x|'i x olarak açtın; x negatif olduğu için |x| = −x."],D:["islem","Mutlak değerleri açarken y'li terimlerin işaretini yanlış taşıdın; y'ler birbirini götürür."],E:["islem","Mutlak değerleri açarken işaretleri yanlış taşıdın; y'ler birbirini götürür, sonuç sadece x'e bağlı."]},
  md2:{A:["islem","İkinci denklemi yanlış çözdün: 2x − 4 = −6 ⇒ x = −1."],C:["dikkat","Sadece negatif durumu çözdün; çarpım için iki kök de gerekli."],D:["bilgi","Sadece pozitif durumu çözdün; |A| = 6 ise A = −6 da olabilir."],E:["islem","Kökleri doğru bulup çarpımda işareti kaybettin: 5 · (−1) = −5."]},
  md3:{A:["bilgi","Aralığı yanlış kurdun; |x + 2| ≤ 5 ⇒ −5 ≤ x + 2 ≤ 5 ⇒ −7 ≤ x ≤ 3."],B:["bilgi","Aralığı yanlış kurdun; |x + 2| ≤ 5 ⇒ −7 ≤ x ≤ 3."],C:["dikkat","Uçları dahil etmedin; ≤ işareti −7 ve 3'ü de kapsar."],D:["islem","Bir ucu saymadın; uçlar dahilse adet = son − ilk + 1."]},
  be1:{A:["islem","En küçük çarpımı yanlış buldun; x → −3 ve y → 4 için çarpım −12'ye yaklaşır."],B:["islem","Uç değerleri eksik çarptın; en küçük −12'ye, en büyük 8'e yaklaşır."],D:["dikkat","Uçlardan birini dahil ettin; −12 ve 8 elde edilemez çünkü eşitsizlikler kesin."],E:["dikkat","İki ucu da dahil ettin; −12 ve 8 elde edilemez."]},
  be2:{A:["bilgi","Negatif sayılarda küçük olanın karesi büyüktür: −3 < −1 ama 9 > 1."],B:["bilgi","İki negatif sayının çarpımı pozitiftir."],C:["bilgi","Aynı işaretli sayılar ters çevrilince sıralama değişir: 1/a > 1/b."],D:["islem","a < b ise a − b negatiftir."]},
  be3:{B:["bilgi","Ara bir değer denedin; en küçük değer aralığın ucunda (x = 6) çıkar."],C:["dikkat","−1 en büyük değer; soru en küçüğü soruyor."],D:["islem","−2 ile çarparken eşitsizliğin yönünü değiştirmedin."],E:["dikkat","x = 0 için hesapladın; x en az 2 olabilir."]}
};
const nedenTur = (id, c) => ((NEDEN[id]||{})[c]||[])[0] || "";
const bkKonular = () => [...new Set(BANKA.map(x=>x.k))];
function bkBasla(ids, ad){ S.bk = {ids, ad, cev:{}, bitti:false, bas:Date.now(), acik:{}}; S.view = "banka"; render(); window.scrollTo(0,0); }
const zEt = z => ({kolay:"Kolay", orta:"Orta", zor:"Zor"})[z]||"";
function pBanka(s){
  const o = og(), B = S.bk, geri = `<button class="iconbtn" data-bk="${B?"liste":"geri"}" aria-label="Geri">${icon("back")}</button>`;
  if(!B){ const ks = bkKonular();
    return `${topbar(`<h1 class="ttl">Soru Bankası</h1>`, "", geri)}
    <div class="page ogpage">
      <div class="seg szmodsec"><button data-act="go" data-v="socoz" aria-pressed="false">Fotoğrafla çöz</button><button aria-pressed="true">Soru Bankası</button></div>
      <div class="card note"><span class="av">${icon("kitapcik")}</span><div><b>Konu seç, çözmeye başla</b><div class="muted small">Sorular ÖSYM tarzında, cevap anahtarı kontrol edilmiş özgün sorular. Bitirince her sorunun adım adım çözümünü görürsün; yanlışların Hata Defteri'ne düşer.</div></div></div>
      <button class="btn pri full" data-bk="karisik">🎲 Karışık test · ${BANKA.length} soru</button>
      <div class="bkkonular">${ks.map(k=>{ const L = BANKA.filter(x=>x.k===k), r = (o.banka||{})[k];
        return `<button class="bkk" data-bk="konu" data-k="${esc(k)}"><span class="bkkd">Matematik</span><b>${esc(konuAdi(k))}</b><span class="faint small">${L.length} soru · ${[...new Set(L.map(x=>zEt(x.z)))].join(", ")}</span>
          ${r?`<span class="bksonuc">Son: ${r.d}/${r.n} doğru</span>`:`<span class="bkbasla">Başla ›</span>`}</button>`; }).join("")}
        ${["Rasyonel Sayılar","Üslü Sayılar","Fizik Bilimine Giriş","Sözcükte Anlam"].map(n=>`<div class="bkk yok"><span class="bkkd">${/Fizik/.test(n)?"Fizik":/Sözcük/.test(n)?"Türkçe":"Matematik"}</span><b>${esc(n)}</b><span class="faint small">Yakında</span></div>`).join("")}</div>
      <p class="faint small" style="margin:0 4px">Prototip: 10 örnek soru. Gerçek sürümde soru havuzundaki binlerce soru konu konu burada olacak.</p>
    </div>`; }
  const L = B.ids.map(id=>BANKA.find(x=>x.id===id)), isa = Object.keys(B.cev).length;
  let ozet = "";
  if(B.bitti){ const d = L.filter(x=>B.cev[x.id]===x.d).length, y = L.filter(x=>B.cev[x.id] && B.cev[x.id]!==x.d).length, bos = L.length-d-y, net = d - y/4;
    ozet = `<div class="card bkozet"><div><b class="num">${d}</b><small>Doğru</small></div><div><b class="num" style="color:var(--bad)">${y}</b><small>Yanlış</small></div><div><b class="num" style="color:var(--muted)">${bos}</b><small>Boş</small></div><div><b class="num" style="color:var(--ac)">${String(net).replace(".",",")}</b><small>Net</small></div><div><b class="num">${dkSn(B.sure/1000)}</b><small>Süre</small></div></div>${(()=>{ const T = {}; L.filter(x=>B.cev[x.id] && B.cev[x.id]!==x.d).forEach(x=>{ const t = nedenTur(x.id, B.cev[x.id]); if(t) T[t] = (T[t]||0)+1; }); const e = Object.entries(T).sort((a,b)=>b[1]-a[1]);
      return e.length ? `<div class="card bknd"><b>Yanlışlarının sebebi</b><div class="bkndl">${e.map(([t,n])=>`<span class="bkndc t-${t}">${NT[t][0]} ${NT[t][1]} <b>${n}</b></span>`).join("")}</div><p class="muted small" style="margin:0">${e[0][0]==="dikkat"?"Bilgin var; soruyu sonuna kadar okumak ve şıkları kontrol etmek sana net kazandırır.":e[0][0]==="islem"?"Konuyu biliyorsun; işlemleri adım adım yazmak ve sonucu kontrol etmek hatayı azaltır.":e[0][0]==="bilgi"?"Bazı kurallar eksik; o konunun videosuna ve kartlarına dönmek iyi olur.":"Süre baskısını azaltmak için önce bildiğin soruları çöz, zor soruyu sona bırak."}</p></div>` : ""; })()}`; }
  return `${topbar(`<h1 class="ttl">${esc(B.ad)}</h1>`, "", geri)}
  <div class="page ogpage bkpage">
    ${ozet || `<div class="bkust"><span>${L.length} soru · <b id="bk-isa">${isa}</b> işaretlendi</span><span class="faint small">4 yanlış 1 doğruyu götürür</span></div>`}
    <div class="bkgrid">${L.map((x,i)=>{ const c = B.cev[x.id], dg = B.bitti && c===x.d, yn = B.bitti && c && c!==x.d;
      return `<div class="bkq ${B.bitti?(dg?"dg":yn?"yn":"bs"):""}" data-q="${x.id}">
        <div class="bkqh"><b>${i+1}.</b><span class="faint small">${esc(konuAdi(x.k))} · ${zEt(x.z)}</span>${B.bitti?`<span class="bkdurum">${dg?"✓ Doğru":yn?"✗ Yanlış · doğrusu "+x.d:"Boş · doğrusu "+x.d}</span>`:""}</div>
        <div class="bkmetin">${esc(x.q).replace(/\n/g,"<br>")}</div>
        <div class="bksik">${Object.entries(x.s).map(([h,v])=>`<button type="button" data-bk="sec" data-id="${x.id}" data-h="${h}" class="${c===h?"sec":""} ${B.bitti&&h===x.d?"dogru":""} ${B.bitti&&c===h&&h!==x.d?"yanlis":""}" ${B.bitti?"disabled":""}><b>${h})</b> ${esc(v)}</button>`).join("")}</div>
        ${B.bitti && yn ? (()=>{ const n = (NEDEN[x.id]||{})[c], t = nedenTur(x.id, c); return `<div class="bkneden"><div><b>🔍 Neden yanlış?</b> ${n?`${c} şıkkını seçtin: ${kalin(n[1])}`:"Çözümü inceleyip hangi adımda ayrıldığına bak."}</div>
          ${t&&NT[t]?`<div class="bkntur"><span class="bkndc t-${t}">${NT[t][0]} ${NT[t][1]}</span></div>`:""}</div>`; })() : ""}
        ${B.bitti?`<button type="button" class="link" data-bk="coz" data-id="${x.id}">${B.acik[x.id]?"Çözümü gizle":"Adım adım çözümü gör"}</button>
          ${B.acik[x.id]?`<div class="bkcoz">${x.ad.map((a,j)=>`<div class="bkad"><span class="bkadn">${j+1}</span><div><b>${esc(a[0])}</b><div class="small">${kalin(a[1])}</div><code>${kalin(a[2])}</code></div></div>`).join("")}<div class="bkpuf">💡 ${kalin(x.puf)}</div></div>`:""}`:""}
      </div>`; }).join("")}</div>
    <div class="bkalt">${B.bitti?`<button class="btn" data-bk="liste">Konulara dön</button><button class="btn pri" data-bk="tekrar">Yeniden çöz</button>`:`<button class="btn pri" data-bk="bitir">Bitir ve kontrol et</button>`}</div>
  </div>`; }
document.addEventListener("click", e=>{ const b = e.target.closest && e.target.closest("[data-bk]"); if(!b) return; const a = b.dataset.bk, B = S.bk;
  if(a==="geri"){ S.view = "ogren"; render(); return; }
  if(a==="liste"){ S.bk = null; render(); window.scrollTo(0,0); return; }
  if(a==="karisik") return bkBasla(BANKA.map(x=>x.id), "Karışık test");
  if(a==="konu") return bkBasla(BANKA.filter(x=>x.k===b.dataset.k).map(x=>x.id), konuAdi(b.dataset.k));
  if(a==="tek") return bkBasla([b.dataset.id], "Hata Defteri tekrarı");
  if(!B) return;
  if(a==="sec"){ const id = b.dataset.id; if(B.cev[id]===b.dataset.h) delete B.cev[id]; else B.cev[id] = b.dataset.h;
    b.parentElement.querySelectorAll("button").forEach(x=>x.classList.toggle("sec", B.cev[id]===x.dataset.h)); const n = $("#bk-isa"); if(n) n.textContent = Object.keys(B.cev).length; sesCal("tik"); return; }
  if(a==="bitir"){ B.bitti = true; B.sure = Date.now()-B.bas; const L = B.ids.map(id=>BANKA.find(x=>x.id===id)), d = L.filter(x=>B.cev[x.id]===x.d).length;
    ogYaz(o=>{ o.banka = o.banka||{}; bkKonular().forEach(k=>{ const M = L.filter(x=>x.k===k); if(M.length && B.ad!=="Hata Defteri tekrarı") o.banka[k] = {d:M.filter(x=>B.cev[x.id]===x.d).length, n:M.length, at:Date.now()}; });
      o.hata = o.hata||[]; L.forEach(x=>{ const c = B.cev[x.id]; o.hata = o.hata.filter(h=>h.bid!==x.id); if(c && c!==x.d) o.hata.push({k:x.k, bid:x.id, at:Date.now(), sonraki:gunSonra(1), tur:((NEDEN[x.id]||{})[c]||[])[0]||""}); }); });
    if(d===L.length) sesCal("basari"); render(); window.scrollTo(0,0); return; }
  if(a==="coz"){ B.acik[b.dataset.id] = !B.acik[b.dataset.id]; render(); return; }
  if(a==="neden"){ ogYaz(o=>{ o.nedenler = o.nedenler||{}; o.nedenler[b.dataset.id] = b.dataset.v; (o.hata||[]).forEach(h=>{ if(h.bid===b.dataset.id) h.tur = b.dataset.v; }); }); render(); return; }
  if(a==="tekrar"){ bkBasla(B.ids, B.ad); return; }
});
/* ---------- Ders ekranı: render()'dan bağımsız, video yeniden yüklenmesin diye ayrı katman ---------- */
const DP = { k:null, p:null, sekme:"ozet", cev:{}, kart:0, ters:false, tak:false, yanit:null, tim:null, oyn:false, sn:0 };
function ytHazir(){ return new Promise((res, rej)=>{ if(window.YT && YT.Player) return res(); const eski = window.onYouTubeIframeAPIReady; window.onYouTubeIframeAPIReady = ()=>{ eski && eski(); res(); };
  if(!document.getElementById("ytapi")){ const sc = document.createElement("script"); sc.id = "ytapi"; sc.src = "https://www.youtube.com/iframe_api"; sc.onerror = rej; document.head.appendChild(sc); } setTimeout(()=>rej(new Error("zaman")), 8000); }); }
const dpZaman = () => { try{ return DP.p && DP.p.getCurrentTime ? DP.p.getCurrentTime() : DP.sn; }catch(e){ return DP.sn; } };
function dpKaydet(){ if(!DP.k || !DP.p || !DP.p.getCurrentTime) return; const t = dpZaman(), d = DP.p.getDuration ? DP.p.getDuration() : 0; if(!t) return;
  ogYaz(o=>{ o.ilerleme = o.ilerleme||{}; o.ilerleme[DP.k] = {t, d, at:Date.now()}; }); }
function dersAc(k, sekme, sn, pi){ const c = icerik(k); if(!c) return; closeSheet(); dersKapat(true); const P = c.parca || [[c.vid, c.baslik, "konu"]]; pi = Math.min(+pi||0, P.length-1); const vid = P[pi][0];
  Object.assign(DP, {k, pi, sekme: sekme||"ozet", cev:{}, kart:0, ters:false, tak:false, yanit:null, oyn:false, sn: sn!=null ? +sn : ((og().ilerleme||{})[k]||{}).t||0});
  const el = document.createElement("div"); el.id = "dersk"; el.className = "dersk";
  el.innerHTML = `<div class="dkust"><button class="iconbtn" data-dk="kapat" aria-label="Geri">${icon("back")}</button><div style="min-width:0;flex:1"><b class="dkad">${esc(konuAdi(k))}</b><div class="dkdurum" id="dkdurum"></div><div class="faint small dkalt">${esc(c.kanal)} · ${esc(P.length>1 ? (pi+1)+". video: "+P[pi][1] : c.baslik)}</div></div></div>
    <div class="dkana"><div class="dksol"><div class="oyn" id="oyn"><div class="kavid dkvid"><div id="ytp"></div></div>
    <div class="oyb" id="oyb" hidden>
      <div class="oyc" id="oyc" role="slider" aria-label="Videoda ilerle" aria-valuemin="0" aria-valuemax="100" tabindex="0"><div class="oyct"><i class="oycy" id="oycy"></i><i class="oycd" id="oycd"></i>${(BOLUM[k]||[]).slice(1).map(([t])=>`<b class="oybl" data-t="${t}"></b>`).join("")}${((og().notlar||{})[k]||[]).map(n=>`<em class="oynt" data-t="${n.t}" title="${esc(n.m)}"></em>`).join("")}</div><span class="oytop" id="oytop"></span></div>
      <div class="oyr">
        <button class="oyd buyuk" data-oy="oynat" aria-label="Oynat" id="oyoynat">▶</button>
        <button class="oyd" data-oy="geri" aria-label="10 saniye geri">⟲<small>10</small></button>
        <button class="oyd" data-oy="ileri" aria-label="10 saniye ileri">⟳<small>10</small></button>
        <span class="oyz" id="oyz">0:00 / 0:00</span>
        <span class="oyara"></span>
        <button class="oyd yazi" data-oy="cc" aria-label="Alt yazı" aria-pressed="${!!og().cc}" id="oycc">CC</button>
        <button class="oyd yazi" data-oy="hiz" aria-label="Oynatma hızı" id="oyhiz">${String(og().hiz||1).replace(".",",")}x</button>
        <button class="oyd" data-dk="not" aria-label="Not al">📝</button>
        <button class="oyd" data-dk="anla" aria-label="Burayı anlamadım">🤔</button>
        <button class="oyd" data-oy="tam" aria-label="Tam ekran">⛶</button>
      </div>
    </div></div>
    <div class="dkarac" id="dkarac-yedek" hidden><button class="btn sm" data-dk="not">📝 Not al</button><button class="btn sm" data-dk="anla">🤔 Burayı anlamadım</button></div>
    ${P.length>1?`<div class="dkbolum"><div class="dkbh">Bu konunun videoları · ${P.length}</div><div class="dkbl">${P.map((x,i)=>`<button data-dk="parca" data-pi="${i}" class="${i===pi?"on":""}"><span>${i+1}. ${x[2]==="soru"?"Soru çözümü":"Konu"}${x[3]?" · "+x[3]+" dk":""}</span>${esc(x[1])}</button>`).join("")}</div></div>`:""}
    ${BOLUM[k]?`<div class="dkbolum"><div class="dkbh">Bölümler</div><div class="dkbl">${BOLUM[k].map(([t,ad],i)=>`<button data-dk="git" data-sn="${t}" data-bi="${i}"><span>${dkSn(t)}</span>${esc(ad)}</button>`).join("")}</div></div>`:""}
    <div class="dksira"><div class="sech"><h3>Sıradaki dersler</h3><span class="faint small">önce aynı dersten</span></div><div class="vkrow">${(()=>{ const L = Object.keys(VIDEO), i = L.indexOf(k), on = k.split("|")[0]; return [...L.slice(i+1), ...L.slice(0, Math.max(0,i))].filter(x=>x.split("|")[0]===on).slice(0,8).map(x=>vidKart(x, st())).join(""); })()}</div></div></div>
    <div class="dksag"><div class="dksek" role="tablist">${[["ozet","Özet"],["test","Test"],["anla","Anlamadım"],["not","Notlarım"]].map(([v,l])=>`<button role="tab" data-dk="sek" data-v="${v}">${l}</button>`).join("")}</div>
    <div id="dkgovde" class="dkgovde"></div></div></div>`;
  document.body.appendChild(el); document.body.classList.add("dersacik"); dpCiz();
  const sade = () => { const yd = $("#dkarac-yedek"); if(yd) yd.hidden = false; const y = $("#ytp"); if(y) y.outerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${vid}?rel=0&playsinline=1&start=${Math.floor(DP.sn)}" allow="encrypted-media; picture-in-picture; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>`; };
  ytHazir().then(()=>{ if(DP.k!==k) return; DP.p = new YT.Player("ytp", { host:"https://www.youtube-nocookie.com", videoId:vid, playerVars:{ start:Math.floor(DP.sn), rel:0, playsinline:1, modestbranding:1, controls:0, fs:0, iv_load_policy:3, disablekb:1, cc_load_policy:0, cc_lang_pref:"tr" },
    events:{ onReady: ev=>{ const b = $("#oyb"); if(b) b.hidden = false; oyBasla(); oyAltYazi(!!og().cc); try{ ev.target.setPlaybackRate(og().hiz||1); const d = ev.target.getDuration(); if(d) ogYaz(o=>{ o.sure = o.sure||{}; o.sure[k] = d; }); }catch(_){} }, onStateChange: ev=>{ DP.oyn = ev.data===1; oyCiz(); if(ev.data===1 && !og().cc) oyAltYazi(false); if(ev.data===2 || ev.data===0) dpKaydet(); if(ev.data===0){ ogYaz(o=>{ o.izlenen = o.izlenen||{}; const L = o.izlenen[k] = o.izlenen[k]||[]; if(!L.includes(pi)) L.push(pi); }); if(pi < P.length-1){ toast("Sıradaki video açılıyor"); setTimeout(()=>dersAc(k, DP.sekme, 0, pi+1), 1200); } else izlendiYap(); } } } }); }).catch(sade);
  clearInterval(DP.tim); DP.tim = setInterval(()=>{ if(!DP.oyn) return; ogYaz(o=>{ o.izleme = o.izleme||{}; o.izleme[today()] = (o.izleme[today()]||0) + 3; }); dpKaydet(); const z = $(".dkzaman"); if(z) z.textContent = dkSn(dpZaman()); bolumIsaretle(); }, 3000);
  geriKoruma(); }
/* ---------- Zekacademy oynatıcısı: YouTube kontrolleri kapalı, kumanda bizim ---------- */
function oyCiz(){ const p = DP.p; if(!p || !p.getDuration) return; let t = 0, d = 0, y = 0; try{ t = p.getCurrentTime()||0; d = p.getDuration()||0; y = p.getVideoLoadedFraction()||0; }catch(_){ return; } if(d) t = Math.min(t, d);
  const f = $("#oycd"), yb = $("#oycy"), z = $("#oyz"), o = $("#oyoynat"), c = $("#oyc"); if(!f) return;
  f.style.width = (d ? t/d*100 : 0) + "%"; yb.style.width = (y*100) + "%"; z.innerHTML = `${dkSn(t)}<span class="oyzt"> / ${dkSn(d)}</span>`; if(c) c.setAttribute("aria-valuenow", Math.round(d ? t/d*100 : 0));
  o.textContent = DP.oyn ? "❚❚" : "▶"; o.setAttribute("aria-label", DP.oyn ? "Durdur" : "Oynat");
  if(d) document.querySelectorAll("#oyc [data-t]").forEach(e=>{ e.style.left = (Math.min(1, +e.dataset.t/d)*100) + "%"; }); }
function oyBasla(){ clearInterval(DP.oyt); DP.oyt = setInterval(()=>{ if(!$("#oyb")) return clearInterval(DP.oyt); oyCiz(); }, 250); oyCiz();
  const c = $("#oyc"); if(!c) return; let sur = false;
  const git = e => { const r = c.getBoundingClientRect(), x = Math.max(0, Math.min(1, (e.clientX - r.left)/r.width)); try{ const d = DP.p.getDuration(); DP.p.seekTo(x*d, true); const tp = $("#oytop"); if(tp){ tp.textContent = dkSn(x*d); tp.style.left = (x*100)+"%"; } }catch(_){} oyCiz(); };
  c.addEventListener("pointerdown", e=>{ sur = true; c.setPointerCapture(e.pointerId); c.classList.add("sur"); git(e); });
  c.addEventListener("pointermove", e=>{ if(sur) git(e); });
  const bit = e=>{ if(!sur) return; sur = false; c.classList.remove("sur"); dpKaydet(); bolumIsaretle(); };
  c.addEventListener("pointerup", bit); c.addEventListener("pointercancel", bit);
  c.addEventListener("keydown", e=>{ if(e.key==="ArrowRight"||e.key==="ArrowLeft"){ e.preventDefault(); oyAtla(e.key==="ArrowRight"?5:-5); } }); }
/* Alt yazı: varsayılan kapalı; CC ile açılır (Türkçe varsa Türkçe), tercih hatırlanır */
function oyAltYazi(acik){ const p = DP.p; if(!p) return; try{ if(acik){ p.loadModule("captions"); p.setOption("captions", "track", {languageCode:"tr"}); } else { p.setOption("captions", "track", {}); p.unloadModule("captions"); p.unloadModule("cc"); } }catch(_){} const b = $("#oycc"); if(b) b.setAttribute("aria-pressed", acik); }
function oyAtla(sn){ try{ DP.p.seekTo(Math.max(0, DP.p.getCurrentTime()+sn), true); }catch(_){} oyCiz(); }
document.addEventListener("click", e=>{ const b = e.target.closest && e.target.closest("[data-oy]"); if(!b || !DP.p) return; const a = b.dataset.oy;
  if(a==="oynat"){ try{ DP.oyn ? DP.p.pauseVideo() : DP.p.playVideo(); }catch(_){} }
  else if(a==="cc"){ const acik = !og().cc; ogYaz(o=>{ o.cc = acik; }); oyAltYazi(acik); toast(acik ? "Alt yazı açık" : "Alt yazı kapalı"); }
  else if(a==="geri") oyAtla(-10); else if(a==="ileri") oyAtla(10);
  else if(a==="hiz"){ const L = [1,1.25,1.5,2], r = L[(L.indexOf(og().hiz||1)+1)%L.length]; ogYaz(o=>{ o.hiz = r; }); try{ DP.p.setPlaybackRate(r); }catch(_){} b.textContent = String(r).replace(".",",")+"x"; }
  else if(a==="tam"){ const w = $("#oyn"); try{ if(document.fullscreenElement) document.exitFullscreen(); else if(w.requestFullscreen) w.requestFullscreen().then(()=>{ try{ screen.orientation.lock("landscape"); }catch(_){} }).catch(()=>{}); else if(w.webkitRequestFullscreen) w.webkitRequestFullscreen(); }catch(_){} }
});
document.addEventListener("keydown", e=>{ if(!DP.p || !$("#dersk") || /input|textarea/i.test((e.target||{}).tagName||"")) return; if(e.key===" "||e.key==="k"){ e.preventDefault(); try{ DP.oyn ? DP.p.pauseVideo() : DP.p.playVideo(); }catch(_){} } else if(e.key==="j") oyAtla(-10); else if(e.key==="l") oyAtla(10); });
function bolumIsaretle(){ const B = BOLUM[DP.k]; if(!B) return; const t = dpZaman(); let i = 0; B.forEach(([s],j)=>{ if(t>=s) i = j; }); document.querySelectorAll(".dkbl button").forEach(b=>b.classList.toggle("on", +b.dataset.bi===i)); }
function dersKapat(sessiz){ const el = $("#dersk"); if(!el) return; dpKaydet(); clearInterval(DP.tim); clearInterval(DP.oyt); try{ DP.p && DP.p.destroy && DP.p.destroy(); }catch(e){} DP.p = null; DP.k = null; el.remove(); document.body.classList.remove("dersacik"); if(!sessiz) render(); }
function izlendiYap(){ const k = DP.k; if(!k) return; const t = (st().topics||{})[k]||{}; if(t.v) return; mutate(x=>{ topic(x,k).v = true; }); sesCal("basari"); toast("Konu izlendi olarak işaretlendi ✓"); }
function dpCiz(){ const g = $("#dkgovde"); if(!g || !DP.k) return; const dd = konuDurum(DP.k, st()), ds = $("#dkdurum"); if(ds && dd) ds.innerHTML = `${durumCip(dd)}<span>▶️ ${dd.iz}/${dd.vTop}</span>${dd.tTop?`<span>🧩 ${dd.ts?dd.ts.d+"/"+dd.ts.n:"—"}</span>`:""}`; const c = icerik(DP.k), o = og(), s = st(), t = (s.topics||{})[DP.k]||{};
  document.querySelectorAll("#dersk [data-dk=sek]").forEach(b=>b.setAttribute("aria-selected", b.dataset.v===DP.sekme));
  let h = "";
  if(DP.sekme==="ozet" && !c.ozet.length) h = `<div class="empty">Bu konunun özeti ve formül kartı yakında. Şimdilik videoyu izle, önemli yerlerde 📝 ile not al.</div>
    <button class="btn ${t.v?"":"pri"}" data-dk="izle" style="width:100%">${t.v?"✅ İzledin · geri al":"✓ İzledim"}</button>`;
  else if(DP.sekme==="test" && !c.test.length) h = `<div class="empty">Bu konunun testi soru havuzundan gelecek. O zamana kadar Soru Bankası'ndaki konulara bakabilirsin.</div>`;
  else if(DP.sekme==="kart" && !c.kart.length) h = `<div class="empty">Bu konunun kartları yakında.</div>`;
  else if(DP.sekme==="ozet") h = `<div class="dkozet">${c.ozet.map(x=>`<div class="kay">${kalin(x)}</div>`).join("")}</div>
    <div class="dkformul">${c.formul.map(f=>`<div><small>${esc(f.ad)}</small><b>${esc(f.ifade)}</b></div>`).join("")}</div>
    <button class="btn ${t.v?"":"pri"}" data-dk="izle" style="width:100%">${t.v?"✅ İzledin · geri al":"✓ İzledim"}</button>`;
  else if(DP.sekme==="not"){ const L = ((o.notlar||{})[DP.k]||[]).slice().sort((a,b)=>a.t-b.t);
    h = `<div class="dknotyaz"><input type="text" id="dk-not" placeholder="Notunu yaz (dakika kendiliğinden eklenir)"><button class="btn pri" data-dk="notkaydet">Kaydet</button></div>
      ${L.length?L.map((n,i)=>`<div class="dknot"><button class="dkt" data-dk="git" data-sn="${n.t}">${dkSn(n.t)}</button><span>${esc(n.m)}</span><button class="dksil" data-dk="notsil" data-at="${n.at}" aria-label="Sil">×</button></div>`).join("")
        :`<div class="empty">Videoda önemli bir yer gelince "Not al"a bas. Dakikaya dokununca video oraya atlar.</div>`}`; }
  else if(DP.sekme==="test"){ const T = c.test;
    h = `<div class="katest">${T.map((x,i)=>{ const v = DP.cev[i];
      return `<div class="kaq"><div class="kaqt"><b>${i+1}.</b> ${esc(x.q)}</div><div class="kasik">${Object.entries(x.s).map(([hh,vv])=>`<button type="button" data-dk="cev" data-i="${i}" data-h="${hh}" class="${v? (hh===x.d?"dogru":hh===v?"yanlis":"") : ""}" ${v?"disabled":""}><b>${hh}</b>${esc(vv)}</button>`).join("")}</div>
        ${v?`<div class="kacoz ${v===x.d?"ok":""}"><b>${v===x.d?"Doğru! 🎉":"Doğru cevap "+x.d+"."}</b> ${kalin(x.c)}${v!==x.d?`<div class="faint small" style="margin-top:6px">📕 Hata defterine eklendi, yarın tekrar karşına çıkacak.</div>`:""}</div>`:""}</div>`; }).join("")}
      ${Object.keys(DP.cev).length===T.length ? (()=>{ const d = T.filter((x,i)=>DP.cev[i]===x.d).length; return `<div class="kasonuc">${d}/${T.length} doğru · ${d===T.length?"Konuyu kapmışsın 💪":"Yanlışların çözümüne bak, gerekirse videonun ilgili yerini tekrar izle."}</div><button class="btn" data-dk="testtekrar" style="width:100%">Testi baştan çöz</button>`; })() : ""}</div>`; }
  else if(DP.sekme==="kart"){ const ks = (o.kartlar||{})[DP.k]||{}, bugun = today(), sira = c.kart.map((x,i)=>i).filter(i=>!ks[i] || ks[i].sonraki<=bugun);
    if(!sira.length) h = `<div class="empty">Bu destenin bugünkü tekrarı bitti 🎉<br><span class="faint small">Sıradaki tekrar: ${esc(Object.values(ks).map(x=>x.sonraki).sort()[0]||"")}</span></div>`;
    else { const i = sira[DP.kart % sira.length], kk = c.kart[i];
      h = `<div class="faint small" style="text-align:center">${sira.length} kart tekrar bekliyor · karta dokun, çevir</div>
        <button class="fkart ${DP.ters?"ters":""}" data-dk="cevir"><span class="fon">${esc(kk[0])}</span><span class="farka">${esc(kk[1])}</span></button>
        ${DP.ters?`<div class="fbtn"><button class="btn" data-dk="kbilme" data-i="${i}">🔁 Tekrar et</button><button class="btn pri" data-dk="kbil" data-i="${i}">✓ Bildim</button></div>`:""}`; } }
  else if(DP.sekme==="anla"){ const z = DP.anlaSn ?? dpZaman();
    h = `<div class="katak"><div class="faint small">Video <b>${dkSn(z)}</b>'da durduruldu · ${esc(konuAdi(DP.k))}</div>
      <label class="f">Neyi anlamadın? <textarea id="dk-ne" rows="3" placeholder="ör. negatife bölünce neden yön değişiyor?">${esc(DP.ne||"")}</textarea></label>
      <button class="btn pri" data-dk="sor" style="width:100%">Soru Çözüm'e sor · 1 hak</button>
      ${DP.yanit?`<div class="kayanit"><div class="faint small">ÖRNEK YANIT · gerçek sürümde Soru Çözüm senin yazdığına ve videonun bu dakikasına göre cevaplar</div>
        ${c.kart.slice(0,2).map(x=>`<div class="kay"><b>${esc(x[0])}</b><br>${esc(x[1])}</div>`).join("")}${c.ozet[1]?`<div class="kay">${kalin(c.ozet[1])}</div>`:`<div class="kay">Gerçek sürümde Soru Çözüm, videonun konusuna ve bu dakikasına göre adım adım anlatır.</div>`}
        <button class="btn sm" data-dk="git" data-sn="${Math.max(0,z-30)}">⏪ Videoyu 30 sn geriden tekrar izle</button></div>`:""}</div>`; }
  g.innerHTML = h; }
document.addEventListener("click", e=>{
  const dd = e.target.closest && e.target.closest("[data-ders]"); if(dd && !e.target.closest("[data-dk]")){ e.preventDefault(); dersAc(dd.dataset.ders, dd.dataset.sekme, dd.dataset.sn); return; }
  const b = e.target.closest && e.target.closest("[data-dk]"); if(!b || !DP.k) return; const a = b.dataset.dk, c = icerik(DP.k);
  if(a==="kapat") return dersKapat();
  if(a==="sek"){ DP.sekme = b.dataset.v; if(DP.sekme==="anla"){ try{ DP.p && DP.p.pauseVideo(); }catch(_){} DP.anlaSn = dpZaman(); } dpCiz(); return; }
  if(a==="not"){ try{ DP.p && DP.p.pauseVideo(); }catch(_){} DP.sekme = "not"; dpCiz(); const i = $("#dk-not"); if(i){ i.placeholder = `${dkSn(dpZaman())} · notunu yaz`; i.focus(); } return; }
  if(a==="anla"){ try{ DP.p && DP.p.pauseVideo(); }catch(_){} DP.anlaSn = dpZaman(); DP.sekme = "anla"; DP.yanit = null; dpCiz(); const n = $("#dk-ne"); if(n) n.focus(); return; }
  if(a==="notkaydet"){ const v = ($("#dk-not")||{}).value||""; if(!v.trim()) return toast("Notunu yaz"); const t = dpZaman(); ogYaz(o=>{ o.notlar = o.notlar||{}; (o.notlar[DP.k] = o.notlar[DP.k]||[]).push({t, m:v.trim(), at:Date.now()}); }); toast("Not kaydedildi · "+dkSn(t)); dpCiz(); return; }
  if(a==="notsil"){ ogYaz(o=>{ o.notlar[DP.k] = (o.notlar[DP.k]||[]).filter(n=>String(n.at)!==b.dataset.at); }); dpCiz(); return; }
  if(a==="parca"){ dpKaydet(); dersAc(DP.k, DP.sekme, 0, +b.dataset.pi); return; }
  if(a==="hiz"){ const r = +b.dataset.v; ogYaz(o=>{ o.hiz = r; }); try{ DP.p.setPlaybackRate(r); }catch(_){} document.querySelectorAll("[data-dk=hiz]").forEach(x=>x.setAttribute("aria-pressed", x===b)); toast(`Hız ${String(r).replace(".",",")}x`); return; }
  if(a==="git"){ const t = +b.dataset.sn; DP.sn = t; try{ DP.p.seekTo(t, true); DP.p.playVideo(); }catch(_){} setTimeout(bolumIsaretle, 300); window.scrollTo(0,0); $("#dersk").scrollTo({top:0, behavior:"smooth"}); return; }
  if(a==="izle"){ const t = (st().topics||{})[DP.k]||{}; if(t.v){ mutate(x=>{ delete topic(x,DP.k).v; }); } else izlendiYap(); setTimeout(dpCiz, 50); return; }
  if(a==="cev"){ const i = +b.dataset.i, x = c.test[i]; DP.cev[i] = b.dataset.h; if(b.dataset.h===x.d) sesCal("basari");
    if(Object.keys(DP.cev).length===c.test.length){ const d = c.test.filter((y,j)=>DP.cev[j]===y.d).length; ogYaz(o=>{ o.testSonuc = o.testSonuc||{}; o.testSonuc[DP.k] = {d, n:c.test.length, at:Date.now()}; }); }
    else ogYaz(o=>{ o.hata = (o.hata||[]).filter(h=>!(h.k===DP.k && h.i===i)); o.hata.push({k:DP.k, i, at:Date.now(), sonraki:gunSonra(1)}); });
    if(b.dataset.h===x.d) ogYaz(o=>{ (o.hata||[]).forEach(h=>{ if(h.k===DP.k && h.i===i) h.tamam = true; }); });
    dpCiz(); return; }
  if(a==="testtekrar"){ DP.cev = {}; dpCiz(); return; }
  if(a==="cevir"){ DP.ters = !DP.ters; dpCiz(); return; }
  if(a==="kbil" || a==="kbilme"){ const i = +b.dataset.i; ogYaz(o=>{ o.kartlar = o.kartlar||{}; const ks = o.kartlar[DP.k] = o.kartlar[DP.k]||{}, x = ks[i]||{kutu:0};
      x.kutu = a==="kbil" ? Math.min(KUTU.length-1, (ks[i]?x.kutu+1:0)) : 0; x.sonraki = gunSonra(a==="kbil" ? KUTU[x.kutu] : 1); ks[i] = x; });
    if(a==="kbil") sesCal("tik"); DP.ters = false; DP.kart++; dpCiz(); return; }
  if(a==="sor"){ const ne = ($("#dk-ne")||{}).value||""; if(!ne.trim()) return toast("Neyi anlamadığını kısaca yaz"); DP.ne = ne; DP.yanit = true; dpCiz(); return; }
});
document.addEventListener("keydown", e=>{ if(e.key==="Enter" && e.target && e.target.id==="dk-not"){ e.preventDefault(); const b = document.querySelector('[data-dk="notkaydet"]'); if(b) b.click(); } });
/* Ana sayfa: bugünün dersi */
function bugunDersKart(s){ const k = haftaKonulari(s).map(x=>x.k).find(k=>icerik(k) && !((s.topics||{})[k]||{}).v); if(!k) return ""; const c = icerik(k);
  return `<button type="button" class="card bgders" data-ders="${esc(k)}"><span class="vkr"><img src="${thumb(c.vid)}" alt="" loading="lazy"><span class="vkp">▶</span></span><span class="bgdt"><small>Bugünün dersi · koçunun hedefi</small><b>${esc(konuAdi(k))}</b><span class="faint small">${esc(c.kanal)} · özet, test ve kartlarıyla</span></span></button>`; }

function openSheet(kind, el){
  const s = st();
  if(kind==="takvim"){ const t = today(), L = takvim().filter(x=>(x.bit||x.bas) >= t).map(x=>({...x, tip:"deneme"})); Object.values(s?.plan||{}).forEach(p=>(p.yazilar||[]).forEach(y=>{ if(y.tarih && y.tarih>=t) L.push({bas:y.tarih, bit:y.tarih, yayin:"Yazılı", ad:y.ders, tip:"yazili"}); })); L.sort((a,b)=>a.bas.localeCompare(b.bas));
    return sheet(`<h3>Deneme takvimi</h3><p class="muted small" style="margin:0">Türkiye geneli denemeler${s?" ve yazılıların":""}. Tarihler yayınevlerinin açıkladığı programlardan; değişebilir.</p><div class="tkl" style="max-height:60vh;overflow:auto">${L.map(takvimSatir).join("") || `<div class="empty">Yaklaşan deneme yok.</div>`}</div><div class="acts"><button type="button" class="btn pri" data-close>Kapat</button></div>`); }
  if(kind==="soruekle"){ S.sqDosya = null;
    return sheet(`<h3>Soru ekle</h3>
      <div class="squp" id="sq-up"><span id="sq-prev">${icon("note")}<b>Sorunun fotoğrafını ekle</b><small>Sorunun tamamı görünsün</small></span></div>
      <div class="sqbtns"><label class="btn pri">📷 Kamerayı aç<input type="file" accept="image/*" capture="environment" id="sq-cam" hidden></label><label class="btn">🖼️ Galeriden seç<input type="file" accept="image/*" id="sq-file" hidden></label></div>
      <div class="two"><label class="f">Ders<select name="ders" id="sq-ders">${cfg().hedefDers.map(d=>`<option>${esc(d)}</option>`).join("")}<option>Diğer</option></select></label>
      <label class="f">Konu <span class="faint" style="font-weight:500">· isteğe bağlı</span><input type="text" name="konu" id="sq-konu" list="sq-kl" placeholder="ör. Türev"></label></div>
      <datalist id="sq-kl">${[...new Set(dersSubs(s, cfg().hedefDers[0]).flatMap(x=>x.t))].map(n=>`<option value="${esc(n)}">`).join("")}</datalist>
      <label class="f">Not <span class="faint" style="font-weight:500">· isteğe bağlı</span><input type="text" name="not" id="sq-not" placeholder="ör. 3D deneme 12. soru, şıkları anlamadım"></label>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri" id="sq-kaydet">Kaydet</button></div>`,
    async (fd, form)=>{ if(!S.sqDosya) return sheetErr("Önce sorunun fotoğrafını ekle."); const bt = $("#sq-kaydet"); bt.disabled = true; bt.textContent = "Yükleniyor…";
      try{ const [buyuk, kucuk] = await Promise.all([resimKucult(S.sqDosya, 1280, 420000), resimKucult(S.sqDosya, 260, 40000)]); const id = uid(), me = S.me;
        await setDoc(doc(fdb,"soruFoto",id), {sid:me, data:buyuk});
        const q = {sid:me, ders:fd.get("ders"), konu:String(fd.get("konu")||"").trim(), not:String(fd.get("not")||"").trim(), at:nowISO(), durum:"bekliyor", thumb:kucuk};
        await setDoc(doc(fdb,"sorular",id), q); S.sorular.set(id, q); closeSheet(); render(); toast("Soru havuzuna eklendi"); }
      catch(e){ bt.disabled = false; bt.textContent = "Kaydet"; sheetErr("Yüklenemedi: " + (e.message||e)); } }); }
  if(kind==="soru"){ const id = el.dataset.id, q = S.sorular.get(id); if(!q) return;
    setTimeout(async ()=>{ try{ const r = await getDoc(doc(fdb,"soruFoto",id)); const im = $("#sq-big"); if(im && r.exists()){ im.src = r.data().data; im.closest(".sqbig").classList.add("ok"); } }catch(e){ const im = $("#sq-big"); if(im) im.alt = "Resim yüklenemedi"; } }, 0);
    return sheet(`<h3>${esc(q.ders||"Soru")}${q.konu?` · ${esc(q.konu)}`:""}</h3>
      <div class="sqbig"><img id="sq-big" src="${q.thumb||""}" alt="Soru" data-act="sqac"></div>
      <p class="faint small" style="margin:-4px 0 0">${trDate((q.at||"").slice(0,10))} eklendi${q.durum==="cozuldu"&&q.cozAt?` · ${trDate(q.cozAt.slice(0,10))} çözüldü`:""} · büyütmek için resme dokun</p>
      ${q.not?`<div class="card" style="padding:10px 12px;box-shadow:none;border:1px solid var(--line)"><b class="small">Öğrencinin notu</b><p class="small" style="margin:4px 0 0">${esc(q.not)}</p></div>`:""}
      ${A() ? `<label class="f">Koç notu <span class="faint" style="font-weight:500">· öğrenci görür</span><input type="text" id="sq-knot" data-sqnot="${id}" value="${esc(q.kocNot||"")}" placeholder="ör. Görüşmede çözdük, benzer 5 soru çöz"></label>` : (q.kocNot?`<div class="card" style="padding:10px 12px;box-shadow:none;background:var(--acs)"><b class="small">Koçunun notu</b><p class="small" style="margin:4px 0 0">${esc(q.kocNot)}</p></div>`:"")}
      <div class="acts"><button type="button" class="btn" data-act="sqsil" data-id="${id}">${icon("trash","xs")} Sil</button><button type="button" class="btn ${q.durum==="cozuldu"?"":"pri"}" data-act="sqdurum" data-id="${id}">${q.durum==="cozuldu"?"Bekleyene al":`${icon("check","xs")} Çözüldü`}</button><button type="button" class="btn" data-close>Kapat</button></div>`); }
  if(kind==="girisler"){ const L = sortedStudents(), gon = L.filter(([id])=>(S.cnotes.get(id)||{}).girisGonderildi).length;
    return sheet(`<h3>Giriş bilgilerini gönder</h3><p class="muted small" style="margin:0">Her öğrencinin WhatsApp düğmesine dokun; mesaj kullanıcı adı ve şifresiyle hazır açılır, sadece <b>Gönder</b>’e basarsın. ${gon}/${L.length} gönderildi.</p>
      <div class="grlist">${L.map(([id,x])=>girisSatir(id,x)).join("")}</div>
      <details class="small"><summary class="muted" style="cursor:pointer;font-weight:700">Örnek mesaj</summary><pre class="grpre">${esc(girisMesaj({name:"Ayşe Yılmaz", kullanici:"ayseyilmaz", ilkSifre:true}))}</pre></details>
      <div class="acts"><button type="button" class="btn pri" data-close>Bitti</button></div>`); }
  if(kind==="kaynak"){ const d = el.dataset.ders, k = el.dataset.k, ex = k==="kitap" ? (el.dataset.ex||"") : "", adk = k==="kitap" ? "kitap" : "hoca", mevcut = k==="kitap" ? kitapK(s,d,ex) : hoca(s,d);
    KYS = kaynakBol(mevcut); S.kyn = {d, k, ex};
    const MX = isMaarif(s), L = [...kaynakListe(d,k,MX), ...(!MX && k==="kitap" && kaynakListe("_brans","kitap").length ? ["# Branş denemeleri", ...kaynakListe("_brans","kitap")] : [])];
    const gruplar = []; let g = {b:k==="kitap"?"Kitaplar":"Hocalar", l:[]}; L.forEach(x=>{ if(/^#/.test(x)){ if(g.l.length) gruplar.push(g); g = {b:x.replace(/^#\s*/,""), l:[]}; } else g.l.push(x); }); if(g.l.length) gruplar.push(g);
    if(ex){ const diger = ex==="TYT" ? "AYT" : "TYT"; for(let i=gruplar.length-1;i>=0;i--){ if(new RegExp("·\\s*"+diger+"$").test(gruplar[i].b)) gruplar.splice(i,1); } } /* TYT kitabı seçerken AYT önerileri çıkmasın */
    const hepsi = new Set(gruplar.flatMap(x=>x.l)), ozel = KYS.filter(x=>!hepsi.has(x)); if(ozel.length) gruplar.unshift({b:"Bu öğrencide yazılı olan", l:ozel});
    const btn = n => `<button type="button" class="kt" data-act="kys" data-v="${esc(n)}" data-q="${esc(trLow(n))}" aria-pressed="${KYS.includes(n)}">${icon("check","xs")}<span>${esc(n)}</span></button>`;
    return sheet(`<h3>${esc(d)} · ${ex?`<span class="kch ex-${ex}" style="vertical-align:2px"><i>${ex}</i>kitapları</span>`:`takip edilen ${k==="kitap"?"kitaplar":"hocalar"}`}</h3>
      <input type="search" id="kyq" placeholder="${k==="kitap"?"Kitap":"Hoca"} ara" autocomplete="off" aria-label="Ara">
      <div class="klist">${gruplar.map(x=>`<div class="kgrp" data-grp><div class="gh">${esc(x.b)}</div>${x.l.map(btn).join("")}</div>`).join("") || `<p class="faint small">Bu ders için kayıtlı ${adk} yok; aşağıdan ekleyebilirsin.</p>`}</div>
      <p class="small" id="kysel" style="margin:0;font-weight:700"></p>
      <div class="two" style="align-items:end"><label class="f">Listede yoksa elle ekle<input type="text" id="kyfree" placeholder="${k==="kitap"?"ör. Karekök":"ör. Hocanın adı"}"></label><button type="button" class="btn" data-act="kyekle">${icon("plus","xs")} Ekle</button></div>
      <p class="faint small" style="margin:0">Dokunduğun anda kaydedilir. Elle eklediğin ${adk} bu dersin listesine de kaydedilir, sonraki öğrencilerde hazır çıkar.</p>
      <div class="acts"><button type="button" class="btn" data-act="kytemiz">Temizle</button><button type="button" class="btn pri" data-close>Bitti</button></div>`,
    ()=>closeSheet()); }
  if(kind==="blok"){ const d = el.dataset.date, MX = isMaarif(s);
    S.blk = {d, rutin:S.blk?.rutin||"", adet:S.blk?.adet||20, ders:S.blk?.ders||"", ex: MX ? "" : (S.blk?.ex ?? (s.sinif==="Mezun"||s.sinif==="12. sınıf" ? "TYT" : "TYT")), tur:S.blk?.tur||"konusoru", konu:[], sure:S.blk?.sure||null, elle:false}; const b = S.blk;
    return sheet(`<h3>${GUN[dIdx(d)]} ${shortDate(d)} · blok ekle</h3>
      <div class="bkrow bk-nr bk-nd"><div class="gh">Ders</div><div class="chips">${blkDersler(s).map(x=>`<button type="button" class="chip" data-act="bkd" data-v="${esc(x)}" aria-pressed="${x===b.ders}">${esc(x)}</button>`).join("")}</div></div>
      ${MX?"":`<div class="bkrow bk-nr"><div class="gh">Sınav</div><div class="chips"><button type="button" class="chip" data-act="bke" data-v="TYT" aria-pressed="${b.ex==="TYT"}">TYT</button><button type="button" class="chip" data-act="bke" data-v="AYT" aria-pressed="${b.ex==="AYT"}">AYT</button><button type="button" class="chip" data-act="bke" data-v="" aria-pressed="${!b.ex}">Yazma</button></div></div>`}
      <div class="bkrow"><div class="gh">Tür</div><div class="chips">${BLK_TUR.map(([k,l])=>`<button type="button" class="chip" data-act="bkt" data-v="${k}" aria-pressed="${turBasili(b,k)}">${l}</button>`).join("")}</div></div>
      <div class="bkrow bk-r"><div class="gh">Günlük rutin</div><div class="chips">${BLK_RUTIN.map(x=>`<button type="button" class="chip" data-act="bkr" data-v="${x}" aria-pressed="${x===b.rutin}">${x}</button>`).join("")}</div>
        <div class="chips">${BLK_ADET.map(n=>`<button type="button" class="chip" data-act="bka" data-v="${n}" aria-pressed="${n===(b.adet||20)}">${n} soru</button>`).join("")}</div></div>
      <details class="bkrow bkkonu bk-nr bk-nd"><summary><span class="gh">Konu</span> <span class="faint small" id="bk-ksay">isteğe bağlı</span></summary>
        <input type="search" id="bkq" placeholder="Konu ara" autocomplete="off" aria-label="Konu ara">
        <div class="klist" id="bk-konu">${blkKonuHTML(s,b)}</div></details>
      <div class="bkrow bk-nr"><div class="gh">Süre</div><div class="chips">${BLK_SURE.map(h=>`<button type="button" class="chip" data-act="bks" data-v="${h}" aria-pressed="${h===b.sure}">${sureYaz(h)}</button>`).join("")}
        <input type="text" inputmode="decimal" id="bk-elle" class="bkelle" placeholder="elle: 45 dk / 4 saat" aria-label="Süreyi elle yaz"></div></div>
      <div class="bkprev" id="bk-prev"></div>
      <div class="acts"><button type="button" class="btn" data-close>Bitti</button><button type="button" class="btn pri" id="bk-ekle" data-act="bkekle">${icon("plus","xs")} Güne ekle</button></div>`); }
  if(kind==="hizli"){ const d = el.dataset.date, say = new Map(), benim = new Map();
    const ekle = (m, t) => { t = String(t||"").trim(); if(t) m.set(t, (m.get(t)||0)+1); };
    Object.values(s.weeks||{}).forEach(x=>Object.values(x).forEach(l=>(l||[]).forEach(k=>ekle(benim, taskText(k)))));
    S.students.forEach((x,id)=>{ if(id===sid()) return; Object.values(x.weeks||{}).forEach(w=>Object.values(w).forEach(l=>(l||[]).forEach(k=>ekle(say, taskText(k))))); });
    const cz = cetele10(s), czSat = cz.map(ceteleSatir);
    const kayitli = cfg().quick, gor = new Set([...kayitli, ...czSat]), sirala = m => [...m.entries()].filter(([t])=>!gor.has(t)).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0],"tr")).map(([t])=>{ gor.add(t); return t; });
    const g1 = kayitli, g2 = sirala(benim), g3 = sirala(say).slice(0,80);
    const btn = t => `<button type="button" class="kt hz" data-act="hz" data-v="${esc(t)}" data-q="${esc(trLow(t))}">${icon("plus","xs")}<span>${esc(t)}</span></button>`;
    const grp = (b, l) => l.length ? `<div class="kgrp" data-grp><div class="gh">${b}</div>${l.map(btn).join("")}</div>` : "";
    S.hzGun = d;
    return sheet(`<h3>${GUN[dIdx(d)]} ${shortDate(d)} · hızlı ekle</h3>
      <input type="search" id="hq" placeholder="Ara (ör. paragraf, fizik, deneme)" autocomplete="off" aria-label="Satır ara">
      <div class="klist">${cz.length ? `<div class="kgrp" data-grp><div class="gh">Çetelede ${CETELE_ESIK}+ yanlış · tekrar önerisi</div>${cz.map((c,i)=>btn(czSat[i]).replace("</span></button>", ` <small class="kwhy">${c.y} yanlış</small></span></button>`)).join("")}</div>` : ""}${grp("Kayıtlı satırlar", g1)}${grp(`${esc(ilkAd(s.name))} için daha önce yazılanlar`, g2)}${grp("Diğer öğrencilerde kullanılanlar", g3)}
        <p class="faint small" id="hnone" hidden>Eşleşen satır yok.</p></div>
      <button type="button" class="btn sm" id="hfree" data-act="hz" data-v="" hidden></button>
      <p class="faint small" style="margin:0">Dokunduğun satır güne eklenir; pencere açık kalır, birden fazla seçebilirsin. Ayarlar → Hızlı ekle listesi’nden kayıtlı satırları düzenleyebilirsin.</p>
      <div class="acts"><button type="button" class="btn pri" data-close>Bitti</button></div>`); }
  if(kind==="konu"){ const d = el.dataset.ders, w = S.week, p = plan(s,w), cur = ((p.hedef||{})[d]||{}).konu || "";
    const subs = dersSubs(s,d), allT = new Set(subs.flatMap(x=>x.t)); KSEL = splitKonu(cur);
    const free = KSEL.filter(x=>!allT.has(x)); KSEL = KSEL.filter(x=>allT.has(x));
    const one = konuOneri(s,d,subs);
    const tbtn = (sub,n) => { const full = topicScore((s.topics||{})[tkey(sub.k,n)])>=1;
      return `<div class="ktw"><button type="button" class="kt ${full?"bitti":""}" data-act="kt" data-v="${esc(n)}" data-q="${esc(trLow(n+" "+sub.n))}" aria-pressed="${KSEL.includes(n)}">${icon("check","xs")}<span>${esc(n)}</span>${full?`<small>bitti</small>`:""}</button><button type="button" class="kbit ${full?"on":""}" data-act="kbit" data-k="${esc(tkey(sub.k,n))}" aria-pressed="${full}" title="${full?"Bitti işaretini kaldır":"Daha önce bitirdi olarak işaretle"}" aria-label="${esc(n)} bitti">${icon("check","xs")}</button></div>`; };
    return sheet(`<h3>${esc(d)} · bitirilecek konu</h3>
      <input type="search" id="kq" placeholder="Konu ara (ör. basınç, türev)" autocomplete="off" aria-label="Konu ara">
      ${one.length?`<div class="koneri"><div class="gh">Öneri</div>${one.map(o=>`<button type="button" class="kt sug" data-act="kt" data-v="${esc(o.n)}" data-q="${esc(trLow(o.n))}" aria-pressed="${KSEL.includes(o.n)}">${icon("check","xs")}<span>${esc(o.n)}<small class="kwhy">${esc(o.why)}</small></span></button>`).join("")}</div>`:""}
      <div class="klist">${subs.map((sub,si)=>`<div class="kgrp ex-${subEx(sub)||"x"}" data-grp><div class="gh">${sub.ex} · ${esc(sub.n)}</div>${sub.t.map(n=>tbtn(sub,n)).join("")}</div>`).join("")}<p class="faint small" id="knone" hidden>Bu aramayla eşleşen konu yok. Aşağıya elle yazabilirsin.</p></div>
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
    const dl = gunGorusme(d0).filter(x=>x.durum!=="iptal"), sonra = dl.some(x=>x.saat) ? toHm(Math.max(...dl.filter(x=>x.saat).map(x=>hmTo(x.saat)+(x.sure||15)))) : "18:00";
    const kisi = g0 ? (g0.sid || "") : (el.dataset.sid && S.students.has(el.dataset.sid) ? el.dataset.sid : ""), ilk = g0 ? g0.tur==="ilk" : (!!bid || (!!kisi && !gorusmesiVar(kisi)));
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
      S.gday = tarih; closeSheet(); if(!["basvuru","detay"].includes(S.view)) S.view = "gorusme"; render(); toast("Görüşme kaydedildi"); }); }
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
      ${g?`<p class="small muted" style="margin:-4px 0 0">Sonraki görüşme: <b style="color:var(--fg)">${GUN[dIdx(g.tarih)]} ${g.saat||""}</b></p>`:""}
      <div class="f">Hazır mesajlar<div class="walist">${wmesajlar().map((m,i)=>`<button type="button" class="wam" data-act="wagonder" data-i="${i}" data-sid="${sid}">${esc(waDoldur(m, sid))}</button>`).join("")}</div></div>
      <label class="f">Ya da kendin yaz<textarea name="serbest" id="wa-serbest" rows="2" placeholder="Mesajın…"></textarea></label>
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Kapat</button><button class="btn pri">Yazdığımı gönder</button></div>`,
    fd=>{ const t = String(fd.get("serbest")||"").trim(); if(!t) return sheetErr("Bir mesaj yaz ya da hazır mesajlardan birine dokun."); waAc(sid, t); }); }
  if(kind==="tema") return sheet(`<h3>Görünüm</h3>
    <div class="f">Mod<div class="seg">${[["system","Otomatik"],["light","Açık"],["dark","Koyu"]].map(([k,l])=>`<button type="button" data-act="mode" data-v="${k}" aria-pressed="${THEME.mode===k}">${l}</button>`).join("")}</div></div>
    <label class="inline"><input type="checkbox" id="sesAcik" ${SES.acik?"checked":""}>Ses efektleri (dokunma ve görev tamamlama sesleri)</label>
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
      <p class="faint small" style="margin:0">Net = Doğru − Yanlış ÷ 4. Boş bırakılan sorular hesaba girmez.</p>
      ${(()=>{ DYK = {}; const subs = tur==="TYT" ? CURX().TYT : aytSubjects(s,false);
        return `<details class="dykw"><summary><b>Yanlış yaptığın konular</b> <span class="faint small" id="dyk-say">isteğe bağlı · çeteleye eklenir</span></summary>
        <input type="search" id="dyq" placeholder="Konu ara (ör. türev, paragraf)" autocomplete="off" aria-label="Konu ara">
        <div class="klist dyk">${subs.map(sub=>`<div class="kgrp" data-grp><div class="gh">${esc(sub.n)}</div>${sub.t.map(n=>`<div class="dykr" data-q="${esc(trLow(n+" "+sub.n))}"><span>${esc(n)}</span><button type="button" class="mini" data-act="dyk" data-k="${esc(tkey(sub.k,n))}" data-v="-1" aria-label="azalt">−</button><b class="num" data-dyn="${esc(tkey(sub.k,n))}">0</b><button type="button" class="mini" data-act="dyk" data-k="${esc(tkey(sub.k,n))}" data-v="1" aria-label="artır">+</button></div>`).join("")}</div>`).join("")}</div></details>`; })()}
      <div class="err" id="serr"></div><div class="acts"><button type="button" class="btn" data-close>Vazgeç</button><button class="btn pri">Kaydet</button></div>`,
    fd=>{ const d = {id:uid(), tur, yayin:String(fd.get("yayin")).trim(), tarih:fd.get("tarih")||today()}; let any=false;
      for(const [k,n,mx] of F){ const D=num(fd.get(k+"_d"))||0, Y=num(fd.get(k+"_y"))||0; if(D<0||Y<0||D+Y>mx) return sheetErr(`${n}: doğru + yanlış en fazla ${mx} olabilir.`); if(D||Y) any=true; d[k]={d:D,y:Y}; }
      if(!any) return sheetErr("En az bir derste doğru veya yanlış sayısı gir.");
      const yk = Object.fromEntries(Object.entries(DYK).filter(([,n])=>n>0)); if(Object.keys(yk).length){ d.yk = yk; s.topics = s.topics||{}; Object.entries(yk).forEach(([k,n])=>{ const tp = topic(s,k); tp.y = (tp.y||0)+n; }); }
      s.denemeler = s.denemeler||[]; s.denemeler.push(d); save(); closeSheet(); render(); const yt = Object.values(yk).reduce((a,b)=>a+b,0); toast(`${tur} denemesi kaydedildi · ${fmt(totalOf(d))} net${yt?` · ${yt} yanlış çeteleye eklendi`:""}`); }); }
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
      <label class="f">Koçluk paketi<select name="paket" id="m-paket">${(()=>{ const L = cfg().paketler, waIst = /whatsapp/i.test((el.dataset.bid&&S.notifs.get(el.dataset.bid)?.hizmet)||""), sec = x ? paketOf(x).k : (waIst ? L.find(p=>p.tur==="whatsapp") : L.find(p=>p.tur!=="whatsapp"))?.k;
        return L.map(p=>`<option value="${esc(p.k)}" ${p.k===sec?"selected":""}>${esc(p.n)}${num(p.fiyat)!=null?` · ${fmtTL(p.fiyat)}`:""} (${p.tur==="whatsapp"?"ilk görüşme + haftalık rapor":"haftalık birebir seans"})</option>`).join(""); })()}</select></label>
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
      const tel = String(fd.get("tel")||"").trim(), paket = String(fd.get("paket")||paketOf(null).k);
      if(x){ Object.assign(x,{name,alan:fd.get("alan"),sinif:sn,okul,tel,paket});
        const mg = fd.get("merge");
        if(mg && S.students.has(mg)){ const o = S.students.get(mg);
          x.topics = {...o.topics, ...x.topics}; x.denemeler = [...(o.denemeler||[]), ...(x.denemeler||[])];
          const own = {...(x.gunluk||{})}; x.gunluk = {...(o.gunluk||{})}; Object.entries(own).forEach(([d,m])=>x.gunluk[d]=(x.gunluk[d]||0)+m);
          x.weeks = {...(o.weeks||{}), ...(x.weeks||{})}; x.plan = {...(o.plan||{}), ...(x.plan||{})}; x.kitaplar = {...(o.kitaplar||{}), ...(x.kitaplar||{})}; x.hocalar = {...(o.hocalar||{}), ...(x.hocalar||{})}; x.sbAd = {...(o.sbAd||{}), ...(x.sbAd||{})};
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
          S.gorus.forEach((g,gid)=>{ if(g.bid===bid && !g.sid){ S.gorus.set(gid, {...g, sid:nid, ad:name}); persistDoc("gorusmeler", gid, 0); } });
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
    callFn("sifreSifirla", {uid:S.cur, sifre:p}).then(()=>{ toast(`Şifre sıfırlandı · yeni şifre ${p}`); rs.textContent = "Sıfırlandı ✓"; const x = S.students.get(S.cur);
        if(x){ x.ilkSifre = true; if(x.tel){ const t = girisMesaj(x).replace("🔑 İlk şifren: 123456", `🔑 Yeni şifren: ${p}`).replace("Zekacademy koçluk uygulaman hazır!", "Şifreni sıfırladım."); rs.insertAdjacentHTML("afterend", `<a class="btn sm pri" style="margin-top:6px" href="${esc(waLink(x.tel, t))}" target="_blank" rel="noopener">${icon("chat","xs")} Yeni şifreyi WhatsApp’tan gönder</a>`); } } })
      .catch(e=>{ rs.disabled = false; rs.textContent = "Şifreyi sıfırla"; err(e && e.message ? e.message : "Sıfırlanamadı, tekrar dene."); });
  });
}
function updateNets(){
  let tot=0; document.querySelectorAll("#sheetForm .dyrow[data-mx]").forEach(r=>{ const [d,y]=r.querySelectorAll("input"); const D=num(d.value)||0, Y=num(y.value)||0, mx=+r.dataset.mx; const n = D-Y/4; const out=r.querySelector(".net"); if(d.value===""&&y.value===""){ out.textContent="—"; } else { out.textContent = fmt(n); out.style.color = D+Y>mx ? "var(--bad)" : ""; tot+=n; } });
  const t=$("#net-tot"); if(t) t.textContent = fmt(tot);
}

/* ---------- Etkileşim ---------- */
/* Geri al / ileri al (⌘Z, ⇧⌘Z): öğrenci kaydındaki her değişiklik; art arda yazma tek adım sayılır */
const HIST = {};
function mutate(fn){ const s = st(); if(!s) return; const id = sid(), once = A() ? JSON.stringify(s) : null; fn(s);
  if(once && once !== JSON.stringify(s)){ const h = HIST[id] = HIST[id] || {u:[], r:[], t:0}, now = Date.now(); if(now - h.t > 900 || !h.u.length){ h.u.push(once); if(h.u.length > 150) h.u.shift(); } h.t = now; h.r = []; geriDurum(); }
  save(); }
function geriDurum(){ const h = HIST[sid()] || {u:[], r:[]}; document.querySelectorAll("[data-act=geri]").forEach(b=>b.disabled = !h.u.length); document.querySelectorAll("[data-act=ileri]").forEach(b=>b.disabled = !h.r.length); }
function geriAl(ileri){ if(!A() || !st()) return; const id = sid(), h = HIST[id]; const src = h && (ileri ? h.r : h.u), dst = h && (ileri ? h.u : h.r);
  if(!src || !src.length){ toast(ileri ? "İleri alınacak işlem yok" : "Geri alınacak işlem yok"); return; }
  dst.push(JSON.stringify(st())); S.students.set(id, JSON.parse(src.pop())); h.t = 0; save(); if($("#layer .ov")) closeSheet(); render(); geriDurum(); toast(ileri ? "İleri alındı" : "Geri alındı"); }
const topic = (s,k) => s.topics[k] || (s.topics[k] = {});
function toast(t){ document.querySelectorAll(".toast").forEach(x=>x.remove()); const el=document.createElement("div"); el.className="toast"; el.textContent=t; document.body.appendChild(el); setTimeout(()=>el.remove(),2200); }

document.addEventListener("click", e=>{
  const b = e.target.closest("[data-act]"); if(!b || b.tagName==="SELECT" || b.tagName==="INPUT") return;
  const a = b.dataset.act, v = b.dataset.v;
  if(A() && b.closest("#settingsPage") && onSettingClick(a, b)) return;
  if(a && a.startsWith("sz") && szAct(a, b, v)) return;
  if(a==="aiekhak" && A()){ aiEkHak(b.dataset.id); return; }
  if(a==="aipyenile" && A()){ aipYukle(); render(); return; }
  switch(a){
    case "arole": S.authRole=v; if(v==="student" && S.auth==="admin") S.auth="login"; renderAuth(); break;
    case "amode": S.auth=v; renderAuth(); window.scrollTo(0,0); break;
    case "install": doInstall(); break;
    case "adresKopya": { const u = location.origin + "/"; (navigator.clipboard ? navigator.clipboard.writeText(u) : Promise.reject()).then(() => toast("Adres kopyalandı. Chrome'u açıp adres çubuğuna yapıştır."), () => toast(u)); break; }
    case "logout": logout(); break;
    case "pushon": enablePush(); break;
    case "go": S.view=v; if(v==="socoz") szKullanimYukle(); if(v==="aipanel") aipYukle(); if(v==="program"){ S.pmode="gun"; S.day=today(); S.week= st() ? curStart(st()) : monday(new Date()); if(!A() && st()){ const x=st(); if(x.programYeni && x.programYeni>(x.programSeen||"")){ x.programSeen=x.programYeni; save(); } } } closeSheet(); render(); window.scrollTo(0,0); break;
    case "bell": S.view="bildirim"; render(); window.scrollTo(0,0); break;
    case "open": if(!b.dataset.id) break; S.cur=b.dataset.id; S.week=curStart(st()); S.view="detay"; S.dtab="ozet"; render(); window.scrollTo(0,0); break;
    case "dtab": S.dtab=v; if(v==="program"){ S.pmode="gun"; S.day=today(); S.week=curStart(st()); } render(); break;
    case "pmode": S.pmode=v; render(); break;
    case "day": S.day=v; S.pmode="gun"; render(); break;
    case "hgun": { const x = st(); S.view = "program"; S.pmode = "gun"; S.day = v; if(x) S.week = curStart(x); render(); window.scrollTo(0,0); break; }
    case "wk": { const d=+b.dataset.d, x=st(); S.week = d<0 ? pPrev(x,S.week) : d>0 ? pNext(x,S.week) : curStart(x); S.day = d ? S.week : today(); render(); break; }
    case "ex": S.ex=v; render(); break;
    case "aytall": S.aytAll=!S.aytAll; render(); break;
    case "mx": S.mx = +v; render(); break;
    case "odendi": { const id=b.dataset.id, d=b.dataset.d; setOdeme(id, o=>{ o.odenen = {...(o.odenen||{})}; o.odenen[d] = {t:today(), tutar:o.tutar??null}; }); render(); toast(`${S.students.get(id)?.name||""}: ${trDate(d)} ödemesi işlendi`); break; }
    case "vtog": { const id=b.dataset.id, d=b.dataset.d; setOdeme(id, o=>{ o.odenen = {...(o.odenen||{})}; if(o.odenen[d]) delete o.odenen[d]; else o.odenen[d] = {t:today(), tutar:o.tutar??null}; }); openSheet("odeme", b); render(); break; }
    case "osil": { const id=b.dataset.id; const cn = {...(S.cnotes.get(id)||{})}; cn.odeme = null; S.cnotes.set(id, cn); persistDoc("coachNotes", id, 0); closeSheet(); render(); toast("Ödeme planı silindi"); break; }
    case "otaslak": odemeTaslak(); render(); break;
    case "yazili": { const w = b.dataset.w; mutate(x=>{ const p = ensurePlan(x,w); p.yazili = !p.yazili; if(p.yazili && !p.yazilar) p.yazilar = []; }); render(); toast(plan(st(),w).yazili?"Bu hafta yazılı haftası olarak işaretlendi":"Yazılı haftası kaldırıldı"); break; }
    case "yzekle": { const w = b.dataset.w, ders = ($("#yz-ders").value||"").trim(), tarih = $("#yz-tarih").value; if(!ders){ toast("Ders adını yaz"); break; } mutate(x=>{ const p = ensurePlan(x,w); p.yazilar = [...(p.yazilar||[]), {ders, tarih}]; }); render(); setTimeout(()=>{ const i=$("#yz-ders"); if(i) i.focus(); },50); break; }
    case "yzsil": { const w = b.dataset.w, i = +b.dataset.i; mutate(x=>{ const p = ensurePlan(x,w); p.yazilar = (p.yazilar||[]).filter((_,k)=>k!==i); }); render(); break; }
    case "kaydir": { const h = document.getElementById(b.dataset.hedef); if(h){ h.scrollIntoView({behavior:"smooth", block:"start"}); h.classList.remove("vurgu"); void h.offsetWidth; h.classList.add("vurgu"); } break; }
    case "git": { S.view = v; if(b.dataset.mod){ S.pmode = b.dataset.mod; const x = st(); if(x){ S.week = curStart(x); S.day = today(); } } render(); window.scrollTo(0,0);
      if(b.dataset.hedef) setTimeout(()=>{ const h = document.getElementById(b.dataset.hedef); if(h){ h.scrollIntoView({behavior:"smooth", block:"start"}); h.classList.add("vurgu"); } }, 350); break; }
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
    case "ngizle": { const n = S.notifs.get(b.dataset.id); if(n){ n.zilGizli = true; n.read = true; persistDoc("notifs", b.dataset.id, 0); } render(); toast("Bildirimden kaldırıldı · Başvurular'da duruyor"); break; }
    case "ntemizle": { if(!b.dataset.armed){ b.dataset.armed = "1"; b.textContent = "Emin misin? Tekrar dokun"; setTimeout(()=>{ if(b.isConnected){ delete b.dataset.armed; b.textContent = "Tümünü temizle"; } }, 3000); break; }
      let k = 0; [...S.notifs.entries()].forEach(([id,n])=>{ if(n.type==="basvuru"){ if(!n.zilGizli){ n.zilGizli = true; n.read = true; persistDoc("notifs", id, 0); k++; } } else { S.notifs.delete(id); deleteDoc(doc(fdb,"notifs",id)).catch(()=>{}); k++; } });
      render(); toast(`${k} bildirim temizlendi · başvurular Başvurular sayfasında duruyor`); break; }
    case "nsil": { const id=b.dataset.id; S.notifs.delete(id); deleteDoc(doc(fdb,"notifs",id)).catch(()=>toast("Silinemedi")); render(); break; }
    case "formkod": formKod(b.dataset.v2==="yenile"); break;
    case "kopyala": { const el=document.getElementById(b.dataset.hedef); if(el){ (navigator.clipboard?navigator.clipboard.writeText(el.textContent):Promise.reject()).then(()=>toast("Kopyalandı")).catch(()=>{ const r=document.createRange(); r.selectNodeContents(el); const sel=getSelection(); sel.removeAllRanges(); sel.addRange(r); toast("Seçildi, kopyala de"); }); } break; }
    case "otaslaksil": S.students.forEach((_,id)=>{ const o = odemeOf(id); if(o && o.taslak){ const cn = {...(S.cnotes.get(id)||{})}; cn.odeme = null; S.cnotes.set(id, cn); persistDoc("coachNotes", id, 0); } }); render(); toast("Taslak ödeme verileri silindi"); break;
    case "bkd": S.blk.ders = v; S.blk.konu = []; if(!isMaarif(st())){ if(/türkçe/i.test(v)) S.blk.ex = "TYT"; else if(/edebiyat/i.test(v)) S.blk.ex = "AYT"; } { const k = $("#bk-konu"); if(k) k.innerHTML = blkKonuHTML(st(), S.blk); } blkGuncelle(); break;
    case "bke": S.blk.ex = v; S.blk.konu = []; { const k = $("#bk-konu"); if(k) k.innerHTML = blkKonuHTML(st(), S.blk); } blkGuncelle(); break;
    case "bkt": S.blk.tur = v; if(v==="deneme") S.blk.konu = []; { const k = $("#bk-konu"); if(k) k.innerHTML = blkKonuHTML(st(), S.blk); } blkGuncelle(); break;
    case "sqf": S.sqf = v; render(); break;
    case "sqdurum": { const id = b.dataset.id, q = S.sorular.get(id); if(!q) break; const cz = q.durum!=="cozuldu"; const yeni = {...q, durum: cz?"cozuldu":"bekliyor", cozAt: cz?nowISO():null};
      S.sorular.set(id, yeni); updateDoc(doc(fdb,"sorular",id), new FieldPath("durum"), yeni.durum, new FieldPath("cozAt"), yeni.cozAt).catch(e=>toast("Kaydedilemedi")); closeSheet(); render(); toast(cz?"Çözüldü olarak işaretlendi 🎉":"Bekleyenlere alındı"); break; }
    case "sqsil": { if(!b.dataset.armed){ b.dataset.armed = "1"; b.textContent = "Silinsin mi? Tekrar dokun"; break; } const id = b.dataset.id; S.sorular.delete(id);
      deleteDoc(doc(fdb,"sorular",id)).catch(()=>{}); deleteDoc(doc(fdb,"soruFoto",id)).catch(()=>{}); closeSheet(); render(); toast("Soru silindi"); break; }
    case "sqac": { const w = window.open(); if(w){ w.document.write(`<title>Soru</title><body style="margin:0;background:#000;display:grid;place-items:center;min-height:100vh"><img src="${b.src}" style="max-width:100%;height:auto">`); } break; }
    case "dyk": { const k = b.dataset.k; DYK[k] = Math.max(0, (DYK[k]||0) + (+v)); const e = [...document.querySelectorAll("#layer [data-dyn]")].find(x=>x.dataset.dyn===k); if(e){ e.textContent = DYK[k]; e.closest(".dykr").classList.toggle("on", DYK[k]>0); }
      const n = Object.values(DYK).filter(x=>x>0).length, t = Object.values(DYK).reduce((a,b)=>a+b,0), sy = $("#dyk-say"); if(sy) sy.textContent = t ? `${n} konu · ${t} yanlış çeteleye eklenecek` : "isteğe bağlı · çeteleye eklenir"; break; }
    case "kys": { const on = !KYS.includes(v); KYS = on ? [...KYS, v] : KYS.filter(x=>x!==v); document.querySelectorAll("#layer [data-act=kys]").forEach(x=>{ if(x.dataset.v===v) x.setAttribute("aria-pressed", on); }); kysNot(true); break; }
    case "kytemiz": KYS = []; document.querySelectorAll("#layer [data-act=kys]").forEach(x=>x.setAttribute("aria-pressed", false)); kysNot(true); break;
    case "kyekle": { const inp = $("#kyfree"), n = (inp?.value||"").trim(); if(!n) break; const {d, k} = S.kyn;
      if(!KYS.includes(n)) KYS.push(n);
      if(!kaynakListe(d,k,isMaarif(st())).includes(n)){ const K = S.settings.kaynak = S.settings.kaynak ? S.settings.kaynak : clone(DEF_KAYNAK); K[d] = K[d] || {kitap:[], hoca:[]}; const L0 = K[d][k]||[], basliklar = L0.filter(x=>/^#/.test(x)); K[d][k] = [...L0, ...(basliklar.length && basliklar[basliklar.length-1]!=="# Diğer" ? ["# Diğer"] : []), n]; saveSettings(); }
      const lst = $("#layer .klist"); if(lst && ![...lst.querySelectorAll("[data-act=kys]")].some(x=>x.dataset.v===n)) lst.insertAdjacentHTML("afterbegin", `<div class="kgrp" data-grp><div class="gh">Yeni eklenen</div><button type="button" class="kt" data-act="kys" data-v="${esc(n)}" data-q="${esc(trLow(n))}" aria-pressed="true">${icon("check","xs")}<span>${esc(n)}</span></button></div>`);
      document.querySelectorAll("#layer [data-act=kys]").forEach(x=>{ if(x.dataset.v===n) x.setAttribute("aria-pressed", true); }); inp.value = ""; kysNot(true); toast(`${n} eklendi`); break; }
    case "kcsil": { const d = b.dataset.ders, k = b.dataset.k, ex = b.dataset.ex||"", alan = k==="kitap" ? "kitaplar" : "hocalar", key = k==="kitap" && ex==="AYT" ? d+"|AYT" : d; const L = kaynakBol(k==="kitap" ? kitapK(st(),d,ex) : hoca(st(),d)).filter(x=>x!==v);
      mutate(x=>{ x[alan] = x[alan]||{}; if(L.length) x[alan][key] = L.join(" + "); else delete x[alan][key]; }); const g = b.closest(".gk"); if(g) g.outerHTML = kaynakCipleri(st(), d, k, ex); break; }
    case "tkopya": { const t = b.closest(".tr")?.querySelector(".tin")?.value.trim(); if(!t) break; S.pano = S.pano || []; if(!S.pano.includes(t)) S.pano.push(t);
      try{ navigator.clipboard?.writeText(S.pano.join("\n"))?.catch(()=>{}); }catch(_){}
      panoGuncelle(); toast(S.pano.length>1 ? `${S.pano.length} görev panoda · istediğin günde “Yapıştır”a bas` : "Kopyalandı · istediğin günde “Yapıştır”a bas"); break; }
    case "tyapistir": { (S.pano||[]).forEach(t=>gunEkle(b.dataset.date, t)); toast(`${(S.pano||[]).length} görev yapıştırıldı`); break; }
    case "ptemizle": S.pano = []; panoGuncelle(); break;
    case "tur": if(b.dataset.l) S.turListe = b.dataset.l; S.tur = +v; render(); break;
    case "turbitir": S.tur = null; S.turKapandi = true; if(!A() && st() && (!st().tanitim || st().yenilik!==YENILIK_SURUM)){ st().tanitim = true; st().yenilik = YENILIK_SURUM; save(); } render(); break;
    case "girisgonder": { const id = b.dataset.id, cn = {...(S.cnotes.get(id)||{}), girisGonderildi: nowISO()}; S.cnotes.set(id, cn); persistDoc("coachNotes", id, 0);
      setTimeout(()=>{ const r = b.closest(".grrow"); if(r) r.outerHTML = girisSatir(id, S.students.get(id)); }, 300); return; }
    case "geri": geriAl(false); break;
    case "ileri": geriAl(true); break;
    case "kbit": { const k = b.dataset.k; let full = false; mutate(x=>{ x.topics = x.topics||{}; const t = x.topics[k] = x.topics[k]||{}; if(topicScore(t)>=1){ delete t.r; delete t.s1; delete t.s2; } else { t.r = Math.max(1, t.r||0); t.s1 = true; t.s2 = true; full = true; } if(!Object.keys(t).length) delete x.topics[k]; });
      b.classList.toggle("on", full); b.setAttribute("aria-pressed", full); const kt = b.previousElementSibling; if(kt){ kt.classList.toggle("bitti", full); const sm = kt.querySelector("small:not(.kwhy)"); if(full && !sm) kt.insertAdjacentHTML("beforeend", "<small>bitti</small>"); if(!full && sm) sm.remove(); }
      toast(full ? "Bitti olarak işaretlendi" : "Bitti işareti kaldırıldı"); break; }
    case "tdel": { const r = b.closest(".tr"), box = b.closest(".tl"); if(r && box){ r.remove(); tlSync(box); } break; }
    case "bkr": S.blk.rutin = v; blkGuncelle(); break;
    case "bka": S.blk.adet = +v; blkGuncelle(); break;
    case "bks": S.blk.sure = +v; S.blk.elle = false; { const e = $("#bk-elle"); if(e) e.value = ""; } blkGuncelle(); break;
    case "bkk": { const on = !S.blk.konu.includes(v); S.blk.konu = on ? [...S.blk.konu, v] : S.blk.konu.filter(x=>x!==v); b.setAttribute("aria-pressed", on); blkGuncelle(); break; }
    case "bkekle": { const t = blkSatir(S.blk); if(!t) break; gunEkle(S.blk.d, t);
      toast(`Eklendi: ${t}`); S.blk.konu = []; document.querySelectorAll("#layer [data-act=bkk]").forEach(x=>x.setAttribute("aria-pressed", false)); blkGuncelle(); break; }
    case "hz": { const t = String(v||"").trim(); if(!t) break; gunEkle(S.hzGun, t);
      b.classList.add("on"); b.dataset.n = (+b.dataset.n||0)+1; toast(`Eklendi: ${t}`); const q = $("#hq"); if(q && b.id==="hfree"){ q.value=""; q.dispatchEvent(new Event("input",{bubbles:true})); } break; }
    case "kt": { const n=v, on=!KSEL.includes(n); KSEL = on ? [...KSEL, n] : KSEL.filter(x=>x!==n); document.querySelectorAll("#layer .kt").forEach(x=>{ if(x.dataset.v===n) x.setAttribute("aria-pressed", on); }); kselNote(); break; }
    case "kclear": KSEL=[]; document.querySelectorAll("#layer .kt").forEach(x=>x.setAttribute("aria-pressed","false")); { const f=$("#kfree"); if(f) f.value=""; } kselNote(); break;
    case "tick": { const d=b.dataset.date, id=b.dataset.id; { const s0 = st(); if(!A() && s0 && s0.timer && s0.timer.task && s0.timer.task.id===id){ const r = sayacDurdur(true); sesCal("basari"); render(); toast(`Tebrikler! ${r.added>0?`+${fmtMin(r.added)} · `:""}görev tamamlandı`); break; } } mutate(s=>{ const it=dayTasks(s,d).find(x=>x.id===id); if(it){ it.done=!it.done; it.doneAt = it.done ? today() : null; if(it.done) sesCal("basari"); else sesCal("tik"); if(it.done && !A()){ const l=dayTasks(s,d); if(l.every(x=>x.done)) setTimeout(()=>toast("Bugünün tüm görevleri tamam! 🎉"),50); } } }); render(); break; }
    case "copyweek": { if(!A()) break; mutate(s=>{ const pw=pPrev(s,S.week), pp=plan(s,pw), np=ensurePlan(s,S.week), oldDays=pDays(s,pw); let c=0;
      pDays(s,S.week).forEach((cd,i)=>{ const pd = oldDays.find(o=>dIdx(o)===dIdx(cd)); if(!pd) return; const src=dayTasks(s,pd); c+=src.length; setDayTasks(s,cd, src.map(t=>({id:uid(), t:taskText(t), done:false, doneAt:null}))); const sv=(pp.saat||{})[pIdx(s,pd)]; if(sv!=null&&sv!=="") np.saat[i]=sv; });
      np.hedef = {}; Object.entries(pp.hedef||{}).forEach(([d,v])=>{ if(v&&v.konu) np.hedef[d]={konu:v.konu, done:false}; });
      toast(c?`Geçen haftanın planı kopyalandı (${c} görev)`:"Geçen hafta için plan yok"); }); render(); break; }
    case "gtick": { const w=b.dataset.w, d=b.dataset.ders; mutate(s=>{ const p=ensurePlan(s,w); if(p.hedef[d]) p.hedef[d].done=!p.hedef[d].done; }); render(); break; }
    case "cpsel": { document.querySelectorAll('#sheetForm input[name=days]').forEach(c=>{ const di=dIdx(c.value); c.checked = v==="hepsi" ? true : di<5; }); break; }
    case "rep": case "yan": { const f = a==="rep"?"r":"y"; mutate(s=>{ const t=topic(s,b.dataset.k); t[f]=Math.max(0,(t[f]||0)+(+b.dataset.d)); }); keepOpen(()=>render()); break; }
    case "sb": mutate(s=>{ const t=topic(s,b.dataset.k); t[b.dataset.f]=!t[b.dataset.f]; }); keepOpen(()=>render()); break;
    case "ddel": { if(!b.dataset.armed){ b.dataset.armed="1"; b.style.color="var(--bad)"; b.style.borderColor="var(--bad)"; toast("Silmek için tekrar dokun"); setTimeout(()=>{ if(b.isConnected){ delete b.dataset.armed; b.style.color=""; b.style.borderColor=""; } },2500); break; }
      mutate(s=>{ const dd = (s.denemeler||[]).find(d=>d.id===b.dataset.id); if(dd && dd.yk) Object.entries(dd.yk).forEach(([k,n])=>{ const tp = (s.topics||{})[k]; if(tp){ tp.y = Math.max(0,(tp.y||0)-n); if(!tp.y) delete tp.y; } }); s.denemeler=s.denemeler.filter(d=>d.id!==b.dataset.id); }); render(); toast("Deneme silindi"); break; }
    case "tstart": mutate(s=>{ s.timer={start:Date.now()}; }); render(); break;
    case "tstop": { const {added} = sayacDurdur(false); render(); toast(added>0?`+${fmtMin(added)} kaydedildi`:"1 dakikadan kısa süre kaydedilmedi"); break; }
    case "tgbasla": { const s0 = st(); if(s0 && s0.timer){ const r = sayacDurdur(false); if(r.added>0) toast(`Önceki sayaç durdu · +${fmtMin(r.added)}`); }
      mutate(s=>{ s.timer = {start:Date.now(), task:{id:b.dataset.id, date:b.dataset.date}}; }); render(); toast("Sayaç başladı · ara verirken “Durdur”a bas"); break; }
    case "tgbitir": { const {added, ad} = sayacDurdur(v==="bitti"); render();
      toast(v==="bitti" ? `Tebrikler! ${added>0?`+${fmtMin(added)} · `:""}görev tamamlandı` : (added>0?`+${fmtMin(added)} kaydedildi · görevi bitirdiysen yuvarlağa dokun`:"1 dakikadan kısa süre kaydedilmedi")); break; }
    case "sheet": openSheet(v, b); wireSheetExtras(); if(v==="hizli"){ const q = $("#hq"); if(q) q.focus({preventScroll:true}); } if(v==="blok") blkGuncelle(); if(v==="kaynak") kysNot(); break;
    case "dtur": { S.ex=v; openSheet("deneme", b); break; }
    case "mode": THEME.mode=v; applyTheme(); openSheet("tema"); render(); break;
    case "temagec": THEME.mode = koyuMu() ? "light" : "dark"; applyTheme(); render(); break;
    case "accent": THEME.accent=v; applyTheme(); openSheet("tema"); render(); break;
    case "addq": { const h=$("#su-h"), m=$("#su-m"); const t=(num(h.value)||0)*60+(num(m.value)||0)+(+v); h.value=Math.floor(t/60); m.value=t%60; break; }
    case "sendnote": { const t=$("#kn").value.trim(); if(!t){ toast("Önce notu yaz"); break; } mutate(s=>{ s.koctanNot={text:t, date:nowISO()}; }); render(); toast("Not öğrencinin ana sayfasına gönderildi"); break; }
    case "clearnote": mutate(s=>{ s.koctanNot=null; }); render(); toast("Not kaldırıldı"); break;
  }
});
function keepOpen(fn){ const open = [...document.querySelectorAll("details.subj")].map((d,i)=>d.open?i:-1).filter(i=>i>=0); fn(); const ds=document.querySelectorAll("details.subj"); open.forEach(i=>{ if(ds[i]) ds[i].open=true; }); }
document.addEventListener("change", e=>{
  const t = e.target;
  if(t.id==="sesAcik"){ SES.acik = t.checked; try{ localStorage.setItem("zk-ses", t.checked ? "1" : "0"); }catch(_){} if(t.checked) sesCal("basari"); return; }
  if((t.id==="szFoto" || t.id==="szKamera" || t.id==="szGaleri") && t.files && t.files[0]){ szFotoSec(t.files[0]); return; }
  if((t.id==="sq-file" || t.id==="sq-cam") && t.files && t.files[0]){ S.sqDosya = t.files[0]; const pv = $("#sq-prev"); if(pv) pv.innerHTML = `<img src="${URL.createObjectURL(t.files[0])}" alt="">`; return; }
  if(t.id==="sq-ders"){ const dl = $("#sq-kl"); if(dl) dl.innerHTML = [...new Set(dersSubs(st(), t.value).flatMap(x=>x.t))].map(n=>`<option value="${esc(n)}">`).join(""); return; }
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
document.addEventListener("keydown", e=>{
  /* ⌘Z / Ctrl+Z geri al, ⇧⌘Z / Ctrl+Y ileri al (ayar ve not alanlarında tarayıcının kendi geri alması çalışır) */
  if((e.metaKey || e.ctrlKey) && !e.altKey && (e.key.toLowerCase()==="z" || (e.ctrlKey && e.key.toLowerCase()==="y")) && A() && S.cur && ["detay","program"].includes(S.view)){
    const a = document.activeElement, yazi = a && a.matches && a.matches("textarea,input[type=text],input[type=number]") && !a.classList.contains("tin");
    if(!yazi){ e.preventDefault(); geriAl(e.key.toLowerCase()==="y" || e.shiftKey); return; } }
  /* Ok tuşları: açılan pencerede arama kutusu ve listeler arasında gezin */
  if(["ArrowDown","ArrowUp","ArrowLeft","ArrowRight"].includes(e.key) && $("#layer .ov")){ const a = document.activeElement, gor = x => !x.hidden && !x.closest("[hidden]") && x.offsetParent !== null;
    const L = [...document.querySelectorAll("#layer .klist .kt")].filter(gor), ara = $("#layer input[type=search]");
    if(a && (a.classList.contains("kt") || a.type==="search") && (e.key==="ArrowDown" || e.key==="ArrowUp")){ const i = L.indexOf(a); let h = null;
      if(a.type==="search") h = e.key==="ArrowDown" ? L[0] : null; else h = e.key==="ArrowDown" ? L[i+1] : (i>0 ? L[i-1] : ara);
      if(h){ e.preventDefault(); h.focus({preventScroll:true}); h.scrollIntoView({block:"nearest"}); } return; }
    if(a && a.classList.contains("chip")){ const C = [...document.querySelectorAll("#layer .chip")].filter(gor), i = C.indexOf(a);
      if(e.key==="ArrowRight" || e.key==="ArrowLeft"){ const h = C[i + (e.key==="ArrowRight" ? 1 : -1)]; if(h){ e.preventDefault(); h.focus(); } return; }
      const satirlar = [...document.querySelectorAll("#layer .chips")].filter(gor), si = satirlar.indexOf(a.closest(".chips")), hedef = satirlar[si + (e.key==="ArrowDown" ? 1 : -1)];
      if(hedef){ const h = [...hedef.querySelectorAll(".chip")].find(gor); if(h){ e.preventDefault(); h.focus(); } } return; } }
  if(e.key==="Enter" && e.target.id==="kyfree"){ e.preventDefault(); $("#layer [data-act=kyekle]")?.click(); return; }
  if(e.key==="Enter" && e.target.id==="kyq"){ e.preventDefault(); const b=[...document.querySelectorAll("#layer .klist .kt")].find(x=>!x.hidden && !x.closest("[hidden]")); if(b) b.click(); else $("#layer [data-act=kyekle]")?.click(); return; }
  if(e.key==="Enter" && e.target.id==="hq"){ e.preventDefault(); const b=[...document.querySelectorAll("#layer .klist .kt")].find(x=>!x.hidden && !x.closest("[hidden]")) || ($("#hfree")?.hidden ? null : $("#hfree")); if(b) b.click(); return; }
  if(e.key==="Enter" && e.target.id==="kq"){ e.preventDefault(); const b=[...document.querySelectorAll("#layer .klist .kt")].find(x=>!x.hidden && !x.closest("[hidden]")); if(b) b.click(); } });
document.addEventListener("input", e=>{
  if(e.target && e.target.id==="szMetin"){ SZ.metin = e.target.value; return; }
  const t = e.target;
  if(A() && t.closest && t.closest("#settingsPage")){ onSetting(t,false); return; }
  if(t.dataset.gnot){ const id = gorusSet(t.dataset.gnot, g=>{ g.not = t.value; }); if(id!==t.dataset.gnot){ t.dataset.gnot = id; S.gsel = id; } return; }
  if(t.classList && t.classList.contains("tin")){ tlSatirGuncelle(t); oneriGoster(t); const box = t.closest(".tl"); clearTimeout(t._z); t._z = setTimeout(()=>tlSync(box), 350); return; }
  if(t.id==="bk-elle"){ const h = sureOku(t.value); if(S.blk){ S.blk.sure = h; S.blk.elle = !!h; blkGuncelle(); } return; }
  if(t.dataset.sqnot){ const id = t.dataset.sqnot, q = S.sorular.get(id); if(q){ q.kocNot = t.value; clearTimeout(t._z); t._z = setTimeout(()=>updateDoc(doc(fdb,"sorular",id), new FieldPath("kocNot"), t.value).catch(()=>toast("Not kaydedilemedi")), 600); } return; }
  if(t.id==="dyq"){ const q = trLow(t.value).trim(); document.querySelectorAll("#layer .dyk .kgrp").forEach(g=>{ let n=0; g.querySelectorAll(".dykr").forEach(r=>{ const ok = !q || q.split(/\s+/).every(w=>r.dataset.q.includes(w)); r.hidden=!ok; if(ok) n++; }); g.hidden = !n; }); return; }
  if(t.id==="kyq"){ const q = trLow(t.value).trim(); document.querySelectorAll("#layer .klist .kgrp").forEach(g=>{ let n=0; g.querySelectorAll(".kt").forEach(b=>{ const ok = !q || b.dataset.q.includes(q); b.hidden=!ok; if(ok) n++; }); g.hidden = !n; }); const f = $("#kyfree"); if(f && q) f.value = t.value; return; }
  if(t.id==="bkq"){ const q = trLow(t.value).trim(); document.querySelectorAll("#bk-konu .kgrp").forEach(g=>{ let n=0; g.querySelectorAll(".kt").forEach(b=>{ const ok = !q || q.split(/\s+/).every(w=>b.dataset.q.includes(w)); b.hidden=!ok; if(ok) n++; }); g.hidden = !n; }); return; }
  if(t.id==="hq"){ const q = trLow(t.value).trim(); let any=false, tam=false;
    document.querySelectorAll("#layer .klist .kgrp").forEach(g=>{ let n=0; g.querySelectorAll(".kt").forEach(b=>{ const ok = !q || q.split(/\s+/).every(w=>b.dataset.q.includes(w)); b.hidden=!ok; if(ok) n++; if(b.dataset.q===q) tam=true; }); g.hidden = !n; if(n) any=true; });
    const hn=$("#hnone"); if(hn) hn.hidden = any; const hf=$("#hfree"); if(hf){ hf.hidden = !q || tam; hf.dataset.v = t.value.trim(); hf.textContent = `“${t.value.trim()}” satırını ekle`; } return; }
  if(t.id==="kq"){ const q = trLow(t.value).trim(); let any=false;
    document.querySelectorAll("#layer .klist .kgrp").forEach(g=>{ let n=0; g.querySelectorAll(".kt").forEach(b=>{ const ok = !q || b.dataset.q.includes(q); b.hidden=!ok; const w = b.closest(".ktw"); if(w) w.hidden=!ok; if(ok) n++; }); g.hidden = !n; if(n) any=true; });
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
  const tv=$("#tval"); if(tv) tv.textContent = clock(timerMin(s)*60); document.querySelectorAll("[data-tlive]").forEach(x=>x.textContent = clock(timerMin(s)*60));
  const tt=$("#ttoday"); if(tt) tt.textContent = fmtMin(minutes(s,today()));
  const lm=$("#liveMin"); if(lm) lm.textContent = fmtMin(minutes(s,today()));
}, 1000);

render();
init();


document.addEventListener("keydown", e=>{ if(e.target && e.target.id==="szSor" && e.key==="Enter" && !e.shiftKey){ e.preventDefault(); szAct("szsor"); } });
