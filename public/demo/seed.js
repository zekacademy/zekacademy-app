/* Zekacademy demo modu: gerçek veriye bağlanmaz. Her şey bu tarayıcının hafızasında kalır.
   Açmak: ?demo=1   Kapatmak: ?demo=0
   Koç girişi: zekacademy / demo1234   Öğrenci girişi: demo / 123456 */
(function(){
  if (localStorage.getItem("mockDb") && localStorage.getItem("zk-demo-v") === "10") return;
  var gun = 864e5, bugun = new Date(); bugun.setHours(12,0,0,0);
  function iso(d){ var x = new Date(d); x.setMinutes(x.getMinutes() - x.getTimezoneOffset()); return x.toISOString().slice(0,10); }
  function ekle(d, n){ return iso(new Date(new Date(d + "T12:00:00").getTime() + n*gun)); }
  var t = iso(bugun), dow = (bugun.getDay() + 6) % 7, pzt = ekle(t, -dow), gecen = ekle(pzt, -7);
  var n = 0; function id(){ return "dm" + (++n); }
  function g(metin, bitti, gunTarih){ return {id:id(), t:metin, done:!!bitti, doneAt: bitti ? gunTarih : null}; }
  var sablon = [
    ["Paragraf 20 soru", "TYT Matematik Konu Soru Çalışması (1,5 saat)", "Fizik Konu Soru Çalışması (1 saat)", "Problem 20 soru"],
    ["Paragraf 20 soru", "AYT Matematik Konu Soru Çalışması (1,5 saat)", "Kimya Konu Soru Çalışması (1 saat)", "Biyoloji Tekrar (45 dk)"],
    ["Paragraf 20 soru", "Geometri Konu Soru Çalışması (1 saat)", "TYT Türkçe Branş Denemesi", "Fizik Soru Bankası 40 soru"],
    ["Paragraf 20 soru", "AYT Matematik Konu Soru Çalışması (1,5 saat)", "Kimya Soru Bankası 40 soru", "Problem 20 soru"],
    ["Paragraf 20 soru", "TYT Matematik Konu Soru Çalışması (1,5 saat)", "Biyoloji Konu Soru Çalışması (1 saat)", "Haftalık Tekrar (1 saat)"],
    ["TYT Genel Deneme (165 dk)", "Deneme Analizi (1 saat)", "Paragraf 20 soru"],
    ["AYT Genel Deneme (180 dk)", "Deneme Analizi (1 saat)", "Serbest Tekrar (1 saat)"]
  ];
  function hafta(bas, gecmisMi){
    var w = {};
    sablon.forEach(function(liste, i){
      var tarih = ekle(bas, i), gecti = tarih < t, bugunMu = tarih === t;
      w[i] = liste.map(function(m, j){ return g(m, gecmisMi ? (j < liste.length - (i % 3 === 0 ? 1 : 0)) : gecti ? j < liste.length - (i === dow - 1 ? 1 : 0) : bugunMu ? j < 1 : false, tarih); });
    });
    return w;
  }
  var gunluk = {};
  for (var i = 1; i <= 13; i++) { var d = ekle(t, -i); if (i % 6 !== 0) gunluk[d] = [210, 185, 240, 160, 275, 300, 195, 230, 150, 260, 205, 180, 240][i-1]; }
  function den(tur, tarih, a, b, c, dd){ return tur === "TYT"
    ? {id:id(), tur:"TYT", yayin:["3D","Özdebir","Hız ve Renk","Supara","Limit","345"][n % 6], tarih:tarih, turkce:{d:a,y:4}, sosyal:{d:b,y:2}, mat:{d:c,y:3}, fen:{d:dd,y:3}}
    : {id:id(), tur:"AYT", yayin:["3D","Özdebir","Limit"][n % 3], tarih:tarih, mat:{d:a,y:4}, fen:{d:b,y:5}}; }
  var denemeler = [
    den("TYT", ekle(t,-63), 28, 11, 16, 8), den("TYT", ekle(t,-49), 29, 12, 19, 9), den("TYT", ekle(t,-35), 30, 12, 18, 10),
    den("TYT", ekle(t,-21), 31, 13, 22, 11), den("TYT", ekle(t,-14), 32, 14, 24, 12), den("TYT", ekle(t,-4), 34, 15, 27, 13),
    den("AYT", ekle(t,-42), 14, 12), den("AYT", ekle(t,-20), 17, 15), den("AYT", ekle(t,-6), 21, 18)
  ];
  var topics = {};
  [["mat",["Temel Kavramlar","Rasyonel Sayılar","Sayı Basamakları","Bölme ve Bölünebilme","Basit Eşitsizlikler","Mutlak Değer"]],
   ["prob",["Sayı Problemleri","Kesir Problemleri","Yaş Problemleri"]],
   ["tr",["Sözcükte Anlam","Söz Yorumu","Deyimler ve Atasözleri","Cümlede Anlam"]],
   ["fiz",["Fizik Bilimine Giriş","Madde ve Özellikleri","Sıvıların Kaldırma Kuvveti","Basınç"]],
   ["kim",["Kimya Bilimi","Atom ve Yapısı","Periyodik Sistem"]],
   ["amat",["Polinomlar","Fonksiyonlar","2.Dereceden Denklemler"]],
   ["afiz",["Vektörler","Bağıl Hareket"]], ["akim",["Modern Atom Teorisi","Gazlar"]]
  ].forEach(function(x){ x[1].forEach(function(k, j){ topics[x[0] + "|" + k] = j < x[1].length - 1 ? {r:1, s1:1, s2: j % 2 ? 1 : 0, y: j % 3} : {r:1}; }); });
  var plan = {}; plan[pzt] = {saat:{0:5,1:5,2:5,3:5,4:5,5:7.5,6:7.5}, hedef:{
    "Matematik":{konu:"Mutlak Değer, Basit Eşitsizlikler", done:false}, "Fizik":{konu:"Basınç", done:false},
    "Kimya":{konu:"Periyodik Sistem", done:true}, "Biyoloji":{konu:"Hücre", done:false}, "Türkçe":{konu:"Cümlede Anlam", done:false}}};
  plan[gecen] = {saat:{0:5,1:5,2:5,3:5,4:5,5:7.5,6:7.5}, hedef:{"Matematik":{konu:"Bölme ve Bölünebilme", done:true}, "Fizik":{konu:"Sıvıların Kaldırma Kuvveti", done:true}}};
  var weeks = {}; weeks[gecen] = hafta(gecen, true); weeks[pzt] = hafta(pzt, false);
  var elif = {
    name:"Elif Demo", alan:"SAY", sinif:"12. sınıf", okul:"Demo Anadolu Lisesi", kullanici:"demo", createdAt:ekle(t,-70), paket:"super",
    baslangic:{tarih:ekle(t,-70), tyt:58, ayt:31, tytYok:false, aytYok:false}, hedef:{tarih:"", tyt:95, ayt:75},
    topics:topics, weeks:weeks, plan:plan, denemeler:denemeler, gunluk:gunluk, timer:null,
    kitaplar:{"Matematik":"Acil Matematik + 345", "Matematik|AYT":"Limit AYT Matematik", "Fizik":"Nihat Bilgin + 345", "Kimya":"Orbital", "Biyoloji":"Biyotik", "Türkçe":"Hız ve Renk Paragraf"},
    hocalar:{"Matematik":"Rehber Matematik", "Fizik":"Fizikle Barışalım", "Kimya":"Kimya Adası"},
    koctanNot:{text:"Elif, bu hafta paragraf rutinini hiç aksatma. Cumartesi denemesinden sonra analizini birlikte yapacağız 💪", date:ekle(t,-1)+"T18:00:00.000Z"},
    notSeen:"", lastSeen:ekle(t,-1), sonGiris:ekle(t,-1)+"T17:42:00.000Z", girisGun:{}, tanitim:true, yenilik:"2026-11-01", ilkSifre:false
  };
  [1,2,3,5,6,8,9,10].forEach(function(k){ elif.girisGun[ekle(t,-k)] = 1; });
  function basit(ad, u, tyt, gecikme){ var w = {}; w[pzt] = hafta(pzt, false); return {name:ad, alan:"EA", sinif:"Mezun", okul:"", kullanici:u, createdAt:ekle(t,-40), paket:"whatsapp",
    baslangic:{tarih:ekle(t,-40), tyt:tyt, ayt:null, tytYok:false, aytYok:true}, hedef:{tarih:"", tyt:tyt+25, ayt:null}, topics:{}, weeks:w, plan:{}, denemeler:[den("TYT", ekle(t,-10), 25, 10, 12, 6)], gunluk:{},
    timer:null, koctanNot:null, notSeen:"", lastSeen:ekle(t,-gecikme), tanitim:true, yenilik:"2026-11-01", ilkSifre:false}; }
  var db = {
    "settings/main": {kurum:"Zekacademy"},
    "students/demo1": elif,
    "students/demo2": basit("Mert Örnek", "mertornek", 44, 4),
    "students/demo3": basit("Zeynep Örnek", "zeynepornek", 51, 0),
    "coachNotes/demo1": {duzen:{gun:(dow+1)%7, saat:"19:00", sure:15, bas:gecen}, odeme:{bas:ekle(t,-70), tutar:6000, periyot:"ay", odenen:{}}, not:"Demo öğrenci. Hedef: Tıp."},
    "coachNotes/demo2": {odeme:{bas:ekle(t,-40), tutar:4000, periyot:"ay", odenen:{}}},
    "notifs/f_demo1": {type:"basvuru", at:new Date(Date.now()-3*3600e3).toISOString(), read:false, sessiz:false, deneme:true, name:"Örnek Başvuru", tel:"0555 000 00 00", alan:"Sayısal", hizmet:"Süper Koçluk Paketi -6000 TL/ay",
      cevaplar:[{s:"İsim-Soyisim", c:"Örnek Başvuru"}, {s:"İletişim Numaran", c:"0555 000 00 00"}, {s:"Hedefin Hangi Üniversite Hangi Bölüm?", c:"Hacettepe Tıp"}, {s:"Kaçıncı Sınıfsın?", c:"12.sınıf"}]}
  };
  db["coachNotes/demo1"].odeme.odenen[ekle(t,-70)] = {t:ekle(t,-70), tutar:6000};
  db["coachNotes/demo1"].odeme.odenen[ekle(t,-40)] = {t:ekle(t,-40), tutar:6000};
  db["coachNotes/demo1"].odeme.odenen[ekle(t,-10)] = {t:ekle(t,-10), tutar:6000};
  /* Çalışma grupları: birkaç örnek öğrenci şu an kronometre açık */
  var simdi = Date.now(), dk = 60000;
  var ornek = [["Ahmet Kaya","ahmetkaya","Kartal","fiz",38,190,"pc"],["Selin Yıldız","selinyildiz","Tıp2027","mat",72,385,"tel"],["Burak Demir","burakdemir","GeceKuşu","",0,120,""],["Ece Arslan","ecearslan","Papatya","kim",15,95,"tab"],["Can Öztürk","canozturk","Maraton","",0,0,""],["Defne Aydın","defneaydin","Yıldız","bio",54,160,"tel"],
    ["Kaan Şahin","kaansahin","Sessiz","tr",44,410,"pc"],["İrem Koç","iremkoc","Hedef1000","mat",9,60,"tel"],["Emre Yalçın","emreyalcin","Baykuş","",0,70,""]];
  var uyeler = ["demo1","demo2","demo3"];
  ornek.forEach(function(o, i){ var u = "dg"+(i+1), x = basit(o[0], o[1], 40+i*3, 0); x.takma = o[2]; x.sinif = i%2 ? "Mezun" : "12. sınıf";
    for(var j=1;j<=13;j++){ var dd = ekle(t,-j); x.gunluk[dd] = [180,210,150,240,200,170][ (i+j)%6 ] - i*10; }
    var ligPlan = [[5,320],[16,450],[0,0],[3,260],[0,0],[8,380],[0,0],[1,250],[0,0]][i];
    for(var j2=1;j2<=13;j2++){ var d2 = ekle(t,-j2); if(j2<=ligPlan[0]) x.gunluk[d2] = ligPlan[1] + (j2%3)*10; else if(ligPlan[0] && j2===ligPlan[0]+1) x.gunluk[d2] = 90; }
    if(o[5]) x.gunluk[t] = o[5]; if(o[4]) x.timer = {start: simdi - o[4]*dk, ders:o[3] || undefined, cihaz:o[6] || "tel"}; if(!o[3] && o[4]) delete x.timer.ders;
    x.avatar = [{cins:"e",ten:1,sac:"fade",sacR:0,giy:"kapus",gom:0,sakal:"hafif",kas:"kalin",aks:"kulaklik",ruh:"kararli",masaR:1,masaSol:"kitaplar",masaSag:"kahve",masaOn:"yks"},{cins:"k",ten:0,sac:"basortu",basR:1,giy:"forma",gom:0,kas:"kavis",ruh:"mutlu",masaR:2,masaSol:"lamba",masaSag:"bitki",masaOn:"postit",detay:"cil"},{cins:"e",ten:3,sac:"kivircik",sacR:0,giy:"tisort",gom:7,sakal:"keci",ruh:"odakli",masaR:4,masaSag:"su"},{cins:"k",ten:2,sac:"sal",basR:4,giy:"kazak",gom:4,aks:"gozluk",ruh:"heyecanli",masaR:3,masaSol:"kalemlik",masaSag:"saat",masaOn:"yildiz"},{cins:"e",ten:1,sac:"yan",sacR:1,giy:"gomlek",gom:5,sakal:"biyik",ruh:"odakli",masaR:0,masaSol:"kitaplar",masaSag:"su",detay:"ben"},{cins:"k",ten:4,sac:"orgu",sacR:0,giy:"kazak",gom:2,kas:"kavis",ruh:"mutlu",masaR:5,masaSol:"lamba",masaSag:"kahve",masaOn:"postit"},{cins:"e",ten:0,sac:"kisa",sacR:2,giy:"gomlek",gom:8,aks:"yuvarlak",kas:"duz",ruh:"kararli",masaR:1,masaSol:"kalemlik",masaSag:"saat",masaOn:"yks"},{cins:"k",ten:2,sac:"basortu",basR:2,giy:"kapus",gom:3,goz:"badem",ruh:"odakli",masaR:2,masaSag:"bitki"},{cins:"e",ten:1,sac:"kel",sacR:5,giy:"kapus",gom:7,sakal:"sakal",ruh:"yorgun",masaR:4,masaSag:"kahve"}][i];
    db["students/"+u] = x; uyeler.push(u); });

  elif.takma = "Elif2027";
  db["students/demo2"].takma = "Mert"; db["students/demo2"].avatar = {cins:"e", ten:2, sac:"dalga", sacR:1, giy:"kazak", gom:6, kas:"kalin"}; db["students/demo2"].gunluk[t] = 75; db["students/demo2"].timer = {start: simdi - 21*dk, ders:"geo", cihaz:"pc"};
  db["students/demo3"].takma = "Zeyno"; db["students/demo3"].gunluk[t] = 450;
  db["gruplar/g1"] = {ad:"Hedef Tıp 2027", uyeler:["dg1","dg2","demo2","dg4","demo1","dg6","dg7","dg8","dg9"], at:simdi};
  db["gruplar/g2"] = {ad:"Mezunlar", uyeler:["demo3","dg3","dg5"], at:simdi};
  /* Öğrencilerin gruplardaki canlı özetleri (gerçekte her öğrencinin uygulaması kendisi yazar) */
  function canli(x){ var c = canli0(x); c.avatar = x.avatar || null; if(!c.avatar) delete c.avatar; return c; }
  function canli0(x){ var w = {}; Object.keys(x.gunluk).forEach(function(d){ if(d >= ekle(t,-13) && d < t) w[d] = x.gunluk[d]; }); return {takma:x.takma||"", basla:x.timer ? x.timer.start : null, ders:(x.timer && x.timer.ders) || "", cihaz:(x.timer && x.timer.cihaz) || "", gun:t, bugunDk:x.gunluk[t]||0, gunler:w, at:simdi}; }
  ["g1","g2"].forEach(function(g){ db["gruplar/"+g].uyeler.forEach(function(u){ if(u!=="demo1") db["gruplar/"+g+"/canli/"+u] = canli(db["students/"+u]); }); });
  localStorage.setItem("mockDb", JSON.stringify(db));
  localStorage.setItem("mockUsers", JSON.stringify({"zekacademy@app.zekacademy.com":{uid:"coach1", p:"demo1234"}, "demo@app.zekacademy.com":{uid:"demo1", p:"123456"},
    "mertornek@app.zekacademy.com":{uid:"demo2", p:"123456"}, "zeynepornek@app.zekacademy.com":{uid:"demo3", p:"123456"}}));
  localStorage.removeItem("mockUser");
  localStorage.setItem("zk-demo-v", "10");
})();
document.addEventListener("DOMContentLoaded", function(){
  var b = document.createElement("div");
  b.innerHTML = 'DEMO · gerçek veri değil · <a href="/?demo=0" style="color:inherit;text-decoration:underline">çık</a> · <a href="#" id="demoSifirla" style="color:inherit;text-decoration:underline">sıfırla</a>';
  b.style.cssText = "position:fixed;bottom:calc(env(safe-area-inset-bottom,0px) + 96px);left:50%;transform:translateX(-50%);z-index:99;background:#F59E0B;color:#1F1300;font:700 11px/1 system-ui,sans-serif;padding:5px 10px;border-radius:99px;box-shadow:0 2px 8px rgba(0,0,0,.15);white-space:nowrap";
  document.body.appendChild(b);
  document.getElementById("demoSifirla").onclick = function(e){ e.preventDefault(); ["mockDb","mockUsers","mockUser","zk-demo-v"].forEach(function(k){ localStorage.removeItem(k); }); location.reload(); };
});
