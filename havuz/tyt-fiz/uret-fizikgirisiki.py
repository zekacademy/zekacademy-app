"""TYT Fizik · Fizik Bilimine Giriş ikinci paket (14 soru, kardeş yok, ipucu 1). Tablo ve şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
H.KONU='Fizik Bilimine Giriş'
P=Parti('fizikgirisiki','Fizik Bilimine Giriş','fiz|Fizik Bilimine Giriş',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2026 TYT Fizik soruları (yalnız mantık) · MEB 9. sınıf fizik'
TIP={'al':('fz-fg2-alt-dal','Olay–alt dal eşleştirme'),
     'di':('fz-fg2-disiplin','Fiziğin diğer bilim dallarıyla ilişkisi'),
     'tt':('fz-fg2-temel-turetilmis','Temel ve türetilmiş nicelikler'),
     'ol':('fz-fg2-olcu-aleti','SI birimleri ve ölçü aletleri'),
     'sv':('fz-fg2-skaler-vektorel','Skaler ve vektörel nicelikler'),
     'by':('fz-fg2-bilimsel-yontem','Bilimsel yöntem basamakları ve hipotez'),
     'dg':('fz-fg2-degisken','Bağımlı, bağımsız ve kontrol değişkeni'),
     'oh':('fz-fg2-olcme-hata','Ölçme ve okuma hatası'),
     'bt':('fz-fg2-birim-tutarlilik','Bağıntılarda birim tutarlılığı'),
     'bd':('fz-fg2-birim-donusum','SI birimine dönüştürme'),
     'mr':('fz-fg2-merkez','Bilim araştırma merkezleri')}
def K(n,t,alt,fikir,tuzak,z,kalip,adim):
    tid,tad=TIP[t]; kart(f'K-FZFG2-{n:02d}',alt,fikir,tuzak,z,kalip,adim,tid,tad,KY)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def sk(*l,sc=1.0): return tikz_svg(HEAD.replace('[','[scale=%s,'%sc,1)+'\n'.join(l)+TAIL)
ROM={1:'I',2:'II',3:'III'}
def lab(s):
    s=sorted(s); return 'Yalnız '+ROM[s[0]] if len(s)==1 else (ROM[s[0]]+' ve '+ROM[s[1]] if len(s)==2 else 'I, II ve III')
def parse(l):
    return {n for n,r in ROM.items() if r in l.replace('Yalnız','').replace(',',' ').replace('ve',' ').split()}
def q(no,**k):
    assert len(k['ip'])==1
    ad=k.pop('ad'); mk(P,no,ad=ad,adim=len(ad),**k)
def onc(no,giris,claims,son,sira,goster=True,**k):
    """claims: [(öncül metni, doğru_mu, gerekçe)]; doğru kümesi, adımlar, çeldirici açıklamaları ve anahtar buradan üretilir."""
    assert len(claims)==3
    truth={i+1 for i,c in enumerate(claims) if c[1]}
    for l in sira: assert lab(parse(l))==l,l
    assert lab(truth) in sira and len(set(sira))==5
    yan=[]
    for l in sira:
        if l==lab(truth): continue
        S=parse(l); p=[]
        for n in sorted(S-truth): p.append(f'{ROM[n]}. yargıyı doğru sanmış: {claims[n-1][2]}')
        for n in sorted(truth-S): p.append(f'{ROM[n]}. yargıyı yanlış sanmış: {claims[n-1][2]}')
        yan.append((l,' '.join(p),'bilgi'))
    ad=[A(f'{ROM[n]}. yargıyı sına',claims[n-1][2],'doğru' if n in truth else 'yanlış') for n in (1,2,3)]
    ad.append(A('Sonucu yaz','Doğru olan yargıları birleştir.','Doğru olanlar: '+lab(truth)))
    kok=giris+('\n'+'\n'.join(f'{ROM[i+1]}. {c[0]}' for i,c in enumerate(claims)) if goster else '')+'\n'+son
    q(no,ad=ad,metin=kok,dogru=lab(truth),yan=yan,sira=sira,kalip=k.pop('kalip','öncüllü'),**k)
S1=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
S2=['Yalnız I','I ve II','I ve III','II ve III','I, II ve III']
ALT1='Fizik Bilimi ve Alt Dalları'; ALT2='Fiziğin Diğer Disiplinlerle İlişkisi'; ALT3='Fiziksel Nicelikler ve Ölçme'; ALT4='Bilimsel Yöntem'; ALT5='Bilim Araştırma Merkezleri'

# ================= 01 · olay–alt dal tablosu · kolay · öncüllü =================
K(1,'al',ALT1,'Fizik; mekanik, termodinamik, optik, elektrik ve manyetizma gibi alt dallara ayrılır; olay hangi niceliği ya da olguyu konu alıyorsa o alt dalda incelenir.','Hâl değişimini optik, pusula yönelmesini mekanik sanmak.','kolay','tablo',3)
OLAY={'I':('Eğik düzlemde kayan top','Mekanik',True),'II':('Soğuk camda yoğuşan su buharı','Optik',False),'III':('Pusula iğnesinin yön göstermesi','Elektrik ve manyetizma',True)}
SK1=tablo_svg(['Numara','Gözlenen olay','Alt dal'],[[r,v[0],v[1]] for r,v in OLAY.items()])
onc('0001','Bir fizik öğretmeni, fiziğin mekanik, termodinamik, optik, elektrik ve manyetizma gibi alt dallara ayrıldığını anlattıktan sonra öğrencilerden günlük hayatta gözlemledikleri olayları, o olayı inceleyen alt dalla eşleştirmelerini istiyor. Bir öğrencinin hazırladığı tablo aşağıda verilmiştir.',
 [('Eğik düzlemdeki topun kayması, cismin konum ve hareket değişimini konu aldığından mekanikte incelenir; eşleştirme doğrudur.',True,'Eğik düzlemde kayan top hareket ve kuvvet bilgisiyle incelenir; mekanik doğru alt daldır.'),
  ('Su buharının soğuk camda yoğuşması',False,'Yoğuşma ısı alışverişi ve hâl değişimidir; termodinamikte incelenir, optikle ilgisi yoktur.'),
  ('Pusulanın yön göstermesi',True,'Pusula iğnesi Dünya’nın manyetik alanında yönelir; bu olay manyetizma ile ilgilidir.')],
 'Buna göre, tablodaki numaralı eşleştirmelerden hangileri doğrudur?',S1,goster=False,
 tipId=TIP['al'][0],tip=TIP['al'][1],z='kolay',alt=ALT1,kaz='Günlük hayattaki olayları fiziğin ilgili alt dalıyla eşleştirir.',
 kart='K-FZFG2-01 (olay–alt dal eşleştirme) · tablo',istenen='Doğru eşleştirmeler.',kalip='tablo',ip=['Her olayda hangi büyüklüğün (hareket, ısı, ışık, mıknatıs) incelendiğini düşün.'],
 bilgi=[B('Fiziğin alt dalları','mekanik hareket ve kuvveti, termodinamik ısıyı ve hâl değişimini, optik ışığı, elektrik ve manyetizma yük akışını ve mıknatıs etkilerini inceler. Örnek: gökkuşağının oluşumu optikte incelenir')],
 puf='Olayda hangi nicelik (kuvvet, ısı, ışık, mıknatıs) öne çıkıyorsa onu inceleyen alt dalı seç.',sekil=SK1)

# ================= 02 · diğer disiplinlerle ilişki · kolay =================
K(2,'di',ALT2,'Fizik, kimya, biyoloji, astronomi ve yer bilimleriyle ortak çalışır; deprem dalgalarının incelenmesi fizik ile jeolojinin ortak alanıdır (jeofizik).','Yer kabuğu çalışmasını astronomi ya da tıpla ilişkilendirmek.','kolay','düz',2)
q('0002',tipId=TIP['di'][0],tip=TIP['di'][1],z='kolay',alt=ALT2,kaz='Fiziğin diğer bilim dallarıyla ilişkisini örnek üzerinde belirler.',
 kart='K-FZFG2-02 (fizik–jeoloji ilişkisi) · jeofizik',kalip='düz',
 metin='Bir üniversitedeki araştırma grubu, depremler sırasında yer kabuğunda yayılan titreşimlerin hızını sismograf adı verilen aletlerle ölçüyor. Elde edilen veriler, fizikteki dalgaların yayılma bilgisiyle yorumlanarak yer kabuğunun katmanlarının yapısı hakkında sonuçlar çıkarılıyor.\nBuna göre bu çalışma, fiziğin hangi bilim dalıyla ilişkisine bir örnektir?',
 dogru='Jeoloji',sira=['Astronomi','Kimya','Biyoloji','Tıp','Jeoloji'],yan=[('Astronomi','Gök cisimlerini inceleyen astronomiyi seçmiş; çalışma yer kabuğuyla ilgilidir.','dikkat'),('Kimya','Maddenin yapısı ve tepkimeleriyle ilgilenen kimyayı seçmiş; burada yer kabuğunun katmanları incelenmektedir.','bilgi'),('Biyoloji','Canlıları inceleyen biyolojiyi seçmiş; ölçülen canlı değil, yer kabuğundaki titreşimlerdir.','bilgi'),('Tıp','İnsan sağlığına yönelik tıbbı seçmiş; çalışmanın insan sağlığıyla ilgisi yoktur.','dikkat')],
 istenen='Çalışmanın fizikle ilişkilendiği bilim dalı.',ip=['Çalışmanın neyi (canlı, gök cismi, yer kabuğu) incelediğine bak.'],
 bilgi=[B('Fiziğin diğer bilimlerle ilişkisi','fizik; astronomi (gök cisimleri), jeoloji (yer kabuğu), biyoloji ve tıp (canlılar), kimya (madde) ile ortak çalışır. Örnek: kalbin elektriksel etkinliğini kaydeden cihaz fiziğin tıpla ilişkisidir')],
 ad=[A('Çalışmanın konusunu bul','Ölçülen titreşimler depremde yer kabuğunda yayılır.','konu: yer kabuğu'),A('Fizik yöntemini belirle','Titreşimlerin hızı dalga bilgisiyle yorumlanır; bu fizik yöntemidir.','yöntem: fizik'),A('Yer kabuğunu inceleyen bilimi seç','Yer kabuğunun yapısını inceleyen bilim dalı jeolojidir.','Jeoloji')],
 puf='Fiziğin başka bilimle ilişkisini, çalışmanın incelediği varlığa (canlı, gök cismi, yer kabuğu) bakarak bul.')

# ================= 03 · temel nicelik sayısı, tablo · orta =================
K(3,'tt',ALT3,'Uzunluk, kütle, zaman, sıcaklık gibi nicelikler temeldir; kuvvet, hız, hacim, alan gibi diğerleri temel niceliklerden türetilir.','Birimi tek sembolle yazılan her niceliği (N gibi) temel saymak.','orta','tablo',3)
NIC=[('Hız','m/s',False),('Kütle','kg',True),('Hacim','m³',False),('Sıcaklık','K',True),('Kuvvet','N',False),('Zaman','s',True),('Alan','m²',False)]
tem=sum(1 for n in NIC if n[2]); assert tem==3 and tem+1==4 and tem+2==5 and tem+3==6 and tem-1==2
SK3=tablo_svg(['Nicelik','SI birimi'],[[a,b] for a,b,_ in NIC])
q('0003',tipId=TIP['tt'][0],tip=TIP['tt'][1],z='orta',alt=ALT3,kaz='Verilen niceliklerden temel olanları ayırt eder.',
 kart='K-FZFG2-03 (temel nicelik sayısı) · tablo, 7 nicelik',kalip='tablo',
 metin='Bir öğrenci, fizik defterine SI birim sisteminde sıkça kullanılan yedi niceliği ve birimlerini aşağıdaki tabloda gösterildiği gibi yazıyor. Öğretmeni, bu niceliklerin hangilerinin başka niceliklerden türetilemeyen, yani temel nicelik olduğunu bulmasını istiyor.\nBuna göre tablodaki niceliklerden kaç tanesi temel niceliktir?',
 sekil=SK3,dogru=3,yan=[(2,'Sıcaklığı temel nicelik saymamış; kütle ve zamanı doğru bulup kelvin birimli sıcaklığı atlamış.','bilgi'),(4,'Birimi tek sembolle yazılan kuvveti (N) de temel saymış.','dikkat'),(5,'Kuvvete ek olarak hacmi (m³) de temel nicelik saymış.','bilgi'),(6,'Kuvvet ve hacme ek olarak hızı da temel saymış; birimleri m ve s cinsinden yazılabilen niceliklerin türetilmiş olduğunu görmemiş.','bilgi')],
 istenen='Tablodaki temel nicelik sayısı.',ip=['Her niceliğin biriminin başka birimlerden oluşup oluşmadığına bak.'],
 bilgi=[B('Temel ve türetilmiş nicelik','temel nicelikler başka niceliklerden türetilemez (uzunluk, kütle, zaman, sıcaklık, akım şiddeti…); türetilmiş niceliklerin birimi temel birimlerden çıkar. Örnek: yoğunluk birimi kg/m³ olduğundan türetilmiştir')],
 ad=[A('Birimleri temel birimlerle karşılaştır','m/s, m³ ve m² birimleri uzunluk ve zaman biriminden oluşur.','hız, hacim, alan: türetilmiş'),A('Kuvveti incele','Newton, kg·m/s² olarak yazılabilir.','kuvvet: türetilmiş'),A('Kalanları say','Kütle (kg), sıcaklık (K) ve zaman (s) başka niceliklerden türetilemez.','kütle, sıcaklık, zaman'),A('Sonuç','Temel nicelik sayısı üçtür.','3')],
 puf='Birimi başka birimlerin çarpım ya da bölümü olarak yazılabilen nicelik türetilmiştir; tek sembollü birim temel olmayı garanti etmez.')

# ================= 04 · dereceli silindir ile hacim ve özkütle · orta =================
K(4,'ol',ALT3,'Dereceli silindirde cismin hacmi, su seviyesindeki artıştan bulunur (1 mL = 1 cm³); özkütle için g ve cm³ SI birimine çevrilir.','Son seviyeyi cismin hacmi saymak; g ve cm³ değerlerini birim çevirmeden kullanmak.','orta','şekilli',4)
V1,V2,mg=20,50,240; dV=V2-V1
assert dV==30 and Fr(mg,1000)/Fr(dV,10**6)==8000
assert Fr(mg,1000)/Fr(V2,10**6)==4800 and Fr(mg,1000)/Fr(V1,10**6)==12000
assert Fr(mg,100)/Fr(dV,10**6)==80000 and Fr(mg)/Fr(dV,10**6)==8000000
sc=.075
def silindir(x0,seviye,top):
    h=60*sc; o=[]
    o.append(f'\\fill[vurgu!15] ({x0},0) rectangle ({x0+1.1},{seviye*sc:.3f});')
    o.append(f'\\draw[thick] ({x0},{h+.25}) -- ({x0},0) -- ({x0+1.1},0) -- ({x0+1.1},{h+.25});')
    o.append(f'\\draw[thick] ({x0},{seviye*sc:.3f}) -- ({x0+1.1},{seviye*sc:.3f});')
    for v in range(0,61,5):
        L=.32 if v%10==0 else .18
        o.append(f'\\draw ({x0},{v*sc:.3f}) -- ({x0+L},{v*sc:.3f});')
        if v%10==0 and v>0: o.append(f'\\node[left,font=\\scriptsize] at ({x0},{v*sc:.3f}) {{${v}$}};')
    if top: o.append(f'\\draw[thick,fill=gray!45] ({x0+.55},.5) circle (.42);')
    return '\n'.join(o)
SK4=sk(silindir(0,V1,False),silindir(3.3,V2,True),'\\node[font=\\scriptsize] at (.55,-.45) {cisimsiz};','\\node[font=\\scriptsize] at (3.85,-.45) {cisimli};','\\node[font=\\scriptsize,above] at (-.35,4.95) {mL};','\\node[font=\\scriptsize] at (2.2,-1.0) {(şekil ölçekli değildir)};',sc=1.1)
q('0004',tipId=TIP['ol'][0],tip=TIP['ol'][1],z='orta',alt=ALT3,kaz='Dereceli silindirden hacim okur ve g, cm³ değerlerini SI birimine çevirerek özkütleyi hesaplar.',
 kart='K-FZFG2-04 (dereceli silindir, özkütle) · 240 g, seviye farkı',kalip='şekilli',
 metin='Laboratuvarda bir öğrenci, düzgün şekilli ve içi dolu bir metal küreyi hem eşit kollu terazide hem de dereceli silindirde inceliyor. Eşit kollu terazide kürenin kütlesini 240 g buluyor. Daha sonra kürenin hacmini bulmak için içinde su bulunan dereceli silindire küreyi şekildeki gibi tamamen batırıyor. Su seviyeleri şekilde gösterilmiştir (1 mL = 1 cm³).\nBuna göre kürenin yapıldığı maddenin özkütlesi kaç kg/m³’tür?',
 sekil=SK4,dogru=8000,yan=[(4800,'Cisim batırıldıktan sonraki seviyeyi (50 mL) cismin hacmi sanmış: 240 g ÷ 50 cm³ = 4,8 g/cm³ = 4800 kg/m³.','dikkat'),(12000,'Cisimsiz seviyeyi (20 mL) cismin hacmi sanmış: 240 g ÷ 20 cm³ = 12 g/cm³ = 12 000 kg/m³.','dikkat'),(80000,'Gramı kilograma çevirirken 1000 yerine 100’e bölmüş: 2,4 kg ÷ (3 × 10⁻⁵ m³) = 80 000 kg/m³.','islem'),(8000000,'Kütleyi kilograma çevirmemiş: 240 g ÷ (3 × 10⁻⁵ m³) = 8 000 000, bunu kg/m³ sanmış.','islem')],
 istenen='Metal kürenin özkütlesi (kg/m³).',ip=['Cisim suya batınca su seviyesinin neden değiştiğini düşün.'],
 bilgi=[B('Hacim ölçme','dereceli silindirde cisim suya batırılınca seviyedeki artış cismin hacmini verir; 1 mL = 1 cm³ = 10⁻⁶ m³. Örnek: seviye 12 mL artarsa hacim 12 cm³ olur'),B('Birim çevirme','1 kg = 1000 g. Özkütle d = m ÷ V; SI birimi kg/m³’tür')],
 ad=[A('Hacmi bul','Cismin hacmi seviye farkına eşittir.','V = 50 − 20 = 30 mL = 30 cm³'),A('Hacmi çevir','1 cm³ = 10⁻⁶ m³.','V = 30 × 10⁻⁶ = 3 × 10⁻⁵ m³'),A('Kütleyi çevir','Gram kilograma çevrilir.','m = 240 g = 0,24 kg'),A('Özkütleyi hesapla','Kütleyi hacme böl.','d = 0,24 ÷ (3 × 10⁻⁵) = 8000 kg/m³')],
 puf='Dereceli silindirde hacim, son seviye ile ilk seviyenin farkıdır; özkütlede g ve cm³ değerlerini SI birimine çevir.')

# ================= 05 · SI birimine dönüştürme · zor · öncüllü =================
K(5,'bd',ALT3,'Birim çevirmede önce büyüklüğün SI karşılığı, sonra oran birimlerinde paydaki ve paydadaki birimler ayrı ayrı çevrilir.','Özkütlede cm³ → m³ çevirmesini unutup g/cm³ değerini 10 ile çarpmak; km/h → m/s için 3,6 ile bölmek yerine çarpmak.','zor','öncüllü',4)
assert Fr(90000,3600)==25 and Fr(78,10)*Fr(1,1000)/Fr(1,10**6)==7800 and Fr(18,10)*Fr(1,1000)/60==Fr(3,10**5)
onc('0005','Bir öğrenci, günlük hayattan seçtiği üç niceliği SI birim sistemine çevirip defterine yazıyor: bir aracın hızını, bir metal parçanın özkütlesini ve bir musluktan akan suyun akış miktarını. Öğretmeni, öğrencinin yaptığı çevirmeleri tek tek kontrol ederek hangilerinin doğru olduğunu soruyor.',
 [('90 km/h’lik hız, SI birim sisteminde 25 m/s’ye eşittir.',True,'90 km = 90 000 m ve 1 saat = 3600 s olduğundan 90 000 ÷ 3600 = 25 m/s’dir.'),
  ('7,8 g/cm³’lük özkütle, SI birim sisteminde 780 kg/m³’e eşittir.',False,'7,8 g = 7,8 × 10⁻³ kg ve 1 cm³ = 10⁻⁶ m³ olduğundan özkütle 7,8 × 10⁻³ ÷ 10⁻⁶ = 7800 kg/m³’tür.'),
  ('Dakikada 1,8 L akan suyun akış miktarı, SI birim sisteminde 3 × 10⁻⁵ m³/s’ye eşittir.',True,'1,8 L = 1,8 × 10⁻³ m³ ve 1 dakika = 60 s olduğundan 1,8 × 10⁻³ ÷ 60 = 3 × 10⁻⁵ m³/s’dir.')],
 'Buna göre, öğrencinin çevirmelerinden hangileri doğrudur?',S2,
 tipId=TIP['bd'][0],tip=TIP['bd'][1],z='zor',alt=ALT3,kaz='Hız, özkütle ve akış miktarı gibi niceliklerin birimlerini SI birimine çevirir.',
 kart='K-FZFG2-05 (SI birimine dönüştürme) · öncüllü',istenen='Doğru olan çevirmeler.',ip=['Her çevirmede pay ve paydadaki birimleri ayrı ayrı SI birimine çevirip oranı yeniden yaz.'],
 bilgi=[B('Birim çevirme','1 km = 1000 m; 1 saat = 3600 s; 1 g = 10⁻³ kg; 1 cm³ = 10⁻⁶ m³; 1 L = 10⁻³ m³; 1 dakika = 60 s. Örnek: 36 km/h = 36 000 m ÷ 3600 s = 10 m/s')],
 puf='Oran birimlerinde pay ve paydayı ayrı ayrı SI birimine çevir; sonra böl.')

# ================= 06 · yol ve yer değiştirme şeması · zor · öncüllü =================
K(6,'sv',ALT3,'Yol skalerdir; yer değiştirme başlangıç ve bitiş konumunu birleştiren vektördür. Geri dönüşlü yolda yer değiştirmenin büyüklüğü yoldan çok küçük olabilir, ortalama sürat ortalama hızın büyüklüğünden büyük olur.','Yer değiştirmenin büyüklüğünü alınan yola eşit saymak; ortalama sürat ile ortalama hızı aynı sanmak.','zor','şekilli',5)
ab,bc,cd=6,8,6; yol=ab+bc+cd; yd=bc
assert yol==20 and yd==8 and yd<yol
u=.42
A_=(0,0); B_=(ab*u,0); C_=(ab*u,bc*u); D_=(ab*u-cd*u,bc*u)
SK6=sk(f'\\draw[thick,vurgu,{ARR}] (0,0) -- ({B_[0]:.3f},0);',f'\\draw[thick,vurgu,{ARR}] ({B_[0]:.3f},0) -- ({C_[0]:.3f},{C_[1]:.3f});',f'\\draw[thick,vurgu,{ARR}] ({C_[0]:.3f},{C_[1]:.3f}) -- ({D_[0]:.3f},{D_[1]:.3f});',
 '\\fill (0,0) circle (2pt); \\node[below left] at (0,0) {A};',f'\\fill ({B_[0]:.3f},0) circle (2pt); \\node[below right] at ({B_[0]:.3f},0) {{B}};',f'\\fill ({C_[0]:.3f},{C_[1]:.3f}) circle (2pt); \\node[above right] at ({C_[0]:.3f},{C_[1]:.3f}) {{C}};',f'\\fill ({D_[0]:.3f},{D_[1]:.3f}) circle (2pt); \\node[above left] at ({D_[0]:.3f},{D_[1]:.3f}) {{D}};',
 f'\\node[below] at ({ab*u/2:.3f},-.05) {{$6$ m}};',f'\\node[right] at ({ab*u+.12:.3f},{bc*u/2:.3f}) {{$8$ m}};',f'\\node[above] at ({ab*u/2:.3f},{bc*u+.05:.3f}) {{$6$ m}};',
 f'\\draw[{ARR},thick] (3.6,.3) -- (3.6,1.1); \\node[above] at (3.6,1.1) {{Kuzey}};',f'\\draw[{ARR},thick] (3.6,.3) -- (4.4,.3); \\node[right] at (4.4,.3) {{Doğu}};',sc=1.2)
onc('0006','Bir öğrenci okul bahçesinde A noktasından yürümeye başlıyor, B ve C noktalarında dönerek D noktasında duruyor. Yolu, uzunlukları ve yönleri şekilde verilmiştir. Öğrenci yolun tamamını sabit süratle yürümüştür.',
 [('Öğrencinin aldığı yol 20 m’dir.',True,'Yol, bütün parçaların toplamıdır: 6 + 8 + 6 = 20 m.'),
  ('Öğrencinin yer değiştirmesinin büyüklüğü 20 m’dir.',False,'Yer değiştirmenin büyüklüğü A ile D arasındaki doğrusal uzaklıktır; D noktası A’nın 8 m kuzeyindedir, yer değiştirme 8 m’dir.'),
  ('Öğrencinin ortalama hızının büyüklüğü, ortalama süratinden küçüktür.',True,'Aynı sürede ortalama sürat 20 m yola, ortalama hızın büyüklüğü 8 m yer değiştirmeye bağlıdır; 8 < 20 olduğundan ortalama hızın büyüklüğü küçüktür.')],
 'Buna göre, bu yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 tipId=TIP['sv'][0],tip=TIP['sv'][1],z='zor',alt=ALT3,kaz='Geri dönüşlü bir yolda yol ve yer değiştirmeyi, sürat ve hızı skaler–vektörel ayrımıyla değerlendirir.',
 kart='K-FZFG2-06 (yol, yer değiştirme, sürat–hız; üç parçalı yol) · öncüllü',istenen='Doğru olan yargılar.',kalip='şekilli',ip=['Yolun toplam uzunluğu ile başlangıç ve bitiş noktaları arasındaki doğrusal uzaklığı ayrı ayrı bul.'],
 bilgi=[B('Skaler ve vektörel','skaler nicelik yalnız büyüklük, vektörel nicelik büyüklük ve yön taşır. Yol skaler, yer değiştirme vektöreldir. Örnek: 3 m doğuya sonra 3 m batıya giden kişinin yolu 6 m, yer değiştirmesi sıfırdır')],
 puf='Yol, gidilen bütün uzunluktur (skaler); yer değiştirme başlangıçtan sona çizilen vektördür ve geri dönüşte yoldan küçük kalır.',sekil=SK6)

# ================= 07 · bilimsel yöntem sıralaması · orta =================
K(7,'by',ALT4,'Bilimsel yöntemde sıra: gözlem, hipotez, deney, sonuç; deney hipotezi sınamak için, sonuç ise deney verileriyle yazılır.','Hipotezi gözlemden önce, deneyi hipotezden önce ya da sonucu deneyden önce yazmak.','orta','düz',4)
ADIM={'I':'Metal ve tahta yüzeyde buz küplerinin erime sürelerini ölçüp kaydeder.','II':'“Metal yüzeydeki buz küpü daha çabuk erir.” biçiminde bir tahmin yazar.','III':'Tezgâhta duran buz küplerinden metal levhanın üstündekinin daha çabuk eridiğini fark eder.','IV':'Ölçüm değerlerini inceleyerek tahmininin doğru olup olmadığına karar verir.'}
DOGRU=['III','II','I','IV']
def sr(x): return ' – '.join(x)
assert sr(DOGRU)=='III – II – I – IV'
q('0007',tipId=TIP['by'][0],tip=TIP['by'][1],z='orta',alt=ALT4,kaz='Bilimsel yöntemin basamaklarını (gözlem, hipotez, deney, sonuç) doğru sıraya koyar.',
 kart='K-FZFG2-07 (bilimsel yöntem sırası) · buz küpü',kalip='düz',
 metin='Bir öğrenci, mutfakta metal bir levha ile tahta bir kesme tahtasının üzerine konan buz küplerinin farklı sürelerde eridiğini görüyor ve bu durumu bilimsel yöntemle araştırmaya karar veriyor. Bunun için aşağıdaki işlemleri yapıyor.\nI. '+ADIM['I']+'\nII. '+ADIM['II']+'\nIII. '+ADIM['III']+'\nIV. '+ADIM['IV']+'\nBuna göre öğrencinin yaptığı işlemlerin bilimsel yöntemdeki doğru sırası aşağıdakilerden hangisidir?',
 dogru=sr(DOGRU),sira=[sr(DOGRU),sr(['III','I','II','IV']),sr(['III','II','IV','I']),sr(['II','III','I','IV']),sr(['I','III','II','IV'])],
 yan=[(sr(['III','I','II','IV']),'Deneyi hipotezden önce yapmış; ölçümler tahmin kurulduktan sonra, onu sınamak için yapılır.','bilgi'),(sr(['III','II','IV','I']),'Sonucu deneyden önce yazmış; karar, ölçüm verileri toplandıktan sonra verilir.','bilgi'),(sr(['II','III','I','IV']),'Hipotezi gözlemden önce yazmış; tahmin, bir gözleme dayanarak kurulur.','bilgi'),(sr(['I','III','II','IV']),'Deneyi gözlemden de hipotezden de önce yapmış; deneyin amacı hipotezi sınamaktır.','bilgi')],
 istenen='İşlemlerin bilimsel yöntemdeki sırası.',ip=['Bir tahminin kurulabilmesi için önce neyin gerekli olduğunu, tahminin ise ne zaman sınanabileceğini düşün.'],
 bilgi=[B('Bilimsel yöntem','önce gözlem yapılır, gözlemden bir hipotez (sınanabilir tahmin) kurulur, hipotez deneyle sınanır, deney verilerine bakılarak sonuca varılır. Örnek: bitkinin pencere yönüne eğildiğini görüp “ışığa yönelir” demek hipotezdir, bunu sınamak deneydir')],
 ad=[A('Başlangıcı bul','Araştırma bir gözlemle başlar.','III. işlem ilk'),A('Hipotezi yerleştir','Gözleme dayanan tahmin, deneyden önce kurulur.','II. işlem ikinci'),A('Deneyi yerleştir','Ölçümler tahmini sınamak için yapılır.','I. işlem üçüncü'),A('Sonuca ulaş','Karar, ölçüm verileri incelenince verilir.','IV. işlem son'),A('Sırayı yaz','Gözlem, hipotez, deney, sonuç sırası uygulanır.','III – II – I – IV')],
 puf='Bilimsel yöntem sırası gözlem, hipotez, deney ve sonuçtur; deney hipotezi sınamak, sonuç ise deney verilerini yorumlamak içindir.')

# ================= 08 · değişken türleri, tablo · zor · öncüllü =================
K(8,'dg',ALT4,'Deneyde değiştirilen etken bağımsız, ölçülüp sonucu gözlenen etken bağımlı, sabit tutulan etkenler kontrol değişkenidir.','Bağımlı ve bağımsız değişkeni karıştırmak; sabit tutulan etkeni değişken saymak.','orta','tablo',4)
DEN=[('K',6,'A4','2,0','1,4'),('L',8,'A4','2,0','1,7'),('M',10,'A4','2,0','2,1')]
assert len({d[2] for d in DEN})==1 and len({d[3] for d in DEN})==1 and len({d[1] for d in DEN})==3 and len({d[4] for d in DEN})==3
SK8=tablo_svg(['Deney','Kanat uzunluğu (cm)','Kâğıt türü','Yükseklik (m)','Süre (s)'],[[d[0],d[1],d[2],d[3],d[4]] for d in DEN])
onc('0008','Bir öğrenci, kâğıttan yaptığı helikopterin kanat uzunluğunun, helikopterin yere düşme süresini etkileyip etkilemediğini araştırıyor. Üç helikopteri aynı cins kâğıttan yapıp aynı noktadan serbest bırakıyor ve her birinin yere ulaşma süresini kronometreyle ölçüyor. Tabloda “yükseklik” helikopterin bırakıldığı yüksekliği, “süre” ise yere ulaşma süresini göstermektedir.',
 [('Bu deneyde bağımsız değişken kanat uzunluğudur.',True,'Kanat uzunluğunu öğrenci kendisi değiştirir; bağımsız değişken budur.'),
  ('Bu deneyde bağımlı değişken düşme süresidir.',True,'Düşme süresi, kanat uzunluğuna bağlı olarak ölçülen niceliktir; bağımlı değişkendir.'),
  ('Kâğıt türü ve bırakma yüksekliği kontrol değişkenleridir.',True,'Tabloda kâğıt türü (A4) ve yükseklik (2,0 m) tüm deneylerde aynıdır; sabit tutulan bu etkenler kontrol değişkenidir.')],
 'Buna göre, bu yargılardan hangileri doğrudur?',S1,
 tipId=TIP['dg'][0],tip=TIP['dg'][1],z='orta',alt=ALT4,kaz='Bir deneyde bağımlı, bağımsız ve kontrol değişkenlerini belirler.',
 kart='K-FZFG2-08 (değişken türleri, kâğıt helikopter) · tablo, öncüllü',istenen='Doğru olan yargılar.',kalip='tablo',ip=['Tabloda hangi sütunun değerleri deneyden deneye değişiyor, hangileri hep aynı; ölçülen sütun hangisi?'],
 bilgi=[B('Değişken türleri','bağımsız değişken deneyde bilerek değiştirilen etkendir; bağımlı değişken ölçülen sonuçtur; kontrol değişkenleri sabit tutulan etkenlerdir. Örnek: bitkinin boyuna ışığın etkisinde ışık süresi bağımsız, boy bağımlı, su miktarı kontrol değişkenidir')],
 puf='Değiştirdiğin etken bağımsız, ölçtüğün sonuç bağımlı, sabit tuttuklarının hepsi kontrol değişkenidir.',sekil=SK8)

# ================= 09 · kontrollü deney ikilileri, tablo · zor · öncüllü =================
K(9,'dg',ALT4,'Bir etkenin etkisi, yalnız o etkenin farklı olduğu iki deneyin karşılaştırılmasıyla incelenir.','Birden çok etkenin değiştiği ikiliyi geçerli saymak.','orta','tablo',4)
DE={'K':(200,500,20),'L':(400,500,20),'M':(400,1000,20),'N':(400,1000,40)}
def fark(a,b): return [i for i in range(3) if DE[a][i]!=DE[b][i]]
assert fark('K','L')==[0] and fark('L','N')==[1,2] and fark('M','N')==[2] and fark('L','M')==[1]
SK9=tablo_svg(['Deney','Su kütlesi (g)','Isıtıcı gücü (W)','Başlangıç sıcaklığı (°C)'],[[k,*v] for k,v in DE.items()])
onc('0009','Bir öğrenci, elektrikli bir ısıtıcıyla ısıtılan suyun kaynama süresini etkileyen etkenleri araştırıyor. Her deneyde aynı cins ve aynı büyüklükte bir kap kullanıyor; kabın içindeki suyun kütlesini, ısıtıcının gücünü ve suyun başlangıç sıcaklığını tabloda gösterildiği gibi değiştiriyor. Daha sonra hangi etkenin kaynama süresine etkisini incelemek için hangi deneylerin kullanılabileceğini yazıyor.',
 [('K ve L deneyleri, su kütlesinin kaynama süresine etkisini incelemek için kullanılabilir.',True,'K ile L’de yalnız su kütlesi farklıdır (200 g, 400 g); ısıtıcı gücü ve başlangıç sıcaklığı aynıdır.'),
  ('L ve N deneyleri, ısıtıcı gücünün kaynama süresine etkisini incelemek için kullanılabilir.',False,'L ile N’de ısıtıcı gücü ve başlangıç sıcaklığı birlikte farklıdır; iki etken birlikte değiştiğinden gücün etkisi ayrılamaz.'),
  ('M ve N deneyleri, başlangıç sıcaklığının kaynama süresine etkisini incelemek için kullanılabilir.',True,'M ile N’de yalnız başlangıç sıcaklığı farklıdır (20 °C, 40 °C); su kütlesi ve ısıtıcı gücü aynıdır.')],
 'Buna göre, bu yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III'],
 tipId=TIP['dg'][0],tip=TIP['dg'][1],z='orta',alt=ALT4,kaz='Kontrollü deneyde yalnız incelenen etkenin değiştiği deney ikililerini belirler.',
 kart='K-FZFG2-09 (kontrollü deney ikilileri, ısıtıcı) · tablo, öncüllü',istenen='Doğru olan yargılar.',kalip='tablo',ip=['Her ikili için üç sütunu karşılaştır; kaç etkenin farklı olduğuna bak.'],
 bilgi=[B('Kontrollü deney','bir etkenin etkisi incelenirken iki deney arasında yalnız o etken farklı olmalı, diğerleri aynı kalmalıdır. Örnek: pil sayısının lamba parlaklığına etkisi için lambalar özdeş, bağlantı aynı tutulur')],
 puf='Etkisi incelenen etken dışındaki her şeyin aynı olduğu iki deney karşılaştırılır.',sekil=SK9)

# ================= 10 · cetvelle uzunluk ölçme · kolay =================
K(10,'oh',ALT3,'Cismin uzunluğu cetvelde iki ucun okunan değerlerinin farkıdır; ölçüm mm duyarlığıyla okunur.','Yalnız sağ ucu okumak; iki ucu toplamak; mm basamağını atmak.','kolay','şekilli',3)
bas,bit=Fr(20,10),Fr(96,10); uz=bit-bas
assert uz==Fr(76,10) and bit==Fr(96,10) and bas+bit==Fr(116,10)
cu=.7; o=[]
o.append(f'\\draw[thick,fill=gray!10] (-.3,0) rectangle ({12*cu+.3:.2f},-.95);')
o.append(f'\\draw[thick,fill=vurgu!20] ({float(bas)*cu:.3f},0) rectangle ({float(bit)*cu:.3f},.5);')
tk=[]
for i in range(0,121):
    Ln=.38 if i%10==0 else (.27 if i%5==0 else .17); tk.append(f'({i*cu/10:.2f},0) -- ({i*cu/10:.2f},{-Ln})')
o.append('\\draw '+' '.join(tk)+';')
for v in range(0,13): o.append(f'\\node[font=\\scriptsize] at ({v*cu:.3f},-.6) {{${v}$}};')
o.append(f'\\node[font=\\scriptsize,right] at ({12*cu+.35:.2f},-.6) {{cm}};')
SK10=sk(*o,sc=1.0)
q('0010',tipId=TIP['oh'][0],tip=TIP['oh'][1],z='kolay',alt=ALT3,kaz='Cetvelde ölçüm yaparken uç değerlerin farkını mm duyarlığıyla okur.',
 kart='K-FZFG2-10 (cetvelle uzunluk okuma) · uç farkı',kalip='şekilli',
 metin='Bir öğrenci, kalemin uzunluğunu ölçmek için kalemi şekildeki gibi cetvelin kenarına yerleştiriyor. Cetvelin en küçük bölmesi 1 mm’dir. Öğrenci kalemin sol ucunun cetvelin sıfır çizgisiyle çakışmadığını fark ediyor ve uzunluğu doğru bulmak için iki ucun okuma değerlerini birlikte kullanıyor.\nBuna göre kalemin uzunluğu kaç cm’dir?',
 sekil=SK10,dogru=Fr(76,10),yan=[(Fr(80,10),'Sonucu en yakın tam sayıya yuvarlamış: 7,6 ≈ 8; ölçüm mm duyarlığıyla okunmalıdır.','dikkat'),(Fr(90,10),'Sağ ucu yalnız tam cm olarak okumuş (9); sol ucu çıkarmamış ve mm basamağını atmış.','dikkat'),(Fr(96,10),'Yalnız sağ ucun okumasını (9,6) alıp sol ucun 2,0 cm’de olduğunu hesaba katmamış.','dikkat'),(Fr(116,10),'İki ucun okumasını toplamış: 2,0 + 9,6; uzunluk için fark alınır.','islem')],
 istenen='Kalemin uzunluğu (cm).',ip=['Kalemin her iki ucunun cetveldeki yerini mm duyarlığıyla oku; uzunluk bu iki okumanın nasıl bir birleşimidir?'],
 bilgi=[B('Cetvelle ölçme','cismin bir ucu sıfıra getirilmediyse uzunluk, sağ uç okuması ile sol uç okumasının farkıdır; okuma en küçük bölme kadar duyarlıdır. Örnek: uçlar 1,5 cm ve 4,0 cm’de ise uzunluk 2,5 cm’dir')],
 ad=[A('Sol ucu oku','Sol uç 2 cm çizgisine denk gelir.','sol uç: 2,0 cm'),A('Sağ ucu oku','Sağ uç 9 cm’den sonraki 6. mm çizgisindedir.','sağ uç: 9,6 cm'),A('Farkı al','Uzunluk iki okumanın farkıdır.','9,6 − 2,0 = 7,6 cm')],
 puf='Cismin ucu sıfır çizgisinde değilse iki uç okumasının farkını al ve mm basamağını unutma.')

# ================= 11 · hipotez · orta · öncüllü =================
K(11,'by',ALT4,'Hipotez sınanabilir olmalı; deney sonucu hipotezi desteklemezse hipotez gözden geçirilir; desteklenen hipotez de yeni deneylerle tekrar sınanabilir.','Bir kez desteklenen hipotezi kesin doğru saymak.','orta','öncüllü',3)
onc('0011','Bir öğrenci, otomobil lastiğinin sıcaklığı arttıkça lastikteki hava basıncının da arttığını düşünüyor ve “Aynı hacimdeki hava ısındıkça basıncı artar.” hipotezini kuruyor. Bu hipotezi sınamak için bir deney düzeneği hazırlıyor ve ölçümlerini yapıyor. Fen bilgisi öğretmeni, öğrencinin çalışmasını değerlendirirken bilimsel hipotezlerle ilgili şu yargıları sıralıyor.',
 [('Hipotez, deneyle sınanabilecek biçimde kurulmalıdır.',True,'Bilimsel hipotez deney ya da gözlemle sınanabilir olmalıdır; sınanamayan tahmin bilimsel hipotez sayılmaz.'),
  ('Deney sonuçları hipotezle uyuşmuyorsa hipotez gözden geçirilir ya da değiştirilir.',True,'Veriler hipotezi desteklemiyorsa hipotez yeniden düşünülür; yeni bir hipotez kurulup sınanabilir.'),
  ('Bir deneyde desteklenen hipotezin yeniden sınanmasına gerek kalmaz.',False,'Desteklenen bir hipotez de farklı koşullarda ve tekrarlanan deneylerle yeniden sınanabilir; tek deney kesinlik sağlamaz.')],
 'Buna göre, bu yargılardan hangileri doğrudur?',S2,goster=True,
 tipId=TIP['by'][0],tip=TIP['by'][1],z='orta',alt=ALT4,kaz='Hipotezin özelliklerini ve deney sonucuyla ilişkisini değerlendirir.',
 kart='K-FZFG2-11 (hipotez özellikleri) · öncüllü',istenen='Doğru olan yargılar.',ip=['Bir hipotezin neden deneyle sınanabilmesi gerektiğini ve sonuçların hipotezle çelişmesi hâlinde ne yapılacağını düşün.'],
 bilgi=[B('Hipotez','gözleme dayanan, deney ya da gözlemle sınanabilen tahmindir. Veriler desteklerse güç kazanır, desteklemezse değiştirilir. Örnek: “Tuz suda çözününce suyun kaynama süresi uzar.” sınanabilir bir hipotezdir')],
 puf='Hipotez sınanabilir olmalı; veriler çelişirse hipotez değişir, desteklense de yeniden sınanabilir.')

# ================= 12 · ölçü aletleri çizimi · orta · öncüllü =================
K(12,'tt',ALT3,'Dinamometre kuvveti (türetilmiş), termometre sıcaklığı ve kronometre zamanı (temel) ölçer; hangi aletle temel nicelik ölçüldüğü ayırt edilir.','Dinamometreyle ölçülen kuvveti temel nicelik saymak.','orta','şekilli',3)
dn=[]
dn.append('\\draw[thick] (0,0.4) rectangle (.55,2.6); \\draw[thick] (.275,.4) -- (.275,-.1); \\draw[thick] (.275,2.6) -- (.275,3.05); \\draw[thick] (.275,3.05) circle (.07);')
dn.append('\\draw[thick] (.275,2.5) -- (.12,2.3) -- (.43,2.05) -- (.12,1.8) -- (.43,1.55) -- (.12,1.3) -- (.275,1.1);')
dn.append('\\draw[thick,fill=gray!30] (.0,-.8) rectangle (.55,-.1);')
tm=[]
tm.append('\\draw[thick] (3.0,.9) -- (3.0,3.0) arc[start angle=180,end angle=0,radius=.1] -- (3.2,.9);')
tm.append('\\draw[thick,fill=vurgu!30] (3.1,.7) circle (.28);')
tm.append('\\fill[vurgu!30] (3.0,.9) rectangle (3.2,1.9); \\draw (3.0,.9) -- (3.0,1.9); \\draw (3.2,.9) -- (3.2,1.9);')
for i in range(0,11): tm.append(f'\\draw (3.2,{1.0+i*.19:.2f}) -- ({3.2+(.22 if i%5==0 else .12)},{1.0+i*.19:.2f});')
kr=[]
kr.append('\\draw[thick,fill=white] (6.2,1.5) circle (.85); \\draw[thick] (6.2,2.35) -- (6.2,2.7); \\draw[thick] (5.95,2.7) rectangle (6.45,2.85);')
for i in range(12): kr.append(f'\\draw ({6.2+.7*math.sin(i*math.pi/6):.3f},{1.5+.7*math.cos(i*math.pi/6):.3f}) -- ({6.2+.8*math.sin(i*math.pi/6):.3f},{1.5+.8*math.cos(i*math.pi/6):.3f});')
kr.append('\\draw[thick] (6.2,1.5) -- (6.55,1.95); \\fill (6.2,1.5) circle (1.5pt);')
SK12=sk(*dn,*tm,*kr,'\\node[font=\\small] at (.275,-1.25) {I};','\\node[font=\\small] at (3.1,-1.25) {II};','\\node[font=\\small] at (6.2,-1.25) {III};',
 '\\node[font=\\scriptsize,align=center] at (.275,-1.75) {dinamometre};','\\node[font=\\scriptsize,align=center] at (3.1,-1.75) {termometre};','\\node[font=\\scriptsize,align=center] at (6.2,-1.75) {kronometre};',sc=1.05)
onc('0012','Fizik laboratuvarında bir öğrenci, şekilde I, II ve III ile numaralandırılmış ölçü aletlerini kullanarak her aletin ölçtüğü niceliği defterine yazıyor. Öğretmeni, bu niceliklerin SI birim sistemindeki yerini sorgulayarak öğrencinin hangi aletlerle temel nicelik ölçtüğünü belirlemesini istiyor.',
 [('I numaralı aletle ölçülen nicelik temel bir niceliktir.',False,'Dinamometre kuvveti (ağırlığı) ölçer; kuvvet kg·m/s² birimiyle türetilmiş bir niceliktir.'),
  ('II numaralı aletle ölçülen nicelik temel bir niceliktir.',True,'Termometre sıcaklığı ölçer; sıcaklık başka niceliklerden türetilemeyen temel niceliktir (SI birimi kelvin).'),
  ('III numaralı aletle ölçülen nicelik temel bir niceliktir.',True,'Kronometre zamanı ölçer; zaman temel niceliktir (SI birimi saniye).')],
 'Buna göre, bu yargılardan hangileri doğrudur?',['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],
 tipId=TIP['tt'][0],tip=TIP['tt'][1],z='orta',alt=ALT3,kaz='Ölçü aletlerinin ölçtüğü niceliklerin temel ya da türetilmiş olduğunu belirler.',
 kart='K-FZFG2-12 (ölçü aleti–temel nicelik) · şekilli, öncüllü; aletler yalnız şekilde',istenen='Doğru olan yargılar.',kalip='şekilli',ip=['Her aletin hangi niceliği ölçtüğünü yaz; sonra o niceliğin başka niceliklerden türetilip türetilmediğine bak.'],
 bilgi=[B('Temel nicelikler','uzunluk, kütle, zaman, sıcaklık gibi nicelikler başka niceliklerden türetilemez. Kuvvet gibi niceliklerin birimi temel birimlerin birleşiminden oluşur. Örnek: metre ölçen cetvel temel nicelik (uzunluk) ölçer')],
 puf='Zaman ve sıcaklık temel niceliktir; dinamometreyle ölçülen kuvvet ise türetilmiş niceliktir.',sekil=SK12)

# ================= 13 · birim tutarlılığı, tablo · zor =================
K(13,'bt',ALT3,'Bir bağıntının her iki yanındaki birimler temel birimlerle yazılıp karşılaştırılır; birimleri uyuşmayan bağıntı doğru olamaz.','Zaman üssünü ya da bir çarpanı atlamak; gücün (W) ve işin (J) birimini karıştırmak.','orta','tablo',5)
U={'x':(0,1,0),'v':(0,1,-1),'a':(0,1,-2),'t':(0,0,1),'m':(1,0,0),'F':(1,1,-2),'E':(1,2,-2)}
def carp(*xs):
    return tuple(sum(U[x][i] for x in xs) for i in range(3))
def bol(a,b): return tuple(U[a][i]-U[b][i] for i in range(3))
assert bol('x','t')!=U['x'] and bol('x','t')==U['v'] and U['v']!=U['a']          # x = v ÷ t ve a = x ÷ t kontrolü aşağıda
assert U['x']!=tuple(U['v'][i]-U['t'][i] for i in range(3))                       # x = v ÷ t tutarsız
assert U['v']!=tuple(U['a'][i]+2*U['t'][i] for i in range(3))                     # v = a × t² tutarsız
assert U['F']!=carp('m','v')                                                       # F = m × v tutarsız
assert U['a']!=bol('x','t')                                                        # a = x ÷ t tutarsız
assert U['E']==carp('F','v','t')                                                   # E = F × v × t tutarlı
assert U['E']!=carp('F','v')                                                       # F × v birimi güçtür
SK13=tablo_svg(['Nicelik','Sembol','SI temel birimleriyle'],[['Yer değiştirme','x','m'],['Hız','v','m/s'],['İvme','a','m/s²'],['Zaman','t','s'],['Kütle','m','kg'],['Kuvvet','F','kg·m/s²'],['İş','E','kg·m²/s²']])
q('0013',tipId=TIP['bt'][0],tip=TIP['bt'][1],z='orta',alt=ALT3,kaz='Bir bağıntının iki yanındaki birimleri temel birimlerle karşılaştırarak tutarlılığını sınar.',
 kart='K-FZFG2-13 (birim tutarlılığı) · tablo',kalip='tablo',
 metin='Bir öğrenci, fizik bağıntılarının doğruluğunu kontrol etmek için her bağıntının iki yanındaki niceliklerin birimini SI temel birimleriyle yazıp karşılaştırıyor. Kullanacağı niceliklerin sembolleri ve temel birimleri tabloda verilmiştir.\nBir bağıntının doğru olabilmesi için iki yanının biriminin aynı olması gerektiğine göre, aşağıdaki bağıntılardan hangisinin her iki yanının birimi aynıdır?',
 sekil=SK13,dogru='E = F × v × t',sira=['E = F × v × t','x = v ÷ t','v = a × t²','F = m × v','a = x ÷ t'],
 yan=[('x = v ÷ t','Sağ yan (m/s) ÷ s = m/s² olur ve ivme birimindedir; sol yan uzunluk (m) birimindedir, uyumsuzdur.','islem'),('v = a × t²','Sağ yan m/s² × s² = m olur, hız birimi (m/s) değildir; zaman üssünü yanlış almış.','islem'),('F = m × v','Sağ yan kg × m/s = kg·m/s olur; kuvvet birimi kg·m/s²’dir, zaman üssü eksiktir.','dikkat'),('a = x ÷ t','Sağ yan m ÷ s = m/s olur; ivmenin birimi m/s²’dir, bir saniye bölmesi daha gerekir.','islem')],
 istenen='Her iki yanının birimi aynı olan bağıntı.',ip=['Seçeneklerin sağ yanını temel birimlerle yaz ve sol yandaki niceliğin birimiyle karşılaştır.'],
 bilgi=[B('Birim kontrolü','bir bağıntının iki yanı aynı birimdeyse bağıntı birim bakımından tutarlıdır; çarpmada birimler çarpılır, bölmede bölünür. Örnek: yol = hız × zaman için (m/s) × s = m olduğundan tutarlıdır')],
 ad=[A('Tabloyu oku','Her niceliğin temel birimini yan yana yaz.','x: m ; v: m/s ; a: m/s² ; t: s'),A('Bölme içerenleri ele','x = v ÷ t ve a = x ÷ t bağıntılarının sağ yanlarını hesapla.','(m/s) ÷ s = m/s² ≠ m ; m ÷ s = m/s ≠ m/s²'),A('Diğer ikisini ele','v = a × t² ve F = m × v bağıntılarının sağ yanlarını yaz.','m/s² × s² = m ≠ m/s ; kg × m/s = kg·m/s ≠ kg·m/s²'),A('Kalan bağıntıyı sına','E = F × v × t için üç niceliğin birimlerini çarp.','kg·m/s² × m/s × s = kg·m²/s²'),A('Sonuç','Bu birim işin birimiyle aynıdır.','E = F × v × t')],
 puf='Her bağıntıyı temel birimlerle yaz; iki yanda m, kg ve s üsleri birebir aynı olmalı.')

# ================= 14 · bilim araştırma merkezleri · kolay =================
K(14,'mr',ALT5,'CERN parçacık hızlandırıcılarıyla temel fizik araştırması, NASA uzay ve havacılık, TÜBİTAK Türkiye’de bilimsel ve teknolojik araştırmaları destekleyen kurumdur.','Kurumların kuruluş amaçlarını birbirine karıştırmak.','kolay','düz',2)
D1='CERN – parçacık hızlandırıcılarıyla temel fizik araştırması'
q('0014',tipId=TIP['mr'][0],tip=TIP['mr'][1],z='kolay',alt=ALT5,kaz='Bilim araştırma merkezlerini kuruluş amaçlarıyla eşleştirir.',
 kart='K-FZFG2-14 (CERN, NASA, TÜBİTAK) · eşleştirme',kalip='düz',
 metin='Bir öğrenci, fizik dersi için bilimsel araştırma kurumlarını tanıtan bir poster hazırlıyor. Posterde CERN, NASA ve TÜBİTAK kurumlarının her biri için o kurumun kuruluş amacına uygun bir çalışma alanı yazacaktır. Öğrenci, posterine yazacağı eşleştirmeleri öğretmenine danışıyor.\nBuna göre aşağıdaki eşleştirmelerden hangisi doğrudur?',
 dogru=D1,
 sira=['NASA – parçacık hızlandırıcılarıyla temel fizik araştırması','TÜBİTAK – uzaya araç gönderme ve gök cismi araştırması',D1,'CERN – uzaya araç gönderme ve gök cismi araştırması','NASA – Türkiye’deki bilimsel araştırmaları destekleme'],
 yan=[('NASA – parçacık hızlandırıcılarıyla temel fizik araştırması','NASA’yı CERN ile karıştırmış; NASA uzay ve havacılık araştırmaları yapan kurumdur.','bilgi'),('TÜBİTAK – uzaya araç gönderme ve gök cismi araştırması','TÜBİTAK’ı NASA ile karıştırmış; TÜBİTAK Türkiye’de bilimsel ve teknolojik araştırmaları destekleyen kurumdur.','bilgi'),('CERN – uzaya araç gönderme ve gök cismi araştırması','CERN’ü NASA ile karıştırmış; CERN parçacık fiziği araştırmaları yapar.','bilgi'),('NASA – Türkiye’deki bilimsel araştırmaları destekleme','NASA’yı TÜBİTAK ile karıştırmış; Türkiye’deki araştırmaları destekleyen kurum TÜBİTAK’tır.','bilgi')],
 istenen='Doğru kurum–çalışma alanı eşleştirmesi.',ip=['Her kurumun kuruluş amacını ayrı ayrı hatırla.'],
 bilgi=[B('Bilim araştırma merkezleri','CERN parçacık hızlandırıcılarıyla maddenin yapısını, NASA uzay ve havacılığı inceler; TÜBİTAK Türkiye’de bilimsel ve teknolojik araştırmaları destekleyen ve yürüten kurumdur. Örnek: bir uzay teleskobunun fırlatılması NASA’nın çalışma alanındadır')],
 ad=[A('Kurumları tanı','Her kurumun çalışma alanını hatırla.','CERN: parçacık fiziği ; NASA: uzay ; TÜBİTAK: Türkiye’de bilim ve teknoloji'),A('Şıkları eşleştir','Her şıktaki kurum ile çalışma alanını karşılaştır.','yalnız CERN – parçacık hızlandırıcıları eşleşmesi doğru'),A('Sonuç','Doğru eşleştirme CERN ile parçacık hızlandırıcılarıdır.','CERN – parçacık hızlandırıcıları')],
 puf='CERN parçacık fiziği, NASA uzay, TÜBİTAK Türkiye’deki bilim ve teknoloji araştırmaları ile anılır.')

H.bitir(P,'fizikgirisiki','fiz|Fizik Bilimine Giriş')
