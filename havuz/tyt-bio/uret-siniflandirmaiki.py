"""TYT Biyoloji · Canlıların Sınıflandırılması · ek paket (siniflandirmaiki): 24 soru, kardeş yok, ipucu 1.
Dallanma şemalarının (soy ağacı) özellik/akrabalık yargıları, dikotom anahtar yürütmeleri, tür kavramı (bölüntü taraması) ve
öncül doğrulukları Python'da hesaplanır; her doğru şık ve çeldirici değeri assert edilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır."""
import sys,os,itertools
BD=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,BD)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Canlıların Sınıflandırılması'; UK='bio|Canlıların Sınıflandırılması'
H.KONU=KONU_
P=Parti('siniflandirmaiki',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji dağılımı (yalnız mantık) · MEB 9. sınıf Canlıların Sınıflandırılması'
TP={'basamak':('by-sn2-basamak','Sınıflandırma basamakları ve hiyerarşi'),'adlandirma':('by-sn2-adlandirma','İkili adlandırma ve tür kavramı'),
    'dallan':('by-sn2-dallan','Dallanma (soy) şeması yorumu'),'anahtar':('by-sn2-anahtar','Dikotom anahtar'),
    'alem':('by-sn2-alem','Âlemler ve virüsler'),'bitki':('by-sn2-bitki','Bitkilerin sınıflandırılması'),
    'hayvan':('by-sn2-hayvan','Hayvanların sınıflandırılması'),'onem':('by-sn2-onem','Canlıların ekonomik ve ekolojik önemi')}
def q(no,tp,z,alt,kaz,kalip,fikir,tuzak,ne,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    tipId,tip=TP[tp]
    kart(f'K-BYSN2-{no}',alt,fikir,tuzak,z,kalip,len(ad),tipId,tip,KY)
    mk(P,'00'+no,ad=ad,adim=len(ad),tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-BYSN2-{no} ({tip.lower()}) · {ne}',**k)
def cap(s): return ('İ' if s[0]=='i' else s[0].upper())+s[1:]
SETS=[{'I'},{'II'},{'III'},{'I','II'},{'I','III'},{'II','III'},{'I','II','III'}]
ISIM=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def onc(d,idx,harf,ara=True):
    """d: {'I':(bool,olgu)}; ara=True doğru olanlar, False yanlış olanlar sorulur; idx: 5 kanonik seçenek sırası; doğru şık harfi assert edilir."""
    T={k for k,v in d.items() if v[0]==ara}; ci=[i for i,s in enumerate(SETS) if s==T]; assert len(ci)==1,T
    ci=ci[0]; assert len(idx)==5 and list(idx)==sorted(set(idx)) and ci in idx and 'ABCDE'[idx.index(ci)]==harf,(T,idx,harf)
    yan=[]
    for i in idx:
        if i==ci: continue
        p=[]
        for x in sorted(SETS[i]^T):
            p.append(f'{x} öncülünü '+('yanlış' if d[x][0] else 'doğru')+f' sanmış; oysa {d[x][1]}')
        yan.append((ISIM[i],'. '.join(p)+'.','bilgi'))
    return dict(dogru=ISIM[ci],yan=yan,sira=[ISIM[i] for i in idx])
def adim_onc(d,keys):
    return A('. '.join(keys)+'. öncül' if len(keys)==1 else ' ve '.join(keys)+'. öncüller',' '.join(cap(d[k][1])+'.' for k in keys),' · '.join(f'{k}: '+('doğru' if d[k][0] else 'yanlış') for k in keys))
def sonuc(d,r,ara=True):
    return A('Sonucu yaz','Sorulan türdeki öncüller bir arada yazılır.',' · '.join(f'{k}: '+('doğru' if v[0] else 'yanlış') for k,v in d.items())+' · Sonuç: '+r['dogru'])
def tek(S,hedef,tur='bilgi'):
    """S: [(metin,bool,neden)] 5 adet; hedef=True: tek doğru, False: tek yanlış (söylenemez/yanlıştır). Döner: dogru,yan,sira."""
    assert len(S)==5; h=[s for s in S if s[1]==hedef]; assert len(h)==1,[s[0] for s in S if s[1]==hedef]
    yan=[]
    for m,b,n in S:
        if b==hedef: continue
        yan.append((m,('Bu ifadeyi doğru sanmış; oysa '+n) if hedef else ('Bu ifadeyi yanlış sanmış; oysa '+n),tur))
    return h[0][0],yan,[s[0] for s in S]
def tk(g,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,g))

# ---------- bilgi kartları ----------
HIY=B('Sınıflandırma basamakları','Basamaklar tür, cins, familya, takım, sınıf, şube ve âlem sırasıyla büyür · Sınıflandırma hiyerarşiktir: her basamak bir üst basamağın içinde yer alır')
IKI=B('İkili adlandırma','Canlının bilimsel adı cins adı + tür adından oluşur (Linne). Cins adı büyük, tür adı küçük harfle başlar; adlar Latince yazılır, basılı metinde eğik yazılır · Örnek: Homo sapiens adında Homo cins adı, sapiens tür adıdır')
TUR=B('Tür kavramı','Tür, doğal ortamda birbiriyle çiftleşip verimli (üreme yeteneği olan) döl verebilen bireyler topluluğudur · Verimsiz (kısır) döl ya da döl oluşmaması, bireylerin farklı türlerden olduğunu gösterir')
DAL=B('Dallanma şeması','Dallanma şeması canlılar arasındaki akrabalığı gösterir · Dalların ayrıldığı noktalar ortak ataları temsil eder')
DIK=B('Dikotom anahtar','Her basamakta iki seçenek (evet/hayır) vardır; canlının özelliğine uyan seçeneğin yönlendirdiği basamağa gidilerek canlı grubuna ulaşılır · Bir basamaktaki ifade, iki yolu yalnızca bir grubun taşıdığı özellikle ayırmalıdır')
ALM=B('Âlemlerin özellikleri','Bakteriler ve arkeler prokaryottur (çekirdek zarı yok) · Protista, mantarlar, bitkiler ve hayvanlar ökaryottur · Mantarlar heterotrof, hücre duvarı kitindir · Bitkiler ototrof, hücre duvarı selülozdur · Hayvanlarda hücre duvarı yoktur')
VIR=B('Virüsler','Virüsler nükleik asit ve protein kılıftan oluşur · Çoğalmak için canlı bir konak hücreye gerek duyarlar')
ARK=B('Arkeler','Arkeler ve bakteriler prokaryot hücrelidir; çekirdek zarı ve zarlı organelleri yoktur · Arkeler bakterilerden ayrı bir âlemde incelenir · Bazı arkeler aşırı tuzlu, sıcak ya da asidik ortamlarda yaşar')
BIT=B('Bitki grupları','Bitkiler damarlı ve damarsız olarak, damarlılar tohumsuz ve tohumlu olarak, tohumlular açık ve kapalı tohumlu olarak gruplandırılır · Tohumsuz bitkiler sporla ürer')
OMG=B('Omurgalı sınıfları','Omurgalılar balıklar, iki yaşamlılar, sürüngenler, kuşlar ve memeliler olarak sınıflandırılır · Sınıflar vücut sıcaklığı, kalp yapısı, solunum organı ve vücut örtüsü gibi özelliklerle ayırt edilir')
OMS=B('Omurgasız eklembacaklılar','Eklembacaklılar böcekler, örümceksiler, kabuklular ve çok ayaklılar gibi gruplara ayrılır · Gruplar bacak sayısı, anten ve vücut bölümü sayısıyla ayırt edilir')
ONEM=B('Ekolojik ve ekonomik önem','Üreticiler besin zincirinin ilk halkasıdır; ayrıştırıcılar organik atıkları inorganik maddelere dönüştürür · Bazı bakteri ve mantarlardan gıda üretiminde ve ilaç elde edilmesinde yararlanılır')

# ================= 0001 · nested sets · kolay · olumsuz =================
SK=[r'\draw[line width=1.3pt] (0,0) ellipse (5.3 and 2.6);',
    r'\draw[line width=1.3pt] (-1.7,-.1) ellipse (2.4 and 1.7);',
    r'\draw[line width=1.3pt] (-2.3,-.15) ellipse (1.1 and .8);',
    r'\draw[line width=1.3pt] (2.9,-.1) ellipse (1.4 and 1.1);',
    r'\node[font=\large\bfseries] at (-4.7,.3) {K};\node[font=\large\bfseries] at (-1.7,1.05) {L};\node[font=\large\bfseries] at (-2.3,-.15) {M};\node[font=\large\bfseries] at (2.9,-.1) {N};']
SK1=tk('\n'.join(SK),.8)
S1=[("M’deki canlıların kendi aralarındaki ortak özellik sayısı, L’deki canlılarınkinden fazladır.",True,'M kümesi L’nin içinde daha dar bir basamaktır; alt basamaktaki canlılar daha çok ortak özellik taşır'),
    ("N’de yer alan bir canlı, L’nin üyesi değildir.",True,'N ile L kümeleri kesişmez; ikisi de K’nin içinde ayrı gruplardır'),
    ("N’deki canlılarla M’deki canlılar arasındaki ortak özellik sayısı, M’deki canlıların kendi aralarındaki ortak özellik sayısından fazladır.",False,'M’deki canlılar ortak özellikleri en çok kendi aralarında paylaşır; N ile ortak özellikler yalnız K düzeyindedir ve daha azdır'),
    ("M’de yer alan her canlı aynı zamanda K’nin de üyesidir.",True,'M, L’nin; L ise K’nin içindedir; alt basamaktaki canlılar üst basamaklara da dahildir'),
    ("K, L’ye göre daha üst bir sınıflandırma basamağıdır.",True,'K, L’yi kapsadığı için daha üst basamaktır')]
d1,y1,s1=tek(S1,False)
q('01','basamak','kolay','Sınıflandırma hiyerarşisi','Sınıflandırma basamaklarında üstten alta ortak özelliklerin arttığını iç içe küme şemasından yorumlar.','şekilli',
  'İç içe kümelerde alta inildikçe küme küçülür, canlıların ortak özellik sayısı artar.','N ile M’yi “uzak” sayıp ortak özelliği L–M ilişkisiyle karıştırmak.','iç içe küme şeması ve yanlış ifade',
  [A('Şemayı oku','K en geniş kümedir; L ve N onun içindedir, M ise L’nin içindedir.','K ⊃ L ⊃ M; K ⊃ N'),
   A('Üstten alta ilkesini hatırla','Küme küçüldükçe canlılar daha çok ortak özellik taşır.','M: en çok ortak özellik'),
   A('Her ifadeyi sına','Dört ifade şemayla uyumludur; M ile N yalnız K düzeyinde ortaklık taşır.','M–N ortaklığı < M kendi içinde'),
   A('Yanlışı seç','Ortak özelliğin daha fazla olduğunu söyleyen ifade yanlıştır.','Söylenemeyen ifade bulundu')],
  metin='Bir biyoloji öğretmeni, canlıların sınıflandırılmasındaki hiyerarşiyi göstermek için şekildeki iç içe kümeleri çizmiştir. K, L, M ve N sınıflandırmadaki birer basamağı (taksonu) temsil etmekte; her küme o basamağa ait bütün canlıları kapsamaktadır.\nBuna göre aşağıdaki ifadelerden hangisi söylenemez?',
  dogru=d1,yan=y1,sira=s1,istenen='Şemaya göre söylenemeyen ifade.',sekil=SK1,ip=['Bir kümenin içindeki canlılar hangi kümelerin de üyesidir?'],
  bilgi=[HIY],puf='İç içe kümede içeri girdikçe canlı sayısı azalır, ortak özellik sayısı artar.')

# ================= 0002 · tablo · öncüllü · orta =================
d2={'I':(True,'kurt (Canis lupus) ve tilki (Vulpes vulpes) Canidae familyasında yer alır'),
    'II':(False,'boz ayı Ursus, tilki Vulpes cinsindedir; cins adları farklıdır'),
    'III':(True,'dört canlının takımı da Carnivora olarak verilmiştir')}
r2=onc(d2,[0,1,2,3,4],'E')
K2='\n'.join([r'\draw[line width=1.3pt] (0,0) ellipse (7.4 and 3.4);',r'\draw[line width=1.3pt] (-3.7,-.3) ellipse (3.4 and 2.2);',r'\draw[line width=1.3pt] (3.7,-.3) ellipse (3.4 and 2.2);',
 r'\node[font=\normalsize\bfseries] at (0,2.95) {Takım: Carnivora};\node[font=\normalsize\bfseries] at (-3.7,1.0) {Familya: Ursidae};\node[font=\normalsize\bfseries] at (3.7,1.0) {Familya: Canidae};',
 r'\node[font=\small] at (-3.7,.2) {Boz ayı (Ursus arctos)};\node[font=\small] at (-3.7,-.7) {Kutup ayısı (Ursus maritimus)};',
 r'\node[font=\small] at (3.7,.2) {Kurt (Canis lupus)};\node[font=\small] at (3.7,-.7) {Tilki (Vulpes vulpes)};'])
T2=tk(K2,.68)
q('02','basamak','orta','Cins, familya ve takım','Bilimsel ad ve familya/takım bilgilerinden canlıların hangi basamakta ortak olduğunu belirler.','şekilli',
  'Bilimsel adın ilk sözcüğü cinsi verir; familya ve takım kümeleri üst basamakları gösterir; ortaklık basamağı kümelerden okunur.','Aynı takımdaki canlıları aynı cinste sanmak.','iç içe küme şeması: familya ve takım',
  [adim_onc(d2,['I']),adim_onc(d2,['II']),adim_onc(d2,['III']),sonuc(d2,r2)],
  metin='Bir doğa bilimleri müzesinde dört memeli hayvanın sınıflandırmadaki yeri, bilimsel adları ve bağlı oldukları familya ile takım iç içe kümelerle şekilde gösterilmiştir.\nBuna göre,\nI. Kurt ile tilki aynı familyadadır.\nII. Boz ayı ile tilki aynı cinstedir.\nIII. Dört canlı da aynı takımda yer alır.\nifadelerinden hangileri doğrudur?',
  dogru=r2['dogru'],yan=r2['yan'],sira=r2['sira'],istenen='Şekle göre doğru olan ifadeler.',sekil=T2,ip=['Cins adı bilimsel adın hangi sözcüğüdür ve hangi canlılar aynı kümededir?'],
  bilgi=[IKI,HIY],puf='Aynı cinsteki canlılar aynı familyada ve takımdadır; ama tersi doğru değildir.')
# 0002 öncül düzeni: Yalnız I, Yalnız II, Yalnız III, I ve II, I ve III → doğru "I ve III" (E)

# ================= 0003 · tür-cins-familya-takım çıkarımı · zor · öncüllü (kesinlikle) =================
def modeller():
    """X,Y,Z,T için (sınıf,takım,familya,cins,tür) etiketleri; her düzeyde 2 değer (hiyerarşik). Koşulları sağlayan tüm düzenler."""
    def eq(a,b,k): return a[:k]==b[:k]       # ilk k düzey aynı
    bir=list(itertools.product((0,1),repeat=5))
    sonuc_=[]
    for X in bir:
        for Y in bir:
            if not (eq(X,Y,4) and X[4]!=Y[4]): continue          # aynı cins, farklı tür
            for Z in bir:
                if not (eq(Y,Z,3) and Y[3]!=Z[3]): continue      # aynı familya, farklı cins
                for T in bir:
                    if eq(Z,T,1) and not eq(Z,T,2): sonuc_.append((X,Y,Z,T))   # aynı sınıf, farklı takım
    return sonuc_
M3=modeller(); assert M3
def ayni(a,b,k): return a[:k]==b[:k]
I3=all(ayni(X,Z,3) for X,Y,Z,T in M3); II3=any(ayni(X,T,2) for X,Y,Z,T in M3); III3=any(ayni(Y,T,3) for X,Y,Z,T in M3)
assert I3 and not II3 and not III3
d3={'I':(True,'X ile Y aynı cinste, Y ile Z aynı familyadadır; bu yüzden X ile Z de aynı familyadadır'),
    'II':(False,'X ile Z aynı takımdadır, Z ile T farklı takımdadır; bu yüzden X ile T aynı takımda olamaz'),
    'III':(False,'Y ile Z aynı familyadadır, Z ile T farklı takımdadır; bu yüzden Y ile T aynı familyada olamaz')}
r3=onc(d3,[0,1,2,3,4],'A')
q('03','basamak','zor','Basamaklar arası çıkarım','Verilen ortaklık bilgilerinden başka canlılar arasındaki basamak ilişkilerini kesin olarak çıkarır.','öncüllü',
  'Alt basamakta ortak olan canlılar bütün üst basamaklarda da ortaktır; üst basamakta ayrılanlar alt basamakta da ayrıdır.','Ayrı takımdaki canlıların aynı familyada olabileceğini düşünmek.','basamak zincirinden kesin çıkarım',
  [A('Bilgileri sırala','Cins ortaklığı familya ve takımı da getirir; familya ortaklığı takımı da getirir.','X=Y cins · Y=Z familya'),
   adim_onc(d3,['I']),adim_onc(d3,['II','III']),sonuc(d3,r3)],
  metin='Bir araştırmacı, X, Y, Z ve T adlı dört hayvan türünün sınıflandırma kayıtlarını inceliyor ve şu bilgilere ulaşıyor:\n• X ile Y aynı cinste yer alan farklı türlerdir.\n• Y ile Z aynı familyadadır; ancak farklı cinslerdedir.\n• Z ile T aynı sınıftadır; ancak farklı takımlardadır.\nBu bilgilere göre,\nI. X ile Z aynı familyadadır.\nII. X ile T aynı takımdadır.\nIII. Y ile T aynı familyadadır.\nifadelerinden hangileri kesinlikle doğrudur?',
  dogru=r3['dogru'],yan=r3['yan'],sira=r3['sira'],istenen='Kesinlikle doğru olan ifadeler.',ip=['Bir basamakta ortak olan canlıların daha üst basamaklarda nasıl konumlandığını düşün.'],
  bilgi=[HIY],puf='Ortaklık alt basamaktan üste doğru taşınır; ayrılık üst basamaktan alta doğru taşınır.')

# ================= 0004 · ikili adlandırma · kolay · olumsuz =================
S4=[("Cins adı büyük harfle başlar.",True,'cins adı büyük harfle yazılır'),
    ("Tür adı küçük harfle yazılır.",True,'tür adı küçük harfle başlar'),
    ("Bilimsel adlandırmada Latince kullanılması, farklı dilleri konuşan bilim insanları arasında ortak bir dil sağlar.",True,'bilimsel adlar Latince yazıldığı için ülkeler arasında ortak anlaşma sağlanır'),
    ("Tür adı, cins adı olmadan tek başına yazıldığında da bir canlıyı tek anlamlı olarak tanımlar.",False,'tür adı cins adıyla birlikte anlamlıdır; yalnız tür adı farklı cinslerde de bulunabilir'),
    ("İkili adlandırma sisteminin temelleri Linne tarafından atılmıştır.",True,'ikili adlandırmayı sistemleştiren bilim insanı Linne’dir')]
d4,y4,s4=tek(S4,False)
q('04','adlandirma','kolay','İkili adlandırma','İkili adlandırmanın yazım ve kullanım kurallarını bilir.','düz',
  'İkili ad cins + tür adından oluşur; cins büyük, tür küçük harfle başlar.','Tür adını tek başına yeterli sanmak.','ikili adlandırma kuralları',
  [A('Kuralı hatırla','Bilimsel ad iki sözcüktür: önce cins, sonra tür adı gelir.','cins + tür'),
   A('Yazımı hatırla','Cins adı büyük harfle, tür adı küçük harfle başlar; adlar Latincedir.','Zea mays gibi'),
   A('İfadeleri sına','Dört ifade kurallarla uyumludur; tür adının tek başına kullanımı kurala uymaz.','Tür adı tek başına yetmez'),
   A('Yanlışı seç','Yanlış olan ifade tür adını tek başına yeterli sayan ifadedir.','Yanlış ifade bulundu')],
  metin='Bir lise biyoloji dersinde öğrenciler, mısırın bilimsel adının Zea mays olduğunu öğreniyor ve bilimsel adların neden iki sözcükten oluştuğunu tartışıyor. Öğretmen, ikili adlandırma sistemini anlatan beş ifade yazıyor ve bu ifadelerden yalnızca birinin hatalı olduğunu söylüyor.\nBuna göre hatalı olan ifade aşağıdakilerden hangisidir?',
  dogru=d4,yan=y4,sira=s4,istenen='İkili adlandırmayla ilgili yanlış ifade.',ip=['Bilimsel adı tek anlamlı yapan nedir?'],
  bilgi=[IKI],puf='İkili ad = Cins (büyük harf) + tür (küçük harf); yalnız tür adı yetmez.')

# ================= 0005 · etiketler · öncüllü · kolay =================
d5={'I':(True,'Olea europaea adında cins adı büyük, tür adı küçük harfle başlar'),
    'II':(True,'Pinus nigra adında cins adı büyük, tür adı küçük harfle başlar'),
    'III':(False,'quercus robur adında cins adı küçük harfle başlamış; cins adı büyük harfle yazılmalıdır')}
r5=onc(d5,[2,3,4,5,6],'B')
q('05','adlandirma','kolay','İkili adlandırma yazımı','Bilimsel adların harf büyüklüğü açısından kurallara uygun yazılıp yazılmadığını değerlendirir.','öncüllü',
  'Etiketteki her adın cins ve tür kısmının baş harfleri tek tek denetlenir.','Her sözcüğün baş harfini büyük yazmanın doğru olduğunu sanmak.','bilimsel ad etiketleri',
  [adim_onc(d5,['I']),adim_onc(d5,['II']),adim_onc(d5,['III']),sonuc(d5,r5)],
  metin='Bir herbaryum görevlisi, topladığı bitki örneklerine şu etiketleri yazıyor:\nI. Olea europaea (zeytin)\nII. Pinus nigra (karaçam)\nIII. quercus robur (saplı meşe)\nEtiketlerin yalnızca harf büyüklüğü açısından ikili adlandırma kuralına uygun olup olmadığı denetlenecektir; Latince ve eğik yazım kuralları dikkate alınmayacaktır.\nBuna göre hangi etiketlerin yazımı bu kurala uygundur?',
  dogru=r5['dogru'],yan=r5['yan'],sira=r5['sira'],istenen='Kurala uygun yazılan etiketler.',ip=['Bilimsel adın iki sözcüğünün baş harf yazımı farklı mıdır?'],
  bilgi=[IKI],puf='Bilimsel adda yalnız cins adının baş harfi büyüktür.')

# ================= 0006 · at-eşek-katır · öncüllü olumsuz · orta =================
d6={'I':(True,'at (Equus caballus) ve eşek (Equus asinus) aynı cinste yer alan iki ayrı türdür'),
    'II':(True,'at ile eşekten doğan katırın kısır olması, verimli döl verilemediği için bu iki canlının farklı tür olduğunu gösterir'),
    'III':(False,'at ile eşek çiftleşip döl verebilse de dölün kısır olması, aynı tür olmadıklarını gösterir; verimli döl şarttır')}
r6=onc(d6,[2,3,4,5,6],'A',ara=False)
q('06','adlandirma','orta','Tür kavramı','Verimli döl ölçütüne göre tür kavramını yorumlar.','öncüllü',
  'Tür sınırı, çiftleşmeden değil verimli döl oluşmasından belirlenir.','Döl oluştuysa aynı tür saymak.','at–eşek–katır örneği',
  [adim_onc(d6,['I']),adim_onc(d6,['II']),adim_onc(d6,['III']),sonuc(d6,r6,False)],
  metin='Bir çiftlikte at (Equus caballus) ile eşek (Equus asinus) çiftleştirildiğinde katır adı verilen bir yavru doğuyor. Katırlar sağlıklı ve güçlü olmakla birlikte kendi aralarında çiftleştirildiklerinde döl oluşturamıyor.\nBu durumla ilgili,\nI. At ve eşek aynı cinste yer alan iki farklı türdür.\nII. Katırın kısır olması, at ile eşeğin farklı türler olduğunu gösterir.\nIII. At ile eşek birbirleriyle çiftleşip döl verebildiğine göre aynı türe aittir.\nifadelerinden hangileri yanlıştır?',
  dogru=r6['dogru'],yan=r6['yan'],sira=r6['sira'],istenen='Yanlış olan ifadeler.',ip=['Tür tanımındaki döl ölçütünün hangi iki koşulu içerdiğini düşün.'],
  bilgi=[TUR],puf='Aynı tür olmanın ölçütü verimli döl vermektir; döl oluşması tek başına yetmez.')

# ================= 0007 · çiftleştirme tablosu · tür sayısı · zor =================
CIFT=[('A','B',True,True),('A','C',True,False),('C','D',True,True),('B','D',False,None)]  # (x,y,döl oluştu mu, verimli mi)
def bolunt(l):
    if not l: yield []; return
    f,*r=l
    for p in bolunt(r):
        for i in range(len(p)): yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
def tutarli(part):
    t={x:i for i,g in enumerate(part) for x in g}
    for x,y,dol,ver in CIFT:
        ayni_=t[x]==t[y]
        if ayni_!=(dol and ver): return False
    return True
MODEL7=[p for p in bolunt(list('ABCD')) if tutarli(p)]
assert len(MODEL7)==1 and sorted(map(sorted,MODEL7[0]))==[['A','B'],['C','D']]
T7=tablo_svg(['Çiftleştirilen','Döl oluşumu','Dölün üreme durumu'],[['A × B','Oluştu','Verimli'],['A × C','Oluştu','Kısır'],['C × D','Oluştu','Verimli'],['B × D','Oluşmadı','—']])
SD7='Populasyonlar iki farklı türe aittir; A ile B bir türü, C ile D diğer türü oluşturur.'
Y7=[('Dört populasyon da aynı türe aittir; çünkü çiftleştirmelerin üçünde döl oluşmuştur.','Döl oluşmasını yeterli sayıp dölün verimli olup olmadığına bakmamış; A × C dölü kısırdır.','bilgi'),
    ('A ile C aynı türe aittir; çünkü bu iki populasyonun çiftleşmesinden döl oluşmuştur.','A × C dölünün kısır olduğunu görmemiş; kısır döl, iki populasyonun farklı tür olduğunu gösterir.','dikkat'),
    ('Üç farklı tür vardır; çünkü B × D çiftleşmesinden döl oluşmamıştır.','A ile B ve C ile D ikililerinin verimli döl verdiğini, yani her ikilinin kendi içinde aynı tür olduğunu atlamış.','dikkat'),
    ('Dört populasyon dört farklı türdür; çünkü en az bir çiftleşmeden kısır ya da hiç döl oluşmuştur.','Yalnız kısır dölü görüp verimli döl veren iki ikiliyi (A × B ve C × D) aynı tür saymamış.','bilgi')]
q('07','adlandirma','zor','Tür kavramı','Çiftleştirme sonuçlarından populasyonların kaç türe ait olduğunu çıkarır.','tablo',
  'Verimli döl veren populasyonlar aynı türdür; kısır döl ya da döl yokluğu ayrı tür demektir; tür ilişkisi geçişlidir.','Sadece döl oluşumuna bakmak.','çiftleştirme sonuçları tablosu',
  [A('Aynı türleri bul','Yalnız verimli döl veren çiftler aynı türdür.','A–B ve C–D: verimli'),
   A('Ayrı olanları bul','Kısır döl ya da döl yokluğu farklı tür demektir.','A × C: kısır · B × D: döl yok'),
   A('Geçişliliği kullan','A ile C farklıysa B ile C ve A ile D de farklıdır; tür sayısı kesinleşir.','{A, B} ve {C, D}'),
   A('Sonucu yaz','Dört populasyon iki türe aittir.','2 tür')],
  metin='Bir araştırma ekibi, dört doğal populasyondan (A, B, C ve D) alınan bireyleri laboratuvarda çiftleştirmiş ve sonuçları aşağıdaki tabloda toplamıştır. Her ikilide bireyler çiftleşme isteği göstermiş, tablodaki durumlar dışında başka çiftleştirme yapılmamıştır.\nBuna göre aşağıdakilerden hangisi kesinlikle doğrudur?',
  dogru=SD7,yan=Y7,sira=[Y7[0][0],Y7[2][0],SD7,Y7[1][0],Y7[3][0]],istenen='Tabloya göre kesinlikle doğru olan ifade.',sekil=T7,ip=['Döl oluşumu ile dölün üreme durumunun tür kavramı açısından ne ifade ettiğini düşün.'],
  bilgi=[TUR],puf='Aynı tür = verimli döl; kısır döl ya da döl yokluğu = ayrı tür.')

# ---------- dallanma şeması yardımcıları ----------
class Nd:
    def __init__(s,ad,kids=(),marks=()): s.ad=ad; s.kids=list(kids); s.marks=list(marks)
def yap(n): return [n.ad] if not n.kids else [y for k in n.kids for y in yap(k)]
def yol_(n,hedef,yol=()):
    yol=yol+(n,)
    if not n.kids: return yol if n.ad==hedef else None
    for k in n.kids:
        r=yol_(k,hedef,yol)
        if r: return r
def ozel(root): return {l:{m for nd in yol_(root,l) for m in nd.marks} for l in yap(root)}
def lcad(root,a,b):
    pa,pb=yol_(root,a),yol_(root,b); k=0
    while k<min(len(pa),len(pb)) and pa[k] is pb[k]: k+=1
    return k-1
def yakin(root,a,b,c): return lcad(root,a,b)>lcad(root,a,c)
def ciz(root,dx=1.7,dy=.85):
    ls=yap(root); Lm=max(len(yol_(root,l))-1 for l in ls); yp={l:-i*dy for i,l in enumerate(ls)}; out=[]
    def rec(n,d):
        if not n.kids: return (Lm*dx,yp[n.ad])
        ch=[rec(k,d+1) for k in n.kids]; x=d*dx; y=sum(c[1] for c in ch)/len(ch)
        out.append(f'\\draw[line width=1.2pt] ({x},{min(c[1] for c in ch)})--({x},{max(c[1] for c in ch)});')
        for k,(cx,cy) in zip(n.kids,ch):
            out.append(f'\\draw[line width=1.2pt] ({x},{cy})--({cx},{cy});')
            for j,m in enumerate(k.marks):
                xm=x+(cx-x)*(j+1)/(len(k.marks)+1)
                out.append(f'\\draw[line width=1.6pt] ({xm:.2f},{cy-.16:.2f})--({xm:.2f},{cy+.16:.2f});\\node[font=\\normalsize\\bfseries] at ({xm:.2f},{cy+.38:.2f}) {{{m}}};')
        return (x,y)
    rx,ry=rec(root,0); out.append(f'\\draw[line width=1.2pt] ({rx-.5},{ry})--({rx},{ry});')
    for l in ls: out.append(f'\\node[anchor=west,font=\\large\\bfseries] at ({Lm*dx+.12},{yp[l]}) {{{l}}};')
    return '\n'.join(out)

# ================= 0008 · dallanma şeması · akrabalık · kolay · öncüllü =================
R8=Nd('k',[Nd('a',[Nd('P'),Nd('R')]),Nd('b',[Nd('c',[Nd('S'),Nd('T')]),Nd('U')])])
assert yakin(R8,'P','R','S') and yakin(R8,'S','T','U') and not yakin(R8,'P','U','T') and not yakin(R8,'P','T','U')
d8={'I':(True,'P ve R’nin ortak atası P ve S’nin ortak atasından daha yakın noktada ayrılır; P, R’ye daha yakın akrabadır'),
    'II':(True,'S ve T’nin ortak atası, S ve U’nun ortak atasından daha yakın noktadadır; S, T’ye daha yakın akrabadır'),
    'III':(False,'P için T ve U ile ortak ata aynı noktadadır (kökteki ayrılma); U, P’ye T’den daha yakın değildir')}
r8=onc(d8,[0,1,2,3,4],'D')
SK8=tk(ciz(R8,1.6,.85),1.0)
q('08','dallan','orta','Akrabalık ilişkisi','Dallanma şemasında ortak atanın konumundan akrabalık derecesini değerlendirir.','şekilli',
  'Ortak atası daha yakın noktada olan iki tür daha yakın akrabadır.','Şemada yan yana yazılan türleri her zaman yakın akraba sanmak.','dallanma şeması ve akrabalık yargıları',
  [A('Şemayı oku','Dalların ayrıldığı noktalar ortak ataları gösterir.','P–R, S–T ayrı ortak atalar'),adim_onc(d8,['I']),adim_onc(d8,['II','III']),sonuc(d8,r8)],
  metin='Moleküler karşılaştırmalar sonucunda bir araştırma ekibi, P, R, S, T ve U adlı beş canlı türünün akrabalık ilişkilerini şekildeki dallanma şemasıyla göstermiştir. Dalların ayrıldığı noktalar ortak ataları temsil etmektedir.\nBuna göre,\nI. P türü, R türüne S türünden daha yakın akrabadır.\nII. S türü, T türüne U türünden daha yakın akrabadır.\nIII. U türü, P türüne T türünden daha yakın akrabadır.\nifadelerinden hangileri doğrudur?',
  dogru=r8['dogru'],yan=r8['yan'],sira=r8['sira'],istenen='Şemaya göre doğru olan ifadeler.',sekil=SK8,ip=['İki türün en yakın ortak atası hangi düğümdedir?'],
  bilgi=[DAL],puf='Ortak ata daha yeni ise akrabalık daha yakındır.')

# ================= 0009 · özellik izleme · sayı · zor =================
R9=Nd('k',[Nd('a',[Nd('A',marks=[5]),Nd('B')],[1]),Nd('b',[Nd('c',[Nd('C'),Nd('D',marks=[6])],[3]),Nd('e',[Nd('E'),Nd('F')],[4])],[2])])
F9=ozel(R9); assert F9=={'A':{1,5},'B':{1},'C':{2,3},'D':{2,3,6},'E':{2,4},'F':{2,4}}
d9=sum(1 for l,f in F9.items() if len(f)==2 and 2 in f)
y_a=sum(1 for l,f in F9.items() if f=={2,4}); y_b=sum(1 for f in F9.values() if len(f)==2); y_c=sum(1 for f in F9.values() if len(f)>=2); y_d=len(F9)
assert (y_a,d9,y_b,y_c,y_d)==(2,3,4,5,6)
SK9=tk(ciz(R9,1.5,.8),1.0)
q('09','dallan','zor','Özelliklerin soya aktarımı','Dallanma şemasında özelliklerin kökten türlere aktarılma yolunu izleyerek tür sayar.','şekilli',
  'Bir türün özellikleri, kökten o türe giden yoldaki tüm özelliklerdir; koşullar türlere tek tek uygulanarak sayılır.','Bir özelliği yalnız bulunduğu dalın ucundaki türe ait saymak.','özellik izleme ve sayma',
  [A('Her türün özelliklerini yaz','Kökten türe giden yoldaki numaralar o türe aittir.','A: 1, 5 · B: 1 · C: 2, 3 · D: 2, 3, 6 · E: 2, 4 · F: 2, 4'),
   A('Tam iki özelliklileri seç','Özellik sayısı iki olan türler ayrılır.','A, C, E, F'),
   A('2 numaralıyı ara','Bu türlerden hangileri 2 numaralı özelliği taşır?','C, E, F'),
   A('Sonucu yaz','Koşulu sağlayan tür sayısı sayılır.','3')],
  metin='Şekilde altı canlı türünün (A, B, C, D, E ve F) dallanma şeması ve dallar üzerinde ortaya çıkan özellikler (1, 2, 3, 4, 5 ve 6) gösterilmiştir. Her özellik yalnızca bir kez ortaya çıkmış, o daldan ayrılan bütün türlere aktarılmış ve hiçbir türde kaybolmamıştır.\nBuna göre tam olarak iki özelliğe sahip türlerden kaçı 2 numaralı özelliği taşır?',
  dogru=d9,yan=[(y_a,'Yalnız 2 ve 4 numaralı özelliklere sahip türleri (E ve F) saymış; C türünün 2 ve 3 numaralı özelliklere sahip olduğunu atlamış.','dikkat'),
                (y_b,'Tam iki özelliği olan bütün türleri saymış; A türünün 2 numaralı özelliğe sahip olmadığını denetlememiş.','dikkat'),
                (y_c,'Tam iki yerine en az iki saymış ve 2 numaralı özellik koşulunu atlamış; iki ya da daha çok özelliği olan A, C, D, E ve F türlerini saymış.','dikkat'),
                (y_d,'Koşulları uygulamayıp bütün türleri saymış.','dikkat')],
  istenen='Koşulu sağlayan tür sayısı.',sekil=SK9,ip=['Önce her türün özellik kümesini kökten türe giden yoldan yaz.'],bilgi=[DAL],puf='Önce her türün özellik listesini çıkar, sonra koşulları listeye uygula.')

# ================= 0010 · dallanma şeması · öncüllü · zor =================
R10=Nd('k',[Nd('a',[Nd('V'),Nd('W',marks=[4])],[1]),Nd('b',[Nd('X',marks=[5]),Nd('c',[Nd('Y'),Nd('Z')],[3])],[2])])
F10=ozel(R10); assert F10=={'V':{1},'W':{1,4},'X':{2,5},'Y':{2,3},'Z':{2,3}}
o1=len(F10['X']&F10['Y'])>len(F10['Y']&F10['Z']); o2=yakin(R10,'Y','X','V'); o3=lcad(R10,'Y','Z')>lcad(R10,'X','Y') and [l for l,f in F10.items() if 3 in f]==['Y','Z']
assert (o1,o2,o3)==(False,True,True)
d10={'I':(o1,'X ile Y’nin ortak özelliği yalnız 2 numaralıdır (1 tane); Y ile Z’nin ortak özellikleri 2 ve 3’tür (2 tane), yani Y–Z daha fazladır'),
     'II':(o2,'Y ile X’in ortak atası, Y ile V’nin ortak atasından daha yakın noktadadır; Y, X’e V’den daha yakın akrabadır'),
     'III':(o3,'Y ile Z’nin ortak atası X ile Y’nin ortak atasından daha yeni bir düğümdür ve 3 numaralı özellik yalnız Y ile Z’de bulunur')}
r10=onc(d10,[1,2,3,4,5],'E')
SK10=tk(ciz(R10,1.6,.85),1.0)
q('10','dallan','zor','Dallanma şeması yargıları','Dallanma şemasında akrabalık ve özellik paylaşımı yargılarını birlikte değerlendirir.','şekilli',
  'Ortak özellik sayısı iki türün kökten ayrıldıkları yola kadar paylaştıkları özelliklerdir; yakın akrabalık ortak atanın konumuyla ölçülür.','Yan yana çizilen türleri akraba sanmak ve özellik paylaşımını ortak atadan bağımsız saymak.','akrabalık ve ortak özellik yargıları',
  [A('Özellikleri yaz','Kökten türe giden yoldaki numaralar türe aittir.','V: 1 · W: 1, 4 · X: 2, 5 · Y: 2, 3 · Z: 2, 3'),adim_onc(d10,['I']),adim_onc(d10,['II','III']),sonuc(d10,r10)],
  metin='Beş canlı türünün (V, W, X, Y ve Z) dallanma şeması şekilde verilmiştir. Dallar üzerindeki 1, 2, 3, 4 ve 5 numaraları, o dalda ortaya çıkıp o daldan ayrılan bütün türlere aktarılan özellikleri göstermektedir; özellikler hiçbir türde kaybolmamıştır.\nBuna göre,\nI. X ile Y türlerinin ortak özellik sayısı, Y ile Z türlerinin ortak özellik sayısından fazladır.\nII. Y türü, X türüne V türünden daha yakın akrabadır.\nIII. Y ile Z türlerinin ortak atası, X ile Y türlerinin ortak atasından daha yakın zamanda yaşamıştır ve 3 numaralı özellik yalnız bu iki türde bulunur.\nifadelerinden hangileri doğrudur?',
  dogru=r10['dogru'],yan=r10['yan'],sira=r10['sira'],istenen='Şemaya göre doğru olan ifadeler.',sekil=SK10,ip=['Her türün özelliklerini yazıp ortak olanları say; akrabalığı ortak atanın yerinden değerlendir.'],bilgi=[DAL],puf='Ortak özellik sayısı ve akrabalık, kökten ayrılma noktasına bakılarak okunur.')

# ---------- dikotom anahtar çizimi ----------
KS=r'\tikzset{qn/.style={draw,rounded corners=3pt,align=center,inner sep=4pt,font=\small,line width=1pt,text width=3.9cm},lf/.style={draw,rounded corners=3pt,inner sep=5pt,font=\large\bfseries,line width=1.4pt,fill=black!6,minimum width=1.2cm}}'
def ke(a,b,t,yan='left'):
    return f'\\draw[line width=1pt,-{{Stealth[length=2mm]}}] ({a}) -- ({b}) node[midway,{yan},font=\\small\\bfseries,inner sep=2pt] {{{t}}};'
# ================= 0011 · omurgalı anahtarı · kolay =================
def calistir(dugum,props):
    """dugum: (soru_anahtar, evet, hayir) ya da str yaprak."""
    while not isinstance(dugum,str):
        dugum=dugum[1] if props[dugum[0]] else dugum[2]
    return dugum
AN11=('sabit',('sut','N','M'),('solungac','K','L'))
YUNUS=dict(sabit=True,sut=True,solungac=False); KURBAGA=dict(sabit=False,sut=False,solungac=False); PENGUEN=dict(sabit=True,sut=False,solungac=False)
assert (calistir(AN11,YUNUS),calistir(AN11,KURBAGA),calistir(AN11,PENGUEN))==('N','L','M')
K11='\n'.join([KS,
 r'\node[qn] (a) at (0,0) {Vücut sıcaklığı sabit mi?};',
 r'\node[qn] (b) at (-3.4,-2.1) {Yetişkin dönemde solungaç var mı?};',
 r'\node[qn] (c) at (3.4,-2.1) {Süt bezleri var mı?};',
 r'\node[lf] (k) at (-4.9,-4.2) {K};\node[lf] (l) at (-1.9,-4.2) {L};\node[lf] (m) at (1.9,-4.2) {M};\node[lf] (n) at (4.9,-4.2) {N};',
 ke('a.south west','b.north','Hayır','left'),ke('a.south east','c.north','Evet','right'),
 ke('b.south west','k.north','Evet','left'),ke('b.south east','l.north','Hayır','right'),
 ke('c.south west','m.north','Hayır','left'),ke('c.south east','n.north','Evet','right')])
SK11=tk(K11,.8)
Y11=[('K – L – M','Yunusu suda yaşadığı için balık sanmış; oysa yunusun süt bezleri vardır ve vücut sıcaklığı sabittir.','bilgi'),
     ('N – K – M','Kurbağanın yetişkin dönemde solungaçla solunduğunu sanmış; oysa yetişkin kurbağada solungaç yoktur.','bilgi'),
     ('M – L – N','Yunus ile penguenin yerini karıştırmış; süt bezi yunusta vardır, penguende yoktur.','dikkat'),
     ('K – L – N','Yunusu balık, penguenin memeli olduğunu sanmış; ikisi için de süt bezi bilgisini ters kullanmış.','bilgi')]
q('11','anahtar','orta','Omurgalı anahtarı','Dikotom anahtarı izleyerek omurgalıların hangi sınıfa ait olduğunu belirler.','şekilli',
  'Anahtar, canlıya ait özellikle yönlendirilerek sırayla işletilir; yaşam ortamı değil vücut özellikleri esastır.','Yunusu suda yaşadığı için balık saymak.','omurgalı dikotom anahtarı',
  [A('Yunus için anahtarı işlet','Vücut sıcaklığı sabit, süt bezleri var.','Sabit → Evet · Süt bezi → Evet'),A('Kurbağa için işlet','Vücut sıcaklığı sabit değil; yetişkinde solungaç yok.','Sabit → Hayır · Solungaç → Hayır'),A('Penguen için işlet','Vücut sıcaklığı sabit; süt bezi yok.','Sabit → Evet · Süt bezi → Hayır'),A('Harfleri yaz','Yaprak harfleri sırayla yazılır.','N – L – M')],
  metin='Bir öğrenci, balıklar, iki yaşamlılar, kuşlar ve memeliler olmak üzere dört omurgalı grubunu ayırt etmek için şekildeki dikotom anahtarı hazırlıyor. Anahtardaki K, L, M ve N harfleri bu dört gruptan birini göstermektedir. Öğrenci; yunus, kurbağa ve penguen için anahtarı sırayla işletiyor.\nBuna göre bu üç canlı sırasıyla hangi harflerle gösterilen gruptadır?',
  dogru='N – L – M',yan=Y11,sira=['N – L – M']+[y[0] for y in Y11],istenen='Yunus, kurbağa ve penguenin grup harfleri.',sekil=SK11,ip=['Her canlının vücut özelliklerini anahtarın sorularına tek tek yanıtla.'],bilgi=[DIK,OMG],puf='Anahtarda canlının yaşadığı yere değil özelliklerine bak.')

# ================= 0012 · bitki anahtarı · orta =================
AN12=('damar',('tohum',('meyve','N','M'),'L'),'K')
KARAYOSUNU=dict(damar=False,tohum=False,meyve=False); CAM=dict(damar=True,tohum=True,meyve=False); FASULYE=dict(damar=True,tohum=True,meyve=True); EGRELTI=dict(damar=True,tohum=False,meyve=False)
assert [calistir(AN12,x) for x in (KARAYOSUNU,CAM,FASULYE,EGRELTI)]==['K','M','N','L']
K12='\n'.join([KS,
 r'\node[qn] (a) at (0,0) {Damar (iletim) demeti var mı?};',
 r'\node[qn] (b) at (3.2,-2.0) {Tohum oluşturur mu?};',
 r'\node[qn] (c) at (6.4,-4.0) {Tohumlar meyve içinde mi?};',
 r'\node[lf] (k) at (-1.6,-2.0) {K};\node[lf] (l) at (0.2,-4.0) {L};\node[lf] (m) at (3.9,-6.0) {M};\node[lf] (n) at (8.2,-6.0) {N};',
 ke('a.south west','k.north','Hayır','left'),ke('a.south east','b.north','Evet','right'),
 ke('b.south west','l.north','Hayır','left'),ke('b.south east','c.north','Evet','right'),
 ke('c.south west','m.north','Hayır','left'),ke('c.south east','n.north','Evet','right')])
SK12=tk(K12,.8)
Y12=[('K – L – N','Çamı tohumsuz bir bitki grubuna koymuş; oysa çam tohum oluşturur ve tohumları meyve içinde değildir.','bilgi'),
     ('L – M – N','Karayosununu damarlı sanmış; oysa karayosununda iletim demeti yoktur.','bilgi'),
     ('K – N – M','Açık ve kapalı tohumluları karıştırmış; çamı kapalı, fasulyeyi açık tohumlu saymış.','bilgi'),
     ('K – M – M','Fasulyenin tohumlarını meyve içinde saymayıp çamla aynı gruba koymuş.','dikkat')]
q('12','anahtar','orta','Bitki anahtarı','Bitki gruplarını ayıran dikotom anahtarı işletir.','şekilli',
  'Anahtarın her basamağı bir grup ayrımını (damarlı/damarsız, tohumlu/tohumsuz, meyveli/meyvesiz) temsil eder.','Açık ve kapalı tohumluları karıştırmak.','bitki dikotom anahtarı',
  [A('Karayosunu için işlet','Damar demeti yok.','Damar → Hayır · K'),A('Çam için işlet','Damar demeti var, tohum var, tohumlar meyve içinde değil.','Damar → Evet · Tohum → Evet · Meyve → Hayır · M'),A('Fasulye için işlet','Damar demeti var, tohum var, tohumlar meyve içinde.','Damar → Evet · Tohum → Evet · Meyve → Evet · N'),A('Harfleri yaz','Üç canlının grup harfleri sırayla yazılır.','K – M – N')],
  metin='Bir botanikçi, damarsız tohumsuz, damarlı tohumsuz, açık tohumlu ve kapalı tohumlu bitkileri ayırt etmek için şekildeki dikotom anahtarı hazırlıyor. Anahtardaki K, L, M ve N harfleri bu dört gruptan birini göstermektedir. Botanikçi anahtarı karayosunu, çam ve fasulye bitkileri için sırayla işletiyor.\nBuna göre bu üç bitki sırasıyla hangi harflerle gösterilen gruptadır?',
  dogru='K – M – N',yan=Y12,sira=[Y12[1][0],Y12[0][0],'K – M – N',Y12[2][0],Y12[3][0]],istenen='Karayosunu, çam ve fasulyenin grup harfleri.',sekil=SK12,ip=['Her bitkiyi anahtarın üç sorusuna kendi özelliklerine göre yanıtlayarak ilerlet.'],bilgi=[DIK,BIT],puf='Bitkiyi anahtarın yönlendirmesine göre damar, tohum, meyve sırasıyla ilerlet.')

# ================= 0013 · anahtar eksik basamak · zor =================
S13=[("Omurgalıdır.",False,'dört sınıfın hepsi omurgalıdır; bu ifade memelileri sürüngenlerden ayırmaz'),
     ("Akciğerle solunum yapar.",False,'hem memeliler hem sürüngenler akciğerle solunur; ayırt edici değildir'),
     ("Kuru ve pullu bir deriye sahiptir.",False,'bu özellik sürüngenlere aittir; “Evet” yolunu memelilere götüremez'),
     ("Süt bezlerine sahiptir.",True,'süt bezleri yalnızca memelilerde bulunur'),
     ("Vücut sıcaklığı dış ortama göre değişir.",False,'bu özellik sürüngenlere aittir; “Evet” yolunu memelilere götüremez')]
d13,y13,s13=tek(S13,True)
K13='\n'.join([KS,
 r'\node[qn] (a) at (0,0) {Vücudu kuş tüyüyle örtülü mü?};',
 r'\node[qn] (b) at (3.2,-2.0) {Solungaçla\\solunum yapar mı?};',
 r'\node[qn] (c) at (6.4,-4.0) {?};',
 r'\node[lf] (k) at (-1.9,-2.0) {Kuşlar};\node[lf] (l) at (0.3,-4.0) {Balıklar};\node[lf] (m) at (3.9,-6.0) {Sürüngenler};\node[lf] (n) at (8.7,-6.0) {Memeliler};',
 ke('a.south west','k.north','Evet','left'),ke('a.south east','b.north','Hayır','right'),
 ke('b.south west','l.north','Evet','left'),ke('b.south east','c.north','Hayır','right'),
 ke('c.south west','m.north','Hayır','left'),ke('c.south east','n.north','Evet','right')])
SK13=tk(K13,.8)
q('13','anahtar','zor','Anahtar basamağı kurma','Dikotom anahtarda bir basamağın iki yolu doğru ayıracak ifadesini belirler.','şekilli',
  'Basamaktaki ifade, “Evet” yolundaki grubun tamamında bulunmalı, “Hayır” yolundaki grupta bulunmamalıdır.','Yalnız doğru bir özelliği seçip ayırt edici olup olmadığına bakmamak.','anahtarda eksik basamak',
  [A('Basamağa ulaşanları bul','Tüylü olanlar ve solungaçla solunanlar önceki basamaklarda ayrılmıştır.','Kalanlar: memeliler ve sürüngenler'),A('Evet yolunu belirle','“Evet” yolu memelilere gitmelidir; ifade memelilerde olmalı, sürüngenlerde olmamalıdır.','Evet → memeliler'),A('Seçenekleri ele','Omurgalı olmak ve akciğerle solunum iki grupta da vardır; pul ve değişken sıcaklık sürüngenlere özgüdür.','Ayırt edici değil · ters grup'),A('Sonucu yaz','Yalnızca memelilere özgü özellik süt bezleridir.','Süt bezleri')],
  metin='Bir öğrenci, balıklar, kuşlar, memeliler ve sürüngenler olmak üzere dört omurgalı sınıfını ayırt etmek için şekildeki dikotom anahtarı hazırlıyor. Son basamağı henüz yazmayan öğrenci, “?” yerine yazılacak ifadenin “Evet” seçeneğinde memelilere, “Hayır” seçeneğinde sürüngenlere ulaşılacak biçimde seçilmesi gerektiğini belirtiyor.\nBuna göre “?” yerine aşağıdakilerden hangisi yazılmalıdır?',
  dogru=d13,yan=y13,sira=s13,istenen='“?” yerine yazılacak doğru ifade.',sekil=SK13,ip=['Bu basamağa hangi iki grup ulaşıyor ve “Evet” yolu yalnız hangisine gitmeli?'],bilgi=[DIK,OMG],puf='Anahtar basamağı yalnız o basamağa gelen grupları kesin ayırmalıdır.')

# ================= 0014 · âlem özellik tablosu · orta =================
T14=tablo_svg(['Grup','Çekirdek zarı','Hücre duvarı','Beslenme','Hücre sayısı'],[
 ['K','Yok','Var','Ototrof/heterotrof','Tek hücreli'],['L','Var','Yok','Heterotrof','Çok hücreli'],
 ['M','Var','Kitin yapılı','Heterotrof','Tek ya da çok'],['N','Var','Bazılarında var','Ototrof/heterotrof','Tek ya da çok']])
D14='Bakteriler – Hayvanlar – Mantarlar – Protista'
Y14=[('Bakteriler – Hayvanlar – Protista – Mantarlar','Kitin yapılı hücre duvarını ve yalnız heterotrof beslenmeyi mantarlara özgü saymamış; M ile N’yi karıştırmış.','bilgi'),
     ('Protista – Hayvanlar – Mantarlar – Bakteriler','Çekirdek zarı bulunmayan grubun prokaryot, yani bakteri olduğunu atlamış.','bilgi'),
     ('Bakteriler – Mantarlar – Hayvanlar – Protista','Hücre duvarı bulunmayan çok hücreli grubu mantar sanmış; hayvanlarda hücre duvarı yoktur.','bilgi'),
     ('Hayvanlar – Bakteriler – Mantarlar – Protista','K ile L’yi karıştırmış; çekirdek zarsız ve duvarlı grup bakterilerdir, hayvanlar hücre duvarsızdır.','dikkat')]
q('14','alem','orta','Âlemlerin özellikleri','Hücre tipi, duvar, beslenme ve hücre sayısı özelliklerinden âlemi belirler.','tablo',
  'Çekirdek zarı prokaryot–ökaryot ayrımını, hücre duvarının yapısı ise ökaryot âlemlerini ayırır.','Kitin ve selüloz ya da duvarsızlık bilgisini karıştırmak.','âlem özellikleri tablosu',
  [A('Prokaryotu bul','Çekirdek zarı olmayan grup bakterilerdir.','K: Bakteriler'),A('Duvarsız grubu bul','Hücre duvarı olmayan heterotrof çok hücreli grup hayvanlardır.','L: Hayvanlar'),A('Kitinli grubu bul','Kitin yapılı duvarlı heterotrof ökaryot mantarlardır.','M: Mantarlar'),A('Kalanı yaz','Kalan ökaryot grup, ototrof beslenebilen protistadır.','N: Protista')],
  metin='Aşağıdaki tabloda bakteriler, protista, mantarlar ve hayvanlar âlemlerine ait dört canlı grubunun (K, L, M ve N) bazı özellikleri verilmiştir. Gruplar bu dört âlemden birine ait olup her âlem yalnız bir kez kullanılmıştır.\nBuna göre K, L, M ve N gruplarının ait olduğu âlemler sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
  dogru=D14,yan=Y14,sira=[Y14[0][0],D14,Y14[1][0],Y14[2][0],Y14[3][0]],istenen='K, L, M ve N gruplarının âlemleri.',sekil=T14,ip=['Önce çekirdek zarına, sonra hücre duvarının yapısına bak.'],bilgi=[ALM],puf='Çekirdek zarı, hücre duvarı ve beslenme türü birlikte âlemi belirler.')

# ================= 0015 · virüsler · öncüllü olumsuz · orta =================
d15={'I':(True,'virüsler hücresel yapıda değildir ve konak hücre dışında canlılık belirtisi göstermez'),
     'II':(False,'virüsler hücresel yapıda olmadığından sınıflandırmada yer alan âlemlerin hiçbirine dahil edilmez'),
     'III':(False,'antibiyotikler bakterilere etki eder; virüslerin çoğalmasını engellemez')}
r15=onc(d15,[1,2,3,4,5],'E',ara=False)
q('15','alem','orta','Virüsler','Virüslerin hücresel yapıda olmadığını ve âlemlerin dışında kaldığını bilir.','öncüllü',
  'Virüsler konak hücre içinde çoğalır, hücresel yapı göstermez ve âlemlerde yer almaz; antibiyotik bakteriye etki eder.','Virüsleri bakteri gibi antibiyotikle tedavi edilebilir saymak.','virüslerle ilgili yargılar',
  [adim_onc(d15,['I']),adim_onc(d15,['II','III']),sonuc(d15,r15,False)],
  metin='Grip belirtileriyle hastaneye giden bir hastaya doktor, hastalığın bir virüsten kaynaklandığını söylemiştir. Hasta, virüsleri merak etmiş ve araştırarak kendi notlarına şu yargıları yazmıştır:\nI. Virüsler, konak hücre dışında canlılık belirtisi göstermez.\nII. Virüsler, sınıflandırmada yer alan âlemlerden birine dahildir.\nIII. Antibiyotikler virüslerin çoğalmasını engeller.\nBuna göre bu yargılardan hangileri yanlıştır?',
  dogru=r15['dogru'],yan=r15['yan'],sira=r15['sira'],istenen='Yanlış olan yargılar.',ip=['Virüslerin hücresel yapısını ve sınıflandırmadaki yerini düşün.'],bilgi=[VIR],puf='Virüs hücre değildir: âlemlerde yoktur ve antibiyotikten etkilenmez.')

# ================= 0016 · arkeler · öncüllü · orta =================
d16={'I':(True,'arkeler de bakteriler gibi prokaryot hücrelidir'),
     'II':(False,'arkeler bakterilerin bir alt grubu değildir; ayrı bir âlemde incelenir'),
     'III':(True,'bazı arkeler aşırı tuzlu, sıcak ya da asidik gibi uç ortamlarda yaşayabilir')}
r16=onc(d16,[2,3,4,5,6],'C')
q('16','alem','orta','Arkeler','Arkelerin hücre tipini ve sınıflandırmadaki yerini bilir.','öncüllü',
  'Arkeler prokaryottur ve bakterilerden ayrı bir âlemdir; bazıları uç ortamlarda yaşar.','Arkeleri bakterilerin içinde saymak.','arkeler hakkında yargılar',
  [adim_onc(d16,['I']),adim_onc(d16,['II']),adim_onc(d16,['III']),sonuc(d16,r16)],
  metin='Bir araştırma ekibi, aşırı tuzlu bir göl suyundan tek hücreli bir canlı izole ediyor. Canlının hücresinde çekirdek zarı ve zarlı organeller bulunmuyor. Ekip, bu canlıyı arkeler âlemine yerleştiriyor ve arkelerle ilgili şu yargıları not alıyor:\nI. Arkeler prokaryot hücrelidir.\nII. Arkeler, bakteriler âleminin bir alt grubudur.\nIII. Arkelerin bazı üyeleri aşırı tuzlu ya da çok sıcak gibi uç ortamlarda yaşayabilir.\nBuna göre bu yargılardan hangileri doğrudur?',
  dogru=r16['dogru'],yan=r16['yan'],sira=r16['sira'],istenen='Doğru olan yargılar.',ip=['Arkelerin hücre yapısını ve sınıflandırmadaki konumunu hatırla.'],bilgi=[ARK],puf='Arkeler prokaryottur ama bakterilerden ayrı bir âlemdir.')

# ================= 0017 · mantar · kolay · düz =================
D17='Mantarlar'
Y17=[('Bakteriler','Çekirdek zarı olan bir canlıyı bakteri sanmış; oysa bakteriler prokaryottur, çekirdek zarı yoktur.','bilgi'),
     ('Bitkiler','Hücre duvarı olduğu için bitki sanmış; oysa bitkilerde duvar selülozdur ve kendi besinini üretirler.','bilgi'),
     ('Hayvanlar','Heterotrof beslenmeyi hayvanlara özgü saymış; oysa hayvan hücrelerinde hücre duvarı yoktur.','bilgi'),
     ('Protista','Çekirdek zarlı tek hücreli canlıları protista sanmış; kitinli duvar ve hücre dışı sindirim mantarlara özgüdür.','bilgi')]
q('17','alem','kolay','Mantarlar','Hücre duvarı ve beslenme biçiminden mantarlar âlemini tanır.','düz',
  'Çekirdek zarlı, kitin duvarlı, heterotrof ve hücre dışında sindirim yapan canlı mantardır.','Kitin duvarı bitkilerdeki selülozla karıştırmak.','mantar özelliklerinden âlem belirleme',
  [A('Hücre tipini yorumla','Çekirdek zarının olması canlının ökaryot olduğunu gösterir.','Ökaryot'),A('Duvarı yorumla','Duvarın kitin olması mantarlar âlemini düşündürür.','Kitin duvar'),A('Beslenmeyi yorumla','Kloroplast yok; besin hücre dışında sindirilip emiliyor.','Heterotrof, hücre dışı sindirim'),A('Sonucu yaz','Üç özellik birlikte mantarları gösterir.','Mantarlar')],
  metin='Nemli bir ekmek parçası üzerinde gelişen tüylü bir küf tabakasını mikroskopta inceleyen bir öğrenci şu gözlemleri yazıyor: Hücrelerde çekirdek zarı var. Hücre duvarı kitinden oluşuyor. Kloroplast yok; canlı, salgıladığı sindirim enzimleriyle ekmeği hücre dışında parçalayıp emerek besleniyor.\nBuna göre bu canlı aşağıdaki âlemlerden hangisinde yer alır?',
  dogru=D17,yan=Y17,sira=[D17]+[y[0] for y in Y17],istenen='Canlının ait olduğu âlem.',ip=['Hücre duvarının yapısı ve besini nerede sindirdiği hangi grubu ayırır?'],bilgi=[ALM],puf='Kitin duvar + heterotrof + hücre dışı sindirim = mantar.')

# ================= 0018 · bitki iç içe küme · orta =================
def pt(x,y,ad,sol=False):
    return f'\\fill ({x},{y}) circle (.09);\\node[anchor={"east" if sol else "west"},font=\\normalsize] at ({x+(-.15 if sol else .15)},{y}) {{{ad}}};'
K18='\n'.join([r'\draw[line width=1.3pt] (0,0) ellipse (5.9 and 2.9);',r'\draw[line width=1.3pt] (1.4,-.1) ellipse (3.9 and 2.05);',r'\draw[line width=1.3pt] (3.0,-.1) ellipse (1.65 and 1.2);',
 pt(-5.3,.9,'Karayosunu'),pt(-1.55,-.55,'Eğrelti otu'),pt(2.2,.3,'Ladin')+pt(2.2,-.7,'Lahana'),
 r'\node[font=\large\bfseries] at (-3.9,-1.7) {1};\node[font=\large\bfseries] at (.3,-1.35) {2};\node[font=\large\bfseries] at (4.1,-.1) {3};'])
SK18=tk(K18,.7)
D18='1: Hücre duvarı selülozdur; 2: İletim (damar) demeti bulunur; 3: Tohum oluşturur.'
Y18=[('1: Tohum oluşturur; 2: İletim (damar) demeti bulunur; 3: Hücre duvarı selülozdur.','Dört bitkinin tamamında bulunan özelliği tohum sanmış; oysa karayosunu tohum oluşturmaz.','bilgi'),
     ('1: Hücre duvarı selülozdur; 2: Tohum oluşturur; 3: Tohumları meyve içindedir.','2. kümede tohumsuz bir bitki (eğrelti otu) olduğunu görmemiş; ladinin tohumlarının da meyve içinde olmadığını atlamış.','dikkat'),
     ('1: Hücre duvarı kitindir; 2: İletim (damar) demeti bulunur; 3: Tohum oluşturur.','Kitin duvarını bitkiler için yazmış; oysa kitin mantarların hücre duvarını yapar.','bilgi'),
     ('1: Hücre duvarı selülozdur; 2: Çiçek ve meyve oluşturur; 3: Tohum oluşturur.','Çiçek ve meyvenin eğrelti otunda ve ladinde bulunmadığını atlamış.','dikkat')]
q('18','bitki','orta','Bitki gruplarının ortak özellikleri','İç içe küme şemasında bitki gruplarının ortak özelliklerini belirler.','şekilli',
  'Küme içindeki tüm bitkilerin ortak özelliği o kümenin özelliğidir; içeri girdikçe ortak özellik artar.','Bir kümedeki bazı bitkilerde olan özelliği kümenin ortak özelliği saymak.','bitki kümeleri ve ortak özellikler',
  [A('Kümeleri oku','Dört bitki 1. kümede; eğrelti otu, ladin ve lahana 2. kümede; ladin ve lahana 3. kümededir.','1 ⊃ 2 ⊃ 3'),A('1. kümenin özelliğini bul','Dört bitkinin ortak özelliği: hücre duvarı selülozdur.','1: selüloz duvar'),A('2. ve 3. kümeyi bul','Karayosununda olmayan, diğer üçünde olan özellik damar demetidir; yalnız ladin ve lahanada olan özellik tohumdur.','2: damar demeti · 3: tohum'),A('Eşleştirmeyi yaz','Üç eşleşme birlikte doğru olan seçeneği verir.','Sonuç bulundu')],
  metin='Şekilde dört bitki (karayosunu, eğrelti otu, ladin ve lahana) ve bu bitkilerin ait olduğu gruplar iç içe kümelerle gösterilmiştir. Her küme, içinde bulunan bitkilerin tamamında ortak olan bir özelliği temsil etmektedir.\nBuna göre 1, 2 ve 3 numaralı kümelerin temsil ettiği ortak özellikler aşağıdakilerden hangisinde doğru verilmiştir?',
  dogru=D18,yan=Y18,sira=[Y18[0][0],Y18[1][0],Y18[2][0],D18,Y18[3][0]],istenen='1, 2 ve 3 numaralı kümelerin ortak özellikleri.',sekil=SK18,ip=['Her kümenin, içindeki bütün bitkilerde ortak olan özelliği gösterdiğini düşün.'],bilgi=[BIT],puf='İç içe kümede ortak özellik, kümenin içindeki en kısıtlı canlı grubuna göre belirlenir.')

# ================= 0019 · bitki grupları · öncüllü olumsuz · orta =================
d19={'I':(True,'karayosunları iletim demeti taşımayan, damarsız bitkilerdir'),
     'II':(False,'eğrelti otları damarlıdır ancak tohum oluşturmaz; sporla çoğalır'),
     'III':(True,'çam açık tohumludur; tohumları meyve içinde değil, kozalak pulları üzerinde bulunur')}
r19=onc(d19,[0,1,2,3,4],'B',ara=False)
q('19','bitki','kolay','Bitki grupları','Karayosunu, eğrelti otu ve çamın özelliklerini karşılaştırır.','öncüllü',
  'Damar demeti ve tohum, bitki gruplarını ayıran iki ölçüttür; eğrelti damarlıdır ama tohumsuzdur.','Damarlı bitkilerin tohumla çoğaldığını sanmak.','bitki gruplarıyla ilgili yargılar',
  [adim_onc(d19,['I']),adim_onc(d19,['II']),adim_onc(d19,['III']),sonuc(d19,r19,False)],
  metin='Bir orman gezisinde öğrenciler, kayalar üzerindeki karayosunlarını, dere kenarındaki eğrelti otlarını ve yamaçtaki çam ağaçlarını inceliyor. Öğretmen, bu üç bitki grubuyla ilgili aşağıdaki yargıları yazıp öğrencilerden hatalı olanları bulmalarını istiyor:\nI. Karayosunları damarsız bitkilerdir.\nII. Eğrelti otları tohumla çoğalan damarlı bitkilerdir.\nIII. Çam ağacının tohumları meyve içinde bulunmaz.\nBuna göre bu yargılardan hangileri yanlıştır?',
  dogru=r19['dogru'],yan=r19['yan'],sira=r19['sira'],istenen='Yanlış olan yargılar.',ip=['Damar ve tohum ölçütlerini her bitki grubuna ayrı ayrı uygula.'],bilgi=[BIT],puf='Damarlı olmak tohumlu olmak demek değildir: eğrelti damarlı ama tohumsuzdur.')

# ================= 0020 · açık tohumlu · kolay =================
D20='Açık tohumlu bitkiler'
Y20=[('Damarsız tohumsuz bitkiler','Kozalaklı bir ağacı karayosunu sanmış; oysa karayosununda tohum ve iletim demeti yoktur.','bilgi'),
     ('Damarlı tohumsuz bitkiler','Damarlı olmasına bakıp tohum oluşturduğunu atlamış; eğrelti otları tohumsuzdur.','dikkat'),
     ('Kapalı tohumlu bitkiler','Tohumlu bitkiyi kapalı tohumlu sanmış; oysa tohumları meyve içinde değildir.','bilgi'),
     ('Mantarlar','Bir bitkiyi mantarlar âlemine koymuş; oysa kozalaklı ağaç ototroftur ve duvarı selülozdur.','bilgi')]
q('20','bitki','kolay','Tohumlu bitkiler','Tohumların yerleşimine göre açık tohumlu bitkileri belirler.','düz',
  'Tohumlar meyve içinde değilse bitki açık tohumludur.','Tohumlu bitkilerin hepsini kapalı tohumlu saymak.','kozalaklı bitkinin grubu',
  [A('Tohumu yorumla','Bitki tohum oluşturur, damar demeti vardır.','Tohumlu damarlı bitki'),A('Tohum yerini yorumla','Tohumlar kozalak pulları üzerinde açıkta; meyve ya da çiçek yok.','Meyve içinde değil'),A('Grubu seç','Tohumları meyve içinde olmayan tohumlu bitkiler açık tohumludur.','Açık tohumlular')],
  metin='Dağ yamacındaki bir ağaçtan toplanan kozalaklı bir dalı inceleyen öğrenci, kozalak pullarının üzerinde tohumlar bulunduğunu, bu tohumların hiçbir meyve içinde yer almadığını ve ağacın çiçek oluşturmadığını not ediyor.\nBuna göre bu ağaç aşağıdaki gruplardan hangisine aittir?',
  dogru=D20,yan=Y20,sira=[y[0] for y in Y20]+[D20],istenen='Bitkinin ait olduğu grup.',ip=['Tohumun bulunduğu yeri tohumlu bitkilerin gruplandırılmasıyla ilişkilendir.'],bilgi=[BIT],puf='Meyve içinde tohum = kapalı tohumlu; meyvesiz kozalak tohumu = açık tohumlu.')

# ================= 0021 · omurgalı tablosu · orta =================
T21=tablo_svg(['Grup','Vücut sıcaklığı','Kalp','Yetişkin solunum','Vücut örtüsü'],[
 ['K','Değişken','2 odacıklı','Solungaç','Pul'],['L','Değişken','3 odacıklı','Akciğer ve deri','Nemli çıplak deri'],['M','Sabit','4 odacıklı','Akciğer','Tüy'],['N','Sabit','4 odacıklı','Akciğer','Kıl']])
D21='Balıklar – İki yaşamlılar – Kuşlar – Memeliler'
Y21=[('Balıklar – İki yaşamlılar – Memeliler – Kuşlar','Kıl ve tüyü karıştırmış; tüy kuşlara, kıl memelilere aittir.','dikkat'),
     ('İki yaşamlılar – Balıklar – Kuşlar – Memeliler','Kalbin odacık sayısını karıştırmış; 2 odacıklı kalp balıklarda, 3 odacıklı kalp iki yaşamlılarda bulunur.','bilgi'),
     ('Balıklar – Sürüngenler – Kuşlar – Memeliler','Nemli çıplak deriyi sürüngenlere atfetmiş; sürüngenlerin derisi kuru ve pulludur.','bilgi'),
     ('Balıklar – İki yaşamlılar – Kuşlar – Sürüngenler','Sabit vücut sıcaklığı ve kıl bilgisini atlayıp N’yi sürüngen saymış; sürüngenlerin sıcaklığı değişkendir.','bilgi')]
q('21','hayvan','orta','Omurgalı sınıfları','Omurgalı sınıflarını vücut sıcaklığı, kalp yapısı, solunum ve vücut örtüsü özelliklerinden ayırt eder.','tablo',
  'Kalp odacık sayısı, solunum organı ve vücut örtüsü omurgalı sınıflarını birbirinden ayırır.','Kuş ve memeliyi ya da iki yaşamlı ve sürüngeni karıştırmak.','omurgalı sınıf özellikleri tablosu',
  [A('Değişken sıcaklıkları ayır','K ve L değişken sıcaklıklıdır; K’nin solungacı ve 2 odacıklı kalbi var.','K: Balıklar'),A('L’yi bul','3 odacıklı kalp, akciğer ve deri solunumu, nemli çıplak deri.','L: İki yaşamlılar'),A('Sabit sıcaklıkları ayır','M ve N sabit sıcaklıklı; tüy kuşlarda, kıl memelilerde bulunur.','M: Kuşlar · N: Memeliler'),A('Sırayla yaz','K, L, M, N sırasıyla.','Balıklar – İki yaşamlılar – Kuşlar – Memeliler')],
  metin='Aşağıdaki tabloda balıklar, iki yaşamlılar, sürüngenler, kuşlar ve memeliler sınıflarından dördüne ait (K, L, M ve N) bazı özellikler verilmiştir. Her sınıf tabloda en çok bir kez yer almaktadır.\nBuna göre K, L, M ve N gruplarının ait olduğu omurgalı sınıfları sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
  dogru=D21,yan=Y21,sira=[D21]+[y[0] for y in Y21],istenen='K, L, M ve N’nin omurgalı sınıfları.',sekil=T21,ip=['Önce vücut sıcaklığı değişken olanlarla sabit olanları ayır.'],bilgi=[OMG],puf='Kalp odacığı: balık 2, iki yaşamlı 3, kuş ve memeli 4.')

# ================= 0022 · yarasa-yunus-penguen · öncüllü olumsuz · orta =================
d22={'I':(True,'yarasa uçsa da memelidir; vücudu kıllıdır ve yavrularını sütle besler'),
     'II':(True,'yunus suda yaşasa da memelidir; akciğerle solunur ve yavrusunu sütle besler'),
     'III':(False,'penguen uçamasa da kuştur; tüyleri ve gagası vardır, vücut sıcaklığı sabittir')}
r22=onc(d22,[0,1,2,3,4],'C',ara=False)
q('22','hayvan','orta','Omurgalı sınıfları','Yaşam ortamı ve hareket biçimine değil, ayırt edici özelliklere göre omurgalıları sınıflar.','öncüllü',
  'Omurgalı sınıfı yaşanılan ortama ya da uçma yeteneğine değil, vücut yapısına bakılarak belirlenir.','Suda yaşayan her canlıyı balık, uçan her canlıyı kuş saymak.','yarasa, yunus ve penguen',
  [adim_onc(d22,['I']),adim_onc(d22,['II']),adim_onc(d22,['III']),sonuc(d22,r22,False)],
  metin='Bir belgesel yapımcısı, yarasa, yunus ve penguen hakkında hazırladığı bölümde izleyicilere şu ifadeleri okuyor:\nI. Yarasa uçabilmesine rağmen memelidir.\nII. Yunus suda yaşamasına rağmen memelidir.\nIII. Penguen uçamadığı için kuş sayılmaz.\nBuna göre bu ifadelerden hangileri yanlıştır?',
  dogru=r22['dogru'],yan=r22['yan'],sira=r22['sira'],istenen='Yanlış olan ifadeler.',ip=['Her canlının hangi vücut özellikleriyle sınıflandırıldığını düşün.'],bilgi=[OMG],puf='Omurgalı sınıfı vücut özelliklerine bakılarak belirlenir; ortam ya da uçma ölçüt değildir.')

# ================= 0023 · böcek-örümcek · kolay · düz =================
D23='X: Arı – Y: Örümcek'
Y23=[('X: Karınca – Y: Kelebek','İki canlıyı da böcek sanmış; Y’nin 8 bacaklı ve antensiz olması örümceksilere özgüdür.','bilgi'),
     ('X: Akrep – Y: Örümcek','Altı bacaklı X’i örümceksi saymış; 6 bacak ve 3 vücut bölümü böceklere özgüdür.','bilgi'),
     ('X: Örümcek – Y: Arı','X ile Y’nin gruplarını ters eşleştirmiş; böceklerde 6, örümceksilerde 8 bacak vardır.','dikkat'),
     ('X: Örümcek – Y: Akrep','İki canlıyı da örümceksi sanmış; 6 bacaklı, anten taşıyan X bir böcektir.','bilgi')]
q('23','hayvan','kolay','Eklembacaklılar','Bacak sayısı, anten ve vücut bölümü özelliklerinden böcek ve örümceksileri ayırır.','düz',
  'Böcekler 3 çift bacaklı, antenli ve 3 bölümlü; örümceksiler 4 çift bacaklı, antensiz ve 2 bölümlüdür.','Örümceği böcek saymak.','eklembacaklı özellikleri',
  [A('X’i yorumla','6 bacak, 1 çift anten ve 3 vücut bölümü böceklerin özelliğidir.','X: böcek'),A('Y’yi yorumla','8 bacak, anten yok, 2 vücut bölümü örümceksilerin özelliğidir.','Y: örümceksi'),A('Çiftleri ele','Önce X’in böcek olduğu seçenekleri ayır, sonra Y’nin örümceksi olduğunu denetle.','Arı: böcek · Örümcek: örümceksi'),A('Sonucu yaz','İki koşulu birlikte sağlayan eşleşme seçilir.','X: Arı – Y: Örümcek')],
  metin='Bahçede iki eklembacaklı canlıyı (X ve Y) büyüteçle inceleyen bir öğrenci şunları not ediyor: X canlısının 6 bacağı, 1 çift anteni ve 3 vücut bölümü var. Y canlısının ise 8 bacağı var, anteni yok ve vücudu 2 bölümden oluşuyor.\nBuna göre X ve Y canlıları aşağıdaki eşleşmelerden hangisinde doğru verilmiştir?',
  dogru=D23,yan=Y23,sira=[Y23[0][0],Y23[1][0],Y23[2][0],D23,Y23[3][0]],istenen='X ve Y canlılarının doğru eşleşmesi.',ip=['Verilen özelliklerin hangi eklembacaklı grubuna ait olduğunu düşün.'],bilgi=[OMS],puf='6 bacak ve anten = böcek; 8 bacak ve antensiz = örümceksi.')

# ================= 0024 · ekolojik ve ekonomik önem · orta =================
S24=[("Fitoplanktonlar, besin zincirinde ayrıştırıcı olarak görev yapar.",False,'fotosentez yapan fitoplanktonlar besin zincirinin üreticisidir'),
     ("Penicillium türü küf mantarlarından antibiyotik elde edilir.",True,'penisilin adlı antibiyotik bu mantardan elde edilir'),
     ("Likenler, iki farklı bakteri türünün ortak yaşamından oluşur.",False,'likenler bir mantar ile bir alg ya da siyanobakterinin ortak yaşamıdır'),
     ("Ekmek mayası fotosentez yaparak kendi besinini üretir.",False,'ekmek mayası heterotroftur; ekmeği fermantasyonla (CO₂ üretimiyle) kabartır, fotosentez yapmaz'),
     ("Virüsler, besin zincirinde üretici basamağında yer alır.",False,'virüsler hücresel yapıda olmadığından besin zincirinde üretici sayılmaz')]
d24,y24,s24=tek(S24,True)
q('24','onem','orta','Ekonomik ve ekolojik önem','Bakteri, mantar ve protistaların ekonomik ve ekolojik önemini doğru örneklerle ilişkilendirir.','düz',
  'Üretici, ayrıştırıcı ve ekonomik kullanım örnekleri doğru gruplarla eşleştirilir.','Likeni bakteri topluluğu ya da mayayı fotosentetik saymak.','canlıların önemiyle ilgili tek doğru ifade',
  [A('Üretici protistaları ele','Fotosentez yapan fitoplanktonlar üreticidir; ayrıştırıcı değildir.','Fitoplankton: üretici'),A('Mantarları ele','Likenler mantar–alg ortaklığıdır; maya heterotroftur; Penicillium antibiyotik kaynağıdır.','Penicillium: antibiyotik'),A('Virüsleri ele','Virüsler hücre değildir; üretici olamaz.','Üretici değil'),A('Doğruyu seç','Tek doğru ifade Penicillium ile ilgili olandır.','Penicillium')],
  metin='Bir gıda teknolojisi öğrencisi, bazı canlı gruplarının ekonomik ve ekolojik önemini anlatan bir poster hazırlamaktadır. Posterde yer alacak bilgilerden yalnızca birinin doğru olduğunu fark eden danışman öğretmen, öğrenciden o bilgiyi bulmasını istemektedir.\nBuna göre posterde yer alabilecek doğru bilgi aşağıdakilerden hangisidir?',
  dogru=d24,yan=y24,sira=s24,istenen='Doğru olan bilgi.',ip=['Her canlı grubunun besin zincirindeki yerini ve insanın yararlandığı ürünleri düşün.'],bilgi=[ONEM],puf='Fotosentetik canlı üretici, mantar–bakteri ayrıştırıcıdır; Penicillium antibiyotiğin kaynağıdır.')

bitir(P,'siniflandirmaiki',UK)
