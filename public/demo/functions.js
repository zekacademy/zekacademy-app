export function getFunctions(){ return {}; }
export function httpsCallable(f, name){ return async (data)=>{ window.__calls = (window.__calls||[]); window.__calls.push([name, data]); if(name==="ogrenciSil"){ const db = window.__db; delete db["students/"+data.uid]; localStorage.setItem("mockDb", JSON.stringify(db)); } if(name==="soruCoz"){ await new Promise(r=>setTimeout(r, 900)); return {data: window.__soruOrnek || DEMO_SORU}; } if(name==="denemeOku"){ await new Promise(r=>setTimeout(r, 1200)); return {data: window.__karneOrnek || DEMO_KARNE}; } if(name==="formAnahtari") return {data:{anahtar:"abc123", url:"https://europe-west3-zekacademy-59b2f.cloudfunctions.net/formBasvuru"}}; return {data:{ok:true}}; }; }

/* Demo: karne okuma her dosyada aynı örnek karneyi döndürür (gerçek okumayı sunucu yapar) */
const DEMO_KARNE = { okunabildi:true, belgeTuru:"karne", uyarilar:["Demo modu: gerçek okuma yapılmadı, örnek karne gösteriliyor."], denemeler:[
  { tur:"TYT", yayin:"3D", sinavAdi:"3D TG TYT 1 2027", tarih:"2026-11-01", kaynak:"ana", toplam:104.5, emin:true, notlar:[], puan:442.9, siralama:"1.198/85.472", altDersler:{},
    bolumler:{ turkce:{d:33,y:4}, sosyal:{d:20,y:0}, mat:{d:35,y:1}, fen:{d:18,y:1} },
    yanlislar:[ {ders:"Matematik",no:3,konu:"Rasyonel Sayılar",eslesen:"Rasyonel Sayılar",durum:"yanlis"}, {ders:"Matematik",no:7,konu:"Tek Çift Sayılar",eslesen:"Temel Kavramlar",durum:"yanlis"},
      {ders:"Kimya",no:13,konu:"Atomun Yapısı",eslesen:"Atom ve Yapısı",durum:"yanlis"}, {ders:"Kimya",no:10,konu:"Asitlerin ve Bazların Tepkimeleri",eslesen:"Asitler, Bazlar ve Tuzlar",durum:"yanlis"},
      {ders:"Türkçe",no:9,konu:"Paragrafta Yardımcı Düşünce",eslesen:null,durum:"yanlis"}, {ders:"Biyoloji",no:17,konu:"Ekosistemde Enerji Akışı",eslesen:"Ekosistem",durum:"yanlis"},
      {ders:"Matematik",no:1,konu:"Sayı Basamakları",eslesen:"Sayı Basamakları",durum:"bos"} ] },
  { tur:"TYT", yayin:"Bilgi Sarmal", sinavAdi:"BİLGİ SARMAL TG TYT 2", tarih:"2026-07-26", kaynak:"gecmis", toplam:95.5, emin:true, notlar:[], altDersler:{}, bolumler:{ turkce:{net:30.25}, sosyal:{net:20}, mat:{net:30.25}, fen:{net:15} }, yanlislar:[] },
  { tur:"TYT", yayin:"Sıfır Pozitif", sinavAdi:"SIFIR POZİTİF TG TYT", tarih:"2026-10-18", kaynak:"gecmis", toplam:89.25, emin:true, notlar:[], altDersler:{}, bolumler:{ turkce:{net:24}, sosyal:{net:18}, mat:{net:28.5}, fen:{net:18.75} }, yanlislar:[] } ] };

/* Demo: Soru Çözüm her fotoğrafta aynı örnek çözümü döndürür */
const DEMO_SORU = { cozum: { okunabildi:true, emin:true, anahtar:"uyumlu", ders:"Matematik", konu:"Ondalık Sayılar", zorluk:"kolay",
  soru:"Dört çiçeğin sap uzunlukları 17,9 cm; 16,8 cm; 19,2 cm ve 20 cm'dir. Hepsi en kısa sapla eşit olacak şekilde kesilirse toplam kaç cm kesilir?",
  siklar:{A:"6,3",B:"6,5",C:"6,7",D:"7,1",E:"7,3"}, istenen:"Üç saptan kesilen parçaların toplam uzunluğu.",
  bilgi:[{ad:"Kullanacağımız bilgi", ifade:"Kesilen = sap uzunluğu − en kısa sap"}],
  adimlar:[{baslik:"En kısa sapı bul", aciklama:"Uzunluklar 17,9; 16,8; 19,2 ve 20. En kısa sap **16,8 cm**."},
    {baslik:"Kesilecek payları hesapla", aciklama:"Diğer üç sap 16,8 cm'ye inmeli. Her birinden kesilecek miktarı bul.", islem:"17,9 − 16,8 = 1,1; 19,2 − 16,8 = 2,4; 20 − 16,8 = 3,2"},
    {baslik:"Topla", aciklama:"Kesilen parçaları topla.", islem:"1,1 + 2,4 + 3,2 = 6,7"}],
  cevap:{sik:"C", deger:"6,7 cm"}, puf:"Önce farkları al, sonra topla; toplamdan 4 × en kısa çıkarmak da aynı sonucu verir." }, id:"demo", model:"kolay", hak:1, kalan:119, toplam:120 };
