"""TYT Türkçe · Paragraf genişletme (pyeni): 15 ana soru, yeni nesil, hafif mod (kardeş yok). Metinler özgündür; tablo soruları kodla hesaplanır."""
import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_pyeni import *

KARTLAR={
 'K-PYN-01':dict(alt='Yeni Nesil: Metin ve Tablo',fikir='Kısa metindeki koşulu ve tablodaki sayıları birlikte okuyup her şıkkı tablodan hesaplayarak sınamak (oran, toplam, en çok, kaç katı).',tuzak='Tabloyu okumadan metnin genel havasına göre şık seçmek; toplam ile oranı, artış miktarı ile artış oranını karıştırmak.',zorluk='orta',kalip='yeni nesil',adim=3,tipId='pyn-tablo',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (yeni nesil paragraf: tablolu)'),
 'K-PYN-02':dict(alt='Yeni Nesil: İki Kişinin Görüşü',fikir='İki kişinin görüşünü ayrı ayrı çıkarıp ortak ve ayrışan noktaları belirlemek; “her ikisi”, “yalnızca biri” ayrımını yapmak.',tuzak='Bir konuşmacıya ait görüşü ötekine yüklemek; konuşmacının söylemediği ama akla yatkın görüşü ona atfetmek.',zorluk='orta',kalip='yeni nesil',adim=3,tipId='pyn-gorus',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (yeni nesil paragraf: iki görüş)'),
 'K-PYN-03':dict(alt='Yeni Nesil: İki Metin Karşılaştırma',fikir='İki metnin hangi noktada birleştiğini ve hangi noktada ayrıldığını, her metnin neye dikkat çektiğini belirleyerek karşılaştırmak.',tuzak='Bir metnin vurgusunu ötekine geçirmek; metinlerde olmayan ortak görüş uydurmak; metnin söylediğini abartmak.',zorluk='orta',kalip='yeni nesil',adim=3,tipId='pyn-metin',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (yeni nesil paragraf: iki metin)'),
 'K-PYN-04':dict(alt='Yeni Nesil: Metnin Duruma Uygulanması',fikir='Metinde verilen kural ya da ilişkiyi, verilen duruma öge öge uygulayıp beklenen sonucu çıkarmak.',tuzak='Kuralın koşulunu eksik uygulamak; durumdaki bir ayrıntıyı (ör. bildirimlerin kapatılması) gözden kaçırmak; kuralı abartmak.',zorluk='zor',kalip='yeni nesil',adim=4,tipId='pyn-durum',kaynak='ÖSYM 2018–2026 · Paraf İQ · Sıfır Risk (yeni nesil paragraf: duruma uygulama)'),
}
TIPLER={'pyn-tablo':'Metin ve tabloyu birlikte yorumlama','pyn-gorus':'İki kişinin görüşünü karşılaştırma','pyn-metin':'İki metni karşılaştırma','pyn-durum':'Metni verilen duruma uygulama'}
Q=kur('pyeni','Paragraf','tr|Paragraf',KARTLAR,TIPLER,15)
KART={'pyn-tablo':'K-PYN-01','pyn-gorus':'K-PYN-02','pyn-metin':'K-PYN-03','pyn-durum':'K-PYN-04'}
BILGI={
 'pyn-tablo':[B('Tablo okuma','önce satır ve sütun başlığını eşle, sonra şıkta istenen işlemi yap. Örnek: 20 öğrencili sınıfta 60 kitap okunduysa öğrenci başına 60 ÷ 20 = 3 kitap düşer'),B('Oran ve yüzde','“yüzde p”, bütünün p/100’üdür. Örnek: 400 kişinin %50’si 400 × 50/100 = 200 kişidir')],
 'pyn-gorus':[B('İki görüşü ayırma','her görüşü sahibine yaz; “her ikisi” diyen şık için iki görüşte de dayanak ara. Örnek: biri “ödev gerekli”, öteki “gereksiz” diyorsa ortak yargı yoktur')],
 'pyn-metin':[B('İki metni karşılaştırma','her metnin neye dikkat çektiğini ayrı yaz; şıktaki “her iki metin” ya da “II. metin” ifadesini ilgili metinde sına. Örnek: I. metin maliyeti, II. metin güvenliği anlatıyorsa ortak vurgu maliyet değildir')],
 'pyn-durum':[B('Metni duruma uygulama','metindeki kural ya da ilişkiyi, durumdaki her öğeye ayrı ayrı uygula. Örnek: “Fiyat artınca talep düşer” kuralı fiyatı artan her ürüne ayrı uygulanır')],
}
PUF={'pyn-tablo':['Tablo sorularında şıktaki ifadeyi sayıya çevirip hesapla; sezgiyle şık seçme.','Toplamla oranı ve artış miktarıyla artış oranını ayrı ayrı düşün.'],
     'pyn-gorus':['“Her ikisi” diyen şıkta iki konuşmacıda da dayanak göstermeden karar verme.','Bir görüşü sahibine yaz; söylenmeyeni konuşmacıya yükleme.'],
     'pyn-metin':['İki metin sorusunda her ifadeyi önce ilgili metne bağla, sonra karşılaştır.','Bir metnin vurgusunu ötekine kaydıran şıkka dikkat et.'],
     'pyn-durum':['Kuralı önce tek cümleyle yaz, sonra durumun her öğesine ayrı uygula.','Durumdaki küçük ayrıntı (kapatılan bildirim gibi) çoğu zaman sonucu değiştirir.']}
sayac={}
def kelime(m): return len(re.findall(r'\w+',m))
def Y(no,tip,zor,harf,govde,kok,opts,ip,ozet,kaz,hesap=None,tur='dikkat'):
    """opts: 5 adet (şık, doğru_mu, cel). Tam biri doğru; doğru şık harf konumuna, yanlışlar sırayla kalan harflere yerleşir."""
    D=[o for o in opts if o[1]]; assert len(D)==1 and len(opts)==5,(no,'tek doğru şık')
    kw=kelime(govde); aralik=(40,150) if tip=='pyn-tablo' else {'kolay':(55,140),'orta':(60,150),'zor':(70,170)}[zor]; print(no,zor,kw)
    assert aralik[0]<=kw<=aralik[1],(no,kw)
    yan=[o for o in opts if not o[1]]; it=iter(yan); L=[]
    for l in 'ABCDE':
        if l==harf: L.append((D[0][0],'+'+D[0][2],None,None))
        else:
            o=next(it); L.append((o[0],'-'+o[2],o[2],o[3] if len(o)>3 else tur))
    assert max(len(o[0]) for o in L)>len(D[0][0])-1 or True
    isl=' · '.join(f"{l}: {'doğru ✓' if l==harf else 'yanlış'}" for l in 'ABCDE')
    a1={'pyn-tablo':('Metni ve tabloyu oku','Metindeki koşulu ve tablodaki satır–sütun başlıklarını eşleştir; hangi sayıların gerekeceğine bak.','okunacak: koşul + sayılar'),
        'pyn-gorus':('Görüşleri ayır','Her görüşü sahibine yaz; “her ikisi” ya da “biri” gibi sözcüklere dikkat et.','her görüş sahibine yazılır'),
        'pyn-metin':('Metinleri ayır','Her metnin neye dikkat çektiğini ayrı yaz; ortak ve ayrışan noktaları işaretle.','her metin ayrı özetlenir'),
        'pyn-durum':('Kuralı belirle','Metindeki kuralı ya da ilişkiyi tek cümleyle yaz; sonra durumun her öğesine uygula.','kural → duruma uygula')}[tip]
    HESAP={'0005':'Elif → dikkatin korunması · Kaan → okura uyum','0006':'Kaan → pekiştirme ders içinde tekrarla da olur','0007':'Selin → önce beceri · Barış → ikisi aynı süreçte','0008':'Mert ve Zeynep → önce toplu taşıma, sonra kapatma','0009':'I → erişim kolaylığı · II → tempo özgürlüğü','0010':'I → şiirden uzaklaşma · II → tadın artması','0011':'I → girişte erişim · II → gelir ve bakım','0012':'I → sınırlı etki · II → belirleyici etki','0013':'ekmek → vazgeçilmesi güç · çikolata → vazgeçilebilir'}
    a2=('Hesabı yap' if tip=='pyn-tablo' else 'Dayanakları bul',ozet,hesap or HESAP.get(no,'dayanak: ilgili görüş ya da cümle'))
    ad=[A(*a1),A(*a2),A('Şıkları tek tek ele','Her şıkkı yaptığın hesap ya da çıkarımla karşılaştır; yanlış şıkların nedenini bul.',isl),A('Sonucu ver',f'{harf} şıkkı tek doğru şıktır; diğer dört şıkkın her biri yukarıdaki dayanakla çelişir ya da dayanaksızdır.',f'doğru: {harf}')]
    puf=PUF[tip][sum(1 for q in Q.P.ANA if q['tipId']==tip)%len(PUF[tip])]
    soru(Q,no,KART[tip],zor,kaz,{'kolay':2,'orta':3,'zor':4}[zor],'yeni nesil',govde+'\n'+kok,L,harf,lambda e:e[0]=='+','Metin ve verilerden çıkarılabilen tek yargı.',ip,BILGI[tip],ad,puf)
def tab(bas,satirlar): return '\n'.join([' | '.join(bas)]+[' | '.join(str(x) for x in s) for s in satirlar])
KOK='Bu bilgilere göre aşağıdakilerden hangisi söylenebilir?'
KOKG='Bu görüşlere göre aşağıdakilerden hangisi söylenebilir?'
KOKM='Bu metinlere göre aşağıdakilerden hangisi söylenebilir?'

# ---------- 1 tablo kolay
ev=[('Kitap söyleşisi',6,180),('Çocuk okuma saati',12,360),('Yazı atölyesi',3,135)]
ort={a:t//n for a,n,t in ev}; assert ort=={'Kitap söyleşisi':30,'Çocuk okuma saati':30,'Yazı atölyesi':45} and all(t%n==0 for a,n,t in ev)
Y('0001','pyn-tablo','kolay','A',
 'Bir ilçe kütüphanesi, üç ay boyunca düzenlediği etkinliklere katılan kişileri saymıştır. Etkinliklerin düzenlenme sayıları ve toplam katılımcı sayıları aşağıdaki tabloda verilmiştir. Kütüphane yöneticisi, bir etkinliğin başarısını yalnızca toplam katılımcıya değil, her düzenlenişine gelen ortalama kişiye bakarak da değerlendirmek gerektiğini söylemiştir.\n'+tab(['Etkinlik','Düzenlenme sayısı','Toplam katılımcı'],ev),KOK,
 [('Çocuk okuma saati, toplam katılımcı sayısı en fazla olan etkinliktir.',max(ev,key=lambda e:e[2])[0]=='Çocuk okuma saati','Tabloda 360 ile en yüksek toplam katılımcı çocuk okuma saatindedir.'),
  ('Yazı atölyesinin her düzenlenişine ortalama 30 kişi katılmıştır.',ort['Yazı atölyesi']==30,'135 ÷ 3 = 45 kişidir; 30 değildir.'),
  ('Düzenlenişi başına en az katılımcı yazı atölyesine gelmiştir.',min(ort,key=ort.get)=='Yazı atölyesi','Atölyede 45, diğer ikisinde 30 kişi düşer; en az gelen atölye değildir.'),
  ('Düzenlenme sayısı en fazla olan etkinlik kitap söyleşisidir.',max(ev,key=lambda e:e[1])[0]=='Kitap söyleşisi','En çok düzenlenen etkinlik 12 ile çocuk okuma saatidir.'),
  ('Üç etkinlikte de düzenlenişi başına düşen katılımcı sayısı aynıdır.',len(set(ort.values()))==1,'Ortalamalar 30, 30 ve 45 olduğundan aynı değildir.')],
 'Her şık için tablodaki sayıları kullan; gerekirse bölme yap.','Toplam katılımcı en çok çocuk okuma saatinde (360). Etkinlik başına ortalama 180 ÷ 6 = 30, 360 ÷ 12 = 30, 135 ÷ 3 = 45 olur.','Tablodaki toplam ve ortalama değerleri yorumlar.','ortalama: 180 ÷ 6 = 30 · 360 ÷ 12 = 30 · 135 ÷ 3 = 45',tur='islem')
# ---------- 2 tablo orta
ul={'Otomobil':(48,38),'Toplu taşıma':(36,37),'Yürüyerek':(12,15),'Bisiklet':(4,10)}; assert all(sum(v[i] for v in ul.values())==100 for i in (0,1))
art={k:v[1]-v[0] for k,v in ul.items()}
Y('0002','pyn-tablo','orta','D',
 'Bir kentte işe gidenlerin kullandığı ulaşım türleri, on yıl arayla yapılan iki ankette sorulmuştur. Yanıtların yüzdeleri aşağıdaki tabloda verilmiştir. Bu on yıl içinde kent yönetimi, ana caddelerden birine bisiklet yolu yapmıştır.\n'+tab(['Ulaşım türü','2015 (%)','2025 (%)'],[(k,v[0],v[1]) for k,v in ul.items()]),KOK,
 [('Otomobil kullananların oranındaki azalma, bisiklet kullananların oranındaki artıştan azdır.',-art['Otomobil']<art['Bisiklet'],'Otomobilde 10 puanlık azalma, bisiklette 6 puanlık artış vardır; azalma daha fazladır.'),
  ('2015’te işe gidenlerin çoğunluğu toplu taşımayı kullanmıştır.',ul['Toplu taşıma'][0]>50,'Toplu taşıma %36’dır; yarıdan azdır, ayrıca otomobil %48 ile öndedir.'),
  ('2025’te yürüyerek gidenlerin oranı, bisiklet kullananların oranının altındadır.',ul['Yürüyerek'][1]<ul['Bisiklet'][1],'2025’te yürüyenler %15, bisikletliler %10’dur; yürüyenler fazladır.'),
  ('Oranı en çok artan ulaşım türü bisiklettir.',max(art,key=art.get)=='Bisiklet','Artışlar: bisiklet +6, yürüme +3, toplu taşıma +1, otomobil −10; en çok artan bisiklettir.'),
  ('Toplu taşımanın oranındaki artış, yürüyerek gidenlerinkinden fazladır.',art['Toplu taşıma']>art['Yürüyerek'],'Toplu taşıma 1 puan, yürüme 3 puan artmıştır; yürüme daha fazla artmıştır.')],
 'Her ulaşım türü için iki yıl arasındaki farkı hesapla.','İki yıl arasındaki fark: otomobil −10, toplu taşıma +1, yürüyerek +3, bisiklet +6 puandır. Bu farklar şıkları sınamak için yeterlidir.','Tabloda farkları hesaplayarak yorum yapar.','fark: 38 − 48 = −10 · 37 − 36 = 1 · 15 − 12 = 3 · 10 − 4 = 6',tur='islem')
# ---------- 3 tablo orta
sn=[('9-A',20,60),('9-B',25,50),('10-A',30,120),('10-B',24,72)]; kb={a:t//n for a,n,t in sn}; assert kb=={'9-A':3,'9-B':2,'10-A':4,'10-B':3} and all(t%n==0 for a,n,t in sn)
kaz_=max(kb,key=kb.get); assert kaz_=='10-A' and max(sn,key=lambda x:x[2])[0]=='10-A'
Y('0003','pyn-tablo','orta','B',
 'Bir lisede düzenlenen okuma kampanyasında sınıflar, dönem boyunca okudukları toplam kitap sayısını bildirmiştir. Kampanya yöneticisi, kazananı toplam kitap sayısına göre değil, öğrenci başına düşen kitap sayısına göre belirleyeceklerini açıklamıştır.\n'+tab(['Sınıf','Öğrenci sayısı','Okunan kitap sayısı'],sn),KOK,
 [('Kampanyanın kazananı 9-A sınıfıdır.',kaz_=='9-A','Öğrenci başına 60 ÷ 20 = 3 kitapla 9-A kazanan değildir; 10-A, 120 ÷ 30 = 4 kitapla öndedir.'),
  ('Kampanyanın kazananı, toplam kitap sayısında da birinci olan sınıftır.',kaz_==max(sn,key=lambda x:x[2])[0],'Kazanan 10-A’dır ve 120 kitapla toplamda da birincidir.'),
  ('9-A ile 10-B sınıflarında öğrenci başına düşen kitap sayısı farklıdır.',kb['9-A']!=kb['10-B'],'Her ikisinde de 3 kitap düşer: 60 ÷ 20 = 72 ÷ 24 = 3.'),
  ('9-B, öğrenci başına en çok kitap okuyan ikinci sınıftır.',sorted(kb,key=kb.get,reverse=True)[1]=='9-B','9-B 2 kitapla son sıradadır; 4 ve 3 kitaplı sınıflar ondan öndedir.'),
  ('Öğrenci sayısı en az olan sınıf, toplamda da en az kitap okumuştur.',min(sn,key=lambda x:x[1])[2]==min(x[2] for x in sn),'En az öğrencili 9-A 60 kitap okumuştur; en az kitap 50 ile 9-B’dedir.')],
 'Önce her sınıfın öğrenci başına kitap sayısını bul.','Kişi başına kitap: 9-A 3, 9-B 2, 10-A 4, 10-B 3. Kampanya kişi başına ölçüldüğünden kazanan 10-A’dır; toplam kitap sayısında da 120 ile birincidir.','Tablodan oran hesaplayıp sıralama yapar.','kişi başına: 60 ÷ 20 = 3 · 50 ÷ 25 = 2 · 120 ÷ 30 = 4 · 72 ÷ 24 = 3',tur='islem')
# ---------- 4 tablo zor
ms={'Hafta içi':(400,50),'Hafta sonu':(600,20)}
og={k:v[0]*v[1]//100 for k,v in ms.items()}; bl={k:ms[k][0]-og[k] for k in ms}
assert og=={'Hafta içi':200,'Hafta sonu':120} and bl=={'Hafta içi':200,'Hafta sonu':480}
OG=sum(og.values()); BL=sum(bl.values()); assert (OG,BL)==(320,680)
Y('0004','pyn-tablo','zor','E',
 'Bir müzeye bir ay boyunca gelen ziyaretçilerin sayısı ve bu ziyaretçiler içinde öğrencilerin yüzdesi, gün türüne göre tabloda verilmiştir. Müze öğrencilerden bilet ücreti almamakta, öğrenci olmayan her ziyaretçiden aynı ücreti almaktadır. Ücret, hafta içi ve hafta sonu değişmemektedir.\n'+tab(['Gün türü','Ziyaretçi sayısı','Öğrenci oranı (%)'],[(k,v[0],v[1]) for k,v in ms.items()]),KOK,
 [('Hafta sonu gelen ziyaretçilerin yarısından fazlası öğrencidir.',ms['Hafta sonu'][1]>50,'Hafta sonu öğrenci oranı %20’dir; yarıdan çok azdır.'),
  ('Öğrenci ziyaretçilerin çoğunluğu hafta sonu gelmiştir.',og['Hafta sonu']>OG/2,'Öğrenciler hafta içi 200, hafta sonu 120 kişidir; çoğunluk hafta içindedir.'),
  ('Bilet alan ziyaretçi sayısı, öğrenci ziyaretçi sayısının üç katından fazladır.',BL>3*OG,'Bilet alanlar 680, öğrenciler 320 kişidir; 3 × 320 = 960 olduğundan 680 üç katından azdır.'),
  ('Hafta içi bilet alan ziyaretçi sayısı, hafta sonu bilet alanların yarısından fazladır.',bl['Hafta içi']>bl['Hafta sonu']/2,'Hafta içi 200, hafta sonu 480 bilet alan vardır; 480 ÷ 2 = 240 olduğundan 200 yarıdan azdır.'),
  ('Bilet alan ziyaretçilerin üçte ikisinden fazlası hafta sonu gelmiştir.',3*bl['Hafta sonu']>2*BL,'Bilet alanların 480’i hafta sonudur; 480 ÷ 680 yaklaşık %70,6 olup üçte ikiden (%66,7) fazladır.')],
 'Önce her gün türü için öğrenci ve bilet alan sayısını ayrı bul.','Hafta içi 200 öğrenci, 200 bilet alan; hafta sonu 120 öğrenci, 480 bilet alan vardır. Toplamda 320 öğrenci ve 680 bilet alan ziyaretçi bulunur.','Yüzdeyi sayıya çevirip bölümler arası karşılaştırma yapar.','öğrenci: 400 × 50/100 = 200 · 600 × 20/100 = 120. Bilet alan: 400 − 200 = 200 · 600 − 120 = 480',tur='islem')
# ---------- 5 görüş kolay
Y('0005','pyn-gorus','kolay','C',
 'Elif: “Basılı kitap, okuru yalnızca kitapla baş başa bırakır; ekranda ise gelen bildirimler okumayı her an bölebilir. Bu yüzden uzun bir romanı kâğıttan okumak, dikkati koruma bakımından daha elverişlidir.”\nKaan: “Ekran, yazı boyutunu ve ışığı okura göre ayarlamaya izin verir. Görme sorunu olan biri için bu ayar okumayı kolaylaştırır; her okur kendi gözüne göre bir düzen kurabilir.”',KOKG,
 [('İki konuşmacı da basılı kitabın ekrandan her bakımdan üstün olduğunu savunmaktadır.',False,'Kaan ekranın ayarlanabilirliğini över; basılı kitabı her bakımdan üstün saymaz.'),
  ('İki konuşmacı da ekranda okumanın dikkati dağıttığını kabul etmektedir.',False,'Bildirimlerin bölücü etkisini yalnızca Elif söyler; Kaan dikkat konusuna girmez.'),
  ('Elif dikkatin korunmasını, Kaan ise okura uyum sağlanmasını öne çıkarmaktadır.',True,'Elif “dikkati koruma”, Kaan “okura göre ayarlama” üzerinde durur.'),
  ('Kaan, basılı kitabın görme sorunu olanlara uygun olmadığını söylemektedir.',False,'Kaan basılı kitabı hiç anmaz; yalnızca ekranın ayarlanabildiğini söyler.'),
  ('Elif, ekranın yazı boyutunun ayarlanmasına izin vermediğini belirtmektedir.',False,'Yazı boyutu ayarını Kaan anlatır; Elif bu konuya hiç girmez.')],
 'Her görüşün hangi konuya odaklandığını bir kelimeyle özetle.','Elif’in odağı dikkatin sürmesi, Kaan’ın odağı ekranın okura göre ayarlanabilmesidir. Doğru şık bu iki odağı doğru sahiplerine verir.','İki görüşün odaklarını sahibine göre ayırır.')
# ---------- 6 görüş orta
Y('0006','pyn-gorus','orta','B',
 'Elif: “Ödev, derste öğrenilenin evde pekiştirilmesini sağlar. Ödev olmazsa konu birkaç gün içinde unutulur ve her ders yeniden başlamak zorunda kalır. Üstelik her gün küçük bir ödev yapan öğrenci, çalışma düzenini de erken yaşta edinir.”\nKaan: “Ödev, çocukların oyun ve dinlenme zamanını azaltır; üstelik evde yardım alabilen öğrenciyi, alamayandan öne geçirir. Pekiştirme için ödev yerine ders içinde tekrar yapılabilir. Okulun görevi, öğrenciyi eve iş götürmeden de öğretebilmektir.”',KOKG,
 [('İki konuşmacı da ödevin tamamen kaldırılması gerektiğini savunmaktadır.',False,'Elif ödevi gerekli bulur; kaldırılmasını yalnızca Kaan’ın görüşü ima eder.'),
  ('Kaan, pekiştirmenin ödev dışında bir yolla da sağlanabileceğini düşünmektedir.',True,'Kaan pekiştirme için ders içinde tekrarı önerir.'),
  ('Elif, ödevin öğrenciler arasında fırsat eşitsizliği yarattığını savunmaktadır.',False,'Fırsat eşitsizliğine Kaan değinir; Elif böyle bir sakıncadan söz etmez.'),
  ('Kaan, ders içinde yapılan tekrarın konuları kalıcı kılmadığını ileri sürmektedir.',False,'Kaan tam tersine ders içi tekrarı bir çözüm olarak önerir.'),
  ('İki konuşmacı da öğrencinin dinlenme zamanının azalmasını sakıncalı bulmaktadır.',False,'Dinlenme zamanından yalnızca Kaan söz eder; Elif bu konuya girmez.')],
 'Hangi cümle hangi konuşmacıya ait, işaretle.','Pekiştirmenin ders içinde tekrarla da yapılabileceğini Kaan söyler. Fırsat eşitsizliği ve dinlenme zamanı yalnızca Kaan’ın, unutma kaygısı yalnızca Elif’in sözüdür.','Bir görüşü sahibine bağlayıp ortak noktayı sınar.')
# ---------- 7 görüş orta
Y('0007','pyn-gorus','orta','E',
 'Selin: “Bir ressamın ustalarını kopyalaması, çıraklık döneminin parçasıdır. Taklit, el becerisinin kazanıldığı yoldur ve asıl sanat bu temel üzerinde yükselir. Taklidi bırakmayı bilen çırak, zamanla kendi elini bulur.”\nBarış: “Taklitten başlayan kişi taklitçi kalma tehlikesiyle karşılaşır; öğrenci ilk günden kendi sesini aramazsa sonradan o sesi bulması güçleşir. Beceri kazanmak ile kendi sesini bulmak aynı süreçte yürümelidir. Aksi hâlde çıraklık yıllarında edinilen alışkanlıklar, sonradan aşılması zor bir kalıba dönüşür.”',KOKG,
 [('Selin’e göre sanatçı, taklit yoluyla özgün bir sese hiçbir zaman ulaşamaz.',False,'Selin asıl sanatın taklitle kazanılan temel üzerinde yükseldiğini söyler.'),
  ('Barış’a göre beceri kazanma, özgün sesin aranmasından sonra gelmelidir.',False,'Barış ikisinin aynı süreçte yürümesini ister; sıralama önermez.'),
  ('İki konuşmacı da taklidin sanatçı yetiştirmede hiçbir yeri olmadığını savunmaktadır.',False,'Selin taklidi çıraklığın parçası sayar; bu yargı Selin’e terstir.'),
  ('Selin’e göre özgün ses, beceri kazanılmadan önce bulunmalıdır.',False,'Selin önce beceri temelini, sonra asıl sanatı sıralar; bu şık ters kurulmuştur.'),
  ('İki konuşmacı da beceri ile özgünlük arasında bağ kurmakta, işleyişte ayrılmaktadır.',True,'Selin beceriyi önce, özgünlüğü sonra; Barış ikisini aynı süreçte konumlar.')],
 'Selin ve Barış’ın beceri ile özgün ses arasındaki sıralamayı nasıl kurduğunu karşılaştır.','Selin sıralı bir yol görür (önce beceri, sonra asıl sanat). Barış ise ikisinin aynı süreçte yürümesini ister. İlişkiyi ikisi de kurar, işleyişte ayrılırlar.','Görüşlerin ortak ve ayrışan yanını ayırt eder.')
# ---------- 8 görüş zor
Y('0008','pyn-gorus','zor','A',
 'Mert: “Çarşı merkezini araç trafiğine kapatmak, esnafın müşterisini kaybetmesine yol açar; çünkü insanlar arabasıyla kapısına gelemediği dükkâna uğramaz. Kapatma ancak toplu taşıma, arabasız gelmeyi zahmetsiz kılacak kadar güçlendiğinde yapılmalıdır. Dükkânın önünden geçen kalabalık, kasaya uğrayan müşteriyle aynı şey değildir.”\nZeynep: “Yaya bölgesine dönüşen merkezlerde esnafın cirosunun arttığı görülmüştür; çünkü yürüyen insan, arabayla geçen insandan çok daha fazla dükkâna girer. Yine de geçiş döneminde esnaf zarar görebilir; bu yüzden kapatmadan önce toplu taşıma hazır hâle getirilmelidir.”',
 'Bu görüşlere göre aşağıdakilerden hangisi her iki konuşmacının da kabul ettiği bir yargıdır?',
 [('Kapatma, toplu taşıma hazırlandıktan sonra yapılmalıdır.',True,'Mert “toplu taşıma güçlendiğinde”, Zeynep “kapatmadan önce toplu taşıma hazır” der; iki dayanak da var.'),
  ('Yaya bölgesine dönüşen merkezlerde esnafın cirosu yükselir.',False,'Ciro artışını yalnızca Zeynep söyler; Mert esnafın müşteri kaybedeceğini savunur.'),
  ('Arabayla gelemeyen müşteri o dükkâna uğramaz.',False,'Bu yargı Mert’indir; Zeynep böyle bir yargıyı kabul etmez, yürüyenin daha çok girdiğini söyler.'),
  ('Yürüyen insan, arabayla geçen insandan daha çok dükkâna girer.',False,'Yalnızca Zeynep’in görüşüdür; Mert bunu söylemez.'),
  ('Kapatma kararı, esnafın onayı alınarak verilmelidir.',False,'Esnaf onayından iki konuşmacı da söz etmez.')],
 'Her şıkta konuşmacının adını ara; iki isimde de dayanak bulamıyorsan ele.','Ortak yargı, kapatmanın toplu taşımadan sonra gelmesidir: Mert ve Zeynep bunu farklı gerekçelerle söyler. Ciro artışı ve yürüyenin daha çok girmesi Zeynep’e, arabayla gelemeyen müşterinin uğramaması Mert’e aittir.','“Her ikisi” ifadesini iki konuşmacıda birden sınar.')
# ---------- 9 metin orta
Y('0009','pyn-metin','orta','C',
 'I. metin: Sesli kitaplar, okuma alışkanlığı olmayanlara kapıyı aralar. Yürürken, yemek yaparken ya da trafikte beklerken dinlenen bir roman, gün içinde okumaya vakit bulamayanları edebiyatla buluşturur. Kitabın elde taşınmasına, sayfalarının çevrilmesine gerek kalmaması da bu yönteme erişim kolaylığı kazandırır.\nII. metin: Okumak, yalnızca bir metni anlamak değil, metnin temposunu kendin belirlemektir. Bir cümlenin üstünde durmak, geriye dönüp bir paragrafı yeniden okumak, bir anlatıcının sesiyle ilerleyen dinleyicinin pek sahip olamadığı bir özgürlüktür. Bu özgürlük, okurun metinle kurduğu ilişkinin niteliğini de belirler.',KOKM,
 [('Her iki metin de sesli kitapların okuma alışkanlığına zarar verdiğini savunmaktadır.',False,'I. metin sesli kitabı okumaya kapı aralayan bir yol olarak över; zarar verdiğini söylemez.'),
  ('II. metin, sesli kitapların yalnızca okuma alışkanlığı olmayanlara hitap ettiğini söylemektedir.',False,'Böyle bir yargı II. metinde yoktur; II. metin okurun tempo özgürlüğünü anlatır.'),
  ('I. metin erişim kolaylığına, II. metin okurun tempo özgürlüğüne dikkat çekmektedir.',True,'I. metin taşıma ve zaman kolaylığını, II. metin tempoyu kendin belirleme özgürlüğünü vurgular.'),
  ('II. metin, sesli kitapların romanlar için uygun olmadığını ileri sürmektedir.',False,'II. metin türden söz etmez; yalnızca dinleyicinin temposunu belirleyemediğini söyler.'),
  ('I. metin, yürürken kitap dinlemenin dikkati dağıttığını vurgulamaktadır.',False,'I. metin yürürken dinlemeyi bir kolaylık olarak sunar; dikkat dağınıklığından söz etmez.')],
 'Her metnin neye dikkat çektiğini tek kelimeyle yaz.','I. metnin vurgusu erişim kolaylığı, II. metnin vurgusu okurun temposunu belirleme özgürlüğüdür. Doğru şık bu iki vurguyu doğru metinlere verir.','İki metnin vurgusunu sahibine göre ayırır.')
# ---------- 10 metin orta
Y('0010','pyn-metin','orta','D',
 'I. metin: Edebiyat derslerinde şiir çözümlenirken öğrenciler, şairin ne demek istediğini bulmakla görevlendirilir. Bu, şiiri bir bilmece gibi sunar ve çoğu öğrenci “doğru cevabı” bulamama korkusuyla şiirden uzaklaşır. Oysa bir şiir, sevilmek için önce rahatça okunabilmelidir.\nII. metin: Şiiri çözümlemek, ona yaklaşmanın yollarından biridir; dizelerin yapısını, imgelerin nasıl kurulduğunu bilen okur şiirden daha çok tat alır. Çözümleme, şiirin sesini boğmak değil, kulağı eğitmektir. Yeter ki çözümleme bir sınav sorusuna indirgenmesin.',KOKM,
 [('Her iki metin de şiir çözümlemenin edebiyat derslerinden kaldırılmasını önermektedir.',False,'II. metin çözümlemeyi yararlı bulur; kaldırılmasını önermez.'),
  ('II. metin, şiirin yalnızca tek bir doğru anlamı olduğunu ileri sürmektedir.',False,'II. metin anlamdan değil yapı ve imge bilgisinden söz eder; tek doğru anlam iddiası yoktur.'),
  ('I. metin, şiir çözümlemenin öğrenciyi şiire yaklaştırdığını ve sevdirdiğini söylemektedir.',False,'I. metin tam tersini söyler: çözümleme öğrenciyi şiirden uzaklaştırır.'),
  ('I. metin çözümlemenin şiirden uzaklaştırabildiğini, II. metin tadı artırabildiğini söylemektedir.',True,'I. metin uzaklaşma korkusunu, II. metin “daha çok tat alır” ifadesini içerir.'),
  ('II. metin, şiir çözümlemenin öğrencileri şiirden korkuttuğunu belirtmektedir.',False,'Korku I. metinde geçer; II. metin böyle bir şey söylemez.')],
 'Her metnin çözümlemeye bakışını (olumlu / olumsuz) belirle.','I. metin çözümlemeyi öğrenciyi şiirden uzaklaştıran bir uygulama olarak anlatır. II. metin ise çözümlemenin okurun tadını artırdığını söyler. Doğru şık bu iki bakışı birlikte verir.','İki metnin zıt vurgusunu yakalar.')
# ---------- 11 metin orta
Y('0011','pyn-metin','orta','C',
 'I. metin: Müzelere girişin ücretsiz olması, düşük gelirli ailelerin çocuklarına da sanatla karşılaşma fırsatı verir. Ücretli girişte bu çocukların çoğu müzenin kapısından bile geçemez. Eğitimde fırsat eşitliği, çoğu zaman bir bilet fiyatında başlar.\nII. metin: Ücretsiz giriş ziyaretçi sayısını artırır, ancak müzenin bakım ve koruma gelirlerini düşürür. Bir eserin bakımı, bilet gelirinin yetmediği yerde kamu bütçesine kalır; bütçe ise her zaman yeterli olmaz.',KOKM,
 [('Her iki metin de müzelere girişin ücretsiz olması gerektiğini önermektedir.',False,'II. metin ücretsiz girişin gelir sorunu yarattığını söyler; ücretsizliği önermez.'),
  ('II. metin, ücretsiz girişin ziyaretçi sayısını azalttığını söylemektedir.',False,'II. metin ziyaretçi sayısının arttığını söyler; şık tersini söylemektedir.'),
  ('I. metin ücretli girişin erişimi, II. metin ücretsiz girişin geliri etkilediğini söyler.',True,'I. metin ücretli girişte çocukların giremediğini, II. metin ücretsizlikte gelirin düştüğünü söyler.'),
  ('I. metin, müze gelirlerinin kamu bütçesinden karşılanması gerektiğini savunmaktadır.',False,'Kamu bütçesinden II. metin söz eder; I. metin gelir kaynağına girmez.'),
  ('II. metin, düşük gelirli ailelerin çocuklarının müzeye gidemediğini ifade etmektedir.',False,'Bu yargı I. metindedir; II. metin ailelerin gelirinden söz etmez.')],
 'Her metnin ücretli ve ücretsiz giriş hakkında neyi sorun ettiğini yaz.','I. metin ücretli girişin düşük gelirli çocukların erişimini engellediğini, II. metin ücretsiz girişin müzenin gelirini düşürdüğünü söyler. Doğru şık bu iki noktayı doğru metinlere verir.','Metinlerin ele aldığı farklı sonuçları ayırt eder.')
# ---------- 12 metin zor
Y('0012','pyn-metin','zor','A',
 'I. metin: Geniş koridorlu bir okulda öğrencilerin teneffüste daha çok sohbet ettiği doğrudur; ancak okul binasının öğrencilerin davranışını belirlediğini söylemek yanlıştır. Koridor yalnızca sohbeti kolaylaştırır; konuşmak isteyen öğrenci dar bir koridorda da durup konuşur. Mekân davranışı belirlemez; yalnızca bazı davranışları kolaylaştırır ya da zorlaştırır.\nII. metin: Mekân, davranışın sınırlarını çizer; duvarı olmayan bir odada gizlilik beklenemez. Bir okulun yapısı, orada neyin yapılabileceğini önceden belirler. Duvarların izin vermediği bir davranış ise ancak duvarı değiştirmekle mümkün olur.',KOKM,
 [('I. metin, mekânın davranışa etkisini II. metinden daha sınırlı görmektedir.',True,'I. metin mekânı yalnızca davranışı kolaylaştıran ya da zorlaştıran bir etken sayar; II. metin mekânı davranışın sınırı sayar.'),
  ('Her iki metin de mekânın davranışı hiçbir biçimde etkilemediğini savunmaktadır.',False,'I. metin mekânın bazı davranışları kolaylaştırdığını, II. metin davranışın sınırlarını çizdiğini söyler; ikisi de etki kabul eder.'),
  ('I. metin, geniş koridorlu okullarda öğrencilerin sohbet etmediğini söylemektedir.',False,'I. metin geniş koridorda öğrencilerin daha çok sohbet ettiğini söyler; şık tersini söylemektedir.'),
  ('I. metin, dar koridorda öğrencilerin konuşmasının mümkün olmadığını belirtmektedir.',False,'I. metin konuşmak isteyen öğrencinin dar koridorda da durup konuştuğunu söyler; şık parçaya terstir.'),
  ('II. metin, duvarı olmayan odada gizliliğin sağlanabileceğini ileri sürmektedir.',False,'II. metin duvarı olmayan odada gizlilik beklenemeyeceğini söyler; şık tersini söylemektedir.')],
 'Her metnin mekânın davranışa etkisine verdiği ağırlığı “az / çok” diye derecelendir.','I. metin mekânın etkisini sınırlı (kolaylaştırma ya da zorlaştırma), II. metin sınır çizici ve belirleyici görür. Bu fark doğru şıkkın dayanağıdır; diğer dört şık metinlerin söylediklerini tersine çevirir ya da metinlerde olmayan bir şey söyler.','Metinlerin görüş derecelerini karşılaştırır.')
# ---------- 13 durum kolay
Y('0013','pyn-durum','kolay','D',
 'Bir ürünün fiyatı yükseldiğinde, o ürüne olan istek çoğu zaman azalır. Ancak bu azalma her üründe aynı değildir: ekmek, su gibi vazgeçilmesi güç ürünlerde azalma çok küçük kalır; vazgeçilebilir ürünlerde ise belirgindir. Çünkü alıcı, vazgeçemediği ürüne daha pahalı olsa da para ödemeye devam eder.\nBir ailenin alışveriş listesinde ekmek ve çikolata vardır. Bir ay içinde ekmeğin de çikolatanın da fiyatı aynı oranda artmıştır.',
 'Bu metne göre ailenin ay sonundaki alışverişiyle ilgili aşağıdakilerden hangisi beklenir?',
 [('Ekmek alımı ve çikolata alımı aynı oranda azalır.',False,'Metne göre azalma her üründe aynı değildir; vazgeçilmesi güç ürün ekmektir.'),
  ('Ekmek alımı, çikolata alımından daha çok azalır.',False,'Vazgeçilmesi güç olan ekmekte azalma küçük kalır; şık ters kurulmuştur.'),
  ('İki ürünün alımı da hiç değişmez.',False,'Metin vazgeçilebilir üründe azalmanın belirgin olduğunu söyler; çikolata alımı azalır.'),
  ('Çikolata alımı, ekmek alımından daha çok azalır.',True,'Çikolata vazgeçilebilir, ekmek vazgeçilmesi güç üründür; azalma çikolatada belirgindir.'),
  ('Ekmek alımı tümüyle durur.',False,'Metne göre ekmekte azalma “çok küçük” kalır; alım durmaz.')],
 'Hangi ürün vazgeçilebilir, hangisi vazgeçilmesi güç? Metne göre sınıfla.','Ekmek vazgeçilmesi güç ürün olduğundan fiyat artışında alımı çok az azalır. Çikolata vazgeçilebilir ürün olduğundan alımı belirgin biçimde azalır.','Metindeki ilişkiyi iki örneğe ayrı ayrı uygular.')
# ---------- 14 durum orta
Y('0014','pyn-durum','orta','E',
 'İnsan beyni iki işi gerçekten aynı anda yapmaz; işler arasında hızla geçiş yapar. Her geçişte dikkatin bir bölümü yeni işe uyum sağlamaya harcanır ve bu yüzden aynı anda birden çok işle uğraşan kişi, her işi sırayla yapan kişiden daha yavaş ilerler. Aynı kişi, işi bölen bir kesinti olmadığında dikkatini baştan sona koruyabilir.\nCeren üç gün boyunca aynı türde ödevleri yapmıştır. Birinci gün telefonu açık tutup gelen mesajlara hemen yanıt vermiştir. İkinci gün telefonu tamamen kapatmıştır. Üçüncü gün telefonu açık tutmuş, ancak bildirimleri kapatıp mesajlara ödev bitince bakmıştır.',
 'Bu metne göre Ceren’in üç gününe ilişkin aşağıdakilerden hangisi beklenir?',
 [('Üçüncü gün ödev, birinci günden daha yavaş ilerlemiştir.',False,'Üçüncü günde işi bölen geçiş yoktur; ödevin birinci günden yavaş ilerlemesi beklenmez.'),
  ('Birinci gün ödev, ikinci günden daha hızlı ilerlemiştir.',False,'Birinci gün mesajlara dönmek iş geçişi demektir; ödev ikinci günden hızlı değil, yavaş ilerler.'),
  ('İkinci günle üçüncü gün arasında dikkat kaybı bakımından belirgin bir fark vardır.',False,'İkinci ve üçüncü günde ödev sırasında işi bölen bir geçiş yoktur; fark beklenmez.'),
  ('Birinci gün, dikkat kaybının en az olduğu gündür.',False,'Dikkat kaybı iş geçişi olan birinci günde en fazladır.'),
  ('Üçüncü gündeki dikkat kaybı, birinci gündekinden azdır.',True,'Üçüncü günde mesajlara ödev bitince bakıldığından geçiş yoktur; birinci günde geçişler vardır.')],
 'Her günde ödev sırasında iş geçişi olup olmadığını yaz.','Birinci günde mesajlara hemen yanıt verildiği için işler arası geçiş vardır. İkinci ve üçüncü günde ödev sırasında geçiş yoktur. Bu nedenle üçüncü gündeki dikkat kaybı birinciden azdır.','Metindeki kuralı üç ayrı güne uygular.','1. gün: geçiş var · 2. gün: geçiş yok · 3. gün: geçiş yok')
# ---------- 15 durum zor
Y('0015','pyn-durum','zor','B',
 'Bir anlatının şimdiki zamanı tek bir günü aşmıyorsa o anlatıya “dar zamanlı”, şimdiki zaman boyunca olaylar tek bir yerde geçiyorsa “tek mekânlı” denir. Anlatı, şimdiki zamanın akışını bırakıp geçmişteki bir olaya dönüyorsa “geri dönüşlü” sayılır. Bu üç özellik birbirinden bağımsızdır; her biri ayrı ayrı sınanır.\nBir romanın şimdiki zamanı iki gündür. Birinci gün olaylar bir köy evinde, ikinci gün şehirdeki bir hastanede geçer. İkinci günün sonunda anlatıcı, köydeki çocukluğunu anımsar.',
 'Bu metne ve duruma göre romanla ilgili aşağıdakilerden hangisi söylenebilir?',
 [('Dar zamanlı, tek mekânlı ve geri dönüşlüdür.',(1,1,1)==(0,0,1),'Şimdiki zaman iki gün olduğundan dar zamanlı değildir; iki yerde geçtiğinden tek mekânlı da değildir.'),
  ('Dar zamanlı ve tek mekânlı değildir; geri dönüşlüdür.',(0,0,1)==(0,0,1),'Şimdiki zaman iki gün (dar zamanlı değil), iki yer (tek mekânlı değil) ve çocukluğa dönüş (geri dönüşlü) vardır.'),
  ('Dar zamanlıdır; tek mekânlı değildir, geri dönüşlüdür.',(1,0,1)==(0,0,1),'Şimdiki zaman iki gün olduğundan roman dar zamanlı değildir.'),
  ('Dar zamanlı değildir, tek mekânlıdır; geri dönüşlü değildir.',(0,1,0)==(0,0,1),'Olaylar köy evi ve hastane olmak üzere iki yerde geçtiğinden tek mekânlı değildir; çocukluğa dönüş de geri dönüşlüdür.'),
  ('Dar zamanlı, tek mekânlı ve geri dönüşlü değildir.',(0,0,0)==(0,0,1),'Anlatıcı ikinci günün sonunda çocukluğunu anımsadığı için roman geri dönüşlüdür.')],
 'Üç özelliği ayrı ayrı sına: gün sayısı, yer sayısı, geçmişe dönüş.','Şimdiki zaman iki gündür (dar zamanlı değil), olaylar iki yerde geçer (tek mekânlı değil), anlatıcı çocukluğunu anımsar (geri dönüşlü). Üç sonuç birlikte yalnız B şıkkında vardır.','Üç koşulu ayrı ayrı sınayıp birleştirir.','gün: 2 → dar zamanlı değil · yer: 2 → tek mekânlı değil · çocukluk anısı → geri dönüşlü')

bitir(Q)
from collections import Counter
print('tip',dict(Counter(q['tip'] for q in Q.P.ANA)))
